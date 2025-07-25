import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
const_269 = relay.const([[[10,-6,5,-6,5,1,-3,6,5,-8,9,10,8],[-3,9,-6,-7,7,8,-4,-3,3,-4,-9,-8,-9],[-10,-7,8,-5,3,-6,-2,10,-8,-5,1,-8,8],[5,6,-4,-3,-7,10,8,3,-4,10,-7,2,1],[3,-8,9,-8,7,3,3,-1,-2,-8,2,10,-6],[2,10,-1,3,3,-5,8,10,-2,-1,-8,1,-8],[6,6,-4,1,-2,-6,-6,-10,9,-2,1,-4,8],[-5,-5,-5,10,6,10,7,-2,10,3,8,7,-3],[-6,1,10,-5,1,-8,1,-5,3,-6,7,4,5]],[[-4,-6,1,7,-7,1,1,-2,-5,7,8,1,7],[-10,-10,5,-7,2,-2,-1,-5,1,-4,-7,7,-8],[3,9,-9,-3,3,-4,10,10,6,-2,-4,7,7],[-9,-7,1,8,10,-8,8,-10,6,2,-3,-7,-9],[8,-1,1,9,-4,-8,10,-10,10,4,4,-3,3],[-5,8,1,10,-1,9,9,-2,-8,4,5,-9,7],[8,-8,-5,-3,-6,1,6,7,3,3,-2,10,-2],[-3,3,-2,1,1,-4,-8,-1,-6,-10,4,-8,1],[-7,-7,5,10,1,10,-6,7,7,8,-4,-5,-7]],[[10,-4,-7,-1,2,6,7,-5,-9,-7,-1,-4,2],[-5,-2,4,10,-2,-2,3,2,-7,-9,5,-5,6],[9,-7,8,8,4,2,1,-3,1,-9,5,4,-2],[2,3,5,8,3,-6,5,-2,-6,-3,7,4,8],[4,3,-1,5,-5,-6,-6,8,-9,-2,10,-5,6],[6,10,9,-6,-1,-7,2,1,-4,8,-9,-3,-9],[8,5,-8,1,-4,1,3,6,-10,-4,6,-8,-10],[-1,-7,-7,4,10,-2,9,1,6,2,6,10,-7],[-7,-9,3,1,10,-6,1,-8,6,1,-5,-3,-10]],[[-3,6,5,4,-2,5,6,3,-2,9,-9,7,-2],[8,-1,4,-9,3,-6,9,5,-1,-1,-4,-1,5],[8,2,4,7,10,-3,-2,2,-5,-7,-5,3,5],[1,10,7,-7,10,-1,-1,8,8,10,9,-1,8],[-5,1,8,-5,5,-8,1,6,-3,-10,10,-1,10],[-10,6,-6,-10,-10,-7,9,-9,6,3,1,-10,-6],[-1,-5,-9,-1,-2,8,1,10,-7,2,6,-3,4],[4,4,-6,-1,7,3,-6,4,9,-6,-5,-10,8],[-9,-4,4,6,-1,5,3,-1,10,3,5,-1,-3]],[[-3,-5,10,1,-6,-3,5,5,4,-3,-4,4,9],[1,10,8,10,2,7,3,8,-6,-8,4,10,-8],[-2,-4,-4,3,-3,-7,4,3,5,-5,-2,8,3],[-3,-9,7,-5,-4,-8,-3,6,3,1,1,4,1],[-8,-5,8,6,-8,1,-4,4,-2,4,-9,7,-5],[-8,-6,-2,-5,-7,-4,4,-6,9,10,5,-2,-9],[7,5,-6,-10,1,9,10,10,-1,-10,-1,-8,-2],[-2,-9,9,9,-8,6,-9,2,2,-6,-8,9,3],[-6,-3,-3,5,8,-9,-10,3,-5,-3,-2,10,9]],[[6,-3,10,-9,8,-7,-3,-8,1,-9,4,-7,-4],[-3,-9,-10,2,6,-3,-4,7,5,-6,4,3,-2],[-9,5,9,6,10,-5,-1,4,-5,6,-2,4,6],[-7,-3,-9,9,-6,1,6,-1,-6,1,-6,-10,8],[3,-2,-10,-1,10,-5,-3,-7,6,8,6,10,5],[4,8,9,-4,10,2,6,1,-10,6,-1,-3,-10],[4,-6,5,4,2,3,-4,1,-8,7,10,-6,-3],[7,-7,-6,-8,-9,4,6,-7,-1,6,7,9,-3],[-9,3,5,9,10,10,8,1,-3,8,-6,10,-3]],[[5,-3,10,5,-8,-7,10,-4,3,2,-4,1,-4],[4,-8,-3,8,-9,-9,-4,-5,-4,6,7,-10,5],[3,-7,-2,1,8,5,9,6,10,-5,-3,-2,-6],[10,8,-9,1,6,-9,-3,2,-4,-2,10,-2,-9],[-3,4,7,-3,-1,-6,2,-6,-10,7,9,-2,4],[4,-7,1,-1,-9,-10,5,-7,-2,2,10,-6,-5],[-10,5,1,10,-2,7,-7,-4,-9,6,10,4,5],[6,-1,-8,8,-7,-3,-6,-9,8,9,10,-1,-3],[6,4,9,5,-3,-3,6,-1,-8,-4,9,-10,6]],[[-6,10,-9,-5,10,-7,6,-7,2,-10,2,1,4],[10,10,-5,2,-4,-4,5,6,8,-1,-2,10,-5],[9,-10,6,6,5,-2,1,-1,-6,-6,8,4,-10],[-2,10,3,-3,-2,-3,7,-4,-9,7,-7,-4,-7],[8,2,10,6,-1,-9,2,-5,10,4,-3,8,-3],[-2,7,-1,-3,-2,-7,10,9,-2,1,-7,3,6],[4,-5,8,-6,-9,9,-8,-4,9,-2,-5,9,-6],[-8,8,5,9,-1,-7,9,1,-7,-9,3,5,4],[2,8,10,6,-2,-1,1,8,-6,6,-7,6,6]],[[-1,7,-2,1,-6,6,10,-3,8,5,-1,-5,8],[-2,5,6,-8,3,3,-8,6,10,-3,-9,6,7],[4,-4,3,1,-3,-3,-1,1,-10,-10,6,-2,-3],[-9,4,-6,-9,5,8,9,-2,-4,-9,-4,7,-3],[3,9,-6,-5,-6,3,3,5,-3,-5,-7,5,-6],[-2,2,-6,-1,-3,5,9,10,5,9,3,6,-6],[-8,8,-9,-7,-8,-8,-9,-5,-10,6,-8,1,2],[-1,3,1,8,5,4,8,6,10,-8,10,3,8],[-6,1,5,6,9,1,-1,-5,-8,-6,1,-10,4]]], dtype = "int16")#candidate|269|(9, 9, 13)|const|int16
const_270 = relay.const([[[7,8,2,-9,3,-8,-10,-4,10,2,9,-2,-5],[3,3,5,-9,-7,2,1,-8,10,7,-6,6,-2],[1,-9,4,4,-7,5,-3,-6,-10,10,6,-7,-6],[4,2,10,-2,2,2,-1,-6,-2,1,-1,4,1],[3,-7,-5,-2,8,10,2,6,-9,-2,5,1,-3],[9,8,-9,9,2,8,-1,-6,6,3,2,1,7],[10,-4,-2,2,2,-1,-9,7,6,4,6,-2,2],[-3,9,-8,7,2,4,9,5,-9,4,-2,1,-4],[3,-8,-9,-9,8,-9,-9,4,5,9,7,6,3]],[[2,1,-3,-4,-3,-1,-3,-10,-5,3,2,7,10],[9,-5,-4,-10,-3,-3,-5,1,-7,-6,5,5,1],[8,9,1,-3,-2,-3,4,-7,-4,3,8,-8,-8],[4,-2,1,4,-7,-7,9,-9,-6,-10,-2,-3,8],[7,-4,2,10,-4,4,-10,2,3,-1,-6,7,-7],[-10,4,-10,7,-7,3,-3,-6,-6,9,-6,-3,-5],[1,7,-1,-8,9,7,3,5,9,4,4,-4,10],[-5,6,-4,-4,-4,-9,1,10,4,-1,-7,8,10],[3,-4,3,-8,1,-5,-2,-1,1,9,-9,-3,3]],[[-3,-3,-2,6,-9,-7,-9,8,3,-2,1,6,3],[6,-8,-7,-9,-5,-7,10,1,5,-4,-3,-3,1],[10,-5,-3,-10,1,5,10,-2,2,-4,-9,-4,-4],[-2,-3,2,-10,-8,-9,7,8,9,-1,-4,4,5],[-9,-6,5,-1,-1,-4,3,8,-2,1,7,7,-4],[1,9,1,7,2,-5,10,7,9,-8,1,3,10],[-3,-10,-8,-6,10,-8,3,7,-2,-4,-5,-6,-1],[2,10,-6,1,-1,-8,7,-4,-5,4,5,-10,-6],[3,7,10,7,-3,2,-10,2,-1,8,-5,-2,-6]],[[6,5,1,3,-9,-7,-2,3,4,-8,3,-7,-5],[-5,-3,4,-7,1,-5,5,-9,4,5,-7,1,5],[-7,7,5,10,1,7,-1,5,5,1,6,-7,-3],[2,-2,-7,9,4,6,-2,-8,-4,-7,6,-2,-8],[-4,-9,-1,-10,8,-3,-1,-3,-3,-3,-3,-1,-7],[4,3,8,-9,4,-8,3,2,-4,-7,2,-9,-10],[-4,-5,-5,10,1,7,7,-9,8,2,2,-4,1],[6,1,-4,-4,-5,8,-10,5,8,-1,-8,1,-10],[4,-9,-2,-8,-10,7,3,-6,9,-1,-3,8,-6]],[[-4,6,9,2,6,-2,6,-1,7,-4,7,8,10],[7,-9,4,-9,9,-2,-5,-4,5,10,-4,-1,1],[-4,4,-4,1,3,7,8,1,7,-8,-6,3,-10],[4,-7,-7,-7,2,3,3,1,-9,5,8,-7,-7],[1,10,8,3,10,4,-3,1,2,-2,-5,3,-1],[6,-7,-3,-2,2,-7,-5,6,-6,-8,5,-2,-4],[-7,7,-9,-8,-5,-7,-1,8,3,-7,-5,-8,-2],[6,9,9,8,-6,8,-3,4,-9,-8,-5,2,-2],[6,1,-2,-2,-8,10,8,3,9,-8,-8,2,-5]],[[9,-10,4,10,6,4,-6,10,10,-2,-3,-9,-8],[9,2,-8,1,3,-5,-3,-6,2,1,10,1,4],[-4,6,-1,3,-9,6,8,7,2,-8,-9,2,2],[3,5,7,2,3,-10,-7,-7,1,2,-1,-10,-5],[-9,10,1,7,3,-5,-9,8,-5,8,-10,9,9],[-6,-1,7,-10,-5,10,-6,6,-8,10,-2,-1,-8],[3,2,-1,10,-1,-4,-6,3,1,-9,-9,-9,2],[-5,-6,-7,2,1,-10,-5,-10,6,-10,-1,6,-7],[8,-3,1,-7,-3,-6,-4,8,9,-6,6,4,1]],[[-8,-7,2,-3,8,-5,1,-9,-2,-3,8,-6,3],[-6,-10,6,4,5,1,-10,-3,3,-10,-2,-7,3],[-9,8,10,10,-3,-10,-10,-10,4,-9,3,-3,-8],[5,2,-9,-8,-2,2,-10,10,1,-4,2,-3,9],[7,-10,6,8,-5,8,5,4,6,4,4,8,10],[-8,-5,8,-8,8,-6,-4,5,-6,4,10,4,5],[-1,5,-7,4,-1,-5,-3,-5,-1,-1,10,7,-9],[-5,-10,10,5,5,-10,7,3,10,-7,6,3,2],[-9,9,-5,1,-5,9,6,-4,-4,6,3,3,1]],[[7,9,7,-10,5,9,1,7,-5,-3,-9,-2,-4],[1,6,-9,7,-2,-7,1,6,-6,-5,8,-5,-9],[-7,9,7,-3,3,-3,1,5,8,7,-5,2,7],[-9,10,-7,8,-10,-6,-7,-4,-1,8,2,1,1],[-6,5,-2,6,-2,-10,-6,7,-5,3,7,-8,-10],[-8,-2,7,3,-1,-8,-8,9,3,2,9,6,-1],[-8,7,-9,-8,-5,9,9,-2,7,7,2,3,-2],[1,6,3,9,1,7,9,6,-10,9,4,-4,2],[-3,-7,-7,4,-10,-7,-9,9,10,5,-9,3,-7]],[[-4,7,4,-2,4,-1,3,7,4,-8,9,-2,-6],[-1,9,-7,8,8,6,5,9,8,9,2,3,-6],[-10,9,1,6,-10,10,6,2,-8,-2,4,1,-7],[-7,-2,3,3,-7,-5,-4,-5,5,-4,3,-5,-1],[7,4,-2,6,-4,-10,-2,3,2,-4,-2,8,7],[8,-8,-3,-8,1,-8,7,-6,2,4,7,1,-2],[-10,8,4,1,4,7,1,-5,-2,4,9,-8,-9],[10,-6,-4,-3,-4,-10,-8,-9,8,10,-2,6,-10],[9,-2,3,-10,-4,-5,-1,-3,4,-5,6,-6,7]]], dtype = "int16")#candidate|270|(9, 9, 13)|const|int16
bop_271 = relay.bitwise_and(const_269.astype('int16'), relay.reshape(const_270.astype('int16'), relay.shape_of(const_269))) # shape=(9, 9, 13)
uop_290 = relay.atanh(const_269.astype('float64')) # shape=(9, 9, 13)
output = relay.Tuple([bop_271,uop_290,])
output2 = relay.Tuple([bop_271,uop_290,])
func_292 = relay.Function([], output)
mod['func_292'] = func_292
mod = relay.transform.InferType()(mod)
mutated_mod['func_292'] = func_292
mutated_mod = relay.transform.InferType()(mutated_mod)
func_292_call = mutated_mod.get_global_var('func_292')
call_293 = func_292_call()
output = call_293
func_294 = relay.Function([], output)
mutated_mod['func_294'] = func_294
mutated_mod = relay.transform.InferType()(mutated_mod)
func_292_call = mod.get_global_var('func_292')
func_294_call = mutated_mod.get_global_var('func_294')
call_311 = relay.TupleGetItem(func_292_call(), 1)
call_312 = relay.TupleGetItem(func_294_call(), 1)
uop_315 = relay.asinh(call_311.astype('float32')) # shape=(9, 9, 13)
uop_317 = relay.asinh(call_312.astype('float32')) # shape=(9, 9, 13)
func_292_call = mod.get_global_var('func_292')
func_294_call = mutated_mod.get_global_var('func_294')
call_318 = relay.TupleGetItem(func_292_call(), 1)
call_319 = relay.TupleGetItem(func_294_call(), 1)
func_292_call = mod.get_global_var('func_292')
func_294_call = mutated_mod.get_global_var('func_294')
call_321 = relay.TupleGetItem(func_292_call(), 0)
call_322 = relay.TupleGetItem(func_294_call(), 0)
func_292_call = mod.get_global_var('func_292')
func_294_call = mutated_mod.get_global_var('func_294')
call_324 = relay.TupleGetItem(func_292_call(), 0)
call_325 = relay.TupleGetItem(func_294_call(), 0)
func_292_call = mod.get_global_var('func_292')
func_294_call = mutated_mod.get_global_var('func_294')
call_336 = relay.TupleGetItem(func_292_call(), 1)
call_337 = relay.TupleGetItem(func_294_call(), 1)
bop_339 = relay.logical_or(call_324.astype('bool'), relay.reshape(call_318.astype('bool'), relay.shape_of(call_324))) # shape=(9, 9, 13)
bop_342 = relay.logical_or(call_325.astype('bool'), relay.reshape(call_319.astype('bool'), relay.shape_of(call_325))) # shape=(9, 9, 13)
output = relay.Tuple([uop_315,call_321,call_336,bop_339,])
output2 = relay.Tuple([uop_317,call_322,call_337,bop_342,])
func_363 = relay.Function([], output)
mod['func_363'] = func_363
mod = relay.transform.InferType()(mod)
output = func_363()
func_364 = relay.Function([], output)
mutated_mod['func_364'] = func_364
mutated_mod = relay.transform.InferType()(mutated_mod)
func_363_call = mod.get_global_var('func_363')
func_364_call = mutated_mod.get_global_var('func_364')
call_423 = relay.TupleGetItem(func_363_call(), 0)
call_424 = relay.TupleGetItem(func_364_call(), 0)
output = call_423
output2 = call_424
func_433 = relay.Function([], output)
mod['func_433'] = func_433
mod = relay.transform.InferType()(mod)
output = func_433()
func_434 = relay.Function([], output)
mutated_mod['func_434'] = func_434
mutated_mod = relay.transform.InferType()(mutated_mod)
func_433_call = mod.get_global_var('func_433')
func_434_call = mutated_mod.get_global_var('func_434')
call_447 = func_433_call()
call_448 = func_433_call()
func_433_call = mod.get_global_var('func_433')
func_434_call = mutated_mod.get_global_var('func_434')
call_449 = func_433_call()
call_450 = func_433_call()
func_363_call = mod.get_global_var('func_363')
func_364_call = mutated_mod.get_global_var('func_364')
call_456 = relay.TupleGetItem(func_363_call(), 2)
call_457 = relay.TupleGetItem(func_364_call(), 2)
func_433_call = mod.get_global_var('func_433')
func_434_call = mutated_mod.get_global_var('func_434')
call_465 = func_433_call()
call_466 = func_433_call()
output = relay.Tuple([call_447,call_449,call_456,call_465,])
output2 = relay.Tuple([call_448,call_450,call_457,call_466,])
func_468 = relay.Function([], output)
mod['func_468'] = func_468
mod = relay.transform.InferType()(mod)
mutated_mod['func_468'] = func_468
mutated_mod = relay.transform.InferType()(mutated_mod)
func_468_call = mutated_mod.get_global_var('func_468')
call_469 = func_468_call()
output = call_469
func_470 = relay.Function([], output)
mutated_mod['func_470'] = func_470
mutated_mod = relay.transform.InferType()(mutated_mod)
func_363_call = mod.get_global_var('func_363')
func_364_call = mutated_mod.get_global_var('func_364')
call_520 = relay.TupleGetItem(func_363_call(), 2)
call_521 = relay.TupleGetItem(func_364_call(), 2)
func_468_call = mod.get_global_var('func_468')
func_470_call = mutated_mod.get_global_var('func_470')
call_522 = relay.TupleGetItem(func_468_call(), 3)
call_523 = relay.TupleGetItem(func_470_call(), 3)
func_468_call = mod.get_global_var('func_468')
func_470_call = mutated_mod.get_global_var('func_470')
call_528 = relay.TupleGetItem(func_468_call(), 2)
call_529 = relay.TupleGetItem(func_470_call(), 2)
func_292_call = mod.get_global_var('func_292')
func_294_call = mutated_mod.get_global_var('func_294')
call_530 = relay.TupleGetItem(func_292_call(), 0)
call_531 = relay.TupleGetItem(func_294_call(), 0)
uop_532 = relay.log(call_520.astype('float32')) # shape=(9, 9, 13)
uop_534 = relay.log(call_521.astype('float32')) # shape=(9, 9, 13)
output = relay.Tuple([call_522,call_528,call_530,uop_532,])
output2 = relay.Tuple([call_523,call_529,call_531,uop_534,])
func_536 = relay.Function([], output)
mod['func_536'] = func_536
mod = relay.transform.InferType()(mod)
output = func_536()
func_537 = relay.Function([], output)
mutated_mod['func_537'] = func_537
mutated_mod = relay.transform.InferType()(mutated_mod)
func_536_call = mod.get_global_var('func_536')
func_537_call = mutated_mod.get_global_var('func_537')
call_565 = relay.TupleGetItem(func_536_call(), 0)
call_566 = relay.TupleGetItem(func_537_call(), 0)
output = call_565
output2 = call_566
func_573 = relay.Function([], output)
mod['func_573'] = func_573
mod = relay.transform.InferType()(mod)
mutated_mod['func_573'] = func_573
mutated_mod = relay.transform.InferType()(mutated_mod)
func_573_call = mutated_mod.get_global_var('func_573')
call_574 = func_573_call()
output = call_574
func_575 = relay.Function([], output)
mutated_mod['func_575'] = func_575
mutated_mod = relay.transform.InferType()(mutated_mod)
var_597 = relay.var("var_597", dtype = "float64", shape = (6, 3, 6))#candidate|597|(6, 3, 6)|var|float64
uop_598 = relay.sigmoid(var_597.astype('float64')) # shape=(6, 3, 6)
var_600 = relay.var("var_600", dtype = "float64", shape = (6, 3, 6))#candidate|600|(6, 3, 6)|var|float64
bop_601 = relay.divide(uop_598.astype('float32'), relay.reshape(var_600.astype('float32'), relay.shape_of(uop_598))) # shape=(6, 3, 6)
uop_607 = relay.asinh(uop_598.astype('float64')) # shape=(6, 3, 6)
uop_611 = relay.atanh(var_600.astype('float32')) # shape=(6, 3, 6)
bop_630 = relay.maximum(uop_598.astype('int32'), relay.reshape(uop_607.astype('int32'), relay.shape_of(uop_598))) # shape=(6, 3, 6)
func_468_call = mod.get_global_var('func_468')
func_470_call = mutated_mod.get_global_var('func_470')
call_648 = relay.TupleGetItem(func_468_call(), 2)
call_649 = relay.TupleGetItem(func_470_call(), 2)
output = relay.Tuple([bop_601,uop_611,bop_630,call_648,])
output2 = relay.Tuple([bop_601,uop_611,bop_630,call_649,])
func_650 = relay.Function([var_597,var_600,], output)
mod['func_650'] = func_650
mod = relay.transform.InferType()(mod)
mutated_mod['func_650'] = func_650
mutated_mod = relay.transform.InferType()(mutated_mod)
func_650_call = mutated_mod.get_global_var('func_650')
var_652 = relay.var("var_652", dtype = "float64", shape = (6, 3, 6))#candidate|652|(6, 3, 6)|var|float64
var_653 = relay.var("var_653", dtype = "float64", shape = (6, 3, 6))#candidate|653|(6, 3, 6)|var|float64
call_651 = func_650_call(var_652,var_653,)
output = call_651
func_654 = relay.Function([var_652,var_653,], output)
mutated_mod['func_654'] = func_654
mutated_mod = relay.transform.InferType()(mutated_mod)
func_536_call = mod.get_global_var('func_536')
func_537_call = mutated_mod.get_global_var('func_537')
call_705 = relay.TupleGetItem(func_536_call(), 3)
call_706 = relay.TupleGetItem(func_537_call(), 3)
uop_711 = relay.rsqrt(call_705.astype('float32')) # shape=(9, 9, 13)
uop_713 = relay.rsqrt(call_706.astype('float32')) # shape=(9, 9, 13)
output = relay.Tuple([uop_711,])
output2 = relay.Tuple([uop_713,])
func_715 = relay.Function([], output)
mod['func_715'] = func_715
mod = relay.transform.InferType()(mod)
output = func_715()
func_716 = relay.Function([], output)
mutated_mod['func_716'] = func_716
mutated_mod = relay.transform.InferType()(mutated_mod)
func_468_call = mod.get_global_var('func_468')
func_470_call = mutated_mod.get_global_var('func_470')
call_743 = relay.TupleGetItem(func_468_call(), 2)
call_744 = relay.TupleGetItem(func_470_call(), 2)
func_573_call = mod.get_global_var('func_573')
func_575_call = mutated_mod.get_global_var('func_575')
call_751 = func_573_call()
call_752 = func_573_call()
func_715_call = mod.get_global_var('func_715')
func_716_call = mutated_mod.get_global_var('func_716')
call_758 = relay.TupleGetItem(func_715_call(), 0)
call_759 = relay.TupleGetItem(func_716_call(), 0)
uop_762 = relay.sqrt(call_743.astype('float32')) # shape=(9, 9, 13)
uop_764 = relay.sqrt(call_744.astype('float32')) # shape=(9, 9, 13)
func_363_call = mod.get_global_var('func_363')
func_364_call = mutated_mod.get_global_var('func_364')
call_768 = relay.TupleGetItem(func_363_call(), 0)
call_769 = relay.TupleGetItem(func_364_call(), 0)
var_772 = relay.var("var_772", dtype = "float32", shape = (9, 9, 13))#candidate|772|(9, 9, 13)|var|float32
bop_773 = relay.less(uop_762.astype('bool'), relay.reshape(var_772.astype('bool'), relay.shape_of(uop_762))) # shape=(9, 9, 13)
bop_776 = relay.less(uop_764.astype('bool'), relay.reshape(var_772.astype('bool'), relay.shape_of(uop_764))) # shape=(9, 9, 13)
output = relay.Tuple([call_751,call_758,call_768,bop_773,])
output2 = relay.Tuple([call_752,call_759,call_769,bop_776,])
func_799 = relay.Function([var_772,], output)
mod['func_799'] = func_799
mod = relay.transform.InferType()(mod)
mutated_mod['func_799'] = func_799
mutated_mod = relay.transform.InferType()(mutated_mod)
var_800 = relay.var("var_800", dtype = "float32", shape = (9, 9, 13))#candidate|800|(9, 9, 13)|var|float32
func_799_call = mutated_mod.get_global_var('func_799')
call_801 = func_799_call(var_800)
output = call_801
func_802 = relay.Function([var_800], output)
mutated_mod['func_802'] = func_802
mutated_mod = relay.transform.InferType()(mutated_mod)
func_363_call = mod.get_global_var('func_363')
func_364_call = mutated_mod.get_global_var('func_364')
call_897 = relay.TupleGetItem(func_363_call(), 0)
call_898 = relay.TupleGetItem(func_364_call(), 0)
func_468_call = mod.get_global_var('func_468')
func_470_call = mutated_mod.get_global_var('func_470')
call_899 = relay.TupleGetItem(func_468_call(), 0)
call_900 = relay.TupleGetItem(func_470_call(), 0)
func_650_call = mod.get_global_var('func_650')
func_654_call = mutated_mod.get_global_var('func_654')
var_920 = relay.var("var_920", dtype = "float64", shape = (3, 36))#candidate|920|(3, 36)|var|float64
call_919 = relay.TupleGetItem(func_650_call(relay.reshape(var_920.astype('float64'), [6, 3, 6]), relay.reshape(var_920.astype('float64'), [6, 3, 6]), ), 1)
call_921 = relay.TupleGetItem(func_654_call(relay.reshape(var_920.astype('float64'), [6, 3, 6]), relay.reshape(var_920.astype('float64'), [6, 3, 6]), ), 1)
bop_931 = relay.multiply(call_899.astype('uint64'), relay.reshape(call_897.astype('uint64'), relay.shape_of(call_899))) # shape=(9, 9, 13)
bop_934 = relay.multiply(call_900.astype('uint64'), relay.reshape(call_898.astype('uint64'), relay.shape_of(call_900))) # shape=(9, 9, 13)
func_715_call = mod.get_global_var('func_715')
func_716_call = mutated_mod.get_global_var('func_716')
call_950 = relay.TupleGetItem(func_715_call(), 0)
call_951 = relay.TupleGetItem(func_716_call(), 0)
func_468_call = mod.get_global_var('func_468')
func_470_call = mutated_mod.get_global_var('func_470')
call_954 = relay.TupleGetItem(func_468_call(), 2)
call_955 = relay.TupleGetItem(func_470_call(), 2)
func_573_call = mod.get_global_var('func_573')
func_575_call = mutated_mod.get_global_var('func_575')
call_965 = func_573_call()
call_966 = func_573_call()
var_975 = relay.var("var_975", dtype = "float64", shape = (3, 36))#candidate|975|(3, 36)|var|float64
bop_976 = relay.equal(var_920.astype('bool'), relay.reshape(var_975.astype('bool'), relay.shape_of(var_920))) # shape=(3, 36)
func_715_call = mod.get_global_var('func_715')
func_716_call = mutated_mod.get_global_var('func_716')
call_986 = relay.TupleGetItem(func_715_call(), 0)
call_987 = relay.TupleGetItem(func_716_call(), 0)
func_468_call = mod.get_global_var('func_468')
func_470_call = mutated_mod.get_global_var('func_470')
call_990 = relay.TupleGetItem(func_468_call(), 3)
call_991 = relay.TupleGetItem(func_470_call(), 3)
var_1003 = relay.var("var_1003", dtype = "float32", shape = (9, 9, 13))#candidate|1003|(9, 9, 13)|var|float32
bop_1004 = relay.greater(call_986.astype('bool'), relay.reshape(var_1003.astype('bool'), relay.shape_of(call_986))) # shape=(9, 9, 13)
bop_1007 = relay.greater(call_987.astype('bool'), relay.reshape(var_1003.astype('bool'), relay.shape_of(call_987))) # shape=(9, 9, 13)
func_433_call = mod.get_global_var('func_433')
func_434_call = mutated_mod.get_global_var('func_434')
call_1016 = func_433_call()
call_1017 = func_433_call()
func_433_call = mod.get_global_var('func_433')
func_434_call = mutated_mod.get_global_var('func_434')
call_1019 = func_433_call()
call_1020 = func_433_call()
func_536_call = mod.get_global_var('func_536')
func_537_call = mutated_mod.get_global_var('func_537')
call_1026 = relay.TupleGetItem(func_536_call(), 2)
call_1027 = relay.TupleGetItem(func_537_call(), 2)
output = relay.Tuple([call_919,bop_931,call_950,call_954,call_965,bop_976,call_990,bop_1004,call_1016,call_1019,call_1026,])
output2 = relay.Tuple([call_921,bop_934,call_951,call_955,call_966,bop_976,call_991,bop_1007,call_1017,call_1020,call_1027,])
func_1037 = relay.Function([var_920,var_975,var_1003,], output)
mod['func_1037'] = func_1037
mod = relay.transform.InferType()(mod)
var_1038 = relay.var("var_1038", dtype = "float64", shape = (3, 36))#candidate|1038|(3, 36)|var|float64
var_1039 = relay.var("var_1039", dtype = "float64", shape = (3, 36))#candidate|1039|(3, 36)|var|float64
var_1040 = relay.var("var_1040", dtype = "float32", shape = (9, 9, 13))#candidate|1040|(9, 9, 13)|var|float32
output = func_1037(var_1038,var_1039,var_1040,)
func_1041 = relay.Function([var_1038,var_1039,var_1040,], output)
mutated_mod['func_1041'] = func_1041
mutated_mod = relay.transform.InferType()(mutated_mod)
func_573_call = mod.get_global_var('func_573')
func_575_call = mutated_mod.get_global_var('func_575')
call_1051 = func_573_call()
call_1052 = func_573_call()
output = call_1051
output2 = call_1052
func_1064 = relay.Function([], output)
mod['func_1064'] = func_1064
mod = relay.transform.InferType()(mod)
mutated_mod['func_1064'] = func_1064
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1064_call = mutated_mod.get_global_var('func_1064')
call_1065 = func_1064_call()
output = call_1065
func_1066 = relay.Function([], output)
mutated_mod['func_1066'] = func_1066
mutated_mod = relay.transform.InferType()(mutated_mod)
func_433_call = mod.get_global_var('func_433')
func_434_call = mutated_mod.get_global_var('func_434')
call_1098 = func_433_call()
call_1099 = func_433_call()
const_1100 = relay.const([[[5.877415,-5.069771,-2.632266,4.605683,-5.009831,4.320562,-4.307641,-3.927927,-1.654073,-9.153515,-5.612421,9.122467,9.234458],[-3.459785,0.413895,-5.208190,-1.404425,9.204275,9.113475,8.987131,4.038338,7.933828,5.840680,0.176578,1.847351,9.917362],[5.950015,1.639708,-3.344559,6.866197,9.058304,-9.117990,-0.363995,-6.431219,-3.939092,5.789194,-6.702205,-3.470038,-5.105556],[0.066724,2.321537,7.948728,3.329460,-5.558388,-7.835035,3.339790,6.751565,0.875272,-4.817493,4.011449,2.947864,-9.611621],[8.967735,-0.229055,-4.593715,-2.154498,-0.967986,2.743718,-7.887080,8.422080,3.119175,-9.918749,8.179629,-6.576565,6.682650],[-8.837859,-7.825003,-3.576636,7.312388,2.269586,-1.729628,-1.647231,-0.974313,-7.958540,5.964426,9.526741,-3.379398,5.413927],[-2.107158,6.193830,7.461528,-8.098236,-3.453778,-6.462933,1.916941,-2.077637,0.743080,6.976487,-9.376799,-8.040556,6.832859],[-9.125217,2.239470,5.646268,6.323980,8.296214,9.028025,-8.680684,-4.714262,6.251405,-3.102334,7.417979,-8.017722,3.594814],[-4.381133,-8.818886,-8.581881,9.440087,-1.577898,4.234647,-7.162742,0.582644,-4.396363,7.082366,-5.740864,2.947738,-6.998432]],[[-4.403580,9.481217,7.405503,9.999258,7.637745,-8.710522,4.360265,-3.438502,-7.797491,3.981379,-1.109822,0.855317,-0.164035],[-0.759821,1.542404,-0.047175,-5.744379,0.168263,8.627387,8.113436,-3.734525,9.260735,8.078382,-7.252086,-3.483227,0.010982],[-0.532578,3.560119,-0.311311,-3.303406,-5.728650,5.099401,-4.045006,3.730854,7.218037,-3.071159,-5.785098,6.335549,3.626101],[-8.402497,8.712061,-9.995760,-5.919659,-8.109570,-0.179310,-9.622057,6.173095,4.163023,1.664730,7.910362,3.187503,-4.842235],[4.339012,0.656298,-8.021250,6.902188,9.495476,1.643851,2.901134,-9.275506,-3.416124,-9.967942,-2.150439,3.843869,-3.165443],[-1.669942,-5.259962,-2.240347,-7.261351,8.963375,4.665467,-8.792908,-3.516608,-9.215513,7.131777,3.039598,-3.079469,5.534487],[9.710235,-5.837698,6.029150,-6.426474,3.621689,-1.171288,-2.409302,-1.940285,-7.653596,6.966238,-7.650407,-1.277310,-2.118283],[3.785310,3.369002,-3.410148,4.450893,8.185466,8.821056,6.121465,-2.801169,4.082939,7.257726,-4.305963,-4.715530,-0.692587],[0.349975,7.756017,3.230905,-6.315023,1.044001,0.896329,1.325643,-9.315291,-5.133765,-7.481588,2.823750,-4.353795,5.807818]],[[-1.973625,-9.406373,6.036319,3.700570,9.320339,6.976518,7.950771,-1.511642,-8.680445,5.252255,1.346158,-8.890466,-4.499651],[3.016740,-0.089131,0.897112,-0.025165,4.480720,-5.948189,-9.920540,0.733066,2.431541,0.081173,-4.151475,-6.144317,-3.451101],[5.490591,9.307217,-2.137157,-4.852202,6.604838,0.176969,3.968572,3.405193,5.926974,-5.665498,-5.435781,1.283994,4.938501],[7.621794,-8.640814,0.596428,-6.127690,4.794869,4.673069,8.733790,-8.524485,5.664607,6.325488,9.808524,-5.717598,-8.650773],[7.569771,-3.431917,1.052131,-9.417493,2.289987,4.186783,-6.322642,-5.003803,2.348689,3.713213,-6.372273,8.657245,3.279505],[-1.591508,-2.740312,-7.429139,1.576309,2.552123,-8.829366,-5.644015,0.031740,9.848946,-2.667717,-5.147575,8.288078,4.047196],[-6.552404,-4.075774,8.044873,9.281839,7.355778,-5.070644,5.426774,7.694749,6.736251,4.612002,8.523403,9.421557,3.891385],[6.152408,1.371686,-9.510963,-6.561382,2.995928,-3.450266,4.311090,5.571095,-7.291258,1.354794,-2.783425,5.958754,-4.892619],[3.626537,-7.859455,6.137985,6.619617,6.336581,-5.483469,-2.636024,3.210126,-4.563606,-2.626742,-9.986771,-2.256347,-3.283417]],[[6.139858,1.168558,5.191009,3.682631,3.744583,0.625496,9.220182,-2.520992,-0.836498,5.137480,0.205609,1.919703,9.726746],[-6.623625,5.620471,5.562539,-4.169674,-8.338118,2.864092,-7.058515,-2.005132,9.035230,-9.422248,4.344622,7.704891,-9.938866],[9.633598,-2.404633,-7.404118,-2.589848,-4.524320,-5.862162,-2.231852,-6.783617,-6.901771,-3.001843,-0.553704,-4.008651,-0.035254],[-1.289889,-1.104415,-7.003304,-5.452503,9.150194,-0.189308,-3.045955,8.889435,9.946362,-0.533407,1.885964,-0.144758,5.263480],[2.631477,6.082459,-1.748504,1.167949,1.874560,-6.771725,2.276008,-2.953539,1.841111,-1.769296,8.178222,8.849403,3.260859],[-1.418354,-0.519885,-0.686188,2.497431,6.614992,1.416631,-1.407974,8.787094,-0.489097,-0.869336,-6.880169,-4.527651,-8.853715],[-1.969970,1.610052,-6.208124,-7.973253,8.745219,7.069650,-4.803815,-2.706508,1.017592,-9.702643,3.953261,5.031806,1.282592],[-1.270998,-7.921606,2.337320,-6.897011,-9.648717,-5.148550,7.924196,-7.584546,-8.217397,-4.062793,-2.884357,-4.053106,-1.761764],[-5.922544,6.998348,4.871604,0.265800,0.685995,-4.694222,0.493652,-7.718958,2.599397,9.895022,-2.267885,0.663666,3.573979]],[[3.426679,-5.161353,0.334086,0.287037,6.922217,-3.798204,8.389274,4.441733,6.692645,-1.887383,4.485716,-5.276612,2.351053],[-6.188944,2.422569,7.918403,5.529231,-9.359321,-4.967673,-2.874725,-1.844551,-6.753756,-3.496244,5.488984,-7.744216,0.497470],[-9.173397,-0.945701,1.042054,-3.881600,-0.884381,5.638316,2.297536,6.417575,5.723987,8.288426,-9.408427,4.386666,-0.990403],[0.672769,3.563891,-6.194134,-1.406287,2.102936,5.292217,-2.430496,4.194290,-8.916130,4.981441,-2.794489,1.066696,-2.122806],[7.598047,-7.861404,-1.102695,-8.877880,-2.804491,7.565431,-3.878294,-6.821572,-9.146687,7.289086,-4.413719,4.962311,2.091257],[4.117156,4.464385,8.489532,1.772173,-6.675209,3.899410,4.747263,3.235888,-2.227048,-0.494067,-3.439800,7.594858,-1.686387],[7.323923,3.996271,-8.073146,2.369201,-3.491124,-7.179667,-3.125261,8.937191,-4.935814,7.713296,-9.567271,3.447544,5.327244],[5.654652,8.384626,-7.408270,8.484618,-9.445970,-3.739358,-8.673450,-2.255211,1.930716,2.859996,-5.705923,0.363823,-6.007893],[9.479294,-3.232688,7.550423,8.427391,-8.279614,7.983155,2.373679,2.648732,3.235144,-3.479233,-0.644694,-8.904285,-4.462829]],[[9.963335,-9.246772,0.265430,6.058492,-0.478470,-7.126168,-6.050583,-7.765635,-5.287630,7.403783,2.143818,9.217012,-0.328699],[3.684025,-4.425142,6.112281,-2.031468,1.919842,9.783729,8.024186,3.473091,4.416575,-5.909694,2.496296,2.124009,-6.172822],[4.739101,-3.066013,-2.972847,-2.741475,2.606647,-3.872518,1.221625,-0.757549,5.269870,4.969483,2.123059,-5.075920,-0.931527],[-1.888486,-0.421694,-9.790555,4.452406,3.978503,1.853921,-0.103974,8.530286,-6.095325,-2.639159,0.092765,-8.316156,-1.470755],[5.036421,-0.761225,-2.126154,1.861570,4.986871,-2.340536,-6.601981,-7.606434,9.522861,-1.657416,-6.864899,5.270415,8.621141],[-0.754858,9.405938,3.251774,5.689470,-2.132999,0.349224,-9.329331,-2.258560,2.053308,-5.806191,-8.656311,-0.122634,-1.204008],[9.419327,1.846519,-0.798211,-3.061118,-1.311920,-4.339097,0.064613,9.977987,-7.287923,-0.779790,-6.886060,5.585731,8.659083],[-1.859492,-4.163085,-7.078690,-2.769055,8.877688,6.583833,1.317324,1.410314,5.384988,-1.944959,1.083714,-0.343483,9.719744],[8.787193,6.731406,-1.096296,-7.461523,-6.870873,-1.746293,-6.155349,8.235758,-6.931903,9.412906,-4.195913,-9.824731,1.388086]],[[8.159758,8.079214,-3.980759,4.599861,-2.526266,7.444831,4.819733,3.272761,1.067092,5.247053,-2.975177,7.608029,9.418968],[-3.987429,-9.303543,-7.942254,-3.378349,3.495567,-1.231952,-6.819724,-6.501536,-3.677976,-7.718624,-1.282842,6.875046,-4.341704],[2.378146,-4.623000,-1.499193,-9.490332,-4.611798,-5.922401,6.557329,-7.539205,4.639902,-5.991473,-0.940695,3.708658,-1.910203],[-5.838636,3.581420,2.890744,-8.469525,3.381136,5.980346,-6.568957,-8.997771,-5.592910,-8.911420,-2.178089,3.071445,8.148467],[7.284714,-4.758437,-1.374952,4.773377,-9.113184,-2.124735,-6.125406,8.655148,-4.298996,-5.470744,-8.383728,-0.529486,2.089112],[-0.862881,0.235133,-8.838375,-5.459350,-6.398391,-7.213712,-1.811135,9.808586,0.723290,7.077797,2.301245,-9.786783,-3.191871],[-9.804792,6.363839,7.675566,-0.005154,-2.974213,1.661793,-2.130099,5.496913,-9.117378,5.797286,1.964163,1.473730,0.827857],[-9.422854,-0.512177,-9.946829,3.001291,-4.733894,-2.453008,2.593433,-0.537894,6.855324,-4.911238,2.191430,9.846551,-7.793580],[6.278545,2.278240,-1.495924,4.165584,-3.633729,9.899886,2.194651,8.957493,2.828788,-0.733941,4.825551,-8.218058,9.661621]],[[-2.330495,-3.362057,4.091701,2.404893,-2.822406,-0.860997,-0.074097,6.426561,-8.181345,-8.365200,-8.958059,-2.976075,1.483460],[1.367043,9.922286,7.323002,8.524557,0.862090,3.866950,3.386027,-5.357544,3.072563,-6.002387,5.631489,-9.571815,-8.424892],[6.891442,8.182030,6.607996,-2.346007,1.333113,-8.292005,1.759670,1.543291,-9.631223,-9.164739,-9.161441,-1.715449,-2.671483],[3.917726,4.358855,-5.809771,-5.547170,6.636608,-7.506860,2.343973,8.122393,-5.402350,0.316119,1.069297,-0.062379,-6.132590],[-9.081701,1.708157,-0.693132,8.022887,8.344955,-0.900706,2.827401,4.671382,3.792786,-0.709954,-9.131494,4.177729,-9.541151],[-6.608423,-9.572405,-0.524215,5.511568,-8.690384,-2.974405,7.064689,7.360980,-6.318601,9.689513,-0.220570,-0.073969,2.582357],[0.847130,-7.555608,6.707207,-4.396777,0.189768,-7.454277,-6.909920,5.092359,-2.190501,-9.435614,-7.180614,6.885842,-4.894860],[4.167066,-2.818808,-0.208763,7.975267,7.102051,4.522688,0.510946,-7.580797,0.021944,-8.196495,-0.313078,3.332001,-3.846294],[6.126259,9.344322,9.114229,-7.481625,9.882454,6.533098,2.753138,2.636051,-1.718933,0.191014,9.357496,6.398108,9.882228]],[[-9.315511,7.922192,0.458651,-7.559260,-0.624122,9.042335,0.004000,8.765729,7.992802,-0.283546,1.815098,6.136684,4.151488],[5.031018,-5.495939,-7.641772,1.315410,5.155640,-3.165155,4.058947,6.785547,6.731482,3.602849,4.987804,4.463589,-2.319256],[-0.448197,-3.703076,-3.404221,0.937268,-8.610043,5.554196,4.243956,-1.653651,5.246606,-7.462058,-1.855174,0.555645,6.408805],[8.179138,-7.565513,5.811808,2.602031,0.436110,-1.572594,3.294533,-4.796660,-3.974120,7.778400,-3.203921,8.742109,-1.401900],[-6.834036,4.163951,-8.478927,8.273759,-3.798697,-5.576222,-1.131958,8.236380,-3.962807,4.892769,-9.569429,-1.577269,1.380158],[-6.460592,9.437822,-1.063577,-4.390345,8.742631,-3.516289,-1.128424,-4.523591,1.961584,-6.505092,1.043634,9.676883,6.731615],[-4.489653,8.358835,-6.387331,-0.969378,-4.487156,-1.592249,4.392960,-5.833891,-3.399764,-5.148588,9.943518,2.601780,4.338622],[-0.190708,0.121131,-6.439170,6.917602,3.694951,3.580546,2.761373,2.516149,-6.737383,-5.150002,-6.292773,0.529464,5.706410],[-2.174107,-7.252554,2.046287,-7.356466,6.660000,-3.485195,7.718383,-2.875788,-4.332058,-2.173940,8.603040,-5.216100,9.065986]]], dtype = "float32")#candidate|1100|(9, 9, 13)|const|float32
bop_1101 = relay.left_shift(call_1098.astype('int32'), relay.reshape(const_1100.astype('int32'), relay.shape_of(call_1098))) # shape=(9, 9, 13)
bop_1104 = relay.left_shift(call_1099.astype('int32'), relay.reshape(const_1100.astype('int32'), relay.shape_of(call_1099))) # shape=(9, 9, 13)
output = relay.Tuple([bop_1101,])
output2 = relay.Tuple([bop_1104,])
func_1115 = relay.Function([], output)
mod['func_1115'] = func_1115
mod = relay.transform.InferType()(mod)
output = func_1115()
func_1116 = relay.Function([], output)
mutated_mod['func_1116'] = func_1116
mutated_mod = relay.transform.InferType()(mutated_mod)
func_573_call = mod.get_global_var('func_573')
func_575_call = mutated_mod.get_global_var('func_575')
call_1128 = func_573_call()
call_1129 = func_573_call()
func_433_call = mod.get_global_var('func_433')
func_434_call = mutated_mod.get_global_var('func_434')
call_1133 = func_433_call()
call_1134 = func_433_call()
var_1136 = relay.var("var_1136", dtype = "float32", shape = (9, 9, 13))#candidate|1136|(9, 9, 13)|var|float32
bop_1137 = relay.bitwise_or(call_1133.astype('int64'), relay.reshape(var_1136.astype('int64'), relay.shape_of(call_1133))) # shape=(9, 9, 13)
bop_1140 = relay.bitwise_or(call_1134.astype('int64'), relay.reshape(var_1136.astype('int64'), relay.shape_of(call_1134))) # shape=(9, 9, 13)
func_363_call = mod.get_global_var('func_363')
func_364_call = mutated_mod.get_global_var('func_364')
call_1142 = relay.TupleGetItem(func_363_call(), 2)
call_1143 = relay.TupleGetItem(func_364_call(), 2)
output = relay.Tuple([call_1128,bop_1137,call_1142,])
output2 = relay.Tuple([call_1129,bop_1140,call_1143,])
func_1146 = relay.Function([var_1136,], output)
mod['func_1146'] = func_1146
mod = relay.transform.InferType()(mod)
mutated_mod['func_1146'] = func_1146
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1147 = relay.var("var_1147", dtype = "float32", shape = (9, 9, 13))#candidate|1147|(9, 9, 13)|var|float32
func_1146_call = mutated_mod.get_global_var('func_1146')
call_1148 = func_1146_call(var_1147)
output = call_1148
func_1149 = relay.Function([var_1147], output)
mutated_mod['func_1149'] = func_1149
mutated_mod = relay.transform.InferType()(mutated_mod)
func_433_call = mod.get_global_var('func_433')
func_434_call = mutated_mod.get_global_var('func_434')
call_1168 = func_433_call()
call_1169 = func_433_call()
output = call_1168
output2 = call_1169
func_1178 = relay.Function([], output)
mod['func_1178'] = func_1178
mod = relay.transform.InferType()(mod)
mutated_mod['func_1178'] = func_1178
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1178_call = mutated_mod.get_global_var('func_1178')
call_1179 = func_1178_call()
output = call_1179
func_1180 = relay.Function([], output)
mutated_mod['func_1180'] = func_1180
mutated_mod = relay.transform.InferType()(mutated_mod)
func_363_call = mod.get_global_var('func_363')
func_364_call = mutated_mod.get_global_var('func_364')
call_1192 = relay.TupleGetItem(func_363_call(), 0)
call_1193 = relay.TupleGetItem(func_364_call(), 0)
func_715_call = mod.get_global_var('func_715')
func_716_call = mutated_mod.get_global_var('func_716')
call_1195 = relay.TupleGetItem(func_715_call(), 0)
call_1196 = relay.TupleGetItem(func_716_call(), 0)
bop_1197 = relay.not_equal(call_1195.astype('bool'), relay.reshape(call_1192.astype('bool'), relay.shape_of(call_1195))) # shape=(9, 9, 13)
bop_1200 = relay.not_equal(call_1196.astype('bool'), relay.reshape(call_1193.astype('bool'), relay.shape_of(call_1196))) # shape=(9, 9, 13)
func_292_call = mod.get_global_var('func_292')
func_294_call = mutated_mod.get_global_var('func_294')
call_1204 = relay.TupleGetItem(func_292_call(), 0)
call_1205 = relay.TupleGetItem(func_294_call(), 0)
func_536_call = mod.get_global_var('func_536')
func_537_call = mutated_mod.get_global_var('func_537')
call_1227 = relay.TupleGetItem(func_536_call(), 1)
call_1228 = relay.TupleGetItem(func_537_call(), 1)
bop_1230 = relay.floor_divide(call_1192.astype('float32'), relay.reshape(call_1195.astype('float32'), relay.shape_of(call_1192))) # shape=(9, 9, 13)
bop_1233 = relay.floor_divide(call_1193.astype('float32'), relay.reshape(call_1196.astype('float32'), relay.shape_of(call_1193))) # shape=(9, 9, 13)
bop_1244 = relay.logical_xor(call_1195.astype('int16'), relay.reshape(call_1227.astype('int16'), relay.shape_of(call_1195))) # shape=(9, 9, 13)
bop_1247 = relay.logical_xor(call_1196.astype('int16'), relay.reshape(call_1228.astype('int16'), relay.shape_of(call_1196))) # shape=(9, 9, 13)
output = relay.Tuple([bop_1197,call_1204,bop_1230,bop_1244,])
output2 = relay.Tuple([bop_1200,call_1205,bop_1233,bop_1247,])
func_1249 = relay.Function([], output)
mod['func_1249'] = func_1249
mod = relay.transform.InferType()(mod)
mutated_mod['func_1249'] = func_1249
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1249_call = mutated_mod.get_global_var('func_1249')
call_1250 = func_1249_call()
output = call_1250
func_1251 = relay.Function([], output)
mutated_mod['func_1251'] = func_1251
mutated_mod = relay.transform.InferType()(mutated_mod)
func_292_call = mod.get_global_var('func_292')
func_294_call = mutated_mod.get_global_var('func_294')
call_1267 = relay.TupleGetItem(func_292_call(), 1)
call_1268 = relay.TupleGetItem(func_294_call(), 1)
uop_1275 = relay.log10(call_1267.astype('float64')) # shape=(9, 9, 13)
uop_1277 = relay.log10(call_1268.astype('float64')) # shape=(9, 9, 13)
uop_1284 = relay.sigmoid(uop_1275.astype('float64')) # shape=(9, 9, 13)
uop_1286 = relay.sigmoid(uop_1277.astype('float64')) # shape=(9, 9, 13)
bop_1288 = relay.floor_mod(uop_1275.astype('float32'), relay.reshape(call_1267.astype('float32'), relay.shape_of(uop_1275))) # shape=(9, 9, 13)
bop_1291 = relay.floor_mod(uop_1277.astype('float32'), relay.reshape(call_1268.astype('float32'), relay.shape_of(uop_1277))) # shape=(9, 9, 13)
output = relay.Tuple([uop_1284,bop_1288,])
output2 = relay.Tuple([uop_1286,bop_1291,])
func_1303 = relay.Function([], output)
mod['func_1303'] = func_1303
mod = relay.transform.InferType()(mod)
output = func_1303()
func_1304 = relay.Function([], output)
mutated_mod['func_1304'] = func_1304
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1364 = relay.const([[[2.660378,-1.116524,-2.086004,-3.903776,1.297608,-3.743834,9.441540,8.333855,0.271660,-6.754242,6.247947,4.053227],[-1.851882,-7.949751,-3.880478,-9.620921,-0.410097,-7.296582,-0.200911,0.344379,8.128638,2.068138,9.256776,-5.329878],[-8.555758,9.544201,3.633269,8.005578,7.388638,1.092304,-5.022160,-8.609172,-0.002343,1.932689,6.721416,-1.307653],[8.466570,-7.754437,-9.188981,6.853738,6.311867,5.087865,4.901525,-0.710209,-8.610543,1.701913,-3.066657,8.794169],[-8.952800,1.387948,8.245111,-8.512231,9.410278,-7.396271,5.810687,-2.537132,-4.275521,2.104918,2.817454,7.044242],[7.990166,-8.974611,-8.884101,-3.585888,-3.632276,-3.640409,7.284915,-7.194868,4.305903,7.314218,-7.907129,2.054563],[8.954821,6.628054,3.466177,-6.588439,8.341646,-2.961053,-5.588694,-5.771504,-1.307171,-3.400308,9.925302,1.758036]],[[2.878245,7.455560,-1.812368,2.089725,0.813934,-0.257555,3.455109,-8.976695,7.113563,-0.089359,9.223650,1.592104],[7.985742,-0.332396,-2.640956,-0.669556,-0.113448,-3.623173,-2.548763,-3.692214,-5.957947,-1.069167,3.720864,-1.867343],[8.288812,-9.636899,2.017559,1.479737,2.467468,0.198484,3.274643,-5.353174,8.073076,-9.166032,-2.513621,2.988069],[-4.836453,-2.056110,-0.840678,-9.429788,6.863726,7.664270,-5.406989,4.397534,-3.700545,-2.607237,-9.945479,9.328293],[8.155416,-6.477606,-4.957035,-0.954350,0.227141,-5.161522,5.753072,-3.681491,7.337957,7.851673,-5.521313,2.816016],[7.031419,-7.378027,-1.499903,7.930484,7.083912,5.823065,6.679396,-9.032991,-5.867075,2.724682,-0.589886,-6.354275],[5.159470,1.593086,7.812435,-3.808312,-5.600406,-2.426079,-1.556980,-9.113882,9.857543,6.782199,1.827157,-4.525877]],[[-0.928118,8.837577,7.004846,-9.837837,1.066623,-3.730242,-2.443931,9.545080,6.833181,-1.018171,3.580855,3.438587],[-7.267464,-9.327061,3.137241,-5.800395,-9.073187,-6.824849,9.039088,-2.907408,-1.448647,0.190732,7.438053,-9.217960],[1.854052,-9.598737,7.462242,0.356606,-8.245646,-9.010758,-9.658180,0.835351,-6.980719,-7.388994,-0.793620,4.304140],[9.708734,5.796110,0.736119,5.546594,-9.227144,-8.958114,-2.905849,-6.118603,3.179973,-2.617344,9.087445,-9.647724],[8.405929,0.969070,6.979074,-7.415561,-4.196737,3.350120,1.856585,-2.795129,-8.349486,-3.102513,-5.062779,2.681228],[6.652248,-5.251166,6.251039,-2.903407,5.826394,-9.591914,-4.099478,-8.336766,-6.408018,6.974422,-2.879661,-6.555651],[-1.954725,6.757758,1.765663,-1.408884,-6.607016,0.996226,6.150813,-6.523649,2.565586,1.955550,-2.166738,-3.609559]],[[7.840346,-0.365694,7.158075,-3.161705,0.376132,5.961601,-0.554621,0.340243,-9.249783,-5.463792,6.015580,-6.013286],[6.465244,-7.207415,3.280672,-8.644904,-6.401641,0.709970,2.286707,5.157132,8.684428,9.812130,-2.373425,0.235931],[0.717492,-7.950877,-3.454397,-7.524496,-9.730352,5.266902,9.790995,-5.601588,2.520810,-1.797447,2.414469,0.550034],[-2.524852,-7.980116,-8.617322,3.648427,5.623268,-9.019814,-8.851030,5.384163,1.010970,7.510777,7.488467,2.905598],[6.831266,8.746739,9.768059,4.202494,-3.951672,9.619689,3.368213,-0.283071,-2.160820,5.291378,8.084428,-7.007048],[9.608334,-5.316050,6.057069,0.626999,7.007313,-3.425579,-9.375503,-3.181444,4.919730,0.981428,-4.583275,-7.964489],[-9.304019,1.870260,-7.427712,-4.716557,3.806963,-2.133648,-1.446383,2.107213,1.435464,2.731080,-8.767675,-7.214763]],[[1.125307,-0.836988,7.116634,-2.302012,-6.308840,-0.862190,5.414501,1.077839,5.031434,-3.822614,9.731793,2.283275],[6.051045,-4.774444,-5.035797,5.835688,-6.092057,5.149709,-9.668390,0.338122,1.272142,-2.923646,5.396336,-5.884862],[3.830219,-7.777551,-4.393841,5.976403,-3.433375,6.711582,-8.359810,-1.748767,8.044699,2.736885,-1.031354,-8.898554],[-3.352098,-2.029069,-7.119056,-9.397588,3.303255,4.048584,-9.788446,4.448914,-0.974859,8.057690,-0.241746,-6.482292],[2.304034,0.758749,-0.183518,0.287679,-3.209378,-3.937485,-5.811932,6.084027,-3.229479,-6.844344,4.812106,6.416815],[-5.967101,3.740162,9.894740,-1.363827,5.011090,-1.911366,-6.693694,-4.664007,2.599852,7.068741,5.606922,-1.681519],[5.875267,-6.702726,-9.295226,7.746019,-5.031548,3.390382,-5.293026,-4.852832,-7.411887,4.907261,-5.877973,9.344350]],[[1.716583,-5.737353,8.803717,-8.305411,1.496687,-3.319090,-6.223514,-1.801914,-8.128178,-7.778156,-8.334440,-2.844619],[2.049086,8.466738,7.980746,-1.702349,0.056338,1.126524,1.619559,-3.893450,-9.829294,-2.307748,-3.028739,3.610227],[0.258820,7.470788,-0.501291,-0.946816,3.963891,1.220172,-4.904058,2.987094,-8.971638,5.270479,-3.143256,-9.365481],[-4.050973,-2.609566,-9.912847,9.250121,0.124178,2.242806,-2.184750,-7.259169,5.714015,-1.950781,2.757684,3.781682],[-7.895019,4.247463,-9.061152,6.658970,-8.720235,9.169082,8.378433,-0.449901,6.704680,-4.551803,4.306080,-8.704526],[-7.160474,4.069462,-2.951558,-4.650599,8.478561,-1.709636,0.524409,-9.305903,9.765557,-3.468101,-3.674578,4.221273],[-4.147575,0.766169,-8.463927,-0.202211,-5.914419,-4.951162,6.256255,3.290506,-3.689858,-5.853626,7.316545,-9.685586]],[[0.764099,4.975010,1.767160,5.910345,-8.456897,-8.584126,-0.165301,6.482248,-8.380148,-4.117294,-2.478446,-8.884485],[7.140006,8.779381,1.257312,9.674840,-3.331365,-6.962710,4.464346,-5.956911,-1.616745,1.785708,7.009828,0.629352],[-6.806964,5.492092,2.594469,-5.555286,4.680214,3.514848,3.026467,2.561986,8.866599,1.197690,4.312111,-7.355620],[-3.985669,5.917744,-7.269106,3.009180,-8.354426,-4.640652,-4.920208,-2.127425,-4.980963,-1.733277,-9.363558,1.088986],[4.307124,-5.126372,-8.996366,-0.380357,-9.381805,5.215651,-1.493993,-1.880204,8.891809,-3.175206,8.093132,3.383992],[-1.802307,7.706281,8.856784,-3.271088,3.192903,-0.369854,6.661570,7.542027,-8.360605,7.895721,4.074313,2.765120],[-9.113904,4.096016,-4.111025,2.994765,-1.741355,5.417802,8.018334,6.091345,-6.423556,4.268991,-2.072801,-0.071101]],[[5.256401,-6.706763,4.953371,6.192704,1.320722,3.446378,-4.863795,1.984503,9.958394,-2.991603,-9.976007,5.454370],[4.051209,9.483100,7.356030,-4.955755,9.259838,-4.591070,-1.679626,-2.820253,-8.387848,5.824471,-4.716097,6.862369],[4.865276,-4.589701,0.891798,1.297113,-2.626987,5.206802,-5.827524,-1.767518,-9.577145,-5.431396,8.585184,-8.139891],[-1.642927,-1.100947,-8.410317,-4.979896,4.478268,-8.231365,-5.653556,-4.835687,-3.498346,5.837043,5.094017,-0.827022],[-4.412694,8.365483,2.640785,5.395195,0.619529,-0.229006,1.791293,-7.745223,8.000000,-0.134859,-4.226676,9.562024],[-6.431191,4.086264,-5.308794,0.812273,-4.084007,-7.776363,-8.781644,2.862650,4.731210,-0.469535,-7.720577,-4.918156],[7.300809,0.679860,9.875859,-3.152361,4.036721,5.603510,5.279695,-3.001296,7.906591,3.856618,-0.522161,-4.241507]],[[-4.101281,4.329997,3.868962,-3.040881,-8.691193,-3.159915,-0.108233,7.418199,-2.278120,-5.247836,8.675190,0.453723],[8.932746,-7.586355,0.060415,-2.209017,3.238758,-2.867057,1.464436,6.968380,-3.013135,8.905993,-3.588999,8.937062],[1.895850,-7.507109,-9.223066,-2.416739,-1.583423,-0.311364,0.584587,1.855551,-5.201064,6.422081,1.878498,1.822650],[-4.985467,-9.162524,3.856595,7.912150,0.441745,2.254098,9.899395,-9.882256,-7.713626,0.302247,3.733081,6.259366],[-8.482526,0.200720,3.130220,4.321466,1.590962,5.684593,7.181009,8.600214,-1.295538,1.978022,-3.260474,-4.231718],[-6.358848,-3.072412,-3.366635,3.293225,-7.376940,-6.671068,8.208786,6.856024,-3.168583,4.423933,9.756774,-4.222518],[0.136310,8.690044,3.588777,-4.476792,3.313356,1.136363,-5.038703,-6.113426,5.129102,7.194751,1.518842,0.508807]],[[2.450230,3.772188,-8.478001,-1.003437,9.974638,9.003723,4.816731,-2.529839,2.408882,3.952925,-8.128658,-3.914109],[-1.920619,-1.159128,8.754420,9.578835,-3.895718,6.387345,2.816296,-1.561810,-0.788394,4.792120,-4.359246,-8.370310],[-4.885815,5.341765,-1.117672,-2.184238,9.253166,-5.356640,0.657078,7.619626,-5.180332,-5.951090,3.422051,9.712502],[-5.758249,0.716142,-3.624670,-6.249074,8.921818,-6.675348,-2.679577,5.855321,2.804229,-6.064579,6.673801,7.575263],[-5.782817,6.337249,-8.471628,2.118411,-7.660037,9.876709,5.703983,4.262231,-7.222185,-4.240721,-2.887921,-2.073555],[2.766314,-3.498870,1.047728,-4.810742,8.603107,1.395639,-6.794329,8.174952,0.484023,-2.315050,-6.743475,-1.860376],[9.194791,5.898365,-2.396838,5.056927,-1.407439,-6.799975,3.454309,-9.704974,3.323176,5.212138,-7.108440,-5.975376]]], dtype = "float64")#candidate|1364|(10, 7, 12)|const|float64
uop_1365 = relay.acos(const_1364.astype('float64')) # shape=(10, 7, 12)
uop_1368 = relay.log(const_1364.astype('float32')) # shape=(10, 7, 12)
uop_1375 = relay.asinh(uop_1365.astype('float64')) # shape=(10, 7, 12)
output = relay.Tuple([uop_1368,uop_1375,])
output2 = relay.Tuple([uop_1368,uop_1375,])
func_1383 = relay.Function([], output)
mod['func_1383'] = func_1383
mod = relay.transform.InferType()(mod)
output = func_1383()
func_1384 = relay.Function([], output)
mutated_mod['func_1384'] = func_1384
mutated_mod = relay.transform.InferType()(mutated_mod)
func_292_call = mod.get_global_var('func_292')
func_294_call = mutated_mod.get_global_var('func_294')
call_1418 = relay.TupleGetItem(func_292_call(), 1)
call_1419 = relay.TupleGetItem(func_294_call(), 1)
var_1458 = relay.var("var_1458", dtype = "float64", shape = (9, 9, 13))#candidate|1458|(9, 9, 13)|var|float64
bop_1459 = relay.power(call_1418.astype('float32'), relay.reshape(var_1458.astype('float32'), relay.shape_of(call_1418))) # shape=(9, 9, 13)
bop_1462 = relay.power(call_1419.astype('float32'), relay.reshape(var_1458.astype('float32'), relay.shape_of(call_1419))) # shape=(9, 9, 13)
output = relay.Tuple([bop_1459,])
output2 = relay.Tuple([bop_1462,])
func_1496 = relay.Function([var_1458,], output)
mod['func_1496'] = func_1496
mod = relay.transform.InferType()(mod)
var_1497 = relay.var("var_1497", dtype = "float64", shape = (9, 9, 13))#candidate|1497|(9, 9, 13)|var|float64
output = func_1496(var_1497)
func_1498 = relay.Function([var_1497], output)
mutated_mod['func_1498'] = func_1498
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1178_call = mod.get_global_var('func_1178')
func_1180_call = mutated_mod.get_global_var('func_1180')
call_1514 = func_1178_call()
call_1515 = func_1178_call()
var_1528 = relay.var("var_1528", dtype = "float32", shape = (9, 9, 13))#candidate|1528|(9, 9, 13)|var|float32
bop_1529 = relay.subtract(call_1514.astype('uint32'), relay.reshape(var_1528.astype('uint32'), relay.shape_of(call_1514))) # shape=(9, 9, 13)
bop_1532 = relay.subtract(call_1515.astype('uint32'), relay.reshape(var_1528.astype('uint32'), relay.shape_of(call_1515))) # shape=(9, 9, 13)
output = relay.Tuple([bop_1529,])
output2 = relay.Tuple([bop_1532,])
func_1537 = relay.Function([var_1528,], output)
mod['func_1537'] = func_1537
mod = relay.transform.InferType()(mod)
mutated_mod['func_1537'] = func_1537
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1538 = relay.var("var_1538", dtype = "float32", shape = (9, 9, 13))#candidate|1538|(9, 9, 13)|var|float32
func_1537_call = mutated_mod.get_global_var('func_1537')
call_1539 = func_1537_call(var_1538)
output = call_1539
func_1540 = relay.Function([var_1538], output)
mutated_mod['func_1540'] = func_1540
mutated_mod = relay.transform.InferType()(mutated_mod)
func_433_call = mod.get_global_var('func_433')
func_434_call = mutated_mod.get_global_var('func_434')
call_1578 = func_433_call()
call_1579 = func_433_call()
var_1584 = relay.var("var_1584", dtype = "float32", shape = (9, 9, 13))#candidate|1584|(9, 9, 13)|var|float32
bop_1585 = relay.divide(call_1578.astype('float32'), relay.reshape(var_1584.astype('float32'), relay.shape_of(call_1578))) # shape=(9, 9, 13)
bop_1588 = relay.divide(call_1579.astype('float32'), relay.reshape(var_1584.astype('float32'), relay.shape_of(call_1579))) # shape=(9, 9, 13)
output = bop_1585
output2 = bop_1588
func_1597 = relay.Function([var_1584,], output)
mod['func_1597'] = func_1597
mod = relay.transform.InferType()(mod)
var_1598 = relay.var("var_1598", dtype = "float32", shape = (9, 9, 13))#candidate|1598|(9, 9, 13)|var|float32
output = func_1597(var_1598)
func_1599 = relay.Function([var_1598], output)
mutated_mod['func_1599'] = func_1599
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1064_call = mod.get_global_var('func_1064')
func_1066_call = mutated_mod.get_global_var('func_1066')
call_1670 = func_1064_call()
call_1671 = func_1064_call()
func_1115_call = mod.get_global_var('func_1115')
func_1116_call = mutated_mod.get_global_var('func_1116')
call_1694 = relay.TupleGetItem(func_1115_call(), 0)
call_1695 = relay.TupleGetItem(func_1116_call(), 0)
const_1700 = relay.const([[[9,-4,-9,-7,-3,-8,-7,5,-5,-4,-8,-2,7],[-3,-10,-5,-4,-3,5,9,-7,10,1,7,-2,-10],[5,3,-9,-9,5,-7,4,-3,10,-8,-2,-10,6],[8,-2,8,2,9,2,-2,3,-5,9,-7,3,-7],[6,7,-7,-9,5,4,3,-1,-1,-1,2,3,-7],[2,8,2,-7,7,5,-2,-7,2,-10,-4,-7,9],[-4,-3,-5,-8,4,-8,-10,6,-2,8,7,-9,2],[-9,-2,-8,-1,5,6,8,5,5,-4,1,-1,7],[-8,4,2,8,-2,-10,9,-8,9,7,5,-9,4]],[[4,8,1,8,7,9,-5,4,-3,-9,8,-8,-1],[-8,1,-10,-7,-4,6,4,-3,-1,-5,2,-5,-8],[2,-7,-10,-5,7,3,6,4,3,-7,2,-3,-10],[4,9,-8,7,-3,-10,-7,-4,1,-10,-1,-3,-9],[6,-2,8,-4,8,-7,-7,4,-9,-4,-1,-2,-10],[-4,-1,9,-5,-6,9,-2,-9,-3,-9,2,6,-10],[3,-8,5,7,6,-3,-9,6,8,2,-6,2,2],[3,1,4,5,6,-7,6,-9,4,10,3,-7,5],[-1,-9,2,10,-5,-9,10,10,10,-1,-7,-6,-5]],[[4,5,-5,6,-9,6,-6,-4,1,2,-1,9,1],[7,4,-4,3,-8,6,-4,6,4,1,9,-2,-3],[-3,-5,8,-10,3,1,-7,-6,-6,-8,8,-4,-2],[1,6,-6,-8,-3,-2,-9,1,1,-10,1,-5,8],[-4,4,-7,-9,1,-2,-8,-5,10,-5,5,-8,-1],[1,-9,1,1,-9,-10,-1,-4,8,-8,2,7,6],[1,7,5,10,-4,7,-6,-6,-5,-5,-8,2,-8],[-3,-2,-8,-4,-7,-10,-3,7,2,8,-8,-4,3],[8,9,10,10,10,-4,-1,-5,7,-9,-10,8,10]],[[-5,10,8,5,-3,-7,6,-9,4,-3,-4,7,-7],[-6,-6,-2,3,-9,10,-6,9,-4,-3,-7,-6,5],[1,5,10,-2,10,-9,5,-1,4,-8,3,9,-8],[4,-7,5,-3,-5,-4,1,-2,-6,-8,4,8,-6],[5,-6,2,-6,-9,6,-3,-6,1,-10,8,9,-5],[-10,4,-4,1,-1,-10,-1,-10,-10,9,8,3,-2],[4,-9,-6,-1,-4,1,-5,-6,1,-1,-4,2,8],[3,9,-2,-1,-3,-9,9,-9,9,-3,8,-2,-5],[-1,2,-8,-3,-4,-10,-8,-2,-7,-10,-1,2,-4]],[[10,-9,-4,3,-4,-5,-5,-3,-4,10,-10,4,5],[9,-1,-8,-2,-5,1,-4,-6,3,-10,10,9,-7],[-7,9,6,9,-4,8,6,-2,-9,2,-7,-1,-1],[-8,-9,9,8,7,-9,-1,3,-9,-3,6,9,-1],[2,3,3,6,-6,9,7,8,-2,1,2,-6,10],[1,9,6,-4,-7,-10,-10,-9,10,6,-2,-1,-6],[2,8,-4,-1,-10,4,-6,2,3,-2,-2,-8,4],[-7,-2,8,6,6,-6,3,-6,2,10,-9,6,7],[6,6,-5,7,-9,9,-2,7,4,7,-9,-1,3]],[[-3,-3,-8,-4,-1,9,-6,2,6,-2,5,5,5],[9,4,-8,-2,7,-10,-6,2,8,6,5,5,4],[-5,-9,2,10,3,-3,1,-7,-1,-1,-10,2,8],[-7,7,2,-10,-6,-3,10,-8,-3,3,9,2,-8],[10,8,9,2,7,-10,5,1,4,-5,4,-1,-5],[2,2,-2,10,-2,-5,5,-6,-3,2,-10,5,9],[1,-4,-10,-6,6,7,-9,-5,1,8,-6,10,-5],[4,-8,-9,5,-7,-10,1,2,4,-5,8,2,3],[9,5,6,3,-6,-4,6,8,-6,-3,-7,2,9]],[[-7,-7,8,8,7,-5,-9,-3,-4,4,-6,-10,-1],[-10,-10,4,-10,10,7,1,1,6,-9,-2,-9,-4],[9,6,3,-6,4,10,10,-2,-9,3,-9,1,8],[-10,2,-4,7,10,5,-1,-7,-1,-3,4,-5,2],[-5,-3,-6,2,6,6,5,1,5,6,-5,7,-1],[-7,-9,2,2,9,-8,-6,8,-6,-10,-2,1,7],[7,3,6,-6,-9,-10,-4,8,9,-4,8,9,-9],[4,-1,7,4,7,9,6,-10,10,-3,-5,4,1],[-3,9,1,3,2,-9,-7,-8,-10,6,-9,5,5]],[[-6,1,-1,8,-6,3,9,7,-4,4,3,-6,-5],[5,9,-2,-9,2,7,1,-7,3,4,5,8,-1],[5,-10,-2,-4,5,6,9,5,8,-9,4,2,-4],[5,-8,5,-4,8,9,7,-8,-9,2,2,2,6],[3,-2,-7,-3,3,-10,10,-5,10,3,6,2,6],[10,5,-3,-4,-9,4,-5,7,-6,-3,-6,-2,10],[10,7,-6,-5,-3,-3,-5,-7,2,10,5,-8,6],[1,4,-7,5,-10,3,4,-4,-4,-9,2,10,3],[-5,-4,-5,-10,-8,3,2,-6,9,-2,9,5,-4]],[[-9,8,-10,3,5,-10,-6,1,6,5,8,-4,-8],[-6,-10,2,5,-3,5,10,3,3,10,1,7,8],[9,-6,4,3,-2,-3,-5,1,-2,9,1,-7,6],[-9,-3,8,10,10,-6,7,-8,-7,9,-4,-9,6],[-5,-4,-2,-3,1,-10,5,-6,5,-3,6,-7,-7],[5,3,7,8,-8,6,7,3,10,-7,3,2,4],[-5,2,-5,-8,-2,-8,-6,-1,8,-2,5,-10,-10],[4,-8,-9,-3,-5,-2,7,-7,2,-1,-6,1,9],[9,8,-4,-1,-3,5,3,-4,-10,7,-6,-1,-2]]], dtype = "int32")#candidate|1700|(9, 9, 13)|const|int32
bop_1701 = relay.logical_and(call_1694.astype('bool'), relay.reshape(const_1700.astype('bool'), relay.shape_of(call_1694))) # shape=(9, 9, 13)
bop_1704 = relay.logical_and(call_1695.astype('bool'), relay.reshape(const_1700.astype('bool'), relay.shape_of(call_1695))) # shape=(9, 9, 13)
output = relay.Tuple([call_1670,bop_1701,])
output2 = relay.Tuple([call_1671,bop_1704,])
func_1714 = relay.Function([], output)
mod['func_1714'] = func_1714
mod = relay.transform.InferType()(mod)
output = func_1714()
func_1715 = relay.Function([], output)
mutated_mod['func_1715'] = func_1715
mutated_mod = relay.transform.InferType()(mutated_mod)
func_363_call = mod.get_global_var('func_363')
func_364_call = mutated_mod.get_global_var('func_364')
call_1727 = relay.TupleGetItem(func_363_call(), 3)
call_1728 = relay.TupleGetItem(func_364_call(), 3)
func_1714_call = mod.get_global_var('func_1714')
func_1715_call = mutated_mod.get_global_var('func_1715')
call_1736 = relay.TupleGetItem(func_1714_call(), 1)
call_1737 = relay.TupleGetItem(func_1715_call(), 1)
output = relay.Tuple([call_1727,call_1736,])
output2 = relay.Tuple([call_1728,call_1737,])
func_1754 = relay.Function([], output)
mod['func_1754'] = func_1754
mod = relay.transform.InferType()(mod)
output = func_1754()
func_1755 = relay.Function([], output)
mutated_mod['func_1755'] = func_1755
mutated_mod = relay.transform.InferType()(mutated_mod)
func_536_call = mod.get_global_var('func_536')
func_537_call = mutated_mod.get_global_var('func_537')
call_1778 = relay.TupleGetItem(func_536_call(), 1)
call_1779 = relay.TupleGetItem(func_537_call(), 1)
var_1781 = relay.var("var_1781", dtype = "float64", shape = (9, 9, 13))#candidate|1781|(9, 9, 13)|var|float64
bop_1782 = relay.less_equal(call_1778.astype('bool'), relay.reshape(var_1781.astype('bool'), relay.shape_of(call_1778))) # shape=(9, 9, 13)
bop_1785 = relay.less_equal(call_1779.astype('bool'), relay.reshape(var_1781.astype('bool'), relay.shape_of(call_1779))) # shape=(9, 9, 13)
output = relay.Tuple([bop_1782,])
output2 = relay.Tuple([bop_1785,])
func_1787 = relay.Function([var_1781,], output)
mod['func_1787'] = func_1787
mod = relay.transform.InferType()(mod)
var_1788 = relay.var("var_1788", dtype = "float64", shape = (9, 9, 13))#candidate|1788|(9, 9, 13)|var|float64
output = func_1787(var_1788)
func_1789 = relay.Function([var_1788], output)
mutated_mod['func_1789'] = func_1789
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1115_call = mod.get_global_var('func_1115')
func_1116_call = mutated_mod.get_global_var('func_1116')
call_1869 = relay.TupleGetItem(func_1115_call(), 0)
call_1870 = relay.TupleGetItem(func_1116_call(), 0)
func_1496_call = mod.get_global_var('func_1496')
func_1498_call = mutated_mod.get_global_var('func_1498')
call_1872 = relay.TupleGetItem(func_1496_call(relay.reshape(call_1869.astype('float64'), [9, 9, 13])), 0)
call_1873 = relay.TupleGetItem(func_1498_call(relay.reshape(call_1869.astype('float64'), [9, 9, 13])), 0)
var_1874 = relay.var("var_1874", dtype = "float32", shape = (9, 9, 13))#candidate|1874|(9, 9, 13)|var|float32
bop_1875 = relay.equal(call_1872.astype('bool'), relay.reshape(var_1874.astype('bool'), relay.shape_of(call_1872))) # shape=(9, 9, 13)
bop_1878 = relay.equal(call_1873.astype('bool'), relay.reshape(var_1874.astype('bool'), relay.shape_of(call_1873))) # shape=(9, 9, 13)
func_1787_call = mod.get_global_var('func_1787')
func_1789_call = mutated_mod.get_global_var('func_1789')
call_1889 = relay.TupleGetItem(func_1787_call(relay.reshape(call_1869.astype('float64'), [9, 9, 13])), 0)
call_1890 = relay.TupleGetItem(func_1789_call(relay.reshape(call_1869.astype('float64'), [9, 9, 13])), 0)
var_1914 = relay.var("var_1914", dtype = "int32", shape = (9, 9, 13))#candidate|1914|(9, 9, 13)|var|int32
bop_1915 = relay.minimum(call_1869.astype('int32'), relay.reshape(var_1914.astype('int32'), relay.shape_of(call_1869))) # shape=(9, 9, 13)
bop_1918 = relay.minimum(call_1870.astype('int32'), relay.reshape(var_1914.astype('int32'), relay.shape_of(call_1870))) # shape=(9, 9, 13)
func_1383_call = mod.get_global_var('func_1383')
func_1384_call = mutated_mod.get_global_var('func_1384')
call_1919 = relay.TupleGetItem(func_1383_call(), 1)
call_1920 = relay.TupleGetItem(func_1384_call(), 1)
output = relay.Tuple([bop_1875,call_1889,bop_1915,call_1919,])
output2 = relay.Tuple([bop_1878,call_1890,bop_1918,call_1920,])
func_1926 = relay.Function([var_1874,var_1914,], output)
mod['func_1926'] = func_1926
mod = relay.transform.InferType()(mod)
var_1927 = relay.var("var_1927", dtype = "float32", shape = (9, 9, 13))#candidate|1927|(9, 9, 13)|var|float32
var_1928 = relay.var("var_1928", dtype = "int32", shape = (9, 9, 13))#candidate|1928|(9, 9, 13)|var|int32
output = func_1926(var_1927,var_1928,)
func_1929 = relay.Function([var_1927,var_1928,], output)
mutated_mod['func_1929'] = func_1929
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1303_call = mod.get_global_var('func_1303')
func_1304_call = mutated_mod.get_global_var('func_1304')
call_1931 = relay.TupleGetItem(func_1303_call(), 1)
call_1932 = relay.TupleGetItem(func_1304_call(), 1)
func_1496_call = mod.get_global_var('func_1496')
func_1498_call = mutated_mod.get_global_var('func_1498')
call_1934 = relay.TupleGetItem(func_1496_call(relay.reshape(call_1931.astype('float64'), [9, 9, 13])), 0)
call_1935 = relay.TupleGetItem(func_1498_call(relay.reshape(call_1931.astype('float64'), [9, 9, 13])), 0)
uop_1952 = relay.log2(call_1931.astype('float64')) # shape=(9, 9, 13)
uop_1954 = relay.log2(call_1932.astype('float64')) # shape=(9, 9, 13)
output = relay.Tuple([call_1934,uop_1952,])
output2 = relay.Tuple([call_1935,uop_1954,])
func_1958 = relay.Function([], output)
mod['func_1958'] = func_1958
mod = relay.transform.InferType()(mod)
mutated_mod['func_1958'] = func_1958
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1958_call = mutated_mod.get_global_var('func_1958')
call_1959 = func_1958_call()
output = call_1959
func_1960 = relay.Function([], output)
mutated_mod['func_1960'] = func_1960
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1303_call = mod.get_global_var('func_1303')
func_1304_call = mutated_mod.get_global_var('func_1304')
call_1985 = relay.TupleGetItem(func_1303_call(), 0)
call_1986 = relay.TupleGetItem(func_1304_call(), 0)
uop_1996 = relay.erf(call_1985.astype('float64')) # shape=(9, 9, 13)
uop_1998 = relay.erf(call_1986.astype('float64')) # shape=(9, 9, 13)
output = relay.Tuple([uop_1996,])
output2 = relay.Tuple([uop_1998,])
func_2001 = relay.Function([], output)
mod['func_2001'] = func_2001
mod = relay.transform.InferType()(mod)
output = func_2001()
func_2002 = relay.Function([], output)
mutated_mod['func_2002'] = func_2002
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2044 = relay.const([[[1.385868,-0.206598,-5.465659,-9.266405,-9.992985,7.140487,-9.805043,-6.032740],[-8.189222,7.980092,-5.442621,-3.855210,2.526355,3.621952,4.229663,8.503453],[-5.101448,7.497634,-7.072659,-6.549792,9.455306,1.153430,-9.801007,9.808829],[6.252576,-3.264156,-4.153720,1.228593,-9.871702,8.095061,1.356305,-8.400254],[4.791111,-9.911737,8.996208,-1.873356,-2.575071,-7.581557,1.066196,-5.743437]],[[-9.669037,-1.381419,0.476188,9.573717,1.516265,5.976630,6.853047,-9.933404],[4.528893,-2.009280,1.483185,-5.725859,7.303988,-5.121840,-9.529141,0.853967],[9.452921,3.347951,9.331927,-3.528727,0.152923,2.238020,5.657362,7.373073],[5.692116,-3.621189,-7.674800,-6.213944,9.964769,-9.049086,3.338845,3.037918],[-8.388567,3.453702,3.254185,-4.239282,2.739298,1.461848,4.047985,-7.803893]],[[3.197484,9.644720,7.541491,5.047596,-9.347016,-5.741565,2.778860,3.455869],[-5.928638,-0.110783,-4.463188,-2.358163,-2.706723,3.022365,9.124137,-9.750473],[-1.129104,-2.241386,-2.771184,-0.935929,-4.155003,-9.128864,-1.021056,1.994178],[4.779234,-6.306779,-9.760010,2.005756,2.988645,-5.331537,-7.706177,4.606803],[-8.810173,-6.737293,2.902881,4.680873,1.217152,5.710562,5.700604,-4.760319]],[[-6.920794,7.335970,-7.491498,-3.900837,9.488098,-2.430063,3.639678,-7.706667],[1.281818,-8.715585,1.263636,-1.918991,-1.021636,4.198488,-9.933752,-7.037223],[-9.986462,8.897905,-4.933955,-3.958749,-3.854749,-8.250751,-8.335383,5.377195],[2.469510,-1.087773,-9.312144,-2.295453,0.391459,-5.818105,5.583223,-4.027823],[-6.763948,-5.485974,5.677245,-5.540217,5.816753,-6.372366,7.399027,-9.517005]],[[3.241263,-5.871878,2.874571,-3.458813,-1.917144,7.342211,3.017668,6.783473],[3.334414,7.023422,3.773978,1.649305,-7.606376,-8.730819,9.784901,-2.388806],[-8.926443,-4.695522,0.118216,-1.583249,-3.424450,-4.440947,3.385231,9.143356],[0.732562,-5.590413,3.406700,-1.396724,3.234241,8.672600,1.331144,5.175430],[-9.985328,8.476116,1.801753,0.061697,7.555448,3.879191,-0.039148,-5.411528]],[[9.995628,-9.216071,-4.740692,-7.018491,9.267736,-9.998219,-6.942319,-4.665092],[-1.700287,-6.943076,5.323365,6.040764,3.961966,-1.788095,3.042315,-6.151194],[0.401985,5.643956,4.949646,5.420636,-7.985840,2.549101,9.043411,4.768245],[5.137545,5.874167,-2.158481,-4.853311,-8.444031,1.608229,5.590054,-0.196078],[-5.045567,-8.803673,-4.955864,-0.855942,2.343565,6.854215,-5.125424,-5.517245]],[[-3.784618,-2.222514,-6.127862,7.107529,4.700523,7.213186,-2.418737,9.232692],[5.604261,-0.034913,4.463683,-4.055234,-4.894229,-4.390089,2.122244,-3.497807],[-7.541471,-3.445885,1.630137,9.171438,-9.636874,1.256915,4.819598,8.679824],[-2.602566,-4.156888,-7.899331,5.502917,-1.547227,2.893462,-2.804235,5.243940],[0.869676,-4.532289,4.639184,8.143752,-6.609444,-5.372123,-8.666477,-5.813585]],[[8.853447,-0.553356,-4.525834,-3.995811,5.914050,-0.689820,-3.717735,0.191903],[2.073430,-2.701447,1.052143,-9.175231,7.116782,6.574844,-1.783432,-3.993348],[-0.289710,9.504915,-0.412835,9.473597,-7.115048,-3.850096,-7.245318,-5.900653],[7.218397,-3.033356,-0.801183,-2.985408,-7.293881,9.742330,4.150888,-8.476590],[0.308349,-7.774596,-8.342022,7.265632,5.803510,2.627785,2.320674,0.798705]],[[-8.699143,-6.710440,-7.498256,-9.642674,-5.525715,2.874017,-2.398303,-3.962919],[-4.566944,8.159881,-7.181473,6.051627,-0.323914,8.746001,-6.148826,-2.421803],[6.636412,1.945926,8.506338,-8.550448,-4.255704,-6.237010,7.165246,-7.607665],[5.692900,-6.684026,-8.101163,-2.967319,-9.240185,4.065927,-2.867735,-8.674525],[-8.984695,-8.483927,2.411959,3.222057,-8.469701,-8.021232,-3.106124,9.049732]],[[7.705212,-1.482649,3.025631,-8.645465,-1.731464,-7.013280,-6.220872,-3.341353],[4.676355,-3.577909,2.606038,-6.141303,1.491686,-1.582149,9.289787,-0.529768],[6.511774,-8.549293,5.739772,7.343554,-3.818558,-0.250058,-5.691207,9.806298],[3.304462,-6.133021,-8.197644,2.776388,-4.312177,3.845678,7.692654,-2.200471],[-5.674093,-6.211704,9.741602,-9.368483,1.052711,-6.126222,8.606744,5.636931]],[[-7.625657,-7.925579,-2.922265,-1.250628,1.796407,-1.938300,8.907976,9.964022],[-2.384305,2.159628,2.760650,5.321321,3.731986,-9.435617,-2.192422,9.369008],[-8.046946,0.655846,3.443987,0.021349,4.965370,-1.116191,-2.636388,7.062490],[4.840561,-5.550592,-4.394787,0.965190,-3.836451,-3.205172,-6.732831,9.599226],[9.821198,8.201399,-4.427163,9.516023,3.615087,5.398075,-0.912623,-3.737552]],[[4.269422,-7.451750,-1.634811,0.683379,-7.633410,8.465335,-0.173813,8.688962],[5.209658,-3.756948,3.116664,-8.291372,7.319960,-9.795297,-8.664912,9.145917],[3.473275,3.672780,-7.125797,-9.513172,-3.716779,7.805154,-1.704447,7.980550],[8.270070,-7.405034,4.797060,9.370238,-6.030414,-9.817327,-6.813321,-2.766596],[-6.429993,-3.909379,9.209006,6.632659,-5.452952,-2.151855,7.066448,0.932998]],[[1.633350,3.450186,-3.955953,-4.868999,-8.001793,0.623014,-7.257749,-5.910122],[5.173998,8.397040,-0.723729,-1.961801,6.210252,4.290358,-1.242790,-0.759934],[-2.222035,6.981147,-5.518018,8.512824,-6.800203,-5.442829,8.146401,6.611059],[1.885627,9.314796,7.185202,-1.009764,-5.839457,8.786131,-3.911486,-8.085945],[4.512734,6.661061,6.824814,-4.167902,9.515279,4.581305,-7.494509,3.361311]],[[1.569290,4.062174,7.073476,-2.194274,9.262052,-4.902627,9.035542,6.562445],[-8.010290,-8.436982,6.376456,-8.444166,0.263289,2.524263,-4.447004,5.862335],[7.406206,6.099396,3.607750,-4.944819,5.916166,-4.535143,-3.313605,-2.709732],[8.500657,-5.929786,5.102646,7.271568,-1.797359,-9.192970,-3.438220,9.168701],[-0.830143,-8.111958,-3.358803,7.705133,8.585616,-0.279984,6.208087,5.800065]]], dtype = "float32")#candidate|2044|(14, 5, 8)|const|float32
uop_2045 = relay.atan(const_2044.astype('float32')) # shape=(14, 5, 8)
output = relay.Tuple([uop_2045,])
output2 = relay.Tuple([uop_2045,])
func_2049 = relay.Function([], output)
mod['func_2049'] = func_2049
mod = relay.transform.InferType()(mod)
output = func_2049()
func_2050 = relay.Function([], output)
mutated_mod['func_2050'] = func_2050
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1714_call = mod.get_global_var('func_1714')
func_1715_call = mutated_mod.get_global_var('func_1715')
call_2069 = relay.TupleGetItem(func_1714_call(), 1)
call_2070 = relay.TupleGetItem(func_1715_call(), 1)
func_1926_call = mod.get_global_var('func_1926')
func_1929_call = mutated_mod.get_global_var('func_1929')
call_2074 = relay.TupleGetItem(func_1926_call(relay.reshape(call_2069.astype('float32'), [9, 9, 13]), relay.reshape(call_2069.astype('int32'), [9, 9, 13]), ), 0)
call_2075 = relay.TupleGetItem(func_1929_call(relay.reshape(call_2069.astype('float32'), [9, 9, 13]), relay.reshape(call_2069.astype('int32'), [9, 9, 13]), ), 0)
func_1714_call = mod.get_global_var('func_1714')
func_1715_call = mutated_mod.get_global_var('func_1715')
call_2076 = relay.TupleGetItem(func_1714_call(), 0)
call_2077 = relay.TupleGetItem(func_1715_call(), 0)
func_363_call = mod.get_global_var('func_363')
func_364_call = mutated_mod.get_global_var('func_364')
call_2092 = relay.TupleGetItem(func_363_call(), 1)
call_2093 = relay.TupleGetItem(func_364_call(), 1)
output = relay.Tuple([call_2069,call_2074,call_2076,call_2092,])
output2 = relay.Tuple([call_2070,call_2075,call_2077,call_2093,])
func_2105 = relay.Function([], output)
mod['func_2105'] = func_2105
mod = relay.transform.InferType()(mod)
mutated_mod['func_2105'] = func_2105
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2105_call = mutated_mod.get_global_var('func_2105')
call_2106 = func_2105_call()
output = call_2106
func_2107 = relay.Function([], output)
mutated_mod['func_2107'] = func_2107
mutated_mod = relay.transform.InferType()(mutated_mod)
func_536_call = mod.get_global_var('func_536')
func_537_call = mutated_mod.get_global_var('func_537')
call_2111 = relay.TupleGetItem(func_536_call(), 1)
call_2112 = relay.TupleGetItem(func_537_call(), 1)
func_1249_call = mod.get_global_var('func_1249')
func_1251_call = mutated_mod.get_global_var('func_1251')
call_2119 = relay.TupleGetItem(func_1249_call(), 1)
call_2120 = relay.TupleGetItem(func_1251_call(), 1)
func_1037_call = mod.get_global_var('func_1037')
func_1041_call = mutated_mod.get_global_var('func_1041')
var_2123 = relay.var("var_2123", dtype = "float64", shape = (6, 18))#candidate|2123|(6, 18)|var|float64
call_2122 = relay.TupleGetItem(func_1037_call(relay.reshape(var_2123.astype('float64'), [3, 36]), relay.reshape(var_2123.astype('float64'), [3, 36]), relay.reshape(call_2119.astype('float32'), [9, 9, 13]), ), 3)
call_2124 = relay.TupleGetItem(func_1041_call(relay.reshape(var_2123.astype('float64'), [3, 36]), relay.reshape(var_2123.astype('float64'), [3, 36]), relay.reshape(call_2119.astype('float32'), [9, 9, 13]), ), 3)
uop_2127 = relay.tan(var_2123.astype('float32')) # shape=(6, 18)
output = relay.Tuple([call_2111,call_2119,call_2122,uop_2127,])
output2 = relay.Tuple([call_2112,call_2120,call_2124,uop_2127,])
func_2135 = relay.Function([var_2123,], output)
mod['func_2135'] = func_2135
mod = relay.transform.InferType()(mod)
mutated_mod['func_2135'] = func_2135
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2136 = relay.var("var_2136", dtype = "float64", shape = (6, 18))#candidate|2136|(6, 18)|var|float64
func_2135_call = mutated_mod.get_global_var('func_2135')
call_2137 = func_2135_call(var_2136)
output = call_2137
func_2138 = relay.Function([var_2136], output)
mutated_mod['func_2138'] = func_2138
mutated_mod = relay.transform.InferType()(mutated_mod)
func_573_call = mod.get_global_var('func_573')
func_575_call = mutated_mod.get_global_var('func_575')
call_2154 = func_573_call()
call_2155 = func_573_call()
output = call_2154
output2 = call_2155
func_2156 = relay.Function([], output)
mod['func_2156'] = func_2156
mod = relay.transform.InferType()(mod)
mutated_mod['func_2156'] = func_2156
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2156_call = mutated_mod.get_global_var('func_2156')
call_2157 = func_2156_call()
output = call_2157
func_2158 = relay.Function([], output)
mutated_mod['func_2158'] = func_2158
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2159 = relay.var("var_2159", dtype = "float64", shape = (11, 16, 15))#candidate|2159|(11, 16, 15)|var|float64
uop_2160 = relay.log(var_2159.astype('float64')) # shape=(11, 16, 15)
func_1178_call = mod.get_global_var('func_1178')
func_1180_call = mutated_mod.get_global_var('func_1180')
call_2174 = func_1178_call()
call_2175 = func_1178_call()
bop_2190 = relay.less(uop_2160.astype('bool'), relay.reshape(var_2159.astype('bool'), relay.shape_of(uop_2160))) # shape=(11, 16, 15)
output = relay.Tuple([call_2174,bop_2190,])
output2 = relay.Tuple([call_2175,bop_2190,])
func_2220 = relay.Function([var_2159,], output)
mod['func_2220'] = func_2220
mod = relay.transform.InferType()(mod)
var_2221 = relay.var("var_2221", dtype = "float64", shape = (11, 16, 15))#candidate|2221|(11, 16, 15)|var|float64
output = func_2220(var_2221)
func_2222 = relay.Function([var_2221], output)
mutated_mod['func_2222'] = func_2222
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2001_call = mod.get_global_var('func_2001')
func_2002_call = mutated_mod.get_global_var('func_2002')
call_2274 = relay.TupleGetItem(func_2001_call(), 0)
call_2275 = relay.TupleGetItem(func_2002_call(), 0)
func_468_call = mod.get_global_var('func_468')
func_470_call = mutated_mod.get_global_var('func_470')
call_2276 = relay.TupleGetItem(func_468_call(), 0)
call_2277 = relay.TupleGetItem(func_470_call(), 0)
func_1115_call = mod.get_global_var('func_1115')
func_1116_call = mutated_mod.get_global_var('func_1116')
call_2284 = relay.TupleGetItem(func_1115_call(), 0)
call_2285 = relay.TupleGetItem(func_1116_call(), 0)
func_1496_call = mod.get_global_var('func_1496')
func_1498_call = mutated_mod.get_global_var('func_1498')
call_2300 = relay.TupleGetItem(func_1496_call(relay.reshape(call_2284.astype('float64'), [9, 9, 13])), 0)
call_2301 = relay.TupleGetItem(func_1498_call(relay.reshape(call_2284.astype('float64'), [9, 9, 13])), 0)
func_433_call = mod.get_global_var('func_433')
func_434_call = mutated_mod.get_global_var('func_434')
call_2305 = func_433_call()
call_2306 = func_433_call()
bop_2307 = relay.add(call_2274.astype('float32'), relay.reshape(call_2300.astype('float32'), relay.shape_of(call_2274))) # shape=(9, 9, 13)
bop_2310 = relay.add(call_2275.astype('float32'), relay.reshape(call_2301.astype('float32'), relay.shape_of(call_2275))) # shape=(9, 9, 13)
var_2315 = relay.var("var_2315", dtype = "float32", shape = (9, 9, 13))#candidate|2315|(9, 9, 13)|var|float32
bop_2316 = relay.right_shift(call_2276.astype('int32'), relay.reshape(var_2315.astype('int32'), relay.shape_of(call_2276))) # shape=(9, 9, 13)
bop_2319 = relay.right_shift(call_2277.astype('int32'), relay.reshape(var_2315.astype('int32'), relay.shape_of(call_2277))) # shape=(9, 9, 13)
output = relay.Tuple([call_2284,call_2305,bop_2307,bop_2316,])
output2 = relay.Tuple([call_2285,call_2306,bop_2310,bop_2319,])
func_2324 = relay.Function([var_2315,], output)
mod['func_2324'] = func_2324
mod = relay.transform.InferType()(mod)
var_2325 = relay.var("var_2325", dtype = "float32", shape = (9, 9, 13))#candidate|2325|(9, 9, 13)|var|float32
output = func_2324(var_2325)
func_2326 = relay.Function([var_2325], output)
mutated_mod['func_2326'] = func_2326
mutated_mod = relay.transform.InferType()(mutated_mod)
func_363_call = mod.get_global_var('func_363')
func_364_call = mutated_mod.get_global_var('func_364')
call_2385 = relay.TupleGetItem(func_363_call(), 2)
call_2386 = relay.TupleGetItem(func_364_call(), 2)
func_1754_call = mod.get_global_var('func_1754')
func_1755_call = mutated_mod.get_global_var('func_1755')
call_2398 = relay.TupleGetItem(func_1754_call(), 1)
call_2399 = relay.TupleGetItem(func_1755_call(), 1)
output = relay.Tuple([call_2385,call_2398,])
output2 = relay.Tuple([call_2386,call_2399,])
func_2403 = relay.Function([], output)
mod['func_2403'] = func_2403
mod = relay.transform.InferType()(mod)
mutated_mod['func_2403'] = func_2403
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2403_call = mutated_mod.get_global_var('func_2403')
call_2404 = func_2403_call()
output = call_2404
func_2405 = relay.Function([], output)
mutated_mod['func_2405'] = func_2405
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1383_call = mod.get_global_var('func_1383')
func_1384_call = mutated_mod.get_global_var('func_1384')
call_2431 = relay.TupleGetItem(func_1383_call(), 0)
call_2432 = relay.TupleGetItem(func_1384_call(), 0)
var_2451 = relay.var("var_2451", dtype = "float32", shape = (10, 7, 12))#candidate|2451|(10, 7, 12)|var|float32
bop_2452 = relay.equal(call_2431.astype('bool'), relay.reshape(var_2451.astype('bool'), relay.shape_of(call_2431))) # shape=(10, 7, 12)
bop_2455 = relay.equal(call_2432.astype('bool'), relay.reshape(var_2451.astype('bool'), relay.shape_of(call_2432))) # shape=(10, 7, 12)
func_2403_call = mod.get_global_var('func_2403')
func_2405_call = mutated_mod.get_global_var('func_2405')
call_2461 = relay.TupleGetItem(func_2403_call(), 0)
call_2462 = relay.TupleGetItem(func_2405_call(), 0)
bop_2472 = relay.bitwise_or(var_2451.astype('uint16'), relay.reshape(call_2431.astype('uint16'), relay.shape_of(var_2451))) # shape=(10, 7, 12)
bop_2475 = relay.bitwise_or(var_2451.astype('uint16'), relay.reshape(call_2432.astype('uint16'), relay.shape_of(var_2451))) # shape=(10, 7, 12)
output = relay.Tuple([bop_2452,call_2461,bop_2472,])
output2 = relay.Tuple([bop_2455,call_2462,bop_2475,])
func_2489 = relay.Function([var_2451,], output)
mod['func_2489'] = func_2489
mod = relay.transform.InferType()(mod)
var_2490 = relay.var("var_2490", dtype = "float32", shape = (10, 7, 12))#candidate|2490|(10, 7, 12)|var|float32
output = func_2489(var_2490)
func_2491 = relay.Function([var_2490], output)
mutated_mod['func_2491'] = func_2491
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2539 = relay.var("var_2539", dtype = "float32", shape = (1, 8, 11))#candidate|2539|(1, 8, 11)|var|float32
uop_2540 = relay.log(var_2539.astype('float32')) # shape=(1, 8, 11)
func_292_call = mod.get_global_var('func_292')
func_294_call = mutated_mod.get_global_var('func_294')
call_2546 = relay.TupleGetItem(func_292_call(), 1)
call_2547 = relay.TupleGetItem(func_294_call(), 1)
output = relay.Tuple([uop_2540,call_2546,])
output2 = relay.Tuple([uop_2540,call_2547,])
func_2554 = relay.Function([var_2539,], output)
mod['func_2554'] = func_2554
mod = relay.transform.InferType()(mod)
mutated_mod['func_2554'] = func_2554
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2555 = relay.var("var_2555", dtype = "float32", shape = (1, 8, 11))#candidate|2555|(1, 8, 11)|var|float32
func_2554_call = mutated_mod.get_global_var('func_2554')
call_2556 = func_2554_call(var_2555)
output = call_2556
func_2557 = relay.Function([var_2555], output)
mutated_mod['func_2557'] = func_2557
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1064_call = mod.get_global_var('func_1064')
func_1066_call = mutated_mod.get_global_var('func_1066')
call_2565 = func_1064_call()
call_2566 = func_1064_call()
output = call_2565
output2 = call_2566
func_2572 = relay.Function([], output)
mod['func_2572'] = func_2572
mod = relay.transform.InferType()(mod)
mutated_mod['func_2572'] = func_2572
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2572_call = mutated_mod.get_global_var('func_2572')
call_2573 = func_2572_call()
output = call_2573
func_2574 = relay.Function([], output)
mutated_mod['func_2574'] = func_2574
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1714_call = mod.get_global_var('func_1714')
func_1715_call = mutated_mod.get_global_var('func_1715')
call_2600 = relay.TupleGetItem(func_1714_call(), 0)
call_2601 = relay.TupleGetItem(func_1715_call(), 0)
func_2220_call = mod.get_global_var('func_2220')
func_2222_call = mutated_mod.get_global_var('func_2222')
var_2609 = relay.var("var_2609", dtype = "float64", shape = (2640,))#candidate|2609|(2640,)|var|float64
call_2608 = relay.TupleGetItem(func_2220_call(relay.reshape(var_2609.astype('float64'), [11, 16, 15])), 0)
call_2610 = relay.TupleGetItem(func_2222_call(relay.reshape(var_2609.astype('float64'), [11, 16, 15])), 0)
output = relay.Tuple([call_2600,call_2608,var_2609,])
output2 = relay.Tuple([call_2601,call_2610,var_2609,])
func_2611 = relay.Function([var_2609,], output)
mod['func_2611'] = func_2611
mod = relay.transform.InferType()(mod)
var_2612 = relay.var("var_2612", dtype = "float64", shape = (2640,))#candidate|2612|(2640,)|var|float64
output = func_2611(var_2612)
func_2613 = relay.Function([var_2612], output)
mutated_mod['func_2613'] = func_2613
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2156_call = mod.get_global_var('func_2156')
func_2158_call = mutated_mod.get_global_var('func_2158')
call_2615 = func_2156_call()
call_2616 = func_2156_call()
func_715_call = mod.get_global_var('func_715')
func_716_call = mutated_mod.get_global_var('func_716')
call_2633 = relay.TupleGetItem(func_715_call(), 0)
call_2634 = relay.TupleGetItem(func_716_call(), 0)
func_799_call = mod.get_global_var('func_799')
func_802_call = mutated_mod.get_global_var('func_802')
call_2637 = relay.TupleGetItem(func_799_call(relay.reshape(call_2633.astype('float32'), [9, 9, 13])), 3)
call_2638 = relay.TupleGetItem(func_802_call(relay.reshape(call_2633.astype('float32'), [9, 9, 13])), 3)
uop_2641 = relay.sinh(call_2615.astype('float64')) # shape=(9, 9, 13)
uop_2643 = relay.sinh(call_2616.astype('float64')) # shape=(9, 9, 13)
func_1383_call = mod.get_global_var('func_1383')
func_1384_call = mutated_mod.get_global_var('func_1384')
call_2650 = relay.TupleGetItem(func_1383_call(), 0)
call_2651 = relay.TupleGetItem(func_1384_call(), 0)
output = relay.Tuple([call_2633,call_2637,uop_2641,call_2650,])
output2 = relay.Tuple([call_2634,call_2638,uop_2643,call_2651,])
func_2653 = relay.Function([], output)
mod['func_2653'] = func_2653
mod = relay.transform.InferType()(mod)
mutated_mod['func_2653'] = func_2653
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2653_call = mutated_mod.get_global_var('func_2653')
call_2654 = func_2653_call()
output = call_2654
func_2655 = relay.Function([], output)
mutated_mod['func_2655'] = func_2655
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1383_call = mod.get_global_var('func_1383')
func_1384_call = mutated_mod.get_global_var('func_1384')
call_2702 = relay.TupleGetItem(func_1383_call(), 0)
call_2703 = relay.TupleGetItem(func_1384_call(), 0)
output = relay.Tuple([call_2702,])
output2 = relay.Tuple([call_2703,])
func_2710 = relay.Function([], output)
mod['func_2710'] = func_2710
mod = relay.transform.InferType()(mod)
mutated_mod['func_2710'] = func_2710
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2710_call = mutated_mod.get_global_var('func_2710')
call_2711 = func_2710_call()
output = call_2711
func_2712 = relay.Function([], output)
mutated_mod['func_2712'] = func_2712
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2001_call = mod.get_global_var('func_2001')
func_2002_call = mutated_mod.get_global_var('func_2002')
call_2713 = relay.TupleGetItem(func_2001_call(), 0)
call_2714 = relay.TupleGetItem(func_2002_call(), 0)
func_2220_call = mod.get_global_var('func_2220')
func_2222_call = mutated_mod.get_global_var('func_2222')
const_2768 = relay.const([4.684752,8.258254,-6.140129,5.316558,4.934679,-8.015279,-3.805751,-1.922426,-9.895304,-3.926567,0.551872,-6.239989,0.400112,2.960871,-4.236744,5.905205,-4.459675,-6.655240,1.215023,-8.742973,-2.026709,-1.195845,-4.745031,6.918078,5.671359,4.401972,-3.850303,9.732906,9.211936,-1.137899,8.831620,3.742057,-9.427975,7.758920,8.030057,-9.456894,-2.110247,-0.912144,1.998242,0.621431,-7.296598,7.446155,-0.108197,-1.147789,2.561466,-2.208146,3.173999,-3.078268,6.163265,4.455789,7.735256,-7.980527,1.140586,1.556009,7.924654,9.119481,4.486488,-4.675643,2.612159,5.904632,4.446578,-2.606238,1.493882,-6.651250,-3.721755,-1.492607,3.873962,9.394814,0.071961,2.171846,3.193762,-5.620683,5.519727,-5.339150,-2.642621,1.148536,8.024244,-7.648789,-7.775673,-4.351150,-0.524865,3.345390,2.857221,-4.930125,4.118469,2.097766,7.364266,1.986972,-9.496421,1.281037,-0.017987,-4.140984,-4.075335,-0.406368,3.460885,4.661947,1.941647,2.434790,0.723334,-1.375283,4.613793,6.594826,0.298881,7.063094,9.544357,-1.178325,1.930888,2.749385,7.039244,1.096666,-0.164089,4.738000,7.340520,1.699191,-1.545770,7.067454,6.638637,-2.087822,0.770167,4.848806,3.874024,-0.086680,-6.537024,-0.412302,-0.667300,3.465121,0.257158,-7.839584,7.756594,2.235647,2.981610,-2.099680,-9.049880,-2.958068,-4.129390,-0.404505,1.552067,5.536537,-7.738903,-6.441442,9.598444,-2.310173,-5.748609,5.548023,-9.367261,5.413780,2.570544,-3.391373,4.019892,8.485654,-9.106807,1.149695,9.804292,-4.553158,-3.809783,-5.802259,-0.109531,-1.694966,2.506432,-1.304803,3.102818,-0.472063,9.344132,-1.685318,4.159673,3.553881,6.017623,7.040212,4.837896,-3.155782,-4.611253,8.762699,9.582041,3.157216,2.428873,-9.013090,-7.987374,2.534694,-9.710873,-2.972148,3.489975,5.678375,-4.274399,1.925278,-4.586801,3.740469,-3.759322,0.051883,8.478292,4.617257,3.510843,8.710153,-3.669131,0.774444,-6.811671,-1.409904,9.288848,-4.251304,-8.134285,8.251912,9.471381,-0.179787,4.741213,-1.758731,-2.270827,1.560287,0.261165,0.045677,6.548139,-9.509427,-6.041182,-5.909972,2.850899,2.671327,-3.113131,-5.346203,-1.920283,-5.081532,8.941386,-0.968012,-9.582079,0.730218,-6.987967,9.141734,5.650019,3.806208,-7.479489,-7.539427,-9.405493,1.690389,-0.064616,-3.652351,-6.164482,4.276666,5.228992,-4.339070,6.276016,-3.587129,-3.061081,-4.236070,4.668798,-1.935593,4.398496,0.654344,-0.884205,-3.585166,2.226301,7.905574,5.043004,8.693677,-6.386418,-4.585500,6.721343,1.839395,-4.798164,0.068918,2.540684,3.791596,-1.389093,-9.069758,-9.887983,-5.359289,-0.862755,8.958900,-5.547948,-6.793147,-7.449653,-4.794320,0.121219,-7.356824,0.777978,-1.534348,9.919416,1.002726,-0.844781,-5.802661,4.383419,-3.388261,5.745095,2.989263,-5.054515,-0.690767,3.346537,-2.275868,3.593271,-0.327496,9.980061,5.387504,4.279693,-3.868289,2.328124,-7.102364,1.922586,-0.639167,-8.374406,-0.362444,4.763115,-1.126787,-3.731575,-1.339601,8.346285,-4.277636,4.477083,4.396889,9.849536,-5.745630,-4.063745,9.174370,-2.472367,-9.614049,9.250172,4.474666,-2.500276,1.636725,6.877890,-7.762979,5.030358,7.402433,-1.501371,1.819601,-8.670777,-4.982332,-1.151936,4.338486,0.638775,5.889289,-3.842762,-9.728962,-7.807010,0.422522,7.848092,-7.298445,6.639211,4.364240,-5.436109,7.496485,-2.580419,-4.020344,0.791561,2.977288,1.925949,4.131443,-0.453703,-0.951444,-5.865418,-9.947319,1.845587,-6.514402,-4.241465,0.995753,-5.415404,7.865997,-5.982592,2.608978,4.732868,9.162954,6.394296,1.998508,-2.851585,7.959786,5.623492,-2.711840,-5.104483,3.439643,-8.478203,-1.521413,2.048923,9.304634,5.223403,5.644122,-5.118673,8.951907,-8.904914,4.488953,4.749904,1.590824,-2.194312,4.076366,-1.945154,5.369427,9.064742,7.685447,3.784924,7.613966,6.489034,-9.365604,3.725986,7.386919,-5.384993,-2.624064,9.334520,-3.677623,8.896439,6.885500,7.601495,-9.510574,-1.532001,5.864635,-8.766402,-4.895615,-8.031603,2.401007,-0.684455,2.661530,4.483129,-3.000669,1.695173,-6.562565,9.725948,-2.666863,-5.394533,2.572866,-7.311191,2.253034,6.718238,-1.614233,-5.437175,0.098416,-6.731742,7.078613,-0.669328,5.104454,-2.586995,-6.584262,0.674673,-6.047821,9.298745,-7.274508,5.955249,4.571550,8.179495,-6.186107,5.970126,-2.278612,-6.831055,-4.600254,-7.879294,-5.315799,3.997842,-7.049809,2.695270,7.955748,-4.660870,-4.890492,8.310899,1.202735,8.220869,-0.182495,1.617053,-4.149201,-2.094053,3.049460,-1.345689,5.300717,-8.235096,-5.924479,3.071798,4.641816,8.339024,6.914657,2.215701,9.425515,-3.994896,0.800719,6.511720,7.568282,-1.168785,-6.086970,-1.900396,7.737683,1.550369,-3.302617,7.504004,-3.635345,3.919828,3.115184,-4.532361,3.101559,-1.807914,3.309276,-7.511546,3.389346,8.421735,-1.377201,2.705036,-0.235317,2.559656,7.369325,-8.586074,-3.472170,5.954782,-5.090456,-1.982691,-2.155793,1.578513,-2.708112,-4.528980,-9.049730,6.798455,9.083293,-8.283656,7.810973,-7.525929,-4.375099,0.513018,-8.551638,-4.295488,-4.727336,-9.529578,1.128711,-8.653097,-9.757219,4.294225,-2.958841,0.804995,-4.695408,-7.447282,0.558634,-9.683828,0.395928,-0.497751,2.296743,5.319960,-6.584991,-9.772536,4.300764,1.599500,-3.674101,-4.192660,-1.882139,-9.035820,-0.415698,-0.600454,-0.346350,4.638057,-8.238224,3.182446,6.686150,-4.152729,2.837148,1.845600,8.175190,-0.433382,-9.704377,1.850889,-7.900924,0.892270,-4.828521,-3.429356,-2.587962,-4.542921,-6.526951,-1.385775,-9.508011,7.586611,-1.581019,-8.223742,0.388679,2.981131,-7.154150,-6.211209,-8.895394,3.098360,-3.623613,2.126542,9.604499,1.847070,-5.478829,7.338393,-4.053868,-7.036092,-4.122244,6.804662,4.355311,3.865166,2.279304,-9.151948,4.928223,-0.120813,0.854494,-2.834916,4.958729,-1.976290,-5.374837,1.073660,-4.246547,0.393572,-8.584404,2.233763,0.300318,1.981324,-5.421686,-7.808515,5.329636,6.112462,8.410108,-5.111065,-4.872607,-6.006237,-7.878062,4.123965,4.192180,4.585239,7.823892,9.709068,1.247452,8.371389,-5.829662,9.292601,-5.345229,-9.025950,5.577826,2.909962,-3.102160,-0.320162,5.247657,4.661316,-4.339958,-2.034285,9.232312,-7.916914,9.513585,7.522193,5.383577,8.711095,0.354101,4.704961,-2.245246,-3.425833,-6.690318,-0.097192,0.871133,-5.321394,-1.212567,1.507009,-1.380859,8.775191,-2.425974,5.754688,6.945191,7.537414,0.539545,8.552389,7.340218,-4.743345,-1.292046,1.955422,-3.843427,4.706284,8.181570,3.944500,-1.299689,7.377028,4.816536,2.916847,8.762572,2.898637,5.212051,9.826742,9.490206,1.974031,-1.858946,9.135609,-0.050586,9.336063,7.963314,-6.180876,7.737677,-5.132428,-3.565821,-6.268448,2.680045,-6.704880,-5.844428,5.040314,0.937274,-3.133508,-1.964755,6.073910,-9.132830,-7.505265,1.477106,-7.391808,-6.544757,8.739738,-2.898522,-2.609442,7.163534,-5.013337,-8.128783,3.604599,-0.766582,7.170057,8.169301,-8.108677,-0.925102,-1.921896,7.143495,-1.873629,7.408683,-2.139264,1.251964,6.916208,-1.371988,3.283650,-6.137982,-5.427465,-2.099165,0.110118,-2.494802,4.714998,-1.244213,-5.266393,-9.596311,8.179197,-3.911551,1.862062,-5.356004,7.687320,3.802667,-0.950855,7.403995,-5.640163,-7.280670,-6.725371,8.351236,1.384776,7.587852,0.433683,7.032865,5.433852,5.650908,2.544083,-1.732186,-6.555583,3.231049,5.710885,5.545351,-8.007585,9.512516,7.111193,0.506147,-6.455033,-3.499883,-8.364242,-1.662201,-8.570903,8.636122,8.059298,-2.513344,8.082028,-1.999233,-0.264521,-8.847429,-1.211983,6.990567,8.172802,-5.643474,8.029733,7.497690,-4.107074,-0.905636,7.196566,9.537979,7.163562,-6.916219,1.804440,3.068128,7.573213,3.340532,5.110172,8.827882,7.937941,-2.522403,-4.906428,-8.525789,0.041200,8.307028,-7.845557,2.645792,-9.738883,-3.012051,3.654524,-1.356933,-4.866658,-2.502033,-0.400341,-2.889817,3.608870,9.544043,-8.630554,9.015063,-7.489955,0.038087,3.524020,-0.707199,-9.985186,7.141666,-9.285862,-0.770159,2.012318,-1.483717,-1.649533,7.524294,0.731532,-5.778167,2.999632,2.900663,-9.364245,-3.843738,1.272171,-7.941878,-1.217223,0.979693,2.919147,8.179729,-7.580628,-0.544690,-8.980018,0.832681,-4.914703,0.558047,6.468639,2.925133,3.655187,1.362579,-2.542758,9.999749,3.046828,0.232167,-9.978466,-7.154044,-9.398946,-5.309774,-5.683932,-6.291008,7.866110,-7.652454,-3.362943,-8.107584,-9.106272,3.192232,4.963658,1.096033,6.779327,3.900378,1.168225,5.194742,5.940967,-3.338311,6.895290,-8.872769,-0.010922,8.502709,5.006951,1.360580,5.551042,-5.588652,7.343909,5.422264,2.625607,-2.436015,-6.016887,-1.216719,1.275830,-4.908942,-4.904290,3.763692,8.313161,6.519909,0.043145,-4.387362,0.486580,4.638418,-2.413369,-0.614455,-5.905005,-0.443669,-4.218008,-0.997116,5.477788,-5.549706,4.090517,4.386858,-4.257915,5.776217,1.602473,-6.917380,3.063728,4.687356,-6.520561,5.565715,-3.334036,-3.592822,-5.876092,1.713123,8.994592,5.083006,8.306209,1.384424,-9.980566,4.775728,4.769497,-9.313995,-9.592892,-8.707417,0.521814,5.657739,-3.918091,-5.419275,-2.918300,-2.048774,1.774629,-7.574055,-8.400748,-5.844102,8.864527,-0.389947,8.372051,8.171015,-5.907489,5.242257,1.150167,-5.901154,-1.866605,-4.361470,-3.293498,-7.816011,0.198145,-9.004588,-3.029126,-0.720554,0.045274,-8.721332,1.410337,-0.891846,-4.865610,-0.956480,-3.842030,6.271808,3.704250,8.943064,-0.837261,-4.523526,-5.803836,-0.545857,5.812857,-2.412051,0.823130,-5.067162,-6.762289,6.123299,-1.209894,-7.918747,-4.592892,1.068223,-8.623837,6.128104,-6.256001,-4.830905,-5.547750,8.634920,6.113785,-7.115073,3.960582,0.738779,5.402808,-5.247488,-4.555122,-0.601028,-5.001159,4.465198,-2.034807,3.947748,-9.909025,-2.608054,-8.203917,-9.277495,8.492564,8.856555,1.568184,7.164634,1.984117,-8.435695,-2.118673,-5.837973,-1.241931,5.813167,-3.155468,7.474933,-0.824663,1.767597,-2.018357,-2.332534,5.239837,-3.175010,6.492868,2.971558,1.325594,-9.245602,6.112796,-8.936649,-1.660162,-4.706802,-7.280108,7.979831,4.426427,-6.313655,4.925489,-9.076687,-5.927456,2.298224,-7.158406,-0.310461,7.151728,0.004089,6.381097,-3.604451,-0.425223,-3.643931,2.524920,3.392652,-2.452676,-3.543849,7.855690,-0.880839,3.425429,9.513552,7.055287,6.469449,-0.149564,8.205498,-6.138500,-6.123572,-3.438799,0.636550,-5.873039,3.035930,-8.110986,-2.084917,-4.897055,1.391049,1.937940,0.558793,-4.323630,7.908167,3.653498,-3.844004,-7.487335,-6.497020,2.783322,-4.984324,3.189124,3.463926,7.768082,4.928980,-5.353013,9.221035,0.922738,-3.426846,9.611147,-9.013515,-7.168698,-7.536364,4.505438,-6.357872,4.287255,7.650771,-2.437566,-8.523455,-9.696745,2.008717,6.864586,-2.431968,2.046451,-3.625739,-4.223398,4.296585,-5.871162,-1.693547,0.525092,-4.717801,8.313118,3.263801,-7.702651,-5.180843,9.801715,-1.682684,-9.925053,6.742411,5.417376,4.314620,-6.608284,2.612346,-9.230972,6.557906,-3.956154,-8.426199,6.936238,4.219003,-8.242833,-4.696739,0.640883,-8.621644,-0.346878,2.179226,4.749841,2.339605,2.435620,-2.318401,-2.329902,4.456363,-4.946964,6.483950,7.998886,1.024772,-3.656485,0.778199,-2.376533,4.139291,5.282189,2.955145,3.757469,6.155773,9.981758,7.608371,3.847109,-4.704901,-3.663225,0.915351,-1.608590,5.474944,-8.473196,-7.980565,-1.145867,8.567940,-9.294610,2.336693,-5.048458,-2.056710,-7.246300,4.679660,7.437218,3.788546,2.633896,4.967352,-9.126075,-0.543170,-1.919003,2.517832,8.370347,-8.320629,4.599765,9.089757,-6.966701,2.187526,1.275791,-7.760264,-8.641600,6.622139,-5.114034,2.485034,3.000707,-4.164327,-9.706315,8.128322,-9.123194,5.177539,7.313578,3.919227,6.044458,-4.785316,-1.240231,9.338164,0.970968,-2.517354,7.311385,-7.211756,-8.394012,-5.276567,-3.176430,-3.755974,-3.722470,0.731363,-1.574829,2.192201,0.281947,5.256285,8.301941,2.292205,0.603939,-5.065790,1.781751,6.180979,7.227134,7.463014,4.055655,4.506784,2.537551,7.282091,4.341180,4.138350,9.140827,-9.533001,2.557679,9.727642,-6.043545,-5.761948,-9.952769,2.887912,5.475161,5.427739,-1.476870,-3.984503,8.385036,6.339086,6.556599,-1.169109,9.368197,2.277149,-8.834044,7.807246,-2.148036,-2.595605,-1.030093,3.670970,-9.770127,-7.292623,0.990853,6.192487,9.943427,8.905535,8.001502,8.185422,8.009336,-4.076594,7.659505,-3.135483,6.138940,-0.502706,-8.463570,2.328746,-6.973386,2.510084,6.032172,4.718869,1.454510,7.535924,-6.082153,-8.337899,9.613332,4.401763,-2.699827,-4.559396,-7.834429,1.662969,-6.107086,-4.062548,6.306080,-1.024883,-9.663160,6.194553,5.795778,-6.133572,0.676754,8.063647,9.063848,4.879316,-2.229462,2.761208,-3.691319,2.433800,-5.599324,7.668711,6.771397,-0.107640,6.315864,9.241565,-3.603268,-3.764840,-9.402241,-4.631415,-6.878356,-1.553719,2.061850,-8.143186,-8.172453,4.021681,1.727566,-8.580058,-2.600778,-1.267188,-0.501605,-5.517777,3.501886,-3.924719,-2.947128,-1.392435,-8.555926,2.478027,-2.547594,0.745733,6.251628,2.027819,-2.841538,2.329372,-5.821950,-3.199288,-5.210123,8.207797,-4.629790,9.158394,-4.030383,0.866146,-2.346512,9.791533,-6.080770,-9.965445,7.056127,-3.224205,1.323731,-9.369552,8.908458,9.299908,-6.774188,-7.280260,-5.572141,4.783171,2.212309,-4.485830,-8.731464,-5.035237,-6.084090,-7.775316,2.405607,3.281865,0.975990,-8.674874,2.016699,-5.383661,2.512677,-4.002220,-1.628776,-7.029933,-2.357932,-7.172049,-5.614174,-2.372535,2.167514,-4.830629,4.589036,5.313222,-1.894599,-5.400780,6.521568,3.028311,9.589427,5.525504,3.399546,2.986795,-9.018833,-0.941436,-0.282072,5.015338,-7.684086,-4.196413,-0.502002,-6.050389,-0.742080,-5.865380,4.082682,-1.030754,2.183675,-1.635202,5.205475,-8.626274,4.260866,6.230163,7.027191,7.931741,-2.395116,-0.414587,-3.904430,6.948486,3.997036,-4.005016,0.835078,6.954606,-3.963069,-8.091087,3.631471,7.152503,0.687153,-0.304743,-1.302845,-2.257060,-9.562539,7.720896,3.998648,1.985968,-3.823865,1.489459,-3.881827,-2.415019,3.900198,-7.296484,5.532541,1.441825,-3.461555,-5.321074,-9.405147,-3.427341,6.780746,9.108559,-2.310848,6.613175,-9.292721,9.018753,0.673822,-6.134160,-6.370945,8.325457,-6.432371,-8.806680,-4.977570,4.340045,-8.648408,6.052245,7.406872,-5.979375,7.360606,-0.944536,2.136211,-7.287421,6.900309,7.610704,-6.960634,-0.022197,9.860347,1.649868,5.751132,-6.314764,-4.458909,0.880926,-8.117047,-5.015267,1.660451,-2.757637,-8.477996,4.893880,8.726280,6.965098,3.001649,-5.434767,-3.294729,-4.730332,7.551085,5.826767,3.206639,3.888402,9.933855,9.636972,5.554146,5.756655,7.005175,3.083837,4.223069,-2.827900,-6.065295,6.293267,-1.091898,-5.403073,8.674758,-6.128248,-2.169420,-8.289095,6.918560,-1.269208,1.122677,-3.792378,-1.113795,2.672411,-5.987191,-6.735388,5.327134,9.719121,-3.902193,5.917719,-5.393407,-2.076143,6.651502,-2.116539,-3.205035,4.462207,-1.437977,-9.334725,-5.704791,-6.970958,2.197086,6.192944,-1.737596,6.992850,3.538826,-1.294500,-1.336386,-4.968510,-8.559413,-6.502405,-4.687489,-9.641266,2.437373,7.356947,7.293890,-2.295443,3.657036,6.825680,-9.608209,-9.303088,6.969036,9.073861,8.198944,7.943728,-4.988157,-6.482981,-0.699153,0.398276,-4.838164,8.659501,-5.336368,-9.887505,3.689419,-8.969759,-4.155520,8.394297,6.643760,9.286111,0.064088,-1.875409,-1.431782,-9.619458,-6.844798,-6.712468,-5.846986,-1.460142,9.966509,-4.821276,-7.129392,2.781391,4.575908,-2.882851,7.861784,7.533401,-2.288907,9.830128,9.567094,2.022536,3.349773,-2.956533,6.539915,0.017389,7.514427,-2.796983,-0.240253,1.473030,-6.571366,-5.040348,4.834430,-9.867574,-7.146622,9.008499,3.501428,5.344783,-1.627681,1.737392,-4.131332,9.627060,-6.716781,7.336384,0.169498,5.283509,-1.940610,4.149916,4.936957,2.654423,2.437727,3.084224,-4.941191,-8.730248,-0.259820,-9.498538,-2.677863,6.592886,9.959280,2.030982,2.599869,7.828487,-6.796825,5.328738,-2.528809,7.589745,2.932284,5.786940,0.154308,1.342940,1.296831,-5.664414,4.229934,-1.399794,-2.151637,8.389503,-7.030704,1.290653,0.849577,8.232928,-1.524345,-9.762712,2.170816,2.924868,6.626670,0.183269,-4.479147,-5.920297,5.782721,4.305364,-9.983463,7.617175,7.594893,8.441538,7.946167,-9.760743,-3.598222,-4.730321,-9.393002,-9.562565,-6.996563,-0.961813,-4.300571,-6.512657,-8.819671,3.296555,-8.887498,3.287138,-0.374311,-2.874128,6.032693,4.522613,2.200052,-9.244169,7.130324,8.711903,-0.752291,-8.819733,-8.167227,-5.677784,-2.224994,8.284049,-9.554178,-6.896786,-9.077972,-0.323349,-1.817354,4.193873,5.454895,9.546508,-7.211743,-3.348728,7.895874,7.564074,2.777657,-4.010434,-2.395417,-4.008380,-4.355545,3.192146,-8.884401,3.268526,1.211921,-2.064848,-4.522809,8.957007,5.014287,5.441517,-4.631298,-4.017175,-0.736682,-1.915351,5.617849,7.568490,0.108832,-8.885332,-7.781617,-6.870276,-6.685995,8.736366,2.513196,9.965919,-4.568256,2.267538,-6.874623,7.144533,-2.757977,7.139428,-6.292577,0.192658,5.752300,2.385952,8.260912,0.898775,6.765803,-0.001137,5.825326,3.089337,-2.123486,-8.075486,-0.863568,9.412015,2.365735,-7.270014,7.082515,-7.036447,3.838835,1.254163,7.872401,-1.767863,4.786618,7.019532,3.219620,-8.405954,7.273350,-8.075059,-8.689883,-7.258797,-4.625755,-9.624859,4.561218,-1.461546,-4.967794,4.744702,-1.154853,-3.025007,0.326071,-8.818399,-7.098435,-3.381716,1.663446,-9.196724,7.064184,-1.249426,4.042860,2.321749,3.532672,-8.944471,0.436408,9.995583,8.229685,3.004774,-1.401175,2.476834,9.186664,-2.611235,-2.839986,-6.685496,-3.708307,4.017635,6.352712,-7.811304,-2.272595,5.935556,-6.498074,3.853138,-4.114941,-3.218122,-8.112745,-5.194611,-1.151180,4.094660,3.097394,-8.095785,-6.141831,0.804451,-6.351404,-0.082665,-6.476104,0.908856,-9.811099,5.817674,9.684697,4.788550,3.515937,3.982765,9.797971,5.726153,9.342668,-2.089331,7.910348,1.894324,2.658127,6.823803,9.483241,-2.035154,8.551518,1.421744,-3.830266,6.162083,-2.289583,1.942148,9.914351,-3.365364,-9.542659,-7.296814,-5.617554,1.996907,7.665399,-5.442109,8.165492,-8.093377,-8.658322,-5.728172,2.132152,-5.393807,-1.183588,1.174476,-9.393968,-0.139735,-0.939705,1.810053,0.690913,-4.921644,2.357235,4.879561,4.303485,3.712436,6.184342,-8.134264,1.372487,-2.596030,-6.883039,8.606587,1.030723,5.885899,-9.829727,2.572321,-4.389462,-0.890941,-1.835315,-7.629535,-9.459291,5.786156,4.225594,-1.288915,-8.426282,8.302691,-2.398523,-1.461059,-8.498186,0.558732,-6.711351,-7.197998,-2.854603,-2.613990,6.530773,-4.424061,-7.924951,5.434637,-0.042088,6.002604,9.214874,0.059422,9.637091,8.856247,-3.687200,8.563551,1.319796,0.141335,-8.124691,-9.975914,-7.345881,9.899246,-3.980893,3.652392,-1.129843,-7.855264,8.910092,4.585158,7.421725,-9.983232,9.711584,-0.691484,-5.555959,-3.431639,7.437786,-5.729226,-4.722667,-5.504751,-4.577009,7.974952,-9.650379,-3.085192,8.632816,2.399574,8.273570,-5.494104,8.551884,0.589289,-7.673230,-2.893032,7.851494,-2.020585,5.451425,-2.853061,-6.241417,-9.250925,4.144975,-3.806727,4.520370,0.875840,1.028351,4.473020,-9.944138,-6.930781,7.630555,-4.777922,2.604774,-9.724829,-9.695025,2.661183,-2.768808,5.937210,-7.990295,-5.792527,7.703571,-8.400382,-2.470405,4.904855,2.748923,3.453405,4.416005,9.651949,-6.528553,9.755566,-8.245595,4.966725,-2.193762,0.982476,-0.419344,-6.399368,3.258673,0.865402,4.788538,9.575652,-3.077713,3.249996,-6.459861,6.122307,-7.710550,1.771624,2.003821,7.561502,-9.379330,-0.128629,-6.837756,-9.112571,-6.799201,3.620258,9.485024,-6.621432,-0.155772,4.568369,-4.271069,9.212101,1.119403,1.484835,-1.170377,-0.749421,7.463227,5.384304,-1.509423,-9.575490,5.576140,-8.802816,-2.225454,2.345381,-3.960932,7.945145,9.279682,1.774070,-9.967454,0.268113,1.887012,8.191751,-2.825820,-5.314029,-1.830389,2.465006,9.004014,-9.218119,-8.304461,-7.335651,-1.033591,4.219998,-4.095903,-9.965098,-9.383572,6.133163,-9.499788,-5.030944,-7.973632,0.062761,5.327319,-9.866429,-4.743545,-9.720121,-7.996769,2.189416,1.423388,-3.150194,2.886341,-7.004079,-2.989698,6.904747,-8.495329,-9.488121,-2.516469,1.950668,-6.086724,-0.491065,3.109597,-2.945956,1.319127,-2.902369,-0.953770,8.816193,-3.807903,8.894753,4.922292,1.544585,3.003824,-3.478852,1.706828,2.229574,-5.809614,-6.880057,3.007588,4.460829,-1.291725,8.941818,5.383244,-2.694051,-0.610072,-8.646666,-0.581655,8.508072,6.559557,6.119881,4.237431,8.940314,7.366495,9.555418,-6.202687,3.231080,3.900459,2.803298,1.593168,-1.763146,-7.699742,-6.696737,-5.875924,-6.094232,4.040777,-7.145309,-9.005363,-8.313590,2.978158,-3.165053,2.278338,-7.394993,-8.173723,5.324774,8.577741,7.456519,-8.611696,-6.625436,1.381740,5.860216,-1.543816,-5.604483,2.121146,-1.120430,-9.605849,-8.101304,9.283851,-2.247646,-7.636923,7.238293,7.864913,3.089365,-4.154175,-4.578848,-9.668185,0.816362,1.136377,-5.964438,-8.352221,0.245167,5.946171,-8.527778,-8.531374,9.274718,-5.991025,-2.420338,7.652076,-5.130432,8.236179,-0.893399,-9.287202,6.111638,9.139960,-9.057260,-9.684570,-0.599115,5.426008,-6.855552,-6.626987,-3.851819,8.872246,-4.626361,4.348404,-9.612032,-8.632935,-3.271402,-4.139771,-5.852229,4.367982,-6.905775,1.541409,-7.054255,7.275185,-9.424948,-4.807935,8.225327,-8.480135,-8.060995,-8.185291,-3.494979,6.585343,6.704720,-2.835558,1.526139,-5.252948,-5.742725,3.194313,-7.198176,2.614607,-4.689378,0.042043,7.134919,1.189575,3.578550,7.412607,-5.739330,7.516714,-1.019340,-3.463880,0.206433,2.980647,-1.091151,-2.019872,-4.764545,9.064589,1.869963,-2.122025,-2.972701,6.407978,4.841357,-8.502636,3.994355,9.853878,2.849679,-6.730065,-7.632221,-5.033563,-7.510318,2.333353,1.685192,5.713437,2.872838,5.021820,0.849866,-6.553791,6.799366,0.412093,-5.148547,6.796095,-4.678850,-6.631914,8.466098,1.667923,-1.626992,-8.701439,1.506567,-8.704523,2.586494,8.134336,-4.536873,8.596197,-9.773917,3.688025,6.202109,-2.093772,-0.273686,-6.754772,-8.144173,1.796488,-0.353521,-7.959046,8.847871,7.069581,-8.144152,4.489999,-4.185137,4.743364,9.945835,9.145957,5.854308,-2.146690,-8.097859,9.088184,-1.512225,3.421810,2.862384,4.681923,0.270823,8.812613,0.477140,-8.545243,-4.891763,-7.900597,-2.237956,-4.110908,2.824244,2.377932,-6.786930,-8.291649,2.227947,3.153993,4.204216,8.430698,1.947990,2.586964,-0.746240,-6.266176,3.883375,-1.962559,-4.316959,7.563938,-7.327248,-5.417341,3.984032,7.000085,-9.139610,6.372877,6.608624,-5.515366,-5.304180,0.142647,-2.917643,7.550204,-7.302088,3.793699,-7.640447,5.337605,-9.487059,7.189228,-4.463600,-8.774197,-2.338570,7.161722,6.940786,-7.088913,3.549123,-8.765361,-7.566588,9.564155,6.191747,7.134007,9.511279,-3.078166,-3.395814,2.916018,9.345887,-5.967469,-1.570468,3.270972,6.823201,3.226831,-5.774510,-3.305167,3.274682,2.742861,6.890555,-8.720034,7.942233,-4.664182,5.984848,2.971110,5.811924,-0.048099,1.282918,6.985716,2.185556,0.032338,-8.744108,-6.985474,5.129439,0.240937,1.183930,9.322901,-3.071328,-8.885644,4.108948,-5.819043,6.644015,-6.111792,3.417230,-6.637676,-4.389440,-0.582189,8.869602,-5.658911,-9.216248,2.754927,-0.233627,4.842320,-8.469317,-0.062360,5.717795,6.359688,6.905138,8.952580,3.000990,5.011868,6.840480,5.204465,5.650165,1.227600,8.000563,2.595408,3.276915,-8.190971,-6.902391,3.113105,-9.501517,8.356943,6.732439,-4.367217,-4.272588,-6.498443,0.108177,-4.141557,-9.534542,-3.258403,7.929301,3.207275,-5.699622,-9.461842,-8.690540,-9.646716,-9.039100,-8.053651,-6.583067,4.780482,-7.276146,-9.838217,6.407247,-8.162581,-2.178299,8.530808,-9.143486,-8.549007,-6.018225,-2.038130,2.945595,5.647976,-1.224797,4.016897,-9.098857,9.961149,-3.703558,-2.322304,-0.715930,2.492153,-4.503834,-2.397090,1.728850,7.522253,-4.740019,-6.725051,9.509355,9.735318,9.651335,-6.851706,8.882208,5.296444,-6.993140,9.056811,-4.606265,0.629036,9.738519,-4.433199,8.621020,1.303261,9.097846,4.798955,2.726963,-9.010804,2.909215,6.799135,-4.085977,-1.153440,-3.997912,6.290759,5.669771,3.946968,2.875881,0.520335,-4.009091,-6.260797,6.649570,-2.288215,-2.804316,1.803732,3.657860,2.984934,9.615756,-7.238737,5.635070,3.282906,0.905406,-4.062687,-1.457468,8.991883,-1.037234,-6.719898,8.659297,-8.408223,4.456872,7.406107,-4.164707,-4.037183,-1.925176,-5.399992,-5.417124,-0.410024,-1.427243,-4.022556,6.952259,7.924049,3.913617,8.188712,-5.630816,7.333071,1.595382,5.945483,1.453114,-7.102156,-2.436316,5.694302,-0.993043,-0.508798,-2.908426,0.064035,-2.709910,0.442820,-6.140443,-8.613413,8.093835,-8.146996,-0.710809,-3.262466,3.370734,-9.505217,9.204715,-9.169073,9.107722,6.881858,-3.212671,7.425515,9.770703,-3.560240,0.860601,1.720829,-6.178497,-8.851037,2.775318,-4.287875,4.956275,-0.414939,4.536460,-9.614370,-8.301217,-9.310430,-5.311376,3.946812,3.783112,3.949794,0.560223,2.244670,-4.155242,-3.958220,-2.056342,-4.439943,9.600864,9.274182,6.101300,-7.589636,0.541327,-9.683543,-4.543979,5.333411,-5.817584,1.377030,6.038781,0.613646,-1.117435,3.889547,2.172087,-4.899518,9.338416,2.158494,4.550551,-8.808089,-2.024689,-4.858705,-5.021574,-3.316998,-5.779524,-7.935002,-3.257340,5.886629,-7.111662,-2.875278,-2.656579,-2.254144,-1.995990,-8.498756,2.091222,-3.368760,-7.087092,4.353935,-2.859632,5.688850,7.884661,0.641781,4.230245,-4.255093,9.690483,8.294377,4.795423,9.825790,9.979360,9.822668,-7.777281,9.985377,-1.549546,-2.120454,-7.991745,9.220203,7.201132,-6.809711,8.225462,-0.804270,7.178153,-9.138862,-8.212281,-9.698495,8.542607,-9.762442,8.171224,-1.941394,-9.830003,-4.703152,-3.458398,-9.765147,-4.241407,5.614808,8.337052,6.815564,8.898532,7.057162,2.602682,-1.349914,5.609765,6.313547,-8.727027,-0.858454,-6.072956,0.827299,-5.651569,-9.291886,-4.838158,-0.951619,-6.331347,-9.099116,2.699592,8.116132,4.976121,-5.306230,-7.970489,0.682623,8.044578,-0.304895,6.131181,4.806388,5.141579,-1.519786,1.770870,-7.694667,-7.673625,5.542313,-7.545637,1.494680,-2.483465,2.909067,6.158948,7.004072,-1.140593,-1.225198,-6.893335,-1.875661,5.253124,3.781067,3.070681,-1.105230,7.459445,-7.620134,-8.460601,0.108743,5.779400,-9.859810,-6.603447], dtype = "float64")#candidate|2768|(2640,)|const|float64
call_2767 = relay.TupleGetItem(func_2220_call(relay.reshape(const_2768.astype('float64'), [11, 16, 15])), 1)
call_2769 = relay.TupleGetItem(func_2222_call(relay.reshape(const_2768.astype('float64'), [11, 16, 15])), 1)
output = relay.Tuple([call_2713,call_2767,const_2768,])
output2 = relay.Tuple([call_2714,call_2769,const_2768,])
func_2780 = relay.Function([], output)
mod['func_2780'] = func_2780
mod = relay.transform.InferType()(mod)
output = func_2780()
func_2781 = relay.Function([], output)
mutated_mod['func_2781'] = func_2781
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1383_call = mod.get_global_var('func_1383')
func_1384_call = mutated_mod.get_global_var('func_1384')
call_2790 = relay.TupleGetItem(func_1383_call(), 0)
call_2791 = relay.TupleGetItem(func_1384_call(), 0)
var_2792 = relay.var("var_2792", dtype = "float32", shape = (10, 7, 12))#candidate|2792|(10, 7, 12)|var|float32
bop_2793 = relay.logical_or(call_2790.astype('bool'), relay.reshape(var_2792.astype('bool'), relay.shape_of(call_2790))) # shape=(10, 7, 12)
bop_2796 = relay.logical_or(call_2791.astype('bool'), relay.reshape(var_2792.astype('bool'), relay.shape_of(call_2791))) # shape=(10, 7, 12)
output = bop_2793
output2 = bop_2796
func_2800 = relay.Function([var_2792,], output)
mod['func_2800'] = func_2800
mod = relay.transform.InferType()(mod)
var_2801 = relay.var("var_2801", dtype = "float32", shape = (10, 7, 12))#candidate|2801|(10, 7, 12)|var|float32
output = func_2800(var_2801)
func_2802 = relay.Function([var_2801], output)
mutated_mod['func_2802'] = func_2802
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2832 = relay.var("var_2832", dtype = "int32", shape = (4, 14, 9))#candidate|2832|(4, 14, 9)|var|int32
var_2833 = relay.var("var_2833", dtype = "int32", shape = (4, 14, 9))#candidate|2833|(4, 14, 9)|var|int32
bop_2834 = relay.bitwise_or(var_2832.astype('int32'), relay.reshape(var_2833.astype('int32'), relay.shape_of(var_2832))) # shape=(4, 14, 9)
func_2105_call = mod.get_global_var('func_2105')
func_2107_call = mutated_mod.get_global_var('func_2107')
call_2856 = relay.TupleGetItem(func_2105_call(), 2)
call_2857 = relay.TupleGetItem(func_2107_call(), 2)
output = relay.Tuple([bop_2834,call_2856,])
output2 = relay.Tuple([bop_2834,call_2857,])
func_2859 = relay.Function([var_2832,var_2833,], output)
mod['func_2859'] = func_2859
mod = relay.transform.InferType()(mod)
mutated_mod['func_2859'] = func_2859
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2859_call = mutated_mod.get_global_var('func_2859')
var_2861 = relay.var("var_2861", dtype = "int32", shape = (4, 14, 9))#candidate|2861|(4, 14, 9)|var|int32
var_2862 = relay.var("var_2862", dtype = "int32", shape = (4, 14, 9))#candidate|2862|(4, 14, 9)|var|int32
call_2860 = func_2859_call(var_2861,var_2862,)
output = call_2860
func_2863 = relay.Function([var_2861,var_2862,], output)
mutated_mod['func_2863'] = func_2863
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2986 = relay.const([[[0.781419,1.393413,-5.209871,-7.612132,8.538081,-2.838935,-4.064859,8.070184,2.836348,-9.943578,4.581017,-7.748508,-9.590722,-7.489560],[3.025283,-6.785828,-2.822210,9.022379,5.116617,9.693679,5.059624,2.813555,2.921895,8.527783,-4.737662,4.430111,8.788291,9.220795],[5.751771,-3.194017,-9.562686,7.108909,-8.328764,5.377854,7.143139,1.664432,-3.246377,-7.666152,1.391210,-6.232439,-2.802961,1.333490]],[[-3.063263,3.705736,9.673422,-3.427731,-6.870864,-2.229914,-0.054097,-5.944276,5.493422,5.992820,-6.455704,4.129511,7.616381,7.870926],[6.516446,9.533695,-6.539106,-8.869885,2.415136,4.015365,-2.923372,-9.439247,6.282386,-8.115337,-7.351447,-6.855382,-3.238436,-0.845005],[4.958086,3.167071,1.656895,-5.624613,6.681578,6.481437,8.922374,-1.510108,-9.550541,7.000488,-6.808737,-0.166709,8.933820,7.814034]],[[0.094327,1.785205,-2.275238,3.411619,-3.046717,4.010182,-2.116944,-0.383329,4.915974,-2.062522,0.849698,4.550447,9.385455,8.952845],[-7.306142,-9.712618,-6.031421,-5.202425,-3.075318,-7.199670,-8.508107,-4.311930,-7.465423,-7.387254,-6.911290,-8.423847,-9.008397,1.518343],[2.762205,-8.576872,9.051075,2.966460,0.962289,-6.145632,-3.891289,-5.302607,-4.879249,7.605243,6.839392,-3.693126,-3.496045,8.837882]],[[-3.626659,7.001301,7.709326,1.746189,-1.759860,8.064530,3.992119,-3.645309,-3.381349,-3.897475,1.439862,-6.873279,1.930793,-1.760117],[1.924132,5.098651,-8.336208,9.587570,-2.099161,3.108166,-8.033997,-4.513417,-1.547355,9.503364,2.609404,-2.783310,7.065009,7.549248],[8.274157,9.075864,-2.457125,0.853943,7.493210,-0.334239,6.558608,-0.463156,-1.876461,9.048365,0.687465,-7.080768,-6.141044,-3.357981]],[[6.497484,2.905519,0.198202,6.404647,5.933653,7.948713,9.791824,-1.970288,5.929506,-6.969760,-4.522598,-0.454782,-5.438222,-4.898513],[7.414438,7.279396,9.411875,-5.951680,2.164763,-5.485483,-7.063519,7.564336,7.006454,-2.585203,-4.979832,7.105880,2.992704,9.379165],[-4.089857,-2.933252,-9.104168,-6.603765,-5.521407,-0.935005,-7.787885,-3.220309,-2.196991,-6.336801,-1.969847,-6.555476,-3.407126,6.886508]],[[-4.010802,3.512846,-2.878154,-2.121781,4.348868,-0.571809,4.433939,7.940174,3.626052,-9.373679,6.181607,-8.739298,-8.364498,0.520642],[-2.687855,-6.170651,5.638700,7.325301,9.099913,-6.578884,-7.210432,2.772961,1.036204,4.926199,-6.428667,6.263890,-3.866972,6.924774],[-3.949482,5.591954,5.791918,0.543952,-6.684909,6.427989,2.614188,-3.548036,-0.709679,4.733495,2.871255,8.043460,5.897202,4.206331]],[[-1.517568,-7.522484,2.645235,9.683400,2.606076,4.175182,0.291796,5.533178,-7.307547,-5.024164,6.355404,9.600006,-7.792616,6.151709],[7.833634,4.781036,3.151991,-3.991167,-3.479246,-1.568721,1.687179,2.721775,-3.939578,2.844355,-1.035615,3.425901,9.644974,-3.119945],[9.334432,6.170135,8.854725,-3.447444,-5.335233,2.131332,-5.743437,-8.454518,-1.447985,-6.452524,0.983986,5.834724,7.850667,8.292266]],[[8.980121,-3.949995,7.186238,4.074303,4.618610,-4.840591,5.944724,-6.006279,7.719567,3.949001,-4.286122,-5.942800,3.527217,5.395541],[-7.510138,8.897440,8.152048,7.116587,-7.857203,7.663156,-7.114519,1.439809,9.053259,-6.618901,7.861452,-3.272477,3.195852,1.868572],[9.083765,-8.969032,5.542892,6.829204,8.091195,-5.494177,-5.655072,7.588848,4.580116,-0.531352,-0.847885,9.828427,-2.072059,9.564910]],[[-5.124070,-2.187505,-1.715497,7.513446,-8.144165,-8.264915,6.377725,2.711565,-3.404138,9.701279,-6.497253,-9.287297,-2.795415,-8.300906],[-1.059967,-6.150966,-5.090905,-8.523456,9.259504,-3.654113,-0.870420,-8.435812,2.007042,9.635088,-4.124463,0.343614,-0.498322,-8.463877],[7.044000,9.238087,-2.346221,-7.763317,-8.111956,4.286729,7.532297,-0.488532,-2.374413,1.295536,-5.647060,5.679969,3.448153,3.898341]],[[2.251570,-3.809415,-8.130801,-9.579044,-5.825998,4.432658,4.503058,-6.262919,7.864636,-4.554743,6.402232,3.389639,5.730120,9.163858],[-0.909640,-1.338710,-0.745071,-3.859637,6.636744,0.222584,-5.643797,-3.982807,-3.132916,-5.692761,3.001954,5.318021,-6.917019,1.683726],[-2.394196,9.555653,8.461869,-4.780563,-3.583864,4.360164,6.813245,7.851131,7.304478,1.781859,0.928499,8.476187,-5.055664,6.633212]],[[-8.418319,-3.485551,7.767471,1.554148,-0.906119,-2.863520,-1.753359,-1.793370,3.705611,9.462535,2.073923,-7.777616,-4.392548,-9.364700],[-3.883773,-9.346953,-8.622577,4.320195,-8.645695,-3.907844,-5.306316,8.580334,-4.001522,-1.330234,-2.750736,8.559924,-9.034833,-4.965638],[9.958584,-0.988781,-3.952213,-1.907476,7.298834,4.343689,-5.796560,-8.055278,-3.194763,-6.417911,2.431539,-2.662452,-1.121237,-8.695859]],[[9.677441,-4.970428,8.877513,0.329690,0.169418,-5.663653,2.784734,-8.914123,8.567701,9.516574,-8.713811,9.949148,-6.431703,8.511158],[7.225820,-0.572352,-3.605938,9.196609,0.903622,-9.860904,5.860161,3.739407,-6.237798,-7.984200,0.371805,1.881224,7.741418,8.256269],[0.743300,3.864757,-7.242830,9.201337,-4.634692,-7.188537,0.549264,-8.966564,7.907680,-0.620159,6.967663,-6.602493,-0.131298,-6.447899]]], dtype = "float32")#candidate|2986|(12, 3, 14)|const|float32
uop_2987 = relay.log2(const_2986.astype('float32')) # shape=(12, 3, 14)
output = uop_2987
output2 = uop_2987
func_2989 = relay.Function([], output)
mod['func_2989'] = func_2989
mod = relay.transform.InferType()(mod)
output = func_2989()
func_2990 = relay.Function([], output)
mutated_mod['func_2990'] = func_2990
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1754_call = mod.get_global_var('func_1754')
func_1755_call = mutated_mod.get_global_var('func_1755')
call_3029 = relay.TupleGetItem(func_1754_call(), 1)
call_3030 = relay.TupleGetItem(func_1755_call(), 1)
func_468_call = mod.get_global_var('func_468')
func_470_call = mutated_mod.get_global_var('func_470')
call_3033 = relay.TupleGetItem(func_468_call(), 2)
call_3034 = relay.TupleGetItem(func_470_call(), 2)
uop_3052 = relay.acos(call_3033.astype('float32')) # shape=(9, 9, 13)
uop_3054 = relay.acos(call_3034.astype('float32')) # shape=(9, 9, 13)
func_1064_call = mod.get_global_var('func_1064')
func_1066_call = mutated_mod.get_global_var('func_1066')
call_3069 = func_1064_call()
call_3070 = func_1064_call()
func_1787_call = mod.get_global_var('func_1787')
func_1789_call = mutated_mod.get_global_var('func_1789')
call_3075 = relay.TupleGetItem(func_1787_call(relay.reshape(call_3069.astype('float64'), [9, 9, 13])), 0)
call_3076 = relay.TupleGetItem(func_1789_call(relay.reshape(call_3069.astype('float64'), [9, 9, 13])), 0)
output = relay.Tuple([call_3029,uop_3052,call_3069,call_3075,])
output2 = relay.Tuple([call_3030,uop_3054,call_3070,call_3076,])
func_3081 = relay.Function([], output)
mod['func_3081'] = func_3081
mod = relay.transform.InferType()(mod)
output = func_3081()
func_3082 = relay.Function([], output)
mutated_mod['func_3082'] = func_3082
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2572_call = mod.get_global_var('func_2572')
func_2574_call = mutated_mod.get_global_var('func_2574')
call_3146 = func_2572_call()
call_3147 = func_2572_call()
output = relay.Tuple([call_3146,])
output2 = relay.Tuple([call_3147,])
func_3161 = relay.Function([], output)
mod['func_3161'] = func_3161
mod = relay.transform.InferType()(mod)
mutated_mod['func_3161'] = func_3161
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3161_call = mutated_mod.get_global_var('func_3161')
call_3162 = func_3161_call()
output = call_3162
func_3163 = relay.Function([], output)
mutated_mod['func_3163'] = func_3163
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3206 = relay.const(3, dtype = "uint16")#candidate|3206|()|const|uint16
var_3207 = relay.var("var_3207", dtype = "uint16", shape = (1, 2, 3))#candidate|3207|(1, 2, 3)|var|uint16
bop_3208 = relay.bitwise_and(const_3206.astype('uint16'), var_3207.astype('uint16')) # shape=(1, 2, 3)
output = bop_3208
output2 = bop_3208
func_3239 = relay.Function([var_3207,], output)
mod['func_3239'] = func_3239
mod = relay.transform.InferType()(mod)
mutated_mod['func_3239'] = func_3239
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3240 = relay.var("var_3240", dtype = "uint16", shape = (1, 2, 3))#candidate|3240|(1, 2, 3)|var|uint16
func_3239_call = mutated_mod.get_global_var('func_3239')
call_3241 = func_3239_call(var_3240)
output = call_3241
func_3242 = relay.Function([var_3240], output)
mutated_mod['func_3242'] = func_3242
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2403_call = mod.get_global_var('func_2403')
func_2405_call = mutated_mod.get_global_var('func_2405')
call_3329 = relay.TupleGetItem(func_2403_call(), 0)
call_3330 = relay.TupleGetItem(func_2405_call(), 0)
func_1958_call = mod.get_global_var('func_1958')
func_1960_call = mutated_mod.get_global_var('func_1960')
call_3349 = relay.TupleGetItem(func_1958_call(), 0)
call_3350 = relay.TupleGetItem(func_1960_call(), 0)
uop_3355 = relay.asin(call_3329.astype('float32')) # shape=(9, 9, 13)
uop_3357 = relay.asin(call_3330.astype('float32')) # shape=(9, 9, 13)
output = relay.Tuple([call_3349,uop_3355,])
output2 = relay.Tuple([call_3350,uop_3357,])
func_3368 = relay.Function([], output)
mod['func_3368'] = func_3368
mod = relay.transform.InferType()(mod)
mutated_mod['func_3368'] = func_3368
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3368_call = mutated_mod.get_global_var('func_3368')
call_3369 = func_3368_call()
output = call_3369
func_3370 = relay.Function([], output)
mutated_mod['func_3370'] = func_3370
mutated_mod = relay.transform.InferType()(mutated_mod)
func_536_call = mod.get_global_var('func_536')
func_537_call = mutated_mod.get_global_var('func_537')
call_3399 = relay.TupleGetItem(func_536_call(), 1)
call_3400 = relay.TupleGetItem(func_537_call(), 1)
func_2710_call = mod.get_global_var('func_2710')
func_2712_call = mutated_mod.get_global_var('func_2712')
call_3421 = relay.TupleGetItem(func_2710_call(), 0)
call_3422 = relay.TupleGetItem(func_2712_call(), 0)
output = relay.Tuple([call_3399,call_3421,])
output2 = relay.Tuple([call_3400,call_3422,])
func_3436 = relay.Function([], output)
mod['func_3436'] = func_3436
mod = relay.transform.InferType()(mod)
output = func_3436()
func_3437 = relay.Function([], output)
mutated_mod['func_3437'] = func_3437
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1754_call = mod.get_global_var('func_1754')
func_1755_call = mutated_mod.get_global_var('func_1755')
call_3539 = relay.TupleGetItem(func_1754_call(), 0)
call_3540 = relay.TupleGetItem(func_1755_call(), 0)
output = call_3539
output2 = call_3540
func_3543 = relay.Function([], output)
mod['func_3543'] = func_3543
mod = relay.transform.InferType()(mod)
mutated_mod['func_3543'] = func_3543
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3543_call = mutated_mod.get_global_var('func_3543')
call_3544 = func_3543_call()
output = call_3544
func_3545 = relay.Function([], output)
mutated_mod['func_3545'] = func_3545
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3436_call = mod.get_global_var('func_3436')
func_3437_call = mutated_mod.get_global_var('func_3437')
call_3572 = relay.TupleGetItem(func_3436_call(), 0)
call_3573 = relay.TupleGetItem(func_3437_call(), 0)
func_2859_call = mod.get_global_var('func_2859')
func_2863_call = mutated_mod.get_global_var('func_2863')
const_3578 = relay.const([-2,3,-10,2,6,-1,-4,-3,3,10,-6,4,3,3,8,2,9,-7,10,8,-7,-6,1,-2,1,-8,-3,2,-2,5,-5,1,-2,2,8,-1,10,-3,-7,5,7,2,-6,5,1,9,6,-9,-8,2,2,10,1,3,10,-5,-9,-8,-3,-2,-4,-2,3,-1,-4,-7,-8,-8,-10,-8,-7,9,2,-3,-10,-1,8,-5,9,-1,8,-1,5,-7,2,-9,-10,7,4,7,4,10,-3,2,10,-7,1,7,7,5,1,10,-2,1,6,-2,8,-4,-7,-5,2,-5,7,-3,8,-6,1,10,3,-1,-1,-3,5,4,-6,8,8,-2,-7,-3,-2,6,5,9,7,-10,3,1,-1,-9,-3,-6,2,8,-1,-4,2,-6,-6,-8,3,5,-9,3,1,-8,10,-5,-10,-10,6,3,6,6,2,-6,9,-10,-8,-2,-8,-3,-6,9,-3,-8,6,6,9,-3,5,-8,1,-5,-3,-5,-9,9,9,1,8,-1,-1,4,1,10,7,2,-8,-6,-6,-1,-1,10,8,-2,-1,9,-1,1,-2,-10,1,-6,3,-9,3,5,2,-4,9,7,10,-1,10,-3,-4,-1,8,-3,1,9,-4,2,2,-4,-3,-10,-6,-3,4,9,10,-5,1,-9,-2,8,3,-9,7,5,-6,-10,7,-1,9,10,-1,-10,-3,-5,-5,10,-5,2,-6,-2,1,7,5,-8,-7,6,3,10,-2,2,10,-7,3,-8,6,1,2,-7,5,3,-4,-8,4,-5,-3,-6,-1,9,-4,-4,9,-2,-5,-9,-4,2,3,5,8,-8,8,-5,8,-6,-2,-5,-8,-1,-5,5,5,5,7,-7,-3,7,8,-4,-7,1,1,-2,2,-5,-8,-4,8,-10,3,-10,-2,-10,1,7,4,-9,3,-7,-9,-1,3,-7,-9,5,-4,-8,4,-7,4,2,3,7,7,2,-6,-10,-2,-1,-5,3,-3,-6,-1,-1,8,-6,-9,8,7,-9,-6,-6,-7,9,3,-1,-3,5,-9,-2,2,-9,-1,4,-6,-2,3,1,5,1,-10,-6,9,-8,8,9,-7,8,3,3,6,-2,-3,8,-10,6,3,-4,3,-5,1,-10,10,6,1,-5,-7,7,-9,-8,6,-1,-7,-1,7,1,10,8,-9,-3,4,-7,-4,-10,1,-4,-3,-6,-9,9,5,-8,1,-2,8,1,3,4,-4,10,4,2,8,8,-7,7,-8,6,9,-10,-5,-1,-10,-8,3,2,2,7,-4,-9,-3,-4,9,10,9,-7,2,-3,-4,1,-8,7,6,2,-8,-2,7,-1,5,-6,-5,9,10,-2,-4,4], dtype = "int32")#candidate|3578|(504,)|const|int32
call_3577 = relay.TupleGetItem(func_2859_call(relay.reshape(const_3578.astype('int32'), [4, 14, 9]), relay.reshape(const_3578.astype('int32'), [4, 14, 9]), ), 1)
call_3579 = relay.TupleGetItem(func_2863_call(relay.reshape(const_3578.astype('int32'), [4, 14, 9]), relay.reshape(const_3578.astype('int32'), [4, 14, 9]), ), 1)
output = relay.Tuple([call_3572,call_3577,const_3578,])
output2 = relay.Tuple([call_3573,call_3579,const_3578,])
func_3584 = relay.Function([], output)
mod['func_3584'] = func_3584
mod = relay.transform.InferType()(mod)
mutated_mod['func_3584'] = func_3584
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3584_call = mutated_mod.get_global_var('func_3584')
call_3585 = func_3584_call()
output = call_3585
func_3586 = relay.Function([], output)
mutated_mod['func_3586'] = func_3586
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3617 = relay.var("var_3617", dtype = "float64", shape = (6, 6, 15))#candidate|3617|(6, 6, 15)|var|float64
uop_3618 = relay.erf(var_3617.astype('float64')) # shape=(6, 6, 15)
uop_3621 = relay.acosh(uop_3618.astype('float32')) # shape=(6, 6, 15)
output = uop_3621
output2 = uop_3621
func_3624 = relay.Function([var_3617,], output)
mod['func_3624'] = func_3624
mod = relay.transform.InferType()(mod)
var_3625 = relay.var("var_3625", dtype = "float64", shape = (6, 6, 15))#candidate|3625|(6, 6, 15)|var|float64
output = func_3624(var_3625)
func_3626 = relay.Function([var_3625], output)
mutated_mod['func_3626'] = func_3626
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3647 = relay.const([[[-5.406524,6.697793,6.250241,6.638982,6.256224,-5.337746,-1.890302,-1.994568,-3.123119],[6.611889,2.113983,-8.885986,-9.000249,2.057211,5.715513,3.158935,9.858711,-9.074776],[-4.096714,3.610452,-5.745346,-9.280056,-8.060221,-3.010803,0.831787,-1.018953,7.937212],[5.351857,6.560370,-5.753160,7.652297,-6.574035,-4.179160,1.803634,-6.020531,-6.530256],[4.354488,7.668917,5.504312,-7.909320,7.644890,6.800490,-6.908226,-4.930991,-1.597874],[-0.760503,7.916577,-3.519483,8.880613,-9.014212,-6.312720,9.790635,8.887971,1.886026],[-1.805255,-5.460477,-3.131276,-6.357799,-1.405566,-9.308203,9.692375,7.889509,0.727752],[-3.727642,6.819346,-9.041666,-9.202583,2.507790,-1.117273,-1.617514,4.014879,1.247178],[4.590950,-9.968059,-0.075228,-9.325189,7.126408,-3.466365,5.764870,-8.611879,2.403275],[-8.033335,-2.765513,-8.272072,-3.417371,1.622462,9.604160,-9.015523,-9.226191,-2.217271],[3.355776,5.423860,-7.324169,-5.505846,-9.674213,5.811250,2.210571,8.051063,4.579739],[7.230017,8.922138,3.598860,3.457232,3.242770,-5.661443,-6.628808,-9.685623,0.464632],[-6.259299,-0.560249,-9.331471,-7.262208,6.323558,1.533157,4.377934,-3.139726,4.474936],[2.818335,0.615354,-0.002653,6.913750,-2.694820,-5.108452,-4.188693,0.677758,-7.246425],[-9.096735,9.720778,-0.349133,8.485284,0.097248,-0.677289,2.055395,9.701824,-4.869021],[5.207596,4.195896,4.523952,0.494673,-6.306831,-2.132318,-9.647312,1.902882,-4.906459]],[[-1.883469,-2.647260,-3.022301,-3.534330,-7.561423,-8.768476,4.931825,-8.351735,6.836127],[3.343819,-6.049218,9.634871,-5.092149,0.905622,-6.457175,8.270421,6.442004,-4.626156],[1.168413,-0.363273,7.165623,-2.355702,-7.530354,0.522433,7.756480,-9.364953,-3.552127],[-7.080361,9.200365,-7.754157,-6.498850,-0.288226,8.170821,0.878267,6.180351,0.564489],[-4.523412,9.361376,-1.090825,5.603782,8.021137,2.468350,2.849917,-6.165592,-7.521111],[-7.491840,7.397744,-4.973255,-4.521464,1.339210,7.069523,-9.456033,-8.418280,-5.130977],[-0.514824,-0.920445,8.280974,9.214118,-6.501900,8.834512,-5.128814,4.072716,-9.049001],[8.562004,8.603787,-3.138630,5.358471,-2.246435,8.358397,-7.381082,-3.896306,5.205620],[4.175752,5.526502,9.888847,-5.101917,-1.906590,1.334199,7.622647,3.248058,9.190552],[-0.537581,-9.311927,-0.659695,8.062875,9.588271,-5.755340,-4.170211,9.032086,5.574687],[-4.056940,7.932593,1.566831,-5.830011,3.984637,6.742966,9.988915,6.404176,-6.557382],[5.849093,-1.942416,-2.915915,-4.241436,-1.121224,-3.396065,-3.863667,4.308059,6.864005],[-5.314162,-4.919783,-0.024584,-3.977451,9.524197,4.211798,8.374638,4.838315,-8.324649],[-2.238133,-9.429258,-2.265836,-0.870095,-6.192822,-1.693812,-6.731798,8.807155,-7.447982],[-1.626113,5.480279,-7.080471,-4.305926,-3.083958,-5.993976,1.125497,8.506971,1.470734],[-3.998179,-1.070687,-4.478716,-9.498781,2.456546,5.115682,1.511035,-7.425828,5.349731]],[[-1.376293,-7.785817,4.731718,8.738603,-3.058728,5.333296,-4.528377,3.051164,-1.112351],[-5.837368,5.664642,-5.059097,9.841272,-4.172418,-6.503598,9.614312,9.535354,4.836501],[-2.934760,5.254643,8.664665,-1.862816,-4.344601,-6.647171,6.601348,-6.730726,-9.247182],[7.077100,-7.401652,3.618915,4.745091,3.878184,4.335366,-8.707007,6.188291,-3.874605],[-1.198274,1.560375,-9.374727,9.327202,-2.561246,-9.531228,-6.911595,-3.189288,-8.972002],[1.507231,-3.754229,-8.218031,-0.235986,0.040531,3.967618,-2.386468,4.319134,-4.052925],[-4.331011,4.887431,2.614441,0.160363,-0.763798,7.742868,-2.333059,-9.525171,8.807978],[-1.003407,2.521301,-7.205387,1.799857,-9.066956,-4.293018,-2.438772,-9.990613,4.786096],[-1.287483,1.767571,-3.510318,4.242620,-4.245015,-0.639322,-1.262033,9.676830,-0.246294],[-3.155450,-5.145308,-1.381856,-3.584843,0.812341,4.168294,-7.942307,-5.807652,-6.963504],[-7.064597,7.837131,5.451215,7.034318,-5.392323,-1.010903,-4.372721,-8.364051,1.975623],[4.005024,2.409330,3.840274,0.867318,-9.386366,5.679994,-3.442309,-3.091574,-9.219968],[1.255158,-9.176320,-1.410134,2.507362,7.570121,-1.541301,-0.182501,-8.836319,-7.008738],[-4.067072,-3.101934,1.777516,9.679207,6.229916,7.305049,-4.738000,4.144477,-8.829481],[7.559568,-4.301432,1.077850,5.692946,-4.185919,-8.823036,1.630887,-7.861721,7.079991],[-3.708486,-6.919131,0.248812,7.050647,-7.793556,-7.351723,1.231719,-0.101986,-9.122168]],[[-3.145194,-2.222210,-6.621994,6.671669,1.640810,7.222460,-1.050932,-9.401812,8.963972],[-0.238124,3.406816,-7.257125,-2.464038,5.307805,3.313382,-4.528099,6.814404,7.278106],[7.649727,-5.264514,-3.964037,-7.559262,1.896999,8.211513,-9.437283,4.027187,0.171770],[9.947081,8.077334,-9.072547,-0.905769,-7.574240,5.979191,6.712286,3.657288,-6.136819],[0.471543,-7.540840,6.062409,-5.534802,9.564982,0.427729,6.565726,-9.160129,8.249719],[4.032822,-5.962667,8.967533,6.764341,-2.658815,-2.500111,1.385832,1.475049,-6.671300],[0.305602,-3.049262,8.534272,9.774320,-7.644147,8.499244,4.600340,-2.109733,7.657588],[0.140922,-1.008709,0.547646,-5.366317,9.755402,-4.769529,-9.220736,-1.988359,-1.742846],[-8.832756,-3.025618,-0.273723,-2.120877,-0.534408,8.203608,9.480933,3.232523,-7.126176],[-5.388066,0.121218,0.505468,-8.425481,4.736011,-1.286236,-4.141476,-7.625345,-6.105098],[-6.942856,-8.748277,8.526180,-1.784405,-1.617912,-5.447949,-8.399388,-9.154276,-8.075962],[6.601248,7.985718,5.167433,7.228747,3.881176,-3.002068,-4.716345,-0.760374,-7.406420],[-1.820662,-5.954879,-7.082219,4.286500,-1.047531,-2.089311,3.812367,9.506491,-4.626027],[7.085609,-7.957741,8.985160,-6.871818,5.078937,-7.891990,-0.810171,7.166176,-8.615931],[9.843032,-3.294221,2.760509,5.139530,1.174973,5.759818,3.960590,7.378684,8.018948],[1.003845,-6.086144,5.380179,-4.520290,6.641388,-3.293913,6.655203,1.200328,0.046686]],[[-0.678939,-6.578098,4.196812,2.150323,-9.970744,-8.609609,-4.601859,5.361578,8.032260],[1.975754,-7.946009,9.363030,-4.440193,-0.865210,-9.436221,-5.600822,-9.974803,-9.983856],[3.377550,5.721478,-3.465149,0.268497,0.371777,7.643982,3.130596,-6.849846,5.897320],[6.419425,-6.502140,-2.015002,6.071912,3.246375,6.626979,-7.060169,8.697503,-0.315843],[5.065918,-3.548657,-5.313061,2.756816,1.385637,2.426875,8.497854,-2.862508,-8.264438],[6.303066,-9.515694,-9.381677,-3.915406,-1.474646,-2.224291,-4.197568,-2.433022,-0.727029],[-4.245207,1.594010,8.362622,2.322098,9.750517,-2.068357,-7.536792,9.650254,-5.130470],[-8.240524,-7.902205,-7.490620,0.146159,8.564822,-7.564365,-8.837433,8.960027,-8.956071],[-8.106354,-6.871551,9.579581,6.144345,-6.779510,-2.537673,-4.881084,1.449759,6.236973],[1.208056,-1.906576,2.705043,-9.963043,-7.790134,3.856676,-3.810320,-0.118454,6.708013],[6.007294,2.441099,9.163287,-9.056054,-0.123052,3.330035,-7.364847,-4.661161,3.295432],[0.899160,9.899965,2.764815,-7.017806,-9.946079,-1.217155,-5.389420,-5.164005,5.480305],[-6.155549,-8.528310,-7.465844,-1.789713,-7.967757,1.091349,-3.402049,-6.644860,-8.382084],[-0.866867,8.402405,6.149878,-2.934824,-1.182046,2.264433,9.045749,9.299526,-0.969389],[0.583968,-1.696066,2.254226,8.108773,-4.867409,2.095220,2.414982,8.034806,-2.974347],[7.769450,3.336308,-3.773839,4.947978,-9.236679,2.529075,-6.002715,9.640634,-9.671580]],[[6.211751,5.390271,8.028546,-7.418410,-3.807486,-4.399794,2.347156,-1.484240,0.753872],[9.732876,-6.116281,5.522174,7.551729,-4.303722,6.514094,2.084426,-8.364701,-7.640376],[-6.907891,-5.873704,4.734393,2.047483,-2.369871,7.555102,-2.257250,1.239718,-8.698414],[-9.123379,-6.355088,-8.515035,-3.666152,-5.265150,-9.064035,-5.770123,-6.201912,-6.317442],[5.632249,-8.843596,5.741216,5.482471,-3.750798,-3.635038,-3.037173,-4.759337,4.690257],[-1.098313,9.723511,-4.172865,1.491007,-1.529559,7.319749,5.745383,-5.176803,0.643751],[1.788910,-8.378856,5.360215,-8.274809,3.835626,-1.368856,-9.742590,-9.828364,-7.095089],[8.168984,-0.639973,2.755204,-6.242003,-5.690870,-9.491387,-6.716557,6.833632,9.812080],[5.466225,-5.515414,2.608541,3.382126,1.733740,1.052559,-5.565536,8.689739,-4.939236],[1.068216,-5.576151,4.410301,4.385142,-1.201822,-3.294995,0.907911,-0.874613,2.129585],[-5.562738,9.331301,-1.681903,4.098822,6.821901,2.046854,3.361275,2.562561,0.105897],[-7.278779,-9.794433,1.554830,7.287571,6.335668,-6.574887,2.158344,0.208392,-7.639058],[2.183150,5.466490,-3.324120,-6.897147,9.840408,9.398874,-2.053183,2.079268,1.936729],[-2.823983,0.314173,-0.773875,-2.528391,-8.058589,-4.555038,6.743558,4.427162,-2.434587],[-5.187095,5.129392,-3.145203,-9.276129,0.970152,-7.223653,-0.951240,5.965698,-4.239723],[3.750176,4.723708,-9.446196,-6.451885,7.239838,-1.991088,9.562433,-0.158319,-8.020220]],[[-2.174500,1.229390,-7.198333,-0.128265,-7.339791,-7.965737,5.076417,1.336429,-6.942354],[-8.816320,-2.144548,-4.012866,1.177047,9.574148,-8.792684,2.923175,-4.081806,-1.879411],[-0.109896,7.624972,-6.311455,8.266503,2.935448,-2.676888,-0.201207,-6.593395,-3.537460],[-3.007507,-6.225752,3.717120,3.179123,5.246138,-7.303496,3.522480,-9.696432,9.470495],[-9.950689,-9.577525,-3.542250,1.891718,1.111040,9.319453,-1.885997,-8.876086,5.775191],[-1.625013,-1.593710,-0.041402,3.402975,9.896333,-5.334147,2.868060,2.213510,-0.881777],[-9.761984,-5.413221,4.745966,-8.638949,5.354881,-5.202250,-3.622015,-2.598688,7.576531],[9.837045,-3.655228,-1.338820,-9.932425,3.472474,-7.265969,0.664150,-4.975400,-6.700676],[1.126393,6.186255,2.345298,1.862379,-7.095760,-0.836232,-6.192330,2.310989,-7.979875],[0.926188,6.450610,-5.863715,-7.635791,-0.498509,-6.615844,-3.721905,0.392867,-4.926827],[2.435508,8.035587,6.964557,0.892335,2.318935,-1.298972,7.288336,-2.653162,2.143205],[-9.463099,-1.255234,-6.045417,7.716158,-0.263310,-7.875848,-1.961397,-2.829658,-9.018368],[0.558988,9.750904,-1.560286,6.283094,5.838229,-4.714718,-7.114616,-9.200149,0.304642],[9.597027,4.515702,-8.917930,0.534689,-4.086160,-6.458736,6.785835,-1.186414,-6.885423],[6.753930,-4.303638,-1.301291,6.486399,6.182225,6.456347,-2.217051,-4.075520,7.839493],[2.086336,0.472088,-1.679482,-7.368555,0.959325,8.849901,0.965618,1.298651,7.672684]],[[-8.689762,4.919780,8.956117,1.535662,6.558650,4.233331,-3.884945,6.992671,-9.549310],[1.901119,-9.879630,-8.138144,-4.151679,-5.326154,0.048241,1.133501,-7.824241,-2.690682],[-4.406630,1.945727,3.567010,-2.664325,6.226453,5.596247,5.618330,6.706479,0.265520],[9.913425,9.602707,-3.800765,-3.237434,4.847822,-0.057123,-5.622038,8.849996,-2.825404],[-1.396682,-2.769747,1.781851,-3.721489,-5.908437,-3.515274,0.883915,3.318764,1.405275],[3.897174,-1.029688,-3.598829,-6.605918,3.647949,-8.033786,-8.277468,-1.525635,-1.923950],[-1.895876,-4.276603,-4.269422,4.191607,6.004033,6.544245,-6.355032,-1.222484,9.331599],[4.019710,0.580576,6.266608,-0.890469,-4.737716,-1.852509,-2.481216,0.234527,7.755467],[4.112753,4.970137,4.238660,0.004826,-4.506469,-7.712716,-8.580206,1.873267,-2.057456],[4.291385,2.473222,3.107554,5.062835,-5.794068,7.104998,-9.159430,-1.387739,6.460335],[-6.838717,9.982369,-0.498977,-1.720759,1.081300,-8.975631,-1.257456,7.128512,4.771235],[3.105664,-5.129922,-1.631985,7.161632,8.770005,-6.748911,-5.742340,1.043618,2.748438],[0.042815,6.898003,-5.031237,3.124167,8.245137,-8.764011,6.704310,9.143130,3.406333],[7.063130,4.359122,8.200469,2.107299,-8.845727,6.569692,-5.275148,-8.873637,-7.525492],[3.043979,5.881131,-9.908046,-1.904939,-2.804147,6.664526,9.922504,-9.698412,8.490605],[-1.422092,4.681889,-5.016294,2.999894,-8.954872,-4.790848,-4.889175,-7.406021,-6.455438]],[[2.111409,-4.448208,0.640242,2.426836,3.886295,3.540182,2.448418,4.678915,-7.311717],[-3.188560,7.772243,4.832472,0.768560,0.185643,-7.976547,-9.821811,-6.341078,0.628637],[-9.410818,-0.241379,-8.808417,6.215468,-7.215317,0.513324,-4.830266,-9.746909,-5.420010],[7.732904,9.006034,5.384048,-0.232011,4.565476,-4.029153,-1.698335,3.053644,-4.727251],[-9.006321,-6.598460,5.307043,-9.337267,2.938180,6.003607,-6.708470,0.640441,9.540920],[6.085212,-2.169818,3.200898,9.217731,2.214376,-1.510018,4.599320,3.575300,0.878391],[6.033903,-2.971704,-9.184954,-4.245757,-4.198347,-1.370855,-1.277115,-7.961918,-2.056659],[1.568961,6.447975,5.781918,5.278197,5.108132,-8.160056,3.428827,-6.794356,-4.657179],[2.179567,3.448937,-7.714023,9.375721,-0.480521,5.431837,0.551382,-7.441010,2.321009],[2.266587,-0.884478,-1.282432,1.035234,-1.702354,1.475095,1.833259,1.295107,9.093494],[-7.211343,-3.076973,-0.019008,-6.504716,4.907878,-9.152760,-9.471422,0.806438,-3.827690],[3.826169,0.969876,4.221983,-2.071482,0.946545,-0.307862,2.616591,5.593331,8.660777],[0.489809,-0.269590,-7.458129,9.727998,-5.990422,-1.258906,-1.886914,-8.333355,2.500508],[0.256278,-9.321268,-5.528793,5.156278,-3.108661,4.188612,-2.881152,7.039922,9.673111],[7.129764,-3.143741,1.985614,9.777155,-8.857676,1.608668,0.828759,1.192445,6.978052],[-9.219396,8.155402,-0.498072,-1.284377,3.758921,6.140801,-2.953068,6.159870,-9.037705]],[[5.667612,0.139384,7.138958,1.304211,8.576615,0.511578,-4.160775,7.160164,-3.406747],[3.822348,-6.867169,-5.357227,6.053793,-0.391736,3.810525,-9.438137,-2.382610,-8.610210],[-9.978724,7.642832,-8.648430,1.936808,-0.304748,-2.282438,-2.188396,-2.047817,-8.093827],[-5.527175,4.964053,-9.515071,6.796228,0.418038,-1.613625,6.603143,4.479742,-1.216873],[7.254265,4.887233,-4.628935,-0.925583,5.045262,8.351421,5.148449,2.551880,1.893250],[5.469660,-5.199459,-5.268080,-2.887348,-7.748194,-0.806556,3.251921,-6.108140,-8.536832],[-3.572594,9.394638,1.280749,9.011150,-9.603380,1.161182,0.725168,-1.004905,9.598826],[-4.614330,-4.414998,9.704532,-2.953443,0.970104,5.582837,7.644356,-2.633991,5.423001],[-1.713519,1.566756,-4.140759,-0.503756,5.372493,4.955927,0.229267,0.814350,-7.975397],[7.862961,8.817178,0.773766,-4.498127,7.154510,9.223830,-5.329661,9.194118,-4.213805],[-3.149543,2.215984,6.109438,-3.855043,1.775160,1.653822,-7.007311,-6.791818,8.463885],[7.031200,-3.852037,-2.711261,2.578943,0.648047,-7.658881,-4.060488,-0.989749,5.513436],[3.946476,6.391955,5.989369,-1.175656,5.521757,0.215584,7.886326,-8.647473,8.303094],[1.234702,5.061874,-2.185533,2.484126,-1.310720,-5.223003,4.524803,8.475987,-1.974035],[5.730631,-1.613792,0.114439,9.116099,-0.137268,6.389197,9.073657,8.997319,0.177982],[-1.808699,-3.989684,4.445439,-9.668888,-4.951593,1.898141,-2.968696,-5.788904,8.002315]],[[5.936025,-9.664161,-3.832853,1.046773,-5.613624,-9.550577,-1.752663,-9.999419,7.106574],[-2.366434,9.442807,3.800640,6.371586,6.220514,-9.074150,-4.545558,-0.881939,-4.537635],[-0.142803,-3.006725,-5.975553,-3.029870,4.538154,2.865920,-9.336902,2.143888,5.266373],[-7.062407,-7.320123,-2.505900,-0.851921,-4.726019,0.607611,0.357507,8.462797,-8.496707],[-9.466480,-1.862336,-3.316243,-8.626844,3.129534,-3.726053,-8.638317,-8.447237,-8.536656],[-3.481390,4.303172,3.010276,6.662128,-9.995492,-2.193973,-9.416228,5.418839,0.748298],[-1.840273,8.439252,3.997886,-5.811193,-5.457689,-7.635248,5.586244,-5.925862,-2.986361],[6.359841,-4.024634,-8.651592,5.159129,-6.325241,0.447485,-2.204159,8.305649,-7.085617],[1.995258,4.986575,9.240938,-6.969800,-8.636985,1.996832,3.662690,-3.012554,-9.360984],[-7.083640,7.110625,-7.084284,-5.086720,-1.148519,-6.170700,-6.861112,-9.913697,-0.251172],[-3.477420,-5.514048,3.192418,9.484220,2.416253,-9.087474,-7.246549,5.866903,5.940953],[-4.552316,-9.557245,-4.203100,5.271315,-7.722086,-1.158053,9.218943,3.103124,5.815826],[1.292970,7.921848,-6.573632,-9.870536,6.544762,-1.220361,-6.469791,-1.687208,4.522234],[3.349773,-8.897298,-1.176446,-5.652370,9.961365,-7.119589,-9.197963,6.470592,-1.743109],[-5.762676,-2.239264,-7.070665,-0.879420,6.264138,3.517502,0.853252,-0.941814,-3.930871],[-8.720598,-3.030063,-6.718966,-0.843551,6.518003,9.915436,2.105839,-9.469318,9.020991]]], dtype = "float32")#candidate|3647|(11, 16, 9)|const|float32
uop_3648 = relay.cos(const_3647.astype('float32')) # shape=(11, 16, 9)
func_2710_call = mod.get_global_var('func_2710')
func_2712_call = mutated_mod.get_global_var('func_2712')
call_3663 = relay.TupleGetItem(func_2710_call(), 0)
call_3664 = relay.TupleGetItem(func_2712_call(), 0)
uop_3672 = relay.cosh(uop_3648.astype('float32')) # shape=(11, 16, 9)
output = relay.Tuple([call_3663,uop_3672,])
output2 = relay.Tuple([call_3664,uop_3672,])
func_3675 = relay.Function([], output)
mod['func_3675'] = func_3675
mod = relay.transform.InferType()(mod)
output = func_3675()
func_3676 = relay.Function([], output)
mutated_mod['func_3676'] = func_3676
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1714_call = mod.get_global_var('func_1714')
func_1715_call = mutated_mod.get_global_var('func_1715')
call_3737 = relay.TupleGetItem(func_1714_call(), 0)
call_3738 = relay.TupleGetItem(func_1715_call(), 0)
output = relay.Tuple([call_3737,])
output2 = relay.Tuple([call_3738,])
func_3769 = relay.Function([], output)
mod['func_3769'] = func_3769
mod = relay.transform.InferType()(mod)
mutated_mod['func_3769'] = func_3769
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3769_call = mutated_mod.get_global_var('func_3769')
call_3770 = func_3769_call()
output = call_3770
func_3771 = relay.Function([], output)
mutated_mod['func_3771'] = func_3771
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3769_call = mod.get_global_var('func_3769')
func_3771_call = mutated_mod.get_global_var('func_3771')
call_3790 = relay.TupleGetItem(func_3769_call(), 0)
call_3791 = relay.TupleGetItem(func_3771_call(), 0)
func_2324_call = mod.get_global_var('func_2324')
func_2326_call = mutated_mod.get_global_var('func_2326')
call_3795 = relay.TupleGetItem(func_2324_call(relay.reshape(call_3790.astype('float32'), [9, 9, 13])), 1)
call_3796 = relay.TupleGetItem(func_2326_call(relay.reshape(call_3790.astype('float32'), [9, 9, 13])), 1)
func_433_call = mod.get_global_var('func_433')
func_434_call = mutated_mod.get_global_var('func_434')
call_3802 = func_433_call()
call_3803 = func_433_call()
uop_3822 = relay.exp(call_3790.astype('float32')) # shape=(9, 9, 13)
uop_3824 = relay.exp(call_3791.astype('float32')) # shape=(9, 9, 13)
output = relay.Tuple([call_3795,call_3802,uop_3822,])
output2 = relay.Tuple([call_3796,call_3803,uop_3824,])
func_3834 = relay.Function([], output)
mod['func_3834'] = func_3834
mod = relay.transform.InferType()(mod)
output = func_3834()
func_3835 = relay.Function([], output)
mutated_mod['func_3835'] = func_3835
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3161_call = mod.get_global_var('func_3161')
func_3163_call = mutated_mod.get_global_var('func_3163')
call_3854 = relay.TupleGetItem(func_3161_call(), 0)
call_3855 = relay.TupleGetItem(func_3163_call(), 0)
func_2324_call = mod.get_global_var('func_2324')
func_2326_call = mutated_mod.get_global_var('func_2326')
call_3856 = relay.TupleGetItem(func_2324_call(relay.reshape(call_3854.astype('float32'), [9, 9, 13])), 0)
call_3857 = relay.TupleGetItem(func_2326_call(relay.reshape(call_3854.astype('float32'), [9, 9, 13])), 0)
output = relay.Tuple([call_3854,call_3856,])
output2 = relay.Tuple([call_3855,call_3857,])
func_3874 = relay.Function([], output)
mod['func_3874'] = func_3874
mod = relay.transform.InferType()(mod)
output = func_3874()
func_3875 = relay.Function([], output)
mutated_mod['func_3875'] = func_3875
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2403_call = mod.get_global_var('func_2403')
func_2405_call = mutated_mod.get_global_var('func_2405')
call_3876 = relay.TupleGetItem(func_2403_call(), 1)
call_3877 = relay.TupleGetItem(func_2405_call(), 1)
func_1537_call = mod.get_global_var('func_1537')
func_1540_call = mutated_mod.get_global_var('func_1540')
call_3879 = relay.TupleGetItem(func_1537_call(relay.reshape(call_3876.astype('float32'), [9, 9, 13])), 0)
call_3880 = relay.TupleGetItem(func_1540_call(relay.reshape(call_3876.astype('float32'), [9, 9, 13])), 0)
bop_3881 = relay.greater_equal(call_3876.astype('bool'), relay.reshape(call_3879.astype('bool'), relay.shape_of(call_3876))) # shape=(9, 9, 13)
bop_3884 = relay.greater_equal(call_3877.astype('bool'), relay.reshape(call_3880.astype('bool'), relay.shape_of(call_3877))) # shape=(9, 9, 13)
output = relay.Tuple([bop_3881,])
output2 = relay.Tuple([bop_3884,])
func_3886 = relay.Function([], output)
mod['func_3886'] = func_3886
mod = relay.transform.InferType()(mod)
mutated_mod['func_3886'] = func_3886
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3886_call = mutated_mod.get_global_var('func_3886')
call_3887 = func_3886_call()
output = call_3887
func_3888 = relay.Function([], output)
mutated_mod['func_3888'] = func_3888
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3900 = relay.const([[[2.627872,4.607781,6.826528,-8.873314,-6.725348,1.608753,-3.119298,9.207556,-8.801219,-2.227957,-9.375893,4.474009,8.559658],[-8.551531,2.933325,-1.475490,2.070984,-5.205902,-7.652439,-2.575783,-5.697320,6.786342,6.748807,8.006699,7.730708,-3.081084],[-9.917860,1.333720,2.490146,-5.587186,0.788929,-0.934509,7.302693,9.180143,9.965568,-0.754994,4.087426,-8.258607,4.892810],[-2.826085,7.591279,-1.894821,8.675128,-4.931665,6.851538,7.771454,7.180073,8.766571,-6.995130,-3.056893,-0.138211,9.384701]],[[-3.808260,9.732523,-0.144994,-4.031219,-8.528273,4.693925,-0.748377,9.850701,2.260178,-5.590452,-9.249516,1.166920,4.177069],[-9.230857,-6.831859,2.527661,5.583832,-9.726307,9.509028,7.015764,5.223941,4.158280,-8.391808,0.148546,0.204121,-5.542458],[-9.845891,-5.270879,9.957358,6.019690,9.840470,0.997495,8.368928,-0.609779,-3.603531,8.833975,-5.491522,-7.131161,8.708033],[-9.617742,1.754140,-2.191436,-5.214427,2.526893,0.473997,-6.341334,-8.276811,8.121870,2.941291,-9.281717,3.470982,-4.579693]],[[-7.745950,1.301910,-6.405993,-3.132201,-8.181211,6.958674,9.733842,9.579785,-2.308572,6.481384,7.780591,-4.429481,-1.010439],[-6.318548,-1.023601,-2.639556,1.929690,-3.263937,3.341002,-6.858136,4.330074,1.435006,-2.610201,4.308726,-9.823430,3.574032],[6.723492,-7.641599,-3.112755,-6.109797,3.813269,7.156827,-1.545321,8.549261,-2.231896,5.850749,4.030176,8.609153,5.648101],[-1.850924,1.436334,7.795105,-4.379969,6.908625,9.613436,9.100111,-1.341315,3.508694,3.746255,-7.416743,-6.415591,6.216390]],[[-4.940088,-9.281678,-8.608847,9.981267,-7.607307,-3.548764,9.053233,-8.055530,8.038146,4.785172,-1.556827,-0.733409,3.037669],[-9.553848,1.824454,-0.626181,-2.730655,1.363671,8.581667,-7.979857,-1.513891,-4.903143,-0.685793,-7.820419,3.915367,9.957081],[-3.086434,2.984566,3.392609,-8.503013,7.097724,-5.177175,0.518498,-1.967977,6.764612,-7.195036,-3.291615,9.486656,5.380761],[-8.503325,9.714784,3.064768,-8.565415,-3.232478,-8.184485,-0.133917,3.550532,8.441736,-4.624922,7.147890,-2.127529,9.548994]],[[5.512340,-5.809510,-6.275381,4.221036,-9.173053,-9.365956,9.615255,-2.070439,5.170257,7.393601,-5.823660,6.471924,0.880117],[-2.072140,-8.075082,-1.831510,-2.878659,5.365638,4.258189,-4.335766,0.899817,-4.611598,1.412221,-6.076063,1.931958,3.598159],[-2.864658,3.579978,-5.157117,8.313595,1.329577,-4.870800,-4.670127,7.922393,-9.908200,-1.440635,-9.898001,-7.511848,9.965794],[-1.664924,-0.931492,-2.680703,-3.309031,-6.554736,3.319706,4.063916,5.806834,-0.747614,7.947153,-4.209874,-5.970315,1.805625]]], dtype = "float32")#candidate|3900|(5, 4, 13)|const|float32
const_3901 = relay.const([[[-1.384985,-2.409969,-0.546304,5.451330,8.030380,-1.660431,-6.493445,-9.488495,-6.583823,7.395889,8.951665,-1.381231,-9.266958],[-3.199821,0.084931,1.585416,7.585826,-4.615007,-1.064003,-1.895563,1.001948,-8.553670,6.151879,-4.336267,-6.781467,-6.447745],[-5.377383,5.580345,5.692524,6.948091,-4.384981,8.785542,-8.085126,1.745461,1.118645,2.882340,-7.071920,-6.240315,-0.784922],[7.741261,-9.547198,-3.152448,2.091950,5.190632,-2.345262,3.713300,6.666549,-0.078508,1.904061,-5.285248,6.636122,5.774390]],[[2.441835,3.590191,-7.879901,2.127343,6.908711,-2.456131,5.372671,2.987457,-4.738280,-0.428667,2.575151,1.739559,-5.908738],[6.357197,9.210836,8.978936,-6.876694,-4.613338,-9.625994,9.839664,-0.162502,-8.251274,8.803224,6.596290,-4.963535,3.727254],[-6.543868,-5.005540,1.833811,-6.802683,1.373941,6.556642,6.144359,-6.253660,1.392796,6.567421,0.619672,-3.288247,6.248877],[-8.886758,8.536747,-3.950570,9.069904,6.497282,-8.395645,4.553423,4.216210,-7.158890,8.445548,-6.850312,-8.427869,-1.143777]],[[4.034406,8.558331,-1.984461,9.273371,9.638699,8.663954,-0.268454,6.854764,-3.503495,-9.051713,-9.126420,-5.937969,-7.041537],[-5.167928,-3.182256,-9.555182,8.975770,0.604515,-4.100258,-9.375548,-5.907813,-0.661312,-4.692851,2.919447,-6.974697,-4.142864],[-2.637473,-2.518839,-8.760248,-9.172451,8.682201,-2.071009,-2.359537,-1.795860,-6.999695,-7.249166,-6.683881,-7.198735,6.923397],[-8.715775,8.183844,-4.220806,5.792020,-4.511251,2.693169,5.182788,-5.437371,-1.469286,6.986614,9.383773,6.060427,-5.117621]],[[-1.548906,-4.260677,-1.720162,8.966455,7.824383,-5.337876,2.280392,-3.032099,1.389437,5.027556,-0.803004,-1.523393,5.204829],[3.402932,0.204882,-9.613698,-5.526312,6.169377,6.661379,4.516921,-6.198270,-2.743079,-2.869525,8.241347,-9.828799,7.524602],[-8.782183,-2.269304,1.070352,-3.116204,2.376639,-5.268651,5.292326,-0.185998,7.551893,2.618651,1.295331,2.340951,6.365267],[5.844348,2.477566,-7.211546,-1.061839,8.520785,-4.626053,4.589850,8.216500,-5.966036,8.180183,7.305626,-4.470616,6.102417]],[[-4.214258,1.034241,8.827590,3.508582,-5.044411,-1.389907,-2.437525,-1.999075,3.457445,-1.324814,-1.921237,0.404959,-6.849160],[-2.847504,6.176753,-3.379890,-2.269489,5.169814,7.830694,-4.182256,-2.964904,-5.157849,8.078641,-8.558908,-5.935174,7.178284],[2.743378,4.060214,6.389039,-5.141471,6.763003,5.999927,-3.237267,6.359420,9.143274,2.817196,-1.581692,4.842527,6.020437],[-3.147632,-7.755709,-3.460070,-8.066659,4.445372,4.516332,-1.541913,9.254891,-4.706612,4.278552,9.685622,5.419782,-1.220578]]], dtype = "float32")#candidate|3901|(5, 4, 13)|const|float32
bop_3902 = relay.mod(const_3900.astype('float32'), relay.reshape(const_3901.astype('float32'), relay.shape_of(const_3900))) # shape=(5, 4, 13)
output = relay.Tuple([bop_3902,])
output2 = relay.Tuple([bop_3902,])
func_3911 = relay.Function([], output)
mod['func_3911'] = func_3911
mod = relay.transform.InferType()(mod)
mutated_mod['func_3911'] = func_3911
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3911_call = mutated_mod.get_global_var('func_3911')
call_3912 = func_3911_call()
output = call_3912
func_3913 = relay.Function([], output)
mutated_mod['func_3913'] = func_3913
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1383_call = mod.get_global_var('func_1383')
func_1384_call = mutated_mod.get_global_var('func_1384')
call_3935 = relay.TupleGetItem(func_1383_call(), 1)
call_3936 = relay.TupleGetItem(func_1384_call(), 1)
output = call_3935
output2 = call_3936
func_3939 = relay.Function([], output)
mod['func_3939'] = func_3939
mod = relay.transform.InferType()(mod)
mutated_mod['func_3939'] = func_3939
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3939_call = mutated_mod.get_global_var('func_3939')
call_3940 = func_3939_call()
output = call_3940
func_3941 = relay.Function([], output)
mutated_mod['func_3941'] = func_3941
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1383_call = mod.get_global_var('func_1383')
func_1384_call = mutated_mod.get_global_var('func_1384')
call_4007 = relay.TupleGetItem(func_1383_call(), 1)
call_4008 = relay.TupleGetItem(func_1384_call(), 1)
output = call_4007
output2 = call_4008
func_4014 = relay.Function([], output)
mod['func_4014'] = func_4014
mod = relay.transform.InferType()(mod)
output = func_4014()
func_4015 = relay.Function([], output)
mutated_mod['func_4015'] = func_4015
mutated_mod = relay.transform.InferType()(mutated_mod)
func_363_call = mod.get_global_var('func_363')
func_364_call = mutated_mod.get_global_var('func_364')
call_4016 = relay.TupleGetItem(func_363_call(), 1)
call_4017 = relay.TupleGetItem(func_364_call(), 1)
output = call_4016
output2 = call_4017
func_4018 = relay.Function([], output)
mod['func_4018'] = func_4018
mod = relay.transform.InferType()(mod)
mutated_mod['func_4018'] = func_4018
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4018_call = mutated_mod.get_global_var('func_4018')
call_4019 = func_4018_call()
output = call_4019
func_4020 = relay.Function([], output)
mutated_mod['func_4020'] = func_4020
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4021 = relay.var("var_4021", dtype = "int8", shape = (6, 8, 2))#candidate|4021|(6, 8, 2)|var|int8
var_4022 = relay.var("var_4022", dtype = "int8", shape = (6, 8, 2))#candidate|4022|(6, 8, 2)|var|int8
bop_4023 = relay.right_shift(var_4021.astype('int8'), relay.reshape(var_4022.astype('int8'), relay.shape_of(var_4021))) # shape=(6, 8, 2)
func_2859_call = mod.get_global_var('func_2859')
func_2863_call = mutated_mod.get_global_var('func_2863')
var_4030 = relay.var("var_4030", dtype = "int32", shape = (504,))#candidate|4030|(504,)|var|int32
call_4029 = relay.TupleGetItem(func_2859_call(relay.reshape(var_4030.astype('int32'), [4, 14, 9]), relay.reshape(var_4030.astype('int32'), [4, 14, 9]), ), 0)
call_4031 = relay.TupleGetItem(func_2863_call(relay.reshape(var_4030.astype('int32'), [4, 14, 9]), relay.reshape(var_4030.astype('int32'), [4, 14, 9]), ), 0)
func_2859_call = mod.get_global_var('func_2859')
func_2863_call = mutated_mod.get_global_var('func_2863')
call_4037 = relay.TupleGetItem(func_2859_call(relay.reshape(var_4030.astype('int32'), [4, 14, 9]), relay.reshape(var_4030.astype('int32'), [4, 14, 9]), ), 1)
call_4038 = relay.TupleGetItem(func_2863_call(relay.reshape(var_4030.astype('int32'), [4, 14, 9]), relay.reshape(var_4030.astype('int32'), [4, 14, 9]), ), 1)
uop_4046 = relay.atan(var_4030.astype('float32')) # shape=(504,)
output = relay.Tuple([bop_4023,call_4029,call_4037,uop_4046,])
output2 = relay.Tuple([bop_4023,call_4031,call_4038,uop_4046,])
func_4056 = relay.Function([var_4021,var_4022,var_4030,], output)
mod['func_4056'] = func_4056
mod = relay.transform.InferType()(mod)
mutated_mod['func_4056'] = func_4056
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4056_call = mutated_mod.get_global_var('func_4056')
var_4058 = relay.var("var_4058", dtype = "int8", shape = (6, 8, 2))#candidate|4058|(6, 8, 2)|var|int8
var_4059 = relay.var("var_4059", dtype = "int8", shape = (6, 8, 2))#candidate|4059|(6, 8, 2)|var|int8
var_4060 = relay.var("var_4060", dtype = "int32", shape = (504,))#candidate|4060|(504,)|var|int32
call_4057 = func_4056_call(var_4058,var_4059,var_4060,)
output = call_4057
func_4061 = relay.Function([var_4058,var_4059,var_4060,], output)
mutated_mod['func_4061'] = func_4061
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4236 = relay.const([[[-9.584203,-0.785920,2.990998,4.113341,-5.997693,6.727460,-8.228243,-1.725063,7.904113,-8.340906,-4.875176,-9.838432,-0.368493],[2.139273,4.722710,-1.357277,-4.000713,4.972952,-1.722817,5.918523,-3.318073,-3.881101,-3.113110,-2.013344,8.761975,7.282271],[-8.886921,2.264765,0.546686,-7.108416,4.756114,3.820929,5.033139,2.032420,6.659143,-6.215827,-9.896723,-4.749470,7.310400]],[[-1.216996,-9.364224,6.883801,7.504313,7.665533,1.832543,4.263736,0.745488,-7.656819,7.965858,-9.380675,-5.210094,-3.004363],[2.512025,-1.549289,-5.443725,4.188758,-6.464322,2.576804,9.013298,1.168972,-9.670572,-7.472692,9.888195,-5.979272,-2.624231],[5.006547,4.494641,1.343186,0.962742,9.259039,-6.413461,-3.828243,5.436135,-2.875367,-7.770778,5.823956,-8.317784,-2.453712]],[[2.471723,-0.539535,7.659658,-8.237054,-7.294802,5.566554,1.818984,5.809664,7.041172,0.862844,4.505643,-8.668238,5.897248],[-7.697184,5.970553,1.950638,5.990723,-5.806411,6.256156,4.482045,0.810115,3.891251,7.543467,-5.789009,-4.145089,-0.745842],[-3.418399,-9.248909,-7.606511,9.797652,2.768529,-4.798708,9.108271,-1.645118,-5.378163,-8.414620,-8.661121,-9.680729,-7.942868]],[[7.315227,-5.468112,-6.132581,-9.675954,-6.537825,3.978472,-6.410438,-8.451418,9.446095,8.325006,6.102626,9.870992,1.485619],[0.619613,7.437944,5.160617,0.043909,-9.416580,-2.452490,-5.992709,-5.158317,-0.317571,-8.060474,8.160456,-9.214669,9.109351],[-2.613592,4.747366,6.232648,-5.803274,-3.695659,8.265827,8.066807,9.623436,-0.564655,6.407728,8.469005,4.826722,-8.497009]],[[6.885521,8.289676,-4.852467,9.939605,-4.719485,7.742936,-6.016429,-2.637998,1.778442,6.537916,7.176873,-6.821584,-3.379973],[-9.111522,7.880044,4.118379,-8.800006,-3.448768,-3.948825,-0.644352,-0.023504,5.505885,-6.466945,-3.751710,-3.839055,-5.132896],[3.107535,-8.363765,5.452524,1.459389,3.627998,8.937305,4.648186,1.953458,-8.993951,-9.506128,6.248276,3.716161,2.319826]],[[4.072096,3.927907,4.791279,-7.742782,7.419945,9.653694,-7.083353,7.843493,-2.207769,2.584059,-2.920001,1.475377,-0.317666],[5.477140,-1.898145,9.210919,-5.280213,-6.059114,8.353627,4.698951,-5.643532,6.394625,9.021265,-6.688970,-8.637993,4.789572],[7.154656,9.875089,4.935239,1.710623,-0.539875,0.390141,-0.810659,-4.377225,-4.598604,-9.145070,-9.200341,-3.503614,-8.381812]],[[2.748374,-6.054315,0.717254,-1.437134,-5.499141,7.074373,5.892431,-4.425190,-6.938193,-1.933854,5.207484,-5.001514,3.190911],[7.827670,7.815805,7.374063,-2.759759,7.977047,0.201057,7.390074,-7.472713,-8.409324,-6.709873,-1.114283,2.450018,7.987017],[-9.097660,-9.323955,6.497688,4.192242,4.400164,0.677306,-2.501743,6.901011,-6.497901,6.366961,-7.085183,0.250044,1.709122]],[[6.171910,-1.214045,6.173954,9.954173,0.731912,4.578942,9.319098,8.790975,9.090286,6.448347,6.149818,0.535771,-3.339304],[-6.152559,-0.254667,-4.515934,-2.611222,-5.229916,7.546276,1.250852,-3.657353,7.453894,0.767896,3.844277,-0.473982,-9.781858],[-0.303690,5.784291,3.510825,-7.239759,2.551060,4.103832,-8.116661,2.825311,3.947295,-1.524796,5.047584,1.380546,-9.872839]],[[1.658996,-4.134104,-7.446907,9.567968,1.187366,-3.081908,-5.745246,-7.373856,5.708814,-5.197256,-5.701794,-5.354735,0.391315],[-9.151643,-2.355041,4.345689,-3.903394,2.094585,7.378931,-6.573925,6.253391,-9.223097,-2.719697,-6.454110,7.574338,-0.845647],[-9.084118,-2.904901,-4.985171,7.296498,2.589518,0.568449,-5.383492,2.832316,2.433493,-3.594984,-7.931387,9.230847,-3.331817]],[[-8.620535,-0.351536,6.351234,3.669280,-3.138799,9.181792,6.123103,0.197849,-6.234176,7.559854,9.566799,2.207421,-2.301529],[-4.611832,-3.611221,7.684513,1.021222,0.020504,-6.213077,-1.525893,-3.176557,-2.911707,5.086731,-1.964328,1.131522,1.037443],[7.771002,4.003609,-8.666877,2.746232,-3.928437,8.480644,-5.030444,-2.315303,-2.559106,3.522090,-0.153357,-9.943778,2.525697]],[[3.845513,-3.136387,5.622009,8.051236,6.472505,4.022335,-9.018038,0.996389,8.525245,-3.944333,8.755214,-7.627155,-9.661587],[-5.935233,-1.549024,2.833371,5.804672,-4.018310,9.623899,0.498171,6.666899,9.013387,-5.779109,-7.243623,-9.216472,4.658426],[7.471532,3.636746,9.270151,-9.160663,6.929206,2.195927,0.990179,-0.379372,-0.034325,-2.233397,-1.628592,9.860408,-9.826545]]], dtype = "float32")#candidate|4236|(11, 3, 13)|const|float32
uop_4237 = relay.cosh(const_4236.astype('float32')) # shape=(11, 3, 13)
func_3436_call = mod.get_global_var('func_3436')
func_3437_call = mutated_mod.get_global_var('func_3437')
call_4243 = relay.TupleGetItem(func_3436_call(), 1)
call_4244 = relay.TupleGetItem(func_3437_call(), 1)
func_2324_call = mod.get_global_var('func_2324')
func_2326_call = mutated_mod.get_global_var('func_2326')
const_4246 = relay.const([5.227332,0.747653,-2.348292,3.869924,-3.388547,6.261576,-9.862209,0.302338,3.790590,-6.627808,-4.440924,9.247462,6.610566,9.954675,-9.710603,-9.661982,3.588278,-9.890307,6.770680,-0.750654,-8.568640,-7.810498,-0.807500,-6.195284,-4.880706,9.595796,-4.953776,5.918992,-1.605183,-5.702597,6.853626,-7.732993,1.660637,-6.390310,7.760529,-1.100089,-9.030676,-4.324539,6.623336,5.174232,9.452885,-4.558672,3.356614,-1.502487,-0.835609,7.494882,6.520517,-4.542728,-2.445779,-9.780336,-1.638146,1.115024,1.417161,6.184539,-2.050043,4.975281,-1.912862,-1.669166,7.748326,0.331711,1.947326,5.250985,1.060636,7.013672,9.199696,8.784293,6.084088,-2.306958,-6.998539,8.000565,-4.458554,8.739392,-5.613725,9.423186,-1.274013,-8.810096,4.133578,-2.092860,9.130688,-0.711207,5.352115,-9.419850,-9.238911,-8.170353,1.133054,7.516139,-3.692195,-0.292458,-0.920424,-6.896539,-9.537342,4.759247,-5.022084,-9.244754,2.081544,-7.892924,-6.166543,5.591861,-1.152087,-2.050165,6.345374,3.295111,-7.930304,1.941522,9.562345,2.678173,-5.167425,4.768777,-9.244002,-9.982174,-6.965680,7.355858,-3.069773,0.092341,-0.820306,-4.420182,-0.643773,3.862986,1.086165,4.593018,-4.544845,-2.666713,8.876916,5.105584,-8.608549,-0.749528,5.327819,4.910282,-5.703186,-7.841423,-2.261392,7.456671,-4.276840,2.468437,0.990629,5.045749,6.840915,-9.817009,1.147143,0.679119,2.904563,0.374997,8.335041,-8.902015,9.030930,-5.631412,1.189521,-1.935697,-7.837390,6.183831,1.570036,1.014765,2.050758,8.493879,6.215470,-5.638993,-4.262313,6.149894,-9.004699,-4.571829,-7.196762,-2.933220,-4.262311,-4.999657,-9.062319,-9.812916,-7.434814,0.579212,9.704241,-7.255209,3.685757,4.112323,-5.858703,7.806623,9.276393,5.346308,-3.119579,2.884231,-2.740774,1.608154,-9.505487,-1.416955,7.422706,-7.837251,2.348708,7.711159,7.035126,-3.138604,-7.662473,-9.502814,6.422752,5.368296,7.229489,-6.445489,-3.572393,0.466247,9.358571,5.464133,8.767178,6.066903,2.018830,9.931354,-2.921054,-1.477164,5.321910,-2.469205,-9.264702,-9.240959,-2.325021,-8.339037,-4.314743,0.577475,5.965814,-4.765523,-5.635975,2.813546,-4.532192,-7.823935,8.888653,2.204998,-6.043910,7.588748,-3.498414,-2.308624,3.149977,3.169411,-2.983312,3.547140,-7.051239,-3.660670,-4.308001,-6.374395,-8.065372,8.518891,9.067599,-6.969019,-6.149104,9.836671,8.931409,9.344553,-7.762258,-0.449020,-6.603928,-2.860155,1.638135,0.304221,5.972204,1.640515,4.678074,0.884029,2.163930,-3.103093,2.205962,-5.924900,0.236088,3.259102,8.005542,0.249338,-8.066458,-7.034221,-3.926655,8.968733,2.254961,-1.925081,7.358947,8.818324,1.500363,-1.252546,1.871679,-1.575179,-8.649975,-6.629547,3.515804,1.000965,-0.412010,-4.488178,-9.396833,-5.744747,-3.306589,-1.318475,-3.889141,-6.501724,7.387164,-9.487488,-0.086540,4.900861,4.930179,-0.143344,4.120852,-2.458565,8.965760,1.195361,-4.590986,3.705385,-6.057721,-6.029031,9.283310,-0.253180,1.025288,-4.997758,1.813786,-1.500596,8.710277,-2.443954,4.249423,-5.192149,8.833456,-6.933319,1.855468,-5.365318,7.220686,-7.406299,8.814071,0.989267,-8.335871,-2.727963,8.365652,-7.660973,9.892132,-2.466015,0.304105,3.750283,-1.822048,-9.640004,8.597646,8.059284,0.179185,-8.262118,-8.466313,6.664754,1.623854,4.830103,-6.958573,6.390791,-5.264127,-0.737779,6.395265,-9.450817,4.313067,4.934739,3.679958,6.370446,4.359751,3.510532,3.475364,-8.583586,3.132362,-2.597066,2.837041,5.716146,1.179558,4.903864,-5.505890,-6.937651,-5.881206,-3.342335,-5.436296,-0.422989,8.158209,0.125451,-9.010414,4.853340,3.129235,7.192085,-6.654905,-3.918194,8.217228,-7.814561,2.330022,9.647368,-5.320800,0.175295,-7.810738,-2.757485,-7.800201,-1.874323,3.284557,-7.307356,8.830053,0.341147,-8.543005,1.568969,1.691262,9.193280,-4.251803,-0.647419,8.731121,7.763382,0.905321,9.360641,-8.705564,-9.326845,-8.982335,-7.028609,2.675205,7.768199,-4.517491,9.528866,-7.396649,-5.875011,5.063194,3.147884,8.286238,-4.290965,7.608656,-6.860219,-7.937817,5.482520,7.412063,-4.724276,-2.913858,-8.575219,8.559602,-0.267564,9.676257,-3.192295,-7.660009,3.720179,3.360352,-4.452113,6.365543,-9.033084,-9.476639,-8.763811,8.669062,-5.207769,-8.616367,-9.758735,-5.490115,0.763479,-8.398894,-6.615722,-7.364120,-0.742925,-1.841095,-6.422366,9.897258,0.041600,-0.834459,4.802398,-8.555041,4.086111,-7.854813,-1.824352,4.468301,-4.221210,-2.887444,-0.813623,-5.064793,-2.305080,9.518128,8.130031,9.393824,-6.048526,-5.490701,6.120552,8.227238,-1.683628,3.977261,-7.274294,-6.897542,-9.460241,-5.725734,9.700291,9.360206,1.832218,-4.111353,6.851466,4.494278,-6.223744,9.701387,-6.986797,-9.920589,-5.216643,-6.949772,-1.093512,-0.408270,4.662285,2.051412,7.854514,-6.772547,-1.782923,8.133636,-2.301423,6.842804,0.707040,-3.517061,-2.966673,-9.955165,-6.265752,1.784554,6.423585,5.351742,-3.133888,-8.328973,1.660743,-5.377217,4.511578,9.490705,-1.045044,-2.598060,9.379189,-6.790476,-2.009363,0.419463,5.380873,4.932758,-3.113663,0.932847,-8.852090,-8.027135,-8.602633,5.816702,3.137296,7.709719,8.254009,9.061078,-4.298629,-1.552352,-8.920222,-0.166240,3.728461,-3.420761,-1.883294,-8.655254,3.180546,0.522484,-5.562655,-1.009835,1.330684,4.761203,9.374587,-1.951450,-6.143802,-4.360920,-7.999348,-9.525078,5.251472,8.228943,-4.324602,-2.268166,-5.520200,8.986663,-4.744843,-7.806315,8.211246,-3.245167,-9.117476,1.900301,-9.407834,8.953579,-1.334690,-4.690470,7.101507,8.535919,0.015901,2.948706,1.880595,-0.313827,-4.210726,-0.330074,4.733914,1.325999,5.782419,-3.719535,-7.523299,-8.208828,-7.948880,-0.009018,-9.562795,2.901436,5.631200,0.292006,-5.554653,-5.681860,3.004253,-6.469042,-8.176625,-2.711937,-4.515493,6.138599,7.680006,5.521912,-3.944952,5.321445,-5.344705,-8.081629,2.005789,-6.728176,-6.365510,7.523938,5.726334,-2.337968,9.323005,5.863515,7.372209,-0.855857,-8.764580,-9.908264,-1.724944,7.537102,8.457182,-4.528573,-0.098385,-5.436730,-9.993287,-3.915361,3.292229,2.393963,3.979401,1.471149,9.970894,7.734967,3.851966,-6.289551,2.061955,-4.691026,7.952457,-1.017099,-6.408824,-0.073243,-2.771795,-7.715278,0.820409,-3.888112,8.280031,-7.641389,1.724057,-6.680397,3.616243,-2.792788,5.935823,2.338588,-0.922157,-1.805314,-5.486550,6.009634,8.464563,7.272393,5.130836,9.366072,1.222091,4.818545,-5.897584,0.141120,-4.233020,-4.157628,3.855186,-7.520492,7.496207,-6.219547,-4.080948,-3.504773,7.673556,-2.855823,3.866926,1.060643,1.092780,-5.225070,6.709606,-7.092817,1.100401,4.915831,-6.312578,-6.395463,-1.921256,-6.675602,-1.434227,-3.336692,-5.856170,-3.734595,-3.524966,-1.586266,-3.330314,6.116798,-0.125414,6.118119,6.449068,-4.717223,4.641105,1.743095,5.799416,-4.872004,0.778793,-3.343115,7.797008,1.669483,-0.622104,-8.566655,-3.491861,-0.771487,5.701854,7.377040,-7.264351,-0.942251,-2.385707,7.340676,0.708050,-7.023874,-0.648506,-2.614215,1.383383,-3.061000,2.732058,5.503348,-9.240746,5.893222,9.135895,-1.259998,-4.332454,6.983171,4.338426,2.286444,-3.383087,1.908897,-4.352363,9.369715,7.656420,5.376805,-9.705650,0.397126,4.620987,-1.760683,5.411600,-3.665574,0.929824,-9.782169,5.311277,-5.947132,0.790717,-2.355601,0.178206,-4.922951,0.944315,-8.769888,-3.454901,3.926052,-9.282019,-4.918816,-2.085301,2.511150,2.275700,-9.642051,2.879413,-5.662758,-9.822943,-9.287731,-2.897609,2.358888,7.625748,5.738524,6.828479,5.722230,-4.481320,4.385334,-4.133486,1.052837,-8.721390,-3.800773,-0.738812,3.121428,-8.928830,-8.475160,-8.063461,-6.311100,6.980419,0.448172,-3.984767,-9.277484,-1.569159,-3.943835,4.133336,-4.503404,9.873708,5.655659,-6.884917,3.888727,1.414244,9.389999,0.810377,7.679505,-8.168628,4.127584,9.708557,5.039399,0.241944,-8.412280,7.240775,-7.871886,-5.725896,-5.263502,-1.620578,1.355773,-7.124174,5.355746,-4.367510,-9.780520,5.367068,-3.071508,-0.224937,8.727826,4.724372,-8.863436,-6.392493,9.366903,-4.099279,5.302806,5.264079,-9.188559,-2.576806,9.254486,-7.439347,8.617844,3.907077,-8.776565,8.913061,2.110156,-9.937435,-5.231747,1.621992,0.423537,0.823586,-1.670478,9.082161,-2.091964,5.668004,-2.734901,-4.723977,4.413291,4.441838,1.748642,7.523609,3.639092,-9.191115,8.244758,-2.474189,7.816479,3.870023,-2.146495,8.046901,-4.212679,4.289204,-2.696455,-1.284910,3.178208,-6.730434,3.152812,-3.572409,8.404561,-7.282652,-1.068360,6.591474,-0.341320,1.514973,8.524229,-7.105318,2.613126,-3.977765,8.194777,-9.372630,0.465739,8.073974,-5.243881,0.328756,-9.358931,-5.206717,-5.512332,-8.114196,4.578134,-5.401450,-5.198979,-1.921116,-3.090338,-4.459401,-5.853931,-3.646494,5.820532,-2.195728,5.526581,8.984734,8.036671,-7.850241,6.966962,-7.109561,0.904592,9.307242,7.468023,7.733635,-0.467394,3.574131,-0.339786,-0.082657,6.518878,-2.354212,1.999593,-4.678992,7.465651,-4.019490,-0.344148,5.668663,3.536420,7.468253,6.860147,-6.052919,-8.385106,-9.108662,-3.235322,-4.598147,6.653536,-7.251898,-9.472783,7.118274,-1.000684,-9.604456,-6.983349,-0.232401,-7.041906,9.850838,-9.296798,-1.351734,9.262682,-7.281870,6.360571,-7.054297,0.238353,6.060226,2.981322,3.606359,3.709499,-1.076523,-5.400740,1.515309,3.175461,-2.296850,7.668780,-9.402482,9.534887,-8.099379,-9.874951,8.236756,7.373283,3.302537,0.519542,-7.195467,7.768387,-7.136945,8.778829,-6.127116,-9.850889,0.948788,4.302844,9.860162,-9.310846,-8.854353,-0.481598,-1.875463,-7.841329,-0.784956,-5.705750,-2.010632,-1.924940,1.654516,6.696170,-3.074372,-8.876047,1.004576,7.148955,-9.155522,-3.551146,-1.492038,-4.638687,-1.222669,1.627031,-1.172021,-2.593419,1.446370,-9.419858,-6.938223,-3.954575,4.774264,-0.266574,3.834840,0.333399,5.631063,-0.048766,-3.703529,-9.464400,8.128073,-4.997036,-5.335590,9.786723,4.147233,-0.437154,4.587605,-8.032584,-7.909231,6.228707,-8.113194,6.479738,-8.790709,-6.315868,4.792893,9.833595,-8.081434,-2.307357,-4.259983,-6.767816,9.231453,-1.157807,5.422473,-2.353061,4.048712,6.092102,-2.585635,-2.447673,-0.663490,-7.306507,8.367974,9.762297,2.469604,-0.682340,4.461931,7.914323,-5.287986,5.428240,-3.622767,2.941567,1.344634,5.862386,8.475757,-7.827416,-8.608750,4.278896,-0.220564,2.560748,7.669814,-3.054032,-3.996896,6.868105,2.289093,8.020918,-9.063699,7.557882,6.273041,-1.973038,-1.075902,3.841258,4.199028,9.059210,3.337980,4.617349,-4.382435,3.003259], dtype = "float32")#candidate|4246|(1053,)|const|float32
call_4245 = relay.TupleGetItem(func_2324_call(relay.reshape(const_4246.astype('float32'), [9, 9, 13])), 1)
call_4247 = relay.TupleGetItem(func_2326_call(relay.reshape(const_4246.astype('float32'), [9, 9, 13])), 1)
func_3675_call = mod.get_global_var('func_3675')
func_3676_call = mutated_mod.get_global_var('func_3676')
call_4255 = relay.TupleGetItem(func_3675_call(), 0)
call_4256 = relay.TupleGetItem(func_3676_call(), 0)
bop_4257 = relay.left_shift(uop_4237.astype('uint64'), relay.reshape(const_4236.astype('uint64'), relay.shape_of(uop_4237))) # shape=(11, 3, 13)
func_1383_call = mod.get_global_var('func_1383')
func_1384_call = mutated_mod.get_global_var('func_1384')
call_4260 = relay.TupleGetItem(func_1383_call(), 1)
call_4261 = relay.TupleGetItem(func_1384_call(), 1)
output = relay.Tuple([call_4243,call_4245,const_4246,call_4255,bop_4257,call_4260,])
output2 = relay.Tuple([call_4244,call_4247,const_4246,call_4256,bop_4257,call_4261,])
func_4265 = relay.Function([], output)
mod['func_4265'] = func_4265
mod = relay.transform.InferType()(mod)
mutated_mod['func_4265'] = func_4265
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4265_call = mutated_mod.get_global_var('func_4265')
call_4266 = func_4265_call()
output = call_4266
func_4267 = relay.Function([], output)
mutated_mod['func_4267'] = func_4267
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4290 = relay.const(-7.130365, dtype = "float32")#candidate|4290|()|const|float32
var_4291 = relay.var("var_4291", dtype = "float32", shape = (8, 4, 14))#candidate|4291|(8, 4, 14)|var|float32
bop_4292 = relay.power(const_4290.astype('float32'), var_4291.astype('float32')) # shape=(8, 4, 14)
func_3911_call = mod.get_global_var('func_3911')
func_3913_call = mutated_mod.get_global_var('func_3913')
call_4295 = relay.TupleGetItem(func_3911_call(), 0)
call_4296 = relay.TupleGetItem(func_3913_call(), 0)
func_1537_call = mod.get_global_var('func_1537')
func_1540_call = mutated_mod.get_global_var('func_1540')
var_4303 = relay.var("var_4303", dtype = "float32", shape = (1053,))#candidate|4303|(1053,)|var|float32
call_4302 = relay.TupleGetItem(func_1537_call(relay.reshape(var_4303.astype('float32'), [9, 9, 13])), 0)
call_4304 = relay.TupleGetItem(func_1540_call(relay.reshape(var_4303.astype('float32'), [9, 9, 13])), 0)
output = relay.Tuple([bop_4292,call_4295,call_4302,var_4303,])
output2 = relay.Tuple([bop_4292,call_4296,call_4304,var_4303,])
func_4311 = relay.Function([var_4291,var_4303,], output)
mod['func_4311'] = func_4311
mod = relay.transform.InferType()(mod)
mutated_mod['func_4311'] = func_4311
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4311_call = mutated_mod.get_global_var('func_4311')
var_4313 = relay.var("var_4313", dtype = "float32", shape = (8, 4, 14))#candidate|4313|(8, 4, 14)|var|float32
var_4314 = relay.var("var_4314", dtype = "float32", shape = (1053,))#candidate|4314|(1053,)|var|float32
call_4312 = func_4311_call(var_4313,var_4314,)
output = call_4312
func_4315 = relay.Function([var_4313,var_4314,], output)
mutated_mod['func_4315'] = func_4315
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4369 = relay.var("var_4369", dtype = "float64", shape = ())#candidate|4369|()|var|float64
const_4370 = relay.const([[[-6.817558,-8.302896,-7.181588,-5.475529,9.777475],[8.328430,-7.534263,4.588174,-1.907050,5.115415],[0.148897,-9.123116,8.025305,5.043805,5.694021],[-5.472678,3.025863,5.746797,-7.513321,-4.778525],[5.641791,-8.374373,8.696215,6.260647,-5.352777]],[[-9.698417,-7.302640,1.291903,-8.538268,7.559168],[8.829128,8.654942,-3.673986,-6.202385,-4.372625],[-0.089475,-1.824235,9.312987,2.151083,7.147285],[8.296776,3.555250,-5.739129,7.348941,4.267006],[0.493561,-0.715417,1.903822,1.055957,6.659062]],[[-7.842127,-9.845327,-5.568132,1.044945,-6.055540],[0.278265,-0.907246,-5.445570,5.470911,4.167760],[-8.623395,7.821048,1.511324,1.217537,-9.907577],[-3.850653,-0.140321,0.548204,7.492654,-5.448082],[-1.226871,3.457060,4.714777,4.601257,-5.919472]],[[3.588364,6.188861,3.064601,-9.298399,-1.847451],[-1.131793,1.672263,3.805450,6.998628,7.411835],[-5.187837,-8.477697,-6.977711,5.537858,-3.045347],[-8.813784,-1.980064,0.309234,-2.032857,-5.404799],[-7.117203,-1.343824,-1.652739,5.945005,-2.025771]],[[8.642186,-3.012319,-6.406273,7.094428,-4.199821],[1.908799,-2.526772,9.878533,-9.270127,4.775203],[-5.017189,9.528402,4.245282,-9.111833,9.288829],[-6.189223,3.889275,-8.823041,6.103659,-4.915016],[-2.803095,8.035828,7.282306,-2.930790,-7.693768]],[[6.879818,8.935399,2.896391,-5.686842,4.238051],[-8.559048,-3.990449,-9.872126,-5.545359,3.301691],[-5.186699,-0.876422,-9.811060,-4.177077,2.689324],[-0.745804,3.155385,7.595528,-2.335629,-9.432151],[-3.617104,7.093801,-2.721454,9.226282,-1.461671]],[[6.445175,-3.988355,-0.139906,-8.734751,9.665252],[0.577431,-8.672966,-8.433172,-3.560968,4.742603],[-9.212387,3.365054,-8.701951,-2.279461,-4.402052],[-1.815700,1.652880,-9.920428,7.081446,-8.169012],[-2.103009,-0.079470,-1.978540,6.203780,-5.395885]],[[8.622172,-4.339054,-1.884912,-7.756685,-4.234518],[7.180929,2.482436,-9.245898,-0.711632,-7.371478],[-7.020197,0.122621,9.514124,1.162673,-8.210218],[9.987657,3.504817,-0.209431,-0.123639,-1.307323],[-1.987151,-4.425261,-2.222652,1.569709,-5.252060]],[[5.278870,-1.013497,-7.381711,-3.891208,-6.152683],[7.866818,-8.846569,8.472312,-7.108574,7.401540],[4.045968,7.745618,2.834549,-1.085732,-8.361107],[-5.959197,1.643608,-7.029305,-2.282894,-3.027355],[4.722349,-5.579798,-6.170246,0.305995,-3.946707]],[[3.215411,-3.741737,6.506056,-0.679483,-8.227121],[-4.239435,-8.878301,6.900099,6.525643,6.840530],[0.688331,6.487115,-9.881381,1.817917,7.384251],[-4.699703,5.198496,4.272988,5.085738,-7.049311],[-4.936603,-8.484761,5.875358,-3.957585,-5.481204]],[[-8.415320,-9.360387,8.004004,6.989496,-3.401059],[-2.107539,2.994545,6.965308,-7.296499,-2.931421],[-5.673201,-8.978474,3.203805,8.246702,-0.521156],[2.187030,9.868358,4.924542,-3.378724,0.152039],[0.360432,9.418150,-1.593473,8.585629,1.359931]],[[4.051394,-1.622764,6.923608,3.955937,5.448533],[-0.389890,-0.648348,7.629277,-8.197794,-7.321191],[-4.344763,-8.538857,-7.483898,3.620012,9.168168],[1.055155,-7.632995,-4.996863,3.024509,-0.670535],[-1.769055,6.645375,-7.969430,-9.588939,-3.259370]],[[9.764692,-4.951259,4.306955,-2.862079,-3.975202],[4.811171,-5.872839,0.886784,1.515258,0.743943],[-7.928664,-7.553979,-7.847879,-3.060460,-0.966801],[-0.554905,2.131045,1.946975,1.311310,4.401678],[7.883026,-8.441457,9.460457,5.930952,-8.529158]],[[-2.818129,-6.166325,4.396192,-2.591524,6.936229],[-4.449316,-2.606697,-6.919347,-7.033927,7.256029],[3.905449,6.374761,-2.249674,6.463722,3.587291],[-3.222567,-6.448554,8.432058,-7.156624,3.973734],[-8.701197,1.275568,-9.573104,-3.313503,5.475967]]], dtype = "float64")#candidate|4370|(14, 5, 5)|const|float64
bop_4371 = relay.floor_mod(var_4369.astype('float64'), const_4370.astype('float64')) # shape=(14, 5, 5)
output = bop_4371
output2 = bop_4371
func_4385 = relay.Function([var_4369,], output)
mod['func_4385'] = func_4385
mod = relay.transform.InferType()(mod)
var_4386 = relay.var("var_4386", dtype = "float64", shape = ())#candidate|4386|()|var|float64
output = func_4385(var_4386)
func_4387 = relay.Function([var_4386], output)
mutated_mod['func_4387'] = func_4387
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1178_call = mod.get_global_var('func_1178')
func_1180_call = mutated_mod.get_global_var('func_1180')
call_4389 = func_1178_call()
call_4390 = func_1178_call()
output = call_4389
output2 = call_4390
func_4429 = relay.Function([], output)
mod['func_4429'] = func_4429
mod = relay.transform.InferType()(mod)
output = func_4429()
func_4430 = relay.Function([], output)
mutated_mod['func_4430'] = func_4430
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2001_call = mod.get_global_var('func_2001')
func_2002_call = mutated_mod.get_global_var('func_2002')
call_4472 = relay.TupleGetItem(func_2001_call(), 0)
call_4473 = relay.TupleGetItem(func_2002_call(), 0)
output = call_4472
output2 = call_4473
func_4474 = relay.Function([], output)
mod['func_4474'] = func_4474
mod = relay.transform.InferType()(mod)
output = func_4474()
func_4475 = relay.Function([], output)
mutated_mod['func_4475'] = func_4475
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4523 = relay.var("var_4523", dtype = "float64", shape = ())#candidate|4523|()|var|float64
var_4524 = relay.var("var_4524", dtype = "float64", shape = (1, 11, 12))#candidate|4524|(1, 11, 12)|var|float64
bop_4525 = relay.power(var_4523.astype('float64'), var_4524.astype('float64')) # shape=(1, 11, 12)
output = relay.Tuple([bop_4525,])
output2 = relay.Tuple([bop_4525,])
func_4536 = relay.Function([var_4523,var_4524,], output)
mod['func_4536'] = func_4536
mod = relay.transform.InferType()(mod)
var_4537 = relay.var("var_4537", dtype = "float64", shape = ())#candidate|4537|()|var|float64
var_4538 = relay.var("var_4538", dtype = "float64", shape = (1, 11, 12))#candidate|4538|(1, 11, 12)|var|float64
output = func_4536(var_4537,var_4538,)
func_4539 = relay.Function([var_4537,var_4538,], output)
mutated_mod['func_4539'] = func_4539
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3874_call = mod.get_global_var('func_3874')
func_3875_call = mutated_mod.get_global_var('func_3875')
call_4585 = relay.TupleGetItem(func_3874_call(), 0)
call_4586 = relay.TupleGetItem(func_3875_call(), 0)
func_1064_call = mod.get_global_var('func_1064')
func_1066_call = mutated_mod.get_global_var('func_1066')
call_4616 = func_1064_call()
call_4617 = func_1064_call()
output = relay.Tuple([call_4585,call_4616,])
output2 = relay.Tuple([call_4586,call_4617,])
func_4627 = relay.Function([], output)
mod['func_4627'] = func_4627
mod = relay.transform.InferType()(mod)
mutated_mod['func_4627'] = func_4627
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4627_call = mutated_mod.get_global_var('func_4627')
call_4628 = func_4627_call()
output = call_4628
func_4629 = relay.Function([], output)
mutated_mod['func_4629'] = func_4629
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4474_call = mod.get_global_var('func_4474')
func_4475_call = mutated_mod.get_global_var('func_4475')
call_4650 = func_4474_call()
call_4651 = func_4474_call()
output = relay.Tuple([call_4650,])
output2 = relay.Tuple([call_4651,])
func_4675 = relay.Function([], output)
mod['func_4675'] = func_4675
mod = relay.transform.InferType()(mod)
mutated_mod['func_4675'] = func_4675
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4675_call = mutated_mod.get_global_var('func_4675')
call_4676 = func_4675_call()
output = call_4676
func_4677 = relay.Function([], output)
mutated_mod['func_4677'] = func_4677
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4265_call = mod.get_global_var('func_4265')
func_4267_call = mutated_mod.get_global_var('func_4267')
call_4697 = relay.TupleGetItem(func_4265_call(), 2)
call_4698 = relay.TupleGetItem(func_4267_call(), 2)
output = call_4697
output2 = call_4698
func_4706 = relay.Function([], output)
mod['func_4706'] = func_4706
mod = relay.transform.InferType()(mod)
mutated_mod['func_4706'] = func_4706
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4706_call = mutated_mod.get_global_var('func_4706')
call_4707 = func_4706_call()
output = call_4707
func_4708 = relay.Function([], output)
mutated_mod['func_4708'] = func_4708
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3368_call = mod.get_global_var('func_3368')
func_3370_call = mutated_mod.get_global_var('func_3370')
call_4752 = relay.TupleGetItem(func_3368_call(), 1)
call_4753 = relay.TupleGetItem(func_3370_call(), 1)
func_2572_call = mod.get_global_var('func_2572')
func_2574_call = mutated_mod.get_global_var('func_2574')
call_4768 = func_2572_call()
call_4769 = func_2572_call()
func_1787_call = mod.get_global_var('func_1787')
func_1789_call = mutated_mod.get_global_var('func_1789')
call_4779 = relay.TupleGetItem(func_1787_call(relay.reshape(call_4768.astype('float64'), [9, 9, 13])), 0)
call_4780 = relay.TupleGetItem(func_1789_call(relay.reshape(call_4768.astype('float64'), [9, 9, 13])), 0)
func_1146_call = mod.get_global_var('func_1146')
func_1149_call = mutated_mod.get_global_var('func_1149')
call_4784 = relay.TupleGetItem(func_1146_call(relay.reshape(call_4768.astype('float32'), [9, 9, 13])), 2)
call_4785 = relay.TupleGetItem(func_1149_call(relay.reshape(call_4768.astype('float32'), [9, 9, 13])), 2)
output = relay.Tuple([call_4752,call_4768,call_4779,call_4784,])
output2 = relay.Tuple([call_4753,call_4769,call_4780,call_4785,])
func_4790 = relay.Function([], output)
mod['func_4790'] = func_4790
mod = relay.transform.InferType()(mod)
output = func_4790()
func_4791 = relay.Function([], output)
mutated_mod['func_4791'] = func_4791
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4813 = relay.var("var_4813", dtype = "int8", shape = (15, 2, 10))#candidate|4813|(15, 2, 10)|var|int8
const_4814 = relay.const([[[-10,-10,-9,8,-2,4,7,10,-8,1],[-3,10,-2,-7,-5,-2,4,-7,-10,-6]],[[-9,10,6,10,-6,1,-1,-1,-9,1],[1,-10,-7,9,6,-10,8,3,-10,9]],[[3,5,-2,6,3,9,3,3,8,7],[-7,-9,5,-8,-6,-10,8,-2,2,-4]],[[-5,2,-2,-8,-7,6,-10,-7,-8,1],[-4,2,8,4,4,-6,-1,-7,-1,7]],[[9,-2,-10,-7,5,-4,-1,-1,-10,1],[-3,5,3,-10,8,-4,3,-10,-4,3]],[[7,8,-4,8,-4,-10,-6,-2,6,3],[1,2,3,7,9,7,-7,-5,-4,5]],[[-4,6,9,-6,1,-10,9,6,-2,-1],[5,8,-5,-3,5,-8,6,-8,-1,1]],[[-8,-2,-10,10,3,4,1,10,-4,4],[4,10,-5,4,-5,-8,3,-9,-10,7]],[[-10,1,-5,-7,5,-2,-5,-8,1,8],[4,-8,-6,2,-5,9,-9,7,1,-5]],[[-7,-7,9,3,-5,7,-7,-6,3,-10],[6,6,-10,-1,8,9,-5,8,-10,-6]],[[-3,4,-10,-4,-10,-3,-4,4,-5,4],[3,1,-8,3,-1,2,-4,4,1,-8]],[[2,9,-2,9,10,-3,5,-10,-2,-2],[2,6,2,-9,-10,6,-8,-8,-8,10]],[[-10,-2,4,9,-6,8,7,-3,4,4],[1,-7,-6,1,-4,3,-1,-1,6,-2]],[[3,10,4,10,9,3,5,1,5,-9],[-3,2,-7,3,-3,6,5,-5,-3,-8]],[[-9,2,-10,-9,-7,3,1,7,8,-1],[-5,4,-7,8,4,-2,-8,10,9,5]]], dtype = "int8")#candidate|4814|(15, 2, 10)|const|int8
bop_4815 = relay.bitwise_xor(var_4813.astype('int8'), relay.reshape(const_4814.astype('int8'), relay.shape_of(var_4813))) # shape=(15, 2, 10)
bop_4825 = relay.multiply(const_4814.astype('uint16'), relay.reshape(var_4813.astype('uint16'), relay.shape_of(const_4814))) # shape=(15, 2, 10)
uop_4834 = relay.cosh(const_4814.astype('float32')) # shape=(15, 2, 10)
output = relay.Tuple([bop_4815,bop_4825,uop_4834,])
output2 = relay.Tuple([bop_4815,bop_4825,uop_4834,])
func_4836 = relay.Function([var_4813,], output)
mod['func_4836'] = func_4836
mod = relay.transform.InferType()(mod)
var_4837 = relay.var("var_4837", dtype = "int8", shape = (15, 2, 10))#candidate|4837|(15, 2, 10)|var|int8
output = func_4836(var_4837)
func_4838 = relay.Function([var_4837], output)
mutated_mod['func_4838'] = func_4838
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4857 = relay.var("var_4857", dtype = "float64", shape = (6, 12, 11))#candidate|4857|(6, 12, 11)|var|float64
uop_4858 = relay.sin(var_4857.astype('float64')) # shape=(6, 12, 11)
func_2156_call = mod.get_global_var('func_2156')
func_2158_call = mutated_mod.get_global_var('func_2158')
call_4871 = func_2156_call()
call_4872 = func_2156_call()
output = relay.Tuple([uop_4858,call_4871,])
output2 = relay.Tuple([uop_4858,call_4872,])
func_4877 = relay.Function([var_4857,], output)
mod['func_4877'] = func_4877
mod = relay.transform.InferType()(mod)
mutated_mod['func_4877'] = func_4877
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4878 = relay.var("var_4878", dtype = "float64", shape = (6, 12, 11))#candidate|4878|(6, 12, 11)|var|float64
func_4877_call = mutated_mod.get_global_var('func_4877')
call_4879 = func_4877_call(var_4878)
output = call_4879
func_4880 = relay.Function([var_4878], output)
mutated_mod['func_4880'] = func_4880
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4946 = relay.var("var_4946", dtype = "uint64", shape = ())#candidate|4946|()|var|uint64
var_4947 = relay.var("var_4947", dtype = "uint64", shape = (7, 15, 4))#candidate|4947|(7, 15, 4)|var|uint64
bop_4948 = relay.maximum(var_4946.astype('uint64'), var_4947.astype('uint64')) # shape=(7, 15, 4)
output = bop_4948
output2 = bop_4948
func_4982 = relay.Function([var_4946,var_4947,], output)
mod['func_4982'] = func_4982
mod = relay.transform.InferType()(mod)
mutated_mod['func_4982'] = func_4982
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4982_call = mutated_mod.get_global_var('func_4982')
var_4984 = relay.var("var_4984", dtype = "uint64", shape = ())#candidate|4984|()|var|uint64
var_4985 = relay.var("var_4985", dtype = "uint64", shape = (7, 15, 4))#candidate|4985|(7, 15, 4)|var|uint64
call_4983 = func_4982_call(var_4984,var_4985,)
output = call_4983
func_4986 = relay.Function([var_4984,var_4985,], output)
mutated_mod['func_4986'] = func_4986
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3543_call = mod.get_global_var('func_3543')
func_3545_call = mutated_mod.get_global_var('func_3545')
call_4988 = func_3543_call()
call_4989 = func_3543_call()
func_4982_call = mod.get_global_var('func_4982')
func_4986_call = mutated_mod.get_global_var('func_4986')
var_4994 = relay.var("var_4994", dtype = "uint64", shape = ())#candidate|4994|()|var|uint64
const_4995 = relay.const([2,-3,-2,5,5,-10,-9,8,-4,6,10,-4,3,-7,-4,-4,-8,5,-9,-5,2,-5,-6,3,-6,1,-10,-7,10,-4,8,5,9,9,-10,10,-10,3,10,8,-6,9,4,10,2,2,-6,-10,-5,-10,-3,-7,7,-1,-9,-4,9,-2,1,-9,-8,7,-8,-6,3,-9,8,9,7,6,-10,10,4,-2,-6,2,-4,5,-3,6,-8,-10,1,4,1,4,10,1,-6,1,-6,5,9,3,-2,7,5,10,9,2,4,1,9,-10,-7,-8,-3,4,-2,3,7,8,9,6,2,10,-5,1,-5,1,-1,2,10,5,4,-8,10,-4,3,-1,-9,10,1,10,-4,7,-9,-9,-6,3,-4,2,-6,-5,6,4,6,-1,-7,5,3,-7,1,-3,10,-9,-8,10,-7,3,-10,9,2,7,5,3,3,2,7,3,3,2,2,5,7,-1,4,-7,3,10,-5,6,2,-4,-3,-6,8,6,-2,-9,9,-9,1,-3,-9,2,3,-4,8,-6,6,7,-4,5,-6,-8,-4,9,-3,2,5,-6,4,5,-1,-2,7,-2,-4,8,3,6,2,-5,-10,-5,-2,3,-4,-7,1,1,-1,-10,3,-9,-3,6,-10,8,-9,-5,5,-9,6,3,7,7,8,7,5,-6,10,-6,4,-2,-9,3,5,-5,8,-10,2,7,7,9,-9,-2,8,9,2,-4,8,-4,-1,-6,7,-6,-3,8,6,-2,4,-5,-2,4,-8,4,8,-1,-9,10,2,6,10,5,-3,2,-3,-10,1,-10,2,5,1,9,-2,7,-4,7,-7,9,-3,7,-7,-2,1,-7,5,-3,7,-8,2,1,8,-1,4,7,2,-3,1,9,-7,-6,-8,9,-2,6,-4,-1,9,-1,1,-10,2,-4,-1,6,9,10,-1,-5,-10,9,10,-6,2,-1,5,-8,7,3,-4,5,3,1,6,8,-6,10,9,-4,5,-5,-9,1,-6,-3,3,4,-5,9,8,9,-6,-2,5,5,-1,2,5,5,8,-2,6,-7,8,4,7,3,-2,-8,1,9,-6,-4,-4,4,7,-3,3,-5,9,-8,5,-8,8,-6,-1,-3], dtype = "uint64")#candidate|4995|(420,)|const|uint64
call_4993 = func_4982_call(relay.reshape(var_4994.astype('uint64'), []), relay.reshape(const_4995.astype('uint64'), [7, 15, 4]), )
call_4996 = func_4982_call(relay.reshape(var_4994.astype('uint64'), []), relay.reshape(const_4995.astype('uint64'), [7, 15, 4]), )
bop_5017 = relay.not_equal(var_4994.astype('bool'), call_4993.astype('bool')) # shape=(7, 15, 4)
bop_5020 = relay.not_equal(var_4994.astype('bool'), call_4996.astype('bool')) # shape=(7, 15, 4)
func_468_call = mod.get_global_var('func_468')
func_470_call = mutated_mod.get_global_var('func_470')
call_5030 = relay.TupleGetItem(func_468_call(), 2)
call_5031 = relay.TupleGetItem(func_470_call(), 2)
bop_5037 = relay.greater_equal(bop_5017.astype('bool'), relay.reshape(const_4995.astype('bool'), relay.shape_of(bop_5017))) # shape=(7, 15, 4)
bop_5040 = relay.greater_equal(bop_5020.astype('bool'), relay.reshape(const_4995.astype('bool'), relay.shape_of(bop_5020))) # shape=(7, 15, 4)
func_1383_call = mod.get_global_var('func_1383')
func_1384_call = mutated_mod.get_global_var('func_1384')
call_5051 = relay.TupleGetItem(func_1383_call(), 1)
call_5052 = relay.TupleGetItem(func_1384_call(), 1)
func_4536_call = mod.get_global_var('func_4536')
func_4539_call = mutated_mod.get_global_var('func_4539')
var_5064 = relay.var("var_5064", dtype = "float64", shape = (132,))#candidate|5064|(132,)|var|float64
call_5063 = relay.TupleGetItem(func_4536_call(relay.reshape(var_4994.astype('float64'), []), relay.reshape(var_5064.astype('float64'), [1, 11, 12]), ), 0)
call_5065 = relay.TupleGetItem(func_4539_call(relay.reshape(var_4994.astype('float64'), []), relay.reshape(var_5064.astype('float64'), [1, 11, 12]), ), 0)
bop_5069 = relay.multiply(bop_5037.astype('uint8'), var_4994.astype('uint8')) # shape=(7, 15, 4)
bop_5072 = relay.multiply(bop_5040.astype('uint8'), var_4994.astype('uint8')) # shape=(7, 15, 4)
output = relay.Tuple([call_4988,call_5030,call_5051,call_5063,var_5064,bop_5069,])
output2 = relay.Tuple([call_4989,call_5031,call_5052,call_5065,var_5064,bop_5072,])
func_5076 = relay.Function([var_4994,var_5064,], output)
mod['func_5076'] = func_5076
mod = relay.transform.InferType()(mod)
mutated_mod['func_5076'] = func_5076
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5076_call = mutated_mod.get_global_var('func_5076')
var_5078 = relay.var("var_5078", dtype = "uint64", shape = ())#candidate|5078|()|var|uint64
var_5079 = relay.var("var_5079", dtype = "float64", shape = (132,))#candidate|5079|(132,)|var|float64
call_5077 = func_5076_call(var_5078,var_5079,)
output = call_5077
func_5080 = relay.Function([var_5078,var_5079,], output)
mutated_mod['func_5080'] = func_5080
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5107 = relay.var("var_5107", dtype = "float64", shape = (5, 4, 6))#candidate|5107|(5, 4, 6)|var|float64
uop_5108 = relay.atan(var_5107.astype('float64')) # shape=(5, 4, 6)
func_1115_call = mod.get_global_var('func_1115')
func_1116_call = mutated_mod.get_global_var('func_1116')
call_5113 = relay.TupleGetItem(func_1115_call(), 0)
call_5114 = relay.TupleGetItem(func_1116_call(), 0)
uop_5119 = relay.sqrt(uop_5108.astype('float64')) # shape=(5, 4, 6)
output = relay.Tuple([call_5113,uop_5119,])
output2 = relay.Tuple([call_5114,uop_5119,])
func_5127 = relay.Function([var_5107,], output)
mod['func_5127'] = func_5127
mod = relay.transform.InferType()(mod)
mutated_mod['func_5127'] = func_5127
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5128 = relay.var("var_5128", dtype = "float64", shape = (5, 4, 6))#candidate|5128|(5, 4, 6)|var|float64
func_5127_call = mutated_mod.get_global_var('func_5127')
call_5129 = func_5127_call(var_5128)
output = call_5129
func_5130 = relay.Function([var_5128], output)
mutated_mod['func_5130'] = func_5130
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2001_call = mod.get_global_var('func_2001')
func_2002_call = mutated_mod.get_global_var('func_2002')
call_5145 = relay.TupleGetItem(func_2001_call(), 0)
call_5146 = relay.TupleGetItem(func_2002_call(), 0)
output = relay.Tuple([call_5145,])
output2 = relay.Tuple([call_5146,])
func_5150 = relay.Function([], output)
mod['func_5150'] = func_5150
mod = relay.transform.InferType()(mod)
output = func_5150()
func_5151 = relay.Function([], output)
mutated_mod['func_5151'] = func_5151
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1958_call = mod.get_global_var('func_1958')
func_1960_call = mutated_mod.get_global_var('func_1960')
call_5163 = relay.TupleGetItem(func_1958_call(), 0)
call_5164 = relay.TupleGetItem(func_1960_call(), 0)
output = call_5163
output2 = call_5164
func_5179 = relay.Function([], output)
mod['func_5179'] = func_5179
mod = relay.transform.InferType()(mod)
mutated_mod['func_5179'] = func_5179
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5179_call = mutated_mod.get_global_var('func_5179')
call_5180 = func_5179_call()
output = call_5180
func_5181 = relay.Function([], output)
mutated_mod['func_5181'] = func_5181
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2572_call = mod.get_global_var('func_2572')
func_2574_call = mutated_mod.get_global_var('func_2574')
call_5212 = func_2572_call()
call_5213 = func_2572_call()
output = call_5212
output2 = call_5213
func_5253 = relay.Function([], output)
mod['func_5253'] = func_5253
mod = relay.transform.InferType()(mod)
mutated_mod['func_5253'] = func_5253
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5253_call = mutated_mod.get_global_var('func_5253')
call_5254 = func_5253_call()
output = call_5254
func_5255 = relay.Function([], output)
mutated_mod['func_5255'] = func_5255
mutated_mod = relay.transform.InferType()(mutated_mod)
func_433_call = mod.get_global_var('func_433')
func_434_call = mutated_mod.get_global_var('func_434')
call_5294 = func_433_call()
call_5295 = func_433_call()
output = relay.Tuple([call_5294,])
output2 = relay.Tuple([call_5295,])
func_5296 = relay.Function([], output)
mod['func_5296'] = func_5296
mod = relay.transform.InferType()(mod)
output = func_5296()
func_5297 = relay.Function([], output)
mutated_mod['func_5297'] = func_5297
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1958_call = mod.get_global_var('func_1958')
func_1960_call = mutated_mod.get_global_var('func_1960')
call_5309 = relay.TupleGetItem(func_1958_call(), 0)
call_5310 = relay.TupleGetItem(func_1960_call(), 0)
func_1037_call = mod.get_global_var('func_1037')
func_1041_call = mutated_mod.get_global_var('func_1041')
var_5336 = relay.var("var_5336", dtype = "float64", shape = (108,))#candidate|5336|(108,)|var|float64
call_5335 = relay.TupleGetItem(func_1037_call(relay.reshape(var_5336.astype('float64'), [3, 36]), relay.reshape(var_5336.astype('float64'), [3, 36]), relay.reshape(call_5309.astype('float32'), [9, 9, 13]), ), 10)
call_5337 = relay.TupleGetItem(func_1041_call(relay.reshape(var_5336.astype('float64'), [3, 36]), relay.reshape(var_5336.astype('float64'), [3, 36]), relay.reshape(call_5309.astype('float32'), [9, 9, 13]), ), 10)
func_5076_call = mod.get_global_var('func_5076')
func_5080_call = mutated_mod.get_global_var('func_5080')
var_5348 = relay.var("var_5348", dtype = "uint64", shape = ())#candidate|5348|()|var|uint64
const_5349 = relay.const([-0.996838,3.994261,-4.688078,2.570358,-7.394574,3.448154,-0.710348,1.960530,-0.190751,9.078256,2.259183,4.633838,6.578717,7.132864,7.690440,-0.791071,-8.156364,-2.709988,8.004414,9.940818,8.450370,6.799698,-3.361977,7.944480,-0.602187,1.376538,5.547328,4.319953,-4.426234,4.898145,8.490113,4.204437,3.957892,-6.410183,0.290886,-6.296070,9.753231,9.958338,-6.987526,-7.604752,4.491958,4.946708,-1.326156,9.633162,8.824590,-2.219548,-1.643069,-3.728831,0.955337,-3.922650,6.420691,4.056984,-6.800203,-1.196199,6.352761,-7.779615,-8.513852,3.149338,-9.296426,6.475605,5.329998,-8.483793,2.714939,-7.602642,8.135582,-4.611344,0.880544,1.225206,-1.917545,4.999989,-5.954235,-1.359599,9.709879,6.709848,-0.625454,8.601534,7.973938,4.791879,5.913168,6.242870,-5.738210,7.417451,-2.514522,1.979198,-9.808400,-7.725930,-3.638295,-6.174272,4.481504,8.370717,-2.755410,0.871863,-8.483258,7.081097,-4.018847,6.900739,-1.459185,4.225683,6.255147,9.127573,4.996336,4.165187,-6.928326,7.364769,4.507041,0.723548,9.658484,7.943363,0.788627,6.799725,-3.476168,-5.006671,8.563329,8.482568,-9.781716,9.087836,-5.853054,-7.083124,-8.152922,-6.477819,-4.434421,1.825891,7.314489,-7.259130,2.360294,-1.861579,-5.933229,-1.623433,-0.260371,-6.830348,-9.756533,-8.924667], dtype = "float64")#candidate|5349|(132,)|const|float64
call_5347 = relay.TupleGetItem(func_5076_call(relay.reshape(var_5348.astype('uint64'), []), relay.reshape(const_5349.astype('float64'), [132,]), ), 4)
call_5350 = relay.TupleGetItem(func_5080_call(relay.reshape(var_5348.astype('uint64'), []), relay.reshape(const_5349.astype('float64'), [132,]), ), 4)
output = relay.Tuple([call_5309,call_5335,var_5336,call_5347,var_5348,const_5349,])
output2 = relay.Tuple([call_5310,call_5337,var_5336,call_5350,var_5348,const_5349,])
func_5360 = relay.Function([var_5336,var_5348,], output)
mod['func_5360'] = func_5360
mod = relay.transform.InferType()(mod)
var_5361 = relay.var("var_5361", dtype = "float64", shape = (108,))#candidate|5361|(108,)|var|float64
var_5362 = relay.var("var_5362", dtype = "uint64", shape = ())#candidate|5362|()|var|uint64
output = func_5360(var_5361,var_5362,)
func_5363 = relay.Function([var_5361,var_5362,], output)
mutated_mod['func_5363'] = func_5363
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2572_call = mod.get_global_var('func_2572')
func_2574_call = mutated_mod.get_global_var('func_2574')
call_5368 = func_2572_call()
call_5369 = func_2572_call()
func_4056_call = mod.get_global_var('func_4056')
func_4061_call = mutated_mod.get_global_var('func_4061')
var_5376 = relay.var("var_5376", dtype = "int8", shape = (96,))#candidate|5376|(96,)|var|int8
var_5377 = relay.var("var_5377", dtype = "int32", shape = (504,))#candidate|5377|(504,)|var|int32
call_5375 = relay.TupleGetItem(func_4056_call(relay.reshape(var_5376.astype('int8'), [6, 8, 2]), relay.reshape(var_5376.astype('int8'), [6, 8, 2]), relay.reshape(var_5377.astype('int32'), [504,]), ), 0)
call_5378 = relay.TupleGetItem(func_4061_call(relay.reshape(var_5376.astype('int8'), [6, 8, 2]), relay.reshape(var_5376.astype('int8'), [6, 8, 2]), relay.reshape(var_5377.astype('int32'), [504,]), ), 0)
func_4877_call = mod.get_global_var('func_4877')
func_4880_call = mutated_mod.get_global_var('func_4880')
var_5380 = relay.var("var_5380", dtype = "float64", shape = (792,))#candidate|5380|(792,)|var|float64
call_5379 = relay.TupleGetItem(func_4877_call(relay.reshape(var_5380.astype('float64'), [6, 12, 11])), 0)
call_5381 = relay.TupleGetItem(func_4880_call(relay.reshape(var_5380.astype('float64'), [6, 12, 11])), 0)
const_5385 = relay.const([[[-9,-8],[10,6],[-9,7],[-10,-8],[5,-2],[2,-2],[-3,6],[-9,-1]],[[7,-9],[-7,3],[9,-4],[2,-8],[9,9],[-3,-10],[8,-2],[-4,9]],[[2,-10],[-10,7],[-2,2],[2,-5],[10,-2],[7,-7],[-8,3],[-4,5]],[[10,-7],[8,-2],[4,8],[-4,6],[-9,4],[2,10],[-4,4],[-7,4]],[[-4,-10],[2,7],[-7,-1],[-6,-4],[-7,10],[4,1],[-6,6],[6,3]],[[-8,6],[-6,-7],[6,4],[8,8],[6,7],[9,-8],[5,-10],[-3,-2]]], dtype = "int8")#candidate|5385|(6, 8, 2)|const|int8
bop_5386 = relay.maximum(call_5375.astype('int16'), relay.reshape(const_5385.astype('int16'), relay.shape_of(call_5375))) # shape=(6, 8, 2)
bop_5389 = relay.maximum(call_5378.astype('int16'), relay.reshape(const_5385.astype('int16'), relay.shape_of(call_5378))) # shape=(6, 8, 2)
func_2859_call = mod.get_global_var('func_2859')
func_2863_call = mutated_mod.get_global_var('func_2863')
call_5390 = relay.TupleGetItem(func_2859_call(relay.reshape(var_5377.astype('int32'), [4, 14, 9]), relay.reshape(var_5377.astype('int32'), [4, 14, 9]), ), 1)
call_5391 = relay.TupleGetItem(func_2863_call(relay.reshape(var_5377.astype('int32'), [4, 14, 9]), relay.reshape(var_5377.astype('int32'), [4, 14, 9]), ), 1)
output = relay.Tuple([call_5368,var_5376,var_5377,call_5379,var_5380,bop_5386,call_5390,])
output2 = relay.Tuple([call_5369,var_5376,var_5377,call_5381,var_5380,bop_5389,call_5391,])
func_5404 = relay.Function([var_5376,var_5377,var_5380,], output)
mod['func_5404'] = func_5404
mod = relay.transform.InferType()(mod)
var_5405 = relay.var("var_5405", dtype = "int8", shape = (96,))#candidate|5405|(96,)|var|int8
var_5406 = relay.var("var_5406", dtype = "int32", shape = (504,))#candidate|5406|(504,)|var|int32
var_5407 = relay.var("var_5407", dtype = "float64", shape = (792,))#candidate|5407|(792,)|var|float64
output = func_5404(var_5405,var_5406,var_5407,)
func_5408 = relay.Function([var_5405,var_5406,var_5407,], output)
mutated_mod['func_5408'] = func_5408
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5451 = relay.var("var_5451", dtype = "float64", shape = (6, 15, 2))#candidate|5451|(6, 15, 2)|var|float64
var_5452 = relay.var("var_5452", dtype = "float64", shape = (6, 15, 2))#candidate|5452|(6, 15, 2)|var|float64
bop_5453 = relay.power(var_5451.astype('float64'), relay.reshape(var_5452.astype('float64'), relay.shape_of(var_5451))) # shape=(6, 15, 2)
var_5466 = relay.var("var_5466", dtype = "float64", shape = (6, 15, 2))#candidate|5466|(6, 15, 2)|var|float64
bop_5467 = relay.logical_or(var_5451.astype('bool'), relay.reshape(var_5466.astype('bool'), relay.shape_of(var_5451))) # shape=(6, 15, 2)
output = relay.Tuple([bop_5453,bop_5467,])
output2 = relay.Tuple([bop_5453,bop_5467,])
func_5479 = relay.Function([var_5451,var_5452,var_5466,], output)
mod['func_5479'] = func_5479
mod = relay.transform.InferType()(mod)
var_5480 = relay.var("var_5480", dtype = "float64", shape = (6, 15, 2))#candidate|5480|(6, 15, 2)|var|float64
var_5481 = relay.var("var_5481", dtype = "float64", shape = (6, 15, 2))#candidate|5481|(6, 15, 2)|var|float64
var_5482 = relay.var("var_5482", dtype = "float64", shape = (6, 15, 2))#candidate|5482|(6, 15, 2)|var|float64
output = func_5479(var_5480,var_5481,var_5482,)
func_5483 = relay.Function([var_5480,var_5481,var_5482,], output)
mutated_mod['func_5483'] = func_5483
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1249_call = mod.get_global_var('func_1249')
func_1251_call = mutated_mod.get_global_var('func_1251')
call_5521 = relay.TupleGetItem(func_1249_call(), 1)
call_5522 = relay.TupleGetItem(func_1251_call(), 1)
func_3239_call = mod.get_global_var('func_3239')
func_3242_call = mutated_mod.get_global_var('func_3242')
const_5532 = relay.const([7,6,-9,-2,-4,-8], dtype = "uint16")#candidate|5532|(6,)|const|uint16
call_5531 = func_3239_call(relay.reshape(const_5532.astype('uint16'), [1, 2, 3]))
call_5533 = func_3239_call(relay.reshape(const_5532.astype('uint16'), [1, 2, 3]))
uop_5537 = relay.atan(call_5521.astype('float32')) # shape=(9, 9, 13)
uop_5539 = relay.atan(call_5522.astype('float32')) # shape=(9, 9, 13)
func_4014_call = mod.get_global_var('func_4014')
func_4015_call = mutated_mod.get_global_var('func_4015')
call_5551 = func_4014_call()
call_5552 = func_4014_call()
output = relay.Tuple([call_5531,const_5532,uop_5537,call_5551,])
output2 = relay.Tuple([call_5533,const_5532,uop_5539,call_5552,])
func_5553 = relay.Function([], output)
mod['func_5553'] = func_5553
mod = relay.transform.InferType()(mod)
mutated_mod['func_5553'] = func_5553
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5553_call = mutated_mod.get_global_var('func_5553')
call_5554 = func_5553_call()
output = call_5554
func_5555 = relay.Function([], output)
mutated_mod['func_5555'] = func_5555
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2105_call = mod.get_global_var('func_2105')
func_2107_call = mutated_mod.get_global_var('func_2107')
call_5611 = relay.TupleGetItem(func_2105_call(), 3)
call_5612 = relay.TupleGetItem(func_2107_call(), 3)
func_3675_call = mod.get_global_var('func_3675')
func_3676_call = mutated_mod.get_global_var('func_3676')
call_5628 = relay.TupleGetItem(func_3675_call(), 0)
call_5629 = relay.TupleGetItem(func_3676_call(), 0)
output = relay.Tuple([call_5611,call_5628,])
output2 = relay.Tuple([call_5612,call_5629,])
func_5631 = relay.Function([], output)
mod['func_5631'] = func_5631
mod = relay.transform.InferType()(mod)
output = func_5631()
func_5632 = relay.Function([], output)
mutated_mod['func_5632'] = func_5632
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2403_call = mod.get_global_var('func_2403')
func_2405_call = mutated_mod.get_global_var('func_2405')
call_5639 = relay.TupleGetItem(func_2403_call(), 1)
call_5640 = relay.TupleGetItem(func_2405_call(), 1)
func_2554_call = mod.get_global_var('func_2554')
func_2557_call = mutated_mod.get_global_var('func_2557')
var_5644 = relay.var("var_5644", dtype = "float32", shape = (1, 88))#candidate|5644|(1, 88)|var|float32
call_5643 = relay.TupleGetItem(func_2554_call(relay.reshape(var_5644.astype('float32'), [1, 8, 11])), 0)
call_5645 = relay.TupleGetItem(func_2557_call(relay.reshape(var_5644.astype('float32'), [1, 8, 11])), 0)
func_2572_call = mod.get_global_var('func_2572')
func_2574_call = mutated_mod.get_global_var('func_2574')
call_5654 = func_2572_call()
call_5655 = func_2572_call()
func_5179_call = mod.get_global_var('func_5179')
func_5181_call = mutated_mod.get_global_var('func_5181')
call_5659 = func_5179_call()
call_5660 = func_5179_call()
func_292_call = mod.get_global_var('func_292')
func_294_call = mutated_mod.get_global_var('func_294')
call_5664 = relay.TupleGetItem(func_292_call(), 0)
call_5665 = relay.TupleGetItem(func_294_call(), 0)
var_5667 = relay.var("var_5667", dtype = "float32", shape = (12, 8, 11))#candidate|5667|(12, 8, 11)|var|float32
bop_5668 = relay.floor_mod(call_5643.astype('float64'), var_5667.astype('float64')) # shape=(12, 8, 11)
bop_5671 = relay.floor_mod(call_5645.astype('float64'), var_5667.astype('float64')) # shape=(12, 8, 11)
func_5479_call = mod.get_global_var('func_5479')
func_5483_call = mutated_mod.get_global_var('func_5483')
const_5674 = relay.const([-4.855834,-7.666247,2.098433,2.222299,1.418893,-3.792305,-3.001626,-2.772875,7.875347,-3.106248,-2.407878,7.828887,-5.442007,-6.027587,6.971046,-1.110685,-3.045005,7.682898,-5.706579,2.154529,-7.253832,6.519050,-8.739899,7.262573,7.737476,-9.304519,-0.826705,1.983248,-2.491348,4.398770,9.861255,6.023760,-0.308162,7.830965,-1.316602,3.886697,-0.796028,0.736851,-5.545323,2.432751,7.112122,0.808150,6.923539,-9.563591,-4.957908,3.792319,8.327881,1.806197,-2.235883,-6.450575,2.043073,6.008248,9.765891,1.171268,2.470046,9.436410,-1.480282,7.506058,-3.305538,2.703811,1.138092,-3.947839,-9.110526,-0.902075,8.949232,9.297342,-5.583993,-1.081291,3.920089,9.935512,-4.699572,7.754135,5.140261,7.353112,-8.105044,-1.648622,1.682986,5.533190,-6.980490,-9.145740,-9.139559,6.576309,-1.964261,-7.006500,0.449510,1.764122,6.117927,-9.260531,6.304688,-6.667599,6.380292,0.419699,3.339798,-5.284944,-2.793166,6.685131,-4.539652,-6.880260,4.282820,-2.484248,-7.074987,-8.768390,0.847183,1.442640,-2.625484,-0.679616,-9.622918,4.324699,-2.100994,-9.977930,-9.437740,-8.830467,-8.042463,-2.382179,2.235334,-7.351647,-5.406840,8.151131,3.222982,-6.751141,-4.685810,5.142103,-2.426349,4.205082,-7.856455,6.258418,8.644295,4.302987,-6.664694,0.536678,0.402973,-0.729864,1.167703,2.423704,-1.284593,-2.012721,-0.063821,4.718752,-7.074689,-4.573037,-4.914962,-9.898834,1.718095,0.629069,7.692298,1.199480,-2.247502,-5.255600,-3.758878,5.427882,9.671312,3.273974,5.440940,-3.605761,7.639231,6.427213,-4.947827,-3.094784,8.848257,-0.885178,-8.206251,7.244244,0.048879,-0.043214,1.991693,-1.609052,-8.990140,9.878481,-4.999092,3.418840,-1.734414,-1.468840,-9.280128,-7.418811,-1.354211,-4.619076,-9.466945,-0.872546,2.168418,2.706966], dtype = "float64")#candidate|5674|(180,)|const|float64
call_5673 = relay.TupleGetItem(func_5479_call(relay.reshape(const_5674.astype('float64'), [6, 15, 2]), relay.reshape(const_5674.astype('float64'), [6, 15, 2]), relay.reshape(const_5674.astype('float64'), [6, 15, 2]), ), 1)
call_5675 = relay.TupleGetItem(func_5483_call(relay.reshape(const_5674.astype('float64'), [6, 15, 2]), relay.reshape(const_5674.astype('float64'), [6, 15, 2]), relay.reshape(const_5674.astype('float64'), [6, 15, 2]), ), 1)
func_1537_call = mod.get_global_var('func_1537')
func_1540_call = mutated_mod.get_global_var('func_1540')
call_5681 = relay.TupleGetItem(func_1537_call(relay.reshape(call_5639.astype('float32'), [9, 9, 13])), 0)
call_5682 = relay.TupleGetItem(func_1540_call(relay.reshape(call_5639.astype('float32'), [9, 9, 13])), 0)
func_3886_call = mod.get_global_var('func_3886')
func_3888_call = mutated_mod.get_global_var('func_3888')
call_5686 = relay.TupleGetItem(func_3886_call(), 0)
call_5687 = relay.TupleGetItem(func_3888_call(), 0)
output = relay.Tuple([call_5639,var_5644,call_5654,call_5659,call_5664,bop_5668,call_5673,const_5674,call_5681,call_5686,])
output2 = relay.Tuple([call_5640,var_5644,call_5655,call_5660,call_5665,bop_5671,call_5675,const_5674,call_5682,call_5687,])
func_5692 = relay.Function([var_5644,var_5667,], output)
mod['func_5692'] = func_5692
mod = relay.transform.InferType()(mod)
mutated_mod['func_5692'] = func_5692
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5692_call = mutated_mod.get_global_var('func_5692')
var_5694 = relay.var("var_5694", dtype = "float32", shape = (1, 88))#candidate|5694|(1, 88)|var|float32
var_5695 = relay.var("var_5695", dtype = "float32", shape = (12, 8, 11))#candidate|5695|(12, 8, 11)|var|float32
call_5693 = func_5692_call(var_5694,var_5695,)
output = call_5693
func_5696 = relay.Function([var_5694,var_5695,], output)
mutated_mod['func_5696'] = func_5696
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5761 = relay.var("var_5761", dtype = "bool", shape = (2, 6, 12))#candidate|5761|(2, 6, 12)|var|bool
var_5762 = relay.var("var_5762", dtype = "bool", shape = (2, 6, 12))#candidate|5762|(2, 6, 12)|var|bool
bop_5763 = relay.logical_and(var_5761.astype('bool'), relay.reshape(var_5762.astype('bool'), relay.shape_of(var_5761))) # shape=(2, 6, 12)
func_1115_call = mod.get_global_var('func_1115')
func_1116_call = mutated_mod.get_global_var('func_1116')
call_5778 = relay.TupleGetItem(func_1115_call(), 0)
call_5779 = relay.TupleGetItem(func_1116_call(), 0)
bop_5791 = relay.less(var_5762.astype('bool'), relay.reshape(var_5761.astype('bool'), relay.shape_of(var_5762))) # shape=(2, 6, 12)
uop_5794 = relay.sqrt(var_5762.astype('float64')) # shape=(2, 6, 12)
bop_5806 = relay.minimum(bop_5791.astype('float64'), relay.reshape(bop_5763.astype('float64'), relay.shape_of(bop_5791))) # shape=(2, 6, 12)
func_4474_call = mod.get_global_var('func_4474')
func_4475_call = mutated_mod.get_global_var('func_4475')
call_5816 = func_4474_call()
call_5817 = func_4474_call()
func_4474_call = mod.get_global_var('func_4474')
func_4475_call = mutated_mod.get_global_var('func_4475')
call_5818 = func_4474_call()
call_5819 = func_4474_call()
output = relay.Tuple([call_5778,uop_5794,bop_5806,call_5816,call_5818,])
output2 = relay.Tuple([call_5779,uop_5794,bop_5806,call_5817,call_5819,])
func_5828 = relay.Function([var_5761,var_5762,], output)
mod['func_5828'] = func_5828
mod = relay.transform.InferType()(mod)
var_5829 = relay.var("var_5829", dtype = "bool", shape = (2, 6, 12))#candidate|5829|(2, 6, 12)|var|bool
var_5830 = relay.var("var_5830", dtype = "bool", shape = (2, 6, 12))#candidate|5830|(2, 6, 12)|var|bool
output = func_5828(var_5829,var_5830,)
func_5831 = relay.Function([var_5829,var_5830,], output)
mutated_mod['func_5831'] = func_5831
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5253_call = mod.get_global_var('func_5253')
func_5255_call = mutated_mod.get_global_var('func_5255')
call_5846 = func_5253_call()
call_5847 = func_5253_call()
output = call_5846
output2 = call_5847
func_5855 = relay.Function([], output)
mod['func_5855'] = func_5855
mod = relay.transform.InferType()(mod)
mutated_mod['func_5855'] = func_5855
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5855_call = mutated_mod.get_global_var('func_5855')
call_5856 = func_5855_call()
output = call_5856
func_5857 = relay.Function([], output)
mutated_mod['func_5857'] = func_5857
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5886 = relay.var("var_5886", dtype = "float32", shape = (12, 16, 2))#candidate|5886|(12, 16, 2)|var|float32
uop_5887 = relay.acosh(var_5886.astype('float32')) # shape=(12, 16, 2)
output = uop_5887
output2 = uop_5887
func_5891 = relay.Function([var_5886,], output)
mod['func_5891'] = func_5891
mod = relay.transform.InferType()(mod)
mutated_mod['func_5891'] = func_5891
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5892 = relay.var("var_5892", dtype = "float32", shape = (12, 16, 2))#candidate|5892|(12, 16, 2)|var|float32
func_5891_call = mutated_mod.get_global_var('func_5891')
call_5893 = func_5891_call(var_5892)
output = call_5893
func_5894 = relay.Function([var_5892], output)
mutated_mod['func_5894'] = func_5894
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2105_call = mod.get_global_var('func_2105')
func_2107_call = mutated_mod.get_global_var('func_2107')
call_5972 = relay.TupleGetItem(func_2105_call(), 3)
call_5973 = relay.TupleGetItem(func_2107_call(), 3)
func_1714_call = mod.get_global_var('func_1714')
func_1715_call = mutated_mod.get_global_var('func_1715')
call_5983 = relay.TupleGetItem(func_1714_call(), 0)
call_5984 = relay.TupleGetItem(func_1715_call(), 0)
bop_5988 = relay.bitwise_xor(call_5972.astype('uint16'), relay.reshape(call_5983.astype('uint16'), relay.shape_of(call_5972))) # shape=(9, 9, 13)
bop_5991 = relay.bitwise_xor(call_5973.astype('uint16'), relay.reshape(call_5984.astype('uint16'), relay.shape_of(call_5973))) # shape=(9, 9, 13)
func_468_call = mod.get_global_var('func_468')
func_470_call = mutated_mod.get_global_var('func_470')
call_5993 = relay.TupleGetItem(func_468_call(), 0)
call_5994 = relay.TupleGetItem(func_470_call(), 0)
output = relay.Tuple([bop_5988,call_5993,])
output2 = relay.Tuple([bop_5991,call_5994,])
func_5998 = relay.Function([], output)
mod['func_5998'] = func_5998
mod = relay.transform.InferType()(mod)
mutated_mod['func_5998'] = func_5998
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5998_call = mutated_mod.get_global_var('func_5998')
call_5999 = func_5998_call()
output = call_5999
func_6000 = relay.Function([], output)
mutated_mod['func_6000'] = func_6000
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2403_call = mod.get_global_var('func_2403')
func_2405_call = mutated_mod.get_global_var('func_2405')
call_6085 = relay.TupleGetItem(func_2403_call(), 0)
call_6086 = relay.TupleGetItem(func_2405_call(), 0)
output = call_6085
output2 = call_6086
func_6103 = relay.Function([], output)
mod['func_6103'] = func_6103
mod = relay.transform.InferType()(mod)
output = func_6103()
func_6104 = relay.Function([], output)
mutated_mod['func_6104'] = func_6104
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2049_call = mod.get_global_var('func_2049')
func_2050_call = mutated_mod.get_global_var('func_2050')
call_6200 = relay.TupleGetItem(func_2049_call(), 0)
call_6201 = relay.TupleGetItem(func_2050_call(), 0)
func_2572_call = mod.get_global_var('func_2572')
func_2574_call = mutated_mod.get_global_var('func_2574')
call_6214 = func_2572_call()
call_6215 = func_2572_call()
func_573_call = mod.get_global_var('func_573')
func_575_call = mutated_mod.get_global_var('func_575')
call_6222 = func_573_call()
call_6223 = func_573_call()
output = relay.Tuple([call_6200,call_6214,call_6222,])
output2 = relay.Tuple([call_6201,call_6215,call_6223,])
func_6229 = relay.Function([], output)
mod['func_6229'] = func_6229
mod = relay.transform.InferType()(mod)
mutated_mod['func_6229'] = func_6229
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6229_call = mutated_mod.get_global_var('func_6229')
call_6230 = func_6229_call()
output = call_6230
func_6231 = relay.Function([], output)
mutated_mod['func_6231'] = func_6231
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3675_call = mod.get_global_var('func_3675')
func_3676_call = mutated_mod.get_global_var('func_3676')
call_6246 = relay.TupleGetItem(func_3675_call(), 0)
call_6247 = relay.TupleGetItem(func_3676_call(), 0)
var_6248 = relay.var("var_6248", dtype = "float32", shape = (10, 7, 12))#candidate|6248|(10, 7, 12)|var|float32
bop_6249 = relay.power(call_6246.astype('float32'), relay.reshape(var_6248.astype('float32'), relay.shape_of(call_6246))) # shape=(10, 7, 12)
bop_6252 = relay.power(call_6247.astype('float32'), relay.reshape(var_6248.astype('float32'), relay.shape_of(call_6247))) # shape=(10, 7, 12)
func_4018_call = mod.get_global_var('func_4018')
func_4020_call = mutated_mod.get_global_var('func_4020')
call_6256 = func_4018_call()
call_6257 = func_4018_call()
output = relay.Tuple([bop_6249,call_6256,])
output2 = relay.Tuple([bop_6252,call_6257,])
func_6259 = relay.Function([var_6248,], output)
mod['func_6259'] = func_6259
mod = relay.transform.InferType()(mod)
mutated_mod['func_6259'] = func_6259
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6260 = relay.var("var_6260", dtype = "float32", shape = (10, 7, 12))#candidate|6260|(10, 7, 12)|var|float32
func_6259_call = mutated_mod.get_global_var('func_6259')
call_6261 = func_6259_call(var_6260)
output = call_6261
func_6262 = relay.Function([var_6260], output)
mutated_mod['func_6262'] = func_6262
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2105_call = mod.get_global_var('func_2105')
func_2107_call = mutated_mod.get_global_var('func_2107')
call_6338 = relay.TupleGetItem(func_2105_call(), 1)
call_6339 = relay.TupleGetItem(func_2107_call(), 1)
func_4675_call = mod.get_global_var('func_4675')
func_4677_call = mutated_mod.get_global_var('func_4677')
call_6345 = relay.TupleGetItem(func_4675_call(), 0)
call_6346 = relay.TupleGetItem(func_4677_call(), 0)
func_4836_call = mod.get_global_var('func_4836')
func_4838_call = mutated_mod.get_global_var('func_4838')
const_6348 = relay.const([-6,9,6,-8,-5,5,-3,6,-5,-1,6,9,6,5,10,7,10,7,-5,5,10,-3,-9,10,10,2,5,-5,3,-2,9,-10,-7,-4,-3,-2,7,8,6,1,9,3,5,7,-7,2,10,6,-10,-10,9,6,7,5,-1,-9,-2,-6,-2,4,4,9,7,-3,-6,-9,-5,5,10,7,-8,4,1,-8,5,-6,9,4,9,-2,2,-3,8,-1,10,2,6,-10,7,2,10,-10,-3,5,-4,10,2,-5,1,-1,-5,1,-10,-8,6,9,-10,-7,3,-5,-10,-5,8,3,5,2,-8,3,3,6,-3,-7,6,-8,-5,8,-9,8,-10,-9,-4,6,6,-1,-3,10,2,1,-3,-6,3,4,6,7,2,2,-9,-9,10,-3,4,8,-1,5,7,4,5,2,-9,-7,5,8,-10,8,-6,-2,4,-10,9,1,-7,8,3,3,-8,-5,-2,8,4,1,-7,-2,-10,-8,-6,-9,-3,6,8,10,-2,1,-9,-3,7,3,-6,6,5,-7,4,5,4,3,-1,-9,7,-4,-1,1,2,3,-9,3,5,-7,7,-8,3,6,4,6,5,2,-10,5,7,9,-9,1,2,4,-2,-4,-4,1,-4,-3,-1,-7,8,-3,10,-10,-2,-4,1,-8,2,9,2,6,-1,7,4,2,-5,-6,7,-3,-8,-5,-7,-1,-7,-7,-2,-7,1,-2,-9,6,9,9,7,5,3,2,5,10,-4,2,-9,-9,-4,-7,7,-7,5,-4,-9,6,1,1,3,-1,-8,5,2,10], dtype = "int8")#candidate|6348|(300,)|const|int8
call_6347 = relay.TupleGetItem(func_4836_call(relay.reshape(const_6348.astype('int8'), [15, 2, 10])), 2)
call_6349 = relay.TupleGetItem(func_4838_call(relay.reshape(const_6348.astype('int8'), [15, 2, 10])), 2)
func_4627_call = mod.get_global_var('func_4627')
func_4629_call = mutated_mod.get_global_var('func_4629')
call_6372 = relay.TupleGetItem(func_4627_call(), 1)
call_6373 = relay.TupleGetItem(func_4629_call(), 1)
func_1537_call = mod.get_global_var('func_1537')
func_1540_call = mutated_mod.get_global_var('func_1540')
call_6374 = relay.TupleGetItem(func_1537_call(relay.reshape(call_6345.astype('float32'), [9, 9, 13])), 0)
call_6375 = relay.TupleGetItem(func_1540_call(relay.reshape(call_6345.astype('float32'), [9, 9, 13])), 0)
uop_6376 = relay.cos(call_6345.astype('float32')) # shape=(9, 9, 13)
uop_6378 = relay.cos(call_6346.astype('float32')) # shape=(9, 9, 13)
output = relay.Tuple([call_6338,call_6347,const_6348,call_6372,call_6374,uop_6376,])
output2 = relay.Tuple([call_6339,call_6349,const_6348,call_6373,call_6375,uop_6378,])
func_6379 = relay.Function([], output)
mod['func_6379'] = func_6379
mod = relay.transform.InferType()(mod)
output = func_6379()
func_6380 = relay.Function([], output)
mutated_mod['func_6380'] = func_6380
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6381 = relay.var("var_6381", dtype = "uint64", shape = (3, 11, 5))#candidate|6381|(3, 11, 5)|var|uint64
const_6382 = relay.const([[[-4,-2,2,6,-5],[3,-4,-1,-8,5],[6,-4,8,-4,10],[6,10,1,-3,-7],[7,6,-10,2,-8],[9,2,2,-1,-3],[-6,-3,9,8,2],[10,5,1,-5,-5],[-1,-6,8,-2,-4],[-10,-4,-7,-8,6],[-10,7,4,-3,2]],[[-1,-10,5,7,-7],[-2,1,9,-8,-3],[-6,3,-10,-3,6],[-9,-8,8,-9,9],[-5,-4,-7,-4,-1],[-1,2,8,1,-3],[7,-5,-2,-6,-7],[-8,8,-1,-6,-1],[-2,2,6,-5,3],[3,-1,5,-3,-8],[-10,7,10,-2,-2]],[[1,-7,9,-5,10],[4,8,-4,-3,-5],[-1,7,10,5,2],[-7,5,-8,-7,1],[-2,1,-2,-2,5],[-6,-10,-6,8,4],[-1,7,-5,10,-9],[-9,8,9,-6,7],[-8,-10,5,1,-1],[5,6,-10,6,-2],[3,-6,-3,10,-7]]], dtype = "uint64")#candidate|6382|(3, 11, 5)|const|uint64
bop_6383 = relay.right_shift(var_6381.astype('uint64'), relay.reshape(const_6382.astype('uint64'), relay.shape_of(var_6381))) # shape=(3, 11, 5)
output = bop_6383
output2 = bop_6383
func_6390 = relay.Function([var_6381,], output)
mod['func_6390'] = func_6390
mod = relay.transform.InferType()(mod)
var_6391 = relay.var("var_6391", dtype = "uint64", shape = (3, 11, 5))#candidate|6391|(3, 11, 5)|var|uint64
output = func_6390(var_6391)
func_6392 = relay.Function([var_6391], output)
mutated_mod['func_6392'] = func_6392
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3436_call = mod.get_global_var('func_3436')
func_3437_call = mutated_mod.get_global_var('func_3437')
call_6410 = relay.TupleGetItem(func_3436_call(), 1)
call_6411 = relay.TupleGetItem(func_3437_call(), 1)
output = call_6410
output2 = call_6411
func_6429 = relay.Function([], output)
mod['func_6429'] = func_6429
mod = relay.transform.InferType()(mod)
mutated_mod['func_6429'] = func_6429
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6429_call = mutated_mod.get_global_var('func_6429')
call_6430 = func_6429_call()
output = call_6430
func_6431 = relay.Function([], output)
mutated_mod['func_6431'] = func_6431
mutated_mod = relay.transform.InferType()(mutated_mod)
func_468_call = mod.get_global_var('func_468')
func_470_call = mutated_mod.get_global_var('func_470')
call_6579 = relay.TupleGetItem(func_468_call(), 0)
call_6580 = relay.TupleGetItem(func_470_call(), 0)
func_2554_call = mod.get_global_var('func_2554')
func_2557_call = mutated_mod.get_global_var('func_2557')
const_6593 = relay.const([[4.278359],[-8.755755],[-5.346276],[0.391107],[-9.267520],[-8.294658],[1.546036],[6.337331],[5.588726],[1.203350],[-2.416398],[-0.500114],[0.648249],[-5.210146],[9.542772],[-5.217582],[9.320257],[-0.847960],[6.867310],[-3.918430],[2.442715],[0.600302],[-9.436560],[6.836673],[2.389238],[-8.718848],[4.785570],[9.406447],[-8.009315],[-5.686904],[4.441542],[3.397346],[-5.606310],[-4.472474],[6.411545],[6.715805],[-0.417265],[3.672466],[6.051200],[-9.113478],[-8.365171],[-4.235583],[3.817666],[-7.023294],[-8.081227],[8.423047],[0.718309],[-0.603602],[-1.979778],[-5.482936],[2.846581],[-1.011761],[-3.262541],[2.455451],[8.373408],[-8.747972],[-7.854857],[4.590461],[7.336087],[8.855384],[8.769723],[0.144464],[3.582096],[-0.499013],[-0.132018],[-7.889903],[-6.445612],[0.460926],[-6.911374],[6.704311],[7.363444],[0.320960],[-3.083251],[2.935641],[-9.776707],[6.286727],[-6.852251],[7.609135],[4.191309],[2.426777],[-4.750361],[0.948245],[9.676687],[0.506085],[3.900070],[7.978206],[2.658210],[-6.750571]], dtype = "float32")#candidate|6593|(88, 1)|const|float32
call_6592 = relay.TupleGetItem(func_2554_call(relay.reshape(const_6593.astype('float32'), [1, 8, 11])), 0)
call_6594 = relay.TupleGetItem(func_2557_call(relay.reshape(const_6593.astype('float32'), [1, 8, 11])), 0)
func_6103_call = mod.get_global_var('func_6103')
func_6104_call = mutated_mod.get_global_var('func_6104')
call_6600 = func_6103_call()
call_6601 = func_6103_call()
uop_6611 = relay.acosh(const_6593.astype('float32')) # shape=(88, 1)
uop_6614 = relay.log2(uop_6611.astype('float64')) # shape=(88, 1)
output = relay.Tuple([call_6579,call_6592,call_6600,uop_6614,])
output2 = relay.Tuple([call_6580,call_6594,call_6601,uop_6614,])
func_6627 = relay.Function([], output)
mod['func_6627'] = func_6627
mod = relay.transform.InferType()(mod)
mutated_mod['func_6627'] = func_6627
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6627_call = mutated_mod.get_global_var('func_6627')
call_6628 = func_6627_call()
output = call_6628
func_6629 = relay.Function([], output)
mutated_mod['func_6629'] = func_6629
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3886_call = mod.get_global_var('func_3886')
func_3888_call = mutated_mod.get_global_var('func_3888')
call_6639 = relay.TupleGetItem(func_3886_call(), 0)
call_6640 = relay.TupleGetItem(func_3888_call(), 0)
func_2780_call = mod.get_global_var('func_2780')
func_2781_call = mutated_mod.get_global_var('func_2781')
call_6666 = relay.TupleGetItem(func_2780_call(), 1)
call_6667 = relay.TupleGetItem(func_2781_call(), 1)
output = relay.Tuple([call_6639,call_6666,])
output2 = relay.Tuple([call_6640,call_6667,])
func_6671 = relay.Function([], output)
mod['func_6671'] = func_6671
mod = relay.transform.InferType()(mod)
mutated_mod['func_6671'] = func_6671
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6671_call = mutated_mod.get_global_var('func_6671')
call_6672 = func_6671_call()
output = call_6672
func_6673 = relay.Function([], output)
mutated_mod['func_6673'] = func_6673
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6687 = relay.const(9.370733, dtype = "float32")#candidate|6687|()|const|float32
var_6688 = relay.var("var_6688", dtype = "float32", shape = (14, 15, 6))#candidate|6688|(14, 15, 6)|var|float32
bop_6689 = relay.minimum(const_6687.astype('float32'), var_6688.astype('float32')) # shape=(14, 15, 6)
output = relay.Tuple([bop_6689,])
output2 = relay.Tuple([bop_6689,])
func_6703 = relay.Function([var_6688,], output)
mod['func_6703'] = func_6703
mod = relay.transform.InferType()(mod)
var_6704 = relay.var("var_6704", dtype = "float32", shape = (14, 15, 6))#candidate|6704|(14, 15, 6)|var|float32
output = func_6703(var_6704)
func_6705 = relay.Function([var_6704], output)
mutated_mod['func_6705'] = func_6705
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3886_call = mod.get_global_var('func_3886')
func_3888_call = mutated_mod.get_global_var('func_3888')
call_6739 = relay.TupleGetItem(func_3886_call(), 0)
call_6740 = relay.TupleGetItem(func_3888_call(), 0)
output = call_6739
output2 = call_6740
func_6747 = relay.Function([], output)
mod['func_6747'] = func_6747
mod = relay.transform.InferType()(mod)
mutated_mod['func_6747'] = func_6747
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6747_call = mutated_mod.get_global_var('func_6747')
call_6748 = func_6747_call()
output = call_6748
func_6749 = relay.Function([], output)
mutated_mod['func_6749'] = func_6749
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6103_call = mod.get_global_var('func_6103')
func_6104_call = mutated_mod.get_global_var('func_6104')
call_6851 = func_6103_call()
call_6852 = func_6103_call()
func_6103_call = mod.get_global_var('func_6103')
func_6104_call = mutated_mod.get_global_var('func_6104')
call_6867 = func_6103_call()
call_6868 = func_6103_call()
func_4536_call = mod.get_global_var('func_4536')
func_4539_call = mutated_mod.get_global_var('func_4539')
const_6872 = relay.const(-5.063124, dtype = "float64")#candidate|6872|()|const|float64
const_6873 = relay.const([6.034233,3.674623,-1.758345,8.000427,6.091899,-2.206999,6.652907,9.016234,4.455544,-8.546727,0.127048,3.923337,5.929331,8.088717,0.363251,-1.689758,8.035506,-0.957648,9.116100,-4.727785,0.895758,-6.975690,-1.753373,-3.480375,2.525397,-9.562593,6.437342,6.135345,5.588000,7.643706,9.343325,7.149656,8.389254,-0.895478,2.626859,-6.836110,4.652491,8.867069,-7.011080,8.781444,5.135511,-8.250896,6.614360,5.850022,2.484454,5.317423,-6.197742,1.003356,5.292516,-3.570239,-9.859793,9.710576,9.048001,4.147828,0.066700,1.395996,-4.551084,2.649952,8.689662,-7.143776,7.345049,3.711202,0.792952,-3.474017,-0.853909,7.759146,5.842795,-6.210197,-3.146522,-2.539640,-4.971856,-3.431239,-7.407190,3.280209,-1.833991,-5.048214,2.313118,7.919760,-2.954978,1.746820,-7.919128,5.787559,-3.270413,-0.836405,1.982710,-1.667109,-4.096467,-4.127186,-4.182672,-4.192417,0.016455,-0.153678,-0.695535,2.273808,2.329414,5.361579,-0.376727,9.832908,-1.884259,7.850746,5.768882,4.125785,-5.483281,-7.207705,8.436923,0.694771,2.642742,-8.142210,2.802472,-1.120257,-7.223410,-4.275814,-3.549355,8.221559,5.668457,-6.768377,-4.123532,-3.651643,2.948105,7.525177,0.009442,9.118872,9.140289,-7.187437,-7.234845,8.642496,-0.968806,5.566981,-4.267330,0.413834,0.682373,-0.945578], dtype = "float64")#candidate|6873|(132,)|const|float64
call_6871 = relay.TupleGetItem(func_4536_call(relay.reshape(const_6872.astype('float64'), []), relay.reshape(const_6873.astype('float64'), [1, 11, 12]), ), 0)
call_6874 = relay.TupleGetItem(func_4539_call(relay.reshape(const_6872.astype('float64'), []), relay.reshape(const_6873.astype('float64'), [1, 11, 12]), ), 0)
output = relay.Tuple([call_6851,call_6867,call_6871,const_6872,const_6873,])
output2 = relay.Tuple([call_6852,call_6868,call_6874,const_6872,const_6873,])
func_6876 = relay.Function([], output)
mod['func_6876'] = func_6876
mod = relay.transform.InferType()(mod)
output = func_6876()
func_6877 = relay.Function([], output)
mutated_mod['func_6877'] = func_6877
mutated_mod = relay.transform.InferType()(mutated_mod)
func_536_call = mod.get_global_var('func_536')
func_537_call = mutated_mod.get_global_var('func_537')
call_6931 = relay.TupleGetItem(func_536_call(), 1)
call_6932 = relay.TupleGetItem(func_537_call(), 1)
func_2001_call = mod.get_global_var('func_2001')
func_2002_call = mutated_mod.get_global_var('func_2002')
call_6953 = relay.TupleGetItem(func_2001_call(), 0)
call_6954 = relay.TupleGetItem(func_2002_call(), 0)
func_4836_call = mod.get_global_var('func_4836')
func_4838_call = mutated_mod.get_global_var('func_4838')
const_6975 = relay.const([8,-6,4,8,7,-4,-5,4,-1,-10,-6,-8,-2,4,-10,10,10,-2,-1,-8,6,7,1,3,-6,4,-7,-6,7,-1,-7,-5,-6,-5,-7,5,-7,5,4,1,8,1,8,-6,-7,1,7,-5,5,10,-5,5,7,-1,5,10,7,-1,-9,9,-2,-4,-10,-10,10,-7,4,6,-2,-2,-9,4,-4,-1,10,2,4,-10,4,-9,1,9,10,7,-2,-2,-9,-9,9,-7,1,2,-5,10,-4,6,-7,-3,2,-10,8,7,10,2,5,-10,-9,2,7,-5,-8,-8,-8,3,-10,-4,7,-8,9,-6,-1,1,-9,8,-4,6,-4,9,7,1,5,8,9,8,-7,-2,-1,2,7,-7,-3,-3,9,-8,-1,4,6,-7,7,5,-10,-4,-2,-2,-6,-8,-1,-7,-10,-7,-6,9,2,-9,3,-6,-10,5,-9,-1,-5,-6,-9,-9,8,1,8,5,8,-10,7,4,-8,-1,6,-2,8,-1,8,5,-7,-9,-8,6,10,9,-4,7,3,-9,-10,4,-8,7,5,4,-10,-7,-9,6,-9,-9,1,-4,-5,-5,-3,-3,4,-9,-1,8,-5,-2,8,-4,-5,1,-8,-2,8,-6,-6,4,-8,-6,-5,2,3,-4,4,-9,10,6,-7,-1,-4,7,-7,-2,3,7,4,8,3,-8,2,5,9,2,-10,10,9,5,-8,4,-5,-9,-8,8,-1,-8,6,-4,5,-1,-10,-8,-10,-6,10,-10,-9,-3,6,-10,-8,9,-2,-10,-1,-1,-4,10,3,-4,8,-7,-5,-5], dtype = "int8")#candidate|6975|(300,)|const|int8
call_6974 = relay.TupleGetItem(func_4836_call(relay.reshape(const_6975.astype('int8'), [15, 2, 10])), 1)
call_6976 = relay.TupleGetItem(func_4838_call(relay.reshape(const_6975.astype('int8'), [15, 2, 10])), 1)
uop_6980 = relay.acosh(call_6974.astype('float32')) # shape=(15, 2, 10)
uop_6982 = relay.acosh(call_6976.astype('float32')) # shape=(15, 2, 10)
bop_6991 = relay.bitwise_and(uop_6980.astype('uint16'), relay.reshape(call_6974.astype('uint16'), relay.shape_of(uop_6980))) # shape=(15, 2, 10)
bop_6994 = relay.bitwise_and(uop_6982.astype('uint16'), relay.reshape(call_6976.astype('uint16'), relay.shape_of(uop_6982))) # shape=(15, 2, 10)
output = relay.Tuple([call_6931,call_6953,const_6975,bop_6991,])
output2 = relay.Tuple([call_6932,call_6954,const_6975,bop_6994,])
func_6995 = relay.Function([], output)
mod['func_6995'] = func_6995
mod = relay.transform.InferType()(mod)
output = func_6995()
func_6996 = relay.Function([], output)
mutated_mod['func_6996'] = func_6996
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3886_call = mod.get_global_var('func_3886')
func_3888_call = mutated_mod.get_global_var('func_3888')
call_7016 = relay.TupleGetItem(func_3886_call(), 0)
call_7017 = relay.TupleGetItem(func_3888_call(), 0)
func_4429_call = mod.get_global_var('func_4429')
func_4430_call = mutated_mod.get_global_var('func_4430')
call_7023 = func_4429_call()
call_7024 = func_4429_call()
output = relay.Tuple([call_7016,call_7023,])
output2 = relay.Tuple([call_7017,call_7024,])
func_7026 = relay.Function([], output)
mod['func_7026'] = func_7026
mod = relay.transform.InferType()(mod)
output = func_7026()
func_7027 = relay.Function([], output)
mutated_mod['func_7027'] = func_7027
mutated_mod = relay.transform.InferType()(mutated_mod)
func_433_call = mod.get_global_var('func_433')
func_434_call = mutated_mod.get_global_var('func_434')
call_7039 = func_433_call()
call_7040 = func_433_call()
output = call_7039
output2 = call_7040
func_7041 = relay.Function([], output)
mod['func_7041'] = func_7041
mod = relay.transform.InferType()(mod)
output = func_7041()
func_7042 = relay.Function([], output)
mutated_mod['func_7042'] = func_7042
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5998_call = mod.get_global_var('func_5998')
func_6000_call = mutated_mod.get_global_var('func_6000')
call_7065 = relay.TupleGetItem(func_5998_call(), 0)
call_7066 = relay.TupleGetItem(func_6000_call(), 0)
output = call_7065
output2 = call_7066
func_7074 = relay.Function([], output)
mod['func_7074'] = func_7074
mod = relay.transform.InferType()(mod)
output = func_7074()
func_7075 = relay.Function([], output)
mutated_mod['func_7075'] = func_7075
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7151 = relay.var("var_7151", dtype = "int8", shape = (4, 14, 12))#candidate|7151|(4, 14, 12)|var|int8
var_7152 = relay.var("var_7152", dtype = "int8", shape = (4, 14, 12))#candidate|7152|(4, 14, 12)|var|int8
bop_7153 = relay.bitwise_xor(var_7151.astype('int8'), relay.reshape(var_7152.astype('int8'), relay.shape_of(var_7151))) # shape=(4, 14, 12)
output = relay.Tuple([bop_7153,])
output2 = relay.Tuple([bop_7153,])
func_7158 = relay.Function([var_7151,var_7152,], output)
mod['func_7158'] = func_7158
mod = relay.transform.InferType()(mod)
var_7159 = relay.var("var_7159", dtype = "int8", shape = (4, 14, 12))#candidate|7159|(4, 14, 12)|var|int8
var_7160 = relay.var("var_7160", dtype = "int8", shape = (4, 14, 12))#candidate|7160|(4, 14, 12)|var|int8
output = func_7158(var_7159,var_7160,)
func_7161 = relay.Function([var_7159,var_7160,], output)
mutated_mod['func_7161'] = func_7161
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3368_call = mod.get_global_var('func_3368')
func_3370_call = mutated_mod.get_global_var('func_3370')
call_7198 = relay.TupleGetItem(func_3368_call(), 1)
call_7199 = relay.TupleGetItem(func_3370_call(), 1)
func_1037_call = mod.get_global_var('func_1037')
func_1041_call = mutated_mod.get_global_var('func_1041')
var_7217 = relay.var("var_7217", dtype = "float64", shape = (108,))#candidate|7217|(108,)|var|float64
call_7216 = relay.TupleGetItem(func_1037_call(relay.reshape(var_7217.astype('float64'), [3, 36]), relay.reshape(var_7217.astype('float64'), [3, 36]), relay.reshape(call_7198.astype('float32'), [9, 9, 13]), ), 4)
call_7218 = relay.TupleGetItem(func_1041_call(relay.reshape(var_7217.astype('float64'), [3, 36]), relay.reshape(var_7217.astype('float64'), [3, 36]), relay.reshape(call_7198.astype('float32'), [9, 9, 13]), ), 4)
output = relay.Tuple([call_7198,call_7216,var_7217,])
output2 = relay.Tuple([call_7199,call_7218,var_7217,])
func_7220 = relay.Function([var_7217,], output)
mod['func_7220'] = func_7220
mod = relay.transform.InferType()(mod)
var_7221 = relay.var("var_7221", dtype = "float64", shape = (108,))#candidate|7221|(108,)|var|float64
output = func_7220(var_7221)
func_7222 = relay.Function([var_7221], output)
mutated_mod['func_7222'] = func_7222
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5998_call = mod.get_global_var('func_5998')
func_6000_call = mutated_mod.get_global_var('func_6000')
call_7227 = relay.TupleGetItem(func_5998_call(), 1)
call_7228 = relay.TupleGetItem(func_6000_call(), 1)
output = relay.Tuple([call_7227,])
output2 = relay.Tuple([call_7228,])
func_7238 = relay.Function([], output)
mod['func_7238'] = func_7238
mod = relay.transform.InferType()(mod)
mutated_mod['func_7238'] = func_7238
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7238_call = mutated_mod.get_global_var('func_7238')
call_7239 = func_7238_call()
output = call_7239
func_7240 = relay.Function([], output)
mutated_mod['func_7240'] = func_7240
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1303_call = mod.get_global_var('func_1303')
func_1304_call = mutated_mod.get_global_var('func_1304')
call_7278 = relay.TupleGetItem(func_1303_call(), 0)
call_7279 = relay.TupleGetItem(func_1304_call(), 0)
func_3584_call = mod.get_global_var('func_3584')
func_3586_call = mutated_mod.get_global_var('func_3586')
call_7284 = relay.TupleGetItem(func_3584_call(), 1)
call_7285 = relay.TupleGetItem(func_3586_call(), 1)
output = relay.Tuple([call_7278,call_7284,])
output2 = relay.Tuple([call_7279,call_7285,])
func_7301 = relay.Function([], output)
mod['func_7301'] = func_7301
mod = relay.transform.InferType()(mod)
output = func_7301()
func_7302 = relay.Function([], output)
mutated_mod['func_7302'] = func_7302
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3584_call = mod.get_global_var('func_3584')
func_3586_call = mutated_mod.get_global_var('func_3586')
call_7344 = relay.TupleGetItem(func_3584_call(), 0)
call_7345 = relay.TupleGetItem(func_3586_call(), 0)
output = call_7344
output2 = call_7345
func_7351 = relay.Function([], output)
mod['func_7351'] = func_7351
mod = relay.transform.InferType()(mod)
output = func_7351()
func_7352 = relay.Function([], output)
mutated_mod['func_7352'] = func_7352
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1064_call = mod.get_global_var('func_1064')
func_1066_call = mutated_mod.get_global_var('func_1066')
call_7391 = func_1064_call()
call_7392 = func_1064_call()
func_1537_call = mod.get_global_var('func_1537')
func_1540_call = mutated_mod.get_global_var('func_1540')
call_7427 = relay.TupleGetItem(func_1537_call(relay.reshape(call_7391.astype('float32'), [9, 9, 13])), 0)
call_7428 = relay.TupleGetItem(func_1540_call(relay.reshape(call_7391.astype('float32'), [9, 9, 13])), 0)
func_2105_call = mod.get_global_var('func_2105')
func_2107_call = mutated_mod.get_global_var('func_2107')
call_7436 = relay.TupleGetItem(func_2105_call(), 3)
call_7437 = relay.TupleGetItem(func_2107_call(), 3)
output = relay.Tuple([call_7391,call_7427,call_7436,])
output2 = relay.Tuple([call_7392,call_7428,call_7437,])
func_7454 = relay.Function([], output)
mod['func_7454'] = func_7454
mod = relay.transform.InferType()(mod)
output = func_7454()
func_7455 = relay.Function([], output)
mutated_mod['func_7455'] = func_7455
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6627_call = mod.get_global_var('func_6627')
func_6629_call = mutated_mod.get_global_var('func_6629')
call_7530 = relay.TupleGetItem(func_6627_call(), 2)
call_7531 = relay.TupleGetItem(func_6629_call(), 2)
output = call_7530
output2 = call_7531
func_7532 = relay.Function([], output)
mod['func_7532'] = func_7532
mod = relay.transform.InferType()(mod)
mutated_mod['func_7532'] = func_7532
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7532_call = mutated_mod.get_global_var('func_7532')
call_7533 = func_7532_call()
output = call_7533
func_7534 = relay.Function([], output)
mutated_mod['func_7534'] = func_7534
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3161_call = mod.get_global_var('func_3161')
func_3163_call = mutated_mod.get_global_var('func_3163')
call_7535 = relay.TupleGetItem(func_3161_call(), 0)
call_7536 = relay.TupleGetItem(func_3163_call(), 0)
func_433_call = mod.get_global_var('func_433')
func_434_call = mutated_mod.get_global_var('func_434')
call_7537 = func_433_call()
call_7538 = func_433_call()
func_5360_call = mod.get_global_var('func_5360')
func_5363_call = mutated_mod.get_global_var('func_5363')
var_7549 = relay.var("var_7549", dtype = "float64", shape = (6, 18))#candidate|7549|(6, 18)|var|float64
const_7550 = relay.const(1, dtype = "uint64")#candidate|7550|()|const|uint64
call_7548 = relay.TupleGetItem(func_5360_call(relay.reshape(var_7549.astype('float64'), [108,]), relay.reshape(const_7550.astype('uint64'), []), ), 1)
call_7551 = relay.TupleGetItem(func_5363_call(relay.reshape(var_7549.astype('float64'), [108,]), relay.reshape(const_7550.astype('uint64'), []), ), 1)
func_4982_call = mod.get_global_var('func_4982')
func_4986_call = mutated_mod.get_global_var('func_4986')
const_7560 = relay.const([-1,-4,1,10,-4,-10,2,9,6,-10,7,10,2,7,3,4,8,-6,-1,-8,3,-6,-4,9,-3,6,-8,7,4,-8,9,-1,-1,7,-3,10,10,3,3,7,2,-5,10,2,7,10,-1,2,-8,-5,3,-7,1,9,3,-9,9,-9,7,2,-1,-7,-1,-6,9,10,-9,7,8,-4,-3,-9,-9,1,8,-8,-4,-3,8,-6,3,9,6,1,-3,4,-2,-8,1,-4,3,-10,-1,-3,-10,-5,8,4,1,5,-2,10,4,-4,-7,6,4,-6,6,-1,-10,-1,10,2,3,-5,-8,1,-3,9,-5,8,2,4,5,6,2,4,7,5,-3,6,-5,5,4,-8,2,10,-1,-2,10,2,7,5,-9,-3,1,6,-8,6,7,-3,-1,1,-7,-8,10,8,5,-3,-4,-9,-8,2,3,2,-1,9,9,-4,4,1,2,-5,-5,-1,5,-5,-4,2,7,9,10,10,9,-4,-7,-9,6,-6,-2,-1,9,-1,5,2,9,1,-1,-9,-6,5,9,2,10,8,7,9,7,10,-7,-7,-6,-6,-9,7,-9,7,-6,5,9,8,-5,5,-8,8,-9,-2,1,-10,-6,-6,-9,10,3,3,-1,9,7,9,-1,3,-10,-5,-6,3,-3,-4,3,-10,-1,10,4,-7,-3,10,-1,-4,-9,-6,-5,4,10,-10,4,-3,5,-7,3,3,10,2,8,4,6,-2,-1,-8,-6,7,-10,-7,4,-7,-9,6,6,1,-5,-1,7,1,2,10,-8,8,-7,-7,10,-9,6,10,-3,-8,-8,-9,-2,4,10,10,10,9,6,10,2,6,-3,2,7,-4,6,-1,-6,2,10,-5,3,-10,2,4,-7,1,-7,8,2,-1,7,-1,-9,-10,-7,1,-9,-9,-1,2,-1,10,10,4,-1,-2,-8,-3,6,-8,-6,-2,-8,-5,-2,-8,4,3,-7,-5,1,-7,10,6,3,8,-2,6,1,-10,-2,8,-6,7,-9,2,-2,10,10,8,9,5,-8,3,4,-4,10,10,6,-9,-4,6,-1,7,-2,5,3,-5,10,-2,-1,-1,-10,-9,2,1,1,9,-4,1,1,9,5,7], dtype = "uint64")#candidate|7560|(420,)|const|uint64
call_7559 = func_4982_call(relay.reshape(const_7550.astype('uint64'), []), relay.reshape(const_7560.astype('uint64'), [7, 15, 4]), )
call_7561 = func_4982_call(relay.reshape(const_7550.astype('uint64'), []), relay.reshape(const_7560.astype('uint64'), [7, 15, 4]), )
output = relay.Tuple([call_7535,call_7537,call_7548,var_7549,const_7550,call_7559,const_7560,])
output2 = relay.Tuple([call_7536,call_7538,call_7551,var_7549,const_7550,call_7561,const_7560,])
func_7564 = relay.Function([var_7549,], output)
mod['func_7564'] = func_7564
mod = relay.transform.InferType()(mod)
mutated_mod['func_7564'] = func_7564
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7565 = relay.var("var_7565", dtype = "float64", shape = (6, 18))#candidate|7565|(6, 18)|var|float64
func_7564_call = mutated_mod.get_global_var('func_7564')
call_7566 = func_7564_call(var_7565)
output = call_7566
func_7567 = relay.Function([var_7565], output)
mutated_mod['func_7567'] = func_7567
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7611 = relay.const([[[5,-6,7,1,-10,7,-4,-10],[7,-3,10,-4,4,-6,1,10],[-1,1,2,-3,-6,8,-9,-9],[10,3,-6,1,-2,10,8,-9],[8,-7,1,-5,-2,1,5,10],[-3,-5,9,10,4,5,2,5],[4,-4,-3,4,-4,-9,-6,-6],[1,8,9,3,8,9,2,1],[5,-2,4,4,-10,9,-1,5],[-6,1,-8,3,2,5,-4,-1],[10,7,-9,2,-5,7,5,7],[-2,-1,5,-8,3,-3,10,8],[-9,-5,-10,-10,-9,-3,1,-8]],[[-10,-5,10,-4,-9,-2,4,10],[-8,4,2,-5,2,-5,-9,6],[-1,-6,6,-6,8,-3,-1,-6],[6,9,3,-10,1,8,10,9],[6,-4,5,9,-9,6,5,-1],[1,10,-5,6,6,7,-9,7],[2,-10,-1,-2,3,-2,-9,9],[4,-1,10,6,5,-3,-10,10],[2,-10,-2,3,10,2,-10,-7],[-10,3,10,-7,-3,-9,-1,-2],[10,-3,-4,-8,4,4,-10,-10],[1,-2,5,6,-2,-8,4,3],[3,8,6,2,5,8,6,8]],[[3,10,9,-3,-3,-3,2,2],[-6,5,-8,4,4,1,-7,-9],[8,8,7,10,4,-6,-9,-6],[-1,-7,-9,-4,-10,-10,1,7],[9,9,-7,-4,10,9,-8,-6],[-5,8,3,-4,-5,10,-6,-7],[4,-2,5,-4,-8,6,-10,-5],[-7,-9,-6,-3,-1,-1,2,3],[6,-9,-3,-7,7,-9,8,-4],[-10,5,-9,-7,1,-9,-5,-1],[10,-1,-4,-8,-2,10,10,6],[10,-5,10,-9,-7,-8,-3,-5],[-8,7,-5,-2,1,-8,7,-2]],[[5,-6,-7,-10,3,1,6,8],[2,-5,-2,3,-1,4,-7,5],[-2,-9,-5,-7,6,6,-4,5],[2,1,6,-7,9,7,8,9],[4,-10,8,9,5,-5,10,5],[9,5,-1,4,-2,7,-4,1],[-4,-7,10,6,9,-4,-9,-10],[4,6,8,9,-1,-1,1,-3],[2,-7,3,-10,5,1,3,-2],[9,-6,10,-6,-10,-5,8,7],[-5,-4,10,-3,8,-8,-7,9],[10,2,1,-10,6,5,5,-8],[10,1,6,4,-7,-6,-5,-2]],[[-2,-5,-6,-7,4,8,4,10],[-8,4,6,-9,-10,-9,9,10],[-10,6,1,8,-3,-5,-2,3],[-7,-3,6,-5,-6,1,-10,9],[-7,-3,6,6,-10,10,-5,2],[-3,4,-7,-6,-7,-8,-2,-4],[2,9,-1,-9,5,2,4,3],[-9,7,-8,-8,-1,-10,5,-2],[-3,5,6,-4,-3,1,10,-5],[3,-6,-4,-5,-3,10,3,5],[4,2,3,-3,4,-6,-7,5],[4,10,6,-4,4,-6,-9,3],[-10,5,10,-10,1,-9,8,8]]], dtype = "int8")#candidate|7611|(5, 13, 8)|const|int8
const_7612 = relay.const([[[8,-2,2,9,7,-7,9,-8],[-6,-3,-3,5,-8,6,-3,-9],[6,7,-1,7,-4,-7,-6,7],[9,7,1,-1,-6,-2,5,-10],[-3,8,5,-4,-10,5,9,10],[-4,-9,8,3,8,-4,1,1],[-3,9,-6,1,5,4,8,3],[10,6,-3,-3,-8,-3,3,2],[5,-7,6,9,-2,7,-8,1],[-4,5,7,10,6,-2,-9,8],[8,7,3,-5,-2,6,-5,-5],[3,-10,-9,-6,6,-6,4,9],[7,-4,-3,-7,3,2,-2,9]],[[-8,-8,7,-3,-3,8,-1,9],[-2,-10,4,-1,-3,-5,1,-10],[2,7,3,-2,7,6,-8,7],[2,6,-9,4,-9,6,-4,-10],[-6,6,7,8,10,3,10,8],[9,7,1,1,2,-2,6,3],[-9,5,-6,1,6,-6,5,-10],[9,4,1,-2,3,-9,5,4],[10,-1,2,-6,5,-9,-5,-5],[-6,-4,2,-8,-9,-7,1,-10],[3,-9,3,-5,7,-7,3,-5],[-10,-4,7,9,-10,-2,-10,-4],[-4,-7,-10,3,6,-8,-1,6]],[[3,4,-1,-6,1,-4,10,3],[-2,-1,1,-10,4,-8,2,-6],[3,5,-5,8,8,-9,1,2],[-10,-6,7,-2,3,-7,3,9],[5,3,-4,-8,-3,3,-8,-7],[-10,-1,-8,-9,2,-5,-1,-10],[-8,-6,4,-7,2,-10,8,9],[2,-6,-5,-1,-1,2,3,-8],[-5,-5,10,-7,-3,5,4,-9],[7,7,10,-7,-8,-5,-2,-2],[-9,7,1,4,-1,-7,-4,-1],[2,3,10,5,10,9,-2,9],[9,3,-10,-8,-7,-5,-1,-3]],[[8,7,5,-6,-3,-5,7,8],[-9,-10,9,9,-2,8,1,-10],[-5,-7,-10,-3,9,2,1,-5],[-3,1,-2,-10,5,10,9,-6],[-9,-7,7,4,10,-3,-3,3],[-5,10,7,4,9,-9,-5,5],[10,-3,-3,-5,10,-6,-8,1],[-5,1,-2,-1,2,-9,5,-1],[7,-1,10,3,-6,2,-8,-7],[5,-5,4,8,-8,-5,3,7],[9,-10,6,6,4,5,-3,5],[10,-5,-7,-2,-9,5,2,-2],[4,7,-7,1,3,3,6,-3]],[[9,-5,-8,9,-6,9,-10,9],[5,3,1,3,-8,1,8,4],[-2,6,-6,9,-1,9,9,5],[-6,-6,-2,2,-9,6,4,7],[-9,-6,-7,-6,-5,-2,-5,-10],[5,7,-7,9,-9,-3,7,1],[-10,10,3,-6,2,-3,-4,7],[9,1,2,-3,-7,4,-6,-9],[-3,4,6,4,-9,-7,10,-6],[-8,4,-9,1,-3,9,1,6],[4,9,3,7,8,6,-8,6],[1,5,9,3,10,-3,-7,-4],[10,-2,5,-4,-5,-3,-5,10]]], dtype = "int8")#candidate|7612|(5, 13, 8)|const|int8
bop_7613 = relay.greater(const_7611.astype('bool'), relay.reshape(const_7612.astype('bool'), relay.shape_of(const_7611))) # shape=(5, 13, 8)
uop_7618 = relay.atanh(bop_7613.astype('float32')) # shape=(5, 13, 8)
output = relay.Tuple([uop_7618,])
output2 = relay.Tuple([uop_7618,])
func_7626 = relay.Function([], output)
mod['func_7626'] = func_7626
mod = relay.transform.InferType()(mod)
mutated_mod['func_7626'] = func_7626
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7626_call = mutated_mod.get_global_var('func_7626')
call_7627 = func_7626_call()
output = call_7627
func_7628 = relay.Function([], output)
mutated_mod['func_7628'] = func_7628
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7632 = relay.var("var_7632", dtype = "float64", shape = (4, 1, 7))#candidate|7632|(4, 1, 7)|var|float64
uop_7633 = relay.acosh(var_7632.astype('float64')) # shape=(4, 1, 7)
bop_7636 = relay.minimum(var_7632.astype('uint64'), relay.reshape(uop_7633.astype('uint64'), relay.shape_of(var_7632))) # shape=(4, 1, 7)
output = bop_7636
output2 = bop_7636
F = relay.Function([var_7632,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_7632,], output2)
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
