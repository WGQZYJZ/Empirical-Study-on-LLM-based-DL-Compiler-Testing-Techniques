import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_1014 = relay.var("var_1014", dtype = "uint8", shape = (6, 12, 6))#candidate|1014|(6, 12, 6)|var|uint8
var_1015 = relay.var("var_1015", dtype = "uint8", shape = (6, 12, 6))#candidate|1015|(6, 12, 6)|var|uint8
bop_1016 = relay.less_equal(var_1014.astype('bool'), relay.reshape(var_1015.astype('bool'), relay.shape_of(var_1014))) # shape=(6, 12, 6)
output = bop_1016
output2 = bop_1016
func_1019 = relay.Function([var_1014,var_1015,], output)
mod['func_1019'] = func_1019
mod = relay.transform.InferType()(mod)
mutated_mod['func_1019'] = func_1019
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1019_call = mutated_mod.get_global_var('func_1019')
var_1021 = relay.var("var_1021", dtype = "uint8", shape = (6, 12, 6))#candidate|1021|(6, 12, 6)|var|uint8
var_1022 = relay.var("var_1022", dtype = "uint8", shape = (6, 12, 6))#candidate|1022|(6, 12, 6)|var|uint8
call_1020 = func_1019_call(var_1021,var_1022,)
output = call_1020
func_1023 = relay.Function([var_1021,var_1022,], output)
mutated_mod['func_1023'] = func_1023
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1514 = relay.var("var_1514", dtype = "float32", shape = (1, 3, 3))#candidate|1514|(1, 3, 3)|var|float32
uop_1515 = relay.atan(var_1514.astype('float32')) # shape=(1, 3, 3)
func_1019_call = mod.get_global_var('func_1019')
func_1023_call = mutated_mod.get_global_var('func_1023')
var_1518 = relay.var("var_1518", dtype = "uint8", shape = (216, 2))#candidate|1518|(216, 2)|var|uint8
call_1517 = func_1019_call(relay.reshape(var_1518.astype('uint8'), [6, 12, 6]), relay.reshape(var_1518.astype('uint8'), [6, 12, 6]), )
call_1519 = func_1019_call(relay.reshape(var_1518.astype('uint8'), [6, 12, 6]), relay.reshape(var_1518.astype('uint8'), [6, 12, 6]), )
uop_1520 = relay.cosh(uop_1515.astype('float32')) # shape=(1, 3, 3)
uop_1528 = relay.asinh(uop_1515.astype('float64')) # shape=(1, 3, 3)
output = relay.Tuple([call_1517,var_1518,uop_1520,uop_1528,])
output2 = relay.Tuple([call_1519,var_1518,uop_1520,uop_1528,])
func_1531 = relay.Function([var_1514,var_1518,], output)
mod['func_1531'] = func_1531
mod = relay.transform.InferType()(mod)
var_1532 = relay.var("var_1532", dtype = "float32", shape = (1, 3, 3))#candidate|1532|(1, 3, 3)|var|float32
var_1533 = relay.var("var_1533", dtype = "uint8", shape = (216, 2))#candidate|1533|(216, 2)|var|uint8
output = func_1531(var_1532,var_1533,)
func_1534 = relay.Function([var_1532,var_1533,], output)
mutated_mod['func_1534'] = func_1534
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1632 = relay.var("var_1632", dtype = "uint64", shape = (12, 1, 13))#candidate|1632|(12, 1, 13)|var|uint64
var_1633 = relay.var("var_1633", dtype = "uint64", shape = (12, 11, 13))#candidate|1633|(12, 11, 13)|var|uint64
bop_1634 = relay.maximum(var_1632.astype('uint64'), var_1633.astype('uint64')) # shape=(12, 11, 13)
func_1531_call = mod.get_global_var('func_1531')
func_1534_call = mutated_mod.get_global_var('func_1534')
const_1638 = relay.const([-7.040355,-3.481152,3.616969,0.743187,6.202328,9.906036,-8.897000,3.959518,2.007715], dtype = "float32")#candidate|1638|(9,)|const|float32
const_1639 = relay.const([1,-9,-5,-7,9,10,-6,5,-3,9,1,3,9,-9,8,-3,5,7,3,1,-2,6,-1,1,7,-1,-1,-10,-6,5,4,7,10,-1,8,4,5,7,3,2,-9,-8,-9,1,5,3,3,-3,4,5,6,-3,9,8,9,2,3,8,-6,9,-2,5,2,6,9,-1,1,9,5,4,7,2,5,2,-7,-5,3,4,-7,5,-4,-5,10,8,9,-9,-7,-6,3,6,-9,10,-10,-7,-9,-4,-9,-9,-1,4,9,6,-8,-10,10,-2,-6,1,9,2,-10,-10,-5,10,5,8,9,10,8,-10,-6,7,5,8,8,1,-8,9,-9,9,-2,8,3,-1,-9,-1,-1,5,-6,1,2,-2,-4,-4,-9,-9,-2,-4,-6,-7,-4,-8,-7,-3,7,-9,-8,1,-3,7,10,4,-4,8,-3,-4,7,2,-8,-9,8,4,-10,-8,-10,6,2,3,-10,7,-9,-2,5,-10,-10,-8,6,6,8,10,10,9,10,7,2,5,7,6,1,4,5,-10,7,9,-10,5,-9,-2,-6,-10,5,10,1,3,-1,5,-3,9,1,-7,-10,-10,9,-9,5,3,-3,3,10,9,-4,-9,7,9,9,10,-10,-8,6,-4,-7,10,-2,5,8,-3,-8,9,2,5,6,1,-8,5,-8,-3,-7,-6,-6,3,5,-6,10,-10,7,-4,-1,-7,3,10,-2,-8,-6,8,-5,7,6,-5,-3,9,-8,-1,7,7,1,-3,10,9,-6,-7,-9,1,10,-2,-10,-2,-3,9,-2,-1,-2,5,-6,8,-3,-10,-1,-8,8,-5,2,-7,2,-6,-2,7,-3,-8,9,10,-2,6,3,8,5,-10,-3,-3,-6,-9,-8,-4,1,10,9,1,2,9,-3,-9,-2,-7,-9,-2,-3,-3,9,2,1,-9,-1,6,-10,-9,5,3,-8,-4,3,1,-7,7,-2,-8,-8,-7,-9,-2,-9,-4,-10,2,9,6,2,-8,-2,6,1,-10,1,9,10,1,-4,-6,3,-4,-5,-4,8,7,6,-3,-5,9,-10,-8,-10,2,5,10,-7,10,-5,-9,8,-2,-9,-3,-7,2,1,-10,8,-6,-1,9,-3,1,5,2,6,-10,-8,-9,5,4,1,6,-7,2], dtype = "uint8")#candidate|1639|(432,)|const|uint8
call_1637 = relay.TupleGetItem(func_1531_call(relay.reshape(const_1638.astype('float32'), [1, 3, 3]), relay.reshape(const_1639.astype('uint8'), [216, 2]), ), 0)
call_1640 = relay.TupleGetItem(func_1534_call(relay.reshape(const_1638.astype('float32'), [1, 3, 3]), relay.reshape(const_1639.astype('uint8'), [216, 2]), ), 0)
func_1531_call = mod.get_global_var('func_1531')
func_1534_call = mutated_mod.get_global_var('func_1534')
call_1648 = relay.TupleGetItem(func_1531_call(relay.reshape(const_1638.astype('float32'), [1, 3, 3]), relay.reshape(const_1639.astype('uint8'), [216, 2]), ), 2)
call_1649 = relay.TupleGetItem(func_1534_call(relay.reshape(const_1638.astype('float32'), [1, 3, 3]), relay.reshape(const_1639.astype('uint8'), [216, 2]), ), 2)
output = relay.Tuple([bop_1634,call_1637,const_1638,const_1639,call_1648,])
output2 = relay.Tuple([bop_1634,call_1640,const_1638,const_1639,call_1649,])
func_1658 = relay.Function([var_1632,var_1633,], output)
mod['func_1658'] = func_1658
mod = relay.transform.InferType()(mod)
var_1659 = relay.var("var_1659", dtype = "uint64", shape = (12, 1, 13))#candidate|1659|(12, 1, 13)|var|uint64
var_1660 = relay.var("var_1660", dtype = "uint64", shape = (12, 11, 13))#candidate|1660|(12, 11, 13)|var|uint64
output = func_1658(var_1659,var_1660,)
func_1661 = relay.Function([var_1659,var_1660,], output)
mutated_mod['func_1661'] = func_1661
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2637 = relay.var("var_2637", dtype = "int8", shape = (15, 5, 14))#candidate|2637|(15, 5, 14)|var|int8
var_2638 = relay.var("var_2638", dtype = "int8", shape = (15, 5, 14))#candidate|2638|(15, 5, 14)|var|int8
bop_2639 = relay.right_shift(var_2637.astype('int8'), relay.reshape(var_2638.astype('int8'), relay.shape_of(var_2637))) # shape=(15, 5, 14)
var_2642 = relay.var("var_2642", dtype = "int8", shape = (15, 5, 14))#candidate|2642|(15, 5, 14)|var|int8
bop_2643 = relay.power(bop_2639.astype('float32'), relay.reshape(var_2642.astype('float32'), relay.shape_of(bop_2639))) # shape=(15, 5, 14)
func_1531_call = mod.get_global_var('func_1531')
func_1534_call = mutated_mod.get_global_var('func_1534')
const_2649 = relay.const([-2.302428,6.553450,8.527858,3.469683,0.126397,4.206034,-9.426568,1.844105,-3.669407], dtype = "float32")#candidate|2649|(9,)|const|float32
var_2650 = relay.var("var_2650", dtype = "uint8", shape = (432,))#candidate|2650|(432,)|var|uint8
call_2648 = relay.TupleGetItem(func_1531_call(relay.reshape(const_2649.astype('float32'), [1, 3, 3]), relay.reshape(var_2650.astype('uint8'), [216, 2]), ), 0)
call_2651 = relay.TupleGetItem(func_1534_call(relay.reshape(const_2649.astype('float32'), [1, 3, 3]), relay.reshape(var_2650.astype('uint8'), [216, 2]), ), 0)
func_1019_call = mod.get_global_var('func_1019')
func_1023_call = mutated_mod.get_global_var('func_1023')
call_2653 = func_1019_call(relay.reshape(call_2648.astype('uint8'), [6, 12, 6]), relay.reshape(var_2650.astype('uint8'), [6, 12, 6]), )
call_2654 = func_1019_call(relay.reshape(call_2648.astype('uint8'), [6, 12, 6]), relay.reshape(var_2650.astype('uint8'), [6, 12, 6]), )
output = relay.Tuple([bop_2643,call_2648,const_2649,var_2650,call_2653,])
output2 = relay.Tuple([bop_2643,call_2651,const_2649,var_2650,call_2654,])
func_2677 = relay.Function([var_2637,var_2638,var_2642,var_2650,], output)
mod['func_2677'] = func_2677
mod = relay.transform.InferType()(mod)
var_2678 = relay.var("var_2678", dtype = "int8", shape = (15, 5, 14))#candidate|2678|(15, 5, 14)|var|int8
var_2679 = relay.var("var_2679", dtype = "int8", shape = (15, 5, 14))#candidate|2679|(15, 5, 14)|var|int8
var_2680 = relay.var("var_2680", dtype = "int8", shape = (15, 5, 14))#candidate|2680|(15, 5, 14)|var|int8
var_2681 = relay.var("var_2681", dtype = "uint8", shape = (432,))#candidate|2681|(432,)|var|uint8
output = func_2677(var_2678,var_2679,var_2680,var_2681,)
func_2682 = relay.Function([var_2678,var_2679,var_2680,var_2681,], output)
mutated_mod['func_2682'] = func_2682
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2712 = relay.var("var_2712", dtype = "uint16", shape = ())#candidate|2712|()|var|uint16
var_2713 = relay.var("var_2713", dtype = "uint16", shape = (12, 6, 12))#candidate|2713|(12, 6, 12)|var|uint16
bop_2714 = relay.multiply(var_2712.astype('uint16'), var_2713.astype('uint16')) # shape=(12, 6, 12)
output = bop_2714
output2 = bop_2714
func_2721 = relay.Function([var_2712,var_2713,], output)
mod['func_2721'] = func_2721
mod = relay.transform.InferType()(mod)
mutated_mod['func_2721'] = func_2721
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2721_call = mutated_mod.get_global_var('func_2721')
var_2723 = relay.var("var_2723", dtype = "uint16", shape = ())#candidate|2723|()|var|uint16
var_2724 = relay.var("var_2724", dtype = "uint16", shape = (12, 6, 12))#candidate|2724|(12, 6, 12)|var|uint16
call_2722 = func_2721_call(var_2723,var_2724,)
output = call_2722
func_2725 = relay.Function([var_2723,var_2724,], output)
mutated_mod['func_2725'] = func_2725
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2822 = relay.var("var_2822", dtype = "uint32", shape = (5, 3, 16))#candidate|2822|(5, 3, 16)|var|uint32
var_2823 = relay.var("var_2823", dtype = "uint32", shape = (5, 3, 16))#candidate|2823|(5, 3, 16)|var|uint32
bop_2824 = relay.minimum(var_2822.astype('uint32'), relay.reshape(var_2823.astype('uint32'), relay.shape_of(var_2822))) # shape=(5, 3, 16)
output = bop_2824
output2 = bop_2824
func_2836 = relay.Function([var_2822,var_2823,], output)
mod['func_2836'] = func_2836
mod = relay.transform.InferType()(mod)
var_2837 = relay.var("var_2837", dtype = "uint32", shape = (5, 3, 16))#candidate|2837|(5, 3, 16)|var|uint32
var_2838 = relay.var("var_2838", dtype = "uint32", shape = (5, 3, 16))#candidate|2838|(5, 3, 16)|var|uint32
output = func_2836(var_2837,var_2838,)
func_2839 = relay.Function([var_2837,var_2838,], output)
mutated_mod['func_2839'] = func_2839
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3640 = relay.var("var_3640", dtype = "float64", shape = (7, 16, 7))#candidate|3640|(7, 16, 7)|var|float64
uop_3641 = relay.acos(var_3640.astype('float64')) # shape=(7, 16, 7)
func_2836_call = mod.get_global_var('func_2836')
func_2839_call = mutated_mod.get_global_var('func_2839')
var_3661 = relay.var("var_3661", dtype = "uint32", shape = (240,))#candidate|3661|(240,)|var|uint32
call_3660 = func_2836_call(relay.reshape(var_3661.astype('uint32'), [5, 3, 16]), relay.reshape(var_3661.astype('uint32'), [5, 3, 16]), )
call_3662 = func_2836_call(relay.reshape(var_3661.astype('uint32'), [5, 3, 16]), relay.reshape(var_3661.astype('uint32'), [5, 3, 16]), )
output = relay.Tuple([uop_3641,call_3660,var_3661,])
output2 = relay.Tuple([uop_3641,call_3662,var_3661,])
func_3670 = relay.Function([var_3640,var_3661,], output)
mod['func_3670'] = func_3670
mod = relay.transform.InferType()(mod)
mutated_mod['func_3670'] = func_3670
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3670_call = mutated_mod.get_global_var('func_3670')
var_3672 = relay.var("var_3672", dtype = "float64", shape = (7, 16, 7))#candidate|3672|(7, 16, 7)|var|float64
var_3673 = relay.var("var_3673", dtype = "uint32", shape = (240,))#candidate|3673|(240,)|var|uint32
call_3671 = func_3670_call(var_3672,var_3673,)
output = call_3671
func_3674 = relay.Function([var_3672,var_3673,], output)
mutated_mod['func_3674'] = func_3674
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3757 = relay.var("var_3757", dtype = "bool", shape = ())#candidate|3757|()|var|bool
const_3758 = relay.const([[[True,True,False,False,True,False,False,True,True,False,True],[False,False,False,False,False,True,True,True,False,True,False],[False,True,False,True,False,True,True,True,True,False,False],[True,False,True,True,False,False,False,False,False,True,False],[False,True,False,False,False,False,False,True,False,False,True],[True,True,True,False,False,False,True,False,False,False,True],[False,True,True,False,True,False,False,False,False,True,False],[True,True,False,True,True,False,True,True,True,False,False],[False,False,True,True,True,True,True,True,False,True,False],[False,False,False,False,False,False,False,True,False,True,False],[True,False,True,True,False,False,False,False,True,False,True],[False,True,False,True,True,False,False,False,False,False,False]],[[False,False,True,True,False,False,True,False,True,False,False],[False,True,False,True,True,True,False,False,False,False,True],[False,True,False,False,True,True,True,True,True,True,True],[False,False,False,True,False,False,False,False,False,False,False],[True,True,True,False,True,True,False,True,True,False,True],[True,True,False,False,False,False,False,True,True,False,False],[True,True,False,True,True,False,False,False,False,True,True],[False,True,True,True,True,False,False,True,True,False,False],[False,False,False,False,False,False,True,True,False,True,False],[False,False,False,False,False,False,True,True,True,True,False],[False,False,True,True,True,True,False,True,True,False,True],[False,False,False,False,False,True,False,True,True,False,True]],[[True,False,False,True,True,True,True,False,False,True,True],[True,False,False,False,True,True,False,True,False,False,False],[False,False,False,True,False,True,True,False,False,False,False],[False,False,False,False,True,False,False,False,True,True,True],[True,False,False,False,False,True,True,False,True,True,False],[True,True,False,False,False,False,True,False,False,True,False],[False,True,True,True,True,False,False,True,True,False,True],[True,False,True,False,True,True,False,True,True,True,False],[True,False,False,True,True,False,True,False,True,False,False],[False,True,True,False,True,False,True,True,True,False,False],[False,True,True,True,True,False,False,False,False,True,False],[False,False,True,True,False,False,False,False,False,False,True]],[[True,True,False,False,False,False,True,True,False,False,False],[True,True,True,False,False,True,False,True,False,True,False],[True,False,False,True,False,False,True,False,True,True,True],[True,True,False,True,False,True,True,False,True,True,False],[False,True,False,True,True,True,True,False,True,True,False],[True,False,False,True,False,True,False,True,False,False,False],[False,True,False,True,True,True,False,False,True,False,True],[True,False,False,False,True,True,False,False,True,True,True],[False,True,True,True,True,False,True,True,False,False,True],[False,True,False,True,False,False,False,False,True,True,False],[True,False,False,False,False,False,False,True,True,False,False],[False,True,False,False,False,True,False,False,False,True,False]],[[False,False,False,False,True,False,True,False,True,True,False],[True,True,False,True,True,False,True,True,False,True,False],[False,False,True,False,False,True,False,True,True,True,False],[True,True,True,False,True,True,True,False,False,False,True],[False,True,True,False,False,False,True,False,True,True,False],[False,True,False,True,False,False,True,True,False,False,False],[True,False,True,False,True,True,False,True,True,True,True],[False,True,True,False,False,True,True,False,True,True,True],[False,True,True,False,False,False,False,False,True,True,True],[False,True,False,False,False,False,True,True,True,True,False],[False,True,True,False,True,True,True,False,False,True,True],[False,True,True,False,True,False,True,False,True,False,False]],[[True,False,False,True,True,True,False,False,True,True,True],[False,True,False,True,False,True,False,False,False,False,True],[False,False,True,False,False,True,True,False,True,False,False],[True,False,True,False,False,True,False,True,False,False,False],[True,False,True,False,False,True,False,False,False,False,False],[True,False,False,True,True,False,False,False,False,False,False],[True,False,False,False,False,False,True,True,False,False,True],[True,False,True,False,False,True,True,True,True,False,True],[False,True,True,False,False,True,True,False,True,False,False],[True,True,True,True,False,False,False,False,True,True,False],[False,False,False,True,True,True,False,True,True,False,True],[False,True,True,True,False,True,False,False,True,True,True]],[[False,True,True,False,True,True,True,False,True,True,False],[False,False,True,True,True,True,False,True,False,False,False],[True,True,False,False,True,True,True,True,False,False,False],[False,False,True,True,False,True,True,True,False,True,False],[True,False,True,False,True,False,False,True,True,True,True],[True,True,False,False,True,True,True,True,True,True,True],[False,False,True,False,True,True,False,False,True,True,True],[False,False,False,False,False,True,True,False,False,True,True],[True,True,False,False,False,True,False,True,True,False,False],[False,False,True,True,False,False,False,False,True,False,False],[True,True,False,False,False,False,True,True,False,False,True],[False,False,True,False,False,True,True,True,True,True,True]],[[False,True,False,False,True,False,True,False,False,False,True],[False,True,True,True,False,True,True,False,False,True,False],[True,True,True,False,False,False,True,False,True,False,True],[True,False,False,True,False,False,True,False,True,False,True],[True,True,True,False,False,True,False,True,False,True,True],[True,False,True,True,True,True,False,True,False,False,False],[True,True,False,True,True,False,True,True,False,False,False],[True,False,False,True,False,True,True,True,False,False,True],[False,True,True,True,True,False,False,True,False,True,True],[False,False,False,True,True,True,True,True,True,False,True],[True,True,True,False,False,True,True,False,False,True,True],[True,False,True,False,False,False,False,True,True,True,False]],[[True,False,True,False,True,True,True,True,False,False,True],[False,True,True,True,False,False,True,True,True,True,True],[False,True,False,True,True,True,False,False,True,False,False],[True,False,True,False,False,True,False,False,False,False,True],[True,True,True,True,True,False,True,False,False,True,True],[False,False,False,True,True,True,True,True,True,False,True],[True,False,True,False,False,False,False,True,True,True,False],[True,True,True,True,False,True,True,True,False,True,False],[True,True,True,False,False,False,True,False,True,False,False],[True,False,False,True,False,True,False,False,False,True,True],[True,True,True,True,False,False,True,False,False,False,True],[True,False,True,True,False,True,True,False,True,False,True]],[[True,True,True,True,True,True,True,True,False,False,False],[True,True,False,False,True,False,False,True,True,False,False],[False,True,False,True,False,False,False,False,True,False,True],[True,True,True,False,False,False,True,False,False,False,False],[False,False,True,True,True,False,False,True,False,True,False],[False,False,True,True,True,True,False,True,True,True,False],[False,False,False,False,True,False,False,True,False,False,False],[True,True,True,False,False,False,False,True,False,True,True],[True,False,False,True,False,True,False,False,True,False,False],[True,False,True,False,False,False,False,False,False,False,False],[True,False,False,True,False,True,False,True,False,True,True],[True,False,False,False,False,False,False,False,False,True,False]],[[True,True,False,True,False,True,False,False,True,True,False],[True,True,False,False,True,False,False,False,True,True,True],[True,False,True,True,False,False,True,True,False,False,True],[True,False,True,False,False,True,True,True,True,False,False],[True,False,True,True,False,False,True,False,True,False,False],[False,False,False,False,True,True,True,False,False,False,False],[True,False,False,False,True,True,True,True,False,True,True],[True,False,True,True,True,True,False,False,True,True,False],[True,True,True,True,False,True,True,False,True,True,False],[True,True,True,True,True,False,True,False,True,False,False],[True,False,False,False,False,False,False,True,False,True,True],[True,False,True,True,False,False,False,True,False,False,False]]], dtype = "bool")#candidate|3758|(11, 12, 11)|const|bool
bop_3759 = relay.logical_and(var_3757.astype('bool'), const_3758.astype('bool')) # shape=(11, 12, 11)
output = bop_3759
output2 = bop_3759
func_3774 = relay.Function([var_3757,], output)
mod['func_3774'] = func_3774
mod = relay.transform.InferType()(mod)
mutated_mod['func_3774'] = func_3774
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3775 = relay.var("var_3775", dtype = "bool", shape = ())#candidate|3775|()|var|bool
func_3774_call = mutated_mod.get_global_var('func_3774')
call_3776 = func_3774_call(var_3775)
output = call_3776
func_3777 = relay.Function([var_3775], output)
mutated_mod['func_3777'] = func_3777
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3927 = relay.var("var_3927", dtype = "int8", shape = (1, 10, 9))#candidate|3927|(1, 10, 9)|var|int8
var_3928 = relay.var("var_3928", dtype = "int8", shape = (2, 10, 9))#candidate|3928|(2, 10, 9)|var|int8
bop_3929 = relay.add(var_3927.astype('int8'), var_3928.astype('int8')) # shape=(2, 10, 9)
output = bop_3929
output2 = bop_3929
func_3937 = relay.Function([var_3927,var_3928,], output)
mod['func_3937'] = func_3937
mod = relay.transform.InferType()(mod)
var_3938 = relay.var("var_3938", dtype = "int8", shape = (1, 10, 9))#candidate|3938|(1, 10, 9)|var|int8
var_3939 = relay.var("var_3939", dtype = "int8", shape = (2, 10, 9))#candidate|3939|(2, 10, 9)|var|int8
output = func_3937(var_3938,var_3939,)
func_3940 = relay.Function([var_3938,var_3939,], output)
mutated_mod['func_3940'] = func_3940
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4428 = relay.var("var_4428", dtype = "float32", shape = (15, 7, 4))#candidate|4428|(15, 7, 4)|var|float32
uop_4429 = relay.rsqrt(var_4428.astype('float32')) # shape=(15, 7, 4)
output = uop_4429
output2 = uop_4429
func_4431 = relay.Function([var_4428,], output)
mod['func_4431'] = func_4431
mod = relay.transform.InferType()(mod)
mutated_mod['func_4431'] = func_4431
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4432 = relay.var("var_4432", dtype = "float32", shape = (15, 7, 4))#candidate|4432|(15, 7, 4)|var|float32
func_4431_call = mutated_mod.get_global_var('func_4431')
call_4433 = func_4431_call(var_4432)
output = call_4433
func_4434 = relay.Function([var_4432], output)
mutated_mod['func_4434'] = func_4434
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4498 = relay.const([[[-6.545911,-6.261899,-6.018659,6.832353,-3.972370,9.015871,9.509882,9.894306,-1.712386,2.484767,9.078260],[7.065667,-6.483460,-2.302762,0.826233,4.704531,-8.363766,5.855147,9.555301,5.578610,3.161916,-6.112988],[9.533910,-5.259978,-8.364871,6.178136,9.824879,5.611095,3.010704,9.671637,-0.909202,6.430607,4.427593],[0.827064,1.816987,-9.122727,4.279996,8.647290,-9.855712,1.795880,7.204867,-7.425782,5.301525,-5.069338],[2.792623,-3.531250,0.235443,-5.996976,-5.299731,0.517297,2.126393,-1.950540,-0.707997,8.790665,-5.600308],[6.594669,-8.082802,-4.017661,-6.456587,-6.820764,1.239830,0.975326,-4.934445,7.751587,3.243978,-3.433502],[-0.493249,1.426081,-5.402765,5.717667,7.862710,-5.047733,-3.816297,-3.013674,-6.858627,-4.191053,8.143884]],[[-4.423879,-8.838226,-2.896050,-7.823628,-0.684814,0.605413,8.480139,-8.801135,-2.185866,-1.132440,8.537047],[-1.840130,3.407696,3.452097,-8.905570,8.273301,-4.988241,-5.034643,6.641448,-9.119348,2.079271,6.490667],[8.820298,0.624662,-9.161786,6.712750,-7.049737,5.269039,-7.880465,2.548614,6.528935,8.179522,-2.025258],[-0.609735,-8.257149,0.350577,-0.630053,-9.500369,7.611663,-9.666962,2.308499,3.628130,0.226745,2.186579],[3.461639,-8.064997,5.227333,1.582373,3.295618,8.012775,-2.998387,2.436861,-9.618975,-8.180736,7.566247],[4.621613,-2.179346,-9.333219,3.200186,0.384350,-2.030211,3.641547,1.194159,-1.536050,-5.112994,-0.188234],[-2.054897,1.446694,-2.409920,-6.418154,-7.611664,-5.447060,0.090898,-4.645925,7.059473,7.875801,1.284758]],[[2.029707,7.689758,4.339335,-5.797412,-0.659466,3.330141,0.477344,-3.750947,3.572543,7.098093,9.457637],[-5.242802,1.976974,-5.806433,-1.948031,6.195214,-0.136696,1.422458,-5.331715,-1.764714,-4.370557,-7.059521],[0.478587,-9.704868,-1.015394,-6.200189,-8.183625,4.536425,-3.079794,-8.363824,-7.645779,9.557370,6.292666],[-1.546355,-7.101579,-9.367712,2.750270,-5.816540,0.669559,0.190941,-9.531257,-1.708869,1.887844,-5.469508],[7.140376,-3.011121,-7.900756,-0.672578,-2.325660,9.556115,1.376886,0.272595,-8.167652,9.501143,-9.327797],[7.117598,0.215908,7.447634,-8.841714,-6.574196,6.609403,7.423305,-6.041431,9.127282,-4.059477,6.811649],[-8.192608,-5.322028,-0.401829,9.186103,1.292669,6.134057,-3.512062,1.694193,-2.857897,-6.287127,-1.286057]],[[3.450278,5.727698,1.230763,5.822048,-1.823407,0.709730,7.204274,-0.341090,4.873122,0.752730,-8.245356],[5.542065,-9.514063,-2.093257,1.796872,-7.054038,4.571403,3.008453,-9.396086,-1.618727,4.088983,3.493668],[3.591975,3.778732,2.844385,-8.991529,-3.574577,9.813232,8.352848,2.417937,-8.956499,-7.959227,4.866903],[-4.503038,-4.084084,-5.098011,8.929139,-8.882356,-6.735910,6.419150,2.604887,1.376839,9.840599,-3.867027],[-0.826603,-6.761955,-4.694971,0.688913,-9.230404,4.964354,-7.016393,-1.981764,6.468763,-6.802840,-7.480501],[-2.804455,5.593304,0.859965,-7.161835,-7.192806,4.690865,-8.991313,9.217130,-7.915638,1.387183,-6.733984],[1.875297,2.015838,-2.589935,-8.065167,7.250749,-7.242571,9.602705,-7.355935,2.021406,-2.537841,1.214750]],[[-2.386961,-6.364452,-3.429747,-8.286437,7.044944,-3.210781,2.198866,6.930805,4.884295,-4.396842,9.902019],[-0.153644,2.390651,-9.717287,-3.531630,-0.605670,-8.767377,6.079475,4.302458,-1.471948,-6.043900,3.861024],[3.038933,8.368548,-7.318324,-9.628033,3.270231,3.946862,-1.207672,9.962627,0.404273,-0.174244,-4.628083],[-7.467916,3.711292,5.273254,0.834861,4.878032,1.385015,-8.828662,-9.125136,0.576819,5.578935,5.369373],[5.961821,-0.293831,-0.042471,-3.003111,9.163214,-5.219826,5.310446,-2.490105,6.200777,9.656836,-8.836667],[-2.108960,-7.229806,7.878377,-3.933503,-5.199485,4.755324,-5.142124,1.833604,-5.319869,0.363949,9.285407],[-1.466979,-0.368750,-9.021248,-4.343200,6.900155,4.749333,2.665200,9.090448,9.412322,4.844917,-5.601271]],[[2.415105,-5.350602,-8.420951,-3.485010,2.000879,4.002399,-7.672398,9.690191,2.361178,7.982747,2.601847],[7.943248,-8.393051,-6.694734,2.673686,5.452601,-9.802887,-9.976010,-0.444054,-2.395136,-4.866878,0.079142],[3.276931,5.777099,2.290996,-3.382500,1.113887,9.358178,-0.982060,6.522988,-1.678256,-9.251745,6.594275],[-9.108839,-4.662847,6.714968,-8.456053,2.846044,3.616633,-9.976750,-4.840709,0.921400,-5.637560,4.355372],[-1.538190,-0.646358,-9.940917,3.310875,-3.756951,6.240447,2.804110,3.118410,4.347026,0.829233,7.740491],[2.133320,-8.515169,-6.315919,4.553471,-2.489024,-7.466368,-0.767784,3.631085,-6.654255,0.932678,-9.196521],[-1.498139,2.913305,0.113067,0.805938,-4.809930,-8.597584,9.029755,-6.365457,-0.435371,0.296092,5.005218]],[[6.954721,1.489027,-5.132371,4.626484,3.229835,-5.543602,2.027322,-8.339385,6.443683,7.230318,8.060717],[-4.377171,3.580316,-8.864217,7.402631,9.679928,3.025239,0.481578,3.690960,-9.915267,-3.248735,2.285627],[-9.825186,-7.386093,4.590064,7.907012,1.294003,-5.419459,4.909417,4.657974,-5.699272,4.495321,2.545939],[-4.859284,-2.621960,-6.853825,1.981121,-2.870501,9.439892,5.143133,5.591241,1.639198,-5.910385,1.275212],[4.223878,3.024285,9.406184,4.578136,8.002663,-6.612440,-2.098852,-4.907087,-9.384298,-8.507099,-3.511641],[-9.390726,-2.042259,-3.494371,6.619621,-9.363769,-7.972441,7.047634,8.879000,-9.184398,-3.771355,-3.847685],[6.961573,-5.788119,5.954615,7.751629,6.041224,9.816328,-0.780772,-3.444400,-1.212821,-4.543459,-6.667778]],[[-2.426514,-0.910582,-9.497723,0.070776,4.012306,-1.734244,5.086540,-4.608915,9.779952,-6.585511,-4.433001],[-1.816160,4.398564,6.657177,8.126059,8.635663,0.881452,-7.035196,-1.265173,-8.816351,5.525569,0.891615],[6.041314,5.892639,2.106424,9.612756,-0.051439,8.281958,-7.053402,1.566294,-1.044385,-4.579982,-6.391901],[-0.292294,-4.398003,0.532399,2.977322,-4.339087,-8.453728,0.594218,-5.549961,0.686297,-3.657411,-8.651159],[-1.256150,-3.755894,-8.522321,-9.829281,0.486106,9.945018,-0.274593,5.825427,1.076042,-9.816513,-8.779249],[-5.948134,-5.521637,6.604301,-2.052178,-7.249304,-7.121422,3.741272,3.706682,2.319296,-7.706646,-2.208925],[1.849887,-4.939303,-4.099478,0.299035,-8.871559,4.669345,0.706129,2.131703,-2.075579,-1.413560,-6.921321]]], dtype = "float64")#candidate|4498|(8, 7, 11)|const|float64
uop_4499 = relay.acosh(const_4498.astype('float64')) # shape=(8, 7, 11)
func_3670_call = mod.get_global_var('func_3670')
func_3674_call = mutated_mod.get_global_var('func_3674')
const_4507 = relay.const([[-8.865551,0.851839,4.164244,7.573934,8.193288,1.639565,-3.145988,9.922115,7.773295,-6.285422,-0.837795,-6.094555,-4.268911,6.646838,3.710095,-6.270712,3.573170,-0.900012,9.205443,-7.402989,7.520583,5.501377,5.317223,7.773221,-0.482397,0.852522,-3.335185,0.994075,7.141093,6.330028,8.850138,-3.017201,-8.102635,-1.802311,-9.039039,-1.854255,-0.853752,0.224502,9.728740,0.036850,-9.135858,-9.333702,-2.326760,-4.286625,-8.006550,-0.744584,9.626311,1.816810,4.015720,4.647179,-0.510253,-6.276159,2.080461,-8.448734,-5.716399,2.599335,-4.132616,0.611439,6.931717,-4.516164,-9.201767,4.167663,8.215599,7.595957,-9.952512,5.445649,-7.100396,-4.146503,6.847278,-1.079327,-0.597919,6.708673,-6.661627,2.226014,-2.124533,2.287360,-6.250864,-2.286104,2.568166,-7.190254,-1.326021,-8.524048,2.546886,-6.696692,-4.029254,2.455317,-1.331197,0.159860,3.879711,-7.448536,7.982790,-8.935773,6.639271,4.191767,-0.167884,-6.511852,5.270632,-6.537769,9.963828,-6.520429,3.109112,-4.945554,-4.207059,-0.277437,-6.398526,4.742854,4.305767,3.763090,-4.656667,8.660718,8.739529,6.413150,3.459216,4.705106,-1.089367,-4.763198,0.401157,-1.700373,-5.172254,-2.705922,9.272151,-6.557114,4.535270,0.312439,2.604606,8.614594,0.312767,5.485585,-8.785700,7.428468,-8.634781,-5.906099,5.162622,6.079926,-5.764763,-2.950492,7.267417,-9.032817,1.430478,-3.933303,-7.546305,0.043808,-1.632553,-0.263844,5.145403,-4.712284,7.363723,-3.429189,8.773246,5.034114,7.792737,3.331036,-1.492503,0.627750,-3.470967,-0.608251,7.775663,-1.282585,4.132171,-3.973031,-9.392508,-0.122084,-1.877006,-3.747596,7.079262,2.183189,-4.323634,9.740239,-7.876172,-1.683859,9.549954,4.137483,-5.864161,-1.576479,3.716738,-0.769816,4.714118,7.261700,4.553858,3.955790,9.787488,0.548204,-1.970761,7.740991,-6.991922,7.724943,-1.599345,-4.931995,-3.876288,-2.667562,-3.894133,8.170423,-0.049915,4.782785,0.606259,-6.643895],[1.445909,-0.681391,-9.161924,-6.551866,2.989208,-9.476891,-7.155292,-0.602435,-6.732100,-8.975176,5.527603,-2.281511,2.491986,-0.371323,5.874064,9.948265,-7.435207,-4.510268,7.900939,5.410137,-0.489125,2.927632,9.575448,2.460292,-9.421821,-7.340159,1.536016,5.001013,-9.256703,9.646010,-1.832199,-8.565483,-4.648158,-0.864916,8.981294,-4.344389,3.122432,-2.526858,2.395632,-9.426989,-4.471148,-8.213282,-1.787007,-9.380117,9.116050,-8.150576,-9.282153,-3.818859,6.833437,8.651490,6.416038,-1.663599,3.009676,3.875165,-3.990121,-7.458000,-7.384104,-0.359379,2.448410,5.463401,5.362661,-4.392393,-9.646561,-0.746424,7.477982,-1.839567,-2.591694,-0.322337,0.277722,-2.396335,8.834955,-1.526161,8.121423,-6.421330,0.119778,8.758681,2.389825,1.311023,4.192799,8.640672,8.334737,4.393279,-6.359444,3.463559,6.319941,1.368851,-0.769323,-1.094660,9.685272,-2.764509,-9.767508,9.589974,-5.692721,9.244689,-5.613679,-7.305853,-2.304175,8.687568,2.405615,-8.250830,4.764039,-5.659739,-9.768978,0.047580,2.654586,-5.470325,-4.062527,-3.523646,-6.508937,-4.229066,-6.403382,-0.650726,-6.390186,-4.295385,-7.977915,-7.737959,-4.269033,-3.592010,3.657758,-9.721535,7.349144,-2.652232,-4.353587,-4.375791,-8.540606,-0.109155,-6.710788,0.577898,-6.728097,-6.319635,-2.318071,-7.525459,0.905261,3.121745,3.382707,-5.709857,6.187465,-5.114560,6.329759,-8.013275,5.586312,-1.887549,-6.352177,-4.257558,1.025894,3.945683,8.172339,5.328357,-1.515318,9.128991,-9.790256,1.461785,-6.923113,-5.979866,-1.738660,1.863904,1.442323,4.117494,9.069033,-2.769848,8.719612,-6.457992,-4.550362,6.664787,6.452669,-4.006409,-8.995847,7.213892,7.175828,-9.469045,-1.782421,9.505897,-0.896152,3.407972,-8.608002,-9.784623,-0.538664,-7.552989,-4.790386,7.486529,-6.279721,-1.105584,2.815275,2.538219,5.520488,3.941846,4.701113,2.839940,0.716739,4.336198,-1.787659,8.035636,-4.692932,2.671212,-2.699774,-4.951857],[-5.540196,3.834204,-6.961848,-0.431739,3.885738,-1.659990,-4.981180,-0.765177,-8.382908,6.686039,1.218414,9.370716,-9.939296,0.072189,-6.495936,5.062143,-4.917389,-7.057059,6.761399,-3.655678,-0.544409,7.239795,-3.350938,4.334658,4.673892,2.453458,8.390924,6.011655,-3.186338,-2.655116,-2.005442,4.820113,6.002400,-7.287336,7.265504,3.724483,4.368855,-2.594615,-9.778593,-9.539747,4.867502,-3.828746,7.589387,-4.924074,-3.330514,-2.820665,7.611332,7.213084,9.437022,9.896571,-4.930466,3.203760,-9.472225,4.910914,2.042120,-1.437034,-4.811009,8.260395,-1.025258,7.192121,2.810155,-2.261044,4.840561,5.606005,8.926862,9.462408,5.092182,7.846968,6.950782,-2.423035,-8.840813,6.590283,9.565600,-7.051201,-8.147192,4.521126,1.617660,-9.025875,5.097913,-5.875631,3.090707,6.340866,-0.853052,-4.470722,9.611258,-4.789511,5.361710,-4.931664,-1.856392,6.338938,-1.924026,-0.367605,-9.645649,0.382609,-9.122762,-4.611535,8.437223,-1.145295,-8.995197,9.086451,7.516103,6.346148,7.265688,-9.387020,8.373836,1.080864,-5.769660,4.934138,-3.951375,-2.457015,-5.087240,-4.988918,-1.580628,5.936006,4.740318,0.066101,-6.624836,-5.952199,-4.604882,-7.461729,-7.277758,-0.189609,3.137106,0.289523,-2.061927,3.703688,-3.302704,-5.306349,-9.605887,1.358303,5.936386,1.784408,1.520527,3.416048,-6.641692,3.879724,0.848260,8.578509,-0.880826,8.141274,-3.699312,3.510014,-7.052329,-1.967886,-7.861546,8.587078,-6.292918,9.558351,-5.851695,0.919698,-4.510477,8.218811,-4.677671,4.968400,4.298548,7.520264,4.191546,-1.908439,4.196342,-1.696583,-3.601132,7.911304,-9.688560,-1.448791,7.115301,2.223026,9.306192,-8.383638,2.541897,-6.980018,-3.083106,0.060692,-4.007191,6.095776,-2.509588,3.113215,0.766124,7.993826,-0.844206,-3.422065,0.257134,4.505470,-9.184932,2.014325,4.279506,-2.757664,6.726732,5.118290,3.678535,2.012287,0.167652,-4.949947,4.872364,-1.978675,-6.172216,-2.799120],[3.312189,-3.112443,7.502477,3.040376,1.463573,-9.635702,5.781397,-5.752553,-4.643439,-2.842447,8.048318,1.104823,-4.278563,-3.251200,-1.488057,4.244431,-3.879332,-2.238520,9.636023,8.135927,7.492931,8.234709,9.618946,-1.296996,-9.393022,3.267382,3.755156,-8.416255,5.746760,-2.360627,6.324948,5.470933,9.627843,8.978235,2.770069,9.354454,-8.757235,-2.235089,8.165821,-7.368158,6.339065,6.347439,-3.497270,9.861403,-7.110496,8.614866,4.850251,1.719374,-0.853225,1.848682,7.593998,8.029485,8.724739,-8.506828,-1.047751,-8.951557,-5.592211,-6.253902,-6.536565,-7.818419,-6.595540,-4.130814,-4.757719,-1.798045,9.429859,5.483299,9.935315,-4.575326,-5.331540,7.500496,4.706881,-7.305565,9.338432,-4.509519,-4.191143,-0.375563,6.966311,-2.870660,-7.333041,-2.214624,-0.322384,6.929172,-4.421713,2.517332,-8.542739,6.258031,-2.405067,1.802238,0.482629,4.576007,3.234439,-5.196676,2.800927,-0.164799,1.917705,3.522642,-2.596707,8.852572,-4.236739,7.691427,1.243620,2.616852,0.585441,1.210444,-3.439559,-5.807164,-5.191288,-8.410721,-8.498949,-0.052416,-8.675768,3.272441,-5.030355,7.867990,7.500232,7.929627,-9.884458,7.148736,8.777448,-1.014416,1.239306,8.470100,1.458535,2.704861,8.939844,8.491706,1.167360,-9.756946,-6.519412,8.521590,6.487830,-8.280796,7.574464,1.179981,7.237434,-8.508392,-2.456068,-9.920592,-6.386936,6.528861,9.333111,5.948175,-6.594958,-9.896865,5.665047,-0.268841,-7.252919,-7.441929,-7.790173,7.077600,4.740028,0.143330,6.139597,7.669030,2.891821,4.452004,-3.380153,-9.443994,3.911919,9.277498,-2.747292,5.616614,-7.940172,-0.119438,2.069597,-7.526186,2.088794,-7.278209,-0.549637,-3.121180,5.825224,-1.050749,-4.595606,-1.658770,-5.483051,9.478238,1.372738,2.707294,-6.546839,3.051264,6.652866,1.492260,0.870858,-3.398918,2.364700,0.168995,-1.488430,-1.126785,-2.258093,-9.844997,-8.996292,5.503807,-9.671355,-8.494580,-8.290109,-1.184874]], dtype = "float64")#candidate|4507|(4, 196)|const|float64
const_4508 = relay.const([-2,-6,-4,5,6,3,-1,5,-5,-6,9,8,8,4,-5,-1,2,7,6,5,7,-1,-8,-2,3,8,4,9,-5,7,-2,4,-6,9,4,7,3,8,4,-6,2,9,9,-7,3,-2,-4,10,-9,3,4,-3,-6,10,-4,7,8,1,5,2,6,4,4,2,-4,7,3,-5,-4,10,-9,6,-2,7,-9,-7,4,-6,7,2,-3,9,2,6,9,7,-1,-7,4,-2,4,-9,-5,9,-3,3,-1,-1,-4,-2,-2,-3,4,8,6,10,-1,8,-1,8,-9,1,1,4,8,-10,-7,-3,-5,-8,3,10,-4,-10,7,-1,8,6,-4,7,-8,-4,2,-5,-10,-7,-8,7,-7,-9,6,1,-3,-3,7,1,-7,-10,2,-5,8,-5,8,10,-10,10,-2,8,-7,-4,-1,2,10,8,-9,6,4,6,5,7,-9,-9,-7,-8,-2,-1,-9,-2,4,3,-4,3,-2,9,-6,-1,5,-8,1,-9,10,5,-2,10,-8,9,6,7,10,-3,6,1,-8,-6,-7,-1,6,8,-2,3,-3,-9,6,-7,3,3,6,3,-5,2,-5,-8,-8,8,-7,9,5,1,5,8,-9,-9,6,-10,10,-2,-6,5,-1,3], dtype = "uint32")#candidate|4508|(240,)|const|uint32
call_4506 = relay.TupleGetItem(func_3670_call(relay.reshape(const_4507.astype('float64'), [7, 16, 7]), relay.reshape(const_4508.astype('uint32'), [240,]), ), 0)
call_4509 = relay.TupleGetItem(func_3674_call(relay.reshape(const_4507.astype('float64'), [7, 16, 7]), relay.reshape(const_4508.astype('uint32'), [240,]), ), 0)
output = relay.Tuple([uop_4499,call_4506,const_4507,const_4508,])
output2 = relay.Tuple([uop_4499,call_4509,const_4507,const_4508,])
func_4510 = relay.Function([], output)
mod['func_4510'] = func_4510
mod = relay.transform.InferType()(mod)
mutated_mod['func_4510'] = func_4510
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4510_call = mutated_mod.get_global_var('func_4510')
call_4511 = func_4510_call()
output = call_4511
func_4512 = relay.Function([], output)
mutated_mod['func_4512'] = func_4512
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4510_call = mod.get_global_var('func_4510')
func_4512_call = mutated_mod.get_global_var('func_4512')
call_4557 = relay.TupleGetItem(func_4510_call(), 1)
call_4558 = relay.TupleGetItem(func_4512_call(), 1)
func_1019_call = mod.get_global_var('func_1019')
func_1023_call = mutated_mod.get_global_var('func_1023')
const_4563 = relay.const([9,-7,5,2,-2,-7,-1,3,-7,1,5,-3,-4,2,-10,1,-6,-6,-10,8,1,2,-10,5,7,3,-9,4,5,-1,-4,-6,-1,-3,1,10,9,-5,10,6,6,-9,8,-2,9,9,6,-6,-6,-5,-10,-8,-8,8,4,5,-5,-9,-6,-7,-2,8,10,4,-3,-4,3,-4,6,1,7,-2,-10,7,-9,3,-9,-9,7,8,2,4,5,-8,-3,-2,7,-5,2,5,4,-5,10,-3,-9,8,-2,-9,-4,9,8,-8,-5,1,2,-1,5,1,-9,-4,-7,8,-7,-8,3,-8,9,5,-6,-1,4,7,5,-7,-2,1,-5,9,-7,5,-4,-3,9,-7,6,-5,10,-2,-10,1,1,-3,4,-2,-9,-1,2,-6,-1,7,-10,8,4,9,8,-10,-6,7,5,1,6,8,7,8,8,-5,-8,2,-2,8,3,-1,2,-6,-7,2,-8,-1,8,-3,5,-5,-1,-4,8,-5,1,7,-5,-2,-10,6,-7,-5,8,-1,5,3,3,-3,1,-1,5,8,2,2,4,-2,-7,-8,-6,-8,-5,1,10,10,-1,6,10,5,3,6,7,10,8,1,-9,4,-3,5,-8,-7,-7,-6,6,-10,1,6,-7,-4,-6,-8,-5,2,-7,3,1,4,-10,4,-2,-5,-4,2,9,8,-2,-2,-9,7,1,-1,10,8,-6,8,-1,-2,3,-8,-2,10,5,5,6,1,-3,-10,8,3,-2,-3,-1,10,10,8,8,-10,-10,8,6,-5,-2,2,-3,-5,3,2,2,1,1,6,7,-2,-8,5,10,4,5,3,10,-4,3,-10,7,-8,1,8,9,-5,2,2,-9,5,4,-1,5,7,1,-4,-9,7,-6,7,6,-4,-1,-2,5,-4,5,-3,-1,10,-10,-10,-9,-8,-1,10,-9,6,1,2,-5,-4,2,-1,-8,6,-7,8,3,-1,-2,-10,7,1,-3,-5,7,-9,7,-5,4,6,8,-7,9,-5,-3,10,-10,10,-1,-4,-6,-1,-4,9,-8,7,-8,-8,4,-6,8,-9,-4,-4,3,5,-8,2,3,-9,-8,-8,5,-1,-9,8,-2,4,5,3,5,-7,6,-6,-5,-9,-3,9,-5,7,-9,9,-1,7,2,-3], dtype = "uint8")#candidate|4563|(432,)|const|uint8
call_4562 = func_1019_call(relay.reshape(const_4563.astype('uint8'), [6, 12, 6]), relay.reshape(const_4563.astype('uint8'), [6, 12, 6]), )
call_4564 = func_1019_call(relay.reshape(const_4563.astype('uint8'), [6, 12, 6]), relay.reshape(const_4563.astype('uint8'), [6, 12, 6]), )
func_3774_call = mod.get_global_var('func_3774')
func_3777_call = mutated_mod.get_global_var('func_3777')
const_4574 = relay.const(True, dtype = "bool")#candidate|4574|()|const|bool
call_4573 = func_3774_call(relay.reshape(const_4574.astype('bool'), []))
call_4575 = func_3774_call(relay.reshape(const_4574.astype('bool'), []))
output = relay.Tuple([call_4557,call_4562,const_4563,call_4573,const_4574,])
output2 = relay.Tuple([call_4558,call_4564,const_4563,call_4575,const_4574,])
func_4581 = relay.Function([], output)
mod['func_4581'] = func_4581
mod = relay.transform.InferType()(mod)
output = func_4581()
func_4582 = relay.Function([], output)
mutated_mod['func_4582'] = func_4582
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4510_call = mod.get_global_var('func_4510')
func_4512_call = mutated_mod.get_global_var('func_4512')
call_4600 = relay.TupleGetItem(func_4510_call(), 1)
call_4601 = relay.TupleGetItem(func_4512_call(), 1)
uop_4608 = relay.asinh(call_4600.astype('float32')) # shape=(7, 16, 7)
uop_4610 = relay.asinh(call_4601.astype('float32')) # shape=(7, 16, 7)
output = uop_4608
output2 = uop_4610
func_4611 = relay.Function([], output)
mod['func_4611'] = func_4611
mod = relay.transform.InferType()(mod)
mutated_mod['func_4611'] = func_4611
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4611_call = mutated_mod.get_global_var('func_4611')
call_4612 = func_4611_call()
output = call_4612
func_4613 = relay.Function([], output)
mutated_mod['func_4613'] = func_4613
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4581_call = mod.get_global_var('func_4581')
func_4582_call = mutated_mod.get_global_var('func_4582')
call_4624 = relay.TupleGetItem(func_4581_call(), 0)
call_4625 = relay.TupleGetItem(func_4582_call(), 0)
output = relay.Tuple([call_4624,])
output2 = relay.Tuple([call_4625,])
func_4637 = relay.Function([], output)
mod['func_4637'] = func_4637
mod = relay.transform.InferType()(mod)
output = func_4637()
func_4638 = relay.Function([], output)
mutated_mod['func_4638'] = func_4638
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4666 = relay.var("var_4666", dtype = "float32", shape = (16, 7, 9))#candidate|4666|(16, 7, 9)|var|float32
uop_4667 = relay.sin(var_4666.astype('float32')) # shape=(16, 7, 9)
func_4611_call = mod.get_global_var('func_4611')
func_4613_call = mutated_mod.get_global_var('func_4613')
call_4679 = func_4611_call()
call_4680 = func_4611_call()
output = relay.Tuple([uop_4667,call_4679,])
output2 = relay.Tuple([uop_4667,call_4680,])
func_4684 = relay.Function([var_4666,], output)
mod['func_4684'] = func_4684
mod = relay.transform.InferType()(mod)
mutated_mod['func_4684'] = func_4684
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4685 = relay.var("var_4685", dtype = "float32", shape = (16, 7, 9))#candidate|4685|(16, 7, 9)|var|float32
func_4684_call = mutated_mod.get_global_var('func_4684')
call_4686 = func_4684_call(var_4685)
output = call_4686
func_4687 = relay.Function([var_4685], output)
mutated_mod['func_4687'] = func_4687
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4637_call = mod.get_global_var('func_4637')
func_4638_call = mutated_mod.get_global_var('func_4638')
call_4698 = relay.TupleGetItem(func_4637_call(), 0)
call_4699 = relay.TupleGetItem(func_4638_call(), 0)
uop_4705 = relay.cos(call_4698.astype('float32')) # shape=(7, 16, 7)
uop_4707 = relay.cos(call_4699.astype('float32')) # shape=(7, 16, 7)
output = relay.Tuple([uop_4705,])
output2 = relay.Tuple([uop_4707,])
func_4728 = relay.Function([], output)
mod['func_4728'] = func_4728
mod = relay.transform.InferType()(mod)
mutated_mod['func_4728'] = func_4728
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4728_call = mutated_mod.get_global_var('func_4728')
call_4729 = func_4728_call()
output = call_4729
func_4730 = relay.Function([], output)
mutated_mod['func_4730'] = func_4730
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4581_call = mod.get_global_var('func_4581')
func_4582_call = mutated_mod.get_global_var('func_4582')
call_4753 = relay.TupleGetItem(func_4581_call(), 2)
call_4754 = relay.TupleGetItem(func_4582_call(), 2)
func_4581_call = mod.get_global_var('func_4581')
func_4582_call = mutated_mod.get_global_var('func_4582')
call_4756 = relay.TupleGetItem(func_4581_call(), 3)
call_4757 = relay.TupleGetItem(func_4582_call(), 3)
func_3774_call = mod.get_global_var('func_3774')
func_3777_call = mutated_mod.get_global_var('func_3777')
const_4768 = relay.const(True, dtype = "bool")#candidate|4768|()|const|bool
call_4767 = func_3774_call(relay.reshape(const_4768.astype('bool'), []))
call_4769 = func_3774_call(relay.reshape(const_4768.astype('bool'), []))
output = relay.Tuple([call_4753,call_4756,call_4767,const_4768,])
output2 = relay.Tuple([call_4754,call_4757,call_4769,const_4768,])
func_4772 = relay.Function([], output)
mod['func_4772'] = func_4772
mod = relay.transform.InferType()(mod)
output = func_4772()
func_4773 = relay.Function([], output)
mutated_mod['func_4773'] = func_4773
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4772_call = mod.get_global_var('func_4772')
func_4773_call = mutated_mod.get_global_var('func_4773')
call_4819 = relay.TupleGetItem(func_4772_call(), 0)
call_4820 = relay.TupleGetItem(func_4773_call(), 0)
func_4637_call = mod.get_global_var('func_4637')
func_4638_call = mutated_mod.get_global_var('func_4638')
call_4821 = relay.TupleGetItem(func_4637_call(), 0)
call_4822 = relay.TupleGetItem(func_4638_call(), 0)
func_4611_call = mod.get_global_var('func_4611')
func_4613_call = mutated_mod.get_global_var('func_4613')
call_4825 = func_4611_call()
call_4826 = func_4611_call()
uop_4836 = relay.sinh(call_4821.astype('float64')) # shape=(7, 16, 7)
uop_4838 = relay.sinh(call_4822.astype('float64')) # shape=(7, 16, 7)
output = relay.Tuple([call_4819,call_4825,uop_4836,])
output2 = relay.Tuple([call_4820,call_4826,uop_4838,])
func_4853 = relay.Function([], output)
mod['func_4853'] = func_4853
mod = relay.transform.InferType()(mod)
mutated_mod['func_4853'] = func_4853
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4853_call = mutated_mod.get_global_var('func_4853')
call_4854 = func_4853_call()
output = call_4854
func_4855 = relay.Function([], output)
mutated_mod['func_4855'] = func_4855
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4853_call = mod.get_global_var('func_4853')
func_4855_call = mutated_mod.get_global_var('func_4855')
call_4862 = relay.TupleGetItem(func_4853_call(), 1)
call_4863 = relay.TupleGetItem(func_4855_call(), 1)
func_4772_call = mod.get_global_var('func_4772')
func_4773_call = mutated_mod.get_global_var('func_4773')
call_4867 = relay.TupleGetItem(func_4772_call(), 2)
call_4868 = relay.TupleGetItem(func_4773_call(), 2)
output = relay.Tuple([call_4862,call_4867,])
output2 = relay.Tuple([call_4863,call_4868,])
func_4908 = relay.Function([], output)
mod['func_4908'] = func_4908
mod = relay.transform.InferType()(mod)
mutated_mod['func_4908'] = func_4908
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4908_call = mutated_mod.get_global_var('func_4908')
call_4909 = func_4908_call()
output = call_4909
func_4910 = relay.Function([], output)
mutated_mod['func_4910'] = func_4910
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4611_call = mod.get_global_var('func_4611')
func_4613_call = mutated_mod.get_global_var('func_4613')
call_4972 = func_4611_call()
call_4973 = func_4611_call()
output = relay.Tuple([call_4972,])
output2 = relay.Tuple([call_4973,])
func_4980 = relay.Function([], output)
mod['func_4980'] = func_4980
mod = relay.transform.InferType()(mod)
mutated_mod['func_4980'] = func_4980
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4980_call = mutated_mod.get_global_var('func_4980')
call_4981 = func_4980_call()
output = call_4981
func_4982 = relay.Function([], output)
mutated_mod['func_4982'] = func_4982
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4581_call = mod.get_global_var('func_4581')
func_4582_call = mutated_mod.get_global_var('func_4582')
call_5019 = relay.TupleGetItem(func_4581_call(), 1)
call_5020 = relay.TupleGetItem(func_4582_call(), 1)
func_1019_call = mod.get_global_var('func_1019')
func_1023_call = mutated_mod.get_global_var('func_1023')
call_5024 = func_1019_call(relay.reshape(call_5019.astype('uint8'), [6, 12, 6]), relay.reshape(call_5019.astype('uint8'), [6, 12, 6]), )
call_5025 = func_1019_call(relay.reshape(call_5019.astype('uint8'), [6, 12, 6]), relay.reshape(call_5019.astype('uint8'), [6, 12, 6]), )
uop_5030 = relay.exp(call_5019.astype('float32')) # shape=(6, 12, 6)
uop_5032 = relay.exp(call_5020.astype('float32')) # shape=(6, 12, 6)
output = relay.Tuple([call_5024,uop_5030,])
output2 = relay.Tuple([call_5025,uop_5032,])
func_5058 = relay.Function([], output)
mod['func_5058'] = func_5058
mod = relay.transform.InferType()(mod)
mutated_mod['func_5058'] = func_5058
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5058_call = mutated_mod.get_global_var('func_5058')
call_5059 = func_5058_call()
output = call_5059
func_5060 = relay.Function([], output)
mutated_mod['func_5060'] = func_5060
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4510_call = mod.get_global_var('func_4510')
func_4512_call = mutated_mod.get_global_var('func_4512')
call_5078 = relay.TupleGetItem(func_4510_call(), 0)
call_5079 = relay.TupleGetItem(func_4512_call(), 0)
func_2677_call = mod.get_global_var('func_2677')
func_2682_call = mutated_mod.get_global_var('func_2682')
var_5087 = relay.var("var_5087", dtype = "int8", shape = (70, 15))#candidate|5087|(70, 15)|var|int8
var_5088 = relay.var("var_5088", dtype = "uint8", shape = (432,))#candidate|5088|(432,)|var|uint8
call_5086 = relay.TupleGetItem(func_2677_call(relay.reshape(var_5087.astype('int8'), [15, 5, 14]), relay.reshape(var_5087.astype('int8'), [15, 5, 14]), relay.reshape(var_5087.astype('int8'), [15, 5, 14]), relay.reshape(var_5088.astype('uint8'), [432,]), ), 4)
call_5089 = relay.TupleGetItem(func_2682_call(relay.reshape(var_5087.astype('int8'), [15, 5, 14]), relay.reshape(var_5087.astype('int8'), [15, 5, 14]), relay.reshape(var_5087.astype('int8'), [15, 5, 14]), relay.reshape(var_5088.astype('uint8'), [432,]), ), 4)
output = relay.Tuple([call_5078,call_5086,var_5087,var_5088,])
output2 = relay.Tuple([call_5079,call_5089,var_5087,var_5088,])
func_5096 = relay.Function([var_5087,var_5088,], output)
mod['func_5096'] = func_5096
mod = relay.transform.InferType()(mod)
var_5097 = relay.var("var_5097", dtype = "int8", shape = (70, 15))#candidate|5097|(70, 15)|var|int8
var_5098 = relay.var("var_5098", dtype = "uint8", shape = (432,))#candidate|5098|(432,)|var|uint8
output = func_5096(var_5097,var_5098,)
func_5099 = relay.Function([var_5097,var_5098,], output)
mutated_mod['func_5099'] = func_5099
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4611_call = mod.get_global_var('func_4611')
func_4613_call = mutated_mod.get_global_var('func_4613')
call_5160 = func_4611_call()
call_5161 = func_4611_call()
uop_5178 = relay.sin(call_5160.astype('float64')) # shape=(7, 16, 7)
uop_5180 = relay.sin(call_5161.astype('float64')) # shape=(7, 16, 7)
output = uop_5178
output2 = uop_5180
func_5192 = relay.Function([], output)
mod['func_5192'] = func_5192
mod = relay.transform.InferType()(mod)
output = func_5192()
func_5193 = relay.Function([], output)
mutated_mod['func_5193'] = func_5193
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4611_call = mod.get_global_var('func_4611')
func_4613_call = mutated_mod.get_global_var('func_4613')
call_5209 = func_4611_call()
call_5210 = func_4611_call()
output = relay.Tuple([call_5209,])
output2 = relay.Tuple([call_5210,])
func_5215 = relay.Function([], output)
mod['func_5215'] = func_5215
mod = relay.transform.InferType()(mod)
mutated_mod['func_5215'] = func_5215
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5215_call = mutated_mod.get_global_var('func_5215')
call_5216 = func_5215_call()
output = call_5216
func_5217 = relay.Function([], output)
mutated_mod['func_5217'] = func_5217
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5239 = relay.var("var_5239", dtype = "float32", shape = ())#candidate|5239|()|var|float32
const_5240 = relay.const([[[-6.498176,-5.219368,-5.383738,9.162273,-4.757727,2.819374,-5.325736,3.312308,3.801354,3.471211,8.217279],[-6.892492,7.044544,4.781505,9.505993,-4.242675,-7.882267,8.456436,8.782360,1.496259,-2.978216,-0.643976],[9.537030,2.920923,-9.217093,-4.779947,5.266527,1.642712,9.219373,8.779105,8.346881,7.151404,-2.472073],[-2.728131,0.699997,8.266087,-4.855557,4.711944,3.841027,-9.644975,7.374057,-2.233113,0.776260,9.773804],[-8.687245,1.944453,0.185111,9.269739,-1.661642,8.565485,-8.454516,5.732325,-5.254763,-3.866750,-1.636219],[7.840647,2.182178,-9.497503,7.774315,0.189215,-4.742283,2.162792,7.453256,9.974587,-8.506039,-3.861915],[-6.596784,1.305367,-4.632264,-9.881733,9.168743,-5.130096,7.007484,6.861087,-0.255777,-7.696232,-8.820170],[-2.061349,0.757998,1.519574,-3.423729,-9.204308,6.124084,0.854418,9.701484,-2.811588,-4.701704,7.103210],[7.346012,-4.070373,9.436446,-1.492251,8.727802,-3.192861,9.939380,-4.246611,9.629174,-4.321870,3.281247],[-0.825617,2.107514,1.196812,1.902298,-5.106367,4.731691,-6.758220,7.555579,-4.843134,-9.729470,4.225456],[-2.779423,4.497752,-8.832864,8.821308,-4.852114,-3.907872,-5.330661,0.469821,-5.665266,5.419608,-0.349406],[2.824085,-3.327383,-5.852746,-3.380865,-9.019072,-1.361685,-9.063786,2.036834,-9.862046,7.672580,-5.921520],[-0.999120,9.563034,1.281508,-9.585466,-6.873049,5.719986,-0.579044,6.799978,-0.145060,3.862903,-8.091684],[1.457250,8.717387,6.626708,1.505724,4.748082,4.332976,-8.767321,7.069058,-2.819311,-5.580522,-4.223271]],[[-1.967018,6.633251,-5.830173,9.777962,-1.930699,-6.149651,-4.018377,-2.903676,7.576144,8.657724,-4.538306],[1.855594,-8.711619,-1.783127,-3.707543,5.391802,-2.378560,0.467607,-7.974642,8.444191,0.645128,-3.612572],[7.973954,3.200837,-8.391161,7.478162,4.345039,-3.626916,5.739607,-6.141432,-6.211077,-3.013588,7.137325],[8.918981,-3.230070,-2.437328,-2.388501,3.344973,-5.230305,4.251533,7.086938,9.507670,5.671945,-7.455370],[-5.940112,-3.717906,6.685924,-7.360634,-1.597834,-8.454534,-9.980060,1.036971,2.314135,7.014669,5.703359],[3.118297,6.629891,3.938066,-9.598917,7.797644,5.515805,8.377317,-7.946172,7.446146,7.214496,9.709838],[-0.863400,2.291760,3.732768,6.991679,3.405929,6.770347,-3.743921,2.674288,1.355946,5.906634,5.452260],[6.203369,-3.431658,-9.041153,-1.873346,-1.439940,-6.074920,-3.789985,-3.176100,5.217617,-4.335913,-9.223101],[5.836852,-9.263334,7.788830,7.670322,-5.847678,-7.310917,9.251799,8.335891,3.803833,7.810784,0.369626],[8.116219,5.601855,5.653021,-6.990111,-1.590734,9.402138,-6.806179,1.938670,7.328692,-9.672642,-1.119475],[4.003203,5.014927,8.965460,-7.549938,-8.905866,-4.498112,-2.753538,-2.711269,-5.359230,9.947705,1.890560],[-0.573588,0.093247,-9.908253,2.545074,-9.790508,-9.535722,8.007074,-8.377536,-2.468169,-2.247408,-8.806230],[-0.496308,6.096647,-7.747093,2.509983,-2.591434,-5.427842,4.888981,7.569958,5.066333,6.817667,9.164783],[-5.306452,9.334759,-5.266832,5.331962,-1.032371,0.579674,-3.804730,-4.882800,6.889287,7.617158,3.632028]],[[0.120909,-4.715135,-3.833099,-2.574941,-4.945954,6.620509,-9.675024,9.622591,-7.657313,2.094003,3.375471],[5.608621,2.586575,-4.803051,-0.276137,-0.838250,-5.907597,4.100168,-3.683438,-8.811550,-5.764711,-9.916797],[-5.926316,-7.393465,-3.311330,-4.970113,-3.303688,8.311510,3.818161,-4.316864,4.729763,6.036109,7.961380],[-7.236122,-6.970845,2.183567,-6.976583,2.079157,3.232558,-6.678666,-5.171595,-8.604273,-7.631504,-8.998311],[1.122360,-3.882511,2.094697,9.784172,-5.490346,2.881071,-1.437169,4.993187,-1.694782,7.601530,-1.133025],[5.468782,2.182483,8.380976,-3.706698,5.822145,1.868001,-0.935717,1.693173,3.196950,-1.288368,-9.579142],[7.465478,9.448605,9.076144,-5.676137,-9.494031,-4.261974,9.474903,-6.206904,9.937103,5.671307,9.931622],[-5.559106,7.039316,-9.574120,-3.549137,9.546510,-3.660020,7.985599,1.711513,9.753997,-4.069552,5.021637],[-8.321559,2.500019,6.079969,-9.149887,-4.217349,6.405194,-4.025717,9.671786,1.587590,2.298258,-2.146726],[8.655068,-2.352632,6.937876,-9.284796,-5.591223,-0.648782,-1.757068,-7.082342,-8.134828,6.493323,5.593845],[4.212308,-7.753852,2.459314,-2.844461,6.065306,7.988241,1.810339,-9.765236,-9.099804,-7.980502,-7.728606],[-5.794352,4.969059,9.509902,3.973271,-4.070004,-7.309681,6.110908,-4.906478,7.761668,0.625717,0.791726],[9.521283,-8.058561,-7.439703,4.616453,4.813002,-1.378346,-6.249297,-2.384905,-3.130340,8.037987,6.613492],[-2.973885,-0.652288,1.216503,-2.902932,-5.941612,-2.313539,5.952527,9.702076,6.507202,0.705189,2.270972]],[[-2.549395,5.509306,0.362763,6.646749,1.812613,-3.086282,3.048485,3.085512,8.538674,6.436457,-3.702716],[-6.186981,9.632040,-7.404983,8.174787,6.970746,7.224264,-8.331357,1.366730,-6.956886,2.872661,-2.353119],[-5.170886,9.291640,-2.249180,-4.189551,5.367248,-2.995330,-4.129484,3.416563,1.541291,1.641275,3.935696],[4.747511,5.837605,2.857588,-4.891381,1.906531,5.446377,-0.925419,-1.286323,-5.814902,-9.659601,-0.775685],[-3.992670,-3.532137,-1.833761,-2.091966,-4.915792,-2.649486,2.991437,-2.175298,-3.216779,8.084793,-7.447015],[6.284060,-7.601833,5.433879,-8.030042,5.559396,3.612622,-2.170239,-1.711182,-3.049795,-1.802263,-8.282511],[-1.755455,-7.643048,8.853357,1.417689,9.848210,-3.256040,-0.795865,-2.627303,4.115192,0.308150,-4.457874],[4.026365,4.870146,3.407217,-6.542087,1.914794,-4.211200,6.590974,2.812838,-8.090621,1.480339,-0.692693],[-8.563388,7.596093,6.584138,-6.185322,-3.151242,-3.632785,7.581250,-2.878386,3.960194,3.586159,3.965744],[9.739404,6.539520,7.032940,-0.474301,-0.768657,6.807504,3.946409,5.326684,-6.228381,7.780061,2.817058],[-6.422170,-2.350635,4.515715,9.722563,5.565016,-3.288124,-7.514850,7.396027,4.575280,5.823831,2.312126],[5.744740,0.493032,6.488923,-1.905759,9.210363,-7.173425,3.354545,0.244243,-8.757517,9.970994,4.128000],[-1.563735,5.172090,2.526983,-1.011623,3.442537,0.006671,4.113032,1.713144,8.836376,-9.505179,-0.481043],[3.804022,1.843997,-6.454323,-6.305061,-1.681713,1.516284,0.599689,9.890630,1.227690,6.414290,4.603477]],[[1.003286,4.852933,6.049530,-1.090864,6.665312,-7.176386,1.320135,2.728266,-7.724125,7.636347,3.008607],[-4.663255,-0.432625,9.772880,-1.210171,4.023168,1.866204,-3.675108,-4.880587,7.432706,1.343471,-3.859221],[-6.795795,-4.261841,-8.862029,-4.898948,-2.201225,-1.630471,0.303764,4.261291,-1.524069,9.266994,2.982315],[-9.416800,2.488314,4.453872,8.749027,1.547830,5.407668,6.128780,4.545866,-6.185015,-4.685274,9.109371],[-8.531865,-8.671030,2.651335,9.807060,2.306611,-1.758952,2.390527,5.101769,-5.054703,-1.027668,0.658749],[8.743154,-1.696444,-7.220461,-2.958440,-7.657993,-3.941426,2.628056,-5.800039,-7.024031,-4.885983,-4.552377],[-7.820643,8.228434,6.733531,4.982167,8.645656,4.451018,-0.140207,-7.183187,9.083113,4.930263,2.572189],[4.836035,7.778537,-1.217590,5.542395,7.759197,-7.119327,-7.115619,8.407144,-0.865307,-7.918563,-5.698818],[-3.426933,7.966652,9.827680,1.105406,3.105559,-9.185618,7.069395,-6.264752,-6.644381,-6.265453,-8.155273],[-3.466564,-4.197279,-0.575126,-8.308154,6.586364,-7.783866,1.562785,-6.948093,-2.867296,9.046005,-9.860917],[1.595775,3.822661,7.902061,0.739267,-5.460621,2.169855,-3.815676,1.876866,-3.019615,0.265887,1.308586],[-6.957674,-5.639440,8.202363,8.488908,-3.246765,8.266954,-0.930415,6.663966,-6.769859,5.434268,4.375066],[-8.374553,7.905224,7.452828,0.304653,2.353060,-1.539490,-4.751931,0.062842,-0.123670,5.010141,-2.462475],[-2.506545,2.934177,9.329270,-5.828370,-0.446319,-5.839923,1.146681,0.079683,-6.066169,-3.745643,-1.795505]],[[0.354989,-4.263906,0.203571,2.904874,-3.028865,4.333619,-8.452111,-6.698934,8.089301,7.630486,-5.431751],[-0.206489,1.033702,-1.292510,5.768754,8.215235,2.852749,-2.918524,1.365067,-9.160022,8.391350,3.090872],[-1.614422,-4.193206,-9.554988,9.753526,-9.244362,-5.475103,2.235606,4.853557,3.604589,9.468329,9.494945],[4.551329,5.685078,-0.958787,-6.517072,-9.328353,7.082014,-3.299865,3.292703,1.343650,2.224931,0.099873],[-7.815512,-4.778930,3.204012,-5.974742,2.304674,8.992439,1.626356,-1.488863,3.503050,4.756081,5.501380],[3.610759,0.679309,0.514607,-9.599886,5.204810,5.538601,8.065968,8.619799,0.641127,5.625919,6.056168],[-2.402549,-0.685444,1.376010,6.579550,-1.580067,9.481771,2.861907,-9.379745,1.297600,-7.601409,9.403283],[-3.022510,-2.954918,-1.543162,-5.941206,-3.430239,5.948382,7.450610,-8.060366,6.101736,0.053630,0.599319],[3.993283,-7.027689,8.332774,-9.031534,-2.841615,-4.867388,-6.812071,3.732546,-8.506857,-1.265049,-5.500048],[-3.405673,-5.333957,0.690647,-9.095517,-0.091789,1.262469,0.894892,2.466575,7.917787,-6.786431,-8.584138],[-4.326421,8.925166,-2.921127,-7.192346,5.214959,0.333298,5.102819,2.842009,8.039903,3.876363,8.127815],[-7.903324,-9.904640,-2.040245,9.723675,-1.398359,-3.339764,-0.642902,8.965499,-1.298892,-0.598976,-2.927586],[-2.769071,8.612866,5.386137,-6.900292,6.295859,0.839189,5.966963,-8.787638,9.458562,-7.619457,2.797400],[-2.915107,-8.654830,7.311286,-3.530168,-7.047232,-8.529511,1.076035,-3.512230,-3.760931,-1.372936,-2.978595]],[[7.513801,-7.839166,4.083835,9.085932,2.641263,5.347484,-2.786104,-6.499078,-7.868358,6.566184,0.207378],[-8.237553,4.827193,5.080064,-3.797776,6.885490,1.168464,-2.490264,-1.549924,3.616774,6.878964,3.294473],[7.625292,2.096015,-4.897396,-5.639917,5.535887,-1.003216,1.178412,-1.544839,7.616138,-0.985217,9.660249],[1.767769,-7.818118,7.015604,1.506471,6.933253,5.899214,-5.848451,7.215483,1.451106,2.520797,9.824617],[3.285640,-8.401439,3.961960,1.428478,-0.968022,2.538074,8.466835,-9.619696,6.219444,-1.709178,-9.494210],[1.010028,7.559449,-0.546519,-7.377969,-2.160148,3.865714,-9.378600,1.541269,9.166152,-2.920024,-6.209236],[-0.435596,-6.117796,-7.732830,-8.184294,2.117666,-3.635228,-7.341966,4.405908,1.811299,-2.356180,-4.197189],[9.281735,8.228353,3.106315,1.172771,0.494378,2.285589,-9.985883,-2.259034,-8.534214,-3.596356,0.144112],[-5.856772,7.308805,-1.239879,-5.999228,-6.178970,-3.014002,2.369988,8.682458,6.713270,-3.107354,-9.913312],[-1.810908,7.171050,-2.183663,9.389900,-9.995547,-0.529412,1.087533,5.075880,3.402858,-9.687114,1.344143],[-7.246538,-7.072545,-7.835819,-2.207356,4.899370,6.931338,7.506283,-3.760218,0.371108,-2.233719,-6.819594],[-1.538501,-3.595670,8.793689,7.734696,-2.209317,0.765524,6.935514,3.660324,-3.954531,-6.560461,3.892422],[0.719655,2.414797,-0.739967,-9.992741,6.206301,-1.475617,5.970415,-6.666945,4.870095,-2.060733,-5.583952],[-6.601709,7.894872,-3.832018,-2.405254,4.866888,-1.340697,2.901634,5.487108,0.446066,-6.159684,-4.482050]]], dtype = "float32")#candidate|5240|(7, 14, 11)|const|float32
bop_5241 = relay.less_equal(var_5239.astype('bool'), const_5240.astype('bool')) # shape=(7, 14, 11)
uop_5258 = relay.acos(const_5240.astype('float32')) # shape=(7, 14, 11)
func_4637_call = mod.get_global_var('func_4637')
func_4638_call = mutated_mod.get_global_var('func_4638')
call_5262 = relay.TupleGetItem(func_4637_call(), 0)
call_5263 = relay.TupleGetItem(func_4638_call(), 0)
func_5192_call = mod.get_global_var('func_5192')
func_5193_call = mutated_mod.get_global_var('func_5193')
call_5290 = func_5192_call()
call_5291 = func_5192_call()
func_3670_call = mod.get_global_var('func_3670')
func_3674_call = mutated_mod.get_global_var('func_3674')
const_5301 = relay.const([-2,6,-1,-10,-8,1,8,1,-2,4,6,-4,-3,-8,-8,10,1,9,-2,8,5,-5,9,7,-7,-5,-8,3,-1,-6,1,7,4,5,-5,8,-2,5,3,3,2,10,-8,-3,5,6,-5,-9,2,-5,-6,-9,7,10,-5,-9,-4,6,3,8,9,5,10,-3,7,9,2,-4,1,9,8,10,-7,1,-6,-10,-5,-6,-7,7,-6,9,-2,7,6,9,3,5,8,10,7,6,4,-6,3,-7,10,9,9,-7,-1,9,8,4,2,-9,-5,-2,10,-10,-3,-2,-2,-5,6,-6,-10,10,10,5,1,4,10,-7,-6,-3,-3,-2,-7,-8,10,-1,10,2,7,-4,1,6,-4,2,-9,8,2,-9,-8,-2,-10,1,-4,9,-10,2,1,-5,-1,4,1,-4,-2,4,9,-10,-8,-10,-6,8,2,-9,7,9,-10,8,4,6,4,-6,5,3,-9,-8,1,-10,5,9,3,10,10,-5,-1,-10,3,9,4,-1,-6,-9,-4,-2,-8,1,-9,-5,10,-3,4,-7,9,-3,7,-7,3,-9,-5,-6,-4,-6,-7,-3,-2,-9,8,-3,1,2,-10,-2,-3,9,-4,10,-1,2,-9,6,-9,-10,-10,-4,9,-10], dtype = "uint32")#candidate|5301|(240,)|const|uint32
call_5300 = relay.TupleGetItem(func_3670_call(relay.reshape(call_5290.astype('float64'), [7, 16, 7]), relay.reshape(const_5301.astype('uint32'), [240,]), ), 0)
call_5302 = relay.TupleGetItem(func_3674_call(relay.reshape(call_5290.astype('float64'), [7, 16, 7]), relay.reshape(const_5301.astype('uint32'), [240,]), ), 0)
func_2721_call = mod.get_global_var('func_2721')
func_2725_call = mutated_mod.get_global_var('func_2725')
var_5304 = relay.var("var_5304", dtype = "uint16", shape = (864,))#candidate|5304|(864,)|var|uint16
call_5303 = func_2721_call(relay.reshape(var_5239.astype('uint16'), []), relay.reshape(var_5304.astype('uint16'), [12, 6, 12]), )
call_5305 = func_2721_call(relay.reshape(var_5239.astype('uint16'), []), relay.reshape(var_5304.astype('uint16'), [12, 6, 12]), )
output = relay.Tuple([bop_5241,uop_5258,call_5262,call_5290,call_5300,const_5301,call_5303,var_5304,])
output2 = relay.Tuple([bop_5241,uop_5258,call_5263,call_5291,call_5302,const_5301,call_5305,var_5304,])
func_5312 = relay.Function([var_5239,var_5304,], output)
mod['func_5312'] = func_5312
mod = relay.transform.InferType()(mod)
var_5313 = relay.var("var_5313", dtype = "float32", shape = ())#candidate|5313|()|var|float32
var_5314 = relay.var("var_5314", dtype = "uint16", shape = (864,))#candidate|5314|(864,)|var|uint16
output = func_5312(var_5313,var_5314,)
func_5315 = relay.Function([var_5313,var_5314,], output)
mutated_mod['func_5315'] = func_5315
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4510_call = mod.get_global_var('func_4510')
func_4512_call = mutated_mod.get_global_var('func_4512')
call_5328 = relay.TupleGetItem(func_4510_call(), 3)
call_5329 = relay.TupleGetItem(func_4512_call(), 3)
output = relay.Tuple([call_5328,])
output2 = relay.Tuple([call_5329,])
func_5336 = relay.Function([], output)
mod['func_5336'] = func_5336
mod = relay.transform.InferType()(mod)
output = func_5336()
func_5337 = relay.Function([], output)
mutated_mod['func_5337'] = func_5337
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5215_call = mod.get_global_var('func_5215')
func_5217_call = mutated_mod.get_global_var('func_5217')
call_5386 = relay.TupleGetItem(func_5215_call(), 0)
call_5387 = relay.TupleGetItem(func_5217_call(), 0)
func_4772_call = mod.get_global_var('func_4772')
func_4773_call = mutated_mod.get_global_var('func_4773')
call_5404 = relay.TupleGetItem(func_4772_call(), 1)
call_5405 = relay.TupleGetItem(func_4773_call(), 1)
uop_5408 = relay.atan(call_5404.astype('float32')) # shape=(11, 12, 11)
uop_5410 = relay.atan(call_5405.astype('float32')) # shape=(11, 12, 11)
func_1019_call = mod.get_global_var('func_1019')
func_1023_call = mutated_mod.get_global_var('func_1023')
var_5413 = relay.var("var_5413", dtype = "uint8", shape = (432,))#candidate|5413|(432,)|var|uint8
call_5412 = func_1019_call(relay.reshape(var_5413.astype('uint8'), [6, 12, 6]), relay.reshape(var_5413.astype('uint8'), [6, 12, 6]), )
call_5414 = func_1019_call(relay.reshape(var_5413.astype('uint8'), [6, 12, 6]), relay.reshape(var_5413.astype('uint8'), [6, 12, 6]), )
func_5312_call = mod.get_global_var('func_5312')
func_5315_call = mutated_mod.get_global_var('func_5315')
var_5417 = relay.var("var_5417", dtype = "float32", shape = ())#candidate|5417|()|var|float32
var_5418 = relay.var("var_5418", dtype = "uint16", shape = (864,))#candidate|5418|(864,)|var|uint16
call_5416 = relay.TupleGetItem(func_5312_call(relay.reshape(var_5417.astype('float32'), []), relay.reshape(var_5418.astype('uint16'), [864,]), ), 4)
call_5419 = relay.TupleGetItem(func_5315_call(relay.reshape(var_5417.astype('float32'), []), relay.reshape(var_5418.astype('uint16'), [864,]), ), 4)
func_5312_call = mod.get_global_var('func_5312')
func_5315_call = mutated_mod.get_global_var('func_5315')
call_5429 = relay.TupleGetItem(func_5312_call(relay.reshape(var_5417.astype('float32'), []), relay.reshape(var_5418.astype('uint16'), [864,]), ), 3)
call_5430 = relay.TupleGetItem(func_5315_call(relay.reshape(var_5417.astype('float32'), []), relay.reshape(var_5418.astype('uint16'), [864,]), ), 3)
func_5215_call = mod.get_global_var('func_5215')
func_5217_call = mutated_mod.get_global_var('func_5217')
call_5433 = relay.TupleGetItem(func_5215_call(), 0)
call_5434 = relay.TupleGetItem(func_5217_call(), 0)
uop_5437 = relay.rsqrt(call_5416.astype('float32')) # shape=(7, 16, 7)
uop_5439 = relay.rsqrt(call_5419.astype('float32')) # shape=(7, 16, 7)
uop_5452 = relay.sqrt(uop_5437.astype('float64')) # shape=(7, 16, 7)
uop_5454 = relay.sqrt(uop_5439.astype('float64')) # shape=(7, 16, 7)
output = relay.Tuple([call_5386,uop_5408,call_5412,var_5413,var_5417,var_5418,call_5429,call_5433,uop_5452,])
output2 = relay.Tuple([call_5387,uop_5410,call_5414,var_5413,var_5417,var_5418,call_5430,call_5434,uop_5454,])
func_5468 = relay.Function([var_5413,var_5417,var_5418,], output)
mod['func_5468'] = func_5468
mod = relay.transform.InferType()(mod)
mutated_mod['func_5468'] = func_5468
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5468_call = mutated_mod.get_global_var('func_5468')
var_5470 = relay.var("var_5470", dtype = "uint8", shape = (432,))#candidate|5470|(432,)|var|uint8
var_5471 = relay.var("var_5471", dtype = "float32", shape = ())#candidate|5471|()|var|float32
var_5472 = relay.var("var_5472", dtype = "uint16", shape = (864,))#candidate|5472|(864,)|var|uint16
call_5469 = func_5468_call(var_5470,var_5471,var_5472,)
output = call_5469
func_5473 = relay.Function([var_5470,var_5471,var_5472,], output)
mutated_mod['func_5473'] = func_5473
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5538 = relay.var("var_5538", dtype = "float64", shape = (1, 4, 12))#candidate|5538|(1, 4, 12)|var|float64
uop_5539 = relay.erf(var_5538.astype('float64')) # shape=(1, 4, 12)
func_4581_call = mod.get_global_var('func_4581')
func_4582_call = mutated_mod.get_global_var('func_4582')
call_5542 = relay.TupleGetItem(func_4581_call(), 4)
call_5543 = relay.TupleGetItem(func_4582_call(), 4)
output = relay.Tuple([uop_5539,call_5542,])
output2 = relay.Tuple([uop_5539,call_5543,])
func_5563 = relay.Function([var_5538,], output)
mod['func_5563'] = func_5563
mod = relay.transform.InferType()(mod)
var_5564 = relay.var("var_5564", dtype = "float64", shape = (1, 4, 12))#candidate|5564|(1, 4, 12)|var|float64
output = func_5563(var_5564)
func_5565 = relay.Function([var_5564], output)
mutated_mod['func_5565'] = func_5565
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5583 = relay.var("var_5583", dtype = "float64", shape = (7, 4, 4))#candidate|5583|(7, 4, 4)|var|float64
var_5584 = relay.var("var_5584", dtype = "float64", shape = (7, 4, 4))#candidate|5584|(7, 4, 4)|var|float64
bop_5585 = relay.floor_divide(var_5583.astype('float64'), relay.reshape(var_5584.astype('float64'), relay.shape_of(var_5583))) # shape=(7, 4, 4)
output = bop_5585
output2 = bop_5585
func_5592 = relay.Function([var_5583,var_5584,], output)
mod['func_5592'] = func_5592
mod = relay.transform.InferType()(mod)
var_5593 = relay.var("var_5593", dtype = "float64", shape = (7, 4, 4))#candidate|5593|(7, 4, 4)|var|float64
var_5594 = relay.var("var_5594", dtype = "float64", shape = (7, 4, 4))#candidate|5594|(7, 4, 4)|var|float64
output = func_5592(var_5593,var_5594,)
func_5595 = relay.Function([var_5593,var_5594,], output)
mutated_mod['func_5595'] = func_5595
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4510_call = mod.get_global_var('func_4510')
func_4512_call = mutated_mod.get_global_var('func_4512')
call_5714 = relay.TupleGetItem(func_4510_call(), 2)
call_5715 = relay.TupleGetItem(func_4512_call(), 2)
output = relay.Tuple([call_5714,])
output2 = relay.Tuple([call_5715,])
func_5716 = relay.Function([], output)
mod['func_5716'] = func_5716
mod = relay.transform.InferType()(mod)
mutated_mod['func_5716'] = func_5716
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5716_call = mutated_mod.get_global_var('func_5716')
call_5717 = func_5716_call()
output = call_5717
func_5718 = relay.Function([], output)
mutated_mod['func_5718'] = func_5718
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5745 = relay.const([[[-4.426577,6.851507,7.551983,2.912966,-5.036156,4.835337,3.568867,7.829299,-3.772267,-4.914639]],[[5.750622,0.927960,-6.291352,-1.581243,2.272709,-0.697198,-3.684136,6.515892,3.621122,-1.275404]],[[2.581675,9.965801,-8.014249,-0.709149,0.070344,0.697285,0.443239,-8.142770,-0.840877,3.868325]],[[-3.008510,0.807393,0.123199,-0.963060,5.758847,-1.540596,-8.384221,9.313623,-7.874011,8.951734]],[[-3.293445,8.398912,6.727363,9.144673,-2.106228,-9.509710,-2.354730,8.504701,-8.663441,-6.895639]],[[6.345914,-9.781775,-8.935878,-1.169838,5.626456,-9.760168,-5.071960,-5.369579,4.316133,6.426502]],[[-5.075888,-9.751853,2.835729,-6.267787,8.470153,8.805436,7.449175,-9.586357,4.726481,3.927459]],[[-9.755308,-3.898971,7.433965,2.416168,-2.675939,-9.286190,-8.405461,8.231858,-8.401034,3.266171]],[[5.215790,-9.851155,-1.473884,-7.145536,0.936469,-4.367396,-3.151763,6.370811,8.443989,-7.291475]],[[6.558743,-0.670848,-2.278091,-3.223384,6.983890,-6.985593,-8.088160,-5.638704,-4.188528,9.675872]],[[-3.743284,1.696034,-6.222840,-6.215627,0.994808,-1.090167,6.254393,-4.872297,-2.576652,-4.947325]],[[-9.390935,-7.443100,-1.651771,3.842586,-6.820749,-0.343781,9.640782,5.890280,-2.489789,6.134764]],[[-8.563658,6.782227,9.554610,5.077855,-2.825880,1.476691,7.545761,4.614766,-4.399720,-8.211118]],[[3.523811,6.888296,-5.799810,3.647700,-0.558845,3.146486,-4.847146,-7.323011,-8.772917,0.498038]],[[-2.244647,-6.288045,8.342858,4.472256,-0.451690,-9.402738,-4.014957,-6.364141,-9.570842,-1.399649]],[[3.002615,0.372627,-6.109386,8.624590,-1.399504,6.161129,8.202778,-5.210347,2.031003,4.322373]]], dtype = "float32")#candidate|5745|(16, 1, 10)|const|float32
var_5746 = relay.var("var_5746", dtype = "float32", shape = (16, 3, 10))#candidate|5746|(16, 3, 10)|var|float32
bop_5747 = relay.floor_mod(const_5745.astype('float32'), var_5746.astype('float32')) # shape=(16, 3, 10)
uop_5752 = relay.cos(bop_5747.astype('float64')) # shape=(16, 3, 10)
output = uop_5752
output2 = uop_5752
func_5759 = relay.Function([var_5746,], output)
mod['func_5759'] = func_5759
mod = relay.transform.InferType()(mod)
var_5760 = relay.var("var_5760", dtype = "float32", shape = (16, 3, 10))#candidate|5760|(16, 3, 10)|var|float32
output = func_5759(var_5760)
func_5761 = relay.Function([var_5760], output)
mutated_mod['func_5761'] = func_5761
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4853_call = mod.get_global_var('func_4853')
func_4855_call = mutated_mod.get_global_var('func_4855')
call_5772 = relay.TupleGetItem(func_4853_call(), 2)
call_5773 = relay.TupleGetItem(func_4855_call(), 2)
output = relay.Tuple([call_5772,])
output2 = relay.Tuple([call_5773,])
func_5774 = relay.Function([], output)
mod['func_5774'] = func_5774
mod = relay.transform.InferType()(mod)
output = func_5774()
func_5775 = relay.Function([], output)
mutated_mod['func_5775'] = func_5775
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5215_call = mod.get_global_var('func_5215')
func_5217_call = mutated_mod.get_global_var('func_5217')
call_5824 = relay.TupleGetItem(func_5215_call(), 0)
call_5825 = relay.TupleGetItem(func_5217_call(), 0)
uop_5830 = relay.sigmoid(call_5824.astype('float64')) # shape=(7, 16, 7)
uop_5832 = relay.sigmoid(call_5825.astype('float64')) # shape=(7, 16, 7)
output = relay.Tuple([uop_5830,])
output2 = relay.Tuple([uop_5832,])
func_5841 = relay.Function([], output)
mod['func_5841'] = func_5841
mod = relay.transform.InferType()(mod)
output = func_5841()
func_5842 = relay.Function([], output)
mutated_mod['func_5842'] = func_5842
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4980_call = mod.get_global_var('func_4980')
func_4982_call = mutated_mod.get_global_var('func_4982')
call_5850 = relay.TupleGetItem(func_4980_call(), 0)
call_5851 = relay.TupleGetItem(func_4982_call(), 0)
output = call_5850
output2 = call_5851
func_5852 = relay.Function([], output)
mod['func_5852'] = func_5852
mod = relay.transform.InferType()(mod)
output = func_5852()
func_5853 = relay.Function([], output)
mutated_mod['func_5853'] = func_5853
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5854 = relay.var("var_5854", dtype = "float32", shape = (11, 10, 5))#candidate|5854|(11, 10, 5)|var|float32
const_5855 = relay.const([[[-4.891566,-5.582277,-1.410751,8.706678,3.233134],[8.821250,1.007959,2.215117,-2.321415,4.395380],[-4.816216,-8.896495,8.876080,1.773653,8.679251],[-9.333941,-1.990334,-8.622918,3.316758,5.684179],[-8.851818,6.162403,4.416769,-3.799337,4.469870],[-3.880639,-1.368966,-1.024867,-8.224686,-1.091653],[-9.679638,4.174708,6.786767,-9.684455,1.578607],[6.578638,-3.067260,-4.029385,1.489171,1.349404],[-6.357018,-8.609150,-2.717047,-7.805136,-7.667296],[2.534370,-3.384808,2.769404,-9.633124,-7.344026]],[[-9.982861,-2.631964,-9.189217,-6.696103,8.959077],[-5.887276,0.378488,-4.649886,-3.263139,-2.523530],[9.251169,3.863474,1.562286,7.877836,-8.665868],[2.836921,-6.055019,5.997291,-3.414465,-5.956858],[-1.367326,8.387491,-7.098637,3.469799,6.358748],[7.631231,3.745122,-7.628444,-2.736111,3.431623],[3.911348,6.293435,-1.959109,-6.570463,-5.191470],[-5.597329,-9.570119,-3.757008,9.943272,7.224866],[1.696209,7.610976,2.007273,7.376386,9.115223],[1.063469,-8.163898,-4.269947,9.461183,1.352201]],[[-8.992257,-5.101013,-0.974749,3.497451,8.290802],[-8.495427,8.775508,6.096469,0.587115,-1.420016],[2.307335,0.536854,-2.146584,-0.014362,-0.734734],[8.054258,8.803098,5.682503,-4.702812,0.178624],[5.448112,8.527883,1.595990,-2.932837,5.538290],[-8.748742,-1.460698,-4.572185,5.429519,-1.184664],[4.327579,-4.041133,-0.576058,-3.259348,-7.145721],[-1.374902,1.621305,7.966006,-0.468746,9.211470],[-8.183688,8.751534,6.642405,-8.334928,-4.810920],[-4.635365,-5.397926,4.033950,6.765509,-0.863700]],[[2.593754,0.030127,-5.199961,-6.432974,-6.522593],[-8.972475,2.614006,7.176602,-6.047255,7.707903],[5.164416,-5.313368,7.632274,-1.776627,1.729008],[-7.715630,4.635113,5.685190,-7.590134,-1.029076],[8.145566,-1.807535,-7.257760,8.024880,0.766732],[-3.107209,-1.861509,-6.710172,-6.443598,-0.261375],[2.931550,-7.257758,8.545152,-9.835602,2.429440],[-3.161141,-4.093266,5.343177,8.982522,4.306059],[-1.156777,2.316502,-9.199797,-4.107021,-6.312465],[-8.737263,1.571687,-4.196010,-2.208081,5.908077]],[[9.813552,-9.607215,-8.058615,1.875533,-0.890236],[-7.632843,-6.105074,7.161961,3.196439,0.018491],[2.171909,-6.814196,-6.496676,6.858341,2.640347],[8.006565,-2.621284,-5.279779,0.858125,-4.157843],[-3.033843,-6.227982,-7.995390,1.648010,0.167361],[3.057205,-1.373877,-0.355125,-5.522239,4.983080],[-8.019564,0.912365,-7.123083,7.456347,7.076966],[2.071800,-4.169106,-3.303870,-2.624772,-4.187584],[-0.829088,-5.945442,8.743717,4.882285,-0.846707],[-5.579171,1.343778,0.343417,5.448392,-7.609095]],[[3.371379,6.804092,6.879375,-7.690471,8.172079],[-7.382123,9.275537,6.482642,3.833795,-8.208424],[6.306643,-1.540417,-0.528979,3.309213,-9.925333],[-2.230067,1.197259,9.560163,5.464221,-2.185375],[-8.347436,-1.682927,2.416498,3.703479,3.753665],[-8.574682,-1.975446,9.788369,8.423883,-3.019841],[-2.806245,5.859699,-8.274031,3.498856,-6.907529],[8.991602,-1.631232,-2.438661,3.800049,-2.785823],[-6.831671,9.092422,8.613831,9.688580,4.233665],[-5.412809,7.643201,-6.635737,-9.571271,4.007685]],[[4.310258,0.674127,4.538782,-4.452044,6.712164],[5.731581,4.726940,-4.891937,1.988246,5.785990],[-9.507501,0.658595,2.270356,8.770420,3.691959],[8.794343,7.379073,-4.557763,-6.720760,3.553322],[3.923013,0.065028,-7.646623,2.581847,-5.156008],[-0.782468,-9.565058,-5.421594,2.896886,2.947383],[-9.657542,-2.343436,5.333141,-6.438325,3.106325],[-3.672314,-8.533677,5.847603,7.332044,0.967808],[-6.326642,-9.107447,1.175586,-2.590779,4.974473],[0.930847,-8.644933,1.316598,-0.402062,-8.461806]],[[-3.003587,-4.560702,-3.005009,0.354672,-3.269331],[7.638389,-9.165238,5.369125,-5.888954,6.995307],[8.960979,-9.450024,-1.020016,9.791281,9.247513],[-9.511282,-5.111377,2.761317,-0.611621,2.405493],[6.846122,2.122667,-5.872177,0.931199,3.486707],[-8.677443,3.041448,-9.634200,7.669331,-5.564245],[5.339330,-9.916808,7.954510,8.111322,-6.125963],[-1.801365,9.462470,0.426190,-4.256726,9.783693],[6.484306,-2.824889,-6.877371,-3.221890,-8.673793],[-9.207915,2.356871,-7.602990,-6.063643,0.580276]],[[-0.386516,-0.601814,8.948406,8.283279,-1.860163],[6.236767,0.033238,-9.103129,3.721145,1.846995],[7.879133,5.703571,-0.122560,4.083847,0.063596],[8.703041,-9.304930,-7.018645,3.722156,9.485344],[-0.647741,-4.480382,-0.505830,1.384629,0.978436],[-1.368144,-2.160294,-2.295962,6.852861,-5.804389],[-6.275791,-1.646857,4.330900,-1.149843,-5.057987],[0.449464,6.058618,-1.226026,-8.078188,5.118501],[-7.504639,4.431896,2.982316,1.355935,1.157423],[-0.802103,8.809083,1.900269,8.149932,-9.337864]],[[7.465440,-9.605090,1.123772,3.105119,-4.726700],[2.656236,-9.390434,0.720103,-8.760235,-8.466638],[-7.559262,4.275312,1.207027,8.551753,6.104024],[-6.964890,2.661602,5.190255,-5.151355,-2.955088],[7.685176,0.610580,-2.773451,0.359090,-5.334647],[2.923293,-7.352861,-4.292465,5.077689,-8.444735],[3.672058,0.100679,0.593385,3.629096,2.993091],[-3.150247,-8.155838,-7.416350,0.560693,3.924558],[8.604445,-8.056912,-1.750300,7.168596,-2.088069],[-8.414326,1.839452,-4.363323,-9.739326,-7.651627]],[[-1.959243,-4.341303,-4.543310,8.474580,-0.008836],[4.577474,8.856332,-1.667050,4.645316,0.186970],[7.039521,8.184050,-7.516015,-7.700032,-0.435227],[-0.816805,1.224591,2.067139,-3.362943,7.212326],[7.455538,-2.676433,9.935720,-0.127411,5.400121],[-7.259672,5.851612,6.757592,-7.993003,-9.128165],[-2.472272,4.109852,9.042119,0.174867,9.924203],[0.481592,-7.969536,-6.104940,-7.675685,-4.834983],[-4.268425,-9.850157,-6.061080,5.691446,5.396675],[5.067537,4.532505,-4.584729,9.111894,-0.347125]]], dtype = "float32")#candidate|5855|(11, 10, 5)|const|float32
bop_5856 = relay.mod(var_5854.astype('float32'), relay.reshape(const_5855.astype('float32'), relay.shape_of(var_5854))) # shape=(11, 10, 5)
output = bop_5856
output2 = bop_5856
func_5861 = relay.Function([var_5854,], output)
mod['func_5861'] = func_5861
mod = relay.transform.InferType()(mod)
var_5862 = relay.var("var_5862", dtype = "float32", shape = (11, 10, 5))#candidate|5862|(11, 10, 5)|var|float32
output = func_5861(var_5862)
func_5863 = relay.Function([var_5862], output)
mutated_mod['func_5863'] = func_5863
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5841_call = mod.get_global_var('func_5841')
func_5842_call = mutated_mod.get_global_var('func_5842')
call_5893 = relay.TupleGetItem(func_5841_call(), 0)
call_5894 = relay.TupleGetItem(func_5842_call(), 0)
func_4684_call = mod.get_global_var('func_4684')
func_4687_call = mutated_mod.get_global_var('func_4687')
var_5902 = relay.var("var_5902", dtype = "float32", shape = (504, 2))#candidate|5902|(504, 2)|var|float32
call_5901 = relay.TupleGetItem(func_4684_call(relay.reshape(var_5902.astype('float32'), [16, 7, 9])), 0)
call_5903 = relay.TupleGetItem(func_4687_call(relay.reshape(var_5902.astype('float32'), [16, 7, 9])), 0)
bop_5904 = relay.bitwise_or(var_5902.astype('uint64'), relay.reshape(call_5901.astype('uint64'), relay.shape_of(var_5902))) # shape=(504, 2)
bop_5907 = relay.bitwise_or(var_5902.astype('uint64'), relay.reshape(call_5903.astype('uint64'), relay.shape_of(var_5902))) # shape=(504, 2)
uop_5908 = relay.atan(bop_5904.astype('float32')) # shape=(504, 2)
uop_5910 = relay.atan(bop_5907.astype('float32')) # shape=(504, 2)
bop_5911 = relay.minimum(call_5901.astype('uint64'), relay.reshape(uop_5908.astype('uint64'), relay.shape_of(call_5901))) # shape=(16, 7, 9)
bop_5914 = relay.minimum(call_5903.astype('uint64'), relay.reshape(uop_5910.astype('uint64'), relay.shape_of(call_5903))) # shape=(16, 7, 9)
bop_5924 = relay.right_shift(uop_5908.astype('uint16'), relay.reshape(call_5901.astype('uint16'), relay.shape_of(uop_5908))) # shape=(504, 2)
bop_5927 = relay.right_shift(uop_5910.astype('uint16'), relay.reshape(call_5903.astype('uint16'), relay.shape_of(uop_5910))) # shape=(504, 2)
output = relay.Tuple([call_5893,bop_5911,bop_5924,])
output2 = relay.Tuple([call_5894,bop_5914,bop_5927,])
func_5933 = relay.Function([var_5902,], output)
mod['func_5933'] = func_5933
mod = relay.transform.InferType()(mod)
mutated_mod['func_5933'] = func_5933
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5934 = relay.var("var_5934", dtype = "float32", shape = (504, 2))#candidate|5934|(504, 2)|var|float32
func_5933_call = mutated_mod.get_global_var('func_5933')
call_5935 = func_5933_call(var_5934)
output = call_5935
func_5936 = relay.Function([var_5934], output)
mutated_mod['func_5936'] = func_5936
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4853_call = mod.get_global_var('func_4853')
func_4855_call = mutated_mod.get_global_var('func_4855')
call_5953 = relay.TupleGetItem(func_4853_call(), 2)
call_5954 = relay.TupleGetItem(func_4855_call(), 2)
func_5096_call = mod.get_global_var('func_5096')
func_5099_call = mutated_mod.get_global_var('func_5099')
var_5965 = relay.var("var_5965", dtype = "int8", shape = (1050,))#candidate|5965|(1050,)|var|int8
const_5966 = relay.const([5,8,-7,-10,10,9,6,10,-2,-10,-8,-1,4,7,1,-1,-2,-2,5,-3,-9,-7,-8,-10,1,-1,3,-9,-1,-8,-4,3,-10,-6,6,-2,-4,1,-7,-4,-1,1,-9,2,9,-6,-9,-9,-3,-5,-6,5,5,-4,7,3,5,3,-4,-7,2,-6,-10,3,-1,2,5,-9,-3,3,1,1,1,1,8,-10,9,5,-10,5,-5,3,4,10,-7,1,-10,5,6,-7,-3,-7,3,-6,-8,-6,-7,3,-3,3,8,7,6,-9,7,9,3,4,7,10,-10,8,-7,1,6,9,7,1,-7,8,-6,-6,4,-6,-2,6,-5,9,7,-2,-3,-6,9,6,8,2,2,3,-1,-6,-5,5,7,4,6,-7,-8,-1,-2,3,-2,2,-6,-1,5,-8,-10,-2,8,10,-1,3,4,6,-3,-4,5,-1,4,-6,9,-1,10,5,9,-2,-4,2,10,-4,7,8,-7,-3,-2,9,-4,10,6,-1,-1,-7,-7,3,-7,10,6,-5,8,-1,6,10,10,5,-5,3,9,-1,9,4,10,1,2,6,-4,8,8,-4,-10,-6,-7,-1,9,5,-7,-5,2,2,9,-4,8,5,-4,4,-9,-10,-9,3,4,-5,6,9,-3,-4,10,9,3,-4,4,10,-2,8,-3,9,-8,10,4,1,-10,-2,-4,10,5,-4,-6,2,7,9,-10,1,3,-1,-1,-4,9,5,7,3,-1,-10,-1,7,10,-2,-4,-8,6,-4,4,-10,-4,-6,-2,2,6,-2,-4,-7,-5,-7,-3,8,6,6,1,-3,-3,-7,-8,10,-3,-10,-3,3,7,-9,-7,-2,2,-3,6,-10,-4,5,8,-7,10,-9,-6,1,4,-8,8,6,-7,-2,6,5,-1,-4,-8,1,8,-10,-2,-10,2,9,-7,1,5,-9,9,1,-4,10,-5,1,1,-10,2,-1,-7,8,5,-9,7,1,2,6,8,10,-7,7,-10,-4,6,-1,-6,-10,-10,-3,-5,-1,-8,-4,4,-10,-3,-10,-3,-9,10,5,-9,-10,3,6,-10,6,-5,-4,2,-10,2,-10,-6,7,7,3,8,6,9,-9,8,-6,-6,2,6,-3,-1,7,-1,3,-6,-5,2,-6,-3,9,-10,6], dtype = "uint8")#candidate|5966|(432,)|const|uint8
call_5964 = relay.TupleGetItem(func_5096_call(relay.reshape(var_5965.astype('int8'), [70, 15]), relay.reshape(const_5966.astype('uint8'), [432,]), ), 3)
call_5967 = relay.TupleGetItem(func_5099_call(relay.reshape(var_5965.astype('int8'), [70, 15]), relay.reshape(const_5966.astype('uint8'), [432,]), ), 3)
output = relay.Tuple([call_5953,call_5964,var_5965,const_5966,])
output2 = relay.Tuple([call_5954,call_5967,var_5965,const_5966,])
func_5981 = relay.Function([var_5965,], output)
mod['func_5981'] = func_5981
mod = relay.transform.InferType()(mod)
mutated_mod['func_5981'] = func_5981
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5982 = relay.var("var_5982", dtype = "int8", shape = (1050,))#candidate|5982|(1050,)|var|int8
func_5981_call = mutated_mod.get_global_var('func_5981')
call_5983 = func_5981_call(var_5982)
output = call_5983
func_5984 = relay.Function([var_5982], output)
mutated_mod['func_5984'] = func_5984
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4772_call = mod.get_global_var('func_4772')
func_4773_call = mutated_mod.get_global_var('func_4773')
call_6070 = relay.TupleGetItem(func_4772_call(), 2)
call_6071 = relay.TupleGetItem(func_4773_call(), 2)
func_4772_call = mod.get_global_var('func_4772')
func_4773_call = mutated_mod.get_global_var('func_4773')
call_6077 = relay.TupleGetItem(func_4772_call(), 0)
call_6078 = relay.TupleGetItem(func_4773_call(), 0)
output = relay.Tuple([call_6070,call_6077,])
output2 = relay.Tuple([call_6071,call_6078,])
func_6083 = relay.Function([], output)
mod['func_6083'] = func_6083
mod = relay.transform.InferType()(mod)
mutated_mod['func_6083'] = func_6083
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6083_call = mutated_mod.get_global_var('func_6083')
call_6084 = func_6083_call()
output = call_6084
func_6085 = relay.Function([], output)
mutated_mod['func_6085'] = func_6085
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4581_call = mod.get_global_var('func_4581')
func_4582_call = mutated_mod.get_global_var('func_4582')
call_6097 = relay.TupleGetItem(func_4581_call(), 1)
call_6098 = relay.TupleGetItem(func_4582_call(), 1)
func_5774_call = mod.get_global_var('func_5774')
func_5775_call = mutated_mod.get_global_var('func_5775')
call_6103 = relay.TupleGetItem(func_5774_call(), 0)
call_6104 = relay.TupleGetItem(func_5775_call(), 0)
func_4637_call = mod.get_global_var('func_4637')
func_4638_call = mutated_mod.get_global_var('func_4638')
call_6115 = relay.TupleGetItem(func_4637_call(), 0)
call_6116 = relay.TupleGetItem(func_4638_call(), 0)
output = relay.Tuple([call_6097,call_6103,call_6115,])
output2 = relay.Tuple([call_6098,call_6104,call_6116,])
func_6119 = relay.Function([], output)
mod['func_6119'] = func_6119
mod = relay.transform.InferType()(mod)
output = func_6119()
func_6120 = relay.Function([], output)
mutated_mod['func_6120'] = func_6120
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4510_call = mod.get_global_var('func_4510')
func_4512_call = mutated_mod.get_global_var('func_4512')
call_6162 = relay.TupleGetItem(func_4510_call(), 2)
call_6163 = relay.TupleGetItem(func_4512_call(), 2)
func_4853_call = mod.get_global_var('func_4853')
func_4855_call = mutated_mod.get_global_var('func_4855')
call_6165 = relay.TupleGetItem(func_4853_call(), 2)
call_6166 = relay.TupleGetItem(func_4855_call(), 2)
var_6186 = relay.var("var_6186", dtype = "float64", shape = (7, 16, 7))#candidate|6186|(7, 16, 7)|var|float64
bop_6187 = relay.right_shift(call_6165.astype('uint8'), relay.reshape(var_6186.astype('uint8'), relay.shape_of(call_6165))) # shape=(7, 16, 7)
bop_6190 = relay.right_shift(call_6166.astype('uint8'), relay.reshape(var_6186.astype('uint8'), relay.shape_of(call_6166))) # shape=(7, 16, 7)
output = relay.Tuple([call_6162,bop_6187,])
output2 = relay.Tuple([call_6163,bop_6190,])
func_6193 = relay.Function([var_6186,], output)
mod['func_6193'] = func_6193
mod = relay.transform.InferType()(mod)
var_6194 = relay.var("var_6194", dtype = "float64", shape = (7, 16, 7))#candidate|6194|(7, 16, 7)|var|float64
output = func_6193(var_6194)
func_6195 = relay.Function([var_6194], output)
mutated_mod['func_6195'] = func_6195
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5852_call = mod.get_global_var('func_5852')
func_5853_call = mutated_mod.get_global_var('func_5853')
call_6209 = func_5852_call()
call_6210 = func_5852_call()
func_5981_call = mod.get_global_var('func_5981')
func_5984_call = mutated_mod.get_global_var('func_5984')
const_6212 = relay.const([[8,2,5,6,3,2,-3,4,8,-2,3,10,-4,9,3,-6,-3,2,-10,-9,8,-9,-8,8,1,2,10,5,-7,1,2,-2,-6,4,-3,-10,-4,1,-4,-9,1,-6,-3,4,3,-1,5,-1,-6,-8,8,1,9,-6,-10,-5,-8,9,1,-1,-1,3,-6,6,9,-2,-1,1,-2,10,-3,3,7,-1,7,7,6,3,-4,3,-10,10,-7,-1,7,-3,8,2,-9,-8,-6,-6,2,-4,8,-10,2,2,-1,8,-4,-10,8,10,4,-8,2,3,-3,2,4,-10,2,-8,4,-4,-9,-3,-6,-6,2,3,8,-9,2,-10,3,-3,-3,9,8,-10,-8,4,7,-6,-6,6,-4,-2,-6,3,4,4,8,9,-7,-3,-3,2,-8,10,9,5,10,-10,-10,8,10,5,7,1,4,-10,-10,-6,1,2,3,3,-5,-10,7,-10,9,-2,9,10,-7,10,-5,6,2,5,-5,9,-3,-4,-6,-7,10,-3,5,4,-6,-9,-9,-8,-5,8,-3,-10,7,-1,8,2,-7,9,-8,4],[-5,6,10,-9,-9,6,6,-10,-10,8,9,6,-2,-10,7,-6,-10,8,-8,-6,-6,9,-6,4,2,-6,9,10,8,-4,5,7,4,-5,4,7,4,1,7,-8,7,-9,-7,-8,1,9,-3,1,-4,8,-10,8,-3,3,-6,6,-4,-10,5,5,-1,2,-3,-9,-9,-4,4,-2,3,-4,6,-2,8,-5,-9,9,-5,2,-3,-4,10,1,2,-10,1,-5,5,-1,-7,-5,5,6,4,9,-1,-10,-10,6,6,-8,9,4,-1,8,-9,6,-7,-5,2,-8,6,-5,-9,-8,-4,-2,10,-10,2,10,-3,7,-1,-10,-8,-6,-6,-1,-10,2,5,-1,-1,-7,9,6,4,-1,-8,7,-1,2,-2,4,2,-7,1,6,-9,7,-10,1,8,8,4,4,8,7,-9,-3,-9,9,-10,-4,-8,10,-5,2,2,-9,-7,4,-9,7,-1,8,-3,-2,4,6,8,-7,-5,-6,1,3,-10,-3,-9,-6,1,4,3,-8,1,-6,-10,-4,4,-3,-7,2,5,-6,-6,-9,-6,-10,7,5],[-6,7,-4,10,-10,2,9,-7,-9,-1,5,9,-2,-2,1,-7,8,2,4,1,-6,5,9,2,-5,1,4,5,3,5,5,-10,5,-9,5,-6,5,6,3,1,2,10,-4,-4,-10,-2,8,-2,-5,3,-10,-10,-10,8,4,-1,-1,-6,4,3,-8,3,-8,-10,-3,-4,-4,8,9,-7,-5,-3,9,-1,-9,1,1,3,6,-4,-8,3,-3,6,-7,6,3,-6,9,7,4,-5,-1,-6,-2,7,-1,2,1,5,-2,10,2,-8,-5,-9,5,6,10,5,4,-4,4,10,-3,-5,-8,10,3,1,5,7,-1,7,6,-7,-6,7,6,-9,-4,4,9,2,-2,-2,-2,-6,-3,-8,5,-9,-6,-2,6,1,-6,-4,9,-9,-10,5,-9,6,-3,10,2,10,-8,10,6,7,-6,-8,-6,5,7,9,2,9,10,5,1,-9,10,4,-3,-9,-2,6,-4,-6,-3,-1,10,2,9,1,-5,-8,2,-2,-5,-5,-7,-6,4,-4,-7,-3,4,7,3,3,10,2,5,8,4,-8],[-8,2,6,-10,10,10,-7,7,-6,-7,-2,-10,-2,9,-6,4,9,6,1,-10,9,5,6,-7,2,1,-2,3,1,-9,8,1,-9,-5,-4,1,5,-3,-10,5,4,-10,-7,2,6,5,7,1,2,6,1,9,-5,-6,3,-1,-7,7,3,-10,-3,2,10,5,9,5,-1,5,9,3,3,2,2,-4,1,3,-10,5,8,9,3,7,-2,-10,-4,-4,-4,6,6,-10,-5,-2,-7,2,-8,3,7,-5,-2,10,7,-4,-10,6,2,6,10,2,-6,-3,5,6,-7,1,-8,-7,6,-4,4,6,-6,3,10,-3,10,-1,-5,-9,9,-4,-2,10,2,6,-3,-4,-3,-7,4,9,10,-9,6,7,-7,-2,2,6,-7,-2,5,1,2,-2,10,10,-1,2,6,-5,-10,3,1,6,2,-8,3,-6,7,-1,9,-4,-2,-10,-8,3,-3,10,6,2,5,6,9,-2,7,-3,9,-7,-6,9,-1,1,-9,-8,8,-2,7,-10,-9,5,10,-2,-7,-7,-5,8,9,10,4,-2],[7,5,1,2,-8,5,5,6,-8,7,-9,9,-8,-5,-8,-5,10,-1,-5,-2,10,-2,9,-10,-1,8,4,8,-8,-4,-10,3,9,5,-7,-9,-6,-5,-9,2,2,9,-9,7,10,6,-2,-9,3,7,3,-8,-8,-6,5,-6,7,-2,2,6,3,-1,-2,-6,-6,-4,10,8,4,5,-9,6,-10,-4,8,-4,5,7,-8,2,-7,-3,-10,-5,4,-4,2,-10,-8,5,-8,8,6,1,-8,10,-1,2,-5,-8,8,-3,-1,3,9,5,10,-9,1,-2,4,6,-6,-1,-7,1,8,-6,-5,8,8,1,1,6,-1,10,-2,-5,7,1,-2,7,-6,-10,-3,-7,4,-1,-8,-6,3,6,-4,-6,-6,5,9,9,7,6,-10,1,1,-8,8,9,1,9,-6,-8,-9,-2,5,6,1,-1,7,4,3,6,-9,3,10,-7,4,-1,-8,-3,-4,-6,3,7,-9,-7,-6,-2,-9,5,6,8,-9,4,3,2,-8,-4,6,-8,-6,-5,-7,-5,3,-6,4,-10,-4,-10,-2,4]], dtype = "int8")#candidate|6212|(5, 210)|const|int8
call_6211 = relay.TupleGetItem(func_5981_call(relay.reshape(const_6212.astype('int8'), [1050,])), 2)
call_6213 = relay.TupleGetItem(func_5984_call(relay.reshape(const_6212.astype('int8'), [1050,])), 2)
func_4684_call = mod.get_global_var('func_4684')
func_4687_call = mutated_mod.get_global_var('func_4687')
const_6220 = relay.const([-8.003152,-5.185297,5.637655,-2.552626,-0.604535,-6.251599,4.010656,-5.429112,7.198918,0.618234,7.374509,9.473665,-0.179855,0.094674,-0.325052,-4.403899,0.701065,-7.715955,-1.840349,-7.471987,-9.885989,3.474425,-2.126673,2.085186,3.933621,8.268610,-4.031292,8.391651,7.768086,-9.460165,-0.064031,-2.422455,6.267172,-3.400078,-5.543153,-3.736790,5.378559,-0.477887,0.627214,9.935801,-8.932865,-1.785621,-7.813615,-3.802000,-2.361929,7.814333,3.584787,7.647322,0.060541,-8.621937,-9.079940,-9.767869,-1.967849,0.149881,-5.403711,1.655814,-1.873895,2.822263,6.552270,-4.445075,6.985114,-2.689308,-8.003797,8.810592,-1.527851,6.823946,5.282713,-2.014861,-8.415612,9.923616,0.083136,-7.804011,-4.873791,-7.922133,3.897986,-5.996239,-3.835817,7.336012,-7.965671,-2.023130,-4.624666,3.537282,1.551301,1.747862,-0.016556,6.418797,5.343170,0.825094,5.163882,-9.867373,-2.322937,6.214475,1.122890,3.651529,-0.493075,-9.411422,0.092812,-9.010408,-4.461010,7.575337,-7.061579,-5.347277,-9.097921,-7.540336,2.364175,-7.722823,4.888593,-1.002175,-4.571118,-5.575412,-6.318765,9.803805,-1.928493,-1.684273,8.530905,8.340740,-9.696777,-5.683713,3.102001,6.301948,3.614025,9.539386,1.707432,4.384358,6.282160,-5.142889,8.087315,-6.829931,2.760294,-5.841512,-4.101254,2.023989,3.797775,9.091319,-8.837398,9.537348,-4.062039,-8.403941,-4.841924,0.380374,8.716215,6.752617,0.969609,-9.641997,7.132734,0.585795,1.488756,-6.277830,-2.694822,7.501772,-9.668684,-6.729469,7.635062,1.439495,1.175660,-8.169068,-9.755552,3.176094,5.515471,4.671248,-0.177498,-2.226216,8.640906,-1.772073,-4.669181,-2.372965,-1.896135,8.730226,8.175998,1.102586,9.989597,0.057319,-8.507425,8.823445,-2.660220,-4.168388,5.230180,-2.812547,4.032568,1.502524,5.915159,3.957217,-2.013941,9.375312,5.561776,-0.482134,-4.548856,-5.024996,-0.093224,-9.881081,-4.615683,8.273301,2.127243,-9.908603,-3.981753,-1.261455,7.915344,1.426209,-3.278464,3.439594,-7.334764,-7.456985,8.410805,6.341972,-1.427629,6.487468,-2.927362,8.568576,-3.449236,-9.904740,2.382280,-0.353409,-0.109067,-5.911085,6.088446,-0.339499,-8.197247,-4.686411,-7.118339,1.491870,-8.102630,6.112094,-8.583587,-2.533529,0.855236,7.266441,-4.364193,0.562507,-6.441656,2.607503,-5.403668,1.120812,8.794083,-3.423422,4.089823,-3.052254,-1.099122,-9.856528,-1.204980,-5.529721,6.852729,-9.019121,7.562464,6.908108,-3.871601,7.899171,-1.444850,9.161349,0.455553,2.264172,6.981975,-5.988455,-0.860103,-2.939811,4.032731,-3.262161,5.298423,-5.782456,-7.040345,-2.148739,1.155767,8.548562,-9.544437,1.419808,2.416098,-5.200370,-3.632311,-8.178644,2.477606,-6.085584,8.888624,1.061497,0.188339,-6.816532,7.283391,-4.778521,-1.356238,8.952009,-2.339922,-9.525094,9.069929,1.057906,8.602155,-7.815071,-8.138090,-5.590744,4.090287,-9.946472,5.358058,1.790239,9.118899,5.683270,4.110067,-0.842388,9.273676,2.365659,5.013025,2.409544,2.661461,9.266826,-1.643383,8.399125,-5.510526,-1.125056,-2.564714,-2.967941,-6.484472,-8.962260,-7.571764,5.099582,9.421858,7.080740,7.416227,-4.186839,-1.427271,8.776317,7.596195,9.119472,-1.625319,7.785836,1.402879,3.316597,-4.539796,2.760072,-5.637815,-5.482909,-5.697658,9.970250,-3.648801,-4.225278,7.664188,5.268349,-3.935734,-0.057765,3.856021,-1.911643,-6.383998,-5.212531,8.465612,7.593250,-7.900054,8.183769,9.747473,6.149715,-1.916441,7.730183,9.953102,-2.238459,4.640911,-3.728334,6.615478,7.952577,-0.549556,-8.237082,6.228133,-2.516672,3.146246,-1.761933,-3.350938,7.350162,7.822010,-7.032099,9.325163,4.325283,-3.501623,0.184184,-1.378710,0.871515,-4.934891,-6.730233,0.087276,-6.798886,-3.190372,-3.172669,-3.258801,-7.676301,-3.467150,-6.552626,2.104703,-7.383408,4.238781,0.134572,-4.602685,8.194960,-1.695066,-6.242997,-1.635232,6.084879,-4.646116,0.044024,7.706083,-8.146436,-4.212635,8.681794,-2.757765,6.374846,-5.762679,1.090279,4.517079,9.223918,-9.571910,-3.644321,-5.349249,-0.588580,2.432731,4.695220,7.022382,-2.225439,-4.132285,7.271107,4.660977,6.183423,-1.620861,-8.811617,4.970248,7.927935,4.117833,-2.938872,6.080761,-9.987190,-8.959050,8.235307,-4.032127,5.951072,-6.949618,4.259671,-1.126871,7.855835,-6.878514,-1.418689,5.581678,4.196320,1.971916,0.548841,-0.134845,8.134082,8.604271,-6.383223,-0.088910,5.625340,9.656427,-4.858227,8.430448,-6.236143,6.397936,0.580778,-8.299210,-7.840262,-3.981119,8.628102,1.176961,2.194956,6.877948,-5.985498,1.810718,-5.034000,5.341886,-2.359947,-4.870037,-7.533141,-3.063288,6.419004,-0.870806,-5.377762,3.190737,-2.473998,8.313689,3.558887,4.264711,-7.201295,9.956499,6.196729,-5.540830,3.398097,-9.407852,-2.654780,1.849996,-7.403916,2.705648,-3.358060,-7.962156,-2.491508,-2.629715,-2.463005,9.380217,4.517025,-8.702468,3.894711,-4.667786,0.599032,-1.039356,9.928618,0.423787,-2.860778,4.555220,7.059118,1.900964,6.487853,-4.545738,4.684974,-4.220311,-7.297423,-1.708479,4.185314,1.686328,4.901839,3.632295,1.279660,-1.820978,4.408847,0.127319,1.952942,-9.925803,-3.464912,3.941349,1.889347,-6.591965,-9.152545,3.164521,-7.131201,-6.643235,2.452906,-4.960180,2.019427,-2.839898,-7.983951,5.202023,-5.818819,-4.734792,-4.177167,-6.217075,-6.859572,-7.365895,7.966629,-3.585214,-4.772250,-6.613410,-3.726337,-4.433295,4.437724,0.953020,-8.492477,-6.650749,-5.424774,-7.244453,-1.537774,-8.288642,1.505248,5.066059,3.116901,-5.557365,-3.974921,6.694601,-9.373571,-0.405060,-6.960689,0.495260,3.308855,0.817899,5.266966,-7.677351,-6.492610,-5.478657,7.474881,5.023660,0.311548,-9.828049,-2.107845,5.780379,-5.241168,-1.737921,6.207903,7.217525,6.607336,-9.378942,-5.470955,-5.171894,-4.777616,6.864649,-0.622903,-9.652179,-0.539384,-7.134716,-6.591178,8.229487,5.917860,9.992709,-7.276449,8.609857,7.994880,-7.530044,9.014799,-8.956194,8.660404,6.029172,-2.907951,4.109929,3.073010,9.863151,8.141487,-0.526654,4.342317,6.265126,-5.097348,5.652096,1.754354,-8.385069,1.578029,-2.713485,-8.098407,-9.381483,5.401873,0.821312,0.696117,-8.311608,-8.093342,-3.718673,-5.141957,9.139712,-7.201489,-1.819900,-4.812573,-6.571610,6.111041,-2.322666,5.879959,1.134435,-0.102265,3.372969,5.369898,6.031207,-8.375789,5.913974,0.875815,1.348701,-2.787178,8.183069,-3.878159,-0.820814,-3.407378,3.144259,6.604220,-6.114303,-8.041361,-8.292058,8.756593,8.040050,3.352388,-1.668637,0.724072,-1.881653,5.424807,-9.755471,-5.736586,-4.643579,0.325552,-1.053122,-9.118387,-5.444240,-9.874975,-1.918362,-3.124183,0.028353,4.663745,4.344562,3.560002,-0.758359,2.591986,1.008976,5.067835,7.210929,3.887172,0.565785,-4.219715,-7.404018,-6.849532,7.330339,-3.365342,-7.652706,-9.183859,-0.712124,-8.589048,1.287798,2.371951,7.717801,-6.716693,3.840405,-4.178861,9.569280,4.376223,4.063683,-0.011842,-2.296857,3.508924,-2.343592,-3.048649,0.829535,3.689008,3.290906,3.234363,8.425103,1.347201,-9.475140,-0.301242,-0.531284,3.047213,1.978056,-5.895952,4.732090,7.983502,-0.302560,-9.171890,-5.231564,-7.425132,9.846149,-8.639221,0.106924,3.565748,2.530844,7.831027,3.735445,8.871052,-0.577039,8.839822,4.764411,-5.675718,-8.770874,1.583236,-0.657186,-2.526268,-5.576706,4.150879,-7.247966,1.067287,-8.978234,-2.363641,0.171930,-6.474510,0.566706,2.719527,-6.500995,-8.385960,2.983997,2.765153,7.293550,9.662952,-7.778542,5.435685,5.403631,-4.656133,2.890786,-1.576259,-6.894481,2.125737,-7.865766,-4.761931,-3.320079,1.508998,4.355288,6.290012,4.335618,-0.889620,4.043161,-1.066814,-9.748631,-7.553894,9.583348,-9.729221,-8.850478,-1.447828,5.880821,0.348580,0.142375,2.976427,-9.471840,-7.084589,3.271203,7.267385,-5.907969,0.150864,1.705456,2.811949,-9.848888,-6.123787,0.605694,9.837961,-3.123789,-1.654697,-5.125127,-5.694645,-2.444366,-4.973136,9.139765,3.288682,3.936706,-0.007734,-9.392973,-1.873166,0.585763,3.720179,6.896267,3.753879,-1.493000,5.296756,7.861169,7.296984,-8.059460,9.178872,4.057236,-9.426290,-8.219102,6.397451,-4.248780,0.094630,9.470309,-3.748932,-4.427206,-0.099408,1.598308,5.789738,5.748577,-7.310337,-5.226505,7.028403,-5.853406,-8.503814,-8.913986,-8.725638,4.153221,-8.518501,-8.832501,9.554405,6.622751,7.810645,-7.383580,1.970286,2.642914,9.868418,-6.389655,-5.049400,-7.005339,5.532096,-9.863543,1.848605,9.358279,-0.409364,-6.959327,-9.386208,8.282160,-7.793299,-6.156129,5.340464,-7.437055,1.153742,8.437324,2.790084,0.263263,-1.574080,-0.029579,8.958881,-4.257822,-1.278244,-7.135344,-6.703150,-6.344014,2.509290,-1.028889,5.692848,7.652634,8.463090,-4.348094,9.141219,2.905880,3.138612,4.048327,-3.780759,4.814082,7.477739,7.283170,3.523134,-9.854781,2.128479,-4.018976,3.548137,8.380693,-5.022710,-3.796413,8.114971,-1.638360,8.695031,-4.818755,5.798768,-7.723716,0.212729,-0.369781,-9.576963,8.563576,0.669971,-5.671070,1.179979,-6.947423,7.901821,2.980075,-3.933473,8.004070,-0.623376,8.523689,1.341961,-1.114665,-1.881589,-5.778091,0.229705,-4.284587,3.779183,-0.412181,-9.827056,-8.020433,6.641316,7.515488,5.369958,4.410828,-2.563748,5.607432,0.054566,-8.153920,-8.471244,-3.350852,-4.242404,0.477524,3.175537,-5.060749,-5.909396,9.293037,5.062020,7.524657,3.851137,-3.910409,-7.701454,-9.644910,3.817196,7.231828,3.936560,6.784625,-4.255819,6.023223,-7.230575,0.135356,-2.822804,-0.664319,8.361309,0.669752,6.228187,-5.856645,4.112808,7.560026,1.335919,1.112482,-8.538421,-5.370993,0.221114,-6.775163,-1.434611,-6.422558,-5.940494,-6.239801,-2.036131,-7.167869,5.738547,6.292841,9.438434,6.821983,7.900042,8.867006,0.343158,-3.997301,9.883009,7.147973,4.093781,9.301519,-1.091280,4.702167,1.295954,-9.005544,8.597866,8.263120,-8.294874,4.108544,8.917463,6.052303,2.998568,0.178832,-2.011277,-6.395939,-2.806767,3.672299,2.159193,-7.721011,2.799800,1.383579,-6.883929,4.275935,3.648630,5.179073,-4.037398,4.440798,-1.458664,-7.219170,6.250092], dtype = "float32")#candidate|6220|(1008,)|const|float32
call_6219 = relay.TupleGetItem(func_4684_call(relay.reshape(const_6220.astype('float32'), [16, 7, 9])), 0)
call_6221 = relay.TupleGetItem(func_4687_call(relay.reshape(const_6220.astype('float32'), [16, 7, 9])), 0)
output = relay.Tuple([call_6209,call_6211,const_6212,call_6219,const_6220,])
output2 = relay.Tuple([call_6210,call_6213,const_6212,call_6221,const_6220,])
func_6231 = relay.Function([], output)
mod['func_6231'] = func_6231
mod = relay.transform.InferType()(mod)
output = func_6231()
func_6232 = relay.Function([], output)
mutated_mod['func_6232'] = func_6232
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4611_call = mod.get_global_var('func_4611')
func_4613_call = mutated_mod.get_global_var('func_4613')
call_6269 = func_4611_call()
call_6270 = func_4611_call()
output = relay.Tuple([call_6269,])
output2 = relay.Tuple([call_6270,])
func_6273 = relay.Function([], output)
mod['func_6273'] = func_6273
mod = relay.transform.InferType()(mod)
mutated_mod['func_6273'] = func_6273
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6273_call = mutated_mod.get_global_var('func_6273')
call_6274 = func_6273_call()
output = call_6274
func_6275 = relay.Function([], output)
mutated_mod['func_6275'] = func_6275
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4510_call = mod.get_global_var('func_4510')
func_4512_call = mutated_mod.get_global_var('func_4512')
call_6280 = relay.TupleGetItem(func_4510_call(), 1)
call_6281 = relay.TupleGetItem(func_4512_call(), 1)
uop_6283 = relay.exp(call_6280.astype('float32')) # shape=(7, 16, 7)
uop_6285 = relay.exp(call_6281.astype('float32')) # shape=(7, 16, 7)
func_5716_call = mod.get_global_var('func_5716')
func_5718_call = mutated_mod.get_global_var('func_5718')
call_6287 = relay.TupleGetItem(func_5716_call(), 0)
call_6288 = relay.TupleGetItem(func_5718_call(), 0)
func_4684_call = mod.get_global_var('func_4684')
func_4687_call = mutated_mod.get_global_var('func_4687')
var_6290 = relay.var("var_6290", dtype = "float32", shape = (1008,))#candidate|6290|(1008,)|var|float32
call_6289 = relay.TupleGetItem(func_4684_call(relay.reshape(var_6290.astype('float32'), [16, 7, 9])), 1)
call_6291 = relay.TupleGetItem(func_4687_call(relay.reshape(var_6290.astype('float32'), [16, 7, 9])), 1)
output = relay.Tuple([uop_6283,call_6287,call_6289,var_6290,])
output2 = relay.Tuple([uop_6285,call_6288,call_6291,var_6290,])
func_6313 = relay.Function([var_6290,], output)
mod['func_6313'] = func_6313
mod = relay.transform.InferType()(mod)
mutated_mod['func_6313'] = func_6313
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6314 = relay.var("var_6314", dtype = "float32", shape = (1008,))#candidate|6314|(1008,)|var|float32
func_6313_call = mutated_mod.get_global_var('func_6313')
call_6315 = func_6313_call(var_6314)
output = call_6315
func_6316 = relay.Function([var_6314], output)
mutated_mod['func_6316'] = func_6316
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4637_call = mod.get_global_var('func_4637')
func_4638_call = mutated_mod.get_global_var('func_4638')
call_6340 = relay.TupleGetItem(func_4637_call(), 0)
call_6341 = relay.TupleGetItem(func_4638_call(), 0)
func_5312_call = mod.get_global_var('func_5312')
func_5315_call = mutated_mod.get_global_var('func_5315')
var_6348 = relay.var("var_6348", dtype = "float32", shape = ())#candidate|6348|()|var|float32
const_6349 = relay.const([1,8,-9,5,-8,8,9,5,1,-3,-7,-2,4,-4,3,6,-3,2,-7,-6,2,-8,-1,2,-4,10,3,-2,10,-7,3,-6,10,-10,7,-3,-3,3,-3,-6,9,-6,10,3,-4,-4,2,5,10,-10,-3,-7,3,10,4,-10,-4,7,-6,5,-1,-9,10,6,1,-6,-8,-1,-2,4,9,-9,2,-6,-8,-8,-9,-1,-3,9,-2,8,-8,10,2,-6,-10,3,-10,-10,-9,7,-7,6,-5,4,10,7,3,-7,-1,-7,7,3,-8,-8,-1,-4,3,-8,5,-6,-4,-2,-2,1,10,-6,-7,-6,4,-3,-9,3,6,-10,3,-5,-1,-1,6,6,-1,4,-3,-4,-6,-2,-3,7,-8,2,3,8,6,4,-3,-9,5,4,-8,3,-7,-9,9,2,2,-9,-3,8,-6,3,-5,6,8,7,10,7,4,8,1,5,3,-10,-10,-8,-3,8,1,-9,3,4,8,3,-9,-9,2,-8,7,3,-6,-6,10,-6,-9,4,3,-7,1,-4,2,5,-7,-1,8,-2,5,-3,3,9,-6,-5,-9,3,2,-2,-1,8,-9,2,3,2,-3,4,-6,-7,-4,-3,-5,-4,-4,-3,5,-4,-2,-2,4,2,8,-3,-9,-7,5,5,-8,8,9,-10,-7,-7,-3,-4,2,4,4,-2,-10,-5,1,-4,10,3,-5,4,-9,9,-1,-1,-10,2,-2,6,-5,4,2,-5,10,-4,2,5,8,-3,8,1,-9,-2,7,-3,-1,-8,-7,-5,-2,-3,6,6,-3,-2,-5,9,-8,-4,-10,-9,6,-2,-10,-1,8,9,-4,-8,5,10,-5,-3,9,-9,-6,10,6,6,-10,10,-5,-2,5,-5,-9,2,3,10,5,-3,-8,5,-6,9,10,-6,8,3,9,4,5,4,1,2,-3,-7,9,-6,4,4,7,-10,-9,8,3,6,10,-5,-3,-9,1,9,9,-8,-1,7,-4,2,-10,-1,-4,10,-8,7,2,-10,-1,5,-4,-2,-5,4,-6,3,9,-2,5,-9,6,6,1,3,5,-1,-2,8,2,7,8,-7,-5,2,-10,3,-6,-6,-5,8,-8,2,1,-7,2,4,-5,-9,-9,-2,-1,-7,-4,-5,-1,-10,1,8,2,9,-3,-3,6,-3,-2,-6,-10,1,3,4,8,-4,7,-5,9,-4,6,3,1,9,-10,6,5,5,-3,5,-4,10,-10,2,-8,-4,-8,-8,-2,10,-9,2,-4,-5,6,8,-6,-1,5,8,4,2,8,8,-7,1,-7,-2,-10,9,5,-5,-8,-7,-2,10,6,7,-2,-3,-5,4,9,-4,5,4,1,-10,6,5,4,-5,7,-4,6,7,4,-5,9,2,1,3,5,-4,-5,-8,-2,9,4,-8,3,-4,-7,9,-8,-10,-7,2,6,-3,-3,-10,-6,6,-4,-2,10,-3,-7,-10,1,6,3,-10,-4,-10,3,-3,10,-1,-6,9,-1,10,5,4,2,-4,8,3,-8,-8,-4,-10,-2,7,5,1,-10,-5,5,-1,-1,-1,2,10,1,-10,9,-9,2,9,6,3,-5,1,10,-4,-10,10,10,-1,-6,-6,-1,-7,5,-8,8,-6,-2,2,2,2,2,3,10,3,-5,4,-7,6,-9,-10,-10,9,-5,3,-8,1,-7,-1,8,-4,6,8,-8,-3,3,-3,2,-2,-4,6,9,9,-2,2,6,-7,-3,4,-1,8,10,4,3,3,-2,7,-6,7,7,-2,-7,-3,-3,-2,4,6,-9,-10,-10,-10,-1,6,-5,7,-4,5,7,-2,7,-5,-3,-6,3,9,-6,6,7,-5,6,-2,-3,2,7,2,-9,4,10,-8,-6,6,5,-9,5,3,-8,-2,4,-10,-1,4,1,-3,7,-4,10,3,4,-10,-8,2,9,-6,9,5,-2,9,-8,4,6,6,-8,3,-3,-2,-5,-8,8,9,-3,7,-7,9,-1,-9,-1,-2,6,-2,6,3,-10,-6,-6,-8,-3,-6,-3,4,-8,-10,-9,-7,-8,5,4,-5,-8,3,-10,-5,-5,-1,-6,2,-9,-10,-5,-5,-7,-8,10,-3,6,4,-8,7,10,2,5,7,-8,-4,5,7,4,2,1,-2,-5,3,5,-7,-1,8,-4,-2,3,7,-9,-1,10,-5,-3,9,5,-1,3,-5,6,-10,10,5,10,-3,-6,10,-2,-8,5,-2,9,-1,3,9,-1,10,-1,-5,6,-9,-4,2,-3,-10,-10,-9,8,-3,7,-10,3,10,-6,-4,-4,-9,-2,-4,-1,-5,9,-10], dtype = "uint16")#candidate|6349|(864,)|const|uint16
call_6347 = relay.TupleGetItem(func_5312_call(relay.reshape(var_6348.astype('float32'), []), relay.reshape(const_6349.astype('uint16'), [864,]), ), 6)
call_6350 = relay.TupleGetItem(func_5315_call(relay.reshape(var_6348.astype('float32'), []), relay.reshape(const_6349.astype('uint16'), [864,]), ), 6)
func_4611_call = mod.get_global_var('func_4611')
func_4613_call = mutated_mod.get_global_var('func_4613')
call_6362 = func_4611_call()
call_6363 = func_4611_call()
func_4431_call = mod.get_global_var('func_4431')
func_4434_call = mutated_mod.get_global_var('func_4434')
const_6371 = relay.const([6.540353,-6.407455,0.675151,-3.471096,0.431213,4.699861,8.208124,-9.940293,-7.482331,0.956055,5.333690,-3.151406,7.609315,-6.179808,-5.916995,-3.104933,9.502731,-2.900913,5.671650,9.072040,6.012649,-0.544606,-1.645860,-6.068710,9.423614,0.783035,-4.898514,7.588975,2.248825,-9.950237,3.735566,-4.283424,-0.249090,5.529435,9.702428,-3.199518,2.377801,4.322916,3.116709,4.016825,3.017887,0.784118,-0.572392,-1.991905,8.991833,2.015541,6.741723,9.511630,-9.262979,2.523215,8.865404,4.620768,-3.003932,7.983943,-1.266369,-7.658911,9.322465,6.794164,1.401095,-6.110657,-8.054739,5.320394,7.742026,6.318204,6.828743,4.485911,-6.447690,6.816920,0.768998,9.638428,2.605488,6.266773,0.569874,-6.062612,-1.283870,0.014698,4.160451,-2.086583,3.690194,-8.625254,-2.852866,-6.172698,-8.728137,9.245159,-7.877623,4.709804,7.115365,-5.955965,1.619685,6.222456,0.693102,2.395463,4.260544,0.595283,9.055348,7.939183,1.780903,5.227012,8.071526,1.325919,1.368875,-3.078432,-1.883092,3.794084,6.838467,2.148232,-8.060145,3.465178,5.392966,-7.151898,2.083612,-1.425828,3.813962,-2.878320,3.360364,-7.178417,0.224289,3.638874,-5.628585,5.295637,2.684705,-9.384962,3.087357,7.392330,1.710194,-5.939450,4.813183,4.772987,-8.758911,5.544669,-0.975561,-6.841414,-8.773839,6.681970,-6.890362,1.645783,2.403835,1.125064,1.769172,0.637116,4.620517,2.459050,8.901286,1.872746,0.340828,2.706812,2.377639,2.162213,7.386126,-3.678783,5.115236,3.179993,7.296165,-3.633073,2.452671,6.569150,5.732713,4.613106,-8.145658,-1.060271,3.150137,6.454650,4.934859,8.159593,4.549428,-7.978589,3.445391,6.287795,6.845750,5.659643,-8.282419,2.977770,-3.335423,-3.351791,4.123292,-6.397897,-6.285743,4.381355,-6.113956,-6.003058,-3.864362,-6.503216,-9.163187,3.582791,3.140902,-3.614302,6.970943,5.868411,-7.476169,-9.525234,-7.162020,-4.198435,-2.445880,-2.840147,-8.506005,-2.939043,-8.201984,-2.572493,7.828776,-9.185144,8.704274,-5.814497,-6.428657,-5.834517,7.854608,-9.173097,5.413494,-4.986955,2.219653,-6.394534,0.986986,-5.467278,4.487275,-9.057742,-7.353467,-0.322381,2.556879,6.833575,-1.327094,-4.280218,-6.916724,-5.181423,7.607024,-5.170495,6.494498,2.967354,2.393011,-6.861694,-3.502213,8.593177,4.025640,-3.248260,-3.090895,-6.807580,1.319892,-3.758926,-6.526105,5.371503,3.967466,-9.323088,-7.363468,6.912584,1.065492,5.151306,-3.991610,3.914985,-6.752696,-0.841825,0.420003,5.208941,8.288879,-2.232150,-2.262049,-8.418739,2.368947,3.206403,-9.950575,-1.739161,-4.108595,2.745626,-1.256228,8.001528,1.872930,-9.646671,-0.940566,4.726244,7.235289,8.718730,-0.747442,-7.606156,-2.806220,3.681511,-4.113720,4.199869,0.119329,-9.926226,8.748427,-3.898203,7.150786,6.192990,0.890841,-9.502210,-2.380902,-9.968803,1.345555,9.927282,-0.168866,-9.551868,-6.992487,-3.344579,-0.226247,0.413013,-2.082563,-9.345958,-7.399726,7.077398,1.669752,7.200663,-2.036706,-3.397455,-5.023461,0.804500,-7.774765,8.978988,2.773535,5.995204,-0.384736,8.238066,-8.077849,2.372950,8.500893,-8.595468,-4.620485,4.854532,-3.915765,-6.756842,4.942610,8.550443,4.316865,-5.899417,-3.350031,-9.876877,-4.270106,3.740238,-2.402376,-6.103536,-2.219845,-9.865361,-1.692634,8.411173,7.205294,1.461159,1.149826,-8.508363,6.675878,-3.415039,-7.488433,8.492377,-3.755420,-5.204957,8.145905,6.317402,1.175428,-0.600500,9.629350,-0.051850,2.419650,3.013911,7.179621,0.735502,-9.705355,-3.555157,-6.049287,2.330618,4.831158,2.367134,-3.432147,-2.033108,-1.171236,9.041294,-1.285454,-4.633027,5.602028,-5.354147,-1.968919,-0.378950,5.192614,0.680915,-7.905415,6.833237,-3.526676,-4.677912,7.539369,8.201248,5.911266,0.395560,-8.589125,2.040601,9.626856,-6.603095,3.308338,-0.770586,-1.919924,-7.779242,-6.963444,-4.483788,6.878786,-2.875580,9.426054,-9.556471,-4.684110,-9.629841,-5.984481,3.119288,0.732515,6.170771,-9.615561,-1.306363,1.983279,8.754612,-7.314220,9.314185,-4.703018,-8.244466,9.613943,-6.170630,-9.038447,-6.312755,-0.093953,-2.304382,-9.960140,-6.096418,8.122880,3.241570,3.347050,-8.036620,-4.031022,8.937313,2.101796,-0.131952], dtype = "float32")#candidate|6371|(420,)|const|float32
call_6370 = func_4431_call(relay.reshape(const_6371.astype('float32'), [15, 7, 4]))
call_6372 = func_4431_call(relay.reshape(const_6371.astype('float32'), [15, 7, 4]))
func_4581_call = mod.get_global_var('func_4581')
func_4582_call = mutated_mod.get_global_var('func_4582')
call_6388 = relay.TupleGetItem(func_4581_call(), 0)
call_6389 = relay.TupleGetItem(func_4582_call(), 0)
func_5981_call = mod.get_global_var('func_5981')
func_5984_call = mutated_mod.get_global_var('func_5984')
const_6392 = relay.const([-4,6,8,5,-3,-5,-1,-1,-8,-9,-4,-6,-4,-7,8,4,9,-5,-5,9,7,3,2,6,7,-10,-6,5,-1,-7,-10,-2,3,8,-10,-4,-10,6,-2,-1,-8,1,-9,5,9,-10,-5,10,10,5,-4,8,7,7,8,10,10,3,-10,-1,10,-9,-2,10,6,5,-6,5,8,-5,-9,6,8,1,6,8,3,-9,-6,-10,-6,-2,7,6,-9,-4,5,8,-7,-3,2,9,9,-2,-8,-9,5,-7,-1,10,5,8,3,-3,-6,-5,8,-6,1,1,-8,6,-4,-8,7,2,-1,1,-8,-6,1,-5,-5,-5,8,-8,8,4,6,-4,-1,2,-9,-5,7,3,1,8,-10,-2,9,-9,-3,-7,-6,-9,-9,8,-6,-5,4,-5,-10,1,-4,-2,-5,1,5,-7,1,7,-9,-8,-8,1,4,7,9,-4,4,-7,7,7,8,-3,1,10,7,-6,4,-6,-5,2,10,-6,-2,-5,3,-2,-7,-3,-7,8,-3,-6,6,-5,5,-3,-3,-1,-4,-5,8,9,2,-4,4,-2,10,6,-2,-5,8,3,-8,8,3,-10,-9,-8,10,-2,6,5,-2,4,-2,10,-8,1,1,8,1,5,-7,-4,7,-5,-10,10,1,-5,-2,3,1,-6,3,4,-3,7,4,-9,7,-3,-6,6,-9,-10,-9,-1,-7,1,-2,-4,-8,5,2,2,-9,4,-9,3,-3,-9,6,-3,8,10,2,6,-7,-9,-6,6,-7,-3,3,6,-10,10,-8,8,-8,-7,4,-8,6,-10,2,10,-8,-8,2,9,-3,-10,4,7,8,-4,-7,3,-2,6,1,-3,-2,2,-7,7,-3,-10,-3,-1,-1,3,-7,-9,-3,3,10,5,-9,5,-1,7,-7,1,6,-3,8,2,6,4,-4,-3,5,8,6,-1,6,-1,8,7,5,-8,-9,8,-10,5,9,2,-10,9,4,5,1,6,-7,1,4,6,-10,9,5,5,5,-10,-8,3,3,5,-3,1,-2,3,-4,9,1,3,3,-4,7,-5,4,-8,-3,1,4,7,6,1,-9,1,10,10,2,-4,-7,-6,5,8,-9,-6,-2,-8,-3,6,3,3,-1,-7,-6,-4,9,4,5,6,2,6,4,-10,-7,10,6,-1,6,-2,10,5,-9,5,-2,10,2,-8,2,-5,8,8,9,-3,-9,9,-2,-1,3,4,1,-9,-2,1,-9,-4,4,-3,3,-9,-10,4,-1,2,4,-9,-2,8,-9,7,-7,-7,2,1,-3,-8,9,4,10,5,-3,-9,-5,8,-5,-4,-7,3,-2,-7,-7,9,-8,7,10,-1,6,-8,6,7,-3,6,-5,-1,3,1,2,5,2,9,-4,6,2,-3,2,-10,2,-6,4,3,5,7,-3,-1,-6,8,3,-2,-8,3,-6,6,10,-4,-1,-4,-2,-8,-5,1,-9,3,-4,7,9,-5,-5,-2,5,9,-4,4,4,-10,-9,2,3,2,-10,1,-8,-4,-7,8,-6,-8,10,6,-4,-4,-9,-10,10,10,-2,-1,9,-3,-4,8,10,2,-10,5,-7,6,3,-8,10,7,3,2,3,-8,-10,9,-4,9,9,7,-3,2,9,-1,2,-10,-5,-6,-10,5,1,-10,-5,9,3,10,7,1,5,-6,1,-3,8,5,2,-10,4,-7,10,-2,2,-8,7,-6,5,-1,-7,5,4,7,-9,-10,-8,-3,3,-1,9,-5,-3,1,2,-6,-8,6,10,1,-10,-4,8,-9,3,7,1,10,-4,2,5,-6,-9,-9,6,8,-1,-6,-8,-3,5,4,-3,-10,7,4,1,7,10,7,-7,4,9,-8,-3,9,10,-3,-8,-1,-4,7,3,-5,1,1,-9,6,4,-5,3,-4,7,-8,-10,-2,-4,-10,-4,-3,9,4,10,-5,4,-1,6,-3,-1,-2,2,5,-4,4,-2,-4,3,-10,-10,5,-7,-4,-2,-9,-8,3,-4,7,-5,-5,-7,9,-1,-1,4,-6,4,5,6,8,5,-3,2,-7,10,8,-3,9,6,4,8,2,-9,-8,10,-9,9,-4,-6,10,4,-5,-4,2,4,1,-5,6,9,1,1,-4,5,-1,-10,-7,8,-3,6,-2,1,-4,6,4,-5,-7,-6,7,1,-2,-9,-7,-1,-1,6,-7,9,-7,3,-2,-6,-5,10,-4,9,1,-5,9,9,-10,3,5,-3,7,-4,2,-6,2,8,6,-4,-9,5,2,6,-2,1,1,2,10,6,7,1,-1,-7,-8,4,-7,-3,-7,-3,10,-10,10,10,9,-3,10,-8,-3,-8,8,-8,2,-6,-2,10,4,10,2,-3,-8,9,-10,-8,2,4,9,4,3,2,8,-5,4,8,7,-8,8,2,-2,1,-8,3,4,1,-9,3,5,-4,5,-4,3,-7,9,9,2,7,-4,9,10,-7,1,10,8,-4,4,-7,-1,-8,-6,2,-10,7,-9,-3,-4,-10,10,2,2,5,5,-4,6,9,-10,9,-9,-3,-3,-9,-7,-4,1,-7,2,-10,3,7,6,1,-6,8,-7,6,-9,6,8,-5,4,3,-3,6,6,7,-7,2,9,1,-2,5,-3,-7,1,-9,3,2,4,-6,-1,-6,1,2,-7,7,9,3,3,3,2,-8,4,5,-9,-10,-3,-9,-2,4,3,1,3,3,3,-1,-8,2,-10,9,5,10,-6,2,-9,7,2,-3,1,-3,4,9,-3,-3,7,2,3,-2,10,-5,4,10,-4,-1,3], dtype = "int8")#candidate|6392|(1050,)|const|int8
call_6391 = relay.TupleGetItem(func_5981_call(relay.reshape(const_6392.astype('int8'), [1050,])), 2)
call_6393 = relay.TupleGetItem(func_5984_call(relay.reshape(const_6392.astype('int8'), [1050,])), 2)
uop_6406 = relay.cosh(call_6347.astype('float64')) # shape=(12, 6, 12)
uop_6408 = relay.cosh(call_6350.astype('float64')) # shape=(12, 6, 12)
output = relay.Tuple([call_6340,var_6348,const_6349,call_6362,call_6370,const_6371,call_6388,call_6391,const_6392,uop_6406,])
output2 = relay.Tuple([call_6341,var_6348,const_6349,call_6363,call_6372,const_6371,call_6389,call_6393,const_6392,uop_6408,])
func_6410 = relay.Function([var_6348,], output)
mod['func_6410'] = func_6410
mod = relay.transform.InferType()(mod)
var_6411 = relay.var("var_6411", dtype = "float32", shape = ())#candidate|6411|()|var|float32
output = func_6410(var_6411)
func_6412 = relay.Function([var_6411], output)
mutated_mod['func_6412'] = func_6412
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4853_call = mod.get_global_var('func_4853')
func_4855_call = mutated_mod.get_global_var('func_4855')
call_6442 = relay.TupleGetItem(func_4853_call(), 2)
call_6443 = relay.TupleGetItem(func_4855_call(), 2)
func_6273_call = mod.get_global_var('func_6273')
func_6275_call = mutated_mod.get_global_var('func_6275')
call_6451 = relay.TupleGetItem(func_6273_call(), 0)
call_6452 = relay.TupleGetItem(func_6275_call(), 0)
func_5215_call = mod.get_global_var('func_5215')
func_5217_call = mutated_mod.get_global_var('func_5217')
call_6459 = relay.TupleGetItem(func_5215_call(), 0)
call_6460 = relay.TupleGetItem(func_5217_call(), 0)
func_5841_call = mod.get_global_var('func_5841')
func_5842_call = mutated_mod.get_global_var('func_5842')
call_6466 = relay.TupleGetItem(func_5841_call(), 0)
call_6467 = relay.TupleGetItem(func_5842_call(), 0)
uop_6474 = relay.erf(call_6466.astype('float32')) # shape=(7, 16, 7)
uop_6476 = relay.erf(call_6467.astype('float32')) # shape=(7, 16, 7)
output = relay.Tuple([call_6442,call_6451,call_6459,uop_6474,])
output2 = relay.Tuple([call_6443,call_6452,call_6460,uop_6476,])
func_6499 = relay.Function([], output)
mod['func_6499'] = func_6499
mod = relay.transform.InferType()(mod)
mutated_mod['func_6499'] = func_6499
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6499_call = mutated_mod.get_global_var('func_6499')
call_6500 = func_6499_call()
output = call_6500
func_6501 = relay.Function([], output)
mutated_mod['func_6501'] = func_6501
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6273_call = mod.get_global_var('func_6273')
func_6275_call = mutated_mod.get_global_var('func_6275')
call_6524 = relay.TupleGetItem(func_6273_call(), 0)
call_6525 = relay.TupleGetItem(func_6275_call(), 0)
output = relay.Tuple([call_6524,])
output2 = relay.Tuple([call_6525,])
func_6529 = relay.Function([], output)
mod['func_6529'] = func_6529
mod = relay.transform.InferType()(mod)
mutated_mod['func_6529'] = func_6529
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6529_call = mutated_mod.get_global_var('func_6529')
call_6530 = func_6529_call()
output = call_6530
func_6531 = relay.Function([], output)
mutated_mod['func_6531'] = func_6531
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6499_call = mod.get_global_var('func_6499')
func_6501_call = mutated_mod.get_global_var('func_6501')
call_6593 = relay.TupleGetItem(func_6499_call(), 0)
call_6594 = relay.TupleGetItem(func_6501_call(), 0)
output = call_6593
output2 = call_6594
func_6597 = relay.Function([], output)
mod['func_6597'] = func_6597
mod = relay.transform.InferType()(mod)
mutated_mod['func_6597'] = func_6597
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6597_call = mutated_mod.get_global_var('func_6597')
call_6598 = func_6597_call()
output = call_6598
func_6599 = relay.Function([], output)
mutated_mod['func_6599'] = func_6599
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6597_call = mod.get_global_var('func_6597')
func_6599_call = mutated_mod.get_global_var('func_6599')
call_6621 = func_6597_call()
call_6622 = func_6597_call()
output = relay.Tuple([call_6621,])
output2 = relay.Tuple([call_6622,])
func_6656 = relay.Function([], output)
mod['func_6656'] = func_6656
mod = relay.transform.InferType()(mod)
output = func_6656()
func_6657 = relay.Function([], output)
mutated_mod['func_6657'] = func_6657
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6674 = relay.var("var_6674", dtype = "float32", shape = (2, 9, 1))#candidate|6674|(2, 9, 1)|var|float32
uop_6675 = relay.tan(var_6674.astype('float32')) # shape=(2, 9, 1)
func_5215_call = mod.get_global_var('func_5215')
func_5217_call = mutated_mod.get_global_var('func_5217')
call_6681 = relay.TupleGetItem(func_5215_call(), 0)
call_6682 = relay.TupleGetItem(func_5217_call(), 0)
output = relay.Tuple([uop_6675,call_6681,])
output2 = relay.Tuple([uop_6675,call_6682,])
func_6683 = relay.Function([var_6674,], output)
mod['func_6683'] = func_6683
mod = relay.transform.InferType()(mod)
mutated_mod['func_6683'] = func_6683
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6684 = relay.var("var_6684", dtype = "float32", shape = (2, 9, 1))#candidate|6684|(2, 9, 1)|var|float32
func_6683_call = mutated_mod.get_global_var('func_6683')
call_6685 = func_6683_call(var_6684)
output = call_6685
func_6686 = relay.Function([var_6684], output)
mutated_mod['func_6686'] = func_6686
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6656_call = mod.get_global_var('func_6656')
func_6657_call = mutated_mod.get_global_var('func_6657')
call_6742 = relay.TupleGetItem(func_6656_call(), 0)
call_6743 = relay.TupleGetItem(func_6657_call(), 0)
func_2677_call = mod.get_global_var('func_2677')
func_2682_call = mutated_mod.get_global_var('func_2682')
const_6747 = relay.const([[-6,5,4,9,-5,10,-10,-6,-4,9,-6,4,-6,-4,7,-6,-8,4,2,10,4,5,8,9,2,-6,4,-10,8,-5,-9,7,3,3,-5,-3,2,4,-9,2,1,-2,9,-7,8,-2,-4,6,2,-5,2,-7,7,-8,4,-8,9,4,-3,-5,-5,-8,9,8,-5,10,10,6,1,-4,4,-2,3,1,4,-7,-6,-8,2,8,-9,-7,-8,-6,4,3,-1,1,8,-2,-7,-3,-5,-9,9,4,-8,6,-3,4,-2,5,2,9,-7],[6,9,8,10,-3,-3,-6,-10,-6,7,-10,8,2,1,-4,2,2,-7,7,6,-8,-7,-1,-9,7,8,4,-3,10,8,2,-3,-1,-3,-10,6,-9,6,-9,-8,2,-6,-5,-3,-2,-10,10,7,4,10,10,-5,1,10,6,-6,5,5,10,-5,-8,9,8,1,-7,-7,-9,7,-6,7,6,-10,-7,10,-2,4,-10,10,-8,-10,-2,-5,1,-10,-10,9,-2,4,4,9,-9,-8,5,-4,8,1,3,2,7,-3,9,-10,2,2,-7],[2,3,2,-7,-2,-4,-5,-8,-3,9,9,-9,-6,-2,7,-9,-5,10,-2,-6,1,9,7,5,10,9,9,-8,-8,-5,-2,-7,-9,-4,3,-9,-10,-2,-6,10,-10,-7,6,6,-8,1,5,4,-5,7,8,4,-4,8,5,6,-4,4,10,4,-9,9,4,-8,-4,9,-10,-2,1,-4,6,2,5,-10,6,-5,10,2,7,-5,4,-3,-6,9,-4,6,3,10,5,-4,-7,-9,3,2,-1,1,10,-2,-10,6,3,4,1,5,5],[9,10,-2,9,-3,1,-6,1,-9,-10,-4,8,-1,1,5,7,9,-3,-10,-5,3,-10,-8,8,1,10,-10,-1,-7,7,8,7,-1,8,-1,6,-10,-2,5,-4,7,-10,-4,6,-3,5,-8,9,-1,3,-4,5,-5,-2,8,-7,-4,9,-9,-1,-9,2,-7,9,1,-9,10,9,-2,6,-9,-4,-9,10,8,-8,8,-6,-4,4,-6,-8,-8,2,8,-9,-10,-1,-5,-8,-4,2,8,-6,5,-8,4,7,-3,-1,8,9,2,8,-10],[-2,3,-6,-4,-5,-4,-7,-7,10,7,2,-1,3,10,1,-6,-4,-7,-1,-3,-9,9,5,2,7,-5,5,9,-9,7,-9,-3,3,-3,10,-1,3,4,-6,-3,8,-2,-6,-10,10,-7,10,3,-1,-8,-2,-1,-8,5,3,-9,-8,5,1,-10,-1,-1,-8,-4,9,-9,10,-8,-5,4,-10,1,1,-5,9,5,-4,-3,-9,9,-1,-8,8,-1,8,-3,8,10,9,-4,-5,-10,-5,1,-2,-1,1,-5,-9,4,-2,8,2,-3,-7],[1,8,-9,6,7,2,-10,1,-6,2,8,6,5,-5,-10,5,-4,-5,-6,-5,-9,-2,4,6,2,7,-3,-7,2,7,4,-3,5,-1,7,5,-5,-8,-8,6,-2,1,9,-2,-10,2,2,-4,3,9,3,7,9,-6,10,9,6,-5,-8,5,7,5,3,8,5,8,-3,6,2,1,6,2,-1,-7,4,-10,1,2,-3,2,10,-5,-4,-5,5,-8,7,2,-7,-9,-3,3,4,-8,8,6,9,-8,-4,-1,10,-1,7,5,2],[-8,4,-9,-9,-5,6,-4,3,-9,-7,-8,-8,-4,-2,-3,-6,9,2,-8,4,7,-7,6,5,8,4,10,7,-10,-6,5,-4,2,2,-7,3,8,-7,1,8,5,-7,7,-3,-5,2,9,-4,-1,10,5,-4,-7,-7,-4,-8,-10,-5,1,6,7,5,3,8,8,-4,5,-5,-10,9,-9,4,-1,6,9,7,-1,1,-4,10,8,4,-3,-4,-3,-10,9,2,4,-4,-2,-8,-5,-7,-9,10,10,-9,-5,7,-7,8,2,7,-8],[1,-4,-2,-10,-10,3,-6,-6,-7,9,8,-2,3,-8,2,-1,-7,3,-4,6,2,5,-4,5,3,7,2,-10,5,-5,-6,-1,-1,-10,-5,-10,8,5,6,5,-5,-3,-4,-2,-10,10,-5,-9,-3,-5,7,-7,1,-1,3,-8,-10,5,-3,7,-8,-9,5,-1,-7,7,2,-1,8,-1,9,7,-2,3,3,-9,6,4,-6,-10,-1,-8,-10,7,-2,9,8,1,10,5,6,2,2,1,-1,2,7,7,1,-7,2,6,-2,2,-1],[-3,1,-6,3,10,8,8,-3,5,10,-9,-6,2,2,-9,-9,1,-10,-2,6,-9,-5,4,-3,-4,-10,3,7,-5,-9,5,7,-9,-5,-1,6,-7,-6,-9,-9,2,-5,5,-2,5,5,1,-6,-2,-3,1,-5,-10,-1,-2,5,10,-8,-4,-7,2,-8,7,-5,-4,4,-10,8,-9,-3,9,-4,-6,8,-1,-8,1,5,-10,7,-1,-3,-9,10,-8,-9,-9,-10,5,6,4,-10,1,-3,8,-7,10,-7,-9,-8,-8,-7,-10,-1,-6],[-1,-10,-3,8,4,-5,-2,-10,-5,4,9,-10,8,-5,5,5,-10,-8,-7,-1,2,-1,3,3,-2,1,10,8,-3,6,-4,5,9,-9,2,5,-7,8,8,10,-10,-1,-4,6,-4,5,-7,-4,-6,1,6,-5,4,5,-7,-4,-5,5,6,5,8,-7,-2,1,7,-7,-10,4,-8,-8,3,9,-6,7,8,9,-4,8,1,-4,-1,-9,-5,-7,-3,5,-6,6,-1,-4,-7,-2,1,-8,9,-1,7,5,7,5,8,6,6,-8,6]], dtype = "int8")#candidate|6747|(10, 105)|const|int8
var_6748 = relay.var("var_6748", dtype = "uint8", shape = (216, 2))#candidate|6748|(216, 2)|var|uint8
call_6746 = relay.TupleGetItem(func_2677_call(relay.reshape(const_6747.astype('int8'), [15, 5, 14]), relay.reshape(const_6747.astype('int8'), [15, 5, 14]), relay.reshape(const_6747.astype('int8'), [15, 5, 14]), relay.reshape(var_6748.astype('uint8'), [432,]), ), 2)
call_6749 = relay.TupleGetItem(func_2682_call(relay.reshape(const_6747.astype('int8'), [15, 5, 14]), relay.reshape(const_6747.astype('int8'), [15, 5, 14]), relay.reshape(const_6747.astype('int8'), [15, 5, 14]), relay.reshape(var_6748.astype('uint8'), [432,]), ), 2)
output = relay.Tuple([call_6742,call_6746,const_6747,var_6748,])
output2 = relay.Tuple([call_6743,call_6749,const_6747,var_6748,])
func_6753 = relay.Function([var_6748,], output)
mod['func_6753'] = func_6753
mod = relay.transform.InferType()(mod)
var_6754 = relay.var("var_6754", dtype = "uint8", shape = (216, 2))#candidate|6754|(216, 2)|var|uint8
output = func_6753(var_6754)
func_6755 = relay.Function([var_6754], output)
mutated_mod['func_6755'] = func_6755
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6231_call = mod.get_global_var('func_6231')
func_6232_call = mutated_mod.get_global_var('func_6232')
call_6757 = relay.TupleGetItem(func_6231_call(), 4)
call_6758 = relay.TupleGetItem(func_6232_call(), 4)
func_5563_call = mod.get_global_var('func_5563')
func_5565_call = mutated_mod.get_global_var('func_5565')
var_6761 = relay.var("var_6761", dtype = "float64", shape = (48,))#candidate|6761|(48,)|var|float64
call_6760 = relay.TupleGetItem(func_5563_call(relay.reshape(var_6761.astype('float64'), [1, 4, 12])), 1)
call_6762 = relay.TupleGetItem(func_5565_call(relay.reshape(var_6761.astype('float64'), [1, 4, 12])), 1)
func_5336_call = mod.get_global_var('func_5336')
func_5337_call = mutated_mod.get_global_var('func_5337')
call_6763 = relay.TupleGetItem(func_5336_call(), 0)
call_6764 = relay.TupleGetItem(func_5337_call(), 0)
output = relay.Tuple([call_6757,call_6760,var_6761,call_6763,])
output2 = relay.Tuple([call_6758,call_6762,var_6761,call_6764,])
func_6780 = relay.Function([var_6761,], output)
mod['func_6780'] = func_6780
mod = relay.transform.InferType()(mod)
var_6781 = relay.var("var_6781", dtype = "float64", shape = (48,))#candidate|6781|(48,)|var|float64
output = func_6780(var_6781)
func_6782 = relay.Function([var_6781], output)
mutated_mod['func_6782'] = func_6782
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5841_call = mod.get_global_var('func_5841')
func_5842_call = mutated_mod.get_global_var('func_5842')
call_6809 = relay.TupleGetItem(func_5841_call(), 0)
call_6810 = relay.TupleGetItem(func_5842_call(), 0)
output = call_6809
output2 = call_6810
func_6832 = relay.Function([], output)
mod['func_6832'] = func_6832
mod = relay.transform.InferType()(mod)
output = func_6832()
func_6833 = relay.Function([], output)
mutated_mod['func_6833'] = func_6833
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5336_call = mod.get_global_var('func_5336')
func_5337_call = mutated_mod.get_global_var('func_5337')
call_6886 = relay.TupleGetItem(func_5336_call(), 0)
call_6887 = relay.TupleGetItem(func_5337_call(), 0)
output = call_6886
output2 = call_6887
func_6896 = relay.Function([], output)
mod['func_6896'] = func_6896
mod = relay.transform.InferType()(mod)
mutated_mod['func_6896'] = func_6896
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6896_call = mutated_mod.get_global_var('func_6896')
call_6897 = func_6896_call()
output = call_6897
func_6898 = relay.Function([], output)
mutated_mod['func_6898'] = func_6898
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5336_call = mod.get_global_var('func_5336')
func_5337_call = mutated_mod.get_global_var('func_5337')
call_6904 = relay.TupleGetItem(func_5336_call(), 0)
call_6905 = relay.TupleGetItem(func_5337_call(), 0)
output = call_6904
output2 = call_6905
func_6926 = relay.Function([], output)
mod['func_6926'] = func_6926
mod = relay.transform.InferType()(mod)
output = func_6926()
func_6927 = relay.Function([], output)
mutated_mod['func_6927'] = func_6927
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4581_call = mod.get_global_var('func_4581')
func_4582_call = mutated_mod.get_global_var('func_4582')
call_6977 = relay.TupleGetItem(func_4581_call(), 2)
call_6978 = relay.TupleGetItem(func_4582_call(), 2)
output = call_6977
output2 = call_6978
func_6991 = relay.Function([], output)
mod['func_6991'] = func_6991
mod = relay.transform.InferType()(mod)
mutated_mod['func_6991'] = func_6991
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6991_call = mutated_mod.get_global_var('func_6991')
call_6992 = func_6991_call()
output = call_6992
func_6993 = relay.Function([], output)
mutated_mod['func_6993'] = func_6993
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6597_call = mod.get_global_var('func_6597')
func_6599_call = mutated_mod.get_global_var('func_6599')
call_7020 = func_6597_call()
call_7021 = func_6597_call()
func_5861_call = mod.get_global_var('func_5861')
func_5863_call = mutated_mod.get_global_var('func_5863')
var_7028 = relay.var("var_7028", dtype = "float32", shape = (550,))#candidate|7028|(550,)|var|float32
call_7027 = func_5861_call(relay.reshape(var_7028.astype('float32'), [11, 10, 5]))
call_7029 = func_5861_call(relay.reshape(var_7028.astype('float32'), [11, 10, 5]))
output = relay.Tuple([call_7020,call_7027,var_7028,])
output2 = relay.Tuple([call_7021,call_7029,var_7028,])
func_7033 = relay.Function([var_7028,], output)
mod['func_7033'] = func_7033
mod = relay.transform.InferType()(mod)
var_7034 = relay.var("var_7034", dtype = "float32", shape = (550,))#candidate|7034|(550,)|var|float32
output = func_7033(var_7034)
func_7035 = relay.Function([var_7034], output)
mutated_mod['func_7035'] = func_7035
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5215_call = mod.get_global_var('func_5215')
func_5217_call = mutated_mod.get_global_var('func_5217')
call_7039 = relay.TupleGetItem(func_5215_call(), 0)
call_7040 = relay.TupleGetItem(func_5217_call(), 0)
func_5861_call = mod.get_global_var('func_5861')
func_5863_call = mutated_mod.get_global_var('func_5863')
var_7061 = relay.var("var_7061", dtype = "float32", shape = (550,))#candidate|7061|(550,)|var|float32
call_7060 = func_5861_call(relay.reshape(var_7061.astype('float32'), [11, 10, 5]))
call_7062 = func_5861_call(relay.reshape(var_7061.astype('float32'), [11, 10, 5]))
output = relay.Tuple([call_7039,call_7060,var_7061,])
output2 = relay.Tuple([call_7040,call_7062,var_7061,])
func_7063 = relay.Function([var_7061,], output)
mod['func_7063'] = func_7063
mod = relay.transform.InferType()(mod)
mutated_mod['func_7063'] = func_7063
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7064 = relay.var("var_7064", dtype = "float32", shape = (550,))#candidate|7064|(550,)|var|float32
func_7063_call = mutated_mod.get_global_var('func_7063')
call_7065 = func_7063_call(var_7064)
output = call_7065
func_7066 = relay.Function([var_7064], output)
mutated_mod['func_7066'] = func_7066
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7165 = relay.const([[[-6,6,-10,2,4,-7,-3,9,4,4,-2,-4,-10,-9,8],[8,-5,-8,1,-8,-10,-7,7,8,-10,7,-5,-6,-1,-4],[7,3,-8,-8,4,5,1,7,-10,1,7,-3,-8,-9,-5]],[[10,-9,-7,-5,-6,-1,3,5,-3,-4,8,-4,-6,-1,3],[-2,-10,-7,7,-2,-3,6,-8,-5,-9,-7,10,9,4,-3],[-7,-2,-3,6,3,7,-2,1,5,10,2,-2,-9,-10,-2]],[[-3,-5,8,6,-2,-3,-4,-1,6,10,1,-7,6,-5,-2],[7,-7,-2,4,10,-8,2,-1,-8,8,-7,10,3,10,2],[6,7,4,8,-7,4,3,-9,9,-1,5,-8,-10,1,-1]],[[-1,-4,8,-6,-6,5,10,5,2,7,1,-3,-7,9,2],[10,-7,-2,2,3,4,-7,-8,6,-6,-5,-4,-5,-1,8],[-4,-9,-3,-6,-2,5,9,-2,6,-6,10,-9,-10,-7,9]],[[-6,-6,-6,9,-5,2,-7,-4,7,7,-4,7,-1,-10,-9],[6,3,-2,10,-2,-2,-5,-5,-8,-8,-6,-9,-6,9,1],[-6,-5,8,10,9,-2,-8,8,5,8,10,-8,8,-1,1]]], dtype = "int8")#candidate|7165|(5, 3, 15)|const|int8
var_7166 = relay.var("var_7166", dtype = "int8", shape = (5, 3, 15))#candidate|7166|(5, 3, 15)|var|int8
bop_7167 = relay.bitwise_xor(const_7165.astype('int8'), relay.reshape(var_7166.astype('int8'), relay.shape_of(const_7165))) # shape=(5, 3, 15)
output = bop_7167
output2 = bop_7167
func_7184 = relay.Function([var_7166,], output)
mod['func_7184'] = func_7184
mod = relay.transform.InferType()(mod)
var_7185 = relay.var("var_7185", dtype = "int8", shape = (5, 3, 15))#candidate|7185|(5, 3, 15)|var|int8
output = func_7184(var_7185)
func_7186 = relay.Function([var_7185], output)
mutated_mod['func_7186'] = func_7186
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6991_call = mod.get_global_var('func_6991')
func_6993_call = mutated_mod.get_global_var('func_6993')
call_7215 = func_6991_call()
call_7216 = func_6991_call()
func_4510_call = mod.get_global_var('func_4510')
func_4512_call = mutated_mod.get_global_var('func_4512')
call_7256 = relay.TupleGetItem(func_4510_call(), 0)
call_7257 = relay.TupleGetItem(func_4512_call(), 0)
output = relay.Tuple([call_7215,call_7256,])
output2 = relay.Tuple([call_7216,call_7257,])
func_7264 = relay.Function([], output)
mod['func_7264'] = func_7264
mod = relay.transform.InferType()(mod)
mutated_mod['func_7264'] = func_7264
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7264_call = mutated_mod.get_global_var('func_7264')
call_7265 = func_7264_call()
output = call_7265
func_7266 = relay.Function([], output)
mutated_mod['func_7266'] = func_7266
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5058_call = mod.get_global_var('func_5058')
func_5060_call = mutated_mod.get_global_var('func_5060')
call_7319 = relay.TupleGetItem(func_5058_call(), 1)
call_7320 = relay.TupleGetItem(func_5060_call(), 1)
output = relay.Tuple([call_7319,])
output2 = relay.Tuple([call_7320,])
func_7342 = relay.Function([], output)
mod['func_7342'] = func_7342
mod = relay.transform.InferType()(mod)
output = func_7342()
func_7343 = relay.Function([], output)
mutated_mod['func_7343'] = func_7343
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6273_call = mod.get_global_var('func_6273')
func_6275_call = mutated_mod.get_global_var('func_6275')
call_7355 = relay.TupleGetItem(func_6273_call(), 0)
call_7356 = relay.TupleGetItem(func_6275_call(), 0)
output = relay.Tuple([call_7355,])
output2 = relay.Tuple([call_7356,])
func_7360 = relay.Function([], output)
mod['func_7360'] = func_7360
mod = relay.transform.InferType()(mod)
mutated_mod['func_7360'] = func_7360
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7360_call = mutated_mod.get_global_var('func_7360')
call_7361 = func_7360_call()
output = call_7361
func_7362 = relay.Function([], output)
mutated_mod['func_7362'] = func_7362
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6083_call = mod.get_global_var('func_6083')
func_6085_call = mutated_mod.get_global_var('func_6085')
call_7383 = relay.TupleGetItem(func_6083_call(), 1)
call_7384 = relay.TupleGetItem(func_6085_call(), 1)
output = call_7383
output2 = call_7384
func_7389 = relay.Function([], output)
mod['func_7389'] = func_7389
mod = relay.transform.InferType()(mod)
mutated_mod['func_7389'] = func_7389
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7389_call = mutated_mod.get_global_var('func_7389')
call_7390 = func_7389_call()
output = call_7390
func_7391 = relay.Function([], output)
mutated_mod['func_7391'] = func_7391
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5774_call = mod.get_global_var('func_5774')
func_5775_call = mutated_mod.get_global_var('func_5775')
call_7397 = relay.TupleGetItem(func_5774_call(), 0)
call_7398 = relay.TupleGetItem(func_5775_call(), 0)
var_7425 = relay.var("var_7425", dtype = "float64", shape = (7, 16, 7))#candidate|7425|(7, 16, 7)|var|float64
bop_7426 = relay.left_shift(call_7397.astype('uint32'), relay.reshape(var_7425.astype('uint32'), relay.shape_of(call_7397))) # shape=(7, 16, 7)
bop_7429 = relay.left_shift(call_7398.astype('uint32'), relay.reshape(var_7425.astype('uint32'), relay.shape_of(call_7398))) # shape=(7, 16, 7)
func_7360_call = mod.get_global_var('func_7360')
func_7362_call = mutated_mod.get_global_var('func_7362')
call_7430 = relay.TupleGetItem(func_7360_call(), 0)
call_7431 = relay.TupleGetItem(func_7362_call(), 0)
uop_7443 = relay.atan(bop_7426.astype('float32')) # shape=(7, 16, 7)
uop_7445 = relay.atan(bop_7429.astype('float32')) # shape=(7, 16, 7)
func_3937_call = mod.get_global_var('func_3937')
func_3940_call = mutated_mod.get_global_var('func_3940')
var_7448 = relay.var("var_7448", dtype = "int8", shape = (90,))#candidate|7448|(90,)|var|int8
var_7449 = relay.var("var_7449", dtype = "int8", shape = (180,))#candidate|7449|(180,)|var|int8
call_7447 = func_3937_call(relay.reshape(var_7448.astype('int8'), [1, 10, 9]), relay.reshape(var_7449.astype('int8'), [2, 10, 9]), )
call_7450 = func_3937_call(relay.reshape(var_7448.astype('int8'), [1, 10, 9]), relay.reshape(var_7449.astype('int8'), [2, 10, 9]), )
func_7342_call = mod.get_global_var('func_7342')
func_7343_call = mutated_mod.get_global_var('func_7343')
call_7465 = relay.TupleGetItem(func_7342_call(), 0)
call_7466 = relay.TupleGetItem(func_7343_call(), 0)
output = relay.Tuple([call_7430,uop_7443,call_7447,var_7448,var_7449,call_7465,])
output2 = relay.Tuple([call_7431,uop_7445,call_7450,var_7448,var_7449,call_7466,])
func_7476 = relay.Function([var_7425,var_7448,var_7449,], output)
mod['func_7476'] = func_7476
mod = relay.transform.InferType()(mod)
var_7477 = relay.var("var_7477", dtype = "float64", shape = (7, 16, 7))#candidate|7477|(7, 16, 7)|var|float64
var_7478 = relay.var("var_7478", dtype = "int8", shape = (90,))#candidate|7478|(90,)|var|int8
var_7479 = relay.var("var_7479", dtype = "int8", shape = (180,))#candidate|7479|(180,)|var|int8
output = func_7476(var_7477,var_7478,var_7479,)
func_7480 = relay.Function([var_7477,var_7478,var_7479,], output)
mutated_mod['func_7480'] = func_7480
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6083_call = mod.get_global_var('func_6083')
func_6085_call = mutated_mod.get_global_var('func_6085')
call_7504 = relay.TupleGetItem(func_6083_call(), 1)
call_7505 = relay.TupleGetItem(func_6085_call(), 1)
func_7264_call = mod.get_global_var('func_7264')
func_7266_call = mutated_mod.get_global_var('func_7266')
call_7524 = relay.TupleGetItem(func_7264_call(), 1)
call_7525 = relay.TupleGetItem(func_7266_call(), 1)
output = relay.Tuple([call_7504,call_7524,])
output2 = relay.Tuple([call_7505,call_7525,])
func_7537 = relay.Function([], output)
mod['func_7537'] = func_7537
mod = relay.transform.InferType()(mod)
mutated_mod['func_7537'] = func_7537
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7537_call = mutated_mod.get_global_var('func_7537')
call_7538 = func_7537_call()
output = call_7538
func_7539 = relay.Function([], output)
mutated_mod['func_7539'] = func_7539
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6832_call = mod.get_global_var('func_6832')
func_6833_call = mutated_mod.get_global_var('func_6833')
call_7554 = func_6832_call()
call_7555 = func_6832_call()
func_6529_call = mod.get_global_var('func_6529')
func_6531_call = mutated_mod.get_global_var('func_6531')
call_7578 = relay.TupleGetItem(func_6529_call(), 0)
call_7579 = relay.TupleGetItem(func_6531_call(), 0)
output = relay.Tuple([call_7554,call_7578,])
output2 = relay.Tuple([call_7555,call_7579,])
func_7616 = relay.Function([], output)
mod['func_7616'] = func_7616
mod = relay.transform.InferType()(mod)
output = func_7616()
func_7617 = relay.Function([], output)
mutated_mod['func_7617'] = func_7617
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4611_call = mod.get_global_var('func_4611')
func_4613_call = mutated_mod.get_global_var('func_4613')
call_7663 = func_4611_call()
call_7664 = func_4611_call()
func_4908_call = mod.get_global_var('func_4908')
func_4910_call = mutated_mod.get_global_var('func_4910')
call_7671 = relay.TupleGetItem(func_4908_call(), 0)
call_7672 = relay.TupleGetItem(func_4910_call(), 0)
func_5312_call = mod.get_global_var('func_5312')
func_5315_call = mutated_mod.get_global_var('func_5315')
var_7684 = relay.var("var_7684", dtype = "float32", shape = ())#candidate|7684|()|var|float32
var_7685 = relay.var("var_7685", dtype = "uint16", shape = (432, 2))#candidate|7685|(432, 2)|var|uint16
call_7683 = relay.TupleGetItem(func_5312_call(relay.reshape(var_7684.astype('float32'), []), relay.reshape(var_7685.astype('uint16'), [864,]), ), 7)
call_7686 = relay.TupleGetItem(func_5315_call(relay.reshape(var_7684.astype('float32'), []), relay.reshape(var_7685.astype('uint16'), [864,]), ), 7)
func_2677_call = mod.get_global_var('func_2677')
func_2682_call = mutated_mod.get_global_var('func_2682')
const_7689 = relay.const([-2,3,8,-3,-5,3,-5,4,1,10,2,3,9,10,-2,-9,-3,-4,-2,-4,-3,10,1,9,5,-2,-1,10,6,9,-2,-2,3,-5,-2,-3,-6,-3,6,-9,-3,5,-3,-5,-6,6,-5,2,-2,-4,-6,9,9,-8,-6,-3,5,5,4,6,-4,-7,-1,-8,5,-9,-10,-2,-10,3,5,-7,5,-10,-1,8,-1,6,-3,-6,8,-1,6,7,-4,-4,-8,1,10,-10,-10,-6,-3,-4,1,-7,7,-9,-1,-9,-7,-6,-3,-8,-10,5,9,10,8,-8,-6,-7,-3,8,-3,9,-1,6,-1,8,-3,1,6,3,7,-10,8,-8,2,-7,4,-6,2,-8,4,-4,10,-10,9,10,-7,-9,-8,10,-4,8,4,2,3,6,-7,-6,-6,-5,2,-10,-8,5,-7,-7,-1,-8,8,-8,-1,8,-7,-7,3,-9,-7,-5,8,-10,-5,8,3,-9,-8,-10,3,5,6,-2,-3,-3,10,5,8,-4,2,8,-10,6,6,-6,-6,1,-4,1,6,8,-4,3,-6,-6,1,-6,1,-10,10,9,7,-9,3,-6,8,2,-7,-5,-5,3,-4,-8,1,-5,-2,-6,-2,-7,5,-3,-7,4,-3,-7,1,-4,-9,2,-8,8,1,6,10,-10,9,7,-10,10,-3,10,6,-1,-6,-4,1,-2,-7,6,4,-2,9,8,4,3,-6,-1,8,-7,4,7,-5,-8,1,-10,1,-7,3,10,-3,5,7,-2,-8,7,2,9,-7,10,4,3,3,-6,5,-4,-10,-8,4,1,-8,-6,-6,-8,4,3,9,3,-5,-8,6,9,-4,-4,4,2,8,4,5,-7,7,8,5,8,2,-10,-2,6,-5,-4,-8,3,-4,-7,7,1,5,2,3,-2,7,-3,3,3,-10,7,3,3,6,-10,8,-9,-3,5,-10,-2,10,-8,-7,-1,9,-6,-7,-4,10,8,-7,1,7,-7,4,5,-7,7,5,-2,5,7,-6,6,6,4,-10,-3,-10,3,-2,-7,3,-4,1,3,3,-7,2,4,7,1,-4,2,7,-9,-8,-9,-10,1,6,-7,-5,-7,-8,-5,1,-2,-10,-1,4,5,6,-6,6,8,-3,-10,-1,-7,10,-6,8,5,4,5,6,3,6,10,7,4,5,10,3,-5,-7,-3,8,-3,6,4,7,-3,7,5,-1,3,6,-2,-1,1,7,-3,4,9,1,1,3,1,9,-3,8,6,1,3,4,-8,-10,6,-6,-3,2,-6,-9,-2,-6,9,-1,6,-5,-4,2,10,4,5,4,-8,1,-9,3,-9,6,-3,-2,-1,-9,-6,6,3,3,-9,-6,-1,-2,-9,2,6,-7,7,9,8,2,6,-9,7,9,-9,4,3,-2,1,-10,4,-5,7,-6,1,-9,5,8,-2,-7,-9,2,-6,-4,-8,5,4,-2,5,5,7,3,-4,3,7,8,2,-9,6,-7,-10,6,-4,4,-6,5,7,-5,-10,-8,8,-4,7,9,7,-8,10,-10,2,-4,-4,-4,-1,-1,-7,10,6,8,-7,5,-4,-2,6,-7,-7,9,-3,4,1,-7,-6,-4,10,6,-10,3,3,-6,-9,-9,7,-8,10,6,-9,8,9,8,5,-9,4,-8,-7,-9,-1,-3,-6,-1,-4,8,2,-9,-9,2,-10,10,5,4,-4,8,-9,4,-3,4,3,-1,5,8,6,9,-3,1,-6,-9,5,-6,10,4,6,-1,7,6,1,-7,5,4,-4,5,-9,8,4,2,3,-7,1,10,3,1,1,2,5,-6,-2,-7,-5,-7,-1,3,3,7,-10,-4,-4,-9,-3,2,7,-7,7,10,-10,-1,3,7,5,-2,10,10,-10,-10,9,3,10,-5,-3,-10,-1,6,-6,2,8,6,9,-3,-4,4,-6,9,6,-2,-8,-1,-7,3,-1,-3,-8,-8,-5,-7,-5,2,9,-5,3,3,-4,-10,-3,-2,-9,-3,6,-5,-2,1,7,-9,5,3,-3,-1,3,8,6,10,9,-4,5,-7,4,-4,-3,9,-7,8,-9,1,-2,-7,10,-8,9,5,1,-2,-4,-8,-9,7,-9,10,-5,9,-1,-10,2,-2,-7,-6,1,-5,-6,3,10,-3,-6,7,5,1,-2,9,-8,-4,7,5,-10,4,5,-1,-9,6,-1,-9,10,-2,-2,4,-9,-6,2,8,-4,-10,-2,-6,7,-6,-8,5,-4,8,-6,-5,5,-5,3,-1,-6,7,-1,-8,-6,9,7,10,8,9,-4,-1,8,-6,-9,-9,7,4,-9,-8,-5,9,-8,-7,-8,-2,-3,-1,-3,3,3,9,-9,10,3,3,5,-2,-10,3,5,2,2,-10,-2,7,6,7,-8,3,7,9,-7,-8,8,-9,-9,-3,-6,-6,-8,6,-8,9,-2,-5,-10,2,5,-6,-1,8,-8,1,-1,-2,7,-3,1,-10,6,-1,-10,-6,2,10,9,-3,6,-10,-8,-6,-10,-1,2,-5,7,-7,-2,-3,-6,-8,-8,1,3,-1,-4,8,-5,-7,8,-7,2,1,-8,-8,7,7,-7,9,10,2,6,-7,9,-8,-8,4,-9,-3,1,-1,-5,4,-9,-1,3,-10,-5,2,1,-3,-6,-8,-3,-4,-10,3,-3,7,-1,10,4,-5,-9,3,6,10,2,-9,-8,-9,7,-6,-10,4,-5,-5,8,-8,-4,8,8,6,-5,6,7,4,9,4,-4,1,5,-8,4,8,10,2,4,-9,2,-4,1,10,-9,9,3,3,-6,10,1,-9,-6], dtype = "int8")#candidate|7689|(1050,)|const|int8
var_7690 = relay.var("var_7690", dtype = "uint8", shape = (432,))#candidate|7690|(432,)|var|uint8
call_7688 = relay.TupleGetItem(func_2677_call(relay.reshape(const_7689.astype('int8'), [15, 5, 14]), relay.reshape(const_7689.astype('int8'), [15, 5, 14]), relay.reshape(const_7689.astype('int8'), [15, 5, 14]), relay.reshape(var_7690.astype('uint8'), [432,]), ), 4)
call_7691 = relay.TupleGetItem(func_2682_call(relay.reshape(const_7689.astype('int8'), [15, 5, 14]), relay.reshape(const_7689.astype('int8'), [15, 5, 14]), relay.reshape(const_7689.astype('int8'), [15, 5, 14]), relay.reshape(var_7690.astype('uint8'), [432,]), ), 4)
output = relay.Tuple([call_7663,call_7671,call_7683,var_7684,var_7685,call_7688,const_7689,var_7690,])
output2 = relay.Tuple([call_7664,call_7672,call_7686,var_7684,var_7685,call_7691,const_7689,var_7690,])
func_7692 = relay.Function([var_7684,var_7685,var_7690,], output)
mod['func_7692'] = func_7692
mod = relay.transform.InferType()(mod)
mutated_mod['func_7692'] = func_7692
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7692_call = mutated_mod.get_global_var('func_7692')
var_7694 = relay.var("var_7694", dtype = "float32", shape = ())#candidate|7694|()|var|float32
var_7695 = relay.var("var_7695", dtype = "uint16", shape = (432, 2))#candidate|7695|(432, 2)|var|uint16
var_7696 = relay.var("var_7696", dtype = "uint8", shape = (432,))#candidate|7696|(432,)|var|uint8
call_7693 = func_7692_call(var_7694,var_7695,var_7696,)
output = call_7693
func_7697 = relay.Function([var_7694,var_7695,var_7696,], output)
mutated_mod['func_7697'] = func_7697
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6119_call = mod.get_global_var('func_6119')
func_6120_call = mutated_mod.get_global_var('func_6120')
call_7728 = relay.TupleGetItem(func_6119_call(), 0)
call_7729 = relay.TupleGetItem(func_6120_call(), 0)
uop_7742 = relay.log(call_7728.astype('float64')) # shape=(6, 12, 6)
uop_7744 = relay.log(call_7729.astype('float64')) # shape=(6, 12, 6)
func_4853_call = mod.get_global_var('func_4853')
func_4855_call = mutated_mod.get_global_var('func_4855')
call_7750 = relay.TupleGetItem(func_4853_call(), 1)
call_7751 = relay.TupleGetItem(func_4855_call(), 1)
func_7184_call = mod.get_global_var('func_7184')
func_7186_call = mutated_mod.get_global_var('func_7186')
var_7774 = relay.var("var_7774", dtype = "int8", shape = (225,))#candidate|7774|(225,)|var|int8
call_7773 = func_7184_call(relay.reshape(var_7774.astype('int8'), [5, 3, 15]))
call_7775 = func_7184_call(relay.reshape(var_7774.astype('int8'), [5, 3, 15]))
output = relay.Tuple([uop_7742,call_7750,call_7773,var_7774,])
output2 = relay.Tuple([uop_7744,call_7751,call_7775,var_7774,])
func_7777 = relay.Function([var_7774,], output)
mod['func_7777'] = func_7777
mod = relay.transform.InferType()(mod)
var_7778 = relay.var("var_7778", dtype = "int8", shape = (225,))#candidate|7778|(225,)|var|int8
output = func_7777(var_7778)
func_7779 = relay.Function([var_7778], output)
mutated_mod['func_7779'] = func_7779
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7537_call = mod.get_global_var('func_7537')
func_7539_call = mutated_mod.get_global_var('func_7539')
call_7792 = relay.TupleGetItem(func_7537_call(), 1)
call_7793 = relay.TupleGetItem(func_7539_call(), 1)
uop_7802 = relay.atan(call_7792.astype('float32')) # shape=(8, 7, 11)
uop_7804 = relay.atan(call_7793.astype('float32')) # shape=(8, 7, 11)
func_6499_call = mod.get_global_var('func_6499')
func_6501_call = mutated_mod.get_global_var('func_6501')
call_7807 = relay.TupleGetItem(func_6499_call(), 1)
call_7808 = relay.TupleGetItem(func_6501_call(), 1)
output = relay.Tuple([uop_7802,call_7807,])
output2 = relay.Tuple([uop_7804,call_7808,])
func_7812 = relay.Function([], output)
mod['func_7812'] = func_7812
mod = relay.transform.InferType()(mod)
output = func_7812()
func_7813 = relay.Function([], output)
mutated_mod['func_7813'] = func_7813
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6896_call = mod.get_global_var('func_6896')
func_6898_call = mutated_mod.get_global_var('func_6898')
call_7841 = func_6896_call()
call_7842 = func_6896_call()
func_2836_call = mod.get_global_var('func_2836')
func_2839_call = mutated_mod.get_global_var('func_2839')
call_7853 = func_2836_call(relay.reshape(call_7841.astype('uint32'), [5, 3, 16]), relay.reshape(call_7841.astype('uint32'), [5, 3, 16]), )
call_7854 = func_2836_call(relay.reshape(call_7841.astype('uint32'), [5, 3, 16]), relay.reshape(call_7841.astype('uint32'), [5, 3, 16]), )
func_7476_call = mod.get_global_var('func_7476')
func_7480_call = mutated_mod.get_global_var('func_7480')
const_7858 = relay.const([-6.817813,-7.142978,-5.060497,-0.404094,-7.636324,5.530522,3.110345,-2.133251,9.351579,5.995722,5.549543,-4.690165,-3.018996,-9.019819,7.238519,-5.432477,-2.858926,-1.968843,3.222323,7.171613,-0.537352,8.319868,-4.410553,-5.347322,-6.188709,-5.469998,-2.053382,-8.779992,0.478816,-7.352186,-7.144879,-4.038243,4.270377,0.433232,0.294766,-0.781684,-7.750204,2.677922,3.781976,-2.984254,1.702851,6.044377,3.110992,3.512516,0.360358,7.237169,-3.788049,-4.783152,0.289425,-0.238850,6.348055,-0.894365,-7.176725,-2.880771,0.363512,-7.622143,5.863740,-8.327769,7.332756,9.931074,3.495654,6.039957,-4.563259,4.083486,9.011284,-4.621556,-6.291621,-3.867056,-3.163752,4.453785,9.560050,1.333147,9.708937,3.828216,7.971728,0.252388,-7.745782,-3.380620,2.924971,-9.388309,-2.326741,2.032325,5.162037,5.072382,-9.790848,8.223216,-8.498896,-0.891562,-3.604079,4.680291,1.514306,-6.342945,1.207198,-8.062058,-5.697510,5.663540,-4.117657,7.042569,0.944963,8.019980,5.179476,8.699616,9.772055,-7.783516,-8.431994,4.586370,-4.223751,6.862152,5.497666,-2.462035,-2.528491,-2.076143,-1.110179,-4.061657,-1.299778,2.862444,-2.995815,-8.108269,4.298332,8.335010,-5.338118,9.471268,-0.535591,-2.605617,-5.522566,1.331954,-9.579115,5.359737,2.640743,-4.735794,-9.561853,-4.808721,6.725645,-1.138152,1.027422,-0.853162,3.310388,-1.040756,-7.385476,2.019498,-0.726967,4.551451,-6.131573,0.283057,-4.365954,2.821207,-8.856988,7.368354,-7.841413,-5.329065,7.601969,8.803603,-3.416260,-2.370835,-3.261813,4.969443,-0.559336,-3.465633,-7.937576,-9.946911,1.912438,1.006786,9.193599,9.275176,-4.610661,5.015659,-2.149879,-4.674924,1.925069,2.793081,-3.693858,-7.214768,2.060349,3.386277,-3.849406,-6.965442,-2.434818,0.350989,-4.127051,9.896588,-0.412573,-0.940147,-2.219624,2.214764,5.286093,1.469273,-2.934742,-6.426952,-1.900294,9.823604,-4.234552,6.094428,3.929120,-1.825608,4.928267,-1.154609,0.872845,9.349168,-2.858583,8.971728,8.118629,7.845169,-0.974781,-7.142463,-1.827041,9.267239,8.680057,1.009588,-2.604429,0.405056,6.143115,7.081244,-4.484205,-8.955868,-6.893401,1.365037,9.344798,1.238263,-3.342052,-1.401855,0.420846,5.823299,-3.978066,3.626572,6.143260,3.529097,-7.446687,1.485565,9.642440,8.982516,3.902334,6.140605,-0.959831,-3.082083,-0.930603,9.305508,-2.051035,4.635821,4.569174,1.779217,2.060356,3.796111,-4.684068,-1.977529,3.053992,6.406260,-3.431723,6.562947,0.950761,-3.062645,-4.673291,1.309291,-6.455117,-5.518965,4.564478,-7.252513,-4.075320,-9.805660,-0.053828,-6.276242,9.728984,-0.731194,-8.922963,-9.875869,6.562709,-8.170128,-1.511025,1.452449,-1.613290,-4.275165,7.869255,-8.363962,-4.839964,-1.312422,3.830774,-0.517207,-4.632759,9.821017,-3.087520,-6.946866,-6.975476,-2.879271,-9.820840,8.434877,6.403441,-9.544570,7.279671,-8.862578,-5.036434,-4.962386,7.360107,-9.524335,-1.373584,-7.098318,0.972315,-3.965460,1.696125,-0.901329,-0.045617,-4.912443,8.798629,2.629692,8.710893,-3.874971,-4.315294,-9.871110,-0.013490,-1.896236,-1.643145,4.406142,6.575122,1.524194,-0.480591,1.945171,0.648976,-5.408705,-7.685698,1.058679,7.332888,3.965162,4.576719,6.317714,-6.797236,-3.087453,5.179981,-7.096859,7.146038,5.064152,9.917844,5.806991,6.210698,7.083846,0.046472,0.619497,4.307307,-2.557740,-0.429448,-6.701351,3.736070,0.281125,-0.698876,-6.859714,1.499406,-6.962626,-9.839409,-9.502568,7.209209,4.441237,-5.343634,-4.982450,-6.059765,-8.527427,-3.497282,8.323685,1.729909,-6.164328,4.608099,-7.165700,4.897650,0.445829,-8.546186,5.302964,-9.210639,-9.949113,3.632293,-0.056167,7.701695,5.731795,7.027199,-0.493344,1.135050,-3.213483,4.894747,-4.888511,7.093236,-7.373933,4.821949,-6.532320,-8.804904,-0.227661,1.733760,9.408145,-9.618073,-3.344674,-8.590177,-2.570362,-2.155980,-4.424013,1.505918,-3.802996,-5.003707,-8.608899,-6.685692,2.657541,8.145250,-4.993559,-4.686326,-4.719568,-5.589259,-1.961382,6.772344,1.804200,-1.101661,3.978777,-7.037275,-3.184392,-4.792578,-2.974697,0.943693,9.049898,0.363922,0.750272,-4.444213,-6.010865,7.285070,3.996199,-4.028843,-8.053825,-6.448822,-3.773437,8.186531,2.135869,-8.107055,-0.795197,-0.289302,-9.762930,7.120874,8.808006,1.949796,8.843813,0.193410,6.675828,8.595645,-3.995549,1.445557,-7.056822,1.641361,-6.145984,9.672754,-1.349966,9.106348,2.577803,-8.621308,-9.281741,2.405798,-2.141797,-9.530695,-1.765916,4.857269,4.819821,7.992899,7.755479,0.317476,-6.639351,-3.120896,-1.485375,-9.029015,0.089107,6.357398,-6.230467,6.905510,4.944673,8.912381,0.634215,-6.379496,8.511370,-5.762786,-3.980059,2.400369,-8.707087,5.487069,8.137426,-5.656312,1.787841,-2.626719,-5.910244,-5.174570,9.116572,9.432475,5.277320,0.310109,-2.757200,9.212845,1.453835,2.859755,4.715257,3.956996,-6.365347,5.775912,7.620953,-1.314210,5.727366,4.486151,-5.602017,0.540743,-7.931018,-1.921420,-6.273563,8.486446,-1.826142,4.871224,-3.869399,-8.942241,-4.094033,-8.016026,4.588113,-3.950284,0.738197,8.546850,-4.070204,3.779791,0.338283,1.915379,-9.763062,-5.191807,-6.614586,-5.725808,-9.280181,5.081869,-3.135254,-9.472441,-9.808002,-9.606455,-2.183825,2.594966,-6.406762,7.022178,5.987252,9.392174,7.003124,-2.986581,6.011823,-2.191049,-2.539088,-5.281699,8.390740,-5.911265,3.152449,-3.816734,3.438362,5.629331,-5.980510,0.854541,8.654833,3.743822,-1.719075,-9.166967,-1.662938,3.924329,8.803060,8.157406,-0.563485,-5.805871,-9.531141,6.777799,3.551208,3.528796,7.678932,7.041015,3.396102,-6.417006,-3.115703,4.627603,9.553180,2.540524,0.350898,-3.278256,0.051394,1.957043,0.245597,6.340332,1.759136,-7.036046,4.601779,-0.648871,5.115908,7.169986,6.040230,-8.056624,8.459433,7.097646,8.533909,0.819666,6.271003,-0.975683,1.137730,2.341924,8.669297,-4.583839,6.483446,0.602189,7.158732,-3.859589,-7.399346,6.195762,6.799183,-5.092354,-3.548531,2.719569,-3.829300,-1.283276,9.938784,6.185617,-7.604294,3.989172,-8.603427,-8.464425,4.006089,-3.434326,4.895916,-4.560903,1.508448,2.519235,-3.460992,0.102871,3.072659,-5.269017,4.038615,1.073271,8.343477,6.952398,7.455634,2.468675,-6.987467,-2.462873,-1.422735,-2.127822,5.372816,5.007539,-7.769010,9.389570,2.692179,-8.568652,8.419932,-0.125158,1.427376,-5.881478,9.589614,5.475428,0.674023,0.824320,-5.750614,2.479627,-0.571112,4.116556,0.141030,-2.925701,5.420000,0.681624,-1.301842,4.395415,9.438681,-4.373049,-3.733657,7.062554,-9.568685,6.341083,-4.671240,-0.296008,8.555577,-7.125446,-4.290171,3.247493,8.509062,-0.259525,-6.057584,1.772046,3.794234,-7.571173,-1.115962,-8.629590,1.172370,4.423821,-0.896048,-3.285284,-1.898659,3.001076,6.251008,-2.519107,5.035716,-5.366249,-9.792825,-4.236996,3.714826,2.063970,-9.298466,-4.912541,4.300244,5.190285,-8.071718,-7.882914,-2.470324,7.011189,-7.501631,3.207072,7.058119,-3.378495,2.710727,6.960018,8.118323,-8.524619,-2.930404,9.625875,2.859191,-6.736918,-2.401947,-4.420094,-4.666932,-5.547097,0.688170,-5.610809,3.810028,-7.931718,8.321933,-7.747691,5.666843,-5.058016,5.655529,7.104167,0.973081,-2.248924,-1.595087,-0.189277,4.361450,-5.551506,-7.870213,1.828666,1.403831,5.546109,8.079680,2.263872,-5.975751,7.628314,-2.626238,-1.325620,-4.298462,6.244314,1.958011,8.099131,5.009938,8.446584,-4.616497,1.767227,9.995602,2.097494,-3.700107,2.445247,-2.861597,1.579308,9.053197,-2.249455,-7.526071,6.302058,-5.773732,-7.617550,-2.080276,9.613290,-5.378591,-9.298619,8.680898,7.885096,-6.337314,6.356798,4.212585,4.159686,-9.986868,-8.017490,-8.774635,1.121999,-8.655186,-1.102735,7.188535,5.438953,-3.192875,0.954419,8.684692,-6.557583,6.556405,5.296533,-7.419255,-5.961073,-3.628176,2.677261,-1.653828], dtype = "float64")#candidate|7858|(784,)|const|float64
const_7859 = relay.const([-9,-10,-6,-7,-6,2,-1,-6,10,9,-9,7,-9,-9,1,2,4,-4,5,-3,-2,-5,-7,1,2,5,1,3,9,4,8,10,8,-2,7,-1,10,3,9,-9,4,-4,7,4,-1,-8,8,1,-3,-6,6,-1,-7,6,-10,7,-10,-10,-8,3,-7,-8,-8,-9,-2,1,-4,6,9,-7,8,3,-7,-3,9,6,-6,9,5,-6,4,-5,-2,-2,-7,-9,7,3,5,10], dtype = "int8")#candidate|7859|(90,)|const|int8
const_7860 = relay.const([-10,-3,4,6,5,9,-10,2,-9,-3,4,-10,-5,-4,-1,-3,7,-7,-4,-4,4,-8,2,8,-9,-2,2,-1,-9,4,-3,8,-3,-4,9,-5,-9,9,4,-5,-2,-7,10,-3,-2,-8,4,-6,2,-5,6,-8,-4,8,-6,-3,1,5,8,2,-5,-7,-8,-5,1,-5,-9,-3,2,2,-4,8,-5,-9,-1,4,-3,2,-2,-4,-8,-1,4,9,-5,3,6,-7,2,-5,-6,8,10,1,-10,6,-5,-2,-10,4,4,7,7,-4,-9,-4,7,-4,-6,8,1,-2,10,-7,9,-10,-9,4,10,-6,6,-5,6,2,4,7,-4,4,-5,6,2,-8,2,6,-1,-2,6,1,-7,-3,-1,-6,9,10,-3,-9,-2,-8,8,-8,-10,-5,-10,-6,9,7,8,-6,-5,3,3,-5,-9,-1,8,-6,-2,3,-7,-10,-8,8,-10,7,1,5,1,8,4,-5], dtype = "int8")#candidate|7860|(180,)|const|int8
call_7857 = relay.TupleGetItem(func_7476_call(relay.reshape(const_7858.astype('float64'), [7, 16, 7]), relay.reshape(const_7859.astype('int8'), [90,]), relay.reshape(const_7860.astype('int8'), [180,]), ), 0)
call_7861 = relay.TupleGetItem(func_7480_call(relay.reshape(const_7858.astype('float64'), [7, 16, 7]), relay.reshape(const_7859.astype('int8'), [90,]), relay.reshape(const_7860.astype('int8'), [180,]), ), 0)
output = relay.Tuple([call_7841,call_7853,call_7857,const_7858,const_7859,const_7860,])
output2 = relay.Tuple([call_7842,call_7854,call_7861,const_7858,const_7859,const_7860,])
func_7863 = relay.Function([], output)
mod['func_7863'] = func_7863
mod = relay.transform.InferType()(mod)
mutated_mod['func_7863'] = func_7863
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7863_call = mutated_mod.get_global_var('func_7863')
call_7864 = func_7863_call()
output = call_7864
func_7865 = relay.Function([], output)
mutated_mod['func_7865'] = func_7865
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4611_call = mod.get_global_var('func_4611')
func_4613_call = mutated_mod.get_global_var('func_4613')
call_7897 = func_4611_call()
call_7898 = func_4611_call()
output = relay.Tuple([call_7897,])
output2 = relay.Tuple([call_7898,])
func_7901 = relay.Function([], output)
mod['func_7901'] = func_7901
mod = relay.transform.InferType()(mod)
mutated_mod['func_7901'] = func_7901
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7901_call = mutated_mod.get_global_var('func_7901')
call_7902 = func_7901_call()
output = call_7902
func_7903 = relay.Function([], output)
mutated_mod['func_7903'] = func_7903
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5841_call = mod.get_global_var('func_5841')
func_5842_call = mutated_mod.get_global_var('func_5842')
call_7952 = relay.TupleGetItem(func_5841_call(), 0)
call_7953 = relay.TupleGetItem(func_5842_call(), 0)
output = relay.Tuple([call_7952,])
output2 = relay.Tuple([call_7953,])
func_7965 = relay.Function([], output)
mod['func_7965'] = func_7965
mod = relay.transform.InferType()(mod)
output = func_7965()
func_7966 = relay.Function([], output)
mutated_mod['func_7966'] = func_7966
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7616_call = mod.get_global_var('func_7616')
func_7617_call = mutated_mod.get_global_var('func_7617')
call_7967 = relay.TupleGetItem(func_7616_call(), 0)
call_7968 = relay.TupleGetItem(func_7617_call(), 0)
output = relay.Tuple([call_7967,])
output2 = relay.Tuple([call_7968,])
func_7985 = relay.Function([], output)
mod['func_7985'] = func_7985
mod = relay.transform.InferType()(mod)
mutated_mod['func_7985'] = func_7985
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7985_call = mutated_mod.get_global_var('func_7985')
call_7986 = func_7985_call()
output = call_7986
func_7987 = relay.Function([], output)
mutated_mod['func_7987'] = func_7987
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5841_call = mod.get_global_var('func_5841')
func_5842_call = mutated_mod.get_global_var('func_5842')
call_8006 = relay.TupleGetItem(func_5841_call(), 0)
call_8007 = relay.TupleGetItem(func_5842_call(), 0)
func_7389_call = mod.get_global_var('func_7389')
func_7391_call = mutated_mod.get_global_var('func_7391')
call_8013 = func_7389_call()
call_8014 = func_7389_call()
output = relay.Tuple([call_8006,call_8013,])
output2 = relay.Tuple([call_8007,call_8014,])
func_8025 = relay.Function([], output)
mod['func_8025'] = func_8025
mod = relay.transform.InferType()(mod)
mutated_mod['func_8025'] = func_8025
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8025_call = mutated_mod.get_global_var('func_8025')
call_8026 = func_8025_call()
output = call_8026
func_8027 = relay.Function([], output)
mutated_mod['func_8027'] = func_8027
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6597_call = mod.get_global_var('func_6597')
func_6599_call = mutated_mod.get_global_var('func_6599')
call_8037 = func_6597_call()
call_8038 = func_6597_call()
output = call_8037
output2 = call_8038
func_8039 = relay.Function([], output)
mod['func_8039'] = func_8039
mod = relay.transform.InferType()(mod)
mutated_mod['func_8039'] = func_8039
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8039_call = mutated_mod.get_global_var('func_8039')
call_8040 = func_8039_call()
output = call_8040
func_8041 = relay.Function([], output)
mutated_mod['func_8041'] = func_8041
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7342_call = mod.get_global_var('func_7342')
func_7343_call = mutated_mod.get_global_var('func_7343')
call_8052 = relay.TupleGetItem(func_7342_call(), 0)
call_8053 = relay.TupleGetItem(func_7343_call(), 0)
var_8056 = relay.var("var_8056", dtype = "float32", shape = (6, 12, 6))#candidate|8056|(6, 12, 6)|var|float32
bop_8057 = relay.subtract(call_8052.astype('float32'), relay.reshape(var_8056.astype('float32'), relay.shape_of(call_8052))) # shape=(6, 12, 6)
bop_8060 = relay.subtract(call_8053.astype('float32'), relay.reshape(var_8056.astype('float32'), relay.shape_of(call_8053))) # shape=(6, 12, 6)
func_3774_call = mod.get_global_var('func_3774')
func_3777_call = mutated_mod.get_global_var('func_3777')
var_8064 = relay.var("var_8064", dtype = "bool", shape = ())#candidate|8064|()|var|bool
call_8063 = func_3774_call(relay.reshape(var_8064.astype('bool'), []))
call_8065 = func_3774_call(relay.reshape(var_8064.astype('bool'), []))
func_1658_call = mod.get_global_var('func_1658')
func_1661_call = mutated_mod.get_global_var('func_1661')
var_8074 = relay.var("var_8074", dtype = "uint64", shape = (3, 52))#candidate|8074|(3, 52)|var|uint64
var_8075 = relay.var("var_8075", dtype = "uint64", shape = (1716,))#candidate|8075|(1716,)|var|uint64
call_8073 = relay.TupleGetItem(func_1658_call(relay.reshape(var_8074.astype('uint64'), [12, 1, 13]), relay.reshape(var_8075.astype('uint64'), [12, 11, 13]), ), 4)
call_8076 = relay.TupleGetItem(func_1661_call(relay.reshape(var_8074.astype('uint64'), [12, 1, 13]), relay.reshape(var_8075.astype('uint64'), [12, 11, 13]), ), 4)
bop_8080 = relay.floor_mod(call_8052.astype('float64'), relay.reshape(bop_8057.astype('float64'), relay.shape_of(call_8052))) # shape=(6, 12, 6)
bop_8083 = relay.floor_mod(call_8053.astype('float64'), relay.reshape(bop_8060.astype('float64'), relay.shape_of(call_8053))) # shape=(6, 12, 6)
func_7360_call = mod.get_global_var('func_7360')
func_7362_call = mutated_mod.get_global_var('func_7362')
call_8085 = relay.TupleGetItem(func_7360_call(), 0)
call_8086 = relay.TupleGetItem(func_7362_call(), 0)
bop_8090 = relay.power(call_8073.astype('float32'), var_8064.astype('float32')) # shape=(1, 3, 3)
bop_8093 = relay.power(call_8076.astype('float32'), var_8064.astype('float32')) # shape=(1, 3, 3)
var_8102 = relay.var("var_8102", dtype = "uint64", shape = (3, 52))#candidate|8102|(3, 52)|var|uint64
bop_8103 = relay.floor_divide(var_8074.astype('float32'), relay.reshape(var_8102.astype('float32'), relay.shape_of(var_8074))) # shape=(3, 52)
output = relay.Tuple([call_8063,var_8075,bop_8080,call_8085,bop_8090,bop_8103,])
output2 = relay.Tuple([call_8065,var_8075,bop_8083,call_8086,bop_8093,bop_8103,])
func_8110 = relay.Function([var_8056,var_8064,var_8074,var_8075,var_8102,], output)
mod['func_8110'] = func_8110
mod = relay.transform.InferType()(mod)
mutated_mod['func_8110'] = func_8110
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8110_call = mutated_mod.get_global_var('func_8110')
var_8112 = relay.var("var_8112", dtype = "float32", shape = (6, 12, 6))#candidate|8112|(6, 12, 6)|var|float32
var_8113 = relay.var("var_8113", dtype = "bool", shape = ())#candidate|8113|()|var|bool
var_8114 = relay.var("var_8114", dtype = "uint64", shape = (3, 52))#candidate|8114|(3, 52)|var|uint64
var_8115 = relay.var("var_8115", dtype = "uint64", shape = (1716,))#candidate|8115|(1716,)|var|uint64
var_8116 = relay.var("var_8116", dtype = "uint64", shape = (3, 52))#candidate|8116|(3, 52)|var|uint64
call_8111 = func_8110_call(var_8112,var_8113,var_8114,var_8115,var_8116,)
output = call_8111
func_8117 = relay.Function([var_8112,var_8113,var_8114,var_8115,var_8116,], output)
mutated_mod['func_8117'] = func_8117
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4611_call = mod.get_global_var('func_4611')
func_4613_call = mutated_mod.get_global_var('func_4613')
call_8125 = func_4611_call()
call_8126 = func_4611_call()
func_4637_call = mod.get_global_var('func_4637')
func_4638_call = mutated_mod.get_global_var('func_4638')
call_8127 = relay.TupleGetItem(func_4637_call(), 0)
call_8128 = relay.TupleGetItem(func_4638_call(), 0)
func_6119_call = mod.get_global_var('func_6119')
func_6120_call = mutated_mod.get_global_var('func_6120')
call_8130 = relay.TupleGetItem(func_6119_call(), 1)
call_8131 = relay.TupleGetItem(func_6120_call(), 1)
output = relay.Tuple([call_8125,call_8127,call_8130,])
output2 = relay.Tuple([call_8126,call_8128,call_8131,])
func_8133 = relay.Function([], output)
mod['func_8133'] = func_8133
mod = relay.transform.InferType()(mod)
output = func_8133()
func_8134 = relay.Function([], output)
mutated_mod['func_8134'] = func_8134
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5192_call = mod.get_global_var('func_5192')
func_5193_call = mutated_mod.get_global_var('func_5193')
call_8178 = func_5192_call()
call_8179 = func_5192_call()
output = call_8178
output2 = call_8179
func_8182 = relay.Function([], output)
mod['func_8182'] = func_8182
mod = relay.transform.InferType()(mod)
output = func_8182()
func_8183 = relay.Function([], output)
mutated_mod['func_8183'] = func_8183
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4637_call = mod.get_global_var('func_4637')
func_4638_call = mutated_mod.get_global_var('func_4638')
call_8255 = relay.TupleGetItem(func_4637_call(), 0)
call_8256 = relay.TupleGetItem(func_4638_call(), 0)
output = relay.Tuple([call_8255,])
output2 = relay.Tuple([call_8256,])
func_8267 = relay.Function([], output)
mod['func_8267'] = func_8267
mod = relay.transform.InferType()(mod)
mutated_mod['func_8267'] = func_8267
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8267_call = mutated_mod.get_global_var('func_8267')
call_8268 = func_8267_call()
output = call_8268
func_8269 = relay.Function([], output)
mutated_mod['func_8269'] = func_8269
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5192_call = mod.get_global_var('func_5192')
func_5193_call = mutated_mod.get_global_var('func_5193')
call_8342 = func_5192_call()
call_8343 = func_5192_call()
output = call_8342
output2 = call_8343
func_8362 = relay.Function([], output)
mod['func_8362'] = func_8362
mod = relay.transform.InferType()(mod)
mutated_mod['func_8362'] = func_8362
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8362_call = mutated_mod.get_global_var('func_8362')
call_8363 = func_8362_call()
output = call_8363
func_8364 = relay.Function([], output)
mutated_mod['func_8364'] = func_8364
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4510_call = mod.get_global_var('func_4510')
func_4512_call = mutated_mod.get_global_var('func_4512')
call_8370 = relay.TupleGetItem(func_4510_call(), 2)
call_8371 = relay.TupleGetItem(func_4512_call(), 2)
uop_8372 = relay.sigmoid(call_8370.astype('float32')) # shape=(4, 196)
uop_8374 = relay.sigmoid(call_8371.astype('float32')) # shape=(4, 196)
bop_8375 = relay.bitwise_and(uop_8372.astype('uint8'), relay.reshape(call_8370.astype('uint8'), relay.shape_of(uop_8372))) # shape=(4, 196)
bop_8378 = relay.bitwise_and(uop_8374.astype('uint8'), relay.reshape(call_8371.astype('uint8'), relay.shape_of(uop_8374))) # shape=(4, 196)
func_5215_call = mod.get_global_var('func_5215')
func_5217_call = mutated_mod.get_global_var('func_5217')
call_8384 = relay.TupleGetItem(func_5215_call(), 0)
call_8385 = relay.TupleGetItem(func_5217_call(), 0)
output = relay.Tuple([bop_8375,call_8384,])
output2 = relay.Tuple([bop_8378,call_8385,])
func_8396 = relay.Function([], output)
mod['func_8396'] = func_8396
mod = relay.transform.InferType()(mod)
output = func_8396()
func_8397 = relay.Function([], output)
mutated_mod['func_8397'] = func_8397
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7985_call = mod.get_global_var('func_7985')
func_7987_call = mutated_mod.get_global_var('func_7987')
call_8429 = relay.TupleGetItem(func_7985_call(), 0)
call_8430 = relay.TupleGetItem(func_7987_call(), 0)
uop_8435 = relay.acosh(call_8429.astype('float32')) # shape=(7, 16, 7)
uop_8437 = relay.acosh(call_8430.astype('float32')) # shape=(7, 16, 7)
bop_8438 = relay.less(call_8429.astype('bool'), relay.reshape(uop_8435.astype('bool'), relay.shape_of(call_8429))) # shape=(7, 16, 7)
bop_8441 = relay.less(call_8430.astype('bool'), relay.reshape(uop_8437.astype('bool'), relay.shape_of(call_8430))) # shape=(7, 16, 7)
output = relay.Tuple([bop_8438,])
output2 = relay.Tuple([bop_8441,])
func_8442 = relay.Function([], output)
mod['func_8442'] = func_8442
mod = relay.transform.InferType()(mod)
mutated_mod['func_8442'] = func_8442
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8442_call = mutated_mod.get_global_var('func_8442')
call_8443 = func_8442_call()
output = call_8443
func_8444 = relay.Function([], output)
mutated_mod['func_8444'] = func_8444
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6896_call = mod.get_global_var('func_6896')
func_6898_call = mutated_mod.get_global_var('func_6898')
call_8453 = func_6896_call()
call_8454 = func_6896_call()
func_7965_call = mod.get_global_var('func_7965')
func_7966_call = mutated_mod.get_global_var('func_7966')
call_8455 = relay.TupleGetItem(func_7965_call(), 0)
call_8456 = relay.TupleGetItem(func_7966_call(), 0)
output = relay.Tuple([call_8453,call_8455,])
output2 = relay.Tuple([call_8454,call_8456,])
func_8461 = relay.Function([], output)
mod['func_8461'] = func_8461
mod = relay.transform.InferType()(mod)
mutated_mod['func_8461'] = func_8461
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8461_call = mutated_mod.get_global_var('func_8461')
call_8462 = func_8461_call()
output = call_8462
func_8463 = relay.Function([], output)
mutated_mod['func_8463'] = func_8463
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4853_call = mod.get_global_var('func_4853')
func_4855_call = mutated_mod.get_global_var('func_4855')
call_8472 = relay.TupleGetItem(func_4853_call(), 2)
call_8473 = relay.TupleGetItem(func_4855_call(), 2)
output = relay.Tuple([call_8472,])
output2 = relay.Tuple([call_8473,])
func_8474 = relay.Function([], output)
mod['func_8474'] = func_8474
mod = relay.transform.InferType()(mod)
mutated_mod['func_8474'] = func_8474
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8474_call = mutated_mod.get_global_var('func_8474')
call_8475 = func_8474_call()
output = call_8475
func_8476 = relay.Function([], output)
mutated_mod['func_8476'] = func_8476
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7360_call = mod.get_global_var('func_7360')
func_7362_call = mutated_mod.get_global_var('func_7362')
call_8486 = relay.TupleGetItem(func_7360_call(), 0)
call_8487 = relay.TupleGetItem(func_7362_call(), 0)
func_2677_call = mod.get_global_var('func_2677')
func_2682_call = mutated_mod.get_global_var('func_2682')
var_8489 = relay.var("var_8489", dtype = "int8", shape = (1050,))#candidate|8489|(1050,)|var|int8
const_8490 = relay.const([[-10,6,10,-1,10,4,-5,-3,-1,-5,6,-10],[2,9,-5,-4,2,4,-5,2,-7,7,-7,-7],[3,-5,2,3,9,2,3,-10,7,6,9,1],[-2,7,9,10,-4,10,-10,-9,-6,-2,8,-5],[-8,-9,9,-2,-8,-2,1,-8,9,-2,-2,-6],[4,7,-4,7,3,6,7,3,-6,-2,-9,3],[-10,-4,8,9,2,3,8,5,-7,-3,10,10],[3,5,2,-9,-5,-5,7,-4,-9,2,-9,1],[1,-10,2,-8,-2,8,-3,8,-3,10,4,8],[2,-5,8,-7,-1,-1,7,-9,-4,-2,-7,-6],[3,8,-9,5,6,-2,-5,5,-8,-9,8,5],[-9,1,-9,-4,-3,10,-9,-5,4,-3,-8,4],[-5,-4,-3,6,-8,-7,6,-7,-4,-10,3,-1],[-5,-5,3,1,-4,-4,6,10,9,-8,9,-3],[-6,7,10,-6,4,-8,-1,-6,5,-2,10,-4],[-9,3,10,10,-8,-5,9,-3,-5,10,1,-2],[8,7,8,-8,-6,3,-4,1,-4,-2,10,-3],[-4,2,3,-2,-10,2,4,2,-8,5,-2,5],[5,-6,-1,-1,-6,-2,6,3,-7,-3,4,1],[4,5,2,-1,-7,1,8,7,-4,-6,-7,8],[3,-4,-9,-8,-1,-9,4,2,-9,-1,5,-2],[9,1,8,-9,-3,7,-10,-6,-9,-5,-7,6],[10,-2,7,5,-3,-3,8,-1,7,-4,4,-9],[7,7,1,-7,-3,7,4,-10,-2,7,7,2],[3,-4,-8,-1,6,-8,-3,1,3,-8,2,3],[2,-4,5,4,4,6,-10,-8,6,5,-10,-5],[-6,9,2,-2,3,3,3,-7,-5,10,1,-4],[-1,-6,7,5,4,-9,-7,1,8,7,1,-8],[-10,-4,6,8,6,10,7,7,9,-10,-9,-8],[2,8,-3,10,5,-4,1,-10,-8,-2,-6,-8],[5,3,6,-10,-9,4,5,5,9,10,-1,-8],[-3,-4,1,5,-10,1,2,-4,10,-2,1,4],[7,1,6,-9,-2,-7,-4,9,1,-10,1,-3],[-4,-5,-4,-7,5,-1,7,-2,-2,2,-1,10],[2,4,-5,-6,6,4,-2,-3,8,10,1,-6],[10,8,2,-3,1,-10,6,5,-9,4,-9,10]], dtype = "uint8")#candidate|8490|(36, 12)|const|uint8
call_8488 = relay.TupleGetItem(func_2677_call(relay.reshape(var_8489.astype('int8'), [15, 5, 14]), relay.reshape(var_8489.astype('int8'), [15, 5, 14]), relay.reshape(var_8489.astype('int8'), [15, 5, 14]), relay.reshape(const_8490.astype('uint8'), [432,]), ), 3)
call_8491 = relay.TupleGetItem(func_2682_call(relay.reshape(var_8489.astype('int8'), [15, 5, 14]), relay.reshape(var_8489.astype('int8'), [15, 5, 14]), relay.reshape(var_8489.astype('int8'), [15, 5, 14]), relay.reshape(const_8490.astype('uint8'), [432,]), ), 3)
bop_8499 = relay.logical_and(const_8490.astype('bool'), relay.reshape(call_8488.astype('bool'), relay.shape_of(const_8490))) # shape=(36, 12)
bop_8502 = relay.logical_and(const_8490.astype('bool'), relay.reshape(call_8491.astype('bool'), relay.shape_of(const_8490))) # shape=(36, 12)
func_6832_call = mod.get_global_var('func_6832')
func_6833_call = mutated_mod.get_global_var('func_6833')
call_8509 = func_6832_call()
call_8510 = func_6832_call()
output = relay.Tuple([call_8486,var_8489,bop_8499,call_8509,])
output2 = relay.Tuple([call_8487,var_8489,bop_8502,call_8510,])
func_8517 = relay.Function([var_8489,], output)
mod['func_8517'] = func_8517
mod = relay.transform.InferType()(mod)
mutated_mod['func_8517'] = func_8517
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8518 = relay.var("var_8518", dtype = "int8", shape = (1050,))#candidate|8518|(1050,)|var|int8
func_8517_call = mutated_mod.get_global_var('func_8517')
call_8519 = func_8517_call(var_8518)
output = call_8519
func_8520 = relay.Function([var_8518], output)
mutated_mod['func_8520'] = func_8520
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7342_call = mod.get_global_var('func_7342')
func_7343_call = mutated_mod.get_global_var('func_7343')
call_8554 = relay.TupleGetItem(func_7342_call(), 0)
call_8555 = relay.TupleGetItem(func_7343_call(), 0)
func_6780_call = mod.get_global_var('func_6780')
func_6782_call = mutated_mod.get_global_var('func_6782')
const_8557 = relay.const([-6.571918,6.273295,5.474250,-5.114277,7.997943,1.778061,3.518494,3.379416,3.148641,7.235590,-5.028546,-9.897929,-6.384895,-9.084652,-8.143778,-3.778146,-9.173733,2.345715,9.663583,-2.789982,-2.220065,0.639861,-1.670188,-5.786611,-3.442043,8.739141,-7.104609,-8.729961,-0.057954,-8.393203,9.924472,-6.259646,-7.807675,-1.524709,2.511702,-4.314195,-0.191144,5.466804,-9.318702,-9.751697,-1.491336,7.266619,2.713178,5.555191,-0.701368,2.892528,5.599247,6.213981], dtype = "float64")#candidate|8557|(48,)|const|float64
call_8556 = relay.TupleGetItem(func_6780_call(relay.reshape(const_8557.astype('float64'), [48,])), 1)
call_8558 = relay.TupleGetItem(func_6782_call(relay.reshape(const_8557.astype('float64'), [48,])), 1)
func_8025_call = mod.get_global_var('func_8025')
func_8027_call = mutated_mod.get_global_var('func_8027')
call_8563 = relay.TupleGetItem(func_8025_call(), 0)
call_8564 = relay.TupleGetItem(func_8027_call(), 0)
output = relay.Tuple([call_8554,call_8556,const_8557,call_8563,])
output2 = relay.Tuple([call_8555,call_8558,const_8557,call_8564,])
func_8577 = relay.Function([], output)
mod['func_8577'] = func_8577
mod = relay.transform.InferType()(mod)
mutated_mod['func_8577'] = func_8577
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8577_call = mutated_mod.get_global_var('func_8577')
call_8578 = func_8577_call()
output = call_8578
func_8579 = relay.Function([], output)
mutated_mod['func_8579'] = func_8579
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8609 = relay.var("var_8609", dtype = "float32", shape = (10, 15, 9))#candidate|8609|(10, 15, 9)|var|float32
uop_8610 = relay.acosh(var_8609.astype('float32')) # shape=(10, 15, 9)
func_5852_call = mod.get_global_var('func_5852')
func_5853_call = mutated_mod.get_global_var('func_5853')
call_8617 = func_5852_call()
call_8618 = func_5852_call()
func_8182_call = mod.get_global_var('func_8182')
func_8183_call = mutated_mod.get_global_var('func_8183')
call_8627 = func_8182_call()
call_8628 = func_8182_call()
output = relay.Tuple([uop_8610,call_8617,call_8627,])
output2 = relay.Tuple([uop_8610,call_8618,call_8628,])
func_8635 = relay.Function([var_8609,], output)
mod['func_8635'] = func_8635
mod = relay.transform.InferType()(mod)
mutated_mod['func_8635'] = func_8635
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8636 = relay.var("var_8636", dtype = "float32", shape = (10, 15, 9))#candidate|8636|(10, 15, 9)|var|float32
func_8635_call = mutated_mod.get_global_var('func_8635')
call_8637 = func_8635_call(var_8636)
output = call_8637
func_8638 = relay.Function([var_8636], output)
mutated_mod['func_8638'] = func_8638
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8718 = relay.var("var_8718", dtype = "int32", shape = (8, 8, 12))#candidate|8718|(8, 8, 12)|var|int32
var_8719 = relay.var("var_8719", dtype = "int32", shape = (8, 8, 12))#candidate|8719|(8, 8, 12)|var|int32
bop_8720 = relay.less_equal(var_8718.astype('bool'), relay.reshape(var_8719.astype('bool'), relay.shape_of(var_8718))) # shape=(8, 8, 12)
output = bop_8720
output2 = bop_8720
func_8726 = relay.Function([var_8718,var_8719,], output)
mod['func_8726'] = func_8726
mod = relay.transform.InferType()(mod)
var_8727 = relay.var("var_8727", dtype = "int32", shape = (8, 8, 12))#candidate|8727|(8, 8, 12)|var|int32
var_8728 = relay.var("var_8728", dtype = "int32", shape = (8, 8, 12))#candidate|8728|(8, 8, 12)|var|int32
output = func_8726(var_8727,var_8728,)
func_8729 = relay.Function([var_8727,var_8728,], output)
mutated_mod['func_8729'] = func_8729
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7863_call = mod.get_global_var('func_7863')
func_7865_call = mutated_mod.get_global_var('func_7865')
call_8753 = relay.TupleGetItem(func_7863_call(), 0)
call_8754 = relay.TupleGetItem(func_7865_call(), 0)
output = call_8753
output2 = call_8754
func_8755 = relay.Function([], output)
mod['func_8755'] = func_8755
mod = relay.transform.InferType()(mod)
output = func_8755()
func_8756 = relay.Function([], output)
mutated_mod['func_8756'] = func_8756
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4772_call = mod.get_global_var('func_4772')
func_4773_call = mutated_mod.get_global_var('func_4773')
call_8766 = relay.TupleGetItem(func_4772_call(), 3)
call_8767 = relay.TupleGetItem(func_4773_call(), 3)
func_6083_call = mod.get_global_var('func_6083')
func_6085_call = mutated_mod.get_global_var('func_6085')
call_8770 = relay.TupleGetItem(func_6083_call(), 0)
call_8771 = relay.TupleGetItem(func_6085_call(), 0)
func_2836_call = mod.get_global_var('func_2836')
func_2839_call = mutated_mod.get_global_var('func_2839')
const_8793 = relay.const([-3,-7,-7,-7,-3,-7,2,-7,8,-2,5,10,-1,7,1,9,3,10,-10,4,-10,4,-7,-2,10,-7,10,-1,10,-9,5,4,6,7,1,-9,-4,-2,3,4,-7,-10,-2,8,-8,2,4,1,-10,-6,-2,3,-8,-5,-8,-6,-3,10,7,5,4,9,5,-10,8,7,10,6,-4,3,-9,5,-5,-7,-2,10,-2,-7,-10,-6,-2,-10,5,-2,-6,-1,4,-9,10,3,-8,1,3,9,-5,-4,9,9,10,1,8,3,7,-1,5,10,-9,5,8,-9,-10,10,-9,-1,10,-6,-3,10,-10,6,7,1,6,-9,-10,7,-1,7,-6,10,-10,6,-5,5,9,1,7,3,-7,-10,-3,9,6,6,6,-9,10,2,-4,-1,8,3,3,3,-10,-9,3,-1,-3,10,2,-8,7,-10,-6,-5,2,-2,-4,4,-9,1,2,1,-8,7,-2,-4,4,1,-2,6,6,8,-4,-8,-7,5,10,7,8,-9,6,1,-7,9,1,-3,3,9,-6,-2,-5,-2,-2,-4,-10,3,8,5,-6,-5,10,-6,-9,-2,-1,8,3,2,1,-8,-10,-9,2,-2,-10,9,-4,5,-9,10,5,-7,-2,-4,6,-5,2,5], dtype = "uint32")#candidate|8793|(240,)|const|uint32
call_8792 = func_2836_call(relay.reshape(const_8793.astype('uint32'), [5, 3, 16]), relay.reshape(const_8793.astype('uint32'), [5, 3, 16]), )
call_8794 = func_2836_call(relay.reshape(const_8793.astype('uint32'), [5, 3, 16]), relay.reshape(const_8793.astype('uint32'), [5, 3, 16]), )
output = relay.Tuple([call_8766,call_8770,call_8792,const_8793,])
output2 = relay.Tuple([call_8767,call_8771,call_8794,const_8793,])
func_8798 = relay.Function([], output)
mod['func_8798'] = func_8798
mod = relay.transform.InferType()(mod)
output = func_8798()
func_8799 = relay.Function([], output)
mutated_mod['func_8799'] = func_8799
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7863_call = mod.get_global_var('func_7863')
func_7865_call = mutated_mod.get_global_var('func_7865')
call_8856 = relay.TupleGetItem(func_7863_call(), 5)
call_8857 = relay.TupleGetItem(func_7865_call(), 5)
output = relay.Tuple([call_8856,])
output2 = relay.Tuple([call_8857,])
func_8886 = relay.Function([], output)
mod['func_8886'] = func_8886
mod = relay.transform.InferType()(mod)
mutated_mod['func_8886'] = func_8886
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8886_call = mutated_mod.get_global_var('func_8886')
call_8887 = func_8886_call()
output = call_8887
func_8888 = relay.Function([], output)
mutated_mod['func_8888'] = func_8888
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8886_call = mod.get_global_var('func_8886')
func_8888_call = mutated_mod.get_global_var('func_8888')
call_8907 = relay.TupleGetItem(func_8886_call(), 0)
call_8908 = relay.TupleGetItem(func_8888_call(), 0)
func_1531_call = mod.get_global_var('func_1531')
func_1534_call = mutated_mod.get_global_var('func_1534')
var_8919 = relay.var("var_8919", dtype = "float32", shape = (9, 1))#candidate|8919|(9, 1)|var|float32
var_8920 = relay.var("var_8920", dtype = "uint8", shape = (432,))#candidate|8920|(432,)|var|uint8
call_8918 = relay.TupleGetItem(func_1531_call(relay.reshape(var_8919.astype('float32'), [1, 3, 3]), relay.reshape(var_8920.astype('uint8'), [216, 2]), ), 2)
call_8921 = relay.TupleGetItem(func_1534_call(relay.reshape(var_8919.astype('float32'), [1, 3, 3]), relay.reshape(var_8920.astype('uint8'), [216, 2]), ), 2)
func_7812_call = mod.get_global_var('func_7812')
func_7813_call = mutated_mod.get_global_var('func_7813')
call_8922 = relay.TupleGetItem(func_7812_call(), 0)
call_8923 = relay.TupleGetItem(func_7813_call(), 0)
uop_8928 = relay.sinh(call_8922.astype('float32')) # shape=(8, 7, 11)
uop_8930 = relay.sinh(call_8923.astype('float32')) # shape=(8, 7, 11)
output = relay.Tuple([call_8907,call_8918,var_8919,var_8920,uop_8928,])
output2 = relay.Tuple([call_8908,call_8921,var_8919,var_8920,uop_8930,])
func_8936 = relay.Function([var_8919,var_8920,], output)
mod['func_8936'] = func_8936
mod = relay.transform.InferType()(mod)
mutated_mod['func_8936'] = func_8936
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8936_call = mutated_mod.get_global_var('func_8936')
var_8938 = relay.var("var_8938", dtype = "float32", shape = (9, 1))#candidate|8938|(9, 1)|var|float32
var_8939 = relay.var("var_8939", dtype = "uint8", shape = (432,))#candidate|8939|(432,)|var|uint8
call_8937 = func_8936_call(var_8938,var_8939,)
output = call_8937
func_8940 = relay.Function([var_8938,var_8939,], output)
mutated_mod['func_8940'] = func_8940
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6991_call = mod.get_global_var('func_6991')
func_6993_call = mutated_mod.get_global_var('func_6993')
call_8959 = func_6991_call()
call_8960 = func_6991_call()
func_6273_call = mod.get_global_var('func_6273')
func_6275_call = mutated_mod.get_global_var('func_6275')
call_8962 = relay.TupleGetItem(func_6273_call(), 0)
call_8963 = relay.TupleGetItem(func_6275_call(), 0)
output = relay.Tuple([call_8959,call_8962,])
output2 = relay.Tuple([call_8960,call_8963,])
func_8985 = relay.Function([], output)
mod['func_8985'] = func_8985
mod = relay.transform.InferType()(mod)
output = func_8985()
func_8986 = relay.Function([], output)
mutated_mod['func_8986'] = func_8986
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5192_call = mod.get_global_var('func_5192')
func_5193_call = mutated_mod.get_global_var('func_5193')
call_9025 = func_5192_call()
call_9026 = func_5192_call()
output = relay.Tuple([call_9025,])
output2 = relay.Tuple([call_9026,])
func_9029 = relay.Function([], output)
mod['func_9029'] = func_9029
mod = relay.transform.InferType()(mod)
mutated_mod['func_9029'] = func_9029
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9029_call = mutated_mod.get_global_var('func_9029')
call_9030 = func_9029_call()
output = call_9030
func_9031 = relay.Function([], output)
mutated_mod['func_9031'] = func_9031
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8025_call = mod.get_global_var('func_8025')
func_8027_call = mutated_mod.get_global_var('func_8027')
call_9041 = relay.TupleGetItem(func_8025_call(), 0)
call_9042 = relay.TupleGetItem(func_8027_call(), 0)
output = relay.Tuple([call_9041,])
output2 = relay.Tuple([call_9042,])
func_9043 = relay.Function([], output)
mod['func_9043'] = func_9043
mod = relay.transform.InferType()(mod)
mutated_mod['func_9043'] = func_9043
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9043_call = mutated_mod.get_global_var('func_9043')
call_9044 = func_9043_call()
output = call_9044
func_9045 = relay.Function([], output)
mutated_mod['func_9045'] = func_9045
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7812_call = mod.get_global_var('func_7812')
func_7813_call = mutated_mod.get_global_var('func_7813')
call_9092 = relay.TupleGetItem(func_7812_call(), 1)
call_9093 = relay.TupleGetItem(func_7813_call(), 1)
output = relay.Tuple([call_9092,])
output2 = relay.Tuple([call_9093,])
func_9104 = relay.Function([], output)
mod['func_9104'] = func_9104
mod = relay.transform.InferType()(mod)
output = func_9104()
func_9105 = relay.Function([], output)
mutated_mod['func_9105'] = func_9105
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5336_call = mod.get_global_var('func_5336')
func_5337_call = mutated_mod.get_global_var('func_5337')
call_9195 = relay.TupleGetItem(func_5336_call(), 0)
call_9196 = relay.TupleGetItem(func_5337_call(), 0)
output = relay.Tuple([call_9195,])
output2 = relay.Tuple([call_9196,])
func_9216 = relay.Function([], output)
mod['func_9216'] = func_9216
mod = relay.transform.InferType()(mod)
mutated_mod['func_9216'] = func_9216
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9216_call = mutated_mod.get_global_var('func_9216')
call_9217 = func_9216_call()
output = call_9217
func_9218 = relay.Function([], output)
mutated_mod['func_9218'] = func_9218
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9104_call = mod.get_global_var('func_9104')
func_9105_call = mutated_mod.get_global_var('func_9105')
call_9235 = relay.TupleGetItem(func_9104_call(), 0)
call_9236 = relay.TupleGetItem(func_9105_call(), 0)
func_5096_call = mod.get_global_var('func_5096')
func_5099_call = mutated_mod.get_global_var('func_5099')
const_9243 = relay.const([10,10,-2,5,4,2,5,6,-4,-6,-3,7,4,8,-9,-7,-2,-6,-9,2,6,-5,-1,-4,-7,4,-7,-7,-10,10,4,8,-4,2,7,7,1,-4,-4,-7,-1,8,-3,1,-9,-5,-8,-3,-7,-6,-1,8,4,2,2,-6,4,1,10,-1,4,-4,-8,5,-1,2,3,-4,3,2,9,8,-3,-1,2,-3,-9,-9,3,-4,6,-8,5,-5,-2,-4,6,-6,-3,-3,10,-9,3,8,3,-2,-8,-7,6,9,-10,9,-5,6,-4,2,5,5,-1,-3,2,3,-8,3,4,-10,-7,2,-5,-9,-7,3,2,9,-10,8,-8,2,-5,9,-8,-6,9,-6,-6,5,6,5,-5,-3,-9,-7,-4,-4,-5,-8,2,-6,10,7,-7,-9,-10,2,1,10,-8,8,5,1,-4,3,-1,-1,2,-8,10,-3,2,-6,5,-6,3,3,7,-8,-2,-1,1,-5,7,4,-1,-8,6,-9,-9,2,-8,-10,10,7,10,-7,7,-5,-5,2,8,10,-3,5,-3,-4,3,-5,-1,-6,-8,3,7,10,1,-10,3,4,-9,9,-5,1,6,-4,-8,-9,5,4,4,-6,7,3,-3,5,4,-4,-9,-1,-2,-2,-9,-9,-5,-8,4,-1,7,-10,-10,4,10,-5,2,-2,4,5,8,-8,4,1,8,-10,7,5,6,1,7,5,-5,4,-2,3,-2,3,4,5,-10,-7,6,4,3,-7,5,-8,8,2,-10,2,-3,-7,10,1,8,7,-1,-5,10,5,-4,8,4,6,2,-3,2,5,1,-4,-5,-2,-3,1,8,9,-8,8,4,5,9,-4,-7,4,5,6,10,6,-2,9,4,4,4,3,5,5,-7,6,7,1,-10,10,2,5,5,-8,1,-3,5,4,-6,-1,-9,-5,8,8,5,-8,-8,-3,-7,1,4,-5,-2,6,-8,-8,-5,-5,1,9,-3,-2,-1,3,-7,-6,-10,9,-9,-7,3,6,-2,-1,6,10,-10,-2,9,-9,-2,1,-7,4,-7,-5,-8,-10,-3,5,4,1,-8,-5,8,7,-8,-4,9,2,-8,-8,-7,-9,1,2,-9,-9,5,8,-5,-5,-3,9,4,-10,8,3,6,6,7,-1,8,-7,-4,-8,10,-4,-2,-7,-6,-3,4,-10,9,6,-1,-4,8,5,6,1,-9,-1,1,9,6,2,7,10,7,2,6,-10,-9,6,-8,-3,3,-8,-3,-2,1,1,-7,4,9,-3,-3,-9,7,8,-4,4,7,4,1,9,1,9,-2,-3,8,4,-8,-4,8,-4,-4,-10,2,-1,1,4,1,-9,6,-2,7,-6,10,-3,3,-1,-6,8,-6,-1,-10,-8,-6,-3,-10,-7,-4,-5,4,-3,5,-5,-8,9,3,-2,2,-5,-8,3,5,8,-4,4,-10,6,-10,6,-6,-1,-4,-4,-4,7,9,-1,-9,-4,9,-10,4,6,-6,1,9,3,-6,2,-7,-1,8,-3,-10,-1,-6,9,6,3,10,-6,-9,-4,9,4,-4,4,-8,10,-5,-8,-1,-8,-4,3,-6,-3,-9,1,-3,-5,3,-7,-6,8,8,-10,-5,-10,-1,1,3,4,10,-9,2,10,-3,6,-3,-1,-10,-4,1,-4,-6,-10,8,10,-1,3,-4,1,-9,9,1,7,-10,8,4,4,4,8,1,-4,-10,8,-1,3,5,-3,1,8,10,3,-8,5,-4,-6,2,7,-8,-6,-3,-10,-1,7,-5,-3,10,1,4,10,1,-3,7,-7,-5,7,-3,8,-9,6,-9,1,5,-9,-1,9,8,-7,1,1,8,-6,4,7,-1,9,9,1,-5,-7,3,8,-7,6,10,4,7,1,5,7,10,-6,-10,-7,7,-1,9,2,6,-5,-7,-4,-8,6,-6,9,-10,7,10,-3,5,9,-5,1,1,6,7,-2,9,-8,2,-1,10,10,-9,1,9,9,1,5,-7,9,3,9,-1,8,-6,-4,4,-10,-9,8,-1,3,-10,3,1,3,5,-7,3,-8,4,-7,7,5,6,-5,-2,-8,-9,4,-5,4,-1,6,8,-4,7,-3,9,-2,1,4,8,-10,5,6,10,-1,3,-6,-1,-3,2,-3,-4,-7,-2,10,5,8,-1,1,6,-4,-9,-10,-1,-9,1,-3,6,-1,3,10,-9,-7,3,-6,1,-10,8,-3,4,-1,3,-1,-6,-5,4,-8,-4,-5,-4,-7,-1,-7,8,-10,-9,9,-7,-9,5,-3,-1,-1,-5,-3,-7,3,-7,9,-10,10,-9,1,1,10,-8,-2,3,4,-2,-6,7,-9,2,2,4,-1,-2,9,-4,1,2,-9,-9,-3,-1,-9,10,3,-5,-4,-8,4,-7,7,-1,-3,4,-10,-8,3,3,6,-2,-5,-7,-6,6,-6,4,-6,4,10,3,10,-2,-9,-6,8,5,7,-4,8,4,5,-9,-2,2,8,1,-7,2,-8,4,-8,-1,2,7,-7,3,-6,-5,-5,10,2,-3,4,6,4,10,-10,7,8,1,-3,-7,7,9,9,-5,-1,-10,4,9,-8,1,9,10,-10,-3,7,5,-4,-6,-6,-1,-9,-3,7,-2,10,2,1,-7,7,7,-9,-8,9,-3,-4,1,5,8,-8,6,-6,-7,4,-2,-3,-3,-1,5,-4,4,-3,3,1,-10,4,8,6,-10,1,-1,9,7,4,10,2,-6,-3,5,-10,4,2,-7,9,-1,7,5,6,6,5,10,3,4,-6,-9,-3,2,5,6,-5,4,-6], dtype = "int8")#candidate|9243|(1050,)|const|int8
var_9244 = relay.var("var_9244", dtype = "uint8", shape = (432,))#candidate|9244|(432,)|var|uint8
call_9242 = relay.TupleGetItem(func_5096_call(relay.reshape(const_9243.astype('int8'), [70, 15]), relay.reshape(var_9244.astype('uint8'), [432,]), ), 0)
call_9245 = relay.TupleGetItem(func_5099_call(relay.reshape(const_9243.astype('int8'), [70, 15]), relay.reshape(var_9244.astype('uint8'), [432,]), ), 0)
output = relay.Tuple([call_9235,call_9242,const_9243,var_9244,])
output2 = relay.Tuple([call_9236,call_9245,const_9243,var_9244,])
func_9255 = relay.Function([var_9244,], output)
mod['func_9255'] = func_9255
mod = relay.transform.InferType()(mod)
mutated_mod['func_9255'] = func_9255
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9256 = relay.var("var_9256", dtype = "uint8", shape = (432,))#candidate|9256|(432,)|var|uint8
func_9255_call = mutated_mod.get_global_var('func_9255')
call_9257 = func_9255_call(var_9256)
output = call_9257
func_9258 = relay.Function([var_9256], output)
mutated_mod['func_9258'] = func_9258
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5192_call = mod.get_global_var('func_5192')
func_5193_call = mutated_mod.get_global_var('func_5193')
call_9370 = func_5192_call()
call_9371 = func_5192_call()
output = relay.Tuple([call_9370,])
output2 = relay.Tuple([call_9371,])
func_9381 = relay.Function([], output)
mod['func_9381'] = func_9381
mod = relay.transform.InferType()(mod)
output = func_9381()
func_9382 = relay.Function([], output)
mutated_mod['func_9382'] = func_9382
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9478 = relay.var("var_9478", dtype = "float64", shape = (16, 9, 16))#candidate|9478|(16, 9, 16)|var|float64
const_9479 = relay.const([[[-4.344930,3.650097,-3.846759,3.683698,-2.161888,-7.075693,-9.734231,-2.375129,-5.606956,-4.151633,-6.087067,-8.749123,2.329872,5.834628,-4.348827,-7.254966],[7.705822,-3.244272,-0.176670,1.137642,9.792623,-2.041796,9.521192,3.271525,-3.158269,1.090134,-0.155428,-8.892902,-0.604870,-8.786237,-8.861304,1.026465],[5.297653,7.920281,0.597794,-4.294783,4.236865,2.966780,1.134572,-3.887390,-6.829408,-0.526157,-3.728804,-5.671251,-2.017154,2.548841,7.687515,9.550514],[-3.569949,-5.036015,2.124474,0.777496,-0.433607,-9.961283,6.274773,8.110742,-1.308023,2.038438,3.086477,2.982184,-9.309980,-7.123399,-2.283880,-0.098934],[5.698583,-1.751799,7.041419,6.343470,-3.846496,-2.343021,-4.202982,4.847857,2.479549,6.115240,6.836691,5.222342,-2.640279,4.873863,2.781736,9.559658],[7.746593,2.337498,5.206981,-1.877173,-4.367699,-8.950655,-2.561579,8.932362,-8.693234,-8.156597,-9.494920,5.022355,-3.790165,6.896743,7.121524,-4.565647],[-6.819544,3.522637,-3.996439,-6.943547,-1.902517,9.938952,-5.655477,0.467524,-6.944200,-8.477991,9.128714,3.759592,0.403643,4.367591,8.800550,4.955727],[8.931330,-7.278392,-2.937430,8.805427,5.995236,6.542996,1.973384,-1.713957,0.325515,-2.026404,-5.724540,-9.088613,-6.521407,-8.023294,1.264123,-4.267844],[4.496426,-8.768896,2.469214,-1.993928,-5.217792,-2.990071,-1.636809,6.708255,-1.102244,-0.129486,4.502775,-8.253076,-7.406852,-3.843756,-4.180262,4.247240]],[[3.076723,3.202250,5.605596,9.224406,2.962149,0.552065,-7.208044,0.836549,2.701122,7.538018,-8.181874,-6.064935,0.098539,-0.701840,3.545062,1.258533],[6.669142,0.386249,-1.047554,1.362985,4.883345,-4.481581,6.008631,-1.892796,8.926199,-7.374196,0.495879,7.904994,6.136867,-7.747947,2.842325,4.908663],[-0.752736,6.637718,7.612628,-0.460814,4.757578,-7.750015,5.497213,2.928139,-6.646752,-3.901923,7.031295,-7.537896,-6.583703,2.292156,-2.471881,-7.150763],[-6.069148,-7.335530,-5.666475,-3.614692,4.278058,8.034800,1.756675,7.193538,-8.851446,1.129459,7.228471,-0.892014,-2.473545,3.304993,-7.666352,8.056397],[0.988238,-6.568192,-1.561968,-0.414155,6.019564,-3.299997,-0.230432,-4.891204,-9.695723,-9.414572,-3.554545,8.644161,5.710531,1.896133,-3.924544,-2.996738],[-8.927595,-9.961355,3.169804,-0.227234,-4.219587,0.914351,9.366332,3.499570,6.791822,1.670081,-7.670899,-7.787265,-7.999062,8.740313,-8.214320,-9.202710],[-2.875255,7.256555,2.181080,-2.948422,0.685203,2.122666,4.864080,-5.170087,-0.259928,-8.955847,-8.277178,-7.778301,2.239382,5.715549,7.767720,-5.272469],[-7.482787,8.406199,-8.599349,2.210394,8.424631,-5.421961,7.118056,3.773803,-3.595415,-8.986681,-2.458930,6.839887,-3.745094,9.799127,6.357656,9.506971],[-4.907407,2.814392,-8.709226,-3.079240,0.554873,6.359467,7.626695,5.812505,-1.412350,-5.482716,-3.286888,-2.598521,-5.017087,8.501867,-1.477099,-8.770559]],[[9.392822,1.870315,-6.717245,-8.234364,-3.558185,3.470759,-2.804128,0.625380,-8.131283,-5.684074,-2.714306,-9.735218,-3.349711,-6.297907,-7.489031,2.142510],[-1.943869,-7.266692,-6.420336,0.610301,-2.880997,-8.976337,1.939373,2.322136,4.385210,-5.682499,1.844952,1.632803,-2.670119,-7.089853,-5.880505,7.675321],[-7.846128,0.374729,-6.022460,3.279987,2.146507,1.179781,2.217384,1.836137,-8.011354,-1.832831,-4.566475,-3.791348,4.266525,8.487790,-5.906090,3.518309],[-7.848329,-9.968435,6.324017,9.755739,8.955600,2.671859,-4.138227,-5.472211,-6.947802,-0.171351,-5.925415,-6.185460,3.228238,0.434051,-3.480996,-3.103730],[6.007790,6.859073,-6.932109,-4.842707,4.539810,-4.812242,-8.694259,0.643239,-8.083576,6.924637,-6.167951,-5.511407,9.271015,6.450357,-3.040981,5.185802],[-2.733475,-9.477224,1.813838,4.639074,-4.516944,-3.529429,-0.583656,-6.735424,1.183355,6.420750,0.908371,2.077287,8.508569,-9.167011,-8.450782,6.362822],[-6.572621,2.716976,-4.378396,-6.515574,9.256290,5.333830,-1.774547,-0.663077,8.985665,2.492147,6.261398,-9.170367,-4.588940,0.823925,-7.416374,5.576092],[-8.210551,-4.907544,1.264317,-9.574437,-8.230549,-0.855551,8.334649,-7.155783,-4.765746,3.353049,4.825608,-4.971509,-0.593641,-8.179382,0.310566,8.221569],[7.527773,-2.052650,-7.296771,6.605757,0.471245,-4.200609,-3.077261,0.961714,-8.944401,-6.557411,-0.435661,7.431728,-3.314606,3.547057,-9.349134,-7.186653]],[[3.570237,-9.806602,6.583263,-6.320291,-3.194268,1.686677,6.452206,8.223396,6.665448,2.828544,4.366249,-4.774069,0.330396,8.069096,-1.448896,9.440826],[-1.630045,8.076844,9.886570,-5.259095,-0.776644,-9.349206,6.472336,-9.601060,0.433135,-5.007194,-7.958006,5.105452,3.380680,6.026512,-9.560025,2.403195],[5.566135,-3.264032,-3.034847,-1.396320,-4.966650,-9.691927,-6.292225,-8.585521,1.005619,-7.162797,4.522170,0.030132,-2.892236,-0.914852,3.985244,-5.354091],[-2.399829,5.062271,2.800271,-1.659328,-6.565390,6.164441,4.452915,-9.792195,0.961433,-0.762360,-6.928087,2.121789,1.347817,3.473951,2.319177,5.486979],[-8.778208,-2.685693,-3.215553,0.108348,1.891860,3.882737,-6.689038,8.873104,1.933553,-2.030945,0.030711,-9.618965,8.276229,3.976846,3.936673,2.782245],[4.995611,-2.458054,-7.654073,-1.713888,-9.621002,-8.265945,-7.465003,-7.318366,6.690254,3.177067,-2.991090,4.922761,-1.927496,-6.866581,3.068439,2.810517],[8.012695,-4.495964,-9.345378,-4.252802,0.993836,2.357551,-2.227669,4.709159,7.092494,9.492587,-2.326090,9.581720,5.086434,1.404776,1.620469,-1.716915],[-9.439070,-9.796808,8.793715,8.573108,6.034463,-1.139224,3.751145,-7.016536,1.264572,-6.844962,-1.543613,-9.278710,-8.694129,4.546594,-0.335165,-7.363517],[-4.937595,7.178539,0.532211,-2.923704,-3.456692,0.280919,-5.071375,-5.730875,7.939203,-0.459294,-1.679179,9.338165,-0.202331,1.063189,-7.161723,6.806350]],[[-1.578448,7.009242,4.056318,7.560986,-1.578420,5.867356,-4.282180,-0.246783,4.847157,8.403058,0.365128,-2.768756,6.216254,2.147253,3.296363,6.053865],[8.738334,-6.290931,-6.171590,-6.007700,-4.157599,-5.340045,0.424929,-4.022181,5.962567,0.891115,-0.755168,-0.384886,9.903553,-0.492197,-9.460144,-2.655818],[-3.660520,-6.444544,-0.267687,5.393037,8.779808,3.503006,3.181498,4.661883,-0.115787,6.893002,-2.772005,-8.049801,5.503406,-6.334080,-4.064736,-2.357908],[7.968640,-8.859008,4.583203,-6.789662,7.438009,-2.925015,4.739796,6.014670,-0.816738,8.604982,-6.257613,-3.736843,-7.297672,5.052369,0.271768,0.793762],[-4.410781,6.186907,3.739981,-5.701111,2.561851,3.825616,-8.903489,-5.996267,-2.444471,2.174872,-7.377566,-8.171618,1.982087,6.093475,6.597611,3.911500],[-8.619990,-2.202101,6.783162,-2.389118,3.637267,3.775657,-7.844736,-1.010962,1.124745,8.545007,9.148931,-1.019353,7.684484,9.970011,-3.105418,3.296054],[5.458819,7.168166,-6.834038,-0.513157,7.110276,-9.659176,4.366188,-0.468843,-9.020229,-7.078606,-1.670092,-1.256316,9.254507,-9.643561,3.749416,-1.375376],[8.244375,2.005655,-5.804576,9.181333,3.533703,4.549422,-4.860838,-9.135199,-6.781213,-1.214243,6.301666,-9.362916,6.722037,2.422717,-9.203129,5.041337],[9.808811,-4.629245,-5.660435,8.382009,8.554207,1.716560,7.203248,-2.400425,-0.582475,-6.691309,-3.972354,-5.997035,4.863757,-5.027431,-6.640923,-3.075469]],[[-9.554568,3.675216,-8.792569,-6.933527,2.550106,-2.580538,8.003995,-0.146150,8.020306,-9.790070,-0.197916,4.556949,-9.584412,4.963773,-4.633346,-0.977059],[-0.543584,5.254623,-3.696726,-4.245395,0.566476,-2.955582,-1.590352,6.352566,3.796093,2.402300,-7.434151,-2.124571,-5.953222,4.608602,2.233113,4.465710],[9.032146,-9.543195,-9.775639,-2.829206,8.891001,1.602824,6.504049,-8.690180,-7.867217,-0.296831,-6.943051,8.675253,8.908311,0.275978,-9.995014,-5.539170],[-8.647210,2.919055,-7.602276,-2.052431,7.122230,2.362481,-9.848963,0.132394,8.198277,-3.923777,-8.388961,-5.225670,-4.365900,-6.087486,-4.906287,4.055140],[-8.479057,6.405333,-5.410612,-2.272420,6.583102,-4.195313,5.357315,-1.494243,-6.399672,8.986861,-8.030979,-2.543929,4.964858,1.693067,0.163992,-4.809603],[-7.873605,-3.125112,-8.249108,-0.771274,-4.510942,9.870043,-8.344550,-7.358766,-8.087578,-6.666195,4.537671,-9.038994,6.673736,-2.766776,-5.283717,-5.115558],[6.931375,3.238682,-1.787806,1.566683,-7.868051,-7.727353,5.828021,6.835702,-3.850282,-9.366693,-0.666068,7.545562,5.681249,9.255532,-5.083925,-9.641784],[-2.347823,7.509314,4.973348,-6.885867,-0.488428,-2.961312,0.668243,2.140642,5.781076,-6.683616,-0.667870,-2.748585,5.633196,6.130564,4.292877,8.485486],[8.988586,-4.211934,-1.585400,6.777661,-7.057097,-5.273402,2.021717,4.851401,0.009118,0.353507,5.097654,0.006988,9.670124,0.315035,-2.391410,-7.009137]],[[8.329640,-4.455464,3.919523,-2.981884,-0.683337,-9.259055,8.423539,-5.791795,3.885017,-6.919622,0.592125,2.789383,3.204100,-4.974816,-2.895075,8.349969],[8.873222,7.605827,1.715171,-7.963510,-5.374438,-3.015223,1.937162,-6.607638,-4.305502,7.273834,4.023189,-5.121619,4.197547,-6.027878,4.082231,-6.342115],[-6.764067,-5.672376,7.916052,5.950980,2.161625,9.501514,-3.725552,0.375258,9.384919,3.679094,3.996213,0.295835,-1.261239,-8.496651,5.656861,-3.455922],[-5.302493,-2.250499,-4.038470,6.433655,8.756540,-0.822028,9.745937,-0.069720,-6.224832,2.808614,2.116058,2.750884,-1.043926,8.096458,-6.846490,9.045009],[-3.166821,-0.827696,1.501525,-1.243656,4.170202,3.546384,-7.444840,7.153498,9.427673,4.090444,9.993138,-2.153088,-9.827344,0.355721,3.217488,-1.935620],[-3.002714,-1.718740,-9.046696,-5.480113,5.111153,-1.037033,3.140952,9.735049,-8.054597,7.107320,9.927795,-5.384757,-2.029692,-2.887791,-0.259961,6.232729],[1.752915,0.131029,5.115467,4.684746,3.496217,-0.896014,2.155053,5.779783,-5.097704,4.564353,-7.242816,-2.628503,-9.695081,-4.568398,3.513740,7.733457],[-6.631393,-5.499908,0.482949,-2.777013,-8.990532,9.068402,-8.315586,9.155558,-6.288709,-4.511964,-6.589614,7.789602,6.658182,-1.707040,3.310548,-7.077271],[-2.028210,4.847487,-7.970373,-9.468010,4.640004,7.333361,-4.854285,-8.068748,3.279760,9.390988,9.097449,-4.117518,-3.219533,2.839086,8.880869,0.522798]],[[4.067803,9.750543,5.875784,-7.202595,7.236032,-8.993964,-7.943413,-3.733308,-2.933380,-2.807751,-5.634590,-6.493620,6.866739,4.190678,5.470146,-5.954498],[0.251786,3.422693,0.249015,5.200107,4.215051,-9.003734,4.292671,5.645662,-0.167587,7.097627,6.329490,2.813587,-4.369712,1.107213,-3.506519,-1.097642],[9.069422,-0.587731,1.894710,9.529642,2.002224,-6.383465,0.987551,-5.995785,5.126644,-6.653712,-5.486345,7.028453,-1.435103,-9.807219,-8.346240,8.862008],[-7.953268,-9.658749,8.485615,-7.760322,0.166669,6.703341,4.333656,-3.092114,-5.030967,4.413632,6.161241,7.037606,4.715947,-3.153360,-9.889779,3.766471],[3.015346,-6.300000,3.598723,9.678517,0.955814,4.494586,4.605400,-8.639839,0.692638,-7.043359,-5.177528,-2.929539,7.272656,-8.933860,-5.422160,1.979040],[7.718444,2.760164,-1.497018,-8.312171,5.588616,-1.679885,4.872001,-1.883847,-2.795190,2.086007,-3.475351,-4.173019,-7.653975,6.687737,-4.105279,-5.158939],[-6.567261,1.292590,1.223722,8.158249,8.810619,5.303615,-8.069442,5.955331,-1.166679,9.528648,6.227596,-2.465802,-5.836089,-2.382544,-3.424340,5.618811],[-0.224686,-5.500054,-4.735037,9.155244,8.822963,-2.959601,-9.255635,0.117180,5.770657,-3.000763,-6.561768,-4.447331,-0.603462,-8.899006,-2.152897,-9.405549],[-7.638556,-1.877714,-8.508304,-2.196729,-5.840594,0.857689,7.685489,3.630859,3.252167,7.337749,-8.970526,8.300935,-9.931864,-9.758061,9.637812,-8.468621]],[[6.481748,-5.163229,-1.967260,8.902703,2.741215,9.906611,5.854496,4.654879,-8.932636,4.586236,9.102090,-7.554241,-7.170660,-7.978054,7.287158,0.158412],[8.801473,-2.160573,-2.227627,-8.841906,-4.626314,-9.779657,-2.103197,-3.141520,-0.694462,4.456892,-1.881822,-2.400173,-6.235350,-3.749780,2.550707,-5.188273],[2.350727,-0.940679,9.866348,-3.607635,-4.191719,6.487543,-7.828491,-9.318298,9.323319,-3.259934,2.270348,-5.667265,4.153063,0.103654,-0.616508,6.398632],[-9.397499,-3.234478,-7.661548,9.738350,9.671177,3.551711,-0.199608,1.610193,-9.089746,-8.102123,-5.664064,7.104206,4.017091,-5.120611,8.531879,-7.686409],[2.676682,3.380796,3.116083,-1.106641,5.007775,-4.895714,5.863795,-7.537925,-2.452311,8.798056,0.632101,-7.273890,3.413250,4.700042,7.959838,-0.064333],[-9.312386,-1.093064,-6.123465,-5.485838,9.699335,-2.900822,-9.088976,-9.184489,5.845027,3.519744,-3.651372,6.535733,-4.461564,-4.012687,-6.619227,-5.746251],[-6.153025,-6.330416,-7.413288,8.437344,-9.982993,-9.450082,-9.920362,2.403215,6.348150,-9.013881,-6.056456,1.233229,-1.177009,-3.249528,2.124471,4.333836],[-3.243082,-1.004470,1.233654,-2.111152,7.732854,-2.684709,5.936261,6.785969,1.658312,-5.724599,-9.956377,-2.908324,-5.274873,4.329599,-0.440799,5.518006],[7.017454,4.044243,8.914007,-5.621846,-4.327982,-2.795831,-8.626870,-4.988392,-6.471054,9.646231,7.479722,7.118181,9.347361,0.856813,-6.579945,-0.102681]],[[-6.477172,-7.190756,2.786619,4.401155,5.321143,0.532172,5.862397,9.162598,-5.509228,-4.424245,3.629924,1.419003,8.535821,-5.538055,-8.171531,6.670897],[-7.527266,-4.576223,-4.989042,3.194533,-6.366032,7.686428,7.211660,7.208881,4.889223,9.168640,4.930899,7.947667,1.005816,-3.720408,-1.490992,-2.187934],[0.850030,-4.814298,-9.672277,-5.927998,-3.931120,0.956237,-6.849314,-4.094900,-7.921543,-9.295007,-2.429572,-4.973219,2.442427,7.772644,-9.841860,-1.500576],[4.249393,7.902571,0.198056,-4.987184,1.018279,4.405800,-5.419018,-3.479577,5.851789,-0.877105,-3.385257,5.372866,-2.693554,-8.417260,-4.805546,-2.962732],[3.746841,-7.243695,1.275536,2.489551,-2.995562,4.724408,-9.425485,5.263768,-0.140252,0.150227,8.213725,4.886468,-3.796162,-6.352451,-7.700696,-9.098990],[7.772882,-9.432318,3.951152,6.113663,-7.833249,-7.435104,-2.958784,-3.894629,1.036679,-8.651085,-7.317674,-2.728289,3.088131,-1.938371,-3.145120,6.060663],[7.598640,-9.810530,5.892274,-0.891156,-7.515030,-2.937426,-1.728179,-9.633716,8.316885,-2.114763,-2.500590,-7.554697,-9.027757,8.264124,1.122725,-6.076132],[0.956929,5.547340,-5.660046,-1.920622,-8.674932,-5.122907,-0.450209,-7.156860,5.583670,2.532143,-3.373041,6.963181,-9.602029,5.305895,6.494667,-8.107968],[-9.331254,-0.010241,9.063856,-7.106657,9.935564,9.961426,5.142272,0.068044,-7.843639,-5.409794,-6.769461,7.364513,-1.533504,-3.781869,-3.154476,-2.841625]],[[-5.963551,-2.342817,-8.892479,9.166593,8.665992,9.617688,7.476882,7.313309,4.079628,-9.500728,9.681326,8.314673,-0.140991,3.712363,-7.364278,0.400717],[-8.530958,2.749233,-1.012696,5.952325,2.638576,-6.485977,2.126342,-9.255593,2.466144,9.108280,6.234091,2.867044,-6.567590,-4.376967,-5.695704,-5.086967],[3.601978,7.683871,-0.226681,2.017068,1.584891,-9.691353,5.084768,-8.289264,9.394577,6.713744,-9.003061,-1.789128,-5.721989,2.997672,5.643954,2.100159],[4.472936,-2.320500,9.869892,9.352336,-8.693037,-8.109691,4.178446,-7.403505,-7.064996,6.274934,-8.050991,8.616326,-3.886603,-3.910383,-2.691603,0.748252],[-2.321826,-4.863841,2.614733,7.847996,0.113328,-6.028051,-8.676005,-6.542973,-6.535785,1.667306,6.565296,0.499238,3.709110,0.924989,-0.681249,-8.878813],[3.882909,-2.563768,-5.521780,-4.881676,3.815103,-6.715955,8.093757,-8.651583,-4.575333,3.641321,8.404894,-3.891958,-2.253540,-4.094981,-2.259425,6.190931],[7.276692,-9.641793,0.363264,-5.975915,5.040556,-3.285033,2.242603,9.950129,-3.578437,4.107139,6.883586,6.115867,-7.819189,-9.320745,-2.137856,-3.309246],[-7.325745,3.810752,6.447882,-4.675726,5.820398,5.629372,-7.075575,-1.235038,2.472301,-3.773770,4.080109,-1.249477,4.335089,-8.544828,4.863973,-9.249141],[-2.220484,8.945644,2.453755,-8.118889,8.157181,5.375432,-1.567810,-0.022705,6.810926,5.364630,-5.446506,-2.824960,-2.943757,4.154242,7.146331,5.342131]],[[-7.924246,6.704846,1.896183,-4.635164,-2.794365,-1.057904,6.723671,-3.975166,6.205919,-7.216502,-1.983430,4.631861,3.412649,-7.968671,-4.936136,-6.545186],[-8.965740,-1.780921,-6.787117,-5.621928,-2.028613,4.824172,-6.060256,7.557583,6.799781,5.570773,-7.072474,3.756658,-0.680239,1.879393,2.717472,4.182065],[4.166141,7.271035,-2.834191,-9.207393,-4.385021,-3.897272,-9.833887,-2.616554,6.712934,4.407611,7.104258,-4.451376,-2.790703,-4.903083,1.898135,6.918022],[-7.451159,-6.409519,1.698753,6.707796,0.226692,-7.268973,6.755714,8.789675,-7.343621,9.904516,0.271041,8.979639,3.176125,-5.993796,5.788371,2.114103],[-0.972047,-7.755902,5.249045,-1.558476,-7.477511,-8.079254,0.353036,-0.310979,-3.398617,6.756798,5.426972,7.068382,0.621789,-3.907546,4.951005,-4.976556],[4.747772,8.457838,-9.071595,5.578702,-9.580624,1.928675,-2.643511,-9.786327,2.242509,-8.739460,-6.694429,8.710402,6.995287,0.349291,8.861518,7.045162],[-4.991629,0.646930,-0.163260,1.858944,-1.684470,-3.400034,2.589784,8.801014,6.034553,1.433421,8.358930,8.776351,-7.176333,-2.924132,-3.696369,4.147542],[-5.365179,3.671542,4.483592,-4.838108,6.594862,-9.338730,9.602831,3.485603,-1.827482,-1.349258,0.030681,-6.654260,-1.186426,-4.988391,-9.358785,-6.185044],[-8.731111,1.302418,-2.651336,-6.581786,1.069860,-2.194862,-9.968427,1.028000,1.290844,9.688399,3.947591,-0.170628,-7.917452,-4.055985,-1.552143,9.211254]],[[-9.108157,5.547925,-8.137915,1.534193,-7.013695,-1.770991,2.647430,5.978544,-4.816950,-2.152904,8.877284,2.592559,2.863676,-0.166970,-8.187559,-1.736061],[8.482294,-5.053931,0.572075,7.698903,6.982934,0.130847,4.703180,2.045899,1.243048,4.947552,1.455890,-1.347131,-6.325647,-4.729233,-8.989057,5.893806],[-1.142424,-2.265950,3.502137,-3.814308,0.984030,-2.313826,-6.975384,-2.500276,6.097258,-4.818858,2.338000,0.296082,-3.615372,-5.549045,-7.003630,-7.466255],[6.749827,2.727447,-0.385020,-6.951355,4.365549,-9.665814,-5.457768,1.284118,-7.104506,-9.485087,-1.554979,3.469077,-1.568817,1.321919,6.707926,6.250212],[-8.065939,-0.822061,-9.470432,8.306795,6.323629,-6.862056,-0.852763,9.067757,6.053508,-1.922810,9.905629,-0.527840,-3.333799,-7.941527,7.950667,-7.642303],[-4.376128,-2.734898,4.000496,-2.696282,0.049426,8.594026,-2.327058,-3.258181,-7.801712,3.648369,-8.257878,1.909666,-9.490536,9.072163,-3.988869,8.836537],[-7.584191,7.772653,1.307073,-5.218894,-1.644366,7.388726,-9.476356,6.250001,-8.643943,-8.147146,-9.162825,2.234450,3.405860,5.722138,9.113919,8.102715],[-3.873561,6.621349,-6.709905,9.468302,1.112997,-3.293842,-9.171482,8.804157,-9.509273,-0.351439,4.220990,7.521918,-6.426766,-9.398310,-4.165374,4.389164],[6.570732,-3.114704,-2.391846,-2.417179,-3.887589,4.697009,-5.108529,-7.142790,-6.402518,-4.226733,-6.444639,-0.995463,-5.370821,-7.134732,-4.530013,3.727491]],[[4.477943,-2.068371,8.241073,1.255836,9.531502,4.417581,9.077485,-4.482994,-2.691699,-9.091163,3.884376,2.981664,4.883767,-9.077206,9.897202,0.794167],[3.945574,-4.422786,7.537313,0.719290,-9.239738,-4.880060,-4.057160,6.104839,9.839156,7.153656,-1.106329,-0.127157,7.714509,-0.614328,2.896720,4.929627],[0.731287,0.322478,7.540493,7.696183,2.420421,-0.563223,-3.588076,-7.462295,8.472089,-5.845588,-2.171520,2.740904,0.692843,-9.770317,-9.324164,-5.317124],[6.790397,-5.588179,-1.931003,-8.953539,2.951620,4.958121,-4.139732,-3.335061,8.150751,-0.449204,9.984755,8.564351,1.043336,0.291917,2.375130,7.028773],[-3.552609,-4.530922,7.031834,-0.669201,0.564376,-6.675052,-0.754719,1.506057,-6.039859,5.827547,3.451098,-6.094449,4.664260,-3.578547,8.020829,1.551847],[8.423911,-6.345218,2.468843,-8.385410,-1.470711,-8.759047,8.404145,2.281880,6.337573,4.014989,7.414935,1.090728,-0.021114,-3.017334,6.573084,0.751708],[0.221991,1.651509,-8.936557,0.818872,5.381615,2.672277,2.923944,-6.583055,-6.626168,7.623084,6.298511,-8.786865,3.019297,-0.054639,-7.465415,7.577052],[8.821760,-1.371345,-0.270235,7.892109,-4.929809,-0.127508,5.636059,-5.483280,7.306808,5.494352,3.846312,-6.996056,-5.882666,9.352529,-1.038926,-2.779016],[-2.176062,5.405246,-2.857722,-9.112361,-3.304936,-2.271453,4.934258,0.494476,5.769817,6.624800,-4.171593,7.537511,-2.538819,1.133141,7.557715,2.451886]],[[9.605603,4.926586,0.702661,-1.398291,-1.436435,5.399503,4.513403,-8.025184,1.257693,3.286092,2.602991,1.463142,-8.020005,-5.032860,-6.271495,7.096586],[8.035831,-3.293328,-7.066061,-2.059167,8.912714,-3.525432,-6.770921,4.289531,-9.061028,9.550134,8.316064,-8.488870,0.365076,-8.190113,-5.823249,2.950226],[-2.282737,-0.876982,-7.402320,0.055475,-6.380809,9.518925,6.977742,-6.506049,9.737155,3.873349,-8.502387,-3.975480,1.539396,-1.923163,-9.741760,3.657765],[2.218549,7.793610,-5.528972,5.961852,-3.695920,0.330099,-7.423096,-6.768114,9.762720,-5.257618,3.279910,5.237254,8.139621,-4.789973,-0.040606,-8.031659],[9.484781,6.132596,0.182573,-7.822563,0.289021,6.090411,3.199605,-4.184897,7.285954,8.574547,3.191047,3.524399,-7.406160,7.452626,8.622079,-7.282819],[5.484263,-0.432800,-3.337650,0.922752,-8.435378,8.699186,-6.863492,-6.752056,5.078613,-6.370049,5.678667,5.181882,5.342595,-2.009830,7.544172,1.747580],[-3.073579,5.445688,-1.150106,1.655377,6.594910,-5.122885,-0.576717,4.455023,-3.764486,-6.175316,-6.495159,8.382798,-8.722335,-0.677629,-2.983330,8.876567],[-7.834771,-0.453462,5.216612,8.293042,-8.829168,-0.155158,2.337695,-8.161846,4.192613,4.066906,6.491111,0.784904,-9.333010,5.497505,2.358959,7.285665],[0.143678,-0.165209,5.505247,6.518307,1.953967,-2.025654,1.676729,6.948573,-4.436305,-0.047809,9.963808,7.372657,-1.706664,9.396355,9.709845,4.413264]],[[-1.863802,3.219306,8.431380,8.006092,-7.486860,0.452513,2.031944,-0.485399,2.646015,7.826510,-7.347709,-9.446588,1.122673,-4.327759,9.087266,1.125633],[3.045510,4.949098,1.650165,-0.182354,6.668667,9.442357,-0.031478,-0.535023,1.059682,-0.955108,-8.106537,-8.117754,-8.542968,4.327789,-5.593380,1.795507],[6.191869,-3.196515,-5.873923,6.208870,8.234164,-2.566193,-6.877789,5.457209,-0.404971,-6.094651,6.505788,-7.820178,3.485324,1.922411,-7.425649,-8.078908],[1.299428,-9.646965,0.094211,3.420902,-5.481356,-4.879878,-6.740240,-9.036833,2.110883,-8.053590,4.130706,0.784639,-1.642895,-4.901926,3.264455,-2.909249],[-0.127148,-4.588112,-2.808954,-2.997703,0.240626,-9.178157,-0.504551,-4.671095,1.914862,-3.548978,8.796664,9.704294,-5.477705,-5.745500,-9.760661,8.005241],[8.855165,-6.986973,7.810826,5.697263,9.979302,9.548424,-3.074628,-9.513795,-1.398516,9.872334,-4.327050,2.428603,-0.014833,-3.574076,-9.248625,7.589091],[-0.377071,-6.347314,-0.289485,-2.372692,6.390841,-3.271491,-2.595610,4.081651,6.646333,-0.295053,6.150305,2.028491,-8.382472,1.314878,8.757906,-1.871329],[-1.315737,2.152089,-6.345917,6.554494,1.205342,-8.790885,-9.068144,-0.746957,-9.420005,1.424929,-2.946175,9.568419,-7.962218,-5.138959,-6.476956,0.320720],[4.122210,6.521777,2.610614,7.008781,-9.142503,-4.572004,1.999583,2.666226,5.677173,9.001848,2.369227,-0.786894,4.724844,1.201207,-6.741243,6.500307]]], dtype = "float64")#candidate|9479|(16, 9, 16)|const|float64
bop_9480 = relay.divide(var_9478.astype('float64'), relay.reshape(const_9479.astype('float64'), relay.shape_of(var_9478))) # shape=(16, 9, 16)
output = bop_9480
output2 = bop_9480
func_9491 = relay.Function([var_9478,], output)
mod['func_9491'] = func_9491
mod = relay.transform.InferType()(mod)
mutated_mod['func_9491'] = func_9491
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9492 = relay.var("var_9492", dtype = "float64", shape = (16, 9, 16))#candidate|9492|(16, 9, 16)|var|float64
func_9491_call = mutated_mod.get_global_var('func_9491')
call_9493 = func_9491_call(var_9492)
output = call_9493
func_9494 = relay.Function([var_9492], output)
mutated_mod['func_9494'] = func_9494
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9381_call = mod.get_global_var('func_9381')
func_9382_call = mutated_mod.get_global_var('func_9382')
call_9498 = relay.TupleGetItem(func_9381_call(), 0)
call_9499 = relay.TupleGetItem(func_9382_call(), 0)
output = call_9498
output2 = call_9499
func_9517 = relay.Function([], output)
mod['func_9517'] = func_9517
mod = relay.transform.InferType()(mod)
mutated_mod['func_9517'] = func_9517
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9517_call = mutated_mod.get_global_var('func_9517')
call_9518 = func_9517_call()
output = call_9518
func_9519 = relay.Function([], output)
mutated_mod['func_9519'] = func_9519
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7965_call = mod.get_global_var('func_7965')
func_7966_call = mutated_mod.get_global_var('func_7966')
call_9555 = relay.TupleGetItem(func_7965_call(), 0)
call_9556 = relay.TupleGetItem(func_7966_call(), 0)
output = call_9555
output2 = call_9556
func_9557 = relay.Function([], output)
mod['func_9557'] = func_9557
mod = relay.transform.InferType()(mod)
mutated_mod['func_9557'] = func_9557
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9557_call = mutated_mod.get_global_var('func_9557')
call_9558 = func_9557_call()
output = call_9558
func_9559 = relay.Function([], output)
mutated_mod['func_9559'] = func_9559
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8886_call = mod.get_global_var('func_8886')
func_8888_call = mutated_mod.get_global_var('func_8888')
call_9581 = relay.TupleGetItem(func_8886_call(), 0)
call_9582 = relay.TupleGetItem(func_8888_call(), 0)
output = relay.Tuple([call_9581,])
output2 = relay.Tuple([call_9582,])
func_9632 = relay.Function([], output)
mod['func_9632'] = func_9632
mod = relay.transform.InferType()(mod)
mutated_mod['func_9632'] = func_9632
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9632_call = mutated_mod.get_global_var('func_9632')
call_9633 = func_9632_call()
output = call_9633
func_9634 = relay.Function([], output)
mutated_mod['func_9634'] = func_9634
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4510_call = mod.get_global_var('func_4510')
func_4512_call = mutated_mod.get_global_var('func_4512')
call_9663 = relay.TupleGetItem(func_4510_call(), 3)
call_9664 = relay.TupleGetItem(func_4512_call(), 3)
output = relay.Tuple([call_9663,])
output2 = relay.Tuple([call_9664,])
func_9669 = relay.Function([], output)
mod['func_9669'] = func_9669
mod = relay.transform.InferType()(mod)
output = func_9669()
func_9670 = relay.Function([], output)
mutated_mod['func_9670'] = func_9670
mutated_mod = relay.transform.InferType()(mutated_mod)
const_9731 = relay.const(-3, dtype = "uint16")#candidate|9731|()|const|uint16
var_9732 = relay.var("var_9732", dtype = "uint16", shape = (14, 12, 1))#candidate|9732|(14, 12, 1)|var|uint16
bop_9733 = relay.bitwise_or(const_9731.astype('uint16'), var_9732.astype('uint16')) # shape=(14, 12, 1)
uop_9736 = relay.log2(var_9732.astype('float64')) # shape=(14, 12, 1)
output = relay.Tuple([bop_9733,uop_9736,])
output2 = relay.Tuple([bop_9733,uop_9736,])
func_9757 = relay.Function([var_9732,], output)
mod['func_9757'] = func_9757
mod = relay.transform.InferType()(mod)
var_9758 = relay.var("var_9758", dtype = "uint16", shape = (14, 12, 1))#candidate|9758|(14, 12, 1)|var|uint16
output = func_9757(var_9758)
func_9759 = relay.Function([var_9758], output)
mutated_mod['func_9759'] = func_9759
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5852_call = mod.get_global_var('func_5852')
func_5853_call = mutated_mod.get_global_var('func_5853')
call_9788 = func_5852_call()
call_9789 = func_5852_call()
func_4853_call = mod.get_global_var('func_4853')
func_4855_call = mutated_mod.get_global_var('func_4855')
call_9790 = relay.TupleGetItem(func_4853_call(), 2)
call_9791 = relay.TupleGetItem(func_4855_call(), 2)
output = relay.Tuple([call_9788,call_9790,])
output2 = relay.Tuple([call_9789,call_9791,])
func_9792 = relay.Function([], output)
mod['func_9792'] = func_9792
mod = relay.transform.InferType()(mod)
output = func_9792()
func_9793 = relay.Function([], output)
mutated_mod['func_9793'] = func_9793
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4728_call = mod.get_global_var('func_4728')
func_4730_call = mutated_mod.get_global_var('func_4730')
call_9913 = relay.TupleGetItem(func_4728_call(), 0)
call_9914 = relay.TupleGetItem(func_4730_call(), 0)
func_8936_call = mod.get_global_var('func_8936')
func_8940_call = mutated_mod.get_global_var('func_8940')
var_9920 = relay.var("var_9920", dtype = "float32", shape = (1, 9))#candidate|9920|(1, 9)|var|float32
const_9921 = relay.const([-7,8,-6,-5,-10,-9,-6,9,-6,-4,6,-8,7,-4,-2,-7,-4,4,-7,-2,-6,5,-4,3,-9,-10,5,3,-9,-6,-2,3,9,7,-8,10,3,-5,2,-4,3,3,3,1,-3,-6,2,-2,-5,-5,-9,7,2,7,-8,-4,-9,10,-5,8,9,-2,1,2,-4,-9,5,4,-5,-3,4,-5,-4,-8,9,-6,8,-1,-3,-5,3,-9,7,8,-4,7,6,-2,-1,1,6,8,7,-3,4,9,-9,6,10,1,2,-4,2,-3,8,-2,-1,-8,-10,1,6,-9,-8,2,8,-2,3,-1,1,7,7,-4,8,1,1,-1,-1,4,5,7,-9,-6,-6,7,-10,-9,-4,9,4,-1,1,-4,2,2,-3,-3,-10,7,7,-3,8,5,-4,-5,4,3,-8,6,6,9,6,4,-2,-2,-2,-5,-7,-4,7,-9,-7,-4,1,5,9,7,-8,3,-9,-1,8,-3,8,-7,-9,6,9,1,4,-9,1,-10,6,-3,6,8,-1,10,2,-6,4,-7,6,4,5,2,-1,7,4,2,1,6,3,-1,3,-8,-1,-9,4,-6,-9,4,-9,-5,10,-2,9,5,4,-9,-5,-2,-1,-3,6,-5,-8,-3,2,1,-9,-5,3,-2,-5,-3,-9,9,8,6,-3,-9,10,9,3,-3,5,1,-7,-2,-8,-3,2,7,-5,-3,4,9,-5,-5,10,-9,8,-2,6,7,1,-9,1,-10,-8,5,5,7,6,-6,-2,1,8,-4,9,8,-1,-2,4,-3,7,6,3,1,5,-8,-6,-8,-4,9,-6,-3,6,3,7,2,-3,-5,-2,-6,6,6,2,-6,-8,10,-4,3,8,9,2,-9,-2,1,-1,-2,2,-8,-4,3,-3,-10,-5,6,8,9,9,-5,2,-4,5,-1,8,1,8,-5,-6,8,7,5,9,7,3,8,8,-10,10,9,-3,-9,4,-1,-1,10,-3,5,-10,-10,6,2,-10,6,6,-7,6,1,3,8,1,4,-4,3,-3,1,-1,-3,5,-10,-5,-1,6,-10,-4,-3,-8,-8,-5,-8,-6,-6,-2,-7,-10,-8,-5,-7,1,-1,6,1,-10,6,-9,-4,5,-1,10,-6,6,-5,-4,-3,-8,3,8,-7], dtype = "uint8")#candidate|9921|(432,)|const|uint8
call_9919 = relay.TupleGetItem(func_8936_call(relay.reshape(var_9920.astype('float32'), [9, 1]), relay.reshape(const_9921.astype('uint8'), [432,]), ), 3)
call_9922 = relay.TupleGetItem(func_8940_call(relay.reshape(var_9920.astype('float32'), [9, 1]), relay.reshape(const_9921.astype('uint8'), [432,]), ), 3)
func_4908_call = mod.get_global_var('func_4908')
func_4910_call = mutated_mod.get_global_var('func_4910')
call_9926 = relay.TupleGetItem(func_4908_call(), 0)
call_9927 = relay.TupleGetItem(func_4910_call(), 0)
output = relay.Tuple([call_9913,call_9919,var_9920,const_9921,call_9926,])
output2 = relay.Tuple([call_9914,call_9922,var_9920,const_9921,call_9927,])
func_9929 = relay.Function([var_9920,], output)
mod['func_9929'] = func_9929
mod = relay.transform.InferType()(mod)
var_9930 = relay.var("var_9930", dtype = "float32", shape = (1, 9))#candidate|9930|(1, 9)|var|float32
output = func_9929(var_9930)
func_9931 = relay.Function([var_9930], output)
mutated_mod['func_9931'] = func_9931
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10037 = relay.var("var_10037", dtype = "float32", shape = (10, 3, 12))#candidate|10037|(10, 3, 12)|var|float32
uop_10038 = relay.cos(var_10037.astype('float32')) # shape=(10, 3, 12)
func_5981_call = mod.get_global_var('func_5981')
func_5984_call = mutated_mod.get_global_var('func_5984')
const_10046 = relay.const([-9,-6,-10,5,7,-5,-2,4,-5,2,-8,5,-5,-6,-4,-8,3,-8,-2,8,8,10,10,-6,2,-2,-7,8,7,-10,4,-4,1,9,4,3,-5,-4,6,-10,9,9,-1,8,10,7,-6,-2,-4,2,-2,-1,-7,10,6,2,-3,1,-7,-10,-7,-2,1,-3,8,-4,-2,5,-2,3,-6,5,-5,1,-5,10,1,6,7,-6,7,-5,-5,-8,-7,4,5,3,6,-1,-7,5,-2,-10,2,-6,-4,-10,3,-5,-9,4,-10,4,-10,-1,6,7,-8,-1,-2,1,-9,-4,-9,5,-2,1,-5,-10,-10,6,-6,7,9,-6,6,7,-8,-2,-4,6,5,7,-2,6,7,-1,-4,-9,-8,-4,-2,-4,3,-1,10,-2,5,-4,4,3,2,6,-2,-1,-10,9,-7,6,6,9,-5,2,8,-8,-7,-6,5,-7,1,-9,4,-4,-10,10,-6,-3,-8,10,2,10,9,10,-2,-2,6,3,-9,10,-7,-7,-9,-5,-7,5,-5,9,-3,-9,-8,5,4,4,6,5,4,8,2,2,-8,-9,10,-8,-8,7,8,2,1,-5,1,2,-2,1,-4,3,8,5,-1,2,-10,7,-2,-1,-6,1,6,3,2,2,-4,7,9,1,-7,-9,-3,-6,-7,9,-3,1,2,9,-5,-9,6,-3,10,-4,1,3,-4,-1,7,-4,-8,2,-6,-7,2,2,-4,4,2,-10,-3,-7,3,8,5,2,5,-7,-5,-6,2,6,4,9,-9,-9,3,1,-3,10,1,3,-4,-8,7,-7,-1,-3,4,-3,3,7,-7,6,7,7,-5,-3,5,1,5,-10,-10,3,7,7,7,9,-2,3,-10,7,-5,8,2,-1,-5,5,-6,-9,4,4,-10,7,-8,1,-5,5,7,-1,1,7,-4,1,-3,-2,4,10,9,-6,-10,-6,3,4,-3,10,8,9,-2,-2,9,-1,2,-9,-1,-9,-9,-7,-4,-2,-7,-10,2,8,10,-8,-6,3,2,-10,-6,5,5,8,2,-8,-4,5,10,9,-3,-10,-8,6,7,-5,6,8,4,1,-10,7,9,-2,-3,-10,8,5,5,7,9,6,-4,7,2,3,8,6,10,-6,-8,1,-6,-5,-8,-4,-4,4,-5,-5,-2,-1,-8,8,6,3,2,-4,-8,1,9,5,-8,-1,-2,1,5,-4,10,1,10,10,9,2,10,5,1,-5,1,-1,4,-4,-6,2,-2,2,8,-4,5,-4,9,8,-1,8,-1,-4,-3,-2,9,-6,8,3,-1,2,-2,5,-10,-1,6,-3,-10,-1,-7,3,6,7,9,-1,6,8,-4,9,-4,2,-2,8,-4,-7,2,9,1,-4,-7,-3,-10,2,4,5,4,1,-6,9,5,-3,8,-7,-9,3,7,10,7,-9,-3,-10,-4,4,9,2,-1,-3,8,-10,-10,-2,9,2,3,-10,8,3,2,-3,-3,4,-1,-5,-6,5,-9,3,-8,7,-10,8,-8,1,-10,-10,-3,-1,1,1,-2,-5,3,3,5,-3,-7,-3,3,5,-2,8,-9,-8,-4,10,-7,-1,5,2,-3,4,-5,5,3,-1,4,10,10,-6,1,2,-4,-6,6,8,-2,-9,1,5,5,1,-7,5,-3,4,10,9,9,-1,-3,4,3,-4,-7,-10,-7,2,-4,-3,-1,-10,-3,2,-4,8,-6,-7,-4,-3,2,-3,-4,6,3,6,6,-2,-7,-10,-1,-10,-1,-6,-10,5,-2,-2,3,-6,-7,10,-10,-2,-9,8,3,7,-7,-8,-1,10,9,-2,9,-1,-10,-10,3,7,-6,-6,-7,2,7,2,3,3,-3,6,-1,-10,8,-3,-2,7,-9,9,-7,9,-3,1,-2,-9,9,9,-4,3,9,-7,10,10,-8,-3,-4,-6,-3,4,-3,-2,-10,-4,-10,-10,-5,-9,-10,4,2,2,2,-2,7,2,-8,-4,-5,-7,-5,1,2,7,-1,-2,10,8,2,-9,-5,-10,-3,-5,3,3,-7,-8,-6,-4,7,9,-10,1,6,-10,1,6,-6,-4,3,5,-2,10,1,5,10,5,-1,-1,-8,-8,2,-7,-4,-5,8,6,6,-8,-2,5,6,-1,8,-4,4,7,7,-4,5,-10,1,3,-4,6,-3,-9,1,-8,3,-7,-3,2,-8,-10,8,-6,-6,8,-1,7,5,4,5,5,3,4,6,-5,4,7,-7,-3,-1,6,-7,-5,8,-8,-1,-2,7,-10,4,7,-5,10,-7,-7,-5,-10,6,5,-7,9,-10,-2,-7,-9,-10,-8,3,8,-2,8,-8,10,-6,-9,9,-10,-7,5,-5,-4,5,1,-10,7,4,9,-8,7,3,-6,4,-1,-8,-6,5,9,1,-7,1,-3,3,-6,-1,4,10,6,6,4,6,-9,9,-10,-10,-1,2,3,-6,-6,-5,-10,-2,9,-6,2,-3,2,8,2,10,6,-7,-9,1,9,8,1,4,8,2,-1,-2,9,-8,8,6,1,-7,6,6,4,-3,-5,-4,8,-4,1,5,-6,2,-10,-1,2,9,-6,5,10,4,6,8,-3,4,-10,3,9,-1,-4,10,-10,7,-6,7,-10,-5,8,2,-8,5,-5,-4,-4,5,-9,5,4,7,-2,-9,-5,1,-8,7,7,-3,-10,7,4,-1,7,-4,8,2,-4,-6,-5,-4,-8,-10,3,-7,2,9,6,-1,-8,3,-4,9,7,-1,-10,7,8,-3,1,-5,6,9,4,6,-4,-9,5,10,-3,4,6,1,9], dtype = "int8")#candidate|10046|(1050,)|const|int8
call_10045 = relay.TupleGetItem(func_5981_call(relay.reshape(const_10046.astype('int8'), [1050,])), 0)
call_10047 = relay.TupleGetItem(func_5984_call(relay.reshape(const_10046.astype('int8'), [1050,])), 0)
output = relay.Tuple([uop_10038,call_10045,const_10046,])
output2 = relay.Tuple([uop_10038,call_10047,const_10046,])
func_10064 = relay.Function([var_10037,], output)
mod['func_10064'] = func_10064
mod = relay.transform.InferType()(mod)
mutated_mod['func_10064'] = func_10064
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10065 = relay.var("var_10065", dtype = "float32", shape = (10, 3, 12))#candidate|10065|(10, 3, 12)|var|float32
func_10064_call = mutated_mod.get_global_var('func_10064')
call_10066 = func_10064_call(var_10065)
output = call_10066
func_10067 = relay.Function([var_10065], output)
mutated_mod['func_10067'] = func_10067
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7342_call = mod.get_global_var('func_7342')
func_7343_call = mutated_mod.get_global_var('func_7343')
call_10092 = relay.TupleGetItem(func_7342_call(), 0)
call_10093 = relay.TupleGetItem(func_7343_call(), 0)
output = relay.Tuple([call_10092,])
output2 = relay.Tuple([call_10093,])
func_10102 = relay.Function([], output)
mod['func_10102'] = func_10102
mod = relay.transform.InferType()(mod)
mutated_mod['func_10102'] = func_10102
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10102_call = mutated_mod.get_global_var('func_10102')
call_10103 = func_10102_call()
output = call_10103
func_10104 = relay.Function([], output)
mutated_mod['func_10104'] = func_10104
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4772_call = mod.get_global_var('func_4772')
func_4773_call = mutated_mod.get_global_var('func_4773')
call_10105 = relay.TupleGetItem(func_4772_call(), 1)
call_10106 = relay.TupleGetItem(func_4773_call(), 1)
const_10149 = relay.const([[[False,False,True,True,False,False,True,False,True,False,True],[False,False,True,False,False,False,False,True,False,True,False],[True,True,False,False,True,False,True,False,False,True,False],[False,False,False,False,False,True,True,False,False,False,False],[True,False,False,True,False,True,False,True,False,True,False],[False,True,True,False,True,True,True,False,True,True,True],[False,True,True,True,False,True,True,False,True,False,False],[False,False,False,True,False,True,True,True,False,True,True],[True,False,False,True,True,False,False,False,True,False,True],[False,True,True,True,False,False,True,True,False,True,True],[True,False,True,False,False,False,False,True,True,False,True],[True,True,False,False,True,False,True,False,True,False,True]],[[True,True,False,True,False,True,True,True,False,False,False],[True,True,False,True,True,True,True,True,True,False,False],[True,False,False,False,False,False,True,False,True,False,True],[True,True,False,False,True,True,False,True,True,True,False],[True,True,False,True,False,True,False,False,False,True,True],[False,True,True,False,True,True,True,True,False,True,True],[False,True,False,False,False,True,True,True,False,True,False],[False,False,False,True,False,True,True,True,False,True,True],[True,True,False,False,True,True,False,False,False,True,True],[False,True,True,False,False,True,False,True,True,False,True],[False,True,True,True,True,True,True,False,False,False,False],[False,False,True,True,False,True,False,True,False,False,False]],[[False,False,True,True,False,False,False,False,False,False,False],[True,True,True,False,False,True,False,False,True,False,False],[False,False,True,True,False,False,False,False,True,False,True],[False,True,True,False,True,False,False,False,False,False,True],[True,False,False,False,True,False,False,True,True,False,True],[False,False,True,False,False,False,True,False,True,True,True],[False,False,False,False,False,False,False,False,False,True,True],[False,False,False,False,False,True,True,False,True,True,False],[False,False,False,False,True,False,True,True,True,False,True],[False,False,True,False,True,False,False,False,True,False,False],[True,True,False,False,False,True,True,False,True,False,False],[False,False,True,False,False,False,False,False,True,False,False]],[[True,False,True,True,True,False,False,True,False,True,False],[True,True,True,False,True,True,True,True,True,True,True],[False,False,True,True,False,True,False,False,False,True,False],[True,False,True,True,False,True,False,True,True,True,True],[False,True,False,True,False,True,False,False,False,True,False],[False,False,False,True,False,False,True,False,False,True,False],[False,False,True,True,False,False,False,True,True,True,False],[True,False,True,False,True,True,True,False,True,True,False],[True,False,False,True,False,False,True,True,True,True,True],[False,False,False,False,True,True,False,False,False,True,False],[True,False,True,False,True,True,True,False,True,False,False],[False,True,False,False,False,True,True,False,True,True,False]],[[True,False,True,False,False,True,False,True,False,True,True],[True,True,False,True,False,False,False,False,True,False,True],[True,True,False,True,False,False,False,False,False,True,False],[False,True,False,True,False,True,True,True,True,True,True],[True,False,True,False,False,False,True,True,True,False,False],[True,True,False,True,True,False,False,False,False,False,False],[False,True,False,False,True,True,True,False,False,False,False],[False,False,False,False,True,True,True,False,True,True,True],[False,False,True,False,False,True,True,False,True,True,False],[True,True,True,True,False,True,True,True,True,True,True],[True,True,True,True,True,True,False,False,False,False,False],[True,True,True,True,False,True,False,True,True,False,True]],[[False,True,True,True,False,False,False,False,False,False,True],[True,True,False,False,True,False,False,False,True,False,True],[False,True,True,True,True,False,True,True,True,True,False],[True,True,True,True,True,True,True,True,False,False,False],[True,False,False,True,True,False,False,True,True,False,False],[False,False,True,False,True,True,False,False,True,True,True],[False,False,True,True,False,False,False,False,True,True,True],[True,False,False,True,True,True,False,True,True,False,True],[False,False,False,True,False,True,True,True,False,True,False],[True,True,False,False,True,False,True,False,True,False,False],[True,True,True,False,True,True,True,True,False,False,True],[True,True,False,False,False,True,False,False,True,False,True]],[[True,False,False,False,True,False,True,True,False,True,False],[False,True,True,True,True,False,True,True,True,False,False],[True,False,True,True,True,True,False,True,False,False,True],[False,False,False,False,True,True,False,False,True,False,False],[False,True,True,False,True,False,True,True,False,True,False],[True,False,True,False,False,False,False,False,True,False,False],[True,False,False,False,True,False,True,True,False,True,True],[True,True,False,True,False,True,False,True,True,True,True],[False,False,False,False,False,False,True,True,True,False,True],[True,False,False,True,True,False,False,False,True,True,True],[True,True,False,False,True,True,False,False,True,False,False],[True,True,True,True,False,False,False,True,True,True,True]],[[False,True,True,False,True,True,True,False,True,False,True],[True,False,False,False,False,True,True,True,True,False,False],[False,False,False,False,False,True,False,False,True,False,True],[False,False,False,True,True,False,False,True,False,True,True],[False,False,False,True,True,True,True,False,True,True,False],[True,False,False,True,False,False,False,False,True,False,False],[True,True,True,False,False,False,False,True,True,False,True],[True,False,True,False,True,True,True,False,True,True,False],[True,False,False,False,False,False,True,False,False,True,True],[True,True,True,True,True,True,True,True,False,False,True],[True,True,False,False,False,True,True,True,True,True,True],[False,True,True,False,False,True,True,True,True,False,False]],[[False,False,True,True,True,True,False,True,False,True,False],[True,False,True,False,True,False,True,False,False,True,True],[True,False,False,True,True,True,False,True,False,False,True],[True,False,False,False,False,False,True,True,False,False,True],[True,False,True,False,True,True,False,True,True,True,True],[True,False,False,False,False,True,False,True,True,False,True],[True,False,True,True,True,False,False,True,False,True,True],[True,True,True,False,True,False,True,True,True,False,True],[True,True,False,False,True,True,True,True,False,True,False],[True,False,True,True,False,True,True,False,False,False,True],[True,True,True,True,False,False,False,True,True,True,False],[True,False,True,False,True,True,False,False,True,True,True]],[[False,True,True,True,False,True,False,True,True,True,False],[False,True,False,False,True,True,True,True,True,True,True],[True,True,False,False,False,True,True,True,False,True,False],[True,True,True,True,True,False,False,False,False,False,True],[False,False,True,False,True,False,True,False,True,False,False],[True,False,False,False,True,True,False,True,False,False,False],[True,True,True,True,True,True,True,True,True,True,True],[False,True,False,False,True,True,True,True,True,False,False],[True,True,True,False,True,False,False,True,False,True,False],[True,False,True,True,True,False,False,True,True,False,False],[False,False,True,True,True,True,False,True,True,True,False],[False,True,False,True,False,True,True,True,False,True,False]],[[True,False,True,False,False,False,True,False,True,True,False],[False,False,True,True,False,False,False,True,True,True,True],[True,False,True,False,True,False,False,False,False,False,False],[False,False,False,False,True,False,True,True,False,False,True],[True,True,False,False,False,True,True,True,False,False,True],[True,False,False,False,True,True,False,True,True,False,True],[False,True,False,False,False,True,True,False,True,False,False],[True,False,False,False,True,True,True,True,False,False,False],[False,False,True,True,True,False,True,True,True,True,False],[True,True,True,True,False,True,False,True,True,True,True],[True,True,True,False,False,False,False,True,False,True,True],[True,False,False,True,True,False,False,False,False,False,False]]], dtype = "bool")#candidate|10149|(11, 12, 11)|const|bool
bop_10150 = relay.power(call_10105.astype('float32'), relay.reshape(const_10149.astype('float32'), relay.shape_of(call_10105))) # shape=(11, 12, 11)
bop_10153 = relay.power(call_10106.astype('float32'), relay.reshape(const_10149.astype('float32'), relay.shape_of(call_10106))) # shape=(11, 12, 11)
uop_10160 = relay.sigmoid(const_10149.astype('float64')) # shape=(11, 12, 11)
func_6499_call = mod.get_global_var('func_6499')
func_6501_call = mutated_mod.get_global_var('func_6501')
call_10169 = relay.TupleGetItem(func_6499_call(), 1)
call_10170 = relay.TupleGetItem(func_6501_call(), 1)
output = relay.Tuple([bop_10150,uop_10160,call_10169,])
output2 = relay.Tuple([bop_10153,uop_10160,call_10170,])
func_10186 = relay.Function([], output)
mod['func_10186'] = func_10186
mod = relay.transform.InferType()(mod)
mutated_mod['func_10186'] = func_10186
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10186_call = mutated_mod.get_global_var('func_10186')
call_10187 = func_10186_call()
output = call_10187
func_10188 = relay.Function([], output)
mutated_mod['func_10188'] = func_10188
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6529_call = mod.get_global_var('func_6529')
func_6531_call = mutated_mod.get_global_var('func_6531')
call_10189 = relay.TupleGetItem(func_6529_call(), 0)
call_10190 = relay.TupleGetItem(func_6531_call(), 0)
output = call_10189
output2 = call_10190
func_10198 = relay.Function([], output)
mod['func_10198'] = func_10198
mod = relay.transform.InferType()(mod)
mutated_mod['func_10198'] = func_10198
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10198_call = mutated_mod.get_global_var('func_10198')
call_10199 = func_10198_call()
output = call_10199
func_10200 = relay.Function([], output)
mutated_mod['func_10200'] = func_10200
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9792_call = mod.get_global_var('func_9792')
func_9793_call = mutated_mod.get_global_var('func_9793')
call_10247 = relay.TupleGetItem(func_9792_call(), 0)
call_10248 = relay.TupleGetItem(func_9793_call(), 0)
output = call_10247
output2 = call_10248
func_10249 = relay.Function([], output)
mod['func_10249'] = func_10249
mod = relay.transform.InferType()(mod)
output = func_10249()
func_10250 = relay.Function([], output)
mutated_mod['func_10250'] = func_10250
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6529_call = mod.get_global_var('func_6529')
func_6531_call = mutated_mod.get_global_var('func_6531')
call_10279 = relay.TupleGetItem(func_6529_call(), 0)
call_10280 = relay.TupleGetItem(func_6531_call(), 0)
func_7616_call = mod.get_global_var('func_7616')
func_7617_call = mutated_mod.get_global_var('func_7617')
call_10282 = relay.TupleGetItem(func_7616_call(), 1)
call_10283 = relay.TupleGetItem(func_7617_call(), 1)
func_4581_call = mod.get_global_var('func_4581')
func_4582_call = mutated_mod.get_global_var('func_4582')
call_10284 = relay.TupleGetItem(func_4581_call(), 2)
call_10285 = relay.TupleGetItem(func_4582_call(), 2)
output = relay.Tuple([call_10279,call_10282,call_10284,])
output2 = relay.Tuple([call_10280,call_10283,call_10285,])
func_10297 = relay.Function([], output)
mod['func_10297'] = func_10297
mod = relay.transform.InferType()(mod)
mutated_mod['func_10297'] = func_10297
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10297_call = mutated_mod.get_global_var('func_10297')
call_10298 = func_10297_call()
output = call_10298
func_10299 = relay.Function([], output)
mutated_mod['func_10299'] = func_10299
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5774_call = mod.get_global_var('func_5774')
func_5775_call = mutated_mod.get_global_var('func_5775')
call_10308 = relay.TupleGetItem(func_5774_call(), 0)
call_10309 = relay.TupleGetItem(func_5775_call(), 0)
func_7264_call = mod.get_global_var('func_7264')
func_7266_call = mutated_mod.get_global_var('func_7266')
call_10318 = relay.TupleGetItem(func_7264_call(), 1)
call_10319 = relay.TupleGetItem(func_7266_call(), 1)
func_6926_call = mod.get_global_var('func_6926')
func_6927_call = mutated_mod.get_global_var('func_6927')
call_10322 = func_6926_call()
call_10323 = func_6926_call()
output = relay.Tuple([call_10308,call_10318,call_10322,])
output2 = relay.Tuple([call_10309,call_10319,call_10323,])
func_10335 = relay.Function([], output)
mod['func_10335'] = func_10335
mod = relay.transform.InferType()(mod)
output = func_10335()
func_10336 = relay.Function([], output)
mutated_mod['func_10336'] = func_10336
mutated_mod = relay.transform.InferType()(mutated_mod)
const_10365 = relay.const([[[9.678651,2.842349,0.685286,5.518075,-6.497109,-7.746352],[0.153415,-1.119796,8.938711,-4.482633,-9.084880,0.751687],[0.313682,-0.678743,-2.726234,9.848852,-3.037374,-0.415395],[8.957271,-5.932631,7.172564,8.052426,-3.625269,-2.688895],[3.576215,5.714233,3.249218,0.573499,-3.050463,-0.635610],[7.379239,-5.463544,9.093296,2.767966,1.711806,-0.847904],[1.356658,5.225338,-6.056029,3.174708,-4.228835,1.182512],[7.710303,-3.439779,-8.589648,3.707011,-4.239921,-2.866260]],[[-7.052151,5.670151,2.143888,9.317077,0.499469,-3.372812],[-9.383655,2.934899,-9.889785,2.292820,-4.600524,0.615701],[-2.706773,-1.743748,0.151619,-8.397501,8.163203,5.330420],[-7.071328,9.591970,9.345740,4.388834,7.899499,-8.118480],[1.770839,-4.234333,5.365726,2.739883,-6.981021,-9.817965],[-9.579344,1.639110,-5.396197,-7.217517,0.019632,-1.471435],[0.579795,5.911491,1.323955,-0.717448,4.791113,-6.423813],[-6.379725,-0.564409,4.161861,-4.829734,-8.733231,1.040456]],[[-7.783415,4.373066,0.579409,-9.181785,1.504837,-7.676764],[2.252898,3.402971,3.135940,7.311363,8.034565,-8.976501],[0.536478,-5.376163,-8.846993,-0.132903,4.239558,8.016782],[-5.361219,7.898016,3.667959,-4.535849,-2.593368,7.147582],[0.038896,-0.278546,-5.109864,6.151987,9.439318,7.675978],[-0.383673,2.909561,4.841028,-0.551948,-9.569490,8.833811],[3.567408,7.542411,-8.332782,9.642640,8.158457,-1.200584],[-9.410953,9.414171,-5.208633,-1.139844,4.798600,-0.921434]],[[-8.224304,-9.733569,9.763189,-5.127384,6.746400,-8.806077],[-2.454986,0.715626,6.467275,2.988052,1.624290,-2.027736],[-9.807428,-4.038498,-6.957298,-3.498259,-3.829954,6.313344],[5.078323,-9.753601,3.507893,-9.189460,4.142866,-4.890651],[8.254356,-3.763029,-6.814760,-0.386682,1.743584,-8.868183],[-7.013633,-3.047305,7.144381,-7.131648,1.898390,1.349797],[1.085207,-3.631812,7.343851,-6.594504,7.523486,-2.135762],[6.423972,-7.668091,0.801158,-9.917181,0.096218,-1.480905]],[[-2.985813,1.206265,-4.580603,3.675767,-7.871183,-1.210217],[-9.819361,1.542154,5.762049,3.675022,-4.169608,-2.823353],[4.254531,4.998797,3.275030,0.711556,-8.813643,-2.956901],[-9.202173,8.800254,7.420082,-9.145851,-2.651803,5.461519],[7.572843,-1.101090,-9.718103,-5.715911,6.282154,6.132368],[9.613890,-4.214658,2.279863,-1.272869,-0.141618,2.667576],[4.909272,5.686507,0.303151,-8.540238,-0.253122,-1.835670],[3.650459,-6.908891,4.216983,2.501788,-2.763279,-2.629554]],[[-4.050858,2.618695,-8.651010,8.420494,2.008781,3.358057],[0.565989,7.146301,-7.554874,6.671343,-8.515334,-8.833110],[6.593575,4.254610,-0.736502,2.593262,-3.295261,5.250095],[3.205924,6.337275,-5.887533,7.142726,-4.188496,8.463966],[7.733179,-9.319101,-4.074401,3.351929,-5.907033,8.941622],[-0.973892,-1.918718,-3.449647,-6.770850,-3.452823,-6.620544],[-4.904809,-8.974034,-9.535885,-7.616620,-5.402158,-0.135122],[9.207612,-1.505277,-9.209916,-5.249187,2.452201,8.598769]],[[2.672483,5.095351,4.429352,-4.869004,-5.182439,-3.130015],[-5.456305,-4.099450,2.556668,3.963542,-5.295763,4.377223],[5.476134,2.174784,-9.492562,-8.921203,-1.430054,6.227274],[0.266295,-5.962346,-0.862270,7.096308,5.794229,-7.992022],[-4.397457,5.247378,3.383731,2.323075,3.097149,1.408680],[2.233363,2.507822,-9.167158,-2.177657,-0.859288,4.001866],[5.909814,1.379648,-6.247088,-1.952875,0.398111,1.372732],[-0.464275,5.211736,9.987297,1.993871,9.929419,2.327638]]], dtype = "float32")#candidate|10365|(7, 8, 6)|const|float32
var_10366 = relay.var("var_10366", dtype = "float32", shape = (7, 8, 6))#candidate|10366|(7, 8, 6)|var|float32
bop_10367 = relay.floor_mod(const_10365.astype('float32'), relay.reshape(var_10366.astype('float32'), relay.shape_of(const_10365))) # shape=(7, 8, 6)
func_6896_call = mod.get_global_var('func_6896')
func_6898_call = mutated_mod.get_global_var('func_6898')
call_10383 = func_6896_call()
call_10384 = func_6896_call()
output = relay.Tuple([bop_10367,call_10383,])
output2 = relay.Tuple([bop_10367,call_10384,])
func_10393 = relay.Function([var_10366,], output)
mod['func_10393'] = func_10393
mod = relay.transform.InferType()(mod)
var_10394 = relay.var("var_10394", dtype = "float32", shape = (7, 8, 6))#candidate|10394|(7, 8, 6)|var|float32
output = func_10393(var_10394)
func_10395 = relay.Function([var_10394], output)
mutated_mod['func_10395'] = func_10395
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10249_call = mod.get_global_var('func_10249')
func_10250_call = mutated_mod.get_global_var('func_10250')
call_10538 = func_10249_call()
call_10539 = func_10249_call()
func_9104_call = mod.get_global_var('func_9104')
func_9105_call = mutated_mod.get_global_var('func_9105')
call_10554 = relay.TupleGetItem(func_9104_call(), 0)
call_10555 = relay.TupleGetItem(func_9105_call(), 0)
func_9043_call = mod.get_global_var('func_9043')
func_9045_call = mutated_mod.get_global_var('func_9045')
call_10558 = relay.TupleGetItem(func_9043_call(), 0)
call_10559 = relay.TupleGetItem(func_9045_call(), 0)
func_8755_call = mod.get_global_var('func_8755')
func_8756_call = mutated_mod.get_global_var('func_8756')
call_10564 = func_8755_call()
call_10565 = func_8755_call()
func_8798_call = mod.get_global_var('func_8798')
func_8799_call = mutated_mod.get_global_var('func_8799')
call_10594 = relay.TupleGetItem(func_8798_call(), 1)
call_10595 = relay.TupleGetItem(func_8799_call(), 1)
output = relay.Tuple([call_10538,call_10554,call_10558,call_10564,call_10594,])
output2 = relay.Tuple([call_10539,call_10555,call_10559,call_10565,call_10595,])
func_10596 = relay.Function([], output)
mod['func_10596'] = func_10596
mod = relay.transform.InferType()(mod)
mutated_mod['func_10596'] = func_10596
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10596_call = mutated_mod.get_global_var('func_10596')
call_10597 = func_10596_call()
output = call_10597
func_10598 = relay.Function([], output)
mutated_mod['func_10598'] = func_10598
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9029_call = mod.get_global_var('func_9029')
func_9031_call = mutated_mod.get_global_var('func_9031')
call_10706 = relay.TupleGetItem(func_9029_call(), 0)
call_10707 = relay.TupleGetItem(func_9031_call(), 0)
output = call_10706
output2 = call_10707
func_10717 = relay.Function([], output)
mod['func_10717'] = func_10717
mod = relay.transform.InferType()(mod)
mutated_mod['func_10717'] = func_10717
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10717_call = mutated_mod.get_global_var('func_10717')
call_10718 = func_10717_call()
output = call_10718
func_10719 = relay.Function([], output)
mutated_mod['func_10719'] = func_10719
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10761 = relay.var("var_10761", dtype = "float32", shape = (11, 11, 1))#candidate|10761|(11, 11, 1)|var|float32
uop_10762 = relay.tan(var_10761.astype('float32')) # shape=(11, 11, 1)
output = uop_10762
output2 = uop_10762
func_10778 = relay.Function([var_10761,], output)
mod['func_10778'] = func_10778
mod = relay.transform.InferType()(mod)
var_10779 = relay.var("var_10779", dtype = "float32", shape = (11, 11, 1))#candidate|10779|(11, 11, 1)|var|float32
output = func_10778(var_10779)
func_10780 = relay.Function([var_10779], output)
mutated_mod['func_10780'] = func_10780
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8133_call = mod.get_global_var('func_8133')
func_8134_call = mutated_mod.get_global_var('func_8134')
call_10802 = relay.TupleGetItem(func_8133_call(), 0)
call_10803 = relay.TupleGetItem(func_8134_call(), 0)
output = relay.Tuple([call_10802,])
output2 = relay.Tuple([call_10803,])
func_10822 = relay.Function([], output)
mod['func_10822'] = func_10822
mod = relay.transform.InferType()(mod)
mutated_mod['func_10822'] = func_10822
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10822_call = mutated_mod.get_global_var('func_10822')
call_10823 = func_10822_call()
output = call_10823
func_10824 = relay.Function([], output)
mutated_mod['func_10824'] = func_10824
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7389_call = mod.get_global_var('func_7389')
func_7391_call = mutated_mod.get_global_var('func_7391')
call_10839 = func_7389_call()
call_10840 = func_7389_call()
func_9216_call = mod.get_global_var('func_9216')
func_9218_call = mutated_mod.get_global_var('func_9218')
call_10849 = relay.TupleGetItem(func_9216_call(), 0)
call_10850 = relay.TupleGetItem(func_9218_call(), 0)
func_10822_call = mod.get_global_var('func_10822')
func_10824_call = mutated_mod.get_global_var('func_10824')
call_10859 = relay.TupleGetItem(func_10822_call(), 0)
call_10860 = relay.TupleGetItem(func_10824_call(), 0)
output = relay.Tuple([call_10839,call_10849,call_10859,])
output2 = relay.Tuple([call_10840,call_10850,call_10860,])
func_10861 = relay.Function([], output)
mod['func_10861'] = func_10861
mod = relay.transform.InferType()(mod)
mutated_mod['func_10861'] = func_10861
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10861_call = mutated_mod.get_global_var('func_10861')
call_10862 = func_10861_call()
output = call_10862
func_10863 = relay.Function([], output)
mutated_mod['func_10863'] = func_10863
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7537_call = mod.get_global_var('func_7537')
func_7539_call = mutated_mod.get_global_var('func_7539')
call_10877 = relay.TupleGetItem(func_7537_call(), 1)
call_10878 = relay.TupleGetItem(func_7539_call(), 1)
output = relay.Tuple([call_10877,])
output2 = relay.Tuple([call_10878,])
func_10879 = relay.Function([], output)
mod['func_10879'] = func_10879
mod = relay.transform.InferType()(mod)
mutated_mod['func_10879'] = func_10879
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10879_call = mutated_mod.get_global_var('func_10879')
call_10880 = func_10879_call()
output = call_10880
func_10881 = relay.Function([], output)
mutated_mod['func_10881'] = func_10881
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8474_call = mod.get_global_var('func_8474')
func_8476_call = mutated_mod.get_global_var('func_8476')
call_10911 = relay.TupleGetItem(func_8474_call(), 0)
call_10912 = relay.TupleGetItem(func_8476_call(), 0)
func_6753_call = mod.get_global_var('func_6753')
func_6755_call = mutated_mod.get_global_var('func_6755')
var_10929 = relay.var("var_10929", dtype = "uint8", shape = (432,))#candidate|10929|(432,)|var|uint8
call_10928 = relay.TupleGetItem(func_6753_call(relay.reshape(var_10929.astype('uint8'), [216, 2])), 3)
call_10930 = relay.TupleGetItem(func_6755_call(relay.reshape(var_10929.astype('uint8'), [216, 2])), 3)
output = relay.Tuple([call_10911,call_10928,var_10929,])
output2 = relay.Tuple([call_10912,call_10930,var_10929,])
func_10934 = relay.Function([var_10929,], output)
mod['func_10934'] = func_10934
mod = relay.transform.InferType()(mod)
var_10935 = relay.var("var_10935", dtype = "uint8", shape = (432,))#candidate|10935|(432,)|var|uint8
output = func_10934(var_10935)
func_10936 = relay.Function([var_10935], output)
mutated_mod['func_10936'] = func_10936
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10952 = relay.var("var_10952", dtype = "float32", shape = (10, 1, 10))#candidate|10952|(10, 1, 10)|var|float32
uop_10953 = relay.cosh(var_10952.astype('float32')) # shape=(10, 1, 10)
output = uop_10953
output2 = uop_10953
func_10970 = relay.Function([var_10952,], output)
mod['func_10970'] = func_10970
mod = relay.transform.InferType()(mod)
mutated_mod['func_10970'] = func_10970
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10971 = relay.var("var_10971", dtype = "float32", shape = (10, 1, 10))#candidate|10971|(10, 1, 10)|var|float32
func_10970_call = mutated_mod.get_global_var('func_10970')
call_10972 = func_10970_call(var_10971)
output = call_10972
func_10973 = relay.Function([var_10971], output)
mutated_mod['func_10973'] = func_10973
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5215_call = mod.get_global_var('func_5215')
func_5217_call = mutated_mod.get_global_var('func_5217')
call_10995 = relay.TupleGetItem(func_5215_call(), 0)
call_10996 = relay.TupleGetItem(func_5217_call(), 0)
func_1019_call = mod.get_global_var('func_1019')
func_1023_call = mutated_mod.get_global_var('func_1023')
var_11028 = relay.var("var_11028", dtype = "uint8", shape = (432,))#candidate|11028|(432,)|var|uint8
call_11027 = func_1019_call(relay.reshape(var_11028.astype('uint8'), [6, 12, 6]), relay.reshape(var_11028.astype('uint8'), [6, 12, 6]), )
call_11029 = func_1019_call(relay.reshape(var_11028.astype('uint8'), [6, 12, 6]), relay.reshape(var_11028.astype('uint8'), [6, 12, 6]), )
output = relay.Tuple([call_10995,call_11027,var_11028,])
output2 = relay.Tuple([call_10996,call_11029,var_11028,])
func_11034 = relay.Function([var_11028,], output)
mod['func_11034'] = func_11034
mod = relay.transform.InferType()(mod)
var_11035 = relay.var("var_11035", dtype = "uint8", shape = (432,))#candidate|11035|(432,)|var|uint8
output = func_11034(var_11035)
func_11036 = relay.Function([var_11035], output)
mutated_mod['func_11036'] = func_11036
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9104_call = mod.get_global_var('func_9104')
func_9105_call = mutated_mod.get_global_var('func_9105')
call_11070 = relay.TupleGetItem(func_9104_call(), 0)
call_11071 = relay.TupleGetItem(func_9105_call(), 0)
var_11078 = relay.var("var_11078", dtype = "float32", shape = (7, 16, 7))#candidate|11078|(7, 16, 7)|var|float32
bop_11079 = relay.logical_and(call_11070.astype('bool'), relay.reshape(var_11078.astype('bool'), relay.shape_of(call_11070))) # shape=(7, 16, 7)
bop_11082 = relay.logical_and(call_11071.astype('bool'), relay.reshape(var_11078.astype('bool'), relay.shape_of(call_11071))) # shape=(7, 16, 7)
output = bop_11079
output2 = bop_11082
func_11087 = relay.Function([var_11078,], output)
mod['func_11087'] = func_11087
mod = relay.transform.InferType()(mod)
mutated_mod['func_11087'] = func_11087
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11088 = relay.var("var_11088", dtype = "float32", shape = (7, 16, 7))#candidate|11088|(7, 16, 7)|var|float32
func_11087_call = mutated_mod.get_global_var('func_11087')
call_11089 = func_11087_call(var_11088)
output = call_11089
func_11090 = relay.Function([var_11088], output)
mutated_mod['func_11090'] = func_11090
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10198_call = mod.get_global_var('func_10198')
func_10200_call = mutated_mod.get_global_var('func_10200')
call_11176 = func_10198_call()
call_11177 = func_10198_call()
var_11178 = relay.var("var_11178", dtype = "float32", shape = (7, 16, 7))#candidate|11178|(7, 16, 7)|var|float32
bop_11179 = relay.less_equal(call_11176.astype('bool'), relay.reshape(var_11178.astype('bool'), relay.shape_of(call_11176))) # shape=(7, 16, 7)
bop_11182 = relay.less_equal(call_11177.astype('bool'), relay.reshape(var_11178.astype('bool'), relay.shape_of(call_11177))) # shape=(7, 16, 7)
func_2677_call = mod.get_global_var('func_2677')
func_2682_call = mutated_mod.get_global_var('func_2682')
var_11184 = relay.var("var_11184", dtype = "int8", shape = (1050,))#candidate|11184|(1050,)|var|int8
const_11185 = relay.const([6,-1,-2,2,9,-7,6,-4,4,8,10,-9,-10,-4,-2,5,6,9,-9,10,-8,-3,-6,-7,-4,2,-10,-8,5,-9,8,-9,2,-6,10,-10,-2,-1,7,-9,-4,-5,-4,-7,7,-10,-10,1,6,4,1,2,-5,2,-2,-5,3,-3,2,-8,5,-6,-6,10,4,5,8,-1,-10,-8,-5,1,2,-5,-3,3,-2,7,-6,7,1,-7,9,5,-2,-2,-6,3,6,-2,2,8,-6,9,2,-4,-9,-5,3,-8,2,2,-2,6,4,8,5,9,3,-5,-7,9,4,-2,3,-1,-9,-3,-7,-8,6,8,-2,-3,6,-9,9,-7,-3,7,9,8,-1,9,-9,9,-3,-9,4,9,1,5,9,10,-2,-5,-7,1,6,-5,8,-4,-1,-5,4,6,-5,5,2,-5,6,-7,3,-8,9,5,9,8,2,-6,-9,-4,-3,10,6,-2,-5,3,7,8,7,3,3,-6,5,3,-4,10,-4,3,-8,-2,3,1,-9,8,-2,-1,-2,-2,-1,-3,-10,2,-5,-5,1,-6,-3,6,3,7,9,-2,7,8,-1,-4,-5,-6,-5,-5,-10,-1,-7,-4,-5,8,1,4,8,-7,-4,9,-1,-4,-7,1,10,-2,-2,-9,-1,10,-9,-1,8,-3,1,4,6,-8,-6,2,-2,-5,5,1,1,8,-6,6,-9,8,10,3,1,10,-10,-5,9,7,4,-9,-9,-6,6,-1,-10,4,-3,7,-8,-3,-9,1,2,3,-3,-2,1,-9,9,-1,-3,8,-4,1,-2,-10,-7,-3,8,5,-10,8,-5,8,9,3,-6,9,8,4,6,-4,-7,-2,-3,-8,3,2,-3,2,-10,5,9,-6,3,8,-5,2,7,9,-10,1,-3,1,-3,-1,9,-7,-7,5,4,-9,4,-1,5,3,6,-9,6,8,-5,2,-2,-4,1,-1,3,-4,-3,-9,4,4,-5,9,-2,-1,-6,3,-2,-9,6,-10,9,-5,-8,1,-8,1,9,-7,9,-10,-2,2,-9,9,-10,4,4,4,-6,3,1,9,4,-10,3,7,-4,1,10,9,-10,1,-2,7,1,4,-4,3,9,2,-5,9,-5,-1,2,-5,2,-6,3,2,3,-6,-1,6,2,5], dtype = "uint8")#candidate|11185|(432,)|const|uint8
call_11183 = relay.TupleGetItem(func_2677_call(relay.reshape(var_11184.astype('int8'), [15, 5, 14]), relay.reshape(var_11184.astype('int8'), [15, 5, 14]), relay.reshape(var_11184.astype('int8'), [15, 5, 14]), relay.reshape(const_11185.astype('uint8'), [432,]), ), 0)
call_11186 = relay.TupleGetItem(func_2682_call(relay.reshape(var_11184.astype('int8'), [15, 5, 14]), relay.reshape(var_11184.astype('int8'), [15, 5, 14]), relay.reshape(var_11184.astype('int8'), [15, 5, 14]), relay.reshape(const_11185.astype('uint8'), [432,]), ), 0)
output = relay.Tuple([bop_11179,call_11183,var_11184,const_11185,])
output2 = relay.Tuple([bop_11182,call_11186,var_11184,const_11185,])
func_11210 = relay.Function([var_11178,var_11184,], output)
mod['func_11210'] = func_11210
mod = relay.transform.InferType()(mod)
mutated_mod['func_11210'] = func_11210
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11210_call = mutated_mod.get_global_var('func_11210')
var_11212 = relay.var("var_11212", dtype = "float32", shape = (7, 16, 7))#candidate|11212|(7, 16, 7)|var|float32
var_11213 = relay.var("var_11213", dtype = "int8", shape = (1050,))#candidate|11213|(1050,)|var|int8
call_11211 = func_11210_call(var_11212,var_11213,)
output = call_11211
func_11214 = relay.Function([var_11212,var_11213,], output)
mutated_mod['func_11214'] = func_11214
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11258 = relay.var("var_11258", dtype = "float32", shape = (10, 16, 8))#candidate|11258|(10, 16, 8)|var|float32
uop_11259 = relay.atanh(var_11258.astype('float32')) # shape=(10, 16, 8)
output = uop_11259
output2 = uop_11259
func_11266 = relay.Function([var_11258,], output)
mod['func_11266'] = func_11266
mod = relay.transform.InferType()(mod)
mutated_mod['func_11266'] = func_11266
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11267 = relay.var("var_11267", dtype = "float32", shape = (10, 16, 8))#candidate|11267|(10, 16, 8)|var|float32
func_11266_call = mutated_mod.get_global_var('func_11266')
call_11268 = func_11266_call(var_11267)
output = call_11268
func_11269 = relay.Function([var_11267], output)
mutated_mod['func_11269'] = func_11269
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10879_call = mod.get_global_var('func_10879')
func_10881_call = mutated_mod.get_global_var('func_10881')
call_11276 = relay.TupleGetItem(func_10879_call(), 0)
call_11277 = relay.TupleGetItem(func_10881_call(), 0)
output = relay.Tuple([call_11276,])
output2 = relay.Tuple([call_11277,])
func_11278 = relay.Function([], output)
mod['func_11278'] = func_11278
mod = relay.transform.InferType()(mod)
mutated_mod['func_11278'] = func_11278
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11278_call = mutated_mod.get_global_var('func_11278')
call_11279 = func_11278_call()
output = call_11279
func_11280 = relay.Function([], output)
mutated_mod['func_11280'] = func_11280
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7264_call = mod.get_global_var('func_7264')
func_7266_call = mutated_mod.get_global_var('func_7266')
call_11303 = relay.TupleGetItem(func_7264_call(), 0)
call_11304 = relay.TupleGetItem(func_7266_call(), 0)
func_8936_call = mod.get_global_var('func_8936')
func_8940_call = mutated_mod.get_global_var('func_8940')
var_11332 = relay.var("var_11332", dtype = "float32", shape = (9,))#candidate|11332|(9,)|var|float32
call_11331 = relay.TupleGetItem(func_8936_call(relay.reshape(var_11332.astype('float32'), [9, 1]), relay.reshape(call_11303.astype('uint8'), [432,]), ), 4)
call_11333 = relay.TupleGetItem(func_8940_call(relay.reshape(var_11332.astype('float32'), [9, 1]), relay.reshape(call_11303.astype('uint8'), [432,]), ), 4)
output = relay.Tuple([call_11303,call_11331,var_11332,])
output2 = relay.Tuple([call_11304,call_11333,var_11332,])
func_11354 = relay.Function([var_11332,], output)
mod['func_11354'] = func_11354
mod = relay.transform.InferType()(mod)
var_11355 = relay.var("var_11355", dtype = "float32", shape = (9,))#candidate|11355|(9,)|var|float32
output = func_11354(var_11355)
func_11356 = relay.Function([var_11355], output)
mutated_mod['func_11356'] = func_11356
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7812_call = mod.get_global_var('func_7812')
func_7813_call = mutated_mod.get_global_var('func_7813')
call_11399 = relay.TupleGetItem(func_7812_call(), 0)
call_11400 = relay.TupleGetItem(func_7813_call(), 0)
var_11407 = relay.var("var_11407", dtype = "float32", shape = (8, 7, 11))#candidate|11407|(8, 7, 11)|var|float32
bop_11408 = relay.subtract(call_11399.astype('int8'), relay.reshape(var_11407.astype('int8'), relay.shape_of(call_11399))) # shape=(8, 7, 11)
bop_11411 = relay.subtract(call_11400.astype('int8'), relay.reshape(var_11407.astype('int8'), relay.shape_of(call_11400))) # shape=(8, 7, 11)
func_5774_call = mod.get_global_var('func_5774')
func_5775_call = mutated_mod.get_global_var('func_5775')
call_11416 = relay.TupleGetItem(func_5774_call(), 0)
call_11417 = relay.TupleGetItem(func_5775_call(), 0)
uop_11432 = relay.cos(call_11399.astype('float64')) # shape=(8, 7, 11)
uop_11434 = relay.cos(call_11400.astype('float64')) # shape=(8, 7, 11)
output = relay.Tuple([bop_11408,call_11416,uop_11432,])
output2 = relay.Tuple([bop_11411,call_11417,uop_11434,])
func_11447 = relay.Function([var_11407,], output)
mod['func_11447'] = func_11447
mod = relay.transform.InferType()(mod)
mutated_mod['func_11447'] = func_11447
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11448 = relay.var("var_11448", dtype = "float32", shape = (8, 7, 11))#candidate|11448|(8, 7, 11)|var|float32
func_11447_call = mutated_mod.get_global_var('func_11447')
call_11449 = func_11447_call(var_11448)
output = call_11449
func_11450 = relay.Function([var_11448], output)
mutated_mod['func_11450'] = func_11450
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4510_call = mod.get_global_var('func_4510')
func_4512_call = mutated_mod.get_global_var('func_4512')
call_11454 = relay.TupleGetItem(func_4510_call(), 0)
call_11455 = relay.TupleGetItem(func_4512_call(), 0)
func_5852_call = mod.get_global_var('func_5852')
func_5853_call = mutated_mod.get_global_var('func_5853')
call_11460 = func_5852_call()
call_11461 = func_5852_call()
func_10249_call = mod.get_global_var('func_10249')
func_10250_call = mutated_mod.get_global_var('func_10250')
call_11462 = func_10249_call()
call_11463 = func_10249_call()
func_10861_call = mod.get_global_var('func_10861')
func_10863_call = mutated_mod.get_global_var('func_10863')
call_11464 = relay.TupleGetItem(func_10861_call(), 2)
call_11465 = relay.TupleGetItem(func_10863_call(), 2)
output = relay.Tuple([call_11454,call_11460,call_11462,call_11464,])
output2 = relay.Tuple([call_11455,call_11461,call_11463,call_11465,])
func_11469 = relay.Function([], output)
mod['func_11469'] = func_11469
mod = relay.transform.InferType()(mod)
output = func_11469()
func_11470 = relay.Function([], output)
mutated_mod['func_11470'] = func_11470
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4908_call = mod.get_global_var('func_4908')
func_4910_call = mutated_mod.get_global_var('func_4910')
call_11500 = relay.TupleGetItem(func_4908_call(), 0)
call_11501 = relay.TupleGetItem(func_4910_call(), 0)
output = relay.Tuple([call_11500,])
output2 = relay.Tuple([call_11501,])
func_11517 = relay.Function([], output)
mod['func_11517'] = func_11517
mod = relay.transform.InferType()(mod)
output = func_11517()
func_11518 = relay.Function([], output)
mutated_mod['func_11518'] = func_11518
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4581_call = mod.get_global_var('func_4581')
func_4582_call = mutated_mod.get_global_var('func_4582')
call_11519 = relay.TupleGetItem(func_4581_call(), 0)
call_11520 = relay.TupleGetItem(func_4582_call(), 0)
func_6683_call = mod.get_global_var('func_6683')
func_6686_call = mutated_mod.get_global_var('func_6686')
var_11535 = relay.var("var_11535", dtype = "float32", shape = (18,))#candidate|11535|(18,)|var|float32
call_11534 = relay.TupleGetItem(func_6683_call(relay.reshape(var_11535.astype('float32'), [2, 9, 1])), 1)
call_11536 = relay.TupleGetItem(func_6686_call(relay.reshape(var_11535.astype('float32'), [2, 9, 1])), 1)
output = relay.Tuple([call_11519,call_11534,var_11535,])
output2 = relay.Tuple([call_11520,call_11536,var_11535,])
func_11551 = relay.Function([var_11535,], output)
mod['func_11551'] = func_11551
mod = relay.transform.InferType()(mod)
var_11552 = relay.var("var_11552", dtype = "float32", shape = (18,))#candidate|11552|(18,)|var|float32
output = func_11551(var_11552)
func_11553 = relay.Function([var_11552], output)
mutated_mod['func_11553'] = func_11553
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8267_call = mod.get_global_var('func_8267')
func_8269_call = mutated_mod.get_global_var('func_8269')
call_11576 = relay.TupleGetItem(func_8267_call(), 0)
call_11577 = relay.TupleGetItem(func_8269_call(), 0)
output = call_11576
output2 = call_11577
func_11578 = relay.Function([], output)
mod['func_11578'] = func_11578
mod = relay.transform.InferType()(mod)
mutated_mod['func_11578'] = func_11578
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11578_call = mutated_mod.get_global_var('func_11578')
call_11579 = func_11578_call()
output = call_11579
func_11580 = relay.Function([], output)
mutated_mod['func_11580'] = func_11580
mutated_mod = relay.transform.InferType()(mutated_mod)
const_11584 = relay.const([[[-0.525596,7.380992,-1.411761,-5.316337,-8.663105,-7.941610],[-9.963483,2.469330,6.144298,6.633244,-2.803940,-1.523205],[1.335343,-4.937516,7.040374,8.986118,-8.110261,-5.334497],[7.692842,7.922730,-1.982569,1.388462,-1.510856,7.879543],[-2.567927,-3.559933,4.443956,-8.063590,-5.779991,-8.898202],[-1.899011,3.248203,-5.356666,7.658589,-0.135643,-7.038162],[-3.684643,-1.743162,-5.303953,-0.533356,-5.811850,8.744807],[6.182587,-0.459620,-9.203389,9.017214,-0.849418,-4.615242],[2.428282,9.659603,-4.295086,-1.852970,9.066041,0.848289],[-0.284307,-9.721374,3.867478,-1.173438,2.027825,-2.459725],[6.136864,-5.650111,-4.513415,0.577770,-0.565975,-0.678543],[-2.384121,6.405134,7.613405,8.031317,-7.409028,-6.289657],[4.402044,5.921000,-6.930233,-3.774729,3.796926,1.090595],[0.163047,5.975742,9.948285,-8.516899,-4.356546,-7.473854],[2.743386,-9.781043,4.535008,3.851370,9.937068,-5.301241],[-7.861074,-0.379583,6.178877,8.352755,-5.048776,7.162755]],[[-4.146977,5.216481,5.446286,-3.911081,7.751518,8.386875],[-6.534898,2.100580,1.767422,3.228710,-5.027449,0.443429],[0.771072,7.439508,-8.281802,-1.604628,-0.155777,1.179007],[5.429727,-6.714263,-6.704874,8.671422,-6.573113,8.367678],[-2.616471,0.170666,-6.423668,2.928758,-6.612401,9.704543],[6.487415,4.248184,6.796286,0.633474,7.507501,1.881779],[0.322048,-8.524340,8.453028,6.191733,-2.075239,-3.638309],[-3.310750,-1.695946,-6.207597,9.939811,5.029779,-6.719269],[4.905989,6.264020,0.442377,3.120157,-0.291674,7.460231],[1.687097,4.985586,9.732960,-0.834772,6.782934,-3.421677],[-6.149315,5.209233,2.439636,-7.402770,-9.192202,5.270599],[-0.478175,-0.685603,-3.356431,-2.669408,3.988952,2.902241],[5.232541,-9.327151,-6.354850,4.767491,-2.272744,3.726024],[-7.947666,-6.843058,3.904594,-3.376637,-9.816737,-2.557109],[-5.667832,-5.054289,1.224991,2.184408,9.509542,5.161272],[-4.159028,-1.547876,-3.446919,-4.845785,7.700412,2.370011]],[[-3.477919,-5.338100,-8.303092,1.573190,3.544599,-3.782271],[2.343786,-0.297396,5.365786,2.116448,-4.660116,-0.036007],[5.477346,5.464696,-0.832898,9.026309,-8.296868,7.385696],[3.700704,-8.901321,9.134236,3.033366,-0.028444,8.191004],[1.117959,6.327969,1.288456,-4.978569,2.252101,7.620567],[-3.514606,-3.308362,7.180599,-7.792129,2.639972,1.411783],[3.354922,6.679310,-8.481501,-1.034410,6.603051,7.553813],[6.341672,8.003187,7.233584,-5.116111,-8.663954,2.190272],[4.939870,-5.105631,-6.411394,7.308537,-5.257300,5.521779],[2.596188,-3.532430,4.479776,2.037282,-9.453643,8.654991],[-9.013988,5.094346,3.023919,-9.002653,-3.025867,9.250385],[-2.009053,8.897214,3.908182,-9.681862,-2.054691,-7.152483],[-4.049456,-7.578292,-5.581108,4.738470,-8.516241,2.283072],[0.401265,-5.749171,-9.222325,-8.780081,-0.471916,0.682067],[-5.740212,-3.675558,9.469062,-4.289857,8.294560,-1.228798],[5.183570,-8.108708,-6.672094,8.151205,6.809463,-6.597619]]], dtype = "float64")#candidate|11584|(3, 16, 6)|const|float64
uop_11585 = relay.erf(const_11584.astype('float64')) # shape=(3, 16, 6)
output = relay.Tuple([uop_11585,])
output2 = relay.Tuple([uop_11585,])
func_11587 = relay.Function([], output)
mod['func_11587'] = func_11587
mod = relay.transform.InferType()(mod)
mutated_mod['func_11587'] = func_11587
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11587_call = mutated_mod.get_global_var('func_11587')
call_11588 = func_11587_call()
output = call_11588
func_11589 = relay.Function([], output)
mutated_mod['func_11589'] = func_11589
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8886_call = mod.get_global_var('func_8886')
func_8888_call = mutated_mod.get_global_var('func_8888')
call_11593 = relay.TupleGetItem(func_8886_call(), 0)
call_11594 = relay.TupleGetItem(func_8888_call(), 0)
func_5312_call = mod.get_global_var('func_5312')
func_5315_call = mutated_mod.get_global_var('func_5315')
const_11604 = relay.const(8.335981, dtype = "float32")#candidate|11604|()|const|float32
const_11605 = relay.const([-9,-10,-10,-1,5,2,-8,-8,-2,-7,-4,-7,8,6,-5,1,-4,1,5,10,-5,7,5,-6,-2,7,7,-9,-10,-6,8,9,8,7,9,-3,-8,-8,6,1,-6,-5,4,9,1,-9,3,-10,-7,4,2,2,8,4,5,-3,4,5,-2,-2,-10,-9,-10,-1,5,4,-5,-7,8,6,-9,-4,6,10,4,10,-6,4,-7,-4,-2,-10,-7,-9,-10,-8,-3,1,2,5,5,9,-4,9,7,6,4,-6,4,-5,10,3,-10,1,6,-7,1,4,8,-9,-7,-6,-10,1,8,8,1,-1,6,2,-8,-6,-6,8,-4,-1,-3,-1,9,-7,-9,-7,8,3,10,7,8,-8,-4,10,-5,-8,-8,-9,2,-6,-3,-1,-10,7,2,7,7,-4,-4,-6,3,-5,-4,8,4,-5,6,10,-2,6,-8,4,10,6,-2,3,8,-8,4,-6,-9,-7,-1,-3,-1,7,-9,7,-8,-3,7,8,6,6,10,-10,7,8,-4,10,-7,9,9,7,-8,10,8,1,-1,-6,2,-2,5,8,-10,-7,7,-2,1,-4,2,6,-1,6,5,3,-9,-6,-6,6,-3,2,6,-6,5,-7,5,9,-10,6,-8,-3,-5,-3,-5,6,9,-10,3,-3,-6,-7,6,7,-2,1,3,7,7,10,9,2,5,3,5,-6,8,4,-9,10,-3,1,9,3,-8,-7,-8,-4,-8,10,-5,-6,2,-9,-10,-4,3,6,-3,-7,-1,-9,3,3,10,-7,-4,2,-3,-8,-1,6,6,-6,-3,2,-9,-5,2,-4,-3,-1,-3,2,-3,1,-3,-10,10,-9,-10,7,2,2,1,-8,8,-1,2,9,6,-3,-8,7,10,-1,5,-2,9,10,-1,-4,10,9,1,-1,-9,-3,7,3,3,10,1,6,-9,9,7,-8,-9,10,5,4,-6,-1,6,-10,9,9,-3,9,1,1,-1,6,-8,-9,-8,6,-1,-6,-2,-8,-8,10,-1,-3,-9,10,-5,-2,-5,-5,4,-8,10,-4,10,-3,8,-10,-4,-3,1,-5,-2,-7,-5,-9,-6,8,10,-10,3,-1,-9,-1,-7,-8,-8,3,7,6,-4,5,-3,-8,4,-5,3,7,6,7,-4,2,-7,1,-6,-7,3,2,2,7,10,-2,-8,5,1,-7,-6,-5,3,6,-5,2,5,-2,-6,5,-2,10,-8,-4,-8,1,2,-6,4,-6,7,6,2,8,-8,-3,-10,2,10,4,-9,-2,3,-9,2,-7,-3,-10,3,-2,-1,-5,10,10,3,7,-10,-6,9,-1,9,9,-3,7,-8,-10,6,1,-1,5,6,-8,1,9,-7,10,-10,-10,-9,-10,-7,-6,-4,-10,-10,10,7,10,2,-9,-2,7,-7,7,-5,2,5,-7,-7,-5,2,-2,-3,-10,-4,4,-5,9,9,1,-3,7,3,9,1,-8,9,-5,-2,5,-1,5,-1,1,10,-5,-4,-3,8,-8,5,-5,8,7,2,-8,-3,10,-7,4,-2,-2,-3,3,6,4,9,-8,-7,7,-6,-4,-9,-5,-5,6,9,-2,-5,-6,8,4,7,-6,-4,-6,9,-1,4,3,-6,5,-6,-8,5,4,3,-3,-8,9,-2,-6,4,-7,5,8,-10,-5,-1,9,-8,-9,9,-5,3,-2,-10,-5,-8,-5,-4,-4,-5,1,3,-1,-1,6,-4,-8,7,-9,-8,1,7,-9,-8,-5,2,-6,6,-8,8,8,6,-9,5,8,-4,-9,7,-4,-3,-6,5,-1,-9,-9,-4,-1,2,-3,-7,2,2,-2,1,3,-5,10,3,2,-2,-1,7,-9,9,7,5,-7,1,5,5,6,9,9,-7,3,3,8,-5,10,10,-2,-5,1,8,7,-8,-3,-1,8,-5,-9,-7,8,-5,8,6,-2,10,-8,-1,-2,-2,-5,-9,-10,4,-3,-6,4,1,-9,-3,1,-4,4,6,6,2,10,4,6,-9,10,-3,-9,8,3,-8,-7,-3,-2,6,8,9,9,-8,-3,7,-2,-2,5,8,-3,4,3,-2,6,-2,8,-2,7,6,-7,-7,-3,10,9,8,6,-4,9,3,4,2,9,10,2,-7,-9,7,-1,2,7,-2,3,-2,-1,-10,2,-6,-3,-6,2,-5,-6,-3,-1,9,-4,-1,-8,-7,-7,6,8,10,-8,-6,8,1,6,-4,-6,5,5,-7,8,-2,3,-4,-9,10,-1,-2,-10,4,7,-10,-1,5,10,1,-7,3,-10,-9,-3,10,7,-2,7,2,-6,-8,-9,4,-8], dtype = "uint16")#candidate|11605|(864,)|const|uint16
call_11603 = relay.TupleGetItem(func_5312_call(relay.reshape(const_11604.astype('float32'), []), relay.reshape(const_11605.astype('uint16'), [864,]), ), 4)
call_11606 = relay.TupleGetItem(func_5315_call(relay.reshape(const_11604.astype('float32'), []), relay.reshape(const_11605.astype('uint16'), [864,]), ), 4)
output = relay.Tuple([call_11593,call_11603,const_11604,const_11605,])
output2 = relay.Tuple([call_11594,call_11606,const_11604,const_11605,])
func_11610 = relay.Function([], output)
mod['func_11610'] = func_11610
mod = relay.transform.InferType()(mod)
mutated_mod['func_11610'] = func_11610
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11610_call = mutated_mod.get_global_var('func_11610')
call_11611 = func_11610_call()
output = call_11611
func_11612 = relay.Function([], output)
mutated_mod['func_11612'] = func_11612
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6119_call = mod.get_global_var('func_6119')
func_6120_call = mutated_mod.get_global_var('func_6120')
call_11616 = relay.TupleGetItem(func_6119_call(), 2)
call_11617 = relay.TupleGetItem(func_6120_call(), 2)
func_5336_call = mod.get_global_var('func_5336')
func_5337_call = mutated_mod.get_global_var('func_5337')
call_11618 = relay.TupleGetItem(func_5336_call(), 0)
call_11619 = relay.TupleGetItem(func_5337_call(), 0)
output = relay.Tuple([call_11616,call_11618,])
output2 = relay.Tuple([call_11617,call_11619,])
func_11623 = relay.Function([], output)
mod['func_11623'] = func_11623
mod = relay.transform.InferType()(mod)
mutated_mod['func_11623'] = func_11623
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11623_call = mutated_mod.get_global_var('func_11623')
call_11624 = func_11623_call()
output = call_11624
func_11625 = relay.Function([], output)
mutated_mod['func_11625'] = func_11625
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11517_call = mod.get_global_var('func_11517')
func_11518_call = mutated_mod.get_global_var('func_11518')
call_11632 = relay.TupleGetItem(func_11517_call(), 0)
call_11633 = relay.TupleGetItem(func_11518_call(), 0)
output = call_11632
output2 = call_11633
func_11640 = relay.Function([], output)
mod['func_11640'] = func_11640
mod = relay.transform.InferType()(mod)
mutated_mod['func_11640'] = func_11640
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11640_call = mutated_mod.get_global_var('func_11640')
call_11641 = func_11640_call()
output = call_11641
func_11642 = relay.Function([], output)
mutated_mod['func_11642'] = func_11642
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5716_call = mod.get_global_var('func_5716')
func_5718_call = mutated_mod.get_global_var('func_5718')
call_11650 = relay.TupleGetItem(func_5716_call(), 0)
call_11651 = relay.TupleGetItem(func_5718_call(), 0)
uop_11652 = relay.sin(call_11650.astype('float64')) # shape=(4, 196)
uop_11654 = relay.sin(call_11651.astype('float64')) # shape=(4, 196)
var_11659 = relay.var("var_11659", dtype = "float64", shape = (4, 196))#candidate|11659|(4, 196)|var|float64
bop_11660 = relay.floor_mod(uop_11652.astype('float64'), relay.reshape(var_11659.astype('float64'), relay.shape_of(uop_11652))) # shape=(4, 196)
bop_11663 = relay.floor_mod(uop_11654.astype('float64'), relay.reshape(var_11659.astype('float64'), relay.shape_of(uop_11654))) # shape=(4, 196)
func_6083_call = mod.get_global_var('func_6083')
func_6085_call = mutated_mod.get_global_var('func_6085')
call_11685 = relay.TupleGetItem(func_6083_call(), 1)
call_11686 = relay.TupleGetItem(func_6085_call(), 1)
uop_11687 = relay.tan(var_11659.astype('float32')) # shape=(4, 196)
output = relay.Tuple([bop_11660,call_11685,uop_11687,])
output2 = relay.Tuple([bop_11663,call_11686,uop_11687,])
func_11694 = relay.Function([var_11659,], output)
mod['func_11694'] = func_11694
mod = relay.transform.InferType()(mod)
var_11695 = relay.var("var_11695", dtype = "float64", shape = (4, 196))#candidate|11695|(4, 196)|var|float64
output = func_11694(var_11695)
func_11696 = relay.Function([var_11695], output)
mutated_mod['func_11696'] = func_11696
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11517_call = mod.get_global_var('func_11517')
func_11518_call = mutated_mod.get_global_var('func_11518')
call_11700 = relay.TupleGetItem(func_11517_call(), 0)
call_11701 = relay.TupleGetItem(func_11518_call(), 0)
output = relay.Tuple([call_11700,])
output2 = relay.Tuple([call_11701,])
func_11735 = relay.Function([], output)
mod['func_11735'] = func_11735
mod = relay.transform.InferType()(mod)
mutated_mod['func_11735'] = func_11735
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11735_call = mutated_mod.get_global_var('func_11735')
call_11736 = func_11735_call()
output = call_11736
func_11737 = relay.Function([], output)
mutated_mod['func_11737'] = func_11737
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8039_call = mod.get_global_var('func_8039')
func_8041_call = mutated_mod.get_global_var('func_8041')
call_11774 = func_8039_call()
call_11775 = func_8039_call()
output = call_11774
output2 = call_11775
func_11788 = relay.Function([], output)
mod['func_11788'] = func_11788
mod = relay.transform.InferType()(mod)
mutated_mod['func_11788'] = func_11788
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11788_call = mutated_mod.get_global_var('func_11788')
call_11789 = func_11788_call()
output = call_11789
func_11790 = relay.Function([], output)
mutated_mod['func_11790'] = func_11790
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6656_call = mod.get_global_var('func_6656')
func_6657_call = mutated_mod.get_global_var('func_6657')
call_11806 = relay.TupleGetItem(func_6656_call(), 0)
call_11807 = relay.TupleGetItem(func_6657_call(), 0)
output = relay.Tuple([call_11806,])
output2 = relay.Tuple([call_11807,])
func_11817 = relay.Function([], output)
mod['func_11817'] = func_11817
mod = relay.transform.InferType()(mod)
output = func_11817()
func_11818 = relay.Function([], output)
mutated_mod['func_11818'] = func_11818
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11906 = relay.var("var_11906", dtype = "float64", shape = (15, 16, 6))#candidate|11906|(15, 16, 6)|var|float64
var_11907 = relay.var("var_11907", dtype = "float64", shape = (15, 16, 6))#candidate|11907|(15, 16, 6)|var|float64
bop_11908 = relay.divide(var_11906.astype('float64'), relay.reshape(var_11907.astype('float64'), relay.shape_of(var_11906))) # shape=(15, 16, 6)
output = bop_11908
output2 = bop_11908
func_11915 = relay.Function([var_11906,var_11907,], output)
mod['func_11915'] = func_11915
mod = relay.transform.InferType()(mod)
var_11916 = relay.var("var_11916", dtype = "float64", shape = (15, 16, 6))#candidate|11916|(15, 16, 6)|var|float64
var_11917 = relay.var("var_11917", dtype = "float64", shape = (15, 16, 6))#candidate|11917|(15, 16, 6)|var|float64
output = func_11915(var_11916,var_11917,)
func_11918 = relay.Function([var_11916,var_11917,], output)
mutated_mod['func_11918'] = func_11918
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9216_call = mod.get_global_var('func_9216')
func_9218_call = mutated_mod.get_global_var('func_9218')
call_11930 = relay.TupleGetItem(func_9216_call(), 0)
call_11931 = relay.TupleGetItem(func_9218_call(), 0)
func_7812_call = mod.get_global_var('func_7812')
func_7813_call = mutated_mod.get_global_var('func_7813')
call_11970 = relay.TupleGetItem(func_7812_call(), 1)
call_11971 = relay.TupleGetItem(func_7813_call(), 1)
func_8886_call = mod.get_global_var('func_8886')
func_8888_call = mutated_mod.get_global_var('func_8888')
call_11972 = relay.TupleGetItem(func_8886_call(), 0)
call_11973 = relay.TupleGetItem(func_8888_call(), 0)
output = relay.Tuple([call_11930,call_11970,call_11972,])
output2 = relay.Tuple([call_11931,call_11971,call_11973,])
func_11984 = relay.Function([], output)
mod['func_11984'] = func_11984
mod = relay.transform.InferType()(mod)
mutated_mod['func_11984'] = func_11984
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11984_call = mutated_mod.get_global_var('func_11984')
call_11985 = func_11984_call()
output = call_11985
func_11986 = relay.Function([], output)
mutated_mod['func_11986'] = func_11986
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6499_call = mod.get_global_var('func_6499')
func_6501_call = mutated_mod.get_global_var('func_6501')
call_12014 = relay.TupleGetItem(func_6499_call(), 3)
call_12015 = relay.TupleGetItem(func_6501_call(), 3)
output = relay.Tuple([call_12014,])
output2 = relay.Tuple([call_12015,])
func_12027 = relay.Function([], output)
mod['func_12027'] = func_12027
mod = relay.transform.InferType()(mod)
mutated_mod['func_12027'] = func_12027
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12027_call = mutated_mod.get_global_var('func_12027')
call_12028 = func_12027_call()
output = call_12028
func_12029 = relay.Function([], output)
mutated_mod['func_12029'] = func_12029
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11578_call = mod.get_global_var('func_11578')
func_11580_call = mutated_mod.get_global_var('func_11580')
call_12045 = func_11578_call()
call_12046 = func_11578_call()
output = call_12045
output2 = call_12046
func_12050 = relay.Function([], output)
mod['func_12050'] = func_12050
mod = relay.transform.InferType()(mod)
mutated_mod['func_12050'] = func_12050
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12050_call = mutated_mod.get_global_var('func_12050')
call_12051 = func_12050_call()
output = call_12051
func_12052 = relay.Function([], output)
mutated_mod['func_12052'] = func_12052
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12078 = relay.var("var_12078", dtype = "uint64", shape = (5, 4, 5))#candidate|12078|(5, 4, 5)|var|uint64
var_12079 = relay.var("var_12079", dtype = "uint64", shape = (5, 4, 5))#candidate|12079|(5, 4, 5)|var|uint64
bop_12080 = relay.logical_xor(var_12078.astype('uint64'), relay.reshape(var_12079.astype('uint64'), relay.shape_of(var_12078))) # shape=(5, 4, 5)
bop_12090 = relay.less(bop_12080.astype('bool'), relay.reshape(var_12079.astype('bool'), relay.shape_of(bop_12080))) # shape=(5, 4, 5)
uop_12099 = relay.sin(bop_12090.astype('float64')) # shape=(5, 4, 5)
func_1019_call = mod.get_global_var('func_1019')
func_1023_call = mutated_mod.get_global_var('func_1023')
const_12104 = relay.const([10,-10,-10,-1,-4,1,2,-3,-2,-9,7,7,-7,-8,-4,3,9,-2,6,4,-8,9,2,6,-2,-8,-8,-5,-9,-8,-10,-7,-6,9,-4,5,-7,3,-6,-3,5,9,6,8,9,-8,-9,-9,6,7,3,4,-4,-9,-8,-9,4,4,-6,-7,8,-3,2,2,-9,10,10,-2,-2,7,5,-3,-7,-9,1,7,1,6,1,-3,-6,-4,10,-5,9,4,-1,3,4,-9,7,-6,-8,-4,-10,-1,2,7,5,4,-5,8,-5,-1,2,-6,8,7,-4,-4,8,3,5,1,3,4,4,-3,4,10,8,6,7,3,-4,8,-4,-3,-2,-9,-10,2,-8,4,10,9,-1,-3,10,-2,3,-8,2,8,-6,10,3,-1,-8,4,-9,8,-9,10,7,6,1,-8,7,-10,6,-8,-3,-1,-2,-1,-9,-2,-9,10,4,7,9,-10,-5,9,10,2,4,4,-8,10,-5,-6,5,-2,9,6,-9,6,7,-5,5,-2,-1,-9,-3,-6,9,5,-5,5,-8,-6,7,1,9,3,-3,5,1,-3,-10,5,1,7,8,-2,1,3,1,-4,-2,-6,-1,-1,2,-9,4,-6,-5,-3,-3,9,-2,-3,-8,3,5,-5,10,-1,1,-7,-3,10,-3,10,7,-1,-4,1,-3,-2,-6,7,4,-8,-7,9,-7,-9,-1,8,8,8,4,-4,6,7,4,7,1,4,-2,1,4,-2,7,-3,-7,-7,-2,10,-4,9,-3,7,-4,4,-3,-5,-5,10,-7,8,-5,7,-3,-5,-3,6,-3,-10,1,-4,10,-9,-8,-8,-5,-9,9,-10,-10,-1,1,1,-8,10,-6,4,-6,3,-4,-9,9,-1,-1,-3,6,-7,9,1,-8,9,-7,-2,-7,-9,9,-2,-3,7,6,6,-1,-10,-1,-10,-4,-5,-3,6,-3,3,-2,-10,-1,-10,4,10,-8,-8,1,-10,-8,-10,3,2,-10,9,1,-6,4,-9,1,-6,2,-2,5,-10,6,-5,-5,-4,-4,-8,10,-7,-9,5,-8,2,6,-2,5,-3,3,7,-4,2,6,3,5,10,-10,5,7,-9,1,-3,5,-7,-3,6,-9,-7,10,9,-4,9,-6,-2,-4,-6,-4,3,-7,8,7,9], dtype = "uint8")#candidate|12104|(432,)|const|uint8
call_12103 = func_1019_call(relay.reshape(const_12104.astype('uint8'), [6, 12, 6]), relay.reshape(const_12104.astype('uint8'), [6, 12, 6]), )
call_12105 = func_1019_call(relay.reshape(const_12104.astype('uint8'), [6, 12, 6]), relay.reshape(const_12104.astype('uint8'), [6, 12, 6]), )
uop_12119 = relay.rsqrt(uop_12099.astype('float32')) # shape=(5, 4, 5)
func_5192_call = mod.get_global_var('func_5192')
func_5193_call = mutated_mod.get_global_var('func_5193')
call_12127 = func_5192_call()
call_12128 = func_5192_call()
output = relay.Tuple([call_12103,const_12104,uop_12119,call_12127,])
output2 = relay.Tuple([call_12105,const_12104,uop_12119,call_12128,])
func_12130 = relay.Function([var_12078,var_12079,], output)
mod['func_12130'] = func_12130
mod = relay.transform.InferType()(mod)
mutated_mod['func_12130'] = func_12130
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12130_call = mutated_mod.get_global_var('func_12130')
var_12132 = relay.var("var_12132", dtype = "uint64", shape = (5, 4, 5))#candidate|12132|(5, 4, 5)|var|uint64
var_12133 = relay.var("var_12133", dtype = "uint64", shape = (5, 4, 5))#candidate|12133|(5, 4, 5)|var|uint64
call_12131 = func_12130_call(var_12132,var_12133,)
output = call_12131
func_12134 = relay.Function([var_12132,var_12133,], output)
mutated_mod['func_12134'] = func_12134
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7360_call = mod.get_global_var('func_7360')
func_7362_call = mutated_mod.get_global_var('func_7362')
call_12154 = relay.TupleGetItem(func_7360_call(), 0)
call_12155 = relay.TupleGetItem(func_7362_call(), 0)
func_9381_call = mod.get_global_var('func_9381')
func_9382_call = mutated_mod.get_global_var('func_9382')
call_12159 = relay.TupleGetItem(func_9381_call(), 0)
call_12160 = relay.TupleGetItem(func_9382_call(), 0)
func_11817_call = mod.get_global_var('func_11817')
func_11818_call = mutated_mod.get_global_var('func_11818')
call_12173 = relay.TupleGetItem(func_11817_call(), 0)
call_12174 = relay.TupleGetItem(func_11818_call(), 0)
func_6656_call = mod.get_global_var('func_6656')
func_6657_call = mutated_mod.get_global_var('func_6657')
call_12178 = relay.TupleGetItem(func_6656_call(), 0)
call_12179 = relay.TupleGetItem(func_6657_call(), 0)
func_3774_call = mod.get_global_var('func_3774')
func_3777_call = mutated_mod.get_global_var('func_3777')
const_12193 = relay.const(False, dtype = "bool")#candidate|12193|()|const|bool
call_12192 = func_3774_call(relay.reshape(const_12193.astype('bool'), []))
call_12194 = func_3774_call(relay.reshape(const_12193.astype('bool'), []))
func_4637_call = mod.get_global_var('func_4637')
func_4638_call = mutated_mod.get_global_var('func_4638')
call_12195 = relay.TupleGetItem(func_4637_call(), 0)
call_12196 = relay.TupleGetItem(func_4638_call(), 0)
func_7360_call = mod.get_global_var('func_7360')
func_7362_call = mutated_mod.get_global_var('func_7362')
call_12200 = relay.TupleGetItem(func_7360_call(), 0)
call_12201 = relay.TupleGetItem(func_7362_call(), 0)
func_8577_call = mod.get_global_var('func_8577')
func_8579_call = mutated_mod.get_global_var('func_8579')
call_12203 = relay.TupleGetItem(func_8577_call(), 3)
call_12204 = relay.TupleGetItem(func_8579_call(), 3)
bop_12222 = relay.mod(call_12195.astype('float64'), relay.reshape(call_12203.astype('float64'), relay.shape_of(call_12195))) # shape=(7, 16, 7)
bop_12225 = relay.mod(call_12196.astype('float64'), relay.reshape(call_12204.astype('float64'), relay.shape_of(call_12196))) # shape=(7, 16, 7)
func_7812_call = mod.get_global_var('func_7812')
func_7813_call = mutated_mod.get_global_var('func_7813')
call_12226 = relay.TupleGetItem(func_7812_call(), 0)
call_12227 = relay.TupleGetItem(func_7813_call(), 0)
func_12027_call = mod.get_global_var('func_12027')
func_12029_call = mutated_mod.get_global_var('func_12029')
call_12233 = relay.TupleGetItem(func_12027_call(), 0)
call_12234 = relay.TupleGetItem(func_12029_call(), 0)
bop_12236 = relay.multiply(call_12159.astype('uint16'), const_12193.astype('uint16')) # shape=(7, 16, 7)
bop_12239 = relay.multiply(call_12160.astype('uint16'), const_12193.astype('uint16')) # shape=(7, 16, 7)
output = relay.Tuple([call_12154,call_12173,call_12178,call_12192,call_12200,bop_12222,call_12226,call_12233,bop_12236,])
output2 = relay.Tuple([call_12155,call_12174,call_12179,call_12194,call_12201,bop_12225,call_12227,call_12234,bop_12239,])
func_12246 = relay.Function([], output)
mod['func_12246'] = func_12246
mod = relay.transform.InferType()(mod)
output = func_12246()
func_12247 = relay.Function([], output)
mutated_mod['func_12247'] = func_12247
mutated_mod = relay.transform.InferType()(mutated_mod)
const_12267 = relay.const(-3, dtype = "int64")#candidate|12267|()|const|int64
var_12268 = relay.var("var_12268", dtype = "int64", shape = (5, 9, 1))#candidate|12268|(5, 9, 1)|var|int64
bop_12269 = relay.bitwise_or(const_12267.astype('int64'), var_12268.astype('int64')) # shape=(5, 9, 1)
output = bop_12269
output2 = bop_12269
func_12272 = relay.Function([var_12268,], output)
mod['func_12272'] = func_12272
mod = relay.transform.InferType()(mod)
var_12273 = relay.var("var_12273", dtype = "int64", shape = (5, 9, 1))#candidate|12273|(5, 9, 1)|var|int64
output = func_12272(var_12273)
func_12274 = relay.Function([var_12273], output)
mutated_mod['func_12274'] = func_12274
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12283 = relay.var("var_12283", dtype = "float32", shape = ())#candidate|12283|()|var|float32
const_12284 = relay.const([[[9.999185,-9.189705,8.111521,-4.411248,-8.578336,3.940244,-5.673916,7.118934]],[[-2.851926,-1.352714,2.422997,-4.596461,-3.711518,0.692144,-8.706611,2.494195]],[[5.957912,4.976765,7.451150,-5.854994,5.192331,-9.482956,-4.037478,-8.484459]],[[-7.978759,-6.615274,0.497817,-7.447299,-0.159392,1.044336,-2.065282,-0.397981]],[[-3.750653,-7.809252,-4.572859,-0.985675,-7.609334,1.881698,-6.465740,2.034864]],[[4.496466,-5.277446,1.159431,-5.054021,-6.839187,-8.309538,5.853997,-4.660593]],[[-0.915579,1.108806,-4.547718,-4.428012,-8.707704,2.581538,6.412679,-5.302747]],[[-7.958275,-3.756214,7.384213,-5.483964,-4.138614,-7.682939,0.331478,2.604320]],[[5.221435,-4.974459,-2.709432,-3.651859,6.710676,-1.136961,6.767824,5.877352]],[[7.827668,1.372555,-1.225088,8.742320,-0.943841,-4.410286,-1.322126,7.363403]],[[-1.004094,6.594932,0.636055,-3.565540,-3.038033,1.676751,9.923985,3.623796]],[[-7.420452,0.717075,-0.860432,6.363417,-2.868984,9.032470,-4.786110,-0.272395]]], dtype = "float32")#candidate|12284|(12, 1, 8)|const|float32
bop_12285 = relay.divide(var_12283.astype('float32'), const_12284.astype('float32')) # shape=(12, 1, 8)
func_11517_call = mod.get_global_var('func_11517')
func_11518_call = mutated_mod.get_global_var('func_11518')
call_12288 = relay.TupleGetItem(func_11517_call(), 0)
call_12289 = relay.TupleGetItem(func_11518_call(), 0)
func_7033_call = mod.get_global_var('func_7033')
func_7035_call = mutated_mod.get_global_var('func_7035')
var_12299 = relay.var("var_12299", dtype = "float32", shape = (550,))#candidate|12299|(550,)|var|float32
call_12298 = relay.TupleGetItem(func_7033_call(relay.reshape(var_12299.astype('float32'), [550,])), 1)
call_12300 = relay.TupleGetItem(func_7035_call(relay.reshape(var_12299.astype('float32'), [550,])), 1)
bop_12309 = relay.subtract(call_12298.astype('uint8'), relay.reshape(var_12299.astype('uint8'), relay.shape_of(call_12298))) # shape=(11, 10, 5)
bop_12312 = relay.subtract(call_12300.astype('uint8'), relay.reshape(var_12299.astype('uint8'), relay.shape_of(call_12300))) # shape=(11, 10, 5)
func_7863_call = mod.get_global_var('func_7863')
func_7865_call = mutated_mod.get_global_var('func_7865')
call_12315 = relay.TupleGetItem(func_7863_call(), 1)
call_12316 = relay.TupleGetItem(func_7865_call(), 1)
output = relay.Tuple([bop_12285,call_12288,bop_12309,call_12315,])
output2 = relay.Tuple([bop_12285,call_12289,bop_12312,call_12316,])
func_12327 = relay.Function([var_12283,var_12299,], output)
mod['func_12327'] = func_12327
mod = relay.transform.InferType()(mod)
var_12328 = relay.var("var_12328", dtype = "float32", shape = ())#candidate|12328|()|var|float32
var_12329 = relay.var("var_12329", dtype = "float32", shape = (550,))#candidate|12329|(550,)|var|float32
output = func_12327(var_12328,var_12329,)
func_12330 = relay.Function([var_12328,var_12329,], output)
mutated_mod['func_12330'] = func_12330
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11623_call = mod.get_global_var('func_11623')
func_11625_call = mutated_mod.get_global_var('func_11625')
call_12371 = relay.TupleGetItem(func_11623_call(), 1)
call_12372 = relay.TupleGetItem(func_11625_call(), 1)
func_5215_call = mod.get_global_var('func_5215')
func_5217_call = mutated_mod.get_global_var('func_5217')
call_12385 = relay.TupleGetItem(func_5215_call(), 0)
call_12386 = relay.TupleGetItem(func_5217_call(), 0)
func_8362_call = mod.get_global_var('func_8362')
func_8364_call = mutated_mod.get_global_var('func_8364')
call_12393 = func_8362_call()
call_12394 = func_8362_call()
output = relay.Tuple([call_12371,call_12385,call_12393,])
output2 = relay.Tuple([call_12372,call_12386,call_12394,])
func_12403 = relay.Function([], output)
mod['func_12403'] = func_12403
mod = relay.transform.InferType()(mod)
output = func_12403()
func_12404 = relay.Function([], output)
mutated_mod['func_12404'] = func_12404
mutated_mod = relay.transform.InferType()(mutated_mod)
const_12419 = relay.const([[[-1.982716,-2.959185,-2.668765,1.733967,-4.421572,3.808072],[-9.458686,-6.954109,6.808610,-2.294662,-4.788976,0.737645],[-3.780816,-4.485014,-5.046230,7.551448,-2.274023,4.008063],[-8.186166,0.345068,8.085221,8.708322,9.613893,4.071079],[8.388696,-3.395947,5.998622,-5.529488,-7.845628,-8.857134],[-5.352866,-4.075377,0.479721,8.657522,-5.256859,-9.195160],[6.434856,9.998100,-8.158504,9.266170,-7.296838,7.580055],[-4.389783,1.820982,-3.487279,8.806705,4.760782,4.092841],[-6.609434,-2.780473,0.253483,-4.040675,-7.095779,6.344634]],[[2.829582,0.519443,-2.694827,0.991589,-6.642436,-8.374228],[-3.404549,2.670044,8.158496,3.176370,-8.533020,-4.326562],[-3.785006,-0.551811,8.891541,7.991570,2.212478,-1.642956],[9.550153,-7.180600,2.377705,7.232461,-4.926179,9.429343],[5.274183,5.724955,6.252397,-7.588354,7.091781,-3.791042],[-3.496087,1.301668,-9.729960,-5.848710,9.972453,9.908073],[5.960534,-4.934168,-8.864817,0.710248,-2.257592,2.669852],[-6.707921,-5.698102,-5.124773,-6.675729,-9.826290,-6.427948],[-3.319425,6.749632,3.301399,-2.618724,9.528149,8.688463]],[[-2.799967,8.918999,5.107955,-4.371431,-5.209932,8.371901],[-2.797195,-2.769352,5.550392,4.090413,2.507331,6.647634],[-3.119110,3.729918,7.310460,0.168788,5.915843,-1.388129],[1.736805,-6.882137,6.901862,-9.221408,-6.074168,2.985825],[-6.282431,8.107276,2.359023,-6.929381,-5.328993,1.184055],[-4.114873,8.637625,8.002862,2.124681,4.832113,3.649740],[2.859132,-4.180810,-4.186170,-1.582223,-3.508729,-5.759790],[-8.977250,1.229219,-8.895658,-1.486802,4.746636,-4.288420],[-9.515971,8.669745,7.141593,-3.022677,2.376226,-4.517367]],[[-1.044785,-1.619383,-8.065571,-3.453909,8.346127,3.659052],[-6.058367,5.594376,-0.495107,1.744465,9.277172,-4.733225],[7.265829,8.389301,5.288771,-3.890115,-5.270489,-8.542819],[4.332731,-5.584984,5.176614,-3.584480,9.147234,0.259591],[4.671308,-8.760068,-9.480319,0.658641,-4.662046,-6.743541],[6.661846,0.581195,2.124280,-4.273905,9.844355,5.526527],[3.735010,-7.818627,3.142327,-0.724827,-0.049639,2.928961],[7.494816,-5.856774,-6.884927,9.800903,0.409958,9.201238],[-3.538632,1.466042,-6.201539,-5.369817,-5.451905,7.749814]],[[7.363271,-7.095064,-8.343780,-8.877225,3.819500,6.188015],[1.516437,3.396218,-7.990680,5.484645,-0.439984,-3.276766],[9.217396,-4.954742,7.689187,-4.505776,3.517846,3.844344],[-9.173325,3.902952,-3.543735,7.421906,7.879181,8.534410],[-8.877622,6.485012,0.694966,0.019819,-9.087999,5.860494],[6.490470,-1.175758,-9.921715,9.496937,4.814482,-2.980997],[9.328979,6.447485,-7.975109,-6.508413,8.437489,-9.655842],[1.585237,-6.524117,2.933694,-3.837449,7.857891,-3.645851],[-8.340998,-0.514149,-3.919905,1.577998,6.327667,4.759121]],[[9.862673,-2.981164,8.630795,-1.453488,-7.037645,-0.579801],[-2.206839,0.682016,-0.212410,7.858477,4.199156,-1.163379],[0.163944,4.335100,4.704012,-1.843632,5.994700,4.184512],[9.558709,4.051957,-5.759706,-8.151415,-8.459322,-5.083409],[9.623835,0.415268,-2.881215,-2.709375,-1.486518,-0.631406],[-8.334562,-9.419319,9.070237,-7.767271,6.930945,-5.848572],[-2.804972,-6.024397,-0.030147,7.941784,3.728064,-7.120245],[-9.735021,6.777902,2.669201,-5.223989,-1.597726,8.700731],[6.782930,6.486319,9.441057,-2.369887,-4.695261,0.719500]],[[-8.052144,-9.315996,6.252108,9.810644,2.944423,-0.863467],[-1.058045,2.276866,-9.119209,-8.066926,-5.541251,-7.812640],[8.971202,5.779904,-8.310317,8.480585,7.633377,-9.273787],[-4.075274,9.436464,-0.813553,-2.672833,-6.134265,7.079294],[-5.683282,-4.914103,0.213649,1.825760,-5.924659,-7.969702],[0.395589,6.660606,3.043498,9.730732,5.495207,-6.844529],[7.249483,-9.719408,-4.883216,-9.479970,3.767394,3.593514],[1.263911,4.111044,-7.757741,-4.273950,8.273431,-8.878017],[3.664804,7.640207,-9.967573,-1.031358,-4.600667,-8.249598]],[[3.035782,-5.838648,0.138788,5.126012,-4.991766,-6.699201],[4.496807,-3.002254,-9.424714,4.873500,-1.575404,-3.989483],[-7.847816,-7.930448,9.137315,7.672067,8.435529,8.708679],[-1.608667,-2.635177,-5.016330,7.221494,3.173616,-0.861753],[-1.489248,-9.642583,-2.115535,-9.720100,3.147416,-7.466652],[9.679038,4.232389,9.640578,1.715949,-7.264740,-7.083214],[6.644340,-0.512607,5.723755,-0.993912,-9.709113,-2.485408],[-6.392884,-5.049214,-3.849216,-0.402576,-9.119733,-5.658276],[2.948869,3.972418,0.946823,-7.746574,6.190965,-0.276557]],[[5.643333,2.460340,0.690475,3.473773,-0.808728,9.645603],[-3.112008,-6.477766,-2.071410,-9.749119,-6.685455,3.368376],[6.828271,-7.011693,-7.308775,8.851177,-4.925187,4.774861],[-6.214626,8.335775,-9.333367,6.039350,-3.573169,-0.137135],[4.167868,-2.223907,-2.103443,4.599395,5.848154,3.994838],[-8.546256,-7.324728,8.514089,-9.847006,-4.811418,-4.495523],[3.697181,4.769635,1.916534,-4.073134,-0.174484,-9.323901],[-5.665481,-9.890439,-6.891610,5.764528,-7.730988,6.702299],[7.079106,1.447103,4.218016,5.511611,-2.847235,-1.744083]],[[-6.800345,-8.142236,-2.293502,2.630509,-5.966367,-4.111648],[3.902572,-5.004404,2.902354,1.136756,7.629778,-2.507015],[-5.207074,7.976764,-4.611209,-6.098454,-7.398303,8.422361],[-9.435040,6.636231,-5.498727,8.632700,3.597964,3.785195],[0.813195,-0.386791,-7.308617,4.148331,-5.233393,4.874305],[-4.974596,7.567670,-8.254620,0.924374,6.572285,9.994267],[2.910899,-6.223554,-6.362423,7.715240,-2.317033,6.731819],[9.491604,-8.564400,7.512393,-2.214889,1.654065,0.996379],[8.276388,-7.213445,1.566121,-0.371441,-9.793240,-7.681914]],[[6.261847,-3.519573,7.201328,-8.643648,-8.624315,-2.972938],[-4.407028,-1.494837,-3.874329,6.632216,-7.435729,-6.015515],[4.574854,-0.594780,2.960265,5.422276,3.776879,5.957395],[7.638137,3.570565,-5.771427,9.120269,-9.776458,-8.460742],[5.224191,-5.516930,-3.100456,-3.055276,-7.998895,3.416833],[3.690599,-3.631867,0.438530,4.783349,5.658789,-9.883715],[-5.339731,-0.664684,1.614277,9.188807,-2.471069,0.926714],[-9.195132,-5.344626,-9.249104,4.731098,-3.816090,-3.869913],[0.978809,-0.901680,-7.943450,-4.684450,0.500243,-7.524899]],[[8.103331,4.500168,3.698374,-6.661644,-1.181918,-9.391252],[4.433202,-6.673771,6.615066,7.419802,-7.612735,5.432047],[-3.080940,2.990011,-8.103192,2.235111,2.022504,4.341952],[3.166092,8.427998,2.402061,-3.669650,0.675827,-4.382957],[-1.198255,5.738571,-4.568825,9.422452,-1.797084,-3.256940],[-1.320297,-8.055984,-9.458788,4.509068,-8.834248,-8.006527],[-3.958566,-8.675401,5.978615,5.145190,-8.466468,3.121107],[3.881465,8.577626,5.684233,8.522835,7.770066,-2.273151],[9.655857,3.509574,-3.355496,3.217714,3.255939,-1.405233]],[[7.776404,-1.584045,-1.688587,-4.927387,-9.907270,4.906031],[9.616395,-8.730445,-4.074296,-8.517614,-7.382922,2.425881],[0.933501,2.230735,-6.124510,-7.091202,9.900956,2.792064],[-2.015813,-3.653285,-6.912680,-6.307398,-7.686596,-7.935358],[3.569247,-7.897070,6.923959,-5.953339,2.074488,3.303760],[7.792415,5.650937,-1.157639,-6.809455,-5.103684,8.790606],[-2.034658,-7.845484,-9.183164,-6.167540,0.643015,1.353138],[-3.669679,-0.764338,-2.007875,-5.707591,7.945550,-4.228220],[-3.656224,-0.678347,3.048963,2.925426,2.927614,-6.600131]],[[9.282940,-6.164489,-4.823787,7.529343,3.392933,-3.881838],[7.246659,-0.890480,-6.588167,-5.467994,3.058029,1.726731],[-5.139799,8.240255,-5.856996,-8.165704,-1.438647,-4.826858],[-7.294988,5.185103,5.975117,9.585843,-0.363966,9.641498],[0.862669,-7.215142,-1.902371,9.248592,-3.080477,4.552286],[8.965732,-5.962015,-8.170910,-7.705957,-9.998794,-9.217742],[9.272324,-0.203534,8.907801,-4.131065,0.009688,-0.510828],[-8.413440,6.205480,-7.660964,2.811297,-0.892953,5.194904],[-0.030477,3.490327,2.042978,0.841122,-4.440748,1.364127]],[[8.801747,-3.990165,-9.311005,6.288353,-2.773644,1.868511],[7.756319,-5.859762,8.252437,-6.605337,9.831708,-0.632665],[6.815395,8.227389,-2.658061,-8.737363,-8.431920,-4.855405],[2.811039,5.632533,-9.633300,-2.810041,6.826609,9.489714],[-6.884023,9.804349,-7.419909,-9.488349,1.652472,5.367105],[-0.041455,8.582222,-2.130708,8.217766,8.139548,3.574760],[-1.186129,4.862277,3.273907,-3.707041,-9.660190,0.555854],[3.038776,6.419135,-5.587351,-6.396434,-6.662368,0.706296],[-6.855781,-0.660560,-8.294397,7.711820,3.622953,-5.848007]]], dtype = "float32")#candidate|12419|(15, 9, 6)|const|float32
uop_12420 = relay.sinh(const_12419.astype('float32')) # shape=(15, 9, 6)
func_10596_call = mod.get_global_var('func_10596')
func_10598_call = mutated_mod.get_global_var('func_10598')
call_12424 = relay.TupleGetItem(func_10596_call(), 3)
call_12425 = relay.TupleGetItem(func_10598_call(), 3)
output = relay.Tuple([uop_12420,call_12424,])
output2 = relay.Tuple([uop_12420,call_12425,])
func_12457 = relay.Function([], output)
mod['func_12457'] = func_12457
mod = relay.transform.InferType()(mod)
mutated_mod['func_12457'] = func_12457
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12457_call = mutated_mod.get_global_var('func_12457')
call_12458 = func_12457_call()
output = call_12458
func_12459 = relay.Function([], output)
mutated_mod['func_12459'] = func_12459
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10198_call = mod.get_global_var('func_10198')
func_10200_call = mutated_mod.get_global_var('func_10200')
call_12516 = func_10198_call()
call_12517 = func_10198_call()
output = call_12516
output2 = call_12517
func_12520 = relay.Function([], output)
mod['func_12520'] = func_12520
mod = relay.transform.InferType()(mod)
output = func_12520()
func_12521 = relay.Function([], output)
mutated_mod['func_12521'] = func_12521
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10335_call = mod.get_global_var('func_10335')
func_10336_call = mutated_mod.get_global_var('func_10336')
call_12534 = relay.TupleGetItem(func_10335_call(), 2)
call_12535 = relay.TupleGetItem(func_10336_call(), 2)
func_6656_call = mod.get_global_var('func_6656')
func_6657_call = mutated_mod.get_global_var('func_6657')
call_12548 = relay.TupleGetItem(func_6656_call(), 0)
call_12549 = relay.TupleGetItem(func_6657_call(), 0)
func_9043_call = mod.get_global_var('func_9043')
func_9045_call = mutated_mod.get_global_var('func_9045')
call_12567 = relay.TupleGetItem(func_9043_call(), 0)
call_12568 = relay.TupleGetItem(func_9045_call(), 0)
output = relay.Tuple([call_12534,call_12548,call_12567,])
output2 = relay.Tuple([call_12535,call_12549,call_12568,])
func_12570 = relay.Function([], output)
mod['func_12570'] = func_12570
mod = relay.transform.InferType()(mod)
mutated_mod['func_12570'] = func_12570
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12570_call = mutated_mod.get_global_var('func_12570')
call_12571 = func_12570_call()
output = call_12571
func_12572 = relay.Function([], output)
mutated_mod['func_12572'] = func_12572
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9632_call = mod.get_global_var('func_9632')
func_9634_call = mutated_mod.get_global_var('func_9634')
call_12649 = relay.TupleGetItem(func_9632_call(), 0)
call_12650 = relay.TupleGetItem(func_9634_call(), 0)
func_7965_call = mod.get_global_var('func_7965')
func_7966_call = mutated_mod.get_global_var('func_7966')
call_12687 = relay.TupleGetItem(func_7965_call(), 0)
call_12688 = relay.TupleGetItem(func_7966_call(), 0)
func_9029_call = mod.get_global_var('func_9029')
func_9031_call = mutated_mod.get_global_var('func_9031')
call_12695 = relay.TupleGetItem(func_9029_call(), 0)
call_12696 = relay.TupleGetItem(func_9031_call(), 0)
output = relay.Tuple([call_12649,call_12687,call_12695,])
output2 = relay.Tuple([call_12650,call_12688,call_12696,])
func_12702 = relay.Function([], output)
mod['func_12702'] = func_12702
mod = relay.transform.InferType()(mod)
mutated_mod['func_12702'] = func_12702
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12702_call = mutated_mod.get_global_var('func_12702')
call_12703 = func_12702_call()
output = call_12703
func_12704 = relay.Function([], output)
mutated_mod['func_12704'] = func_12704
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8039_call = mod.get_global_var('func_8039')
func_8041_call = mutated_mod.get_global_var('func_8041')
call_12705 = func_8039_call()
call_12706 = func_8039_call()
output = call_12705
output2 = call_12706
func_12733 = relay.Function([], output)
mod['func_12733'] = func_12733
mod = relay.transform.InferType()(mod)
mutated_mod['func_12733'] = func_12733
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12733_call = mutated_mod.get_global_var('func_12733')
call_12734 = func_12733_call()
output = call_12734
func_12735 = relay.Function([], output)
mutated_mod['func_12735'] = func_12735
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5774_call = mod.get_global_var('func_5774')
func_5775_call = mutated_mod.get_global_var('func_5775')
call_12816 = relay.TupleGetItem(func_5774_call(), 0)
call_12817 = relay.TupleGetItem(func_5775_call(), 0)
output = call_12816
output2 = call_12817
func_12831 = relay.Function([], output)
mod['func_12831'] = func_12831
mod = relay.transform.InferType()(mod)
mutated_mod['func_12831'] = func_12831
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12831_call = mutated_mod.get_global_var('func_12831')
call_12832 = func_12831_call()
output = call_12832
func_12833 = relay.Function([], output)
mutated_mod['func_12833'] = func_12833
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6991_call = mod.get_global_var('func_6991')
func_6993_call = mutated_mod.get_global_var('func_6993')
call_12866 = func_6991_call()
call_12867 = func_6991_call()
func_5215_call = mod.get_global_var('func_5215')
func_5217_call = mutated_mod.get_global_var('func_5217')
call_12868 = relay.TupleGetItem(func_5215_call(), 0)
call_12869 = relay.TupleGetItem(func_5217_call(), 0)
output = relay.Tuple([call_12866,call_12868,])
output2 = relay.Tuple([call_12867,call_12869,])
func_12881 = relay.Function([], output)
mod['func_12881'] = func_12881
mod = relay.transform.InferType()(mod)
output = func_12881()
func_12882 = relay.Function([], output)
mutated_mod['func_12882'] = func_12882
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8985_call = mod.get_global_var('func_8985')
func_8986_call = mutated_mod.get_global_var('func_8986')
call_12906 = relay.TupleGetItem(func_8985_call(), 0)
call_12907 = relay.TupleGetItem(func_8986_call(), 0)
output = call_12906
output2 = call_12907
func_12908 = relay.Function([], output)
mod['func_12908'] = func_12908
mod = relay.transform.InferType()(mod)
output = func_12908()
func_12909 = relay.Function([], output)
mutated_mod['func_12909'] = func_12909
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12927 = relay.var("var_12927", dtype = "float32", shape = (2, 5, 6))#candidate|12927|(2, 5, 6)|var|float32
uop_12928 = relay.sqrt(var_12927.astype('float32')) # shape=(2, 5, 6)
output = uop_12928
output2 = uop_12928
func_12943 = relay.Function([var_12927,], output)
mod['func_12943'] = func_12943
mod = relay.transform.InferType()(mod)
var_12944 = relay.var("var_12944", dtype = "float32", shape = (2, 5, 6))#candidate|12944|(2, 5, 6)|var|float32
output = func_12943(var_12944)
func_12945 = relay.Function([var_12944], output)
mutated_mod['func_12945'] = func_12945
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12985 = relay.var("var_12985", dtype = "float64", shape = (2, 14, 8))#candidate|12985|(2, 14, 8)|var|float64
uop_12986 = relay.acos(var_12985.astype('float64')) # shape=(2, 14, 8)
var_13000 = relay.var("var_13000", dtype = "float64", shape = (2, 14, 8))#candidate|13000|(2, 14, 8)|var|float64
bop_13001 = relay.add(uop_12986.astype('int16'), relay.reshape(var_13000.astype('int16'), relay.shape_of(uop_12986))) # shape=(2, 14, 8)
uop_13010 = relay.sqrt(var_13000.astype('float64')) # shape=(2, 14, 8)
output = relay.Tuple([bop_13001,uop_13010,])
output2 = relay.Tuple([bop_13001,uop_13010,])
func_13021 = relay.Function([var_12985,var_13000,], output)
mod['func_13021'] = func_13021
mod = relay.transform.InferType()(mod)
var_13022 = relay.var("var_13022", dtype = "float64", shape = (2, 14, 8))#candidate|13022|(2, 14, 8)|var|float64
var_13023 = relay.var("var_13023", dtype = "float64", shape = (2, 14, 8))#candidate|13023|(2, 14, 8)|var|float64
output = func_13021(var_13022,var_13023,)
func_13024 = relay.Function([var_13022,var_13023,], output)
mutated_mod['func_13024'] = func_13024
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7812_call = mod.get_global_var('func_7812')
func_7813_call = mutated_mod.get_global_var('func_7813')
call_13082 = relay.TupleGetItem(func_7812_call(), 0)
call_13083 = relay.TupleGetItem(func_7813_call(), 0)
func_12733_call = mod.get_global_var('func_12733')
func_12735_call = mutated_mod.get_global_var('func_12735')
call_13084 = func_12733_call()
call_13085 = func_12733_call()
output = relay.Tuple([call_13082,call_13084,])
output2 = relay.Tuple([call_13083,call_13085,])
func_13105 = relay.Function([], output)
mod['func_13105'] = func_13105
mod = relay.transform.InferType()(mod)
mutated_mod['func_13105'] = func_13105
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13105_call = mutated_mod.get_global_var('func_13105')
call_13106 = func_13105_call()
output = call_13106
func_13107 = relay.Function([], output)
mutated_mod['func_13107'] = func_13107
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10879_call = mod.get_global_var('func_10879')
func_10881_call = mutated_mod.get_global_var('func_10881')
call_13128 = relay.TupleGetItem(func_10879_call(), 0)
call_13129 = relay.TupleGetItem(func_10881_call(), 0)
var_13140 = relay.var("var_13140", dtype = "float64", shape = (8, 7, 11))#candidate|13140|(8, 7, 11)|var|float64
bop_13141 = relay.minimum(call_13128.astype('uint8'), relay.reshape(var_13140.astype('uint8'), relay.shape_of(call_13128))) # shape=(8, 7, 11)
bop_13144 = relay.minimum(call_13129.astype('uint8'), relay.reshape(var_13140.astype('uint8'), relay.shape_of(call_13129))) # shape=(8, 7, 11)
output = relay.Tuple([bop_13141,])
output2 = relay.Tuple([bop_13144,])
func_13152 = relay.Function([var_13140,], output)
mod['func_13152'] = func_13152
mod = relay.transform.InferType()(mod)
mutated_mod['func_13152'] = func_13152
mutated_mod = relay.transform.InferType()(mutated_mod)
var_13153 = relay.var("var_13153", dtype = "float64", shape = (8, 7, 11))#candidate|13153|(8, 7, 11)|var|float64
func_13152_call = mutated_mod.get_global_var('func_13152')
call_13154 = func_13152_call(var_13153)
output = call_13154
func_13155 = relay.Function([var_13153], output)
mutated_mod['func_13155'] = func_13155
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12403_call = mod.get_global_var('func_12403')
func_12404_call = mutated_mod.get_global_var('func_12404')
call_13226 = relay.TupleGetItem(func_12403_call(), 1)
call_13227 = relay.TupleGetItem(func_12404_call(), 1)
func_11278_call = mod.get_global_var('func_11278')
func_11280_call = mutated_mod.get_global_var('func_11280')
call_13239 = relay.TupleGetItem(func_11278_call(), 0)
call_13240 = relay.TupleGetItem(func_11280_call(), 0)
output = relay.Tuple([call_13226,call_13239,])
output2 = relay.Tuple([call_13227,call_13240,])
func_13244 = relay.Function([], output)
mod['func_13244'] = func_13244
mod = relay.transform.InferType()(mod)
mutated_mod['func_13244'] = func_13244
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13244_call = mutated_mod.get_global_var('func_13244')
call_13245 = func_13244_call()
output = call_13245
func_13246 = relay.Function([], output)
mutated_mod['func_13246'] = func_13246
mutated_mod = relay.transform.InferType()(mutated_mod)
var_13291 = relay.var("var_13291", dtype = "float64", shape = (4, 15, 5))#candidate|13291|(4, 15, 5)|var|float64
uop_13292 = relay.erf(var_13291.astype('float64')) # shape=(4, 15, 5)
bop_13301 = relay.logical_and(uop_13292.astype('bool'), relay.reshape(var_13291.astype('bool'), relay.shape_of(uop_13292))) # shape=(4, 15, 5)
func_12881_call = mod.get_global_var('func_12881')
func_12882_call = mutated_mod.get_global_var('func_12882')
call_13306 = relay.TupleGetItem(func_12881_call(), 1)
call_13307 = relay.TupleGetItem(func_12882_call(), 1)
func_11266_call = mod.get_global_var('func_11266')
func_11269_call = mutated_mod.get_global_var('func_11269')
var_13314 = relay.var("var_13314", dtype = "float32", shape = (1280,))#candidate|13314|(1280,)|var|float32
call_13313 = func_11266_call(relay.reshape(var_13314.astype('float32'), [10, 16, 8]))
call_13315 = func_11266_call(relay.reshape(var_13314.astype('float32'), [10, 16, 8]))
output = relay.Tuple([bop_13301,call_13306,call_13313,var_13314,])
output2 = relay.Tuple([bop_13301,call_13307,call_13315,var_13314,])
func_13318 = relay.Function([var_13291,var_13314,], output)
mod['func_13318'] = func_13318
mod = relay.transform.InferType()(mod)
var_13319 = relay.var("var_13319", dtype = "float64", shape = (4, 15, 5))#candidate|13319|(4, 15, 5)|var|float64
var_13320 = relay.var("var_13320", dtype = "float32", shape = (1280,))#candidate|13320|(1280,)|var|float32
output = func_13318(var_13319,var_13320,)
func_13321 = relay.Function([var_13319,var_13320,], output)
mutated_mod['func_13321'] = func_13321
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5841_call = mod.get_global_var('func_5841')
func_5842_call = mutated_mod.get_global_var('func_5842')
call_13326 = relay.TupleGetItem(func_5841_call(), 0)
call_13327 = relay.TupleGetItem(func_5842_call(), 0)
output = call_13326
output2 = call_13327
func_13342 = relay.Function([], output)
mod['func_13342'] = func_13342
mod = relay.transform.InferType()(mod)
mutated_mod['func_13342'] = func_13342
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13342_call = mutated_mod.get_global_var('func_13342')
call_13343 = func_13342_call()
output = call_13343
func_13344 = relay.Function([], output)
mutated_mod['func_13344'] = func_13344
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5774_call = mod.get_global_var('func_5774')
func_5775_call = mutated_mod.get_global_var('func_5775')
call_13427 = relay.TupleGetItem(func_5774_call(), 0)
call_13428 = relay.TupleGetItem(func_5775_call(), 0)
output = call_13427
output2 = call_13428
func_13466 = relay.Function([], output)
mod['func_13466'] = func_13466
mod = relay.transform.InferType()(mod)
output = func_13466()
func_13467 = relay.Function([], output)
mutated_mod['func_13467'] = func_13467
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6273_call = mod.get_global_var('func_6273')
func_6275_call = mutated_mod.get_global_var('func_6275')
call_13479 = relay.TupleGetItem(func_6273_call(), 0)
call_13480 = relay.TupleGetItem(func_6275_call(), 0)
output = call_13479
output2 = call_13480
func_13485 = relay.Function([], output)
mod['func_13485'] = func_13485
mod = relay.transform.InferType()(mod)
mutated_mod['func_13485'] = func_13485
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13485_call = mutated_mod.get_global_var('func_13485')
call_13486 = func_13485_call()
output = call_13486
func_13487 = relay.Function([], output)
mutated_mod['func_13487'] = func_13487
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5716_call = mod.get_global_var('func_5716')
func_5718_call = mutated_mod.get_global_var('func_5718')
call_13517 = relay.TupleGetItem(func_5716_call(), 0)
call_13518 = relay.TupleGetItem(func_5718_call(), 0)
uop_13538 = relay.asinh(call_13517.astype('float64')) # shape=(4, 196)
uop_13540 = relay.asinh(call_13518.astype('float64')) # shape=(4, 196)
uop_13541 = relay.exp(uop_13538.astype('float64')) # shape=(4, 196)
uop_13543 = relay.exp(uop_13540.astype('float64')) # shape=(4, 196)
func_9757_call = mod.get_global_var('func_9757')
func_9759_call = mutated_mod.get_global_var('func_9759')
var_13547 = relay.var("var_13547", dtype = "uint16", shape = (168,))#candidate|13547|(168,)|var|uint16
call_13546 = relay.TupleGetItem(func_9757_call(relay.reshape(var_13547.astype('uint16'), [14, 12, 1])), 1)
call_13548 = relay.TupleGetItem(func_9759_call(relay.reshape(var_13547.astype('uint16'), [14, 12, 1])), 1)
output = relay.Tuple([uop_13541,call_13546,var_13547,])
output2 = relay.Tuple([uop_13543,call_13548,var_13547,])
func_13549 = relay.Function([var_13547,], output)
mod['func_13549'] = func_13549
mod = relay.transform.InferType()(mod)
mutated_mod['func_13549'] = func_13549
mutated_mod = relay.transform.InferType()(mutated_mod)
var_13550 = relay.var("var_13550", dtype = "uint16", shape = (168,))#candidate|13550|(168,)|var|uint16
func_13549_call = mutated_mod.get_global_var('func_13549')
call_13551 = func_13549_call(var_13550)
output = call_13551
func_13552 = relay.Function([var_13550], output)
mutated_mod['func_13552'] = func_13552
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6896_call = mod.get_global_var('func_6896')
func_6898_call = mutated_mod.get_global_var('func_6898')
call_13658 = func_6896_call()
call_13659 = func_6896_call()
output = relay.Tuple([call_13658,])
output2 = relay.Tuple([call_13659,])
func_13665 = relay.Function([], output)
mod['func_13665'] = func_13665
mod = relay.transform.InferType()(mod)
output = func_13665()
func_13666 = relay.Function([], output)
mutated_mod['func_13666'] = func_13666
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13665_call = mod.get_global_var('func_13665')
func_13666_call = mutated_mod.get_global_var('func_13666')
call_13699 = relay.TupleGetItem(func_13665_call(), 0)
call_13700 = relay.TupleGetItem(func_13666_call(), 0)
output = relay.Tuple([call_13699,])
output2 = relay.Tuple([call_13700,])
func_13706 = relay.Function([], output)
mod['func_13706'] = func_13706
mod = relay.transform.InferType()(mod)
mutated_mod['func_13706'] = func_13706
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13706_call = mutated_mod.get_global_var('func_13706')
call_13707 = func_13706_call()
output = call_13707
func_13708 = relay.Function([], output)
mutated_mod['func_13708'] = func_13708
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7985_call = mod.get_global_var('func_7985')
func_7987_call = mutated_mod.get_global_var('func_7987')
call_13780 = relay.TupleGetItem(func_7985_call(), 0)
call_13781 = relay.TupleGetItem(func_7987_call(), 0)
func_7476_call = mod.get_global_var('func_7476')
func_7480_call = mutated_mod.get_global_var('func_7480')
const_13783 = relay.const([1,4,4,-4,-3,6,4,3,1,1,-8,3,-7,-5,-5,2,-2,9,-6,9,-6,7,3,1,5,-9,-6,5,7,6,-2,7,-5,-2,-9,-2,-7,4,8,3,-9,4,-5,1,-3,-1,5,9,-6,1,-1,10,-2,10,-2,-3,5,10,-8,-9,10,-6,-2,5,7,3,8,7,-10,8,-2,-6,-8,-7,7,-9,-8,2,-9,9,-10,3,-6,8,9,-9,-6,-8,-3,-5], dtype = "int8")#candidate|13783|(90,)|const|int8
var_13784 = relay.var("var_13784", dtype = "int8", shape = (180,))#candidate|13784|(180,)|var|int8
call_13782 = relay.TupleGetItem(func_7476_call(relay.reshape(call_13780.astype('float64'), [7, 16, 7]), relay.reshape(const_13783.astype('int8'), [90,]), relay.reshape(var_13784.astype('int8'), [180,]), ), 5)
call_13785 = relay.TupleGetItem(func_7480_call(relay.reshape(call_13780.astype('float64'), [7, 16, 7]), relay.reshape(const_13783.astype('int8'), [90,]), relay.reshape(var_13784.astype('int8'), [180,]), ), 5)
func_11735_call = mod.get_global_var('func_11735')
func_11737_call = mutated_mod.get_global_var('func_11737')
call_13786 = relay.TupleGetItem(func_11735_call(), 0)
call_13787 = relay.TupleGetItem(func_11737_call(), 0)
func_8936_call = mod.get_global_var('func_8936')
func_8940_call = mutated_mod.get_global_var('func_8940')
const_13789 = relay.const([[-9.372197,0.764775,-4.696091],[6.315704,-9.689161,4.031015],[-7.409306,-1.246830,-4.226556]], dtype = "float32")#candidate|13789|(3, 3)|const|float32
call_13788 = relay.TupleGetItem(func_8936_call(relay.reshape(const_13789.astype('float32'), [9, 1]), relay.reshape(call_13782.astype('uint8'), [432,]), ), 1)
call_13790 = relay.TupleGetItem(func_8940_call(relay.reshape(const_13789.astype('float32'), [9, 1]), relay.reshape(call_13782.astype('uint8'), [432,]), ), 1)
output = relay.Tuple([call_13780,call_13782,const_13783,var_13784,call_13786,call_13788,const_13789,])
output2 = relay.Tuple([call_13781,call_13785,const_13783,var_13784,call_13787,call_13790,const_13789,])
func_13802 = relay.Function([var_13784,], output)
mod['func_13802'] = func_13802
mod = relay.transform.InferType()(mod)
var_13803 = relay.var("var_13803", dtype = "int8", shape = (180,))#candidate|13803|(180,)|var|int8
output = func_13802(var_13803)
func_13804 = relay.Function([var_13803], output)
mutated_mod['func_13804'] = func_13804
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5192_call = mod.get_global_var('func_5192')
func_5193_call = mutated_mod.get_global_var('func_5193')
call_13821 = func_5192_call()
call_13822 = func_5192_call()
func_13706_call = mod.get_global_var('func_13706')
func_13708_call = mutated_mod.get_global_var('func_13708')
call_13827 = relay.TupleGetItem(func_13706_call(), 0)
call_13828 = relay.TupleGetItem(func_13708_call(), 0)
func_8133_call = mod.get_global_var('func_8133')
func_8134_call = mutated_mod.get_global_var('func_8134')
call_13835 = relay.TupleGetItem(func_8133_call(), 2)
call_13836 = relay.TupleGetItem(func_8134_call(), 2)
func_4637_call = mod.get_global_var('func_4637')
func_4638_call = mutated_mod.get_global_var('func_4638')
call_13860 = relay.TupleGetItem(func_4637_call(), 0)
call_13861 = relay.TupleGetItem(func_4638_call(), 0)
output = relay.Tuple([call_13821,call_13827,call_13835,call_13860,])
output2 = relay.Tuple([call_13822,call_13828,call_13836,call_13861,])
func_13863 = relay.Function([], output)
mod['func_13863'] = func_13863
mod = relay.transform.InferType()(mod)
output = func_13863()
func_13864 = relay.Function([], output)
mutated_mod['func_13864'] = func_13864
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11278_call = mod.get_global_var('func_11278')
func_11280_call = mutated_mod.get_global_var('func_11280')
call_13872 = relay.TupleGetItem(func_11278_call(), 0)
call_13873 = relay.TupleGetItem(func_11280_call(), 0)
func_9557_call = mod.get_global_var('func_9557')
func_9559_call = mutated_mod.get_global_var('func_9559')
call_13886 = func_9557_call()
call_13887 = func_9557_call()
output = relay.Tuple([call_13872,call_13886,])
output2 = relay.Tuple([call_13873,call_13887,])
func_13905 = relay.Function([], output)
mod['func_13905'] = func_13905
mod = relay.transform.InferType()(mod)
output = func_13905()
func_13906 = relay.Function([], output)
mutated_mod['func_13906'] = func_13906
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6529_call = mod.get_global_var('func_6529')
func_6531_call = mutated_mod.get_global_var('func_6531')
call_13918 = relay.TupleGetItem(func_6529_call(), 0)
call_13919 = relay.TupleGetItem(func_6531_call(), 0)
func_11587_call = mod.get_global_var('func_11587')
func_11589_call = mutated_mod.get_global_var('func_11589')
call_13983 = relay.TupleGetItem(func_11587_call(), 0)
call_13984 = relay.TupleGetItem(func_11589_call(), 0)
output = relay.Tuple([call_13918,call_13983,])
output2 = relay.Tuple([call_13919,call_13984,])
func_13986 = relay.Function([], output)
mod['func_13986'] = func_13986
mod = relay.transform.InferType()(mod)
mutated_mod['func_13986'] = func_13986
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13986_call = mutated_mod.get_global_var('func_13986')
call_13987 = func_13986_call()
output = call_13987
func_13988 = relay.Function([], output)
mutated_mod['func_13988'] = func_13988
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9104_call = mod.get_global_var('func_9104')
func_9105_call = mutated_mod.get_global_var('func_9105')
call_14062 = relay.TupleGetItem(func_9104_call(), 0)
call_14063 = relay.TupleGetItem(func_9105_call(), 0)
func_10596_call = mod.get_global_var('func_10596')
func_10598_call = mutated_mod.get_global_var('func_10598')
call_14066 = relay.TupleGetItem(func_10596_call(), 0)
call_14067 = relay.TupleGetItem(func_10598_call(), 0)
uop_14071 = relay.atanh(call_14062.astype('float64')) # shape=(7, 16, 7)
uop_14073 = relay.atanh(call_14063.astype('float64')) # shape=(7, 16, 7)
func_1019_call = mod.get_global_var('func_1019')
func_1023_call = mutated_mod.get_global_var('func_1023')
var_14081 = relay.var("var_14081", dtype = "uint8", shape = (432,))#candidate|14081|(432,)|var|uint8
call_14080 = func_1019_call(relay.reshape(var_14081.astype('uint8'), [6, 12, 6]), relay.reshape(var_14081.astype('uint8'), [6, 12, 6]), )
call_14082 = func_1019_call(relay.reshape(var_14081.astype('uint8'), [6, 12, 6]), relay.reshape(var_14081.astype('uint8'), [6, 12, 6]), )
output = relay.Tuple([call_14066,uop_14071,call_14080,var_14081,])
output2 = relay.Tuple([call_14067,uop_14073,call_14082,var_14081,])
func_14108 = relay.Function([var_14081,], output)
mod['func_14108'] = func_14108
mod = relay.transform.InferType()(mod)
mutated_mod['func_14108'] = func_14108
mutated_mod = relay.transform.InferType()(mutated_mod)
var_14109 = relay.var("var_14109", dtype = "uint8", shape = (432,))#candidate|14109|(432,)|var|uint8
func_14108_call = mutated_mod.get_global_var('func_14108')
call_14110 = func_14108_call(var_14109)
output = call_14110
func_14111 = relay.Function([var_14109], output)
mutated_mod['func_14111'] = func_14111
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8182_call = mod.get_global_var('func_8182')
func_8183_call = mutated_mod.get_global_var('func_8183')
call_14117 = func_8182_call()
call_14118 = func_8182_call()
output = relay.Tuple([call_14117,])
output2 = relay.Tuple([call_14118,])
func_14119 = relay.Function([], output)
mod['func_14119'] = func_14119
mod = relay.transform.InferType()(mod)
mutated_mod['func_14119'] = func_14119
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14119_call = mutated_mod.get_global_var('func_14119')
call_14120 = func_14119_call()
output = call_14120
func_14121 = relay.Function([], output)
mutated_mod['func_14121'] = func_14121
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8182_call = mod.get_global_var('func_8182')
func_8183_call = mutated_mod.get_global_var('func_8183')
call_14194 = func_8182_call()
call_14195 = func_8182_call()
func_13802_call = mod.get_global_var('func_13802')
func_13804_call = mutated_mod.get_global_var('func_13804')
const_14219 = relay.const([[-1],[5],[3],[-6],[-8],[9],[9],[-1],[-9],[2],[8],[-3],[5],[-2],[-5],[9],[-3],[-6],[10],[1],[-4],[-7],[6],[-5],[-7],[-8],[-2],[-9],[-2],[9],[-1],[-7],[-5],[-3],[4],[-2],[-6],[1],[-9],[4],[5],[8],[-4],[-4],[7],[-6],[-4],[-3],[6],[3],[-1],[6],[7],[9],[4],[-9],[-7],[6],[-5],[-10],[6],[3],[8],[10],[-3],[4],[9],[1],[-7],[-2],[-4],[-10],[10],[-6],[6],[7],[1],[1],[-5],[5],[-3],[4],[-1],[8],[5],[-9],[-10],[2],[4],[-5],[4],[-2],[2],[-8],[4],[7],[-2],[-9],[-5],[-1],[6],[-1],[-10],[8],[-3],[-6],[-5],[-1],[2],[3],[3],[-1],[-10],[10],[-9],[6],[-2],[4],[2],[-9],[5],[9],[4],[4],[-1],[1],[-9],[-3],[-7],[6],[5],[-1],[-1],[-10],[-9],[5],[4],[1],[-7],[-5],[-5],[4],[-3],[5],[-9],[3],[-3],[10],[1],[6],[-9],[-3],[6],[-3],[10],[1],[6],[-1],[2],[8],[7],[5],[8],[-5],[-7],[1],[1],[-1],[10],[7],[-3],[9],[-4],[8],[-6],[-9],[-10],[6],[-2],[-8]], dtype = "int8")#candidate|14219|(180, 1)|const|int8
call_14218 = relay.TupleGetItem(func_13802_call(relay.reshape(const_14219.astype('int8'), [180,])), 3)
call_14220 = relay.TupleGetItem(func_13804_call(relay.reshape(const_14219.astype('int8'), [180,])), 3)
func_10861_call = mod.get_global_var('func_10861')
func_10863_call = mutated_mod.get_global_var('func_10863')
call_14227 = relay.TupleGetItem(func_10861_call(), 1)
call_14228 = relay.TupleGetItem(func_10863_call(), 1)
output = relay.Tuple([call_14194,call_14218,const_14219,call_14227,])
output2 = relay.Tuple([call_14195,call_14220,const_14219,call_14228,])
func_14243 = relay.Function([], output)
mod['func_14243'] = func_14243
mod = relay.transform.InferType()(mod)
output = func_14243()
func_14244 = relay.Function([], output)
mutated_mod['func_14244'] = func_14244
mutated_mod = relay.transform.InferType()(mutated_mod)
const_14269 = relay.const([[[-8.252040,-4.495142,5.980887,7.138529],[-4.755071,-6.536750,7.744790,1.888156],[-0.475997,-0.621682,-2.751509,-8.042743],[0.699934,-0.297262,-3.018726,5.640207],[4.506457,-6.498307,-6.085361,8.850424],[9.656913,-4.072901,-4.015786,-7.129327],[8.053073,0.679456,7.656731,-4.303458],[-3.451322,-3.523435,-9.827179,-4.614964],[6.511982,-4.783481,-4.432532,-2.190179],[-3.514236,-5.659474,3.847835,1.840688],[5.505770,-2.845238,-0.936229,7.269383],[1.129587,4.122508,8.802976,7.366997],[-0.849809,7.585825,9.246229,-2.976446],[-6.052257,-7.703062,4.451417,4.836555]],[[2.013798,8.237682,-7.577567,-4.130889],[-6.892751,-9.953172,5.158514,-3.962650],[7.571644,-4.856079,-4.752041,-6.584340],[3.406499,-0.432922,-6.884662,5.816861],[9.029055,-1.575867,7.238818,-0.963111],[-6.954020,-1.264393,-3.503887,-5.081683],[-4.221533,8.796908,3.984413,0.540266],[-9.074298,-1.729557,8.448185,-5.141611],[-9.305650,3.962596,-9.894780,-9.875291],[-7.035754,-0.594422,6.334405,-5.154938],[-1.462406,-0.477763,-6.780444,-3.108172],[5.863060,2.082108,3.936412,-3.442109],[-9.612064,0.878557,7.792132,-0.817411],[-5.016825,-7.453781,4.300252,2.394397]]], dtype = "float32")#candidate|14269|(2, 14, 4)|const|float32
uop_14270 = relay.asin(const_14269.astype('float32')) # shape=(2, 14, 4)
bop_14276 = relay.logical_xor(const_14269.astype('int8'), relay.reshape(uop_14270.astype('int8'), relay.shape_of(const_14269))) # shape=(2, 14, 4)
uop_14283 = relay.cos(const_14269.astype('float32')) # shape=(2, 14, 4)
func_6193_call = mod.get_global_var('func_6193')
func_6195_call = mutated_mod.get_global_var('func_6195')
const_14292 = relay.const([-4.196627,1.710550,-8.887819,2.479558,4.897617,7.416370,3.439529,8.575686,-2.210753,0.525702,4.546105,-8.007575,8.200022,-2.740461,8.205900,5.619789,8.939176,4.335337,0.803542,-8.018525,-2.987669,2.329887,-4.528406,-3.863572,7.144716,3.464209,1.369102,-4.098496,2.071931,4.806687,-6.006888,-9.664110,9.491788,6.051966,-9.378056,6.115007,-2.722754,-4.937367,6.042892,7.464428,-5.868868,8.716082,6.018365,3.081678,-9.747785,3.628794,6.546111,4.928441,5.620825,0.984675,-0.375320,8.975111,9.367962,4.737513,-3.548538,-8.790208,5.106314,-6.694762,9.980276,8.817758,-7.170967,-9.181619,-9.526498,-4.056421,-8.516190,1.174956,-4.609585,6.153691,-4.354629,-9.187306,-2.944731,-2.192352,-0.384434,-0.886321,-4.098605,-1.537110,-3.909844,-7.291055,-8.432757,-4.379705,3.786311,8.487169,-0.059083,3.821799,9.744781,0.932380,-5.315806,0.673859,-5.260586,-0.443019,-6.793033,3.417866,1.284721,8.911912,-7.219461,1.100595,-3.426647,8.422606,7.899361,2.383780,-2.537202,-0.451562,-8.906612,-5.981520,5.256533,7.938727,7.454894,-6.804800,6.036125,-7.555780,-3.973504,1.019581,-1.436821,0.608531,8.605801,-4.891286,-7.659406,4.458397,-0.081976,3.068623,-2.753397,2.770435,-0.200839,2.144172,-4.351474,1.110965,6.522814,6.985450,-4.470518,5.993496,5.913970,0.894594,0.871361,3.367192,-1.565004,3.317935,6.591041,-5.795802,4.440301,3.998797,5.608027,-8.252793,5.899943,-8.179612,-6.603282,-2.371236,5.279823,2.139397,-7.325414,7.985400,-0.045469,7.894973,6.531302,8.411313,0.341429,-6.034260,9.568992,4.892041,-5.540440,-6.641615,-0.724747,0.182166,5.103056,-0.341698,7.122199,-8.346852,-0.529665,8.583075,-6.692212,-2.261295,-0.666762,-0.751769,3.478948,-9.699082,-5.803792,2.195600,1.568264,-2.351422,1.246951,-2.747173,-2.466085,-1.808822,6.625444,1.410811,-6.332079,1.293463,-5.474895,1.120689,-0.036300,-1.815034,-0.122143,4.876481,-0.435528,-0.332756,-1.016591,-0.826053,-0.566389,0.016742,-5.671128,2.013188,6.690389,6.652368,-3.562995,9.342368,9.665842,4.591916,2.672309,7.820866,8.781526,-1.463949,4.677648,-3.306596,1.682856,6.790122,-2.664219,5.747004,8.266516,-7.616358,7.451191,-6.895690,5.324882,-3.194811,-4.820519,-6.456987,-8.615982,6.544059,3.260284,1.540010,-1.876451,-2.093630,1.492611,-9.814590,9.090013,-7.689354,-6.780523,3.597638,8.588921,5.888659,0.835002,9.892952,-1.757280,2.737495,-1.414113,-9.544748,8.040856,-6.453420,-1.092956,-8.963051,2.937278,-9.374366,2.786501,8.192682,-7.670042,9.698743,-8.883334,4.166216,9.426780,-9.013087,0.239960,-1.242910,1.697673,3.845330,1.588180,7.766935,-9.927366,2.750254,1.324573,-8.040575,2.027439,-9.284684,-6.893897,-6.748000,-1.977150,-6.953912,2.904547,3.754462,6.086178,3.674377,-4.044255,2.030208,-3.750840,-9.900668,6.226325,2.161434,-2.472610,-8.831156,3.186415,7.739725,8.433544,9.985357,-6.586827,0.900249,3.308127,0.212655,-2.175895,5.663939,9.214334,-3.946762,-3.508273,0.396800,3.903652,-1.260810,-2.250930,5.608499,0.267330,-3.954735,8.163741,7.527866,-8.114625,-0.765700,0.568387,-8.219139,7.436325,9.919683,-3.355768,1.783061,-1.010206,0.045240,0.470686,-2.123183,7.018213,-1.871886,-6.091862,-0.505462,-9.022263,6.765030,-7.670555,-2.017641,4.875462,3.198454,-7.855555,1.704753,-3.277344,3.757873,0.817869,-4.079281,0.959373,9.257643,-4.027843,-1.051179,-8.880837,-9.271249,9.071144,5.795349,-6.619390,5.487784,7.603795,3.038386,1.068031,9.725501,-8.358662,6.655327,-3.786743,-1.988167,-2.589269,-1.087288,-3.115917,8.754410,8.162751,-6.179057,-3.307349,4.934179,0.586901,3.063105,0.167398,7.642514,5.352048,7.365394,-0.059162,-1.442683,0.319931,2.926068,-5.064628,7.057811,7.059092,3.454867,7.695282,2.265418,-9.832375,8.744222,0.264324,5.337273,-5.349747,3.415155,-8.932013,6.895407,-5.921738,-2.261274,-1.947960,-4.307962,8.249188,8.714232,-4.098319,3.697385,4.480982,8.771238,-2.883159,2.634799,5.978027,3.788165,5.736972,3.559374,0.026665,-4.188774,-2.211435,-4.358984,-9.144158,-9.622265,-0.321987,2.041847,6.731139,3.623133,-7.552132,-1.423999,8.605945,3.773921,-6.229361,-5.905278,-8.173477,3.159044,9.157808,6.118977,4.070085,4.344894,9.230130,-1.821161,1.170204,-8.278113,-9.108982,5.792155,-1.674564,-1.184711,-8.099219,9.875043,3.982102,6.562681,-6.094886,8.871184,-4.897104,4.177145,7.050235,-6.791312,2.173448,-0.215438,2.825451,7.372786,3.740820,4.470489,-9.546505,-5.708377,5.686120,7.184989,-8.174863,-8.069707,1.981512,2.401588,3.789142,5.674321,-2.704400,-2.248930,4.337069,-9.748807,-4.490394,-1.543419,-6.585932,-0.361616,-4.381573,3.166354,-9.317776,-3.886160,3.353487,4.283800,3.980786,-5.111345,-7.188840,-8.504039,-2.452569,-6.027803,-9.067062,-7.642425,-0.542852,-7.701958,-5.229364,6.839591,6.273817,-6.711680,0.505920,5.536160,-4.429452,1.459693,7.142394,-9.090010,-0.976229,-7.726243,-9.713430,7.802311,2.894816,1.703901,8.505129,0.382705,-7.073739,9.634182,5.489733,3.903932,-2.347038,-9.488423,-4.107781,-2.638661,-6.978820,6.932990,7.062771,3.309328,-3.507072,-3.312250,5.266876,1.590365,6.552146,-5.586814,6.999401,-4.845733,-6.848949,3.945240,2.423482,0.555910,-9.492382,-4.499008,5.483921,7.257814,0.050824,5.492950,5.046488,-3.059731,3.675919,7.830518,-6.436648,4.014812,-0.429073,3.328667,-3.428936,8.076986,3.360586,-4.497852,6.046023,9.756324,2.671426,-4.295788,5.239673,3.046286,8.069561,8.457204,-7.542418,-7.137676,-6.020637,-2.790136,-5.338219,7.178192,-8.863375,-9.931074,5.077269,-9.049412,-7.242952,5.292539,0.520678,-9.069909,4.994928,0.122362,-9.751548,1.842497,4.943610,6.833178,9.670041,-5.111442,-3.930470,-5.332025,-1.276007,-5.095233,1.243951,-5.709559,-9.291266,7.485051,-7.608428,2.568219,-5.926798,2.589437,4.259168,6.689562,-2.505701,-1.217888,-5.828298,-9.575781,8.047930,2.695243,3.261795,8.840966,-6.572070,4.757295,4.919593,-9.856088,6.213820,-0.129077,-8.390891,-4.581128,3.326495,-0.769312,7.836322,-7.766405,5.746325,1.738966,9.293028,4.166493,9.536615,-1.175051,3.186169,-9.000934,7.643636,6.081821,-3.580445,-8.198478,-4.878477,2.710771,8.650673,-4.131499,2.539049,0.824405,8.963336,-3.784086,-1.734196,2.156733,9.522206,-8.747634,-9.307128,5.051260,6.479797,-9.083044,-6.633598,4.412047,2.517632,-5.010252,3.365188,1.171386,-4.385607,7.368856,9.420015,8.848100,-7.061675,1.659212,5.362289,6.709018,-3.055032,2.569728,1.068103,-4.580838,-2.789679,7.824161,2.821723,-0.164408,3.255947,-5.373038,5.219836,8.536954,2.248086,-7.764713,6.596367,-6.020174,-3.901681,-1.004006,-4.253412,-4.360075,-1.544815,1.682500,8.304228,2.950564,0.460126,7.077472,8.734874,6.750032,8.471334,-3.942259,4.626615,-8.529361,-0.600293,-7.890604,1.742606,7.734328,-4.497655,6.651175,2.406460,-9.570256,-2.118731,9.049192,3.520584,6.387411,-5.386080,7.369670,-9.403849,5.498987,5.533519,2.666343,2.659203,-4.272163,5.981232,8.419352,-7.784631,-1.503711,4.607083,4.470071,-9.582376,3.700928,-0.419788,-7.330149,-0.816894,4.816289,4.841319,-6.394311,1.977288,3.525970,7.122117,2.386269,-5.316266,-9.588111,9.491978,-4.787752,-4.623051,8.935835,2.842635,7.315913,0.017339,5.429636,-1.021942,5.744842,-9.743385,-9.708495,7.740776,5.400530,5.978155,8.258548,0.252670,-8.107755,9.944965,-5.119551,-5.729717,-2.687778,-4.632498,-8.323543,-8.830998,1.904115,-6.998076,-3.699858,0.446371,-6.603076,9.513276,-4.929948,0.944461,3.164308,-7.080102,6.824902,8.254992,-3.245152,8.346310,-6.855528,7.619918,-9.853388,-8.325185,6.520929,0.993662,-1.623830,-5.688285,3.121948,-6.724833,-6.068368,5.860878,5.547693,-9.879505,-2.272450,-7.927556,8.376750,-7.514639,-1.895961,-2.695427,5.179597,8.445375,-5.147725,-9.108907,6.102504], dtype = "float64")#candidate|14292|(784,)|const|float64
call_14291 = relay.TupleGetItem(func_6193_call(relay.reshape(const_14292.astype('float64'), [7, 16, 7])), 1)
call_14293 = relay.TupleGetItem(func_6195_call(relay.reshape(const_14292.astype('float64'), [7, 16, 7])), 1)
var_14296 = relay.var("var_14296", dtype = "float32", shape = (2, 14, 4))#candidate|14296|(2, 14, 4)|var|float32
bop_14297 = relay.subtract(uop_14283.astype('uint8'), relay.reshape(var_14296.astype('uint8'), relay.shape_of(uop_14283))) # shape=(2, 14, 4)
output = relay.Tuple([bop_14276,call_14291,const_14292,bop_14297,])
output2 = relay.Tuple([bop_14276,call_14293,const_14292,bop_14297,])
F = relay.Function([var_14296,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_14296,], output2)
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
	relay.transform.SimplifyExpr(),
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
