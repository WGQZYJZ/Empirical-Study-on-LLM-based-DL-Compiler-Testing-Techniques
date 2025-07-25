import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
const_60 = relay.const(-3.817513, dtype = "float64")#candidate|60|()|const|float64
const_61 = relay.const([[[-2.225999,0.545833,-5.142861,9.409868,-1.269783,-8.720379]],[[-8.795201,8.007037,4.955176,8.926987,7.350359,5.399013]],[[-0.721667,0.464173,-9.188401,-8.658683,-8.773053,9.306111]],[[-9.484202,-7.018543,-2.868757,0.918406,-1.945192,-5.357904]],[[-0.425427,-3.079269,-4.645286,7.411556,-9.224646,8.130138]],[[3.519788,5.688038,2.462390,-4.155965,3.632091,-8.254347]]], dtype = "float64")#candidate|61|(6, 1, 6)|const|float64
bop_62 = relay.power(const_60.astype('float64'), const_61.astype('float64')) # shape=(6, 1, 6)
bop_67 = relay.multiply(const_60.astype('int64'), bop_62.astype('int64')) # shape=(6, 1, 6)
uop_80 = relay.sigmoid(bop_62.astype('float32')) # shape=(6, 1, 6)
output = relay.Tuple([bop_67,uop_80,])
output2 = relay.Tuple([bop_67,uop_80,])
func_93 = relay.Function([], output)
mod['func_93'] = func_93
mod = relay.transform.InferType()(mod)
mutated_mod['func_93'] = func_93
mutated_mod = relay.transform.InferType()(mutated_mod)
func_93_call = mutated_mod.get_global_var('func_93')
call_94 = func_93_call()
output = call_94
func_95 = relay.Function([], output)
mutated_mod['func_95'] = func_95
mutated_mod = relay.transform.InferType()(mutated_mod)
func_93_call = mod.get_global_var('func_93')
func_95_call = mutated_mod.get_global_var('func_95')
call_98 = relay.TupleGetItem(func_93_call(), 0)
call_99 = relay.TupleGetItem(func_95_call(), 0)
func_93_call = mod.get_global_var('func_93')
func_95_call = mutated_mod.get_global_var('func_95')
call_102 = relay.TupleGetItem(func_93_call(), 1)
call_103 = relay.TupleGetItem(func_95_call(), 1)
uop_110 = relay.log(call_102.astype('float64')) # shape=(6, 1, 6)
uop_112 = relay.log(call_103.astype('float64')) # shape=(6, 1, 6)
func_93_call = mod.get_global_var('func_93')
func_95_call = mutated_mod.get_global_var('func_95')
call_113 = relay.TupleGetItem(func_93_call(), 0)
call_114 = relay.TupleGetItem(func_95_call(), 0)
output = relay.Tuple([call_98,uop_110,call_113,])
output2 = relay.Tuple([call_99,uop_112,call_114,])
func_119 = relay.Function([], output)
mod['func_119'] = func_119
mod = relay.transform.InferType()(mod)
mutated_mod['func_119'] = func_119
mutated_mod = relay.transform.InferType()(mutated_mod)
func_119_call = mutated_mod.get_global_var('func_119')
call_120 = func_119_call()
output = call_120
func_121 = relay.Function([], output)
mutated_mod['func_121'] = func_121
mutated_mod = relay.transform.InferType()(mutated_mod)
func_119_call = mod.get_global_var('func_119')
func_121_call = mutated_mod.get_global_var('func_121')
call_136 = relay.TupleGetItem(func_119_call(), 0)
call_137 = relay.TupleGetItem(func_121_call(), 0)
func_93_call = mod.get_global_var('func_93')
func_95_call = mutated_mod.get_global_var('func_95')
call_152 = relay.TupleGetItem(func_93_call(), 0)
call_153 = relay.TupleGetItem(func_95_call(), 0)
output = relay.Tuple([call_136,call_152,])
output2 = relay.Tuple([call_137,call_153,])
func_167 = relay.Function([], output)
mod['func_167'] = func_167
mod = relay.transform.InferType()(mod)
output = func_167()
func_168 = relay.Function([], output)
mutated_mod['func_168'] = func_168
mutated_mod = relay.transform.InferType()(mutated_mod)
func_119_call = mod.get_global_var('func_119')
func_121_call = mutated_mod.get_global_var('func_121')
call_235 = relay.TupleGetItem(func_119_call(), 0)
call_236 = relay.TupleGetItem(func_121_call(), 0)
output = relay.Tuple([call_235,])
output2 = relay.Tuple([call_236,])
func_242 = relay.Function([], output)
mod['func_242'] = func_242
mod = relay.transform.InferType()(mod)
output = func_242()
func_243 = relay.Function([], output)
mutated_mod['func_243'] = func_243
mutated_mod = relay.transform.InferType()(mutated_mod)
func_167_call = mod.get_global_var('func_167')
func_168_call = mutated_mod.get_global_var('func_168')
call_253 = relay.TupleGetItem(func_167_call(), 0)
call_254 = relay.TupleGetItem(func_168_call(), 0)
output = call_253
output2 = call_254
func_255 = relay.Function([], output)
mod['func_255'] = func_255
mod = relay.transform.InferType()(mod)
output = func_255()
func_256 = relay.Function([], output)
mutated_mod['func_256'] = func_256
mutated_mod = relay.transform.InferType()(mutated_mod)
func_93_call = mod.get_global_var('func_93')
func_95_call = mutated_mod.get_global_var('func_95')
call_270 = relay.TupleGetItem(func_93_call(), 0)
call_271 = relay.TupleGetItem(func_95_call(), 0)
uop_272 = relay.asinh(call_270.astype('float64')) # shape=(6, 1, 6)
uop_274 = relay.asinh(call_271.astype('float64')) # shape=(6, 1, 6)
output = uop_272
output2 = uop_274
func_276 = relay.Function([], output)
mod['func_276'] = func_276
mod = relay.transform.InferType()(mod)
mutated_mod['func_276'] = func_276
mutated_mod = relay.transform.InferType()(mutated_mod)
func_276_call = mutated_mod.get_global_var('func_276')
call_277 = func_276_call()
output = call_277
func_278 = relay.Function([], output)
mutated_mod['func_278'] = func_278
mutated_mod = relay.transform.InferType()(mutated_mod)
func_276_call = mod.get_global_var('func_276')
func_278_call = mutated_mod.get_global_var('func_278')
call_281 = func_276_call()
call_282 = func_276_call()
output = call_281
output2 = call_282
func_285 = relay.Function([], output)
mod['func_285'] = func_285
mod = relay.transform.InferType()(mod)
output = func_285()
func_286 = relay.Function([], output)
mutated_mod['func_286'] = func_286
mutated_mod = relay.transform.InferType()(mutated_mod)
var_296 = relay.var("var_296", dtype = "uint8", shape = (4, 5, 13))#candidate|296|(4, 5, 13)|var|uint8
const_297 = relay.const([[[9,5,-1,-2,7,7,-1,-9,4,-3,-1,7,-7],[8,6,-5,1,-3,-3,7,2,3,9,-10,-4,-3],[9,10,8,5,-9,-9,10,-5,4,2,7,1,9],[-6,-6,9,-8,1,-8,10,-7,-10,-8,2,6,-1],[-1,-9,-4,5,-6,5,-3,2,5,9,-10,10,3]],[[-3,8,-1,6,1,-7,-2,-1,6,5,5,9,-3],[4,-10,-7,-7,-7,-6,-10,-5,-1,9,5,-6,-3],[-2,7,-5,1,8,-8,-3,-3,8,-3,-10,9,6],[5,6,-3,4,4,-8,5,-2,-1,8,3,-9,8],[-1,-1,2,-7,5,7,-9,-9,7,-5,6,4,-1]],[[-1,-1,4,-7,9,2,-8,-7,6,-9,2,-10,-2],[2,10,3,8,10,8,-6,9,-4,-6,-3,8,9],[5,-7,-6,5,6,7,1,-5,-5,5,-10,-10,-3],[-9,4,-1,7,-7,10,-9,9,-8,3,9,-4,-1],[-5,-9,3,-9,5,-7,-9,5,10,6,10,-10,-7]],[[1,3,-6,-3,5,2,-5,4,-3,-10,-4,4,10],[2,-5,6,10,7,8,-10,6,-6,3,6,-5,-4],[-7,-9,-10,-4,1,2,1,-7,9,-1,9,7,9],[6,10,-5,8,-3,-6,-5,8,6,7,8,1,1],[9,2,3,-4,-7,1,2,6,-10,-2,-8,-2,4]]], dtype = "uint8")#candidate|297|(4, 5, 13)|const|uint8
bop_298 = relay.bitwise_or(var_296.astype('uint8'), relay.reshape(const_297.astype('uint8'), relay.shape_of(var_296))) # shape=(4, 5, 13)
bop_311 = relay.add(var_296.astype('uint32'), relay.reshape(const_297.astype('uint32'), relay.shape_of(var_296))) # shape=(4, 5, 13)
func_167_call = mod.get_global_var('func_167')
func_168_call = mutated_mod.get_global_var('func_168')
call_314 = relay.TupleGetItem(func_167_call(), 1)
call_315 = relay.TupleGetItem(func_168_call(), 1)
func_285_call = mod.get_global_var('func_285')
func_286_call = mutated_mod.get_global_var('func_286')
call_318 = func_285_call()
call_319 = func_285_call()
output = relay.Tuple([bop_298,bop_311,call_314,call_318,])
output2 = relay.Tuple([bop_298,bop_311,call_315,call_319,])
func_326 = relay.Function([var_296,], output)
mod['func_326'] = func_326
mod = relay.transform.InferType()(mod)
var_327 = relay.var("var_327", dtype = "uint8", shape = (4, 5, 13))#candidate|327|(4, 5, 13)|var|uint8
output = func_326(var_327)
func_328 = relay.Function([var_327], output)
mutated_mod['func_328'] = func_328
mutated_mod = relay.transform.InferType()(mutated_mod)
func_93_call = mod.get_global_var('func_93')
func_95_call = mutated_mod.get_global_var('func_95')
call_372 = relay.TupleGetItem(func_93_call(), 0)
call_373 = relay.TupleGetItem(func_95_call(), 0)
func_93_call = mod.get_global_var('func_93')
func_95_call = mutated_mod.get_global_var('func_95')
call_393 = relay.TupleGetItem(func_93_call(), 1)
call_394 = relay.TupleGetItem(func_95_call(), 1)
bop_403 = relay.less(call_372.astype('bool'), relay.reshape(call_393.astype('bool'), relay.shape_of(call_372))) # shape=(6, 1, 6)
bop_406 = relay.less(call_373.astype('bool'), relay.reshape(call_394.astype('bool'), relay.shape_of(call_373))) # shape=(6, 1, 6)
output = relay.Tuple([bop_403,])
output2 = relay.Tuple([bop_406,])
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
func_407_call = mod.get_global_var('func_407')
func_409_call = mutated_mod.get_global_var('func_409')
call_501 = relay.TupleGetItem(func_407_call(), 0)
call_502 = relay.TupleGetItem(func_409_call(), 0)
output = call_501
output2 = call_502
func_506 = relay.Function([], output)
mod['func_506'] = func_506
mod = relay.transform.InferType()(mod)
output = func_506()
func_507 = relay.Function([], output)
mutated_mod['func_507'] = func_507
mutated_mod = relay.transform.InferType()(mutated_mod)
func_242_call = mod.get_global_var('func_242')
func_243_call = mutated_mod.get_global_var('func_243')
call_526 = relay.TupleGetItem(func_242_call(), 0)
call_527 = relay.TupleGetItem(func_243_call(), 0)
const_529 = relay.const([[[-9,7,2,5,-9,7],[-3,9,10,9,5,-3],[4,3,5,7,6,10],[-5,-9,8,-2,-3,-8],[-6,-10,1,-3,5,10],[-9,6,3,5,-10,4],[10,-8,9,-7,5,4],[-9,10,3,3,-6,-7],[-4,-9,-9,-2,-7,2]],[[-8,-10,4,-8,3,6],[7,7,-8,-4,-9,9],[-4,-4,1,8,5,-2],[-4,-4,10,2,-7,3],[-3,2,-10,9,1,-6],[3,4,3,-9,-10,-3],[-10,10,-4,-7,-1,-3],[9,6,7,-2,7,-8],[-4,9,-9,4,9,-7]],[[8,2,-2,-2,-6,10],[-10,6,10,2,-1,8],[5,-9,10,7,-1,-7],[3,5,8,5,-8,9],[-4,-2,2,-7,5,-9],[-4,-3,5,-2,-9,-10],[-2,7,5,-8,5,-6],[-3,3,-10,3,9,3],[-5,-4,1,3,8,-3]],[[-4,-4,2,-7,4,3],[4,-2,-1,9,-1,10],[5,-7,-3,-6,3,7],[1,-2,-6,10,2,-5],[8,-9,-4,-3,4,4],[10,4,9,3,-7,-6],[4,5,10,9,3,-7],[10,-8,9,10,1,5],[7,-3,-4,1,4,2]],[[-7,2,-2,9,-8,-4],[10,-6,-2,-4,-8,-7],[-3,-8,6,1,-2,3],[1,-6,2,3,8,4],[10,-10,4,-9,-6,6],[-9,-3,-9,7,-2,-8],[-4,6,-2,-1,8,-1],[9,-9,-8,-4,3,10],[-8,1,-1,-4,-4,7]],[[1,-10,-1,1,-4,-4],[-7,-1,-8,2,7,5],[6,3,10,-6,9,-9],[-9,-2,-1,5,-7,-8],[-7,-2,-6,10,-8,2],[4,10,5,6,10,-7],[4,-8,-8,7,-9,-8],[8,10,3,-6,1,-2],[3,-10,-4,5,9,-1]]], dtype = "int64")#candidate|529|(6, 9, 6)|const|int64
bop_530 = relay.divide(call_526.astype('float32'), const_529.astype('float32')) # shape=(6, 9, 6)
bop_533 = relay.divide(call_527.astype('float32'), const_529.astype('float32')) # shape=(6, 9, 6)
output = relay.Tuple([bop_530,])
output2 = relay.Tuple([bop_533,])
func_561 = relay.Function([], output)
mod['func_561'] = func_561
mod = relay.transform.InferType()(mod)
output = func_561()
func_562 = relay.Function([], output)
mutated_mod['func_562'] = func_562
mutated_mod = relay.transform.InferType()(mutated_mod)
func_119_call = mod.get_global_var('func_119')
func_121_call = mutated_mod.get_global_var('func_121')
call_578 = relay.TupleGetItem(func_119_call(), 1)
call_579 = relay.TupleGetItem(func_121_call(), 1)
func_407_call = mod.get_global_var('func_407')
func_409_call = mutated_mod.get_global_var('func_409')
call_580 = relay.TupleGetItem(func_407_call(), 0)
call_581 = relay.TupleGetItem(func_409_call(), 0)
uop_586 = relay.erf(call_578.astype('float64')) # shape=(6, 1, 6)
uop_588 = relay.erf(call_579.astype('float64')) # shape=(6, 1, 6)
output = relay.Tuple([call_580,uop_586,])
output2 = relay.Tuple([call_581,uop_588,])
func_610 = relay.Function([], output)
mod['func_610'] = func_610
mod = relay.transform.InferType()(mod)
output = func_610()
func_611 = relay.Function([], output)
mutated_mod['func_611'] = func_611
mutated_mod = relay.transform.InferType()(mutated_mod)
var_638 = relay.var("var_638", dtype = "uint64", shape = (5, 5, 7))#candidate|638|(5, 5, 7)|var|uint64
const_639 = relay.const([[[3,-8,10,-4,-8,5,8],[6,9,-5,-1,-3,-4,-9],[-8,-10,6,4,3,-8,8],[9,-9,8,-10,-8,2,8],[-8,-4,9,-9,-9,8,-10]],[[6,-2,-4,4,8,4,3],[-1,3,-1,8,-10,-2,8],[2,-8,6,7,-2,5,-5],[8,-7,2,-10,9,-10,5],[-8,1,2,2,3,9,10]],[[-5,-3,4,4,3,8,4],[-9,-9,-1,-8,-2,-1,10],[10,6,-5,-10,2,-5,-10],[7,9,2,-4,10,7,2],[9,-10,2,-4,-8,5,10]],[[4,-1,3,-6,9,9,-2],[3,6,8,1,-3,-6,-1],[10,-9,1,-5,1,3,-1],[-9,-1,-7,-2,-3,4,10],[-9,-10,-2,5,-10,-2,-2]],[[-9,7,8,-8,-3,1,-7],[-5,4,10,5,3,-7,-10],[4,-4,-7,-10,-9,9,1],[9,4,7,-8,-3,8,2],[-9,-4,4,-5,-9,7,3]]], dtype = "uint64")#candidate|639|(5, 5, 7)|const|uint64
bop_640 = relay.greater_equal(var_638.astype('bool'), relay.reshape(const_639.astype('bool'), relay.shape_of(var_638))) # shape=(5, 5, 7)
func_242_call = mod.get_global_var('func_242')
func_243_call = mutated_mod.get_global_var('func_243')
call_646 = relay.TupleGetItem(func_242_call(), 0)
call_647 = relay.TupleGetItem(func_243_call(), 0)
output = relay.Tuple([bop_640,call_646,])
output2 = relay.Tuple([bop_640,call_647,])
func_649 = relay.Function([var_638,], output)
mod['func_649'] = func_649
mod = relay.transform.InferType()(mod)
var_650 = relay.var("var_650", dtype = "uint64", shape = (5, 5, 7))#candidate|650|(5, 5, 7)|var|uint64
output = func_649(var_650)
func_651 = relay.Function([var_650], output)
mutated_mod['func_651'] = func_651
mutated_mod = relay.transform.InferType()(mutated_mod)
func_119_call = mod.get_global_var('func_119')
func_121_call = mutated_mod.get_global_var('func_121')
call_656 = relay.TupleGetItem(func_119_call(), 1)
call_657 = relay.TupleGetItem(func_121_call(), 1)
uop_658 = relay.acosh(call_656.astype('float64')) # shape=(6, 1, 6)
uop_660 = relay.acosh(call_657.astype('float64')) # shape=(6, 1, 6)
bop_666 = relay.bitwise_xor(uop_658.astype('uint64'), relay.reshape(call_656.astype('uint64'), relay.shape_of(uop_658))) # shape=(6, 1, 6)
bop_669 = relay.bitwise_xor(uop_660.astype('uint64'), relay.reshape(call_657.astype('uint64'), relay.shape_of(uop_660))) # shape=(6, 1, 6)
func_285_call = mod.get_global_var('func_285')
func_286_call = mutated_mod.get_global_var('func_286')
call_674 = func_285_call()
call_675 = func_285_call()
func_506_call = mod.get_global_var('func_506')
func_507_call = mutated_mod.get_global_var('func_507')
call_678 = func_506_call()
call_679 = func_506_call()
output = relay.Tuple([bop_666,call_674,call_678,])
output2 = relay.Tuple([bop_669,call_675,call_679,])
func_685 = relay.Function([], output)
mod['func_685'] = func_685
mod = relay.transform.InferType()(mod)
mutated_mod['func_685'] = func_685
mutated_mod = relay.transform.InferType()(mutated_mod)
func_685_call = mutated_mod.get_global_var('func_685')
call_686 = func_685_call()
output = call_686
func_687 = relay.Function([], output)
mutated_mod['func_687'] = func_687
mutated_mod = relay.transform.InferType()(mutated_mod)
func_407_call = mod.get_global_var('func_407')
func_409_call = mutated_mod.get_global_var('func_409')
call_699 = relay.TupleGetItem(func_407_call(), 0)
call_700 = relay.TupleGetItem(func_409_call(), 0)
output = relay.Tuple([call_699,])
output2 = relay.Tuple([call_700,])
func_707 = relay.Function([], output)
mod['func_707'] = func_707
mod = relay.transform.InferType()(mod)
output = func_707()
func_708 = relay.Function([], output)
mutated_mod['func_708'] = func_708
mutated_mod = relay.transform.InferType()(mutated_mod)
func_276_call = mod.get_global_var('func_276')
func_278_call = mutated_mod.get_global_var('func_278')
call_717 = func_276_call()
call_718 = func_276_call()
output = call_717
output2 = call_718
func_731 = relay.Function([], output)
mod['func_731'] = func_731
mod = relay.transform.InferType()(mod)
output = func_731()
func_732 = relay.Function([], output)
mutated_mod['func_732'] = func_732
mutated_mod = relay.transform.InferType()(mutated_mod)
func_242_call = mod.get_global_var('func_242')
func_243_call = mutated_mod.get_global_var('func_243')
call_738 = relay.TupleGetItem(func_242_call(), 0)
call_739 = relay.TupleGetItem(func_243_call(), 0)
const_742 = relay.const([[[-6,-6,1,-6,9,9],[9,1,-6,-4,-5,3],[-6,8,3,-9,-2,-4],[3,1,-9,2,-8,3],[-5,-7,8,4,-5,3],[-4,-8,7,1,-1,-2],[7,-10,8,-8,-2,5],[5,6,-4,9,-1,-6]],[[7,10,2,-10,-7,-3],[-4,8,-6,-8,6,10],[-10,8,3,4,3,-10],[8,-5,8,8,9,-10],[10,-5,-9,-6,3,4],[10,-8,2,10,-7,4],[3,9,-9,8,-4,-6],[7,4,8,5,-6,10]],[[10,9,-7,5,5,3],[-3,-3,-3,2,3,-9],[5,-8,7,-10,-10,-6],[-2,-6,-5,8,9,4],[4,-1,3,-7,-3,1],[5,-9,-10,1,-6,-6],[-3,8,10,3,8,-9],[3,1,-5,8,-4,4]],[[-3,-6,1,1,-8,5],[1,-10,-3,1,-8,-3],[-3,-2,7,-10,2,-9],[-8,6,-9,4,10,-8],[4,10,2,-5,-4,3],[-3,-2,-7,-8,1,-10],[5,-10,-7,-10,10,3],[1,8,-4,-7,-1,2]],[[9,-4,-3,1,-10,7],[-9,-8,-6,10,10,-5],[8,1,-2,-1,4,3],[2,7,7,1,10,-7],[-2,-4,-7,-5,10,6],[9,-4,3,-10,3,8],[1,6,-9,-8,1,3],[2,3,-6,-5,-4,-7]],[[6,3,7,7,-1,1],[-7,-4,2,6,-7,-5],[8,9,-9,-1,6,-2],[7,2,6,1,4,-4],[3,10,1,-7,5,2],[-4,7,-9,4,-2,-6],[-4,2,2,-4,-7,9],[2,-8,-1,1,5,5]]], dtype = "int64")#candidate|742|(6, 8, 6)|const|int64
bop_743 = relay.equal(call_738.astype('bool'), const_742.astype('bool')) # shape=(6, 8, 6)
bop_746 = relay.equal(call_739.astype('bool'), const_742.astype('bool')) # shape=(6, 8, 6)
output = relay.Tuple([bop_743,])
output2 = relay.Tuple([bop_746,])
func_747 = relay.Function([], output)
mod['func_747'] = func_747
mod = relay.transform.InferType()(mod)
output = func_747()
func_748 = relay.Function([], output)
mutated_mod['func_748'] = func_748
mutated_mod = relay.transform.InferType()(mutated_mod)
func_242_call = mod.get_global_var('func_242')
func_243_call = mutated_mod.get_global_var('func_243')
call_909 = relay.TupleGetItem(func_242_call(), 0)
call_910 = relay.TupleGetItem(func_243_call(), 0)
func_561_call = mod.get_global_var('func_561')
func_562_call = mutated_mod.get_global_var('func_562')
call_920 = relay.TupleGetItem(func_561_call(), 0)
call_921 = relay.TupleGetItem(func_562_call(), 0)
output = relay.Tuple([call_909,call_920,])
output2 = relay.Tuple([call_910,call_921,])
func_926 = relay.Function([], output)
mod['func_926'] = func_926
mod = relay.transform.InferType()(mod)
mutated_mod['func_926'] = func_926
mutated_mod = relay.transform.InferType()(mutated_mod)
func_926_call = mutated_mod.get_global_var('func_926')
call_927 = func_926_call()
output = call_927
func_928 = relay.Function([], output)
mutated_mod['func_928'] = func_928
mutated_mod = relay.transform.InferType()(mutated_mod)
const_929 = relay.const([[[-9,8,-5,9,4,-5,8],[-10,-3,-2,-2,-4,-8,-9],[5,7,-4,2,-1,9,-4],[8,-4,2,-1,-8,-7,-7],[3,-10,-6,4,1,-1,-8],[-8,9,-2,-6,10,-9,2],[5,3,-7,-8,-7,5,10],[-10,8,-9,-4,10,7,7],[10,-4,-9,5,-9,9,7],[5,9,6,-3,-4,7,-7],[4,2,3,1,2,-10,-10],[8,4,-7,-9,10,-1,7],[6,4,-9,-6,-2,-6,6],[5,4,5,7,1,-8,-5]],[[5,7,-7,-3,-7,9,-7],[-4,-9,-9,2,-3,10,4],[4,7,3,-3,4,9,7],[1,-2,-9,3,8,-5,-6],[-4,3,2,-1,1,-9,2],[-8,-5,6,-5,-2,4,6],[10,4,-4,4,-4,-3,9],[-2,10,-1,-1,4,-2,6],[6,-3,6,2,4,-8,-9],[5,-2,10,-9,7,-5,-7],[9,3,7,-6,5,7,-2],[-8,-5,-2,2,-1,10,-2],[-10,4,-4,9,-2,6,-10],[7,-7,6,9,-3,7,-9]],[[-1,-4,10,2,-2,7,3],[1,8,7,2,9,9,-2],[5,3,-2,7,-2,8,-10],[-8,-10,-6,7,-6,-7,2],[-9,2,6,8,-2,-2,5],[-10,6,-8,7,5,-9,6],[-5,4,3,-8,1,6,2],[-10,9,2,8,-2,-3,-10],[9,10,4,-10,10,-5,3],[-6,3,-3,-6,10,4,10],[10,-2,7,4,4,8,9],[4,-7,8,8,4,8,-9],[-5,-10,8,5,1,-7,-1],[-8,-10,-4,-5,-9,-6,7]]], dtype = "uint32")#candidate|929|(3, 14, 7)|const|uint32
var_930 = relay.var("var_930", dtype = "uint32", shape = (3, 14, 7))#candidate|930|(3, 14, 7)|var|uint32
bop_931 = relay.greater(const_929.astype('bool'), relay.reshape(var_930.astype('bool'), relay.shape_of(const_929))) # shape=(3, 14, 7)
func_506_call = mod.get_global_var('func_506')
func_507_call = mutated_mod.get_global_var('func_507')
call_935 = func_506_call()
call_936 = func_506_call()
output = relay.Tuple([bop_931,call_935,])
output2 = relay.Tuple([bop_931,call_936,])
func_939 = relay.Function([var_930,], output)
mod['func_939'] = func_939
mod = relay.transform.InferType()(mod)
mutated_mod['func_939'] = func_939
mutated_mod = relay.transform.InferType()(mutated_mod)
var_940 = relay.var("var_940", dtype = "uint32", shape = (3, 14, 7))#candidate|940|(3, 14, 7)|var|uint32
func_939_call = mutated_mod.get_global_var('func_939')
call_941 = func_939_call(var_940)
output = call_941
func_942 = relay.Function([var_940], output)
mutated_mod['func_942'] = func_942
mutated_mod = relay.transform.InferType()(mutated_mod)
func_561_call = mod.get_global_var('func_561')
func_562_call = mutated_mod.get_global_var('func_562')
call_947 = relay.TupleGetItem(func_561_call(), 0)
call_948 = relay.TupleGetItem(func_562_call(), 0)
output = call_947
output2 = call_948
func_953 = relay.Function([], output)
mod['func_953'] = func_953
mod = relay.transform.InferType()(mod)
output = func_953()
func_954 = relay.Function([], output)
mutated_mod['func_954'] = func_954
mutated_mod = relay.transform.InferType()(mutated_mod)
var_957 = relay.var("var_957", dtype = "float64", shape = (3, 1, 5))#candidate|957|(3, 1, 5)|var|float64
uop_958 = relay.cos(var_957.astype('float64')) # shape=(3, 1, 5)
output = relay.Tuple([uop_958,])
output2 = relay.Tuple([uop_958,])
func_980 = relay.Function([var_957,], output)
mod['func_980'] = func_980
mod = relay.transform.InferType()(mod)
var_981 = relay.var("var_981", dtype = "float64", shape = (3, 1, 5))#candidate|981|(3, 1, 5)|var|float64
output = func_980(var_981)
func_982 = relay.Function([var_981], output)
mutated_mod['func_982'] = func_982
mutated_mod = relay.transform.InferType()(mutated_mod)
func_242_call = mod.get_global_var('func_242')
func_243_call = mutated_mod.get_global_var('func_243')
call_1044 = relay.TupleGetItem(func_242_call(), 0)
call_1045 = relay.TupleGetItem(func_243_call(), 0)
func_953_call = mod.get_global_var('func_953')
func_954_call = mutated_mod.get_global_var('func_954')
call_1046 = func_953_call()
call_1047 = func_953_call()
var_1055 = relay.var("var_1055", dtype = "int64", shape = (6, 10, 6))#candidate|1055|(6, 10, 6)|var|int64
bop_1056 = relay.bitwise_xor(call_1044.astype('uint16'), var_1055.astype('uint16')) # shape=(6, 10, 6)
bop_1059 = relay.bitwise_xor(call_1045.astype('uint16'), var_1055.astype('uint16')) # shape=(6, 10, 6)
uop_1084 = relay.acosh(var_1055.astype('float32')) # shape=(6, 10, 6)
func_326_call = mod.get_global_var('func_326')
func_328_call = mutated_mod.get_global_var('func_328')
var_1102 = relay.var("var_1102", dtype = "uint8", shape = (260,))#candidate|1102|(260,)|var|uint8
call_1101 = relay.TupleGetItem(func_326_call(relay.reshape(var_1102.astype('uint8'), [4, 5, 13])), 2)
call_1103 = relay.TupleGetItem(func_328_call(relay.reshape(var_1102.astype('uint8'), [4, 5, 13])), 2)
output = relay.Tuple([call_1046,bop_1056,uop_1084,call_1101,var_1102,])
output2 = relay.Tuple([call_1047,bop_1059,uop_1084,call_1103,var_1102,])
func_1104 = relay.Function([var_1055,var_1102,], output)
mod['func_1104'] = func_1104
mod = relay.transform.InferType()(mod)
var_1105 = relay.var("var_1105", dtype = "int64", shape = (6, 10, 6))#candidate|1105|(6, 10, 6)|var|int64
var_1106 = relay.var("var_1106", dtype = "uint8", shape = (260,))#candidate|1106|(260,)|var|uint8
output = func_1104(var_1105,var_1106,)
func_1107 = relay.Function([var_1105,var_1106,], output)
mutated_mod['func_1107'] = func_1107
mutated_mod = relay.transform.InferType()(mutated_mod)
func_285_call = mod.get_global_var('func_285')
func_286_call = mutated_mod.get_global_var('func_286')
call_1111 = func_285_call()
call_1112 = func_285_call()
var_1118 = relay.var("var_1118", dtype = "float64", shape = (6, 1, 6))#candidate|1118|(6, 1, 6)|var|float64
bop_1119 = relay.mod(call_1111.astype('float32'), relay.reshape(var_1118.astype('float32'), relay.shape_of(call_1111))) # shape=(6, 1, 6)
bop_1122 = relay.mod(call_1112.astype('float32'), relay.reshape(var_1118.astype('float32'), relay.shape_of(call_1112))) # shape=(6, 1, 6)
uop_1128 = relay.sin(call_1111.astype('float32')) # shape=(6, 1, 6)
uop_1130 = relay.sin(call_1112.astype('float32')) # shape=(6, 1, 6)
bop_1141 = relay.less_equal(uop_1128.astype('bool'), relay.reshape(call_1111.astype('bool'), relay.shape_of(uop_1128))) # shape=(6, 1, 6)
bop_1144 = relay.less_equal(uop_1130.astype('bool'), relay.reshape(call_1112.astype('bool'), relay.shape_of(uop_1130))) # shape=(6, 1, 6)
output = relay.Tuple([bop_1119,bop_1141,])
output2 = relay.Tuple([bop_1122,bop_1144,])
func_1145 = relay.Function([var_1118,], output)
mod['func_1145'] = func_1145
mod = relay.transform.InferType()(mod)
var_1146 = relay.var("var_1146", dtype = "float64", shape = (6, 1, 6))#candidate|1146|(6, 1, 6)|var|float64
output = func_1145(var_1146)
func_1147 = relay.Function([var_1146], output)
mutated_mod['func_1147'] = func_1147
mutated_mod = relay.transform.InferType()(mutated_mod)
func_407_call = mod.get_global_var('func_407')
func_409_call = mutated_mod.get_global_var('func_409')
call_1177 = relay.TupleGetItem(func_407_call(), 0)
call_1178 = relay.TupleGetItem(func_409_call(), 0)
func_93_call = mod.get_global_var('func_93')
func_95_call = mutated_mod.get_global_var('func_95')
call_1184 = relay.TupleGetItem(func_93_call(), 1)
call_1185 = relay.TupleGetItem(func_95_call(), 1)
output = relay.Tuple([call_1177,call_1184,])
output2 = relay.Tuple([call_1178,call_1185,])
func_1197 = relay.Function([], output)
mod['func_1197'] = func_1197
mod = relay.transform.InferType()(mod)
output = func_1197()
func_1198 = relay.Function([], output)
mutated_mod['func_1198'] = func_1198
mutated_mod = relay.transform.InferType()(mutated_mod)
func_255_call = mod.get_global_var('func_255')
func_256_call = mutated_mod.get_global_var('func_256')
call_1204 = func_255_call()
call_1205 = func_255_call()
output = call_1204
output2 = call_1205
func_1206 = relay.Function([], output)
mod['func_1206'] = func_1206
mod = relay.transform.InferType()(mod)
mutated_mod['func_1206'] = func_1206
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1206_call = mutated_mod.get_global_var('func_1206')
call_1207 = func_1206_call()
output = call_1207
func_1208 = relay.Function([], output)
mutated_mod['func_1208'] = func_1208
mutated_mod = relay.transform.InferType()(mutated_mod)
func_610_call = mod.get_global_var('func_610')
func_611_call = mutated_mod.get_global_var('func_611')
call_1222 = relay.TupleGetItem(func_610_call(), 0)
call_1223 = relay.TupleGetItem(func_611_call(), 0)
output = relay.Tuple([call_1222,])
output2 = relay.Tuple([call_1223,])
func_1234 = relay.Function([], output)
mod['func_1234'] = func_1234
mod = relay.transform.InferType()(mod)
output = func_1234()
func_1235 = relay.Function([], output)
mutated_mod['func_1235'] = func_1235
mutated_mod = relay.transform.InferType()(mutated_mod)
func_285_call = mod.get_global_var('func_285')
func_286_call = mutated_mod.get_global_var('func_286')
call_1239 = func_285_call()
call_1240 = func_285_call()
output = relay.Tuple([call_1239,])
output2 = relay.Tuple([call_1240,])
func_1245 = relay.Function([], output)
mod['func_1245'] = func_1245
mod = relay.transform.InferType()(mod)
output = func_1245()
func_1246 = relay.Function([], output)
mutated_mod['func_1246'] = func_1246
mutated_mod = relay.transform.InferType()(mutated_mod)
func_610_call = mod.get_global_var('func_610')
func_611_call = mutated_mod.get_global_var('func_611')
call_1347 = relay.TupleGetItem(func_610_call(), 0)
call_1348 = relay.TupleGetItem(func_611_call(), 0)
uop_1358 = relay.asin(call_1347.astype('float32')) # shape=(6, 1, 6)
uop_1360 = relay.asin(call_1348.astype('float32')) # shape=(6, 1, 6)
output = uop_1358
output2 = uop_1360
func_1363 = relay.Function([], output)
mod['func_1363'] = func_1363
mod = relay.transform.InferType()(mod)
mutated_mod['func_1363'] = func_1363
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1363_call = mutated_mod.get_global_var('func_1363')
call_1364 = func_1363_call()
output = call_1364
func_1365 = relay.Function([], output)
mutated_mod['func_1365'] = func_1365
mutated_mod = relay.transform.InferType()(mutated_mod)
func_953_call = mod.get_global_var('func_953')
func_954_call = mutated_mod.get_global_var('func_954')
call_1376 = func_953_call()
call_1377 = func_953_call()
uop_1388 = relay.atan(call_1376.astype('float32')) # shape=(6, 9, 6)
uop_1390 = relay.atan(call_1377.astype('float32')) # shape=(6, 9, 6)
uop_1393 = relay.exp(call_1376.astype('float64')) # shape=(6, 9, 6)
uop_1395 = relay.exp(call_1377.astype('float64')) # shape=(6, 9, 6)
func_707_call = mod.get_global_var('func_707')
func_708_call = mutated_mod.get_global_var('func_708')
call_1414 = relay.TupleGetItem(func_707_call(), 0)
call_1415 = relay.TupleGetItem(func_708_call(), 0)
func_326_call = mod.get_global_var('func_326')
func_328_call = mutated_mod.get_global_var('func_328')
var_1420 = relay.var("var_1420", dtype = "uint8", shape = (260,))#candidate|1420|(260,)|var|uint8
call_1419 = relay.TupleGetItem(func_326_call(relay.reshape(var_1420.astype('uint8'), [4, 5, 13])), 0)
call_1421 = relay.TupleGetItem(func_328_call(relay.reshape(var_1420.astype('uint8'), [4, 5, 13])), 0)
uop_1422 = relay.atanh(uop_1388.astype('float32')) # shape=(6, 9, 6)
uop_1424 = relay.atanh(uop_1390.astype('float32')) # shape=(6, 9, 6)
output = relay.Tuple([uop_1393,call_1414,call_1419,var_1420,uop_1422,])
output2 = relay.Tuple([uop_1395,call_1415,call_1421,var_1420,uop_1424,])
func_1426 = relay.Function([var_1420,], output)
mod['func_1426'] = func_1426
mod = relay.transform.InferType()(mod)
mutated_mod['func_1426'] = func_1426
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1427 = relay.var("var_1427", dtype = "uint8", shape = (260,))#candidate|1427|(260,)|var|uint8
func_1426_call = mutated_mod.get_global_var('func_1426')
call_1428 = func_1426_call(var_1427)
output = call_1428
func_1429 = relay.Function([var_1427], output)
mutated_mod['func_1429'] = func_1429
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1245_call = mod.get_global_var('func_1245')
func_1246_call = mutated_mod.get_global_var('func_1246')
call_1442 = relay.TupleGetItem(func_1245_call(), 0)
call_1443 = relay.TupleGetItem(func_1246_call(), 0)
var_1453 = relay.var("var_1453", dtype = "float64", shape = (6, 3, 6))#candidate|1453|(6, 3, 6)|var|float64
bop_1454 = relay.less_equal(call_1442.astype('bool'), var_1453.astype('bool')) # shape=(6, 3, 6)
bop_1457 = relay.less_equal(call_1443.astype('bool'), var_1453.astype('bool')) # shape=(6, 3, 6)
uop_1460 = relay.tan(call_1442.astype('float32')) # shape=(6, 1, 6)
uop_1462 = relay.tan(call_1443.astype('float32')) # shape=(6, 1, 6)
func_953_call = mod.get_global_var('func_953')
func_954_call = mutated_mod.get_global_var('func_954')
call_1467 = func_953_call()
call_1468 = func_953_call()
output = relay.Tuple([bop_1454,uop_1460,call_1467,])
output2 = relay.Tuple([bop_1457,uop_1462,call_1468,])
func_1472 = relay.Function([var_1453,], output)
mod['func_1472'] = func_1472
mod = relay.transform.InferType()(mod)
var_1473 = relay.var("var_1473", dtype = "float64", shape = (6, 3, 6))#candidate|1473|(6, 3, 6)|var|float64
output = func_1472(var_1473)
func_1474 = relay.Function([var_1473], output)
mutated_mod['func_1474'] = func_1474
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1537 = relay.const([[[-3.779111,0.198454,9.835140,-9.674741,8.357133,-8.972465,-0.091863,3.990000,5.482340,-2.426277,1.990928,4.997599],[4.131151,-1.118991,-4.219230,-9.797495,-2.032698,7.361314,9.283869,5.765205,6.943820,4.902680,-4.844540,-2.425201],[-0.916868,9.262649,2.308869,-9.447139,4.700235,-3.000221,-3.253108,-1.430014,-1.051056,-1.631105,6.483176,-2.957977],[-4.456613,-9.401962,3.573448,-0.073217,9.386365,2.361874,-1.716722,0.660338,-2.785070,1.784813,-7.702197,7.835704],[2.190354,-5.239895,6.497825,-9.841876,8.774119,3.262509,6.582782,-1.056178,5.992507,3.655422,0.907831,5.611557],[-7.053964,-7.560177,-6.097314,-8.508011,-6.531175,0.275231,2.789636,3.494199,-5.115591,9.579918,-6.613897,7.132652],[7.479832,5.793768,0.699266,-9.710920,8.929391,4.312139,0.877585,1.919743,-9.349582,5.157808,-0.013831,-5.869465],[7.398830,-3.104430,4.683133,-7.167259,-7.209416,4.616882,-7.620304,-9.000405,9.855342,-4.521581,4.332960,-9.084581],[-7.723045,1.912134,-0.298515,2.950921,-8.237884,4.010261,5.333041,-4.344516,0.480745,-9.987057,-1.353578,0.468448],[-4.596622,-1.067084,8.747291,9.464566,-5.762808,8.491273,5.742176,9.805510,-1.779372,1.605083,-6.319591,-4.180280]],[[-2.676146,6.033812,5.149222,-9.303341,-4.456909,5.469683,0.288511,6.983508,5.705078,-2.711227,-3.545967,-3.494399],[-9.528488,-8.163464,-6.922757,-0.552459,4.986055,9.319652,-3.351925,-7.193091,-5.908145,-4.739451,9.168402,7.660724],[-1.162881,1.438175,2.267637,-6.125650,7.876594,-1.700164,4.855209,-8.861064,2.677875,0.387003,5.902932,-8.797009],[8.146919,3.564737,2.786584,0.150491,-2.591802,-3.742695,2.871934,2.202561,5.135720,-4.652521,-8.979605,-7.552922],[-6.162375,7.030315,1.053993,7.790256,3.368852,7.867251,9.909511,-5.086396,6.813553,-4.014616,6.861555,-5.930617],[5.110865,5.364063,3.780626,5.836965,3.444752,-4.427057,9.770143,4.591227,-4.995617,9.428304,-9.351880,-3.336042],[-5.283670,-8.174402,-9.865914,-0.637886,8.166591,-5.263384,2.348814,-1.139288,-5.070365,-0.551523,-1.832880,-4.217995],[-8.750254,-8.814125,-2.600130,3.968052,1.215329,-9.043786,-9.100927,-6.309500,9.328794,-0.777701,-8.125818,8.778298],[8.157233,-6.711346,-5.717765,5.103829,-2.640756,7.393259,-7.739189,5.518187,-6.573728,3.417373,6.713253,-0.211576],[-5.950378,3.041361,8.899724,-6.725782,-1.163916,-0.089820,8.227843,-7.833869,1.912064,-7.163785,-5.050497,-6.689093]],[[-5.631632,4.394480,4.842704,-3.865324,-9.383161,-3.711857,-9.588196,4.903111,-4.610144,6.241246,9.611385,8.567261],[3.172732,-4.529126,-5.156860,-6.916348,-9.103449,-9.359291,4.034352,-7.919659,-2.690475,9.875943,1.136741,-9.237502],[-2.585708,6.223303,1.954395,2.314423,8.138572,-4.991132,-4.686687,-9.742584,-4.655794,-9.773985,7.022407,5.533605],[0.167987,-7.332257,8.626819,-7.300073,5.302417,6.407030,7.981926,4.366926,-7.865339,-6.089814,8.898029,-2.610589],[9.507620,3.340770,9.180123,-9.673590,-6.418590,6.803428,9.982445,5.688430,1.596554,1.823747,0.097745,7.952697],[-5.845021,-5.245993,-8.498956,1.844221,9.703150,-5.839906,-3.409593,-4.346240,-8.076712,-2.939916,4.247442,-7.774658],[7.892843,4.758120,-0.498798,-2.572859,-9.642404,-9.330964,6.178863,-8.519172,6.433817,5.776189,-0.911194,-2.980181],[2.160595,-8.844609,-2.573395,-3.574129,0.458414,9.545221,-2.305264,-3.419767,-1.759697,-0.113967,7.857571,3.680562],[1.608135,-4.810940,-0.637475,-6.811242,0.359342,-3.857928,8.000337,6.385157,7.568415,5.280755,0.515359,-4.727498],[-4.335556,4.615072,-7.620977,-1.426352,-6.018566,4.691693,2.558906,-8.449309,-1.854873,1.087826,0.922376,-5.267361]],[[1.401222,3.872333,-4.345342,-6.680217,-2.181190,-5.732929,-3.022459,-9.996281,1.029326,9.809392,-3.917284,4.023916],[0.848255,-9.041194,-3.899965,9.294109,-9.058643,-9.686993,-6.666877,-3.565278,-4.476849,8.069652,9.400958,3.502349],[4.826194,-8.913387,9.198436,4.376046,-6.971902,0.621708,-6.692694,-1.274429,8.348896,0.926333,4.217987,-7.725519],[-6.974840,9.810996,-7.196558,-9.754056,6.243031,5.818383,5.052467,0.233391,-0.483789,-2.363952,6.276179,-1.298556],[3.139798,8.444961,9.059130,-9.310563,0.426409,3.291381,6.695602,-8.861458,-5.727843,1.563093,-0.603112,8.737970],[7.142229,9.550756,-3.381489,-4.733277,-6.144043,5.659408,7.122972,4.868412,2.848783,-5.127092,4.465308,9.245588],[-7.239577,6.147768,-8.841636,-1.640491,-6.367101,-3.712279,8.546157,-6.288370,-3.134239,1.842840,7.500779,9.251496],[2.403825,4.959234,-8.017437,3.752091,4.954962,7.870143,5.733298,-3.596796,6.079620,8.001105,4.647602,-3.680875],[1.522252,6.284672,1.821075,5.765905,9.486524,4.595327,3.896308,-9.243004,1.825349,-8.313398,7.488847,-4.917228],[-9.695173,6.500109,9.632942,3.747840,0.899103,7.109484,1.264559,-8.978272,-5.477898,-1.408652,-4.787459,-3.722309]],[[-0.253661,-6.847076,1.301856,8.805128,-3.373561,1.052377,-7.428066,-0.724200,-0.964428,-2.489616,-2.704789,-5.399327],[-6.662836,4.669665,0.615632,-6.953296,-5.799837,-7.561227,3.121436,5.991514,-3.777473,9.283196,-1.266011,4.655948],[-1.071784,-9.913086,-9.615397,2.753407,-5.328435,2.438372,-8.679848,6.155262,-7.170392,3.422429,2.142370,-6.110518],[7.883499,8.972393,5.747799,-7.575050,-7.480085,0.900689,7.645487,-2.317208,4.915778,-8.063235,3.050189,-2.639070],[4.062344,-3.499305,5.890958,-9.415033,-7.161277,-9.095432,-0.493415,0.970287,5.856873,0.853987,3.858150,-3.708438],[5.801610,1.795661,3.915916,7.556769,3.832775,7.410319,-1.016306,8.677446,1.622138,-1.466184,1.385854,0.274368],[-9.791117,5.789693,-5.528964,-7.835540,-3.187484,-3.567367,-8.440368,-9.597023,2.469093,-2.070361,-2.915142,1.058511],[1.551411,8.933944,4.557152,1.259118,-8.719576,-7.145802,3.048311,-8.205586,-5.970200,0.925118,-0.619480,-4.747288],[5.407961,9.768696,-9.159623,-9.599046,4.156920,-4.363084,-2.614797,-0.356313,6.140574,8.190644,-9.291724,-1.994728],[-3.582899,1.076696,-6.889427,8.516414,-0.214012,5.080674,5.407265,-9.427017,9.346201,1.931254,-5.863321,-8.245486]],[[-8.656116,-2.917802,-7.886510,7.970161,-4.704407,1.610920,-0.204797,6.766389,-6.812644,-9.986144,-7.927659,-5.922128],[5.331821,5.046201,6.299341,0.012898,8.823447,-5.239855,8.110757,-2.785012,-8.747616,-6.022765,-1.624106,2.470089],[-5.745366,-1.061604,-0.267913,-3.887697,5.555805,-0.546138,-6.848800,-7.505906,8.048830,2.063949,4.861475,9.859644],[5.400045,-2.458024,4.956114,-6.682596,2.704410,-8.580909,4.747630,-1.420217,-9.047537,-3.817337,-6.082521,-3.486397],[1.896445,-8.188693,6.271311,1.944866,3.195744,2.951075,6.428796,-1.158808,-0.705658,6.137378,-3.193055,-7.446265],[-7.735589,1.415289,-6.217898,-5.894976,7.937673,-4.324823,-0.672984,3.002365,8.638094,-8.456250,5.678498,-7.620156],[7.845750,3.814875,4.111905,-3.689849,-3.453123,-9.603230,8.646221,3.303414,-0.356508,-5.975037,0.346775,-9.941797],[-1.384882,4.748850,-9.977501,1.863762,6.160658,1.625548,2.836861,-7.833874,6.571381,-6.985039,-0.330798,1.933219],[5.603705,1.667631,0.068450,0.436968,3.142748,3.727746,-1.010648,2.080012,-3.261857,-5.281313,8.131015,7.181291],[-3.698102,2.297011,3.261472,8.875140,-8.835403,6.355738,-4.787747,6.037707,-8.970291,0.174004,-6.989152,-7.612789]],[[7.329900,-7.963126,-4.555444,4.464522,7.184826,6.971873,5.551256,8.850631,8.189917,-9.992449,9.407393,9.805333],[-4.533924,7.714787,-8.495906,1.901676,-2.057535,-8.032468,-8.773415,0.508687,-9.668483,-1.978667,9.378466,-3.864311],[4.330365,1.077445,-2.708142,-8.660050,4.362015,9.127241,5.513915,-3.437305,-5.646544,-7.365896,-2.746145,-7.213258],[-6.376120,6.192729,-1.103495,9.332434,-5.629359,3.032477,8.619312,1.075071,5.083179,-9.799033,-1.057315,-3.993808],[4.663832,7.422292,9.787105,3.498255,-7.621331,7.295784,-7.161639,-0.224374,7.974732,9.286693,7.970105,-7.287543],[-7.846055,-3.316410,2.094083,6.822229,1.999627,-9.820660,0.062084,6.251410,-0.649699,-5.136303,1.191782,2.729051],[-1.430191,2.826375,-1.384830,-4.355754,7.959915,4.759383,-6.183384,5.275688,3.193852,-7.425677,9.975023,-4.489095],[-0.583627,-3.867580,-3.802793,8.540606,8.933198,-9.412717,-1.320663,-9.473620,1.677414,-4.529766,-7.411540,-0.870657],[6.167125,-0.221762,-3.268575,9.861616,-9.297895,-8.820942,2.159994,2.546161,-8.722615,-0.015885,3.009514,-3.433637],[-1.488845,-6.601283,3.436686,-3.239051,1.253237,0.288636,-9.311862,-3.582383,3.478732,3.575726,-5.868635,4.528342]],[[-3.360836,3.652546,-1.636818,0.822218,-3.358550,5.078665,-8.136132,9.368438,8.426867,4.891200,1.770240,-2.609995],[-5.068350,2.689187,-3.883624,4.085712,4.636617,-1.351391,1.136772,-0.985982,3.617689,6.221038,-9.498465,3.684940],[7.145219,1.567340,7.069293,8.020668,3.901093,-2.498210,6.253988,-2.682576,9.670806,-4.374966,-5.044340,-7.021348],[9.690884,4.337749,-3.063028,4.446735,6.111649,-1.562340,-9.221451,-6.548715,9.978431,0.836715,4.927175,1.032331],[2.138968,4.045731,-5.180695,5.250610,2.882772,4.528643,-2.995537,0.486892,7.481769,-2.242794,-5.663887,3.633793],[9.918033,-4.532083,5.333447,0.832278,-8.781270,-5.702498,8.699106,-5.535548,3.421222,-8.393238,-3.512911,4.529319],[-3.535956,2.977300,6.604584,-1.840929,9.503898,9.354565,-0.269233,7.219517,9.900441,4.336190,-4.126123,6.185328],[-8.724014,7.637004,4.793850,-7.187894,-0.305345,-6.727200,1.066501,-5.175119,-0.548981,9.950642,5.387730,3.458048],[-3.716811,7.424511,-7.496258,-8.777471,-7.408098,7.633495,9.293100,6.652981,4.507722,2.954052,-5.952052,3.644961],[4.802533,0.393004,-3.576996,0.949941,-6.839010,0.409274,6.865009,0.234506,8.264251,1.934110,-6.951978,-4.928121]],[[0.411257,-5.288088,7.543302,-3.615992,-8.621645,3.654208,-3.608818,-4.012783,9.878675,8.981673,7.814321,3.465264],[5.187571,3.308613,9.273872,9.007989,1.988127,2.886294,9.021367,7.144228,7.396644,-5.970576,0.758739,-7.091365],[-0.439552,7.962375,-3.239887,-7.159959,-6.083686,-1.129816,8.238379,-8.984433,3.161242,-6.777101,3.561018,3.025661],[-3.849858,-6.591345,-5.501059,5.593564,-9.528958,-2.446718,8.499180,-7.525603,1.233825,5.081329,-5.169353,9.414327],[0.803679,-9.095352,-8.017246,-5.764932,-1.140612,-6.641196,5.648496,0.949019,9.948775,1.935654,8.425010,-6.328363],[-8.576037,6.735645,0.301507,-1.116567,-4.331980,4.802144,-4.852185,-7.149581,-4.783061,3.760864,-2.069615,2.478599],[4.799549,-6.977773,-9.680600,7.530293,-3.695312,1.913017,8.624893,2.540256,-0.544455,-9.029727,-8.183217,8.556803],[-4.821124,-9.776029,-1.408659,-8.021946,-1.374283,-6.679792,4.461504,3.790533,-4.763619,6.745377,6.560373,-6.581990],[3.028287,-0.579246,9.438675,-5.426486,5.833681,-4.816052,-0.444411,7.860187,7.304580,9.970328,9.221631,-2.369857],[9.760372,7.098078,-3.375399,-1.258756,9.148624,9.379952,3.422626,-9.680675,1.389153,-1.544955,2.328441,-9.767443]],[[3.673267,2.147687,2.830455,-9.570991,1.184153,2.059107,3.556283,7.720959,-6.906360,0.185584,-7.441108,-3.384030],[-8.028051,8.182848,-7.866813,-8.005610,1.783591,-1.310184,-4.006282,7.496201,6.293246,8.308361,-0.752491,1.646100],[-6.484335,-9.040798,-1.148583,-0.071572,7.988718,-4.101391,2.170761,3.259028,-7.609589,2.144666,9.160063,-3.101382],[1.018988,8.508502,-1.133919,6.283201,-0.638690,7.464336,-0.053300,3.407795,4.871245,-2.199067,5.068282,2.469029],[4.949317,-5.726409,2.750366,1.409640,-3.670517,-1.757132,7.720848,8.017683,-9.475077,-6.558719,-5.457457,-5.222808],[1.183289,2.442240,1.673722,-2.895418,3.528955,5.133288,3.021143,-7.855003,1.208566,-7.314354,-0.538595,-5.847274],[-9.133276,5.897444,2.954488,-7.146043,-1.549457,6.878938,-8.994221,8.751373,-4.858166,-3.061297,6.248333,7.614259],[-6.676448,-4.113473,-6.384155,6.664046,5.802418,6.092332,-8.742705,-1.630669,9.348221,-8.408920,3.445641,-8.188221],[-7.907112,-0.862265,9.706804,7.521578,7.707207,-0.939298,-4.957494,1.195999,-2.818310,-1.650467,-8.506159,-4.447373],[-8.981801,-2.805163,-6.197272,1.173744,8.367581,-9.454777,-5.974285,-2.525715,0.130424,6.126637,-4.240145,-2.937822]],[[7.664049,-1.998658,3.068297,-8.389035,5.319125,6.839056,4.598840,3.154418,-9.752650,8.767034,8.002000,9.868899],[-7.781459,-6.974777,4.922088,5.474044,-0.070932,-5.938475,-4.498969,6.605229,0.371364,5.282147,-5.514282,-1.228092],[1.780889,0.891913,7.732251,4.599296,5.433040,7.406051,-7.059811,7.169669,-7.455781,-6.814497,-6.642190,-9.538900],[9.523903,-3.057874,-0.405148,-2.677201,-8.322491,-7.805613,-5.779888,5.071572,-0.899822,-2.911109,-1.304093,4.508429],[-3.772234,3.882094,8.252128,-0.475596,-4.757910,-6.662775,2.550677,-6.981584,-2.309450,-9.130276,-5.793935,-6.562221],[-9.536424,-3.589069,0.357554,8.673309,6.357723,-8.498659,-8.105907,1.569697,-4.051182,-3.538126,0.351877,9.028736],[0.323391,-6.849178,-2.477381,-7.088200,-4.062655,8.498265,-1.319587,8.984354,2.105197,2.474770,-0.636538,-1.823424],[-1.234107,4.178539,1.195476,-1.582319,-6.383204,0.105228,2.692318,4.964489,-0.486586,9.464054,7.929963,-6.510132],[5.819976,-2.147482,9.472611,-6.064619,3.581677,6.380026,-1.361330,-0.661048,-1.244939,6.983357,1.429055,7.660737],[2.786570,3.959506,1.654008,-9.182471,9.620786,4.615856,8.896688,-0.295565,0.948409,-5.466557,6.597015,-4.610758]],[[-6.779047,-4.512367,-9.340318,2.126023,-1.025586,-6.962254,-4.065194,-4.879327,8.624747,-7.496665,6.446706,-4.756398],[-4.201896,2.012141,4.076491,-6.008916,5.586937,2.249625,-5.189193,-8.478704,7.635990,7.415586,9.954922,1.709777],[1.039265,3.333442,1.067061,5.116314,-6.980962,3.931091,-6.483626,2.862703,-3.097664,2.100103,7.670862,-6.073553],[-9.578794,9.301682,8.675247,-6.152086,-5.717970,-7.223466,7.691123,-2.465333,-4.209896,0.358126,6.349086,-7.739810],[-0.562366,-9.586209,2.084122,-5.229718,-9.953359,0.109260,9.138324,-4.648929,-6.325996,7.268182,-9.218995,5.902960],[9.630804,5.843610,-8.063272,1.211443,1.818081,-7.733033,-2.556972,-5.109802,-9.178233,-4.138506,-2.878505,-5.236373],[2.081620,-0.022966,0.406530,-3.416746,3.861699,3.593481,-3.418014,-3.268489,-8.996164,-1.057720,7.730094,-5.558850],[3.763141,9.738147,1.743791,-3.468411,5.529342,7.458469,-2.493571,-4.184773,4.801919,5.374096,-4.369563,-7.387688],[4.402454,5.719399,4.132400,-2.444342,-5.811476,-3.461595,2.365457,1.503335,-7.076193,3.984920,-5.219820,-3.349361],[2.650623,8.136028,1.863253,2.074550,9.304383,6.228885,-7.165258,0.343484,-1.982761,-6.359211,-2.014739,-8.604453]],[[-9.491086,1.046515,6.620219,8.831277,-2.017243,-5.965502,-8.991320,-2.810013,-6.081148,-8.923101,7.011108,-0.702259],[-3.770285,-3.682370,-1.249392,6.668523,-0.176010,0.911975,-7.949954,1.305477,-0.788552,-9.902314,6.614196,-9.769607],[-3.819063,-4.904336,-5.127756,2.609546,2.591336,9.615724,8.380283,6.633584,1.554265,0.934884,9.160341,-2.068902],[6.863617,-1.041539,5.020003,-3.768331,9.050514,-0.792786,5.654110,-5.663595,5.061531,-9.991110,-2.152946,-0.698905],[2.275264,9.011609,-1.359197,-8.026017,-9.510211,-9.282199,7.366182,-2.324804,8.855346,-9.264933,-5.580635,-5.963087],[-7.328056,-2.938499,-4.546100,-0.802533,6.340625,-3.521482,-9.267057,4.754697,0.031084,-9.719393,-3.484512,1.379944],[2.823233,2.404046,0.095792,3.634692,-5.643035,-3.964286,2.394548,-4.461189,0.778625,-1.774968,1.986854,-0.258962],[-7.079694,0.554315,6.911937,-4.708388,-9.780107,1.247521,0.712381,8.340866,-8.100345,-7.776063,4.553152,-7.658207],[0.155217,-3.108019,-5.902184,6.262141,7.901125,-8.172275,-1.790315,-6.883027,-1.531465,-5.085941,-4.703294,8.625040],[2.649968,-0.803212,4.642104,0.347930,-0.057211,1.942462,3.746649,0.210599,-6.809671,5.157540,-0.891421,9.656553]],[[7.871713,1.005581,-7.287571,5.992787,-3.617102,-0.632381,-4.500597,1.220380,5.749271,-9.656336,2.423623,7.375188],[1.408763,-0.081508,-7.201386,-1.747909,3.065907,-4.104503,-2.925884,-6.565399,7.931730,-0.872119,-4.068014,-6.124872],[9.527012,-9.746499,-3.451690,-5.971396,0.106656,-2.764353,-8.668792,4.663489,-0.446595,1.799123,3.251660,7.223658],[-1.676059,5.993295,5.092341,-5.675844,-0.724093,-1.247648,3.667184,-1.787637,6.088895,-7.509919,1.644729,-0.771812],[4.955093,-9.403027,5.201292,-8.485045,-6.740253,-6.184280,6.482093,-1.307437,-6.722430,9.076305,1.401642,-9.718110],[-4.266471,-8.253115,-2.586178,0.411455,7.011697,2.088571,0.007538,-6.730449,5.535547,-3.860136,-7.354322,-5.413266],[7.986498,-0.333798,4.061336,0.953482,3.121605,9.783959,-3.168175,-7.714478,-1.313970,-0.806246,6.741052,9.119725],[-0.291839,4.906903,-5.743434,7.332070,5.617449,-4.614163,-8.420634,-0.165095,-3.419245,2.899635,-0.384130,-3.409303],[2.737435,8.112698,9.768621,4.229250,-3.118305,-0.898863,-9.880535,-0.678836,7.663321,-8.372640,-4.725954,-1.778886],[-9.351891,-4.160633,5.645127,-5.457923,1.045605,9.129378,-6.762901,-6.475906,7.065494,-3.260958,-7.059567,-3.631446]],[[4.768093,4.400253,0.463863,-6.924160,-5.074279,4.429285,4.739713,-4.702201,6.559724,-2.954034,9.667920,-1.757566],[0.116486,-6.152001,2.381506,-3.424795,-6.678583,-3.911729,6.327198,4.778878,4.772165,3.108503,-1.201979,-5.195081],[7.486084,-6.864365,9.859490,4.982752,7.313086,5.128459,-7.234436,8.757071,5.801853,0.914661,0.009778,-2.743424],[1.445276,1.030373,-4.921034,9.070653,-6.105996,-0.118273,-5.039918,5.480148,1.947752,-0.170319,-8.613417,-8.647853],[7.768039,-7.554418,9.472767,-0.645907,-8.387594,-2.391836,5.006481,-7.721570,7.540821,3.458740,-3.776021,5.552374],[5.930530,-3.041455,-8.381653,-1.218002,-0.802341,-4.859038,5.688716,-0.520497,-2.629158,-4.855816,-7.639103,-1.525142],[4.526986,8.129465,-7.429053,-6.646682,-9.923962,3.427187,3.809439,-1.882285,-7.859691,1.957700,9.069881,5.411572],[3.049933,4.929380,-7.573314,4.947546,-7.027174,2.444852,-9.336900,-6.232251,-3.298140,5.254376,4.172699,1.109034],[-3.724174,-9.908233,-5.823848,0.163035,7.633834,0.427466,-2.326399,-7.344843,3.901643,6.105362,1.801939,-8.294900],[0.914744,7.949150,-0.917938,-5.911400,-7.996988,-0.156463,-5.833288,-4.246020,0.464434,3.227719,-2.345171,-9.367747]]], dtype = "float32")#candidate|1537|(15, 10, 12)|const|float32
var_1538 = relay.var("var_1538", dtype = "float32", shape = (15, 10, 12))#candidate|1538|(15, 10, 12)|var|float32
bop_1539 = relay.mod(const_1537.astype('float32'), relay.reshape(var_1538.astype('float32'), relay.shape_of(const_1537))) # shape=(15, 10, 12)
func_939_call = mod.get_global_var('func_939')
func_942_call = mutated_mod.get_global_var('func_942')
var_1549 = relay.var("var_1549", dtype = "uint32", shape = (294,))#candidate|1549|(294,)|var|uint32
call_1548 = relay.TupleGetItem(func_939_call(relay.reshape(var_1549.astype('uint32'), [3, 14, 7])), 0)
call_1550 = relay.TupleGetItem(func_942_call(relay.reshape(var_1549.astype('uint32'), [3, 14, 7])), 0)
func_1197_call = mod.get_global_var('func_1197')
func_1198_call = mutated_mod.get_global_var('func_1198')
call_1551 = relay.TupleGetItem(func_1197_call(), 0)
call_1552 = relay.TupleGetItem(func_1198_call(), 0)
output = relay.Tuple([bop_1539,call_1548,var_1549,call_1551,])
output2 = relay.Tuple([bop_1539,call_1550,var_1549,call_1552,])
func_1559 = relay.Function([var_1538,var_1549,], output)
mod['func_1559'] = func_1559
mod = relay.transform.InferType()(mod)
mutated_mod['func_1559'] = func_1559
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1559_call = mutated_mod.get_global_var('func_1559')
var_1561 = relay.var("var_1561", dtype = "float32", shape = (15, 10, 12))#candidate|1561|(15, 10, 12)|var|float32
var_1562 = relay.var("var_1562", dtype = "uint32", shape = (294,))#candidate|1562|(294,)|var|uint32
call_1560 = func_1559_call(var_1561,var_1562,)
output = call_1560
func_1563 = relay.Function([var_1561,var_1562,], output)
mutated_mod['func_1563'] = func_1563
mutated_mod = relay.transform.InferType()(mutated_mod)
func_506_call = mod.get_global_var('func_506')
func_507_call = mutated_mod.get_global_var('func_507')
call_1582 = func_506_call()
call_1583 = func_506_call()
output = relay.Tuple([call_1582,])
output2 = relay.Tuple([call_1583,])
func_1584 = relay.Function([], output)
mod['func_1584'] = func_1584
mod = relay.transform.InferType()(mod)
mutated_mod['func_1584'] = func_1584
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1584_call = mutated_mod.get_global_var('func_1584')
call_1585 = func_1584_call()
output = call_1585
func_1586 = relay.Function([], output)
mutated_mod['func_1586'] = func_1586
mutated_mod = relay.transform.InferType()(mutated_mod)
func_926_call = mod.get_global_var('func_926')
func_928_call = mutated_mod.get_global_var('func_928')
call_1630 = relay.TupleGetItem(func_926_call(), 1)
call_1631 = relay.TupleGetItem(func_928_call(), 1)
output = relay.Tuple([call_1630,])
output2 = relay.Tuple([call_1631,])
func_1633 = relay.Function([], output)
mod['func_1633'] = func_1633
mod = relay.transform.InferType()(mod)
output = func_1633()
func_1634 = relay.Function([], output)
mutated_mod['func_1634'] = func_1634
mutated_mod = relay.transform.InferType()(mutated_mod)
func_685_call = mod.get_global_var('func_685')
func_687_call = mutated_mod.get_global_var('func_687')
call_1645 = relay.TupleGetItem(func_685_call(), 0)
call_1646 = relay.TupleGetItem(func_687_call(), 0)
func_1104_call = mod.get_global_var('func_1104')
func_1107_call = mutated_mod.get_global_var('func_1107')
var_1652 = relay.var("var_1652", dtype = "int64", shape = (360,))#candidate|1652|(360,)|var|int64
var_1653 = relay.var("var_1653", dtype = "uint8", shape = (260,))#candidate|1653|(260,)|var|uint8
call_1651 = relay.TupleGetItem(func_1104_call(relay.reshape(var_1652.astype('int64'), [6, 10, 6]), relay.reshape(var_1653.astype('uint8'), [260,]), ), 0)
call_1654 = relay.TupleGetItem(func_1107_call(relay.reshape(var_1652.astype('int64'), [6, 10, 6]), relay.reshape(var_1653.astype('uint8'), [260,]), ), 0)
output = relay.Tuple([call_1645,call_1651,var_1652,var_1653,])
output2 = relay.Tuple([call_1646,call_1654,var_1652,var_1653,])
func_1662 = relay.Function([var_1652,var_1653,], output)
mod['func_1662'] = func_1662
mod = relay.transform.InferType()(mod)
mutated_mod['func_1662'] = func_1662
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1662_call = mutated_mod.get_global_var('func_1662')
var_1664 = relay.var("var_1664", dtype = "int64", shape = (360,))#candidate|1664|(360,)|var|int64
var_1665 = relay.var("var_1665", dtype = "uint8", shape = (260,))#candidate|1665|(260,)|var|uint8
call_1663 = func_1662_call(var_1664,var_1665,)
output = call_1663
func_1666 = relay.Function([var_1664,var_1665,], output)
mutated_mod['func_1666'] = func_1666
mutated_mod = relay.transform.InferType()(mutated_mod)
func_731_call = mod.get_global_var('func_731')
func_732_call = mutated_mod.get_global_var('func_732')
call_1722 = func_731_call()
call_1723 = func_731_call()
output = relay.Tuple([call_1722,])
output2 = relay.Tuple([call_1723,])
func_1728 = relay.Function([], output)
mod['func_1728'] = func_1728
mod = relay.transform.InferType()(mod)
mutated_mod['func_1728'] = func_1728
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1728_call = mutated_mod.get_global_var('func_1728')
call_1729 = func_1728_call()
output = call_1729
func_1730 = relay.Function([], output)
mutated_mod['func_1730'] = func_1730
mutated_mod = relay.transform.InferType()(mutated_mod)
func_707_call = mod.get_global_var('func_707')
func_708_call = mutated_mod.get_global_var('func_708')
call_1731 = relay.TupleGetItem(func_707_call(), 0)
call_1732 = relay.TupleGetItem(func_708_call(), 0)
output = call_1731
output2 = call_1732
func_1745 = relay.Function([], output)
mod['func_1745'] = func_1745
mod = relay.transform.InferType()(mod)
output = func_1745()
func_1746 = relay.Function([], output)
mutated_mod['func_1746'] = func_1746
mutated_mod = relay.transform.InferType()(mutated_mod)
func_731_call = mod.get_global_var('func_731')
func_732_call = mutated_mod.get_global_var('func_732')
call_1820 = func_731_call()
call_1821 = func_731_call()
output = call_1820
output2 = call_1821
func_1834 = relay.Function([], output)
mod['func_1834'] = func_1834
mod = relay.transform.InferType()(mod)
mutated_mod['func_1834'] = func_1834
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1834_call = mutated_mod.get_global_var('func_1834')
call_1835 = func_1834_call()
output = call_1835
func_1836 = relay.Function([], output)
mutated_mod['func_1836'] = func_1836
mutated_mod = relay.transform.InferType()(mutated_mod)
func_561_call = mod.get_global_var('func_561')
func_562_call = mutated_mod.get_global_var('func_562')
call_1863 = relay.TupleGetItem(func_561_call(), 0)
call_1864 = relay.TupleGetItem(func_562_call(), 0)
output = call_1863
output2 = call_1864
func_1865 = relay.Function([], output)
mod['func_1865'] = func_1865
mod = relay.transform.InferType()(mod)
mutated_mod['func_1865'] = func_1865
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1865_call = mutated_mod.get_global_var('func_1865')
call_1866 = func_1865_call()
output = call_1866
func_1867 = relay.Function([], output)
mutated_mod['func_1867'] = func_1867
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1363_call = mod.get_global_var('func_1363')
func_1365_call = mutated_mod.get_global_var('func_1365')
call_1881 = func_1363_call()
call_1882 = func_1363_call()
output = relay.Tuple([call_1881,])
output2 = relay.Tuple([call_1882,])
func_1889 = relay.Function([], output)
mod['func_1889'] = func_1889
mod = relay.transform.InferType()(mod)
output = func_1889()
func_1890 = relay.Function([], output)
mutated_mod['func_1890'] = func_1890
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1363_call = mod.get_global_var('func_1363')
func_1365_call = mutated_mod.get_global_var('func_1365')
call_1906 = func_1363_call()
call_1907 = func_1363_call()
output = relay.Tuple([call_1906,])
output2 = relay.Tuple([call_1907,])
func_1911 = relay.Function([], output)
mod['func_1911'] = func_1911
mod = relay.transform.InferType()(mod)
mutated_mod['func_1911'] = func_1911
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1911_call = mutated_mod.get_global_var('func_1911')
call_1912 = func_1911_call()
output = call_1912
func_1913 = relay.Function([], output)
mutated_mod['func_1913'] = func_1913
mutated_mod = relay.transform.InferType()(mutated_mod)
func_242_call = mod.get_global_var('func_242')
func_243_call = mutated_mod.get_global_var('func_243')
call_1918 = relay.TupleGetItem(func_242_call(), 0)
call_1919 = relay.TupleGetItem(func_243_call(), 0)
func_953_call = mod.get_global_var('func_953')
func_954_call = mutated_mod.get_global_var('func_954')
call_1933 = func_953_call()
call_1934 = func_953_call()
func_1363_call = mod.get_global_var('func_1363')
func_1365_call = mutated_mod.get_global_var('func_1365')
call_1941 = func_1363_call()
call_1942 = func_1363_call()
output = relay.Tuple([call_1918,call_1933,call_1941,])
output2 = relay.Tuple([call_1919,call_1934,call_1942,])
func_1947 = relay.Function([], output)
mod['func_1947'] = func_1947
mod = relay.transform.InferType()(mod)
output = func_1947()
func_1948 = relay.Function([], output)
mutated_mod['func_1948'] = func_1948
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1363_call = mod.get_global_var('func_1363')
func_1365_call = mutated_mod.get_global_var('func_1365')
call_1949 = func_1363_call()
call_1950 = func_1363_call()
output = relay.Tuple([call_1949,])
output2 = relay.Tuple([call_1950,])
func_1964 = relay.Function([], output)
mod['func_1964'] = func_1964
mod = relay.transform.InferType()(mod)
mutated_mod['func_1964'] = func_1964
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1964_call = mutated_mod.get_global_var('func_1964')
call_1965 = func_1964_call()
output = call_1965
func_1966 = relay.Function([], output)
mutated_mod['func_1966'] = func_1966
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1964_call = mod.get_global_var('func_1964')
func_1966_call = mutated_mod.get_global_var('func_1966')
call_1999 = relay.TupleGetItem(func_1964_call(), 0)
call_2000 = relay.TupleGetItem(func_1966_call(), 0)
uop_2013 = relay.exp(call_1999.astype('float64')) # shape=(6, 1, 6)
uop_2015 = relay.exp(call_2000.astype('float64')) # shape=(6, 1, 6)
bop_2025 = relay.floor_divide(uop_2013.astype('float64'), relay.reshape(call_1999.astype('float64'), relay.shape_of(uop_2013))) # shape=(6, 1, 6)
bop_2028 = relay.floor_divide(uop_2015.astype('float64'), relay.reshape(call_2000.astype('float64'), relay.shape_of(uop_2015))) # shape=(6, 1, 6)
bop_2038 = relay.add(bop_2025.astype('int32'), relay.reshape(call_1999.astype('int32'), relay.shape_of(bop_2025))) # shape=(6, 1, 6)
bop_2041 = relay.add(bop_2028.astype('int32'), relay.reshape(call_2000.astype('int32'), relay.shape_of(bop_2028))) # shape=(6, 1, 6)
var_2042 = relay.var("var_2042", dtype = "float64", shape = (6, 9, 6))#candidate|2042|(6, 9, 6)|var|float64
bop_2043 = relay.less(bop_2025.astype('bool'), var_2042.astype('bool')) # shape=(6, 9, 6)
bop_2046 = relay.less(bop_2028.astype('bool'), var_2042.astype('bool')) # shape=(6, 9, 6)
uop_2051 = relay.asinh(var_2042.astype('float32')) # shape=(6, 9, 6)
output = relay.Tuple([bop_2038,bop_2043,uop_2051,])
output2 = relay.Tuple([bop_2041,bop_2046,uop_2051,])
func_2059 = relay.Function([var_2042,], output)
mod['func_2059'] = func_2059
mod = relay.transform.InferType()(mod)
var_2060 = relay.var("var_2060", dtype = "float64", shape = (6, 9, 6))#candidate|2060|(6, 9, 6)|var|float64
output = func_2059(var_2060)
func_2061 = relay.Function([var_2060], output)
mutated_mod['func_2061'] = func_2061
mutated_mod = relay.transform.InferType()(mutated_mod)
func_926_call = mod.get_global_var('func_926')
func_928_call = mutated_mod.get_global_var('func_928')
call_2083 = relay.TupleGetItem(func_926_call(), 0)
call_2084 = relay.TupleGetItem(func_928_call(), 0)
output = call_2083
output2 = call_2084
func_2107 = relay.Function([], output)
mod['func_2107'] = func_2107
mod = relay.transform.InferType()(mod)
output = func_2107()
func_2108 = relay.Function([], output)
mutated_mod['func_2108'] = func_2108
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2126 = relay.const([[[1,-3,10,-7,-4,-6,-10,-9,-6,-8,-3,-1,-7,-3],[8,-6,-7,-8,-4,-9,-7,-1,-5,6,1,8,-8,-10],[9,3,-1,8,9,4,10,4,-6,4,5,3,-5,-9]],[[2,-9,5,8,-10,1,-2,-3,-8,-10,1,-6,-6,-10],[3,-4,-9,4,5,-7,8,-4,-4,-3,-5,-7,-6,1],[-5,3,-10,-3,-9,2,-10,-9,-8,-9,2,-7,2,1]],[[8,-2,-5,-2,-1,6,1,4,-7,-8,-5,-9,8,4],[-9,-9,-9,3,5,10,8,6,4,-1,-10,-7,-5,-2],[4,4,-10,-4,4,-4,-1,-5,-2,10,-8,8,9,4]],[[4,8,1,3,7,-2,-3,9,5,-6,-2,5,-5,-9],[8,10,-7,-10,-2,-2,10,-9,-4,-10,-2,-6,-1,6],[3,2,-7,3,-3,-6,8,4,-4,3,-1,5,-7,8]],[[3,8,9,9,-4,-2,7,-4,8,5,8,7,10,3],[-6,-9,-4,7,9,-9,-10,2,1,-4,-1,-8,-8,-10],[-9,-10,-3,6,-6,-9,8,-7,-9,8,4,-6,3,-6]],[[8,-1,-1,4,8,9,2,8,-4,-8,2,2,10,-1],[-3,-3,-6,-10,7,-9,3,-10,6,2,-1,-4,8,10],[-5,10,1,8,10,-2,-1,2,1,-8,-10,-6,3,-5]],[[-7,1,-8,-9,-4,4,-5,3,-9,2,6,6,10,-6],[-1,6,-6,9,7,10,-5,7,3,7,-4,-4,1,-8],[-4,-6,5,-5,8,-2,-2,-6,9,6,-3,7,-4,-10]],[[3,-5,-10,1,2,6,-10,7,-3,6,8,5,4,1],[-3,2,8,-10,-8,-6,7,-4,-2,-6,6,6,-3,-7],[3,5,-10,-9,-4,-9,-9,5,-6,-2,10,5,7,9]],[[-2,-7,6,-10,-6,-5,7,-3,8,2,-8,4,2,3],[-1,-1,1,-10,9,3,1,6,-9,-4,-8,1,-3,-4],[-4,-6,1,8,5,-9,9,10,8,-8,6,4,-2,-1]],[[-9,2,2,-6,5,-7,5,-7,-9,-4,4,6,6,5],[4,-5,-1,-6,-6,7,10,4,-1,-10,7,-7,-8,10],[-4,5,10,-3,-6,-3,-1,4,6,7,-8,-6,-2,7]],[[-10,7,-3,-4,-10,-4,-3,-9,-9,8,-2,1,-1,-6],[-3,-5,1,7,-4,-6,7,3,9,6,8,3,10,-9],[-4,6,-9,2,-4,-3,-1,5,9,8,1,-7,-10,6]],[[-6,-1,-3,10,9,-3,3,1,4,-2,3,10,7,-2],[10,9,4,-8,8,-10,-2,-1,-8,-8,10,5,3,-9],[5,-9,9,10,-7,-2,-8,3,-5,4,-9,-8,-4,2]],[[2,-10,-3,3,5,5,4,9,10,-10,6,-10,8,-4],[3,-2,9,4,-8,-2,-10,7,4,8,9,9,-3,2],[9,4,4,-6,7,-5,-7,-2,-3,5,-6,-1,10,-10]],[[-9,4,8,9,-5,5,7,9,-6,-4,-9,-6,1,-7],[7,6,10,3,8,-2,-7,5,4,9,-4,-10,-4,-5],[6,-8,1,-9,3,-3,-4,-6,-9,-6,-6,4,1,-10]],[[-2,10,8,1,9,4,-3,-5,-9,7,-1,-2,9,-6],[2,5,-2,2,-2,-1,4,-5,4,2,-10,-3,4,-9],[-5,-5,-10,1,-5,3,-5,-10,-2,3,-4,1,-6,8]],[[-2,-4,1,-4,-10,-6,5,2,-4,8,-7,5,-6,9],[1,-1,-4,1,-4,10,-9,7,-6,3,-3,-7,2,4],[-8,-9,8,-3,-6,-2,1,-2,-8,4,2,-3,8,5]]], dtype = "uint16")#candidate|2126|(16, 3, 14)|const|uint16
var_2127 = relay.var("var_2127", dtype = "uint16", shape = (16, 3, 14))#candidate|2127|(16, 3, 14)|var|uint16
bop_2128 = relay.less_equal(const_2126.astype('bool'), relay.reshape(var_2127.astype('bool'), relay.shape_of(const_2126))) # shape=(16, 3, 14)
uop_2135 = relay.sin(bop_2128.astype('float64')) # shape=(16, 3, 14)
uop_2139 = relay.log10(uop_2135.astype('float32')) # shape=(16, 3, 14)
func_1559_call = mod.get_global_var('func_1559')
func_1563_call = mutated_mod.get_global_var('func_1563')
const_2156 = relay.const([-5.947562,1.491327,-3.270852,-2.533487,2.030017,6.505062,-8.399823,-6.142272,-0.643604,-6.962366,-0.646740,6.028742,-4.259583,-3.753352,8.611939,3.232648,-6.582807,4.097076,-9.449129,-8.945851,8.499299,-2.214411,-9.622979,-2.003007,-8.033788,-4.625990,-0.451907,6.868593,5.710686,-9.971088,4.082590,0.909608,-4.530474,-8.508312,-7.304843,4.266448,-5.285425,9.213184,-4.695055,5.990011,-5.820240,7.114329,-1.730834,0.451235,1.638070,-2.320085,1.844799,-3.721079,-1.141920,-6.085368,4.831724,5.299783,5.705103,-2.075850,-7.520226,2.713450,1.530269,-8.013387,6.530206,-8.473433,0.677148,2.694329,-8.538743,8.334039,-6.233915,2.539386,5.606684,-3.453642,8.131200,-1.077624,-2.998767,-7.121368,-3.226264,3.459714,-3.498674,-1.346579,4.799726,-6.496303,8.942500,-1.073224,-0.131291,1.056409,-6.764120,-7.527975,-2.570599,-7.749932,-7.929985,7.211612,9.020243,-3.188121,-2.901134,6.080231,-9.796672,6.263564,2.981301,-9.508158,0.161683,8.282857,8.171941,8.145307,-2.225971,-8.431264,-2.896743,-0.784309,7.989065,2.773932,4.955243,7.103571,-7.015233,-3.666399,-9.017686,8.364891,-0.742383,-0.976248,9.351435,-7.758920,4.793245,-3.296106,-2.752317,6.327786,-5.961130,7.578524,3.972908,1.250225,1.417383,-0.190297,-0.533663,1.267420,-7.855466,-1.203227,2.871881,-1.126115,-4.606445,-5.357717,4.783023,-0.255179,-3.209279,8.632628,-3.288767,8.726353,-1.971519,0.881954,-6.400731,-6.305748,-9.520897,-3.222763,2.380800,-9.872416,8.412570,-8.611366,-3.689548,-8.907879,-7.497430,5.123563,8.215386,-9.400348,-9.074364,-3.386339,-8.245944,0.085669,-0.852413,-7.347803,-2.582437,9.760947,0.387463,-9.479352,-4.270417,-5.547041,4.430967,6.358713,-7.172742,-8.271885,3.768384,9.650532,3.948239,8.229250,-0.027797,6.095822,-1.353399,5.229804,-2.561640,-2.541294,-0.247215,7.169945,-8.463117,-3.818131,-2.947847,4.032848,-1.668904,3.628463,3.903162,0.570492,-2.215527,6.435658,8.644194,-1.544256,-2.965357,-1.930649,1.193979,-6.258810,-2.871161,6.587560,-8.660792,-0.922155,8.983598,-0.993099,-9.852887,3.879492,4.594894,-3.178222,6.109393,-1.470077,7.942255,-0.624547,8.447073,-5.159379,-0.212457,-3.131945,-1.563478,8.930006,9.636273,-2.248334,0.870364,-5.198247,-5.482504,8.240162,-2.887949,-4.083982,-9.495650,-1.944879,7.430938,1.018518,-8.233758,-4.843471,-8.444758,0.810487,-3.556436,-1.322440,2.169446,-5.013724,0.410925,1.285382,9.987500,2.262145,-3.107325,4.171570,-4.531408,8.564047,6.254442,5.489947,2.330765,1.745750,-2.664873,2.246958,-9.691502,-7.009910,6.980986,5.888376,6.569361,-9.216263,3.212836,0.484970,-7.817629,-7.637821,3.543597,-0.554440,-4.141467,-0.500840,0.816461,-3.323658,6.545572,6.240752,-0.885220,5.669061,7.284266,-1.727963,-4.539819,-3.690978,-3.123199,-1.733813,-8.926925,5.047067,-3.211210,0.835706,4.751799,8.573061,-6.399421,-3.045454,-2.909248,-8.136524,9.224243,-4.135369,5.092994,9.466878,1.603728,2.462408,-1.625016,7.469617,-9.679495,-0.144115,-3.705752,-4.035890,-2.044546,-3.371955,-5.842690,-9.582621,5.926480,4.154815,4.711915,-4.483595,-9.448090,-2.716707,-8.557281,1.108822,-3.656212,6.573549,-6.840094,-7.652051,-6.565181,3.222541,5.923951,-4.316959,-2.810311,4.467277,-1.434494,-2.858612,6.147367,1.354922,-1.451860,-0.264311,-8.407559,-1.722419,8.612202,6.301366,2.191628,5.365080,-8.076262,5.825290,8.397148,-1.891259,-5.432077,0.644167,9.661507,-4.256678,9.183355,9.119588,-6.473600,-2.091123,-0.070132,4.972035,-5.498390,-7.188090,-7.584567,2.424142,1.301325,-7.128882,1.958813,0.498690,-5.508629,-0.433467,9.389352,-1.404562,7.799738,6.828301,-3.483512,4.806882,1.518925,-7.197642,0.215159,-3.903828,7.339628,1.405897,-6.554432,-8.674124,-5.358477,-4.646512,-3.298094,9.578474,-2.529002,1.152863,4.424849,3.663715,-2.139001,-2.972520,-8.055222,-1.797848,6.709709,-5.090483,9.753663,9.844533,6.202590,4.019679,-3.974470,-2.263846,0.182982,4.159353,-6.781612,-0.649313,-5.125307,0.755538,9.979384,7.298141,7.438183,-4.438888,-5.484737,-6.950950,4.062626,7.832264,-4.625885,-6.242919,2.405431,-8.707117,6.774693,-7.996205,7.493042,-9.792267,-0.603813,-8.674946,4.259540,-7.839307,-2.602438,7.482531,-7.160667,2.412588,-5.595936,-8.368274,4.115648,-7.771370,6.948482,9.607181,-9.783622,2.084947,5.908973,-1.874445,-2.720549,-5.348523,6.518982,6.003605,-7.152941,-2.843289,-3.034938,-9.772656,5.981450,-8.253661,7.258861,5.801913,4.603068,-5.760712,-7.184108,9.191782,7.039264,7.771918,-1.259673,-3.426551,9.181679,7.708218,-9.611844,-4.012329,-7.846036,-7.817699,-0.013172,9.639629,8.254437,-3.391646,-6.194965,-1.448408,8.095484,-1.861994,-5.644248,-4.811846,4.176323,-1.348941,4.871995,2.539854,6.949092,0.009871,-8.589246,-2.387747,4.946911,5.662354,-9.912904,3.453089,-9.148436,5.093711,2.812614,-3.362608,-5.771080,-6.910089,2.424953,1.701551,5.306040,-5.530351,-8.556599,2.769619,5.346063,0.806233,7.896627,0.603660,9.424930,-5.950447,-1.392193,8.658906,8.228273,-6.133800,-0.660669,-3.919650,9.154582,9.973093,2.526395,2.209098,9.148436,-9.801288,6.078225,-4.402754,5.001096,0.265736,-5.224343,-8.892381,-2.274063,-2.001762,-0.676979,2.017471,-5.908079,6.167448,5.601664,-8.460008,-9.823254,0.318053,7.760681,-8.232310,9.548545,-4.138064,-4.977715,6.350666,-5.882770,2.819816,-3.449077,-4.654497,6.355473,-7.562838,-5.409876,-8.840579,-3.218206,-6.184719,7.376052,-4.558565,2.777306,-0.821114,2.733361,-6.947768,-6.293939,-6.780519,-0.365993,7.569259,9.974768,7.902030,-1.341606,-8.685689,1.254069,-6.692221,9.629439,6.274533,-0.471803,-1.146358,-7.054882,5.730965,7.165164,7.809243,-2.413847,8.694947,0.872326,9.256439,-2.096965,-4.748274,-5.744937,8.703877,6.489260,-5.857922,-0.566341,9.497292,-0.107937,3.990845,-5.956851,8.174016,1.142040,-7.378746,6.550055,8.478409,1.826652,-4.749092,-2.019437,2.481470,-5.465276,5.538166,5.762204,4.536631,3.140337,7.359768,-2.329624,-1.296667,8.160791,-7.462643,-6.607788,0.213214,7.258227,-0.059431,7.175873,6.558858,4.514430,-4.303850,3.808752,-9.504159,5.836717,-1.654176,9.397555,3.277138,-0.925322,2.333501,8.953869,-4.217030,-9.307777,8.685929,7.826037,-4.964441,1.004451,0.506850,-1.014126,-6.385469,3.356630,4.257266,8.393828,0.788079,-8.315775,1.272191,4.469217,-4.123018,-5.897395,2.868757,-2.832730,-2.782869,2.382910,-4.444832,-5.114362,7.607111,-7.543212,-4.751757,1.133929,8.140631,-5.730803,-3.203450,-6.979798,-7.967902,-7.394337,-7.859647,7.909690,-7.329801,-8.588951,-4.484403,0.379889,-5.294102,6.225965,-2.280560,9.991214,-4.371902,-8.191099,1.813761,-8.672519,9.894794,-5.293662,6.968554,-5.847175,-2.260095,5.382914,6.098874,-0.160798,-2.850794,-4.072059,-3.720640,-1.619173,-9.772507,9.322776,8.746733,2.288096,-6.243860,1.373477,7.459448,-8.213289,-2.753096,-2.184392,-7.891432,-7.777624,-7.867370,8.136868,-9.016732,-9.538093,-9.779664,-6.625216,0.168190,-9.095310,1.003059,3.561655,-1.915261,-3.099021,0.878753,-5.971047,9.849672,-2.972849,-4.062079,4.872144,6.345609,3.328263,5.208395,-2.908255,4.707275,4.720245,-1.776084,1.570156,-4.467442,6.789565,-7.289853,9.036109,-4.697526,-2.122600,-5.291195,7.601519,1.258521,2.350081,3.953059,9.824770,4.251579,2.653624,1.220310,-3.236261,9.846860,-3.539314,9.073746,3.846129,1.300302,-9.818833,0.874940,-9.307151,-3.222477,-1.350335,6.282214,-2.912326,-6.134890,-6.344164,-4.893047,5.142310,-7.849305,-7.923474,6.849989,-6.025826,6.940969,-2.722019,-4.586982,0.409660,4.243725,-7.483344,9.584569,2.511573,1.623491,8.384967,-0.237013,8.085033,-4.631862,-9.346032,9.467322,4.818000,-4.858525,-4.223110,-0.830828,3.414412,9.327279,-3.173321,0.624284,-3.471103,6.986768,-3.468412,-1.330576,-3.646154,8.475415,-4.176108,0.670923,7.469955,-0.706258,2.773838,6.118572,-8.562385,-3.640460,9.655007,-6.460544,-8.624947,-5.354252,8.854029,-1.445153,0.721440,-6.476474,9.511835,7.866486,6.892864,-8.991833,-9.294052,-8.518627,-1.711661,5.175832,-8.751002,6.501875,2.601542,4.029279,-0.391459,4.720752,-9.992901,0.334386,8.301408,-7.167595,-5.818078,3.549263,8.971222,3.442275,4.052423,6.011140,-7.352817,-6.971684,-7.557883,-4.117726,-1.688919,4.773435,-7.382365,-4.159116,3.120946,-4.868255,2.374497,9.601716,1.841664,-9.165867,0.938814,-5.053604,-0.132873,-7.338246,4.934847,7.111854,-0.074096,-9.252980,8.534859,-4.883467,1.403009,6.420149,1.230867,5.466203,0.827212,4.031384,-3.064823,2.602669,-5.388018,4.114457,-0.909246,5.563854,0.606574,3.588243,-8.170830,-3.065471,8.043880,-7.937527,-5.627219,1.267226,8.460648,-4.845918,2.817327,-4.885008,5.703952,4.014748,-4.442569,-7.412393,-3.762022,5.296890,-9.155211,-8.872425,9.536969,-7.087959,4.104767,2.755698,-6.243644,-5.767714,9.281299,3.729977,-4.810708,1.705359,-7.676644,2.587397,3.977963,6.845139,-1.826018,1.165605,3.955279,3.253578,-9.454952,7.794066,-9.939739,-7.789642,7.560313,0.584688,-2.053038,-4.126653,-1.191378,9.001578,-9.969799,5.250799,-8.799094,-7.569672,-9.775752,-8.705240,2.009167,9.065289,2.752856,5.355104,-2.849966,9.399692,8.324888,7.245876,8.784208,-4.556912,5.030900,-2.715109,-9.206320,1.593128,-6.545377,7.239206,-0.845465,3.434943,-7.290798,-7.534224,5.786137,6.738963,4.978840,8.343703,3.080593,4.492004,4.769174,0.861311,-3.228742,0.503143,-3.036123,-4.264904,1.038161,3.777109,7.798994,-4.094407,9.987650,9.294381,-2.970318,1.317313,-2.007232,9.158004,-7.395095,-8.384361,4.338754,5.262943,-8.892571,-8.406511,9.115333,-9.879695,0.883633,-2.553935,-9.648641,-6.930808,-2.473120,2.790253,-5.363746,-9.167320,2.861257,9.722144,-5.890089,-6.687892,5.023498,4.540079,-2.663353,5.202361,-0.928304,-9.604742,1.470464,-0.584575,-4.625188,6.992116,-8.758565,8.409801,-2.349570,-8.184870,4.092306,4.004574,-1.506771,-5.513246,-6.817019,-3.749544,4.686088,-9.705419,4.622800,-9.441511,-4.154180,-3.865292,0.823769,-9.618410,6.377552,3.449605,5.847521,9.981607,9.297298,6.555651,4.531271,-1.947981,-5.156725,3.293279,8.860766,-9.912752,0.705211,-6.978238,-0.892441,-4.652044,-6.141648,6.264840,6.926526,9.237575,-0.816025,-5.705540,-1.322737,-7.600209,4.562714,5.857265,8.989910,-5.701860,-0.530381,5.420418,6.684971,-9.097977,1.095999,-6.921056,-6.893155,0.067256,-2.892879,-1.205654,9.688228,5.715983,1.844635,2.582785,-7.333760,1.502534,9.697683,-5.334979,7.826148,-6.253884,-0.626567,4.011226,-5.274351,4.671012,-1.039989,9.865148,-0.801030,1.745130,0.431148,-7.698998,-9.701439,8.416789,-2.981308,3.859774,-1.966615,4.393024,-9.399244,-5.242193,6.709668,9.059076,6.209396,9.129397,0.323922,5.617527,-1.586260,8.379548,-6.136749,-9.379194,-0.954640,-1.699012,2.488956,7.527595,-2.998719,-3.286620,1.696155,8.301258,-2.551609,-9.863083,9.853893,4.637241,1.917741,0.156866,6.319210,-9.839164,3.451936,-6.682827,-7.488467,-3.955492,6.219118,9.608880,-6.850460,-9.321696,0.676086,-0.467835,-2.769603,-1.534774,-4.743078,9.810948,4.708506,4.800690,-9.645045,2.452154,8.077166,5.346267,-3.345403,3.707391,-4.282247,-8.777240,-2.166894,-4.471138,-8.773493,-2.919696,-8.773790,-7.675735,-8.460630,-2.172913,6.932606,5.305313,2.958209,-2.035107,0.872841,-1.494371,7.975291,-6.677092,-3.162139,-5.600838,1.547981,6.736677,9.156142,-4.323455,-3.912382,-5.970351,-9.204760,-5.181148,6.560860,-7.316721,6.150748,-8.344723,6.714959,-1.051928,6.106478,-9.474667,-6.589844,4.525320,0.383480,9.772136,-3.221183,0.808604,5.087190,3.751181,-6.895499,-3.187541,-3.127327,-8.228745,4.709753,8.811302,-3.227063,6.677423,-9.670216,-9.421886,-8.407057,0.284495,1.357110,-4.439276,-8.094034,9.525933,8.984380,-6.936718,-7.914828,5.913157,-2.358027,5.355708,-8.037665,8.134628,2.505509,-5.957002,0.226969,-7.793379,-7.848882,9.992012,-9.774966,-0.036813,-8.666607,-9.103437,4.393913,-5.443325,-1.888636,-0.886792,1.212623,0.544345,2.288354,-9.475006,3.241715,-1.310555,7.217331,7.087890,-0.898655,6.434147,-0.678038,-8.824650,6.870443,6.064185,-8.743290,-1.979193,5.159962,-4.737940,4.778508,1.365594,7.392109,9.164524,-4.381374,0.412905,-5.841950,8.910779,-1.437396,-7.867704,0.456665,8.944587,-9.511846,7.926382,-9.873289,-0.948169,-5.673281,-1.251240,7.834044,8.587913,-9.913127,1.413317,6.866037,-8.908167,-6.643137,-5.182739,-2.837682,1.211235,4.572745,8.889645,-8.786696,-4.528987,7.928163,-4.488536,-9.408061,-9.954668,-7.899847,1.366281,5.331461,5.678436,-4.915499,0.696479,-0.670820,8.000735,6.758377,9.222700,2.275289,-6.486751,-2.653283,9.720657,-8.663538,-1.717476,4.477023,7.054447,7.719949,-8.137584,-3.533987,-0.571205,-6.751513,-4.891618,-6.605480,8.733744,6.229332,1.305324,1.188313,-3.869048,-3.278679,-6.530222,-6.760191,-9.708017,2.377411,-7.301949,-2.374589,-9.175272,-3.253357,-1.895706,-7.907754,-3.062745,-4.607603,0.655744,3.171259,7.349990,-5.467910,8.189555,1.383116,-6.272770,9.147743,-0.976302,-6.552945,-6.151768,-5.623139,6.784323,6.565668,-0.319494,0.404536,9.032368,-7.989823,2.745613,-0.431760,0.822924,-9.245786,-6.123767,-7.453048,-2.790562,7.345908,-6.261702,0.965263,-1.892772,9.705269,-4.518005,7.051541,5.371696,0.291206,-2.559796,-3.293938,4.068859,-2.314531,-1.445580,9.524240,0.276024,4.170516,-5.272644,5.203862,6.411536,8.413124,-4.027235,8.238708,-8.110596,-2.473991,9.373700,9.330528,5.511485,-1.196099,-6.711917,-2.805659,5.486061,7.948215,5.118166,-7.631916,-8.869035,-9.271028,-6.305486,-5.498372,-3.449229,-9.036055,0.905512,6.395626,7.272131,-1.221235,1.238300,1.032174,5.632649,-1.980813,7.138427,8.883633,-9.915100,-6.552246,-5.082272,-6.864730,5.587116,-0.275596,-0.715693,-2.328248,3.212582,7.306513,5.259314,9.349422,-8.503503,3.190768,6.558851,4.700184,8.260250,-3.424681,-8.522632,-1.676076,7.898104,8.683652,-0.887397,0.046486,-4.458857,-1.358979,0.225571,-3.171333,9.769262,-2.276219,8.400287,5.771481,5.239624,-1.623374,-4.259725,-1.224217,1.406023,2.845986,4.180281,5.357273,1.312615,9.980503,-6.337058,-6.462738,-2.925668,-5.568518,-8.905096,-7.483128,2.887900,-1.278301,8.208818,-0.348041,-2.073510,7.757352,-5.118978,1.935563,-8.211421,4.231436,5.857743,7.103654,-9.408210,2.330418,5.019436,-6.153388,-3.404001,-1.899721,4.955482,-7.860051,-5.044976,2.132419,-0.432089,-6.405320,-8.965120,1.719191,-5.995244,7.919025,-3.574516,8.867977,-0.165623,2.009846,-0.249497,-1.652331,-7.740171,3.044918,-6.210700,3.536332,-3.135095,-7.161860,6.881836,-7.002851,-6.681038,-8.821828,-5.665915,-4.593727,-2.924351,7.288509,4.156713,-3.502816,-0.754898,-3.267687,1.538698,4.610809,4.574113,-7.496938,-4.730802,-7.262410,-0.487257,2.919395,6.390734,9.480327,9.771480,-9.174699,-9.758422,-1.482336,7.439295,-9.817575,1.153067,-4.470184,1.243066,3.324009,5.215818,-3.642841,7.220381,-8.137819,6.367104,-3.070355,-4.168563,8.434607,3.859862,5.030233,-2.538021,0.914220,8.569048,-8.098512,-0.649858,-2.883765,-2.595525,9.695541,2.404616,-9.181687,1.300805,8.267041,7.450290,6.251054,0.346846,4.397311,-9.606950,4.641889,-0.068727,-2.113875,2.677922,-8.713361,8.487134,1.548501,2.504810,2.483597,-8.869588,-0.850922,8.631392,1.248428,-9.786695,-8.444448,0.658019,8.037691,5.378272,5.065461,-8.137271,-4.844101,8.464506,-7.742431,7.340500,-4.925178,1.934753,-3.148928,-6.627199,8.152605,-5.626813,2.314018,1.604775,-7.589594,-3.233311,9.975076,3.392042,-7.095149,-5.904748,-6.951311,-7.067436,9.014624,6.163736,-6.895647,0.099083,9.588977,4.299435,-0.486959,4.445579,3.855685,-8.421324,-3.556381,7.156991,-6.572748,-8.133105,8.716917,5.545040,-6.921469,-3.929106,-8.530714,-4.198187,-0.031588,-1.702607,-9.184659,2.209245,2.157580,-3.858290,0.767390,-9.184150,4.782393,-8.095509,3.618557,-9.773911,9.301951,-8.213979,-3.559355,0.370626,-5.347733,8.568642,6.858525,0.374601,-4.113357,-3.018186,4.110013,-1.199641,9.592510,3.860672,-6.554152,-1.589418,7.616228,-7.401664,8.069343,-1.608129,8.425349,-0.445885,-5.721613,-7.598792,-7.671240,-7.386780,8.623060,-5.409435,-8.967924,-5.152966,7.803609,-8.001112,4.994079,4.007199,-4.852573,8.533297,1.794027,-9.693813,4.624355,3.905423,6.364912,7.899337,-9.543168,-0.553230,2.623976,6.301888,3.450174,1.119432,-8.872563,-9.943633,-4.040155,0.353067,9.796684,6.048590,-7.572607,-0.372034,9.581722,-3.704521,-5.998506,-8.262671,0.043783,-7.100588,2.338205,-7.589946,-6.822456,-6.226156,-2.410019,1.342992,6.983736,-5.349182,4.698332,9.243609,-4.543737,-4.531776,-5.462078,-0.731163,-0.105015,4.645758,5.479382,-8.260985,-7.392035,-1.854631,-6.874596,-3.986049,2.558862,5.554107,-6.211098,5.185305,-2.984637,0.262565,-0.817542,9.776580,-5.994360,-1.570014,-8.515206,-9.667572,6.621294,2.497817,-9.572371,1.677292,-8.437700,-0.991811,6.793800,5.652138,2.431865,7.016387,-2.919134,-2.100910,3.819805,-5.114768,2.886326,-0.757205,-2.879307,-1.169255,2.963485,-1.491816,-8.466573,-3.375732,-1.150897,-3.592646,-7.340319,6.994382,-9.537358,-3.840906,-7.927404,9.918532,2.954189,-1.029079,2.184590,-4.203406,-1.173466,-6.895039,9.513032,-4.148844,-6.692615,5.156885,-2.307640,2.836628,-6.499979,-7.776235,4.252004,1.489158,2.627935,-0.020254,-1.491816,-2.550285,7.330426,-7.866555,7.027255,-0.122672,5.668050,1.353030,-4.410432,-4.621583,-4.185963,0.056681,-9.780032,-5.122435,-3.706726,-2.889396,4.008558,3.482433,3.704837,6.835391,-3.301043,-7.799108,8.156258,-6.083514,-2.798463,-1.752785,1.148896,-6.242419,-7.331472,-2.659852,0.726140,-3.875674,7.628615,7.233936,0.322652,1.554056,-3.414247,8.203867,4.985621,5.947550,-1.382814,-5.479680,1.012917,9.660607,7.493679,-6.222273,-7.933283,9.686647,-4.233691,-4.005922,6.661312,-2.227953,1.815530,1.523390,4.741485,-1.148982,5.885457,9.785201,-1.841487,-1.777577,-7.933762,-7.152713,6.375666,-4.687657,3.736661,5.638089], dtype = "float32")#candidate|2156|(1800,)|const|float32
const_2157 = relay.const([[7],[6],[-9],[3],[-1],[-8],[6],[10],[-5],[-7],[-5],[-9],[9],[6],[-9],[2],[6],[-9],[-1],[4],[-9],[-9],[-4],[8],[-1],[6],[-8],[-5],[-6],[-2],[3],[-3],[10],[-2],[8],[-2],[-2],[-10],[4],[-6],[5],[-3],[8],[-9],[-10],[1],[5],[-2],[10],[7],[-2],[3],[-2],[2],[2],[-2],[-3],[3],[2],[-6],[-3],[8],[3],[-2],[-6],[10],[-7],[-3],[7],[6],[-5],[-8],[5],[10],[3],[4],[4],[-3],[-1],[-1],[5],[-4],[4],[3],[5],[1],[-2],[-8],[10],[6],[3],[1],[-9],[-6],[3],[-7],[9],[-1],[1],[4],[-5],[-5],[4],[4],[1],[-1],[-10],[-4],[9],[9],[-7],[10],[-10],[-9],[-9],[6],[-6],[3],[-4],[7],[-6],[2],[1],[5],[5],[-3],[4],[6],[-8],[-4],[8],[1],[3],[-5],[10],[4],[10],[-4],[-1],[-2],[6],[-7],[-3],[-2],[-10],[6],[-8],[-3],[2],[10],[9],[9],[-2],[-2],[-3],[9],[2],[-8],[3],[-5],[-10],[-2],[-9],[-1],[-2],[-2],[5],[-2],[-4],[9],[-1],[-5],[-6],[-9],[4],[-1],[-7],[3],[7],[-7],[-5],[10],[8],[-8],[-8],[-8],[-7],[3],[7],[-2],[8],[-5],[4],[10],[-2],[-10],[4],[8],[4],[6],[4],[3],[8],[-5],[-10],[4],[-10],[-10],[7],[-8],[7],[-5],[-10],[4],[-2],[5],[4],[-9],[4],[5],[-3],[-9],[-10],[-7],[-10],[-7],[3],[-9],[6],[6],[-4],[3],[-9],[-10],[6],[-4],[-8],[2],[-5],[-6],[-4],[-4],[-4],[1],[-8],[7],[-9],[2],[3],[-10],[9],[10],[8],[-7],[10],[10],[4],[-2],[-6],[-10],[3],[-8],[8],[-10],[-2],[-1],[-6],[-10],[10],[-7],[-1],[-6],[-10],[-5],[5],[-3],[-1],[-1],[-9],[-1],[3],[1],[3],[-4],[-9],[5],[10],[4],[10],[-8],[-3],[3],[2],[-4]], dtype = "uint32")#candidate|2157|(294, 1)|const|uint32
call_2155 = relay.TupleGetItem(func_1559_call(relay.reshape(const_2156.astype('float32'), [15, 10, 12]), relay.reshape(const_2157.astype('uint32'), [294,]), ), 1)
call_2158 = relay.TupleGetItem(func_1563_call(relay.reshape(const_2156.astype('float32'), [15, 10, 12]), relay.reshape(const_2157.astype('uint32'), [294,]), ), 1)
output = relay.Tuple([uop_2139,call_2155,const_2156,const_2157,])
output2 = relay.Tuple([uop_2139,call_2158,const_2156,const_2157,])
func_2165 = relay.Function([var_2127,], output)
mod['func_2165'] = func_2165
mod = relay.transform.InferType()(mod)
mutated_mod['func_2165'] = func_2165
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2166 = relay.var("var_2166", dtype = "uint16", shape = (16, 3, 14))#candidate|2166|(16, 3, 14)|var|uint16
func_2165_call = mutated_mod.get_global_var('func_2165')
call_2167 = func_2165_call(var_2166)
output = call_2167
func_2168 = relay.Function([var_2166], output)
mutated_mod['func_2168'] = func_2168
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1197_call = mod.get_global_var('func_1197')
func_1198_call = mutated_mod.get_global_var('func_1198')
call_2259 = relay.TupleGetItem(func_1197_call(), 1)
call_2260 = relay.TupleGetItem(func_1198_call(), 1)
func_1662_call = mod.get_global_var('func_1662')
func_1666_call = mutated_mod.get_global_var('func_1666')
const_2276 = relay.const([[8,1,10,-10,3,-9,-7,5,-10,5],[4,-2,-1,3,-2,3,-6,4,8,-10],[3,6,-2,7,3,-6,8,-7,2,2],[8,5,-2,1,-6,-1,-2,8,-7,6],[7,-6,-7,-3,-2,4,-10,7,10,2],[-10,-5,-7,4,8,-3,-1,1,3,-8],[10,-8,-1,-4,4,6,-6,-6,-2,8],[-2,6,-3,3,10,2,3,10,-6,4],[-10,-6,1,-3,4,-4,4,10,-8,5],[6,8,9,3,4,-7,-10,-3,5,-6],[7,5,-2,1,10,8,3,-5,-7,10],[-8,8,-10,-10,4,5,-8,5,7,-9],[-1,-5,4,9,-8,3,-7,-7,1,-3],[-5,-8,-9,10,8,5,6,-6,-7,4],[-5,5,-9,1,2,-4,-2,-10,5,9],[9,5,-1,8,7,7,-8,-7,7,-6],[4,5,-2,9,5,3,9,1,-10,-9],[-10,2,-1,6,7,-4,-10,8,-2,-1],[4,-10,3,-4,2,-3,-2,-2,-4,-8],[8,1,-10,2,-6,8,-9,5,-2,7],[4,8,-5,-8,9,-9,9,7,-10,1],[3,8,-10,6,-5,7,4,-7,6,-9],[3,-1,7,10,-8,5,-2,5,-7,-5],[-7,2,-8,2,6,6,-9,-10,7,-6],[-2,-6,4,-6,2,3,-4,1,-6,5],[-4,1,-9,2,2,-9,-6,1,-6,-3],[8,10,-3,-3,5,10,6,5,-4,-1],[4,3,5,-2,-10,-9,-10,-10,9,-1],[9,6,-5,-3,7,-7,6,-10,3,1],[-6,-4,1,-9,-7,-7,-4,-4,-1,9],[-4,8,6,10,10,5,-4,-2,2,5],[2,8,4,-6,-2,4,1,4,10,7],[5,-3,10,4,-7,-3,-3,-6,4,4],[8,2,8,7,9,-7,5,-5,-5,8],[8,-2,4,-9,-3,6,9,-3,3,-6],[-5,1,2,8,3,-1,7,5,3,-2]], dtype = "int64")#candidate|2276|(36, 10)|const|int64
const_2277 = relay.const([10,-6,-2,4,-5,10,10,10,-1,-3,-7,6,-4,3,5,-3,-1,-7,-2,-10,9,-3,-4,-6,7,7,-2,5,2,-9,8,-2,-3,-4,8,-3,6,8,8,-4,5,-10,-4,10,-7,-1,-3,5,-1,-2,-3,-8,1,-10,1,-6,5,1,5,5,2,-6,-10,2,10,-10,9,3,-5,-10,8,1,4,-5,5,10,6,4,-8,7,10,-2,-9,-8,-7,1,4,1,5,-6,5,-2,5,9,10,-3,7,-9,2,1,8,7,3,2,5,2,6,-3,8,6,7,-8,7,-1,7,-10,-1,8,4,-5,8,9,1,-4,-3,7,-2,-6,-4,-9,8,-5,6,-4,3,-1,7,4,-1,7,1,-4,10,-3,7,-5,-1,4,6,-10,-7,10,1,4,-2,-6,6,7,1,2,4,-3,-10,4,4,8,7,7,-2,9,-3,-1,4,5,-8,3,4,8,-2,-3,10,-8,-9,-4,8,-9,8,-8,-5,-10,-1,8,-1,-1,-1,-7,-4,-8,4,4,-5,2,2,-8,4,4,2,-1,8,-4,-6,10,8,3,-7,-3,-1,-6,5,-1,-1,-6,-5,-6,1,-2,2,7,7,3,10,-6,3,5,5,8,-9,1,-1,6,6,9,7,10,-7,-8,1,7,6,-1,-7,9,3,-9,6,6,-1,-9,-10,-2], dtype = "uint8")#candidate|2277|(260,)|const|uint8
call_2275 = relay.TupleGetItem(func_1662_call(relay.reshape(const_2276.astype('int64'), [360,]), relay.reshape(const_2277.astype('uint8'), [260,]), ), 0)
call_2278 = relay.TupleGetItem(func_1666_call(relay.reshape(const_2276.astype('int64'), [360,]), relay.reshape(const_2277.astype('uint8'), [260,]), ), 0)
uop_2279 = relay.asinh(const_2276.astype('float64')) # shape=(36, 10)
output = relay.Tuple([call_2259,call_2275,const_2277,uop_2279,])
output2 = relay.Tuple([call_2260,call_2278,const_2277,uop_2279,])
func_2288 = relay.Function([], output)
mod['func_2288'] = func_2288
mod = relay.transform.InferType()(mod)
mutated_mod['func_2288'] = func_2288
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2288_call = mutated_mod.get_global_var('func_2288')
call_2289 = func_2288_call()
output = call_2289
func_2290 = relay.Function([], output)
mutated_mod['func_2290'] = func_2290
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1363_call = mod.get_global_var('func_1363')
func_1365_call = mutated_mod.get_global_var('func_1365')
call_2339 = func_1363_call()
call_2340 = func_1363_call()
uop_2345 = relay.log2(call_2339.astype('float64')) # shape=(6, 1, 6)
uop_2347 = relay.log2(call_2340.astype('float64')) # shape=(6, 1, 6)
uop_2351 = relay.sinh(call_2339.astype('float64')) # shape=(6, 1, 6)
uop_2353 = relay.sinh(call_2340.astype('float64')) # shape=(6, 1, 6)
output = relay.Tuple([uop_2345,uop_2351,])
output2 = relay.Tuple([uop_2347,uop_2353,])
func_2356 = relay.Function([], output)
mod['func_2356'] = func_2356
mod = relay.transform.InferType()(mod)
output = func_2356()
func_2357 = relay.Function([], output)
mutated_mod['func_2357'] = func_2357
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1197_call = mod.get_global_var('func_1197')
func_1198_call = mutated_mod.get_global_var('func_1198')
call_2407 = relay.TupleGetItem(func_1197_call(), 0)
call_2408 = relay.TupleGetItem(func_1198_call(), 0)
output = call_2407
output2 = call_2408
func_2423 = relay.Function([], output)
mod['func_2423'] = func_2423
mod = relay.transform.InferType()(mod)
mutated_mod['func_2423'] = func_2423
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2423_call = mutated_mod.get_global_var('func_2423')
call_2424 = func_2423_call()
output = call_2424
func_2425 = relay.Function([], output)
mutated_mod['func_2425'] = func_2425
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2472 = relay.var("var_2472", dtype = "float64", shape = ())#candidate|2472|()|var|float64
var_2473 = relay.var("var_2473", dtype = "float64", shape = (6, 9, 15))#candidate|2473|(6, 9, 15)|var|float64
bop_2474 = relay.minimum(var_2472.astype('float64'), var_2473.astype('float64')) # shape=(6, 9, 15)
output = relay.Tuple([bop_2474,])
output2 = relay.Tuple([bop_2474,])
func_2481 = relay.Function([var_2472,var_2473,], output)
mod['func_2481'] = func_2481
mod = relay.transform.InferType()(mod)
mutated_mod['func_2481'] = func_2481
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2481_call = mutated_mod.get_global_var('func_2481')
var_2483 = relay.var("var_2483", dtype = "float64", shape = ())#candidate|2483|()|var|float64
var_2484 = relay.var("var_2484", dtype = "float64", shape = (6, 9, 15))#candidate|2484|(6, 9, 15)|var|float64
call_2482 = func_2481_call(var_2483,var_2484,)
output = call_2482
func_2485 = relay.Function([var_2483,var_2484,], output)
mutated_mod['func_2485'] = func_2485
mutated_mod = relay.transform.InferType()(mutated_mod)
func_685_call = mod.get_global_var('func_685')
func_687_call = mutated_mod.get_global_var('func_687')
call_2573 = relay.TupleGetItem(func_685_call(), 1)
call_2574 = relay.TupleGetItem(func_687_call(), 1)
output = call_2573
output2 = call_2574
func_2594 = relay.Function([], output)
mod['func_2594'] = func_2594
mod = relay.transform.InferType()(mod)
output = func_2594()
func_2595 = relay.Function([], output)
mutated_mod['func_2595'] = func_2595
mutated_mod = relay.transform.InferType()(mutated_mod)
func_707_call = mod.get_global_var('func_707')
func_708_call = mutated_mod.get_global_var('func_708')
call_2623 = relay.TupleGetItem(func_707_call(), 0)
call_2624 = relay.TupleGetItem(func_708_call(), 0)
output = relay.Tuple([call_2623,])
output2 = relay.Tuple([call_2624,])
func_2629 = relay.Function([], output)
mod['func_2629'] = func_2629
mod = relay.transform.InferType()(mod)
mutated_mod['func_2629'] = func_2629
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2629_call = mutated_mod.get_global_var('func_2629')
call_2630 = func_2629_call()
output = call_2630
func_2631 = relay.Function([], output)
mutated_mod['func_2631'] = func_2631
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2639 = relay.const(-6, dtype = "uint32")#candidate|2639|()|const|uint32
var_2640 = relay.var("var_2640", dtype = "uint32", shape = (4, 2, 1))#candidate|2640|(4, 2, 1)|var|uint32
bop_2641 = relay.greater_equal(const_2639.astype('bool'), var_2640.astype('bool')) # shape=(4, 2, 1)
bop_2650 = relay.equal(var_2640.astype('bool'), relay.reshape(bop_2641.astype('bool'), relay.shape_of(var_2640))) # shape=(4, 2, 1)
output = relay.Tuple([bop_2650,])
output2 = relay.Tuple([bop_2650,])
func_2656 = relay.Function([var_2640,], output)
mod['func_2656'] = func_2656
mod = relay.transform.InferType()(mod)
mutated_mod['func_2656'] = func_2656
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2657 = relay.var("var_2657", dtype = "uint32", shape = (4, 2, 1))#candidate|2657|(4, 2, 1)|var|uint32
func_2656_call = mutated_mod.get_global_var('func_2656')
call_2658 = func_2656_call(var_2657)
output = call_2658
func_2659 = relay.Function([var_2657], output)
mutated_mod['func_2659'] = func_2659
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2674 = relay.var("var_2674", dtype = "float32", shape = (4, 1, 15))#candidate|2674|(4, 1, 15)|var|float32
uop_2675 = relay.log10(var_2674.astype('float32')) # shape=(4, 1, 15)
output = relay.Tuple([uop_2675,])
output2 = relay.Tuple([uop_2675,])
func_2689 = relay.Function([var_2674,], output)
mod['func_2689'] = func_2689
mod = relay.transform.InferType()(mod)
var_2690 = relay.var("var_2690", dtype = "float32", shape = (4, 1, 15))#candidate|2690|(4, 1, 15)|var|float32
output = func_2689(var_2690)
func_2691 = relay.Function([var_2690], output)
mutated_mod['func_2691'] = func_2691
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1197_call = mod.get_global_var('func_1197')
func_1198_call = mutated_mod.get_global_var('func_1198')
call_2693 = relay.TupleGetItem(func_1197_call(), 1)
call_2694 = relay.TupleGetItem(func_1198_call(), 1)
uop_2719 = relay.cosh(call_2693.astype('float32')) # shape=(6, 1, 6)
uop_2721 = relay.cosh(call_2694.astype('float32')) # shape=(6, 1, 6)
output = uop_2719
output2 = uop_2721
func_2722 = relay.Function([], output)
mod['func_2722'] = func_2722
mod = relay.transform.InferType()(mod)
output = func_2722()
func_2723 = relay.Function([], output)
mutated_mod['func_2723'] = func_2723
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2594_call = mod.get_global_var('func_2594')
func_2595_call = mutated_mod.get_global_var('func_2595')
call_2745 = func_2594_call()
call_2746 = func_2594_call()
output = relay.Tuple([call_2745,])
output2 = relay.Tuple([call_2746,])
func_2751 = relay.Function([], output)
mod['func_2751'] = func_2751
mod = relay.transform.InferType()(mod)
output = func_2751()
func_2752 = relay.Function([], output)
mutated_mod['func_2752'] = func_2752
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1947_call = mod.get_global_var('func_1947')
func_1948_call = mutated_mod.get_global_var('func_1948')
call_2772 = relay.TupleGetItem(func_1947_call(), 2)
call_2773 = relay.TupleGetItem(func_1948_call(), 2)
var_2777 = relay.var("var_2777", dtype = "float32", shape = (6, 4, 6))#candidate|2777|(6, 4, 6)|var|float32
bop_2778 = relay.less(call_2772.astype('bool'), var_2777.astype('bool')) # shape=(6, 4, 6)
bop_2781 = relay.less(call_2773.astype('bool'), var_2777.astype('bool')) # shape=(6, 4, 6)
func_1584_call = mod.get_global_var('func_1584')
func_1586_call = mutated_mod.get_global_var('func_1586')
call_2784 = relay.TupleGetItem(func_1584_call(), 0)
call_2785 = relay.TupleGetItem(func_1586_call(), 0)
output = relay.Tuple([bop_2778,call_2784,])
output2 = relay.Tuple([bop_2781,call_2785,])
func_2791 = relay.Function([var_2777,], output)
mod['func_2791'] = func_2791
mod = relay.transform.InferType()(mod)
mutated_mod['func_2791'] = func_2791
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2792 = relay.var("var_2792", dtype = "float32", shape = (6, 4, 6))#candidate|2792|(6, 4, 6)|var|float32
func_2791_call = mutated_mod.get_global_var('func_2791')
call_2793 = func_2791_call(var_2792)
output = call_2793
func_2794 = relay.Function([var_2792], output)
mutated_mod['func_2794'] = func_2794
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1889_call = mod.get_global_var('func_1889')
func_1890_call = mutated_mod.get_global_var('func_1890')
call_2824 = relay.TupleGetItem(func_1889_call(), 0)
call_2825 = relay.TupleGetItem(func_1890_call(), 0)
output = call_2824
output2 = call_2825
func_2832 = relay.Function([], output)
mod['func_2832'] = func_2832
mod = relay.transform.InferType()(mod)
output = func_2832()
func_2833 = relay.Function([], output)
mutated_mod['func_2833'] = func_2833
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1633_call = mod.get_global_var('func_1633')
func_1634_call = mutated_mod.get_global_var('func_1634')
call_2856 = relay.TupleGetItem(func_1633_call(), 0)
call_2857 = relay.TupleGetItem(func_1634_call(), 0)
func_980_call = mod.get_global_var('func_980')
func_982_call = mutated_mod.get_global_var('func_982')
var_2864 = relay.var("var_2864", dtype = "float64", shape = (15,))#candidate|2864|(15,)|var|float64
call_2863 = relay.TupleGetItem(func_980_call(relay.reshape(var_2864.astype('float64'), [3, 1, 5])), 0)
call_2865 = relay.TupleGetItem(func_982_call(relay.reshape(var_2864.astype('float64'), [3, 1, 5])), 0)
func_747_call = mod.get_global_var('func_747')
func_748_call = mutated_mod.get_global_var('func_748')
call_2870 = relay.TupleGetItem(func_747_call(), 0)
call_2871 = relay.TupleGetItem(func_748_call(), 0)
output = relay.Tuple([call_2856,call_2863,var_2864,call_2870,])
output2 = relay.Tuple([call_2857,call_2865,var_2864,call_2871,])
func_2876 = relay.Function([var_2864,], output)
mod['func_2876'] = func_2876
mod = relay.transform.InferType()(mod)
var_2877 = relay.var("var_2877", dtype = "float64", shape = (15,))#candidate|2877|(15,)|var|float64
output = func_2876(var_2877)
func_2878 = relay.Function([var_2877], output)
mutated_mod['func_2878'] = func_2878
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2880 = relay.var("var_2880", dtype = "float32", shape = (9, 2, 2))#candidate|2880|(9, 2, 2)|var|float32
uop_2881 = relay.exp(var_2880.astype('float32')) # shape=(9, 2, 2)
output = relay.Tuple([uop_2881,])
output2 = relay.Tuple([uop_2881,])
func_2890 = relay.Function([var_2880,], output)
mod['func_2890'] = func_2890
mod = relay.transform.InferType()(mod)
mutated_mod['func_2890'] = func_2890
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2891 = relay.var("var_2891", dtype = "float32", shape = (9, 2, 2))#candidate|2891|(9, 2, 2)|var|float32
func_2890_call = mutated_mod.get_global_var('func_2890')
call_2892 = func_2890_call(var_2891)
output = call_2892
func_2893 = relay.Function([var_2891], output)
mutated_mod['func_2893'] = func_2893
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1889_call = mod.get_global_var('func_1889')
func_1890_call = mutated_mod.get_global_var('func_1890')
call_2960 = relay.TupleGetItem(func_1889_call(), 0)
call_2961 = relay.TupleGetItem(func_1890_call(), 0)
func_2594_call = mod.get_global_var('func_2594')
func_2595_call = mutated_mod.get_global_var('func_2595')
call_2969 = func_2594_call()
call_2970 = func_2594_call()
bop_2987 = relay.right_shift(call_2969.astype('int16'), relay.reshape(call_2960.astype('int16'), relay.shape_of(call_2969))) # shape=(6, 1, 6)
bop_2990 = relay.right_shift(call_2970.astype('int16'), relay.reshape(call_2961.astype('int16'), relay.shape_of(call_2970))) # shape=(6, 1, 6)
output = relay.Tuple([bop_2987,])
output2 = relay.Tuple([bop_2990,])
func_2994 = relay.Function([], output)
mod['func_2994'] = func_2994
mod = relay.transform.InferType()(mod)
mutated_mod['func_2994'] = func_2994
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2994_call = mutated_mod.get_global_var('func_2994')
call_2995 = func_2994_call()
output = call_2995
func_2996 = relay.Function([], output)
mutated_mod['func_2996'] = func_2996
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1745_call = mod.get_global_var('func_1745')
func_1746_call = mutated_mod.get_global_var('func_1746')
call_3027 = func_1745_call()
call_3028 = func_1745_call()
func_2288_call = mod.get_global_var('func_2288')
func_2290_call = mutated_mod.get_global_var('func_2290')
call_3030 = relay.TupleGetItem(func_2288_call(), 3)
call_3031 = relay.TupleGetItem(func_2290_call(), 3)
var_3037 = relay.var("var_3037", dtype = "float64", shape = (36, 10))#candidate|3037|(36, 10)|var|float64
bop_3038 = relay.equal(call_3030.astype('bool'), relay.reshape(var_3037.astype('bool'), relay.shape_of(call_3030))) # shape=(36, 10)
bop_3041 = relay.equal(call_3031.astype('bool'), relay.reshape(var_3037.astype('bool'), relay.shape_of(call_3031))) # shape=(36, 10)
func_326_call = mod.get_global_var('func_326')
func_328_call = mutated_mod.get_global_var('func_328')
var_3049 = relay.var("var_3049", dtype = "uint8", shape = (260,))#candidate|3049|(260,)|var|uint8
call_3048 = relay.TupleGetItem(func_326_call(relay.reshape(var_3049.astype('uint8'), [4, 5, 13])), 1)
call_3050 = relay.TupleGetItem(func_328_call(relay.reshape(var_3049.astype('uint8'), [4, 5, 13])), 1)
output = relay.Tuple([call_3027,bop_3038,call_3048,var_3049,])
output2 = relay.Tuple([call_3028,bop_3041,call_3050,var_3049,])
func_3053 = relay.Function([var_3037,var_3049,], output)
mod['func_3053'] = func_3053
mod = relay.transform.InferType()(mod)
var_3054 = relay.var("var_3054", dtype = "float64", shape = (36, 10))#candidate|3054|(36, 10)|var|float64
var_3055 = relay.var("var_3055", dtype = "uint8", shape = (260,))#candidate|3055|(260,)|var|uint8
output = func_3053(var_3054,var_3055,)
func_3056 = relay.Function([var_3054,var_3055,], output)
mutated_mod['func_3056'] = func_3056
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1745_call = mod.get_global_var('func_1745')
func_1746_call = mutated_mod.get_global_var('func_1746')
call_3067 = func_1745_call()
call_3068 = func_1745_call()
const_3069 = relay.const([[[False,True,True,True,False,True],[False,False,False,False,True,False]],[[True,False,False,False,False,True],[True,True,False,True,False,True]],[[True,True,False,True,True,True],[True,True,False,True,True,False]],[[False,True,False,False,True,False],[False,False,False,False,False,True]],[[True,True,False,True,False,True],[False,True,False,False,False,True]],[[True,False,True,True,True,False],[True,True,True,False,True,False]]], dtype = "bool")#candidate|3069|(6, 2, 6)|const|bool
bop_3070 = relay.logical_xor(call_3067.astype('int32'), const_3069.astype('int32')) # shape=(6, 2, 6)
bop_3073 = relay.logical_xor(call_3068.astype('int32'), const_3069.astype('int32')) # shape=(6, 2, 6)
uop_3074 = relay.atan(const_3069.astype('float64')) # shape=(6, 2, 6)
output = relay.Tuple([bop_3070,uop_3074,])
output2 = relay.Tuple([bop_3073,uop_3074,])
func_3079 = relay.Function([], output)
mod['func_3079'] = func_3079
mod = relay.transform.InferType()(mod)
output = func_3079()
func_3080 = relay.Function([], output)
mutated_mod['func_3080'] = func_3080
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3084 = relay.const([[[-0.606935,8.104513,-0.065585,-7.463889,5.045119,-9.605915,0.743343,1.232482,9.264760,-7.649358,8.083163,-0.908280],[0.194837,1.777860,1.217916,-8.191316,6.821940,-7.218826,6.870963,-4.093396,2.695795,-7.626164,9.120637,-1.600459],[2.385389,4.550476,5.490113,-0.961912,9.762732,-8.928761,-3.853830,-6.375018,-1.805353,6.614674,1.626861,-4.603098],[-3.779947,-5.118810,8.052497,-4.452889,7.054527,3.685673,1.588115,-9.553544,1.152356,5.749829,2.253222,3.668222],[0.238372,7.344887,4.350098,6.856708,-4.404984,3.187230,-5.022021,5.639571,-2.875224,-6.185102,-6.481557,-4.682877],[-1.082341,9.574067,0.444677,6.448391,6.876337,3.715043,5.699627,-6.720377,-7.159387,3.423180,7.950101,3.754015],[5.179916,3.915587,-7.699706,8.071213,7.684395,-8.260758,1.572667,1.898432,-2.334672,2.245961,3.425787,8.854041],[-7.753956,-4.147279,4.725848,8.415635,-4.840196,-0.782002,-2.292972,3.549295,-2.651514,-5.713787,9.555571,-5.371405],[-0.461886,3.572870,2.019303,-1.055171,3.184649,7.555082,-1.179137,7.734491,2.265095,7.164461,7.639674,-9.707428],[-0.376306,-3.011428,-7.342899,5.614819,-0.109054,2.600775,8.750033,5.134194,-3.172591,-9.130657,9.459483,7.130620]],[[3.579579,-9.223664,1.871686,2.412377,6.288530,-7.683287,-5.396664,6.727675,-5.820674,8.349371,-6.471339,1.571154],[3.913506,6.835930,9.801663,-7.637923,9.303646,-4.261847,6.854591,-2.814028,2.975662,-5.521040,-0.177340,-4.097961],[-6.853458,-8.102173,0.288086,-1.772030,3.745875,7.795175,-7.296762,-7.314006,7.465239,0.466982,-8.016542,5.220890],[-7.978673,1.906269,6.200823,9.268239,3.435345,-3.341000,9.562008,-3.127969,-2.182363,-5.147564,0.156741,-5.711290],[5.135530,7.545442,2.585131,8.861968,-0.021180,-2.627480,-0.106342,-9.495529,-3.921409,-4.220489,7.420143,-3.439078],[3.612214,-6.846287,4.259228,7.998817,-9.755742,-8.657931,4.739404,4.033275,9.103210,-0.303539,-7.161582,8.720774],[1.770286,-5.113357,-4.327198,0.438834,9.990668,-0.396464,-4.932441,0.398624,-0.244182,6.005167,1.149927,-1.438319],[-3.526670,1.259170,8.151879,4.275293,-5.519816,8.447919,0.332694,-0.555433,-6.843631,9.633093,-0.951855,-6.849364],[2.041558,7.371500,-0.521631,4.887244,-2.256253,6.566951,3.472019,-9.603315,8.500374,0.884111,-1.391050,2.768914],[-4.613558,-8.747545,-9.941193,-3.367532,-2.511531,-5.743553,8.819480,1.527740,-4.885587,9.400875,-6.388950,-6.524499]],[[2.281944,-9.046051,6.890983,-0.598309,-1.541356,3.022737,0.035850,-4.549915,6.230518,1.341014,-2.406735,-6.548410],[2.655792,5.745867,2.418742,0.177516,7.468854,8.642824,-8.279008,-5.054515,-4.911820,6.921912,7.382615,8.861982],[-4.140339,9.572953,3.048738,-3.103191,0.802341,-6.890423,7.598663,7.525250,1.968458,8.718382,5.252903,8.039381],[1.133064,2.325026,-6.517216,8.042549,3.212459,-6.339618,-2.629414,-2.801934,-9.118453,8.039413,-4.785136,-8.782478],[2.410324,2.010877,7.288595,-0.768923,6.613104,-8.480068,-7.410124,5.151098,-9.230382,-6.998924,-3.077569,5.553918],[-6.651178,-7.056396,7.567797,-8.180300,-4.852377,1.544211,-6.351272,5.052008,-8.191421,-1.279111,3.996275,-0.959784],[1.773101,3.421581,3.818609,-2.556904,4.841322,2.167816,8.522532,1.142421,5.045144,0.866052,-3.341844,-8.260719],[-3.024303,2.149997,-9.603543,-1.052168,-3.261518,8.442355,-1.043951,2.080159,-1.574940,-4.839820,5.701290,9.875621],[7.688927,-5.045289,8.899577,-7.644904,4.657524,-1.839334,4.490878,6.414002,-3.535740,-7.284727,-5.483231,-5.154731],[-1.189108,-9.803962,-2.272143,-7.991335,6.912965,4.068500,9.272930,-6.162571,6.897713,-9.827340,3.906092,-1.509550]],[[-1.412168,-8.804550,3.970582,2.774618,-7.167558,8.275665,-6.821003,-1.298360,-9.910373,-4.645462,9.473515,4.578838],[1.617343,6.505787,3.123771,-9.099246,-0.016152,5.682717,9.894197,6.247484,-2.131904,-8.589719,6.267069,-9.103770],[-0.660585,9.518680,-8.156960,-5.777676,8.495938,-2.984284,-5.743227,-7.469675,-5.406256,-1.441887,3.853002,7.761725],[-4.533933,-3.070872,-9.076449,1.316948,7.813368,-1.524821,4.036744,-3.930711,-0.485246,-4.337431,9.428279,-9.958926],[-6.689662,-5.279607,-9.683698,0.599962,4.133556,-4.242357,8.581517,0.941070,6.654076,-6.528318,-4.421640,3.472164],[4.336619,7.661521,-0.218249,-5.383866,-3.705665,-4.062794,-9.399697,4.474075,9.854898,7.380131,-0.079052,-3.872871],[-5.919309,-9.743636,1.329724,-2.689884,5.623704,6.519656,2.102021,-7.851536,-1.911106,-1.567305,6.283230,7.502346],[-0.455180,0.499599,4.628137,-2.950706,-2.229412,-2.616994,-0.388560,-2.134854,9.544678,7.447742,-6.343634,-2.442997],[5.504094,9.705011,0.908562,7.532703,-8.400376,-1.542082,-8.336841,8.009817,8.371437,-7.073950,-9.428715,-2.357866],[8.741968,-0.469399,6.764919,-6.063662,-2.416690,5.842632,-6.936498,5.712624,9.877427,-9.599060,-2.507620,-4.289962]],[[-0.696129,0.442674,-1.024532,-4.638789,2.046378,2.436508,8.028063,6.855867,1.158562,2.981806,-2.373477,-0.449686],[-9.051315,4.611621,4.704168,4.696364,1.917492,-2.699921,-1.417677,1.571483,-6.230395,-3.582458,-2.396652,5.457978],[4.565343,-4.968824,6.407066,5.236699,3.247101,-1.148792,2.420053,-6.872727,-2.293814,-3.885451,4.693974,-0.492742],[-1.602105,-4.211923,6.578988,-9.539916,-3.410725,-1.410860,-3.169373,-4.276218,-7.183425,-9.873069,-9.985579,-6.819880],[4.982058,0.320468,-6.594058,-5.392808,-1.015026,-6.054367,-0.929829,-7.884580,1.955502,-1.214447,4.676532,3.278950],[6.819633,1.588677,5.405761,-9.437208,-7.555915,2.298040,-8.765854,9.927061,-0.311436,-8.122382,-9.142123,-1.292423],[7.210565,2.984785,8.046225,-2.106711,-5.400843,-5.674214,-1.822359,2.371523,-1.246320,6.732070,-8.950079,8.044908],[-3.610912,-7.352595,8.908315,-8.430563,3.286470,8.778677,7.253447,-8.399880,3.369285,9.657951,4.246077,-7.468325],[2.790992,-6.356854,-2.043403,6.508550,7.488245,9.110810,-3.715034,6.180465,-9.573635,-4.863073,5.290691,4.381499],[9.325815,-1.711169,0.857328,-8.512009,-0.987352,5.303496,-6.474156,-9.926599,-0.575526,-6.653213,1.071741,-3.245950]],[[-4.073743,7.505611,3.113789,-2.348717,9.133249,-3.079696,0.174993,-6.069880,7.249025,-8.078921,-0.766079,-1.753612],[4.446518,5.112064,-0.555039,-8.248093,-4.527505,-3.365007,-5.926394,-2.609440,8.430357,1.155088,6.431214,2.847825],[3.916890,-8.141551,-9.906983,-7.078670,-4.400380,-7.623318,2.006799,2.309686,2.349544,-0.437241,7.207644,0.159653],[7.022621,3.292754,-0.150328,2.550945,0.119827,5.303387,-1.759707,4.346578,7.912354,-7.315359,-2.438849,-4.592936],[5.396008,0.459827,7.289015,-5.286792,0.315998,5.101352,-4.885763,9.715378,3.372666,2.385151,-3.113649,-4.778178],[-5.582443,4.947859,-5.539631,-5.496970,-2.978802,-4.544263,5.265920,-8.160855,5.397471,-4.742554,-8.953870,0.876610],[7.685867,-5.744619,9.780942,8.653376,7.912951,-2.249142,2.796198,2.613636,-9.340990,1.019497,-3.031574,4.709127],[-7.810644,7.104685,1.127187,-9.469623,4.177766,2.802417,3.449657,9.963230,6.582594,-0.405783,-9.184988,-1.978213],[-2.793723,-3.556047,7.075598,-9.801623,-3.237573,-0.899015,-2.174518,-1.966936,7.770304,-4.644928,-6.124523,3.079837],[3.680599,-2.757445,-4.738387,-8.062542,7.871643,3.135934,-2.878253,-8.997206,-4.511140,7.286748,0.373213,-3.974991]],[[0.093430,8.715084,-7.564432,6.801816,-5.028344,-8.671142,-3.654331,1.522776,9.499461,-7.428053,-5.313829,-0.099397],[7.434623,6.438909,5.694861,-0.818826,-7.332835,6.082120,-8.450813,-3.934998,-0.815594,0.558943,-8.708504,-4.220717],[-5.978206,7.590740,2.675046,6.415574,5.491572,9.548140,-3.776290,4.931759,9.000190,-4.506317,9.599139,3.536989],[2.148361,-6.802286,7.489459,7.046381,8.072845,1.293385,2.550878,-8.454926,7.600791,6.174951,5.389198,3.488585],[3.121196,-1.845350,-0.085751,0.087058,1.219934,4.099103,-3.800729,-2.283925,-8.404890,0.192319,-1.568537,-7.525083],[4.936627,8.320754,6.053959,-2.674011,-2.267138,0.786601,-9.791700,-8.454777,5.922082,-6.585958,2.373094,3.277394],[-5.950878,6.663890,-9.907859,0.357768,5.054511,-0.406496,5.593991,-3.152716,-1.277784,-6.661194,-3.744952,-4.446262],[2.896842,1.533296,1.341826,-8.543875,1.483776,-3.314739,6.447738,-0.503183,-2.282995,0.202934,6.762375,-8.489250],[-4.620829,-1.654881,9.554631,-0.432893,9.653974,2.520682,-7.835217,7.109958,5.236802,-2.078812,5.850107,-7.011762],[0.308660,2.583239,0.956533,-3.618330,-1.526829,-2.875618,7.579747,-8.338842,-3.017420,1.030943,6.716166,4.752481]]], dtype = "float64")#candidate|3084|(7, 10, 12)|const|float64
uop_3085 = relay.sin(const_3084.astype('float64')) # shape=(7, 10, 12)
func_1197_call = mod.get_global_var('func_1197')
func_1198_call = mutated_mod.get_global_var('func_1198')
call_3087 = relay.TupleGetItem(func_1197_call(), 1)
call_3088 = relay.TupleGetItem(func_1198_call(), 1)
output = relay.Tuple([uop_3085,call_3087,])
output2 = relay.Tuple([uop_3085,call_3088,])
func_3089 = relay.Function([], output)
mod['func_3089'] = func_3089
mod = relay.transform.InferType()(mod)
output = func_3089()
func_3090 = relay.Function([], output)
mutated_mod['func_3090'] = func_3090
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1633_call = mod.get_global_var('func_1633')
func_1634_call = mutated_mod.get_global_var('func_1634')
call_3097 = relay.TupleGetItem(func_1633_call(), 0)
call_3098 = relay.TupleGetItem(func_1634_call(), 0)
func_926_call = mod.get_global_var('func_926')
func_928_call = mutated_mod.get_global_var('func_928')
call_3105 = relay.TupleGetItem(func_926_call(), 1)
call_3106 = relay.TupleGetItem(func_928_call(), 1)
output = relay.Tuple([call_3097,call_3105,])
output2 = relay.Tuple([call_3098,call_3106,])
func_3109 = relay.Function([], output)
mod['func_3109'] = func_3109
mod = relay.transform.InferType()(mod)
output = func_3109()
func_3110 = relay.Function([], output)
mutated_mod['func_3110'] = func_3110
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3079_call = mod.get_global_var('func_3079')
func_3080_call = mutated_mod.get_global_var('func_3080')
call_3130 = relay.TupleGetItem(func_3079_call(), 0)
call_3131 = relay.TupleGetItem(func_3080_call(), 0)
uop_3149 = relay.sqrt(call_3130.astype('float64')) # shape=(6, 2, 6)
uop_3151 = relay.sqrt(call_3131.astype('float64')) # shape=(6, 2, 6)
uop_3152 = relay.rsqrt(uop_3149.astype('float64')) # shape=(6, 2, 6)
uop_3154 = relay.rsqrt(uop_3151.astype('float64')) # shape=(6, 2, 6)
uop_3164 = relay.tan(uop_3152.astype('float32')) # shape=(6, 2, 6)
uop_3166 = relay.tan(uop_3154.astype('float32')) # shape=(6, 2, 6)
var_3183 = relay.var("var_3183", dtype = "float32", shape = (6, 2, 6))#candidate|3183|(6, 2, 6)|var|float32
bop_3184 = relay.minimum(uop_3164.astype('int8'), relay.reshape(var_3183.astype('int8'), relay.shape_of(uop_3164))) # shape=(6, 2, 6)
bop_3187 = relay.minimum(uop_3166.astype('int8'), relay.reshape(var_3183.astype('int8'), relay.shape_of(uop_3166))) # shape=(6, 2, 6)
const_3195 = relay.const([[[-4,-1,5,-5,2,-8],[8,5,7,3,7,-4]],[[-4,3,5,-7,1,1],[-6,8,8,-7,9,2]],[[-9,6,2,5,4,-3],[10,-7,-10,4,7,-3]],[[1,-1,-2,-8,5,9],[3,-3,-1,-3,-8,1]],[[-1,3,-10,2,8,2],[6,3,2,-1,5,2]],[[-2,-9,7,10,7,-5],[10,6,3,-2,-8,2]]], dtype = "int8")#candidate|3195|(6, 2, 6)|const|int8
bop_3196 = relay.multiply(bop_3184.astype('int32'), relay.reshape(const_3195.astype('int32'), relay.shape_of(bop_3184))) # shape=(6, 2, 6)
bop_3199 = relay.multiply(bop_3187.astype('int32'), relay.reshape(const_3195.astype('int32'), relay.shape_of(bop_3187))) # shape=(6, 2, 6)
output = relay.Tuple([bop_3196,])
output2 = relay.Tuple([bop_3199,])
func_3204 = relay.Function([var_3183,], output)
mod['func_3204'] = func_3204
mod = relay.transform.InferType()(mod)
mutated_mod['func_3204'] = func_3204
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3205 = relay.var("var_3205", dtype = "float32", shape = (6, 2, 6))#candidate|3205|(6, 2, 6)|var|float32
func_3204_call = mutated_mod.get_global_var('func_3204')
call_3206 = func_3204_call(var_3205)
output = call_3206
func_3207 = relay.Function([var_3205], output)
mutated_mod['func_3207'] = func_3207
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3212 = relay.var("var_3212", dtype = "uint64", shape = (5, 5, 1))#candidate|3212|(5, 5, 1)|var|uint64
var_3213 = relay.var("var_3213", dtype = "uint64", shape = (5, 5, 10))#candidate|3213|(5, 5, 10)|var|uint64
bop_3214 = relay.bitwise_and(var_3212.astype('uint64'), var_3213.astype('uint64')) # shape=(5, 5, 10)
output = bop_3214
output2 = bop_3214
func_3218 = relay.Function([var_3212,var_3213,], output)
mod['func_3218'] = func_3218
mod = relay.transform.InferType()(mod)
var_3219 = relay.var("var_3219", dtype = "uint64", shape = (5, 5, 1))#candidate|3219|(5, 5, 1)|var|uint64
var_3220 = relay.var("var_3220", dtype = "uint64", shape = (5, 5, 10))#candidate|3220|(5, 5, 10)|var|uint64
output = func_3218(var_3219,var_3220,)
func_3221 = relay.Function([var_3219,var_3220,], output)
mutated_mod['func_3221'] = func_3221
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2832_call = mod.get_global_var('func_2832')
func_2833_call = mutated_mod.get_global_var('func_2833')
call_3259 = func_2832_call()
call_3260 = func_2832_call()
output = call_3259
output2 = call_3260
func_3263 = relay.Function([], output)
mod['func_3263'] = func_3263
mod = relay.transform.InferType()(mod)
output = func_3263()
func_3264 = relay.Function([], output)
mutated_mod['func_3264'] = func_3264
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2994_call = mod.get_global_var('func_2994')
func_2996_call = mutated_mod.get_global_var('func_2996')
call_3275 = relay.TupleGetItem(func_2994_call(), 0)
call_3276 = relay.TupleGetItem(func_2996_call(), 0)
output = call_3275
output2 = call_3276
func_3277 = relay.Function([], output)
mod['func_3277'] = func_3277
mod = relay.transform.InferType()(mod)
output = func_3277()
func_3278 = relay.Function([], output)
mutated_mod['func_3278'] = func_3278
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3319 = relay.var("var_3319", dtype = "uint16", shape = (9, 11, 10))#candidate|3319|(9, 11, 10)|var|uint16
const_3320 = relay.const([[[-1,4,8,-10,-4,-9,-1,6,4,-7],[9,-5,6,6,-10,-3,-5,-4,7,-3],[5,1,-3,-9,-6,1,6,4,-3,1],[3,4,-1,2,-2,-10,-8,-7,5,7],[4,9,-6,-6,-3,2,-3,5,-5,-1],[-3,6,-1,10,8,-9,7,-6,3,2],[9,4,-10,-3,8,-4,6,-10,-2,4],[10,-6,-5,2,2,-4,7,2,-8,4],[10,5,-7,-2,-9,-1,-4,-8,9,5],[-3,2,-8,7,9,2,-9,-5,3,-7],[8,3,-7,8,-8,-7,3,-1,4,-9]],[[-1,-4,7,7,1,-4,2,-10,8,-4],[3,9,1,-9,10,-1,6,-3,9,4],[-4,8,6,4,7,2,9,6,-3,-8],[10,6,-7,8,9,-3,-10,10,10,-2],[3,-5,-7,-6,-5,-5,-4,-10,10,-4],[-7,3,-9,-3,-10,-7,9,7,4,-6],[8,1,-2,2,8,2,-2,-3,9,-1],[1,2,-10,7,4,3,7,-5,-5,-1],[-10,8,-10,-4,-9,6,5,-1,10,-10],[-1,6,7,7,6,-6,-2,2,-7,1],[-3,5,6,4,-2,-10,-5,3,10,5]],[[1,-4,-6,-7,3,9,4,6,10,7],[2,6,-6,1,-2,-3,8,6,-4,-6],[-10,4,1,-7,8,4,5,-9,-3,-8],[9,-6,7,-2,8,9,-5,3,1,-8],[7,-10,1,5,2,-9,-3,9,-8,2],[-8,-3,3,10,9,2,-9,-8,2,6],[-5,6,-1,-9,-7,-4,-3,10,6,-10],[10,-9,-4,3,8,-1,-4,2,-5,4],[-3,7,-7,2,10,8,-3,1,4,3],[-3,7,-3,-5,-10,-10,-9,-9,-5,2],[4,-7,7,-4,4,-2,-4,-6,-8,7]],[[10,-10,-4,7,-3,-7,7,4,4,4],[7,-6,-5,-10,-5,-2,2,-4,-3,8],[-10,-3,-10,10,6,1,9,6,10,-8],[1,-10,4,-3,-6,4,-5,10,5,9],[-5,-7,-8,10,-7,2,10,4,7,10],[-8,7,3,-9,9,-10,-8,9,-7,5],[9,3,9,-5,5,-10,-2,-6,-6,1],[-5,-10,-7,-1,7,-2,1,-8,-5,9],[-8,10,-5,5,1,5,-9,9,3,2],[-5,-10,2,-1,1,-4,6,-9,10,2],[-1,9,3,6,9,-8,2,3,6,-10]],[[1,-5,10,9,9,-3,-8,10,10,7],[-4,4,-5,-2,10,-9,8,1,10,-9],[-1,1,5,-1,5,-4,7,7,-8,6],[-10,10,-8,5,-9,9,7,1,3,-8],[-4,-9,2,-4,2,-8,-4,10,9,2],[-10,-10,-2,10,3,-4,-10,-7,-9,-3],[-10,3,1,-7,-9,-8,9,7,-7,7],[-4,-6,-3,9,5,-3,4,2,-1,4],[6,-2,-8,-6,-7,6,3,-8,-8,-8],[-8,9,-1,7,-7,-4,3,-8,5,7],[-7,3,-6,4,-7,-6,-7,5,5,10]],[[3,7,-9,6,-8,-6,-5,-5,-10,-4],[3,-2,-6,-10,8,-4,-5,-8,5,6],[6,-10,-1,-3,-4,-9,-10,1,7,6],[-3,-8,-9,-1,-10,-10,9,1,-5,-2],[-5,7,-2,-9,10,-6,-4,-9,1,-9],[-9,1,-1,9,-9,6,-3,-7,-9,-4],[2,2,-4,-2,1,8,-2,-7,3,10],[6,-6,-9,2,1,-9,-5,10,-1,4],[4,9,3,1,-1,-10,9,6,10,9],[3,4,-8,7,7,-1,-1,6,-6,2],[10,-6,7,-10,-9,8,-7,-2,-7,4]],[[8,4,6,5,-9,-3,10,-1,-9,-6],[7,2,6,-9,-3,-8,10,2,2,-10],[-6,-3,10,7,-2,-10,7,-3,8,-10],[6,-1,10,4,3,-4,-7,-9,-8,8],[9,8,-2,3,-4,-2,-8,9,-8,-9],[-7,4,-9,-2,-9,-8,-2,4,-1,5],[-9,8,-10,5,-9,1,-9,-9,7,-7],[4,5,-6,-10,-6,-2,2,2,4,3],[4,-1,-10,1,-2,4,-8,3,-7,-8],[-10,8,8,-5,9,-10,-4,4,-9,-9],[-5,-10,1,-6,-6,1,-5,-7,3,9]],[[-2,5,-8,-7,-7,-2,1,-5,5,1],[6,-9,-5,5,-8,9,3,-5,-4,2],[1,4,-7,-6,-2,6,-1,10,1,3],[2,-1,-8,8,1,5,-5,3,10,6],[6,-10,9,4,-5,-1,-9,-2,1,10],[1,3,6,1,5,10,1,10,-1,-2],[-1,3,-9,8,-6,-1,4,6,8,-8],[7,6,-7,10,1,4,8,4,4,-7],[-10,1,10,6,5,3,-1,9,-7,5],[2,-2,9,-8,-9,7,-1,5,-4,-3],[6,-2,-7,4,2,4,3,6,3,6]],[[9,1,-10,5,-9,6,4,-4,-8,7],[-10,-6,6,-6,6,-8,5,-6,8,-2],[10,4,-5,5,7,-3,-2,1,-1,-6],[8,3,-3,-10,-2,10,10,6,-2,-9],[4,7,3,3,-6,-2,-2,8,3,8],[10,-7,-2,8,-5,-3,10,-2,-10,8],[3,10,4,3,-8,5,9,-10,5,2],[-4,-9,-7,-7,6,-4,-5,4,-4,7],[8,-10,3,5,-8,8,-4,-4,7,-9],[-9,4,9,3,7,-5,-1,-1,5,-2],[4,4,-6,10,-4,-8,4,-6,4,-4]]], dtype = "uint16")#candidate|3320|(9, 11, 10)|const|uint16
bop_3321 = relay.add(var_3319.astype('uint16'), relay.reshape(const_3320.astype('uint16'), relay.shape_of(var_3319))) # shape=(9, 11, 10)
var_3331 = relay.var("var_3331", dtype = "uint16", shape = (9, 11, 10))#candidate|3331|(9, 11, 10)|var|uint16
bop_3332 = relay.floor_divide(bop_3321.astype('float32'), relay.reshape(var_3331.astype('float32'), relay.shape_of(bop_3321))) # shape=(9, 11, 10)
func_2832_call = mod.get_global_var('func_2832')
func_2833_call = mutated_mod.get_global_var('func_2833')
call_3338 = func_2832_call()
call_3339 = func_2832_call()
output = relay.Tuple([bop_3332,call_3338,])
output2 = relay.Tuple([bop_3332,call_3339,])
func_3340 = relay.Function([var_3319,var_3331,], output)
mod['func_3340'] = func_3340
mod = relay.transform.InferType()(mod)
var_3341 = relay.var("var_3341", dtype = "uint16", shape = (9, 11, 10))#candidate|3341|(9, 11, 10)|var|uint16
var_3342 = relay.var("var_3342", dtype = "uint16", shape = (9, 11, 10))#candidate|3342|(9, 11, 10)|var|uint16
output = func_3340(var_3341,var_3342,)
func_3343 = relay.Function([var_3341,var_3342,], output)
mutated_mod['func_3343'] = func_3343
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3430 = relay.var("var_3430", dtype = "float64", shape = (14, 8, 2))#candidate|3430|(14, 8, 2)|var|float64
const_3431 = relay.const([[[9.869710,-8.902113],[-4.609685,2.033254],[-0.153574,6.814451],[4.149266,7.663755],[-6.738843,1.534943],[-4.798164,6.903867],[-6.855031,-8.298347],[-2.621366,-6.379583]],[[-0.134626,4.811364],[-7.576994,-7.735347],[-3.582834,-5.805004],[-9.121184,-0.642082],[-9.545226,7.471393],[-7.047774,3.706109],[-0.039866,5.601326],[-5.707163,-7.733290]],[[-1.530084,8.894553],[9.007819,5.331931],[3.888848,0.765408],[-1.698716,-2.063601],[8.656155,0.917468],[-1.477298,-1.998680],[-5.701570,5.072155],[5.171119,-5.576337]],[[-8.568758,-2.268970],[9.932165,6.166621],[2.301602,-1.793864],[7.001410,8.797163],[5.512465,-0.721927],[3.742628,-7.339423],[-9.533325,-7.379091],[-6.202669,8.993362]],[[-8.343306,-5.684814],[-5.933666,-2.280305],[-5.616795,0.958441],[-9.201231,1.131171],[0.667916,3.164126],[-4.127805,-4.808832],[-9.615121,4.641750],[5.281505,9.046674]],[[-1.733441,-8.896723],[8.541290,9.498528],[2.844645,3.310800],[0.829830,9.971157],[-2.486846,3.611754],[9.241437,2.091330],[4.206048,-8.513379],[-4.851502,-8.990422]],[[9.008786,3.224683],[-7.006658,-6.193955],[0.697398,3.273604],[-8.528089,7.090144],[2.904195,-5.776380],[-9.145750,-0.338855],[-5.258894,4.125706],[-7.026735,1.574705]],[[-1.229114,3.791486],[4.245581,-8.337248],[1.412173,0.473758],[1.216917,6.618908],[-9.408661,1.323141],[3.678954,-0.984459],[-3.861794,-2.973306],[6.171846,-7.569368]],[[-0.898929,-4.012083],[4.077839,-9.907467],[-4.381140,6.639563],[-4.781001,6.718418],[-0.382067,-1.508998],[-8.353116,8.733255],[-3.796004,-4.546829],[7.190842,0.413720]],[[-0.498194,-0.698916],[-7.226441,-9.259829],[-0.669380,-7.376487],[-2.508902,9.311637],[-0.460751,7.030783],[-6.066951,7.352999],[-6.966919,4.473012],[-1.429230,-3.847900]],[[-3.332020,1.193508],[0.276908,-3.303604],[1.043138,6.092304],[-4.157021,-1.184407],[-9.511746,9.027731],[-0.939083,7.387681],[-7.827377,-2.548491],[9.011690,9.962553]],[[9.176580,-0.404844],[1.230198,9.516963],[-2.032513,-8.389107],[8.795677,5.207294],[-5.913312,1.064284],[-7.632698,-2.190712],[9.134401,3.701821],[3.564807,-9.815483]],[[8.510855,5.719157],[7.122187,3.298175],[2.476822,-3.179330],[-6.358369,-9.104078],[7.308131,5.944395],[-3.127762,-8.021816],[9.471021,-1.806023],[8.005429,8.802211]],[[-8.077562,1.420123],[7.967791,4.854432],[-3.510117,-0.741462],[5.613647,-1.711544],[-6.064394,-3.542209],[4.795901,-6.264551],[8.542859,5.431418],[8.590382,6.915059]]], dtype = "float64")#candidate|3431|(14, 8, 2)|const|float64
bop_3432 = relay.equal(var_3430.astype('bool'), relay.reshape(const_3431.astype('bool'), relay.shape_of(var_3430))) # shape=(14, 8, 2)
func_1472_call = mod.get_global_var('func_1472')
func_1474_call = mutated_mod.get_global_var('func_1474')
var_3444 = relay.var("var_3444", dtype = "float64", shape = (108,))#candidate|3444|(108,)|var|float64
call_3443 = relay.TupleGetItem(func_1472_call(relay.reshape(var_3444.astype('float64'), [6, 3, 6])), 1)
call_3445 = relay.TupleGetItem(func_1474_call(relay.reshape(var_3444.astype('float64'), [6, 3, 6])), 1)
output = relay.Tuple([bop_3432,call_3443,var_3444,])
output2 = relay.Tuple([bop_3432,call_3445,var_3444,])
func_3449 = relay.Function([var_3430,var_3444,], output)
mod['func_3449'] = func_3449
mod = relay.transform.InferType()(mod)
mutated_mod['func_3449'] = func_3449
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3449_call = mutated_mod.get_global_var('func_3449')
var_3451 = relay.var("var_3451", dtype = "float64", shape = (14, 8, 2))#candidate|3451|(14, 8, 2)|var|float64
var_3452 = relay.var("var_3452", dtype = "float64", shape = (108,))#candidate|3452|(108,)|var|float64
call_3450 = func_3449_call(var_3451,var_3452,)
output = call_3450
func_3453 = relay.Function([var_3451,var_3452,], output)
mutated_mod['func_3453'] = func_3453
mutated_mod = relay.transform.InferType()(mutated_mod)
func_119_call = mod.get_global_var('func_119')
func_121_call = mutated_mod.get_global_var('func_121')
call_3460 = relay.TupleGetItem(func_119_call(), 2)
call_3461 = relay.TupleGetItem(func_121_call(), 2)
func_1426_call = mod.get_global_var('func_1426')
func_1429_call = mutated_mod.get_global_var('func_1429')
var_3463 = relay.var("var_3463", dtype = "uint8", shape = (65, 4))#candidate|3463|(65, 4)|var|uint8
call_3462 = relay.TupleGetItem(func_1426_call(relay.reshape(var_3463.astype('uint8'), [260,])), 3)
call_3464 = relay.TupleGetItem(func_1429_call(relay.reshape(var_3463.astype('uint8'), [260,])), 3)
uop_3493 = relay.cos(var_3463.astype('float64')) # shape=(65, 4)
output = relay.Tuple([call_3460,call_3462,uop_3493,])
output2 = relay.Tuple([call_3461,call_3464,uop_3493,])
func_3499 = relay.Function([var_3463,], output)
mod['func_3499'] = func_3499
mod = relay.transform.InferType()(mod)
var_3500 = relay.var("var_3500", dtype = "uint8", shape = (65, 4))#candidate|3500|(65, 4)|var|uint8
output = func_3499(var_3500)
func_3501 = relay.Function([var_3500], output)
mutated_mod['func_3501'] = func_3501
mutated_mod = relay.transform.InferType()(mutated_mod)
func_167_call = mod.get_global_var('func_167')
func_168_call = mutated_mod.get_global_var('func_168')
call_3530 = relay.TupleGetItem(func_167_call(), 0)
call_3531 = relay.TupleGetItem(func_168_call(), 0)
func_119_call = mod.get_global_var('func_119')
func_121_call = mutated_mod.get_global_var('func_121')
call_3533 = relay.TupleGetItem(func_119_call(), 0)
call_3534 = relay.TupleGetItem(func_121_call(), 0)
output = relay.Tuple([call_3530,call_3533,])
output2 = relay.Tuple([call_3531,call_3534,])
func_3536 = relay.Function([], output)
mod['func_3536'] = func_3536
mod = relay.transform.InferType()(mod)
mutated_mod['func_3536'] = func_3536
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3536_call = mutated_mod.get_global_var('func_3536')
call_3537 = func_3536_call()
output = call_3537
func_3538 = relay.Function([], output)
mutated_mod['func_3538'] = func_3538
mutated_mod = relay.transform.InferType()(mutated_mod)
func_119_call = mod.get_global_var('func_119')
func_121_call = mutated_mod.get_global_var('func_121')
call_3552 = relay.TupleGetItem(func_119_call(), 2)
call_3553 = relay.TupleGetItem(func_121_call(), 2)
func_1633_call = mod.get_global_var('func_1633')
func_1634_call = mutated_mod.get_global_var('func_1634')
call_3575 = relay.TupleGetItem(func_1633_call(), 0)
call_3576 = relay.TupleGetItem(func_1634_call(), 0)
output = relay.Tuple([call_3552,call_3575,])
output2 = relay.Tuple([call_3553,call_3576,])
func_3579 = relay.Function([], output)
mod['func_3579'] = func_3579
mod = relay.transform.InferType()(mod)
output = func_3579()
func_3580 = relay.Function([], output)
mutated_mod['func_3580'] = func_3580
mutated_mod = relay.transform.InferType()(mutated_mod)
func_285_call = mod.get_global_var('func_285')
func_286_call = mutated_mod.get_global_var('func_286')
call_3596 = func_285_call()
call_3597 = func_285_call()
output = call_3596
output2 = call_3597
func_3601 = relay.Function([], output)
mod['func_3601'] = func_3601
mod = relay.transform.InferType()(mod)
output = func_3601()
func_3602 = relay.Function([], output)
mutated_mod['func_3602'] = func_3602
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3089_call = mod.get_global_var('func_3089')
func_3090_call = mutated_mod.get_global_var('func_3090')
call_3617 = relay.TupleGetItem(func_3089_call(), 1)
call_3618 = relay.TupleGetItem(func_3090_call(), 1)
output = call_3617
output2 = call_3618
func_3634 = relay.Function([], output)
mod['func_3634'] = func_3634
mod = relay.transform.InferType()(mod)
output = func_3634()
func_3635 = relay.Function([], output)
mutated_mod['func_3635'] = func_3635
mutated_mod = relay.transform.InferType()(mutated_mod)
func_242_call = mod.get_global_var('func_242')
func_243_call = mutated_mod.get_global_var('func_243')
call_3709 = relay.TupleGetItem(func_242_call(), 0)
call_3710 = relay.TupleGetItem(func_243_call(), 0)
func_1834_call = mod.get_global_var('func_1834')
func_1836_call = mutated_mod.get_global_var('func_1836')
call_3713 = func_1834_call()
call_3714 = func_1834_call()
output = relay.Tuple([call_3709,call_3713,])
output2 = relay.Tuple([call_3710,call_3714,])
func_3715 = relay.Function([], output)
mod['func_3715'] = func_3715
mod = relay.transform.InferType()(mod)
mutated_mod['func_3715'] = func_3715
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3715_call = mutated_mod.get_global_var('func_3715')
call_3716 = func_3715_call()
output = call_3716
func_3717 = relay.Function([], output)
mutated_mod['func_3717'] = func_3717
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3579_call = mod.get_global_var('func_3579')
func_3580_call = mutated_mod.get_global_var('func_3580')
call_3720 = relay.TupleGetItem(func_3579_call(), 0)
call_3721 = relay.TupleGetItem(func_3580_call(), 0)
func_3218_call = mod.get_global_var('func_3218')
func_3221_call = mutated_mod.get_global_var('func_3221')
const_3724 = relay.const([[-5,-7,-7,-1,6],[-1,2,-5,6,-5],[-9,9,5,-5,9],[5,10,3,3,-10],[-9,-3,9,-6,-8]], dtype = "uint64")#candidate|3724|(5, 5)|const|uint64
const_3725 = relay.const([[-8,-9,3,10,-7,-8,-6,-4,8,9],[-5,-9,5,3,-1,-3,-8,-1,-4,-10],[6,1,-5,-3,6,2,10,8,-5,5],[1,-5,10,1,-9,-7,1,10,-3,-8],[4,-4,1,2,-4,2,-6,-8,4,-2],[-10,-9,7,6,2,-10,-4,-1,-6,-3],[-1,-8,1,-3,5,8,-4,-6,-6,-10],[-6,5,7,-7,10,-5,-4,-9,-9,9],[-8,9,4,3,-8,8,-5,8,-8,5],[4,10,3,2,-4,5,-8,3,10,3],[1,3,-6,-10,-5,-4,-4,-8,6,10],[3,-9,10,4,-8,-7,10,-4,1,1],[-8,-7,-9,-3,5,2,-9,-10,3,-8],[-2,-1,-6,-7,1,-5,10,3,-6,-4],[-10,-10,7,9,-5,4,-3,-10,-2,-6],[-4,1,-2,5,1,-9,-4,-3,1,3],[-8,-3,-2,9,-9,-4,-5,-7,9,5],[1,-2,-4,-6,-6,1,7,-6,7,10],[2,7,1,6,-7,-10,4,-3,-9,-1],[9,-1,-6,-5,2,-8,-1,2,10,2],[7,-6,-7,9,-8,-3,2,3,-8,-2],[-6,-3,-5,9,-2,-5,-4,-2,-9,-7],[1,4,-1,-5,7,-9,8,-10,-10,-10],[-1,-1,-5,-5,4,-1,-1,10,4,-3],[3,-6,8,3,8,-8,8,5,6,10]], dtype = "uint64")#candidate|3725|(25, 10)|const|uint64
call_3723 = func_3218_call(relay.reshape(const_3724.astype('uint64'), [5, 5, 1]), relay.reshape(const_3725.astype('uint64'), [5, 5, 10]), )
call_3726 = func_3218_call(relay.reshape(const_3724.astype('uint64'), [5, 5, 1]), relay.reshape(const_3725.astype('uint64'), [5, 5, 10]), )
output = relay.Tuple([call_3720,call_3723,const_3724,const_3725,])
output2 = relay.Tuple([call_3721,call_3726,const_3724,const_3725,])
func_3735 = relay.Function([], output)
mod['func_3735'] = func_3735
mod = relay.transform.InferType()(mod)
output = func_3735()
func_3736 = relay.Function([], output)
mutated_mod['func_3736'] = func_3736
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2994_call = mod.get_global_var('func_2994')
func_2996_call = mutated_mod.get_global_var('func_2996')
call_3763 = relay.TupleGetItem(func_2994_call(), 0)
call_3764 = relay.TupleGetItem(func_2996_call(), 0)
output = call_3763
output2 = call_3764
func_3775 = relay.Function([], output)
mod['func_3775'] = func_3775
mod = relay.transform.InferType()(mod)
mutated_mod['func_3775'] = func_3775
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3775_call = mutated_mod.get_global_var('func_3775')
call_3776 = func_3775_call()
output = call_3776
func_3777 = relay.Function([], output)
mutated_mod['func_3777'] = func_3777
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3816 = relay.const([[[-9.415001,0.442508,-8.291029,-2.535749,-6.462029,-1.379037,-6.979304,6.364818,8.884049,0.812616,1.629886,-1.193950,-4.113074],[-4.514743,3.239299,8.801972,5.102728,-8.859531,0.239466,-2.112448,-0.871300,0.734845,0.607476,1.337452,6.140928,-6.788729],[-1.542399,1.905899,7.182306,7.901561,9.822735,-9.597695,4.481690,-6.838551,4.020606,3.824960,4.907814,-8.914080,2.955868],[-1.499864,2.945716,0.041259,0.161849,-4.814403,-7.668826,4.980327,-4.470672,7.093568,-2.875450,-1.624340,-2.479165,1.701190],[-7.508103,-1.562512,-1.254388,-5.825666,8.989562,7.672272,-8.535324,8.869145,9.390017,-7.753482,8.958789,-6.595987,3.064812],[7.600481,-9.341968,-9.593882,2.913774,-1.859666,2.954037,2.573782,-5.975367,0.772048,-6.273832,0.740203,6.193658,-0.750535],[3.865559,9.140834,6.559313,-0.374753,0.159845,8.230580,8.627859,-6.623269,-0.803636,-7.212897,6.403451,-4.986640,-0.393326]],[[7.039497,5.746231,-1.517298,-1.754151,-2.022371,7.193034,7.532605,1.115150,9.719246,-2.250626,1.715214,5.175880,8.928947],[9.207483,-8.245452,-6.194630,2.945154,8.106024,-3.492794,6.585949,-6.906108,-1.128523,-7.798364,-5.528678,-5.930552,6.727516],[0.053452,8.120711,5.896557,-3.474583,8.182610,-9.436423,6.000727,-4.220263,7.115973,-7.870669,-0.614847,-0.763313,-7.774261],[-1.343917,7.318541,-3.291928,-3.892098,-8.943930,-3.881711,-3.349374,0.316164,-2.442000,-1.505870,-2.453452,4.044722,5.907262],[4.082299,-1.060898,-2.495665,7.569175,-6.125162,1.227527,7.723014,2.690021,-2.003997,5.169495,-5.299205,-4.163996,7.202610],[-6.701070,6.995677,-3.037763,0.132850,-7.386678,-7.034575,-2.403940,4.092416,1.714403,9.615915,-7.920555,-5.964993,9.923833],[-0.898718,-2.260402,-5.264680,-6.985628,-0.122058,1.992591,2.083074,-1.980986,8.109926,-5.219059,-6.381507,8.079019,-6.879256]],[[2.850929,-2.369490,9.533502,7.930797,-7.232816,4.913031,4.070122,2.981663,2.496352,9.657837,-9.861922,-7.956074,2.747375],[9.261451,-4.003762,9.805772,-5.899705,-7.715921,-7.888628,4.939894,-0.848754,9.657515,7.354810,-7.865766,0.411712,-2.456931],[-6.921889,-2.706750,6.702591,-4.718517,-4.073988,7.197622,0.910688,-1.006872,1.188573,-4.218596,-7.266073,-3.903699,0.814014],[5.459281,-7.140179,-7.978185,-1.682853,-5.630185,-8.869023,-7.534623,-2.411274,-0.435643,8.604544,4.202513,-6.542227,-7.733612],[3.101692,-8.053726,8.051247,4.843941,0.112803,-2.488993,0.794949,1.479739,-4.634088,-3.355638,-9.036398,-1.705491,5.536718],[-1.853953,-3.070910,2.776978,0.067242,-9.662641,8.829824,-2.209601,0.833737,-8.073372,-9.146982,7.540870,1.939895,9.450508],[-7.120385,-6.843791,-4.936752,4.830601,8.542021,-4.941588,8.672674,-1.561155,7.229026,5.124916,0.162310,3.280529,-5.384325]],[[-9.214498,-5.077429,7.495376,-6.718342,-5.716593,-1.584859,2.219926,-1.474251,4.291966,-8.617551,-2.910412,-6.453213,-4.811962],[-8.754412,2.681589,-1.990521,-4.007875,-0.984404,1.240357,2.702640,0.536022,-3.767432,-0.568442,-0.031628,-5.221725,0.340587],[-6.698072,-2.624635,4.073032,-8.429415,0.061379,8.793607,5.155505,1.487355,-8.715802,3.273900,7.120723,-9.128607,-2.381158],[2.491196,9.744411,-9.829813,-1.128818,-1.771444,3.800097,4.945190,-0.564783,-4.398768,-4.873165,-1.831071,2.190027,-4.066391],[7.652990,-6.672375,9.388328,-4.943486,-1.210743,5.692116,-8.905565,-7.284564,-5.952702,-2.851096,-3.597407,9.764625,3.596396],[4.431264,9.814479,7.285396,-2.433485,-9.401776,4.110484,-2.821985,2.113674,-2.638305,-7.275738,8.159756,-5.457165,0.686364],[8.733808,7.555775,-0.831519,3.476027,-7.062556,8.081479,-3.838957,9.470098,-4.287933,6.606095,2.194234,1.420801,-3.850853]],[[-9.157955,6.233862,-3.117503,-4.846789,9.324977,-6.607194,-3.828782,5.536778,-6.607825,-0.983968,6.887351,6.919765,-4.003782],[-8.569775,-1.437821,6.921301,-8.351340,-2.544588,5.853098,-8.755475,-5.534016,8.556170,-5.929258,-0.024004,-6.287477,-8.574244],[9.589458,-8.938085,-4.562419,-6.750579,8.675381,0.484031,-8.937619,-7.248894,1.366496,-6.663843,-8.479037,-3.935466,-2.936813],[0.433608,2.528479,-7.283370,7.081462,2.502677,2.760115,9.673342,6.068739,-0.614601,-8.495315,1.311447,-7.496935,5.225775],[3.438620,0.900008,-2.064408,-9.835931,-3.511305,7.013700,9.130035,8.461229,-4.759937,3.516739,4.967238,6.481095,7.637758],[8.976694,-6.741249,-7.960089,6.922846,7.372638,-2.773254,2.047072,-3.491304,-7.939055,4.611426,-1.860883,-3.338342,8.912751],[-0.092828,-4.258085,3.046014,8.347437,-9.746600,7.777127,7.490021,-1.190201,-9.220642,-7.143109,-2.463022,-8.772711,-0.365234]]], dtype = "float32")#candidate|3816|(5, 7, 13)|const|float32
uop_3817 = relay.asin(const_3816.astype('float32')) # shape=(5, 7, 13)
output = relay.Tuple([uop_3817,])
output2 = relay.Tuple([uop_3817,])
func_3819 = relay.Function([], output)
mod['func_3819'] = func_3819
mod = relay.transform.InferType()(mod)
mutated_mod['func_3819'] = func_3819
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3819_call = mutated_mod.get_global_var('func_3819')
call_3820 = func_3819_call()
output = call_3820
func_3821 = relay.Function([], output)
mutated_mod['func_3821'] = func_3821
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1745_call = mod.get_global_var('func_1745')
func_1746_call = mutated_mod.get_global_var('func_1746')
call_3846 = func_1745_call()
call_3847 = func_1745_call()
var_3853 = relay.var("var_3853", dtype = "bool", shape = (6, 12, 6))#candidate|3853|(6, 12, 6)|var|bool
bop_3854 = relay.not_equal(call_3846.astype('bool'), var_3853.astype('bool')) # shape=(6, 12, 6)
bop_3857 = relay.not_equal(call_3847.astype('bool'), var_3853.astype('bool')) # shape=(6, 12, 6)
uop_3871 = relay.sqrt(call_3846.astype('float64')) # shape=(6, 1, 6)
uop_3873 = relay.sqrt(call_3847.astype('float64')) # shape=(6, 1, 6)
func_3449_call = mod.get_global_var('func_3449')
func_3453_call = mutated_mod.get_global_var('func_3453')
var_3881 = relay.var("var_3881", dtype = "float64", shape = (224,))#candidate|3881|(224,)|var|float64
var_3882 = relay.var("var_3882", dtype = "float64", shape = (108,))#candidate|3882|(108,)|var|float64
call_3880 = relay.TupleGetItem(func_3449_call(relay.reshape(var_3881.astype('float64'), [14, 8, 2]), relay.reshape(var_3882.astype('float64'), [108,]), ), 0)
call_3883 = relay.TupleGetItem(func_3453_call(relay.reshape(var_3881.astype('float64'), [14, 8, 2]), relay.reshape(var_3882.astype('float64'), [108,]), ), 0)
output = relay.Tuple([bop_3854,uop_3871,call_3880,var_3881,var_3882,])
output2 = relay.Tuple([bop_3857,uop_3873,call_3883,var_3881,var_3882,])
func_3892 = relay.Function([var_3853,var_3881,var_3882,], output)
mod['func_3892'] = func_3892
mod = relay.transform.InferType()(mod)
mutated_mod['func_3892'] = func_3892
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3892_call = mutated_mod.get_global_var('func_3892')
var_3894 = relay.var("var_3894", dtype = "bool", shape = (6, 12, 6))#candidate|3894|(6, 12, 6)|var|bool
var_3895 = relay.var("var_3895", dtype = "float64", shape = (224,))#candidate|3895|(224,)|var|float64
var_3896 = relay.var("var_3896", dtype = "float64", shape = (108,))#candidate|3896|(108,)|var|float64
call_3893 = func_3892_call(var_3894,var_3895,var_3896,)
output = call_3893
func_3897 = relay.Function([var_3894,var_3895,var_3896,], output)
mutated_mod['func_3897'] = func_3897
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1911_call = mod.get_global_var('func_1911')
func_1913_call = mutated_mod.get_global_var('func_1913')
call_3977 = relay.TupleGetItem(func_1911_call(), 0)
call_3978 = relay.TupleGetItem(func_1913_call(), 0)
var_3981 = relay.var("var_3981", dtype = "float32", shape = (6, 7, 6))#candidate|3981|(6, 7, 6)|var|float32
bop_3982 = relay.logical_xor(call_3977.astype('uint16'), var_3981.astype('uint16')) # shape=(6, 7, 6)
bop_3985 = relay.logical_xor(call_3978.astype('uint16'), var_3981.astype('uint16')) # shape=(6, 7, 6)
output = relay.Tuple([bop_3982,])
output2 = relay.Tuple([bop_3985,])
func_4005 = relay.Function([var_3981,], output)
mod['func_4005'] = func_4005
mod = relay.transform.InferType()(mod)
var_4006 = relay.var("var_4006", dtype = "float32", shape = (6, 7, 6))#candidate|4006|(6, 7, 6)|var|float32
output = func_4005(var_4006)
func_4007 = relay.Function([var_4006], output)
mutated_mod['func_4007'] = func_4007
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4113 = relay.var("var_4113", dtype = "uint32", shape = ())#candidate|4113|()|var|uint32
var_4114 = relay.var("var_4114", dtype = "uint32", shape = (10, 6, 5))#candidate|4114|(10, 6, 5)|var|uint32
bop_4115 = relay.maximum(var_4113.astype('uint32'), var_4114.astype('uint32')) # shape=(10, 6, 5)
bop_4125 = relay.less_equal(bop_4115.astype('bool'), var_4113.astype('bool')) # shape=(10, 6, 5)
output = bop_4125
output2 = bop_4125
func_4142 = relay.Function([var_4113,var_4114,], output)
mod['func_4142'] = func_4142
mod = relay.transform.InferType()(mod)
mutated_mod['func_4142'] = func_4142
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4142_call = mutated_mod.get_global_var('func_4142')
var_4144 = relay.var("var_4144", dtype = "uint32", shape = ())#candidate|4144|()|var|uint32
var_4145 = relay.var("var_4145", dtype = "uint32", shape = (10, 6, 5))#candidate|4145|(10, 6, 5)|var|uint32
call_4143 = func_4142_call(var_4144,var_4145,)
output = call_4143
func_4146 = relay.Function([var_4144,var_4145,], output)
mutated_mod['func_4146'] = func_4146
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2629_call = mod.get_global_var('func_2629')
func_2631_call = mutated_mod.get_global_var('func_2631')
call_4154 = relay.TupleGetItem(func_2629_call(), 0)
call_4155 = relay.TupleGetItem(func_2631_call(), 0)
output = relay.Tuple([call_4154,])
output2 = relay.Tuple([call_4155,])
func_4158 = relay.Function([], output)
mod['func_4158'] = func_4158
mod = relay.transform.InferType()(mod)
output = func_4158()
func_4159 = relay.Function([], output)
mutated_mod['func_4159'] = func_4159
mutated_mod = relay.transform.InferType()(mutated_mod)
func_255_call = mod.get_global_var('func_255')
func_256_call = mutated_mod.get_global_var('func_256')
call_4204 = func_255_call()
call_4205 = func_255_call()
func_2656_call = mod.get_global_var('func_2656')
func_2659_call = mutated_mod.get_global_var('func_2659')
const_4208 = relay.const([1,8,9,3,-1,8,-8,4], dtype = "uint32")#candidate|4208|(8,)|const|uint32
call_4207 = relay.TupleGetItem(func_2656_call(relay.reshape(const_4208.astype('uint32'), [4, 2, 1])), 0)
call_4209 = relay.TupleGetItem(func_2659_call(relay.reshape(const_4208.astype('uint32'), [4, 2, 1])), 0)
func_2059_call = mod.get_global_var('func_2059')
func_2061_call = mutated_mod.get_global_var('func_2061')
var_4212 = relay.var("var_4212", dtype = "float64", shape = (162, 2))#candidate|4212|(162, 2)|var|float64
call_4211 = relay.TupleGetItem(func_2059_call(relay.reshape(var_4212.astype('float64'), [6, 9, 6])), 2)
call_4213 = relay.TupleGetItem(func_2061_call(relay.reshape(var_4212.astype('float64'), [6, 9, 6])), 2)
func_276_call = mod.get_global_var('func_276')
func_278_call = mutated_mod.get_global_var('func_278')
call_4219 = func_276_call()
call_4220 = func_276_call()
bop_4228 = relay.power(call_4207.astype('float32'), relay.reshape(const_4208.astype('float32'), relay.shape_of(call_4207))) # shape=(4, 2, 1)
bop_4231 = relay.power(call_4209.astype('float32'), relay.reshape(const_4208.astype('float32'), relay.shape_of(call_4209))) # shape=(4, 2, 1)
output = relay.Tuple([call_4204,call_4211,var_4212,call_4219,bop_4228,])
output2 = relay.Tuple([call_4205,call_4213,var_4212,call_4220,bop_4231,])
func_4233 = relay.Function([var_4212,], output)
mod['func_4233'] = func_4233
mod = relay.transform.InferType()(mod)
var_4234 = relay.var("var_4234", dtype = "float64", shape = (162, 2))#candidate|4234|(162, 2)|var|float64
output = func_4233(var_4234)
func_4235 = relay.Function([var_4234], output)
mutated_mod['func_4235'] = func_4235
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4239 = relay.var("var_4239", dtype = "float32", shape = ())#candidate|4239|()|var|float32
var_4240 = relay.var("var_4240", dtype = "float32", shape = (12, 11, 2))#candidate|4240|(12, 11, 2)|var|float32
bop_4241 = relay.floor_mod(var_4239.astype('float32'), var_4240.astype('float32')) # shape=(12, 11, 2)
func_3892_call = mod.get_global_var('func_3892')
func_3897_call = mutated_mod.get_global_var('func_3897')
var_4245 = relay.var("var_4245", dtype = "bool", shape = (432,))#candidate|4245|(432,)|var|bool
const_4246 = relay.const([[3.283696,-6.406909,-0.252847,-7.613891,-4.826651,-2.609707,1.062046,7.420042,-3.864799,-6.168120,-0.564903,6.876169,1.541653,-8.447496,-9.903868,1.652868,4.526807,-8.431258,5.571789,7.936951,6.113927,6.271097,-3.243541,5.561959,-9.692554,-6.874982,-6.399204,-2.838436,-9.860885,6.426294,4.414753,6.167959,-1.588999,8.013553,-6.168109,6.044680,-8.260977,5.444969,1.504505,9.633061,-1.093781,-3.066608,-5.582840,6.097791,-6.274857,9.317105,5.349748,-4.693235,-4.828271,7.546199,8.384104,-3.795046,-4.226478,-8.003434,-6.714158,8.562215,8.294383,5.660012,2.090968,4.963952,0.937122,8.063061,7.288256,-6.034876,7.806232,-0.343321,-1.218709,0.356900,-5.816508,-7.572392,5.998752,-4.018179,-3.873123,-6.175651,-3.454329,2.462774,1.882565,-6.991324,-6.262147,-6.060413,5.578084,-2.238853,-2.520515,-7.548867,9.663371,6.393687,-5.789904,-5.476602,-6.897304,-0.503873,-6.467377,-1.447618,6.120176,-1.432042,-7.909408,6.186369,6.620662,8.278608,9.593051,8.051140,3.442655,-9.709497,-6.625573,-1.637375,4.247384,1.946352,-5.345452,4.973392,-7.362237,1.171565,9.135747,-4.160124],[0.714089,-2.335998,5.314069,8.815068,-1.316820,2.921965,-5.341219,3.691457,-0.942570,8.875327,8.390695,-5.173194,-0.562547,-6.296939,3.592915,2.255286,-7.516831,1.864765,3.515518,-6.987293,-6.317102,-7.673968,0.219832,3.953068,-4.554584,-8.446363,8.545828,8.448316,4.856583,9.833781,5.258942,5.126755,-1.679720,8.358042,0.314824,-4.296812,0.201383,8.425608,-2.600220,7.264908,8.334277,-4.275943,-9.778655,5.580039,8.645205,-9.809686,5.458769,7.793085,4.787689,2.076968,-1.211679,-9.624144,-2.271007,0.208380,-5.503657,6.243197,-4.770881,8.901144,6.792628,-8.308515,9.768526,2.004938,-9.864464,3.737097,-2.787461,7.354609,-8.785517,-2.606832,3.034791,4.300078,-2.908855,3.830733,5.926276,-8.878249,9.711072,1.630639,3.129999,0.018796,4.148792,2.842076,9.193399,1.661617,8.801516,-2.766091,2.961920,-2.456675,-9.678066,-1.962840,-0.351488,5.787943,-1.008996,9.997714,2.853790,1.419309,9.034132,-2.449048,7.173486,-0.850657,-4.458789,9.507583,-5.414294,9.697712,-0.156439,-8.787034,-6.685910,-9.621240,2.309846,9.906369,3.729970,9.399324,0.265825,5.237654]], dtype = "float64")#candidate|4246|(2, 112)|const|float64
const_4247 = relay.const([9.929632,7.174861,3.897973,-5.150654,6.380727,-7.720698,-9.218450,-6.884216,-6.665956,5.352258,-7.082353,-7.218314,-9.354664,4.590225,9.661377,6.518982,9.353726,8.858503,-4.111349,-0.666498,-6.012576,2.579275,-6.510549,-7.965503,1.668352,-5.700276,5.539426,-4.874295,-6.347439,6.427894,-2.706370,-4.523181,-1.634398,-4.075217,-9.336012,-7.868774,-3.310951,4.161892,6.814581,5.973939,5.165208,-0.247717,1.839918,4.615195,-4.560541,2.212296,7.461384,2.440589,5.656458,-8.973772,-2.478728,6.568454,8.279105,5.535953,-6.298220,1.698005,-0.196800,-2.547222,-9.634841,-8.207754,4.918019,-6.484481,2.902235,-0.163377,6.046971,-1.522516,3.602426,-3.200110,3.244191,9.465908,3.315582,7.741448,-9.364060,9.541130,4.626864,-8.172499,5.128586,-7.471545,-3.484857,-9.645939,3.387031,1.828951,-4.182569,6.651326,-0.487630,5.092549,-7.718754,3.838858,6.960874,5.383973,-5.363307,2.390772,-6.047224,4.507264,-3.014695,0.897812,-8.175303,-2.430772,-2.554388,-2.138218,-5.487148,-8.269009,1.801716,3.886898,-9.044358,0.323600,-0.605365,5.943540], dtype = "float64")#candidate|4247|(108,)|const|float64
call_4244 = relay.TupleGetItem(func_3892_call(relay.reshape(var_4245.astype('bool'), [6, 12, 6]), relay.reshape(const_4246.astype('float64'), [224,]), relay.reshape(const_4247.astype('float64'), [108,]), ), 1)
call_4248 = relay.TupleGetItem(func_3897_call(relay.reshape(var_4245.astype('bool'), [6, 12, 6]), relay.reshape(const_4246.astype('float64'), [224,]), relay.reshape(const_4247.astype('float64'), [108,]), ), 1)
output = relay.Tuple([bop_4241,call_4244,var_4245,const_4246,const_4247,])
output2 = relay.Tuple([bop_4241,call_4248,var_4245,const_4246,const_4247,])
func_4249 = relay.Function([var_4239,var_4240,var_4245,], output)
mod['func_4249'] = func_4249
mod = relay.transform.InferType()(mod)
mutated_mod['func_4249'] = func_4249
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4249_call = mutated_mod.get_global_var('func_4249')
var_4251 = relay.var("var_4251", dtype = "float32", shape = ())#candidate|4251|()|var|float32
var_4252 = relay.var("var_4252", dtype = "float32", shape = (12, 11, 2))#candidate|4252|(12, 11, 2)|var|float32
var_4253 = relay.var("var_4253", dtype = "bool", shape = (432,))#candidate|4253|(432,)|var|bool
call_4250 = func_4249_call(var_4251,var_4252,var_4253,)
output = call_4250
func_4254 = relay.Function([var_4251,var_4252,var_4253,], output)
mutated_mod['func_4254'] = func_4254
mutated_mod = relay.transform.InferType()(mutated_mod)
func_506_call = mod.get_global_var('func_506')
func_507_call = mutated_mod.get_global_var('func_507')
call_4270 = func_506_call()
call_4271 = func_506_call()
output = call_4270
output2 = call_4271
func_4282 = relay.Function([], output)
mod['func_4282'] = func_4282
mod = relay.transform.InferType()(mod)
mutated_mod['func_4282'] = func_4282
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4282_call = mutated_mod.get_global_var('func_4282')
call_4283 = func_4282_call()
output = call_4283
func_4284 = relay.Function([], output)
mutated_mod['func_4284'] = func_4284
mutated_mod = relay.transform.InferType()(mutated_mod)
func_926_call = mod.get_global_var('func_926')
func_928_call = mutated_mod.get_global_var('func_928')
call_4364 = relay.TupleGetItem(func_926_call(), 0)
call_4365 = relay.TupleGetItem(func_928_call(), 0)
func_3892_call = mod.get_global_var('func_3892')
func_3897_call = mutated_mod.get_global_var('func_3897')
const_4380 = relay.const([True,True,False,False,True,True,True,False,False,False,True,True,False,True,False,False,True,True,False,False,True,True,True,False,True,False,True,False,True,True,True,False,False,True,False,True,True,False,True,True,False,True,False,True,False,False,True,True,False,True,True,True,False,False,True,False,False,False,False,True,True,False,True,True,True,False,True,False,False,False,True,False,True,True,True,True,False,False,False,False,True,True,True,False,True,True,False,True,True,False,False,True,False,False,False,False,False,True,False,False,False,False,False,True,True,False,True,True,False,True,True,False,True,True,False,False,False,False,False,True,False,False,False,True,False,True,True,False,False,True,False,False,True,True,False,True,True,True,False,True,False,False,True,True,True,True,False,True,True,False,False,False,False,True,True,True,False,False,True,False,True,False,True,True,True,True,False,False,False,False,True,False,False,True,False,True,False,False,False,False,False,True,False,False,False,True,True,False,True,True,False,False,True,True,True,False,False,True,False,False,False,True,True,False,False,True,False,True,True,False,True,True,True,True,True,True,False,True,True,True,False,False,True,True,True,True,True,False,False,True,False,False,False,True,True,True,False,True,False,True,True,True,False,True,False,False,False,False,True,False,True,True,False,False,False,True,True,True,True,False,False,False,False,False,True,True,True,False,False,True,True,False,False,False,True,False,False,True,False,True,True,True,False,True,False,False,True,True,True,False,True,True,False,False,True,False,True,True,False,False,False,True,False,True,True,True,True,True,False,False,False,False,True,False,True,True,False,False,True,True,True,False,False,True,False,False,True,False,True,True,False,True,True,False,False,False,True,False,False,True,False,False,True,True,True,True,True,True,True,False,True,False,False,True,False,True,True,True,True,False,True,True,False,False,True,False,False,False,False,False,True,False,True,True,False,False,False,True,True,True,True,False,False,True,False,False,False,True,True,True,False,False,False,False,False,True,False,True,True,True,True,True,True,False,False,True,False,False,False,False,True,True,False,True,True,False,True,True,False,True,True,False,True,True,False,False,True,False,True,False,True,False], dtype = "bool")#candidate|4380|(432,)|const|bool
var_4381 = relay.var("var_4381", dtype = "float64", shape = (224,))#candidate|4381|(224,)|var|float64
var_4382 = relay.var("var_4382", dtype = "float64", shape = (108,))#candidate|4382|(108,)|var|float64
call_4379 = relay.TupleGetItem(func_3892_call(relay.reshape(const_4380.astype('bool'), [6, 12, 6]), relay.reshape(var_4381.astype('float64'), [224,]), relay.reshape(var_4382.astype('float64'), [108,]), ), 0)
call_4383 = relay.TupleGetItem(func_3897_call(relay.reshape(const_4380.astype('bool'), [6, 12, 6]), relay.reshape(var_4381.astype('float64'), [224,]), relay.reshape(var_4382.astype('float64'), [108,]), ), 0)
output = relay.Tuple([call_4364,call_4379,const_4380,var_4381,var_4382,])
output2 = relay.Tuple([call_4365,call_4383,const_4380,var_4381,var_4382,])
func_4386 = relay.Function([var_4381,var_4382,], output)
mod['func_4386'] = func_4386
mod = relay.transform.InferType()(mod)
mutated_mod['func_4386'] = func_4386
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4386_call = mutated_mod.get_global_var('func_4386')
var_4388 = relay.var("var_4388", dtype = "float64", shape = (224,))#candidate|4388|(224,)|var|float64
var_4389 = relay.var("var_4389", dtype = "float64", shape = (108,))#candidate|4389|(108,)|var|float64
call_4387 = func_4386_call(var_4388,var_4389,)
output = call_4387
func_4390 = relay.Function([var_4388,var_4389,], output)
mutated_mod['func_4390'] = func_4390
mutated_mod = relay.transform.InferType()(mutated_mod)
func_119_call = mod.get_global_var('func_119')
func_121_call = mutated_mod.get_global_var('func_121')
call_4397 = relay.TupleGetItem(func_119_call(), 1)
call_4398 = relay.TupleGetItem(func_121_call(), 1)
func_2890_call = mod.get_global_var('func_2890')
func_2893_call = mutated_mod.get_global_var('func_2893')
call_4399 = relay.TupleGetItem(func_2890_call(relay.reshape(call_4397.astype('float32'), [9, 2, 2])), 0)
call_4400 = relay.TupleGetItem(func_2893_call(relay.reshape(call_4397.astype('float32'), [9, 2, 2])), 0)
func_953_call = mod.get_global_var('func_953')
func_954_call = mutated_mod.get_global_var('func_954')
call_4410 = func_953_call()
call_4411 = func_953_call()
func_2288_call = mod.get_global_var('func_2288')
func_2290_call = mutated_mod.get_global_var('func_2290')
call_4423 = relay.TupleGetItem(func_2288_call(), 2)
call_4424 = relay.TupleGetItem(func_2290_call(), 2)
bop_4427 = relay.subtract(call_4397.astype('int64'), relay.reshape(call_4399.astype('int64'), relay.shape_of(call_4397))) # shape=(6, 1, 6)
bop_4430 = relay.subtract(call_4398.astype('int64'), relay.reshape(call_4400.astype('int64'), relay.shape_of(call_4398))) # shape=(6, 1, 6)
func_4233_call = mod.get_global_var('func_4233')
func_4235_call = mutated_mod.get_global_var('func_4235')
call_4437 = relay.TupleGetItem(func_4233_call(relay.reshape(call_4410.astype('float64'), [162, 2])), 1)
call_4438 = relay.TupleGetItem(func_4235_call(relay.reshape(call_4410.astype('float64'), [162, 2])), 1)
bop_4442 = relay.floor_mod(bop_4427.astype('float64'), relay.reshape(call_4399.astype('float64'), relay.shape_of(bop_4427))) # shape=(6, 1, 6)
bop_4445 = relay.floor_mod(bop_4430.astype('float64'), relay.reshape(call_4400.astype('float64'), relay.shape_of(bop_4430))) # shape=(6, 1, 6)
output = relay.Tuple([call_4410,call_4423,call_4437,bop_4442,])
output2 = relay.Tuple([call_4411,call_4424,call_4438,bop_4445,])
func_4446 = relay.Function([], output)
mod['func_4446'] = func_4446
mod = relay.transform.InferType()(mod)
mutated_mod['func_4446'] = func_4446
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4446_call = mutated_mod.get_global_var('func_4446')
call_4447 = func_4446_call()
output = call_4447
func_4448 = relay.Function([], output)
mutated_mod['func_4448'] = func_4448
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3735_call = mod.get_global_var('func_3735')
func_3736_call = mutated_mod.get_global_var('func_3736')
call_4461 = relay.TupleGetItem(func_3735_call(), 1)
call_4462 = relay.TupleGetItem(func_3736_call(), 1)
func_2594_call = mod.get_global_var('func_2594')
func_2595_call = mutated_mod.get_global_var('func_2595')
call_4467 = func_2594_call()
call_4468 = func_2594_call()
output = relay.Tuple([call_4461,call_4467,])
output2 = relay.Tuple([call_4462,call_4468,])
func_4477 = relay.Function([], output)
mod['func_4477'] = func_4477
mod = relay.transform.InferType()(mod)
output = func_4477()
func_4478 = relay.Function([], output)
mutated_mod['func_4478'] = func_4478
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3634_call = mod.get_global_var('func_3634')
func_3635_call = mutated_mod.get_global_var('func_3635')
call_4487 = func_3634_call()
call_4488 = func_3634_call()
var_4509 = relay.var("var_4509", dtype = "float32", shape = (6, 4, 6))#candidate|4509|(6, 4, 6)|var|float32
bop_4510 = relay.logical_or(call_4487.astype('bool'), var_4509.astype('bool')) # shape=(6, 4, 6)
bop_4513 = relay.logical_or(call_4488.astype('bool'), var_4509.astype('bool')) # shape=(6, 4, 6)
output = relay.Tuple([bop_4510,])
output2 = relay.Tuple([bop_4513,])
func_4519 = relay.Function([var_4509,], output)
mod['func_4519'] = func_4519
mod = relay.transform.InferType()(mod)
var_4520 = relay.var("var_4520", dtype = "float32", shape = (6, 4, 6))#candidate|4520|(6, 4, 6)|var|float32
output = func_4519(var_4520)
func_4521 = relay.Function([var_4520], output)
mutated_mod['func_4521'] = func_4521
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4627 = relay.var("var_4627", dtype = "float64", shape = (3, 10, 8))#candidate|4627|(3, 10, 8)|var|float64
uop_4628 = relay.sqrt(var_4627.astype('float64')) # shape=(3, 10, 8)
output = relay.Tuple([uop_4628,])
output2 = relay.Tuple([uop_4628,])
func_4649 = relay.Function([var_4627,], output)
mod['func_4649'] = func_4649
mod = relay.transform.InferType()(mod)
var_4650 = relay.var("var_4650", dtype = "float64", shape = (3, 10, 8))#candidate|4650|(3, 10, 8)|var|float64
output = func_4649(var_4650)
func_4651 = relay.Function([var_4650], output)
mutated_mod['func_4651'] = func_4651
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1728_call = mod.get_global_var('func_1728')
func_1730_call = mutated_mod.get_global_var('func_1730')
call_4658 = relay.TupleGetItem(func_1728_call(), 0)
call_4659 = relay.TupleGetItem(func_1730_call(), 0)
output = relay.Tuple([call_4658,])
output2 = relay.Tuple([call_4659,])
func_4668 = relay.Function([], output)
mod['func_4668'] = func_4668
mod = relay.transform.InferType()(mod)
output = func_4668()
func_4669 = relay.Function([], output)
mutated_mod['func_4669'] = func_4669
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2994_call = mod.get_global_var('func_2994')
func_2996_call = mutated_mod.get_global_var('func_2996')
call_4670 = relay.TupleGetItem(func_2994_call(), 0)
call_4671 = relay.TupleGetItem(func_2996_call(), 0)
output = call_4670
output2 = call_4671
func_4691 = relay.Function([], output)
mod['func_4691'] = func_4691
mod = relay.transform.InferType()(mod)
mutated_mod['func_4691'] = func_4691
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4691_call = mutated_mod.get_global_var('func_4691')
call_4692 = func_4691_call()
output = call_4692
func_4693 = relay.Function([], output)
mutated_mod['func_4693'] = func_4693
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1889_call = mod.get_global_var('func_1889')
func_1890_call = mutated_mod.get_global_var('func_1890')
call_4746 = relay.TupleGetItem(func_1889_call(), 0)
call_4747 = relay.TupleGetItem(func_1890_call(), 0)
var_4749 = relay.var("var_4749", dtype = "float32", shape = (6, 11, 6))#candidate|4749|(6, 11, 6)|var|float32
bop_4750 = relay.add(call_4746.astype('float64'), var_4749.astype('float64')) # shape=(6, 11, 6)
bop_4753 = relay.add(call_4747.astype('float64'), var_4749.astype('float64')) # shape=(6, 11, 6)
output = bop_4750
output2 = bop_4753
func_4769 = relay.Function([var_4749,], output)
mod['func_4769'] = func_4769
mod = relay.transform.InferType()(mod)
mutated_mod['func_4769'] = func_4769
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4770 = relay.var("var_4770", dtype = "float32", shape = (6, 11, 6))#candidate|4770|(6, 11, 6)|var|float32
func_4769_call = mutated_mod.get_global_var('func_4769')
call_4771 = func_4769_call(var_4770)
output = call_4771
func_4772 = relay.Function([var_4770], output)
mutated_mod['func_4772'] = func_4772
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4477_call = mod.get_global_var('func_4477')
func_4478_call = mutated_mod.get_global_var('func_4478')
call_4780 = relay.TupleGetItem(func_4477_call(), 1)
call_4781 = relay.TupleGetItem(func_4478_call(), 1)
output = call_4780
output2 = call_4781
func_4786 = relay.Function([], output)
mod['func_4786'] = func_4786
mod = relay.transform.InferType()(mod)
mutated_mod['func_4786'] = func_4786
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4786_call = mutated_mod.get_global_var('func_4786')
call_4787 = func_4786_call()
output = call_4787
func_4788 = relay.Function([], output)
mutated_mod['func_4788'] = func_4788
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4796 = relay.const([[[9.763809,-6.655257,-3.800551,8.420039,-3.481637,-6.378995,4.979112,-3.775529,8.843253,2.394120,-8.504548,6.766427],[-1.980369,3.934351,4.753615,7.032631,-3.619941,6.197871,-6.316031,5.287410,-1.716754,-6.550651,-0.669310,7.785743],[3.225175,-3.050228,-5.780076,-7.008137,-8.883890,7.758650,-5.698156,-3.200404,2.730929,4.318341,-6.755745,-2.086830],[-7.222902,-6.854995,5.494264,-2.467487,5.487727,-9.562172,-6.863913,-4.361112,-7.362337,-7.642255,4.403842,7.831003],[8.292258,-4.355102,1.787551,-2.582449,0.305358,-9.715001,-6.754702,-0.728515,3.753569,-8.703689,6.374976,-3.600182],[-8.420393,-1.937445,-5.490853,-4.227934,-7.130031,0.159699,6.609179,5.097693,0.479288,7.054347,-7.048117,4.924523],[-3.436846,4.688549,-1.306052,0.972146,-0.551130,-6.795972,5.377527,-6.984163,-8.426299,-5.756414,2.344253,-3.713577],[5.010991,5.657413,2.512312,-0.006867,-2.129185,0.011974,4.933477,5.977175,-3.371384,-8.770662,3.252667,9.010870],[2.215705,9.551316,6.956973,5.393807,-8.752786,-6.828780,5.183104,7.103462,-8.061517,-6.352900,-5.681439,-8.233374],[-7.671535,-0.798060,0.759244,9.776290,5.220123,-6.658443,-5.123017,-4.355999,-5.916820,7.044036,7.860310,5.142625],[1.217808,4.024716,8.622721,3.091714,3.278154,9.915305,5.821964,8.474583,-6.893082,-1.834924,5.725418,8.140761]],[[7.124041,5.517726,3.948274,5.538741,-1.714459,-0.428264,-9.850777,6.224393,-0.552025,-6.013687,7.285080,-0.516897],[4.663594,0.849916,3.931367,-2.171714,9.969356,0.765262,-0.779174,6.919531,-9.333787,4.721532,8.586657,-1.982954],[3.343832,-2.638884,-1.142761,-0.263447,6.711373,-7.191176,-7.334210,6.847851,-1.521224,9.779915,9.009858,8.613310],[-2.005591,-0.599705,-5.051555,8.682449,-4.542066,-1.417148,4.087013,-8.401949,-0.326308,5.427830,-1.293053,-3.843512],[-5.980921,5.672747,7.472899,5.531823,4.480477,8.376346,-7.186301,-8.845484,-0.532350,5.376486,8.529091,-6.864960],[-0.506159,7.347636,4.993422,2.136809,3.922822,0.890943,0.126456,-7.893830,2.348966,-1.089802,3.352293,-3.645198],[-5.023571,1.546694,1.992810,6.410448,5.220792,-7.646244,9.621296,-8.681276,5.852758,8.552886,-0.547487,3.460433],[3.606684,2.442614,-8.676057,1.080951,8.077179,4.584793,-2.038870,-2.286140,4.434314,-2.925213,-2.455960,1.337237],[8.584262,7.650363,-9.249285,1.639015,-8.926239,-9.330605,-9.741867,6.359280,-4.874013,-6.504287,-4.934768,7.208213],[-3.449425,-8.157531,-6.925272,-5.392480,-1.025713,-6.874712,-7.363554,-5.265415,-5.809105,-1.573035,-3.805916,8.132366],[-5.565042,-5.300833,-6.095095,-8.657181,5.856493,-5.940870,-9.298225,7.780798,-1.949294,7.271563,7.424565,0.961450]],[[8.440218,-9.076677,-7.967452,-6.429657,-2.770130,3.620670,-6.228478,3.690842,-3.403686,-9.191771,-1.227331,8.234864],[3.317574,2.796137,-0.858595,-9.489007,-0.532591,-1.154429,-2.098435,6.301815,2.054496,-3.153263,-4.679468,7.476632],[0.394394,7.852469,-9.095564,-1.235433,-2.043506,-3.652427,-0.915614,-1.228043,-8.170600,7.332469,4.730432,5.302271],[9.927901,3.593259,0.224920,-8.169806,-2.824291,-1.853721,-5.934656,-9.925503,-3.815815,-2.041780,8.557973,-8.630429],[2.890073,5.664551,-3.000928,3.831815,-4.595593,-2.370673,9.058963,-9.262078,-1.901282,-8.782964,9.971884,2.242463],[-2.079196,-3.107486,-1.687739,0.799074,7.822319,6.382123,7.210365,5.332334,1.446789,5.383170,7.313568,-6.021081],[-0.268518,-7.894638,7.475369,8.416530,5.412621,9.670019,-1.121975,8.758941,9.572178,-2.716692,4.593700,-5.069731],[0.799596,-7.420152,5.369157,-3.917243,9.387294,1.112360,7.675683,-7.798978,0.067556,-7.018613,-4.833134,5.396338],[-0.276509,-6.295492,6.740625,-8.502984,-0.437480,7.359758,6.340990,3.668010,3.998224,0.774344,-1.481097,4.715849],[-6.984498,0.042911,-3.880679,-7.185538,-2.184911,-1.229650,-4.436913,-9.004283,4.401113,-1.880815,-8.807069,-4.046850],[5.238816,-7.893977,7.929492,6.762836,6.157651,8.732200,3.083192,6.121837,-0.135619,5.142611,-2.363130,-3.115301]],[[-7.523681,5.075659,-4.329378,-6.175613,6.903351,1.714586,-9.998249,-2.032763,-8.905533,1.485802,-4.370471,3.678353],[2.279252,4.696113,2.977651,7.127981,-2.217128,-5.905780,-0.535756,-8.186051,8.733139,7.498380,-6.681797,6.422935],[9.178870,-8.352179,9.112149,-1.916062,6.511673,9.125907,9.009742,-9.530970,4.474303,8.676067,5.525385,7.615137],[5.802121,-4.881073,2.331014,-6.766343,8.044726,-7.583591,7.442446,4.375465,-7.436203,5.983521,5.917268,9.081481],[-0.881302,9.339024,8.701682,-0.444545,9.370720,-6.268077,-1.293897,4.991120,-3.593345,9.108894,-2.541886,-1.383901],[4.734917,5.250146,3.545826,0.070549,2.879274,4.514790,9.429471,1.498891,-0.255194,5.203835,1.636487,-4.641197],[-0.449655,7.538238,-2.610825,5.842668,4.310022,3.164687,-5.413628,-8.963119,1.002454,-5.618580,4.910631,4.571242],[4.146678,-2.270441,1.044844,-7.670427,-1.803281,-7.995042,1.157110,-2.744254,-6.283040,0.190531,-1.548676,-6.133533],[0.964767,5.255827,0.058995,6.969943,0.140736,7.437285,-7.303960,7.402834,0.449601,-8.111293,9.252884,7.735226],[-1.576303,-2.534567,-6.199478,-0.384486,9.058906,-6.259709,-7.486493,-6.015667,3.013740,-7.863901,3.289296,7.078932],[2.477430,-3.133763,-5.106450,9.130875,-9.503640,-3.146828,-5.721879,3.359392,-2.406106,-4.957320,8.352348,-7.885330]],[[-9.819018,-4.561207,-3.278231,-7.857853,7.520281,3.309319,-6.329667,-0.276839,-4.273361,8.166875,7.078163,5.852249],[-1.151224,-5.948190,-8.538153,8.791127,5.060505,-1.274526,4.886016,-1.729588,7.796708,-3.516376,-3.966871,7.039612],[2.635686,9.195625,1.135178,-2.861875,0.735783,1.439940,-6.848484,-1.177473,-5.530044,4.971824,-0.315854,7.904088],[6.506095,4.979511,-2.433222,2.823461,-2.055772,8.838490,3.909176,0.172845,-5.032145,-0.933179,0.072465,1.192064],[7.925518,7.542300,-1.348686,-6.226181,0.543954,6.913542,-1.775586,2.128937,4.132850,-8.830452,5.552879,4.343518],[-0.469763,-5.886705,1.134617,3.807085,-5.675260,-5.269677,2.569743,1.093962,-5.730148,4.083996,7.935105,6.818891],[2.681431,6.979793,-7.599305,-0.994926,-8.128310,-6.626173,-3.995117,-6.094454,5.481371,9.908688,9.145742,0.542211],[0.520479,-6.522138,6.803234,-7.900364,0.239691,5.951126,-2.853954,-2.679651,-1.441115,-2.936273,1.504541,-3.370403],[1.887873,5.245400,-2.674181,6.688609,9.742203,-4.690523,2.726479,4.432124,-0.782390,-2.421353,2.670555,1.020283],[-3.840356,-3.127900,-9.049072,-3.772568,9.290093,4.030528,-3.848932,6.811873,-8.628101,-8.662133,-5.907029,0.627020],[8.713303,-3.944606,-2.786490,-6.545335,0.838531,-6.971739,1.511092,-1.029841,4.957615,-9.107386,-1.105793,5.180182]]], dtype = "float64")#candidate|4796|(5, 11, 12)|const|float64
uop_4797 = relay.erf(const_4796.astype('float64')) # shape=(5, 11, 12)
uop_4804 = relay.atan(uop_4797.astype('float32')) # shape=(5, 11, 12)
output = uop_4804
output2 = uop_4804
func_4807 = relay.Function([], output)
mod['func_4807'] = func_4807
mod = relay.transform.InferType()(mod)
output = func_4807()
func_4808 = relay.Function([], output)
mutated_mod['func_4808'] = func_4808
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3263_call = mod.get_global_var('func_3263')
func_3264_call = mutated_mod.get_global_var('func_3264')
call_4817 = func_3263_call()
call_4818 = func_3263_call()
output = relay.Tuple([call_4817,])
output2 = relay.Tuple([call_4818,])
func_4819 = relay.Function([], output)
mod['func_4819'] = func_4819
mod = relay.transform.InferType()(mod)
output = func_4819()
func_4820 = relay.Function([], output)
mutated_mod['func_4820'] = func_4820
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1197_call = mod.get_global_var('func_1197')
func_1198_call = mutated_mod.get_global_var('func_1198')
call_4911 = relay.TupleGetItem(func_1197_call(), 0)
call_4912 = relay.TupleGetItem(func_1198_call(), 0)
output = relay.Tuple([call_4911,])
output2 = relay.Tuple([call_4912,])
func_4923 = relay.Function([], output)
mod['func_4923'] = func_4923
mod = relay.transform.InferType()(mod)
mutated_mod['func_4923'] = func_4923
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4923_call = mutated_mod.get_global_var('func_4923')
call_4924 = func_4923_call()
output = call_4924
func_4925 = relay.Function([], output)
mutated_mod['func_4925'] = func_4925
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1964_call = mod.get_global_var('func_1964')
func_1966_call = mutated_mod.get_global_var('func_1966')
call_4948 = relay.TupleGetItem(func_1964_call(), 0)
call_4949 = relay.TupleGetItem(func_1966_call(), 0)
func_2629_call = mod.get_global_var('func_2629')
func_2631_call = mutated_mod.get_global_var('func_2631')
call_4956 = relay.TupleGetItem(func_2629_call(), 0)
call_4957 = relay.TupleGetItem(func_2631_call(), 0)
output = relay.Tuple([call_4948,call_4956,])
output2 = relay.Tuple([call_4949,call_4957,])
func_4959 = relay.Function([], output)
mod['func_4959'] = func_4959
mod = relay.transform.InferType()(mod)
output = func_4959()
func_4960 = relay.Function([], output)
mutated_mod['func_4960'] = func_4960
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1889_call = mod.get_global_var('func_1889')
func_1890_call = mutated_mod.get_global_var('func_1890')
call_4966 = relay.TupleGetItem(func_1889_call(), 0)
call_4967 = relay.TupleGetItem(func_1890_call(), 0)
output = relay.Tuple([call_4966,])
output2 = relay.Tuple([call_4967,])
func_4977 = relay.Function([], output)
mod['func_4977'] = func_4977
mod = relay.transform.InferType()(mod)
output = func_4977()
func_4978 = relay.Function([], output)
mutated_mod['func_4978'] = func_4978
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3775_call = mod.get_global_var('func_3775')
func_3777_call = mutated_mod.get_global_var('func_3777')
call_5054 = func_3775_call()
call_5055 = func_3775_call()
output = call_5054
output2 = call_5055
func_5056 = relay.Function([], output)
mod['func_5056'] = func_5056
mod = relay.transform.InferType()(mod)
mutated_mod['func_5056'] = func_5056
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5056_call = mutated_mod.get_global_var('func_5056')
call_5057 = func_5056_call()
output = call_5057
func_5058 = relay.Function([], output)
mutated_mod['func_5058'] = func_5058
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5095 = relay.const([[[2,3,-7,-4,10,-10,2,6,2,9],[-10,4,8,-8,-5,-4,-8,-9,-9,1],[-8,4,2,8,-6,4,5,-1,-3,7],[-1,7,9,4,6,-9,8,-4,3,-6],[8,-4,-10,-7,6,-1,6,-6,-3,-3],[8,5,5,-8,-3,7,6,8,6,9],[1,9,-9,10,-5,-2,5,1,-9,8],[5,7,9,-7,1,7,5,7,10,7],[10,-10,-9,7,-2,-3,-4,-6,4,-8],[-9,-6,10,10,1,-3,1,8,-4,9],[3,1,-2,8,2,10,-10,8,10,-8],[-7,3,-4,-9,7,-4,-2,6,6,10],[2,1,-6,10,7,6,8,-4,-2,3]],[[-3,-10,4,10,3,-9,-10,5,-7,4],[2,10,1,4,-10,-3,-4,9,10,-9],[9,-8,-8,7,-9,-1,-2,10,-6,-7],[1,-9,-4,2,-8,-8,1,-6,-10,-4],[7,-9,4,-2,-4,-7,10,10,6,7],[5,1,-1,4,-3,10,2,8,-9,-8],[-9,9,-3,-3,-3,3,6,-5,-2,-8],[-7,-4,8,-7,-10,9,2,-1,9,5],[2,3,3,-7,-8,9,-5,-4,-5,-9],[6,6,-8,-4,-9,-10,-7,9,2,7],[10,5,1,8,2,10,-5,-7,-1,9],[-8,-1,1,-8,-5,-1,3,2,-9,9],[-8,-1,-5,-6,-7,-6,-4,-1,8,-6]],[[-4,-2,4,2,-4,7,2,-7,-4,3],[7,-6,10,-4,9,-1,-6,4,7,-5],[7,-5,8,5,-4,-3,2,10,1,10],[1,-4,4,-8,4,-6,-3,-9,2,5],[6,6,9,2,9,9,3,8,-1,-10],[2,-5,6,8,-10,7,10,6,9,-9],[-9,-2,-2,-10,9,-8,-8,5,-9,-6],[-5,6,6,7,1,-6,4,1,-8,-3],[-4,7,-5,8,5,-10,-6,-8,-10,10],[10,-10,-3,2,-5,-10,5,-3,-10,-2],[-6,7,-1,-4,9,2,9,-6,4,-6],[3,8,-5,-10,-1,-2,-7,8,-6,-10],[-6,8,4,-10,2,-5,-3,-4,-3,3]],[[-9,8,-6,7,-1,-10,-9,4,10,2],[-1,-8,-2,-1,9,9,-9,-3,5,8],[8,3,-6,-3,-1,10,-5,-4,-3,4],[-9,9,1,-4,3,-2,-9,8,-2,-4],[9,-6,-4,-1,-7,10,-9,-7,-2,-7],[-2,8,6,9,-9,2,10,-2,2,3],[8,7,-4,-8,-5,3,-3,-9,7,8],[4,3,10,8,1,-1,-5,-8,5,5],[-10,5,9,4,-5,-1,-4,3,-2,-6],[-2,-3,7,8,-5,10,-3,-1,-3,8],[9,9,6,7,-2,-2,-2,-5,-6,1],[-8,-9,9,3,6,2,-3,-9,10,10],[9,-8,8,-7,8,6,-10,9,6,1]],[[-5,9,3,-6,2,-7,-7,1,8,-10],[8,4,-2,9,-7,1,-5,-10,6,1],[4,-10,-3,-6,9,-9,3,-6,6,-2],[8,-3,-2,9,-10,10,8,-5,-1,2],[-9,8,4,-7,-1,-1,2,2,-8,-4],[3,2,-3,2,8,-7,-5,-8,-1,9],[-4,1,-6,-10,3,-3,-9,8,10,10],[-4,-4,2,-7,-7,-4,-7,-6,7,-7],[1,7,-5,-6,4,6,10,4,1,4],[-8,-8,-1,-7,-2,9,6,-5,-2,9],[-6,-2,4,10,-9,-5,1,3,-10,2],[-5,-5,-8,2,-3,6,4,8,7,-3],[-10,-5,-2,5,-9,3,-8,4,1,8]]], dtype = "int32")#candidate|5095|(5, 13, 10)|const|int32
var_5096 = relay.var("var_5096", dtype = "int32", shape = (5, 13, 10))#candidate|5096|(5, 13, 10)|var|int32
bop_5097 = relay.logical_xor(const_5095.astype('int32'), relay.reshape(var_5096.astype('int32'), relay.shape_of(const_5095))) # shape=(5, 13, 10)
uop_5102 = relay.sinh(const_5095.astype('float64')) # shape=(5, 13, 10)
func_4819_call = mod.get_global_var('func_4819')
func_4820_call = mutated_mod.get_global_var('func_4820')
call_5115 = relay.TupleGetItem(func_4819_call(), 0)
call_5116 = relay.TupleGetItem(func_4820_call(), 0)
output = relay.Tuple([bop_5097,uop_5102,call_5115,])
output2 = relay.Tuple([bop_5097,uop_5102,call_5116,])
func_5123 = relay.Function([var_5096,], output)
mod['func_5123'] = func_5123
mod = relay.transform.InferType()(mod)
var_5124 = relay.var("var_5124", dtype = "int32", shape = (5, 13, 10))#candidate|5124|(5, 13, 10)|var|int32
output = func_5123(var_5124)
func_5125 = relay.Function([var_5124], output)
mutated_mod['func_5125'] = func_5125
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1947_call = mod.get_global_var('func_1947')
func_1948_call = mutated_mod.get_global_var('func_1948')
call_5235 = relay.TupleGetItem(func_1947_call(), 1)
call_5236 = relay.TupleGetItem(func_1948_call(), 1)
func_3819_call = mod.get_global_var('func_3819')
func_3821_call = mutated_mod.get_global_var('func_3821')
call_5258 = relay.TupleGetItem(func_3819_call(), 0)
call_5259 = relay.TupleGetItem(func_3821_call(), 0)
func_3277_call = mod.get_global_var('func_3277')
func_3278_call = mutated_mod.get_global_var('func_3278')
call_5263 = func_3277_call()
call_5264 = func_3277_call()
uop_5276 = relay.acos(call_5258.astype('float32')) # shape=(5, 7, 13)
uop_5278 = relay.acos(call_5259.astype('float32')) # shape=(5, 7, 13)
output = relay.Tuple([call_5235,call_5263,uop_5276,])
output2 = relay.Tuple([call_5236,call_5264,uop_5278,])
func_5279 = relay.Function([], output)
mod['func_5279'] = func_5279
mod = relay.transform.InferType()(mod)
output = func_5279()
func_5280 = relay.Function([], output)
mutated_mod['func_5280'] = func_5280
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4819_call = mod.get_global_var('func_4819')
func_4820_call = mutated_mod.get_global_var('func_4820')
call_5283 = relay.TupleGetItem(func_4819_call(), 0)
call_5284 = relay.TupleGetItem(func_4820_call(), 0)
output = relay.Tuple([call_5283,])
output2 = relay.Tuple([call_5284,])
func_5290 = relay.Function([], output)
mod['func_5290'] = func_5290
mod = relay.transform.InferType()(mod)
mutated_mod['func_5290'] = func_5290
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5290_call = mutated_mod.get_global_var('func_5290')
call_5291 = func_5290_call()
output = call_5291
func_5292 = relay.Function([], output)
mutated_mod['func_5292'] = func_5292
mutated_mod = relay.transform.InferType()(mutated_mod)
func_561_call = mod.get_global_var('func_561')
func_562_call = mutated_mod.get_global_var('func_562')
call_5398 = relay.TupleGetItem(func_561_call(), 0)
call_5399 = relay.TupleGetItem(func_562_call(), 0)
output = call_5398
output2 = call_5399
func_5402 = relay.Function([], output)
mod['func_5402'] = func_5402
mod = relay.transform.InferType()(mod)
output = func_5402()
func_5403 = relay.Function([], output)
mutated_mod['func_5403'] = func_5403
mutated_mod = relay.transform.InferType()(mutated_mod)
func_276_call = mod.get_global_var('func_276')
func_278_call = mutated_mod.get_global_var('func_278')
call_5424 = func_276_call()
call_5425 = func_276_call()
const_5426 = relay.const([[[4.512977,-1.182026,3.267410,7.309336,4.961178,0.128040],[8.776926,-3.265416,2.796587,4.026359,-9.967369,4.874538],[9.673650,-5.758205,-6.446639,-5.045284,5.134212,1.892604],[-7.164314,3.752436,-4.597580,0.965257,-4.143709,-4.671444],[-2.691266,7.680027,-1.046418,3.516674,-6.890651,-4.739290],[6.536548,1.046229,-8.643254,7.706843,5.671022,-3.883595],[2.713318,7.050981,8.862856,6.202222,5.764048,-7.905570],[5.296673,-8.191967,8.529675,6.117256,2.876399,-3.577756],[3.209547,-8.347926,-3.908278,-6.212588,0.214518,7.661121],[6.982909,-8.006947,5.027690,1.041221,-3.759540,4.648425],[-2.958132,-8.210118,6.642204,4.340877,-3.697526,4.593778],[-6.693199,-4.582277,1.740159,5.041441,5.448376,-7.946914],[-9.706061,6.778219,2.046594,3.652402,5.792068,8.811930],[-2.077929,6.974489,-8.753968,4.560153,8.358228,-0.470047],[-1.109931,2.974312,-1.296826,-4.059551,9.513403,5.431323]],[[-6.213155,2.502935,6.796457,-9.204716,8.735886,-5.752514],[-7.235478,5.901161,-3.094752,5.722082,8.549300,-1.495549],[-7.067635,-0.385438,-0.874323,-6.001785,-2.844238,3.331466],[-7.414686,6.458341,3.187413,5.436616,-7.638068,1.339916],[4.208952,2.327822,-3.622787,-9.904419,-3.354249,-9.774802],[-2.369179,-4.943422,-6.525588,-3.328556,9.645087,0.667937],[-7.436097,1.852332,9.339813,9.571322,9.793130,4.411404],[-9.692612,-5.236069,-9.053894,6.708733,4.651901,-0.200589],[2.787673,-6.046591,-5.949763,-5.616012,-4.177092,8.592998],[-2.178505,-3.040622,3.905367,3.775925,9.599391,4.289513],[8.889213,7.993498,-0.219549,-4.845423,-9.595168,-5.487931],[-0.940026,0.888241,-5.755601,-2.181215,6.879308,-8.260738],[-8.848677,-5.576024,5.045658,-3.249956,9.534384,0.813194],[0.469543,4.228610,-8.685239,-8.580878,-1.674369,-2.339159],[9.455427,-8.606737,6.724689,6.712383,-4.557842,-4.394167]],[[1.095008,-7.119600,-4.766175,-6.299946,-2.100756,3.944718],[-8.070398,9.726622,-3.940980,9.954768,1.281316,-3.713901],[1.488340,-4.772368,-0.989358,7.926397,0.923524,-7.354317],[-9.035639,5.702183,-3.993723,8.891740,9.870308,-6.362005],[-0.853820,2.038022,0.254368,0.323811,3.675814,-1.888922],[-5.744944,-6.288805,-6.833332,0.204631,9.021549,2.552082],[6.295700,-3.914417,8.760415,-9.763623,1.740665,6.546177],[-9.943421,0.151777,7.723173,4.893556,3.295707,6.481403],[-9.490814,-4.764175,-6.062144,2.376445,1.605124,-8.246706],[-9.905404,-2.601096,-2.134555,-4.376099,-4.730074,-1.845328],[-6.159359,9.777069,8.555549,3.162597,8.921512,-9.206939],[8.200303,-4.160604,3.841527,1.467832,2.986814,2.578083],[-8.916352,-4.595036,1.504159,-4.499113,-3.275870,-6.532762],[-6.143102,9.295712,6.221044,3.591601,-6.167560,9.459301],[-1.555912,0.574782,4.887500,4.803677,9.339602,-7.339211]],[[1.868597,-3.281093,3.025327,4.515169,-9.083490,2.861394],[-2.214801,-8.509503,-8.444666,3.924561,-5.413487,5.487883],[6.308592,2.836414,-7.168792,-3.147663,-4.972909,-7.165233],[6.457787,-3.138467,-4.089286,2.897740,-7.558205,5.141252],[-1.194267,-3.475462,-9.474257,-9.360738,-4.864968,-4.701113],[5.014738,-6.197545,1.398850,2.144617,1.437754,-0.118726],[-3.483115,-7.188193,5.975244,3.317424,-9.252500,-6.424704],[6.635482,6.142869,4.957366,4.297802,-0.263841,-1.157538],[-0.822947,-5.908614,9.870977,9.120063,-4.681897,7.844316],[-5.313414,1.279389,-2.443842,9.679711,-3.672155,8.051782],[-4.424264,4.757283,4.748408,-8.747960,2.832590,2.931904],[8.779534,-2.631840,-5.093670,4.811542,4.193735,-7.214728],[-0.986283,5.588604,-8.868701,-1.945570,1.295012,6.281607],[-8.595737,-1.033569,-5.892897,-7.771078,6.772753,4.135413],[-2.370574,-4.159971,-8.987835,2.248867,-1.797218,5.524042]],[[-9.931479,7.714602,7.438892,-3.319189,-2.281786,-7.304388],[-1.940071,-0.306895,6.906762,2.449725,-3.166717,4.500219],[-3.810291,3.182442,-4.466952,8.162982,3.444635,-2.082298],[4.067960,-2.999736,-2.767163,-6.605657,4.076291,-8.227530],[2.574574,7.413707,6.806637,-0.280211,7.936779,-1.869098],[-5.879454,-7.652992,-8.417975,4.036846,6.676463,4.265554],[-5.255787,-7.526501,-9.009211,-4.265294,8.749500,5.200606],[7.548735,-2.128660,5.849648,-1.449268,4.645098,7.660098],[9.554885,0.447675,-1.018695,-2.563386,6.392745,3.716493],[1.646397,5.485026,8.127088,9.468211,-1.669705,8.438231],[-5.058651,8.406736,8.833766,1.700289,7.144781,1.150690],[9.253777,-5.471700,3.496511,-1.366892,-2.338225,7.076767],[-5.338412,-7.365571,-7.184118,2.103481,6.596755,-8.304787],[7.496999,6.239079,5.446906,8.871845,2.804630,9.702828],[1.650156,3.699281,6.456999,9.273391,-6.861036,-7.105876]],[[3.978009,6.434697,-5.855930,2.283336,-8.760107,1.807996],[-6.989279,-5.504786,-2.222035,-9.402861,-1.041463,7.674850],[-9.029556,5.164792,-6.187256,4.745396,0.732718,-3.960887],[7.061980,-6.856593,8.851179,1.758567,-8.162231,6.742318],[2.494313,-7.412318,6.852853,9.314448,-5.001552,-6.091006],[-1.351877,-2.105946,4.711641,3.537242,6.336745,-2.998493],[8.672210,-1.736762,5.309718,6.704901,0.559567,-5.701161],[8.999017,-7.473293,1.910946,0.395887,-5.881510,5.064591],[-0.620873,-2.322784,-7.991667,-2.471129,-5.430110,3.354869],[-4.165701,-3.788911,-9.777005,2.136290,-6.032009,4.061168],[-6.262950,1.588364,4.677120,-2.555656,-3.105719,4.383593],[1.112507,-9.245327,-6.495081,-2.404141,-6.017262,-1.812538],[5.969444,0.904477,8.398097,2.897496,3.282816,-7.723451],[-5.413772,-8.269403,-0.651514,1.200315,-0.361604,3.868098],[-5.813497,4.203385,4.660441,7.009137,0.016372,-5.925844]]], dtype = "float64")#candidate|5426|(6, 15, 6)|const|float64
bop_5427 = relay.subtract(call_5424.astype('uint64'), const_5426.astype('uint64')) # shape=(6, 15, 6)
bop_5430 = relay.subtract(call_5425.astype('uint64'), const_5426.astype('uint64')) # shape=(6, 15, 6)
func_649_call = mod.get_global_var('func_649')
func_651_call = mutated_mod.get_global_var('func_651')
var_5437 = relay.var("var_5437", dtype = "uint64", shape = (175,))#candidate|5437|(175,)|var|uint64
call_5436 = relay.TupleGetItem(func_649_call(relay.reshape(var_5437.astype('uint64'), [5, 5, 7])), 0)
call_5438 = relay.TupleGetItem(func_651_call(relay.reshape(var_5437.astype('uint64'), [5, 5, 7])), 0)
uop_5452 = relay.atanh(const_5426.astype('float32')) # shape=(6, 15, 6)
output = relay.Tuple([bop_5427,call_5436,var_5437,uop_5452,])
output2 = relay.Tuple([bop_5430,call_5438,var_5437,uop_5452,])
func_5459 = relay.Function([var_5437,], output)
mod['func_5459'] = func_5459
mod = relay.transform.InferType()(mod)
mutated_mod['func_5459'] = func_5459
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5460 = relay.var("var_5460", dtype = "uint64", shape = (175,))#candidate|5460|(175,)|var|uint64
func_5459_call = mutated_mod.get_global_var('func_5459')
call_5461 = func_5459_call(var_5460)
output = call_5461
func_5462 = relay.Function([var_5460], output)
mutated_mod['func_5462'] = func_5462
mutated_mod = relay.transform.InferType()(mutated_mod)
func_747_call = mod.get_global_var('func_747')
func_748_call = mutated_mod.get_global_var('func_748')
call_5490 = relay.TupleGetItem(func_747_call(), 0)
call_5491 = relay.TupleGetItem(func_748_call(), 0)
func_731_call = mod.get_global_var('func_731')
func_732_call = mutated_mod.get_global_var('func_732')
call_5492 = func_731_call()
call_5493 = func_731_call()
bop_5498 = relay.bitwise_or(call_5492.astype('uint8'), call_5490.astype('uint8')) # shape=(6, 8, 6)
bop_5501 = relay.bitwise_or(call_5493.astype('uint8'), call_5491.astype('uint8')) # shape=(6, 8, 6)
output = bop_5498
output2 = bop_5501
func_5502 = relay.Function([], output)
mod['func_5502'] = func_5502
mod = relay.transform.InferType()(mod)
mutated_mod['func_5502'] = func_5502
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5502_call = mutated_mod.get_global_var('func_5502')
call_5503 = func_5502_call()
output = call_5503
func_5504 = relay.Function([], output)
mutated_mod['func_5504'] = func_5504
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2356_call = mod.get_global_var('func_2356')
func_2357_call = mutated_mod.get_global_var('func_2357')
call_5548 = relay.TupleGetItem(func_2356_call(), 0)
call_5549 = relay.TupleGetItem(func_2357_call(), 0)
const_5550 = relay.const([[[-5.402478,0.861983,-9.842008,-9.325373,1.880661,2.871861],[6.897536,0.581768,-3.871445,-0.523178,-0.928888,7.310888],[-3.530578,8.977497,3.814489,-6.658902,-7.689584,3.417956],[-8.923480,-7.733038,1.214819,-8.233370,-9.178418,6.489453],[2.975966,7.433212,5.191949,3.919602,-3.296338,2.081619]],[[-6.044553,-7.222601,-2.151220,8.300224,5.094519,-0.458792],[5.185376,7.881360,8.587451,-2.737615,-1.583511,-3.877927],[-4.206739,5.457327,8.171649,-7.343817,-9.243100,-3.144997],[-4.369188,-8.558827,2.012577,-4.161447,4.065338,1.187297],[6.865044,6.819584,8.444852,9.788615,-6.555111,7.485613]],[[0.493654,6.431377,-3.196676,-2.361584,5.944262,-7.812902],[-8.814410,4.321337,3.775525,-3.555300,-0.280435,-6.559263],[4.187102,4.341745,3.411718,9.972040,-1.386724,-4.856413],[-1.269465,-2.613999,2.642588,5.037473,9.129208,7.639102],[3.012521,0.466002,-7.965667,6.813136,5.029091,7.072528]],[[7.858739,-6.754643,5.776094,-7.770463,5.749697,7.146490],[-5.771110,-5.080882,7.282157,-3.033884,3.042891,-2.476239],[4.279689,-6.951298,-2.888895,2.324966,-4.175746,1.617408],[3.563810,-9.915532,-7.123504,3.663347,-1.553907,7.989869],[-9.330317,-8.231600,3.909830,4.092024,-6.227177,-4.084201]],[[3.326253,4.186152,8.782429,8.414054,-0.121293,4.265321],[6.794762,1.454587,6.548616,2.889900,-3.581969,8.765323],[-2.499166,2.097990,-1.649038,9.822535,0.399892,-3.013710],[6.989872,4.283821,7.619973,9.595657,-0.363054,-4.267524],[0.686623,3.312651,5.956395,7.601623,2.551860,-4.625191]],[[-5.112862,9.706355,-2.906946,-2.671970,4.719244,-2.666242],[0.822248,3.946205,-5.883039,0.395456,1.449872,-5.702787],[8.560602,-6.415893,-8.105737,0.868863,-0.693973,-2.914566],[-5.667800,-5.141955,7.397109,-3.595243,-7.753068,-3.964259],[4.485184,-1.104538,-7.998783,0.297663,9.337176,-0.089334]]], dtype = "float64")#candidate|5550|(6, 5, 6)|const|float64
bop_5551 = relay.bitwise_and(call_5548.astype('uint16'), const_5550.astype('uint16')) # shape=(6, 5, 6)
bop_5554 = relay.bitwise_and(call_5549.astype('uint16'), const_5550.astype('uint16')) # shape=(6, 5, 6)
output = relay.Tuple([bop_5551,])
output2 = relay.Tuple([bop_5554,])
func_5555 = relay.Function([], output)
mod['func_5555'] = func_5555
mod = relay.transform.InferType()(mod)
output = func_5555()
func_5556 = relay.Function([], output)
mutated_mod['func_5556'] = func_5556
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5596 = relay.var("var_5596", dtype = "float32", shape = (2, 1, 15))#candidate|5596|(2, 1, 15)|var|float32
const_5597 = relay.const([[[4.913225,7.251735,6.702068,5.350995,3.928403,-5.491776,-9.139176,-8.817351,2.500058,6.166967,6.702935,3.677125,-3.565093,-4.084806,-8.470016],[2.029681,-0.014982,-2.568449,-4.658878,-8.495430,-0.914982,9.040023,8.318094,-9.588484,-4.093368,-9.949246,-4.145563,1.326871,8.634810,3.377345],[5.863084,-6.078239,0.719305,-4.678593,-2.857695,0.093041,3.525805,-5.708621,-0.042009,6.109746,-7.916850,0.578950,9.337091,3.698069,-7.715659],[1.316755,-4.918529,8.715228,-8.931895,3.434354,-5.180574,-1.117801,6.360568,-3.921608,5.786504,-9.814181,-7.277644,-9.309291,-9.478050,-9.291417],[-7.738435,1.205684,2.541298,-6.375746,-0.178766,5.604000,-6.439825,-9.456657,-2.302559,-8.215182,4.966052,9.125798,-5.754667,3.528669,2.656152],[2.165111,0.166869,-4.496930,4.460220,5.844727,-0.507773,-6.176714,-4.785544,-5.497065,1.081744,-3.262088,-6.882352,-8.639986,3.216083,5.662327],[-1.020708,-0.519732,6.620361,-1.727671,3.537676,-1.766047,-7.536086,-6.099133,-5.669801,8.790159,6.309008,-5.788001,8.572132,-1.350645,-7.987779],[-1.796960,-2.113172,9.567803,6.339689,-3.803226,9.802854,8.169365,7.651351,-3.649395,-4.965851,-0.927915,1.871240,0.697069,4.069791,7.796529],[-5.773440,-7.361162,-8.647136,-1.805794,-3.979340,-7.464508,-5.425015,5.132233,2.217643,6.787938,-8.182668,-8.649722,-7.419186,-3.770361,3.088303],[9.626390,8.456790,6.730363,1.565805,-7.562683,-9.656727,8.000195,-5.102215,6.314605,-3.332858,6.455013,-4.165640,-6.608881,-3.468790,-9.853922],[-7.338500,5.571967,-4.942368,1.573267,-8.072777,0.735224,-2.388476,9.815533,0.713070,5.432826,0.393773,-7.717008,-6.815713,-7.198823,-2.309530],[-2.485404,8.523244,-2.094747,-0.778389,8.270310,6.771575,-3.416891,-0.092848,-0.156684,-4.591569,9.562255,0.418654,2.072132,7.037464,-9.151265]],[[-1.059925,-0.308202,-9.763946,7.074657,1.531910,9.528065,0.532294,-3.882345,-7.024342,-1.272275,-2.564592,-0.056100,9.084483,2.881201,-6.764384],[-4.030109,5.545880,-7.469161,-0.375087,-2.907577,-2.196118,-1.721314,0.988846,4.606393,-1.853841,-5.958443,-0.383891,-7.079626,-5.996657,-6.599764],[7.732603,-4.176137,4.025321,-0.152772,-5.006265,2.299644,-8.991588,1.455248,1.246149,9.938805,-8.834328,-8.385374,9.878173,-3.137204,5.033500],[-6.097102,-0.596622,0.987176,2.328254,6.635132,-9.549225,-7.301090,-5.842955,1.197780,3.544932,6.204706,-4.790736,-0.680162,-7.936850,-8.307358],[2.807160,-2.577021,8.625840,3.006175,5.947836,-7.063299,-9.354350,4.556128,-3.362441,-8.391079,8.325065,8.662891,8.258734,6.573628,6.525288],[4.868245,-0.137836,-5.061023,4.417726,-9.980493,-1.541911,2.176737,-4.348699,1.466979,7.863473,-4.272005,-3.475818,-3.369060,5.757830,4.588121],[1.836094,5.864598,3.318448,6.669303,6.579333,8.908509,6.561225,-1.752595,0.169812,-2.150905,0.590059,-6.359910,5.162168,-7.278758,-6.525538],[4.765779,-2.698504,-6.545173,-0.316613,1.400774,0.015602,4.046683,3.196801,-6.211160,9.564277,2.481428,0.540933,-1.318091,-4.028886,1.150253],[5.190919,3.449873,0.275700,6.673279,9.454405,-2.655433,8.014944,4.203650,9.766779,-6.090205,7.807004,-4.879043,2.008585,4.399687,5.279621],[-3.790448,8.596395,-3.913101,9.125238,-1.320928,-1.982248,-1.212421,-5.201594,-3.680801,8.740553,-9.503119,-7.839367,-6.409581,-6.676187,-3.452073],[-5.465729,-8.594265,-0.119144,5.210473,-1.334678,-2.286779,-1.296521,-4.109503,0.293928,-0.201993,0.866948,6.132530,8.322766,7.994019,7.324807],[5.427348,4.229490,5.085734,4.917222,2.438225,-3.347118,-2.977514,-2.394561,1.567104,-2.907851,4.137328,-8.824485,9.288829,-9.629707,6.697742]]], dtype = "float32")#candidate|5597|(2, 12, 15)|const|float32
bop_5598 = relay.mod(var_5596.astype('float32'), const_5597.astype('float32')) # shape=(2, 12, 15)
var_5604 = relay.var("var_5604", dtype = "float32", shape = (2, 12, 15))#candidate|5604|(2, 12, 15)|var|float32
bop_5605 = relay.not_equal(const_5597.astype('bool'), relay.reshape(var_5604.astype('bool'), relay.shape_of(const_5597))) # shape=(2, 12, 15)
const_5615 = relay.const([[[3.066779,5.710940,-6.597126,-3.633788,-1.998215,4.628677,2.612498,8.480438,-3.184241,-7.592475,-9.796674,0.398695,7.339158,8.393254,-1.130687],[-1.187614,4.333193,8.812123,-3.430554,-6.186093,-3.111322,8.862472,-5.050928,-1.331712,-8.856717,-9.858149,-9.840703,-3.898600,2.540322,-0.116576],[-6.503026,1.615316,-6.867306,9.722380,-8.479126,-8.146672,-7.420157,4.574082,-1.087323,9.846749,-6.096163,-9.437713,-1.402533,-3.996802,-5.743582],[0.725206,-6.266646,4.500292,4.356105,4.948701,-4.821819,-2.298439,-5.867756,6.417778,4.176411,4.725750,7.895551,1.006576,-3.143897,7.292037],[-6.278598,-7.024282,-9.354776,9.333897,-1.004570,9.197951,-5.240677,2.921198,6.411367,-9.642963,-4.635329,-5.838142,1.288349,1.422753,-4.403171],[-2.481961,2.551916,9.321717,-8.547054,-0.158703,5.212256,-7.522837,6.102186,-3.454673,-8.760587,-8.000964,6.302990,-5.350549,-4.970966,-9.712521],[4.621616,2.291928,5.914597,-7.965334,8.514185,0.128606,-6.444649,2.912831,9.168189,1.882422,-4.688685,-3.197810,-9.121204,-9.964866,-4.928539],[3.096569,5.044479,3.232141,0.738206,4.714170,-7.759214,-1.476271,-1.857225,-2.077792,5.817922,8.713917,1.788307,7.957785,8.405682,-6.548325],[8.833710,5.133987,-3.330919,8.393285,-3.603612,9.608418,0.295289,5.027976,4.526803,-3.949015,4.155248,-9.107765,2.970410,6.388371,7.557913],[2.987488,1.149025,3.288500,5.294854,-1.565071,8.888778,-2.163053,5.692374,-7.022675,2.266875,9.559969,8.957338,-6.858410,-9.307405,8.183348],[2.028869,-2.882521,6.758893,1.573313,-1.242609,-0.196708,3.174479,4.109235,-3.204619,3.954272,-2.976105,5.840952,-3.084487,-4.407776,8.257185],[-4.699967,-9.107208,9.015339,-2.701831,-8.862373,-0.623747,9.085062,4.235190,-3.840428,-6.152799,-4.082614,9.242477,-8.332981,7.224787,-1.273435]],[[-1.021547,6.309684,0.078558,-4.622851,1.223425,-3.172810,9.579528,8.528981,-9.755356,4.445280,3.687586,7.726378,5.489559,-9.082691,0.559655],[2.881220,1.805817,-6.661694,4.396476,3.541288,-4.639813,5.481110,9.645888,-8.702539,-1.730679,-8.957717,3.074365,-7.159292,-3.943065,8.318416],[7.229211,7.391222,-6.909504,2.775959,9.926363,-7.802380,4.919699,1.118785,1.172253,-5.755450,2.050529,5.801257,9.332814,1.953506,5.459488],[0.380968,2.876518,5.128431,-2.544526,-5.947113,0.001932,6.852541,-4.623435,0.915066,2.418481,3.890863,7.869833,3.827721,5.282043,-1.635967],[-1.586242,6.682562,-5.709659,2.949435,-5.964248,-8.918850,-7.258123,-2.460319,7.334683,-1.133535,0.117402,2.547841,9.729516,3.721907,-6.431102],[5.299383,2.585497,-9.444880,5.155016,7.375955,3.535905,-7.398231,6.133968,-8.883031,-8.903344,9.120394,1.813994,-5.083882,-2.627359,4.135628],[3.312837,7.884107,3.632823,4.083492,2.590517,-3.023849,-0.933774,-6.347143,7.290667,-2.362970,-1.879843,-3.251750,1.338050,-0.327115,-9.646943],[-6.768921,-4.216083,0.763679,2.130537,-0.215541,1.905789,-8.412638,5.704826,0.847217,5.386803,4.436681,-1.292659,8.188235,-8.320187,7.905880],[2.539825,7.565276,4.207084,-0.745778,9.286697,6.133832,9.207285,-9.665566,-6.956685,-5.351418,-3.896839,8.004545,3.218202,-3.336297,-4.220025],[-2.528962,0.793331,3.892282,-5.894863,5.123610,3.710300,-1.546416,-6.448977,2.185532,9.813373,5.985808,8.695645,-6.850631,0.714531,5.752811],[-1.990341,-3.957013,3.191279,-7.545804,0.118043,8.667944,-3.427052,2.391089,-2.329786,6.493715,-5.733416,6.386214,-6.494858,-8.521897,-2.913004],[7.132320,-3.916790,-7.324373,-6.082283,1.647770,0.460843,-0.531773,2.897177,-6.846174,-5.589714,6.622672,-0.078387,1.290993,-4.630171,8.345802]]], dtype = "float32")#candidate|5615|(2, 12, 15)|const|float32
bop_5616 = relay.less_equal(bop_5598.astype('bool'), relay.reshape(const_5615.astype('bool'), relay.shape_of(bop_5598))) # shape=(2, 12, 15)
output = relay.Tuple([bop_5605,bop_5616,])
output2 = relay.Tuple([bop_5605,bop_5616,])
func_5620 = relay.Function([var_5596,var_5604,], output)
mod['func_5620'] = func_5620
mod = relay.transform.InferType()(mod)
var_5621 = relay.var("var_5621", dtype = "float32", shape = (2, 1, 15))#candidate|5621|(2, 1, 15)|var|float32
var_5622 = relay.var("var_5622", dtype = "float32", shape = (2, 12, 15))#candidate|5622|(2, 12, 15)|var|float32
output = func_5620(var_5621,var_5622,)
func_5623 = relay.Function([var_5621,var_5622,], output)
mutated_mod['func_5623'] = func_5623
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4819_call = mod.get_global_var('func_4819')
func_4820_call = mutated_mod.get_global_var('func_4820')
call_5627 = relay.TupleGetItem(func_4819_call(), 0)
call_5628 = relay.TupleGetItem(func_4820_call(), 0)
func_3263_call = mod.get_global_var('func_3263')
func_3264_call = mutated_mod.get_global_var('func_3264')
call_5630 = func_3263_call()
call_5631 = func_3263_call()
func_3277_call = mod.get_global_var('func_3277')
func_3278_call = mutated_mod.get_global_var('func_3278')
call_5632 = func_3277_call()
call_5633 = func_3277_call()
func_3079_call = mod.get_global_var('func_3079')
func_3080_call = mutated_mod.get_global_var('func_3080')
call_5645 = relay.TupleGetItem(func_3079_call(), 0)
call_5646 = relay.TupleGetItem(func_3080_call(), 0)
output = relay.Tuple([call_5627,call_5630,call_5632,call_5645,])
output2 = relay.Tuple([call_5628,call_5631,call_5633,call_5646,])
func_5677 = relay.Function([], output)
mod['func_5677'] = func_5677
mod = relay.transform.InferType()(mod)
mutated_mod['func_5677'] = func_5677
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5677_call = mutated_mod.get_global_var('func_5677')
call_5678 = func_5677_call()
output = call_5678
func_5679 = relay.Function([], output)
mutated_mod['func_5679'] = func_5679
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5732 = relay.const([[[-3.533562],[-6.261785],[2.856403],[-8.843594],[3.563014],[7.792887],[-0.575133],[-7.177362],[-0.809130],[-8.639663],[-7.160188],[-5.157104],[8.021050],[-2.354368],[-8.357903],[-8.218941]],[[3.356278],[-5.062264],[-5.331253],[-3.611630],[7.511296],[-8.168204],[0.465997],[-4.584659],[-2.278295],[4.938934],[0.243332],[-3.304006],[-9.700799],[7.399488],[-3.105118],[5.131496]],[[-5.123852],[-1.115653],[-1.429048],[-1.768775],[7.502918],[-4.463183],[8.565669],[-4.088769],[1.544774],[9.935384],[6.436837],[9.527286],[-1.453487],[-9.871340],[-5.895813],[7.536991]],[[1.241170],[1.225977],[-1.158656],[-1.739956],[-9.211726],[-4.443181],[8.214929],[2.540400],[-4.703424],[8.866549],[-7.290570],[5.244989],[3.185687],[0.659095],[2.269416],[-6.317787]],[[-9.676461],[2.092525],[9.669682],[-0.744842],[-0.374683],[-1.869409],[2.839435],[-7.556194],[-0.535798],[-4.761138],[-2.992871],[3.139318],[2.208112],[1.614656],[3.634698],[-5.131369]],[[4.902434],[-3.432969],[3.129206],[-5.298286],[3.563477],[4.028761],[-7.634219],[-7.171805],[6.861307],[4.060842],[-6.620102],[5.207017],[9.090671],[8.371880],[-2.365657],[-8.598712]],[[4.692710],[-6.932959],[-6.451977],[-0.247247],[3.145576],[-0.033656],[1.191237],[-1.837964],[0.461461],[-4.667821],[5.040976],[-9.056029],[-1.651714],[7.230436],[7.207348],[-4.629616]],[[6.632417],[7.345758],[2.001027],[9.966151],[5.846273],[-9.561560],[4.318347],[4.248892],[-6.145079],[-1.174891],[1.964323],[-3.753152],[-7.397185],[-3.863582],[9.180438],[-4.708860]],[[0.902223],[-3.735153],[2.698131],[-6.069370],[-5.490162],[1.162457],[7.770424],[-8.196221],[-7.540764],[9.811802],[1.567246],[1.390007],[-4.762590],[0.911167],[-8.652966],[-7.293819]],[[4.553946],[-4.111276],[-1.675872],[0.376074],[7.834402],[-0.008916],[5.817143],[-6.119418],[-7.265800],[6.570034],[5.080843],[3.793152],[-8.646507],[-7.393154],[7.295684],[6.208886]],[[7.463458],[9.469631],[-5.400416],[-5.558784],[-5.635083],[-1.443589],[-9.926840],[3.975129],[5.457585],[-1.464933],[-7.258247],[-6.822180],[1.228915],[9.474340],[7.426983],[9.337493]],[[2.757035],[-2.709271],[-3.529388],[2.559112],[-9.600346],[-9.956837],[5.600297],[3.026982],[5.877761],[7.020947],[5.684260],[-3.893454],[-6.466196],[3.143780],[-3.802441],[4.346530]],[[-6.919385],[6.710285],[-0.980982],[1.919121],[9.822063],[3.464771],[5.811693],[8.282702],[2.747559],[-9.022815],[-8.169088],[7.142730],[9.061807],[-1.185289],[8.726241],[9.970931]],[[3.832255],[-8.050163],[2.901882],[-3.950677],[-2.062806],[4.497646],[-3.909240],[-5.758578],[-5.767421],[9.017341],[3.702577],[9.747877],[5.317176],[3.525135],[8.473237],[-2.957368]],[[9.403450],[7.792061],[-7.441503],[3.195908],[5.048125],[8.461970],[6.919537],[6.358343],[-4.562637],[-0.958343],[7.497444],[-5.886237],[3.899763],[-3.602819],[-0.388888],[-2.039160]]], dtype = "float64")#candidate|5732|(15, 16, 1)|const|float64
uop_5733 = relay.sin(const_5732.astype('float64')) # shape=(15, 16, 1)
bop_5735 = relay.less(uop_5733.astype('bool'), relay.reshape(const_5732.astype('bool'), relay.shape_of(uop_5733))) # shape=(15, 16, 1)
bop_5742 = relay.logical_and(bop_5735.astype('bool'), relay.reshape(const_5732.astype('bool'), relay.shape_of(bop_5735))) # shape=(15, 16, 1)
uop_5748 = relay.erf(bop_5735.astype('float32')) # shape=(15, 16, 1)
output = relay.Tuple([bop_5742,uop_5748,])
output2 = relay.Tuple([bop_5742,uop_5748,])
func_5762 = relay.Function([], output)
mod['func_5762'] = func_5762
mod = relay.transform.InferType()(mod)
mutated_mod['func_5762'] = func_5762
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5762_call = mutated_mod.get_global_var('func_5762')
call_5763 = func_5762_call()
output = call_5763
func_5764 = relay.Function([], output)
mutated_mod['func_5764'] = func_5764
mutated_mod = relay.transform.InferType()(mutated_mod)
func_119_call = mod.get_global_var('func_119')
func_121_call = mutated_mod.get_global_var('func_121')
call_5770 = relay.TupleGetItem(func_119_call(), 2)
call_5771 = relay.TupleGetItem(func_121_call(), 2)
func_1472_call = mod.get_global_var('func_1472')
func_1474_call = mutated_mod.get_global_var('func_1474')
var_5781 = relay.var("var_5781", dtype = "float64", shape = (108,))#candidate|5781|(108,)|var|float64
call_5780 = relay.TupleGetItem(func_1472_call(relay.reshape(var_5781.astype('float64'), [6, 3, 6])), 0)
call_5782 = relay.TupleGetItem(func_1474_call(relay.reshape(var_5781.astype('float64'), [6, 3, 6])), 0)
output = relay.Tuple([call_5770,call_5780,var_5781,])
output2 = relay.Tuple([call_5771,call_5782,var_5781,])
func_5783 = relay.Function([var_5781,], output)
mod['func_5783'] = func_5783
mod = relay.transform.InferType()(mod)
var_5784 = relay.var("var_5784", dtype = "float64", shape = (108,))#candidate|5784|(108,)|var|float64
output = func_5783(var_5784)
func_5785 = relay.Function([var_5784], output)
mutated_mod['func_5785'] = func_5785
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1728_call = mod.get_global_var('func_1728')
func_1730_call = mutated_mod.get_global_var('func_1730')
call_5798 = relay.TupleGetItem(func_1728_call(), 0)
call_5799 = relay.TupleGetItem(func_1730_call(), 0)
output = call_5798
output2 = call_5799
func_5800 = relay.Function([], output)
mod['func_5800'] = func_5800
mod = relay.transform.InferType()(mod)
output = func_5800()
func_5801 = relay.Function([], output)
mutated_mod['func_5801'] = func_5801
mutated_mod = relay.transform.InferType()(mutated_mod)
func_285_call = mod.get_global_var('func_285')
func_286_call = mutated_mod.get_global_var('func_286')
call_5812 = func_285_call()
call_5813 = func_285_call()
const_5822 = relay.const([[[-1.208336,6.314122,7.655351,1.881273,2.523025,2.666630],[-0.626490,7.291068,7.782647,2.438985,6.552011,-8.886594],[4.848177,-2.270480,-8.927613,-1.886133,3.832641,-6.025544],[3.671821,-5.668888,9.639938,8.894496,7.696706,-5.847344],[2.847635,5.712815,-2.831752,8.307676,-8.034959,-8.416443],[5.779270,-9.481910,-4.476661,1.174554,-0.458737,-3.417144],[-3.210994,7.145096,-8.623179,-2.112680,-6.473862,-4.223972],[-8.931056,-0.796649,-8.338365,4.519075,-6.178787,-8.700588]],[[-8.424083,-8.193491,3.373779,-4.990612,4.227536,8.093493],[-7.164826,4.050841,9.501197,4.178780,0.809606,1.068408],[-3.070047,-5.802234,-8.291964,2.458799,-9.182380,1.483764],[-0.426244,7.072366,-0.514829,1.823732,8.215534,0.697069],[7.474372,-6.019205,-4.951164,-0.438950,-0.333294,9.123542],[8.719693,4.151465,1.447699,1.531014,1.939712,4.959277],[-2.680925,-7.320691,2.473695,-5.501962,-5.588608,-8.757713],[-8.243740,-3.316393,3.270781,3.112151,-0.948505,-9.569424]],[[-3.594859,-2.585539,2.507710,5.093017,-8.731717,7.512288],[8.913948,-0.333820,-6.521093,-8.638553,8.553018,7.477424],[1.542688,9.660513,5.833327,9.175180,-5.928355,1.153446],[2.920860,0.256358,-0.527439,0.935153,-0.124528,-1.468728],[-6.490895,-1.542658,3.460432,-6.188856,-5.738023,-6.110343],[-4.246387,6.373210,1.281387,-4.090122,4.867297,1.870120],[-6.444001,0.443754,-9.204734,5.992456,1.614772,7.216058],[4.312989,5.278173,4.281431,8.510489,2.796851,-3.939428]],[[-9.480104,7.750870,-9.406288,1.918219,7.293353,-2.880890],[-7.621876,3.217905,3.079069,-8.586014,-3.868584,-2.226785],[-7.941670,0.446750,7.392012,-9.063898,-1.709343,7.298768],[-4.146682,2.057809,-5.907753,-6.079969,0.637693,-6.231171],[-3.196021,9.886822,-6.363206,-3.579307,-6.019510,-4.846393],[-7.256458,0.484957,-0.934067,9.095733,6.681063,-2.519107],[-0.061429,5.555964,-4.568911,-8.274146,-9.641907,-4.273695],[-8.009224,6.073197,-5.109765,-1.699930,6.454558,-5.196388]],[[-8.781940,-8.604961,-1.259107,0.517561,5.074602,0.795466],[-8.790279,-5.656906,1.488545,1.894164,-3.713706,-5.100561],[-3.455676,2.406814,-0.841115,0.611907,4.896900,7.056482],[9.926479,6.137310,0.496638,-7.902708,-6.464290,-8.934813],[3.292494,3.149375,4.957023,4.031224,-0.728647,3.142134],[-2.570540,-5.953367,-4.795708,0.364865,-5.380069,9.181016],[7.352959,-1.159080,-7.475403,-0.948979,-6.837762,0.140185],[9.617343,-5.486677,9.273040,2.783883,-1.653733,-1.474277]],[[8.025268,-0.734250,-3.455991,8.546077,-4.461335,9.599880],[-6.403907,-1.642329,-8.161624,-9.423215,-6.685533,3.939983],[-5.857824,0.034040,-8.034099,-4.724707,-7.516993,-4.522854],[-2.783569,-9.332832,3.255253,7.159598,6.667142,-4.366428],[-5.433735,-1.390072,9.849924,-1.291242,-7.014467,6.671269],[1.916228,-6.424115,-7.961936,-0.960112,-6.997063,9.394785],[1.208430,3.617775,6.013487,-9.826670,4.501899,-8.965471],[-4.085999,-6.628932,4.822635,-2.737467,3.815639,-3.148061]]], dtype = "float64")#candidate|5822|(6, 8, 6)|const|float64
bop_5823 = relay.floor_divide(call_5812.astype('float64'), const_5822.astype('float64')) # shape=(6, 8, 6)
bop_5826 = relay.floor_divide(call_5813.astype('float64'), const_5822.astype('float64')) # shape=(6, 8, 6)
const_5831 = relay.const([[[-5.605214,6.600263,-8.923596,-4.738850,-4.468707,-2.995737],[-8.539538,-5.404592,4.054140,-8.426084,5.482176,2.942475],[-7.331279,-4.149127,7.068930,-7.943923,7.467901,-2.262876],[9.376659,0.040894,-2.135900,8.173057,-9.944739,-6.516836],[-6.042864,-5.843297,-0.343271,3.724267,8.899157,-2.583553],[5.922583,-8.336288,-3.167209,7.744482,-1.312084,3.722941],[-9.746216,9.844277,3.241304,-6.756106,-3.235440,8.845938],[-7.495614,3.157176,-3.817708,-8.964233,-1.047029,-5.973575]],[[0.049133,-8.539911,-6.778480,2.460258,6.376383,8.958450],[-2.910794,-0.178993,-1.887095,7.285926,-8.080758,-1.509090],[-9.836402,0.584694,-0.068170,9.026195,1.524051,4.935208],[-2.987043,-3.649544,9.894825,-2.967328,3.451528,-3.414530],[-5.827161,-6.478378,1.306945,-3.573863,3.616063,-7.155880],[8.277023,2.207378,-4.920022,7.774498,1.306638,-0.805025],[0.662976,8.826355,2.903500,4.351605,6.371623,7.689475],[-7.953886,8.157379,5.541485,5.928637,6.820636,3.136645]],[[5.774163,-4.141117,-9.538684,7.362360,4.779834,-7.489364],[6.123637,9.126270,6.429161,9.233029,-2.638560,6.194118],[-2.513788,-5.622360,9.159917,3.417498,-3.196480,-3.529521],[-7.931321,5.819607,-0.123276,7.658279,0.800375,-4.411657],[1.049734,-1.545928,-6.387367,0.230095,0.021432,3.695467],[2.752802,4.816528,-9.876455,-6.238854,-9.780895,6.255581],[2.148499,-2.309995,3.420186,5.069712,-1.087841,-8.086235],[0.178681,9.149213,0.307257,7.497351,-7.721951,5.905199]],[[-0.868846,8.706964,3.996872,9.136260,8.323335,2.972748],[2.023855,1.341875,-3.548518,-8.109808,0.913245,-8.331385],[-4.533184,7.730059,7.493072,-9.279746,-7.450648,-3.606305],[-5.053170,-6.964286,7.449689,-6.573806,-4.436426,-8.704072],[8.697869,-8.586485,-2.729817,6.287676,7.270081,5.996377],[5.610415,-5.069135,-6.101356,7.670843,3.103095,-4.366345],[9.202976,7.140046,3.918504,9.918442,-6.799717,5.673351],[-5.319550,-8.543510,-5.455445,-0.476902,9.000055,4.101635]],[[0.848876,-7.385322,0.765395,3.451340,0.138782,-6.722588],[-1.200833,1.802227,-8.595246,-8.820578,3.197461,-4.693724],[-6.476767,-9.333200,0.384485,3.687939,-4.349659,5.824723],[6.640015,0.370223,1.439463,1.841794,1.777766,1.549201],[8.218052,-7.673336,-8.357084,-6.678754,-0.645354,-5.970192],[4.784779,-9.057351,5.077364,1.442320,6.752533,5.211405],[-5.403482,-1.740482,5.590078,9.617735,7.188625,5.564072],[-9.332858,6.298774,-2.252084,7.978598,9.947321,-1.060356]],[[8.538803,8.312189,-2.779028,-8.563484,0.554610,-3.482989],[-4.425508,-3.231128,6.172406,9.464198,7.741256,-6.150803],[-1.223654,3.699081,-8.806092,-7.389430,1.335240,-7.848408],[-6.019130,3.553244,6.532243,-6.221388,3.854682,-3.550188],[-2.532738,7.675395,-3.224620,-3.671777,0.768794,-2.797902],[6.913292,2.701429,1.009204,-8.226613,-8.223300,7.600555],[2.594033,0.557248,-3.472500,5.715956,5.224284,3.973991],[7.964418,-2.361386,2.927201,-5.486498,9.310525,-5.168526]]], dtype = "float64")#candidate|5831|(6, 8, 6)|const|float64
bop_5832 = relay.less(bop_5823.astype('bool'), relay.reshape(const_5831.astype('bool'), relay.shape_of(bop_5823))) # shape=(6, 8, 6)
bop_5835 = relay.less(bop_5826.astype('bool'), relay.reshape(const_5831.astype('bool'), relay.shape_of(bop_5826))) # shape=(6, 8, 6)
uop_5846 = relay.asinh(const_5831.astype('float64')) # shape=(6, 8, 6)
output = relay.Tuple([bop_5832,uop_5846,])
output2 = relay.Tuple([bop_5835,uop_5846,])
func_5848 = relay.Function([], output)
mod['func_5848'] = func_5848
mod = relay.transform.InferType()(mod)
output = func_5848()
func_5849 = relay.Function([], output)
mutated_mod['func_5849'] = func_5849
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5871 = relay.var("var_5871", dtype = "float32", shape = (8, 16, 2))#candidate|5871|(8, 16, 2)|var|float32
uop_5872 = relay.atan(var_5871.astype('float32')) # shape=(8, 16, 2)
uop_5878 = relay.asin(var_5871.astype('float32')) # shape=(8, 16, 2)
func_685_call = mod.get_global_var('func_685')
func_687_call = mutated_mod.get_global_var('func_687')
call_5897 = relay.TupleGetItem(func_685_call(), 2)
call_5898 = relay.TupleGetItem(func_687_call(), 2)
func_1964_call = mod.get_global_var('func_1964')
func_1966_call = mutated_mod.get_global_var('func_1966')
call_5917 = relay.TupleGetItem(func_1964_call(), 0)
call_5918 = relay.TupleGetItem(func_1966_call(), 0)
output = relay.Tuple([uop_5872,uop_5878,call_5897,call_5917,])
output2 = relay.Tuple([uop_5872,uop_5878,call_5898,call_5918,])
func_5922 = relay.Function([var_5871,], output)
mod['func_5922'] = func_5922
mod = relay.transform.InferType()(mod)
mutated_mod['func_5922'] = func_5922
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5923 = relay.var("var_5923", dtype = "float32", shape = (8, 16, 2))#candidate|5923|(8, 16, 2)|var|float32
func_5922_call = mutated_mod.get_global_var('func_5922')
call_5924 = func_5922_call(var_5923)
output = call_5924
func_5925 = relay.Function([var_5923], output)
mutated_mod['func_5925'] = func_5925
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3715_call = mod.get_global_var('func_3715')
func_3717_call = mutated_mod.get_global_var('func_3717')
call_6001 = relay.TupleGetItem(func_3715_call(), 1)
call_6002 = relay.TupleGetItem(func_3717_call(), 1)
output = relay.Tuple([call_6001,])
output2 = relay.Tuple([call_6002,])
func_6048 = relay.Function([], output)
mod['func_6048'] = func_6048
mod = relay.transform.InferType()(mod)
output = func_6048()
func_6049 = relay.Function([], output)
mutated_mod['func_6049'] = func_6049
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4691_call = mod.get_global_var('func_4691')
func_4693_call = mutated_mod.get_global_var('func_4693')
call_6171 = func_4691_call()
call_6172 = func_4691_call()
var_6175 = relay.var("var_6175", dtype = "int16", shape = (6, 13, 6))#candidate|6175|(6, 13, 6)|var|int16
bop_6176 = relay.equal(call_6171.astype('bool'), var_6175.astype('bool')) # shape=(6, 13, 6)
bop_6179 = relay.equal(call_6172.astype('bool'), var_6175.astype('bool')) # shape=(6, 13, 6)
func_1145_call = mod.get_global_var('func_1145')
func_1147_call = mutated_mod.get_global_var('func_1147')
call_6182 = relay.TupleGetItem(func_1145_call(relay.reshape(call_6171.astype('float64'), [6, 1, 6])), 1)
call_6183 = relay.TupleGetItem(func_1147_call(relay.reshape(call_6171.astype('float64'), [6, 1, 6])), 1)
func_1245_call = mod.get_global_var('func_1245')
func_1246_call = mutated_mod.get_global_var('func_1246')
call_6195 = relay.TupleGetItem(func_1245_call(), 0)
call_6196 = relay.TupleGetItem(func_1246_call(), 0)
output = relay.Tuple([bop_6176,call_6182,call_6195,])
output2 = relay.Tuple([bop_6179,call_6183,call_6196,])
func_6212 = relay.Function([var_6175,], output)
mod['func_6212'] = func_6212
mod = relay.transform.InferType()(mod)
var_6213 = relay.var("var_6213", dtype = "int16", shape = (6, 13, 6))#candidate|6213|(6, 13, 6)|var|int16
output = func_6212(var_6213)
func_6214 = relay.Function([var_6213], output)
mutated_mod['func_6214'] = func_6214
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1584_call = mod.get_global_var('func_1584')
func_1586_call = mutated_mod.get_global_var('func_1586')
call_6240 = relay.TupleGetItem(func_1584_call(), 0)
call_6241 = relay.TupleGetItem(func_1586_call(), 0)
func_1834_call = mod.get_global_var('func_1834')
func_1836_call = mutated_mod.get_global_var('func_1836')
call_6254 = func_1834_call()
call_6255 = func_1834_call()
func_3536_call = mod.get_global_var('func_3536')
func_3538_call = mutated_mod.get_global_var('func_3538')
call_6266 = relay.TupleGetItem(func_3536_call(), 0)
call_6267 = relay.TupleGetItem(func_3538_call(), 0)
func_4233_call = mod.get_global_var('func_4233')
func_4235_call = mutated_mod.get_global_var('func_4235')
var_6283 = relay.var("var_6283", dtype = "float64", shape = (9, 36))#candidate|6283|(9, 36)|var|float64
call_6282 = relay.TupleGetItem(func_4233_call(relay.reshape(var_6283.astype('float64'), [162, 2])), 0)
call_6284 = relay.TupleGetItem(func_4235_call(relay.reshape(var_6283.astype('float64'), [162, 2])), 0)
output = relay.Tuple([call_6240,call_6254,call_6266,call_6282,var_6283,])
output2 = relay.Tuple([call_6241,call_6255,call_6267,call_6284,var_6283,])
func_6309 = relay.Function([var_6283,], output)
mod['func_6309'] = func_6309
mod = relay.transform.InferType()(mod)
mutated_mod['func_6309'] = func_6309
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6310 = relay.var("var_6310", dtype = "float64", shape = (9, 36))#candidate|6310|(9, 36)|var|float64
func_6309_call = mutated_mod.get_global_var('func_6309')
call_6311 = func_6309_call(var_6310)
output = call_6311
func_6312 = relay.Function([var_6310], output)
mutated_mod['func_6312'] = func_6312
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4282_call = mod.get_global_var('func_4282')
func_4284_call = mutated_mod.get_global_var('func_4284')
call_6314 = func_4282_call()
call_6315 = func_4282_call()
var_6318 = relay.var("var_6318", dtype = "bool", shape = (6, 4, 6))#candidate|6318|(6, 4, 6)|var|bool
bop_6319 = relay.divide(call_6314.astype('float64'), var_6318.astype('float64')) # shape=(6, 4, 6)
bop_6322 = relay.divide(call_6315.astype('float64'), var_6318.astype('float64')) # shape=(6, 4, 6)
output = relay.Tuple([bop_6319,])
output2 = relay.Tuple([bop_6322,])
func_6323 = relay.Function([var_6318,], output)
mod['func_6323'] = func_6323
mod = relay.transform.InferType()(mod)
mutated_mod['func_6323'] = func_6323
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6324 = relay.var("var_6324", dtype = "bool", shape = (6, 4, 6))#candidate|6324|(6, 4, 6)|var|bool
func_6323_call = mutated_mod.get_global_var('func_6323')
call_6325 = func_6323_call(var_6324)
output = call_6325
func_6326 = relay.Function([var_6324], output)
mutated_mod['func_6326'] = func_6326
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6360 = relay.var("var_6360", dtype = "float32", shape = (10, 1, 2))#candidate|6360|(10, 1, 2)|var|float32
uop_6361 = relay.asin(var_6360.astype('float32')) # shape=(10, 1, 2)
uop_6374 = relay.log(uop_6361.astype('float64')) # shape=(10, 1, 2)
bop_6376 = relay.floor_divide(uop_6374.astype('float32'), relay.reshape(var_6360.astype('float32'), relay.shape_of(uop_6374))) # shape=(10, 1, 2)
output = bop_6376
output2 = bop_6376
F = relay.Function([var_6360,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_6360,], output2)
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
