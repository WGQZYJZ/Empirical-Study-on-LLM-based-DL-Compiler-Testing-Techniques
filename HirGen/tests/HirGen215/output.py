import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
const_250 = relay.const([[[False,True,True,True,True,False,True,True,True],[True,True,False,False,False,True,True,True,False],[False,False,True,False,True,True,False,False,True],[False,True,True,False,True,False,False,False,False],[False,True,True,True,False,False,True,False,False],[True,False,True,True,False,False,False,False,True],[False,False,True,True,False,False,False,True,True],[True,True,True,True,True,False,False,True,False]],[[False,False,True,False,True,True,False,False,True],[False,True,True,True,True,False,False,False,False],[False,False,True,True,True,False,False,False,False],[False,False,True,False,False,True,True,True,True],[False,True,True,True,True,False,True,False,True],[True,False,True,True,False,False,True,True,True],[True,True,False,True,True,False,False,True,True],[False,True,False,True,True,True,False,True,False]],[[True,False,False,False,True,False,False,False,False],[False,True,True,True,True,False,True,False,True],[False,True,False,True,True,True,True,False,True],[False,False,False,False,True,False,False,False,True],[False,False,True,False,False,True,True,True,False],[True,True,False,False,True,True,False,False,False],[False,True,False,True,True,True,True,True,False],[True,True,False,False,True,False,True,True,False]]], dtype = "bool")#candidate|250|(3, 8, 9)|const|bool
const_251 = relay.const([[[False,False,False,True,True,True,True,False,False],[True,False,True,True,True,True,False,False,False],[True,True,True,False,False,True,False,True,False],[False,False,False,False,False,False,True,True,True],[False,False,True,False,True,True,True,True,False],[True,True,False,True,True,True,False,True,True],[False,False,False,False,False,False,False,False,False],[True,True,True,False,True,True,False,False,True]],[[True,True,False,False,False,True,False,False,False],[False,False,False,True,False,False,False,False,False],[False,True,False,True,False,False,False,False,True],[False,False,True,True,False,True,True,False,True],[False,False,True,True,False,False,True,False,False],[True,False,True,True,False,False,True,True,False],[True,False,False,True,False,True,False,True,True],[True,False,True,True,False,True,False,True,False]],[[False,False,False,True,True,False,False,False,False],[False,False,False,False,True,False,False,False,False],[True,True,True,False,False,True,True,True,True],[True,False,True,True,False,True,True,True,True],[True,True,True,True,True,True,True,True,True],[True,False,True,True,True,False,False,False,True],[True,True,False,True,False,False,False,True,True],[True,False,False,False,True,False,False,True,True]]], dtype = "bool")#candidate|251|(3, 8, 9)|const|bool
bop_252 = relay.logical_or(const_250.astype('bool'), relay.reshape(const_251.astype('bool'), relay.shape_of(const_250))) # shape=(3, 8, 9)
output = bop_252
output2 = bop_252
func_255 = relay.Function([], output)
mod['func_255'] = func_255
mod = relay.transform.InferType()(mod)
mutated_mod['func_255'] = func_255
mutated_mod = relay.transform.InferType()(mutated_mod)
func_255_call = mutated_mod.get_global_var('func_255')
call_256 = func_255_call()
output = call_256
func_257 = relay.Function([], output)
mutated_mod['func_257'] = func_257
mutated_mod = relay.transform.InferType()(mutated_mod)
func_255_call = mod.get_global_var('func_255')
func_257_call = mutated_mod.get_global_var('func_257')
call_319 = func_255_call()
call_320 = func_255_call()
uop_328 = relay.atan(call_319.astype('float64')) # shape=(3, 8, 9)
uop_330 = relay.atan(call_320.astype('float64')) # shape=(3, 8, 9)
output = uop_328
output2 = uop_330
func_332 = relay.Function([], output)
mod['func_332'] = func_332
mod = relay.transform.InferType()(mod)
output = func_332()
func_333 = relay.Function([], output)
mutated_mod['func_333'] = func_333
mutated_mod = relay.transform.InferType()(mutated_mod)
func_255_call = mod.get_global_var('func_255')
func_257_call = mutated_mod.get_global_var('func_257')
call_434 = func_255_call()
call_435 = func_255_call()
uop_436 = relay.erf(call_434.astype('float32')) # shape=(3, 8, 9)
uop_438 = relay.erf(call_435.astype('float32')) # shape=(3, 8, 9)
uop_444 = relay.sin(uop_436.astype('float32')) # shape=(3, 8, 9)
uop_446 = relay.sin(uop_438.astype('float32')) # shape=(3, 8, 9)
bop_459 = relay.left_shift(uop_436.astype('int16'), relay.reshape(uop_444.astype('int16'), relay.shape_of(uop_436))) # shape=(3, 8, 9)
bop_462 = relay.left_shift(uop_438.astype('int16'), relay.reshape(uop_446.astype('int16'), relay.shape_of(uop_438))) # shape=(3, 8, 9)
output = bop_459
output2 = bop_462
func_507 = relay.Function([], output)
mod['func_507'] = func_507
mod = relay.transform.InferType()(mod)
output = func_507()
func_508 = relay.Function([], output)
mutated_mod['func_508'] = func_508
mutated_mod = relay.transform.InferType()(mutated_mod)
func_507_call = mod.get_global_var('func_507')
func_508_call = mutated_mod.get_global_var('func_508')
call_522 = func_507_call()
call_523 = func_507_call()
func_332_call = mod.get_global_var('func_332')
func_333_call = mutated_mod.get_global_var('func_333')
call_526 = func_332_call()
call_527 = func_332_call()
output = relay.Tuple([call_522,call_526,])
output2 = relay.Tuple([call_523,call_527,])
func_543 = relay.Function([], output)
mod['func_543'] = func_543
mod = relay.transform.InferType()(mod)
output = func_543()
func_544 = relay.Function([], output)
mutated_mod['func_544'] = func_544
mutated_mod = relay.transform.InferType()(mutated_mod)
func_255_call = mod.get_global_var('func_255')
func_257_call = mutated_mod.get_global_var('func_257')
call_554 = func_255_call()
call_555 = func_255_call()
var_556 = relay.var("var_556", dtype = "bool", shape = (3, 8, 9))#candidate|556|(3, 8, 9)|var|bool
bop_557 = relay.equal(call_554.astype('bool'), relay.reshape(var_556.astype('bool'), relay.shape_of(call_554))) # shape=(3, 8, 9)
bop_560 = relay.equal(call_555.astype('bool'), relay.reshape(var_556.astype('bool'), relay.shape_of(call_555))) # shape=(3, 8, 9)
bop_563 = relay.bitwise_xor(call_554.astype('uint32'), relay.reshape(bop_557.astype('uint32'), relay.shape_of(call_554))) # shape=(3, 8, 9)
bop_566 = relay.bitwise_xor(call_555.astype('uint32'), relay.reshape(bop_560.astype('uint32'), relay.shape_of(call_555))) # shape=(3, 8, 9)
bop_571 = relay.floor_mod(bop_557.astype('float32'), relay.reshape(bop_563.astype('float32'), relay.shape_of(bop_557))) # shape=(3, 8, 9)
bop_574 = relay.floor_mod(bop_560.astype('float32'), relay.reshape(bop_566.astype('float32'), relay.shape_of(bop_560))) # shape=(3, 8, 9)
output = bop_571
output2 = bop_574
func_577 = relay.Function([var_556,], output)
mod['func_577'] = func_577
mod = relay.transform.InferType()(mod)
mutated_mod['func_577'] = func_577
mutated_mod = relay.transform.InferType()(mutated_mod)
var_578 = relay.var("var_578", dtype = "bool", shape = (3, 8, 9))#candidate|578|(3, 8, 9)|var|bool
func_577_call = mutated_mod.get_global_var('func_577')
call_579 = func_577_call(var_578)
output = call_579
func_580 = relay.Function([var_578], output)
mutated_mod['func_580'] = func_580
mutated_mod = relay.transform.InferType()(mutated_mod)
func_332_call = mod.get_global_var('func_332')
func_333_call = mutated_mod.get_global_var('func_333')
call_600 = func_332_call()
call_601 = func_332_call()
func_255_call = mod.get_global_var('func_255')
func_257_call = mutated_mod.get_global_var('func_257')
call_604 = func_255_call()
call_605 = func_255_call()
output = relay.Tuple([call_600,call_604,])
output2 = relay.Tuple([call_601,call_605,])
func_609 = relay.Function([], output)
mod['func_609'] = func_609
mod = relay.transform.InferType()(mod)
mutated_mod['func_609'] = func_609
mutated_mod = relay.transform.InferType()(mutated_mod)
func_609_call = mutated_mod.get_global_var('func_609')
call_610 = func_609_call()
output = call_610
func_611 = relay.Function([], output)
mutated_mod['func_611'] = func_611
mutated_mod = relay.transform.InferType()(mutated_mod)
var_612 = relay.var("var_612", dtype = "float64", shape = (5, 14, 13))#candidate|612|(5, 14, 13)|var|float64
var_613 = relay.var("var_613", dtype = "float64", shape = (5, 14, 13))#candidate|613|(5, 14, 13)|var|float64
bop_614 = relay.floor_mod(var_612.astype('float64'), relay.reshape(var_613.astype('float64'), relay.shape_of(var_612))) # shape=(5, 14, 13)
output = bop_614
output2 = bop_614
func_620 = relay.Function([var_612,var_613,], output)
mod['func_620'] = func_620
mod = relay.transform.InferType()(mod)
var_621 = relay.var("var_621", dtype = "float64", shape = (5, 14, 13))#candidate|621|(5, 14, 13)|var|float64
var_622 = relay.var("var_622", dtype = "float64", shape = (5, 14, 13))#candidate|622|(5, 14, 13)|var|float64
output = func_620(var_621,var_622,)
func_623 = relay.Function([var_621,var_622,], output)
mutated_mod['func_623'] = func_623
mutated_mod = relay.transform.InferType()(mutated_mod)
func_332_call = mod.get_global_var('func_332')
func_333_call = mutated_mod.get_global_var('func_333')
call_630 = func_332_call()
call_631 = func_332_call()
output = call_630
output2 = call_631
func_638 = relay.Function([], output)
mod['func_638'] = func_638
mod = relay.transform.InferType()(mod)
mutated_mod['func_638'] = func_638
mutated_mod = relay.transform.InferType()(mutated_mod)
func_638_call = mutated_mod.get_global_var('func_638')
call_639 = func_638_call()
output = call_639
func_640 = relay.Function([], output)
mutated_mod['func_640'] = func_640
mutated_mod = relay.transform.InferType()(mutated_mod)
var_671 = relay.var("var_671", dtype = "int8", shape = (16, 8, 6))#candidate|671|(16, 8, 6)|var|int8
const_672 = relay.const([[[7,-2,5,3,-3,4],[4,-4,8,-10,10,3],[5,-2,2,-8,7,-8],[-5,-2,3,-2,5,6],[7,-4,2,-5,-3,-4],[9,6,4,-10,-6,-7],[-10,5,-5,7,-7,-9],[2,-7,-2,-2,3,-9]],[[-3,-7,-3,7,3,7],[5,4,-8,-2,-8,5],[-10,-3,4,-1,2,3],[2,9,4,-7,-3,-2],[3,-9,-2,5,1,8],[-1,-2,9,-10,-7,-8],[6,-9,-8,10,-4,-4],[-5,-10,-6,-2,9,10]],[[9,-1,-1,-9,-6,-8],[9,6,8,2,1,-10],[2,4,7,-1,5,5],[3,-3,-10,3,-10,5],[-3,1,-8,-10,4,4],[-7,-8,-9,8,-4,-8],[3,-6,-2,-9,7,-8],[-1,-7,-10,6,8,-2]],[[4,-8,3,5,-9,7],[3,8,-7,8,5,-5],[-8,4,5,-4,8,-7],[8,-6,-6,-10,-2,10],[-5,1,4,4,-9,2],[6,10,8,6,-1,6],[-7,6,-5,9,7,-9],[-8,-4,3,8,2,5]],[[9,-9,-4,-10,1,10],[-4,-7,1,-1,1,5],[-3,-3,-4,6,-10,4],[10,-4,-9,7,5,4],[8,-6,-3,2,5,1],[-8,3,-2,3,-2,-2],[-3,-6,-1,-6,-10,-9],[-3,-8,-10,8,-8,5]],[[9,-3,-7,3,4,-10],[-2,5,9,4,8,-10],[1,-6,10,-8,-1,9],[-3,-8,10,3,4,-3],[-3,7,-8,-2,7,-5],[-9,-4,-3,-8,5,-5],[-4,8,-8,5,7,5],[-8,-4,2,10,4,4]],[[8,8,-8,8,-3,3],[7,-3,7,10,2,10],[5,7,-5,7,-3,-7],[-9,-4,-3,-2,-3,7],[-10,5,2,7,-7,-5],[7,8,-8,-4,1,-9],[-5,5,5,-9,-10,8],[2,-7,4,-1,-7,-3]],[[-3,-2,-5,9,2,-9],[7,-4,2,8,1,-3],[1,-6,-1,3,-5,10],[-8,1,4,-10,8,9],[8,-6,-5,2,2,-4],[6,-9,-4,3,8,5],[6,3,9,-5,-1,6],[1,4,7,-8,-7,3]],[[8,7,-2,7,8,-1],[4,-4,1,3,-9,7],[6,8,-4,7,1,-5],[-6,2,-4,1,-10,-3],[6,-3,4,2,5,3],[4,-9,-6,7,-9,-6],[-1,3,1,-2,-3,-5],[-5,6,8,7,-9,-7]],[[5,7,-5,8,-9,9],[8,-10,-8,-9,1,-1],[5,2,-6,-1,7,6],[-2,-9,-5,2,2,6],[6,-1,9,9,-1,9],[2,-10,-9,-8,-1,1],[-7,-9,6,7,1,2],[-1,3,10,1,4,-10]],[[10,-2,-6,6,8,10],[-1,6,6,-1,9,-9],[7,-2,3,-4,9,-3],[10,8,-5,2,7,9],[5,10,-5,2,1,5],[-5,7,6,9,-9,4],[7,-1,3,8,9,4],[9,8,-10,-3,3,-9]],[[2,-6,6,5,7,8],[8,-10,7,1,-9,-5],[-3,4,-10,8,10,3],[6,-9,-5,-5,-4,10],[-8,-7,-1,8,1,-3],[-6,3,4,1,-5,3],[9,5,-4,7,7,10],[6,-3,9,-8,-4,2]],[[8,-10,-6,-2,-2,10],[-1,7,-9,-5,3,2],[3,-9,-2,7,-6,10],[9,-7,-1,4,-2,-2],[-5,7,-5,4,-10,5],[5,1,-8,-1,5,7],[-3,-9,-3,7,8,-8],[3,-10,-6,-5,10,10]],[[7,4,-1,9,3,10],[-1,-6,9,1,-7,-4],[-10,3,5,8,9,5],[5,4,5,6,9,4],[-7,1,-10,8,-8,-9],[-8,-6,-9,5,-6,-3],[-2,-7,-2,-10,-8,4],[10,7,5,-2,3,10]],[[-8,5,5,-6,-1,-10],[6,4,3,-1,2,-2],[5,1,-1,-9,7,4],[4,-1,-5,-7,-10,-4],[-1,-7,-6,-1,2,-9],[7,1,-2,8,-7,10],[-7,-2,8,-10,-4,3],[8,10,-7,3,7,-8]],[[9,4,2,-7,-10,7],[-6,8,-4,9,-2,1],[8,-3,-8,-1,-4,2],[-8,8,9,-6,10,4],[-3,-7,-1,-6,4,1],[10,-8,6,2,-10,-2],[4,3,-3,2,-9,-3],[-1,7,-10,-7,2,-5]]], dtype = "int8")#candidate|672|(16, 8, 6)|const|int8
bop_673 = relay.logical_xor(var_671.astype('int8'), relay.reshape(const_672.astype('int8'), relay.shape_of(var_671))) # shape=(16, 8, 6)
output = bop_673
output2 = bop_673
func_686 = relay.Function([var_671,], output)
mod['func_686'] = func_686
mod = relay.transform.InferType()(mod)
var_687 = relay.var("var_687", dtype = "int8", shape = (16, 8, 6))#candidate|687|(16, 8, 6)|var|int8
output = func_686(var_687)
func_688 = relay.Function([var_687], output)
mutated_mod['func_688'] = func_688
mutated_mod = relay.transform.InferType()(mutated_mod)
func_609_call = mod.get_global_var('func_609')
func_611_call = mutated_mod.get_global_var('func_611')
call_708 = relay.TupleGetItem(func_609_call(), 1)
call_709 = relay.TupleGetItem(func_611_call(), 1)
uop_717 = relay.cosh(call_708.astype('float64')) # shape=(3, 8, 9)
uop_719 = relay.cosh(call_709.astype('float64')) # shape=(3, 8, 9)
func_686_call = mod.get_global_var('func_686')
func_688_call = mutated_mod.get_global_var('func_688')
var_731 = relay.var("var_731", dtype = "int8", shape = (16, 48))#candidate|731|(16, 48)|var|int8
call_730 = func_686_call(relay.reshape(var_731.astype('int8'), [16, 8, 6]))
call_732 = func_686_call(relay.reshape(var_731.astype('int8'), [16, 8, 6]))
func_255_call = mod.get_global_var('func_255')
func_257_call = mutated_mod.get_global_var('func_257')
call_735 = func_255_call()
call_736 = func_255_call()
uop_738 = relay.tan(uop_717.astype('float64')) # shape=(3, 8, 9)
uop_740 = relay.tan(uop_719.astype('float64')) # shape=(3, 8, 9)
func_609_call = mod.get_global_var('func_609')
func_611_call = mutated_mod.get_global_var('func_611')
call_754 = relay.TupleGetItem(func_609_call(), 0)
call_755 = relay.TupleGetItem(func_611_call(), 0)
func_638_call = mod.get_global_var('func_638')
func_640_call = mutated_mod.get_global_var('func_640')
call_760 = func_638_call()
call_761 = func_638_call()
bop_766 = relay.not_equal(uop_738.astype('bool'), relay.reshape(call_754.astype('bool'), relay.shape_of(uop_738))) # shape=(3, 8, 9)
bop_769 = relay.not_equal(uop_740.astype('bool'), relay.reshape(call_755.astype('bool'), relay.shape_of(uop_740))) # shape=(3, 8, 9)
func_332_call = mod.get_global_var('func_332')
func_333_call = mutated_mod.get_global_var('func_333')
call_770 = func_332_call()
call_771 = func_332_call()
uop_774 = relay.rsqrt(uop_738.astype('float64')) # shape=(3, 8, 9)
uop_776 = relay.rsqrt(uop_740.astype('float64')) # shape=(3, 8, 9)
output = relay.Tuple([call_730,var_731,call_735,call_760,bop_766,call_770,uop_774,])
output2 = relay.Tuple([call_732,var_731,call_736,call_761,bop_769,call_771,uop_776,])
func_779 = relay.Function([var_731,], output)
mod['func_779'] = func_779
mod = relay.transform.InferType()(mod)
mutated_mod['func_779'] = func_779
mutated_mod = relay.transform.InferType()(mutated_mod)
var_780 = relay.var("var_780", dtype = "int8", shape = (16, 48))#candidate|780|(16, 48)|var|int8
func_779_call = mutated_mod.get_global_var('func_779')
call_781 = func_779_call(var_780)
output = call_781
func_782 = relay.Function([var_780], output)
mutated_mod['func_782'] = func_782
mutated_mod = relay.transform.InferType()(mutated_mod)
var_791 = relay.var("var_791", dtype = "uint16", shape = (1, 5, 16))#candidate|791|(1, 5, 16)|var|uint16
var_792 = relay.var("var_792", dtype = "uint16", shape = (6, 5, 16))#candidate|792|(6, 5, 16)|var|uint16
bop_793 = relay.subtract(var_791.astype('uint16'), var_792.astype('uint16')) # shape=(6, 5, 16)
bop_796 = relay.left_shift(bop_793.astype('uint64'), var_791.astype('uint64')) # shape=(6, 5, 16)
output = bop_796
output2 = bop_796
func_799 = relay.Function([var_791,var_792,], output)
mod['func_799'] = func_799
mod = relay.transform.InferType()(mod)
mutated_mod['func_799'] = func_799
mutated_mod = relay.transform.InferType()(mutated_mod)
func_799_call = mutated_mod.get_global_var('func_799')
var_801 = relay.var("var_801", dtype = "uint16", shape = (1, 5, 16))#candidate|801|(1, 5, 16)|var|uint16
var_802 = relay.var("var_802", dtype = "uint16", shape = (6, 5, 16))#candidate|802|(6, 5, 16)|var|uint16
call_800 = func_799_call(var_801,var_802,)
output = call_800
func_803 = relay.Function([var_801,var_802,], output)
mutated_mod['func_803'] = func_803
mutated_mod = relay.transform.InferType()(mutated_mod)
var_811 = relay.var("var_811", dtype = "float64", shape = (3, 13, 1))#candidate|811|(3, 13, 1)|var|float64
uop_812 = relay.asinh(var_811.astype('float64')) # shape=(3, 13, 1)
func_686_call = mod.get_global_var('func_686')
func_688_call = mutated_mod.get_global_var('func_688')
const_817 = relay.const([[-10,7,-8,8,8,-1,-1,-7,2,-9,8,5,-5,6,-10,5,9,10,5,-1,7,-6,-9,-3,4,10,-3,7,-5,1,3,-5,-7,4,-3,7,-6,-8,-7,-6,4,-10,-2,6,-1,-3,4,9,-5,5,7,-7,2,-8,10,-9,-1,-3,7,-10,-10,-3,5,8,-8,-7,3,-9,-3,6,-2,-8,-4,-6,2,-9,1,7,-7,-5,7,9,-7,-7,-5,2,7,-10,10,-4,-4,-7,5,10,-8,-7,8,-5,4,3,-4,-9,-6,-4,5,-1,8,-5,-1,-9,1,-5,3,3,-1,-9,3,8,4,-8,-7,-1,8,-2,-10,-9,6,-1,-4,-4,-3,2,10,-9,-9,5,-7,-4,2,-3,4,7,-6,7,-5,4,6,5,-3,2,1,-1,6,5,-9,2,2,3,8,-5,3,-10,-5,-6,-1,-4,6,3,1,9,6,-3,-9,-6,8,-9,-3,3,5,-8,-8,9,8,-5,1,8,3,6,10,10,-3,3,7,-6,5,-7,6,6,-9,4,-5,7,-6,4,7,5,1,8,6,-8,-7,4,4,-9,1,3,6,7,-5,7,3,1,-2,1,2,8,8,-5,2,-3,9,-2,-8,-6,-8,-4,-9,-6,-4,10,8,-7,10,7,6,-8,8,2,8,10,3,8,8,4,9,-2,-9,-3,1,-4,10,3,-1,5,-3,7,8,1,-7,2,6,-5,2,-8,8,9,-4,-7,9,4,8,9,7,3,-4,2,-8,-7,-6,3,-6,3,7,5,-3,-8,-2,-4,9,-3,-2,-5,5,-1,6,5,8,-2,-8,-3,-7,10,9,8,-1,3,9,4,-9,-3,10,-6,5,-5,4,2,10,1,-5,-9,2,-2,9,3,4,2,-5,4,6,-1,-9,2,-4,-9,3,-9,-10,-6,-8,9,-8,-6,7,10,-1,-6,5,-10,-2,-2,-8,10,2,1,8,4,8,6,3,-1,-9,5,-4,5,-7,-10,7,-5,7,-3,-3,-10,8,-8,-4,-5,5,-10,-8,-6,-3,-10,-8,1,2,-2,-10,7,8,9,4,6,-6,2,-3,-9,-5,-5,5,-10,-10,1,7,-10,-5,9,-4,1,-3,-6,-1,1,5,1,-3,-6,-7,3,-6,7,3,-1,2,9,-6,10,-9,3,6,-3,-9,2,-7,-8,-9,2,-2,8,-6,-9,-1,8,-9,-5,9,6,8,-3,-6,-6,9,-6,3,-7,3,9,-5,8,-10,-3,-3,-8,-10,4,4,-2,9,6,-3,9,8,-2,5,-1,2,-5,-6,6,3,-1,-9,10,10,-10,-10,1,-6,-3,2,5,9,-1,-2,10,-6,-10,3,-4,7,-5,2,-5,8,9,-3,8,-6,-8,5,-2,8,-5,-4,-3,3,-8,-4,3,-2,-4,9,-8,10,-3,-3,-5,9,-3,8,-5,-3,-4,-5,-1,-9,1,-8,5,6,-4,-5,1,8,8,-9,-5,-4,-1,7,-8,-6,6,-10,3,-3,7,5,-1,-6,-9,9,-9,-4,-6,10,-9,2,2,8,-2,-10,8,-8,8,-9,-9,10,3,-8,-7,2,-7,-1,8,4,-2,-8,-2,1,-2,-7,-9,1,-3,3,-9,5,-9,5,-10,7,5,-4,4,5,6,-9,10,-8,-10,4,6,-7,8,2,1,9,7,-3,9,-8,-1,-1,-8,-6,2,10,-9,-4,-9,4,8,-7,9,7,-7,4,-4,1,-5,-2,8,8,-9,6,-9,-1,8,-5,8,-4,8,7,4,-4,6,8,10,-3,8,-8,-4,7,6,6,3,1,9,-3,-7,-1,-7,-8,7,-3,-3,-4,-9,-6,3,9,3,7,-7,2,-1,6,4,-2,-5,7,-7,6,2,-9,5,10,7,7,-10,-9,-4,7,-10,2,-6,-5,10,9,3,-4,5,6,1,-9,4,2,-2,9,-9,-7,-8,8,-6,-7,-6,-7,6,4,-5,-8,10,9,10,5,-7,-6,7,-2,-2,1,-3,-8,10,-6,-6,5,8,-9,-4,-8,9,5,-10,10,-9,8,9]], dtype = "int8")#candidate|817|(1, 768)|const|int8
call_816 = func_686_call(relay.reshape(const_817.astype('int8'), [16, 8, 6]))
call_818 = func_686_call(relay.reshape(const_817.astype('int8'), [16, 8, 6]))
bop_821 = relay.multiply(uop_812.astype('int8'), const_817.astype('int8')) # shape=(3, 13, 768)
bop_826 = relay.logical_and(const_817.astype('bool'), bop_821.astype('bool')) # shape=(3, 13, 768)
func_255_call = mod.get_global_var('func_255')
func_257_call = mutated_mod.get_global_var('func_257')
call_830 = func_255_call()
call_831 = func_255_call()
output = relay.Tuple([call_816,bop_826,call_830,])
output2 = relay.Tuple([call_818,bop_826,call_831,])
func_833 = relay.Function([var_811,], output)
mod['func_833'] = func_833
mod = relay.transform.InferType()(mod)
mutated_mod['func_833'] = func_833
mutated_mod = relay.transform.InferType()(mutated_mod)
var_834 = relay.var("var_834", dtype = "float64", shape = (3, 13, 1))#candidate|834|(3, 13, 1)|var|float64
func_833_call = mutated_mod.get_global_var('func_833')
call_835 = func_833_call(var_834)
output = call_835
func_836 = relay.Function([var_834], output)
mutated_mod['func_836'] = func_836
mutated_mod = relay.transform.InferType()(mutated_mod)
func_507_call = mod.get_global_var('func_507')
func_508_call = mutated_mod.get_global_var('func_508')
call_876 = func_507_call()
call_877 = func_507_call()
func_609_call = mod.get_global_var('func_609')
func_611_call = mutated_mod.get_global_var('func_611')
call_897 = relay.TupleGetItem(func_609_call(), 0)
call_898 = relay.TupleGetItem(func_611_call(), 0)
uop_900 = relay.sinh(call_897.astype('float32')) # shape=(3, 8, 9)
uop_902 = relay.sinh(call_898.astype('float32')) # shape=(3, 8, 9)
func_638_call = mod.get_global_var('func_638')
func_640_call = mutated_mod.get_global_var('func_640')
call_903 = func_638_call()
call_904 = func_638_call()
output = relay.Tuple([call_876,uop_900,call_903,])
output2 = relay.Tuple([call_877,uop_902,call_904,])
func_916 = relay.Function([], output)
mod['func_916'] = func_916
mod = relay.transform.InferType()(mod)
mutated_mod['func_916'] = func_916
mutated_mod = relay.transform.InferType()(mutated_mod)
func_916_call = mutated_mod.get_global_var('func_916')
call_917 = func_916_call()
output = call_917
func_918 = relay.Function([], output)
mutated_mod['func_918'] = func_918
mutated_mod = relay.transform.InferType()(mutated_mod)
const_921 = relay.const(-2, dtype = "uint64")#candidate|921|()|const|uint64
const_922 = relay.const([[[4,5,4,-3,-6,-1,2,-8,-2,4],[1,-9,-7,5,8,3,9,-1,-3,-5]]], dtype = "uint64")#candidate|922|(1, 2, 10)|const|uint64
bop_923 = relay.bitwise_or(const_921.astype('uint64'), const_922.astype('uint64')) # shape=(1, 2, 10)
bop_943 = relay.multiply(const_921.astype('float32'), const_922.astype('float32')) # shape=(1, 2, 10)
bop_946 = relay.less(const_922.astype('bool'), const_921.astype('bool')) # shape=(1, 2, 10)
output = relay.Tuple([bop_923,bop_943,bop_946,])
output2 = relay.Tuple([bop_923,bop_943,bop_946,])
func_949 = relay.Function([], output)
mod['func_949'] = func_949
mod = relay.transform.InferType()(mod)
mutated_mod['func_949'] = func_949
mutated_mod = relay.transform.InferType()(mutated_mod)
func_949_call = mutated_mod.get_global_var('func_949')
call_950 = func_949_call()
output = call_950
func_951 = relay.Function([], output)
mutated_mod['func_951'] = func_951
mutated_mod = relay.transform.InferType()(mutated_mod)
func_638_call = mod.get_global_var('func_638')
func_640_call = mutated_mod.get_global_var('func_640')
call_974 = func_638_call()
call_975 = func_638_call()
func_686_call = mod.get_global_var('func_686')
func_688_call = mutated_mod.get_global_var('func_688')
const_980 = relay.const([9,8,8,3,8,-5,-7,-10,6,5,6,-8,-2,1,-5,9,-8,2,-4,9,6,-5,-8,-10,-8,-10,9,-5,-1,2,-1,-1,-7,-4,-8,10,-8,9,-3,2,-3,8,-10,-2,9,8,6,-8,2,3,6,4,-10,2,1,7,-6,-4,7,-9,2,6,-9,-1,8,-1,-7,8,7,1,4,1,-10,-8,3,-1,7,4,-4,8,-9,8,-3,3,6,9,-9,-2,5,8,-7,6,-8,3,5,6,8,2,-10,-3,-9,8,3,1,-10,-6,7,5,2,7,-9,3,-7,-1,2,-3,6,-2,-3,-7,-9,-2,-6,-2,-6,8,-4,-3,8,5,-7,2,4,-4,-5,10,3,4,10,8,7,-1,6,1,9,-3,-6,2,9,7,-5,1,10,9,-1,7,-4,-8,-4,6,5,-10,6,-3,7,8,6,2,-3,7,10,2,4,-4,-9,10,2,6,-1,1,-8,2,10,-1,4,9,-4,8,10,-4,4,4,-5,2,-9,6,3,3,-1,-6,-2,1,-5,2,2,-8,-10,-10,5,3,-4,1,-6,-1,-9,-3,2,-7,-2,-6,-6,9,-9,3,1,-7,-2,2,-5,4,-10,4,-1,-2,-1,7,5,3,7,7,9,-2,-2,-8,9,-10,-9,2,-5,-2,7,4,-7,7,1,9,7,1,-8,-8,-3,6,3,3,-4,-6,6,2,-7,5,-4,7,8,3,-9,10,9,5,4,4,4,-1,-2,-4,-4,6,-5,-7,9,8,-1,9,4,6,3,-8,-1,-9,-1,-1,-4,-1,10,-4,10,-6,-10,-4,10,-4,7,-1,-10,1,-3,-8,-1,-10,9,-9,-7,3,-1,-4,5,5,-10,2,5,3,8,-9,-10,-8,-6,-9,2,-10,9,6,-4,7,7,3,-3,-2,-8,9,-3,-9,6,1,2,-2,7,-4,-9,4,10,-8,6,5,-4,-5,3,-3,2,6,-7,-4,8,-5,8,-3,-9,-1,-2,10,-1,2,-9,-5,-10,6,1,10,-5,-6,-6,-1,-9,-9,-9,8,6,-5,4,-7,-3,10,10,-1,8,-9,-6,7,-3,10,-7,-3,6,-7,10,-5,-6,6,8,2,7,-8,2,-10,-4,-6,-9,-4,-8,7,7,-10,-10,9,-6,-4,10,5,9,-6,8,-4,2,-3,-10,-8,-6,-8,-7,-4,7,3,10,-1,5,-2,9,1,-3,-2,7,-10,10,-9,6,-9,1,-10,2,-2,9,10,-9,1,-5,6,3,-5,5,-2,-7,-4,3,-9,-5,3,-4,-4,-6,-4,-10,-3,6,7,-3,-2,10,-9,10,-9,1,-1,-7,-10,1,-3,4,-3,-5,-2,9,-9,10,3,9,4,-6,-7,-1,-3,10,-3,-4,-7,-7,7,6,9,7,-5,6,8,-6,4,-1,8,-4,10,-7,5,7,-4,-10,-9,2,3,3,9,-6,5,-9,1,-5,-9,7,8,8,8,-4,-6,3,4,3,-5,6,8,-6,1,9,6,6,3,6,3,-10,-6,-8,-9,6,10,6,9,9,3,-10,6,-3,-9,4,-8,-10,-9,7,-9,-4,6,9,3,-7,-5,-7,4,-2,8,-4,-2,3,3,9,-2,1,4,5,-5,4,-1,3,-1,-8,-2,-7,5,4,-9,-9,8,3,9,9,-2,6,-4,-9,-3,-3,-9,7,-10,3,-8,4,-4,7,-5,-7,-7,-2,-1,5,-10,-7,9,-7,9,-10,-4,-2,-1,2,-3,-3,-4,-3,-8,9,9,8,-1,6,-7,-8,3,9,-7,10,-2,4,9,-10,-8,-6,-4,4,1,9,10,-9,5,7,-1,-6,3,10,9,-1,-9,-5,-3,-2,1,-2,-1,4,-1,10,9,8,7,-5,7,3,-5,3,-7,4,-10,-9,-7,7,-5,3,-4,-7,8,7,-10,-3,9,2,-5,-8,-3,4,-1,2,-7,-1,4,1,-1,-7,-9,5,10,-7,-4,-10,1,8,4,-9,5,-3,7,-10,2,-9,-2,10,2,7,-2,4,10,5,-4,-8,-4,7,-6], dtype = "int8")#candidate|980|(768,)|const|int8
call_979 = func_686_call(relay.reshape(const_980.astype('int8'), [16, 8, 6]))
call_981 = func_686_call(relay.reshape(const_980.astype('int8'), [16, 8, 6]))
output = relay.Tuple([call_974,call_979,const_980,])
output2 = relay.Tuple([call_975,call_981,const_980,])
func_989 = relay.Function([], output)
mod['func_989'] = func_989
mod = relay.transform.InferType()(mod)
mutated_mod['func_989'] = func_989
mutated_mod = relay.transform.InferType()(mutated_mod)
func_989_call = mutated_mod.get_global_var('func_989')
call_990 = func_989_call()
output = call_990
func_991 = relay.Function([], output)
mutated_mod['func_991'] = func_991
mutated_mod = relay.transform.InferType()(mutated_mod)
func_255_call = mod.get_global_var('func_255')
func_257_call = mutated_mod.get_global_var('func_257')
call_992 = func_255_call()
call_993 = func_255_call()
output = call_992
output2 = call_993
func_1002 = relay.Function([], output)
mod['func_1002'] = func_1002
mod = relay.transform.InferType()(mod)
mutated_mod['func_1002'] = func_1002
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1002_call = mutated_mod.get_global_var('func_1002')
call_1003 = func_1002_call()
output = call_1003
func_1004 = relay.Function([], output)
mutated_mod['func_1004'] = func_1004
mutated_mod = relay.transform.InferType()(mutated_mod)
func_916_call = mod.get_global_var('func_916')
func_918_call = mutated_mod.get_global_var('func_918')
call_1011 = relay.TupleGetItem(func_916_call(), 2)
call_1012 = relay.TupleGetItem(func_918_call(), 2)
output = call_1011
output2 = call_1012
func_1013 = relay.Function([], output)
mod['func_1013'] = func_1013
mod = relay.transform.InferType()(mod)
output = func_1013()
func_1014 = relay.Function([], output)
mutated_mod['func_1014'] = func_1014
mutated_mod = relay.transform.InferType()(mutated_mod)
func_255_call = mod.get_global_var('func_255')
func_257_call = mutated_mod.get_global_var('func_257')
call_1063 = func_255_call()
call_1064 = func_255_call()
func_638_call = mod.get_global_var('func_638')
func_640_call = mutated_mod.get_global_var('func_640')
call_1069 = func_638_call()
call_1070 = func_638_call()
func_543_call = mod.get_global_var('func_543')
func_544_call = mutated_mod.get_global_var('func_544')
call_1081 = relay.TupleGetItem(func_543_call(), 0)
call_1082 = relay.TupleGetItem(func_544_call(), 0)
func_609_call = mod.get_global_var('func_609')
func_611_call = mutated_mod.get_global_var('func_611')
call_1083 = relay.TupleGetItem(func_609_call(), 0)
call_1084 = relay.TupleGetItem(func_611_call(), 0)
func_543_call = mod.get_global_var('func_543')
func_544_call = mutated_mod.get_global_var('func_544')
call_1085 = relay.TupleGetItem(func_543_call(), 0)
call_1086 = relay.TupleGetItem(func_544_call(), 0)
output = relay.Tuple([call_1063,call_1069,call_1081,call_1083,call_1085,])
output2 = relay.Tuple([call_1064,call_1070,call_1082,call_1084,call_1086,])
func_1091 = relay.Function([], output)
mod['func_1091'] = func_1091
mod = relay.transform.InferType()(mod)
mutated_mod['func_1091'] = func_1091
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1091_call = mutated_mod.get_global_var('func_1091')
call_1092 = func_1091_call()
output = call_1092
func_1093 = relay.Function([], output)
mutated_mod['func_1093'] = func_1093
mutated_mod = relay.transform.InferType()(mutated_mod)
func_543_call = mod.get_global_var('func_543')
func_544_call = mutated_mod.get_global_var('func_544')
call_1118 = relay.TupleGetItem(func_543_call(), 1)
call_1119 = relay.TupleGetItem(func_544_call(), 1)
uop_1122 = relay.asinh(call_1118.astype('float64')) # shape=(3, 8, 9)
uop_1124 = relay.asinh(call_1119.astype('float64')) # shape=(3, 8, 9)
bop_1136 = relay.divide(uop_1122.astype('float64'), relay.reshape(call_1118.astype('float64'), relay.shape_of(uop_1122))) # shape=(3, 8, 9)
bop_1139 = relay.divide(uop_1124.astype('float64'), relay.reshape(call_1119.astype('float64'), relay.shape_of(uop_1124))) # shape=(3, 8, 9)
output = bop_1136
output2 = bop_1139
func_1186 = relay.Function([], output)
mod['func_1186'] = func_1186
mod = relay.transform.InferType()(mod)
output = func_1186()
func_1187 = relay.Function([], output)
mutated_mod['func_1187'] = func_1187
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1013_call = mod.get_global_var('func_1013')
func_1014_call = mutated_mod.get_global_var('func_1014')
call_1188 = func_1013_call()
call_1189 = func_1013_call()
output = relay.Tuple([call_1188,])
output2 = relay.Tuple([call_1189,])
func_1192 = relay.Function([], output)
mod['func_1192'] = func_1192
mod = relay.transform.InferType()(mod)
output = func_1192()
func_1193 = relay.Function([], output)
mutated_mod['func_1193'] = func_1193
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1091_call = mod.get_global_var('func_1091')
func_1093_call = mutated_mod.get_global_var('func_1093')
call_1199 = relay.TupleGetItem(func_1091_call(), 4)
call_1200 = relay.TupleGetItem(func_1093_call(), 4)
func_799_call = mod.get_global_var('func_799')
func_803_call = mutated_mod.get_global_var('func_803')
const_1202 = relay.const([[-2],[-4],[-1],[-8],[8],[2],[-10],[-4],[-6],[7],[3],[-3],[2],[-2],[3],[-3],[10],[3],[4],[6],[9],[-2],[5],[-1],[2],[-4],[-9],[-9],[-2],[-1],[-6],[1],[-2],[7],[-6],[-8],[3],[3],[-3],[-2],[2],[9],[3],[-10],[8],[2],[-8],[1],[-5],[-5],[-3],[5],[-10],[-7],[-5],[-7],[5],[8],[-3],[-2],[2],[8],[5],[1],[8],[-5],[1],[-1],[10],[-6],[-7],[2],[1],[9],[-10],[7],[-5],[3],[4],[1]], dtype = "uint16")#candidate|1202|(80, 1)|const|uint16
var_1203 = relay.var("var_1203", dtype = "uint16", shape = (480,))#candidate|1203|(480,)|var|uint16
call_1201 = func_799_call(relay.reshape(const_1202.astype('uint16'), [1, 5, 16]), relay.reshape(var_1203.astype('uint16'), [6, 5, 16]), )
call_1204 = func_799_call(relay.reshape(const_1202.astype('uint16'), [1, 5, 16]), relay.reshape(var_1203.astype('uint16'), [6, 5, 16]), )
var_1209 = relay.var("var_1209", dtype = "uint64", shape = (6, 5, 16))#candidate|1209|(6, 5, 16)|var|uint64
bop_1210 = relay.power(call_1201.astype('float32'), relay.reshape(var_1209.astype('float32'), relay.shape_of(call_1201))) # shape=(6, 5, 16)
bop_1213 = relay.power(call_1204.astype('float32'), relay.reshape(var_1209.astype('float32'), relay.shape_of(call_1204))) # shape=(6, 5, 16)
uop_1215 = relay.cosh(var_1209.astype('float32')) # shape=(6, 5, 16)
func_686_call = mod.get_global_var('func_686')
func_688_call = mutated_mod.get_global_var('func_688')
const_1226 = relay.const([2,-10,-7,8,-5,-2,-7,-2,-2,10,1,10,-1,3,-2,8,8,-4,-1,8,7,7,-6,8,5,-9,9,2,2,7,-10,9,-7,4,5,-5,3,-8,-3,8,-8,2,-8,9,-2,5,3,9,-7,7,-6,-6,-6,-9,-5,-7,-5,2,7,-7,-10,-10,-8,-5,3,-9,-8,-9,1,3,6,9,-3,7,4,7,-8,-1,10,-1,9,2,-5,4,-9,-4,-9,8,-5,9,1,-5,7,-3,-1,-7,-6,-10,2,-9,-10,-7,5,10,10,-9,-9,8,-10,10,9,4,10,6,-9,-2,9,10,5,-4,-1,-6,7,6,-8,1,-6,3,-10,-8,6,-9,-9,1,-9,1,-9,-2,-2,6,-5,-7,9,-8,9,-7,6,-1,5,1,6,7,8,4,8,-9,-4,-7,-6,-3,1,-9,-7,1,10,-7,-1,-4,4,8,5,-8,-4,3,9,5,7,4,4,-6,-5,-3,-5,-7,2,-2,5,-7,4,10,-5,1,9,-7,-3,7,6,-6,6,2,1,6,-4,6,10,-1,-1,8,10,-2,10,2,-1,9,-4,-5,6,2,4,-10,-3,1,3,-3,7,-7,7,3,10,5,-4,8,4,4,7,2,4,4,-5,2,4,-8,-1,-1,4,4,10,2,3,4,7,-9,-1,10,-4,7,4,-1,8,-5,-9,4,2,-5,-9,6,-7,9,-2,4,-3,-3,10,-1,7,-3,-6,8,-3,6,4,-2,-9,-8,1,-4,-5,-9,-1,5,8,-6,5,6,-9,-1,-4,-5,-3,-3,-7,7,4,-8,10,-4,-9,5,-6,-3,-5,1,5,-2,9,3,2,9,-7,2,-8,6,-1,-3,-5,-6,-1,10,3,4,-7,9,6,7,4,-1,-10,-2,-1,9,-3,4,10,-10,8,-6,-1,-6,2,10,-7,-8,1,9,5,8,1,-2,8,5,-3,2,-7,-1,-6,-4,-4,-1,4,-9,-7,7,-10,10,-10,-5,9,7,8,6,-10,8,-5,-1,8,-8,-6,5,-3,-6,-4,-7,10,9,-1,1,-5,5,7,-9,-5,-2,-1,1,-1,-8,-9,8,-9,7,-1,-9,-9,-6,-2,3,-1,10,-1,-5,-7,-7,-8,-6,-3,-6,3,-1,-2,1,4,-1,9,7,10,2,7,-4,6,1,-4,2,-2,2,-3,-6,-6,-4,-8,-5,-2,-8,8,-1,3,-2,9,-6,10,-5,-10,-2,7,5,4,6,9,-5,7,9,-10,-8,-6,9,2,-1,-4,3,6,9,-8,-7,10,-3,-8,8,5,8,-2,-7,1,-1,10,10,-1,-7,-5,-7,-4,3,-3,1,-9,-9,-6,-7,6,-5,1,-2,4,5,-2,6,3,10,-2,-5,-2,4,-3,-8,-1,5,6,-6,5,-10,4,-4,5,6,-7,-10,7,10,9,9,8,-3,9,5,-3,-2,-10,5,-10,-5,-3,-7,-1,10,-4,-1,3,7,3,8,8,4,-6,-3,1,-3,-5,5,-7,7,4,-6,-1,-2,4,2,-2,9,-5,-2,2,-1,8,-4,-8,8,8,2,-6,6,6,3,-6,6,7,-8,-5,-6,2,10,9,-6,4,8,2,-10,-6,6,5,1,-2,-1,-7,-2,4,-3,-1,-4,6,-5,-8,9,-9,-5,-7,-8,-7,-5,-5,7,10,4,8,-6,-2,5,5,-5,8,-9,-6,5,-6,-10,-9,8,-7,-1,-2,1,6,-3,1,5,6,6,3,-7,-2,-7,2,-10,-2,5,-6,6,-2,4,7,-3,-7,6,8,6,10,3,-1,-2,4,6,4,3,-1,9,8,2,3,-5,3,3,5,7,8,10,9,-1,8,-8,3,-8,3,8,9,-7,5,8,-5,-9,-6,-5,2,7,4,-8,7,9,7,-4,-3,1,-10,-9,5,7,4,10,10,8,5,10,-4,-9,-10,-7,3,-10,-8,5,-8,7,-4,10,4,-5,-5,-10,6,8,-4,9,-3,-10,10,6,-10,2,2,8,-9,7,-10,3,-8,-3,5,10,3,-1,-5,-2], dtype = "int8")#candidate|1226|(768,)|const|int8
call_1225 = func_686_call(relay.reshape(const_1226.astype('int8'), [16, 8, 6]))
call_1227 = func_686_call(relay.reshape(const_1226.astype('int8'), [16, 8, 6]))
output = relay.Tuple([call_1199,const_1202,var_1203,bop_1210,uop_1215,call_1225,const_1226,])
output2 = relay.Tuple([call_1200,const_1202,var_1203,bop_1213,uop_1215,call_1227,const_1226,])
func_1234 = relay.Function([var_1203,var_1209,], output)
mod['func_1234'] = func_1234
mod = relay.transform.InferType()(mod)
var_1235 = relay.var("var_1235", dtype = "uint16", shape = (480,))#candidate|1235|(480,)|var|uint16
var_1236 = relay.var("var_1236", dtype = "uint64", shape = (6, 5, 16))#candidate|1236|(6, 5, 16)|var|uint64
output = func_1234(var_1235,var_1236,)
func_1237 = relay.Function([var_1235,var_1236,], output)
mutated_mod['func_1237'] = func_1237
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1322 = relay.var("var_1322", dtype = "int8", shape = (16, 14, 15))#candidate|1322|(16, 14, 15)|var|int8
var_1323 = relay.var("var_1323", dtype = "int8", shape = (16, 14, 15))#candidate|1323|(16, 14, 15)|var|int8
bop_1324 = relay.subtract(var_1322.astype('int8'), relay.reshape(var_1323.astype('int8'), relay.shape_of(var_1322))) # shape=(16, 14, 15)
bop_1331 = relay.divide(bop_1324.astype('float32'), relay.reshape(var_1322.astype('float32'), relay.shape_of(bop_1324))) # shape=(16, 14, 15)
uop_1343 = relay.log2(var_1322.astype('float32')) # shape=(16, 14, 15)
uop_1354 = relay.cos(bop_1331.astype('float32')) # shape=(16, 14, 15)
func_609_call = mod.get_global_var('func_609')
func_611_call = mutated_mod.get_global_var('func_611')
call_1358 = relay.TupleGetItem(func_609_call(), 0)
call_1359 = relay.TupleGetItem(func_611_call(), 0)
output = relay.Tuple([uop_1343,uop_1354,call_1358,])
output2 = relay.Tuple([uop_1343,uop_1354,call_1359,])
func_1361 = relay.Function([var_1322,var_1323,], output)
mod['func_1361'] = func_1361
mod = relay.transform.InferType()(mod)
mutated_mod['func_1361'] = func_1361
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1361_call = mutated_mod.get_global_var('func_1361')
var_1363 = relay.var("var_1363", dtype = "int8", shape = (16, 14, 15))#candidate|1363|(16, 14, 15)|var|int8
var_1364 = relay.var("var_1364", dtype = "int8", shape = (16, 14, 15))#candidate|1364|(16, 14, 15)|var|int8
call_1362 = func_1361_call(var_1363,var_1364,)
output = call_1362
func_1365 = relay.Function([var_1363,var_1364,], output)
mutated_mod['func_1365'] = func_1365
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1396 = relay.const([[[-3.356365,-9.197895,1.420750],[-1.749479,-5.727827,8.006628],[1.864203,-9.059639,0.847253],[0.430194,-7.709939,3.414024],[2.741987,-9.664576,-4.124584],[-0.853445,3.757011,6.769154],[5.118148,-1.708856,-9.308689],[-3.884706,-5.960405,-1.897264],[4.892294,-4.827126,8.858304],[-0.905785,7.716825,6.600825]],[[-7.697423,1.885858,-6.440258],[-1.872127,-5.252331,9.810983],[-5.726479,0.798287,-5.347612],[7.977156,3.860506,-7.680037],[1.819114,6.243938,6.594642],[-3.284264,-6.978559,1.041893],[4.115861,6.876380,7.934715],[-9.801184,-6.923965,-0.929274],[2.933535,-3.096409,8.755599],[1.273656,9.647414,3.494942]],[[1.628132,-8.351250,7.949333],[7.795922,6.486793,8.605071],[7.981872,5.846222,2.571794],[9.243963,3.583961,4.002465],[-8.545020,1.845225,3.800693],[-1.600931,5.044123,1.687587],[5.855230,9.374585,6.859337],[0.624575,-1.792345,-3.820250],[-3.295450,7.941213,6.480244],[-5.291512,4.794177,-0.278184]],[[-8.888948,-2.494360,2.807961],[8.915293,-9.395153,-4.971491],[8.662029,-4.826194,-3.221302],[4.091080,-2.439763,-2.117155],[6.340449,1.433654,-0.218261],[9.433873,8.421516,-6.387789],[8.004577,4.750763,-8.343323],[6.772112,5.450713,-9.723988],[-6.530613,-1.892848,-9.105230],[7.890453,0.435326,-9.297561]],[[-7.774447,-5.608129,4.111946],[-0.810277,-0.886619,-0.056168],[4.700307,-1.818904,-7.889791],[-9.785118,-9.926908,1.236382],[4.669344,-8.260295,-8.047380],[3.560578,6.777152,-6.541410],[-7.205781,7.024116,-0.928922],[-0.457278,-3.880145,-3.275912],[6.633134,8.733650,2.293328],[-4.351842,1.204242,3.216302]],[[3.004038,-4.723886,-9.127129],[-7.281693,-5.563454,-2.841653],[9.871907,-1.548088,9.827979],[-8.093406,-3.056985,6.310972],[9.232831,-6.497450,-7.468353],[-8.622762,-1.100703,-8.545657],[7.329983,-2.693801,2.322661],[-1.890492,8.442048,-8.542368],[6.650615,7.519518,-2.490698],[3.186282,-4.382827,7.711073]],[[4.534320,-1.230921,-1.904077],[-2.417917,0.007968,2.148728],[9.738531,-4.569339,2.536250],[-4.477904,2.620662,-6.013040],[-8.570904,1.825525,7.594227],[7.723485,-5.472141,0.123743],[1.348143,-9.458183,-1.633614],[7.920098,6.496275,-0.238841],[-2.892436,7.632639,-4.233911],[9.776145,3.456463,3.906925]],[[8.870331,5.347846,-5.510563],[1.467006,9.705793,0.218701],[9.509437,6.238444,-2.829729],[4.366206,-8.636726,-9.817482],[-3.220662,6.857982,3.282232],[0.984815,-2.421577,-3.089736],[4.143345,-2.600300,-2.487011],[-3.072506,-7.099592,-4.114115],[4.841739,5.992837,7.011093],[-1.461651,8.793559,3.334782]],[[-9.826318,-6.015307,-8.918575],[0.125263,-4.667806,-4.061090],[1.427693,-3.931667,-7.103405],[-3.397382,8.116732,-7.584763],[-1.163700,-4.521065,-5.281285],[-9.723634,-2.927475,5.074009],[0.411195,-4.868563,-2.000487],[-1.787609,4.456105,0.368315],[-0.912991,9.130269,2.686010],[-2.242510,-2.489373,-6.513550]],[[-8.611938,2.486642,0.738495],[4.129660,-1.186776,-9.363068],[-5.045197,-3.821346,8.902104],[-3.460613,-6.599427,1.366081],[7.861515,1.291284,4.673625],[-6.143037,-1.431989,-1.172985],[9.896158,-4.479416,-6.456748],[-1.122045,-7.309743,-2.959067],[4.268540,8.742131,5.905129],[3.143091,-0.586689,-2.433578]],[[-9.581112,8.349060,7.334907],[-5.671043,-1.896187,-2.208492],[6.492880,0.968792,0.505522],[-7.088151,-0.499860,-5.721205],[-0.867342,-3.165759,-7.051472],[-3.619377,-1.862940,2.731452],[-3.049349,-5.999463,6.720732],[0.052515,4.897920,-4.314734],[-9.154904,0.850792,-9.011725],[-6.726246,-7.875971,9.954253]]], dtype = "float64")#candidate|1396|(11, 10, 3)|const|float64
uop_1397 = relay.log2(const_1396.astype('float64')) # shape=(11, 10, 3)
func_949_call = mod.get_global_var('func_949')
func_951_call = mutated_mod.get_global_var('func_951')
call_1409 = relay.TupleGetItem(func_949_call(), 1)
call_1410 = relay.TupleGetItem(func_951_call(), 1)
uop_1416 = relay.cos(const_1396.astype('float64')) # shape=(11, 10, 3)
func_799_call = mod.get_global_var('func_799')
func_803_call = mutated_mod.get_global_var('func_803')
var_1436 = relay.var("var_1436", dtype = "uint16", shape = (80,))#candidate|1436|(80,)|var|uint16
const_1437 = relay.const([[-1,8,-6,-10,2,6,-3,9,-8,-9,3,-3,9,5,-3,6,1,7,8,6,-7,7,3,-2,-8,7,6,-2,-5,1,-9,-4,-3,-8,8,1,8,-7,-8,1,-9,9,-10,10,-1,-5,-10,-1,-10,1,6,-7,-10,7,-3,-3,-9,-10,5,-6,1,-7,10,1,10,2,-4,2,3,-3,10,-9,-10,9,8,-4,-5,-1,10,7,-6,7,7,-7,9,-7,7,9,6,7,-1,7,3,-5,10,2,-2,-5,8,-1,1,7,5,-7,4,-9,4,-3,3,-9,-1,-6,-10,1,-4,-7,10,3,10,8,-6,10,-2,7,2,-6,-9,-3,-7,8,-7,-4,-9,-4,-1,-2,9,4,-7,-5,-9,10,-7,-6,1,4,9,7,-9,6,1,-4,1,2,-3,7,-1,-7,-3,-1,-6,-2,-6,-2,8,-4,7,-9,-8,-8,-9,-2,-3,-9,1,-9,-6,2,8,7,-4,-4,1,-3,8,9,-6,10,-9,6,-8,8,3,-7,6,8,-7,2,8,8,-7,-3,-9,4,1,-9,-4,4,9,-10,-9,8,1,-5,-7,4,9,9,-10,5,3,-10,-3,4,-8,-10,3,5,7,-2,5,8,-3,2,-2,-5,-5,3,1,-1],[-4,-10,-6,-2,6,-7,9,-3,-2,6,-5,10,9,-7,3,-1,-6,5,-5,5,10,-10,-7,1,-1,-7,9,-8,3,1,3,4,-3,5,5,-1,2,-3,-6,2,1,-6,7,1,1,-5,-3,6,-7,6,-1,-6,-10,-5,3,-6,5,7,7,-1,9,3,-4,-10,1,4,4,-6,10,3,-9,10,-2,-5,4,-7,3,-6,10,7,-1,5,2,10,-5,5,-1,-7,1,-1,-1,9,10,-8,-1,-4,-7,-10,2,-10,4,-10,-10,7,2,-8,8,-4,5,1,-8,-10,5,3,1,-4,-9,-9,3,10,-6,6,-8,-4,-4,-10,-3,-9,-2,4,6,-8,2,3,5,-1,-2,7,-1,4,10,-10,-4,-9,-3,-10,3,-3,-9,-2,-10,7,4,-3,-9,-10,8,-9,-1,9,-3,3,8,3,-10,4,-10,3,7,8,-2,-2,-8,-5,1,-3,2,2,-9,9,-2,1,-4,-7,-2,-6,3,5,8,2,-3,-6,10,6,3,-3,10,10,-10,-6,3,-5,1,10,1,1,-9,-8,4,-10,-1,3,-7,-9,1,-7,9,-1,-5,2,-6,-7,-9,-4,1,10,-7,5,-8,-10,2,-3,3,-3,-6,-2,7,7,-6,-9]], dtype = "uint16")#candidate|1437|(2, 240)|const|uint16
call_1435 = func_799_call(relay.reshape(var_1436.astype('uint16'), [1, 5, 16]), relay.reshape(const_1437.astype('uint16'), [6, 5, 16]), )
call_1438 = func_799_call(relay.reshape(var_1436.astype('uint16'), [1, 5, 16]), relay.reshape(const_1437.astype('uint16'), [6, 5, 16]), )
func_543_call = mod.get_global_var('func_543')
func_544_call = mutated_mod.get_global_var('func_544')
call_1439 = relay.TupleGetItem(func_543_call(), 0)
call_1440 = relay.TupleGetItem(func_544_call(), 0)
bop_1442 = relay.multiply(uop_1416.astype('uint64'), relay.reshape(const_1396.astype('uint64'), relay.shape_of(uop_1416))) # shape=(11, 10, 3)
output = relay.Tuple([uop_1397,call_1409,call_1435,var_1436,const_1437,call_1439,bop_1442,])
output2 = relay.Tuple([uop_1397,call_1410,call_1438,var_1436,const_1437,call_1440,bop_1442,])
func_1451 = relay.Function([var_1436,], output)
mod['func_1451'] = func_1451
mod = relay.transform.InferType()(mod)
mutated_mod['func_1451'] = func_1451
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1452 = relay.var("var_1452", dtype = "uint16", shape = (80,))#candidate|1452|(80,)|var|uint16
func_1451_call = mutated_mod.get_global_var('func_1451')
call_1453 = func_1451_call(var_1452)
output = call_1453
func_1454 = relay.Function([var_1452], output)
mutated_mod['func_1454'] = func_1454
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1473 = relay.var("var_1473", dtype = "float64", shape = (15, 16, 3))#candidate|1473|(15, 16, 3)|var|float64
uop_1474 = relay.exp(var_1473.astype('float64')) # shape=(15, 16, 3)
uop_1484 = relay.cosh(var_1473.astype('float64')) # shape=(15, 16, 3)
func_577_call = mod.get_global_var('func_577')
func_580_call = mutated_mod.get_global_var('func_580')
var_1494 = relay.var("var_1494", dtype = "bool", shape = (216,))#candidate|1494|(216,)|var|bool
call_1493 = func_577_call(relay.reshape(var_1494.astype('bool'), [3, 8, 9]))
call_1495 = func_577_call(relay.reshape(var_1494.astype('bool'), [3, 8, 9]))
uop_1499 = relay.tan(uop_1484.astype('float64')) # shape=(15, 16, 3)
func_916_call = mod.get_global_var('func_916')
func_918_call = mutated_mod.get_global_var('func_918')
call_1527 = relay.TupleGetItem(func_916_call(), 2)
call_1528 = relay.TupleGetItem(func_918_call(), 2)
func_833_call = mod.get_global_var('func_833')
func_836_call = mutated_mod.get_global_var('func_836')
var_1530 = relay.var("var_1530", dtype = "float64", shape = (39,))#candidate|1530|(39,)|var|float64
call_1529 = relay.TupleGetItem(func_833_call(relay.reshape(var_1530.astype('float64'), [3, 13, 1])), 0)
call_1531 = relay.TupleGetItem(func_836_call(relay.reshape(var_1530.astype('float64'), [3, 13, 1])), 0)
output = relay.Tuple([uop_1474,call_1493,var_1494,uop_1499,call_1527,call_1529,var_1530,])
output2 = relay.Tuple([uop_1474,call_1495,var_1494,uop_1499,call_1528,call_1531,var_1530,])
func_1536 = relay.Function([var_1473,var_1494,var_1530,], output)
mod['func_1536'] = func_1536
mod = relay.transform.InferType()(mod)
var_1537 = relay.var("var_1537", dtype = "float64", shape = (15, 16, 3))#candidate|1537|(15, 16, 3)|var|float64
var_1538 = relay.var("var_1538", dtype = "bool", shape = (216,))#candidate|1538|(216,)|var|bool
var_1539 = relay.var("var_1539", dtype = "float64", shape = (39,))#candidate|1539|(39,)|var|float64
output = func_1536(var_1537,var_1538,var_1539,)
func_1540 = relay.Function([var_1537,var_1538,var_1539,], output)
mutated_mod['func_1540'] = func_1540
mutated_mod = relay.transform.InferType()(mutated_mod)
func_332_call = mod.get_global_var('func_332')
func_333_call = mutated_mod.get_global_var('func_333')
call_1551 = func_332_call()
call_1552 = func_332_call()
output = call_1551
output2 = call_1552
func_1574 = relay.Function([], output)
mod['func_1574'] = func_1574
mod = relay.transform.InferType()(mod)
output = func_1574()
func_1575 = relay.Function([], output)
mutated_mod['func_1575'] = func_1575
mutated_mod = relay.transform.InferType()(mutated_mod)
func_989_call = mod.get_global_var('func_989')
func_991_call = mutated_mod.get_global_var('func_991')
call_1589 = relay.TupleGetItem(func_989_call(), 0)
call_1590 = relay.TupleGetItem(func_991_call(), 0)
func_620_call = mod.get_global_var('func_620')
func_623_call = mutated_mod.get_global_var('func_623')
var_1594 = relay.var("var_1594", dtype = "float64", shape = (455, 2))#candidate|1594|(455, 2)|var|float64
call_1593 = func_620_call(relay.reshape(var_1594.astype('float64'), [5, 14, 13]), relay.reshape(var_1594.astype('float64'), [5, 14, 13]), )
call_1595 = func_620_call(relay.reshape(var_1594.astype('float64'), [5, 14, 13]), relay.reshape(var_1594.astype('float64'), [5, 14, 13]), )
uop_1621 = relay.sinh(var_1594.astype('float32')) # shape=(455, 2)
uop_1642 = relay.atanh(uop_1621.astype('float64')) # shape=(455, 2)
func_543_call = mod.get_global_var('func_543')
func_544_call = mutated_mod.get_global_var('func_544')
call_1646 = relay.TupleGetItem(func_543_call(), 0)
call_1647 = relay.TupleGetItem(func_544_call(), 0)
output = relay.Tuple([call_1589,call_1593,uop_1642,call_1646,])
output2 = relay.Tuple([call_1590,call_1595,uop_1642,call_1647,])
func_1656 = relay.Function([var_1594,], output)
mod['func_1656'] = func_1656
mod = relay.transform.InferType()(mod)
mutated_mod['func_1656'] = func_1656
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1657 = relay.var("var_1657", dtype = "float64", shape = (455, 2))#candidate|1657|(455, 2)|var|float64
func_1656_call = mutated_mod.get_global_var('func_1656')
call_1658 = func_1656_call(var_1657)
output = call_1658
func_1659 = relay.Function([var_1657], output)
mutated_mod['func_1659'] = func_1659
mutated_mod = relay.transform.InferType()(mutated_mod)
func_507_call = mod.get_global_var('func_507')
func_508_call = mutated_mod.get_global_var('func_508')
call_1703 = func_507_call()
call_1704 = func_507_call()
uop_1710 = relay.sqrt(call_1703.astype('float32')) # shape=(3, 8, 9)
uop_1712 = relay.sqrt(call_1704.astype('float32')) # shape=(3, 8, 9)
func_1192_call = mod.get_global_var('func_1192')
func_1193_call = mutated_mod.get_global_var('func_1193')
call_1713 = relay.TupleGetItem(func_1192_call(), 0)
call_1714 = relay.TupleGetItem(func_1193_call(), 0)
func_577_call = mod.get_global_var('func_577')
func_580_call = mutated_mod.get_global_var('func_580')
call_1732 = func_577_call(relay.reshape(call_1713.astype('bool'), [3, 8, 9]))
call_1733 = func_577_call(relay.reshape(call_1713.astype('bool'), [3, 8, 9]))
func_799_call = mod.get_global_var('func_799')
func_803_call = mutated_mod.get_global_var('func_803')
var_1736 = relay.var("var_1736", dtype = "uint16", shape = (80,))#candidate|1736|(80,)|var|uint16
const_1737 = relay.const([[-7,-9,3,-8],[-6,3,1,3],[-1,-1,10,3],[3,6,-2,-5],[1,5,-6,9],[7,4,-7,-5],[-8,9,10,-10],[2,7,6,2],[-7,-5,9,5],[-7,-5,7,-3],[10,3,-6,3],[8,-1,-5,6],[-9,5,5,5],[10,-8,-3,2],[-5,-3,9,-8],[-7,5,-1,4],[-2,-9,8,10],[-5,6,1,1],[-2,-8,10,2],[-4,-9,-6,6],[-1,-4,10,-8],[-6,5,2,-5],[10,-9,-7,10],[-6,8,-2,-9],[-1,4,10,-8],[-8,-4,-1,-7],[10,3,-5,-1],[-2,2,-5,-8],[5,-10,6,1],[-3,6,-2,6],[9,1,4,4],[3,1,8,-6],[1,-9,-6,-3],[-5,-6,4,-1],[3,6,4,-3],[-7,-4,-4,-1],[6,4,-2,4],[7,-6,-2,-1],[-7,-2,8,-5],[-10,1,9,8],[4,1,10,3],[3,-8,6,-10],[6,-3,7,-9],[-9,2,-2,5],[-4,-2,-2,-2],[4,-2,9,3],[-3,-2,-6,-1],[1,5,8,1],[-8,8,8,7],[-10,-4,10,-8],[6,5,-1,1],[2,9,-7,1],[3,-5,9,-5],[-10,2,8,3],[10,-8,-6,6],[4,-9,-6,-6],[10,-10,-3,2],[5,1,3,-9],[-6,7,5,-2],[-9,-10,3,-5],[-5,-4,1,-2],[-9,2,-9,-7],[8,-8,9,2],[3,4,5,-9],[-4,1,-8,-4],[7,8,-6,2],[-1,7,-2,-8],[10,-9,1,9],[10,5,-2,4],[6,7,9,8],[-10,1,-5,-7],[3,3,-5,-3],[10,-4,6,4],[-1,6,10,3],[-10,-2,-5,1],[6,-6,-4,-7],[-5,-9,-8,-3],[-3,1,2,3],[-6,6,-5,-1],[-2,-1,4,-5],[8,1,8,-5],[4,6,7,7],[-6,7,3,4],[7,-4,-5,1],[2,9,10,10],[-1,-10,-8,4],[-2,-7,2,-2],[9,9,4,7],[-4,5,4,7],[-4,4,4,5],[-2,2,-6,-1],[10,-8,2,10],[4,9,5,-3],[-3,-2,-8,4],[1,-4,-2,-9],[6,7,-5,-5],[6,-8,10,-9],[-2,-1,-8,-10],[2,-6,-10,-7],[4,-4,4,-9],[5,-1,-1,-9],[3,-3,6,-2],[9,1,2,-6],[3,-5,-9,-7],[-2,-9,-1,7],[-10,-7,-4,-3],[6,2,5,4],[8,-6,6,3],[-4,-2,-3,-8],[-9,-9,3,-8],[7,7,-6,9],[2,10,9,-5],[-6,-7,-8,-1],[-2,-2,4,4],[-7,-3,-1,6],[-10,-1,-10,3],[7,-6,-6,10],[1,3,-1,7],[7,1,-6,3],[-5,-6,-5,4]], dtype = "uint16")#candidate|1737|(120, 4)|const|uint16
call_1735 = func_799_call(relay.reshape(var_1736.astype('uint16'), [1, 5, 16]), relay.reshape(const_1737.astype('uint16'), [6, 5, 16]), )
call_1738 = func_799_call(relay.reshape(var_1736.astype('uint16'), [1, 5, 16]), relay.reshape(const_1737.astype('uint16'), [6, 5, 16]), )
output = relay.Tuple([uop_1710,call_1713,call_1732,call_1735,var_1736,const_1737,])
output2 = relay.Tuple([uop_1712,call_1714,call_1733,call_1738,var_1736,const_1737,])
func_1755 = relay.Function([var_1736,], output)
mod['func_1755'] = func_1755
mod = relay.transform.InferType()(mod)
var_1756 = relay.var("var_1756", dtype = "uint16", shape = (80,))#candidate|1756|(80,)|var|uint16
output = func_1755(var_1756)
func_1757 = relay.Function([var_1756], output)
mutated_mod['func_1757'] = func_1757
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1788 = relay.var("var_1788", dtype = "float64", shape = (7, 4, 1))#candidate|1788|(7, 4, 1)|var|float64
uop_1789 = relay.exp(var_1788.astype('float64')) # shape=(7, 4, 1)
output = uop_1789
output2 = uop_1789
func_1793 = relay.Function([var_1788,], output)
mod['func_1793'] = func_1793
mod = relay.transform.InferType()(mod)
var_1794 = relay.var("var_1794", dtype = "float64", shape = (7, 4, 1))#candidate|1794|(7, 4, 1)|var|float64
output = func_1793(var_1794)
func_1795 = relay.Function([var_1794], output)
mutated_mod['func_1795'] = func_1795
mutated_mod = relay.transform.InferType()(mutated_mod)
func_507_call = mod.get_global_var('func_507')
func_508_call = mutated_mod.get_global_var('func_508')
call_1808 = func_507_call()
call_1809 = func_507_call()
uop_1810 = relay.atanh(call_1808.astype('float32')) # shape=(3, 8, 9)
uop_1812 = relay.atanh(call_1809.astype('float32')) # shape=(3, 8, 9)
func_1793_call = mod.get_global_var('func_1793')
func_1795_call = mutated_mod.get_global_var('func_1795')
var_1814 = relay.var("var_1814", dtype = "float64", shape = (28,))#candidate|1814|(28,)|var|float64
call_1813 = func_1793_call(relay.reshape(var_1814.astype('float64'), [7, 4, 1]))
call_1815 = func_1793_call(relay.reshape(var_1814.astype('float64'), [7, 4, 1]))
output = relay.Tuple([uop_1810,call_1813,var_1814,])
output2 = relay.Tuple([uop_1812,call_1815,var_1814,])
func_1816 = relay.Function([var_1814,], output)
mod['func_1816'] = func_1816
mod = relay.transform.InferType()(mod)
var_1817 = relay.var("var_1817", dtype = "float64", shape = (28,))#candidate|1817|(28,)|var|float64
output = func_1816(var_1817)
func_1818 = relay.Function([var_1817], output)
mutated_mod['func_1818'] = func_1818
mutated_mod = relay.transform.InferType()(mutated_mod)
func_507_call = mod.get_global_var('func_507')
func_508_call = mutated_mod.get_global_var('func_508')
call_1846 = func_507_call()
call_1847 = func_507_call()
func_543_call = mod.get_global_var('func_543')
func_544_call = mutated_mod.get_global_var('func_544')
call_1850 = relay.TupleGetItem(func_543_call(), 0)
call_1851 = relay.TupleGetItem(func_544_call(), 0)
func_799_call = mod.get_global_var('func_799')
func_803_call = mutated_mod.get_global_var('func_803')
const_1863 = relay.const([-7,8,10,9,-4,6,3,3,-5,9,-2,3,1,2,-7,9,-5,-7,-10,4,-3,-3,4,-6,-8,8,-1,-6,3,2,-8,-3,-9,-9,7,4,-4,6,2,7,-6,2,6,-10,7,-8,-2,-7,1,9,-9,-8,1,-1,6,4,2,1,-3,8,10,4,-9,2,-7,10,7,9,1,-10,-7,-1,10,9,-3,-5,5,7,-10,-5], dtype = "uint16")#candidate|1863|(80,)|const|uint16
var_1864 = relay.var("var_1864", dtype = "uint16", shape = (480,))#candidate|1864|(480,)|var|uint16
call_1862 = func_799_call(relay.reshape(const_1863.astype('uint16'), [1, 5, 16]), relay.reshape(var_1864.astype('uint16'), [6, 5, 16]), )
call_1865 = func_799_call(relay.reshape(const_1863.astype('uint16'), [1, 5, 16]), relay.reshape(var_1864.astype('uint16'), [6, 5, 16]), )
func_1234_call = mod.get_global_var('func_1234')
func_1237_call = mutated_mod.get_global_var('func_1237')
call_1871 = relay.TupleGetItem(func_1234_call(relay.reshape(call_1862.astype('uint16'), [480,]), relay.reshape(call_1862.astype('uint64'), [6, 5, 16]), ), 2)
call_1872 = relay.TupleGetItem(func_1237_call(relay.reshape(call_1862.astype('uint16'), [480,]), relay.reshape(call_1862.astype('uint64'), [6, 5, 16]), ), 2)
output = relay.Tuple([call_1846,call_1850,call_1862,const_1863,var_1864,call_1871,])
output2 = relay.Tuple([call_1847,call_1851,call_1865,const_1863,var_1864,call_1872,])
func_1877 = relay.Function([var_1864,], output)
mod['func_1877'] = func_1877
mod = relay.transform.InferType()(mod)
var_1878 = relay.var("var_1878", dtype = "uint16", shape = (480,))#candidate|1878|(480,)|var|uint16
output = func_1877(var_1878)
func_1879 = relay.Function([var_1878], output)
mutated_mod['func_1879'] = func_1879
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1013_call = mod.get_global_var('func_1013')
func_1014_call = mutated_mod.get_global_var('func_1014')
call_1901 = func_1013_call()
call_1902 = func_1013_call()
output = relay.Tuple([call_1901,])
output2 = relay.Tuple([call_1902,])
func_1918 = relay.Function([], output)
mod['func_1918'] = func_1918
mod = relay.transform.InferType()(mod)
output = func_1918()
func_1919 = relay.Function([], output)
mutated_mod['func_1919'] = func_1919
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1002_call = mod.get_global_var('func_1002')
func_1004_call = mutated_mod.get_global_var('func_1004')
call_1989 = func_1002_call()
call_1990 = func_1002_call()
func_620_call = mod.get_global_var('func_620')
func_623_call = mutated_mod.get_global_var('func_623')
const_1994 = relay.const([6.750968,-3.793577,-1.355399,0.371108,-3.791111,-1.580712,8.013676,2.451203,-7.984633,2.211822,-7.549456,3.268025,-3.305044,6.299480,-8.172279,8.125798,-4.198699,-3.869354,-0.098079,-5.006544,1.605965,-0.947048,-8.366949,9.100243,2.243344,-1.050803,6.469960,3.900959,8.947675,0.946655,-9.002823,5.647275,-5.076173,-9.831007,5.926202,1.256774,8.264456,6.965803,4.408403,4.117419,9.991672,3.383885,4.521849,1.853053,6.980929,5.560127,4.994320,3.926512,-5.829179,-5.478441,-0.840038,6.213717,5.698069,-9.408966,1.811518,-9.829529,2.707528,4.880981,-2.076137,6.615607,8.091211,9.336071,9.930161,-2.112190,-0.075150,4.003941,-9.734809,6.080009,1.650470,1.699707,6.071161,-1.054061,0.772484,9.390573,-7.612670,5.565418,2.541572,-3.316434,3.976929,3.514856,5.173866,6.739740,8.532190,4.129919,-1.410624,5.090862,-7.155320,-8.625357,-8.990687,8.211849,3.606189,-8.570628,-3.867592,2.443433,-6.641053,0.061411,-0.766583,7.746440,0.869401,-7.114724,3.802713,7.427634,7.160017,9.947564,-8.383554,-1.810450,-9.840223,-7.075787,0.433808,-0.497728,-9.239759,8.160833,-9.977424,-0.735120,-7.843748,2.042005,9.020096,0.964896,1.541507,-9.875420,-6.849813,3.515318,5.806602,6.213349,7.429313,-0.930689,3.858050,-7.000718,4.915978,-0.891350,-7.166985,1.781390,-5.446484,-1.531175,-8.181920,1.012795,-8.299929,3.681566,0.002701,-1.154671,-7.582869,-3.671149,0.630468,-9.443238,-4.120218,-9.710088,-8.531037,-2.931157,-7.594483,-7.956043,6.087644,5.337007,-3.389686,1.459187,0.003654,1.577815,8.529946,-8.818615,-8.109165,9.993028,2.489863,4.179098,7.096720,-6.021500,3.010740,-6.858920,5.827307,-1.519712,-8.237613,6.848003,4.849960,-0.880142,-1.149219,5.460476,9.011797,1.512106,-7.879505,-4.506793,-5.293819,-9.027222,-8.603374,-5.573032,-2.853049,3.021989,0.349577,9.699968,0.438494,6.178926,-9.111332,8.275091,3.721682,-1.040465,1.690756,4.443886,9.173180,2.993725,0.919752,8.546765,-9.314802,-1.897422,7.128059,2.959742,5.594293,1.113856,2.291571,4.565337,2.530874,2.254752,0.070873,3.700686,-9.413768,-3.690447,-1.957653,6.146884,-7.275652,-9.460657,1.020123,8.917815,-3.992700,-8.429392,1.326534,-2.203599,1.913268,5.511682,1.494072,-6.191781,-3.675539,4.240617,-1.337729,9.828375,-9.424042,8.635484,2.145224,9.432699,1.094187,-7.781947,7.117196,6.632647,-7.699072,3.002534,6.357364,4.335067,-4.833883,4.751888,1.977406,-7.633884,-2.880597,-8.162607,-7.211376,-3.057498,9.612545,-9.174113,3.096367,-4.691983,-2.668852,0.609985,7.124504,5.947157,9.302438,-4.160929,-3.641573,9.448050,-3.601353,-3.502554,6.956198,-0.259510,0.829204,1.075814,4.596514,-5.663534,-6.518948,9.337413,-6.355447,8.483526,3.666201,6.023697,-6.723681,9.872528,-0.099983,6.673934,-7.374186,-4.459686,-2.667562,-5.143389,0.011428,-5.302727,8.438927,7.856398,-9.443279,1.695216,8.787860,6.054168,4.506660,-6.880822,0.220219,8.244599,-6.657608,5.284308,-7.247154,-3.603415,9.626601,8.588632,-1.591324,-2.105206,9.967338,8.731961,-9.465276,8.031160,8.685185,9.458253,0.900443,-1.193443,4.679191,3.118794,1.407476,4.994686,-2.016769,1.459696,-5.573511,8.759658,-6.871449,-7.064292,-9.592693,-1.970887,1.114755,-8.402649,0.818471,-9.628631,-3.885264,-9.027053,5.079051,-0.644774,-5.944665,3.691398,-1.914562,-8.676722,0.646324,8.595827,-9.692619,0.480532,-8.637307,4.415345,-1.192828,-9.152186,4.276396,-6.398985,-8.171883,-6.993994,2.502152,4.624526,-4.265562,-6.988121,-9.798223,1.818265,5.281283,7.595297,-0.314202,2.155521,-3.801795,-9.460226,-3.131008,1.269385,0.909510,7.658192,5.093907,-9.713566,1.142430,2.122011,1.503239,-4.033184,4.457075,-0.794784,-5.829329,-9.606559,2.225580,-2.168784,5.861935,-8.286023,7.872303,1.379918,8.640107,5.248793,-8.623320,-7.008417,4.505272,2.976520,-2.976473,8.081369,5.550866,-9.884663,-1.186793,2.168025,-7.718001,-8.160655,3.114603,-3.882549,-0.084567,3.637747,-2.501033,-5.968050,1.588391,-2.204744,3.595247,-0.101098,8.028999,0.073540,-5.600616,4.635348,-9.221071,-9.247669,-4.810173,-3.021201,-4.935193,9.657073,-3.384361,0.477618,6.313466,8.131186,5.880871,-2.724278,-3.046295,-6.080095,-6.776184,9.260258,1.270192,-3.403796,-2.672209,-6.928342,1.050189,6.646666,8.172635,5.154995,-9.798987,8.428565,-0.654521,-6.371059,2.409682,0.314319,4.266325,1.630719,0.659615,-9.057097,-8.594108,-9.855022,-2.742770,7.426655,-7.736122,3.745199,-4.298701,-2.507420,-6.625025,1.583893,2.868152,2.038239,-5.596449,-8.150695,-4.509919,3.067589,8.889899,-7.312921,-3.165323,-6.560839,-3.983518,0.743839,-3.564014,-9.456632,1.347617,0.791549,-5.675197,7.336288,5.892687,-8.589760,-0.723090,-8.068001,-7.443137,9.911284,7.493926,1.803172,4.584076,-6.456692,2.752624,-2.866255,-5.391556,9.218182,-0.639407,8.951009,-5.965382,-1.479775,-1.635893,7.326379,3.462630,0.298306,-7.637456,7.696666,6.205489,8.481850,-1.290324,0.878548,5.014867,5.803625,3.531611,0.793069,7.627890,-3.523004,9.280556,-6.730317,3.796755,5.443243,-5.701955,7.331494,-5.401352,-6.397315,9.492784,7.289471,2.670560,-4.460507,-6.397112,-0.141686,9.152715,5.450751,-0.515263,-0.796403,3.386823,3.205744,-0.409976,9.690189,-2.746486,2.029776,-5.917717,-2.050132,2.597438,-0.336349,7.492520,4.499948,-4.163352,8.067649,-7.185522,-2.638588,8.395392,-8.095265,-6.519480,-2.228213,8.561572,-0.933212,-8.209796,7.503050,-8.320375,4.760632,4.694725,-7.701279,7.779980,-7.962822,5.593170,0.453449,4.761002,-6.668929,-9.211390,-0.037583,-0.024739,6.692394,1.456192,7.958267,-7.279527,7.538538,3.765768,3.975633,0.146260,8.708250,-6.365643,9.013332,-2.586625,-2.076345,-5.153825,-1.493281,0.665772,-2.522263,0.418945,-0.616284,-4.348592,1.510083,-9.533850,1.652941,-5.779047,-9.872227,1.953779,-0.330237,-4.137622,-5.536759,8.948595,5.320791,-1.356446,-2.827262,1.530510,-1.251938,-9.186527,-7.025234,-3.973015,2.465338,-3.994609,-0.942253,2.442183,7.102376,1.851621,9.010876,-4.071584,6.750688,-7.471401,-2.061124,4.933081,7.632783,-6.666384,-6.502353,6.395492,-5.784594,0.144233,-2.889807,0.347242,-0.839098,1.627104,-1.066137,1.446691,7.485883,0.028764,6.984484,-0.313238,-3.000859,-8.570944,8.352310,-2.377087,0.444556,-2.284881,4.439230,2.437311,-3.640216,0.691062,9.222454,6.089639,-7.055521,-1.455243,6.419639,-8.257634,-9.420355,-7.975737,5.444270,7.181312,-9.724069,-2.380294,7.865442,-3.701549,-0.340085,-3.001653,-0.031133,-6.833470,-4.500679,-5.510717,8.939219,-4.257168,-9.240623,-6.547937,2.430313,-6.034290,1.114795,8.379898,5.634405,7.328590,9.515177,9.748085,9.602068,-6.177509,-6.339324,1.051434,-4.706035,6.256517,-4.276759,-3.935154,0.536096,8.263165,4.087370,-2.444775,-6.765742,-1.152513,0.793414,7.973067,-8.180975,3.377722,1.092365,-3.667798,-9.181983,-7.748771,7.363294,-0.698499,5.542572,-4.758566,9.101170,4.445103,-8.441276,9.366879,3.233146,-1.040232,9.949177,1.611454,-5.110638,-9.206145,6.476979,4.570254,7.130178,-7.949800,1.813109,0.970635,6.091124,0.913214,-1.148976,8.312173,0.354954,8.446681,6.758895,9.241375,6.491837,-9.590003,-7.264387,9.394191,-4.617279,7.339230,-1.879188,-7.260196,4.333415,9.445984,-0.751107,-2.177741,-0.652349,-8.665061,-8.644856,4.514587,1.894900,-8.826520,2.826251,3.715473,6.507339,-3.325487,6.000204,1.007603,-4.449849,7.480219,-7.400857,-8.376583,7.182915,-4.952455,9.211584,8.999522,-2.050758,-5.522411,-0.123144,0.497743,-4.509709,3.944313,-2.929190,8.656571,-1.970993,3.937317,-4.554506,6.554369,4.234740,0.370832,-6.905668,2.742859,-0.717606,-2.155769,-3.157433,6.122976,3.563535,-1.958811,1.485016,-5.022492,-7.794356,-9.579883,-0.724526,7.560889,-7.476352,-9.266474,5.320983,9.732727,4.408812,-6.554606,3.267624,3.911963,0.277498,-2.249893,8.176185,-4.900740,-9.596625,-3.601647,-1.001071,-9.797466,-7.541747,7.835983,9.454203,7.103376,8.766907,-0.115496,6.134383,5.568273,9.580107,-6.733437,5.207011,3.404422,8.503058,-2.212233,4.894571,-3.493249,7.792881,4.078877,-7.303015,0.067254,8.032486,-0.275616,6.124844,4.399855,1.527659,1.165435,-6.237235,6.324557,-9.667722,5.359829,-7.443957,3.020876,-4.659772,-9.250619,-8.092433,-8.427146,5.093169,-1.881187,-8.292612,-3.355130,6.749422,-6.749820,-9.823546,-1.398292,4.083938,-8.846836,9.762048,5.555816,-2.593370,8.437822,-2.166311,-3.417814,-9.576788,-6.944616,-7.863096,2.585740,1.410375,0.350232,2.401603,-1.079404,-6.546314,-8.393572,3.848458,1.826503,-8.302883,-3.135894,-6.280491,-7.903663,6.403016,1.798913,5.920387,-8.609462,2.328835,-6.310509,0.015734,5.999543,2.192088,5.759031,-3.322183,8.139537,6.907164,2.537214,-7.982911,6.132712,-5.070769,-4.962207,3.500578,-1.716987,-9.623873,4.567343,-7.073479,4.769862,-7.230691,-3.891238,0.490337,0.888217,7.784718,-8.720486,7.381658,6.720059,9.450210,8.045571,-4.909151,1.841427,6.006714,-3.467287,3.424545,0.201874,4.580883,-6.025372,1.525309,8.353918,-6.102427,4.587301,8.849518,-2.066184,-1.180620], dtype = "float64")#candidate|1994|(910,)|const|float64
call_1993 = func_620_call(relay.reshape(const_1994.astype('float64'), [5, 14, 13]), relay.reshape(const_1994.astype('float64'), [5, 14, 13]), )
call_1995 = func_620_call(relay.reshape(const_1994.astype('float64'), [5, 14, 13]), relay.reshape(const_1994.astype('float64'), [5, 14, 13]), )
output = relay.Tuple([call_1989,call_1993,const_1994,])
output2 = relay.Tuple([call_1990,call_1995,const_1994,])
func_2007 = relay.Function([], output)
mod['func_2007'] = func_2007
mod = relay.transform.InferType()(mod)
mutated_mod['func_2007'] = func_2007
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2007_call = mutated_mod.get_global_var('func_2007')
call_2008 = func_2007_call()
output = call_2008
func_2009 = relay.Function([], output)
mutated_mod['func_2009'] = func_2009
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2023 = relay.var("var_2023", dtype = "float64", shape = (2, 12, 11))#candidate|2023|(2, 12, 11)|var|float64
uop_2024 = relay.sinh(var_2023.astype('float64')) # shape=(2, 12, 11)
func_609_call = mod.get_global_var('func_609')
func_611_call = mutated_mod.get_global_var('func_611')
call_2026 = relay.TupleGetItem(func_609_call(), 1)
call_2027 = relay.TupleGetItem(func_611_call(), 1)
output = relay.Tuple([uop_2024,call_2026,])
output2 = relay.Tuple([uop_2024,call_2027,])
func_2033 = relay.Function([var_2023,], output)
mod['func_2033'] = func_2033
mod = relay.transform.InferType()(mod)
var_2034 = relay.var("var_2034", dtype = "float64", shape = (2, 12, 11))#candidate|2034|(2, 12, 11)|var|float64
output = func_2033(var_2034)
func_2035 = relay.Function([var_2034], output)
mutated_mod['func_2035'] = func_2035
mutated_mod = relay.transform.InferType()(mutated_mod)
func_332_call = mod.get_global_var('func_332')
func_333_call = mutated_mod.get_global_var('func_333')
call_2054 = func_332_call()
call_2055 = func_332_call()
func_833_call = mod.get_global_var('func_833')
func_836_call = mutated_mod.get_global_var('func_836')
var_2062 = relay.var("var_2062", dtype = "float64", shape = (39,))#candidate|2062|(39,)|var|float64
call_2061 = relay.TupleGetItem(func_833_call(relay.reshape(var_2062.astype('float64'), [3, 13, 1])), 1)
call_2063 = relay.TupleGetItem(func_836_call(relay.reshape(var_2062.astype('float64'), [3, 13, 1])), 1)
output = relay.Tuple([call_2054,call_2061,var_2062,])
output2 = relay.Tuple([call_2055,call_2063,var_2062,])
func_2086 = relay.Function([var_2062,], output)
mod['func_2086'] = func_2086
mod = relay.transform.InferType()(mod)
var_2087 = relay.var("var_2087", dtype = "float64", shape = (39,))#candidate|2087|(39,)|var|float64
output = func_2086(var_2087)
func_2088 = relay.Function([var_2087], output)
mutated_mod['func_2088'] = func_2088
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2095 = relay.var("var_2095", dtype = "float64", shape = (16, 11, 5))#candidate|2095|(16, 11, 5)|var|float64
uop_2096 = relay.sin(var_2095.astype('float64')) # shape=(16, 11, 5)
func_620_call = mod.get_global_var('func_620')
func_623_call = mutated_mod.get_global_var('func_623')
const_2100 = relay.const([[7.913329,9.349323,-5.955698,0.505326,-1.268842,-1.213480,9.638822,2.279700,-0.552763,-8.662880,-1.414792,-9.207351,-9.526349,-8.913353,-3.406353,-4.172873,7.258557,8.838388,-4.331377,-4.299328,9.476889,1.413185,9.909388,0.488491,4.342753,-9.417126,3.843739,9.413449,-0.716248,-6.590538,-0.732152,4.345432,-4.235086,9.677273,2.369124,6.053819,-1.096368,-2.574583,7.395455,7.939071,0.739590,-7.778471,-0.312530,-7.442111,2.572411,-3.352111,7.946335,9.562896,-4.485776,-7.938906,1.452098,-8.714566,2.304421,5.475374,-4.647232,1.816842,-2.130840,-6.378878,8.836161,-6.690447,0.557768,-6.095536,-1.640203,-9.063534,1.567811,-4.273582,-5.145313,-0.375968,9.507716,-4.051504,3.268328,2.709196,-4.322324,-6.375887,6.910427,-2.310503,6.076849,3.821702,5.961743,-6.970341,0.623753,3.652383,7.932796,7.874347,7.568812,8.175091,0.717414,6.938033,-1.392985,7.079685,-6.359927,1.741648,2.394189,2.438715,-2.599479,7.316477,-8.077091,-4.270737,-0.122995,6.982897,2.408889,-1.529869,2.943281,-4.163831,-7.354794,7.945366,-2.930398,-9.062052,-0.155822,-8.561359,-9.350952,-9.518038,-9.599951,-4.076343,-5.490495,-4.193265,-6.657387,-5.111481,-2.889579,-1.587927,-9.353729,9.329683,-3.413270,-0.403026,3.779838,3.384803,-7.341716,3.984380,-9.086389,-0.360743,2.703649,9.147073,8.715771,6.432145,-9.518532,-5.294001,-1.009134,1.431747,-2.399997,0.845030,-4.903870,4.616771,-3.192798,2.052911,-0.279770,7.725423,0.170763,-1.438079,-2.208939,-2.455011,1.670824,4.278157,0.714203,-6.516279,8.430583,6.846084,-3.516886,-9.263803,3.568799,-6.225554,0.761631,8.318496,-6.997012,-3.761444,-7.964236,5.488772,8.351084,4.288842,-2.491120,-0.770049,3.692726,8.453352,-8.947617,-6.149013,-8.366962,-3.338367,-7.077363,-9.192750,9.133918,8.567459,0.774488,2.200137,8.702619,6.763419,-0.682547,3.982969,-6.452038,6.707288,2.127717,-6.159813,-9.077991,7.763683,0.230497,9.530618,-3.184752,-5.635141,-8.134909,8.318106,-7.901919,5.956653,-7.441481,-9.504637,3.191461,-3.213025,6.533880,-7.996326,1.221783,-5.354717,1.191234,8.356762,-1.635609,-8.666728,4.359500,-9.085053,-3.139027,-0.152609,9.473091,3.196335,-0.878758,3.278483,4.244566,-5.771301,9.480078,2.668260,-4.864598,9.785436,-3.295000,8.004783,5.458375,9.707027,7.155467,-0.742014,-9.839440,-7.764077,8.169116,-9.176252,5.952003,6.317934,1.005232,-9.511710,6.339876,-4.461723,2.371497,2.315197,6.976381,-7.821232,-1.708137,6.258044,4.269616,-3.141982,6.850501,2.743539,4.413162,-9.343262,3.020902,-0.458175,-9.919759,-1.382649,9.491158,-6.918702,-7.604240,1.139874,0.162589,7.554136,-8.675155,-4.613309,-0.336886,5.255773,-6.676065,-0.069250,-6.555273,4.728119,1.876531,-8.682317,4.584507,6.292757,1.387848,2.036857,-4.635224,1.244386,-2.999387,-1.902441,2.193313,-3.337066,3.304701,8.579319,7.487892,-6.792845,-4.760238,3.639771,5.117060,6.738778,-9.998373,-7.881934,3.680806,5.074587,5.355321,-3.130511,7.342038,-4.757697,2.151362,-2.455244,-5.025778,3.304744,5.902855,3.261119,-4.230385,-5.477777,8.135287,0.735203,-8.071431,-9.612342,-5.388137,5.870369,8.319229,9.631037,9.729729,2.916942,-2.774829,8.135074,-6.410353,5.848909,7.872221,4.633063,-0.653744,-4.049287,5.074808,-1.547487,5.687370,-7.396353,8.706545,-1.325921,0.362161,5.611525,-6.956729,-6.468831,7.130228,3.821074,3.888742,1.414938,9.756867,-3.008743,-5.080615,3.667985,-7.510021,-3.955783,3.982748,4.198569,-2.876406,-9.985029,0.036857,5.664271,-1.278403,6.395901,1.452028,6.483304,-6.865830,-1.930289,-0.654566,4.288290,6.960674,5.478189,-0.417509,7.208801,3.126332,6.100402,-0.907701,6.538062,-4.203616,-1.649077,7.992532,-5.328176,-8.073421,-9.525624,-1.709029,5.522699,1.938658,-1.439755,8.925753,-8.977116,-1.794889,5.823128,7.126551,1.604927,-4.239833,2.049206,-2.820264,4.544131,-0.366920,8.847440,1.923585,-0.812039,0.776357,-7.815201,5.851944,6.167304,9.068017,-1.761377,5.355716,-4.814692,-1.082441,2.368359,8.256062,4.404471,-5.911101,2.218645,9.543417,-0.575079,-2.559335,-7.153025,-0.576326,9.153529,-5.362775,-9.295029,-1.121997,2.002083,-4.596629,4.514827,-7.013162,-3.835955,4.744657,-5.712760,7.682653,-1.835363,-2.040360,2.212745,-9.976716,-8.494895,4.286150,5.455078,2.178462,-1.951325,4.002445,3.133136,-3.730290,9.127999,4.381857,-2.660682,-8.127824,4.320683,4.969444,1.968822,3.365223,7.025118,-7.287654,-8.813347,4.301916,-9.545283,-9.239266,-3.893688,3.109528,2.499631,-1.615938,4.133048,-7.045747,6.621408,-4.269460,7.179051,-3.018931,-8.838814,0.018539,-6.601761,7.791728,-7.104207,-3.143415,-5.119402,-7.827878,6.359319,9.149255,5.558801,5.224726,-2.994801,-3.062016,4.637234,-2.326981,5.060740,5.346511,-1.054126,-3.674216,-7.824963,-1.308665,-1.805462,-7.501936,7.889788,4.425422,4.336575,7.911285,-7.518736,-7.944827,-7.577334,7.870887,-8.758763,4.481475,5.080754,0.136017,-8.753978,-3.560395,-9.605026,-7.080761,-4.004951,2.085173,-1.190850,4.409516,-7.411105,7.931385,-8.839363,-1.181706,7.208035,-5.491621,-4.438001,-0.167857,5.797089,0.915947,-0.405734,0.066923,1.655082,-3.975169,2.273392,-7.101885,7.474016,-2.924360,-4.789155,5.440985,-3.381571,-5.009084,5.639754,5.059872,6.771036,5.078813,7.125839,2.575688,4.369811,-1.910581,7.725449,-2.820559,-4.021217,0.968034,2.741941,-8.675624,-0.990801,-0.409765,-4.917214,-8.831366,5.244129,2.609453,-1.320532,5.994400,-8.051335,-7.514296,4.254387,5.526668,0.077150,-4.460765,9.301965,-5.377901,-2.154595,7.728288,-9.474479,-6.618108,0.925797,-0.814762,-9.808349,9.576276,-2.650097,6.833607,-7.049304,8.572569,5.330125,4.856983,0.157106,-4.076813,-3.969753,-5.799994,8.619061,-8.249240,-0.190286,-9.581139,4.987187,7.957266,0.449321,0.959160,1.082792,5.334750,-9.810555,0.257947,-0.688970,2.089675,-1.529233,2.434423,7.642270,-8.373204,0.995127,-1.745538,4.072732,-7.664065,-4.416355,-6.042660,-4.412931,-7.927912,-5.630483,-9.478381,2.935164,-0.648353,3.670672,5.248104,5.757142,-4.887366,-3.842579,2.270162,2.696973,-4.205055,1.434232,0.558176,-7.036904,8.215139,-5.558390,3.280482,9.042058,6.110215,-7.563106,0.878640,-3.919295,-3.573081,1.467935,-4.531537,0.020540,-6.389195,-7.917827,-0.201632,-8.186877,8.714276,-9.478896,-6.846186,-2.475460,-8.647952,6.948876,1.590550,-9.997473,-3.611657,9.135652,-9.942112,-7.593634,-9.620360,-0.176107,0.314446,-2.160062,5.929072,-4.549588,-9.703334,0.230608,0.518075,4.799917,7.580636,-5.894289,4.701295,-8.392325,-9.303713,-6.556637,3.417040,2.941296,5.925996,-6.264423,-0.789635,6.845288,5.398524,-8.340372,1.555103,0.372710,7.702738,-2.246053,-9.971927,-5.635494,3.760358,2.463427,1.388158,-5.924799,-5.532828,-8.645821,2.736126,3.182751,-2.250156,9.273111,6.026857,-4.191336,-4.843988,5.519018,-4.701860,9.625089,8.058046,-6.350708,0.637037,5.089546,9.966107,8.024330,5.262672,-3.632894,-6.174472,3.473557,-8.917624,-3.917639,3.942261,9.999455,7.529395,4.427152,8.791456,5.163955,-5.661739,-0.839793,-4.346562,-2.431198,6.872760,-4.707947,-4.559525,5.010100,0.973000,9.130135,-7.567890,-0.699401,6.919947,-0.746850,-9.844617,-5.381812,-4.952537,-7.536327,-4.586652,9.304097,9.094148,7.520295,2.715436,8.208365,-1.301270,0.582681,0.407882,-5.812747,-8.433511,-6.072349,-8.708063,5.266064,6.249666,-2.732078,0.082874,3.846683,5.742881,-9.230245,-0.393239,0.011626,7.502922,3.904044,9.113112,7.961440,-6.349894,-1.492984,-9.902041,8.660053,5.182381,0.310150,8.690205,-5.968054,3.455411,-2.123284,-1.112110,-0.072608,-1.264760,-1.171262,0.543713,3.304783,3.113807,7.318055,-7.638747,-1.441896,-6.299441,-1.047233,-5.186434,-6.620905,7.912178,3.830894,-4.186683,3.240781,2.996831,-4.676152,-2.072448,-4.536693,7.303885,3.875654,3.024081,-8.686913,-8.526128,2.899910,8.974355,-7.501191,-3.190060,-3.954571,-3.932746,-3.351239,4.834397,-0.045838,-6.728869,-8.361959,-0.466123,7.485657,2.287108,2.130586,-7.263609,-8.444299,-4.232686,7.986951,4.443143,-4.011423,0.382945,9.751652,2.785842,-8.968476,2.001342,-3.959550,9.997731,2.818349,8.701821,-0.678957,6.958966,9.436029,5.285565,7.757332,-8.082923,-9.901363,-5.766186,-2.036502,-6.904957,3.132710,0.416393,2.935450,-2.025441,3.849593,-6.743609,4.980997,1.922188,9.393587,3.376872,5.343256,-2.186166,-1.840390,1.780868,7.270003,7.089751,2.739413,-4.274094,0.419764,3.447844,-7.272333,-6.225853,-5.132737,-1.329455,3.721982,-7.088310,4.038889,-4.554170,4.565023,-2.937790,7.739301,3.184763,8.246289,-3.015826,-0.564482,0.124087,9.424950,6.423708,1.346675,0.882615,3.637558,4.689324,0.575354,-0.718196,-3.308603,5.395450,0.154519,-4.536778,-8.095667,6.665744,7.273110,9.071661,1.223064,-0.602352,-5.619097,8.673240,8.101641,-0.447530,-0.942938,1.076389,7.815899,3.666361,0.158895,9.575387,-8.430578,7.965915,-9.564403,-9.157014,0.521528,-6.701832,-0.084818,3.584614,7.576633,-7.914146,4.828076,-1.657145,-6.350836,8.502540,8.919591,9.479053,6.702069,0.864736,3.493058]], dtype = "float64")#candidate|2100|(1, 910)|const|float64
call_2099 = func_620_call(relay.reshape(const_2100.astype('float64'), [5, 14, 13]), relay.reshape(const_2100.astype('float64'), [5, 14, 13]), )
call_2101 = func_620_call(relay.reshape(const_2100.astype('float64'), [5, 14, 13]), relay.reshape(const_2100.astype('float64'), [5, 14, 13]), )
output = relay.Tuple([uop_2096,call_2099,const_2100,])
output2 = relay.Tuple([uop_2096,call_2101,const_2100,])
func_2110 = relay.Function([var_2095,], output)
mod['func_2110'] = func_2110
mod = relay.transform.InferType()(mod)
mutated_mod['func_2110'] = func_2110
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2111 = relay.var("var_2111", dtype = "float64", shape = (16, 11, 5))#candidate|2111|(16, 11, 5)|var|float64
func_2110_call = mutated_mod.get_global_var('func_2110')
call_2112 = func_2110_call(var_2111)
output = call_2112
func_2113 = relay.Function([var_2111], output)
mutated_mod['func_2113'] = func_2113
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2118 = relay.const([[[-2.526356,-9.332460,9.251240,-7.164840,-7.272062,-7.489037,-7.857642,-2.660613,-3.179377,1.191526,-4.867220,-3.672939,3.229435,7.037011],[-8.113955,-6.807834,-5.970939,9.346445,-8.500131,2.866035,-3.255621,2.953663,-5.435652,1.973998,-2.653237,-4.597514,-7.471725,-9.754088],[8.240269,-1.467000,-1.346971,-7.322867,4.761040,-3.360903,-5.600954,-1.852467,3.893639,6.270701,-1.452040,-7.256608,0.141173,6.551244],[5.809497,-5.776103,-6.712837,9.327585,1.934100,3.104229,1.295198,-7.869198,1.117670,-1.945921,0.059673,0.772741,-9.713461,-0.652306],[-8.630178,-2.130370,6.500591,9.163198,0.955448,-1.525497,-4.374208,3.879539,2.272796,8.052149,-5.463378,-4.813582,4.809858,4.194359],[1.929156,-5.506520,-4.710516,-9.933809,5.378915,3.444052,-4.410905,3.336951,7.790644,-2.655212,-6.926685,-1.314694,7.857763,-4.268511],[-1.970676,-6.819944,1.418549,8.777804,4.499120,3.410510,3.284035,6.003149,-5.159381,1.135057,0.818268,4.386505,5.751424,6.656669],[-8.373516,-7.349333,9.738286,-5.449236,5.910192,-0.048157,0.775456,5.735294,-7.609661,-5.280015,2.353408,9.658833,6.801639,-8.534834],[-7.584762,7.980516,-4.381976,1.231893,7.239223,-2.193865,0.884100,4.021146,5.108937,-7.275291,-4.560289,-0.506381,-7.719021,-0.565676],[-4.418870,-7.329677,-5.888770,1.622744,9.141195,7.147576,1.300906,6.400120,-5.644415,3.548689,2.348999,-6.316663,0.564804,9.008741]]], dtype = "float64")#candidate|2118|(1, 10, 14)|const|float64
const_2119 = relay.const([[[9.141895,3.453521,-4.088623,-6.930563,3.070979,-4.867433,2.378996,0.299414,-0.637229,7.931016,-9.277702,4.046162,9.582836,6.840853],[9.520094,-4.084739,8.150438,-2.627751,5.154612,0.515124,-5.209983,6.368472,-0.420733,-6.302348,2.809383,-1.350919,5.571130,9.869932],[8.754647,-9.908825,-3.242649,6.163216,-4.506203,8.321709,-2.503373,-4.821994,-8.433532,-0.459869,-3.855830,6.876316,5.575756,-3.315584],[-6.557180,4.309342,-9.782633,-3.234099,-1.429753,-9.709637,8.952574,-2.940237,5.428196,6.397824,-1.701162,-3.089893,-2.220864,2.082748],[8.912385,-1.499026,6.979237,2.183137,5.699321,-2.437937,7.898680,-2.284987,-8.215380,-7.084161,7.173571,4.075835,-1.853232,-6.975310],[-3.495997,-4.114414,6.676770,2.813496,-3.830347,8.150574,-9.271330,9.160035,-5.102529,-0.151825,9.427731,-2.186896,-8.671548,-8.702039],[8.493197,9.786687,-1.219032,-9.623909,-4.699469,5.159619,-1.528930,-0.630254,-0.604354,0.663806,9.535743,-2.917237,-8.743465,2.913150],[-3.654990,5.666971,7.061879,7.307482,-7.054309,8.875741,9.659088,2.348791,4.802266,-6.696157,-5.611259,0.134866,-2.624276,-3.444963],[-5.527449,3.849652,8.462446,5.106886,-6.369681,5.214206,-8.322844,6.504141,4.288143,0.291986,7.324315,-8.387400,3.352118,6.051182],[8.764854,6.627502,-2.332353,7.906831,5.256487,-0.081360,8.998587,8.554159,-5.372312,-2.594272,3.381986,5.449105,7.187563,-8.051251]],[[9.089634,-4.528119,8.763345,-6.043188,4.834755,-1.255918,-6.582483,-6.927452,-3.178521,3.991195,-0.865262,-6.908114,-2.109439,-3.300953],[4.140179,-1.631541,5.902429,-8.098224,-3.139037,-5.264030,-5.772096,8.614464,9.399479,-5.315369,9.765244,-2.982019,8.002967,2.675978],[-7.489295,-1.058602,7.980869,-6.377787,8.283913,4.521861,-2.481688,8.813163,-0.586666,2.578843,-2.347541,5.291964,-0.008566,-7.666281],[-4.841039,1.683520,3.860557,7.616873,-1.686254,4.097733,-5.503021,-5.838467,-2.791097,6.291470,-6.117670,-5.743355,-5.022371,-5.284662],[-8.397999,3.761984,-2.233449,0.599225,-3.603240,-7.240256,9.297698,-9.463468,6.843456,-0.487103,9.964540,-7.264871,-5.483057,-3.310561],[9.140479,2.699435,5.415488,-4.840256,8.762773,-3.658613,-4.219348,5.506778,-7.018656,4.319660,-2.504124,-2.972599,8.005432,9.783598],[8.148379,6.139971,-6.873728,-8.288020,0.708011,4.531096,4.232508,-0.757648,4.391156,8.599977,2.696830,2.948108,-9.677563,2.735505],[-1.853324,9.607413,4.366717,-6.017715,-8.723776,5.062812,-8.430374,-8.705652,-9.915370,5.486869,-1.130645,-7.946207,-4.922362,8.682414],[6.892186,-2.534975,5.735530,2.366442,-5.874493,-0.128083,1.885009,-0.944241,3.529999,2.868981,9.008595,9.963733,1.728573,-1.948781],[8.475600,-4.268002,-4.265167,-5.769297,-3.943635,-1.514283,-3.584530,9.197213,3.588478,8.997118,6.550874,-9.106404,1.522344,-6.057203]],[[3.466294,-7.104092,0.024663,2.341872,-7.546758,8.217679,-0.918817,1.621142,6.527703,-7.612698,1.635386,9.682514,-5.976502,9.047685],[1.439617,-6.468508,-0.170430,5.266408,8.457984,-4.718828,-0.641705,-4.647914,5.060791,6.698607,4.948262,7.118042,5.381482,9.449295],[8.075835,-2.219608,-8.174346,1.255749,3.080031,-7.928397,-5.132321,-0.461712,5.560085,5.446043,1.261479,9.479828,-5.374611,6.181589],[5.693038,5.333172,2.498509,1.272015,-2.389448,7.883011,7.332894,-7.895976,-3.055172,-0.066808,8.758798,-1.805566,3.273268,9.418456],[8.260613,9.780812,6.523797,6.135357,-6.266104,1.200791,0.633968,7.634989,-3.939117,-8.432055,-6.527652,-2.174685,-3.393566,-6.770618],[-4.598783,9.382187,-4.624067,-1.278553,1.336043,2.807358,-3.392930,-8.155278,3.430072,-8.251032,3.995475,-0.920093,-3.832127,-6.433899],[6.893486,-1.647721,-0.147372,9.409120,-6.246460,1.853947,5.010908,-0.819214,5.883351,-9.912618,-7.963904,-0.606388,4.092486,2.261746],[-9.926532,6.053150,2.562492,4.649427,7.285852,-5.446462,0.836917,-9.570170,-9.956961,-1.846836,7.224237,-6.562051,-7.643274,-8.617233],[6.187910,3.800229,6.093101,-1.627939,-6.459474,-9.691347,-0.727333,9.611603,-5.852746,2.372680,-1.037012,-8.501124,-3.993735,3.502057],[-8.716804,-2.268796,-7.509402,6.506739,-4.962017,-8.170591,3.305764,3.333502,6.452115,2.974203,-1.514098,6.810646,0.763742,-8.223101]],[[-8.998409,-9.590665,5.644722,9.425991,-2.716887,3.598404,-6.933800,4.659024,1.118584,0.263482,6.088640,-7.388235,0.532443,2.102691],[-6.633334,-8.636844,4.564462,5.491562,-3.837781,-6.293999,3.530924,2.314853,5.090538,7.574531,3.406026,-0.742110,-8.661466,-4.375791],[-1.590304,-1.377638,-2.770525,4.610309,4.736406,-6.898429,8.341738,-9.403264,7.202418,-4.270365,-1.470393,9.618602,2.028654,-4.805650],[-1.213356,0.889989,-5.905873,7.746953,0.774427,8.168957,9.144490,-9.776009,-0.038154,9.820185,-7.323200,4.750394,-8.477607,1.026135],[-1.129811,0.790571,-5.787824,7.655055,-8.885560,3.228222,6.840701,-9.250662,6.708001,-7.445828,8.304818,3.801373,9.148234,-4.941822],[3.113666,3.117903,1.288086,-0.370340,-8.062677,4.704523,4.778852,-6.848747,0.429821,4.218185,6.730886,-3.036245,-4.954581,-7.731348],[-3.191118,1.734085,-0.992718,5.649519,5.298576,-1.310636,0.426785,-6.336831,-3.092897,-9.712309,8.588055,-7.260372,2.921546,0.691260],[-8.772935,0.536926,-1.155970,-5.574832,-6.206880,-8.250631,-3.256277,8.670842,-1.130517,-4.657751,-9.252901,-7.205810,-5.259024,-8.753950],[-3.209492,3.681072,5.106623,3.524703,1.473767,7.664654,-4.884866,9.033023,-5.294999,-4.187752,-7.894193,2.577937,4.681263,-1.795284],[6.182535,9.354054,-4.733662,-2.026615,-9.445446,2.576564,-2.052683,4.284075,4.349041,6.656510,1.572098,-3.440840,-1.517173,-4.794730]],[[-4.246296,1.888256,7.687299,5.220517,-6.181332,7.229810,7.668408,-7.060259,0.739677,-2.873398,2.398532,-4.009113,-8.669514,-1.898074],[2.227917,-5.467471,-0.830399,6.671010,1.553393,0.339178,-2.972757,-2.104402,-2.369077,1.290310,-3.566280,-1.647557,8.143173,-5.129983],[8.293065,-9.703597,3.615056,-0.757767,8.943381,2.851619,-2.958970,-4.480377,8.890159,7.699561,0.108699,-1.020427,-6.309063,2.818621],[3.780443,4.184022,0.563037,5.803304,4.322408,-1.035308,6.048166,7.725159,-2.921004,1.488974,-7.756011,8.175466,6.104236,9.009852],[-3.020265,-8.514405,-8.185373,9.663545,6.496848,-3.342033,-6.569949,1.794948,-5.484474,-3.216837,-8.172269,-5.517732,-8.940421,7.796898],[7.560172,8.210966,1.271727,-0.164456,-7.040898,4.664815,-9.563113,-3.407967,-4.704382,2.523600,-4.877604,-0.596061,2.441233,0.258944],[-7.944576,6.547695,4.058168,-7.849482,-0.773007,-3.022103,-8.964918,9.710157,9.629435,1.191331,5.445815,-4.579414,-6.681867,9.605628],[3.680795,0.703918,1.030689,-2.969529,-8.899336,6.166358,9.003091,4.954066,-0.747690,-3.355796,-2.542375,5.516717,-1.060428,9.744843],[-9.008070,-4.721116,8.135111,-0.502087,7.903001,5.043468,9.356781,-0.893302,-9.652347,-2.929561,-6.532037,-1.305973,-1.935520,0.321780],[2.251580,-5.750778,3.709968,7.059503,-7.203481,3.255176,-3.043511,7.259358,4.125233,-4.632486,4.425792,-4.600158,-7.094436,-6.685083]],[[6.022999,7.099600,-5.839282,-6.978967,1.331986,-3.255118,5.728571,6.036571,-7.366059,1.842733,-7.363126,6.233592,-4.075855,-6.868149],[-5.145739,-6.412417,-6.859799,-4.570662,6.952050,-8.329802,4.532845,-8.293819,-9.459840,-6.875055,6.081237,-9.417655,-7.544351,7.209147],[-8.279798,1.273719,5.709420,-9.686671,0.182672,-4.374710,3.667362,5.046097,-4.169682,-4.983490,7.564347,0.278146,-4.441948,5.719799],[-0.644107,-4.091616,-1.383425,9.551397,8.685961,6.463272,8.759502,0.513832,-2.699231,8.476809,-4.289430,1.220578,-8.805517,-6.339137],[-3.153653,7.761848,6.024601,8.729472,3.773406,4.362221,-2.167141,-3.195159,-7.884999,9.707674,-1.070009,6.133783,-2.730155,1.751405],[-6.811607,9.000097,4.200932,0.281846,-8.582311,-8.971986,8.345071,-8.116931,-5.338899,4.401407,-5.838219,2.472456,8.115021,-9.087007],[7.602816,0.353771,3.403407,-0.533355,1.409668,4.441274,2.973949,-0.379917,9.009123,-5.710238,3.808739,0.512600,-8.663472,-9.186856],[7.070626,7.566865,-2.588677,-3.929007,-4.402900,-3.987735,-0.987046,5.013664,2.112767,1.992607,9.613665,-4.127277,6.456124,-5.226276],[-2.677364,-1.967348,9.277492,-7.046253,-6.575641,-8.845481,-6.597246,-1.649080,-1.906060,-1.722319,8.186546,9.834938,7.925826,4.559971],[8.852253,4.259847,6.027624,4.031497,5.698621,-2.249461,8.557214,-1.319748,-3.156576,-8.216108,4.013170,-4.839017,-2.168518,4.917796]],[[-7.136652,9.255444,-0.140859,4.489265,-7.760930,1.868973,7.973091,8.701480,-4.873712,-4.290651,-3.859658,8.721571,3.222054,0.308911],[3.022134,2.585404,4.702636,4.154252,7.789893,0.424087,-8.134318,-9.979957,9.713704,-4.343456,5.094347,-6.672560,8.223411,8.180340],[5.030903,7.158568,3.708524,-2.878318,6.269215,7.558871,7.385627,-8.186677,1.019124,2.835624,-7.897894,-4.405174,-2.684350,7.143828],[-8.177346,-3.896517,9.402636,7.322915,-2.048185,-8.528962,6.160122,1.062079,-5.227556,-4.578761,-6.123698,-5.453765,2.019984,-8.662133],[4.945011,-8.433169,9.452477,-5.204529,-8.579012,9.122339,0.096840,-6.694923,9.164005,4.229283,4.002943,7.709255,0.055170,-4.629633],[-0.221720,-3.660781,-0.163986,-3.113430,5.238087,9.152327,-8.770532,7.443690,-2.570993,-4.739607,5.684494,7.790315,-3.284000,-1.578709],[1.628233,-5.724371,6.095294,8.791511,5.177669,3.600409,-5.098929,-4.998526,-7.758274,6.238925,6.817329,-1.237692,9.274745,8.938146],[8.999961,-4.410840,-8.080043,-0.949883,5.625650,-0.388532,7.489377,-4.354770,-1.478230,-7.082533,-8.147894,9.854062,-5.955228,-0.609542],[9.616253,9.208880,1.015178,5.082612,-2.964219,6.330803,-8.857581,4.452929,-5.108286,9.590731,-4.185506,7.886222,4.984396,5.910031],[-5.137620,-9.077516,3.169411,-5.740832,6.596051,6.565396,-5.632363,7.162172,-7.451598,-3.361208,-1.450416,9.358486,-9.407428,0.539756]],[[5.518525,6.055183,-7.154162,4.679229,7.684265,-8.212714,-5.993235,-0.931761,1.747323,4.782684,-6.386976,-6.337854,8.771307,-1.441809],[-3.228270,-2.918872,-5.799306,4.412177,7.803799,-0.249884,9.837260,8.992558,-8.245803,-6.292171,7.775737,8.394588,1.509026,8.031669],[9.083691,-3.706642,2.423218,3.310811,-5.984721,9.006213,-3.683417,-5.651418,-1.078764,6.475580,-7.918374,-5.413421,2.109029,8.459843],[2.099792,7.301446,-7.439187,-6.301863,-9.961780,5.332673,7.122610,-8.750867,4.396172,5.610110,-4.318601,-7.577946,-3.395217,3.011678],[4.774759,-7.833902,5.174307,6.208981,-9.501968,7.559341,-0.211287,2.330100,6.080857,4.000738,7.514277,8.619393,3.029498,-6.076658],[-2.847253,3.716090,-5.309541,6.105833,1.768730,-5.795552,-9.710226,7.325243,-5.386632,-8.395842,-0.382428,-1.890496,-7.332654,-2.342696],[-6.281144,0.712735,-2.763373,-9.008944,5.996248,-0.384974,-7.762222,-4.934894,-7.823310,8.591562,-3.624505,7.000310,7.693197,-3.549963],[1.451301,5.165102,7.508327,-1.039242,7.346543,7.795702,-5.537041,-4.825490,-2.106816,-4.789428,-3.565125,9.602061,8.892549,0.142863],[4.835687,0.690616,-1.906202,-9.733080,3.533569,7.284962,5.132141,6.681158,-3.013238,-3.751406,-6.761390,-9.134489,8.159787,-4.021058],[-7.745971,4.803058,5.346656,-4.098195,-9.415553,-5.335458,2.068709,-3.842733,-6.283274,6.642543,6.345435,3.970554,-1.922238,-8.375702]],[[2.851642,-6.405971,5.075584,2.425469,-6.054022,-6.215395,-8.978787,7.253939,5.560861,-1.796680,3.262562,-1.185989,-7.754587,0.212223],[8.473491,-9.327896,-3.807486,-2.417325,-7.874400,-3.395686,5.841994,6.747729,2.023133,-5.335323,1.367142,-8.689688,-1.186646,6.998819],[-0.516971,3.635863,4.917338,9.925371,-7.000446,5.444035,9.689300,-2.686870,-2.691786,5.505238,-8.390371,-4.474182,-8.841709,-8.001607],[-0.566073,6.294505,-3.854552,-4.764869,-0.521980,1.885133,-1.764485,-0.137655,0.392064,-0.325763,-4.173706,3.694280,1.715876,-1.409113],[4.779258,-2.969823,6.458557,-9.571702,-7.404404,0.090657,-4.314507,-1.463208,6.048177,9.585826,2.049275,-9.559958,0.710363,-4.067252],[-0.704468,-3.000581,6.770971,6.419369,9.592946,7.457832,-1.327830,-6.795500,3.552750,4.213667,5.895861,1.798642,9.344268,6.619573],[-2.702500,5.574397,-0.891277,-4.760540,4.349464,-6.080823,7.543149,-0.338907,-8.114129,1.059536,4.832610,-1.867460,8.994656,9.422961],[-9.488040,8.610414,-5.908502,2.414308,-0.485738,7.266770,1.671301,-2.475236,8.772652,-9.883558,-1.001727,5.465112,3.217940,-8.484668],[-8.549647,7.165534,-8.541852,2.585160,7.731884,-0.924063,-2.569219,0.451086,1.968300,-9.670152,3.581362,7.211825,-5.418174,7.225414],[-0.040779,-0.129062,-0.833696,4.988015,-5.918504,7.360824,7.960939,-4.736962,5.853444,0.903292,8.584621,7.214639,5.539650,-1.421600]],[[-5.888375,7.731743,-4.443198,6.479241,3.857945,5.529620,7.884026,7.442686,-8.081932,-4.717866,-1.707283,0.262807,5.077495,-2.515354],[7.921348,4.602739,-1.629169,-8.707127,-7.450039,8.563802,5.998751,-5.313366,-8.515942,6.789463,8.961078,-3.418104,-7.889753,8.677596],[4.837289,-5.930361,4.730799,-7.549593,-6.896342,-0.390347,-1.699582,-8.221114,-3.165524,-0.167981,-0.094091,-8.909367,3.673501,3.073872],[-7.628020,0.506620,-2.256493,-5.072105,5.871089,-9.668235,4.903353,3.191964,-4.130834,7.390865,-2.674607,6.396403,-5.386449,-6.026665],[9.795014,7.165422,-8.477771,3.701209,-4.664467,-1.904729,-2.900660,6.539822,8.311607,0.983490,-4.599483,8.163069,-8.054145,8.889480],[-0.022585,-7.567301,-3.661571,3.457839,-1.139779,7.132227,-0.751235,2.926783,-0.262679,-7.823360,2.569739,-7.834500,9.949657,-6.601485],[-8.524554,-1.802309,1.384470,-4.670459,-9.620867,-5.783661,-7.843756,9.318119,-4.550568,2.975537,5.323638,-3.611473,0.844405,-1.323490],[-2.549353,-2.178555,-9.132432,4.521682,1.589797,7.054462,9.166678,4.804835,-2.298633,-8.003805,2.190231,0.776830,-9.814339,0.232515],[-1.405452,-5.263815,-0.737460,-3.757459,4.538430,-5.646866,5.442148,-0.440683,4.745519,5.101378,-6.883733,-6.757420,3.888759,-7.655545],[-7.502845,-2.755022,0.839254,4.745572,3.699845,-0.514968,-7.606146,-1.451454,9.567545,-2.035582,-0.285239,-4.549990,-8.147075,-2.472242]],[[-9.371189,7.225641,-5.832454,-5.641120,-7.487618,6.190465,2.825389,-4.982546,-1.568803,9.187936,6.345797,-7.348917,1.463866,-6.397453],[-0.350997,-4.540132,5.969622,7.295036,0.993994,9.684593,2.334114,7.498265,-9.013803,-8.639024,-1.293813,-3.956069,-6.536841,6.654766],[6.330623,7.224965,-5.816662,3.504173,2.960038,2.235403,-4.329987,-2.265409,5.010584,-1.190627,0.016768,-9.672539,-5.519813,9.698393],[-3.162802,6.687769,-6.110234,5.056362,-0.042434,-2.732359,0.710877,-9.372539,-4.632591,1.786161,-0.005125,5.266257,5.046903,-8.874869],[7.485108,-1.300959,-6.965499,9.318838,-3.316478,-1.351119,3.281059,-7.243817,-7.357230,-0.839211,5.897324,9.620051,4.788544,8.644755],[-1.309645,1.623914,3.444124,2.158349,0.675658,-8.673457,8.484283,-3.223347,2.872617,0.552855,1.016290,-0.867801,-7.275330,-5.786696],[-7.750388,-1.568022,0.907117,-5.576362,8.516175,6.273171,8.180828,-7.708614,-1.890196,6.156968,5.582731,2.627377,2.936139,5.729782],[9.033811,4.208030,8.404583,7.925893,0.369666,0.391057,2.050666,4.832627,-1.638364,-1.661806,-8.815407,-0.230015,-2.754294,-4.278927],[5.009797,1.773192,-4.354445,-0.233011,-3.847668,-6.024631,-5.112806,-0.443484,-3.001422,-1.910950,5.244121,8.431202,-6.979177,4.314623],[-7.841082,-3.005849,8.216053,-3.363852,7.284636,4.809679,-9.195456,9.578515,3.219562,1.326174,-9.395757,-1.099122,-7.873963,3.171803]],[[3.678285,8.838375,7.762766,4.212508,-0.473717,-6.719414,8.117879,3.689178,1.063441,-6.705422,3.555693,7.921572,6.571617,3.318068],[9.333210,-3.762370,-6.121375,-2.540917,-2.289131,-0.871080,-6.035322,-0.027080,8.494976,1.558738,-0.949346,9.243091,2.811193,7.727893],[5.057494,-9.390069,-3.377821,2.112244,6.898038,-5.275152,-2.370846,-2.033231,3.017043,-8.412859,-7.182927,1.765820,5.167702,-4.896937],[0.262684,1.640086,1.773192,-0.241772,-6.826485,-7.091198,0.583485,4.880822,3.409172,-2.070831,-4.711422,6.862096,4.032399,-5.004931],[-7.326516,5.205809,-9.612732,-2.684585,0.821490,2.534700,-1.047332,5.300412,-3.425956,3.945852,-0.907692,-5.803268,-8.905745,3.761492],[5.384410,-5.669553,0.392419,0.460908,-9.864237,7.928260,-8.220720,-8.088066,-5.992946,5.644345,-8.547540,-4.738098,-1.251958,-5.740372],[1.911087,-5.149886,1.390653,-5.503502,4.752095,-3.259946,1.325583,7.869904,1.692728,-4.622417,7.354699,-4.410070,7.947390,-4.758424],[-8.094874,-4.542922,-3.721340,-5.858044,-1.269007,-4.958837,-5.195801,0.635331,-6.982424,-9.176225,-2.656558,8.774167,-2.530305,-5.997902],[7.948604,1.289445,0.143281,7.880848,6.960686,8.997415,-7.776104,8.148881,-9.957521,-2.040328,8.846289,-8.792143,5.060591,6.868235],[-9.684863,4.303863,-2.969008,2.162157,3.518269,3.963001,-7.123392,-4.022359,1.223639,7.504487,-2.127411,-1.956502,-2.616432,-3.153044]],[[1.329610,4.598914,3.025823,2.567662,-7.803067,4.861906,5.852924,-2.629317,3.993359,-3.927347,-1.846490,-7.061443,2.881547,-9.798889],[-6.945409,0.403186,-3.059920,9.298343,-4.281987,9.038938,8.059905,-6.908191,6.931406,-1.265891,4.445280,1.139061,-6.867756,-6.844532],[6.134913,-8.396693,3.880220,1.257474,-4.849234,2.276272,3.753812,2.717690,1.191411,4.540061,-3.420522,4.751931,-5.797842,6.396580],[1.119467,-9.740877,-1.011067,-8.845514,-0.069549,6.484365,-0.630378,2.362910,9.049253,-6.188301,-5.946599,-4.983163,5.344993,-2.318043],[-5.521274,-3.512335,-5.244344,-0.496246,8.880000,-8.549513,-7.190946,9.215347,7.463986,-7.929395,2.431732,4.370749,-1.838813,3.198120],[-8.159595,6.401093,0.368369,-0.018141,-2.217019,6.075476,0.687381,-9.526943,7.041483,-6.653351,-4.832077,-5.715130,0.113167,-1.706817],[8.613266,7.739025,8.395035,-7.222291,-9.933749,-3.223841,-6.372940,7.801162,-1.644008,9.712094,4.635915,-3.410379,5.628626,2.666927],[-6.458326,-8.028052,2.251358,7.210988,4.408126,-6.729196,-6.227228,-5.107155,-0.638476,-3.385104,6.049957,-3.008251,8.173502,6.600572],[0.958145,6.319846,-7.628004,2.683427,9.571657,-8.198907,9.905044,1.125926,-6.640276,-1.483093,8.907890,1.968657,-5.371276,5.532718],[-8.144664,-0.967864,1.816777,9.633846,-9.589011,-7.741050,-1.958339,-6.625019,2.186472,6.595457,8.153492,-9.848145,3.382806,-9.463457]],[[4.763263,3.186928,-7.826749,-9.204523,-1.632693,6.583047,-6.390137,-6.020839,-7.116745,-1.673018,-6.760873,2.741508,3.963243,-1.436816],[9.168625,2.193225,-4.229452,-4.754637,-4.297184,7.134631,8.454697,5.658183,-0.050866,-1.730782,-5.848072,-0.241097,-4.025482,6.918379],[1.338656,-0.977165,-5.118483,6.235431,7.751530,9.999692,-0.515016,-8.049637,0.610584,-5.542614,0.096467,-0.135693,1.837065,4.071122],[0.735775,-8.066619,-0.268236,5.223016,-2.003229,-6.483943,2.620162,2.054099,-9.820322,4.197763,-6.011372,6.136403,-9.071428,3.913178],[-4.699530,0.733444,5.701623,-1.745245,7.832820,-3.231761,-6.010207,2.576758,-0.550628,-8.951753,-4.115032,-1.158986,0.671330,-1.149046],[-4.426915,2.369685,-2.776224,-6.900748,-0.323233,-7.792403,-3.772588,4.764324,9.581810,-9.699479,-3.882403,-4.577640,-1.363034,5.074176],[-6.580787,8.215511,0.918450,1.682832,-2.311102,-2.783919,-4.564245,-6.600301,3.283771,9.596162,-8.250900,4.214285,-8.125711,5.863728],[-9.317265,-2.277228,-2.459912,4.625742,3.939706,-9.902359,-2.549738,-7.101254,4.212731,-9.083005,5.984643,8.862115,0.315567,-3.009506],[-0.034521,5.752172,-6.853302,8.427570,5.106535,-0.127495,7.207623,-4.603545,3.873222,-8.218232,9.714490,-9.673024,-2.894803,-7.371128],[-5.506682,-6.566709,-3.971340,7.397780,0.172103,-0.213518,-9.866965,3.252947,0.114313,2.811538,2.622938,2.638810,-2.401418,5.223272]],[[9.101186,6.106518,-1.468419,-4.050605,5.279475,1.979737,-2.820627,1.880178,-7.677913,-5.306494,0.690156,4.310751,2.582543,6.725336],[-1.739769,-5.955274,9.340893,2.750950,6.220622,-9.577273,7.364583,-7.103483,9.497226,-7.384690,-4.227459,6.706047,9.257184,-2.679626],[1.662183,-0.577404,-9.625528,0.929404,-2.413978,2.690423,-6.825657,-4.114613,4.317037,5.364957,4.261490,6.752617,-6.008547,7.119920],[2.497744,-4.436551,6.896314,-8.545780,-4.152132,8.063157,-0.961734,-4.437825,8.421280,-3.468794,6.407769,8.696087,-8.303042,5.832801],[-3.417032,-7.795014,-0.802951,-8.802042,5.329414,-3.659452,2.010735,9.214456,-8.964399,-3.606569,-2.977417,1.852190,3.151022,-0.510764],[4.581339,-8.568693,-8.566498,3.948178,-0.961867,6.451009,-2.246705,7.425585,9.909627,5.631651,-7.812559,4.346507,-4.922862,9.876932],[-1.173695,4.308682,5.954714,6.691132,-1.764940,-5.087235,-2.896114,7.607905,5.790257,-6.272895,3.651180,5.234661,-7.758619,-0.474913],[6.898387,-3.144675,-4.798463,2.398933,5.441137,1.810909,3.059457,-0.680574,2.358036,-3.479807,-2.946019,-6.114445,-1.787653,-8.843433],[-6.101440,0.627487,-6.888354,1.764639,-9.093382,-6.713939,2.479002,6.738460,5.503021,5.941195,0.765407,-1.451862,-6.624816,5.376076],[-8.228626,9.861417,3.923962,-3.419256,-1.682367,-9.408066,-0.763711,6.902337,-5.844495,-2.446475,-1.212884,6.925361,5.889275,-8.921940]],[[-0.381260,-3.185466,9.751253,8.508362,-4.110873,-0.224877,-3.839279,2.610946,6.571375,-2.302938,-0.111533,7.200413,-7.743667,-9.710345],[-1.329497,-3.004916,4.127421,5.117069,-5.827481,5.014763,-0.309762,-8.221968,-0.546851,2.678417,-4.295535,9.297623,-8.495223,6.267675],[7.500736,-3.070656,-8.594553,-8.684896,9.625543,-4.537962,2.185333,6.867480,7.191746,-3.269009,3.204744,2.808297,0.361808,-4.328448],[-1.381286,4.236770,-2.610575,4.907586,-6.070344,-1.809508,-4.953386,2.965619,-5.747366,4.134718,-8.059167,1.591194,-8.355808,3.412482],[4.995466,5.271572,-3.431510,-3.133261,1.301500,8.676531,3.153238,9.647221,6.207161,8.167984,6.657991,2.718425,-9.918641,-0.119845],[-7.220466,4.202563,5.180597,6.907803,0.981043,-8.383730,8.219229,-6.967324,5.975404,-7.237447,-0.248114,-2.384235,9.925118,-8.191028],[-2.783867,-7.446063,-1.693786,0.865538,-9.882457,6.012359,-0.030384,-4.273307,-2.574330,-7.174914,7.810369,-6.913894,2.888946,9.071269],[-0.133234,-2.772401,-8.847349,0.023760,-7.232525,3.118011,0.204050,-4.183596,-5.030373,-1.540041,5.490226,7.835876,0.696028,6.116366],[-9.073583,1.322716,-6.281718,-3.437589,-8.103569,3.724059,-6.403794,-9.192215,-2.084535,8.281616,9.916752,6.922693,-1.925471,0.842797],[-7.565249,-7.714413,-3.125796,8.943256,-9.540968,3.853132,-2.789020,9.558672,3.753580,-5.767843,2.139967,1.657273,8.355906,8.051976]]], dtype = "float64")#candidate|2119|(16, 10, 14)|const|float64
bop_2120 = relay.divide(const_2118.astype('float64'), const_2119.astype('float64')) # shape=(16, 10, 14)
func_2007_call = mod.get_global_var('func_2007')
func_2009_call = mutated_mod.get_global_var('func_2009')
call_2124 = relay.TupleGetItem(func_2007_call(), 0)
call_2125 = relay.TupleGetItem(func_2009_call(), 0)
output = relay.Tuple([bop_2120,call_2124,])
output2 = relay.Tuple([bop_2120,call_2125,])
func_2126 = relay.Function([], output)
mod['func_2126'] = func_2126
mod = relay.transform.InferType()(mod)
output = func_2126()
func_2127 = relay.Function([], output)
mutated_mod['func_2127'] = func_2127
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1918_call = mod.get_global_var('func_1918')
func_1919_call = mutated_mod.get_global_var('func_1919')
call_2139 = relay.TupleGetItem(func_1918_call(), 0)
call_2140 = relay.TupleGetItem(func_1919_call(), 0)
output = relay.Tuple([call_2139,])
output2 = relay.Tuple([call_2140,])
func_2145 = relay.Function([], output)
mod['func_2145'] = func_2145
mod = relay.transform.InferType()(mod)
output = func_2145()
func_2146 = relay.Function([], output)
mutated_mod['func_2146'] = func_2146
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2145_call = mod.get_global_var('func_2145')
func_2146_call = mutated_mod.get_global_var('func_2146')
call_2214 = relay.TupleGetItem(func_2145_call(), 0)
call_2215 = relay.TupleGetItem(func_2146_call(), 0)
func_2110_call = mod.get_global_var('func_2110')
func_2113_call = mutated_mod.get_global_var('func_2113')
const_2219 = relay.const([[0.180841,-7.807161,-3.438500,5.116606,-4.727157,-8.661918,-6.450410,-4.080625,-9.804733,-0.633881,-0.290215,5.742665,-2.687546,2.787000,-1.774807,5.655015,4.257983,-7.106804,1.780325,3.798811,-0.481280,-8.626284,8.984361,7.342622,-9.423081,-5.781179,1.905583,-7.154713,-7.326286,-8.416896,-9.538504,-3.340171,-0.691155,-0.865628,6.776062,9.996571,2.455395,-9.010347,-2.331956,-9.120830,4.336630,7.009793,-4.733764,1.390728,-1.322013,-4.955569,8.717907,-7.886703,2.364514,9.681395,-5.369672,-4.931761,0.921790,-3.896424,5.956812,-6.904072,8.620591,4.865803,4.122496,-7.116903,-9.941372,-3.925404,-6.023967,7.670797,4.723777,-8.328166,8.148988,-9.051906,3.264847,-1.677373,5.922686,-4.031333,5.703040,4.788183,-7.298912,-0.573624,-4.691302,-0.800661,8.163846,-3.633485,-6.267638,-3.935070,-8.828074,-5.117638,-9.809477,-6.005748,1.144861,-7.748757,-9.234603,2.830990,-6.974692,9.187598,1.271161,5.071880,-2.001166,0.115972,-7.715193,-0.020216,-2.482312,-8.426651,-6.268544,7.659870,7.023350,-6.365911,6.893254,-0.261710,6.653708,-2.179520,5.576653,9.819571,8.142635,4.860416,-1.791594,-1.249926,-1.645319,1.488942,5.292265,9.756635,6.494420,-5.755237,0.515816,-2.022033,3.303093,2.914334,-3.853400,-7.401387,-7.156461,5.219427,4.805639,6.908806,-2.057144,-7.061453,4.074554,9.980781,5.849977,4.417213,-9.874195,5.345817,-0.514419,6.285173,2.912593,0.644332,7.591009,4.857180,-4.074190,-1.297450,5.900205,4.461995,-1.710799,0.232051,-8.838463,6.242219,-8.628675,-7.160747,0.226448,6.258288,1.653290,-1.965953,5.387809,-9.505658,8.969205,6.844051,0.301105,3.479818,5.549865,-3.415533,-6.303252,-7.183686,-2.471049,5.564889,-7.480961,2.219341,1.100014,-4.001128,7.830039,3.212513,-8.673665,3.514848,8.601345,5.583681,-4.446772,-2.174404,4.566467,2.188244,-6.053606,-9.048583,-2.872284,-6.720889,6.092720,-8.842606,1.233740,3.149764,-5.237439,-1.662835,-6.501036,-8.524680,2.199366,6.044239,-1.170161,-3.334242,4.189842,3.558858,-0.531072,-6.906118,0.648703,-0.490750,-7.121779,-9.703061,8.593569,-7.013552,-8.204090,-4.562200,8.084573,2.448092,-8.985988,-9.080101,-4.152399,2.957829,-6.699351,-5.487665,7.564667,-1.074159,0.368210,-6.712596,9.662171,-4.445246,-4.227917,1.017545,-5.964274,6.866921,7.866940,-4.355266,1.838169,-1.236228,6.770330,3.300131,-8.737764,-2.987769,-8.153045,-3.879400,9.404883,-6.193303,9.483574,-2.692977,-5.543616,-0.547638,6.411740,5.735298,3.275309,-5.246090,-7.612447,0.599082,-7.085561,-0.348860,-4.939346,-9.241373,5.896302,6.714672,2.599736,-2.354700,0.037323,4.410939,-6.871377,-7.860218,-1.574745,-5.124228,-3.920136,3.465907,-1.900541,-2.536722,-2.572656,-6.526784,1.198468,-9.544816,2.940533,-1.417764,-2.824665,-6.841177,-1.861763,-2.263977,2.311201,2.368437,-6.887296,-4.320101,4.858965,8.136992,-5.247698,2.422197,-6.993339,-0.661494,7.174610,-3.111084,-4.791377,-8.161424,9.795442,3.492169,6.079344,1.778411,-1.760499,-1.175635,-9.291489,2.247786,-5.269039,-0.255200,8.369979,-2.528370,9.730146,-1.104771,5.626140,-4.329980,0.655592,-1.764565,-0.368459,-8.444169,8.817139,-5.975352,-6.971088,-3.088115,4.901707,2.526679,2.288664,0.811414,7.915399,-2.918715,-3.522742,0.161981,5.625710,-3.325790,0.790438,-8.709665,-2.676162,-3.787741,-8.050991,2.679668,7.788703,-6.679375,-4.487951,2.043752,2.949445,2.311182,-4.894410,7.667275,-8.688235,-7.132615,-8.614578,-3.392861,0.492279,-5.863330,-3.840452,1.485464,-3.306476,-6.036111,0.190605,-4.556683,-5.682929,-9.040604,2.180686,-7.271942,-5.295285,0.273008,9.325601,6.890805,8.021998,-6.924457,9.883364,6.589482,-2.175985,-1.619427,-8.801002,-5.107371,-9.690009,2.518965,6.326218,0.149030,-7.258327,-4.195742,5.655472,1.368672,4.585090,-7.209018,5.222206,4.578235,1.557925,-3.426862,-3.714582,-2.397710,4.913759,-1.169114,8.771282,-2.561716,3.042855,2.917865,-0.613113,6.242929,5.278946,-6.810687,8.657005,-0.913894,-9.565266,-0.179048,9.318058,9.357956,5.821073,9.367513,-2.614144,-6.895933,8.008466,-2.212144,-8.278182,7.650012,4.704853,2.971081,7.508668,3.503108,-4.183879,0.557324,9.985353,-6.438873,-1.344952,3.698936,-8.696184,-5.260789,-3.426241,6.099347,-2.267990,-6.421363,0.388084,7.092214,3.939869,-5.273344,-1.244311,4.516718,-4.781053,-6.867595,-1.746895,5.137653,-8.482348,-2.541376,-2.794496,4.243749,-8.371796,-7.726020,7.919005,1.953846,5.713476,-5.680754,0.941891,5.489894,-3.872239,-5.265886,8.506113,9.993223,-5.449296,-7.928570,2.099258,5.779700,4.151811,0.173677,4.859379,8.254834,-5.897794,9.052552,-0.768800,-1.336420,-0.225297,3.805579,-2.611376,1.169250,-6.438272,-6.502687,-3.629377,9.771759,4.557043,-6.287181,4.879070,5.620409,-5.747407,1.761861,7.007422,7.512593,5.124960,-4.191292,0.927606,-5.578488,5.234542,6.889152,-1.972487,-5.192508,-9.632196,9.584781,-0.912253,6.101176,7.982061,0.253225,-7.356305,-5.909083,3.901075,-2.535016,0.307675,-6.804923,6.070686,-5.740156,7.148510,9.480480,6.674597,3.158278,-7.350233,-6.677938,-1.192711,-0.213511,-6.396611,-5.921625,2.008290,-9.829607,5.874339,-4.631618,7.814761,-8.165522,4.274476,-8.954951,-8.104650,-3.330966,-3.342718,-2.584765,6.643339,-2.358749,-8.068860,3.543754,4.170528,-3.397186,8.242222,8.868546,6.730579,4.488523,5.724533,9.062866,3.994079,-3.891790,2.827401,-0.134225,-6.306218,-1.003493,1.949633,-9.577834,-5.603893,1.593920,3.412158,-3.526059,5.150158,8.977333,8.572719,-7.447052,7.929821,-1.138026,-6.481165,5.634703,4.943686,0.284077,7.390958,1.493674,-2.574997,0.196312,7.082082,-0.784251,2.255656,-6.886173,-8.377325,-2.476693,4.021668,-0.066223,5.977375,-8.357796,-0.068532,-1.053285,-3.621744,4.057788,-2.259200,-8.902044,-8.064314,-0.675424,7.443102,-9.526316,-7.514842,2.178680,0.153588,9.832366,2.510297,-3.921573,8.578760,9.740075,-4.550483,-4.594901,-7.271779,8.361139,3.881208,-2.352896,-4.216938,-5.845198,0.831235,-9.376723,-8.878222,-1.717478,-5.683630,5.851562,9.002708,4.035667,2.994607,-5.881233,-8.835589,-6.121788,-6.320300,-1.336492,4.164781,5.200143,-2.398043,6.607773,2.922058,-5.434688,-7.966665,3.193142,1.435026,-7.410166,-4.034461,-3.321959,-2.362115,-1.216878,3.763179,2.337683,7.868028,-2.845500,-1.028585,-1.982154,1.510088,4.282921,-0.348299,4.060173,4.877479,-2.142514,-5.277534,5.539734,7.007624,1.522578,-8.445140,5.500100,7.103618,-9.198851,-2.912961,1.783212,7.964577,8.194946,5.993164,0.842455,-5.534460,-9.104520,-3.521301,8.025311,2.730777,9.528879,0.747567,-2.400191,-3.507493,0.280736,2.886200,-2.947361,5.422259,9.944405,-3.241714,-0.865331,-7.014669,7.974097,-4.130936,7.186795,-0.407749,8.585199,7.288078,-0.118808,-3.977182,-2.789877,1.210525,6.813844,9.886365,5.821520,5.715052,-2.665760,5.103953,1.199106,4.175586,5.288026,2.265082,2.470669,-6.233620,-2.264587,9.678085,7.407735,0.636126,-7.901374,7.936470,-2.398915,0.117509,-0.604991,-0.784792,-0.593725,-9.516696,6.702031,-3.624313,9.678176,0.854637,-4.715730,-9.471096,7.157358,-0.883307,-8.181471,7.387470,-4.564767,-7.253278,8.493123,-9.310990,-0.705432,-9.997122,-0.050156,-4.132735,8.374580,5.936251,6.176569,4.433442,2.718088,-4.799249,5.372590,-1.576320,-4.515148,2.106847,-6.071590,0.673808,-5.821483,-5.756301,-7.557692,-3.009268,-3.723684,4.889648,-5.551080,-7.990881,-5.000518,9.625833,5.860229,-7.528735,-5.914879,8.210911,1.337634,4.908016,-9.183468,7.848459,6.469981,9.774163,1.775224,3.067122,8.367360,-4.302548,-3.180214,-0.796489,4.251951,2.396838,-2.886070,-9.423551,4.710657,8.644471,-7.234238,-1.134315,6.299452,3.162181,3.246198,-1.661517,4.675797,-2.285494,-3.514246,6.262609,7.828360,-3.984873,3.488953,-2.987074,-6.996829,0.967522,-2.715037,-6.604016,3.981702,-4.077298,-5.457710,4.517442,0.043276,9.668148,-7.171748,-3.986022,8.291956,3.380807,8.244481,7.810268,-1.656988,-9.653401,1.479244,-3.451354,3.213225,8.686515,6.164525,4.200265,-1.748622,-2.650353,1.692238,2.973448,8.861148,2.382348,-5.187118,1.158772,9.714488,4.335730,-0.843070,4.685925,-6.130888,-9.548411,-4.996666,5.438840,-6.057827,1.517046,-7.914349,1.937606,-0.874196,-7.313999,6.111067,7.931338,-7.604171,0.836422,-7.974154,-4.656057,4.985954,-4.928357,-7.000495,4.542627,1.629140,-3.433496,2.085011,-1.858877,-7.370716,-1.540687,-2.476988,2.156030,-9.712212,7.307012,9.685603,8.564103,-0.390208,-9.113523,5.585682,-9.867988,9.744683,-9.380951,-6.589940,-8.333835,-3.432611,-2.393827,-9.377335,3.749533,3.527208,7.054106,-1.872834,3.280949,-3.921213,9.131355,2.038467,-0.360806,-5.379018,0.623671,0.972474,1.923879,-4.432346,-1.983676,9.409983,2.886802,7.190521,-0.010789,-5.011485,-6.940974,8.668108]], dtype = "float64")#candidate|2219|(1, 880)|const|float64
call_2218 = relay.TupleGetItem(func_2110_call(relay.reshape(const_2219.astype('float64'), [16, 11, 5])), 2)
call_2220 = relay.TupleGetItem(func_2113_call(relay.reshape(const_2219.astype('float64'), [16, 11, 5])), 2)
func_543_call = mod.get_global_var('func_543')
func_544_call = mutated_mod.get_global_var('func_544')
call_2225 = relay.TupleGetItem(func_543_call(), 1)
call_2226 = relay.TupleGetItem(func_544_call(), 1)
output = relay.Tuple([call_2214,call_2218,const_2219,call_2225,])
output2 = relay.Tuple([call_2215,call_2220,const_2219,call_2226,])
func_2246 = relay.Function([], output)
mod['func_2246'] = func_2246
mod = relay.transform.InferType()(mod)
mutated_mod['func_2246'] = func_2246
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2246_call = mutated_mod.get_global_var('func_2246')
call_2247 = func_2246_call()
output = call_2247
func_2248 = relay.Function([], output)
mutated_mod['func_2248'] = func_2248
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2249 = relay.var("var_2249", dtype = "int16", shape = (13, 5, 16))#candidate|2249|(13, 5, 16)|var|int16
var_2250 = relay.var("var_2250", dtype = "int16", shape = (13, 5, 16))#candidate|2250|(13, 5, 16)|var|int16
bop_2251 = relay.equal(var_2249.astype('bool'), relay.reshape(var_2250.astype('bool'), relay.shape_of(var_2249))) # shape=(13, 5, 16)
bop_2256 = relay.left_shift(bop_2251.astype('uint32'), relay.reshape(var_2250.astype('uint32'), relay.shape_of(bop_2251))) # shape=(13, 5, 16)
func_916_call = mod.get_global_var('func_916')
func_918_call = mutated_mod.get_global_var('func_918')
call_2260 = relay.TupleGetItem(func_916_call(), 1)
call_2261 = relay.TupleGetItem(func_918_call(), 1)
func_989_call = mod.get_global_var('func_989')
func_991_call = mutated_mod.get_global_var('func_991')
call_2284 = relay.TupleGetItem(func_989_call(), 2)
call_2285 = relay.TupleGetItem(func_991_call(), 2)
uop_2289 = relay.atanh(var_2249.astype('float64')) # shape=(13, 5, 16)
func_1234_call = mod.get_global_var('func_1234')
func_1237_call = mutated_mod.get_global_var('func_1237')
const_2292 = relay.const([-1,-10,-4,10,8,1,-5,-7,-4,7,4,-6,9,1,6,-7,-4,-7,-3,6,8,9,2,-2,-7,-4,10,1,-9,-9,6,-10,-3,9,-6,7,-4,-7,-2,-3,-10,1,-9,1,-5,-3,-6,-1,1,-5,5,-9,10,-5,7,-3,-5,10,9,3,2,6,8,9,7,4,-9,3,1,2,-6,-6,9,6,-7,-1,3,-9,7,10,-5,8,-9,1,-8,9,-8,-4,1,7,9,9,7,4,-7,8,1,5,-6,2,-1,-6,6,-10,-2,-4,-4,4,10,-5,-4,-10,10,7,-4,-10,9,-6,7,-3,10,1,-10,-5,-5,-1,5,6,-7,-1,-1,7,-6,5,8,4,5,4,-2,-8,-1,-8,10,-2,-6,-7,-2,6,-7,3,7,5,-5,-9,-2,-4,8,1,-5,-7,6,7,-8,9,-4,-5,2,-4,1,-3,-2,5,-8,-8,-1,-5,8,-6,5,-6,-8,9,-10,-6,-8,-3,-4,10,7,9,4,-3,-8,-3,-6,3,9,-3,-8,-2,-6,5,-5,5,5,-8,-10,3,1,4,-4,-1,-2,6,3,-4,-2,10,8,-7,-9,-3,-5,-8,2,-4,-10,3,-9,-2,6,-1,7,-6,-5,7,10,-5,-6,-3,-9,-9,2,-1,-1,-5,-8,-5,-6,-9,6,8,-6,10,8,-4,-10,5,5,7,10,-2,6,5,-8,6,-10,9,7,-10,3,-1,-5,7,4,-5,-5,5,4,-5,2,-10,4,-8,9,6,-2,-6,-5,8,-8,8,-3,5,2,-2,9,-9,-1,6,7,-5,10,9,-6,-9,-1,8,-9,-1,-10,5,7,6,1,10,-3,8,-6,-1,3,9,-4,-9,-9,-3,-5,2,-2,-2,8,10,8,-5,4,-9,5,-10,4,-3,10,-3,4,-1,-4,9,6,3,9,8,-5,10,-4,10,-2,2,1,-10,-3,-3,-3,-6,4,-3,-9,-8,-8,6,-3,-4,9,8,3,7,9,10,-4,1,8,-3,-2,3,1,6,4,-8,7,-5,4,-4,-3,4,-3,-5,6,-7,-1,2,8,6,9,-8,-2,5,-6,8,5,7,7,-8,10,-3,8,2,5,-1,-4,9,2,1,-6,9,2,-9,8,4,-7,-10,4,2,-4,4,-1,-3,10,3,4,7,-8,7,-8,-5,-9,1,-8,5,-5,9,5,-1,7,-10,9,-9,4,4,-8,-6,-5,4,-9,7,-9,1,10,8,-9,-10,-6,5,6,3,-10,5,-5,1,8,-9,4,-1], dtype = "uint16")#candidate|2292|(480,)|const|uint16
call_2291 = relay.TupleGetItem(func_1234_call(relay.reshape(const_2292.astype('uint16'), [480,]), relay.reshape(const_2292.astype('uint64'), [6, 5, 16]), ), 2)
call_2293 = relay.TupleGetItem(func_1237_call(relay.reshape(const_2292.astype('uint16'), [480,]), relay.reshape(const_2292.astype('uint64'), [6, 5, 16]), ), 2)
bop_2305 = relay.bitwise_or(uop_2289.astype('int32'), relay.reshape(bop_2251.astype('int32'), relay.shape_of(uop_2289))) # shape=(13, 5, 16)
var_2314 = relay.var("var_2314", dtype = "bool", shape = (13, 5, 16))#candidate|2314|(13, 5, 16)|var|bool
bop_2315 = relay.logical_xor(bop_2251.astype('int8'), relay.reshape(var_2314.astype('int8'), relay.shape_of(bop_2251))) # shape=(13, 5, 16)
output = relay.Tuple([bop_2256,call_2260,call_2284,call_2291,const_2292,bop_2305,bop_2315,])
output2 = relay.Tuple([bop_2256,call_2261,call_2285,call_2293,const_2292,bop_2305,bop_2315,])
func_2319 = relay.Function([var_2249,var_2250,var_2314,], output)
mod['func_2319'] = func_2319
mod = relay.transform.InferType()(mod)
var_2320 = relay.var("var_2320", dtype = "int16", shape = (13, 5, 16))#candidate|2320|(13, 5, 16)|var|int16
var_2321 = relay.var("var_2321", dtype = "int16", shape = (13, 5, 16))#candidate|2321|(13, 5, 16)|var|int16
var_2322 = relay.var("var_2322", dtype = "bool", shape = (13, 5, 16))#candidate|2322|(13, 5, 16)|var|bool
output = func_2319(var_2320,var_2321,var_2322,)
func_2323 = relay.Function([var_2320,var_2321,var_2322,], output)
mutated_mod['func_2323'] = func_2323
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1091_call = mod.get_global_var('func_1091')
func_1093_call = mutated_mod.get_global_var('func_1093')
call_2363 = relay.TupleGetItem(func_1091_call(), 1)
call_2364 = relay.TupleGetItem(func_1093_call(), 1)
output = call_2363
output2 = call_2364
func_2389 = relay.Function([], output)
mod['func_2389'] = func_2389
mod = relay.transform.InferType()(mod)
output = func_2389()
func_2390 = relay.Function([], output)
mutated_mod['func_2390'] = func_2390
mutated_mod = relay.transform.InferType()(mutated_mod)
func_543_call = mod.get_global_var('func_543')
func_544_call = mutated_mod.get_global_var('func_544')
call_2445 = relay.TupleGetItem(func_543_call(), 1)
call_2446 = relay.TupleGetItem(func_544_call(), 1)
func_833_call = mod.get_global_var('func_833')
func_836_call = mutated_mod.get_global_var('func_836')
var_2460 = relay.var("var_2460", dtype = "float64", shape = (39,))#candidate|2460|(39,)|var|float64
call_2459 = relay.TupleGetItem(func_833_call(relay.reshape(var_2460.astype('float64'), [3, 13, 1])), 1)
call_2461 = relay.TupleGetItem(func_836_call(relay.reshape(var_2460.astype('float64'), [3, 13, 1])), 1)
output = relay.Tuple([call_2445,call_2459,var_2460,])
output2 = relay.Tuple([call_2446,call_2461,var_2460,])
func_2462 = relay.Function([var_2460,], output)
mod['func_2462'] = func_2462
mod = relay.transform.InferType()(mod)
var_2463 = relay.var("var_2463", dtype = "float64", shape = (39,))#candidate|2463|(39,)|var|float64
output = func_2462(var_2463)
func_2464 = relay.Function([var_2463], output)
mutated_mod['func_2464'] = func_2464
mutated_mod = relay.transform.InferType()(mutated_mod)
func_609_call = mod.get_global_var('func_609')
func_611_call = mutated_mod.get_global_var('func_611')
call_2488 = relay.TupleGetItem(func_609_call(), 0)
call_2489 = relay.TupleGetItem(func_611_call(), 0)
func_2319_call = mod.get_global_var('func_2319')
func_2323_call = mutated_mod.get_global_var('func_2323')
const_2507 = relay.const([-10,-5,-5,-3,-3,-6,5,-8,-6,-3,-8,9,3,6,8,2,8,-9,4,7,6,4,5,-2,-4,3,-4,-4,2,4,-3,-9,8,7,-1,1,8,-9,-9,5,-8,5,-1,-2,7,2,-4,5,9,6,-6,7,2,6,9,-5,10,-2,9,3,-9,9,5,7,-6,6,-2,6,1,7,3,-8,2,-1,5,10,-10,9,-3,-9,-1,-2,8,-7,10,-10,6,6,-9,10,3,-7,-8,-8,5,3,4,9,5,-10,9,-8,9,4,10,-9,-3,6,5,6,3,7,7,9,1,-7,-1,-7,8,6,5,-3,-6,-2,6,2,-9,7,5,8,-7,-8,9,-9,-7,8,-2,10,3,10,2,-9,9,7,-3,-9,9,9,3,8,4,-1,7,4,-3,-7,6,-6,-3,-8,7,7,5,5,-5,-9,8,-5,1,-3,6,1,-8,-7,-9,7,2,-3,9,6,-2,-3,5,5,9,-4,2,7,2,10,8,-9,-9,-7,2,-4,-10,-7,5,3,-2,9,2,-1,-1,-6,-10,7,-7,10,10,6,-1,5,2,1,6,-7,7,1,-1,-5,9,-10,8,6,4,-8,-2,10,-2,10,-1,4,-7,6,-3,-10,-4,-9,-10,10,8,10,2,5,-1,2,4,-1,-5,10,9,10,-10,-8,5,-6,-8,4,6,-4,6,8,3,2,8,4,4,3,-5,4,-8,5,-7,-4,8,-10,3,6,-9,4,2,7,1,10,8,8,-6,-10,1,6,3,4,5,-3,-10,-4,-4,10,10,3,-6,3,-3,-7,-8,-4,10,-10,7,7,-10,-2,1,-2,-4,8,6,-3,4,-1,-4,5,2,7,9,-7,-7,5,-2,9,-2,7,-8,-4,2,-5,2,-2,-3,4,-5,3,1,-1,5,-9,9,-4,6,-7,5,7,-2,-2,8,-7,6,-6,-7,9,9,8,6,4,2,-2,-3,-6,10,10,-3,-2,8,-5,-6,-7,-6,2,-7,-4,8,-7,7,-6,3,-4,2,5,-5,-4,-9,-6,6,-7,-4,1,8,-3,-3,-1,-4,5,2,-7,-4,-8,2,8,-1,10,-5,-7,10,10,-8,4,-8,9,8,-9,-9,-7,-10,-10,9,8,2,9,-5,9,-9,-7,-1,9,6,-4,-6,7,-6,-8,-6,1,2,-2,-10,-4,2,-8,-10,4,4,1,7,-5,-5,-9,9,-1,-1,-10,3,-10,5,-8,4,3,10,-7,3,1,4,3,10,-4,6,-2,10,-4,9,-2,-5,-10,-10,-3,6,1,4,3,7,-4,5,-1,-7,10,6,8,6,6,2,8,-3,-8,-4,-2,-10,3,-2,10,7,5,1,-5,-9,4,-10,9,-3,10,-10,8,1,-5,6,-2,5,-8,-1,5,2,1,-2,-5,9,-2,-10,-9,2,3,9,-10,-5,1,9,-7,-5,-5,1,4,7,-1,4,9,-3,-3,10,-9,2,-4,-7,-6,-9,1,-2,4,-9,-8,2,-1,2,9,9,-8,7,-6,2,7,4,5,-3,5,1,-6,-3,-10,-5,8,7,7,-7,-10,-6,2,5,5,-6,9,-6,-10,4,-5,-9,2,-6,-1,3,-5,6,-8,5,-10,-4,8,-4,2,-8,-6,7,-2,7,7,5,-9,-9,4,10,7,-3,-7,-3,6,3,10,-9,2,-6,-8,-3,3,-5,10,-1,1,-1,-2,5,-8,9,8,-8,6,3,6,10,-10,6,-10,6,-2,10,-1,-1,5,7,-10,8,-1,-7,-7,-8,-3,8,1,7,-10,9,-1,-2,-2,2,4,-5,10,-3,2,5,-6,-1,6,-4,2,-8,4,1,-7,-8,-4,-7,9,-3,-3,-6,-3,8,4,4,5,-1,1,7,-7,-10,-1,7,-7,1,-1,9,-6,3,-8,6,-8,4,-8,-9,9,-8,-4,-10,-7,3,8,4,-10,3,-4,3,5,1,-2,8,10,4,1,7,5,-8,1,-8,-6,8,8,-2,-3,-6,-5,-6,2,-9,4,-3,-5,1,-2,6,7,-8,7,10,4,5,-2,-4,-1,-9,10,-3,2,10,2,-2,2,-8,1,-9,3,4,-4,-2,-5,9,1,-10,-5,-7,-8,8,8,-9,3,3,3,-3,-8,-2,-4,-8,-3,9,1,-5,-4,9,6,-2,7,6,3,-6,2,5,9,4,4,-9,1,3,6,9,1,10,-5,7,6,2,-9,8,2,9,-5,-2,2,-2,-9,-10,-2,-8,9,-6,9,2,5,-8,-2,-5,-5,1,-2,6,4,10,6,-3,-5,7,9,2,1,-2,-8,8,-2,1,-2,3,-2,-1,3,3,-5,10,4,-9,-3,-8,6,4,-4,9,-3,5,-7,4,-2,-8,1,-2,-3,10,10,6,-3,-3,7,-7,6,6,8,-7,-8,7,4,-6,8,4,-3,5,3,5,10,10,3,3,-5,2,-5,7,-8,-10,-9,6,5,8,-7,-7,6,-7,3,-2,10,6,-1,-9,-3,5,1,4,1,5,-6,7,10,-2,-3,1,-6,-9,7,-8,-6,4,4,-5,-1,-5,3,-2,-5,5,-9,-9,3,-6,7,3,-6,-3,7,5,8,-7,-1,5,-3,4,-7,1,-5,10,-10,5,10,-6,8,4,-3,-9,10,-2,4,-7,1,1,-2,7,-2,7,2,10,7,6,-5,-4,-10,-7,2,-7,1,-6,7,-4,8,4,7,8,5,3,10,6,4,6,7,-1,-1,1,10,8,1], dtype = "int16")#candidate|2507|(1040,)|const|int16
call_2506 = relay.TupleGetItem(func_2319_call(relay.reshape(const_2507.astype('int16'), [13, 5, 16]), relay.reshape(const_2507.astype('int16'), [13, 5, 16]), relay.reshape(const_2507.astype('bool'), [13, 5, 16]), ), 2)
call_2508 = relay.TupleGetItem(func_2323_call(relay.reshape(const_2507.astype('int16'), [13, 5, 16]), relay.reshape(const_2507.astype('int16'), [13, 5, 16]), relay.reshape(const_2507.astype('bool'), [13, 5, 16]), ), 2)
func_2319_call = mod.get_global_var('func_2319')
func_2323_call = mutated_mod.get_global_var('func_2323')
call_2528 = relay.TupleGetItem(func_2319_call(relay.reshape(const_2507.astype('int16'), [13, 5, 16]), relay.reshape(const_2507.astype('int16'), [13, 5, 16]), relay.reshape(const_2507.astype('bool'), [13, 5, 16]), ), 6)
call_2529 = relay.TupleGetItem(func_2323_call(relay.reshape(const_2507.astype('int16'), [13, 5, 16]), relay.reshape(const_2507.astype('int16'), [13, 5, 16]), relay.reshape(const_2507.astype('bool'), [13, 5, 16]), ), 6)
func_1918_call = mod.get_global_var('func_1918')
func_1919_call = mutated_mod.get_global_var('func_1919')
call_2536 = relay.TupleGetItem(func_1918_call(), 0)
call_2537 = relay.TupleGetItem(func_1919_call(), 0)
func_507_call = mod.get_global_var('func_507')
func_508_call = mutated_mod.get_global_var('func_508')
call_2543 = func_507_call()
call_2544 = func_507_call()
func_1451_call = mod.get_global_var('func_1451')
func_1454_call = mutated_mod.get_global_var('func_1454')
const_2550 = relay.const([-9,-5,-3,9,-10,-4,5,4,-8,7,-4,9,7,-10,-2,-6,-4,-5,2,8,10,-8,10,4,-6,-2,-6,-4,9,-3,5,-3,2,5,3,-7,-7,-9,-6,-5,-7,-7,-7,7,-2,-8,-10,5,-2,-8,-6,-9,2,8,-4,4,-1,4,9,6,2,10,7,-5,-8,4,-10,6,3,-1,8,-8,-4,7,-4,9,-6,-7,4,2], dtype = "uint16")#candidate|2550|(80,)|const|uint16
call_2549 = relay.TupleGetItem(func_1451_call(relay.reshape(const_2550.astype('uint16'), [80,])), 4)
call_2551 = relay.TupleGetItem(func_1454_call(relay.reshape(const_2550.astype('uint16'), [80,])), 4)
bop_2556 = relay.minimum(call_2543.astype('uint32'), relay.reshape(call_2488.astype('uint32'), relay.shape_of(call_2543))) # shape=(3, 8, 9)
bop_2559 = relay.minimum(call_2544.astype('uint32'), relay.reshape(call_2489.astype('uint32'), relay.shape_of(call_2544))) # shape=(3, 8, 9)
output = relay.Tuple([call_2506,const_2507,call_2528,call_2536,call_2549,const_2550,bop_2556,])
output2 = relay.Tuple([call_2508,const_2507,call_2529,call_2537,call_2551,const_2550,bop_2559,])
func_2560 = relay.Function([], output)
mod['func_2560'] = func_2560
mod = relay.transform.InferType()(mod)
output = func_2560()
func_2561 = relay.Function([], output)
mutated_mod['func_2561'] = func_2561
mutated_mod = relay.transform.InferType()(mutated_mod)
func_949_call = mod.get_global_var('func_949')
func_951_call = mutated_mod.get_global_var('func_951')
call_2562 = relay.TupleGetItem(func_949_call(), 0)
call_2563 = relay.TupleGetItem(func_951_call(), 0)
output = relay.Tuple([call_2562,])
output2 = relay.Tuple([call_2563,])
func_2564 = relay.Function([], output)
mod['func_2564'] = func_2564
mod = relay.transform.InferType()(mod)
mutated_mod['func_2564'] = func_2564
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2564_call = mutated_mod.get_global_var('func_2564')
call_2565 = func_2564_call()
output = call_2565
func_2566 = relay.Function([], output)
mutated_mod['func_2566'] = func_2566
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1002_call = mod.get_global_var('func_1002')
func_1004_call = mutated_mod.get_global_var('func_1004')
call_2710 = func_1002_call()
call_2711 = func_1002_call()
func_2564_call = mod.get_global_var('func_2564')
func_2566_call = mutated_mod.get_global_var('func_2566')
call_2713 = relay.TupleGetItem(func_2564_call(), 0)
call_2714 = relay.TupleGetItem(func_2566_call(), 0)
uop_2719 = relay.rsqrt(call_2713.astype('float32')) # shape=(1, 2, 10)
uop_2721 = relay.rsqrt(call_2714.astype('float32')) # shape=(1, 2, 10)
func_1536_call = mod.get_global_var('func_1536')
func_1540_call = mutated_mod.get_global_var('func_1540')
var_2723 = relay.var("var_2723", dtype = "float64", shape = (720,))#candidate|2723|(720,)|var|float64
const_2724 = relay.const([4.202847,8.158017,7.196771,4.047500,7.199293,3.725212,5.487691,-3.146587,8.593990,7.005469,3.262907,7.329752,-7.025706,-6.560650,-8.805638,3.285617,7.024640,4.182707,7.967469,-7.391464,1.919781,6.782793,4.078473,0.123472,3.346456,-0.480628,8.681758,4.574056,-4.963051,7.529300,2.006029,-8.817074,-4.361240,5.095226,-7.130943,-3.833256,2.011819,-4.148569,8.399884], dtype = "float64")#candidate|2724|(39,)|const|float64
call_2722 = relay.TupleGetItem(func_1536_call(relay.reshape(var_2723.astype('float64'), [15, 16, 3]), relay.reshape(call_2710.astype('bool'), [216,]), relay.reshape(const_2724.astype('float64'), [39,]), ), 0)
call_2725 = relay.TupleGetItem(func_1540_call(relay.reshape(var_2723.astype('float64'), [15, 16, 3]), relay.reshape(call_2710.astype('bool'), [216,]), relay.reshape(const_2724.astype('float64'), [39,]), ), 0)
func_638_call = mod.get_global_var('func_638')
func_640_call = mutated_mod.get_global_var('func_640')
call_2726 = func_638_call()
call_2727 = func_638_call()
bop_2732 = relay.logical_and(call_2713.astype('bool'), relay.reshape(uop_2719.astype('bool'), relay.shape_of(call_2713))) # shape=(1, 2, 10)
bop_2735 = relay.logical_and(call_2714.astype('bool'), relay.reshape(uop_2721.astype('bool'), relay.shape_of(call_2714))) # shape=(1, 2, 10)
output = relay.Tuple([call_2710,call_2722,var_2723,const_2724,call_2726,bop_2732,])
output2 = relay.Tuple([call_2711,call_2725,var_2723,const_2724,call_2727,bop_2735,])
func_2741 = relay.Function([var_2723,], output)
mod['func_2741'] = func_2741
mod = relay.transform.InferType()(mod)
var_2742 = relay.var("var_2742", dtype = "float64", shape = (720,))#candidate|2742|(720,)|var|float64
output = func_2741(var_2742)
func_2743 = relay.Function([var_2742], output)
mutated_mod['func_2743'] = func_2743
mutated_mod = relay.transform.InferType()(mutated_mod)
func_638_call = mod.get_global_var('func_638')
func_640_call = mutated_mod.get_global_var('func_640')
call_2748 = func_638_call()
call_2749 = func_638_call()
func_1816_call = mod.get_global_var('func_1816')
func_1818_call = mutated_mod.get_global_var('func_1818')
const_2756 = relay.const([[-4.282738,-5.458272],[1.121766,7.523147],[1.124899,-0.080709],[0.881493,6.116558],[-1.937368,-7.833057],[-5.525233,-8.572925],[-6.838677,-5.256325],[8.885449,-6.951545],[-9.182749,2.375177],[7.398406,-0.107498],[9.388419,-9.617280],[6.901627,1.642895],[9.603322,-9.211427],[-1.042774,3.220748]], dtype = "float64")#candidate|2756|(14, 2)|const|float64
call_2755 = relay.TupleGetItem(func_1816_call(relay.reshape(const_2756.astype('float64'), [28,])), 0)
call_2757 = relay.TupleGetItem(func_1818_call(relay.reshape(const_2756.astype('float64'), [28,])), 0)
func_255_call = mod.get_global_var('func_255')
func_257_call = mutated_mod.get_global_var('func_257')
call_2761 = func_255_call()
call_2762 = func_255_call()
func_1536_call = mod.get_global_var('func_1536')
func_1540_call = mutated_mod.get_global_var('func_1540')
var_2768 = relay.var("var_2768", dtype = "float64", shape = (720,))#candidate|2768|(720,)|var|float64
var_2769 = relay.var("var_2769", dtype = "float64", shape = (39,))#candidate|2769|(39,)|var|float64
call_2767 = relay.TupleGetItem(func_1536_call(relay.reshape(var_2768.astype('float64'), [15, 16, 3]), relay.reshape(call_2761.astype('bool'), [216,]), relay.reshape(var_2769.astype('float64'), [39,]), ), 3)
call_2770 = relay.TupleGetItem(func_1540_call(relay.reshape(var_2768.astype('float64'), [15, 16, 3]), relay.reshape(call_2761.astype('bool'), [216,]), relay.reshape(var_2769.astype('float64'), [39,]), ), 3)
func_2319_call = mod.get_global_var('func_2319')
func_2323_call = mutated_mod.get_global_var('func_2323')
const_2772 = relay.const([[9,2,10,7,-2,3,-8,3,3,-3,4,-3,-5,10,6,-7,6,3,5,-10,-6,-3,9,8,-4,9,3,6,-8,5,-6,10,-2,-8,2,-4,-2,-5,-2,4,-8,-8,2,6,-2,-5,3,-2,6,-2,9,-1,4,3,10,4,8,-8,7,10,7,10,9,-7,-6,-7,6,6,-3,7,-4,-1,4,3,-3,3,-10,-2,-6,6,-9,-7,-1,6,-1,7,-8,10,-8,-5,9,1,-10,-8,1,8,-9,4,7,-1,-4,6,7,-4,-10,-5,5,-8,-10,-1,10,-10,4,8,3,2,10,-9,-5,-3,2,-3,6,1,-8,7,-4,9,-1,3,-8,5,-2,-8,-7,-1,-9,-5,-6,10,-1,-3,4,-4,1,-2,2,-1,-10,-1,-8,-6,-7,-1,-7,8,-8,2,-5,6,4,6,-5,-10,4,4,6,-8,-10,7,-9,-7,5,8,6,5,2,-5,6,2,7,-1,-5,-5,9,-6,6,-5,1,-3,9,-6,-1,10,6,-7,-9,5,1,-10,-1,-9,8,-10,-9,-7,-2,9,-3,1,2,-4,10,4,-9,-10,-1,-9,-4,1,3,2,-10,-1,4,4,-9,5,-8,-1,-3,9,-9,-6,-9,-8,4,10,-5,-9,-2,-2,-3,-2,-6,-8,-1,7,-5,-5,-10,7,-5,8,-7,-6,3,-9,5,-7,-2,3,2,-5,3,-1,5,6,4,-9,-2,9,-2,-10,-10,9,-2,7,-10,-2,4,-5,1,10,-5,6,3,1,-2,2,9,-3,-4,6,-3,-9,10,-8,5,-4,-9,8,-6,7,3,1,3,-3,-4,-2,-5,-6,5,6,3,2,2,4,-10,-7,2,-3,2,3,4,3,-4,-6,6,-1,-4,1,-3,-6,-7,4,-9,-6,4,6,-5,-9,1,-10,-7,-4,-3,9,-1,7,-5,9,9,-6,-7,2,3,-2,7,1,-2,7,1,9,10,-4,-8,-1,-10,-3,1,-8,-7,1,4,-9,9,2,-3,-4,1,-8,-10,-8,-9,-9,4,-7,10,8,1,10,5,-2,7,1,-5,-6,9,-7,-3,-9,4,2,5,9,9,-8,3,3,5,7,3,6,7,8,-10,1,-2,-1,4,3,-9,-8,-8,-2,4,-4,7,9,-5,-8,-2,2,-3,-1,1,8,4,2,-8,-6,8,-1,3,-8,5,-5,4,-2,-10,-4,6,3,-10,3,-1,-2,10,5,1,2,-9,4,-4,-2,9,5,8,7,-5,5,9,7,9,5,-5,-8,5,2,10,4,-8,7,9,5,4,9,7,5,8,-10,10,-1,-9,6,5,-9,3,2,-1,5,6,9,4,3,-7,-6,10,3,8,-9,1,9,-3,5,7,9,8,9,5,1,-5,-10,4,-4,-3,7,-10,-8,-7,-7,3,-6,-4,-10,-8,-1,-9,8,4,-6,-7,-1,-9,-10,-9,1,-2,2,3,-7,6,6,8,-9,-7,9,9,-9,-8,7,5,-1,4,-5,7,9,-9,-9,8,9,-6,-9,10,-7,6,-6,-1,-8,-2,5,-2,-5,9,9,-5,-3,9,-7,-10,9,-8,7,-4,8,7,-7,8,-1,7,4,-8,-4,9,-8,-6,6,-2,5,9,1,-7,-6,-10,3,7,-1,4,-4,5,-3,8,6,4,7,-5,9,5,-8,-2,-4,8,-4,9,7,-1,-6,4,3,3,1,-6,-1,-6,8,10,7,-7,2,10,-3,-4,3,1,5,-4,4,-7,-5,-6,10,-6,5,9,-9,-9,-1,-1,2,-10,10,3,6,-10,2,-3,-1,-9,-2,6,-9,-6,-9,-5,-1,-5,-9,-4,8,-5,10,-5,6,-7,-2,2,9,2,-4,-8,1,7,-4,6,-5,-4,-10,-5,-3,-7,-9,-8,6,6,-6,7,8,9,5,5,8,-6,-8,-7,7,-6,4,5,-6,1,5,-1,-2,-6,6,8,1,-2,-6,10,2,10,-1,-5,-3,-9,4,3,8,2,9,10,5,8,1,-7,-3,-1,1,1,2,-4,10,2,-5,4,8,3,-7,7,9,3,10,-8,9,4,-1,-8,4,-1,-6,-4,-10,-8,-9,3,8,2,9,8,1,-7,-10,5,5,-4,10,5,-4,7,7,-1,-5,2,5,1,-2,10,3,8,3,1,10,5,1,9,-1,3,-5,1,-7,-8,1,2,5,-4,-2,2,-2,-9,-7,1,1,6,-10,-8,9,7,3,-4,7,-5,-4,2,3,7,10,-10,3,-8,10,2,-9,-9,-8,9,4,6,-2,-4,-10,7,-10,-2,10,5,-6,-3,-6,7,7,9,3,-1,-4,2,-7,-5,-5,-1,-8,8,3,-1,4,-1,8,-4,5,-8,10,4,-10,-6,7,1,-4,-3,2,4,-4,9,-4,2,10,-10,-9,-8,3,-1,3,-10,-5,-2,7,-3,2,2,6,-7,4,-7,-10,-10,-10,5,-7,10,8,-8,-7,-7,-2,-5,4,7,9,-9,-8,2,-1,3,4,9,3,-8,-8,-1,3,-1,10,-5,1,-8,4,-8,10,5,3,5,-3,10,9,2,-9,-1,2,-10,9,-1,-9,-9,10,-3,10,-3,-3,4,4,4,-2,6,10,-6,-3,3,6,1,8,1,1,2,-4,-6,4,-6,6,8,-6,-4,-1,-1,10,5,3,7,9,-10,6,3,-9,-4,-3,-2,9,7,4,9,9,2,-1,10,10,2,9,4,6,-4,2,-7,-1,-3,4,8,7,9,-3,-7,-8]], dtype = "int16")#candidate|2772|(1, 1040)|const|int16
call_2771 = relay.TupleGetItem(func_2319_call(relay.reshape(const_2772.astype('int16'), [13, 5, 16]), relay.reshape(const_2772.astype('int16'), [13, 5, 16]), relay.reshape(const_2772.astype('bool'), [13, 5, 16]), ), 3)
call_2773 = relay.TupleGetItem(func_2323_call(relay.reshape(const_2772.astype('int16'), [13, 5, 16]), relay.reshape(const_2772.astype('int16'), [13, 5, 16]), relay.reshape(const_2772.astype('bool'), [13, 5, 16]), ), 3)
output = relay.Tuple([call_2748,call_2755,const_2756,call_2761,call_2767,var_2768,var_2769,call_2771,const_2772,])
output2 = relay.Tuple([call_2749,call_2757,const_2756,call_2762,call_2770,var_2768,var_2769,call_2773,const_2772,])
func_2774 = relay.Function([var_2768,var_2769,], output)
mod['func_2774'] = func_2774
mod = relay.transform.InferType()(mod)
var_2775 = relay.var("var_2775", dtype = "float64", shape = (720,))#candidate|2775|(720,)|var|float64
var_2776 = relay.var("var_2776", dtype = "float64", shape = (39,))#candidate|2776|(39,)|var|float64
output = func_2774(var_2775,var_2776,)
func_2777 = relay.Function([var_2775,var_2776,], output)
mutated_mod['func_2777'] = func_2777
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1918_call = mod.get_global_var('func_1918')
func_1919_call = mutated_mod.get_global_var('func_1919')
call_2798 = relay.TupleGetItem(func_1918_call(), 0)
call_2799 = relay.TupleGetItem(func_1919_call(), 0)
output = relay.Tuple([call_2798,])
output2 = relay.Tuple([call_2799,])
func_2800 = relay.Function([], output)
mod['func_2800'] = func_2800
mod = relay.transform.InferType()(mod)
mutated_mod['func_2800'] = func_2800
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2800_call = mutated_mod.get_global_var('func_2800')
call_2801 = func_2800_call()
output = call_2801
func_2802 = relay.Function([], output)
mutated_mod['func_2802'] = func_2802
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2145_call = mod.get_global_var('func_2145')
func_2146_call = mutated_mod.get_global_var('func_2146')
call_2826 = relay.TupleGetItem(func_2145_call(), 0)
call_2827 = relay.TupleGetItem(func_2146_call(), 0)
output = call_2826
output2 = call_2827
func_2854 = relay.Function([], output)
mod['func_2854'] = func_2854
mod = relay.transform.InferType()(mod)
output = func_2854()
func_2855 = relay.Function([], output)
mutated_mod['func_2855'] = func_2855
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2861 = relay.const([[[False,True],[True,True],[False,False],[True,True]],[[True,False],[False,False],[False,True],[True,False]],[[False,True],[True,True],[True,False],[False,True]]], dtype = "bool")#candidate|2861|(3, 4, 2)|const|bool
const_2862 = relay.const([[[True,False],[False,False],[True,False],[False,True]],[[False,False],[True,False],[True,False],[True,True]],[[False,True],[True,True],[False,True],[False,True]]], dtype = "bool")#candidate|2862|(3, 4, 2)|const|bool
bop_2863 = relay.logical_and(const_2861.astype('bool'), relay.reshape(const_2862.astype('bool'), relay.shape_of(const_2861))) # shape=(3, 4, 2)
func_1013_call = mod.get_global_var('func_1013')
func_1014_call = mutated_mod.get_global_var('func_1014')
call_2870 = func_1013_call()
call_2871 = func_1013_call()
output = relay.Tuple([bop_2863,call_2870,])
output2 = relay.Tuple([bop_2863,call_2871,])
func_2891 = relay.Function([], output)
mod['func_2891'] = func_2891
mod = relay.transform.InferType()(mod)
output = func_2891()
func_2892 = relay.Function([], output)
mutated_mod['func_2892'] = func_2892
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2389_call = mod.get_global_var('func_2389')
func_2390_call = mutated_mod.get_global_var('func_2390')
call_2933 = func_2389_call()
call_2934 = func_2389_call()
func_620_call = mod.get_global_var('func_620')
func_623_call = mutated_mod.get_global_var('func_623')
const_2944 = relay.const([7.788082,-6.838539,9.549619,-9.615449,3.694595,5.298831,-3.160040,-2.219204,3.666833,7.462408,7.742608,-6.340225,-3.568947,4.425247,6.152956,9.413565,-6.043103,-7.017719,-4.123051,0.601996,8.409167,0.336500,-4.800788,3.549601,2.112900,9.890847,1.457160,-6.580446,2.865130,2.576292,2.040955,9.945904,-9.860978,0.201721,-1.688454,1.800982,8.863144,4.936972,-5.863004,8.687849,3.618141,-6.955606,-5.159758,-3.244506,-2.734730,-7.527436,-2.817411,2.108485,9.152881,8.240766,-0.568889,7.578642,-5.771943,2.563900,9.378523,-4.251703,2.146262,4.343402,-5.258802,1.070710,-8.742976,-0.290891,-6.378779,8.653849,-1.574695,2.758002,5.876412,-5.814977,-7.598536,-9.798568,-0.818536,-8.134320,-0.548204,8.251827,-6.936641,7.294207,-8.765815,4.802920,-5.088920,-4.155338,-2.927105,1.840283,1.083494,6.286510,4.360318,4.828085,-0.049438,-6.303745,-4.425668,1.438301,-3.671787,5.539034,-4.878344,4.742624,2.297212,5.505437,-2.772619,-9.654161,-5.482364,6.541491,4.960813,7.319116,-7.427007,-1.057747,0.041951,5.024102,0.503844,-3.836423,-1.362943,-2.774396,-5.021043,8.048780,-4.930105,-9.336406,5.840635,-7.596736,-4.887267,-7.867304,6.252020,7.436393,5.654151,8.964309,1.437097,-6.891368,9.271845,-2.513585,3.136320,-5.744196,8.652977,-1.246426,-1.864280,6.960965,2.309285,-5.490234,9.084061,4.202081,-0.132565,5.501654,4.265851,4.700752,-6.676148,-8.392657,6.680497,6.713396,6.208678,4.529113,-3.870466,-1.312258,7.165505,1.035229,6.168235,2.298859,8.754656,7.513103,-6.477502,4.229640,-6.237357,-1.212192,5.303964,-3.509036,-1.415081,-2.451065,8.904838,-9.264260,9.676772,9.053926,-2.205253,2.481400,9.556868,-0.936765,3.377504,-9.240632,4.411626,-5.325085,-9.758897,5.122905,-6.152359,9.064981,1.593195,-8.954171,6.754992,4.888671,-5.572665,2.038029,4.636190,-9.345461,-7.244751,1.000863,3.903320,-9.869751,-8.191885,-4.441547,8.708314,-1.773694,7.211740,-3.196843,-7.203209,4.177407,-5.038871,-4.217890,-3.538366,-8.444306,2.418024,5.568461,2.172686,-4.549625,8.270304,9.596941,8.391165,6.084136,-8.532962,6.150385,2.423089,-9.514039,-8.405169,-9.469181,3.882205,1.214697,-3.474794,3.305505,-7.888421,1.341881,0.309253,-2.695940,4.037960,3.867460,9.761371,-3.440930,7.108423,-7.294921,-9.239913,6.457034,-2.153322,-2.292537,0.326573,-7.077362,-3.002430,5.202362,-0.769614,-2.962559,-5.999716,-2.180095,-3.297232,-7.014912,7.328436,1.117268,9.272000,0.433904,5.785685,-8.478459,5.454876,-4.569685,3.595653,4.920884,-2.861629,4.247959,-3.779331,-0.916229,-8.278816,-6.992332,-1.626622,4.253749,-1.475833,1.670691,8.950821,-6.918466,-2.561879,-5.277756,8.363398,-5.050775,9.093505,-9.646148,0.127221,-5.620483,3.317333,7.956879,3.525782,-0.481381,2.819406,9.931572,8.899128,2.534546,5.076134,4.302471,-6.245650,-8.674823,6.990625,9.734645,2.756263,9.009697,-0.810299,-0.805372,9.284806,-7.708309,-1.186563,1.922094,9.076691,-9.452297,-8.981199,5.242901,3.110527,-4.662437,-3.716794,2.571243,-6.377093,1.196012,9.660678,-3.322734,-5.594573,7.549890,-1.601993,-5.303549,7.980291,-4.639588,5.294894,-0.738243,4.989507,1.072563,-5.426022,-8.703582,2.253491,-6.879777,8.218158,-2.323311,7.658170,7.970663,-3.899678,3.019249,-2.282925,-1.133374,-1.047414,-7.058587,1.547776,2.350751,-2.292912,-5.443762,2.619653,-9.249999,3.997695,-0.554588,-4.925849,2.854958,-2.162325,-7.837285,-5.198012,-9.341946,-5.561499,5.192229,-5.422355,8.442670,-6.771434,6.489460,-0.568763,-5.526381,-8.277292,-3.353841,-7.614848,7.535174,6.570149,7.745141,-9.907208,-6.196384,-6.905611,2.236201,-7.764433,8.985052,-4.544108,6.831698,-6.193185,4.562781,-8.165721,8.165078,2.974073,5.704411,3.589167,-8.118806,-9.535762,-6.144969,-6.481127,-1.422761,-2.172025,8.203054,-0.099069,-4.118429,4.332196,0.350169,3.487565,-9.095572,6.156440,0.917937,1.532692,2.581637,-9.748913,-1.371000,2.211272,-4.526413,8.798835,-3.437037,-9.154480,-8.322269,-5.669626,7.143779,6.258057,-3.012977,-1.846067,1.161417,-8.351370,9.883591,-7.019317,9.870238,-1.799815,7.370618,-4.351151,8.197848,-5.003438,-1.552694,7.866912,4.127111,4.080058,-1.065501,2.318672,9.037701,-0.588621,2.561759,9.012557,-3.815575,-6.307239,6.049941,9.807541,6.326243,-1.149864,2.298140,9.706853,-8.937868,-3.204610,-3.547087,-7.363253,5.215981,1.759471,5.199222,-8.671710,-9.069614,-1.264963,7.290103,0.646938,0.137554,-0.377923,7.260541,7.300564,-9.532923,-0.928881,-3.646410,7.997048,0.531750,-9.638035,3.713717,-0.364973,5.040321,5.519390,5.997983,1.280351,-2.819616,0.757541,7.503007,-4.226696,-5.506189,2.626591,8.113204,2.223754,1.854016,-8.469361,-5.495987,-0.212646,9.729242,-6.087053,-6.222672,1.131156,3.979615,8.498354,-9.966023,-7.314024,-6.939297,5.967135,-4.497976,3.690435,-5.879480,-0.554175,-6.344329,-2.239409,-7.057213,-9.616040,-5.293835,-4.989071,-4.066149,-9.890551,9.768418,-8.013910,-2.892643,8.853917,-9.082134,-5.959105,-6.090826,1.906377,-9.780975,-3.658676,-1.262576,3.062530,0.021390,-5.741515,2.348236,-7.088205,4.458335,2.549260,-4.999518,9.719822,0.274297,1.090352,-2.852284,-1.104404,-7.869041,-3.070495,-2.449266,9.828634,9.635354,6.950559,-9.127807,8.595180,-9.273073,-4.647041,8.547808,3.964615,0.547339,9.648173,3.210777,-8.111161,-2.773377,-6.108947,3.828983,-1.025676,5.745347,2.713383,7.106007,-3.653144,9.157253,-3.319036,-7.689052,3.481572,-0.634105,9.442852,8.706173,2.777606,-2.061706,-4.300089,4.951303,-2.754099,-0.404977,1.836306,-6.882047,-9.383884,-0.851805,5.171997,-6.965626,-4.925668,9.034439,1.723276,-5.685475,-1.527809,-7.672301,-4.821200,-9.537588,7.486446,-5.297507,-9.214641,-5.974603,9.149535,-4.329412,3.681336,5.448918,3.113341,6.989375,3.942621,-7.803532,8.136803,-1.169883,-4.237859,-0.855341,-1.719265,-2.618907,-8.638174,1.729624,0.407904,-0.061557,-2.002793,5.645442,-8.440162,-7.680650,-8.456651,1.396514,-1.576372,2.858487,-4.117701,-5.830445,-9.945271,-8.538423,2.335070,-1.896858,3.078862,6.454347,7.938645,8.858497,6.390045,4.745710,-4.783447,1.615811,0.008878,-6.661723,1.367187,-6.510550,9.422332,-0.465670,-9.570179,-7.877668,6.346512,8.516127,-5.650244,-3.860383,5.913336,9.231960,-0.431714,-6.179484,6.152233,-4.373297,7.499572,-0.769084,0.972427,6.338498,-6.831314,9.025291,7.453721,-7.256576,4.439386,8.284527,-5.757145,4.102598,-8.078404,-0.856070,-1.756420,-8.623425,8.481344,-2.879444,9.400443,-3.938526,1.350532,5.999726,2.791820,-4.008626,-0.804261,5.570150,-4.189080,9.745824,-7.484663,-5.647334,-3.122058,-4.119377,-5.152787,-7.138278,-6.215620,0.018407,-7.206139,-7.928662,-1.438555,4.744319,-9.218943,0.900704,3.812769,7.267916,6.588404,-5.084053,-1.485361,5.610975,5.752304,-0.376749,6.219906,-5.847670,-3.141033,7.253740,4.570453,3.519870,6.143195,4.301657,-8.794374,-0.544912,-6.890713,6.809455,6.552794,1.777681,9.181195,-5.668840,1.940870,-1.156575,6.859695,-3.216058,-0.454121,-2.130576,5.557513,-3.313083,8.298796,9.807220,6.166730,-3.943087,2.152514,-7.335077,-4.956498,9.654896,3.048914,0.570188,4.437352,1.660935,-3.975872,7.744711,4.760496,0.110774,-1.478418,6.832864,8.452633,-8.112581,8.208949,1.460612,4.002351,-9.028410,3.726927,2.569001,3.230982,-3.078796,1.149962,7.683637,-1.288751,1.228074,6.195563,-1.610572,-4.847325,-6.268947,0.760332,9.995007,-1.852414,2.435071,-1.178058,9.088205,-8.860409,4.469488,2.785599,-7.959261,7.971425,2.429492,-3.817025,1.898545,-0.546585,4.967059,-2.312446,5.579629,-8.091169,-9.289852,3.755428,-1.618012,6.019725,2.058660,2.794262,-8.108695,1.396153,3.643780,-2.416773,0.050484,-9.355769,-1.411487,7.752345,-1.247951,2.800114,-3.347600,-1.058735,-5.495686,-0.669367,-5.945558,7.360561,-8.058646,-5.984179,6.022314,3.558119,-5.707842,9.212524,-9.419365,-5.548610,-7.029578,3.062539,-8.048061,1.381324,1.919013,0.050551,7.857229,8.020770,9.393616,-3.342836,-4.889082,1.595254,7.663200,1.054455,-5.445216,-1.586087,4.615304,4.899894,1.551369,-0.997195,9.086400,3.117177,4.793607,-7.768144,-4.186356,8.162468,-7.814179,7.715709,8.283910,1.736245,-8.147385,-8.336295,2.989330,-9.684933,-5.392353,-1.230406,-9.737076,4.583053,-1.675251,-0.879448,-3.519464,9.461926,8.417861,-8.943823,0.141896,-5.698905,-6.721853,-2.252502,-1.317220,-4.632772,9.558813,-5.132639,-0.611975,1.243044,-6.180857,-4.078318,5.841138,0.547971,-9.892413,2.406584,-3.220557,-9.463542,-4.102022,-7.278608,0.792540,-6.601453,5.907772,-0.200022,-1.390452,-4.045729,2.766312,8.953680,-4.725947,0.253034,-5.643566,0.841994,-4.130368,4.416788,-0.014487,-8.873673,3.928768,-9.946370,0.624261,-1.600421,5.640237,-0.005546,7.504615,1.685353,5.435373,7.303788,-0.537138,-2.631300,-1.038463,0.338113,7.074271,-3.433343,-6.748492,-6.040418,5.989961,4.443352,3.059710,7.436030,1.770287,6.340721,-4.446298,4.667392,5.578033,0.368819,0.672532,-9.693884,-2.674079,4.061758,0.066107,5.285340,3.143124,4.202123,-8.207979,5.057286,-6.816329], dtype = "float64")#candidate|2944|(910,)|const|float64
call_2943 = func_620_call(relay.reshape(const_2944.astype('float64'), [5, 14, 13]), relay.reshape(const_2944.astype('float64'), [5, 14, 13]), )
call_2945 = func_620_call(relay.reshape(const_2944.astype('float64'), [5, 14, 13]), relay.reshape(const_2944.astype('float64'), [5, 14, 13]), )
func_1877_call = mod.get_global_var('func_1877')
func_1879_call = mutated_mod.get_global_var('func_1879')
const_2950 = relay.const([10,-9,2,1,9,-7,-5,-2,-4,3,-9,7,6,6,-8,3,-5,-9,8,-2,1,5,-2,-8,2,-10,-6,9,-10,-4,-1,4,-1,-3,-2,-5,-6,-9,-9,-5,-8,2,-1,-6,5,7,6,2,-6,-8,1,3,4,-6,-7,-4,5,9,-4,-6,2,4,9,-7,10,5,-9,-7,-10,-5,-5,2,-4,7,-5,-6,-8,-8,6,-2,-3,6,-7,4,-7,4,10,1,8,-2,10,-3,8,-5,-7,1,-6,-1,-1,10,-3,-9,4,-7,-7,-7,-6,-5,-10,-1,9,-6,-10,-10,1,8,-4,-9,6,-1,4,7,-8,6,-3,6,10,7,-8,-10,6,-3,4,1,7,-2,1,10,-4,-1,5,8,-9,5,3,6,-1,2,-10,-7,6,-5,1,-10,4,-3,-9,4,8,-5,5,2,10,-3,-6,5,-2,-1,-8,9,2,-10,-2,9,4,-1,-5,4,9,-4,-10,9,1,-4,-2,-2,-2,5,9,-4,-8,-1,-1,6,6,5,1,5,-5,-1,-3,-3,-5,1,-4,6,-3,5,-6,2,-3,6,-10,-5,4,-3,-1,2,-7,-10,9,1,5,-3,-8,-2,1,-6,1,-7,-7,1,-7,4,7,2,-1,7,-10,-10,-9,-1,10,-1,-7,7,-9,6,3,-9,-5,6,8,6,8,-8,6,-7,-5,1,-9,9,-7,7,4,-10,-8,7,-4,6,8,-8,1,5,6,-1,-2,-6,-7,9,-8,2,-7,-4,3,2,-3,-8,-8,4,6,-2,8,-9,10,8,-9,5,-9,-7,-10,6,9,-10,6,2,1,-2,1,-4,1,8,2,8,-6,-6,3,-2,5,-1,7,-2,-9,-7,-8,-1,3,-1,-7,-6,5,1,-3,2,8,10,-1,6,-9,-10,4,-7,3,1,8,-4,9,-1,-2,-4,-8,-6,7,9,-4,2,-2,-4,7,-6,-3,8,-8,8,-5,10,5,2,-7,7,-10,9,5,7,-1,9,-5,-7,7,3,-6,-5,9,4,-8,7,-9,10,-2,-8,-9,-6,-1,7,8,1,-3,8,4,7,-2,-10,1,-5,-8,-5,-7,3,-5,9,2,-9,4,8,9,10,2,-2,-1,-7,1,5,-4,-7,1,-10,6,8,9,10,3,-9,1,7,10,2,-7,-9,-7,8,4,9,-9,2,4,6,-3,2,8,-7,-5,-10,-7,-3,-7,10,-1,1,-7,10,4,-1,-10,-10,-6,7,-5,-6,-5,-5,-10,-4,-6,-10,8,6,-5,7,-2,6], dtype = "uint16")#candidate|2950|(480,)|const|uint16
call_2949 = relay.TupleGetItem(func_1877_call(relay.reshape(const_2950.astype('uint16'), [480,])), 3)
call_2951 = relay.TupleGetItem(func_1879_call(relay.reshape(const_2950.astype('uint16'), [480,])), 3)
output = relay.Tuple([call_2933,call_2943,const_2944,call_2949,const_2950,])
output2 = relay.Tuple([call_2934,call_2945,const_2944,call_2951,const_2950,])
func_2957 = relay.Function([], output)
mod['func_2957'] = func_2957
mod = relay.transform.InferType()(mod)
output = func_2957()
func_2958 = relay.Function([], output)
mutated_mod['func_2958'] = func_2958
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2800_call = mod.get_global_var('func_2800')
func_2802_call = mutated_mod.get_global_var('func_2802')
call_2990 = relay.TupleGetItem(func_2800_call(), 0)
call_2991 = relay.TupleGetItem(func_2802_call(), 0)
output = call_2990
output2 = call_2991
func_2995 = relay.Function([], output)
mod['func_2995'] = func_2995
mod = relay.transform.InferType()(mod)
output = func_2995()
func_2996 = relay.Function([], output)
mutated_mod['func_2996'] = func_2996
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2246_call = mod.get_global_var('func_2246')
func_2248_call = mutated_mod.get_global_var('func_2248')
call_3075 = relay.TupleGetItem(func_2246_call(), 2)
call_3076 = relay.TupleGetItem(func_2248_call(), 2)
var_3089 = relay.var("var_3089", dtype = "float64", shape = (14, 880))#candidate|3089|(14, 880)|var|float64
bop_3090 = relay.equal(call_3075.astype('bool'), var_3089.astype('bool')) # shape=(14, 880)
bop_3093 = relay.equal(call_3076.astype('bool'), var_3089.astype('bool')) # shape=(14, 880)
bop_3095 = relay.left_shift(call_3075.astype('uint8'), var_3089.astype('uint8')) # shape=(14, 880)
bop_3098 = relay.left_shift(call_3076.astype('uint8'), var_3089.astype('uint8')) # shape=(14, 880)
output = relay.Tuple([bop_3090,bop_3095,])
output2 = relay.Tuple([bop_3093,bop_3098,])
func_3111 = relay.Function([var_3089,], output)
mod['func_3111'] = func_3111
mod = relay.transform.InferType()(mod)
var_3112 = relay.var("var_3112", dtype = "float64", shape = (14, 880))#candidate|3112|(14, 880)|var|float64
output = func_3111(var_3112)
func_3113 = relay.Function([var_3112], output)
mutated_mod['func_3113'] = func_3113
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2389_call = mod.get_global_var('func_2389')
func_2390_call = mutated_mod.get_global_var('func_2390')
call_3115 = func_2389_call()
call_3116 = func_2389_call()
func_799_call = mod.get_global_var('func_799')
func_803_call = mutated_mod.get_global_var('func_803')
var_3124 = relay.var("var_3124", dtype = "uint16", shape = (80,))#candidate|3124|(80,)|var|uint16
var_3125 = relay.var("var_3125", dtype = "uint16", shape = (4, 120))#candidate|3125|(4, 120)|var|uint16
call_3123 = func_799_call(relay.reshape(var_3124.astype('uint16'), [1, 5, 16]), relay.reshape(var_3125.astype('uint16'), [6, 5, 16]), )
call_3126 = func_799_call(relay.reshape(var_3124.astype('uint16'), [1, 5, 16]), relay.reshape(var_3125.astype('uint16'), [6, 5, 16]), )
func_543_call = mod.get_global_var('func_543')
func_544_call = mutated_mod.get_global_var('func_544')
call_3161 = relay.TupleGetItem(func_543_call(), 0)
call_3162 = relay.TupleGetItem(func_544_call(), 0)
func_2246_call = mod.get_global_var('func_2246')
func_2248_call = mutated_mod.get_global_var('func_2248')
call_3164 = relay.TupleGetItem(func_2246_call(), 2)
call_3165 = relay.TupleGetItem(func_2248_call(), 2)
func_989_call = mod.get_global_var('func_989')
func_991_call = mutated_mod.get_global_var('func_991')
call_3168 = relay.TupleGetItem(func_989_call(), 1)
call_3169 = relay.TupleGetItem(func_991_call(), 1)
func_638_call = mod.get_global_var('func_638')
func_640_call = mutated_mod.get_global_var('func_640')
call_3170 = func_638_call()
call_3171 = func_638_call()
output = relay.Tuple([call_3115,call_3123,var_3124,var_3125,call_3161,call_3164,call_3168,call_3170,])
output2 = relay.Tuple([call_3116,call_3126,var_3124,var_3125,call_3162,call_3165,call_3169,call_3171,])
func_3183 = relay.Function([var_3124,var_3125,], output)
mod['func_3183'] = func_3183
mod = relay.transform.InferType()(mod)
mutated_mod['func_3183'] = func_3183
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3183_call = mutated_mod.get_global_var('func_3183')
var_3185 = relay.var("var_3185", dtype = "uint16", shape = (80,))#candidate|3185|(80,)|var|uint16
var_3186 = relay.var("var_3186", dtype = "uint16", shape = (4, 120))#candidate|3186|(4, 120)|var|uint16
call_3184 = func_3183_call(var_3185,var_3186,)
output = call_3184
func_3187 = relay.Function([var_3185,var_3186,], output)
mutated_mod['func_3187'] = func_3187
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2854_call = mod.get_global_var('func_2854')
func_2855_call = mutated_mod.get_global_var('func_2855')
call_3337 = func_2854_call()
call_3338 = func_2854_call()
output = call_3337
output2 = call_3338
func_3353 = relay.Function([], output)
mod['func_3353'] = func_3353
mod = relay.transform.InferType()(mod)
output = func_3353()
func_3354 = relay.Function([], output)
mutated_mod['func_3354'] = func_3354
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3425 = relay.const([[[1.583527,7.137439,-4.298773,-6.228634,-6.122292,0.822213,8.633175],[-1.705872,2.933276,6.779210,2.475572,9.691722,-8.740371,-5.738396]],[[-8.079721,-2.810401,-3.610010,-2.553306,3.570384,3.764666,-7.053587],[7.935994,4.339682,5.142793,8.745222,3.564133,-2.901607,-9.227429]],[[-2.526029,8.309246,9.169044,5.542380,1.992136,-1.693682,-9.718038],[-8.801047,0.960361,-9.614079,5.402631,1.324632,-1.562820,0.979692]],[[8.466881,5.564888,4.739827,-5.385838,7.716742,-2.549807,2.690843],[3.617962,0.184792,-7.798138,7.537504,8.114237,-6.066749,3.338985]],[[-8.077548,-6.520395,6.290305,9.758391,-7.493193,9.587972,4.647724],[-1.601562,-2.378762,-1.321330,7.766644,-3.628629,-6.280325,-9.955593]],[[-7.184581,4.237553,-2.673775,-5.851793,-5.285273,-7.538252,9.110541],[-1.777045,-0.167109,0.588974,-4.875881,-8.055666,-9.446770,-0.509078]],[[-8.347316,-3.916223,8.017030,1.710273,1.459865,3.461380,-0.057896],[-3.694999,3.701548,-5.745639,3.759596,-4.169352,-6.700984,5.196387]],[[-7.933268,9.834974,-2.624386,0.729087,9.915897,-9.351902,6.942537],[-9.428690,6.661125,1.136944,9.595982,-0.205078,-6.976517,-8.048128]],[[1.970570,0.943479,-6.586829,2.339495,-7.318568,-6.105885,5.946638],[-0.938294,-8.489029,-6.834785,4.639524,-7.154392,-2.104785,3.656614]],[[3.901248,8.651069,-2.119683,-8.572592,3.860731,3.279400,8.241331],[0.393453,-3.546646,4.872655,9.193911,6.420781,5.071085,3.773791]],[[-0.702849,-1.319174,4.892052,8.710278,8.765306,-3.032388,9.962834],[-6.648605,4.744156,7.513308,-7.302056,-3.712740,3.780636,-0.017591]],[[9.312089,-8.635972,6.252026,4.672116,-0.183472,-6.870088,7.084630],[-2.562781,-5.896484,6.455826,-2.129321,-8.685738,6.397658,-7.449315]]], dtype = "float64")#candidate|3425|(12, 2, 7)|const|float64
uop_3426 = relay.asinh(const_3425.astype('float64')) # shape=(12, 2, 7)
uop_3428 = relay.atan(uop_3426.astype('float64')) # shape=(12, 2, 7)
output = relay.Tuple([uop_3428,])
output2 = relay.Tuple([uop_3428,])
func_3431 = relay.Function([], output)
mod['func_3431'] = func_3431
mod = relay.transform.InferType()(mod)
mutated_mod['func_3431'] = func_3431
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3431_call = mutated_mod.get_global_var('func_3431')
call_3432 = func_3431_call()
output = call_3432
func_3433 = relay.Function([], output)
mutated_mod['func_3433'] = func_3433
mutated_mod = relay.transform.InferType()(mutated_mod)
func_332_call = mod.get_global_var('func_332')
func_333_call = mutated_mod.get_global_var('func_333')
call_3442 = func_332_call()
call_3443 = func_332_call()
func_1186_call = mod.get_global_var('func_1186')
func_1187_call = mutated_mod.get_global_var('func_1187')
call_3444 = func_1186_call()
call_3445 = func_1186_call()
output = relay.Tuple([call_3442,call_3444,])
output2 = relay.Tuple([call_3443,call_3445,])
func_3448 = relay.Function([], output)
mod['func_3448'] = func_3448
mod = relay.transform.InferType()(mod)
mutated_mod['func_3448'] = func_3448
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3448_call = mutated_mod.get_global_var('func_3448')
call_3449 = func_3448_call()
output = call_3449
func_3450 = relay.Function([], output)
mutated_mod['func_3450'] = func_3450
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1091_call = mod.get_global_var('func_1091')
func_1093_call = mutated_mod.get_global_var('func_1093')
call_3503 = relay.TupleGetItem(func_1091_call(), 1)
call_3504 = relay.TupleGetItem(func_1093_call(), 1)
func_2389_call = mod.get_global_var('func_2389')
func_2390_call = mutated_mod.get_global_var('func_2390')
call_3511 = func_2389_call()
call_3512 = func_2389_call()
output = relay.Tuple([call_3503,call_3511,])
output2 = relay.Tuple([call_3504,call_3512,])
func_3525 = relay.Function([], output)
mod['func_3525'] = func_3525
mod = relay.transform.InferType()(mod)
output = func_3525()
func_3526 = relay.Function([], output)
mutated_mod['func_3526'] = func_3526
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1574_call = mod.get_global_var('func_1574')
func_1575_call = mutated_mod.get_global_var('func_1575')
call_3538 = func_1574_call()
call_3539 = func_1574_call()
func_3183_call = mod.get_global_var('func_3183')
func_3187_call = mutated_mod.get_global_var('func_3187')
var_3542 = relay.var("var_3542", dtype = "uint16", shape = (80,))#candidate|3542|(80,)|var|uint16
const_3543 = relay.const([[-9,10,9,4,-5,4,-5,-6,-8,-2,5,-2,2,5,-1,-8,-7,-8,4,-8,8,1,-10,-8,1,-3,-3,-3,-4,2,-1,-4,1,-5,-7,-6,-6,-8,5,-5,5,1,5,-1,-4,4,7,4,-3,3,-1,-5,-7,3,9,8,-8,-10,-3,-3,7,-2,9,-10,-2,-2,-3,10,-10,-2,1,-10,9,3,2,10,-3,-2,10,-5,-9,7,-6,4,8,-2,5,9,2,7,7,-3,-2,3,9,4,6,1,-8,7,-8,6,-1,-7,-6,6,4,2,-4,-7,6,2,5,-6,-6,-1,-2,-10,-2,5,-3,-9,-10,-10,9,-9,1,7,-3,-8,-5,-5,-8,9,4,-7,-5,-2,9,-9,-3,1,10,-9,10,1,-8,10,3,-5,-3,2,1,5,9,-8,2,4,9,4,3,-5,-4,-7,6,4,8,-9,9,9,-8,10,-6,4,10,-7,5,-1,8,-8,4,6,-7,9,9,-5,4,-8,2,8,-10,-2,-6,6,5,-8,5,8,-9,7,6,-4,9,-5,-2,10,9,-8,7,10,-9,10,4,-7,7,-10,8,-5,6,6,2,-1,-10,-5,5,10,4,10,-7,1,-1,-7,5,-5,-2,8,-1,-3,9,9],[-3,-8,8,-7,4,-7,8,-5,-5,-3,-3,1,9,-6,-3,-10,5,-5,5,6,-9,6,8,-10,2,-2,-4,1,-6,-2,2,-7,-2,-10,6,8,-10,3,-4,10,8,-10,-4,6,8,9,9,-6,8,-8,1,-8,-10,8,-7,9,2,-8,10,4,-1,7,9,-1,-9,-9,-6,-3,1,-10,2,4,9,-10,-5,5,9,5,5,-3,6,-7,1,9,-9,-8,8,-5,-5,6,-9,-7,-4,6,-8,-4,-3,7,8,3,6,-10,-7,-3,-10,-4,1,9,4,5,-6,-6,-9,-2,8,-6,-9,1,1,-10,-5,2,-6,1,8,-1,6,-3,10,-10,3,5,2,9,9,2,4,10,-5,-9,9,-7,-5,10,8,-4,-5,4,-4,-1,-4,7,-7,7,9,6,4,-5,-6,4,6,-6,6,10,-2,-3,4,-4,8,-4,7,-9,3,-2,10,2,4,6,-7,2,-5,-8,4,1,-5,-10,-5,5,-2,7,-3,-7,9,8,10,-7,-6,6,-9,3,10,-8,10,-4,-10,-6,2,-9,7,-6,9,3,-10,-5,-4,3,-2,2,4,-6,-7,-5,-8,-1,-4,-1,2,-10,3,-1,6,2,5,-1,9,1,-10,6,-3,-2]], dtype = "uint16")#candidate|3543|(2, 240)|const|uint16
call_3541 = relay.TupleGetItem(func_3183_call(relay.reshape(var_3542.astype('uint16'), [80,]), relay.reshape(const_3543.astype('uint16'), [4, 120]), ), 1)
call_3544 = relay.TupleGetItem(func_3187_call(relay.reshape(var_3542.astype('uint16'), [80,]), relay.reshape(const_3543.astype('uint16'), [4, 120]), ), 1)
func_799_call = mod.get_global_var('func_799')
func_803_call = mutated_mod.get_global_var('func_803')
call_3552 = func_799_call(relay.reshape(var_3542.astype('uint16'), [1, 5, 16]), relay.reshape(call_3541.astype('uint16'), [6, 5, 16]), )
call_3553 = func_799_call(relay.reshape(var_3542.astype('uint16'), [1, 5, 16]), relay.reshape(call_3541.astype('uint16'), [6, 5, 16]), )
var_3556 = relay.var("var_3556", dtype = "uint64", shape = (6, 5, 16))#candidate|3556|(6, 5, 16)|var|uint64
bop_3557 = relay.logical_and(call_3552.astype('bool'), relay.reshape(var_3556.astype('bool'), relay.shape_of(call_3552))) # shape=(6, 5, 16)
bop_3560 = relay.logical_and(call_3553.astype('bool'), relay.reshape(var_3556.astype('bool'), relay.shape_of(call_3553))) # shape=(6, 5, 16)
output = relay.Tuple([call_3538,call_3541,var_3542,const_3543,bop_3557,])
output2 = relay.Tuple([call_3539,call_3544,var_3542,const_3543,bop_3560,])
func_3567 = relay.Function([var_3542,var_3556,], output)
mod['func_3567'] = func_3567
mod = relay.transform.InferType()(mod)
var_3568 = relay.var("var_3568", dtype = "uint16", shape = (80,))#candidate|3568|(80,)|var|uint16
var_3569 = relay.var("var_3569", dtype = "uint64", shape = (6, 5, 16))#candidate|3569|(6, 5, 16)|var|uint64
output = func_3567(var_3568,var_3569,)
func_3570 = relay.Function([var_3568,var_3569,], output)
mutated_mod['func_3570'] = func_3570
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3431_call = mod.get_global_var('func_3431')
func_3433_call = mutated_mod.get_global_var('func_3433')
call_3578 = relay.TupleGetItem(func_3431_call(), 0)
call_3579 = relay.TupleGetItem(func_3433_call(), 0)
output = relay.Tuple([call_3578,])
output2 = relay.Tuple([call_3579,])
func_3587 = relay.Function([], output)
mod['func_3587'] = func_3587
mod = relay.transform.InferType()(mod)
mutated_mod['func_3587'] = func_3587
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3587_call = mutated_mod.get_global_var('func_3587')
call_3588 = func_3587_call()
output = call_3588
func_3589 = relay.Function([], output)
mutated_mod['func_3589'] = func_3589
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2145_call = mod.get_global_var('func_2145')
func_2146_call = mutated_mod.get_global_var('func_2146')
call_3624 = relay.TupleGetItem(func_2145_call(), 0)
call_3625 = relay.TupleGetItem(func_2146_call(), 0)
func_2560_call = mod.get_global_var('func_2560')
func_2561_call = mutated_mod.get_global_var('func_2561')
call_3627 = relay.TupleGetItem(func_2560_call(), 1)
call_3628 = relay.TupleGetItem(func_2561_call(), 1)
func_1091_call = mod.get_global_var('func_1091')
func_1093_call = mutated_mod.get_global_var('func_1093')
call_3632 = relay.TupleGetItem(func_1091_call(), 2)
call_3633 = relay.TupleGetItem(func_1093_call(), 2)
func_1793_call = mod.get_global_var('func_1793')
func_1795_call = mutated_mod.get_global_var('func_1795')
var_3639 = relay.var("var_3639", dtype = "float64", shape = (28,))#candidate|3639|(28,)|var|float64
call_3638 = func_1793_call(relay.reshape(var_3639.astype('float64'), [7, 4, 1]))
call_3640 = func_1793_call(relay.reshape(var_3639.astype('float64'), [7, 4, 1]))
uop_3642 = relay.acos(call_3638.astype('float32')) # shape=(7, 4, 1)
uop_3644 = relay.acos(call_3640.astype('float32')) # shape=(7, 4, 1)
func_2995_call = mod.get_global_var('func_2995')
func_2996_call = mutated_mod.get_global_var('func_2996')
call_3655 = func_2995_call()
call_3656 = func_2995_call()
var_3660 = relay.var("var_3660", dtype = "float32", shape = (7, 4, 8))#candidate|3660|(7, 4, 8)|var|float32
bop_3661 = relay.minimum(uop_3642.astype('uint64'), var_3660.astype('uint64')) # shape=(7, 4, 8)
bop_3664 = relay.minimum(uop_3644.astype('uint64'), var_3660.astype('uint64')) # shape=(7, 4, 8)
uop_3667 = relay.atanh(bop_3661.astype('float64')) # shape=(7, 4, 8)
uop_3669 = relay.atanh(bop_3664.astype('float64')) # shape=(7, 4, 8)
var_3670 = relay.var("var_3670", dtype = "float64", shape = (7, 4, 8))#candidate|3670|(7, 4, 8)|var|float64
bop_3671 = relay.logical_xor(uop_3667.astype('int32'), relay.reshape(var_3670.astype('int32'), relay.shape_of(uop_3667))) # shape=(7, 4, 8)
bop_3674 = relay.logical_xor(uop_3669.astype('int32'), relay.reshape(var_3670.astype('int32'), relay.shape_of(uop_3669))) # shape=(7, 4, 8)
output = relay.Tuple([call_3624,call_3627,call_3632,var_3639,call_3655,bop_3671,])
output2 = relay.Tuple([call_3625,call_3628,call_3633,var_3639,call_3656,bop_3674,])
func_3683 = relay.Function([var_3639,var_3660,var_3670,], output)
mod['func_3683'] = func_3683
mod = relay.transform.InferType()(mod)
mutated_mod['func_3683'] = func_3683
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3683_call = mutated_mod.get_global_var('func_3683')
var_3685 = relay.var("var_3685", dtype = "float64", shape = (28,))#candidate|3685|(28,)|var|float64
var_3686 = relay.var("var_3686", dtype = "float32", shape = (7, 4, 8))#candidate|3686|(7, 4, 8)|var|float32
var_3687 = relay.var("var_3687", dtype = "float64", shape = (7, 4, 8))#candidate|3687|(7, 4, 8)|var|float64
call_3684 = func_3683_call(var_3685,var_3686,var_3687,)
output = call_3684
func_3688 = relay.Function([var_3685,var_3686,var_3687,], output)
mutated_mod['func_3688'] = func_3688
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3701 = relay.const([[[-8.521529,6.651925,-8.061916,0.592304,-5.311631,1.121934,9.152168,8.323649,-6.014109,4.903865,-2.985347,-6.827184,2.205420,-0.290084,1.303992,-7.406904],[1.189545,-1.632493,2.649192,9.368844,-8.975540,-6.325124,0.949628,6.942455,3.801948,-9.112341,1.357975,5.150086,8.024735,-5.219370,4.209776,5.068951],[2.462790,-4.185986,8.869111,-3.404075,9.002207,7.803352,3.661368,-3.364316,4.587354,-9.260673,9.903753,2.912840,-2.243274,8.632081,-7.494416,-8.787274],[9.308288,5.001324,-6.863196,-5.541560,-9.128989,-0.835619,3.470486,-3.182874,-9.971157,0.081527,1.612640,-5.396631,-7.297183,1.724748,-5.094600,-3.150200],[6.804836,4.938928,-4.658553,5.071618,8.833787,-2.184161,-6.102743,-5.648265,6.064164,0.661493,-1.086484,-1.651337,9.205648,-5.509654,-1.861598,5.225742],[-0.381095,3.611401,4.672823,4.985372,1.803644,6.547091,-4.828614,-3.115672,5.484002,-7.468719,2.531400,-1.150373,6.579034,9.308004,-4.039413,9.607907],[6.606004,4.583327,4.541163,7.452025,-8.980606,-9.102913,-9.375999,-3.921263,-2.135608,-5.739470,-4.464159,5.109282,0.921134,1.685153,1.033581,-6.154396],[7.620422,3.247471,-0.972113,9.721976,9.974596,5.623083,-6.440319,3.224530,3.297908,7.596019,5.606297,2.743085,6.863527,-8.097634,1.923393,2.475347],[-4.797014,7.664633,0.065948,4.915086,-6.483770,8.046369,-7.705240,-7.022475,-4.578960,3.641445,-4.268425,-2.936016,5.444810,-2.498452,6.175416,-0.160459],[4.029568,-8.270694,-4.086459,0.094362,-2.351400,-3.024710,-3.451455,-9.793827,-8.083262,-3.951314,-4.337735,-3.408601,1.488525,-7.513501,-1.341668,-1.065190],[-7.421069,-2.006565,-4.399876,-3.369980,-2.000742,7.298547,6.228189,7.855155,-2.558251,-1.602126,-5.990216,-8.428221,1.859283,-6.766683,8.665177,7.560125],[8.618189,1.907042,-1.769090,7.843371,-5.051828,0.347832,-1.935368,8.469858,-4.041388,-1.955689,-3.928443,-9.159605,6.556299,8.762270,5.509361,2.644111]],[[-2.287133,-9.303633,-2.319139,-7.995851,-9.962052,-3.019160,-3.327583,6.778259,6.263762,-8.268716,4.692424,8.273595,2.569577,9.491133,-3.258168,-5.236889],[7.350400,3.714061,-9.006923,-7.099276,2.823564,0.907635,-5.899583,-8.869189,-2.728013,9.005681,7.276899,9.320734,5.050221,5.327813,8.194751,1.839643],[-9.413767,-5.128039,-5.111110,6.249489,3.391598,1.579212,-7.067694,5.530899,-4.075500,-9.897873,8.447559,1.905883,-8.134712,-0.395974,-6.955155,4.096944],[-7.189251,9.940816,-3.714219,-2.016849,9.750339,-6.736622,9.177444,8.201506,-3.446215,3.344266,5.437269,5.698054,5.588943,4.144572,2.279407,-2.462889],[-6.628504,-4.234796,7.912678,-6.425424,-2.491930,-8.858422,-7.557437,-0.277521,0.470429,-7.829805,-0.243561,-8.957120,-6.910625,5.464733,-7.906288,4.672532],[1.751152,-2.982027,5.889464,1.148021,1.504734,3.517603,9.575609,-0.861986,-4.655490,8.893020,-0.668775,-4.824222,4.864835,-3.909046,-2.000879,-2.716337],[8.990182,-6.824197,0.158651,8.241798,3.015844,-9.180782,-5.116343,7.092108,-9.680453,1.828667,-4.771327,5.753987,1.613947,-1.298115,0.402487,8.473585],[8.807859,7.716398,9.482302,3.406553,-9.348029,-4.847879,-7.781444,1.444394,-9.147877,-8.156636,-8.460156,3.398823,2.865358,0.567119,-9.803112,-1.679446],[-7.351653,5.058974,-5.823389,-9.071036,-4.919398,8.991134,-9.278600,1.815856,5.252334,-3.775233,2.735580,1.404002,2.917405,-7.702011,3.902235,0.155467],[-1.398157,0.518974,8.726990,0.632934,-7.925773,-1.930085,5.784059,-3.312447,1.828151,8.157845,-7.779944,-0.738257,0.205120,3.417432,8.397048,0.259116],[4.765432,-7.910232,-4.469706,7.749688,-6.985102,-6.903566,6.220773,-3.457923,8.569313,-9.841426,-6.095423,5.929943,6.820991,-8.675541,6.811122,-8.441706],[-4.445598,4.119366,5.315070,-4.567550,-2.194180,0.062563,2.505641,0.666807,1.298600,-2.810963,-0.191284,-1.285501,-2.904564,-3.620270,-8.137367,0.644880]],[[3.501117,3.862805,6.508843,-0.055751,-7.289999,7.157700,3.705206,-3.098730,-3.270951,-0.247770,-7.327526,-7.303517,3.396141,-0.425401,-3.244820,-7.959859],[-4.024623,-6.507290,1.456892,-7.407174,-7.063452,8.374759,-7.344822,8.168615,-6.046337,2.343220,-3.735224,-3.650064,-1.849227,7.124006,-7.640539,-0.755297],[0.023054,-3.719199,6.131558,0.035463,-3.397627,4.584059,-0.459578,-7.433979,-6.771687,-6.968651,0.055774,-4.645571,4.493394,-1.247691,9.890883,1.852744],[8.240312,-7.076448,-6.153811,1.570428,-0.257330,6.856706,9.397304,-3.590059,3.428888,-9.291298,9.524204,-7.105834,-5.217824,-4.875374,9.409937,-7.720792],[8.730627,5.568204,-3.548489,-8.491407,9.595514,-0.193263,1.804883,-1.762327,5.892889,-3.526942,8.216273,0.430852,1.451996,7.817574,2.789049,-7.076471],[-4.474384,-5.765465,-0.853171,-9.106975,-2.210233,-4.703560,4.188305,-4.298672,5.799960,8.069605,4.526254,-9.295972,-9.170901,3.042277,8.788826,-4.891032],[7.156420,7.894726,3.271995,2.806569,-1.509391,-3.193671,-6.717608,-5.065849,6.178534,-2.550562,-6.051776,6.615917,2.841358,0.145357,-3.396718,-1.472969],[-5.951503,9.273023,5.258754,-9.180787,-6.054356,5.028458,3.794949,-5.510062,4.774934,-0.477599,4.033492,-1.104048,-7.109456,-4.986192,4.072365,8.610115],[-7.733772,-8.225373,4.024365,1.772826,4.702151,4.011289,-5.396028,4.588086,-7.995315,2.561760,6.263185,-9.957161,5.451136,5.648114,-8.101337,4.287042],[0.332235,-3.794381,-8.301732,9.432708,0.109914,-8.742951,-2.405938,6.542993,2.878992,3.899221,3.682908,7.582450,-1.841316,3.515150,7.485795,5.084758],[-8.246617,3.952335,5.748238,-7.857670,3.721783,-7.808621,-4.156245,9.006064,-5.909898,4.852498,-5.998101,5.043586,0.499108,5.999611,6.547214,0.938401],[4.071260,-0.992252,2.877146,1.190419,9.296820,0.463210,3.029477,-0.406519,2.467675,7.966008,-1.553844,-3.837872,-2.604162,-9.635686,-1.005069,6.777367]],[[-2.009860,-2.297215,6.704945,3.369977,2.011578,-6.615856,5.514580,-2.448338,-1.896480,-0.487901,-5.187110,-4.722725,0.291575,-6.083478,6.288580,4.596776],[4.650561,5.684764,6.713832,-3.285670,6.119149,1.080063,4.372130,0.152806,-5.386256,-0.241089,-0.370084,6.572988,0.729930,3.440233,1.504578,-3.263360],[-4.393572,3.311915,-9.622980,-4.230450,9.138086,-6.475857,-1.265071,-4.535782,-5.059618,3.463974,-0.310126,-0.847163,7.162879,-0.566910,-1.133159,1.953006],[-3.651341,-3.546145,-9.307741,6.745114,-7.615118,-8.582010,4.300667,0.094978,0.458102,4.078019,2.155914,6.955586,3.237249,-0.643915,0.108815,5.521928],[-2.737576,-3.948540,-1.723394,-2.104203,-9.473928,5.503975,-1.426353,0.622654,-6.205358,6.440800,-2.026755,-1.508748,-6.374710,6.886636,-1.681900,5.849551],[-2.558323,-2.956313,8.967310,2.085310,2.000742,-5.142594,-7.692462,-0.374673,-2.831088,-7.858633,-4.298685,-8.175410,8.194627,-0.955166,-9.213246,4.700919],[-5.959732,-4.668631,-0.323740,3.720691,-6.405737,0.568509,6.937246,7.401507,5.091289,-1.259650,-2.434914,-1.091008,-5.620689,-2.996430,4.516730,2.978384],[4.043911,4.625922,8.851407,2.507191,-2.682534,-1.423973,-6.100108,1.606953,-2.582436,-1.856510,2.173282,-5.510933,2.967748,-0.953896,-8.474083,-4.621216],[4.649548,-7.741230,-3.687600,6.247384,-1.488514,-9.171034,8.862348,1.025062,1.553010,2.538644,-1.917212,-6.545967,-9.553302,-6.421118,-1.099469,-3.952213],[7.768179,4.527652,-8.018173,-5.580060,-2.346500,-0.639383,5.479792,6.651351,5.158410,1.829445,4.814644,0.797034,-8.391320,-7.189072,4.979457,2.378540],[5.264516,-1.394651,7.311610,4.088135,-1.958896,3.003324,4.651521,-6.988378,6.711851,-5.057800,-3.974475,-1.446752,-2.601216,3.471610,9.302330,-3.147623],[3.367038,6.432289,5.121803,8.453292,-7.117548,8.201199,3.793422,-6.049645,0.161859,1.472215,-8.606835,9.202998,6.157369,-3.432678,1.589800,6.761315]],[[-2.025723,2.646700,8.332990,8.511236,0.712228,6.678727,-7.972092,-7.431298,3.078636,1.063990,1.070777,-5.284292,-1.449202,-1.704153,7.760068,-9.014660],[-9.056578,6.301757,-3.591755,5.573882,-7.368795,2.026864,-5.294994,-4.798253,4.443224,0.663890,-1.291823,8.756541,8.102539,-5.694597,-5.541882,-3.874904],[-1.272554,-1.816970,-5.880245,5.767574,2.941525,9.300010,-1.595729,4.245036,-4.838960,-6.243481,-8.972032,9.725590,3.219971,-0.118475,-6.801011,-6.378853],[-1.092242,-9.304745,-0.544659,4.253534,-9.518150,6.765970,9.374675,-1.330449,-3.608205,-1.856327,1.551459,-0.146363,-0.331821,-7.951007,6.824470,9.509986],[2.462331,-3.017690,0.699254,5.367755,-2.603981,-5.805221,6.033145,7.667879,-0.721102,-4.230506,8.841730,-5.784347,2.996222,5.470128,-9.579957,9.275705],[-5.656812,5.619686,5.907739,4.681544,-7.371412,1.674464,-2.775047,4.159322,9.393056,-8.775738,-7.191670,-6.859283,3.585463,-1.998858,-3.803151,-6.389490],[9.897156,1.449061,-9.449144,-0.810682,-9.542763,2.327475,3.056412,4.390182,-5.336659,6.511186,4.125527,6.670373,4.369060,-2.546862,8.945069,-9.558825],[-6.974118,8.188480,-6.074528,0.334717,-5.147897,-9.548380,7.537635,-2.279042,2.551791,-7.646091,6.564592,-3.938438,4.329777,-6.801431,9.537521,4.483698],[-4.134905,-3.757416,2.396435,-1.952029,-9.787776,3.902348,-3.076166,-0.423404,9.277336,-6.223830,-8.578423,-0.518893,0.184681,-5.464254,8.806174,4.964810],[-1.352560,1.706564,9.005807,8.668446,-3.797375,-4.944105,-7.298511,-6.369410,2.420768,-2.609946,6.433671,-1.951800,-1.324277,2.585307,-4.174173,8.288705],[8.148635,-7.365329,-8.979531,-6.102452,-4.965584,-7.530373,0.986846,9.813852,6.365418,-5.493215,-2.209465,-1.661530,7.238570,-2.473742,-4.645420,2.510615],[-5.370011,-1.308561,4.980616,4.485808,6.932716,4.226337,7.208599,-5.072291,-3.602555,0.223710,2.557471,8.055435,-8.859545,-1.937869,-2.210078,-2.201625]],[[-4.029270,7.323189,0.819434,9.356345,-9.775135,-0.942782,9.928712,3.128588,3.778070,-5.202060,-6.874015,-4.073477,-5.546100,8.520702,-6.492145,4.979020],[-5.431663,-6.443953,-2.443542,0.745091,-3.025950,-8.176110,-3.577049,-2.823020,-7.395323,-7.984380,-9.568190,9.432208,3.801416,3.317250,-8.650936,-9.543124],[-3.069880,5.189917,1.065656,9.781515,-0.763776,8.364295,3.429557,-4.570098,3.193829,-5.375412,2.560040,-3.634436,-7.237862,-4.857905,-1.763179,-4.444074],[-0.896243,9.920090,-9.776992,8.920668,-4.464359,8.645628,-5.873214,-0.427160,-4.867868,-0.153830,-5.460731,-4.867580,-5.953276,-5.774237,-0.154184,0.472984],[-7.772260,-7.517184,-2.235715,8.431389,-5.213099,-2.975679,-9.692889,-2.301443,-9.268714,7.996528,1.799881,2.341769,-4.870807,3.976835,-0.436958,0.341886],[8.943717,3.893637,-6.829079,6.846192,4.055833,3.739135,-6.641828,-7.714156,-6.936762,6.079504,-0.666307,-0.742216,-8.928442,2.520438,-8.358025,7.469226],[-4.275610,0.423895,8.808438,5.413829,1.007874,5.097344,0.679563,-1.850063,1.682654,1.389730,-5.347969,-4.842249,8.906991,-0.774812,2.893913,-0.774389],[-2.101262,-3.456192,-5.095074,4.614013,-5.313276,1.902199,-3.383860,-8.617605,1.957323,9.624585,5.953633,0.058620,3.369262,-8.009092,2.836161,-5.951135],[9.570438,-9.226383,8.005930,4.124229,-2.472844,5.375555,-5.051878,-1.768232,9.269370,3.058830,2.937532,-6.508431,-4.645688,7.564516,7.956200,-9.175278],[-7.043260,-4.079361,-1.876228,-4.475304,-3.766686,7.875016,5.664914,-9.515487,-4.190197,9.270248,-2.291093,-6.389900,-2.005719,5.972766,-1.889487,-7.787740],[-3.864356,-0.435659,-9.068129,1.428972,-7.503240,1.451534,-0.882981,-9.108018,-5.915194,-4.822386,9.816993,4.187234,6.558023,6.298490,-2.662005,-1.468361],[-0.531631,8.587789,2.892314,9.137534,-3.806649,0.798696,1.125631,0.346252,7.848724,-0.308096,-0.628204,0.448975,-5.370501,4.807949,-3.170991,8.380785]],[[-3.996966,-6.437025,2.192572,9.330102,-9.513726,-0.515557,4.881623,7.542452,-9.710819,9.473030,-0.828513,-7.582576,-8.059240,8.477372,1.634202,3.742375],[-5.333713,-1.238941,-6.524025,9.191090,-3.267979,-3.668978,7.690602,4.706083,7.593676,-7.470498,1.698893,2.173444,5.162673,-2.641440,9.315491,-6.556640],[0.799084,-4.123207,0.420903,9.114423,6.170101,0.738118,1.121577,-1.650434,4.429661,-6.568372,8.846442,-6.493040,8.060668,-0.182297,7.340822,-1.879716],[5.016559,-5.723777,-7.954666,-7.080947,9.542265,-1.180776,-2.059499,7.930068,0.008078,-9.867754,5.899081,3.175081,-5.952762,-8.476279,4.427784,-0.730687],[8.572380,0.661464,-5.448663,2.075788,3.000884,4.997999,5.195275,6.841071,-9.025807,2.701211,3.447818,-4.205915,-3.784475,6.609846,2.741823,-8.662801],[-1.346067,-2.853059,-5.185650,-2.856876,7.111334,2.510500,-0.832612,-0.277151,8.445562,0.492858,-3.506348,-0.087866,-4.767804,-5.544658,9.040518,-6.504575],[-3.624610,8.347370,-0.989937,-8.074595,9.017212,-0.822304,4.953697,-0.422963,8.676898,0.364263,-4.458225,-6.734289,8.687588,-5.471294,-2.830815,-3.122126],[-6.388953,0.370664,6.375197,-4.121792,3.191751,-1.315138,7.374000,2.697410,-0.899236,8.922573,-2.443360,7.106510,-6.777198,3.890498,-8.201175,-1.073434],[9.030968,-4.377374,2.736549,1.733540,5.852998,6.986840,-0.937406,4.493478,3.534571,7.531831,2.813362,6.435738,6.203783,-1.032571,-3.955219,-5.984730],[-1.190936,-9.359745,5.023070,-3.928104,-1.652422,-4.018765,9.206443,0.851096,-5.749063,-8.246660,-5.397194,8.879146,-5.699976,7.751088,-2.133788,-4.746056],[-7.639544,3.139289,-3.096285,3.111968,5.856088,-5.957969,6.579660,-6.582006,-4.895389,7.629491,-8.866370,-1.196513,-4.731604,-9.364905,4.669020,9.214391],[5.169400,-1.544180,7.740220,-1.230468,2.411248,7.006963,6.042396,-0.444503,-4.370840,-6.414217,-4.939821,-6.226748,-7.415979,-3.758492,7.809544,-3.278891]],[[-6.063034,2.161337,-9.753753,-1.044325,-6.098735,-6.414037,9.592955,5.174775,6.968892,1.241376,2.860688,-9.388168,-6.363543,1.754598,8.304853,-6.207037],[-3.981159,7.524233,-4.055161,-8.512893,5.861889,-1.804867,5.377053,-8.509976,6.561215,1.983193,5.725888,-8.442338,-0.574414,-1.584741,4.485125,5.468500],[-8.845858,-0.569701,-0.623903,8.089212,-1.913236,2.176815,1.974650,-7.505352,4.103433,0.889372,9.626223,-9.356403,-3.122982,2.680457,4.126850,8.240216],[3.911226,-0.615087,7.377493,3.738870,1.935274,3.402708,3.687170,5.142936,2.421466,6.731296,1.770060,-4.966395,-3.334273,5.095338,-3.571073,5.407526],[1.345163,-5.977403,8.680501,-4.574029,-2.905262,-7.834211,0.330272,-8.114345,-5.771651,0.004130,7.837590,2.211442,-1.560735,4.012719,-2.929764,-9.457825],[7.866378,-7.103070,3.075855,8.463451,-0.123586,9.810730,-9.020351,8.688903,1.243754,-5.489371,-3.895260,4.357982,-7.054498,-3.823568,1.885735,-0.775539],[0.694604,-8.664418,8.026874,-3.904767,1.688697,8.067659,2.095694,-3.066888,-6.896177,6.250826,9.269825,5.921801,6.009683,-6.302944,-2.850469,4.748482],[2.911343,-3.091831,-5.446213,-9.545011,-5.941691,0.407809,-8.476111,4.907242,-2.086956,-2.988836,8.403681,2.495059,1.560411,4.190384,8.570598,5.815976],[-4.033301,2.178601,-4.560801,-2.734785,-5.688569,-2.662177,-0.172491,9.157401,-8.447724,-3.272067,8.351351,-7.753140,3.783882,-4.116623,2.731401,9.070377],[-9.699442,-2.873292,-5.682375,7.539921,-5.016006,-3.388714,7.499649,3.749644,5.632152,7.601315,9.323751,2.562254,-2.371223,2.622427,6.288841,5.728541],[-6.036051,-3.478791,0.424317,7.508708,6.456073,-8.978884,1.225663,-0.815432,3.751205,2.357855,1.105544,8.967163,-0.952907,3.220422,6.827668,4.514176],[-6.346441,-1.158220,-4.996132,3.042521,5.981930,-3.459406,3.038093,0.917082,8.609116,-3.839991,2.438323,-2.196944,-6.478688,4.326226,-0.113699,0.792513]],[[-6.613881,-2.481747,4.169353,-9.959046,4.346632,4.203987,7.320117,6.054627,7.318080,-6.799283,0.915197,2.778727,-3.465297,0.694100,0.891498,-1.230917],[8.088944,-6.383388,-2.481115,3.981375,-0.524569,2.671867,-7.337099,-5.879228,-3.846981,-4.640126,5.368207,9.597854,2.413054,-0.745272,-6.120791,-4.331636],[-9.677627,-4.104071,-5.400836,-9.441655,8.566742,-3.180861,8.925456,8.299005,9.435827,3.246782,4.210484,4.124036,-0.196859,-7.639755,-8.721001,-6.670581],[0.677901,4.531287,-1.379542,-7.511357,5.306921,6.281120,1.890713,-5.769609,2.344008,9.998335,4.698940,6.388040,4.334657,-3.029717,-5.565713,-9.539229],[2.326651,7.099888,8.350777,1.978002,5.244941,9.552634,-3.563704,7.491786,-7.851219,-2.583957,2.646558,9.889509,5.507987,-3.677801,-8.715485,-4.906921],[6.442898,1.583270,8.049153,8.200052,-2.572174,-7.794408,7.848774,-4.424203,-4.761419,8.085548,-3.266742,-9.165144,-8.635178,4.538120,2.907402,-2.344409],[-7.802595,-3.388030,0.533479,-9.248165,-3.246038,-2.741104,-1.721140,1.360580,6.213191,6.829480,0.809278,-6.869930,-3.606973,-9.306038,0.342752,-5.679078],[1.465421,2.208411,9.953259,-8.207646,-0.092942,0.588801,3.618062,-8.816287,4.558528,-4.808638,1.879716,-1.911873,-2.020470,-4.026691,8.523169,6.870345],[4.860764,9.493371,-1.330238,-1.505511,-8.543589,-7.012752,1.217011,1.017158,-7.358777,3.834062,-1.423589,9.675405,3.050618,-9.775807,4.066517,0.873411],[-9.999444,6.534705,-4.676937,-2.465214,6.029663,-4.890867,6.581226,0.240838,0.246644,9.012929,-8.515505,-3.668969,-0.482243,-8.969174,9.497646,-2.854633],[6.231812,-5.238991,-1.928676,-0.351031,6.150648,-0.203589,-1.086731,-6.589536,-8.567894,1.536291,4.527607,-7.473145,-8.748975,3.388005,-4.208481,-8.387938],[0.194534,9.567234,6.255130,9.893734,-7.726633,4.839028,1.328504,-6.176219,2.910796,-8.592006,-9.702001,6.172796,2.062080,-4.579834,-4.810002,0.802035]],[[9.682391,6.447757,4.196948,-2.012218,-2.954459,-7.759930,5.177624,-7.596393,8.330143,5.539071,3.953468,-5.564312,4.438899,5.790900,8.015716,3.112770],[1.813496,8.581115,3.248913,5.390602,0.479251,3.892509,-3.274780,-2.802443,-6.038856,6.983149,-1.459829,6.825694,-7.510890,8.820506,7.832784,2.591183],[-8.774515,7.445755,-7.281179,7.868135,4.149933,-9.385756,-7.362406,9.797575,9.480432,4.464405,-9.645168,7.625872,8.002648,8.189908,-1.914839,8.557330],[8.563298,-4.345336,9.793620,-9.541309,1.286732,1.629213,7.925770,-2.116941,0.203279,-2.035170,-6.928957,1.240731,-1.294788,8.505129,1.020243,9.537193],[1.784292,-7.932004,-3.779941,3.689401,5.762922,9.356311,7.436565,4.161554,7.514146,8.025717,-6.555071,5.174966,2.474656,7.786933,-2.001536,2.392900],[-1.708996,-8.919324,-5.322626,-5.955738,-8.439180,-1.472041,-8.778206,2.809926,7.544119,1.295533,1.805699,2.992316,7.790678,7.346005,9.786504,-0.473565],[-9.646966,-2.652911,-9.889441,-7.406985,1.959755,8.184677,9.768085,1.146919,9.473904,-9.478829,-6.211443,5.507225,-3.570508,8.178030,3.781291,4.057526],[-1.028299,8.569730,4.792165,-7.572426,-3.711084,-2.337241,-3.793967,1.107660,-9.302287,-5.158172,4.678801,7.777055,-9.256929,9.946260,-4.660182,0.676186],[0.952888,6.283285,-0.662597,9.479096,2.464621,-3.794373,4.293880,3.505358,3.979083,-7.803737,8.962671,-0.496946,-8.526453,-5.637524,1.909600,-0.861165],[-7.971489,1.407992,7.542468,9.993683,-5.896416,-7.455600,9.785389,5.046849,5.139745,2.859489,8.286893,-1.782412,-6.179837,-8.058307,-1.028548,-7.406860],[4.944013,5.694024,-8.103893,6.639496,5.111046,-7.155370,-5.073526,9.211246,-0.426550,-7.416564,9.074165,2.764965,0.905229,0.186760,-4.816597,-9.657534],[7.592437,-1.591509,0.206324,-6.258058,9.139296,6.547807,-0.842431,5.703144,-8.212882,7.398161,-9.714974,5.744878,-7.013987,8.986010,-8.697241,-2.274697]],[[-9.475242,8.827082,8.909084,-1.957153,-9.552425,-8.895913,-4.404152,0.651102,8.309642,-0.357190,-5.884792,-4.689869,-2.604788,9.466973,5.178020,-9.359799],[5.431398,5.165287,7.605757,4.415916,-4.097043,0.558247,-9.049648,5.479101,6.528076,4.245156,2.790883,-0.937914,-7.662780,-5.523440,-7.465063,1.257620],[-8.686760,-1.082570,-9.568063,4.621578,9.413033,7.223471,-8.800084,3.203982,3.934176,6.515016,-6.374356,-4.816266,9.975688,1.508084,-3.232124,5.740621],[3.221167,-1.295294,-9.744594,-3.483860,-5.910717,1.331986,-6.402204,-6.221547,8.681574,-6.285821,-4.394877,-8.131854,3.880847,9.060151,-3.373573,-0.209181],[-4.027200,5.942498,2.061406,-5.644023,-5.241091,-9.743629,-7.797509,-0.716066,-3.867279,-9.144357,2.769279,-9.275919,-3.323641,-9.384234,1.627069,-0.231792],[-6.891321,-1.439938,-6.838344,8.139930,-4.836256,8.843731,9.462887,-3.137069,1.497406,-7.547317,-1.695841,9.428768,-8.272450,5.834884,5.968544,9.490026],[-4.616515,3.667947,-3.359198,9.620189,-4.892674,6.275441,-0.043126,4.034534,-8.490155,-5.104904,-0.603404,3.081262,-5.579049,-3.838400,8.138289,2.136876],[5.881660,-7.814208,0.906094,-6.193869,-6.406839,2.701967,-6.910603,-0.595359,-2.515297,3.055533,5.479541,4.317688,7.326095,4.522419,5.816907,-9.341898],[4.522479,-8.708757,-1.261001,-9.899742,2.074869,0.211534,-4.008692,-7.096822,3.270572,8.828365,1.968084,-2.703085,5.939251,4.617930,-4.453802,8.127052],[-2.788474,-1.453504,4.607778,2.204083,8.637875,-2.075469,5.116944,-8.128622,-9.840096,0.935318,2.543437,-5.801055,1.965826,3.747656,-8.392790,1.273010],[9.626704,2.746121,-6.265968,0.521360,-9.025395,0.299789,-6.580912,-3.253194,5.046780,-6.045578,1.879266,0.985493,-3.323905,-1.234169,-5.715436,8.488091],[3.304637,-5.421500,-1.010423,9.846543,0.636463,-6.332225,9.319555,-0.313934,-9.732577,9.548624,5.899918,-2.946220,7.026296,-6.700040,-7.500104,7.113202]],[[3.801919,7.119093,9.613282,-5.727887,7.468913,2.530373,4.093600,9.528015,-1.765655,5.439678,-8.779116,-2.993666,-3.862697,5.320981,-6.398268,-8.242504],[-8.905129,6.313959,3.177904,-7.337563,-8.976304,9.701002,9.353221,5.563452,6.224781,6.883267,-3.022858,4.133447,5.908002,6.087800,-1.682465,4.686167],[4.500551,-8.798840,-5.732434,7.279838,-2.345626,-1.605150,-7.348018,-5.776269,-6.932599,2.937799,0.735021,8.131678,2.163921,-5.348012,-0.462206,-0.295425],[5.048249,-5.917258,2.422799,-5.323737,-7.942220,2.132602,7.784870,-8.346012,8.920113,-4.446199,7.166796,9.785484,3.292008,-9.975771,5.773914,4.403900],[7.317546,-7.116023,-5.134126,2.590108,1.819713,1.839974,-6.635004,-5.004798,8.229324,-5.831511,-3.278805,7.472515,8.331222,-4.533677,-2.540695,5.889557],[3.495528,-3.057987,4.697768,3.654095,-3.767874,7.777985,-1.308034,-2.142709,-8.103782,-9.121947,0.220057,-3.949974,3.230580,6.879417,4.973803,-0.720603],[4.241054,-6.580854,-3.994353,9.962931,-5.959838,5.545865,5.633668,-1.774005,-8.535745,-5.923511,-8.964284,-0.601221,6.931845,0.667041,8.202559,-5.399630],[-1.823623,0.498128,-7.739158,9.992698,3.789140,7.903450,-2.666778,-9.260372,5.548953,-4.561109,-7.218973,6.405895,8.168667,-7.640568,-5.348651,8.022198],[6.684965,1.690190,3.711030,-7.118211,8.968250,1.273062,3.023063,-2.755016,3.745693,-6.840581,-2.362256,4.681069,-2.452368,-1.332933,-1.432860,7.272231],[-3.430349,1.347073,2.890040,-1.572001,-0.169544,-3.067665,2.179563,-5.455736,-1.169337,-9.850659,-5.213498,-3.797220,3.909784,-1.995915,-5.362456,8.702100],[-8.723963,-9.480403,-0.515705,6.560585,7.720619,-8.172059,-5.895388,9.339221,7.117016,8.962541,5.772927,-1.825567,-1.575027,2.017787,-8.194442,2.224513],[2.521223,-9.774530,-6.223241,-0.716283,-3.805505,9.258788,1.940263,4.919172,-6.106589,3.189246,-7.297054,7.032901,-9.195847,4.861225,7.412162,7.015945]],[[-1.318984,4.574153,1.617568,-5.144262,-9.966671,4.342163,-9.931439,8.772411,5.187965,8.147804,-6.192939,7.786053,8.796804,-5.639007,8.038863,5.102772],[0.041326,9.065347,1.969418,-0.256772,1.761011,1.064458,-1.969548,-9.096880,9.900485,7.293634,-0.356153,-5.187593,1.026946,7.268470,1.822609,1.605798],[5.484484,7.038469,-8.337887,-8.855068,6.446454,-3.630650,-3.011833,-4.725429,-0.513045,-8.823408,-1.218321,-2.538724,4.412013,-2.718407,-7.649219,8.992049],[-2.392972,-8.729686,8.238028,-3.052388,5.368833,-2.152589,-5.124211,2.567996,6.039539,3.818538,1.330667,8.338841,7.052436,3.848837,9.787938,9.112580],[7.857628,7.947761,0.401700,-0.016792,-4.097259,-2.079207,1.498943,8.540209,7.211192,-8.430579,-1.442231,4.477645,7.384468,4.883288,-1.875164,8.452571],[8.513530,-9.383248,-5.284101,5.715787,0.007090,8.864170,3.518144,7.125192,-8.765951,8.974323,-1.574333,-1.345151,4.107165,-2.199451,2.805337,-9.881224],[-7.715438,0.139841,3.233860,7.103085,-7.111577,5.031518,9.804498,9.717196,-2.476168,-8.474683,6.952448,-2.886841,4.836198,-6.844326,-5.273798,4.694208],[8.097106,-7.248695,1.205795,-6.531380,-4.743436,0.804783,-7.656236,1.975269,-8.226799,5.478235,7.844347,-4.197630,9.807025,5.483949,6.332264,-2.157197],[1.907885,2.663471,8.568212,-9.437180,9.682686,8.180827,-1.806922,-2.593542,4.996131,8.030520,-9.457920,4.197720,-2.783771,0.048184,7.733293,0.207757],[-5.487111,4.740372,-3.049915,-8.422714,5.411110,6.685464,-3.357696,-0.357402,-2.766539,-2.934289,-7.950201,-3.522828,-2.814226,-6.139749,1.519362,-6.613556],[3.821484,0.045108,-7.718013,5.513809,-8.047782,0.349686,8.633198,-1.585137,8.640641,-6.412956,-7.224601,1.257199,-7.335271,-8.310184,7.238411,-0.156655],[-2.930369,-7.671255,7.662647,-2.797066,-9.402705,-6.624349,-5.429583,4.750483,-1.948275,7.860224,-6.747832,1.830589,-0.405257,1.616769,9.001612,-1.404265]],[[6.883487,-7.993505,1.347579,-0.217586,-8.714601,5.091303,2.691961,0.707842,-5.273598,-3.371677,8.350783,2.401824,4.806773,8.863914,-7.868578,-0.902932],[-6.579607,-0.037997,-6.622788,8.597225,-5.191357,8.661579,-8.188858,0.932080,2.746956,4.523994,0.856329,-5.371039,7.673360,2.453226,-1.042385,-8.228289],[-4.759332,-4.964336,3.349691,-5.222729,-1.099038,-0.642146,-1.658957,8.711698,1.286315,-1.319505,9.390872,-1.011540,-4.424666,1.608961,5.637809,8.462471],[-8.763406,-8.159333,0.039901,6.798633,-7.396406,-6.575830,3.852900,-8.597404,0.940508,-3.179006,-8.167086,0.987336,-2.595102,4.979514,-7.094612,-9.409974],[-5.465274,2.152980,3.747968,2.826890,-7.905399,-2.277482,6.342954,-3.723415,9.305988,2.914923,9.231377,-6.463873,4.935369,-7.212940,-4.377602,8.502568],[8.543138,-5.590792,0.187382,2.634108,-8.973977,-5.345936,-4.235518,-0.575412,3.147576,7.836534,-5.286693,-0.272376,3.667419,-2.509448,4.956419,-9.708015],[-6.562667,8.087890,-0.011991,8.565929,-1.983655,-1.458089,-4.247129,-9.453995,0.139629,7.700591,1.249085,6.397271,-0.025041,-0.807851,3.905363,-7.869662],[-8.089597,-4.294477,-6.802865,2.458098,6.396124,-9.625225,-0.678006,6.302024,-3.846223,2.628726,-5.702150,7.354577,-6.184404,3.782511,-0.414918,9.995992],[1.610196,-0.920605,2.622070,5.314349,0.188834,4.542469,-1.638765,8.054179,4.114115,4.637204,-6.484533,-3.729835,-3.723316,-5.413892,7.186916,4.175099],[4.566737,1.715547,8.413646,4.368063,-1.721838,-0.618279,5.528883,9.784519,3.475967,1.717846,3.931425,-1.378946,0.914664,6.386652,8.117621,4.447535],[-3.827147,0.403011,1.510624,-5.934033,5.926818,8.540527,0.511907,8.752016,1.364534,-6.370550,-4.688493,-0.437237,5.232805,2.622957,1.133115,-2.621751],[7.441293,1.321706,-1.911780,-4.212732,9.379622,3.073053,-9.124298,5.635274,4.060008,0.223235,-2.168585,2.340883,0.297242,-2.442223,2.470045,-4.596858]],[[1.781335,-8.382478,3.368520,4.241112,-3.614753,7.450894,-0.467366,-7.209540,-5.822783,7.347743,6.592553,9.746944,5.304478,4.491139,-9.554459,6.134245],[-0.739737,5.043887,-6.959565,-7.385527,2.797514,-8.093445,-8.787120,8.149632,-5.706153,9.569569,4.512874,-4.551836,7.064500,-9.075906,9.575244,8.765175],[2.609195,4.787600,6.474453,-3.905625,-0.893083,-6.944761,2.482902,4.251065,9.989809,2.833983,1.927387,8.719063,-1.235605,-0.749539,-2.829929,0.192507],[0.678710,1.599610,-3.822510,1.444073,-7.947773,7.956798,-9.100058,7.828669,7.563151,-5.099367,-3.820709,8.057422,1.374175,-8.474783,0.020412,1.364850],[6.362977,-9.051594,-2.295239,-9.949161,6.572994,-2.497661,-9.860228,1.332151,1.214218,4.011916,-7.539201,-0.100358,-4.585685,3.750410,-9.648987,-2.167767],[1.878054,1.994873,7.279915,6.312254,5.069003,-1.349618,9.556719,6.887814,4.153494,3.684314,-3.893314,-6.697164,-5.489715,-1.576837,-6.581612,-1.402678],[1.773053,-7.483521,1.246658,-0.155601,2.328264,4.090829,-0.431391,4.079948,4.969671,8.044663,-1.455560,-1.992683,4.149656,9.380116,-3.617381,-6.074143],[6.885113,-3.787002,-0.884057,0.114571,4.384714,-1.444882,-3.497953,8.102606,-8.642750,9.487243,-8.101841,-6.706999,-9.743413,-2.311743,7.049755,2.435957],[1.537638,-8.205701,-6.681170,6.546956,-0.167442,7.589221,-1.325498,-2.795575,-1.850048,7.413330,0.604849,-6.818676,-7.216922,-6.005837,5.421809,-7.964601],[5.557806,-7.587550,1.045712,7.248402,-5.148292,-6.068422,-7.930522,1.609869,-3.881645,8.589860,-0.085820,8.138078,-2.619217,9.634843,3.211762,-3.364267],[-5.288040,-5.294149,8.397292,7.288472,2.881642,-8.674953,-0.078222,-5.696190,-3.339183,-6.116467,0.761713,5.987143,-5.169542,-2.666248,5.135165,-7.018985],[5.144177,0.972309,0.108433,-8.638841,-8.952915,-0.872338,3.331246,4.749737,-1.698708,-3.443771,8.901394,-9.162820,-4.889260,-2.158592,6.596769,2.712801]]], dtype = "float32")#candidate|3701|(15, 12, 16)|const|float32
uop_3702 = relay.sigmoid(const_3701.astype('float32')) # shape=(15, 12, 16)
uop_3708 = relay.tan(uop_3702.astype('float64')) # shape=(15, 12, 16)
uop_3712 = relay.cosh(uop_3708.astype('float64')) # shape=(15, 12, 16)
output = relay.Tuple([uop_3712,])
output2 = relay.Tuple([uop_3712,])
func_3714 = relay.Function([], output)
mod['func_3714'] = func_3714
mod = relay.transform.InferType()(mod)
output = func_3714()
func_3715 = relay.Function([], output)
mutated_mod['func_3715'] = func_3715
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2564_call = mod.get_global_var('func_2564')
func_2566_call = mutated_mod.get_global_var('func_2566')
call_3745 = relay.TupleGetItem(func_2564_call(), 0)
call_3746 = relay.TupleGetItem(func_2566_call(), 0)
output = relay.Tuple([call_3745,])
output2 = relay.Tuple([call_3746,])
func_3760 = relay.Function([], output)
mod['func_3760'] = func_3760
mod = relay.transform.InferType()(mod)
output = func_3760()
func_3761 = relay.Function([], output)
mutated_mod['func_3761'] = func_3761
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1574_call = mod.get_global_var('func_1574')
func_1575_call = mutated_mod.get_global_var('func_1575')
call_3778 = func_1574_call()
call_3779 = func_1574_call()
output = call_3778
output2 = call_3779
func_3784 = relay.Function([], output)
mod['func_3784'] = func_3784
mod = relay.transform.InferType()(mod)
mutated_mod['func_3784'] = func_3784
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3784_call = mutated_mod.get_global_var('func_3784')
call_3785 = func_3784_call()
output = call_3785
func_3786 = relay.Function([], output)
mutated_mod['func_3786'] = func_3786
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2800_call = mod.get_global_var('func_2800')
func_2802_call = mutated_mod.get_global_var('func_2802')
call_3787 = relay.TupleGetItem(func_2800_call(), 0)
call_3788 = relay.TupleGetItem(func_2802_call(), 0)
output = call_3787
output2 = call_3788
func_3794 = relay.Function([], output)
mod['func_3794'] = func_3794
mod = relay.transform.InferType()(mod)
output = func_3794()
func_3795 = relay.Function([], output)
mutated_mod['func_3795'] = func_3795
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3714_call = mod.get_global_var('func_3714')
func_3715_call = mutated_mod.get_global_var('func_3715')
call_3796 = relay.TupleGetItem(func_3714_call(), 0)
call_3797 = relay.TupleGetItem(func_3715_call(), 0)
func_1186_call = mod.get_global_var('func_1186')
func_1187_call = mutated_mod.get_global_var('func_1187')
call_3798 = func_1186_call()
call_3799 = func_1186_call()
func_3784_call = mod.get_global_var('func_3784')
func_3786_call = mutated_mod.get_global_var('func_3786')
call_3800 = func_3784_call()
call_3801 = func_3784_call()
const_3807 = relay.const([[[-7.107227,-9.534057,3.167039,-9.947800,-9.732377,6.309298,-1.520592,5.695955,8.749756,6.646060,3.530962,-6.265621,6.413119,-2.457411,-6.525945,5.314594],[-1.256842,7.515025,-3.403785,-1.465663,-1.761259,-0.306789,3.257203,8.172834,5.785750,6.400035,0.886722,-1.806902,-2.020565,9.635270,-9.859938,0.479998],[-0.378347,-0.166240,-1.332974,-2.771735,7.115341,3.955597,-7.827660,9.583879,-9.983543,-0.532176,-9.039302,-3.736045,0.367168,2.669244,1.039684,0.116959],[-0.482452,-8.074655,-0.139879,9.424486,1.618155,-1.367946,9.791783,-5.791278,-1.521534,-1.133966,6.740420,8.939138,-6.229504,-1.667488,8.305960,1.433028],[-2.045292,6.155315,-1.117606,-8.923569,5.849061,-2.079138,-7.517309,-8.995764,2.411727,6.183984,-4.570140,-5.092857,-2.497252,-3.105452,-5.267787,4.932053],[9.381946,6.711347,9.120372,1.340680,8.989290,-7.218794,-1.232700,-3.923233,1.862416,-6.726944,7.666858,-0.299560,-7.223256,2.295082,-3.455878,6.409567],[9.675950,-1.653982,-5.322279,-0.780451,9.696502,3.117996,2.560965,9.218708,0.734990,-0.140363,-7.530357,-7.317083,4.282874,7.219162,-8.170039,2.822120],[-8.419484,1.421849,-3.771179,-0.052220,-1.541080,1.224184,6.873872,-1.594235,6.110894,9.019864,9.248685,-6.061518,-8.338365,-3.841310,-7.654386,-1.595665],[9.292106,7.805809,8.758116,8.059804,7.426013,-8.021440,-1.819879,1.593536,9.392491,3.946573,9.966067,-7.680381,-0.189019,-9.587814,-6.431693,2.803617],[-0.745760,6.505796,-2.658975,1.790447,-4.307563,-5.885620,-4.181171,-9.117808,3.278784,-5.573758,8.749441,-9.238414,-9.718938,-9.708724,5.360314,-3.833852],[-2.123862,-8.922007,7.240240,-6.838304,2.553298,-5.604162,-3.659513,7.060475,-4.272722,-2.552466,-2.845202,6.745903,-1.786153,-0.393469,3.301087,0.106901],[-4.309769,-4.367196,-4.070055,5.172346,-1.999309,6.141694,-9.528354,-2.704953,1.134088,-8.496231,1.793296,-5.340997,5.571691,8.325320,6.203899,-4.556312]],[[-5.378434,7.750123,6.638818,-5.594695,-1.878442,8.598140,9.186559,-5.848381,-7.422974,-7.162675,-1.252628,6.411576,6.276551,9.223466,-2.959173,8.806516],[-1.794006,1.499909,6.227642,0.946383,7.203058,6.537697,-4.546634,8.855940,-2.581123,-7.431597,-0.630538,4.014310,5.922875,3.209980,-0.746649,-1.489622],[4.928827,1.961154,-9.781868,1.352260,6.756017,-4.092940,-8.346873,-4.829954,0.725698,8.499395,9.957952,-3.875727,4.220187,-5.980931,-1.826882,5.648696],[-7.561214,-1.791776,7.462617,-9.441108,-5.511833,7.415762,0.127755,-2.677057,-8.726177,-1.520952,-3.953205,-1.388176,-8.546689,5.895223,-9.558650,7.780746],[1.240715,5.909955,0.577897,5.287916,-0.642588,-1.998676,1.489261,-0.977577,-7.053222,9.570691,8.576314,0.866922,-8.405454,-0.847371,8.863711,2.547409],[-2.897181,7.291058,-6.130490,3.410934,4.481919,-1.586668,-1.965980,8.092541,-3.499387,1.102597,-3.381156,6.026602,-3.991574,0.726417,7.936552,-9.603043],[0.976200,6.346833,1.568668,-8.612861,-7.651885,9.455002,-7.199675,-9.359975,1.422188,-9.508653,-6.209455,-9.310975,-0.025710,-5.392948,-3.454956,7.868334],[-7.469786,9.798111,2.594851,6.426214,4.196449,2.833797,4.933321,-3.872379,2.838419,-8.526666,-8.197579,-0.204033,9.940689,7.523711,-1.319020,7.472063],[9.071258,-3.855668,9.509620,3.069159,-4.564908,-2.899064,-1.378380,-4.037119,3.442929,8.159493,5.309557,-8.206565,-3.369702,-8.637188,-9.805193,0.670508],[-9.175804,4.543566,9.288418,-1.145093,1.365378,7.902642,7.936580,5.718855,1.686340,6.951339,4.153932,1.319116,6.860151,-3.875396,9.025161,3.032582],[4.082306,1.611695,0.671886,-3.005567,-1.223507,-3.070302,4.118422,1.750948,-2.113506,3.435383,-1.666987,1.781193,-9.794110,-8.769647,-2.925838,5.619036],[-1.131326,-7.249207,4.735163,-0.121502,1.287082,5.444537,-3.449565,5.133577,6.103930,-0.220010,8.480967,2.917564,4.067744,4.672248,-8.482402,8.767061]],[[-1.144625,-9.294850,-6.487135,8.486506,-4.679200,-8.630813,1.486010,4.347725,-8.797380,0.202797,-9.008678,6.291922,-5.420859,9.160457,-1.917253,2.480639],[-3.026536,-4.856298,-6.329604,-6.938157,-2.486796,6.842078,-1.952868,9.496851,2.684729,-8.157606,4.422689,0.749669,7.150533,-3.936972,-8.984853,-3.326409],[-8.824930,9.931743,-1.626501,5.111637,3.600919,7.913643,9.156839,-8.250698,5.147667,-6.419200,8.419157,-8.421783,-9.729389,-9.470103,-9.201134,-2.374428],[6.904210,7.499482,5.247502,-0.011944,1.009179,6.576488,-4.420684,8.979852,-7.466117,3.265837,-3.580542,-5.921191,-3.363409,0.062363,6.886259,1.412500],[7.824403,2.678003,0.360856,2.381213,2.909243,-9.471969,5.576119,2.104587,8.627590,0.660824,-5.837842,5.951109,-2.883788,4.279939,-6.708134,-8.934006],[3.904103,-3.761896,2.531143,9.427060,-6.937801,3.948411,-2.203168,-9.435580,2.575951,4.645664,8.304009,-7.690571,1.054491,-1.289000,4.373467,2.918286],[-2.529569,2.366417,-5.008494,-6.707732,-1.108336,-6.953925,-5.565557,2.162371,-6.834795,3.696312,4.397298,7.322493,5.509371,-8.500006,-7.137799,3.187667],[6.561869,-1.254075,4.261839,8.751353,-4.576973,-1.026352,-3.381136,-3.406275,-8.000138,-1.108781,-9.419423,-7.816066,9.182147,-0.482645,6.014875,-9.632752],[-7.882801,-6.119016,9.569825,-4.023256,5.378563,-8.140419,-8.964509,-0.570253,-0.367052,-5.488767,-1.153194,-6.298411,0.759891,1.559007,-9.863177,6.544864],[-0.450838,8.467325,8.606214,-6.004617,-1.411942,-1.511431,8.954664,-5.073238,-5.175937,-1.710129,1.847754,-0.080457,0.932972,0.801573,-3.571927,4.100525],[-5.669725,-6.057789,-0.327231,-8.966822,-5.752567,9.865348,9.287508,0.894300,-9.146680,-1.239795,5.548385,-1.216944,-1.885689,-1.626952,-5.148872,-0.423108],[-6.848581,5.618143,7.523236,-1.316636,-4.945045,4.287573,7.753989,8.641120,5.831841,1.912960,7.043980,9.977283,-4.688882,-1.057241,6.116556,4.812315]],[[1.287030,-6.370113,6.766837,-6.524640,-3.796161,8.254007,1.409786,5.563350,4.244449,9.954111,-1.850179,-6.711821,-1.280749,-1.219479,7.778446,-5.419155],[-9.674274,1.481481,2.172197,7.059412,-5.920196,2.522160,-4.628945,-0.813553,2.865216,-3.096213,-9.600108,-5.359549,7.071547,5.687472,8.892787,9.108391],[-5.647932,1.921220,9.744861,-6.752601,2.743404,8.362812,-7.137819,8.482307,6.915604,-4.918234,6.179440,-7.940145,1.722026,3.810312,1.357947,-2.381922],[-2.408411,2.462094,-7.224153,2.577282,6.168643,8.305592,-6.075734,-1.668335,-7.558192,6.316444,1.482748,-8.346623,1.836881,7.601745,5.587752,9.651746],[5.915534,5.669521,-2.343581,-0.769179,1.637039,4.386763,-8.220987,1.899506,-6.628493,-4.612801,-5.020542,-3.662814,5.807349,1.747779,0.998527,-5.929373],[4.106503,7.092794,-6.957049,-7.493894,5.473056,5.053797,6.877248,5.614032,4.408135,2.137656,-6.104530,-6.382355,-4.267252,-8.036135,-8.915022,-6.673459],[-5.421562,0.815482,0.014784,-9.557222,9.932677,6.912350,-5.009811,7.851664,-1.444035,-2.034415,-4.270319,-0.307967,-3.334431,5.771696,2.287690,-0.398224],[2.894334,-3.480858,2.356924,7.164461,-9.213591,3.575945,4.206533,1.551660,-7.139170,7.167479,-6.419610,4.809038,-8.040048,8.434351,-8.186399,-9.440613],[0.152893,7.868767,6.834302,2.784091,1.771224,7.341514,5.081515,-8.348419,-4.734090,8.555808,-9.572715,6.981901,4.274610,-8.479126,-3.752030,5.066474],[-2.150297,9.149254,8.807946,9.967158,4.575819,-6.391087,1.174873,-0.070353,-7.172443,-9.565321,-7.632412,6.175876,-1.909333,-0.034022,-2.626638,-7.280537],[-9.501132,1.420283,6.152866,-0.790767,5.006744,5.329153,2.247959,-6.077273,7.567817,-7.254525,-1.891236,3.782838,-1.286348,6.672808,7.495869,0.223097],[4.315906,-3.040339,0.816977,-8.271030,4.248944,-1.574711,9.854097,-5.088719,2.340970,8.588061,-6.197163,3.253219,-1.170135,-9.997984,-8.615058,4.017154]],[[-9.585762,-9.007200,-6.389410,-5.122853,4.072326,-3.486039,6.078295,1.604121,-0.886356,-6.740194,-9.987430,3.475903,-6.496220,-7.232692,1.947027,4.828770],[5.549223,5.736357,-8.822879,2.751106,-6.026598,-1.379168,-0.588707,4.002094,-2.740583,-8.350797,8.982974,6.544305,2.033607,-5.546451,7.582468,-2.392754],[-1.260537,-5.802007,3.802432,-5.527914,-3.349586,7.665801,-5.961841,1.592176,-5.813560,3.625669,4.722850,4.422415,2.594681,1.511407,2.912979,6.085899],[3.499171,-1.214307,-7.466898,5.649524,-0.550680,0.303259,1.416510,9.269711,-4.887624,2.255556,-3.228092,-9.362487,-1.814680,-5.825568,3.922012,8.453008],[-0.574300,4.199056,-3.916340,2.647265,6.921381,-2.317167,9.688623,-6.853192,-4.142614,4.185264,2.819500,-8.152876,6.626751,8.305914,7.629071,9.722065],[1.538036,-3.940793,8.867789,-0.036109,-8.688169,6.400014,-6.065407,-2.829142,8.086300,6.122689,1.725963,2.009098,1.215390,-5.148864,4.450867,-3.789016],[-6.027324,6.285294,-1.541924,7.134157,-6.209198,-2.967665,-7.438969,7.133102,-3.166816,-7.775628,5.275827,-7.123022,9.112080,5.213196,-3.341970,4.120003],[-1.571828,4.408590,-9.241255,5.205933,8.461314,4.359748,-9.336214,-9.836281,-7.832545,2.706724,-5.532831,-1.234267,-2.986860,-0.392332,7.684182,9.828244],[-8.701993,-3.186383,9.241785,4.347191,6.649264,2.427508,-4.486291,-8.199077,-6.631489,-6.385367,4.971216,-2.836764,-7.862983,-6.068048,-1.407216,5.318233],[-5.521591,8.687080,3.032903,9.915452,-7.254998,0.741429,-1.036505,1.974248,4.867275,3.037197,-5.058309,-7.632086,-6.304062,-8.058254,-9.867259,-6.344115],[3.254897,6.768929,-5.332882,5.603074,1.983474,7.257436,-8.846297,-2.210303,-7.833807,-0.214832,-4.346002,8.558042,9.476182,8.951237,3.590219,2.621097],[-3.874418,-1.448088,0.950322,4.702615,-8.612730,-8.249422,5.246931,-5.346156,-8.107458,-5.774689,6.080376,4.821780,2.960561,-6.619456,-4.068278,8.556454]],[[-2.862970,-7.541340,6.662202,-6.918417,-0.015762,-6.892492,-6.757255,-2.339563,3.181243,5.990371,-3.572867,9.267467,3.017857,6.370230,1.001172,-3.344324],[-7.158004,5.840954,-9.345355,4.569475,-8.982802,-5.112170,-3.389130,5.885756,2.205187,-5.306364,-2.483915,8.919512,0.240032,9.952305,2.460963,2.415289],[-7.169163,5.488726,-2.316806,-2.393703,-5.350591,8.539431,2.132654,-5.868070,0.663950,-1.825116,2.666040,-1.397325,-4.554201,7.221282,0.232653,1.652935],[-6.868369,5.507568,2.944134,9.873715,-2.950157,-4.152945,-9.445640,3.633259,1.879149,2.200918,7.629358,-2.754603,5.487035,-1.031452,-1.227734,5.889493],[-0.657830,2.690403,-1.650117,-4.774415,-0.628658,-4.863764,9.935827,-0.608623,0.170483,3.005780,4.393610,7.616097,-6.100109,-2.079126,5.830128,6.718035],[-9.721172,-7.198608,0.249656,1.737853,6.317429,-2.406990,9.836571,-6.745396,-2.929571,-6.783366,9.593647,1.362354,3.982089,-6.112905,3.542205,-8.525407],[-4.275310,-8.856849,9.180802,2.221895,8.504715,-0.189589,8.358613,4.344492,-0.095789,4.182125,7.912242,1.448250,-5.499165,-3.350898,6.384023,9.342943],[5.200965,-7.112463,-7.043064,3.999342,6.114666,-7.204132,-4.750176,1.635666,4.008958,-5.520714,3.266148,1.256455,6.372978,8.249823,0.628350,0.095556],[-7.000452,4.543844,1.499056,-0.071788,-5.767240,5.234895,-8.959095,-4.062778,-5.951946,3.750547,-2.017614,3.282907,-1.681626,7.652796,-5.510505,-1.000264],[-6.249124,5.871951,-5.091659,-0.632696,-0.495227,-4.241435,-2.870768,4.141389,5.410716,-2.018526,3.094339,-2.813905,-5.715105,9.929701,-6.566858,5.384276],[-3.924486,-0.896475,-2.986220,5.128867,5.049571,-6.460398,-9.859964,-3.226509,-1.130448,-5.368376,-3.598547,2.057968,-8.700308,4.601195,-9.961291,4.188201],[3.434834,2.977717,-7.299449,4.050197,-4.244127,-3.046438,3.477729,1.844541,0.859959,8.043776,-6.693529,6.394780,-4.064896,1.377739,5.702636,2.712762]],[[-3.068532,0.041326,5.468816,-1.682902,-2.194384,0.749549,8.218862,2.202051,-3.257105,8.940745,0.758644,1.547669,4.237280,-8.668018,5.798024,-4.358560],[-3.377990,-1.945824,-4.904362,-0.072912,9.878147,-2.762366,-4.784394,-5.222599,-4.656800,5.617641,-1.628664,4.536488,1.152924,-1.300001,5.156310,-1.637460],[-9.140147,-3.489461,-9.560610,5.911103,-1.728363,-1.109757,8.535732,9.123967,-4.206577,6.588508,3.334185,8.986624,-3.584128,2.067536,-1.612840,-1.858447],[-4.172263,9.986522,9.797509,4.074650,-1.977024,-0.255009,-3.273304,0.620366,-6.928025,2.194155,-1.081077,-4.594366,-9.513356,-6.294227,5.641847,-4.516709],[5.650095,-2.743192,-4.541894,-6.451687,-7.537949,0.764396,-1.316616,6.536656,6.078123,-0.685592,3.590503,5.241757,-2.155895,-7.368574,-8.569507,-0.776038],[-4.899260,-7.244712,-1.653901,9.977772,3.750881,5.431486,-2.707711,-4.862461,9.917423,6.054458,2.593254,-5.737523,-6.058197,0.501663,2.283473,4.779007],[8.558088,0.464009,-6.361240,-5.962429,3.706497,-8.846150,-4.179016,7.435744,9.664461,5.020773,2.539083,5.286151,-2.080750,-6.732208,-6.263401,-4.287423],[4.469599,1.648110,-0.519771,2.232413,6.370687,4.639466,-4.676470,0.652895,0.107422,-2.161780,-9.803021,0.898405,1.350338,6.989031,4.633679,7.225613],[1.369403,-9.030599,-1.674669,4.342965,2.732329,2.793182,0.895548,-7.072531,5.214457,-8.663979,-2.446069,5.397451,9.828365,8.315782,-5.897082,-5.784412],[3.729910,5.836702,-9.216359,2.861845,-6.285019,-9.631846,5.262361,-8.034538,9.977341,-7.440949,-3.483480,0.968491,-0.900618,-1.387070,1.286942,-3.340271],[-4.373589,-2.966247,-6.581639,-7.560505,5.107038,3.407202,1.308939,4.587505,-9.308221,-7.922563,0.401080,-9.874712,-2.715074,-6.577009,2.501654,-2.817253],[8.281294,3.070304,-0.489235,-1.335432,-7.527925,-7.055477,0.023781,-6.801323,-3.304764,5.601061,0.139482,3.193057,-0.978045,9.798025,8.125644,5.532531]],[[5.949536,-8.650644,4.040349,9.604162,-6.649206,7.620199,7.306662,3.719082,4.244238,-9.417150,3.275099,-0.408620,9.688550,8.939386,-7.653564,4.315992],[0.189702,0.785161,-8.146031,-9.667338,9.592370,1.595259,-0.360515,-6.736076,8.951883,-6.631242,-3.867962,-7.423225,-5.402082,-4.274537,6.730235,-8.965802],[-4.397908,1.671709,-6.802511,8.632252,1.840656,7.095166,-0.701150,5.572423,-3.453858,-1.077493,2.991268,-6.020539,-3.747865,-6.749186,6.603016,4.617357],[-5.170131,-4.546500,-0.682494,-5.476434,-6.623093,5.466896,9.226808,-6.509753,-4.482029,5.595814,-3.940588,-5.279056,-2.839128,-3.037780,1.879332,9.963023],[-6.318592,4.930441,-9.416767,-3.654063,0.250396,0.823997,9.502246,-6.944483,-1.472948,6.086408,6.099325,1.042799,-5.624607,4.863749,6.000918,2.366233],[2.689350,5.418650,2.465287,-6.854584,5.633224,7.849426,-7.466245,3.200209,6.957173,2.208348,-5.183580,6.873774,-1.156421,-3.063534,6.048061,9.529758],[-4.827441,-4.161335,-6.388806,-5.069305,-6.498012,-9.556812,4.788036,0.996395,-4.431476,-6.003447,-1.325844,6.852709,-2.385252,-3.006924,-9.679386,-2.730126],[-8.022837,-9.242882,-5.727148,3.274101,-0.155041,7.896012,7.907552,6.944364,2.069984,-8.431201,2.697288,-9.285448,2.339020,6.551973,-9.215243,6.332476],[5.205901,0.626274,-8.219945,-1.459656,8.391633,6.660202,6.283399,-1.728546,-4.848947,-0.523958,0.918592,9.522927,4.725646,-2.198212,8.371781,5.798676],[6.362203,-2.232378,4.475410,-8.247142,-5.152104,4.435257,-0.841454,-9.380633,-4.992691,-5.181594,5.391208,-3.912292,9.817914,-9.998306,-1.825469,1.977144],[-3.858131,-0.491542,-3.605855,-6.794380,-9.112287,-4.474238,-2.169161,5.975652,7.954873,-8.077394,3.959605,-6.182449,0.759937,5.721552,-6.366029,2.749211],[-6.727309,-3.299342,-8.511488,5.798846,-8.473439,-9.052008,-7.271636,7.959200,8.058099,-4.629787,-1.072432,8.026591,8.633281,-9.473756,9.126006,3.169484]],[[9.879460,3.096567,-6.205487,-1.261893,-1.928881,0.890402,-0.904266,2.680229,-2.579828,-0.387207,-3.133109,-7.511003,1.885744,1.716959,-2.183634,-3.265938],[-7.542367,-3.823307,8.056807,0.666510,9.756387,-9.509666,9.988103,8.432432,-1.983639,-6.516683,-7.531638,-5.654291,6.328595,-4.409399,-4.478081,8.684951],[-0.409340,-1.963555,-1.892270,-4.082314,-6.774520,9.501209,-5.045667,-9.925548,2.456574,2.435134,3.870144,7.415290,0.666813,1.013899,-7.891804,-8.751494],[-8.608725,-9.430718,-5.420462,-3.465959,-3.979607,-7.878620,-8.823486,6.470914,6.219563,4.777485,-2.742032,-0.163627,1.713517,-8.640117,-3.674815,-0.373567],[1.337725,-4.708417,8.297633,-2.073769,-3.936047,-6.354610,7.041654,-4.919983,-3.985583,-3.141733,-1.335680,-0.071441,-6.333767,-9.815454,0.570335,7.983234],[0.698518,-9.152374,-0.289247,-4.229009,9.825954,2.489868,-0.161823,-5.866944,-6.348117,-1.965957,6.889468,-3.406749,5.770214,-4.711823,3.362897,9.036726],[0.472281,-3.218003,-0.411576,7.323053,9.195510,3.904553,-2.434372,2.728711,-8.350566,-0.285312,-6.465259,2.295011,7.486917,9.007467,3.210982,6.988561],[-4.021187,-5.980844,0.880885,3.995387,-6.269436,-2.719010,-1.599692,2.126815,4.040861,-8.914107,-5.280877,6.538771,5.354227,2.285258,5.226658,-2.900626],[-8.700632,1.734217,-7.665389,-0.411087,9.935408,6.345186,-7.468780,-1.264534,-8.604258,-3.851549,-1.377645,-3.784743,-5.467611,-6.557931,3.031604,0.487119],[7.874847,5.363412,3.790446,-2.767612,-8.303611,-5.360508,8.364687,1.726442,6.336695,-4.138339,6.971199,-3.184615,-3.151678,-6.890766,9.944389,0.406283],[-9.559190,-3.821860,4.264173,-2.727196,-3.135979,-5.085994,4.944550,-6.343991,8.594255,-5.166817,6.585994,-6.309585,9.280859,4.581107,0.447614,8.509616],[6.381171,4.998085,-8.726579,4.839750,4.959717,-5.696825,9.541411,2.187128,-6.486030,1.224833,-2.573281,5.069006,-8.463680,-2.518445,-3.900818,8.237678]],[[4.858227,-1.880601,-8.263697,7.143786,1.659458,-4.498692,-9.029240,-2.715330,8.814104,-1.505110,2.500099,8.393724,3.156474,4.500571,8.049322,7.684977],[-5.724124,3.481013,9.476069,-8.801510,-0.553550,5.350172,-8.365508,9.696651,-4.590619,-5.775826,-7.428525,9.317567,1.636452,0.825551,-6.449966,-9.044716],[-6.725872,5.605742,-7.814950,-7.978220,6.872741,9.780861,7.035042,1.538230,-3.151052,-8.014607,-4.079686,-9.448406,-9.148894,-1.298557,3.465568,8.660088],[-7.554260,9.525612,-0.607510,-5.579396,-0.001695,-4.631501,-8.730197,2.003560,4.963420,2.670852,0.158516,0.331078,3.054038,-1.641762,-4.779522,-1.958494],[9.020702,1.612599,-9.513288,9.317349,1.186952,-5.792126,8.617063,5.974095,1.865829,-6.252681,-6.659150,5.113215,-6.971289,-8.912187,6.318121,1.542130],[3.316032,7.687465,-8.232641,-3.387372,-8.156469,-2.824885,-5.468175,-3.855549,-6.248714,-4.427749,-6.665462,2.124385,-2.768992,-1.560910,-7.263187,-5.304125],[-3.667889,0.371580,-1.818983,6.035138,8.908102,-5.883667,9.827986,9.469535,-5.815641,-0.997831,0.371906,2.425432,-8.293700,-0.169432,9.888411,-0.691954],[-8.244578,0.352673,0.439955,4.638366,-9.912406,-0.294352,-1.124450,7.125120,0.109654,5.583916,7.012552,-2.991968,-8.549122,6.870272,6.091333,-2.353559],[2.119292,-2.305609,-3.840437,1.594309,-3.463004,-3.672898,-0.918974,0.860553,0.625339,-9.016948,5.275463,-4.886271,3.826941,9.576577,2.957098,-0.722680],[4.642189,5.039114,-3.568087,-2.247226,-0.286800,6.185757,8.878419,1.310414,-3.787041,3.985978,-6.666120,2.596965,0.610882,1.260134,-8.300080,-0.848900],[-2.480770,8.674847,-8.182195,5.212582,-6.523338,5.392552,7.345671,3.925620,7.806477,2.563769,-8.463775,3.294637,-9.680703,2.139045,7.455656,-0.153666],[3.718677,-0.369879,-5.702432,6.371780,2.365154,-9.027359,5.036631,-2.704642,-0.329608,-2.626309,-2.533527,7.333679,-3.505094,-5.316787,-3.354531,-3.833596]],[[-1.833337,5.497324,-0.788641,-2.652874,-7.777344,3.055032,-1.592642,-3.116087,7.598360,4.626964,-6.952187,-6.398101,7.734282,-6.036821,-2.473865,-6.634991],[-9.573418,9.491481,-7.920142,-7.008945,-7.405263,-7.067162,8.386678,4.166912,0.532185,-4.004355,6.370181,0.094667,4.799996,-0.602589,-0.686354,1.548838],[6.744547,5.029165,-7.429172,-5.670541,2.263163,3.573555,4.790225,-4.118418,5.521382,-4.770103,2.990307,-9.684074,-8.755360,-1.644844,1.903267,1.461921],[-4.672632,-4.075040,-0.784589,8.228365,4.766343,-3.602618,-3.015154,0.066014,4.040715,-0.264103,4.028500,-0.301112,-1.026317,-2.793556,-0.481023,-0.006738],[7.626115,6.540242,7.079916,1.404744,5.875685,7.967437,-6.291943,7.977597,-0.479864,2.477768,-3.929382,1.272135,-4.140766,-6.972633,8.552061,-7.816224],[7.240311,-2.996079,-8.919877,5.672045,6.341468,6.649793,-2.045012,-7.102542,9.847377,-9.461718,6.805945,-3.517838,-8.073439,-4.176179,2.868591,-1.822973],[-5.198000,9.172352,-5.684486,-7.750234,9.889091,-6.562146,-9.722626,-7.746221,-6.570115,-5.063175,9.550424,7.962432,0.202222,8.711253,-0.723496,-3.079937],[3.972180,-7.561682,-3.597318,0.480648,-6.749499,4.190676,-2.100796,-1.976861,9.621162,-7.043139,1.405748,-0.627730,2.262202,1.191679,0.477227,-0.281454],[1.244563,-4.085626,9.489439,9.276865,9.347101,4.155363,7.629790,-1.507808,-9.397705,6.141569,6.447739,-1.354481,6.347655,-3.948486,5.602430,2.914355],[2.924901,1.437584,-3.892205,8.770290,7.103523,1.966871,-5.837320,5.390042,9.709402,9.623813,-3.619167,9.194468,4.572057,-0.381127,3.938137,-6.176838],[-7.469475,6.844413,-8.764417,-8.374790,7.816264,-6.819146,-2.540428,-3.458855,-1.186167,-5.049727,-0.896061,9.791754,5.167994,-8.724024,5.709677,-8.314098],[-9.758789,-6.457772,-1.101314,2.623205,3.959857,6.298012,9.467477,0.039303,8.194364,6.961254,1.163867,-4.334397,-5.536677,7.495004,9.865291,0.431128]],[[-6.668271,-8.335839,0.392505,-0.311843,-4.668398,-5.613078,-8.591927,9.130667,6.934894,6.520237,2.548701,9.435797,-7.349545,-8.428746,-4.311784,-8.601904],[7.944813,6.011977,-3.158059,9.901166,-5.622192,-7.459290,3.253400,-4.821900,-3.103092,-9.318381,9.117291,-8.517391,-2.146403,1.427432,-8.575009,2.361656],[9.290530,-9.410209,8.667892,-1.653399,4.034113,-0.682383,-8.013501,8.844181,-1.553389,9.348365,-6.746393,8.224522,-2.694675,4.042739,-8.660845,-6.575231],[-5.293796,7.883209,4.547674,3.097735,7.144463,1.318119,-0.962928,-7.442079,-0.164221,6.531200,1.945526,-5.462583,6.420959,4.709113,-4.503230,6.736121],[-0.310746,-3.352771,-3.049799,6.772983,2.360079,-4.723676,5.088824,-4.530146,-5.745551,-6.293800,2.902888,5.973516,9.730395,-1.508671,-1.477854,-7.685404],[2.089775,-4.839818,-0.501021,6.377186,2.207345,4.675884,-6.628344,-6.727547,2.779227,3.460412,2.787599,-6.845699,7.491484,5.529408,-6.020715,-1.674761],[-3.765839,-6.997494,-9.621684,5.837185,2.168542,2.434544,-2.850483,-0.243244,-8.550031,-5.944416,-8.726340,-4.818963,-2.300340,0.272130,8.970251,-2.607477],[7.404384,-7.148143,-9.569742,5.424952,8.012555,7.120258,-9.755848,4.585082,0.936167,9.334247,-8.699869,8.041192,3.697685,-2.740590,2.764483,-8.095070],[0.211113,-8.182479,-0.331823,7.274125,-2.000386,-5.251780,-4.881769,-9.177512,3.829729,2.922441,2.697695,-6.808888,7.987094,-2.606724,9.368931,5.928415],[0.001204,-6.485181,0.779259,3.181686,2.937545,1.271787,-3.441071,3.837994,2.322733,3.978869,-2.412162,5.917031,-3.638896,-7.202786,-4.046712,-3.658233],[5.942582,-0.110044,-2.121062,5.285637,8.963933,4.499540,-4.403524,8.811395,3.093068,-4.393434,7.696765,-2.177851,3.982090,0.969975,-1.701452,-5.316203],[2.383108,7.614464,-4.339051,4.559609,6.997278,3.397914,0.442706,0.977197,-6.837917,-0.175660,1.746492,5.194610,0.740244,-1.103295,0.008029,-8.100973]],[[9.804418,-3.993197,-6.823803,4.108748,5.590939,2.439588,-4.352928,2.542328,-7.522998,-2.775784,-1.299674,2.304069,-2.538960,-1.072201,-5.534649,-3.129459],[-2.641855,1.845973,-2.571569,-5.001534,-4.713103,4.576288,-4.022191,5.759253,-4.534993,-3.671132,8.645874,5.393692,4.593749,2.580117,-9.809000,-9.354562],[6.464899,6.208411,-3.354720,1.362726,8.076055,2.688720,4.230100,-2.364632,-9.835706,6.649260,-4.742919,-1.701440,-5.623182,6.262221,3.344615,1.916883],[-0.700832,6.128320,-5.137791,9.944439,6.180453,3.130484,9.626680,-5.829853,-6.083183,7.171470,-4.503392,-8.929797,-2.365114,2.283854,1.464909,-0.339117],[4.153279,9.453101,-4.189226,8.066642,3.105224,-8.454668,8.116149,9.772249,-2.348860,-7.014325,-4.232062,6.351713,9.949920,-9.829273,4.333195,-0.656347],[-4.575804,-2.482337,-5.302077,-1.641893,-2.945234,-5.914024,-5.539645,2.483345,-7.525486,6.539754,6.450419,8.426120,-1.934136,4.601642,-5.644594,-9.276770],[1.200895,1.567544,2.449919,-6.790428,6.161664,9.013818,-5.709630,-1.974307,-6.946872,4.561972,8.869100,-5.915125,-7.963207,2.310163,6.575028,-7.317239],[3.952186,-9.957163,4.189258,-1.314695,1.600459,-3.481871,8.962031,9.237351,9.969309,6.875203,2.412612,-2.355904,1.717844,6.284181,4.333824,-2.290536],[8.357590,1.398904,0.405989,4.169150,3.501455,-8.989256,5.237387,8.487491,-6.450252,7.808657,-7.207676,4.297377,9.663471,6.253763,-6.371406,5.915818],[-9.821969,7.168013,2.695981,5.552245,-6.771611,3.958259,7.189536,-0.856052,5.342372,3.144866,1.753338,5.833009,5.569978,-5.708581,-9.542068,-5.990317],[-5.284441,-0.258470,-1.603690,7.953602,3.619987,-4.283477,7.969460,-9.883397,-9.591749,-6.116625,0.708806,6.190869,-0.104410,-6.958496,6.826796,-1.510369],[-8.840318,6.867912,-5.218904,-9.754029,9.537141,-0.708873,7.111596,6.741331,-3.988264,-0.670284,-9.377682,0.127258,4.152480,5.760869,-3.318931,-9.846270]],[[0.804229,5.905638,-9.915709,9.149626,2.538381,-6.375198,9.116537,-2.310808,-9.704787,1.256975,-3.057415,4.773494,-0.266172,3.594548,-7.477834,-2.490894],[3.388858,0.511843,8.136178,-9.496413,-1.297372,1.376640,-3.588338,-1.517428,-8.611430,2.009909,-9.911543,-2.060232,-9.831936,2.850063,-9.042831,-2.102593],[9.216841,5.446599,-6.966499,5.742761,9.078986,-7.312148,0.177996,-0.426203,-3.539601,-2.329936,-3.750230,-0.868043,-7.681518,-0.896605,9.128923,0.147031],[-1.913097,4.573241,-4.141816,-1.223615,8.383669,0.551431,8.370040,6.252920,-2.355558,-2.406624,-5.047881,5.014847,-6.596750,2.935317,-0.400726,-9.952950],[-6.828196,4.228683,5.802849,-8.551587,1.213466,0.068254,9.699465,-5.171899,-7.843117,-4.258330,6.395759,-3.034693,0.494561,4.064153,-4.345438,5.674631],[7.237382,8.246386,-0.700946,-4.227172,0.352672,-6.858162,-3.518952,-1.717256,2.672716,3.429348,-8.172444,-7.450495,-5.221304,9.537878,9.161931,1.538373],[-0.933717,5.701512,-8.077738,-0.193073,3.737293,-3.111284,4.816754,9.465861,4.937372,-9.308867,-1.939154,-4.809068,-0.738149,7.547736,-2.041234,3.617387],[9.061794,9.703397,-2.783500,1.682803,-5.961982,8.305254,6.922152,-5.640116,7.529697,-7.287834,8.650848,-7.497364,9.306840,6.297386,-5.472719,-0.694654],[-8.966803,4.808861,0.274460,-4.907721,-6.544296,3.274387,-5.146254,9.401601,-1.399188,5.909244,-8.649940,-9.127687,5.474806,8.379501,-4.640155,9.883406],[7.451124,4.208930,-7.532653,-8.053272,1.626599,-8.596138,9.398955,0.484396,3.537584,4.468625,0.095663,9.613839,7.745284,-0.343529,-9.141988,-7.332635],[9.975692,-7.115943,-8.398088,-2.051058,6.432690,8.471347,-7.587630,-1.952994,-6.101684,4.015535,4.961425,-7.200835,2.784853,-1.540840,3.000871,0.500480],[-7.466781,-9.763212,-4.397398,-7.547868,5.962890,-1.192596,8.224309,1.430297,-2.191746,2.647516,-6.849761,7.021795,-7.581087,8.718840,-0.152599,-2.864763]],[[6.272384,8.269470,-1.424248,9.339845,-1.352751,0.823175,-5.975310,7.057995,-9.343872,5.511661,-4.374328,-1.502805,-6.038967,-1.149576,6.769817,-4.697607],[3.610250,-5.649946,9.204787,1.242374,-3.464431,5.698131,-8.104584,9.734926,4.674017,4.133930,7.728662,7.717248,6.211915,2.681610,-5.613463,9.512350],[3.855812,4.279844,1.426175,-5.973473,-8.856015,4.017840,-4.317596,3.041679,2.355692,-0.231260,-0.198231,-5.480092,0.993964,-7.414411,3.583175,-8.967786],[-1.229287,-7.198512,-7.859599,1.768731,-3.964019,6.477547,6.373528,0.419691,0.299433,-0.295767,8.067605,-6.213701,-0.623959,-8.278084,-1.451285,-7.813958],[8.019243,5.634889,-3.595691,-6.878625,8.242646,5.199338,-7.772698,2.210878,-6.769863,7.169136,-2.139863,0.968565,6.740394,9.965110,-5.122826,-6.081787],[-3.440561,7.308779,-0.098573,4.326009,-4.440077,-2.205040,1.952329,-3.037096,7.099620,3.476630,0.118350,-4.661590,6.574124,0.431301,-4.971188,2.462686],[2.425757,1.453769,-3.610417,9.714546,5.685198,6.991330,0.408676,5.607959,3.665130,-8.223867,8.742258,6.361225,-7.271363,-0.737932,-1.498484,9.166725],[-8.847400,5.851844,-4.905584,3.105730,9.649866,-7.772501,1.618133,1.396428,6.133913,9.963957,9.435975,2.724507,4.418141,-5.174297,1.663024,9.101925],[-5.811731,-7.281549,0.010013,-3.479160,-2.979912,1.214100,-2.780400,-4.388257,5.485985,-9.514871,7.771102,-6.778429,4.552658,-5.491619,3.194053,3.269975],[0.271997,-4.529135,5.862254,1.296092,2.807750,8.008034,1.103437,2.458480,-4.164035,5.093946,0.872500,-9.451572,-3.653047,2.741692,4.914560,2.757756],[-6.211215,7.233039,6.737736,4.510025,-3.303716,-0.285981,2.855153,-8.332508,-2.839753,6.295965,6.605790,-1.209024,-5.706762,5.822805,-9.408295,-0.512350],[-8.523719,9.009358,-0.278301,3.948890,9.002003,2.399237,5.480622,-1.529963,8.401451,-5.128503,-5.054334,0.630579,-3.144561,-9.805471,6.409060,-5.928289]]], dtype = "float64")#candidate|3807|(15, 12, 16)|const|float64
bop_3808 = relay.less(call_3796.astype('bool'), relay.reshape(const_3807.astype('bool'), relay.shape_of(call_3796))) # shape=(15, 12, 16)
bop_3811 = relay.less(call_3797.astype('bool'), relay.reshape(const_3807.astype('bool'), relay.shape_of(call_3797))) # shape=(15, 12, 16)
output = relay.Tuple([call_3798,call_3800,bop_3808,])
output2 = relay.Tuple([call_3799,call_3801,bop_3811,])
func_3813 = relay.Function([], output)
mod['func_3813'] = func_3813
mod = relay.transform.InferType()(mod)
output = func_3813()
func_3814 = relay.Function([], output)
mutated_mod['func_3814'] = func_3814
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1192_call = mod.get_global_var('func_1192')
func_1193_call = mutated_mod.get_global_var('func_1193')
call_3832 = relay.TupleGetItem(func_1192_call(), 0)
call_3833 = relay.TupleGetItem(func_1193_call(), 0)
output = call_3832
output2 = call_3833
func_3840 = relay.Function([], output)
mod['func_3840'] = func_3840
mod = relay.transform.InferType()(mod)
mutated_mod['func_3840'] = func_3840
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3840_call = mutated_mod.get_global_var('func_3840')
call_3841 = func_3840_call()
output = call_3841
func_3842 = relay.Function([], output)
mutated_mod['func_3842'] = func_3842
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3851 = relay.var("var_3851", dtype = "int8", shape = (14, 7, 5))#candidate|3851|(14, 7, 5)|var|int8
var_3852 = relay.var("var_3852", dtype = "int8", shape = (14, 7, 5))#candidate|3852|(14, 7, 5)|var|int8
bop_3853 = relay.right_shift(var_3851.astype('int8'), relay.reshape(var_3852.astype('int8'), relay.shape_of(var_3851))) # shape=(14, 7, 5)
output = relay.Tuple([bop_3853,])
output2 = relay.Tuple([bop_3853,])
func_3858 = relay.Function([var_3851,var_3852,], output)
mod['func_3858'] = func_3858
mod = relay.transform.InferType()(mod)
mutated_mod['func_3858'] = func_3858
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3858_call = mutated_mod.get_global_var('func_3858')
var_3860 = relay.var("var_3860", dtype = "int8", shape = (14, 7, 5))#candidate|3860|(14, 7, 5)|var|int8
var_3861 = relay.var("var_3861", dtype = "int8", shape = (14, 7, 5))#candidate|3861|(14, 7, 5)|var|int8
call_3859 = func_3858_call(var_3860,var_3861,)
output = call_3859
func_3862 = relay.Function([var_3860,var_3861,], output)
mutated_mod['func_3862'] = func_3862
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3874 = relay.var("var_3874", dtype = "float32", shape = (4, 2, 14))#candidate|3874|(4, 2, 14)|var|float32
uop_3875 = relay.rsqrt(var_3874.astype('float32')) # shape=(4, 2, 14)
func_577_call = mod.get_global_var('func_577')
func_580_call = mutated_mod.get_global_var('func_580')
var_3880 = relay.var("var_3880", dtype = "bool", shape = (216,))#candidate|3880|(216,)|var|bool
call_3879 = func_577_call(relay.reshape(var_3880.astype('bool'), [3, 8, 9]))
call_3881 = func_577_call(relay.reshape(var_3880.astype('bool'), [3, 8, 9]))
func_916_call = mod.get_global_var('func_916')
func_918_call = mutated_mod.get_global_var('func_918')
call_3898 = relay.TupleGetItem(func_916_call(), 2)
call_3899 = relay.TupleGetItem(func_918_call(), 2)
bop_3907 = relay.divide(uop_3875.astype('float64'), relay.reshape(var_3874.astype('float64'), relay.shape_of(uop_3875))) # shape=(4, 2, 14)
bop_3914 = relay.power(bop_3907.astype('float64'), relay.reshape(uop_3875.astype('float64'), relay.shape_of(bop_3907))) # shape=(4, 2, 14)
output = relay.Tuple([call_3879,var_3880,call_3898,bop_3914,])
output2 = relay.Tuple([call_3881,var_3880,call_3899,bop_3914,])
func_3944 = relay.Function([var_3874,var_3880,], output)
mod['func_3944'] = func_3944
mod = relay.transform.InferType()(mod)
var_3945 = relay.var("var_3945", dtype = "float32", shape = (4, 2, 14))#candidate|3945|(4, 2, 14)|var|float32
var_3946 = relay.var("var_3946", dtype = "bool", shape = (216,))#candidate|3946|(216,)|var|bool
output = func_3944(var_3945,var_3946,)
func_3947 = relay.Function([var_3945,var_3946,], output)
mutated_mod['func_3947'] = func_3947
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3953 = relay.const([[[-6.389221,3.745760,-0.565496,-8.929881,-4.873140,9.290325,-5.955887,-8.070018,-0.814645,7.969541,-7.448168,-0.629509,-0.889786,7.233421,-6.417031,7.130230],[3.553607,-9.449682,-8.974043,-6.248899,1.702848,3.312772,2.549578,5.518288,6.917439,-9.673811,-1.736625,2.567569,-3.063682,2.332536,3.837379,-9.006074],[8.445069,9.888116,3.955688,-1.397062,2.775159,-5.225919,8.188928,8.355478,-9.132416,-6.510488,-8.282836,7.421600,1.235497,-4.451372,4.008373,9.166588],[8.122261,5.623793,-1.967689,2.678063,3.933767,6.554417,6.559731,8.699183,-5.708603,-6.458802,5.117671,4.256088,-0.570899,-2.453878,-6.182998,-3.921823],[-5.164768,-6.127905,2.213394,-6.525317,9.719829,3.330034,-8.885984,-6.855153,9.435115,-1.521709,1.445092,4.254442,1.531970,5.450808,9.249592,3.537659],[0.733621,3.160477,4.289201,-9.801453,5.260594,-6.293215,-7.832515,-9.786374,9.502553,3.182522,-9.266632,5.296110,-5.574605,-9.162528,-9.225538,2.003005],[7.465278,7.681101,-2.040674,-1.659399,1.851808,-4.031168,1.061265,4.421863,8.387158,1.118814,2.482727,2.203229,-4.090588,-6.475442,5.908963,-3.664237],[-5.298258,2.244995,2.399237,-5.152187,-4.960959,0.353428,0.732251,6.323585,4.984655,-2.921731,2.053363,-9.847224,8.530545,-3.376671,-0.988421,-1.634041],[-8.786241,7.285750,3.704551,5.532920,-1.597273,6.450626,7.458249,-8.264853,-6.082414,-3.632814,-0.436781,0.809099,8.681741,-6.395784,-1.780291,-1.897707],[3.968248,4.134670,6.304106,-9.343268,8.642061,9.361301,-5.584622,2.710805,-5.102813,-5.674893,-9.108930,0.653976,-3.462690,9.969942,-5.105161,7.431187],[4.135388,-0.893382,8.040755,5.186595,-3.887351,-7.387013,-8.937577,3.946550,2.513115,-8.294538,3.803205,4.071975,1.935676,5.887514,-2.516490,8.556585],[5.946820,-4.215718,9.692007,7.264725,-2.874283,-7.659852,3.293478,3.329962,-3.053466,-3.097193,5.393900,6.319841,-7.573385,-0.460918,0.210784,-9.451417],[7.975178,-8.561448,-6.451610,8.519014,2.455075,-8.278487,7.367815,0.629666,6.808864,-0.419537,5.602498,5.500506,-2.509486,-1.735356,-1.190896,-5.695555],[2.588905,-0.235400,-1.312284,-6.981524,7.637989,-9.287236,-5.651875,-1.457151,9.848420,3.133751,-7.430881,-9.396431,-7.391716,7.306420,8.715832,2.942140],[-8.017961,1.904516,5.076352,-1.600098,-0.169096,5.342126,-2.345672,-7.770559,-0.427585,-2.122087,-4.410219,9.879493,4.881266,3.376793,-0.852018,1.347114]],[[-6.317610,8.830244,-9.499910,8.351813,-9.381086,1.987103,-7.383392,-1.005167,2.996621,-2.434287,7.839528,4.434376,-4.331606,-7.141437,2.212236,6.749214],[-4.355448,6.733716,-1.534371,2.169566,0.464976,1.792003,-6.472578,7.169788,-2.862243,3.876183,4.946781,-8.918700,-0.292038,3.378936,-5.991045,9.013428],[3.472067,4.761689,7.942503,5.371698,6.998326,3.552780,-4.259566,-7.315139,-9.426912,9.818112,-5.659763,7.354238,-0.196419,-9.171508,3.713367,8.264092],[-9.549530,-0.261794,5.888993,-0.912291,-7.866283,-0.621578,-3.173724,2.100992,-1.307541,1.198592,-4.731660,0.267104,4.252634,6.737460,-4.126866,0.074656],[3.412826,-9.686031,4.795727,3.310619,-7.199984,7.573162,-0.684891,2.464472,1.804884,4.546789,8.160748,-6.159135,-6.809408,2.411338,-2.273501,8.604504],[-4.774239,-6.718422,3.923248,0.942811,2.283687,-0.700403,6.015016,-7.175674,-9.808491,-6.975459,2.057605,-0.785767,-1.699490,-2.813914,4.625610,-5.406868],[2.662530,0.256168,7.004681,9.134719,1.006913,-5.992684,0.104589,3.700569,7.321577,-5.291668,-5.219498,-2.333539,-4.766369,2.244678,7.179171,-3.006190],[-9.505599,4.258586,-0.644111,-1.208078,-6.958192,3.867613,-0.380693,-7.032537,-1.098462,-9.628223,2.354023,-9.246020,5.121199,5.034364,4.743287,2.736195],[-0.957048,8.861022,4.948821,-7.995581,3.535184,-5.001544,9.364675,2.713002,2.126145,-6.009376,-6.950143,-2.721086,8.661474,-2.666172,0.173378,-7.225977],[-1.617962,3.464406,-2.666136,-6.372620,5.245463,0.186886,8.347249,-8.130436,-1.268513,0.703129,4.229372,-6.631264,-4.562724,-1.592134,-9.616158,8.531619],[-2.684162,8.512952,-1.838802,-7.221703,-7.190954,-7.760323,-8.669874,-5.165399,-3.539365,-5.738368,7.697324,-5.103877,1.888706,-0.881359,0.851738,6.522057],[-8.389175,-5.031616,-7.033220,-2.242577,-3.436661,-1.494842,5.317621,7.755494,-5.413189,-5.972788,-6.353202,7.782040,9.025647,-6.306695,4.000127,-8.205917],[-5.652987,1.488958,-6.292172,9.227862,-1.127092,6.739870,-1.078242,4.298543,-5.140256,-6.337419,-5.834037,5.480306,1.292905,9.877391,8.516372,-5.602918],[-1.710816,-4.367549,6.093083,-4.365082,1.307968,-1.696589,-5.307370,-4.957953,8.012279,-4.949072,5.960244,3.228758,0.097958,5.631905,-2.357847,-4.306306],[3.612514,9.514529,-8.115626,6.407067,-1.749013,1.314050,8.956462,6.711020,-0.468825,5.430866,0.915644,1.659164,6.992245,9.753710,-6.093058,-3.772142]],[[-0.537769,9.796443,5.998831,-1.367477,-7.200126,3.668327,-8.399930,-1.404462,-1.410305,-5.117131,-4.362507,-7.775880,-1.770334,8.588509,9.935406,1.875489],[-8.784907,-7.294504,3.385144,3.336245,-6.119819,1.701057,3.403471,7.716311,6.694773,-1.600973,2.599369,3.774859,-8.633496,7.174959,9.566366,-7.863710],[4.127654,0.897378,9.582259,-6.486386,9.310601,-0.694590,3.598850,-5.090304,6.089348,-1.711766,1.017858,4.793803,-0.923958,1.231910,3.385154,8.505813],[-4.713444,9.079685,0.592648,6.924043,7.536243,-4.670984,-7.750213,-0.695722,0.193853,-1.795798,-3.486784,-2.796447,-4.603987,-3.007791,4.263004,-8.905117],[1.758927,-4.396945,4.691350,3.260726,1.316359,6.556486,8.627942,-7.715930,-3.345601,0.297075,-5.371406,-8.821855,-0.301178,-1.303897,-6.181693,6.891271],[-0.405805,0.452836,-8.045143,-9.174631,-8.587808,8.151401,9.798386,-6.632391,-6.169736,1.038956,4.318457,-6.288531,-7.526547,-4.119789,1.882619,-1.673065],[7.533251,-8.620462,9.116942,2.589771,-4.308935,7.029965,-5.285861,-0.964938,6.366258,6.332234,9.544355,-9.123467,-5.631495,-4.651420,4.658622,8.795231],[-9.042091,-4.063873,4.331537,7.095212,-3.039866,8.994203,-6.699513,3.897633,0.921969,7.348295,-6.010128,7.764730,-3.941704,9.987995,-0.962359,-0.834165],[-7.639377,-3.573551,-4.787226,5.170191,-0.998872,-3.636031,-6.727713,4.681760,-2.545290,-1.177218,-8.336790,-4.017191,-8.374430,-2.874886,-2.405697,0.200883],[4.415251,-4.848908,-8.268155,-0.718446,8.332705,2.349058,2.975618,5.542634,4.453271,-1.763278,6.558908,-3.465506,-4.199489,8.693545,3.271396,4.341862],[-5.329489,3.197735,-0.407745,-8.848610,-9.306947,5.632444,-1.578409,5.971978,8.848078,7.232573,-7.332133,-0.035561,5.978790,-9.796682,-1.999656,6.293670],[9.366642,5.734155,1.421237,1.833184,-3.051563,3.997973,-4.750606,-4.282410,-3.719136,-8.316382,-1.167007,-1.807244,-6.557428,-0.356500,-5.041803,-3.036725],[-8.824232,5.568733,5.271448,3.963567,-8.937173,-0.339851,-9.843975,-3.449659,-8.710645,6.003809,8.387336,-9.736597,-1.224182,-1.334275,5.739864,4.077734],[3.967367,4.863580,2.740583,-6.594149,1.135543,-5.344409,7.371342,-1.988600,-6.235306,-8.100880,7.612808,5.239800,-8.724247,9.855439,-7.340184,5.238671],[9.668912,-9.086787,-9.158003,-3.520085,3.621815,2.314988,4.640213,3.372868,9.100725,2.945158,-8.999994,9.792520,5.076563,-6.884695,4.696922,6.648810]],[[-5.033494,8.838499,-4.508365,-8.628879,1.422013,-2.854005,-8.557366,-8.381495,-3.449769,-1.013237,-8.404111,1.595803,-4.854084,-1.237668,6.524312,7.146703],[1.220789,-0.336773,-7.518913,-4.907739,-8.740321,7.029881,-2.577849,7.474222,3.432559,4.621484,6.064275,9.144833,0.620031,0.291376,1.112617,-3.309243],[1.626572,-5.706113,-3.885937,7.170680,-0.407111,5.853193,-4.257141,4.110956,-0.974464,-1.731164,0.078082,-5.548609,3.930959,8.533217,-1.468570,0.029596],[9.872358,9.054467,-4.348451,-3.216592,2.117548,1.230870,-6.617103,-2.213051,-1.518297,-0.383440,-9.982041,-2.090495,-1.952373,5.186476,3.443752,2.424459],[-7.795282,-4.454073,0.967304,1.616623,-2.636185,8.774244,2.140067,-7.577376,-5.031789,0.074527,5.242233,-5.334571,-0.022653,-4.339940,-5.360453,-0.261299],[-6.670787,-2.632480,6.431831,8.377454,-3.123718,5.362292,-4.227744,6.275337,-9.866420,2.377929,-0.958808,-9.282509,7.266126,0.499854,-2.997775,3.845208],[-8.122885,-0.841632,5.667029,-6.262892,-4.912324,-1.623021,0.480404,2.706034,-0.525071,3.492352,-2.389030,0.980357,-0.998359,-1.187435,-6.302793,5.179691],[7.198506,5.400878,5.931853,-0.471791,9.593246,-1.751181,7.024282,-3.205297,3.925038,-9.960603,1.529906,1.135682,-3.614414,-0.070609,8.198423,-3.844365],[-4.836735,-2.740054,1.261508,3.969797,5.346392,8.675172,-4.678227,-0.492087,4.939500,2.473461,1.344878,-4.873587,-4.811566,-6.699855,-7.742081,-6.120464],[-5.790075,6.923394,-2.533737,-0.208338,-5.225794,-7.635708,-4.706485,-5.958651,9.020589,-9.792632,2.298344,0.502807,-9.492959,9.628957,-7.866467,4.347704],[-4.392211,-8.481497,9.649882,-5.488190,-0.583561,-4.873087,-5.331955,-0.413079,3.075958,-7.749677,7.482443,-1.107264,1.332680,-6.076363,-5.798135,8.877389],[-3.794135,0.408797,-1.348326,-7.192130,-0.370399,9.902284,6.940507,-4.102538,1.395711,8.126353,-9.722787,-6.936130,-4.821932,9.906168,-1.148419,1.500344],[-3.510552,-6.539506,5.884345,0.453609,-0.187148,-0.979893,-6.713263,-1.381364,2.612474,-7.796832,6.894455,0.196509,-7.942764,-7.770719,1.019443,0.279798],[-8.920758,9.327533,-9.738606,2.947519,6.701657,1.545177,8.775675,4.615163,1.278784,-7.613062,-4.052893,-1.106226,3.807808,8.789725,6.449419,-6.734531],[0.578105,3.448870,6.363442,-9.577814,-0.512824,-7.243440,9.426460,-4.071920,-3.629372,0.435008,-5.355091,2.855398,6.700151,2.430749,3.314388,-7.116598]],[[3.405370,8.917121,8.966114,1.052547,2.073595,9.869680,-1.310846,6.639235,-3.888678,7.124626,3.064276,-0.061622,-8.218076,0.237454,-6.398357,-5.195987],[2.205365,-9.900180,2.555301,-2.816949,7.944393,4.458963,8.100056,-5.486813,9.524419,-1.799758,-9.676250,3.504702,-0.676378,2.199327,5.245439,-9.013380],[0.054878,7.815378,7.457350,2.726336,9.183535,-9.277690,0.809938,-0.674275,-1.104076,0.395074,-9.474654,2.271515,2.713656,9.168756,-0.162550,8.433048],[-4.334750,-0.257739,-4.598015,-4.944328,-7.030130,-6.479174,-7.382535,6.988944,-1.067128,7.401512,2.895270,8.717433,4.633102,8.148937,8.924154,3.446022],[5.861269,9.295745,7.958757,4.159124,-0.074646,-8.011887,9.871333,8.919212,-3.103161,-1.219405,-6.238333,0.748512,-9.494539,8.737584,7.122431,1.094873],[5.961162,8.442484,-2.504581,-8.011044,-4.611954,7.521879,-2.431737,2.063807,-9.888680,5.759790,-3.316896,-2.760519,2.924839,-5.469972,4.211260,-0.502981],[-4.875423,3.069893,-1.294665,4.681671,-1.519951,-2.883037,6.883330,-7.492507,6.885723,-0.761144,-2.236116,-5.402577,6.741091,-4.808773,-9.814272,7.333854],[-3.265726,-6.543770,-4.835180,-8.360246,-4.118117,-0.956585,-5.424794,9.900023,-8.010666,8.718540,3.566216,-9.963231,-8.204849,6.618373,8.900286,4.195729],[6.942300,4.592437,6.466287,0.947365,-6.927412,-1.385890,-2.840424,4.673971,2.262968,8.254082,-9.004454,6.025209,-6.094107,-5.358771,7.167973,-4.857201],[9.682607,5.637610,1.744353,-0.174552,-9.877503,-7.251067,1.037970,3.831023,0.919173,6.740665,-1.930050,-7.066115,5.582988,3.701470,0.365229,5.591934],[1.622304,4.908822,9.990124,-9.046529,-3.888347,-8.241089,-3.609143,6.134941,-8.333082,-3.313219,5.827224,-1.429976,0.322338,-4.163177,2.886254,8.732249],[-5.082142,1.408840,-7.922870,1.183881,-1.660220,-7.432792,4.105480,-2.437658,-0.038261,-7.047823,-4.586051,-1.068319,-4.787878,-8.070737,4.592913,-7.743017],[-1.870131,6.017987,-0.207104,-7.982852,0.189020,8.368533,-2.302259,-9.506506,-5.000351,-2.217778,2.871685,-7.189566,8.272135,8.399460,-7.749357,-1.132996],[6.538657,-1.241168,-3.880925,5.133088,2.652148,-6.992718,-3.523998,1.659236,-2.987733,0.380886,-3.909115,8.351720,-6.296990,-5.859885,6.800382,-8.344676],[5.583722,-4.359832,0.481866,2.951616,-4.991476,-3.679582,-6.497963,-2.786326,7.157388,4.041286,7.771302,-8.768977,2.811087,7.405783,5.574923,-8.678224]]], dtype = "float64")#candidate|3953|(5, 15, 16)|const|float64
uop_3954 = relay.tan(const_3953.astype('float64')) # shape=(5, 15, 16)
output = relay.Tuple([uop_3954,])
output2 = relay.Tuple([uop_3954,])
func_3962 = relay.Function([], output)
mod['func_3962'] = func_3962
mod = relay.transform.InferType()(mod)
mutated_mod['func_3962'] = func_3962
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3962_call = mutated_mod.get_global_var('func_3962')
call_3963 = func_3962_call()
output = call_3963
func_3964 = relay.Function([], output)
mutated_mod['func_3964'] = func_3964
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2800_call = mod.get_global_var('func_2800')
func_2802_call = mutated_mod.get_global_var('func_2802')
call_3982 = relay.TupleGetItem(func_2800_call(), 0)
call_3983 = relay.TupleGetItem(func_2802_call(), 0)
output = relay.Tuple([call_3982,])
output2 = relay.Tuple([call_3983,])
func_3995 = relay.Function([], output)
mod['func_3995'] = func_3995
mod = relay.transform.InferType()(mod)
mutated_mod['func_3995'] = func_3995
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3995_call = mutated_mod.get_global_var('func_3995')
call_3996 = func_3995_call()
output = call_3996
func_3997 = relay.Function([], output)
mutated_mod['func_3997'] = func_3997
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4009 = relay.var("var_4009", dtype = "float64", shape = (15, 16, 16))#candidate|4009|(15, 16, 16)|var|float64
var_4010 = relay.var("var_4010", dtype = "float64", shape = (15, 16, 16))#candidate|4010|(15, 16, 16)|var|float64
bop_4011 = relay.subtract(var_4009.astype('float64'), relay.reshape(var_4010.astype('float64'), relay.shape_of(var_4009))) # shape=(15, 16, 16)
func_1361_call = mod.get_global_var('func_1361')
func_1365_call = mutated_mod.get_global_var('func_1365')
const_4025 = relay.const([3,8,-4,4,3,10,-9,6,-10,-2,-7,1,10,10,-8,-7,-5,-2,1,4,-2,-10,1,10,-4,8,9,-5,5,-6,2,-3,-10,5,2,5,-6,-3,-8,-8,-5,4,-8,-5,-4,-5,6,-1,-2,8,-8,6,-6,10,-1,-10,7,-10,-3,-9,6,1,-9,-10,1,-4,1,-4,10,2,-2,-10,6,-5,5,-6,-5,6,-3,8,-4,-4,4,-1,2,8,8,5,9,5,-2,-6,-9,-5,-9,-6,-5,8,-10,8,4,8,-5,8,-10,8,3,1,10,-4,-10,2,5,-7,-8,-7,-10,-6,5,-8,6,-9,4,3,-9,-3,-9,2,-4,9,3,-6,-10,-9,8,-1,5,-5,1,3,5,9,-10,8,-2,-7,4,10,-8,10,-6,10,3,10,-3,6,-6,2,5,-9,-8,4,10,5,-4,-5,5,2,3,2,5,-4,2,-9,5,-4,4,4,-3,-5,-1,7,-6,-4,1,4,3,-10,-3,1,-9,-10,6,-1,2,-6,-4,9,-2,-8,-10,-2,8,9,1,1,7,-4,-7,4,9,-2,-2,3,-5,-8,1,9,2,-5,8,-4,7,-9,-3,4,2,-4,-9,2,-8,-1,2,2,-6,8,1,10,-2,-4,4,6,4,-2,-9,-6,-7,-7,7,-3,-6,-6,5,-7,-6,1,-7,-6,6,-3,-4,-9,-6,-10,-8,5,-5,3,8,8,-10,-4,3,9,1,2,1,-6,2,9,10,3,6,7,3,9,-4,2,4,5,-5,3,-2,2,-7,-1,-8,4,8,9,-9,-9,-3,8,-4,5,4,5,6,-10,-2,-2,5,4,9,9,2,-1,-8,-2,-6,2,-4,-5,-4,-5,-6,-7,-3,8,-4,10,-2,-9,-1,-3,-10,6,1,6,6,4,-8,-7,-1,3,-10,9,5,4,-3,-1,-3,-6,-8,-2,6,8,-4,-5,10,10,4,-3,9,2,-6,4,-4,4,5,-8,-1,-4,-1,-1,8,10,1,10,-3,-4,9,-8,10,-5,-9,5,9,-4,10,-3,7,2,-9,9,-5,10,-3,-7,2,8,-4,1,4,-6,-3,5,-4,-9,7,4,-3,6,-3,-10,4,8,3,-1,-7,3,6,9,3,3,-7,4,1,5,4,3,-3,5,-10,-5,3,-8,-8,-1,6,2,2,3,-7,-1,6,-10,3,-7,4,-2,1,-8,-9,-9,6,6,9,-3,-10,9,6,-4,-5,-4,6,7,-7,8,5,-9,-1,1,6,8,8,-1,7,5,-10,-2,-4,6,6,-7,3,4,-3,-4,8,-7,9,1,7,1,-5,-6,2,2,5,-8,7,2,8,-3,10,-3,1,-9,1,8,3,-7,-7,2,10,2,-6,1,2,8,-3,-5,6,3,-3,3,6,-10,1,-6,-4,2,5,-3,5,-1,4,-3,1,6,-8,10,1,6,4,4,-2,-9,8,-4,-3,3,2,-8,3,-8,4,-6,8,8,-4,9,9,-3,-7,-1,-3,-8,4,9,-9,-10,-5,-10,8,2,-10,-8,-8,-5,-7,9,-5,-4,-2,-8,-9,8,3,-6,3,3,-10,2,3,7,8,-9,-3,-3,7,8,8,-10,3,1,6,1,6,-6,-3,-8,-6,-3,1,6,5,-2,1,5,-9,-1,-2,-1,-6,-7,7,-1,2,4,9,-1,-3,1,-6,7,3,-8,-2,1,-3,8,-4,7,-2,1,-10,-10,-7,8,-7,9,-6,-3,6,-6,-4,3,3,8,-10,9,-3,-6,1,-4,-10,8,-9,-2,-7,-6,-5,3,-6,5,3,-9,-6,9,-6,4,5,1,5,9,-4,-6,-1,-8,1,-6,-9,3,7,-1,-4,-10,-8,-2,-6,6,-5,10,-1,-4,2,-1,2,-6,-5,-1,-5,9,-4,8,-4,-2,7,5,-10,2,-9,-5,-6,-10,-10,-1,6,8,-5,-9,-1,7,3,-5,5,9,10,-4,4,9,-9,-1,-4,-4,-5,7,-4,-3,-10,-3,6,8,-3,4,8,-5,8,1,-5,9,8,8,-2,-10,-1,-7,3,5,-8,5,-4,5,6,-4,-1,-5,-10,-10,5,-5,2,-5,7,-1,9,-3,8,-7,-3,9,5,-2,8,7,1,2,-6,-8,-7,10,-7,-2,-10,-3,-9,7,-8,-9,9,4,8,3,2,-6,2,-6,-8,6,-7,-1,5,10,-4,-2,3,-5,1,-6,9,2,10,10,6,6,-9,10,4,9,-7,3,6,-4,7,-10,3,-10,1,1,-10,-1,-3,-4,8,-4,-4,-8,6,7,-1,-2,8,9,5,-7,4,-3,6,3,3,-3,-4,-7,-3,4,9,10,9,7,9,9,1,-2,1,2,-1,-1,6,-5,-10,4,-6,-9,4,-1,1,6,-5,-10,4,-10,-7,-9,-9,-1,-5,10,-9,-10,-8,-6,4,10,4,4,4,-2,9,3,8,-8,-10,6,-9,2,9,6,-4,1,-10,6,2,-4,-9,-8,-2,-10,7,2,4,5,6,7,10,9,-4,4,3,7,-5,-9,-3,1,-6,-6,-9,-6,-2,6,-2,2,10,-3,3,6,-7,7,5,10,1,4,8,-6,2,2,8,9,1,-10,-4,-2,-3,-2,9,10,9,1,-5,-8,8,10,-6,-4,2,3,2,6,-6,-4,2,4,-1,1,-1,-2,8,7,-2,5,6,-10,5,6,8,-8,-5,2,-7,-1,-1,-7,6,5,4,-3,-9,-3,-3,-8,10,-1,-6,2,-5,2,-9,-5,5,-4,-1,3,4,-6,6,7,-8,2,1,-9,-10,-4,-4,-3,-10,-9,-6,3,-10,-8,-1,-2,-5,-4,2,-5,-6,1,-8,8,1,-9,2,8,2,-10,-1,3,9,-4,-1,-5,-8,7,-1,3,4,1,-5,10,5,10,2,-3,1,6,-6,8,-7,1,-10,2,-8,10,5,3,-1,7,-8,-8,10,10,-5,2,-3,-2,9,5,-10,-5,8,-5,4,-4,-4,3,6,-2,4,-5,-10,8,-2,9,1,-8,-3,-5,7,-1,-2,7,-2,9,6,10,2,5,2,-7,-9,1,-10,-1,8,9,10,7,6,5,1,-6,-7,6,-7,2,10,10,-2,6,-4,-9,3,-6,4,-3,-9,8,1,5,9,-4,3,-8,4,2,-10,-4,-8,4,-2,-7,-5,6,8,-4,9,7,-3,-6,10,-6,-10,3,-1,-10,-3,3,-1,-6,8,-8,-1,10,10,10,5,-8,4,-3,-10,7,9,5,-7,-10,2,-4,3,-6,2,-2,-10,2,-4,9,7,9,-6,-7,-5,7,-7,2,-9,-2,4,7,-4,10,-5,2,-6,1,5,-4,7,10,6,-1,-2,-5,-6,-2,5,-8,4,-4,3,2,-3,10,10,3,2,1,8,-10,-10,7,-6,-8,5,1,-7,-7,3,-2,5,-9,1,1,-7,6,-5,5,-7,2,-6,1,-9,-6,6,-5,5,-10,-5,-6,3,-4,-6,-10,3,-5,6,-2,6,7,-6,-3,-6,7,-5,6,6,6,8,-5,9,-9,7,2,-7,-5,1,6,-2,-1,-8,5,-6,8,-9,6,-4,-5,-4,4,7,-6,9,6,-7,-6,-3,-10,2,-2,2,8,-2,-5,-1,-10,10,7,-10,-1,-1,3,-10,2,3,-2,1,-1,5,1,-6,-6,-7,-6,-7,5,5,-9,-10,-6,4,-8,-10,-10,-4,2,-2,-8,1,-7,10,6,7,-10,-8,-10,4,9,-6,10,-2,9,1,4,-1,2,-4,-9,-6,9,-3,6,6,3,8,1,-6,-5,-10,-2,-1,-4,-5,-5,-2,-2,-5,4,6,5,-3,-4,-9,-7,-10,-3,3,6,-2,8,-7,-1,-1,-4,-4,-8,5,5,3,-6,1,3,-9,-2,4,-5,2,-3,-2,-7,8,-3,-1,1,-10,-6,6,-5,-10,6,-8,-5,8,3,-7,-6,10,-9,6,3,-7,-5,8,-8,8,2,-6,8,5,1,2,8,-5,-2,-5,6,-6,4,4,4,-7,-10,1,4,9,-9,-5,4,-2,-2,3,-10,3,-3,-8,-1,-1,-6,8,10,7,2,-6,3,-5,8,5,7,4,4,-6,6,5,4,4,-5,-3,5,5,9,3,6,-5,-5,-2,10,-4,-9,-10,4,-7,7,6,-1,-7,1,-8,-7,1,-2,1,-2,2,-5,4,-6,-10,3,4,9,2,3,-8,-3,-2,-1,-8,-9,-4,-3,-6,9,4,4,-6,1,-4,8,-3,-8,-7,-8,-1,7,3,-4,-9,-7,-7,-2,5,-10,6,-10,2,-3,-8,-6,-10,-6,1,10,-5,4,7,4,9,-2,6,3,-3,-7,-9,-1,3,10,9,7,-8,-7,-9,10,7,-3,5,10,-4,10,-7,-4,8,8,5,-1,-6,-1,-9,3,2,-10,-5,6,7,-5,-7,-9,-5,4,10,-5,4,-3,7,-3,-5,-8,3,-10,-10,-7,5,5,2,-10,-5,-1,4,-3,4,-2,1,7,-3,-6,-3,-3,-10,-6,8,-5,4,-3,1,-9,-4,-4,-10,8,-2,-8,9,1,10,2,-5,2,-2,-8,-10,10,8,6,-8,1,1,3,1,-9,-3,-2,7,-10,6,6,6,8,1,-2,-10,-9,2,-3,7,-5,-5,1,-10,3,-2,2,4,-2,5,3,4,-8,-5,-9,-5,3,3,3,8,9,-2,7,-2,2,2,-5,-9,-5,6,-5,2,2,-5,-1,1,-10,-3,-1,-8,4,-10,10,-4,2,-3,-2,8,-10,-8,-3,-1,2,-3,-10,-7,5,-3,-5,-2,-6,7,-9,3,5,2,-2,4,-8,-8,8,-3,3,7,-3,-6,-3,-1,7,4,7,1,-9,-3,1,-7,9,1,-6,-1,-7,-1,9,3,-4,-9,2,-10,4,-10,-9,4,-7,-1,3,-5,10,-1,6,8,-2,2,-6,7,-8,-6,5,6,-5,8,-10,8,-7,-2,2,4,6,10,-8,3,-5,2,9,4,6,3,5,9,-8,-4,10,6,3,5,2,-7,7,9,-9,1,6,-3,-3,2,1,4,5,-7,-6,2,-10,-5,10,2,-8,5,7,5,-10,3,-5,5,9,-10,4,-2,-1,-1,10,10,-8,-2,-5,-5,3,6,-5,10,1,-8,4,-9,-7,-7,6,5,-2,-9,3,2,1,4,9,1,-7,-6,9,7,-8,2,-2,9,5,3,-1,-4,4,-8,5,4,-8,-3,8,10,-4,1,1,-2,-8,-6,1,-1,1,8,9,-8,-4,4,10,-9,8,2,2,10,10,-8,8,-6,9,7,-5,6,5,-1,-4,1,2,3,-9,5,9,-2,5,7,9,-3,-8,-4,-7,-10,-5,2,4,3,-10,-3,-4,-7,-3,2,-8,-8,3,1,-9,2,-10,3,-2,9,7,-1,9,9,-2,-5,7,9,7,2,1,-2,-8,6,3,4,-7,10,-2,-7,-9,7,8,-6,7,1,-1,10,-9,-1,-2,-2,-9,5,1,-8,-6,8,10,-7,3,-7,-2,-6,-3,-5,4,-6,-10,-6,4,-5,8,2,-9,-7,8,9,-10,3,3,-8,5,-4,4,-10,-4,7,-8,10,-8,8,-8,10,-3,1,10,5,-3,2,6,4,-5,-2,1,-10,6,7,-6,-1,-9,-3,2,-8,-6,10,2,-4,8,2,7,-8,-10,6,-3,5,9,-5,-7,-6,1,6,4,2,7,1,8,4,6,5,9,1,7,9,-7,8,-10,5,6,6,-3,-5,6,-8,1,10,-3,-8,-9,4,-3,-5,-7,-7,-10,-6,1,4,3,10,7,-6,2,-1,-4,-6,9,9,4,9,-10,6,8,-9,-4,-7,-10,3,10,5,-1,8,-4,4,-3,-1,9,4,-7,-10,-3,-6,-1,-7,3,2,2,-1,-7,6,1,-2,-5,8,1,-7,-5,7,9,7,-5,5,-3,6,5,-9,-9,7,-1,-10,-4,-9,7,7,2,-10,-6,-4,5,-8,-10,-7,2,-5,-2,7,1,7,4,5,-9,-10,-4,-6,2,9,5,-5,3,-9,-4,-1,4,4,-3,1,6,8,6,6,10,-4,-5,-1,8,1,8,-8,1,10,10,5,5,-3,9,-2,9,5,2,10,8,3,-5,-10,-4,-10,4,-10,1,1,-7,1,9,-7,2,3,9,7,9,-2,-10,7,8,-4,-5,10,-9,5,9,-9,9,2,-7,6,8,1,8,3,-7,6,-3,-3,7,8,-10,-6,8,9,-7,-3,2,-3,2,-8,-3,3,1,6,-4,4,3,4,-8,-7,9,1,2,4,10,-6,-6,-8,-5,-7,-3,6,10,5,7,2,2,7,-9,-9,-5,-3,4,-10,-8,-1,-7,-6,8,-3,-3,-1,10,10,-1,8,6,6,3,-10,-2,-3,-9,-6,-10,2,-5,10,-10,-5,-1,-6,-4,-6,8,-9,8,-9,-1,-6,3,-6,-10,4,-9,3,-1,7,-9,2,9,-10,-3,8,6,-5,-1,-7,-1,2,-1,-2,-4,-10,1,2,3,-9,-1,-8,-10,-5,-6,-3,-7,-9,-2,3,-9,10,-4,10,-4,-2,5,-1,-5,-5,3,9,4,10,-8,-1,5,9,-4,7,-9,3,10,-10,-4,-5,-2,7,-2,-4,-2,-1,8,8,-10,-10,-5,4,8,-10,8,9,10,8,5,-4,8,-3,7,8,8,8,-10,-1,-8,-1,6,8,6,-10,9,7,1,-2,5,6,8,9,8,-8,-10,-3,-9,-2,9,5,6,-3,-5,-5,-7,-4,-9,-6,-2,5,3,6,-1,6,-10,7,-6,5,7,2,5,2,-10,10,1,1,3,6,8,5,-5,-8,-5,2,4,-8,1,-2,-6,-10,8,-3,-3,-9,2,-2,6,-10,10,-5,-8,-3,2,-10,8,9,3,10,-2,-8,-3,-5,-8,-10,-1,-3,7,-7,-1,-1,-7,6,-4,-8,3,3,4,-5,-7,3,9,6,-3,-8,10,-5,10,8,6,-10,-10,3,5,10,-2,-7,-10,8,5,-10,-5,-3,6,9,-5,-9,6,-3,-1,-2,-6,5,-3,1,-10,5,8,2,-9,-4,-2,3,8,-10,9,-3,2,-2,4,4,-4,1,7,4,4,4,2,5,-5,8,-6,8,-2,2,-4,9,-3,10,2,10,3,-4,-3,-4,4,2,-6,8,3,-1,4,4,10,1,-9,8,7,6,10,8,-5,-4,3,6,-1,10,7,-5,8,-9,-9,9,-10,5,9,6,4,-3,-3,10,8,-1,5,-1,2,-2,-10,6,-7,2,6,10,-9,6,3,-7,-9,-5,-2,7,-10,-6,9,-2,5,-2,3,1,-6,5,-7,2,1,-8,8,1,-4,10,-1,2,6,6,-8,3,-6,-5,3,8,-5,-8,-4,2,-6,-3,-3,-2,9,-10,7,-10,6,-5,-5,6,9,-4,3,-3,6,-7,-1,10,8,-6,7,-7,5,3,-5,9,-3,9,7,-8,-9,2,5,-9,-5,-6,-5,5,-5,8,-9,3,10,-1,-5,-9,-3,4,4,1,-10,-2,-7,5,-7,-1,-9,-2,8,3,-2,10,5,5,7,1,-10,2,-1,-1,-9,-7,-9,-5,-2,-2,3,2,-6,-1,3,-10,-6,4,9,-6,-8,-7,3,3,2,-2,7,-5,2,-6,8,10,10,1,-9,-10,-1,-3,-8,-2,2,-5,9,-4,8,8,7,1,-3,-1,-1,-9,-7,-9,-1,-5,-6,-1,-2,5,-6,5,-10,3,9,6,-6,-2,-1,1,-1,-2,9,-1,-10,-1,9,2,-2,-5,-10,1,-9,-10,-2,-10,-7,2,-8,9,9,-6,5,10,-4,8,-7,9,-2,4,-2,-8,7,-7,5,6,-5,4,2,-9,10,-10,8,1,-10,3,1,3,5,4,-7,4,7,-1,-2,7,10,9,7,-6,-6,1,2,5,3,7,-4,-1,9,-9,-4,2,-4,-10,10,-7,6,-4,-1,8,-8,5,6,-2,10,5,-10,8,8,4,-5,-6,1,1,-9,-8,-4,9,-3,-4,-2,8,7,-5,-3,5,-2,-1,1,4,3,-6,-9,8,6,4,2,-2,-8,-4,-6,9,1,10,3,3,8,-2,4,8,3,-10,5,-4,8,4,-10,-1,-4,-5,7,-3,-7,1,-7,3,-4,-5,-6,-10,8,10,6,8,-4,-4,-3,5,2,-5,-6,8,-3,9,-3,-6,2,8,-7,7,-1,2,10,4,-5,2,9,-3,5,4,10,9,-3,-1,5,-4,9,-10,3,-2,5,2,-3,6,7,-8,-7,-9,5,-3,-8,-7,-2,7,-3,6,2,-9,2,-5,-5,-6,-1,5,6,8,-2,2,-4,-1,-9,-2,-2,-8,-8,3,-7,8,-3,5,8,3,2,7,-4,10,3,4,7,-2,-4,-10,4,-10,10,6,1,-1,-3,-9,-5,10,-3,7,-6,-4,-6,3,2,-6,-9,2,10,-4,-10,-1,2,-6,6,4,4,2,4,-1,9,1,-10,9,-6,4,-4,2,-6,2,4,4,5,10,-3,10,-8,9,5,9,-9,-7,10,2,10,8,9,3,-9,-7,-4,4,9,-10,-1,6,-4,4,4,9,-9,9,-10,6,-5,-4,2,-1,-1,-5,-3,-2,-6,10,4,6,-8,-5,-9,-2,6,7,3,-10,10,7,-8,10,-5,4,4,5,8,2,1,-6,-1,-6,1,-1,3,4,-4,5,-9,-1,2,-4,-5,10,2,2,8,-8,-6,-10,4,10,10,-1,8,-1,9,-3,-2,10,-8,5,-4,3,-3,-7,-8,-7,6,-9,-2,-5,4,5,10,9,-10,3,9,-2,-10,-9,9,9,6,8,-8,6,4,7,-7,-1,3,10,10,6,4,8,-3,-7,-5,-8,-1,-5,6,-8,-8,-1,-2,5,-5,-4,8,2,-1,2,-5,8,-5], dtype = "int8")#candidate|4025|(3360,)|const|int8
call_4024 = relay.TupleGetItem(func_1361_call(relay.reshape(const_4025.astype('int8'), [16, 14, 15]), relay.reshape(const_4025.astype('int8'), [16, 14, 15]), ), 2)
call_4026 = relay.TupleGetItem(func_1365_call(relay.reshape(const_4025.astype('int8'), [16, 14, 15]), relay.reshape(const_4025.astype('int8'), [16, 14, 15]), ), 2)
output = relay.Tuple([bop_4011,call_4024,const_4025,])
output2 = relay.Tuple([bop_4011,call_4026,const_4025,])
func_4031 = relay.Function([var_4009,var_4010,], output)
mod['func_4031'] = func_4031
mod = relay.transform.InferType()(mod)
mutated_mod['func_4031'] = func_4031
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4031_call = mutated_mod.get_global_var('func_4031')
var_4033 = relay.var("var_4033", dtype = "float64", shape = (15, 16, 16))#candidate|4033|(15, 16, 16)|var|float64
var_4034 = relay.var("var_4034", dtype = "float64", shape = (15, 16, 16))#candidate|4034|(15, 16, 16)|var|float64
call_4032 = func_4031_call(var_4033,var_4034,)
output = call_4032
func_4035 = relay.Function([var_4033,var_4034,], output)
mutated_mod['func_4035'] = func_4035
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2389_call = mod.get_global_var('func_2389')
func_2390_call = mutated_mod.get_global_var('func_2390')
call_4055 = func_2389_call()
call_4056 = func_2389_call()
func_1755_call = mod.get_global_var('func_1755')
func_1757_call = mutated_mod.get_global_var('func_1757')
var_4071 = relay.var("var_4071", dtype = "uint16", shape = (40, 2))#candidate|4071|(40, 2)|var|uint16
call_4070 = relay.TupleGetItem(func_1755_call(relay.reshape(var_4071.astype('uint16'), [80,])), 5)
call_4072 = relay.TupleGetItem(func_1757_call(relay.reshape(var_4071.astype('uint16'), [80,])), 5)
func_833_call = mod.get_global_var('func_833')
func_836_call = mutated_mod.get_global_var('func_836')
const_4077 = relay.const([1.925099,-0.540078,2.386658,-0.469817,-1.473095,-6.753174,5.219753,8.554427,-0.034447,2.703868,6.792417,7.082876,-2.943160,-4.658041,8.622474,-4.303164,5.938461,-7.128852,-3.075733,-7.554722,-1.940957,4.615820,8.824792,9.379828,3.658777,2.002962,2.830875,-4.877665,-8.962252,0.118846,6.951196,-6.805826,4.321792,-0.035364,3.575281,-5.979520,3.713244,3.376939,-5.759672], dtype = "float64")#candidate|4077|(39,)|const|float64
call_4076 = relay.TupleGetItem(func_833_call(relay.reshape(const_4077.astype('float64'), [3, 13, 1])), 2)
call_4078 = relay.TupleGetItem(func_836_call(relay.reshape(const_4077.astype('float64'), [3, 13, 1])), 2)
func_2246_call = mod.get_global_var('func_2246')
func_2248_call = mutated_mod.get_global_var('func_2248')
call_4093 = relay.TupleGetItem(func_2246_call(), 2)
call_4094 = relay.TupleGetItem(func_2248_call(), 2)
func_1877_call = mod.get_global_var('func_1877')
func_1879_call = mutated_mod.get_global_var('func_1879')
call_4095 = relay.TupleGetItem(func_1877_call(relay.reshape(call_4070.astype('uint16'), [480,])), 4)
call_4096 = relay.TupleGetItem(func_1879_call(relay.reshape(call_4070.astype('uint16'), [480,])), 4)
func_2086_call = mod.get_global_var('func_2086')
func_2088_call = mutated_mod.get_global_var('func_2088')
call_4113 = relay.TupleGetItem(func_2086_call(relay.reshape(const_4077.astype('float64'), [39,])), 0)
call_4114 = relay.TupleGetItem(func_2088_call(relay.reshape(const_4077.astype('float64'), [39,])), 0)
func_3840_call = mod.get_global_var('func_3840')
func_3842_call = mutated_mod.get_global_var('func_3842')
call_4127 = func_3840_call()
call_4128 = func_3840_call()
output = relay.Tuple([call_4055,call_4070,var_4071,call_4076,const_4077,call_4093,call_4095,call_4113,call_4127,])
output2 = relay.Tuple([call_4056,call_4072,var_4071,call_4078,const_4077,call_4094,call_4096,call_4114,call_4128,])
func_4129 = relay.Function([var_4071,], output)
mod['func_4129'] = func_4129
mod = relay.transform.InferType()(mod)
var_4130 = relay.var("var_4130", dtype = "uint16", shape = (40, 2))#candidate|4130|(40, 2)|var|uint16
output = func_4129(var_4130)
func_4131 = relay.Function([var_4130], output)
mutated_mod['func_4131'] = func_4131
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3840_call = mod.get_global_var('func_3840')
func_3842_call = mutated_mod.get_global_var('func_3842')
call_4146 = func_3840_call()
call_4147 = func_3840_call()
output = call_4146
output2 = call_4147
func_4153 = relay.Function([], output)
mod['func_4153'] = func_4153
mod = relay.transform.InferType()(mod)
output = func_4153()
func_4154 = relay.Function([], output)
mutated_mod['func_4154'] = func_4154
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2800_call = mod.get_global_var('func_2800')
func_2802_call = mutated_mod.get_global_var('func_2802')
call_4174 = relay.TupleGetItem(func_2800_call(), 0)
call_4175 = relay.TupleGetItem(func_2802_call(), 0)
output = call_4174
output2 = call_4175
func_4183 = relay.Function([], output)
mod['func_4183'] = func_4183
mod = relay.transform.InferType()(mod)
mutated_mod['func_4183'] = func_4183
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4183_call = mutated_mod.get_global_var('func_4183')
call_4184 = func_4183_call()
output = call_4184
func_4185 = relay.Function([], output)
mutated_mod['func_4185'] = func_4185
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3525_call = mod.get_global_var('func_3525')
func_3526_call = mutated_mod.get_global_var('func_3526')
call_4215 = relay.TupleGetItem(func_3525_call(), 1)
call_4216 = relay.TupleGetItem(func_3526_call(), 1)
output = call_4215
output2 = call_4216
func_4217 = relay.Function([], output)
mod['func_4217'] = func_4217
mod = relay.transform.InferType()(mod)
output = func_4217()
func_4218 = relay.Function([], output)
mutated_mod['func_4218'] = func_4218
mutated_mod = relay.transform.InferType()(mutated_mod)
func_638_call = mod.get_global_var('func_638')
func_640_call = mutated_mod.get_global_var('func_640')
call_4219 = func_638_call()
call_4220 = func_638_call()
uop_4221 = relay.log(call_4219.astype('float64')) # shape=(3, 8, 9)
uop_4223 = relay.log(call_4220.astype('float64')) # shape=(3, 8, 9)
output = relay.Tuple([uop_4221,])
output2 = relay.Tuple([uop_4223,])
func_4225 = relay.Function([], output)
mod['func_4225'] = func_4225
mod = relay.transform.InferType()(mod)
mutated_mod['func_4225'] = func_4225
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4225_call = mutated_mod.get_global_var('func_4225')
call_4226 = func_4225_call()
output = call_4226
func_4227 = relay.Function([], output)
mutated_mod['func_4227'] = func_4227
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3525_call = mod.get_global_var('func_3525')
func_3526_call = mutated_mod.get_global_var('func_3526')
call_4254 = relay.TupleGetItem(func_3525_call(), 0)
call_4255 = relay.TupleGetItem(func_3526_call(), 0)
func_4225_call = mod.get_global_var('func_4225')
func_4227_call = mutated_mod.get_global_var('func_4227')
call_4265 = relay.TupleGetItem(func_4225_call(), 0)
call_4266 = relay.TupleGetItem(func_4227_call(), 0)
output = relay.Tuple([call_4254,call_4265,])
output2 = relay.Tuple([call_4255,call_4266,])
func_4285 = relay.Function([], output)
mod['func_4285'] = func_4285
mod = relay.transform.InferType()(mod)
mutated_mod['func_4285'] = func_4285
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4285_call = mutated_mod.get_global_var('func_4285')
call_4286 = func_4285_call()
output = call_4286
func_4287 = relay.Function([], output)
mutated_mod['func_4287'] = func_4287
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4297 = relay.var("var_4297", dtype = "int16", shape = (15, 16, 14))#candidate|4297|(15, 16, 14)|var|int16
const_4298 = relay.const([[[4,10,-9,-1,10,-9,-3,-9,2,-9,5,-2,3,-5],[-4,-4,4,-6,5,-2,-9,1,-4,5,2,-6,2,-6],[-10,10,3,4,-10,-2,8,-3,7,-8,-4,-6,9,-3],[-10,5,-9,-5,9,-4,8,7,2,-2,1,7,-3,2],[-4,10,-6,-3,-10,-9,-8,9,1,-3,-3,9,4,-1],[-10,8,10,2,-3,-10,3,-1,4,-8,-5,7,5,5],[-3,-6,-1,-1,-2,-6,-7,-7,8,3,7,7,10,1],[-2,-5,-3,10,-5,5,-3,10,7,-10,7,-7,5,-8],[9,-2,-6,-6,8,-10,-6,-10,-6,-8,-10,-6,-4,-1],[8,-5,9,-6,4,1,-7,-7,-8,3,-9,-6,9,-6],[-4,1,-8,-9,-4,1,8,-4,-7,-9,9,-10,10,9],[-8,4,6,6,-4,3,9,-7,-8,-3,5,-1,-1,-5],[6,2,-1,-8,4,2,-10,-7,9,-7,7,3,9,6],[-4,2,-7,4,5,-6,7,-8,-3,5,10,-10,-1,1],[-4,3,-10,-7,-3,6,4,-8,1,7,10,-5,-5,7],[7,-9,7,-10,9,3,-8,-10,10,-3,-2,5,4,2]],[[7,7,-9,5,-8,-2,-2,-9,-3,-3,4,4,-6,-10],[8,-2,-3,-9,5,8,-8,-2,-5,-3,1,1,-1,3],[-3,10,7,6,-10,2,-8,-3,-3,7,8,-8,5,6],[4,7,-2,-1,-10,-9,-2,6,-5,6,-5,-8,4,-4],[5,9,7,9,5,-10,-6,3,-2,-8,9,-7,-9,-9],[-10,4,-1,7,8,-1,7,-6,-2,3,-10,-3,4,-5],[-2,6,9,7,2,10,-1,1,-2,-1,5,-8,-4,6],[-8,3,-7,-4,-8,6,7,9,9,-6,-6,5,10,6],[6,-3,5,6,4,10,-3,3,-2,-9,-2,-2,-3,-2],[2,-8,2,-3,-5,10,-3,1,-7,-7,9,-10,3,1],[-10,-1,-1,-3,10,1,-6,-7,3,4,-4,-9,-7,4],[-4,5,8,-8,-5,-3,6,-2,-6,3,9,-7,10,-6],[6,6,6,4,7,2,-1,-9,-8,-1,-10,-4,-4,1],[-7,-1,-8,-5,-8,6,-10,-9,5,10,-7,-10,7,-5],[4,-5,3,-6,-2,-5,1,-8,-2,-4,3,10,8,8],[-3,8,-10,-8,8,-4,-6,-1,-10,10,5,9,-9,-9]],[[-9,2,-1,9,3,6,3,2,-9,-8,1,3,1,6],[-10,-5,-6,-1,7,-10,-9,-2,6,-2,6,-8,-8,-6],[2,7,9,-1,10,3,3,-10,2,5,-5,-5,-6,9],[-3,-3,7,4,-3,-2,-10,2,2,8,-5,2,-9,-2],[-9,1,6,-6,3,10,7,-10,-10,-2,4,6,4,-9],[6,-8,-2,6,2,-2,4,-10,5,9,2,-8,3,8],[-2,10,10,-3,-8,2,-3,-4,6,9,6,7,-1,-6],[10,4,5,-2,-2,7,5,10,2,6,-8,9,5,1],[2,-2,5,6,10,3,4,1,-9,-9,3,-1,4,-6],[-8,7,-6,4,-5,-1,10,-6,-6,-4,-8,-6,-10,-3],[-6,3,7,4,1,7,10,-10,2,5,-4,2,3,4],[-6,-8,-7,-6,3,10,-10,9,-6,10,-6,7,5,-4],[9,2,5,8,2,-8,8,8,-6,-9,7,-2,6,5],[-9,10,4,-3,-1,-3,-9,-10,3,-6,-7,3,6,-9],[5,6,2,3,-7,9,1,10,4,-8,10,-6,-1,-2],[-4,-1,-8,6,2,-8,-8,-4,-8,9,-6,9,-1,4]],[[-5,8,1,10,-6,-9,-6,5,5,-10,-8,7,8,-2],[10,-10,6,4,-9,9,1,-2,-7,10,8,5,9,-10],[7,-5,-9,3,6,3,4,-1,-1,3,-9,10,-2,-1],[-6,-9,2,1,10,-9,1,-4,-5,9,5,2,2,-1],[-8,5,-7,8,-10,-3,2,9,-3,8,5,1,-9,5],[-6,8,-3,7,-9,9,5,10,-3,1,-9,3,-6,5],[1,7,-8,-1,-7,-1,5,-4,4,-8,-2,-5,7,6],[-6,7,2,-5,10,-3,6,5,-6,4,4,8,-10,-8],[3,-8,-6,-6,-2,1,5,-1,10,4,7,-7,-9,-7],[-10,-6,1,-1,3,-5,8,-9,2,6,7,9,8,-7],[2,6,10,-4,7,8,-3,-5,1,-6,5,6,-1,-8],[-2,6,10,4,5,1,-3,2,-3,9,-2,-8,4,-10],[10,6,4,6,3,6,-9,-9,-5,8,-7,-2,1,-5],[6,2,3,10,9,1,-7,9,3,8,-9,8,5,-5],[9,-3,-3,-3,-2,-6,-10,-4,-4,-2,-3,9,-7,7],[4,-8,2,-10,-8,-1,-7,-3,4,3,-10,-8,-5,4]],[[1,-6,3,-2,7,10,-6,-6,-10,7,4,-3,-4,9],[10,-1,-5,8,3,3,-1,-3,-5,-9,8,8,-7,-8],[6,10,1,4,10,-3,3,3,8,10,-7,-8,-4,-6],[-1,-2,4,-10,-7,8,-8,10,-9,-5,1,2,-4,-2],[9,1,-6,7,-7,2,3,1,3,3,6,-8,-5,6],[3,8,-8,3,2,-4,9,2,8,-3,7,-2,6,-2],[2,-10,8,10,7,-1,-5,9,-1,-6,-4,-9,-7,-6],[2,-3,7,-1,1,10,7,6,-4,-8,6,3,2,-3],[-2,-1,-6,-9,8,-8,5,5,-9,6,8,10,7,-5],[5,6,-8,2,-1,-7,-4,8,-4,1,-5,-9,-8,-8],[4,4,3,9,-8,5,5,-10,6,-8,10,6,-6,-10],[-5,1,-4,-1,6,-6,2,-6,3,7,4,2,5,-1],[2,-5,-2,6,-1,10,-8,2,8,-8,1,-2,1,9],[3,-6,3,-2,10,-10,-5,-10,9,-3,-9,-9,6,-7],[7,-2,-8,-3,-2,6,5,4,-6,-2,-6,1,-8,8],[-2,-1,-1,-9,-3,-9,-9,6,-1,-3,7,-10,-4,10]],[[1,-8,-1,2,-1,-2,-3,-9,8,-8,10,-5,-9,-9],[8,-7,-7,2,1,1,-6,8,4,4,7,-10,-3,3],[2,7,1,-8,6,-6,5,2,-10,1,-10,-5,-6,3],[10,3,7,-1,-1,-7,-9,7,2,-3,4,6,10,-2],[-8,8,-10,-1,9,5,9,1,9,-1,-9,-3,10,-6],[1,-9,-2,9,7,9,10,-8,-10,-6,-8,9,-3,2],[-2,-8,-8,-1,5,4,-10,8,9,-8,6,5,2,3],[6,1,-6,10,5,4,-1,-9,-1,10,4,8,-3,4],[-7,-1,2,9,-10,-10,10,2,-4,4,-10,7,2,4],[8,-1,4,-8,-5,-4,5,7,-10,1,-3,-1,-9,9],[-4,9,10,7,-3,10,-1,10,-8,5,9,4,-1,5],[5,-5,8,1,3,3,2,-1,-8,2,9,6,3,8],[-8,6,-10,4,-5,5,4,4,-1,-10,-6,-7,-10,-1],[-4,7,-3,-7,5,10,-8,-6,10,10,-4,10,-3,-5],[1,-7,6,-9,8,1,-9,3,-5,-2,8,-8,-2,-4],[-5,-9,-4,1,10,-8,-10,-4,-1,8,6,1,-10,8]],[[-7,-7,3,1,2,-7,4,3,-6,2,-3,-3,10,3],[-3,4,-5,-2,-8,-6,-5,-5,10,-4,4,-8,-6,-4],[-5,8,9,-7,2,-3,-2,-1,1,9,-3,-2,9,-5],[-10,-3,7,-2,3,1,9,-8,-2,-10,-6,-8,2,-9],[9,7,-3,6,-2,-8,-8,-4,2,7,-2,9,-8,10],[-7,10,-1,7,7,-7,2,8,4,-4,-4,2,-10,6],[8,-9,-3,10,7,-1,1,-5,-3,2,5,-8,8,6],[1,-7,8,-1,-4,6,-8,-6,-4,1,-6,-9,-8,-1],[-6,-6,9,-7,7,7,-1,-3,-1,-10,-9,-6,-4,7],[1,10,-7,6,8,-4,-3,8,-5,5,-7,-2,-7,-5],[-1,-5,-2,-10,1,-8,1,-6,4,-10,-3,6,-1,-10],[7,1,10,2,3,5,-10,-5,-5,-7,4,-10,4,9],[-6,-6,-6,1,-3,10,-7,-1,7,7,-4,-3,-4,5],[10,-5,-5,-9,8,-1,-3,8,-5,6,-3,-8,-1,-5],[-5,-5,6,-3,-1,-4,-2,-1,-5,6,7,5,-9,9],[5,5,4,-7,9,3,-2,-10,-1,3,9,-9,-5,8]],[[-7,-2,-1,-2,-6,-7,-9,-7,-7,-9,-8,-6,6,-5],[10,-3,-2,-9,3,-10,-10,-5,9,-4,-7,-7,-7,-1],[-10,2,-2,7,3,9,-7,4,-9,-8,9,5,7,10],[-4,-9,-9,-4,-7,9,7,5,-8,-3,7,3,5,3],[-7,10,-6,-6,9,10,-1,5,6,3,-8,-8,10,-3],[9,-1,-1,-10,7,3,-5,1,1,-3,-7,-10,-3,-3],[10,-9,4,-7,-8,-1,10,10,-1,1,-10,-1,-1,5],[-7,-6,-4,8,-5,-2,-10,8,1,5,-3,-3,1,2],[-3,5,-5,1,-5,7,1,-5,-4,-3,2,-4,6,-10],[3,10,-8,8,-5,-3,7,2,-1,1,9,10,-3,8],[4,-8,-9,3,-3,-1,9,1,-5,-3,2,-2,7,-4],[-8,2,2,9,8,1,4,-2,-7,10,-7,-10,9,2],[6,8,10,-6,-10,4,-8,1,-6,-6,3,-6,-10,-1],[-10,7,-9,-8,7,-9,-10,6,9,-9,-8,9,10,4],[-2,9,8,-8,10,-5,-1,-3,9,-6,-5,-3,-9,-4],[8,8,-5,-3,-10,-9,8,-7,-8,9,-10,-6,-1,7]],[[9,-10,-1,8,3,10,-2,-4,-3,-9,-1,-8,7,-5],[-3,8,-6,-1,-7,5,-10,-3,-4,-3,2,-7,2,4],[-9,8,3,-6,-6,-6,-5,3,7,-6,-7,-7,-2,-1],[-2,-4,6,-5,-7,6,7,6,-6,-7,-9,6,-3,4],[-9,-10,10,4,-3,4,1,5,3,-1,-4,-2,3,-6],[10,10,5,-10,3,2,4,-7,-4,-2,8,8,2,-5],[-7,-9,-1,6,-10,-2,2,-10,7,-1,4,10,7,-3],[7,1,-9,10,-3,7,-5,-6,-2,-5,-6,2,10,-1],[1,3,2,-3,-8,10,-9,5,-7,-3,9,-9,-2,4],[-6,-6,-7,-6,-7,-9,-2,-6,-7,5,4,-4,-5,8],[6,9,7,1,-8,-2,-6,10,1,8,-7,-3,-10,3],[-1,-3,5,1,9,7,-6,10,1,9,4,-1,10,-1],[2,-6,-9,10,-8,5,2,5,-2,-2,-5,-4,-8,-1],[8,9,-7,2,1,-9,2,8,-7,-4,8,-1,-8,-3],[9,-7,7,6,-10,-2,-10,-1,7,8,4,5,1,6],[-1,6,-2,-9,-8,5,-3,8,-9,8,8,-4,-2,-4]],[[-4,-10,9,9,10,2,-2,3,-5,-3,-10,2,8,2],[-4,-3,-7,5,3,-7,1,9,8,1,5,-8,4,4],[-6,4,-3,8,1,7,-7,-7,6,2,-9,5,-8,2],[-1,-7,-5,6,-9,-9,8,-4,-10,3,-6,8,-9,-3],[6,-2,4,-3,-10,6,-3,-10,10,-6,-5,-6,6,-10],[7,-4,1,-1,3,1,-4,3,-3,-8,6,-3,5,-6],[3,5,-9,4,-3,2,-8,-1,3,10,8,-9,4,-7],[-1,-9,9,8,-1,8,9,3,-5,2,10,-6,-1,-5],[6,3,7,4,4,-3,-6,10,-1,3,-9,5,-6,-10],[-5,2,-8,-9,-7,-10,8,-5,-4,-10,-9,-10,9,-8],[8,1,-4,3,8,-1,-8,3,4,-10,6,-3,2,-1],[-3,-5,-10,2,-9,-8,-10,9,9,4,3,-4,-2,2],[-4,-7,6,8,8,10,9,-2,6,-7,-5,-2,2,5],[-7,-10,-2,10,8,-3,-1,2,10,9,7,-3,-6,1],[1,4,5,-8,2,6,-5,-8,10,6,-6,-6,-10,3],[3,6,2,-9,5,-7,-5,-8,-1,-9,-6,1,-2,5]],[[5,10,4,2,-7,4,-10,2,3,10,-6,-3,5,-6],[-2,-9,-9,-6,6,-8,3,-6,2,-10,7,6,-10,8],[4,2,-5,6,-1,-4,2,-1,-5,-8,4,9,-10,7],[-6,5,10,-8,10,6,8,-10,3,5,-8,-4,-1,-8],[-10,2,1,-5,-7,-4,9,-10,-2,-7,-10,5,-3,4],[4,6,-6,-7,6,-6,7,9,1,-2,10,10,-10,-9],[3,-9,-5,8,-1,-8,9,9,-5,-9,-10,1,-10,9],[5,-3,3,-5,6,10,10,-6,4,-4,-8,7,-6,7],[9,-6,-5,-3,2,7,-5,9,4,6,-3,-9,5,-8],[-6,7,-10,-10,-5,-3,4,6,4,-7,-1,10,-5,-4],[7,-1,6,10,2,-10,4,-3,3,10,-5,10,1,-1],[-9,7,6,10,-8,7,-10,-7,4,5,-9,5,-1,1],[4,-8,-6,8,-3,-3,9,-10,-1,-3,7,10,-10,-4],[-1,3,-7,-6,-8,-5,3,3,-10,-10,10,-5,1,4],[2,2,-3,9,-10,4,-9,8,-1,-5,3,-1,9,1],[1,1,3,7,10,5,10,5,-2,-3,-5,-3,4,-5]],[[-10,-2,2,-6,-7,-9,10,-7,7,2,-7,2,5,-4],[1,-3,6,6,7,10,-7,-10,-5,7,-9,1,6,-1],[3,10,-7,-7,-8,-8,6,-10,-7,10,-9,3,-6,7],[-2,-2,6,-10,-7,-3,-1,2,8,-8,6,8,5,-3],[-8,2,1,-6,6,-7,5,7,-10,1,3,-5,-7,4],[4,2,10,-3,-6,5,7,4,-3,-7,-10,-2,-10,-1],[10,9,-3,-8,-5,-3,2,-4,1,4,-8,6,9,-10],[7,-8,-9,10,9,6,-1,-6,6,-3,-9,10,7,-5],[5,7,-9,8,-1,-9,-8,-4,-1,-1,2,5,-2,9],[10,-8,-9,9,-10,-3,7,9,6,-6,6,5,5,9],[6,9,-10,-3,1,-7,8,2,-2,5,-4,5,10,8],[-2,3,5,-4,-8,-5,8,10,2,3,2,-1,9,-8],[8,4,-3,7,-8,4,-7,-7,-1,-1,10,6,-4,-10],[-5,-1,4,-2,-2,-6,10,-8,-1,2,-3,-2,8,5],[-6,-4,5,5,-1,-8,-6,5,8,-2,10,8,6,-8],[-1,4,-10,-10,4,-4,-2,1,-1,-5,2,6,1,7]],[[6,-10,8,4,-2,3,-2,4,1,4,-2,1,-6,7],[-2,3,-8,5,-8,-4,-5,-8,-5,-1,-8,8,-3,5],[7,7,6,7,4,10,3,2,-2,-5,5,-1,10,-6],[-10,2,-2,-7,8,2,8,-4,7,-8,-8,-6,-8,9],[-8,-1,-5,6,-2,6,6,4,10,-4,-3,8,5,8],[10,-1,2,7,-7,-5,-7,-8,8,9,-9,-7,-5,-6],[6,4,-1,4,-9,9,5,4,4,5,6,-2,-6,7],[-5,-10,7,6,-2,-9,3,-6,3,-10,-4,3,-8,-4],[5,6,4,-2,1,-9,10,4,10,-2,2,4,-9,-5],[-3,1,-10,-9,-2,-7,8,-6,6,2,1,-10,7,8],[-10,-3,4,10,-3,-10,9,10,1,-6,7,4,-3,9],[-8,-6,-2,1,4,-1,2,4,7,7,-1,7,-10,-3],[5,4,3,-2,-10,-2,-8,-3,-4,-10,-2,-9,1,-10],[8,3,-7,9,-7,-6,5,3,-3,-4,3,8,-10,-8],[-4,1,2,-7,2,-1,-6,8,-7,7,-5,-6,2,6],[10,4,-2,8,-10,5,1,-3,-2,-8,-9,-10,-5,-5]],[[-8,-10,4,-4,10,10,-7,2,-10,-4,-5,3,9,-10],[-10,1,7,6,-7,10,2,-5,-5,-6,-3,7,-5,6],[4,8,3,1,3,3,-8,5,-1,9,-1,-8,7,4],[8,6,6,-5,3,10,5,-4,-4,-3,1,-10,-8,7],[-6,7,-3,-5,5,9,-7,-4,2,-5,6,1,3,2],[-4,9,1,5,7,4,-1,1,-4,2,4,-2,5,-10],[7,-2,-10,-2,-4,-7,-6,-6,6,6,-4,-5,6,-1],[-1,1,-2,10,1,4,-6,10,-4,10,4,1,6,8],[-3,7,9,-5,-1,4,-6,9,1,-7,-6,6,-5,-9],[5,7,6,4,-9,6,-6,4,-1,6,-4,1,-10,-1],[-6,-9,10,8,7,-1,3,-8,10,-10,9,-4,-9,-5],[4,5,6,10,10,-2,-10,-3,10,1,-7,2,-9,9],[3,-6,-9,6,6,3,-4,1,8,8,-7,-2,1,10],[-2,7,-2,4,-5,1,6,5,9,-3,-10,-6,9,-3],[2,10,2,-1,10,8,-6,5,2,-2,-6,9,6,-6],[5,-7,1,-3,7,-9,-1,-2,-7,9,-9,-10,5,-2]],[[7,6,-5,9,10,-3,7,-4,9,5,3,5,6,6],[7,2,5,-5,1,-8,-7,-8,3,3,7,9,-2,3],[-2,-1,6,4,-1,2,5,3,-3,6,-4,-7,7,-3],[10,8,5,-2,3,10,5,6,-4,-3,3,-2,-10,-9],[6,-5,10,-10,-3,5,6,-1,-9,-2,7,9,-7,-8],[3,2,-1,-8,2,-5,-10,-2,6,-9,2,8,-9,9],[10,-2,5,2,3,-7,8,2,10,4,9,1,-7,1],[5,-1,-9,8,7,10,-10,4,8,-5,2,-6,-5,2],[-3,-5,5,3,-6,-8,1,-2,-6,8,-2,2,-4,-5],[-3,-10,-10,-7,10,-8,1,1,5,-2,2,3,-4,-8],[-3,-9,9,-7,4,-3,3,5,7,-5,-1,-1,8,-7],[-1,3,9,2,-3,7,10,6,-1,-9,-6,1,3,10],[-10,-4,-3,4,-10,10,-3,3,-8,9,7,-8,-4,2],[-4,9,-1,-4,-9,-8,3,4,-6,-1,5,2,2,7],[-2,3,3,-8,4,-9,-10,-4,7,-1,5,7,-6,2],[-2,3,-9,-8,8,-5,9,7,-4,-2,-9,6,-9,-3]]], dtype = "int16")#candidate|4298|(15, 16, 14)|const|int16
bop_4299 = relay.bitwise_and(var_4297.astype('int16'), relay.reshape(const_4298.astype('int16'), relay.shape_of(var_4297))) # shape=(15, 16, 14)
output = relay.Tuple([bop_4299,])
output2 = relay.Tuple([bop_4299,])
func_4303 = relay.Function([var_4297,], output)
mod['func_4303'] = func_4303
mod = relay.transform.InferType()(mod)
var_4304 = relay.var("var_4304", dtype = "int16", shape = (15, 16, 14))#candidate|4304|(15, 16, 14)|var|int16
output = func_4303(var_4304)
func_4305 = relay.Function([var_4304], output)
mutated_mod['func_4305'] = func_4305
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4310 = relay.var("var_4310", dtype = "uint16", shape = (8, 16, 16))#candidate|4310|(8, 16, 16)|var|uint16
var_4311 = relay.var("var_4311", dtype = "uint16", shape = (8, 16, 16))#candidate|4311|(8, 16, 16)|var|uint16
bop_4312 = relay.right_shift(var_4310.astype('uint16'), relay.reshape(var_4311.astype('uint16'), relay.shape_of(var_4310))) # shape=(8, 16, 16)
output = relay.Tuple([bop_4312,])
output2 = relay.Tuple([bop_4312,])
func_4316 = relay.Function([var_4310,var_4311,], output)
mod['func_4316'] = func_4316
mod = relay.transform.InferType()(mod)
var_4317 = relay.var("var_4317", dtype = "uint16", shape = (8, 16, 16))#candidate|4317|(8, 16, 16)|var|uint16
var_4318 = relay.var("var_4318", dtype = "uint16", shape = (8, 16, 16))#candidate|4318|(8, 16, 16)|var|uint16
output = func_4316(var_4317,var_4318,)
func_4319 = relay.Function([var_4317,var_4318,], output)
mutated_mod['func_4319'] = func_4319
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1918_call = mod.get_global_var('func_1918')
func_1919_call = mutated_mod.get_global_var('func_1919')
call_4321 = relay.TupleGetItem(func_1918_call(), 0)
call_4322 = relay.TupleGetItem(func_1919_call(), 0)
uop_4332 = relay.exp(call_4321.astype('float32')) # shape=(3, 8, 9)
uop_4334 = relay.exp(call_4322.astype('float32')) # shape=(3, 8, 9)
output = uop_4332
output2 = uop_4334
func_4336 = relay.Function([], output)
mod['func_4336'] = func_4336
mod = relay.transform.InferType()(mod)
mutated_mod['func_4336'] = func_4336
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4336_call = mutated_mod.get_global_var('func_4336')
call_4337 = func_4336_call()
output = call_4337
func_4338 = relay.Function([], output)
mutated_mod['func_4338'] = func_4338
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2246_call = mod.get_global_var('func_2246')
func_2248_call = mutated_mod.get_global_var('func_2248')
call_4388 = relay.TupleGetItem(func_2246_call(), 3)
call_4389 = relay.TupleGetItem(func_2248_call(), 3)
output = call_4388
output2 = call_4389
func_4396 = relay.Function([], output)
mod['func_4396'] = func_4396
mod = relay.transform.InferType()(mod)
mutated_mod['func_4396'] = func_4396
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4396_call = mutated_mod.get_global_var('func_4396')
call_4397 = func_4396_call()
output = call_4397
func_4398 = relay.Function([], output)
mutated_mod['func_4398'] = func_4398
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2007_call = mod.get_global_var('func_2007')
func_2009_call = mutated_mod.get_global_var('func_2009')
call_4422 = relay.TupleGetItem(func_2007_call(), 2)
call_4423 = relay.TupleGetItem(func_2009_call(), 2)
output = call_4422
output2 = call_4423
func_4429 = relay.Function([], output)
mod['func_4429'] = func_4429
mod = relay.transform.InferType()(mod)
mutated_mod['func_4429'] = func_4429
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4429_call = mutated_mod.get_global_var('func_4429')
call_4430 = func_4429_call()
output = call_4430
func_4431 = relay.Function([], output)
mutated_mod['func_4431'] = func_4431
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2126_call = mod.get_global_var('func_2126')
func_2127_call = mutated_mod.get_global_var('func_2127')
call_4468 = relay.TupleGetItem(func_2126_call(), 1)
call_4469 = relay.TupleGetItem(func_2127_call(), 1)
func_989_call = mod.get_global_var('func_989')
func_991_call = mutated_mod.get_global_var('func_991')
call_4481 = relay.TupleGetItem(func_989_call(), 2)
call_4482 = relay.TupleGetItem(func_991_call(), 2)
output = relay.Tuple([call_4468,call_4481,])
output2 = relay.Tuple([call_4469,call_4482,])
func_4485 = relay.Function([], output)
mod['func_4485'] = func_4485
mod = relay.transform.InferType()(mod)
mutated_mod['func_4485'] = func_4485
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4485_call = mutated_mod.get_global_var('func_4485')
call_4486 = func_4485_call()
output = call_4486
func_4487 = relay.Function([], output)
mutated_mod['func_4487'] = func_4487
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3448_call = mod.get_global_var('func_3448')
func_3450_call = mutated_mod.get_global_var('func_3450')
call_4501 = relay.TupleGetItem(func_3448_call(), 1)
call_4502 = relay.TupleGetItem(func_3450_call(), 1)
func_2110_call = mod.get_global_var('func_2110')
func_2113_call = mutated_mod.get_global_var('func_2113')
var_4508 = relay.var("var_4508", dtype = "float64", shape = (880,))#candidate|4508|(880,)|var|float64
call_4507 = relay.TupleGetItem(func_2110_call(relay.reshape(var_4508.astype('float64'), [16, 11, 5])), 2)
call_4509 = relay.TupleGetItem(func_2113_call(relay.reshape(var_4508.astype('float64'), [16, 11, 5])), 2)
func_4217_call = mod.get_global_var('func_4217')
func_4218_call = mutated_mod.get_global_var('func_4218')
call_4531 = func_4217_call()
call_4532 = func_4217_call()
output = relay.Tuple([call_4501,call_4507,var_4508,call_4531,])
output2 = relay.Tuple([call_4502,call_4509,var_4508,call_4532,])
func_4535 = relay.Function([var_4508,], output)
mod['func_4535'] = func_4535
mod = relay.transform.InferType()(mod)
var_4536 = relay.var("var_4536", dtype = "float64", shape = (880,))#candidate|4536|(880,)|var|float64
output = func_4535(var_4536)
func_4537 = relay.Function([var_4536], output)
mutated_mod['func_4537'] = func_4537
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4225_call = mod.get_global_var('func_4225')
func_4227_call = mutated_mod.get_global_var('func_4227')
call_4561 = relay.TupleGetItem(func_4225_call(), 0)
call_4562 = relay.TupleGetItem(func_4227_call(), 0)
output = relay.Tuple([call_4561,])
output2 = relay.Tuple([call_4562,])
func_4577 = relay.Function([], output)
mod['func_4577'] = func_4577
mod = relay.transform.InferType()(mod)
output = func_4577()
func_4578 = relay.Function([], output)
mutated_mod['func_4578'] = func_4578
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4590 = relay.var("var_4590", dtype = "int8", shape = (11, 11, 5))#candidate|4590|(11, 11, 5)|var|int8
const_4591 = relay.const([[[-7,2,9,-7,9],[4,2,4,-9,2],[-7,10,-8,5,8],[-3,-7,5,7,8],[3,-3,6,-9,-4],[-7,-9,1,3,-1],[10,-8,-9,4,-6],[-1,2,5,1,3],[4,6,-10,1,5],[-4,5,1,-4,9],[9,10,4,-1,9]],[[2,-5,5,7,1],[-9,4,-9,-8,-4],[-5,-7,-2,8,7],[7,-1,10,-2,-5],[7,-7,7,-10,9],[4,-4,-6,-3,2],[-6,-1,-5,-6,-6],[-7,-4,-7,-10,-6],[10,-4,-2,-3,-7],[-6,5,-1,-8,5],[-5,-8,9,-9,-4]],[[-2,6,9,6,-2],[-4,-5,6,9,-2],[-8,9,7,-5,10],[3,2,-6,7,10],[7,10,4,10,9],[-8,-1,5,8,4],[9,-10,9,1,-9],[9,-8,-8,2,6],[9,10,-2,8,7],[7,-1,7,2,8],[-1,-7,-6,1,-4]],[[1,10,5,-6,-3],[-7,9,7,8,5],[3,4,5,7,-10],[-3,-6,2,-7,4],[-3,2,9,-9,-3],[6,10,-7,2,1],[3,-2,-4,-10,-7],[5,-5,4,-10,-2],[7,8,8,2,-9],[3,-4,-3,-1,1],[9,-8,5,-10,-4]],[[8,10,9,-3,-1],[2,6,-9,4,2],[-8,3,5,9,-3],[-10,4,-10,10,-2],[6,5,7,1,-5],[-9,3,-10,-10,-4],[2,5,-3,-7,-8],[6,-2,-6,-4,-10],[-9,2,1,-10,1],[-5,9,-6,-6,-7],[-3,-10,3,-4,4]],[[-6,5,7,-9,8],[-3,2,-6,6,3],[-8,-8,1,-6,-8],[1,5,1,-1,-9],[10,-5,-5,1,2],[-7,-2,7,-6,-8],[-3,-10,4,-10,-2],[5,4,4,-8,-3],[3,-9,6,-8,-10],[9,-5,4,10,4],[7,-4,9,10,-7]],[[6,-4,-4,-2,3],[9,7,-8,-5,7],[10,9,4,-4,-5],[-9,8,7,-4,-4],[-3,6,9,5,4],[-5,7,-8,2,-7],[-10,8,-10,10,4],[-8,9,10,-9,3],[-6,-8,2,4,-6],[9,-7,-4,9,-10],[9,3,3,-5,-8]],[[-8,7,-9,-9,-1],[6,-3,-4,-2,2],[-10,-4,-7,8,-1],[-10,-5,4,6,-7],[-10,-6,7,-1,-4],[3,-4,-1,-3,-4],[-7,5,3,-6,-5],[-5,-7,10,-10,-5],[4,10,-4,-8,10],[-5,-6,1,-2,-8],[1,3,-4,-1,4]],[[9,-3,-5,-2,6],[-4,-2,-1,-2,9],[1,-3,7,-7,-2],[-6,10,-1,-8,7],[6,-5,2,1,-9],[3,-10,4,6,10],[4,-10,-5,9,-4],[7,6,8,8,-3],[10,8,-4,1,-6],[9,-7,4,10,3],[-10,3,2,3,1]],[[-6,-3,2,9,-9],[-4,-4,-9,-3,4],[4,6,-9,1,8],[-9,4,1,9,-1],[4,1,6,-8,1],[-5,-5,2,-1,5],[4,6,-6,-6,-6],[7,10,-9,10,-5],[1,-7,3,8,4],[-3,-9,-8,5,-2],[-9,-2,7,-7,-1]],[[9,4,-6,-7,1],[2,-10,5,6,2],[-3,-6,-1,-8,-1],[3,-1,-6,-6,-3],[-4,2,-6,4,7],[9,-8,-6,-8,-7],[3,9,-9,-3,7],[1,-1,-7,-2,-8],[-8,8,1,-5,8],[10,-4,-5,3,7],[6,-3,-4,5,-3]]], dtype = "int8")#candidate|4591|(11, 11, 5)|const|int8
bop_4592 = relay.greater(var_4590.astype('bool'), relay.reshape(const_4591.astype('bool'), relay.shape_of(var_4590))) # shape=(11, 11, 5)
func_4129_call = mod.get_global_var('func_4129')
func_4131_call = mutated_mod.get_global_var('func_4131')
const_4596 = relay.const([6,1,-8,5,-1,4,-10,7,-10,4,-3,10,9,1,-4,10,-4,5,-5,3,-3,-1,9,-1,-8,-3,-4,-9,6,3,-10,-1,-7,8,9,7,8,6,-3,6,-4,2,-3,2,-3,-1,-1,7,1,9,7,-3,-5,-4,-8,2,1,-1,-7,6,-10,-2,3,9,7,5,8,-10,-7,-1,-5,10,-7,2,5,-3,-7,6,-6,-4], dtype = "uint16")#candidate|4596|(80,)|const|uint16
call_4595 = relay.TupleGetItem(func_4129_call(relay.reshape(const_4596.astype('uint16'), [40, 2])), 0)
call_4597 = relay.TupleGetItem(func_4131_call(relay.reshape(const_4596.astype('uint16'), [40, 2])), 0)
uop_4604 = relay.acos(bop_4592.astype('float64')) # shape=(11, 11, 5)
var_4610 = relay.var("var_4610", dtype = "float64", shape = (11, 11, 5))#candidate|4610|(11, 11, 5)|var|float64
bop_4611 = relay.subtract(uop_4604.astype('int32'), relay.reshape(var_4610.astype('int32'), relay.shape_of(uop_4604))) # shape=(11, 11, 5)
output = relay.Tuple([call_4595,const_4596,bop_4611,])
output2 = relay.Tuple([call_4597,const_4596,bop_4611,])
func_4617 = relay.Function([var_4590,var_4610,], output)
mod['func_4617'] = func_4617
mod = relay.transform.InferType()(mod)
var_4618 = relay.var("var_4618", dtype = "int8", shape = (11, 11, 5))#candidate|4618|(11, 11, 5)|var|int8
var_4619 = relay.var("var_4619", dtype = "float64", shape = (11, 11, 5))#candidate|4619|(11, 11, 5)|var|float64
output = func_4617(var_4618,var_4619,)
func_4620 = relay.Function([var_4618,var_4619,], output)
mutated_mod['func_4620'] = func_4620
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4716 = relay.const([[[9.726045,3.093690,-4.008814,-4.275770,-2.086984,-1.484868]]], dtype = "float32")#candidate|4716|(1, 1, 6)|const|float32
const_4717 = relay.const([[[2.312903,4.191044,4.258582,-7.639945,-2.824515,0.188499],[2.529785,4.840073,3.671319,-0.205049,7.664829,-3.468229],[-9.237959,-8.778725,-2.587087,-4.325644,0.904052,1.356856],[-6.615972,6.335806,7.144228,5.368121,6.651799,4.007763],[-7.025329,9.259462,0.829861,-2.248846,5.092603,3.675162],[-6.258955,0.098190,4.600315,-6.609934,6.800247,-2.316533],[-7.658393,8.555028,-0.598305,-4.131025,-7.942537,-3.686633],[-3.308725,-5.658709,-6.511177,8.034483,9.246728,-0.731333],[5.389591,-4.497765,7.881902,6.789152,-1.291160,9.027938]],[[-0.172657,-3.442866,3.318108,-4.877657,4.084029,-3.272907],[-7.730625,-6.976970,-1.929242,0.149787,-8.102606,-7.573499],[-1.205623,3.601374,5.198838,-4.763470,4.015207,-5.232202],[5.697248,-9.889306,5.680245,-3.419601,-5.295682,5.074127],[-4.150360,-5.275915,8.232751,-2.071789,0.835363,-6.662855],[-5.919620,-5.456030,3.994563,1.487767,2.854263,2.122175],[-6.138369,-5.835507,0.330450,5.221519,-7.627673,-9.739790],[3.093515,-7.513882,-6.617997,0.783672,1.997255,-2.684194],[-5.529487,5.731097,0.992794,9.926953,6.844592,-7.087555]],[[2.708362,-4.738043,-8.211152,9.983945,4.401727,-2.512369],[1.541240,-1.308439,0.219467,7.157045,-4.213197,7.064686],[-4.378312,6.421326,-8.495013,-9.398083,-6.863117,-2.505537],[9.366086,-6.927042,2.521379,-5.666594,-0.565525,2.454825],[-6.773808,7.231698,5.656331,-3.744633,2.737621,7.130318],[-9.849263,-2.910070,-9.380030,9.531277,-9.623041,-7.418897],[-2.482874,-2.908043,-0.251585,-6.213652,7.188959,3.755108],[-1.232250,-6.208250,-9.871597,1.173659,9.603240,8.515201],[-2.791742,7.231582,-2.769197,-1.307505,-7.576080,2.059392]],[[-2.094507,8.325783,7.628928,0.952642,0.242405,-6.557021],[2.697130,-2.948301,5.254599,2.779868,-4.287050,-7.540444],[-2.099047,8.620262,-7.956278,2.305965,-8.694300,-9.983121],[-1.710146,2.477243,1.526916,0.808072,2.459597,8.821975],[3.639191,6.977067,0.621259,-1.015822,-2.958708,-0.416867],[-1.784135,-3.581570,1.164981,-1.562564,-9.485499,8.704765],[8.723573,-2.396137,-9.040005,4.212810,-0.956396,5.029396],[2.798115,-0.701993,9.840016,-8.818944,-0.911733,-8.782169],[1.335950,6.418550,-1.789822,3.922142,2.337421,-9.181877]],[[4.576957,8.312856,-9.540800,4.562582,-8.462507,-9.736924],[-4.529323,2.611690,1.039479,-1.852558,1.894174,-1.076706],[-1.503030,4.222916,5.619849,1.330811,-8.100719,1.470216],[8.159083,-1.424157,-5.316927,2.866560,5.824032,6.388167],[-6.962622,0.559735,-5.552845,7.133364,1.314306,-2.932974],[2.626001,8.684934,1.835507,-8.515711,2.284781,-0.459817],[3.006597,-8.248938,8.795868,4.639571,-3.677147,4.208357],[-5.367538,9.379966,9.236552,2.280403,-3.078783,-3.359366],[7.850531,-2.099858,7.766788,-8.756497,0.826769,3.559719]],[[-7.544542,-7.213723,6.258857,8.117144,0.107501,1.659624],[9.946234,0.131324,4.826853,5.759438,-1.300515,6.020362],[-0.018986,2.171908,8.764495,-1.657196,2.462376,-6.983933],[-6.674309,7.629421,-2.567745,5.923312,2.192864,2.398565],[-6.441075,9.704973,8.741371,5.725394,-0.091197,2.682534],[0.633881,2.696517,-1.628854,-6.471355,-6.668688,-0.297795],[-1.818430,-1.548990,-7.519517,5.008894,-0.403180,-3.305114],[7.644029,2.669644,-1.673615,4.407173,5.623230,-4.989497],[-1.000257,-5.522634,-4.115158,-2.548808,-8.768860,-6.842152]],[[-2.569280,-2.839776,-1.975444,-8.105932,-6.248046,3.527317],[-8.542037,-3.861677,-3.949887,-2.016738,6.089017,6.278724],[3.182795,6.650063,-3.500969,6.715033,5.007704,8.390157],[-7.677504,6.207777,0.230900,6.153619,-1.048709,1.615336],[-6.139112,7.492907,1.452353,-0.989832,-0.035738,-7.175614],[7.964859,-2.280348,4.580887,8.743673,1.486652,-7.839796],[4.245896,2.841847,-5.042057,-9.556708,-3.523932,-7.087293],[-4.359559,-1.869939,-2.731583,4.064049,-9.560337,-5.251203],[2.382574,9.215546,7.002036,-0.711903,2.954977,-1.096694]],[[-7.097394,2.078013,-2.050472,-0.372601,-6.907971,-8.328788],[-6.240989,-5.596894,5.269295,-1.819821,-7.563682,0.486478],[-3.820467,7.614646,0.884287,5.959903,-4.297478,-9.192698],[-4.749598,-5.057279,-0.999348,-7.353450,-7.640866,7.555677],[3.167984,3.329843,-0.680638,8.698488,-3.189012,-0.502475],[-9.393551,6.824201,-5.294932,-4.324375,3.668539,6.941757],[5.207229,-9.551395,7.438545,4.259807,4.741854,-7.042742],[6.210321,-7.227742,-5.039346,-1.636116,-3.966093,-6.032646],[1.061281,-0.087321,4.012717,-1.338663,3.390301,-5.182069]],[[7.087939,8.295121,-9.741266,-2.827375,-6.310110,0.130861],[9.802056,0.473606,-0.483375,4.003512,-8.982828,-8.029104],[4.869169,-1.142023,8.490041,7.011750,-5.226863,2.909701],[2.193413,5.194452,2.746906,-6.922734,-4.968056,-9.711436],[7.672013,-8.400752,4.239507,5.348507,-2.647003,9.578553],[3.354671,-6.162231,-6.027580,-9.064908,9.342242,4.273995],[1.740102,4.016714,0.559892,-8.540553,8.147572,5.007582],[7.329914,-6.134104,-5.560445,0.471724,-4.114289,-2.639378],[2.278541,-4.379112,-6.755845,7.846830,-6.714304,8.528531]]], dtype = "float32")#candidate|4717|(9, 9, 6)|const|float32
bop_4718 = relay.less(const_4716.astype('bool'), const_4717.astype('bool')) # shape=(9, 9, 6)
func_2560_call = mod.get_global_var('func_2560')
func_2561_call = mutated_mod.get_global_var('func_2561')
call_4726 = relay.TupleGetItem(func_2560_call(), 3)
call_4727 = relay.TupleGetItem(func_2561_call(), 3)
func_609_call = mod.get_global_var('func_609')
func_611_call = mutated_mod.get_global_var('func_611')
call_4737 = relay.TupleGetItem(func_609_call(), 1)
call_4738 = relay.TupleGetItem(func_611_call(), 1)
output = relay.Tuple([bop_4718,call_4726,call_4737,])
output2 = relay.Tuple([bop_4718,call_4727,call_4738,])
func_4739 = relay.Function([], output)
mod['func_4739'] = func_4739
mod = relay.transform.InferType()(mod)
output = func_4739()
func_4740 = relay.Function([], output)
mutated_mod['func_4740'] = func_4740
mutated_mod = relay.transform.InferType()(mutated_mod)
func_255_call = mod.get_global_var('func_255')
func_257_call = mutated_mod.get_global_var('func_257')
call_4752 = func_255_call()
call_4753 = func_255_call()
func_1656_call = mod.get_global_var('func_1656')
func_1659_call = mutated_mod.get_global_var('func_1659')
const_4787 = relay.const([-5.162834,7.113096,8.937285,-4.870419,-1.689748,-5.967106,6.645485,5.724272,-7.483359,9.102045,0.122123,1.100868,0.188729,-8.605083,1.109455,-7.595534,5.272341,-7.839683,4.437638,-2.686834,2.377078,4.383823,1.957852,6.024492,-6.489916,4.429375,-0.154199,8.983605,-2.648652,-3.360540,-7.062327,-2.336649,-9.156977,-6.401227,5.696274,1.121360,-1.197757,-9.930266,-7.644543,9.940008,-7.793794,-4.312837,-9.674666,-4.340347,6.379397,-6.258264,7.261332,6.285002,-7.267041,-7.953777,5.679109,-1.675485,-9.907247,2.889911,-0.873889,7.240517,3.640697,5.724167,3.667634,-5.823203,-6.187884,-7.497420,4.143062,3.822683,-8.888778,-1.918595,-5.752093,4.627038,8.656449,2.449829,5.565386,-6.207165,-2.633175,-3.834891,7.992393,-0.842256,-4.489394,-7.813946,-9.132164,3.084176,7.811890,-9.139253,-8.237852,-7.278338,-2.667567,7.055338,-7.476219,-9.180276,3.018132,-3.702199,-6.403833,-3.379083,-8.316674,-1.325539,-6.133260,5.898805,6.058916,5.335261,6.611177,9.477601,3.843965,2.460394,-1.298330,-8.623549,8.450518,3.848520,6.966827,-7.348801,-8.820304,4.084541,-1.265541,-2.164970,-1.466342,5.621713,6.429195,-9.660116,0.200064,-9.872065,6.390048,4.298411,3.398071,-9.657825,-9.813589,-9.732954,-1.153561,0.784801,-0.885927,-9.602798,-9.401255,-0.297594,9.196820,-9.346788,5.929212,-5.421805,-4.680108,5.244853,-1.881460,-3.623563,-8.251942,9.526254,-5.360674,3.211880,-8.154791,-2.259438,0.484961,-7.471693,1.600489,1.835092,2.309674,0.644909,3.379721,-2.271455,0.945935,-3.586526,2.850584,-9.426184,-2.322002,0.913891,2.669432,6.492838,-7.640456,2.416275,2.148844,-8.517638,9.570367,-1.348380,-0.185669,-3.961271,4.949346,9.492302,2.041206,2.416356,9.394787,-7.775345,-8.066291,6.151169,-0.900335,-5.767293,4.824772,-7.263370,-1.177067,2.627067,6.749337,-0.259496,-6.598335,-7.808440,8.135595,-3.536662,-6.619860,-8.520742,-6.888692,9.874734,-2.295720,-2.116286,8.752729,-6.654146,1.150956,-0.377579,-7.380663,-2.904231,1.175567,-0.279629,-9.462211,5.363828,7.670826,4.645156,-7.873399,-8.526823,-1.302573,-8.622976,-1.866024,6.433068,1.749945,-7.105151,2.653102,-9.499374,4.939187,9.511595,0.960691,-5.077134,-0.397571,3.291424,7.248605,-7.928216,-9.563445,9.436538,7.959116,6.427444,-0.741294,-0.852329,-3.008031,-2.736760,4.007933,3.055160,0.324316,-7.503413,6.115898,-6.487614,7.557094,-0.443966,2.951627,-4.567116,-7.059421,5.431670,-3.211307,-6.223504,7.269338,-3.453499,2.780171,0.346483,-4.870086,-7.164816,9.989772,-1.754221,2.242219,1.084560,-6.463054,-3.644348,5.928200,6.391796,7.591638,-2.168640,0.276804,-0.802320,-9.630547,9.028778,5.607624,-9.109571,-8.392390,3.007638,4.860521,-7.859439,5.555538,-4.196152,6.764333,-2.230770,-6.574002,7.941059,0.261007,-6.325867,4.457042,-6.224600,1.365709,-6.936759,3.895470,-4.210944,-9.754227,-6.604337,4.811110,-3.185292,9.527943,6.547544,5.331351,1.468028,-9.918763,-1.314407,8.344570,-0.534585,8.580986,-2.396557,7.446506,0.751232,0.831320,7.583514,-0.771370,1.386477,-6.119896,5.322879,7.013077,-7.184228,-4.132099,-5.824042,-4.971303,0.050736,9.780400,-3.785799,-4.609554,-5.161259,-7.441267,-4.921524,8.896236,-7.187649,-2.008123,7.751959,-5.628997,-6.241014,-8.148389,-2.245165,5.035419,-2.503308,1.374787,8.959995,-2.921200,2.979116,0.614305,0.482152,-5.367284,-2.449020,-9.631870,-8.725071,-1.634884,0.354914,3.751854,7.585743,2.918924,0.743871,-3.853904,-5.975212,-8.627114,8.533330,4.288591,-8.205235,-4.172938,4.669131,-3.174160,5.446543,-2.593342,0.958603,-8.913055,-4.096335,-1.657103,-1.219472,4.409180,2.679809,4.360191,1.505700,-9.818838,-0.664435,4.125394,0.326789,3.598260,-4.435433,0.924346,-6.724411,-8.126641,-0.187732,-0.941694,7.971730,9.488735,-5.784104,-8.096365,-5.234830,1.100324,1.362939,-4.545008,3.702620,-4.343854,7.107368,4.475795,3.175814,-0.677099,5.788339,3.289462,-0.197656,3.890184,2.055793,3.177911,-4.083214,-5.956657,9.784843,-4.455621,-5.250901,-4.236736,2.905451,5.606706,6.041622,-8.269137,2.793252,4.131643,-4.014719,-4.868907,-3.799349,0.304515,-5.909197,3.698211,-5.593531,-3.841032,-5.685602,-1.745720,3.787879,-1.085279,-7.085691,3.258171,-4.053183,6.531451,5.133655,-8.163006,9.126864,8.276985,9.476239,5.663737,-0.890469,7.381614,-3.362973,-9.126882,8.957635,-4.959177,2.226541,8.610726,0.818525,0.887961,-2.333748,-4.948532,4.157991,-3.847305,-6.839528,2.684739,1.114370,1.180760,-3.578279,1.306385,5.338203,1.159803,8.491648,-2.205903,-5.984528,-4.749699,-9.434875,-9.895757,-0.916775,-1.536401,8.647453,7.994102,-0.780677,-8.256932,8.006279,1.431284,-6.607177,8.682317,3.913369,-8.208329,6.023743,7.734583,1.942471,-7.330597,-3.839081,9.855440,-5.037171,-6.595244,3.220175,0.245964,2.025885,4.077501,-4.079620,1.323117,9.414869,8.448515,-3.844299,-4.518274,-8.007554,6.539108,0.223004,-8.606705,-2.610912,9.237468,-3.312703,-0.402449,6.349720,2.517276,-9.177434,7.493469,-0.313474,4.925577,0.815373,-0.187784,-7.746375,-3.717582,-1.583092,4.426826,-0.153871,6.349248,4.211761,-7.289063,7.402620,-2.523535,-4.633124,7.889195,-0.099461,-3.361954,-7.541831,-4.349673,-0.291344,3.789833,6.351459,5.566484,0.622704,-0.442176,-7.670728,0.897953,-1.852073,-5.517136,2.253838,2.790774,-8.343398,-5.063825,8.957383,4.703277,1.680658,-5.446902,1.516139,-3.405193,-8.042235,9.559148,1.614340,6.653083,3.902799,1.286742,9.236164,-8.159387,-0.801114,5.930431,2.178260,4.428457,4.652608,-7.361962,-5.232840,7.185379,1.598282,1.957198,3.478226,0.712038,-2.039536,9.940790,8.949387,3.083940,-0.930085,7.752607,2.859346,3.247237,2.011096,8.453255,-3.565823,-6.583459,-9.058894,2.625600,-0.652561,-9.422714,2.633519,1.063165,3.173185,-8.240166,8.156463,-6.553537,-0.496609,4.289300,0.341354,2.483091,8.872225,2.765297,-3.234135,5.797034,1.064539,9.251927,5.720853,-2.610426,-4.389422,7.506766,-9.265564,-6.352187,7.858882,-9.194294,5.084105,-3.646217,-7.348009,-5.072053,-6.743846,8.380380,7.920068,-0.443082,9.835183,9.325111,1.154182,1.247491,-2.819606,2.567984,5.343154,-4.785292,6.038135,9.205216,7.921253,-1.978547,9.919737,8.499880,0.948040,-1.447122,-2.721622,-1.875920,-2.304300,-3.523833,3.632990,-7.095175,9.736966,3.270764,2.260677,-3.532676,-7.988854,5.487172,3.461508,-0.547449,-8.306532,3.146647,2.841745,2.561884,-7.433559,-8.147683,8.955963,-0.637402,-7.532039,1.680060,2.434536,-4.630539,2.921956,4.731046,-1.538958,0.609332,-6.419435,-3.622489,-1.531501,4.738507,8.705806,-3.717475,-1.984891,4.064509,6.726916,1.251523,8.489260,-8.454510,8.339627,1.291838,-9.315017,-0.519371,9.093063,-5.206170,-0.269970,-0.753108,8.281666,-4.793589,-5.205134,-3.298333,3.823875,-5.067763,3.712048,6.993873,-8.849601,9.183910,9.557997,-1.829110,-8.732372,-6.123287,-7.096721,-7.444163,9.830994,-1.221224,-9.651139,0.872223,-0.263792,-7.302342,8.892100,-0.657588,-9.815890,-1.915904,7.896553,1.138262,0.853014,9.800337,-3.044620,2.404064,-0.542055,4.120125,7.375620,-7.300515,-0.119498,3.895288,-7.112200,-7.795789,6.543908,-8.510796,8.964896,-6.290987,1.639301,-2.989577,1.600814,-2.323792,0.744489,7.734341,-9.568692,-8.912049,-0.091883,-2.648228,5.693320,-1.922432,0.905638,-8.792521,-0.389251,6.544114,-7.193465,1.808130,-4.904240,4.767904,-9.343160,-0.752927,9.175666,5.672672,-2.229322,-4.675667,-5.892040,7.197642,-2.041408,-2.951008,-6.492002,-6.978883,-5.232800,0.463357,0.907575,-8.441649,9.876593,5.606267,-9.913324,-0.948925,-1.535529,-1.425637,8.640737,5.914779,9.114488,-6.234180,1.898959,-0.065519,7.919140,-5.972897,3.930983,-6.365539,2.431345,0.298186,-2.797589,5.104228,-0.238139,-8.428709,2.283292,3.022765,2.289896,-1.417178,9.941912,-9.412491,-6.222879,1.464183,-7.419961,-8.250784,9.049819,8.371624,-3.025304,7.827880,-8.064797,-3.107603,8.046329,6.195266,-5.717228,9.668663,-4.383584,-1.167373,0.675154,-3.942100,8.214997,5.020732,-5.638000,-3.190014,1.628353,-0.476236,7.382603,2.349988,-9.792294,-1.920611,8.683431,-7.070669,1.743706,-9.273704,6.138186,-0.163710,-3.538045,9.777321,-6.318724,6.413554,2.434710,-8.754998,-0.946798,6.934722,-0.587111,6.147475,-3.415498,6.760874,-7.052982,-1.862596,8.643718,-5.016928,-1.381174,-3.598928,-0.456483,5.770005,0.972549,-3.323526,5.903809,7.646800,6.816700,6.022061,-9.228340,-0.845668,6.778850,-9.485504,1.634284,-3.274849,7.287151,2.038684,-5.994590,7.170661,-1.703558,7.359833,-2.267615,8.145118,-4.394716,7.175163,2.462690,5.891063,-1.869466,0.306078,7.264434,6.821155,7.449231,-3.434192,6.732295,3.348812,6.120065,-4.675708,4.756509,-4.283146,-2.746500,6.448317,8.894668,-3.050483,-5.458757,3.679892,3.864308,-5.319580,5.601965,-6.215142,5.417006,-5.073725,9.890333,-9.695133,-6.428786,-2.369261,-8.759822,3.016412,-4.500634,1.025319,8.177961,-6.600309,5.747469,6.605084,9.174438,-2.781566,-7.945866,-2.660044,7.643919,-5.477844,0.110422,-8.253067,-1.145020,7.625752,-2.839960,-5.565177,8.770550], dtype = "float64")#candidate|4787|(910,)|const|float64
call_4786 = relay.TupleGetItem(func_1656_call(relay.reshape(const_4787.astype('float64'), [455, 2])), 1)
call_4788 = relay.TupleGetItem(func_1659_call(relay.reshape(const_4787.astype('float64'), [455, 2])), 1)
func_3525_call = mod.get_global_var('func_3525')
func_3526_call = mutated_mod.get_global_var('func_3526')
call_4791 = relay.TupleGetItem(func_3525_call(), 0)
call_4792 = relay.TupleGetItem(func_3526_call(), 0)
uop_4803 = relay.tan(const_4787.astype('float32')) # shape=(910,)
output = relay.Tuple([call_4752,call_4786,call_4791,uop_4803,])
output2 = relay.Tuple([call_4753,call_4788,call_4792,uop_4803,])
func_4820 = relay.Function([], output)
mod['func_4820'] = func_4820
mod = relay.transform.InferType()(mod)
mutated_mod['func_4820'] = func_4820
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4820_call = mutated_mod.get_global_var('func_4820')
call_4821 = func_4820_call()
output = call_4821
func_4822 = relay.Function([], output)
mutated_mod['func_4822'] = func_4822
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4869 = relay.var("var_4869", dtype = "bool", shape = (11, 1, 15))#candidate|4869|(11, 1, 15)|var|bool
var_4870 = relay.var("var_4870", dtype = "bool", shape = (11, 15, 15))#candidate|4870|(11, 15, 15)|var|bool
bop_4871 = relay.logical_or(var_4869.astype('bool'), var_4870.astype('bool')) # shape=(11, 15, 15)
func_1091_call = mod.get_global_var('func_1091')
func_1093_call = mutated_mod.get_global_var('func_1093')
call_4882 = relay.TupleGetItem(func_1091_call(), 3)
call_4883 = relay.TupleGetItem(func_1093_call(), 3)
func_2145_call = mod.get_global_var('func_2145')
func_2146_call = mutated_mod.get_global_var('func_2146')
call_4890 = relay.TupleGetItem(func_2145_call(), 0)
call_4891 = relay.TupleGetItem(func_2146_call(), 0)
func_949_call = mod.get_global_var('func_949')
func_951_call = mutated_mod.get_global_var('func_951')
call_4895 = relay.TupleGetItem(func_949_call(), 2)
call_4896 = relay.TupleGetItem(func_951_call(), 2)
func_1234_call = mod.get_global_var('func_1234')
func_1237_call = mutated_mod.get_global_var('func_1237')
const_4898 = relay.const([-4,1,7,9,7,-10,2,-8,-8,8,-3,-4,-2,10,-3,-7,-3,-6,6,-10,-7,-1,-10,-3,-4,-10,5,-1,-10,-4,4,-8,10,7,7,10,8,7,10,8,9,10,-1,3,-4,4,8,6,6,-5,1,-1,7,-6,-7,1,-2,4,-6,7,-3,9,-3,-1,-8,-5,4,-7,3,-7,8,10,3,-5,8,8,-3,5,1,6,-4,8,7,8,9,-2,-7,8,4,-6,5,8,-10,5,-10,-3,-2,-4,-4,-10,-2,-9,5,-9,-1,5,-9,-4,-5,4,-2,4,6,4,4,3,6,-5,1,2,-8,-10,10,-10,4,2,1,-9,-6,6,-5,-4,-5,4,4,10,2,3,-3,-7,-8,-1,7,-3,3,10,2,-10,6,5,-7,4,-4,-1,9,-5,7,6,-8,-6,10,-8,4,1,10,-10,10,8,2,-4,7,9,-5,-9,-4,3,-3,-10,9,-8,5,9,3,-3,7,7,-5,8,-9,-7,4,-1,-1,5,-10,2,-1,5,8,-1,3,1,-2,2,-5,-8,-6,-7,10,10,5,9,5,-1,10,-10,-10,3,-9,7,1,-5,4,6,4,-8,-10,-4,-9,-7,-9,-1,7,2,6,-10,-5,-4,6,5,-9,-6,9,1,-7,6,7,-6,1,10,7,4,6,-1,1,-2,-10,-9,-10,-5,-1,4,8,2,-8,-7,-4,-5,3,3,-5,-4,3,3,4,-2,-1,-10,-6,10,-5,-7,10,-9,1,8,-7,8,-6,3,9,6,2,8,-10,-2,-7,-4,-4,-1,5,8,2,1,-6,-1,-2,6,-2,-3,-5,7,-5,-9,4,-1,-9,-10,-4,-2,-7,-7,7,2,10,-2,-2,8,-10,6,7,2,8,-9,-4,7,2,-8,-9,-8,8,7,9,-9,10,-2,5,-3,7,-9,2,10,-2,-5,-3,-2,-5,2,2,-10,9,1,5,8,7,2,-5,-3,5,8,3,10,8,-9,-3,7,2,-5,2,-10,5,10,6,-5,-3,8,2,3,10,-2,-2,5,7,-2,7,9,8,10,-5,5,-7,-4,-9,-10,-9,-1,1,5,-8,-8,3,-7,-7,4,-3,7,-2,-10,8,-1,2,5,10,3,1,4,-9,2,9,7,5,-1,-7,-9,1,-1,1,-8,8,-10,-3,2,5,-7,1,6,7,4,-8,-10,-2,10,7,-4,-9,5,-9,5,10,-10,-5,-9,-4,10,-6,1,-9,1,8,10,-2,-3,-1,-8,-10,4,-7,-10,7,-4], dtype = "uint16")#candidate|4898|(480,)|const|uint16
call_4897 = relay.TupleGetItem(func_1234_call(relay.reshape(const_4898.astype('uint16'), [480,]), relay.reshape(const_4898.astype('uint64'), [6, 5, 16]), ), 3)
call_4899 = relay.TupleGetItem(func_1237_call(relay.reshape(const_4898.astype('uint16'), [480,]), relay.reshape(const_4898.astype('uint64'), [6, 5, 16]), ), 3)
uop_4903 = relay.log2(var_4870.astype('float32')) # shape=(11, 15, 15)
bop_4907 = relay.left_shift(uop_4903.astype('int64'), var_4869.astype('int64')) # shape=(11, 15, 15)
output = relay.Tuple([bop_4871,call_4882,call_4890,call_4895,call_4897,const_4898,bop_4907,])
output2 = relay.Tuple([bop_4871,call_4883,call_4891,call_4896,call_4899,const_4898,bop_4907,])
func_4911 = relay.Function([var_4869,var_4870,], output)
mod['func_4911'] = func_4911
mod = relay.transform.InferType()(mod)
mutated_mod['func_4911'] = func_4911
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4911_call = mutated_mod.get_global_var('func_4911')
var_4913 = relay.var("var_4913", dtype = "bool", shape = (11, 1, 15))#candidate|4913|(11, 1, 15)|var|bool
var_4914 = relay.var("var_4914", dtype = "bool", shape = (11, 15, 15))#candidate|4914|(11, 15, 15)|var|bool
call_4912 = func_4911_call(var_4913,var_4914,)
output = call_4912
func_4915 = relay.Function([var_4913,var_4914,], output)
mutated_mod['func_4915'] = func_4915
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3353_call = mod.get_global_var('func_3353')
func_3354_call = mutated_mod.get_global_var('func_3354')
call_4929 = func_3353_call()
call_4930 = func_3353_call()
func_4031_call = mod.get_global_var('func_4031')
func_4035_call = mutated_mod.get_global_var('func_4035')
var_4934 = relay.var("var_4934", dtype = "float64", shape = (4, 960))#candidate|4934|(4, 960)|var|float64
call_4933 = relay.TupleGetItem(func_4031_call(relay.reshape(var_4934.astype('float64'), [15, 16, 16]), relay.reshape(var_4934.astype('float64'), [15, 16, 16]), ), 2)
call_4935 = relay.TupleGetItem(func_4035_call(relay.reshape(var_4934.astype('float64'), [15, 16, 16]), relay.reshape(var_4934.astype('float64'), [15, 16, 16]), ), 2)
uop_4936 = relay.sigmoid(call_4933.astype('float64')) # shape=(3360,)
uop_4938 = relay.sigmoid(call_4935.astype('float64')) # shape=(3360,)
output = relay.Tuple([call_4929,var_4934,uop_4936,])
output2 = relay.Tuple([call_4930,var_4934,uop_4938,])
func_4947 = relay.Function([var_4934,], output)
mod['func_4947'] = func_4947
mod = relay.transform.InferType()(mod)
mutated_mod['func_4947'] = func_4947
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4948 = relay.var("var_4948", dtype = "float64", shape = (4, 960))#candidate|4948|(4, 960)|var|float64
func_4947_call = mutated_mod.get_global_var('func_4947')
call_4949 = func_4947_call(var_4948)
output = call_4949
func_4950 = relay.Function([var_4948], output)
mutated_mod['func_4950'] = func_4950
mutated_mod = relay.transform.InferType()(mutated_mod)
func_609_call = mod.get_global_var('func_609')
func_611_call = mutated_mod.get_global_var('func_611')
call_4961 = relay.TupleGetItem(func_609_call(), 0)
call_4962 = relay.TupleGetItem(func_611_call(), 0)
output = relay.Tuple([call_4961,])
output2 = relay.Tuple([call_4962,])
func_4964 = relay.Function([], output)
mod['func_4964'] = func_4964
mod = relay.transform.InferType()(mod)
mutated_mod['func_4964'] = func_4964
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4964_call = mutated_mod.get_global_var('func_4964')
call_4965 = func_4964_call()
output = call_4965
func_4966 = relay.Function([], output)
mutated_mod['func_4966'] = func_4966
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2560_call = mod.get_global_var('func_2560')
func_2561_call = mutated_mod.get_global_var('func_2561')
call_5084 = relay.TupleGetItem(func_2560_call(), 4)
call_5085 = relay.TupleGetItem(func_2561_call(), 4)
var_5086 = relay.var("var_5086", dtype = "uint16", shape = (2, 240))#candidate|5086|(2, 240)|var|uint16
bop_5087 = relay.multiply(call_5084.astype('uint32'), relay.reshape(var_5086.astype('uint32'), relay.shape_of(call_5084))) # shape=(2, 240)
bop_5090 = relay.multiply(call_5085.astype('uint32'), relay.reshape(var_5086.astype('uint32'), relay.shape_of(call_5085))) # shape=(2, 240)
uop_5098 = relay.rsqrt(var_5086.astype('float32')) # shape=(2, 240)
output = relay.Tuple([bop_5087,uop_5098,])
output2 = relay.Tuple([bop_5090,uop_5098,])
func_5102 = relay.Function([var_5086,], output)
mod['func_5102'] = func_5102
mod = relay.transform.InferType()(mod)
mutated_mod['func_5102'] = func_5102
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5103 = relay.var("var_5103", dtype = "uint16", shape = (2, 240))#candidate|5103|(2, 240)|var|uint16
func_5102_call = mutated_mod.get_global_var('func_5102')
call_5104 = func_5102_call(var_5103)
output = call_5104
func_5105 = relay.Function([var_5103], output)
mutated_mod['func_5105'] = func_5105
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5185 = relay.var("var_5185", dtype = "float64", shape = (9, 11, 12))#candidate|5185|(9, 11, 12)|var|float64
uop_5186 = relay.cos(var_5185.astype('float64')) # shape=(9, 11, 12)
uop_5190 = relay.log10(var_5185.astype('float64')) # shape=(9, 11, 12)
uop_5200 = relay.sin(uop_5190.astype('float32')) # shape=(9, 11, 12)
func_1574_call = mod.get_global_var('func_1574')
func_1575_call = mutated_mod.get_global_var('func_1575')
call_5203 = func_1574_call()
call_5204 = func_1574_call()
uop_5211 = relay.acosh(var_5185.astype('float64')) # shape=(9, 11, 12)
func_577_call = mod.get_global_var('func_577')
func_580_call = mutated_mod.get_global_var('func_580')
call_5217 = func_577_call(relay.reshape(call_5203.astype('bool'), [3, 8, 9]))
call_5218 = func_577_call(relay.reshape(call_5203.astype('bool'), [3, 8, 9]))
output = relay.Tuple([uop_5186,uop_5200,call_5203,uop_5211,call_5217,])
output2 = relay.Tuple([uop_5186,uop_5200,call_5204,uop_5211,call_5218,])
func_5220 = relay.Function([var_5185,], output)
mod['func_5220'] = func_5220
mod = relay.transform.InferType()(mod)
mutated_mod['func_5220'] = func_5220
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5221 = relay.var("var_5221", dtype = "float64", shape = (9, 11, 12))#candidate|5221|(9, 11, 12)|var|float64
func_5220_call = mutated_mod.get_global_var('func_5220')
call_5222 = func_5220_call(var_5221)
output = call_5222
func_5223 = relay.Function([var_5221], output)
mutated_mod['func_5223'] = func_5223
mutated_mod = relay.transform.InferType()(mutated_mod)
func_332_call = mod.get_global_var('func_332')
func_333_call = mutated_mod.get_global_var('func_333')
call_5245 = func_332_call()
call_5246 = func_332_call()
func_3995_call = mod.get_global_var('func_3995')
func_3997_call = mutated_mod.get_global_var('func_3997')
call_5267 = relay.TupleGetItem(func_3995_call(), 0)
call_5268 = relay.TupleGetItem(func_3997_call(), 0)
output = relay.Tuple([call_5245,call_5267,])
output2 = relay.Tuple([call_5246,call_5268,])
func_5269 = relay.Function([], output)
mod['func_5269'] = func_5269
mod = relay.transform.InferType()(mod)
mutated_mod['func_5269'] = func_5269
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5269_call = mutated_mod.get_global_var('func_5269')
call_5270 = func_5269_call()
output = call_5270
func_5271 = relay.Function([], output)
mutated_mod['func_5271'] = func_5271
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4396_call = mod.get_global_var('func_4396')
func_4398_call = mutated_mod.get_global_var('func_4398')
call_5310 = func_4396_call()
call_5311 = func_4396_call()
func_4225_call = mod.get_global_var('func_4225')
func_4227_call = mutated_mod.get_global_var('func_4227')
call_5345 = relay.TupleGetItem(func_4225_call(), 0)
call_5346 = relay.TupleGetItem(func_4227_call(), 0)
func_989_call = mod.get_global_var('func_989')
func_991_call = mutated_mod.get_global_var('func_991')
call_5353 = relay.TupleGetItem(func_989_call(), 0)
call_5354 = relay.TupleGetItem(func_991_call(), 0)
output = relay.Tuple([call_5310,call_5345,call_5353,])
output2 = relay.Tuple([call_5311,call_5346,call_5354,])
func_5356 = relay.Function([], output)
mod['func_5356'] = func_5356
mod = relay.transform.InferType()(mod)
output = func_5356()
func_5357 = relay.Function([], output)
mutated_mod['func_5357'] = func_5357
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5358 = relay.var("var_5358", dtype = "float32", shape = (10, 12, 8))#candidate|5358|(10, 12, 8)|var|float32
uop_5359 = relay.log(var_5358.astype('float32')) # shape=(10, 12, 8)
func_4303_call = mod.get_global_var('func_4303')
func_4305_call = mutated_mod.get_global_var('func_4305')
const_5366 = relay.const([-6,-8,-5,-6,-5,-6,1,-7,-5,5,-7,-8,5,-7,9,-9,-7,4,10,-2,4,3,1,-6,-5,8,1,-10,-10,-3,9,4,7,-5,-7,3,-5,5,-6,-4,2,-3,-8,1,10,-4,4,-4,-5,-9,5,4,-6,-10,9,-3,4,6,-1,-9,-1,-1,-5,7,3,2,7,2,4,8,-5,-8,1,2,-9,4,-8,-4,-1,2,-6,-3,-10,-8,8,2,1,2,-2,-3,-7,-2,3,5,8,7,2,8,-9,-10,6,-8,-2,8,-5,6,7,7,5,-3,9,-6,4,-7,-4,-7,9,-7,8,-6,6,6,-1,3,-5,8,8,9,1,4,2,-6,-9,-1,-8,-3,-10,-10,-4,-6,1,4,-9,-3,8,-6,9,1,-6,-8,-1,1,-9,-2,-3,-1,2,4,-10,-2,4,-9,9,-2,2,9,10,3,-10,4,3,8,3,-7,-8,-1,4,-7,8,7,-1,3,8,-3,-1,4,2,-9,3,-10,-4,5,-1,-2,2,-8,10,6,-9,8,6,6,-3,5,-3,-9,5,7,-6,4,-10,1,-6,-8,6,7,-10,-1,9,1,10,1,5,1,6,-9,10,8,7,-2,-4,6,-1,-6,-3,-4,-8,10,2,-7,9,-9,-6,-4,3,-7,-5,8,9,8,-5,-7,-9,8,-8,-2,-1,-5,-7,3,7,4,2,-9,10,-3,2,-7,6,-2,10,-3,-6,9,9,1,1,-9,-1,-2,-8,5,-4,2,-10,6,10,-1,8,-10,-2,-5,8,6,4,2,4,5,4,9,4,3,5,-10,6,3,1,-2,4,10,-7,-2,-4,8,4,1,3,2,10,2,-2,-5,-3,-3,5,4,8,3,-3,-1,8,-7,-7,-10,10,4,-7,6,6,-4,3,-2,-6,-6,-6,7,10,-9,-4,-6,1,8,-1,-5,-4,-9,-8,9,-6,4,3,-9,7,1,-5,6,9,3,6,8,-8,6,-9,-2,3,8,7,-8,3,8,8,-3,7,8,3,-5,4,7,-10,8,-4,7,4,-8,7,-5,9,6,6,-1,-2,10,-10,9,5,-3,-4,10,8,-6,-5,1,-1,-2,-1,-7,-3,-10,5,3,7,-9,-6,10,9,8,9,10,6,-8,-6,1,2,-4,-3,9,3,-2,8,-5,-9,3,-4,-7,-6,1,-2,3,6,-2,-4,-8,8,-10,-3,7,7,10,-4,4,-4,4,-7,-1,-6,-9,-4,1,-6,-10,5,-1,-9,6,1,-3,-4,2,-8,4,4,6,2,-9,8,9,9,6,2,9,-1,-10,-3,-8,-3,-5,-8,6,6,-10,7,8,9,1,-7,5,-7,4,-7,-1,7,-9,4,-6,-1,7,-6,-1,10,-6,-4,-6,8,-1,6,-7,-5,-9,2,-3,2,8,-6,2,-2,-4,1,-9,4,6,-1,3,9,-7,7,-3,-10,6,-1,4,7,4,-10,9,-3,3,7,-10,-8,-9,-6,4,3,-4,8,-2,5,-7,6,-10,10,-3,-9,-7,-1,-2,7,5,-7,6,4,-2,-3,6,4,8,-1,-3,5,9,-6,-5,8,5,-8,3,-9,2,4,1,6,-4,-4,9,-6,-7,1,5,1,-7,1,10,-4,3,-2,8,6,7,8,9,-4,8,8,5,5,8,-1,-7,-3,-5,-7,-5,4,4,7,9,2,7,3,1,5,2,-10,-2,-1,9,9,-10,-5,-6,8,6,-3,9,-6,-3,-10,8,6,-2,-9,3,-5,3,-7,-4,6,-4,4,6,6,2,6,5,-10,-9,9,6,-4,6,10,6,-2,5,-6,8,10,-7,10,8,-2,-8,8,-7,-5,-6,4,10,-4,2,8,3,9,-6,-3,-8,1,8,-2,-4,7,-1,-3,7,-6,1,-10,-3,4,10,6,-6,6,8,6,-6,-3,-4,-7,-6,-9,-8,1,9,-3,-7,-7,-5,7,-10,5,-8,2,-5,-2,-4,9,-1,5,8,-9,8,9,8,7,9,-5,-8,-8,5,-3,-2,-3,3,-4,-10,9,2,1,2,-9,8,7,-10,1,4,6,-8,-10,9,-3,9,-4,10,3,3,-2,-6,9,3,-3,5,2,8,-4,5,5,1,-7,7,2,1,-1,4,-7,1,3,-9,7,6,6,1,7,5,3,-3,-3,1,-5,5,2,-10,-2,-10,8,-10,-7,-10,-3,6,6,-2,-8,-3,10,3,-4,8,5,4,-4,-10,7,3,4,7,3,-8,-4,1,1,-9,8,2,5,-7,-10,2,-8,7,-6,-3,-4,7,-4,-4,-4,-1,-10,6,-8,-6,1,-8,-3,-10,-9,-8,-3,-3,-7,3,9,4,8,-7,-4,-7,-1,3,-1,-4,7,3,9,9,2,5,-6,3,10,2,-2,-10,-5,-8,-7,7,4,-4,-8,7,2,3,5,-6,7,1,-9,4,-4,-10,-5,-5,-9,-2,-9,-8,2,-3,-9,-4,-8,-6,3,-1,-2,-8,-2,-6,9,9,-6,2,-10,7,-3,8,3,8,-3,5,-4,2,5,6,-5,-5,-1,1,2,-3,-8,-8,-4,-8,-7,-2,-5,4,4,7,4,10,-7,-7,8,5,10,8,-10,-10,-9,-6,9,-6,2,2,-5,3,5,2,1,-9,9,-4,-4,-3,-5,9,1,-6,-1,10,1,8,3,-9,-7,5,8,4,2,-4,8,-2,1,3,8,-5,-7,7,5,6,6,6,1,-7,7,3,-7,6,4,-9,3,1,9,1,4,3,-9,6,-9,4,-6,-5,3,-2,-1,1,-5,5,10,5,1,8,7,1,-8,-5,-3,9,2,-5,2,-6,-8,-10,-6,6,3,7,-7,7,5,-10,-2,6,-2,-6,9,-1,2,-7,6,-6,-7,-10,-3,-10,1,-9,-10,-7,-10,-7,7,-5,-7,7,-8,-2,-8,-9,-9,1,8,-5,7,-9,6,-5,3,-2,-4,6,4,9,10,4,5,-1,7,9,9,10,-5,-8,7,-9,-3,-5,2,-10,9,4,-1,-7,3,4,-6,-7,9,9,7,7,2,-8,5,9,-4,-8,-1,5,2,4,-4,-9,6,1,8,5,9,6,-1,-7,-1,-2,-1,6,8,3,1,-7,2,4,5,9,1,9,4,7,-5,8,7,1,-4,-7,6,5,1,7,-7,9,4,9,6,-5,-4,6,7,-7,2,7,8,-8,-1,3,5,-7,-4,9,4,-10,7,10,-5,-6,-10,7,-6,5,3,-9,-3,-7,5,-6,10,-5,-2,-2,1,4,-2,9,7,7,-3,-8,3,3,3,-4,5,-1,-6,4,2,1,10,-2,-4,-8,-5,5,-4,-7,8,-2,-3,-10,8,8,-3,-6,1,-9,-6,3,-3,-1,-5,-4,10,-7,-10,3,2,-10,2,-7,3,-7,-3,2,7,3,-4,6,-2,8,-10,2,4,-7,7,9,-2,-8,-5,2,-8,7,-1,-7,-5,-7,-5,7,2,-6,-1,-8,1,7,10,9,4,7,8,10,-10,8,-9,-5,-2,9,-7,-4,5,-4,3,-3,9,2,-6,1,-3,-1,6,3,-8,9,1,2,7,1,9,-6,-5,-6,-5,7,7,-10,6,9,8,-1,-3,5,9,1,1,8,6,-9,2,8,-3,-10,-4,5,9,10,-9,4,-10,-7,2,9,1,10,-1,3,-9,-5,6,-4,3,6,9,-9,-5,-10,-4,-5,-6,-8,-3,2,-8,4,6,10,2,-1,-8,-9,-9,-9,9,-7,9,3,10,4,2,-3,-8,10,-9,-10,-3,1,10,-4,4,-6,-9,-6,6,-7,10,9,-3,7,-1,-10,-7,-6,-10,10,4,-8,-6,-9,6,1,8,-5,8,-2,2,3,2,8,10,6,5,6,-10,-4,-3,-6,4,1,-7,2,6,9,-5,-1,-7,10,3,-3,-10,-1,1,-3,1,6,-8,7,4,-3,-5,3,-1,3,-8,9,3,-5,9,9,4,10,-4,6,-3,6,-3,-7,3,-10,-8,2,-1,6,-5,-10,10,8,6,-1,-5,4,-5,2,-5,-10,-1,4,9,10,5,-10,-1,-1,6,-6,9,7,-5,4,9,-2,-8,2,8,-9,3,10,-2,1,-2,-7,8,-7,-2,2,-6,-4,1,-10,-8,-2,10,5,2,10,-4,7,10,7,-4,5,-3,2,3,-3,-5,-1,8,9,-3,-5,3,-1,5,-6,6,9,-8,-3,7,1,-10,6,-10,7,-1,10,-6,10,-10,-2,-8,8,-6,-7,7,-4,2,-7,5,6,6,-4,9,-6,10,7,-9,-4,-6,-7,-10,-1,10,-7,-2,3,-10,-2,8,-10,-6,-6,2,9,10,-2,-6,5,9,-3,6,10,-10,5,-10,8,-1,-10,-4,-10,6,7,5,10,-3,-6,8,4,-8,-9,3,-4,-4,7,5,4,-1,5,-2,-1,-9,-3,3,-4,6,1,3,-4,-4,-6,-2,2,1,9,-2,8,7,8,-9,-3,8,-4,3,-7,-3,-6,3,-6,5,8,8,-1,-9,5,3,-5,-5,-3,1,5,-5,6,-1,4,10,5,10,-10,-9,9,6,5,4,-10,-10,-6,-8,-2,-5,-4,10,2,9,1,1,-10,-3,-10,4,4,7,-8,-2,-3,-7,-5,-8,9,1,7,-7,10,-3,10,10,-1,4,9,10,-5,1,-5,7,8,1,9,-4,1,9,5,5,-4,7,-5,7,5,-1,7,-6,7,2,-7,-7,4,-2,-3,6,4,-1,2,2,-6,-10,3,9,3,-8,-8,1,-10,2,9,-1,5,5,-9,-5,-10,-7,-2,6,10,10,-10,-1,-3,4,-2,7,8,-5,9,-4,-8,3,-9,-7,-5,-6,-7,5,-1,4,-5,-3,2,-2,9,-9,6,6,3,4,-8,2,9,-7,-6,4,-1,4,4,-2,9,9,-5,5,-8,-5,1,-4,-3,-1,-2,-10,-3,-4,-8,3,10,-7,6,-3,2,3,-5,6,-9,-9,-5,4,1,6,-6,9,10,9,7,-2,-1,-2,5,-6,-6,-5,-4,-8,7,-4,-2,9,10,-10,1,8,1,10,-8,10,1,-3,-6,-10,5,-8,-1,-1,-6,-10,6,-10,-7,-3,-9,1,10,-7,-6,-1,-2,-10,-7,-6,5,-9,3,8,-2,-7,5,10,-3,-4,-3,10,6,-2,10,-6,-3,5,-6,8,-3,-8,-2,-4,5,-3,-2,8,10,3,-8,-6,3,7,-6,7,1,-8,4,-9,1,-9,-3,-3,7,-7,-2,-5,6,-4,10,-2,5,-3,3,9,-4,-8,-7,3,6,10,5,-3,-9,3,-8,-8,8,-3,-5,-4,-1,9,-3,4,2,-7,9,-8,-9,-8,8,2,-1,-7,-7,7,-5,-8,1,-8,-5,-10,9,5,-8,4,10,2,-1,8,-9,-8,3,3,-9,7,-7,8,-4,3,5,10,5,9,-10,-6,3,-3,1,2,-8,3,7,-1,-6,5,-4,-9,8,7,-4,-6,8,-5,9,8,-10,5,4,-10,-2,2,-1,-7,10,6,-10,2,6,-8,7,-2,-6,-4,-3,-1,-9,-1,5,-1,3,-8,10,10,7,10,-3,-3,-7,9,1,-5,4,-3,3,5,-1,-8,3,8,-5,6,-1,6,3,-10,-7,7,10,-2,3,-10,10,-5,5,3,-2,-5,-5,10,6,4,-2,7,-10,6,6,-6,-3,1,6,5,2,-8,-3,-7,-8,-4,-2,6,-2,5,-8,6,4,1,-1,8,8,-2,-6,-10,2,9,-7,-7,-7,6,-5,-9,10,-1,-6,-4,-6,-5,-5,-9,1,2,10,6,2,-3,6,8,-1,9,-7,-2,-1,-5,4,-5,9,2,7,-9,1,7,-5,5,3,3,-9,3,4,8,10,-2,3,10,-1,10,-10,-1,-10,-1,2,-3,1,-3,-3,-2,6,-4,5,10,5,-1,-7,-10,-9,-1,6,-2,-1,-1,-5,7,-4,-2,-9,8,4,-8,10,-9,-2,-9,-6,5,-3,-2,-9,2,4,-4,-8,-4,2,3,-4,10,-7,-4,2,-2,8,-5,-5,-10,-1,-9,-9,-1,-8,10,1,6,2,2,-1,-9,8,-4,1,1,10,-10,4,-7,-8,-2,10,-6,10,-6,-2,-10,1,3,-9,5,-4,-8,6,1,-6,-2,5,-1,-6,7,-4,-8,10,8,-6,9,-5,10,-6,-7,6,-1,9,-7,10,5,-9,-10,4,8,-8,10,6,9,1,-6,-7,-7,8,-5,7,4,-1,-5,-2,-5,-10,6,-4,-9,2,3,2,-10,-3,-1,-3,6,-1,8,-4,6,5,3,10,6,7,3,-9,-10,-6,-5,-7,-2,2,4,1,1,5,-7,5,-6,3,2,10,6,-6,-2,2,3,-4,-1,10,-2,5,9,5,4,3,-1,1,-7,-8,2,-5,-1,6,3,-3,1,6,-2,5,10,4,-9,9,-4,8,-5,4,1,10,-6,-1,-5,-8,10,2,1,3,5,-7,9,6,8,3,-10,7,8,-4,7,-7,-5,-8,7,6,3,2,9,-7,-7,-10,3,-4,5,3,10,-10,-1,9,10,-1,-7,7,10,-6,-4,6,4,-8,8,3,-1,10,3,-9,3,10,-10,9,-8,-9,-9,-10,6,4,-1,-1,1,-2,1,9,-1,7,5,3,8,8,10,-2,7,-10,2,1,-5,8,-4,1,8,-9,3,-8,6,10,-3,-2,-8,-9,6,-4,2,-8,-10,4,-8,-3,-6,3,5,8,10,10,-4,8,10,-2,5,1,-10,7,1,-10,1,9,-1,-5,10,-8,-6,-6,-10,9,8,-5,8,-6,-2,-5,10,-2,-4,-1,-4,-9,-7,7,3,5,9,-10,1,-5,2,9,-6,4,-8,4,-4,-2,-8,-8,-8,-4,2,5,2,10,2,8,8,7,7,-10,4,9,3,-3,-10,-8,-1,-8,5,-6,5,4,-6,-1,-2,-3,3,6,-1,8,6,-4,1,9,-9,-2,9,-2,-6,-9,6,-5,-3,-6,2,6,2,-6,-3,8,9,10,5,-6,-5,-9,6,9,-5,-6,10,6,3,6,6,-9,3,5,-1,9,6,6,-10,-1,-1,3,-8,-5,10,6,5,-2,-7,6,-10,4,3,-7,-7,9,3,1,-2,2,-6,-9,-6,-9,10,10,10,-5,6,-7,8,4,9,-5,-2,4,-7,-10,4,5,7,-3,1,-2,-7,3,5,1,1,-5,-4,2,2,6,1,9,9,7,-7,9,7,3,9,6,-1,4,1,-9,-8,-8,-8,-9,8,-9,4,-3,9,-3,-10,-8,-1,6,-8,5,-10,5,4,5,9,-9,1,5,7,-10,-6,-6,1,-9,7,-5,8,4,-3,4,-2,-8,-4,-5,-1,-8,3,4,-5,3,8,10,-7,8,5,5,-6,4,-5,2,4,-5,-3,-3,3,-2,-5,6,1,5,9,-7,4,-4,-10,5,6,3,8,-8,3,1,-4,-9,3,3,3,-7,-9,5,7,3,1,-1,-3,1,10,-1,9,9,5,3,2,-6,1,10,3,-1,1,-5,-4,-10,8,-9,5,-10,2,10,-3,2,-8,-4,-8,-7,-1,-5,9,-9,1,6,6,8,-9,-1,-5,-10,7,-5,-1,8,-5,8,10,-10,3,-7,-2,-8,-3,7,4,-10,1,8,8,-7,8,-6,1,1,2,7,-5,6,4,6,1,10,3,-8,-3,3,-10,-2,-7,-9,1,4,8,3,-5,3,7,2,1,-1,6,-10,5,9,4,-10,1,2,7,-5,-6,-10,2,-5,3,9,-1,6,-10,-9,-5,3,4,7,-3,-4,1,-4,-6,-5,-4,-10,3,5,3,2,-3,-5,-2,-6,7,6,4,8,-8,2,-9,-10,-8,-10,7,2,8,-6,-10,-5,-4,2,10,1,6,1,4,8,6,-7,-1,-2,-6,7,-1,-10,3,5,3,3,-7,-5,-6,7,2,-7,-4,-9,-7,4,-1,5,6,7,-5,-1,5,-5,10,4,-7,2,-10,-10,9,7,8,-4,-1,6,-3,8,4,8,-7,-3,-3,-4,7,-10,-7,8,8,-10,5,6,-4,6,8,-1,8,9,-10,-6,6,7,2,7,-7,10,-4,10,1,-7,1,5,-3,-3,-7,3,-5,-5,6,-9,-10,7,-7,3,4,-8,1,6,-8,-10,-10,-6,-3,-5,4,2,-5,9,5,-10,5,5,1,-1,-2,4,4,-8,5,-6,9,3,8,-6,4,-3,5,-5,9,7,-5,-3,3,5,-7,6,-2,10,1,-2,-3,3,3,4,2,-3,-4,-7,10,-6,-5,-2,1,9,-7,6,6,-8,9,-2,5,9,2,6,-10,-8,5,3,2,-10,3,-3,-7,-9,-4,9,-6,1,-4,9,-1,10,7,-4,3,1,9,-6,-4,-5,8,10,-10,-10,-9,-10,-8,-6,4,-5,3,-5,-2,1,8,8,7,7,-10,6,8,8,8,10,-4,-9,4,9,6,2,5,-9,-10,4,3,-7,-7,6,9,-5,2,-1,-9,2,2,1,-6,4,5,3,-7,3,-5,9,-7,-8,10,7,10,7,5,-1,-6,-6,2,-3,2,-3,4,-3,-8,-2,-2,10,-8,6,-4,-6,-2,5,2,3,1,10,-1,8,6,8,9,-2,4,2,-4,2,9,-2,-5,-4,4,-4,9,-2,2,-2,5,-7,1,9,-8,-5,-8,7,-3,-2,6,-10,9,-9,2,-9,-5,-8,-6,6,-9,10,-10,-3,-9,-10,2,-10,-1,-10,-10,10,7,-6,6,-8,4,4,-6,-9,-3,-2,8,-8,2,-2,8,10,1,-10,-9,-3,6,-9,4,7,-6,4,10,-10,9,7,-5,5,-4,-4,3,9,3,-10,-7,-6,-4,4,-2,8,-10,1,1,-1,10,9,-1,1,-6,2,-7,-6], dtype = "int16")#candidate|5366|(3360,)|const|int16
call_5365 = relay.TupleGetItem(func_4303_call(relay.reshape(const_5366.astype('int16'), [15, 16, 14])), 0)
call_5367 = relay.TupleGetItem(func_4305_call(relay.reshape(const_5366.astype('int16'), [15, 16, 14])), 0)
func_2891_call = mod.get_global_var('func_2891')
func_2892_call = mutated_mod.get_global_var('func_2892')
call_5371 = relay.TupleGetItem(func_2891_call(), 0)
call_5372 = relay.TupleGetItem(func_2892_call(), 0)
bop_5375 = relay.divide(const_5366.astype('float64'), relay.reshape(call_5365.astype('float64'), relay.shape_of(const_5366))) # shape=(3360,)
bop_5378 = relay.divide(const_5366.astype('float64'), relay.reshape(call_5367.astype('float64'), relay.shape_of(const_5366))) # shape=(3360,)
output = relay.Tuple([uop_5359,call_5371,bop_5375,])
output2 = relay.Tuple([uop_5359,call_5372,bop_5378,])
func_5389 = relay.Function([var_5358,], output)
mod['func_5389'] = func_5389
mod = relay.transform.InferType()(mod)
var_5390 = relay.var("var_5390", dtype = "float32", shape = (10, 12, 8))#candidate|5390|(10, 12, 8)|var|float32
output = func_5389(var_5390)
func_5391 = relay.Function([var_5390], output)
mutated_mod['func_5391'] = func_5391
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4820_call = mod.get_global_var('func_4820')
func_4822_call = mutated_mod.get_global_var('func_4822')
call_5417 = relay.TupleGetItem(func_4820_call(), 0)
call_5418 = relay.TupleGetItem(func_4822_call(), 0)
func_1186_call = mod.get_global_var('func_1186')
func_1187_call = mutated_mod.get_global_var('func_1187')
call_5421 = func_1186_call()
call_5422 = func_1186_call()
bop_5430 = relay.subtract(call_5421.astype('float64'), relay.reshape(call_5417.astype('float64'), relay.shape_of(call_5421))) # shape=(3, 8, 9)
bop_5433 = relay.subtract(call_5422.astype('float64'), relay.reshape(call_5418.astype('float64'), relay.shape_of(call_5422))) # shape=(3, 8, 9)
func_3183_call = mod.get_global_var('func_3183')
func_3187_call = mutated_mod.get_global_var('func_3187')
var_5436 = relay.var("var_5436", dtype = "uint16", shape = (80, 1))#candidate|5436|(80, 1)|var|uint16
const_5437 = relay.const([-1,1,-3,-7,-6,8,-9,3,-9,-8,-5,-7,-4,5,9,3,7,5,3,-6,-7,6,9,10,2,-8,-6,9,-1,-9,-10,-10,6,-7,-9,7,7,10,5,-5,-1,-3,1,-6,-6,-3,-9,3,10,4,3,5,-5,8,-6,-6,-8,-3,-2,-1,6,-5,7,-2,-8,-8,8,-2,8,-4,3,-3,-10,9,-7,-4,-4,-10,9,-10,10,9,-1,2,1,6,-5,-4,-5,-1,-3,5,-4,-10,9,-1,10,-7,-8,-2,7,2,7,9,9,2,6,1,2,-2,-3,-10,-2,-6,7,1,8,-8,-9,4,-8,2,-6,4,6,9,-9,-6,5,3,-2,6,8,-2,10,7,-6,1,-3,8,-3,1,-3,2,1,-9,-10,2,10,2,-1,9,-7,-7,-7,2,-3,1,1,3,-1,-4,9,6,9,-9,-9,8,-1,8,4,-8,-4,3,4,-7,10,3,-5,-1,1,5,-8,-7,1,-7,-7,2,-3,9,10,-2,7,-4,-6,-9,4,-8,8,-3,3,4,4,5,10,5,-10,-4,2,-1,2,-7,3,-9,1,2,2,5,-5,-3,4,6,-5,-3,10,-7,-4,-9,10,-10,1,-6,-1,9,3,10,2,-1,8,-5,-8,1,9,-10,7,1,-5,1,7,-1,-1,-8,-9,-1,-5,-7,1,6,7,8,-6,-4,-5,7,4,-2,9,10,-3,8,9,10,3,-9,-9,-6,7,6,-4,4,10,-3,-10,-8,-5,-8,2,-2,5,5,10,1,-3,9,-7,-5,1,-8,2,3,-2,2,10,-9,7,8,-7,-5,5,10,-9,1,-5,-2,-4,-4,7,-8,-10,-1,-1,6,-10,-10,7,7,5,7,-6,6,-3,4,-6,6,-1,3,-7,-4,2,-2,-4,-4,-6,8,9,3,4,-1,-2,-6,-5,7,-10,9,-4,10,9,-8,6,-8,-10,10,-8,4,-9,5,1,-5,4,2,2,-8,7,-5,-4,9,-4,7,9,4,-2,-1,-2,4,8,-5,-8,-1,-1,-8,-9,-8,-8,-9,-6,7,3,-1,-4,-2,-8,5,2,-1,-4,5,-7,-8,-7,2,-9,1,6,-8,6,-5,7,-10,-7,1,1,-5,-10,-3,-10,-2,1,1,-5,10,-9,6,6,-6,-1,6,-2,10,6,10,-8,6,-4,-9,-8,-2,5,-2,8,-5,4,10,-2,9,-6,5,9,-3,8,4,2,-2,8,7,-3,-4,6,2,-6,8,-10,-6,-4,-2,1,-8,-5,-10,-6,8], dtype = "uint16")#candidate|5437|(480,)|const|uint16
call_5435 = relay.TupleGetItem(func_3183_call(relay.reshape(var_5436.astype('uint16'), [80,]), relay.reshape(const_5437.astype('uint16'), [4, 120]), ), 5)
call_5438 = relay.TupleGetItem(func_3187_call(relay.reshape(var_5436.astype('uint16'), [80,]), relay.reshape(const_5437.astype('uint16'), [4, 120]), ), 5)
func_3714_call = mod.get_global_var('func_3714')
func_3715_call = mutated_mod.get_global_var('func_3715')
call_5447 = relay.TupleGetItem(func_3714_call(), 0)
call_5448 = relay.TupleGetItem(func_3715_call(), 0)
output = relay.Tuple([bop_5430,call_5435,var_5436,const_5437,call_5447,])
output2 = relay.Tuple([bop_5433,call_5438,var_5436,const_5437,call_5448,])
func_5453 = relay.Function([var_5436,], output)
mod['func_5453'] = func_5453
mod = relay.transform.InferType()(mod)
var_5454 = relay.var("var_5454", dtype = "uint16", shape = (80, 1))#candidate|5454|(80, 1)|var|uint16
output = func_5453(var_5454)
func_5455 = relay.Function([var_5454], output)
mutated_mod['func_5455'] = func_5455
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2145_call = mod.get_global_var('func_2145')
func_2146_call = mutated_mod.get_global_var('func_2146')
call_5469 = relay.TupleGetItem(func_2145_call(), 0)
call_5470 = relay.TupleGetItem(func_2146_call(), 0)
var_5471 = relay.var("var_5471", dtype = "float64", shape = (3, 8, 9))#candidate|5471|(3, 8, 9)|var|float64
bop_5472 = relay.power(call_5469.astype('float32'), relay.reshape(var_5471.astype('float32'), relay.shape_of(call_5469))) # shape=(3, 8, 9)
bop_5475 = relay.power(call_5470.astype('float32'), relay.reshape(var_5471.astype('float32'), relay.shape_of(call_5470))) # shape=(3, 8, 9)
func_1877_call = mod.get_global_var('func_1877')
func_1879_call = mutated_mod.get_global_var('func_1879')
var_5477 = relay.var("var_5477", dtype = "uint16", shape = (480,))#candidate|5477|(480,)|var|uint16
call_5476 = relay.TupleGetItem(func_1877_call(relay.reshape(var_5477.astype('uint16'), [480,])), 3)
call_5478 = relay.TupleGetItem(func_1879_call(relay.reshape(var_5477.astype('uint16'), [480,])), 3)
bop_5487 = relay.mod(bop_5472.astype('float32'), relay.reshape(call_5469.astype('float32'), relay.shape_of(bop_5472))) # shape=(3, 8, 9)
bop_5490 = relay.mod(bop_5475.astype('float32'), relay.reshape(call_5470.astype('float32'), relay.shape_of(bop_5475))) # shape=(3, 8, 9)
func_2462_call = mod.get_global_var('func_2462')
func_2464_call = mutated_mod.get_global_var('func_2464')
var_5501 = relay.var("var_5501", dtype = "float64", shape = (39,))#candidate|5501|(39,)|var|float64
call_5500 = relay.TupleGetItem(func_2462_call(relay.reshape(var_5501.astype('float64'), [39,])), 0)
call_5502 = relay.TupleGetItem(func_2464_call(relay.reshape(var_5501.astype('float64'), [39,])), 0)
output = relay.Tuple([call_5476,var_5477,bop_5487,call_5500,var_5501,])
output2 = relay.Tuple([call_5478,var_5477,bop_5490,call_5502,var_5501,])
func_5517 = relay.Function([var_5471,var_5477,var_5501,], output)
mod['func_5517'] = func_5517
mod = relay.transform.InferType()(mod)
var_5518 = relay.var("var_5518", dtype = "float64", shape = (3, 8, 9))#candidate|5518|(3, 8, 9)|var|float64
var_5519 = relay.var("var_5519", dtype = "uint16", shape = (480,))#candidate|5519|(480,)|var|uint16
var_5520 = relay.var("var_5520", dtype = "float64", shape = (39,))#candidate|5520|(39,)|var|float64
output = func_5517(var_5518,var_5519,var_5520,)
func_5521 = relay.Function([var_5518,var_5519,var_5520,], output)
mutated_mod['func_5521'] = func_5521
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4739_call = mod.get_global_var('func_4739')
func_4740_call = mutated_mod.get_global_var('func_4740')
call_5529 = relay.TupleGetItem(func_4739_call(), 1)
call_5530 = relay.TupleGetItem(func_4740_call(), 1)
output = relay.Tuple([call_5529,])
output2 = relay.Tuple([call_5530,])
func_5531 = relay.Function([], output)
mod['func_5531'] = func_5531
mod = relay.transform.InferType()(mod)
mutated_mod['func_5531'] = func_5531
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5531_call = mutated_mod.get_global_var('func_5531')
call_5532 = func_5531_call()
output = call_5532
func_5533 = relay.Function([], output)
mutated_mod['func_5533'] = func_5533
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3714_call = mod.get_global_var('func_3714')
func_3715_call = mutated_mod.get_global_var('func_3715')
call_5576 = relay.TupleGetItem(func_3714_call(), 0)
call_5577 = relay.TupleGetItem(func_3715_call(), 0)
var_5611 = relay.var("var_5611", dtype = "float64", shape = (15, 12, 16))#candidate|5611|(15, 12, 16)|var|float64
bop_5612 = relay.bitwise_or(call_5576.astype('int16'), relay.reshape(var_5611.astype('int16'), relay.shape_of(call_5576))) # shape=(15, 12, 16)
bop_5615 = relay.bitwise_or(call_5577.astype('int16'), relay.reshape(var_5611.astype('int16'), relay.shape_of(call_5577))) # shape=(15, 12, 16)
func_2564_call = mod.get_global_var('func_2564')
func_2566_call = mutated_mod.get_global_var('func_2566')
call_5623 = relay.TupleGetItem(func_2564_call(), 0)
call_5624 = relay.TupleGetItem(func_2566_call(), 0)
var_5625 = relay.var("var_5625", dtype = "uint64", shape = (8, 2, 10))#candidate|5625|(8, 2, 10)|var|uint64
bop_5626 = relay.logical_xor(call_5623.astype('uint8'), var_5625.astype('uint8')) # shape=(8, 2, 10)
bop_5629 = relay.logical_xor(call_5624.astype('uint8'), var_5625.astype('uint8')) # shape=(8, 2, 10)
output = relay.Tuple([bop_5612,bop_5626,])
output2 = relay.Tuple([bop_5615,bop_5629,])
func_5638 = relay.Function([var_5611,var_5625,], output)
mod['func_5638'] = func_5638
mod = relay.transform.InferType()(mod)
mutated_mod['func_5638'] = func_5638
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5638_call = mutated_mod.get_global_var('func_5638')
var_5640 = relay.var("var_5640", dtype = "float64", shape = (15, 12, 16))#candidate|5640|(15, 12, 16)|var|float64
var_5641 = relay.var("var_5641", dtype = "uint64", shape = (8, 2, 10))#candidate|5641|(8, 2, 10)|var|uint64
call_5639 = func_5638_call(var_5640,var_5641,)
output = call_5639
func_5642 = relay.Function([var_5640,var_5641,], output)
mutated_mod['func_5642'] = func_5642
mutated_mod = relay.transform.InferType()(mutated_mod)
func_332_call = mod.get_global_var('func_332')
func_333_call = mutated_mod.get_global_var('func_333')
call_5652 = func_332_call()
call_5653 = func_332_call()
output = call_5652
output2 = call_5653
func_5654 = relay.Function([], output)
mod['func_5654'] = func_5654
mod = relay.transform.InferType()(mod)
mutated_mod['func_5654'] = func_5654
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5654_call = mutated_mod.get_global_var('func_5654')
call_5655 = func_5654_call()
output = call_5655
func_5656 = relay.Function([], output)
mutated_mod['func_5656'] = func_5656
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2800_call = mod.get_global_var('func_2800')
func_2802_call = mutated_mod.get_global_var('func_2802')
call_5684 = relay.TupleGetItem(func_2800_call(), 0)
call_5685 = relay.TupleGetItem(func_2802_call(), 0)
output = relay.Tuple([call_5684,])
output2 = relay.Tuple([call_5685,])
func_5689 = relay.Function([], output)
mod['func_5689'] = func_5689
mod = relay.transform.InferType()(mod)
mutated_mod['func_5689'] = func_5689
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5689_call = mutated_mod.get_global_var('func_5689')
call_5690 = func_5689_call()
output = call_5690
func_5691 = relay.Function([], output)
mutated_mod['func_5691'] = func_5691
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5356_call = mod.get_global_var('func_5356')
func_5357_call = mutated_mod.get_global_var('func_5357')
call_5767 = relay.TupleGetItem(func_5356_call(), 0)
call_5768 = relay.TupleGetItem(func_5357_call(), 0)
output = call_5767
output2 = call_5768
func_5774 = relay.Function([], output)
mod['func_5774'] = func_5774
mod = relay.transform.InferType()(mod)
mutated_mod['func_5774'] = func_5774
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5774_call = mutated_mod.get_global_var('func_5774')
call_5775 = func_5774_call()
output = call_5775
func_5776 = relay.Function([], output)
mutated_mod['func_5776'] = func_5776
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5846 = relay.var("var_5846", dtype = "float64", shape = (3, 5, 3))#candidate|5846|(3, 5, 3)|var|float64
const_5847 = relay.const([[[8.118221,2.528643,-2.578463],[5.575892,-2.416973,9.637919],[-6.807101,-1.118169,1.776022],[-9.004742,-7.613641,4.215798],[-4.981456,-3.328622,-2.203756]],[[-7.722413,-4.488916,4.585069],[-2.774497,1.215506,9.502638],[5.352112,-5.733484,-5.741908],[0.859278,4.300364,9.299312],[-7.840957,5.518738,-4.772687]],[[-0.128642,0.371505,-3.913156],[-9.802785,4.019593,-1.706155],[-6.480877,-7.504404,7.738197],[-2.587702,-1.548167,-5.854467],[3.849087,1.101299,7.713619]]], dtype = "float64")#candidate|5847|(3, 5, 3)|const|float64
bop_5848 = relay.mod(var_5846.astype('float64'), relay.reshape(const_5847.astype('float64'), relay.shape_of(var_5846))) # shape=(3, 5, 3)
output = relay.Tuple([bop_5848,])
output2 = relay.Tuple([bop_5848,])
F = relay.Function([var_5846,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_5846,], output2)
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
