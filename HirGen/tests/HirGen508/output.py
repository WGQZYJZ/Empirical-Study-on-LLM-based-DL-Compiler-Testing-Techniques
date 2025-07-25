import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_282 = relay.var("var_282", dtype = "bool", shape = ())#candidate|282|()|var|bool
const_283 = relay.const([[[False,True,False,True,False,True],[False,False,False,False,True,False],[False,False,True,True,False,False],[False,True,True,False,True,True],[False,True,True,False,True,False],[False,True,True,False,True,True],[True,True,True,True,False,False]],[[True,False,False,False,False,False],[True,False,True,False,True,True],[False,True,False,True,True,False],[True,True,True,False,True,False],[True,False,False,False,False,False],[False,True,False,False,False,False],[False,True,True,False,True,False]],[[True,True,True,True,False,True],[True,True,False,True,True,False],[True,False,False,True,False,False],[True,False,False,False,False,False],[False,True,True,True,True,False],[True,False,False,True,True,False],[False,True,False,False,False,True]],[[False,True,False,True,True,False],[True,False,True,True,False,True],[True,True,False,False,False,True],[True,False,True,True,True,True],[True,True,False,True,True,False],[True,False,True,True,True,False],[True,False,True,False,False,True]],[[False,True,False,False,False,True],[False,True,True,True,False,False],[False,True,True,False,True,False],[False,False,False,False,True,True],[False,False,False,True,True,False],[True,True,True,True,True,True],[False,True,False,True,True,False]],[[True,True,False,False,False,True],[True,False,True,True,False,False],[True,True,False,True,False,True],[True,True,False,False,True,False],[False,True,True,False,True,False],[True,False,False,True,True,False],[False,False,False,True,True,True]],[[True,False,False,True,True,False],[True,False,False,True,True,True],[True,True,False,True,True,True],[True,False,False,True,True,True],[True,True,True,False,False,False],[True,True,True,True,True,False],[True,False,True,True,True,False]],[[False,True,True,True,False,False],[False,True,True,False,True,False],[True,False,False,False,False,False],[True,True,False,False,False,True],[False,False,True,True,True,False],[True,False,True,False,True,True],[True,True,True,False,False,False]],[[False,True,False,False,False,True],[True,True,False,True,True,True],[False,True,True,True,True,False],[True,False,False,True,True,True],[False,False,True,True,False,True],[True,False,False,False,True,False],[True,False,True,True,True,False]],[[False,True,False,True,False,True],[False,True,True,False,False,False],[False,True,False,True,False,False],[False,False,True,False,False,False],[True,True,False,False,False,True],[True,True,False,True,False,False],[False,False,True,True,True,False]],[[False,True,True,False,False,True],[True,False,True,False,False,True],[False,True,False,False,False,True],[True,True,False,True,False,False],[True,False,True,False,True,False],[False,True,True,True,False,True],[True,True,True,False,True,True]],[[False,True,True,False,True,True],[True,False,False,True,True,False],[False,False,False,True,False,True],[True,True,True,False,False,True],[True,True,False,False,False,True],[True,False,False,False,False,True],[True,False,True,True,True,False]],[[True,True,False,True,False,False],[True,True,True,False,True,False],[True,False,True,True,False,True],[False,False,True,False,False,False],[True,False,False,False,True,True],[False,True,True,False,False,True],[False,True,True,False,True,False]],[[False,False,True,True,True,True],[True,True,True,False,True,False],[False,False,False,False,False,True],[False,False,False,True,False,True],[False,True,False,True,True,False],[False,True,False,True,False,False],[False,True,True,False,False,True]]], dtype = "bool")#candidate|283|(14, 7, 6)|const|bool
bop_284 = relay.logical_or(var_282.astype('bool'), const_283.astype('bool')) # shape=(14, 7, 6)
uop_296 = relay.log(const_283.astype('float32')) # shape=(14, 7, 6)
output = relay.Tuple([bop_284,uop_296,])
output2 = relay.Tuple([bop_284,uop_296,])
func_300 = relay.Function([var_282,], output)
mod['func_300'] = func_300
mod = relay.transform.InferType()(mod)
mutated_mod['func_300'] = func_300
mutated_mod = relay.transform.InferType()(mutated_mod)
var_301 = relay.var("var_301", dtype = "bool", shape = ())#candidate|301|()|var|bool
func_300_call = mutated_mod.get_global_var('func_300')
call_302 = func_300_call(var_301)
output = call_302
func_303 = relay.Function([var_301], output)
mutated_mod['func_303'] = func_303
mutated_mod = relay.transform.InferType()(mutated_mod)
var_327 = relay.var("var_327", dtype = "uint32", shape = (5, 1, 10))#candidate|327|(5, 1, 10)|var|uint32
var_328 = relay.var("var_328", dtype = "uint32", shape = (5, 5, 10))#candidate|328|(5, 5, 10)|var|uint32
bop_329 = relay.not_equal(var_327.astype('bool'), var_328.astype('bool')) # shape=(5, 5, 10)
output = bop_329
output2 = bop_329
func_340 = relay.Function([var_327,var_328,], output)
mod['func_340'] = func_340
mod = relay.transform.InferType()(mod)
mutated_mod['func_340'] = func_340
mutated_mod = relay.transform.InferType()(mutated_mod)
func_340_call = mutated_mod.get_global_var('func_340')
var_342 = relay.var("var_342", dtype = "uint32", shape = (5, 1, 10))#candidate|342|(5, 1, 10)|var|uint32
var_343 = relay.var("var_343", dtype = "uint32", shape = (5, 5, 10))#candidate|343|(5, 5, 10)|var|uint32
call_341 = func_340_call(var_342,var_343,)
output = call_341
func_344 = relay.Function([var_342,var_343,], output)
mutated_mod['func_344'] = func_344
mutated_mod = relay.transform.InferType()(mutated_mod)
var_586 = relay.var("var_586", dtype = "int16", shape = (16, 1, 7))#candidate|586|(16, 1, 7)|var|int16
var_587 = relay.var("var_587", dtype = "int16", shape = (16, 6, 7))#candidate|587|(16, 6, 7)|var|int16
bop_588 = relay.bitwise_or(var_586.astype('int16'), var_587.astype('int16')) # shape=(16, 6, 7)
output = relay.Tuple([bop_588,])
output2 = relay.Tuple([bop_588,])
func_592 = relay.Function([var_586,var_587,], output)
mod['func_592'] = func_592
mod = relay.transform.InferType()(mod)
var_593 = relay.var("var_593", dtype = "int16", shape = (16, 1, 7))#candidate|593|(16, 1, 7)|var|int16
var_594 = relay.var("var_594", dtype = "int16", shape = (16, 6, 7))#candidate|594|(16, 6, 7)|var|int16
output = func_592(var_593,var_594,)
func_595 = relay.Function([var_593,var_594,], output)
mutated_mod['func_595'] = func_595
mutated_mod = relay.transform.InferType()(mutated_mod)
var_613 = relay.var("var_613", dtype = "bool", shape = (5, 9, 5))#candidate|613|(5, 9, 5)|var|bool
const_614 = relay.const([[[True,True,True,True,False],[False,False,False,True,True],[False,False,True,False,False],[True,False,False,False,False],[True,True,False,False,True],[True,False,False,True,False],[False,False,True,False,True],[False,False,True,False,True],[False,True,True,False,True]],[[False,True,True,False,True],[True,True,False,True,False],[False,False,False,False,True],[False,False,True,False,False],[False,False,True,True,False],[False,False,True,False,False],[False,False,True,False,False],[False,True,False,False,True],[False,False,True,False,False]],[[True,True,True,False,True],[True,True,True,False,False],[True,True,False,True,True],[False,True,True,True,True],[True,True,True,True,False],[False,True,False,True,False],[True,False,True,False,True],[False,True,False,True,False],[False,False,True,True,True]],[[False,True,True,True,True],[False,False,False,True,False],[False,True,True,True,True],[True,False,True,False,False],[False,False,True,False,True],[True,True,False,False,False],[True,False,True,False,True],[False,True,False,True,False],[False,True,False,True,False]],[[True,True,False,False,True],[False,True,False,False,True],[True,True,False,True,False],[False,True,False,False,True],[False,False,False,False,True],[True,False,True,True,True],[True,False,False,False,False],[False,False,True,False,False],[True,True,False,True,True]]], dtype = "bool")#candidate|614|(5, 9, 5)|const|bool
bop_615 = relay.logical_or(var_613.astype('bool'), relay.reshape(const_614.astype('bool'), relay.shape_of(var_613))) # shape=(5, 9, 5)
func_300_call = mod.get_global_var('func_300')
func_303_call = mutated_mod.get_global_var('func_303')
const_623 = relay.const(False, dtype = "bool")#candidate|623|()|const|bool
call_622 = relay.TupleGetItem(func_300_call(relay.reshape(const_623.astype('bool'), [])), 0)
call_624 = relay.TupleGetItem(func_303_call(relay.reshape(const_623.astype('bool'), [])), 0)
uop_626 = relay.log2(const_614.astype('float32')) # shape=(5, 9, 5)
output = relay.Tuple([bop_615,call_622,const_623,uop_626,])
output2 = relay.Tuple([bop_615,call_624,const_623,uop_626,])
func_633 = relay.Function([var_613,], output)
mod['func_633'] = func_633
mod = relay.transform.InferType()(mod)
var_634 = relay.var("var_634", dtype = "bool", shape = (5, 9, 5))#candidate|634|(5, 9, 5)|var|bool
output = func_633(var_634)
func_635 = relay.Function([var_634], output)
mutated_mod['func_635'] = func_635
mutated_mod = relay.transform.InferType()(mutated_mod)
var_741 = relay.var("var_741", dtype = "float32", shape = (4, 3, 8))#candidate|741|(4, 3, 8)|var|float32
var_742 = relay.var("var_742", dtype = "float32", shape = (4, 3, 8))#candidate|742|(4, 3, 8)|var|float32
bop_743 = relay.floor_divide(var_741.astype('float32'), relay.reshape(var_742.astype('float32'), relay.shape_of(var_741))) # shape=(4, 3, 8)
func_300_call = mod.get_global_var('func_300')
func_303_call = mutated_mod.get_global_var('func_303')
var_752 = relay.var("var_752", dtype = "bool", shape = ())#candidate|752|()|var|bool
call_751 = relay.TupleGetItem(func_300_call(relay.reshape(var_752.astype('bool'), [])), 0)
call_753 = relay.TupleGetItem(func_303_call(relay.reshape(var_752.astype('bool'), [])), 0)
uop_760 = relay.rsqrt(call_751.astype('float64')) # shape=(14, 7, 6)
uop_762 = relay.rsqrt(call_753.astype('float64')) # shape=(14, 7, 6)
func_633_call = mod.get_global_var('func_633')
func_635_call = mutated_mod.get_global_var('func_635')
var_770 = relay.var("var_770", dtype = "bool", shape = (225,))#candidate|770|(225,)|var|bool
call_769 = relay.TupleGetItem(func_633_call(relay.reshape(var_770.astype('bool'), [5, 9, 5])), 0)
call_771 = relay.TupleGetItem(func_635_call(relay.reshape(var_770.astype('bool'), [5, 9, 5])), 0)
func_300_call = mod.get_global_var('func_300')
func_303_call = mutated_mod.get_global_var('func_303')
call_785 = relay.TupleGetItem(func_300_call(relay.reshape(var_752.astype('bool'), [])), 0)
call_786 = relay.TupleGetItem(func_303_call(relay.reshape(var_752.astype('bool'), [])), 0)
bop_809 = relay.power(uop_760.astype('float64'), relay.reshape(call_785.astype('float64'), relay.shape_of(uop_760))) # shape=(14, 7, 6)
bop_812 = relay.power(uop_762.astype('float64'), relay.reshape(call_786.astype('float64'), relay.shape_of(uop_762))) # shape=(14, 7, 6)
func_300_call = mod.get_global_var('func_300')
func_303_call = mutated_mod.get_global_var('func_303')
call_816 = relay.TupleGetItem(func_300_call(relay.reshape(var_752.astype('bool'), [])), 0)
call_817 = relay.TupleGetItem(func_303_call(relay.reshape(var_752.astype('bool'), [])), 0)
func_340_call = mod.get_global_var('func_340')
func_344_call = mutated_mod.get_global_var('func_344')
var_832 = relay.var("var_832", dtype = "uint32", shape = (50,))#candidate|832|(50,)|var|uint32
const_833 = relay.const([-10,6,-1,5,-5,6,-2,1,3,-5,6,2,-5,8,-5,-1,-7,-10,-8,-10,10,6,-8,10,-5,-4,5,6,-2,-9,-9,-3,-7,-7,-10,8,10,-3,-3,2,6,-10,5,-10,10,3,2,-8,-10,6,9,-9,-7,1,-3,-9,-10,-1,5,-1,3,-6,9,7,-10,-7,-6,2,-9,5,-6,5,3,3,9,3,-6,-8,7,-4,8,-10,8,-10,-4,10,-9,-8,-1,8,-4,4,4,-5,-1,7,-10,6,8,-8,-2,4,3,2,4,-8,5,-8,-5,-7,2,6,3,-4,9,-3,10,2,1,1,-6,-2,10,9,3,-4,1,8,3,5,4,2,-7,-9,-8,4,7,6,-7,5,-10,4,-8,-7,4,4,2,-2,-10,-9,-9,-6,-10,6,-7,7,9,-1,6,7,-10,8,6,-10,2,7,-2,-10,7,-8,-6,-4,-8,1,2,4,8,5,3,-2,-7,-8,4,-1,-3,-5,-6,3,3,6,1,-9,-3,3,-10,-2,-6,5,-6,8,7,-10,2,7,-7,-1,4,-7,6,4,5,-4,4,-10,8,-4,1,8,-7,-9,7,-3,3,9,-10,-5,6,-7,-1,-5,-4,3,-2,1,5,4,-3,4,-6,5,-3,10,-2,-4,-3,1,7,-5,3,10], dtype = "uint32")#candidate|833|(250,)|const|uint32
call_831 = func_340_call(relay.reshape(var_832.astype('uint32'), [5, 1, 10]), relay.reshape(const_833.astype('uint32'), [5, 5, 10]), )
call_834 = func_340_call(relay.reshape(var_832.astype('uint32'), [5, 1, 10]), relay.reshape(const_833.astype('uint32'), [5, 5, 10]), )
var_838 = relay.var("var_838", dtype = "bool", shape = (14, 7, 6))#candidate|838|(14, 7, 6)|var|bool
bop_839 = relay.multiply(call_751.astype('int16'), relay.reshape(var_838.astype('int16'), relay.shape_of(call_751))) # shape=(14, 7, 6)
bop_842 = relay.multiply(call_753.astype('int16'), relay.reshape(var_838.astype('int16'), relay.shape_of(call_753))) # shape=(14, 7, 6)
output = relay.Tuple([bop_743,var_752,call_769,var_770,bop_809,call_816,call_831,var_832,const_833,bop_839,])
output2 = relay.Tuple([bop_743,var_752,call_771,var_770,bop_812,call_817,call_834,var_832,const_833,bop_842,])
func_849 = relay.Function([var_741,var_742,var_752,var_770,var_832,var_838,], output)
mod['func_849'] = func_849
mod = relay.transform.InferType()(mod)
var_850 = relay.var("var_850", dtype = "float32", shape = (4, 3, 8))#candidate|850|(4, 3, 8)|var|float32
var_851 = relay.var("var_851", dtype = "float32", shape = (4, 3, 8))#candidate|851|(4, 3, 8)|var|float32
var_852 = relay.var("var_852", dtype = "bool", shape = ())#candidate|852|()|var|bool
var_853 = relay.var("var_853", dtype = "bool", shape = (225,))#candidate|853|(225,)|var|bool
var_854 = relay.var("var_854", dtype = "uint32", shape = (50,))#candidate|854|(50,)|var|uint32
var_855 = relay.var("var_855", dtype = "bool", shape = (14, 7, 6))#candidate|855|(14, 7, 6)|var|bool
output = func_849(var_850,var_851,var_852,var_853,var_854,var_855,)
func_856 = relay.Function([var_850,var_851,var_852,var_853,var_854,var_855,], output)
mutated_mod['func_856'] = func_856
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1037 = relay.var("var_1037", dtype = "float32", shape = (16, 2, 15))#candidate|1037|(16, 2, 15)|var|float32
uop_1038 = relay.atanh(var_1037.astype('float32')) # shape=(16, 2, 15)
bop_1055 = relay.equal(uop_1038.astype('bool'), relay.reshape(var_1037.astype('bool'), relay.shape_of(uop_1038))) # shape=(16, 2, 15)
var_1064 = relay.var("var_1064", dtype = "float32", shape = (16, 2, 15))#candidate|1064|(16, 2, 15)|var|float32
bop_1065 = relay.left_shift(var_1037.astype('int8'), relay.reshape(var_1064.astype('int8'), relay.shape_of(var_1037))) # shape=(16, 2, 15)
output = relay.Tuple([bop_1055,bop_1065,])
output2 = relay.Tuple([bop_1055,bop_1065,])
func_1073 = relay.Function([var_1037,var_1064,], output)
mod['func_1073'] = func_1073
mod = relay.transform.InferType()(mod)
mutated_mod['func_1073'] = func_1073
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1073_call = mutated_mod.get_global_var('func_1073')
var_1075 = relay.var("var_1075", dtype = "float32", shape = (16, 2, 15))#candidate|1075|(16, 2, 15)|var|float32
var_1076 = relay.var("var_1076", dtype = "float32", shape = (16, 2, 15))#candidate|1076|(16, 2, 15)|var|float32
call_1074 = func_1073_call(var_1075,var_1076,)
output = call_1074
func_1077 = relay.Function([var_1075,var_1076,], output)
mutated_mod['func_1077'] = func_1077
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1429 = relay.var("var_1429", dtype = "int16", shape = (7, 3, 8))#candidate|1429|(7, 3, 8)|var|int16
var_1430 = relay.var("var_1430", dtype = "int16", shape = (7, 3, 8))#candidate|1430|(7, 3, 8)|var|int16
bop_1431 = relay.multiply(var_1429.astype('int16'), relay.reshape(var_1430.astype('int16'), relay.shape_of(var_1429))) # shape=(7, 3, 8)
output = bop_1431
output2 = bop_1431
func_1440 = relay.Function([var_1429,var_1430,], output)
mod['func_1440'] = func_1440
mod = relay.transform.InferType()(mod)
var_1441 = relay.var("var_1441", dtype = "int16", shape = (7, 3, 8))#candidate|1441|(7, 3, 8)|var|int16
var_1442 = relay.var("var_1442", dtype = "int16", shape = (7, 3, 8))#candidate|1442|(7, 3, 8)|var|int16
output = func_1440(var_1441,var_1442,)
func_1443 = relay.Function([var_1441,var_1442,], output)
mutated_mod['func_1443'] = func_1443
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1619 = relay.var("var_1619", dtype = "uint64", shape = (1, 13))#candidate|1619|(1, 13)|var|uint64
var_1620 = relay.var("var_1620", dtype = "uint64", shape = (1, 13))#candidate|1620|(1, 13)|var|uint64
bop_1621 = relay.left_shift(var_1619.astype('uint64'), relay.reshape(var_1620.astype('uint64'), relay.shape_of(var_1619))) # shape=(1, 13)
output = bop_1621
output2 = bop_1621
func_1627 = relay.Function([var_1619,var_1620,], output)
mod['func_1627'] = func_1627
mod = relay.transform.InferType()(mod)
var_1628 = relay.var("var_1628", dtype = "uint64", shape = (1, 13))#candidate|1628|(1, 13)|var|uint64
var_1629 = relay.var("var_1629", dtype = "uint64", shape = (1, 13))#candidate|1629|(1, 13)|var|uint64
output = func_1627(var_1628,var_1629,)
func_1630 = relay.Function([var_1628,var_1629,], output)
mutated_mod['func_1630'] = func_1630
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1715 = relay.var("var_1715", dtype = "float64", shape = (9, 3, 3))#candidate|1715|(9, 3, 3)|var|float64
uop_1716 = relay.tan(var_1715.astype('float64')) # shape=(9, 3, 3)
func_592_call = mod.get_global_var('func_592')
func_595_call = mutated_mod.get_global_var('func_595')
var_1724 = relay.var("var_1724", dtype = "int16", shape = (112,))#candidate|1724|(112,)|var|int16
const_1725 = relay.const([7,6,2,6,6,-4,3,2,8,1,6,-7,1,-7,10,3,-10,7,-3,-10,3,5,3,-1,9,10,-3,6,-10,-4,-7,-10,-7,8,2,-1,3,2,-3,-8,6,-8,4,-6,6,-9,-4,-1,5,-3,7,-3,-9,-6,-7,-5,-2,-5,-6,3,8,7,8,-5,7,-2,-9,7,-10,-10,-7,2,-7,-8,-8,7,10,8,-1,-2,10,-5,1,-8,-6,7,-5,-5,-6,5,1,-9,-7,-10,1,-9,8,-3,9,-9,2,-8,-5,-9,-7,6,-8,10,2,-6,-4,6,-2,-2,-10,5,6,-9,8,3,-4,-3,6,2,5,-2,6,10,5,-8,-2,-9,6,-9,-9,10,-5,-8,8,8,-9,-2,-6,-2,4,-10,-2,-5,8,-3,-8,10,9,4,-9,1,-1,-2,5,10,1,8,-8,2,-6,-2,-9,10,2,5,4,-1,1,4,7,-7,-3,-2,7,8,2,-8,2,-10,1,10,-3,2,4,2,-9,10,6,-4,9,-4,2,1,-1,-2,6,8,5,-3,-4,-10,6,9,-3,4,-7,-10,-2,6,-10,6,2,-5,-1,-6,3,-2,-6,-2,-5,1,-5,-2,-4,2,9,-9,-1,-8,3,1,-9,-9,-5,-6,-5,4,-1,-1,-7,6,1,8,2,-8,9,-2,-4,5,-2,-10,1,-9,2,-5,2,-6,-1,-7,-10,7,-4,-10,-10,6,10,-8,-3,3,-6,-4,-4,-1,7,-7,3,-8,2,3,-5,-5,8,7,-10,-5,-3,-7,3,1,6,-7,-9,-3,-3,5,5,4,-3,3,5,4,-10,4,-8,3,10,-10,5,2,-10,-5,-8,10,-3,-9,-4,-6,-3,-10,-3,3,-5,4,8,5,2,-5,-2,-4,-8,5,7,8,2,-8,-1,10,-8,3,10,-4,-1,-5,-5,-9,-5,7,-6,9,-1,6,-2,9,1,-3,-1,5,9,-6,-10,-7,9,-6,-9,6,-4,5,9,3,5,2,7,9,-7,10,1,-4,-3,7,5,-5,6,-2,-3,6,3,5,5,-5,10,2,3,4,-4,10,-6,6,-3,10,5,4,-6,-9,-5,-3,-2,-8,9,-10,5,-2,-3,5,-9,3,-1,-6,-8,-5,-1,-7,3,7,9,7,-7,3,7,9,-2,-10,1,-9,-10,9,-7,6,4,-4,-1,7,9,-2,-9,-2,5,-6,-7,3,-1,1,-1,-8,10,-9,2,-1,-5,7,5,-7,-1,-5,7,-8,-2,-6,5,9,-7,-8,-4,10,-3,-5,6,9,2,8,3,10,6,-8,4,-6,-6,10,3,-1,-10,-5,6,-6,9,10,9,-9,9,-5,7,-2,8,-4,3,-9,10,9,-9,6,10,-2,-9,-3,-10,-9,-4,1,4,-4,1,-10,-7,-8,-6,8,4,5,3,-2,-10,10,-2,5,6,-5,-3,9,5,-10,-4,7,8,-3,-3,2,6,7,-4,-5,4,-7,-4,8,-4,10,-7,-7,-2,6,5,-1,1,-8,2,3,-3,4,-7,-7,-3,2,-6,4,9,-5,9,5,4,3,7,4,8,-7,4,-9,-1,-6,-10,-6,2,7,-9,-1,6,-1,-2,4,6,-9,5,5,9,-2,-6,1,-4,-9,-1,-6,-4,3,-3,-8,-8,7,-4,-9,8,5,-2,1,-5,8,1,-6,-8,-3,-5,10,-7,-7,3,-6,-7,-4,7,6,-8,-9,-6,-5,3,-7,-8,-4,-6,-6,8,10,10,6,-9,-9,-5,-5,-5,-7,-8,-9,-5,-9,-7,-2,6,-10,-3,-4], dtype = "int16")#candidate|1725|(672,)|const|int16
call_1723 = relay.TupleGetItem(func_592_call(relay.reshape(var_1724.astype('int16'), [16, 1, 7]), relay.reshape(const_1725.astype('int16'), [16, 6, 7]), ), 0)
call_1726 = relay.TupleGetItem(func_595_call(relay.reshape(var_1724.astype('int16'), [16, 1, 7]), relay.reshape(const_1725.astype('int16'), [16, 6, 7]), ), 0)
func_300_call = mod.get_global_var('func_300')
func_303_call = mutated_mod.get_global_var('func_303')
var_1740 = relay.var("var_1740", dtype = "bool", shape = ())#candidate|1740|()|var|bool
call_1739 = relay.TupleGetItem(func_300_call(relay.reshape(var_1740.astype('bool'), [])), 0)
call_1741 = relay.TupleGetItem(func_303_call(relay.reshape(var_1740.astype('bool'), [])), 0)
output = relay.Tuple([uop_1716,call_1723,var_1724,const_1725,call_1739,var_1740,])
output2 = relay.Tuple([uop_1716,call_1726,var_1724,const_1725,call_1741,var_1740,])
func_1747 = relay.Function([var_1715,var_1724,var_1740,], output)
mod['func_1747'] = func_1747
mod = relay.transform.InferType()(mod)
mutated_mod['func_1747'] = func_1747
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1747_call = mutated_mod.get_global_var('func_1747')
var_1749 = relay.var("var_1749", dtype = "float64", shape = (9, 3, 3))#candidate|1749|(9, 3, 3)|var|float64
var_1750 = relay.var("var_1750", dtype = "int16", shape = (112,))#candidate|1750|(112,)|var|int16
var_1751 = relay.var("var_1751", dtype = "bool", shape = ())#candidate|1751|()|var|bool
call_1748 = func_1747_call(var_1749,var_1750,var_1751,)
output = call_1748
func_1752 = relay.Function([var_1749,var_1750,var_1751,], output)
mutated_mod['func_1752'] = func_1752
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1852 = relay.var("var_1852", dtype = "float64", shape = (3, 16, 8))#candidate|1852|(3, 16, 8)|var|float64
var_1853 = relay.var("var_1853", dtype = "float64", shape = (3, 16, 8))#candidate|1853|(3, 16, 8)|var|float64
bop_1854 = relay.mod(var_1852.astype('float64'), relay.reshape(var_1853.astype('float64'), relay.shape_of(var_1852))) # shape=(3, 16, 8)
func_1627_call = mod.get_global_var('func_1627')
func_1630_call = mutated_mod.get_global_var('func_1630')
const_1859 = relay.const([-1,7,-10,9,-10,3,5,6,-5,-5,-4,-8,-4], dtype = "uint64")#candidate|1859|(13,)|const|uint64
call_1858 = func_1627_call(relay.reshape(const_1859.astype('uint64'), [1, 13]), relay.reshape(const_1859.astype('uint64'), [1, 13]), )
call_1860 = func_1627_call(relay.reshape(const_1859.astype('uint64'), [1, 13]), relay.reshape(const_1859.astype('uint64'), [1, 13]), )
func_849_call = mod.get_global_var('func_849')
func_856_call = mutated_mod.get_global_var('func_856')
var_1868 = relay.var("var_1868", dtype = "float32", shape = (96,))#candidate|1868|(96,)|var|float32
var_1869 = relay.var("var_1869", dtype = "bool", shape = ())#candidate|1869|()|var|bool
const_1870 = relay.const([True,True,True,False,False,False,False,False,False,False,True,True,False,False,False,True,True,True,False,True,False,True,True,False,False,False,True,True,True,False,True,False,True,False,False,True,True,False,True,True,False,False,True,False,False,True,False,False,True,False,True,True,True,False,False,False,False,True,True,True,True,True,True,False,True,True,True,False,True,False,False,True,False,True,False,True,False,False,True,True,False,False,True,False,True,True,False,True,False,True,True,False,False,False,False,False,False,False,False,True,False,False,True,True,True,True,False,False,True,True,True,True,True,False,True,False,True,True,False,False,True,True,False,True,True,False,True,True,False,False,True,True,False,False,False,False,True,False,False,False,True,True,True,False,False,True,True,True,False,True,True,True,False,True,True,True,False,False,True,False,False,False,True,True,False,True,True,True,True,True,True,False,False,False,True,False,True,False,False,False,True,True,True,True,True,False,False,True,True,True,True,True,True,True,False,True,False,True,False,False,False,True,False,True,False,True,True,True,True,True,True,False,True,True,True,False,True,False,True,False,True,False,False,True,True], dtype = "bool")#candidate|1870|(225,)|const|bool
const_1871 = relay.const([9,8,9,-7,1,8,6,8,8,-8,-3,5,-4,9,-1,5,-6,-5,-1,4,6,5,7,3,5,4,8,6,-4,-3,-1,-5,3,2,2,6,-7,10,-6,9,4,-3,-5,-4,6,-5,6,-4,10,5], dtype = "uint32")#candidate|1871|(50,)|const|uint32
const_1872 = relay.const([[False,False,False,False,False,True,True,False,True,True,False,False,True,False,True,False,True,True,False,False,False,True,True,False,False,True,False,False,True,True,True,True,True,True,False,True,True,True,True,False,False,False,False,True,False,True,True,True,True,True,True,True,False,True,True,False,False,True,True,False,False,False,True,False,False,True,True,True,False,True,True,False,True,True,True,True,False,False,False,True,False,True,True,False],[False,False,True,True,False,False,True,False,False,False,False,False,False,False,True,False,True,False,True,False,True,False,True,False,True,True,True,True,False,False,True,True,True,False,False,True,False,True,True,True,True,False,True,True,False,True,False,True,True,True,True,True,True,False,True,False,True,False,True,True,True,True,False,False,True,False,True,False,True,False,True,True,False,False,False,False,True,False,True,True,True,False,False,True],[False,True,True,True,True,True,True,False,False,True,False,True,False,True,True,True,False,False,False,False,True,True,True,False,True,False,True,True,True,True,False,True,False,True,True,False,False,False,False,False,True,True,False,True,False,True,True,False,False,True,True,True,False,False,True,False,False,True,True,True,False,True,True,True,False,False,True,True,False,True,True,True,False,True,True,True,True,False,True,True,True,False,False,False],[False,True,False,True,False,True,False,True,False,True,False,False,True,True,True,True,False,True,True,True,False,False,False,True,False,True,False,True,False,False,True,False,False,True,True,False,False,False,True,False,True,True,True,True,False,False,False,True,True,True,False,False,True,False,True,True,True,False,True,True,False,False,False,False,False,True,True,False,True,False,True,True,False,False,False,False,False,False,True,False,False,True,False,True],[True,True,True,True,True,False,False,False,False,False,False,False,False,True,True,True,False,False,False,False,False,False,False,False,True,False,False,True,True,False,False,True,False,True,False,True,True,False,True,False,True,False,False,True,True,True,False,True,True,True,True,True,True,False,False,False,False,False,True,True,True,False,False,True,True,False,False,True,True,False,True,False,False,True,True,True,True,True,True,False,False,False,False,False],[False,False,False,False,False,False,False,True,False,False,False,True,True,True,False,False,True,True,False,True,True,True,False,False,False,True,False,True,False,False,True,False,False,True,True,True,True,True,False,True,True,True,True,False,False,True,False,True,True,False,False,False,True,False,False,False,False,False,True,False,True,False,False,True,True,True,False,True,False,True,False,False,False,True,False,False,True,True,True,False,True,True,False,True],[True,False,True,True,False,False,True,True,False,False,True,True,True,True,False,False,False,True,False,False,False,False,False,True,True,True,True,True,False,True,False,False,True,True,True,False,True,True,True,True,True,False,False,False,False,True,False,False,False,False,True,False,True,True,False,False,True,True,True,True,True,True,True,False,False,True,False,True,False,False,False,True,False,True,True,False,False,False,True,False,False,False,False,True]], dtype = "bool")#candidate|1872|(7, 84)|const|bool
call_1867 = relay.TupleGetItem(func_849_call(relay.reshape(var_1868.astype('float32'), [4, 3, 8]), relay.reshape(var_1868.astype('float32'), [4, 3, 8]), relay.reshape(var_1869.astype('bool'), []), relay.reshape(const_1870.astype('bool'), [225,]), relay.reshape(const_1871.astype('uint32'), [50,]), relay.reshape(const_1872.astype('bool'), [14, 7, 6]), ), 1)
call_1873 = relay.TupleGetItem(func_856_call(relay.reshape(var_1868.astype('float32'), [4, 3, 8]), relay.reshape(var_1868.astype('float32'), [4, 3, 8]), relay.reshape(var_1869.astype('bool'), []), relay.reshape(const_1870.astype('bool'), [225,]), relay.reshape(const_1871.astype('uint32'), [50,]), relay.reshape(const_1872.astype('bool'), [14, 7, 6]), ), 1)
output = relay.Tuple([bop_1854,call_1858,const_1859,call_1867,var_1868,var_1869,const_1870,const_1871,const_1872,])
output2 = relay.Tuple([bop_1854,call_1860,const_1859,call_1873,var_1868,var_1869,const_1870,const_1871,const_1872,])
func_1876 = relay.Function([var_1852,var_1853,var_1868,var_1869,], output)
mod['func_1876'] = func_1876
mod = relay.transform.InferType()(mod)
var_1877 = relay.var("var_1877", dtype = "float64", shape = (3, 16, 8))#candidate|1877|(3, 16, 8)|var|float64
var_1878 = relay.var("var_1878", dtype = "float64", shape = (3, 16, 8))#candidate|1878|(3, 16, 8)|var|float64
var_1879 = relay.var("var_1879", dtype = "float32", shape = (96,))#candidate|1879|(96,)|var|float32
var_1880 = relay.var("var_1880", dtype = "bool", shape = ())#candidate|1880|()|var|bool
output = func_1876(var_1877,var_1878,var_1879,var_1880,)
func_1881 = relay.Function([var_1877,var_1878,var_1879,var_1880,], output)
mutated_mod['func_1881'] = func_1881
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2194 = relay.const([[[-2,2],[4,-3]],[[-1,2],[-5,-7]],[[4,-1],[7,7]],[[-9,-4],[5,-8]],[[3,-6],[-1,-4]],[[2,-4],[8,-2]],[[-3,1],[1,7]],[[1,10],[5,1]],[[-7,-5],[-8,1]],[[-4,-8],[6,7]],[[3,9],[-5,5]],[[-8,-10],[-4,-9]],[[1,-9],[4,8]],[[-7,-10],[-8,-4]]], dtype = "int32")#candidate|2194|(14, 2, 2)|const|int32
var_2195 = relay.var("var_2195", dtype = "int32", shape = (14, 2, 2))#candidate|2195|(14, 2, 2)|var|int32
bop_2196 = relay.less_equal(const_2194.astype('bool'), relay.reshape(var_2195.astype('bool'), relay.shape_of(const_2194))) # shape=(14, 2, 2)
output = relay.Tuple([bop_2196,])
output2 = relay.Tuple([bop_2196,])
func_2207 = relay.Function([var_2195,], output)
mod['func_2207'] = func_2207
mod = relay.transform.InferType()(mod)
var_2208 = relay.var("var_2208", dtype = "int32", shape = (14, 2, 2))#candidate|2208|(14, 2, 2)|var|int32
output = func_2207(var_2208)
func_2209 = relay.Function([var_2208], output)
mutated_mod['func_2209'] = func_2209
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2707 = relay.var("var_2707", dtype = "float64", shape = (4, 5, 10))#candidate|2707|(4, 5, 10)|var|float64
uop_2708 = relay.sin(var_2707.astype('float64')) # shape=(4, 5, 10)
output = uop_2708
output2 = uop_2708
func_2728 = relay.Function([var_2707,], output)
mod['func_2728'] = func_2728
mod = relay.transform.InferType()(mod)
var_2729 = relay.var("var_2729", dtype = "float64", shape = (4, 5, 10))#candidate|2729|(4, 5, 10)|var|float64
output = func_2728(var_2729)
func_2730 = relay.Function([var_2729], output)
mutated_mod['func_2730'] = func_2730
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2891 = relay.var("var_2891", dtype = "float32", shape = (6, 14, 12))#candidate|2891|(6, 14, 12)|var|float32
uop_2892 = relay.cos(var_2891.astype('float32')) # shape=(6, 14, 12)
output = uop_2892
output2 = uop_2892
func_2920 = relay.Function([var_2891,], output)
mod['func_2920'] = func_2920
mod = relay.transform.InferType()(mod)
var_2921 = relay.var("var_2921", dtype = "float32", shape = (6, 14, 12))#candidate|2921|(6, 14, 12)|var|float32
output = func_2920(var_2921)
func_2922 = relay.Function([var_2921], output)
mutated_mod['func_2922'] = func_2922
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3081 = relay.var("var_3081", dtype = "float64", shape = (13, 7, 16))#candidate|3081|(13, 7, 16)|var|float64
uop_3082 = relay.tan(var_3081.astype('float64')) # shape=(13, 7, 16)
output = relay.Tuple([uop_3082,])
output2 = relay.Tuple([uop_3082,])
func_3090 = relay.Function([var_3081,], output)
mod['func_3090'] = func_3090
mod = relay.transform.InferType()(mod)
mutated_mod['func_3090'] = func_3090
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3091 = relay.var("var_3091", dtype = "float64", shape = (13, 7, 16))#candidate|3091|(13, 7, 16)|var|float64
func_3090_call = mutated_mod.get_global_var('func_3090')
call_3092 = func_3090_call(var_3091)
output = call_3092
func_3093 = relay.Function([var_3091], output)
mutated_mod['func_3093'] = func_3093
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3377 = relay.const([[[-2,9,-5,-10,-8,5,-7],[-6,-5,3,-1,-1,6,-3],[7,2,-3,9,3,-2,-10],[-5,-8,-5,-5,2,-5,10],[-8,6,5,7,7,5,-5]],[[3,3,-2,2,5,-8,-1],[9,4,2,-5,8,-6,-5],[-6,-7,-8,8,-1,-9,-6],[-1,-2,8,-10,-4,9,4],[-8,6,1,-5,-4,-9,3]],[[-1,-9,-8,3,-4,10,7],[-1,-7,-1,-5,8,1,10],[7,10,-4,10,-7,-10,7],[3,7,6,5,9,-8,-7],[-9,9,-2,-5,7,6,2]],[[8,-6,-5,7,9,7,-1],[2,-5,6,-8,4,-5,-1],[-6,-9,-4,5,7,1,5],[1,4,-5,6,-5,-2,-10],[-10,9,5,2,2,9,9]],[[-5,-9,-10,2,5,9,-4],[9,-7,6,6,-4,1,6],[-3,-1,9,5,-6,-7,4],[-1,4,-4,-8,6,2,-2],[4,-4,-3,5,8,3,8]],[[-4,-3,-3,-4,9,7,-8],[5,-3,-8,-6,-3,-4,5],[-4,-7,-7,3,9,-9,1],[-4,-7,1,-8,7,1,-6],[-1,-2,4,-5,-10,-3,8]],[[-9,-9,8,-2,6,-9,3],[-4,-6,-2,2,-8,8,-5],[-8,2,2,10,7,-10,-1],[7,8,3,-8,2,10,7],[1,9,-5,-9,-2,6,1]],[[2,4,6,-1,-5,5,-1],[1,-4,-9,2,-6,2,1],[7,3,-4,1,8,10,-2],[-3,1,-10,6,8,5,10],[1,-7,-3,-10,-7,10,4]],[[1,6,-9,-7,2,10,3],[3,5,7,2,2,1,-4],[5,1,-4,-9,4,5,1],[-5,3,10,-9,1,10,-5],[3,10,-5,-3,9,-5,-7]],[[-8,-6,-5,-10,8,-3,-3],[2,-2,5,-2,-4,-1,-6],[6,7,-4,-7,-3,-3,8],[-9,10,7,8,-5,-4,7],[4,4,-9,-3,3,1,9]],[[-6,-1,-8,-6,-5,8,-7],[1,-8,7,4,-2,-2,-9],[2,8,-6,2,-2,-8,-5],[8,-9,-3,-3,-10,10,-6],[-8,5,6,7,-4,6,9]],[[4,-2,-3,-1,-1,-1,-3],[-4,3,-5,-3,4,3,-9],[6,2,-2,-10,7,-3,6],[-9,5,8,-7,-8,4,-10],[-8,3,-9,-3,1,-5,-7]],[[-9,2,-1,-3,-5,-4,1],[-5,-4,-10,-8,-3,-9,4],[-5,2,-3,-3,-1,5,-5],[1,8,6,8,10,6,-6],[-10,-1,-1,-10,-7,-1,7]],[[6,-7,-9,2,7,-3,7],[10,6,-4,-8,10,-1,1],[5,2,-2,-10,-3,8,4],[9,-3,-5,-1,-6,5,-7],[2,8,7,-1,-8,2,5]],[[5,3,3,3,5,-8,-4],[-10,7,10,1,7,6,5],[1,10,-1,10,-9,3,-8],[8,4,-3,-7,-10,8,-2],[-7,4,7,3,-7,4,-5]],[[-1,-10,5,4,-4,-8,-1],[4,-3,-8,-8,-3,5,-6],[-5,5,-6,-2,8,-6,8],[9,-10,-1,-3,-10,-8,-5],[-2,-1,2,2,3,-8,1]]], dtype = "uint32")#candidate|3377|(16, 5, 7)|const|uint32
const_3378 = relay.const([[[8,-3,-9,-8,-2,3,-9],[-8,7,-2,-10,-7,2,-7],[3,8,10,-8,-10,-1,-9],[4,1,-6,2,5,-6,-3],[6,1,-2,3,-2,-2,-9]],[[3,-9,-3,-1,-9,8,-8],[-8,-5,5,-6,-6,-10,9],[-9,6,6,10,-6,-10,-7],[10,-5,8,-7,-7,-1,-3],[3,2,-10,-5,6,6,8]],[[6,6,-1,-8,-2,-4,-9],[4,-6,2,1,8,10,9],[5,-4,3,1,-1,-4,6],[-4,3,-5,-6,-8,-2,-1],[2,8,7,2,-10,-5,2]],[[3,-9,2,-4,-2,-5,7],[9,-8,8,-2,-8,7,5],[-10,-1,-6,-10,2,-3,-6],[7,6,9,-10,-1,-4,-5],[10,4,9,-3,-6,3,-8]],[[-6,-7,-6,-10,-8,-4,3],[2,10,9,2,-9,-5,7],[-7,-6,-9,-8,7,-10,10],[-6,3,-2,9,-8,1,5],[6,-8,9,8,7,1,-3]],[[9,-6,-6,-2,-3,-2,-2],[-8,-1,-1,7,-2,-7,10],[5,10,9,-10,6,-3,-2],[8,8,-3,2,9,-3,4],[-4,-8,10,-2,4,3,-5]],[[-9,-3,-3,4,-1,1,6],[3,-5,-6,5,-1,-4,10],[-6,-6,-1,1,10,-3,4],[3,9,-9,4,-7,1,7],[-6,-3,-1,7,-7,-10,-8]],[[8,-7,9,6,8,5,-8],[-5,2,-9,4,-5,3,-1],[-7,-6,-8,-3,-6,-7,8],[2,-8,8,-8,6,-10,-5],[1,8,7,-2,-6,4,-5]],[[-8,4,-10,9,-2,-8,1],[7,10,3,7,-3,-5,-7],[3,-1,-6,3,7,3,-8],[-8,-6,-6,7,6,9,5],[8,-4,-4,2,-10,-4,-6]],[[8,8,3,-3,4,-8,3],[10,1,10,1,-10,3,-9],[-9,-6,8,-3,9,2,5],[4,5,-6,5,2,9,2],[-4,-9,-5,1,8,-6,1]],[[2,6,-4,1,-9,-5,4],[-5,-5,7,-3,8,6,10],[-5,-10,5,-5,10,10,-4],[-2,-8,-7,7,9,-6,6],[7,6,4,-10,-5,-9,-1]],[[-4,-3,-7,7,-8,-8,6],[5,10,5,5,3,8,10],[-2,-6,10,-5,2,1,-8],[-6,4,4,5,-1,9,-8],[3,6,-3,-2,-4,9,2]],[[-6,10,-3,-7,-8,6,-5],[-3,-2,4,-2,10,9,-4],[10,10,-4,-1,-5,-4,1],[4,5,-2,6,4,-1,3],[-6,2,-2,-3,-5,5,-1]],[[4,-1,1,-8,2,6,-1],[8,-1,-10,10,7,8,8],[-1,4,-2,-6,8,5,-5],[6,10,-9,-10,-5,-10,-6],[2,4,2,1,-3,-6,-10]],[[-3,-3,-10,-4,-5,-9,-7],[-3,-9,-6,10,-3,3,-9],[-6,-1,1,-9,9,1,10],[-4,-9,1,-4,5,6,-7],[3,-9,3,10,-5,7,2]],[[8,8,-10,-9,-6,-7,-6],[-8,-3,7,10,3,-5,8],[-10,10,4,-10,-6,7,-3],[-3,-9,-2,-10,4,10,-1],[-6,7,-9,6,4,10,-6]]], dtype = "uint32")#candidate|3378|(16, 5, 7)|const|uint32
bop_3379 = relay.greater_equal(const_3377.astype('bool'), relay.reshape(const_3378.astype('bool'), relay.shape_of(const_3377))) # shape=(16, 5, 7)
uop_3393 = relay.tan(const_3378.astype('float32')) # shape=(16, 5, 7)
uop_3402 = relay.sigmoid(uop_3393.astype('float64')) # shape=(16, 5, 7)
func_592_call = mod.get_global_var('func_592')
func_595_call = mutated_mod.get_global_var('func_595')
const_3417 = relay.const([-3,-1,-10,-6,-1,4,2,8,-4,-5,-5,4,-1,-2,-4,4,-5,-8,7,-1,9,-6,1,-2,-5,5,-3,-4,1,9,-8,-5,-7,7,9,10,-5,10,-10,-4,7,-5,-10,5,6,9,6,-8,-8,-6,-4,4,-3,-7,5,10,-3,-4,-7,-4,-2,8,6,-2,-10,9,5,3,-8,-4,4,-6,-10,-7,9,9,-4,-3,2,3,6,-6,-7,-10,1,-9,8,1,-8,-5,2,2,1,-6,-3,-7,-3,9,-9,-7,2,5,-3,-10,-5,-10,8,-2,-9,4,-9,8], dtype = "int16")#candidate|3417|(112,)|const|int16
const_3418 = relay.const([[1,-2,-1,7,-3,-10,10,5,-3,-8,6,5,-6,-6,-8,3,-2,-2,-4,-5,-5,-1,-1,10,-7,-4,6,10,-6,-3,3,-6,1,-8,-9,1,9,7,-2,-1,5,2,7,-5,10,-9,-2,-10,3,7,2,-3,3,9,7,2,5,5,-8,7,8,3,-1,4,-2,5,10,2,-6,-9,-3,6,7,-2,-10,2,-4,-10,7,-8,-5,-2,-1,-10,-7,1,-2,-10,8,3,-10,8,2,-9,-9,10,2,-1,-6,1,10,5,-8,-10,-4,4,9,-8,-9,-2,7,-6,-1,1,8,5,5,9,-5,-10,5,5,-8,-5,-1,7,6,-7,10,8,-2,-5,3,10,6,-6,-6,5,3,2,6,2,-5,-2,-6,3,1,3,-6,1,3,-5,8,2,9,-7,-5,8,7,5,10,9,9,-7,-5,1,8,6,3,9,-1,-8,7,-8,-7,8,-4,1,1,10,-8,5,-6,-4,-8,-2,1,-9,7,-3,-10,-4,-9,10,4,-7,3,-10,2,8,9,1,10,-8,-7,1,-1,-4,9,2,5,10,1,7,-6,-5,4,2,-8,-1,3,-4,9,7,-5,-3,-8,8,-3,-3,7,3,-6,5,5,-10,-10,-3,6,6,8,-2,2,-6,-3,5,8,1,-3,9,4,8,-8,10,-2,-5,-6,5,-5,5,1,-7,-8,-5,7,-10,-5,-3,-9,9,1,-10,-3,7,7,7,3,-6,-4,-1,7,2,-8,-7,1,-8,1,1,6,-1,1,-2,-4,3,-1,1,-6,10,-1,2,-2,-6,10,-9,7,-9,10,1,10,-3,10,7,-8,-3,3,-3,-6,1,8,2,10,2,-3,-3,10,-3,10,8,8,-1,7,-9,-2,-10,-10,6],[8,-9,4,5,8,4,-10,7,6,-3,1,9,-4,-6,5,-4,1,-1,7,-8,-6,2,7,-7,9,-9,4,6,8,4,-3,4,4,-10,3,-6,10,-6,9,-3,3,-7,-9,7,-4,-1,-1,-4,10,8,9,2,-1,-10,2,-7,5,-2,-8,4,-1,-10,7,9,-7,1,-8,7,3,-10,-1,10,10,2,2,-1,-8,7,-6,-5,1,8,10,1,-5,8,7,-1,9,-4,-9,6,-5,-5,7,-3,-7,-2,-8,-2,-3,6,8,6,1,10,4,-9,7,9,5,4,2,-1,-8,-1,3,10,7,1,-5,-9,-7,7,2,1,7,9,3,10,-5,4,-8,-1,2,2,3,6,10,7,1,-1,-5,-8,2,-10,8,-5,10,-1,8,-10,5,-4,-1,-8,8,1,-10,2,6,9,7,10,9,-10,5,9,-7,-6,3,1,1,-5,-2,5,8,-1,7,4,3,5,7,-9,-7,5,6,1,7,-10,-4,6,-8,-9,-10,-3,1,10,-3,2,-3,2,-2,-9,-3,-7,-4,9,2,9,2,-5,-1,1,-6,-6,8,8,-2,-1,4,2,-3,-1,2,8,-1,7,8,6,10,2,-1,-10,-7,-10,10,-10,4,9,1,-9,8,4,5,1,3,7,-4,-9,-7,4,2,10,5,-1,5,-9,-8,-1,5,2,7,-4,-6,4,1,-3,-3,-8,-2,-7,10,4,-10,-5,-8,3,-4,-8,9,6,-1,-4,3,5,2,4,5,-4,-2,-10,-3,8,1,10,10,-1,-6,-7,8,4,-1,3,-8,-3,-3,-3,-7,8,8,9,5,-1,4,1,2,-1,6,3,1,4,-10,-4,9,6,-9,5,2,8,8,7,7,-4,-3,6]], dtype = "int16")#candidate|3418|(2, 336)|const|int16
call_3416 = relay.TupleGetItem(func_592_call(relay.reshape(const_3417.astype('int16'), [16, 1, 7]), relay.reshape(const_3418.astype('int16'), [16, 6, 7]), ), 0)
call_3419 = relay.TupleGetItem(func_595_call(relay.reshape(const_3417.astype('int16'), [16, 1, 7]), relay.reshape(const_3418.astype('int16'), [16, 6, 7]), ), 0)
output = relay.Tuple([bop_3379,uop_3402,call_3416,const_3417,const_3418,])
output2 = relay.Tuple([bop_3379,uop_3402,call_3419,const_3417,const_3418,])
func_3426 = relay.Function([], output)
mod['func_3426'] = func_3426
mod = relay.transform.InferType()(mod)
mutated_mod['func_3426'] = func_3426
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3426_call = mutated_mod.get_global_var('func_3426')
call_3427 = func_3426_call()
output = call_3427
func_3428 = relay.Function([], output)
mutated_mod['func_3428'] = func_3428
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3429 = relay.var("var_3429", dtype = "int16", shape = (3, 9, 16))#candidate|3429|(3, 9, 16)|var|int16
var_3430 = relay.var("var_3430", dtype = "int16", shape = (3, 9, 16))#candidate|3430|(3, 9, 16)|var|int16
bop_3431 = relay.left_shift(var_3429.astype('int16'), relay.reshape(var_3430.astype('int16'), relay.shape_of(var_3429))) # shape=(3, 9, 16)
func_3426_call = mod.get_global_var('func_3426')
func_3428_call = mutated_mod.get_global_var('func_3428')
call_3443 = relay.TupleGetItem(func_3426_call(), 4)
call_3444 = relay.TupleGetItem(func_3428_call(), 4)
output = relay.Tuple([bop_3431,call_3443,])
output2 = relay.Tuple([bop_3431,call_3444,])
func_3450 = relay.Function([var_3429,var_3430,], output)
mod['func_3450'] = func_3450
mod = relay.transform.InferType()(mod)
var_3451 = relay.var("var_3451", dtype = "int16", shape = (3, 9, 16))#candidate|3451|(3, 9, 16)|var|int16
var_3452 = relay.var("var_3452", dtype = "int16", shape = (3, 9, 16))#candidate|3452|(3, 9, 16)|var|int16
output = func_3450(var_3451,var_3452,)
func_3453 = relay.Function([var_3451,var_3452,], output)
mutated_mod['func_3453'] = func_3453
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3426_call = mod.get_global_var('func_3426')
func_3428_call = mutated_mod.get_global_var('func_3428')
call_3462 = relay.TupleGetItem(func_3426_call(), 0)
call_3463 = relay.TupleGetItem(func_3428_call(), 0)
output = call_3462
output2 = call_3463
func_3479 = relay.Function([], output)
mod['func_3479'] = func_3479
mod = relay.transform.InferType()(mod)
output = func_3479()
func_3480 = relay.Function([], output)
mutated_mod['func_3480'] = func_3480
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3504 = relay.var("var_3504", dtype = "float64", shape = (3, 1, 3))#candidate|3504|(3, 1, 3)|var|float64
uop_3505 = relay.erf(var_3504.astype('float64')) # shape=(3, 1, 3)
uop_3509 = relay.exp(var_3504.astype('float32')) # shape=(3, 1, 3)
bop_3531 = relay.floor_divide(var_3504.astype('float64'), relay.reshape(uop_3509.astype('float64'), relay.shape_of(var_3504))) # shape=(3, 1, 3)
func_300_call = mod.get_global_var('func_300')
func_303_call = mutated_mod.get_global_var('func_303')
const_3537 = relay.const(True, dtype = "bool")#candidate|3537|()|const|bool
call_3536 = relay.TupleGetItem(func_300_call(relay.reshape(const_3537.astype('bool'), [])), 0)
call_3538 = relay.TupleGetItem(func_303_call(relay.reshape(const_3537.astype('bool'), [])), 0)
bop_3545 = relay.left_shift(uop_3505.astype('int32'), const_3537.astype('int32')) # shape=(3, 1, 3)
func_592_call = mod.get_global_var('func_592')
func_595_call = mutated_mod.get_global_var('func_595')
const_3549 = relay.const([6,-8,4,-8,4,8,3,-8,-1,5,-9,2,7,5,1,-3,8,10,5,-5,-3,10,-4,-2,-9,10,-9,-4,-2,-4,-3,-1,-8,-2,-8,-1,10,8,-2,-9,-9,-9,-1,-3,-1,7,-3,6,-9,4,5,-8,-7,-9,7,9,6,4,-2,2,3,-1,10,-10,6,-6,-9,6,-3,4,4,5,3,9,6,9,5,-8,7,-5,1,-8,8,-6,-10,10,-6,-3,-6,-6,-8,-4,5,7,1,9,-3,-2,-10,3,-1,-1,10,7,8,8,8,-10,-5,7,9,8], dtype = "int16")#candidate|3549|(112,)|const|int16
var_3550 = relay.var("var_3550", dtype = "int16", shape = (672,))#candidate|3550|(672,)|var|int16
call_3548 = relay.TupleGetItem(func_592_call(relay.reshape(const_3549.astype('int16'), [16, 1, 7]), relay.reshape(var_3550.astype('int16'), [16, 6, 7]), ), 0)
call_3551 = relay.TupleGetItem(func_595_call(relay.reshape(const_3549.astype('int16'), [16, 1, 7]), relay.reshape(var_3550.astype('int16'), [16, 6, 7]), ), 0)
func_2207_call = mod.get_global_var('func_2207')
func_2209_call = mutated_mod.get_global_var('func_2209')
var_3560 = relay.var("var_3560", dtype = "int32", shape = (56,))#candidate|3560|(56,)|var|int32
call_3559 = relay.TupleGetItem(func_2207_call(relay.reshape(var_3560.astype('int32'), [14, 2, 2])), 0)
call_3561 = relay.TupleGetItem(func_2209_call(relay.reshape(var_3560.astype('int32'), [14, 2, 2])), 0)
bop_3563 = relay.mod(uop_3509.astype('float32'), relay.reshape(uop_3505.astype('float32'), relay.shape_of(uop_3509))) # shape=(3, 1, 3)
uop_3580 = relay.atanh(call_3536.astype('float32')) # shape=(14, 7, 6)
uop_3582 = relay.atanh(call_3538.astype('float32')) # shape=(14, 7, 6)
func_592_call = mod.get_global_var('func_592')
func_595_call = mutated_mod.get_global_var('func_595')
call_3583 = relay.TupleGetItem(func_592_call(relay.reshape(const_3549.astype('int16'), [16, 1, 7]), relay.reshape(call_3548.astype('int16'), [16, 6, 7]), ), 0)
call_3584 = relay.TupleGetItem(func_595_call(relay.reshape(const_3549.astype('int16'), [16, 1, 7]), relay.reshape(call_3548.astype('int16'), [16, 6, 7]), ), 0)
func_1747_call = mod.get_global_var('func_1747')
func_1752_call = mutated_mod.get_global_var('func_1752')
const_3590 = relay.const([4.660547,3.507652,0.448487,-3.355417,7.662141,-9.093182,2.450478,-7.524552,0.180268,-5.029785,3.561933,5.944160,2.751368,0.357340,-1.464451,-5.771599,-9.612460,-4.406680,-1.295478,0.445482,-1.496465,-2.985309,2.626786,-3.002515,2.360114,-1.109428,2.311548,-4.902864,9.152481,3.183139,-4.664365,5.096771,7.518554,-2.143791,-9.713689,2.802068,1.190665,7.619768,5.336290,-6.353656,-7.513572,2.655344,-8.996486,-1.911803,0.482261,1.837880,-3.058664,0.140448,-5.966118,9.896785,3.741696,2.458341,-1.566614,3.419600,-6.892768,6.581838,0.196804,-8.602957,-7.832449,0.611771,-4.412594,-1.746097,2.894746,9.424062,2.557402,9.756339,0.727506,-2.791136,1.004016,8.800024,7.003553,-9.092286,7.830818,-6.935079,-0.419235,-1.799962,-1.583006,8.487765,-8.322915,7.746608,4.255470], dtype = "float64")#candidate|3590|(81,)|const|float64
call_3589 = relay.TupleGetItem(func_1747_call(relay.reshape(const_3590.astype('float64'), [9, 3, 3]), relay.reshape(const_3549.astype('int16'), [112,]), relay.reshape(const_3537.astype('bool'), []), ), 2)
call_3591 = relay.TupleGetItem(func_1752_call(relay.reshape(const_3590.astype('float64'), [9, 3, 3]), relay.reshape(const_3549.astype('int16'), [112,]), relay.reshape(const_3537.astype('bool'), []), ), 2)
func_1627_call = mod.get_global_var('func_1627')
func_1630_call = mutated_mod.get_global_var('func_1630')
var_3605 = relay.var("var_3605", dtype = "uint64", shape = (13,))#candidate|3605|(13,)|var|uint64
call_3604 = func_1627_call(relay.reshape(var_3605.astype('uint64'), [1, 13]), relay.reshape(var_3605.astype('uint64'), [1, 13]), )
call_3606 = func_1627_call(relay.reshape(var_3605.astype('uint64'), [1, 13]), relay.reshape(var_3605.astype('uint64'), [1, 13]), )
output = relay.Tuple([bop_3531,bop_3545,call_3548,const_3549,var_3550,call_3559,var_3560,bop_3563,uop_3580,call_3583,call_3589,const_3590,call_3604,var_3605,])
output2 = relay.Tuple([bop_3531,bop_3545,call_3551,const_3549,var_3550,call_3561,var_3560,bop_3563,uop_3582,call_3584,call_3591,const_3590,call_3606,var_3605,])
func_3607 = relay.Function([var_3504,var_3550,var_3560,var_3605,], output)
mod['func_3607'] = func_3607
mod = relay.transform.InferType()(mod)
mutated_mod['func_3607'] = func_3607
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3607_call = mutated_mod.get_global_var('func_3607')
var_3609 = relay.var("var_3609", dtype = "float64", shape = (3, 1, 3))#candidate|3609|(3, 1, 3)|var|float64
var_3610 = relay.var("var_3610", dtype = "int16", shape = (672,))#candidate|3610|(672,)|var|int16
var_3611 = relay.var("var_3611", dtype = "int32", shape = (56,))#candidate|3611|(56,)|var|int32
var_3612 = relay.var("var_3612", dtype = "uint64", shape = (13,))#candidate|3612|(13,)|var|uint64
call_3608 = func_3607_call(var_3609,var_3610,var_3611,var_3612,)
output = call_3608
func_3613 = relay.Function([var_3609,var_3610,var_3611,var_3612,], output)
mutated_mod['func_3613'] = func_3613
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3426_call = mod.get_global_var('func_3426')
func_3428_call = mutated_mod.get_global_var('func_3428')
call_3657 = relay.TupleGetItem(func_3426_call(), 0)
call_3658 = relay.TupleGetItem(func_3428_call(), 0)
func_1876_call = mod.get_global_var('func_1876')
func_1881_call = mutated_mod.get_global_var('func_1881')
const_3663 = relay.const([7.890857,9.211929,-2.959036,7.372841,-3.755140,-4.971526,-1.620329,4.206515,-1.806366,-9.758118,9.816215,-4.958643,4.140545,-6.277686,9.086608,8.262397,9.261748,4.433060,-7.060299,-4.179121,-3.384656,3.012275,-0.710334,8.159144,4.152396,-8.183967,-2.741463,-1.033473,-6.984324,-2.739285,5.223454,3.019481,-9.875525,-3.663802,5.788217,4.014610,3.684422,-7.410165,-7.380079,8.403991,-7.848832,-2.086584,-3.300387,-5.611998,0.389518,-8.729593,3.502931,3.148560,-1.031773,-0.290875,8.842067,-5.514225,-5.625564,-0.710335,-4.209522,-6.371019,-2.688906,3.238832,7.697582,2.151167,-7.584294,6.182551,2.803301,6.532103,-9.173285,3.873213,-1.208137,3.838273,3.748360,8.295042,0.343408,-4.069847,-8.219263,-6.772466,2.798803,-6.754725,-2.334883,9.611696,-2.394810,1.212063,1.214249,-3.907297,-3.244701,-2.664910,-7.652955,4.588013,-8.890098,5.373174,1.037714,-4.369893,2.416796,-7.622389,9.028969,-7.671254,4.962506,-6.277405,-2.000621,-0.283475,-4.804888,-4.042430,-0.501149,-5.349540,1.264623,6.985493,-2.220166,-1.709011,-1.057584,5.444886,-3.358138,8.994476,6.576804,-6.343345,0.457097,1.864136,-3.878139,-2.919715,3.843661,8.134933,-9.195902,-0.588495,-9.458664,-2.378924,7.288289,-1.208122,3.631037,7.125541,-2.559737,8.769552,-1.922795,5.982238,-7.073350,9.461979,0.474059,3.015730,3.923394,-4.224034,-8.026127,-5.007774,-0.990103,2.336338,0.390585,-1.129537,5.609700,1.292281,-6.240787,-1.018146,-6.556136,9.239071,-6.344655,3.351485,-1.174176,2.639732,-4.418195,-6.630875,7.932200,2.747565,2.564197,-2.453843,2.794441,-3.372291,-8.836990,-4.852936,5.061025,-1.399999,-6.044563,7.551723,1.727758,4.003087,4.048020,-4.967754,-0.865514,6.729632,-4.897768,-9.960640,1.842905,8.595978,4.056154,-7.566820,1.742525,-9.251606,-5.665414,-9.914965,-3.813106,6.532289,-8.294280,-6.186244,9.905993,-7.882296,6.435590,6.581415,1.924378,1.879467,1.364566,2.936403,-0.434072,-1.770108,-8.356046,4.676954,6.410325,-9.289748,-4.300245,-2.671105,-0.175837,9.266899,3.935823,-1.202031,-8.141424,6.918881,0.246245,-5.195532,-9.262548,-6.592471,-8.053654,9.996230,-8.186820,3.359924,5.371848,2.860997,-9.953794,2.653817,2.069439,-4.227728,6.315100,6.295810,1.040419,7.152302,7.824862,-1.163435,2.504978,1.396459,3.486162,-4.910558,-5.251146,-3.899726,4.418005,-0.659799,0.248281,-1.422339,-5.416860,0.600696,3.418245,7.638480,-9.875060,-7.939995,9.744005,6.060592,-1.328355,7.212564,1.959345,6.985416,-0.908731,-0.085919,1.713145,-9.651146,-9.521083,2.338958,-8.813935,-9.155377,-2.032958,-2.529830,-3.694084,-4.880359,-4.128436,6.609198,4.221228,-4.027240,-1.375201,5.539630,8.435665,0.453817,3.922812,3.616184,6.177012,-9.724430,4.781497,-6.520525,-1.499978,-6.454740,-0.131726,6.466447,4.712043,3.992580,-7.129136,9.580944,6.227492,5.401043,4.784142,-0.154138,7.523696,-5.926156,-6.233840,-4.145699,9.823872,4.937599,9.302018,7.375699,-9.582457,-3.455385,2.877867,-0.365602,6.615492,5.374204,-3.583525,5.549256,-6.563204,-4.886046,-7.564723,2.592058,-3.326824,-1.383799,7.453321,-5.084693,-8.963013,-3.682981,-7.267269,-5.979310,9.891607,-2.316932,-2.929624,4.893253,5.428738,2.712139,-3.478033,2.267123,3.021963,-2.539667,0.996143,-2.759999,-8.344567,5.104242,8.355695,-3.938290,6.625965,-3.762006,-1.602555,-8.446474,-2.302879,-7.748830,-0.208406,3.742690,7.741929,2.552179,-8.436452,-7.617029,-6.666099,2.755942,-9.788815,-5.902625,-3.004992,3.885528,-3.706046,-0.474378,6.758217,-2.821898,-2.958285,2.569492,5.594399,-4.167901,-3.645632,-5.932886,-9.429829,-9.497199,8.829309,-2.885284,3.480001,4.625208,4.651367,-5.819278,-7.209929,-4.490509,-5.964137,-0.865842,-2.904786,9.719798,2.770486,-9.615217,0.860313,-4.579432,9.182484,-9.669728,-4.056738,0.890589,6.695304,-6.237384], dtype = "float64")#candidate|3663|(384,)|const|float64
var_3664 = relay.var("var_3664", dtype = "float32", shape = (8, 12))#candidate|3664|(8, 12)|var|float32
const_3665 = relay.const(False, dtype = "bool")#candidate|3665|()|const|bool
call_3662 = relay.TupleGetItem(func_1876_call(relay.reshape(const_3663.astype('float64'), [3, 16, 8]), relay.reshape(const_3663.astype('float64'), [3, 16, 8]), relay.reshape(var_3664.astype('float32'), [96,]), relay.reshape(const_3665.astype('bool'), []), ), 1)
call_3666 = relay.TupleGetItem(func_1881_call(relay.reshape(const_3663.astype('float64'), [3, 16, 8]), relay.reshape(const_3663.astype('float64'), [3, 16, 8]), relay.reshape(var_3664.astype('float32'), [96,]), relay.reshape(const_3665.astype('bool'), []), ), 1)
output = relay.Tuple([call_3657,call_3662,const_3663,var_3664,const_3665,])
output2 = relay.Tuple([call_3658,call_3666,const_3663,var_3664,const_3665,])
func_3681 = relay.Function([var_3664,], output)
mod['func_3681'] = func_3681
mod = relay.transform.InferType()(mod)
mutated_mod['func_3681'] = func_3681
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3682 = relay.var("var_3682", dtype = "float32", shape = (8, 12))#candidate|3682|(8, 12)|var|float32
func_3681_call = mutated_mod.get_global_var('func_3681')
call_3683 = func_3681_call(var_3682)
output = call_3683
func_3684 = relay.Function([var_3682], output)
mutated_mod['func_3684'] = func_3684
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3426_call = mod.get_global_var('func_3426')
func_3428_call = mutated_mod.get_global_var('func_3428')
call_3701 = relay.TupleGetItem(func_3426_call(), 4)
call_3702 = relay.TupleGetItem(func_3428_call(), 4)
output = call_3701
output2 = call_3702
func_3712 = relay.Function([], output)
mod['func_3712'] = func_3712
mod = relay.transform.InferType()(mod)
output = func_3712()
func_3713 = relay.Function([], output)
mutated_mod['func_3713'] = func_3713
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3479_call = mod.get_global_var('func_3479')
func_3480_call = mutated_mod.get_global_var('func_3480')
call_3900 = func_3479_call()
call_3901 = func_3479_call()
output = call_3900
output2 = call_3901
func_3905 = relay.Function([], output)
mod['func_3905'] = func_3905
mod = relay.transform.InferType()(mod)
output = func_3905()
func_3906 = relay.Function([], output)
mutated_mod['func_3906'] = func_3906
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3426_call = mod.get_global_var('func_3426')
func_3428_call = mutated_mod.get_global_var('func_3428')
call_3921 = relay.TupleGetItem(func_3426_call(), 2)
call_3922 = relay.TupleGetItem(func_3428_call(), 2)
func_3450_call = mod.get_global_var('func_3450')
func_3453_call = mutated_mod.get_global_var('func_3453')
var_3932 = relay.var("var_3932", dtype = "int16", shape = (432,))#candidate|3932|(432,)|var|int16
call_3931 = relay.TupleGetItem(func_3450_call(relay.reshape(var_3932.astype('int16'), [3, 9, 16]), relay.reshape(var_3932.astype('int16'), [3, 9, 16]), ), 1)
call_3933 = relay.TupleGetItem(func_3453_call(relay.reshape(var_3932.astype('int16'), [3, 9, 16]), relay.reshape(var_3932.astype('int16'), [3, 9, 16]), ), 1)
output = relay.Tuple([call_3921,call_3931,var_3932,])
output2 = relay.Tuple([call_3922,call_3933,var_3932,])
func_3935 = relay.Function([var_3932,], output)
mod['func_3935'] = func_3935
mod = relay.transform.InferType()(mod)
mutated_mod['func_3935'] = func_3935
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3936 = relay.var("var_3936", dtype = "int16", shape = (432,))#candidate|3936|(432,)|var|int16
func_3935_call = mutated_mod.get_global_var('func_3935')
call_3937 = func_3935_call(var_3936)
output = call_3937
func_3938 = relay.Function([var_3936], output)
mutated_mod['func_3938'] = func_3938
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3479_call = mod.get_global_var('func_3479')
func_3480_call = mutated_mod.get_global_var('func_3480')
call_3944 = func_3479_call()
call_3945 = func_3479_call()
output = relay.Tuple([call_3944,])
output2 = relay.Tuple([call_3945,])
func_3946 = relay.Function([], output)
mod['func_3946'] = func_3946
mod = relay.transform.InferType()(mod)
output = func_3946()
func_3947 = relay.Function([], output)
mutated_mod['func_3947'] = func_3947
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3426_call = mod.get_global_var('func_3426')
func_3428_call = mutated_mod.get_global_var('func_3428')
call_3963 = relay.TupleGetItem(func_3426_call(), 0)
call_3964 = relay.TupleGetItem(func_3428_call(), 0)
uop_3979 = relay.cos(call_3963.astype('float64')) # shape=(16, 5, 7)
uop_3981 = relay.cos(call_3964.astype('float64')) # shape=(16, 5, 7)
func_300_call = mod.get_global_var('func_300')
func_303_call = mutated_mod.get_global_var('func_303')
const_3993 = relay.const(True, dtype = "bool")#candidate|3993|()|const|bool
call_3992 = relay.TupleGetItem(func_300_call(relay.reshape(const_3993.astype('bool'), [])), 0)
call_3994 = relay.TupleGetItem(func_303_call(relay.reshape(const_3993.astype('bool'), [])), 0)
func_592_call = mod.get_global_var('func_592')
func_595_call = mutated_mod.get_global_var('func_595')
const_4005 = relay.const([4,3,-4,5,3,5,-4,10,9,-6,-7,-1,-1,7,4,8,-8,4,-6,-7,6,3,-10,5,10,-4,8,-3,2,-2,2,6,10,5,-1,-5,4,-1,8,2,7,-4,3,3,-9,-4,4,-2,8,-10,-10,9,2,10,6,-7,10,-8,-9,10,6,1,-2,4,-2,2,-9,8,1,-1,-10,7,-2,-6,-6,8,-10,3,2,5,-4,-6,8,-6,1,-5,8,4,-9,-10,7,-10,-9,-1,2,4,3,-1,-5,-1,6,9,9,5,-2,-6,5,7,9,-4,4,-9], dtype = "int16")#candidate|4005|(112,)|const|int16
var_4006 = relay.var("var_4006", dtype = "int16", shape = (672,))#candidate|4006|(672,)|var|int16
call_4004 = relay.TupleGetItem(func_592_call(relay.reshape(const_4005.astype('int16'), [16, 1, 7]), relay.reshape(var_4006.astype('int16'), [16, 6, 7]), ), 0)
call_4007 = relay.TupleGetItem(func_595_call(relay.reshape(const_4005.astype('int16'), [16, 1, 7]), relay.reshape(var_4006.astype('int16'), [16, 6, 7]), ), 0)
func_1747_call = mod.get_global_var('func_1747')
func_1752_call = mutated_mod.get_global_var('func_1752')
var_4013 = relay.var("var_4013", dtype = "float64", shape = (27, 3))#candidate|4013|(27, 3)|var|float64
call_4012 = relay.TupleGetItem(func_1747_call(relay.reshape(var_4013.astype('float64'), [9, 3, 3]), relay.reshape(const_4005.astype('int16'), [112,]), relay.reshape(const_3993.astype('bool'), []), ), 1)
call_4014 = relay.TupleGetItem(func_1752_call(relay.reshape(var_4013.astype('float64'), [9, 3, 3]), relay.reshape(const_4005.astype('int16'), [112,]), relay.reshape(const_3993.astype('bool'), []), ), 1)
bop_4026 = relay.mod(uop_3979.astype('float32'), relay.reshape(call_3963.astype('float32'), relay.shape_of(uop_3979))) # shape=(16, 5, 7)
bop_4029 = relay.mod(uop_3981.astype('float32'), relay.reshape(call_3964.astype('float32'), relay.shape_of(uop_3981))) # shape=(16, 5, 7)
func_3090_call = mod.get_global_var('func_3090')
func_3093_call = mutated_mod.get_global_var('func_3093')
var_4040 = relay.var("var_4040", dtype = "float64", shape = (1456,))#candidate|4040|(1456,)|var|float64
call_4039 = relay.TupleGetItem(func_3090_call(relay.reshape(var_4040.astype('float64'), [13, 7, 16])), 0)
call_4041 = relay.TupleGetItem(func_3093_call(relay.reshape(var_4040.astype('float64'), [13, 7, 16])), 0)
output = relay.Tuple([call_3992,const_3993,call_4004,const_4005,var_4006,call_4012,var_4013,bop_4026,call_4039,var_4040,])
output2 = relay.Tuple([call_3994,const_3993,call_4007,const_4005,var_4006,call_4014,var_4013,bop_4029,call_4041,var_4040,])
func_4044 = relay.Function([var_4006,var_4013,var_4040,], output)
mod['func_4044'] = func_4044
mod = relay.transform.InferType()(mod)
mutated_mod['func_4044'] = func_4044
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4044_call = mutated_mod.get_global_var('func_4044')
var_4046 = relay.var("var_4046", dtype = "int16", shape = (672,))#candidate|4046|(672,)|var|int16
var_4047 = relay.var("var_4047", dtype = "float64", shape = (27, 3))#candidate|4047|(27, 3)|var|float64
var_4048 = relay.var("var_4048", dtype = "float64", shape = (1456,))#candidate|4048|(1456,)|var|float64
call_4045 = func_4044_call(var_4046,var_4047,var_4048,)
output = call_4045
func_4049 = relay.Function([var_4046,var_4047,var_4048,], output)
mutated_mod['func_4049'] = func_4049
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3946_call = mod.get_global_var('func_3946')
func_3947_call = mutated_mod.get_global_var('func_3947')
call_4051 = relay.TupleGetItem(func_3946_call(), 0)
call_4052 = relay.TupleGetItem(func_3947_call(), 0)
output = relay.Tuple([call_4051,])
output2 = relay.Tuple([call_4052,])
func_4077 = relay.Function([], output)
mod['func_4077'] = func_4077
mod = relay.transform.InferType()(mod)
output = func_4077()
func_4078 = relay.Function([], output)
mutated_mod['func_4078'] = func_4078
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3426_call = mod.get_global_var('func_3426')
func_3428_call = mutated_mod.get_global_var('func_3428')
call_4117 = relay.TupleGetItem(func_3426_call(), 3)
call_4118 = relay.TupleGetItem(func_3428_call(), 3)
var_4127 = relay.var("var_4127", dtype = "int16", shape = (112,))#candidate|4127|(112,)|var|int16
bop_4128 = relay.greater_equal(call_4117.astype('bool'), relay.reshape(var_4127.astype('bool'), relay.shape_of(call_4117))) # shape=(112,)
bop_4131 = relay.greater_equal(call_4118.astype('bool'), relay.reshape(var_4127.astype('bool'), relay.shape_of(call_4118))) # shape=(112,)
func_3607_call = mod.get_global_var('func_3607')
func_3613_call = mutated_mod.get_global_var('func_3613')
const_4162 = relay.const([8.997962,4.992085,8.569638,-6.131874,-4.590648,-7.638142,6.630941,-4.400397,2.634708], dtype = "float64")#candidate|4162|(9,)|const|float64
const_4163 = relay.const([6,5,10,4,-6,4,-1,-10,-5,2,-4,-5,-5,4,-5,-9,-2,10,2,9,-5,10,9,6,2,-8,-10,-5,-8,-6,7,-3,8,10,-9,8,3,1,-7,7,-4,6,-8,1,-9,10,-10,2,8,8,10,-3,-3,6,-1,7,-8,1,3,3,-7,-5,-7,7,-8,5,10,-2,2,2,1,-1,2,4,-4,-5,-1,9,9,3,10,7,6,4,-5,3,6,4,6,3,-4,-10,-3,3,5,-7,-6,5,-4,-1,-3,-7,-8,9,7,-5,-4,-8,-4,-7,8,1,10,5,-5,5,1,-1,10,-5,3,10,5,-2,-10,9,7,-2,-8,-3,3,4,-9,-5,4,8,9,3,-7,-6,-8,-6,5,-3,5,7,-3,4,-6,1,-10,-7,8,-5,-9,-3,-6,-3,7,5,4,-3,-4,9,7,-4,-10,8,-3,2,-5,-10,-5,1,10,7,-1,1,7,-7,-9,-1,-2,-6,1,-8,4,-7,-2,3,8,6,-8,5,6,-2,-3,-5,-2,-3,-8,1,-10,2,-1,-5,-5,-8,-9,-10,5,9,7,-6,-4,5,-9,-7,7,2,-4,-8,-8,-4,9,2,-10,-5,-7,-5,9,5,6,-6,1,2,-5,-6,5,9,-8,10,-6,-2,-6,-3,6,-3,-2,-7,7,2,-8,-4,-2,10,8,7,-7,-4,-9,9,9,-8,-3,7,4,3,-8,8,-3,-10,-8,-2,10,-9,-7,2,10,-8,-9,-6,-4,5,-7,-2,1,1,10,6,1,7,-2,5,-3,7,-8,4,-2,-4,4,-9,-7,-4,-6,-7,6,7,4,-9,5,-8,-1,-4,1,-1,-1,10,5,-5,6,9,7,-7,-8,-8,6,-5,-8,9,-7,4,5,6,-8,10,-4,-6,-5,-1,-3,5,7,-4,10,-4,-6,-5,-10,8,3,-4,6,-9,4,3,1,7,-9,2,-6,6,-5,-10,1,5,-7,10,-10,4,9,3,5,-9,-1,-6,7,9,-3,7,9,6,2,1,5,9,-1,5,10,-2,4,10,-8,-1,7,2,1,-6,-6,-6,10,-6,-8,9,-4,1,-7,-7,-7,5,-6,4,7,-10,-6,-3,-2,7,7,-9,7,8,8,-10,-4,3,-3,7,6,2,-4,8,3,7,3,2,-4,5,-4,9,9,-7,-8,2,-10,5,9,-1,9,2,-3,-4,-3,-1,6,-6,-3,-7,7,-4,-4,-2,-2,-3,10,7,-10,-2,-1,-1,-4,-2,-9,-7,-8,3,10,5,8,-7,5,-6,6,-9,3,-6,8,2,-6,-4,-10,8,-2,-5,5,3,-7,-7,6,-2,8,6,5,-3,-8,7,6,1,-2,-2,-10,7,3,4,9,-8,3,5,1,1,7,-9,-5,10,-7,-4,-7,-6,-2,10,6,10,-2,-9,3,4,10,-2,2,-4,-4,7,7,2,4,1,-1,-1,-6,-6,10,8,3,-7,-1,5,-7,-9,-6,2,-4,-3,-5,-8,7,-1,-5,-9,10,5,-4,1,3,-6,2,2,-4,-2,9,2,-5,-3,6,1,7,-1,8,-4,1,-1,-9,-2,-6,-2,6,1,10,6,-9,2,-4,-8,-5,3,-4,3,-5,-8,9,8,-5,1,-4,-9,-3,-8,6,-9,-10,-8,-5,10,6,-3,-6,-2,-9,-6,9,5,-8,9,10,-6,-10,-5,-5,-9,10,6,2,-9,-1,5,10,-2,-4,4,-10,-4,-5,7,5,9,-7,-3,4,-1,7,-5,-7,-7,9,-7,-2,-9,-2,-6,-4,2,1,2], dtype = "int16")#candidate|4163|(672,)|const|int16
const_4164 = relay.const([10,-9,-1,3,7,3,-1,5,-3,10,-5,4,6,3,1,-1,-4,-8,-7,6,3,8,-4,7,3,7,-2,5,8,-5,-10,10,9,8,8,-9,-3,6,3,3,9,-4,-10,-8,-9,-7,-3,2,6,-5,-5,-5,3,-6,-3,2], dtype = "int32")#candidate|4164|(56,)|const|int32
var_4165 = relay.var("var_4165", dtype = "uint64", shape = (13,))#candidate|4165|(13,)|var|uint64
call_4161 = relay.TupleGetItem(func_3607_call(relay.reshape(const_4162.astype('float64'), [3, 1, 3]), relay.reshape(const_4163.astype('int16'), [672,]), relay.reshape(const_4164.astype('int32'), [56,]), relay.reshape(var_4165.astype('uint64'), [13,]), ), 3)
call_4166 = relay.TupleGetItem(func_3613_call(relay.reshape(const_4162.astype('float64'), [3, 1, 3]), relay.reshape(const_4163.astype('int16'), [672,]), relay.reshape(const_4164.astype('int32'), [56,]), relay.reshape(var_4165.astype('uint64'), [13,]), ), 3)
func_3450_call = mod.get_global_var('func_3450')
func_3453_call = mutated_mod.get_global_var('func_3453')
const_4172 = relay.const([-9,5,-7,-3,6,-7,-8,-8,-5,6,-1,9,-4,5,-6,-3,-1,-7,1,-5,-8,10,9,7,-3,10,-9,-2,-7,-5,5,-7,6,5,6,6,4,-1,4,-9,-2,-2,5,8,-3,6,-10,-6,-9,-6,3,-8,-10,10,-7,-2,7,2,10,-7,-2,10,-7,10,9,10,2,9,-9,3,-9,8,10,1,1,-2,-10,-7,-3,3,-5,-4,-5,6,-3,1,-7,-1,1,7,-9,-5,5,5,10,-10,3,1,-8,-1,9,6,-2,-3,8,-5,2,7,3,-5,-2,-8,-10,2,-8,-2,6,3,4,1,7,-10,-7,6,9,-2,8,-7,-9,-8,-3,-5,8,-6,-5,4,-6,-1,-1,2,-10,-2,-6,-9,-9,3,-9,8,-10,10,5,9,10,2,-9,-3,3,-7,6,4,-5,5,9,3,-2,-5,9,-6,-6,-4,5,3,-5,-6,6,-4,1,7,7,-9,3,3,10,4,-8,-2,-4,-4,3,9,2,-4,-5,4,1,10,-9,-7,-4,8,7,-6,3,9,-2,9,4,-8,4,-2,5,-6,-6,-5,4,-2,-3,2,-10,2,-1,-5,-4,-5,-5,1,10,-6,2,9,-7,5,-1,6,7,-1,-8,-5,-9,1,9,6,1,8,-5,9,9,-4,10,10,-5,-8,-9,-7,5,-4,10,-6,4,-4,2,-3,-7,9,-4,-7,-2,-5,-1,-9,10,1,-5,-3,-2,10,-10,4,9,-7,6,5,2,-9,4,-7,3,-6,-6,9,-8,3,1,7,5,-4,-9,-9,1,-2,-7,-1,9,-1,8,3,7,4,-3,8,5,9,5,3,-5,2,3,4,-1,-7,5,5,-5,-9,-9,6,-3,6,-2,-5,-5,9,-10,-2,-8,-2,-8,-4,-5,1,2,-6,6,-4,-2,-5,5,6,7,-8,6,5,-6,-7,3,-3,-9,1,-2,2,-5,-2,1,10,6,2,-8,6,-7,5,10,5,6,3,-5,5,-3,2,6,1,-10,4,9,1,2,6,-3,-1,8,-8,-10,3,-9,7,-9,-7,-3,-6,-10,8,5,4,-4,-7,-1,-3,10,-4,1,4,2,-8,2,-7,4,-4,1,7,3,8,-10,4,-7,9,-2,9,-2,-10,2,7,-5,3], dtype = "int16")#candidate|4172|(432,)|const|int16
call_4171 = relay.TupleGetItem(func_3450_call(relay.reshape(const_4172.astype('int16'), [3, 9, 16]), relay.reshape(const_4172.astype('int16'), [3, 9, 16]), ), 0)
call_4173 = relay.TupleGetItem(func_3453_call(relay.reshape(const_4172.astype('int16'), [3, 9, 16]), relay.reshape(const_4172.astype('int16'), [3, 9, 16]), ), 0)
output = relay.Tuple([bop_4128,call_4161,const_4162,const_4163,const_4164,var_4165,call_4171,const_4172,])
output2 = relay.Tuple([bop_4131,call_4166,const_4162,const_4163,const_4164,var_4165,call_4173,const_4172,])
func_4181 = relay.Function([var_4127,var_4165,], output)
mod['func_4181'] = func_4181
mod = relay.transform.InferType()(mod)
var_4182 = relay.var("var_4182", dtype = "int16", shape = (112,))#candidate|4182|(112,)|var|int16
var_4183 = relay.var("var_4183", dtype = "uint64", shape = (13,))#candidate|4183|(13,)|var|uint64
output = func_4181(var_4182,var_4183,)
func_4184 = relay.Function([var_4182,var_4183,], output)
mutated_mod['func_4184'] = func_4184
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3479_call = mod.get_global_var('func_3479')
func_3480_call = mutated_mod.get_global_var('func_3480')
call_4223 = func_3479_call()
call_4224 = func_3479_call()
output = relay.Tuple([call_4223,])
output2 = relay.Tuple([call_4224,])
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
const_4360 = relay.const([[[-5.329098,-7.014146,-1.789108,3.013799,-8.374209,0.995987,-0.383407,1.708234,-4.861688,6.234343],[-5.928482,7.422442,4.425747,7.730313,-9.631576,-2.541461,-4.883023,-1.725946,-8.841240,-7.588524],[-8.938794,-2.783644,-2.605622,0.485772,1.308356,6.445529,-8.679595,-0.267601,-5.804141,1.021011],[9.565385,5.333212,4.933105,-5.705535,3.864576,-4.263750,-7.972094,-0.562377,-0.071324,4.317761]],[[-1.820539,8.279743,-5.276242,2.508467,5.109503,6.013584,-9.694352,-7.315891,-6.470743,4.256062],[-4.084159,-9.083260,-7.339276,1.204156,-6.137118,-5.970725,1.806853,-8.138926,-8.350397,-4.472442],[-3.854827,-9.071679,-1.387648,-5.787744,4.888361,7.597850,-9.296041,9.065313,-5.961416,2.864700],[0.966608,-5.481947,-5.525205,-3.416208,-1.097195,-7.837881,-5.814786,7.132605,-2.030994,-9.256890]],[[2.170324,9.814897,7.637784,1.406921,2.881981,-8.925596,-0.245395,-5.126664,8.383510,2.238325],[8.001425,8.119929,-3.764601,6.103066,-8.439820,5.805415,6.874719,3.552658,4.548629,-7.760879],[-4.021692,7.940078,4.427606,1.476833,4.800887,-6.717840,-1.666081,-3.143829,-7.262407,3.491057],[3.337783,0.900133,2.348531,9.785236,3.695523,-1.660457,5.589534,-7.349288,8.425424,2.926347]],[[4.316757,4.207570,8.743654,-5.320666,6.090556,5.805297,-5.311585,5.692885,0.967797,-8.690228],[0.561545,-3.824510,6.905796,6.547095,-9.960308,5.424505,8.184683,-3.302196,-1.954045,-2.048311],[-0.646524,5.564853,-7.745554,8.051048,3.665221,-4.843620,-8.949600,1.801019,-2.581957,-4.428666],[-7.215306,-5.949196,-2.122294,-5.789011,9.169994,4.622064,-6.111004,2.389844,5.698555,5.989204]],[[-1.783888,0.205320,-2.299828,-2.485333,-4.583344,-6.407651,-3.847031,-1.979051,0.273780,-3.745072],[8.808862,-2.866217,-5.927463,8.425886,-0.799758,-5.416377,-1.064781,3.250066,3.119365,9.879056],[-1.923459,-6.379154,-4.836431,-7.731830,8.248053,0.233085,-8.912406,6.471075,4.485292,-2.880048],[0.692132,-3.063717,1.423468,-4.392534,-5.113633,-9.257794,9.296605,2.450006,5.602211,3.125394]],[[-8.835206,0.079388,7.765360,7.751377,2.086420,-2.214600,7.499094,8.160237,7.655331,5.729104],[2.000240,-3.626784,-8.358706,0.622549,7.559986,-8.788609,6.089342,-8.319778,-9.199862,4.050072],[-4.645527,-3.534896,-9.238542,-1.180486,-5.009834,0.466531,5.077536,-3.155640,-9.902881,0.694086],[9.727398,7.337270,2.774862,3.818825,-4.776735,-2.684602,-8.966367,-6.312751,-0.687710,-4.638568]]], dtype = "float64")#candidate|4360|(6, 4, 10)|const|float64
var_4361 = relay.var("var_4361", dtype = "float64", shape = (6, 4, 10))#candidate|4361|(6, 4, 10)|var|float64
bop_4362 = relay.divide(const_4360.astype('float64'), relay.reshape(var_4361.astype('float64'), relay.shape_of(const_4360))) # shape=(6, 4, 10)
func_633_call = mod.get_global_var('func_633')
func_635_call = mutated_mod.get_global_var('func_635')
var_4366 = relay.var("var_4366", dtype = "bool", shape = (225, 1))#candidate|4366|(225, 1)|var|bool
call_4365 = relay.TupleGetItem(func_633_call(relay.reshape(var_4366.astype('bool'), [5, 9, 5])), 1)
call_4367 = relay.TupleGetItem(func_635_call(relay.reshape(var_4366.astype('bool'), [5, 9, 5])), 1)
uop_4377 = relay.log10(bop_4362.astype('float64')) # shape=(6, 4, 10)
func_3090_call = mod.get_global_var('func_3090')
func_3093_call = mutated_mod.get_global_var('func_3093')
const_4396 = relay.const([9.811587,-8.639040,0.024521,-9.059762,8.751503,0.851287,1.251802,1.486909,9.291549,-7.188419,0.576637,-4.938962,-9.809878,4.216812,9.497455,3.467295,9.801059,8.031060,7.662758,-7.009983,8.306299,3.451808,-2.600653,-1.040219,-5.223293,3.075588,-0.426000,-4.379585,-4.782523,7.040456,-7.598306,-6.511280,-1.454146,4.219654,-7.677739,-0.867317,7.296246,-0.541045,3.238685,3.185374,1.956293,1.798549,9.151873,-3.933148,-8.176639,3.848861,-3.154224,-3.024262,-7.373786,-2.417649,6.442182,-7.477723,4.608119,-0.815260,4.193092,-1.230560,7.338571,6.830327,6.797958,-2.038540,9.953074,8.735442,-8.442411,-3.955188,5.205449,3.686258,-0.728436,0.918640,-4.450158,-7.023693,-4.915554,-3.039352,-4.964131,-9.849675,2.409825,1.142660,-4.586289,-4.941989,-9.889916,9.735493,2.789458,-4.874855,-2.787044,4.983497,-5.697319,0.445223,-7.443804,-1.200226,5.828894,3.635612,4.613844,6.948003,1.380091,-3.170586,-7.652836,5.047161,-7.608848,8.814025,1.097765,7.126700,-1.360557,-1.835567,-3.456058,-7.377991,2.392794,-0.184461,-7.959413,9.575265,7.699970,-9.860999,2.357799,-6.064029,8.418425,4.522159,-0.767133,-2.410089,4.674674,-3.006846,1.064419,8.981512,-0.142199,-5.691174,3.536714,-4.212907,9.182248,-9.120760,-3.953131,8.807258,6.442085,-0.005493,0.401605,-0.448685,-3.478533,7.265342,5.132352,-3.141285,-6.452015,7.479618,-6.408184,0.429742,-6.575882,1.568358,-1.142882,-6.876259,1.639172,8.108744,-4.000434,0.421238,-4.782265,-6.541223,2.906111,1.829841,3.463393,2.211915,-1.509871,-5.453261,-4.975323,5.039960,-5.505187,-0.981803,7.528989,-5.292815,-0.792544,-8.841772,-9.306764,-2.537965,3.883391,-3.786943,-7.210546,0.407877,-6.392611,8.018882,6.249267,6.265977,8.155784,4.800420,0.323565,-8.680066,3.581354,2.599807,8.166464,6.072338,9.018735,-5.892943,4.153670,5.881219,5.311236,-0.223193,7.443368,-1.620883,-2.864136,0.025790,4.488447,8.052937,-6.972034,8.598282,-0.314688,6.415627,-0.568646,-7.089562,9.306585,5.734861,-0.544840,4.778366,1.233068,-1.155421,3.113127,8.365063,4.314034,5.525581,8.712468,-7.166730,5.868432,-9.268669,4.546221,9.572625,-3.225789,6.886945,-6.184123,-2.930086,-1.179705,7.878857,8.560331,-9.895081,9.205983,-9.077736,-1.357824,5.873983,-7.498347,3.226499,-4.097952,-3.970289,2.313918,1.223445,-7.196373,3.021033,8.726260,-0.963777,-6.510095,8.455780,-1.841430,-2.457967,-1.110133,-4.776491,5.479917,-9.060955,-3.341268,-8.147156,-7.952810,-6.526855,-2.885910,7.596403,-0.258396,-6.300300,4.850674,6.554775,2.516183,-4.236299,2.969627,5.298774,5.451067,-1.734130,-1.453654,5.221438,-6.837394,-0.516322,-4.104034,-3.143033,9.989401,3.419642,9.652875,4.539837,-8.035532,-3.371192,-1.227706,4.796619,-8.399193,-4.218241,-4.587864,2.510176,4.305505,1.730831,-7.031106,-6.835232,-9.477876,-7.819155,-4.658247,7.406337,3.759428,-8.670066,2.616399,8.054888,3.045551,-3.457064,-8.163754,2.262983,5.866988,0.363181,-6.158969,-6.136758,6.246001,-3.279791,-7.109480,-0.006984,-0.159244,7.656656,-0.629320,7.684400,-0.827213,-9.153850,7.664486,-0.501171,-2.594564,-0.431918,-8.482912,-0.230705,1.150803,9.539989,-6.973355,-9.064539,1.809344,-1.578784,-8.339159,0.762362,4.020489,5.287684,6.642405,-9.216793,0.906028,0.052937,7.048782,3.345832,-1.154505,-6.726835,8.875637,3.713122,-9.623834,-2.609751,1.637642,-7.204557,3.799325,-2.968815,2.238596,3.400218,2.796667,-2.100699,-3.088961,-5.006217,6.832892,5.000827,0.525435,3.282208,-2.927548,-1.400729,1.895205,-1.917180,4.763922,-0.137221,3.021353,7.181335,-6.285288,0.765120,-7.981173,3.583292,-9.760252,-8.866447,-9.664569,-2.816337,0.869629,-8.033664,3.928460,-6.921391,3.209402,4.789537,-8.649737,-4.407109,1.142810,3.976224,9.920797,5.879519,3.176375,7.755804,7.197684,-1.448151,-3.230896,7.652480,2.296742,-2.757773,-6.730439,-5.440967,1.048069,2.976777,-3.740264,-9.593275,-3.323629,-9.922500,0.562548,2.180228,3.852675,0.667107,-2.803718,7.615478,-5.188703,2.013117,0.532508,3.704133,-6.535878,0.047977,9.346789,-2.517107,2.324001,2.046767,-8.781259,5.959376,-6.186454,7.760271,-5.523508,7.516756,4.829043,4.025769,-6.287116,2.649739,-8.956333,4.230152,-5.616299,1.198385,-5.317133,-0.675021,4.619933,-0.241108,-8.360196,-1.196955,-4.941377,-5.127071,-7.214700,9.854791,-5.465870,8.895651,4.642592,3.639118,-9.867027,-7.515904,9.889342,7.363737,-4.733356,1.215873,-1.918149,6.986078,5.591474,-6.572431,-7.493923,-2.251198,-3.449547,4.111936,-5.467140,8.900003,8.600749,-0.366408,-4.235752,1.392555,4.820628,2.325578,-3.545320,0.948316,-6.198886,-4.311248,8.088947,-0.862548,-5.141330,0.777303,-7.758208,-6.919434,-4.749790,-0.428865,-2.524888,-6.081033,-6.783562,5.597920,-6.458093,-2.053073,-2.797118,9.559212,7.362636,4.763494,6.127553,0.354279,0.487941,5.398820,-0.786230,-2.203281,3.574166,-2.369335,0.778746,2.282058,-6.479626,-0.089850,-6.231889,-6.199145,9.161614,8.931606,3.483550,-2.370219,-8.222826,-7.781355,-1.602659,-8.183558,0.637750,4.858489,-4.662022,6.330529,1.310453,-7.533477,9.458686,8.895964,-4.103274,-9.873223,7.204400,1.868340,-1.486904,-5.177153,-4.939534,3.684584,-8.816134,-3.078158,6.679580,2.369465,-5.882036,-0.749785,8.407624,-2.059548,-3.702014,2.063756,-9.449539,-0.518995,-5.082179,5.841140,8.792245,9.356244,0.489136,-9.650615,8.318409,0.026621,0.391970,3.813834,-7.584949,9.814219,-5.283386,-6.880080,2.083976,-4.847581,-5.388416,-7.170580,-6.360656,2.389967,-3.408377,-7.707197,0.587162,5.555947,9.902371,3.777627,-1.902579,-0.920377,2.681007,2.113855,1.454365,8.869296,6.190520,5.671077,1.215166,-0.531751,8.728744,4.146561,-9.243111,2.146841,7.202305,8.679415,1.907144,6.269775,9.115737,1.817937,-1.069053,-3.742980,2.427997,3.322958,-8.987849,-7.268505,-0.538244,-4.631692,-2.294995,-1.501672,4.384577,3.505528,6.009452,2.011344,-1.119366,-5.223742,1.630550,-2.350612,-2.853085,6.681905,5.887621,-7.782604,5.402667,3.447134,5.892701,-1.802622,8.350958,6.103360,-6.691451,6.046701,-9.866460,0.689622,-0.849218,-9.580957,5.732670,0.358683,3.857941,-6.399826,7.740235,-9.688028,6.013552,2.512845,-2.026385,2.102849,2.780612,3.406390,-5.339944,-7.043660,5.203687,-7.268069,-2.627187,4.399700,2.307804,8.305632,6.424734,1.758889,-5.844060,-1.471829,-9.595818,6.367396,-5.261827,5.904055,8.767131,-9.358095,-9.246562,2.456503,-9.534320,-3.845190,-4.212405,-3.635189,2.061816,-6.461314,-4.744719,-2.888127,-6.501240,1.877146,9.950568,-9.246178,-9.094296,4.306271,5.955588,9.717335,4.102731,2.001319,0.868025,-7.311639,-6.614245,-9.057698,2.159717,6.139021,-0.503267,-6.283126,2.231433,-1.106974,3.456458,-9.809944,-6.683333,9.550105,7.116652,7.053151,-7.205188,2.956624,-9.063739,-1.243490,-4.060248,-4.297716,-3.245740,-0.344048,7.990557,3.506339,-1.178130,6.458954,0.825538,2.998266,0.987324,-6.052272,-8.659407,-4.698013,9.857892,-4.932436,-7.253500,0.131984,6.467940,-0.230766,-1.046014,-7.347427,6.538487,-7.277136,-2.181512,2.703659,-4.024698,5.083125,9.440605,-0.314001,-6.156004,8.553995,2.400437,6.987444,-0.008452,8.331093,0.488739,-7.487667,4.229992,-1.420857,-2.767596,8.960114,6.468440,7.873693,9.867191,4.916347,-6.083466,-2.445341,8.578039,-0.063438,-1.914952,8.862697,4.144382,-9.407478,-0.954215,-8.836176,7.154144,3.621345,7.822024,5.993136,-0.369973,-9.087135,0.067415,-7.273542,7.482101,4.618918,-8.580112,0.300070,-8.568876,-7.355500,-1.239431,5.305431,1.405899,-3.147408,4.718780,9.868923,1.632930,-0.948779,-8.237816,4.424591,0.285757,8.769146,4.234878,-7.431686,1.653880,-6.662169,2.101780,9.574636,9.175352,4.932194,7.132521,-3.105953,9.539555,-1.684700,-1.574859,7.011580,-9.538732,7.222975,2.896919,8.794529,9.633879,4.971518,2.439531,8.625947,-0.899291,2.752741,6.103911,-4.084757,-1.323220,-8.271628,8.381931,-4.706294,7.343369,2.138807,1.815016,5.109212,9.844161,-6.593164,1.205296,6.968128,-8.194481,3.173361,-1.903119,-2.440278,-5.675525,6.784412,-7.380015,5.878383,-9.179584,0.444082,8.962372,-9.099972,8.780075,8.281482,-1.202644,-2.012497,4.241454,-9.209569,-3.432574,-1.143064,4.100905,-9.604723,-4.688484,6.162523,-3.767144,-7.863011,7.266584,-0.536507,2.611714,5.681900,-0.999660,0.763441,-7.292545,-3.519309,-0.038716,3.751049,-9.042223,-1.855735,-1.337075,9.180860,-1.060508,-5.522561,-8.866275,-9.097991,0.025494,5.186006,9.814634,8.754029,-7.278565,-5.957809,4.319229,7.973296,7.043302,-7.988305,3.838450,1.572982,2.041690,-3.871840,-1.955106,-3.975132,-6.590363,-9.034288,-7.643205,3.650928,8.568077,9.564179,-6.840821,-6.957376,-0.995442,1.101868,0.264431,5.013729,-6.879935,-7.099104,-9.050084,-8.739857,8.377464,9.407575,0.678168,-5.296975,-8.015005,6.708720,-4.285714,1.195227,-7.241511,5.810626,7.875435,-8.884487,-6.341378,-2.397341,3.283077,5.008162,2.123858,-0.297704,-4.003553,9.038091,5.579855,9.295377,6.372365,-5.731928,9.466178,7.179186,7.781024,-3.453382,-9.938241,-8.886276,-9.683646,-3.754163,-9.665172,-4.020726,-7.477067,-2.720466,-8.773823,5.693893,-6.568159,3.004679,6.535666,-0.894556,-5.415561,-8.297146,4.377277,1.605146,6.894182,-0.410409,-4.490514,-4.298036,-0.812731,-7.957009,-3.989754,-8.146578,-9.292227,-7.005616,-7.207020,-5.814390,9.719463,-2.097566,9.397541,-6.691556,2.686880,3.429652,6.660055,-4.721867,-7.113250,-4.094048,5.842323,1.450448,-6.288330,7.727471,-2.015902,-3.237859,7.464545,-9.835255,-1.678824,8.531406,6.240035,4.709006,-6.629587,2.018541,8.230700,4.448571,-0.806829,-4.687907,-6.723547,-4.142340,4.108242,-0.151634,9.741004,3.605612,-9.544893,2.110365,9.131883,-1.437426,6.669464,-1.470583,-9.488037,0.919925,-2.050106,1.130606,2.986373,3.541746,-0.994614,0.143916,5.922560,4.053823,1.719429,9.940829,-3.646102,-1.452038,3.575400,-7.805143,-0.366288,7.098321,0.958451,9.614852,-3.292680,5.491706,8.715293,-3.866097,7.933956,-5.508464,-1.682235,-1.974234,9.843865,-1.911786,9.648832,-1.367391,-0.623040,4.068340,0.117201,7.371412,1.127218,-2.468661,7.887951,5.501041,0.717382,-4.327395,-4.071168,-3.050208,3.001064,-3.962362,1.704834,6.659284,-7.205904,3.259937,4.440421,2.197492,6.681580,9.275130,-4.124817,6.529220,-5.244192,-1.384273,-9.672780,7.181246,4.601141,1.754161,-5.425810,5.165769,6.828638,-9.801333,4.290840,7.418712,-5.279082,9.796315,-3.898326,-0.668278,-1.459559,8.125247,1.786863,9.816980,-0.222381,3.453241,8.161247,-1.169565,4.393846,1.058196,-1.029802,8.426333,-9.604961,-4.383572,2.766622,6.007349,0.275610,5.168549,2.250345,2.110929,2.915482,7.583137,1.609754,4.314611,-8.340973,3.681441,4.098249,3.667369,-0.373345,-9.296577,-0.979761,9.897061,-3.321129,-2.804219,8.247332,-6.646719,-4.064478,0.897331,7.848715,-4.442890,-3.611035,-7.802285,-9.982496,8.956792,9.580414,4.823872,2.955698,7.120733,2.687112,-6.775325,-7.566473,1.802759,-6.213991,-0.429568,3.604912,6.500965,2.065772,0.907315,-2.180762,-8.024537,8.471647,5.475611,-0.840416,-4.887003,9.472678,2.073025,8.406423,-5.933849,5.437069,1.594781,-6.258708,-7.742610,9.219941,8.067686,-5.836361,0.173190,6.798197,6.698773,-6.540009,1.317372,-1.418601,2.318229,3.878713,0.321348,-1.179796,3.544920,0.048194,-9.617094,-2.560104,-0.103127,5.492877,-9.822515,1.232176,0.579768,3.611586,2.628909,5.753844,-2.544862,-6.602514,4.603918,-7.799775,4.021452,4.687696,-1.747963,-3.858220,-5.486174,5.475431,-2.988485,-2.566292,-3.661597,0.779431,8.347161,-6.236124,8.586492,7.953232,5.208710,-7.226024,-5.373427,9.718311,3.756018,0.536149,8.451804,-9.264800,9.629835,5.971383,-8.057582,9.461042,3.483678,1.923227,7.119948,-2.375380,9.115172,5.351500,-4.357280,-6.579537,-1.695585,5.256062,-7.347228,-2.513877,0.635680,8.437008,-2.087153,4.365292,-8.979006,-0.907989,-9.813472,6.280940,5.500513,6.244646,3.264089,6.383179,1.217809,0.007521,-2.312797,-4.650288,-0.681305,-3.073036,-3.400756,-6.763181,-8.575194,-0.777645,9.173207,-6.689610,2.710623,-7.567392,-8.125665,-9.018100,2.135417,4.399345,4.887408,4.360037,-8.727828,-7.104908,0.928420,7.043313,-8.793408,-1.522120,4.393034,-1.774254,-8.089785,6.727828,3.427110,4.175724,-5.251417,-7.553432,-4.469410,3.760088,8.186135,1.030421,-2.149151,5.163578,9.812173,6.994761,-7.083900,8.571303,-3.673844,1.016533,-1.403656,-1.772128,-3.220473,4.540323,-6.538453,6.538031,-9.333400,7.628476,6.180273,0.030914,-9.893802,-6.908267,9.531244,-9.610296,-0.973019,4.684444,-3.047748,4.137068,-1.922120,0.742853,4.952280,1.721733,5.307575,9.697098,3.978266,8.519540,8.382077,-2.537329,9.148696,-0.961426,3.183686,6.977264,-9.396167,-1.220945,2.713929,0.932994,-3.059132,-3.979004,0.763324,-3.921011,7.944278,9.034867,5.390508,7.565532,-8.480660,1.119871,9.108938,0.866521,4.818848,-2.385954,6.955016,-4.332095,-5.585501,0.946063,-9.309571,-8.798224,-9.039488,-6.564242,-8.841788,-8.020093,3.352608,-7.190593,-1.279754,-3.192481,7.810620,-8.616764,2.010420,-6.140817,-1.741731,7.418069,2.929873,-4.528122,7.765074,-6.946525,-3.278293,-8.070741,-0.726275,-4.809926,-8.589191,-5.910163,6.969334,-4.154697,7.832518,0.333406,1.468455,-1.748201,-4.059174,-2.285276,0.158125,3.165471,3.041199,-8.078975,-7.128722,5.786386,4.082476,-4.593867,-5.480341,9.318940,3.453475,0.378067,-8.977203,-7.201953,-1.006873,-2.441592,9.562573,0.095473,-9.251535,-7.811934,-4.991171,8.384660,6.533705,0.578267,5.083630,-2.089345,8.725541,6.877357,8.226757,-7.315153,-9.104156,-3.520529,8.238844,-4.890872,9.355884,-7.685307,-3.283363,6.389490,-2.466327,-2.058933,-6.884790,-2.567342,-7.122134,3.590409,3.387022,-7.663229,-0.936933,2.235776,-8.358047,1.864631,-8.518853,-7.734895,-6.760964,5.076822,-9.178883,-3.653936,-9.741328,-3.926743,-1.431058,-4.271161,3.139041,5.650096,3.883776,8.381583,-2.185046,8.526077,8.632723,-1.828018,-5.156255,-8.412512,1.830201,3.619985,0.967954,-3.691233,5.400574,-9.554928,2.061548,-6.871225,-6.579229,5.387998,5.292266,-7.666014,-8.307139,-5.735150,-2.950989,1.434178,3.053122,8.767399,-7.375364,-9.675402,-5.872555,-9.867396,-7.599028,2.450598,5.225143,1.609953,4.316140,3.807186,-1.533847,-0.580939,-2.525776,-7.131064,-2.510638,-6.069800,-0.799830,-3.654707,5.303218,-8.855828,-6.105579,0.558932,-3.711114,-8.852561,-5.637704,2.606629,1.937321,2.692266,9.003874,1.455753,8.683580,-6.142041,-2.767914], dtype = "float64")#candidate|4396|(1456,)|const|float64
call_4395 = relay.TupleGetItem(func_3090_call(relay.reshape(const_4396.astype('float64'), [13, 7, 16])), 0)
call_4397 = relay.TupleGetItem(func_3093_call(relay.reshape(const_4396.astype('float64'), [13, 7, 16])), 0)
func_3426_call = mod.get_global_var('func_3426')
func_3428_call = mutated_mod.get_global_var('func_3428')
call_4408 = relay.TupleGetItem(func_3426_call(), 4)
call_4409 = relay.TupleGetItem(func_3428_call(), 4)
output = relay.Tuple([call_4365,var_4366,uop_4377,call_4395,const_4396,call_4408,])
output2 = relay.Tuple([call_4367,var_4366,uop_4377,call_4397,const_4396,call_4409,])
func_4410 = relay.Function([var_4361,var_4366,], output)
mod['func_4410'] = func_4410
mod = relay.transform.InferType()(mod)
mutated_mod['func_4410'] = func_4410
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4410_call = mutated_mod.get_global_var('func_4410')
var_4412 = relay.var("var_4412", dtype = "float64", shape = (6, 4, 10))#candidate|4412|(6, 4, 10)|var|float64
var_4413 = relay.var("var_4413", dtype = "bool", shape = (225, 1))#candidate|4413|(225, 1)|var|bool
call_4411 = func_4410_call(var_4412,var_4413,)
output = call_4411
func_4414 = relay.Function([var_4412,var_4413,], output)
mutated_mod['func_4414'] = func_4414
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3712_call = mod.get_global_var('func_3712')
func_3713_call = mutated_mod.get_global_var('func_3713')
call_4447 = func_3712_call()
call_4448 = func_3712_call()
output = relay.Tuple([call_4447,])
output2 = relay.Tuple([call_4448,])
func_4457 = relay.Function([], output)
mod['func_4457'] = func_4457
mod = relay.transform.InferType()(mod)
output = func_4457()
func_4458 = relay.Function([], output)
mutated_mod['func_4458'] = func_4458
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4077_call = mod.get_global_var('func_4077')
func_4078_call = mutated_mod.get_global_var('func_4078')
call_4495 = relay.TupleGetItem(func_4077_call(), 0)
call_4496 = relay.TupleGetItem(func_4078_call(), 0)
func_3712_call = mod.get_global_var('func_3712')
func_3713_call = mutated_mod.get_global_var('func_3713')
call_4505 = func_3712_call()
call_4506 = func_3712_call()
output = relay.Tuple([call_4495,call_4505,])
output2 = relay.Tuple([call_4496,call_4506,])
func_4521 = relay.Function([], output)
mod['func_4521'] = func_4521
mod = relay.transform.InferType()(mod)
output = func_4521()
func_4522 = relay.Function([], output)
mutated_mod['func_4522'] = func_4522
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4225_call = mod.get_global_var('func_4225')
func_4227_call = mutated_mod.get_global_var('func_4227')
call_4533 = relay.TupleGetItem(func_4225_call(), 0)
call_4534 = relay.TupleGetItem(func_4227_call(), 0)
uop_4541 = relay.sin(call_4533.astype('float64')) # shape=(16, 5, 7)
uop_4543 = relay.sin(call_4534.astype('float64')) # shape=(16, 5, 7)
output = uop_4541
output2 = uop_4543
func_4558 = relay.Function([], output)
mod['func_4558'] = func_4558
mod = relay.transform.InferType()(mod)
mutated_mod['func_4558'] = func_4558
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4558_call = mutated_mod.get_global_var('func_4558')
call_4559 = func_4558_call()
output = call_4559
func_4560 = relay.Function([], output)
mutated_mod['func_4560'] = func_4560
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3479_call = mod.get_global_var('func_3479')
func_3480_call = mutated_mod.get_global_var('func_3480')
call_4633 = func_3479_call()
call_4634 = func_3479_call()
output = relay.Tuple([call_4633,])
output2 = relay.Tuple([call_4634,])
func_4639 = relay.Function([], output)
mod['func_4639'] = func_4639
mod = relay.transform.InferType()(mod)
mutated_mod['func_4639'] = func_4639
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4639_call = mutated_mod.get_global_var('func_4639')
call_4640 = func_4639_call()
output = call_4640
func_4641 = relay.Function([], output)
mutated_mod['func_4641'] = func_4641
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3905_call = mod.get_global_var('func_3905')
func_3906_call = mutated_mod.get_global_var('func_3906')
call_4655 = func_3905_call()
call_4656 = func_3905_call()
func_3946_call = mod.get_global_var('func_3946')
func_3947_call = mutated_mod.get_global_var('func_3947')
call_4660 = relay.TupleGetItem(func_3946_call(), 0)
call_4661 = relay.TupleGetItem(func_3947_call(), 0)
func_633_call = mod.get_global_var('func_633')
func_635_call = mutated_mod.get_global_var('func_635')
const_4666 = relay.const([False,True,False,False,False,True,False,True,False,True,True,True,False,False,True,True,False,True,False,False,True,False,True,True,True,False,True,False,False,True,False,True,False,False,True,False,False,True,True,False,False,False,False,True,True,True,False,True,False,False,False,False,False,True,True,True,True,False,True,False,True,True,True,True,False,False,True,False,True,False,False,True,True,False,False,False,True,False,True,False,False,True,False,False,True,True,True,False,False,False,False,True,False,True,True,False,True,False,False,False,True,False,False,False,True,False,False,False,True,True,False,True,True,False,False,False,False,True,False,False,False,True,True,False,False,False,False,False,True,False,False,False,False,False,False,True,True,False,False,False,True,False,True,False,True,True,False,True,True,True,True,True,False,False,True,False,True,True,False,False,True,True,False,True,True,False,True,False,False,True,False,True,True,False,False,False,True,False,True,False,True,False,True,True,True,False,False,False,True,False,False,False,True,False,False,True,False,True,True,False,False,False,True,True,False,True,False,True,False,True,False,True,False,True,True,True,False,True,True,True,True,True,False,True,True], dtype = "bool")#candidate|4666|(225,)|const|bool
call_4665 = relay.TupleGetItem(func_633_call(relay.reshape(const_4666.astype('bool'), [5, 9, 5])), 2)
call_4667 = relay.TupleGetItem(func_635_call(relay.reshape(const_4666.astype('bool'), [5, 9, 5])), 2)
func_3090_call = mod.get_global_var('func_3090')
func_3093_call = mutated_mod.get_global_var('func_3093')
const_4674 = relay.const([-1.838335,0.280485,-1.716734,9.636402,8.998034,-7.585113,-1.978000,7.695309,0.123181,9.417546,4.261022,3.718229,-8.683228,-5.300703,-0.075913,6.736548,0.532823,-9.962845,1.498751,2.036722,1.678583,9.319657,-7.594452,-9.170166,3.172873,-9.355194,0.180340,8.875348,-3.852737,-6.614616,0.285798,2.963297,-0.709183,0.218585,5.184014,-4.123941,-8.257591,-3.811732,-7.182543,-0.986259,-6.967404,-9.502429,-2.427753,3.650691,9.463483,5.104234,4.842607,8.602509,-7.871865,7.962244,-6.111188,8.742806,-7.874435,3.692688,-5.781925,-5.688282,-1.902846,3.168294,-3.990823,9.660273,-6.254894,7.816740,7.992371,1.011773,6.617311,8.103203,7.552856,-9.058070,-2.387011,-5.372931,5.475130,2.904618,-2.439120,-1.263761,8.404184,-2.772853,-7.716172,4.856602,0.864983,-8.880121,3.151303,-9.930846,-7.008309,-1.184505,-8.851949,0.695887,-6.484334,8.691322,4.526360,5.575825,6.642904,-7.628190,8.193446,3.970396,7.733884,9.187956,6.783504,1.992621,-2.058927,-5.015190,-6.575604,-1.414080,-9.398590,8.095567,6.588734,-1.781048,7.737656,4.829716,-3.220971,2.360323,-7.997871,-7.663913,-4.096825,7.035637,-7.386947,8.157104,5.168613,0.843255,1.841233,-7.381027,9.946340,4.687264,2.718328,-3.786699,0.442381,2.646260,-5.860307,5.401449,6.287848,-8.883555,-4.392920,7.544757,3.639242,9.951157,2.768775,-1.843387,-9.994569,1.638247,-2.858413,9.648107,5.417227,9.653436,-5.964901,-5.075449,5.669198,3.474180,-0.800731,8.009316,6.285340,-4.597518,-9.267653,-8.536338,-0.015417,4.962276,2.971966,-7.687684,9.630886,-7.220871,-4.703593,-7.629200,9.222641,7.847477,-9.464044,-7.931409,0.975588,-9.885677,7.196791,-8.412455,0.911029,-0.344829,-9.267927,4.552101,-9.447705,-0.797886,4.858685,-9.953583,-3.009275,-5.573195,-9.651090,8.524842,-3.285419,-1.215573,-9.997241,8.081677,-4.996384,-9.003934,6.822670,-5.510583,3.578018,-9.774592,5.228607,-9.043148,6.637710,-6.909738,6.911295,1.120562,-0.052664,3.362472,2.537372,-8.713211,-7.927336,-7.605143,-6.272978,4.662496,4.748323,-3.209104,-3.709501,7.480180,-6.839936,8.133992,3.765972,4.380734,-6.776726,-1.686585,6.139675,6.086064,0.351412,7.036682,4.735540,1.219135,6.552217,3.435510,-3.365358,5.148187,6.638389,-2.781270,6.627000,-7.785407,-5.404419,7.902386,8.390605,5.993321,2.708659,-7.201442,7.879279,6.926872,-4.340037,-4.025505,7.763885,7.756434,6.819300,1.514243,0.418957,-1.181692,-3.865752,2.735984,6.109866,-4.940126,-0.899895,7.139567,0.076024,-6.939622,7.107066,-7.950044,-8.965641,6.272405,-7.206586,-7.955872,-4.423263,0.345036,1.476128,-5.912469,-8.525911,6.406992,-4.939098,-3.098052,5.174258,7.338730,-2.707913,-7.635156,2.796694,-3.413576,-8.759558,7.617476,4.930362,-7.275349,3.951785,3.528901,0.746111,-3.188853,0.487802,5.610720,9.474982,-6.722503,6.204413,-7.246615,-5.561184,-0.616474,-3.821739,-2.842525,-3.476973,-4.554633,0.757256,9.841400,-2.162533,-8.106599,3.492257,-4.059564,-9.435904,-7.640962,9.169387,-2.333234,9.366067,8.947593,-9.678823,5.954979,-8.501206,5.265972,-2.248246,-6.875332,-7.734685,-1.789232,0.300755,9.679605,9.095781,0.397148,-5.788738,8.937917,-9.490914,5.236165,-9.897769,0.671635,-8.620954,-6.893694,-4.910980,2.450156,-4.044953,-7.108863,6.990157,5.718760,5.220975,1.529611,4.742370,2.225150,7.782693,-3.779354,7.729483,-2.091585,-9.185710,-2.536590,-8.382225,-4.780434,-7.207528,-1.103157,-5.840596,-1.093909,-4.085136,7.359165,-4.990514,2.288501,-9.876289,6.539924,4.998077,2.701694,0.431515,-6.800685,-7.905939,-0.791325,9.592654,-1.766329,-5.618743,2.046876,-4.019075,-0.627257,5.018123,4.911608,-4.034406,-7.590578,-2.028800,1.061590,4.288350,2.294041,-7.079385,-5.425751,-4.132874,1.889285,-8.169831,0.787087,-2.719173,9.167344,4.450062,1.895177,-9.226569,-5.658115,6.130472,-7.361564,1.206417,-4.911888,3.543179,-7.224678,6.936571,-4.592591,-6.626831,6.953727,-8.959138,2.923918,2.004930,2.848343,-2.881503,-8.540910,8.166440,-8.454446,7.800038,5.632492,-3.348738,-6.294324,1.075837,0.646908,9.598839,-9.002985,3.418201,0.969118,-4.067928,-4.049678,-0.445356,6.866338,1.338826,0.642966,-9.442084,0.320067,-5.850748,1.791553,9.625137,0.413263,8.944809,-0.971817,0.719780,0.250395,-4.620501,-9.434916,-7.604512,-3.504878,-9.068553,-7.357562,-9.826257,8.181470,-7.150300,6.960495,3.836252,-2.119849,-9.505152,3.616431,-1.523713,-2.151099,9.196604,-3.642888,-3.756839,2.615332,-9.782176,6.034021,-5.712134,1.670825,6.452684,-2.755575,6.016407,8.156885,9.413136,-1.624961,5.766374,-2.707303,1.865613,3.848502,9.618703,-5.114665,-7.283130,3.026747,-3.360583,2.619959,0.824741,-8.729499,-0.368651,-8.210067,4.523420,-5.044910,1.815719,9.286148,3.073883,-0.036841,3.718216,-3.853355,8.799508,-6.803420,-0.628607,2.736928,6.858133,-5.234775,-5.100072,1.741440,0.948794,-9.348966,-8.610640,-0.713725,-7.389453,4.793159,4.743786,-7.690036,8.978076,6.881924,-9.936721,5.826005,-8.135490,-4.409263,-9.386643,-3.384809,9.170605,9.247767,-1.626042,8.439270,-0.014562,8.458204,-6.337136,-0.735832,-3.920287,3.900928,5.139914,3.895317,-9.639253,-6.417367,9.426828,2.282247,4.831618,9.806708,-1.061010,1.010899,2.795852,-0.690919,-7.748452,7.566001,-0.758760,0.155427,2.658205,-8.102155,-9.167374,-3.287384,3.288696,-6.256185,-6.425534,0.448663,-1.132296,-3.351912,6.997436,2.048134,3.157402,-6.597036,4.882065,3.714813,-7.963048,4.185381,-3.899246,4.937176,2.090505,9.527639,6.877752,-2.737675,2.507113,8.020648,8.412129,-7.752205,7.984896,8.474474,-9.918550,5.060618,-1.093602,-8.055645,-3.124396,-0.671190,9.577051,-3.346771,-7.299787,9.374117,9.573284,-5.259357,7.366024,0.426983,-4.069591,-5.961545,-2.340659,9.879206,-8.432872,6.006813,6.743589,-6.220014,2.353885,5.609775,5.715707,5.547582,5.405113,3.415363,-0.117915,0.581805,5.843337,-3.121740,3.153848,-1.045532,2.698275,4.757256,-3.609274,5.785868,-6.415555,8.117178,1.392028,-3.011513,4.468344,-4.432641,-3.475870,-2.834241,3.803761,6.677888,-9.762176,-8.144730,-6.427023,8.906866,2.548435,-1.110521,5.145049,4.438636,8.746025,-9.668228,7.147712,-2.936552,-4.267936,-2.138953,7.032323,2.356421,0.043686,1.386289,8.062771,-6.913948,-7.024687,-7.674173,5.983970,-3.104065,6.516400,8.672133,3.529036,-9.792360,-0.896187,6.248299,1.761305,1.617715,-4.596178,-4.238351,1.146491,-1.409271,4.202737,-8.762698,-2.769467,0.859719,3.236667,4.518437,7.615095,-8.097988,-0.030997,8.067590,-6.392022,-7.419290,-8.694396,-0.539461,-0.486819,1.436276,5.996801,-9.497897,-7.653640,8.978397,-3.787787,4.693160,0.754645,9.163286,6.855003,1.675846,9.563431,1.772332,-9.363010,-7.559289,-3.185380,-0.070782,0.725729,-9.562898,9.846477,4.284188,-4.506431,7.695885,-7.690528,1.345051,1.553707,-4.296994,-4.566765,-8.561082,8.755660,3.103522,-5.231348,-8.039757,-7.592369,-9.188749,-4.141602,0.187210,-6.710949,-6.410608,7.641906,-0.096890,-9.071678,-5.889673,-0.564121,9.704140,7.806460,-8.883629,4.869247,9.695689,2.050194,0.912152,6.754251,-4.130884,8.764019,-7.083543,-8.144002,4.792954,8.938607,9.800223,2.407708,-5.594759,-4.018249,-4.861113,0.251546,1.092920,4.421605,-2.871929,-6.651119,-6.308822,-5.365496,-4.647100,-3.228294,0.878163,8.089234,9.818492,-7.544533,1.764541,-7.284207,-0.918132,1.780632,-8.240088,-3.531648,9.009913,3.461342,-0.401830,9.350404,-3.970076,-0.757249,6.829348,4.843104,-0.270886,-8.070287,-7.412484,-5.305034,-5.780888,-0.900077,-6.890016,-9.279368,1.286499,-2.121129,0.881993,8.040957,4.938718,2.331327,1.480738,9.009816,-9.944112,-9.608790,1.910235,3.673270,-1.858026,-9.285247,-5.604650,3.703667,5.102471,7.519149,7.527232,-9.063791,0.365043,3.364668,-1.503170,-1.918358,4.874048,4.636877,5.341517,-6.108907,1.211084,1.671415,7.614921,2.439565,-3.131271,8.966389,2.008797,-8.221027,-9.513900,-7.549276,-5.182924,0.592006,2.010570,-1.271531,-4.693934,-2.610080,-3.649545,4.661367,-2.963673,-7.762448,-7.130192,-6.388034,4.677935,-3.328661,7.081870,3.910768,0.121917,7.389023,5.132796,-4.878426,-7.246116,9.634380,-5.949959,5.739939,-5.999698,1.076311,0.300301,-5.928172,-8.411329,-6.936630,4.187210,8.736825,8.578473,2.986552,3.097873,-0.509421,4.969209,-9.091487,-7.311265,-6.997872,8.470003,6.880656,-1.374021,0.608519,-3.332519,-6.905171,6.887914,4.103160,-2.480537,-1.698997,-5.232928,8.342175,-3.588934,2.309544,9.043660,9.847933,6.504605,-8.125709,0.751562,-9.032082,4.766931,6.212132,-3.347882,8.829121,-1.098947,-3.973465,-7.794498,-5.231224,9.271029,-4.302213,2.670043,0.831064,-8.115859,-7.323243,-5.982912,-8.823252,4.830939,-6.024188,-9.266102,-3.095289,1.531935,1.284412,2.366187,1.736445,0.645211,3.591427,0.723690,6.469665,-1.312867,3.415445,-1.926509,8.875853,-6.832197,3.436656,9.309336,5.620181,2.022653,8.293510,-0.088574,8.494399,-8.757957,-4.286693,-0.935251,7.031398,-2.626674,5.165912,-7.584923,-0.778199,-6.969848,1.656571,-5.343053,8.328640,6.516808,-9.564127,4.000846,9.060010,-7.948224,0.789039,7.169577,-6.546427,-2.017014,-5.188390,-6.625898,3.000899,1.404692,-3.439182,1.325991,4.900008,-9.500921,-7.666997,9.679031,8.264572,0.164241,-4.755056,-4.929321,-9.022175,-7.301292,0.465466,-9.311472,-5.889964,-1.664467,3.297625,-3.896927,-4.655949,-2.423473,-0.460984,3.953240,2.345291,-2.862822,1.238012,-3.697586,6.137442,7.597632,3.409684,6.927496,7.904052,8.252743,5.503742,2.207259,-5.427405,-2.663211,2.459909,6.821751,2.073642,9.530916,-6.985373,-6.704822,-0.921796,-7.305593,7.610737,0.166737,5.791585,3.805540,-2.515174,7.411102,-8.028288,1.711545,2.912431,0.009164,4.642436,7.992224,-5.864888,7.209745,1.774141,7.074513,-7.539178,6.285490,2.940072,-4.631485,2.044567,-9.875877,-3.761758,-1.566314,-7.003823,-1.784555,-3.193313,7.450279,1.864482,4.685716,0.217082,-9.599583,-8.621593,2.566790,-7.073240,4.524890,8.775029,-3.014875,-1.215609,9.588520,-1.190508,-7.404156,-3.261432,0.704376,-8.176607,-0.388585,6.447552,6.646024,1.581097,1.653209,4.897974,3.968783,1.576299,-0.121293,-9.304194,-2.266045,2.701015,4.404384,2.425954,2.521348,-7.038189,3.708647,-5.143865,9.299531,4.622589,-7.344920,5.047612,-5.550584,1.188973,-5.537820,-8.401667,-1.221601,9.311624,1.183570,-7.812985,9.701908,3.527821,6.999774,2.294854,6.890151,6.343405,1.404372,9.343779,1.207187,-2.559659,7.488460,3.322023,-2.764663,0.396018,7.273362,2.354882,-1.009461,0.504412,-3.465037,-3.614632,6.559674,2.615694,2.934561,-2.255905,0.982221,-2.742883,-8.032581,-2.357144,2.173341,-7.584328,-8.497698,5.572993,-1.279575,-2.002448,8.835101,-5.332004,-2.648617,-1.008487,6.080135,8.375594,8.525901,9.665788,0.386562,3.386463,3.143158,9.536660,3.816179,2.136553,3.490714,-4.370611,-8.644166,5.070107,5.764427,-1.888807,5.413597,7.618763,-6.419430,-1.989806,3.011840,-6.415527,2.138959,-5.880265,-9.335277,2.612853,0.141768,-6.495991,-5.106944,-4.276207,6.004626,-4.892186,-2.910185,-1.921682,-7.800568,-8.996266,-7.327374,1.271215,-4.316734,-1.996281,1.730907,-9.382119,9.938723,-0.080374,9.525089,9.007330,-4.368302,4.964837,-5.135406,5.345621,-6.449085,-6.989498,-0.904195,-1.344267,0.015641,1.711667,-3.260260,0.512411,-1.725974,-3.154804,-1.135874,5.725527,2.344634,-8.653708,-4.782051,7.143316,7.803039,4.270747,5.358636,8.684659,-5.092831,2.941682,-8.120762,-0.075869,-4.763035,-8.130312,9.411108,8.452975,-8.362009,-3.589849,1.912117,3.625154,5.490634,-1.774584,5.753810,5.172440,-7.396429,-8.143448,3.040670,-2.880934,4.972017,-6.118690,-5.971296,-7.535221,4.758974,0.260614,-2.785727,-3.414783,5.481453,-8.465635,-2.185913,-4.341945,-3.341520,6.508965,3.478987,8.415410,1.127973,9.296319,-0.716910,-8.476419,-2.762440,-6.624482,2.907411,-6.095579,-5.880510,6.549134,-7.890601,3.622618,-5.540271,-9.070709,-1.148254,7.236588,-5.653983,5.488846,-4.877611,-5.444861,8.343936,1.150245,7.507382,6.229799,-5.076891,-9.721536,-5.203893,1.339851,9.047470,9.934963,9.555251,0.422510,8.905093,-6.038896,-8.875233,4.957058,-9.267024,-5.045251,-7.046356,3.414305,-8.940260,-1.637686,3.397835,-2.816936,9.396129,6.002926,-1.106455,-7.493325,1.096439,4.028840,-2.707193,-7.537564,5.127782,-0.091250,-8.886227,-3.681958,-6.249274,-2.681747,-6.889825,-4.128906,-0.784530,-2.089946,-9.773341,-7.899125,-9.460695,3.480810,-9.129701,8.374872,4.959669,-5.528480,0.193417,-6.760875,6.004291,0.509236,1.607074,3.092789,3.007452,-7.859977,7.757734,-1.341221,-4.237489,-5.816227,1.354305,-7.842579,2.312783,-7.677606,7.380572,-8.604806,7.839853,-4.015322,5.360035,-2.077448,-3.766463,-4.685109,-5.226570,8.133171,1.996702,1.943100,8.051734,0.094807,-1.897772,8.603829,-6.874062,-2.168825,7.584094,2.401595,4.437222,-1.126485,-4.411034,8.069863,3.527808,-4.513289,-6.488645,4.353533,3.746998,-6.310876,-2.501809,-5.722086,-7.251099,8.297724,1.352943,-3.069196,-0.621402,-1.464868,-3.618791,9.569635,-2.048972,-4.460209,-5.131292,-8.439530,-6.371872,4.361153,-2.044107,4.601596,0.041446,2.305134,5.972652,8.675998,-0.560691,3.636092,8.873850,-1.248805,-1.092132,-7.225514,-1.586805,-2.838212,4.134059,3.019935,9.022924,-3.578787,3.285889,-4.535803,-0.829107,9.932742,3.354976,0.644794,0.162056,7.087119,-6.720794,-5.800659,-8.212863,4.708398,4.999647,-4.382053,3.613838,0.247278,-6.973673,-5.551193,4.945046,1.949092,-5.359822,5.937271,-9.400883,9.937230,-8.778701,9.832616,-4.680286,-7.874480,8.274849,8.113208,-2.493550,-9.755042,-6.816125,4.070890,-7.315292,-4.653964,0.058622,-2.603172,-8.624188,-9.185094,-9.003186,-8.048027,-4.593593,-4.630876,3.426231,-4.183628,-0.013710,-4.250132,9.095744,-2.976859,-8.003837,-6.601406,-3.036139,9.071452,-9.351913,7.290615,6.989481,-5.620073,-2.518116,1.881816,-1.110052,2.069095,-8.126691,5.980647,4.287582,2.763838,-6.477385,4.189880,8.884987,-3.672805,-1.313719,-9.674671,8.598737,4.911745,3.387696,1.069861,4.731414,-5.602975,-3.293584,6.577405,9.658963,5.762445,9.446993,-7.425994,3.766351,-4.315084,-5.515868,4.403511,1.269226,2.591575,7.176090,-3.630180,-7.153454,6.903845,-0.724338,-3.616448,5.630681,-9.814861,7.403139,5.458237,5.896138,-7.661187,-7.983004,4.563499,8.504812,-8.158337,9.899028,2.287373,1.350837,-0.254434,6.958786,7.681875,-9.306761,0.553628,-8.570134,-7.269017,2.270180,8.900456,-7.503367,8.542351,-7.100354,-4.589077,9.596508], dtype = "float64")#candidate|4674|(1456,)|const|float64
call_4673 = relay.TupleGetItem(func_3090_call(relay.reshape(const_4674.astype('float64'), [13, 7, 16])), 0)
call_4675 = relay.TupleGetItem(func_3093_call(relay.reshape(const_4674.astype('float64'), [13, 7, 16])), 0)
output = relay.Tuple([call_4655,call_4660,call_4665,const_4666,call_4673,const_4674,])
output2 = relay.Tuple([call_4656,call_4661,call_4667,const_4666,call_4675,const_4674,])
func_4683 = relay.Function([], output)
mod['func_4683'] = func_4683
mod = relay.transform.InferType()(mod)
mutated_mod['func_4683'] = func_4683
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4683_call = mutated_mod.get_global_var('func_4683')
call_4684 = func_4683_call()
output = call_4684
func_4685 = relay.Function([], output)
mutated_mod['func_4685'] = func_4685
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4558_call = mod.get_global_var('func_4558')
func_4560_call = mutated_mod.get_global_var('func_4560')
call_4686 = func_4558_call()
call_4687 = func_4558_call()
uop_4688 = relay.sinh(call_4686.astype('float64')) # shape=(16, 5, 7)
uop_4690 = relay.sinh(call_4687.astype('float64')) # shape=(16, 5, 7)
func_4639_call = mod.get_global_var('func_4639')
func_4641_call = mutated_mod.get_global_var('func_4641')
call_4701 = relay.TupleGetItem(func_4639_call(), 0)
call_4702 = relay.TupleGetItem(func_4641_call(), 0)
func_4457_call = mod.get_global_var('func_4457')
func_4458_call = mutated_mod.get_global_var('func_4458')
call_4720 = relay.TupleGetItem(func_4457_call(), 0)
call_4721 = relay.TupleGetItem(func_4458_call(), 0)
output = relay.Tuple([uop_4688,call_4701,call_4720,])
output2 = relay.Tuple([uop_4690,call_4702,call_4721,])
func_4722 = relay.Function([], output)
mod['func_4722'] = func_4722
mod = relay.transform.InferType()(mod)
output = func_4722()
func_4723 = relay.Function([], output)
mutated_mod['func_4723'] = func_4723
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3905_call = mod.get_global_var('func_3905')
func_3906_call = mutated_mod.get_global_var('func_3906')
call_4768 = func_3905_call()
call_4769 = func_3905_call()
output = relay.Tuple([call_4768,])
output2 = relay.Tuple([call_4769,])
func_4780 = relay.Function([], output)
mod['func_4780'] = func_4780
mod = relay.transform.InferType()(mod)
mutated_mod['func_4780'] = func_4780
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4780_call = mutated_mod.get_global_var('func_4780')
call_4781 = func_4780_call()
output = call_4781
func_4782 = relay.Function([], output)
mutated_mod['func_4782'] = func_4782
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4722_call = mod.get_global_var('func_4722')
func_4723_call = mutated_mod.get_global_var('func_4723')
call_4888 = relay.TupleGetItem(func_4722_call(), 2)
call_4889 = relay.TupleGetItem(func_4723_call(), 2)
uop_4900 = relay.log10(call_4888.astype('float32')) # shape=(2, 336)
uop_4902 = relay.log10(call_4889.astype('float32')) # shape=(2, 336)
bop_4913 = relay.logical_and(uop_4900.astype('bool'), relay.reshape(call_4888.astype('bool'), relay.shape_of(uop_4900))) # shape=(2, 336)
bop_4916 = relay.logical_and(uop_4902.astype('bool'), relay.reshape(call_4889.astype('bool'), relay.shape_of(uop_4902))) # shape=(2, 336)
bop_4917 = relay.subtract(uop_4900.astype('uint64'), relay.reshape(bop_4913.astype('uint64'), relay.shape_of(uop_4900))) # shape=(2, 336)
bop_4920 = relay.subtract(uop_4902.astype('uint64'), relay.reshape(bop_4916.astype('uint64'), relay.shape_of(uop_4902))) # shape=(2, 336)
func_3681_call = mod.get_global_var('func_3681')
func_3684_call = mutated_mod.get_global_var('func_3684')
const_4924 = relay.const([[-6.802827,0.108040,2.221726,0.709572,-2.851169,5.884953,-8.865136,-5.969708,9.338104,7.377338,-2.060747,-5.843934,8.903719,-6.849045,-8.171919,9.944480,-9.920447,-9.101117,0.243704,-7.891832,8.300779,-7.578498,1.338290,4.360210,-6.088507,5.451435,3.204312,-9.870431,0.618330,2.200846,-6.251108,-2.553847,4.133936,5.062472,-3.402147,-6.804428,3.313533,-3.617657,6.982717,1.070460,-0.382904,-9.698017,9.822386,-5.006287,-4.268139,-4.748267,-9.785206,2.040703,-3.711562,-4.126960,-5.938550,-2.151711,9.674978,-3.642420,-1.900365,-6.461607,-5.004510,7.483689,-4.703841,-1.380217,3.593091,9.582825,8.047032,8.688198,3.568225,-7.933490,-8.137239,2.899285,6.340861,8.943792,-0.335579,-3.558006,-5.394226,-0.830986,2.738971,6.303199,4.841438,-3.587383,7.567855,-2.491732,0.987178,-0.271300,5.265637,1.288410,8.704295,7.255328,6.783327,-2.813495,8.792532,-6.556853,6.117607,9.280338,-7.899663,4.664974,6.457064,8.925681]], dtype = "float32")#candidate|4924|(1, 96)|const|float32
call_4923 = relay.TupleGetItem(func_3681_call(relay.reshape(const_4924.astype('float32'), [8, 12])), 1)
call_4925 = relay.TupleGetItem(func_3684_call(relay.reshape(const_4924.astype('float32'), [8, 12])), 1)
bop_4935 = relay.equal(bop_4917.astype('bool'), relay.reshape(uop_4900.astype('bool'), relay.shape_of(bop_4917))) # shape=(2, 336)
bop_4938 = relay.equal(bop_4920.astype('bool'), relay.reshape(uop_4902.astype('bool'), relay.shape_of(bop_4920))) # shape=(2, 336)
func_633_call = mod.get_global_var('func_633')
func_635_call = mutated_mod.get_global_var('func_635')
var_4949 = relay.var("var_4949", dtype = "bool", shape = (25, 9))#candidate|4949|(25, 9)|var|bool
call_4948 = relay.TupleGetItem(func_633_call(relay.reshape(var_4949.astype('bool'), [5, 9, 5])), 2)
call_4950 = relay.TupleGetItem(func_635_call(relay.reshape(var_4949.astype('bool'), [5, 9, 5])), 2)
output = relay.Tuple([call_4923,const_4924,bop_4935,call_4948,var_4949,])
output2 = relay.Tuple([call_4925,const_4924,bop_4938,call_4950,var_4949,])
func_4962 = relay.Function([var_4949,], output)
mod['func_4962'] = func_4962
mod = relay.transform.InferType()(mod)
var_4963 = relay.var("var_4963", dtype = "bool", shape = (25, 9))#candidate|4963|(25, 9)|var|bool
output = func_4962(var_4963)
func_4964 = relay.Function([var_4963], output)
mutated_mod['func_4964'] = func_4964
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3712_call = mod.get_global_var('func_3712')
func_3713_call = mutated_mod.get_global_var('func_3713')
call_4968 = func_3712_call()
call_4969 = func_3712_call()
func_633_call = mod.get_global_var('func_633')
func_635_call = mutated_mod.get_global_var('func_635')
var_4973 = relay.var("var_4973", dtype = "bool", shape = (225,))#candidate|4973|(225,)|var|bool
call_4972 = relay.TupleGetItem(func_633_call(relay.reshape(var_4973.astype('bool'), [5, 9, 5])), 1)
call_4974 = relay.TupleGetItem(func_635_call(relay.reshape(var_4973.astype('bool'), [5, 9, 5])), 1)
output = relay.Tuple([call_4968,call_4972,var_4973,])
output2 = relay.Tuple([call_4969,call_4974,var_4973,])
func_4975 = relay.Function([var_4973,], output)
mod['func_4975'] = func_4975
mod = relay.transform.InferType()(mod)
var_4976 = relay.var("var_4976", dtype = "bool", shape = (225,))#candidate|4976|(225,)|var|bool
output = func_4975(var_4976)
func_4977 = relay.Function([var_4976], output)
mutated_mod['func_4977'] = func_4977
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4722_call = mod.get_global_var('func_4722')
func_4723_call = mutated_mod.get_global_var('func_4723')
call_5047 = relay.TupleGetItem(func_4722_call(), 0)
call_5048 = relay.TupleGetItem(func_4723_call(), 0)
output = relay.Tuple([call_5047,])
output2 = relay.Tuple([call_5048,])
func_5057 = relay.Function([], output)
mod['func_5057'] = func_5057
mod = relay.transform.InferType()(mod)
output = func_5057()
func_5058 = relay.Function([], output)
mutated_mod['func_5058'] = func_5058
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5057_call = mod.get_global_var('func_5057')
func_5058_call = mutated_mod.get_global_var('func_5058')
call_5231 = relay.TupleGetItem(func_5057_call(), 0)
call_5232 = relay.TupleGetItem(func_5058_call(), 0)
output = call_5231
output2 = call_5232
func_5268 = relay.Function([], output)
mod['func_5268'] = func_5268
mod = relay.transform.InferType()(mod)
output = func_5268()
func_5269 = relay.Function([], output)
mutated_mod['func_5269'] = func_5269
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4722_call = mod.get_global_var('func_4722')
func_4723_call = mutated_mod.get_global_var('func_4723')
call_5280 = relay.TupleGetItem(func_4722_call(), 0)
call_5281 = relay.TupleGetItem(func_4723_call(), 0)
func_4521_call = mod.get_global_var('func_4521')
func_4522_call = mutated_mod.get_global_var('func_4522')
call_5297 = relay.TupleGetItem(func_4521_call(), 0)
call_5298 = relay.TupleGetItem(func_4522_call(), 0)
func_4225_call = mod.get_global_var('func_4225')
func_4227_call = mutated_mod.get_global_var('func_4227')
call_5309 = relay.TupleGetItem(func_4225_call(), 0)
call_5310 = relay.TupleGetItem(func_4227_call(), 0)
output = relay.Tuple([call_5280,call_5297,call_5309,])
output2 = relay.Tuple([call_5281,call_5298,call_5310,])
func_5317 = relay.Function([], output)
mod['func_5317'] = func_5317
mod = relay.transform.InferType()(mod)
output = func_5317()
func_5318 = relay.Function([], output)
mutated_mod['func_5318'] = func_5318
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4077_call = mod.get_global_var('func_4077')
func_4078_call = mutated_mod.get_global_var('func_4078')
call_5324 = relay.TupleGetItem(func_4077_call(), 0)
call_5325 = relay.TupleGetItem(func_4078_call(), 0)
output = relay.Tuple([call_5324,])
output2 = relay.Tuple([call_5325,])
func_5338 = relay.Function([], output)
mod['func_5338'] = func_5338
mod = relay.transform.InferType()(mod)
output = func_5338()
func_5339 = relay.Function([], output)
mutated_mod['func_5339'] = func_5339
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5268_call = mod.get_global_var('func_5268')
func_5269_call = mutated_mod.get_global_var('func_5269')
call_5349 = func_5268_call()
call_5350 = func_5268_call()
uop_5356 = relay.asin(call_5349.astype('float64')) # shape=(16, 5, 7)
uop_5358 = relay.asin(call_5350.astype('float64')) # shape=(16, 5, 7)
output = uop_5356
output2 = uop_5358
func_5366 = relay.Function([], output)
mod['func_5366'] = func_5366
mod = relay.transform.InferType()(mod)
mutated_mod['func_5366'] = func_5366
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5366_call = mutated_mod.get_global_var('func_5366')
call_5367 = func_5366_call()
output = call_5367
func_5368 = relay.Function([], output)
mutated_mod['func_5368'] = func_5368
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4457_call = mod.get_global_var('func_4457')
func_4458_call = mutated_mod.get_global_var('func_4458')
call_5405 = relay.TupleGetItem(func_4457_call(), 0)
call_5406 = relay.TupleGetItem(func_4458_call(), 0)
uop_5409 = relay.exp(call_5405.astype('float32')) # shape=(2, 336)
uop_5411 = relay.exp(call_5406.astype('float32')) # shape=(2, 336)
const_5414 = relay.const([[-8,-4,4,-6,2,-9,-5,5,7,4,5,-9,-1,-7,-4,4,10,6,1,10,1,6,-2,2,3,1,6,-1,10,9,-1,-9,-10,6,-8,-3,-10,7,-1,3,6,2,-3,-10,-2,-10,-3,5,5,-5,10,2,-10,-3,-1,-7,-10,9,-3,-8,-10,-10,-7,-8,-6,5,-4,7,-9,7,5,-7,4,-8,-6,1,-7,3,-6,6,6,8,-2,4,-3,1,6,5,-5,6,-9,9,8,10,3,-5,-1,8,8,-7,2,1,6,-7,-8,2,10,5,-3,3,3,4,-1,-9,2,-1,4,4,9,10,-4,5,6,-5,5,5,-8,-3,-1,9,6,10,6,-1,7,2,-6,9,-9,2,-2,3,8,-10,-8,-10,1,-6,6,-3,9,-4,2,-8,8,6,-9,-2,5,-3,3,1,7,-2,-5,6,10,-2,5,-5,1,5,-10,-6,8,-10,-7,6,8,-7,-3,-10,2,5,-1,-10,-2,2,-1,7,-2,-10,-9,2,-4,-2,-9,10,-2,9,-3,-6,4,-7,10,4,-2,-10,-3,-8,-1,-6,1,-4,-8,8,3,-6,-6,2,6,8,4,-9,-10,6,5,2,5,-1,-10,-4,-5,-8,5,6,9,1,2,10,7,3,-7,10,-4,5,-3,5,-1,-8,-4,-10,-8,6,-3,4,-4,1,-4,3,3,-10,-7,4,-9,-4,1,-7,7,1,-4,9,1,-9,-1,3,-10,-2,-1,5,-3,4,-5,2,-6,1,7,-8,-9,3,9,8,2,-8,-8,-2,4,-6,-7,-2,-3,-5,-4,-7,9,-5,-8,2,2,-3,-3,-3,1,9,-10,-2,-5,-3,9,-3,2,1,-8,-1,2,-3,1,5,9,-1,-4,-2,-2,-9,-5,-3],[10,-8,-6,-1,3,5,-3,-7,4,-9,-2,1,-6,-9,5,-7,-6,3,3,2,9,-9,10,3,3,4,5,-1,8,-1,2,5,-4,-1,4,3,5,-6,-10,-10,-2,-10,10,7,1,-10,-9,-2,5,2,-9,3,-10,8,7,-5,-2,8,-8,1,-5,4,-6,-9,-10,-2,-7,-10,5,5,5,3,-6,-9,-5,6,1,-4,-6,10,5,4,9,6,-3,-8,-2,-4,-1,3,-5,-6,8,-3,-4,-10,-9,10,8,3,-9,-8,3,9,8,10,10,-8,-7,-1,-8,-1,-5,4,-8,-5,-10,-8,-6,7,-1,-5,-2,-7,6,1,1,10,4,9,10,7,-6,3,3,6,-6,3,6,6,-2,-7,-10,8,10,3,1,2,-6,1,-6,3,10,1,-8,1,5,-2,4,6,-9,-7,-9,-8,-5,-4,6,4,-3,-1,3,2,9,-10,6,-10,-5,5,-6,-2,-4,6,4,-5,7,2,9,6,8,2,4,-8,6,6,8,5,-4,1,10,-7,-1,7,-10,7,-10,3,8,-4,5,-8,-6,5,3,8,-10,-10,-3,-3,9,3,9,-3,7,3,7,-5,4,5,-3,-1,-9,6,-8,-4,-8,-8,5,4,-1,4,-10,-3,8,-2,-10,-6,5,-8,2,2,3,7,-1,7,-9,10,-9,-6,10,8,2,-8,7,-10,9,6,-1,-7,-5,-6,5,-6,8,1,-9,-7,-2,-9,-10,5,2,3,-6,8,7,6,10,8,3,8,-6,-2,-10,7,-2,3,-6,9,-9,3,-1,-9,10,-8,7,-4,1,-1,-9,-4,3,-4,6,-2,10,-10,-6,-1,8,-9,7,8,-1,2,-9,2,-4,2,-2,4,10,3,4,-2,5,-7]], dtype = "int16")#candidate|5414|(2, 336)|const|int16
bop_5415 = relay.add(call_5405.astype('uint64'), relay.reshape(const_5414.astype('uint64'), relay.shape_of(call_5405))) # shape=(2, 336)
bop_5418 = relay.add(call_5406.astype('uint64'), relay.reshape(const_5414.astype('uint64'), relay.shape_of(call_5406))) # shape=(2, 336)
func_4521_call = mod.get_global_var('func_4521')
func_4522_call = mutated_mod.get_global_var('func_4522')
call_5419 = relay.TupleGetItem(func_4521_call(), 0)
call_5420 = relay.TupleGetItem(func_4522_call(), 0)
output = relay.Tuple([uop_5409,bop_5415,call_5419,])
output2 = relay.Tuple([uop_5411,bop_5418,call_5420,])
func_5424 = relay.Function([], output)
mod['func_5424'] = func_5424
mod = relay.transform.InferType()(mod)
mutated_mod['func_5424'] = func_5424
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5424_call = mutated_mod.get_global_var('func_5424')
call_5425 = func_5424_call()
output = call_5425
func_5426 = relay.Function([], output)
mutated_mod['func_5426'] = func_5426
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4077_call = mod.get_global_var('func_4077')
func_4078_call = mutated_mod.get_global_var('func_4078')
call_5444 = relay.TupleGetItem(func_4077_call(), 0)
call_5445 = relay.TupleGetItem(func_4078_call(), 0)
output = relay.Tuple([call_5444,])
output2 = relay.Tuple([call_5445,])
func_5449 = relay.Function([], output)
mod['func_5449'] = func_5449
mod = relay.transform.InferType()(mod)
mutated_mod['func_5449'] = func_5449
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5449_call = mutated_mod.get_global_var('func_5449')
call_5450 = func_5449_call()
output = call_5450
func_5451 = relay.Function([], output)
mutated_mod['func_5451'] = func_5451
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4780_call = mod.get_global_var('func_4780')
func_4782_call = mutated_mod.get_global_var('func_4782')
call_5498 = relay.TupleGetItem(func_4780_call(), 0)
call_5499 = relay.TupleGetItem(func_4782_call(), 0)
func_5449_call = mod.get_global_var('func_5449')
func_5451_call = mutated_mod.get_global_var('func_5451')
call_5504 = relay.TupleGetItem(func_5449_call(), 0)
call_5505 = relay.TupleGetItem(func_5451_call(), 0)
output = relay.Tuple([call_5498,call_5504,])
output2 = relay.Tuple([call_5499,call_5505,])
func_5506 = relay.Function([], output)
mod['func_5506'] = func_5506
mod = relay.transform.InferType()(mod)
mutated_mod['func_5506'] = func_5506
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5506_call = mutated_mod.get_global_var('func_5506')
call_5507 = func_5506_call()
output = call_5507
func_5508 = relay.Function([], output)
mutated_mod['func_5508'] = func_5508
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5449_call = mod.get_global_var('func_5449')
func_5451_call = mutated_mod.get_global_var('func_5451')
call_5512 = relay.TupleGetItem(func_5449_call(), 0)
call_5513 = relay.TupleGetItem(func_5451_call(), 0)
func_4410_call = mod.get_global_var('func_4410')
func_4414_call = mutated_mod.get_global_var('func_4414')
const_5515 = relay.const([-9.266055,6.377925,-8.110320,-6.342067,-5.670644,-6.196935,9.475562,-0.515620,9.017241,4.060884,2.284107,0.220491,-2.023515,-9.848139,-0.416775,4.272079,-2.664437,-6.332892,3.641890,-6.610891,2.990513,7.461848,-0.537232,-4.068004,7.710581,-9.140394,-1.928375,-6.260227,-1.746674,8.854727,-4.097564,0.690180,0.709013,6.908769,-0.587873,-3.751142,2.716798,-5.625964,4.662044,4.951781,2.036037,0.493145,7.389540,-9.938136,4.524936,2.647041,9.718363,-3.370934,-8.977097,3.241370,0.717454,-0.209666,3.865261,7.078145,-1.556046,8.226876,-6.065777,7.661406,-6.577374,6.535023,9.197325,2.250894,-6.641265,-2.726287,-8.972589,5.964432,0.261291,-3.181984,7.322294,-7.411913,-9.787770,0.702303,-6.662881,-2.976630,-9.706305,-4.008785,-5.587682,-1.630551,-7.942963,4.062337,6.831757,-7.049016,2.077891,9.152762,-3.864949,-1.188915,-0.701684,-0.917874,-4.217357,0.806596,-1.507377,9.922714,-9.495111,2.208123,-7.141169,9.128835,-1.420284,-8.431734,-7.426264,-9.574624,2.938866,4.786140,-5.394470,3.890065,-4.566186,4.988357,-5.338644,-7.017620,4.073562,2.256626,-6.788860,7.530023,4.109162,-1.558950,2.818049,-8.552294,9.869448,-4.709508,0.628886,2.850040,9.272818,7.446012,1.315959,-1.678933,5.853260,-9.375479,-6.114406,-8.475850,1.405321,7.003649,1.411948,-7.570981,2.523196,-0.189172,-2.299254,-2.736567,4.496446,6.335758,7.115822,9.361201,-4.381188,1.450325,2.271798,-5.666456,-3.394582,1.596763,3.230840,6.082307,9.310842,-5.397746,4.155839,3.966642,-6.982129,4.424883,-6.198379,-6.247015,-1.203565,6.938789,-9.231213,-8.839570,3.224458,-8.227355,1.539623,8.414995,-7.222316,-5.228619,-5.919702,-8.060734,8.184037,6.637566,-7.033502,-9.136545,2.613043,-8.305982,2.066353,-5.277582,-9.980279,5.798078,-7.846700,-9.798559,-7.148663,-1.091831,-4.856210,6.388652,-6.295683,7.118721,0.311658,7.111203,5.799273,-2.512765,6.465445,8.925963,3.861082,2.304430,4.940806,-7.535073,2.677672,1.819463,5.867000,4.516133,8.898520,-5.606719,-6.339272,2.060424,8.592243,-8.126481,-3.864105,5.503525,-0.881157,-0.523057,-3.521014,-6.400046,7.733539,-1.998656,-9.573246,1.691603,-9.343590,-7.204173,3.961510,6.736514,9.569351,9.512219,0.915490,-8.055109,-9.588236,-9.712365,6.365522,-7.581357,-1.507673,-1.060870,-8.486455,-5.987736,0.579602,6.971348,-0.315148,-4.162192,-6.649417,5.955072,-8.199890,5.904216], dtype = "float64")#candidate|5515|(240,)|const|float64
var_5516 = relay.var("var_5516", dtype = "bool", shape = (225,))#candidate|5516|(225,)|var|bool
call_5514 = relay.TupleGetItem(func_4410_call(relay.reshape(const_5515.astype('float64'), [6, 4, 10]), relay.reshape(var_5516.astype('bool'), [225, 1]), ), 5)
call_5517 = relay.TupleGetItem(func_4414_call(relay.reshape(const_5515.astype('float64'), [6, 4, 10]), relay.reshape(var_5516.astype('bool'), [225, 1]), ), 5)
output = relay.Tuple([call_5512,call_5514,const_5515,var_5516,])
output2 = relay.Tuple([call_5513,call_5517,const_5515,var_5516,])
func_5534 = relay.Function([var_5516,], output)
mod['func_5534'] = func_5534
mod = relay.transform.InferType()(mod)
var_5535 = relay.var("var_5535", dtype = "bool", shape = (225,))#candidate|5535|(225,)|var|bool
output = func_5534(var_5535)
func_5536 = relay.Function([var_5535], output)
mutated_mod['func_5536'] = func_5536
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4521_call = mod.get_global_var('func_4521')
func_4522_call = mutated_mod.get_global_var('func_4522')
call_5543 = relay.TupleGetItem(func_4521_call(), 1)
call_5544 = relay.TupleGetItem(func_4522_call(), 1)
output = call_5543
output2 = call_5544
func_5545 = relay.Function([], output)
mod['func_5545'] = func_5545
mod = relay.transform.InferType()(mod)
output = func_5545()
func_5546 = relay.Function([], output)
mutated_mod['func_5546'] = func_5546
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5559 = relay.const([[[8,6,-4,9,-8,-2,-5,-5,-5,1,-2,8,-4,10,-8,3],[-10,1,1,-7,10,-3,2,-4,-10,7,-7,-6,6,1,6,3],[-7,1,-4,-5,10,9,-8,9,7,-8,2,7,9,3,-4,-1],[-1,-6,-3,-9,-1,-4,-3,-6,2,-7,9,-2,2,4,-4,-6],[9,9,-5,6,-1,6,7,6,-10,-4,7,-7,-3,-4,8,-3],[-1,3,-3,3,-1,-7,3,-8,6,-1,-9,-1,-1,-1,-4,8],[-9,1,-9,-5,3,1,-7,10,2,-8,2,-5,-8,-4,1,8],[-2,-1,3,-3,1,-6,-2,4,10,5,5,4,6,-6,9,-8],[-2,4,-8,4,3,-8,8,1,7,-9,5,6,1,-2,-5,-1],[-1,4,2,-9,-10,9,2,-6,-7,-1,-6,6,10,-8,-8,2],[2,9,4,10,-8,1,-1,8,2,10,8,-5,-4,5,-2,1],[3,-9,-9,-2,-9,4,-2,8,4,1,-6,2,1,-9,-6,-8],[-10,9,-7,-6,-6,6,5,-3,6,2,-4,9,6,10,-10,-3],[7,-10,3,-1,-8,-10,-5,-3,8,-10,-4,8,8,-1,6,9],[-6,-8,-6,-9,-7,9,-1,-10,10,1,-10,-1,7,-9,6,6],[8,10,-4,2,9,1,4,10,1,9,8,-2,-3,-10,10,10]],[[2,5,10,-5,-9,-10,-10,-8,-2,4,6,-7,-8,6,4,7],[-6,2,-10,-7,-5,-1,-7,-6,3,-9,10,7,-2,6,-1,-2],[7,-6,-10,5,8,-2,4,-4,-2,7,-8,7,-1,5,-10,-10],[-8,-6,-9,-8,9,-4,10,2,-10,1,5,-7,5,-10,-9,-3],[-7,9,-2,-5,-9,-5,-4,10,-6,-3,10,-9,3,9,-10,-1],[1,-4,-7,5,-5,-4,5,-6,-6,6,-8,3,4,3,4,2],[-4,-2,5,-8,6,-3,7,-6,8,-10,-6,-10,-5,-6,-9,-8],[-7,5,-6,6,4,-6,9,-3,-1,3,-6,-10,8,-1,6,-9],[10,9,-6,9,-2,-10,-7,8,-7,-7,-6,3,-5,-8,-4,6],[-10,1,9,5,-6,-4,9,9,5,-9,3,2,8,10,8,9],[2,3,9,5,-2,-6,-1,6,-3,6,9,-7,-9,-3,3,-4],[-2,-6,-2,6,-10,-4,1,8,7,1,3,6,-5,10,1,-4],[-10,3,3,-7,-4,-5,-2,-9,6,-6,-10,-2,1,4,5,-4],[10,10,-9,-8,9,7,6,-2,-10,1,3,6,7,-8,7,9],[1,3,-8,2,4,-3,-7,-3,5,6,9,-4,3,-1,5,-10],[-1,4,-5,9,6,-10,-6,8,8,3,-8,-6,-8,1,-6,10]],[[5,-9,10,10,9,-7,-2,10,2,9,-10,-1,1,4,5,7],[5,2,3,1,9,-6,-4,-3,10,8,-9,8,3,9,3,-1],[3,6,-3,-5,7,-5,10,7,2,-7,6,-2,7,-8,9,-1],[-1,6,3,6,7,-1,9,-6,-5,3,10,10,-7,8,-8,-8],[-5,10,-8,-10,-10,-1,-2,2,-1,9,-8,-7,-7,-3,-5,3],[5,-9,-2,9,1,2,8,1,9,-1,8,4,-4,-2,7,-8],[-9,-9,-8,-4,10,-10,-10,-10,-10,-9,-2,8,1,-4,5,5],[10,6,4,-5,-6,7,-8,6,-9,-8,8,-6,6,-9,3,-5],[-8,1,1,-8,-2,4,1,10,6,10,4,5,5,10,-8,3],[8,-7,1,-9,-8,5,-4,9,4,4,-3,-9,10,8,-6,3],[-4,-6,-4,10,-5,-1,-9,-7,-10,-3,9,-3,3,7,2,-5],[8,1,-4,6,-5,8,-9,-1,7,2,-5,-5,6,-8,-1,5],[4,-3,-9,8,6,-2,-5,4,4,-8,-8,-9,-6,-3,10,6],[5,2,8,10,8,-1,-2,4,10,8,8,4,-4,1,-6,10],[8,-7,-4,2,-8,4,7,-7,2,7,-5,-2,-8,5,-1,7],[-6,6,9,1,-1,9,-1,-5,4,-2,4,7,8,8,-6,-7]],[[-7,-2,10,-6,-6,-7,3,-1,5,-7,-9,3,-6,-7,5,-5],[-6,1,-8,-7,3,-3,-9,5,-8,-4,-9,-4,-7,-9,4,5],[9,-8,-4,-3,-10,-3,-9,-2,5,3,5,8,6,-4,-1,10],[6,9,4,7,6,-2,10,-3,-2,-8,-6,8,-6,-2,-5,7],[4,-1,7,2,-10,2,8,5,-4,8,-1,-3,3,2,-2,9],[-6,-2,-10,8,-9,-2,-8,1,-9,-3,5,5,-1,-6,-7,-9],[-7,6,7,9,-8,5,7,-9,2,7,8,-5,-1,4,-6,-3],[-3,-2,6,-6,-2,10,4,-6,-1,-4,-6,-10,4,7,6,-4],[-10,9,10,8,-4,-1,-10,-5,-9,2,1,-4,-7,-4,-10,1],[-5,-6,6,6,4,8,-6,5,-3,-3,-10,-7,8,7,2,-10],[10,1,-1,6,6,-9,9,10,-2,6,7,-6,-7,-5,-3,-5],[10,-9,-6,-6,10,-5,-1,1,-7,7,10,-1,8,-7,8,6],[-9,8,-9,-8,-10,-8,-9,6,3,9,9,-4,3,-10,5,-10],[-10,-10,3,-9,-10,-5,3,-4,-7,4,1,2,1,-7,-5,-1],[-7,5,-6,2,9,-6,3,1,-10,-5,-2,7,7,10,-2,9],[9,-9,6,4,3,8,-9,-3,5,-2,-4,-10,4,3,10,-5]],[[-3,5,-8,-5,-8,-6,-3,6,6,4,-8,1,6,-9,-7,5],[-1,-1,9,1,-10,-4,5,-2,-9,-2,-3,-10,8,-7,-4,-7],[5,5,4,1,2,-1,-7,-1,-9,5,10,1,5,-5,10,-5],[9,-9,5,-9,7,-7,2,1,2,1,1,10,-10,6,-8,-5],[10,-10,-5,-3,10,7,9,1,-5,-3,-6,4,-9,-8,-1,4],[8,-8,4,5,3,-5,-1,-4,-9,-5,-2,-3,-9,-8,3,-4],[5,-3,-7,-2,-2,3,-3,2,-3,-9,7,-8,10,-9,-7,3],[8,8,6,-4,-6,6,5,1,6,-5,-1,-9,8,-5,4,-6],[6,6,5,-4,10,-8,7,-4,-9,-6,-1,-1,-7,-3,-6,3],[-2,-4,10,8,8,-4,-7,-10,5,-7,4,-7,-6,-2,-9,4],[2,8,8,2,4,-10,2,7,7,6,-6,2,3,-4,-7,-6],[8,2,2,1,10,4,3,-1,-9,-2,2,-7,-8,-9,-9,3],[-9,-3,-9,-6,6,-10,3,-9,-10,5,5,-9,3,7,3,1],[-4,-4,7,-1,9,-1,-5,-3,1,9,2,-10,-7,8,8,-5],[-2,-7,-8,3,2,-10,-4,3,2,3,3,-8,-4,-2,6,5],[8,-8,-10,4,2,-8,10,4,-7,-8,2,-1,-4,9,2,-7]],[[-5,9,-3,7,8,4,1,9,-4,-6,-5,-3,2,9,5,6],[-9,7,-7,-1,-2,-4,2,-10,-2,-3,5,-6,-7,5,-8,-1],[-6,-3,3,-10,9,-9,-7,5,7,-6,3,3,6,-1,-9,-5],[9,7,-2,-8,-3,9,-5,-1,2,9,1,7,-8,-4,-9,1],[5,-1,-9,7,5,1,-10,-6,-2,-10,-5,-8,5,1,1,3],[1,4,-4,-1,-4,-1,-5,-9,-2,-9,7,-1,1,8,3,7],[-7,6,-9,2,-9,10,-10,2,1,10,-9,2,-10,-2,-4,-10],[8,-2,-3,4,7,-6,6,-10,9,5,-10,10,9,-4,-8,6],[10,-7,-2,5,-7,-10,-10,8,-2,-9,-1,-2,-10,-5,-3,-6],[-9,-6,-4,-2,-3,-1,-5,-4,3,-1,2,-7,4,-1,-3,1],[-10,4,-7,4,-1,3,-4,-6,10,-3,1,-7,4,-1,4,8],[9,7,-8,-8,-6,6,-9,10,10,-4,-3,-5,6,3,-7,4],[-3,-2,4,2,2,-1,-10,10,4,10,-2,6,10,10,10,-1],[-6,6,4,9,5,5,-3,-5,9,-8,-10,-9,-4,8,-2,9],[-2,8,-10,-2,-1,10,3,2,-3,-1,5,-3,-8,2,-10,7],[-3,-9,-4,-10,7,-8,9,2,-2,-5,2,3,1,-9,-6,6]],[[-1,-6,6,-7,-8,-5,7,-9,8,-4,-5,10,4,-8,6,-4],[7,-2,-6,7,-4,-10,-8,9,-2,6,-2,3,8,6,5,2],[10,6,3,-9,-6,9,8,9,1,-9,-6,8,-8,-9,-6,7],[-5,1,8,6,-1,-7,-4,-2,4,9,6,3,4,6,-4,-8],[-8,8,1,10,-8,-2,1,-9,-5,-4,-6,6,-8,-9,-5,-1],[8,-9,-3,2,3,-6,-7,-9,1,-5,10,-6,4,-1,2,2],[-1,-10,7,6,5,-4,4,7,9,-2,-5,-9,4,8,2,-8],[10,-7,-8,-8,-2,-5,8,-4,6,-9,-4,10,8,6,9,-5],[1,-7,-3,-2,-5,-3,-1,-3,-5,-5,-1,-7,-2,-9,8,-9],[5,8,1,3,8,-1,5,3,-6,-8,-5,6,-9,-10,10,-6],[7,1,3,-4,-1,8,-10,-5,1,-3,-10,4,3,-8,3,-6],[-5,6,2,-9,-6,-1,7,-1,3,3,-3,5,-10,7,-7,4],[1,-2,-10,7,7,2,-8,-2,-9,6,-3,5,6,-7,-8,-6],[10,1,-8,-6,10,1,-3,1,-10,-1,8,6,-2,6,3,7],[10,3,-10,-3,9,10,-6,3,8,1,-1,-9,-2,-3,6,8],[9,6,-2,-2,4,4,-5,-8,-10,8,-7,-6,-1,-4,8,5]],[[-3,9,-1,-10,-4,-4,3,1,-2,7,-7,6,2,7,2,-7],[4,-4,-6,-7,-1,1,-5,-9,3,-6,-9,-8,-2,10,8,3],[-3,6,-1,10,-8,-6,-3,-9,1,7,-8,2,10,6,-9,-2],[5,-2,5,-8,4,5,9,4,-9,-1,-5,-9,-6,7,-5,8],[8,-6,-5,-3,10,-6,2,-10,-2,10,-7,6,-5,9,-1,1],[10,-2,4,1,3,-5,-1,10,10,-3,-10,-10,-2,-6,-7,-10],[-2,1,-8,-2,-2,-10,3,-8,-9,-10,2,3,-1,6,-3,5],[9,-3,-10,9,-3,-7,-8,-1,-10,7,3,7,-8,1,9,1],[4,6,1,6,-8,-2,9,-5,-6,-2,-2,-2,2,-4,-1,-1],[-8,-9,-6,-5,-9,3,8,-9,-10,-3,2,5,-9,6,-5,-5],[6,4,-8,-8,-3,6,-9,-8,-6,3,6,-1,-10,-7,4,10],[7,-5,2,-3,-6,-10,2,6,-1,-7,9,-4,-4,4,4,-1],[-9,-5,2,7,6,3,-7,7,7,5,-1,5,-9,-5,-4,-3],[5,-3,7,-4,-9,-3,5,-4,-4,-8,-5,2,5,-8,-6,-1],[10,-7,-4,-2,-8,-1,4,5,2,5,-10,3,4,2,4,-10],[-7,-1,-8,8,-7,6,2,-9,7,-4,-1,-10,-10,-7,-8,-1]]], dtype = "int16")#candidate|5559|(8, 16, 16)|const|int16
var_5560 = relay.var("var_5560", dtype = "int16", shape = (8, 16, 16))#candidate|5560|(8, 16, 16)|var|int16
bop_5561 = relay.bitwise_xor(const_5559.astype('int16'), relay.reshape(var_5560.astype('int16'), relay.shape_of(const_5559))) # shape=(8, 16, 16)
func_300_call = mod.get_global_var('func_300')
func_303_call = mutated_mod.get_global_var('func_303')
const_5565 = relay.const(False, dtype = "bool")#candidate|5565|()|const|bool
call_5564 = relay.TupleGetItem(func_300_call(relay.reshape(const_5565.astype('bool'), [])), 0)
call_5566 = relay.TupleGetItem(func_303_call(relay.reshape(const_5565.astype('bool'), [])), 0)
uop_5574 = relay.erf(call_5564.astype('float32')) # shape=(14, 7, 6)
uop_5576 = relay.erf(call_5566.astype('float32')) # shape=(14, 7, 6)
func_4780_call = mod.get_global_var('func_4780')
func_4782_call = mutated_mod.get_global_var('func_4782')
call_5579 = relay.TupleGetItem(func_4780_call(), 0)
call_5580 = relay.TupleGetItem(func_4782_call(), 0)
func_4683_call = mod.get_global_var('func_4683')
func_4685_call = mutated_mod.get_global_var('func_4685')
call_5594 = relay.TupleGetItem(func_4683_call(), 0)
call_5595 = relay.TupleGetItem(func_4685_call(), 0)
func_4962_call = mod.get_global_var('func_4962')
func_4964_call = mutated_mod.get_global_var('func_4964')
const_5609 = relay.const([True,False,True,False,False,True,False,False,True,False,False,False,True,True,True,True,False,False,False,True,False,False,True,False,True,False,True,True,True,False,False,False,False,False,False,False,True,False,False,True,True,True,True,False,False,False,True,False,False,False,False,False,False,True,True,False,True,False,True,False,False,False,False,False,False,False,False,True,True,True,False,False,False,True,False,False,False,False,False,False,False,False,True,False,False,False,False,True,False,False,False,True,False,False,True,False,True,False,True,False,True,False,False,True,True,False,True,True,False,True,False,False,False,True,True,False,True,True,True,True,True,True,False,True,False,False,True,True,False,True,True,True,True,True,False,False,True,True,False,False,False,False,False,False,True,True,False,False,True,False,True,False,True,False,False,True,False,True,False,False,False,True,True,True,False,True,False,False,False,False,False,False,False,False,True,True,False,True,True,True,True,False,True,True,False,True,False,False,True,True,False,True,False,True,True,True,False,True,True,False,True,True,True,True,True,False,False,True,True,True,False,True,True,False,False,False,True,False,False,False,True,True,False,False,False], dtype = "bool")#candidate|5609|(225,)|const|bool
call_5608 = relay.TupleGetItem(func_4962_call(relay.reshape(const_5609.astype('bool'), [25, 9])), 3)
call_5610 = relay.TupleGetItem(func_4964_call(relay.reshape(const_5609.astype('bool'), [25, 9])), 3)
func_4044_call = mod.get_global_var('func_4044')
func_4049_call = mutated_mod.get_global_var('func_4049')
const_5614 = relay.const([1,8,8,-5,3,-10,-7,5,10,8,-8,-7,-5,4,8,-9,-5,-7,7,7,-7,-10,-9,-8,-5,-8,-3,-9,5,4,9,4,-4,-6,-3,9,-7,-4,-8,-7,1,7,-10,4,-8,-1,-4,10,4,-9,8,-8,-8,5,-7,8,10,1,10,5,4,6,1,-7,3,-3,-3,7,-3,7,5,-7,-9,-4,4,10,7,7,5,2,-10,-10,-4,-6,9,7,9,10,-2,8,6,-3,5,1,-6,7,-6,10,-3,-8,-10,-8,-9,-6,5,-7,3,3,2,5,5,-5,-6,-2,3,-1,5,1,-10,-4,-10,-5,1,-10,-10,-2,-4,7,-3,-9,6,-9,-3,-6,-7,7,1,2,-10,6,5,4,-8,9,9,-8,-2,-8,9,-8,-4,6,7,-9,2,8,5,9,4,-5,-8,7,-3,-2,9,-1,-5,8,6,-10,3,6,-1,-3,4,7,4,1,1,2,-3,4,-9,-3,-10,-5,-2,-2,7,7,7,1,-10,-9,-8,-2,1,1,8,6,7,-10,-4,2,-2,-3,5,-8,-8,5,-7,5,2,-9,1,8,-9,-7,-5,-4,-9,3,1,-8,-10,5,1,5,-7,4,2,-6,-2,-3,3,3,-6,-8,10,8,-3,5,-2,-7,-5,-6,7,-7,6,-8,-9,3,-7,-6,10,-7,6,7,2,-8,-7,5,8,-4,2,-3,3,10,-8,-7,10,-1,5,6,-2,-8,9,-4,3,-1,-10,-10,8,-4,-4,-5,6,3,-2,3,-1,4,2,9,7,-2,2,-1,2,9,8,-2,-9,-8,-2,-6,9,5,7,-9,-3,1,-5,-8,-8,2,-2,-8,9,-2,6,4,-8,-9,2,-9,-10,-10,3,-1,8,6,-8,-1,-2,-8,10,4,-10,3,10,6,-4,-3,8,-7,7,-4,-10,2,7,8,1,-5,4,2,10,4,-6,-1,2,1,-1,-4,2,-3,-5,6,3,-6,9,-1,-8,3,1,-10,-1,-2,-8,5,2,6,-7,5,4,-6,-1,-10,-1,3,-6,-5,-6,1,-3,1,-2,-5,1,-10,-3,-8,5,-3,2,10,-1,-4,2,-8,-2,2,-9,-5,-9,5,-3,-8,2,7,-7,1,4,4,1,-10,-2,6,-9,2,-8,-2,2,1,1,-8,-7,-6,-4,-6,2,-9,10,8,8,9,-6,7,1,2,8,-2,-8,-7,-9,-9,-10,-7,-6,10,-4,-2,-10,-10,8,4,-3,2,-7,6,-3,8,5,-6,2,-7,-4,9,-9,-8,-5,5,-1,1,-8,-5,-6,-4,2,-2,-5,1,7,7,2,-2,-10,-5,6,10,-7,-4,-9,3,-10,4,-5,7,8,9,1,-5,10,3,-9,9,7,-8,2,6,6,7,8,5,-2,-5,8,4,-1,-4,-10,-6,-6,3,-6,2,-2,5,-5,-5,-7,-9,-10,2,2,4,1,-10,4,7,-4,-4,-7,6,3,8,2,4,-10,5,-6,-3,9,-6,-7,-7,-1,7,1,-10,3,-4,-5,6,7,-5,-2,-2,2,-8,-8,-9,-5,6,2,-2,-6,-1,-7,6,10,-8,10,3,-7,-2,-5,5,9,-8,9,-5,10,-6,3,-2,-3,-5,-2,6,1,-4,9,6,1,9,8,7,-2,-5,-4,9,-9,10,-5,3,-2,-10,-6,-1,2,9,5,-6,-6,3,-9,-7,7,2,-4,5,1,9,4,4,-1,6,8,3,4,-4,-8,-1,-8,6,7,-10,-7,-6,8,-6,5,-4,-5,-7,-5,-2,-3,8,8,-5], dtype = "int16")#candidate|5614|(672,)|const|int16
const_5615 = relay.const([[9.456862],[4.844591],[-5.960991],[-2.936298],[-4.221660],[7.035779],[-5.644751],[3.643856],[3.030449],[-0.104633],[3.388304],[-6.363601],[2.637756],[-4.363467],[-5.909488],[-1.302844],[-2.740055],[1.487157],[3.157323],[-0.827871],[-7.686516],[0.035795],[2.818450],[-0.342811],[-1.693271],[7.486665],[-1.377650],[9.535743],[-6.888154],[-9.039704],[-6.209922],[-1.867034],[-2.646445],[3.501995],[-6.549631],[-1.985988],[4.461221],[2.977929],[-5.738340],[4.194532],[-1.398541],[-7.729332],[9.306284],[-9.638525],[-6.996534],[-8.976743],[-1.286497],[9.246110],[1.587030],[-0.825606],[-6.997935],[-5.594531],[-5.488741],[-7.403069],[6.634342],[9.279104],[7.382821],[-1.181705],[-7.441192],[-0.782234],[1.369873],[4.094045],[2.261048],[9.383151],[7.914966],[-0.066623],[-3.842659],[-1.023959],[-4.164377],[5.968209],[-0.667784],[-2.385083],[9.360867],[-0.638258],[8.825534],[-3.029323],[-0.761331],[-1.940001],[-4.040303],[-5.261227],[-4.365276]], dtype = "float64")#candidate|5615|(81, 1)|const|float64
var_5616 = relay.var("var_5616", dtype = "float64", shape = (1456,))#candidate|5616|(1456,)|var|float64
call_5613 = relay.TupleGetItem(func_4044_call(relay.reshape(const_5614.astype('int16'), [672,]), relay.reshape(const_5615.astype('float64'), [27, 3]), relay.reshape(var_5616.astype('float64'), [1456,]), ), 6)
call_5617 = relay.TupleGetItem(func_4049_call(relay.reshape(const_5614.astype('int16'), [672,]), relay.reshape(const_5615.astype('float64'), [27, 3]), relay.reshape(var_5616.astype('float64'), [1456,]), ), 6)
output = relay.Tuple([bop_5561,const_5565,uop_5574,call_5579,call_5594,call_5608,const_5609,call_5613,const_5614,const_5615,var_5616,])
output2 = relay.Tuple([bop_5561,const_5565,uop_5576,call_5580,call_5595,call_5610,const_5609,call_5617,const_5614,const_5615,var_5616,])
func_5619 = relay.Function([var_5560,var_5616,], output)
mod['func_5619'] = func_5619
mod = relay.transform.InferType()(mod)
mutated_mod['func_5619'] = func_5619
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5619_call = mutated_mod.get_global_var('func_5619')
var_5621 = relay.var("var_5621", dtype = "int16", shape = (8, 16, 16))#candidate|5621|(8, 16, 16)|var|int16
var_5622 = relay.var("var_5622", dtype = "float64", shape = (1456,))#candidate|5622|(1456,)|var|float64
call_5620 = func_5619_call(var_5621,var_5622,)
output = call_5620
func_5623 = relay.Function([var_5621,var_5622,], output)
mutated_mod['func_5623'] = func_5623
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5449_call = mod.get_global_var('func_5449')
func_5451_call = mutated_mod.get_global_var('func_5451')
call_5649 = relay.TupleGetItem(func_5449_call(), 0)
call_5650 = relay.TupleGetItem(func_5451_call(), 0)
func_5619_call = mod.get_global_var('func_5619')
func_5623_call = mutated_mod.get_global_var('func_5623')
var_5656 = relay.var("var_5656", dtype = "int16", shape = (2048,))#candidate|5656|(2048,)|var|int16
const_5657 = relay.const([3.692513,-5.187378,2.346939,4.797447,-2.535786,7.918185,-1.664802,4.966961,0.112072,8.552067,2.097519,-1.252116,6.017359,-7.464341,-5.640676,-0.348955,7.596105,-0.001932,-2.025713,-8.201531,-4.304722,8.476519,5.398094,-6.700179,-8.783052,-8.850067,-2.141522,9.162794,6.874358,-2.927869,0.124443,6.948201,9.633084,9.790718,-1.380427,1.577846,0.251516,4.516301,3.387356,-5.439325,3.576113,9.183715,8.135641,0.461081,-9.857106,-0.231148,8.535292,-7.223476,3.977043,-7.317215,2.740712,0.108892,-6.946736,7.548991,-5.794655,8.279289,5.510258,2.960792,8.590473,8.341290,-6.568631,5.517834,2.071786,-3.570461,8.194971,-7.111443,-5.821266,8.566117,-1.746158,-1.148098,-6.168944,7.803325,3.480822,-1.472829,6.166017,-0.123219,5.059644,4.446444,-0.360440,-5.988672,-3.867003,-2.634211,-4.556639,8.237354,6.209085,6.020266,6.365218,6.886385,1.587323,3.368617,6.047066,-1.928709,6.223387,0.606018,7.924652,8.238649,4.999913,6.619259,-9.258295,-0.723051,-9.970714,3.177040,-2.482464,-2.646325,3.474327,8.349999,-9.372749,5.800596,5.288936,1.044196,-2.375375,5.081175,-7.575810,5.291114,2.073458,-3.366956,8.167070,-3.135389,-9.334093,3.854165,-9.840623,-3.143784,-1.807075,2.663490,2.568458,0.604798,1.979856,6.847882,2.806367,-2.911861,-0.754882,-9.471452,4.799599,-5.517248,-7.811101,8.123824,-5.093706,6.463200,3.821217,-1.495338,1.486332,4.288786,-0.208896,-3.189593,7.083305,7.857348,-4.421637,-1.491166,-4.719911,8.746327,-2.128164,0.152477,2.324976,-6.321544,1.597852,0.644895,-2.735261,-5.052995,5.840591,-2.333944,8.745393,-9.253873,0.758251,6.043518,0.555346,-4.522295,1.195374,-6.591424,-4.750874,-6.012652,-5.910854,-1.103887,-9.610442,6.615576,-5.886648,-9.572999,1.983310,7.861169,5.457931,-2.506523,4.317380,9.080361,6.935741,1.694842,-7.643862,1.478594,1.839203,4.619760,-6.668278,8.269012,-0.576455,7.507380,5.861926,-7.147579,7.276279,3.127091,-1.605610,-7.037796,4.255935,9.577192,8.978654,-3.793266,3.261473,-9.227855,-5.659731,-6.938553,5.958301,2.952536,-3.974828,-8.374014,-9.154311,-6.573491,-6.735642,-2.775538,2.205268,4.120268,4.693938,7.687085,3.785289,-5.387363,-4.180341,-7.461298,-8.296029,-5.998647,7.396075,8.669772,-7.018913,-4.038017,-2.369418,-5.305390,7.541264,-6.225688,0.009757,8.387515,4.247380,7.931702,-0.882680,8.849668,5.467348,0.067944,-0.587329,-6.752974,-7.083716,6.500824,-7.687591,-8.975910,7.289891,-5.485290,8.660098,8.752239,0.889966,-0.108411,-3.924409,7.363438,5.547544,9.526422,3.051781,-9.004208,-3.654940,-7.235721,-5.622328,-6.056268,3.845847,-6.043674,-1.475297,2.940169,-0.885143,4.057877,6.495455,-4.400795,9.872795,8.101719,-9.452058,2.316789,8.721679,6.496109,-7.584373,-7.524811,-7.667808,-7.399589,-0.386927,-1.363780,1.042863,-4.668013,-9.682684,3.787592,-4.168386,-5.080765,9.710759,1.528919,9.332820,-8.586390,8.934487,6.893181,3.568575,-9.877171,3.180385,2.265346,0.365721,-6.686643,-3.734708,9.396481,-2.445688,3.447666,6.182967,-4.652307,4.632330,7.198302,3.278155,-4.728683,-0.261020,9.639335,-5.266339,8.905791,-2.335435,2.002319,8.335331,7.864197,3.101101,2.681152,9.488824,6.830373,-1.576216,3.829899,-7.543684,5.775622,4.220648,-3.575345,3.793217,3.442975,9.051924,-7.816812,4.515335,-5.290476,4.064947,-4.475180,-4.469360,1.511565,-6.541063,-0.178625,7.632838,1.335197,-1.493648,-2.062648,5.968102,3.513823,-3.781041,-6.573920,1.798169,-5.846201,-1.558867,-5.523505,3.746974,-6.021028,-4.495369,-2.264460,-3.907227,-1.574059,1.189402,-9.010812,-3.145471,-2.043071,1.394734,1.655876,3.463269,9.863299,-3.959344,-0.383974,-6.536876,8.561809,-4.644785,-6.001672,0.504834,4.619513,2.392251,-0.029857,-4.272782,-4.488624,2.024322,-3.327227,-5.032973,-1.815203,2.007798,-3.812123,7.154067,7.350992,9.766337,-3.071464,-2.243551,0.738958,9.828703,-4.185777,-5.646304,-0.085000,-8.165872,1.291299,-0.059016,9.275037,-6.397436,0.779158,7.036232,6.927527,-5.310354,7.847025,-1.729325,-6.328137,-6.121682,4.216264,-6.545436,-8.535010,-1.415485,7.487487,-0.097481,3.627883,-7.829209,-1.271942,7.064231,-6.288714,-4.545618,-1.751710,-7.572775,-2.900580,1.544762,-6.186788,6.396401,-9.812739,-7.805327,5.999442,-7.152282,6.470603,9.523720,-0.991505,-6.496993,5.983067,1.522439,1.592795,-5.567184,-7.043400,4.498773,2.936335,-5.356326,-6.307049,4.224378,0.485342,-5.787447,-0.797104,-3.796167,-9.054303,8.044512,6.818634,-4.467339,9.510738,0.428141,-1.921370,-7.524103,7.051439,-3.367252,1.743557,6.912808,8.064518,6.934901,-5.190401,6.102989,-4.441310,-0.918411,2.778434,-3.743545,5.724190,-3.632717,-7.775825,-7.656822,4.416716,-4.816744,-2.171723,9.793554,8.869287,-1.196828,9.657406,4.171616,-8.908243,7.217322,-0.914701,-0.008311,6.887436,2.179942,0.569749,-4.650281,-9.971817,3.255775,-8.910409,2.962893,-0.383150,5.556488,6.585754,3.950416,-9.142345,5.793834,3.912823,1.839329,-1.066224,-6.237199,-3.293472,5.596657,2.573651,4.749000,6.207619,-0.332314,-5.379638,4.366946,-1.957706,-6.871366,-3.540325,4.054023,0.460560,-9.948380,0.539042,-2.415993,3.076921,8.706376,-9.101707,6.739363,9.893744,2.587496,7.739820,2.696826,-1.410330,6.199143,6.452523,-0.875921,6.433531,-9.358061,9.946374,-1.946350,-8.977339,-6.944178,-0.302547,4.020535,4.579663,-5.344942,5.886607,-6.978961,2.723650,-3.461030,-3.391552,7.648916,-9.688813,-5.433681,-9.525963,-6.297302,-4.038674,-7.446930,-3.892752,-1.439146,-7.156694,9.011370,-2.301156,4.556503,9.957367,-5.648232,-6.374831,6.017297,-3.888408,2.047064,-6.890336,5.043302,-2.476439,0.834862,3.172913,-4.954879,-0.823424,-1.406979,1.371785,-5.926231,2.623360,-5.301983,6.925801,-1.262449,6.944906,-7.539176,-3.955132,3.004844,6.182081,8.664532,-5.248723,5.265623,1.900749,-8.198434,0.756183,0.318044,3.600355,7.118265,4.338984,-3.297442,1.960788,-0.835867,3.183985,-7.483675,3.524863,1.253423,9.474280,-7.295621,-9.695456,3.719471,-4.319618,6.034442,-0.029082,-2.682406,-5.959970,-0.355022,1.395784,8.551317,-6.331031,-9.075560,-6.292315,-3.092566,-6.149642,-5.759932,6.480097,-0.725989,8.054241,5.322534,-6.310271,8.897582,6.731852,-7.433936,8.981950,2.777818,9.963005,3.243738,2.461892,3.703204,-6.804700,2.659492,1.901078,7.771558,5.277465,-8.974478,-8.875795,-6.233804,-7.529545,2.872637,7.657102,3.410607,-5.401279,-7.341226,-3.110926,5.107099,7.624904,-9.253924,-3.676237,8.049474,9.132242,-4.258402,-1.228941,3.007836,0.525275,-3.999553,4.021235,-0.489041,-5.069723,5.694228,-8.796287,7.737669,6.057609,4.981815,-5.757309,5.183926,-0.552209,0.353791,3.591639,7.876376,6.523692,3.414951,-6.604797,-8.908752,-1.783366,1.889782,-4.586326,-0.714845,6.298701,-7.464078,3.252854,6.242455,6.393060,-7.713971,4.812955,8.688258,6.545410,1.356698,-4.734834,-3.297409,2.227388,-3.622194,-1.434283,-7.326987,-9.665505,4.332942,-3.532141,9.951421,-1.157106,-4.993061,-2.029965,-3.143619,-6.872091,8.448324,-3.640876,2.340831,8.096261,9.453978,7.348271,5.862809,-4.070374,7.463341,2.975598,-8.072124,-2.543543,0.682581,8.553780,-7.502680,1.735252,-0.957270,2.528246,-7.708642,4.272032,-8.704693,7.451652,-5.471019,8.076200,-0.947725,1.086543,-3.719779,-2.904048,-7.336737,3.337574,8.369770,-9.355845,-1.727819,-5.220752,-0.240368,4.380565,-9.614216,6.715748,-6.349104,-1.397678,0.525070,-9.347056,0.406531,-3.542523,-7.500299,-7.632766,-7.703747,7.832759,-4.638941,7.163441,-9.907245,6.484131,2.054307,0.426620,4.908169,6.730767,4.765663,-0.540779,-9.072329,-6.982330,2.987871,-0.260459,1.789342,-4.831692,9.400793,6.717374,-3.042246,-5.321883,8.527182,-2.244654,8.199103,8.512296,3.834800,6.520419,-5.176307,-8.941469,-5.246786,-3.329592,-2.135664,9.249626,-4.270408,8.279499,-4.247416,4.704536,-3.358378,-9.863043,5.915085,-6.995310,-2.520639,-6.941067,-7.701161,-8.260515,6.238319,-1.055933,4.947900,-0.769668,-7.459709,8.845535,0.301234,-2.399062,-5.962016,-2.495629,2.361691,-2.685745,-9.582686,-2.695500,3.918891,-4.075175,6.354901,-4.953210,-5.473598,4.870443,2.273337,9.344067,6.702925,-0.459332,6.127476,0.679990,7.994247,-5.655517,-6.634161,-4.623217,1.907221,-1.550655,-0.179482,7.140542,4.701315,6.635530,2.478047,-0.030856,6.930343,-5.628690,2.350594,5.486810,6.298735,-9.892532,-5.478968,7.513430,1.733920,0.341382,1.206735,6.344551,7.388840,1.859047,9.359849,4.373154,-3.058936,0.801825,2.320303,-4.895652,-9.931950,-6.994339,-0.085654,-4.446849,4.796071,4.057477,3.454603,-4.457026,8.496708,3.173857,4.127802,0.137906,1.936827,2.131858,2.785666,5.948885,-2.662089,9.813629,-7.317082,3.012476,9.237553,-9.398290,1.037184,8.288741,-5.535113,6.987553,9.371958,5.613258,-3.294156,8.764574,-4.331662,6.096450,-5.397405,2.289179,9.688806,-8.500637,3.645695,3.994647,0.996792,-0.086896,7.482083,9.196533,-7.023671,7.009011,4.531026,3.484382,-3.609539,3.910567,1.436209,1.583715,0.659476,1.158614,-5.785135,4.975529,8.980004,6.046081,2.644450,0.783713,2.754078,-0.112589,5.758973,-8.633944,0.499830,-4.277922,0.833286,5.965497,3.018004,8.839456,5.164513,-8.985663,-7.283735,2.361547,-4.569458,-5.730364,-2.607546,2.201237,-5.286796,9.490232,7.267176,-5.361540,8.169474,3.438897,-8.613685,-0.499945,2.679749,-1.052007,-3.921891,3.146620,-0.417492,-1.001014,2.063544,-3.886831,7.355252,8.609584,8.432812,7.569872,3.325951,5.276922,-5.237695,0.136681,-5.400622,6.628372,9.192521,-9.954848,-9.539998,-4.394180,-4.029457,6.247670,-6.281361,-3.337442,-5.420089,-5.466871,-3.379788,2.721727,9.571741,-1.184873,-5.960567,-0.707937,-1.839103,2.775502,2.802481,-0.017201,-1.104163,-5.975514,-3.067051,-1.567630,-9.472945,-0.579774,4.370379,6.376135,-2.644099,-1.908182,-1.775831,4.196573,5.438622,2.872477,-2.557813,-0.089707,-4.418398,-9.927978,3.750654,3.166410,7.266664,-7.561653,-7.563955,-2.872449,9.940212,5.579158,4.234322,1.222934,-7.761904,-4.195751,-0.678969,3.795339,3.655687,-7.019736,8.077301,-5.246508,0.494722,2.384839,2.222560,8.755125,-6.436395,-1.300632,3.298537,5.060098,-1.480289,-4.471282,-6.282011,1.677756,0.855898,3.915240,-5.984713,-2.745613,-2.256816,6.381765,3.975618,2.719358,1.799642,4.813783,9.337722,-8.467161,-5.883078,-9.141422,9.929895,-9.451866,1.459701,7.347037,-8.951971,-1.836777,7.050458,-0.079851,-7.046735,-5.188094,3.097653,-0.674181,-6.365226,-2.670726,5.299110,-5.170226,7.150762,-9.511962,-6.805800,-4.426361,7.648876,0.383413,-2.173020,6.404708,4.519696,-7.611238,7.670699,6.988924,-6.726451,6.704876,8.040707,-5.706426,-6.714532,5.359561,-3.137184,0.945319,-8.747907,-7.579997,-4.061111,4.942154,9.626198,-3.572734,-4.876831,6.098421,-0.997860,8.211065,-5.657867,-1.700424,-9.344116,1.515079,8.666716,-9.258201,1.740843,-4.028231,-6.838339,-4.712876,1.936430,-5.252649,-5.572830,-0.510042,-2.961013,-9.596739,7.995414,-0.555720,0.139456,-8.442022,-2.967750,-1.575042,9.711128,-2.724634,3.079759,-7.475226,3.229635,-4.231275,-3.587527,-2.566651,-8.603098,1.431505,4.780068,8.156406,2.995840,3.215871,-3.037573,9.093946,-7.711223,8.803775,-6.299814,3.842145,6.877950,-6.563133,-1.452885,-4.326400,3.218838,3.059710,6.282679,7.273277,-1.479026,6.022805,0.756850,3.034714,-9.900883,1.542547,-5.912889,-8.683467,-7.073485,0.967707,-3.734845,-1.706843,6.498760,-4.400211,-7.699786,2.796438,2.229109,-3.115073,6.547598,-4.299773,-6.839601,8.572694,-2.062161,-0.196575,-7.964437,-6.866971,-3.187738,-5.925289,-1.115902,-6.228840,7.578974,5.494268,-1.470140,5.750683,0.294611,5.697996,4.432882,-8.635425,4.790682,-2.978316,-8.221029,-1.111464,1.703279,-5.085243,4.377626,5.163189,-7.766132,6.357601,-1.309806,6.989394,9.975091,4.295200,1.538333,-5.051257,7.787796,-8.187058,9.345454,-4.460992,7.142851,-6.280517,8.571658,0.532605,1.812212,7.306976,9.814853,6.502999,6.607877,7.953104,0.862114,8.011580,9.693714,-4.888483,-2.057688,1.430934,-3.340015,4.302342,9.373916,4.963782,1.925714,-6.362334,7.571842,6.100161,0.514140,3.679653,8.561341,1.157617,-5.472018,4.682327,-1.988194,4.331568,4.719032,-9.562613,4.644382,4.863076,-5.272935,-2.286398,9.933396,6.898405,-9.465516,5.664102,7.260011,-7.637797,1.794845,1.782379,2.444533,-3.709107,1.558613,6.219024,-5.479819,6.360430,2.107496,1.722772,-1.413666,1.542243,0.343016,-9.191310,2.651469,4.740127,-8.383948,-8.744521,3.262581,-8.886409,7.471663,8.683822,-7.698232,9.827229,-0.503714,7.304225,2.976902,-3.914731,9.559545,9.740788,2.087612,9.036693,9.964571,0.279208,-4.652487,3.070428,-5.289963,-8.141860,-1.995840,-6.357473,-2.314264,2.367511,-3.572087,-6.489148,-5.085680,-0.436017,-0.793269,7.335621,8.650453,-4.005020,0.652346,8.319043,0.822461,-2.676604,7.347982,-1.881368,-4.954393,2.550454,4.873236,1.646953,-6.342027,-7.150184,9.167825,-6.977984,-2.398758,0.569252,9.371126,9.796361,-8.895716,-6.679371,-8.641398,0.814226,-0.910890,0.095361,-2.584908,1.208660,-9.524526,-2.032519,2.143694,-6.495762,9.838924,6.597751,5.713011,1.424200,8.450617,4.849674,0.062481,-8.874135,-1.464809,0.926149,-8.650971,4.628830,-3.308456,1.524957,-3.882406,-3.859551,4.708608,-7.671969,-1.390104,-3.545063,1.739946,-5.046390,-7.326548,-5.963575,-2.018564,5.239970,-9.524883,-1.042428,-3.170608,4.157731,6.907114,8.296148,4.613114,0.206547,6.773652,3.189227,-7.717935,6.939180,1.885132,1.708653,-1.945887,-4.887850,4.111642,9.342135,-7.851090,-7.728083,-9.612739,-5.530669,-0.147903,-0.864439,3.414697,-3.983893,5.262391,-5.923116,-2.182467,-8.089292,5.494210,9.918739,2.269455,-6.713833,2.272265,-1.142231,-2.565486,-5.600942,-8.511543,0.655770,-6.235936,0.676153,7.340097,-6.610027,1.058237,-1.771031,-7.745567,4.699866,5.501533,4.675929,3.733258,-1.769351,7.318538,-7.268072,0.528175,7.071726,5.058276,9.621502,0.746486,-5.578371,6.849442,6.494166,2.940428,8.122212,-7.677202,6.444548,-5.049166,-4.442677,-3.948599,-1.277028,-1.177316,-8.061923,-6.017358,-9.392365,2.096126,8.492858,-2.799065,-2.703140,7.563606,-6.001566,7.435905,1.558265,9.028567,5.484213,-8.969659,-1.899828,0.476138,9.160009,-4.489061,0.557233,-6.993054,-3.849117,8.459143,-3.386781,3.175718,8.526567,2.825681,-6.150756,-3.796947,-8.692468,8.113682,7.837455,7.839986,8.737510,-2.112537,-0.575997,3.720045,1.278307,1.439811,8.200285,-3.455046,6.447623,-1.363426,4.580042], dtype = "float64")#candidate|5657|(1456,)|const|float64
call_5655 = relay.TupleGetItem(func_5619_call(relay.reshape(var_5656.astype('int16'), [8, 16, 16]), relay.reshape(const_5657.astype('float64'), [1456,]), ), 8)
call_5658 = relay.TupleGetItem(func_5623_call(relay.reshape(var_5656.astype('int16'), [8, 16, 16]), relay.reshape(const_5657.astype('float64'), [1456,]), ), 8)
output = relay.Tuple([call_5649,call_5655,var_5656,const_5657,])
output2 = relay.Tuple([call_5650,call_5658,var_5656,const_5657,])
func_5660 = relay.Function([var_5656,], output)
mod['func_5660'] = func_5660
mod = relay.transform.InferType()(mod)
var_5661 = relay.var("var_5661", dtype = "int16", shape = (2048,))#candidate|5661|(2048,)|var|int16
output = func_5660(var_5661)
func_5662 = relay.Function([var_5661], output)
mutated_mod['func_5662'] = func_5662
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4639_call = mod.get_global_var('func_4639')
func_4641_call = mutated_mod.get_global_var('func_4641')
call_5701 = relay.TupleGetItem(func_4639_call(), 0)
call_5702 = relay.TupleGetItem(func_4641_call(), 0)
output = call_5701
output2 = call_5702
func_5725 = relay.Function([], output)
mod['func_5725'] = func_5725
mod = relay.transform.InferType()(mod)
mutated_mod['func_5725'] = func_5725
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5725_call = mutated_mod.get_global_var('func_5725')
call_5726 = func_5725_call()
output = call_5726
func_5727 = relay.Function([], output)
mutated_mod['func_5727'] = func_5727
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3712_call = mod.get_global_var('func_3712')
func_3713_call = mutated_mod.get_global_var('func_3713')
call_5770 = func_3712_call()
call_5771 = func_3712_call()
var_5772 = relay.var("var_5772", dtype = "int16", shape = (2, 336))#candidate|5772|(2, 336)|var|int16
bop_5773 = relay.minimum(call_5770.astype('int16'), relay.reshape(var_5772.astype('int16'), relay.shape_of(call_5770))) # shape=(2, 336)
bop_5776 = relay.minimum(call_5771.astype('int16'), relay.reshape(var_5772.astype('int16'), relay.shape_of(call_5771))) # shape=(2, 336)
output = relay.Tuple([bop_5773,])
output2 = relay.Tuple([bop_5776,])
func_5794 = relay.Function([var_5772,], output)
mod['func_5794'] = func_5794
mod = relay.transform.InferType()(mod)
var_5795 = relay.var("var_5795", dtype = "int16", shape = (2, 336))#candidate|5795|(2, 336)|var|int16
output = func_5794(var_5795)
func_5796 = relay.Function([var_5795], output)
mutated_mod['func_5796'] = func_5796
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4457_call = mod.get_global_var('func_4457')
func_4458_call = mutated_mod.get_global_var('func_4458')
call_5893 = relay.TupleGetItem(func_4457_call(), 0)
call_5894 = relay.TupleGetItem(func_4458_call(), 0)
uop_5895 = relay.atan(call_5893.astype('float32')) # shape=(2, 336)
uop_5897 = relay.atan(call_5894.astype('float32')) # shape=(2, 336)
output = uop_5895
output2 = uop_5897
func_5901 = relay.Function([], output)
mod['func_5901'] = func_5901
mod = relay.transform.InferType()(mod)
mutated_mod['func_5901'] = func_5901
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5901_call = mutated_mod.get_global_var('func_5901')
call_5902 = func_5901_call()
output = call_5902
func_5903 = relay.Function([], output)
mutated_mod['func_5903'] = func_5903
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5725_call = mod.get_global_var('func_5725')
func_5727_call = mutated_mod.get_global_var('func_5727')
call_5925 = func_5725_call()
call_5926 = func_5725_call()
output = call_5925
output2 = call_5926
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
var_5934 = relay.var("var_5934", dtype = "uint32", shape = (9, 2, 8))#candidate|5934|(9, 2, 8)|var|uint32
var_5935 = relay.var("var_5935", dtype = "uint32", shape = (9, 2, 8))#candidate|5935|(9, 2, 8)|var|uint32
bop_5936 = relay.bitwise_xor(var_5934.astype('uint32'), relay.reshape(var_5935.astype('uint32'), relay.shape_of(var_5934))) # shape=(9, 2, 8)
func_5928_call = mod.get_global_var('func_5928')
func_5930_call = mutated_mod.get_global_var('func_5930')
call_5943 = func_5928_call()
call_5944 = func_5928_call()
func_3479_call = mod.get_global_var('func_3479')
func_3480_call = mutated_mod.get_global_var('func_3480')
call_5952 = func_3479_call()
call_5953 = func_3479_call()
output = relay.Tuple([bop_5936,call_5943,call_5952,])
output2 = relay.Tuple([bop_5936,call_5944,call_5953,])
func_6001 = relay.Function([var_5934,var_5935,], output)
mod['func_6001'] = func_6001
mod = relay.transform.InferType()(mod)
mutated_mod['func_6001'] = func_6001
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6001_call = mutated_mod.get_global_var('func_6001')
var_6003 = relay.var("var_6003", dtype = "uint32", shape = (9, 2, 8))#candidate|6003|(9, 2, 8)|var|uint32
var_6004 = relay.var("var_6004", dtype = "uint32", shape = (9, 2, 8))#candidate|6004|(9, 2, 8)|var|uint32
call_6002 = func_6001_call(var_6003,var_6004,)
output = call_6002
func_6005 = relay.Function([var_6003,var_6004,], output)
mutated_mod['func_6005'] = func_6005
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5424_call = mod.get_global_var('func_5424')
func_5426_call = mutated_mod.get_global_var('func_5426')
call_6028 = relay.TupleGetItem(func_5424_call(), 0)
call_6029 = relay.TupleGetItem(func_5426_call(), 0)
const_6037 = relay.const([[7.868215,-7.893158,-4.291610,-0.217499,-9.374967,6.137721,0.345025,-3.121105,7.539471,-1.886288,3.950262,2.086839,2.455268,4.139664,1.760517,6.922970,-5.826662,6.238774,9.337846,-9.394275,6.800560,-1.872558,3.533163,3.873246,-1.654974,-1.522558,-6.138289,-0.212569,-1.937144,6.091166,-9.398343,-1.371479,-6.303600,6.485000,4.890019,-7.220097,3.340001,3.582682,0.379399,-3.527275,9.202852,9.119212,-0.009062,5.527418,4.424899,9.083526,6.358055,-8.330555,2.234072,3.651216,9.196123,-9.724998,-3.483906,2.952622,-5.610134,-5.888354,-4.700260,1.913743,0.423825,3.025934,-1.127556,-2.897400,3.909309,9.794778,5.756332,8.570687,-7.904705,2.798519,-9.999310,-8.353509,-8.561655,-1.202092,5.876645,-0.179619,-0.730230,0.146178,-8.842839,2.020698,2.948571,-6.278121,0.587653,3.761429,2.703868,3.296931,-5.387961,-1.183859,-3.967791,8.564268,5.543488,-9.748435,-0.262328,-8.427125,0.448920,-2.233827,-1.188754,6.549544,-7.002642,-0.662336,-7.447787,1.612097,7.965938,0.262311,-6.320576,3.875823,-0.202960,-7.226184,-1.141441,7.908180,-2.269068,-0.985016,4.824695,-7.809820,-8.006073,6.035699,-6.614130,8.443807,1.064930,2.896909,-8.536065,8.454246,-3.355425,0.801184,-7.157815,9.775811,-0.335557,0.782768,8.582549,0.394469,-1.680969,-5.823825,-9.168283,2.409238,0.463337,7.435461,0.624663,-3.533245,-3.368735,-4.167382,9.604656,1.286289,1.785408,4.969150,1.606127,2.263506,9.250357,-7.872914,1.952491,9.237795,7.283378,-4.207446,8.301651,-0.812971,-6.007984,-0.002639,-0.732232,9.016899,0.062806,1.998653,-0.952034,-5.014646,-9.881296,8.979739,-7.124094,-2.639708,0.335448,4.265672,-7.409976,3.686841,-1.116238,-9.477254,9.856872,1.114261,-2.397782,6.215653,8.218807,-2.532663,4.797637,3.626267,9.950212,2.474612,5.748310,7.958133,-3.725253,-5.428255,7.638130,-5.239447,7.581791,2.552364,-2.557008,-4.703282,-1.341139,2.112934,-1.580658,-3.153237,3.351627,-3.710021,-4.404027,-8.353921,-3.875581,5.157173,3.878547,2.227815,1.686433,-7.197259,5.493172,3.025335,8.345386,8.467104,-4.177421,3.672971,2.394259,-8.504059,-3.024195,3.498438,4.517228,-2.210537,-7.831754,3.172752,-1.680384,9.634065,-9.485460,0.317407,8.758292,2.673743,-0.430001,2.774705,8.659991,4.528776,-6.673539,-0.858107,-5.328576,-7.883422,-8.937199,-1.539934,6.652757,9.564574,3.836847,-4.768687,8.382932,-6.178146,-5.599058,-8.893858,9.911226,3.425972,-1.047799,4.022988,-4.067085,0.672835,-8.654889,4.888161,4.146429,5.287784,-2.582263,4.976867,-6.247073,0.947286,-2.831087,-1.903827,-0.945948,5.109830,1.769161,6.139357,9.229842,9.266114,-7.599577,0.681270,0.508433,-3.379913,-0.898747,7.039918,7.557508,-4.669619,-0.634053,2.778188,-2.828454,8.134985,-3.770057,-6.420081,7.939257,1.464575,-4.086084,9.480757,3.863954,7.203074,-9.197904,-4.981206,-9.668019,8.773004,0.013506,9.209724,2.251428,-6.078215,2.532886,6.361943,-4.554813,-0.481973,-4.931554,-1.456285,-4.696959,9.331087,-3.568058,-3.507884,-5.535255,-4.295961,3.658700,-9.459048,-6.227413,-2.959597,8.697257,8.570977,-8.584144,-6.598754,6.445346,-0.661965,1.891695,-8.662959,-2.287002,-7.707495,-3.465768,-3.884328,-7.348878,7.879453,4.627938,-7.009838,1.083193,-1.058069,5.356538,-7.866977,8.974433,-1.942490,7.464726,5.232958,-9.724109,-9.329172,-0.378042,-1.910656],[5.585825,9.410402,6.083347,7.029638,3.198275,-9.859112,7.262845,-6.001303,2.163017,9.458899,0.431019,-1.360292,-9.111978,4.396818,-7.969564,0.953115,8.036496,-7.957587,-5.363210,4.847433,-6.940299,-6.785789,8.862338,-8.474992,-1.304420,9.280295,-4.750209,4.996315,-8.156076,2.426345,-1.023701,6.771050,-2.876430,-1.240362,6.182884,-8.865986,6.510785,9.329519,1.389720,9.433068,4.366425,-0.314020,1.163472,-6.562284,-5.869421,-0.027822,-5.559625,-0.780364,4.523722,1.915141,-2.723165,-9.669225,3.378636,-0.235068,-8.822600,-2.506224,-5.046558,2.613680,-9.100504,-9.809787,-0.319026,6.782490,-1.887069,9.878086,-4.811017,-3.541768,-4.613600,-7.319978,7.633105,1.416276,-2.821646,4.985996,-6.032512,-8.991772,2.526273,7.374990,9.709620,-9.438905,-3.896109,-5.183138,1.421692,9.800471,0.241390,2.408148,1.450681,-8.166812,-9.097304,-1.486583,5.308489,0.173194,6.632558,-8.101177,2.161217,-2.380758,-3.506494,-4.510932,-9.532881,3.934913,8.709723,-1.761754,6.779458,-5.302334,-0.839984,-4.993119,-5.522841,-9.028930,-2.806608,-7.406260,-1.817264,4.302917,3.030171,-8.518743,-0.507978,-5.297891,-2.524059,-9.354463,8.295895,1.961467,1.822279,8.309150,3.211656,-3.325244,-7.625246,6.550727,4.206895,1.056287,-1.406152,-5.236608,-9.463622,-2.032279,7.892804,-8.077468,1.577379,9.444724,-8.429236,-7.785772,-1.516146,4.229395,-2.196965,4.889625,-2.422051,-0.850388,-4.029084,0.825479,4.842216,5.498156,-8.896920,-0.025663,7.329602,-0.866113,-2.514340,1.997250,5.193158,-5.795889,2.513519,-6.786963,-1.225978,-7.346563,7.691551,1.781073,0.417023,-4.697077,0.747663,-5.336497,-7.234459,-7.650578,3.967470,8.898878,-0.475314,-8.030458,-2.110348,9.148476,-3.734349,0.865580,7.656322,-0.982234,-9.389547,-4.089346,3.957972,-5.890485,-3.173790,6.265717,8.360579,-3.509672,-1.393188,2.605567,6.923190,8.071169,6.590887,-1.353121,-0.054821,0.992531,1.954179,-9.298856,-1.952297,-2.955311,4.197989,4.625927,-1.608358,-3.896632,-0.792046,1.161633,4.657668,2.330158,-5.525093,3.662253,3.956014,5.535027,3.031882,5.645681,-3.967464,-9.218388,3.291803,-0.737880,7.663444,-7.959172,4.602420,-0.999245,9.449893,8.194584,3.189504,-1.776016,8.781995,8.902333,0.081465,9.565369,-3.827278,8.717293,0.815566,5.896658,-9.733489,-2.599961,-3.330026,-2.580244,6.154403,7.453707,2.813876,5.236304,6.523548,6.739572,3.854771,-8.499023,-3.454207,-3.704722,-1.298138,-5.065456,8.631231,-2.836570,6.820121,9.037426,-1.133613,8.777134,-8.658080,-5.440003,4.841180,-9.225882,-4.253706,-8.340597,-8.533728,-2.652277,3.223220,-1.699214,-3.346201,-3.100936,9.485354,-8.672790,-4.660323,1.171173,-5.626715,-3.139718,1.768082,-5.197316,9.722487,-8.202983,3.663806,-5.158466,-9.411956,-4.864816,4.590815,-4.757006,-4.410369,-8.935748,7.500975,-1.116919,-1.294587,8.160812,3.362776,3.258467,1.660605,7.617760,8.848142,1.517649,-7.179569,-6.623051,-3.702572,-0.588610,5.789364,3.226746,8.117632,-0.757745,-7.511165,0.401707,6.902328,-0.624589,4.184076,-3.626565,-2.202237,-4.576323,1.534195,-3.754214,9.595241,-3.815316,-2.789135,7.538734,5.626423,7.327378,-2.868123,-2.733349,8.671547,-3.916379,-5.578117,8.078525,-3.436121,6.868585,-8.500992,7.686427,-7.983593,-9.285323,3.100607,-9.296530,9.808068,-9.955500,5.796871,-1.025542,4.196232,1.560377]], dtype = "float32")#candidate|6037|(2, 336)|const|float32
bop_6038 = relay.not_equal(call_6028.astype('bool'), relay.reshape(const_6037.astype('bool'), relay.shape_of(call_6028))) # shape=(2, 336)
bop_6041 = relay.not_equal(call_6029.astype('bool'), relay.reshape(const_6037.astype('bool'), relay.shape_of(call_6029))) # shape=(2, 336)
func_3681_call = mod.get_global_var('func_3681')
func_3684_call = mutated_mod.get_global_var('func_3684')
const_6045 = relay.const([-6.450665,3.512000,9.071358,0.770896,-4.026829,-6.986299,7.825376,1.230106,-3.103843,-3.686370,5.057379,-5.441387,-0.312793,7.698439,6.737215,-4.875811,-0.404463,5.337490,-0.662597,-9.651658,9.983930,6.664816,-2.695171,-3.037187,-0.408870,-5.469017,-0.875035,-8.013277,-0.387797,-6.804716,4.285967,7.080767,-5.872792,4.659440,5.087911,8.774248,-9.773139,8.718795,-1.366277,4.773642,-7.834828,-1.066737,-0.896576,3.790767,-8.726047,-8.620048,-6.446483,-3.117720,8.405912,1.760647,9.111170,9.775854,2.875226,1.900323,-2.799239,4.431630,-4.987131,8.676000,-2.490027,6.727049,-4.995041,9.957317,1.109780,1.174361,0.311294,7.707204,-5.325945,8.327010,9.137403,3.704997,6.864670,-3.992434,-2.566808,2.608150,6.751582,2.097794,-3.317809,-9.728944,-2.634722,-1.167790,1.834271,4.398549,-1.310469,8.456508,3.040460,9.047289,3.554931,-7.761242,3.081697,7.929294,-8.867016,-5.052125,4.278775,-8.554455,2.393038,3.448549], dtype = "float32")#candidate|6045|(96,)|const|float32
call_6044 = relay.TupleGetItem(func_3681_call(relay.reshape(const_6045.astype('float32'), [8, 12])), 2)
call_6046 = relay.TupleGetItem(func_3684_call(relay.reshape(const_6045.astype('float32'), [8, 12])), 2)
func_1440_call = mod.get_global_var('func_1440')
func_1443_call = mutated_mod.get_global_var('func_1443')
var_6074 = relay.var("var_6074", dtype = "int16", shape = (168,))#candidate|6074|(168,)|var|int16
call_6073 = func_1440_call(relay.reshape(var_6074.astype('int16'), [7, 3, 8]), relay.reshape(var_6074.astype('int16'), [7, 3, 8]), )
call_6075 = func_1440_call(relay.reshape(var_6074.astype('int16'), [7, 3, 8]), relay.reshape(var_6074.astype('int16'), [7, 3, 8]), )
func_4077_call = mod.get_global_var('func_4077')
func_4078_call = mutated_mod.get_global_var('func_4078')
call_6094 = relay.TupleGetItem(func_4077_call(), 0)
call_6095 = relay.TupleGetItem(func_4078_call(), 0)
func_4410_call = mod.get_global_var('func_4410')
func_4414_call = mutated_mod.get_global_var('func_4414')
const_6098 = relay.const([5.942047,-8.396359,-4.224874,5.195531,6.979163,-5.172382,2.905878,-4.358389,7.108472,7.996198,-8.385106,-8.380200,-7.158610,-1.088412,6.133373,-4.788967,-1.851756,0.147874,-1.356997,5.648578,7.473918,-8.198422,9.085739,3.700979,-4.936457,-6.138917,-3.188103,3.017533,-6.748552,5.901974,1.944398,7.065481,-4.619247,-4.039286,0.949730,-2.735176,9.709778,-5.939888,5.457495,2.456804,-9.708565,-2.359885,-8.413629,7.539590,3.552008,-3.654458,-5.320361,-1.100065,-9.441748,-5.540438,8.328336,-8.614587,0.555214,3.214434,-1.753636,-9.191173,9.176928,-4.993424,8.644579,-5.802964,-2.114172,7.161060,-2.999259,0.263552,-5.218697,5.596620,-2.530036,-2.545697,-5.592194,-1.042512,-7.558273,4.789538,1.804712,8.623092,0.655865,9.151479,8.018472,-8.731400,-7.430825,-0.521196,3.985985,-6.493076,-3.060161,1.140182,6.371110,9.672642,7.257049,7.297949,-7.271715,1.964661,-9.755413,3.927866,9.008049,-1.370306,2.922180,-3.264680,-6.847761,-6.808469,9.560304,3.180437,6.462731,-0.751427,7.704807,3.583851,-4.746437,4.042519,4.930762,-3.306141,-1.687647,8.848059,-8.370404,5.868890,-1.948995,6.075337,8.411553,-3.693051,5.017930,1.782208,-4.013228,0.887662,7.132526,-5.835567,4.698059,7.393732,9.187682,-4.058660,-2.213907,-5.700715,8.073464,-8.918631,-8.565070,-6.467890,4.698548,-1.777574,-7.390267,2.246545,-4.280720,2.903502,-4.254399,4.855723,2.314155,4.489485,6.150330,-3.519708,5.511663,-4.457678,-7.747823,-6.344480,-8.827471,4.722484,-5.781522,1.939405,-1.027506,-0.529984,1.116424,-1.272303,8.485842,4.561884,9.330134,-0.130749,-2.637339,-9.658743,2.860598,7.072786,1.525061,-7.902308,5.718754,-8.193799,-5.640471,-1.793875,7.910893,-1.938199,0.090809,4.470259,-9.002299,0.002307,-3.671260,9.009306,-2.207909,-1.945991,9.225730,5.269497,-2.103110,8.889038,8.960935,-8.620084,-0.794031,6.411300,-3.131098,2.966425,-2.010615,-4.154023,-5.183839,-2.079530,-8.302389,9.665227,-1.054214,-2.676485,-5.214161,5.068745,0.537124,-5.029580,4.821321,1.402417,7.179468,-1.424840,-3.937508,-1.738999,-7.810428,3.823599,4.932703,-9.427003,-7.932674,-5.444897,-7.948168,-7.315697,-4.483564,-9.115997,-0.678588,1.789096,-1.325365,-9.394231,-0.556288,0.980755,4.701834,9.942099,6.053897,-7.426183,-5.177680,3.631047,6.391394,6.300408,-5.011714,7.493997,3.219760,-9.954408,-3.236440,-2.038467,-5.440915,9.497800], dtype = "float64")#candidate|6098|(240,)|const|float64
const_6099 = relay.const([True,True,True,True,False,False,False,True,False,True,False,False,True,True,False,False,False,False,False,False,False,True,False,False,True,True,False,False,True,False,True,True,True,False,False,True,False,False,False,True,True,True,True,False,False,True,False,False,True,False,True,True,False,True,False,True,True,False,True,False,False,False,True,True,True,True,False,True,True,False,False,False,True,True,True,True,True,True,False,False,False,True,False,False,False,False,True,True,False,False,False,False,False,True,True,True,True,True,True,False,True,True,True,True,True,False,False,False,True,False,False,True,True,False,True,False,False,False,True,False,False,True,False,True,True,True,False,False,False,True,False,False,True,True,True,False,True,True,False,True,False,False,False,True,True,False,True,True,False,True,False,True,False,False,False,True,False,False,True,False,False,False,False,True,True,True,True,True,True,True,False,True,True,False,False,False,False,False,False,True,True,False,False,True,False,False,True,False,False,False,True,False,False,True,True,False,True,False,True,False,True,True,True,True,True,True,True,False,True,True,True,False,True,True,False,False,True,True,False,True,True,True,False,False,True], dtype = "bool")#candidate|6099|(225,)|const|bool
call_6097 = relay.TupleGetItem(func_4410_call(relay.reshape(const_6098.astype('float64'), [6, 4, 10]), relay.reshape(const_6099.astype('bool'), [225, 1]), ), 0)
call_6100 = relay.TupleGetItem(func_4414_call(relay.reshape(const_6098.astype('float64'), [6, 4, 10]), relay.reshape(const_6099.astype('bool'), [225, 1]), ), 0)
func_4077_call = mod.get_global_var('func_4077')
func_4078_call = mutated_mod.get_global_var('func_4078')
call_6101 = relay.TupleGetItem(func_4077_call(), 0)
call_6102 = relay.TupleGetItem(func_4078_call(), 0)
func_5317_call = mod.get_global_var('func_5317')
func_5318_call = mutated_mod.get_global_var('func_5318')
call_6119 = relay.TupleGetItem(func_5317_call(), 0)
call_6120 = relay.TupleGetItem(func_5318_call(), 0)
uop_6121 = relay.erf(const_6037.astype('float32')) # shape=(2, 336)
func_3905_call = mod.get_global_var('func_3905')
func_3906_call = mutated_mod.get_global_var('func_3906')
call_6127 = func_3905_call()
call_6128 = func_3905_call()
uop_6131 = relay.sinh(uop_6121.astype('float64')) # shape=(2, 336)
func_4975_call = mod.get_global_var('func_4975')
func_4977_call = mutated_mod.get_global_var('func_4977')
call_6140 = relay.TupleGetItem(func_4975_call(relay.reshape(const_6099.astype('bool'), [225,])), 0)
call_6141 = relay.TupleGetItem(func_4977_call(relay.reshape(const_6099.astype('bool'), [225,])), 0)
uop_6142 = relay.log(uop_6131.astype('float32')) # shape=(2, 336)
bop_6152 = relay.maximum(uop_6142.astype('uint32'), relay.reshape(uop_6131.astype('uint32'), relay.shape_of(uop_6142))) # shape=(2, 336)
uop_6156 = relay.sin(uop_6131.astype('float32')) # shape=(2, 336)
output = relay.Tuple([bop_6038,call_6044,const_6045,call_6073,var_6074,call_6094,call_6097,const_6098,const_6099,call_6101,call_6119,call_6127,call_6140,bop_6152,uop_6156,])
output2 = relay.Tuple([bop_6041,call_6046,const_6045,call_6075,var_6074,call_6095,call_6100,const_6098,const_6099,call_6102,call_6120,call_6128,call_6141,bop_6152,uop_6156,])
func_6158 = relay.Function([var_6074,], output)
mod['func_6158'] = func_6158
mod = relay.transform.InferType()(mod)
mutated_mod['func_6158'] = func_6158
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6159 = relay.var("var_6159", dtype = "int16", shape = (168,))#candidate|6159|(168,)|var|int16
func_6158_call = mutated_mod.get_global_var('func_6158')
call_6160 = func_6158_call(var_6159)
output = call_6160
func_6161 = relay.Function([var_6159], output)
mutated_mod['func_6161'] = func_6161
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6176 = relay.var("var_6176", dtype = "float32", shape = (5, 15, 14))#candidate|6176|(5, 15, 14)|var|float32
uop_6177 = relay.cos(var_6176.astype('float32')) # shape=(5, 15, 14)
output = uop_6177
output2 = uop_6177
func_6185 = relay.Function([var_6176,], output)
mod['func_6185'] = func_6185
mod = relay.transform.InferType()(mod)
mutated_mod['func_6185'] = func_6185
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6186 = relay.var("var_6186", dtype = "float32", shape = (5, 15, 14))#candidate|6186|(5, 15, 14)|var|float32
func_6185_call = mutated_mod.get_global_var('func_6185')
call_6187 = func_6185_call(var_6186)
output = call_6187
func_6188 = relay.Function([var_6186], output)
mutated_mod['func_6188'] = func_6188
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3479_call = mod.get_global_var('func_3479')
func_3480_call = mutated_mod.get_global_var('func_3480')
call_6214 = func_3479_call()
call_6215 = func_3479_call()
output = relay.Tuple([call_6214,])
output2 = relay.Tuple([call_6215,])
func_6216 = relay.Function([], output)
mod['func_6216'] = func_6216
mod = relay.transform.InferType()(mod)
mutated_mod['func_6216'] = func_6216
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6216_call = mutated_mod.get_global_var('func_6216')
call_6217 = func_6216_call()
output = call_6217
func_6218 = relay.Function([], output)
mutated_mod['func_6218'] = func_6218
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3946_call = mod.get_global_var('func_3946')
func_3947_call = mutated_mod.get_global_var('func_3947')
call_6241 = relay.TupleGetItem(func_3946_call(), 0)
call_6242 = relay.TupleGetItem(func_3947_call(), 0)
var_6251 = relay.var("var_6251", dtype = "bool", shape = (16, 5, 7))#candidate|6251|(16, 5, 7)|var|bool
bop_6252 = relay.add(call_6241.astype('uint8'), relay.reshape(var_6251.astype('uint8'), relay.shape_of(call_6241))) # shape=(16, 5, 7)
bop_6255 = relay.add(call_6242.astype('uint8'), relay.reshape(var_6251.astype('uint8'), relay.shape_of(call_6242))) # shape=(16, 5, 7)
func_4457_call = mod.get_global_var('func_4457')
func_4458_call = mutated_mod.get_global_var('func_4458')
call_6261 = relay.TupleGetItem(func_4457_call(), 0)
call_6262 = relay.TupleGetItem(func_4458_call(), 0)
func_4044_call = mod.get_global_var('func_4044')
func_4049_call = mutated_mod.get_global_var('func_4049')
const_6269 = relay.const([6.558448,3.236612,5.185322,-3.218467,5.456132,-9.847913,-0.336691,0.388810,-6.444253,-0.837140,-0.789478,-2.909006,2.314798,-7.466508,2.606592,-1.870739,3.084183,-7.266381,-8.371126,4.447772,0.250021,-9.357170,4.881760,-2.901826,-9.924776,-6.492886,0.324978,1.454097,8.939301,8.317764,-0.585452,4.569913,9.513181,-2.467501,-5.040002,4.480517,5.338973,-1.254337,9.094720,-0.883330,8.093610,-6.758762,-0.398073,7.224063,4.457592,-8.367164,-8.866773,-2.999487,9.167978,6.339742,-2.908212,8.571017,7.482686,1.274160,-4.752328,-6.901233,-8.988531,-5.747398,-2.344117,8.053957,-4.215404,2.431163,8.647655,-8.304428,5.849145,1.755549,-2.601619,7.399564,-8.303195,-8.242987,9.259434,-6.458861,-5.255248,-9.965023,-1.250761,-7.056055,7.894090,-4.906991,3.257936,7.233775,-2.522143], dtype = "float64")#candidate|6269|(81,)|const|float64
const_6270 = relay.const([-1.631488,5.408457,5.961774,0.953991,-5.777422,8.877227,0.656451,-7.309122,-6.587658,5.424919,6.986298,-0.937689,6.158143,5.706866,7.504424,-4.575159,-1.393730,7.057900,-9.723604,8.279206,-0.766621,8.759624,-9.319665,7.005576,1.346302,1.040505,-9.182278,5.503232,0.097892,-7.226967,-9.456719,-8.935303,-0.852375,8.092866,9.387840,5.122483,6.738620,2.923592,6.174114,-8.953432,2.578436,2.019033,5.648636,-3.529587,9.972682,-7.678449,5.172366,-7.873309,-0.564283,-2.368050,-5.357166,6.747048,-5.941404,0.960440,4.091209,-0.471350,-5.110364,-9.669960,-6.682033,-0.771808,0.481848,-3.218201,7.804865,-6.127346,-3.644579,2.422666,7.830273,-7.032457,1.553599,8.237735,4.277161,-8.378564,1.358057,-5.975750,1.406683,0.121027,2.425123,4.944361,-6.897620,-7.179839,-7.827920,0.506919,-2.878935,4.475923,2.299339,-3.070234,-4.431710,-6.891343,-3.749663,9.674894,0.533943,-3.388821,-2.621246,-7.488397,-2.607867,1.982459,-7.611614,-4.576359,-6.723151,3.549914,-3.346164,2.042132,-6.921527,-6.310772,-8.367687,-3.146751,-9.879241,-6.866335,-8.243410,5.701506,7.216691,1.200604,9.522090,-9.706045,5.058361,4.457762,1.955088,-0.361917,5.376020,-1.220959,-4.614368,6.807937,-7.749813,-4.017188,-2.891290,5.506356,-5.871331,-9.442772,-3.796320,-0.566472,-3.740546,7.503084,-0.992923,8.171385,-1.560646,4.916345,-4.006978,1.850084,-8.328815,2.449863,4.470235,-0.616537,0.805088,5.409850,3.625424,1.164061,7.491809,3.192882,-7.549438,5.672188,5.293935,5.452313,-2.575698,-2.819905,-9.007029,6.034049,-9.520188,-0.548455,-5.091290,8.549116,6.113791,9.012791,4.194363,-8.621138,7.311425,-8.578341,-9.188819,-6.889640,-8.175269,8.943686,-9.411974,-6.869747,-0.320863,-1.242357,-1.467083,-3.765653,-2.257318,-7.937994,-6.897150,1.424801,2.826105,-6.113439,-2.261052,-1.270126,4.108450,8.074774,-6.502782,-6.843695,-1.240089,-8.749618,-6.939634,-8.619773,-9.996120,-7.533020,6.875529,9.190480,5.544783,-1.163164,-1.524205,-9.544989,-5.137988,-1.761557,4.895043,0.373993,9.553490,-6.162691,-5.086676,2.721349,-4.748227,-1.036551,0.619055,-4.719808,9.658803,-2.839659,9.726247,-9.295597,4.540122,-8.020821,1.771659,-0.069837,7.455287,0.566682,-7.038558,4.110575,-5.059364,-9.980202,0.981420,2.132864,-2.970679,-2.248191,-1.619939,7.381821,2.726520,4.945133,-3.788447,-9.367026,-2.026649,6.163961,-5.038770,3.852907,-6.548471,-0.941542,-0.747420,3.508873,-4.140731,-4.975899,-8.978544,-2.976269,-9.147906,-7.152548,3.701719,-2.382214,-3.458405,-7.325339,-3.447922,-8.648635,-8.764944,-8.250980,-1.380657,2.505177,-4.044868,0.517176,5.046480,-8.599170,3.397106,-2.984605,6.982494,6.529052,8.619623,-6.782831,7.312199,-3.887134,-2.368031,6.040734,-6.056140,8.365790,-8.496515,2.766843,-9.400201,0.219362,0.217232,-3.490885,7.155135,-2.201666,-7.083154,-0.371148,6.709342,7.944063,-2.733003,-1.252166,0.334754,6.964051,8.451390,9.805116,-5.261050,1.938556,4.169197,7.641544,9.595673,2.407518,-7.965941,-4.036393,-4.660522,8.854132,-6.749802,-7.262269,3.893562,0.167609,-8.084719,-2.837624,-7.764903,-7.198756,-7.078816,-8.982221,-6.320301,2.575759,1.068960,-2.163203,6.340248,-1.616121,-8.363132,1.832805,-7.880701,-2.944405,3.336620,-7.758890,-0.626914,0.158911,-2.904186,9.931281,6.105630,0.895408,-2.831992,3.919493,-1.350301,8.970228,-3.557224,-3.648606,8.656550,0.095124,-8.173613,-0.828102,5.484201,3.150640,2.745251,-6.142192,2.100454,-5.657106,7.505077,1.445064,0.965515,-9.445947,9.892748,4.037271,9.683042,4.626410,-8.282580,2.818439,-1.268998,8.704333,7.360068,-4.118063,3.940521,-6.776866,-5.519487,-5.452781,-3.116338,7.305398,-2.999709,-6.507512,-9.986933,4.341593,-9.124418,-0.442474,0.729910,-7.991007,2.418025,7.491526,8.101497,5.273250,2.519209,-1.596056,0.578843,4.016884,-6.725986,7.928943,3.657020,6.169366,9.913942,-7.683224,6.655384,1.866073,-9.967607,8.776392,-4.755654,8.857372,0.105095,2.558297,-6.673091,-2.032574,6.877532,8.920925,-5.434341,-9.088555,-4.637735,-2.292916,8.062229,-3.286015,-0.726502,-6.262188,-5.809073,-0.208326,9.906682,-1.327388,-1.079050,-4.721519,0.939005,-4.249387,-3.616394,0.517949,-1.431328,-8.747810,-6.082509,9.471523,-0.655346,4.349734,6.031074,-3.375912,-1.665550,-3.482796,6.780799,-5.840973,-8.101975,-0.801343,1.126944,2.096874,7.425175,7.209525,-6.461690,-1.319684,-1.902394,-8.048690,4.947615,-0.066828,2.353732,-9.436116,2.956396,6.641200,-5.608368,-3.433944,-9.315974,6.085842,0.257570,8.706935,1.143720,9.808635,9.188708,8.331770,-5.184538,-2.883694,7.181105,5.027587,8.583126,-5.415371,-9.446812,9.095325,2.240035,0.043056,-5.666764,-8.127705,-7.671626,0.800280,0.141055,8.400817,4.386807,-5.207108,-5.957893,7.469112,-4.689334,6.718623,2.193586,2.823415,4.817432,8.054264,8.274267,4.412497,7.196766,-1.062731,-4.714369,2.158451,3.517694,-5.946981,5.522194,-6.261787,5.296843,-2.068397,-7.219705,5.242854,-6.360831,9.244367,1.281754,-7.100134,-2.280268,8.270987,-6.470087,-7.127867,-5.413782,0.571169,-9.593019,-2.026353,-5.512668,-0.413474,-1.012880,-6.306134,7.894165,8.534602,9.583982,9.344881,-7.968519,-2.647207,5.384676,-7.270296,4.397032,7.644335,3.388276,7.185754,4.460412,6.778581,-0.308994,-3.000436,1.600019,-1.941168,1.985555,-4.482366,-5.037698,-4.167162,5.184224,-0.428282,6.982834,1.249633,6.534939,-6.784116,-2.130299,-1.756877,5.751834,-1.112528,-2.766922,2.719108,3.409944,8.344826,-3.288667,9.663837,6.143603,-1.400670,-7.534946,5.103247,3.571366,-0.295839,6.299881,-9.419395,4.680247,-1.039946,4.097663,-4.515682,7.429465,-2.294262,0.137468,-5.074575,6.521936,7.589777,-3.084620,8.446179,-5.974696,2.073096,9.886141,9.934275,9.145206,-8.308065,6.285319,3.459323,5.223836,7.416638,6.150537,4.388054,-1.832874,-0.169838,9.429734,-8.471577,1.556868,-2.506077,2.563046,-6.433712,9.912777,7.871776,3.820670,7.779112,7.055999,5.876420,-1.204294,6.503258,-3.670713,8.626887,-2.078807,5.104125,-9.507448,-3.287523,5.906789,-7.998258,0.665406,-6.670775,-5.641862,7.863735,-6.478549,-8.283336,8.176020,3.040831,-8.456146,-2.234471,0.251597,-1.744524,5.168839,5.054374,5.062168,7.275986,-2.083603,2.082639,1.679784,-3.331343,-7.862265,6.837171,-1.461174,7.281000,2.945096,1.398941,5.281623,-8.360520,-3.120263,-7.020657,0.131395,7.184069,6.352419,-1.062942,0.317440,-2.976072,-9.309342,-4.536494,-6.194528,2.326821,1.605223,-2.147716,-2.576800,8.530993,1.986701,4.044398,1.402457,-8.565660,1.282212,0.769383,3.114778,-2.701367,7.599618,-7.672805,-0.772856,-5.508519,7.133910,0.439681,7.231280,-1.203362,-3.221069,-4.138466,-0.415349,-7.681655,2.991922,9.566799,6.853161,-1.167846,-9.627236,-2.179879,-6.570173,-6.229300,-0.985433,-0.927168,-0.544647,-1.086523,-3.531362,-7.092108,7.057665,-7.573898,-4.806384,8.222423,-4.318620,1.151749,-2.657194,8.161445,-3.650631,-5.564642,6.635063,-8.990999,-4.462760,-4.127547,0.245968,7.943602,8.765703,-4.171147,2.134015,3.643651,6.837063,-6.238065,2.870675,2.927244,5.733725,-4.235562,-2.767303,-3.574083,1.113266,3.490112,1.300868,5.969762,-8.748745,7.986382,1.263390,1.845076,9.181822,-4.610101,-5.602573,-9.949449,-4.396680,-7.323541,5.844730,3.690162,-2.033850,-8.565087,4.339827,-2.668899,0.936363,-6.445849,3.656511,2.874250,4.083304,5.087299,9.406414,-0.969561,-0.519656,-8.011441,5.891032,-9.538098,-8.504074,-1.539167,-6.046780,-6.033475,-3.228862,-6.530946,-7.946670,-6.283380,5.618980,1.447564,9.406942,-3.013475,4.321686,4.792379,-1.042199,-3.174235,-6.191309,6.821739,2.774681,-4.830755,-4.985900,2.638477,4.466059,-5.252238,5.985121,1.297918,2.811439,-9.257687,9.350040,-7.390277,9.081288,-3.175193,2.985096,-0.683099,6.218454,-7.447516,1.860824,8.095095,6.817293,-2.724038,9.410958,9.880801,7.622553,9.414944,1.055941,5.714615,-7.977830,5.443325,0.171686,4.055552,-0.238544,-6.712965,9.957795,-7.068848,0.524119,-0.346903,0.387837,-9.182414,4.436499,7.382570,0.139105,-2.924372,-5.764953,2.910209,6.376108,2.902096,-0.842388,-5.543517,1.813078,-7.219474,3.467459,4.571219,-8.877664,6.528587,-9.702393,-8.409102,3.214070,8.880089,-3.793819,7.015004,7.165252,-9.940509,-6.577323,-2.078656,4.137726,1.938008,7.556803,4.678456,-0.037158,6.867850,0.746541,-4.721871,-6.878180,5.074489,-2.445830,6.466381,7.189319,2.373580,-4.667436,1.686855,-2.947284,-7.531682,2.391132,5.712052,-5.439721,-8.000937,-3.677885,2.356519,0.110474,-0.846610,6.367704,0.585282,6.386016,5.106521,-4.735665,4.974047,1.330070,-5.747110,-4.549848,-1.655313,6.839985,-8.957752,7.050740,-5.575177,-5.263944,-0.998656,-0.415393,-8.331059,-9.951223,7.766495,-9.740951,7.912135,-0.164625,7.174577,1.765804,-7.938895,-7.411029,-6.727780,-3.001726,-4.751330,6.860835,-1.028553,5.453185,4.186460,-3.552759,-1.586187,-2.000316,-4.735743,-8.419392,6.609364,0.923638,-8.964854,-3.963796,3.958768,1.529034,-6.853239,-4.463808,0.148979,2.638065,5.757365,8.454270,4.003921,6.549838,1.779151,7.612711,9.069129,-5.769566,-4.314643,5.103636,1.946878,-1.674441,7.674605,-9.335190,-0.818871,-8.955339,-6.088100,6.032563,9.246169,8.116489,-1.587726,6.321406,-9.898610,7.224413,-6.717158,-2.800771,-6.211197,1.870737,-7.857034,-0.086401,-6.142737,-7.639926,-0.833167,-7.589475,2.918850,-7.691800,-9.976782,0.650650,9.921143,8.464029,5.606218,2.432363,-5.479782,-3.800893,3.231709,5.817398,2.948502,-9.373078,-7.433643,8.161201,-7.953598,4.864552,3.586944,3.072158,-5.643012,-7.283714,0.389920,4.645552,1.617892,-7.955581,-6.696620,-1.018764,2.343831,4.475427,3.951039,7.132656,4.530314,-0.010906,-2.913246,9.113902,-4.312889,-6.644719,-0.028146,-0.321272,7.184502,-1.184483,-8.498602,1.487787,1.210611,1.594721,7.804317,-7.375583,-3.160435,9.637627,4.101043,3.433643,1.229071,5.360157,7.869966,0.621331,-9.152681,-8.506556,-9.091753,-1.500928,-0.855151,-4.999221,0.188725,-5.572726,7.407853,-3.119009,4.949319,-6.583461,4.684639,-6.200707,2.610865,-8.779384,1.477559,3.444473,-4.332544,9.002487,2.825119,0.489688,-9.244972,-8.037919,4.396036,-1.032453,-0.366406,6.272267,-4.391792,-3.132244,7.755193,4.802231,8.443819,-1.258111,8.302056,8.690103,2.901052,5.866334,-2.125392,7.155412,-3.512065,-0.758999,2.721204,-0.210845,4.656275,6.257206,7.018058,3.938496,0.682174,2.947561,7.293851,-9.724978,5.764631,7.141840,3.160549,5.492192,-6.374134,7.505724,-6.761601,-1.486735,-1.340888,-5.142958,-0.582747,1.324001,-9.755277,-8.648864,6.401439,-4.423958,-7.095657,-3.066276,3.494656,3.488479,-8.264758,6.159469,9.232235,-8.530459,4.436867,6.103881,8.401513,-0.021257,7.234826,3.432530,9.217489,0.076735,2.657347,3.503215,-2.561316,1.281908,5.930147,5.050394,-0.948594,1.788798,-0.888980,4.243601,4.303442,1.496697,9.581706,8.130829,7.070942,-6.224455,-0.893564,2.982791,8.835901,0.002358,1.429484,4.086500,2.317169,3.703578,1.905651,4.703773,-6.255499,-1.519222,2.091966,-4.407139,-6.171347,-1.722319,5.294375,4.675998,-3.265456,4.476451,8.071919,1.659364,7.576072,5.155433,5.034372,1.009983,6.563110,2.212012,1.647281,1.233882,8.885448,2.470717,0.049289,1.833061,1.691200,8.423206,1.194589,5.751226,-0.074936,3.472747,7.546191,2.045515,-8.597525,-5.075283,9.395385,-6.540987,3.597695,2.607124,-9.264046,-9.365936,7.237875,0.621173,-1.451391,-3.384239,5.816943,-5.974126,-3.028799,4.559841,0.325823,0.601207,-3.588512,2.365379,9.595434,-8.593130,4.946293,2.994896,5.398853,3.334831,-8.601364,-3.354482,2.982276,-3.276964,-2.184917,0.722235,5.452349,-4.620900,-5.678156,3.063914,-3.412495,4.265819,-1.806601,8.896033,5.433837,8.199407,-5.266413,4.499995,1.772448,5.841281,-2.573997,9.373070,3.944886,3.131235,1.571486,6.657015,-2.508963,7.776659,-2.151207,-6.851889,3.040719,7.437215,5.117270,3.361132,-0.955891,6.935190,0.117400,4.221716,-3.950582,-8.260652,8.007178,-9.871462,0.748476,7.122410,-1.353142,6.736653,5.435079,9.745169,-4.570557,6.520067,6.767317,7.142872,5.176474,-6.396087,3.403330,6.890777,-0.958025,-2.639548,3.320312,7.247347,-4.429402,7.869673,3.208066,-2.342957,-8.672140,8.387978,-9.451998,-2.890072,4.855605,-2.630673,-3.702420,8.944292,2.119108,-4.171072,0.502303,-0.967348,-9.929958,-0.268228,-3.077431,1.735848,-0.986199,-5.260782,3.731113,2.087300,4.825680,6.147485,1.915166,1.575504,9.312445,-7.541817,9.510321,-8.841179,-3.923156,-2.685608,5.475628,1.099058,-0.643680,8.339067,0.839710,-3.603011,-1.888592,-0.363443,-0.728147,-5.906143,3.294267,0.357642,4.374831,-3.264346,-2.188195,-9.370998,0.600422,3.785905,5.923540,4.466006,5.293947,-0.684997,-6.504195,-7.022720,-2.907273,-5.528002,3.872549,-7.155519,1.661917,-9.607396,3.129588,2.079604,8.622350,-5.880558,0.484715,8.356928,7.388719,-5.658712,-2.527356,1.620443,1.686422,-6.337483,9.370072,7.597671,4.376037,-0.837740,-1.518614,8.382315,-1.128827,1.685659,-6.764040,3.465746,-1.057736,4.075073,-7.214733,7.319409,-0.331961,-3.448704,-7.254177,-6.248776,2.000055,4.138462,-8.314881,8.878769,-3.309523,2.258184,0.232190,0.266282,-4.665963,-1.849685,4.897962,6.816236,3.043268,4.852341,1.019880,-1.902512,-9.408735,0.672431,-8.101976,9.216953,6.955685,0.388771,9.150278,-8.256861,9.215093,-1.497081,-5.235247,-9.051374,6.517942,1.476137,9.525559,-0.572956,9.713226,1.558667,-5.174929,6.616314,0.923582,5.779398,4.418367,-4.149682,-9.887038,2.945155,-5.021390,4.601973,1.992190,1.375893,-0.856931,-3.517913,3.015646,9.953551,-0.788401,3.773980,-9.635458,1.598271,-4.516182,-1.365497,-2.571608,6.515904,-7.519082,4.744420,2.202626,-7.760146,-4.650896,-1.486929,-8.638197,1.302216,-2.905693,-7.418225,9.151870,-1.586923,-2.323030,5.701535,-2.553954,7.211150,4.167011,-1.174052,9.620875,-3.619342,2.849430,0.832671,-0.469741,-2.056463,8.088332,1.824427,-1.457050,-5.850462,1.316862,-1.289875,-7.950659,-0.206510,-8.291223,4.662229,4.660491,0.220938,-7.263881,9.287772,6.174842,9.111880,-4.757498,-4.874538,-3.268051,3.049370,-2.142166,6.686535,-1.969268,-7.910016,-1.996584,-2.982605,3.024189,-5.140075,3.257140,-7.022118,7.105039,4.330884,5.776075,0.456767,1.408448,9.915854,-4.246680,-3.440078,-2.236764,2.214487,-9.662276,-9.917358,3.011775,7.402785,-5.600087,1.831959,1.920924,-0.985903,-7.968968,-4.281658,-9.290341,9.533082,-0.832840,5.532202,-8.909690,9.081460,1.651632], dtype = "float64")#candidate|6270|(1456,)|const|float64
call_6268 = relay.TupleGetItem(func_4044_call(relay.reshape(call_6261.astype('int16'), [672,]), relay.reshape(const_6269.astype('float64'), [27, 3]), relay.reshape(const_6270.astype('float64'), [1456,]), ), 9)
call_6271 = relay.TupleGetItem(func_4049_call(relay.reshape(call_6261.astype('int16'), [672,]), relay.reshape(const_6269.astype('float64'), [27, 3]), relay.reshape(const_6270.astype('float64'), [1456,]), ), 9)
func_2728_call = mod.get_global_var('func_2728')
func_2730_call = mutated_mod.get_global_var('func_2730')
const_6275 = relay.const([-8.681225,-9.152056,-8.294949,-4.429825,0.667600,-1.143752,-1.113975,4.582662,6.211712,-3.914576,5.873394,-8.534974,-1.186801,-7.765968,6.520503,-4.539349,8.553565,3.144204,1.913698,-9.320903,9.803071,-6.740826,-0.132186,1.811791,6.574097,-9.771867,-1.196339,-3.459384,9.699625,-7.551606,-4.430538,-5.039062,6.077976,-3.299055,7.600676,0.155045,5.838209,9.063701,-8.808109,6.038356,-5.547878,-2.627661,-6.421069,5.607736,8.634237,-3.671839,-1.281292,9.835987,-9.068725,6.234440,6.222096,-6.420188,-1.059331,-2.062742,8.638216,2.323373,-8.671287,-8.528941,-7.683334,-4.183702,0.098623,-0.729461,-4.595116,5.920524,4.023555,-8.237347,-1.385231,7.288373,-7.399379,9.956658,7.286779,1.607609,-4.978676,-6.799015,-8.394655,-2.901774,-5.232711,4.201394,0.959698,7.183509,2.546410,5.233905,6.300937,8.545717,-8.036280,8.094498,2.528233,3.936138,-4.177102,-3.533074,9.243742,-5.234828,0.455202,-1.702853,-4.089097,7.525800,8.632027,4.576036,9.711130,0.388779,0.143031,9.303965,3.823718,-6.089773,8.920058,-5.414552,-7.794468,-5.943962,3.475932,-9.880627,-3.005818,7.063198,-4.008458,-4.069273,3.763202,3.413855,-7.520220,1.177441,-7.954103,4.581461,4.597669,-5.944516,-3.810286,8.529650,1.779849,-5.053696,-8.472116,2.786007,-3.035641,-3.500133,5.251825,1.196798,1.128574,-5.394433,-5.863014,0.306434,5.452922,7.351625,-0.606199,0.303982,-4.900017,5.066952,-5.295523,1.752934,6.708433,-3.171565,-0.009621,-0.881878,2.518225,1.426091,8.127349,2.685410,-0.828854,-3.641488,4.559597,-7.747704,5.635293,-6.480440,-1.476971,3.630223,-1.798583,4.062040,4.599939,-5.585911,-7.532156,-9.724638,-1.706221,-1.505125,6.604946,4.064913,6.109605,-5.733764,0.366653,-5.825491,8.739397,5.873814,9.202600,-0.320797,3.569733,0.332229,-0.713884,8.663828,2.787939,8.269074,-0.572219,-8.245366,-5.857212,8.167378,3.065314,0.286562,9.891009,-5.353180,3.247222,3.112424,4.792303,-2.735236,-1.445647,-0.799400,-8.911126,-9.505995], dtype = "float64")#candidate|6275|(200,)|const|float64
call_6274 = func_2728_call(relay.reshape(const_6275.astype('float64'), [4, 5, 10]))
call_6276 = func_2728_call(relay.reshape(const_6275.astype('float64'), [4, 5, 10]))
output = relay.Tuple([bop_6252,call_6261,call_6268,const_6269,const_6270,call_6274,const_6275,])
output2 = relay.Tuple([bop_6255,call_6262,call_6271,const_6269,const_6270,call_6276,const_6275,])
func_6279 = relay.Function([var_6251,], output)
mod['func_6279'] = func_6279
mod = relay.transform.InferType()(mod)
mutated_mod['func_6279'] = func_6279
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6280 = relay.var("var_6280", dtype = "bool", shape = (16, 5, 7))#candidate|6280|(16, 5, 7)|var|bool
func_6279_call = mutated_mod.get_global_var('func_6279')
call_6281 = func_6279_call(var_6280)
output = call_6281
func_6282 = relay.Function([var_6280], output)
mutated_mod['func_6282'] = func_6282
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4683_call = mod.get_global_var('func_4683')
func_4685_call = mutated_mod.get_global_var('func_4685')
call_6293 = relay.TupleGetItem(func_4683_call(), 2)
call_6294 = relay.TupleGetItem(func_4685_call(), 2)
func_5794_call = mod.get_global_var('func_5794')
func_5796_call = mutated_mod.get_global_var('func_5796')
var_6327 = relay.var("var_6327", dtype = "int16", shape = (672,))#candidate|6327|(672,)|var|int16
call_6326 = relay.TupleGetItem(func_5794_call(relay.reshape(var_6327.astype('int16'), [2, 336])), 0)
call_6328 = relay.TupleGetItem(func_5796_call(relay.reshape(var_6327.astype('int16'), [2, 336])), 0)
func_1627_call = mod.get_global_var('func_1627')
func_1630_call = mutated_mod.get_global_var('func_1630')
var_6339 = relay.var("var_6339", dtype = "uint64", shape = (13, 1))#candidate|6339|(13, 1)|var|uint64
call_6338 = func_1627_call(relay.reshape(var_6339.astype('uint64'), [1, 13]), relay.reshape(var_6339.astype('uint64'), [1, 13]), )
call_6340 = func_1627_call(relay.reshape(var_6339.astype('uint64'), [1, 13]), relay.reshape(var_6339.astype('uint64'), [1, 13]), )
func_5506_call = mod.get_global_var('func_5506')
func_5508_call = mutated_mod.get_global_var('func_5508')
call_6350 = relay.TupleGetItem(func_5506_call(), 1)
call_6351 = relay.TupleGetItem(func_5508_call(), 1)
output = relay.Tuple([call_6293,call_6326,var_6327,call_6338,var_6339,call_6350,])
output2 = relay.Tuple([call_6294,call_6328,var_6327,call_6340,var_6339,call_6351,])
func_6354 = relay.Function([var_6327,var_6339,], output)
mod['func_6354'] = func_6354
mod = relay.transform.InferType()(mod)
mutated_mod['func_6354'] = func_6354
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6354_call = mutated_mod.get_global_var('func_6354')
var_6356 = relay.var("var_6356", dtype = "int16", shape = (672,))#candidate|6356|(672,)|var|int16
var_6357 = relay.var("var_6357", dtype = "uint64", shape = (13, 1))#candidate|6357|(13, 1)|var|uint64
call_6355 = func_6354_call(var_6356,var_6357,)
output = call_6355
func_6358 = relay.Function([var_6356,var_6357,], output)
mutated_mod['func_6358'] = func_6358
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6386 = relay.var("var_6386", dtype = "float32", shape = (8, 11, 7))#candidate|6386|(8, 11, 7)|var|float32
uop_6387 = relay.atan(var_6386.astype('float32')) # shape=(8, 11, 7)
bop_6395 = relay.minimum(uop_6387.astype('uint64'), relay.reshape(var_6386.astype('uint64'), relay.shape_of(uop_6387))) # shape=(8, 11, 7)
func_5268_call = mod.get_global_var('func_5268')
func_5269_call = mutated_mod.get_global_var('func_5269')
call_6406 = func_5268_call()
call_6407 = func_5268_call()
func_5534_call = mod.get_global_var('func_5534')
func_5536_call = mutated_mod.get_global_var('func_5536')
var_6413 = relay.var("var_6413", dtype = "bool", shape = (5, 45))#candidate|6413|(5, 45)|var|bool
call_6412 = relay.TupleGetItem(func_5534_call(relay.reshape(var_6413.astype('bool'), [225,])), 3)
call_6414 = relay.TupleGetItem(func_5536_call(relay.reshape(var_6413.astype('bool'), [225,])), 3)
func_4077_call = mod.get_global_var('func_4077')
func_4078_call = mutated_mod.get_global_var('func_4078')
call_6429 = relay.TupleGetItem(func_4077_call(), 0)
call_6430 = relay.TupleGetItem(func_4078_call(), 0)
output = relay.Tuple([bop_6395,call_6406,call_6412,var_6413,call_6429,])
output2 = relay.Tuple([bop_6395,call_6407,call_6414,var_6413,call_6430,])
func_6436 = relay.Function([var_6386,var_6413,], output)
mod['func_6436'] = func_6436
mod = relay.transform.InferType()(mod)
mutated_mod['func_6436'] = func_6436
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6436_call = mutated_mod.get_global_var('func_6436')
var_6438 = relay.var("var_6438", dtype = "float32", shape = (8, 11, 7))#candidate|6438|(8, 11, 7)|var|float32
var_6439 = relay.var("var_6439", dtype = "bool", shape = (5, 45))#candidate|6439|(5, 45)|var|bool
call_6437 = func_6436_call(var_6438,var_6439,)
output = call_6437
func_6440 = relay.Function([var_6438,var_6439,], output)
mutated_mod['func_6440'] = func_6440
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4521_call = mod.get_global_var('func_4521')
func_4522_call = mutated_mod.get_global_var('func_4522')
call_6447 = relay.TupleGetItem(func_4521_call(), 1)
call_6448 = relay.TupleGetItem(func_4522_call(), 1)
var_6451 = relay.var("var_6451", dtype = "int16", shape = (2, 336))#candidate|6451|(2, 336)|var|int16
bop_6452 = relay.mod(call_6447.astype('float32'), relay.reshape(var_6451.astype('float32'), relay.shape_of(call_6447))) # shape=(2, 336)
bop_6455 = relay.mod(call_6448.astype('float32'), relay.reshape(var_6451.astype('float32'), relay.shape_of(call_6448))) # shape=(2, 336)
func_4077_call = mod.get_global_var('func_4077')
func_4078_call = mutated_mod.get_global_var('func_4078')
call_6458 = relay.TupleGetItem(func_4077_call(), 0)
call_6459 = relay.TupleGetItem(func_4078_call(), 0)
output = relay.Tuple([bop_6452,call_6458,])
output2 = relay.Tuple([bop_6455,call_6459,])
func_6472 = relay.Function([var_6451,], output)
mod['func_6472'] = func_6472
mod = relay.transform.InferType()(mod)
var_6473 = relay.var("var_6473", dtype = "int16", shape = (2, 336))#candidate|6473|(2, 336)|var|int16
output = func_6472(var_6473)
func_6474 = relay.Function([var_6473], output)
mutated_mod['func_6474'] = func_6474
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5057_call = mod.get_global_var('func_5057')
func_5058_call = mutated_mod.get_global_var('func_5058')
call_6495 = relay.TupleGetItem(func_5057_call(), 0)
call_6496 = relay.TupleGetItem(func_5058_call(), 0)
output = relay.Tuple([call_6495,])
output2 = relay.Tuple([call_6496,])
func_6499 = relay.Function([], output)
mod['func_6499'] = func_6499
mod = relay.transform.InferType()(mod)
output = func_6499()
func_6500 = relay.Function([], output)
mutated_mod['func_6500'] = func_6500
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5901_call = mod.get_global_var('func_5901')
func_5903_call = mutated_mod.get_global_var('func_5903')
call_6601 = func_5901_call()
call_6602 = func_5901_call()
output = relay.Tuple([call_6601,])
output2 = relay.Tuple([call_6602,])
func_6610 = relay.Function([], output)
mod['func_6610'] = func_6610
mod = relay.transform.InferType()(mod)
mutated_mod['func_6610'] = func_6610
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6610_call = mutated_mod.get_global_var('func_6610')
call_6611 = func_6610_call()
output = call_6611
func_6612 = relay.Function([], output)
mutated_mod['func_6612'] = func_6612
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5928_call = mod.get_global_var('func_5928')
func_5930_call = mutated_mod.get_global_var('func_5930')
call_6613 = func_5928_call()
call_6614 = func_5928_call()
output = relay.Tuple([call_6613,])
output2 = relay.Tuple([call_6614,])
func_6637 = relay.Function([], output)
mod['func_6637'] = func_6637
mod = relay.transform.InferType()(mod)
output = func_6637()
func_6638 = relay.Function([], output)
mutated_mod['func_6638'] = func_6638
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5268_call = mod.get_global_var('func_5268')
func_5269_call = mutated_mod.get_global_var('func_5269')
call_6648 = func_5268_call()
call_6649 = func_5268_call()
func_3426_call = mod.get_global_var('func_3426')
func_3428_call = mutated_mod.get_global_var('func_3428')
call_6714 = relay.TupleGetItem(func_3426_call(), 2)
call_6715 = relay.TupleGetItem(func_3428_call(), 2)
uop_6719 = relay.asinh(call_6648.astype('float32')) # shape=(16, 5, 7)
uop_6721 = relay.asinh(call_6649.astype('float32')) # shape=(16, 5, 7)
output = relay.Tuple([call_6714,uop_6719,])
output2 = relay.Tuple([call_6715,uop_6721,])
func_6726 = relay.Function([], output)
mod['func_6726'] = func_6726
mod = relay.transform.InferType()(mod)
mutated_mod['func_6726'] = func_6726
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6726_call = mutated_mod.get_global_var('func_6726')
call_6727 = func_6726_call()
output = call_6727
func_6728 = relay.Function([], output)
mutated_mod['func_6728'] = func_6728
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4722_call = mod.get_global_var('func_4722')
func_4723_call = mutated_mod.get_global_var('func_4723')
call_6754 = relay.TupleGetItem(func_4722_call(), 2)
call_6755 = relay.TupleGetItem(func_4723_call(), 2)
var_6758 = relay.var("var_6758", dtype = "int16", shape = (2, 336))#candidate|6758|(2, 336)|var|int16
bop_6759 = relay.greater_equal(call_6754.astype('bool'), relay.reshape(var_6758.astype('bool'), relay.shape_of(call_6754))) # shape=(2, 336)
bop_6762 = relay.greater_equal(call_6755.astype('bool'), relay.reshape(var_6758.astype('bool'), relay.shape_of(call_6755))) # shape=(2, 336)
const_6771 = relay.const([[1,9,-7,-3,4,6,10,6,-10,-7,-9,-3,-3,3,1,5,5,-9,5,-3,2,6,-9,-4,-9,7,3,10,-2,-9,6,4,-10,-6,-9,-5,10,-2,8,-7,6,4,5,5,-9,-2,-10,8,1,8,3,-10,-7,-4,-8,-9,-5,6,-8,-1,7,4,2,-9,8,-5,-1,5,-9,10,-2,-4,5,-8,10,2,3,-7,1,-7,3,9,-7,3,-5,-5,-3,3,8,-3,-1,8,-2,-6,-10,10,-7,9,-5,-1,-5,-9,-5,8,-6,-4,5,-8,4,8,10,-9,-8,10,1,6,-8,-6,-1,-6,3,-3,-9,-5,-6,-9,10,-3,6,-2,5,-5,-6,3,5,-4,9,-9,10,-5,7,-5,2,5,-1,7,6,-6,10,10,1,4,-3,10,6,-10,-7,-10,-10,9,2,5,5,-2,5,2,8,-5,8,-4,9,9,-6,-9,2,10,-1,3,8,-2,-1,-8,10,-10,7,7,8,5,3,-2,1,10,-7,-9,2,8,6,2,9,6,-6,3,-9,7,4,6,1,7,-2,-3,-8,6,8,1,2,3,-2,-3,7,-2,1,-6,5,10,-8,2,3,1,7,-9,3,6,-8,-6,-1,8,8,2,-5,-3,-5,-10,-4,-10,-5,10,10,-3,7,5,-10,7,5,1,2,-3,-6,5,-4,-3,-5,6,10,-4,-1,-6,10,-6,5,-4,-9,5,-10,9,9,-4,4,-10,1,3,2,2,-5,6,-6,-8,-7,-4,5,-10,5,9,-6,-6,-2,1,-10,-8,1,-6,4,6,7,6,-3,-8,-2,8,5,-5,4,-3,-8,9,2,-8,9,8,4,-10,4,-7,-5,4,-10,-7,4,-9,10,4,5,-10,6,2,6,8],[2,-6,-2,-6,-7,7,4,6,5,-8,9,-5,-8,6,-1,-3,10,9,-8,-2,-2,10,6,2,5,-2,-7,-1,3,10,10,6,-3,-1,4,7,4,-1,-3,-2,2,5,10,-6,-3,-1,-8,-2,4,3,9,-1,9,-3,-7,-3,10,8,-1,-7,1,-7,2,1,7,3,5,-8,10,-7,8,-5,7,8,-8,-2,10,-9,3,2,5,5,-1,-2,-4,-5,-10,-1,-4,3,-6,2,-8,-2,-2,-10,-10,-4,-8,2,-7,6,-9,-2,-8,6,4,1,10,3,-8,8,-10,8,1,1,7,7,6,9,-6,9,-3,-10,-4,7,-7,-7,-9,2,5,2,-1,-7,6,-3,1,2,2,8,-6,7,4,-8,-1,5,-6,-7,3,5,8,-4,10,2,8,10,-9,-7,1,5,8,7,6,2,-5,-1,-7,-3,-10,10,7,4,-7,8,-8,9,3,-1,-9,10,-4,-1,5,9,-9,7,-9,3,-4,3,5,10,-1,9,-8,5,10,-2,-8,-4,1,4,-2,7,9,10,3,2,-2,3,-9,-9,-4,8,3,-10,1,6,2,-9,-5,-3,-8,-4,5,10,8,5,-2,6,4,2,2,1,5,-3,9,-9,-10,-9,2,10,-9,-4,9,8,7,-1,10,-5,1,5,5,-1,9,-1,-7,1,-10,-5,-4,-4,-3,-4,-8,9,-6,-3,8,-7,2,-8,-10,5,3,-1,-4,-1,-2,1,-3,-1,-5,-9,6,2,3,7,8,-5,1,-7,3,-2,-3,6,5,5,2,5,-10,-8,-6,8,8,-2,-9,5,-8,-8,-2,-5,2,9,3,-5,-2,6,9,-1,-7,-7,-3,-8,-1,-10,-1,-2,-6,-10,-6,2,8,-5,3,-6]], dtype = "int16")#candidate|6771|(2, 336)|const|int16
bop_6772 = relay.multiply(call_6754.astype('int64'), relay.reshape(const_6771.astype('int64'), relay.shape_of(call_6754))) # shape=(2, 336)
bop_6775 = relay.multiply(call_6755.astype('int64'), relay.reshape(const_6771.astype('int64'), relay.shape_of(call_6755))) # shape=(2, 336)
func_3450_call = mod.get_global_var('func_3450')
func_3453_call = mutated_mod.get_global_var('func_3453')
const_6778 = relay.const([-7,-6,3,-4,1,-4,-5,7,-4,8,-8,-10,8,-5,-2,3,-7,-2,5,9,3,6,-2,-6,8,8,-9,-2,10,7,4,-1,1,3,-1,-3,-4,2,1,-4,-2,-6,-3,-9,8,6,6,-4,3,2,-8,6,-3,1,6,7,-10,-10,-3,-7,-5,-4,-2,-7,-6,9,-5,7,5,5,3,-1,5,3,10,-1,-3,-3,5,-10,-2,-4,-5,-6,7,2,-3,3,4,-8,-6,-7,-5,-7,-4,-1,7,-3,6,-3,-1,5,7,4,3,-8,-10,-9,-7,5,-3,-8,-10,3,10,-1,10,-7,-1,10,2,3,3,6,10,3,-8,6,-4,5,2,7,1,10,-4,8,-6,-7,-4,-1,4,10,9,-9,-4,6,-10,9,-4,3,-7,3,3,6,-1,-4,3,7,1,-4,10,-10,-1,-4,-9,-3,10,-2,6,-10,7,3,7,1,-6,2,2,-8,4,10,-1,-10,10,1,9,2,5,-5,7,-10,-2,-1,-6,-9,-3,4,1,2,-5,7,6,2,-7,4,5,-7,8,-1,-8,-7,-9,-4,2,-4,-1,-2,2,-8,9,5,8,10,9,-4,-6,-8,1,-7,-8,-1,4,5,5,7,3,-9,1,9,-5,-8,4,-5,-8,10,-5,-4,-4,7,10,5,-3,6,-8,-7,-8,5,1,-6,4,2,7,-2,-4,-2,10,-10,4,8,-3,-4,-10,-4,8,-7,-8,-6,6,7,5,-4,5,-10,4,-10,3,-9,-2,1,4,6,8,6,10,-1,1,9,-1,-6,7,3,9,-4,-6,-4,-4,2,-2,3,2,-6,1,-2,6,-9,-1,4,4,-2,2,1,-6,-7,3,-10,-4,-9,-2,9,-8,-1,-3,-10,5,-7,10,3,3,6,-10,1,5,-10,1,-4,-2,-10,2,-1,-6,3,8,-3,6,5,8,-1,-7,9,-4,9,-8,10,10,6,-2,1,-5,-1,8,8,-3,10,-1,10,-1,-3,7,-10,7,-3,5,10,-2,10,8,-5,-8,-3,-3,-6,1,5,3,6,-3,2,7,-7,-5,-7,6,6,-7,3,-3,4,6,-3,-5,2,10,-6,-6,-5,2,3,-6,-2,-9,4,-3,5,8,-10,-7,-2,8,3,3,-2,2,2], dtype = "int16")#candidate|6778|(432,)|const|int16
call_6777 = relay.TupleGetItem(func_3450_call(relay.reshape(const_6778.astype('int16'), [3, 9, 16]), relay.reshape(const_6778.astype('int16'), [3, 9, 16]), ), 1)
call_6779 = relay.TupleGetItem(func_3453_call(relay.reshape(const_6778.astype('int16'), [3, 9, 16]), relay.reshape(const_6778.astype('int16'), [3, 9, 16]), ), 1)
output = relay.Tuple([bop_6759,bop_6772,call_6777,const_6778,])
output2 = relay.Tuple([bop_6762,bop_6775,call_6779,const_6778,])
func_6790 = relay.Function([var_6758,], output)
mod['func_6790'] = func_6790
mod = relay.transform.InferType()(mod)
var_6791 = relay.var("var_6791", dtype = "int16", shape = (2, 336))#candidate|6791|(2, 336)|var|int16
output = func_6790(var_6791)
func_6792 = relay.Function([var_6791], output)
mutated_mod['func_6792'] = func_6792
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6794 = relay.var("var_6794", dtype = "float32", shape = ())#candidate|6794|()|var|float32
var_6795 = relay.var("var_6795", dtype = "float32", shape = (5, 7, 10))#candidate|6795|(5, 7, 10)|var|float32
bop_6796 = relay.floor_mod(var_6794.astype('float32'), var_6795.astype('float32')) # shape=(5, 7, 10)
output = relay.Tuple([bop_6796,])
output2 = relay.Tuple([bop_6796,])
func_6799 = relay.Function([var_6794,var_6795,], output)
mod['func_6799'] = func_6799
mod = relay.transform.InferType()(mod)
var_6800 = relay.var("var_6800", dtype = "float32", shape = ())#candidate|6800|()|var|float32
var_6801 = relay.var("var_6801", dtype = "float32", shape = (5, 7, 10))#candidate|6801|(5, 7, 10)|var|float32
output = func_6799(var_6800,var_6801,)
func_6802 = relay.Function([var_6800,var_6801,], output)
mutated_mod['func_6802'] = func_6802
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3712_call = mod.get_global_var('func_3712')
func_3713_call = mutated_mod.get_global_var('func_3713')
call_7046 = func_3712_call()
call_7047 = func_3712_call()
func_4780_call = mod.get_global_var('func_4780')
func_4782_call = mutated_mod.get_global_var('func_4782')
call_7088 = relay.TupleGetItem(func_4780_call(), 0)
call_7089 = relay.TupleGetItem(func_4782_call(), 0)
output = relay.Tuple([call_7046,call_7088,])
output2 = relay.Tuple([call_7047,call_7089,])
func_7090 = relay.Function([], output)
mod['func_7090'] = func_7090
mod = relay.transform.InferType()(mod)
output = func_7090()
func_7091 = relay.Function([], output)
mutated_mod['func_7091'] = func_7091
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4722_call = mod.get_global_var('func_4722')
func_4723_call = mutated_mod.get_global_var('func_4723')
call_7100 = relay.TupleGetItem(func_4722_call(), 2)
call_7101 = relay.TupleGetItem(func_4723_call(), 2)
output = relay.Tuple([call_7100,])
output2 = relay.Tuple([call_7101,])
func_7128 = relay.Function([], output)
mod['func_7128'] = func_7128
mod = relay.transform.InferType()(mod)
mutated_mod['func_7128'] = func_7128
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7128_call = mutated_mod.get_global_var('func_7128')
call_7129 = func_7128_call()
output = call_7129
func_7130 = relay.Function([], output)
mutated_mod['func_7130'] = func_7130
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7194 = relay.var("var_7194", dtype = "float32", shape = (3, 7, 10))#candidate|7194|(3, 7, 10)|var|float32
uop_7195 = relay.erf(var_7194.astype('float32')) # shape=(3, 7, 10)
bop_7197 = relay.less(uop_7195.astype('bool'), relay.reshape(var_7194.astype('bool'), relay.shape_of(uop_7195))) # shape=(3, 7, 10)
func_5057_call = mod.get_global_var('func_5057')
func_5058_call = mutated_mod.get_global_var('func_5058')
call_7205 = relay.TupleGetItem(func_5057_call(), 0)
call_7206 = relay.TupleGetItem(func_5058_call(), 0)
func_4225_call = mod.get_global_var('func_4225')
func_4227_call = mutated_mod.get_global_var('func_4227')
call_7228 = relay.TupleGetItem(func_4225_call(), 0)
call_7229 = relay.TupleGetItem(func_4227_call(), 0)
output = relay.Tuple([bop_7197,call_7205,call_7228,])
output2 = relay.Tuple([bop_7197,call_7206,call_7229,])
func_7233 = relay.Function([var_7194,], output)
mod['func_7233'] = func_7233
mod = relay.transform.InferType()(mod)
mutated_mod['func_7233'] = func_7233
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7234 = relay.var("var_7234", dtype = "float32", shape = (3, 7, 10))#candidate|7234|(3, 7, 10)|var|float32
func_7233_call = mutated_mod.get_global_var('func_7233')
call_7235 = func_7233_call(var_7234)
output = call_7235
func_7236 = relay.Function([var_7234], output)
mutated_mod['func_7236'] = func_7236
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5268_call = mod.get_global_var('func_5268')
func_5269_call = mutated_mod.get_global_var('func_5269')
call_7241 = func_5268_call()
call_7242 = func_5268_call()
func_2920_call = mod.get_global_var('func_2920')
func_2922_call = mutated_mod.get_global_var('func_2922')
var_7253 = relay.var("var_7253", dtype = "float32", shape = (1008,))#candidate|7253|(1008,)|var|float32
call_7252 = func_2920_call(relay.reshape(var_7253.astype('float32'), [6, 14, 12]))
call_7254 = func_2920_call(relay.reshape(var_7253.astype('float32'), [6, 14, 12]))
func_5338_call = mod.get_global_var('func_5338')
func_5339_call = mutated_mod.get_global_var('func_5339')
call_7270 = relay.TupleGetItem(func_5338_call(), 0)
call_7271 = relay.TupleGetItem(func_5339_call(), 0)
output = relay.Tuple([call_7241,call_7252,var_7253,call_7270,])
output2 = relay.Tuple([call_7242,call_7254,var_7253,call_7271,])
func_7275 = relay.Function([var_7253,], output)
mod['func_7275'] = func_7275
mod = relay.transform.InferType()(mod)
var_7276 = relay.var("var_7276", dtype = "float32", shape = (1008,))#candidate|7276|(1008,)|var|float32
output = func_7275(var_7276)
func_7277 = relay.Function([var_7276], output)
mutated_mod['func_7277'] = func_7277
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7291 = relay.var("var_7291", dtype = "uint8", shape = (8, 15, 6))#candidate|7291|(8, 15, 6)|var|uint8
const_7292 = relay.const([[[3,-7,5,5,-6,-1],[-10,2,-7,-5,8,-10],[1,1,10,-1,-3,-4],[-10,2,-6,10,-7,-5],[9,-5,-10,-3,6,-10],[-9,-1,-3,-3,-6,9],[-7,-7,3,3,2,10],[-5,-4,9,9,-8,10],[-7,-4,-7,-4,-4,-1],[3,-9,-1,6,4,-9],[7,-10,-10,6,-3,-10],[-5,-5,5,6,-1,10],[7,-10,-7,5,8,-9],[-6,-6,5,-9,2,9],[-3,5,3,-8,3,-1]],[[-10,6,-4,4,10,-8],[8,7,-5,-7,-3,-4],[8,-7,1,-5,6,9],[-6,9,5,-3,7,4],[6,2,-4,8,-8,6],[4,-10,-3,-10,4,-7],[7,1,-1,7,6,9],[-4,3,1,-3,1,5],[4,2,-5,4,-10,5],[2,9,3,-8,-4,-9],[2,-1,-5,4,-2,-7],[7,8,-8,9,6,8],[5,-6,-8,-5,9,3],[4,5,-6,-2,6,2],[-4,-4,10,-2,1,-7]],[[7,9,-10,1,-2,10],[1,-2,-4,10,7,8],[9,4,10,-9,3,-2],[-2,7,-1,3,10,8],[-10,-2,4,6,-2,1],[4,-8,8,2,-2,6],[-7,-5,2,1,-2,3],[-4,9,-1,-7,-2,2],[4,-2,2,-10,-6,-7],[8,2,-2,-8,-4,-4],[9,10,8,-3,-7,-9],[-4,-9,3,9,-6,1],[-8,8,-8,-8,6,10],[3,10,-10,-8,-9,-5],[3,-2,-6,8,-4,7]],[[9,-10,-7,-2,-6,8],[-3,-10,-3,3,-8,-6],[-1,-10,3,8,-5,8],[9,-2,-2,2,-9,6],[-9,2,5,2,4,-1],[-1,8,7,10,6,4],[-4,-3,-9,7,-9,5],[-8,-2,-3,9,3,-10],[3,-8,-3,7,9,2],[-9,7,-9,4,1,2],[-10,-8,10,5,7,2],[-6,-9,9,4,-2,9],[-3,-1,-10,10,3,5],[5,7,-3,-4,-10,-7],[-4,-8,-2,-8,-2,1]],[[1,2,-9,-7,6,8],[5,-2,3,-3,-8,3],[-9,-7,9,3,-1,-6],[-5,-9,-9,2,-7,8],[-2,8,1,4,-2,1],[10,3,-2,-6,-4,-7],[9,8,4,9,4,-7],[-9,-4,-3,4,10,7],[-8,6,7,6,1,-4],[-9,-2,-2,-7,2,-2],[6,-8,-5,8,-9,7],[8,-2,9,-5,-10,-1],[-5,-5,-10,2,5,2],[-7,5,-5,-2,8,-3],[3,-3,-2,-7,-3,-2]],[[9,8,-5,4,-3,10],[1,-2,-7,6,-10,2],[3,8,2,-6,-5,-5],[-7,4,7,-9,-7,9],[-5,-3,4,-6,7,-3],[-6,-7,5,3,10,1],[3,-10,-2,-4,4,1],[-5,6,-3,-8,-8,-9],[-9,-5,10,-6,8,1],[7,-7,5,10,7,1],[-5,-6,-7,5,7,-5],[-8,10,-9,7,8,-6],[4,-4,-3,8,7,-10],[10,10,-5,-6,6,-2],[9,-8,5,-4,1,9]],[[-3,10,2,-4,-5,-2],[7,-7,4,-7,-9,3],[-8,-3,3,5,-9,-7],[4,3,-8,-2,-3,-10],[-8,-1,2,1,1,1],[7,1,10,9,3,-5],[-7,6,6,8,-2,1],[2,-4,-9,6,-10,4],[-7,3,-6,-1,-7,-4],[4,9,2,-8,5,9],[8,9,-4,-7,7,3],[10,8,-2,2,-6,-1],[-2,-3,2,10,7,5],[4,4,-4,9,-2,1],[1,9,-6,-6,-1,5]],[[10,3,-5,-1,-2,4],[-4,10,-2,-2,-6,-2],[3,-1,8,-10,-1,8],[-5,7,-5,-3,-6,9],[-6,8,-3,-4,-10,-5],[-9,7,-7,-6,-5,10],[-5,-1,8,6,-2,-7],[7,-3,4,-5,2,3],[-6,-2,5,1,8,1],[-3,-1,-5,9,-8,1],[10,-7,6,2,2,-3],[7,-6,-5,3,6,-10],[-2,5,1,4,-9,-2],[2,7,7,10,3,10],[-3,-3,-7,-1,3,-9]]], dtype = "uint8")#candidate|7292|(8, 15, 6)|const|uint8
bop_7293 = relay.maximum(var_7291.astype('uint8'), relay.reshape(const_7292.astype('uint8'), relay.shape_of(var_7291))) # shape=(8, 15, 6)
uop_7304 = relay.log(const_7292.astype('float32')) # shape=(8, 15, 6)
output = relay.Tuple([bop_7293,uop_7304,])
output2 = relay.Tuple([bop_7293,uop_7304,])
func_7315 = relay.Function([var_7291,], output)
mod['func_7315'] = func_7315
mod = relay.transform.InferType()(mod)
mutated_mod['func_7315'] = func_7315
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7316 = relay.var("var_7316", dtype = "uint8", shape = (8, 15, 6))#candidate|7316|(8, 15, 6)|var|uint8
func_7315_call = mutated_mod.get_global_var('func_7315')
call_7317 = func_7315_call(var_7316)
output = call_7317
func_7318 = relay.Function([var_7316], output)
mutated_mod['func_7318'] = func_7318
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7320 = relay.const([[[9.523068,5.073187,3.321844,-3.133956,0.287718,-5.643528,9.243818,-2.466858],[9.506178,9.957017,5.426628,7.410712,-8.469881,-3.837805,3.002252,-8.240322],[8.092581,-7.734827,-2.745671,5.776484,4.332925,7.659584,-4.413619,2.627909],[-1.096922,7.895558,-8.346739,5.500923,-6.760192,1.372454,6.738050,4.711616],[-6.137657,-5.559274,-1.535268,-4.218237,3.303866,7.588614,9.506276,7.801317],[7.574385,7.111376,6.534330,-2.128554,7.655703,3.020503,0.201283,0.693289],[5.927986,-1.640811,1.038251,9.497684,2.215079,8.017218,7.872673,-0.045448],[2.756450,-7.384458,2.366211,4.594945,3.172193,8.495230,9.473584,-3.023179],[-6.895549,-7.899891,6.661351,-6.295983,-7.429737,9.004484,-7.428141,-8.887532],[9.276831,-1.017672,-4.920396,2.482135,3.740425,-4.646255,-3.911433,2.745131],[-5.721753,-1.320892,0.132660,-2.637134,-6.618542,0.322989,7.160344,2.345560],[-7.326767,1.427021,6.396125,-5.054516,-1.772375,4.056844,3.116480,7.738373],[-6.671724,8.216239,3.491273,-5.063360,5.928585,-9.661796,6.368458,-6.677962],[-4.738219,-8.167044,-3.337547,-3.697165,-9.732328,3.718773,-6.213531,4.094836]],[[2.489345,-4.996360,-4.765042,-9.307025,-6.248697,-7.128445,-6.812184,8.653242],[1.458432,-5.672666,1.753627,-5.965495,-6.639787,1.101593,-6.547523,-8.966057],[-9.328283,-1.359524,2.529890,-3.675351,-4.565110,2.899522,8.115362,4.086337],[2.271380,4.125345,-0.887491,-2.388597,7.538366,3.856391,-1.446027,8.316031],[-0.368442,2.762109,4.216483,7.396364,-7.862721,-5.143167,2.839925,-5.257337],[-7.814339,6.426999,1.419091,2.968179,-5.962481,0.788903,-0.243501,1.690307],[-1.841865,-0.956942,-4.645084,1.343348,1.237116,6.091476,0.403676,6.156417],[5.875385,-9.366462,-2.166258,5.033441,-0.792691,7.990200,-3.159477,3.389760],[8.993994,-7.573137,9.548895,-5.373832,4.417439,-8.000837,-5.955969,-1.680469],[-4.332766,-9.693598,9.191287,4.105814,-5.959546,-8.050875,5.729850,-8.740441],[-6.739082,5.470173,-3.821855,-6.361593,9.291441,0.831022,-0.739264,5.943192],[-4.844580,7.849228,7.638615,-9.021576,7.971964,-0.015186,-8.884180,3.254488],[0.539399,3.071195,-5.866138,-5.389986,-1.417127,0.385466,7.407749,0.234012],[9.044444,9.404524,-8.491458,-8.919808,1.082570,-2.005002,4.447196,-8.693657]],[[-3.100526,2.161945,2.173798,-4.391939,9.149282,-6.525296,-2.207018,-4.661244],[-3.094942,2.575486,4.668168,-2.100660,-6.271579,4.428779,-1.732934,8.171424],[6.108014,1.154746,-3.210460,-0.118670,-8.532007,-3.130168,-9.988202,-7.832538],[3.407212,2.605143,2.081693,7.240168,3.128795,-1.614633,-9.784772,-4.271306],[-4.807402,-8.916320,-0.161461,-0.940223,3.103305,0.570393,2.168287,-0.961983],[6.735857,-1.853773,9.597277,3.660753,-2.627890,-9.472233,3.972218,-8.191721],[-0.607235,-9.972164,8.735971,2.809444,2.310173,-3.024154,-4.274299,2.103247],[9.350131,4.313235,1.167728,8.477191,-2.969524,-2.581835,-4.567822,9.342627],[0.376726,2.248373,-8.432568,2.973083,-0.528104,-5.744252,-3.993015,-8.828235],[5.420414,-9.814037,-2.574625,-8.311394,2.117944,-3.439257,5.296925,8.773258],[1.306010,8.475210,2.059179,-4.013570,2.154528,4.035962,-2.757431,2.639570],[7.587473,7.295891,8.476743,-7.519274,-5.891961,-9.819483,-9.884721,3.469999],[3.923899,6.467777,2.395091,-7.854013,-7.442383,9.895208,6.778492,8.470349],[-2.865750,4.027352,-9.307799,5.742244,-8.480922,1.275416,3.019399,7.549084]],[[8.317452,5.708321,-6.392739,1.876974,2.058720,8.456480,3.583657,4.838713],[3.483871,6.178150,-2.674380,3.239564,8.394165,9.299690,6.384012,0.049219],[7.460887,9.308081,-9.845086,9.929785,5.834431,-4.762089,1.303339,7.771189],[-2.952682,-9.605627,9.073271,-9.012264,-1.474973,7.759978,-9.647416,9.590124],[3.521475,1.962167,1.224652,-1.622314,9.720540,-3.398199,-5.255348,-7.961510],[-7.857206,-5.628209,-8.439457,-6.820152,-9.758074,-2.946136,-0.626246,7.165173],[-7.335751,5.882451,5.895181,9.944464,2.805501,3.344907,8.780673,-3.178523],[-9.091169,6.464954,2.815947,-5.481524,8.857373,-4.921167,-8.260153,6.445974],[-7.104672,-4.810143,-0.512920,0.417068,0.703295,-4.893447,-9.892772,7.804217],[9.788396,6.442416,-6.688618,-2.213549,-5.599700,-1.992356,-9.575107,0.679054],[-4.470755,-4.105583,2.888177,-3.213434,-9.146387,0.300371,-9.849126,-9.666420],[8.560473,-7.181752,2.629698,6.228922,-7.184122,-7.456285,-4.507120,5.686833],[5.749905,9.131050,9.265438,-0.250485,-1.582788,-5.793054,-1.018218,-5.210837],[-4.534316,5.608929,-2.672405,5.511265,-8.781881,0.598931,-6.820274,-0.843459]],[[0.954157,-4.235221,2.965224,-3.371220,4.032063,-7.342790,3.709613,1.294509],[-5.864225,8.471272,-0.021449,1.930832,-7.419480,4.183159,3.702175,1.119546],[6.890103,-3.249178,-6.301275,2.653420,7.421665,7.955124,-9.305040,4.356683],[7.353730,4.971784,8.877992,3.230789,-5.076875,-8.368361,-9.879246,-4.593339],[-9.672330,-4.082104,4.323445,-8.808475,-7.673565,-9.188947,-8.493248,5.344850],[-7.651966,4.877899,5.310521,-0.388962,4.911879,9.034268,-0.424515,-5.634902],[-9.916269,2.117361,-4.936244,8.313186,2.881664,7.038775,0.700218,1.651701],[-6.899314,4.086618,8.095646,8.236994,5.049701,-7.812641,-1.211221,-1.779882],[-5.911870,-9.081095,1.466754,4.213866,9.649491,-8.661879,6.287045,4.124202],[0.306848,9.790399,-4.831900,3.718922,0.036493,7.781963,-1.812776,7.750198],[7.627758,6.234506,0.263796,7.232141,-6.117809,3.554030,4.048787,8.613852],[3.310220,-0.156238,1.081867,8.739195,7.254452,-7.581228,-3.662427,-5.939783],[1.001813,-2.979632,-1.497268,-8.626895,-7.430953,-3.601134,-1.456298,-9.035821],[-7.162410,0.298090,-4.429718,5.248508,6.615816,-9.949202,9.542412,8.403975]],[[-1.676134,1.466950,6.549228,7.847400,5.105931,0.114219,1.111073,8.022992],[-0.154336,9.457442,-5.178229,1.773663,-9.119749,0.323934,-8.593728,6.904475],[6.928070,-0.902228,-4.704359,-1.150515,8.163040,5.964573,4.839043,1.375023],[5.106335,-7.920366,0.460580,7.227128,4.421900,1.315019,9.424586,5.744490],[8.434914,6.668707,0.117015,0.377551,0.153257,-0.301949,5.822507,5.806321],[-0.892920,-5.338160,2.230371,-7.943974,0.749805,-6.026167,-7.627294,8.088816],[5.322605,5.507599,-2.008634,-0.441947,9.715701,-1.337793,-9.015427,8.108516],[4.145593,-9.272232,1.299752,-0.358056,-7.045851,3.483261,-6.273900,-7.996084],[6.936079,-6.715946,-6.760825,8.264735,4.302533,-3.934138,2.761494,4.332706],[-4.664647,2.980431,-0.028928,-1.391217,2.249716,4.096735,-9.161642,7.167012],[7.922960,4.648260,-6.525136,0.791365,-3.084390,6.511177,5.366495,-2.773204],[-6.754959,7.035352,7.520100,8.528226,1.897189,-2.005153,-7.997704,8.474562],[-4.070457,0.261850,4.030333,-6.052823,5.963908,-8.524561,-2.853965,-6.756401],[-1.319572,9.055985,7.343847,-9.949852,8.385898,-1.683500,9.555609,1.079146]],[[-6.308343,-9.947780,4.117293,9.833381,5.126587,6.152051,-5.412178,-4.987969],[0.363330,6.233058,7.442810,9.515608,-8.992222,-4.919931,8.368884,0.333716],[4.094099,-7.962839,3.437860,6.323793,0.639280,-5.310602,-6.886818,-2.755187],[2.037780,-5.411359,-4.539263,6.758432,7.705495,-6.738664,-7.687568,-0.869003],[0.175944,-4.933457,-8.959701,6.344215,6.793566,4.383318,8.032020,8.101955],[8.477327,9.252155,-2.722670,1.897886,-5.762950,-1.643861,3.879408,-9.239002],[4.544196,2.172204,-2.832594,0.630961,9.313092,1.454914,1.308339,5.249572],[-6.646328,-4.660823,0.598426,-0.834788,4.665056,-8.864941,8.119394,0.840587],[-9.051736,-8.045243,-7.295210,-1.175726,1.660661,-2.432095,-8.529954,6.438000],[-1.822320,8.914285,2.835650,5.153136,7.799068,-8.445970,1.168244,2.550065],[-5.892217,-3.649107,-3.917255,-8.125544,0.886975,-7.122166,-0.145739,-1.512927],[7.193455,6.167936,-7.413109,8.278874,-3.968607,-0.132790,4.196768,4.609075],[-0.867881,-5.339133,-1.907058,-1.530947,2.711926,-1.317276,-5.353641,-2.858460],[-1.396063,9.817174,7.019697,-2.578718,-7.703617,3.192682,4.205613,8.433275]],[[-2.974563,-1.048560,2.646709,-5.484928,3.973941,-5.177962,-3.370784,8.946524],[-9.577815,1.920474,2.956202,-8.932823,-9.806276,9.164912,-5.675843,5.882966],[8.626242,-6.244561,-1.215228,3.465027,2.228138,-1.803944,4.595943,-0.795273],[-6.741341,2.009409,-5.866033,6.993250,3.262958,-1.498034,6.097126,-9.519769],[0.069195,0.059662,-4.455750,2.275600,0.622243,5.860148,2.910431,-8.740987],[0.661938,2.520804,0.519932,-1.081946,9.890076,9.433399,8.816317,6.189383],[-0.401334,-8.991460,-1.819114,-0.307492,7.383617,-6.828836,3.983550,-5.286224],[-3.476290,-5.676755,-9.071552,-6.812897,6.852742,5.594357,8.621680,5.497549],[5.409191,-9.869814,4.039178,0.781225,-7.833348,8.416618,2.554941,-9.118608],[0.581130,3.132283,-2.219502,-9.824195,1.615268,-3.317173,-6.511838,-1.983109],[8.053247,7.479850,2.626474,-3.527973,-4.736447,-9.874780,1.352760,6.845437],[1.084235,1.366319,-2.501867,-5.820712,3.381448,3.883571,-5.942877,8.914738],[-7.000667,4.170540,-9.766713,-9.518103,2.342989,-3.986948,9.242335,-0.181250],[-0.627643,-2.212602,8.452112,4.770328,6.284206,-7.568594,-9.789183,-1.907124]],[[8.952377,5.251465,4.375800,-0.315109,-2.589116,7.695833,3.506758,-2.856595],[4.041880,-6.603761,2.849417,0.335999,-3.369746,5.103432,-0.095496,-9.881274],[2.414969,6.929397,9.040149,8.062730,-0.275936,3.191207,-3.720937,1.295889],[3.233921,-5.871811,5.321418,1.754705,-3.916283,3.844624,-1.557848,-0.215451],[7.874560,-4.961916,5.673161,-0.688177,8.957223,3.927884,9.804428,6.008113],[4.509451,-2.598338,-1.570541,-6.895894,-2.374830,7.370205,3.800519,-5.053032],[4.346396,9.824233,-3.363847,-2.133068,-9.935684,-2.242316,-7.392300,-8.569986],[7.406009,2.008079,-0.256431,-8.301579,4.163863,-4.580312,7.423817,1.542259],[1.336555,-9.555539,-6.367322,8.385560,-5.020164,-5.099003,-3.057050,-8.419674],[1.854645,8.392490,-7.432655,-7.969946,9.572342,-0.192797,4.456830,9.770014],[4.800381,5.684591,-9.560469,-0.662613,-0.662586,9.648874,3.040199,-4.130054],[6.118857,-6.369146,-6.824301,0.382326,7.111408,-6.268048,5.124614,-1.209094],[0.886916,-9.426057,-1.315604,4.364547,-8.424187,4.152590,-6.295263,-6.570849],[4.924956,0.594023,-9.423722,8.125612,1.286233,-3.715193,9.737511,4.514552]],[[-3.786691,-2.843407,-9.029030,8.684350,7.839732,-7.216625,6.041617,1.713617],[4.777708,-3.879273,-1.588661,-4.507450,2.909027,-3.515824,8.485802,-6.416640],[-1.283251,-8.015737,-1.319368,3.718081,0.192010,5.477836,-5.022555,9.019108],[-9.908391,0.688602,-1.229041,-0.447096,9.092596,-6.293096,-3.443759,-8.868316],[-3.510094,5.189622,2.909645,-1.062000,-3.323829,3.313042,-1.900456,-1.454607],[-4.314714,4.777240,9.660854,-8.815119,7.163206,4.803387,7.149637,-9.888378],[9.010443,-7.575051,-6.689966,8.625522,2.535429,7.398028,5.104373,-7.282279],[-2.625592,-9.946505,7.813973,-4.446584,-6.869018,-0.345547,5.226769,1.775298],[-3.801754,9.605331,-3.727829,0.325065,6.134844,5.098684,-2.736674,-0.097904],[-3.159083,1.242945,-1.387325,-8.385009,4.989447,-7.032099,1.943426,0.298772],[-5.356183,-5.509849,4.089627,-0.575827,-7.876561,-8.669268,5.592298,9.425000],[0.164243,1.154218,-7.065997,-6.184284,-3.611083,8.581432,-4.294663,3.130736],[1.788039,5.811032,5.548386,-5.429264,-2.111836,-1.842964,5.223290,9.993351],[-5.789374,-3.799441,-4.101024,4.487836,-1.300392,-3.643404,2.086964,4.770973]]], dtype = "float32")#candidate|7320|(10, 14, 8)|const|float32
uop_7321 = relay.sigmoid(const_7320.astype('float32')) # shape=(10, 14, 8)
output = relay.Tuple([uop_7321,])
output2 = relay.Tuple([uop_7321,])
func_7326 = relay.Function([], output)
mod['func_7326'] = func_7326
mod = relay.transform.InferType()(mod)
output = func_7326()
func_7327 = relay.Function([], output)
mutated_mod['func_7327'] = func_7327
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5449_call = mod.get_global_var('func_5449')
func_5451_call = mutated_mod.get_global_var('func_5451')
call_7362 = relay.TupleGetItem(func_5449_call(), 0)
call_7363 = relay.TupleGetItem(func_5451_call(), 0)
func_5534_call = mod.get_global_var('func_5534')
func_5536_call = mutated_mod.get_global_var('func_5536')
var_7385 = relay.var("var_7385", dtype = "bool", shape = (25, 9))#candidate|7385|(25, 9)|var|bool
call_7384 = relay.TupleGetItem(func_5534_call(relay.reshape(var_7385.astype('bool'), [225,])), 0)
call_7386 = relay.TupleGetItem(func_5536_call(relay.reshape(var_7385.astype('bool'), [225,])), 0)
uop_7393 = relay.log10(var_7385.astype('float64')) # shape=(25, 9)
bop_7407 = relay.logical_and(uop_7393.astype('bool'), relay.reshape(var_7385.astype('bool'), relay.shape_of(uop_7393))) # shape=(25, 9)
output = relay.Tuple([call_7362,call_7384,bop_7407,])
output2 = relay.Tuple([call_7363,call_7386,bop_7407,])
func_7412 = relay.Function([var_7385,], output)
mod['func_7412'] = func_7412
mod = relay.transform.InferType()(mod)
var_7413 = relay.var("var_7413", dtype = "bool", shape = (25, 9))#candidate|7413|(25, 9)|var|bool
output = func_7412(var_7413)
func_7414 = relay.Function([var_7413], output)
mutated_mod['func_7414'] = func_7414
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5268_call = mod.get_global_var('func_5268')
func_5269_call = mutated_mod.get_global_var('func_5269')
call_7491 = func_5268_call()
call_7492 = func_5268_call()
func_5506_call = mod.get_global_var('func_5506')
func_5508_call = mutated_mod.get_global_var('func_5508')
call_7494 = relay.TupleGetItem(func_5506_call(), 0)
call_7495 = relay.TupleGetItem(func_5508_call(), 0)
output = relay.Tuple([call_7491,call_7494,])
output2 = relay.Tuple([call_7492,call_7495,])
func_7498 = relay.Function([], output)
mod['func_7498'] = func_7498
mod = relay.transform.InferType()(mod)
output = func_7498()
func_7499 = relay.Function([], output)
mutated_mod['func_7499'] = func_7499
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3479_call = mod.get_global_var('func_3479')
func_3480_call = mutated_mod.get_global_var('func_3480')
call_7538 = func_3479_call()
call_7539 = func_3479_call()
func_3712_call = mod.get_global_var('func_3712')
func_3713_call = mutated_mod.get_global_var('func_3713')
call_7544 = func_3712_call()
call_7545 = func_3712_call()
func_3712_call = mod.get_global_var('func_3712')
func_3713_call = mutated_mod.get_global_var('func_3713')
call_7546 = func_3712_call()
call_7547 = func_3712_call()
bop_7584 = relay.less(call_7546.astype('bool'), relay.reshape(call_7544.astype('bool'), relay.shape_of(call_7546))) # shape=(2, 336)
bop_7587 = relay.less(call_7547.astype('bool'), relay.reshape(call_7545.astype('bool'), relay.shape_of(call_7547))) # shape=(2, 336)
output = relay.Tuple([call_7538,bop_7584,])
output2 = relay.Tuple([call_7539,bop_7587,])
func_7599 = relay.Function([], output)
mod['func_7599'] = func_7599
mod = relay.transform.InferType()(mod)
output = func_7599()
func_7600 = relay.Function([], output)
mutated_mod['func_7600'] = func_7600
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4077_call = mod.get_global_var('func_4077')
func_4078_call = mutated_mod.get_global_var('func_4078')
call_7651 = relay.TupleGetItem(func_4077_call(), 0)
call_7652 = relay.TupleGetItem(func_4078_call(), 0)
func_3946_call = mod.get_global_var('func_3946')
func_3947_call = mutated_mod.get_global_var('func_3947')
call_7657 = relay.TupleGetItem(func_3946_call(), 0)
call_7658 = relay.TupleGetItem(func_3947_call(), 0)
output = relay.Tuple([call_7651,call_7657,])
output2 = relay.Tuple([call_7652,call_7658,])
func_7662 = relay.Function([], output)
mod['func_7662'] = func_7662
mod = relay.transform.InferType()(mod)
mutated_mod['func_7662'] = func_7662
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7662_call = mutated_mod.get_global_var('func_7662')
call_7663 = func_7662_call()
output = call_7663
func_7664 = relay.Function([], output)
mutated_mod['func_7664'] = func_7664
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3946_call = mod.get_global_var('func_3946')
func_3947_call = mutated_mod.get_global_var('func_3947')
call_7672 = relay.TupleGetItem(func_3946_call(), 0)
call_7673 = relay.TupleGetItem(func_3947_call(), 0)
func_5725_call = mod.get_global_var('func_5725')
func_5727_call = mutated_mod.get_global_var('func_5727')
call_7677 = func_5725_call()
call_7678 = func_5725_call()
output = relay.Tuple([call_7672,call_7677,])
output2 = relay.Tuple([call_7673,call_7678,])
func_7686 = relay.Function([], output)
mod['func_7686'] = func_7686
mod = relay.transform.InferType()(mod)
mutated_mod['func_7686'] = func_7686
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7686_call = mutated_mod.get_global_var('func_7686')
call_7687 = func_7686_call()
output = call_7687
func_7688 = relay.Function([], output)
mutated_mod['func_7688'] = func_7688
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4521_call = mod.get_global_var('func_4521')
func_4522_call = mutated_mod.get_global_var('func_4522')
call_7691 = relay.TupleGetItem(func_4521_call(), 1)
call_7692 = relay.TupleGetItem(func_4522_call(), 1)
output = call_7691
output2 = call_7692
func_7712 = relay.Function([], output)
mod['func_7712'] = func_7712
mod = relay.transform.InferType()(mod)
output = func_7712()
func_7713 = relay.Function([], output)
mutated_mod['func_7713'] = func_7713
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6610_call = mod.get_global_var('func_6610')
func_6612_call = mutated_mod.get_global_var('func_6612')
call_7732 = relay.TupleGetItem(func_6610_call(), 0)
call_7733 = relay.TupleGetItem(func_6612_call(), 0)
uop_7741 = relay.rsqrt(call_7732.astype('float64')) # shape=(2, 336)
uop_7743 = relay.rsqrt(call_7733.astype('float64')) # shape=(2, 336)
uop_7744 = relay.cos(uop_7741.astype('float64')) # shape=(2, 336)
uop_7746 = relay.cos(uop_7743.astype('float64')) # shape=(2, 336)
func_4639_call = mod.get_global_var('func_4639')
func_4641_call = mutated_mod.get_global_var('func_4641')
call_7773 = relay.TupleGetItem(func_4639_call(), 0)
call_7774 = relay.TupleGetItem(func_4641_call(), 0)
uop_7782 = relay.asin(uop_7744.astype('float32')) # shape=(2, 336)
uop_7784 = relay.asin(uop_7746.astype('float32')) # shape=(2, 336)
var_7788 = relay.var("var_7788", dtype = "float64", shape = (2, 336))#candidate|7788|(2, 336)|var|float64
bop_7789 = relay.left_shift(uop_7744.astype('uint8'), relay.reshape(var_7788.astype('uint8'), relay.shape_of(uop_7744))) # shape=(2, 336)
bop_7792 = relay.left_shift(uop_7746.astype('uint8'), relay.reshape(var_7788.astype('uint8'), relay.shape_of(uop_7746))) # shape=(2, 336)
output = relay.Tuple([call_7773,uop_7782,bop_7789,])
output2 = relay.Tuple([call_7774,uop_7784,bop_7792,])
func_7793 = relay.Function([var_7788,], output)
mod['func_7793'] = func_7793
mod = relay.transform.InferType()(mod)
var_7794 = relay.var("var_7794", dtype = "float64", shape = (2, 336))#candidate|7794|(2, 336)|var|float64
output = func_7793(var_7794)
func_7795 = relay.Function([var_7794], output)
mutated_mod['func_7795'] = func_7795
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4780_call = mod.get_global_var('func_4780')
func_4782_call = mutated_mod.get_global_var('func_4782')
call_7816 = relay.TupleGetItem(func_4780_call(), 0)
call_7817 = relay.TupleGetItem(func_4782_call(), 0)
output = relay.Tuple([call_7816,])
output2 = relay.Tuple([call_7817,])
func_7824 = relay.Function([], output)
mod['func_7824'] = func_7824
mod = relay.transform.InferType()(mod)
output = func_7824()
func_7825 = relay.Function([], output)
mutated_mod['func_7825'] = func_7825
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4225_call = mod.get_global_var('func_4225')
func_4227_call = mutated_mod.get_global_var('func_4227')
call_7837 = relay.TupleGetItem(func_4225_call(), 0)
call_7838 = relay.TupleGetItem(func_4227_call(), 0)
func_592_call = mod.get_global_var('func_592')
func_595_call = mutated_mod.get_global_var('func_595')
var_7845 = relay.var("var_7845", dtype = "int16", shape = (56, 2))#candidate|7845|(56, 2)|var|int16
const_7846 = relay.const([-10,-1,-8,-7,-6,-9,9,-9,-3,5,-2,-6,4,-1,5,-8,3,-8,-2,5,7,6,-2,-4,-3,4,-8,2,-8,6,-4,-10,8,7,-4,-8,6,4,1,1,-5,-1,-7,6,-7,1,-9,-8,9,-6,10,4,8,-2,-6,-4,1,-5,-10,6,-3,1,-7,10,-8,9,-10,2,10,6,-10,-8,-8,9,-4,-7,1,-3,-1,-2,-7,5,-3,5,2,9,4,10,2,9,-4,5,6,-4,8,6,-9,5,7,-7,-3,-10,4,10,9,4,-8,1,-6,3,-10,-3,9,3,10,-6,6,2,5,-8,1,-10,-10,3,5,-9,-6,-6,-10,10,8,-5,-1,4,8,10,3,-8,-2,-6,8,4,10,8,10,2,-5,2,-3,-2,10,10,-4,6,-9,5,-10,3,10,1,-1,-9,7,4,10,1,-10,3,9,-1,2,8,-8,1,2,9,-5,2,10,4,-2,9,-3,-7,4,1,-6,7,1,4,-1,9,-1,-10,6,2,6,-1,6,3,6,5,4,7,-1,1,4,-8,10,8,9,-6,-3,-5,-5,-8,-4,-6,-4,-6,-6,7,-6,4,10,-3,-2,-5,8,-4,10,-3,-7,-5,-3,-8,-5,-6,-9,-8,-4,1,2,1,-7,2,-8,-2,-5,10,7,7,-4,-4,5,3,4,5,1,7,-10,-5,-5,5,-3,10,-2,3,-1,-8,-8,-8,-6,-10,1,-5,6,1,-9,3,-1,4,-3,-9,4,3,-2,-6,-7,7,4,1,4,-3,-8,4,3,-5,5,-1,5,2,-6,-8,-3,-1,7,-8,3,5,-10,-3,9,7,5,-2,1,-10,2,-10,-10,-3,4,-1,3,-8,-5,3,-2,7,-8,10,4,-6,5,-1,-10,6,-6,-1,-1,1,2,7,4,-3,-2,2,2,-2,6,2,8,10,-4,-4,-9,-10,-8,-7,10,7,-1,-10,8,10,7,-2,1,-10,2,-10,6,-2,-9,-9,6,-3,-4,2,8,10,7,10,-3,-4,6,-5,-6,-9,5,3,3,-10,2,-10,7,4,9,1,8,-8,9,-7,10,9,-3,7,-10,-2,3,3,-2,-2,-2,-5,-8,5,8,-10,1,4,-2,1,-1,6,-6,4,3,9,10,-8,-10,-6,8,-5,-7,-2,-3,3,-5,-8,6,-9,9,-8,3,-9,-2,1,3,8,6,-1,2,-3,-2,8,-4,-1,-4,-3,-7,-1,-7,9,-10,-8,-7,-7,2,8,10,6,-2,6,7,4,-2,-5,1,9,-2,-10,-7,-10,7,-4,1,-3,-8,10,10,1,2,1,9,5,-6,-10,1,1,-5,7,7,-2,10,-2,7,10,-7,-3,10,8,10,-8,-8,-9,6,-1,-5,-9,5,5,3,1,8,-8,9,-6,-4,2,-5,-6,-6,-5,-10,-5,-8,-8,8,2,-1,-4,-8,1,-7,3,3,-5,6,9,-6,2,-7,-6,-10,-10,-9,-3,-7,9,7,-5,3,9,-10,7,7,2,2,10,6,-2,6,-4,-10,-6,6,9,-1,-1,1,9,-1,-3,-8,-4,-4,-1,-2,5,9,10,5,7,8,-1,9,-8,-2,3,3,-6,4,9,-2,9,-8,-9,8,10,-7,6,10,6,4,-2,1,-6,-5,2,-1,-1,7,3,7,1,4,-9,1,6,9,2,8,-4,5,10,-4,-7,10,-8,5,8,9,6,3,5,2,1,-7,2,-8,2,-3,4,-10,10,-4,-7,-8,-2,6,4,-7,9,7,-8,4,-8,8,2], dtype = "int16")#candidate|7846|(672,)|const|int16
call_7844 = relay.TupleGetItem(func_592_call(relay.reshape(var_7845.astype('int16'), [16, 1, 7]), relay.reshape(const_7846.astype('int16'), [16, 6, 7]), ), 0)
call_7847 = relay.TupleGetItem(func_595_call(relay.reshape(var_7845.astype('int16'), [16, 1, 7]), relay.reshape(const_7846.astype('int16'), [16, 6, 7]), ), 0)
var_7850 = relay.var("var_7850", dtype = "int16", shape = (56, 2))#candidate|7850|(56, 2)|var|int16
bop_7851 = relay.subtract(var_7845.astype('uint64'), relay.reshape(var_7850.astype('uint64'), relay.shape_of(var_7845))) # shape=(56, 2)
output = relay.Tuple([call_7837,call_7844,const_7846,bop_7851,])
output2 = relay.Tuple([call_7838,call_7847,const_7846,bop_7851,])
func_7859 = relay.Function([var_7845,var_7850,], output)
mod['func_7859'] = func_7859
mod = relay.transform.InferType()(mod)
mutated_mod['func_7859'] = func_7859
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7859_call = mutated_mod.get_global_var('func_7859')
var_7861 = relay.var("var_7861", dtype = "int16", shape = (56, 2))#candidate|7861|(56, 2)|var|int16
var_7862 = relay.var("var_7862", dtype = "int16", shape = (56, 2))#candidate|7862|(56, 2)|var|int16
call_7860 = func_7859_call(var_7861,var_7862,)
output = call_7860
func_7863 = relay.Function([var_7861,var_7862,], output)
mutated_mod['func_7863'] = func_7863
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7712_call = mod.get_global_var('func_7712')
func_7713_call = mutated_mod.get_global_var('func_7713')
call_7876 = func_7712_call()
call_7877 = func_7712_call()
output = call_7876
output2 = call_7877
func_7881 = relay.Function([], output)
mod['func_7881'] = func_7881
mod = relay.transform.InferType()(mod)
mutated_mod['func_7881'] = func_7881
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7881_call = mutated_mod.get_global_var('func_7881')
call_7882 = func_7881_call()
output = call_7882
func_7883 = relay.Function([], output)
mutated_mod['func_7883'] = func_7883
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7915 = relay.var("var_7915", dtype = "float32", shape = (4, 5, 13))#candidate|7915|(4, 5, 13)|var|float32
uop_7916 = relay.rsqrt(var_7915.astype('float32')) # shape=(4, 5, 13)
bop_7922 = relay.right_shift(uop_7916.astype('uint64'), relay.reshape(var_7915.astype('uint64'), relay.shape_of(uop_7916))) # shape=(4, 5, 13)
func_7824_call = mod.get_global_var('func_7824')
func_7825_call = mutated_mod.get_global_var('func_7825')
call_7929 = relay.TupleGetItem(func_7824_call(), 0)
call_7930 = relay.TupleGetItem(func_7825_call(), 0)
func_4044_call = mod.get_global_var('func_4044')
func_4049_call = mutated_mod.get_global_var('func_4049')
var_7935 = relay.var("var_7935", dtype = "int16", shape = (672,))#candidate|7935|(672,)|var|int16
var_7936 = relay.var("var_7936", dtype = "float64", shape = (81,))#candidate|7936|(81,)|var|float64
const_7937 = relay.const([0.812386,-5.640453,-7.428524,8.209291,5.843640,3.870532,-3.066337,7.573179,-5.087290,-9.760026,-7.345226,-1.483158,-4.336000,-6.588757,-6.311557,6.395446,-2.750242,-9.638472,-2.760295,-6.586216,-5.753743,-9.446825,-0.775906,-8.606353,8.029159,-0.897054,5.220248,7.399397,5.877069,-8.866188,2.074711,0.784228,2.544566,-8.615096,8.519093,6.709900,4.404741,-9.366766,-3.365312,-7.732544,5.457889,2.892297,2.142669,1.719044,-0.806648,9.851326,5.146538,1.327860,-3.521209,-1.048740,-1.610259,8.152820,-6.906224,-9.745511,7.700010,-5.081033,0.973720,4.250178,-7.137374,4.507342,-9.293758,4.705923,0.548899,-5.931517,-5.057619,7.799141,2.054408,-0.822118,-4.005037,-6.006985,1.117997,-8.196638,-3.932720,-0.296594,-8.420304,4.848722,-4.506151,9.494202,9.102920,9.838926,-3.884069,6.321170,9.745889,5.302725,-8.637288,7.989198,2.212221,-2.468352,-7.649821,-8.385322,-4.535080,1.658948,-5.463420,-6.553219,3.759379,-6.416853,-6.253664,3.672258,5.267426,7.926796,-7.202226,-3.745624,-6.705083,2.656783,2.270286,-0.241768,4.777622,-7.239896,-1.625573,9.481987,-8.372002,7.267125,5.753103,-4.455223,-7.860847,-1.279900,8.889562,-6.764203,3.468499,-1.454722,3.916757,-0.112302,-4.392109,4.340972,2.831525,-7.684233,-5.083605,-8.426386,-6.196169,-8.282843,-7.680469,3.440741,9.681276,-2.082854,2.846777,3.741546,2.967010,1.581109,-1.827626,-2.923434,-3.507417,8.150310,-3.925878,-9.771149,3.541865,2.974044,-3.278303,8.861970,-7.451795,-0.883493,-8.167924,8.393067,-8.991174,6.496599,5.707501,-7.280079,1.267061,-4.176864,-2.246895,-4.194325,3.674088,1.322636,5.902839,-2.715930,-9.475042,7.388505,-9.682738,-6.436621,-7.637266,-9.886462,9.725462,1.162631,-7.848105,1.686398,-2.155413,-9.955003,2.750830,3.916904,-4.608668,7.353144,2.709357,3.806003,6.842329,-4.112976,-7.473215,9.057725,7.224019,-2.083713,-0.060015,-8.717666,8.181466,-4.164362,9.933369,8.038555,6.352173,-7.336659,-6.264486,3.011640,-7.539484,1.244019,-6.446597,-4.111581,4.410755,3.412579,-0.028574,-6.798848,1.416435,6.312256,5.646051,-0.395710,3.270935,4.645302,4.234784,4.749598,-0.334284,-6.117171,4.422937,-3.629672,8.183098,-9.115104,-9.423523,1.307928,0.029719,-3.284980,-6.119260,-9.176745,9.463449,0.808025,-4.116781,-2.133439,8.750365,0.399126,-5.323451,9.416419,2.729979,2.914822,-3.115139,7.593441,7.598728,-1.875512,9.283197,0.518758,-0.159977,0.656411,4.159536,1.706229,-7.278747,0.972748,4.488962,-7.564521,-9.021473,-0.902812,-9.247916,4.728541,9.937088,1.267771,-7.756787,9.354290,3.075153,5.491108,2.121598,2.128126,5.353813,-3.184094,6.934157,0.824072,-5.907094,7.507238,-8.600935,1.147111,-3.267256,-0.505894,1.951905,-2.588996,-3.118371,-3.510828,-3.121313,8.772989,-8.424712,-3.953063,-5.463099,-0.201038,1.239212,6.511792,-6.792638,5.643167,-1.189978,8.638161,-6.841196,-0.403227,2.494755,-9.327977,0.188607,8.009443,3.654970,5.493794,7.775546,-3.133119,1.023765,-3.660567,-4.641857,1.232657,8.261746,1.608020,-7.595359,-6.221909,-3.308305,4.629266,-7.365756,7.507093,2.876943,6.462322,-9.363574,7.513693,-0.380695,0.470666,-2.642454,7.121411,6.328667,4.895032,-2.086757,2.490171,-1.019729,-2.800322,9.511735,-6.231861,6.497278,-5.882917,8.451878,8.711432,8.951244,6.106542,3.352123,-7.541073,5.206265,-6.285267,1.455894,-7.381798,1.809908,5.281316,-7.962383,3.222459,5.423919,-2.603439,8.883225,-6.726066,-7.310554,-2.592253,-5.400352,6.783086,-1.551918,-7.597002,1.252174,2.986429,4.121842,-8.620195,-7.541075,3.640554,8.012288,6.059234,-3.152381,0.893855,6.249590,-3.729653,-8.464697,8.624193,-3.983316,8.272522,-3.907966,-6.408493,7.769177,2.451488,-2.857265,9.912249,-4.286583,-0.585061,3.098039,-2.304166,-3.971075,-1.707824,-1.244660,7.590536,2.065259,-6.050579,-0.019671,-0.494471,5.171252,2.009521,-0.957423,6.982555,4.179110,8.942880,-8.554899,9.701013,2.003418,6.930575,5.111714,-4.874967,7.422183,-7.151202,7.531690,5.021501,3.091079,-5.092625,-4.609496,-5.606654,4.653509,-4.995147,8.318203,-5.185747,5.241181,-6.005085,3.908151,-9.770580,-9.820633,-7.519919,0.581074,-5.251120,-7.932031,-1.036304,7.105218,8.212155,9.945431,-5.048411,0.525372,0.552466,-9.550220,-8.182514,-7.356726,7.647821,6.002998,-2.754528,0.853288,6.054074,8.615207,-1.959370,1.536532,8.716143,2.138536,5.406151,5.302464,-7.933387,2.960742,9.021976,4.744077,-7.474462,-3.415699,1.474865,3.088873,5.795980,-3.195157,6.822773,8.211990,-1.668983,-6.548474,-9.755809,-9.697503,-7.487894,6.398064,4.923108,-9.943099,5.713870,-7.748133,-8.387502,-5.242809,-0.010903,-8.340610,-9.063181,7.643870,-8.090536,-2.512007,0.350519,6.071416,-8.602865,0.859194,0.644311,7.014487,-9.016891,8.812464,-9.178774,-8.436825,8.255103,-7.368004,0.909295,-0.248165,-5.670767,-1.516941,-9.797463,9.054102,-4.313083,-8.169305,-7.880780,-7.101405,-5.907217,5.438305,7.695055,0.795136,-5.280113,-4.669005,3.869256,-6.202980,-8.584741,4.298200,-9.745350,4.650178,5.410025,4.847914,-1.941570,-6.914114,9.885864,1.233271,-0.468714,6.002164,-7.761510,-6.082140,2.043852,0.646796,2.829741,-6.247436,6.334361,-7.638124,9.488499,-5.018258,7.046104,-9.775216,9.629030,-2.555158,3.744059,-4.660790,3.777277,1.018802,0.416009,-4.861663,-1.676384,1.143139,7.929579,-8.483579,3.158641,-6.365843,-9.882827,3.072339,-8.897878,0.886095,-6.222360,6.532413,-6.686089,-8.850161,-3.753506,-3.784547,8.241966,-2.832424,8.557628,2.453872,-1.511230,8.192004,2.515985,-9.975184,-5.558460,3.845260,7.192187,4.403143,2.056245,-7.153874,-2.307854,-7.129151,-1.185650,-2.641064,-4.213583,-3.455119,9.021052,6.098714,-1.258524,-5.750976,1.561295,5.485184,5.749412,-5.901860,-5.678570,-9.000850,3.923577,-3.961475,2.158605,7.153339,8.639765,-7.171144,3.625869,6.975800,9.196353,5.381376,7.309918,-7.401146,0.255329,5.317702,3.726989,-7.441394,6.068875,-1.861424,-0.821556,-6.238227,4.519239,-2.973882,-7.469901,-5.128053,-0.552743,-3.041188,2.539431,-0.880805,3.467064,-3.965872,7.384341,0.342025,-0.494659,3.847157,4.564044,-4.850515,3.273286,4.147828,-9.777273,4.600101,3.598756,-0.672826,-0.748033,9.201119,-6.646141,-5.519971,5.698470,-8.983301,4.134667,-6.014270,8.732036,4.006653,6.747775,-4.207818,8.311315,-1.930851,1.598198,2.001166,8.310530,4.260130,-5.258875,5.533507,4.335892,5.202616,-5.425516,3.318366,-8.840809,-2.142814,-8.954480,0.515382,-7.191616,-8.235095,-7.299634,-2.687554,0.024659,-2.441087,3.719399,3.188847,1.923006,-9.746913,-1.036615,-1.464319,-9.039558,-6.355154,1.716609,-1.115323,-0.330009,-4.097760,-1.575521,-9.058608,-3.349864,-8.788777,7.096296,5.497757,-5.812800,-1.791019,1.415905,-1.338440,6.020261,-5.526593,-8.118921,-8.182240,-7.061546,-5.506872,5.396231,-8.705812,4.543188,-6.867225,-1.440000,7.725374,3.159349,7.719475,-6.153367,-7.546721,-2.556534,3.165925,-9.381985,9.675298,-9.837703,5.897207,7.366785,8.722837,-1.323887,3.990642,2.078465,-6.967893,-7.717178,-6.115964,6.379518,-3.863052,0.549048,-0.621490,5.024198,-4.028488,9.847505,-3.242564,7.641881,7.807248,5.652805,-9.373308,-7.367524,1.216650,-6.788519,4.573295,-2.861135,-5.625485,4.269967,8.510151,-4.069398,-3.610577,-1.930808,-2.158260,6.384531,0.321362,-2.592583,8.455295,-8.372306,9.963219,-1.000579,-9.755639,-9.593783,0.305983,-8.149343,3.637533,-6.369699,-3.930539,-5.318242,3.012689,2.771717,-1.788719,-0.572859,-4.362756,-2.526216,-7.658792,-8.381611,0.605608,4.225664,2.374518,-5.108822,-4.732038,-5.925186,5.203111,-7.751871,-2.913730,0.776833,2.117597,5.675769,8.105831,-4.660120,-1.476321,-7.933128,7.526469,-4.098072,3.789731,0.330209,-1.457382,2.725917,-3.101313,-9.748585,4.223979,8.166465,2.182131,-9.663872,-9.360713,-9.775497,7.706026,3.978722,-4.936026,4.921448,-7.089858,-9.860335,3.395970,-0.126943,3.148897,-0.501189,-3.436612,5.691026,-3.591801,-2.017580,-8.175538,-8.098661,-0.307614,7.763763,5.893715,-5.486178,0.418765,-5.084260,-4.554475,1.804895,5.359922,-8.366230,0.721552,-2.578107,6.855133,7.224559,2.504501,-3.448650,5.649502,3.909911,-0.418892,-3.690999,-8.690355,-5.648916,0.882974,-1.591358,-0.238975,-5.361335,-6.270598,8.342499,-5.527627,-4.171207,-0.493576,6.176621,-3.731017,3.050357,-7.125915,-8.219161,-2.410490,-1.597680,-7.169733,6.893432,2.745869,1.271189,-0.607888,-4.371504,2.754607,-3.118447,7.535920,9.119602,-0.433677,-6.646445,-0.931937,4.470960,-2.154727,-7.690606,-4.515398,6.914183,4.326369,-4.529048,0.932051,-9.236222,5.876560,3.996699,-9.253063,-8.527112,2.719807,-1.932671,3.105590,-1.553286,2.213107,7.049346,-4.909980,2.042391,5.945559,2.107457,-1.885646,2.273744,0.269220,-1.340075,0.907719,-4.389364,-1.973376,-0.168436,4.440813,3.625335,0.898746,-4.657781,0.751123,7.459418,8.478706,0.411202,6.852016,4.109332,7.674956,-8.962076,-8.209140,8.333846,5.947082,7.271110,9.371517,7.099841,5.751142,-1.271974,-6.661691,4.661336,8.171850,8.482906,0.321229,7.545168,4.125872,0.351809,-5.638240,-9.523218,-5.707543,-4.627343,-5.659480,-5.902554,-0.551007,-2.855708,-9.525440,-8.593956,-4.375581,-7.273408,4.024578,7.477736,-2.211770,-4.832074,2.019121,-6.192677,-8.431495,7.618506,4.879407,-1.202722,8.420577,-7.516791,-0.910400,4.063824,-8.000394,-8.484344,2.938854,-9.499505,-9.386538,-7.496323,2.841175,4.710502,-1.425907,-5.618100,-3.294257,0.647994,3.969945,-2.529887,-0.688468,1.283456,1.378285,-8.589136,1.886949,-5.821430,-2.481240,0.452376,-3.939009,0.037601,-9.139485,-2.946544,0.488887,-4.728693,0.390941,-1.563408,-8.936150,-8.476573,-6.374953,-0.547744,-6.844641,2.099195,5.257596,-2.116462,-9.230535,-3.933888,-3.359747,1.102446,-5.383231,-2.430196,-3.633675,-1.347307,-2.985870,0.008417,5.221251,-6.838073,-4.569389,-6.892231,0.232373,8.872485,8.135906,-6.248842,-5.403788,9.760522,1.256113,-7.236178,-1.747311,-4.119897,-6.465296,6.376371,5.247843,5.282483,-5.185211,8.632703,-1.693485,9.767630,1.447403,6.217688,1.770537,-2.633425,9.646474,6.452368,4.975994,-2.931027,9.659113,-0.558583,-9.933924,-8.261862,2.109438,-2.088352,7.798936,2.557111,0.045339,-8.095571,2.448673,8.845490,-7.455630,9.920673,-7.753322,0.797548,9.224718,-5.003588,6.373308,-6.607782,-4.965159,-7.722260,-5.897500,-7.064847,0.047842,8.386758,-0.184558,7.549818,5.438319,-2.236574,-5.793014,8.349065,9.942351,9.277437,-7.534143,-9.934727,-8.285157,-3.264471,-5.989088,-2.473581,-8.653691,7.084449,-0.859019,0.512871,3.436414,1.086591,3.357330,9.240614,-9.888321,4.797062,9.157482,-7.475460,-6.822024,-8.044398,5.712598,-2.097820,-2.703554,-9.748522,-4.330520,-1.735828,-8.089952,-6.968249,-8.647522,-2.464472,-6.551753,-6.981983,9.492864,-6.212872,5.311446,1.890732,4.857398,-2.806449,4.401619,3.402222,-3.359034,8.336244,1.225177,-0.716834,1.767557,6.560925,-5.822063,6.115550,-4.247407,-5.526019,0.953266,-0.495312,3.811149,-4.895253,-5.238987,1.303181,-5.935977,8.866188,-2.743321,1.128874,-5.561593,8.878465,-2.379138,7.883925,-6.961749,7.565486,7.685037,1.502068,-6.064480,4.227408,2.717219,-3.437392,5.373313,6.452161,2.448614,3.024870,8.712486,5.768505,-3.300547,-3.162819,-5.303347,-1.473881,-6.002674,-2.175174,2.122636,1.022681,-0.856539,-8.380325,6.561723,8.997904,9.825986,-1.567281,-5.832253,-7.606615,-2.182672,5.617282,-8.279243,-8.898037,1.476703,-6.939108,-4.089596,9.227323,2.252579,-4.027866,-3.978812,0.117484,9.513554,-6.391199,9.619777,-7.660938,-8.183078,-3.899636,4.351142,9.547385,-1.552953,7.130110,0.940730,9.167837,2.012292,3.575135,-6.221983,0.565062,-9.798992,4.229425,-7.956454,-2.736852,0.610722,-5.365225,1.824263,-6.955293,4.801760,1.547501,-9.812670,1.241727,-9.640675,8.684091,8.795500,-3.701647,1.283062,-2.676279,4.981306,-0.191221,8.760462,3.755553,-4.245001,-7.492734,-1.194037,-8.495521,8.126680,-7.725806,-9.927871,-7.879053,-3.299740,3.421429,-5.171549,5.748752,-7.301656,-5.688257,-8.290295,0.149650,1.890250,-8.810652,8.050081,6.803878,-9.382019,-7.961062,8.829500,2.022647,-4.366286,1.071056,-8.168084,-1.620634,-4.893176,-4.379133,3.223527,9.923079,-9.902280,-6.781259,-7.657856,-3.573800,0.222427,6.372985,3.644508,-3.738985,-1.074873,-0.814439,-9.920125,9.210734,3.369490,-5.998013,9.437172,-1.166697,2.400730,8.995280,-4.247123,2.970094,0.767327,-3.926098,5.001454,-8.747744,7.527145,-1.336615,6.550644,-3.200103,0.149886,0.888081,8.419342,-6.043935,-5.082636,-9.604499,3.396137,-9.965244,2.508617,1.928370,5.243352,-1.340865,-5.775791,9.419338,-1.125432,5.477957,-3.940885,4.881662,-6.398301,-2.850380,9.476251,5.892930,-7.178442,2.919114,-1.928253,-8.071342,-0.075880,-3.444481,9.436365,0.762034,-2.480592,-5.986969,1.070781,-5.819988,0.599286,6.063798,5.800510,-8.402146,-0.444976,8.854596,-5.395498,9.597099,-9.271955,-8.351239,9.146213,-0.120814,-9.566100,-9.669679,-7.154797,9.219445,4.788519,-3.127187,5.145455,5.263984,4.062527,-4.392042,-8.510004,-6.977979,-4.637333,8.599565,-3.570485,0.269270,-4.903762,8.438581,-5.021508,-9.101497,4.990899,-5.126302,8.275271,-1.231154,0.454989,8.538796,-5.422159,-8.722616,-3.346175,-6.549693,8.823749,3.025223,2.350473,-9.099083,3.040782,-7.754409,-2.699471,3.319491,-1.292215,-4.748149,-1.295087,9.554143,9.682917,5.275668,4.209386,5.680957,2.202966,-3.178844,7.963634,-4.309396,-6.063887,2.475469,-1.769785,-7.126571,-4.348169,-2.820314,-3.699828,-2.568973,6.138135,6.101369,6.208237,-1.954335,4.357468,-6.133405,0.851870,9.160121,5.921597,-4.367003,6.250121,-7.174704,2.435699,8.322377,-4.830370,-2.670503,5.367606,9.877265,-9.958369,-7.752770,-3.757827,-9.706057,1.145859,3.236521,-2.974716,-8.927077,4.140088,8.730087,2.317461,-1.424074,-4.898390,-5.205940,2.654727,5.343064,9.438971,5.903177,-8.327024,4.867237,-9.461066,-5.811804,1.616904,-2.661405,2.884088,8.986217,-3.574692,-2.815442,-2.564221,2.898101,-2.368672,0.248657,-8.683690,-2.077183,-1.419561,-3.045524,-5.837124,3.465594,-7.188142,-1.750970,-5.357856,-6.605069,-4.427048,6.121252,4.568090,-7.004706,7.142952,1.055400,-5.164885,-2.580271,-6.491276,5.722497,9.562889,-1.602968,6.777164,2.896354,-1.492528,-2.002002,3.092576,-1.120575,-5.227445,-9.838880,-9.314148,0.609725,3.533011,-1.181544,4.256629,3.927285,-3.283337,-5.592471,-1.526503,6.538302,7.088624,4.507789,-8.608078,-0.672365,-8.870946,-6.482131,-2.614318,-4.336719,-7.289656,6.597163], dtype = "float64")#candidate|7937|(1456,)|const|float64
call_7934 = relay.TupleGetItem(func_4044_call(relay.reshape(var_7935.astype('int16'), [672,]), relay.reshape(var_7936.astype('float64'), [27, 3]), relay.reshape(const_7937.astype('float64'), [1456,]), ), 1)
call_7938 = relay.TupleGetItem(func_4049_call(relay.reshape(var_7935.astype('int16'), [672,]), relay.reshape(var_7936.astype('float64'), [27, 3]), relay.reshape(const_7937.astype('float64'), [1456,]), ), 1)
func_5268_call = mod.get_global_var('func_5268')
func_5269_call = mutated_mod.get_global_var('func_5269')
call_7939 = func_5268_call()
call_7940 = func_5268_call()
func_3479_call = mod.get_global_var('func_3479')
func_3480_call = mutated_mod.get_global_var('func_3480')
call_7947 = func_3479_call()
call_7948 = func_3479_call()
func_3905_call = mod.get_global_var('func_3905')
func_3906_call = mutated_mod.get_global_var('func_3906')
call_7965 = func_3905_call()
call_7966 = func_3905_call()
bop_7968 = relay.divide(uop_7916.astype('float32'), relay.reshape(bop_7922.astype('float32'), relay.shape_of(uop_7916))) # shape=(4, 5, 13)
func_5534_call = mod.get_global_var('func_5534')
func_5536_call = mutated_mod.get_global_var('func_5536')
var_7992 = relay.var("var_7992", dtype = "bool", shape = (225,))#candidate|7992|(225,)|var|bool
call_7991 = relay.TupleGetItem(func_5534_call(relay.reshape(var_7992.astype('bool'), [225,])), 1)
call_7993 = relay.TupleGetItem(func_5536_call(relay.reshape(var_7992.astype('bool'), [225,])), 1)
func_7326_call = mod.get_global_var('func_7326')
func_7327_call = mutated_mod.get_global_var('func_7327')
call_7994 = relay.TupleGetItem(func_7326_call(), 0)
call_7995 = relay.TupleGetItem(func_7327_call(), 0)
output = relay.Tuple([call_7929,call_7934,var_7935,var_7936,const_7937,call_7939,call_7947,call_7965,bop_7968,call_7991,var_7992,call_7994,])
output2 = relay.Tuple([call_7930,call_7938,var_7935,var_7936,const_7937,call_7940,call_7948,call_7966,bop_7968,call_7993,var_7992,call_7995,])
func_7997 = relay.Function([var_7915,var_7935,var_7936,var_7992,], output)
mod['func_7997'] = func_7997
mod = relay.transform.InferType()(mod)
var_7998 = relay.var("var_7998", dtype = "float32", shape = (4, 5, 13))#candidate|7998|(4, 5, 13)|var|float32
var_7999 = relay.var("var_7999", dtype = "int16", shape = (672,))#candidate|7999|(672,)|var|int16
var_8000 = relay.var("var_8000", dtype = "float64", shape = (81,))#candidate|8000|(81,)|var|float64
var_8001 = relay.var("var_8001", dtype = "bool", shape = (225,))#candidate|8001|(225,)|var|bool
output = func_7997(var_7998,var_7999,var_8000,var_8001,)
func_8002 = relay.Function([var_7998,var_7999,var_8000,var_8001,], output)
mutated_mod['func_8002'] = func_8002
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5268_call = mod.get_global_var('func_5268')
func_5269_call = mutated_mod.get_global_var('func_5269')
call_8069 = func_5268_call()
call_8070 = func_5268_call()
func_3426_call = mod.get_global_var('func_3426')
func_3428_call = mutated_mod.get_global_var('func_3428')
call_8071 = relay.TupleGetItem(func_3426_call(), 3)
call_8072 = relay.TupleGetItem(func_3428_call(), 3)
output = relay.Tuple([call_8069,call_8071,])
output2 = relay.Tuple([call_8070,call_8072,])
func_8077 = relay.Function([], output)
mod['func_8077'] = func_8077
mod = relay.transform.InferType()(mod)
output = func_8077()
func_8078 = relay.Function([], output)
mutated_mod['func_8078'] = func_8078
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8090 = relay.var("var_8090", dtype = "uint32", shape = (5, 3, 1))#candidate|8090|(5, 3, 1)|var|uint32
var_8091 = relay.var("var_8091", dtype = "uint32", shape = (5, 3, 16))#candidate|8091|(5, 3, 16)|var|uint32
bop_8092 = relay.bitwise_xor(var_8090.astype('uint32'), var_8091.astype('uint32')) # shape=(5, 3, 16)
func_5928_call = mod.get_global_var('func_5928')
func_5930_call = mutated_mod.get_global_var('func_5930')
call_8108 = func_5928_call()
call_8109 = func_5928_call()
func_4683_call = mod.get_global_var('func_4683')
func_4685_call = mutated_mod.get_global_var('func_4685')
call_8111 = relay.TupleGetItem(func_4683_call(), 1)
call_8112 = relay.TupleGetItem(func_4685_call(), 1)
uop_8121 = relay.log2(var_8091.astype('float32')) # shape=(5, 3, 16)
func_5366_call = mod.get_global_var('func_5366')
func_5368_call = mutated_mod.get_global_var('func_5368')
call_8132 = func_5366_call()
call_8133 = func_5366_call()
func_4410_call = mod.get_global_var('func_4410')
func_4414_call = mutated_mod.get_global_var('func_4414')
var_8142 = relay.var("var_8142", dtype = "bool", shape = (225,))#candidate|8142|(225,)|var|bool
call_8141 = relay.TupleGetItem(func_4410_call(relay.reshape(bop_8092.astype('float64'), [6, 4, 10]), relay.reshape(var_8142.astype('bool'), [225, 1]), ), 5)
call_8143 = relay.TupleGetItem(func_4414_call(relay.reshape(bop_8092.astype('float64'), [6, 4, 10]), relay.reshape(var_8142.astype('bool'), [225, 1]), ), 5)
output = relay.Tuple([bop_8092,call_8108,call_8111,uop_8121,call_8132,call_8141,var_8142,])
output2 = relay.Tuple([bop_8092,call_8109,call_8112,uop_8121,call_8133,call_8143,var_8142,])
func_8148 = relay.Function([var_8090,var_8091,var_8142,], output)
mod['func_8148'] = func_8148
mod = relay.transform.InferType()(mod)
var_8149 = relay.var("var_8149", dtype = "uint32", shape = (5, 3, 1))#candidate|8149|(5, 3, 1)|var|uint32
var_8150 = relay.var("var_8150", dtype = "uint32", shape = (5, 3, 16))#candidate|8150|(5, 3, 16)|var|uint32
var_8151 = relay.var("var_8151", dtype = "bool", shape = (225,))#candidate|8151|(225,)|var|bool
output = func_8148(var_8149,var_8150,var_8151,)
func_8152 = relay.Function([var_8149,var_8150,var_8151,], output)
mutated_mod['func_8152'] = func_8152
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5366_call = mod.get_global_var('func_5366')
func_5368_call = mutated_mod.get_global_var('func_5368')
call_8170 = func_5366_call()
call_8171 = func_5366_call()
output = relay.Tuple([call_8170,])
output2 = relay.Tuple([call_8171,])
func_8191 = relay.Function([], output)
mod['func_8191'] = func_8191
mod = relay.transform.InferType()(mod)
mutated_mod['func_8191'] = func_8191
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8191_call = mutated_mod.get_global_var('func_8191')
call_8192 = func_8191_call()
output = call_8192
func_8193 = relay.Function([], output)
mutated_mod['func_8193'] = func_8193
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7881_call = mod.get_global_var('func_7881')
func_7883_call = mutated_mod.get_global_var('func_7883')
call_8219 = func_7881_call()
call_8220 = func_7881_call()
var_8223 = relay.var("var_8223", dtype = "int16", shape = (2, 336))#candidate|8223|(2, 336)|var|int16
bop_8224 = relay.bitwise_or(call_8219.astype('int32'), relay.reshape(var_8223.astype('int32'), relay.shape_of(call_8219))) # shape=(2, 336)
bop_8227 = relay.bitwise_or(call_8220.astype('int32'), relay.reshape(var_8223.astype('int32'), relay.shape_of(call_8220))) # shape=(2, 336)
output = relay.Tuple([bop_8224,])
output2 = relay.Tuple([bop_8227,])
func_8230 = relay.Function([var_8223,], output)
mod['func_8230'] = func_8230
mod = relay.transform.InferType()(mod)
mutated_mod['func_8230'] = func_8230
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8231 = relay.var("var_8231", dtype = "int16", shape = (2, 336))#candidate|8231|(2, 336)|var|int16
func_8230_call = mutated_mod.get_global_var('func_8230')
call_8232 = func_8230_call(var_8231)
output = call_8232
func_8233 = relay.Function([var_8231], output)
mutated_mod['func_8233'] = func_8233
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8288 = relay.var("var_8288", dtype = "float64", shape = (6, 3, 5))#candidate|8288|(6, 3, 5)|var|float64
uop_8289 = relay.sigmoid(var_8288.astype('float64')) # shape=(6, 3, 5)
output = relay.Tuple([uop_8289,])
output2 = relay.Tuple([uop_8289,])
func_8306 = relay.Function([var_8288,], output)
mod['func_8306'] = func_8306
mod = relay.transform.InferType()(mod)
var_8307 = relay.var("var_8307", dtype = "float64", shape = (6, 3, 5))#candidate|8307|(6, 3, 5)|var|float64
output = func_8306(var_8307)
func_8308 = relay.Function([var_8307], output)
mutated_mod['func_8308'] = func_8308
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5317_call = mod.get_global_var('func_5317')
func_5318_call = mutated_mod.get_global_var('func_5318')
call_8329 = relay.TupleGetItem(func_5317_call(), 2)
call_8330 = relay.TupleGetItem(func_5318_call(), 2)
output = call_8329
output2 = call_8330
func_8331 = relay.Function([], output)
mod['func_8331'] = func_8331
mod = relay.transform.InferType()(mod)
output = func_8331()
func_8332 = relay.Function([], output)
mutated_mod['func_8332'] = func_8332
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8351 = relay.var("var_8351", dtype = "int64", shape = (13, 4, 16))#candidate|8351|(13, 4, 16)|var|int64
const_8352 = relay.const([[[9,-3,2,2,6,-8,-10,2,8,3,-2,-2,6,2,-5,2],[-6,8,-9,-4,8,1,6,7,-7,-9,-5,-3,-5,3,-1,1],[-9,7,-1,-10,2,8,7,4,-6,-4,-6,-3,5,10,-10,3],[-1,-7,1,3,1,3,-5,-3,-2,1,7,8,2,7,-10,-1]],[[-3,3,-6,-1,-6,-4,-3,-3,7,4,9,-5,1,-1,4,-2],[-10,5,1,-4,2,9,8,-2,-7,-6,-8,5,3,-2,10,6],[-9,10,8,-9,4,6,2,-5,-4,-3,-4,-4,6,3,-8,-10],[1,6,-3,-10,7,-9,3,7,-6,10,1,-6,7,-5,-2,1]],[[2,-5,-6,-2,-8,-9,-4,6,7,2,7,-6,-9,1,-5,-7],[2,4,4,9,6,2,-6,-9,-6,2,-9,10,-1,-1,3,-5],[-7,-3,4,4,-1,9,-7,-4,-9,6,7,8,-7,6,9,3],[10,-9,-9,6,9,9,4,-9,-10,-3,-1,6,-3,5,4,8]],[[-5,10,-9,-6,-2,4,-8,10,-8,-6,-5,-6,-3,-10,3,10],[-4,4,9,-4,6,-10,3,-4,-3,1,-3,8,-9,2,8,-10],[4,-8,5,-7,-1,5,5,4,-10,-9,1,-6,8,2,1,10],[7,10,1,-3,4,-6,-5,-10,7,-5,-7,-3,-10,2,-9,9]],[[-2,8,-8,-6,6,1,6,8,1,6,-6,-4,3,10,-2,-8],[9,10,6,8,-9,5,2,-1,-9,-10,5,5,-4,10,5,-10],[5,-10,7,-2,6,-4,-3,1,3,6,7,-7,-6,9,-6,-6],[1,1,1,-4,3,7,-4,-7,-2,-4,6,-2,-10,-6,1,7]],[[-5,10,4,-6,2,4,-4,3,-5,6,10,-6,10,9,3,3],[-4,7,-5,-6,8,4,-8,7,4,7,-3,6,-4,-3,1,-6],[-7,5,-5,10,9,-5,-1,-2,-8,-10,-1,-2,-9,3,-1,5],[1,-1,-10,-2,-6,-6,9,-1,7,8,6,-5,5,5,7,3]],[[1,-8,4,10,5,7,5,5,-7,-10,-10,-10,-2,-10,-6,-9],[-6,9,-5,2,-6,7,6,3,-2,-6,7,1,10,8,-6,-6],[2,-4,6,-8,-6,-2,-7,-6,8,-5,-10,4,-8,8,7,-6],[-9,7,-8,-8,2,-9,-4,9,-8,7,-1,-8,3,-2,-1,-1]],[[-1,-6,3,-5,3,-5,-8,-1,3,4,8,4,1,-2,-6,-3],[-1,-8,-2,-1,-7,-3,5,3,1,1,-3,-1,-10,-5,5,-3],[-6,1,4,-4,-10,-7,-1,10,-8,-1,5,5,4,4,-7,-6],[-10,2,8,-4,-5,3,1,-5,-4,2,-8,-7,-5,2,7,-7]],[[-4,10,7,2,5,7,9,-5,-8,-6,-1,1,-3,-2,-10,7],[9,7,9,7,7,10,-6,10,-3,2,-9,-4,5,-3,4,-2],[5,-1,1,10,4,3,-8,-5,1,-5,-2,5,4,6,-5,-10],[-8,-7,-1,-6,-1,-6,-3,-10,-10,-5,3,-10,7,4,2,4]],[[-7,10,10,-4,6,9,-10,-4,-3,1,-10,-2,6,-10,-10,-2],[-5,-6,10,-7,-9,-6,5,-9,8,4,-2,-4,2,9,-8,2],[5,10,9,10,6,-9,5,-1,8,10,4,10,-9,2,10,-3],[-4,-10,2,3,5,1,9,-2,9,-9,-9,-9,-6,8,-4,2]],[[-3,1,2,7,3,9,2,-9,7,-2,-6,7,-3,-1,3,7],[6,5,-9,7,-10,5,10,-1,-3,3,7,1,-4,-8,-6,5],[2,-1,-10,-4,7,-10,-5,-5,-5,8,-10,-3,3,-1,6,-4],[6,9,6,-8,-5,3,1,-10,8,-10,1,1,5,-5,-10,9]],[[-6,1,2,-8,-10,-8,-9,-7,6,-5,1,1,2,6,6,-5],[4,6,-7,-4,5,8,-10,-3,4,-3,8,2,-3,9,4,4],[3,-5,-6,9,-2,-7,4,1,2,5,-10,-9,5,-4,5,8],[-10,10,3,9,-8,10,-8,4,-2,1,5,-7,-9,3,9,-4]],[[6,4,5,7,-10,9,-5,-2,-1,-1,5,1,6,-10,5,3],[7,-3,9,-8,-4,-10,10,-5,3,7,3,1,-2,-6,4,8],[-7,4,8,8,10,10,8,-9,3,-10,-4,10,4,2,-7,9],[-3,1,-6,-5,7,-6,-3,9,-3,-2,1,-4,8,-3,10,9]]], dtype = "int64")#candidate|8352|(13, 4, 16)|const|int64
bop_8353 = relay.subtract(var_8351.astype('int64'), relay.reshape(const_8352.astype('int64'), relay.shape_of(var_8351))) # shape=(13, 4, 16)
uop_8368 = relay.cos(const_8352.astype('float64')) # shape=(13, 4, 16)
func_4780_call = mod.get_global_var('func_4780')
func_4782_call = mutated_mod.get_global_var('func_4782')
call_8370 = relay.TupleGetItem(func_4780_call(), 0)
call_8371 = relay.TupleGetItem(func_4782_call(), 0)
var_8372 = relay.var("var_8372", dtype = "float64", shape = (13, 4, 16))#candidate|8372|(13, 4, 16)|var|float64
bop_8373 = relay.left_shift(uop_8368.astype('int8'), relay.reshape(var_8372.astype('int8'), relay.shape_of(uop_8368))) # shape=(13, 4, 16)
func_7859_call = mod.get_global_var('func_7859')
func_7863_call = mutated_mod.get_global_var('func_7863')
var_8377 = relay.var("var_8377", dtype = "int16", shape = (112,))#candidate|8377|(112,)|var|int16
call_8376 = relay.TupleGetItem(func_7859_call(relay.reshape(var_8377.astype('int16'), [56, 2]), relay.reshape(var_8377.astype('int16'), [56, 2]), ), 2)
call_8378 = relay.TupleGetItem(func_7863_call(relay.reshape(var_8377.astype('int16'), [56, 2]), relay.reshape(var_8377.astype('int16'), [56, 2]), ), 2)
uop_8382 = relay.log10(uop_8368.astype('float32')) # shape=(13, 4, 16)
uop_8385 = relay.atan(uop_8382.astype('float64')) # shape=(13, 4, 16)
output = relay.Tuple([bop_8353,call_8370,bop_8373,call_8376,var_8377,uop_8385,])
output2 = relay.Tuple([bop_8353,call_8371,bop_8373,call_8378,var_8377,uop_8385,])
func_8391 = relay.Function([var_8351,var_8372,var_8377,], output)
mod['func_8391'] = func_8391
mod = relay.transform.InferType()(mod)
var_8392 = relay.var("var_8392", dtype = "int64", shape = (13, 4, 16))#candidate|8392|(13, 4, 16)|var|int64
var_8393 = relay.var("var_8393", dtype = "float64", shape = (13, 4, 16))#candidate|8393|(13, 4, 16)|var|float64
var_8394 = relay.var("var_8394", dtype = "int16", shape = (112,))#candidate|8394|(112,)|var|int16
output = func_8391(var_8392,var_8393,var_8394,)
func_8395 = relay.Function([var_8392,var_8393,var_8394,], output)
mutated_mod['func_8395'] = func_8395
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5424_call = mod.get_global_var('func_5424')
func_5426_call = mutated_mod.get_global_var('func_5426')
call_8431 = relay.TupleGetItem(func_5424_call(), 2)
call_8432 = relay.TupleGetItem(func_5426_call(), 2)
output = relay.Tuple([call_8431,])
output2 = relay.Tuple([call_8432,])
func_8439 = relay.Function([], output)
mod['func_8439'] = func_8439
mod = relay.transform.InferType()(mod)
output = func_8439()
func_8440 = relay.Function([], output)
mutated_mod['func_8440'] = func_8440
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8455 = relay.var("var_8455", dtype = "uint16", shape = ())#candidate|8455|()|var|uint16
var_8456 = relay.var("var_8456", dtype = "uint16", shape = (13, 9, 7))#candidate|8456|(13, 9, 7)|var|uint16
bop_8457 = relay.bitwise_or(var_8455.astype('uint16'), var_8456.astype('uint16')) # shape=(13, 9, 7)
func_5366_call = mod.get_global_var('func_5366')
func_5368_call = mutated_mod.get_global_var('func_5368')
call_8460 = func_5366_call()
call_8461 = func_5366_call()
func_849_call = mod.get_global_var('func_849')
func_856_call = mutated_mod.get_global_var('func_856')
const_8465 = relay.const([5.055968,0.383781,-3.750158,-0.728438,9.258982,8.082469,-7.289808,6.913373,0.405528,-3.945438,7.796359,-3.429603,-0.247092,6.054618,-1.230765,-2.656323,0.531661,8.012182,5.387880,7.798944,4.508653,-4.516066,-8.551472,5.088343,-7.470473,-0.391388,-6.525180,-0.182391,-3.105089,-5.879126,1.343552,2.161153,-8.828624,-2.212473,-7.796031,-4.274712,-4.541039,2.250136,-2.117557,5.380050,-1.576135,4.539346,-0.218500,-5.794954,1.324421,4.288295,5.671745,4.570640,1.878533,4.052494,6.115462,7.202194,-2.724621,-2.315958,6.583481,-2.165778,-2.727778,-4.383749,2.888145,3.647763,1.982039,2.861959,7.425280,-0.983554,-9.918988,5.725730,6.726256,-3.094655,9.189009,1.006153,-2.249862,3.831010,0.446620,4.891686,-3.359598,5.691309,-7.996919,-4.390813,9.787849,-6.527480,-0.234789,0.428969,7.005315,-4.084652,-2.550309,4.327277,1.334785,0.649763,0.552434,2.576671,-0.117563,5.587584,-2.476914,-7.733373,8.038531,8.085304], dtype = "float32")#candidate|8465|(96,)|const|float32
var_8466 = relay.var("var_8466", dtype = "bool", shape = (225,))#candidate|8466|(225,)|var|bool
const_8467 = relay.const([1,-8,5,1,-10,-5,5,3,5,-2,9,4,9,8,-1,7,-3,10,-8,-10,-8,-1,10,1,-5,-6,4,-2,2,-6,9,7,-6,-7,-8,5,6,10,-10,-1,3,-9,9,-4,1,6,-3,1,-9,-6], dtype = "uint32")#candidate|8467|(50,)|const|uint32
const_8468 = relay.const([True,True,True,True,False,False,False,False,False,True,False,False,False,True,False,True,False,True,False,True,True,False,False,False,False,True,True,True,False,True,False,False,True,False,True,True,False,True,True,False,False,False,True,True,True,True,False,True,False,False,True,False,True,True,False,True,False,True,True,True,False,True,True,True,True,False,False,False,True,False,False,False,False,True,True,True,True,True,False,True,False,True,True,True,True,True,False,True,False,True,False,True,True,True,False,False,True,True,False,True,True,True,True,True,False,False,False,True,True,False,True,True,False,False,False,True,False,True,False,False,False,True,True,True,False,False,False,False,True,False,True,False,True,False,True,False,False,True,True,True,True,False,True,True,True,True,False,True,False,True,True,True,False,True,False,False,True,False,False,False,True,True,False,False,True,True,False,True,False,False,True,True,False,False,True,True,True,True,False,False,False,False,True,False,True,True,True,False,False,True,False,True,True,False,True,False,True,False,False,True,False,True,False,False,True,True,False,False,True,False,False,True,False,True,False,True,True,True,True,True,False,True,False,True,True,True,False,False,True,False,True,True,True,False,False,False,True,False,False,False,False,True,False,True,False,False,False,True,True,False,False,True,True,False,True,True,False,True,True,True,True,True,True,False,True,True,False,False,True,False,True,True,True,True,False,False,True,True,True,False,True,False,True,False,False,False,True,False,True,True,False,False,False,True,False,True,False,False,True,True,True,False,False,False,True,True,False,False,False,False,False,True,False,False,True,False,False,True,True,False,False,True,False,False,False,True,True,False,True,False,True,False,True,True,True,False,False,True,True,False,True,True,True,True,True,True,False,False,False,True,False,False,False,False,False,False,True,True,False,True,True,True,True,False,False,False,True,True,False,False,True,True,True,True,True,True,False,True,True,False,False,True,False,False,True,False,False,True,True,False,False,False,True,True,True,True,False,False,False,False,False,False,True,True,True,False,False,True,True,True,True,True,False,True,True,False,True,True,True,False,True,True,False,False,False,True,False,False,True,False,False,True,False,False,True,True,False,True,False,False,True,True,True,True,False,True,True,True,False,False,True,False,True,False,False,False,True,False,False,True,True,True,False,True,True,True,True,True,True,True,True,False,True,True,True,True,False,True,True,False,True,False,False,True,False,True,True,False,True,True,True,False,False,True,False,True,True,True,True,False,False,False,False,True,True,True,True,True,False,False,False,False,False,False,True,True,True,False,True,True,True,False,True,False,True,True,True,False,False,False,False,True,True,False,False,False,False,True,False,False,True,False,False,False,False,True,True,False,True,False,True,True,False,False,True,True,False,False,False,False,True,False,True,False,True,False,False,True,True,False,True,True,False,False,True,True,True,False,True,True,False,False,False,False,False,True,True,False], dtype = "bool")#candidate|8468|(588,)|const|bool
call_8464 = relay.TupleGetItem(func_849_call(relay.reshape(const_8465.astype('float32'), [4, 3, 8]), relay.reshape(const_8465.astype('float32'), [4, 3, 8]), relay.reshape(var_8455.astype('bool'), []), relay.reshape(var_8466.astype('bool'), [225,]), relay.reshape(const_8467.astype('uint32'), [50,]), relay.reshape(const_8468.astype('bool'), [14, 7, 6]), ), 8)
call_8469 = relay.TupleGetItem(func_856_call(relay.reshape(const_8465.astype('float32'), [4, 3, 8]), relay.reshape(const_8465.astype('float32'), [4, 3, 8]), relay.reshape(var_8455.astype('bool'), []), relay.reshape(var_8466.astype('bool'), [225,]), relay.reshape(const_8467.astype('uint32'), [50,]), relay.reshape(const_8468.astype('bool'), [14, 7, 6]), ), 8)
var_8473 = relay.var("var_8473", dtype = "uint16", shape = (13, 9, 7))#candidate|8473|(13, 9, 7)|var|uint16
bop_8474 = relay.logical_and(var_8456.astype('bool'), relay.reshape(var_8473.astype('bool'), relay.shape_of(var_8456))) # shape=(13, 9, 7)
output = relay.Tuple([bop_8457,call_8460,call_8464,const_8465,var_8466,const_8467,const_8468,bop_8474,])
output2 = relay.Tuple([bop_8457,call_8461,call_8469,const_8465,var_8466,const_8467,const_8468,bop_8474,])
func_8484 = relay.Function([var_8455,var_8456,var_8466,var_8473,], output)
mod['func_8484'] = func_8484
mod = relay.transform.InferType()(mod)
var_8485 = relay.var("var_8485", dtype = "uint16", shape = ())#candidate|8485|()|var|uint16
var_8486 = relay.var("var_8486", dtype = "uint16", shape = (13, 9, 7))#candidate|8486|(13, 9, 7)|var|uint16
var_8487 = relay.var("var_8487", dtype = "bool", shape = (225,))#candidate|8487|(225,)|var|bool
var_8488 = relay.var("var_8488", dtype = "uint16", shape = (13, 9, 7))#candidate|8488|(13, 9, 7)|var|uint16
output = func_8484(var_8485,var_8486,var_8487,var_8488,)
func_8489 = relay.Function([var_8485,var_8486,var_8487,var_8488,], output)
mutated_mod['func_8489'] = func_8489
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4521_call = mod.get_global_var('func_4521')
func_4522_call = mutated_mod.get_global_var('func_4522')
call_8523 = relay.TupleGetItem(func_4521_call(), 0)
call_8524 = relay.TupleGetItem(func_4522_call(), 0)
func_3905_call = mod.get_global_var('func_3905')
func_3906_call = mutated_mod.get_global_var('func_3906')
call_8529 = func_3905_call()
call_8530 = func_3905_call()
func_5366_call = mod.get_global_var('func_5366')
func_5368_call = mutated_mod.get_global_var('func_5368')
call_8552 = func_5366_call()
call_8553 = func_5366_call()
output = relay.Tuple([call_8523,call_8529,call_8552,])
output2 = relay.Tuple([call_8524,call_8530,call_8553,])
func_8574 = relay.Function([], output)
mod['func_8574'] = func_8574
mod = relay.transform.InferType()(mod)
mutated_mod['func_8574'] = func_8574
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8574_call = mutated_mod.get_global_var('func_8574')
call_8575 = func_8574_call()
output = call_8575
func_8576 = relay.Function([], output)
mutated_mod['func_8576'] = func_8576
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8331_call = mod.get_global_var('func_8331')
func_8332_call = mutated_mod.get_global_var('func_8332')
call_8661 = func_8331_call()
call_8662 = func_8331_call()
func_8331_call = mod.get_global_var('func_8331')
func_8332_call = mutated_mod.get_global_var('func_8332')
call_8688 = func_8331_call()
call_8689 = func_8331_call()
func_4225_call = mod.get_global_var('func_4225')
func_4227_call = mutated_mod.get_global_var('func_4227')
call_8700 = relay.TupleGetItem(func_4225_call(), 0)
call_8701 = relay.TupleGetItem(func_4227_call(), 0)
func_300_call = mod.get_global_var('func_300')
func_303_call = mutated_mod.get_global_var('func_303')
const_8704 = relay.const(True, dtype = "bool")#candidate|8704|()|const|bool
call_8703 = relay.TupleGetItem(func_300_call(relay.reshape(const_8704.astype('bool'), [])), 0)
call_8705 = relay.TupleGetItem(func_303_call(relay.reshape(const_8704.astype('bool'), [])), 0)
output = relay.Tuple([call_8661,call_8688,call_8700,call_8703,const_8704,])
output2 = relay.Tuple([call_8662,call_8689,call_8701,call_8705,const_8704,])
func_8724 = relay.Function([], output)
mod['func_8724'] = func_8724
mod = relay.transform.InferType()(mod)
output = func_8724()
func_8725 = relay.Function([], output)
mutated_mod['func_8725'] = func_8725
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8743 = relay.var("var_8743", dtype = "float64", shape = (2, 1, 1))#candidate|8743|(2, 1, 1)|var|float64
uop_8744 = relay.log2(var_8743.astype('float64')) # shape=(2, 1, 1)
output = uop_8744
output2 = uop_8744
func_8762 = relay.Function([var_8743,], output)
mod['func_8762'] = func_8762
mod = relay.transform.InferType()(mod)
var_8763 = relay.var("var_8763", dtype = "float64", shape = (2, 1, 1))#candidate|8763|(2, 1, 1)|var|float64
output = func_8762(var_8763)
func_8764 = relay.Function([var_8763], output)
mutated_mod['func_8764'] = func_8764
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4521_call = mod.get_global_var('func_4521')
func_4522_call = mutated_mod.get_global_var('func_4522')
call_8807 = relay.TupleGetItem(func_4521_call(), 1)
call_8808 = relay.TupleGetItem(func_4522_call(), 1)
output = call_8807
output2 = call_8808
func_8816 = relay.Function([], output)
mod['func_8816'] = func_8816
mod = relay.transform.InferType()(mod)
mutated_mod['func_8816'] = func_8816
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8816_call = mutated_mod.get_global_var('func_8816')
call_8817 = func_8816_call()
output = call_8817
func_8818 = relay.Function([], output)
mutated_mod['func_8818'] = func_8818
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8724_call = mod.get_global_var('func_8724')
func_8725_call = mutated_mod.get_global_var('func_8725')
call_8891 = relay.TupleGetItem(func_8724_call(), 1)
call_8892 = relay.TupleGetItem(func_8725_call(), 1)
output = relay.Tuple([call_8891,])
output2 = relay.Tuple([call_8892,])
func_8894 = relay.Function([], output)
mod['func_8894'] = func_8894
mod = relay.transform.InferType()(mod)
output = func_8894()
func_8895 = relay.Function([], output)
mutated_mod['func_8895'] = func_8895
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8894_call = mod.get_global_var('func_8894')
func_8895_call = mutated_mod.get_global_var('func_8895')
call_8915 = relay.TupleGetItem(func_8894_call(), 0)
call_8916 = relay.TupleGetItem(func_8895_call(), 0)
output = call_8915
output2 = call_8916
func_8918 = relay.Function([], output)
mod['func_8918'] = func_8918
mod = relay.transform.InferType()(mod)
output = func_8918()
func_8919 = relay.Function([], output)
mutated_mod['func_8919'] = func_8919
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8950 = relay.var("var_8950", dtype = "bool", shape = (8, 9, 1))#candidate|8950|(8, 9, 1)|var|bool
var_8951 = relay.var("var_8951", dtype = "bool", shape = (8, 9, 16))#candidate|8951|(8, 9, 16)|var|bool
bop_8952 = relay.logical_or(var_8950.astype('bool'), var_8951.astype('bool')) # shape=(8, 9, 16)
func_5506_call = mod.get_global_var('func_5506')
func_5508_call = mutated_mod.get_global_var('func_5508')
call_8977 = relay.TupleGetItem(func_5506_call(), 1)
call_8978 = relay.TupleGetItem(func_5508_call(), 1)
func_4558_call = mod.get_global_var('func_4558')
func_4560_call = mutated_mod.get_global_var('func_4560')
call_8996 = func_4558_call()
call_8997 = func_4558_call()
bop_8999 = relay.less(var_8950.astype('bool'), var_8951.astype('bool')) # shape=(8, 9, 16)
output = relay.Tuple([bop_8952,call_8977,call_8996,bop_8999,])
output2 = relay.Tuple([bop_8952,call_8978,call_8997,bop_8999,])
func_9005 = relay.Function([var_8950,var_8951,], output)
mod['func_9005'] = func_9005
mod = relay.transform.InferType()(mod)
var_9006 = relay.var("var_9006", dtype = "bool", shape = (8, 9, 1))#candidate|9006|(8, 9, 1)|var|bool
var_9007 = relay.var("var_9007", dtype = "bool", shape = (8, 9, 16))#candidate|9007|(8, 9, 16)|var|bool
output = func_9005(var_9006,var_9007,)
func_9008 = relay.Function([var_9006,var_9007,], output)
mutated_mod['func_9008'] = func_9008
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4722_call = mod.get_global_var('func_4722')
func_4723_call = mutated_mod.get_global_var('func_4723')
call_9062 = relay.TupleGetItem(func_4722_call(), 0)
call_9063 = relay.TupleGetItem(func_4723_call(), 0)
func_6472_call = mod.get_global_var('func_6472')
func_6474_call = mutated_mod.get_global_var('func_6474')
const_9069 = relay.const([[-10],[-9],[5],[-8],[3],[-5],[-7],[2],[10],[2],[-6],[8],[-2],[-3],[5],[-5],[6],[-5],[-3],[-1],[-6],[-9],[-1],[-7],[-6],[-6],[-1],[-6],[-1],[1],[6],[-10],[-4],[-7],[-10],[1],[-7],[9],[3],[2],[2],[-4],[4],[9],[10],[-1],[7],[-1],[8],[6],[-6],[-4],[-9],[-2],[8],[4],[2],[6],[-7],[-3],[-4],[-5],[8],[10],[4],[6],[4],[7],[-4],[8],[5],[-3],[-9],[2],[3],[-6],[2],[7],[-9],[-7],[-4],[-7],[4],[4],[2],[-9],[5],[3],[2],[-1],[-3],[-3],[-8],[4],[-9],[2],[-4],[2],[10],[-4],[-1],[9],[-7],[-1],[10],[-8],[-8],[-7],[-1],[-4],[1],[-4],[3],[-1],[-3],[7],[-9],[1],[1],[-7],[-3],[-5],[5],[-7],[-2],[-7],[-7],[6],[-6],[-2],[3],[4],[-8],[-10],[-8],[-1],[3],[1],[-7],[-4],[-7],[1],[-9],[-3],[5],[5],[-9],[-2],[5],[-5],[8],[-3],[-1],[8],[-3],[4],[-1],[-6],[-2],[-7],[-6],[-7],[-1],[-1],[8],[1],[-3],[8],[9],[1],[-6],[1],[-10],[2],[-6],[2],[-1],[-9],[7],[-3],[10],[-2],[8],[-7],[6],[8],[5],[-1],[-8],[8],[2],[-10],[-9],[9],[10],[3],[-6],[3],[5],[-3],[-9],[2],[4],[-8],[6],[8],[8],[-5],[6],[-4],[-8],[8],[-10],[-1],[4],[5],[-7],[-7],[10],[-5],[3],[-8],[-1],[9],[7],[-8],[10],[10],[-1],[-6],[-5],[8],[10],[4],[3],[8],[-3],[9],[9],[3],[-3],[2],[9],[5],[5],[4],[-4],[3],[-10],[-6],[6],[-2],[-10],[3],[1],[7],[9],[9],[-5],[7],[-10],[9],[5],[-10],[9],[-9],[9],[4],[-2],[-3],[4],[-1],[1],[-10],[-8],[6],[10],[-2],[7],[10],[-5],[1],[-10],[-7],[3],[-7],[10],[-10],[10],[9],[9],[-4],[1],[1],[-7],[6],[-10],[7],[-3],[2],[2],[2],[1],[-5],[6],[-9],[-9],[3],[10],[-10],[7],[-8],[-4],[-6],[-9],[4],[2],[-5],[2],[4],[-4],[-2],[-7],[-5],[-2],[-3],[-2],[7],[5],[-4],[6],[8],[-3],[-2],[3],[-2],[10],[-1],[10],[-3],[10],[3],[-6],[7],[-6],[6],[8],[1],[-6],[-8],[-9],[-7],[-4],[-6],[-6],[-9],[5],[-10],[4],[2],[10],[-3],[9],[2],[7],[6],[10],[-4],[4],[3],[9],[8],[-5],[4],[-10],[3],[-2],[10],[10],[-9],[-2],[2],[-8],[8],[-6],[-4],[2],[6],[-2],[1],[5],[-2],[8],[-2],[-4],[7],[6],[9],[8],[8],[8],[-7],[-5],[10],[-3],[9],[-4],[-9],[-3],[-3],[2],[4],[-1],[-3],[-10],[-1],[4],[1],[-2],[7],[3],[-5],[9],[9],[3],[-2],[4],[-2],[-6],[-4],[-8],[3],[4],[1],[6],[-1],[-6],[-3],[-10],[-10],[4],[7],[-5],[-3],[-6],[5],[3],[-5],[-3],[-4],[6],[7],[-4],[8],[5],[-7],[7],[9],[5],[-3],[10],[-4],[-10],[-3],[-7],[4],[-4],[5],[3],[2],[-1],[-9],[2],[-2],[-9],[-7],[-5],[-1],[4],[-1],[-10],[-4],[8],[-4],[5],[1],[4],[-4],[-7],[5],[-1],[4],[-7],[-2],[10],[4],[10],[6],[-9],[1],[6],[-8],[1],[1],[8],[3],[-10],[5],[1],[-10],[3],[-10],[-2],[-3],[7],[-3],[-5],[7],[4],[-5],[4],[2],[-4],[-3],[6],[-7],[-5],[-4],[-3],[8],[-10],[-7],[3],[-4],[-4],[7],[-8],[3],[-8],[10],[-10],[-5],[-3],[-4],[7],[-8],[-2],[-5],[-1],[-1],[-9],[-2],[-9],[-2],[3],[-1],[8],[-2],[6],[-7],[7],[-1],[2],[-3],[2],[-9],[-2],[9],[-10],[-8],[-10],[8],[4],[8],[5],[10],[-1],[-10],[-6],[10],[-8],[-8],[-2],[4],[7],[-4],[9],[-4],[-3],[3],[-8],[-1],[-6],[3],[-5],[10],[4],[4],[7],[7],[-9],[1],[-3],[3],[7],[-6],[-8],[3],[-8],[-4],[1],[-8],[3],[8],[-1],[-4],[-6],[-10],[-9],[-6],[8],[-9],[-9],[-10],[1],[1],[9],[-5],[-1],[-2],[8],[1],[-8],[6],[4],[4],[-6],[-8],[-7],[1],[2],[8],[-9],[-6],[5],[-1],[4],[10],[4],[1],[-8],[8],[10],[-8],[-4],[-5],[-10],[10],[5],[10],[-5],[-5],[-4],[3],[1],[-6],[1],[-4],[9],[7],[10],[10]], dtype = "int16")#candidate|9069|(672, 1)|const|int16
call_9068 = relay.TupleGetItem(func_6472_call(relay.reshape(const_9069.astype('int16'), [2, 336])), 0)
call_9070 = relay.TupleGetItem(func_6474_call(relay.reshape(const_9069.astype('int16'), [2, 336])), 0)
func_3479_call = mod.get_global_var('func_3479')
func_3480_call = mutated_mod.get_global_var('func_3480')
call_9087 = func_3479_call()
call_9088 = func_3479_call()
output = relay.Tuple([call_9062,call_9068,const_9069,call_9087,])
output2 = relay.Tuple([call_9063,call_9070,const_9069,call_9088,])
func_9094 = relay.Function([], output)
mod['func_9094'] = func_9094
mod = relay.transform.InferType()(mod)
mutated_mod['func_9094'] = func_9094
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9094_call = mutated_mod.get_global_var('func_9094')
call_9095 = func_9094_call()
output = call_9095
func_9096 = relay.Function([], output)
mutated_mod['func_9096'] = func_9096
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5545_call = mod.get_global_var('func_5545')
func_5546_call = mutated_mod.get_global_var('func_5546')
call_9099 = func_5545_call()
call_9100 = func_5545_call()
uop_9104 = relay.atanh(call_9099.astype('float64')) # shape=(2, 336)
uop_9106 = relay.atanh(call_9100.astype('float64')) # shape=(2, 336)
output = uop_9104
output2 = uop_9106
func_9109 = relay.Function([], output)
mod['func_9109'] = func_9109
mod = relay.transform.InferType()(mod)
output = func_9109()
func_9110 = relay.Function([], output)
mutated_mod['func_9110'] = func_9110
mutated_mod = relay.transform.InferType()(mutated_mod)
const_9160 = relay.const(10, dtype = "int64")#candidate|9160|()|const|int64
var_9161 = relay.var("var_9161", dtype = "int64", shape = (7, 4, 8))#candidate|9161|(7, 4, 8)|var|int64
bop_9162 = relay.subtract(const_9160.astype('int64'), var_9161.astype('int64')) # shape=(7, 4, 8)
output = relay.Tuple([bop_9162,])
output2 = relay.Tuple([bop_9162,])
func_9169 = relay.Function([var_9161,], output)
mod['func_9169'] = func_9169
mod = relay.transform.InferType()(mod)
var_9170 = relay.var("var_9170", dtype = "int64", shape = (7, 4, 8))#candidate|9170|(7, 4, 8)|var|int64
output = func_9169(var_9170)
func_9171 = relay.Function([var_9170], output)
mutated_mod['func_9171'] = func_9171
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4639_call = mod.get_global_var('func_4639')
func_4641_call = mutated_mod.get_global_var('func_4641')
call_9205 = relay.TupleGetItem(func_4639_call(), 0)
call_9206 = relay.TupleGetItem(func_4641_call(), 0)
var_9209 = relay.var("var_9209", dtype = "bool", shape = (16, 5, 7))#candidate|9209|(16, 5, 7)|var|bool
bop_9210 = relay.subtract(call_9205.astype('int32'), relay.reshape(var_9209.astype('int32'), relay.shape_of(call_9205))) # shape=(16, 5, 7)
bop_9213 = relay.subtract(call_9206.astype('int32'), relay.reshape(var_9209.astype('int32'), relay.shape_of(call_9206))) # shape=(16, 5, 7)
func_6216_call = mod.get_global_var('func_6216')
func_6218_call = mutated_mod.get_global_var('func_6218')
call_9229 = relay.TupleGetItem(func_6216_call(), 0)
call_9230 = relay.TupleGetItem(func_6218_call(), 0)
output = relay.Tuple([bop_9210,call_9229,])
output2 = relay.Tuple([bop_9213,call_9230,])
func_9237 = relay.Function([var_9209,], output)
mod['func_9237'] = func_9237
mod = relay.transform.InferType()(mod)
mutated_mod['func_9237'] = func_9237
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9238 = relay.var("var_9238", dtype = "bool", shape = (16, 5, 7))#candidate|9238|(16, 5, 7)|var|bool
func_9237_call = mutated_mod.get_global_var('func_9237')
call_9239 = func_9237_call(var_9238)
output = call_9239
func_9240 = relay.Function([var_9238], output)
mutated_mod['func_9240'] = func_9240
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8816_call = mod.get_global_var('func_8816')
func_8818_call = mutated_mod.get_global_var('func_8818')
call_9255 = func_8816_call()
call_9256 = func_8816_call()
func_5545_call = mod.get_global_var('func_5545')
func_5546_call = mutated_mod.get_global_var('func_5546')
call_9293 = func_5545_call()
call_9294 = func_5545_call()
output = relay.Tuple([call_9255,call_9293,])
output2 = relay.Tuple([call_9256,call_9294,])
func_9299 = relay.Function([], output)
mod['func_9299'] = func_9299
mod = relay.transform.InferType()(mod)
mutated_mod['func_9299'] = func_9299
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9299_call = mutated_mod.get_global_var('func_9299')
call_9300 = func_9299_call()
output = call_9300
func_9301 = relay.Function([], output)
mutated_mod['func_9301'] = func_9301
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9438 = relay.var("var_9438", dtype = "int32", shape = (13, 1, 2))#candidate|9438|(13, 1, 2)|var|int32
var_9439 = relay.var("var_9439", dtype = "int32", shape = (13, 15, 2))#candidate|9439|(13, 15, 2)|var|int32
bop_9440 = relay.bitwise_and(var_9438.astype('int32'), var_9439.astype('int32')) # shape=(13, 15, 2)
func_4225_call = mod.get_global_var('func_4225')
func_4227_call = mutated_mod.get_global_var('func_4227')
call_9443 = relay.TupleGetItem(func_4225_call(), 0)
call_9444 = relay.TupleGetItem(func_4227_call(), 0)
output = relay.Tuple([bop_9440,call_9443,])
output2 = relay.Tuple([bop_9440,call_9444,])
func_9452 = relay.Function([var_9438,var_9439,], output)
mod['func_9452'] = func_9452
mod = relay.transform.InferType()(mod)
mutated_mod['func_9452'] = func_9452
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9452_call = mutated_mod.get_global_var('func_9452')
var_9454 = relay.var("var_9454", dtype = "int32", shape = (13, 1, 2))#candidate|9454|(13, 1, 2)|var|int32
var_9455 = relay.var("var_9455", dtype = "int32", shape = (13, 15, 2))#candidate|9455|(13, 15, 2)|var|int32
call_9453 = func_9452_call(var_9454,var_9455,)
output = call_9453
func_9456 = relay.Function([var_9454,var_9455,], output)
mutated_mod['func_9456'] = func_9456
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3712_call = mod.get_global_var('func_3712')
func_3713_call = mutated_mod.get_global_var('func_3713')
call_9490 = func_3712_call()
call_9491 = func_3712_call()
var_9501 = relay.var("var_9501", dtype = "int16", shape = (2, 336))#candidate|9501|(2, 336)|var|int16
bop_9502 = relay.floor_divide(call_9490.astype('float32'), relay.reshape(var_9501.astype('float32'), relay.shape_of(call_9490))) # shape=(2, 336)
bop_9505 = relay.floor_divide(call_9491.astype('float32'), relay.reshape(var_9501.astype('float32'), relay.shape_of(call_9491))) # shape=(2, 336)
output = relay.Tuple([bop_9502,])
output2 = relay.Tuple([bop_9505,])
F = relay.Function([var_9501,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_9501,], output2)
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
