import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_276 = relay.var("var_276", dtype = "bool", shape = (9, 4, 16))#candidate|276|(9, 4, 16)|var|bool
var_277 = relay.var("var_277", dtype = "bool", shape = (9, 4, 16))#candidate|277|(9, 4, 16)|var|bool
bop_278 = relay.logical_and(var_276.astype('bool'), relay.reshape(var_277.astype('bool'), relay.shape_of(var_276))) # shape=(9, 4, 16)
output = bop_278
output2 = bop_278
func_311 = relay.Function([var_276,var_277,], output)
mod['func_311'] = func_311
mod = relay.transform.InferType()(mod)
mutated_mod['func_311'] = func_311
mutated_mod = relay.transform.InferType()(mutated_mod)
func_311_call = mutated_mod.get_global_var('func_311')
var_313 = relay.var("var_313", dtype = "bool", shape = (9, 4, 16))#candidate|313|(9, 4, 16)|var|bool
var_314 = relay.var("var_314", dtype = "bool", shape = (9, 4, 16))#candidate|314|(9, 4, 16)|var|bool
call_312 = func_311_call(var_313,var_314,)
output = call_312
func_315 = relay.Function([var_313,var_314,], output)
mutated_mod['func_315'] = func_315
mutated_mod = relay.transform.InferType()(mutated_mod)
var_490 = relay.var("var_490", dtype = "uint8", shape = ())#candidate|490|()|var|uint8
var_491 = relay.var("var_491", dtype = "uint8", shape = (13, 1, 13))#candidate|491|(13, 1, 13)|var|uint8
bop_492 = relay.right_shift(var_490.astype('uint8'), var_491.astype('uint8')) # shape=(13, 1, 13)
bop_497 = relay.bitwise_xor(var_490.astype('int16'), bop_492.astype('int16')) # shape=(13, 1, 13)
func_311_call = mod.get_global_var('func_311')
func_315_call = mutated_mod.get_global_var('func_315')
var_503 = relay.var("var_503", dtype = "bool", shape = (576,))#candidate|503|(576,)|var|bool
call_502 = func_311_call(relay.reshape(var_503.astype('bool'), [9, 4, 16]), relay.reshape(var_503.astype('bool'), [9, 4, 16]), )
call_504 = func_311_call(relay.reshape(var_503.astype('bool'), [9, 4, 16]), relay.reshape(var_503.astype('bool'), [9, 4, 16]), )
func_311_call = mod.get_global_var('func_311')
func_315_call = mutated_mod.get_global_var('func_315')
call_507 = func_311_call(relay.reshape(var_503.astype('bool'), [9, 4, 16]), relay.reshape(var_503.astype('bool'), [9, 4, 16]), )
call_508 = func_311_call(relay.reshape(var_503.astype('bool'), [9, 4, 16]), relay.reshape(var_503.astype('bool'), [9, 4, 16]), )
output = relay.Tuple([bop_497,call_502,var_503,call_507,])
output2 = relay.Tuple([bop_497,call_504,var_503,call_508,])
func_511 = relay.Function([var_490,var_491,var_503,], output)
mod['func_511'] = func_511
mod = relay.transform.InferType()(mod)
var_512 = relay.var("var_512", dtype = "uint8", shape = ())#candidate|512|()|var|uint8
var_513 = relay.var("var_513", dtype = "uint8", shape = (13, 1, 13))#candidate|513|(13, 1, 13)|var|uint8
var_514 = relay.var("var_514", dtype = "bool", shape = (576,))#candidate|514|(576,)|var|bool
output = func_511(var_512,var_513,var_514,)
func_515 = relay.Function([var_512,var_513,var_514,], output)
mutated_mod['func_515'] = func_515
mutated_mod = relay.transform.InferType()(mutated_mod)
var_525 = relay.var("var_525", dtype = "float64", shape = (8, 5, 5))#candidate|525|(8, 5, 5)|var|float64
uop_526 = relay.log(var_525.astype('float64')) # shape=(8, 5, 5)
output = uop_526
output2 = uop_526
func_553 = relay.Function([var_525,], output)
mod['func_553'] = func_553
mod = relay.transform.InferType()(mod)
mutated_mod['func_553'] = func_553
mutated_mod = relay.transform.InferType()(mutated_mod)
var_554 = relay.var("var_554", dtype = "float64", shape = (8, 5, 5))#candidate|554|(8, 5, 5)|var|float64
func_553_call = mutated_mod.get_global_var('func_553')
call_555 = func_553_call(var_554)
output = call_555
func_556 = relay.Function([var_554], output)
mutated_mod['func_556'] = func_556
mutated_mod = relay.transform.InferType()(mutated_mod)
const_691 = relay.const([[[False,True,False,True,False,True,True,True],[True,False,True,False,True,True,False,False],[False,False,False,True,False,True,True,True],[False,True,False,False,False,True,False,False],[True,False,False,True,True,True,False,False],[True,False,False,True,True,True,True,True],[True,False,False,True,True,True,False,False],[False,False,False,False,False,False,False,True],[False,False,False,True,True,False,True,True],[False,False,False,True,True,True,False,False],[True,False,True,True,True,True,True,True],[True,True,True,True,True,False,False,True],[False,False,False,False,True,True,True,True],[True,True,True,False,False,True,False,False],[False,True,True,True,False,False,True,False],[True,False,True,False,False,False,True,True]],[[False,True,True,True,False,False,True,False],[True,False,False,True,True,True,True,True],[False,False,True,True,False,False,True,True],[False,False,True,True,False,False,False,True],[True,True,False,False,True,True,False,False],[True,False,True,True,True,True,False,False],[True,True,True,False,True,False,True,False],[False,True,True,True,True,True,False,True],[False,False,True,True,False,True,True,True],[True,False,False,True,True,True,True,True],[False,False,True,False,False,False,False,False],[True,True,True,True,False,True,False,False],[False,True,True,False,False,False,True,True],[False,False,False,False,True,True,True,True],[True,False,True,True,False,True,False,False],[False,True,True,False,True,True,False,True]],[[False,True,True,False,True,False,True,False],[False,False,False,True,True,True,True,True],[True,False,False,True,False,False,True,False],[False,False,True,True,True,True,False,True],[True,True,True,False,True,True,False,False],[True,False,True,False,True,False,True,False],[True,False,False,True,False,True,True,False],[False,False,True,True,False,True,True,True],[False,False,True,False,True,False,False,False],[False,True,True,False,False,False,False,True],[False,False,False,True,False,True,True,False],[False,True,True,False,False,False,True,True],[True,False,True,False,False,True,True,True],[False,False,True,False,False,True,True,True],[False,True,False,False,True,True,False,True],[False,True,True,True,False,False,False,True]],[[False,True,True,True,False,False,False,False],[False,True,True,True,False,False,False,False],[False,False,False,True,True,False,False,False],[False,True,True,False,True,True,True,True],[False,False,False,False,True,False,False,True],[True,True,False,False,False,False,False,False],[False,True,True,False,True,True,False,True],[False,True,True,True,False,False,False,False],[True,True,False,False,True,False,True,True],[False,False,True,False,False,True,False,True],[False,True,True,False,False,True,True,False],[False,True,True,False,True,True,False,False],[False,False,False,False,False,False,True,False],[False,False,False,False,True,False,True,False],[True,False,False,True,True,True,True,True],[False,False,True,False,False,True,False,False]],[[True,True,False,False,True,True,False,True],[True,True,True,True,True,True,True,True],[True,True,False,True,False,False,False,True],[False,False,True,False,True,True,True,True],[False,True,True,True,True,True,False,False],[False,False,True,False,True,False,True,False],[True,True,True,False,True,False,True,False],[False,False,False,True,True,True,False,False],[True,True,True,False,True,False,False,True],[False,False,True,True,False,False,True,False],[False,True,False,True,True,True,True,True],[True,False,False,False,True,True,False,False],[False,False,False,True,False,True,True,False],[True,False,True,True,True,False,True,True],[True,True,False,False,False,False,True,True],[False,False,False,True,True,False,False,True]],[[False,False,True,False,True,False,False,False],[False,True,False,True,False,True,False,True],[True,True,False,True,True,True,True,True],[True,True,False,False,True,False,False,False],[True,True,False,False,True,True,True,True],[False,True,True,False,False,True,False,True],[False,False,True,True,True,False,False,True],[True,True,True,False,True,True,False,False],[False,True,True,True,False,False,True,False],[True,False,True,True,True,True,True,False],[True,False,True,False,False,False,True,True],[True,True,True,False,False,False,True,True],[True,False,False,True,False,True,True,True],[True,False,False,True,True,True,True,False],[True,False,True,True,False,False,False,True],[True,False,False,False,False,True,True,True]],[[True,True,False,True,True,True,False,False],[False,False,True,True,False,False,False,True],[True,True,True,True,True,True,True,True],[True,True,True,True,False,False,False,True],[True,False,False,False,False,False,True,False],[False,False,True,False,True,True,False,False],[False,True,True,False,False,False,True,False],[True,False,True,True,False,False,False,True],[False,False,False,False,False,True,False,True],[True,False,True,False,True,True,False,False],[False,False,False,True,False,True,True,False],[True,False,True,True,False,False,False,True],[False,False,True,True,True,False,False,True],[False,True,True,True,True,False,True,True],[False,True,False,False,False,True,False,True],[False,False,False,False,False,True,True,False]],[[True,True,True,True,True,True,False,True],[True,True,False,False,True,False,True,True],[True,False,False,False,True,False,True,True],[False,False,False,False,True,True,True,False],[False,False,True,True,False,True,False,True],[True,True,True,False,True,False,False,False],[False,False,False,False,False,False,True,True],[False,True,True,True,True,False,True,True],[True,True,True,True,False,True,False,True],[False,True,False,True,True,False,False,False],[False,False,False,False,False,True,True,False],[True,True,True,False,True,True,True,False],[False,False,True,False,False,True,False,False],[False,False,False,False,False,False,False,False],[False,False,False,True,True,False,True,False],[True,True,False,False,False,False,True,False]],[[False,False,False,False,False,False,True,False],[False,True,False,False,True,False,False,True],[False,True,False,False,True,False,False,False],[True,True,False,True,True,True,True,True],[False,True,False,False,False,True,False,False],[False,True,True,True,True,True,False,False],[False,True,False,True,True,False,True,False],[True,False,True,False,True,False,False,True],[True,False,True,True,True,False,False,True],[True,True,False,False,False,False,False,True],[True,False,False,False,True,False,False,False],[False,True,True,True,True,True,True,True],[True,False,False,False,False,False,True,True],[True,True,False,False,True,False,True,True],[True,True,True,False,True,False,False,True],[True,True,True,True,False,False,False,True]],[[False,False,True,True,True,False,False,False],[True,False,False,True,True,True,False,False],[True,True,False,False,True,False,False,True],[False,True,False,False,True,False,False,True],[False,True,False,True,False,True,False,True],[True,False,False,False,False,False,False,True],[False,False,True,True,True,True,False,True],[False,False,True,True,False,True,True,True],[True,True,False,True,False,False,False,False],[True,True,False,True,True,True,False,True],[True,True,True,False,True,True,True,True],[False,True,True,False,False,False,True,True],[True,False,False,False,False,True,False,True],[False,False,False,True,True,False,True,True],[False,False,True,True,True,True,False,True],[False,True,False,False,True,True,False,True]],[[True,False,True,False,True,True,True,True],[True,False,True,True,False,False,False,False],[False,True,True,True,False,False,True,False],[True,True,True,True,False,True,False,False],[True,True,False,True,False,True,False,True],[True,True,False,False,True,False,False,True],[False,False,True,False,False,False,True,True],[True,False,False,True,True,False,True,False],[True,True,True,True,True,False,True,False],[True,True,False,True,False,True,False,False],[True,True,False,True,True,True,False,False],[True,True,False,False,True,True,True,True],[True,False,False,False,False,True,False,False],[True,True,True,True,False,True,True,True],[True,True,False,False,True,False,True,False],[True,True,True,True,False,False,False,True]],[[False,False,True,True,False,False,True,True],[True,False,False,True,True,True,False,False],[False,False,True,True,False,False,False,False],[True,True,True,True,True,True,True,True],[True,False,False,True,False,True,False,True],[True,False,False,True,True,False,True,False],[False,False,True,True,False,True,True,True],[False,False,True,True,True,False,True,False],[False,True,False,True,True,False,False,False],[True,True,True,False,True,True,False,False],[True,False,True,False,True,False,True,False],[False,False,True,True,False,False,True,True],[False,True,False,True,False,False,True,True],[True,True,True,True,False,False,True,True],[False,False,True,True,False,True,True,False],[True,True,True,False,True,False,True,True]],[[False,True,False,False,True,False,True,True],[True,False,False,True,False,True,False,False],[True,False,False,True,True,True,True,False],[False,False,False,False,False,True,True,False],[False,False,False,False,False,True,True,True],[False,True,False,False,False,False,True,True],[False,True,False,True,False,True,False,True],[True,False,True,True,False,False,False,False],[False,False,False,False,False,True,True,False],[False,True,False,False,False,True,True,False],[False,True,False,True,False,False,False,True],[False,True,True,False,True,True,True,False],[True,True,False,True,True,False,True,True],[True,False,False,True,True,True,False,False],[True,False,True,True,False,True,True,False],[False,False,True,True,True,False,True,False]],[[True,False,False,False,False,True,False,True],[True,False,True,True,True,True,True,False],[True,False,False,True,True,True,True,True],[True,False,False,False,False,False,False,False],[False,False,False,False,False,False,True,True],[False,False,False,False,True,True,False,False],[True,False,True,False,True,True,True,False],[True,False,False,False,False,True,False,False],[True,False,False,True,True,True,True,True],[False,True,True,True,True,False,False,False],[False,True,True,False,False,False,False,False],[False,True,False,False,False,False,False,True],[False,False,True,True,False,False,True,False],[True,False,True,False,False,True,True,True],[True,False,True,True,False,True,True,True],[False,True,True,False,True,False,False,False]]], dtype = "bool")#candidate|691|(14, 16, 8)|const|bool
const_692 = relay.const([[[True,True,False,True,False,False,False,True],[False,True,True,True,False,False,False,False],[True,False,False,True,True,True,True,True],[True,False,False,True,False,False,True,True],[False,False,False,False,False,False,True,False],[True,True,False,True,True,False,True,True],[False,False,False,False,True,True,True,False],[True,True,True,True,False,True,False,False],[True,False,False,True,True,False,False,False],[True,False,False,False,False,True,True,True],[True,True,True,True,True,False,True,False],[True,True,False,True,False,False,True,True],[True,False,False,False,False,False,False,True],[False,False,True,True,False,True,False,True],[False,True,False,True,True,False,False,False],[True,False,False,True,False,True,False,True]],[[True,False,True,True,True,False,False,True],[False,False,False,False,True,False,False,True],[True,False,True,False,False,True,True,True],[True,True,False,True,False,False,True,False],[True,False,True,False,False,False,True,True],[False,False,True,True,False,True,False,False],[False,True,False,False,False,True,False,True],[False,False,True,True,True,False,True,False],[False,False,False,True,False,True,False,False],[True,True,True,False,True,False,False,True],[True,False,True,False,False,True,True,False],[False,False,True,True,False,False,True,True],[True,True,False,True,False,False,False,False],[True,True,False,False,True,False,True,True],[False,True,True,False,False,False,True,False],[True,False,True,True,True,False,False,False]],[[True,False,True,False,False,True,False,False],[True,False,False,False,False,False,True,False],[True,False,True,True,True,False,False,False],[False,True,True,True,False,False,True,True],[False,True,True,True,False,True,True,True],[True,True,False,True,True,True,False,False],[False,True,False,True,True,False,True,True],[True,False,True,True,False,False,True,True],[True,False,False,False,False,True,True,True],[False,True,True,False,True,True,False,True],[False,False,False,True,False,True,False,False],[True,True,True,False,False,False,True,True],[True,True,True,True,False,True,False,False],[False,True,False,True,False,True,False,False],[True,False,True,False,True,False,False,True],[True,True,True,True,False,False,True,True]],[[True,False,False,True,True,False,True,False],[False,False,True,False,True,False,True,False],[False,False,False,False,False,False,True,False],[False,False,True,False,False,False,True,True],[True,True,False,False,True,True,False,True],[True,False,False,False,False,True,True,False],[True,True,False,False,False,True,False,False],[True,True,False,True,False,True,False,True],[False,False,True,True,False,False,True,True],[False,True,False,False,False,True,False,True],[False,True,True,False,False,True,False,False],[True,False,True,True,True,False,False,True],[False,True,True,False,True,False,False,True],[True,False,True,True,True,False,False,True],[True,False,False,True,True,False,True,False],[True,True,True,False,True,True,False,True]],[[True,True,False,False,True,False,False,False],[False,True,True,True,True,True,False,False],[True,False,False,True,True,True,True,False],[False,True,False,True,False,False,True,True],[True,True,False,False,True,False,False,True],[True,True,False,True,True,False,True,False],[True,True,True,False,True,True,False,True],[False,False,True,False,True,False,False,False],[True,False,True,False,False,True,True,True],[True,True,False,False,True,False,False,False],[True,False,False,False,True,False,False,True],[True,True,True,False,True,True,False,False],[True,True,False,True,True,True,True,False],[False,True,False,True,True,False,False,True],[False,False,True,True,True,True,False,False],[False,False,False,True,True,False,True,True]],[[False,True,False,True,False,True,True,False],[True,True,False,False,True,False,True,False],[False,True,True,True,False,False,True,True],[False,True,False,True,False,False,False,False],[True,True,True,False,False,False,False,True],[True,False,False,False,False,True,False,True],[False,False,False,True,False,False,False,False],[True,False,True,True,False,False,True,False],[True,False,False,True,False,False,True,True],[True,True,False,True,False,False,False,True],[False,True,False,False,True,False,False,False],[False,False,False,True,False,True,True,True],[False,True,False,False,True,True,False,False],[False,False,False,True,False,False,False,True],[True,False,True,False,False,False,True,False],[False,True,True,False,False,False,True,False]],[[True,True,True,True,True,True,True,True],[True,True,False,True,False,False,False,True],[False,False,False,False,False,True,True,False],[False,False,False,False,True,True,True,False],[False,False,True,True,True,True,True,False],[False,True,True,False,False,False,False,False],[False,False,True,False,True,False,False,True],[False,False,True,True,True,False,False,True],[False,True,True,True,False,False,True,True],[True,True,True,True,True,True,False,True],[True,True,True,False,True,True,True,True],[True,True,True,False,True,True,True,False],[False,False,True,True,False,True,False,False],[False,True,True,True,True,True,False,False],[False,True,True,True,False,False,True,True],[True,False,True,True,True,False,True,True]],[[True,False,False,True,True,False,True,True],[False,True,False,True,False,False,True,True],[True,False,False,True,True,True,False,False],[True,True,True,False,False,False,False,True],[True,False,False,False,True,False,False,True],[True,False,False,True,True,True,False,False],[False,True,False,True,False,False,True,False],[False,True,False,False,True,False,True,False],[True,True,True,False,True,True,True,False],[True,True,False,False,False,False,True,False],[True,True,True,False,True,True,False,True],[False,False,True,True,True,False,False,False],[False,True,False,True,False,True,False,True],[False,False,False,False,False,True,True,False],[False,False,False,True,True,False,True,True],[False,False,True,True,True,True,True,True]],[[False,True,False,False,False,False,True,False],[False,True,True,True,False,False,True,False],[False,True,False,False,True,True,True,True],[True,False,True,False,True,False,True,True],[False,False,True,False,False,True,True,True],[False,False,False,True,False,True,True,False],[False,True,False,True,False,False,False,False],[False,True,False,False,False,False,True,False],[False,True,False,False,False,True,True,False],[True,True,True,True,False,True,False,False],[False,False,True,True,False,False,True,True],[True,True,True,True,True,False,True,True],[True,False,False,True,True,True,False,True],[True,True,False,True,False,False,False,True],[True,True,False,True,True,True,False,True],[False,True,False,False,False,False,True,True]],[[False,True,True,True,True,True,False,False],[False,True,True,True,True,True,False,False],[True,False,False,False,True,False,True,True],[False,False,True,False,False,True,True,False],[False,False,True,True,True,False,True,False],[True,True,True,False,False,True,True,True],[True,True,False,False,True,True,True,True],[True,True,True,True,False,True,True,False],[True,True,False,True,True,True,True,False],[False,False,False,True,True,True,False,False],[False,False,False,False,False,True,True,True],[False,True,True,False,False,False,True,True],[True,True,False,False,False,True,False,True],[True,True,False,False,False,False,False,True],[True,False,True,True,False,False,False,False],[True,True,True,True,False,False,True,True]],[[True,True,False,True,True,False,False,False],[True,False,True,False,True,True,True,False],[False,False,True,False,False,True,False,False],[True,True,True,True,True,False,False,False],[False,False,False,True,True,False,True,False],[True,False,False,False,False,True,False,False],[True,True,False,False,False,False,False,True],[False,True,False,True,False,True,False,False],[True,False,True,False,False,False,True,True],[True,True,True,True,True,True,True,False],[False,True,False,True,True,False,False,True],[False,True,True,False,False,True,False,True],[True,True,False,True,True,True,True,False],[False,False,True,True,False,False,False,False],[True,False,True,True,True,False,False,True],[True,True,True,True,False,True,False,True]],[[False,False,True,True,True,False,False,False],[False,True,True,False,False,True,True,True],[False,False,False,True,False,True,False,True],[False,True,False,True,False,True,False,False],[True,True,True,True,True,True,True,False],[True,False,False,True,False,True,False,False],[False,True,True,False,False,True,False,False],[False,False,True,False,True,False,False,True],[True,True,False,True,True,True,True,False],[True,True,True,True,True,True,True,True],[False,False,True,False,True,True,True,True],[False,False,True,True,False,True,False,False],[True,False,True,False,True,False,False,True],[True,True,False,False,False,False,True,True],[False,True,True,False,False,False,True,False],[True,True,False,True,False,False,True,True]],[[True,False,True,False,False,True,True,False],[False,False,False,True,False,False,False,False],[True,True,False,True,False,False,False,True],[True,False,False,True,False,False,True,True],[False,False,False,True,False,True,True,False],[True,True,True,True,True,True,False,False],[True,False,False,True,False,False,False,True],[False,False,True,False,False,False,False,True],[False,False,False,False,True,True,True,True],[False,False,False,False,False,False,False,True],[True,False,False,True,False,False,True,False],[False,False,True,True,False,True,False,False],[True,False,True,False,True,False,True,True],[False,False,True,False,False,False,True,True],[False,True,True,True,True,False,True,False],[False,False,True,False,True,True,False,False]],[[True,True,True,False,True,False,True,False],[False,True,False,True,True,False,False,True],[True,True,False,True,True,False,True,True],[False,False,True,False,True,False,False,False],[True,True,False,True,False,True,True,False],[False,True,True,True,True,False,True,True],[True,True,False,True,True,True,False,False],[True,False,False,False,False,False,False,True],[False,False,False,False,True,True,False,False],[True,False,True,False,False,False,True,True],[False,True,False,True,False,True,True,True],[True,True,True,True,False,True,False,False],[True,True,False,True,False,False,True,True],[False,False,False,False,True,True,False,True],[True,False,False,True,True,False,True,False],[True,False,True,True,False,False,True,True]]], dtype = "bool")#candidate|692|(14, 16, 8)|const|bool
bop_693 = relay.logical_and(const_691.astype('bool'), relay.reshape(const_692.astype('bool'), relay.shape_of(const_691))) # shape=(14, 16, 8)
func_511_call = mod.get_global_var('func_511')
func_515_call = mutated_mod.get_global_var('func_515')
var_698 = relay.var("var_698", dtype = "uint8", shape = ())#candidate|698|()|var|uint8
var_699 = relay.var("var_699", dtype = "uint8", shape = (169,))#candidate|699|(169,)|var|uint8
var_700 = relay.var("var_700", dtype = "bool", shape = (576,))#candidate|700|(576,)|var|bool
call_697 = relay.TupleGetItem(func_511_call(relay.reshape(var_698.astype('uint8'), []), relay.reshape(var_699.astype('uint8'), [13, 1, 13]), relay.reshape(var_700.astype('bool'), [576,]), ), 1)
call_701 = relay.TupleGetItem(func_515_call(relay.reshape(var_698.astype('uint8'), []), relay.reshape(var_699.astype('uint8'), [13, 1, 13]), relay.reshape(var_700.astype('bool'), [576,]), ), 1)
func_311_call = mod.get_global_var('func_311')
func_315_call = mutated_mod.get_global_var('func_315')
call_705 = func_311_call(relay.reshape(var_700.astype('bool'), [9, 4, 16]), relay.reshape(var_700.astype('bool'), [9, 4, 16]), )
call_706 = func_311_call(relay.reshape(var_700.astype('bool'), [9, 4, 16]), relay.reshape(var_700.astype('bool'), [9, 4, 16]), )
func_553_call = mod.get_global_var('func_553')
func_556_call = mutated_mod.get_global_var('func_556')
var_709 = relay.var("var_709", dtype = "float64", shape = (200,))#candidate|709|(200,)|var|float64
call_708 = func_553_call(relay.reshape(var_709.astype('float64'), [8, 5, 5]))
call_710 = func_553_call(relay.reshape(var_709.astype('float64'), [8, 5, 5]))
uop_733 = relay.cos(var_699.astype('float32')) # shape=(169,)
uop_737 = relay.log2(uop_733.astype('float32')) # shape=(169,)
output = relay.Tuple([bop_693,call_697,var_698,var_700,call_705,call_708,var_709,uop_737,])
output2 = relay.Tuple([bop_693,call_701,var_698,var_700,call_706,call_710,var_709,uop_737,])
func_757 = relay.Function([var_698,var_699,var_700,var_709,], output)
mod['func_757'] = func_757
mod = relay.transform.InferType()(mod)
var_758 = relay.var("var_758", dtype = "uint8", shape = ())#candidate|758|()|var|uint8
var_759 = relay.var("var_759", dtype = "uint8", shape = (169,))#candidate|759|(169,)|var|uint8
var_760 = relay.var("var_760", dtype = "bool", shape = (576,))#candidate|760|(576,)|var|bool
var_761 = relay.var("var_761", dtype = "float64", shape = (200,))#candidate|761|(200,)|var|float64
output = func_757(var_758,var_759,var_760,var_761,)
func_762 = relay.Function([var_758,var_759,var_760,var_761,], output)
mutated_mod['func_762'] = func_762
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1180 = relay.var("var_1180", dtype = "float64", shape = (11, 13, 10))#candidate|1180|(11, 13, 10)|var|float64
uop_1181 = relay.atanh(var_1180.astype('float64')) # shape=(11, 13, 10)
func_311_call = mod.get_global_var('func_311')
func_315_call = mutated_mod.get_global_var('func_315')
var_1190 = relay.var("var_1190", dtype = "bool", shape = (576,))#candidate|1190|(576,)|var|bool
call_1189 = func_311_call(relay.reshape(var_1190.astype('bool'), [9, 4, 16]), relay.reshape(var_1190.astype('bool'), [9, 4, 16]), )
call_1191 = func_311_call(relay.reshape(var_1190.astype('bool'), [9, 4, 16]), relay.reshape(var_1190.astype('bool'), [9, 4, 16]), )
func_757_call = mod.get_global_var('func_757')
func_762_call = mutated_mod.get_global_var('func_762')
const_1195 = relay.const(6, dtype = "uint8")#candidate|1195|()|const|uint8
var_1196 = relay.var("var_1196", dtype = "uint8", shape = (169,))#candidate|1196|(169,)|var|uint8
var_1197 = relay.var("var_1197", dtype = "float64", shape = (200,))#candidate|1197|(200,)|var|float64
call_1194 = relay.TupleGetItem(func_757_call(relay.reshape(const_1195.astype('uint8'), []), relay.reshape(var_1196.astype('uint8'), [169,]), relay.reshape(var_1190.astype('bool'), [576,]), relay.reshape(var_1197.astype('float64'), [200,]), ), 5)
call_1198 = relay.TupleGetItem(func_762_call(relay.reshape(const_1195.astype('uint8'), []), relay.reshape(var_1196.astype('uint8'), [169,]), relay.reshape(var_1190.astype('bool'), [576,]), relay.reshape(var_1197.astype('float64'), [200,]), ), 5)
uop_1212 = relay.atan(var_1180.astype('float32')) # shape=(11, 13, 10)
output = relay.Tuple([uop_1181,call_1189,var_1190,call_1194,const_1195,var_1196,var_1197,uop_1212,])
output2 = relay.Tuple([uop_1181,call_1191,var_1190,call_1198,const_1195,var_1196,var_1197,uop_1212,])
func_1230 = relay.Function([var_1180,var_1190,var_1196,var_1197,], output)
mod['func_1230'] = func_1230
mod = relay.transform.InferType()(mod)
mutated_mod['func_1230'] = func_1230
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1230_call = mutated_mod.get_global_var('func_1230')
var_1232 = relay.var("var_1232", dtype = "float64", shape = (11, 13, 10))#candidate|1232|(11, 13, 10)|var|float64
var_1233 = relay.var("var_1233", dtype = "bool", shape = (576,))#candidate|1233|(576,)|var|bool
var_1234 = relay.var("var_1234", dtype = "uint8", shape = (169,))#candidate|1234|(169,)|var|uint8
var_1235 = relay.var("var_1235", dtype = "float64", shape = (200,))#candidate|1235|(200,)|var|float64
call_1231 = func_1230_call(var_1232,var_1233,var_1234,var_1235,)
output = call_1231
func_1236 = relay.Function([var_1232,var_1233,var_1234,var_1235,], output)
mutated_mod['func_1236'] = func_1236
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1254 = relay.const([[[-2.897673,-8.452989,5.943481,-6.897435,0.193541,-5.862780,5.692675,0.360507,7.214160],[-5.012734,8.478352,4.177880,8.581833,-6.486789,-9.646716,-0.495518,-3.188710,-2.407925],[-2.624823,-0.182827,-0.822827,-7.817667,8.991522,2.587798,-8.144335,-6.533465,-9.431851],[-0.075048,-0.537947,9.451396,-2.677428,6.267935,-4.423699,-7.247735,3.794846,-0.480585],[9.633248,7.100122,-5.333768,-9.705730,-7.977564,4.478290,-4.145486,-0.665248,-0.496340]],[[7.844057,-1.733884,-6.146735,-7.088084,1.926465,7.481159,3.485640,-4.072963,4.376414],[1.424267,9.044117,1.834221,6.718294,-6.771301,-8.385064,7.812143,-4.395605,0.790018],[-5.917897,3.013695,5.859805,5.972826,-0.339577,2.625857,4.337968,6.525842,-9.987790],[5.398668,-9.639630,8.475027,-6.581027,-3.417029,-0.265184,1.601714,-6.901108,7.375262],[-7.194679,-4.798237,-0.915039,-6.191823,9.144724,3.906019,-9.563475,5.577744,-3.469430]],[[-8.632485,3.203685,4.640333,-8.626819,-3.672217,-9.635787,-6.725069,-5.221275,8.182276],[-9.967602,-3.586790,5.248609,3.423062,-6.742497,-6.549665,1.892242,-4.705109,2.943050],[2.568981,-4.390684,-8.033452,1.784192,6.628968,-2.637031,-6.042198,4.418002,-9.201209],[-3.154603,-0.576602,-5.131222,-2.475614,8.100389,-2.857193,-2.569504,-4.884377,3.239564],[1.450186,0.783179,-3.733899,2.687147,-6.490329,-4.910448,3.837087,-0.836235,0.474509]],[[-4.009050,3.136379,-9.294912,5.809233,4.974725,-1.682239,-2.015557,2.270959,-6.233570],[9.092316,-5.076518,-3.629040,-0.821102,-6.159376,-2.834816,8.466104,7.450532,-5.249759],[-7.275466,-1.695013,-1.832520,-0.415216,9.517926,-9.581321,-8.918235,4.691531,-9.782052],[7.315721,-9.157741,6.679029,4.253961,5.921529,3.534824,8.280107,9.452051,6.451564],[-8.594078,7.958706,2.120049,6.904425,9.719444,4.782526,7.488757,0.187084,-3.998759]],[[-7.104747,3.093013,-7.573589,0.751289,7.805463,0.278153,-7.925589,-5.198329,7.409527],[-0.285273,6.661832,-4.814173,2.442576,5.646546,2.057446,6.488203,-8.909982,9.530272],[-0.063127,-3.020629,-7.240834,-1.877714,1.564114,-1.961222,1.437456,6.648748,-5.098427],[8.345190,1.760769,-9.806037,-7.815965,-7.025111,8.816433,7.953382,3.396925,0.549807],[5.715771,-0.283327,-1.956809,-5.230172,8.907985,5.254700,5.187924,0.051666,3.768599]],[[3.661599,-1.715696,-6.730296,9.984737,8.306709,7.643124,-1.781991,-2.604408,3.917412],[4.077156,-8.609198,-9.898422,8.735586,-8.667241,-7.960858,-1.148056,5.320425,-7.166853],[-9.995680,1.652089,-2.675426,-0.318574,-8.355382,4.769440,-9.820367,8.273430,-4.204799],[-1.298916,9.477091,-3.822225,-0.567741,7.598959,5.101033,-8.893599,2.543316,1.637960],[-9.921514,7.481621,9.526502,2.738939,1.387480,-6.513104,-6.034875,2.017119,-3.660670]],[[2.965645,5.091321,-6.542146,-8.031665,-1.584975,8.731310,9.968826,-7.033582,-5.676051],[-0.182652,8.027999,-4.419440,2.937944,-7.131767,-3.896112,-3.238596,6.941533,-2.786789],[9.281218,-7.528919,-3.613618,0.746684,-6.111046,-2.277166,7.697822,-6.369401,4.581203],[8.684264,4.212219,0.551224,-1.528549,9.745314,3.645837,9.048161,7.768018,6.208598],[4.877754,3.891786,-6.311166,-8.572054,-1.812946,-3.272519,1.025435,-8.944287,1.160461]],[[-9.162212,-5.268212,0.208000,8.843891,-2.742182,6.653583,9.053920,-8.436501,-4.431614],[-4.408584,1.999389,5.866016,-3.028818,0.182643,8.260050,9.126036,-4.305113,6.223836],[8.059692,-3.269527,4.490770,2.854743,2.381983,-4.700919,-7.590710,-0.221240,5.443432],[2.536774,2.971477,7.606056,9.715438,-1.936375,-2.502828,-9.873969,9.225780,8.047551],[-0.668420,1.405606,-7.795405,1.500235,-5.313362,-7.495617,8.896337,-2.352295,-2.210703]],[[2.536239,-9.781426,3.735562,5.522885,-9.839357,6.213309,-5.717209,7.137826,6.102636],[3.801722,-0.837515,-2.856692,4.376509,3.021318,-4.525415,1.500433,2.046644,-3.098064],[-3.050427,-3.198116,-3.466311,-3.865711,6.582097,-4.719376,-5.560713,6.277367,7.218934],[3.779648,9.726365,-1.897759,3.782954,5.615223,5.636443,2.909256,-9.904992,7.217096],[6.979640,4.849928,2.894436,2.731787,0.445367,-2.720835,6.488314,7.839592,-6.896250]],[[-7.327433,-2.623721,5.863470,2.074797,3.327567,-7.269334,-9.147884,2.307843,9.035685],[6.001643,-3.462121,2.607318,-2.044046,-7.959341,-6.872936,6.472300,-2.209197,-0.158125],[-5.576021,8.888228,4.668304,-6.014942,6.454417,5.498567,-7.315301,-5.651311,3.112974],[5.280828,-2.151585,-4.278504,0.900579,9.240611,2.591727,6.085853,-8.002155,1.428836],[-7.962638,1.050550,9.884383,-6.457605,-8.216294,-1.568011,3.976180,0.688332,-4.339114]],[[-2.367780,0.050042,9.761879,2.973224,-6.472809,5.832055,-1.474755,3.915262,-2.646345],[-4.516948,-3.784496,7.331474,6.747570,0.986245,-9.481388,-9.461144,0.087375,-5.693686],[-3.483333,0.946675,9.237497,-5.682560,-6.252076,-9.728367,0.873410,-9.118978,4.691950],[-1.985722,-3.556881,9.035289,8.386633,0.787315,2.633363,-3.490891,6.096368,9.614276],[-7.333639,-7.542060,6.774740,8.542452,-7.182673,8.390746,9.407396,-6.282846,6.429330]],[[-6.909845,8.791861,7.689970,-9.415467,-4.882394,5.254596,-5.472051,2.387687,-5.265611],[8.319377,1.868625,0.293814,6.615538,7.732556,-9.514072,5.036363,0.704971,-8.576400],[-3.425064,-9.952769,6.264060,-7.345676,-2.623112,-9.774932,-6.780293,-4.672305,6.116413],[-8.197283,4.933437,-1.701782,-2.501855,-6.729738,-7.762185,-5.438012,4.373976,1.155045],[-6.037878,2.907503,-0.520171,-7.199068,0.070160,-4.299841,-4.860996,-6.853301,-8.090764]],[[-5.705588,-3.385936,9.074809,7.544112,6.503876,-6.585583,5.694107,-1.150403,0.104401],[9.981591,-3.662468,4.991667,8.613442,9.125362,0.870684,4.344047,9.878906,-7.372865],[-8.694697,-1.765145,9.222366,2.182152,-7.081736,4.793725,-4.508655,5.395435,0.965090],[9.309690,-6.449865,-4.596888,0.178074,9.003621,-5.511362,6.897699,-8.359075,-3.875036],[-2.956923,-8.992441,-0.715869,1.969890,-8.807640,9.008705,4.329507,6.110613,7.348325]]], dtype = "float32")#candidate|1254|(13, 5, 9)|const|float32
uop_1255 = relay.rsqrt(const_1254.astype('float32')) # shape=(13, 5, 9)
output = uop_1255
output2 = uop_1255
func_1257 = relay.Function([], output)
mod['func_1257'] = func_1257
mod = relay.transform.InferType()(mod)
output = func_1257()
func_1258 = relay.Function([], output)
mutated_mod['func_1258'] = func_1258
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1257_call = mod.get_global_var('func_1257')
func_1258_call = mutated_mod.get_global_var('func_1258')
call_1262 = func_1257_call()
call_1263 = func_1257_call()
output = call_1262
output2 = call_1263
func_1302 = relay.Function([], output)
mod['func_1302'] = func_1302
mod = relay.transform.InferType()(mod)
output = func_1302()
func_1303 = relay.Function([], output)
mutated_mod['func_1303'] = func_1303
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1257_call = mod.get_global_var('func_1257')
func_1258_call = mutated_mod.get_global_var('func_1258')
call_1321 = func_1257_call()
call_1322 = func_1257_call()
output = call_1321
output2 = call_1322
func_1323 = relay.Function([], output)
mod['func_1323'] = func_1323
mod = relay.transform.InferType()(mod)
output = func_1323()
func_1324 = relay.Function([], output)
mutated_mod['func_1324'] = func_1324
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1257_call = mod.get_global_var('func_1257')
func_1258_call = mutated_mod.get_global_var('func_1258')
call_1378 = func_1257_call()
call_1379 = func_1257_call()
uop_1384 = relay.sin(call_1378.astype('float64')) # shape=(13, 5, 9)
uop_1386 = relay.sin(call_1379.astype('float64')) # shape=(13, 5, 9)
output = relay.Tuple([uop_1384,])
output2 = relay.Tuple([uop_1386,])
func_1393 = relay.Function([], output)
mod['func_1393'] = func_1393
mod = relay.transform.InferType()(mod)
output = func_1393()
func_1394 = relay.Function([], output)
mutated_mod['func_1394'] = func_1394
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1302_call = mod.get_global_var('func_1302')
func_1303_call = mutated_mod.get_global_var('func_1303')
call_1412 = func_1302_call()
call_1413 = func_1302_call()
func_757_call = mod.get_global_var('func_757')
func_762_call = mutated_mod.get_global_var('func_762')
const_1416 = relay.const(-2, dtype = "uint8")#candidate|1416|()|const|uint8
const_1417 = relay.const([7,-9,8,3,8,5,4,-10,-8,7,9,9,5,7,-4,-9,4,-2,-7,-6,4,1,-5,-4,1,5,1,-1,5,-6,-2,-2,4,3,-8,-6,-8,10,-9,6,-6,-9,2,-5,-8,6,5,10,-3,-1,-10,5,8,-3,10,5,10,-4,4,9,-2,5,4,-9,8,10,-10,10,-10,3,4,-5,3,-7,1,-10,1,-2,-3,-4,2,-1,-8,-10,-3,8,10,2,-5,2,-4,-8,-10,-2,3,3,1,-8,4,7,1,-7,-9,6,-7,-9,-1,-8,9,-3,7,10,2,6,5,3,9,7,-8,-1,1,8,6,2,-5,10,3,-7,-7,10,6,-10,-5,2,-9,-10,10,-10,-1,6,9,7,7,4,-9,-9,-8,-10,5,-8,-5,-5,-6,5,-9,-5,-8,-8,-8,-2,9,-4,8,1,7,10,-8,9,1], dtype = "uint8")#candidate|1417|(169,)|const|uint8
const_1418 = relay.const([False,True,False,True,False,True,True,True,False,False,True,False,False,False,True,False,False,False,False,False,False,True,True,True,False,True,True,False,True,False,True,True,True,True,True,True,True,False,False,True,False,True,False,True,True,True,True,True,True,True,False,True,False,True,False,False,False,False,False,True,False,False,True,True,True,False,False,False,False,False,False,False,False,False,True,True,True,False,True,True,True,True,False,True,False,True,True,False,True,False,True,True,False,False,False,True,False,False,False,False,False,False,True,False,False,False,False,True,True,True,False,False,False,True,False,False,False,True,False,True,True,True,False,True,False,False,True,False,False,True,True,False,True,False,True,True,False,True,False,True,False,True,False,False,False,False,False,False,True,False,True,True,True,True,False,True,True,True,False,True,False,True,True,True,True,False,False,True,True,True,True,True,False,True,True,False,True,True,False,False,True,True,True,True,False,False,False,True,True,False,False,False,True,True,True,False,False,False,False,True,True,True,True,True,False,False,True,True,False,True,True,True,False,True,False,False,True,True,True,False,True,True,False,True,False,False,True,False,False,True,False,True,False,True,False,False,True,True,True,True,False,True,True,False,False,True,False,True,False,True,True,False,False,False,True,False,False,False,True,False,False,True,True,False,False,True,True,True,False,False,True,False,True,False,False,True,True,False,False,False,True,False,False,True,False,True,True,False,True,False,False,True,True,True,False,True,False,True,True,False,True,False,False,True,False,False,False,True,False,True,True,True,True,True,False,True,False,True,True,False,False,True,True,True,False,True,True,False,False,False,False,False,False,False,True,False,False,True,True,False,False,True,True,True,False,True,False,True,False,True,True,False,False,False,False,False,False,True,False,False,True,False,False,True,False,True,True,False,True,False,False,True,True,True,True,False,False,True,True,True,True,False,True,True,False,True,False,False,False,False,True,True,True,True,False,True,True,True,False,False,False,False,True,True,False,False,True,False,False,False,True,True,False,True,False,True,False,False,True,True,True,False,False,False,False,True,True,True,False,True,True,False,False,False,False,False,True,True,False,True,False,False,False,False,True,False,True,True,True,True,False,False,True,True,False,True,False,True,False,False,True,True,True,True,False,True,True,True,False,True,False,False,True,False,True,False,False,False,False,True,True,False,True,True,True,True,False,True,True,True,False,False,False,True,True,False,False,False,True,False,True,True,True,True,True,False,True,False,False,True,True,False,False,True,True,True,False,True,True,True,False,True,True,True,False,False,True,False,False,True,False,False,False,True,True,False,True,False,False,False,False,True,False,False,False,True,True,True,False,False,False,True,True,False,False,True,False,True,True,True,False,False,True,True,True,False,True,True,False,True,True,False,False,True,False,True], dtype = "bool")#candidate|1418|(576,)|const|bool
const_1419 = relay.const([6.428140,6.891362,8.345114,8.835098,-4.846568,5.593524,2.349557,-6.130455,-7.572017,-2.354982,-6.655574,-7.176559,3.226564,-0.013658,-4.970791,-1.636603,0.114497,0.623605,-1.473999,-9.605203,-8.875432,-4.034991,4.915769,6.478471,1.423658,-5.817843,-8.236776,3.543651,5.659274,-5.197391,9.307386,5.697896,0.573645,-3.719143,1.357485,-8.029700,-4.060480,-3.461260,-2.166560,3.126727,0.777240,0.592741,-3.569649,6.900651,-1.250164,6.112064,-9.323675,0.399130,-1.663355,3.272282,-3.904855,2.761448,-2.490103,3.522756,-9.124519,-6.425375,-2.377658,2.954734,2.773663,-6.982214,2.774149,9.211081,-1.690245,2.243167,-4.991056,-1.884884,-8.438284,5.329978,1.822727,4.989316,-9.471459,6.675636,7.298032,4.904569,9.953807,4.768573,-4.323146,-5.784640,2.247985,6.997931,-5.151725,-7.657421,4.520781,-1.720906,-2.211209,-3.273153,7.255487,9.913869,2.349670,6.720563,-2.335515,4.666281,-1.976235,1.308034,0.253476,2.103433,1.767251,-2.538198,-8.042563,7.456898,6.583072,2.576971,-5.117814,4.090062,0.029943,-7.408578,8.600972,-1.729982,-7.426699,4.971995,-8.370523,8.825745,3.222669,3.340032,-7.442866,-4.205341,-9.605013,9.007430,8.977708,-6.900388,2.387843,-4.571415,-4.445124,-2.079344,4.971291,-7.705209,2.589197,5.942844,-3.285850,-4.936640,6.691469,-5.287198,-1.289291,-0.354806,-3.967557,-5.601080,-5.848793,1.721880,-7.788364,1.392321,7.395760,2.668618,0.343507,9.454947,3.665725,1.680586,0.269655,9.598937,7.926322,7.029112,-2.435908,6.002329,-8.793300,-3.049928,6.703128,-6.967718,1.745265,0.950537,-7.537731,-1.935164,-8.694281,9.004157,9.090864,5.424310,-0.942344,3.585819,-1.485196,4.322703,8.381303,4.222797,2.636858,7.621104,-4.568075,-4.400591,-4.730016,-8.435789,-9.755617,-6.277761,-7.736718,-9.371042,-9.812665,-4.745053,-8.259801,7.375799,7.110503,-2.610975,0.944099,3.083997,-7.698877,-8.989442,0.319631,3.118083,-6.750169,6.379879,7.139508,-5.183099,2.049731,9.247646,-5.945017,2.372460], dtype = "float64")#candidate|1419|(200,)|const|float64
call_1415 = relay.TupleGetItem(func_757_call(relay.reshape(const_1416.astype('uint8'), []), relay.reshape(const_1417.astype('uint8'), [169,]), relay.reshape(const_1418.astype('bool'), [576,]), relay.reshape(const_1419.astype('float64'), [200,]), ), 4)
call_1420 = relay.TupleGetItem(func_762_call(relay.reshape(const_1416.astype('uint8'), []), relay.reshape(const_1417.astype('uint8'), [169,]), relay.reshape(const_1418.astype('bool'), [576,]), relay.reshape(const_1419.astype('float64'), [200,]), ), 4)
func_757_call = mod.get_global_var('func_757')
func_762_call = mutated_mod.get_global_var('func_762')
call_1422 = relay.TupleGetItem(func_757_call(relay.reshape(const_1416.astype('uint8'), []), relay.reshape(const_1417.astype('uint8'), [169,]), relay.reshape(const_1418.astype('bool'), [576,]), relay.reshape(const_1419.astype('float64'), [200,]), ), 7)
call_1423 = relay.TupleGetItem(func_762_call(relay.reshape(const_1416.astype('uint8'), []), relay.reshape(const_1417.astype('uint8'), [169,]), relay.reshape(const_1418.astype('bool'), [576,]), relay.reshape(const_1419.astype('float64'), [200,]), ), 7)
output = relay.Tuple([call_1412,call_1415,const_1416,const_1417,const_1418,const_1419,call_1422,])
output2 = relay.Tuple([call_1413,call_1420,const_1416,const_1417,const_1418,const_1419,call_1423,])
func_1424 = relay.Function([], output)
mod['func_1424'] = func_1424
mod = relay.transform.InferType()(mod)
mutated_mod['func_1424'] = func_1424
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1424_call = mutated_mod.get_global_var('func_1424')
call_1425 = func_1424_call()
output = call_1425
func_1426 = relay.Function([], output)
mutated_mod['func_1426'] = func_1426
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1323_call = mod.get_global_var('func_1323')
func_1324_call = mutated_mod.get_global_var('func_1324')
call_1514 = func_1323_call()
call_1515 = func_1323_call()
func_757_call = mod.get_global_var('func_757')
func_762_call = mutated_mod.get_global_var('func_762')
const_1519 = relay.const(-6, dtype = "uint8")#candidate|1519|()|const|uint8
var_1520 = relay.var("var_1520", dtype = "uint8", shape = (169,))#candidate|1520|(169,)|var|uint8
var_1521 = relay.var("var_1521", dtype = "bool", shape = (576,))#candidate|1521|(576,)|var|bool
const_1522 = relay.const([1.566390,-8.949692,-9.924839,6.005563,2.661628,7.680563,2.530963,-8.202745,2.365661,-5.313198,2.508255,3.148402,-8.928279,-6.009372,7.754785,9.649003,6.238163,6.394591,5.080497,4.342980,3.496760,8.528913,2.682300,-1.686863,-8.855946,7.940145,4.498657,1.897025,4.514893,-6.789016,-4.314853,2.444399,2.544083,5.713770,0.977251,3.881874,9.156457,0.337243,1.886123,8.978121,2.090800,8.138820,-8.000783,-4.627513,-8.570894,-0.232455,-8.919611,-5.429696,6.983927,5.986347,-1.087391,3.697846,7.580892,7.808125,-7.943335,-5.389816,7.238466,4.929884,3.065971,0.337312,-7.966889,-5.551208,7.007318,-0.243118,-7.625257,3.826151,2.191702,6.723107,-1.673486,6.666395,5.392410,-2.769004,6.090974,-3.808877,6.787288,-7.678145,-3.588283,2.934085,3.415131,-9.954003,3.112301,9.311952,-5.444021,1.813031,7.423832,8.387190,-7.887456,0.529747,1.031491,-1.911683,1.412193,-3.870355,0.185961,1.320781,-5.717339,5.879864,6.900627,-3.144757,8.203693,-0.221940,-2.234692,3.942714,0.111981,-8.976910,8.348139,-8.721815,7.808089,-9.048761,-1.654871,7.301403,1.966447,-3.620226,8.434341,-3.879853,-7.030742,4.259767,-3.207486,3.972976,8.266446,7.561825,8.451894,1.898076,-3.129911,1.271676,3.124701,0.964016,8.323422,-4.965005,-9.703678,5.771475,3.364965,3.762742,-3.946725,-6.795121,-3.528664,-3.958486,7.600675,-8.475342,5.056656,-0.732504,2.999254,4.387468,5.262375,7.898332,-0.869128,-0.147637,-4.328837,6.569512,-3.818224,-2.925090,8.956810,-0.767328,0.788060,5.190566,5.194521,3.790468,6.650779,1.787902,-9.566399,0.958957,-8.405908,2.996853,8.899611,9.885098,-6.176245,8.829482,-1.186371,-4.846157,-5.793629,-2.446345,9.147825,-7.945913,-0.969001,2.491937,1.730253,3.789270,-3.295930,-4.175346,2.341812,9.101719,8.499117,-3.923101,4.283296,6.799133,-9.773959,6.354642,-4.688841,-9.603720,1.276857,8.786049,-0.668655,-1.996665,3.596181,1.104515,-9.071773,-1.169337,4.399082,7.183675,1.618150,-4.715874], dtype = "float64")#candidate|1522|(200,)|const|float64
call_1518 = relay.TupleGetItem(func_757_call(relay.reshape(const_1519.astype('uint8'), []), relay.reshape(var_1520.astype('uint8'), [169,]), relay.reshape(var_1521.astype('bool'), [576,]), relay.reshape(const_1522.astype('float64'), [200,]), ), 1)
call_1523 = relay.TupleGetItem(func_762_call(relay.reshape(const_1519.astype('uint8'), []), relay.reshape(var_1520.astype('uint8'), [169,]), relay.reshape(var_1521.astype('bool'), [576,]), relay.reshape(const_1522.astype('float64'), [200,]), ), 1)
uop_1537 = relay.erf(call_1514.astype('float32')) # shape=(13, 5, 9)
uop_1539 = relay.erf(call_1515.astype('float32')) # shape=(13, 5, 9)
output = relay.Tuple([call_1518,const_1519,var_1520,var_1521,const_1522,uop_1537,])
output2 = relay.Tuple([call_1523,const_1519,var_1520,var_1521,const_1522,uop_1539,])
func_1546 = relay.Function([var_1520,var_1521,], output)
mod['func_1546'] = func_1546
mod = relay.transform.InferType()(mod)
var_1547 = relay.var("var_1547", dtype = "uint8", shape = (169,))#candidate|1547|(169,)|var|uint8
var_1548 = relay.var("var_1548", dtype = "bool", shape = (576,))#candidate|1548|(576,)|var|bool
output = func_1546(var_1547,var_1548,)
func_1549 = relay.Function([var_1547,var_1548,], output)
mutated_mod['func_1549'] = func_1549
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1393_call = mod.get_global_var('func_1393')
func_1394_call = mutated_mod.get_global_var('func_1394')
call_1562 = relay.TupleGetItem(func_1393_call(), 0)
call_1563 = relay.TupleGetItem(func_1394_call(), 0)
output = call_1562
output2 = call_1563
func_1575 = relay.Function([], output)
mod['func_1575'] = func_1575
mod = relay.transform.InferType()(mod)
output = func_1575()
func_1576 = relay.Function([], output)
mutated_mod['func_1576'] = func_1576
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1302_call = mod.get_global_var('func_1302')
func_1303_call = mutated_mod.get_global_var('func_1303')
call_1604 = func_1302_call()
call_1605 = func_1302_call()
func_553_call = mod.get_global_var('func_553')
func_556_call = mutated_mod.get_global_var('func_556')
var_1612 = relay.var("var_1612", dtype = "float64", shape = (5, 40))#candidate|1612|(5, 40)|var|float64
call_1611 = func_553_call(relay.reshape(var_1612.astype('float64'), [8, 5, 5]))
call_1613 = func_553_call(relay.reshape(var_1612.astype('float64'), [8, 5, 5]))
uop_1614 = relay.log2(var_1612.astype('float32')) # shape=(5, 40)
func_1575_call = mod.get_global_var('func_1575')
func_1576_call = mutated_mod.get_global_var('func_1576')
call_1616 = func_1575_call()
call_1617 = func_1575_call()
output = relay.Tuple([call_1604,call_1611,uop_1614,call_1616,])
output2 = relay.Tuple([call_1605,call_1613,uop_1614,call_1617,])
func_1618 = relay.Function([var_1612,], output)
mod['func_1618'] = func_1618
mod = relay.transform.InferType()(mod)
mutated_mod['func_1618'] = func_1618
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1619 = relay.var("var_1619", dtype = "float64", shape = (5, 40))#candidate|1619|(5, 40)|var|float64
func_1618_call = mutated_mod.get_global_var('func_1618')
call_1620 = func_1618_call(var_1619)
output = call_1620
func_1621 = relay.Function([var_1619], output)
mutated_mod['func_1621'] = func_1621
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1393_call = mod.get_global_var('func_1393')
func_1394_call = mutated_mod.get_global_var('func_1394')
call_1631 = relay.TupleGetItem(func_1393_call(), 0)
call_1632 = relay.TupleGetItem(func_1394_call(), 0)
output = call_1631
output2 = call_1632
func_1634 = relay.Function([], output)
mod['func_1634'] = func_1634
mod = relay.transform.InferType()(mod)
output = func_1634()
func_1635 = relay.Function([], output)
mutated_mod['func_1635'] = func_1635
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1302_call = mod.get_global_var('func_1302')
func_1303_call = mutated_mod.get_global_var('func_1303')
call_1658 = func_1302_call()
call_1659 = func_1302_call()
var_1676 = relay.var("var_1676", dtype = "float32", shape = (13, 5, 9))#candidate|1676|(13, 5, 9)|var|float32
bop_1677 = relay.floor_divide(call_1658.astype('float64'), relay.reshape(var_1676.astype('float64'), relay.shape_of(call_1658))) # shape=(13, 5, 9)
bop_1680 = relay.floor_divide(call_1659.astype('float64'), relay.reshape(var_1676.astype('float64'), relay.shape_of(call_1659))) # shape=(13, 5, 9)
func_1424_call = mod.get_global_var('func_1424')
func_1426_call = mutated_mod.get_global_var('func_1426')
call_1687 = relay.TupleGetItem(func_1424_call(), 2)
call_1688 = relay.TupleGetItem(func_1426_call(), 2)
output = relay.Tuple([bop_1677,call_1687,])
output2 = relay.Tuple([bop_1680,call_1688,])
func_1696 = relay.Function([var_1676,], output)
mod['func_1696'] = func_1696
mod = relay.transform.InferType()(mod)
mutated_mod['func_1696'] = func_1696
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1697 = relay.var("var_1697", dtype = "float32", shape = (13, 5, 9))#candidate|1697|(13, 5, 9)|var|float32
func_1696_call = mutated_mod.get_global_var('func_1696')
call_1698 = func_1696_call(var_1697)
output = call_1698
func_1699 = relay.Function([var_1697], output)
mutated_mod['func_1699'] = func_1699
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1302_call = mod.get_global_var('func_1302')
func_1303_call = mutated_mod.get_global_var('func_1303')
call_1718 = func_1302_call()
call_1719 = func_1302_call()
output = call_1718
output2 = call_1719
func_1726 = relay.Function([], output)
mod['func_1726'] = func_1726
mod = relay.transform.InferType()(mod)
output = func_1726()
func_1727 = relay.Function([], output)
mutated_mod['func_1727'] = func_1727
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1323_call = mod.get_global_var('func_1323')
func_1324_call = mutated_mod.get_global_var('func_1324')
call_1739 = func_1323_call()
call_1740 = func_1323_call()
output = call_1739
output2 = call_1740
func_1758 = relay.Function([], output)
mod['func_1758'] = func_1758
mod = relay.transform.InferType()(mod)
output = func_1758()
func_1759 = relay.Function([], output)
mutated_mod['func_1759'] = func_1759
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1765 = relay.var("var_1765", dtype = "float32", shape = (4, 10, 11))#candidate|1765|(4, 10, 11)|var|float32
uop_1766 = relay.asinh(var_1765.astype('float32')) # shape=(4, 10, 11)
func_1758_call = mod.get_global_var('func_1758')
func_1759_call = mutated_mod.get_global_var('func_1759')
call_1778 = func_1758_call()
call_1779 = func_1758_call()
output = relay.Tuple([uop_1766,call_1778,])
output2 = relay.Tuple([uop_1766,call_1779,])
func_1782 = relay.Function([var_1765,], output)
mod['func_1782'] = func_1782
mod = relay.transform.InferType()(mod)
var_1783 = relay.var("var_1783", dtype = "float32", shape = (4, 10, 11))#candidate|1783|(4, 10, 11)|var|float32
output = func_1782(var_1783)
func_1784 = relay.Function([var_1783], output)
mutated_mod['func_1784'] = func_1784
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1575_call = mod.get_global_var('func_1575')
func_1576_call = mutated_mod.get_global_var('func_1576')
call_1790 = func_1575_call()
call_1791 = func_1575_call()
output = call_1790
output2 = call_1791
func_1801 = relay.Function([], output)
mod['func_1801'] = func_1801
mod = relay.transform.InferType()(mod)
output = func_1801()
func_1802 = relay.Function([], output)
mutated_mod['func_1802'] = func_1802
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1634_call = mod.get_global_var('func_1634')
func_1635_call = mutated_mod.get_global_var('func_1635')
call_1825 = func_1634_call()
call_1826 = func_1634_call()
func_1726_call = mod.get_global_var('func_1726')
func_1727_call = mutated_mod.get_global_var('func_1727')
call_1850 = func_1726_call()
call_1851 = func_1726_call()
func_1618_call = mod.get_global_var('func_1618')
func_1621_call = mutated_mod.get_global_var('func_1621')
var_1859 = relay.var("var_1859", dtype = "float64", shape = (200,))#candidate|1859|(200,)|var|float64
call_1858 = relay.TupleGetItem(func_1618_call(relay.reshape(var_1859.astype('float64'), [5, 40])), 0)
call_1860 = relay.TupleGetItem(func_1621_call(relay.reshape(var_1859.astype('float64'), [5, 40])), 0)
func_1302_call = mod.get_global_var('func_1302')
func_1303_call = mutated_mod.get_global_var('func_1303')
call_1869 = func_1302_call()
call_1870 = func_1302_call()
func_1634_call = mod.get_global_var('func_1634')
func_1635_call = mutated_mod.get_global_var('func_1635')
call_1871 = func_1634_call()
call_1872 = func_1634_call()
output = relay.Tuple([call_1825,call_1850,call_1858,var_1859,call_1869,call_1871,])
output2 = relay.Tuple([call_1826,call_1851,call_1860,var_1859,call_1870,call_1872,])
func_1889 = relay.Function([var_1859,], output)
mod['func_1889'] = func_1889
mod = relay.transform.InferType()(mod)
mutated_mod['func_1889'] = func_1889
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1890 = relay.var("var_1890", dtype = "float64", shape = (200,))#candidate|1890|(200,)|var|float64
func_1889_call = mutated_mod.get_global_var('func_1889')
call_1891 = func_1889_call(var_1890)
output = call_1891
func_1892 = relay.Function([var_1890], output)
mutated_mod['func_1892'] = func_1892
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1726_call = mod.get_global_var('func_1726')
func_1727_call = mutated_mod.get_global_var('func_1727')
call_1918 = func_1726_call()
call_1919 = func_1726_call()
output = call_1918
output2 = call_1919
func_1927 = relay.Function([], output)
mod['func_1927'] = func_1927
mod = relay.transform.InferType()(mod)
output = func_1927()
func_1928 = relay.Function([], output)
mutated_mod['func_1928'] = func_1928
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1424_call = mod.get_global_var('func_1424')
func_1426_call = mutated_mod.get_global_var('func_1426')
call_1929 = relay.TupleGetItem(func_1424_call(), 4)
call_1930 = relay.TupleGetItem(func_1426_call(), 4)
output = call_1929
output2 = call_1930
func_1940 = relay.Function([], output)
mod['func_1940'] = func_1940
mod = relay.transform.InferType()(mod)
output = func_1940()
func_1941 = relay.Function([], output)
mutated_mod['func_1941'] = func_1941
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1323_call = mod.get_global_var('func_1323')
func_1324_call = mutated_mod.get_global_var('func_1324')
call_1966 = func_1323_call()
call_1967 = func_1323_call()
output = relay.Tuple([call_1966,])
output2 = relay.Tuple([call_1967,])
func_1974 = relay.Function([], output)
mod['func_1974'] = func_1974
mod = relay.transform.InferType()(mod)
mutated_mod['func_1974'] = func_1974
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1974_call = mutated_mod.get_global_var('func_1974')
call_1975 = func_1974_call()
output = call_1975
func_1976 = relay.Function([], output)
mutated_mod['func_1976'] = func_1976
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1302_call = mod.get_global_var('func_1302')
func_1303_call = mutated_mod.get_global_var('func_1303')
call_2004 = func_1302_call()
call_2005 = func_1302_call()
var_2010 = relay.var("var_2010", dtype = "float32", shape = (13, 5, 9))#candidate|2010|(13, 5, 9)|var|float32
bop_2011 = relay.not_equal(call_2004.astype('bool'), relay.reshape(var_2010.astype('bool'), relay.shape_of(call_2004))) # shape=(13, 5, 9)
bop_2014 = relay.not_equal(call_2005.astype('bool'), relay.reshape(var_2010.astype('bool'), relay.shape_of(call_2005))) # shape=(13, 5, 9)
output = relay.Tuple([bop_2011,])
output2 = relay.Tuple([bop_2014,])
func_2019 = relay.Function([var_2010,], output)
mod['func_2019'] = func_2019
mod = relay.transform.InferType()(mod)
mutated_mod['func_2019'] = func_2019
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2020 = relay.var("var_2020", dtype = "float32", shape = (13, 5, 9))#candidate|2020|(13, 5, 9)|var|float32
func_2019_call = mutated_mod.get_global_var('func_2019')
call_2021 = func_2019_call(var_2020)
output = call_2021
func_2022 = relay.Function([var_2020], output)
mutated_mod['func_2022'] = func_2022
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2037 = relay.var("var_2037", dtype = "float32", shape = (11, 8, 7))#candidate|2037|(11, 8, 7)|var|float32
uop_2038 = relay.erf(var_2037.astype('float32')) # shape=(11, 8, 7)
func_2019_call = mod.get_global_var('func_2019')
func_2022_call = mutated_mod.get_global_var('func_2022')
var_2041 = relay.var("var_2041", dtype = "float32", shape = (585,))#candidate|2041|(585,)|var|float32
call_2040 = relay.TupleGetItem(func_2019_call(relay.reshape(var_2041.astype('float32'), [13, 5, 9])), 0)
call_2042 = relay.TupleGetItem(func_2022_call(relay.reshape(var_2041.astype('float32'), [13, 5, 9])), 0)
output = relay.Tuple([uop_2038,call_2040,var_2041,])
output2 = relay.Tuple([uop_2038,call_2042,var_2041,])
func_2046 = relay.Function([var_2037,var_2041,], output)
mod['func_2046'] = func_2046
mod = relay.transform.InferType()(mod)
var_2047 = relay.var("var_2047", dtype = "float32", shape = (11, 8, 7))#candidate|2047|(11, 8, 7)|var|float32
var_2048 = relay.var("var_2048", dtype = "float32", shape = (585,))#candidate|2048|(585,)|var|float32
output = func_2046(var_2047,var_2048,)
func_2049 = relay.Function([var_2047,var_2048,], output)
mutated_mod['func_2049'] = func_2049
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1940_call = mod.get_global_var('func_1940')
func_1941_call = mutated_mod.get_global_var('func_1941')
call_2057 = func_1940_call()
call_2058 = func_1940_call()
func_757_call = mod.get_global_var('func_757')
func_762_call = mutated_mod.get_global_var('func_762')
const_2095 = relay.const(-9, dtype = "uint8")#candidate|2095|()|const|uint8
const_2096 = relay.const([2,-7,2,3,10,4,9,-6,-4,-6,10,9,10,8,-4,-7,8,-3,6,6,-1,3,2,8,10,3,2,10,3,9,6,-2,-10,5,-2,-3,3,-4,5,-3,7,-5,-9,-1,4,8,8,4,-6,3,2,-10,1,-10,-5,1,10,-1,2,9,-1,-6,6,6,-1,-9,-6,7,-2,-6,-1,-1,7,-8,-5,5,-4,7,-2,-2,-4,5,-2,7,-1,-3,2,-1,-9,7,6,1,6,-9,-1,-1,-4,6,1,9,8,2,9,8,4,1,-1,1,-10,-6,-3,-7,5,10,7,-8,5,-7,-7,2,2,3,-6,1,-7,1,3,-5,-3,6,8,7,6,-8,10,-4,3,-8,-2,-7,5,8,-7,-10,-2,10,-10,3,-10,-9,-1,5,-10,5,3,2,-1,7,5,-6,-4,7,5,10,-1,8,-1,7,5], dtype = "uint8")#candidate|2096|(169,)|const|uint8
const_2097 = relay.const([2.806349,2.642336,8.715629,-4.203653,4.249514,-6.597647,-9.839138,1.805948,2.003781,-5.158941,-1.114141,-9.707062,-5.679932,8.060469,8.252678,-8.992590,-1.586499,3.448398,-3.294244,9.813902,-1.524093,-3.294438,5.415322,8.943770,4.309939,7.255279,8.375739,2.076291,-1.920587,4.057544,-2.038281,-8.580128,9.816427,-8.875522,1.281899,0.092303,9.503136,-3.116626,-7.477610,-6.570261,3.131945,7.755919,0.674261,-3.048173,1.277305,3.786392,-9.827704,-4.850529,2.303477,6.290713,-9.097914,-6.526844,1.556071,9.570643,-1.109392,5.727326,7.946482,-7.206809,1.149076,-6.038895,-3.620244,-7.645125,6.576649,-7.134419,-2.741082,1.960543,5.209433,-1.955740,9.816955,-0.172846,0.757121,6.061208,-5.947904,-3.350738,7.151690,7.566850,-6.218594,-1.587582,-9.780117,8.884559,-9.048918,-1.919423,-8.442668,-1.058842,-8.156829,-4.791699,-2.237731,-7.638982,1.590178,8.803543,-3.792103,9.613010,-9.706062,-3.734525,-6.278524,1.857887,9.311466,-2.240686,4.691262,4.700615,0.611925,9.162278,4.340863,6.369436,-8.629958,4.612488,2.516356,-0.846060,-6.328184,-0.759016,-4.589478,-2.317811,3.237337,3.322772,1.979761,-3.932557,-1.700275,4.225342,-4.564451,7.360005,4.207214,0.078159,8.168309,-5.010857,-9.397536,-3.558532,6.874624,-6.686484,-7.845251,6.225647,-6.088693,-2.030251,6.101185,9.837731,-9.487485,7.180463,6.357660,-4.245472,-7.297479,3.909354,-7.714370,0.555805,-5.793673,-9.523188,3.381514,-2.830724,-5.466320,1.652320,-5.888730,3.461648,6.159290,-2.282143,4.928058,0.663582,-3.311210,-4.772389,-1.912419,-7.957543,-8.016151,9.201877,-7.206959,1.412816,8.922202,-1.041991,4.652035,-3.860803,-3.816586,-9.432601,-8.589830,3.616422,-4.609566,8.120391,0.775949,1.299897,-8.422659,-6.688107,-5.117003,3.460599,-7.695768,-9.517691,7.611871,-1.894798,9.166931,4.182360,-8.068700,-4.526161,6.792706,7.566286,4.325183,-3.315048,-6.660041,-9.796788,-1.945223,-7.680182,-4.652474,4.593177,0.042049,2.112065,-8.862074,-9.220691], dtype = "float64")#candidate|2097|(200,)|const|float64
call_2094 = relay.TupleGetItem(func_757_call(relay.reshape(const_2095.astype('uint8'), []), relay.reshape(const_2096.astype('uint8'), [169,]), relay.reshape(call_2057.astype('bool'), [576,]), relay.reshape(const_2097.astype('float64'), [200,]), ), 5)
call_2098 = relay.TupleGetItem(func_762_call(relay.reshape(const_2095.astype('uint8'), []), relay.reshape(const_2096.astype('uint8'), [169,]), relay.reshape(call_2057.astype('bool'), [576,]), relay.reshape(const_2097.astype('float64'), [200,]), ), 5)
func_2019_call = mod.get_global_var('func_2019')
func_2022_call = mutated_mod.get_global_var('func_2022')
const_2103 = relay.const([[-7.074953],[3.213153],[-8.104540],[4.427106],[-4.195464],[-1.865845],[3.059694],[4.468599],[1.864781],[6.729132],[-4.953586],[1.642483],[-4.635227],[0.945414],[7.121445],[9.375880],[-7.421959],[-8.192898],[8.072778],[9.528057],[7.124724],[9.922136],[-0.227927],[-3.605806],[0.931701],[9.366810],[-6.526307],[-5.755292],[6.632609],[8.156680],[5.646297],[-0.894682],[-3.955000],[-6.842843],[-2.718075],[1.764264],[1.055212],[3.718170],[4.499749],[4.194955],[5.940357],[-4.286453],[6.217881],[-5.948531],[9.470082],[5.107193],[1.407968],[-7.825877],[5.520265],[9.102286],[-7.668267],[4.226258],[9.218828],[6.191246],[-7.285026],[4.929211],[-4.051864],[7.168392],[-6.099366],[-0.051783],[-7.700012],[4.549793],[-2.446308],[3.878753],[-5.344320],[0.088609],[1.097400],[1.662820],[5.124539],[-6.605761],[3.738111],[8.173873],[0.827582],[-9.264897],[1.192837],[3.593998],[-3.226916],[7.269491],[-6.205327],[-9.827415],[8.474887],[-4.447445],[-0.255560],[5.804135],[-2.964023],[9.941756],[5.922227],[9.046414],[-7.136929],[3.243176],[8.551989],[3.297282],[8.816931],[-0.717545],[1.091007],[-1.796381],[-7.396502],[4.484480],[-1.551902],[4.773291],[-5.780917],[8.611779],[9.422916],[3.492393],[-6.002109],[5.521816],[9.930888],[7.478057],[4.238883],[4.001275],[8.502665],[0.153626],[-8.680977],[-7.465258],[6.566982],[0.730212],[1.795729],[-1.818247],[-4.013983],[-0.565054],[-4.202280],[-0.553797],[-8.449019],[-7.098879],[8.285516],[-9.076296],[1.999704],[-4.135450],[-2.172023],[4.022657],[-5.257836],[-2.816319],[9.739181],[5.016873],[-1.364656],[-1.785894],[7.664763],[-4.434770],[-5.772593],[-8.382070],[-7.895799],[-2.882098],[-4.831820],[6.960644],[-3.922117],[7.078852],[-8.967164],[-9.047098],[-2.467504],[9.313874],[9.216120],[7.275250],[-1.079460],[-5.642049],[-7.491805],[-2.543439],[2.182992],[-1.003914],[4.083211],[-7.350512],[-3.645225],[5.574250],[0.376558],[-2.665989],[6.620278],[-0.491180],[9.305606],[1.250739],[-4.725005],[4.282446],[-3.087132],[9.172318],[-3.743429],[-9.199469],[-5.795533],[0.897249],[-8.157675],[9.293457],[-5.280480],[8.992365],[4.839632],[-1.381038],[4.003008],[-8.352493],[8.885215],[-7.022676],[9.038927],[4.218436],[3.661149],[3.439801],[4.476741],[8.732358],[2.773085],[4.570478],[-6.290831],[2.101089],[3.002873],[6.629230],[-8.922678],[-2.655886],[8.395187],[0.158588],[-2.823279],[-6.219732],[-6.933945],[5.424334],[8.620173],[0.349357],[3.457815],[-6.577185],[3.486990],[6.926279],[-6.778023],[2.527863],[-9.125343],[-7.787479],[-2.886454],[-0.140096],[6.375053],[8.638407],[7.389335],[8.774652],[6.531764],[5.932474],[1.835011],[-4.785911],[-5.325967],[1.965492],[-6.192943],[8.896971],[-4.682847],[-0.161566],[8.466049],[-8.940940],[-9.947159],[0.801450],[-7.077576],[-0.359258],[2.782600],[5.297943],[6.176257],[-0.788517],[1.448226],[-6.946811],[-7.311993],[4.860713],[-9.625490],[-8.801552],[-4.405640],[-6.891924],[-9.807398],[-5.157670],[-1.422428],[-0.582618],[3.088420],[-3.282454],[9.190984],[-7.371847],[7.708300],[3.092190],[-8.287431],[-4.770203],[-2.399265],[-1.875530],[1.056959],[2.946677],[-7.110762],[0.020495],[-1.561819],[4.326989],[1.918704],[6.771598],[-5.195180],[9.807704],[-9.642204],[8.559590],[2.623001],[5.898610],[-2.595792],[0.767045],[-9.441006],[5.185032],[-9.189502],[6.927275],[-0.340769],[-9.045254],[3.396084],[6.040548],[1.417055],[2.474450],[7.892000],[-6.504573],[-1.263961],[-5.751427],[-2.195347],[7.509378],[6.762637],[4.169080],[7.996635],[-2.393331],[2.008222],[2.569808],[-9.301857],[-7.567397],[0.261333],[-2.642593],[9.660608],[-0.791962],[-8.333413],[-6.722047],[-1.837323],[-7.994755],[0.886723],[9.451937],[-0.956343],[-5.204918],[3.059740],[-0.397580],[-7.253960],[4.794717],[-6.919629],[-8.615578],[9.926189],[-9.348695],[-0.176494],[-1.328270],[-8.155357],[-6.171587],[-1.316955],[-1.608343],[4.442198],[7.419262],[-3.899107],[8.560280],[-5.314570],[-7.202508],[-8.563653],[-7.115143],[9.196194],[7.244617],[-0.598612],[-2.029877],[-6.275674],[-6.285445],[5.701366],[-0.194873],[2.265630],[5.086856],[5.497321],[9.660589],[2.448110],[0.375287],[-7.345711],[8.319563],[-0.903745],[1.103801],[-4.981633],[4.616817],[-9.460380],[-3.261194],[-0.489463],[1.818238],[-4.973395],[7.563082],[1.903898],[5.944511],[-9.711741],[-2.770780],[4.555593],[2.076207],[-1.992740],[-2.691872],[-3.613243],[-9.863956],[7.906301],[-7.371494],[4.935541],[5.160378],[-7.188959],[6.060663],[4.487854],[3.478856],[3.998628],[4.333782],[6.456460],[-8.694155],[4.076440],[8.191947],[-9.315182],[5.204904],[-1.714222],[2.122846],[5.995967],[9.156334],[0.843346],[2.094879],[8.603335],[9.381128],[-5.078941],[3.164989],[4.921381],[8.626465],[-9.384060],[-7.364394],[-0.569199],[-1.988274],[-1.638360],[-7.744116],[8.159955],[2.251622],[5.423238],[5.387445],[5.776695],[2.230857],[4.777432],[-5.689179],[3.590026],[-0.618151],[-6.054361],[-6.818424],[-2.424393],[7.290683],[0.140949],[-2.774392],[8.213574],[9.680976],[-0.553405],[7.884304],[6.683610],[7.435641],[-2.573887],[7.302957],[0.399347],[2.256422],[7.475798],[5.512762],[9.392852],[-1.166175],[-1.989309],[6.554640],[-4.299806],[-2.332616],[4.019059],[9.395264],[0.806144],[-6.140826],[-9.561586],[4.054867],[0.240381],[4.155720],[-0.207364],[-5.526294],[6.566706],[-2.155070],[3.852878],[0.083860],[7.521684],[-6.639374],[2.588210],[7.003279],[-6.861020],[-7.537735],[-8.293248],[-4.252008],[9.278296],[-4.042787],[-3.764702],[5.877698],[6.946447],[-0.922393],[1.557243],[-0.863947],[3.479712],[2.113010],[-5.722611],[4.645501],[-4.224703],[2.477035],[8.901392],[-3.213201],[9.089758],[8.024364],[0.833489],[0.415729],[-8.399381],[9.798505],[9.352969],[-7.083511],[-1.024346],[-4.932510],[4.656262],[1.899536],[5.393571],[-4.370322],[7.915014],[6.304016],[7.599942],[-8.726630],[9.220732],[3.028568],[5.475599],[5.713762],[-6.941034],[-3.406063],[-8.604680],[-5.318817],[-7.863801],[5.682233],[-5.528481],[5.548962],[5.068269],[3.799275],[5.130808],[4.874254],[0.037679],[-8.929849],[-1.529600],[-2.797558],[-8.722724],[9.120288],[3.680490],[-6.394759],[-2.238972],[0.957122],[7.771659],[-3.644876],[-2.043163],[3.715280],[9.340163],[-0.992586],[7.862219],[-9.378177],[8.558439],[-5.455724],[8.273861],[-3.885368],[4.789018],[-1.628466],[-0.458584],[7.485584],[-3.249648],[-2.947294],[1.186708],[-5.787308],[3.190048],[5.352835],[-6.182142],[-6.571827],[-8.593272],[2.463022],[-2.797334],[-5.019098],[-4.462843],[5.574701],[3.134570],[-5.941275],[-4.655542],[-5.626260],[-6.197832],[8.967614],[7.149015],[-4.265844],[-9.728605],[5.282866],[5.335774],[-8.329329],[-0.426499],[-7.224875],[9.758820],[-9.451001],[-8.771807],[0.036448],[6.427673],[-6.587337],[-2.441881],[9.398232],[-3.555390],[2.254712],[-3.706518],[-5.182887],[0.220488],[-0.277864],[5.738251],[-4.057337],[-2.491992]], dtype = "float32")#candidate|2103|(585, 1)|const|float32
call_2102 = relay.TupleGetItem(func_2019_call(relay.reshape(const_2103.astype('float32'), [13, 5, 9])), 0)
call_2104 = relay.TupleGetItem(func_2022_call(relay.reshape(const_2103.astype('float32'), [13, 5, 9])), 0)
bop_2107 = relay.multiply(call_2057.astype('uint8'), const_2103.astype('uint8')) # shape=(585, 576)
bop_2110 = relay.multiply(call_2058.astype('uint8'), const_2103.astype('uint8')) # shape=(585, 576)
func_1546_call = mod.get_global_var('func_1546')
func_1549_call = mutated_mod.get_global_var('func_1549')
call_2113 = relay.TupleGetItem(func_1546_call(relay.reshape(const_2096.astype('uint8'), [169,]), relay.reshape(call_2057.astype('bool'), [576,]), ), 4)
call_2114 = relay.TupleGetItem(func_1549_call(relay.reshape(const_2096.astype('uint8'), [169,]), relay.reshape(call_2057.astype('bool'), [576,]), ), 4)
output = relay.Tuple([call_2094,const_2095,const_2096,const_2097,call_2102,bop_2107,call_2113,])
output2 = relay.Tuple([call_2098,const_2095,const_2096,const_2097,call_2104,bop_2110,call_2114,])
func_2115 = relay.Function([], output)
mod['func_2115'] = func_2115
mod = relay.transform.InferType()(mod)
output = func_2115()
func_2116 = relay.Function([], output)
mutated_mod['func_2116'] = func_2116
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1424_call = mod.get_global_var('func_1424')
func_1426_call = mutated_mod.get_global_var('func_1426')
call_2131 = relay.TupleGetItem(func_1424_call(), 2)
call_2132 = relay.TupleGetItem(func_1426_call(), 2)
func_2115_call = mod.get_global_var('func_2115')
func_2116_call = mutated_mod.get_global_var('func_2116')
call_2148 = relay.TupleGetItem(func_2115_call(), 2)
call_2149 = relay.TupleGetItem(func_2116_call(), 2)
output = relay.Tuple([call_2131,call_2148,])
output2 = relay.Tuple([call_2132,call_2149,])
func_2172 = relay.Function([], output)
mod['func_2172'] = func_2172
mod = relay.transform.InferType()(mod)
output = func_2172()
func_2173 = relay.Function([], output)
mutated_mod['func_2173'] = func_2173
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1393_call = mod.get_global_var('func_1393')
func_1394_call = mutated_mod.get_global_var('func_1394')
call_2229 = relay.TupleGetItem(func_1393_call(), 0)
call_2230 = relay.TupleGetItem(func_1394_call(), 0)
output = relay.Tuple([call_2229,])
output2 = relay.Tuple([call_2230,])
func_2235 = relay.Function([], output)
mod['func_2235'] = func_2235
mod = relay.transform.InferType()(mod)
output = func_2235()
func_2236 = relay.Function([], output)
mutated_mod['func_2236'] = func_2236
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1424_call = mod.get_global_var('func_1424')
func_1426_call = mutated_mod.get_global_var('func_1426')
call_2279 = relay.TupleGetItem(func_1424_call(), 1)
call_2280 = relay.TupleGetItem(func_1426_call(), 1)
output = relay.Tuple([call_2279,])
output2 = relay.Tuple([call_2280,])
func_2283 = relay.Function([], output)
mod['func_2283'] = func_2283
mod = relay.transform.InferType()(mod)
mutated_mod['func_2283'] = func_2283
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2283_call = mutated_mod.get_global_var('func_2283')
call_2284 = func_2283_call()
output = call_2284
func_2285 = relay.Function([], output)
mutated_mod['func_2285'] = func_2285
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1940_call = mod.get_global_var('func_1940')
func_1941_call = mutated_mod.get_global_var('func_1941')
call_2302 = func_1940_call()
call_2303 = func_1940_call()
output = call_2302
output2 = call_2303
func_2317 = relay.Function([], output)
mod['func_2317'] = func_2317
mod = relay.transform.InferType()(mod)
output = func_2317()
func_2318 = relay.Function([], output)
mutated_mod['func_2318'] = func_2318
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2364 = relay.var("var_2364", dtype = "uint8", shape = (13, 7, 8))#candidate|2364|(13, 7, 8)|var|uint8
var_2365 = relay.var("var_2365", dtype = "uint8", shape = (13, 7, 8))#candidate|2365|(13, 7, 8)|var|uint8
bop_2366 = relay.equal(var_2364.astype('bool'), relay.reshape(var_2365.astype('bool'), relay.shape_of(var_2364))) # shape=(13, 7, 8)
output = relay.Tuple([bop_2366,])
output2 = relay.Tuple([bop_2366,])
func_2369 = relay.Function([var_2364,var_2365,], output)
mod['func_2369'] = func_2369
mod = relay.transform.InferType()(mod)
mutated_mod['func_2369'] = func_2369
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2369_call = mutated_mod.get_global_var('func_2369')
var_2371 = relay.var("var_2371", dtype = "uint8", shape = (13, 7, 8))#candidate|2371|(13, 7, 8)|var|uint8
var_2372 = relay.var("var_2372", dtype = "uint8", shape = (13, 7, 8))#candidate|2372|(13, 7, 8)|var|uint8
call_2370 = func_2369_call(var_2371,var_2372,)
output = call_2370
func_2373 = relay.Function([var_2371,var_2372,], output)
mutated_mod['func_2373'] = func_2373
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2399 = relay.const([[[7,-2,3,-1,-1,6],[-4,-5,8,-5,4,-3],[-9,6,8,6,9,2]],[[1,2,10,-8,-2,-7],[1,-5,3,-5,-8,10],[3,1,2,-4,9,-7]],[[-6,5,-5,10,-4,10],[4,8,8,-6,-2,1],[-10,-10,-4,8,-1,-2]],[[5,2,-7,-7,-10,3],[-4,7,7,1,6,6],[8,2,9,8,5,5]],[[4,5,8,-2,-8,-8],[8,2,-1,-3,-4,-10],[8,9,10,7,8,8]],[[9,-8,-8,2,6,-9],[2,-9,9,-1,9,-10],[6,3,-9,-9,8,7]],[[-4,1,1,-10,-3,9],[-8,9,-10,8,-6,1],[-9,-6,-10,2,-10,-7]]], dtype = "uint16")#candidate|2399|(7, 3, 6)|const|uint16
var_2400 = relay.var("var_2400", dtype = "uint16", shape = (7, 3, 6))#candidate|2400|(7, 3, 6)|var|uint16
bop_2401 = relay.left_shift(const_2399.astype('uint16'), relay.reshape(var_2400.astype('uint16'), relay.shape_of(const_2399))) # shape=(7, 3, 6)
func_1393_call = mod.get_global_var('func_1393')
func_1394_call = mutated_mod.get_global_var('func_1394')
call_2406 = relay.TupleGetItem(func_1393_call(), 0)
call_2407 = relay.TupleGetItem(func_1394_call(), 0)
bop_2411 = relay.logical_or(const_2399.astype('bool'), relay.reshape(var_2400.astype('bool'), relay.shape_of(const_2399))) # shape=(7, 3, 6)
func_1974_call = mod.get_global_var('func_1974')
func_1976_call = mutated_mod.get_global_var('func_1976')
call_2418 = relay.TupleGetItem(func_1974_call(), 0)
call_2419 = relay.TupleGetItem(func_1976_call(), 0)
bop_2422 = relay.multiply(bop_2411.astype('uint32'), relay.reshape(bop_2401.astype('uint32'), relay.shape_of(bop_2411))) # shape=(7, 3, 6)
uop_2436 = relay.log(call_2406.astype('float32')) # shape=(13, 5, 9)
uop_2438 = relay.log(call_2407.astype('float32')) # shape=(13, 5, 9)
bop_2441 = relay.subtract(uop_2436.astype('uint64'), relay.reshape(call_2418.astype('uint64'), relay.shape_of(uop_2436))) # shape=(13, 5, 9)
bop_2444 = relay.subtract(uop_2438.astype('uint64'), relay.reshape(call_2419.astype('uint64'), relay.shape_of(uop_2438))) # shape=(13, 5, 9)
func_1889_call = mod.get_global_var('func_1889')
func_1892_call = mutated_mod.get_global_var('func_1892')
var_2449 = relay.var("var_2449", dtype = "float64", shape = (5, 40))#candidate|2449|(5, 40)|var|float64
call_2448 = relay.TupleGetItem(func_1889_call(relay.reshape(var_2449.astype('float64'), [200,])), 3)
call_2450 = relay.TupleGetItem(func_1892_call(relay.reshape(var_2449.astype('float64'), [200,])), 3)
output = relay.Tuple([bop_2422,bop_2441,call_2448,var_2449,])
output2 = relay.Tuple([bop_2422,bop_2444,call_2450,var_2449,])
func_2451 = relay.Function([var_2400,var_2449,], output)
mod['func_2451'] = func_2451
mod = relay.transform.InferType()(mod)
var_2452 = relay.var("var_2452", dtype = "uint16", shape = (7, 3, 6))#candidate|2452|(7, 3, 6)|var|uint16
var_2453 = relay.var("var_2453", dtype = "float64", shape = (5, 40))#candidate|2453|(5, 40)|var|float64
output = func_2451(var_2452,var_2453,)
func_2454 = relay.Function([var_2452,var_2453,], output)
mutated_mod['func_2454'] = func_2454
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1927_call = mod.get_global_var('func_1927')
func_1928_call = mutated_mod.get_global_var('func_1928')
call_2456 = func_1927_call()
call_2457 = func_1927_call()
output = call_2456
output2 = call_2457
func_2461 = relay.Function([], output)
mod['func_2461'] = func_2461
mod = relay.transform.InferType()(mod)
output = func_2461()
func_2462 = relay.Function([], output)
mutated_mod['func_2462'] = func_2462
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2283_call = mod.get_global_var('func_2283')
func_2285_call = mutated_mod.get_global_var('func_2285')
call_2479 = relay.TupleGetItem(func_2283_call(), 0)
call_2480 = relay.TupleGetItem(func_2285_call(), 0)
var_2487 = relay.var("var_2487", dtype = "bool", shape = (9, 4, 16))#candidate|2487|(9, 4, 16)|var|bool
bop_2488 = relay.mod(call_2479.astype('float32'), relay.reshape(var_2487.astype('float32'), relay.shape_of(call_2479))) # shape=(9, 4, 16)
bop_2491 = relay.mod(call_2480.astype('float32'), relay.reshape(var_2487.astype('float32'), relay.shape_of(call_2480))) # shape=(9, 4, 16)
output = bop_2488
output2 = bop_2491
func_2505 = relay.Function([var_2487,], output)
mod['func_2505'] = func_2505
mod = relay.transform.InferType()(mod)
mutated_mod['func_2505'] = func_2505
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2506 = relay.var("var_2506", dtype = "bool", shape = (9, 4, 16))#candidate|2506|(9, 4, 16)|var|bool
func_2505_call = mutated_mod.get_global_var('func_2505')
call_2507 = func_2505_call(var_2506)
output = call_2507
func_2508 = relay.Function([var_2506], output)
mutated_mod['func_2508'] = func_2508
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1758_call = mod.get_global_var('func_1758')
func_1759_call = mutated_mod.get_global_var('func_1759')
call_2510 = func_1758_call()
call_2511 = func_1758_call()
func_2019_call = mod.get_global_var('func_2019')
func_2022_call = mutated_mod.get_global_var('func_2022')
call_2512 = relay.TupleGetItem(func_2019_call(relay.reshape(call_2510.astype('float32'), [13, 5, 9])), 0)
call_2513 = relay.TupleGetItem(func_2022_call(relay.reshape(call_2510.astype('float32'), [13, 5, 9])), 0)
output = relay.Tuple([call_2510,call_2512,])
output2 = relay.Tuple([call_2511,call_2513,])
func_2515 = relay.Function([], output)
mod['func_2515'] = func_2515
mod = relay.transform.InferType()(mod)
output = func_2515()
func_2516 = relay.Function([], output)
mutated_mod['func_2516'] = func_2516
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2235_call = mod.get_global_var('func_2235')
func_2236_call = mutated_mod.get_global_var('func_2236')
call_2612 = relay.TupleGetItem(func_2235_call(), 0)
call_2613 = relay.TupleGetItem(func_2236_call(), 0)
func_2515_call = mod.get_global_var('func_2515')
func_2516_call = mutated_mod.get_global_var('func_2516')
call_2636 = relay.TupleGetItem(func_2515_call(), 1)
call_2637 = relay.TupleGetItem(func_2516_call(), 1)
func_1546_call = mod.get_global_var('func_1546')
func_1549_call = mutated_mod.get_global_var('func_1549')
var_2643 = relay.var("var_2643", dtype = "uint8", shape = (1, 169))#candidate|2643|(1, 169)|var|uint8
const_2644 = relay.const([True,True,True,True,False,False,False,False,True,True,False,False,False,False,True,False,False,False,False,True,True,True,False,True,False,True,False,True,True,True,False,False,False,True,True,True,False,True,True,True,False,False,True,True,False,False,True,True,False,True,False,True,True,False,False,True,False,True,False,True,False,False,True,False,True,True,True,True,False,True,True,True,True,False,False,True,True,True,False,True,True,False,True,False,True,True,True,True,False,True,False,False,True,True,True,False,False,False,False,True,True,True,False,False,True,False,False,False,True,False,False,False,True,True,False,False,False,True,True,True,False,True,True,True,False,False,False,True,True,False,False,False,True,False,True,False,False,True,True,True,True,True,False,False,False,False,False,False,False,True,True,False,False,True,False,True,True,False,False,False,False,False,True,True,False,False,True,False,True,False,True,False,True,True,True,True,False,True,False,False,True,True,False,True,False,False,False,False,False,False,False,False,False,True,True,False,True,True,False,False,True,False,True,True,True,False,False,True,True,False,True,False,False,False,False,False,False,False,False,True,True,True,True,True,False,True,False,False,False,False,False,True,False,True,False,False,True,True,True,True,True,True,True,True,True,True,False,True,False,False,False,True,True,False,False,False,True,False,False,True,True,False,False,True,False,True,True,True,False,True,False,True,False,False,True,True,True,True,False,True,True,True,False,True,True,True,True,False,True,True,True,False,True,True,False,True,False,True,True,False,False,True,False,False,True,True,True,True,False,False,False,True,True,True,False,False,False,True,False,True,False,True,False,False,False,False,True,True,True,False,True,False,False,True,False,True,False,False,False,False,False,True,False,True,False,False,True,False,False,True,True,False,False,True,False,False,True,False,True,True,False,True,True,False,False,True,False,True,True,False,True,True,True,True,False,True,False,True,True,False,False,True,False,False,False,True,True,False,True,False,True,True,True,False,False,False,True,False,True,True,False,False,False,False,False,True,True,False,False,True,False,True,False,False,True,False,True,False,False,False,True,True,False,False,True,False,False,True,False,True,False,False,False,False,False,False,True,False,False,False,True,False,True,True,False,False,True,False,True,False,False,False,True,False,False,True,False,True,False,False,False,False,True,False,False,True,False,False,True,False,False,False,False,True,True,True,True,True,True,False,True,True,False,False,False,True,True,False,False,True,True,False,True,False,True,False,True,True,False,True,False,False,True,False,True,True,True,False,False,False,True,True,False,True,True,False,False,True,False,False,False,True,True,False,True,False,False,True,True,False,False,True,False,True,False,True,False,True,True,False,False,False,True,False,False,True,False,False,False,False,True,False,False,False,False,True,False,False,False,True,False,False,True,False,False,True,True,False,False,True,True,False,True,False,False,True], dtype = "bool")#candidate|2644|(576,)|const|bool
call_2642 = relay.TupleGetItem(func_1546_call(relay.reshape(var_2643.astype('uint8'), [169,]), relay.reshape(const_2644.astype('bool'), [576,]), ), 5)
call_2645 = relay.TupleGetItem(func_1549_call(relay.reshape(var_2643.astype('uint8'), [169,]), relay.reshape(const_2644.astype('bool'), [576,]), ), 5)
func_1393_call = mod.get_global_var('func_1393')
func_1394_call = mutated_mod.get_global_var('func_1394')
call_2646 = relay.TupleGetItem(func_1393_call(), 0)
call_2647 = relay.TupleGetItem(func_1394_call(), 0)
output = relay.Tuple([call_2612,call_2636,call_2642,var_2643,const_2644,call_2646,])
output2 = relay.Tuple([call_2613,call_2637,call_2645,var_2643,const_2644,call_2647,])
func_2649 = relay.Function([var_2643,], output)
mod['func_2649'] = func_2649
mod = relay.transform.InferType()(mod)
mutated_mod['func_2649'] = func_2649
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2650 = relay.var("var_2650", dtype = "uint8", shape = (1, 169))#candidate|2650|(1, 169)|var|uint8
func_2649_call = mutated_mod.get_global_var('func_2649')
call_2651 = func_2649_call(var_2650)
output = call_2651
func_2652 = relay.Function([var_2650], output)
mutated_mod['func_2652'] = func_2652
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1801_call = mod.get_global_var('func_1801')
func_1802_call = mutated_mod.get_global_var('func_1802')
call_2683 = func_1801_call()
call_2684 = func_1801_call()
func_553_call = mod.get_global_var('func_553')
func_556_call = mutated_mod.get_global_var('func_556')
var_2689 = relay.var("var_2689", dtype = "float64", shape = (200,))#candidate|2689|(200,)|var|float64
call_2688 = func_553_call(relay.reshape(var_2689.astype('float64'), [8, 5, 5]))
call_2690 = func_553_call(relay.reshape(var_2689.astype('float64'), [8, 5, 5]))
func_2115_call = mod.get_global_var('func_2115')
func_2116_call = mutated_mod.get_global_var('func_2116')
call_2721 = relay.TupleGetItem(func_2115_call(), 6)
call_2722 = relay.TupleGetItem(func_2116_call(), 6)
func_1927_call = mod.get_global_var('func_1927')
func_1928_call = mutated_mod.get_global_var('func_1928')
call_2726 = func_1927_call()
call_2727 = func_1927_call()
output = relay.Tuple([call_2683,call_2688,var_2689,call_2721,call_2726,])
output2 = relay.Tuple([call_2684,call_2690,var_2689,call_2722,call_2727,])
func_2729 = relay.Function([var_2689,], output)
mod['func_2729'] = func_2729
mod = relay.transform.InferType()(mod)
var_2730 = relay.var("var_2730", dtype = "float64", shape = (200,))#candidate|2730|(200,)|var|float64
output = func_2729(var_2730)
func_2731 = relay.Function([var_2730], output)
mutated_mod['func_2731'] = func_2731
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1424_call = mod.get_global_var('func_1424')
func_1426_call = mutated_mod.get_global_var('func_1426')
call_2733 = relay.TupleGetItem(func_1424_call(), 0)
call_2734 = relay.TupleGetItem(func_1426_call(), 0)
output = relay.Tuple([call_2733,])
output2 = relay.Tuple([call_2734,])
func_2735 = relay.Function([], output)
mod['func_2735'] = func_2735
mod = relay.transform.InferType()(mod)
output = func_2735()
func_2736 = relay.Function([], output)
mutated_mod['func_2736'] = func_2736
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2317_call = mod.get_global_var('func_2317')
func_2318_call = mutated_mod.get_global_var('func_2318')
call_2761 = func_2317_call()
call_2762 = func_2317_call()
uop_2766 = relay.sigmoid(call_2761.astype('float32')) # shape=(576,)
uop_2768 = relay.sigmoid(call_2762.astype('float32')) # shape=(576,)
func_1618_call = mod.get_global_var('func_1618')
func_1621_call = mutated_mod.get_global_var('func_1621')
const_2773 = relay.const([-7.808876,2.258785,0.115177,9.824558,-5.984331,-1.891290,5.624433,5.154803,4.102002,-6.499055,3.284357,-0.437410,-5.742685,-6.557964,-0.756210,-2.081721,-3.422017,6.350677,2.423274,1.952852,9.281611,-9.011362,-4.930811,-1.766344,5.516716,-7.656900,1.480277,-8.632628,4.396781,5.669206,-9.459347,9.477889,5.766153,-5.602562,6.976029,9.271675,1.207116,8.027055,5.138539,3.449449,-2.989539,-7.847324,-6.468080,4.888089,6.154143,-3.952701,6.603858,5.159705,-5.232654,3.736527,5.352054,-7.065476,-7.028745,-4.139519,2.788959,-5.099283,9.944907,8.315128,1.990956,-7.336250,6.327118,0.677834,-1.547058,-3.554002,-7.706774,-0.861069,-4.759775,5.398179,4.649312,-0.511735,8.561283,-0.285833,9.094485,5.813556,1.978624,-6.556350,-0.153442,6.348510,-1.101995,7.744057,7.413813,-9.885077,-6.567418,-4.012236,0.276551,2.290050,9.922390,9.957797,7.044710,-5.138655,-5.187448,-1.526109,-2.722048,4.131518,3.249841,0.260204,7.416241,-9.704715,3.935331,0.564671,0.307673,-6.415733,-3.628117,-2.527402,-7.594086,-0.010746,5.125669,2.204414,-6.076067,-8.661225,6.761286,-5.234304,1.242986,-5.604264,7.418947,5.547759,-6.352923,-3.948491,0.034524,5.739648,3.564983,5.006290,-5.958498,-0.401942,8.151941,-4.349257,-9.227472,3.773064,7.978917,7.169781,7.161425,3.843314,-5.490543,4.733363,-9.017971,5.625053,-9.203922,-5.833366,0.681435,-5.905097,7.065267,0.016772,8.273923,1.736158,-5.986993,-6.112085,7.588090,-4.284903,9.768779,-6.581063,-8.627589,6.561778,-2.062936,5.320756,-7.009729,-5.824282,-7.506471,7.656795,0.601261,-9.329521,4.399678,4.164996,-8.668189,-7.559314,9.721151,-4.967760,-0.268747,5.215192,3.245177,-9.201906,-0.545686,-2.813776,-5.846637,-3.431126,-2.653276,-4.244720,0.142784,8.882113,5.880583,1.631467,-7.227235,-5.941814,8.995504,5.478397,-9.221703,-2.482654,-0.520861,0.330224,0.396233,-7.950475,-0.376140,4.792330,9.604508,8.393366,3.265111,1.427342,-0.977108,-4.771587,8.241393,0.112516], dtype = "float64")#candidate|2773|(200,)|const|float64
call_2772 = relay.TupleGetItem(func_1618_call(relay.reshape(const_2773.astype('float64'), [5, 40])), 1)
call_2774 = relay.TupleGetItem(func_1621_call(relay.reshape(const_2773.astype('float64'), [5, 40])), 1)
output = relay.Tuple([uop_2766,call_2772,const_2773,])
output2 = relay.Tuple([uop_2768,call_2774,const_2773,])
func_2778 = relay.Function([], output)
mod['func_2778'] = func_2778
mod = relay.transform.InferType()(mod)
output = func_2778()
func_2779 = relay.Function([], output)
mutated_mod['func_2779'] = func_2779
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2317_call = mod.get_global_var('func_2317')
func_2318_call = mutated_mod.get_global_var('func_2318')
call_2803 = func_2317_call()
call_2804 = func_2317_call()
output = relay.Tuple([call_2803,])
output2 = relay.Tuple([call_2804,])
func_2806 = relay.Function([], output)
mod['func_2806'] = func_2806
mod = relay.transform.InferType()(mod)
mutated_mod['func_2806'] = func_2806
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2806_call = mutated_mod.get_global_var('func_2806')
call_2807 = func_2806_call()
output = call_2807
func_2808 = relay.Function([], output)
mutated_mod['func_2808'] = func_2808
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2819 = relay.var("var_2819", dtype = "float32", shape = (9, 4, 8))#candidate|2819|(9, 4, 8)|var|float32
uop_2820 = relay.log2(var_2819.astype('float32')) # shape=(9, 4, 8)
uop_2822 = relay.asinh(var_2819.astype('float64')) # shape=(9, 4, 8)
bop_2836 = relay.greater_equal(var_2819.astype('bool'), relay.reshape(uop_2822.astype('bool'), relay.shape_of(var_2819))) # shape=(9, 4, 8)
uop_2844 = relay.atan(uop_2822.astype('float32')) # shape=(9, 4, 8)
func_1424_call = mod.get_global_var('func_1424')
func_1426_call = mutated_mod.get_global_var('func_1426')
call_2846 = relay.TupleGetItem(func_1424_call(), 1)
call_2847 = relay.TupleGetItem(func_1426_call(), 1)
uop_2848 = relay.sqrt(uop_2820.astype('float64')) # shape=(9, 4, 8)
func_553_call = mod.get_global_var('func_553')
func_556_call = mutated_mod.get_global_var('func_556')
const_2860 = relay.const([3.864881,-0.085184,-4.575889,9.883378,0.355938,7.078095,-7.736802,6.157343,-6.433015,4.019398,-9.208538,-1.955835,2.295775,6.020824,-2.750549,3.007648,-6.738740,8.544081,8.607064,-9.141398,-7.824834,-1.606221,-4.616041,6.583397,2.396745,-8.561381,2.512418,-7.554584,-9.453480,2.203518,-4.362268,-6.642273,-9.799156,7.180274,-3.902482,8.170453,5.717596,5.406589,7.651405,-5.903474,0.346355,-6.191916,-5.330064,-0.764838,-5.844136,5.009818,-2.903349,1.056222,-7.445365,-2.852733,-5.908030,6.506571,3.144405,8.203984,8.165651,7.464342,-3.220275,-0.213320,-4.377274,1.611502,-1.038684,-8.703910,3.070651,-7.781576,-4.984039,-3.030186,-9.892969,6.277449,8.533537,-5.628728,-0.997100,1.952026,0.485159,6.054953,-0.477258,9.180284,-7.460409,3.017922,5.280549,3.333286,-5.443669,3.046882,9.516958,-9.797712,3.574663,-7.128513,-1.022267,8.372360,8.349254,-4.689012,2.047513,-8.021064,8.689888,5.559361,4.292185,-9.749010,6.216655,-1.367457,-3.474751,8.815397,2.282778,-5.881118,9.684523,-3.672514,-2.880248,2.906092,-8.249252,9.902266,2.017986,-2.240815,0.394598,7.163662,-2.999505,-1.243297,-5.074640,9.812221,3.504272,-9.915764,9.891918,5.795539,4.491575,0.574066,-2.910515,7.875979,-9.860477,1.113125,-0.273078,-3.116162,-4.024320,-1.232437,-7.739958,7.683455,3.027145,-2.303044,-1.195797,-8.318746,-5.169855,0.430431,3.182203,1.316289,-2.914457,1.913489,9.542056,-6.331252,-7.676354,-9.726999,-8.979890,-6.858134,8.870319,-9.259870,-9.963582,6.434582,-9.480978,-7.912987,7.837344,4.079090,-6.691361,9.914675,-3.512988,0.379176,-9.711692,4.308897,8.789636,-1.119479,0.305395,-6.911655,1.130274,-0.091493,-0.754765,9.297491,-4.482648,-4.847652,-6.457202,-5.516934,7.824636,9.824517,-9.147888,-0.491150,0.455043,-7.927442,1.780546,-8.199160,5.064401,-8.358685,0.629587,3.757522,3.836297,-9.182109,8.006870,-6.900601,2.371687,-4.152489,6.193483,6.295237,4.785441,0.692500,2.167049,-8.999108,-7.566551,-8.866015], dtype = "float64")#candidate|2860|(200,)|const|float64
call_2859 = func_553_call(relay.reshape(const_2860.astype('float64'), [8, 5, 5]))
call_2861 = func_553_call(relay.reshape(const_2860.astype('float64'), [8, 5, 5]))
output = relay.Tuple([bop_2836,uop_2844,call_2846,uop_2848,call_2859,const_2860,])
output2 = relay.Tuple([bop_2836,uop_2844,call_2847,uop_2848,call_2861,const_2860,])
func_2886 = relay.Function([var_2819,], output)
mod['func_2886'] = func_2886
mod = relay.transform.InferType()(mod)
var_2887 = relay.var("var_2887", dtype = "float32", shape = (9, 4, 8))#candidate|2887|(9, 4, 8)|var|float32
output = func_2886(var_2887)
func_2888 = relay.Function([var_2887], output)
mutated_mod['func_2888'] = func_2888
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1575_call = mod.get_global_var('func_1575')
func_1576_call = mutated_mod.get_global_var('func_1576')
call_2912 = func_1575_call()
call_2913 = func_1575_call()
var_2915 = relay.var("var_2915", dtype = "float64", shape = (13, 5, 9))#candidate|2915|(13, 5, 9)|var|float64
bop_2916 = relay.equal(call_2912.astype('bool'), relay.reshape(var_2915.astype('bool'), relay.shape_of(call_2912))) # shape=(13, 5, 9)
bop_2919 = relay.equal(call_2913.astype('bool'), relay.reshape(var_2915.astype('bool'), relay.shape_of(call_2913))) # shape=(13, 5, 9)
func_2451_call = mod.get_global_var('func_2451')
func_2454_call = mutated_mod.get_global_var('func_2454')
const_2928 = relay.const([-7,-6,6,4,3,4,-8,-6,-5,-2,-4,-3,-1,-4,-8,8,-1,-10,4,-7,-3,-4,3,1,-10,5,9,-9,-10,-5,1,6,6,1,9,10,-2,10,-4,-5,3,-8,-8,5,1,8,3,-4,-9,2,-4,9,-5,-1,-1,-5,4,1,8,2,7,-1,-4,-1,9,-3,4,-7,3,1,-4,-2,-8,2,8,5,-4,6,-1,-10,-2,3,5,8,10,5,4,4,-10,-7,-2,4,1,3,10,-4,6,-10,-7,-10,6,1,-3,-1,3,1,-4,-1,-6,-9,-8,1,-10,5,-7,-4,-10,-2,-2,-4,-5,-2,10,6,-8,6], dtype = "uint16")#candidate|2928|(126,)|const|uint16
const_2929 = relay.const([5.046937,4.230723,-5.187320,0.865984,8.007661,-6.847864,4.738477,-4.863941,-2.620299,-1.238580,-7.405767,5.260748,-6.905875,8.283683,9.180875,7.198212,-5.198125,5.103006,-0.265320,-8.633645,-5.881899,6.202360,-8.112145,5.843433,-2.822791,2.324617,-3.281787,3.776779,4.681656,2.341774,5.325161,7.575440,4.484976,-3.924421,-9.050478,5.966858,4.383924,-5.436667,-0.707332,-0.436526,3.254561,1.915560,8.267719,-1.790265,4.540853,4.512131,-0.915891,3.956957,6.216885,-4.559613,-2.006453,-2.492994,-3.898068,4.958192,9.280127,4.078846,4.246008,-0.856917,-7.795253,0.467146,-3.488340,-3.666936,7.108542,-0.521958,5.942112,-6.837377,-0.864636,0.268515,9.378267,-0.380859,4.566756,-1.010895,-7.089354,3.980973,6.681585,3.271069,4.411717,1.873985,2.581604,3.400999,-8.461026,-6.855683,-9.241463,2.594176,-4.476752,-3.979038,-4.451189,-8.700201,-4.888953,1.512814,-2.729848,6.926110,-8.778771,-1.901443,0.240601,-6.756696,-8.725959,-8.047873,-1.467371,-6.327171,5.366639,-4.764533,2.497212,6.931498,-8.747117,-2.893887,2.223973,-7.790584,-3.704462,3.414878,-4.428608,1.771907,-3.633433,-7.211413,3.420759,1.342763,5.042753,-5.012398,-5.114555,-5.605979,-2.191717,6.507618,0.306453,0.472847,-9.463803,0.249502,-3.361899,1.746849,-0.710828,-1.680768,3.564935,0.290056,7.449255,0.875890,0.517119,1.887425,-4.862447,8.181187,-2.318450,8.720065,0.100602,-9.206275,0.224755,-3.357403,8.037463,-5.023296,-0.909814,2.393907,7.762428,9.475399,0.836055,8.107408,1.487913,4.178587,2.663845,-2.509345,2.447191,6.537223,6.430332,-5.561301,-3.646850,8.878022,-6.676026,-9.321844,7.470830,-7.649634,-1.175230,3.191106,-4.313333,-1.333262,2.041249,-5.389671,9.437858,-5.343659,5.291762,2.083218,6.621717,-0.267432,0.538425,4.404378,-7.436184,6.618233,8.699294,-2.764754,6.686601,-5.818650,-4.786798,2.282174,-6.027986,-2.998952,4.325426,6.082612,-9.479325,-6.352896,-0.212347,-2.941402,-0.306450,-0.588546,-1.613567,5.126181], dtype = "float64")#candidate|2929|(200,)|const|float64
call_2927 = relay.TupleGetItem(func_2451_call(relay.reshape(const_2928.astype('uint16'), [7, 3, 6]), relay.reshape(const_2929.astype('float64'), [5, 40]), ), 0)
call_2930 = relay.TupleGetItem(func_2454_call(relay.reshape(const_2928.astype('uint16'), [7, 3, 6]), relay.reshape(const_2929.astype('float64'), [5, 40]), ), 0)
output = relay.Tuple([bop_2916,call_2927,const_2928,const_2929,])
output2 = relay.Tuple([bop_2919,call_2930,const_2928,const_2929,])
func_2935 = relay.Function([var_2915,], output)
mod['func_2935'] = func_2935
mod = relay.transform.InferType()(mod)
mutated_mod['func_2935'] = func_2935
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2936 = relay.var("var_2936", dtype = "float64", shape = (13, 5, 9))#candidate|2936|(13, 5, 9)|var|float64
func_2935_call = mutated_mod.get_global_var('func_2935')
call_2937 = func_2935_call(var_2936)
output = call_2937
func_2938 = relay.Function([var_2936], output)
mutated_mod['func_2938'] = func_2938
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2317_call = mod.get_global_var('func_2317')
func_2318_call = mutated_mod.get_global_var('func_2318')
call_2955 = func_2317_call()
call_2956 = func_2317_call()
func_2729_call = mod.get_global_var('func_2729')
func_2731_call = mutated_mod.get_global_var('func_2731')
const_2960 = relay.const([-3.997095,2.572564,7.529683,2.710737,9.144601,2.060919,5.872158,-4.015112,1.294294,2.705549,-8.734534,-6.126193,-3.195691,6.409444,-2.778760,8.180374,-0.577753,-9.314440,-2.996591,1.598707,9.741136,-0.082289,0.057143,-2.802196,-7.272470,-3.136993,7.630079,-4.152037,-9.176635,-5.769049,-9.510883,9.798329,-0.996027,-7.593266,-6.051915,-2.867179,-8.067924,-9.314170,1.781713,-7.527048,7.954926,0.579325,4.394396,-4.154912,3.442339,8.320065,-4.433751,-7.062004,-9.205205,4.477518,-8.978946,-6.446679,6.045450,-9.171208,3.475304,-0.510392,4.243912,3.938060,-3.974643,-0.249363,-8.484004,4.910671,8.971121,0.563770,5.257914,-4.742648,4.177848,-3.668717,3.479181,0.884106,-1.379276,2.332657,1.181562,-0.453441,9.602190,0.248412,-6.296798,-4.623564,-1.724948,3.425731,2.112534,3.781258,-6.460659,3.819122,-0.392842,-3.038437,-6.671889,-5.577405,0.498532,9.921986,-2.577703,-7.775465,-6.878962,-6.477313,5.444101,-2.183884,3.015306,1.746518,0.673351,6.350029,6.528598,-5.934872,-3.989395,-5.145882,-9.941043,-5.571881,-6.679033,3.449462,7.855889,-5.636966,-9.125026,8.625447,-7.202870,8.612619,3.029021,-2.650486,4.877427,7.030780,9.439167,7.362985,2.464257,-9.092683,-4.846791,-0.691850,8.055577,-2.896139,2.412474,8.156573,-6.506807,-7.479853,-8.128476,5.686297,9.916063,5.841605,-6.840504,-3.880578,-3.211431,8.209721,6.899761,-3.467122,-2.571422,-6.603350,0.859434,-3.549569,-2.250130,4.093043,8.934222,-3.877469,4.913444,1.315370,-6.518050,-2.544333,0.284313,-6.904946,5.586148,7.366189,9.005412,-0.599098,-3.500303,6.569465,4.894903,9.377529,4.334620,5.670660,8.855007,-6.905415,1.780463,-9.563308,-2.162905,5.166249,0.141871,-8.298625,-0.398948,8.369632,1.787899,1.980455,-7.861928,2.291161,9.902140,-8.479471,2.851506,-8.895417,3.862723,5.802311,4.636029,-4.102353,-1.889057,-4.600525,5.172473,8.291045,-6.112485,0.228900,1.882276,-9.266436,6.439864,6.569612,9.841801,4.593943,-3.618070,-4.942276], dtype = "float64")#candidate|2960|(200,)|const|float64
call_2959 = relay.TupleGetItem(func_2729_call(relay.reshape(const_2960.astype('float64'), [200,])), 2)
call_2961 = relay.TupleGetItem(func_2731_call(relay.reshape(const_2960.astype('float64'), [200,])), 2)
func_2451_call = mod.get_global_var('func_2451')
func_2454_call = mutated_mod.get_global_var('func_2454')
var_2963 = relay.var("var_2963", dtype = "uint16", shape = (126,))#candidate|2963|(126,)|var|uint16
call_2962 = relay.TupleGetItem(func_2451_call(relay.reshape(var_2963.astype('uint16'), [7, 3, 6]), relay.reshape(const_2960.astype('float64'), [5, 40]), ), 2)
call_2964 = relay.TupleGetItem(func_2454_call(relay.reshape(var_2963.astype('uint16'), [7, 3, 6]), relay.reshape(const_2960.astype('float64'), [5, 40]), ), 2)
func_1696_call = mod.get_global_var('func_1696')
func_1699_call = mutated_mod.get_global_var('func_1699')
var_2981 = relay.var("var_2981", dtype = "float32", shape = (195, 3))#candidate|2981|(195, 3)|var|float32
call_2980 = relay.TupleGetItem(func_1696_call(relay.reshape(var_2981.astype('float32'), [13, 5, 9])), 0)
call_2982 = relay.TupleGetItem(func_1699_call(relay.reshape(var_2981.astype('float32'), [13, 5, 9])), 0)
func_2172_call = mod.get_global_var('func_2172')
func_2173_call = mutated_mod.get_global_var('func_2173')
call_2985 = relay.TupleGetItem(func_2172_call(), 1)
call_2986 = relay.TupleGetItem(func_2173_call(), 1)
output = relay.Tuple([call_2955,call_2959,const_2960,call_2962,var_2963,call_2980,var_2981,call_2985,])
output2 = relay.Tuple([call_2956,call_2961,const_2960,call_2964,var_2963,call_2982,var_2981,call_2986,])
func_2989 = relay.Function([var_2963,var_2981,], output)
mod['func_2989'] = func_2989
mod = relay.transform.InferType()(mod)
mutated_mod['func_2989'] = func_2989
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2989_call = mutated_mod.get_global_var('func_2989')
var_2991 = relay.var("var_2991", dtype = "uint16", shape = (126,))#candidate|2991|(126,)|var|uint16
var_2992 = relay.var("var_2992", dtype = "float32", shape = (195, 3))#candidate|2992|(195, 3)|var|float32
call_2990 = func_2989_call(var_2991,var_2992,)
output = call_2990
func_2993 = relay.Function([var_2991,var_2992,], output)
mutated_mod['func_2993'] = func_2993
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3053 = relay.var("var_3053", dtype = "uint16", shape = (12, 8, 11))#candidate|3053|(12, 8, 11)|var|uint16
const_3054 = relay.const([[[7,-7,2,-1,-3,6,7,1,3,-4,-1],[-9,-9,5,5,7,5,-8,-9,5,5,-3],[5,2,-8,-10,-9,1,-4,-5,6,-2,7],[8,-10,7,-4,8,6,7,8,-3,6,9],[2,10,6,-7,-3,9,7,9,-8,-1,8],[-8,-7,5,7,-5,8,5,7,-4,-8,-4],[-1,-8,-9,-3,1,5,-2,-1,-4,8,-2],[-5,6,1,-4,-10,-7,4,-9,5,8,-8]],[[-2,-7,-7,-10,7,-10,-7,-8,-8,-8,9],[3,10,-10,9,7,8,8,1,6,3,3],[-9,-9,-9,3,8,10,7,-6,-9,-6,9],[4,-1,-7,8,-2,-1,5,-9,-2,8,7],[-1,10,6,-8,-1,4,-5,-6,-3,10,-3],[-5,-5,3,8,-7,-3,-10,-6,-5,-3,10],[-3,8,7,1,-3,4,5,9,7,4,-4],[2,-5,6,-7,-3,-3,8,9,1,8,-1]],[[-3,6,-8,-2,7,2,-9,7,5,8,-2],[-9,8,4,5,8,-6,8,7,6,-1,3],[7,8,1,-1,6,4,7,-9,3,-10,4],[-3,-5,-4,-7,6,8,-7,2,1,-5,-2],[-5,7,-10,9,3,4,10,2,-4,1,-4],[10,6,6,6,-6,-10,-9,7,6,-9,-8],[8,-8,10,-6,-10,10,10,9,-5,9,7],[-8,7,6,4,-6,-4,9,-6,8,-3,-1]],[[-6,1,5,-9,-9,9,-10,-1,-9,-9,3],[-8,-2,4,7,-10,-8,-6,-2,-9,1,6],[-3,8,-6,-6,4,10,4,-3,3,-6,4],[-6,-7,7,3,1,-2,9,-5,-9,-10,-9],[4,5,-5,6,3,8,-7,7,-8,-5,7],[-10,-8,5,7,4,6,-7,-10,-2,9,2],[5,-7,8,-5,5,-9,-4,4,-6,3,8],[3,-4,-1,-5,10,-2,6,8,-7,7,-9]],[[10,-2,-2,8,-4,-9,8,-3,3,-2,10],[-9,1,1,-1,9,-4,8,8,5,1,-4],[4,-9,-1,-5,10,9,-9,-9,1,-2,1],[-10,-9,4,-8,6,-6,-8,7,9,-5,-1],[9,5,-10,-4,10,-1,-8,7,-3,-6,10],[-5,-9,-8,-3,1,9,-1,-4,1,10,2],[-6,3,-4,8,5,4,-10,-8,-1,6,-4],[10,-3,-3,2,-8,-6,10,10,-7,5,-8]],[[-4,-9,-5,5,-1,1,-6,4,2,6,3],[-10,-6,-9,-6,6,-5,-5,10,-2,-6,5],[-9,-10,3,9,-2,2,-3,8,7,-1,9],[-5,-7,3,1,-7,-9,1,3,-9,-6,4],[1,1,6,-2,-8,-7,3,-10,8,-5,4],[-10,-4,3,-1,9,9,-1,2,3,10,6],[-9,-8,-6,3,-8,9,3,2,-1,5,-1],[-8,-2,2,10,-7,-6,6,-9,4,-4,-9]],[[-6,-1,4,-8,4,7,-6,10,-8,-5,-2],[-6,9,-10,2,-2,-2,7,10,-10,-3,2],[9,3,9,-2,8,3,8,2,3,-8,8],[-1,-3,5,-10,-3,-9,6,6,-8,-6,2],[6,-3,2,4,-9,10,-5,-5,-2,-4,7],[-6,8,7,-6,-7,7,-1,-1,8,-9,-9],[-3,-1,-7,5,-5,-8,6,-6,-8,-7,10],[3,5,1,-2,-10,7,2,-8,-7,-10,5]],[[-2,-2,-5,5,-7,7,4,7,10,-2,1],[-10,-3,-2,-4,10,-2,-6,1,10,-2,9],[-7,-3,-6,-6,3,5,-5,-8,6,4,-2],[2,-6,1,-3,5,9,-9,-4,-1,10,-2],[5,-3,10,10,10,5,-6,3,7,1,7],[-2,-4,-8,8,-7,-2,5,-8,5,-9,-5],[5,4,7,9,-7,4,3,-4,-2,8,-3],[-5,8,-2,-10,-1,6,-8,-5,6,-9,1]],[[-10,5,-10,-7,5,-8,2,1,-7,-7,-10],[-6,4,-4,10,-5,4,4,2,-7,-3,-2],[-4,-7,3,-6,10,9,1,9,1,-2,5],[-7,9,-5,-2,7,8,-9,-1,6,-4,-7],[8,-6,1,4,-8,-4,8,9,-6,5,2],[5,-6,5,7,5,-10,-6,1,-9,-10,3],[-2,-7,-9,-2,-4,-4,-9,-2,-3,-4,10],[-3,8,9,5,-6,-6,-7,5,10,6,2]],[[5,4,3,-10,-5,-5,5,3,-9,10,3],[-2,9,-8,6,-2,5,8,3,-2,-10,-5],[2,8,-8,7,-8,-2,1,-1,1,7,-1],[-6,2,7,7,-9,-10,10,-7,-1,-8,-9],[-2,-5,4,-9,-6,1,4,-1,8,10,9],[7,-9,-9,9,5,10,6,-1,-1,1,4],[-8,4,7,5,6,-1,8,3,10,1,-7],[6,-2,-4,6,8,-4,-1,6,6,8,8]],[[-9,-5,8,-1,-5,-6,1,-1,9,3,10],[4,-2,10,8,-7,-9,-8,-10,-6,3,3],[-2,-2,-2,6,-1,-9,-1,-2,-9,7,-3],[4,1,10,2,1,8,6,-8,-3,1,9],[-3,2,-10,-7,-2,-6,-3,-1,10,10,3],[7,6,-10,3,2,2,5,1,-7,-5,7],[1,-4,8,-10,-9,4,-8,6,-8,7,-2],[-4,-4,-7,-5,-10,2,9,9,-5,-8,-8]],[[7,-10,-2,-5,-9,7,-1,4,-1,-2,10],[5,3,-10,10,9,-3,2,-4,-2,-5,6],[-5,2,7,-1,7,8,7,-1,7,-4,-9],[-8,3,-7,2,8,6,-5,6,-1,9,3],[7,-3,-5,7,-5,-8,8,1,-9,-7,-9],[-9,6,7,7,-3,7,-1,5,6,-6,10],[-10,-3,-8,-3,3,-1,1,-8,10,-5,9],[9,7,-6,10,6,-7,-8,-1,3,2,-5]]], dtype = "uint16")#candidate|3054|(12, 8, 11)|const|uint16
bop_3055 = relay.equal(var_3053.astype('bool'), relay.reshape(const_3054.astype('bool'), relay.shape_of(var_3053))) # shape=(12, 8, 11)
output = bop_3055
output2 = bop_3055
func_3068 = relay.Function([var_3053,], output)
mod['func_3068'] = func_3068
mod = relay.transform.InferType()(mod)
var_3069 = relay.var("var_3069", dtype = "uint16", shape = (12, 8, 11))#candidate|3069|(12, 8, 11)|var|uint16
output = func_3068(var_3069)
func_3070 = relay.Function([var_3069], output)
mutated_mod['func_3070'] = func_3070
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2317_call = mod.get_global_var('func_2317')
func_2318_call = mutated_mod.get_global_var('func_2318')
call_3080 = func_2317_call()
call_3081 = func_2317_call()
output = call_3080
output2 = call_3081
func_3090 = relay.Function([], output)
mod['func_3090'] = func_3090
mod = relay.transform.InferType()(mod)
mutated_mod['func_3090'] = func_3090
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3090_call = mutated_mod.get_global_var('func_3090')
call_3091 = func_3090_call()
output = call_3091
func_3092 = relay.Function([], output)
mutated_mod['func_3092'] = func_3092
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3116 = relay.var("var_3116", dtype = "float32", shape = (4, 8, 2))#candidate|3116|(4, 8, 2)|var|float32
uop_3117 = relay.acos(var_3116.astype('float32')) # shape=(4, 8, 2)
output = relay.Tuple([uop_3117,])
output2 = relay.Tuple([uop_3117,])
func_3122 = relay.Function([var_3116,], output)
mod['func_3122'] = func_3122
mod = relay.transform.InferType()(mod)
mutated_mod['func_3122'] = func_3122
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3123 = relay.var("var_3123", dtype = "float32", shape = (4, 8, 2))#candidate|3123|(4, 8, 2)|var|float32
func_3122_call = mutated_mod.get_global_var('func_3122')
call_3124 = func_3122_call(var_3123)
output = call_3124
func_3125 = relay.Function([var_3123], output)
mutated_mod['func_3125'] = func_3125
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2515_call = mod.get_global_var('func_2515')
func_2516_call = mutated_mod.get_global_var('func_2516')
call_3159 = relay.TupleGetItem(func_2515_call(), 0)
call_3160 = relay.TupleGetItem(func_2516_call(), 0)
output = relay.Tuple([call_3159,])
output2 = relay.Tuple([call_3160,])
func_3166 = relay.Function([], output)
mod['func_3166'] = func_3166
mod = relay.transform.InferType()(mod)
mutated_mod['func_3166'] = func_3166
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3166_call = mutated_mod.get_global_var('func_3166')
call_3167 = func_3166_call()
output = call_3167
func_3168 = relay.Function([], output)
mutated_mod['func_3168'] = func_3168
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1758_call = mod.get_global_var('func_1758')
func_1759_call = mutated_mod.get_global_var('func_1759')
call_3209 = func_1758_call()
call_3210 = func_1758_call()
output = call_3209
output2 = call_3210
func_3211 = relay.Function([], output)
mod['func_3211'] = func_3211
mod = relay.transform.InferType()(mod)
output = func_3211()
func_3212 = relay.Function([], output)
mutated_mod['func_3212'] = func_3212
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1927_call = mod.get_global_var('func_1927')
func_1928_call = mutated_mod.get_global_var('func_1928')
call_3259 = func_1927_call()
call_3260 = func_1927_call()
output = call_3259
output2 = call_3260
func_3262 = relay.Function([], output)
mod['func_3262'] = func_3262
mod = relay.transform.InferType()(mod)
output = func_3262()
func_3263 = relay.Function([], output)
mutated_mod['func_3263'] = func_3263
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1974_call = mod.get_global_var('func_1974')
func_1976_call = mutated_mod.get_global_var('func_1976')
call_3283 = relay.TupleGetItem(func_1974_call(), 0)
call_3284 = relay.TupleGetItem(func_1976_call(), 0)
output = relay.Tuple([call_3283,])
output2 = relay.Tuple([call_3284,])
func_3285 = relay.Function([], output)
mod['func_3285'] = func_3285
mod = relay.transform.InferType()(mod)
mutated_mod['func_3285'] = func_3285
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3285_call = mutated_mod.get_global_var('func_3285')
call_3286 = func_3285_call()
output = call_3286
func_3287 = relay.Function([], output)
mutated_mod['func_3287'] = func_3287
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2735_call = mod.get_global_var('func_2735')
func_2736_call = mutated_mod.get_global_var('func_2736')
call_3368 = relay.TupleGetItem(func_2735_call(), 0)
call_3369 = relay.TupleGetItem(func_2736_call(), 0)
func_2451_call = mod.get_global_var('func_2451')
func_2454_call = mutated_mod.get_global_var('func_2454')
const_3373 = relay.const([[9,3],[2,2],[-2,-4],[1,-9],[8,5],[-6,5],[5,-4],[-5,2],[-2,7],[-6,3],[3,-8],[-7,-5],[8,7],[2,7],[1,4],[8,1],[10,3],[-8,6],[6,-10],[-1,-10],[-5,-7],[10,6],[-5,-9],[-8,-4],[10,-6],[6,2],[6,-4],[6,-9],[10,-10],[8,-4],[-8,-8],[3,7],[-9,-2],[7,-4],[-3,-1],[2,-10],[4,3],[-5,6],[9,-2],[-8,-6],[3,2],[1,2],[-4,-2],[1,-1],[1,-8],[2,-10],[10,5],[-2,-4],[8,-5],[-2,2],[-8,-6],[-8,5],[-10,8],[8,3],[1,-7],[9,-7],[7,-6],[9,-9],[-6,-7],[10,4],[6,2],[-1,4],[-2,-4]], dtype = "uint16")#candidate|3373|(63, 2)|const|uint16
var_3374 = relay.var("var_3374", dtype = "float64", shape = (200,))#candidate|3374|(200,)|var|float64
call_3372 = relay.TupleGetItem(func_2451_call(relay.reshape(const_3373.astype('uint16'), [7, 3, 6]), relay.reshape(var_3374.astype('float64'), [5, 40]), ), 1)
call_3375 = relay.TupleGetItem(func_2454_call(relay.reshape(const_3373.astype('uint16'), [7, 3, 6]), relay.reshape(var_3374.astype('float64'), [5, 40]), ), 1)
func_1618_call = mod.get_global_var('func_1618')
func_1621_call = mutated_mod.get_global_var('func_1621')
call_3376 = relay.TupleGetItem(func_1618_call(relay.reshape(var_3374.astype('float64'), [5, 40])), 0)
call_3377 = relay.TupleGetItem(func_1621_call(relay.reshape(var_3374.astype('float64'), [5, 40])), 0)
func_1257_call = mod.get_global_var('func_1257')
func_1258_call = mutated_mod.get_global_var('func_1258')
call_3379 = func_1257_call()
call_3380 = func_1257_call()
output = relay.Tuple([call_3368,call_3372,const_3373,var_3374,call_3376,call_3379,])
output2 = relay.Tuple([call_3369,call_3375,const_3373,var_3374,call_3377,call_3380,])
func_3388 = relay.Function([var_3374,], output)
mod['func_3388'] = func_3388
mod = relay.transform.InferType()(mod)
mutated_mod['func_3388'] = func_3388
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3389 = relay.var("var_3389", dtype = "float64", shape = (200,))#candidate|3389|(200,)|var|float64
func_3388_call = mutated_mod.get_global_var('func_3388')
call_3390 = func_3388_call(var_3389)
output = call_3390
func_3391 = relay.Function([var_3389], output)
mutated_mod['func_3391'] = func_3391
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1424_call = mod.get_global_var('func_1424')
func_1426_call = mutated_mod.get_global_var('func_1426')
call_3393 = relay.TupleGetItem(func_1424_call(), 1)
call_3394 = relay.TupleGetItem(func_1426_call(), 1)
output = relay.Tuple([call_3393,])
output2 = relay.Tuple([call_3394,])
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
func_2283_call = mod.get_global_var('func_2283')
func_2285_call = mutated_mod.get_global_var('func_2285')
call_3455 = relay.TupleGetItem(func_2283_call(), 0)
call_3456 = relay.TupleGetItem(func_2285_call(), 0)
const_3463 = relay.const([[[False,False,False,False,True,True,True,True,True,False,True,True,True,True,True,False],[False,True,False,False,True,False,True,True,True,False,False,False,True,True,False,True],[True,False,False,False,True,True,True,False,True,False,True,False,False,False,False,False],[False,True,False,True,True,False,True,True,False,True,True,False,True,True,True,False]],[[True,True,True,False,True,False,False,False,True,True,True,True,True,True,True,True],[False,True,True,False,True,False,True,False,True,False,False,False,True,True,True,False],[True,False,False,False,False,False,False,True,True,True,False,False,True,True,False,True],[True,True,True,False,True,False,False,False,False,False,True,True,False,False,True,True]],[[False,True,True,False,True,True,False,False,True,False,True,False,False,True,True,True],[False,True,True,True,True,False,True,False,False,False,True,False,False,True,True,False],[False,False,True,False,False,True,False,True,True,True,True,True,False,False,False,False],[True,False,True,True,False,True,True,False,True,False,True,False,True,False,False,False]],[[True,True,False,True,False,False,False,False,False,True,True,False,True,False,True,True],[False,False,False,False,True,True,False,True,True,True,True,True,False,True,True,True],[True,True,False,True,True,False,True,True,True,True,False,False,True,True,True,True],[True,True,True,True,False,True,False,False,True,True,True,True,False,False,False,True]],[[True,False,True,False,False,False,False,True,True,False,True,False,True,True,True,False],[False,False,True,True,False,True,True,True,False,False,False,True,False,False,False,True],[False,True,True,False,False,True,True,True,True,False,False,False,True,True,True,False],[False,False,True,False,False,False,True,False,False,True,True,False,True,False,True,True]],[[True,False,True,True,False,False,True,True,False,True,False,False,False,True,False,False],[True,True,False,True,True,True,False,True,False,True,True,True,True,False,False,True],[False,True,False,False,True,True,False,False,False,False,False,True,True,False,True,False],[True,False,False,False,True,False,True,False,True,False,True,True,False,False,False,False]],[[True,False,True,True,False,True,True,False,True,True,True,False,True,True,False,False],[True,False,False,False,False,True,False,False,True,False,True,True,False,True,True,True],[True,False,False,True,True,True,False,False,False,True,False,True,False,True,True,True],[True,True,False,False,False,False,False,True,False,True,False,False,False,False,False,True]],[[False,False,True,False,False,True,False,False,False,True,False,True,False,True,False,True],[True,False,True,True,True,True,True,True,False,True,False,False,True,False,False,False],[False,True,False,False,False,False,True,False,True,True,True,True,False,False,True,True],[False,False,True,True,False,False,True,False,True,True,True,True,True,True,True,True]],[[False,True,False,False,True,True,False,True,False,False,False,False,False,True,False,False],[False,True,False,False,True,True,False,False,False,True,True,True,False,False,False,False],[True,False,False,True,True,True,False,True,True,False,False,True,False,False,True,False],[True,True,False,False,False,False,False,False,False,False,True,False,False,False,True,False]]], dtype = "bool")#candidate|3463|(9, 4, 16)|const|bool
bop_3464 = relay.logical_xor(call_3455.astype('uint64'), relay.reshape(const_3463.astype('uint64'), relay.shape_of(call_3455))) # shape=(9, 4, 16)
bop_3467 = relay.logical_xor(call_3456.astype('uint64'), relay.reshape(const_3463.astype('uint64'), relay.shape_of(call_3456))) # shape=(9, 4, 16)
func_2935_call = mod.get_global_var('func_2935')
func_2938_call = mutated_mod.get_global_var('func_2938')
var_3477 = relay.var("var_3477", dtype = "float64", shape = (195, 3))#candidate|3477|(195, 3)|var|float64
call_3476 = relay.TupleGetItem(func_2935_call(relay.reshape(var_3477.astype('float64'), [13, 5, 9])), 0)
call_3478 = relay.TupleGetItem(func_2938_call(relay.reshape(var_3477.astype('float64'), [13, 5, 9])), 0)
output = relay.Tuple([bop_3464,call_3476,var_3477,])
output2 = relay.Tuple([bop_3467,call_3478,var_3477,])
func_3482 = relay.Function([var_3477,], output)
mod['func_3482'] = func_3482
mod = relay.transform.InferType()(mod)
var_3483 = relay.var("var_3483", dtype = "float64", shape = (195, 3))#candidate|3483|(195, 3)|var|float64
output = func_3482(var_3483)
func_3484 = relay.Function([var_3483], output)
mutated_mod['func_3484'] = func_3484
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3532 = relay.var("var_3532", dtype = "float64", shape = (13, 16, 10))#candidate|3532|(13, 16, 10)|var|float64
uop_3533 = relay.acos(var_3532.astype('float64')) # shape=(13, 16, 10)
func_1940_call = mod.get_global_var('func_1940')
func_1941_call = mutated_mod.get_global_var('func_1941')
call_3537 = func_1940_call()
call_3538 = func_1940_call()
output = relay.Tuple([uop_3533,call_3537,])
output2 = relay.Tuple([uop_3533,call_3538,])
func_3541 = relay.Function([var_3532,], output)
mod['func_3541'] = func_3541
mod = relay.transform.InferType()(mod)
var_3542 = relay.var("var_3542", dtype = "float64", shape = (13, 16, 10))#candidate|3542|(13, 16, 10)|var|float64
output = func_3541(var_3542)
func_3543 = relay.Function([var_3542], output)
mutated_mod['func_3543'] = func_3543
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1424_call = mod.get_global_var('func_1424')
func_1426_call = mutated_mod.get_global_var('func_1426')
call_3563 = relay.TupleGetItem(func_1424_call(), 2)
call_3564 = relay.TupleGetItem(func_1426_call(), 2)
func_2649_call = mod.get_global_var('func_2649')
func_2652_call = mutated_mod.get_global_var('func_2652')
var_3576 = relay.var("var_3576", dtype = "uint8", shape = (169,))#candidate|3576|(169,)|var|uint8
call_3575 = relay.TupleGetItem(func_2649_call(relay.reshape(var_3576.astype('uint8'), [1, 169])), 0)
call_3577 = relay.TupleGetItem(func_2652_call(relay.reshape(var_3576.astype('uint8'), [1, 169])), 0)
func_3388_call = mod.get_global_var('func_3388')
func_3391_call = mutated_mod.get_global_var('func_3391')
const_3581 = relay.const([5.848914,-3.785551,-8.155587,6.886425,-3.560470,3.633895,6.166963,-4.503532,3.025959,-3.295119,1.875066,6.453424,-6.170077,3.624290,-1.923442,-3.936560,6.347240,-2.061362,-7.632138,0.198662,4.868588,-3.429711,-5.854031,-1.939090,8.938527,-7.734656,-7.345510,-9.270378,-1.766287,-2.868996,0.703915,-5.237257,6.039299,-5.626409,6.751206,7.861726,-2.315475,0.723813,-0.474312,0.690821,3.205857,3.186822,4.064100,-0.262298,0.862926,4.079553,3.029207,-6.962695,-9.683179,-4.877285,-4.808971,-1.078271,-4.388946,0.985082,2.329608,-3.314468,9.418243,-3.089643,5.584341,-3.833913,0.730655,2.706203,-1.771329,-1.848354,-7.493674,-4.169974,-3.130614,-7.697853,-2.253762,2.697296,-7.498593,-0.903158,8.720168,-8.393706,3.800843,-1.628770,-6.076011,5.946088,7.652824,-5.936998,1.015144,-7.937288,1.271453,-2.304977,-5.402651,-5.751251,7.383267,-2.542192,6.323905,-0.035433,-1.877358,-3.465460,-6.027125,8.320988,4.559179,-5.331258,-5.919865,-1.962784,4.829125,3.713463,-1.862482,-2.193758,9.988126,7.996318,7.801212,3.737814,-8.236427,7.777009,-7.805152,-4.034837,-4.086547,-2.587465,7.257347,-3.586841,6.133334,-0.994017,1.688776,0.057650,-3.467010,-1.198389,-9.238859,2.987076,3.879186,-8.491834,0.349167,2.339083,0.619599,-6.423444,-3.403224,8.332954,-3.023211,3.210991,-8.605481,-0.994769,9.167330,-5.932371,4.938747,-8.554156,-4.155619,-4.389681,2.288046,5.453005,7.267463,4.337764,6.525753,0.066440,9.083387,0.805456,1.112329,-0.571251,-7.819217,7.793835,-6.673483,-5.193184,-7.596272,-2.114096,-0.718583,-7.283407,9.935387,9.829058,-4.930911,-0.355676,-8.839283,2.814497,-2.105253,-8.527731,-3.490462,-3.319066,-4.513148,-1.416197,2.228180,-1.491127,-2.774598,3.684762,2.039562,-1.293091,3.726912,4.736786,6.041365,8.351984,-6.850186,-0.117112,4.821284,2.859652,-4.152052,-7.706343,-3.240048,4.688759,0.206053,-3.746249,-6.058390,-6.729348,7.532799,3.171587,-8.120938,-7.821306,-3.774419,-2.267217,3.020401,0.308315], dtype = "float64")#candidate|3581|(200,)|const|float64
call_3580 = relay.TupleGetItem(func_3388_call(relay.reshape(const_3581.astype('float64'), [200,])), 4)
call_3582 = relay.TupleGetItem(func_3391_call(relay.reshape(const_3581.astype('float64'), [200,])), 4)
func_2451_call = mod.get_global_var('func_2451')
func_2454_call = mutated_mod.get_global_var('func_2454')
const_3623 = relay.const([-10,-8,9,9,-3,9,3,-1,10,6,-3,5,10,6,7,4,4,-10,3,8,-4,-2,-8,-1,8,-10,-2,-10,-6,10,2,3,-7,8,2,-8,3,-3,-4,9,-2,7,-4,8,-3,-5,4,2,9,-3,-6,-9,-10,1,-7,-8,-9,-4,-1,-5,3,-1,6,-10,3,-7,-4,-7,-9,8,9,4,10,3,4,-8,-9,-6,4,1,-1,4,7,10,2,-3,-6,8,-6,-9,-10,7,-8,6,1,9,10,-7,-7,-4,-7,-9,-3,-10,10,9,-8,1,1,8,-7,-6,-2,-5,-10,-7,5,1,-5,-8,10,-6,8,-4,7,3], dtype = "uint16")#candidate|3623|(126,)|const|uint16
call_3622 = relay.TupleGetItem(func_2451_call(relay.reshape(const_3623.astype('uint16'), [7, 3, 6]), relay.reshape(const_3581.astype('float64'), [5, 40]), ), 2)
call_3624 = relay.TupleGetItem(func_2454_call(relay.reshape(const_3623.astype('uint16'), [7, 3, 6]), relay.reshape(const_3581.astype('float64'), [5, 40]), ), 2)
func_1323_call = mod.get_global_var('func_1323')
func_1324_call = mutated_mod.get_global_var('func_1324')
call_3625 = func_1323_call()
call_3626 = func_1323_call()
func_2515_call = mod.get_global_var('func_2515')
func_2516_call = mutated_mod.get_global_var('func_2516')
call_3628 = relay.TupleGetItem(func_2515_call(), 0)
call_3629 = relay.TupleGetItem(func_2516_call(), 0)
uop_3641 = relay.atanh(call_3575.astype('float64')) # shape=(13, 5, 9)
uop_3643 = relay.atanh(call_3577.astype('float64')) # shape=(13, 5, 9)
output = relay.Tuple([call_3563,var_3576,call_3580,const_3581,call_3622,const_3623,call_3625,call_3628,uop_3641,])
output2 = relay.Tuple([call_3564,var_3576,call_3582,const_3581,call_3624,const_3623,call_3626,call_3629,uop_3643,])
func_3645 = relay.Function([var_3576,], output)
mod['func_3645'] = func_3645
mod = relay.transform.InferType()(mod)
var_3646 = relay.var("var_3646", dtype = "uint8", shape = (169,))#candidate|3646|(169,)|var|uint8
output = func_3645(var_3646)
func_3647 = relay.Function([var_3646], output)
mutated_mod['func_3647'] = func_3647
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2806_call = mod.get_global_var('func_2806')
func_2808_call = mutated_mod.get_global_var('func_2808')
call_3675 = relay.TupleGetItem(func_2806_call(), 0)
call_3676 = relay.TupleGetItem(func_2808_call(), 0)
func_1801_call = mod.get_global_var('func_1801')
func_1802_call = mutated_mod.get_global_var('func_1802')
call_3686 = func_1801_call()
call_3687 = func_1801_call()
output = relay.Tuple([call_3675,call_3686,])
output2 = relay.Tuple([call_3676,call_3687,])
func_3697 = relay.Function([], output)
mod['func_3697'] = func_3697
mod = relay.transform.InferType()(mod)
output = func_3697()
func_3698 = relay.Function([], output)
mutated_mod['func_3698'] = func_3698
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3763 = relay.var("var_3763", dtype = "float64", shape = (7, 13, 6))#candidate|3763|(7, 13, 6)|var|float64
uop_3764 = relay.tan(var_3763.astype('float64')) # shape=(7, 13, 6)
bop_3775 = relay.maximum(var_3763.astype('int32'), relay.reshape(uop_3764.astype('int32'), relay.shape_of(var_3763))) # shape=(7, 13, 6)
uop_3790 = relay.atanh(uop_3764.astype('float32')) # shape=(7, 13, 6)
output = relay.Tuple([bop_3775,uop_3790,])
output2 = relay.Tuple([bop_3775,uop_3790,])
func_3793 = relay.Function([var_3763,], output)
mod['func_3793'] = func_3793
mod = relay.transform.InferType()(mod)
mutated_mod['func_3793'] = func_3793
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3794 = relay.var("var_3794", dtype = "float64", shape = (7, 13, 6))#candidate|3794|(7, 13, 6)|var|float64
func_3793_call = mutated_mod.get_global_var('func_3793')
call_3795 = func_3793_call(var_3794)
output = call_3795
func_3796 = relay.Function([var_3794], output)
mutated_mod['func_3796'] = func_3796
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2735_call = mod.get_global_var('func_2735')
func_2736_call = mutated_mod.get_global_var('func_2736')
call_3859 = relay.TupleGetItem(func_2735_call(), 0)
call_3860 = relay.TupleGetItem(func_2736_call(), 0)
output = relay.Tuple([call_3859,])
output2 = relay.Tuple([call_3860,])
func_3878 = relay.Function([], output)
mod['func_3878'] = func_3878
mod = relay.transform.InferType()(mod)
output = func_3878()
func_3879 = relay.Function([], output)
mutated_mod['func_3879'] = func_3879
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3878_call = mod.get_global_var('func_3878')
func_3879_call = mutated_mod.get_global_var('func_3879')
call_3883 = relay.TupleGetItem(func_3878_call(), 0)
call_3884 = relay.TupleGetItem(func_3879_call(), 0)
func_1974_call = mod.get_global_var('func_1974')
func_1976_call = mutated_mod.get_global_var('func_1976')
call_3890 = relay.TupleGetItem(func_1974_call(), 0)
call_3891 = relay.TupleGetItem(func_1976_call(), 0)
uop_3907 = relay.sinh(call_3883.astype('float64')) # shape=(13, 5, 9)
uop_3909 = relay.sinh(call_3884.astype('float64')) # shape=(13, 5, 9)
func_3068_call = mod.get_global_var('func_3068')
func_3070_call = mutated_mod.get_global_var('func_3070')
var_3916 = relay.var("var_3916", dtype = "uint16", shape = (1056,))#candidate|3916|(1056,)|var|uint16
call_3915 = func_3068_call(relay.reshape(var_3916.astype('uint16'), [12, 8, 11]))
call_3917 = func_3068_call(relay.reshape(var_3916.astype('uint16'), [12, 8, 11]))
func_1257_call = mod.get_global_var('func_1257')
func_1258_call = mutated_mod.get_global_var('func_1258')
call_3921 = func_1257_call()
call_3922 = func_1257_call()
output = relay.Tuple([call_3890,uop_3907,call_3915,var_3916,call_3921,])
output2 = relay.Tuple([call_3891,uop_3909,call_3917,var_3916,call_3922,])
func_3944 = relay.Function([var_3916,], output)
mod['func_3944'] = func_3944
mod = relay.transform.InferType()(mod)
var_3945 = relay.var("var_3945", dtype = "uint16", shape = (1056,))#candidate|3945|(1056,)|var|uint16
output = func_3944(var_3945)
func_3946 = relay.Function([var_3945], output)
mutated_mod['func_3946'] = func_3946
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2172_call = mod.get_global_var('func_2172')
func_2173_call = mutated_mod.get_global_var('func_2173')
call_3972 = relay.TupleGetItem(func_2172_call(), 1)
call_3973 = relay.TupleGetItem(func_2173_call(), 1)
uop_3975 = relay.rsqrt(call_3972.astype('float64')) # shape=(169,)
uop_3977 = relay.rsqrt(call_3973.astype('float64')) # shape=(169,)
output = relay.Tuple([uop_3975,])
output2 = relay.Tuple([uop_3977,])
func_3978 = relay.Function([], output)
mod['func_3978'] = func_3978
mod = relay.transform.InferType()(mod)
mutated_mod['func_3978'] = func_3978
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3978_call = mutated_mod.get_global_var('func_3978')
call_3979 = func_3978_call()
output = call_3979
func_3980 = relay.Function([], output)
mutated_mod['func_3980'] = func_3980
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2778_call = mod.get_global_var('func_2778')
func_2779_call = mutated_mod.get_global_var('func_2779')
call_3989 = relay.TupleGetItem(func_2778_call(), 0)
call_3990 = relay.TupleGetItem(func_2779_call(), 0)
uop_3999 = relay.sin(call_3989.astype('float64')) # shape=(576,)
uop_4001 = relay.sin(call_3990.astype('float64')) # shape=(576,)
func_1257_call = mod.get_global_var('func_1257')
func_1258_call = mutated_mod.get_global_var('func_1258')
call_4013 = func_1257_call()
call_4014 = func_1257_call()
output = relay.Tuple([uop_3999,call_4013,])
output2 = relay.Tuple([uop_4001,call_4014,])
func_4016 = relay.Function([], output)
mod['func_4016'] = func_4016
mod = relay.transform.InferType()(mod)
mutated_mod['func_4016'] = func_4016
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4016_call = mutated_mod.get_global_var('func_4016')
call_4017 = func_4016_call()
output = call_4017
func_4018 = relay.Function([], output)
mutated_mod['func_4018'] = func_4018
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2515_call = mod.get_global_var('func_2515')
func_2516_call = mutated_mod.get_global_var('func_2516')
call_4024 = relay.TupleGetItem(func_2515_call(), 1)
call_4025 = relay.TupleGetItem(func_2516_call(), 1)
output = relay.Tuple([call_4024,])
output2 = relay.Tuple([call_4025,])
func_4026 = relay.Function([], output)
mod['func_4026'] = func_4026
mod = relay.transform.InferType()(mod)
mutated_mod['func_4026'] = func_4026
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4026_call = mutated_mod.get_global_var('func_4026')
call_4027 = func_4026_call()
output = call_4027
func_4028 = relay.Function([], output)
mutated_mod['func_4028'] = func_4028
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2317_call = mod.get_global_var('func_2317')
func_2318_call = mutated_mod.get_global_var('func_2318')
call_4029 = func_2317_call()
call_4030 = func_2317_call()
output = relay.Tuple([call_4029,])
output2 = relay.Tuple([call_4030,])
func_4068 = relay.Function([], output)
mod['func_4068'] = func_4068
mod = relay.transform.InferType()(mod)
output = func_4068()
func_4069 = relay.Function([], output)
mutated_mod['func_4069'] = func_4069
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1302_call = mod.get_global_var('func_1302')
func_1303_call = mutated_mod.get_global_var('func_1303')
call_4091 = func_1302_call()
call_4092 = func_1302_call()
func_4016_call = mod.get_global_var('func_4016')
func_4018_call = mutated_mod.get_global_var('func_4018')
call_4101 = relay.TupleGetItem(func_4016_call(), 0)
call_4102 = relay.TupleGetItem(func_4018_call(), 0)
output = relay.Tuple([call_4091,call_4101,])
output2 = relay.Tuple([call_4092,call_4102,])
func_4107 = relay.Function([], output)
mod['func_4107'] = func_4107
mod = relay.transform.InferType()(mod)
output = func_4107()
func_4108 = relay.Function([], output)
mutated_mod['func_4108'] = func_4108
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4125 = relay.var("var_4125", dtype = "uint32", shape = (12, 6, 15))#candidate|4125|(12, 6, 15)|var|uint32
var_4126 = relay.var("var_4126", dtype = "uint32", shape = (12, 6, 15))#candidate|4126|(12, 6, 15)|var|uint32
bop_4127 = relay.greater(var_4125.astype('bool'), relay.reshape(var_4126.astype('bool'), relay.shape_of(var_4125))) # shape=(12, 6, 15)
func_2806_call = mod.get_global_var('func_2806')
func_2808_call = mutated_mod.get_global_var('func_2808')
call_4132 = relay.TupleGetItem(func_2806_call(), 0)
call_4133 = relay.TupleGetItem(func_2808_call(), 0)
func_2283_call = mod.get_global_var('func_2283')
func_2285_call = mutated_mod.get_global_var('func_2285')
call_4134 = relay.TupleGetItem(func_2283_call(), 0)
call_4135 = relay.TupleGetItem(func_2285_call(), 0)
output = relay.Tuple([bop_4127,call_4132,call_4134,])
output2 = relay.Tuple([bop_4127,call_4133,call_4135,])
func_4153 = relay.Function([var_4125,var_4126,], output)
mod['func_4153'] = func_4153
mod = relay.transform.InferType()(mod)
var_4154 = relay.var("var_4154", dtype = "uint32", shape = (12, 6, 15))#candidate|4154|(12, 6, 15)|var|uint32
var_4155 = relay.var("var_4155", dtype = "uint32", shape = (12, 6, 15))#candidate|4155|(12, 6, 15)|var|uint32
output = func_4153(var_4154,var_4155,)
func_4156 = relay.Function([var_4154,var_4155,], output)
mutated_mod['func_4156'] = func_4156
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3395_call = mod.get_global_var('func_3395')
func_3397_call = mutated_mod.get_global_var('func_3397')
call_4165 = relay.TupleGetItem(func_3395_call(), 0)
call_4166 = relay.TupleGetItem(func_3397_call(), 0)
func_4153_call = mod.get_global_var('func_4153')
func_4156_call = mutated_mod.get_global_var('func_4156')
const_4171 = relay.const([-7,-4,9,-9,1,-8,-8,6,2,6,-3,-10,-1,-7,3,9,-8,-2,4,3,-9,-8,8,9,-3,5,5,-5,10,-3,3,-3,-6,10,-6,7,-4,4,-1,1,2,-2,-9,5,8,-2,-9,-1,-2,5,6,3,9,3,4,1,-9,-3,9,-10,4,-7,-9,-8,-1,-8,6,-8,-3,-4,6,1,8,6,1,-6,9,10,4,-10,-2,4,2,-5,-5,-1,2,-6,5,-2,7,-3,-1,-6,-10,10,7,-10,-5,5,1,1,-10,-8,1,3,-7,-6,-7,1,-1,9,-2,6,-3,-9,8,10,9,3,7,1,2,2,2,-7,4,-10,7,6,-6,6,7,2,-5,9,10,-8,7,-2,-3,1,-6,-6,6,5,-8,-8,7,2,-4,6,9,4,5,-7,4,-8,7,-5,7,-5,-9,2,2,1,-5,7,2,1,7,6,6,-6,-7,5,9,8,2,5,4,-9,-5,-4,-10,-4,5,-10,3,1,7,3,8,3,3,-4,-5,7,-9,-7,-8,-8,1,1,6,-6,-9,-6,-4,7,-10,-6,3,-7,4,3,-6,-4,-9,-3,-8,5,-7,4,-3,-9,-1,-9,8,-9,9,8,-3,2,-9,8,-3,-7,-5,4,-4,-10,-9,1,5,2,2,-1,4,8,8,3,8,-4,2,2,2,-3,10,-8,4,1,2,2,5,9,7,-7,-3,9,-10,3,2,2,-10,7,2,9,-9,-10,-10,-8,-3,1,7,-3,-10,10,4,3,2,-5,7,-8,2,1,-1,8,-5,1,-10,10,5,-1,-1,1,4,10,10,10,-10,-6,9,4,-5,-7,-3,3,8,-7,8,-4,5,-8,2,7,-6,-2,8,-8,-2,6,-3,-5,4,-9,9,-7,-7,-9,2,10,10,-2,9,9,-6,-9,3,9,8,-2,-3,-1,-5,-9,8,-4,3,-5,5,-6,-9,1,2,1,-1,-5,3,5,8,-4,5,-3,3,5,-3,10,-7,-8,-2,7,4,-8,-9,7,-6,4,-9,2,-8,-10,7,5,-3,-2,-3,-8,4,8,-8,-3,-7,8,7,-10,6,-5,3,8,6,1,-3,-8,7,-2,-2,9,-1,7,-6,2,10,6,9,7,8,-5,-9,9,1,-8,4,4,4,-5,2,-4,-5,6,-8,9,3,8,9,5,-9,-6,-2,-10,4,9,-5,10,5,5,-9,1,2,-3,9,2,-4,-10,-9,-5,10,-10,-8,6,-6,-9,9,6,-1,2,-8,-5,3,9,10,6,9,-4,6,-4,-10,7,5,1,-2,-6,-7,3,8,3,-7,7,-3,-6,-8,-1,-5,10,-2,6,5,-6,-4,-4,4,-2,4,-8,-10,-8,-7,9,-7,-2,1,5,-1,-10,-4,1,4,9,-5,-7,-3,3,3,-10,2,-1,1,3,-7,-8,9,-8,-5,9,4,-4,2,-5,-3,5,-8,-10,-2,-10,6,-1,9,6,-6,5,4,7,9,8,6,7,2,2,2,3,9,-3,-3,4,5,-9,9,4,5,-9,-7,-6,8,1,1,-8,-9,-1,-1,2,-2,-6,5,10,1,-3,-8,7,1,5,-3,-4,-5,5,-10,3,-7,5,-8,2,-4,10,-5,7,-5,8,7,-2,-5,-10,5,-8,-6,-2,10,6,8,6,-10,-9,-7,-7,-7,9,-8,-10,6,-5,5,-7,-3,6,8,7,7,7,3,8,-2,5,-6,3,4,-4,-5,-1,5,-2,-1,3,4,-2,1,-8,-5,-3,7,4,-3,-10,1,-9,-3,9,7,-4,1,8,3,7,9,2,-5,9,5,8,-3,10,7,9,-3,-7,-8,10,-10,-3,8,-7,2,-3,-5,10,-10,-3,-4,-5,7,5,8,9,4,-9,7,-7,9,-5,3,-2,8,1,10,-10,7,-4,-1,-5,7,7,-7,3,4,-4,-3,-9,-4,6,-8,4,-2,-10,-3,7,-8,-4,-9,-5,-4,10,-5,-2,-3,4,-5,-7,-7,9,2,8,8,-5,10,10,8,3,2,2,-6,-5,3,5,8,9,-9,10,-10,4,6,4,-5,7,4,1,6,-10,-7,-8,-10,7,-4,7,-5,-4,7,6,6,-9,3,-2,-7,7,-9,1,1,-9,4,-1,-6,-1,-4,5,10,-2,-4,-9,9,5,2,9,3,-10,-3,7,7,-2,-2,-1,-9,-5,-9,3,2,-8,-3,8,5,4,-1,7,8,-9,6,-5,6,7,-6,-5,-8,3,-10,-9,8,-2,6,-7,9,-9,9,-10,-5,10,9,10,-8,1,3,-4,-7,2,-6,-2,-6,-7,-6,-9,6,-4,5,-2,-8,-1,-7,2,1,-7,-2,1,-9,-4,-7,-8,10,-8,6,8,-7,5,-3,-7,-2,1,-5,-3,-3,9,-7,3,-9,-2,2,-8,-8,10,9,-8,-4,-6,-3,3,-3,-8,-9,10,1,-2,-2,2,3,-3,-9,-5,4,-2,-10,5,-5,-4,1,4,-5,-6,7,7,10,-4,3,-2,1,-3,8,2,8,-10,1,-2,-10,-3,6,9,-2,-5,-2,-1,2,2,2,5,-4,-1,-1,-1,-3,10,-6,7,1,4,-10,4,9,-4,-4,10,-6,-2,8,-9,-10,2,9,-6,1,4,5,7,-6,2,2,7,-5,-4,-4,5,4,-2,7,3,-9,3,-5,-5,-1,-4,-1,10,9,10,-9,-9,-2,-5,-10,1,5,1,-2,4,3,6,-6,1,-4,-1,8,7,-1,-1,1,8,3,6,6,-9,-6,5,5,1,9,-2,4,-6,-4,-5,10,10,5,-1,8,3,6,9,-8,-1,-2,3,-4,10,10,4,-1,3,2,10,-3,3,-3,-3,3,-9,8,-3], dtype = "uint32")#candidate|4171|(1080,)|const|uint32
call_4170 = relay.TupleGetItem(func_4153_call(relay.reshape(const_4171.astype('uint32'), [12, 6, 15]), relay.reshape(const_4171.astype('uint32'), [12, 6, 15]), ), 0)
call_4172 = relay.TupleGetItem(func_4156_call(relay.reshape(const_4171.astype('uint32'), [12, 6, 15]), relay.reshape(const_4171.astype('uint32'), [12, 6, 15]), ), 0)
func_2283_call = mod.get_global_var('func_2283')
func_2285_call = mutated_mod.get_global_var('func_2285')
call_4173 = relay.TupleGetItem(func_2283_call(), 0)
call_4174 = relay.TupleGetItem(func_2285_call(), 0)
bop_4189 = relay.greater(call_4165.astype('bool'), relay.reshape(call_4173.astype('bool'), relay.shape_of(call_4165))) # shape=(9, 4, 16)
bop_4192 = relay.greater(call_4166.astype('bool'), relay.reshape(call_4174.astype('bool'), relay.shape_of(call_4166))) # shape=(9, 4, 16)
func_1546_call = mod.get_global_var('func_1546')
func_1549_call = mutated_mod.get_global_var('func_1549')
const_4194 = relay.const([[-6,7,1,4,7,8,10,2,-8,-4,-4,-2,10,5,-5,5,5,-5,-6,-10,5,-6,-1,-8,5,6,8,10,-4,-1,-3,2,10,4,8,-10,-4,-7,-5,6,6,-9,-9,-4,3,4,4,4,5,10,4,6,6,-2,8,-1,7,-1,-1,1,-2,2,3,10,5,-3,1,6,-3,-10,-6,5,3,4,-3,-9,-8,-1,-6,10,2,-10,-3,2,-5,-4,3,8,7,9,-5,-5,9,5,-6,7,-8,-2,-3,6,-5,1,-2,-4,-1,1,1,-10,-1,-4,-1,6,7,-10,-2,-8,-7,-5,-8,-9,1,-2,5,1,-8,-4,7,8,-10,4,-5,9,9,-10,-2,-5,-9,5,10,10,10,-9,-4,1,-7,5,7,-3,-7,-5,-4,-2,-7,6,5,-7,2,4,-5,1,9,-4,-8,-5,2,6,10,10,6]], dtype = "uint8")#candidate|4194|(1, 169)|const|uint8
call_4193 = relay.TupleGetItem(func_1546_call(relay.reshape(const_4194.astype('uint8'), [169,]), relay.reshape(call_4173.astype('bool'), [576,]), ), 5)
call_4195 = relay.TupleGetItem(func_1549_call(relay.reshape(const_4194.astype('uint8'), [169,]), relay.reshape(call_4173.astype('bool'), [576,]), ), 5)
func_2935_call = mod.get_global_var('func_2935')
func_2938_call = mutated_mod.get_global_var('func_2938')
call_4198 = relay.TupleGetItem(func_2935_call(relay.reshape(call_4193.astype('float64'), [13, 5, 9])), 0)
call_4199 = relay.TupleGetItem(func_2938_call(relay.reshape(call_4193.astype('float64'), [13, 5, 9])), 0)
output = relay.Tuple([call_4170,const_4171,bop_4189,call_4193,const_4194,call_4198,])
output2 = relay.Tuple([call_4172,const_4171,bop_4192,call_4195,const_4194,call_4199,])
func_4201 = relay.Function([], output)
mod['func_4201'] = func_4201
mod = relay.transform.InferType()(mod)
output = func_4201()
func_4202 = relay.Function([], output)
mutated_mod['func_4202'] = func_4202
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1424_call = mod.get_global_var('func_1424')
func_1426_call = mutated_mod.get_global_var('func_1426')
call_4242 = relay.TupleGetItem(func_1424_call(), 2)
call_4243 = relay.TupleGetItem(func_1426_call(), 2)
func_1618_call = mod.get_global_var('func_1618')
func_1621_call = mutated_mod.get_global_var('func_1621')
var_4263 = relay.var("var_4263", dtype = "float64", shape = (200,))#candidate|4263|(200,)|var|float64
call_4262 = relay.TupleGetItem(func_1618_call(relay.reshape(var_4263.astype('float64'), [5, 40])), 1)
call_4264 = relay.TupleGetItem(func_1621_call(relay.reshape(var_4263.astype('float64'), [5, 40])), 1)
output = relay.Tuple([call_4242,call_4262,var_4263,])
output2 = relay.Tuple([call_4243,call_4264,var_4263,])
func_4278 = relay.Function([var_4263,], output)
mod['func_4278'] = func_4278
mod = relay.transform.InferType()(mod)
var_4279 = relay.var("var_4279", dtype = "float64", shape = (200,))#candidate|4279|(200,)|var|float64
output = func_4278(var_4279)
func_4280 = relay.Function([var_4279], output)
mutated_mod['func_4280'] = func_4280
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1726_call = mod.get_global_var('func_1726')
func_1727_call = mutated_mod.get_global_var('func_1727')
call_4302 = func_1726_call()
call_4303 = func_1726_call()
var_4306 = relay.var("var_4306", dtype = "float32", shape = (13, 5, 9))#candidate|4306|(13, 5, 9)|var|float32
bop_4307 = relay.bitwise_xor(call_4302.astype('uint8'), relay.reshape(var_4306.astype('uint8'), relay.shape_of(call_4302))) # shape=(13, 5, 9)
bop_4310 = relay.bitwise_xor(call_4303.astype('uint8'), relay.reshape(var_4306.astype('uint8'), relay.shape_of(call_4303))) # shape=(13, 5, 9)
func_3211_call = mod.get_global_var('func_3211')
func_3212_call = mutated_mod.get_global_var('func_3212')
call_4327 = func_3211_call()
call_4328 = func_3211_call()
func_1546_call = mod.get_global_var('func_1546')
func_1549_call = mutated_mod.get_global_var('func_1549')
const_4339 = relay.const([[-9],[6],[8],[-4],[6],[-8],[-10],[10],[8],[-9],[4],[-7],[5],[10],[5],[-1],[-8],[-8],[1],[-1],[-8],[7],[9],[7],[-5],[-10],[8],[-3],[-3],[-7],[1],[-3],[-5],[7],[5],[-4],[-8],[10],[-2],[5],[-3],[-8],[4],[6],[-4],[-8],[-10],[-6],[-1],[10],[3],[-8],[7],[-8],[-7],[8],[-8],[1],[-8],[1],[-9],[-9],[-9],[-2],[7],[8],[-8],[-1],[-6],[-7],[10],[1],[10],[1],[-8],[-1],[1],[-3],[-4],[5],[-9],[-3],[9],[5],[3],[-10],[-5],[-2],[-4],[6],[5],[-8],[7],[1],[8],[-7],[8],[5],[4],[-5],[-4],[-1],[-6],[6],[5],[-2],[9],[-1],[1],[10],[-7],[-6],[6],[2],[-3],[-8],[-2],[6],[1],[-9],[-5],[-9],[1],[3],[-3],[9],[9],[-6],[-9],[5],[-7],[-9],[-2],[-8],[8],[-9],[10],[-7],[1],[3],[2],[-5],[9],[8],[-10],[-10],[-7],[-6],[7],[-10],[-3],[7],[-1],[2],[-6],[-6],[-7],[1],[-4],[4],[3],[-1],[-4],[-7],[-2],[5],[10],[-7],[-10]], dtype = "uint8")#candidate|4339|(169, 1)|const|uint8
var_4340 = relay.var("var_4340", dtype = "bool", shape = (576,))#candidate|4340|(576,)|var|bool
call_4338 = relay.TupleGetItem(func_1546_call(relay.reshape(const_4339.astype('uint8'), [169,]), relay.reshape(var_4340.astype('bool'), [576,]), ), 4)
call_4341 = relay.TupleGetItem(func_1549_call(relay.reshape(const_4339.astype('uint8'), [169,]), relay.reshape(var_4340.astype('bool'), [576,]), ), 4)
uop_4343 = relay.tan(call_4327.astype('float32')) # shape=(13, 5, 9)
uop_4345 = relay.tan(call_4328.astype('float32')) # shape=(13, 5, 9)
const_4347 = relay.const([False,False,True,False,True,False,False,True,True,True,True,True,False,True,False,True,True,False,False,True,False,False,True,False,False,False,False,False,False,True,True,True,False,False,True,True,False,True,False,False,False,False,True,False,True,True,False,False,True,False,True,False,False,False,False,False,False,False,True,True,True,False,False,True,False,True,True,False,True,True,False,True,True,False,False,True,True,False,True,True,False,True,True,False,True,True,True,False,True,False,True,False,False,True,False,False,False,True,False,True,False,True,True,False,True,True,True,False,True,False,True,True,True,False,True,True,True,False,True,False,False,False,True,False,True,True,False,True,False,True,True,False,False,False,False,True,True,True,True,False,False,True,True,True,True,False,False,True,True,True,True,True,True,False,False,False,True,False,False,True,True,True,False,True,True,False,False,False,False,False,False,False,True,True,True,False,True,False,True,False,True,True,False,True,True,False,True,True,False,True,False,False,False,False,True,True,True,False,True,True,False,True,True,True,False,False,True,False,False,True,False,False,False,False,True,True,False,False,False,True,False,True,True,False,True,False,False,False,False,True,True,False,True,False,True,True,True,True,True,True,False,False,True,False,False,False,True,True,True,False,False,True,True,True,True,False,True,True,True,False,True,False,False,False,True,False,True,False,True,True,True,True,True,True,True,True,True,False,False,False,False,False,True,True,True,True,False,True,False,True,True,True,True,True,True,False,True,True,False,False,False,False,True,True,True,False,False,False,True,True,True,True,True,False,True,True,True,True,False,False,False,True,True,True,False,True,False,False,False,False,False,False,False,False,True,True,False,True,False,True,False,True,True,False,True,False,True,True,True,True,True,True,False,False,False,False,True,False,False,True,True,True,True,True,True,False,True,True,False,True,True,False,False,False,False,True,False,True,False,True,False,True,False,False,False,False,True,True,True,True,True,False,False,False,True,True,True,False,True,True,True,False,True,True,False,False,True,False,True,True,True,False,True,True,False,True,True,True,False,False,True,True,False,True,False,False,True,True,False,False,False,False,False,True,True,False,True,False,False,True,False,True,True,True,False,True,False,True,True,False,False,False,False,False,True,False,False,False,True,True,False,True,True,False,False,False,False,False,True,False,True,True,True,False,False,True,True,False,True,False,False,True,False,False,True,False,False,False,False,True,True,True,False,False,True,True,False,False,True,True,False,False,False,False,False,False,True,True,False,False,False,True,True,False,True,True,False,False,True,True,True,False,False,False,False,True,True,False,True,False,False,False,False,False,False,False,True,True,True,True,False,True,False,True,False,False,False,False,False,True,True,True,True,True,True,True,True,False,False,False,False,False,False,False,False,False,False,True,False,False,True,False,True,True,True,True], dtype = "bool")#candidate|4347|(576,)|const|bool
bop_4348 = relay.greater_equal(var_4340.astype('bool'), relay.reshape(const_4347.astype('bool'), relay.shape_of(var_4340))) # shape=(576,)
func_2649_call = mod.get_global_var('func_2649')
func_2652_call = mutated_mod.get_global_var('func_2652')
call_4354 = relay.TupleGetItem(func_2649_call(relay.reshape(const_4339.astype('uint8'), [1, 169])), 0)
call_4355 = relay.TupleGetItem(func_2652_call(relay.reshape(const_4339.astype('uint8'), [1, 169])), 0)
output = relay.Tuple([bop_4307,call_4338,const_4339,uop_4343,bop_4348,call_4354,])
output2 = relay.Tuple([bop_4310,call_4341,const_4339,uop_4345,bop_4348,call_4355,])
func_4357 = relay.Function([var_4306,var_4340,], output)
mod['func_4357'] = func_4357
mod = relay.transform.InferType()(mod)
var_4358 = relay.var("var_4358", dtype = "float32", shape = (13, 5, 9))#candidate|4358|(13, 5, 9)|var|float32
var_4359 = relay.var("var_4359", dtype = "bool", shape = (576,))#candidate|4359|(576,)|var|bool
output = func_4357(var_4358,var_4359,)
func_4360 = relay.Function([var_4358,var_4359,], output)
mutated_mod['func_4360'] = func_4360
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4401 = relay.const([[[-3.978986,-7.166014,-6.170818,6.122207],[-8.907681,-1.350846,4.701009,-5.424228],[8.931492,-0.727679,-9.127641,7.252913],[-4.763759,2.335891,9.514316,0.840898]],[[5.369865,-7.891593,-0.481208,-5.475298],[5.954650,4.475122,-3.425627,3.342149],[0.377752,-0.066452,-8.625542,5.477961],[7.073622,-9.204601,-2.138893,-3.155609]],[[0.744901,4.530798,-9.789680,-1.023343],[-2.332238,-6.182766,6.660201,3.026117],[8.788933,0.454984,3.484117,-1.597399],[0.572732,9.568633,-3.728688,-4.998599]],[[-7.808294,6.360879,1.451035,-1.473663],[-7.883545,-8.837252,-8.148481,-7.644130],[0.409033,6.715276,-3.233466,-9.103780],[-8.232874,4.010883,2.261694,-0.529617]],[[9.131600,9.299590,-3.671098,0.106422],[-2.774897,-6.185528,5.755790,1.668848],[-3.372453,3.825838,-2.845052,9.539181],[9.604351,-5.406219,-4.699872,-1.182039]],[[-5.957716,-7.625439,9.756299,8.392184],[8.122128,-7.301091,-2.661067,-7.721401],[-4.340298,-9.622550,3.117327,-7.106136],[-3.766754,0.326108,3.522160,2.362425]],[[4.248355,-5.138786,3.344838,8.296206],[-1.946484,7.758003,3.020752,0.128153],[7.198336,-6.765391,5.849085,4.069662],[2.525753,-8.957026,-2.828264,0.914332]],[[6.568573,-4.249693,4.904185,-9.987992],[5.810379,7.352910,9.580680,-7.839395],[-0.764717,4.618096,3.851205,5.943619],[1.583213,-5.247916,0.844009,-8.081239]],[[5.785991,6.677002,-4.927395,-6.787765],[8.100815,-8.714116,1.462672,9.064686],[5.667453,1.633557,2.222548,-4.593854],[1.216579,-3.170162,-0.042685,9.511867]]], dtype = "float32")#candidate|4401|(9, 4, 4)|const|float32
uop_4402 = relay.tan(const_4401.astype('float32')) # shape=(9, 4, 4)
uop_4404 = relay.atan(uop_4402.astype('float32')) # shape=(9, 4, 4)
output = uop_4404
output2 = uop_4404
func_4419 = relay.Function([], output)
mod['func_4419'] = func_4419
mod = relay.transform.InferType()(mod)
mutated_mod['func_4419'] = func_4419
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4419_call = mutated_mod.get_global_var('func_4419')
call_4420 = func_4419_call()
output = call_4420
func_4421 = relay.Function([], output)
mutated_mod['func_4421'] = func_4421
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1726_call = mod.get_global_var('func_1726')
func_1727_call = mutated_mod.get_global_var('func_1727')
call_4481 = func_1726_call()
call_4482 = func_1726_call()
output = relay.Tuple([call_4481,])
output2 = relay.Tuple([call_4482,])
func_4488 = relay.Function([], output)
mod['func_4488'] = func_4488
mod = relay.transform.InferType()(mod)
output = func_4488()
func_4489 = relay.Function([], output)
mutated_mod['func_4489'] = func_4489
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1323_call = mod.get_global_var('func_1323')
func_1324_call = mutated_mod.get_global_var('func_1324')
call_4516 = func_1323_call()
call_4517 = func_1323_call()
output = call_4516
output2 = call_4517
func_4530 = relay.Function([], output)
mod['func_4530'] = func_4530
mod = relay.transform.InferType()(mod)
mutated_mod['func_4530'] = func_4530
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4530_call = mutated_mod.get_global_var('func_4530')
call_4531 = func_4530_call()
output = call_4531
func_4532 = relay.Function([], output)
mutated_mod['func_4532'] = func_4532
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3285_call = mod.get_global_var('func_3285')
func_3287_call = mutated_mod.get_global_var('func_3287')
call_4571 = relay.TupleGetItem(func_3285_call(), 0)
call_4572 = relay.TupleGetItem(func_3287_call(), 0)
output = relay.Tuple([call_4571,])
output2 = relay.Tuple([call_4572,])
func_4580 = relay.Function([], output)
mod['func_4580'] = func_4580
mod = relay.transform.InferType()(mod)
output = func_4580()
func_4581 = relay.Function([], output)
mutated_mod['func_4581'] = func_4581
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1940_call = mod.get_global_var('func_1940')
func_1941_call = mutated_mod.get_global_var('func_1941')
call_4652 = func_1940_call()
call_4653 = func_1940_call()
output = call_4652
output2 = call_4653
func_4665 = relay.Function([], output)
mod['func_4665'] = func_4665
mod = relay.transform.InferType()(mod)
output = func_4665()
func_4666 = relay.Function([], output)
mutated_mod['func_4666'] = func_4666
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1302_call = mod.get_global_var('func_1302')
func_1303_call = mutated_mod.get_global_var('func_1303')
call_4677 = func_1302_call()
call_4678 = func_1302_call()
output = call_4677
output2 = call_4678
func_4690 = relay.Function([], output)
mod['func_4690'] = func_4690
mod = relay.transform.InferType()(mod)
mutated_mod['func_4690'] = func_4690
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4690_call = mutated_mod.get_global_var('func_4690')
call_4691 = func_4690_call()
output = call_4691
func_4692 = relay.Function([], output)
mutated_mod['func_4692'] = func_4692
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3090_call = mod.get_global_var('func_3090')
func_3092_call = mutated_mod.get_global_var('func_3092')
call_4705 = func_3090_call()
call_4706 = func_3090_call()
output = relay.Tuple([call_4705,])
output2 = relay.Tuple([call_4706,])
func_4713 = relay.Function([], output)
mod['func_4713'] = func_4713
mod = relay.transform.InferType()(mod)
output = func_4713()
func_4714 = relay.Function([], output)
mutated_mod['func_4714'] = func_4714
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1323_call = mod.get_global_var('func_1323')
func_1324_call = mutated_mod.get_global_var('func_1324')
call_4720 = func_1323_call()
call_4721 = func_1323_call()
func_3645_call = mod.get_global_var('func_3645')
func_3647_call = mutated_mod.get_global_var('func_3647')
const_4739 = relay.const([10,3,9,-3,2,-6,10,-5,10,-7,7,-1,-5,-9,-10,3,2,-4,-1,-10,6,1,9,4,8,-8,-1,-10,-5,3,1,-5,-3,-6,8,7,-1,-2,4,2,5,-7,-8,-5,9,-10,4,-3,-6,1,-6,10,5,-10,7,-3,1,-1,8,-3,3,-5,-9,-4,-1,9,-3,7,-10,-9,10,-9,1,-3,5,-5,-1,7,-1,5,8,-9,2,9,4,6,1,6,-5,-2,-7,9,7,6,-9,-2,-4,7,9,-7,-5,9,-8,1,-6,-4,-10,-8,10,-7,-6,5,-1,7,10,5,5,-5,-10,6,7,-6,-2,-4,-8,-1,-9,6,9,-10,-5,8,8,5,-8,-4,9,-2,2,-3,-6,-7,-1,4,6,10,-8,5,10,6,1,2,7,10,9,-4,-6,-9,5,8,5,5,6,1,-10,-5,6,10,3], dtype = "uint8")#candidate|4739|(169,)|const|uint8
call_4738 = relay.TupleGetItem(func_3645_call(relay.reshape(const_4739.astype('uint8'), [169,])), 3)
call_4740 = relay.TupleGetItem(func_3647_call(relay.reshape(const_4739.astype('uint8'), [169,])), 3)
output = relay.Tuple([call_4720,call_4738,const_4739,])
output2 = relay.Tuple([call_4721,call_4740,const_4739,])
func_4748 = relay.Function([], output)
mod['func_4748'] = func_4748
mod = relay.transform.InferType()(mod)
output = func_4748()
func_4749 = relay.Function([], output)
mutated_mod['func_4749'] = func_4749
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2735_call = mod.get_global_var('func_2735')
func_2736_call = mutated_mod.get_global_var('func_2736')
call_4862 = relay.TupleGetItem(func_2735_call(), 0)
call_4863 = relay.TupleGetItem(func_2736_call(), 0)
func_1257_call = mod.get_global_var('func_1257')
func_1258_call = mutated_mod.get_global_var('func_1258')
call_4868 = func_1257_call()
call_4869 = func_1257_call()
func_4713_call = mod.get_global_var('func_4713')
func_4714_call = mutated_mod.get_global_var('func_4714')
call_4871 = relay.TupleGetItem(func_4713_call(), 0)
call_4872 = relay.TupleGetItem(func_4714_call(), 0)
func_3090_call = mod.get_global_var('func_3090')
func_3092_call = mutated_mod.get_global_var('func_3092')
call_4875 = func_3090_call()
call_4876 = func_3090_call()
func_1974_call = mod.get_global_var('func_1974')
func_1976_call = mutated_mod.get_global_var('func_1976')
call_4882 = relay.TupleGetItem(func_1974_call(), 0)
call_4883 = relay.TupleGetItem(func_1976_call(), 0)
output = relay.Tuple([call_4862,call_4868,call_4871,call_4875,call_4882,])
output2 = relay.Tuple([call_4863,call_4869,call_4872,call_4876,call_4883,])
func_4888 = relay.Function([], output)
mod['func_4888'] = func_4888
mod = relay.transform.InferType()(mod)
output = func_4888()
func_4889 = relay.Function([], output)
mutated_mod['func_4889'] = func_4889
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1575_call = mod.get_global_var('func_1575')
func_1576_call = mutated_mod.get_global_var('func_1576')
call_4893 = func_1575_call()
call_4894 = func_1575_call()
func_2019_call = mod.get_global_var('func_2019')
func_2022_call = mutated_mod.get_global_var('func_2022')
call_4897 = relay.TupleGetItem(func_2019_call(relay.reshape(call_4893.astype('float32'), [13, 5, 9])), 0)
call_4898 = relay.TupleGetItem(func_2022_call(relay.reshape(call_4893.astype('float32'), [13, 5, 9])), 0)
output = relay.Tuple([call_4893,call_4897,])
output2 = relay.Tuple([call_4894,call_4898,])
func_4901 = relay.Function([], output)
mod['func_4901'] = func_4901
mod = relay.transform.InferType()(mod)
output = func_4901()
func_4902 = relay.Function([], output)
mutated_mod['func_4902'] = func_4902
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4107_call = mod.get_global_var('func_4107')
func_4108_call = mutated_mod.get_global_var('func_4108')
call_4923 = relay.TupleGetItem(func_4107_call(), 1)
call_4924 = relay.TupleGetItem(func_4108_call(), 1)
func_2989_call = mod.get_global_var('func_2989')
func_2993_call = mutated_mod.get_global_var('func_2993')
var_4942 = relay.var("var_4942", dtype = "uint16", shape = (126,))#candidate|4942|(126,)|var|uint16
const_4943 = relay.const([-1.551839,0.709316,5.637532,6.854735,8.471754,-9.281941,-5.612154,-1.415283,-5.475532,-5.724234,-7.401947,3.406737,-4.628708,0.783224,2.206293,2.240867,4.322898,6.371249,-4.594339,0.552238,0.780903,0.765783,-7.528475,2.536935,-9.951761,-4.939748,-4.565359,-0.413742,-6.790380,-2.177987,-6.673149,-4.443246,5.355329,-3.992869,-6.561074,7.369384,4.106550,-3.777150,-3.148573,-8.938337,1.028377,0.563395,-9.966336,-6.667643,5.557389,-9.435804,2.445267,-2.933711,-5.301611,-2.070717,-6.346596,4.624643,-9.638263,-5.521835,8.510215,-1.511374,4.033151,-7.404097,5.402388,8.384272,-7.926116,-8.350985,-2.158119,-4.529452,4.665510,8.000395,-2.388922,6.391835,-9.380539,2.037248,-0.534549,-7.378747,5.378884,4.015684,-1.988830,-3.395585,-0.105102,-3.214469,4.534581,4.011508,9.268494,-5.350284,9.226631,-2.225517,0.851193,-9.734538,5.190478,-7.602044,9.640100,4.119862,-5.236071,-9.541298,-2.803320,3.878787,1.783531,-1.768790,1.560447,-5.843002,-2.362742,0.536506,-9.282429,8.781804,-4.601995,3.337746,2.543482,3.370740,-9.307845,-2.722615,-3.868272,-3.479050,6.749832,-3.410708,1.519797,0.670533,-3.756127,-6.752764,-6.013501,-4.596446,9.059391,0.839649,6.188337,-9.799653,-0.327532,-7.107048,-7.473717,3.146934,-2.845036,-1.341238,-4.813340,3.263308,-7.242980,-1.169194,-9.553186,-4.078523,-9.041040,-2.472432,-7.254509,8.180287,-8.816445,-3.778939,-9.461650,-7.385332,7.798910,-3.021661,-2.506670,-8.640626,9.921078,-4.332547,-2.167576,5.116957,-8.073202,-7.750638,-1.398497,1.306992,4.606662,6.159882,5.801490,-8.085397,2.808517,5.705499,8.099208,-0.517696,-8.317232,-8.655985,2.455082,5.645804,4.964972,7.411399,6.191138,-6.696908,-9.989443,-5.893075,3.606803,-8.516034,9.891515,7.762041,-2.448381,-5.043930,-5.068237,4.842718,-9.761313,9.094605,-1.761916,-9.463030,7.622768,-3.781120,-0.221559,-0.005596,-2.841313,-0.498348,-4.007848,-2.371337,-6.421904,4.117870,3.244315,-8.740108,8.176291,4.745276,-9.377336,5.875867,1.346311,6.596644,-7.182354,4.482923,6.507509,-7.237096,0.218037,-4.303382,0.014840,-5.674418,-8.440753,0.509051,-3.395356,1.904873,-2.389203,7.458174,-9.816332,9.712050,-9.890015,3.220039,4.492779,8.738953,-5.782237,-2.694833,0.003952,-8.323712,1.483232,8.300134,4.495405,7.734790,7.988032,1.443538,9.414722,-2.958138,9.540534,7.845041,3.996154,-4.178159,-4.386611,-5.877411,9.870043,3.276907,-9.648549,0.516971,2.757036,2.037853,7.125536,9.185793,0.163645,-5.612859,0.965746,0.604520,-5.999200,3.422117,-1.131715,-4.709812,-8.771937,5.504540,-8.580137,-1.532266,1.875939,-4.558811,-3.772595,5.102175,6.118111,5.802968,-7.239169,6.196015,-4.834052,7.484237,-4.469618,-2.447718,-7.215559,6.202688,-9.965625,-7.630474,0.633712,-0.634988,-4.955447,-3.227858,6.567882,2.935502,-2.445650,-1.075866,3.560138,-8.493467,5.115315,-4.588625,-1.628638,-6.137878,-7.765029,-1.277010,7.095097,3.096907,-2.476950,9.736276,3.003730,8.110699,-2.311269,-5.406962,-3.446448,5.681190,-1.852301,3.085733,-7.895881,5.387434,-3.005962,-3.884079,4.203950,-3.427033,4.665754,5.675614,-0.405927,8.078318,8.653215,-1.428520,-3.226697,1.944646,7.984780,1.659119,0.596540,-3.737012,-6.553696,9.485333,7.480779,4.715561,-6.138120,8.686605,-3.574599,3.589279,5.028057,7.595381,0.184796,-2.360042,1.753716,-0.751120,-2.668269,-6.814275,-0.889318,-9.405480,9.144962,-3.923744,5.172230,-2.478286,-9.490627,5.454438,4.043832,9.195379,8.046796,-8.924200,1.447245,3.884104,6.950922,-0.953631,-2.935584,9.802919,6.066693,5.952750,-8.212519,-7.670779,9.167776,-5.973896,-0.334480,1.671168,4.061998,-3.740706,5.453120,-7.953419,2.603744,-5.553415,-8.839315,-7.934933,4.409419,-7.976139,7.780258,2.647736,-5.568631,-6.214489,1.404977,-1.934859,0.014787,-0.133003,8.760757,1.174502,6.639967,-3.037566,-0.992763,7.256056,-6.477620,6.531451,-5.822817,-7.893689,-4.886932,8.686406,-5.073898,-2.123314,-2.389477,-9.479076,3.398113,4.448420,8.907388,-9.974972,-2.282037,-4.861771,1.456326,-9.790392,-6.546128,-8.043253,4.055504,-8.066982,-1.370617,5.311876,8.675006,-1.426369,-5.259255,-2.822224,6.525691,3.157226,-2.265836,-4.088614,0.081193,-9.519218,4.867570,-3.112187,-2.000816,-0.018195,7.319188,-9.850892,-8.495461,7.815770,-8.702772,-3.277897,4.527887,9.424454,3.832042,4.337304,-4.534581,-6.913535,9.482322,3.301238,-4.055418,-9.199211,7.491996,-7.479279,1.731556,-4.803423,2.870778,7.015245,-1.159404,7.097325,-8.605401,-0.393757,-6.311832,-7.625806,8.299432,3.739475,2.097848,9.979710,-2.697713,-2.915622,-5.049747,7.106825,-7.700987,-2.325439,8.705963,-2.031250,-1.797301,9.157989,-4.847514,-8.998375,7.398914,1.210938,4.980606,1.289715,-7.061502,5.408042,2.943989,8.819074,5.520476,-6.307807,5.382401,-9.768959,-3.512090,-7.583358,1.680853,-0.652010,-1.397178,-8.489406,4.472055,-3.685808,5.571404,-5.995096,-0.441704,-0.855226,1.060936,2.565589,-2.328149,-0.282605,6.110949,9.749059,-8.242145,1.178024,5.133626,-7.471006,8.428844,-1.964544,5.454795,9.308901,-1.571623,8.111122,1.069630,-8.297255,2.902822,-9.714307,1.661715,9.269462,4.504585,8.914041,-6.987805,6.606454,-3.366539,6.668263,-3.759162,5.535573,-3.310371,-3.216517,9.872671,7.308947,-5.206299,1.285658,8.481487,7.029359,6.770768,0.324497,-8.095889,-8.794291,5.398216,-1.543312,-6.937275,-8.459771,1.816295,-0.235071,-0.380583,6.084689,4.539592,-5.165982,4.545640,-7.190130,-5.271320,7.849182,-5.427219,3.399449,8.177149,-8.726924,-4.493226,-1.488500,7.265296,-6.144994,7.240399,-0.789611,3.853404,3.847330,-1.264733,4.918543,-2.403956,-3.792154,-6.182534,-2.105229,1.198074,-4.510667,7.690576,5.924543,9.965716,-6.661573,5.596381,-8.745892,-0.737013,-2.035201,2.691155,6.651765,-3.341596,-8.312760,-0.439195,-2.332839,7.018268], dtype = "float32")#candidate|4943|(585,)|const|float32
call_4941 = relay.TupleGetItem(func_2989_call(relay.reshape(var_4942.astype('uint16'), [126,]), relay.reshape(const_4943.astype('float32'), [195, 3]), ), 2)
call_4944 = relay.TupleGetItem(func_2993_call(relay.reshape(var_4942.astype('uint16'), [126,]), relay.reshape(const_4943.astype('float32'), [195, 3]), ), 2)
output = relay.Tuple([call_4923,call_4941,var_4942,const_4943,])
output2 = relay.Tuple([call_4924,call_4944,var_4942,const_4943,])
func_4945 = relay.Function([var_4942,], output)
mod['func_4945'] = func_4945
mod = relay.transform.InferType()(mod)
mutated_mod['func_4945'] = func_4945
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4946 = relay.var("var_4946", dtype = "uint16", shape = (126,))#candidate|4946|(126,)|var|uint16
func_4945_call = mutated_mod.get_global_var('func_4945')
call_4947 = func_4945_call(var_4946)
output = call_4947
func_4948 = relay.Function([var_4946], output)
mutated_mod['func_4948'] = func_4948
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4419_call = mod.get_global_var('func_4419')
func_4421_call = mutated_mod.get_global_var('func_4421')
call_5020 = func_4419_call()
call_5021 = func_4419_call()
func_1575_call = mod.get_global_var('func_1575')
func_1576_call = mutated_mod.get_global_var('func_1576')
call_5022 = func_1575_call()
call_5023 = func_1575_call()
func_4665_call = mod.get_global_var('func_4665')
func_4666_call = mutated_mod.get_global_var('func_4666')
call_5031 = func_4665_call()
call_5032 = func_4665_call()
output = relay.Tuple([call_5020,call_5022,call_5031,])
output2 = relay.Tuple([call_5021,call_5023,call_5032,])
func_5037 = relay.Function([], output)
mod['func_5037'] = func_5037
mod = relay.transform.InferType()(mod)
mutated_mod['func_5037'] = func_5037
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5037_call = mutated_mod.get_global_var('func_5037')
call_5038 = func_5037_call()
output = call_5038
func_5039 = relay.Function([], output)
mutated_mod['func_5039'] = func_5039
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1424_call = mod.get_global_var('func_1424')
func_1426_call = mutated_mod.get_global_var('func_1426')
call_5059 = relay.TupleGetItem(func_1424_call(), 6)
call_5060 = relay.TupleGetItem(func_1426_call(), 6)
uop_5061 = relay.exp(call_5059.astype('float64')) # shape=(169,)
uop_5063 = relay.exp(call_5060.astype('float64')) # shape=(169,)
bop_5070 = relay.mod(uop_5061.astype('float64'), relay.reshape(call_5059.astype('float64'), relay.shape_of(uop_5061))) # shape=(169,)
bop_5073 = relay.mod(uop_5063.astype('float64'), relay.reshape(call_5060.astype('float64'), relay.shape_of(uop_5063))) # shape=(169,)
const_5080 = relay.const([2.021313,-1.668257,-7.594533,-4.307979,-2.295593,7.989950,-9.344037,-5.975727,-9.198629,8.248365,7.621557,9.360850,-1.631582,-3.513975,8.962698,-5.184257,9.575358,-1.559769,3.786492,-5.280209,5.428323,-5.349986,3.269640,-3.342601,-2.464699,3.055219,1.810867,6.063952,8.271079,9.868125,-5.781825,0.550558,-5.888334,0.404580,-4.137178,2.993986,9.702976,-6.724149,3.239359,-0.499914,-1.514440,7.208000,-0.356360,0.256568,-5.029511,6.099392,-3.799440,1.582885,-7.345607,-2.541953,-1.386766,-7.365843,1.941044,-5.253782,4.482098,7.405784,1.111519,3.255854,7.163938,1.465894,-5.596028,-5.491873,7.647239,1.610441,-8.572676,-4.217612,-3.188127,-1.311232,9.321764,-0.998855,-3.693519,-6.998582,-1.906648,0.723349,-2.569585,-9.512250,8.727132,8.106534,-0.096874,3.066423,1.850272,2.544881,-5.304292,7.369687,3.192563,5.883795,9.503789,3.202121,3.068822,-1.058006,7.216169,-5.729074,4.199899,3.312777,4.595870,8.052625,-0.716539,-9.820255,-4.542221,3.484805,4.143792,1.533159,-1.186248,-6.453931,-8.266518,-2.457245,5.707416,-9.060377,-8.132675,-6.848928,-5.767041,-1.188411,3.232887,-9.930803,7.007959,6.047435,-3.330674,6.938593,0.183719,-9.138336,-6.883437,0.262909,-5.432891,4.867673,4.268432,-4.323536,0.378763,-4.379905,4.062433,-6.021914,-9.288036,5.832491,0.462729,-1.666481,-3.034835,-9.022178,8.902073,2.079355,7.496062,-0.208531,-0.870438,1.506840,-7.604128,-1.292110,-0.422228,-6.269785,-4.174104,6.829983,-0.123223,-3.121740,-5.007065,-6.385432,-4.792769,8.135344,-9.393354,-5.721771,-2.470928,-7.250513,-3.329753,-2.264771,0.202552,5.147502,-6.571320,1.459600,-8.278336,-2.152650,-3.281838,-7.445661,-4.572975], dtype = "float32")#candidate|5080|(169,)|const|float32
bop_5081 = relay.less(call_5059.astype('bool'), relay.reshape(const_5080.astype('bool'), relay.shape_of(call_5059))) # shape=(169,)
bop_5084 = relay.less(call_5060.astype('bool'), relay.reshape(const_5080.astype('bool'), relay.shape_of(call_5060))) # shape=(169,)
uop_5091 = relay.sinh(const_5080.astype('float64')) # shape=(169,)
bop_5097 = relay.bitwise_and(bop_5081.astype('uint8'), relay.reshape(bop_5070.astype('uint8'), relay.shape_of(bop_5081))) # shape=(169,)
bop_5100 = relay.bitwise_and(bop_5084.astype('uint8'), relay.reshape(bop_5073.astype('uint8'), relay.shape_of(bop_5084))) # shape=(169,)
func_2935_call = mod.get_global_var('func_2935')
func_2938_call = mutated_mod.get_global_var('func_2938')
const_5104 = relay.const([1.498380,-0.363121,-0.154848,9.323187,-3.512072,-6.725662,1.320923,8.638778,-1.631902,-1.796206,-1.226631,-5.026441,-1.991406,5.835380,2.182226,-5.159413,-2.925130,-0.183052,7.655384,5.134134,-3.350533,3.741717,3.374644,-1.161911,-2.724725,0.137294,-6.039252,9.369631,5.140946,-2.927801,-0.378552,9.302815,0.991911,0.842198,3.852735,-5.915748,3.446064,4.071349,-9.421194,-9.563333,8.763718,2.583561,6.624790,-0.382778,2.806327,-3.985172,7.724214,-5.116637,8.031882,-7.301652,-1.471535,-2.596622,-8.911542,-7.760448,0.224741,7.902568,-7.317297,-1.193239,6.052663,2.588840,2.457675,-9.112330,4.203047,8.625738,5.331888,-4.150620,0.862603,2.026549,-9.913339,-3.600287,-3.789935,-1.170940,4.932945,-1.812114,-4.419400,7.770193,7.158628,-1.547714,8.370193,8.643415,2.031137,-6.753837,-2.919090,-1.349189,-6.012287,0.668920,-3.116133,5.611300,-1.185151,1.509761,6.707295,0.552402,-8.951232,-6.526712,9.503142,-1.073427,2.831082,8.445031,-0.257688,-5.700842,7.070646,3.249854,-2.792369,9.115313,7.630196,1.564317,5.720894,6.959901,-1.198449,9.732620,-8.731736,8.012148,6.226605,8.945950,-9.011475,-5.051877,9.005491,-4.095261,-7.594629,3.787309,-1.953903,9.049962,1.950687,3.702119,-9.789281,1.265581,0.280352,-2.342062,-5.906216,-6.529392,8.893784,-0.973108,2.896536,-6.505020,-5.812277,1.600283,-0.947882,-7.210680,3.541477,-8.845316,7.126263,-2.361563,-2.684980,1.868431,2.489712,7.975474,-8.951373,4.395760,-4.520100,1.312747,6.889437,4.727761,5.175240,8.550214,-2.664757,-0.861524,-3.087097,-7.673574,1.390858,0.858213,8.725174,-9.207123,-9.293893,3.664911,9.829226,2.789461,5.288770,8.782076,-4.872887,-9.713007,-9.876936,-2.983765,4.346393,4.613029,-8.138094,8.955758,7.942761,4.462012,-2.970171,7.462024,-6.710871,-2.591919,9.403036,-7.817123,9.756147,-8.398243,-8.166723,-7.027140,0.238168,-9.446938,-9.898961,-5.916339,9.066952,5.775514,-1.052949,-9.131119,2.003545,8.856566,-1.785314,-9.997960,-8.473772,1.914827,-1.792866,-1.083815,0.800061,4.254360,9.264946,0.740883,-4.688560,-1.799603,6.252853,6.402295,6.529012,-3.150106,-3.409425,2.635808,6.988916,6.732001,-4.402248,-8.046239,2.611372,5.386015,5.782483,1.350134,7.792914,-7.180890,-3.221305,3.411032,-6.925512,3.533184,7.635087,4.331486,7.590420,-3.791027,6.097060,8.322770,-5.936197,2.840312,-1.832887,2.639222,-1.681884,-0.787952,2.762518,-4.789275,8.857628,6.241473,1.170264,-6.970551,8.807419,-1.108789,2.041885,8.243925,3.408754,5.453253,-0.208152,3.537323,-8.853845,7.786499,-0.643884,-0.282426,-1.029114,-6.762549,-7.578392,-8.338899,0.885520,-3.644511,9.972178,-8.843210,-7.881373,-2.934724,7.220866,7.352528,3.482495,1.152878,0.116576,-6.615086,1.778311,6.367983,9.595160,-1.111878,-7.910372,3.278487,-3.111801,-8.478194,6.836979,8.625138,3.827970,-1.864117,-0.906469,-8.518400,3.254781,1.198090,0.913876,1.114539,-7.639974,5.024809,-5.804914,-4.120722,-3.964541,-1.687474,0.158599,-3.256156,-2.366059,-4.485159,1.634974,-3.472955,1.882348,4.082751,-6.504084,5.591148,-3.040002,-8.093522,1.033164,-9.664402,8.338198,4.618227,-9.137364,0.491535,-3.848873,5.510886,-6.624220,9.646575,0.903392,-1.236436,0.643552,6.373366,-9.216638,-0.088620,-9.672678,-9.642191,6.472352,3.703218,6.629353,5.692415,-8.320712,9.649282,-9.818235,-6.059004,-3.418968,-8.881991,-0.626449,9.659142,6.493764,-2.370829,-2.444610,5.045167,-0.120090,-9.532078,-7.061160,0.928232,-7.086082,7.968886,7.016859,5.533200,3.507578,1.041974,3.339990,-9.412698,8.428729,-7.548071,7.745012,9.588623,-1.049404,-4.890019,1.821408,6.820498,-7.932906,0.175034,-9.432692,3.606426,-2.333884,5.275566,-7.601969,-5.855566,-3.495194,1.742985,-5.905243,1.909390,-9.114668,3.243319,-1.272206,-9.466281,-7.800370,-1.015425,-9.160779,-1.251852,2.313483,-5.794462,5.382551,0.966538,4.302639,-5.444209,6.134114,4.000348,8.572698,-7.071864,2.396112,-1.905283,-3.087627,0.100565,5.619408,5.409803,3.006698,-5.630550,-2.617924,3.384308,-7.761769,6.415106,1.109549,-9.043973,-6.647110,-6.997959,2.315449,9.635455,-3.427129,-6.917477,-7.675544,-3.113760,3.651845,-2.646089,-3.236363,1.448995,3.725612,-2.133856,8.416111,8.664890,1.953612,-3.204230,1.058910,-3.397324,-8.905195,9.480623,-4.323586,-0.136835,-3.362305,6.004036,-1.626363,4.193260,-8.854422,4.914577,-2.920779,0.915721,-6.065875,-7.734972,8.909871,7.264863,6.162171,-6.515021,-9.769102,7.431502,4.994871,6.376200,-0.764090,-9.210115,5.803829,-8.083877,-9.536335,9.345066,3.099999,-8.484579,1.597845,-8.169333,-4.647964,-6.017907,-3.538784,5.337340,1.074684,5.932189,-1.550731,-4.359781,9.745511,5.082943,-9.276987,4.321063,5.239245,-0.448729,9.258308,9.178726,5.004806,7.400766,-7.360644,2.149224,0.020009,8.629398,-5.836942,2.861982,-4.776270,-1.401936,-4.384777,7.368809,2.990516,-3.166455,-8.364069,8.609522,1.782891,3.229504,8.301397,3.685748,-9.434443,-3.375564,-3.853273,-7.214134,4.897933,0.445663,-1.776042,8.676465,-8.782369,3.249205,8.185133,-9.902810,2.181726,-1.070848,1.897569,8.616000,-4.340845,-2.710743,-4.785756,-5.119690,4.759205,4.907339,-0.692589,-9.145693,-4.120387,3.322133,-7.079022,-9.573107,-3.706097,-9.016708,0.333817,3.716537,-8.190383,-2.460360,-4.912755,-9.133513,9.185235,-6.289022,-0.705305,-1.261752,-5.163690,-7.084054,-8.814687,-7.352502,-5.664892,-4.893498,-3.064856,7.214337,6.817246,3.599587,-0.641181,-7.682937,6.748807,6.856377,5.573037,-2.757041,-6.926352,-9.257453,-1.316690,9.063852,9.050058,-5.958888,6.205020,-0.211731,9.332766,-1.906643,2.878888,7.882536,1.819353,-1.696518,9.383667,-7.698345,-4.621888,-0.073185,4.830876,4.966577,3.686282,5.711541,9.290422,1.743844,0.697646,3.814283,-8.436615,-0.410491,8.113374,-7.139831,8.951702], dtype = "float64")#candidate|5104|(585,)|const|float64
call_5103 = relay.TupleGetItem(func_2935_call(relay.reshape(const_5104.astype('float64'), [13, 5, 9])), 2)
call_5105 = relay.TupleGetItem(func_2938_call(relay.reshape(const_5104.astype('float64'), [13, 5, 9])), 2)
func_757_call = mod.get_global_var('func_757')
func_762_call = mutated_mod.get_global_var('func_762')
const_5111 = relay.const(8, dtype = "uint8")#candidate|5111|()|const|uint8
const_5112 = relay.const([False,True,False,False,True,False,False,True,True,True,True,True,False,False,False,True,False,True,True,True,False,True,False,False,False,False,True,False,True,True,False,False,False,True,False,False,True,False,True,False,False,False,True,False,True,True,True,True,True,False,False,True,True,False,True,False,True,True,False,False,False,True,False,True,False,False,True,True,True,False,True,True,False,True,True,True,False,False,False,True,False,True,True,False,True,False,False,False,True,False,True,False,True,True,True,True,False,False,False,True,False,False,False,False,True,True,False,True,True,False,True,True,True,False,True,True,False,True,True,False,False,False,False,True,False,True,True,False,True,True,True,True,True,True,True,False,False,True,False,True,False,True,False,True,True,False,False,True,True,False,True,True,False,True,True,False,False,False,False,True,True,True,False,True,False,False,True,False,True,True,True,True,False,False,True,True,False,True,True,True,True,False,True,False,False,False,False,False,False,True,False,True,False,False,False,True,False,False,True,False,True,True,True,False,True,False,True,True,False,False,False,True,True,True,True,True,True,False,True,True,True,True,True,True,False,True,False,False,True,False,False,True,True,False,True,False,False,False,True,False,True,True,False,False,True,True,True,False,True,False,False,False,False,True,False,False,False,False,False,False,False,True,True,True,True,False,True,True,False,False,False,True,False,False,True,True,True,False,True,True,True,True,True,True,False,True,True,True,False,True,True,False,False,False,False,True,False,True,True,False,False,True,False,False,True,True,True,False,False,False,True,True,False,True,False,False,False,True,True,False,False,False,True,True,False,True,False,False,False,True,True,False,False,True,False,True,False,True,False,False,False,True,True,False,False,True,False,True,False,False,True,True,False,False,False,True,True,False,True,False,False,False,False,False,True,True,False,False,False,False,False,False,True,False,False,False,True,True,True,False,True,False,True,True,True,True,False,False,True,False,False,True,False,True,False,False,False,False,False,False,False,False,True,True,False,True,True,False,False,False,False,True,True,True,True,False,False,True,False,True,True,True,True,False,False,True,False,False,True,False,False,True,False,True,False,True,True,False,True,True,False,True,True,True,False,False,True,False,True,False,True,True,True,False,True,True,True,True,True,False,True,True,True,True,True,False,False,False,False,True,True,False,False,False,False,False,False,True,False,False,True,False,True,False,False,False,True,False,True,False,False,False,False,False,True,True,False,False,True,False,True,False,False,False,True,False,False,True,False,True,True,True,True,False,False,True,False,True,True,True,False,False,True,False,False,True,True,False,True,False,False,False,False,False,False,True,True,True,True,True,False,False,False,True,True,False,False,True,False,False,True,False,False,False,False,False,True,True,False,False,True,False,True,True,False,True,True,True,False,False,False,False,False,True,True,True], dtype = "bool")#candidate|5112|(576,)|const|bool
var_5113 = relay.var("var_5113", dtype = "float64", shape = (200,))#candidate|5113|(200,)|var|float64
call_5110 = relay.TupleGetItem(func_757_call(relay.reshape(const_5111.astype('uint8'), []), relay.reshape(const_5080.astype('uint8'), [169,]), relay.reshape(const_5112.astype('bool'), [576,]), relay.reshape(var_5113.astype('float64'), [200,]), ), 3)
call_5114 = relay.TupleGetItem(func_762_call(relay.reshape(const_5111.astype('uint8'), []), relay.reshape(const_5080.astype('uint8'), [169,]), relay.reshape(const_5112.astype('bool'), [576,]), relay.reshape(var_5113.astype('float64'), [200,]), ), 3)
func_2886_call = mod.get_global_var('func_2886')
func_2888_call = mutated_mod.get_global_var('func_2888')
var_5118 = relay.var("var_5118", dtype = "float32", shape = (288,))#candidate|5118|(288,)|var|float32
call_5117 = relay.TupleGetItem(func_2886_call(relay.reshape(var_5118.astype('float32'), [9, 4, 8])), 3)
call_5119 = relay.TupleGetItem(func_2888_call(relay.reshape(var_5118.astype('float32'), [9, 4, 8])), 3)
func_3068_call = mod.get_global_var('func_3068')
func_3070_call = mutated_mod.get_global_var('func_3070')
var_5129 = relay.var("var_5129", dtype = "uint16", shape = (8, 132))#candidate|5129|(8, 132)|var|uint16
call_5128 = func_3068_call(relay.reshape(var_5129.astype('uint16'), [12, 8, 11]))
call_5130 = func_3068_call(relay.reshape(var_5129.astype('uint16'), [12, 8, 11]))
uop_5132 = relay.erf(bop_5097.astype('float64')) # shape=(169,)
uop_5134 = relay.erf(bop_5100.astype('float64')) # shape=(169,)
bop_5149 = relay.equal(uop_5132.astype('bool'), relay.reshape(call_5059.astype('bool'), relay.shape_of(uop_5132))) # shape=(169,)
bop_5152 = relay.equal(uop_5134.astype('bool'), relay.reshape(call_5060.astype('bool'), relay.shape_of(uop_5134))) # shape=(169,)
func_4901_call = mod.get_global_var('func_4901')
func_4902_call = mutated_mod.get_global_var('func_4902')
call_5153 = relay.TupleGetItem(func_4901_call(), 0)
call_5154 = relay.TupleGetItem(func_4902_call(), 0)
bop_5161 = relay.power(uop_5132.astype('float64'), relay.reshape(bop_5149.astype('float64'), relay.shape_of(uop_5132))) # shape=(169,)
bop_5164 = relay.power(uop_5134.astype('float64'), relay.reshape(bop_5152.astype('float64'), relay.shape_of(uop_5134))) # shape=(169,)
func_1782_call = mod.get_global_var('func_1782')
func_1784_call = mutated_mod.get_global_var('func_1784')
const_5172 = relay.const([-0.225171,7.781837,5.865883,-4.591992,4.433974,7.116466,-2.943682,4.659816,3.028061,5.526229,7.294684,-1.523515,-6.208991,-5.258105,9.120444,-9.721229,-0.494197,-6.117842,-4.427551,1.362563,-4.467008,2.752544,4.974199,5.528271,-1.553041,-8.143964,1.259315,7.173027,-5.923517,4.947388,6.765560,4.208161,3.417143,-2.317177,5.180805,9.321918,-0.737282,-6.872933,4.993122,-8.344628,-3.455743,5.904002,-4.449658,9.937030,1.766084,-8.985658,-9.475785,-0.088046,2.984559,2.877585,-9.075169,-8.407325,-6.027554,-3.324265,2.729052,9.516989,-7.200475,7.408038,1.312025,2.401358,5.511863,-6.617489,5.934538,-0.512799,0.949125,7.004622,-5.069005,-4.037424,-5.794501,9.746394,-0.858089,9.139925,3.090182,6.397963,9.300119,0.606364,-2.302386,-3.826771,-3.428893,-6.933340,4.942662,-2.117643,-3.774380,-2.900456,9.417000,-6.134445,-6.901533,-5.533292,-7.200318,-0.071104,-2.069160,-6.422126,2.987392,4.904959,6.354845,1.104149,2.792768,1.794749,2.215358,7.487087,3.978354,-0.240555,9.018236,0.063510,-6.828204,-0.567997,-5.210273,4.591714,7.000714,3.093321,-5.661545,9.814168,-3.698684,9.857077,-7.297247,3.273909,-6.978616,3.683224,-6.208335,3.443945,4.612890,-7.706220,9.771743,1.293339,-5.270560,8.565160,-1.023965,-7.750166,4.506061,-3.224858,-1.087298,6.221122,6.701831,6.333935,-2.102749,-9.877865,-0.719679,9.973990,-9.859763,-5.771594,9.687002,6.784310,7.528593,8.997816,-9.185398,-6.624239,6.777630,8.721906,5.225171,-3.536319,-6.419007,2.062446,3.726136,-7.226878,2.382283,-0.721400,-5.497004,-2.523893,-6.046974,7.179939,3.932803,6.448102,9.783733,6.839548,4.195955,-4.554856,-0.974583,-3.156317,-5.452971,7.009851,-1.901313,7.419049,-5.404953,-8.913692,5.236287,8.513749,4.989367,9.020450,4.391178,2.275722,-7.662949,-2.088488,1.552176,8.158124,1.099750,-8.883101,-1.187790,7.615947,9.402678,0.274782,4.312920,-1.243882,-7.129831,2.089841,-0.805135,-4.588648,3.861597,-0.028503,-5.085786,-1.120871,-5.099081,8.090446,-4.149335,8.674378,-4.626015,-1.367112,5.440110,-7.232556,-4.446305,-0.854942,0.108148,-4.623890,1.110598,4.784647,-5.548646,-3.494663,-4.048821,4.870482,-1.087755,8.684099,-7.720505,-5.177210,-2.876184,7.020908,-0.903239,2.456369,-2.547247,-6.430648,-7.589063,1.057035,-4.461764,-4.722674,6.756457,4.093409,-5.150612,-7.347000,8.353305,0.404046,-8.106088,-4.876571,-5.606378,-4.049105,5.776708,-3.717800,-7.415600,-5.940637,6.692690,-5.773665,0.525714,-5.868658,-0.303394,-5.675752,7.773491,8.445194,-7.529428,6.393495,5.152313,4.010760,-0.133951,4.055933,-3.152115,0.995200,-4.255585,-5.475452,-4.217245,4.974567,-6.699291,-6.564043,8.069676,2.004053,2.039528,-8.025390,-4.713341,-7.974934,-0.628471,9.003951,9.420645,-8.987783,-8.106395,0.409005,-2.155568,0.507238,-9.984454,-5.521442,9.907881,4.616201,-1.154516,-3.474667,-4.140756,-8.185300,-4.616503,4.512535,-0.413415,2.801889,-5.216480,0.379301,7.149648,5.490703,-2.554225,-2.366277,3.900216,5.620662,3.702714,-2.438688,-6.415826,-1.475198,8.719731,-8.178598,-0.599582,-8.604772,9.030856,4.044142,0.748947,-9.056602,-0.566289,9.061163,7.997607,-5.211572,-3.308480,-8.792071,4.650626,5.873705,-2.568072,-8.261573,5.407272,6.277652,6.176417,-8.622621,-6.003411,-5.467791,1.415575,-4.028098,-2.953261,8.761932,-1.552312,5.737071,2.927126,-9.585707,5.986337,-7.325542,2.946114,5.203313,-0.313746,1.777986,-0.281512,4.823203,-9.465592,-9.994413,-1.503427,4.161737,3.645514,-9.136368,-9.604656,-4.162502,-6.277602,-7.947832,1.235442,-9.619730,2.444791,-1.293816,4.905431,5.626570,7.845446,1.495920,-7.316463,-3.607657,2.355534,-7.317779,2.018659,8.789285,8.878559,-2.599080,3.867725,-7.502930,-8.904180,0.054162,-8.011690,1.303740,-4.302586,-6.845454,-6.103163,3.956492,4.004842,7.985792,-0.497917,-4.845400,-7.105555,-3.790585,6.717205,3.874080,5.640712,-0.053808,9.245550,-1.627157,-1.069733,-2.695209,6.787759,-0.916337,9.949151,-2.598798,6.863292,0.235151,8.369678,8.535951,-5.242090,-4.306010,8.560332,-0.650641,8.214330,2.306670,7.633206,-8.323444,7.017754,6.065295,-4.987092,-9.158372,6.279466,6.003599,-4.334398,3.244758,4.149342,-6.244649,-9.266877,-2.286997,9.414877,2.262102,9.379531,-3.440789,5.568773,-7.488255,1.513923,2.826320,-6.084082,6.206444,5.863400,-5.850666,-6.801627,-6.143079,9.382534,-7.163044], dtype = "float32")#candidate|5172|(440,)|const|float32
call_5171 = relay.TupleGetItem(func_1782_call(relay.reshape(const_5172.astype('float32'), [4, 10, 11])), 1)
call_5173 = relay.TupleGetItem(func_1784_call(relay.reshape(const_5172.astype('float32'), [4, 10, 11])), 1)
var_5175 = relay.var("var_5175", dtype = "float64", shape = (169,))#candidate|5175|(169,)|var|float64
bop_5176 = relay.bitwise_or(bop_5161.astype('int32'), relay.reshape(var_5175.astype('int32'), relay.shape_of(bop_5161))) # shape=(169,)
bop_5179 = relay.bitwise_or(bop_5164.astype('int32'), relay.reshape(var_5175.astype('int32'), relay.shape_of(bop_5164))) # shape=(169,)
bop_5188 = relay.divide(uop_5132.astype('float64'), relay.reshape(bop_5176.astype('float64'), relay.shape_of(uop_5132))) # shape=(169,)
bop_5191 = relay.divide(uop_5134.astype('float64'), relay.reshape(bop_5179.astype('float64'), relay.shape_of(uop_5134))) # shape=(169,)
output = relay.Tuple([uop_5091,call_5103,const_5104,call_5110,const_5111,const_5112,var_5113,call_5117,var_5118,call_5128,var_5129,call_5153,call_5171,const_5172,bop_5188,])
output2 = relay.Tuple([uop_5091,call_5105,const_5104,call_5114,const_5111,const_5112,var_5113,call_5119,var_5118,call_5130,var_5129,call_5154,call_5173,const_5172,bop_5191,])
func_5198 = relay.Function([var_5113,var_5118,var_5129,var_5175,], output)
mod['func_5198'] = func_5198
mod = relay.transform.InferType()(mod)
mutated_mod['func_5198'] = func_5198
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5198_call = mutated_mod.get_global_var('func_5198')
var_5200 = relay.var("var_5200", dtype = "float64", shape = (200,))#candidate|5200|(200,)|var|float64
var_5201 = relay.var("var_5201", dtype = "float32", shape = (288,))#candidate|5201|(288,)|var|float32
var_5202 = relay.var("var_5202", dtype = "uint16", shape = (8, 132))#candidate|5202|(8, 132)|var|uint16
var_5203 = relay.var("var_5203", dtype = "float64", shape = (169,))#candidate|5203|(169,)|var|float64
call_5199 = func_5198_call(var_5200,var_5201,var_5202,var_5203,)
output = call_5199
func_5204 = relay.Function([var_5200,var_5201,var_5202,var_5203,], output)
mutated_mod['func_5204'] = func_5204
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4748_call = mod.get_global_var('func_4748')
func_4749_call = mutated_mod.get_global_var('func_4749')
call_5228 = relay.TupleGetItem(func_4748_call(), 2)
call_5229 = relay.TupleGetItem(func_4749_call(), 2)
func_2451_call = mod.get_global_var('func_2451')
func_2454_call = mutated_mod.get_global_var('func_2454')
const_5233 = relay.const([6,5,-8,4,9,-10,-6,-9,4,8,-5,2,-1,-3,-6,10,-10,7,6,-5,7,-7,-4,10,10,-2,10,-10,2,4,10,10,-7,-7,2,1,9,6,4,1,-6,10,-8,-7,-4,8,4,-5,9,-5,3,-10,-2,6,-2,2,4,6,-2,2,-5,-1,10,-10,-9,-10,1,-7,-8,-10,1,-10,2,7,-10,-2,-1,6,1,4,10,-2,-6,3,1,-4,-5,-9,2,-3,-7,1,-7,3,2,-8,1,-3,-1,1,-2,-6,1,4,-3,10,-1,10,-8,8,2,2,7,10,-6,2,8,-4,3,-6,6,-6,7,-5,-1,-4], dtype = "uint16")#candidate|5233|(126,)|const|uint16
var_5234 = relay.var("var_5234", dtype = "float64", shape = (50, 4))#candidate|5234|(50, 4)|var|float64
call_5232 = relay.TupleGetItem(func_2451_call(relay.reshape(const_5233.astype('uint16'), [7, 3, 6]), relay.reshape(var_5234.astype('float64'), [5, 40]), ), 3)
call_5235 = relay.TupleGetItem(func_2454_call(relay.reshape(const_5233.astype('uint16'), [7, 3, 6]), relay.reshape(var_5234.astype('float64'), [5, 40]), ), 3)
func_2886_call = mod.get_global_var('func_2886')
func_2888_call = mutated_mod.get_global_var('func_2888')
var_5242 = relay.var("var_5242", dtype = "float32", shape = (288,))#candidate|5242|(288,)|var|float32
call_5241 = relay.TupleGetItem(func_2886_call(relay.reshape(var_5242.astype('float32'), [9, 4, 8])), 4)
call_5243 = relay.TupleGetItem(func_2888_call(relay.reshape(var_5242.astype('float32'), [9, 4, 8])), 4)
func_3978_call = mod.get_global_var('func_3978')
func_3980_call = mutated_mod.get_global_var('func_3980')
call_5258 = relay.TupleGetItem(func_3978_call(), 0)
call_5259 = relay.TupleGetItem(func_3980_call(), 0)
func_1302_call = mod.get_global_var('func_1302')
func_1303_call = mutated_mod.get_global_var('func_1303')
call_5261 = func_1302_call()
call_5262 = func_1302_call()
uop_5267 = relay.asinh(call_5261.astype('float32')) # shape=(13, 5, 9)
uop_5269 = relay.asinh(call_5262.astype('float32')) # shape=(13, 5, 9)
output = relay.Tuple([call_5228,call_5232,const_5233,var_5234,call_5241,var_5242,call_5258,uop_5267,])
output2 = relay.Tuple([call_5229,call_5235,const_5233,var_5234,call_5243,var_5242,call_5259,uop_5269,])
func_5276 = relay.Function([var_5234,var_5242,], output)
mod['func_5276'] = func_5276
mod = relay.transform.InferType()(mod)
mutated_mod['func_5276'] = func_5276
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5276_call = mutated_mod.get_global_var('func_5276')
var_5278 = relay.var("var_5278", dtype = "float64", shape = (50, 4))#candidate|5278|(50, 4)|var|float64
var_5279 = relay.var("var_5279", dtype = "float32", shape = (288,))#candidate|5279|(288,)|var|float32
call_5277 = func_5276_call(var_5278,var_5279,)
output = call_5277
func_5280 = relay.Function([var_5278,var_5279,], output)
mutated_mod['func_5280'] = func_5280
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3211_call = mod.get_global_var('func_3211')
func_3212_call = mutated_mod.get_global_var('func_3212')
call_5373 = func_3211_call()
call_5374 = func_3211_call()
func_5276_call = mod.get_global_var('func_5276')
func_5280_call = mutated_mod.get_global_var('func_5280')
const_5378 = relay.const([[8.861508],[-8.887146],[7.936039],[6.907906],[9.126514],[7.097738],[-9.206367],[-7.030995],[3.287907],[9.172811],[-3.236505],[6.114394],[2.891612],[-9.108186],[4.431115],[-3.014602],[5.130726],[0.388673],[3.843743],[0.557008],[-1.140754],[-4.448588],[-1.801901],[0.882082],[3.126517],[7.054148],[-8.143779],[-5.706876],[3.606218],[-8.802689],[-6.794610],[7.339699],[6.569660],[-3.569411],[-8.140588],[9.025305],[-8.513962],[9.956057],[-9.507139],[-5.490981],[-2.124408],[-4.349917],[5.313680],[-6.399131],[0.750151],[6.444601],[5.068745],[-7.653392],[6.029155],[1.163201],[-4.920348],[4.238643],[-7.945618],[-5.928613],[4.695539],[6.443055],[-3.403106],[-1.341892],[-9.739529],[-0.895081],[7.211729],[6.947821],[-2.019148],[6.538172],[-2.867718],[5.606304],[3.660473],[9.398000],[-1.170022],[2.874858],[7.913648],[8.991985],[-2.402478],[1.500489],[-5.507430],[-3.968387],[1.996212],[-8.951239],[3.321379],[-3.816341],[-8.315587],[9.530003],[-6.796244],[-2.925943],[-4.982893],[-0.959052],[-4.035011],[6.147206],[8.546971],[6.286661],[-8.577598],[-6.396650],[-8.081822],[5.259203],[-9.188746],[2.010167],[-4.680792],[3.171974],[-0.374991],[5.579674],[3.169740],[-2.825775],[7.991247],[-7.240345],[-9.699419],[-5.749413],[7.147187],[-5.569526],[1.600078],[-2.713094],[7.759394],[-2.637452],[-3.869094],[-2.487804],[5.817922],[6.430398],[7.332636],[-9.207476],[1.307461],[-9.443616],[4.087363],[-0.477965],[8.555634],[-9.819854],[-9.484579],[-2.732572],[-3.377545],[8.258602],[-5.819028],[0.895287],[0.073350],[-4.080671],[-7.965430],[4.327246],[0.152137],[5.792074],[-3.253565],[-9.267011],[8.381573],[-7.298358],[5.162761],[5.135053],[-7.965364],[-5.841672],[3.006788],[-5.128158],[-0.182236],[6.238341],[-5.199330],[-6.763771],[-6.526681],[-3.529869],[0.331252],[-9.221443],[3.984398],[-1.042992],[-1.829105],[-0.801984],[3.299057],[1.252398],[8.995614],[5.494683],[5.889904],[-1.442548],[-9.264450],[4.815364],[4.027990],[0.904512],[-1.147910],[0.365664],[3.278921],[-1.191830],[6.609402],[-7.875728],[5.582176],[6.938906],[3.776671],[-8.928566],[-4.379550],[-2.994573],[3.036808],[5.480814],[0.127534],[9.881102],[1.103743],[0.565766],[3.929991],[-3.397566],[3.913103],[5.911917],[-1.748532],[3.451943],[3.000195],[-8.113389],[-2.639575],[-2.913221],[6.889829],[-0.628853],[4.455736],[-6.498634]], dtype = "float64")#candidate|5378|(200, 1)|const|float64
var_5379 = relay.var("var_5379", dtype = "float32", shape = (288,))#candidate|5379|(288,)|var|float32
call_5377 = relay.TupleGetItem(func_5276_call(relay.reshape(const_5378.astype('float64'), [50, 4]), relay.reshape(var_5379.astype('float32'), [288,]), ), 1)
call_5380 = relay.TupleGetItem(func_5280_call(relay.reshape(const_5378.astype('float64'), [50, 4]), relay.reshape(var_5379.astype('float32'), [288,]), ), 1)
output = relay.Tuple([call_5373,call_5377,const_5378,var_5379,])
output2 = relay.Tuple([call_5374,call_5380,const_5378,var_5379,])
func_5382 = relay.Function([var_5379,], output)
mod['func_5382'] = func_5382
mod = relay.transform.InferType()(mod)
var_5383 = relay.var("var_5383", dtype = "float32", shape = (288,))#candidate|5383|(288,)|var|float32
output = func_5382(var_5383)
func_5384 = relay.Function([var_5383], output)
mutated_mod['func_5384'] = func_5384
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5399 = relay.var("var_5399", dtype = "int8", shape = (4, 16, 1))#candidate|5399|(4, 16, 1)|var|int8
var_5400 = relay.var("var_5400", dtype = "int8", shape = (4, 16, 15))#candidate|5400|(4, 16, 15)|var|int8
bop_5401 = relay.not_equal(var_5399.astype('bool'), var_5400.astype('bool')) # shape=(4, 16, 15)
output = bop_5401
output2 = bop_5401
func_5414 = relay.Function([var_5399,var_5400,], output)
mod['func_5414'] = func_5414
mod = relay.transform.InferType()(mod)
var_5415 = relay.var("var_5415", dtype = "int8", shape = (4, 16, 1))#candidate|5415|(4, 16, 1)|var|int8
var_5416 = relay.var("var_5416", dtype = "int8", shape = (4, 16, 15))#candidate|5416|(4, 16, 15)|var|int8
output = func_5414(var_5415,var_5416,)
func_5417 = relay.Function([var_5415,var_5416,], output)
mutated_mod['func_5417'] = func_5417
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4713_call = mod.get_global_var('func_4713')
func_4714_call = mutated_mod.get_global_var('func_4714')
call_5432 = relay.TupleGetItem(func_4713_call(), 0)
call_5433 = relay.TupleGetItem(func_4714_call(), 0)
func_3541_call = mod.get_global_var('func_3541')
func_3543_call = mutated_mod.get_global_var('func_3543')
const_5442 = relay.const([-1.115478,-3.238938,-3.620578,-2.988504,7.492291,6.526810,4.924699,-7.386911,4.984748,3.074263,9.208792,-0.724361,-2.385672,7.239762,-9.238771,-7.410306,-9.952219,-2.774900,7.063638,7.590114,-8.107960,9.178633,-7.184047,4.674051,-7.849383,-6.951965,-7.379633,0.089646,2.834584,-6.530732,-7.630700,-3.432975,4.556235,4.445246,1.327708,0.515757,-3.855614,5.039889,3.854564,-9.938446,-8.669830,9.372988,-6.475453,1.001180,9.932186,5.647214,9.746428,1.845276,-6.923575,7.919194,4.812279,6.630808,7.783621,-6.281019,-6.699357,2.378843,7.443657,7.289978,1.939010,8.245143,-1.794739,-4.761836,-2.616932,-5.208619,9.110559,-8.584032,-7.106884,-8.957058,3.904325,-3.576740,3.497872,-6.674020,-4.767742,-1.359943,-8.332135,0.864376,1.499331,-7.704344,7.773971,-7.624276,-3.756059,1.387852,2.721203,1.135255,-4.644253,-0.075712,8.638247,5.887730,-6.071293,0.471057,8.695247,5.218378,6.008321,3.965798,-8.035544,7.144539,-5.466351,9.742566,-5.649855,-5.569948,3.134475,-9.934932,3.088948,-8.747738,-6.769802,5.552765,-7.964797,-5.058683,-6.043082,-6.879107,9.541407,-6.480291,-7.898830,4.584268,-7.713855,-8.596564,-4.301308,-3.343816,-7.082742,3.262197,-6.792738,-0.341414,8.625683,-8.016904,-6.065963,-5.089077,-3.767773,-1.655537,8.293490,3.323454,7.033393,1.819402,9.490653,-1.128235,-5.208939,-7.912691,-8.528015,-7.130680,0.298189,1.514125,5.988559,0.728223,-1.662417,3.029630,-7.268722,1.519880,-6.789631,7.484015,-7.416779,6.689574,-6.980740,-5.006519,-4.559021,-0.594927,3.996886,-7.689949,-8.716719,0.548008,3.265420,-7.503572,6.005255,1.624388,-2.241782,1.621445,-1.956852,6.474567,-4.805440,7.922683,-1.525947,-5.474811,-8.324687,3.857802,9.271402,6.384870,1.307975,-1.316775,-2.627302,-5.844014,-3.528517,7.988957,-4.932171,5.432793,-8.772437,0.970007,0.080159,4.597654,-7.936632,-7.453893,1.954750,-3.141122,1.328625,5.916909,8.953233,-9.326094,-7.887014,-5.568960,-3.021682,7.135326,2.487227,-1.747075,2.172733,-4.849734,-7.610743,6.670877,-4.250689,-4.408012,-3.156431,6.135778,1.490996,8.873759,-3.382084,-0.855584,-1.765061,6.343545,-8.201903,-4.667979,3.574593,-9.893641,0.453100,2.527807,3.801223,5.240202,-8.029292,5.186600,-6.631072,7.133456,7.395050,9.738573,1.909001,3.863319,-8.268707,9.318197,-5.643993,9.457933,8.815254,7.845116,-1.780356,-0.073305,-8.229943,-0.270225,9.892498,6.656271,4.088525,-8.043760,3.189994,5.117929,2.576968,-1.633144,-4.818599,8.714525,-1.625890,-7.057613,2.134958,7.585984,3.604276,-8.718392,0.265012,1.449558,-2.623141,-3.760976,6.643745,-4.792376,-3.311947,-8.127368,-5.944418,6.087061,-6.988244,-0.516208,-3.245410,7.108930,5.915977,-1.180982,2.461015,-6.825680,0.418348,-0.523156,-2.632288,9.249115,8.197378,6.583089,1.087270,-1.891613,-4.537069,5.920359,6.284272,-3.810581,-3.690549,8.766017,-2.205199,-6.765736,-8.204999,-1.190455,3.394372,-1.075230,4.960486,-5.440205,-5.626719,3.440112,1.423939,5.338061,9.433770,-7.052677,9.826403,-2.782104,9.133037,2.131383,4.141560,-0.512797,-8.667997,9.822122,-8.940829,-7.700148,-3.983384,8.150033,9.712774,-6.083599,8.585371,-0.401698,7.721660,-3.386907,5.284337,-7.853312,-5.456525,3.573868,3.636382,-1.001167,1.073509,-0.672430,-1.529718,6.600556,5.150893,9.164949,-9.532985,1.646327,-8.068300,-6.406629,5.611251,-6.216702,6.953323,-8.043623,-4.042338,-0.743067,-8.219245,5.428097,3.325400,-6.959363,8.444093,5.345890,9.171742,0.092360,-8.935628,-9.237432,-2.497962,1.121794,-1.130497,7.489583,8.498874,-9.302402,-7.017905,-4.683815,1.583783,-2.018858,-6.585750,-6.944996,-1.025475,7.460715,-3.305489,4.908899,-1.400684,-2.752026,-4.913119,2.280933,-0.405104,3.156377,-0.313642,-5.504981,-3.397390,-8.679842,-5.575385,6.472672,-7.249075,1.232514,-4.320994,0.835485,-5.711711,9.696157,5.445099,-6.602372,6.500179,5.598960,8.270580,3.268628,-4.404613,2.255022,-9.347588,-9.096354,3.370405,8.224020,-4.931674,6.180223,5.004878,9.518256,1.612401,-9.547953,-7.440771,-2.398748,0.340811,2.089220,9.451961,-9.133575,3.109575,-0.449769,-1.071802,-7.991562,0.777875,7.111122,7.474047,3.438142,-7.698538,0.960736,0.740805,1.307398,0.088854,2.273629,7.168220,-1.407631,-5.741064,6.219624,0.516383,0.567428,6.799795,6.513630,6.189995,-5.113985,-3.908117,-1.387739,4.173251,-7.730141,6.990956,-3.646011,5.328028,7.158689,3.860241,-1.830036,9.491729,8.636799,3.219135,7.198607,-2.973348,-2.928612,1.668969,-5.385640,-1.059696,9.387010,-1.264236,-4.477222,-9.447421,9.492308,9.865069,-8.653201,6.874581,5.772694,-3.792394,-4.253286,-0.118166,9.579258,5.862904,4.554704,-6.873251,8.734129,-9.191675,-5.952014,-1.775835,-2.349396,-7.843710,-5.260459,2.265978,-6.539047,-9.963868,-2.328634,2.288810,-9.773919,5.520397,1.808684,-9.064835,0.989769,-1.554732,0.609875,4.596085,-5.424664,2.948984,-3.434616,0.363021,-2.852209,8.401872,-7.975197,6.696600,3.979897,-2.798612,-2.310508,-2.770729,2.463501,-0.091314,6.718920,3.871934,5.827425,-2.458663,4.922609,-4.976187,2.019414,-7.866137,-1.733754,-0.669342,-3.842292,-6.489873,5.233953,-7.504336,-0.514741,9.583665,0.391135,4.894477,1.624712,-0.392741,0.532165,7.815831,-9.114111,0.579651,1.931337,-0.747807,-1.835748,-3.236344,1.891045,0.396577,0.012900,7.771260,0.117371,0.299477,-9.078864,9.234069,-5.094378,-8.631948,-8.656199,-1.856944,1.561463,1.166727,6.051431,6.550839,8.033529,-2.989177,-8.237427,0.004601,2.583305,-3.509251,-3.331493,8.428507,-1.478127,8.610261,3.671974,-0.759044,-0.953726,3.697679,-0.384750,3.871616,6.094495,-8.729979,9.645415,8.714304,8.263401,8.930586,4.557882,-4.083033,-6.441606,-5.291515,1.551300,3.176303,-8.759423,-6.573368,8.631984,-2.144479,3.711520,-2.992549,-9.167560,5.537271,-8.803486,0.471910,-3.244255,6.793484,1.636077,-2.005843,9.742512,2.351345,-2.530132,-5.155178,9.993645,-4.609691,4.135244,7.030325,-4.400117,4.022722,4.926000,-9.455582,4.916283,1.846753,6.004552,2.348623,0.837049,9.601515,-6.696895,0.738837,-7.190967,8.773557,7.225110,-9.860896,1.548706,-3.546617,-1.435763,-5.358669,-3.429205,6.680610,-8.475092,-1.622181,4.539733,7.523021,5.890216,7.972464,4.321537,-3.311206,8.245787,-5.168544,-2.028705,-5.076169,-6.519025,-1.055671,-3.274676,-9.062255,6.375157,-6.292423,-7.970185,-2.116365,-3.929321,-5.190253,-3.820408,-3.111218,3.490374,6.201954,9.550618,-6.486098,-1.374696,4.836375,-4.143765,1.657957,-3.276764,-1.147483,-3.187927,3.493201,-9.911445,-9.505894,-8.207475,8.080417,4.458448,9.049523,-8.732962,-5.106237,0.082967,3.063322,-5.560953,2.276213,-5.725437,5.731950,-4.095539,8.164336,-3.934663,-7.140800,8.396917,-9.532279,-9.144674,3.552571,-9.103872,3.923763,8.554735,5.154581,-7.037206,0.788153,6.466433,1.222480,3.459046,-7.905551,-1.349300,-7.971627,-1.483967,-2.288569,-2.095218,1.477082,-3.720851,-9.877874,7.672645,4.137538,-9.349222,-4.556985,4.040298,-8.774633,8.723735,9.054175,1.219553,0.818377,-9.944764,-7.508109,9.550432,9.883449,-6.215134,-9.186888,-0.899581,9.727626,-2.328389,-7.069418,1.413480,-1.487071,8.535416,-6.105248,9.408567,2.258445,-6.424472,-9.339161,4.358746,5.852158,-9.777120,-9.831913,9.743663,7.612374,2.891926,9.864350,-3.137671,7.305547,1.930562,-9.519781,1.233890,3.760877,5.072326,-1.463631,8.872541,2.635629,1.528123,-4.310518,1.230886,-3.372147,3.422620,-5.912228,7.769577,-1.821796,3.481631,1.896135,-4.005645,-1.914258,-9.018096,-0.126572,-2.104380,2.296343,4.544782,-6.446488,-9.896187,-2.675750,6.938575,5.067650,-0.346911,2.398063,0.285977,1.158053,0.765749,4.387635,-7.940440,-8.298539,8.389078,-0.216785,4.112065,-1.108053,9.339383,-5.339563,3.566256,2.662554,4.927457,1.701745,0.395159,-4.774363,2.753490,-9.590262,3.260379,-8.564499,5.101256,-4.574460,-5.706412,-7.928078,6.763289,-3.360300,-9.059322,-2.919027,-0.613750,-7.410524,-6.104175,7.368784,4.159934,9.340648,-3.142890,3.837657,-3.712474,-9.602253,-2.174155,-6.447784,5.260083,-8.757455,-7.558562,2.813289,0.878695,-4.571489,-6.676648,2.018647,-1.617143,7.547507,-1.289468,-7.522434,-8.545385,2.632016,2.112368,-0.814706,-6.961762,-5.488429,6.903720,-1.388845,-5.243660,1.717538,-6.094049,-1.033497,6.557608,6.352013,-2.629510,9.837425,-2.073950,-3.431791,-7.419848,5.398780,0.287159,-3.434165,7.905946,6.744315,8.997042,8.470463,4.628565,-2.208933,1.332811,2.900086,6.750812,-8.984435,1.609609,8.684764,4.587598,3.051434,9.693397,8.668709,-2.767758,-9.281873,7.060526,4.233853,4.118604,-2.819941,3.908379,-8.913956,-5.084553,-7.243435,7.801248,8.084043,-3.813400,-6.524855,-5.490410,7.937787,-0.422947,1.983076,3.988801,0.956186,-3.141344,6.395218,6.137874,9.719580,-1.881805,0.471439,2.901552,-1.344807,8.241444,8.533974,-8.190989,-0.138957,-8.652379,6.072991,-1.579906,-9.625764,-6.131936,-0.803980,-1.546172,9.828899,-0.381231,-5.987742,6.339446,9.033239,2.603634,0.535103,6.837649,5.931634,4.589311,9.831904,8.032445,-1.549662,1.658063,5.746276,-7.216391,-5.708160,0.877880,8.998208,0.883386,-0.256354,3.312524,0.468643,0.444687,5.350425,0.473294,8.786258,-3.901766,-6.460744,-3.211006,1.009079,-7.876355,4.872447,7.802265,-8.689546,-3.350499,4.183541,-8.282799,-3.613339,2.567673,-3.669239,0.690505,3.874235,-2.611719,3.316260,7.030555,3.759980,7.529655,-4.417102,9.337344,2.473591,4.237845,-8.024091,7.522817,3.928751,-7.991287,3.503624,8.871152,0.361773,-6.678487,4.364710,-3.758388,5.803261,1.828861,-6.445033,0.357228,-6.179783,-8.986973,-9.133434,-0.633327,3.338644,-3.740083,-5.086687,8.398803,8.022789,-5.418735,-4.712069,8.886383,-6.060686,6.698353,-8.372666,9.717199,3.930979,1.534803,8.108316,8.077585,-6.196199,-7.437712,-9.904321,-0.107027,6.840066,-3.435232,3.029053,-3.868519,-7.018308,-4.399092,-7.509187,-8.944005,-9.486454,2.482853,0.024369,-5.156139,-1.762878,-7.551889,-7.493466,-2.072448,9.174214,7.109168,5.997428,7.118560,1.599110,-8.479756,9.469332,5.885041,-7.427542,3.294800,-2.427297,6.386110,-1.876170,2.412975,-4.424984,2.318438,-6.561479,3.662625,-4.001714,7.559470,-0.161562,9.734200,-6.651920,2.933962,3.589352,-2.412332,-1.159894,9.916316,3.989526,-8.397766,-7.547247,-7.134471,-6.010584,-7.717044,-3.201055,6.223965,1.325832,-9.558435,0.671456,-7.859807,-1.634421,-2.649074,-0.527969,-1.743659,-2.740210,-2.383008,-5.241646,4.593907,-4.636652,7.305332,-4.286840,0.892072,3.017090,7.809534,-3.867260,6.752952,5.627958,1.120315,6.523133,2.415444,-2.486186,8.326732,-5.160889,-7.919170,-5.119560,8.436191,-4.706355,9.228195,-3.100685,-3.462905,-4.928113,-4.488986,-4.836346,-9.434000,6.939126,4.987778,4.948198,-8.737005,-8.606259,-7.085672,-3.428921,4.341904,-1.626771,-8.134511,5.105325,0.063051,-8.528147,3.247423,-3.313101,0.840795,-5.131398,0.373750,8.053794,3.970464,-2.436821,-2.590801,-3.085709,7.134736,-6.045713,9.560746,1.504344,-2.602256,-0.772416,-4.349928,6.345371,-2.005825,-7.776393,2.695023,6.762135,3.149564,-6.988520,-3.889623,7.375482,7.736447,2.821685,-1.792119,-8.545901,5.492626,-9.283404,5.411591,9.989667,4.211477,2.225495,1.022039,-6.892628,7.495656,-9.257416,5.377576,8.477336,-4.375119,2.298765,1.148638,4.141160,5.049457,-9.783301,2.445137,-0.392870,-4.358578,9.062418,2.416323,-4.741680,-8.399487,-4.327012,8.472736,-0.099334,3.867338,-5.841662,4.114202,6.582096,6.390651,0.759236,5.887115,-0.702604,-5.503966,7.893024,5.756923,-1.635206,-1.246500,1.846332,-9.415361,0.481841,4.103758,0.716855,4.245203,1.419156,-3.501039,3.256476,8.601280,0.787974,7.780819,6.204239,5.946784,-9.241726,-6.396560,5.920164,-6.636904,-3.998140,-8.255360,-7.511674,-9.312389,-2.777180,5.203163,-3.481298,2.834410,-7.710350,-2.910000,9.555223,4.355849,-2.895295,4.634246,-2.598338,-6.732613,-2.567760,-6.195165,8.046188,-4.490618,-2.161713,7.312995,-1.957706,-1.373888,-7.196841,-1.963008,-3.009071,4.759356,-8.548176,-9.662556,-9.865684,0.015127,1.883974,-0.456739,2.706719,9.842374,-3.379538,-3.328944,1.997912,6.076533,-4.017511,-6.493230,8.584611,5.644703,-1.013103,-8.397162,-8.393806,1.010182,-8.263787,-5.898909,1.380702,9.050542,4.590742,-8.858740,-7.012694,-8.517273,-0.244920,-2.143629,-1.463550,3.345049,4.687683,-8.906079,3.351313,-3.595076,0.066778,9.007794,-5.352937,-7.618486,3.303181,-3.179526,-3.420836,-9.775978,1.852463,-6.303305,-6.303510,6.717368,2.373547,9.053899,9.692471,-1.735075,1.699731,3.924772,-5.095974,1.622849,5.477587,-7.118118,-4.726281,-1.514365,6.468839,3.396346,-0.385994,8.590168,-2.932564,-2.994852,-7.310682,-0.578404,2.036741,0.841681,9.146673,4.371933,5.610392,-8.570046,-2.378663,8.391214,5.296708,8.161463,2.046210,-3.094760,1.695170,-1.551980,6.470173,1.295645,-0.751583,2.235307,6.417368,-0.323849,-6.170054,-8.457498,9.615191,-3.601031,4.149680,-3.572177,-5.962603,-1.482346,-3.864387,-8.885033,-5.149300,-3.277701,-2.532836,-8.254701,-9.698579,-7.472641,-3.473294,9.125433,3.912149,-9.588759,2.040875,0.278008,1.634733,1.013643,-0.123654,-5.727924,-3.192530,-9.388924,-6.560115,-1.044289,8.991473,6.938917,-1.494827,-2.492247,-0.154777,-5.459164,1.146872,9.545318,4.030860,-8.361638,-4.558004,-2.598738,4.419978,-2.000988,-4.791481,-4.822943,7.487271,4.331426,-4.364354,8.782037,-5.962010,-2.305200,-9.811901,0.019220,9.789960,0.512270,-1.136336,-4.252443,-1.148606,7.957090,7.059995,0.124066,9.354545,-1.031461,-1.489318,-5.539495,6.894091,-2.890606,-7.723201,-1.020491,-1.320900,-9.253535,0.256343,-2.952038,0.337135,-0.298620,-9.356586,1.004431,-0.177298,6.639199,-4.421487,-2.718132,6.258260,4.851693,-0.330632,0.290561,0.177067,1.773165,-2.222055,0.811666,2.041598,-7.429817,2.268193,6.065874,-1.347277,-2.012903,-4.892981,-7.419542,1.293484,1.293200,5.505622,-1.840443,-7.709756,-4.628491,-5.197991,-9.553022,5.121758,8.378084,4.482238,1.956090,7.634591,-4.183809,-7.629913,4.347738,-8.117439,0.330091,3.427990,-5.840200,8.330168,-7.707545,-6.017349,4.187312,-4.437966,-5.611078,4.178687,1.226917,4.317685,-3.614551,-8.814403,-8.456841,-0.873447,2.835628,6.675175,-4.976618,-0.816509,-7.418191,7.901588,-3.523377,-8.203136,2.173956,-2.758884,4.665615,-1.389850,3.665663,0.585219,3.984395,1.518407,-6.346772,1.068839,7.142989,1.545402,-3.842726,9.655352,-2.746918,-7.990525,4.335493,-6.243980,-0.157893,-6.387264,-5.231238,1.177934,-6.688448,-1.254628,-5.714913,5.392754,3.794512,5.961034,0.905290,-3.420683,5.072703,-9.238583,-0.717620,7.574571,3.706004,-8.167512,7.912040,-7.357847,8.956111,-7.592615,-9.295353,7.977506,6.377563,7.866227,-7.686654,-6.946608,-6.183208,-9.946479,-4.273265,-4.908563,-0.654926,9.761977,-4.757045,7.429707,-4.867377,6.848596,8.357690,-4.455770,-0.463815,5.661719,9.963564,-7.414532,-6.668989,-6.004852,-1.145697,3.568174,-5.331535,-6.700198,-7.248129,-1.907332,-4.497595,4.095291,-2.375831,-5.513861,8.319714,1.358453,7.528670,5.487976,2.821144,-8.035436,-5.430165,-6.011692,-0.021177,5.876288,-5.699002,5.010228,-5.017722,-0.834775,-0.232200,3.935281,-1.113528,5.985950,-0.009796,-0.252732,-0.752643,6.622964,-5.787337,9.354781,-4.914619,0.531398,-6.081394,4.308979,1.555878,-2.446245,-6.656941,2.243445,-7.060216,6.431920,5.964110,-3.306279,-1.189336,-6.491358,3.910775,-9.558659,7.350545,-5.131401,-6.432487,-4.648679,4.460612,-2.608922,-7.659258,2.311869,-6.466949,5.632618,-7.734616,5.516101,4.472790,8.716760,-3.360524,-7.575468,9.399799,8.742178,7.109511,8.509080,-2.889231,-0.072151,0.913453,-2.800747,-7.545091,-9.219893,3.825039,-2.898687,5.868017,-2.090391,0.161808,3.871104,0.305013,-6.831775,-2.357733,-2.420213,8.658426,8.165420,-6.161915,-8.764489,3.445210,1.395715,4.614663,9.514567,9.347480,-5.848661,9.437924,8.539424,-9.210871,4.862419,7.014891,-0.826657,-4.438333,9.285268,1.245461,-0.446140,-4.109179,5.459511,8.274784,5.869312,-3.038773,0.411476,6.512197,7.615223,-8.857101,7.493019,-3.468960,4.439938,8.875362,1.192060,-7.026823,-7.882708,9.827195,-4.611584,-5.887291,8.803067,2.633276,-2.106722,4.478393,2.914872,-1.679588,8.448735,-6.733244,-9.302949,6.287475,-6.480001,5.282582,0.352009,-2.246925,2.641657,9.358786,-4.211656,0.099383,9.760109,-5.400026,-3.384957,4.314028,3.709603,-4.602833,-1.315808,0.458027,-1.988046,0.690042,9.073006,7.678326,-9.046621,3.189428,-1.153196,-9.942710,0.459144,-8.350802,7.652135,8.318570,5.857139,-8.916476,8.479568,-9.074013,-9.529608,5.077804,9.827228,-5.505977,3.823764,-8.941249,-0.859617,-1.290969,7.538215,-8.973223,-4.686127,8.775513,2.059514,8.521751,0.608149,-1.302668,6.453943,7.094675,4.123601,7.787118,7.860837,-8.650684,-1.147292,3.754039,0.931088,-8.065053,0.076148,3.998106,-4.987586,-7.235877,-2.375314,7.947480,-4.017174,-2.860755,1.504900,2.126134,-7.899569,-8.154273,-6.263726,-2.490203,3.539131,6.187054,9.681908,-8.688836,-7.626084,1.941725,7.189407,-8.105150,-1.992159,6.104292,-6.432327,-0.709478,-3.876562,3.107620,6.569737,-9.382076,7.002543,5.034877,-6.076001,-8.699287,-2.940179,5.651408,-4.337078,-1.054635,0.607801,-0.240558,-1.274675,-6.522159,-6.932755,3.666496,0.431448,-3.826130,4.141724,8.452824,9.372468,-3.719721,-3.786079,-3.730425,-1.066469,7.673287,-2.728715,2.644523,-2.357609,-0.416184,-4.503068,-0.583730,4.523490,-3.195397,4.848069,0.494053,6.881870,-2.249588,6.304135,-6.800565,5.188874,9.785077,-5.760343,-7.271920,-0.552282,6.452579,-2.564134,5.285674,-5.741537,8.629799,3.645215,8.737642,-9.609745,-6.648073,-7.117399,4.289119,-2.190990,9.106770,-6.998850,-0.416954,-9.047227,4.381270,9.727846,1.784341,-8.848745,8.160659,0.909264,-8.893377,1.847080,9.039396,5.412078,1.964482,-8.724585,-1.072969,1.199843,5.254275,-4.271391,-9.561238,6.306375,-8.526266,-2.058435,-6.005984,-2.047308,-4.354723,8.925725,2.793649,-8.527670,8.201492,7.386418,9.188947,-7.779053,9.124671,9.444704,-4.036974,0.785382,-6.219772,4.865554,5.787918,4.017594,4.964250,3.896881,-7.819204,4.149602,-9.751775,7.445977,8.743256,0.495210,2.424818,1.971495,9.749169,-0.977250,-0.495535,-8.925861,7.419854,5.855471,9.359175,6.487584,7.561307,8.607674,5.803705,7.636809,-6.762346,8.959966,-8.127691,8.187908,7.042825,4.593400,9.067504,4.941962,-2.576457,3.708206,-4.160032,9.789860,-0.766895,3.841776,2.479345,-2.861087,7.539607,7.570454,-7.148393,-3.395937,-7.827377,-0.791978,7.125870,-0.797488,-4.522406,2.876605,-8.843355,-7.559044,6.429335,9.827009,5.303734,-1.561307,0.773581,-5.220615,7.054833,-7.681900,-8.538399,8.349862,-7.496995,5.132177,-2.478947,1.115023,1.819905,2.701594,-9.651134,-4.449276,-4.692728,-3.059106,-9.253129,-1.769172,6.130600,-9.391270,0.195464,-3.948475,6.634299,-4.149691,-2.137514,1.064824,-0.829050,9.148338,7.191232,-6.589274,-9.880009,3.343029,8.843636,-4.897818,-3.350383,-3.917773,4.191135,-0.722369,1.137536,-7.455441,-4.736503,7.486463,-8.944296,4.183599,-4.350038,9.349113,9.742062,-2.875692,-3.063140,6.257410,1.167637,-8.652287,-3.158605,4.609841,-4.853169,-7.781720,4.260335,1.933790,-6.953865,7.541231,-2.323217,2.850819,-0.978243,-7.026952,5.481521,5.628326,6.273341,9.386575,-0.712298,0.781419,-0.321259,-6.594879,-9.566097,5.492771,-8.513611,0.017435,6.831896,-9.133603,-1.589279,3.645322,8.803834,-2.584853,-8.905065,-6.365532,6.282208,9.879632,6.505915,7.900622,2.765361,-7.624111,-0.964124,-7.064812,6.873674,4.288759,8.842734,4.730296,1.609826,-5.801767,3.342933,4.323925,-3.644920,-7.574067,-8.086733,3.368847,-2.285635,9.135825,-6.575311,-1.458993,0.310218,8.891229,-0.907202,1.437727,7.635357,-6.922890,-8.277384,2.780192,-1.867968,6.247447,5.495619,6.390533,-0.923761,-1.664463,-0.357824,-4.840522,-1.827308,4.414646,-0.246519,1.471254,-8.843614,-5.525947,4.800250,0.739055,8.658913,-2.253374,-1.232382,-8.067935,-3.111935,8.246964,-2.060453,-6.464222,9.175900,6.424673,-8.904963,1.508519,-2.713892,-9.298581,9.522810,-9.788086,-3.511544,-6.324937,-1.348190,8.338592,7.015882,0.062413,0.524218,5.590623,5.097347,-1.297270,6.231882,-3.561042,-1.229111,8.834967,0.783216,-2.205162,-5.545419,-2.276480,-4.684714,4.272235,-2.500073,9.619677,2.384835,-0.335638,1.916403,-2.690904,8.257061,9.119706,8.922109,6.616395,-6.275159,-5.604457,-5.760847,8.739774,9.495461,1.627449,3.145967,2.033145,1.047200,-7.329536,-5.474370,4.835543,4.649984,8.764873,6.365513,5.338070,9.157571,-4.435107,-4.228425,-1.583008,-4.909200,3.059610,-5.663115,-0.563447,2.524225,-3.373203,-4.039356,7.180793,-3.927561,-8.044349,4.931178], dtype = "float64")#candidate|5442|(2080,)|const|float64
call_5441 = relay.TupleGetItem(func_3541_call(relay.reshape(const_5442.astype('float64'), [13, 16, 10])), 1)
call_5443 = relay.TupleGetItem(func_3543_call(relay.reshape(const_5442.astype('float64'), [13, 16, 10])), 1)
output = relay.Tuple([call_5432,call_5441,const_5442,])
output2 = relay.Tuple([call_5433,call_5443,const_5442,])
func_5461 = relay.Function([], output)
mod['func_5461'] = func_5461
mod = relay.transform.InferType()(mod)
mutated_mod['func_5461'] = func_5461
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5461_call = mutated_mod.get_global_var('func_5461')
call_5462 = func_5461_call()
output = call_5462
func_5463 = relay.Function([], output)
mutated_mod['func_5463'] = func_5463
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5467 = relay.var("var_5467", dtype = "uint8", shape = (6, 2, 12))#candidate|5467|(6, 2, 12)|var|uint8
var_5468 = relay.var("var_5468", dtype = "uint8", shape = (6, 2, 12))#candidate|5468|(6, 2, 12)|var|uint8
bop_5469 = relay.right_shift(var_5467.astype('uint8'), relay.reshape(var_5468.astype('uint8'), relay.shape_of(var_5467))) # shape=(6, 2, 12)
func_3395_call = mod.get_global_var('func_3395')
func_3397_call = mutated_mod.get_global_var('func_3397')
call_5480 = relay.TupleGetItem(func_3395_call(), 0)
call_5481 = relay.TupleGetItem(func_3397_call(), 0)
output = relay.Tuple([bop_5469,call_5480,])
output2 = relay.Tuple([bop_5469,call_5481,])
func_5486 = relay.Function([var_5467,var_5468,], output)
mod['func_5486'] = func_5486
mod = relay.transform.InferType()(mod)
var_5487 = relay.var("var_5487", dtype = "uint8", shape = (6, 2, 12))#candidate|5487|(6, 2, 12)|var|uint8
var_5488 = relay.var("var_5488", dtype = "uint8", shape = (6, 2, 12))#candidate|5488|(6, 2, 12)|var|uint8
output = func_5486(var_5487,var_5488,)
func_5489 = relay.Function([var_5487,var_5488,], output)
mutated_mod['func_5489'] = func_5489
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2461_call = mod.get_global_var('func_2461')
func_2462_call = mutated_mod.get_global_var('func_2462')
call_5522 = func_2461_call()
call_5523 = func_2461_call()
output = call_5522
output2 = call_5523
func_5542 = relay.Function([], output)
mod['func_5542'] = func_5542
mod = relay.transform.InferType()(mod)
output = func_5542()
func_5543 = relay.Function([], output)
mutated_mod['func_5543'] = func_5543
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2172_call = mod.get_global_var('func_2172')
func_2173_call = mutated_mod.get_global_var('func_2173')
call_5553 = relay.TupleGetItem(func_2172_call(), 1)
call_5554 = relay.TupleGetItem(func_2173_call(), 1)
func_311_call = mod.get_global_var('func_311')
func_315_call = mutated_mod.get_global_var('func_315')
var_5559 = relay.var("var_5559", dtype = "bool", shape = (576,))#candidate|5559|(576,)|var|bool
call_5558 = func_311_call(relay.reshape(var_5559.astype('bool'), [9, 4, 16]), relay.reshape(var_5559.astype('bool'), [9, 4, 16]), )
call_5560 = func_311_call(relay.reshape(var_5559.astype('bool'), [9, 4, 16]), relay.reshape(var_5559.astype('bool'), [9, 4, 16]), )
uop_5582 = relay.cos(var_5559.astype('float32')) # shape=(576,)
output = relay.Tuple([call_5553,call_5558,uop_5582,])
output2 = relay.Tuple([call_5554,call_5560,uop_5582,])
func_5586 = relay.Function([var_5559,], output)
mod['func_5586'] = func_5586
mod = relay.transform.InferType()(mod)
var_5587 = relay.var("var_5587", dtype = "bool", shape = (576,))#candidate|5587|(576,)|var|bool
output = func_5586(var_5587)
func_5588 = relay.Function([var_5587], output)
mutated_mod['func_5588'] = func_5588
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2317_call = mod.get_global_var('func_2317')
func_2318_call = mutated_mod.get_global_var('func_2318')
call_5592 = func_2317_call()
call_5593 = func_2317_call()
output = call_5592
output2 = call_5593
func_5610 = relay.Function([], output)
mod['func_5610'] = func_5610
mod = relay.transform.InferType()(mod)
mutated_mod['func_5610'] = func_5610
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5610_call = mutated_mod.get_global_var('func_5610')
call_5611 = func_5610_call()
output = call_5611
func_5612 = relay.Function([], output)
mutated_mod['func_5612'] = func_5612
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5542_call = mod.get_global_var('func_5542')
func_5543_call = mutated_mod.get_global_var('func_5543')
call_5616 = func_5542_call()
call_5617 = func_5542_call()
func_1726_call = mod.get_global_var('func_1726')
func_1727_call = mutated_mod.get_global_var('func_1727')
call_5621 = func_1726_call()
call_5622 = func_1726_call()
output = relay.Tuple([call_5616,call_5621,])
output2 = relay.Tuple([call_5617,call_5622,])
func_5636 = relay.Function([], output)
mod['func_5636'] = func_5636
mod = relay.transform.InferType()(mod)
mutated_mod['func_5636'] = func_5636
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5636_call = mutated_mod.get_global_var('func_5636')
call_5637 = func_5636_call()
output = call_5637
func_5638 = relay.Function([], output)
mutated_mod['func_5638'] = func_5638
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4580_call = mod.get_global_var('func_4580')
func_4581_call = mutated_mod.get_global_var('func_4581')
call_5730 = relay.TupleGetItem(func_4580_call(), 0)
call_5731 = relay.TupleGetItem(func_4581_call(), 0)
func_1618_call = mod.get_global_var('func_1618')
func_1621_call = mutated_mod.get_global_var('func_1621')
const_5752 = relay.const([[0.736271,2.716932,-7.117546,9.794590,-8.433239,3.213180,2.674796,-6.351335,1.339755,0.049975,3.763514,-7.691811,5.496788,7.230765,-6.078750,8.912237,-5.623619,3.346220,9.156067,-9.807536],[0.490618,6.231605,-4.971778,-3.309125,9.812699,7.988122,-3.376667,-1.135859,8.981110,-8.794938,-1.150290,-0.584801,-3.005618,-7.586053,-3.405154,-4.112019,-0.291033,3.177202,2.009290,7.650875],[4.553478,-9.816660,-3.289337,-0.677697,-1.540698,-6.927397,-0.584459,-2.164404,-6.730319,-5.944039,2.740794,-2.491909,-8.768381,-9.549186,-4.047260,-8.146779,6.982621,3.778726,-9.121431,6.768428],[-8.631117,4.224057,-3.066536,-3.402019,-1.744597,-6.932215,5.971226,-0.049336,-3.732212,2.021826,-4.626381,-2.875978,-5.283820,0.533238,7.684990,-9.590572,-4.462853,-3.419497,8.915041,3.962900],[-8.177090,1.374819,6.319514,4.164056,9.639234,-0.939013,5.832785,4.082993,-2.768011,-3.472009,0.550044,-1.776181,-0.960118,8.181899,5.472440,-0.831697,-7.871412,4.787656,8.397484,2.895961],[3.345587,-5.326019,-6.011719,7.223119,-9.322777,4.172285,-7.415956,-7.241058,-1.130904,-1.098911,-6.858198,8.558621,-4.962773,-6.163738,-2.164486,-7.481569,3.707864,-1.021530,-4.918866,1.065335],[0.144951,6.613329,-7.769958,-6.295024,8.946256,-1.478876,8.804693,-8.649595,-3.126493,2.566346,-7.586783,-7.257134,-5.329332,1.944422,-5.504372,-7.255179,1.742088,4.982690,1.338503,0.536801],[-4.538018,-2.607080,7.850778,-4.231222,-7.166230,-9.807268,0.762430,-3.067093,2.080383,4.811778,-5.512419,1.182276,4.537444,0.550406,1.348054,4.630226,-1.383271,3.825072,-3.066378,4.092432],[-6.071121,9.614740,7.118749,7.947209,2.262102,-1.443210,-7.515099,-2.249103,6.103087,-1.069754,-2.628410,-5.996076,-5.290280,-6.187023,2.421814,1.944152,-1.905677,-6.592924,-4.193115,-1.700020],[-8.698682,-7.044392,5.055118,-2.114481,-3.434855,5.231337,-8.141482,-2.293882,0.772574,7.785334,-1.441755,-8.748536,8.202292,-3.246195,7.357824,3.915486,-9.401451,-2.520285,-7.940407,-5.707646]], dtype = "float64")#candidate|5752|(10, 20)|const|float64
call_5751 = relay.TupleGetItem(func_1618_call(relay.reshape(const_5752.astype('float64'), [5, 40])), 3)
call_5753 = relay.TupleGetItem(func_1621_call(relay.reshape(const_5752.astype('float64'), [5, 40])), 3)
output = relay.Tuple([call_5730,call_5751,const_5752,])
output2 = relay.Tuple([call_5731,call_5753,const_5752,])
func_5765 = relay.Function([], output)
mod['func_5765'] = func_5765
mod = relay.transform.InferType()(mod)
output = func_5765()
func_5766 = relay.Function([], output)
mutated_mod['func_5766'] = func_5766
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5815 = relay.var("var_5815", dtype = "int32", shape = (3, 2, 10))#candidate|5815|(3, 2, 10)|var|int32
const_5816 = relay.const([[[8,6,9,3,6,-9,8,4,9,10],[-8,-3,-5,-2,5,2,9,-5,5,-6]],[[-3,8,4,3,-9,-1,5,3,-8,-2],[4,6,-1,-4,10,7,-6,5,6,-3]],[[2,-4,-7,-4,4,10,9,1,-9,-6],[4,2,-10,-8,-6,3,-7,4,6,1]]], dtype = "int32")#candidate|5816|(3, 2, 10)|const|int32
bop_5817 = relay.maximum(var_5815.astype('int32'), relay.reshape(const_5816.astype('int32'), relay.shape_of(var_5815))) # shape=(3, 2, 10)
func_4530_call = mod.get_global_var('func_4530')
func_4532_call = mutated_mod.get_global_var('func_4532')
call_5827 = func_4530_call()
call_5828 = func_4530_call()
const_5831 = relay.const([[[-10,5,3,4,-5,9,-6,-10,-7,8],[-7,-7,-3,-7,8,7,8,7,-3,1]],[[-1,4,1,10,9,6,-9,4,-5,-5],[8,10,-3,-7,-8,-6,1,6,-6,-1]],[[-6,-10,10,-7,2,8,5,7,-5,-8],[-5,9,4,5,4,6,5,-5,1,-1]]], dtype = "int32")#candidate|5831|(3, 2, 10)|const|int32
bop_5832 = relay.logical_or(var_5815.astype('bool'), relay.reshape(const_5831.astype('bool'), relay.shape_of(var_5815))) # shape=(3, 2, 10)
output = relay.Tuple([bop_5817,call_5827,bop_5832,])
output2 = relay.Tuple([bop_5817,call_5828,bop_5832,])
func_5838 = relay.Function([var_5815,], output)
mod['func_5838'] = func_5838
mod = relay.transform.InferType()(mod)
mutated_mod['func_5838'] = func_5838
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5839 = relay.var("var_5839", dtype = "int32", shape = (3, 2, 10))#candidate|5839|(3, 2, 10)|var|int32
func_5838_call = mutated_mod.get_global_var('func_5838')
call_5840 = func_5838_call(var_5839)
output = call_5840
func_5841 = relay.Function([var_5839], output)
mutated_mod['func_5841'] = func_5841
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2172_call = mod.get_global_var('func_2172')
func_2173_call = mutated_mod.get_global_var('func_2173')
call_5913 = relay.TupleGetItem(func_2172_call(), 0)
call_5914 = relay.TupleGetItem(func_2173_call(), 0)
output = call_5913
output2 = call_5914
func_5974 = relay.Function([], output)
mod['func_5974'] = func_5974
mod = relay.transform.InferType()(mod)
mutated_mod['func_5974'] = func_5974
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5974_call = mutated_mod.get_global_var('func_5974')
call_5975 = func_5974_call()
output = call_5975
func_5976 = relay.Function([], output)
mutated_mod['func_5976'] = func_5976
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4665_call = mod.get_global_var('func_4665')
func_4666_call = mutated_mod.get_global_var('func_4666')
call_6069 = func_4665_call()
call_6070 = func_4665_call()
func_1575_call = mod.get_global_var('func_1575')
func_1576_call = mutated_mod.get_global_var('func_1576')
call_6080 = func_1575_call()
call_6081 = func_1575_call()
func_2806_call = mod.get_global_var('func_2806')
func_2808_call = mutated_mod.get_global_var('func_2808')
call_6083 = relay.TupleGetItem(func_2806_call(), 0)
call_6084 = relay.TupleGetItem(func_2808_call(), 0)
output = relay.Tuple([call_6069,call_6080,call_6083,])
output2 = relay.Tuple([call_6070,call_6081,call_6084,])
func_6113 = relay.Function([], output)
mod['func_6113'] = func_6113
mod = relay.transform.InferType()(mod)
output = func_6113()
func_6114 = relay.Function([], output)
mutated_mod['func_6114'] = func_6114
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4068_call = mod.get_global_var('func_4068')
func_4069_call = mutated_mod.get_global_var('func_4069')
call_6135 = relay.TupleGetItem(func_4068_call(), 0)
call_6136 = relay.TupleGetItem(func_4069_call(), 0)
output = call_6135
output2 = call_6136
func_6153 = relay.Function([], output)
mod['func_6153'] = func_6153
mod = relay.transform.InferType()(mod)
output = func_6153()
func_6154 = relay.Function([], output)
mutated_mod['func_6154'] = func_6154
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1940_call = mod.get_global_var('func_1940')
func_1941_call = mutated_mod.get_global_var('func_1941')
call_6204 = func_1940_call()
call_6205 = func_1940_call()
output = call_6204
output2 = call_6205
func_6218 = relay.Function([], output)
mod['func_6218'] = func_6218
mod = relay.transform.InferType()(mod)
output = func_6218()
func_6219 = relay.Function([], output)
mutated_mod['func_6219'] = func_6219
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5765_call = mod.get_global_var('func_5765')
func_5766_call = mutated_mod.get_global_var('func_5766')
call_6220 = relay.TupleGetItem(func_5765_call(), 0)
call_6221 = relay.TupleGetItem(func_5766_call(), 0)
uop_6226 = relay.log10(call_6220.astype('float32')) # shape=(13, 5, 9)
uop_6228 = relay.log10(call_6221.astype('float32')) # shape=(13, 5, 9)
func_2461_call = mod.get_global_var('func_2461')
func_2462_call = mutated_mod.get_global_var('func_2462')
call_6236 = func_2461_call()
call_6237 = func_2461_call()
func_1782_call = mod.get_global_var('func_1782')
func_1784_call = mutated_mod.get_global_var('func_1784')
const_6243 = relay.const([[8.339967,-3.006299,2.146572,-7.952725,-3.168645,0.400030,5.600427,2.760313,5.617347,8.654557,-9.815639,-1.292519,-1.613874,9.990883,9.566877,-3.468936,-3.630874,7.385339,7.181688,2.002017,0.626175,4.085067,-2.117462,7.307157,-6.475810,-1.160488,7.032525,4.061973,-8.454377,-7.155653,-5.991506,-5.038596,9.378530,-0.518678,-9.622314,-8.640432,1.128511,-6.809956,2.073594,9.071257,8.175221,-3.916409,-7.336372,-8.598697,2.362121,-1.345705,8.051519,-4.579534,-9.022436,0.509837,-7.850226,-0.197984,-6.409819,-5.790496,9.773650,9.931451,6.325770,2.541826,4.625354,3.197950,-1.019201,-6.868709,-6.678488,8.630129,-0.075474,9.139745,-4.594757,-5.544871,4.691198,-5.841274,-8.113969,9.178783,-8.258578,1.808009,-1.758253,-3.303143,-8.360787,-5.784816,6.906897,7.448796,-3.116803,2.859494,-5.806523,1.002412,-1.824023,-0.644021,5.629348,-8.849471],[-7.558656,3.121847,-5.221153,-3.109474,9.776142,-2.507813,-0.245672,-2.057756,-6.791535,1.305976,1.554111,-2.599264,8.258885,-3.275613,-9.526000,-7.568179,-4.149592,0.882920,9.131456,8.222402,-3.704284,6.587181,5.470591,-6.485405,7.018497,-9.996235,-5.504842,-1.059908,-0.102752,6.129241,-3.039621,5.647942,9.818156,9.631214,-3.933161,7.404121,-4.132795,4.368954,-3.768216,-2.072813,-1.830654,-9.143239,3.947367,-1.685425,4.871983,7.558168,6.881379,-2.682059,3.023001,3.848407,-7.706344,3.215090,5.996617,-3.877795,-1.139363,-7.060383,-6.942234,6.116312,4.610398,4.786371,3.498916,-9.218177,1.282351,-5.156483,1.153645,2.464297,-3.464997,-3.306476,3.530965,-5.269712,5.621334,-5.904344,8.197696,-0.604257,2.167031,-4.801121,-4.295447,9.749649,8.981540,-6.365905,4.153913,1.150558,-5.797285,-5.192630,-0.437400,7.543189,9.980763,1.809706],[-1.663061,3.090172,0.301931,-0.106036,5.468609,-3.679621,9.956196,2.718752,-2.457839,5.145775,-5.315822,-4.050700,-1.224555,2.425414,-1.303727,-6.102756,-3.140644,-0.410743,5.112822,2.960954,3.855947,-0.247623,-6.314229,1.426844,-5.530948,-8.477416,-3.224795,4.582598,-8.074696,-1.932321,-8.460253,4.442725,7.824840,-9.947123,2.789464,3.331965,1.162349,6.380651,2.868972,-4.191552,6.407390,-5.850671,-5.105862,-2.951969,-3.778440,4.221762,-5.670203,5.889688,-8.796546,-0.353961,7.874696,-5.105075,5.921562,6.267163,2.559083,-4.563108,-8.714109,-9.985391,7.471807,5.502359,-4.572256,-9.650225,-7.267014,-8.656538,3.674817,-2.905267,-3.227405,-4.819343,-8.747315,-0.105613,4.648592,0.961951,3.460825,-1.664007,-9.847830,7.346813,-3.179165,0.751825,5.700626,-1.477082,1.298184,-2.287258,3.806448,1.735770,-8.071328,4.869113,4.804134,4.941391],[2.639410,4.260971,8.935845,-8.874845,-9.764288,-0.117100,7.072314,-7.629657,7.319926,-6.672813,6.657845,1.141426,2.680980,-7.734008,1.728334,7.099158,6.962774,-1.219820,9.944783,6.709103,2.632017,-2.093979,-6.198570,1.055111,5.534121,-2.397458,0.212370,-4.448145,8.441373,8.014449,-4.424300,6.847089,3.265246,-8.669755,-2.209151,-3.596205,-9.475059,-1.995794,-2.374996,-6.746247,2.155692,-3.246416,-6.515307,8.593641,6.618167,-8.389000,5.650325,-6.010552,-9.455586,-6.057446,-1.826543,-9.492890,9.783611,2.361562,-1.469444,6.942835,-9.879264,-0.176016,-3.233010,-9.698942,9.062978,2.067158,-5.038387,0.460731,-5.014914,4.746166,7.615995,0.079467,-1.813199,-2.964984,4.664381,-1.926091,9.927323,-1.350443,-2.655584,-0.017081,-3.877794,2.822917,7.002624,8.730275,-2.524586,-7.368047,-0.788962,-5.387278,-0.363821,5.778413,-5.504323,8.124748],[-0.686130,3.955470,8.420647,-6.955316,0.180095,-4.755200,0.517365,-3.650800,9.628842,3.090372,1.581776,-3.909061,-3.068479,7.485317,-6.085962,-9.990109,-0.661285,6.414097,6.298028,0.747740,6.916828,6.129337,9.642151,-8.559174,-6.635610,-1.307758,9.059489,7.555846,-1.718849,-3.515501,-7.142016,-7.264648,-2.890848,-7.652471,0.702728,-5.514165,2.971336,1.185587,-9.700738,3.343839,3.730565,-9.176804,4.085248,-5.683762,-3.733057,-6.001379,-9.919461,0.726622,-3.636401,-7.233627,-2.445803,5.882722,5.724852,-7.538845,-2.679878,-2.879882,-5.291797,6.414662,6.125881,2.612022,-7.944456,-1.584432,-7.792942,-5.296760,7.916809,1.890036,3.737424,7.292220,2.355732,-9.328305,-6.713567,-8.448488,3.968202,-7.742693,7.625338,-6.728467,9.535118,-9.009647,6.716401,-4.647427,-4.470539,-5.051686,-6.410696,-8.231518,5.491948,-5.369907,8.801857,-7.875981]], dtype = "float32")#candidate|6243|(5, 88)|const|float32
call_6242 = relay.TupleGetItem(func_1782_call(relay.reshape(const_6243.astype('float32'), [4, 10, 11])), 1)
call_6244 = relay.TupleGetItem(func_1784_call(relay.reshape(const_6243.astype('float32'), [4, 10, 11])), 1)
func_2935_call = mod.get_global_var('func_2935')
func_2938_call = mutated_mod.get_global_var('func_2938')
call_6250 = relay.TupleGetItem(func_2935_call(relay.reshape(call_6220.astype('float64'), [13, 5, 9])), 3)
call_6251 = relay.TupleGetItem(func_2938_call(relay.reshape(call_6220.astype('float64'), [13, 5, 9])), 3)
output = relay.Tuple([uop_6226,call_6236,call_6242,const_6243,call_6250,])
output2 = relay.Tuple([uop_6228,call_6237,call_6244,const_6243,call_6251,])
func_6252 = relay.Function([], output)
mod['func_6252'] = func_6252
mod = relay.transform.InferType()(mod)
output = func_6252()
func_6253 = relay.Function([], output)
mutated_mod['func_6253'] = func_6253
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5610_call = mod.get_global_var('func_5610')
func_5612_call = mutated_mod.get_global_var('func_5612')
call_6262 = func_5610_call()
call_6263 = func_5610_call()
output = relay.Tuple([call_6262,])
output2 = relay.Tuple([call_6263,])
func_6280 = relay.Function([], output)
mod['func_6280'] = func_6280
mod = relay.transform.InferType()(mod)
output = func_6280()
func_6281 = relay.Function([], output)
mutated_mod['func_6281'] = func_6281
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6295 = relay.const([[[8.657626],[3.494508]],[[0.876093],[3.554921]],[[-1.624401],[6.342084]],[[6.891709],[8.866809]],[[-5.693095],[-5.871762]],[[-4.975301],[-9.503297]],[[-3.701026],[-1.043049]],[[8.087367],[9.664895]],[[-3.240473],[4.274194]]], dtype = "float32")#candidate|6295|(9, 2, 1)|const|float32
uop_6296 = relay.cosh(const_6295.astype('float32')) # shape=(9, 2, 1)
func_5276_call = mod.get_global_var('func_5276')
func_5280_call = mutated_mod.get_global_var('func_5280')
var_6308 = relay.var("var_6308", dtype = "float64", shape = (200,))#candidate|6308|(200,)|var|float64
const_6309 = relay.const([-6.502338,-1.158350,-7.364657,-3.318043,0.817869,3.651358,3.247808,-5.513576,4.039939,-9.892733,-9.775799,3.890212,-9.062928,8.818254,-1.464365,-2.004201,-6.499102,9.187819,-8.328327,5.860460,6.184523,4.297862,-1.282567,9.055620,2.270764,8.478132,-9.846060,-2.014242,-2.550895,8.850835,-3.877943,4.305785,-4.536065,0.613007,-0.057494,-4.548102,4.733877,1.652694,9.788462,-3.633299,-9.183325,9.069779,-8.529426,9.675838,1.599057,-4.215886,-6.730905,0.034914,-1.581973,1.489357,9.123269,-4.646137,-0.631913,6.483356,-4.857814,-6.770360,8.929648,-7.527829,9.866898,-7.598543,-6.614504,-3.391307,-1.239880,0.670676,-7.963121,-4.013998,1.301391,-9.162953,-4.070477,7.110345,9.039096,9.951448,0.272940,0.681223,9.044030,-7.016976,-3.065148,-6.116368,-6.644326,2.960083,-6.028881,-6.068631,-6.388115,5.308954,-8.499675,4.046767,-8.811323,7.735244,-3.425874,-7.954768,-3.575229,3.059349,0.207593,-6.433108,-0.041818,-9.278933,2.790936,-1.954034,-4.138291,-5.802439,-0.371622,-6.395172,-1.048601,3.583711,-8.352139,-3.120257,-7.988651,6.219093,5.604282,7.768028,6.784646,-6.295375,-4.259461,-1.778306,1.158287,-4.080962,0.651615,-3.913321,-3.894704,-8.753659,-9.805123,0.564703,9.238350,-5.013173,-6.553419,-5.704175,-9.213304,-5.194681,7.682245,6.800736,7.422910,-0.609751,-9.470681,-8.444143,-6.976125,-3.472811,1.606195,5.142045,-4.954786,4.379232,2.123915,8.631765,7.644188,2.367430,-5.289613,7.343476,-9.584743,-3.428088,-9.018140,5.606839,-5.716502,6.973650,2.258974,-9.786361,4.644123,2.206659,2.160346,-6.134750,-2.948586,1.902146,-8.159712,2.737956,-1.332532,5.057360,-8.253641,-1.319369,-3.059280,0.508830,-3.756656,-3.657691,3.038478,1.124957,-6.985951,6.507534,3.462709,9.690720,0.446773,-1.472829,2.819199,9.859942,-4.683351,-1.193187,8.851424,-8.570519,7.137895,4.449783,-6.533964,8.212820,-1.832193,-5.694959,4.467102,8.588484,-1.368794,-3.747712,-8.938684,4.682889,1.170092,4.311946,5.395605,9.770152,-2.726168,-9.887723,6.196828,2.742101,-6.675799,9.590437,-8.369063,3.569091,-1.749529,-1.766890,2.217668,0.479229,5.196659,9.410319,-5.965533,0.366212,-9.870876,-3.465006,8.242297,0.444825,4.485287,9.821330,-4.734275,-4.812126,-0.797848,4.461561,-6.819943,7.106432,4.585948,3.632520,3.909311,7.748655,-3.327729,6.013608,8.090655,8.242363,4.341558,-2.020050,2.887700,-3.739846,8.146038,7.344141,-9.089139,9.546955,-0.940786,6.782777,0.683680,0.439930,-5.907457,1.247561,6.519861,-2.338359,9.783744,-4.227667,7.953700,9.645329,-4.288372,6.415878,4.070171,8.700540,2.742183,1.316057,0.485708,-2.143838,5.503792,3.153821,-6.013308,7.497623,7.274469,5.093957,-6.396629,4.546648,8.629195,0.874080,-4.691098,-0.737257,6.419194,-7.782182,-3.640961,7.579229,5.600742,1.537959,-2.615339,7.572386,-6.857933,6.421902,3.656990,-4.301380], dtype = "float32")#candidate|6309|(288,)|const|float32
call_6307 = relay.TupleGetItem(func_5276_call(relay.reshape(var_6308.astype('float64'), [50, 4]), relay.reshape(const_6309.astype('float32'), [288,]), ), 1)
call_6310 = relay.TupleGetItem(func_5280_call(relay.reshape(var_6308.astype('float64'), [50, 4]), relay.reshape(const_6309.astype('float32'), [288,]), ), 1)
func_3697_call = mod.get_global_var('func_3697')
func_3698_call = mutated_mod.get_global_var('func_3698')
call_6322 = relay.TupleGetItem(func_3697_call(), 1)
call_6323 = relay.TupleGetItem(func_3698_call(), 1)
output = relay.Tuple([uop_6296,call_6307,var_6308,const_6309,call_6322,])
output2 = relay.Tuple([uop_6296,call_6310,var_6308,const_6309,call_6323,])
func_6324 = relay.Function([var_6308,], output)
mod['func_6324'] = func_6324
mod = relay.transform.InferType()(mod)
mutated_mod['func_6324'] = func_6324
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6325 = relay.var("var_6325", dtype = "float64", shape = (200,))#candidate|6325|(200,)|var|float64
func_6324_call = mutated_mod.get_global_var('func_6324')
call_6326 = func_6324_call(var_6325)
output = call_6326
func_6327 = relay.Function([var_6325], output)
mutated_mod['func_6327'] = func_6327
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1575_call = mod.get_global_var('func_1575')
func_1576_call = mutated_mod.get_global_var('func_1576')
call_6334 = func_1575_call()
call_6335 = func_1575_call()
func_3068_call = mod.get_global_var('func_3068')
func_3070_call = mutated_mod.get_global_var('func_3070')
var_6337 = relay.var("var_6337", dtype = "uint16", shape = (2, 528))#candidate|6337|(2, 528)|var|uint16
call_6336 = func_3068_call(relay.reshape(var_6337.astype('uint16'), [12, 8, 11]))
call_6338 = func_3068_call(relay.reshape(var_6337.astype('uint16'), [12, 8, 11]))
output = relay.Tuple([call_6334,call_6336,var_6337,])
output2 = relay.Tuple([call_6335,call_6338,var_6337,])
func_6341 = relay.Function([var_6337,], output)
mod['func_6341'] = func_6341
mod = relay.transform.InferType()(mod)
mutated_mod['func_6341'] = func_6341
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6342 = relay.var("var_6342", dtype = "uint16", shape = (2, 528))#candidate|6342|(2, 528)|var|uint16
func_6341_call = mutated_mod.get_global_var('func_6341')
call_6343 = func_6341_call(var_6342)
output = call_6343
func_6344 = relay.Function([var_6342], output)
mutated_mod['func_6344'] = func_6344
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4026_call = mod.get_global_var('func_4026')
func_4028_call = mutated_mod.get_global_var('func_4028')
call_6351 = relay.TupleGetItem(func_4026_call(), 0)
call_6352 = relay.TupleGetItem(func_4028_call(), 0)
func_4357_call = mod.get_global_var('func_4357')
func_4360_call = mutated_mod.get_global_var('func_4360')
const_6365 = relay.const([[True,True,False,True],[True,True,False,False],[False,False,True,True],[False,False,False,True],[True,True,False,False],[False,True,True,True],[True,False,True,False],[False,True,False,True],[False,False,False,True],[True,True,True,True],[True,False,True,True],[False,True,True,True],[False,True,True,True],[False,False,False,True],[True,False,False,True],[True,False,True,True],[False,True,False,True],[False,True,True,True],[True,False,True,True],[True,False,False,True],[True,False,False,False],[False,True,True,True],[True,True,True,False],[True,False,True,True],[True,True,True,False],[False,False,True,True],[False,False,False,True],[False,False,False,False],[False,True,False,True],[False,True,False,True],[True,True,True,False],[True,False,False,True],[True,True,True,True],[True,False,False,True],[True,False,False,True],[False,False,True,True],[True,True,False,True],[True,False,False,False],[False,True,False,True],[True,False,False,False],[True,True,True,False],[False,True,True,True],[True,True,False,False],[False,False,True,True],[True,True,True,False],[True,True,False,True],[True,True,True,False],[True,True,True,True],[True,False,True,True],[False,True,False,True],[False,False,True,False],[False,False,False,False],[True,True,False,True],[False,True,False,True],[False,True,False,True],[True,True,False,False],[True,False,True,True],[True,True,True,True],[True,False,False,False],[True,False,False,False],[True,False,True,True],[True,False,True,True],[True,True,True,False],[False,True,False,True],[True,True,True,False],[False,False,False,False],[False,False,False,True],[False,False,False,True],[False,True,False,False],[True,True,True,True],[False,False,True,False],[False,False,False,True],[True,True,False,False],[True,False,False,True],[False,False,True,False],[False,True,True,False],[False,True,False,False],[True,False,True,True],[False,False,False,False],[False,False,False,False],[True,False,False,False],[False,False,True,False],[False,False,False,False],[True,True,False,False],[False,True,False,True],[True,True,True,True],[True,True,False,False],[True,False,False,False],[False,False,False,False],[False,True,False,False],[False,False,False,True],[True,False,True,True],[True,True,True,False],[False,False,False,False],[True,False,False,False],[False,False,False,False],[False,False,False,False],[True,False,False,True],[False,False,True,True],[False,False,False,False],[False,True,False,False],[True,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,True,False],[False,False,True,True],[True,False,True,True],[True,True,True,True],[False,False,True,False],[False,False,True,True],[False,True,True,True],[False,False,True,False],[False,False,True,True],[True,False,False,False],[False,True,True,False],[False,False,True,False],[False,False,True,True],[False,False,False,True],[True,True,False,True],[True,True,False,False],[True,True,True,False],[True,True,False,False],[False,True,False,False],[False,True,True,False],[True,False,True,False],[False,True,True,True],[True,True,True,False],[False,True,False,True],[False,True,False,True],[False,False,True,False],[False,True,True,False],[False,False,False,False],[False,False,False,False],[True,True,True,False],[False,False,True,False],[True,True,True,True],[True,True,True,True],[False,False,False,False],[False,True,False,False],[True,False,False,True],[False,False,True,False],[True,False,False,True],[True,True,True,False]], dtype = "bool")#candidate|6365|(144, 4)|const|bool
call_6364 = relay.TupleGetItem(func_4357_call(relay.reshape(call_6351.astype('float32'), [13, 5, 9]), relay.reshape(const_6365.astype('bool'), [576,]), ), 0)
call_6366 = relay.TupleGetItem(func_4360_call(relay.reshape(call_6351.astype('float32'), [13, 5, 9]), relay.reshape(const_6365.astype('bool'), [576,]), ), 0)
output = relay.Tuple([call_6351,call_6364,const_6365,])
output2 = relay.Tuple([call_6352,call_6366,const_6365,])
func_6389 = relay.Function([], output)
mod['func_6389'] = func_6389
mod = relay.transform.InferType()(mod)
mutated_mod['func_6389'] = func_6389
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6389_call = mutated_mod.get_global_var('func_6389')
call_6390 = func_6389_call()
output = call_6390
func_6391 = relay.Function([], output)
mutated_mod['func_6391'] = func_6391
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3211_call = mod.get_global_var('func_3211')
func_3212_call = mutated_mod.get_global_var('func_3212')
call_6436 = func_3211_call()
call_6437 = func_3211_call()
var_6451 = relay.var("var_6451", dtype = "float32", shape = (13, 5, 9))#candidate|6451|(13, 5, 9)|var|float32
bop_6452 = relay.maximum(call_6436.astype('int8'), relay.reshape(var_6451.astype('int8'), relay.shape_of(call_6436))) # shape=(13, 5, 9)
bop_6455 = relay.maximum(call_6437.astype('int8'), relay.reshape(var_6451.astype('int8'), relay.shape_of(call_6437))) # shape=(13, 5, 9)
func_3285_call = mod.get_global_var('func_3285')
func_3287_call = mutated_mod.get_global_var('func_3287')
call_6458 = relay.TupleGetItem(func_3285_call(), 0)
call_6459 = relay.TupleGetItem(func_3287_call(), 0)
func_1257_call = mod.get_global_var('func_1257')
func_1258_call = mutated_mod.get_global_var('func_1258')
call_6464 = func_1257_call()
call_6465 = func_1257_call()
func_1302_call = mod.get_global_var('func_1302')
func_1303_call = mutated_mod.get_global_var('func_1303')
call_6513 = func_1302_call()
call_6514 = func_1302_call()
output = relay.Tuple([bop_6452,call_6458,call_6464,call_6513,])
output2 = relay.Tuple([bop_6455,call_6459,call_6465,call_6514,])
func_6515 = relay.Function([var_6451,], output)
mod['func_6515'] = func_6515
mod = relay.transform.InferType()(mod)
mutated_mod['func_6515'] = func_6515
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6516 = relay.var("var_6516", dtype = "float32", shape = (13, 5, 9))#candidate|6516|(13, 5, 9)|var|float32
func_6515_call = mutated_mod.get_global_var('func_6515')
call_6517 = func_6515_call(var_6516)
output = call_6517
func_6518 = relay.Function([var_6516], output)
mutated_mod['func_6518'] = func_6518
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2235_call = mod.get_global_var('func_2235')
func_2236_call = mutated_mod.get_global_var('func_2236')
call_6523 = relay.TupleGetItem(func_2235_call(), 0)
call_6524 = relay.TupleGetItem(func_2236_call(), 0)
var_6525 = relay.var("var_6525", dtype = "float64", shape = (13, 5, 9))#candidate|6525|(13, 5, 9)|var|float64
bop_6526 = relay.bitwise_and(call_6523.astype('uint8'), relay.reshape(var_6525.astype('uint8'), relay.shape_of(call_6523))) # shape=(13, 5, 9)
bop_6529 = relay.bitwise_and(call_6524.astype('uint8'), relay.reshape(var_6525.astype('uint8'), relay.shape_of(call_6524))) # shape=(13, 5, 9)
var_6531 = relay.var("var_6531", dtype = "uint8", shape = (13, 5, 9))#candidate|6531|(13, 5, 9)|var|uint8
bop_6532 = relay.logical_or(bop_6526.astype('bool'), relay.reshape(var_6531.astype('bool'), relay.shape_of(bop_6526))) # shape=(13, 5, 9)
bop_6535 = relay.logical_or(bop_6529.astype('bool'), relay.reshape(var_6531.astype('bool'), relay.shape_of(bop_6529))) # shape=(13, 5, 9)
output = relay.Tuple([bop_6532,])
output2 = relay.Tuple([bop_6535,])
func_6542 = relay.Function([var_6525,var_6531,], output)
mod['func_6542'] = func_6542
mod = relay.transform.InferType()(mod)
mutated_mod['func_6542'] = func_6542
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6542_call = mutated_mod.get_global_var('func_6542')
var_6544 = relay.var("var_6544", dtype = "float64", shape = (13, 5, 9))#candidate|6544|(13, 5, 9)|var|float64
var_6545 = relay.var("var_6545", dtype = "uint8", shape = (13, 5, 9))#candidate|6545|(13, 5, 9)|var|uint8
call_6543 = func_6542_call(var_6544,var_6545,)
output = call_6543
func_6546 = relay.Function([var_6544,var_6545,], output)
mutated_mod['func_6546'] = func_6546
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2461_call = mod.get_global_var('func_2461')
func_2462_call = mutated_mod.get_global_var('func_2462')
call_6550 = func_2461_call()
call_6551 = func_2461_call()
output = call_6550
output2 = call_6551
func_6562 = relay.Function([], output)
mod['func_6562'] = func_6562
mod = relay.transform.InferType()(mod)
mutated_mod['func_6562'] = func_6562
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6562_call = mutated_mod.get_global_var('func_6562')
call_6563 = func_6562_call()
output = call_6563
func_6564 = relay.Function([], output)
mutated_mod['func_6564'] = func_6564
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2172_call = mod.get_global_var('func_2172')
func_2173_call = mutated_mod.get_global_var('func_2173')
call_6569 = relay.TupleGetItem(func_2172_call(), 1)
call_6570 = relay.TupleGetItem(func_2173_call(), 1)
var_6576 = relay.var("var_6576", dtype = "uint8", shape = (169,))#candidate|6576|(169,)|var|uint8
bop_6577 = relay.logical_and(call_6569.astype('bool'), relay.reshape(var_6576.astype('bool'), relay.shape_of(call_6569))) # shape=(169,)
bop_6580 = relay.logical_and(call_6570.astype('bool'), relay.reshape(var_6576.astype('bool'), relay.shape_of(call_6570))) # shape=(169,)
uop_6589 = relay.acos(var_6576.astype('float64')) # shape=(169,)
bop_6594 = relay.floor_divide(uop_6589.astype('float64'), relay.reshape(call_6569.astype('float64'), relay.shape_of(uop_6589))) # shape=(169,)
bop_6597 = relay.floor_divide(uop_6589.astype('float64'), relay.reshape(call_6570.astype('float64'), relay.shape_of(uop_6589))) # shape=(169,)
output = relay.Tuple([bop_6577,bop_6594,])
output2 = relay.Tuple([bop_6580,bop_6597,])
func_6599 = relay.Function([var_6576,], output)
mod['func_6599'] = func_6599
mod = relay.transform.InferType()(mod)
mutated_mod['func_6599'] = func_6599
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6600 = relay.var("var_6600", dtype = "uint8", shape = (169,))#candidate|6600|(169,)|var|uint8
func_6599_call = mutated_mod.get_global_var('func_6599')
call_6601 = func_6599_call(var_6600)
output = call_6601
func_6602 = relay.Function([var_6600], output)
mutated_mod['func_6602'] = func_6602
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1424_call = mod.get_global_var('func_1424')
func_1426_call = mutated_mod.get_global_var('func_1426')
call_6671 = relay.TupleGetItem(func_1424_call(), 4)
call_6672 = relay.TupleGetItem(func_1426_call(), 4)
output = relay.Tuple([call_6671,])
output2 = relay.Tuple([call_6672,])
func_6677 = relay.Function([], output)
mod['func_6677'] = func_6677
mod = relay.transform.InferType()(mod)
output = func_6677()
func_6678 = relay.Function([], output)
mutated_mod['func_6678'] = func_6678
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6389_call = mod.get_global_var('func_6389')
func_6391_call = mutated_mod.get_global_var('func_6391')
call_6704 = relay.TupleGetItem(func_6389_call(), 1)
call_6705 = relay.TupleGetItem(func_6391_call(), 1)
output = call_6704
output2 = call_6705
func_6729 = relay.Function([], output)
mod['func_6729'] = func_6729
mod = relay.transform.InferType()(mod)
mutated_mod['func_6729'] = func_6729
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6729_call = mutated_mod.get_global_var('func_6729')
call_6730 = func_6729_call()
output = call_6730
func_6731 = relay.Function([], output)
mutated_mod['func_6731'] = func_6731
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1257_call = mod.get_global_var('func_1257')
func_1258_call = mutated_mod.get_global_var('func_1258')
call_6761 = func_1257_call()
call_6762 = func_1257_call()
output = relay.Tuple([call_6761,])
output2 = relay.Tuple([call_6762,])
func_6799 = relay.Function([], output)
mod['func_6799'] = func_6799
mod = relay.transform.InferType()(mod)
output = func_6799()
func_6800 = relay.Function([], output)
mutated_mod['func_6800'] = func_6800
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5037_call = mod.get_global_var('func_5037')
func_5039_call = mutated_mod.get_global_var('func_5039')
call_6832 = relay.TupleGetItem(func_5037_call(), 1)
call_6833 = relay.TupleGetItem(func_5039_call(), 1)
var_6840 = relay.var("var_6840", dtype = "float64", shape = (13, 5, 9))#candidate|6840|(13, 5, 9)|var|float64
bop_6841 = relay.right_shift(call_6832.astype('uint32'), relay.reshape(var_6840.astype('uint32'), relay.shape_of(call_6832))) # shape=(13, 5, 9)
bop_6844 = relay.right_shift(call_6833.astype('uint32'), relay.reshape(var_6840.astype('uint32'), relay.shape_of(call_6833))) # shape=(13, 5, 9)
output = bop_6841
output2 = bop_6844
func_6857 = relay.Function([var_6840,], output)
mod['func_6857'] = func_6857
mod = relay.transform.InferType()(mod)
mutated_mod['func_6857'] = func_6857
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6858 = relay.var("var_6858", dtype = "float64", shape = (13, 5, 9))#candidate|6858|(13, 5, 9)|var|float64
func_6857_call = mutated_mod.get_global_var('func_6857')
call_6859 = func_6857_call(var_6858)
output = call_6859
func_6860 = relay.Function([var_6858], output)
mutated_mod['func_6860'] = func_6860
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3262_call = mod.get_global_var('func_3262')
func_3263_call = mutated_mod.get_global_var('func_3263')
call_6880 = func_3262_call()
call_6881 = func_3262_call()
uop_6918 = relay.cos(call_6880.astype('float64')) # shape=(13, 5, 9)
uop_6920 = relay.cos(call_6881.astype('float64')) # shape=(13, 5, 9)
func_1940_call = mod.get_global_var('func_1940')
func_1941_call = mutated_mod.get_global_var('func_1941')
call_6926 = func_1940_call()
call_6927 = func_1940_call()
func_511_call = mod.get_global_var('func_511')
func_515_call = mutated_mod.get_global_var('func_515')
const_6931 = relay.const(-10, dtype = "uint8")#candidate|6931|()|const|uint8
const_6932 = relay.const([-1,2,-8,1,-1,-4,7,-3,7,-4,-2,-3,3,8,-8,-5,-2,10,-8,-3,-1,-9,-6,5,10,6,-4,-1,-10,-4,-6,7,8,9,-6,2,-9,8,-5,-9,-10,9,5,3,-10,4,-6,3,-6,-9,-5,4,3,-9,4,-7,2,8,-7,3,-10,5,-7,1,3,10,10,-1,-5,-3,-8,-1,8,10,-4,5,1,1,10,-5,-3,-10,8,-8,-2,2,-1,2,6,-7,4,-6,1,5,1,-2,-5,-9,-6,10,8,-9,6,-10,-3,5,-8,4,-8,1,-9,6,-7,-8,10,10,9,8,-1,10,-3,3,5,1,6,-5,-4,10,-7,-4,-8,4,-4,-5,-1,8,9,5,9,-9,5,10,8,1,-8,-2,-1,-4,-1,9,3,5,-1,9,-4,4,4,-1,2,8,8,8,6,-4,10,-8,3,6,4], dtype = "uint8")#candidate|6932|(169,)|const|uint8
call_6930 = relay.TupleGetItem(func_511_call(relay.reshape(const_6931.astype('uint8'), []), relay.reshape(const_6932.astype('uint8'), [13, 1, 13]), relay.reshape(call_6926.astype('bool'), [576,]), ), 1)
call_6933 = relay.TupleGetItem(func_515_call(relay.reshape(const_6931.astype('uint8'), []), relay.reshape(const_6932.astype('uint8'), [13, 1, 13]), relay.reshape(call_6926.astype('bool'), [576,]), ), 1)
func_6280_call = mod.get_global_var('func_6280')
func_6281_call = mutated_mod.get_global_var('func_6281')
call_6946 = relay.TupleGetItem(func_6280_call(), 0)
call_6947 = relay.TupleGetItem(func_6281_call(), 0)
func_4888_call = mod.get_global_var('func_4888')
func_4889_call = mutated_mod.get_global_var('func_4889')
call_6949 = relay.TupleGetItem(func_4888_call(), 4)
call_6950 = relay.TupleGetItem(func_4889_call(), 4)
uop_6953 = relay.sin(const_6932.astype('float64')) # shape=(169,)
func_5382_call = mod.get_global_var('func_5382')
func_5384_call = mutated_mod.get_global_var('func_5384')
var_6956 = relay.var("var_6956", dtype = "float32", shape = (288,))#candidate|6956|(288,)|var|float32
call_6955 = relay.TupleGetItem(func_5382_call(relay.reshape(var_6956.astype('float32'), [288,])), 3)
call_6957 = relay.TupleGetItem(func_5384_call(relay.reshape(var_6956.astype('float32'), [288,])), 3)
output = relay.Tuple([uop_6918,call_6926,call_6930,const_6931,call_6946,call_6949,uop_6953,call_6955,var_6956,])
output2 = relay.Tuple([uop_6920,call_6927,call_6933,const_6931,call_6947,call_6950,uop_6953,call_6957,var_6956,])
func_6959 = relay.Function([var_6956,], output)
mod['func_6959'] = func_6959
mod = relay.transform.InferType()(mod)
mutated_mod['func_6959'] = func_6959
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6960 = relay.var("var_6960", dtype = "float32", shape = (288,))#candidate|6960|(288,)|var|float32
func_6959_call = mutated_mod.get_global_var('func_6959')
call_6961 = func_6959_call(var_6960)
output = call_6961
func_6962 = relay.Function([var_6960], output)
mutated_mod['func_6962'] = func_6962
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1801_call = mod.get_global_var('func_1801')
func_1802_call = mutated_mod.get_global_var('func_1802')
call_7028 = func_1801_call()
call_7029 = func_1801_call()
func_1940_call = mod.get_global_var('func_1940')
func_1941_call = mutated_mod.get_global_var('func_1941')
call_7034 = func_1940_call()
call_7035 = func_1940_call()
uop_7039 = relay.log(call_7034.astype('float32')) # shape=(576,)
uop_7041 = relay.log(call_7035.astype('float32')) # shape=(576,)
output = relay.Tuple([call_7028,uop_7039,])
output2 = relay.Tuple([call_7029,uop_7041,])
func_7055 = relay.Function([], output)
mod['func_7055'] = func_7055
mod = relay.transform.InferType()(mod)
mutated_mod['func_7055'] = func_7055
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7055_call = mutated_mod.get_global_var('func_7055')
call_7056 = func_7055_call()
output = call_7056
func_7057 = relay.Function([], output)
mutated_mod['func_7057'] = func_7057
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4419_call = mod.get_global_var('func_4419')
func_4421_call = mutated_mod.get_global_var('func_4421')
call_7171 = func_4419_call()
call_7172 = func_4419_call()
output = call_7171
output2 = call_7172
func_7192 = relay.Function([], output)
mod['func_7192'] = func_7192
mod = relay.transform.InferType()(mod)
output = func_7192()
func_7193 = relay.Function([], output)
mutated_mod['func_7193'] = func_7193
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7305 = relay.const([[[7.824300,1.274707],[0.811244,-4.967195],[-1.632591,-5.895871],[-8.358451,-1.562073],[3.550262,5.066298],[-1.039092,1.641089],[2.756948,9.184831]],[[7.854191,5.874992],[3.167350,-6.887327],[-9.441700,-1.107365],[-6.942310,9.182094],[-1.604673,4.304849],[-5.404490,-4.381059],[-7.475395,9.256598]],[[-9.976684,-0.526962],[8.089471,5.578196],[-7.612957,3.089050],[-7.182364,7.612927],[5.286254,-2.488068],[-1.013803,6.388031],[-2.436085,1.624792]],[[-4.013108,-7.330650],[1.458915,-3.191218],[-3.435923,-4.369823],[8.595999,6.411543],[7.052567,-9.006863],[9.113526,-1.082822],[-2.914476,4.218241]],[[5.850364,-6.749560],[3.059420,8.767191],[2.557907,7.774200],[2.992914,-0.107806],[-4.181544,-9.547902],[-9.834090,-8.282759],[1.878817,1.004815]],[[-1.203929,-0.660950],[-5.310546,4.263105],[-4.585712,-9.019177],[2.446838,2.021586],[8.581358,5.140635],[-4.019242,4.630753],[0.224703,-4.211096]],[[-0.219599,-3.924359],[-2.436860,2.309512],[3.292568,-5.837487],[2.060367,2.253488],[2.295387,2.521094],[-0.939621,-6.646553],[-2.385412,8.760283]],[[9.240346,2.857290],[-8.439045,-0.887053],[-7.563384,0.689229],[4.366279,7.395974],[-1.599606,5.522677],[-6.630893,2.743027],[2.428707,8.742640]],[[9.701263,9.110491],[-0.769824,9.443533],[1.292329,-1.035437],[9.418683,3.640380],[6.886289,2.450598],[-2.899132,6.496855],[1.460840,9.385934]]], dtype = "float64")#candidate|7305|(9, 7, 2)|const|float64
uop_7306 = relay.cosh(const_7305.astype('float64')) # shape=(9, 7, 2)
bop_7308 = relay.divide(const_7305.astype('float32'), relay.reshape(uop_7306.astype('float32'), relay.shape_of(const_7305))) # shape=(9, 7, 2)
func_3541_call = mod.get_global_var('func_3541')
func_3543_call = mutated_mod.get_global_var('func_3543')
var_7316 = relay.var("var_7316", dtype = "float64", shape = (2080,))#candidate|7316|(2080,)|var|float64
call_7315 = relay.TupleGetItem(func_3541_call(relay.reshape(var_7316.astype('float64'), [13, 16, 10])), 1)
call_7317 = relay.TupleGetItem(func_3543_call(relay.reshape(var_7316.astype('float64'), [13, 16, 10])), 1)
output = relay.Tuple([bop_7308,call_7315,var_7316,])
output2 = relay.Tuple([bop_7308,call_7317,var_7316,])
func_7331 = relay.Function([var_7316,], output)
mod['func_7331'] = func_7331
mod = relay.transform.InferType()(mod)
mutated_mod['func_7331'] = func_7331
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7332 = relay.var("var_7332", dtype = "float64", shape = (2080,))#candidate|7332|(2080,)|var|float64
func_7331_call = mutated_mod.get_global_var('func_7331')
call_7333 = func_7331_call(var_7332)
output = call_7333
func_7334 = relay.Function([var_7332], output)
mutated_mod['func_7334'] = func_7334
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7336 = relay.var("var_7336", dtype = "float64", shape = (1, 4, 7))#candidate|7336|(1, 4, 7)|var|float64
uop_7337 = relay.rsqrt(var_7336.astype('float64')) # shape=(1, 4, 7)
uop_7342 = relay.sin(uop_7337.astype('float32')) # shape=(1, 4, 7)
func_1618_call = mod.get_global_var('func_1618')
func_1621_call = mutated_mod.get_global_var('func_1621')
const_7347 = relay.const([2.320061,-8.052971,-4.003348,0.584932,-3.190954,-8.019147,-1.152792,-7.301763,8.514250,9.324316,-8.192598,-3.094288,-9.887701,4.801766,4.522029,4.003630,8.358545,2.953047,1.522513,-6.747675,-1.833617,1.333558,9.531070,0.146352,-5.900435,-9.722008,5.371258,8.903582,3.251611,-2.702786,-3.138933,3.247987,4.075398,-9.006831,1.161407,-3.447008,8.944180,-1.634372,1.559723,3.859611,1.696397,-2.918970,-5.857113,-5.541736,3.699731,-3.134073,-6.255788,1.909754,-3.117059,5.936558,-0.434457,-0.439318,4.164975,-5.168551,-2.945277,-5.242802,8.733538,-4.744896,-2.893195,8.725553,5.055615,-6.642897,1.652053,6.927871,8.910676,7.609245,-4.787524,1.786814,4.182834,-2.726047,8.260099,5.293293,-6.475736,-7.745535,-9.564730,-6.239016,5.733495,6.161432,-4.468394,3.552857,8.147778,9.619991,-5.882851,4.527780,-8.099953,8.487434,1.309129,7.517383,-9.086248,-3.811367,3.434360,1.684736,0.252552,-1.665506,3.236716,2.169666,-5.926509,5.779829,8.074069,-2.715427,-8.196686,6.868676,-7.385976,3.153873,-5.535018,6.216091,-8.293551,0.304448,-1.672975,7.952589,8.721966,-8.195375,9.074374,-2.756758,3.636739,3.326808,-9.611286,9.039498,6.383701,1.028996,-5.409965,9.481796,5.936705,9.174989,-0.698899,-8.028173,8.823730,-1.964054,-0.867806,-2.793571,3.648480,9.170535,-9.712687,2.663324,-8.499850,-5.392144,9.400609,6.720635,-5.301762,-8.095290,-5.920192,-2.963122,-8.144529,-4.437110,9.888380,-8.092269,-7.751401,-4.982299,-1.240949,-0.748888,-8.425712,9.713814,3.886486,1.682544,5.911155,-5.416127,-8.362552,-9.943273,7.032150,9.164955,8.363990,-0.016960,7.377350,-3.998193,-6.124919,-1.798459,3.694648,-5.793647,7.115283,-0.475027,-6.148408,-5.875779,7.739624,0.848830,7.963793,7.571343,-8.710875,9.486108,-7.526885,5.549445,-6.607847,-7.562423,4.005651,-7.511139,-2.287711,-2.107353,-3.015660,3.347457,5.974404,-1.890045,6.763452,0.856116,4.567306,3.393238,-6.236098,-5.893870,9.988848,7.573463,-4.988608,6.185770], dtype = "float64")#candidate|7347|(200,)|const|float64
call_7346 = relay.TupleGetItem(func_1618_call(relay.reshape(const_7347.astype('float64'), [5, 40])), 1)
call_7348 = relay.TupleGetItem(func_1621_call(relay.reshape(const_7347.astype('float64'), [5, 40])), 1)
output = relay.Tuple([uop_7342,call_7346,const_7347,])
output2 = relay.Tuple([uop_7342,call_7348,const_7347,])
func_7350 = relay.Function([var_7336,], output)
mod['func_7350'] = func_7350
mod = relay.transform.InferType()(mod)
mutated_mod['func_7350'] = func_7350
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7351 = relay.var("var_7351", dtype = "float64", shape = (1, 4, 7))#candidate|7351|(1, 4, 7)|var|float64
func_7350_call = mutated_mod.get_global_var('func_7350')
call_7352 = func_7350_call(var_7351)
output = call_7352
func_7353 = relay.Function([var_7351], output)
mutated_mod['func_7353'] = func_7353
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5037_call = mod.get_global_var('func_5037')
func_5039_call = mutated_mod.get_global_var('func_5039')
call_7374 = relay.TupleGetItem(func_5037_call(), 1)
call_7375 = relay.TupleGetItem(func_5039_call(), 1)
output = relay.Tuple([call_7374,])
output2 = relay.Tuple([call_7375,])
func_7381 = relay.Function([], output)
mod['func_7381'] = func_7381
mod = relay.transform.InferType()(mod)
mutated_mod['func_7381'] = func_7381
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7381_call = mutated_mod.get_global_var('func_7381')
call_7382 = func_7381_call()
output = call_7382
func_7383 = relay.Function([], output)
mutated_mod['func_7383'] = func_7383
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4748_call = mod.get_global_var('func_4748')
func_4749_call = mutated_mod.get_global_var('func_4749')
call_7453 = relay.TupleGetItem(func_4748_call(), 0)
call_7454 = relay.TupleGetItem(func_4749_call(), 0)
output = relay.Tuple([call_7453,])
output2 = relay.Tuple([call_7454,])
func_7460 = relay.Function([], output)
mod['func_7460'] = func_7460
mod = relay.transform.InferType()(mod)
output = func_7460()
func_7461 = relay.Function([], output)
mutated_mod['func_7461'] = func_7461
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7460_call = mod.get_global_var('func_7460')
func_7461_call = mutated_mod.get_global_var('func_7461')
call_7506 = relay.TupleGetItem(func_7460_call(), 0)
call_7507 = relay.TupleGetItem(func_7461_call(), 0)
output = relay.Tuple([call_7506,])
output2 = relay.Tuple([call_7507,])
func_7511 = relay.Function([], output)
mod['func_7511'] = func_7511
mod = relay.transform.InferType()(mod)
output = func_7511()
func_7512 = relay.Function([], output)
mutated_mod['func_7512'] = func_7512
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5765_call = mod.get_global_var('func_5765')
func_5766_call = mutated_mod.get_global_var('func_5766')
call_7543 = relay.TupleGetItem(func_5765_call(), 1)
call_7544 = relay.TupleGetItem(func_5766_call(), 1)
func_2505_call = mod.get_global_var('func_2505')
func_2508_call = mutated_mod.get_global_var('func_2508')
var_7548 = relay.var("var_7548", dtype = "bool", shape = (288, 2))#candidate|7548|(288, 2)|var|bool
call_7547 = func_2505_call(relay.reshape(var_7548.astype('bool'), [9, 4, 16]))
call_7549 = func_2505_call(relay.reshape(var_7548.astype('bool'), [9, 4, 16]))
uop_7557 = relay.asin(call_7547.astype('float64')) # shape=(9, 4, 16)
uop_7559 = relay.asin(call_7549.astype('float64')) # shape=(9, 4, 16)
func_7460_call = mod.get_global_var('func_7460')
func_7461_call = mutated_mod.get_global_var('func_7461')
call_7567 = relay.TupleGetItem(func_7460_call(), 0)
call_7568 = relay.TupleGetItem(func_7461_call(), 0)
func_7331_call = mod.get_global_var('func_7331')
func_7334_call = mutated_mod.get_global_var('func_7334')
const_7571 = relay.const([5.410085,6.198440,4.913817,1.377665,0.856086,-1.010567,5.544592,3.901596,5.332214,8.383133,0.266644,-6.261725,-9.695402,4.307838,-8.424343,4.278629,-7.792767,3.056072,-8.117588,-9.188673,3.271970,-2.938843,6.144998,3.150371,-2.422836,9.065595,7.769320,5.415280,-6.667638,-7.982210,-3.811637,5.220256,-2.695563,-9.743187,4.822245,-0.439191,7.308526,4.149913,-7.471016,-9.013532,4.372991,7.203919,1.501528,6.111797,3.639558,-4.986490,7.842021,-7.702804,8.910617,-3.229472,-9.289913,4.114383,9.149110,-9.541596,-4.305000,6.891922,-8.426621,-9.716319,5.724420,-0.697552,7.924808,-1.052132,-6.900834,-6.392448,-5.280055,-7.768857,2.297978,-6.936156,-2.178070,8.444522,6.566904,6.761279,6.708268,-4.624765,8.265872,7.268731,2.927255,9.162645,-9.745961,2.806003,-0.492108,1.572914,-0.734125,-9.659772,-3.483803,9.305086,-8.791879,-5.368890,-3.977785,-9.371610,5.123762,7.626079,-0.901795,-7.473477,-1.844094,7.871905,9.407072,0.231608,-3.606690,-9.707021,9.762341,0.424541,-4.861185,5.964162,-4.182279,-4.569965,0.338614,-2.785111,-4.517170,-3.603461,0.997319,5.427411,0.388756,-2.838473,9.034282,-7.804084,-1.855887,-0.621119,6.565365,9.124231,-9.752704,1.259873,3.691377,1.223231,-7.572383,9.289115,4.587141,-2.200566,4.539701,-1.378074,-7.055641,7.767564,-0.377949,5.543676,3.762280,7.107737,3.530858,7.511938,5.085265,-7.991314,-9.408285,6.138809,9.924023,-3.951873,-2.323979,5.617289,-6.165504,3.401166,-9.271860,-7.323969,0.734203,1.036525,9.060613,-5.134288,1.564659,-7.305486,-4.572886,4.002996,-6.082614,-7.830066,3.481359,6.265198,-6.285717,-6.313090,2.398581,-3.983807,8.720069,7.305937,-2.391506,8.735182,9.162051,3.502626,5.253602,4.267240,7.274809,-2.874671,2.557432,-4.703551,-3.542433,-8.468434,3.279219,-2.866082,0.066990,0.809288,4.088221,5.844754,2.341186,-2.541134,-8.005187,-5.824315,0.289242,-3.631272,-8.013714,-3.522982,1.419835,-9.959908,3.502965,6.048807,9.696783,-4.530473,6.621755,2.783239,6.122152,5.491962,1.614478,5.227701,-1.682640,0.332106,-5.894978,7.493234,-3.791794,-9.985311,7.203495,-0.186308,6.160534,3.394520,3.710542,1.034304,7.997168,-4.203431,-1.427726,8.794548,2.734631,1.119814,1.360884,3.283473,-9.545710,0.501656,-0.594126,-2.320159,4.014005,-4.290560,-7.358622,6.747314,8.390179,-4.440795,6.163663,-2.536777,-2.186274,-5.983293,2.238131,-2.858595,5.017096,2.820133,1.700950,3.899689,5.210944,7.698431,2.888018,9.259267,-1.252145,-8.856086,-8.611305,-7.484027,-6.605878,-3.797338,8.228129,-5.779314,-8.453127,-4.775006,8.027931,-4.439898,8.781988,0.224127,-3.088940,3.584462,-8.251213,-4.270866,6.202066,-3.048599,3.347105,8.674918,3.994520,-9.656428,8.550004,5.967570,-5.571248,7.698963,-6.259102,2.852450,-2.133417,2.792076,-1.465475,3.756701,6.392621,-8.756417,-5.853745,2.697678,3.212287,7.382074,-2.937049,2.741493,6.890595,-1.780520,4.283618,-2.355930,0.567748,7.645874,-0.668955,6.388105,-6.765563,-0.199334,9.353076,-2.082813,8.967904,7.534105,-8.343026,3.396082,2.840327,2.387611,2.774256,-6.564304,-3.613483,-8.701106,-8.041229,-6.538877,6.818534,0.157711,-2.319902,7.565978,-2.836917,3.830141,-3.883078,-1.033208,-2.026906,-1.274295,5.325376,-7.924444,-2.347989,-1.006545,-1.608226,7.594875,-2.065926,-6.199698,-8.559550,-6.322440,-6.585204,-5.416467,-6.593979,2.790657,-6.055753,-4.534884,-4.588695,6.485234,-3.966723,-3.447022,-0.535912,-4.013881,-6.903270,1.489880,4.170493,1.417873,4.501407,-6.679255,-3.738203,6.128930,6.254575,6.189565,-2.923960,1.664017,-7.365600,-0.941847,1.791463,3.759359,2.247251,4.581400,8.918504,8.251764,-9.376201,-1.852755,0.100668,6.468708,-6.311483,-6.048058,-1.688007,7.718703,7.230495,7.229485,-5.019060,3.261536,-4.420540,-0.783736,4.232704,-9.339339,0.056656,3.254248,-4.595982,-6.155936,2.358794,-2.063176,-3.188269,-6.670384,1.913876,-0.110724,7.530523,6.836494,-2.133372,5.085902,2.359045,7.304371,-4.511412,9.851244,-7.423063,1.829616,7.056047,8.706675,6.677203,8.291081,7.630864,3.456468,3.219734,-6.352805,-2.512347,-4.994712,-3.136613,9.123263,-1.112883,5.087984,-9.352081,-4.178216,-1.010466,4.407615,1.763001,-9.253631,-7.244650,0.642835,2.167854,-1.696969,5.045243,0.031360,-2.190851,3.200214,-4.730422,2.482168,7.588368,-4.269686,0.559131,-3.654813,-6.217702,-5.037299,-3.243789,6.587473,2.291547,4.906750,-1.035150,-6.508453,7.652172,7.286786,2.074499,-2.421697,-6.714126,-4.544964,-1.905803,-8.925312,-0.184824,-3.721679,6.663812,-3.179763,4.257111,1.086393,-7.045152,-6.104208,6.581849,2.443499,8.883134,-5.517882,-5.423504,6.270942,6.629334,-6.916406,-4.751677,-1.712946,-2.428857,5.286301,-8.656323,6.325145,-1.877597,4.182454,0.807892,-3.134981,-4.774923,-8.114499,-6.413794,-6.498114,8.122615,9.958381,1.189551,9.901622,-5.464837,9.314608,-1.926372,4.517611,-9.498278,-9.569161,-6.631398,-0.230698,6.421451,9.985573,1.722667,5.131100,-6.049436,-8.342221,-9.393211,6.948863,-6.630820,-5.760324,7.198425,-7.774589,-0.554199,3.887859,4.840307,7.184141,-4.426621,-9.644949,-7.559352,9.759440,-3.872078,-8.135374,9.701242,6.939108,-4.173495,-5.269667,-8.245301,-5.675224,-5.297006,3.414198,5.072462,-3.255713,6.785957,8.914951,6.605779,8.911424,1.553335,-3.790393,0.969554,-4.174108,5.954719,-3.331455,7.174235,-3.755351,-9.745551,-5.524763,7.200529,-5.022686,7.410369,-7.478499,-4.949290,7.214122,-1.265723,-5.267102,2.666481,1.588120,-1.685216,-5.636263,-7.722706,4.105032,-7.010297,5.098779,-5.770962,9.986606,1.329335,-6.544273,4.610835,6.872532,-5.669816,5.468405,5.250091,-3.432768,-5.805375,2.386880,-7.049601,-9.295052,-6.476449,-1.844901,2.738904,7.094826,0.053175,-0.780437,4.501574,-2.997709,4.548421,0.261975,2.728984,-3.566760,3.513864,-2.681166,-7.885301,-4.151790,-6.894343,-0.778399,-6.158889,3.017832,8.386013,-6.253703,3.962727,-9.297788,8.877622,1.673450,-4.839115,-9.231815,-7.289549,8.306006,1.627397,4.820155,-0.793244,0.181524,1.693244,-0.657188,-9.044990,4.354264,-8.419457,3.462321,-5.730512,-8.706212,-8.686190,-2.747617,2.449199,-7.109588,9.365397,7.026859,6.001029,2.498062,8.431000,2.736222,-1.170888,0.303560,1.095412,-3.799077,-4.149305,-0.670181,-6.795982,6.834290,-4.639012,-5.438571,5.898796,5.046898,6.726000,-0.400892,-0.779344,-0.612671,-0.097960,7.473916,-6.687488,9.241068,-9.133615,-2.674938,-0.366768,5.378301,7.186236,8.024167,9.156652,6.743048,5.352520,1.897919,4.888340,-7.974825,9.450738,9.773307,-0.552909,-2.915555,-9.094087,5.118810,-0.898007,9.218389,-9.359567,8.379718,3.126026,-0.690744,-8.909281,4.841105,-7.582571,8.875651,6.970379,4.373881,-8.381626,7.327542,-7.942331,0.620995,2.744295,-8.579753,0.882274,3.449007,-3.067457,2.247021,8.445663,7.179136,2.693913,7.075681,1.784623,-4.099483,2.768898,1.511755,-8.159216,-5.557476,1.652081,7.071391,-0.164125,-0.439297,7.289076,0.373455,-3.062971,-2.516919,-2.784880,-2.623427,-5.574480,6.282052,-0.421115,-6.049305,6.953857,-6.440765,2.134675,-1.356183,-7.551334,4.482412,-3.573141,-1.619306,6.305853,-7.166581,0.750498,9.325275,5.518429,1.278934,7.544746,-1.893334,-3.071026,-4.746662,7.008422,-3.316216,7.123989,5.797776,-2.644831,-1.955316,-6.795953,9.582957,4.578724,6.361795,6.521206,5.662996,-3.505473,-1.786665,-5.061529,0.388995,9.682472,-7.663463,3.346723,-7.840548,0.198435,0.811552,-6.205687,6.786733,4.413517,-2.933001,7.986784,-9.372603,-2.756873,5.395495,5.317147,-9.214020,-6.031219,4.599203,-3.273888,3.825803,-3.903984,7.747685,-1.565960,-1.379042,7.864027,-4.179909,-4.497417,6.217527,0.362585,-5.366279,9.809920,5.558644,9.112682,1.978260,9.447178,3.103021,4.522138,-8.601347,-8.207286,8.344497,0.724831,-1.914341,-2.486174,-4.517292,-3.846429,-8.289747,3.221654,0.228395,-1.335380,-6.469019,-2.768699,4.566296,-9.948475,7.844515,1.460330,4.299990,-3.885040,-5.258583,1.752707,6.502615,3.119536,4.016509,5.111179,0.661472,0.969171,8.544328,-9.623562,1.382955,-6.200006,2.550376,9.321514,0.308267,-4.638687,5.959779,-9.587861,-5.967651,-7.885698,2.900074,-4.816619,-5.868590,-8.568132,5.506690,-6.993691,-2.845611,4.269285,-4.377630,-9.772655,5.344408,-5.273010,-4.806270,2.640410,-0.240287,-2.955696,3.058805,2.446258,-7.308672,-2.903909,-3.950933,-7.348657,7.366634,-8.644814,-1.095189,0.837069,5.370522,-6.781265,5.329618,-7.419376,-6.022199,5.245182,-9.887254,1.834892,-0.771574,-9.912782,-8.898863,9.394722,2.394792,-4.554712,-9.346649,8.520034,1.941518,6.215933,3.623875,-4.984077,-5.147977,9.557672,-9.794412,0.181800,-9.912185,1.920454,-3.735765,5.192110,-7.476555,-2.484322,3.515186,9.900054,4.140912,6.461631,-0.697335,-0.125252,6.361331,1.101802,-9.187473,4.069608,0.353873,-5.766915,7.847824,6.724339,8.286971,8.499551,2.329118,1.401604,7.960549,8.350869,-4.331711,4.127056,2.520785,-4.293657,2.045251,9.273840,-5.528241,2.340247,0.273856,-5.407972,-1.135091,1.908592,-5.525377,-4.848347,-3.621543,8.122785,-5.206326,-1.021465,-6.671732,5.237094,-5.695571,-2.245627,-2.629585,6.881984,-8.078305,-0.940898,7.664252,-9.360010,-8.360537,6.698915,-8.381606,-0.320932,8.139741,-1.263256,3.638145,-6.266432,-9.840102,-4.828864,-2.321986,-4.514979,4.029867,6.032601,2.094012,-6.462045,-9.783582,-8.450641,4.131358,8.174795,1.117032,-0.427890,-2.439129,5.588091,9.418665,7.213540,4.664995,-1.861604,4.286705,1.215253,5.769874,-2.185082,9.847700,-1.829327,1.297995,-1.294632,7.409972,7.609415,1.212891,0.119667,7.292563,-1.069499,-0.383772,9.665382,-9.788077,-0.903678,8.099163,3.443927,1.281846,7.948178,-7.829862,-9.725563,-9.274651,9.763625,-4.038070,-6.136350,9.260263,-3.054948,0.279639,2.768843,-4.996782,0.443508,6.090156,-4.293356,-9.215227,0.180324,1.399885,-3.172762,-7.795191,0.835261,-1.515649,-8.949314,-2.468024,-9.938180,-3.581164,8.713984,7.284632,-9.696706,-3.783463,-0.766686,-3.094880,9.885966,7.465820,7.510792,0.821472,-0.220823,-7.000153,9.900904,9.180687,-9.276145,-4.822423,-7.062200,-5.289342,-7.126979,0.887012,1.461203,-6.941405,-3.757193,0.709341,7.898717,-5.086078,-2.990427,-2.334722,-7.314188,1.689562,-4.543386,-0.768863,-7.691192,0.250796,5.532047,4.810989,4.768166,9.285405,3.867363,4.467345,4.475551,-1.044049,8.395997,-8.746239,-0.652045,-1.399128,4.430844,7.668718,-0.150447,-5.009650,1.559789,-2.546392,7.076847,-3.627982,-7.023831,-9.203672,-5.846454,-9.982777,0.010788,6.887390,-6.460115,-6.697663,-8.948865,2.805276,1.901563,4.680787,0.487613,1.317459,7.725549,9.850052,4.720159,-3.888413,-5.179816,1.762815,2.025102,4.940102,7.972013,4.608754,4.914710,-7.881863,-5.417580,-4.423254,8.759006,-3.071919,8.400727,6.157565,7.505477,-9.444281,-3.711072,-8.098248,-7.310627,3.414941,6.841835,-5.109665,-9.154561,5.813222,-2.087079,-4.019431,1.545167,-9.722491,9.651709,-0.150654,5.473023,-3.081495,-5.459838,6.769718,7.914904,-1.973802,8.924322,6.531138,2.847245,-4.141375,-0.199642,-3.322891,-4.774811,7.113700,-9.031531,-3.158470,-7.512705,2.526328,2.035525,-6.782394,5.514509,-9.357881,7.523440,-4.350653,-2.528463,-5.374399,-6.510971,5.653964,9.085326,-1.887492,-2.263555,-7.096247,6.162549,7.311593,-0.050721,3.012010,0.092456,9.602894,-0.025340,8.844313,-2.108929,1.010141,-0.946666,9.675713,2.297188,7.245117,3.846396,0.883232,5.452814,6.207350,-1.527807,-4.096959,-9.727856,-3.843438,9.383779,-2.740816,7.284952,-4.674664,-9.364367,8.328471,0.836935,5.591010,-5.646693,-7.227028,4.051789,-3.063321,-2.225945,0.418589,-1.005167,5.776939,-2.366628,0.267775,-0.445581,5.831506,-5.721420,-0.776256,-0.084721,-6.675931,-1.467410,-5.169620,-0.160070,8.638686,0.154689,-7.896559,-1.325673,-6.892311,4.455072,-0.465426,6.373139,-4.211162,0.143822,-9.812856,-6.302560,-0.378654,2.276652,-4.654521,9.067970,-5.595330,8.828746,-7.899320,0.490439,-3.818892,4.448488,-9.062643,-0.939088,-0.746132,0.189160,0.399843,5.295549,2.946114,1.681106,-9.679617,8.734419,0.449736,5.759365,9.856767,-4.653295,3.989169,-9.877706,7.673444,-4.378359,-9.817607,-5.866841,4.999563,-4.469312,-8.928192,8.765513,-3.288682,3.712706,0.338252,-0.907371,2.318229,-4.221846,-2.707085,-5.538457,6.474444,4.144758,9.674694,-7.280849,7.758890,1.269608,-1.708048,-8.710008,9.438305,-3.051611,9.800595,4.887231,-0.321506,9.205993,7.472862,-0.130581,9.404138,-4.430642,7.557668,0.414103,8.523807,-4.815622,8.505763,1.282086,-3.844834,5.471991,-8.561761,9.465354,-0.968297,2.446103,-3.817246,7.975678,0.194218,-1.553337,-1.871154,0.303217,-9.931193,6.582144,-0.992137,0.210327,-3.032444,-7.709294,2.418680,0.218420,1.570863,3.627482,-4.659391,9.261353,7.125476,-3.094304,7.315694,1.252239,4.965944,-8.810333,0.061933,9.755470,-6.680074,-5.553089,5.690026,-7.075153,-2.764832,-9.693721,-3.424700,-8.806716,-9.016268,9.614594,-9.565142,0.081478,4.158061,-0.752034,1.954838,-3.795860,3.903003,-5.551590,4.770952,6.244230,-8.167352,-4.189938,3.506718,-8.375585,-7.304109,-8.760892,9.810459,-2.671082,0.049425,2.278588,-7.695985,-6.900508,6.113060,-7.774122,0.435800,-6.462463,-9.984382,-3.922208,-5.379536,1.106108,-8.557553,3.531468,0.174371,-0.100835,-9.514927,-2.657575,-5.960005,6.267968,2.546353,-2.473836,4.964568,-2.185171,1.486251,-9.829797,-7.874297,-7.012239,3.986416,-7.272705,-8.749024,1.141412,-2.958667,0.285803,-2.245170,-0.802521,3.707344,2.750952,-8.397662,-6.494538,-9.397478,5.424451,-8.353479,-0.318107,2.577646,-8.444462,9.501527,4.128722,7.429163,-9.413297,2.230802,4.053950,1.491285,7.659050,8.221203,-0.943269,-5.318943,-4.382364,6.693789,-7.309236,0.194501,-4.814726,-8.810968,-3.607045,3.362495,-6.824432,-7.582404,8.917383,-1.023134,9.698045,-8.373376,6.397498,9.177552,8.942224,-0.127391,1.213439,-1.095025,4.347237,2.543434,2.081745,-0.692072,5.279190,0.897343,7.491321,-9.847934,2.763229,-5.691710,7.243232,-6.382005,-4.648852,3.931429,-4.668443,-7.839888,-6.813947,-2.624020,-5.688249,3.532360,3.319677,-4.905839,-8.044601,9.974332,8.634650,7.873390,2.974317,8.841143,-2.731676,0.430961,-9.231783,-7.320891,-6.990586,-7.306184,-7.694148,-6.935058,8.260036,-9.331675,9.383573,9.099543,0.640353,-8.205737,6.347429,-1.134628,-7.852846,-9.691168,6.097450,6.091267,0.574937,-8.407388,-8.658396,0.766863,2.395917,2.204597,6.703843,5.226351,7.450666,4.665627,8.052386,0.594308,-2.311943,1.407080,-6.886297,3.018614,-2.267983,1.998018,-2.335025,-0.126008,-4.530494,5.531855,0.885713,-8.557524,-8.563368,9.154170,-9.759199,7.565653,-2.077497,-9.756554,9.349890,8.566070,-9.984492,-1.357338,7.468923,-9.340162,4.966589,-5.912602,7.513155,1.970539,-7.550526,0.331675,0.781962,1.067172,1.277578,5.520732,1.505063,2.581567,1.281364,8.751297,-6.741642,9.904499,7.700673,-9.459458,-7.766525,-8.674936,-2.519828,8.238455,-6.726395,-8.017544,3.610289,-1.100788,-8.037619,-5.095733,-4.456051,-5.710039,2.091674,-8.264875,1.888643,0.999244,-6.987795,7.820250,-9.668674,2.464429,0.610251,-3.836520,7.658623,-0.801322,-1.050693,4.478665,-5.071026,-5.231218,8.815077,-6.198642,8.788862,8.720638,1.048559,0.970673,3.868808,-8.627205,-2.764898,7.926714,8.335866,1.106847,-8.045517,-1.665344,-5.917653,7.522560,2.371322,4.659882,2.281285,9.526201,7.868688,-6.630120,7.142585,0.481131,-9.001550,1.816747,-5.273409,2.190834,4.868103,4.906930,-6.374286,-5.846477,-3.582877,3.943416,-4.107377,-5.430667,2.039660,-5.624103,8.222585,-0.943692,3.248514,-0.900639,-8.990669,-1.755494,2.655702,5.687966,-0.106258,-1.183512,7.650709,8.104522,-2.358806,4.932244,-4.994153,-9.863213,-9.826197,7.089950,-6.558175,8.874940,-4.927074,-6.388464,-8.365550,3.459651,5.477282,0.585791,9.517880,-6.934762,5.159292,0.860267,-3.359508,5.407856,-8.962149,-4.622264,-9.655240,8.164723,9.474785,3.284986,-1.100323,4.678595,-0.044289,-0.853721,2.080698,4.797754,7.777097,-9.718857,-5.481197,-7.988820,8.168239,4.157666,-7.536079,-9.441773,-3.108456,6.382830,-6.244695,3.952213,-9.372213,2.056596,-3.061462,-3.156125,5.123843,7.759047,-0.496907,7.366204,-2.413101,-1.021825,3.467154,6.297962,-6.474601,-2.151290,5.134849,7.632956,-5.669896,2.880710,1.386332,-1.130185,-4.418845,-8.433584,9.341016,-6.346487,-2.123088,-6.839751,9.793747,1.217179,1.939649,4.449825,4.777605,-4.326006,0.497265,5.003730,7.058520,9.968373,0.120287,-3.993766,3.132577,9.672261,5.768475,-0.910760,6.241415,-8.351601,3.432004,6.735931,-3.489148,-4.229954,6.421960,-1.994233,1.399039,-6.253456,7.188520,4.850286,-9.454217,-3.826129,3.585269,-5.916339,4.022538,2.906826,-5.403427,7.893279,-8.118121,-9.110528,0.710081,-6.814245,6.976699,-4.561447,2.850348,7.539533,-6.506213,-4.609619,-0.306798,-2.913952,6.568592,4.146877,-7.519507,0.940938,-1.645975,-1.422276,-7.971344,7.796952,3.686002,4.287129,6.538794,-8.039714,-4.990990,2.540470,-6.115554,-5.754379,0.265277,8.908007,9.680429,-8.058397,2.921130,2.204497,8.925733,3.283546,-4.621109,-0.975977,5.312589,2.366596,4.572791,7.388671,-5.372292,0.369317,4.489564,1.327276,4.500392,-3.067925,-1.170566,3.785485,-1.039000,4.952669,5.529530,1.082027,-1.794460,-5.517875,5.487445,4.869544,-1.982977,-2.206281,-2.861037,-4.393466,9.054918,-7.838596,-2.485973,-1.989190,-6.632919,-4.548174,5.132418,-3.446408,-5.785006,1.480980,-3.169419,-1.405776,9.631268,-1.125423,-9.822351,-0.906898,-4.735505,-4.903208,-1.193844,5.466803,-3.621934,-2.575896,7.147817,4.668321,7.047072,-6.860184,-4.959859,-1.750520,4.716467,5.917821,2.426765,3.366477,-5.240223,3.351148,-0.028054,9.852139,-5.744397,-4.813079,-2.393591,8.316786,-1.104034,-3.225408,-9.588440,0.524889,1.968821,-6.135797,-8.623275,-4.951780,0.010073,7.252026,1.126721,-2.240613,-5.626098,7.496887,-8.355601,-9.662371,-4.373095,5.511554,-3.439208,-4.406796,0.192248,-6.757472,4.392514,-4.710430,-2.846622,-6.900360,-8.024168,7.549722,-4.880004,-0.375947,-7.459565,4.918512,3.130212,2.301565,0.703035,3.875729,-9.151752,-6.180620,7.359586,-0.154380,-3.345663,0.320112,3.337652,0.505846,3.651817,2.195764,0.671311,1.499112,6.900576,-3.157247,-3.392401,-5.514291,6.535557,-3.550792,1.812829,0.902880,-8.669904,1.798141,0.962325,6.167468,-3.889959,-3.357566,2.044707,-4.041672,2.173516,-4.243564,-2.347454,-7.232405,7.397974,-2.648037,-8.325635,3.602448,-5.923876,-8.647168,5.132830,0.097979,-8.546405,5.992546,0.406726,4.899539,-3.039389,-8.611814,-2.826011,0.934960,-4.534238,-5.722497,8.679420,6.028490,-6.168781,2.124592,2.458090,7.109700,2.954630,4.986345,-0.952608,1.241121,-7.885057,-1.503631,-3.857437,3.984941,5.602166,5.106961,6.823884,3.686108,9.925331,4.126938,3.178086,-9.753169,-5.063191,8.248397,-2.304625,7.950854,-1.949338,2.411322,5.844319,8.510592,5.835350,0.534252,3.704187,-5.012614,-2.557046,7.440727,0.295638,-6.946745,-7.013975,-0.453146,-5.160561,2.589951,1.116741,9.199657,0.186151,-9.306093,-0.780284,2.714315,-9.616350,-2.351575,-1.962666,-9.457029,7.657334,9.667984,-4.587679,6.428133,0.691478,1.823727,5.608500,-1.759935,-3.970225,7.506463,-3.613636,-1.501579,2.712681,2.586125,3.667067,2.047192,-9.497432,-0.895940,-6.332147,2.956189,-5.769185,7.372548,-7.724065,9.180653,-9.186237,3.321833,9.415133,7.063818,-0.946081,-2.636900,-0.709303,-8.051375,-5.407203,9.729696,-3.397055,2.686224,7.576983,6.133987,-4.128444,-1.555178,6.938147,7.166153,-0.043527,1.039138,-6.559034,-3.244627,9.091086,8.995427,7.619520,6.804396,-7.245066,-9.681919,3.575821,9.309192,-0.344751,-6.814642,9.643476,6.933940,-8.399045,-2.578288,-1.984711,7.222015,3.914481,-2.143615,2.489755,8.570832,-6.658083,9.884117,4.127398,6.256031,5.453928,0.204914,6.088034,-1.595356,-2.224413,-1.569333,7.641553,-8.052268,2.705683,4.065338,-8.394180,-8.833499,-7.214406,-7.168490,-5.182679,-7.669553,0.717795,-4.981025,-5.545619,-0.357002,0.800064,0.555015,-8.596718,5.719554,-1.321839,-2.757391,1.228294,3.557052,8.034777,2.425941,5.103333,8.822079,-6.280041,-3.414830,-1.843573,7.153081,8.856370,-4.965565,-5.834411,8.268959,-6.898556,-5.654048,-5.266835,4.385706,1.851525,8.842339,-9.413811,-1.921730,-6.302666,3.671659,7.288705,-7.150979,-4.692050,8.443113,7.155887,1.578710,-3.363918,1.499642,-5.923615,-2.449328,-8.859572,-7.313856,-4.648588,1.659544,0.757987,7.247812,0.599275,-6.563693,-2.088674,-4.037238,-3.002733,9.112224,3.449722,-4.274099,-5.043423,-4.732255,-6.856726,6.921786,0.625289,-9.641289,-3.742544,0.636956,8.582812,8.835939,1.649954,0.778307,0.276968,1.252184], dtype = "float64")#candidate|7571|(2080,)|const|float64
call_7570 = relay.TupleGetItem(func_7331_call(relay.reshape(const_7571.astype('float64'), [2080,])), 1)
call_7572 = relay.TupleGetItem(func_7334_call(relay.reshape(const_7571.astype('float64'), [2080,])), 1)
uop_7576 = relay.rsqrt(uop_7557.astype('float32')) # shape=(9, 4, 16)
uop_7578 = relay.rsqrt(uop_7559.astype('float32')) # shape=(9, 4, 16)
func_6542_call = mod.get_global_var('func_6542')
func_6546_call = mutated_mod.get_global_var('func_6546')
call_7588 = relay.TupleGetItem(func_6542_call(relay.reshape(call_7543.astype('float64'), [13, 5, 9]), relay.reshape(call_7567.astype('uint8'), [13, 5, 9]), ), 0)
call_7589 = relay.TupleGetItem(func_6546_call(relay.reshape(call_7543.astype('float64'), [13, 5, 9]), relay.reshape(call_7567.astype('uint8'), [13, 5, 9]), ), 0)
bop_7590 = relay.bitwise_or(uop_7576.astype('int8'), relay.reshape(uop_7557.astype('int8'), relay.shape_of(uop_7576))) # shape=(9, 4, 16)
bop_7593 = relay.bitwise_or(uop_7578.astype('int8'), relay.reshape(uop_7559.astype('int8'), relay.shape_of(uop_7578))) # shape=(9, 4, 16)
output = relay.Tuple([call_7543,var_7548,call_7567,call_7570,const_7571,call_7588,bop_7590,])
output2 = relay.Tuple([call_7544,var_7548,call_7568,call_7572,const_7571,call_7589,bop_7593,])
func_7598 = relay.Function([var_7548,], output)
mod['func_7598'] = func_7598
mod = relay.transform.InferType()(mod)
var_7599 = relay.var("var_7599", dtype = "bool", shape = (288, 2))#candidate|7599|(288, 2)|var|bool
output = func_7598(var_7599)
func_7600 = relay.Function([var_7599], output)
mutated_mod['func_7600'] = func_7600
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1940_call = mod.get_global_var('func_1940')
func_1941_call = mutated_mod.get_global_var('func_1941')
call_7626 = func_1940_call()
call_7627 = func_1940_call()
output = call_7626
output2 = call_7627
func_7641 = relay.Function([], output)
mod['func_7641'] = func_7641
mod = relay.transform.InferType()(mod)
output = func_7641()
func_7642 = relay.Function([], output)
mutated_mod['func_7642'] = func_7642
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6389_call = mod.get_global_var('func_6389')
func_6391_call = mutated_mod.get_global_var('func_6391')
call_7680 = relay.TupleGetItem(func_6389_call(), 1)
call_7681 = relay.TupleGetItem(func_6391_call(), 1)
output = relay.Tuple([call_7680,])
output2 = relay.Tuple([call_7681,])
func_7690 = relay.Function([], output)
mod['func_7690'] = func_7690
mod = relay.transform.InferType()(mod)
mutated_mod['func_7690'] = func_7690
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7690_call = mutated_mod.get_global_var('func_7690')
call_7691 = func_7690_call()
output = call_7691
func_7692 = relay.Function([], output)
mutated_mod['func_7692'] = func_7692
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7726 = relay.var("var_7726", dtype = "int64", shape = ())#candidate|7726|()|var|int64
var_7727 = relay.var("var_7727", dtype = "int64", shape = (1, 1, 8))#candidate|7727|(1, 1, 8)|var|int64
bop_7728 = relay.logical_xor(var_7726.astype('int64'), var_7727.astype('int64')) # shape=(1, 1, 8)
bop_7735 = relay.logical_and(bop_7728.astype('bool'), relay.reshape(var_7727.astype('bool'), relay.shape_of(bop_7728))) # shape=(1, 1, 8)
func_2935_call = mod.get_global_var('func_2935')
func_2938_call = mutated_mod.get_global_var('func_2938')
var_7742 = relay.var("var_7742", dtype = "float64", shape = (585,))#candidate|7742|(585,)|var|float64
call_7741 = relay.TupleGetItem(func_2935_call(relay.reshape(var_7742.astype('float64'), [13, 5, 9])), 3)
call_7743 = relay.TupleGetItem(func_2938_call(relay.reshape(var_7742.astype('float64'), [13, 5, 9])), 3)
output = relay.Tuple([bop_7735,call_7741,var_7742,])
output2 = relay.Tuple([bop_7735,call_7743,var_7742,])
func_7746 = relay.Function([var_7726,var_7727,var_7742,], output)
mod['func_7746'] = func_7746
mod = relay.transform.InferType()(mod)
var_7747 = relay.var("var_7747", dtype = "int64", shape = ())#candidate|7747|()|var|int64
var_7748 = relay.var("var_7748", dtype = "int64", shape = (1, 1, 8))#candidate|7748|(1, 1, 8)|var|int64
var_7749 = relay.var("var_7749", dtype = "float64", shape = (585,))#candidate|7749|(585,)|var|float64
output = func_7746(var_7747,var_7748,var_7749,)
func_7750 = relay.Function([var_7747,var_7748,var_7749,], output)
mutated_mod['func_7750'] = func_7750
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3878_call = mod.get_global_var('func_3878')
func_3879_call = mutated_mod.get_global_var('func_3879')
call_7771 = relay.TupleGetItem(func_3878_call(), 0)
call_7772 = relay.TupleGetItem(func_3879_call(), 0)
func_7192_call = mod.get_global_var('func_7192')
func_7193_call = mutated_mod.get_global_var('func_7193')
call_7775 = func_7192_call()
call_7776 = func_7192_call()
output = relay.Tuple([call_7771,call_7775,])
output2 = relay.Tuple([call_7772,call_7776,])
func_7779 = relay.Function([], output)
mod['func_7779'] = func_7779
mod = relay.transform.InferType()(mod)
output = func_7779()
func_7780 = relay.Function([], output)
mutated_mod['func_7780'] = func_7780
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4530_call = mod.get_global_var('func_4530')
func_4532_call = mutated_mod.get_global_var('func_4532')
call_7896 = func_4530_call()
call_7897 = func_4530_call()
func_3262_call = mod.get_global_var('func_3262')
func_3263_call = mutated_mod.get_global_var('func_3263')
call_7906 = func_3262_call()
call_7907 = func_3262_call()
func_6857_call = mod.get_global_var('func_6857')
func_6860_call = mutated_mod.get_global_var('func_6860')
call_7914 = func_6857_call(relay.reshape(call_7896.astype('float64'), [13, 5, 9]))
call_7915 = func_6857_call(relay.reshape(call_7896.astype('float64'), [13, 5, 9]))
output = relay.Tuple([call_7896,call_7906,call_7914,])
output2 = relay.Tuple([call_7897,call_7907,call_7915,])
func_7916 = relay.Function([], output)
mod['func_7916'] = func_7916
mod = relay.transform.InferType()(mod)
mutated_mod['func_7916'] = func_7916
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7916_call = mutated_mod.get_global_var('func_7916')
call_7917 = func_7916_call()
output = call_7917
func_7918 = relay.Function([], output)
mutated_mod['func_7918'] = func_7918
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1393_call = mod.get_global_var('func_1393')
func_1394_call = mutated_mod.get_global_var('func_1394')
call_7934 = relay.TupleGetItem(func_1393_call(), 0)
call_7935 = relay.TupleGetItem(func_1394_call(), 0)
func_4690_call = mod.get_global_var('func_4690')
func_4692_call = mutated_mod.get_global_var('func_4692')
call_7945 = func_4690_call()
call_7946 = func_4690_call()
func_4278_call = mod.get_global_var('func_4278')
func_4280_call = mutated_mod.get_global_var('func_4280')
const_7951 = relay.const([-0.850218,3.631750,-6.696446,-6.386948,5.323427,9.409662,1.539953,-4.786815,2.953095,-3.549981,-0.061819,9.119195,3.738224,5.746519,-9.855272,-0.068843,-9.625268,-4.633843,2.226519,-2.995169,7.065125,6.358286,-3.880491,7.036424,-5.021478,1.465913,9.133893,5.881337,-5.532166,-7.195135,0.708201,3.459063,-3.807763,-4.897844,1.861664,2.226547,-6.692582,3.482571,-4.362693,-3.922068,-0.127218,-4.263085,-4.583400,-4.544056,-8.613369,-2.484916,6.988417,0.437373,2.187111,4.030635,7.020498,4.042506,9.520792,-8.135004,-4.290823,-5.149615,2.275399,-3.309931,6.714769,-7.857827,5.949403,8.258771,-6.586404,1.723931,-0.369100,-0.078115,2.883980,-1.889260,-7.061693,-1.194411,6.921104,2.534985,6.482739,7.123079,4.946927,5.221759,-4.842320,7.177209,0.614324,-3.295289,-3.718520,9.595542,6.380691,-3.049314,0.331265,-3.578565,-8.290079,7.321273,5.748732,-0.950971,-2.381036,-7.534876,-4.642469,5.775069,-9.631112,5.576452,0.358495,-8.320104,-5.778812,-9.563998,2.921345,0.711241,9.136877,-5.005020,2.913500,7.302423,-8.273329,-6.922993,0.809838,-7.863496,6.193878,-6.555864,7.096769,3.464046,-7.142976,6.371884,-6.589193,5.970861,1.082719,9.001306,-8.608189,-3.782249,-9.081205,5.780222,-6.194104,7.054219,7.944952,-5.635102,-1.661043,4.598937,-8.735318,-6.995998,5.381843,-5.179125,4.242560,6.639407,-7.765351,-7.559710,-8.696667,-2.701641,-3.500523,-3.471571,-2.096565,-0.285194,2.268934,5.738312,-0.741843,-4.661436,0.151566,-8.376833,-8.308961,-8.823504,8.559994,0.398534,-0.024361,-8.144843,4.256176,-4.171274,-1.626329,-6.049046,-5.485424,6.292958,-3.546954,-4.556823,-0.818754,-9.929988,-6.736438,2.964632,-6.388813,8.698360,-8.794650,3.096822,0.562397,3.474154,-3.591183,9.634758,5.731187,0.896356,-1.532249,7.624723,-7.356968,-2.247296,-3.733847,-9.054219,-2.666749,5.052782,3.729709,0.373710,5.119106,-6.248899,-0.435216,-3.562522,-7.458568,2.326492,-3.918690,0.276344,7.376089,5.512391,2.536339,-4.536815], dtype = "float64")#candidate|7951|(200,)|const|float64
call_7950 = relay.TupleGetItem(func_4278_call(relay.reshape(const_7951.astype('float64'), [200,])), 0)
call_7952 = relay.TupleGetItem(func_4280_call(relay.reshape(const_7951.astype('float64'), [200,])), 0)
func_1940_call = mod.get_global_var('func_1940')
func_1941_call = mutated_mod.get_global_var('func_1941')
call_7993 = func_1940_call()
call_7994 = func_1940_call()
func_4945_call = mod.get_global_var('func_4945')
func_4948_call = mutated_mod.get_global_var('func_4948')
var_7999 = relay.var("var_7999", dtype = "uint16", shape = (1, 126))#candidate|7999|(1, 126)|var|uint16
call_7998 = relay.TupleGetItem(func_4945_call(relay.reshape(var_7999.astype('uint16'), [126,])), 2)
call_8000 = relay.TupleGetItem(func_4948_call(relay.reshape(var_7999.astype('uint16'), [126,])), 2)
func_6857_call = mod.get_global_var('func_6857')
func_6860_call = mutated_mod.get_global_var('func_6860')
call_8001 = func_6857_call(relay.reshape(call_7934.astype('float64'), [13, 5, 9]))
call_8002 = func_6857_call(relay.reshape(call_7934.astype('float64'), [13, 5, 9]))
output = relay.Tuple([call_7934,call_7945,call_7950,const_7951,call_7993,call_7998,var_7999,call_8001,])
output2 = relay.Tuple([call_7935,call_7946,call_7952,const_7951,call_7994,call_8000,var_7999,call_8002,])
func_8003 = relay.Function([var_7999,], output)
mod['func_8003'] = func_8003
mod = relay.transform.InferType()(mod)
var_8004 = relay.var("var_8004", dtype = "uint16", shape = (1, 126))#candidate|8004|(1, 126)|var|uint16
output = func_8003(var_8004)
func_8005 = relay.Function([var_8004], output)
mutated_mod['func_8005'] = func_8005
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1927_call = mod.get_global_var('func_1927')
func_1928_call = mutated_mod.get_global_var('func_1928')
call_8012 = func_1927_call()
call_8013 = func_1927_call()
func_1696_call = mod.get_global_var('func_1696')
func_1699_call = mutated_mod.get_global_var('func_1699')
call_8032 = relay.TupleGetItem(func_1696_call(relay.reshape(call_8012.astype('float32'), [13, 5, 9])), 0)
call_8033 = relay.TupleGetItem(func_1699_call(relay.reshape(call_8012.astype('float32'), [13, 5, 9])), 0)
func_1758_call = mod.get_global_var('func_1758')
func_1759_call = mutated_mod.get_global_var('func_1759')
call_8041 = func_1758_call()
call_8042 = func_1758_call()
output = relay.Tuple([call_8012,call_8032,call_8041,])
output2 = relay.Tuple([call_8013,call_8033,call_8042,])
func_8059 = relay.Function([], output)
mod['func_8059'] = func_8059
mod = relay.transform.InferType()(mod)
output = func_8059()
func_8060 = relay.Function([], output)
mutated_mod['func_8060'] = func_8060
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1302_call = mod.get_global_var('func_1302')
func_1303_call = mutated_mod.get_global_var('func_1303')
call_8129 = func_1302_call()
call_8130 = func_1302_call()
output = call_8129
output2 = call_8130
func_8136 = relay.Function([], output)
mod['func_8136'] = func_8136
mod = relay.transform.InferType()(mod)
output = func_8136()
func_8137 = relay.Function([], output)
mutated_mod['func_8137'] = func_8137
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8181 = relay.var("var_8181", dtype = "uint64", shape = (13, 9, 7))#candidate|8181|(13, 9, 7)|var|uint64
const_8182 = relay.const([[[-9,-6,5,10,-9,7,2],[1,-2,-2,-1,-10,3,6],[7,7,2,-8,3,1,3],[-7,1,-1,-8,2,5,4],[3,8,-5,7,-10,-4,-4],[-7,5,2,-2,1,-7,1],[-6,-9,-4,8,-2,7,-1],[-7,8,-2,7,-8,-6,-3],[1,-6,-9,-5,-2,2,-9]],[[7,2,7,-7,-4,2,5],[1,2,2,-9,2,5,7],[7,-10,8,-6,3,-3,-10],[-9,2,3,-3,1,-7,8],[-5,3,2,6,-5,-6,-8],[5,1,-2,-3,-6,-9,10],[10,-2,-4,-6,-8,8,-5],[-2,-1,-10,3,7,7,4],[-2,4,2,-6,-10,-3,-5]],[[4,5,-4,4,-1,5,3],[-1,10,1,7,1,-10,-8],[-1,-3,-4,2,-5,3,5],[1,-10,5,10,-5,9,-10],[8,1,-2,6,-3,5,7],[3,6,10,-10,7,2,7],[-7,-2,7,-6,-10,-5,3],[2,-8,1,-8,-1,9,8],[-9,5,-2,-4,-2,5,3]],[[6,2,7,10,-3,1,9],[-1,1,2,7,-3,-2,-1],[9,-9,-1,3,-10,-6,-3],[6,-6,9,-6,-3,4,3],[-3,4,-10,6,-5,-1,-2],[-9,-5,7,1,-9,6,1],[-10,-9,-1,-4,8,-4,1],[-2,-4,7,6,-3,1,-6],[-5,-8,-3,7,-10,7,-3]],[[4,8,-6,-7,-6,-9,1],[-10,-7,-6,-10,-2,3,10],[-1,-2,-6,1,7,-6,-2],[-9,-3,10,3,-4,4,-2],[7,6,-4,3,1,3,-1],[-8,-4,-5,-7,8,2,-7],[-8,-3,8,5,10,-3,3],[10,6,8,-6,-8,10,6],[-8,8,9,-2,-3,-10,-6]],[[-5,-8,-6,2,6,-9,-2],[8,2,-9,1,2,-7,-2],[-7,10,9,4,4,-9,5],[-5,-8,-4,-1,1,-3,7],[7,8,10,-7,-8,4,8],[-2,-3,1,-2,-4,-10,-6],[7,4,5,-9,10,3,6],[9,1,8,-10,7,-3,-6],[-5,7,-10,-9,5,-9,5]],[[-4,-9,6,6,-8,-2,2],[-6,-8,3,-7,6,-9,4],[-5,-1,-10,4,4,2,10],[-5,-7,1,5,9,-8,-6],[6,-4,-10,2,7,8,7],[3,3,-8,-2,6,-4,7],[-3,-8,4,-2,8,6,9],[9,3,-1,-2,9,-9,-9],[-3,4,3,5,-5,2,10]],[[-1,4,-4,5,-5,8,1],[10,-10,-10,7,6,1,-8],[5,2,8,9,3,1,1],[2,5,-3,5,9,7,5],[-7,2,2,9,8,-3,-3],[10,2,-7,-4,-3,-6,-2],[-8,-10,1,-8,-5,-2,-6],[-5,9,-3,7,-9,-10,9],[-7,-8,7,1,-9,-2,7]],[[-7,-9,1,6,-1,4,4],[-4,-10,4,-7,6,-1,-8],[-7,-7,1,-7,-7,8,7],[-10,8,6,7,5,-4,-6],[6,-8,-1,9,4,-6,-2],[9,-6,2,4,-1,-7,9],[-7,-8,10,-6,-2,5,-3],[-7,3,4,-6,5,-4,5],[1,5,-10,1,-9,-1,3]],[[9,6,3,-3,-1,3,2],[-2,-9,2,3,8,-2,-10],[-10,-10,1,4,-7,10,9],[-6,1,8,1,7,-2,5],[-10,8,1,8,5,-7,2],[-2,3,1,-4,-5,9,-6],[-4,8,9,5,-5,4,-8],[4,-8,-10,2,4,-10,-10],[10,-1,-10,-2,6,-9,-2]],[[-3,-3,10,-3,2,-10,3],[7,9,1,6,1,-8,-5],[10,-9,-10,1,-4,10,10],[-6,10,-6,3,-2,-9,-6],[2,6,-1,-6,-7,-10,-1],[-1,-10,6,10,-2,-1,1],[7,-7,-9,10,7,-2,5],[7,2,-9,-7,-6,-6,2],[-3,7,10,-9,-4,2,7]],[[6,-6,7,3,2,-10,-6],[5,4,-1,-7,5,-4,7],[10,8,7,1,1,10,3],[-10,-8,7,6,-5,10,1],[8,-8,3,6,-9,3,-2],[-3,-3,-6,-1,-3,4,10],[-7,-8,8,-5,3,8,-10],[-3,-4,-9,-3,-7,1,-1],[-7,7,-3,-9,2,-9,-5]],[[8,-10,8,-9,-10,-2,-7],[7,8,-1,8,-1,-5,10],[7,-3,-9,-7,-4,3,-9],[10,-10,5,9,-4,-2,-3],[-7,10,-8,-2,-3,-5,-5],[2,-5,-9,-7,4,2,4],[-2,-10,-2,6,3,-7,5],[5,8,4,-8,-10,-9,3],[-2,-7,6,5,8,-5,7]]], dtype = "uint64")#candidate|8182|(13, 9, 7)|const|uint64
bop_8183 = relay.greater(var_8181.astype('bool'), relay.reshape(const_8182.astype('bool'), relay.shape_of(var_8181))) # shape=(13, 9, 7)
func_1696_call = mod.get_global_var('func_1696')
func_1699_call = mutated_mod.get_global_var('func_1699')
const_8191 = relay.const([[2.278362],[-5.495357],[6.363270],[-2.123026],[-9.066863],[-5.773437],[9.722643],[2.180166],[1.278508],[9.559282],[-2.728012],[0.688675],[-6.933417],[-0.530003],[-3.849142],[-9.837359],[-0.060773],[-4.980266],[4.769821],[8.535159],[-8.857032],[0.871785],[-2.274669],[5.134576],[5.926772],[-9.703800],[8.421366],[8.043852],[-7.982754],[7.528764],[5.887377],[7.239472],[-4.630293],[6.506713],[-5.583510],[4.569651],[-0.217859],[-2.315089],[-7.666166],[-8.669449],[-6.460311],[4.375107],[-3.785042],[5.275824],[2.688853],[-6.482435],[-3.692345],[-2.725378],[2.250108],[-0.911320],[-7.803840],[6.374584],[1.198120],[-8.538100],[0.428368],[6.679494],[2.042432],[6.005367],[8.705164],[8.712797],[1.743825],[8.963692],[8.532056],[-5.741273],[4.418971],[-7.220762],[8.701248],[6.509955],[1.980786],[-3.084561],[-1.450990],[-3.134988],[-6.114954],[-9.423908],[6.861175],[-0.123319],[5.174479],[-6.994318],[2.814923],[9.597843],[-9.232745],[1.457832],[1.226918],[-6.251352],[-8.393767],[5.718625],[-4.338150],[-0.850970],[-9.881288],[-3.030366],[-3.019682],[-8.218903],[-2.522604],[-0.183072],[-5.388031],[-1.450978],[8.732201],[-6.711637],[-5.225404],[8.652880],[3.645524],[-0.506186],[0.120459],[-8.619965],[1.651145],[1.988455],[-1.338887],[0.109256],[-0.514697],[-4.369479],[1.996249],[7.035706],[-1.117646],[-7.014050],[-1.386673],[4.922294],[-3.745642],[8.017477],[2.221562],[5.017632],[-7.890306],[-0.048849],[7.850300],[3.858121],[-0.930412],[-5.286914],[1.862742],[-4.318325],[3.331961],[-6.920377],[1.628245],[5.380436],[9.489338],[4.372968],[-5.032496],[2.683510],[6.893267],[8.565461],[6.555725],[-5.426955],[2.176053],[-2.073500],[1.916596],[-8.701397],[5.502313],[-0.897970],[3.084358],[-2.708680],[7.401794],[8.441697],[7.009992],[-1.719091],[-9.869162],[4.274907],[5.918193],[6.757191],[-1.159796],[2.110819],[3.337499],[-4.407774],[-0.768171],[7.348625],[-7.733392],[0.087498],[4.628358],[2.297656],[0.193112],[1.519459],[-1.023057],[-6.598694],[-3.967826],[-0.343168],[7.538322],[-0.073373],[4.255053],[3.818399],[-4.360266],[1.912678],[-2.063124],[-0.961624],[0.995836],[-1.893429],[4.452159],[6.451973],[-5.227920],[6.157435],[0.013712],[1.800778],[5.271752],[9.635769],[-5.912906],[7.194318],[6.090082],[2.830225],[8.246260],[6.259857],[-4.681496],[8.566580],[3.637748],[7.227527],[-5.920316],[2.966086],[-5.499473],[-6.469315],[-5.370732],[-1.365780],[-2.943852],[9.841304],[8.164313],[-4.349438],[-0.142921],[6.578888],[7.776908],[3.437539],[6.048159],[4.730321],[3.372831],[-0.953128],[0.476827],[-9.576801],[-2.877765],[0.244472],[-5.592004],[3.873953],[5.180903],[-4.617291],[1.371413],[-0.280127],[-4.310567],[-5.309449],[-8.742707],[-2.883642],[-2.745504],[7.660588],[7.641308],[3.418891],[7.276040],[2.815100],[-1.088308],[1.287744],[-0.438121],[8.115772],[1.249939],[-1.666529],[9.639177],[-0.777357],[-7.336060],[-4.296097],[8.452226],[2.108309],[5.945909],[-6.238068],[3.812458],[-3.503062],[-4.255462],[2.604189],[5.161231],[5.157799],[2.834253],[-3.025412],[-0.270482],[-3.800068],[2.579708],[3.310225],[0.319906],[-2.941659],[7.730125],[5.029520],[-7.659786],[-7.410305],[0.787128],[2.814000],[8.120602],[3.617064],[-8.960622],[6.050763],[-1.497582],[-5.562517],[-6.912129],[-3.051836],[-9.271003],[-2.138730],[-1.862774],[-2.656422],[7.211630],[7.369807],[-3.644792],[1.458298],[9.614309],[-6.441467],[3.544288],[-2.618414],[-2.357206],[5.306675],[-4.106236],[-6.180844],[-7.425448],[9.735012],[-4.233261],[8.360487],[-7.988342],[-3.630113],[7.161848],[-0.116901],[-2.968302],[3.036167],[6.682062],[-6.108343],[-4.468714],[-3.294828],[9.826984],[3.361761],[-1.892124],[-1.345489],[-1.443049],[-6.737037],[5.469480],[9.451433],[5.382076],[2.090994],[0.865646],[4.497550],[7.086825],[-5.661522],[5.749639],[-4.186752],[8.868353],[3.839272],[-5.562964],[-6.623155],[5.817375],[-2.812194],[1.190546],[-2.775035],[9.707044],[-4.250616],[-0.732447],[4.713759],[1.432877],[1.178708],[2.003678],[-7.337090],[4.284795],[-9.836817],[8.874406],[-6.435648],[5.603046],[3.820842],[-9.835543],[8.902720],[-6.449018],[-6.405463],[3.447109],[-0.635608],[7.531362],[-1.641355],[8.686246],[6.495437],[-7.800286],[8.729148],[-8.550703],[-8.783747],[-7.919398],[-2.490871],[3.673172],[-4.793451],[-1.090547],[-9.750258],[1.441469],[-8.228313],[-2.082239],[2.172029],[5.772811],[-3.200091],[-0.781729],[-8.347722],[1.234681],[-5.778240],[-8.493117],[7.566767],[2.400036],[8.611248],[-5.900475],[4.574861],[-1.094468],[8.685394],[-7.956023],[3.599644],[9.253067],[2.554453],[9.458041],[0.982031],[1.927570],[-7.522793],[-1.024367],[8.528007],[1.232599],[5.611671],[8.802208],[0.091428],[2.828418],[-3.689488],[6.303797],[6.761611],[-5.123926],[-9.483241],[-0.688832],[-9.759486],[-7.598032],[-9.578107],[-3.682666],[-3.697798],[-0.851869],[-7.327040],[-6.029971],[-5.420335],[-1.240587],[-7.315120],[-7.213201],[-4.580447],[-1.427538],[-0.810299],[-2.183653],[-0.474929],[6.660313],[-1.773072],[8.725172],[9.749799],[-7.726410],[9.498466],[-1.866944],[-7.131816],[-8.753334],[-6.577257],[7.357473],[1.422096],[-3.107844],[-2.274782],[6.313468],[3.014666],[8.987421],[-2.968261],[-1.976942],[2.445381],[9.159985],[6.431233],[-0.830019],[-2.238007],[-2.938028],[6.530990],[-1.515100],[-7.679459],[-8.601222],[7.554019],[3.376461],[-1.295233],[-5.427019],[7.183302],[-4.517132],[-6.171125],[2.603208],[9.708909],[6.920191],[5.400076],[5.454900],[4.622928],[9.712112],[-0.291905],[6.687495],[3.102595],[-9.792644],[5.852376],[6.704571],[3.200546],[8.695172],[8.943069],[8.021213],[-9.726301],[3.731255],[6.965636],[-8.971572],[-2.052262],[-8.090685],[3.952851],[-0.825255],[-7.038774],[-1.999032],[-0.358852],[9.097232],[-9.690844],[1.430958],[9.192366],[-2.645084],[7.821725],[2.593917],[-4.186113],[-9.744048],[-2.796683],[1.780181],[-0.053290],[-7.584587],[-8.886439],[-9.302252],[-3.400466],[-6.527188],[4.603580],[8.046551],[4.343362],[-9.777471],[3.783753],[3.139063],[-7.726366],[-9.959727],[-4.005364],[-8.049905],[0.168398],[9.065491],[-5.665076],[-2.737861],[7.472059],[3.434279],[-8.952996],[-3.647298],[-6.796580],[4.848434],[-8.232025],[-6.482500],[-8.833566],[8.022901],[-8.150336],[5.693498],[4.892696],[-2.147616],[-3.785157],[-2.210615],[0.496949],[-2.630816],[-8.420834],[3.494169],[-6.966100],[-1.110766],[1.958628],[9.314131],[1.336040],[-9.640751],[-7.993598],[-7.553862],[8.923759],[0.783765],[0.483853],[0.386424],[7.201968],[8.786664],[-5.023901],[1.023260],[3.523701],[-3.143262],[-6.668371],[-4.765259],[-6.988126],[8.682938],[-5.330754],[-7.276431],[-8.205065],[0.626353],[-5.617499],[2.426534],[2.691371],[1.981365],[5.392344],[-4.143675],[8.739592],[-6.536969],[-6.461291],[7.029583],[5.304809],[0.178674],[-3.833230],[8.534650],[-6.397355],[4.064206],[-0.880878],[-1.335666],[8.604203],[8.366933]], dtype = "float32")#candidate|8191|(585, 1)|const|float32
call_8190 = relay.TupleGetItem(func_1696_call(relay.reshape(const_8191.astype('float32'), [13, 5, 9])), 0)
call_8192 = relay.TupleGetItem(func_1699_call(relay.reshape(const_8191.astype('float32'), [13, 5, 9])), 0)
func_1230_call = mod.get_global_var('func_1230')
func_1236_call = mutated_mod.get_global_var('func_1236')
const_8194 = relay.const([[-1.016705,9.693059,9.326266,7.175122,5.171678,-1.650314,2.617727,4.322029,7.926105,-7.715693],[-5.579632,6.558528,0.555342,8.328970,6.743547,9.390576,-1.149206,1.652596,-6.843628,0.626409],[4.317874,6.546554,-6.889404,3.408550,4.693309,-9.086549,5.735855,9.974018,-2.492660,-2.779619],[-1.597570,9.347082,-3.265192,-9.679345,-4.149507,-9.023018,-9.181999,-7.134559,1.953431,-8.884679],[0.856977,-0.536016,-9.870998,0.299540,7.279443,-0.830632,-1.195095,-7.755725,-7.975994,2.724720],[-7.501587,-7.815230,0.684954,9.527889,-9.730972,0.138797,-7.696507,-1.070422,9.547382,-0.516942],[2.646166,-0.979167,-9.925460,-2.041449,-7.559556,0.596509,-6.550002,5.545069,3.887199,-3.528918],[-7.748960,0.344859,6.769679,0.362252,-1.722831,7.456009,-2.064010,4.708545,-0.722045,-7.298064],[0.895500,3.930605,8.548644,5.815929,-0.360835,9.522744,0.169329,6.138311,-9.689760,-1.842722],[-3.803743,2.176253,4.043063,-7.507954,-2.006653,-2.518276,-1.719790,5.282613,-0.599959,-4.192437],[-4.463311,7.602712,0.425447,6.763646,2.798359,-1.697386,5.720282,9.171002,-6.611538,1.419402],[-6.900702,-9.091456,4.150174,-3.392900,-1.969340,-4.233586,-4.561183,-6.148580,8.895907,-9.646563],[2.947312,-2.541313,-4.135411,-0.421572,1.095431,4.759466,6.300392,9.242141,-3.650076,0.234947],[-3.209075,6.710883,9.121860,-6.681227,5.703155,-5.339298,8.863608,-1.076479,-0.141245,-1.162429],[-7.495597,3.880527,8.813622,-0.979672,-4.888836,-3.778170,-8.181823,-4.422031,-4.331712,-1.616570],[2.169733,-9.447807,9.938225,-3.718944,9.847636,-5.259297,-7.484766,-4.254581,-8.953125,8.638963],[-3.503212,7.309976,-1.259950,-8.048599,4.678547,-0.921368,3.013959,2.563249,5.410583,-4.515527],[2.134639,-1.144061,-0.129283,4.927189,-5.250305,-8.765409,1.443206,9.354618,4.072936,-5.767462],[-3.272567,1.647344,8.086537,-4.644640,-5.336796,-2.351723,5.139528,5.951260,8.298361,-8.420075],[-0.501432,-5.944607,4.459890,9.842352,4.902251,3.472977,-1.840743,-6.171962,4.574318,1.649084],[4.768162,4.690915,-5.197653,6.480332,-1.834174,4.761194,-1.896085,-4.875482,4.655823,-7.117505],[2.571617,-1.817544,-1.823117,6.512943,-6.833376,6.351173,-0.210457,-0.627969,4.480617,-4.980250],[-9.741062,-9.017174,8.360558,-2.558664,-2.138234,-6.749435,-3.213973,-1.645494,1.411723,-5.951195],[-6.107657,4.047748,2.693699,7.660208,5.750102,-3.743833,-6.253882,-6.772829,4.307809,-8.206434],[2.954481,1.653552,-1.416147,-2.484302,0.525704,0.002228,-7.141886,0.262582,-9.015861,9.409876],[-8.231104,3.496327,-5.331478,5.869778,-9.106018,-8.770347,-2.105500,6.867928,9.080563,-9.210065],[3.285033,-4.760991,-0.820936,0.797606,-6.597859,2.957920,-8.292787,7.982513,-1.064097,-2.245705],[8.157597,4.618679,-0.997283,-5.927342,-1.350128,-6.223509,-6.434851,-2.353924,-4.720586,4.107858],[-2.694186,-7.535953,-4.645391,0.122180,-2.380663,1.141003,-5.557590,5.913467,-7.349933,-3.220253],[-8.991461,-7.504902,5.827843,0.594489,-1.940529,7.586687,2.884901,8.158279,3.617939,9.732809],[-0.515510,9.708603,6.840991,4.952641,-6.280075,-8.046825,-8.999340,7.510013,0.646166,-2.061073],[-0.319038,-1.332000,7.968102,6.708499,7.493928,-7.357424,2.640418,-4.598139,-1.511328,-4.772543],[-6.486295,7.298268,2.954150,-0.260374,4.636744,-1.411319,-0.240979,-8.692977,-3.664431,0.385789],[-4.093980,2.153622,0.687984,-1.773357,8.844859,3.207459,3.929886,9.625184,8.206644,-2.265251],[-9.254678,-2.884760,9.870673,-4.871667,-6.102985,7.110784,0.548663,9.758963,7.180717,-4.533404],[-5.341939,-6.270588,-4.480283,8.870662,0.922608,-6.218525,-2.023113,5.188458,0.691144,-1.750896],[0.712736,-7.112546,-1.641116,8.448114,0.567908,6.058290,8.239057,-5.232972,3.820937,-7.905711],[0.320531,-1.150338,0.038596,5.626591,1.036675,2.002597,-6.797508,4.126949,0.939634,-1.093651],[-8.429474,-3.003726,1.052428,2.761567,-9.066085,6.180776,-6.779198,-7.270811,8.917534,3.303446],[3.929080,5.492880,-6.309395,-5.654445,-7.793356,8.299883,-1.381792,-2.954764,-4.785419,-3.939878],[1.208708,-4.227480,5.072268,-2.052678,-2.058655,1.424377,-0.748049,1.442163,1.866901,-6.719730],[-1.153817,-8.103128,6.989143,-0.437924,-8.866278,5.186755,8.524295,-8.859037,-9.960966,3.356771],[-4.282901,-2.340918,-7.804729,6.554873,4.403924,4.370614,2.354035,1.635822,-5.087532,-8.358171],[-0.144835,1.280710,1.577334,5.279726,-9.996173,3.781642,7.764700,3.084489,3.210961,-8.555584],[-3.457168,1.493477,2.934623,-7.189355,-5.662888,8.770889,-3.279485,-3.843647,-3.593574,0.754137],[2.032388,7.551107,-3.200689,-3.475538,6.830389,4.775332,-8.439283,-4.148723,6.234536,1.825593],[1.682467,-5.829825,0.319927,-0.095254,-3.957855,-7.852799,-6.695496,1.572336,-8.689012,-9.241800],[-8.144244,5.595572,-6.389521,-2.323062,1.784223,-9.116217,-7.648270,-2.179930,1.462048,5.885464],[5.961858,9.614070,4.343385,-7.860876,-4.946457,-3.326367,-3.152624,7.747588,7.400457,-5.340320],[-6.647491,3.994214,-7.258912,-9.544301,-1.862953,5.478884,-9.609509,6.877706,0.168832,4.656803],[7.586952,-0.463094,-2.494827,-7.288025,-2.301421,-1.120594,7.264818,8.802725,3.647071,-7.007093],[-3.937026,7.812515,-3.926086,-9.455254,9.061713,-2.951949,2.286617,-3.284078,-4.455406,6.430494],[-0.312409,3.550734,-0.801607,7.074987,5.829809,8.315788,6.323794,-9.843164,-0.069071,-1.270650],[-6.787778,-1.302579,7.747780,4.763009,4.876867,-8.324435,-3.334102,-6.429624,3.382826,5.677802],[9.783011,-9.117212,2.647774,-1.305960,7.869730,6.018305,7.068606,-1.864366,5.189401,1.777556],[-3.318484,-4.464422,7.294679,4.505656,-4.486043,3.671310,-2.624252,-2.062613,-7.548450,7.273434],[7.294354,-9.978692,-7.227850,-5.183387,-2.274593,-7.137410,2.128217,-5.530812,0.812288,2.592500],[-0.282297,6.127991,-5.579185,-5.232908,5.460538,3.061844,2.913753,4.385476,-0.215876,7.939462],[6.832786,6.683242,-5.986195,-9.216201,-7.720470,3.587505,-5.451289,1.212057,-8.087850,-8.859882],[0.007181,3.875437,3.395825,-1.982122,-0.363771,-3.095172,1.194128,-7.987869,0.010420,-9.621733],[6.793852,-5.281506,-0.966511,-9.380935,-8.216435,-9.070518,-5.484058,-0.680195,8.806800,4.167611],[-8.087095,0.551962,-2.468102,9.307962,-2.691665,1.624054,8.304622,-8.230721,4.233417,-8.655339],[4.992565,5.352381,-5.456859,5.984652,-3.729927,3.142872,-1.231153,-9.283031,7.207643,5.645379],[7.362288,0.941735,-1.909972,3.441870,-3.839710,0.825071,-5.781277,-2.717391,-7.464585,-0.489706],[-5.151031,0.220983,5.499212,1.428114,1.163745,-0.622227,7.249136,5.504903,7.345054,0.937277],[9.438854,6.241556,0.964840,-1.681097,3.632497,-3.629129,3.272785,6.778788,-8.224954,4.181504],[8.730771,-6.606336,3.505228,-2.771202,-2.092859,-6.347434,5.160893,-1.199203,9.404418,-6.266991],[9.636144,3.374227,8.684266,0.324433,9.877828,7.565043,0.065094,-9.387788,-2.303902,0.717714],[-4.223287,-5.985593,-5.969782,0.336873,1.508580,-1.889869,-4.252905,0.577408,-4.551532,3.465420],[7.255067,-7.258180,7.319343,7.807376,-4.889333,-3.427195,9.398135,-1.485659,0.304230,9.041174],[1.810710,-0.724467,4.822111,3.279444,-2.104508,-8.970819,-2.449001,-8.850536,9.501757,8.365529],[0.823732,-2.926056,-2.364025,-6.494336,-6.940316,-7.314384,1.122127,-1.363870,3.632565,1.245866],[-2.153457,1.420329,-1.131585,-2.887792,-1.632800,6.581131,-2.103328,-3.189988,-4.933778,-1.976705],[-1.986922,4.395192,1.208159,4.703979,9.755170,5.575647,-8.455679,-5.272701,-3.007165,-1.564329],[-1.067804,-0.645692,5.551296,1.460472,2.328731,9.662290,9.949074,-1.691059,-4.674350,7.182979],[-5.670073,9.908553,9.761902,2.460921,0.613252,-9.325831,-9.366608,-7.468051,9.832358,3.950331],[7.272154,6.873130,7.249737,-1.048889,4.060135,-6.923154,-2.689255,-0.705440,9.347025,8.696423],[9.069520,1.940623,2.525974,4.787307,9.844722,3.256885,9.511522,4.558453,-0.479775,-5.812787],[8.773374,3.743617,6.410932,-1.862939,-2.170760,6.517431,5.020057,6.265031,-7.149153,-7.979699],[9.984056,-7.512606,-6.991418,-1.814368,1.725373,-4.353522,4.665677,-5.271705,1.332560,7.989027],[3.719793,1.894176,0.315277,6.809149,1.656302,-0.844477,5.600254,-7.097434,-9.143783,8.045748],[2.790662,7.922597,2.203212,3.537163,-2.344326,-1.584018,3.578602,-1.333649,-2.060658,-6.684384],[1.315594,1.726986,-4.190498,-3.847085,-5.758537,-4.445429,2.667811,-6.348560,-8.601743,0.073159],[-3.000446,-9.189423,3.122216,5.007821,-8.997871,-0.607753,-1.296486,-5.633634,9.361164,5.174283],[-8.527179,9.084412,4.268256,4.835271,-4.345674,-2.368415,-5.698845,-3.126554,-0.099783,-1.415629],[-0.665967,-9.621703,-8.504448,9.066616,-1.088499,4.620332,-0.576543,-5.726582,-4.298391,7.301918],[5.943807,2.586800,-9.990459,8.332750,7.246998,5.409677,-6.000176,-0.370917,0.102764,-4.394877],[9.757766,-6.454726,7.309559,9.166998,-9.030626,-3.811117,8.967001,-9.913892,9.960677,-6.921657],[8.353516,-8.054240,9.175706,-8.541872,-4.223634,-1.014955,-4.646629,-6.815223,-3.556878,1.614794],[-2.371274,-1.665535,0.095239,-2.659891,-9.728096,-2.107793,-1.090304,-8.285281,6.233824,-1.706198],[1.118370,7.981490,-0.433019,0.407320,-1.686114,6.561762,-9.236970,-9.927665,-4.456544,9.503072],[9.907308,-5.778056,-0.451076,2.434112,2.394358,-9.157439,6.999441,-4.759188,0.545170,-0.265446],[-0.563288,-1.457559,9.003664,5.056461,2.403555,-1.875702,-5.982501,0.351430,9.298897,-4.875920],[-9.848365,-0.344565,3.384157,3.540289,-3.504395,-6.355918,-2.468073,-5.021212,4.803230,0.314886],[-1.649304,3.913753,9.860117,8.898137,8.386274,5.780111,-6.861802,1.192150,7.981196,-9.899476],[-2.793497,-0.383286,-4.780127,-3.178008,-4.997855,-5.659687,-0.921753,1.488593,-3.945498,-5.011299],[3.498925,-6.962038,5.112948,6.710473,-0.013364,3.422956,-1.490642,6.924523,-8.955252,-2.676491],[-2.932502,6.600474,-8.984557,-7.904481,7.843930,-2.920626,-3.208144,7.362526,6.635296,-4.518190],[-9.324141,-6.750541,-5.894066,5.473495,-2.115286,1.019053,2.949179,8.388444,-2.835061,-5.387809],[-8.046446,-4.914266,8.489088,4.767405,-0.269347,8.497175,5.074187,3.746764,9.569307,-3.690195],[-4.407965,-1.525935,-3.882246,1.042657,8.873872,-0.986411,-6.539362,0.984170,-6.921089,-2.305810],[-6.195755,-8.224278,-0.366169,0.602157,-9.316899,2.068103,-0.197521,-0.013519,5.796352,0.904259],[-1.054569,-2.732309,-0.078072,-9.808106,-8.905719,2.716015,-9.413676,-4.987143,6.758995,4.383402],[8.869111,-3.320619,-2.201436,-0.823594,-1.738802,9.587639,-7.155046,4.881462,6.156705,7.010061],[4.142058,-1.570691,-1.557971,-9.103868,7.679012,-6.412683,-0.314434,-7.228238,8.273383,-6.701907],[-5.997792,-0.966562,7.455218,8.770888,-5.961739,3.739789,8.342162,5.792676,-8.746970,4.190263],[3.767178,4.955440,-9.347611,4.315441,-7.836214,0.836727,5.612196,8.725738,2.053385,9.149892],[-0.512008,4.110553,-5.212512,9.129500,-1.055435,-5.840772,-8.819481,5.000940,6.265991,2.480066],[-0.737523,-4.953539,-7.366230,6.908670,-4.243536,4.007220,0.769592,-5.246272,-5.942144,-8.965596],[-6.801504,-3.100344,-1.037853,3.657148,-6.612911,-8.793309,2.529072,-6.169194,-8.178358,-6.364131],[-3.783562,6.598833,-5.968603,-6.821592,-1.110859,-7.979427,4.561270,1.495904,-6.368932,-4.539140],[1.092791,-8.679097,6.840263,0.475092,-6.719783,8.668438,3.688895,-1.681966,-0.016476,-6.164904],[7.908090,-1.432802,-7.205443,8.521968,-6.365736,6.084058,-1.572738,0.696828,5.647541,7.216842],[-4.663459,-9.863469,-3.702593,9.169140,2.427420,0.151643,-2.641516,-6.818541,5.784609,-4.991663],[3.647616,-7.119033,8.764595,4.356094,-6.704896,-9.402093,0.368984,-0.742488,9.884071,7.952751],[-8.314980,4.736900,-9.600607,0.624731,0.088929,3.432404,0.938212,-1.319559,9.814323,4.414243],[2.279638,-8.245597,6.307936,-4.728048,1.009887,5.836526,-2.272566,-2.325655,-3.137256,-8.803790],[8.377910,-0.021552,1.102861,8.975350,5.475721,-2.337535,-1.550362,0.863638,-4.866145,-0.633459],[7.811633,9.353714,1.503760,-2.702205,0.751979,3.414140,1.740564,0.933047,5.254593,1.894542],[-8.580626,7.022204,9.347420,-3.893670,-0.866606,7.962698,-3.408836,1.883118,-5.926386,-5.565532],[-7.799979,6.240694,5.352664,3.542927,1.945426,1.855865,-0.398845,2.718021,-8.571526,4.123021],[-2.514706,-3.767255,6.624925,-2.608202,-1.198069,0.619452,6.170921,-7.079272,-8.876201,4.543147],[-4.904244,6.975196,3.563734,-3.587524,-2.896854,-2.438393,-8.852865,2.465729,-4.147562,-6.386701],[-6.424400,1.026227,-6.062918,4.487910,6.294271,-2.731543,3.151694,6.238110,-2.336986,-3.298900],[8.924138,-3.973116,-9.995189,-7.727866,7.985721,1.745621,-0.631057,1.287604,-9.089854,9.311252],[5.885314,1.397697,0.900131,7.074734,9.994015,-9.062183,-6.847612,-9.441953,0.196692,7.156232],[9.496691,-5.658496,-8.277672,-9.707156,-0.086849,-2.854607,-6.248991,3.418900,-9.036420,3.399761],[-5.086973,8.501381,-1.019292,1.068827,-7.254380,8.003556,2.246874,9.036200,9.110300,-5.785917],[-8.855777,-8.532315,7.946311,-0.660368,-8.860653,1.264136,-5.682894,-2.734636,-1.189719,-2.026375],[-8.456765,8.412898,6.236625,0.767585,-5.339357,3.735748,3.900558,7.314608,2.894502,-4.648707],[-1.474068,-1.736584,-4.069309,7.855477,8.712373,7.512917,2.381780,0.434471,-1.770316,-6.602847],[7.759520,3.584057,2.704653,9.646650,-6.321457,-7.162625,0.909930,0.643026,6.366029,-1.538153],[-3.409288,0.197597,-7.157657,1.638467,4.350917,-8.729386,1.360690,5.800123,-6.653526,9.732059],[8.363825,7.896847,-1.293002,-7.118038,-0.420694,-7.365115,4.945891,-5.260562,8.067846,-7.850539],[8.972949,4.867233,-4.880286,5.688480,8.834745,5.402870,9.215982,2.791405,-3.447522,7.772706],[-3.133962,9.182973,2.306218,-2.403414,9.062729,-2.306095,1.445428,0.748908,-0.501134,-0.404709],[0.751902,-9.053898,0.128590,8.447150,-7.956794,-2.034966,-4.270437,-4.537617,4.970056,-3.175929],[9.142013,-8.910344,-9.837286,-5.419514,-0.767291,-2.149339,-0.128178,-9.927162,-0.354226,3.454121],[6.826369,-4.312269,-1.023642,5.616276,8.591111,-2.206085,-9.926988,7.984156,9.385021,-9.189660],[-5.206834,1.028840,4.835025,-7.249911,7.890322,-7.886558,9.676415,4.323984,6.397927,-6.577933],[-1.676915,3.150719,9.470567,-0.386580,-0.501274,-6.242036,6.778612,-5.902070,-5.284881,8.898638],[-6.908826,-0.402266,-4.590076,8.672582,-8.677208,-8.456796,4.940685,-2.216907,-5.112815,7.365286],[7.825034,4.220308,4.515002,0.920121,2.070549,-8.389047,8.880988,5.373343,-5.411143,5.755781]], dtype = "float64")#candidate|8194|(143, 10)|const|float64
var_8195 = relay.var("var_8195", dtype = "bool", shape = (576,))#candidate|8195|(576,)|var|bool
var_8196 = relay.var("var_8196", dtype = "uint8", shape = (1, 169))#candidate|8196|(1, 169)|var|uint8
const_8197 = relay.const([[-1.009128,9.486531,1.838255,-7.201094,-4.142269,-3.562563,-5.777807,3.583737,2.460277,-8.231435,-9.771128,-8.199301,-6.620859,-5.218054,-0.332493,5.849133,0.974826,-6.943893,-5.611041,9.125916],[4.661983,4.735875,3.812162,-1.830186,1.544789,-3.640927,-4.475701,2.199091,4.340821,3.019926,0.595191,-6.677118,2.363198,8.714678,4.708629,-3.722980,-7.736943,1.887618,-0.614078,-3.254909],[-2.901157,-7.995531,1.457906,-8.037287,7.501161,-6.135331,-4.301221,3.530099,-8.584031,0.999085,7.805838,-3.521524,5.477524,-0.607835,7.259446,9.436637,7.755121,-5.733665,5.525324,8.635673],[-2.200856,7.266584,4.213655,-5.976539,3.773844,1.121689,0.376869,-8.613874,1.199876,7.248214,9.225078,9.762400,-3.803854,1.965049,-4.895785,-1.488091,8.449946,6.543393,5.882939,-5.946075],[6.792130,7.403062,7.293600,9.361849,-6.688366,0.659542,3.727366,8.877774,5.032301,-3.401651,8.165641,-6.527706,-8.993844,7.137510,-9.587152,9.257994,-9.489205,-7.593322,-3.342197,-5.328357],[-4.744255,3.122335,-7.319188,2.573833,9.250912,1.996492,0.885067,2.913292,6.397664,7.282484,-8.825295,5.459631,1.112440,-6.814062,0.347820,6.365906,1.972591,-4.566709,3.586903,1.198802],[7.061978,2.809558,-6.096004,-2.405298,-2.336522,0.623841,-4.731298,7.442202,6.429106,-6.070915,-8.557908,-2.290252,-2.184835,-7.714808,6.323501,-2.863848,-1.579710,9.062308,2.624513,1.390676],[2.731981,-0.868912,8.793395,0.694836,-0.712374,-0.127751,1.636747,-0.441708,5.323079,9.914632,-1.502015,1.473575,-6.965669,5.791681,-2.149696,6.334168,-4.088884,-9.404482,1.416299,-9.252595],[6.503682,-1.098232,7.783022,-1.726945,5.639269,5.513989,3.465340,8.430150,2.594579,4.996307,2.390411,4.667004,1.573428,4.206157,-1.963680,-7.091746,-5.757779,-3.895007,5.423707,-3.141768],[6.400326,-3.069386,-8.717138,-7.264696,-7.436470,-6.196192,-3.535708,4.259594,5.099462,-9.800867,-1.855243,9.580517,1.773627,4.781589,-9.121769,-7.873778,9.613288,-3.028806,-7.181448,-5.634223]], dtype = "float64")#candidate|8197|(10, 20)|const|float64
call_8193 = relay.TupleGetItem(func_1230_call(relay.reshape(const_8194.astype('float64'), [11, 13, 10]), relay.reshape(var_8195.astype('bool'), [576,]), relay.reshape(var_8196.astype('uint8'), [169,]), relay.reshape(const_8197.astype('float64'), [200,]), ), 3)
call_8198 = relay.TupleGetItem(func_1236_call(relay.reshape(const_8194.astype('float64'), [11, 13, 10]), relay.reshape(var_8195.astype('bool'), [576,]), relay.reshape(var_8196.astype('uint8'), [169,]), relay.reshape(const_8197.astype('float64'), [200,]), ), 3)
var_8202 = relay.var("var_8202", dtype = "uint64", shape = (13, 9, 7))#candidate|8202|(13, 9, 7)|var|uint64
bop_8203 = relay.power(const_8182.astype('float64'), relay.reshape(var_8202.astype('float64'), relay.shape_of(const_8182))) # shape=(13, 9, 7)
var_8208 = relay.var("var_8208", dtype = "float32", shape = (585, 9))#candidate|8208|(585, 9)|var|float32
bop_8209 = relay.bitwise_or(const_8191.astype('uint16'), var_8208.astype('uint16')) # shape=(585, 9)
uop_8213 = relay.asin(const_8194.astype('float32')) # shape=(143, 10)
bop_8218 = relay.subtract(bop_8203.astype('uint32'), relay.reshape(var_8202.astype('uint32'), relay.shape_of(bop_8203))) # shape=(13, 9, 7)
output = relay.Tuple([bop_8183,call_8190,call_8193,var_8195,var_8196,const_8197,bop_8209,uop_8213,bop_8218,])
output2 = relay.Tuple([bop_8183,call_8192,call_8198,var_8195,var_8196,const_8197,bop_8209,uop_8213,bop_8218,])
func_8228 = relay.Function([var_8181,var_8195,var_8196,var_8202,var_8208,], output)
mod['func_8228'] = func_8228
mod = relay.transform.InferType()(mod)
mutated_mod['func_8228'] = func_8228
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8228_call = mutated_mod.get_global_var('func_8228')
var_8230 = relay.var("var_8230", dtype = "uint64", shape = (13, 9, 7))#candidate|8230|(13, 9, 7)|var|uint64
var_8231 = relay.var("var_8231", dtype = "bool", shape = (576,))#candidate|8231|(576,)|var|bool
var_8232 = relay.var("var_8232", dtype = "uint8", shape = (1, 169))#candidate|8232|(1, 169)|var|uint8
var_8233 = relay.var("var_8233", dtype = "uint64", shape = (13, 9, 7))#candidate|8233|(13, 9, 7)|var|uint64
var_8234 = relay.var("var_8234", dtype = "float32", shape = (585, 9))#candidate|8234|(585, 9)|var|float32
call_8229 = func_8228_call(var_8230,var_8231,var_8232,var_8233,var_8234,)
output = call_8229
func_8235 = relay.Function([var_8230,var_8231,var_8232,var_8233,var_8234,], output)
mutated_mod['func_8235'] = func_8235
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6280_call = mod.get_global_var('func_6280')
func_6281_call = mutated_mod.get_global_var('func_6281')
call_8451 = relay.TupleGetItem(func_6280_call(), 0)
call_8452 = relay.TupleGetItem(func_6281_call(), 0)
func_4068_call = mod.get_global_var('func_4068')
func_4069_call = mutated_mod.get_global_var('func_4069')
call_8458 = relay.TupleGetItem(func_4068_call(), 0)
call_8459 = relay.TupleGetItem(func_4069_call(), 0)
output = relay.Tuple([call_8451,call_8458,])
output2 = relay.Tuple([call_8452,call_8459,])
func_8465 = relay.Function([], output)
mod['func_8465'] = func_8465
mod = relay.transform.InferType()(mod)
output = func_8465()
func_8466 = relay.Function([], output)
mutated_mod['func_8466'] = func_8466
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8527 = relay.var("var_8527", dtype = "int8", shape = (14, 2, 6))#candidate|8527|(14, 2, 6)|var|int8
var_8528 = relay.var("var_8528", dtype = "int8", shape = (14, 2, 6))#candidate|8528|(14, 2, 6)|var|int8
bop_8529 = relay.bitwise_or(var_8527.astype('int8'), relay.reshape(var_8528.astype('int8'), relay.shape_of(var_8527))) # shape=(14, 2, 6)
bop_8535 = relay.logical_or(var_8528.astype('bool'), relay.reshape(var_8527.astype('bool'), relay.shape_of(var_8528))) # shape=(14, 2, 6)
func_7192_call = mod.get_global_var('func_7192')
func_7193_call = mutated_mod.get_global_var('func_7193')
call_8550 = func_7192_call()
call_8551 = func_7192_call()
output = relay.Tuple([bop_8529,bop_8535,call_8550,])
output2 = relay.Tuple([bop_8529,bop_8535,call_8551,])
func_8562 = relay.Function([var_8527,var_8528,], output)
mod['func_8562'] = func_8562
mod = relay.transform.InferType()(mod)
var_8563 = relay.var("var_8563", dtype = "int8", shape = (14, 2, 6))#candidate|8563|(14, 2, 6)|var|int8
var_8564 = relay.var("var_8564", dtype = "int8", shape = (14, 2, 6))#candidate|8564|(14, 2, 6)|var|int8
output = func_8562(var_8563,var_8564,)
func_8565 = relay.Function([var_8563,var_8564,], output)
mutated_mod['func_8565'] = func_8565
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2235_call = mod.get_global_var('func_2235')
func_2236_call = mutated_mod.get_global_var('func_2236')
call_8567 = relay.TupleGetItem(func_2235_call(), 0)
call_8568 = relay.TupleGetItem(func_2236_call(), 0)
output = call_8567
output2 = call_8568
func_8576 = relay.Function([], output)
mod['func_8576'] = func_8576
mod = relay.transform.InferType()(mod)
output = func_8576()
func_8577 = relay.Function([], output)
mutated_mod['func_8577'] = func_8577
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5765_call = mod.get_global_var('func_5765')
func_5766_call = mutated_mod.get_global_var('func_5766')
call_8615 = relay.TupleGetItem(func_5765_call(), 2)
call_8616 = relay.TupleGetItem(func_5766_call(), 2)
const_8634 = relay.const([[0.059733,-3.196649,-4.249883,-0.847136,-8.214575,1.680288,-8.814531,-8.198833,-0.065670,-7.288546,9.009239,-6.582123,4.028717,0.769635,-9.411484,-0.650978,6.630076,-8.973844,0.968854,6.141854],[8.412508,-4.212349,9.495387,-5.020664,8.057748,0.383295,6.415252,-2.634057,9.102470,-3.638201,-2.132305,5.486113,3.044013,8.925048,6.270361,-0.029312,-4.321459,-9.563475,-8.587585,4.583940],[1.864464,-4.243325,-2.248465,5.639308,0.324823,-9.793380,-9.271461,5.668415,7.279500,-1.912208,7.895683,3.666016,3.975430,-0.700684,-5.609397,-5.295784,-3.805702,-1.082470,5.131999,2.157129],[2.671205,9.274858,2.131396,-1.765197,0.945094,1.697213,1.014973,-0.515681,5.398136,-2.970054,-3.419502,6.701448,-2.299771,-5.766924,-6.303539,-7.917783,5.386028,8.525003,-7.147546,8.640229],[3.561802,7.183556,5.687817,3.281740,-4.596093,-3.220378,-0.916506,0.769383,-7.314510,4.715086,8.800485,-0.591603,4.564171,-2.072366,3.855675,7.621706,-6.204112,-7.707010,8.378132,-7.422693],[8.132747,-6.331413,9.802486,-3.929914,0.037009,-6.532034,4.867160,8.202169,-8.598954,4.455163,2.998734,-5.934819,8.194037,0.364067,1.730591,-1.820011,8.737212,-3.824362,-1.845540,-0.117283],[-4.260471,2.316940,7.584362,-4.432596,-6.837793,-9.667283,2.570546,7.925640,6.873981,2.167964,0.521044,1.761310,-1.305169,1.900799,4.119933,2.606283,-2.069687,4.984819,8.049345,5.671931],[5.947629,-3.622648,4.510465,4.786478,-2.905484,8.896102,-5.132163,-0.086654,-3.733690,-4.421205,1.656512,-1.117895,-9.628107,-3.293573,2.901224,0.645571,8.256684,0.196555,5.195000,5.393216],[3.813618,2.860957,5.505612,5.420466,8.250125,1.145652,2.580948,-6.165082,-9.171390,3.009508,1.430949,-8.333789,-3.994021,9.967168,9.709137,-4.196752,5.531434,-2.987022,0.460153,-3.763079],[7.872194,-4.338244,0.653458,-3.426904,8.470916,-5.653468,-9.954878,2.514499,-4.667710,5.535258,0.970610,7.907841,6.556852,8.095454,9.007210,-2.350927,-8.699162,0.436304,3.646048,5.832431]], dtype = "float64")#candidate|8634|(10, 20)|const|float64
bop_8635 = relay.greater(call_8615.astype('bool'), relay.reshape(const_8634.astype('bool'), relay.shape_of(call_8615))) # shape=(10, 20)
bop_8638 = relay.greater(call_8616.astype('bool'), relay.reshape(const_8634.astype('bool'), relay.shape_of(call_8616))) # shape=(10, 20)
bop_8642 = relay.logical_and(bop_8635.astype('bool'), relay.reshape(const_8634.astype('bool'), relay.shape_of(bop_8635))) # shape=(10, 20)
bop_8645 = relay.logical_and(bop_8638.astype('bool'), relay.reshape(const_8634.astype('bool'), relay.shape_of(bop_8638))) # shape=(10, 20)
func_4945_call = mod.get_global_var('func_4945')
func_4948_call = mutated_mod.get_global_var('func_4948')
var_8660 = relay.var("var_8660", dtype = "uint16", shape = (126, 1))#candidate|8660|(126, 1)|var|uint16
call_8659 = relay.TupleGetItem(func_4945_call(relay.reshape(var_8660.astype('uint16'), [126,])), 2)
call_8661 = relay.TupleGetItem(func_4948_call(relay.reshape(var_8660.astype('uint16'), [126,])), 2)
func_6280_call = mod.get_global_var('func_6280')
func_6281_call = mutated_mod.get_global_var('func_6281')
call_8662 = relay.TupleGetItem(func_6280_call(), 0)
call_8663 = relay.TupleGetItem(func_6281_call(), 0)
func_4580_call = mod.get_global_var('func_4580')
func_4581_call = mutated_mod.get_global_var('func_4581')
call_8672 = relay.TupleGetItem(func_4580_call(), 0)
call_8673 = relay.TupleGetItem(func_4581_call(), 0)
uop_8676 = relay.sinh(bop_8642.astype('float32')) # shape=(10, 20)
uop_8678 = relay.sinh(bop_8645.astype('float32')) # shape=(10, 20)
var_8680 = relay.var("var_8680", dtype = "float32", shape = (10, 20))#candidate|8680|(10, 20)|var|float32
bop_8681 = relay.bitwise_or(uop_8676.astype('uint32'), relay.reshape(var_8680.astype('uint32'), relay.shape_of(uop_8676))) # shape=(10, 20)
bop_8684 = relay.bitwise_or(uop_8678.astype('uint32'), relay.reshape(var_8680.astype('uint32'), relay.shape_of(uop_8678))) # shape=(10, 20)
func_7916_call = mod.get_global_var('func_7916')
func_7918_call = mutated_mod.get_global_var('func_7918')
call_8690 = relay.TupleGetItem(func_7916_call(), 0)
call_8691 = relay.TupleGetItem(func_7918_call(), 0)
output = relay.Tuple([call_8659,var_8660,call_8662,call_8672,bop_8681,call_8690,])
output2 = relay.Tuple([call_8661,var_8660,call_8663,call_8673,bop_8684,call_8691,])
func_8693 = relay.Function([var_8660,var_8680,], output)
mod['func_8693'] = func_8693
mod = relay.transform.InferType()(mod)
var_8694 = relay.var("var_8694", dtype = "uint16", shape = (126, 1))#candidate|8694|(126, 1)|var|uint16
var_8695 = relay.var("var_8695", dtype = "float32", shape = (10, 20))#candidate|8695|(10, 20)|var|float32
output = func_8693(var_8694,var_8695,)
func_8696 = relay.Function([var_8694,var_8695,], output)
mutated_mod['func_8696'] = func_8696
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7192_call = mod.get_global_var('func_7192')
func_7193_call = mutated_mod.get_global_var('func_7193')
call_8734 = func_7192_call()
call_8735 = func_7192_call()
output = relay.Tuple([call_8734,])
output2 = relay.Tuple([call_8735,])
func_8786 = relay.Function([], output)
mod['func_8786'] = func_8786
mod = relay.transform.InferType()(mod)
output = func_8786()
func_8787 = relay.Function([], output)
mutated_mod['func_8787'] = func_8787
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7690_call = mod.get_global_var('func_7690')
func_7692_call = mutated_mod.get_global_var('func_7692')
call_8793 = relay.TupleGetItem(func_7690_call(), 0)
call_8794 = relay.TupleGetItem(func_7692_call(), 0)
func_1726_call = mod.get_global_var('func_1726')
func_1727_call = mutated_mod.get_global_var('func_1727')
call_8795 = func_1726_call()
call_8796 = func_1726_call()
func_2172_call = mod.get_global_var('func_2172')
func_2173_call = mutated_mod.get_global_var('func_2173')
call_8800 = relay.TupleGetItem(func_2172_call(), 0)
call_8801 = relay.TupleGetItem(func_2173_call(), 0)
output = relay.Tuple([call_8793,call_8795,call_8800,])
output2 = relay.Tuple([call_8794,call_8796,call_8801,])
func_8810 = relay.Function([], output)
mod['func_8810'] = func_8810
mod = relay.transform.InferType()(mod)
mutated_mod['func_8810'] = func_8810
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8810_call = mutated_mod.get_global_var('func_8810')
call_8811 = func_8810_call()
output = call_8811
func_8812 = relay.Function([], output)
mutated_mod['func_8812'] = func_8812
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1927_call = mod.get_global_var('func_1927')
func_1928_call = mutated_mod.get_global_var('func_1928')
call_8853 = func_1927_call()
call_8854 = func_1927_call()
func_6280_call = mod.get_global_var('func_6280')
func_6281_call = mutated_mod.get_global_var('func_6281')
call_8880 = relay.TupleGetItem(func_6280_call(), 0)
call_8881 = relay.TupleGetItem(func_6281_call(), 0)
func_7746_call = mod.get_global_var('func_7746')
func_7750_call = mutated_mod.get_global_var('func_7750')
const_8900 = relay.const(-8, dtype = "int64")#candidate|8900|()|const|int64
const_8901 = relay.const([[-8,-5,-5,-2,-10,5,8,-3]], dtype = "int64")#candidate|8901|(1, 8)|const|int64
call_8899 = relay.TupleGetItem(func_7746_call(relay.reshape(const_8900.astype('int64'), []), relay.reshape(const_8901.astype('int64'), [1, 1, 8]), relay.reshape(call_8853.astype('float64'), [585,]), ), 2)
call_8902 = relay.TupleGetItem(func_7750_call(relay.reshape(const_8900.astype('int64'), []), relay.reshape(const_8901.astype('int64'), [1, 1, 8]), relay.reshape(call_8853.astype('float64'), [585,]), ), 2)
output = relay.Tuple([call_8853,call_8880,call_8899,const_8900,const_8901,])
output2 = relay.Tuple([call_8854,call_8881,call_8902,const_8900,const_8901,])
func_8903 = relay.Function([], output)
mod['func_8903'] = func_8903
mod = relay.transform.InferType()(mod)
mutated_mod['func_8903'] = func_8903
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8903_call = mutated_mod.get_global_var('func_8903')
call_8904 = func_8903_call()
output = call_8904
func_8905 = relay.Function([], output)
mutated_mod['func_8905'] = func_8905
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4888_call = mod.get_global_var('func_4888')
func_4889_call = mutated_mod.get_global_var('func_4889')
call_8923 = relay.TupleGetItem(func_4888_call(), 1)
call_8924 = relay.TupleGetItem(func_4889_call(), 1)
output = call_8923
output2 = call_8924
func_8925 = relay.Function([], output)
mod['func_8925'] = func_8925
mod = relay.transform.InferType()(mod)
mutated_mod['func_8925'] = func_8925
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8925_call = mutated_mod.get_global_var('func_8925')
call_8926 = func_8925_call()
output = call_8926
func_8927 = relay.Function([], output)
mutated_mod['func_8927'] = func_8927
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3262_call = mod.get_global_var('func_3262')
func_3263_call = mutated_mod.get_global_var('func_3263')
call_8967 = func_3262_call()
call_8968 = func_3262_call()
func_6542_call = mod.get_global_var('func_6542')
func_6546_call = mutated_mod.get_global_var('func_6546')
call_8980 = relay.TupleGetItem(func_6542_call(relay.reshape(call_8967.astype('float64'), [13, 5, 9]), relay.reshape(call_8967.astype('uint8'), [13, 5, 9]), ), 0)
call_8981 = relay.TupleGetItem(func_6546_call(relay.reshape(call_8967.astype('float64'), [13, 5, 9]), relay.reshape(call_8967.astype('uint8'), [13, 5, 9]), ), 0)
func_3262_call = mod.get_global_var('func_3262')
func_3263_call = mutated_mod.get_global_var('func_3263')
call_8987 = func_3262_call()
call_8988 = func_3262_call()
output = relay.Tuple([call_8967,call_8980,call_8987,])
output2 = relay.Tuple([call_8968,call_8981,call_8988,])
func_9003 = relay.Function([], output)
mod['func_9003'] = func_9003
mod = relay.transform.InferType()(mod)
mutated_mod['func_9003'] = func_9003
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9003_call = mutated_mod.get_global_var('func_9003')
call_9004 = func_9003_call()
output = call_9004
func_9005 = relay.Function([], output)
mutated_mod['func_9005'] = func_9005
mutated_mod = relay.transform.InferType()(mutated_mod)
const_9038 = relay.const([[[7,-3,-4,-10,2],[5,-7,-9,4,-4],[-6,5,10,-6,4],[10,-1,-8,5,-3],[10,-6,4,6,9],[-2,8,-9,-5,-1],[-2,-2,-5,9,2],[8,-9,-7,-10,-9],[-2,-7,8,-1,3],[-6,4,-2,-10,-2]],[[3,4,-4,5,5],[6,6,-10,-9,1],[-2,9,-5,-8,1],[9,9,8,-4,9],[8,7,-9,10,7],[-2,-6,-8,3,10],[-5,2,4,-7,-4],[8,-4,-5,3,2],[5,-10,8,-6,3],[7,-4,-9,-10,7]],[[-3,-5,1,9,-3],[5,-7,-1,-2,-6],[-2,2,-5,-4,-9],[8,-7,10,-2,3],[2,-7,2,5,-4],[10,7,2,7,6],[1,2,8,-8,-5],[-10,-1,-7,5,-9],[-3,5,-5,2,6],[-1,-2,5,-7,2]],[[5,8,-7,9,6],[-10,-10,-9,-3,8],[8,6,-2,-10,5],[-8,4,-6,-10,-10],[4,-5,7,1,6],[-1,9,-4,10,10],[8,8,6,2,9],[-2,1,9,-3,10],[-2,-4,8,-3,-6],[6,5,-5,-7,6]],[[-8,-1,6,-9,-2],[8,9,6,4,6],[4,-3,5,9,6],[8,-2,6,-10,-6],[-5,-8,-8,2,4],[1,9,9,5,-5],[-1,-6,-1,10,-7],[-6,3,-7,-8,5],[4,-2,-2,-8,-8],[8,6,-4,-4,2]],[[3,4,-2,8,-7],[-2,9,-7,-8,7],[-7,-7,7,-4,6],[-4,4,4,8,-3],[-5,9,2,6,-8],[6,-10,-10,2,9],[8,6,1,7,2],[-6,7,-2,9,9],[-2,5,-5,10,7],[-5,3,8,-1,-5]],[[4,-9,-7,10,-10],[-5,1,6,-3,3],[-6,-6,10,-2,8],[4,-9,3,-4,1],[-9,6,-4,-5,-9],[-8,9,-1,-9,-9],[-8,-7,4,2,2],[-1,10,2,-10,-5],[-7,1,7,6,4],[-3,8,1,9,-1]],[[-9,-3,-10,4,-1],[-8,-2,-6,-2,6],[-8,10,8,-8,-7],[9,9,-2,6,10],[5,-10,6,5,-10],[4,8,4,7,5],[10,7,-8,10,-7],[1,-8,-8,-9,-2],[5,-7,-2,-1,10],[1,1,-9,1,3]]], dtype = "uint16")#candidate|9038|(8, 10, 5)|const|uint16
var_9039 = relay.var("var_9039", dtype = "uint16", shape = (8, 10, 5))#candidate|9039|(8, 10, 5)|var|uint16
bop_9040 = relay.right_shift(const_9038.astype('uint16'), relay.reshape(var_9039.astype('uint16'), relay.shape_of(const_9038))) # shape=(8, 10, 5)
output = bop_9040
output2 = bop_9040
func_9048 = relay.Function([var_9039,], output)
mod['func_9048'] = func_9048
mod = relay.transform.InferType()(mod)
mutated_mod['func_9048'] = func_9048
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9049 = relay.var("var_9049", dtype = "uint16", shape = (8, 10, 5))#candidate|9049|(8, 10, 5)|var|uint16
func_9048_call = mutated_mod.get_global_var('func_9048')
call_9050 = func_9048_call(var_9049)
output = call_9050
func_9051 = relay.Function([var_9049], output)
mutated_mod['func_9051'] = func_9051
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6113_call = mod.get_global_var('func_6113')
func_6114_call = mutated_mod.get_global_var('func_6114')
call_9053 = relay.TupleGetItem(func_6113_call(), 2)
call_9054 = relay.TupleGetItem(func_6114_call(), 2)
output = call_9053
output2 = call_9054
func_9077 = relay.Function([], output)
mod['func_9077'] = func_9077
mod = relay.transform.InferType()(mod)
output = func_9077()
func_9078 = relay.Function([], output)
mutated_mod['func_9078'] = func_9078
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2806_call = mod.get_global_var('func_2806')
func_2808_call = mutated_mod.get_global_var('func_2808')
call_9127 = relay.TupleGetItem(func_2806_call(), 0)
call_9128 = relay.TupleGetItem(func_2808_call(), 0)
output = call_9127
output2 = call_9128
func_9163 = relay.Function([], output)
mod['func_9163'] = func_9163
mod = relay.transform.InferType()(mod)
output = func_9163()
func_9164 = relay.Function([], output)
mutated_mod['func_9164'] = func_9164
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7192_call = mod.get_global_var('func_7192')
func_7193_call = mutated_mod.get_global_var('func_7193')
call_9245 = func_7192_call()
call_9246 = func_7192_call()
output = relay.Tuple([call_9245,])
output2 = relay.Tuple([call_9246,])
func_9256 = relay.Function([], output)
mod['func_9256'] = func_9256
mod = relay.transform.InferType()(mod)
mutated_mod['func_9256'] = func_9256
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9256_call = mutated_mod.get_global_var('func_9256')
call_9257 = func_9256_call()
output = call_9257
func_9258 = relay.Function([], output)
mutated_mod['func_9258'] = func_9258
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2515_call = mod.get_global_var('func_2515')
func_2516_call = mutated_mod.get_global_var('func_2516')
call_9288 = relay.TupleGetItem(func_2515_call(), 0)
call_9289 = relay.TupleGetItem(func_2516_call(), 0)
output = relay.Tuple([call_9288,])
output2 = relay.Tuple([call_9289,])
func_9304 = relay.Function([], output)
mod['func_9304'] = func_9304
mod = relay.transform.InferType()(mod)
mutated_mod['func_9304'] = func_9304
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9304_call = mutated_mod.get_global_var('func_9304')
call_9305 = func_9304_call()
output = call_9305
func_9306 = relay.Function([], output)
mutated_mod['func_9306'] = func_9306
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5461_call = mod.get_global_var('func_5461')
func_5463_call = mutated_mod.get_global_var('func_5463')
call_9331 = relay.TupleGetItem(func_5461_call(), 2)
call_9332 = relay.TupleGetItem(func_5463_call(), 2)
output = relay.Tuple([call_9331,])
output2 = relay.Tuple([call_9332,])
func_9333 = relay.Function([], output)
mod['func_9333'] = func_9333
mod = relay.transform.InferType()(mod)
output = func_9333()
func_9334 = relay.Function([], output)
mutated_mod['func_9334'] = func_9334
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9385 = relay.var("var_9385", dtype = "int64", shape = (14, 4, 6))#candidate|9385|(14, 4, 6)|var|int64
const_9386 = relay.const([[[-9,4,-10,-8,-3,9],[3,-4,10,-3,3,7],[-3,10,5,-3,-6,4],[9,-5,2,6,1,-6]],[[-10,-5,10,6,2,5],[5,4,6,-1,4,7],[-2,-3,-3,-4,-8,5],[-3,-3,6,6,5,-5]],[[10,8,-2,9,-6,-8],[1,-3,3,7,10,10],[-8,-9,6,6,2,9],[-6,1,-3,4,-3,1]],[[4,1,-9,-10,-9,10],[3,-3,-9,-10,-3,9],[-9,9,8,7,9,-6],[9,5,-4,-5,-10,-5]],[[-3,4,-5,-1,3,-6],[10,-3,-9,7,-6,8],[-7,1,1,8,1,9],[2,8,-10,6,-8,-10]],[[1,-7,-2,-9,9,-10],[-5,4,8,-2,3,-8],[6,6,-7,1,6,7],[4,-8,-5,3,7,-8]],[[1,7,-9,9,-3,9],[3,-7,9,-8,-9,8],[-5,8,8,-6,5,3],[10,-1,-6,2,4,8]],[[-5,-8,3,10,7,-1],[-3,4,-2,-4,-6,7],[9,1,1,7,-6,-8],[-1,8,-6,4,3,7]],[[-2,10,-8,-2,-6,-8],[-4,1,-2,-8,9,2],[4,3,4,5,-1,-8],[1,5,4,-4,-10,10]],[[-6,-4,6,-8,-4,8],[-3,7,-9,2,-4,-7],[4,-1,-8,8,-1,9],[-10,8,2,-3,-10,-6]],[[5,6,8,-10,-7,-9],[-1,-1,9,8,10,5],[-1,-4,9,9,-1,1],[-10,-4,-3,-6,-9,-5]],[[-8,10,-10,-10,3,3],[8,-4,-6,-10,8,-7],[-6,5,9,-6,4,7],[-10,6,-4,3,-2,-3]],[[-2,7,9,-10,7,2],[7,5,3,5,2,5],[2,-10,-5,-3,7,6],[3,1,-3,-8,-3,2]],[[-6,9,10,-3,-4,-7],[5,-5,-9,10,-10,6],[6,-4,6,4,4,-9],[7,-5,5,9,1,4]]], dtype = "int64")#candidate|9386|(14, 4, 6)|const|int64
bop_9387 = relay.greater_equal(var_9385.astype('bool'), relay.reshape(const_9386.astype('bool'), relay.shape_of(var_9385))) # shape=(14, 4, 6)
output = relay.Tuple([bop_9387,])
output2 = relay.Tuple([bop_9387,])
F = relay.Function([var_9385,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_9385,], output2)
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
