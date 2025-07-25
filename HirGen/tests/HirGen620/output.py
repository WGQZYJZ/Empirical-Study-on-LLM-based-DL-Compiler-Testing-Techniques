import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_0 = relay.var("var_0", dtype = "float32", shape = (12, 13, 3))#candidate|0|(12, 13, 3)|var|float32
var_1 = relay.var("var_1", dtype = "float32", shape = (12, 13, 3))#candidate|1|(12, 13, 3)|var|float32
bop_2 = relay.greater(var_0.astype('bool'), relay.reshape(var_1.astype('bool'), relay.shape_of(var_0))) # shape=(12, 13, 3)
output = relay.Tuple([bop_2,])
output2 = relay.Tuple([bop_2,])
func_7 = relay.Function([var_0,var_1,], output)
mod['func_7'] = func_7
mod = relay.transform.InferType()(mod)
mutated_mod['func_7'] = func_7
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7_call = mutated_mod.get_global_var('func_7')
var_9 = relay.var("var_9", dtype = "float32", shape = (12, 13, 3))#candidate|9|(12, 13, 3)|var|float32
var_10 = relay.var("var_10", dtype = "float32", shape = (12, 13, 3))#candidate|10|(12, 13, 3)|var|float32
call_8 = func_7_call(var_9,var_10,)
output = call_8
func_11 = relay.Function([var_9,var_10,], output)
mutated_mod['func_11'] = func_11
mutated_mod = relay.transform.InferType()(mutated_mod)
var_345 = relay.var("var_345", dtype = "bool", shape = (13, 15, 15))#candidate|345|(13, 15, 15)|var|bool
var_346 = relay.var("var_346", dtype = "bool", shape = (13, 15, 15))#candidate|346|(13, 15, 15)|var|bool
bop_347 = relay.logical_or(var_345.astype('bool'), relay.reshape(var_346.astype('bool'), relay.shape_of(var_345))) # shape=(13, 15, 15)
output = bop_347
output2 = bop_347
func_371 = relay.Function([var_345,var_346,], output)
mod['func_371'] = func_371
mod = relay.transform.InferType()(mod)
var_372 = relay.var("var_372", dtype = "bool", shape = (13, 15, 15))#candidate|372|(13, 15, 15)|var|bool
var_373 = relay.var("var_373", dtype = "bool", shape = (13, 15, 15))#candidate|373|(13, 15, 15)|var|bool
output = func_371(var_372,var_373,)
func_374 = relay.Function([var_372,var_373,], output)
mutated_mod['func_374'] = func_374
mutated_mod = relay.transform.InferType()(mutated_mod)
var_553 = relay.var("var_553", dtype = "float64", shape = (3, 7, 15))#candidate|553|(3, 7, 15)|var|float64
var_554 = relay.var("var_554", dtype = "float64", shape = (3, 7, 15))#candidate|554|(3, 7, 15)|var|float64
bop_555 = relay.mod(var_553.astype('float64'), relay.reshape(var_554.astype('float64'), relay.shape_of(var_553))) # shape=(3, 7, 15)
func_371_call = mod.get_global_var('func_371')
func_374_call = mutated_mod.get_global_var('func_374')
const_560 = relay.const([[False,True,False,False,False,True,False,False,False,True,True,True,False,True,False,False,True,True,True,False,True,False,False,False,False,False,False,True,False,False,True,False,True,True,True,True,False,True,False,False,False,True,False,False,False,False,False,True,True,True,True,True,True,True,True,False,True,False,True,True,False,False,False,True,True,True,True,False,False,True,False,False,False,False,False,False,True,False,True,False,True,False,True,True,False,True,True,True,True,False,True,True,True,True,False,False,False,True,False,False,False,True,False,False,True,False,False,False,False,True,True,True,False,False,False,False,True,True,True,False,False,False,True,True,True,False,True,True,True,False,True,False,True,True,False,False,True,True,True,True,False,False,True,False,False,True,False,False,True,False,False,True,False,False,False,False,False,True,True,True,True,True,True,False,False,False,True,False,True,False,True,True,False,False,False,False,False,False,False,True,False,True,False,True,True,False,True,True,True,False,False,True,True,False,True,False,False,False,False,True,False,True,False,False,False,False,True,False,True,True,True,True,False,True,False,True,True,True,False,False,False,True,True,True,True,True,True,True,True,True,False,False,True,False,False,True,True,True,True,False,True,False,True,True,True,False,True,False,True,True,False,True,False,False,True,True,True,False,False,False,False,False,False,True,True,True,False,False,False,True,False,True,True,True,True,False,True,False,False,True,True,False,False,False,False,True,True,True,False,False,False,False,False,False,True,True,True,True,True,False,False,True,True,True,True,False,True,False,False,True,True,False,True,False,False,False,True,True,True,True,True,True,True,False,False,False,True,True,True,True,True,True,False,True,False,True,True,True,False,False,False,True,False,False,True,False,False,True,True,True,False,True,True,False,True,True,False,False,False,False,True,False,True,False,True,False,True,False,True,True,False,False,True,False,False,False,False,False,True,False,True,False,True,False,False,False,True,False,False,False,False,False,False,False,False,True,False,True,True,True,True,False,True,False,False,True,False,True,True,False,True,True,False,False,True,False,False,True,False,False,True,True,False,True,True,False,False,True,False,True,False,True,True,False,True,False,True,True,True,True,True,False,False,True,False,True,True,False,False,False,False,True,True,True,False,False,True,False,True,True,False,True,False,True,True,True,True,True,True,False,False,False,False,False,False,False,True,True,False,False,True,True,True,False,False,False,False,True,False,True,True,False,True,True,False,False,True,True,True,False,False,True,False,False,True,False,True,True,False,True,True,True,False,False,False,False,False,False,False,True,False,True,True,True,False,True,True,True,True,True,True,True,False,False,True,False,False,False,True,False,False,False,False,False,False,False,True,True,False,True,False,False,False,True,True,False,True,True,False,False,False,True,True,False,True,False,False,False,True,True,False,True,True,False,True,False,False,False,True,True,True,True,True,True,False],[True,False,True,False,False,True,False,True,False,False,True,True,True,True,False,False,True,True,False,False,False,False,False,True,True,True,False,False,True,False,False,False,False,False,False,False,True,False,True,False,False,False,True,True,True,True,False,True,False,False,True,False,False,True,True,True,True,False,True,False,False,True,False,False,True,False,False,True,False,True,True,False,False,False,False,True,True,False,False,True,False,True,True,False,True,True,True,False,True,False,False,True,True,False,True,True,False,True,False,False,False,True,False,False,True,False,False,False,False,False,True,False,False,False,False,True,True,True,True,False,True,True,True,True,True,False,False,True,True,False,True,False,True,True,False,False,False,False,False,False,True,True,True,True,True,True,False,True,True,True,True,False,False,True,True,True,True,True,False,True,True,True,True,False,False,True,False,False,False,False,True,True,True,False,False,True,True,False,False,False,True,True,True,True,False,False,False,False,False,False,True,True,True,False,False,True,True,False,False,True,True,True,False,False,True,False,True,False,False,True,True,True,True,False,False,True,False,False,True,False,False,False,False,True,False,False,True,False,False,True,True,True,False,False,False,True,False,True,True,True,True,False,False,False,False,True,True,True,True,True,True,False,True,True,True,False,True,False,False,False,True,True,True,True,True,True,False,False,True,False,True,False,False,True,False,True,False,True,False,False,False,True,False,False,True,True,False,False,False,False,False,True,True,False,True,True,True,True,True,False,True,False,False,False,True,False,True,False,False,True,False,False,False,False,False,True,True,False,False,True,False,False,True,False,False,False,True,False,True,False,False,True,False,True,True,True,True,False,True,True,True,True,False,True,True,False,True,True,True,True,False,True,True,True,True,False,True,False,False,True,False,False,False,False,True,True,False,True,True,True,False,False,True,False,True,False,True,False,True,False,True,False,True,True,True,True,True,True,True,True,False,False,True,False,False,True,True,False,False,False,False,False,False,True,True,True,True,False,False,True,False,True,True,True,False,False,False,True,True,False,False,True,False,False,True,False,True,False,True,True,False,True,True,False,False,False,False,True,False,False,False,False,True,True,False,False,False,False,True,True,False,False,True,False,False,False,True,True,True,False,False,True,True,True,False,True,False,False,False,False,False,True,True,True,False,True,True,False,True,True,False,False,True,True,False,True,True,True,False,False,True,False,False,False,True,False,True,True,False,False,False,False,True,True,True,True,False,True,False,True,False,False,True,True,True,False,False,False,True,False,True,True,False,True,True,True,True,True,True,True,True,True,True,False,False,False,True,False,True,True,True,True,True,True,False,False,True,False,True,False,False,False,True,False,True,True,False,False,False,True,True,True,False,False,True,False,False,False,False,False,False,True,True,True,False,False,False,True,False,True,False,True,True,True,True],[False,False,True,False,False,False,True,True,False,True,False,False,True,True,False,True,True,False,True,False,False,True,False,False,True,True,False,False,False,True,False,False,False,True,False,False,False,True,False,False,False,False,True,False,True,True,True,False,True,False,True,False,True,True,False,True,True,False,True,True,True,True,False,True,True,False,False,True,False,False,True,False,False,False,False,False,False,False,False,True,False,True,True,False,True,True,True,False,True,False,True,True,False,True,False,True,False,False,False,False,False,True,False,True,False,True,True,False,True,True,True,True,True,True,True,False,False,False,False,False,True,True,True,True,True,True,False,True,False,False,True,False,True,True,True,True,False,False,True,True,False,True,True,True,False,False,True,False,True,True,False,False,False,True,True,True,True,True,False,True,True,True,True,False,True,True,False,True,True,True,True,True,False,False,False,False,False,True,True,True,False,True,True,True,True,False,False,False,True,True,True,False,False,False,True,True,True,True,True,True,False,False,False,True,False,True,True,False,False,False,False,True,False,True,False,True,False,False,True,True,True,False,False,False,False,True,True,False,False,False,True,False,False,True,True,False,False,True,True,True,True,True,False,True,False,False,False,False,False,True,False,False,True,False,False,False,True,True,False,True,False,True,True,False,False,True,True,True,False,False,False,True,True,False,True,True,False,True,False,False,True,False,False,False,False,False,False,True,False,False,False,False,True,True,False,False,False,True,True,False,True,True,False,False,True,True,False,True,False,False,True,True,False,False,False,False,False,False,True,False,True,True,False,False,False,True,False,True,False,True,True,False,False,True,False,True,False,False,False,True,False,False,False,False,False,False,False,False,True,True,True,False,False,True,False,True,False,True,False,True,False,True,True,True,True,True,False,True,False,True,False,False,True,True,True,True,True,True,True,False,True,False,False,True,False,True,False,False,False,False,True,False,False,False,True,True,False,False,False,False,True,True,False,False,False,True,True,True,True,False,False,False,True,False,True,True,True,False,True,True,False,True,False,False,True,True,True,True,True,False,True,False,True,False,False,True,True,True,False,False,False,False,False,True,True,False,False,False,False,True,False,False,False,False,True,False,True,False,True,True,False,True,True,True,True,False,False,False,True,True,True,True,True,True,False,False,True,False,True,True,False,True,False,False,True,True,False,False,True,False,True,False,True,True,True,False,True,False,False,False,True,True,False,False,True,False,True,False,True,False,False,True,True,False,True,False,True,False,False,False,False,False,False,True,True,False,True,False,False,True,False,True,True,False,True,False,True,False,False,False,False,False,True,True,False,False,True,True,False,False,False,False,False,False,True,True,False,False,True,False,False,True,True,True,False,True,True,True,True,True,True,False,False,False,True,False,False,True,False,True,True,False,True,True,False],[True,False,True,True,True,True,True,False,True,False,False,False,True,True,True,True,False,True,True,False,True,True,True,False,True,False,True,True,True,False,False,False,False,True,False,True,False,True,True,True,False,False,True,True,True,True,False,False,False,True,False,True,True,True,True,False,True,False,False,True,False,False,True,False,True,True,True,True,True,True,True,True,True,False,False,False,True,True,False,False,False,True,True,True,False,True,False,False,True,False,True,False,False,False,False,True,False,False,False,True,True,True,False,False,False,False,False,True,True,True,True,False,False,True,True,False,False,True,False,True,True,True,True,True,False,False,False,False,False,True,True,True,False,True,True,False,True,True,False,True,False,True,True,False,False,False,True,False,False,True,False,True,True,True,True,True,True,True,True,True,False,False,False,True,True,True,True,False,True,True,True,True,True,False,False,True,True,True,False,True,False,False,False,True,True,True,False,True,True,True,False,True,True,True,False,False,False,False,True,True,True,False,True,False,True,True,False,False,False,False,True,False,False,True,False,True,True,False,False,False,False,True,True,True,False,False,False,False,False,True,False,True,True,True,False,False,False,False,False,False,False,True,False,False,True,False,True,False,True,False,False,True,True,True,False,True,True,False,True,True,True,True,True,True,False,True,True,False,True,False,False,True,True,True,True,False,True,False,False,False,False,False,True,True,False,False,False,True,False,False,True,False,True,False,True,False,True,False,False,False,False,True,True,False,False,False,False,True,False,True,False,True,True,True,False,True,True,True,True,False,True,False,False,False,False,True,False,True,True,True,True,False,False,False,False,False,False,False,True,False,True,True,True,True,True,False,False,False,True,True,False,False,True,False,False,True,True,True,False,True,False,True,True,False,True,True,False,True,True,True,False,True,True,True,False,False,True,False,False,False,False,True,False,True,True,True,True,True,False,True,False,False,True,True,False,False,False,False,False,True,True,False,False,False,True,False,False,True,True,True,True,True,False,False,False,True,True,True,False,True,True,False,True,False,True,True,False,True,True,False,True,False,False,True,True,False,False,True,True,True,False,False,False,False,False,False,False,True,False,False,False,True,True,True,True,False,False,True,False,True,False,True,False,False,False,True,False,False,False,True,True,True,False,True,True,False,False,True,False,False,False,False,True,True,False,False,True,False,True,True,False,True,False,False,False,True,True,False,True,True,False,True,False,False,False,False,False,False,True,False,False,True,True,True,False,True,True,False,True,True,True,True,False,False,True,False,True,False,True,False,False,True,True,False,True,False,False,True,False,False,False,True,True,True,False,False,False,False,False,True,True,True,True,True,True,False,False,False,True,True,True,True,False,False,True,True,False,False,False,True,False,False,False,True,True,False,True,True,False,True,True,True,True,False,True],[False,False,True,True,True,False,False,False,False,False,False,True,True,False,True,False,False,False,False,True,True,False,True,True,True,False,False,False,True,False,True,False,False,False,True,False,False,True,False,False,True,False,True,False,False,True,False,False,True,False,False,False,True,True,True,False,True,True,False,True,True,False,True,False,False,False,False,True,True,False,True,False,True,True,True,True,False,True,False,True,False,False,True,True,True,True,True,False,False,True,True,False,True,False,False,False,False,False,True,True,False,False,False,True,True,True,True,True,False,True,False,False,True,False,True,False,True,False,False,True,False,False,True,True,False,True,True,True,True,False,False,False,True,False,True,False,True,False,False,False,True,False,False,False,False,False,False,True,False,True,True,False,True,False,False,True,False,True,False,True,False,True,True,True,True,True,True,True,True,True,True,True,False,True,True,False,True,False,False,False,True,True,False,False,True,False,True,True,False,False,True,False,True,False,True,False,True,False,True,True,False,False,False,False,False,True,False,True,True,False,True,False,True,False,False,True,False,False,False,False,False,True,False,True,False,True,True,True,False,True,False,False,True,False,False,True,False,False,True,True,True,False,False,False,False,False,True,True,False,False,True,False,True,False,True,True,True,True,True,True,False,True,True,True,False,True,True,False,False,False,True,True,False,True,True,True,False,True,False,False,True,True,True,False,True,False,False,True,True,True,False,True,False,False,True,False,True,False,False,True,False,False,False,False,True,False,True,True,True,True,False,False,True,True,False,False,True,False,True,True,True,False,False,False,False,True,False,True,True,True,True,True,True,True,False,False,True,True,False,False,True,False,False,False,True,True,False,False,True,False,True,True,False,False,True,False,True,True,True,True,False,False,False,True,False,False,False,True,False,False,False,True,False,False,True,True,True,True,True,True,True,True,False,True,True,True,True,False,False,True,True,True,True,False,False,True,False,False,True,False,False,True,True,False,True,False,True,True,False,True,False,True,False,False,True,True,True,False,True,True,True,True,False,True,True,True,False,True,True,True,False,False,False,True,False,False,False,False,True,False,True,True,True,True,True,False,False,False,True,True,True,False,False,False,True,True,True,False,True,False,True,True,False,False,False,True,False,False,True,True,False,False,False,False,True,True,False,True,True,True,False,False,False,True,False,True,False,True,True,True,False,True,False,False,True,True,True,True,True,False,False,False,False,False,False,True,True,False,False,False,False,True,False,False,False,True,True,False,False,True,False,False,False,False,True,True,True,False,False,True,True,False,True,True,False,True,True,True,True,True,True,True,False,True,True,False,False,True,True,True,False,True,True,False,True,False,True,True,True,True,False,False,True,True,True,True,False,False,False,True,False,True,True,False,False,False,True,True,True,False,False,True,True,True,True]], dtype = "bool")#candidate|560|(5, 585)|const|bool
call_559 = func_371_call(relay.reshape(const_560.astype('bool'), [13, 15, 15]), relay.reshape(const_560.astype('bool'), [13, 15, 15]), )
call_561 = func_371_call(relay.reshape(const_560.astype('bool'), [13, 15, 15]), relay.reshape(const_560.astype('bool'), [13, 15, 15]), )
output = relay.Tuple([bop_555,call_559,const_560,])
output2 = relay.Tuple([bop_555,call_561,const_560,])
func_568 = relay.Function([var_553,var_554,], output)
mod['func_568'] = func_568
mod = relay.transform.InferType()(mod)
mutated_mod['func_568'] = func_568
mutated_mod = relay.transform.InferType()(mutated_mod)
func_568_call = mutated_mod.get_global_var('func_568')
var_570 = relay.var("var_570", dtype = "float64", shape = (3, 7, 15))#candidate|570|(3, 7, 15)|var|float64
var_571 = relay.var("var_571", dtype = "float64", shape = (3, 7, 15))#candidate|571|(3, 7, 15)|var|float64
call_569 = func_568_call(var_570,var_571,)
output = call_569
func_572 = relay.Function([var_570,var_571,], output)
mutated_mod['func_572'] = func_572
mutated_mod = relay.transform.InferType()(mutated_mod)
var_815 = relay.var("var_815", dtype = "float64", shape = (4, 4, 7))#candidate|815|(4, 4, 7)|var|float64
var_816 = relay.var("var_816", dtype = "float64", shape = (4, 4, 7))#candidate|816|(4, 4, 7)|var|float64
bop_817 = relay.not_equal(var_815.astype('bool'), relay.reshape(var_816.astype('bool'), relay.shape_of(var_815))) # shape=(4, 4, 7)
func_7_call = mod.get_global_var('func_7')
func_11_call = mutated_mod.get_global_var('func_11')
var_830 = relay.var("var_830", dtype = "float32", shape = (1, 468))#candidate|830|(1, 468)|var|float32
call_829 = relay.TupleGetItem(func_7_call(relay.reshape(var_830.astype('float32'), [12, 13, 3]), relay.reshape(var_830.astype('float32'), [12, 13, 3]), ), 0)
call_831 = relay.TupleGetItem(func_11_call(relay.reshape(var_830.astype('float32'), [12, 13, 3]), relay.reshape(var_830.astype('float32'), [12, 13, 3]), ), 0)
func_371_call = mod.get_global_var('func_371')
func_374_call = mutated_mod.get_global_var('func_374')
const_835 = relay.const([False,True,True,False,True,False,False,False,True,False,True,True,False,False,True,False,True,False,False,True,False,False,True,False,True,True,True,True,False,True,True,True,False,False,True,True,True,True,True,False,True,True,True,False,True,False,False,False,True,True,True,True,True,True,False,True,False,True,False,False,False,True,True,False,True,True,True,False,False,True,False,False,False,False,False,True,False,False,False,True,True,True,True,True,False,True,False,False,False,False,True,False,True,False,False,False,True,True,True,False,False,True,False,False,True,False,False,False,False,False,True,False,True,False,True,False,True,True,False,True,True,True,True,False,False,True,False,True,True,True,True,True,True,True,False,False,True,False,False,False,False,False,False,True,False,True,True,False,False,False,True,True,True,True,True,True,False,True,True,True,True,False,True,False,False,True,False,True,True,True,True,True,True,True,False,True,False,False,True,False,False,True,True,True,False,False,True,False,False,False,False,True,False,True,True,False,False,True,False,True,False,True,False,True,True,False,True,True,False,False,False,False,True,True,False,True,False,True,False,False,True,False,True,True,True,False,False,True,True,False,False,False,True,False,True,False,False,False,False,True,True,False,True,False,True,True,False,True,False,False,True,True,False,False,True,True,False,True,False,False,True,False,False,False,False,True,True,False,False,True,True,True,True,True,True,False,False,True,False,True,True,True,False,True,False,True,False,False,False,False,False,True,False,False,False,False,False,True,True,False,False,False,True,True,True,False,True,False,False,True,True,True,True,True,True,True,True,True,True,True,False,False,True,False,False,True,True,False,False,False,False,False,False,True,True,False,False,False,False,False,False,True,True,True,False,False,False,True,False,True,True,False,True,False,False,False,True,True,False,True,True,True,True,False,False,False,False,False,False,False,False,False,True,False,True,True,False,True,True,False,True,False,False,False,False,True,False,True,False,True,False,False,False,True,False,False,True,False,True,True,False,True,False,True,True,True,False,False,True,True,False,False,True,True,False,True,False,True,False,False,False,False,False,False,True,False,False,False,False,True,False,False,True,False,True,False,True,False,False,False,True,True,False,True,False,True,False,False,False,True,False,False,True,True,False,True,True,False,True,False,False,True,False,True,True,False,True,True,False,False,True,True,True,False,False,True,True,True,True,True,False,True,True,True,False,True,False,False,True,False,False,True,True,False,False,True,False,False,False,False,False,True,False,True,True,False,False,False,True,True,True,True,False,False,True,True,True,True,True,True,True,True,False,True,True,True,False,False,True,False,False,True,True,False,False,True,True,False,True,False,True,True,False,True,True,True,False,True,False,True,False,False,False,False,True,False,True,True,False,False,True,False,True,False,True,True,True,False,True,True,False,False,False,False,False,True,True,False,False,False,False,False,False,False,True,True,False,False,False,False,True,True,True,False,True,False,False,True,False,True,False,False,False,False,True,False,True,False,False,False,False,False,False,False,True,True,True,True,False,True,False,True,False,True,True,False,True,True,True,True,True,True,True,True,True,False,True,False,True,True,False,True,False,True,False,True,False,True,False,False,True,False,True,True,True,True,True,False,False,False,True,True,True,True,False,False,True,True,True,False,True,True,False,True,False,False,False,True,True,False,True,False,True,True,False,False,False,True,True,False,False,False,False,True,True,False,False,True,False,True,True,True,False,True,False,True,True,False,False,True,False,True,True,True,False,True,False,False,True,True,True,True,True,True,False,True,True,False,False,True,True,True,False,False,True,False,True,False,False,True,True,True,False,True,False,True,False,False,True,True,True,False,False,True,True,True,False,True,True,False,False,True,True,True,True,False,True,False,True,False,True,False,True,True,True,True,False,False,False,False,True,True,False,False,False,False,True,False,True,False,False,True,True,False,False,False,False,False,False,True,False,True,False,True,True,True,False,True,True,False,True,True,False,False,True,False,False,False,True,True,False,True,False,False,True,True,False,False,True,True,True,True,False,True,False,True,True,False,True,False,True,False,True,True,False,False,True,False,False,False,True,True,False,False,True,True,True,True,True,False,False,True,True,True,False,True,False,True,True,True,False,False,False,True,True,False,False,True,True,False,True,False,True,True,False,False,True,True,False,False,True,False,True,False,True,False,True,False,True,True,True,True,True,True,True,True,False,True,False,True,True,True,True,True,True,False,True,False,True,True,False,True,False,False,True,True,False,True,True,True,False,True,True,True,False,False,False,False,True,False,True,False,False,True,True,True,True,True,True,False,False,True,True,False,True,True,False,True,False,True,True,False,False,False,True,True,False,False,True,True,False,True,True,False,False,True,True,True,False,False,True,False,False,True,True,True,False,True,True,False,False,False,False,True,False,True,False,False,True,True,True,False,False,False,False,False,True,False,True,True,False,True,False,False,False,True,False,False,False,True,False,False,True,False,True,True,True,True,True,True,True,False,True,True,False,True,False,False,True,True,True,False,False,True,False,False,False,False,False,False,True,False,True,False,False,False,True,False,False,False,True,True,False,False,False,True,True,False,True,True,False,False,True,False,False,True,True,False,False,True,True,True,False,False,False,False,False,True,False,False,False,True,True,False,True,False,True,True,False,False,False,False,True,True,True,True,False,False,True,False,True,False,False,True,False,False,False,True,True,False,True,True,False,True,False,True,True,True,False,True,False,False,False,True,True,True,False,False,True,True,False,False,False,False,False,False,False,False,True,False,False,True,True,False,False,True,False,True,True,False,False,True,True,False,False,False,True,False,False,False,True,True,True,True,True,True,False,False,True,True,False,True,False,True,False,False,True,False,True,False,False,False,True,True,False,True,False,False,True,False,False,False,True,True,False,True,False,False,True,True,True,True,True,False,False,True,False,True,True,False,True,True,False,False,True,False,True,True,False,False,True,True,True,True,False,True,False,True,True,True,False,False,False,True,False,False,False,True,False,True,True,True,True,True,False,False,True,True,True,False,False,False,True,True,True,True,False,True,False,True,False,True,True,False,False,False,True,True,True,True,False,False,False,True,True,False,True,False,False,False,False,False,True,True,True,False,True,True,False,True,False,False,False,True,True,True,True,False,False,False,True,False,False,True,False,True,False,True,False,False,False,False,False,True,False,True,True,True,False,True,False,False,False,True,True,True,False,True,True,False,True,False,False,False,True,False,True,True,False,True,True,False,False,True,True,False,False,False,True,False,False,True,False,False,False,False,True,False,True,False,False,False,False,True,False,True,True,False,True,True,True,False,True,True,False,False,True,False,True,False,True,True,False,True,True,False,True,False,True,False,False,True,True,False,False,True,True,False,True,False,True,True,True,True,False,True,True,False,True,False,False,False,True,False,False,False,True,True,False,False,False,False,True,True,False,False,False,False,False,False,False,True,True,True,False,True,False,False,True,False,False,False,False,False,False,False,False,True,False,True,True,False,True,True,True,False,True,True,False,True,True,False,False,False,False,True,False,False,True,True,False,True,True,True,True,False,True,False,True,True,True,True,True,False,False,False,False,True,False,False,False,True,True,False,False,True,True,False,True,False,True,False,False,True,True,True,True,False,True,False,False,False,True,True,True,True,False,True,False,False,False,False,True,True,True,True,False,False,True,True,True,True,True,True,False,False,False,True,True,False,True,True,False,True,False,True,False,False,True,True,False,True,True,False,False,False,True,False,True,True,True,False,False,True,True,False,True,True,True,False,True,False,True,False,True,False,True,False,False,False,True,True,True,False,True,True,True,False,True,False,True,True,False,True,False,True,True,True,False,False,False,False,True,True,False,False,True,True,False,False,False,True,True,True,False,False,True,True,False,False,True,False,True,True,True,True,False,True,True,False,True,True,False,False,False,False,True,False,False,True,False,False,True,True,True,True,True,False,False,True,True,True,True,False,False,True,False,False,False,True,False,True,False,True,False,False,True,True,False,True,False,False,True,True,True,True,False,False,True,False,False,False,True,True,True,True,False,True,True,False,False,False,False,False,True,False,False,False,True,True,False,True,True,True,True,True,False,True,True,False,False,True,False,True,True,True,True,True,False,False,False,False,False,False,False,True,False,True,False,True,False,False,False,True,True,True,False,False,True,False,False,True,True,False,False,False,False,True,False,False,False,False,True,False,False,True,False,False,False,False,True,False,False,True,False,True,True,False,True,False,False,True,True,False,False,True,False,False,True,False,False,True,False,True,True,False,True,True,False,True,True,True,False,True,True,False,True,False,False,False,False,True,False,True,True,False,False,True,False,True,False,False,False,False,False,False,True,True,True,True,False,True,True,False,False,False,False,True,False,True,False,False,False,False,True,True,False,True,False,False,True,False,False,True,True,False,True,False,True,True,True,False,False,False,False,False,False,True,False,False,False,False,False,False,False,True,True,False,True,True,False,False,False,False,True,True,True,True,True,False,False,False,False,False,True,True,False,True,False,False,False,False,False,False,False,False,False,True,False,True,False,False,True,False,True,False,True,False,True,False,False,True,True,True,True,False,False,False,True,False,False,True,False,True,False,False,True,False,True,False,True,True,False,False,False,True,False,True,True,False,False,False,True,True,True,True,True,True,True,False,True,True,False,True,False,False,True,False,False,False,False,True,True,False,True,True,False,True,True,True,True,True,True,True,False,False,False,True,True,True,True,False,False,True,True,True,True,False,True,True,False,True,False,False,True,True,True,True,True,False,True,False,True,False,True,True,True,True,False,False,False,False,True,True,True,False,False,True,True,True,False,True,False,True,True,True,False,True,True,True,True,False,False,True,False,True,False,True,True,True,False,True,True,True,False,False,True,False,True,False,True,False,False,True,True,True,True,True,False,False,True,False,False,True,True,False,False,True,False,True,False,False,True,True,True,True,False,False,False,True,True,True,True,True,True,False,False,False,False,True,False,True,True,False,False,False,False,False,True,False,False,False,False,True,True,True,False,True,False,False,True,True,False,False,False,True,True,False,True,True,True,True,False,False,True,False,False,True,False,False,False,False,False,False,True,True,False,False,True,False,False,False,True,False,False,True,True,True,True,False,False,True,True,False,True,False,False,False,False,True,False,False,True,False,False,True,True,False,True,False,False,True,False,True,False,True,False,True,False,False,False,True,True,True,True,False,False,False,False,False,True,False,False,False,False,False,True,False,True,False,False,True,False,True,True,False,False,True,True,False,True,True,True,False,True,True,True,True,True,True,True,False,False,True,False,False,True,False,False,False,False,True,False,False,False,True,False,False,False,False,False,False,True,False,False,False,True,True,True,False,True,False,False,True,True,False,True,True,False,False,True,True,True,True,True,True,False,False,True,True,False,True,True,True,True,True,False,False,True,True,False,False,False,False,True,True,True,False,False,True,False,False,False,True,True,False,False,False,False,True,True,False,True,False,True,False,True,True,True,False,True,True,False,True,False,True,False,True,False,True,False,False,True,True,False,False,True,False,False,True,False,True,True,True,True,False,True,True,False,False,True,True,False,False,False,False,True,False,True,True,True,True,False,False,False,False,True,True,False,True,False,False,True,True,True,False,False,True,True,False,True,True,True,True,True,True,True,False,True,False,False,True,False,False,True,False,False,False,False,False,False,False,True,True,False,False,True,False,True,True,False,True,False,True,False,True,False,False,True,True,False,True,False,False,True,False,True,True,False,True,False,False,True,True,True,True,True,True,True,True,False,True,False,False,False,False,True,False,False,False,False,True,False,False,True,True,False,False,True,True,True,True,True,True,False,True,False,True,False,False,False,False,True,False,False,False,True,True,False,True,True,False,False,True,True,False,True,True,False,False,False,False,True,False,True,True,True,True,False,True,True,True,True,True,True,True,True,False,False,True,False,True,False,False,True,True,False,False,False,True,False,True,True,True,True,False,False,False,True,False,True,True,True,False,False,True,True,True,True,True,False,True,False,False,False,True,True,False,True,False,True,True,True,False,False,False,False,False,False,False,True,True,True,False,True,True,True,False,False,True,True,False,False,True,True,False,True,False,True,False,False,False,False,True,True,False,True,True,True,True,True,False,False,False,False,True,True,False,True,True,True,False,False,True,False,True,False,True,True,True,True,False,True,True,True,False,False,True,False,True,False,True,True,True,False,True,False,True,True,False,True,False,False,True,False,False,False,False,True,True,True,True,True,False,False,True,True,False,False,True,True,False,False,False,True,False,False,False,False,True,False,True,False,False,False,False,True,False,False,False,True,True,True,True,True,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,True,False,False,True,False,True,True,False,False,True,True,True,False,False,True,False,True,False,False,False,False,False,False,False,False,True,True,False,True,True,False,True,True,True,False,True,False,False,True,False,True,False,False,True,False,True,True,True,True,True,False,True,True,False,False,False,True,True,False,True,False,True,False,True,False,False,False,False,False,True,True,True,True,True,False,True,False,True,True,False,False,True,True,False,True,True,False,True,False,False,False,False,True,False,True,True,False,True,False,True,False,True,False,True,False,True,True,False,False,False,False,True,True,False,True,False,True,True,True,False,True,True,False,True,True,False,False,False,True,False,True,False,True,True,True,True,False,False,False,True,False,False,False,True,False,True,False,False,False,True,False,True,True,False,False,False,False,True,False,False,True,True,False,True,True,True,False,True,False,False,False,False,True,False,False,True,True,False,True,True,True,True,True,False,False,True,True,False,False,True,False,False,True,False,True,False,False,True,True,False,False,False,False,True,False,False,False,False,False,False,True,False,True,False,False,True,False,True,False,False,True,False,False,False,True,True,False,True,True,True,True,True,True], dtype = "bool")#candidate|835|(2925,)|const|bool
call_834 = func_371_call(relay.reshape(const_835.astype('bool'), [13, 15, 15]), relay.reshape(const_835.astype('bool'), [13, 15, 15]), )
call_836 = func_371_call(relay.reshape(const_835.astype('bool'), [13, 15, 15]), relay.reshape(const_835.astype('bool'), [13, 15, 15]), )
output = relay.Tuple([bop_817,call_829,var_830,call_834,const_835,])
output2 = relay.Tuple([bop_817,call_831,var_830,call_836,const_835,])
func_842 = relay.Function([var_815,var_816,var_830,], output)
mod['func_842'] = func_842
mod = relay.transform.InferType()(mod)
mutated_mod['func_842'] = func_842
mutated_mod = relay.transform.InferType()(mutated_mod)
func_842_call = mutated_mod.get_global_var('func_842')
var_844 = relay.var("var_844", dtype = "float64", shape = (4, 4, 7))#candidate|844|(4, 4, 7)|var|float64
var_845 = relay.var("var_845", dtype = "float64", shape = (4, 4, 7))#candidate|845|(4, 4, 7)|var|float64
var_846 = relay.var("var_846", dtype = "float32", shape = (1, 468))#candidate|846|(1, 468)|var|float32
call_843 = func_842_call(var_844,var_845,var_846,)
output = call_843
func_847 = relay.Function([var_844,var_845,var_846,], output)
mutated_mod['func_847'] = func_847
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1952 = relay.var("var_1952", dtype = "float32", shape = (3, 6, 16))#candidate|1952|(3, 6, 16)|var|float32
uop_1953 = relay.sin(var_1952.astype('float32')) # shape=(3, 6, 16)
func_842_call = mod.get_global_var('func_842')
func_847_call = mutated_mod.get_global_var('func_847')
const_1968 = relay.const([[-7.399509,-0.552168,5.119849,-2.657220,-0.322763,7.045185,-3.643195,-4.495681,-1.133798,2.083477,4.619896,-8.274285,-1.949137,-2.966650,-6.484816,-8.392910,-0.736814,1.976473,8.965245,-1.492925,8.258499,7.207704,9.299375,-5.764924,3.522548,-0.123686,9.328046,-1.334460],[-0.800459,-7.674738,-2.237589,6.346630,-3.154965,-1.813853,-3.078328,8.379421,1.723085,3.578779,5.591919,-5.425882,-2.951260,6.025505,-4.950030,1.031215,-8.795849,0.721634,-3.594645,8.878843,6.416292,-5.380301,-0.499881,5.181256,0.380313,-6.934306,4.550847,6.432761],[0.877238,3.163199,7.677885,9.826826,0.476658,-3.398039,5.848005,-2.065499,-0.995509,9.506721,-7.029458,-8.773530,1.483133,-5.104481,3.366515,-4.711768,-7.992679,-3.952139,-6.420365,1.273216,-9.586245,5.836679,0.023015,-3.089649,4.135169,9.960110,6.393758,1.288140],[-6.533562,4.197938,1.296530,2.752970,9.040190,2.065776,3.522062,7.284275,1.985562,0.904534,-4.680326,-7.904673,6.825979,-2.770003,9.501469,-9.860252,2.163396,7.207769,9.803654,7.476300,0.142336,0.492170,1.934812,-8.875523,5.750843,-5.726779,-4.806476,6.902065]], dtype = "float64")#candidate|1968|(4, 28)|const|float64
var_1969 = relay.var("var_1969", dtype = "float32", shape = (468,))#candidate|1969|(468,)|var|float32
call_1967 = relay.TupleGetItem(func_842_call(relay.reshape(const_1968.astype('float64'), [4, 4, 7]), relay.reshape(const_1968.astype('float64'), [4, 4, 7]), relay.reshape(var_1969.astype('float32'), [1, 468]), ), 0)
call_1970 = relay.TupleGetItem(func_847_call(relay.reshape(const_1968.astype('float64'), [4, 4, 7]), relay.reshape(const_1968.astype('float64'), [4, 4, 7]), relay.reshape(var_1969.astype('float32'), [1, 468]), ), 0)
func_7_call = mod.get_global_var('func_7')
func_11_call = mutated_mod.get_global_var('func_11')
call_2035 = relay.TupleGetItem(func_7_call(relay.reshape(var_1969.astype('float32'), [12, 13, 3]), relay.reshape(var_1969.astype('float32'), [12, 13, 3]), ), 0)
call_2036 = relay.TupleGetItem(func_11_call(relay.reshape(var_1969.astype('float32'), [12, 13, 3]), relay.reshape(var_1969.astype('float32'), [12, 13, 3]), ), 0)
output = relay.Tuple([uop_1953,call_1967,const_1968,var_1969,call_2035,])
output2 = relay.Tuple([uop_1953,call_1970,const_1968,var_1969,call_2036,])
func_2037 = relay.Function([var_1952,var_1969,], output)
mod['func_2037'] = func_2037
mod = relay.transform.InferType()(mod)
var_2038 = relay.var("var_2038", dtype = "float32", shape = (3, 6, 16))#candidate|2038|(3, 6, 16)|var|float32
var_2039 = relay.var("var_2039", dtype = "float32", shape = (468,))#candidate|2039|(468,)|var|float32
output = func_2037(var_2038,var_2039,)
func_2040 = relay.Function([var_2038,var_2039,], output)
mutated_mod['func_2040'] = func_2040
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2606 = relay.const([[[0.487821,-9.312494,-3.509175,-9.761347,8.243830,9.129393,-1.860441,5.549913,-2.293660,4.740294],[7.775499,1.848596,-6.494524,2.340317,1.335549,-2.871489,-9.569166,-9.787002,-6.831962,2.370768],[-8.083754,-4.682164,5.299773,-9.312211,-0.897747,7.121192,2.057834,-6.091855,0.843604,-2.476096],[-2.022975,-9.514671,4.876237,-4.390516,3.919212,4.558894,-0.440912,7.891215,-2.304016,-5.127261],[7.922431,-5.342438,-0.377340,7.664322,-2.066992,4.156516,-5.565500,0.882222,-0.319046,9.046803],[2.638428,-8.093284,-5.563450,3.824065,1.884378,-8.201276,8.505180,3.194153,1.938657,9.660765],[-1.836651,0.319461,-4.522728,3.790967,-3.631517,8.244561,2.161488,1.290843,8.635142,-7.112958],[-6.860946,3.156690,4.264853,-4.972068,5.152759,-6.574940,-9.624844,-0.162443,-6.617555,1.872319],[-5.349701,-2.839130,-0.992792,-6.422256,-4.536584,-2.867402,8.669732,-5.536570,-3.774614,3.070732],[3.304993,-3.128481,3.321627,-5.088125,-5.154143,-3.344719,-5.170043,-9.062483,6.365535,-2.611458],[-3.159300,-4.897131,1.197739,-2.705532,4.099193,3.594161,-5.924615,-5.573783,5.169718,6.146173],[9.506070,-6.038958,2.426714,-8.746544,5.475298,-1.333034,-0.085415,4.124443,-6.780339,8.566789],[-8.469583,-6.865921,-3.872076,-4.280962,8.166948,7.310724,-1.190925,3.966671,5.016338,-3.027081],[-7.322573,-5.669125,0.251504,-8.558676,1.732825,-7.458589,7.622802,-6.191084,2.134886,2.492174],[5.049079,4.551779,-6.201978,9.930269,7.160618,0.992265,-7.994210,-0.680185,8.054630,6.693194]],[[-2.848512,-4.431104,-2.208054,-8.193747,-3.605201,6.731950,-9.845585,2.878110,1.095365,-1.758846],[-0.007607,-8.997904,9.705223,-0.594418,-4.356326,-5.674081,8.122987,-1.889159,7.195054,-3.609061],[-7.748918,2.877371,-5.987626,3.452689,8.934598,-7.708886,4.821763,6.728033,3.538055,-6.449502],[6.689702,2.039071,8.615171,9.804557,-5.343787,-0.745218,4.170162,4.839866,-4.927993,4.466512],[1.757151,0.329414,-0.544386,9.951590,0.789354,0.285342,-2.802615,0.167133,-4.739102,0.947989],[-0.471258,2.778643,7.601913,-1.826066,-0.712008,-9.716702,7.335667,-9.311470,-3.227020,-4.071329],[4.424391,-1.944884,-5.885778,-3.554200,-2.486270,7.254284,8.140785,-0.537817,0.915091,3.566241],[-3.085331,5.760889,3.617367,-7.484668,-2.406676,5.964408,-7.211928,5.543717,-0.486779,-9.552052],[2.268379,3.891107,-4.414468,-3.759738,-2.381540,2.430830,5.175528,7.917525,4.242804,-7.127678],[-8.632593,2.362130,2.967290,0.710760,-3.844018,0.928102,4.388428,4.897245,-3.466116,8.599836],[4.273575,-6.305838,-6.760996,3.037371,3.145851,7.897205,-7.569232,-9.287138,1.329393,1.518868],[2.258261,-4.157322,2.248432,1.530224,8.743468,0.145879,2.067800,3.682121,6.047782,4.112201],[-9.380566,-9.301752,-6.430567,-0.566804,-3.397391,4.990842,-4.804398,-1.182342,1.410500,-9.958025],[-4.866062,3.115418,1.270531,0.280843,-7.851681,6.802936,1.003246,9.302328,-9.633585,-7.032047],[4.030898,5.429343,3.715643,0.009023,2.711966,0.965788,3.947556,0.477618,9.138162,3.305629]],[[-1.136410,-0.943811,-2.549726,4.841540,9.339564,5.891841,3.966275,2.223588,-5.419966,-7.189259],[-5.140152,-4.087828,-5.353040,-6.316166,-5.443787,4.137683,-5.823096,1.035712,1.433213,2.747037],[-4.336731,3.447920,3.704256,-8.043180,-5.649271,0.474734,-0.237431,-0.386415,-4.460305,-2.318383],[3.362241,6.655870,0.086346,-8.891501,8.600416,0.869469,4.692670,8.562122,9.190980,-0.158710],[-8.722752,-8.514142,0.656945,-0.698621,1.914794,7.977774,-8.324321,-8.669915,2.475608,5.510829],[5.291589,-7.993795,8.358863,6.745196,1.448083,-3.351812,-4.012603,-9.302904,-1.368316,5.080788],[6.502219,-2.343382,9.311885,1.413446,3.801554,3.939886,4.274288,2.451239,5.033565,-6.029819],[7.865393,7.407286,8.915176,1.697028,-8.002909,-2.633502,5.209978,0.510152,6.271529,6.799592],[5.266832,5.585361,-3.184052,-2.027892,-5.726687,-7.683894,1.439472,4.705594,1.246798,-4.977317],[6.727670,5.721350,5.005004,3.469071,8.377180,-1.823980,4.505725,-2.618945,-4.227823,9.665289],[8.169176,-2.677621,2.311406,7.545449,3.563182,-7.576375,-8.510635,9.485407,3.404227,8.259583],[-7.847364,2.078010,9.288267,9.959365,-6.067548,-5.476331,7.139922,9.073315,-9.263952,8.376615],[-8.429967,-7.111328,-5.822854,9.006597,-1.475954,-4.380705,-7.690435,-2.642990,7.891381,3.469055],[0.710209,9.017014,5.032111,4.895639,-9.719914,3.011285,8.585517,3.562257,7.648689,8.356597],[4.581694,-0.376903,8.883130,-8.111076,5.959955,0.800069,2.324724,6.749596,9.840418,3.998304]],[[2.474974,-3.612187,-5.403760,-6.549325,-6.564542,-0.591214,-0.896960,3.742357,9.017575,-1.915685],[-1.907410,2.208141,1.758769,-1.952080,-2.777734,-7.508813,-4.248482,-3.212614,-2.726778,-8.313261],[-8.168825,9.018111,-6.652338,-3.420614,-8.541602,-0.520070,-9.774391,-6.865787,-0.221161,-8.165823],[-9.549556,-5.551813,-8.475238,-3.693951,-7.975174,5.561567,3.900832,0.722239,-2.005217,9.681036],[-0.821569,3.855046,-0.771902,-4.592852,-1.871027,5.669350,5.285229,3.236919,-4.663465,1.606291],[-8.630978,7.611438,7.631653,6.816276,-4.080495,-4.282835,-0.739153,-3.879250,2.548587,4.930207],[7.591021,6.697032,7.315823,-7.175731,-9.520418,-7.497060,1.395681,-2.176595,-6.232890,-1.846458],[-3.355203,2.084793,-0.332543,3.218160,5.229331,5.667689,1.465086,4.200534,1.424887,-4.471822],[5.835624,-9.210812,-3.023641,6.184412,4.054154,-7.436170,-9.540956,-1.463019,0.141592,9.446611],[2.336269,0.941949,4.368221,6.982585,4.606983,-4.341323,-0.069359,2.942236,9.056725,0.298202],[-3.977098,-4.629737,3.097064,7.103501,6.229126,8.104526,9.236879,2.269220,-8.905506,4.490118],[3.311631,-4.581782,-0.712158,-2.397523,9.399266,-8.034318,8.679247,-8.572547,-9.853906,2.830331],[-6.528517,-0.443085,-7.110549,-4.962672,-8.166315,-7.825277,2.474346,6.303071,-2.035059,9.998519],[7.574863,1.654025,4.308681,8.550931,6.392930,4.064469,-3.689951,0.608290,3.726735,1.124422],[6.750494,6.700577,-9.795307,-8.885528,4.839513,-6.504908,-8.559594,3.186446,-2.621053,6.337963]],[[-0.015904,3.759245,-2.585360,3.221670,5.920946,4.755654,-4.473008,2.011828,2.083436,4.292678],[-2.912974,4.261385,1.559805,-1.260127,6.428113,7.751647,-5.186388,-2.496192,2.951951,-6.342397],[-2.087382,6.897303,8.701667,-0.125266,-3.144652,9.827696,7.648903,5.179203,0.453567,-3.847302],[5.267138,-6.587272,7.398316,-0.107230,-7.166296,7.337333,-6.055883,2.027234,1.736880,-0.318991],[7.739994,-8.931306,-8.999911,1.232185,1.596633,9.170979,8.991761,-1.850575,-8.663774,9.173461],[-2.137601,-0.189188,4.830392,-8.669649,0.579089,0.031071,-1.007460,6.277263,5.770950,-0.881792],[3.103981,-0.809872,-6.558475,6.963087,4.825444,1.706382,9.913169,4.150091,-5.086208,0.024912],[-9.483238,-2.016332,1.461032,-3.577062,4.157774,1.987336,-1.020837,1.949569,7.785931,5.774298],[-3.613249,-0.839275,-4.755827,-4.272983,5.373244,-2.436308,-2.931910,-2.136927,5.788473,4.324466],[1.017129,7.048801,-9.886319,-9.774785,7.486334,-3.291955,1.917663,4.739113,-4.158762,-2.955073],[5.092030,-7.231097,0.090975,4.460162,6.389822,4.666966,-1.811533,-6.730134,-3.456259,-7.917492],[-6.136288,7.890067,5.721933,-3.536343,-5.650613,7.151280,2.868003,-5.859035,-7.497566,0.193021],[-7.284778,-7.121340,9.615521,7.636606,-1.084648,3.116822,-7.753954,-1.239920,4.678961,-7.452588],[0.423629,-7.195644,6.191533,9.941904,-4.647336,6.906561,-1.786225,1.253057,-8.373603,6.621354],[-0.470955,7.228258,2.515982,-0.031239,-8.871564,-4.717654,-2.339988,3.901179,7.590065,4.254840]],[[2.457200,-6.391280,5.445541,-5.510894,-1.254775,-7.776584,-7.322142,-0.722977,0.146724,1.231807],[1.935849,5.767977,-3.211919,0.785873,7.137293,4.173007,1.497443,-6.406953,-4.013538,-2.477814],[-5.828241,2.406279,-6.310164,-4.684843,6.276994,-3.892857,-9.523224,-0.355080,-3.116693,-1.035913],[4.067980,-3.181296,-0.662027,3.668704,1.765557,9.990923,-1.809214,1.789675,-9.253319,-7.373083],[5.994673,-1.092065,-7.994035,-9.309714,-3.653312,-2.723613,-4.109330,-1.888166,-9.191661,2.814292],[6.594939,2.958278,-5.134832,2.835188,9.703437,-3.621199,-5.311183,-3.553205,9.000825,7.694785],[5.195604,6.044147,-8.271300,-8.071273,3.776917,0.795054,7.117971,-5.320677,9.255774,-9.199142],[1.203635,9.800349,-4.131739,-7.221243,-0.353872,9.330028,-2.456715,8.870282,3.426649,5.244734],[-5.698590,4.550067,4.671271,1.520878,6.427393,1.149025,-2.041609,-6.491555,-8.243698,-6.097066],[-0.503272,1.176088,9.672561,-4.320296,-7.933030,6.808898,-3.552423,-1.486305,6.003683,-5.926046],[-7.170602,7.483942,-6.426559,9.652726,8.295913,4.194445,2.526745,-2.840164,1.721726,5.353264],[-2.472639,-9.478493,-5.761783,-3.277908,-8.877073,-3.098392,7.035775,2.761117,-0.345909,-8.455230],[0.023745,5.076025,-4.206563,8.249420,-2.032741,-0.528227,4.293830,1.522033,7.323038,6.733598],[-5.525229,-4.301682,-8.897282,3.490283,-2.260194,-8.569137,6.791921,3.309540,2.785426,-0.633129],[3.050614,-3.280063,9.116402,-0.007904,4.998881,5.018968,-6.098315,2.335412,3.010619,4.489563]],[[3.992930,5.167649,8.364071,-0.528061,8.975929,6.956585,7.762341,-4.977640,9.936773,-3.916479],[-0.313897,0.189362,6.254623,0.184736,3.185440,5.874739,-1.429658,-1.510867,2.227524,-1.970029],[7.881541,1.363268,9.626503,7.542771,7.452564,-8.004351,8.072855,-8.568280,-9.311840,-8.421548],[-8.732740,-6.832377,-3.290886,-2.863385,-8.472235,5.047368,-0.626587,-6.849887,-1.983875,0.536749],[4.028337,4.290180,2.510167,-1.857118,-6.669586,5.682367,-7.490659,3.304071,-9.931626,-3.635675],[1.216883,-3.416314,-8.085961,6.564580,9.761693,-9.077598,-5.575724,9.558923,7.679103,-5.051379],[-7.831752,-2.746543,1.767505,-1.370669,-4.612163,-1.047531,-4.714612,7.391000,-0.464085,1.435514],[1.449989,-9.381737,3.994640,5.976372,3.684634,-3.662087,-9.028683,-0.636725,0.616859,7.839234],[9.767268,8.805394,5.956454,3.766397,7.289975,4.049835,-7.178046,0.980038,6.732885,5.253710],[-3.459904,3.916827,-0.152319,-0.900133,-8.948102,9.201363,-7.367341,7.063550,-7.687381,8.542714],[0.927207,-0.024581,-0.774702,8.441433,9.303387,9.456605,5.640672,-2.871517,-5.637010,1.690309],[-6.609546,5.663950,8.733409,-7.935830,0.167649,1.932613,-5.035135,-8.185656,9.693853,0.632497],[-9.442634,-4.946252,4.813046,-9.626833,-6.109235,-1.388461,-9.496195,9.508441,-4.197590,2.556671],[5.415922,-7.748354,3.360957,-0.423342,-9.133121,6.563746,-5.570447,-7.447247,-0.018630,-0.816823],[-3.583397,6.217191,-2.393341,-8.640157,6.492577,-8.825708,9.164134,-0.306685,3.909139,6.094252]],[[-9.737390,9.848198,1.532750,-9.205716,-9.952933,-8.104824,6.938169,6.456513,-3.236520,-6.103104],[-2.878655,-8.081206,9.259951,-9.114397,9.176281,8.428582,-5.998208,4.209980,-8.994176,5.724183],[-8.313940,-4.462483,6.707512,5.154961,2.488656,7.239961,-0.949199,1.965263,9.478822,-0.842547],[-8.815600,-4.652213,-7.652938,-6.555562,-3.014360,7.034067,2.695716,-9.083630,-9.690052,-7.303696],[-0.160033,6.888502,3.255614,-5.631929,-8.021144,3.377345,-2.833357,1.216065,9.111790,-7.939628],[0.886187,-3.596033,6.605370,9.299377,-0.193156,5.718402,-8.174931,7.559715,-8.927355,-7.354436],[7.951721,8.037841,9.718446,-1.837925,-2.533146,-0.909826,8.465415,-3.630053,-5.711579,-6.985435],[4.554838,7.837223,-6.219287,6.257507,-8.179736,1.485697,0.576459,-0.324110,0.093709,-6.823471],[2.273709,5.724594,2.831110,9.258725,9.303134,5.853298,2.534091,-9.494533,1.509075,-3.300427],[7.506823,3.947644,-7.778190,-8.713009,9.032444,3.661053,8.030001,2.783147,-0.810163,-2.892019],[-1.689614,-4.663840,-1.447207,0.106621,-5.908590,-2.693224,5.773587,4.427335,5.864623,8.666420],[-6.147524,8.819511,8.770903,-7.992346,4.555178,6.274400,-8.906441,2.381915,1.905076,6.471435],[1.712925,4.543766,5.825181,-5.535221,-2.632530,2.499353,7.650389,6.407742,0.895553,-7.328188],[-9.227844,-0.535288,-4.755197,-5.629614,-9.300703,2.382559,9.375981,-1.139514,4.099929,6.273870],[-2.874668,-0.685758,3.296877,-4.013990,-7.125809,3.341452,8.924143,4.849178,5.157087,9.299562]],[[3.348388,3.595118,2.013195,-7.028446,0.808515,0.992790,-3.475065,1.676077,1.690505,6.206260],[-1.403705,-4.997138,-9.240270,4.788038,1.175619,-1.280032,-0.163668,2.440221,0.213148,-1.448295],[7.769160,6.252712,-8.780444,2.739371,-5.303403,9.580943,2.061122,-6.671635,7.524259,-9.931316],[-6.266563,-2.572817,-3.186469,0.544231,3.292279,-7.673973,4.107066,-5.708430,-2.311455,5.601424],[-2.939610,-8.236104,-0.123385,-4.385301,-0.099754,5.487999,6.258091,2.246727,3.634970,3.248886],[9.733725,-0.377760,8.573026,-4.258201,-6.746122,2.158244,-0.841050,2.008605,-7.816881,-3.800593],[-8.330840,-5.085552,1.601798,5.293389,-7.806407,2.053877,6.245762,-5.434060,6.211631,-1.874784],[-5.736412,-5.081648,8.866346,2.703478,8.422383,3.310677,7.760847,7.768442,0.435499,-0.552689],[-2.071499,1.445078,7.526729,-3.639918,-1.106158,-5.960957,-4.812342,4.143855,-4.738823,-9.937967],[7.872054,1.821951,6.542689,9.573541,-8.710313,-1.314080,-0.266789,-3.821012,9.498986,-6.848015],[3.499186,-7.763759,5.838691,-7.715938,-3.169757,-0.016653,-4.408571,3.104858,-7.684892,-7.538059],[-5.158381,7.680760,0.040619,-6.515014,4.803863,-0.044215,6.181732,-9.038787,3.509706,8.724379],[1.113985,9.539452,8.651210,7.988742,4.414007,-0.745113,-4.561753,-0.076695,7.863620,-7.568006],[7.044861,-3.071435,1.162692,-6.481288,3.386998,9.198899,7.540224,-8.262980,7.956064,-9.701715],[7.750490,-7.307761,7.741136,8.704056,9.857186,6.031065,1.195856,2.091469,-5.717067,4.328348]],[[3.957179,9.789368,1.235651,-8.392599,9.844974,1.176960,7.562077,2.168356,0.191452,-6.531262],[-8.620986,4.825122,6.311927,7.607845,-1.221638,7.599239,8.992043,-3.628477,-3.165521,7.462215],[-3.900540,-1.215022,-1.429090,-2.407043,6.470763,-5.295715,-0.456984,5.750449,-5.603138,4.941256],[0.527492,6.140930,5.529819,8.796714,-1.913931,-5.834937,3.992891,-2.510027,-6.337907,1.351821],[7.700204,8.125667,-1.495728,9.022246,7.458730,2.910286,1.411416,7.054548,3.498009,-0.215346],[9.416115,-2.794971,-8.172840,-5.870878,3.756185,-2.993641,2.168081,-6.885781,-2.904302,4.991579],[-1.173889,-6.544683,4.396056,7.272390,-7.816738,-4.042797,-7.651239,-8.040432,6.550860,9.962456],[7.659978,-7.572336,0.102294,-4.876347,-3.514702,-0.934746,-9.834769,8.304606,-9.757454,-3.641093],[-0.942499,1.629038,5.368735,3.879437,-4.301305,2.017815,-8.767626,6.755782,-8.948555,7.895175],[6.776748,-2.017634,-0.971631,6.579388,-4.590546,9.048032,-9.156206,9.784410,2.760913,-2.452489],[9.935070,9.670904,5.941631,3.497982,-6.913307,3.625323,-1.429963,7.123512,7.741147,-1.672124],[3.650139,-4.749363,-7.046602,8.066686,8.893360,0.489030,-2.197524,-0.644240,7.527449,1.136696],[0.750844,6.330395,-3.142309,-3.351004,4.472642,6.649610,0.303884,-0.675155,9.540346,3.972097],[-5.342334,6.451594,1.509685,-9.350393,-6.247366,-2.657771,-2.408111,7.022209,-1.238325,-5.276671],[-5.085024,-5.587360,-8.777077,1.010485,7.250566,-2.358732,-0.488160,-5.585088,8.570973,-1.793638]],[[-3.514877,0.347299,1.270672,-4.413955,8.585888,3.813559,-1.932493,7.694598,9.979810,2.514777],[1.380668,-2.751315,7.624670,4.252865,0.690346,-9.648213,-5.704778,7.921607,8.102798,1.152168],[-3.336053,-4.417831,9.057843,0.103391,5.963149,5.674822,-7.948503,-9.899352,-2.331286,3.276530],[6.330723,5.291021,5.399486,5.516654,-7.662408,1.010555,-3.629646,-2.416156,7.368857,-5.181211],[-3.827708,2.730795,9.471091,-7.361930,9.036941,5.636903,-2.710320,-9.262899,4.382239,-5.974670],[0.164285,1.698490,0.464825,9.079809,7.673704,9.487926,1.078463,0.936819,-0.247608,-4.410035],[4.775236,0.032371,-5.765986,1.919939,8.739877,-9.749388,-1.975187,-3.082277,6.193563,-9.960880],[4.528746,-9.601831,2.023866,7.017847,2.373965,7.747264,-3.586765,-4.295544,1.625619,-3.551871],[6.671511,2.053451,-0.020004,-8.404701,7.767294,9.642134,-5.234573,7.690428,3.961576,-7.724229],[-6.074181,2.975513,-9.407219,1.810972,2.044052,-8.986598,-0.972257,-4.149711,-9.234359,-1.804100],[-3.262970,-5.776349,6.517075,-6.264091,8.711428,-5.935926,-4.899793,-5.775766,2.118061,-0.060030],[1.057460,-8.327660,-3.638443,4.031181,7.239637,-7.272559,0.786427,-0.416227,-0.799356,0.726521],[0.758779,5.109786,5.838085,-8.601596,-6.359110,1.176721,-8.895543,1.028644,9.507763,1.476783],[1.727508,-7.619461,-4.642691,1.869539,9.692354,-3.205570,-9.919292,-2.822710,9.324097,8.836485],[-5.798783,-0.152055,-7.397754,1.014141,-5.622725,-7.205266,1.767923,-1.141555,0.449402,-9.322394]],[[-8.415663,-6.274564,6.583177,-3.762567,7.948113,-9.505482,-9.928940,-6.451689,-7.805370,-9.496829],[-7.789427,-6.955066,2.417179,-5.042264,1.762341,0.248836,0.167965,-9.934309,3.868876,-6.451915],[-6.732635,-7.790867,0.282063,9.981372,-9.937860,-2.296641,-3.193718,-1.869233,8.210518,6.556164],[-0.984027,-6.538131,-7.055357,-4.406427,1.585182,-6.041441,4.592657,-3.625883,-7.284968,-0.028548],[-4.543611,9.483228,-0.969591,-1.937299,-5.387790,-3.166165,4.072682,5.125521,7.219926,6.107545],[-7.039376,9.506386,-3.367017,-6.218592,5.244948,8.206092,4.115883,4.542009,0.835949,8.744528],[3.991306,-6.074477,-1.269660,-4.441619,1.910562,-6.071804,7.716684,6.333817,3.577329,-1.054915],[-4.880116,-8.626528,5.319498,3.623700,-1.840837,-5.159976,-4.633179,-6.104476,-8.178785,6.845782],[-4.989591,5.597785,5.076229,8.113762,-5.096339,1.235244,7.333337,-4.477747,3.965645,3.356338],[-5.271514,0.259862,-9.372896,1.423394,-9.417379,-2.330921,-1.524305,0.441981,-2.386959,8.707246],[-5.730417,-7.669617,-2.583323,-4.863085,-8.211490,2.561572,-1.477156,-9.233385,-4.837347,5.469004],[-7.099503,8.456303,-4.206832,-8.550993,1.666361,4.875893,-8.619805,-6.665142,0.626769,6.716608],[-7.319484,-2.523264,8.993805,-8.715193,9.883758,5.793537,6.959780,-1.751665,6.054035,6.217778],[-6.264309,-2.054330,-8.720887,-6.720206,-3.537257,5.294461,-5.143064,8.177086,-8.753316,-8.208505],[5.544077,8.922206,-5.976608,-2.712722,-0.676848,5.474212,9.537755,-2.171489,-1.155270,9.887020]],[[-6.523569,2.721766,-6.843850,-0.486585,-4.407870,-9.893223,-7.632831,9.137192,-2.040265,-0.150818],[3.621735,7.491733,-4.386820,-3.486153,-5.126553,8.256454,-8.739201,-8.911002,0.938600,-0.126923],[1.104603,1.871110,-0.981720,-5.387398,3.007555,-7.828005,-2.698088,8.744250,4.309813,0.674938],[2.679224,-0.187002,-6.952148,-8.623993,8.491508,6.017472,-1.598846,2.430569,5.466904,3.810964],[-3.243657,9.060558,5.104459,9.503513,-7.154702,7.198552,5.226314,-9.399675,-1.874998,6.258616],[4.956343,-7.291481,-1.416456,-4.053163,5.475504,-9.499795,9.322285,2.166933,-0.771736,4.949740],[0.781976,-9.376487,-9.865481,-4.221786,4.320111,7.817484,1.507427,-4.568624,7.314909,8.681752],[-6.989519,-8.811628,-2.717269,1.730474,3.168704,9.045488,2.554432,2.990573,-2.995652,-5.342978],[-8.181205,-5.168857,0.864422,9.043796,-2.379863,3.323035,-6.219209,-2.011021,8.639426,1.242532],[0.542044,-0.923250,-3.526153,-5.106012,7.091301,-1.595438,-0.126373,2.111422,-1.889395,-2.082760],[-0.948644,4.783535,-4.509231,0.308409,2.395650,-3.364287,2.680422,1.742715,-1.398060,7.393405],[-8.688181,4.503579,-4.228855,-8.052760,2.276877,7.864622,2.527528,-2.978640,7.617235,1.895621],[-3.268693,0.578008,-9.793638,0.689156,-7.664133,8.001297,7.753021,-4.964912,1.681252,-5.203375],[2.881900,-1.353567,-8.657374,-2.971280,-9.416817,6.601437,0.039040,4.014402,6.603470,5.523076],[4.919128,5.977196,1.926661,-4.735573,-1.931952,-0.167436,0.592663,-9.075791,4.620456,6.883967]],[[7.190147,8.264860,8.052589,-3.466067,1.248530,-6.132317,-3.545327,3.096796,6.995091,1.803395],[-4.398919,-5.998159,-5.643067,-5.994747,9.104469,-6.146040,-6.123900,-4.269768,-2.013725,-6.752023],[-6.169348,-1.753695,-1.273803,-4.579379,7.635644,-8.445644,1.307088,9.832391,2.913265,-2.044141],[1.857790,9.023932,-3.582582,3.105562,3.025946,-4.519423,5.070089,-2.262666,2.096533,7.863753],[-2.979695,-0.088816,-5.034293,-0.456364,1.676580,3.714787,4.103538,-1.636590,-0.625114,-0.682780],[-9.166161,4.317082,9.405530,6.457572,-7.425845,5.987985,-0.541915,4.920830,-7.395889,1.993986],[-3.866734,-7.933200,4.082596,3.013512,6.248173,7.442326,-1.398861,3.107015,9.650784,-2.572395],[8.010990,-9.534976,-7.616815,5.483146,7.635495,-9.595578,4.249483,7.317537,-9.168326,-9.832040],[-8.983449,9.544801,-9.435365,-8.712156,1.195002,1.890193,4.577038,2.914352,2.647874,-1.102154],[3.586915,-6.012793,1.120437,3.866786,-8.116613,9.082056,-6.502049,-0.428400,4.269704,-3.842180],[1.279111,-6.518881,7.885521,-8.793782,-5.290231,-0.456872,-9.091315,-3.852031,-3.435827,9.744762],[0.970467,-1.635567,7.865941,-4.262247,0.900084,6.954177,-2.404343,9.955043,3.066267,9.657320],[-1.607826,4.725819,-5.252643,7.263055,-0.757572,-5.258117,1.735580,4.349141,8.276482,-9.696750],[-0.585087,4.431422,1.447017,-1.283974,8.859907,-5.659150,6.971559,-3.375722,3.177191,4.216104],[-8.210120,4.870056,-0.878868,-4.773695,-9.091957,-7.400584,-0.660052,8.929949,5.288876,3.457202]],[[8.607187,-3.403260,1.984047,0.243391,-2.762465,-7.328431,-7.649786,2.641762,-4.887369,-0.081454],[-6.970463,4.018790,-0.168480,-9.099759,9.760254,-1.010422,6.551745,2.763659,1.493536,1.525450],[3.488393,-8.940840,7.503790,-7.641793,1.010089,-1.291471,-3.141071,1.946543,-9.147853,-7.369655],[2.417493,8.540516,9.229086,3.070092,4.382093,8.131721,3.908950,-9.065410,6.453223,-2.971002],[1.176647,-4.703439,0.475549,-7.479035,6.455717,0.725975,-4.022917,5.382487,8.976263,-3.516718],[8.514337,-5.646356,-3.690676,0.516664,9.941373,-5.503285,-8.871855,-2.621498,-2.016782,3.516178],[7.177698,-3.281175,8.395044,-2.015865,9.497555,2.246708,-3.232996,9.317191,-8.737019,-4.379892],[-7.611029,-3.125238,5.402387,-6.694335,-4.670613,9.113055,-6.866005,5.476884,9.435540,3.871644],[-5.193113,2.935025,-4.043976,9.221495,6.696868,-3.070041,1.015371,-7.509267,-9.584259,-7.673428],[-6.391205,-7.600919,-8.606966,2.083031,3.852194,-9.276169,0.510336,-5.329614,-2.979287,8.450587],[1.665935,7.750602,-1.100976,3.842094,0.116078,5.944733,4.266751,-4.120116,7.480103,9.064590],[-3.681770,8.194432,7.338779,9.623677,0.913808,4.960195,1.391772,6.825023,-6.956698,-8.409049],[2.765789,-4.532026,5.849027,-1.075964,-6.144378,-2.028009,3.217956,-0.854336,3.929139,-0.300634],[-6.974002,-3.700139,-4.782427,-2.979700,-4.637809,-8.972142,-7.730926,8.704647,-0.331892,9.305598],[7.347280,6.684396,0.918379,-9.922412,-7.450785,2.642477,-8.553277,-2.773969,-6.439925,-3.248498]]], dtype = "float64")#candidate|2606|(15, 15, 10)|const|float64
uop_2607 = relay.sinh(const_2606.astype('float64')) # shape=(15, 15, 10)
func_2037_call = mod.get_global_var('func_2037')
func_2040_call = mutated_mod.get_global_var('func_2040')
var_2617 = relay.var("var_2617", dtype = "float32", shape = (288,))#candidate|2617|(288,)|var|float32
const_2618 = relay.const([[-7.465190,-2.956789,5.337261,-4.236737,4.659693,3.018750,1.594636,9.787076,-3.434569,-6.121158,0.252838,-1.523277,-0.569966,-7.590573,9.533834,2.795171,-0.591451,0.678322,6.616798,-1.485005,-7.650301,9.712253,-1.739672,-8.252849,6.492906,6.143586,9.419000,-6.989460,4.268018,-8.691590,4.346862,7.411461,2.657114,5.062519,-1.075996,0.438193,2.906873,6.398875,-1.698313,-9.506532,-7.584932,-7.029494,-1.751644,7.273270,-4.352612,-3.857495,-6.964196,6.029578,-7.027298,-0.070893,-7.647803,-6.224218,-1.129614,1.955876,8.073007,1.229974,-8.263215,-2.984469,-1.721910,-4.235362,1.096134,-8.584140,-6.579189,-3.633424,0.019511,-5.923453,-8.403619,8.206668,-5.670017,0.515017,3.665815,8.902536,2.901125,-7.394017,9.254291,-0.653833,2.251612,-8.939834,-1.084445,-6.689207,-3.872878,4.550513,3.315685,6.219805,-7.184658,-1.191738,6.904850,8.985580,1.970198,-5.467600,-8.472791,5.350382,-7.420993,-2.788494,-0.727384,-6.601928,8.333475,-9.482121,-9.702704,-6.178420,-6.742637,-1.035015,-6.128323,-3.895936,0.383405,-0.250113,0.717153,2.275343,-2.748337,-9.158828,0.602540,2.544692,8.247558,5.278692,4.142810,-9.225787,-6.522285,-2.442146,-7.535826,-0.415096,6.979314,3.389845,4.732569,-4.356627,-5.569407,-9.976634,8.207114,-4.532029,3.646467,2.031671,9.572337,8.156534,-6.768976,-6.710550,-8.684934,3.661630,-2.897110,6.357920,3.629085,9.502687,-5.614850,9.905112,7.585489,-7.488578,-2.911383,8.807574,4.121853,3.504262,-5.755673,-1.665095,5.024437,1.991272,3.033086,1.049312,-6.135549,-0.490082],[-7.045508,3.710074,-2.962538,0.894035,5.401818,-4.159830,9.360565,-7.938510,-4.066402,-4.772436,-5.260412,9.098305,-7.738834,0.046477,1.796769,-8.651732,6.244681,8.023970,8.267475,-6.930720,6.648731,-5.318409,1.068520,1.379184,1.291511,0.845365,7.288483,8.327652,5.340060,-1.185831,4.606975,-6.686629,-5.473086,-6.405482,-1.908925,-7.445049,0.284004,-3.964667,-2.354979,-9.098607,-7.552689,3.468031,-4.615413,5.496176,1.233920,-5.550786,-8.233205,-1.549403,-0.465955,7.342281,9.401509,6.919920,-7.846151,6.693155,7.197184,-1.361342,3.780803,4.316535,4.513264,1.572160,-3.195455,4.199285,4.670627,-8.483914,-5.479085,-5.989214,4.158874,-3.217946,-5.227563,-7.718668,-7.740600,1.624082,5.649953,2.755145,3.172917,4.405555,5.571652,9.836899,-5.974143,-7.769150,2.946246,0.137094,-5.399744,-7.875805,8.981701,-0.932326,6.957400,-3.859089,-5.531161,3.031736,-1.305014,-5.888095,8.731111,-3.504535,7.845108,-7.105612,-3.792195,0.819807,-3.079325,2.111707,4.878576,7.945703,4.294490,0.934020,6.748126,4.052377,0.339620,8.464122,8.655229,3.313741,5.002951,3.925067,4.709595,-0.450032,-8.159431,0.043224,-7.485339,3.938521,-1.678910,1.030586,7.969231,-3.962998,-1.925900,-9.028139,9.217991,-9.253910,0.539412,-5.530971,2.663607,-9.944353,-9.071148,3.435159,-1.223685,-3.750668,9.498808,2.111567,2.184725,2.807419,8.358309,4.962855,7.748840,5.290438,-8.091027,1.076806,3.659260,9.512594,-8.409925,-7.985413,7.566394,1.060939,-2.932446,-6.681110,-3.646970,-9.676099,1.861318,4.426187],[2.301897,0.969188,-8.605042,4.449898,4.678016,-4.841404,3.117093,-9.936989,0.872208,0.740294,-8.480155,6.896560,-8.353455,5.141782,-0.266178,-1.021828,2.887105,8.950270,2.426832,3.375475,2.588089,-5.597548,-0.995502,-4.141101,-8.388995,-8.086331,5.420601,-3.183212,6.416936,3.694502,-3.378551,4.919092,2.526825,6.849894,-0.325052,6.854256,-8.545511,-6.851605,2.123601,1.437808,2.258005,-3.618448,0.046825,-1.931518,-0.601956,-9.501232,8.557084,5.667673,-8.446810,6.790013,8.752481,6.233764,-7.083166,7.684286,-2.017384,-9.469703,-8.273385,-9.747129,8.307260,-2.293864,-4.786959,-7.718215,-4.224688,-1.566935,-9.914367,2.822209,1.634971,-7.820431,1.459957,5.368606,-7.428357,2.101604,-9.821311,-6.605217,-9.688451,-3.593387,-0.380938,-7.598310,-0.623799,6.556608,6.465205,-7.839029,2.810088,-2.437509,-0.670773,-0.741431,4.493266,3.964889,4.827978,3.713109,-4.654220,-3.222187,-5.988737,-9.790977,-4.289819,-4.859988,-9.175868,-7.342553,1.956061,-9.463334,-4.711755,-1.567262,-8.246548,5.570884,9.117697,5.618102,-2.175081,-9.996730,3.690508,4.508950,5.406863,8.512149,3.420674,4.738018,-1.353827,-0.280627,6.775216,5.565716,2.212991,3.787854,0.012634,-6.744667,4.491292,0.039001,5.154974,-7.749195,-1.592258,9.337823,3.636920,-4.479166,-6.841183,-3.223271,7.581489,-6.110882,-5.871415,9.113011,-4.959695,-7.996140,4.312080,-1.707464,-0.620345,7.140157,-1.306235,-2.051172,5.376513,-8.090344,-5.168519,6.180774,-4.417070,-2.245888,-3.362178,-0.390709,2.851698,-6.124835,-4.098387,-9.624772]], dtype = "float32")#candidate|2618|(3, 156)|const|float32
call_2616 = relay.TupleGetItem(func_2037_call(relay.reshape(var_2617.astype('float32'), [3, 6, 16]), relay.reshape(const_2618.astype('float32'), [468,]), ), 2)
call_2619 = relay.TupleGetItem(func_2040_call(relay.reshape(var_2617.astype('float32'), [3, 6, 16]), relay.reshape(const_2618.astype('float32'), [468,]), ), 2)
output = relay.Tuple([uop_2607,call_2616,var_2617,const_2618,])
output2 = relay.Tuple([uop_2607,call_2619,var_2617,const_2618,])
func_2623 = relay.Function([var_2617,], output)
mod['func_2623'] = func_2623
mod = relay.transform.InferType()(mod)
mutated_mod['func_2623'] = func_2623
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2624 = relay.var("var_2624", dtype = "float32", shape = (288,))#candidate|2624|(288,)|var|float32
func_2623_call = mutated_mod.get_global_var('func_2623')
call_2625 = func_2623_call(var_2624)
output = call_2625
func_2626 = relay.Function([var_2624], output)
mutated_mod['func_2626'] = func_2626
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2821 = relay.const([[[-3.479154,-9.582940,-1.993443,5.771525,-5.045392,1.215493,-3.097963,-1.542377,0.995652,8.193434,-7.770844,-0.034689,-8.662886],[8.063147,9.696730,5.528927,9.529093,-7.801256,-2.074081,-4.418748,6.990173,4.139478,-4.403871,3.181116,3.665493,-5.282486],[-4.571386,-5.858530,0.606233,6.638527,4.430078,4.298472,-5.420835,-4.999298,5.000126,4.497662,-3.672490,0.976965,-5.538027],[6.602781,7.293947,4.806726,-8.438536,-6.258130,-4.737240,7.799833,3.204910,-0.277632,-3.051976,-9.599594,9.627115,4.602584],[-2.563422,-4.067387,4.745548,-5.530334,7.218980,-0.233838,-7.389492,9.577313,-3.183255,-0.553090,1.665072,7.018878,1.520131],[-4.096276,-1.326564,-2.502340,-5.839543,0.578893,-8.511774,-7.821577,-1.768021,-9.677047,7.249026,1.500947,-6.408099,6.848567]],[[-7.094369,6.240552,3.709497,-5.551713,1.951420,-8.995422,9.339705,9.460018,-2.554592,0.578521,3.394961,9.623687,8.129994],[-9.536754,-7.548260,-2.506105,1.519590,-4.368753,0.971289,-8.838311,5.485760,-1.343759,-8.040125,6.483000,3.250893,6.770000],[-8.396358,2.211714,4.200624,7.208837,-5.401338,-1.464888,0.553212,-8.374439,3.295849,-5.671670,4.127001,6.980844,-9.873172],[-4.929806,6.032132,-8.639263,-4.317384,-9.558399,-4.778627,3.673279,0.670069,-4.459290,-3.797559,4.297915,7.439858,9.251249],[-8.743278,-4.116197,7.808515,-4.158537,2.454850,-1.972233,-9.154308,4.487064,-4.096532,7.352045,0.118219,-8.733506,-3.278375],[8.727727,8.413315,6.096653,-0.115907,6.540527,-4.543337,-1.455495,-2.823511,-7.602529,4.665025,7.228607,-9.810458,6.751524]],[[-0.836500,-8.760126,7.544995,-3.910296,-6.002451,-1.074340,-1.594259,-4.721318,6.368022,-4.711570,7.064837,9.425953,-0.477613],[-2.262182,9.658688,-6.830091,4.419941,8.758027,7.729797,-5.007179,4.296647,-5.851927,-9.025342,-5.297723,6.496512,0.210605],[9.577564,-0.200211,-0.176901,9.575238,-4.037130,7.459542,-9.380945,2.033204,8.332535,0.147535,-3.649129,-6.829262,-5.426642],[0.535651,7.556147,-5.329666,5.271954,-4.088850,5.024240,3.336879,-6.145146,0.694464,7.032999,-9.361066,-0.977735,8.159621],[0.240208,7.583421,4.008140,1.991028,-8.432864,2.959862,-7.833026,8.477234,3.118695,-8.581867,0.536689,-9.345937,-2.210812],[5.944300,-0.497446,9.425906,-8.042849,0.903579,7.550556,-0.868368,-0.250312,8.908585,-9.584027,-3.837914,-2.202201,1.220046]],[[3.552078,-3.434961,-6.061828,-8.089585,8.130806,-9.386553,8.237518,9.247921,-4.487291,-3.326984,7.495257,-0.121520,-0.628282],[-8.820703,2.410778,-9.586791,6.163487,-0.284206,7.090629,8.494974,-7.861140,-4.257698,7.445554,2.932736,-0.305199,8.261424],[3.997142,5.142035,-5.633034,-8.019155,3.931828,-4.169506,-7.048090,-9.805749,-1.351380,-6.452459,1.035559,-9.691130,-6.956342],[-4.325941,8.593194,-8.518532,1.137108,-2.916503,2.425339,7.267451,1.821749,-5.953248,-8.745172,0.224122,-9.806100,-1.390990],[2.822182,-9.051746,-2.629881,-0.654325,-7.143783,-2.963055,-4.594531,-5.458762,-7.344853,-8.879055,2.082122,0.783094,4.620873],[-8.783982,-0.202787,1.132272,2.900521,5.289227,-1.594855,0.766727,-7.916934,2.331021,-2.072309,8.334069,0.704608,8.778137]],[[-7.029199,4.244298,3.715029,8.336635,-8.038658,6.121592,-0.438269,0.042282,-2.851886,-4.965951,-6.789770,9.892395,5.035831],[9.926594,-8.148157,2.080285,1.049036,-2.563256,7.809678,-4.233599,-5.393066,1.065717,-5.608070,-0.970378,-0.307465,-5.954008],[-7.640117,0.713832,-3.623145,-1.544594,8.345572,4.777374,-6.546561,-5.257393,6.752411,2.058465,-7.639326,-9.188492,7.345512],[-5.477372,9.849558,4.800542,-7.478477,2.552641,8.355312,-9.675880,-3.353036,-0.259977,5.740000,-4.051333,7.595568,4.732247],[-6.508079,7.103610,-2.188167,5.507209,-4.914400,6.995198,-0.871733,3.741155,-2.473100,-3.321973,7.781739,-1.087113,9.484722],[6.990996,-3.681101,4.886715,-2.914940,1.404274,-0.918943,2.948974,5.383021,1.442768,1.887515,7.956096,-6.162066,-5.902217]],[[-0.999334,6.908243,4.614859,1.671699,9.632434,2.439721,1.876198,-5.892590,5.731905,-0.632228,-7.092869,-2.920304,-1.924706],[3.175436,-2.819658,-1.315373,-1.259939,-4.246987,-6.551020,-2.806969,-6.693373,2.732810,-4.064923,7.651089,1.232208,-5.989797],[-8.547271,-1.967052,-5.799392,7.742383,3.987933,-5.290744,4.672254,-9.623983,-7.614794,8.642579,-1.926985,-6.409797,-2.640298],[-2.424953,6.579363,0.794850,-2.190972,-6.276380,-7.373392,3.308261,2.418215,2.082217,-6.507367,-6.514789,-3.044967,-2.553237],[-0.630939,1.910558,-4.284601,8.643271,-5.190468,7.855602,-1.822644,-0.852960,-5.475610,-9.585717,4.423858,-9.511761,5.107917],[-1.200132,0.740772,-3.313638,6.944824,-9.766676,-5.594113,4.052871,5.696352,2.310078,-5.142132,-6.043459,6.160372,-5.953568]],[[-1.548225,-5.398513,0.216942,-0.661028,1.643196,-1.259512,-7.351960,9.970783,-6.333876,-0.890442,3.785148,9.282540,3.130762],[-0.732834,7.067037,6.928341,-8.741580,3.005598,-4.203309,-5.082015,5.435594,-0.342331,1.489108,-8.521639,-0.330395,6.737769],[-7.039983,2.523844,-4.402478,-1.077012,-5.282164,-7.601019,8.649126,-6.173090,5.194798,-1.337265,3.374948,-5.725662,-2.627616],[2.390010,4.632477,-6.064227,3.567325,1.462645,-5.510937,1.936293,1.276189,8.772225,-3.356580,-7.489419,-5.840021,-9.243879],[8.032547,-6.543909,4.805244,-5.533996,4.422733,-5.484724,-3.016474,-6.218198,6.970256,9.120459,6.042714,3.370027,-7.609358],[1.545095,-4.966416,6.783428,2.289261,1.409233,1.054684,9.960205,2.575769,1.119232,-7.520968,-8.702205,-8.267525,-4.377220]],[[-1.967600,9.187239,-2.980867,5.278617,-5.056029,-4.708912,-4.899990,-0.788740,-1.731332,-0.302385,1.777302,7.957686,-6.829679],[9.286282,-0.580120,-6.748679,5.741234,7.723985,8.195977,8.593332,6.949679,7.176451,3.072672,6.258889,2.403089,6.303116],[-9.248937,-7.757921,-6.532894,0.009031,-7.943207,6.481984,3.274240,0.789358,0.607187,-5.903092,-8.413771,4.114653,9.751868],[1.491548,-5.678966,8.803735,-7.980790,7.782947,6.934583,3.412782,1.795221,4.582213,5.044734,3.441145,8.036352,-7.026132],[6.524592,-2.809598,-3.078191,5.640235,-6.470394,8.125504,2.813951,-8.475035,0.626323,-8.474359,-5.242315,7.284510,-6.026805],[6.323793,-9.726141,1.317043,7.859000,-4.326198,-6.516393,-8.601025,-4.467585,4.982591,0.869539,-2.325902,3.463216,2.365588]]], dtype = "float64")#candidate|2821|(8, 6, 13)|const|float64
const_2822 = relay.const([[[5.632219,0.565637,9.225798,-0.697229,4.670030,-2.356608,-4.185663,9.693041,-3.388152,-4.630784,2.584889,3.686596,3.477919],[-2.153501,-6.160093,6.294228,9.406800,-3.054994,0.145928,-6.363579,-6.857453,-8.022448,1.497998,-2.964102,-8.712814,2.872819],[-0.670480,9.664154,3.199721,-0.147883,1.429077,7.297629,-0.009095,-4.125762,0.640654,-9.486674,1.899319,-0.877449,-3.961328],[-0.839370,6.083452,1.638692,-7.647565,6.924378,-3.168178,-3.748116,-7.541055,6.414065,0.233862,-1.329557,-9.069976,0.761445],[7.953079,-8.957512,-7.330404,-0.768894,-2.603698,9.685303,3.765965,-7.814427,-0.106303,5.182346,-8.239864,3.668631,-6.605539],[-5.981559,-8.058424,3.533395,0.415334,8.285120,-3.357684,-7.988899,4.591096,-2.484214,-2.435713,1.644368,0.526169,3.240238]],[[9.552526,0.444722,-0.255794,-3.527369,5.966066,0.566896,4.609903,-4.259944,-7.949702,-5.593712,-3.199850,-9.340840,8.595845],[0.378048,8.670466,-9.904101,0.323228,-4.054994,-7.718480,-0.790238,-9.957798,-0.006133,1.784260,-7.663415,1.887399,7.738366],[8.738660,6.935050,6.729867,3.777368,9.779278,6.837066,4.421241,4.874790,-6.619970,-4.827326,2.511116,-1.591586,1.464661],[-4.166583,8.824185,6.151553,-3.977426,8.170529,6.706605,-0.030232,1.734585,-4.616379,5.562994,-2.329849,7.057583,1.141496],[7.770341,4.912803,-0.919510,-2.072922,-0.258930,-1.441790,-8.187636,-1.041634,-4.124783,-3.707483,3.953063,-4.433614,-5.868748],[-1.659643,9.198628,-4.148656,-7.748422,-4.636616,-9.208145,-2.383230,-8.798176,8.611236,6.472128,-5.138409,-8.519668,0.502817]],[[5.455666,-7.830567,-8.635499,-8.590294,-4.077280,-1.853531,-5.156590,6.096440,7.640645,4.088040,-3.191741,-1.699099,3.575444],[4.784187,-9.455526,5.217272,8.883739,5.362191,-5.259192,9.345289,3.052104,5.736055,-0.063347,-8.522416,3.196120,5.605905],[-8.194637,3.222148,2.714245,6.288903,5.442061,7.797628,-9.064032,-1.246521,-6.228813,-1.965190,3.355822,-0.726113,-4.038159],[-8.005476,-6.921481,-5.345597,9.308143,-7.214208,-1.174815,-2.135581,-5.941852,-5.802697,5.513552,-2.132124,1.097024,7.587966],[-2.430988,-4.565934,-9.108823,-6.531052,4.403329,5.473043,-3.748843,8.409405,1.158743,-9.664737,5.762280,-8.003087,1.236756],[2.376057,7.197916,-6.091329,-1.548075,1.878876,4.610619,3.857383,-7.048339,8.968477,0.537952,3.256283,5.764629,-9.121859]],[[0.759408,9.115382,6.395175,1.132820,0.160430,1.141625,-8.815084,-4.354800,-2.386020,-0.236252,-3.042225,-8.234133,-3.526776],[-6.419891,6.269489,1.846998,2.223911,-8.665466,8.301541,-5.797205,8.094181,-2.488235,-1.656325,9.456356,-5.746978,9.635155],[4.292725,-8.575651,1.130542,8.058751,-9.375474,6.343149,6.597350,-7.105378,9.108533,0.647135,-2.391837,7.390668,-4.937939],[-0.828886,-6.079148,5.209449,0.071006,-8.511911,-5.222128,9.409162,-1.838122,7.094940,-9.986796,-8.222947,-6.100946,-0.449621],[7.075902,2.134625,-6.832447,-8.403791,3.573377,1.770266,-8.934102,3.113890,1.743013,5.869221,-0.641375,-8.012646,-4.815431],[-2.745802,-7.331134,-7.600103,-2.327575,-8.895467,6.009087,-4.935352,-6.655549,0.453202,8.043936,-4.059089,9.124441,-9.262182]],[[-7.363159,5.383518,5.298153,1.442767,-5.127157,4.311245,0.464296,-1.263648,-1.990656,8.344781,-6.336340,4.903352,9.315026],[-4.871979,5.558492,-9.428555,8.284688,9.398416,-4.045191,2.187829,-3.219621,1.420108,-9.540664,-6.018843,-2.210585,3.968887],[-7.045670,-1.472108,-5.601287,-3.928990,9.045880,6.196850,-0.210944,0.998239,7.988301,-8.772005,5.213699,2.640782,8.441805],[3.553219,2.044228,-0.314585,3.340808,-9.274300,0.641997,-7.934878,9.018013,-0.361324,-2.227432,-8.544983,-6.654520,6.078002],[9.764782,8.637267,-6.373005,-4.369822,8.940253,9.995368,-1.121267,9.344862,-6.925357,-9.272424,3.456572,-6.577134,9.070628],[-5.984027,9.429865,5.051139,-0.297832,6.046925,7.985556,2.366138,-6.425209,-4.119795,-1.775384,-0.941995,0.941328,-4.390798]],[[2.923397,-5.069528,-2.849296,-5.946340,-6.673121,-0.543003,-7.492570,8.013751,2.307472,2.820221,0.331543,-2.918482,8.668428],[-8.005369,-5.783374,2.460343,9.766334,-5.935244,-2.069418,3.353634,-7.739646,-6.329017,9.685719,1.056863,-3.704516,-5.348090],[-8.373636,4.231416,-0.829621,-3.978588,-2.075937,-7.738064,1.702491,0.607797,-9.435544,-4.242299,-8.753410,2.411102,-9.050954],[0.039707,3.680762,-9.133907,-5.048233,9.173136,5.627949,9.198448,-2.292875,-2.346736,-7.598415,8.294819,-6.133050,-7.426470],[-0.478773,0.815042,-9.073860,7.754808,-8.172824,1.621245,1.191305,5.748419,-5.196771,2.841592,7.387639,-5.787301,0.527524],[-2.187642,9.725149,1.619971,-6.050625,-8.256438,5.646523,3.991936,2.910007,-8.179924,9.138899,2.277289,1.966915,-0.635470]],[[-6.848457,-8.291115,6.530268,-6.937187,6.824512,-0.330297,-8.600161,-4.712673,4.197794,5.323253,-3.084137,8.127673,-4.772151],[6.937584,5.865687,-5.153208,-7.342900,-9.096137,7.434428,-9.516760,-5.386822,-6.467507,9.188481,-5.221207,-8.968177,2.363502],[9.960958,8.460864,-8.432520,2.979204,-4.103338,7.365516,3.210134,-0.153368,-7.715013,6.300712,-3.468654,8.025605,0.983085],[-1.694674,-4.797015,-6.572780,-9.729280,3.939000,5.812318,2.649735,-2.255556,-8.229991,-8.851011,-0.317480,-8.567136,4.444145],[0.409502,-6.144221,-4.136537,4.872967,2.346624,-9.677761,7.598168,-8.586512,0.876178,-3.388036,-5.725529,8.935924,-9.051449],[-4.879774,9.180902,4.861688,-3.712768,8.413224,-7.572866,1.276731,5.732161,0.464228,4.761278,7.887142,7.547801,-0.829332]],[[-3.948790,-2.109143,2.472191,3.230878,-2.642995,-1.290215,0.329539,4.942803,-2.184961,5.231217,8.358759,-4.598479,-7.011715],[5.132380,4.072337,1.941040,8.505944,-5.650312,-9.365086,8.630270,-2.421286,-8.001186,-0.978236,5.505276,-2.195004,-6.630600],[-1.338557,1.710543,-0.185915,-0.858921,-8.222470,8.158738,-4.364255,6.042602,-4.656149,3.319276,-2.780681,-8.269191,-6.708313],[7.292844,-9.266476,-2.323246,-0.490650,1.518266,-0.644292,-5.336168,7.172702,-7.491912,-4.438739,7.237442,-9.343059,2.995900],[-0.017980,2.872607,-4.797778,3.187321,-8.999228,9.059717,7.345557,8.343259,-8.810257,3.380781,-5.502603,6.673784,5.611927],[4.015110,-0.439340,-4.661106,-7.640891,2.172865,-9.416895,3.869909,-5.335335,1.797701,4.438127,1.361323,-4.654883,1.839193]]], dtype = "float64")#candidate|2822|(8, 6, 13)|const|float64
bop_2823 = relay.mod(const_2821.astype('float64'), relay.reshape(const_2822.astype('float64'), relay.shape_of(const_2821))) # shape=(8, 6, 13)
uop_2830 = relay.acosh(bop_2823.astype('float32')) # shape=(8, 6, 13)
func_2037_call = mod.get_global_var('func_2037')
func_2040_call = mutated_mod.get_global_var('func_2040')
const_2843 = relay.const([9.630167,-9.622855,-2.721113,1.141714,0.978025,-4.615209,-7.897713,3.837349,-0.156175,4.002868,-7.422094,-9.707622,8.009986,-9.946131,-0.751457,-4.948761,3.216897,-7.016621,8.143351,-1.976236,-3.417762,2.796287,-3.878406,-9.994257,0.170431,-2.856503,-5.519489,1.376133,-6.294772,-8.149099,5.429049,5.048037,8.189802,9.477525,9.763727,5.844427,-8.026032,-3.757367,-1.433567,-5.896978,-0.312338,0.284711,4.325408,0.671234,-3.330976,3.854675,-2.983020,-1.673341,-2.608265,-6.514723,-1.468505,9.182344,0.415698,2.781486,1.439628,1.336576,-3.526063,-0.724125,9.051423,-2.636171,1.680580,1.166694,-0.799903,4.641688,7.935170,-6.056542,6.922596,6.781573,3.432177,-9.987564,-7.943663,-0.701904,4.636029,-1.750464,-0.186336,-5.811345,-2.233641,-0.772724,-9.469344,3.595226,7.177305,6.237595,-6.537629,7.894885,5.782792,-4.531475,9.488186,0.426525,8.784709,4.092724,-6.905487,1.356217,-9.240927,6.569564,0.499435,-8.923983,-1.253813,9.384269,-1.187466,-1.237593,8.175572,4.804064,4.732978,8.170002,0.569342,3.164811,-1.803545,-7.642190,-1.856963,4.003231,1.611096,-4.741922,3.753952,-1.453761,0.120333,-6.712445,3.990643,9.601611,-2.647961,1.976010,-9.806517,7.802791,7.935962,9.873660,0.670559,5.153246,-3.599146,-3.503175,0.809374,-6.167689,3.234356,9.715065,-1.328821,4.376478,1.735563,-9.224333,7.177984,2.905796,-0.694411,-6.136874,0.195672,-8.448182,-5.257308,-8.276681,1.219721,-2.676271,0.452199,6.928738,-3.210764,-6.624347,6.934849,9.555674,-6.074941,3.172873,9.848804,-0.353077,4.142499,3.519340,0.862286,3.114524,-5.499998,5.667031,-1.865645,8.186740,5.258108,-9.579895,8.045722,-2.776398,-6.531551,-9.552009,9.166269,4.049028,8.648845,-9.542475,-4.626334,5.241197,4.204936,-1.775628,3.238483,8.008203,3.974499,2.742439,5.268643,-3.916373,2.549715,-6.343146,5.111998,2.487424,-9.084132,8.976596,8.087972,3.953991,2.741437,-1.886741,0.019096,0.783312,-3.207425,4.676017,-9.524417,0.360803,-1.051508,7.075889,9.985565,-9.930213,-7.963380,-6.682774,-0.738273,5.707010,7.788533,-0.643126,1.868076,8.663550,-6.901539,9.938794,-9.000956,-2.774320,-6.775867,-4.602663,-7.571870,0.870450,-6.463971,3.550926,9.126008,-8.856182,-4.811005,-5.907017,8.549097,2.313847,-4.413380,-1.659858,-8.801233,-0.370221,-4.524982,-5.695277,4.391266,-8.670877,-3.202921,9.572795,-1.523127,-0.968810,-7.083803,-7.564951,3.881649,-2.443359,-6.280912,-8.076810,3.433720,-6.092513,-2.930411,0.604531,-7.407605,7.204803,5.799658,1.634463,7.634986,-7.039490,-2.841824,8.678599,0.253767,3.432059,-8.305718,-8.455700,-4.011815,-6.333154,2.019912,8.974750,4.866934,-8.140172,7.584543,-4.393366,-3.490819,-4.649289,8.360819,-9.985516,3.987893,-9.220664,2.964791,-0.365979,4.113182,-8.106037,-6.478084,5.661954,9.803866,-5.139330,5.396356,6.065195,9.427019,-3.324660], dtype = "float32")#candidate|2843|(288,)|const|float32
const_2844 = relay.const([-9.862698,-9.650984,-1.408862,-9.594736,1.622373,7.448939,-1.565404,3.142590,-2.945436,-5.362069,-4.886728,1.759863,0.221666,-8.660507,-8.115578,-9.901449,-0.478763,6.675840,5.919457,-3.989931,-0.643701,-3.196588,-7.965713,-9.670609,6.324139,-1.074852,-1.516473,4.922854,9.317654,-0.870575,-2.381493,7.363131,-2.201169,0.665688,-6.333729,-9.815513,4.887938,5.450163,5.266422,7.623959,-8.515606,-2.590385,9.564924,-3.142193,-1.738122,5.199668,4.917003,3.663740,3.529333,1.893360,-5.061151,-0.265069,-7.035740,-6.941239,-6.587067,-3.117177,9.252114,3.038991,9.101568,-6.486269,1.527985,-9.849763,-5.870685,-8.291324,-7.452730,2.069030,9.118319,1.856367,4.475404,2.332780,9.630467,-0.032973,7.633719,7.025052,0.137374,-6.526595,4.425800,-0.954084,-2.808345,0.367509,-5.966642,7.235071,1.226839,-0.318355,-5.009486,-9.650668,0.984741,4.268991,-6.162451,0.276869,-4.805049,-9.476668,-5.922730,1.989266,6.453670,-4.325866,0.598029,-7.092829,-7.124269,5.470088,-0.368311,-8.903954,-0.467412,-3.958815,-8.299866,-4.642706,8.648785,2.647340,1.981376,-8.033311,3.613203,0.879328,9.978641,6.906659,-6.140325,-2.032561,-2.188741,-3.037434,-8.051231,-1.053416,7.827304,5.677233,2.484230,-8.273723,4.241225,-5.030641,9.957785,6.541474,2.548057,-9.698686,9.419224,-9.198052,8.462149,-0.624566,-4.606856,9.237379,-1.049297,-3.245498,5.423945,-6.044695,-1.711408,8.649823,-2.460044,-0.755912,-1.673536,5.442004,8.906514,3.328643,8.037547,7.072633,-2.904056,9.403945,9.483968,9.952038,-4.886382,-3.558874,-8.331009,2.389936,-7.456787,-1.489905,-3.699707,8.496794,9.775182,8.315687,-6.522429,-7.680336,0.427459,0.160745,-1.274656,7.645510,6.695361,9.324763,7.461644,-6.380295,-7.655566,-1.396803,2.004901,-9.962873,1.320979,9.496488,-4.929943,-5.950823,8.432473,9.010141,-1.557955,-8.020368,-3.955166,2.305130,-0.112404,3.103841,-3.339033,-8.252803,1.672727,0.728831,-0.815613,3.719219,-1.601020,-9.830213,6.881721,4.973001,-3.751644,0.065169,3.672418,-1.642988,0.824869,-4.289055,-9.592137,1.077619,-6.578641,-2.733126,1.940198,9.003482,3.669191,1.885313,8.787621,8.348991,-4.342458,-4.295125,5.023560,-1.237818,5.736802,7.209428,1.859345,6.491852,3.941164,-2.515331,4.640453,-4.240250,1.769639,-2.047294,6.837706,-0.837133,-3.800885,0.476446,7.391056,-4.234773,3.292513,-2.658534,-4.725475,-4.542850,8.546615,-0.967544,-8.410334,-5.960445,-2.065276,8.674329,-0.717528,-7.445781,-2.946184,-2.191690,2.986977,-5.318858,-0.152628,4.196140,0.515033,-8.402044,-1.946816,7.216695,-4.864470,-5.324371,-7.714953,-8.338546,0.868821,-7.883677,-0.244331,2.580694,5.723083,-8.306627,5.262406,6.009301,4.291468,6.711036,-6.765176,3.044519,-6.567067,-9.664190,8.088537,9.236540,8.605732,-0.280535,0.299817,4.941134,-1.858157,-4.846664,4.929892,-3.283254,-1.849672,-2.150237,-4.018244,1.310011,5.549448,-8.469630,-1.447930,7.074230,4.871314,0.786558,8.211817,6.703487,9.920484,2.122171,4.223306,8.887969,-9.509124,6.973705,4.615537,9.336594,-2.117773,4.843986,-5.421615,-8.402129,4.499400,-1.453472,-6.613089,-8.138873,2.512959,-2.647404,8.435112,-4.259237,7.354054,-1.257958,-4.315548,0.778892,5.835367,7.854426,1.896909,0.842146,-7.670112,9.419192,-4.817832,-3.775786,-2.012805,-7.148929,-3.916839,6.930285,-1.218282,1.253785,4.463003,2.820513,1.482401,-9.658698,-3.640039,6.239635,4.886051,7.131995,-4.852947,-2.058517,-4.231031,-4.722454,4.326055,-2.336313,-4.942755,9.376424,-9.519506,-9.264241,6.476780,-2.009262,4.503071,-2.036339,1.146611,-1.390929,8.324010,-1.217715,0.998236,8.978407,-2.872283,4.135273,5.710784,-0.017979,3.646585,6.225132,-7.145957,9.322247,-6.664333,-3.068371,9.585365,3.882602,4.154088,1.466384,6.913242,-3.291544,-7.170892,-6.834662,-6.139988,-3.887979,8.433039,-1.314457,1.653023,9.934023,-7.794174,3.823263,-2.043728,-7.074192,-5.148367,2.016958,-2.918563,8.136735,7.224666,-3.923510,4.815594,0.066727,3.819986,-7.308116,9.308807,-6.106406,9.887218,-0.943723,-5.788043,-6.122002,-9.744456,-0.576731,1.555441,7.977849,3.356413,-1.310455,-8.324380,-8.309037,0.955215,9.330892,-9.245373,-6.189624,7.245450,-2.405175,-6.191229,2.904422,-4.094637,2.375794,0.754901,-7.322560,9.397213,4.701807,-9.652024,6.421687,-0.119723,9.173209,-3.532021,1.677876,-4.705989,2.360509,-1.480228,3.780196,4.636783,-6.004009,5.175635,2.290855,2.896972,6.532094,-2.058570,3.772882,9.496941,-4.775830,0.746134,0.566028,7.065101,-9.115060,6.227577,-4.475967,-9.259881,-3.791223,5.864743,-3.224155,-8.767106,-9.088418,-5.837774,-0.868465,-2.399963,1.388124,-8.786846,0.416219], dtype = "float32")#candidate|2844|(468,)|const|float32
call_2842 = relay.TupleGetItem(func_2037_call(relay.reshape(const_2843.astype('float32'), [3, 6, 16]), relay.reshape(const_2844.astype('float32'), [468,]), ), 2)
call_2845 = relay.TupleGetItem(func_2040_call(relay.reshape(const_2843.astype('float32'), [3, 6, 16]), relay.reshape(const_2844.astype('float32'), [468,]), ), 2)
uop_2875 = relay.cosh(const_2821.astype('float64')) # shape=(8, 6, 13)
uop_2880 = relay.sin(const_2844.astype('float32')) # shape=(468,)
bop_2893 = relay.logical_or(uop_2830.astype('bool'), relay.reshape(uop_2875.astype('bool'), relay.shape_of(uop_2830))) # shape=(8, 6, 13)
output = relay.Tuple([call_2842,const_2843,uop_2880,bop_2893,])
output2 = relay.Tuple([call_2845,const_2843,uop_2880,bop_2893,])
func_2899 = relay.Function([], output)
mod['func_2899'] = func_2899
mod = relay.transform.InferType()(mod)
output = func_2899()
func_2900 = relay.Function([], output)
mutated_mod['func_2900'] = func_2900
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2899_call = mod.get_global_var('func_2899')
func_2900_call = mutated_mod.get_global_var('func_2900')
call_2901 = relay.TupleGetItem(func_2899_call(), 1)
call_2902 = relay.TupleGetItem(func_2900_call(), 1)
output = relay.Tuple([call_2901,])
output2 = relay.Tuple([call_2902,])
func_2921 = relay.Function([], output)
mod['func_2921'] = func_2921
mod = relay.transform.InferType()(mod)
mutated_mod['func_2921'] = func_2921
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2921_call = mutated_mod.get_global_var('func_2921')
call_2922 = func_2921_call()
output = call_2922
func_2923 = relay.Function([], output)
mutated_mod['func_2923'] = func_2923
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2899_call = mod.get_global_var('func_2899')
func_2900_call = mutated_mod.get_global_var('func_2900')
call_2943 = relay.TupleGetItem(func_2899_call(), 2)
call_2944 = relay.TupleGetItem(func_2900_call(), 2)
output = relay.Tuple([call_2943,])
output2 = relay.Tuple([call_2944,])
func_2967 = relay.Function([], output)
mod['func_2967'] = func_2967
mod = relay.transform.InferType()(mod)
output = func_2967()
func_2968 = relay.Function([], output)
mutated_mod['func_2968'] = func_2968
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2921_call = mod.get_global_var('func_2921')
func_2923_call = mutated_mod.get_global_var('func_2923')
call_3089 = relay.TupleGetItem(func_2921_call(), 0)
call_3090 = relay.TupleGetItem(func_2923_call(), 0)
func_7_call = mod.get_global_var('func_7')
func_11_call = mutated_mod.get_global_var('func_11')
var_3094 = relay.var("var_3094", dtype = "float32", shape = (234, 2))#candidate|3094|(234, 2)|var|float32
call_3093 = relay.TupleGetItem(func_7_call(relay.reshape(var_3094.astype('float32'), [12, 13, 3]), relay.reshape(var_3094.astype('float32'), [12, 13, 3]), ), 0)
call_3095 = relay.TupleGetItem(func_11_call(relay.reshape(var_3094.astype('float32'), [12, 13, 3]), relay.reshape(var_3094.astype('float32'), [12, 13, 3]), ), 0)
bop_3119 = relay.not_equal(var_3094.astype('bool'), relay.reshape(call_3093.astype('bool'), relay.shape_of(var_3094))) # shape=(234, 2)
bop_3122 = relay.not_equal(var_3094.astype('bool'), relay.reshape(call_3095.astype('bool'), relay.shape_of(var_3094))) # shape=(234, 2)
func_2967_call = mod.get_global_var('func_2967')
func_2968_call = mutated_mod.get_global_var('func_2968')
call_3134 = relay.TupleGetItem(func_2967_call(), 0)
call_3135 = relay.TupleGetItem(func_2968_call(), 0)
func_568_call = mod.get_global_var('func_568')
func_572_call = mutated_mod.get_global_var('func_572')
const_3138 = relay.const([8.757310,2.719334,-8.563249,-1.226994,-5.443115,-6.254592,-6.800398,9.929582,-7.177908,-6.833443,-5.222315,5.895697,-1.646703,-7.689787,-4.350228,9.951622,2.386613,4.152936,-4.843749,0.110374,-3.465514,2.759568,1.801304,-4.326238,-3.484357,1.613115,-8.846193,3.719558,7.675159,7.833549,0.159021,-5.008685,9.665755,-6.552116,6.827621,-3.200808,4.274083,-9.591048,7.829471,-6.144074,6.758882,-1.626979,-5.541386,-1.118800,4.669429,9.013356,-2.085894,-2.901459,-3.134008,-8.484040,-9.214927,3.692725,-6.182246,-9.207570,-9.515668,9.224366,-9.310105,-9.422095,5.985922,7.004391,-5.296701,9.832514,-3.585495,-9.426088,-2.826519,-6.349920,8.056086,-4.412262,8.956427,8.833067,7.119852,2.624969,-4.022196,1.046654,7.050284,5.347950,0.248660,-8.233198,-9.598870,-6.660611,5.301899,6.581868,2.232173,-3.235063,-4.676253,-0.364750,1.327729,-8.177255,3.291141,5.838245,-7.782278,-1.617312,-7.040034,1.755002,8.978873,9.365463,-2.921708,-5.988476,3.582367,-6.486983,-1.185654,4.466333,-5.618284,-2.194356,9.301500,-6.129972,-3.212223,-0.560175,-7.493018,0.035022,0.310642,-3.176073,0.848285,5.314510,-0.002546,-2.199044,3.136003,-6.728417,7.046313,3.404303,-6.573586,-8.170489,0.191729,4.827884,-9.622462,4.715861,-0.817464,8.101916,-9.501794,-1.834444,-3.660451,-3.380210,-1.106958,-0.138397,2.573067,9.654730,0.412593,-9.503370,-7.081370,-3.430901,-5.286550,-1.923110,-8.592930,-4.823863,8.267011,6.568868,6.733900,7.611228,-9.974896,-7.128043,9.027766,7.404564,8.952887,6.323889,-4.006040,6.436857,-5.854615,8.604481,3.358815,6.024562,-4.138066,3.826848,-2.062979,6.290589,-1.732145,-0.763169,7.194759,-8.942885,8.531545,-1.889928,-5.400881,-0.694376,-4.926480,2.854027,2.915289,-9.502001,1.544857,-2.868599,-5.279124,-0.325718,6.433126,-4.605891,-5.539776,8.847545,6.241064,8.289881,6.768234,-1.054255,0.741405,-3.327342,-9.113121,-0.929649,-1.671268,-2.562176,0.224257,7.964989,0.835045,2.992059,-9.163206,-5.845708,9.575536,4.559701,6.368515,-7.928623,3.937353,-6.362181,0.091099,5.897363,5.078580,-8.873990,-5.419500,2.741748,8.688080,-9.183799,6.180911,9.795852,-8.506085,-8.260243,-5.113423,0.270105,8.479691,-3.362784,-4.301861,-4.865402,3.476278,-3.968782,-3.978020,1.027417,8.138774,4.461237,-7.559107,9.615967,-5.842291,6.959927,-9.123429,-6.130817,-5.853367,-1.028123,8.136589,-2.125404,9.048988,-0.851456,-8.489261,2.949132,5.720524,-2.795985,-8.180394,2.056064,6.558984,0.431588,7.060905,7.947489,-6.351950,-1.988851,-7.852522,-5.775881,-4.785152,2.385242,1.686690,-9.967105,-9.553650,-9.761224,-8.646149,3.106109,-8.199503,5.919636,-5.509302,7.336923,-4.450560,-4.334154,-2.584160,-2.114341,-9.098216,2.012656,-3.034609,-4.892485,3.007044,6.525132,-8.695378,1.019109,-9.613639,-4.774756,-9.838386,5.117853,-8.725431,0.848057,5.617602,6.078326,-6.034013,3.079940,-2.833594,1.602262,-9.236932,5.841861,8.316715,-1.260071,7.942584,-0.308566,-1.838016,-0.435905,-8.997054,-1.121333,3.020494,1.482477,-6.187780,-8.566461,-8.501029,-0.680604,0.127193,-4.559093,0.631680,-4.334070,4.317199,-6.538540,-9.027446], dtype = "float64")#candidate|3138|(315,)|const|float64
call_3137 = relay.TupleGetItem(func_568_call(relay.reshape(const_3138.astype('float64'), [3, 7, 15]), relay.reshape(const_3138.astype('float64'), [3, 7, 15]), ), 0)
call_3139 = relay.TupleGetItem(func_572_call(relay.reshape(const_3138.astype('float64'), [3, 7, 15]), relay.reshape(const_3138.astype('float64'), [3, 7, 15]), ), 0)
func_2967_call = mod.get_global_var('func_2967')
func_2968_call = mutated_mod.get_global_var('func_2968')
call_3140 = relay.TupleGetItem(func_2967_call(), 0)
call_3141 = relay.TupleGetItem(func_2968_call(), 0)
func_371_call = mod.get_global_var('func_371')
func_374_call = mutated_mod.get_global_var('func_374')
const_3143 = relay.const([True,False,False,False,False,False,True,True,True,False,True,True,False,True,False,True,True,True,True,False,False,False,True,True,False,True,True,False,False,True,True,True,False,True,True,False,True,True,False,False,True,True,True,True,False,False,True,True,True,False,True,True,True,True,True,True,False,False,True,False,True,False,False,True,False,True,False,True,False,False,False,False,True,True,True,False,True,False,True,True,True,True,False,False,False,True,True,False,True,False,False,True,True,False,False,True,False,False,False,False,False,False,False,False,False,False,False,True,False,True,False,True,False,True,True,False,False,False,False,False,True,True,True,False,True,True,True,True,False,True,False,False,False,False,False,False,False,False,True,True,False,False,False,False,True,False,True,True,False,True,True,True,False,False,True,False,False,False,True,False,False,True,False,False,False,True,False,False,True,True,True,True,True,False,False,False,False,True,False,False,False,True,False,True,False,True,True,False,False,False,False,False,False,False,False,False,True,False,False,True,True,False,False,True,False,False,True,False,True,True,False,False,True,False,True,True,False,False,True,False,False,True,False,False,True,False,False,True,False,True,False,True,True,False,False,True,True,False,True,False,True,True,False,False,False,True,True,False,True,False,False,False,True,False,False,True,False,True,False,False,False,False,True,True,False,False,False,True,False,True,False,True,False,False,False,False,False,True,False,True,False,False,True,True,False,False,False,False,True,False,False,True,False,False,False,True,False,False,False,False,True,False,True,True,True,True,False,True,True,False,False,True,True,False,False,True,False,True,False,True,True,False,False,False,False,False,True,False,False,True,False,True,False,False,False,True,True,False,False,False,True,False,True,False,False,False,True,False,True,True,True,False,False,True,False,False,True,True,True,True,True,True,False,True,True,True,False,True,True,False,True,False,False,True,False,True,True,False,True,False,True,True,False,True,False,True,False,False,False,True,True,True,False,False,False,False,True,False,True,False,False,False,True,True,True,True,False,False,True,True,False,True,False,True,False,True,False,False,True,False,True,False,False,False,False,False,False,True,True,True,False,True,True,True,False,True,False,False,True,False,False,False,True,False,True,True,True,True,False,False,True,True,True,True,True,True,False,True,True,True,False,True,False,False,False,True,True,False,True,False,False,True,False,True,False,True,True,True,False,True,False,False,False,True,True,False,False,True,True,True,False,False,False,True,False,False,False,True,True,True,True,True,True,False,True,True,True,False,False,False,True,False,False,True,True,True,True,False,True,True,True,True,True,False,False,True,False,False,False,True,False,True,True,True,True,False,False,True,False,False,True,True,True,True,False,False,False,False,False,True,True,False,True,False,False,True,True,False,False,True,False,False,False,True,True,False,True,True,True,True,True,False,False,False,True,False,True,True,False,True,True,True,True,False,True,True,True,False,False,True,True,False,True,False,True,False,False,False,True,True,True,True,True,True,True,False,True,False,True,False,False,False,True,True,False,True,True,False,True,True,True,True,True,True,True,False,True,True,False,True,False,True,False,True,False,True,True,True,False,False,True,False,True,True,True,True,False,False,True,True,True,True,False,False,False,True,False,True,False,False,False,False,True,False,True,True,False,False,True,False,True,False,False,False,True,True,True,True,False,True,True,True,False,True,False,False,True,False,True,True,True,False,False,False,False,True,False,False,False,True,False,True,True,False,True,True,False,False,False,False,True,True,True,True,True,True,True,False,False,True,True,True,True,True,True,True,True,True,False,True,False,False,False,False,True,True,True,True,True,True,True,True,True,False,False,False,False,False,False,False,True,True,True,False,True,False,True,False,False,True,True,False,False,True,False,True,False,True,False,True,True,True,False,False,True,True,False,True,True,False,True,False,True,False,False,False,True,True,False,True,True,True,True,True,False,False,False,False,True,False,False,False,True,False,False,False,True,False,False,False,False,True,False,False,False,False,False,True,False,True,False,True,False,True,False,True,True,False,True,True,False,True,True,True,False,False,True,True,False,True,False,True,True,False,True,True,True,True,False,True,False,False,False,True,True,False,False,True,False,True,False,False,True,True,True,True,True,False,False,False,False,False,True,True,True,False,False,False,True,False,True,False,False,True,True,True,True,True,False,True,False,False,True,True,False,False,False,True,False,True,True,False,True,False,True,False,False,True,False,False,True,True,False,True,False,True,True,True,False,True,False,False,False,True,False,False,True,False,True,False,True,True,False,True,True,False,True,False,True,False,False,True,True,False,False,False,True,True,True,True,True,False,True,True,True,True,True,True,False,False,True,True,True,True,False,True,True,False,True,True,False,True,False,True,True,False,True,False,False,True,True,True,True,False,False,False,False,True,True,False,True,False,True,True,False,False,False,True,False,True,False,False,False,False,True,True,True,True,True,True,False,False,False,True,False,False,True,False,True,True,False,False,True,False,True,True,False,True,True,False,False,True,False,False,False,True,True,True,False,False,False,False,False,False,True,True,False,True,True,True,False,False,True,True,False,True,True,False,False,False,False,True,True,False,True,True,True,True,False,False,True,False,False,False,False,False,True,False,True,False,True,True,False,True,False,False,False,True,False,False,True,False,True,True,False,True,False,False,False,True,False,True,True,False,True,False,False,False,False,True,True,False,False,True,True,True,False,True,False,False,True,False,True,True,True,True,False,True,True,False,False,True,True,False,False,True,False,False,True,False,False,False,False,False,False,True,True,False,False,False,False,False,False,True,True,True,True,True,False,False,True,True,False,False,True,False,True,True,False,True,True,False,True,False,True,True,True,False,True,False,False,False,False,False,True,True,True,False,False,False,True,True,True,True,True,False,True,True,True,True,False,False,False,True,False,True,True,False,True,False,False,False,False,False,False,False,True,False,False,True,False,True,False,True,False,True,True,True,False,False,True,False,False,True,False,True,False,True,True,True,True,True,True,False,True,False,False,False,False,False,True,False,False,True,True,False,False,False,False,True,False,True,True,False,False,True,True,False,False,False,True,False,True,True,False,False,True,False,False,True,False,True,True,False,False,False,True,True,False,True,False,False,False,True,False,False,True,False,False,True,False,True,True,False,False,True,False,True,True,True,False,False,False,True,False,True,True,True,False,True,False,False,True,False,True,False,False,False,False,False,False,False,False,True,False,False,True,True,False,False,False,False,False,False,False,True,True,True,False,True,True,True,True,False,True,True,False,False,True,False,False,True,True,False,True,True,True,False,False,True,False,False,True,True,True,True,False,False,True,False,False,False,True,True,False,True,False,True,True,False,True,True,True,False,False,False,False,True,False,False,False,True,True,True,False,False,True,False,False,False,False,False,False,False,False,False,True,False,True,False,False,True,True,False,True,True,False,True,False,True,False,False,False,True,False,False,True,True,False,True,True,False,False,True,False,False,True,True,False,True,True,True,False,True,True,True,False,True,True,True,False,True,True,False,False,True,False,True,False,False,False,True,True,False,False,True,False,False,True,True,True,False,False,True,True,True,False,False,False,True,True,True,False,False,True,False,False,False,True,False,False,False,False,True,False,False,True,True,False,False,False,True,False,False,False,False,True,True,False,True,False,True,False,True,True,False,True,True,False,True,False,False,True,False,False,True,False,True,False,True,True,False,False,True,False,True,True,True,False,True,True,False,False,True,True,False,True,True,True,True,False,True,False,True,True,False,False,False,True,True,True,False,True,True,True,False,False,True,True,False,False,False,True,True,False,False,True,True,True,False,True,True,False,True,False,True,True,True,True,False,False,False,False,True,False,True,True,False,False,True,True,True,True,False,False,True,False,True,True,False,True,False,True,True,True,False,True,False,True,False,False,True,True,False,False,True,True,False,True,False,True,False,True,False,False,True,False,True,False,True,True,True,True,False,True,False,False,False,False,True,False,False,False,True,False,True,False,True,True,False,True,False,False,False,False,True,True,False,False,True,True,True,True,False,True,False,False,False,False,False,True,False,False,False,False,False,True,False,False,False,False,True,False,True,False,False,False,True,True,False,True,False,True,False,True,False,False,True,False,False,False,False,False,False,False,False,True,True,True,True,True,True,False,True,False,False,True,False,False,False,False,True,True,True,True,False,False,True,True,False,True,True,False,True,False,False,False,True,True,True,False,False,False,False,True,True,True,True,True,True,True,False,False,False,True,True,False,True,False,False,False,True,True,False,False,True,True,False,False,False,True,False,True,False,True,False,True,False,True,False,True,True,False,True,True,False,False,False,True,False,False,True,True,True,False,True,True,True,False,True,True,True,False,False,True,True,True,False,True,False,True,False,True,True,True,True,True,True,True,True,True,True,False,False,False,False,True,True,True,True,True,True,True,True,True,False,False,False,True,True,True,False,True,False,True,False,True,True,True,False,False,False,True,False,False,False,True,True,True,False,True,False,True,False,True,True,False,True,True,True,False,False,True,True,True,True,True,False,False,False,True,False,False,False,False,False,False,True,False,False,False,True,False,True,True,False,False,True,True,False,True,False,False,False,True,True,True,True,False,True,True,True,True,False,True,False,False,False,True,False,False,True,True,False,True,False,False,True,False,False,True,True,False,False,True,True,True,True,False,True,False,False,False,False,False,False,False,False,False,True,True,False,True,False,False,False,True,True,True,True,True,True,False,True,True,True,False,False,False,True,False,True,True,False,True,True,False,True,True,False,False,False,False,True,True,True,True,False,False,True,True,True,False,True,False,True,False,False,True,True,True,True,False,False,False,True,True,False,False,True,True,False,True,True,False,False,False,True,False,False,False,True,True,False,False,True,True,True,False,True,False,True,False,False,False,False,True,True,True,True,False,False,True,False,True,True,False,False,True,True,False,True,False,False,False,True,True,True,False,True,False,False,True,True,False,True,True,True,False,False,False,True,False,True,True,False,True,True,False,False,False,False,True,True,False,True,False,False,True,False,True,True,False,False,False,False,True,False,True,False,False,True,True,True,False,False,True,True,True,True,True,False,True,True,True,False,False,True,False,True,True,True,True,True,False,True,True,True,True,False,True,False,True,False,True,True,False,False,True,False,True,False,False,False,True,True,False,False,False,False,True,True,False,False,False,False,False,True,True,True,True,True,True,False,True,False,True,False,False,False,False,True,True,False,False,False,True,False,False,True,True,False,False,True,False,False,True,False,True,False,False,False,True,True,False,True,False,True,True,False,False,True,False,True,True,False,True,False,False,False,True,True,False,True,False,False,True,True,True,False,False,True,False,True,False,False,False,False,True,True,True,True,False,True,False,True,True,False,True,True,False,False,True,False,True,True,False,False,True,True,False,True,False,False,False,True,False,True,True,False,False,False,True,True,True,False,False,False,False,False,False,False,False,True,False,False,False,False,False,True,False,True,False,False,True,True,True,False,False,True,False,False,True,True,True,True,True,False,True,True,False,True,True,False,False,True,False,True,False,True,False,False,False,True,False,True,False,False,True,False,True,True,False,False,True,False,True,False,False,True,False,False,False,True,False,True,True,True,False,True,False,False,True,False,True,True,True,True,True,True,True,False,False,False,True,True,False,False,False,False,True,False,False,False,True,False,True,False,True,True,True,True,True,False,True,True,False,True,False,True,False,False,False,False,False,True,False,False,True,False,False,True,False,False,True,True,False,False,False,False,True,True,True,False,False,True,True,False,False,False,True,False,False,True,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,True,True,False,True,True,True,True,True,True,True,True,True,True,False,True,True,True,False,True,True,False,True,False,True,True,False,True,True,False,True,False,True,False,False,False,False,True,True,True,False,False,False,True,True,True,False,False,False,False,True,True,True,False,True,False,True,True,True,True,True,False,True,False,False,True,False,False,False,False,False,False,False,False,True,False,True,True,False,True,False,False,False,True,False,True,True,False,False,False,True,True,False,False,True,False,True,False,True,True,False,True,True,False,True,False,False,True,True,True,False,True,True,True,False,True,False,True,True,True,True,False,False,True,False,False,False,True,False,True,False,False,False,True,False,True,True,True,False,True,False,True,False,True,False,True,False,False,False,False,True,False,False,False,True,True,False,True,False,False,False,True,False,False,False,False,False,False,True,False,True,True,True,True,False,True,False,True,False,True,True,True,True,True,True,False,False,True,False,True,True,False,False,True,True,False,False,True,False,True,True,True,True,True,True,True,False,True,False,False,False,True,False,True,True,True,False,True,True,False,False,False,False,False,False,True,True,False,False,True,True,False,True,False,True,False,False,True,True,False,False,False,False,False,True,True,True,True,False,False,True,True,True,False,True,True,True,False,True,False,False,False,False,True,True,True,True,True,False,False,True,False,False,True,False,False,False,False,True,True,False,True,False,True,True,True,False,False,False,True,False,False,False,False,True,True,True,False,False,False,False,True,False,True,True,True,True,True,True,False,False,True,True,False,True,False,False,True,True,False,True,True,False,True,False,True,False,True,True,False,True,True,True,False,False,False,True,True,False,False,False,False,True,True,True,False,False,True,False,True,True,True,False,True,False,False,False,False,False,True,False,True,False,True,True,True,False,False,False,False,False,False,False,False,False,True,False,False,False,False,True,True,True,True,False,True,False,False,True,False,True,True,True,False,True,True,True,True,True,True,True,False,False,True,False,False,True,False,False,True,True,True,True,False,False,True,False,False,False,True,False,True,True,False,True,False,True,False,True,False,False,False,False,False,True,False,False,False,True,False,False,False,True,True,False,True,False,False,False,False,False,False,False,True,False,True,True,True,False,False,False,False,False,False,False,True,True,False,False,False,False,False,False,True,True], dtype = "bool")#candidate|3143|(2925,)|const|bool
call_3142 = func_371_call(relay.reshape(const_3143.astype('bool'), [13, 15, 15]), relay.reshape(const_3143.astype('bool'), [13, 15, 15]), )
call_3144 = func_371_call(relay.reshape(const_3143.astype('bool'), [13, 15, 15]), relay.reshape(const_3143.astype('bool'), [13, 15, 15]), )
output = relay.Tuple([call_3089,bop_3119,call_3134,call_3137,const_3138,call_3140,call_3142,const_3143,])
output2 = relay.Tuple([call_3090,bop_3122,call_3135,call_3139,const_3138,call_3141,call_3144,const_3143,])
func_3152 = relay.Function([var_3094,], output)
mod['func_3152'] = func_3152
mod = relay.transform.InferType()(mod)
var_3153 = relay.var("var_3153", dtype = "float32", shape = (234, 2))#candidate|3153|(234, 2)|var|float32
output = func_3152(var_3153)
func_3154 = relay.Function([var_3153], output)
mutated_mod['func_3154'] = func_3154
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2967_call = mod.get_global_var('func_2967')
func_2968_call = mutated_mod.get_global_var('func_2968')
call_3181 = relay.TupleGetItem(func_2967_call(), 0)
call_3182 = relay.TupleGetItem(func_2968_call(), 0)
output = call_3181
output2 = call_3182
func_3194 = relay.Function([], output)
mod['func_3194'] = func_3194
mod = relay.transform.InferType()(mod)
output = func_3194()
func_3195 = relay.Function([], output)
mutated_mod['func_3195'] = func_3195
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2899_call = mod.get_global_var('func_2899')
func_2900_call = mutated_mod.get_global_var('func_2900')
call_3293 = relay.TupleGetItem(func_2899_call(), 1)
call_3294 = relay.TupleGetItem(func_2900_call(), 1)
func_371_call = mod.get_global_var('func_371')
func_374_call = mutated_mod.get_global_var('func_374')
const_3296 = relay.const([True,False,True,False,True,False,True,True,True,True,False,False,False,False,True,False,True,False,True,True,True,False,True,True,False,True,False,False,False,False,False,True,True,True,False,False,True,True,False,True,False,False,True,False,True,True,False,False,True,True,True,False,False,True,True,False,False,True,False,True,False,False,False,True,True,False,True,True,False,True,False,False,False,True,True,True,False,True,True,False,True,True,False,True,False,False,True,False,True,True,True,True,False,False,False,True,False,False,False,False,True,False,True,True,False,False,False,False,True,False,False,False,True,True,True,True,True,False,True,False,False,True,False,False,True,False,True,True,False,False,False,False,False,True,True,False,True,False,True,False,False,True,True,True,False,False,False,True,True,True,False,True,False,False,True,True,False,False,True,True,False,True,True,True,False,False,True,True,False,False,True,False,False,False,True,False,True,True,False,False,True,False,True,True,False,False,True,False,False,False,True,True,True,False,False,True,True,True,False,True,False,True,False,False,False,True,False,True,True,False,True,False,False,False,True,False,False,False,True,False,False,False,True,True,True,True,False,False,True,False,True,True,False,True,True,False,True,True,True,False,False,False,False,False,False,True,True,False,False,False,False,False,False,False,False,True,True,False,True,False,True,True,True,True,False,False,True,True,False,False,True,False,False,True,False,False,True,True,False,True,True,False,True,False,False,True,True,False,False,True,False,True,False,False,False,False,False,True,False,False,True,True,False,True,True,True,True,False,False,True,True,False,True,False,False,False,False,True,False,False,False,False,True,False,False,True,True,True,False,True,True,True,False,False,False,True,True,True,True,True,False,False,True,True,True,True,True,True,True,True,True,True,False,False,False,False,True,True,True,True,False,True,False,False,True,False,False,False,True,True,True,True,False,True,False,True,False,False,False,True,True,True,True,True,True,True,False,False,False,True,True,False,False,True,False,True,True,False,True,False,False,True,True,False,False,True,True,False,True,True,False,True,False,True,False,True,False,False,True,False,False,False,False,False,True,False,False,False,True,True,False,True,False,True,True,False,False,False,True,False,True,True,True,True,False,True,False,False,False,True,False,False,True,False,False,False,False,False,False,True,False,False,False,False,True,True,True,True,True,False,True,False,True,False,True,True,False,True,True,False,False,True,False,True,True,False,True,True,True,True,True,True,True,True,True,False,True,False,False,False,False,True,True,True,False,False,False,False,False,True,False,False,False,False,False,True,False,True,True,True,True,False,False,False,True,False,True,False,False,True,True,True,False,False,False,False,False,True,False,False,False,False,True,True,False,True,False,True,False,True,False,True,True,True,False,True,True,True,True,True,False,False,False,False,False,True,True,True,False,True,True,False,False,False,True,False,True,False,True,False,True,False,True,True,True,True,False,False,False,True,True,False,False,False,True,False,True,False,True,True,True,True,True,True,True,True,False,True,True,True,True,False,True,False,True,False,False,True,False,False,True,False,True,True,False,False,True,True,False,True,False,True,False,True,True,True,False,True,False,True,False,True,False,False,False,True,False,False,True,True,False,False,True,True,True,True,True,False,False,True,True,False,True,True,True,False,True,False,True,True,True,True,True,True,True,True,True,False,True,False,True,True,False,False,True,True,True,False,True,True,False,True,True,True,False,False,True,True,False,False,True,False,True,False,True,True,True,False,True,False,False,False,True,False,False,False,True,True,True,True,False,True,False,True,False,False,True,True,False,False,True,True,False,False,True,True,True,False,False,False,False,False,False,True,True,False,False,False,True,True,True,True,False,True,False,False,False,False,True,False,False,False,True,False,False,False,True,False,False,True,False,False,False,True,True,True,True,True,True,True,False,True,False,False,False,True,False,False,True,True,False,True,True,True,True,False,True,False,False,True,False,False,True,False,True,True,True,True,False,False,False,True,True,False,True,False,True,False,False,False,True,True,True,True,False,False,True,False,True,True,True,True,True,True,True,True,False,False,False,False,False,False,True,False,False,True,False,False,True,False,False,False,True,False,True,False,False,False,False,True,True,True,False,True,False,True,False,False,True,False,True,False,False,False,False,False,True,False,False,False,False,True,True,False,True,False,False,True,True,False,True,False,True,True,True,False,True,True,False,False,True,True,False,True,False,False,False,True,False,False,False,True,True,True,True,False,True,True,False,False,True,True,True,False,False,False,False,True,False,True,False,True,False,False,True,False,True,True,False,True,True,False,False,True,True,True,True,False,False,True,True,True,False,False,False,True,False,False,False,False,True,False,False,False,True,True,False,False,False,False,True,True,False,False,False,True,True,False,False,False,True,True,True,False,True,True,True,True,False,True,False,True,False,False,True,True,True,False,True,True,False,False,False,True,False,True,False,False,True,False,False,False,True,True,False,False,True,True,False,True,True,False,False,True,False,False,False,True,False,True,False,False,True,False,True,False,True,False,False,False,False,False,True,False,True,True,False,False,True,False,True,False,False,False,True,False,False,True,True,False,False,True,False,True,False,False,True,True,False,True,False,False,True,True,False,True,False,True,True,True,True,True,True,False,True,False,False,True,True,False,True,True,True,True,True,True,True,False,True,True,False,True,False,True,False,False,False,False,True,False,False,True,True,True,True,False,False,True,True,True,True,False,True,True,True,False,False,True,False,True,False,False,False,False,False,False,True,False,True,False,False,True,True,True,False,False,True,False,False,False,False,True,False,True,False,False,True,True,True,True,False,True,False,True,False,False,True,True,False,False,True,True,True,True,False,False,True,False,False,True,False,False,True,True,True,True,True,False,False,False,False,True,True,False,False,True,False,True,False,False,False,False,True,True,True,False,True,False,False,False,False,False,False,True,True,False,False,False,False,True,False,False,False,False,False,False,True,False,True,False,True,True,False,False,True,True,False,False,True,False,False,True,True,True,False,False,True,True,True,True,False,True,False,False,True,False,False,True,True,True,True,False,True,True,False,False,False,True,False,True,True,True,True,False,False,True,True,True,False,False,False,False,True,False,False,True,True,False,False,False,False,True,False,True,False,False,True,False,True,True,True,True,False,False,True,False,False,False,True,False,False,False,True,False,False,True,True,True,False,True,True,False,False,True,True,False,False,False,False,True,True,True,False,False,False,False,False,False,False,False,False,True,False,True,True,False,True,False,False,True,True,True,True,True,True,False,True,True,False,True,False,True,False,True,True,False,True,False,False,True,False,True,False,False,False,True,False,True,True,False,False,False,False,True,True,True,True,False,False,True,True,False,True,False,True,False,False,False,False,True,False,False,False,False,False,False,False,True,False,True,True,False,False,True,False,True,False,True,False,False,True,True,True,False,True,False,False,False,True,True,True,True,True,True,True,False,True,True,True,True,True,False,False,True,False,False,False,False,True,False,True,False,False,False,False,True,False,True,True,True,False,False,False,True,True,False,True,True,True,False,False,False,True,False,True,True,False,False,True,False,False,False,False,False,False,True,False,True,False,True,False,False,False,True,True,True,True,True,False,False,True,True,True,False,True,False,True,False,False,True,False,True,True,False,True,False,True,True,True,True,True,True,True,True,False,True,False,True,False,True,False,True,False,True,False,True,True,True,True,False,False,True,True,False,False,False,False,True,False,True,True,True,False,False,False,True,True,False,False,True,True,False,True,True,True,True,True,True,False,False,True,True,False,False,True,False,False,True,True,False,False,False,True,False,True,True,True,False,False,False,False,True,False,True,True,False,False,False,True,False,False,False,True,False,False,False,False,False,True,False,True,True,False,False,False,True,False,True,False,False,True,False,True,False,True,False,False,True,False,True,True,True,True,True,True,True,True,False,True,True,False,False,False,False,True,False,False,True,False,False,True,True,False,False,True,True,True,True,False,True,False,True,False,True,False,False,False,False,False,False,True,False,False,True,False,True,False,False,False,False,False,True,True,False,False,True,True,True,False,True,False,True,True,True,False,True,True,True,True,True,True,False,True,True,False,True,True,False,False,True,False,False,True,True,True,True,False,False,False,True,False,False,False,True,True,False,False,False,True,False,True,False,False,False,False,False,False,True,False,False,False,False,False,True,False,True,False,False,False,False,True,False,True,True,True,False,False,True,True,True,True,False,False,False,True,False,False,True,True,True,True,True,True,True,True,True,True,True,False,True,False,True,True,True,True,False,True,True,True,False,False,True,True,False,True,False,False,True,True,True,False,False,True,False,True,False,True,False,True,True,True,True,True,False,False,False,False,False,True,False,False,True,True,True,False,False,True,False,True,False,False,False,False,True,False,False,True,True,False,False,True,False,False,False,False,False,False,True,False,True,True,True,False,False,False,False,False,False,True,True,False,True,True,True,False,True,True,True,True,True,True,False,True,True,False,False,False,False,True,False,True,False,True,True,False,False,False,False,False,True,True,False,False,True,True,False,False,False,True,True,False,False,True,True,False,True,True,False,True,False,False,False,False,False,False,False,False,False,False,False,True,False,False,True,True,False,True,True,False,False,True,False,False,False,False,False,False,True,False,True,False,True,False,False,True,False,True,True,False,True,True,True,True,True,False,False,True,True,False,False,True,True,False,True,True,False,False,True,False,False,True,False,True,True,False,False,True,True,True,True,True,False,False,False,False,False,True,True,True,True,True,False,False,False,True,True,False,True,True,False,False,False,False,True,True,True,False,False,False,True,True,True,False,True,False,False,True,True,True,False,False,True,False,False,True,True,True,True,True,False,False,True,False,False,False,True,True,False,True,False,False,False,True,False,True,True,False,False,False,True,False,False,False,False,False,True,False,False,True,True,False,True,False,True,True,False,False,True,True,False,True,True,False,False,True,False,False,True,False,False,False,True,True,True,True,True,False,True,True,True,False,False,False,False,True,False,True,True,True,False,True,False,True,False,False,False,False,False,True,False,True,True,True,False,False,True,True,True,False,True,False,True,True,True,True,False,True,False,True,False,False,True,False,True,True,False,True,True,True,False,True,False,False,True,False,False,False,True,True,False,False,False,True,True,True,True,True,False,True,True,False,False,False,False,True,True,False,True,False,True,True,True,True,True,False,True,False,False,True,True,True,True,True,False,True,False,True,False,False,True,True,False,True,True,False,False,False,True,True,False,False,True,False,False,False,False,True,False,True,False,False,False,False,True,False,True,False,False,True,False,True,True,True,False,False,True,False,True,False,False,True,True,True,True,True,True,False,False,False,True,True,False,True,True,True,True,False,True,True,True,False,False,False,True,False,True,False,True,False,True,True,True,False,False,True,True,True,True,True,True,False,False,True,True,True,True,False,True,False,False,True,False,False,True,True,True,False,False,False,False,True,True,False,True,True,True,False,False,False,True,False,False,False,True,True,True,False,True,True,True,True,False,True,False,True,True,True,False,True,True,False,False,False,False,True,True,True,True,True,True,False,True,True,False,True,False,False,True,False,True,False,True,True,False,True,False,True,False,False,False,True,True,False,True,True,True,False,True,False,False,False,False,True,False,True,False,False,True,False,False,False,False,False,True,False,True,True,True,False,False,True,True,True,True,True,False,False,True,True,False,True,False,True,True,False,False,True,False,True,True,True,True,False,True,False,False,False,True,False,False,True,True,False,False,True,True,True,True,False,False,False,False,False,True,True,False,True,False,True,False,False,False,True,False,True,True,False,True,False,False,False,False,False,False,False,True,True,True,False,True,False,False,True,False,True,False,True,False,True,False,False,True,False,True,True,True,False,True,False,True,False,False,True,False,False,True,True,True,True,True,True,True,False,False,True,True,True,False,False,False,False,False,True,False,False,False,True,False,True,False,True,True,False,False,True,True,False,False,False,True,False,True,False,False,False,True,True,True,False,True,True,False,False,False,True,False,False,False,False,True,False,False,True,True,False,False,False,False,True,False,True,True,False,True,True,False,True,False,True,True,False,False,True,False,False,False,False,False,True,False,True,True,False,False,False,True,True,False,True,False,True,True,True,True,False,False,True,True,False,False,False,False,False,False,False,False,False,False,False,True,True,True,True,True,False,True,False,True,False,False,True,True,True,False,False,True,False,True,True,False,True,True,True,True,True,True,True,False,False,True,True,True,False,False,False,False,False,True,True,False,True,False,True,False,False,True,True,False,False,False,True,True,False,False,False,True,True,True,True,True,False,True,False,False,True,True,True,True,False,False,True,True,True,False,True,True,True,False,False,True,True,True,False,True,True,False,False,False,True,False,False,True,True,False,False,False,True,True,False,True,True,True,False,False,False,True,False,True,False,False,True,True,True,True,False,False,False,False,False,True,False,False,True,True,True,True,False,False,False,False,False,True,True,False,False,True,False,False,True,False,False,False,True,True,True,True,True,True,True,True,True,False,False,False,True,True,True,True,True,True,True,True,False,True,False,False,False,False,False,True,False,False,True,True,True,True,False,False,False,True,False,True,True,False,True,True,True,False,False,False,True,False,False,False,True,False,False,True,False,True,True,False,True,False,True,True,True,True,True,False,False,True,True,False,True,True,True,False,True,True,True,True,True,True,True,False,True,True,False,True,False,True,True,False,True,False,True,True,True,False,True,True,False,False,True,True,True,False,False,True,False,True,False,True,False,True,False,True,False,False,False,True,True,True,True,False,True,False,True,False,False,False,True,False,True,True,False,False,True,False,True,True,True,True,True,True,False,True,False,True,True,False,False,False,True,True,False,False,True,False,False,True,False,True,False,True,False,False,False,False,False,True,True,True,True,False,False,True,True,False,False,False,False,False,False,True,True,True,True,False,True,True,False,True,False], dtype = "bool")#candidate|3296|(2925,)|const|bool
call_3295 = func_371_call(relay.reshape(const_3296.astype('bool'), [13, 15, 15]), relay.reshape(const_3296.astype('bool'), [13, 15, 15]), )
call_3297 = func_371_call(relay.reshape(const_3296.astype('bool'), [13, 15, 15]), relay.reshape(const_3296.astype('bool'), [13, 15, 15]), )
bop_3298 = relay.minimum(call_3295.astype('uint64'), relay.reshape(const_3296.astype('uint64'), relay.shape_of(call_3295))) # shape=(13, 15, 15)
bop_3301 = relay.minimum(call_3297.astype('uint64'), relay.reshape(const_3296.astype('uint64'), relay.shape_of(call_3297))) # shape=(13, 15, 15)
output = relay.Tuple([call_3293,bop_3298,])
output2 = relay.Tuple([call_3294,bop_3301,])
func_3302 = relay.Function([], output)
mod['func_3302'] = func_3302
mod = relay.transform.InferType()(mod)
output = func_3302()
func_3303 = relay.Function([], output)
mutated_mod['func_3303'] = func_3303
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3312 = relay.const([[[-1.520762,-7.072820,-4.328507],[-9.839092,1.162010,-6.674564],[-3.594362,7.620441,-5.991069],[1.632281,0.384108,5.092661],[-0.931914,-6.042665,-1.345187],[-3.355239,8.591917,3.154139],[-9.112646,-8.428343,-4.889613],[1.689195,-1.096607,6.674525],[6.932826,8.734376,-7.132734]],[[8.401054,-4.192974,4.435280],[7.230173,4.251724,-0.843133],[-6.364444,-1.610999,2.523455],[2.706636,-5.119786,1.113741],[-8.818498,-6.156323,-6.517544],[3.631380,6.266085,6.865983],[-3.116214,-9.566878,-7.677304],[-6.823960,3.440192,9.031114],[-9.608024,5.505100,6.656505]],[[-7.957271,9.800749,4.372033],[6.257947,3.669802,-2.521547],[6.976244,8.977753,8.987138],[9.480683,-3.594958,-5.894862],[3.318823,3.064985,8.194298],[4.695833,-0.073378,-0.407363],[-0.626623,-2.989565,-2.294872],[4.584421,-6.471758,-2.124676],[-9.692724,4.639033,-9.920952]]], dtype = "float32")#candidate|3312|(3, 9, 3)|const|float32
uop_3313 = relay.cosh(const_3312.astype('float32')) # shape=(3, 9, 3)
func_7_call = mod.get_global_var('func_7')
func_11_call = mutated_mod.get_global_var('func_11')
var_3321 = relay.var("var_3321", dtype = "float32", shape = (78, 6))#candidate|3321|(78, 6)|var|float32
call_3320 = relay.TupleGetItem(func_7_call(relay.reshape(var_3321.astype('float32'), [12, 13, 3]), relay.reshape(var_3321.astype('float32'), [12, 13, 3]), ), 0)
call_3322 = relay.TupleGetItem(func_11_call(relay.reshape(var_3321.astype('float32'), [12, 13, 3]), relay.reshape(var_3321.astype('float32'), [12, 13, 3]), ), 0)
func_842_call = mod.get_global_var('func_842')
func_847_call = mutated_mod.get_global_var('func_847')
const_3325 = relay.const([-5.713529,6.304156,1.375122,6.249663,-9.309847,-7.166345,-5.441744,-3.683628,5.472651,-4.896172,-0.917895,3.984058,1.223310,8.592311,7.710472,3.409975,3.460902,-1.951887,7.910422,7.298028,-3.236771,-5.467244,3.085825,3.835749,1.483072,0.435073,-6.336369,-0.730626,-6.257346,0.228091,6.914223,3.858486,0.042968,1.825858,-8.877260,-2.366681,-4.280282,0.931893,4.875327,-9.564473,-2.542319,-9.959924,-5.347121,-2.366444,0.698881,7.533173,6.415918,4.187027,-7.851357,9.682157,5.703850,2.885209,-8.687639,-2.292420,6.136735,-2.224119,-5.307553,9.031964,5.701646,3.179257,7.372408,1.891264,-1.259145,9.966509,0.408256,6.282507,-9.089645,-9.124034,3.974695,4.610747,5.157072,7.072986,-3.308216,3.096844,-5.782922,-4.742463,4.565184,-6.375903,-2.512299,-3.869488,-0.498548,5.519883,0.844716,5.520152,-9.357641,8.541735,-2.307236,8.545494,8.883304,1.797758,6.395862,8.537315,6.226513,-0.858761,1.530812,-7.144499,-9.300030,4.843059,2.285237,7.981302,2.260398,-9.146981,8.976788,-7.293088,-8.219578,-2.249740,-7.164179,-4.693643,-9.459620,7.731574,5.078437,1.490725], dtype = "float64")#candidate|3325|(112,)|const|float64
call_3324 = relay.TupleGetItem(func_842_call(relay.reshape(const_3325.astype('float64'), [4, 4, 7]), relay.reshape(const_3325.astype('float64'), [4, 4, 7]), relay.reshape(var_3321.astype('float32'), [1, 468]), ), 2)
call_3326 = relay.TupleGetItem(func_847_call(relay.reshape(const_3325.astype('float64'), [4, 4, 7]), relay.reshape(const_3325.astype('float64'), [4, 4, 7]), relay.reshape(var_3321.astype('float32'), [1, 468]), ), 2)
output = relay.Tuple([uop_3313,call_3320,var_3321,call_3324,const_3325,])
output2 = relay.Tuple([uop_3313,call_3322,var_3321,call_3326,const_3325,])
func_3332 = relay.Function([var_3321,], output)
mod['func_3332'] = func_3332
mod = relay.transform.InferType()(mod)
mutated_mod['func_3332'] = func_3332
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3333 = relay.var("var_3333", dtype = "float32", shape = (78, 6))#candidate|3333|(78, 6)|var|float32
func_3332_call = mutated_mod.get_global_var('func_3332')
call_3334 = func_3332_call(var_3333)
output = call_3334
func_3335 = relay.Function([var_3333], output)
mutated_mod['func_3335'] = func_3335
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3194_call = mod.get_global_var('func_3194')
func_3195_call = mutated_mod.get_global_var('func_3195')
call_3349 = func_3194_call()
call_3350 = func_3194_call()
output = relay.Tuple([call_3349,])
output2 = relay.Tuple([call_3350,])
func_3351 = relay.Function([], output)
mod['func_3351'] = func_3351
mod = relay.transform.InferType()(mod)
mutated_mod['func_3351'] = func_3351
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3351_call = mutated_mod.get_global_var('func_3351')
call_3352 = func_3351_call()
output = call_3352
func_3353 = relay.Function([], output)
mutated_mod['func_3353'] = func_3353
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2899_call = mod.get_global_var('func_2899')
func_2900_call = mutated_mod.get_global_var('func_2900')
call_3356 = relay.TupleGetItem(func_2899_call(), 0)
call_3357 = relay.TupleGetItem(func_2900_call(), 0)
uop_3360 = relay.sigmoid(call_3356.astype('float64')) # shape=(4, 28)
uop_3362 = relay.sigmoid(call_3357.astype('float64')) # shape=(4, 28)
uop_3371 = relay.sinh(uop_3360.astype('float64')) # shape=(4, 28)
uop_3373 = relay.sinh(uop_3362.astype('float64')) # shape=(4, 28)
func_2623_call = mod.get_global_var('func_2623')
func_2626_call = mutated_mod.get_global_var('func_2626')
var_3376 = relay.var("var_3376", dtype = "float32", shape = (1, 288))#candidate|3376|(1, 288)|var|float32
call_3375 = relay.TupleGetItem(func_2623_call(relay.reshape(var_3376.astype('float32'), [288,])), 2)
call_3377 = relay.TupleGetItem(func_2626_call(relay.reshape(var_3376.astype('float32'), [288,])), 2)
output = relay.Tuple([uop_3371,call_3375,var_3376,])
output2 = relay.Tuple([uop_3373,call_3377,var_3376,])
func_3385 = relay.Function([var_3376,], output)
mod['func_3385'] = func_3385
mod = relay.transform.InferType()(mod)
mutated_mod['func_3385'] = func_3385
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3386 = relay.var("var_3386", dtype = "float32", shape = (1, 288))#candidate|3386|(1, 288)|var|float32
func_3385_call = mutated_mod.get_global_var('func_3385')
call_3387 = func_3385_call(var_3386)
output = call_3387
func_3388 = relay.Function([var_3386], output)
mutated_mod['func_3388'] = func_3388
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2899_call = mod.get_global_var('func_2899')
func_2900_call = mutated_mod.get_global_var('func_2900')
call_3432 = relay.TupleGetItem(func_2899_call(), 2)
call_3433 = relay.TupleGetItem(func_2900_call(), 2)
output = call_3432
output2 = call_3433
func_3437 = relay.Function([], output)
mod['func_3437'] = func_3437
mod = relay.transform.InferType()(mod)
mutated_mod['func_3437'] = func_3437
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3437_call = mutated_mod.get_global_var('func_3437')
call_3438 = func_3437_call()
output = call_3438
func_3439 = relay.Function([], output)
mutated_mod['func_3439'] = func_3439
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3351_call = mod.get_global_var('func_3351')
func_3353_call = mutated_mod.get_global_var('func_3353')
call_3440 = relay.TupleGetItem(func_3351_call(), 0)
call_3441 = relay.TupleGetItem(func_3353_call(), 0)
func_2967_call = mod.get_global_var('func_2967')
func_2968_call = mutated_mod.get_global_var('func_2968')
call_3451 = relay.TupleGetItem(func_2967_call(), 0)
call_3452 = relay.TupleGetItem(func_2968_call(), 0)
output = relay.Tuple([call_3440,call_3451,])
output2 = relay.Tuple([call_3441,call_3452,])
func_3461 = relay.Function([], output)
mod['func_3461'] = func_3461
mod = relay.transform.InferType()(mod)
output = func_3461()
func_3462 = relay.Function([], output)
mutated_mod['func_3462'] = func_3462
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3351_call = mod.get_global_var('func_3351')
func_3353_call = mutated_mod.get_global_var('func_3353')
call_3481 = relay.TupleGetItem(func_3351_call(), 0)
call_3482 = relay.TupleGetItem(func_3353_call(), 0)
output = relay.Tuple([call_3481,])
output2 = relay.Tuple([call_3482,])
func_3483 = relay.Function([], output)
mod['func_3483'] = func_3483
mod = relay.transform.InferType()(mod)
mutated_mod['func_3483'] = func_3483
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3483_call = mutated_mod.get_global_var('func_3483')
call_3484 = func_3483_call()
output = call_3484
func_3485 = relay.Function([], output)
mutated_mod['func_3485'] = func_3485
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2967_call = mod.get_global_var('func_2967')
func_2968_call = mutated_mod.get_global_var('func_2968')
call_3497 = relay.TupleGetItem(func_2967_call(), 0)
call_3498 = relay.TupleGetItem(func_2968_call(), 0)
output = call_3497
output2 = call_3498
func_3526 = relay.Function([], output)
mod['func_3526'] = func_3526
mod = relay.transform.InferType()(mod)
mutated_mod['func_3526'] = func_3526
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3526_call = mutated_mod.get_global_var('func_3526')
call_3527 = func_3526_call()
output = call_3527
func_3528 = relay.Function([], output)
mutated_mod['func_3528'] = func_3528
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2967_call = mod.get_global_var('func_2967')
func_2968_call = mutated_mod.get_global_var('func_2968')
call_3631 = relay.TupleGetItem(func_2967_call(), 0)
call_3632 = relay.TupleGetItem(func_2968_call(), 0)
func_3332_call = mod.get_global_var('func_3332')
func_3335_call = mutated_mod.get_global_var('func_3335')
call_3642 = relay.TupleGetItem(func_3332_call(relay.reshape(call_3631.astype('float32'), [78, 6])), 3)
call_3643 = relay.TupleGetItem(func_3335_call(relay.reshape(call_3631.astype('float32'), [78, 6])), 3)
func_2037_call = mod.get_global_var('func_2037')
func_2040_call = mutated_mod.get_global_var('func_2040')
var_3645 = relay.var("var_3645", dtype = "float32", shape = (288,))#candidate|3645|(288,)|var|float32
call_3644 = relay.TupleGetItem(func_2037_call(relay.reshape(var_3645.astype('float32'), [3, 6, 16]), relay.reshape(call_3631.astype('float32'), [468,]), ), 3)
call_3646 = relay.TupleGetItem(func_2040_call(relay.reshape(var_3645.astype('float32'), [3, 6, 16]), relay.reshape(call_3631.astype('float32'), [468,]), ), 3)
func_2899_call = mod.get_global_var('func_2899')
func_2900_call = mutated_mod.get_global_var('func_2900')
call_3647 = relay.TupleGetItem(func_2899_call(), 1)
call_3648 = relay.TupleGetItem(func_2900_call(), 1)
output = relay.Tuple([call_3631,call_3642,call_3644,var_3645,call_3647,])
output2 = relay.Tuple([call_3632,call_3643,call_3646,var_3645,call_3648,])
func_3650 = relay.Function([var_3645,], output)
mod['func_3650'] = func_3650
mod = relay.transform.InferType()(mod)
var_3651 = relay.var("var_3651", dtype = "float32", shape = (288,))#candidate|3651|(288,)|var|float32
output = func_3650(var_3651)
func_3652 = relay.Function([var_3651], output)
mutated_mod['func_3652'] = func_3652
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2967_call = mod.get_global_var('func_2967')
func_2968_call = mutated_mod.get_global_var('func_2968')
call_3657 = relay.TupleGetItem(func_2967_call(), 0)
call_3658 = relay.TupleGetItem(func_2968_call(), 0)
uop_3660 = relay.sqrt(call_3657.astype('float32')) # shape=(468,)
uop_3662 = relay.sqrt(call_3658.astype('float32')) # shape=(468,)
uop_3676 = relay.asin(uop_3660.astype('float64')) # shape=(468,)
uop_3678 = relay.asin(uop_3662.astype('float64')) # shape=(468,)
output = uop_3676
output2 = uop_3678
func_3694 = relay.Function([], output)
mod['func_3694'] = func_3694
mod = relay.transform.InferType()(mod)
mutated_mod['func_3694'] = func_3694
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3694_call = mutated_mod.get_global_var('func_3694')
call_3695 = func_3694_call()
output = call_3695
func_3696 = relay.Function([], output)
mutated_mod['func_3696'] = func_3696
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3763 = relay.var("var_3763", dtype = "float32", shape = (13, 8, 8))#candidate|3763|(13, 8, 8)|var|float32
uop_3764 = relay.asin(var_3763.astype('float32')) # shape=(13, 8, 8)
output = uop_3764
output2 = uop_3764
func_3766 = relay.Function([var_3763,], output)
mod['func_3766'] = func_3766
mod = relay.transform.InferType()(mod)
mutated_mod['func_3766'] = func_3766
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3767 = relay.var("var_3767", dtype = "float32", shape = (13, 8, 8))#candidate|3767|(13, 8, 8)|var|float32
func_3766_call = mutated_mod.get_global_var('func_3766')
call_3768 = func_3766_call(var_3767)
output = call_3768
func_3769 = relay.Function([var_3767], output)
mutated_mod['func_3769'] = func_3769
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3351_call = mod.get_global_var('func_3351')
func_3353_call = mutated_mod.get_global_var('func_3353')
call_3776 = relay.TupleGetItem(func_3351_call(), 0)
call_3777 = relay.TupleGetItem(func_3353_call(), 0)
output = call_3776
output2 = call_3777
func_3779 = relay.Function([], output)
mod['func_3779'] = func_3779
mod = relay.transform.InferType()(mod)
output = func_3779()
func_3780 = relay.Function([], output)
mutated_mod['func_3780'] = func_3780
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2967_call = mod.get_global_var('func_2967')
func_2968_call = mutated_mod.get_global_var('func_2968')
call_3790 = relay.TupleGetItem(func_2967_call(), 0)
call_3791 = relay.TupleGetItem(func_2968_call(), 0)
output = relay.Tuple([call_3790,])
output2 = relay.Tuple([call_3791,])
func_3794 = relay.Function([], output)
mod['func_3794'] = func_3794
mod = relay.transform.InferType()(mod)
output = func_3794()
func_3795 = relay.Function([], output)
mutated_mod['func_3795'] = func_3795
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3483_call = mod.get_global_var('func_3483')
func_3485_call = mutated_mod.get_global_var('func_3485')
call_3853 = relay.TupleGetItem(func_3483_call(), 0)
call_3854 = relay.TupleGetItem(func_3485_call(), 0)
output = relay.Tuple([call_3853,])
output2 = relay.Tuple([call_3854,])
func_3859 = relay.Function([], output)
mod['func_3859'] = func_3859
mod = relay.transform.InferType()(mod)
mutated_mod['func_3859'] = func_3859
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3859_call = mutated_mod.get_global_var('func_3859')
call_3860 = func_3859_call()
output = call_3860
func_3861 = relay.Function([], output)
mutated_mod['func_3861'] = func_3861
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2899_call = mod.get_global_var('func_2899')
func_2900_call = mutated_mod.get_global_var('func_2900')
call_3907 = relay.TupleGetItem(func_2899_call(), 0)
call_3908 = relay.TupleGetItem(func_2900_call(), 0)
var_3917 = relay.var("var_3917", dtype = "float64", shape = (4, 28))#candidate|3917|(4, 28)|var|float64
bop_3918 = relay.logical_and(call_3907.astype('bool'), relay.reshape(var_3917.astype('bool'), relay.shape_of(call_3907))) # shape=(4, 28)
bop_3921 = relay.logical_and(call_3908.astype('bool'), relay.reshape(var_3917.astype('bool'), relay.shape_of(call_3908))) # shape=(4, 28)
output = relay.Tuple([bop_3918,])
output2 = relay.Tuple([bop_3921,])
func_3954 = relay.Function([var_3917,], output)
mod['func_3954'] = func_3954
mod = relay.transform.InferType()(mod)
mutated_mod['func_3954'] = func_3954
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3955 = relay.var("var_3955", dtype = "float64", shape = (4, 28))#candidate|3955|(4, 28)|var|float64
func_3954_call = mutated_mod.get_global_var('func_3954')
call_3956 = func_3954_call(var_3955)
output = call_3956
func_3957 = relay.Function([var_3955], output)
mutated_mod['func_3957'] = func_3957
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3302_call = mod.get_global_var('func_3302')
func_3303_call = mutated_mod.get_global_var('func_3303')
call_3959 = relay.TupleGetItem(func_3302_call(), 0)
call_3960 = relay.TupleGetItem(func_3303_call(), 0)
func_568_call = mod.get_global_var('func_568')
func_572_call = mutated_mod.get_global_var('func_572')
var_3963 = relay.var("var_3963", dtype = "float64", shape = (5, 63))#candidate|3963|(5, 63)|var|float64
call_3962 = relay.TupleGetItem(func_568_call(relay.reshape(var_3963.astype('float64'), [3, 7, 15]), relay.reshape(var_3963.astype('float64'), [3, 7, 15]), ), 0)
call_3964 = relay.TupleGetItem(func_572_call(relay.reshape(var_3963.astype('float64'), [3, 7, 15]), relay.reshape(var_3963.astype('float64'), [3, 7, 15]), ), 0)
var_3969 = relay.var("var_3969", dtype = "float64", shape = (5, 63))#candidate|3969|(5, 63)|var|float64
bop_3970 = relay.minimum(var_3963.astype('float64'), relay.reshape(var_3969.astype('float64'), relay.shape_of(var_3963))) # shape=(5, 63)
func_3859_call = mod.get_global_var('func_3859')
func_3861_call = mutated_mod.get_global_var('func_3861')
call_3973 = relay.TupleGetItem(func_3859_call(), 0)
call_3974 = relay.TupleGetItem(func_3861_call(), 0)
output = relay.Tuple([call_3959,call_3962,bop_3970,call_3973,])
output2 = relay.Tuple([call_3960,call_3964,bop_3970,call_3974,])
func_3976 = relay.Function([var_3963,var_3969,], output)
mod['func_3976'] = func_3976
mod = relay.transform.InferType()(mod)
var_3977 = relay.var("var_3977", dtype = "float64", shape = (5, 63))#candidate|3977|(5, 63)|var|float64
var_3978 = relay.var("var_3978", dtype = "float64", shape = (5, 63))#candidate|3978|(5, 63)|var|float64
output = func_3976(var_3977,var_3978,)
func_3979 = relay.Function([var_3977,var_3978,], output)
mutated_mod['func_3979'] = func_3979
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3993 = relay.var("var_3993", dtype = "int64", shape = (12, 9, 10))#candidate|3993|(12, 9, 10)|var|int64
var_3994 = relay.var("var_3994", dtype = "int64", shape = (12, 9, 10))#candidate|3994|(12, 9, 10)|var|int64
bop_3995 = relay.bitwise_xor(var_3993.astype('int64'), relay.reshape(var_3994.astype('int64'), relay.shape_of(var_3993))) # shape=(12, 9, 10)
func_3437_call = mod.get_global_var('func_3437')
func_3439_call = mutated_mod.get_global_var('func_3439')
call_4005 = func_3437_call()
call_4006 = func_3437_call()
output = relay.Tuple([bop_3995,call_4005,])
output2 = relay.Tuple([bop_3995,call_4006,])
func_4008 = relay.Function([var_3993,var_3994,], output)
mod['func_4008'] = func_4008
mod = relay.transform.InferType()(mod)
mutated_mod['func_4008'] = func_4008
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4008_call = mutated_mod.get_global_var('func_4008')
var_4010 = relay.var("var_4010", dtype = "int64", shape = (12, 9, 10))#candidate|4010|(12, 9, 10)|var|int64
var_4011 = relay.var("var_4011", dtype = "int64", shape = (12, 9, 10))#candidate|4011|(12, 9, 10)|var|int64
call_4009 = func_4008_call(var_4010,var_4011,)
output = call_4009
func_4012 = relay.Function([var_4010,var_4011,], output)
mutated_mod['func_4012'] = func_4012
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2899_call = mod.get_global_var('func_2899')
func_2900_call = mutated_mod.get_global_var('func_2900')
call_4083 = relay.TupleGetItem(func_2899_call(), 2)
call_4084 = relay.TupleGetItem(func_2900_call(), 2)
func_2623_call = mod.get_global_var('func_2623')
func_2626_call = mutated_mod.get_global_var('func_2626')
const_4086 = relay.const([1.798356,8.213454,0.770354,-1.137662,-2.703508,1.938748,-5.239798,-6.515315,0.415097,-0.921731,0.571304,4.988298,2.622238,8.743492,-0.920521,1.389623,3.339651,-1.546881,-3.923071,-6.060446,-1.636063,2.239388,-6.804159,-8.742809,-5.323383,-6.324828,-6.110446,1.993509,6.145532,-6.583320,-8.869494,1.263201,2.984792,-8.448859,5.640758,-0.261310,4.178771,-3.776157,8.744393,9.575946,8.913239,3.166223,1.007030,-4.177272,-4.500011,1.844481,-3.091492,-1.294609,-1.654759,7.351314,8.825226,2.781358,5.907767,2.142812,-3.118252,-0.143315,-2.222756,-6.301307,1.422831,-1.239158,3.155475,-5.010235,5.603688,5.696781,-5.111280,4.810138,-3.672610,-2.082956,-0.049216,-0.806068,-5.204167,-4.974351,9.662195,1.161375,3.778481,-2.843249,9.193663,-0.672226,7.989315,-6.548733,-1.807660,1.179418,9.551918,4.755625,1.335443,-1.397292,-9.676878,0.608536,6.116047,-7.002394,-5.405252,-6.132584,-1.073816,-1.775682,-3.027922,6.980619,-2.728496,-2.298650,-0.810705,6.157470,2.958790,3.949750,4.773533,8.237376,3.932022,8.403218,-2.640323,1.784847,9.978686,-4.847840,9.928059,-7.532891,8.843772,4.400491,-5.899455,9.409871,-0.772174,-2.820433,9.266907,6.043433,3.702774,3.249087,-2.038358,-4.858024,-1.384585,3.669795,-0.699161,-0.208539,-9.721808,9.623109,-9.401245,2.477683,-9.639312,-6.969175,1.294156,-9.715031,6.362326,2.038429,4.562440,0.596896,-7.185548,8.851550,-5.796567,-1.488687,6.731055,-1.573278,9.556651,-6.287174,1.259613,2.769863,-8.219446,9.404362,6.785475,2.833478,1.577789,4.544671,-5.258982,-2.385192,-0.514825,5.553029,8.178387,0.561153,8.060186,-7.769556,2.451606,-1.951572,3.923557,4.224438,-1.120505,3.725082,2.016507,1.386197,3.143901,-8.739184,9.328276,8.218824,8.875785,9.010436,5.093057,1.965787,6.756092,-1.597394,-4.153821,-7.991872,3.531735,-4.408924,-7.059244,-9.766715,3.572762,3.402062,-7.930971,7.495366,8.192805,6.075422,-9.625802,3.901611,-7.592648,5.504887,7.087634,4.927850,1.942609,2.029504,9.654399,-5.428441,1.604390,0.602359,-7.056254,1.502711,2.111409,-7.724580,-5.416385,-9.973167,-5.233984,0.068692,4.909325,-6.769056,-6.440353,-5.147561,7.510624,-4.987306,-4.723865,-7.106591,9.621633,-9.960466,-4.242125,-4.817784,7.362803,6.477357,-2.319993,5.388556,3.275261,6.470168,-0.332095,-7.310706,-8.048660,-1.016961,-4.583324,0.596559,-5.500200,2.903177,6.437302,1.196155,-4.186329,-7.137009,0.814579,-8.764174,3.155376,-0.916632,9.341243,8.699720,-1.823116,-8.100052,-0.267311,-2.547359,9.445798,-0.017564,3.438468,1.057678,-6.501998,7.146876,-5.308989,8.377431,5.554613,3.198235,-6.114986,-2.958469,-1.021822,4.443696,-1.732612,1.825529,0.925155,-4.598628,-6.405435,-1.164006,4.399142,-8.315424,6.386313,6.491852,-8.908401,0.787621,6.275113,4.089585,-0.689499,6.152743,-7.980043,8.910873,-2.354655,-7.426609], dtype = "float32")#candidate|4086|(288,)|const|float32
call_4085 = relay.TupleGetItem(func_2623_call(relay.reshape(const_4086.astype('float32'), [288,])), 0)
call_4087 = relay.TupleGetItem(func_2626_call(relay.reshape(const_4086.astype('float32'), [288,])), 0)
output = relay.Tuple([call_4083,call_4085,const_4086,])
output2 = relay.Tuple([call_4084,call_4087,const_4086,])
func_4088 = relay.Function([], output)
mod['func_4088'] = func_4088
mod = relay.transform.InferType()(mod)
mutated_mod['func_4088'] = func_4088
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4088_call = mutated_mod.get_global_var('func_4088')
call_4089 = func_4088_call()
output = call_4089
func_4090 = relay.Function([], output)
mutated_mod['func_4090'] = func_4090
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3483_call = mod.get_global_var('func_3483')
func_3485_call = mutated_mod.get_global_var('func_3485')
call_4097 = relay.TupleGetItem(func_3483_call(), 0)
call_4098 = relay.TupleGetItem(func_3485_call(), 0)
output = call_4097
output2 = call_4098
func_4108 = relay.Function([], output)
mod['func_4108'] = func_4108
mod = relay.transform.InferType()(mod)
output = func_4108()
func_4109 = relay.Function([], output)
mutated_mod['func_4109'] = func_4109
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2921_call = mod.get_global_var('func_2921')
func_2923_call = mutated_mod.get_global_var('func_2923')
call_4110 = relay.TupleGetItem(func_2921_call(), 0)
call_4111 = relay.TupleGetItem(func_2923_call(), 0)
func_2037_call = mod.get_global_var('func_2037')
func_2040_call = mutated_mod.get_global_var('func_2040')
var_4146 = relay.var("var_4146", dtype = "float32", shape = (468,))#candidate|4146|(468,)|var|float32
call_4145 = relay.TupleGetItem(func_2037_call(relay.reshape(call_4110.astype('float32'), [3, 6, 16]), relay.reshape(var_4146.astype('float32'), [468,]), ), 2)
call_4147 = relay.TupleGetItem(func_2040_call(relay.reshape(call_4110.astype('float32'), [3, 6, 16]), relay.reshape(var_4146.astype('float32'), [468,]), ), 2)
func_4008_call = mod.get_global_var('func_4008')
func_4012_call = mutated_mod.get_global_var('func_4012')
const_4150 = relay.const([[-10,9,-4,-10,8,-3,-6,1,-6,5,6,-1,-8,-5,-2,3,5,2,2,4,1,-2,-8,6,2,8,-1,-5,7,-7,3,10,1,7,6,-5,9,-6,10,2,3,8,-10,-3,2,-7,10,-5,9,-6,5,2,1,-2,-9,-3,-6,-4,-5,-5],[-9,-6,-8,-9,2,4,9,9,3,2,-6,4,-7,10,9,3,-6,4,7,-2,1,4,1,1,-7,-8,10,-6,-4,1,2,9,2,-3,-9,5,3,1,7,10,6,8,3,5,2,1,1,-3,5,1,5,5,7,1,-9,7,-10,3,1,-1],[7,9,3,-10,-2,-6,9,2,-7,-10,-6,4,-4,-9,5,9,3,-10,2,7,-3,8,4,7,-4,10,6,6,-8,-8,-7,7,-5,-8,-8,-10,8,4,9,-3,-8,1,-6,-7,-1,9,2,-10,2,-3,-1,-3,10,-10,9,-1,8,-5,8,1],[7,-9,-6,5,5,2,10,6,3,10,-1,10,-1,-6,-7,10,6,2,-6,-4,4,6,1,5,-8,-7,5,2,2,-7,-4,-4,6,-4,2,3,4,-1,3,-9,2,2,3,5,2,8,-1,-8,-8,-9,-2,6,4,-9,3,10,3,-3,5,-6],[10,-3,-6,-9,-5,3,-3,-1,6,5,-9,-3,6,1,-3,-8,-2,-7,-4,-1,5,6,2,-8,-9,-8,-8,1,6,-7,2,6,-8,10,-7,1,-6,-3,-6,7,-4,2,-5,-7,-6,3,-10,1,10,-10,-2,-1,9,7,5,-1,-8,-10,-7,-5],[1,-10,-5,-9,-2,-3,1,3,10,-7,3,-3,-2,-5,9,-1,-5,1,4,6,10,-2,-5,-3,4,-9,10,9,6,9,3,-6,-3,-10,-7,-4,-10,-8,-9,2,-2,2,5,-4,-5,-4,4,-7,-9,3,5,-4,2,-10,4,-6,-2,-10,10,-8],[6,-1,4,-7,-7,10,10,7,-6,4,-8,6,-9,-9,-10,-3,-10,9,2,-8,8,3,2,9,6,7,2,-7,2,9,4,-10,-6,-10,-5,-9,6,9,1,-5,-1,-4,8,5,9,3,8,8,4,-6,6,-2,-9,-2,10,9,10,6,5,9],[7,-7,-7,1,-3,-10,2,3,6,-2,-3,-10,4,-2,-9,-5,4,1,7,3,-7,-2,7,-10,1,1,-3,-6,9,6,-10,4,2,-5,7,2,-3,5,-10,-4,7,4,8,-8,9,-5,-4,-2,4,7,7,5,4,9,5,4,1,-3,-7,8],[-5,-4,3,7,-5,-9,6,2,4,-3,-7,2,-6,-8,7,8,10,3,9,-3,8,7,-5,-3,10,-7,-4,4,-3,-2,8,-4,-3,-4,-9,-9,10,-1,4,-2,-10,3,8,-2,10,3,6,-8,4,-3,2,2,-7,5,-4,10,-7,-8,10,6],[-5,-8,6,-10,-2,3,-5,4,-7,7,-7,5,-8,7,-2,8,3,6,5,-8,-1,1,-8,-1,-3,6,5,-1,4,-3,-2,2,10,-3,-8,-2,-5,-6,-7,10,5,-9,9,5,10,8,8,9,1,-3,-4,7,-9,6,10,-5,4,-7,-7,-6],[8,-1,5,-4,-2,3,-3,7,3,-7,1,-10,-9,-10,9,1,10,-4,2,1,-9,1,-7,4,-4,-5,-5,2,3,-8,7,-8,3,-4,-3,10,1,2,10,2,-8,-10,3,7,-5,-8,6,9,-9,-6,-8,-2,8,1,-1,3,-9,2,-7,7],[6,4,1,-1,6,3,-6,5,1,1,6,-5,8,-4,-8,7,-6,4,-4,-8,-6,4,-7,5,2,4,-1,2,6,-6,-9,-8,6,2,9,-8,-4,7,1,1,-8,-1,6,8,-9,8,-9,-3,-10,-5,-7,-4,-7,-2,2,10,-2,7,-4,2],[1,-3,8,-7,3,7,-7,10,-1,10,10,3,3,-2,7,2,5,10,1,10,-9,3,8,-10,8,4,2,-9,-7,3,4,2,3,3,-1,-10,-9,-6,8,6,6,5,-7,-2,-5,8,2,-9,4,-1,-4,-7,3,10,9,-9,-7,-2,9,9],[-9,-5,9,-6,-5,-9,-5,2,10,-1,-7,2,7,8,-8,-1,-6,-7,-10,7,7,4,2,4,-7,1,-7,8,6,1,-5,-10,7,-5,10,2,-1,3,-2,5,4,-5,-8,-7,3,10,-10,-10,-10,4,8,-9,-2,-2,9,-6,-5,4,-6,-10],[8,-6,2,5,-10,4,-7,-6,-7,-3,-8,-1,-2,6,7,6,8,6,-7,-6,2,-6,4,7,-10,2,-1,-1,-10,-2,5,-2,3,4,1,-8,9,1,6,7,-10,4,-1,-6,-1,8,10,8,-10,-3,2,5,5,-5,5,7,-10,-7,-5,2],[3,4,1,-7,6,-1,3,-8,-5,-7,4,6,-6,-4,7,-9,-5,-6,-8,-7,-4,3,-6,6,-3,-2,9,-8,10,-6,-8,-9,-1,-1,-9,3,7,-1,-6,-6,1,3,-5,-5,-5,-4,-7,9,-8,-6,7,10,-5,8,-9,-10,2,8,-6,-4],[3,7,-1,-7,5,7,3,7,-10,9,1,8,3,-3,-1,4,-3,4,-5,4,-2,-3,8,-3,7,8,1,1,3,5,-9,8,9,-7,-2,-6,1,9,1,10,6,-6,-5,1,1,2,4,-3,1,-9,2,-7,-9,4,2,8,1,3,2,-4],[9,-4,-3,5,-8,6,2,-5,-4,10,3,2,-3,10,8,-10,-7,9,1,5,-2,1,6,6,-5,8,6,1,-4,7,-2,-10,-9,-8,-4,-4,-6,10,-3,4,3,-5,1,-8,-7,-8,2,-10,6,3,-3,-4,-2,-2,1,4,-7,2,-6,-4]], dtype = "int64")#candidate|4150|(18, 60)|const|int64
call_4149 = relay.TupleGetItem(func_4008_call(relay.reshape(const_4150.astype('int64'), [12, 9, 10]), relay.reshape(const_4150.astype('int64'), [12, 9, 10]), ), 1)
call_4151 = relay.TupleGetItem(func_4012_call(relay.reshape(const_4150.astype('int64'), [12, 9, 10]), relay.reshape(const_4150.astype('int64'), [12, 9, 10]), ), 1)
output = relay.Tuple([call_4110,call_4145,var_4146,call_4149,const_4150,])
output2 = relay.Tuple([call_4111,call_4147,var_4146,call_4151,const_4150,])
func_4161 = relay.Function([var_4146,], output)
mod['func_4161'] = func_4161
mod = relay.transform.InferType()(mod)
mutated_mod['func_4161'] = func_4161
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4162 = relay.var("var_4162", dtype = "float32", shape = (468,))#candidate|4162|(468,)|var|float32
func_4161_call = mutated_mod.get_global_var('func_4161')
call_4163 = func_4161_call(var_4162)
output = call_4163
func_4164 = relay.Function([var_4162], output)
mutated_mod['func_4164'] = func_4164
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4192 = relay.var("var_4192", dtype = "int8", shape = (12, 12, 11))#candidate|4192|(12, 12, 11)|var|int8
var_4193 = relay.var("var_4193", dtype = "int8", shape = (12, 12, 11))#candidate|4193|(12, 12, 11)|var|int8
bop_4194 = relay.multiply(var_4192.astype('int8'), relay.reshape(var_4193.astype('int8'), relay.shape_of(var_4192))) # shape=(12, 12, 11)
func_3766_call = mod.get_global_var('func_3766')
func_3769_call = mutated_mod.get_global_var('func_3769')
var_4205 = relay.var("var_4205", dtype = "float32", shape = (832,))#candidate|4205|(832,)|var|float32
call_4204 = func_3766_call(relay.reshape(var_4205.astype('float32'), [13, 8, 8]))
call_4206 = func_3766_call(relay.reshape(var_4205.astype('float32'), [13, 8, 8]))
func_3483_call = mod.get_global_var('func_3483')
func_3485_call = mutated_mod.get_global_var('func_3485')
call_4208 = relay.TupleGetItem(func_3483_call(), 0)
call_4209 = relay.TupleGetItem(func_3485_call(), 0)
func_371_call = mod.get_global_var('func_371')
func_374_call = mutated_mod.get_global_var('func_374')
const_4220 = relay.const([True,True,True,False,False,True,False,True,True,True,True,False,True,False,True,False,False,False,False,True,False,True,False,True,True,False,False,True,True,False,False,False,False,True,False,False,False,False,True,True,False,False,True,True,True,False,True,True,False,True,False,False,False,False,True,True,False,False,True,True,False,True,True,False,False,True,False,False,False,True,True,False,False,False,True,True,True,False,False,True,True,False,False,True,True,True,True,True,True,False,True,False,True,False,False,True,False,True,True,False,False,False,False,False,False,True,True,True,True,True,True,False,False,True,True,True,False,False,False,False,False,True,False,True,False,False,False,False,True,True,False,False,True,False,False,False,True,False,True,False,True,False,False,True,True,True,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,True,True,False,True,True,False,True,True,True,True,True,False,True,True,True,True,True,True,True,True,False,True,False,False,True,False,True,True,True,True,False,True,True,False,False,False,False,True,False,False,False,True,False,True,False,True,False,True,False,True,True,False,True,True,True,False,True,False,False,False,True,False,True,False,False,True,True,True,True,True,True,True,False,True,True,False,False,True,True,False,True,False,True,False,True,False,False,False,False,False,True,True,False,False,False,True,False,True,False,True,False,True,False,False,False,True,False,False,True,True,False,False,False,True,False,True,True,False,False,True,True,True,True,True,True,True,False,True,False,False,False,False,True,True,False,True,False,False,True,True,True,False,True,True,True,True,True,True,False,True,False,True,False,True,False,True,False,True,True,False,True,True,False,True,False,False,False,True,False,False,False,False,False,False,True,True,True,False,False,True,True,True,False,True,False,True,True,True,False,False,True,True,True,False,False,False,False,True,True,True,True,True,True,True,True,False,False,True,True,True,False,False,False,True,False,False,False,True,True,False,True,True,True,False,True,False,False,True,True,True,False,False,True,True,True,False,False,True,True,True,False,False,True,False,True,True,True,True,False,False,True,True,True,False,False,False,False,False,False,True,False,False,True,True,False,False,True,False,False,True,True,False,True,False,True,False,False,False,True,False,False,False,False,False,False,False,False,True,False,False,False,False,True,False,True,True,False,True,True,False,False,False,True,True,False,False,True,False,False,False,True,False,False,True,False,False,True,True,True,True,True,False,False,False,False,True,True,False,False,False,True,False,False,False,True,True,False,False,True,False,False,False,False,False,True,True,True,False,False,False,False,True,False,False,False,False,True,True,True,False,False,False,False,False,False,False,True,False,False,True,False,True,True,False,True,True,True,False,True,True,True,True,True,True,True,True,False,True,False,True,True,False,True,True,True,True,True,False,True,False,True,True,True,True,True,False,False,True,True,True,False,False,True,True,True,False,False,True,True,True,False,False,True,True,False,False,False,True,True,True,True,False,False,False,True,False,True,True,True,False,True,True,False,False,True,True,False,True,True,False,False,True,False,False,True,False,False,True,False,True,True,True,False,True,False,True,True,True,True,False,True,False,False,True,False,True,False,False,False,True,False,True,True,True,True,False,True,True,True,True,True,False,True,True,False,True,False,True,False,True,False,True,True,False,False,True,True,False,False,True,False,False,False,True,True,True,True,True,True,False,False,False,True,True,True,True,False,True,False,False,True,False,True,False,False,True,False,True,False,False,True,False,False,True,True,False,True,False,True,False,False,True,False,True,True,True,False,True,False,True,False,True,True,True,False,False,True,False,True,True,False,False,True,False,False,False,False,True,False,True,True,False,True,True,False,False,False,False,True,False,True,True,False,True,True,False,True,False,False,False,True,False,True,False,False,True,False,True,False,False,False,True,False,True,False,False,True,False,True,True,False,False,False,False,True,True,False,False,True,False,True,False,False,False,False,True,True,False,False,True,False,False,False,True,False,False,True,True,False,False,False,False,True,True,True,False,False,True,True,False,False,False,False,False,False,True,True,True,True,True,False,False,False,False,True,False,False,False,True,False,True,False,False,False,True,True,False,True,True,True,True,True,True,False,True,True,True,True,False,False,False,False,False,False,False,True,False,False,False,False,False,True,False,True,True,True,False,True,False,True,True,False,False,False,False,False,False,True,True,False,True,True,True,False,False,True,True,False,False,True,False,False,False,False,True,True,True,False,True,False,True,False,False,False,False,False,False,False,True,True,True,False,False,False,False,False,True,False,True,True,True,True,False,False,False,True,True,True,True,False,True,True,False,True,True,True,True,True,True,False,False,False,True,False,False,True,True,False,True,False,True,True,True,True,True,True,True,False,True,False,True,False,True,True,False,False,False,True,True,False,False,True,False,True,False,True,False,True,True,False,True,False,True,False,False,False,False,True,False,True,True,True,True,True,True,True,True,True,True,True,True,True,False,False,False,False,True,False,True,False,False,False,False,True,True,False,True,True,True,False,False,True,True,True,False,False,True,True,False,False,False,True,True,True,True,True,True,False,True,True,False,False,True,True,True,False,True,True,True,True,True,True,False,False,True,False,True,False,True,True,False,False,False,True,True,False,False,False,False,True,True,True,True,True,False,True,True,True,False,True,False,True,False,False,True,True,False,False,True,False,True,True,False,False,False,True,False,False,True,False,False,True,True,True,False,True,False,True,True,False,False,True,True,True,False,True,False,False,True,False,False,True,True,False,True,False,True,True,False,True,True,False,False,True,False,False,False,False,True,True,True,False,True,False,True,True,True,True,True,True,True,False,False,True,False,True,True,False,False,True,True,True,False,True,False,False,True,True,False,False,False,True,False,True,False,True,False,True,True,False,False,False,False,False,True,False,True,False,False,True,False,True,True,False,False,True,False,True,False,False,False,True,False,False,False,False,False,True,True,True,True,False,True,True,False,True,True,False,True,False,True,True,True,False,True,False,False,True,True,False,False,True,True,False,False,False,False,False,True,True,True,False,True,False,True,False,True,False,False,True,False,True,False,False,False,False,False,False,True,True,False,True,True,False,True,True,False,True,True,True,True,False,True,False,False,False,False,False,False,False,True,True,False,True,True,False,True,True,False,True,False,False,False,True,False,False,False,False,True,True,True,False,True,False,True,False,False,True,False,True,False,True,False,False,False,True,False,False,False,False,True,False,False,True,False,True,True,False,True,True,False,True,True,True,True,False,True,False,False,True,True,False,False,True,False,True,False,False,True,False,False,False,False,False,True,False,True,True,True,True,False,True,False,True,False,True,False,False,True,False,True,False,False,False,True,False,True,True,False,False,True,False,False,False,False,True,False,False,False,True,True,False,False,True,False,True,False,False,True,False,False,False,False,False,False,False,False,True,True,False,True,True,False,True,True,False,True,True,False,True,True,True,False,True,False,False,False,True,False,True,True,False,False,True,False,False,True,False,False,True,False,True,False,False,True,True,False,False,False,True,True,True,False,True,True,True,True,True,False,True,True,True,True,True,False,True,True,False,True,True,True,True,True,True,True,False,False,False,False,False,True,True,False,True,True,True,False,False,False,False,False,True,True,True,False,False,True,False,False,False,True,True,False,False,False,True,False,False,True,False,False,False,False,False,False,True,True,False,True,False,True,True,True,False,True,False,False,False,False,False,False,True,True,False,False,True,False,False,True,True,True,False,False,True,False,False,False,False,False,True,False,True,True,True,False,False,True,False,False,True,True,False,True,False,True,True,False,True,True,True,False,False,True,False,True,False,False,True,False,True,True,False,False,False,True,False,False,True,True,False,False,False,False,True,False,True,False,False,False,False,False,True,False,True,True,False,True,False,True,True,True,False,True,True,False,True,False,False,False,True,False,False,True,True,False,True,False,False,False,True,False,False,False,True,True,True,True,True,True,False,False,False,True,False,False,True,True,False,False,True,True,False,True,False,True,True,True,False,False,True,True,False,True,True,True,True,False,False,False,False,True,False,False,False,False,False,True,True,False,True,False,True,False,False,True,True,True,True,True,True,False,False,False,False,True,True,True,False,False,True,False,True,True,False,True,False,True,False,True,True,False,False,True,False,False,False,True,True,True,True,True,False,True,True,False,True,False,True,True,False,False,True,True,True,True,False,True,False,True,True,False,True,True,True,True,True,True,False,False,True,True,True,True,True,False,True,False,True,False,True,True,False,False,True,True,True,True,True,False,False,False,False,True,True,True,False,False,False,True,False,True,False,False,False,True,False,True,True,True,True,False,True,True,False,False,True,False,True,False,False,False,False,False,True,True,True,False,True,True,True,True,True,True,True,True,True,False,True,False,True,False,True,False,False,True,False,True,True,False,True,True,False,True,True,True,False,False,True,True,False,False,False,True,False,False,False,True,False,True,True,True,False,False,False,False,False,False,True,True,False,False,True,False,True,False,False,True,True,True,False,True,False,False,False,False,False,False,True,False,False,False,False,False,True,False,False,True,False,True,False,True,True,True,True,False,False,True,True,True,True,True,False,True,True,False,True,False,False,False,False,False,False,False,False,True,False,False,False,True,True,True,False,False,False,True,False,False,True,True,True,False,False,True,True,False,True,False,False,False,False,False,False,False,True,True,False,True,True,False,False,True,True,False,True,False,False,False,False,True,True,False,True,False,True,False,False,True,False,False,True,False,False,True,False,True,False,False,True,False,True,True,True,False,False,False,False,False,False,True,True,False,True,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,True,True,False,False,False,True,False,False,False,True,False,False,False,True,False,True,True,False,True,True,False,True,True,False,True,True,True,True,False,True,False,True,False,False,True,False,False,True,True,False,False,True,False,False,True,True,True,False,True,True,False,False,False,True,False,True,True,True,True,True,False,True,False,False,True,True,True,True,False,False,True,True,True,False,True,False,True,True,True,False,False,True,False,False,False,True,True,True,False,False,False,True,True,False,True,True,True,False,False,False,False,False,True,False,False,False,False,True,True,True,True,True,False,False,True,True,True,True,False,True,True,True,False,True,True,False,False,True,False,False,True,True,False,False,True,False,False,True,True,False,True,True,True,True,True,True,False,False,False,True,True,True,False,False,False,True,False,False,False,False,True,True,True,True,True,False,False,False,False,True,False,True,False,True,False,True,False,True,True,False,False,True,False,False,True,False,True,True,True,False,True,False,True,True,True,True,True,True,True,True,True,True,False,True,False,True,True,True,False,False,True,False,True,True,False,False,False,True,True,True,True,True,True,True,False,False,False,True,False,True,True,True,False,True,False,False,False,True,True,False,False,True,False,True,False,False,False,False,False,True,True,True,False,False,False,False,True,False,False,True,True,True,False,True,False,False,False,True,False,True,True,False,False,False,True,True,False,True,True,False,True,True,False,True,True,False,False,False,True,False,True,False,True,True,False,True,False,False,False,False,True,False,False,False,False,True,True,False,True,False,True,False,True,True,True,True,True,True,True,False,True,True,True,False,False,True,False,False,True,False,False,False,False,False,False,False,False,True,True,True,False,False,True,True,True,False,False,False,False,False,True,True,True,False,False,True,True,False,False,False,False,False,False,True,True,True,True,True,False,False,False,False,False,True,False,True,True,False,False,True,False,True,True,True,True,True,True,False,True,True,False,True,True,False,False,False,True,False,True,False,False,True,False,True,False,False,False,False,True,False,True,True,True,False,True,False,True,False,False,False,True,False,False,False,True,False,True,False,False,False,False,True,False,True,False,False,True,False,False,False,True,False,False,False,False,True,True,False,True,True,False,False,False,False,False,True,True,True,True,True,False,False,False,False,True,False,False,False,True,True,True,False,True,True,False,True,False,True,True,True,True,False,True,True,False,True,False,True,True,True,True,True,True,True,True,False,False,True,True,True,False,False,True,True,True,True,True,True,True,False,False,False,False,True,True,True,False,True,False,True,False,True,False,False,True,True,False,True,True,True,False,True,True,True,True,False,False,False,True,True,False,True,True,True,False,False,False,True,True,False,False,False,False,True,False,True,False,False,False,True,False,False,True,True,True,False,False,True,False,True,True,False,True,False,True,True,True,True,False,False,False,True,False,False,False,False,True,False,True,True,False,True,True,True,False,False,True,False,True,True,False,False,True,True,True,True,False,False,False,True,False,False,False,True,False,False,True,True,False,False,False,False,True,True,True,False,True,False,False,True,True,False,True,True,True,False,False,False,False,False,True,True,True,True,False,True,True,True,True,True,False,True,False,True,True,True,True,False,False,False,True,True,False,True,False,False,True,False,False,False,True,True,True,False,False,True,True,True,False,False,False,False,False,False,False,True,False,True,True,False,True,True,True,False,False,False,False,True,False,False,True,True,True,False,True,True,True,True,False,False,True,False,False,True,True,False,False,True,False,False,True,True,True,False,True,True,False,True,False,True,True,False,False,False,False,False,True,False,True,True,False,False,False,False,False,True,True,False,False,True,False,True,False,True,True,False,False,False,True,True,True,True,True,True,True,True,True,True,True,False,False,True,True,False,False,True,True,True,True,True,False,False,False,False,True,False,False,False,False,False,True,True,True,False,False,False,True,False,True,True,False,False,False,True,False,False,False,False,True,False,True,True,False,False,False,True,False,False,True,False,False,False,True,True,False,True,False,False,True,True,True,False,True,True,True,False,False,False,False,True,False,True,True,False,True,True,True,True,True,True,True,False,True,False,True,False,False,True,False,True,True,True,True,False,False,True,False,False,True,False,False,True,False,True,True,True,False,False,True,True,True,False,True,True,True,True,True,True,False,True,False,True,False,False,False,False,True,False,True,False,True,True], dtype = "bool")#candidate|4220|(2925,)|const|bool
call_4219 = func_371_call(relay.reshape(const_4220.astype('bool'), [13, 15, 15]), relay.reshape(const_4220.astype('bool'), [13, 15, 15]), )
call_4221 = func_371_call(relay.reshape(const_4220.astype('bool'), [13, 15, 15]), relay.reshape(const_4220.astype('bool'), [13, 15, 15]), )
output = relay.Tuple([bop_4194,call_4204,var_4205,call_4208,call_4219,const_4220,])
output2 = relay.Tuple([bop_4194,call_4206,var_4205,call_4209,call_4221,const_4220,])
func_4224 = relay.Function([var_4192,var_4193,var_4205,], output)
mod['func_4224'] = func_4224
mod = relay.transform.InferType()(mod)
var_4225 = relay.var("var_4225", dtype = "int8", shape = (12, 12, 11))#candidate|4225|(12, 12, 11)|var|int8
var_4226 = relay.var("var_4226", dtype = "int8", shape = (12, 12, 11))#candidate|4226|(12, 12, 11)|var|int8
var_4227 = relay.var("var_4227", dtype = "float32", shape = (832,))#candidate|4227|(832,)|var|float32
output = func_4224(var_4225,var_4226,var_4227,)
func_4228 = relay.Function([var_4225,var_4226,var_4227,], output)
mutated_mod['func_4228'] = func_4228
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3859_call = mod.get_global_var('func_3859')
func_3861_call = mutated_mod.get_global_var('func_3861')
call_4230 = relay.TupleGetItem(func_3859_call(), 0)
call_4231 = relay.TupleGetItem(func_3861_call(), 0)
output = call_4230
output2 = call_4231
func_4250 = relay.Function([], output)
mod['func_4250'] = func_4250
mod = relay.transform.InferType()(mod)
mutated_mod['func_4250'] = func_4250
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4250_call = mutated_mod.get_global_var('func_4250')
call_4251 = func_4250_call()
output = call_4251
func_4252 = relay.Function([], output)
mutated_mod['func_4252'] = func_4252
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3859_call = mod.get_global_var('func_3859')
func_3861_call = mutated_mod.get_global_var('func_3861')
call_4256 = relay.TupleGetItem(func_3859_call(), 0)
call_4257 = relay.TupleGetItem(func_3861_call(), 0)
output = call_4256
output2 = call_4257
func_4266 = relay.Function([], output)
mod['func_4266'] = func_4266
mod = relay.transform.InferType()(mod)
output = func_4266()
func_4267 = relay.Function([], output)
mutated_mod['func_4267'] = func_4267
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3483_call = mod.get_global_var('func_3483')
func_3485_call = mutated_mod.get_global_var('func_3485')
call_4278 = relay.TupleGetItem(func_3483_call(), 0)
call_4279 = relay.TupleGetItem(func_3485_call(), 0)
func_2623_call = mod.get_global_var('func_2623')
func_2626_call = mutated_mod.get_global_var('func_2626')
var_4287 = relay.var("var_4287", dtype = "float32", shape = (288,))#candidate|4287|(288,)|var|float32
call_4286 = relay.TupleGetItem(func_2623_call(relay.reshape(var_4287.astype('float32'), [288,])), 0)
call_4288 = relay.TupleGetItem(func_2626_call(relay.reshape(var_4287.astype('float32'), [288,])), 0)
uop_4300 = relay.cosh(call_4286.astype('float32')) # shape=(15, 15, 10)
uop_4302 = relay.cosh(call_4288.astype('float32')) # shape=(15, 15, 10)
output = relay.Tuple([call_4278,var_4287,uop_4300,])
output2 = relay.Tuple([call_4279,var_4287,uop_4302,])
func_4310 = relay.Function([var_4287,], output)
mod['func_4310'] = func_4310
mod = relay.transform.InferType()(mod)
mutated_mod['func_4310'] = func_4310
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4311 = relay.var("var_4311", dtype = "float32", shape = (288,))#candidate|4311|(288,)|var|float32
func_4310_call = mutated_mod.get_global_var('func_4310')
call_4312 = func_4310_call(var_4311)
output = call_4312
func_4313 = relay.Function([var_4311], output)
mutated_mod['func_4313'] = func_4313
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4333 = relay.var("var_4333", dtype = "uint32", shape = ())#candidate|4333|()|var|uint32
var_4334 = relay.var("var_4334", dtype = "uint32", shape = (3, 1, 4))#candidate|4334|(3, 1, 4)|var|uint32
bop_4335 = relay.greater(var_4333.astype('bool'), var_4334.astype('bool')) # shape=(3, 1, 4)
bop_4343 = relay.floor_divide(var_4333.astype('float64'), bop_4335.astype('float64')) # shape=(3, 1, 4)
output = relay.Tuple([bop_4343,])
output2 = relay.Tuple([bop_4343,])
func_4346 = relay.Function([var_4333,var_4334,], output)
mod['func_4346'] = func_4346
mod = relay.transform.InferType()(mod)
mutated_mod['func_4346'] = func_4346
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4346_call = mutated_mod.get_global_var('func_4346')
var_4348 = relay.var("var_4348", dtype = "uint32", shape = ())#candidate|4348|()|var|uint32
var_4349 = relay.var("var_4349", dtype = "uint32", shape = (3, 1, 4))#candidate|4349|(3, 1, 4)|var|uint32
call_4347 = func_4346_call(var_4348,var_4349,)
output = call_4347
func_4350 = relay.Function([var_4348,var_4349,], output)
mutated_mod['func_4350'] = func_4350
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2899_call = mod.get_global_var('func_2899')
func_2900_call = mutated_mod.get_global_var('func_2900')
call_4364 = relay.TupleGetItem(func_2899_call(), 1)
call_4365 = relay.TupleGetItem(func_2900_call(), 1)
func_3351_call = mod.get_global_var('func_3351')
func_3353_call = mutated_mod.get_global_var('func_3353')
call_4391 = relay.TupleGetItem(func_3351_call(), 0)
call_4392 = relay.TupleGetItem(func_3353_call(), 0)
func_3332_call = mod.get_global_var('func_3332')
func_3335_call = mutated_mod.get_global_var('func_3335')
call_4393 = relay.TupleGetItem(func_3332_call(relay.reshape(call_4391.astype('float32'), [78, 6])), 2)
call_4394 = relay.TupleGetItem(func_3335_call(relay.reshape(call_4391.astype('float32'), [78, 6])), 2)
func_3332_call = mod.get_global_var('func_3332')
func_3335_call = mutated_mod.get_global_var('func_3335')
call_4416 = relay.TupleGetItem(func_3332_call(relay.reshape(call_4391.astype('float32'), [78, 6])), 2)
call_4417 = relay.TupleGetItem(func_3335_call(relay.reshape(call_4391.astype('float32'), [78, 6])), 2)
var_4432 = relay.var("var_4432", dtype = "float32", shape = (78, 6))#candidate|4432|(78, 6)|var|float32
bop_4433 = relay.less_equal(call_4393.astype('bool'), relay.reshape(var_4432.astype('bool'), relay.shape_of(call_4393))) # shape=(78, 6)
bop_4436 = relay.less_equal(call_4394.astype('bool'), relay.reshape(var_4432.astype('bool'), relay.shape_of(call_4394))) # shape=(78, 6)
func_3694_call = mod.get_global_var('func_3694')
func_3696_call = mutated_mod.get_global_var('func_3696')
call_4448 = func_3694_call()
call_4449 = func_3694_call()
output = relay.Tuple([call_4364,call_4391,call_4416,bop_4433,call_4448,])
output2 = relay.Tuple([call_4365,call_4392,call_4417,bop_4436,call_4449,])
func_4450 = relay.Function([var_4432,], output)
mod['func_4450'] = func_4450
mod = relay.transform.InferType()(mod)
var_4451 = relay.var("var_4451", dtype = "float32", shape = (78, 6))#candidate|4451|(78, 6)|var|float32
output = func_4450(var_4451)
func_4452 = relay.Function([var_4451], output)
mutated_mod['func_4452'] = func_4452
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4088_call = mod.get_global_var('func_4088')
func_4090_call = mutated_mod.get_global_var('func_4090')
call_4459 = relay.TupleGetItem(func_4088_call(), 2)
call_4460 = relay.TupleGetItem(func_4090_call(), 2)
output = call_4459
output2 = call_4460
func_4464 = relay.Function([], output)
mod['func_4464'] = func_4464
mod = relay.transform.InferType()(mod)
output = func_4464()
func_4465 = relay.Function([], output)
mutated_mod['func_4465'] = func_4465
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3483_call = mod.get_global_var('func_3483')
func_3485_call = mutated_mod.get_global_var('func_3485')
call_4484 = relay.TupleGetItem(func_3483_call(), 0)
call_4485 = relay.TupleGetItem(func_3485_call(), 0)
func_842_call = mod.get_global_var('func_842')
func_847_call = mutated_mod.get_global_var('func_847')
var_4493 = relay.var("var_4493", dtype = "float64", shape = (112,))#candidate|4493|(112,)|var|float64
call_4492 = relay.TupleGetItem(func_842_call(relay.reshape(var_4493.astype('float64'), [4, 4, 7]), relay.reshape(var_4493.astype('float64'), [4, 4, 7]), relay.reshape(call_4484.astype('float32'), [1, 468]), ), 1)
call_4494 = relay.TupleGetItem(func_847_call(relay.reshape(var_4493.astype('float64'), [4, 4, 7]), relay.reshape(var_4493.astype('float64'), [4, 4, 7]), relay.reshape(call_4484.astype('float32'), [1, 468]), ), 1)
func_3794_call = mod.get_global_var('func_3794')
func_3795_call = mutated_mod.get_global_var('func_3795')
call_4497 = relay.TupleGetItem(func_3794_call(), 0)
call_4498 = relay.TupleGetItem(func_3795_call(), 0)
var_4508 = relay.var("var_4508", dtype = "bool", shape = (12, 13, 3))#candidate|4508|(12, 13, 3)|var|bool
bop_4509 = relay.greater_equal(call_4492.astype('bool'), relay.reshape(var_4508.astype('bool'), relay.shape_of(call_4492))) # shape=(12, 13, 3)
bop_4512 = relay.greater_equal(call_4494.astype('bool'), relay.reshape(var_4508.astype('bool'), relay.shape_of(call_4494))) # shape=(12, 13, 3)
var_4515 = relay.var("var_4515", dtype = "bool", shape = (12, 13, 3))#candidate|4515|(12, 13, 3)|var|bool
bop_4516 = relay.bitwise_or(var_4508.astype('uint64'), relay.reshape(var_4515.astype('uint64'), relay.shape_of(var_4508))) # shape=(12, 13, 3)
output = relay.Tuple([call_4484,var_4493,call_4497,bop_4509,bop_4516,])
output2 = relay.Tuple([call_4485,var_4493,call_4498,bop_4512,bop_4516,])
func_4519 = relay.Function([var_4493,var_4508,var_4515,], output)
mod['func_4519'] = func_4519
mod = relay.transform.InferType()(mod)
var_4520 = relay.var("var_4520", dtype = "float64", shape = (112,))#candidate|4520|(112,)|var|float64
var_4521 = relay.var("var_4521", dtype = "bool", shape = (12, 13, 3))#candidate|4521|(12, 13, 3)|var|bool
var_4522 = relay.var("var_4522", dtype = "bool", shape = (12, 13, 3))#candidate|4522|(12, 13, 3)|var|bool
output = func_4519(var_4520,var_4521,var_4522,)
func_4523 = relay.Function([var_4520,var_4521,var_4522,], output)
mutated_mod['func_4523'] = func_4523
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4250_call = mod.get_global_var('func_4250')
func_4252_call = mutated_mod.get_global_var('func_4252')
call_4532 = func_4250_call()
call_4533 = func_4250_call()
func_4008_call = mod.get_global_var('func_4008')
func_4012_call = mutated_mod.get_global_var('func_4012')
const_4535 = relay.const([1,-2,1,-5,10,-7,6,-4,2,6,6,5,-1,-7,6,-4,9,8,-10,5,4,-10,2,7,-7,4,-7,9,1,9,-5,-4,9,-8,-6,-10,5,-9,5,2,9,5,6,3,9,-7,-5,3,-5,-2,4,-1,3,7,-8,-1,-5,-4,-2,10,-9,8,-8,-7,-1,-5,-10,-3,8,2,-9,6,9,6,-9,3,-3,-3,1,3,-8,5,7,-10,10,-5,-4,6,3,5,8,3,10,-2,5,-10,-6,-10,7,-7,3,-7,-3,10,-6,-9,4,6,7,4,-5,-6,3,3,-7,6,-4,-6,-7,4,-3,8,6,-3,5,-8,4,-3,-1,7,-1,-5,8,-4,8,-10,3,-10,5,-6,1,-1,8,-9,2,-5,9,-8,3,-3,9,4,3,-3,-7,9,2,2,3,9,9,8,5,-6,7,-1,-5,10,-9,8,-1,4,6,5,7,-5,-9,-4,-9,5,2,-2,-1,6,-5,-7,-9,2,-7,5,3,2,-2,-8,-9,-5,-9,7,-7,-1,7,-9,-9,2,-7,1,8,2,2,-9,3,1,2,5,10,2,-5,4,3,1,-6,2,8,1,5,10,-7,1,10,9,-3,-7,-3,2,10,9,-6,9,-6,3,-2,9,-5,-9,8,4,8,-10,6,-8,-3,-4,10,2,-4,9,-7,7,1,-4,-1,-8,2,1,-10,-6,-8,4,4,5,-1,5,-3,10,8,10,-4,10,8,6,10,3,-2,7,-10,-3,-7,9,-3,-3,-4,-10,-5,4,2,1,4,4,-8,-10,-5,3,1,3,2,-5,-1,5,-7,-9,-1,-5,-4,-10,9,-5,5,8,2,2,-9,8,-3,-6,-4,-3,7,1,-6,8,-1,2,2,1,-1,-6,9,-10,9,-3,3,9,4,3,-8,-7,-5,4,1,9,-8,4,-1,10,-2,-4,-10,7,10,6,-3,9,-6,-7,-8,-10,-3,6,1,-5,-10,8,-3,-4,6,-3,6,9,4,-8,-2,1,-5,1,-2,8,9,-1,-4,-5,6,-1,1,4,-8,2,-5,7,-9,-5,-7,4,-1,-6,10,5,-3,-10,-8,2,1,6,-6,-5,3,7,-4,-6,5,-2,-5,-3,-3,3,-9,7,-8,5,8,-10,-9,1,-9,8,8,9,7,4,-4,3,-1,-5,-7,-4,8,6,-10,-3,-3,-2,-1,6,2,-9,-8,-2,-5,9,-7,7,-6,5,9,6,-8,-4,-9,6,2,-8,8,-1,-6,4,-5,9,3,7,1,-3,2,-8,10,2,9,-4,1,9,8,-3,4,2,7,7,-5,-8,10,5,2,-3,9,-8,-5,-8,-2,-5,2,-2,-9,8,1,-8,-4,2,2,6,5,10,1,-4,-10,9,-6,-2,10,-6,7,-6,9,-6,-5,2,6,-3,-1,-2,-4,2,2,3,-5,-4,5,5,10,-4,-2,7,8,7,-5,-10,-9,-10,-8,2,-4,-6,-8,2,2,3,2,-4,-9,8,9,4,-10,-9,-7,-2,9,9,-8,-7,7,-4,9,-9,-8,-4,-7,-5,1,7,-4,1,6,-3,1,5,-10,-8,9,-1,6,-4,-2,-10,-2,2,-4,7,3,6,-2,5,-2,-4,2,-9,-9,-9,-3,-5,-6,9,2,-3,8,10,-2,3,-7,6,10,-8,-2,9,10,10,-3,-7,7,-9,-9,6,-3,5,3,1,-1,-2,8,8,-7,3,7,4,-1,-10,1,4,-4,4,-4,-3,-4,8,8,9,2,7,5,5,4,10,1,7,-5,-5,6,4,4,-1,5,10,-3,9,8,-5,1,-8,-9,10,-8,3,-2,1,6,-10,3,10,-9,-5,5,1,-5,-8,8,8,-2,7,5,-2,3,2,4,-1,1,9,-5,-1,1,-7,-7,2,-4,-5,-10,-2,1,-6,-5,5,4,3,-4,2,-2,-4,-1,-10,7,6,4,-10,-3,9,7,6,-8,1,-1,-7,1,4,8,-1,-1,6,-6,-2,5,4,3,-3,9,3,8,-5,-3,-3,4,8,10,3,-2,-4,4,1,8,-8,-10,6,-3,9,9,7,-5,-1,10,-10,8,-9,1,-2,4,7,3,3,6,1,3,1,6,-2,7,-9,5,-7,-8,9,-9,9,2,9,4,-5,10,5,-9,2,-1,9,9,-6,5,2,-10,7,2,1,-5,-5,2,1,-8,-7,4,-9,-4,-1,-8,4,-3,-1,-4,-3,9,-4,-9,-4,7,-8,-9,-3,9,3,-6,-7,-7,-4,-1,2,4,-10,-10,-9,-8,-8,-3,-2,-3,-2,-2,-10,7,2,10,7,9,-6,-4,7,-4,-8,4,-1,-5,-9,-4,-7,-10,1,4,-5,-7,-3,-6,4,-7,-8,4,-9,-4,7,-5,1,5,7,-1,-2,3,-3,8,-10,-10,6,-8,3,5,-10,-8,8,-4,-3,-9,-7,-2,1,6,5,-10,9,7,-7,-6,3,-9,-7,9,-10,-5,-1,5,-7,3,-6,4,-10,9,-3,4,7,10,8,4,-6,-5,7,10,1,-7,-6,-2,2,-4,6,-3,-3,9,-10,9,3,4,-2,-4,-8,9,2,2,5,-8,-6,-8,-4,10,1,2,1,-3,-8,7,-8,2,10,-5,-10,9,-6,4,-3,5,-2,-7,-3,-8,-9,-9,-1,-8,-4,7,-6,1,3,-1,10,10,3,6,8,-6,-9,6,7,3,7,-7,-6,4,-6,6,10,-9,-1,-8,-1,8,1,-1,7,10,-4,6,7,-1,-6,-10,-1,1,6,-3,-6,-8,-6,-3,-5,-7,-2,-10,3,-4,6,-5,-5,-1,8,9,-6,8,7,4,-6,2,-6,-9,-4,9,-8,-9,3,-5,3,-2,2,2,3], dtype = "int64")#candidate|4535|(1080,)|const|int64
call_4534 = relay.TupleGetItem(func_4008_call(relay.reshape(const_4535.astype('int64'), [12, 9, 10]), relay.reshape(const_4535.astype('int64'), [12, 9, 10]), ), 0)
call_4536 = relay.TupleGetItem(func_4012_call(relay.reshape(const_4535.astype('int64'), [12, 9, 10]), relay.reshape(const_4535.astype('int64'), [12, 9, 10]), ), 0)
func_3461_call = mod.get_global_var('func_3461')
func_3462_call = mutated_mod.get_global_var('func_3462')
call_4540 = relay.TupleGetItem(func_3461_call(), 1)
call_4541 = relay.TupleGetItem(func_3462_call(), 1)
output = relay.Tuple([call_4532,call_4534,const_4535,call_4540,])
output2 = relay.Tuple([call_4533,call_4536,const_4535,call_4541,])
func_4549 = relay.Function([], output)
mod['func_4549'] = func_4549
mod = relay.transform.InferType()(mod)
mutated_mod['func_4549'] = func_4549
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4549_call = mutated_mod.get_global_var('func_4549')
call_4550 = func_4549_call()
output = call_4550
func_4551 = relay.Function([], output)
mutated_mod['func_4551'] = func_4551
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3526_call = mod.get_global_var('func_3526')
func_3528_call = mutated_mod.get_global_var('func_3528')
call_4730 = func_3526_call()
call_4731 = func_3526_call()
func_3437_call = mod.get_global_var('func_3437')
func_3439_call = mutated_mod.get_global_var('func_3439')
call_4734 = func_3437_call()
call_4735 = func_3437_call()
output = relay.Tuple([call_4730,call_4734,])
output2 = relay.Tuple([call_4731,call_4735,])
func_4738 = relay.Function([], output)
mod['func_4738'] = func_4738
mod = relay.transform.InferType()(mod)
mutated_mod['func_4738'] = func_4738
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4738_call = mutated_mod.get_global_var('func_4738')
call_4739 = func_4738_call()
output = call_4739
func_4740 = relay.Function([], output)
mutated_mod['func_4740'] = func_4740
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3302_call = mod.get_global_var('func_3302')
func_3303_call = mutated_mod.get_global_var('func_3303')
call_4750 = relay.TupleGetItem(func_3302_call(), 0)
call_4751 = relay.TupleGetItem(func_3303_call(), 0)
output = relay.Tuple([call_4750,])
output2 = relay.Tuple([call_4751,])
func_4752 = relay.Function([], output)
mod['func_4752'] = func_4752
mod = relay.transform.InferType()(mod)
mutated_mod['func_4752'] = func_4752
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4752_call = mutated_mod.get_global_var('func_4752')
call_4753 = func_4752_call()
output = call_4753
func_4754 = relay.Function([], output)
mutated_mod['func_4754'] = func_4754
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3794_call = mod.get_global_var('func_3794')
func_3795_call = mutated_mod.get_global_var('func_3795')
call_4768 = relay.TupleGetItem(func_3794_call(), 0)
call_4769 = relay.TupleGetItem(func_3795_call(), 0)
output = call_4768
output2 = call_4769
func_4773 = relay.Function([], output)
mod['func_4773'] = func_4773
mod = relay.transform.InferType()(mod)
mutated_mod['func_4773'] = func_4773
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4773_call = mutated_mod.get_global_var('func_4773')
call_4774 = func_4773_call()
output = call_4774
func_4775 = relay.Function([], output)
mutated_mod['func_4775'] = func_4775
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4549_call = mod.get_global_var('func_4549')
func_4551_call = mutated_mod.get_global_var('func_4551')
call_4868 = relay.TupleGetItem(func_4549_call(), 3)
call_4869 = relay.TupleGetItem(func_4551_call(), 3)
output = relay.Tuple([call_4868,])
output2 = relay.Tuple([call_4869,])
func_4917 = relay.Function([], output)
mod['func_4917'] = func_4917
mod = relay.transform.InferType()(mod)
mutated_mod['func_4917'] = func_4917
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4917_call = mutated_mod.get_global_var('func_4917')
call_4918 = func_4917_call()
output = call_4918
func_4919 = relay.Function([], output)
mutated_mod['func_4919'] = func_4919
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3194_call = mod.get_global_var('func_3194')
func_3195_call = mutated_mod.get_global_var('func_3195')
call_4945 = func_3194_call()
call_4946 = func_3194_call()
output = call_4945
output2 = call_4946
func_4958 = relay.Function([], output)
mod['func_4958'] = func_4958
mod = relay.transform.InferType()(mod)
output = func_4958()
func_4959 = relay.Function([], output)
mutated_mod['func_4959'] = func_4959
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3794_call = mod.get_global_var('func_3794')
func_3795_call = mutated_mod.get_global_var('func_3795')
call_4967 = relay.TupleGetItem(func_3794_call(), 0)
call_4968 = relay.TupleGetItem(func_3795_call(), 0)
func_3302_call = mod.get_global_var('func_3302')
func_3303_call = mutated_mod.get_global_var('func_3303')
call_4969 = relay.TupleGetItem(func_3302_call(), 0)
call_4970 = relay.TupleGetItem(func_3303_call(), 0)
func_3650_call = mod.get_global_var('func_3650')
func_3652_call = mutated_mod.get_global_var('func_3652')
call_4985 = relay.TupleGetItem(func_3650_call(relay.reshape(call_4969.astype('float32'), [288,])), 0)
call_4986 = relay.TupleGetItem(func_3652_call(relay.reshape(call_4969.astype('float32'), [288,])), 0)
output = relay.Tuple([call_4967,call_4969,call_4985,])
output2 = relay.Tuple([call_4968,call_4970,call_4986,])
func_4998 = relay.Function([], output)
mod['func_4998'] = func_4998
mod = relay.transform.InferType()(mod)
mutated_mod['func_4998'] = func_4998
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4998_call = mutated_mod.get_global_var('func_4998')
call_4999 = func_4998_call()
output = call_4999
func_5000 = relay.Function([], output)
mutated_mod['func_5000'] = func_5000
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2921_call = mod.get_global_var('func_2921')
func_2923_call = mutated_mod.get_global_var('func_2923')
call_5021 = relay.TupleGetItem(func_2921_call(), 0)
call_5022 = relay.TupleGetItem(func_2923_call(), 0)
func_4161_call = mod.get_global_var('func_4161')
func_4164_call = mutated_mod.get_global_var('func_4164')
const_5026 = relay.const([-1.674949,-8.414503,-2.187420,-8.226610,8.919926,-7.768963,9.392017,-9.842139,3.071381,-3.834741,-2.279310,9.686737,9.251196,4.354603,-9.664894,8.877580,-7.189053,-5.335505,-4.848193,-6.247082,-7.370929,6.753053,0.265881,-9.106874,5.415126,-8.278633,-9.568001,-1.011023,-7.345737,-7.394473,-5.296512,0.585838,3.408383,-7.627757,-0.886159,0.965813,6.587642,5.350919,4.029799,4.005089,-3.183318,-6.735715,4.867548,-3.130411,6.295481,-6.547627,9.513050,-4.249814,2.291960,-0.817649,5.516331,-6.185273,1.724868,0.470788,-3.917728,0.938879,-2.651094,5.464669,-6.139248,5.373390,-4.644804,-3.623227,9.614751,2.413826,0.723909,8.684506,9.520289,9.118895,1.582057,7.939172,0.843607,-4.781434,3.970251,7.896710,-7.773105,3.253512,-8.209281,-8.064789,-4.842171,7.853487,3.826344,0.538239,-4.561830,3.850396,7.933772,2.799425,-9.237441,2.314466,4.411606,0.316096,4.800239,0.229652,-5.518422,-0.929706,6.195022,-5.024826,-6.134291,3.756244,-3.449929,-7.358974,-1.689364,-4.979401,4.285513,-8.618833,-0.846113,-8.691093,-6.331631,-5.295541,7.849358,5.431345,-7.791193,-0.122639,9.666844,5.883358,-9.428059,-0.174269,-8.503361,2.660099,-0.492291,-3.527209,-6.292733,-2.717734,-2.989633,4.078914,2.027638,-2.464516,6.773231,-5.070244,7.367819,-8.718361,7.179313,-5.742396,-2.310112,-2.745421,0.505992,1.566832,3.348181,-2.027093,-5.956167,-5.944273,-0.607540,0.998895,5.110345,6.135448,-3.520359,-9.173521,-2.503503,3.721456,9.626246,1.873711,-1.966773,-4.138489,-4.823486,-9.906583,-8.442625,2.949032,8.576352,-7.997305,-9.657373,4.675620,-8.642151,6.038269,-8.157440,3.822211,-2.685946,-0.043133,4.643693,-6.288619,1.125973,1.815785,8.008847,1.527921,8.287299,4.510667,0.097189,-2.298870,7.226656,-5.420583,-9.711936,4.607194,-0.439151,-3.741223,-3.166271,9.877040,1.988830,0.841348,4.541367,8.314248,6.566168,2.214900,-7.416665,-7.248556,1.494926,3.865076,-3.375759,-3.425860,7.277800,-8.772304,7.586775,1.621452,-5.854725,-7.572910,3.491993,7.820410,-6.907144,2.157997,-8.811262,-0.202274,-1.523608,-3.450501,-5.011449,7.308483,9.799880,7.667819,-0.150997,3.799878,-4.042671,-6.277333,8.503155,-1.609761,-4.801413,-5.350507,7.652946,-5.808918,8.874353,-0.261785,1.410009,1.340217,8.031269,-9.525128,2.859442,6.745546,6.394451,-6.828677,1.224613,-9.259865,-2.682689,-0.308001,-2.925425,-1.211390,7.891414,2.438609,-0.263466,4.514030,-5.792825,6.349936,4.731584,6.662564,8.016731,-3.289612,-0.752560,-5.307346,3.436201,-6.098100,-6.128136,2.723660,0.764792,-1.291897,6.117466,1.222778,0.851269,-6.805794,2.109774,5.610559,6.931956,3.592297,5.675169,-0.459260,4.605632,-6.263481,1.464716,8.566377,-7.725601,8.760364,-6.045664,1.127979,1.223458,-3.150386,4.950474,0.778745,8.077223,-5.950113,7.158698,-9.511751,1.036333,-4.669775,-2.625593,3.254806,1.853114,4.366462,-2.286736,-2.847072,-3.259226,-9.899137,-4.538055,-9.830458,0.397636,-5.997222,7.771285,4.632077,4.886979,-2.368170,6.970826,1.402072,-4.600281,-0.249197,4.510585,-8.211560,-3.508286,-2.050146,1.540533,-3.100537,8.687420,2.433882,8.077450,-7.667671,-1.579768,4.119294,-7.904534,-9.495655,7.691165,2.831818,6.591104,-1.752097,2.177085,4.904075,6.144691,1.311564,-5.210634,1.753323,6.878164,2.222514,-7.477408,9.409596,7.754118,9.308730,4.654770,0.796558,7.850841,-4.766893,-7.415764,5.376820,1.328176,2.346558,1.941149,-4.337658,-7.854327,-6.199033,-3.271994,4.427873,1.623783,-1.656281,-8.557658,-6.486708,4.685152,-8.450591,-7.234500,3.152881,-9.601893,0.401988,1.658662,-2.176907,1.155614,3.258321,-8.430602,2.577999,7.493167,-9.540694,-2.506952,9.028031,9.795283,6.658822,6.757532,-4.907122,0.073287,7.844157,9.459155,-6.405155,-3.076931,-7.733146,0.795268,1.935406,2.023543,-1.530450,-8.966639,4.626634,5.946382,1.227159,7.469981,-9.151487,4.793736,4.508602,9.139372,-9.574148,2.745588,-3.749416,-2.683679,-4.149436,-0.059555,3.976425,-6.490765,-0.609774,-2.906702,9.955089,3.279198,-2.408836,7.904906,3.738401,-7.309151,7.897726,-5.313684,-8.870331,4.102171,-7.359193,0.508064,-0.479932,-9.813325,3.657095,-8.039293,-6.555852,-2.975559,-7.499732,8.055493,-4.058411,6.408848,7.768594,0.257204,9.520189,-0.132008,-6.804205,8.375058,-9.160246,-5.324573,-7.795599,-3.274717,-7.614402,-2.679311,-1.671626,4.939835,6.386822,-2.041833,-9.976278,-7.551571,-2.990314,-3.041404,-3.163304,4.421423,2.480233,-0.780808,-0.461818,7.795010,2.295493,-6.427069,6.067663,-2.861447,-1.121528,6.101208,-4.696579,-5.124079,5.431596,-7.165144,5.378814,-8.975525,2.675634,-4.479063,9.592755,-2.763622,4.505648], dtype = "float32")#candidate|5026|(468,)|const|float32
call_5025 = relay.TupleGetItem(func_4161_call(relay.reshape(const_5026.astype('float32'), [468,])), 1)
call_5027 = relay.TupleGetItem(func_4164_call(relay.reshape(const_5026.astype('float32'), [468,])), 1)
var_5030 = relay.var("var_5030", dtype = "float64", shape = (4, 28))#candidate|5030|(4, 28)|var|float64
bop_5031 = relay.greater(call_5025.astype('bool'), relay.reshape(var_5030.astype('bool'), relay.shape_of(call_5025))) # shape=(4, 28)
bop_5034 = relay.greater(call_5027.astype('bool'), relay.reshape(var_5030.astype('bool'), relay.shape_of(call_5027))) # shape=(4, 28)
func_4346_call = mod.get_global_var('func_4346')
func_4350_call = mutated_mod.get_global_var('func_4350')
const_5036 = relay.const(-3, dtype = "uint32")#candidate|5036|()|const|uint32
var_5037 = relay.var("var_5037", dtype = "uint32", shape = (12,))#candidate|5037|(12,)|var|uint32
call_5035 = relay.TupleGetItem(func_4346_call(relay.reshape(const_5036.astype('uint32'), []), relay.reshape(var_5037.astype('uint32'), [3, 1, 4]), ), 0)
call_5038 = relay.TupleGetItem(func_4350_call(relay.reshape(const_5036.astype('uint32'), []), relay.reshape(var_5037.astype('uint32'), [3, 1, 4]), ), 0)
bop_5044 = relay.greater_equal(call_5025.astype('bool'), relay.reshape(var_5030.astype('bool'), relay.shape_of(call_5025))) # shape=(4, 28)
bop_5047 = relay.greater_equal(call_5027.astype('bool'), relay.reshape(var_5030.astype('bool'), relay.shape_of(call_5027))) # shape=(4, 28)
func_2899_call = mod.get_global_var('func_2899')
func_2900_call = mutated_mod.get_global_var('func_2900')
call_5071 = relay.TupleGetItem(func_2899_call(), 3)
call_5072 = relay.TupleGetItem(func_2900_call(), 3)
func_4773_call = mod.get_global_var('func_4773')
func_4775_call = mutated_mod.get_global_var('func_4775')
call_5074 = func_4773_call()
call_5075 = func_4773_call()
uop_5090 = relay.log(bop_5031.astype('float64')) # shape=(4, 28)
uop_5092 = relay.log(bop_5034.astype('float64')) # shape=(4, 28)
func_4161_call = mod.get_global_var('func_4161')
func_4164_call = mutated_mod.get_global_var('func_4164')
call_5097 = relay.TupleGetItem(func_4161_call(relay.reshape(call_5074.astype('float32'), [468,])), 4)
call_5098 = relay.TupleGetItem(func_4164_call(relay.reshape(call_5074.astype('float32'), [468,])), 4)
const_5105 = relay.const([[-3.895956,9.688471,-0.691707,-7.794506,-7.684815,-3.704225,-9.904148,-2.815377,-9.213077,-7.336601,7.882820,7.477002,-3.137468,-0.835172,8.134616,3.302705,-4.203192,-3.680791,-6.079124,2.073653,-7.827258,-0.848963,4.899941,1.031326,2.033025,-7.623025,7.000605,-1.023229],[4.688125,-1.477368,-7.688038,-7.074541,6.494192,4.462860,9.632313,-6.962686,-4.981587,3.072766,6.514300,1.356147,-1.945298,4.200122,1.706379,7.614213,-2.725101,8.739516,-6.382686,8.485662,-9.832687,3.426220,1.498058,-6.555931,-4.344311,-4.252221,-4.045415,9.652930],[6.230433,3.247631,-1.083180,0.403683,-6.866214,8.394102,3.996588,-8.344431,5.624963,1.257343,5.275872,-0.307759,3.098793,8.357646,-0.885899,9.743971,9.742149,-2.985395,2.558036,-3.301405,-9.275384,-2.969373,-9.257980,1.219932,-4.635646,9.783311,-8.315130,-4.070169],[-0.152195,-5.337685,-9.447029,-7.452931,-3.127226,2.180396,5.299034,8.681087,5.543497,8.169686,1.318426,1.300104,0.781576,9.866012,-8.928362,-5.285257,-3.602319,2.804420,-5.668166,-1.455150,-9.462817,-3.177181,-1.822027,7.996150,-2.383759,5.190157,2.466353,5.233434]], dtype = "float64")#candidate|5105|(4, 28)|const|float64
bop_5106 = relay.equal(uop_5090.astype('bool'), relay.reshape(const_5105.astype('bool'), relay.shape_of(uop_5090))) # shape=(4, 28)
bop_5109 = relay.equal(uop_5092.astype('bool'), relay.reshape(const_5105.astype('bool'), relay.shape_of(uop_5092))) # shape=(4, 28)
func_842_call = mod.get_global_var('func_842')
func_847_call = mutated_mod.get_global_var('func_847')
call_5110 = relay.TupleGetItem(func_842_call(relay.reshape(const_5105.astype('float64'), [4, 4, 7]), relay.reshape(call_5025.astype('float64'), [4, 4, 7]), relay.reshape(call_5074.astype('float32'), [1, 468]), ), 0)
call_5111 = relay.TupleGetItem(func_847_call(relay.reshape(const_5105.astype('float64'), [4, 4, 7]), relay.reshape(call_5025.astype('float64'), [4, 4, 7]), relay.reshape(call_5074.astype('float32'), [1, 468]), ), 0)
output = relay.Tuple([call_5021,const_5026,call_5035,const_5036,var_5037,bop_5044,call_5071,call_5074,call_5097,bop_5106,call_5110,])
output2 = relay.Tuple([call_5022,const_5026,call_5038,const_5036,var_5037,bop_5047,call_5072,call_5075,call_5098,bop_5109,call_5111,])
func_5117 = relay.Function([var_5030,var_5037,], output)
mod['func_5117'] = func_5117
mod = relay.transform.InferType()(mod)
var_5118 = relay.var("var_5118", dtype = "float64", shape = (4, 28))#candidate|5118|(4, 28)|var|float64
var_5119 = relay.var("var_5119", dtype = "uint32", shape = (12,))#candidate|5119|(12,)|var|uint32
output = func_5117(var_5118,var_5119,)
func_5120 = relay.Function([var_5118,var_5119,], output)
mutated_mod['func_5120'] = func_5120
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3483_call = mod.get_global_var('func_3483')
func_3485_call = mutated_mod.get_global_var('func_3485')
call_5130 = relay.TupleGetItem(func_3483_call(), 0)
call_5131 = relay.TupleGetItem(func_3485_call(), 0)
uop_5155 = relay.tan(call_5130.astype('float64')) # shape=(468,)
uop_5157 = relay.tan(call_5131.astype('float64')) # shape=(468,)
output = uop_5155
output2 = uop_5157
func_5170 = relay.Function([], output)
mod['func_5170'] = func_5170
mod = relay.transform.InferType()(mod)
mutated_mod['func_5170'] = func_5170
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5170_call = mutated_mod.get_global_var('func_5170')
call_5171 = func_5170_call()
output = call_5171
func_5172 = relay.Function([], output)
mutated_mod['func_5172'] = func_5172
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3461_call = mod.get_global_var('func_3461')
func_3462_call = mutated_mod.get_global_var('func_3462')
call_5208 = relay.TupleGetItem(func_3461_call(), 0)
call_5209 = relay.TupleGetItem(func_3462_call(), 0)
func_4250_call = mod.get_global_var('func_4250')
func_4252_call = mutated_mod.get_global_var('func_4252')
call_5224 = func_4250_call()
call_5225 = func_4250_call()
output = relay.Tuple([call_5208,call_5224,])
output2 = relay.Tuple([call_5209,call_5225,])
func_5243 = relay.Function([], output)
mod['func_5243'] = func_5243
mod = relay.transform.InferType()(mod)
output = func_5243()
func_5244 = relay.Function([], output)
mutated_mod['func_5244'] = func_5244
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5256 = relay.var("var_5256", dtype = "float32", shape = (7, 10, 12))#candidate|5256|(7, 10, 12)|var|float32
uop_5257 = relay.cos(var_5256.astype('float32')) # shape=(7, 10, 12)
output = relay.Tuple([uop_5257,])
output2 = relay.Tuple([uop_5257,])
func_5259 = relay.Function([var_5256,], output)
mod['func_5259'] = func_5259
mod = relay.transform.InferType()(mod)
mutated_mod['func_5259'] = func_5259
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5260 = relay.var("var_5260", dtype = "float32", shape = (7, 10, 12))#candidate|5260|(7, 10, 12)|var|float32
func_5259_call = mutated_mod.get_global_var('func_5259')
call_5261 = func_5259_call(var_5260)
output = call_5261
func_5262 = relay.Function([var_5260], output)
mutated_mod['func_5262'] = func_5262
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3483_call = mod.get_global_var('func_3483')
func_3485_call = mutated_mod.get_global_var('func_3485')
call_5340 = relay.TupleGetItem(func_3483_call(), 0)
call_5341 = relay.TupleGetItem(func_3485_call(), 0)
func_3194_call = mod.get_global_var('func_3194')
func_3195_call = mutated_mod.get_global_var('func_3195')
call_5360 = func_3194_call()
call_5361 = func_3194_call()
output = relay.Tuple([call_5340,call_5360,])
output2 = relay.Tuple([call_5341,call_5361,])
func_5369 = relay.Function([], output)
mod['func_5369'] = func_5369
mod = relay.transform.InferType()(mod)
mutated_mod['func_5369'] = func_5369
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5369_call = mutated_mod.get_global_var('func_5369')
call_5370 = func_5369_call()
output = call_5370
func_5371 = relay.Function([], output)
mutated_mod['func_5371'] = func_5371
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5372 = relay.var("var_5372", dtype = "int16", shape = ())#candidate|5372|()|var|int16
var_5373 = relay.var("var_5373", dtype = "int16", shape = (7, 2, 3))#candidate|5373|(7, 2, 3)|var|int16
bop_5374 = relay.greater_equal(var_5372.astype('bool'), var_5373.astype('bool')) # shape=(7, 2, 3)
func_2623_call = mod.get_global_var('func_2623')
func_2626_call = mutated_mod.get_global_var('func_2626')
var_5386 = relay.var("var_5386", dtype = "float32", shape = (72, 4))#candidate|5386|(72, 4)|var|float32
call_5385 = relay.TupleGetItem(func_2623_call(relay.reshape(var_5386.astype('float32'), [288,])), 2)
call_5387 = relay.TupleGetItem(func_2626_call(relay.reshape(var_5386.astype('float32'), [288,])), 2)
output = relay.Tuple([bop_5374,call_5385,var_5386,])
output2 = relay.Tuple([bop_5374,call_5387,var_5386,])
func_5390 = relay.Function([var_5372,var_5373,var_5386,], output)
mod['func_5390'] = func_5390
mod = relay.transform.InferType()(mod)
var_5391 = relay.var("var_5391", dtype = "int16", shape = ())#candidate|5391|()|var|int16
var_5392 = relay.var("var_5392", dtype = "int16", shape = (7, 2, 3))#candidate|5392|(7, 2, 3)|var|int16
var_5393 = relay.var("var_5393", dtype = "float32", shape = (72, 4))#candidate|5393|(72, 4)|var|float32
output = func_5390(var_5391,var_5392,var_5393,)
func_5394 = relay.Function([var_5391,var_5392,var_5393,], output)
mutated_mod['func_5394'] = func_5394
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4549_call = mod.get_global_var('func_4549')
func_4551_call = mutated_mod.get_global_var('func_4551')
call_5396 = relay.TupleGetItem(func_4549_call(), 2)
call_5397 = relay.TupleGetItem(func_4551_call(), 2)
func_2623_call = mod.get_global_var('func_2623')
func_2626_call = mutated_mod.get_global_var('func_2626')
const_5403 = relay.const([8.009711,-4.852259,-8.620940,8.884111,2.630254,9.815993,-9.546707,-8.261487,-2.491100,-0.037878,-2.596461,-6.887566,6.559771,-4.748072,-0.060600,-3.819356,9.572877,-5.342055,-8.222886,-8.995451,-5.079154,-1.447870,4.324471,-0.323027,4.424332,-7.385357,7.362616,-0.033545,2.427361,5.207382,-6.801978,1.552618,-1.300807,4.632124,0.105523,-6.372474,8.597385,5.383572,-5.000935,-4.867840,-9.671610,0.528525,-5.477551,6.896156,-1.420695,9.282550,-3.685084,-0.957871,-9.316118,-5.798474,4.892945,-2.325157,3.684470,8.894190,7.978231,7.557650,6.853454,-4.281515,9.529409,7.038723,-8.263500,-8.125399,9.700481,-3.785047,-4.515611,0.966206,9.133071,-1.584654,1.930035,-9.868275,-2.084005,1.282248,-4.771958,3.847795,9.642359,-4.175728,0.595560,-0.585277,3.170290,0.741040,7.050651,-5.440283,-5.903057,0.094647,-7.349577,-5.778523,-3.910562,-0.851319,1.081795,-8.930480,-7.560991,7.304753,6.197256,-1.390591,-9.053962,-1.542141,3.554925,-3.250070,3.986606,7.961667,-3.409134,-0.205239,6.915686,1.568518,-1.678156,7.103226,-4.582482,8.931076,6.764406,6.790962,3.947333,8.148670,-2.897964,-8.463692,-4.873849,2.240359,3.449595,9.720470,9.020438,-3.703535,-4.701623,-4.228199,-7.165372,-6.904546,-8.935911,8.969945,1.732468,-6.367234,-0.274686,3.574943,-7.471076,4.223237,7.574002,8.243893,-1.277775,-8.914786,1.642539,5.015808,-4.375633,4.838206,5.395628,-1.748101,-5.853831,-6.983295,2.588734,1.284125,8.746034,-9.984385,8.499590,8.989523,6.365570,-1.360817,-2.402212,-4.231758,3.080718,3.142178,-6.172799,8.146227,-1.329318,9.953206,9.993677,-5.914847,-9.890641,0.719956,-8.248930,1.382393,8.910679,-5.221132,3.550936,-1.166320,8.431240,-2.711977,-6.696555,-5.639280,8.375166,-2.982438,-8.480908,8.147332,1.141345,-9.308382,3.567917,5.685946,4.080000,2.749976,-1.770573,5.732481,9.686719,1.713104,8.842345,4.440135,-6.780842,2.238102,-4.280057,2.982933,-6.093823,3.512578,6.284372,-4.774852,-6.187565,3.515333,5.857092,-4.670747,-3.627442,-9.343181,7.583908,5.612058,-9.369094,-6.056405,0.345267,-4.317460,3.278251,-5.793617,3.477750,8.910518,-3.620142,-4.638806,8.850854,-1.229660,8.753704,5.995591,-0.364830,-1.767734,-4.961579,7.984849,-0.335812,7.596177,9.325472,-5.674681,-9.916850,0.611236,-5.239888,-3.722715,-1.592866,-0.364553,-8.188406,8.818511,-6.598074,4.317837,-6.651336,-2.115549,-7.840199,3.771432,7.746773,-9.567847,6.856424,-5.329524,-5.986464,-2.576764,-5.189804,-1.044252,-2.593150,1.280252,2.181442,5.280481,-1.435927,-3.220288,4.115245,-7.912610,0.320558,-6.290850,-5.081746,-9.847873,-8.786767,-8.853239,1.172853,6.031638,-6.787970,-4.165882,3.416839,0.185511,-4.250443,-9.409913,7.634646,-5.594631,-4.818364,-7.624363,-1.703259,7.546137,5.117004,1.783692,-3.284364,-2.063344,2.984931,-4.101188,5.459245,-9.583225,0.018118,0.916189], dtype = "float32")#candidate|5403|(288,)|const|float32
call_5402 = relay.TupleGetItem(func_2623_call(relay.reshape(const_5403.astype('float32'), [288,])), 2)
call_5404 = relay.TupleGetItem(func_2626_call(relay.reshape(const_5403.astype('float32'), [288,])), 2)
func_4519_call = mod.get_global_var('func_4519')
func_4523_call = mutated_mod.get_global_var('func_4523')
const_5425 = relay.const([8.083278,1.773078,3.131556,0.417132,-7.397271,1.236271,-0.105781,9.837885,-8.994889,-0.148680,-4.913607,1.400464,2.890504,5.345224,1.886895,-0.075134,-4.198574,2.860422,6.823544,2.111256,-4.081512,1.251516,-3.547752,6.475566,-0.101962,6.621639,-5.415052,7.418806,-3.566289,-6.331817,2.164226,-5.719554,-6.705798,5.615733,1.666159,-2.739497,5.999881,-0.335796,-2.993253,6.509060,0.101689,-0.862989,3.336087,7.741974,-9.605451,-2.051407,-0.341646,6.865712,-5.674724,-1.022428,5.708794,-8.210081,8.376475,-1.017921,-9.740571,-9.654615,-7.339199,2.693969,-9.757642,-5.850225,-3.837637,-4.361297,2.552628,-2.818340,7.086376,2.752695,1.586529,7.822198,-1.092155,-7.411880,6.049094,-2.549330,3.959345,-5.353981,-8.251958,-0.655953,6.531638,-4.902582,6.793941,-5.976618,5.380400,7.523691,0.686202,6.675958,3.913878,7.612132,5.808349,-4.689496,1.311676,-9.615924,2.350853,8.162992,-0.554448,-7.369325,-1.446682,-6.425527,-5.272984,-2.246984,-5.338981,-1.071581,6.053816,4.502519,5.893419,-6.483992,-2.154433,8.965097,6.503959,-6.899814,-3.209976,2.822795,6.059568,-5.563809], dtype = "float64")#candidate|5425|(112,)|const|float64
var_5426 = relay.var("var_5426", dtype = "bool", shape = (468,))#candidate|5426|(468,)|var|bool
call_5424 = relay.TupleGetItem(func_4519_call(relay.reshape(const_5425.astype('float64'), [112,]), relay.reshape(var_5426.astype('bool'), [12, 13, 3]), relay.reshape(var_5426.astype('bool'), [12, 13, 3]), ), 0)
call_5427 = relay.TupleGetItem(func_4523_call(relay.reshape(const_5425.astype('float64'), [112,]), relay.reshape(var_5426.astype('bool'), [12, 13, 3]), relay.reshape(var_5426.astype('bool'), [12, 13, 3]), ), 0)
output = relay.Tuple([call_5396,call_5402,const_5403,call_5424,const_5425,var_5426,])
output2 = relay.Tuple([call_5397,call_5404,const_5403,call_5427,const_5425,var_5426,])
func_5428 = relay.Function([var_5426,], output)
mod['func_5428'] = func_5428
mod = relay.transform.InferType()(mod)
var_5429 = relay.var("var_5429", dtype = "bool", shape = (468,))#candidate|5429|(468,)|var|bool
output = func_5428(var_5429)
func_5430 = relay.Function([var_5429], output)
mutated_mod['func_5430'] = func_5430
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5243_call = mod.get_global_var('func_5243')
func_5244_call = mutated_mod.get_global_var('func_5244')
call_5498 = relay.TupleGetItem(func_5243_call(), 0)
call_5499 = relay.TupleGetItem(func_5244_call(), 0)
output = call_5498
output2 = call_5499
func_5501 = relay.Function([], output)
mod['func_5501'] = func_5501
mod = relay.transform.InferType()(mod)
output = func_5501()
func_5502 = relay.Function([], output)
mutated_mod['func_5502'] = func_5502
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3779_call = mod.get_global_var('func_3779')
func_3780_call = mutated_mod.get_global_var('func_3780')
call_5559 = func_3779_call()
call_5560 = func_3779_call()
output = relay.Tuple([call_5559,])
output2 = relay.Tuple([call_5560,])
func_5570 = relay.Function([], output)
mod['func_5570'] = func_5570
mod = relay.transform.InferType()(mod)
mutated_mod['func_5570'] = func_5570
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5570_call = mutated_mod.get_global_var('func_5570')
call_5571 = func_5570_call()
output = call_5571
func_5572 = relay.Function([], output)
mutated_mod['func_5572'] = func_5572
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3483_call = mod.get_global_var('func_3483')
func_3485_call = mutated_mod.get_global_var('func_3485')
call_5623 = relay.TupleGetItem(func_3483_call(), 0)
call_5624 = relay.TupleGetItem(func_3485_call(), 0)
output = call_5623
output2 = call_5624
func_5626 = relay.Function([], output)
mod['func_5626'] = func_5626
mod = relay.transform.InferType()(mod)
output = func_5626()
func_5627 = relay.Function([], output)
mutated_mod['func_5627'] = func_5627
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3779_call = mod.get_global_var('func_3779')
func_3780_call = mutated_mod.get_global_var('func_3780')
call_5706 = func_3779_call()
call_5707 = func_3779_call()
output = call_5706
output2 = call_5707
func_5711 = relay.Function([], output)
mod['func_5711'] = func_5711
mod = relay.transform.InferType()(mod)
mutated_mod['func_5711'] = func_5711
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5711_call = mutated_mod.get_global_var('func_5711')
call_5712 = func_5711_call()
output = call_5712
func_5713 = relay.Function([], output)
mutated_mod['func_5713'] = func_5713
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4108_call = mod.get_global_var('func_4108')
func_4109_call = mutated_mod.get_global_var('func_4109')
call_5720 = func_4108_call()
call_5721 = func_4108_call()
output = relay.Tuple([call_5720,])
output2 = relay.Tuple([call_5721,])
func_5723 = relay.Function([], output)
mod['func_5723'] = func_5723
mod = relay.transform.InferType()(mod)
mutated_mod['func_5723'] = func_5723
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5723_call = mutated_mod.get_global_var('func_5723')
call_5724 = func_5723_call()
output = call_5724
func_5725 = relay.Function([], output)
mutated_mod['func_5725'] = func_5725
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3859_call = mod.get_global_var('func_3859')
func_3861_call = mutated_mod.get_global_var('func_3861')
call_5743 = relay.TupleGetItem(func_3859_call(), 0)
call_5744 = relay.TupleGetItem(func_3861_call(), 0)
func_4161_call = mod.get_global_var('func_4161')
func_4164_call = mutated_mod.get_global_var('func_4164')
call_5754 = relay.TupleGetItem(func_4161_call(relay.reshape(call_5743.astype('float32'), [468,])), 2)
call_5755 = relay.TupleGetItem(func_4164_call(relay.reshape(call_5743.astype('float32'), [468,])), 2)
func_3385_call = mod.get_global_var('func_3385')
func_3388_call = mutated_mod.get_global_var('func_3388')
var_5770 = relay.var("var_5770", dtype = "float32", shape = (4, 72))#candidate|5770|(4, 72)|var|float32
call_5769 = relay.TupleGetItem(func_3385_call(relay.reshape(var_5770.astype('float32'), [1, 288])), 1)
call_5771 = relay.TupleGetItem(func_3388_call(relay.reshape(var_5770.astype('float32'), [1, 288])), 1)
output = relay.Tuple([call_5743,call_5754,call_5769,var_5770,])
output2 = relay.Tuple([call_5744,call_5755,call_5771,var_5770,])
func_5779 = relay.Function([var_5770,], output)
mod['func_5779'] = func_5779
mod = relay.transform.InferType()(mod)
mutated_mod['func_5779'] = func_5779
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5780 = relay.var("var_5780", dtype = "float32", shape = (4, 72))#candidate|5780|(4, 72)|var|float32
func_5779_call = mutated_mod.get_global_var('func_5779')
call_5781 = func_5779_call(var_5780)
output = call_5781
func_5782 = relay.Function([var_5780], output)
mutated_mod['func_5782'] = func_5782
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2967_call = mod.get_global_var('func_2967')
func_2968_call = mutated_mod.get_global_var('func_2968')
call_5824 = relay.TupleGetItem(func_2967_call(), 0)
call_5825 = relay.TupleGetItem(func_2968_call(), 0)
func_5369_call = mod.get_global_var('func_5369')
func_5371_call = mutated_mod.get_global_var('func_5371')
call_5830 = relay.TupleGetItem(func_5369_call(), 1)
call_5831 = relay.TupleGetItem(func_5371_call(), 1)
func_3437_call = mod.get_global_var('func_3437')
func_3439_call = mutated_mod.get_global_var('func_3439')
call_5833 = func_3437_call()
call_5834 = func_3437_call()
func_3766_call = mod.get_global_var('func_3766')
func_3769_call = mutated_mod.get_global_var('func_3769')
const_5838 = relay.const([-0.943764,7.578962,-3.247787,-3.922966,7.773340,-2.228457,1.083442,3.394742,3.655717,7.115477,5.581986,-7.873160,3.048825,2.256311,-1.897266,-7.911090,-0.220480,5.840740,6.053681,4.957429,4.941114,7.590771,7.544233,-6.425423,-1.038457,1.620871,4.058092,-0.286904,2.325542,3.697645,6.479817,-3.247135,7.433375,-5.413212,1.160274,-5.738166,-3.463181,9.977357,-3.473068,-5.037243,9.501490,-7.289690,-8.794525,-1.829959,-0.249967,5.389635,3.241906,5.564085,6.437425,5.901798,5.802339,2.773898,8.778743,5.836367,4.438164,-5.958122,-6.870473,6.510125,1.386713,-4.095882,2.906794,2.861240,7.302257,-3.881285,9.649392,1.132363,1.912113,-2.744520,-9.626970,-9.804103,0.939907,-3.916380,4.966395,-0.168640,0.049179,-8.529980,-8.960502,9.801597,-3.593088,4.619470,0.839009,-1.123842,0.004299,8.350655,8.430356,1.070815,-2.820412,-0.314135,9.780298,-2.100694,0.934107,-0.389543,0.250550,1.813934,6.522925,8.097858,3.587095,0.068217,-4.419988,-4.862124,-8.452633,-3.833035,-0.176680,-0.807825,-2.081056,-0.694358,7.729859,0.353898,5.163795,-7.455406,3.375746,4.085616,9.278725,-0.622254,-7.434691,8.069994,-0.539433,5.314416,-9.487651,1.457192,1.663836,-8.858974,-5.253991,8.822538,-5.697932,-2.624802,3.319732,7.797745,-4.877923,-7.427608,-5.457469,4.796050,7.037454,9.347528,-4.639798,-5.498315,3.063064,-2.033141,0.740014,9.360521,6.502499,8.200654,1.464340,2.344864,-0.330737,-8.966802,-2.521350,-2.276733,0.383750,7.983034,-1.376012,7.663871,6.700763,1.862399,7.066731,-0.393610,-4.968145,2.686415,-3.650653,5.087308,-5.664998,-6.329370,3.821069,-3.712567,-3.601837,-5.364756,-3.401861,-0.791720,1.319672,-5.166448,-6.431369,6.178044,-5.592172,6.377180,2.134650,-6.088657,-6.187667,-4.221456,7.973613,-6.194586,5.868517,-2.240303,-1.690234,3.295936,-5.546891,-7.624910,-0.546302,6.332567,-2.573746,-7.356685,9.603045,2.225277,7.917543,7.143110,0.600446,-3.688473,-2.422730,-5.335007,-4.086232,-8.594357,6.436457,3.588975,-5.527697,-3.181358,6.051327,-6.956738,1.957527,5.512851,-3.913098,3.427812,-4.586960,-7.488628,-3.903316,-1.406505,-6.729790,7.144781,4.926803,9.430133,4.436381,3.749164,-2.213761,3.024334,4.465208,-5.454542,8.729300,3.201097,-0.391976,-3.282533,-0.063287,5.576437,4.536014,-6.058140,2.216620,-7.018818,-5.397166,-8.494271,-5.967635,-8.725156,-1.868513,4.417545,6.549020,3.271377,-5.508449,-1.987418,-3.898839,5.121956,0.371289,1.171248,6.894606,6.451507,6.896020,8.591094,-9.340562,9.622506,-1.213840,-3.865465,-2.593618,6.886452,-9.295425,2.542362,0.196263,-0.112038,6.287477,-9.453086,-0.466239,-7.581689,7.007924,5.537608,7.726530,-3.092485,4.586623,7.860921,-1.485262,-1.480532,9.617467,-4.097494,-5.186265,6.714010,-2.635412,-7.122432,7.607946,-3.402977,-3.631342,-4.099566,-3.982645,-9.735250,-5.548660,4.048230,-1.705954,0.834755,-5.348465,7.387855,-4.942562,-2.071674,-1.030877,3.404901,1.029101,-8.107568,7.344006,1.228579,7.770072,0.052383,-7.866937,-7.282917,-1.856750,-0.282963,3.015030,1.591421,-6.309445,-3.183885,0.404362,-0.392887,2.386536,-4.480968,-1.521121,4.383569,5.203235,2.200166,1.214902,2.882497,2.678924,-9.473901,5.961314,-7.347983,3.390479,-2.754426,3.224600,6.966613,1.042466,4.837144,-6.518664,6.436938,-7.935619,6.959351,-0.217599,1.283887,-8.602759,2.684990,-6.450861,5.829007,-1.607770,-4.941525,-6.665815,5.045016,4.789710,8.123590,7.637374,-3.029762,2.163625,7.537240,-7.042223,2.319211,1.192387,-1.968452,6.887130,6.808730,6.646948,0.567594,-8.259636,7.548878,5.013887,3.069085,7.065507,-6.357753,9.298478,-8.228000,3.345748,-0.251634,-7.701509,-0.835159,-4.934836,-4.499345,3.996298,6.632563,-9.682076,7.699620,-5.963195,-5.209715,-6.883199,-4.489867,-8.120857,9.156333,4.831797,-9.743944,-8.975365,1.103182,2.456284,-2.406977,9.821818,-9.527035,-1.954504,4.273304,-8.475656,-8.773951,3.541044,-0.157711,-8.572682,7.685682,3.430089,6.579830,-0.430179,-0.110889,-1.492765,-2.947387,-4.289153,6.723355,-5.784081,6.046381,-3.268905,-7.806540,2.515093,-6.473383,-5.989755,2.540608,8.236186,-8.529466,6.797408,7.193225,4.265229,8.085495,-9.895226,4.158235,1.177238,5.917875,-6.140609,0.666444,-5.518094,7.794750,2.186817,-5.939364,-4.202827,-9.912777,1.015630,1.989491,0.474921,4.336600,-6.136613,1.718637,7.519443,9.606051,-1.683493,1.904929,-4.380311,3.485453,0.113048,8.261662,-6.576243,7.262790,2.043008,7.176070,4.992676,1.492931,5.456516,-6.751064,7.150459,-4.218312,-8.888351,2.588006,9.211620,1.666406,-1.492818,-0.759987,-1.182793,6.782653,-2.219663,9.393917,0.653156,6.377712,4.232660,7.839118,-0.308704,-8.879834,-6.241377,9.283954,-8.491635,-4.066569,0.282208,-5.191822,8.748432,-5.943670,-0.416685,0.650332,-3.196410,-4.635370,-8.736119,-9.963538,0.464608,-9.973702,-0.561419,7.425974,-1.382954,-9.416523,-7.698585,2.005687,-1.769931,-2.627305,8.027153,-4.380982,-5.386208,1.948852,-2.278642,7.050138,-6.224185,1.401552,-8.555963,-9.062676,4.937110,-1.527059,4.352865,6.627478,0.183081,-6.529674,1.834083,-8.312659,9.774670,7.352903,-3.612596,5.741533,-9.738439,6.632689,-6.986912,3.441334,-9.290101,5.188835,2.642120,6.531595,-7.628420,-6.095930,-3.126027,-1.715880,-6.742144,-5.336459,-4.058460,-7.237949,-6.477958,6.045099,9.081965,-3.225212,6.939535,8.597039,-5.825301,5.860136,-7.382402,6.000211,8.282099,-4.808088,2.388339,-8.314025,-0.119930,-4.263339,-3.338528,5.513987,-2.993048,-6.680722,-7.803462,-4.034041,-9.972214,7.075346,2.816073,-5.568785,-2.538847,1.647976,8.346613,-0.953978,-7.081931,-7.623150,-3.896411,-3.671496,-5.116902,-6.777138,-6.654227,0.415078,1.134315,2.581829,3.566824,5.133285,-2.385946,6.304866,-2.648191,1.376584,-1.555728,0.248668,-7.796412,5.956025,-7.476418,3.563680,4.888377,-2.736851,6.042861,6.037689,4.813793,4.097405,8.872537,7.964646,-2.985879,-8.427110,-6.258698,1.392791,5.739479,0.958478,3.285194,-7.982238,-5.486510,7.171566,-7.190631,-6.479119,4.196841,4.931149,6.194612,-0.372482,-3.500572,-6.881615,-6.937077,8.363103,4.136664,-7.760744,5.880127,6.832527,6.445849,6.622388,0.289718,6.766114,1.813619,-8.477272,6.795660,-1.543101,0.352318,-8.832728,2.396563,-6.731413,8.178975,0.430448,1.915927,-2.826428,5.261132,0.875710,4.038934,0.433490,0.744546,3.010824,-9.973676,-5.347639,9.980032,7.919291,-1.445935,4.182464,-9.242132,-2.734625,2.666338,-7.502307,9.548811,8.844554,-3.126312,0.948743,-1.842634,-9.392689,1.291738,1.955595,-4.450366,3.744160,-8.176720,-3.849431,6.271856,-2.167825,3.401649,1.588186,-0.928985,9.994719,3.768201,0.263161,-9.928798,-5.121790,-3.257167,-5.076841,-0.894043,-8.714972,-6.669815,-1.902167,0.924814,-5.858304,2.021778,5.581291,-0.215885,0.350940,-4.987468,-4.268171,-6.640403,-2.780927,-5.248079,0.124136,-2.103941,9.151722,-9.270205,-1.687810,-2.065893,-0.061944,-7.845132,-7.016562,3.958796,-2.384988,-1.549985,-3.773450,0.938108,1.517764,5.982620,-3.665480,-2.740528,-4.891198,0.616759,6.326849,5.691990,-9.433086,7.005409,-0.439268,-4.365961,-5.460834,1.556939,7.335216,1.691589,-8.247890,-7.060676,-2.991849,-2.802314,4.465262,4.227813,-0.855683,6.598560,-3.739667,5.068236,0.962505,2.868143,-1.343061,-9.917430,0.253998,-3.220825,-4.777840,5.354582,-2.537179,9.992355,8.450002,-3.297693,9.497144,-0.618073,-2.945465,-8.148692,8.808004,-8.013645,7.504884,-6.732815,-7.370312,-7.365101,2.395138,-2.307216,-9.145072,1.818640,-7.006149,1.552222,8.655888,-5.465142,1.929497,9.399657,-8.146138,-4.493609,-9.293399,3.798459,2.857928,0.918186,9.050885,-6.466618,5.869155,3.850589,4.877166,2.723059,2.427245,5.458683,5.733296,1.364821,-4.179415,5.902666,-6.089976,8.934629,-4.407214,-2.798865,-5.734223,1.035081,2.864448,-8.874500,7.222829,9.924841,7.061534,4.662055,-0.584445,-6.025796,-9.222425,0.611244,-9.351693,6.684620,-3.168488,-4.736625,-7.905913,-5.946763,9.618140,0.958732,1.881093,4.370265,8.465036,4.334009,3.070404,-6.786573,5.816136,8.651611,-0.849650,-0.653450,-9.393880,-4.876339,4.174405,-9.776957,5.709259,1.546391,3.652409,8.501541,-4.121811,-1.545243,-3.966165,7.208529,-5.518842,-5.831557,7.838274,3.337341,1.686333,2.418329,0.110265], dtype = "float32")#candidate|5838|(832,)|const|float32
call_5837 = func_3766_call(relay.reshape(const_5838.astype('float32'), [13, 8, 8]))
call_5839 = func_3766_call(relay.reshape(const_5838.astype('float32'), [13, 8, 8]))
func_4088_call = mod.get_global_var('func_4088')
func_4090_call = mutated_mod.get_global_var('func_4090')
call_5841 = relay.TupleGetItem(func_4088_call(), 1)
call_5842 = relay.TupleGetItem(func_4090_call(), 1)
func_2037_call = mod.get_global_var('func_2037')
func_2040_call = mutated_mod.get_global_var('func_2040')
const_5844 = relay.const([7.836144,-8.245168,-2.335115,7.050767,-2.194428,1.850296,9.207437,-6.137808,-7.964002,-9.536596,-3.994246,-7.103893,9.279663,9.048284,9.083599,-8.214874,0.545266,6.002092,-0.531809,-7.785194,3.304605,-1.303249,-3.926542,9.815191,-7.126948,2.523466,-4.012473,-0.880596,-0.735467,-1.259715,4.020318,9.276091,-6.923464,3.675500,6.266455,7.691799,3.494443,8.775880,5.490444,-5.878334,-3.010609,-6.431636,9.612018,-1.290820,-6.066468,7.588330,4.466406,-8.739955,6.117481,-3.850165,0.905589,0.278191,9.796290,1.462518,9.349517,-0.969772,1.942639,-1.174363,0.763159,6.502780,-8.077631,-0.155296,8.737229,6.203103,-6.935881,8.899867,6.799215,-5.327863,3.510621,8.564818,5.986851,-1.558018,-9.332667,1.558852,7.441088,8.765642,-1.899014,-9.286705,9.717794,-5.893784,8.778769,8.611673,7.376719,-7.156072,7.414171,4.686478,4.342586,-9.913677,3.778629,-2.761475,-7.898568,-2.246907,2.141303,-6.704114,-4.349559,-5.084114,-8.127238,-7.128592,8.315022,-6.872937,0.075358,4.022626,8.402039,-6.928446,4.027513,8.276795,2.100756,-9.199659,-8.571332,1.384675,-4.325404,2.439670,3.928274,-5.669600,-8.509243,-8.347065,-0.420425,-9.228281,3.983872,-5.733364,1.538661,-3.676506,6.526089,6.880505,7.199551,-2.976753,-2.946080,-8.839283,-6.290758,-2.729975,1.280113,-0.207031,-5.016621,7.011078,4.043761,9.280422,6.762528,5.574594,-7.018094,2.217788,2.000791,7.642733,9.453462,-6.262191,-2.758635,-8.796700,8.781871,-6.861841,9.440919,3.186116,9.762056,-2.460273,-3.149475,-9.989210,-9.234888,-6.993478,2.139788,-6.628096,8.816475,-1.065102,1.341951,1.332365,1.175667,1.772755,9.196540,-2.158052,6.855889,6.991791,-5.558954,-9.673166,2.882517,8.054603,1.447760,0.272336,-7.572531,-6.923785,-6.847516,-9.618135,6.464807,2.891531,-2.767172,-1.847055,-5.975113,1.295613,6.342792,3.727162,-7.304918,4.069196,-1.736845,-1.582096,7.876675,3.440214,-3.762726,5.660870,1.311518,-9.585563,-4.770556,4.257065,-9.448301,-6.677309,-3.272342,4.689644,-5.075806,-8.876803,5.344650,9.522649,-0.096401,2.986259,-1.614152,-5.075086,1.698362,6.745453,6.818707,-6.675689,6.716635,4.213726,-3.405796,-9.816790,-8.734500,-7.189097,9.497452,-1.405872,-8.502058,-1.254633,-0.092290,-9.364742,5.778562,-1.741882,-9.088138,-7.631733,3.640712,1.303854,-3.798923,-5.367975,1.955252,1.797530,-1.047607,-3.399344,0.509653,7.054665,2.338868,6.866837,7.129941,-0.175136,-1.075817,2.534272,-6.157158,2.760274,-6.565020,9.127672,-8.557159,-1.583213,-2.936752,8.540192,7.175527,-9.672169,-6.163702,0.901107,7.631940,8.188247,-9.005257,2.789315,-3.894472,-6.503995,-4.825052,-8.225063,-9.655967,7.559368,1.591553,-1.278952,8.806221,0.197351,-8.126275,3.656527,-1.034772,9.835093,6.127298,-8.366221,5.389919,-4.416192,-5.915164,8.026794,1.482373,-9.654005,3.340790,0.060242,4.293280,8.186882], dtype = "float32")#candidate|5844|(288,)|const|float32
call_5843 = relay.TupleGetItem(func_2037_call(relay.reshape(const_5844.astype('float32'), [3, 6, 16]), relay.reshape(call_5830.astype('float32'), [468,]), ), 1)
call_5845 = relay.TupleGetItem(func_2040_call(relay.reshape(const_5844.astype('float32'), [3, 6, 16]), relay.reshape(call_5830.astype('float32'), [468,]), ), 1)
output = relay.Tuple([call_5824,call_5830,call_5833,call_5837,const_5838,call_5841,call_5843,const_5844,])
output2 = relay.Tuple([call_5825,call_5831,call_5834,call_5839,const_5838,call_5842,call_5845,const_5844,])
func_5852 = relay.Function([], output)
mod['func_5852'] = func_5852
mod = relay.transform.InferType()(mod)
output = func_5852()
func_5853 = relay.Function([], output)
mutated_mod['func_5853'] = func_5853
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2899_call = mod.get_global_var('func_2899')
func_2900_call = mutated_mod.get_global_var('func_2900')
call_5867 = relay.TupleGetItem(func_2899_call(), 1)
call_5868 = relay.TupleGetItem(func_2900_call(), 1)
output = relay.Tuple([call_5867,])
output2 = relay.Tuple([call_5868,])
func_5878 = relay.Function([], output)
mod['func_5878'] = func_5878
mod = relay.transform.InferType()(mod)
mutated_mod['func_5878'] = func_5878
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5878_call = mutated_mod.get_global_var('func_5878')
call_5879 = func_5878_call()
output = call_5879
func_5880 = relay.Function([], output)
mutated_mod['func_5880'] = func_5880
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5909 = relay.var("var_5909", dtype = "float32", shape = (11, 2, 10))#candidate|5909|(11, 2, 10)|var|float32
var_5910 = relay.var("var_5910", dtype = "float32", shape = (11, 2, 10))#candidate|5910|(11, 2, 10)|var|float32
bop_5911 = relay.maximum(var_5909.astype('float32'), relay.reshape(var_5910.astype('float32'), relay.shape_of(var_5909))) # shape=(11, 2, 10)
output = relay.Tuple([bop_5911,])
output2 = relay.Tuple([bop_5911,])
func_5914 = relay.Function([var_5909,var_5910,], output)
mod['func_5914'] = func_5914
mod = relay.transform.InferType()(mod)
mutated_mod['func_5914'] = func_5914
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5914_call = mutated_mod.get_global_var('func_5914')
var_5916 = relay.var("var_5916", dtype = "float32", shape = (11, 2, 10))#candidate|5916|(11, 2, 10)|var|float32
var_5917 = relay.var("var_5917", dtype = "float32", shape = (11, 2, 10))#candidate|5917|(11, 2, 10)|var|float32
call_5915 = func_5914_call(var_5916,var_5917,)
output = call_5915
func_5918 = relay.Function([var_5916,var_5917,], output)
mutated_mod['func_5918'] = func_5918
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5570_call = mod.get_global_var('func_5570')
func_5572_call = mutated_mod.get_global_var('func_5572')
call_5929 = relay.TupleGetItem(func_5570_call(), 0)
call_5930 = relay.TupleGetItem(func_5572_call(), 0)
func_5243_call = mod.get_global_var('func_5243')
func_5244_call = mutated_mod.get_global_var('func_5244')
call_5943 = relay.TupleGetItem(func_5243_call(), 0)
call_5944 = relay.TupleGetItem(func_5244_call(), 0)
func_4958_call = mod.get_global_var('func_4958')
func_4959_call = mutated_mod.get_global_var('func_4959')
call_5946 = func_4958_call()
call_5947 = func_4958_call()
bop_5963 = relay.logical_xor(call_5946.astype('uint64'), relay.reshape(call_5929.astype('uint64'), relay.shape_of(call_5946))) # shape=(468,)
bop_5966 = relay.logical_xor(call_5947.astype('uint64'), relay.reshape(call_5930.astype('uint64'), relay.shape_of(call_5947))) # shape=(468,)
output = relay.Tuple([call_5943,bop_5963,])
output2 = relay.Tuple([call_5944,bop_5966,])
func_5967 = relay.Function([], output)
mod['func_5967'] = func_5967
mod = relay.transform.InferType()(mod)
mutated_mod['func_5967'] = func_5967
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5967_call = mutated_mod.get_global_var('func_5967')
call_5968 = func_5967_call()
output = call_5968
func_5969 = relay.Function([], output)
mutated_mod['func_5969'] = func_5969
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3794_call = mod.get_global_var('func_3794')
func_3795_call = mutated_mod.get_global_var('func_3795')
call_5985 = relay.TupleGetItem(func_3794_call(), 0)
call_5986 = relay.TupleGetItem(func_3795_call(), 0)
output = call_5985
output2 = call_5986
func_5989 = relay.Function([], output)
mod['func_5989'] = func_5989
mod = relay.transform.InferType()(mod)
mutated_mod['func_5989'] = func_5989
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5989_call = mutated_mod.get_global_var('func_5989')
call_5990 = func_5989_call()
output = call_5990
func_5991 = relay.Function([], output)
mutated_mod['func_5991'] = func_5991
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6026 = relay.var("var_6026", dtype = "int16", shape = (16, 4, 8))#candidate|6026|(16, 4, 8)|var|int16
var_6027 = relay.var("var_6027", dtype = "int16", shape = (16, 4, 8))#candidate|6027|(16, 4, 8)|var|int16
bop_6028 = relay.logical_xor(var_6026.astype('int16'), relay.reshape(var_6027.astype('int16'), relay.shape_of(var_6026))) # shape=(16, 4, 8)
func_2967_call = mod.get_global_var('func_2967')
func_2968_call = mutated_mod.get_global_var('func_2968')
call_6037 = relay.TupleGetItem(func_2967_call(), 0)
call_6038 = relay.TupleGetItem(func_2968_call(), 0)
output = relay.Tuple([bop_6028,call_6037,])
output2 = relay.Tuple([bop_6028,call_6038,])
func_6040 = relay.Function([var_6026,var_6027,], output)
mod['func_6040'] = func_6040
mod = relay.transform.InferType()(mod)
var_6041 = relay.var("var_6041", dtype = "int16", shape = (16, 4, 8))#candidate|6041|(16, 4, 8)|var|int16
var_6042 = relay.var("var_6042", dtype = "int16", shape = (16, 4, 8))#candidate|6042|(16, 4, 8)|var|int16
output = func_6040(var_6041,var_6042,)
func_6043 = relay.Function([var_6041,var_6042,], output)
mutated_mod['func_6043'] = func_6043
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4250_call = mod.get_global_var('func_4250')
func_4252_call = mutated_mod.get_global_var('func_4252')
call_6045 = func_4250_call()
call_6046 = func_4250_call()
func_2899_call = mod.get_global_var('func_2899')
func_2900_call = mutated_mod.get_global_var('func_2900')
call_6062 = relay.TupleGetItem(func_2899_call(), 2)
call_6063 = relay.TupleGetItem(func_2900_call(), 2)
output = relay.Tuple([call_6045,call_6062,])
output2 = relay.Tuple([call_6046,call_6063,])
func_6065 = relay.Function([], output)
mod['func_6065'] = func_6065
mod = relay.transform.InferType()(mod)
mutated_mod['func_6065'] = func_6065
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6065_call = mutated_mod.get_global_var('func_6065')
call_6066 = func_6065_call()
output = call_6066
func_6067 = relay.Function([], output)
mutated_mod['func_6067'] = func_6067
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4958_call = mod.get_global_var('func_4958')
func_4959_call = mutated_mod.get_global_var('func_4959')
call_6100 = func_4958_call()
call_6101 = func_4958_call()
func_5779_call = mod.get_global_var('func_5779')
func_5782_call = mutated_mod.get_global_var('func_5782')
var_6121 = relay.var("var_6121", dtype = "float32", shape = (24, 12))#candidate|6121|(24, 12)|var|float32
call_6120 = relay.TupleGetItem(func_5779_call(relay.reshape(var_6121.astype('float32'), [4, 72])), 3)
call_6122 = relay.TupleGetItem(func_5782_call(relay.reshape(var_6121.astype('float32'), [4, 72])), 3)
func_4998_call = mod.get_global_var('func_4998')
func_5000_call = mutated_mod.get_global_var('func_5000')
call_6123 = relay.TupleGetItem(func_4998_call(), 0)
call_6124 = relay.TupleGetItem(func_5000_call(), 0)
var_6139 = relay.var("var_6139", dtype = "float32", shape = (4, 72))#candidate|6139|(4, 72)|var|float32
bop_6140 = relay.left_shift(call_6120.astype('uint16'), relay.reshape(var_6139.astype('uint16'), relay.shape_of(call_6120))) # shape=(4, 72)
bop_6143 = relay.left_shift(call_6122.astype('uint16'), relay.reshape(var_6139.astype('uint16'), relay.shape_of(call_6122))) # shape=(4, 72)
uop_6146 = relay.log10(bop_6140.astype('float32')) # shape=(4, 72)
uop_6148 = relay.log10(bop_6143.astype('float32')) # shape=(4, 72)
var_6153 = relay.var("var_6153", dtype = "float32", shape = (4, 72))#candidate|6153|(4, 72)|var|float32
bop_6154 = relay.minimum(call_6120.astype('uint64'), relay.reshape(var_6153.astype('uint64'), relay.shape_of(call_6120))) # shape=(4, 72)
bop_6157 = relay.minimum(call_6122.astype('uint64'), relay.reshape(var_6153.astype('uint64'), relay.shape_of(call_6122))) # shape=(4, 72)
output = relay.Tuple([call_6100,var_6121,call_6123,uop_6146,bop_6154,])
output2 = relay.Tuple([call_6101,var_6121,call_6124,uop_6148,bop_6157,])
func_6161 = relay.Function([var_6121,var_6139,var_6153,], output)
mod['func_6161'] = func_6161
mod = relay.transform.InferType()(mod)
var_6162 = relay.var("var_6162", dtype = "float32", shape = (24, 12))#candidate|6162|(24, 12)|var|float32
var_6163 = relay.var("var_6163", dtype = "float32", shape = (4, 72))#candidate|6163|(4, 72)|var|float32
var_6164 = relay.var("var_6164", dtype = "float32", shape = (4, 72))#candidate|6164|(4, 72)|var|float32
output = func_6161(var_6162,var_6163,var_6164,)
func_6165 = relay.Function([var_6162,var_6163,var_6164,], output)
mutated_mod['func_6165'] = func_6165
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3483_call = mod.get_global_var('func_3483')
func_3485_call = mutated_mod.get_global_var('func_3485')
call_6180 = relay.TupleGetItem(func_3483_call(), 0)
call_6181 = relay.TupleGetItem(func_3485_call(), 0)
func_5779_call = mod.get_global_var('func_5779')
func_5782_call = mutated_mod.get_global_var('func_5782')
const_6185 = relay.const([-6.116123,3.273664,-9.272244,0.149975,-4.987788,8.961304,8.053854,-9.136431,4.527408,4.968858,-1.462039,3.392447,-5.328402,8.712693,-9.561111,3.810634,7.212631,-2.105552,0.272767,-8.331552,0.972745,9.489042,7.659364,7.446490,5.798830,-5.571345,2.822111,-4.551125,-4.861715,5.021819,3.641761,-1.165459,9.124079,-7.095427,-0.789324,7.352197,-5.879462,8.664545,-6.639286,-3.670792,9.693711,-0.156779,-4.619015,5.747389,-0.054782,5.769606,4.272648,-8.696516,5.149556,-9.580046,-9.691764,5.697400,-8.057466,-4.512993,7.130824,3.441636,7.276150,2.665125,-2.824071,5.712031,-7.390493,-1.606303,-2.833509,-1.941825,3.330708,0.253962,-7.986547,-6.029532,0.281611,-8.568926,7.838040,-1.541738,4.309840,-7.385405,-7.159431,-6.909295,0.327681,-6.217000,5.219818,0.640403,1.101120,-0.724691,0.780737,0.448309,1.310138,0.555673,0.089819,-4.035613,-3.383069,-6.918741,-8.889756,4.313748,-8.645232,4.339148,-0.510829,-2.334031,8.982074,-8.384543,-8.749156,-2.405783,5.214484,-3.442059,1.906174,5.158094,-2.744175,-7.200352,-9.778976,-1.442411,6.153278,-1.375109,-1.340610,-2.528527,-7.833882,-7.631816,-2.435983,-7.165564,-4.733615,-3.151456,3.956900,4.061151,8.785639,-4.108259,3.161188,-6.018361,-1.475164,0.344722,-0.011403,9.090810,-3.177775,8.690833,-7.947936,-8.269726,-9.897369,-5.090939,-0.369025,7.466444,8.307257,5.931938,-8.108681,8.251240,-6.450316,6.797681,-6.603299,5.226229,-4.327207,3.598268,2.804189,-0.430693,-6.347827,4.232784,-0.192148,4.232635,3.714139,0.925792,-1.420575,-8.424777,6.671100,0.739795,-7.852188,-8.062673,5.854043,5.851472,3.425744,7.404620,-7.254671,-9.541206,8.758879,-6.253306,-7.974317,6.488806,7.739753,5.992825,9.887557,-5.239440,-2.562332,5.669587,6.676896,-0.413453,-5.321780,-3.962686,-9.898274,8.080132,-9.561549,-4.062797,4.438131,-5.364618,-1.771470,8.497546,-2.113036,2.643624,-0.040223,7.377410,-7.987049,-2.013752,1.688697,4.516175,8.283472,6.527615,4.668185,-9.464044,6.984229,7.364041,3.844459,-0.636232,-5.215925,-1.201970,-3.967669,-8.387280,1.529004,7.298901,-2.884616,-5.355492,7.131177,6.896413,-0.720238,-0.872739,-1.019316,2.374721,-4.750443,-5.669674,2.304143,-7.918989,-7.211678,-1.184563,2.394195,-5.735839,1.197687,-5.391570,-1.105760,2.116614,3.557632,4.078769,7.651715,0.427488,-4.550965,-6.152381,-0.136128,1.695321,-9.049607,-9.719924,4.196827,4.503130,-2.039997,1.987242,8.006273,8.174967,-1.264089,5.858780,3.236396,-5.530623,-5.878354,9.790923,3.685012,7.433155,6.539439,5.150496,-0.611569,1.493659,-4.771817,0.340419,3.174861,8.945948,2.914973,4.822106,2.886076,-9.050269,-8.879175,0.046871,-7.036831,4.913581,-5.786009,-1.505617,9.628616,6.625615,3.677085,-1.355246,9.220964,-4.678072,-1.181564,8.302990,3.150678,2.351525,-2.942013,3.132298,7.430981,-4.454962,-6.583466,-6.061276], dtype = "float32")#candidate|6185|(288,)|const|float32
call_6184 = relay.TupleGetItem(func_5779_call(relay.reshape(const_6185.astype('float32'), [4, 72])), 2)
call_6186 = relay.TupleGetItem(func_5782_call(relay.reshape(const_6185.astype('float32'), [4, 72])), 2)
output = relay.Tuple([call_6180,call_6184,const_6185,])
output2 = relay.Tuple([call_6181,call_6186,const_6185,])
func_6196 = relay.Function([], output)
mod['func_6196'] = func_6196
mod = relay.transform.InferType()(mod)
output = func_6196()
func_6197 = relay.Function([], output)
mutated_mod['func_6197'] = func_6197
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2967_call = mod.get_global_var('func_2967')
func_2968_call = mutated_mod.get_global_var('func_2968')
call_6202 = relay.TupleGetItem(func_2967_call(), 0)
call_6203 = relay.TupleGetItem(func_2968_call(), 0)
func_4998_call = mod.get_global_var('func_4998')
func_5000_call = mutated_mod.get_global_var('func_5000')
call_6204 = relay.TupleGetItem(func_4998_call(), 1)
call_6205 = relay.TupleGetItem(func_5000_call(), 1)
func_6065_call = mod.get_global_var('func_6065')
func_6067_call = mutated_mod.get_global_var('func_6067')
call_6206 = relay.TupleGetItem(func_6065_call(), 1)
call_6207 = relay.TupleGetItem(func_6067_call(), 1)
func_568_call = mod.get_global_var('func_568')
func_572_call = mutated_mod.get_global_var('func_572')
var_6213 = relay.var("var_6213", dtype = "float64", shape = (315,))#candidate|6213|(315,)|var|float64
call_6212 = relay.TupleGetItem(func_568_call(relay.reshape(var_6213.astype('float64'), [3, 7, 15]), relay.reshape(var_6213.astype('float64'), [3, 7, 15]), ), 2)
call_6214 = relay.TupleGetItem(func_572_call(relay.reshape(var_6213.astype('float64'), [3, 7, 15]), relay.reshape(var_6213.astype('float64'), [3, 7, 15]), ), 2)
output = relay.Tuple([call_6202,call_6204,call_6206,call_6212,var_6213,])
output2 = relay.Tuple([call_6203,call_6205,call_6207,call_6214,var_6213,])
func_6237 = relay.Function([var_6213,], output)
mod['func_6237'] = func_6237
mod = relay.transform.InferType()(mod)
mutated_mod['func_6237'] = func_6237
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6238 = relay.var("var_6238", dtype = "float64", shape = (315,))#candidate|6238|(315,)|var|float64
func_6237_call = mutated_mod.get_global_var('func_6237')
call_6239 = func_6237_call(var_6238)
output = call_6239
func_6240 = relay.Function([var_6238], output)
mutated_mod['func_6240'] = func_6240
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4958_call = mod.get_global_var('func_4958')
func_4959_call = mutated_mod.get_global_var('func_4959')
call_6298 = func_4958_call()
call_6299 = func_4958_call()
output = relay.Tuple([call_6298,])
output2 = relay.Tuple([call_6299,])
func_6300 = relay.Function([], output)
mod['func_6300'] = func_6300
mod = relay.transform.InferType()(mod)
mutated_mod['func_6300'] = func_6300
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6300_call = mutated_mod.get_global_var('func_6300')
call_6301 = func_6300_call()
output = call_6301
func_6302 = relay.Function([], output)
mutated_mod['func_6302'] = func_6302
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5989_call = mod.get_global_var('func_5989')
func_5991_call = mutated_mod.get_global_var('func_5991')
call_6305 = func_5989_call()
call_6306 = func_5989_call()
func_3461_call = mod.get_global_var('func_3461')
func_3462_call = mutated_mod.get_global_var('func_3462')
call_6307 = relay.TupleGetItem(func_3461_call(), 1)
call_6308 = relay.TupleGetItem(func_3462_call(), 1)
func_4998_call = mod.get_global_var('func_4998')
func_5000_call = mutated_mod.get_global_var('func_5000')
call_6337 = relay.TupleGetItem(func_4998_call(), 0)
call_6338 = relay.TupleGetItem(func_5000_call(), 0)
func_5852_call = mod.get_global_var('func_5852')
func_5853_call = mutated_mod.get_global_var('func_5853')
call_6339 = relay.TupleGetItem(func_5852_call(), 7)
call_6340 = relay.TupleGetItem(func_5853_call(), 7)
output = relay.Tuple([call_6305,call_6307,call_6337,call_6339,])
output2 = relay.Tuple([call_6306,call_6308,call_6338,call_6340,])
func_6348 = relay.Function([], output)
mod['func_6348'] = func_6348
mod = relay.transform.InferType()(mod)
mutated_mod['func_6348'] = func_6348
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6348_call = mutated_mod.get_global_var('func_6348')
call_6349 = func_6348_call()
output = call_6349
func_6350 = relay.Function([], output)
mutated_mod['func_6350'] = func_6350
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5170_call = mod.get_global_var('func_5170')
func_5172_call = mutated_mod.get_global_var('func_5172')
call_6419 = func_5170_call()
call_6420 = func_5170_call()
func_4008_call = mod.get_global_var('func_4008')
func_4012_call = mutated_mod.get_global_var('func_4012')
const_6424 = relay.const([4,-7,8,7,-8,3,2,-6,6,-4,6,-3,7,1,-1,-2,-10,1,6,1,3,-4,10,5,9,-8,-3,2,-9,10,5,6,8,-5,-3,8,4,2,3,-10,9,7,-3,6,4,-3,-7,-6,6,9,10,9,1,-8,1,9,9,5,-7,-3,6,-9,7,-8,-7,-4,8,2,5,8,-1,-5,4,-2,1,-1,-3,10,6,-1,-8,-1,-8,-8,3,6,-2,4,-3,7,2,-2,6,5,1,4,-2,-8,8,-1,1,-4,-2,-8,-5,-10,-1,-3,6,1,-3,9,-2,6,-2,-10,6,-5,-2,-3,8,-5,-8,9,6,1,7,-7,-6,8,1,10,-1,6,-10,2,6,8,-6,6,-7,3,7,-2,2,3,-9,1,-10,5,9,7,-5,-7,-9,4,2,-1,-5,3,4,-1,1,-3,2,-10,-5,4,1,2,-6,8,-2,-6,4,6,-7,3,10,6,3,-3,-2,-10,-10,-5,-7,-6,-1,-7,4,-7,2,-7,-5,6,-1,-8,-6,6,-9,4,-3,6,-5,-3,6,-9,7,1,-3,1,6,6,8,-9,4,-6,6,-3,4,-1,5,9,8,-7,6,4,9,-5,-4,5,-10,7,4,-8,-9,1,10,7,9,-8,1,-9,4,7,-8,7,5,5,-7,8,-3,9,8,-1,7,-3,3,-9,6,6,10,2,-1,-7,-2,-4,5,-8,7,-1,3,5,8,3,-1,9,-4,9,10,4,10,-8,-9,-9,8,-5,5,-6,-5,6,8,7,6,7,-1,-9,7,7,4,6,-5,-4,2,-3,9,-3,5,-10,8,-1,8,-10,-5,-5,-3,2,2,8,6,-1,1,1,-5,-8,-10,-2,9,7,10,-5,-3,-3,-5,-8,-10,-5,4,6,-8,-4,5,1,1,10,-8,-4,-3,5,-8,8,-4,7,-10,-9,9,-9,1,-8,7,-4,2,7,7,-3,7,-10,-6,-8,2,-7,1,5,5,2,3,9,4,-1,10,-5,-9,7,-4,2,-2,-8,4,-5,-9,2,-3,-7,9,-9,6,-7,6,2,8,-7,2,3,9,8,-5,1,-3,6,-8,2,-8,1,-2,-6,-7,-3,8,-9,-4,-6,7,-10,6,6,-10,2,-9,1,-5,2,-10,5,2,5,-10,6,8,10,1,-10,6,10,4,-7,-10,5,5,-10,-3,-5,-5,2,7,9,-10,1,-2,1,4,-9,8,-4,3,2,-10,8,-7,1,2,6,-1,-8,-7,1,9,-6,3,2,8,9,-10,-5,7,5,-8,-1,-7,3,8,-7,-3,3,-5,-1,8,10,9,7,1,-5,-10,-7,-3,-2,6,9,-2,-5,-7,9,8,-5,5,3,3,-5,2,1,2,-10,5,-8,-10,-6,-1,4,6,-6,-3,-7,7,-3,-3,8,-10,-6,6,1,-8,4,-4,1,-10,-3,8,-1,-1,5,9,-1,-10,3,2,-3,-3,-4,-7,-8,-3,-10,-2,-3,-5,9,2,2,-7,-7,9,3,-6,10,1,-10,1,-3,-1,6,-7,-2,4,-10,-9,4,-6,1,-2,-5,10,-5,-5,6,7,4,6,2,9,5,-8,7,3,-5,-10,-8,-4,-3,-3,7,-10,3,-6,-8,-6,5,1,7,-2,1,-3,-4,3,-7,4,-6,4,10,4,-7,4,-4,5,-1,6,-1,-2,-5,2,-1,6,3,-7,-8,-5,-1,8,-4,-1,-10,-8,3,7,2,1,-8,-1,5,-5,8,9,-9,-9,9,-7,-4,-1,-4,6,-10,1,4,-10,-9,3,7,1,8,-10,-9,-6,-3,-1,-5,-4,3,-4,7,-5,1,8,-9,-5,-8,-6,1,7,10,10,4,-2,-9,-6,-2,-7,-1,2,-3,-9,-1,5,6,7,-1,-1,1,3,-2,6,-2,-7,-7,2,-6,-10,-7,-1,8,-9,3,5,-5,-3,9,-1,4,3,4,3,8,9,10,-8,-5,7,-1,3,-3,5,8,3,1,-5,-3,9,4,9,-5,2,8,-10,-4,-6,-9,-8,-6,-9,9,6,-4,5,10,-10,3,-6,3,-9,-7,1,6,3,2,-3,-7,3,3,-9,-2,-9,-3,3,9,3,6,3,5,8,-9,-6,-7,10,-7,-2,-10,-1,5,8,-7,-1,-7,7,-2,9,3,10,4,-1,-10,7,5,2,-3,4,-3,3,9,10,-4,-5,-4,-8,-6,9,-3,4,8,7,-8,1,6,-9,-3,-8,-10,5,-7,-4,3,9,-4,5,-10,-3,-1,-8,-10,2,10,2,3,5,10,3,7,-1,-4,2,7,2,2,7,-9,-7,8,-8,-5,-3,6,-10,7,-3,8,-4,-5,-4,-6,-10,9,3,-7,10,-8,8,-8,-7,2,5,9,4,6,10,-9,7,8,-7,3,-6,10,-4,-4,5,-3,3,-2,6,7,9,6,5,-6,-10,2,9,-2,2,6,-10,-8,10,4,-7,2,8,-10,6,7,-6,-2,1,-9,-9,-2,5,4,9,1,-10,2,3,-2,9,-2,10,-1,9,-6,7,7,-8,-7,-8,5,-9,5,8,-10,-1,-3,8,2,5,4,-7,-4,-2,4,-7,-8,-3,-10,-2,-1,3,-4,9,6,5,8,1,-7,-2,2,9,10,3,-4,-10,-10,10,-4,9,6,2,-5,5,7,-4,-9,-9,4,8,-10,4,3,-1,6,-1,-3,-4,7,2,-7,4,-9,6,8,-1,4,6,1,6,-9,-8,1,3,-3,5,1,-7,-2,-4,-7,-9,-10,8,-4,9,-5,-6,-10,6,5,-5,-1,-9,-5,5,5,3,-1,-9,9,-8,8,1,-4,3,-8,-8,-1,6,-7,10,-5,1,5,-10,-9,-9,6], dtype = "int64")#candidate|6424|(1080,)|const|int64
call_6423 = relay.TupleGetItem(func_4008_call(relay.reshape(const_6424.astype('int64'), [12, 9, 10]), relay.reshape(const_6424.astype('int64'), [12, 9, 10]), ), 1)
call_6425 = relay.TupleGetItem(func_4012_call(relay.reshape(const_6424.astype('int64'), [12, 9, 10]), relay.reshape(const_6424.astype('int64'), [12, 9, 10]), ), 1)
func_3483_call = mod.get_global_var('func_3483')
func_3485_call = mutated_mod.get_global_var('func_3485')
call_6432 = relay.TupleGetItem(func_3483_call(), 0)
call_6433 = relay.TupleGetItem(func_3485_call(), 0)
func_3650_call = mod.get_global_var('func_3650')
func_3652_call = mutated_mod.get_global_var('func_3652')
var_6437 = relay.var("var_6437", dtype = "float32", shape = (288,))#candidate|6437|(288,)|var|float32
call_6436 = relay.TupleGetItem(func_3650_call(relay.reshape(var_6437.astype('float32'), [288,])), 0)
call_6438 = relay.TupleGetItem(func_3652_call(relay.reshape(var_6437.astype('float32'), [288,])), 0)
func_2037_call = mod.get_global_var('func_2037')
func_2040_call = mutated_mod.get_global_var('func_2040')
call_6466 = relay.TupleGetItem(func_2037_call(relay.reshape(var_6437.astype('float32'), [3, 6, 16]), relay.reshape(call_6432.astype('float32'), [468,]), ), 3)
call_6467 = relay.TupleGetItem(func_2040_call(relay.reshape(var_6437.astype('float32'), [3, 6, 16]), relay.reshape(call_6432.astype('float32'), [468,]), ), 3)
func_4161_call = mod.get_global_var('func_4161')
func_4164_call = mutated_mod.get_global_var('func_4164')
call_6483 = relay.TupleGetItem(func_4161_call(relay.reshape(call_6466.astype('float32'), [468,])), 2)
call_6484 = relay.TupleGetItem(func_4164_call(relay.reshape(call_6466.astype('float32'), [468,])), 2)
func_6040_call = mod.get_global_var('func_6040')
func_6043_call = mutated_mod.get_global_var('func_6043')
const_6510 = relay.const([-4,9,-9,-2,6,-10,10,-3,-9,8,3,8,1,-6,-4,6,-1,5,-5,2,6,4,8,-9,-2,6,8,5,-3,-10,10,-7,10,-1,-9,-4,-7,-3,6,3,-2,3,2,-9,-7,-3,4,7,2,-7,-1,7,1,-2,-3,-5,3,-5,6,-1,3,-1,4,1,6,-8,-2,4,5,10,-10,-5,3,-7,5,5,1,-7,7,-2,9,-9,-3,4,-8,7,9,10,-3,-4,-4,10,-6,10,-6,-6,10,-6,2,-2,4,10,-1,-7,7,7,-10,-5,-6,2,7,9,-7,2,-4,-10,4,-4,-10,1,2,-9,5,-1,-10,4,-2,7,-9,7,-5,-6,6,-4,-10,-2,-5,5,6,2,2,3,1,3,3,5,-8,-7,-8,-1,-7,1,5,-1,-5,-4,1,8,1,1,-5,2,-7,8,-3,8,-3,4,-6,-8,10,-5,-3,-2,-6,8,1,-5,-10,-8,3,5,-4,7,-3,-10,-8,3,-9,8,10,-7,8,1,-8,-3,4,8,-4,-9,-1,-2,-1,-2,10,8,-6,2,8,1,4,-6,1,-8,10,-6,4,9,2,8,3,-3,2,2,9,-5,-1,-3,6,9,-9,-6,-10,-2,10,6,7,-2,-5,8,-2,-6,3,-3,-1,6,7,4,-1,-4,8,2,-9,4,-1,-7,5,-3,-5,7,3,7,-7,9,-7,7,-3,3,-5,6,-9,-8,8,-3,2,-8,-5,-4,6,-10,-6,-10,-10,-1,-2,-3,-9,3,4,10,-8,-10,-5,-5,10,6,6,7,1,-3,4,-1,-4,-2,-2,4,-3,3,1,-9,-7,6,-10,-1,10,3,-7,7,-3,-2,1,5,2,-2,-9,-3,3,-10,-2,-6,-3,6,-7,3,-4,-5,1,-9,-9,6,-1,4,6,-10,5,3,-7,9,-4,2,-7,2,-6,-1,-5,4,-3,1,2,-2,-5,6,3,-6,10,-6,-4,7,1,-6,4,-2,8,-10,3,7,6,2,1,-8,-7,-9,3,10,1,-2,-7,4,8,-4,-6,2,6,-1,1,9,-2,-8,4,10,-7,-2,9,-8,2,9,-6,-7,-5,1,-8,6,1,-6,4,-4,-10,-5,-4,5,6,-3,-3,5,9,-5,-8,-6,5,-8,7,1,-8,-4,9,8,3,10,-2,-5,-10,-7,-1,1,-6,-6,9,-2,-4,-9,8,-10,9,-9,4,-3,6,5,4,5,3,4,-9,-8,5,-7,7,3,7,8,-8,6,-10,3,-6,-7,-2,-2,-7,5,10,-4,9,-2,9,-6,10,3,2,5,4,7,-2,6,-1,-3,3,9,-5,8,10,1,5,-1,9,5,7,9,2,1,6,-6], dtype = "int16")#candidate|6510|(512,)|const|int16
call_6509 = relay.TupleGetItem(func_6040_call(relay.reshape(const_6510.astype('int16'), [16, 4, 8]), relay.reshape(const_6510.astype('int16'), [16, 4, 8]), ), 1)
call_6511 = relay.TupleGetItem(func_6043_call(relay.reshape(const_6510.astype('int16'), [16, 4, 8]), relay.reshape(const_6510.astype('int16'), [16, 4, 8]), ), 1)
output = relay.Tuple([call_6419,call_6423,const_6424,call_6432,call_6436,var_6437,call_6466,call_6483,call_6509,const_6510,])
output2 = relay.Tuple([call_6420,call_6425,const_6424,call_6433,call_6438,var_6437,call_6467,call_6484,call_6511,const_6510,])
func_6513 = relay.Function([var_6437,], output)
mod['func_6513'] = func_6513
mod = relay.transform.InferType()(mod)
mutated_mod['func_6513'] = func_6513
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6514 = relay.var("var_6514", dtype = "float32", shape = (288,))#candidate|6514|(288,)|var|float32
func_6513_call = mutated_mod.get_global_var('func_6513')
call_6515 = func_6513_call(var_6514)
output = call_6515
func_6516 = relay.Function([var_6514], output)
mutated_mod['func_6516'] = func_6516
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5711_call = mod.get_global_var('func_5711')
func_5713_call = mutated_mod.get_global_var('func_5713')
call_6554 = func_5711_call()
call_6555 = func_5711_call()
func_4450_call = mod.get_global_var('func_4450')
func_4452_call = mutated_mod.get_global_var('func_4452')
call_6569 = relay.TupleGetItem(func_4450_call(relay.reshape(call_6554.astype('float32'), [78, 6])), 1)
call_6570 = relay.TupleGetItem(func_4452_call(relay.reshape(call_6554.astype('float32'), [78, 6])), 1)
output = relay.Tuple([call_6554,call_6569,])
output2 = relay.Tuple([call_6555,call_6570,])
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
func_4773_call = mod.get_global_var('func_4773')
func_4775_call = mutated_mod.get_global_var('func_4775')
call_6588 = func_4773_call()
call_6589 = func_4773_call()
func_4161_call = mod.get_global_var('func_4161')
func_4164_call = mutated_mod.get_global_var('func_4164')
call_6590 = relay.TupleGetItem(func_4161_call(relay.reshape(call_6588.astype('float32'), [468,])), 1)
call_6591 = relay.TupleGetItem(func_4164_call(relay.reshape(call_6588.astype('float32'), [468,])), 1)
func_4519_call = mod.get_global_var('func_4519')
func_4523_call = mutated_mod.get_global_var('func_4523')
call_6604 = relay.TupleGetItem(func_4519_call(relay.reshape(call_6590.astype('float64'), [112,]), relay.reshape(call_6588.astype('bool'), [12, 13, 3]), relay.reshape(call_6588.astype('bool'), [12, 13, 3]), ), 1)
call_6605 = relay.TupleGetItem(func_4523_call(relay.reshape(call_6590.astype('float64'), [112,]), relay.reshape(call_6588.astype('bool'), [12, 13, 3]), relay.reshape(call_6588.astype('bool'), [12, 13, 3]), ), 1)
func_2921_call = mod.get_global_var('func_2921')
func_2923_call = mutated_mod.get_global_var('func_2923')
call_6607 = relay.TupleGetItem(func_2921_call(), 0)
call_6608 = relay.TupleGetItem(func_2923_call(), 0)
func_4161_call = mod.get_global_var('func_4161')
func_4164_call = mutated_mod.get_global_var('func_4164')
call_6621 = relay.TupleGetItem(func_4161_call(relay.reshape(call_6588.astype('float32'), [468,])), 4)
call_6622 = relay.TupleGetItem(func_4164_call(relay.reshape(call_6588.astype('float32'), [468,])), 4)
func_7_call = mod.get_global_var('func_7')
func_11_call = mutated_mod.get_global_var('func_11')
call_6637 = relay.TupleGetItem(func_7_call(relay.reshape(call_6588.astype('float32'), [12, 13, 3]), relay.reshape(call_6588.astype('float32'), [12, 13, 3]), ), 0)
call_6638 = relay.TupleGetItem(func_11_call(relay.reshape(call_6588.astype('float32'), [12, 13, 3]), relay.reshape(call_6588.astype('float32'), [12, 13, 3]), ), 0)
output = relay.Tuple([call_6588,call_6590,call_6604,call_6607,call_6621,call_6637,])
output2 = relay.Tuple([call_6589,call_6591,call_6605,call_6608,call_6622,call_6638,])
func_6643 = relay.Function([], output)
mod['func_6643'] = func_6643
mod = relay.transform.InferType()(mod)
mutated_mod['func_6643'] = func_6643
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6643_call = mutated_mod.get_global_var('func_6643')
call_6644 = func_6643_call()
output = call_6644
func_6645 = relay.Function([], output)
mutated_mod['func_6645'] = func_6645
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4088_call = mod.get_global_var('func_4088')
func_4090_call = mutated_mod.get_global_var('func_4090')
call_6709 = relay.TupleGetItem(func_4088_call(), 0)
call_6710 = relay.TupleGetItem(func_4090_call(), 0)
output = call_6709
output2 = call_6710
func_6711 = relay.Function([], output)
mod['func_6711'] = func_6711
mod = relay.transform.InferType()(mod)
output = func_6711()
func_6712 = relay.Function([], output)
mutated_mod['func_6712'] = func_6712
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5852_call = mod.get_global_var('func_5852')
func_5853_call = mutated_mod.get_global_var('func_5853')
call_6719 = relay.TupleGetItem(func_5852_call(), 5)
call_6720 = relay.TupleGetItem(func_5853_call(), 5)
output = call_6719
output2 = call_6720
func_6721 = relay.Function([], output)
mod['func_6721'] = func_6721
mod = relay.transform.InferType()(mod)
output = func_6721()
func_6722 = relay.Function([], output)
mutated_mod['func_6722'] = func_6722
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6643_call = mod.get_global_var('func_6643')
func_6645_call = mutated_mod.get_global_var('func_6645')
call_6813 = relay.TupleGetItem(func_6643_call(), 3)
call_6814 = relay.TupleGetItem(func_6645_call(), 3)
func_4250_call = mod.get_global_var('func_4250')
func_4252_call = mutated_mod.get_global_var('func_4252')
call_6842 = func_4250_call()
call_6843 = func_4250_call()
output = relay.Tuple([call_6813,call_6842,])
output2 = relay.Tuple([call_6814,call_6843,])
func_6847 = relay.Function([], output)
mod['func_6847'] = func_6847
mod = relay.transform.InferType()(mod)
mutated_mod['func_6847'] = func_6847
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6847_call = mutated_mod.get_global_var('func_6847')
call_6848 = func_6847_call()
output = call_6848
func_6849 = relay.Function([], output)
mutated_mod['func_6849'] = func_6849
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2899_call = mod.get_global_var('func_2899')
func_2900_call = mutated_mod.get_global_var('func_2900')
call_6855 = relay.TupleGetItem(func_2899_call(), 0)
call_6856 = relay.TupleGetItem(func_2900_call(), 0)
output = relay.Tuple([call_6855,])
output2 = relay.Tuple([call_6856,])
func_6879 = relay.Function([], output)
mod['func_6879'] = func_6879
mod = relay.transform.InferType()(mod)
mutated_mod['func_6879'] = func_6879
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6879_call = mutated_mod.get_global_var('func_6879')
call_6880 = func_6879_call()
output = call_6880
func_6881 = relay.Function([], output)
mutated_mod['func_6881'] = func_6881
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4088_call = mod.get_global_var('func_4088')
func_4090_call = mutated_mod.get_global_var('func_4090')
call_6972 = relay.TupleGetItem(func_4088_call(), 0)
call_6973 = relay.TupleGetItem(func_4090_call(), 0)
var_6976 = relay.var("var_6976", dtype = "float32", shape = (468,))#candidate|6976|(468,)|var|float32
bop_6977 = relay.divide(call_6972.astype('float64'), relay.reshape(var_6976.astype('float64'), relay.shape_of(call_6972))) # shape=(468,)
bop_6980 = relay.divide(call_6973.astype('float64'), relay.reshape(var_6976.astype('float64'), relay.shape_of(call_6973))) # shape=(468,)
output = relay.Tuple([bop_6977,])
output2 = relay.Tuple([bop_6980,])
func_6988 = relay.Function([var_6976,], output)
mod['func_6988'] = func_6988
mod = relay.transform.InferType()(mod)
var_6989 = relay.var("var_6989", dtype = "float32", shape = (468,))#candidate|6989|(468,)|var|float32
output = func_6988(var_6989)
func_6990 = relay.Function([var_6989], output)
mutated_mod['func_6990'] = func_6990
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5369_call = mod.get_global_var('func_5369')
func_5371_call = mutated_mod.get_global_var('func_5371')
call_7010 = relay.TupleGetItem(func_5369_call(), 1)
call_7011 = relay.TupleGetItem(func_5371_call(), 1)
output = relay.Tuple([call_7010,])
output2 = relay.Tuple([call_7011,])
func_7014 = relay.Function([], output)
mod['func_7014'] = func_7014
mod = relay.transform.InferType()(mod)
mutated_mod['func_7014'] = func_7014
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7014_call = mutated_mod.get_global_var('func_7014')
call_7015 = func_7014_call()
output = call_7015
func_7016 = relay.Function([], output)
mutated_mod['func_7016'] = func_7016
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7038 = relay.const([[[4.754409],[-2.961245],[-2.399326],[9.272795],[6.752831],[4.403695],[5.634496],[4.366581]],[[7.274472],[-4.985529],[-3.520514],[1.438751],[0.876178],[-7.464197],[-9.769808],[-6.814565]],[[-7.894044],[4.914177],[-5.228027],[9.778317],[-3.245285],[1.338243],[3.218770],[-9.504690]],[[0.849401],[7.107540],[1.747806],[4.786908],[-6.165377],[6.400480],[2.751019],[-4.502886]],[[-8.101910],[-6.986488],[-1.991162],[5.506296],[-6.006263],[1.806493],[2.038690],[5.334510]],[[-3.079367],[-7.266750],[7.334438],[-5.703120],[9.987538],[-1.552990],[-6.862227],[1.371248]],[[0.885537],[8.541384],[1.498138],[-0.406262],[8.782335],[1.836172],[1.154309],[3.264622]],[[7.048494],[-7.843968],[0.725945],[6.026553],[-5.483135],[4.086305],[-0.467928],[-7.230683]],[[3.968774],[-5.978397],[-2.784635],[-5.958571],[-1.496728],[-9.167233],[-5.486989],[6.779247]],[[4.825855],[0.985592],[7.228154],[5.419390],[-4.533416],[-6.618345],[1.087398],[-4.044169]],[[-5.022884],[-8.458659],[6.251138],[-0.501796],[-4.186239],[-5.715000],[3.685093],[8.207630]],[[6.254076],[2.788489],[4.515439],[-2.679017],[-3.914976],[-4.429981],[3.634213],[-6.305908]],[[7.950111],[-1.895296],[6.644236],[-8.725336],[5.180652],[7.107708],[4.777496],[7.920927]],[[7.502456],[6.353696],[-4.952328],[-4.333179],[-0.165852],[-1.219238],[-2.937027],[0.179597]],[[2.557020],[-8.997632],[-6.922626],[0.282061],[9.938481],[-9.172776],[0.233077],[6.107758]]], dtype = "float64")#candidate|7038|(15, 8, 1)|const|float64
uop_7039 = relay.sqrt(const_7038.astype('float64')) # shape=(15, 8, 1)
uop_7041 = relay.acos(const_7038.astype('float64')) # shape=(15, 8, 1)
bop_7048 = relay.power(uop_7039.astype('float32'), relay.reshape(uop_7041.astype('float32'), relay.shape_of(uop_7039))) # shape=(15, 8, 1)
bop_7058 = relay.minimum(bop_7048.astype('float32'), relay.reshape(uop_7039.astype('float32'), relay.shape_of(bop_7048))) # shape=(15, 8, 1)
func_3461_call = mod.get_global_var('func_3461')
func_3462_call = mutated_mod.get_global_var('func_3462')
call_7065 = relay.TupleGetItem(func_3461_call(), 1)
call_7066 = relay.TupleGetItem(func_3462_call(), 1)
bop_7091 = relay.less(call_7065.astype('bool'), uop_7039.astype('bool')) # shape=(15, 8, 468)
bop_7094 = relay.less(call_7066.astype('bool'), uop_7039.astype('bool')) # shape=(15, 8, 468)
func_4752_call = mod.get_global_var('func_4752')
func_4754_call = mutated_mod.get_global_var('func_4754')
call_7096 = relay.TupleGetItem(func_4752_call(), 0)
call_7097 = relay.TupleGetItem(func_4754_call(), 0)
bop_7098 = relay.add(call_7065.astype('float64'), bop_7058.astype('float64')) # shape=(15, 8, 468)
bop_7101 = relay.add(call_7066.astype('float64'), bop_7058.astype('float64')) # shape=(15, 8, 468)
func_4958_call = mod.get_global_var('func_4958')
func_4959_call = mutated_mod.get_global_var('func_4959')
call_7102 = func_4958_call()
call_7103 = func_4958_call()
output = relay.Tuple([bop_7091,call_7096,bop_7098,call_7102,])
output2 = relay.Tuple([bop_7094,call_7097,bop_7101,call_7103,])
func_7107 = relay.Function([], output)
mod['func_7107'] = func_7107
mod = relay.transform.InferType()(mod)
mutated_mod['func_7107'] = func_7107
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7107_call = mutated_mod.get_global_var('func_7107')
call_7108 = func_7107_call()
output = call_7108
func_7109 = relay.Function([], output)
mutated_mod['func_7109'] = func_7109
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4088_call = mod.get_global_var('func_4088')
func_4090_call = mutated_mod.get_global_var('func_4090')
call_7136 = relay.TupleGetItem(func_4088_call(), 2)
call_7137 = relay.TupleGetItem(func_4090_call(), 2)
output = relay.Tuple([call_7136,])
output2 = relay.Tuple([call_7137,])
func_7144 = relay.Function([], output)
mod['func_7144'] = func_7144
mod = relay.transform.InferType()(mod)
output = func_7144()
func_7145 = relay.Function([], output)
mutated_mod['func_7145'] = func_7145
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4773_call = mod.get_global_var('func_4773')
func_4775_call = mutated_mod.get_global_var('func_4775')
call_7180 = func_4773_call()
call_7181 = func_4773_call()
output = call_7180
output2 = call_7181
func_7187 = relay.Function([], output)
mod['func_7187'] = func_7187
mod = relay.transform.InferType()(mod)
mutated_mod['func_7187'] = func_7187
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7187_call = mutated_mod.get_global_var('func_7187')
call_7188 = func_7187_call()
output = call_7188
func_7189 = relay.Function([], output)
mutated_mod['func_7189'] = func_7189
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5711_call = mod.get_global_var('func_5711')
func_5713_call = mutated_mod.get_global_var('func_5713')
call_7217 = func_5711_call()
call_7218 = func_5711_call()
func_4738_call = mod.get_global_var('func_4738')
func_4740_call = mutated_mod.get_global_var('func_4740')
call_7222 = relay.TupleGetItem(func_4738_call(), 1)
call_7223 = relay.TupleGetItem(func_4740_call(), 1)
output = relay.Tuple([call_7217,call_7222,])
output2 = relay.Tuple([call_7218,call_7223,])
func_7224 = relay.Function([], output)
mod['func_7224'] = func_7224
mod = relay.transform.InferType()(mod)
mutated_mod['func_7224'] = func_7224
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7224_call = mutated_mod.get_global_var('func_7224')
call_7225 = func_7224_call()
output = call_7225
func_7226 = relay.Function([], output)
mutated_mod['func_7226'] = func_7226
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7224_call = mod.get_global_var('func_7224')
func_7226_call = mutated_mod.get_global_var('func_7226')
call_7244 = relay.TupleGetItem(func_7224_call(), 1)
call_7245 = relay.TupleGetItem(func_7226_call(), 1)
func_4224_call = mod.get_global_var('func_4224')
func_4228_call = mutated_mod.get_global_var('func_4228')
const_7253 = relay.const([2,5,3,-4,6,2,10,2,4,10,-5,-4,9,-9,5,-9,3,10,3,5,-10,5,-8,6,6,-2,8,7,1,8,2,-10,1,-9,5,-4,-2,3,-5,-2,2,1,9,7,5,-3,-5,2,-4,-10,6,4,-6,-9,-5,-1,6,-6,9,-2,-1,1,-1,-1,3,-4,9,10,4,-4,2,-5,-7,-1,4,-3,10,10,7,6,5,9,-9,-7,8,-1,9,7,7,-2,-3,8,9,7,-9,5,7,8,-5,-9,8,-3,6,-1,-10,-5,-2,-10,-9,8,-4,-2,9,6,-4,-4,7,-9,9,-5,5,-4,3,7,-3,-9,-7,7,-2,-9,10,-9,3,9,8,-1,-5,1,10,-7,-4,-9,9,9,1,-8,-1,5,4,4,-9,4,-1,-10,-4,4,-5,-1,1,8,5,-2,-2,2,10,-8,2,-10,9,-6,9,1,4,-10,1,8,5,-4,-6,5,-2,-2,-6,-9,-4,-8,-4,-7,-2,-5,7,8,-3,1,1,-5,8,9,-4,9,-1,1,9,-6,-6,-3,-6,5,5,1,1,-1,5,-10,-6,7,7,5,-5,-6,-3,2,-2,-1,2,-5,9,-1,-3,3,2,-7,5,7,-2,-1,-2,4,-9,-10,-8,5,10,10,-6,3,3,1,3,-10,-10,1,1,7,2,-4,-4,-6,6,8,-10,-2,-2,-3,-10,3,1,2,-1,5,-8,-2,9,-5,-5,-6,5,-8,-10,3,1,10,9,-7,2,-4,10,-1,3,3,-10,-2,9,-3,10,-1,-1,4,-4,2,2,6,-3,4,-4,3,8,-10,-7,7,8,-8,-10,3,-3,2,3,1,7,-2,-2,9,-2,6,2,5,-1,3,7,-5,-10,-10,-5,9,-6,-4,-5,8,-2,7,10,-5,8,2,3,6,4,-8,-6,-2,-7,-1,-7,-2,-5,-2,4,4,5,-5,-5,2,6,-8,-7,3,7,8,2,3,-10,10,2,4,-4,-4,2,6,-7,2,-7,8,10,-7,6,10,5,-10,8,4,6,8,-5,-8,3,8,5,-5,4,9,-4,-7,-1,-7,2,-2,1,-8,6,-1,-6,-10,-5,-9,-9,-10,-7,3,6,10,3,-8,-2,1,4,9,-10,-4,6,-5,-10,-1,4,7,-5,-7,9,-1,4,8,-3,-10,6,2,-5,-10,-4,4,-4,-7,9,7,1,-6,-1,3,-1,-1,-6,10,7,-8,10,8,-6,3,1,3,10,-7,4,-7,4,4,10,-3,4,10,5,8,-5,7,2,5,1,-5,3,-2,1,-9,9,-7,-3,-7,-7,10,-7,-5,8,1,4,-6,1,6,-5,-2,-4,9,10,-6,2,-6,-6,6,-2,5,6,-5,-1,-8,5,-1,2,6,6,8,1,-5,-4,-1,9,-4,-7,-1,-7,3,2,1,-3,-6,3,9,8,9,6,-10,-5,-1,3,-1,2,4,-7,9,-4,-1,9,-10,-3,-10,-2,5,5,10,-7,-8,-4,-6,-7,-2,-8,-9,4,-5,-2,-5,5,2,5,8,4,4,10,2,3,-10,9,-9,3,-10,-6,9,-5,1,-4,4,9,-5,-6,-6,-1,1,10,-4,3,-7,-9,2,9,5,-4,-1,-7,-2,3,3,8,7,5,2,5,8,-8,-9,-6,10,5,3,-8,-4,-6,-9,2,-4,-7,-6,-6,8,5,-2,-2,-10,-4,9,-9,4,-2,10,1,3,-10,10,-1,9,6,4,-4,6,-7,-1,-8,4,10,-5,9,10,-5,5,-9,-2,6,4,2,9,5,-10,6,4,-7,8,-5,5,-9,7,-5,-4,7,-2,-7,2,10,4,3,2,7,8,-6,-3,1,2,9,6,3,-6,-8,2,-10,4,4,-7,-5,2,-8,-8,-3,5,-8,9,-1,-2,5,9,-8,-1,10,-3,3,-10,-8,-7,1,-2,-7,10,6,-8,-6,6,-1,-8,5,8,5,-6,-6,-6,9,6,9,-1,-8,7,6,-7,10,-8,7,2,3,6,3,6,10,-5,10,5,4,1,5,9,-5,10,-2,-5,8,-6,-5,-2,-6,3,2,-3,2,-10,-4,-10,-5,-3,1,-2,9,-2,10,-9,-3,-2,2,3,9,-1,-2,4,-1,4,2,5,-6,8,-2,-2,-9,10,-10,-7,8,-4,9,10,4,4,-4,9,-7,-5,4,-4,4,8,8,-6,3,1,-9,-4,6,1,8,-9,-7,-3,-4,5,10,-3,-1,9,9,8,10,1,3,-8,-1,5,1,-10,7,-2,-1,7,4,-7,-5,-10,-8,-5,-4,3,1,-5,10,-9,1,3,-6,5,8,2,-7,-2,-5,8,-1,-5,1,-7,5,7,7,9,2,-3,6,-8,10,-9,-7,4,-10,-2,-9,1,7,2,-9,9,-5,-4,10,3,3,4,-9,-10,7,9,5,10,9,7,-2,-9,-3,-9,6,2,6,-1,-4,5,7,9,-5,3,10,-1,-6,-3,-5,3,-6,3,1,-10,-7,8,8,-5,6,-8,7,3,10,-4,8,-8,-10,-8,-7,10,3,9,5,6,-1,10,-6,1,8,-2,-3,-1,-3,6,9,-7,5,-6,1,4,8,2,-8,9,10,-2,-4,-6,4,-1,9,5,-8,-6,3,-3,-7,-3,7,1,-5,-10,6,8,-7,2,8,2,6,-5,10,-10,-2,-2,-6,8,-7,-2,2,4,-2,-7,-4,8,-9,-1,-10,7,-5,-5,-3,-4,-9,5,10,-3,6,3,-9,1,4,8,-2,-10,-6,-8,5,-1,-8,-8,-6,1,8,-9,6,8,2,8,3,-9,-2,-1,-8,-1,-9,-7,9,6,-3,-6,-6,1,-10,-2,-6,3,-9,-4,7,5,6,2,9,3,-4,3,3,6,4,8,10,-7,-6,-5,-6,-10,2,8,-9,-7,7,-2,5,-6,7,-6,-5,-5,-4,3,-1,-4,6,-6,10,9,3,-10,9,-7,9,-1,-8,3,-7,4,3,2,-10,4,4,-9,-3,7,-6,8,8,8,-6,-8,1,-10,1,-2,10,3,9,3,3,-8,2,2,5,-4,3,5,-3,6,9,-5,6,-5,1,1,-5,3,-4,7,-7,4,4,-5,6,-1,1,-6,-5,6,-8,-2,-7,-2,3,2,-2,-1,-8,5,10,-9,-3,10,5,-6,4,-7,4,-1,1,-9,2,1,-6,1,2,7,-4,-5,-4,3,-10,6,-10,-3,2,5,-9,3,-5,-3,6,-4,6,3,-2,-7,-7,-6,-2,7,10,10,-10,-7,1,2,10,10,-5,8,-9,10,8,2,-7,-5,-3,-6,-10,-10,5,-10,9,-2,5,2,5,-10,9,2,-1,3,-4,8,4,-6,-1,-3,-6,-5,-5,5,-8,-2,4,-3,2,10,-4,1,8,8,-4,2,-8,-1,5,-4,10,9,1,-1,-7,9,1,1,9,-1,-2,5,1,6,3,-8,-5,6,-9,9,8,-7,-9,-8,-8,3,3,4,3,9,-10,-6,-4,-1,1,-6,1,10,4,10,1,3,-1,-10,-7,-8,-8,1,9,4,3,1,-7,-6,10,-10,9,-7,-2,-3,-7,-3,-7,8,6,6,-6,-5,-9,-2,7,2,-7,8,-5,8,4,-9,-6,7,-9,-1,-9,5,-7,8,1,2,10,-7,1,-7,7,-5,2,-2,4,-7,-2,-2,-1,3,-2,-10,-4,-7,2,-9,-1,1,6,-8,9,-3,2,-9,8,5,-6,-4,3,7,-5,-6,1,-4,3,7,-9,-2,-8,4,-5,-9,5,3,-3,5,7,8,9,6,4,-3,-8,6,9,5,10,-7,5,4,2,-8,1,8,-8,1,10,8,2,-5,3,-5,1,-9,3,4,5,4,-8,7,9,-9,-3,-8,-1,5,2,-7,9,-1,9,8,7,-1,6,-2,-5,5,-8,-4,7,-2,-7,-6,-5,1,-2,10,-2,-8,-9,5,-1,-4,5,-9,5,-5,-2,-9,10,3,-8,3,5,10,2,-10,8,-6,-9,-9,-8,-7,7,-7,7,-9,6,6,-5,-7,-4,2,8,6,4,-4,-10,-1,8,-2,-10,1,-4,9,-7,-4,3,4,-5,1,-8,10,-7,-4,10,1,8,-10,-2,10,7,-2,-4,-4,-9,-6,1,4,8,-4,-6,2,8,8,1,1,6,8,2,-6,-6,-7,-10,-6,10,9,-4,4,3,4,-2,9], dtype = "int8")#candidate|7253|(1584,)|const|int8
const_7254 = relay.const([0.240254,9.034365,-6.271847,-0.883746,3.508034,8.240676,-6.041898,-0.349460,6.388616,3.088618,-0.236702,-4.229429,9.200870,-1.393613,-6.002812,2.728717,-6.273440,3.659902,-0.652191,-2.481030,0.019413,3.165871,8.000468,4.421341,-4.985527,5.285086,-0.692364,-9.931574,-7.040905,-6.094123,-7.466178,2.646832,-0.979690,0.667699,-2.790147,-0.952950,-1.348843,-8.825958,-9.693867,-1.056919,-4.064049,0.790920,8.160437,-5.506930,-6.950347,-4.137760,2.933748,4.539555,-0.202374,-0.983885,5.759932,3.770333,-0.856096,7.439025,0.156044,8.892766,6.750567,-9.323859,-5.501713,3.010721,0.577177,6.614964,7.638222,9.935136,-6.441780,-5.515622,-3.659465,5.496279,5.023792,7.943138,-4.441251,0.397910,2.940468,-5.184879,-8.014166,4.571057,8.516268,-3.766905,5.794579,-2.865529,-0.103239,0.709520,-1.747364,5.395816,-4.924579,6.287358,-6.404895,-6.403184,-9.939786,3.583901,-7.337766,6.291000,-8.794951,-6.080946,3.317947,4.419309,-8.830972,-9.721218,5.581720,-4.449764,7.910788,-6.039616,-1.500632,2.885360,4.962915,-1.121331,9.812100,2.530356,4.377571,-6.048562,-1.732031,-0.938375,-0.364321,-7.180362,0.789257,3.430851,-4.608202,-3.757813,0.537082,3.132541,-8.518055,-6.629336,5.485260,4.393828,-3.042893,2.812784,1.607541,7.743476,5.618565,1.479668,-1.257061,9.901987,-1.248304,-1.870578,5.014081,-7.165606,1.824695,-6.246962,-5.144757,0.120387,2.573349,-4.497346,9.254083,-1.812062,4.349175,9.234737,9.686063,-8.004568,-5.467822,3.776834,-7.023691,0.660258,-3.591286,2.622037,-3.447685,9.333328,6.190027,-7.524792,8.339930,1.856358,4.365673,7.010687,6.927135,-7.156035,-3.002851,-3.168086,-3.499377,-1.557454,4.116129,4.102594,-1.158056,9.712196,-5.793580,-2.429760,-5.567142,-9.737466,-1.001063,-7.424861,3.285335,6.343773,-6.330932,0.687545,-7.625348,-2.645350,4.987768,5.709671,-8.953226,2.393288,-4.635370,5.938689,-3.568672,-1.512328,1.031836,-2.054496,-8.992973,-8.447903,2.241849,2.281578,4.758581,1.507061,9.562030,-7.767727,2.992040,2.701939,-0.520105,4.019181,-2.622478,9.546193,-6.258833,5.819092,-8.646243,-8.731592,1.740569,8.227301,7.722108,6.460715,3.839220,-2.136102,2.549554,-4.383494,-7.472723,-9.762661,-7.688169,-9.617780,-7.611978,8.122629,7.334426,-2.387540,1.704281,3.562962,2.276832,0.092825,6.770463,7.537067,3.326559,-3.798243,3.820613,9.528670,-1.410034,6.830658,8.886351,9.095428,-5.634433,1.894794,3.883150,-6.208829,5.572474,1.961230,6.058603,6.623187,6.686211,0.699148,0.106404,-6.523186,-7.537677,-1.630030,-8.928498,3.338581,5.060907,-5.653785,6.394994,6.812416,-6.770086,1.217408,-5.036389,5.965464,-4.608845,-5.393102,9.821245,-9.759489,-3.794075,8.857499,-9.225208,0.120092,6.447888,9.787442,-1.726422,4.192823,2.297882,5.262055,5.433310,0.829022,4.285539,6.574042,-4.079299,-3.300545,-7.267082,3.939389,-5.601775,4.447779,-6.308733,0.490654,4.364880,-2.134297,2.683193,-7.140141,-3.213845,4.038906,-8.307419,-8.819136,-9.662923,5.391264,-9.146881,5.811836,-6.355496,-3.298755,8.413549,8.719661,-9.590337,-8.561040,8.129793,-6.142363,-7.250399,0.976163,8.660291,-1.737695,8.644968,-3.806641,-1.728298,-3.999736,-7.236449,-9.581913,-2.457271,6.820612,3.520145,9.854646,-9.199037,-2.954912,7.357010,5.743619,8.280546,-9.396913,-8.539930,-6.651664,-6.824586,0.479739,3.264561,6.482185,9.420397,-3.902568,-8.418675,-5.711184,5.054317,6.259274,-4.211154,4.810264,-3.773109,-1.645320,6.235083,-8.658055,-5.191731,-2.536490,2.707855,3.229521,-3.599225,0.833692,4.978076,-3.881224,-9.128512,9.954963,-0.844869,-2.087264,-1.907649,8.870759,2.696139,-1.211362,5.170663,0.450947,-6.393549,-2.004540,-2.701542,0.830062,1.164228,-7.838509,0.563515,-1.400032,3.254613,6.225692,-1.595468,0.356780,-7.314000,6.313674,-0.808034,-1.172515,5.690975,-3.360771,-8.893037,-7.883032,6.193479,1.764771,-4.288741,-6.483483,-9.171669,-9.904001,5.732340,-6.314948,3.247511,7.145497,-9.332198,-0.263141,-4.395825,4.897436,-2.540438,-6.207561,-5.122957,-8.075301,-4.775674,-0.096556,-3.305072,5.995904,-2.131179,1.914208,9.725185,-0.290391,-0.675345,0.183170,9.460017,7.202945,-4.676995,9.669021,2.532546,-6.066926,-5.445694,-2.078430,9.726904,-8.334093,8.159105,9.595682,3.084530,-3.147159,-9.056054,-7.956399,-9.903673,2.692241,-4.619443,-1.748132,-7.228226,0.916799,4.521689,-3.547489,1.758439,1.986616,-3.312912,3.292346,-2.243717,-2.001380,3.522968,-3.457394,-0.106961,8.288237,-4.587742,6.850454,-2.762123,9.005036,-0.447501,-3.528187,5.784929,2.101373,-2.647392,9.686265,-7.675607,7.196888,-6.945584,-5.006030,4.998294,6.658500,6.697671,-3.680069,3.465531,0.877892,0.824838,8.721380,9.287487,3.042573,4.323062,-2.500668,-9.610097,-7.482289,5.846178,7.460917,-5.260336,-8.078226,6.534924,4.061163,4.512192,0.655713,-0.153652,0.169269,1.043246,6.458419,1.810674,-8.698247,6.702525,-2.415386,3.406672,0.806523,1.037453,0.774484,-8.574323,8.370604,-2.599120,2.824992,-8.335169,-7.365652,1.665656,-0.265085,-6.471211,-5.337973,4.948570,-9.860566,-5.859672,-0.129400,-9.233251,6.319772,-5.996009,-6.491998,9.128423,2.519981,-7.906831,2.723094,0.442567,-9.205980,-5.409783,9.765832,0.108780,6.729189,3.706573,1.864846,5.596430,6.624197,-8.714803,-2.993975,5.523463,7.592391,-2.251058,1.553103,-6.766564,9.767136,-8.297657,1.813366,-9.583230,1.766710,-2.126959,0.954052,8.893702,-9.102534,-8.127136,1.975252,-5.992504,0.654769,7.395339,1.813317,-9.651888,9.790247,4.309758,5.275186,6.331851,-7.697186,4.390273,0.885902,-3.137003,-6.864022,1.198859,-5.058827,-0.155660,-3.419273,-8.699813,-8.046488,-8.603483,4.303486,-4.370542,4.741442,4.011065,0.461616,-1.068834,-3.166484,-6.663322,6.769958,-7.929177,-2.322363,-0.071643,7.969888,-3.983707,0.790558,4.503041,-6.729055,9.445458,6.837740,9.144902,-3.527931,6.297971,-8.206968,5.005589,1.742241,8.647825,2.876469,-8.926790,-3.372276,-1.726835,7.561076,-6.719361,8.710706,-1.429358,4.559237,2.064101,2.137980,-4.811408,5.820351,5.790082,8.321010,-6.731773,-9.657497,5.456935,1.270109,2.246056,6.418771,-3.692041,9.641826,8.221508,6.206349,-6.261517,-7.927279,-9.326571,9.008946,-3.866267,4.859019,5.415276,-5.238321,-5.247712,-3.262388,-1.327235,-6.582367,-9.489042,0.448231,-0.398165,-3.153361,4.266929,5.790770,-7.404188,-3.831045,8.830784,3.699433,0.879995,-5.663897,9.720364,2.391777,-3.326428,3.318728,-0.779671,3.590800,8.710555,1.940025,-3.828145,-7.477338,8.011964,0.433987,-9.060006,7.765943,-3.592943,-1.291176,-5.729064,-1.910063,0.136751,3.075631,-8.305137,-7.445635,1.562594,7.681209,-4.868883,-2.369676,-2.847456,-7.952574,5.184787,-2.215813,8.454934,2.776164,5.363763,1.760457,0.484375,-2.642072,4.056416,2.872597,-1.119114,-4.769848,6.536982,0.883963,-7.905922,-1.521141,3.791664,-2.336561,8.333560,2.851201,5.500351,0.160346,8.987191,-6.396113,-3.766299,7.113161,-3.576147,2.380497,5.954651,3.898660,0.296367,6.721204,9.813694,1.718349,3.534843,8.277842,5.565842,-9.335142,-5.213722,2.466251,-6.911420,9.265319,-7.430481,-4.798278,4.688011,-1.215208,-1.897584,-2.687845,7.396888,-7.794291,-2.536561,9.263847,8.348884,-9.375505,-9.605999,-3.715596,9.194499,-3.019190,0.196584,2.145593,-9.536044,3.557511,5.283553,-9.902379,9.669058,7.023322,-5.813156,-3.905383,-9.051200,7.973476,-1.917084,-0.315387,-9.224912,-8.407300,3.485651,-3.402596,6.617015,-7.782405,5.359052,0.192014,-4.336819,-3.800274,1.831643,-3.069548,-2.583968,-0.533778,4.390260,-6.383320,8.978211,8.869699,-2.608292,8.447387,4.685957,-9.682238,-6.714020,-1.208523,-2.240471,-7.997004,9.003946,-1.460280,-9.465901,-1.937759,5.892202,6.883525,4.152398,7.713640,8.633026,0.563773,2.748896,2.043339,8.070817,-7.699887,6.405654,2.405879,3.511499,-3.890135,4.372828,9.415818,2.516980,0.010785,-7.196923,-8.200183,8.110815,-2.650388,9.001285,9.898623,4.880449,-5.400937,-3.961632,4.028467,6.930504,2.194616,4.146796,8.492887,-6.048503,4.861096,-4.018911,-2.400129,-6.073344,-0.156863,-2.382403,-3.088087,9.271564,-4.823495,3.712813,2.336229,0.061475,4.788880,3.906187,2.416965,3.423035,-7.526245,-5.658304,-4.910630,-8.651961,-5.554703,-3.841772,-4.695415,-9.092910,4.813148], dtype = "float32")#candidate|7254|(832,)|const|float32
call_7252 = relay.TupleGetItem(func_4224_call(relay.reshape(const_7253.astype('int8'), [12, 12, 11]), relay.reshape(const_7253.astype('int8'), [12, 12, 11]), relay.reshape(const_7254.astype('float32'), [832,]), ), 0)
call_7255 = relay.TupleGetItem(func_4228_call(relay.reshape(const_7253.astype('int8'), [12, 12, 11]), relay.reshape(const_7253.astype('int8'), [12, 12, 11]), relay.reshape(const_7254.astype('float32'), [832,]), ), 0)
output = relay.Tuple([call_7244,call_7252,const_7253,const_7254,])
output2 = relay.Tuple([call_7245,call_7255,const_7253,const_7254,])
func_7258 = relay.Function([], output)
mod['func_7258'] = func_7258
mod = relay.transform.InferType()(mod)
output = func_7258()
func_7259 = relay.Function([], output)
mutated_mod['func_7259'] = func_7259
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3779_call = mod.get_global_var('func_3779')
func_3780_call = mutated_mod.get_global_var('func_3780')
call_7265 = func_3779_call()
call_7266 = func_3779_call()
func_7144_call = mod.get_global_var('func_7144')
func_7145_call = mutated_mod.get_global_var('func_7145')
call_7297 = relay.TupleGetItem(func_7144_call(), 0)
call_7298 = relay.TupleGetItem(func_7145_call(), 0)
func_5369_call = mod.get_global_var('func_5369')
func_5371_call = mutated_mod.get_global_var('func_5371')
call_7301 = relay.TupleGetItem(func_5369_call(), 1)
call_7302 = relay.TupleGetItem(func_5371_call(), 1)
output = relay.Tuple([call_7265,call_7297,call_7301,])
output2 = relay.Tuple([call_7266,call_7298,call_7302,])
func_7317 = relay.Function([], output)
mod['func_7317'] = func_7317
mod = relay.transform.InferType()(mod)
output = func_7317()
func_7318 = relay.Function([], output)
mutated_mod['func_7318'] = func_7318
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3779_call = mod.get_global_var('func_3779')
func_3780_call = mutated_mod.get_global_var('func_3780')
call_7328 = func_3779_call()
call_7329 = func_3779_call()
output = call_7328
output2 = call_7329
func_7339 = relay.Function([], output)
mod['func_7339'] = func_7339
mod = relay.transform.InferType()(mod)
mutated_mod['func_7339'] = func_7339
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7339_call = mutated_mod.get_global_var('func_7339')
call_7340 = func_7339_call()
output = call_7340
func_7341 = relay.Function([], output)
mutated_mod['func_7341'] = func_7341
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2967_call = mod.get_global_var('func_2967')
func_2968_call = mutated_mod.get_global_var('func_2968')
call_7376 = relay.TupleGetItem(func_2967_call(), 0)
call_7377 = relay.TupleGetItem(func_2968_call(), 0)
output = relay.Tuple([call_7376,])
output2 = relay.Tuple([call_7377,])
func_7378 = relay.Function([], output)
mod['func_7378'] = func_7378
mod = relay.transform.InferType()(mod)
output = func_7378()
func_7379 = relay.Function([], output)
mutated_mod['func_7379'] = func_7379
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5852_call = mod.get_global_var('func_5852')
func_5853_call = mutated_mod.get_global_var('func_5853')
call_7406 = relay.TupleGetItem(func_5852_call(), 2)
call_7407 = relay.TupleGetItem(func_5853_call(), 2)
func_5117_call = mod.get_global_var('func_5117')
func_5120_call = mutated_mod.get_global_var('func_5120')
const_7432 = relay.const([-3.933432,8.834557,3.090840,-0.542567,-3.277624,0.881083,-8.172018,2.342908,4.569834,-7.997072,-3.307287,7.360224,-7.677436,-9.024534,-8.929308,4.425319,-0.725542,6.890512,-3.706626,-3.040266,-5.516624,5.891286,6.954005,2.201078,-8.640466,-6.796729,-6.945679,-5.681427,1.185706,-0.451594,3.093447,-0.404573,-7.847243,0.809724,-9.297507,2.055063,6.746877,7.349828,-8.780890,9.891035,-1.779126,8.034469,2.636846,-0.188917,-0.951732,-0.608517,-0.775113,7.049823,-4.401838,-0.018619,-7.139726,4.926488,-5.128417,-5.818380,1.559296,6.653086,5.197541,-8.433849,6.216765,9.253295,9.394123,9.490930,5.950465,-8.049273,4.747576,-5.221540,6.935657,0.895594,-6.952550,-9.453460,1.593620,4.286288,-4.065118,9.036938,-6.755541,5.631483,-0.632548,-3.962540,3.085097,9.323818,2.124432,-2.414673,6.212427,-8.230153,6.701915,3.342055,9.274310,3.631484,2.063706,0.832828,-4.928789,6.783094,4.445063,-0.818631,5.835662,9.299726,7.115266,8.665134,5.881094,-7.803055,-8.477458,9.934247,-0.053205,0.304933,3.231892,-2.341296,6.188351,-0.354430,1.291885,4.050177,-7.706944,5.952210], dtype = "float64")#candidate|7432|(112,)|const|float64
var_7433 = relay.var("var_7433", dtype = "uint32", shape = (3, 4))#candidate|7433|(3, 4)|var|uint32
call_7431 = relay.TupleGetItem(func_5117_call(relay.reshape(const_7432.astype('float64'), [4, 28]), relay.reshape(var_7433.astype('uint32'), [12,]), ), 9)
call_7434 = relay.TupleGetItem(func_5120_call(relay.reshape(const_7432.astype('float64'), [4, 28]), relay.reshape(var_7433.astype('uint32'), [12,]), ), 9)
func_6348_call = mod.get_global_var('func_6348')
func_6350_call = mutated_mod.get_global_var('func_6350')
call_7446 = relay.TupleGetItem(func_6348_call(), 0)
call_7447 = relay.TupleGetItem(func_6350_call(), 0)
func_371_call = mod.get_global_var('func_371')
func_374_call = mutated_mod.get_global_var('func_374')
const_7449 = relay.const([True,True,False,True,False,True,True,True,True,True,False,False,True,False,True,True,True,False,False,False,False,False,True,False,True,True,True,False,False,True,True,True,True,False,True,True,True,False,True,True,True,True,True,True,True,False,False,False,False,False,True,True,False,False,True,False,True,False,False,True,False,True,True,True,True,False,False,True,False,True,False,True,False,True,False,True,False,False,False,False,True,True,True,True,True,True,True,False,True,True,True,True,True,False,False,False,False,True,True,False,False,True,False,True,True,False,False,True,True,False,True,False,True,True,True,False,False,True,False,True,False,False,True,True,False,True,False,True,False,True,True,True,True,True,False,False,False,False,True,True,True,False,True,False,True,False,True,True,True,True,True,False,True,False,True,False,True,True,True,False,True,False,True,False,False,True,False,False,True,True,True,False,True,False,True,True,False,False,False,False,True,True,False,True,True,True,True,True,True,False,True,False,False,False,False,False,True,False,False,False,True,True,True,False,True,False,True,False,False,False,False,True,True,False,False,True,True,True,False,False,True,True,False,False,True,False,False,False,False,True,False,True,False,True,False,False,True,True,False,True,True,False,True,True,False,True,False,True,True,False,False,False,True,False,False,False,True,True,False,True,False,False,True,False,False,True,False,True,False,False,True,False,False,False,True,False,True,True,False,False,True,False,True,False,False,True,False,True,False,False,True,False,False,False,True,False,True,True,False,True,False,True,True,False,True,False,True,False,True,True,True,False,True,False,False,True,True,False,True,False,False,False,False,True,False,True,True,True,True,True,False,True,False,False,True,True,False,False,False,False,True,True,False,False,True,True,False,False,True,True,False,False,True,True,True,True,False,False,False,True,False,False,False,False,False,False,False,True,False,False,True,False,True,True,False,False,False,False,False,False,True,True,False,False,False,True,True,False,True,True,False,True,False,False,False,False,False,False,True,True,False,False,True,True,False,True,True,False,False,True,False,True,False,False,False,False,True,True,True,True,True,True,False,True,True,False,True,False,False,True,True,False,True,False,True,True,True,False,False,True,False,False,True,False,True,True,True,False,False,False,True,True,True,False,False,False,False,False,False,True,True,True,True,False,True,True,False,True,True,False,False,True,False,True,False,True,False,True,False,True,True,True,False,False,True,True,False,False,True,True,True,False,False,False,False,False,True,False,True,True,False,True,False,True,True,False,False,True,True,False,False,False,False,True,False,True,False,True,True,True,False,False,True,False,True,True,False,False,False,True,True,False,True,False,True,False,False,False,True,False,False,False,False,False,True,True,False,True,False,True,False,False,False,True,False,True,False,True,True,False,False,True,True,True,True,False,True,True,False,True,True,True,True,False,True,False,True,True,True,True,True,True,True,True,False,True,False,False,False,True,True,True,False,False,False,True,False,False,True,True,True,False,False,False,False,True,False,True,True,True,False,False,False,True,True,False,True,True,False,True,False,True,False,True,True,True,False,False,True,True,True,False,False,True,False,False,False,False,False,True,True,False,True,True,False,False,True,True,True,True,False,False,True,True,True,False,False,True,False,True,True,True,True,True,False,True,True,True,True,True,False,False,False,False,True,False,False,False,True,False,True,True,False,False,False,True,True,False,False,True,True,True,True,False,False,True,True,False,False,False,True,True,False,True,True,True,True,True,True,False,True,True,False,True,True,False,False,False,True,True,False,False,False,True,True,True,False,False,True,True,True,False,False,True,False,True,True,True,False,False,False,False,True,False,True,True,False,False,True,True,True,True,False,True,False,True,False,True,True,True,False,False,False,False,False,False,True,True,True,True,True,True,True,True,True,True,False,False,True,True,True,False,True,True,True,True,False,False,False,False,True,False,False,True,False,False,True,True,True,True,True,True,False,False,False,False,True,False,False,False,True,True,False,False,True,False,False,True,False,False,True,True,True,False,True,True,False,False,True,False,True,False,True,False,False,True,False,False,True,False,False,False,True,True,True,False,True,True,False,True,True,True,False,False,True,True,False,False,False,True,False,True,True,True,True,True,False,True,True,True,True,False,True,True,True,False,True,False,True,True,True,True,True,True,True,False,True,True,False,True,False,False,False,True,True,False,True,True,True,False,False,True,False,False,False,True,False,True,True,False,True,False,True,False,False,False,False,True,False,True,False,False,True,False,False,True,False,True,False,False,True,True,True,False,True,True,True,True,False,True,True,True,True,False,True,True,True,False,False,True,True,False,True,False,True,True,True,True,False,False,True,False,True,False,False,False,True,True,True,False,False,True,True,False,True,True,True,False,True,False,True,False,False,True,False,True,False,False,True,True,False,False,True,True,True,True,True,False,False,False,False,True,True,False,True,True,True,False,True,False,False,True,False,True,False,False,False,False,False,True,True,False,False,False,True,True,True,False,True,False,True,False,True,False,False,False,True,True,False,True,True,True,False,True,False,False,True,False,False,False,False,False,False,False,False,False,True,False,False,False,False,True,False,True,False,False,True,True,True,True,False,False,False,False,True,False,False,True,True,True,True,True,True,True,True,True,True,False,True,False,False,True,True,True,False,True,True,True,True,True,True,True,True,True,False,True,False,False,False,True,True,True,False,False,False,True,False,False,True,True,False,True,True,True,False,True,True,False,True,False,True,False,True,False,True,True,True,True,False,True,False,True,False,False,False,True,True,False,True,False,True,True,False,False,False,False,False,True,False,True,True,True,True,True,False,False,False,True,False,False,True,False,False,True,True,False,False,False,False,True,True,True,False,True,False,True,True,False,False,False,True,False,True,False,True,True,False,True,True,False,False,False,True,False,True,False,False,False,False,False,True,True,True,False,False,True,True,False,True,True,False,False,True,True,False,False,True,True,False,False,True,False,False,False,False,True,False,False,True,True,False,True,False,True,True,True,True,False,True,False,True,True,True,True,False,True,True,True,False,True,True,False,True,True,False,True,True,True,True,False,False,True,True,False,True,False,True,False,False,False,False,False,True,True,True,False,True,False,True,True,False,True,True,True,False,False,True,True,True,False,False,True,False,True,True,True,False,True,True,False,True,True,False,True,True,True,True,False,False,False,True,False,True,True,True,False,True,False,True,False,True,True,True,True,True,False,False,True,True,True,True,True,False,False,False,True,True,True,True,True,True,True,True,True,False,True,True,True,True,False,True,False,False,False,True,True,False,True,False,False,False,True,True,True,True,True,False,True,False,False,False,True,True,False,False,True,True,True,False,False,False,True,True,False,True,False,True,True,False,True,True,False,False,False,True,False,True,False,True,True,False,True,True,True,True,True,False,False,True,False,True,True,True,False,True,False,False,False,True,False,True,True,True,True,True,False,True,True,False,False,False,False,False,True,True,True,True,True,False,False,True,True,True,False,True,False,False,True,False,False,False,True,True,True,False,False,True,False,True,False,False,False,False,False,True,False,False,False,True,False,False,True,True,True,True,False,True,False,True,True,False,True,False,True,False,True,True,False,True,True,False,True,True,False,False,False,False,False,True,False,False,True,True,True,True,False,True,False,False,False,False,False,False,False,True,False,True,True,False,False,False,False,False,True,True,False,True,True,False,False,True,False,False,False,True,True,True,False,True,True,False,True,False,False,False,True,True,True,False,True,False,False,False,False,True,True,False,True,False,False,True,False,False,True,False,True,False,True,True,False,True,True,True,True,False,True,False,True,True,True,False,True,True,False,True,True,True,True,False,False,True,True,False,True,True,False,False,True,False,True,True,True,False,True,False,False,False,False,True,True,True,False,False,True,False,True,False,False,False,False,False,True,True,False,False,False,False,False,False,False,True,True,True,False,False,True,False,True,False,False,False,True,False,True,False,False,False,False,False,True,False,False,False,False,False,True,False,True,True,False,True,True,False,True,True,False,False,True,True,False,True,False,False,True,True,False,False,True,True,False,False,True,True,True,True,True,False,False,False,True,False,False,False,False,True,True,True,True,True,False,False,False,False,False,False,True,False,False,True,True,False,True,True,True,False,False,True,False,False,True,False,True,True,False,True,False,False,False,False,True,True,False,True,True,False,True,True,False,True,False,False,False,True,True,True,False,True,False,False,False,False,False,True,True,True,False,False,True,True,False,False,False,False,True,True,False,True,False,False,False,False,False,False,False,True,False,False,True,False,False,True,False,True,False,False,False,False,False,True,True,False,True,True,False,False,True,False,True,True,False,False,False,True,False,False,False,False,False,True,True,False,False,True,True,False,True,True,True,True,False,False,True,True,False,True,False,True,True,True,False,False,True,False,True,False,False,True,False,False,True,True,True,True,True,False,False,False,False,True,False,False,True,True,False,True,True,False,False,False,True,True,False,True,True,True,True,False,True,True,False,False,True,True,True,False,False,True,False,False,False,False,False,False,False,False,True,True,False,False,True,False,True,False,True,False,True,False,False,False,True,True,False,False,False,False,False,False,True,True,False,False,True,True,False,True,True,True,False,False,True,False,False,False,False,True,True,True,True,True,False,False,False,False,True,True,False,True,True,False,False,False,False,False,True,False,True,False,True,False,False,True,False,False,True,False,True,False,True,False,False,True,True,False,False,False,True,False,True,True,False,False,True,False,False,False,False,True,False,False,True,True,True,True,True,False,True,True,True,True,True,True,False,False,True,False,False,True,True,False,False,True,False,True,False,False,True,False,True,True,False,True,False,True,False,False,False,False,True,True,True,False,False,True,True,True,False,True,False,True,True,False,False,True,True,False,True,False,True,True,False,True,False,False,True,False,False,True,False,True,False,True,False,False,True,True,True,True,False,False,False,False,False,False,True,False,True,True,False,False,False,False,True,False,True,False,False,True,True,True,True,True,False,True,True,True,False,True,False,False,True,False,False,True,True,False,True,False,True,False,False,True,False,True,True,True,False,True,True,True,False,False,True,True,True,False,False,True,True,True,True,False,True,False,False,False,False,True,False,True,True,False,False,False,False,True,True,False,False,False,True,True,False,False,False,True,True,False,False,False,True,False,True,True,False,True,True,False,False,False,True,False,False,True,False,False,False,True,False,False,False,False,True,False,False,True,False,True,False,False,False,True,False,True,False,False,False,False,False,False,False,True,False,False,False,False,True,False,False,True,True,False,True,False,False,False,False,False,True,False,True,True,True,True,False,False,False,False,False,False,True,False,False,True,False,False,False,True,True,False,True,False,False,False,False,False,False,False,True,False,False,False,True,False,True,False,False,True,False,False,False,True,False,False,True,False,False,True,False,True,True,True,True,True,True,False,True,False,False,False,False,True,False,True,True,False,True,True,True,False,True,True,True,True,True,False,True,False,True,True,True,False,False,True,True,False,True,True,False,True,True,False,False,False,True,True,False,True,False,True,True,True,True,False,False,False,True,False,False,False,True,False,True,False,True,False,False,False,True,False,True,True,False,False,True,True,True,True,False,False,False,True,True,True,False,False,False,True,False,False,True,True,False,False,True,True,True,True,True,False,True,True,True,True,True,False,True,False,True,True,False,False,True,False,True,True,False,True,False,False,False,True,True,False,False,True,False,True,False,True,True,False,False,True,True,True,True,False,False,True,False,False,True,True,False,False,False,False,False,False,False,False,True,False,False,True,True,False,False,True,False,False,True,False,True,True,False,False,True,False,True,True,False,False,False,True,True,False,True,True,False,False,True,False,False,True,True,True,False,False,False,False,False,False,False,True,True,False,True,False,False,True,False,True,True,False,False,False,True,True,True,True,True,False,True,True,False,True,False,False,True,True,False,True,True,False,False,False,True,True,False,True,False,False,False,False,True,False,False,False,False,False,True,True,False,True,True,False,False,True,False,True,False,False,False,True,True,False,True,False,True,False,True,False,False,False,False,True,False,False,True,False,False,True,False,True,False,True,True,False,False,False,True,True,False,True,False,True,True,False,True,False,False,True,False,False,True,False,False,True,True,True,False,True,False,False,False,False,True,False,False,True,False,True,False,False,False,True,False,True,True,True,False,True,False,False,True,True,True,True,True,False,True,True,True,True,True,False,False,False,False,False,True,False,False,False,False,False,True,False,False,False,False,False,True,False,False,False,False,True,False,True,True,True,False,True,False,True,True,False,True,True,True,False,True,True,False,True,True,True,False,True,True,False,True,False,False,False,True,False,True,True,True,True,False,True,False,False,False,True,True,True,False,False,False,True,True,False,False,False,False,False,False,True,False,True,False,True,True,True,True,True,False,True,False,False,False,False,False,True,True,True,False,True,True,False,False,False,True,False,True,True,True,True,False,True,False,False,False,False,True,False,True,True,True,True,True,True,True,False,False,False,True,True,True,True,True,True,True,False,True,False,True,False,True,False,False,False,False,False,False,False,False,True,True,True,False,True,True,True,True,True,True,False,False,False,True,False,True,True,False,False,True,False,True,True,False,True,True,False,True,True,False,False,False,False,True,False,True,False,True,False,False,False,False,False,False,False,False,True,True,True,True,False,True,False,True,True,True,False,True,True,True,False,True,True,False,False,True,True,True,False,True,True,False,True,True,False,True,False,True,False,True,True,True,False,True,False,True,True,True,False,False,False,False,True,False,False,True,True,True,False,False,False,True,False,False,True,True,True,True,False,False,False,True,True,False,True,True,True,False,False,True,False,True,False,True,True,False,False,False,False,True,False,False,False,True,False,True,False,False,False,False,False,False,False,True,False,True,False,True,True,True,True,True,False,True,False,True,True,False,True,True,True,False,False,False,True,False,True,True,False,False,True,False,False], dtype = "bool")#candidate|7449|(2925,)|const|bool
call_7448 = func_371_call(relay.reshape(const_7449.astype('bool'), [13, 15, 15]), relay.reshape(const_7449.astype('bool'), [13, 15, 15]), )
call_7450 = func_371_call(relay.reshape(const_7449.astype('bool'), [13, 15, 15]), relay.reshape(const_7449.astype('bool'), [13, 15, 15]), )
func_4008_call = mod.get_global_var('func_4008')
func_4012_call = mutated_mod.get_global_var('func_4012')
const_7452 = relay.const([-8,8,6,1,-3,-10,-7,2,5,-5,5,-10,9,-9,10,3,-8,4,-1,5,3,-10,-6,2,-10,-4,6,7,-10,4,-6,-9,-6,-10,8,-2,3,-3,4,10,-2,-1,2,6,4,-3,-7,-5,-5,-1,-10,-6,-4,-2,4,-4,-10,-7,-3,-2,10,-5,8,-9,7,-6,2,-10,2,-5,-5,3,4,-6,2,3,-5,-1,10,-6,2,4,5,-10,-7,3,4,7,-7,-6,-5,5,9,5,-7,-8,4,-3,-7,5,-8,6,-6,3,-10,-6,-9,-4,-6,10,9,-4,-2,-3,-10,5,-9,-1,5,-10,-2,-9,7,9,-2,1,-1,-6,4,3,10,-3,8,5,7,-8,4,-9,-1,-8,-9,6,-4,2,4,1,3,4,-7,5,-6,2,-10,-5,-1,-4,2,2,-2,5,10,-9,-9,4,-2,1,-4,10,-5,-3,-7,-9,-6,-4,-5,-4,4,-10,6,10,-5,-8,5,-2,-2,-9,3,6,6,8,9,-8,5,8,4,-9,-1,7,-2,6,-8,-3,-2,-10,10,-2,10,-4,8,4,1,10,-8,-6,7,-6,-9,-6,9,1,-4,2,1,-8,-9,-10,6,2,6,-8,-2,-8,5,-3,-9,-6,5,6,-4,-6,9,-3,3,-10,-3,-2,3,7,-3,2,3,5,-4,6,7,2,8,-10,-1,2,9,1,5,7,8,-1,7,-1,-9,2,-2,4,8,-3,-6,-2,-2,-4,1,-6,-3,2,-3,5,-3,-1,-9,-5,1,-7,6,2,4,-4,9,6,6,-4,-2,-2,5,-1,2,-3,-5,-10,4,8,7,-5,-9,8,10,6,-10,10,-4,10,-7,9,-5,-5,-2,-7,3,5,4,9,5,9,-6,9,-9,5,1,-10,-6,3,7,7,3,-6,-5,-2,-10,6,-1,-5,-3,8,8,-10,4,2,-5,-3,-1,5,4,8,2,2,-8,-6,9,7,-6,2,10,3,-5,4,-7,-3,8,-9,-5,4,7,-4,-3,-6,8,9,5,5,-10,5,-10,10,-10,-8,7,-6,-1,-5,-5,-5,2,-3,8,5,9,-5,8,4,-4,3,-4,8,-1,-2,-7,-9,1,-3,2,-6,10,9,-9,-6,-7,4,7,-7,-6,-7,5,1,-10,2,-4,4,-2,-4,7,-1,8,-6,-9,5,1,8,10,2,6,3,-4,6,1,6,9,-2,5,3,-2,-9,2,1,-9,-3,6,-4,4,-6,-9,5,-2,-4,7,-2,6,4,-3,10,-7,-6,9,-3,2,-2,-4,9,-5,6,10,3,-9,2,1,3,-4,-10,1,-8,5,-3,6,-8,5,-5,1,-9,-6,-4,6,6,6,-5,-1,9,-2,8,4,-2,-9,-4,-6,3,-7,-10,2,-2,-2,-7,-9,-3,-1,-2,-7,6,1,8,-4,-9,6,1,-5,-8,10,-4,-4,-10,5,1,-6,10,8,5,1,-2,-3,-6,-8,7,-4,6,7,-4,-10,6,6,3,6,-6,2,-3,-3,-5,-5,-10,5,-6,2,5,-7,-9,-9,-6,10,3,2,-1,6,7,-10,10,-2,10,-8,-7,-5,7,1,-10,-5,-5,8,-3,3,4,8,-3,-2,-6,7,5,-2,-8,6,-3,9,-10,-5,-9,-3,-6,-9,-3,9,9,-3,-7,-7,-7,3,3,-10,-8,6,-7,-10,-3,-1,10,-4,-5,-5,5,9,4,3,-3,2,10,-9,-8,10,-10,8,1,10,2,-2,7,8,-5,-9,-6,2,-9,-4,9,-10,5,10,-9,-5,4,-5,-1,2,-4,8,2,-7,-10,9,5,10,-5,-7,9,-5,-9,5,3,-10,8,8,-6,2,6,-5,1,10,-6,-10,10,9,6,-3,-3,10,9,-3,3,-10,7,9,-3,-3,9,-3,1,-10,7,-9,-6,-2,-7,9,10,-10,-9,4,9,10,-3,8,-6,-4,-4,3,-10,-7,8,8,7,5,-8,-9,-8,-6,3,-6,4,4,-3,-10,-10,1,-2,7,8,7,-3,-4,5,-2,5,9,-8,-7,-10,3,1,9,4,5,10,-7,-8,3,-10,-4,-3,-4,6,3,8,5,1,-5,9,-4,-3,3,-1,-7,-1,7,3,-6,-3,-2,-4,-4,-10,7,-10,10,3,7,10,-8,4,-5,-7,4,10,4,-5,-7,7,6,-7,3,2,6,5,-2,-9,3,-10,7,7,1,10,-6,-4,-6,-9,-10,2,-4,2,-3,-5,-7,7,4,-7,-5,5,-6,4,-1,-5,-5,-9,-2,-4,-9,3,-5,-4,-4,4,-8,1,-9,7,9,10,-1,-2,9,-9,-7,6,3,-1,-1,-6,-7,4,-1,7,-7,5,-8,-8,-5,7,1,5,5,1,-2,-4,6,-4,-3,9,10,5,-1,4,1,-9,7,6,-2,8,6,3,-2,-8,-10,4,-1,7,-3,1,4,-6,-5,-1,-1,-1,10,8,-10,8,5,7,10,-1,7,-7,-1,-10,-5,-5,1,-1,9,5,-8,-9,-7,-9,2,-10,-2,-8,7,-3,-2,-9,4,5,1,-3,5,2,-8,-8,2,9,-4,1,6,6,-2,-10,6,10,-7,8,4,-5,4,-3,3,2,-9,-1,-7,-5,-3,-5,-2,8,-9,1,-8,-6,-10,-9,-10,-10,-4,-6,-7,9,-7,9,-1,-9,3,2,6,4,-8,9,-3,-1,-10,-1,-9,5,5,3,10,6,2,5,-7,-4,-1,5,3,-5,2,-8,-6,-6,8,9,-3,-3,3,3,-8,-7,3,5,9,-7,-5,1,-9,-2,-8,6,6,-6,-1,2,-9,8,-2,-6,-2,3,7,7,-3,-4,2,2,-3,-8,9,-2,9,-8,3,-4,-8,-2,-1,2,10,4,-8,-9], dtype = "int64")#candidate|7452|(1080,)|const|int64
call_7451 = relay.TupleGetItem(func_4008_call(relay.reshape(const_7452.astype('int64'), [12, 9, 10]), relay.reshape(const_7452.astype('int64'), [12, 9, 10]), ), 0)
call_7453 = relay.TupleGetItem(func_4012_call(relay.reshape(const_7452.astype('int64'), [12, 9, 10]), relay.reshape(const_7452.astype('int64'), [12, 9, 10]), ), 0)
func_5989_call = mod.get_global_var('func_5989')
func_5991_call = mutated_mod.get_global_var('func_5991')
call_7457 = func_5989_call()
call_7458 = func_5989_call()
bop_7490 = relay.bitwise_and(const_7449.astype('uint8'), relay.reshape(call_7448.astype('uint8'), relay.shape_of(const_7449))) # shape=(2925,)
bop_7493 = relay.bitwise_and(const_7449.astype('uint8'), relay.reshape(call_7450.astype('uint8'), relay.shape_of(const_7449))) # shape=(2925,)
uop_7498 = relay.acos(call_7431.astype('float64')) # shape=(4, 28)
uop_7500 = relay.acos(call_7434.astype('float64')) # shape=(4, 28)
bop_7513 = relay.bitwise_or(uop_7498.astype('uint8'), relay.reshape(call_7431.astype('uint8'), relay.shape_of(uop_7498))) # shape=(4, 28)
bop_7516 = relay.bitwise_or(uop_7500.astype('uint8'), relay.reshape(call_7434.astype('uint8'), relay.shape_of(uop_7500))) # shape=(4, 28)
func_3694_call = mod.get_global_var('func_3694')
func_3696_call = mutated_mod.get_global_var('func_3696')
call_7523 = func_3694_call()
call_7524 = func_3694_call()
func_3437_call = mod.get_global_var('func_3437')
func_3439_call = mutated_mod.get_global_var('func_3439')
call_7527 = func_3437_call()
call_7528 = func_3437_call()
uop_7539 = relay.sin(uop_7498.astype('float64')) # shape=(4, 28)
uop_7541 = relay.sin(uop_7500.astype('float64')) # shape=(4, 28)
output = relay.Tuple([call_7406,const_7432,var_7433,call_7446,call_7451,const_7452,call_7457,bop_7490,bop_7513,call_7523,call_7527,uop_7539,])
output2 = relay.Tuple([call_7407,const_7432,var_7433,call_7447,call_7453,const_7452,call_7458,bop_7493,bop_7516,call_7524,call_7528,uop_7541,])
func_7542 = relay.Function([var_7433,], output)
mod['func_7542'] = func_7542
mod = relay.transform.InferType()(mod)
var_7543 = relay.var("var_7543", dtype = "uint32", shape = (3, 4))#candidate|7543|(3, 4)|var|uint32
output = func_7542(var_7543)
func_7544 = relay.Function([var_7543], output)
mutated_mod['func_7544'] = func_7544
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7378_call = mod.get_global_var('func_7378')
func_7379_call = mutated_mod.get_global_var('func_7379')
call_7550 = relay.TupleGetItem(func_7378_call(), 0)
call_7551 = relay.TupleGetItem(func_7379_call(), 0)
output = call_7550
output2 = call_7551
func_7559 = relay.Function([], output)
mod['func_7559'] = func_7559
mod = relay.transform.InferType()(mod)
output = func_7559()
func_7560 = relay.Function([], output)
mutated_mod['func_7560'] = func_7560
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7224_call = mod.get_global_var('func_7224')
func_7226_call = mutated_mod.get_global_var('func_7226')
call_7603 = relay.TupleGetItem(func_7224_call(), 1)
call_7604 = relay.TupleGetItem(func_7226_call(), 1)
output = call_7603
output2 = call_7604
func_7613 = relay.Function([], output)
mod['func_7613'] = func_7613
mod = relay.transform.InferType()(mod)
mutated_mod['func_7613'] = func_7613
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7613_call = mutated_mod.get_global_var('func_7613')
call_7614 = func_7613_call()
output = call_7614
func_7615 = relay.Function([], output)
mutated_mod['func_7615'] = func_7615
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7258_call = mod.get_global_var('func_7258')
func_7259_call = mutated_mod.get_global_var('func_7259')
call_7616 = relay.TupleGetItem(func_7258_call(), 1)
call_7617 = relay.TupleGetItem(func_7259_call(), 1)
output = relay.Tuple([call_7616,])
output2 = relay.Tuple([call_7617,])
func_7636 = relay.Function([], output)
mod['func_7636'] = func_7636
mod = relay.transform.InferType()(mod)
mutated_mod['func_7636'] = func_7636
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7636_call = mutated_mod.get_global_var('func_7636')
call_7637 = func_7636_call()
output = call_7637
func_7638 = relay.Function([], output)
mutated_mod['func_7638'] = func_7638
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6711_call = mod.get_global_var('func_6711')
func_6712_call = mutated_mod.get_global_var('func_6712')
call_7845 = func_6711_call()
call_7846 = func_6711_call()
output = relay.Tuple([call_7845,])
output2 = relay.Tuple([call_7846,])
func_7855 = relay.Function([], output)
mod['func_7855'] = func_7855
mod = relay.transform.InferType()(mod)
output = func_7855()
func_7856 = relay.Function([], output)
mutated_mod['func_7856'] = func_7856
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7014_call = mod.get_global_var('func_7014')
func_7016_call = mutated_mod.get_global_var('func_7016')
call_7906 = relay.TupleGetItem(func_7014_call(), 0)
call_7907 = relay.TupleGetItem(func_7016_call(), 0)
output = call_7906
output2 = call_7907
func_7915 = relay.Function([], output)
mod['func_7915'] = func_7915
mod = relay.transform.InferType()(mod)
mutated_mod['func_7915'] = func_7915
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7915_call = mutated_mod.get_global_var('func_7915')
call_7916 = func_7915_call()
output = call_7916
func_7917 = relay.Function([], output)
mutated_mod['func_7917'] = func_7917
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7961 = relay.const([[[9.203202,5.605181,-7.999346,3.114236,-1.385330],[4.996545,-9.739290,-2.084041,-9.024200,9.395102],[-6.779651,-6.894189,-2.785923,6.311110,2.338606],[0.195464,-5.355590,2.777454,2.195711,-7.668925],[-6.936855,-7.679119,3.117141,7.146420,0.760537],[-6.763459,2.898918,4.953864,-5.141707,2.177623],[1.577856,-3.341372,-9.168232,-3.946219,-6.073796],[2.846011,-4.216455,5.075419,7.372906,-0.624320],[5.678746,-6.497263,9.656931,-0.973403,-8.374338],[6.294375,6.320638,5.065313,4.380530,7.489030],[-7.020375,-6.361630,8.745522,0.592132,1.453027]],[[2.168663,-2.375985,7.547315,9.635931,7.724315],[5.839903,6.034790,-9.147626,-4.038973,-3.694762],[5.438622,5.699838,-6.887613,-6.757727,7.230509],[9.695341,-4.013570,-4.375377,3.023681,-0.320907],[0.417193,7.207477,-6.860727,-6.212804,9.282108],[-7.040346,5.791561,4.528283,-6.489928,2.474740],[9.081652,-6.849176,-5.373810,9.134372,-7.934905],[-4.142522,8.395800,-1.404059,5.911046,1.144924],[-6.012199,-1.274655,5.408256,8.923129,3.288186],[8.706717,6.840687,-0.057266,-3.986118,2.411687],[6.204563,-4.926560,2.791211,-7.743114,2.208695]],[[5.879763,-2.192804,-3.702462,7.330742,2.315991],[-6.308727,4.390676,2.674651,-6.266661,4.172460],[-8.654341,4.690452,-1.338228,-4.797582,-9.505397],[-5.457119,0.335976,2.106888,-5.004298,4.549704],[6.547175,-8.034461,8.462153,-2.556095,9.029533],[3.382106,7.637630,-2.302725,7.804208,-6.541058],[6.254639,5.224485,1.474603,-9.335562,-4.670919],[-1.338830,4.990855,-7.969889,-4.984266,-8.550864],[1.432627,4.684927,3.462317,-8.557861,-4.903709],[-7.612531,3.287310,-3.508180,-7.235883,-3.109138],[-3.242306,-2.892645,5.514488,-1.435158,5.751845]],[[0.693278,-9.815392,5.503822,-4.944734,-3.114859],[2.322014,-8.146991,4.172854,4.577138,1.789375],[-8.980806,-4.622759,-7.224943,8.913480,6.449258],[5.291388,6.520072,-9.197260,9.379472,-6.858003],[6.596821,-5.608719,-6.991984,1.177428,6.212055],[3.952483,-0.025679,-1.047857,0.733928,-3.206234],[2.651076,0.957864,1.814824,9.635609,8.822139],[0.678738,1.740506,-2.478850,8.044671,-2.225814],[6.518801,-0.215007,0.806640,-4.282508,-8.307566],[-7.651719,-4.813371,2.656618,9.315620,1.127109],[-8.647316,8.636886,-2.122988,-3.460777,6.770472]],[[3.085956,-9.196740,5.755182,-8.769133,1.733938],[-7.941610,-6.449599,5.308500,-7.281188,6.823790],[7.972083,-1.016396,7.975831,7.232012,-0.841878],[-7.381888,3.535594,2.271553,7.066452,-1.833732],[1.776116,-3.620072,8.772925,7.624177,-6.838119],[2.126719,-0.721826,-8.911685,0.308814,1.649294],[8.477466,4.227918,7.775527,2.527540,-3.016571],[6.462522,-7.514250,-9.983685,3.027976,2.531641],[-6.125187,-0.656309,9.400341,-9.564426,-1.876863],[-4.553286,-0.436214,-1.822391,3.312858,-4.850452],[2.551302,7.034084,3.035031,8.123404,2.281559]],[[-0.239125,-8.835323,-0.917716,8.612822,-4.773151],[4.198344,7.262162,-6.370438,1.989398,1.233241],[0.757605,7.375348,-9.593740,-5.201948,9.873279],[0.538510,5.357884,-0.579468,6.087840,6.605864],[3.058744,-5.627738,-8.550457,-7.114489,-0.270986],[7.108475,-8.946163,-5.478890,0.220364,0.274771],[-3.488577,-3.034789,-6.556450,-0.606261,-5.154143],[0.674343,-2.546848,7.324821,-3.140049,-6.624282],[8.244699,-1.186047,-7.871706,2.476620,-1.531623],[-6.063431,1.558383,-6.953833,-2.169459,6.983232],[-1.429383,-0.339393,-2.995369,8.229341,-2.492240]],[[-6.215713,8.220131,6.436552,6.692029,9.942309],[7.374731,5.904895,-6.545887,-0.602297,-4.827156],[-7.004163,-2.662154,6.397937,-8.188030,9.902340],[-8.336399,-0.688953,2.305898,2.416305,-5.532845],[-1.175087,-3.120307,-6.163315,1.534178,4.360653],[-6.138329,8.917474,1.144660,-0.201636,7.149153],[-6.129638,4.707597,-4.358786,-7.520536,7.781682],[-5.105800,6.164792,9.110494,-8.441416,-4.350876],[-1.329047,1.774206,-9.378161,-9.295532,-3.075491],[-8.206488,3.085384,9.732848,-4.808518,5.252335],[1.691952,4.102233,2.664683,-2.173834,-8.426270]]], dtype = "float64")#candidate|7961|(7, 11, 5)|const|float64
uop_7962 = relay.sinh(const_7961.astype('float64')) # shape=(7, 11, 5)
output = relay.Tuple([uop_7962,])
output2 = relay.Tuple([uop_7962,])
func_7966 = relay.Function([], output)
mod['func_7966'] = func_7966
mod = relay.transform.InferType()(mod)
mutated_mod['func_7966'] = func_7966
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7966_call = mutated_mod.get_global_var('func_7966')
call_7967 = func_7966_call()
output = call_7967
func_7968 = relay.Function([], output)
mutated_mod['func_7968'] = func_7968
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3779_call = mod.get_global_var('func_3779')
func_3780_call = mutated_mod.get_global_var('func_3780')
call_8010 = func_3779_call()
call_8011 = func_3779_call()
func_4917_call = mod.get_global_var('func_4917')
func_4919_call = mutated_mod.get_global_var('func_4919')
call_8012 = relay.TupleGetItem(func_4917_call(), 0)
call_8013 = relay.TupleGetItem(func_4919_call(), 0)
func_3794_call = mod.get_global_var('func_3794')
func_3795_call = mutated_mod.get_global_var('func_3795')
call_8015 = relay.TupleGetItem(func_3794_call(), 0)
call_8016 = relay.TupleGetItem(func_3795_call(), 0)
func_6721_call = mod.get_global_var('func_6721')
func_6722_call = mutated_mod.get_global_var('func_6722')
call_8024 = func_6721_call()
call_8025 = func_6721_call()
func_3526_call = mod.get_global_var('func_3526')
func_3528_call = mutated_mod.get_global_var('func_3528')
call_8036 = func_3526_call()
call_8037 = func_3526_call()
output = relay.Tuple([call_8010,call_8012,call_8015,call_8024,call_8036,])
output2 = relay.Tuple([call_8011,call_8013,call_8016,call_8025,call_8037,])
func_8043 = relay.Function([], output)
mod['func_8043'] = func_8043
mod = relay.transform.InferType()(mod)
output = func_8043()
func_8044 = relay.Function([], output)
mutated_mod['func_8044'] = func_8044
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4108_call = mod.get_global_var('func_4108')
func_4109_call = mutated_mod.get_global_var('func_4109')
call_8060 = func_4108_call()
call_8061 = func_4108_call()
var_8077 = relay.var("var_8077", dtype = "float32", shape = (468,))#candidate|8077|(468,)|var|float32
bop_8078 = relay.minimum(call_8060.astype('int64'), relay.reshape(var_8077.astype('int64'), relay.shape_of(call_8060))) # shape=(468,)
bop_8081 = relay.minimum(call_8061.astype('int64'), relay.reshape(var_8077.astype('int64'), relay.shape_of(call_8061))) # shape=(468,)
output = relay.Tuple([bop_8078,])
output2 = relay.Tuple([bop_8081,])
func_8087 = relay.Function([var_8077,], output)
mod['func_8087'] = func_8087
mod = relay.transform.InferType()(mod)
var_8088 = relay.var("var_8088", dtype = "float32", shape = (468,))#candidate|8088|(468,)|var|float32
output = func_8087(var_8088)
func_8089 = relay.Function([var_8088], output)
mutated_mod['func_8089'] = func_8089
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4998_call = mod.get_global_var('func_4998')
func_5000_call = mutated_mod.get_global_var('func_5000')
call_8151 = relay.TupleGetItem(func_4998_call(), 2)
call_8152 = relay.TupleGetItem(func_5000_call(), 2)
func_7258_call = mod.get_global_var('func_7258')
func_7259_call = mutated_mod.get_global_var('func_7259')
call_8156 = relay.TupleGetItem(func_7258_call(), 1)
call_8157 = relay.TupleGetItem(func_7259_call(), 1)
output = relay.Tuple([call_8151,call_8156,])
output2 = relay.Tuple([call_8152,call_8157,])
func_8175 = relay.Function([], output)
mod['func_8175'] = func_8175
mod = relay.transform.InferType()(mod)
mutated_mod['func_8175'] = func_8175
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8175_call = mutated_mod.get_global_var('func_8175')
call_8176 = func_8175_call()
output = call_8176
func_8177 = relay.Function([], output)
mutated_mod['func_8177'] = func_8177
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8225 = relay.var("var_8225", dtype = "uint64", shape = ())#candidate|8225|()|var|uint64
var_8226 = relay.var("var_8226", dtype = "uint64", shape = (16, 8, 10))#candidate|8226|(16, 8, 10)|var|uint64
bop_8227 = relay.multiply(var_8225.astype('uint64'), var_8226.astype('uint64')) # shape=(16, 8, 10)
func_4450_call = mod.get_global_var('func_4450')
func_4452_call = mutated_mod.get_global_var('func_4452')
var_8242 = relay.var("var_8242", dtype = "float32", shape = (468,))#candidate|8242|(468,)|var|float32
call_8241 = relay.TupleGetItem(func_4450_call(relay.reshape(var_8242.astype('float32'), [78, 6])), 2)
call_8243 = relay.TupleGetItem(func_4452_call(relay.reshape(var_8242.astype('float32'), [78, 6])), 2)
func_4008_call = mod.get_global_var('func_4008')
func_4012_call = mutated_mod.get_global_var('func_4012')
var_8256 = relay.var("var_8256", dtype = "int64", shape = (1080,))#candidate|8256|(1080,)|var|int64
call_8255 = relay.TupleGetItem(func_4008_call(relay.reshape(var_8256.astype('int64'), [12, 9, 10]), relay.reshape(var_8256.astype('int64'), [12, 9, 10]), ), 0)
call_8257 = relay.TupleGetItem(func_4012_call(relay.reshape(var_8256.astype('int64'), [12, 9, 10]), relay.reshape(var_8256.astype('int64'), [12, 9, 10]), ), 0)
func_3332_call = mod.get_global_var('func_3332')
func_3335_call = mutated_mod.get_global_var('func_3335')
call_8260 = relay.TupleGetItem(func_3332_call(relay.reshape(call_8241.astype('float32'), [78, 6])), 4)
call_8261 = relay.TupleGetItem(func_3335_call(relay.reshape(call_8241.astype('float32'), [78, 6])), 4)
func_7317_call = mod.get_global_var('func_7317')
func_7318_call = mutated_mod.get_global_var('func_7318')
call_8263 = relay.TupleGetItem(func_7317_call(), 2)
call_8264 = relay.TupleGetItem(func_7318_call(), 2)
output = relay.Tuple([bop_8227,call_8241,var_8242,call_8255,var_8256,call_8260,call_8263,])
output2 = relay.Tuple([bop_8227,call_8243,var_8242,call_8257,var_8256,call_8261,call_8264,])
func_8268 = relay.Function([var_8225,var_8226,var_8242,var_8256,], output)
mod['func_8268'] = func_8268
mod = relay.transform.InferType()(mod)
var_8269 = relay.var("var_8269", dtype = "uint64", shape = ())#candidate|8269|()|var|uint64
var_8270 = relay.var("var_8270", dtype = "uint64", shape = (16, 8, 10))#candidate|8270|(16, 8, 10)|var|uint64
var_8271 = relay.var("var_8271", dtype = "float32", shape = (468,))#candidate|8271|(468,)|var|float32
var_8272 = relay.var("var_8272", dtype = "int64", shape = (1080,))#candidate|8272|(1080,)|var|int64
output = func_8268(var_8269,var_8270,var_8271,var_8272,)
func_8273 = relay.Function([var_8269,var_8270,var_8271,var_8272,], output)
mutated_mod['func_8273'] = func_8273
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7613_call = mod.get_global_var('func_7613')
func_7615_call = mutated_mod.get_global_var('func_7615')
call_8344 = func_7613_call()
call_8345 = func_7613_call()
func_6065_call = mod.get_global_var('func_6065')
func_6067_call = mutated_mod.get_global_var('func_6067')
call_8366 = relay.TupleGetItem(func_6065_call(), 0)
call_8367 = relay.TupleGetItem(func_6067_call(), 0)
output = relay.Tuple([call_8344,call_8366,])
output2 = relay.Tuple([call_8345,call_8367,])
func_8411 = relay.Function([], output)
mod['func_8411'] = func_8411
mod = relay.transform.InferType()(mod)
mutated_mod['func_8411'] = func_8411
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8411_call = mutated_mod.get_global_var('func_8411')
call_8412 = func_8411_call()
output = call_8412
func_8413 = relay.Function([], output)
mutated_mod['func_8413'] = func_8413
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6196_call = mod.get_global_var('func_6196')
func_6197_call = mutated_mod.get_global_var('func_6197')
call_8434 = relay.TupleGetItem(func_6196_call(), 1)
call_8435 = relay.TupleGetItem(func_6197_call(), 1)
output = call_8434
output2 = call_8435
func_8445 = relay.Function([], output)
mod['func_8445'] = func_8445
mod = relay.transform.InferType()(mod)
output = func_8445()
func_8446 = relay.Function([], output)
mutated_mod['func_8446'] = func_8446
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3779_call = mod.get_global_var('func_3779')
func_3780_call = mutated_mod.get_global_var('func_3780')
call_8468 = func_3779_call()
call_8469 = func_3779_call()
func_7014_call = mod.get_global_var('func_7014')
func_7016_call = mutated_mod.get_global_var('func_7016')
call_8478 = relay.TupleGetItem(func_7014_call(), 0)
call_8479 = relay.TupleGetItem(func_7016_call(), 0)
func_4998_call = mod.get_global_var('func_4998')
func_5000_call = mutated_mod.get_global_var('func_5000')
call_8486 = relay.TupleGetItem(func_4998_call(), 2)
call_8487 = relay.TupleGetItem(func_5000_call(), 2)
output = relay.Tuple([call_8468,call_8478,call_8486,])
output2 = relay.Tuple([call_8469,call_8479,call_8487,])
func_8489 = relay.Function([], output)
mod['func_8489'] = func_8489
mod = relay.transform.InferType()(mod)
output = func_8489()
func_8490 = relay.Function([], output)
mutated_mod['func_8490'] = func_8490
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5369_call = mod.get_global_var('func_5369')
func_5371_call = mutated_mod.get_global_var('func_5371')
call_8528 = relay.TupleGetItem(func_5369_call(), 0)
call_8529 = relay.TupleGetItem(func_5371_call(), 0)
func_3976_call = mod.get_global_var('func_3976')
func_3979_call = mutated_mod.get_global_var('func_3979')
const_8533 = relay.const([8.616478,6.766174,-6.375511,-1.688228,-2.547572,-3.696965,0.677194,-0.527807,-6.370963,-8.065372,-5.696340,-4.130095,-2.413856,-2.250301,2.215870,-9.082569,-5.271883,-2.236923,8.373304,-9.443938,-4.802054,-7.152374,-7.290103,-1.516777,8.664210,5.412945,-8.912135,-1.539019,2.307761,-7.562795,-0.849768,0.496244,1.981489,5.895717,-9.605200,-3.305377,5.940429,-8.276730,2.828668,-2.870888,-2.777392,2.768207,-4.442126,7.366976,-3.358318,-4.462992,-1.657819,0.755850,9.795680,2.007625,-3.164983,-5.932479,-1.257492,5.341139,-7.377225,3.524051,-8.979656,5.714138,-9.844450,-2.787481,-4.797254,1.768760,-4.907671,-8.174693,-2.182200,6.309837,1.106372,-7.669066,7.165839,-4.487211,6.188396,-9.012985,-3.442194,-8.398216,-7.841981,9.787551,2.286325,0.590785,-5.381839,4.798726,9.486492,9.593507,4.613796,5.904737,-5.638039,-6.633414,3.408775,4.663635,-9.737924,-2.460390,-6.777780,4.718295,-8.609023,9.615576,4.770291,5.665877,4.482577,6.300555,-1.549841,6.626583,-4.970699,3.383917,-7.549476,3.190130,-9.812791,3.596762,-4.361164,3.299732,-6.917337,8.391589,9.725465,-1.622928,1.443157,1.267751,-2.347107,-5.154985,-2.221785,-1.450915,-4.751800,3.612240,7.720073,7.940485,-3.949929,9.841911,9.769000,-0.639285,3.458943,-9.796964,-2.734496,7.828976,-9.619799,-1.153533,5.248536,-4.200017,-4.126482,-7.044431,-1.337886,2.865817,-5.486917,1.191313,9.316869,1.042134,3.329586,-1.944545,3.994985,-1.418483,5.671066,8.354978,-9.681270,1.090787,7.692818,-8.361461,5.792661,-4.312880,-0.564377,-3.668906,9.163467,7.517071,5.505082,2.356894,9.034872,-2.182653,-5.704662,7.306165,5.177202,4.249292,-3.926818,5.720112,-0.868775,-6.979164,4.683875,-4.638825,-0.724685,7.622185,4.921458,-3.726259,1.260497,-1.765244,-9.102705,-6.044368,-0.862988,5.059100,0.386260,-4.334580,-1.351660,5.478502,1.533663,2.167382,1.592178,3.542235,9.479357,1.156086,5.408742,-5.775312,1.712838,9.973577,-6.843955,-1.671622,2.155160,5.079631,8.071807,-4.070383,6.802178,-7.071370,-4.984965,2.207686,-4.222557,-9.882293,-4.241992,3.286940,7.787453,9.722835,1.796683,-0.307018,5.155325,3.857318,-4.925293,3.280849,2.923539,-5.398515,-1.097121,8.315028,-3.484952,-0.935594,-2.264711,-4.556584,-7.462694,0.159297,9.569580,8.961032,-5.474161,-5.016624,-6.362013,-1.480258,7.774689,7.496082,-6.535174,-6.176540,8.643812,-7.457957,3.864742,8.838459,-7.354446,2.647790,-5.243173,-1.654666,1.464507,5.805096,3.161787,2.647383,-6.094424,-8.941550,4.248441,0.931306,6.660324,-0.960506,-1.722459,-1.903452,9.081833,2.605047,-8.352382,-0.151830,-3.455261,4.100073,0.686590,-6.546234,-3.622194,-4.222290,-1.875168,-5.844974,0.109795,-1.590676,-5.331963,7.981113,-6.209837,-6.657339,-9.669332,1.648652,-6.707628,-6.674877,9.093431,-1.901780,6.485687,-0.088089,-2.854484,4.017572,5.001698,-3.164384,3.260341,4.342695,-4.117945,-1.157845,-6.304907,0.021365,3.789403,-5.919590,-6.803634,-0.314923,-5.057713,9.852633,7.165431,-6.004066,-1.733074,-8.101303,-7.356038,-7.571548,8.122238,-4.711370,-1.449681,9.062757,3.888395,-9.190728,-5.667379,-1.464251,5.789043], dtype = "float64")#candidate|8533|(315,)|const|float64
call_8532 = relay.TupleGetItem(func_3976_call(relay.reshape(const_8533.astype('float64'), [5, 63]), relay.reshape(const_8533.astype('float64'), [5, 63]), ), 3)
call_8534 = relay.TupleGetItem(func_3979_call(relay.reshape(const_8533.astype('float64'), [5, 63]), relay.reshape(const_8533.astype('float64'), [5, 63]), ), 3)
output = relay.Tuple([call_8528,call_8532,const_8533,])
output2 = relay.Tuple([call_8529,call_8534,const_8533,])
func_8540 = relay.Function([], output)
mod['func_8540'] = func_8540
mod = relay.transform.InferType()(mod)
mutated_mod['func_8540'] = func_8540
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8540_call = mutated_mod.get_global_var('func_8540')
call_8541 = func_8540_call()
output = call_8541
func_8542 = relay.Function([], output)
mutated_mod['func_8542'] = func_8542
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7258_call = mod.get_global_var('func_7258')
func_7259_call = mutated_mod.get_global_var('func_7259')
call_8555 = relay.TupleGetItem(func_7258_call(), 3)
call_8556 = relay.TupleGetItem(func_7259_call(), 3)
func_2037_call = mod.get_global_var('func_2037')
func_2040_call = mutated_mod.get_global_var('func_2040')
const_8562 = relay.const([[6.450743,-7.350276,-0.940030,9.082168,-0.225420,9.338514,6.109998,3.377513,-9.151472,-5.080972,4.014715,6.833747,-1.676027,3.505960,5.555721,1.363177,-4.828079,7.846416,-2.730365,5.637123,-2.764502,-3.033961,-9.290254,9.726517,-9.682017,-6.366314,7.979855,2.400091,-0.332421,-6.593317,-2.855976,0.518401,-2.419114,2.222109,7.031017,5.421823,9.642434,1.100413,3.273833,-5.413639,-9.778993,0.357585,5.001750,-5.797278,-8.518849,4.285069,-8.684090,5.629595,-2.929943,7.046952,-9.536852,5.953960,-1.451764,3.281391,-7.205772,9.697332,-1.326202,-1.949129,-5.478214,-5.797064,4.504670,3.642982,-8.052051,-8.396828,-2.719332,-5.809917,8.451743,-3.669963,9.822361,0.490802,-8.914354,-5.566692,-4.201112,-2.423019,6.881869,6.833929,-5.847029,6.228048,7.188876,6.682354,5.749518,-0.094044,-6.163772,4.104870,-5.344199,3.319449,8.651616,-7.253688,-0.679962,-4.809084,3.453309,-5.952758,6.724165,-9.000024,-4.131676,-1.761228,2.358483,-8.775929,8.048461,5.015641,-3.584863,-6.852928,4.117524,8.010479,6.910453,9.109441,5.568903,1.628773,0.464743,-2.368905,0.335642,-1.880755,2.691414,-1.262722,-0.401580,4.416071,-7.193062,-5.021568,-0.098696,1.193524,-0.279877,-7.522593,6.246263,-8.901837,7.154957,-9.054055,5.202713,3.601877,1.767463,5.147170,-8.404794,-4.137266,0.376100,-5.764193,2.206416,8.984280,-7.809123,6.570709,6.781793,7.962547,-6.539813,-9.445898,-9.918795,8.432711],[8.479078,1.714990,2.430111,7.529428,-1.013718,-6.227883,9.375580,5.956601,3.651317,5.443506,-9.177345,4.312995,-8.219271,-9.966736,2.456798,-7.392284,3.379248,-2.260842,-4.226714,8.662999,9.474333,-5.274560,5.233523,1.024172,-7.939371,-2.881937,1.509242,-3.209271,7.272977,-0.669630,-8.355067,4.349381,-1.772470,-2.425314,6.952965,8.326889,7.723966,-3.748352,-9.763066,2.401305,-4.654248,8.935437,9.131160,-2.245658,1.287807,6.457574,8.323795,0.054978,7.746987,-0.701367,7.847780,8.084340,0.177801,0.260599,2.788292,8.873406,-5.020158,3.199365,-7.649423,-1.922753,-1.602082,4.915870,1.365094,7.526229,-5.878657,4.144927,-4.062554,-0.118630,-1.725934,3.140216,-3.045448,-3.988329,3.164453,-6.944289,3.747494,8.543012,-3.976732,6.271150,5.399335,-0.498511,1.649835,7.941291,3.717751,3.550750,-9.157076,5.808966,5.848110,9.776878,-3.132496,-1.965657,4.439928,8.389226,-0.752260,0.747148,-9.241450,0.633246,5.871803,1.827861,-0.498397,4.826154,8.792443,7.475019,-5.619198,9.886632,-6.128642,-0.507605,-2.185726,-7.764904,-5.974865,-4.053908,6.793326,-4.114816,2.551722,7.641534,5.106942,-2.369527,-9.572723,7.087790,-1.394333,5.533649,8.511916,-0.412621,3.865695,-5.932853,-6.646646,-1.445121,3.026324,4.595538,-4.750391,-8.090028,7.039685,-7.597185,5.630892,-0.118252,7.670319,-9.034349,9.134136,-0.507204,9.811734,-9.569258,2.691363,-1.589638,-4.886605,3.288916]], dtype = "float32")#candidate|8562|(2, 144)|const|float32
var_8563 = relay.var("var_8563", dtype = "float32", shape = (468,))#candidate|8563|(468,)|var|float32
call_8561 = relay.TupleGetItem(func_2037_call(relay.reshape(const_8562.astype('float32'), [3, 6, 16]), relay.reshape(var_8563.astype('float32'), [468,]), ), 4)
call_8564 = relay.TupleGetItem(func_2040_call(relay.reshape(const_8562.astype('float32'), [3, 6, 16]), relay.reshape(var_8563.astype('float32'), [468,]), ), 4)
var_8574 = relay.var("var_8574", dtype = "float32", shape = (2, 144))#candidate|8574|(2, 144)|var|float32
bop_8575 = relay.bitwise_or(const_8562.astype('uint32'), relay.reshape(var_8574.astype('uint32'), relay.shape_of(const_8562))) # shape=(2, 144)
func_2037_call = mod.get_global_var('func_2037')
func_2040_call = mutated_mod.get_global_var('func_2040')
call_8584 = relay.TupleGetItem(func_2037_call(relay.reshape(bop_8575.astype('float32'), [3, 6, 16]), relay.reshape(var_8563.astype('float32'), [468,]), ), 2)
call_8585 = relay.TupleGetItem(func_2040_call(relay.reshape(bop_8575.astype('float32'), [3, 6, 16]), relay.reshape(var_8563.astype('float32'), [468,]), ), 2)
uop_8586 = relay.acos(var_8574.astype('float32')) # shape=(2, 144)
func_7224_call = mod.get_global_var('func_7224')
func_7226_call = mutated_mod.get_global_var('func_7226')
call_8590 = relay.TupleGetItem(func_7224_call(), 1)
call_8591 = relay.TupleGetItem(func_7226_call(), 1)
uop_8596 = relay.tan(uop_8586.astype('float32')) # shape=(2, 144)
uop_8606 = relay.exp(uop_8596.astype('float32')) # shape=(2, 144)
uop_8608 = relay.erf(uop_8606.astype('float64')) # shape=(2, 144)
output = relay.Tuple([call_8555,call_8561,var_8563,bop_8575,call_8584,call_8590,uop_8608,])
output2 = relay.Tuple([call_8556,call_8564,var_8563,bop_8575,call_8585,call_8591,uop_8608,])
func_8614 = relay.Function([var_8563,var_8574,], output)
mod['func_8614'] = func_8614
mod = relay.transform.InferType()(mod)
var_8615 = relay.var("var_8615", dtype = "float32", shape = (468,))#candidate|8615|(468,)|var|float32
var_8616 = relay.var("var_8616", dtype = "float32", shape = (2, 144))#candidate|8616|(2, 144)|var|float32
output = func_8614(var_8615,var_8616,)
func_8617 = relay.Function([var_8615,var_8616,], output)
mutated_mod['func_8617'] = func_8617
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5878_call = mod.get_global_var('func_5878')
func_5880_call = mutated_mod.get_global_var('func_5880')
call_8622 = relay.TupleGetItem(func_5878_call(), 0)
call_8623 = relay.TupleGetItem(func_5880_call(), 0)
output = relay.Tuple([call_8622,])
output2 = relay.Tuple([call_8623,])
func_8642 = relay.Function([], output)
mod['func_8642'] = func_8642
mod = relay.transform.InferType()(mod)
mutated_mod['func_8642'] = func_8642
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8642_call = mutated_mod.get_global_var('func_8642')
call_8643 = func_8642_call()
output = call_8643
func_8644 = relay.Function([], output)
mutated_mod['func_8644'] = func_8644
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7966_call = mod.get_global_var('func_7966')
func_7968_call = mutated_mod.get_global_var('func_7968')
call_8659 = relay.TupleGetItem(func_7966_call(), 0)
call_8660 = relay.TupleGetItem(func_7968_call(), 0)
var_8661 = relay.var("var_8661", dtype = "float64", shape = (7, 11, 5))#candidate|8661|(7, 11, 5)|var|float64
bop_8662 = relay.less(call_8659.astype('bool'), relay.reshape(var_8661.astype('bool'), relay.shape_of(call_8659))) # shape=(7, 11, 5)
bop_8665 = relay.less(call_8660.astype('bool'), relay.reshape(var_8661.astype('bool'), relay.shape_of(call_8660))) # shape=(7, 11, 5)
output = relay.Tuple([bop_8662,])
output2 = relay.Tuple([bop_8665,])
func_8671 = relay.Function([var_8661,], output)
mod['func_8671'] = func_8671
mod = relay.transform.InferType()(mod)
mutated_mod['func_8671'] = func_8671
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8672 = relay.var("var_8672", dtype = "float64", shape = (7, 11, 5))#candidate|8672|(7, 11, 5)|var|float64
func_8671_call = mutated_mod.get_global_var('func_8671')
call_8673 = func_8671_call(var_8672)
output = call_8673
func_8674 = relay.Function([var_8672], output)
mutated_mod['func_8674'] = func_8674
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2899_call = mod.get_global_var('func_2899')
func_2900_call = mutated_mod.get_global_var('func_2900')
call_8687 = relay.TupleGetItem(func_2899_call(), 0)
call_8688 = relay.TupleGetItem(func_2900_call(), 0)
output = relay.Tuple([call_8687,])
output2 = relay.Tuple([call_8688,])
func_8697 = relay.Function([], output)
mod['func_8697'] = func_8697
mod = relay.transform.InferType()(mod)
output = func_8697()
func_8698 = relay.Function([], output)
mutated_mod['func_8698'] = func_8698
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8175_call = mod.get_global_var('func_8175')
func_8177_call = mutated_mod.get_global_var('func_8177')
call_8721 = relay.TupleGetItem(func_8175_call(), 1)
call_8722 = relay.TupleGetItem(func_8177_call(), 1)
func_4519_call = mod.get_global_var('func_4519')
func_4523_call = mutated_mod.get_global_var('func_4523')
const_8731 = relay.const([-5.052688,3.398204,9.858232,3.859195,-2.598564,1.532945,2.276411,2.676654,9.019433,1.953540,3.044338,6.558015,0.695242,2.486838,2.493318,2.792607,6.449195,7.906895,-4.972948,-2.847102,-8.392319,7.623699,-5.092259,-5.302278,7.886562,7.773652,-8.453472,7.520661,2.686054,-8.784973,7.290005,-1.715206,3.637163,4.795485,4.496356,-7.003145,6.824976,6.948341,-1.337543,7.219149,1.460187,9.966209,-8.575261,7.503222,0.579534,-9.351456,-3.564454,3.033574,7.337532,3.673881,-0.790807,-7.989191,0.953434,5.040777,6.080178,5.199614,1.919385,-7.781671,-7.372766,1.348122,-8.820432,-5.199843,4.361132,-9.299649,3.585191,5.103144,9.314839,3.403195,1.405408,6.649670,-8.708814,-4.874164,7.902503,4.747230,-0.623702,3.869547,-3.608453,5.687672,1.345657,-1.064779,-8.260965,-8.142581,-9.446761,-9.624068,-1.008299,-5.824677,2.606847,9.204975,-9.412670,-5.741463,9.877959,8.101828,7.325173,6.540223,-2.767919,5.987851,1.539396,-0.858499,-9.146375,-1.435641,-6.171749,5.971888,8.007340,-0.520921,5.479221,-4.643981,-6.451402,-4.397429,0.362343,-5.915713,-5.519581,-3.237277], dtype = "float64")#candidate|8731|(112,)|const|float64
const_8732 = relay.const([False,False,True,False,False,False,True,False,False,False,True,True,False,True,True,True,False,False,True,False,False,True,False,True,True,False,True,False,True,True,False,True,True,True,False,True,False,True,False,False,True,True,False,False,False,True,True,True,True,True,True,True,False,True,True,True,True,False,True,False,True,True,False,True,True,False,False,True,True,False,True,True,True,True,True,False,False,False,True,False,True,False,True,False,False,False,True,True,False,True,False,False,False,False,True,True,False,True,False,True,False,False,False,True,True,True,True,False,False,False,False,True,True,True,True,True,False,True,False,False,False,False,False,False,False,True,False,False,True,False,False,True,False,False,False,False,False,False,False,False,False,False,True,True,True,True,False,True,False,True,False,False,True,False,False,False,False,False,False,True,True,False,False,True,True,False,True,True,False,True,True,True,True,False,False,True,True,True,False,True,False,False,True,True,True,False,True,True,False,False,False,True,False,False,True,True,False,False,False,True,False,True,False,True,False,False,False,True,True,True,True,True,True,False,True,False,False,False,True,True,False,True,False,True,True,True,False,False,False,True,True,False,False,True,True,False,True,False,False,True,True,True,False,False,True,True,True,False,False,False,True,False,False,True,True,True,True,False,True,True,True,False,True,True,True,False,False,True,False,False,False,True,True,False,False,False,False,True,False,False,True,True,False,True,True,False,True,False,False,False,True,True,True,False,False,False,False,False,True,True,False,True,False,True,False,False,False,False,True,False,False,True,False,False,False,True,False,True,True,False,False,False,True,True,False,False,True,False,False,True,True,True,False,False,False,False,False,False,False,False,True,False,True,True,True,True,False,True,True,True,False,True,True,True,False,True,True,True,True,False,False,True,True,True,True,True,True,True,False,False,True,True,False,False,False,True,False,False,True,True,True,True,False,False,False,False,True,False,True,False,False,False,True,True,True,False,False,False,False,False,False,True,True,True,False,True,False,False,True,True,True,False,False,True,False,True,True,True,True,False,False,True,False,True,False,True,False,False,False,False,True,False,True,False,True,True,False,False,True,True,True,False,False,False,True,False,True,False,False,False,True,False,True,True,True,True,True,True,True,True,True,False,True,True,True,True,False,True], dtype = "bool")#candidate|8732|(468,)|const|bool
call_8730 = relay.TupleGetItem(func_4519_call(relay.reshape(const_8731.astype('float64'), [112,]), relay.reshape(const_8732.astype('bool'), [12, 13, 3]), relay.reshape(const_8732.astype('bool'), [12, 13, 3]), ), 4)
call_8733 = relay.TupleGetItem(func_4523_call(relay.reshape(const_8731.astype('float64'), [112,]), relay.reshape(const_8732.astype('bool'), [12, 13, 3]), relay.reshape(const_8732.astype('bool'), [12, 13, 3]), ), 4)
output = relay.Tuple([call_8721,call_8730,const_8731,const_8732,])
output2 = relay.Tuple([call_8722,call_8733,const_8731,const_8732,])
func_8736 = relay.Function([], output)
mod['func_8736'] = func_8736
mod = relay.transform.InferType()(mod)
output = func_8736()
func_8737 = relay.Function([], output)
mutated_mod['func_8737'] = func_8737
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6847_call = mod.get_global_var('func_6847')
func_6849_call = mutated_mod.get_global_var('func_6849')
call_8741 = relay.TupleGetItem(func_6847_call(), 0)
call_8742 = relay.TupleGetItem(func_6849_call(), 0)
func_6988_call = mod.get_global_var('func_6988')
func_6990_call = mutated_mod.get_global_var('func_6990')
var_8745 = relay.var("var_8745", dtype = "float32", shape = (468,))#candidate|8745|(468,)|var|float32
call_8744 = relay.TupleGetItem(func_6988_call(relay.reshape(var_8745.astype('float32'), [468,])), 0)
call_8746 = relay.TupleGetItem(func_6990_call(relay.reshape(var_8745.astype('float32'), [468,])), 0)
func_3694_call = mod.get_global_var('func_3694')
func_3696_call = mutated_mod.get_global_var('func_3696')
call_8764 = func_3694_call()
call_8765 = func_3694_call()
func_5967_call = mod.get_global_var('func_5967')
func_5969_call = mutated_mod.get_global_var('func_5969')
call_8799 = relay.TupleGetItem(func_5967_call(), 0)
call_8800 = relay.TupleGetItem(func_5969_call(), 0)
func_8268_call = mod.get_global_var('func_8268')
func_8273_call = mutated_mod.get_global_var('func_8273')
var_8809 = relay.var("var_8809", dtype = "uint64", shape = ())#candidate|8809|()|var|uint64
var_8810 = relay.var("var_8810", dtype = "uint64", shape = (2, 640))#candidate|8810|(2, 640)|var|uint64
var_8811 = relay.var("var_8811", dtype = "int64", shape = (1080,))#candidate|8811|(1080,)|var|int64
call_8808 = relay.TupleGetItem(func_8268_call(relay.reshape(var_8809.astype('uint64'), []), relay.reshape(var_8810.astype('uint64'), [16, 8, 10]), relay.reshape(var_8745.astype('float32'), [468,]), relay.reshape(var_8811.astype('int64'), [1080,]), ), 0)
call_8812 = relay.TupleGetItem(func_8273_call(relay.reshape(var_8809.astype('uint64'), []), relay.reshape(var_8810.astype('uint64'), [16, 8, 10]), relay.reshape(var_8745.astype('float32'), [468,]), relay.reshape(var_8811.astype('int64'), [1080,]), ), 0)
func_6065_call = mod.get_global_var('func_6065')
func_6067_call = mutated_mod.get_global_var('func_6067')
call_8826 = relay.TupleGetItem(func_6065_call(), 1)
call_8827 = relay.TupleGetItem(func_6067_call(), 1)
output = relay.Tuple([call_8741,call_8744,var_8745,call_8764,call_8799,call_8808,var_8809,var_8810,var_8811,call_8826,])
output2 = relay.Tuple([call_8742,call_8746,var_8745,call_8765,call_8800,call_8812,var_8809,var_8810,var_8811,call_8827,])
func_8835 = relay.Function([var_8745,var_8809,var_8810,var_8811,], output)
mod['func_8835'] = func_8835
mod = relay.transform.InferType()(mod)
var_8836 = relay.var("var_8836", dtype = "float32", shape = (468,))#candidate|8836|(468,)|var|float32
var_8837 = relay.var("var_8837", dtype = "uint64", shape = ())#candidate|8837|()|var|uint64
var_8838 = relay.var("var_8838", dtype = "uint64", shape = (2, 640))#candidate|8838|(2, 640)|var|uint64
var_8839 = relay.var("var_8839", dtype = "int64", shape = (1080,))#candidate|8839|(1080,)|var|int64
output = func_8835(var_8836,var_8837,var_8838,var_8839,)
func_8840 = relay.Function([var_8836,var_8837,var_8838,var_8839,], output)
mutated_mod['func_8840'] = func_8840
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4738_call = mod.get_global_var('func_4738')
func_4740_call = mutated_mod.get_global_var('func_4740')
call_8850 = relay.TupleGetItem(func_4738_call(), 1)
call_8851 = relay.TupleGetItem(func_4740_call(), 1)
func_4088_call = mod.get_global_var('func_4088')
func_4090_call = mutated_mod.get_global_var('func_4090')
call_8866 = relay.TupleGetItem(func_4088_call(), 2)
call_8867 = relay.TupleGetItem(func_4090_call(), 2)
output = relay.Tuple([call_8850,call_8866,])
output2 = relay.Tuple([call_8851,call_8867,])
func_8878 = relay.Function([], output)
mod['func_8878'] = func_8878
mod = relay.transform.InferType()(mod)
output = func_8878()
func_8879 = relay.Function([], output)
mutated_mod['func_8879'] = func_8879
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5626_call = mod.get_global_var('func_5626')
func_5627_call = mutated_mod.get_global_var('func_5627')
call_8880 = func_5626_call()
call_8881 = func_5626_call()
func_2037_call = mod.get_global_var('func_2037')
func_2040_call = mutated_mod.get_global_var('func_2040')
var_8888 = relay.var("var_8888", dtype = "float32", shape = (288,))#candidate|8888|(288,)|var|float32
call_8887 = relay.TupleGetItem(func_2037_call(relay.reshape(var_8888.astype('float32'), [3, 6, 16]), relay.reshape(call_8880.astype('float32'), [468,]), ), 1)
call_8889 = relay.TupleGetItem(func_2040_call(relay.reshape(var_8888.astype('float32'), [3, 6, 16]), relay.reshape(call_8880.astype('float32'), [468,]), ), 1)
func_3437_call = mod.get_global_var('func_3437')
func_3439_call = mutated_mod.get_global_var('func_3439')
call_8891 = func_3437_call()
call_8892 = func_3437_call()
var_8900 = relay.var("var_8900", dtype = "bool", shape = (4, 4, 7))#candidate|8900|(4, 4, 7)|var|bool
bop_8901 = relay.divide(call_8887.astype('float32'), relay.reshape(var_8900.astype('float32'), relay.shape_of(call_8887))) # shape=(4, 4, 7)
bop_8904 = relay.divide(call_8889.astype('float32'), relay.reshape(var_8900.astype('float32'), relay.shape_of(call_8889))) # shape=(4, 4, 7)
output = relay.Tuple([call_8880,var_8888,call_8891,bop_8901,])
output2 = relay.Tuple([call_8881,var_8888,call_8892,bop_8904,])
func_8908 = relay.Function([var_8888,var_8900,], output)
mod['func_8908'] = func_8908
mod = relay.transform.InferType()(mod)
var_8909 = relay.var("var_8909", dtype = "float32", shape = (288,))#candidate|8909|(288,)|var|float32
var_8910 = relay.var("var_8910", dtype = "bool", shape = (4, 4, 7))#candidate|8910|(4, 4, 7)|var|bool
output = func_8908(var_8909,var_8910,)
func_8911 = relay.Function([var_8909,var_8910,], output)
mutated_mod['func_8911'] = func_8911
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8540_call = mod.get_global_var('func_8540')
func_8542_call = mutated_mod.get_global_var('func_8542')
call_8958 = relay.TupleGetItem(func_8540_call(), 0)
call_8959 = relay.TupleGetItem(func_8542_call(), 0)
func_6040_call = mod.get_global_var('func_6040')
func_6043_call = mutated_mod.get_global_var('func_6043')
var_8974 = relay.var("var_8974", dtype = "int16", shape = (512,))#candidate|8974|(512,)|var|int16
call_8973 = relay.TupleGetItem(func_6040_call(relay.reshape(var_8974.astype('int16'), [16, 4, 8]), relay.reshape(var_8974.astype('int16'), [16, 4, 8]), ), 1)
call_8975 = relay.TupleGetItem(func_6043_call(relay.reshape(var_8974.astype('int16'), [16, 4, 8]), relay.reshape(var_8974.astype('int16'), [16, 4, 8]), ), 1)
func_2921_call = mod.get_global_var('func_2921')
func_2923_call = mutated_mod.get_global_var('func_2923')
call_8982 = relay.TupleGetItem(func_2921_call(), 0)
call_8983 = relay.TupleGetItem(func_2923_call(), 0)
output = relay.Tuple([call_8958,call_8973,var_8974,call_8982,])
output2 = relay.Tuple([call_8959,call_8975,var_8974,call_8983,])
func_8991 = relay.Function([var_8974,], output)
mod['func_8991'] = func_8991
mod = relay.transform.InferType()(mod)
mutated_mod['func_8991'] = func_8991
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8992 = relay.var("var_8992", dtype = "int16", shape = (512,))#candidate|8992|(512,)|var|int16
func_8991_call = mutated_mod.get_global_var('func_8991')
call_8993 = func_8991_call(var_8992)
output = call_8993
func_8994 = relay.Function([var_8992], output)
mutated_mod['func_8994'] = func_8994
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4108_call = mod.get_global_var('func_4108')
func_4109_call = mutated_mod.get_global_var('func_4109')
call_8998 = func_4108_call()
call_8999 = func_4108_call()
func_8835_call = mod.get_global_var('func_8835')
func_8840_call = mutated_mod.get_global_var('func_8840')
var_9008 = relay.var("var_9008", dtype = "uint64", shape = ())#candidate|9008|()|var|uint64
const_9009 = relay.const([8,-7,-10,10,-10,-4,2,-5,9,-7,-5,-10,10,6,2,-9,9,9,-8,3,5,-10,-1,4,-9,3,-2,3,-4,-3,8,9,2,7,8,-8,7,-1,-7,8,-8,9,4,1,3,-6,-8,10,-4,1,-9,4,9,4,-4,1,5,-1,2,-1,-6,7,2,3,4,-8,3,9,-1,9,9,-7,-1,-5,8,9,-5,-7,2,2,4,-9,4,-2,-2,10,2,-8,-4,8,-1,6,-1,-2,3,-1,6,7,-7,-6,-9,-2,4,5,-5,1,-8,-1,-10,-4,-6,1,4,-3,6,-1,4,7,7,7,5,-7,5,-3,-10,-9,1,-10,9,-7,-1,-1,6,-4,-9,3,8,-8,8,9,10,6,-9,8,8,-2,-6,3,-10,2,-5,-7,9,-6,-7,-6,-5,8,-7,-2,2,3,9,-9,-2,-10,10,-9,-3,5,-2,-6,-3,10,3,-6,-6,-4,-4,3,5,-4,3,1,10,5,-9,10,-7,2,2,6,9,-4,4,1,-3,4,8,-1,5,4,-6,4,7,-5,7,9,-3,9,10,-7,-4,-8,-10,3,-4,-7,-3,4,-10,1,10,3,2,-1,1,7,10,-10,-6,-6,-1,-1,-8,6,-3,5,-6,-7,10,5,7,-9,-1,9,-3,8,-10,10,-3,3,-3,9,7,-2,-5,10,-10,9,7,9,-3,-6,7,10,-4,7,-3,1,-4,9,-1,-9,8,-4,-8,-9,-1,5,-2,-9,-9,-6,-3,-4,-1,6,4,2,-5,-10,-9,-5,3,10,6,4,4,-10,6,-5,1,-8,7,8,4,7,7,6,4,7,-3,-7,-10,7,-5,4,2,-10,10,2,-7,9,-1,-6,-9,6,4,3,2,-2,10,10,6,2,-9,-9,-3,8,3,2,-9,-6,-2,6,8,-1,-4,2,-1,5,1,6,-4,2,10,-9,-2,9,5,8,-5,-6,9,8,-4,-2,9,-1,-2,-10,6,-9,-6,2,8,-7,-10,2,10,-1,-7,9,1,-10,-2,-7,-10,7,-7,-7,9,-7,-6,-8,3,3,4,-7,-4,10,-7,-6,-5,1,10,-8,4,9,6,-8,-9,-10,-5,-10,4,-4,-8,6,-3,-7,6,3,-1,-2,10,-6,3,1,-3,-4,2,-5,-8,4,-9,4,4,-7,-2,2,1,2,-5,9,-6,6,2,-6,4,4,1,-1,7,-2,9,10,3,3,5,-8,6,8,-5,2,6,-5,4,-4,3,10,9,1,4,-9,-7,-1,-1,3,-3,7,1,-6,7,-7,-5,2,9,-3,-7,-3,9,7,2,6,-7,3,-5,4,-1,2,-10,-10,-8,-3,7,-9,-9,-6,10,-6,-7,4,10,-1,9,-8,10,7,5,2,7,10,-2,8,-10,-1,-5,-6,5,7,5,-2,-7,10,2,-6,7,-6,2,-3,8,9,8,-8,5,6,3,4,8,2,7,-8,3,5,8,10,-1,9,4,-2,-5,10,8,-9,-5,-8,-10,9,2,9,-4,-6,-7,8,-4,-2,-1,-8,4,7,10,-4,-4,6,-10,6,5,1,-8,-3,1,1,6,1,7,-9,-7,-9,-7,9,-9,3,8,6,-5,6,2,8,-7,8,-8,4,2,-8,-8,8,1,-3,-5,5,-6,6,10,-8,2,2,-6,7,2,1,-10,9,-2,2,-9,-7,-10,5,-6,9,-2,8,-9,-8,-10,-1,9,6,10,9,7,-6,-1,-8,-7,-5,-10,-1,-9,10,-9,10,10,-9,3,2,6,-8,-3,1,3,-3,10,2,2,-9,-10,8,6,-2,5,-1,-4,-7,-7,-8,-6,-3,-2,8,-4,4,-7,-6,10,-3,2,8,-7,4,3,4,3,-8,10,-1,-2,-10,9,-3,2,8,4,-1,-10,4,-6,-3,-6,6,-6,2,-3,-8,-8,1,-10,5,4,-6,-8,-8,-9,-3,-1,-10,-3,-4,5,-9,6,3,1,-10,2,9,-8,-4,7,1,4,6,6,-6,-3,-1,6,-5,-2,2,-2,-5,10,-7,-5,-9,-2,8,5,6,-8,-9,3,-1,-8,10,-8,8,2,-6,-4,8,10,-1,-2,4,-7,6,4,4,4,2,9,-9,7,-10,2,6,-7,-8,-7,-1,-7,2,-8,-5,-4,-4,9,4,1,-5,-3,9,-10,-9,1,-9,8,-2,-2,1,-4,-7,-8,-6,-6,-6,-4,6,-1,-2,6,-3,-5,-3,3,-2,-6,-1,1,-5,-10,5,5,-1,6,-3,5,7,2,-6,3,-4,-1,7,-4,-9,5,-2,5,9,5,4,-9,-9,-2,-9,-6,-7,-8,7,9,8,-1,-6,-2,-8,8,-8,-4,9,-3,-2,-1,-6,-5,3,-10,-10,9,-7,-3,-9,-8,8,-5,7,-7,-7,-10,-9,7,-1,-3,7,-8,-3,1,10,9,9,-8,2,-7,-6,-3,6,-7,6,-9,-1,9,-8,8,-10,-7,-2,9,-2,4,-5,-5,6,9,1,7,5,-10,8,10,-4,9,5,10,4,7,3,-2,3,1,9,8,3,8,5,-9,8,6,8,1,10,-3,10,-1,9,7,-1,-4,4,-8,-10,9,-7,-1,1,-8,10,3,9,10,-10,-5,-3,-7,-1,-7,2,-8,1,5,-1,-2,-4,-10,-2,10,9,-3,4,-9,-3,-7,2,-5,7,4,2,-1,-2,-1,1,-8,-9,-3,9,10,-8,-8,-4,-3,2,9,3,2,10,2,5,2,-1,8,6,-3,-7,-3,5,-10,-3,-2,-8,4,6,-9,-5,6,5,5,4,-6,-8,-9,-4,9,9,-4,4,9,5,2,1,6,-1,-7,-1,-3,-1,2,-3,-5,-2,3,8,-7,-10,-2,6,6,3,10,8,2,8,-5,7,-7,-10,7,2,10,3,-4,-2,-6,-8,8,10,5,6,-10,1,-3,8,10,4,-6,2,5,4,10,8,8,-9,-7,-3,9,-4,5,-2,6,5,-4,5,4,3,-1,-3,10,-2,-9,5,10,-2,-3,-2,-2,-2,7,-8,-7,4,-3,-9,-6,-1,9,-5,-5,-6,1,9,6,-10,1,1,-2,-7,1,-9,10,-4,-5,-8,3,-1,1,-8,5,9,7,-5,-6,-5,10,-3,-3,9,-5,-10,-10,-5,-3,7,2,-6,-7,-9,5,9,-7,8,-1,-7,4,9,8,-3,6,1,-10,-6,-7,-2,-8,-8,5,-2,-2,7,8,-10,-9,-9,4,10,6,1,-10,6,3,-2,9,-7,4,-9,-9,1,1,-2,2,1,9,-1,-4,-8,10,-7,3,-2,-1,9,1,7,-10,8,-2,-9,-10,1,-7,3,10,-8,8,-10,-2,-9,1,-4,-7,-4,-1,2,-5,-7,6,2,4,9,-10,2,-9,7,-9,2,3,-8,1,10], dtype = "uint64")#candidate|9009|(1280,)|const|uint64
const_9010 = relay.const([[10],[-9],[-4],[-2],[9],[9],[2],[-9],[1],[4],[-5],[-6],[10],[9],[1],[-4],[7],[-5],[4],[-9],[1],[-6],[1],[4],[7],[1],[10],[-3],[5],[8],[1],[6],[-7],[-10],[-10],[5],[9],[4],[9],[2],[-7],[7],[2],[-10],[6],[-4],[9],[-7],[-3],[-7],[-8],[-2],[-4],[-4],[4],[10],[-1],[-1],[-9],[-2],[8],[-3],[6],[-3],[-9],[-9],[5],[-1],[-10],[3],[-5],[9],[9],[8],[10],[6],[6],[5],[1],[8],[-8],[-4],[-10],[3],[2],[-8],[-8],[2],[7],[-7],[2],[5],[3],[9],[-5],[2],[5],[8],[3],[-7],[-7],[3],[-2],[-1],[6],[3],[1],[9],[7],[-6],[6],[8],[5],[7],[7],[-4],[-1],[-10],[-1],[9],[10],[9],[-2],[-5],[-6],[-1],[-10],[4],[-7],[5],[6],[-10],[6],[9],[2],[-9],[2],[4],[-6],[-2],[10],[5],[-2],[-7],[-9],[-3],[-4],[4],[-5],[-9],[3],[-9],[-4],[8],[2],[4],[-3],[3],[-7],[6],[-7],[-3],[-4],[-10],[9],[3],[-7],[-6],[5],[-3],[-6],[-10],[6],[-8],[-6],[-1],[5],[-3],[-10],[-7],[-4],[1],[-5],[2],[-3],[-7],[-2],[9],[10],[2],[-2],[-10],[-6],[6],[-10],[7],[5],[3],[6],[-10],[-10],[9],[-5],[1],[8],[3],[6],[-6],[10],[10],[-7],[4],[-4],[-4],[4],[-9],[-4],[-8],[9],[-6],[5],[-6],[5],[-5],[6],[-5],[-4],[-6],[7],[1],[5],[-6],[8],[-8],[5],[3],[-5],[1],[1],[-7],[3],[1],[-10],[-8],[-1],[8],[8],[-7],[-8],[-5],[-10],[3],[7],[5],[9],[-6],[-3],[-10],[8],[-2],[4],[6],[-6],[8],[9],[8],[-2],[-5],[2],[9],[-2],[-2],[4],[10],[9],[-10],[3],[-6],[-9],[4],[-8],[5],[1],[8],[-2],[3],[-2],[10],[10],[-7],[-5],[-3],[-2],[-9],[3],[-7],[4],[-2],[-6],[6],[-9],[-1],[-7],[-8],[-5],[5],[1],[8],[7],[4],[-9],[-3],[-7],[-7],[5],[-10],[-6],[5],[3],[10],[8],[8],[3],[5],[-3],[10],[-4],[-8],[5],[-3],[-1],[-5],[5],[10],[-3],[8],[4],[-3],[3],[-7],[-10],[2],[-1],[4],[-6],[-6],[-9],[3],[3],[4],[4],[9],[9],[6],[-1],[8],[-3],[3],[1],[-10],[6],[3],[9],[1],[-1],[-9],[-6],[-6],[-2],[7],[-9],[-5],[7],[4],[7],[4],[-10],[-9],[5],[2],[-5],[-1],[-3],[8],[-1],[-9],[3],[-1],[-3],[-8],[-1],[-4],[-1],[1],[-4],[-2],[-7],[-10],[1],[-4],[-4],[-3],[8],[-7],[10],[-1],[-2],[-1],[9],[7],[-6],[2],[1],[2],[3],[-4],[-10],[4],[-2],[-8],[10],[3],[-8],[3],[6],[-1],[-10],[-6],[9],[4],[-7],[-9],[-7],[4],[7],[2],[-5],[7],[9],[9],[1],[-8],[6],[-3],[5],[7],[8],[-8],[10],[-6],[5],[-2],[1],[2],[-9],[-5],[-4],[3],[-10],[-5],[6],[4],[9],[-10],[-3],[-3],[4],[-9],[-5],[7],[5],[-6],[7],[-8],[-10],[2],[8],[-1],[-8],[-3],[-7],[1],[2],[-6],[-2],[-2],[-5],[5],[2],[10],[10],[-7],[10],[5],[-6],[10],[5],[-5],[-3],[5],[-6],[-4],[9],[-4],[5],[-2],[-8],[3],[-4],[-5],[-7],[6],[-6],[10],[-5],[-7],[-3],[-3],[-10],[-3],[3],[-10],[-4],[-8],[-3],[1],[-9],[3],[-9],[5],[9],[-7],[2],[-7],[7],[7],[-7],[2],[4],[-10],[-6],[-9],[7],[10],[-9],[3],[8],[-2],[-10],[-3],[3],[8],[7],[-1],[-3],[-7],[1],[1],[10],[-7],[-8],[-8],[-10],[7],[1],[6],[7],[4],[-3],[4],[6],[-4],[9],[-7],[7],[-9],[6],[-1],[8],[-4],[-7],[-3],[-4],[10],[-9],[-5],[8],[-4],[-5],[8],[-6],[-8],[4],[7],[-9],[-1],[3],[3],[-10],[-7],[7],[-4],[1],[2],[8],[9],[6],[-6],[-1],[4],[-6],[-6],[-8],[6],[-2],[-7],[-5],[4],[10],[4],[-3],[-3],[2],[-9],[4],[3],[-8],[-1],[-10],[6],[-2],[-10],[7],[-4],[7],[4],[1],[-9],[9],[-4],[-1],[5],[5],[-8],[2],[6],[-9],[2],[-10],[1],[-4],[-7],[6],[-6],[4],[-8],[-6],[-6],[8],[6],[6],[-6],[10],[-10],[-6],[-6],[-10],[5],[-1],[-1],[-2],[1],[9],[-1],[-9],[-6],[2],[-1],[2],[1],[-2],[10],[1],[8],[-10],[-6],[7],[2],[-3],[4],[3],[7],[4],[6],[-9],[5],[5],[5],[-5],[-6],[3],[7],[9],[5],[-6],[2],[-9],[-5],[-8],[10],[-9],[1],[4],[-9],[-1],[4],[-9],[4],[-2],[-8],[8],[-10],[-2],[1],[-7],[7],[5],[1],[6],[-8],[7],[2],[3],[-3],[-5],[-5],[-2],[1],[9],[4],[-10],[-1],[1],[-6],[-2],[-3],[-4],[-4],[-1],[4],[-8],[10],[-4],[-6],[2],[9],[10],[-8],[-10],[5],[7],[-8],[5],[10],[10],[1],[-4],[10],[1],[-1],[3],[-4],[9],[-4],[-6],[-10],[9],[6],[1],[9],[1],[-9],[-10],[-3],[4],[-5],[-5],[2],[2],[-3],[-6],[-5],[-1],[10],[-8],[-3],[-10],[4],[-1],[2],[-4],[-2],[7],[4],[-1],[2],[-2],[-4],[-8],[6],[7],[5],[-2],[-7],[9],[-8],[-10],[3],[-4],[9],[-4],[3],[-7],[-8],[3],[-9],[3],[-8],[-4],[-10],[8],[-5],[8],[-6],[-2],[8],[-7],[3],[-9],[-7],[9],[5],[-1],[-9],[-9],[7],[6],[-4],[9],[-7],[-6],[-9],[9],[6],[-7],[4],[-10],[-7],[3],[-7],[2],[-10],[5],[3],[5],[-5],[8],[-3],[-9],[4],[-2],[1],[-7],[-5],[4],[-3],[-6],[-7],[10],[-7],[1],[-7],[7],[5],[-8],[2],[-7],[-4],[-1],[7],[10],[2],[-4],[9],[8],[-8],[-7],[7],[4],[9],[-10],[6],[4],[-2],[-10],[10],[8],[10],[-10],[7],[-6],[-8],[-9],[-8],[-4],[-6],[8],[2],[3],[-8],[-2],[5],[-10],[-5],[3],[-2],[-6],[-3],[-3],[9],[-7],[-4],[9],[8],[-9],[-7],[5],[-2],[-8],[-9],[8],[1],[10],[-10],[-2],[-2],[5],[4],[1],[8],[-10],[-10],[8],[2],[-10],[6],[-10],[3],[-10],[5],[-1],[-2],[5],[10],[10],[6],[2],[5],[-10],[5],[-7],[8],[-9],[-9],[4],[-2],[-3],[1],[10],[5],[-1],[2],[-9],[-5],[-3],[10],[3],[-9],[-9],[-3],[2],[-9],[-10],[4],[4],[-4],[10],[-2],[2],[-9],[10],[-6],[7],[7],[-2],[10],[6],[1],[-2],[9],[-2],[-2],[-6],[1],[-2],[4],[-10],[-4],[6],[5],[-2],[3],[6],[7],[9],[-3],[7],[-3],[-10],[3],[-7],[-3],[-7],[-5],[10],[2],[5],[-1],[9],[9],[4],[-9],[7],[-5],[10],[-8],[-7],[5],[-2],[9],[-10],[-4],[-8],[6],[-3],[-7],[8],[9],[10],[2],[-4],[-9],[3],[-6],[-4],[-7],[-8],[9],[-5],[3],[-1],[8],[-6],[5],[-1],[-8],[-7],[-5],[-8],[-5]], dtype = "int64")#candidate|9010|(1080, 1)|const|int64
call_9007 = relay.TupleGetItem(func_8835_call(relay.reshape(call_8998.astype('float32'), [468,]), relay.reshape(var_9008.astype('uint64'), []), relay.reshape(const_9009.astype('uint64'), [2, 640]), relay.reshape(const_9010.astype('int64'), [1080,]), ), 8)
call_9011 = relay.TupleGetItem(func_8840_call(relay.reshape(call_8998.astype('float32'), [468,]), relay.reshape(var_9008.astype('uint64'), []), relay.reshape(const_9009.astype('uint64'), [2, 640]), relay.reshape(const_9010.astype('int64'), [1080,]), ), 8)
func_7542_call = mod.get_global_var('func_7542')
func_7544_call = mutated_mod.get_global_var('func_7544')
var_9021 = relay.var("var_9021", dtype = "uint32", shape = (12,))#candidate|9021|(12,)|var|uint32
call_9020 = relay.TupleGetItem(func_7542_call(relay.reshape(var_9021.astype('uint32'), [3, 4])), 1)
call_9022 = relay.TupleGetItem(func_7544_call(relay.reshape(var_9021.astype('uint32'), [3, 4])), 1)
func_7542_call = mod.get_global_var('func_7542')
func_7544_call = mutated_mod.get_global_var('func_7544')
call_9036 = relay.TupleGetItem(func_7542_call(relay.reshape(var_9021.astype('uint32'), [3, 4])), 6)
call_9037 = relay.TupleGetItem(func_7544_call(relay.reshape(var_9021.astype('uint32'), [3, 4])), 6)
output = relay.Tuple([call_8998,call_9007,var_9008,const_9009,const_9010,call_9020,var_9021,call_9036,])
output2 = relay.Tuple([call_8999,call_9011,var_9008,const_9009,const_9010,call_9022,var_9021,call_9037,])
func_9046 = relay.Function([var_9008,var_9021,], output)
mod['func_9046'] = func_9046
mod = relay.transform.InferType()(mod)
var_9047 = relay.var("var_9047", dtype = "uint64", shape = ())#candidate|9047|()|var|uint64
var_9048 = relay.var("var_9048", dtype = "uint32", shape = (12,))#candidate|9048|(12,)|var|uint32
output = func_9046(var_9047,var_9048,)
func_9049 = relay.Function([var_9047,var_9048,], output)
mutated_mod['func_9049'] = func_9049
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3437_call = mod.get_global_var('func_3437')
func_3439_call = mutated_mod.get_global_var('func_3439')
call_9068 = func_3437_call()
call_9069 = func_3437_call()
output = call_9068
output2 = call_9069
func_9076 = relay.Function([], output)
mod['func_9076'] = func_9076
mod = relay.transform.InferType()(mod)
output = func_9076()
func_9077 = relay.Function([], output)
mutated_mod['func_9077'] = func_9077
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4549_call = mod.get_global_var('func_4549')
func_4551_call = mutated_mod.get_global_var('func_4551')
call_9114 = relay.TupleGetItem(func_4549_call(), 1)
call_9115 = relay.TupleGetItem(func_4551_call(), 1)
output = call_9114
output2 = call_9115
func_9122 = relay.Function([], output)
mod['func_9122'] = func_9122
mod = relay.transform.InferType()(mod)
mutated_mod['func_9122'] = func_9122
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9122_call = mutated_mod.get_global_var('func_9122')
call_9123 = func_9122_call()
output = call_9123
func_9124 = relay.Function([], output)
mutated_mod['func_9124'] = func_9124
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8043_call = mod.get_global_var('func_8043')
func_8044_call = mutated_mod.get_global_var('func_8044')
call_9161 = relay.TupleGetItem(func_8043_call(), 3)
call_9162 = relay.TupleGetItem(func_8044_call(), 3)
func_3302_call = mod.get_global_var('func_3302')
func_3303_call = mutated_mod.get_global_var('func_3303')
call_9167 = relay.TupleGetItem(func_3302_call(), 0)
call_9168 = relay.TupleGetItem(func_3303_call(), 0)
func_8697_call = mod.get_global_var('func_8697')
func_8698_call = mutated_mod.get_global_var('func_8698')
call_9180 = relay.TupleGetItem(func_8697_call(), 0)
call_9181 = relay.TupleGetItem(func_8698_call(), 0)
output = relay.Tuple([call_9161,call_9167,call_9180,])
output2 = relay.Tuple([call_9162,call_9168,call_9181,])
func_9187 = relay.Function([], output)
mod['func_9187'] = func_9187
mod = relay.transform.InferType()(mod)
mutated_mod['func_9187'] = func_9187
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9187_call = mutated_mod.get_global_var('func_9187')
call_9188 = func_9187_call()
output = call_9188
func_9189 = relay.Function([], output)
mutated_mod['func_9189'] = func_9189
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6643_call = mod.get_global_var('func_6643')
func_6645_call = mutated_mod.get_global_var('func_6645')
call_9206 = relay.TupleGetItem(func_6643_call(), 4)
call_9207 = relay.TupleGetItem(func_6645_call(), 4)
func_8445_call = mod.get_global_var('func_8445')
func_8446_call = mutated_mod.get_global_var('func_8446')
call_9210 = func_8445_call()
call_9211 = func_8445_call()
func_5967_call = mod.get_global_var('func_5967')
func_5969_call = mutated_mod.get_global_var('func_5969')
call_9213 = relay.TupleGetItem(func_5967_call(), 0)
call_9214 = relay.TupleGetItem(func_5969_call(), 0)
const_9218 = relay.const([[4,-9,-10,4,-6,9,2,-8,-5,-10,-4,3,-2,-8,10,6,1,-9,-8,-8,-5,-2,5,8,7,-3,5,-6,8,7,-9,2,-8,-1,-5,-1,-8,-7,-7,6,-1,6,6,6,-6,-4,5,7,6,-2,-10,3,-5,4,-3,5,-7,3,-3,-9],[-1,-5,8,2,3,5,6,-1,8,3,4,-9,-9,8,1,-2,-10,-1,-1,2,-6,5,-7,-2,-4,8,5,2,-8,-5,-6,1,5,4,-4,10,-3,1,3,-5,-8,-6,-8,6,-7,-7,9,-10,-10,10,3,4,-5,8,-8,-5,-5,9,9,1],[6,10,-6,10,7,9,-8,-5,-8,2,-5,-2,8,-6,-5,-3,-7,-8,5,10,-8,1,-2,2,9,-5,9,-7,-7,5,9,4,-3,8,2,10,-7,-9,-9,-2,-3,5,4,-2,-4,-6,-7,1,-5,-9,-9,9,2,-8,7,1,6,-3,-1,-5],[1,10,-4,-7,-1,7,7,-7,-4,-2,-4,-2,-3,3,9,1,-1,-6,-3,3,-3,-6,-6,1,-8,2,10,-4,-8,-6,-9,5,-7,5,7,-6,10,-1,4,8,-7,-6,4,-9,-1,9,2,-9,8,1,-4,6,-6,2,-2,-2,3,-5,1,3],[-1,-1,-8,-3,4,2,8,6,8,4,10,-9,5,4,-2,-8,-9,5,9,4,10,3,-5,-2,7,-2,-1,2,9,-1,-10,1,8,-7,-1,-10,4,-1,-2,-1,-8,-8,6,-6,-5,-5,8,4,-1,2,-1,-5,6,5,8,1,-1,-4,10,-1],[8,9,1,1,6,5,6,2,5,-1,3,8,10,10,-3,4,8,-9,-9,-10,6,2,-5,-3,2,-5,6,1,-7,-6,4,6,-3,9,-7,-7,-4,4,-7,-2,-1,-6,-10,4,7,-2,8,-3,2,3,10,-2,-2,6,3,8,2,-2,-10,4],[6,10,-3,-5,4,-6,-1,-1,-7,2,-2,6,6,-10,4,-6,1,4,-7,-1,-8,-5,7,4,2,4,6,-10,7,9,-6,-2,10,-1,7,-10,-10,6,1,-3,-5,7,-6,6,-8,9,-9,-9,8,-8,3,-2,2,-2,7,6,-2,-5,-3,-6],[-7,5,5,-7,-5,8,2,10,-7,7,-10,7,-9,2,7,-2,-2,-10,-2,-10,1,-4,-9,7,9,-9,8,-10,-2,8,2,-2,7,-3,-9,4,2,-5,4,-6,-7,-3,3,-1,-8,4,8,-4,10,-2,2,-8,-5,5,4,-6,6,-5,3,-6],[4,-10,-8,7,-4,6,8,10,7,-5,-7,-4,-10,-6,5,-3,3,-3,-10,8,1,9,8,-3,7,7,-10,-8,8,-3,-7,-3,-2,1,7,5,1,-7,3,3,-1,5,1,-4,-9,-3,-3,-7,3,6,-5,-7,-3,7,-6,8,-1,9,-6,1],[9,-10,-10,-9,4,2,4,-8,-4,5,-5,7,5,8,-8,5,-2,-2,-3,-3,4,-6,5,-9,9,8,8,10,1,3,4,7,-6,-8,9,5,9,6,-7,10,9,-8,3,-8,-3,-4,-10,4,-9,6,6,-3,-5,6,2,-6,5,-5,1,5],[-6,-4,9,4,-4,7,-4,-4,9,-10,7,-1,-1,5,2,9,-6,-6,-3,-2,-3,-7,-9,-5,-1,1,-1,4,-1,-6,-8,10,-8,-8,9,7,1,6,-5,8,5,5,4,-10,8,-7,-10,10,-5,10,8,-3,-1,9,-1,-1,-8,4,6,6],[-1,10,-2,-1,9,-1,9,8,-5,6,-5,4,-5,-5,2,7,-4,5,9,5,7,7,-1,6,1,4,2,1,-6,-10,-10,2,-6,-2,-2,5,2,-5,-6,-1,-4,-2,4,-4,2,1,-1,-5,-1,-3,3,-2,9,-10,-8,-1,9,-9,-9,-5],[6,-10,-10,-3,-2,-4,4,2,5,10,4,-8,-7,5,-9,-6,6,-2,-2,7,-3,1,-9,3,-4,9,-4,-10,-5,8,5,1,-1,10,-7,-7,10,-8,-2,2,3,3,-10,10,-8,-1,4,6,2,7,3,-2,6,1,-2,-4,-6,-4,-10,4],[-5,-10,-5,-2,-2,-10,7,-9,1,-10,5,-8,1,-9,-8,-8,6,-2,6,-9,7,7,-1,-6,8,-5,-2,-6,-7,-3,-8,10,2,-6,-7,9,4,7,-4,-8,-1,-7,-8,-5,10,1,-2,1,-4,2,-3,5,-9,-5,-7,5,-5,-2,-7,-9],[-6,4,-3,2,5,-9,7,6,-8,8,3,5,8,-3,4,-4,4,10,7,5,6,-8,9,8,4,-5,9,-7,7,6,3,2,9,3,4,6,1,4,8,9,7,-1,4,-7,-7,2,2,7,8,5,-9,3,-5,-10,-8,-6,-3,-5,-6,-5],[3,3,1,-7,10,-10,-3,9,-9,-2,9,4,-7,-8,1,-6,-3,10,-10,3,-8,-1,8,-8,10,-6,10,-3,-10,9,-6,-6,5,3,4,5,10,1,-5,-7,-1,-6,-4,7,9,5,-5,4,-8,5,-2,-4,-8,2,-5,2,3,-6,-6,1],[1,3,-9,-5,-2,1,-3,-8,-9,8,-9,-10,8,-9,9,2,-8,-3,1,-7,10,-1,-2,-6,9,-5,-4,-1,10,-9,-10,8,-7,8,-1,-5,3,-4,2,8,-5,10,-9,-2,-8,10,3,9,-9,7,4,-10,7,3,-3,-1,-3,8,1,-3],[-2,-9,10,-4,-7,-10,-5,9,4,1,5,8,2,-2,-7,-2,-9,-5,-2,-10,1,1,2,-8,-6,-6,3,-10,9,8,8,-4,-4,6,7,5,7,4,10,6,2,-6,7,10,10,1,-9,-5,-3,6,-6,-9,-9,-2,6,-4,3,3,-5,-3]], dtype = "int64")#candidate|9218|(18, 60)|const|int64
bop_9219 = relay.equal(call_9206.astype('bool'), relay.reshape(const_9218.astype('bool'), relay.shape_of(call_9206))) # shape=(18, 60)
bop_9222 = relay.equal(call_9207.astype('bool'), relay.reshape(const_9218.astype('bool'), relay.shape_of(call_9207))) # shape=(18, 60)
func_3859_call = mod.get_global_var('func_3859')
func_3861_call = mutated_mod.get_global_var('func_3861')
call_9227 = relay.TupleGetItem(func_3859_call(), 0)
call_9228 = relay.TupleGetItem(func_3861_call(), 0)
func_6040_call = mod.get_global_var('func_6040')
func_6043_call = mutated_mod.get_global_var('func_6043')
const_9232 = relay.const([-4,4,3,7,6,-1,-5,-3,3,-6,-1,4,7,1,7,6,2,-7,-7,-4,4,-9,8,-10,2,-7,3,3,7,6,7,-5,-5,3,9,-6,-5,-3,-5,-6,-3,9,6,-7,-5,7,8,-8,6,-6,1,7,-5,8,7,8,-7,-5,-9,8,-9,4,8,-10,-7,1,-8,-3,1,4,7,8,-9,9,-7,-9,-3,-6,9,7,-4,-4,-7,3,10,5,-9,3,6,-3,-10,-3,-9,4,-5,-6,9,9,-8,-3,-2,-6,-1,-9,3,-2,-6,4,4,-3,-8,9,-8,-3,-3,-5,-5,7,1,3,-8,7,-9,-9,-8,3,-1,5,-1,6,-3,10,-1,3,3,-8,-10,2,5,-4,4,-2,10,-6,4,-6,2,-6,-2,-7,-5,-5,9,6,-1,-8,8,1,5,-10,9,9,-1,-6,-4,-8,-7,5,2,-9,-2,7,-7,9,-8,-3,4,-10,-7,-7,-9,-9,10,10,5,-5,6,-6,-2,7,5,-7,-1,1,-1,-8,-5,-7,-3,7,8,-5,-3,9,8,-5,5,-2,-7,2,-1,-10,-7,1,4,8,-9,-6,7,-8,-1,-10,5,3,-2,1,5,-2,-8,4,1,4,8,2,7,-10,3,7,9,9,6,7,-1,6,1,3,-4,2,9,7,2,-8,-5,-2,-6,-8,-10,4,5,3,1,-8,3,9,3,-7,3,-9,-10,-5,-1,9,-9,5,4,-1,-3,4,-8,9,-8,6,4,2,-8,2,-9,3,5,-1,7,6,1,-8,-2,10,-5,-3,-6,3,-1,5,6,-5,5,10,8,-4,3,-7,10,6,8,2,-6,7,-8,5,-8,4,8,9,-7,4,6,-6,-9,-2,4,10,-1,-7,-7,4,7,-3,10,-1,-5,-1,-6,-7,-1,-3,-5,9,8,-4,10,-2,-5,-2,-7,4,-9,2,3,-2,10,-3,10,2,8,5,-5,-3,-2,-5,-9,10,7,-3,3,7,5,-2,-2,3,2,5,4,8,-4,-6,6,-1,2,-3,3,10,-10,1,7,-1,1,-6,6,3,-9,-5,9,-5,-1,-5,8,10,-10,-9,6,-7,8,4,-7,5,7,10,3,-6,2,9,-9,-8,-2,5,9,-7,-5,-10,-7,8,-5,2,4,4,-1,7,-4,6,-2,-5,3,7,-4,-10,-3,7,-7,-8,8,8,-7,-7,10,6,-6,-2,-5,-7,-7,10,-3,8,7,-2,9,2,5,-4,7,-4,1,4,-6,-4,5,-2,2,-10,-5,-2,4,-10,-7,1,-4,-9,-2,2,-1,10,-2,-6,-4,5,-1,-4,3,4,-8,-6,-10,7,5,2,10,3,6,-8,8,-10,10,-5], dtype = "int16")#candidate|9232|(512,)|const|int16
call_9231 = relay.TupleGetItem(func_6040_call(relay.reshape(const_9232.astype('int16'), [16, 4, 8]), relay.reshape(const_9232.astype('int16'), [16, 4, 8]), ), 0)
call_9233 = relay.TupleGetItem(func_6043_call(relay.reshape(const_9232.astype('int16'), [16, 4, 8]), relay.reshape(const_9232.astype('int16'), [16, 4, 8]), ), 0)
output = relay.Tuple([call_9210,call_9213,bop_9219,call_9227,call_9231,const_9232,])
output2 = relay.Tuple([call_9211,call_9214,bop_9222,call_9228,call_9233,const_9232,])
func_9241 = relay.Function([], output)
mod['func_9241'] = func_9241
mod = relay.transform.InferType()(mod)
mutated_mod['func_9241'] = func_9241
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9241_call = mutated_mod.get_global_var('func_9241')
call_9242 = func_9241_call()
output = call_9242
func_9243 = relay.Function([], output)
mutated_mod['func_9243'] = func_9243
mutated_mod = relay.transform.InferType()(mutated_mod)
const_9244 = relay.const([[[False,False,False,False,True,False,False,True,True,True,True,True,False,True,True,False],[True,True,False,False,False,False,False,True,True,False,False,False,True,False,False,False]],[[False,True,False,True,True,False,True,False,False,False,False,False,True,True,False,False],[False,True,True,True,True,True,False,False,False,False,False,True,False,True,True,False]],[[False,True,False,True,False,True,False,False,True,False,False,False,True,False,True,True],[True,False,False,False,True,False,True,True,True,True,True,True,False,False,False,False]],[[False,False,False,False,True,False,False,False,False,False,False,True,False,True,False,False],[True,True,False,True,True,True,False,False,True,True,False,True,False,False,False,False]],[[False,False,False,True,False,False,True,False,False,True,True,False,True,True,False,False],[False,True,True,False,False,False,False,True,True,False,True,True,False,True,True,False]],[[True,True,True,True,True,False,True,True,False,False,False,True,True,False,True,False],[True,True,False,False,True,False,True,False,True,False,False,True,True,True,False,False]],[[True,True,True,False,False,False,False,False,False,False,True,False,False,False,False,False],[True,False,False,False,False,True,True,True,False,True,True,True,False,True,False,True]],[[False,True,False,False,False,False,False,False,False,True,False,False,False,False,False,True],[False,False,False,True,False,True,False,False,False,True,True,False,False,True,False,True]],[[True,False,True,True,False,False,True,False,True,False,False,True,False,True,True,True],[True,True,False,True,False,False,True,False,False,True,False,False,False,False,True,True]],[[False,True,False,False,True,False,False,False,False,True,False,False,False,True,True,True],[False,True,True,False,False,False,False,False,True,False,False,False,True,False,True,True]],[[True,False,False,False,False,False,False,False,True,False,False,True,True,False,True,True],[True,False,True,True,False,True,True,False,False,False,False,True,False,True,False,True]]], dtype = "bool")#candidate|9244|(11, 2, 16)|const|bool
var_9245 = relay.var("var_9245", dtype = "bool", shape = (11, 2, 16))#candidate|9245|(11, 2, 16)|var|bool
bop_9246 = relay.logical_or(const_9244.astype('bool'), relay.reshape(var_9245.astype('bool'), relay.shape_of(const_9244))) # shape=(11, 2, 16)
func_8671_call = mod.get_global_var('func_8671')
func_8674_call = mutated_mod.get_global_var('func_8674')
var_9258 = relay.var("var_9258", dtype = "float64", shape = (55, 7))#candidate|9258|(55, 7)|var|float64
call_9257 = relay.TupleGetItem(func_8671_call(relay.reshape(var_9258.astype('float64'), [7, 11, 5])), 0)
call_9259 = relay.TupleGetItem(func_8674_call(relay.reshape(var_9258.astype('float64'), [7, 11, 5])), 0)
output = relay.Tuple([bop_9246,call_9257,var_9258,])
output2 = relay.Tuple([bop_9246,call_9259,var_9258,])
func_9262 = relay.Function([var_9245,var_9258,], output)
mod['func_9262'] = func_9262
mod = relay.transform.InferType()(mod)
var_9263 = relay.var("var_9263", dtype = "bool", shape = (11, 2, 16))#candidate|9263|(11, 2, 16)|var|bool
var_9264 = relay.var("var_9264", dtype = "float64", shape = (55, 7))#candidate|9264|(55, 7)|var|float64
output = func_9262(var_9263,var_9264,)
func_9265 = relay.Function([var_9263,var_9264,], output)
mutated_mod['func_9265'] = func_9265
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2921_call = mod.get_global_var('func_2921')
func_2923_call = mutated_mod.get_global_var('func_2923')
call_9285 = relay.TupleGetItem(func_2921_call(), 0)
call_9286 = relay.TupleGetItem(func_2923_call(), 0)
func_6579_call = mod.get_global_var('func_6579')
func_6581_call = mutated_mod.get_global_var('func_6581')
call_9293 = relay.TupleGetItem(func_6579_call(), 1)
call_9294 = relay.TupleGetItem(func_6581_call(), 1)
func_4250_call = mod.get_global_var('func_4250')
func_4252_call = mutated_mod.get_global_var('func_4252')
call_9297 = func_4250_call()
call_9298 = func_4250_call()
func_5369_call = mod.get_global_var('func_5369')
func_5371_call = mutated_mod.get_global_var('func_5371')
call_9317 = relay.TupleGetItem(func_5369_call(), 1)
call_9318 = relay.TupleGetItem(func_5371_call(), 1)
output = relay.Tuple([call_9285,call_9293,call_9297,call_9317,])
output2 = relay.Tuple([call_9286,call_9294,call_9298,call_9318,])
func_9329 = relay.Function([], output)
mod['func_9329'] = func_9329
mod = relay.transform.InferType()(mod)
mutated_mod['func_9329'] = func_9329
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9329_call = mutated_mod.get_global_var('func_9329')
call_9330 = func_9329_call()
output = call_9330
func_9331 = relay.Function([], output)
mutated_mod['func_9331'] = func_9331
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9332 = relay.var("var_9332", dtype = "uint16", shape = ())#candidate|9332|()|var|uint16
var_9333 = relay.var("var_9333", dtype = "uint16", shape = (1, 15, 14))#candidate|9333|(1, 15, 14)|var|uint16
bop_9334 = relay.greater_equal(var_9332.astype('bool'), var_9333.astype('bool')) # shape=(1, 15, 14)
func_9187_call = mod.get_global_var('func_9187')
func_9189_call = mutated_mod.get_global_var('func_9189')
call_9340 = relay.TupleGetItem(func_9187_call(), 0)
call_9341 = relay.TupleGetItem(func_9189_call(), 0)
output = relay.Tuple([bop_9334,call_9340,])
output2 = relay.Tuple([bop_9334,call_9341,])
func_9348 = relay.Function([var_9332,var_9333,], output)
mod['func_9348'] = func_9348
mod = relay.transform.InferType()(mod)
var_9349 = relay.var("var_9349", dtype = "uint16", shape = ())#candidate|9349|()|var|uint16
var_9350 = relay.var("var_9350", dtype = "uint16", shape = (1, 15, 14))#candidate|9350|(1, 15, 14)|var|uint16
output = func_9348(var_9349,var_9350,)
func_9351 = relay.Function([var_9349,var_9350,], output)
mutated_mod['func_9351'] = func_9351
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4549_call = mod.get_global_var('func_4549')
func_4551_call = mutated_mod.get_global_var('func_4551')
call_9413 = relay.TupleGetItem(func_4549_call(), 0)
call_9414 = relay.TupleGetItem(func_4551_call(), 0)
output = relay.Tuple([call_9413,])
output2 = relay.Tuple([call_9414,])
func_9439 = relay.Function([], output)
mod['func_9439'] = func_9439
mod = relay.transform.InferType()(mod)
mutated_mod['func_9439'] = func_9439
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9439_call = mutated_mod.get_global_var('func_9439')
call_9440 = func_9439_call()
output = call_9440
func_9441 = relay.Function([], output)
mutated_mod['func_9441'] = func_9441
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9187_call = mod.get_global_var('func_9187')
func_9189_call = mutated_mod.get_global_var('func_9189')
call_9447 = relay.TupleGetItem(func_9187_call(), 1)
call_9448 = relay.TupleGetItem(func_9189_call(), 1)
output = relay.Tuple([call_9447,])
output2 = relay.Tuple([call_9448,])
func_9455 = relay.Function([], output)
mod['func_9455'] = func_9455
mod = relay.transform.InferType()(mod)
output = func_9455()
func_9456 = relay.Function([], output)
mutated_mod['func_9456'] = func_9456
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9463 = relay.var("var_9463", dtype = "float32", shape = (12, 10, 12))#candidate|9463|(12, 10, 12)|var|float32
const_9464 = relay.const([[[-2.294487,4.335320,7.479130,6.484069,-4.162137,-0.550405,-9.193652,8.059407,1.772243,2.824270,1.759332,1.395225],[5.824127,2.925916,-0.114999,-3.330690,-7.466106,1.649648,2.373458,4.115490,8.697097,8.484818,-5.696943,-0.780024],[3.956440,9.691642,-1.573889,-2.572322,3.414680,-9.854161,-6.383835,-9.405008,-2.998280,7.871486,8.495107,4.024509],[-7.147224,-5.068953,3.023107,0.317573,5.206595,2.237373,5.405298,6.345494,-4.575401,-9.877120,-9.299255,2.339785],[2.040022,-6.442523,8.122946,6.510734,3.911528,3.917830,2.513649,2.727455,4.269092,-3.770002,-4.236393,4.392494],[9.036859,6.269114,7.525520,-7.602331,6.797919,6.685977,-1.539557,5.897502,-3.441635,-5.696197,1.079749,-2.211262],[-2.016821,5.365068,5.606781,8.341990,3.751330,-5.986451,4.155507,1.244209,-3.846146,-6.827303,9.328168,-9.299748],[-9.792465,7.560733,-2.047782,-3.773506,-7.547060,3.826504,6.528239,-0.612160,5.167722,1.649751,8.619909,-7.645388],[3.763622,-0.763091,-5.002452,-5.979802,0.294259,-5.800355,-8.762662,8.674947,-3.046600,-9.108725,1.139393,-6.397151],[0.927027,-2.227930,-7.805508,-5.334122,0.383589,7.992567,1.310250,-3.681465,2.863705,-8.600197,0.410556,8.634428]],[[-2.576269,4.144728,-1.626116,8.613841,4.040878,3.288106,-9.959702,2.332026,-7.922124,4.923258,7.699465,1.793343],[-1.132086,-1.542510,3.484272,2.931547,6.656038,6.508352,2.901865,0.229032,-9.497571,-6.654451,7.991954,-7.909029],[-0.001827,7.991572,5.980138,9.812484,8.213219,-8.604471,6.657146,-5.073729,-1.220316,-9.343185,-3.596837,6.792031],[-6.443622,0.994425,2.542107,-8.989626,8.660753,6.132721,-4.329016,-9.330936,-2.883407,-7.593579,4.130744,-9.817936],[-5.541931,4.490018,5.060642,-5.427125,-3.564133,9.241758,4.493316,-8.461375,7.526447,-0.841093,-9.259458,4.399538],[9.518050,-3.947895,1.213283,-1.660989,5.819422,-3.870070,-0.920519,1.968748,9.590665,6.505375,-6.156367,8.885976],[1.455478,5.020663,8.508422,6.357234,-2.908308,8.408926,-2.231433,8.017729,2.717662,-2.221609,-1.426239,-9.386563],[-6.842451,4.867218,5.357655,3.062501,-6.241809,-7.390357,6.557150,-9.656266,1.572238,7.551996,7.191244,-2.265522],[2.387661,5.883008,-1.150919,3.204068,9.288409,2.226178,2.030270,9.270881,4.051144,8.796832,6.832080,-5.074791],[3.640408,4.800175,-5.816067,5.500692,-3.609435,-5.348338,8.319963,-4.211505,-3.998104,4.057748,-1.030369,6.982965]],[[0.271279,-5.031793,-7.208540,3.013018,7.260211,-7.020433,-5.218946,0.763103,-6.967906,2.598685,0.654111,-1.886083],[4.613581,6.819796,2.765958,9.674139,-8.491302,8.888329,-7.311229,-2.054897,8.670412,-9.087669,0.114822,0.552235],[0.320372,1.851663,-0.327217,-5.663821,4.387705,2.159640,-0.852531,1.588950,-0.324119,4.573304,-3.005093,-8.897367],[-9.944699,8.935187,-7.433384,-8.079667,-6.046387,-0.651711,1.921888,-5.526007,7.702356,4.425621,7.389260,-5.163120],[-4.439922,-7.742173,1.506386,-1.178891,3.618881,6.648492,-3.599938,6.852613,0.800241,0.253963,-1.111989,-2.450644],[0.271958,4.206169,-8.165868,8.868281,7.655560,1.984733,-1.787139,7.316615,-0.615866,-1.318529,-2.424589,9.123893],[0.032537,-2.854713,-6.584865,0.027694,1.721749,-5.073718,-0.617395,-1.662163,-1.089360,3.463494,5.939015,-3.414197],[3.420264,8.401068,7.368561,-1.878307,8.729748,-7.014893,0.106130,-5.281309,5.700945,-3.481642,-5.982957,6.336079],[2.184670,1.667851,2.807298,-7.293279,-8.431762,-4.200937,-7.338941,9.558475,-0.139123,8.731671,4.214103,-2.596485],[3.136921,1.456602,0.119589,-7.464345,8.918252,8.221094,6.898556,4.135092,0.258259,1.699059,-8.549423,-9.953839]],[[2.922738,-0.411943,2.933880,6.225753,-3.398182,-9.355140,0.790857,-0.678764,-9.660415,-4.001317,8.986948,-1.689253],[7.521827,-5.895515,-7.253703,-3.775966,-6.284243,-9.480704,5.760386,-7.465867,-9.133231,2.517625,1.334002,-4.701469],[-3.886030,-8.103356,3.392705,-7.827362,-5.232577,-9.541370,0.516838,-6.919993,-1.879566,2.107599,-5.293920,5.786407],[-9.825960,7.765993,-3.966171,-5.376843,-3.222164,-2.337104,7.274049,-1.539756,5.207414,-3.244750,-6.153243,-2.637548],[4.062408,-0.910996,-6.797634,6.175683,7.721855,-2.272972,-9.976174,-4.101032,8.935183,-4.305935,1.303588,3.871095],[-7.862932,-0.813465,-7.857716,0.281580,-1.942651,-9.175617,3.532379,-1.712321,-6.633278,-4.258627,7.782831,3.750829],[7.914721,6.331697,-6.968434,6.205833,-8.697164,3.533557,-2.236003,-7.956780,3.886598,5.337318,-5.230649,3.760618],[6.326020,-1.029548,-3.648889,5.151758,8.801319,-6.142749,2.208296,-8.977168,9.839238,3.005513,-5.781291,9.815463],[-4.099136,-0.814326,-5.772171,2.306666,9.282695,-5.623394,0.170495,0.292667,-3.821827,-9.054475,6.513184,8.817078],[4.602395,7.891686,-9.994322,6.448073,6.235875,-0.001592,4.501531,8.101928,2.185742,-0.267331,-0.836845,3.257403]],[[6.948247,-2.795998,1.815693,-3.872333,-8.625455,-2.468294,-1.950299,8.812653,-9.382782,5.818298,6.188010,-3.732926],[-5.046834,0.659096,0.352534,3.930307,3.727013,3.656013,9.698518,3.155663,4.997135,-5.619804,9.885381,-1.560244],[6.613100,5.899694,-9.631678,8.008310,-8.335483,0.315117,-9.537235,-2.071672,7.282664,-5.847505,5.351285,-0.748782],[5.878891,-7.333104,1.007671,-2.865761,-9.674032,2.786360,-5.519137,3.473404,-2.626460,-1.084614,1.842981,-3.783066],[-8.381782,2.476266,-6.673263,1.749933,3.368533,-8.857561,-1.560842,4.523221,-6.967597,0.298783,-6.405706,6.749862],[-4.742765,8.079020,-0.286426,-2.019682,-4.161142,0.139326,3.000916,-0.556321,-6.804200,5.646610,-8.027766,-6.153043],[-3.279980,7.091352,-8.009023,8.028398,-7.230834,6.187386,-5.264732,0.713386,0.659670,1.817432,6.101274,2.743901],[-0.852325,-5.719513,-5.289100,6.221969,8.549894,2.796174,1.910834,-7.982172,1.682445,-6.457049,0.386588,-6.684362],[-5.777501,4.653154,1.731032,-6.518787,-8.216240,-8.949093,9.284336,9.777133,-4.693568,-7.451919,8.957064,4.691813],[-1.831147,-9.719837,-2.604329,4.334339,-1.026190,-5.217510,9.022398,2.325626,-0.870428,-0.722012,9.193303,-3.697493]],[[-2.586063,2.462101,3.012099,-2.832612,-6.307621,3.917466,6.892060,-2.462766,1.252747,-2.377097,1.264127,-0.150555],[8.795892,1.967146,-5.972302,5.461458,-8.376466,-2.055498,9.447946,-5.065046,9.612312,-9.343243,-9.095048,-6.584906],[-7.727392,-5.030434,-0.188245,9.333821,-4.513652,-2.125605,-4.931760,7.282055,-6.664937,-0.395998,9.588113,-6.884528],[-5.635982,0.993029,3.587506,-9.097041,-7.791999,5.909682,-1.199153,3.712692,1.995686,4.273819,5.164839,-1.437461],[8.256505,2.365808,0.063349,9.002623,3.639261,-9.451935,5.768011,-4.230405,-4.088413,-4.268695,-7.955505,9.867682],[-1.537057,5.446617,3.170757,6.548003,-2.515655,6.161982,-7.129920,5.557702,-6.535333,-3.629731,-3.923610,0.778505],[-8.306697,4.612178,8.953601,-6.576710,-0.737572,4.063041,-8.587541,-3.000090,-1.378811,-4.532958,-1.582203,-2.148240],[-9.010227,-1.672099,6.591458,9.774923,-6.763576,-0.198975,6.688168,3.655197,-2.311589,2.023301,7.715577,8.031733],[-8.609136,6.165482,2.205584,5.262955,-2.837694,-5.527910,9.427074,-4.012327,9.524332,-1.331748,2.384208,-0.184953],[-2.073558,-1.127926,6.386842,4.768026,-5.481942,-0.187977,-3.946896,8.430880,-3.824432,-7.226585,8.650214,2.033808]],[[5.619677,2.744526,5.195616,-6.480082,2.264868,1.743916,-7.341259,-9.086350,3.804314,-1.098373,-0.520631,8.652898],[-8.846933,2.851897,-4.462590,-6.700908,-7.511488,-7.216660,0.152706,5.931017,-4.778766,8.667626,-2.573697,6.710605],[-9.132500,5.809410,1.715395,3.860785,6.665544,0.542894,3.797810,0.209195,6.226183,9.270781,5.810506,3.303725],[-1.232035,-0.754113,1.749481,-3.181278,-8.590031,-6.462600,-2.000511,4.014743,-5.559733,8.498928,-9.540199,8.666193],[7.915440,-5.480623,-4.921723,-9.182423,-2.070325,3.862970,-1.140437,2.266359,9.887690,-8.589595,-2.050161,9.963027],[-3.514628,-6.186115,-1.915683,-1.372269,0.873807,-2.581662,-2.784833,-7.915504,7.230463,-5.654253,1.647314,-3.656839],[-9.657957,7.160773,-8.061496,4.310786,2.474591,4.571294,-1.066028,2.914908,-3.712468,0.494521,-1.575687,9.468780],[4.873099,6.399608,-1.664299,0.522703,-6.671126,9.802489,-9.041005,2.387794,-5.303740,2.471637,-9.525158,-9.064540],[-5.287339,-8.326404,7.251315,-6.016861,2.438109,-7.337226,-9.042938,-1.834970,-8.649857,4.350115,7.101894,-7.448614],[-7.999658,-6.933122,5.693976,0.720636,-6.772532,-3.978476,-8.855314,-3.618433,4.417426,0.225517,-6.290433,-2.983059]],[[4.387340,2.246518,0.270950,-7.781362,6.586620,-8.477875,-7.498386,-7.229565,3.856683,-6.870228,-6.936772,-2.313463],[2.135705,9.904519,3.035640,-6.298399,0.857028,1.850330,-6.109557,-5.976052,-7.798620,-9.305525,1.103575,6.861701],[8.413407,-3.135442,-4.379018,6.817493,-5.473189,-9.469263,4.186020,-6.665736,-9.790067,9.357939,1.049538,5.760716],[-8.965901,-0.238501,-5.432372,4.689179,-2.719020,6.088913,-5.942929,-6.549953,7.333469,-5.089012,-7.349557,-9.259415],[0.245808,8.534944,2.534580,-6.203798,-3.939420,8.420168,8.993634,-2.893947,-3.842441,-2.347159,8.300435,0.353411],[8.712586,0.337962,-4.433606,2.645841,3.150685,5.707538,4.825450,-9.396870,-3.576795,-2.007407,-9.107989,4.726061],[0.816021,7.424792,7.640666,7.090028,6.640858,-4.893686,-0.245332,9.003522,-2.877192,3.569715,-8.290587,4.206382],[5.905038,-4.588093,-4.425899,5.280384,-8.391597,-6.258664,9.143494,-4.707282,-8.518743,8.866588,-3.430498,-3.130740],[6.716476,-2.655309,-5.079158,-1.240486,-0.684188,1.473989,3.873364,-6.306812,-3.617341,4.322717,-4.244745,-9.862739],[-8.597666,-5.393999,-3.026595,5.455510,-3.179805,1.085440,9.941010,-1.566508,6.463709,-6.729823,-8.602974,-2.147710]],[[-6.813845,0.951251,0.531972,7.911294,6.816548,4.849374,9.037363,6.153089,-8.813799,-6.997230,-1.621933,1.520751],[-3.881813,-4.483032,-6.505688,0.822510,-5.401175,-2.100266,-9.274302,7.096467,1.827563,1.307812,4.250472,-0.644331],[-7.220412,9.967590,8.640150,-7.997949,5.895011,7.739435,3.839084,-6.015679,0.530582,0.024989,-3.808838,9.881378],[0.985233,-8.876014,3.689517,6.366624,9.655313,-5.312058,1.074736,0.582425,-5.641524,3.636104,7.626550,2.044034],[-4.192531,2.495043,-8.619177,-8.364368,4.072003,-0.846971,8.038052,-8.084839,8.620203,5.047290,4.038271,5.156227],[3.436662,4.835593,-8.246629,3.314236,-3.003092,5.747611,6.034473,-4.159851,3.655752,0.211639,-9.966721,0.888709],[7.270574,5.667939,2.070245,-0.213858,6.685556,-6.139368,-4.751845,-1.998830,-5.661674,2.582012,1.335682,-5.072198],[7.957599,6.906836,-3.700662,7.422118,1.320309,-9.469233,2.578306,-3.197145,2.367888,-6.111013,-0.587021,-8.357676],[-2.171815,3.890233,7.579328,-8.424159,7.005150,1.323355,6.232115,8.092948,9.176696,0.683892,-1.385708,9.612159],[-3.891511,-4.942669,-7.240551,3.382815,-9.826594,-7.886025,9.092928,-6.375995,-5.853555,-7.389710,-5.930128,-3.388704]],[[5.265716,-7.464137,7.028552,6.238377,3.425751,3.724063,-4.974149,7.142162,5.329496,1.976277,-4.169639,7.828877],[1.022321,-4.460240,-3.725374,5.526347,4.389361,5.467495,6.711733,-0.946733,-9.689679,-4.031001,2.207924,-1.506710],[0.755326,6.543496,3.928243,-7.857205,-9.664376,8.204206,7.811379,-9.244931,-0.540600,-2.856893,7.230804,6.206102],[-6.884727,-1.193966,6.083883,-8.941461,-5.661255,-8.635460,-0.175573,-1.649322,-8.621079,6.699062,-4.343618,-2.806434],[-5.279548,-1.625425,5.644459,0.617247,8.706881,4.196581,-8.375047,1.329455,2.722003,0.618607,-9.902247,-7.369511],[1.051081,5.401560,-2.536088,-8.146206,-2.193759,-1.426916,-4.688337,9.784133,5.277233,-4.333992,-3.221985,9.060542],[-9.200817,8.380446,-1.723066,6.671937,-3.137253,-4.426339,-8.997485,9.938787,6.173514,-8.516996,9.698284,-9.074068],[0.724951,5.445995,-1.160459,4.400339,8.721361,-3.875243,2.872640,9.811810,-7.829717,-3.711678,-2.862394,9.923558],[2.855314,-2.304385,4.228570,7.965052,2.929397,-6.975538,0.536929,-7.633550,-5.606129,1.871729,-3.596159,0.428825],[-2.123074,5.300314,4.314987,-5.416783,4.311216,-2.783785,0.390802,9.885490,-1.430689,7.464920,2.139041,-8.106056]],[[-0.540032,9.943862,-9.601728,6.299966,-7.026152,6.817735,6.859078,-0.550157,-9.704226,0.998096,8.955058,9.098339],[-6.422687,4.890105,-0.499728,2.235850,9.432520,-7.554505,-1.636370,-0.106430,-4.460354,-7.641787,-4.151088,-3.588669],[0.296742,-0.712724,-2.702499,-5.198827,-4.176340,3.398321,8.066145,3.068239,7.741992,-8.560614,0.151343,5.670436],[3.447021,8.129551,-8.720744,-1.773814,3.797018,-7.534269,-2.109740,-0.333715,3.562289,-7.612231,4.868352,2.566542],[4.758570,-7.609110,7.951484,-1.335981,4.092084,-7.656062,-2.274085,-2.253670,8.969100,7.539759,2.121755,3.855970],[7.817126,-9.389671,4.454717,-2.627136,4.887265,-1.374231,-6.258023,2.323399,-8.814435,0.646036,0.815301,2.538572],[4.688832,-7.692032,-1.252594,9.111287,8.782038,-3.772139,8.856354,3.748019,9.834393,4.117700,0.135489,-5.925999],[-2.004077,-1.707316,4.617962,0.325148,-0.385223,9.575500,0.186868,8.052527,-5.928509,6.006763,-0.861599,2.317209],[-0.418042,1.600515,3.175291,-2.316776,1.065373,4.409472,-2.291419,0.403865,4.597419,5.873834,4.070396,2.407107],[7.567170,-4.579782,-6.836672,8.514771,-2.095377,-4.066950,-7.691332,-7.647879,1.992598,-6.362099,-6.803732,-7.725015]],[[8.149113,-7.115028,-8.608189,-2.671701,-5.166468,9.995570,-3.175284,-7.209722,6.745290,1.819559,0.521643,-5.983828],[9.239262,-9.104302,-4.765592,4.190068,-7.247100,7.837681,-3.509102,-0.642240,-8.515927,3.296321,4.677530,5.733578],[-9.601067,-3.442597,-6.088847,-8.720096,-0.289735,4.225184,5.014524,-7.922972,-7.251722,6.935676,5.254003,-6.840717],[0.584340,3.411219,1.751669,-3.627150,4.335799,9.822222,4.002321,5.263230,-7.386065,-5.539151,-5.398630,4.187083],[-2.608765,8.428531,9.316982,3.450391,7.193204,6.452953,-0.811536,-2.258555,-7.143874,3.418517,3.695155,8.324076],[-2.627883,4.163897,-4.795672,3.741547,2.947837,2.150745,-4.439844,-7.924476,0.735525,-3.885314,9.570794,9.779259],[-7.328661,0.421752,0.260665,1.896150,-5.951828,-6.904336,-0.676010,-9.358554,-2.911808,-1.379587,-0.949526,-3.264247],[-9.714667,6.914433,9.845156,1.961523,-5.681062,3.421535,-2.110705,6.200178,-8.872735,7.616768,9.647677,-0.089212],[7.411399,2.797953,3.715772,9.298510,-4.226607,6.422450,7.849916,-3.165821,0.930460,-5.169580,-9.234601,2.088875],[3.069040,2.545695,-8.751900,1.047288,-7.683273,6.392850,-1.022317,9.707125,-9.281937,1.991080,-1.846909,1.322161]]], dtype = "float32")#candidate|9464|(12, 10, 12)|const|float32
bop_9465 = relay.floor_mod(var_9463.astype('float32'), relay.reshape(const_9464.astype('float32'), relay.shape_of(var_9463))) # shape=(12, 10, 12)
func_3650_call = mod.get_global_var('func_3650')
func_3652_call = mutated_mod.get_global_var('func_3652')
const_9470 = relay.const([[1.100804],[8.977158],[4.847774],[-9.849158],[2.620818],[-1.073806],[1.778876],[6.060459],[-0.482513],[-3.779053],[-8.647729],[-9.269384],[1.625175],[3.977702],[-8.360963],[-1.061400],[-9.513756],[-6.945703],[0.401988],[-7.787830],[-7.197153],[2.180983],[-3.235419],[-8.803592],[1.985397],[-7.995507],[4.687117],[-3.019840],[0.393572],[-1.845624],[-9.109969],[2.416040],[-9.855810],[-8.068494],[-8.451712],[6.882036],[8.246227],[-8.884007],[5.163639],[-6.673107],[4.813112],[5.787130],[-1.477486],[-8.634736],[5.890162],[2.609409],[2.014668],[-5.310104],[-8.755982],[9.701000],[8.889073],[5.425180],[3.391828],[-4.212282],[-7.935867],[4.574125],[5.571260],[-1.509243],[6.583037],[3.975677],[-5.519438],[-2.950519],[4.894902],[4.098475],[0.262804],[-3.565785],[2.650085],[2.036231],[-7.059816],[-4.415609],[-1.993890],[-1.578826],[-5.918109],[6.401253],[3.465900],[-7.585323],[6.387617],[1.092488],[4.964790],[-6.068287],[1.176820],[9.043090],[4.466353],[5.241431],[-0.570175],[-8.830385],[-9.658150],[-1.445056],[-1.549178],[-8.155777],[7.651375],[5.362619],[8.065931],[5.457063],[9.922571],[5.638528],[8.551830],[-8.578056],[6.353675],[-5.347070],[4.177813],[-5.268096],[2.639036],[-0.603323],[4.657966],[-2.503601],[8.842918],[1.019221],[-4.867657],[1.745035],[4.561130],[5.542990],[8.376877],[0.688905],[2.653179],[-7.009391],[-1.975161],[-6.823019],[8.193420],[6.944909],[5.033155],[7.556572],[8.236212],[4.838805],[-3.646153],[-5.535008],[7.126338],[-6.848542],[4.750991],[9.927780],[6.182393],[0.902983],[2.471653],[5.301927],[-1.007650],[9.631897],[-0.191508],[-5.739721],[2.094045],[-3.330193],[-4.217087],[5.148461],[-4.511644],[-5.757316],[9.433541],[-9.677850],[2.988054],[1.442175],[-3.268236],[2.404001],[5.511190],[-1.167417],[-8.238485],[-6.035125],[2.939494],[3.727262],[3.648186],[3.354903],[-3.006375],[9.088578],[-1.004962],[-5.972759],[8.746681],[-7.502686],[-8.572108],[-1.481608],[-0.329755],[-5.089591],[3.476504],[-6.464497],[5.304315],[-0.393022],[7.326078],[-1.076539],[5.412909],[0.396551],[8.862630],[4.810153],[9.085334],[-4.539581],[7.715896],[-2.224692],[-8.524724],[-8.415809],[0.598252],[-1.243067],[-5.825031],[5.308345],[-8.494629],[9.139377],[2.431092],[3.919608],[-3.586134],[6.022450],[-8.225045],[-7.816041],[-9.686798],[8.544289],[0.056486],[-3.414377],[8.194667],[6.153088],[5.738121],[4.917164],[-8.250781],[6.496255],[9.697391],[-2.894646],[0.328115],[-1.004440],[-6.582542],[1.781378],[9.984047],[3.757790],[0.724287],[7.878557],[-8.906379],[-0.629275],[5.503003],[1.096383],[9.565535],[7.919210],[-0.366913],[-9.749206],[6.292210],[3.150354],[9.288798],[-4.731032],[-2.272039],[0.913618],[6.693095],[-0.987708],[6.705952],[2.836922],[-3.045239],[-6.235528],[5.837788],[-8.140877],[-9.020730],[5.219953],[9.876334],[0.220377],[2.611903],[6.165208],[6.952836],[8.223684],[0.223618],[-7.527029],[4.740438],[4.458489],[-0.142993],[4.302041],[4.003463],[1.840576],[-2.231962],[8.021314],[-8.133731],[1.618488],[-5.969597],[2.951839],[5.536153],[-4.557619],[-1.192907],[-7.338222],[-4.805883],[8.027445],[0.645647],[-4.907485],[-8.712119],[-2.458140],[-2.550803],[7.863257],[-9.422033],[9.293349],[4.742920],[-2.323376],[9.186015],[-3.085506],[9.602636],[4.496982],[-1.171111],[1.060227],[2.932832],[5.842163],[4.466463],[7.036005],[2.875347],[-0.106953]], dtype = "float32")#candidate|9470|(288, 1)|const|float32
call_9469 = relay.TupleGetItem(func_3650_call(relay.reshape(const_9470.astype('float32'), [288,])), 3)
call_9471 = relay.TupleGetItem(func_3652_call(relay.reshape(const_9470.astype('float32'), [288,])), 3)
uop_9477 = relay.sin(var_9463.astype('float32')) # shape=(12, 10, 12)
output = relay.Tuple([bop_9465,call_9469,const_9470,uop_9477,])
output2 = relay.Tuple([bop_9465,call_9471,const_9470,uop_9477,])
func_9482 = relay.Function([var_9463,], output)
mod['func_9482'] = func_9482
mod = relay.transform.InferType()(mod)
var_9483 = relay.var("var_9483", dtype = "float32", shape = (12, 10, 12))#candidate|9483|(12, 10, 12)|var|float32
output = func_9482(var_9483)
func_9484 = relay.Function([var_9483], output)
mutated_mod['func_9484'] = func_9484
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7224_call = mod.get_global_var('func_7224')
func_7226_call = mutated_mod.get_global_var('func_7226')
call_9492 = relay.TupleGetItem(func_7224_call(), 0)
call_9493 = relay.TupleGetItem(func_7226_call(), 0)
output = relay.Tuple([call_9492,])
output2 = relay.Tuple([call_9493,])
func_9504 = relay.Function([], output)
mod['func_9504'] = func_9504
mod = relay.transform.InferType()(mod)
mutated_mod['func_9504'] = func_9504
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9504_call = mutated_mod.get_global_var('func_9504')
call_9505 = func_9504_call()
output = call_9505
func_9506 = relay.Function([], output)
mutated_mod['func_9506'] = func_9506
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5711_call = mod.get_global_var('func_5711')
func_5713_call = mutated_mod.get_global_var('func_5713')
call_9522 = func_5711_call()
call_9523 = func_5711_call()
func_3483_call = mod.get_global_var('func_3483')
func_3485_call = mutated_mod.get_global_var('func_3485')
call_9527 = relay.TupleGetItem(func_3483_call(), 0)
call_9528 = relay.TupleGetItem(func_3485_call(), 0)
output = relay.Tuple([call_9522,call_9527,])
output2 = relay.Tuple([call_9523,call_9528,])
func_9531 = relay.Function([], output)
mod['func_9531'] = func_9531
mod = relay.transform.InferType()(mod)
mutated_mod['func_9531'] = func_9531
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9531_call = mutated_mod.get_global_var('func_9531')
call_9532 = func_9531_call()
output = call_9532
func_9533 = relay.Function([], output)
mutated_mod['func_9533'] = func_9533
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6196_call = mod.get_global_var('func_6196')
func_6197_call = mutated_mod.get_global_var('func_6197')
call_9564 = relay.TupleGetItem(func_6196_call(), 0)
call_9565 = relay.TupleGetItem(func_6197_call(), 0)
output = relay.Tuple([call_9564,])
output2 = relay.Tuple([call_9565,])
func_9566 = relay.Function([], output)
mod['func_9566'] = func_9566
mod = relay.transform.InferType()(mod)
mutated_mod['func_9566'] = func_9566
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9566_call = mutated_mod.get_global_var('func_9566')
call_9567 = func_9566_call()
output = call_9567
func_9568 = relay.Function([], output)
mutated_mod['func_9568'] = func_9568
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7107_call = mod.get_global_var('func_7107')
func_7109_call = mutated_mod.get_global_var('func_7109')
call_9585 = relay.TupleGetItem(func_7107_call(), 3)
call_9586 = relay.TupleGetItem(func_7109_call(), 3)
func_2623_call = mod.get_global_var('func_2623')
func_2626_call = mutated_mod.get_global_var('func_2626')
var_9619 = relay.var("var_9619", dtype = "float32", shape = (4, 72))#candidate|9619|(4, 72)|var|float32
call_9618 = relay.TupleGetItem(func_2623_call(relay.reshape(var_9619.astype('float32'), [288,])), 2)
call_9620 = relay.TupleGetItem(func_2626_call(relay.reshape(var_9619.astype('float32'), [288,])), 2)
bop_9627 = relay.power(var_9619.astype('float64'), relay.reshape(call_9618.astype('float64'), relay.shape_of(var_9619))) # shape=(4, 72)
bop_9630 = relay.power(var_9619.astype('float64'), relay.reshape(call_9620.astype('float64'), relay.shape_of(var_9619))) # shape=(4, 72)
output = relay.Tuple([call_9585,bop_9627,])
output2 = relay.Tuple([call_9586,bop_9630,])
func_9648 = relay.Function([var_9619,], output)
mod['func_9648'] = func_9648
mod = relay.transform.InferType()(mod)
var_9649 = relay.var("var_9649", dtype = "float32", shape = (4, 72))#candidate|9649|(4, 72)|var|float32
output = func_9648(var_9649)
func_9650 = relay.Function([var_9649], output)
mutated_mod['func_9650'] = func_9650
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6643_call = mod.get_global_var('func_6643')
func_6645_call = mutated_mod.get_global_var('func_6645')
call_9688 = relay.TupleGetItem(func_6643_call(), 4)
call_9689 = relay.TupleGetItem(func_6645_call(), 4)
uop_9690 = relay.sqrt(call_9688.astype('float32')) # shape=(18, 60)
uop_9692 = relay.sqrt(call_9689.astype('float32')) # shape=(18, 60)
uop_9696 = relay.cosh(uop_9690.astype('float64')) # shape=(18, 60)
uop_9698 = relay.cosh(uop_9692.astype('float64')) # shape=(18, 60)
func_8540_call = mod.get_global_var('func_8540')
func_8542_call = mutated_mod.get_global_var('func_8542')
call_9700 = relay.TupleGetItem(func_8540_call(), 2)
call_9701 = relay.TupleGetItem(func_8542_call(), 2)
output = relay.Tuple([uop_9696,call_9700,])
output2 = relay.Tuple([uop_9698,call_9701,])
func_9707 = relay.Function([], output)
mod['func_9707'] = func_9707
mod = relay.transform.InferType()(mod)
mutated_mod['func_9707'] = func_9707
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9707_call = mutated_mod.get_global_var('func_9707')
call_9708 = func_9707_call()
output = call_9708
func_9709 = relay.Function([], output)
mutated_mod['func_9709'] = func_9709
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9753 = relay.var("var_9753", dtype = "uint64", shape = (14, 12, 9))#candidate|9753|(14, 12, 9)|var|uint64
var_9754 = relay.var("var_9754", dtype = "uint64", shape = (14, 12, 9))#candidate|9754|(14, 12, 9)|var|uint64
bop_9755 = relay.equal(var_9753.astype('bool'), relay.reshape(var_9754.astype('bool'), relay.shape_of(var_9753))) # shape=(14, 12, 9)
output = bop_9755
output2 = bop_9755
func_9759 = relay.Function([var_9753,var_9754,], output)
mod['func_9759'] = func_9759
mod = relay.transform.InferType()(mod)
var_9760 = relay.var("var_9760", dtype = "uint64", shape = (14, 12, 9))#candidate|9760|(14, 12, 9)|var|uint64
var_9761 = relay.var("var_9761", dtype = "uint64", shape = (14, 12, 9))#candidate|9761|(14, 12, 9)|var|uint64
output = func_9759(var_9760,var_9761,)
func_9762 = relay.Function([var_9760,var_9761,], output)
mutated_mod['func_9762'] = func_9762
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5989_call = mod.get_global_var('func_5989')
func_5991_call = mutated_mod.get_global_var('func_5991')
call_9784 = func_5989_call()
call_9785 = func_5989_call()
func_4917_call = mod.get_global_var('func_4917')
func_4919_call = mutated_mod.get_global_var('func_4919')
call_9790 = relay.TupleGetItem(func_4917_call(), 0)
call_9791 = relay.TupleGetItem(func_4919_call(), 0)
func_9504_call = mod.get_global_var('func_9504')
func_9506_call = mutated_mod.get_global_var('func_9506')
call_9816 = relay.TupleGetItem(func_9504_call(), 0)
call_9817 = relay.TupleGetItem(func_9506_call(), 0)
output = relay.Tuple([call_9784,call_9790,call_9816,])
output2 = relay.Tuple([call_9785,call_9791,call_9817,])
func_9823 = relay.Function([], output)
mod['func_9823'] = func_9823
mod = relay.transform.InferType()(mod)
output = func_9823()
func_9824 = relay.Function([], output)
mutated_mod['func_9824'] = func_9824
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9531_call = mod.get_global_var('func_9531')
func_9533_call = mutated_mod.get_global_var('func_9533')
call_9873 = relay.TupleGetItem(func_9531_call(), 1)
call_9874 = relay.TupleGetItem(func_9533_call(), 1)
output = relay.Tuple([call_9873,])
output2 = relay.Tuple([call_9874,])
func_9930 = relay.Function([], output)
mod['func_9930'] = func_9930
mod = relay.transform.InferType()(mod)
mutated_mod['func_9930'] = func_9930
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9930_call = mutated_mod.get_global_var('func_9930')
call_9931 = func_9930_call()
output = call_9931
func_9932 = relay.Function([], output)
mutated_mod['func_9932'] = func_9932
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2921_call = mod.get_global_var('func_2921')
func_2923_call = mutated_mod.get_global_var('func_2923')
call_9936 = relay.TupleGetItem(func_2921_call(), 0)
call_9937 = relay.TupleGetItem(func_2923_call(), 0)
func_5170_call = mod.get_global_var('func_5170')
func_5172_call = mutated_mod.get_global_var('func_5172')
call_9958 = func_5170_call()
call_9959 = func_5170_call()
func_5914_call = mod.get_global_var('func_5914')
func_5918_call = mutated_mod.get_global_var('func_5918')
const_9963 = relay.const([4.078187,7.889191,7.515033,-7.471506,-2.803596,5.796171,-6.863158,7.437085,5.903234,8.392805,-4.514251,-2.727462,8.632025,8.418094,-1.519403,-2.261614,-7.852734,1.034047,-9.132590,-1.335908,-0.637698,7.928682,1.348810,-3.883044,-0.200420,-9.799544,-5.270928,-8.048942,5.372717,9.328496,-6.495216,-9.265977,2.171084,-9.156789,5.881412,-2.149498,-9.458897,-5.317104,-3.834815,-4.928595,8.619823,3.135624,4.766292,0.977581,-1.423885,3.616718,-8.823803,6.603668,5.085953,6.027763,-7.736410,-6.001694,1.640185,-3.546395,1.928610,-6.090690,-3.046526,-7.128740,1.300935,-4.545787,-3.569242,5.225119,3.642753,3.568267,-3.353707,-6.740040,-5.841971,-4.335597,2.950012,-8.667249,7.633759,9.487416,-4.829041,-0.238377,7.072323,2.659355,-6.500825,5.862382,0.081146,-8.178352,5.566395,-5.357285,9.799160,-1.238709,-6.024069,2.666798,0.708401,5.291798,-8.081278,-0.510841,-4.217466,-7.643735,-5.601625,9.843169,-3.051617,5.162122,-1.767641,3.179979,-2.915004,-1.112741,-6.685337,2.031592,2.784220,-8.204294,-7.823012,1.164651,-8.750725,1.036231,2.492626,7.426773,-5.488672,-1.915868,-6.386265,-7.976748,7.203771,3.821214,-9.086719,7.839605,8.585097,3.331469,-2.564575,8.162083,-0.399574,1.497470,4.045129,5.585978,-1.915440,-6.015005,-5.466433,3.294637,2.776726,8.327913,5.350938,8.574534,-9.539601,-2.924217,-8.219992,-6.749652,-8.689400,-1.341023,-2.117144,7.643437,7.615303,2.109429,-3.953755,2.970045,-3.249323,2.095736,-1.749574,-4.786427,-9.595081,5.493832,-2.832921,3.831488,-8.933570,-3.654257,-6.873799,2.928404,0.451716,5.871977,4.285698,-6.831796,2.666912,-8.944720,-9.904390,9.210946,0.964132,9.192609,-8.256579,7.601078,3.847771,0.882483,9.562108,7.740549,6.733064,3.358559,-7.896676,-7.460036,9.610147,8.027714,-5.011959,-8.704231,4.316401,9.439503,4.773831,-1.780929,5.525837,-1.266017,-9.375733,7.649973,-8.198120,2.418309,-8.783171,-5.607170,-6.936650,-6.695272,-0.232208,-3.036873,-3.556094,7.944810,-7.650579,-6.804067,1.151862,3.361176,6.642144,-0.939157,3.374985,-6.466132,6.243831,1.471412,-5.230434,-4.891293,0.887720,-2.947881,3.387381,3.093188,-6.438074,1.664469,-2.528994,4.355506], dtype = "float32")#candidate|9963|(220,)|const|float32
call_9962 = relay.TupleGetItem(func_5914_call(relay.reshape(const_9963.astype('float32'), [11, 2, 10]), relay.reshape(const_9963.astype('float32'), [11, 2, 10]), ), 0)
call_9964 = relay.TupleGetItem(func_5918_call(relay.reshape(const_9963.astype('float32'), [11, 2, 10]), relay.reshape(const_9963.astype('float32'), [11, 2, 10]), ), 0)
func_4310_call = mod.get_global_var('func_4310')
func_4313_call = mutated_mod.get_global_var('func_4313')
call_9978 = relay.TupleGetItem(func_4310_call(relay.reshape(call_9936.astype('float32'), [288,])), 2)
call_9979 = relay.TupleGetItem(func_4313_call(relay.reshape(call_9936.astype('float32'), [288,])), 2)
output = relay.Tuple([call_9936,call_9958,call_9962,const_9963,call_9978,])
output2 = relay.Tuple([call_9937,call_9959,call_9964,const_9963,call_9979,])
func_9983 = relay.Function([], output)
mod['func_9983'] = func_9983
mod = relay.transform.InferType()(mod)
output = func_9983()
func_9984 = relay.Function([], output)
mutated_mod['func_9984'] = func_9984
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7966_call = mod.get_global_var('func_7966')
func_7968_call = mutated_mod.get_global_var('func_7968')
call_10003 = relay.TupleGetItem(func_7966_call(), 0)
call_10004 = relay.TupleGetItem(func_7968_call(), 0)
uop_10012 = relay.asinh(call_10003.astype('float64')) # shape=(7, 11, 5)
uop_10014 = relay.asinh(call_10004.astype('float64')) # shape=(7, 11, 5)
bop_10024 = relay.logical_or(uop_10012.astype('bool'), relay.reshape(call_10003.astype('bool'), relay.shape_of(uop_10012))) # shape=(7, 11, 5)
bop_10027 = relay.logical_or(uop_10014.astype('bool'), relay.reshape(call_10004.astype('bool'), relay.shape_of(uop_10014))) # shape=(7, 11, 5)
func_7636_call = mod.get_global_var('func_7636')
func_7638_call = mutated_mod.get_global_var('func_7638')
call_10028 = relay.TupleGetItem(func_7636_call(), 0)
call_10029 = relay.TupleGetItem(func_7638_call(), 0)
output = relay.Tuple([bop_10024,call_10028,])
output2 = relay.Tuple([bop_10027,call_10029,])
func_10030 = relay.Function([], output)
mod['func_10030'] = func_10030
mod = relay.transform.InferType()(mod)
output = func_10030()
func_10031 = relay.Function([], output)
mutated_mod['func_10031'] = func_10031
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6300_call = mod.get_global_var('func_6300')
func_6302_call = mutated_mod.get_global_var('func_6302')
call_10076 = relay.TupleGetItem(func_6300_call(), 0)
call_10077 = relay.TupleGetItem(func_6302_call(), 0)
output = call_10076
output2 = call_10077
func_10078 = relay.Function([], output)
mod['func_10078'] = func_10078
mod = relay.transform.InferType()(mod)
mutated_mod['func_10078'] = func_10078
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10078_call = mutated_mod.get_global_var('func_10078')
call_10079 = func_10078_call()
output = call_10079
func_10080 = relay.Function([], output)
mutated_mod['func_10080'] = func_10080
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8642_call = mod.get_global_var('func_8642')
func_8644_call = mutated_mod.get_global_var('func_8644')
call_10089 = relay.TupleGetItem(func_8642_call(), 0)
call_10090 = relay.TupleGetItem(func_8644_call(), 0)
output = relay.Tuple([call_10089,])
output2 = relay.Tuple([call_10090,])
func_10102 = relay.Function([], output)
mod['func_10102'] = func_10102
mod = relay.transform.InferType()(mod)
output = func_10102()
func_10103 = relay.Function([], output)
mutated_mod['func_10103'] = func_10103
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7107_call = mod.get_global_var('func_7107')
func_7109_call = mutated_mod.get_global_var('func_7109')
call_10141 = relay.TupleGetItem(func_7107_call(), 3)
call_10142 = relay.TupleGetItem(func_7109_call(), 3)
func_568_call = mod.get_global_var('func_568')
func_572_call = mutated_mod.get_global_var('func_572')
var_10155 = relay.var("var_10155", dtype = "float64", shape = (315,))#candidate|10155|(315,)|var|float64
call_10154 = relay.TupleGetItem(func_568_call(relay.reshape(var_10155.astype('float64'), [3, 7, 15]), relay.reshape(var_10155.astype('float64'), [3, 7, 15]), ), 2)
call_10156 = relay.TupleGetItem(func_572_call(relay.reshape(var_10155.astype('float64'), [3, 7, 15]), relay.reshape(var_10155.astype('float64'), [3, 7, 15]), ), 2)
var_10174 = relay.var("var_10174", dtype = "bool", shape = (5, 585))#candidate|10174|(5, 585)|var|bool
bop_10175 = relay.greater(call_10154.astype('bool'), relay.reshape(var_10174.astype('bool'), relay.shape_of(call_10154))) # shape=(5, 585)
bop_10178 = relay.greater(call_10156.astype('bool'), relay.reshape(var_10174.astype('bool'), relay.shape_of(call_10156))) # shape=(5, 585)
func_8835_call = mod.get_global_var('func_8835')
func_8840_call = mutated_mod.get_global_var('func_8840')
var_10180 = relay.var("var_10180", dtype = "uint64", shape = ())#candidate|10180|()|var|uint64
var_10181 = relay.var("var_10181", dtype = "uint64", shape = (320, 4))#candidate|10181|(320, 4)|var|uint64
var_10182 = relay.var("var_10182", dtype = "int64", shape = (90, 12))#candidate|10182|(90, 12)|var|int64
call_10179 = relay.TupleGetItem(func_8835_call(relay.reshape(call_10141.astype('float32'), [468,]), relay.reshape(var_10180.astype('uint64'), []), relay.reshape(var_10181.astype('uint64'), [2, 640]), relay.reshape(var_10182.astype('int64'), [1080,]), ), 0)
call_10183 = relay.TupleGetItem(func_8840_call(relay.reshape(call_10141.astype('float32'), [468,]), relay.reshape(var_10180.astype('uint64'), []), relay.reshape(var_10181.astype('uint64'), [2, 640]), relay.reshape(var_10182.astype('int64'), [1080,]), ), 0)
output = relay.Tuple([call_10141,var_10155,bop_10175,call_10179,var_10180,var_10181,var_10182,])
output2 = relay.Tuple([call_10142,var_10155,bop_10178,call_10183,var_10180,var_10181,var_10182,])
func_10190 = relay.Function([var_10155,var_10174,var_10180,var_10181,var_10182,], output)
mod['func_10190'] = func_10190
mod = relay.transform.InferType()(mod)
var_10191 = relay.var("var_10191", dtype = "float64", shape = (315,))#candidate|10191|(315,)|var|float64
var_10192 = relay.var("var_10192", dtype = "bool", shape = (5, 585))#candidate|10192|(5, 585)|var|bool
var_10193 = relay.var("var_10193", dtype = "uint64", shape = ())#candidate|10193|()|var|uint64
var_10194 = relay.var("var_10194", dtype = "uint64", shape = (320, 4))#candidate|10194|(320, 4)|var|uint64
var_10195 = relay.var("var_10195", dtype = "int64", shape = (90, 12))#candidate|10195|(90, 12)|var|int64
output = func_10190(var_10191,var_10192,var_10193,var_10194,var_10195,)
func_10196 = relay.Function([var_10191,var_10192,var_10193,var_10194,var_10195,], output)
mutated_mod['func_10196'] = func_10196
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4773_call = mod.get_global_var('func_4773')
func_4775_call = mutated_mod.get_global_var('func_4775')
call_10252 = func_4773_call()
call_10253 = func_4773_call()
func_2921_call = mod.get_global_var('func_2921')
func_2923_call = mutated_mod.get_global_var('func_2923')
call_10279 = relay.TupleGetItem(func_2921_call(), 0)
call_10280 = relay.TupleGetItem(func_2923_call(), 0)
func_9348_call = mod.get_global_var('func_9348')
func_9351_call = mutated_mod.get_global_var('func_9351')
const_10286 = relay.const(8, dtype = "uint16")#candidate|10286|()|const|uint16
var_10287 = relay.var("var_10287", dtype = "uint16", shape = (105, 2))#candidate|10287|(105, 2)|var|uint16
call_10285 = relay.TupleGetItem(func_9348_call(relay.reshape(const_10286.astype('uint16'), []), relay.reshape(var_10287.astype('uint16'), [1, 15, 14]), ), 1)
call_10288 = relay.TupleGetItem(func_9351_call(relay.reshape(const_10286.astype('uint16'), []), relay.reshape(var_10287.astype('uint16'), [1, 15, 14]), ), 1)
func_3302_call = mod.get_global_var('func_3302')
func_3303_call = mutated_mod.get_global_var('func_3303')
call_10289 = relay.TupleGetItem(func_3302_call(), 0)
call_10290 = relay.TupleGetItem(func_3303_call(), 0)
func_3332_call = mod.get_global_var('func_3332')
func_3335_call = mutated_mod.get_global_var('func_3335')
call_10307 = relay.TupleGetItem(func_3332_call(relay.reshape(call_10252.astype('float32'), [78, 6])), 4)
call_10308 = relay.TupleGetItem(func_3335_call(relay.reshape(call_10252.astype('float32'), [78, 6])), 4)
output = relay.Tuple([call_10252,call_10279,call_10285,const_10286,var_10287,call_10289,call_10307,])
output2 = relay.Tuple([call_10253,call_10280,call_10288,const_10286,var_10287,call_10290,call_10308,])
func_10317 = relay.Function([var_10287,], output)
mod['func_10317'] = func_10317
mod = relay.transform.InferType()(mod)
var_10318 = relay.var("var_10318", dtype = "uint16", shape = (105, 2))#candidate|10318|(105, 2)|var|uint16
output = func_10317(var_10318)
func_10319 = relay.Function([var_10318], output)
mutated_mod['func_10319'] = func_10319
mutated_mod = relay.transform.InferType()(mutated_mod)
const_10352 = relay.const([[[7.740914,3.019269,0.337979,0.435688,2.683968,-3.933171,-6.862309,4.079491,5.852627],[-7.764316,9.222489,-2.323298,7.473826,-2.046723,-5.490723,4.139176,-8.028064,1.508375],[3.274636,7.529037,5.333604,3.774446,-3.048219,-2.185351,6.330035,5.673545,7.667278],[-9.056940,4.476856,2.754345,-1.731290,0.834032,-9.594277,-5.024341,0.963518,-8.822224],[3.189465,-8.681841,-5.411316,-0.277371,1.864094,-6.061762,9.187217,7.688367,-4.064823],[1.021243,-0.326049,3.387818,6.232528,-9.288690,4.781161,8.665454,8.469819,9.005845],[-0.088619,7.086800,3.382069,-9.416850,0.606167,3.230659,2.034596,-8.556927,-3.009711],[-3.914667,-1.235937,-4.410793,8.539081,-3.175948,-0.003672,-6.163747,0.878381,-9.971187],[-8.159305,-2.771922,8.320752,0.951325,-6.736430,-4.733991,6.348994,-9.933729,8.174768],[6.695550,-2.288787,3.492764,7.187147,7.588338,-9.143391,-3.938996,-6.492216,-3.944488],[-1.312889,-5.856486,0.843445,1.762876,2.594920,-8.461461,3.827867,3.922413,-3.415449],[-1.305915,7.472322,-1.014530,4.668857,-8.745641,6.773379,7.593214,-6.410585,-8.947786],[-1.199296,-9.940466,8.847702,0.183885,-4.144153,-0.791967,3.512452,9.066832,-9.619952],[-6.051046,-4.316752,-7.619234,6.091758,8.553967,3.415780,-9.405910,-0.213266,-6.556154]],[[7.823643,-9.446804,-3.338754,-9.389276,6.769390,-0.896111,-6.694120,8.175812,7.717056],[-0.599216,-3.184545,-5.947315,-9.886529,9.359660,8.372416,-7.401231,1.589851,1.889877],[-3.566382,-6.576748,8.550714,1.110124,4.713270,-5.381979,-4.548117,-5.342893,-1.640048],[1.899935,8.196370,1.058325,-9.881279,0.403234,-9.356405,1.296030,0.564814,-4.213157],[5.688065,-8.559602,1.278890,3.447346,1.945477,-4.571903,0.742808,-4.510124,-1.043147],[9.396416,-1.035067,4.059755,2.194712,9.956943,-8.142211,7.314474,5.417738,-1.802550],[-6.566086,1.639163,9.677352,-5.412587,5.040551,3.224634,-5.396208,-8.955752,-1.554119],[-3.743845,-0.237912,-5.354371,0.826936,-9.037653,5.680141,8.327103,7.896362,3.939964],[-3.479132,3.180333,0.435059,-6.421907,6.499648,-2.614085,-1.041470,-6.636372,-1.138736],[0.454276,-9.634007,-9.085155,-2.641431,-4.426231,-3.034925,1.927672,0.794380,-9.614618],[5.287865,-9.500817,3.548019,-5.584370,7.655582,8.876804,0.189516,-0.339291,-0.966371],[7.998147,-4.498779,-7.783182,-7.783201,-0.701179,-7.599637,-9.823830,8.663136,3.038391],[6.404530,-8.833147,-9.683901,-6.463910,-6.377644,1.365362,0.411428,9.534534,-5.194692],[1.142922,9.824351,-6.942270,-4.492861,-7.394136,-6.911075,6.932786,0.148383,-0.710791]],[[7.269138,-1.618654,9.338144,-9.096525,-7.500419,6.236681,-7.332356,1.851512,-1.101140],[8.367525,-7.558401,-1.725736,0.544146,-7.203304,9.498333,-1.782283,4.070230,-8.350691],[1.984531,-0.966322,-2.271986,-1.167734,-1.652712,8.961926,-6.822639,6.118434,-2.404676],[6.019836,5.206446,-1.083378,-1.821698,2.844116,4.313261,6.090831,4.494029,4.564851],[2.759889,-4.626259,4.092027,-2.865058,-3.221726,3.184667,9.497086,8.341210,-8.643056],[5.852609,-2.764708,4.652838,-9.496944,-9.055407,-4.580272,0.846084,-0.574293,1.840377],[0.458539,5.447623,4.486073,-6.270917,2.997401,-0.920726,-3.209322,-6.827709,-7.525478],[-8.554375,-5.672737,-2.364317,-4.446875,-0.353856,2.462198,9.746930,9.075468,5.222720],[2.789782,0.870424,9.920908,-4.474647,7.353480,-4.375482,-2.667612,-8.086989,-7.140281],[1.585143,8.240778,2.909542,6.616030,2.235889,3.359282,-9.077100,2.405559,3.276712],[3.616840,-0.055803,-1.848193,-0.070562,2.530870,-2.249435,-5.200343,1.152498,0.410952],[-0.178988,6.292759,-7.470937,-1.967892,6.242879,-4.537293,-9.208768,-0.847704,4.807941],[-9.367033,-2.301395,-7.523539,9.281552,-1.286136,-9.356737,8.304953,3.948359,8.755426],[2.752947,-3.337318,6.166138,6.071213,-5.182506,-9.121131,-9.622618,6.707337,-2.436871]],[[3.212677,-1.370775,-3.767888,-5.396619,-2.639482,-0.601049,5.147723,7.001259,-3.536117],[-3.117824,8.854940,-0.189953,-3.582978,-1.913257,2.417530,-6.211916,-4.046072,-2.698721],[7.205761,-7.320683,-5.328459,0.674789,-4.563741,1.772850,7.599824,-8.709039,-4.660517],[-6.303324,1.175915,9.189130,-2.244995,-2.023616,-8.743420,9.954330,7.022038,1.948123],[0.461107,3.109992,-4.994031,-8.779830,-7.669120,-7.585442,2.156793,-8.862722,5.907945],[6.098429,7.547352,-7.038580,0.077159,0.069049,3.776395,-7.150326,-0.279357,-8.548454],[4.770553,-3.090261,3.765428,-6.790802,-5.973890,0.621229,-6.187295,3.235078,-7.542279],[-4.537838,0.078502,-3.537464,-1.268904,1.706465,-1.174606,1.440304,9.362810,-3.953763],[-1.226996,9.880060,7.675811,-6.672484,-7.900904,4.519629,3.052566,-2.047235,9.764354],[5.331222,8.912286,-6.691528,-2.783592,8.802111,-1.458547,-5.285139,2.597082,6.548846],[6.548967,-3.132988,4.695267,-3.372971,2.324892,1.829228,-6.754266,8.144860,-3.088383],[3.302073,5.616092,-9.413084,-4.124031,8.689186,-6.008626,-7.110102,-4.340984,9.868052],[-2.650272,3.138119,-2.939181,1.488378,9.206683,8.084024,-1.090932,9.546734,4.183327],[4.325036,-4.732374,8.720040,9.394207,-0.010870,4.198713,6.969447,-2.430998,1.777126]],[[-8.091293,3.057171,0.105366,5.172784,7.550179,-9.052281,-9.953577,6.649852,-6.875115],[6.178398,-5.576101,8.460022,-1.445921,-8.412416,6.202617,3.756749,-8.170170,-7.562001],[0.155313,1.028376,-0.470270,-6.831691,-2.068481,2.117354,-2.781860,-6.412173,0.679834],[-2.368511,8.020660,-2.489802,6.050464,-1.090659,-4.135484,4.347344,-7.810041,-7.554143],[-1.122355,8.493384,-6.381135,2.648788,7.857705,-1.050123,-9.514693,-5.989987,7.066279],[-0.024561,2.265092,-8.777029,5.237704,1.915134,-6.002161,-7.648950,-1.518894,0.822902],[9.644523,-7.301627,0.187185,8.524711,5.984919,6.919509,-5.473225,9.754197,-3.911104],[1.321687,-4.308160,1.842662,-4.434532,2.242325,4.640407,-6.337746,-4.372835,3.931715],[9.300297,4.709266,4.548155,9.066775,-6.300450,7.881857,-6.269064,3.922747,4.133584],[6.931783,-2.479722,8.466159,-8.641573,-8.418854,-1.306718,-0.701607,-1.220178,-6.663794],[-3.367077,7.189784,5.663153,3.362169,7.582743,-1.182465,1.394538,4.615340,-9.792796],[7.485267,-1.370064,3.949605,9.390196,-1.073460,6.610086,9.398500,-0.846215,7.436233],[9.668302,6.871941,9.214768,-9.713022,0.052671,-3.326459,-0.252967,-1.611160,-5.594153],[0.841423,7.178303,1.372857,-4.288997,-1.347222,-3.251173,-2.481925,-3.457315,-6.111923]],[[4.971507,-1.577888,-9.106110,8.787932,-7.186452,8.852405,7.049226,3.198054,-7.478194],[-0.028193,7.632985,5.705327,-7.756829,-1.643818,2.302078,-2.698873,4.378346,-4.011187],[1.277944,-5.445712,9.393566,-7.603832,-6.877116,-8.909040,9.870163,9.078106,3.786739],[-7.572218,8.593302,3.485177,8.222693,6.883239,-2.856822,4.716447,3.939511,-3.953931],[2.799388,-8.158581,-6.506194,2.027152,8.137458,-4.530829,6.659486,-3.621198,2.357785],[-8.096419,8.613677,8.235891,3.238537,9.962145,-4.091653,4.640499,9.705551,9.302936],[-2.498158,3.753621,-0.776306,6.070741,-2.700146,-8.005086,0.005282,-2.446349,-1.894020],[-0.878062,-3.414631,6.226966,3.439268,6.912499,-7.892414,-3.038747,6.078679,-4.982214],[-3.334602,1.410253,8.789458,-3.736912,-4.003325,9.818240,9.852034,-1.517029,0.778638],[-9.502282,8.967470,7.315173,8.716683,-8.237824,6.785845,-5.400740,-2.100449,-7.711990],[0.074575,-6.266247,-1.301187,-2.052944,-7.621078,7.883351,-0.091029,-5.990001,8.645815],[0.061243,-0.987419,3.861770,-7.102952,9.852977,-8.944861,-3.719125,-1.523609,5.063608],[-9.198358,-8.225940,7.888016,1.208063,-8.937653,0.562192,1.923973,-6.293144,-4.087077],[-7.228764,4.837288,-5.785715,5.005376,3.786223,5.107792,-2.968706,-5.012164,-9.310686]],[[4.846266,-2.067748,-4.090642,4.008472,-5.805053,9.353380,-2.006843,-9.385031,7.260644],[4.625111,8.639886,-6.855475,0.371843,6.891194,-4.111256,7.422556,4.990482,0.608271],[7.898387,6.801821,-7.543411,2.271587,-8.452263,-6.735406,-0.507273,1.442695,-5.234113],[-2.042262,-6.494968,9.063036,-8.278439,-3.504199,-4.417549,9.583556,1.307903,-6.376718],[7.578006,-7.295733,5.084312,1.349630,-8.706973,5.430735,-6.281727,-4.046228,2.022140],[5.272555,9.938872,6.491162,8.492517,4.282214,-9.872188,-3.766563,7.337971,7.760406],[0.487721,-5.416698,6.705265,-2.639531,-8.942748,0.520133,8.038377,4.208102,-9.111733],[-5.915148,8.892312,-7.983984,7.432983,8.623585,1.353609,5.503284,6.433685,-4.141203],[-1.594389,-0.251920,-2.389920,-6.900333,7.513905,-5.860141,1.259124,1.129950,-7.139035],[-7.167241,1.801662,1.608957,-9.394630,1.378815,-6.398942,7.588240,0.931011,2.898664],[7.873443,4.051129,4.167501,-3.525370,-1.187552,1.874586,-9.128516,8.934849,5.496029],[-7.413355,8.659897,4.416853,-8.569659,-6.286588,2.092261,0.725773,-3.671272,2.597680],[-0.113435,-9.902151,0.357652,9.984657,7.870259,7.059451,2.876470,-1.057627,-0.588433],[4.862120,-0.527982,-9.221184,9.273428,-3.739346,-1.215594,-6.599632,-0.743214,2.030266]],[[-3.782382,6.424039,4.857132,4.962539,-7.816555,-5.476032,4.603995,7.699092,6.660496],[0.628171,9.383931,-8.382468,4.473836,-8.096601,2.595130,-8.692707,2.459402,9.947909],[-2.425130,1.238302,4.026673,9.673961,3.284933,-0.248548,-2.834578,-4.507786,-5.981704],[5.038504,2.109793,7.349192,-5.264746,-5.433443,3.081326,-7.043044,-9.845320,-0.627671],[4.015858,2.365325,3.009920,-3.778909,3.703062,7.646617,0.343282,-4.441429,5.820036],[-9.475755,2.475998,8.225198,-3.896117,-4.075657,1.378003,-9.930225,0.411509,-4.033387],[-6.903902,-7.607706,3.490197,3.441142,8.477598,7.461789,9.948633,-9.735554,-6.933593],[6.297750,9.214554,-8.062201,-0.898900,-5.812005,-4.245243,-2.633544,9.022924,-4.586286],[3.523663,7.068447,1.363169,8.634854,-8.154689,5.588005,9.252161,-7.565709,3.888363],[9.760742,8.548294,2.561440,-1.075297,-3.871227,-4.834544,-9.503704,-1.669552,-2.912756],[-1.194179,-2.886431,9.440540,-5.997910,-1.814491,-6.022896,8.303741,-2.031338,1.144183],[-5.677666,2.104008,4.123700,3.876810,1.261427,2.432806,-0.262536,8.050598,0.903621],[-7.216956,7.569825,-6.423267,-0.490158,-5.192146,-1.437201,-1.843440,7.154343,-2.967167],[-5.242973,7.250688,5.096900,2.096743,-1.706724,6.894850,-4.924190,7.349155,-3.621649]],[[6.956329,6.309513,8.757363,9.101780,-2.968239,-1.597266,0.664503,5.023543,-1.611206],[5.310180,-7.615705,2.596454,1.228330,5.803188,3.764398,-0.621479,9.567537,-6.626057],[-3.377919,-1.025683,4.405000,4.387921,7.992135,1.504700,0.678889,-4.927200,-1.972681],[0.636528,5.389904,7.748373,1.955582,0.765906,2.420522,3.149458,0.763356,8.409713],[-0.191062,6.789496,0.248176,-4.205314,4.319318,-3.879596,-4.088925,-7.896150,-0.963969],[-7.397844,9.133509,-4.536120,-8.587647,-6.544765,-2.348547,-6.264097,-1.311415,-7.103117],[-4.390431,4.544011,3.764920,9.768373,0.300826,4.577111,2.601714,2.809850,6.007099],[-6.694517,-2.068632,4.361734,-2.334931,3.941061,9.293484,-9.868909,-3.167486,-0.282708],[8.206526,4.520730,9.252931,-7.881144,5.961253,1.370051,-1.284670,-5.354166,5.866609],[5.865739,6.621904,-7.125815,-0.744775,-7.765075,-0.532761,3.188206,-3.849011,1.152091],[2.880802,6.563693,0.043167,-0.898193,-2.746376,-7.985411,-1.712251,4.951036,3.765868],[2.186613,-4.810614,-2.906696,-0.084078,-0.990421,6.463372,-4.177128,9.046966,8.908907],[-2.547218,-8.764258,-5.710897,-9.325596,-3.939065,-1.469016,-6.838432,-0.947530,0.274812],[6.843678,-9.950672,-8.808942,2.877912,-4.462619,-3.974362,-9.293278,3.875484,8.774560]],[[2.094444,3.900224,3.111648,6.307751,0.271502,-5.120435,5.943152,-4.669459,8.479755],[5.113212,0.498465,-5.203150,3.676924,-4.652681,5.749972,-4.238931,-5.230628,8.081950],[3.580726,3.002094,-3.602691,5.724538,6.907881,7.895195,-8.221449,-3.691773,-9.899922],[-9.870699,7.615663,8.246094,-5.228635,5.783635,4.678557,1.908217,-3.486245,6.478420],[-2.183048,-1.426026,-4.659132,4.125768,-6.356797,-8.187743,-5.656592,-1.837001,2.049238],[-6.746132,8.339978,-1.273107,-4.409010,3.574491,-7.122168,5.685875,6.271975,7.078199],[2.774192,-1.084889,-2.791510,1.478870,5.887911,-3.864816,3.563905,9.039754,-1.955633],[3.160513,3.403874,2.563115,3.473487,-7.201079,-7.761354,-7.787702,-9.283121,1.285760],[3.549537,5.694822,-9.483746,9.056638,5.304497,-1.946049,3.432326,-5.379701,-6.360872],[-3.345397,7.890518,-6.201589,-2.304661,4.447551,-6.469184,8.275897,4.304190,-6.551103],[-6.234009,9.695539,-5.576735,-0.366635,2.785849,-5.050432,-9.217518,5.291076,-1.032735],[-6.948576,-4.220728,2.373465,-9.240875,-2.467131,-8.230595,-4.882896,4.629243,-8.960491],[1.263115,2.719333,2.462343,9.604948,-6.215072,1.815960,-4.163220,-3.774510,-5.242746],[6.635474,-2.499062,-4.198145,4.238423,-8.758780,2.750586,-8.760715,1.827868,7.437098]],[[-5.512876,-1.551994,-5.230134,3.918325,2.920999,6.167589,8.936152,2.010986,1.428752],[-7.382582,-8.380001,2.248852,3.391753,-6.393648,7.168155,-5.254786,-8.753901,-5.473890],[-8.919019,-9.076319,7.224932,9.047093,-8.469299,7.983519,4.435020,-7.683926,-6.973894],[2.202522,-4.617392,-2.379042,4.866378,4.596936,6.672619,-0.758317,8.949636,-7.104334],[5.849136,0.997869,-5.511972,8.849372,8.252648,9.131354,3.356068,2.366979,-3.846035],[6.894148,-3.533550,-1.133852,-8.173854,-0.009391,3.974738,8.449488,-0.826635,-4.551859],[1.880465,-7.438073,-1.070212,-3.852182,-8.985054,6.824211,4.398708,4.183534,3.791494],[8.695536,-5.485397,1.486296,-6.037629,-5.800161,9.467165,1.454280,-8.434937,2.714437],[2.009249,-0.070361,-0.049654,1.334992,-9.902422,2.580844,-4.793816,-6.228076,-6.686467],[-8.841647,-0.986770,-4.085762,9.122044,-5.420913,4.087869,-3.849551,8.113928,9.771186],[-2.921248,3.588513,5.154363,-5.491155,0.207274,-0.219178,-9.825819,8.300375,-7.315592],[0.861679,3.003901,5.050804,9.392943,-8.110909,6.751103,-9.034632,-3.040644,-2.865220],[2.553486,9.876639,6.033542,-3.716421,-8.720682,-7.348482,8.737711,-7.917926,5.349403],[-5.501602,-0.941211,9.031894,-6.544053,3.316697,5.688597,-9.573625,6.684710,-3.352109]],[[7.663499,-7.592338,-7.269436,-5.507755,-1.401623,-0.910350,1.249309,1.494440,8.551966],[2.799911,-7.371446,-4.517950,-3.693042,-0.784619,-6.713127,8.981638,-5.147956,4.822947],[-8.371229,-3.051270,1.973728,9.861090,8.375891,-9.812264,0.530406,-8.458351,-4.064257],[-7.671944,3.911590,-4.965625,3.929182,-8.876468,-0.749447,-6.790691,5.176549,1.610682],[6.334822,4.666473,6.481017,-7.322686,4.471160,6.934709,5.438280,2.847850,-4.488399],[1.948139,4.484428,8.726543,9.984573,-2.878894,3.772894,7.457348,-3.960531,7.554889],[-2.646834,4.391475,5.354594,-4.974955,-2.530087,1.716362,9.035547,-2.899710,-5.745900],[-1.441462,4.400911,5.704103,5.503883,0.767583,5.095913,0.664020,-8.584250,-0.233045],[0.844510,2.049922,-8.731667,9.620938,8.052094,-3.876675,7.315946,2.941319,0.908104],[8.022971,-3.127634,6.176393,-9.897337,6.252501,7.773353,-4.463429,-5.914179,-7.500570],[-6.522629,3.641149,3.271571,-2.223966,-3.668146,8.904449,-5.350850,-2.378367,0.477686],[-1.006340,9.750451,4.630181,5.858584,2.737529,2.633450,-0.727910,5.482349,7.719968],[5.980900,-0.961604,9.839526,-4.496946,-5.309144,-5.416274,-4.480832,9.347384,4.624674],[-2.293376,-0.081295,-2.748015,6.679164,-1.461924,-6.700029,0.562257,7.215240,-5.418648]]], dtype = "float32")#candidate|10352|(12, 14, 9)|const|float32
uop_10353 = relay.log2(const_10352.astype('float32')) # shape=(12, 14, 9)
func_6300_call = mod.get_global_var('func_6300')
func_6302_call = mutated_mod.get_global_var('func_6302')
call_10356 = relay.TupleGetItem(func_6300_call(), 0)
call_10357 = relay.TupleGetItem(func_6302_call(), 0)
uop_10364 = relay.asin(uop_10353.astype('float32')) # shape=(12, 14, 9)
output = relay.Tuple([call_10356,uop_10364,])
output2 = relay.Tuple([call_10357,uop_10364,])
func_10372 = relay.Function([], output)
mod['func_10372'] = func_10372
mod = relay.transform.InferType()(mod)
mutated_mod['func_10372'] = func_10372
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10372_call = mutated_mod.get_global_var('func_10372')
call_10373 = func_10372_call()
output = call_10373
func_10374 = relay.Function([], output)
mutated_mod['func_10374'] = func_10374
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4266_call = mod.get_global_var('func_4266')
func_4267_call = mutated_mod.get_global_var('func_4267')
call_10445 = func_4266_call()
call_10446 = func_4266_call()
output = call_10445
output2 = call_10446
func_10501 = relay.Function([], output)
mod['func_10501'] = func_10501
mod = relay.transform.InferType()(mod)
mutated_mod['func_10501'] = func_10501
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10501_call = mutated_mod.get_global_var('func_10501')
call_10502 = func_10501_call()
output = call_10502
func_10503 = relay.Function([], output)
mutated_mod['func_10503'] = func_10503
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6579_call = mod.get_global_var('func_6579')
func_6581_call = mutated_mod.get_global_var('func_6581')
call_10510 = relay.TupleGetItem(func_6579_call(), 0)
call_10511 = relay.TupleGetItem(func_6581_call(), 0)
func_3526_call = mod.get_global_var('func_3526')
func_3528_call = mutated_mod.get_global_var('func_3528')
call_10528 = func_3526_call()
call_10529 = func_3526_call()
func_842_call = mod.get_global_var('func_842')
func_847_call = mutated_mod.get_global_var('func_847')
var_10537 = relay.var("var_10537", dtype = "float64", shape = (28, 4))#candidate|10537|(28, 4)|var|float64
call_10536 = relay.TupleGetItem(func_842_call(relay.reshape(var_10537.astype('float64'), [4, 4, 7]), relay.reshape(var_10537.astype('float64'), [4, 4, 7]), relay.reshape(call_10510.astype('float32'), [1, 468]), ), 1)
call_10538 = relay.TupleGetItem(func_847_call(relay.reshape(var_10537.astype('float64'), [4, 4, 7]), relay.reshape(var_10537.astype('float64'), [4, 4, 7]), relay.reshape(call_10510.astype('float32'), [1, 468]), ), 1)
output = relay.Tuple([call_10510,call_10528,call_10536,var_10537,])
output2 = relay.Tuple([call_10511,call_10529,call_10538,var_10537,])
func_10539 = relay.Function([var_10537,], output)
mod['func_10539'] = func_10539
mod = relay.transform.InferType()(mod)
mutated_mod['func_10539'] = func_10539
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10540 = relay.var("var_10540", dtype = "float64", shape = (28, 4))#candidate|10540|(28, 4)|var|float64
func_10539_call = mutated_mod.get_global_var('func_10539')
call_10541 = func_10539_call(var_10540)
output = call_10541
func_10542 = relay.Function([var_10540], output)
mutated_mod['func_10542'] = func_10542
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9076_call = mod.get_global_var('func_9076')
func_9077_call = mutated_mod.get_global_var('func_9077')
call_10563 = func_9076_call()
call_10564 = func_9076_call()
func_7855_call = mod.get_global_var('func_7855')
func_7856_call = mutated_mod.get_global_var('func_7856')
call_10571 = relay.TupleGetItem(func_7855_call(), 0)
call_10572 = relay.TupleGetItem(func_7856_call(), 0)
func_6300_call = mod.get_global_var('func_6300')
func_6302_call = mutated_mod.get_global_var('func_6302')
call_10609 = relay.TupleGetItem(func_6300_call(), 0)
call_10610 = relay.TupleGetItem(func_6302_call(), 0)
output = relay.Tuple([call_10563,call_10571,call_10609,])
output2 = relay.Tuple([call_10564,call_10572,call_10610,])
func_10616 = relay.Function([], output)
mod['func_10616'] = func_10616
mod = relay.transform.InferType()(mod)
mutated_mod['func_10616'] = func_10616
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10616_call = mutated_mod.get_global_var('func_10616')
call_10617 = func_10616_call()
output = call_10617
func_10618 = relay.Function([], output)
mutated_mod['func_10618'] = func_10618
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4549_call = mod.get_global_var('func_4549')
func_4551_call = mutated_mod.get_global_var('func_4551')
call_10625 = relay.TupleGetItem(func_4549_call(), 2)
call_10626 = relay.TupleGetItem(func_4551_call(), 2)
output = relay.Tuple([call_10625,])
output2 = relay.Tuple([call_10626,])
func_10635 = relay.Function([], output)
mod['func_10635'] = func_10635
mod = relay.transform.InferType()(mod)
mutated_mod['func_10635'] = func_10635
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10635_call = mutated_mod.get_global_var('func_10635')
call_10636 = func_10635_call()
output = call_10636
func_10637 = relay.Function([], output)
mutated_mod['func_10637'] = func_10637
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8445_call = mod.get_global_var('func_8445')
func_8446_call = mutated_mod.get_global_var('func_8446')
call_10641 = func_8445_call()
call_10642 = func_8445_call()
output = call_10641
output2 = call_10642
func_10662 = relay.Function([], output)
mod['func_10662'] = func_10662
mod = relay.transform.InferType()(mod)
output = func_10662()
func_10663 = relay.Function([], output)
mutated_mod['func_10663'] = func_10663
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6065_call = mod.get_global_var('func_6065')
func_6067_call = mutated_mod.get_global_var('func_6067')
call_10834 = relay.TupleGetItem(func_6065_call(), 0)
call_10835 = relay.TupleGetItem(func_6067_call(), 0)
func_9531_call = mod.get_global_var('func_9531')
func_9533_call = mutated_mod.get_global_var('func_9533')
call_10866 = relay.TupleGetItem(func_9531_call(), 1)
call_10867 = relay.TupleGetItem(func_9533_call(), 1)
func_9122_call = mod.get_global_var('func_9122')
func_9124_call = mutated_mod.get_global_var('func_9124')
call_10883 = func_9122_call()
call_10884 = func_9122_call()
const_10887 = relay.const([[[1,-3,7,9,6,7,3,7,-8,7],[5,4,7,-9,6,-10,7,1,1,-7],[6,-4,1,-10,-10,7,-7,3,5,-1],[-1,9,4,-1,-2,3,4,6,9,-4],[-4,-6,-2,-7,3,9,10,-2,-9,-9],[-3,10,2,-3,-3,1,6,2,-8,-6],[-8,-5,-6,-1,9,-6,6,10,-2,-10],[7,-4,-1,-4,7,10,-8,2,-1,7],[-6,-2,10,10,-4,9,-4,-8,-3,-3]],[[-2,-4,7,4,-2,8,5,10,-2,9],[1,-9,5,9,10,6,5,4,-9,-10],[9,-9,-9,-2,-9,1,1,6,-7,-3],[9,9,-3,-7,-9,-3,6,5,-1,10],[-9,4,1,7,-9,5,2,-1,6,7],[-7,-6,-2,-10,-9,7,-3,8,-2,-2],[-5,-6,-10,4,-7,1,-3,8,-9,10],[-1,4,7,8,6,8,-4,2,5,9],[-9,7,9,-7,4,-6,4,8,1,1]],[[-3,-1,-5,-2,9,4,4,-7,-5,-3],[2,3,-9,-7,5,10,-9,7,-3,6],[-2,1,-2,-3,5,-7,5,-2,10,-5],[-1,7,5,6,4,-2,-4,4,-3,4],[-5,4,-2,-4,-8,-9,3,9,-9,8],[6,-10,4,6,-5,5,3,9,6,6],[-4,4,-1,7,-9,3,-8,-8,1,10],[-6,5,4,3,-9,7,5,1,6,8],[-5,-1,-8,-5,-2,-4,-4,6,-2,10]],[[-7,5,8,-10,5,10,-10,5,9,-6],[7,-9,-8,-8,5,4,-7,-6,4,-1],[-5,-9,1,3,-3,1,1,-10,-5,1],[-10,-2,3,-4,-5,4,-6,-6,-6,-5],[10,-9,-5,9,-1,10,7,-10,1,5],[-1,-7,-3,-3,2,8,-3,-2,-9,-8],[3,-4,3,1,10,-1,7,7,1,-9],[-8,-4,5,1,8,6,9,-2,-6,8],[8,-4,-7,5,2,2,2,-1,5,2]],[[-3,-5,-10,7,-3,-9,-2,6,-7,1],[6,7,1,-4,2,-10,-8,-9,5,4],[9,-8,10,4,6,5,9,9,-4,8],[3,-2,4,-9,7,6,-9,-7,-10,-6],[-6,-10,5,-9,-6,-6,7,-10,-9,-4],[4,-2,-6,-2,2,5,-9,7,8,-2],[4,-3,-7,-4,4,5,-9,1,-8,4],[-10,-7,5,2,9,6,-3,-6,4,7],[9,-7,10,4,2,-5,-6,-1,10,2]],[[9,-5,-9,-1,1,2,-3,-10,1,-9],[1,-7,-10,-8,4,-10,-10,-3,5,3],[-5,10,5,1,2,-1,5,10,6,6],[7,-3,2,-5,4,-5,-2,9,2,5],[9,9,-4,9,-6,-2,-2,8,-2,1],[1,-9,10,2,7,8,-5,-9,-7,-1],[-5,3,-7,-9,4,-9,5,-9,5,9],[-1,9,5,5,8,4,-6,-1,8,5],[2,-10,-1,4,-10,-9,1,5,6,9]],[[-5,-9,9,-3,2,2,2,-10,9,-9],[6,-8,-6,2,-4,-7,-3,-9,8,1],[1,-5,3,6,-1,1,-2,4,-3,-9],[-9,-5,5,-5,5,7,7,-9,-9,-2],[-1,-10,1,3,4,2,-10,-6,-10,-2],[-8,3,10,8,6,-4,5,1,9,2],[6,7,-1,-1,-7,-10,-1,-4,4,2],[4,-8,-9,-4,1,-4,-2,-2,-5,5],[-7,6,-7,-9,-2,10,9,4,-7,8]],[[8,4,10,-2,1,6,-4,4,-5,-2],[-5,3,-2,-2,9,8,10,7,10,-7],[-1,-8,7,8,-6,9,5,-5,-10,8],[7,-9,10,8,-9,10,10,-7,-2,9],[7,9,-1,-1,-9,2,-4,2,-1,3],[-9,-2,-3,-8,-5,-10,6,-4,-4,-7],[3,1,-2,-1,-7,-5,-7,5,-5,4],[-1,-2,-6,3,-3,-4,-2,4,-10,-1],[9,-1,-2,-8,-1,-8,-7,-1,-9,2]],[[7,-10,3,-6,-1,7,-10,8,-5,10],[-9,10,9,8,8,-3,7,5,-9,2],[6,4,8,-10,10,-10,-6,-4,4,4],[3,-4,-3,10,-9,-4,2,3,-1,4],[2,-10,-6,5,8,9,-9,2,3,-3],[-6,7,6,9,-2,-9,-7,-5,5,3],[1,5,-7,1,-10,-4,3,8,3,5],[10,-2,-6,4,-6,7,10,-9,-10,9],[-7,10,-4,7,6,3,-9,5,-1,-7]],[[5,-8,7,-2,-10,-6,-5,6,5,-7],[9,-6,-6,-4,-1,7,6,-1,-5,-7],[-7,3,-1,9,4,4,-9,-2,3,-3],[-8,10,-6,-6,-7,7,9,-4,-8,-4],[-1,6,1,5,3,-6,-10,4,9,-8],[-4,-8,4,-3,7,5,-8,-7,6,-10],[-4,9,-5,10,6,10,-3,-4,2,-9],[5,-6,2,9,-7,-8,-7,5,-3,-8],[4,-8,-6,-4,-10,-5,7,-7,5,1]],[[-8,7,10,-7,-6,2,3,-7,-4,7],[-5,8,-6,-3,2,-6,-4,6,-2,7],[-10,-10,-2,-3,-9,8,-7,-8,-3,3],[-6,8,2,4,-10,4,3,-4,2,-9],[10,-6,6,-7,4,6,2,2,1,8],[8,-1,9,-5,-5,-1,-4,9,1,-10],[-9,-7,-4,5,-4,5,8,-4,-3,5],[5,-2,-4,-8,-10,-2,-7,-10,-9,-6],[-9,-8,9,1,2,10,5,-6,-5,-6]],[[5,4,8,-4,-2,-1,-1,7,10,4],[5,7,7,10,10,-9,-3,-8,10,9],[2,2,-8,7,-6,-10,-6,2,10,7],[8,-4,2,4,-4,3,-5,-3,-3,-1],[-1,1,-7,3,7,-9,8,7,-5,-2],[-6,-9,8,-1,2,10,-2,3,8,-7],[7,-9,9,-5,-9,-7,1,-5,8,2],[10,5,6,9,5,-6,-4,-7,3,9],[-2,8,-10,4,10,10,-9,2,-3,7]]], dtype = "int64")#candidate|10887|(12, 9, 10)|const|int64
bop_10888 = relay.less(call_10883.astype('bool'), relay.reshape(const_10887.astype('bool'), relay.shape_of(call_10883))) # shape=(12, 9, 10)
bop_10891 = relay.less(call_10884.astype('bool'), relay.reshape(const_10887.astype('bool'), relay.shape_of(call_10884))) # shape=(12, 9, 10)
output = relay.Tuple([call_10834,call_10866,bop_10888,])
output2 = relay.Tuple([call_10835,call_10867,bop_10891,])
func_10895 = relay.Function([], output)
mod['func_10895'] = func_10895
mod = relay.transform.InferType()(mod)
mutated_mod['func_10895'] = func_10895
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10895_call = mutated_mod.get_global_var('func_10895')
call_10896 = func_10895_call()
output = call_10896
func_10897 = relay.Function([], output)
mutated_mod['func_10897'] = func_10897
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8175_call = mod.get_global_var('func_8175')
func_8177_call = mutated_mod.get_global_var('func_8177')
call_10930 = relay.TupleGetItem(func_8175_call(), 0)
call_10931 = relay.TupleGetItem(func_8177_call(), 0)
func_6711_call = mod.get_global_var('func_6711')
func_6712_call = mutated_mod.get_global_var('func_6712')
call_10951 = func_6711_call()
call_10952 = func_6711_call()
func_3859_call = mod.get_global_var('func_3859')
func_3861_call = mutated_mod.get_global_var('func_3861')
call_10957 = relay.TupleGetItem(func_3859_call(), 0)
call_10958 = relay.TupleGetItem(func_3861_call(), 0)
output = relay.Tuple([call_10930,call_10951,call_10957,])
output2 = relay.Tuple([call_10931,call_10952,call_10958,])
func_10981 = relay.Function([], output)
mod['func_10981'] = func_10981
mod = relay.transform.InferType()(mod)
output = func_10981()
func_10982 = relay.Function([], output)
mutated_mod['func_10982'] = func_10982
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9504_call = mod.get_global_var('func_9504')
func_9506_call = mutated_mod.get_global_var('func_9506')
call_10988 = relay.TupleGetItem(func_9504_call(), 0)
call_10989 = relay.TupleGetItem(func_9506_call(), 0)
func_9329_call = mod.get_global_var('func_9329')
func_9331_call = mutated_mod.get_global_var('func_9331')
call_10990 = relay.TupleGetItem(func_9329_call(), 3)
call_10991 = relay.TupleGetItem(func_9331_call(), 3)
func_3650_call = mod.get_global_var('func_3650')
func_3652_call = mutated_mod.get_global_var('func_3652')
const_10996 = relay.const([[-3.304841,8.467688],[-2.075112,-0.139295],[0.871894,-9.354702],[-8.321337,3.191023],[5.691868,-7.017414],[6.065880,-3.896721],[-9.720660,0.728270],[9.375414,7.180621],[-7.057900,8.773228],[2.306501,3.291208],[3.977288,0.330764],[3.501652,-2.040030],[9.995134,-2.247751],[-8.949107,-6.177720],[-4.356922,5.453502],[4.969695,-6.475259],[-3.246715,-1.615359],[6.973493,-8.415055],[4.321614,0.953176],[-5.046190,7.308206],[-8.415877,-8.090110],[-2.960770,4.807737],[-2.343967,-9.223354],[1.421147,-2.686878],[-9.828603,6.763413],[-9.582942,1.458816],[-0.679620,2.883876],[-0.770750,-6.092945],[-2.540740,-5.715689],[-5.287884,6.044046],[-8.759911,-0.181063],[-0.806690,4.423570],[1.906519,0.664332],[-8.818409,5.701118],[8.112311,-2.988348],[1.454364,-0.792755],[0.756639,-5.633195],[-0.099765,2.520556],[4.863599,-9.401490],[-5.857974,9.601635],[-8.220027,0.597984],[1.459513,1.940928],[8.471405,-4.291375],[5.574954,-3.332302],[0.182822,-7.776528],[5.459136,6.345885],[0.276899,-2.889886],[5.934886,2.993707],[-7.044443,1.351512],[4.158122,-1.235426],[-5.825235,0.077877],[1.213922,-5.968955],[-7.226671,-9.441862],[-5.550861,-1.473590],[7.985385,3.824432],[-0.982173,6.699860],[-9.755587,-9.457405],[6.875433,-3.765750],[-7.618456,8.380629],[-1.624655,-5.883484],[-5.174579,-5.303914],[-5.349553,-8.592292],[3.499488,0.017230],[-7.753755,1.297645],[2.996609,-3.065413],[-2.953137,-1.434616],[-8.290020,0.592665],[6.127391,7.707226],[-8.443850,1.992227],[3.196726,3.759187],[2.594732,-0.958719],[9.223016,-0.442638],[-2.686607,2.715634],[-1.999349,1.114358],[-5.113901,1.854656],[-9.960166,6.145084],[-6.494665,-5.566459],[9.440007,-1.393858],[-0.308265,-0.369078],[-0.914029,-1.076293],[-1.959271,-5.267456],[2.670982,7.501885],[-4.241873,6.381506],[-3.433484,3.538027],[2.120515,-0.718969],[0.173022,-4.911430],[6.374130,7.181890],[5.560290,-3.675872],[-8.877547,-3.064614],[-7.704767,0.803612],[-6.159879,-3.775056],[7.752441,8.524989],[5.681228,3.320251],[1.578808,-9.279999],[7.009437,-7.369070],[5.888674,-3.506786],[6.756825,8.015305],[-4.827439,-1.585105],[9.869818,5.792452],[0.245873,-0.261584],[-9.546621,3.048968],[5.380414,3.636282],[-7.904566,8.059981],[-6.010489,9.663694],[3.800269,-6.789415],[9.830438,-6.449418],[1.314152,2.924518],[7.354991,4.079058],[-7.664212,1.622802],[-5.815697,-1.717731],[-5.291895,-9.644595],[6.161529,6.299274],[-4.839697,-9.095039],[-5.699174,-7.555176],[2.571203,-7.190092],[8.540291,-6.084075],[6.770715,4.490436],[-1.264096,-0.280349],[-7.859611,-7.167735],[-5.749460,-0.080228],[1.522631,-6.002414],[1.454078,2.450027],[-0.387240,5.673753],[2.305683,6.611336],[6.304885,-7.494954],[-3.679792,9.782280],[1.078034,-3.695296],[7.440432,-8.949978],[-7.936944,-8.741878],[9.887688,-2.752007],[-9.620551,-7.069247],[1.303496,-2.966058],[-4.423739,0.597647],[7.830430,8.697397],[-5.822129,-8.086477],[-3.534213,-3.971193],[4.035943,7.331918],[-8.311954,-5.362851],[9.577915,-5.784943],[4.364508,-1.237999],[5.023053,-3.136738],[-4.517188,5.491525],[-3.801875,-7.603512],[-2.998698,6.978165]], dtype = "float32")#candidate|10996|(144, 2)|const|float32
call_10995 = relay.TupleGetItem(func_3650_call(relay.reshape(const_10996.astype('float32'), [288,])), 0)
call_10997 = relay.TupleGetItem(func_3652_call(relay.reshape(const_10996.astype('float32'), [288,])), 0)
output = relay.Tuple([call_10988,call_10990,call_10995,const_10996,])
output2 = relay.Tuple([call_10989,call_10991,call_10997,const_10996,])
func_11002 = relay.Function([], output)
mod['func_11002'] = func_11002
mod = relay.transform.InferType()(mod)
output = func_11002()
func_11003 = relay.Function([], output)
mutated_mod['func_11003'] = func_11003
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6721_call = mod.get_global_var('func_6721')
func_6722_call = mutated_mod.get_global_var('func_6722')
call_11012 = func_6721_call()
call_11013 = func_6721_call()
uop_11018 = relay.acosh(call_11012.astype('float64')) # shape=(15, 15, 10)
uop_11020 = relay.acosh(call_11013.astype('float64')) # shape=(15, 15, 10)
output = relay.Tuple([uop_11018,])
output2 = relay.Tuple([uop_11020,])
func_11025 = relay.Function([], output)
mod['func_11025'] = func_11025
mod = relay.transform.InferType()(mod)
output = func_11025()
func_11026 = relay.Function([], output)
mutated_mod['func_11026'] = func_11026
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7636_call = mod.get_global_var('func_7636')
func_7638_call = mutated_mod.get_global_var('func_7638')
call_11062 = relay.TupleGetItem(func_7636_call(), 0)
call_11063 = relay.TupleGetItem(func_7638_call(), 0)
output = relay.Tuple([call_11062,])
output2 = relay.Tuple([call_11063,])
func_11090 = relay.Function([], output)
mod['func_11090'] = func_11090
mod = relay.transform.InferType()(mod)
mutated_mod['func_11090'] = func_11090
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11090_call = mutated_mod.get_global_var('func_11090')
call_11091 = func_11090_call()
output = call_11091
func_11092 = relay.Function([], output)
mutated_mod['func_11092'] = func_11092
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10501_call = mod.get_global_var('func_10501')
func_10503_call = mutated_mod.get_global_var('func_10503')
call_11129 = func_10501_call()
call_11130 = func_10501_call()
output = call_11129
output2 = call_11130
func_11141 = relay.Function([], output)
mod['func_11141'] = func_11141
mod = relay.transform.InferType()(mod)
output = func_11141()
func_11142 = relay.Function([], output)
mutated_mod['func_11142'] = func_11142
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4088_call = mod.get_global_var('func_4088')
func_4090_call = mutated_mod.get_global_var('func_4090')
call_11156 = relay.TupleGetItem(func_4088_call(), 2)
call_11157 = relay.TupleGetItem(func_4090_call(), 2)
output = call_11156
output2 = call_11157
func_11158 = relay.Function([], output)
mod['func_11158'] = func_11158
mod = relay.transform.InferType()(mod)
mutated_mod['func_11158'] = func_11158
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11158_call = mutated_mod.get_global_var('func_11158')
call_11159 = func_11158_call()
output = call_11159
func_11160 = relay.Function([], output)
mutated_mod['func_11160'] = func_11160
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6579_call = mod.get_global_var('func_6579')
func_6581_call = mutated_mod.get_global_var('func_6581')
call_11188 = relay.TupleGetItem(func_6579_call(), 0)
call_11189 = relay.TupleGetItem(func_6581_call(), 0)
output = relay.Tuple([call_11188,])
output2 = relay.Tuple([call_11189,])
func_11195 = relay.Function([], output)
mod['func_11195'] = func_11195
mod = relay.transform.InferType()(mod)
output = func_11195()
func_11196 = relay.Function([], output)
mutated_mod['func_11196'] = func_11196
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9187_call = mod.get_global_var('func_9187')
func_9189_call = mutated_mod.get_global_var('func_9189')
call_11246 = relay.TupleGetItem(func_9187_call(), 2)
call_11247 = relay.TupleGetItem(func_9189_call(), 2)
func_6300_call = mod.get_global_var('func_6300')
func_6302_call = mutated_mod.get_global_var('func_6302')
call_11256 = relay.TupleGetItem(func_6300_call(), 0)
call_11257 = relay.TupleGetItem(func_6302_call(), 0)
output = relay.Tuple([call_11246,call_11256,])
output2 = relay.Tuple([call_11247,call_11257,])
func_11267 = relay.Function([], output)
mod['func_11267'] = func_11267
mod = relay.transform.InferType()(mod)
mutated_mod['func_11267'] = func_11267
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11267_call = mutated_mod.get_global_var('func_11267')
call_11268 = func_11267_call()
output = call_11268
func_11269 = relay.Function([], output)
mutated_mod['func_11269'] = func_11269
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11195_call = mod.get_global_var('func_11195')
func_11196_call = mutated_mod.get_global_var('func_11196')
call_11272 = relay.TupleGetItem(func_11195_call(), 0)
call_11273 = relay.TupleGetItem(func_11196_call(), 0)
output = relay.Tuple([call_11272,])
output2 = relay.Tuple([call_11273,])
func_11285 = relay.Function([], output)
mod['func_11285'] = func_11285
mod = relay.transform.InferType()(mod)
output = func_11285()
func_11286 = relay.Function([], output)
mutated_mod['func_11286'] = func_11286
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11294 = relay.var("var_11294", dtype = "float32", shape = (2, 11, 15))#candidate|11294|(2, 11, 15)|var|float32
uop_11295 = relay.asinh(var_11294.astype('float32')) # shape=(2, 11, 15)
output = relay.Tuple([uop_11295,])
output2 = relay.Tuple([uop_11295,])
func_11306 = relay.Function([var_11294,], output)
mod['func_11306'] = func_11306
mod = relay.transform.InferType()(mod)
mutated_mod['func_11306'] = func_11306
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11307 = relay.var("var_11307", dtype = "float32", shape = (2, 11, 15))#candidate|11307|(2, 11, 15)|var|float32
func_11306_call = mutated_mod.get_global_var('func_11306')
call_11308 = func_11306_call(var_11307)
output = call_11308
func_11309 = relay.Function([var_11307], output)
mutated_mod['func_11309'] = func_11309
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7187_call = mod.get_global_var('func_7187')
func_7189_call = mutated_mod.get_global_var('func_7189')
call_11311 = func_7187_call()
call_11312 = func_7187_call()
func_6300_call = mod.get_global_var('func_6300')
func_6302_call = mutated_mod.get_global_var('func_6302')
call_11340 = relay.TupleGetItem(func_6300_call(), 0)
call_11341 = relay.TupleGetItem(func_6302_call(), 0)
func_9823_call = mod.get_global_var('func_9823')
func_9824_call = mutated_mod.get_global_var('func_9824')
call_11347 = relay.TupleGetItem(func_9823_call(), 2)
call_11348 = relay.TupleGetItem(func_9824_call(), 2)
func_9707_call = mod.get_global_var('func_9707')
func_9709_call = mutated_mod.get_global_var('func_9709')
call_11372 = relay.TupleGetItem(func_9707_call(), 0)
call_11373 = relay.TupleGetItem(func_9709_call(), 0)
output = relay.Tuple([call_11311,call_11340,call_11347,call_11372,])
output2 = relay.Tuple([call_11312,call_11341,call_11348,call_11373,])
func_11404 = relay.Function([], output)
mod['func_11404'] = func_11404
mod = relay.transform.InferType()(mod)
output = func_11404()
func_11405 = relay.Function([], output)
mutated_mod['func_11405'] = func_11405
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6643_call = mod.get_global_var('func_6643')
func_6645_call = mutated_mod.get_global_var('func_6645')
call_11605 = relay.TupleGetItem(func_6643_call(), 4)
call_11606 = relay.TupleGetItem(func_6645_call(), 4)
output = call_11605
output2 = call_11606
func_11608 = relay.Function([], output)
mod['func_11608'] = func_11608
mod = relay.transform.InferType()(mod)
output = func_11608()
func_11609 = relay.Function([], output)
mutated_mod['func_11609'] = func_11609
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4958_call = mod.get_global_var('func_4958')
func_4959_call = mutated_mod.get_global_var('func_4959')
call_11691 = func_4958_call()
call_11692 = func_4958_call()
func_4346_call = mod.get_global_var('func_4346')
func_4350_call = mutated_mod.get_global_var('func_4350')
var_11712 = relay.var("var_11712", dtype = "uint32", shape = ())#candidate|11712|()|var|uint32
var_11713 = relay.var("var_11713", dtype = "uint32", shape = (12,))#candidate|11713|(12,)|var|uint32
call_11711 = relay.TupleGetItem(func_4346_call(relay.reshape(var_11712.astype('uint32'), []), relay.reshape(var_11713.astype('uint32'), [3, 1, 4]), ), 0)
call_11714 = relay.TupleGetItem(func_4350_call(relay.reshape(var_11712.astype('uint32'), []), relay.reshape(var_11713.astype('uint32'), [3, 1, 4]), ), 0)
func_5570_call = mod.get_global_var('func_5570')
func_5572_call = mutated_mod.get_global_var('func_5572')
call_11718 = relay.TupleGetItem(func_5570_call(), 0)
call_11719 = relay.TupleGetItem(func_5572_call(), 0)
func_7107_call = mod.get_global_var('func_7107')
func_7109_call = mutated_mod.get_global_var('func_7109')
call_11733 = relay.TupleGetItem(func_7107_call(), 2)
call_11734 = relay.TupleGetItem(func_7109_call(), 2)
func_8991_call = mod.get_global_var('func_8991')
func_8994_call = mutated_mod.get_global_var('func_8994')
const_11748 = relay.const([[-7],[-4],[-3],[-9],[8],[3],[-7],[-1],[6],[-7],[-9],[-2],[9],[9],[1],[5],[-6],[-8],[4],[7],[9],[1],[7],[-5],[6],[-10],[3],[1],[-7],[8],[-10],[5],[1],[-5],[1],[6],[10],[-5],[1],[-1],[-10],[-4],[-5],[6],[3],[-10],[-4],[9],[8],[-10],[-3],[-6],[8],[-1],[-9],[-6],[5],[3],[2],[2],[3],[10],[-6],[-5],[-2],[1],[3],[-2],[1],[10],[8],[-1],[5],[-3],[-5],[-6],[-4],[6],[-5],[4],[5],[-5],[-5],[1],[-10],[5],[6],[-1],[2],[-10],[6],[5],[-2],[1],[1],[-5],[3],[7],[6],[-3],[9],[-6],[-6],[8],[10],[6],[1],[7],[-2],[1],[6],[-10],[-7],[-8],[-6],[-3],[2],[2],[6],[-7],[7],[2],[3],[-3],[10],[8],[9],[6],[8],[-3],[6],[1],[-3],[6],[-4],[-6],[8],[-9],[7],[-6],[6],[-2],[4],[3],[1],[-6],[9],[-7],[-2],[-6],[7],[7],[9],[-6],[8],[1],[10],[10],[-1],[-5],[8],[1],[1],[-4],[10],[9],[-1],[5],[-2],[4],[5],[-5],[1],[8],[-10],[-8],[6],[-8],[7],[10],[-1],[7],[5],[1],[2],[-9],[-3],[1],[-2],[7],[2],[10],[5],[7],[-1],[1],[7],[-5],[-9],[10],[-2],[-8],[3],[-10],[-6],[5],[-4],[-8],[-5],[1],[3],[10],[-10],[-10],[1],[-2],[-9],[1],[-8],[5],[10],[6],[4],[-3],[10],[-5],[-7],[-10],[-9],[-10],[2],[-7],[-10],[1],[7],[-6],[5],[-3],[7],[-8],[-1],[7],[-7],[9],[-9],[8],[8],[-10],[-2],[-10],[6],[-10],[-7],[10],[8],[-10],[-10],[-8],[-4],[-2],[-7],[6],[-8],[6],[9],[10],[2],[-6],[2],[3],[-3],[-8],[-10],[1],[5],[-8],[-6],[8],[1],[3],[-9],[-7],[3],[-2],[-1],[-5],[-9],[-9],[-1],[-4],[-4],[1],[-9],[3],[4],[-1],[-8],[-6],[2],[-8],[-2],[-9],[-5],[-10],[9],[-5],[6],[-2],[-6],[4],[10],[4],[4],[1],[-7],[-6],[1],[2],[4],[-4],[-5],[5],[-4],[8],[-3],[-9],[10],[10],[-3],[-7],[-9],[3],[-10],[6],[6],[8],[-9],[-7],[-3],[5],[9],[-8],[-9],[-2],[-9],[-5],[4],[8],[3],[-10],[4],[-10],[-3],[7],[2],[-2],[8],[-2],[8],[9],[3],[-6],[2],[-4],[10],[3],[4],[-8],[-10],[4],[9],[-7],[-6],[1],[-2],[-1],[-6],[3],[3],[-2],[1],[-6],[9],[-3],[10],[-5],[5],[-5],[-8],[3],[9],[-5],[3],[5],[-5],[-8],[2],[-3],[-9],[-10],[-6],[-8],[-6],[10],[-1],[3],[10],[-7],[6],[-8],[6],[-9],[-1],[9],[-1],[-1],[-3],[-7],[-3],[-2],[3],[4],[-3],[-6],[-2],[-2],[-2],[9],[5],[5],[7],[4],[4],[1],[-2],[10],[8],[9],[-7],[-2],[1],[9],[9],[9],[6],[-10],[10],[4],[-7],[1],[-10],[3],[7],[1],[10],[4],[1],[7],[1],[-2],[9],[-9],[7],[-3],[10],[2],[-7],[8],[-8],[9],[-4],[9],[8],[3],[-1],[-6],[8],[1],[1],[-10],[10],[-1],[-8],[10],[-7],[5],[-3],[7],[10],[1],[-7],[-4],[-4],[-2],[1],[-8],[-5],[-5],[-7],[8],[5],[7],[8],[9],[6],[-1],[-7],[-9],[2],[-6],[5],[-1]], dtype = "int16")#candidate|11748|(512, 1)|const|int16
call_11747 = relay.TupleGetItem(func_8991_call(relay.reshape(const_11748.astype('int16'), [512,])), 0)
call_11749 = relay.TupleGetItem(func_8994_call(relay.reshape(const_11748.astype('int16'), [512,])), 0)
var_11753 = relay.var("var_11753", dtype = "int16", shape = (512, 12))#candidate|11753|(512, 12)|var|int16
bop_11754 = relay.divide(const_11748.astype('float64'), var_11753.astype('float64')) # shape=(512, 12)
func_5259_call = mod.get_global_var('func_5259')
func_5262_call = mutated_mod.get_global_var('func_5262')
var_11758 = relay.var("var_11758", dtype = "float32", shape = (6, 140))#candidate|11758|(6, 140)|var|float32
call_11757 = relay.TupleGetItem(func_5259_call(relay.reshape(var_11758.astype('float32'), [7, 10, 12])), 0)
call_11759 = relay.TupleGetItem(func_5262_call(relay.reshape(var_11758.astype('float32'), [7, 10, 12])), 0)
var_11773 = relay.var("var_11773", dtype = "int16", shape = (512, 12))#candidate|11773|(512, 12)|var|int16
bop_11774 = relay.add(var_11753.astype('float64'), relay.reshape(var_11773.astype('float64'), relay.shape_of(var_11753))) # shape=(512, 12)
var_11807 = relay.var("var_11807", dtype = "int16", shape = (512, 12))#candidate|11807|(512, 12)|var|int16
bop_11808 = relay.bitwise_xor(var_11773.astype('int8'), relay.reshape(var_11807.astype('int8'), relay.shape_of(var_11773))) # shape=(512, 12)
func_6711_call = mod.get_global_var('func_6711')
func_6712_call = mutated_mod.get_global_var('func_6712')
call_11819 = func_6711_call()
call_11820 = func_6711_call()
output = relay.Tuple([call_11691,call_11711,var_11712,var_11713,call_11718,call_11733,call_11747,bop_11754,call_11757,var_11758,bop_11774,bop_11808,call_11819,])
output2 = relay.Tuple([call_11692,call_11714,var_11712,var_11713,call_11719,call_11734,call_11749,bop_11754,call_11759,var_11758,bop_11774,bop_11808,call_11820,])
func_11824 = relay.Function([var_11712,var_11713,var_11753,var_11758,var_11773,var_11807,], output)
mod['func_11824'] = func_11824
mod = relay.transform.InferType()(mod)
var_11825 = relay.var("var_11825", dtype = "uint32", shape = ())#candidate|11825|()|var|uint32
var_11826 = relay.var("var_11826", dtype = "uint32", shape = (12,))#candidate|11826|(12,)|var|uint32
var_11827 = relay.var("var_11827", dtype = "int16", shape = (512, 12))#candidate|11827|(512, 12)|var|int16
var_11828 = relay.var("var_11828", dtype = "float32", shape = (6, 140))#candidate|11828|(6, 140)|var|float32
var_11829 = relay.var("var_11829", dtype = "int16", shape = (512, 12))#candidate|11829|(512, 12)|var|int16
var_11830 = relay.var("var_11830", dtype = "int16", shape = (512, 12))#candidate|11830|(512, 12)|var|int16
output = func_11824(var_11825,var_11826,var_11827,var_11828,var_11829,var_11830,)
func_11831 = relay.Function([var_11825,var_11826,var_11827,var_11828,var_11829,var_11830,], output)
mutated_mod['func_11831'] = func_11831
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5369_call = mod.get_global_var('func_5369')
func_5371_call = mutated_mod.get_global_var('func_5371')
call_11911 = relay.TupleGetItem(func_5369_call(), 0)
call_11912 = relay.TupleGetItem(func_5371_call(), 0)
output = relay.Tuple([call_11911,])
output2 = relay.Tuple([call_11912,])
func_11935 = relay.Function([], output)
mod['func_11935'] = func_11935
mod = relay.transform.InferType()(mod)
output = func_11935()
func_11936 = relay.Function([], output)
mutated_mod['func_11936'] = func_11936
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8697_call = mod.get_global_var('func_8697')
func_8698_call = mutated_mod.get_global_var('func_8698')
call_11943 = relay.TupleGetItem(func_8697_call(), 0)
call_11944 = relay.TupleGetItem(func_8698_call(), 0)
uop_11952 = relay.atan(call_11943.astype('float32')) # shape=(4, 28)
uop_11954 = relay.atan(call_11944.astype('float32')) # shape=(4, 28)
uop_11960 = relay.acosh(call_11943.astype('float64')) # shape=(4, 28)
uop_11962 = relay.acosh(call_11944.astype('float64')) # shape=(4, 28)
func_4108_call = mod.get_global_var('func_4108')
func_4109_call = mutated_mod.get_global_var('func_4109')
call_11976 = func_4108_call()
call_11977 = func_4108_call()
func_9076_call = mod.get_global_var('func_9076')
func_9077_call = mutated_mod.get_global_var('func_9077')
call_11985 = func_9076_call()
call_11986 = func_9076_call()
func_3483_call = mod.get_global_var('func_3483')
func_3485_call = mutated_mod.get_global_var('func_3485')
call_12000 = relay.TupleGetItem(func_3483_call(), 0)
call_12001 = relay.TupleGetItem(func_3485_call(), 0)
func_7317_call = mod.get_global_var('func_7317')
func_7318_call = mutated_mod.get_global_var('func_7318')
call_12004 = relay.TupleGetItem(func_7317_call(), 0)
call_12005 = relay.TupleGetItem(func_7318_call(), 0)
func_3332_call = mod.get_global_var('func_3332')
func_3335_call = mutated_mod.get_global_var('func_3335')
call_12025 = relay.TupleGetItem(func_3332_call(relay.reshape(call_11985.astype('float32'), [78, 6])), 4)
call_12026 = relay.TupleGetItem(func_3335_call(relay.reshape(call_11985.astype('float32'), [78, 6])), 4)
func_7339_call = mod.get_global_var('func_7339')
func_7341_call = mutated_mod.get_global_var('func_7341')
call_12027 = func_7339_call()
call_12028 = func_7339_call()
func_10662_call = mod.get_global_var('func_10662')
func_10663_call = mutated_mod.get_global_var('func_10663')
call_12031 = func_10662_call()
call_12032 = func_10662_call()
func_5570_call = mod.get_global_var('func_5570')
func_5572_call = mutated_mod.get_global_var('func_5572')
call_12035 = relay.TupleGetItem(func_5570_call(), 0)
call_12036 = relay.TupleGetItem(func_5572_call(), 0)
output = relay.Tuple([uop_11952,uop_11960,call_11976,call_11985,call_12000,call_12004,call_12025,call_12027,call_12031,call_12035,])
output2 = relay.Tuple([uop_11954,uop_11962,call_11977,call_11986,call_12001,call_12005,call_12026,call_12028,call_12032,call_12036,])
func_12037 = relay.Function([], output)
mod['func_12037'] = func_12037
mod = relay.transform.InferType()(mod)
mutated_mod['func_12037'] = func_12037
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12037_call = mutated_mod.get_global_var('func_12037')
call_12038 = func_12037_call()
output = call_12038
func_12039 = relay.Function([], output)
mutated_mod['func_12039'] = func_12039
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4464_call = mod.get_global_var('func_4464')
func_4465_call = mutated_mod.get_global_var('func_4465')
call_12046 = func_4464_call()
call_12047 = func_4464_call()
output = call_12046
output2 = call_12047
func_12051 = relay.Function([], output)
mod['func_12051'] = func_12051
mod = relay.transform.InferType()(mod)
output = func_12051()
func_12052 = relay.Function([], output)
mutated_mod['func_12052'] = func_12052
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6879_call = mod.get_global_var('func_6879')
func_6881_call = mutated_mod.get_global_var('func_6881')
call_12065 = relay.TupleGetItem(func_6879_call(), 0)
call_12066 = relay.TupleGetItem(func_6881_call(), 0)
output = relay.Tuple([call_12065,])
output2 = relay.Tuple([call_12066,])
func_12071 = relay.Function([], output)
mod['func_12071'] = func_12071
mod = relay.transform.InferType()(mod)
mutated_mod['func_12071'] = func_12071
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12071_call = mutated_mod.get_global_var('func_12071')
call_12072 = func_12071_call()
output = call_12072
func_12073 = relay.Function([], output)
mutated_mod['func_12073'] = func_12073
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12071_call = mod.get_global_var('func_12071')
func_12073_call = mutated_mod.get_global_var('func_12073')
call_12079 = relay.TupleGetItem(func_12071_call(), 0)
call_12080 = relay.TupleGetItem(func_12073_call(), 0)
func_7915_call = mod.get_global_var('func_7915')
func_7917_call = mutated_mod.get_global_var('func_7917')
call_12100 = func_7915_call()
call_12101 = func_7915_call()
func_2967_call = mod.get_global_var('func_2967')
func_2968_call = mutated_mod.get_global_var('func_2968')
call_12110 = relay.TupleGetItem(func_2967_call(), 0)
call_12111 = relay.TupleGetItem(func_2968_call(), 0)
func_8268_call = mod.get_global_var('func_8268')
func_8273_call = mutated_mod.get_global_var('func_8273')
var_12120 = relay.var("var_12120", dtype = "uint64", shape = ())#candidate|12120|()|var|uint64
const_12121 = relay.const([-8,-9,-7,-7,2,3,9,-5,-5,6,-8,10,1,-7,8,7,-2,-4,-9,-3,-1,6,-10,6,7,-1,-8,2,-2,6,10,8,2,-1,5,3,-10,-3,-7,-6,-3,-1,8,2,-2,-2,6,4,-1,8,-1,-9,7,1,-3,2,4,6,-7,-3,-1,-1,6,2,2,-3,-2,-6,-6,-4,-6,4,-10,-5,1,7,-5,-8,6,8,1,-3,-8,1,-7,-3,-3,-6,-9,9,-9,1,-5,-4,-8,-10,-6,1,3,-7,9,7,7,5,4,-6,-10,-6,-6,7,3,-7,10,2,-2,-6,-9,10,-4,-1,-1,-1,4,6,-8,-7,10,-9,-2,4,9,4,10,-1,-1,5,1,-2,3,-6,3,-1,7,-3,-10,2,6,-5,-2,-3,1,4,3,-7,-4,-7,-8,1,-6,-4,-1,6,-4,6,-9,10,4,-4,-10,3,-3,2,-7,-7,-7,-1,-9,8,8,-1,2,9,-7,-4,3,2,8,-7,9,9,-7,6,9,-9,-9,-6,-4,-6,-7,10,8,5,-10,-2,-8,-8,-3,-1,10,3,-2,10,-3,1,-7,-9,-4,2,9,-2,-6,10,-5,-6,-10,-6,-8,-2,-3,3,1,6,6,-9,5,-2,2,-2,2,5,5,-6,-6,-3,1,-8,10,10,-5,1,-10,2,-6,2,2,-1,7,-9,-8,-1,-10,1,-6,-6,-10,2,1,-4,8,-2,-1,5,-10,8,-9,-7,9,-9,-1,-5,-1,10,1,-6,8,-9,-2,-7,-1,2,-6,-10,-9,10,-1,10,4,-3,-6,5,-10,-4,-9,5,-8,1,-8,-8,10,-6,5,-3,7,-5,9,-6,-4,-1,3,-4,-5,-4,-8,7,-10,-8,-8,-5,1,8,2,6,6,1,-5,10,-4,10,-7,-9,-1,-4,-10,-4,3,-10,7,2,-5,-7,-10,8,-1,7,9,-9,-4,9,-3,6,6,10,-2,-9,5,-7,4,2,-6,-5,6,-5,-6,6,-5,7,8,7,10,-9,3,-4,1,-2,5,-4,-1,1,3,-1,10,2,-7,-8,-4,-6,2,3,5,4,5,3,9,7,1,-2,6,-1,-2,2,5,-4,5,2,-3,2,-4,-5,-8,5,-10,2,-9,-9,-1,9,-6,-3,-8,-2,1,2,8,-8,-8,6,10,-4,-9,1,5,-6,-3,-3,-5,-6,9,-4,3,-1,-7,-1,-5,7,9,5,-10,-4,-1,-5,-1,5,-7,9,10,-3,9,3,10,-7,2,4,5,6,-4,-4,-10,-9,7,10,-9,6,8,1,1,-8,2,-4,1,-2,-1,-2,-7,-9,-10,-6,2,5,1,-10,4,5,2,-10,9,8,2,10,-2,6,10,8,-3,-1,-9,-7,9,-8,1,-3,-3,10,-10,5,-1,-1,2,-2,2,-9,6,-5,-10,-7,-2,3,1,9,6,-1,-4,10,4,2,5,7,9,-8,5,-2,-4,-2,-8,6,4,3,-2,5,4,1,3,1,-2,-1,-4,5,7,5,-8,-9,10,2,4,-7,-9,8,-6,3,9,4,8,3,7,-1,9,-7,4,1,1,8,4,-1,6,8,-10,1,2,-5,2,-3,-8,1,4,-3,8,4,-7,2,-10,1,5,-2,-5,-5,1,-9,-8,2,-2,6,6,4,8,-9,8,-2,1,9,9,5,2,10,6,-4,6,-10,2,6,-10,10,-4,-1,6,-10,-4,4,3,-5,-7,7,1,-6,9,-4,-8,7,9,-6,7,-8,3,4,6,-4,2,-6,9,5,5,-7,6,-4,3,9,-6,-9,-9,-4,4,-7,9,9,-7,-6,-8,7,8,-8,-1,-10,-4,-5,-4,7,9,6,9,-4,2,3,4,3,-1,-6,9,-1,-5,-3,7,8,-8,-4,10,5,9,-1,10,-8,4,-5,-9,6,-3,2,-1,-6,3,-7,-9,4,-2,4,8,3,5,6,2,-8,1,7,-10,-4,-4,-7,-3,2,7,-9,9,10,-10,7,-8,-9,7,-4,8,2,-9,6,2,-9,-7,8,10,9,4,-4,-1,3,8,4,7,9,-7,-8,-6,-9,-5,8,-5,-7,-2,-1,-3,-2,-6,-6,-4,-7,-3,-9,-3,-1,-5,6,-3,9,4,-10,-8,8,9,-5,1,4,-8,-3,1,-1,-3,8,-2,3,9,-4,4,-9,8,-5,-7,-4,-2,-7,-1,1,7,-1,-6,-6,-8,2,-4,6,-6,-10,-10,1,1,6,8,7,-5,-6,-1,-6,5,-10,10,1,-8,10,-5,-1,8,-8,5,2,2,-2,10,-3,-7,-4,-2,4,5,-8,-4,-7,-8,-1,-10,2,-10,-8,-4,7,-7,-10,-7,-9,-8,-5,7,7,8,-6,-2,2,-5,-6,5,-4,-6,3,9,-8,-8,1,4,1,-7,-10,-7,3,-7,3,-2,-6,1,2,1,9,2,5,8,-7,4,4,-2,-3,5,10,-5,6,8,-6,-7,-8,-4,4,-10,-7,-8,6,-7,10,-5,9,-9,-5,-2,-3,7,9,-6,-1,4,1,-10,-4,5,9,4,-9,-3,-9,-7,-6,-6,4,-8,10,-5,-5,-7,-4,-5,-4,2,-4,-10,-2,7,-3,-2,9,-4,-1,-2,-5,-7,3,3,3,-1,-10,9,-9,-1,3,1,-3,-1,-5,-3,3,-1,-4,-4,-8,3,7,4,-2,10,6,7,6,4,-2,4,-8,10,7,-8,-10,-5,-5,-4,-3,2,6,1,-9,5,-3,-7,-2,-5,-2,6,-6,-8,1,9,6,5,3,8,-10,-5,2,6,-8,4,3,-9,-4,-1,-9,-1,4,-9,-10,10,9,-5,-5,6,-1,1,-4,-5,9,3,8,3,8,8,-10,-1,2,-4,8,-10,2,-5,4,-3,7,1,10,5,9,-7,2,1,-4,10,-5,-3,2,1,9,10,-2,1,-8,-9,2,7,-5,-5,-3,1,5,-5,3,4,-2,7,-7,5,5,-2,1,10,-10,-5,9,-3,1,3,5,-5,4,-10,-8,-6,-10,-1,-10,9,5,-4,-3,1,4,7,3,-6,-3,10,3,6,4,6,-6,3,10,-6,-4,-6,-2,8,8,4,10,3,-10,7,-6,-8,-10,6,10,-5,-10,5,-8,9,6,-5,7,-2,-9,-1,-3,-9,-3,5,6,10,-10,8,-7,-2,-10,3,-7,6,-3,-10,9,-9,2,-6,1,2,8,-9,-7,-9,-8,-8,-7,-10,1,-7,7,3,-10,-8,4,2,4,-8,-2,9,1,-6,2,-1,6,-5,3,-4,6,2,4,3,-7,8,-10,-1,6,3,5,-1,9,-4,4,5,-8,2,-3,1,-6,9,-7,8,10,-1,5,-4,10,7,3,-5,-9,6,-10,1,-5,-3,-1,-6,-4,5,-1,-4,-6,4,-2,-2,-6,4,5], dtype = "uint64")#candidate|12121|(1280,)|const|uint64
var_12122 = relay.var("var_12122", dtype = "int64", shape = (1080,))#candidate|12122|(1080,)|var|int64
call_12119 = relay.TupleGetItem(func_8268_call(relay.reshape(var_12120.astype('uint64'), []), relay.reshape(const_12121.astype('uint64'), [16, 8, 10]), relay.reshape(call_12100.astype('float32'), [468,]), relay.reshape(var_12122.astype('int64'), [1080,]), ), 2)
call_12123 = relay.TupleGetItem(func_8273_call(relay.reshape(var_12120.astype('uint64'), []), relay.reshape(const_12121.astype('uint64'), [16, 8, 10]), relay.reshape(call_12100.astype('float32'), [468,]), relay.reshape(var_12122.astype('int64'), [1080,]), ), 2)
func_10030_call = mod.get_global_var('func_10030')
func_10031_call = mutated_mod.get_global_var('func_10031')
call_12129 = relay.TupleGetItem(func_10030_call(), 1)
call_12130 = relay.TupleGetItem(func_10031_call(), 1)
func_11306_call = mod.get_global_var('func_11306')
func_11309_call = mutated_mod.get_global_var('func_11309')
const_12133 = relay.const([[-9.087224,-7.913700,-5.898349,-5.459015,8.116783,-3.299569],[-3.728964,-8.718546,-1.689414,-9.919593,1.147042,-4.121515],[6.053053,0.633240,7.574196,5.185908,-8.749362,8.974498],[-1.348235,-1.112893,-7.650993,-6.005708,-5.984244,9.065232],[-9.798728,-9.576247,2.831167,-1.549440,-1.275910,5.893767],[1.907332,-4.396423,-2.675339,7.260986,2.888733,-2.531969],[-1.730571,3.164246,0.834494,7.860054,-9.107262,-8.155521],[4.070330,-1.911081,-6.518151,7.357729,-7.697081,5.323593],[7.056408,-8.811981,-8.969185,-0.378837,1.303371,2.530512],[-4.131516,-3.274541,-2.297496,-0.346948,9.617812,-2.528778],[-4.067962,-2.104941,8.359054,7.245277,-1.489622,7.352976],[4.247439,3.598413,6.907161,3.901206,6.532687,-5.681290],[-4.489077,7.850450,2.240019,-1.888445,2.476858,2.158964],[-2.178096,3.458276,-1.485614,-7.819173,-0.201610,-9.924795],[-7.347613,9.231255,-2.468613,-3.242852,5.028727,-5.242058],[5.154164,-8.499861,1.589424,2.667602,5.919320,-3.116711],[2.220029,1.929054,-7.673107,-5.929806,0.956476,2.712784],[0.396017,5.379598,5.173642,-6.368786,-7.838076,-4.143250],[-6.336716,7.884528,-4.395372,3.172731,-0.967545,-4.812753],[-4.823215,-8.886784,-8.755083,4.923946,6.299583,-0.614737],[3.796228,2.125610,-5.546955,8.477594,3.661975,-1.825063],[5.373158,6.696297,-3.672484,-6.014577,-9.464888,-0.143681],[-6.176750,8.425223,-5.106690,2.192499,-7.651260,6.272056],[-3.237151,1.573516,-7.133357,6.338528,4.560241,4.477468],[-2.224265,-8.340217,-3.298849,-3.740800,9.781615,-2.441180],[9.712626,1.542455,-5.501777,-3.727337,1.720633,-7.002205],[0.122809,3.889148,0.663550,-0.785911,5.044126,-8.995503],[-8.338332,-9.918851,-7.942264,0.106143,-8.256554,8.486500],[-7.705324,8.679140,1.215240,4.135458,-2.134799,5.014843],[0.296015,7.492103,8.619930,6.631929,-3.390588,3.170813],[-1.547090,7.182745,8.949829,-7.336685,-7.375235,5.848799],[1.180474,7.502821,-9.993319,6.586712,-6.899045,-9.637446],[9.879389,1.975163,3.792606,-9.032953,-2.976552,0.221729],[8.114635,4.656081,4.858494,8.234554,3.143928,-0.275347],[-0.129148,7.074535,5.869504,-7.779177,1.979598,-4.966478],[-6.215309,3.018109,-0.022588,-5.219775,-6.256116,-0.778511],[-7.394581,-3.944233,-2.895320,9.635881,0.005169,6.659066],[-7.634391,5.059062,-0.837854,0.621088,-7.154493,4.268991],[8.034539,-2.937034,4.830011,7.056880,6.290895,1.680253],[9.625648,-6.175085,0.326845,6.970018,1.210938,-1.499999],[-5.304104,-6.015849,-6.179017,-7.512770,8.059136,6.382200],[7.815973,-5.144130,-3.578225,-9.475869,6.353028,-5.730295],[-8.256209,-3.716673,-0.056617,5.985221,-9.054230,-9.246340],[3.044494,-7.590226,4.420274,1.850020,3.874054,0.503652],[0.651295,1.160492,-7.114744,-7.915461,0.246664,-0.692486],[4.344323,-4.522925,0.852874,-2.401001,7.546033,7.736908],[-5.187432,8.314553,3.757057,7.037248,-9.445336,8.604570],[0.971538,-3.676073,-9.286526,-5.539163,-6.615316,-6.884986],[4.621476,6.921398,7.831562,-0.565809,5.366000,8.001895],[-7.131114,-4.139303,7.253940,-0.745312,6.111715,3.405714],[4.077778,2.561249,9.143517,-4.934000,-5.765481,3.134895],[-9.372346,4.868101,-5.878425,-3.068370,4.037934,5.705405],[-6.313963,8.378682,-1.112768,-2.270533,8.146238,-0.830715],[4.587111,4.004212,-7.375618,4.633575,-3.899307,-0.233317],[-5.977666,-8.971142,3.740023,-0.646185,5.750670,7.465324]], dtype = "float32")#candidate|12133|(55, 6)|const|float32
call_12132 = relay.TupleGetItem(func_11306_call(relay.reshape(const_12133.astype('float32'), [2, 11, 15])), 0)
call_12134 = relay.TupleGetItem(func_11309_call(relay.reshape(const_12133.astype('float32'), [2, 11, 15])), 0)
output = relay.Tuple([call_12079,call_12100,call_12110,call_12119,var_12120,const_12121,var_12122,call_12129,call_12132,const_12133,])
output2 = relay.Tuple([call_12080,call_12101,call_12111,call_12123,var_12120,const_12121,var_12122,call_12130,call_12134,const_12133,])
func_12139 = relay.Function([var_12120,var_12122,], output)
mod['func_12139'] = func_12139
mod = relay.transform.InferType()(mod)
mutated_mod['func_12139'] = func_12139
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12139_call = mutated_mod.get_global_var('func_12139')
var_12141 = relay.var("var_12141", dtype = "uint64", shape = ())#candidate|12141|()|var|uint64
var_12142 = relay.var("var_12142", dtype = "int64", shape = (1080,))#candidate|12142|(1080,)|var|int64
call_12140 = func_12139_call(var_12141,var_12142,)
output = call_12140
func_12143 = relay.Function([var_12141,var_12142,], output)
mutated_mod['func_12143'] = func_12143
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5723_call = mod.get_global_var('func_5723')
func_5725_call = mutated_mod.get_global_var('func_5725')
call_12163 = relay.TupleGetItem(func_5723_call(), 0)
call_12164 = relay.TupleGetItem(func_5725_call(), 0)
func_10616_call = mod.get_global_var('func_10616')
func_10618_call = mutated_mod.get_global_var('func_10618')
call_12181 = relay.TupleGetItem(func_10616_call(), 0)
call_12182 = relay.TupleGetItem(func_10618_call(), 0)
output = relay.Tuple([call_12163,call_12181,])
output2 = relay.Tuple([call_12164,call_12182,])
func_12184 = relay.Function([], output)
mod['func_12184'] = func_12184
mod = relay.transform.InferType()(mod)
output = func_12184()
func_12185 = relay.Function([], output)
mutated_mod['func_12185'] = func_12185
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6721_call = mod.get_global_var('func_6721')
func_6722_call = mutated_mod.get_global_var('func_6722')
call_12373 = func_6721_call()
call_12374 = func_6721_call()
func_6300_call = mod.get_global_var('func_6300')
func_6302_call = mutated_mod.get_global_var('func_6302')
call_12377 = relay.TupleGetItem(func_6300_call(), 0)
call_12378 = relay.TupleGetItem(func_6302_call(), 0)
output = relay.Tuple([call_12373,call_12377,])
output2 = relay.Tuple([call_12374,call_12378,])
func_12407 = relay.Function([], output)
mod['func_12407'] = func_12407
mod = relay.transform.InferType()(mod)
mutated_mod['func_12407'] = func_12407
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12407_call = mutated_mod.get_global_var('func_12407')
call_12408 = func_12407_call()
output = call_12408
func_12409 = relay.Function([], output)
mutated_mod['func_12409'] = func_12409
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7224_call = mod.get_global_var('func_7224')
func_7226_call = mutated_mod.get_global_var('func_7226')
call_12448 = relay.TupleGetItem(func_7224_call(), 0)
call_12449 = relay.TupleGetItem(func_7226_call(), 0)
func_3194_call = mod.get_global_var('func_3194')
func_3195_call = mutated_mod.get_global_var('func_3195')
call_12452 = func_3194_call()
call_12453 = func_3194_call()
func_6065_call = mod.get_global_var('func_6065')
func_6067_call = mutated_mod.get_global_var('func_6067')
call_12456 = relay.TupleGetItem(func_6065_call(), 1)
call_12457 = relay.TupleGetItem(func_6067_call(), 1)
func_10102_call = mod.get_global_var('func_10102')
func_10103_call = mutated_mod.get_global_var('func_10103')
call_12461 = relay.TupleGetItem(func_10102_call(), 0)
call_12462 = relay.TupleGetItem(func_10103_call(), 0)
func_6879_call = mod.get_global_var('func_6879')
func_6881_call = mutated_mod.get_global_var('func_6881')
call_12471 = relay.TupleGetItem(func_6879_call(), 0)
call_12472 = relay.TupleGetItem(func_6881_call(), 0)
func_11267_call = mod.get_global_var('func_11267')
func_11269_call = mutated_mod.get_global_var('func_11269')
call_12474 = relay.TupleGetItem(func_11267_call(), 1)
call_12475 = relay.TupleGetItem(func_11269_call(), 1)
output = relay.Tuple([call_12448,call_12452,call_12456,call_12461,call_12471,call_12474,])
output2 = relay.Tuple([call_12449,call_12453,call_12457,call_12462,call_12472,call_12475,])
func_12505 = relay.Function([], output)
mod['func_12505'] = func_12505
mod = relay.transform.InferType()(mod)
mutated_mod['func_12505'] = func_12505
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12505_call = mutated_mod.get_global_var('func_12505')
call_12506 = func_12505_call()
output = call_12506
func_12507 = relay.Function([], output)
mutated_mod['func_12507'] = func_12507
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12538 = relay.var("var_12538", dtype = "uint32", shape = (2, 12, 8))#candidate|12538|(2, 12, 8)|var|uint32
var_12539 = relay.var("var_12539", dtype = "uint32", shape = (2, 12, 8))#candidate|12539|(2, 12, 8)|var|uint32
bop_12540 = relay.bitwise_or(var_12538.astype('uint32'), relay.reshape(var_12539.astype('uint32'), relay.shape_of(var_12538))) # shape=(2, 12, 8)
func_5170_call = mod.get_global_var('func_5170')
func_5172_call = mutated_mod.get_global_var('func_5172')
call_12545 = func_5170_call()
call_12546 = func_5170_call()
func_12407_call = mod.get_global_var('func_12407')
func_12409_call = mutated_mod.get_global_var('func_12409')
call_12547 = relay.TupleGetItem(func_12407_call(), 0)
call_12548 = relay.TupleGetItem(func_12409_call(), 0)
output = relay.Tuple([bop_12540,call_12545,call_12547,])
output2 = relay.Tuple([bop_12540,call_12546,call_12548,])
func_12559 = relay.Function([var_12538,var_12539,], output)
mod['func_12559'] = func_12559
mod = relay.transform.InferType()(mod)
mutated_mod['func_12559'] = func_12559
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12559_call = mutated_mod.get_global_var('func_12559')
var_12561 = relay.var("var_12561", dtype = "uint32", shape = (2, 12, 8))#candidate|12561|(2, 12, 8)|var|uint32
var_12562 = relay.var("var_12562", dtype = "uint32", shape = (2, 12, 8))#candidate|12562|(2, 12, 8)|var|uint32
call_12560 = func_12559_call(var_12561,var_12562,)
output = call_12560
func_12563 = relay.Function([var_12561,var_12562,], output)
mutated_mod['func_12563'] = func_12563
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12625 = relay.var("var_12625", dtype = "int32", shape = ())#candidate|12625|()|var|int32
var_12626 = relay.var("var_12626", dtype = "int32", shape = (13, 8, 12))#candidate|12626|(13, 8, 12)|var|int32
bop_12627 = relay.logical_xor(var_12625.astype('int32'), var_12626.astype('int32')) # shape=(13, 8, 12)
func_6237_call = mod.get_global_var('func_6237')
func_6240_call = mutated_mod.get_global_var('func_6240')
var_12647 = relay.var("var_12647", dtype = "float64", shape = (5, 63))#candidate|12647|(5, 63)|var|float64
call_12646 = relay.TupleGetItem(func_6237_call(relay.reshape(var_12647.astype('float64'), [315,])), 2)
call_12648 = relay.TupleGetItem(func_6240_call(relay.reshape(var_12647.astype('float64'), [315,])), 2)
output = relay.Tuple([bop_12627,call_12646,var_12647,])
output2 = relay.Tuple([bop_12627,call_12648,var_12647,])
func_12666 = relay.Function([var_12625,var_12626,var_12647,], output)
mod['func_12666'] = func_12666
mod = relay.transform.InferType()(mod)
mutated_mod['func_12666'] = func_12666
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12666_call = mutated_mod.get_global_var('func_12666')
var_12668 = relay.var("var_12668", dtype = "int32", shape = ())#candidate|12668|()|var|int32
var_12669 = relay.var("var_12669", dtype = "int32", shape = (13, 8, 12))#candidate|12669|(13, 8, 12)|var|int32
var_12670 = relay.var("var_12670", dtype = "float64", shape = (5, 63))#candidate|12670|(5, 63)|var|float64
call_12667 = func_12666_call(var_12668,var_12669,var_12670,)
output = call_12667
func_12671 = relay.Function([var_12668,var_12669,var_12670,], output)
mutated_mod['func_12671'] = func_12671
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8878_call = mod.get_global_var('func_8878')
func_8879_call = mutated_mod.get_global_var('func_8879')
call_12724 = relay.TupleGetItem(func_8878_call(), 0)
call_12725 = relay.TupleGetItem(func_8879_call(), 0)
func_8908_call = mod.get_global_var('func_8908')
func_8911_call = mutated_mod.get_global_var('func_8911')
const_12738 = relay.const([-6.473577,-7.241523,-5.871124,2.348527,-6.782729,9.687122,-7.065059,-7.814292,0.530449,-9.986053,8.619902,-5.323394,6.503224,-7.118709,-6.716885,3.320634,9.268604,4.312745,9.503653,6.495864,9.992708,2.624866,9.209074,6.179815,-4.890077,-7.305396,-9.845403,-1.701131,-4.895837,-9.207689,5.375513,-6.143829,6.360091,-1.371361,-9.058455,9.937794,-4.279624,4.208381,-3.281159,-1.891430,-8.762415,-6.211446,6.976694,-5.151710,6.009432,9.354839,9.574113,5.556416,3.882141,9.801183,-7.322991,4.464072,5.541784,-9.458898,9.473245,0.140845,6.572308,-1.625555,-0.744575,-1.980548,1.763218,-6.801061,6.817534,-8.555028,-3.030812,4.614148,-6.190046,4.886701,9.179810,9.601531,2.459082,5.650810,-7.986080,4.471652,-3.944020,2.878034,4.445737,-5.829472,6.085350,7.876247,8.234079,-8.567129,-1.622821,4.441246,2.845169,-9.074807,8.223746,3.796759,-8.610021,1.542174,0.802221,-6.777675,-3.357470,8.087686,1.011835,6.781113,0.089259,-6.900742,-5.037693,-1.117933,-2.142310,-8.326571,-6.678917,-5.955382,-4.293708,7.500747,-9.354643,5.499501,0.440465,-6.343707,7.992870,0.691315,-3.122711,-7.775559,8.499770,-9.795731,-3.310983,-2.098916,1.289545,0.286559,-3.532302,8.153126,-1.156344,6.914022,8.246616,7.971563,-7.424525,-7.066097,-3.184640,5.514077,0.486421,-1.014951,-1.997568,-8.432284,1.250623,8.696953,-3.627653,-1.721372,2.805495,-6.658034,4.481207,-8.870508,-0.681677,-7.582379,3.862580,9.225468,-1.435262,-9.056114,-4.042417,-1.791762,-1.957960,8.342654,-6.344740,-5.937067,3.371290,-7.128390,-1.163383,-5.878298,0.123388,1.707700,-3.681262,2.927766,-4.917689,5.594977,-2.908858,-5.259858,-8.284206,-9.613609,2.028266,-8.011126,5.691761,-9.893069,1.373090,0.080810,5.685533,-4.123315,2.568385,-6.603206,9.040292,-8.311029,3.885113,9.632241,-6.925604,-9.538585,-1.797160,-2.171349,-0.204138,5.308913,-7.079965,-9.266419,3.115187,9.203556,2.541234,0.280366,-3.381535,-1.487586,-6.398035,2.837833,8.492814,4.570656,-2.009300,-9.690920,-2.992260,4.539850,-0.516370,-7.659093,-0.965078,-3.512419,-7.702375,-5.208211,4.247436,-9.473624,-5.864747,-1.713108,-0.554602,9.790429,2.085828,3.107427,2.162584,-5.469033,-7.894608,-2.803014,8.878875,-1.509663,-4.434429,-4.115198,-7.046087,1.758389,-7.434094,-6.676867,5.395718,0.452091,7.882927,-4.454970,7.509345,-0.907610,-4.053229,-0.324647,5.152891,5.285570,-7.200563,4.299783,-7.419645,1.456009,-8.935765,3.135247,-9.216688,6.644759,0.552656,-6.680775,-3.512665,5.648975,8.609640,-5.797816,-8.403041,-7.391510,7.643342,0.910281,2.528709,-4.549799,1.688952,3.218399,7.844695,9.670864,6.019646,5.784397,0.681625,-3.102915,3.463892,9.026179,-5.185950,-0.991070,-0.955636,7.470385,-5.603206,7.613600,-8.954377,1.852204,6.121722,-5.619605,8.792111,8.155275,-8.428824,2.525348,-9.799544,-3.556506,8.679814,3.576524], dtype = "float32")#candidate|12738|(288,)|const|float32
var_12739 = relay.var("var_12739", dtype = "bool", shape = (112,))#candidate|12739|(112,)|var|bool
call_12737 = relay.TupleGetItem(func_8908_call(relay.reshape(const_12738.astype('float32'), [288,]), relay.reshape(var_12739.astype('bool'), [4, 4, 7]), ), 2)
call_12740 = relay.TupleGetItem(func_8911_call(relay.reshape(const_12738.astype('float32'), [288,]), relay.reshape(var_12739.astype('bool'), [4, 4, 7]), ), 2)
output = relay.Tuple([call_12724,call_12737,const_12738,var_12739,])
output2 = relay.Tuple([call_12725,call_12740,const_12738,var_12739,])
func_12764 = relay.Function([var_12739,], output)
mod['func_12764'] = func_12764
mod = relay.transform.InferType()(mod)
mutated_mod['func_12764'] = func_12764
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12765 = relay.var("var_12765", dtype = "bool", shape = (112,))#candidate|12765|(112,)|var|bool
func_12764_call = mutated_mod.get_global_var('func_12764')
call_12766 = func_12764_call(var_12765)
output = call_12766
func_12767 = relay.Function([var_12765], output)
mutated_mod['func_12767'] = func_12767
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11158_call = mod.get_global_var('func_11158')
func_11160_call = mutated_mod.get_global_var('func_11160')
call_12783 = func_11158_call()
call_12784 = func_11158_call()
func_3385_call = mod.get_global_var('func_3385')
func_3388_call = mutated_mod.get_global_var('func_3388')
call_12798 = relay.TupleGetItem(func_3385_call(relay.reshape(call_12783.astype('float32'), [1, 288])), 2)
call_12799 = relay.TupleGetItem(func_3388_call(relay.reshape(call_12783.astype('float32'), [1, 288])), 2)
output = relay.Tuple([call_12783,call_12798,])
output2 = relay.Tuple([call_12784,call_12799,])
func_12809 = relay.Function([], output)
mod['func_12809'] = func_12809
mod = relay.transform.InferType()(mod)
output = func_12809()
func_12810 = relay.Function([], output)
mutated_mod['func_12810'] = func_12810
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12837 = relay.var("var_12837", dtype = "float64", shape = (2, 12, 6))#candidate|12837|(2, 12, 6)|var|float64
var_12838 = relay.var("var_12838", dtype = "float64", shape = (2, 12, 6))#candidate|12838|(2, 12, 6)|var|float64
bop_12839 = relay.floor_mod(var_12837.astype('float64'), relay.reshape(var_12838.astype('float64'), relay.shape_of(var_12837))) # shape=(2, 12, 6)
func_11404_call = mod.get_global_var('func_11404')
func_11405_call = mutated_mod.get_global_var('func_11405')
call_12844 = relay.TupleGetItem(func_11404_call(), 0)
call_12845 = relay.TupleGetItem(func_11405_call(), 0)
uop_12852 = relay.asin(var_12837.astype('float32')) # shape=(2, 12, 6)
func_6196_call = mod.get_global_var('func_6196')
func_6197_call = mutated_mod.get_global_var('func_6197')
call_12860 = relay.TupleGetItem(func_6196_call(), 0)
call_12861 = relay.TupleGetItem(func_6197_call(), 0)
output = relay.Tuple([bop_12839,call_12844,uop_12852,call_12860,])
output2 = relay.Tuple([bop_12839,call_12845,uop_12852,call_12861,])
func_12868 = relay.Function([var_12837,var_12838,], output)
mod['func_12868'] = func_12868
mod = relay.transform.InferType()(mod)
mutated_mod['func_12868'] = func_12868
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12868_call = mutated_mod.get_global_var('func_12868')
var_12870 = relay.var("var_12870", dtype = "float64", shape = (2, 12, 6))#candidate|12870|(2, 12, 6)|var|float64
var_12871 = relay.var("var_12871", dtype = "float64", shape = (2, 12, 6))#candidate|12871|(2, 12, 6)|var|float64
call_12869 = func_12868_call(var_12870,var_12871,)
output = call_12869
func_12872 = relay.Function([var_12870,var_12871,], output)
mutated_mod['func_12872'] = func_12872
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6847_call = mod.get_global_var('func_6847')
func_6849_call = mutated_mod.get_global_var('func_6849')
call_12907 = relay.TupleGetItem(func_6847_call(), 1)
call_12908 = relay.TupleGetItem(func_6849_call(), 1)
output = call_12907
output2 = call_12908
func_12914 = relay.Function([], output)
mod['func_12914'] = func_12914
mod = relay.transform.InferType()(mod)
output = func_12914()
func_12915 = relay.Function([], output)
mutated_mod['func_12915'] = func_12915
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10981_call = mod.get_global_var('func_10981')
func_10982_call = mutated_mod.get_global_var('func_10982')
call_13006 = relay.TupleGetItem(func_10981_call(), 0)
call_13007 = relay.TupleGetItem(func_10982_call(), 0)
func_8697_call = mod.get_global_var('func_8697')
func_8698_call = mutated_mod.get_global_var('func_8698')
call_13009 = relay.TupleGetItem(func_8697_call(), 0)
call_13010 = relay.TupleGetItem(func_8698_call(), 0)
func_2899_call = mod.get_global_var('func_2899')
func_2900_call = mutated_mod.get_global_var('func_2900')
call_13038 = relay.TupleGetItem(func_2899_call(), 1)
call_13039 = relay.TupleGetItem(func_2900_call(), 1)
func_7636_call = mod.get_global_var('func_7636')
func_7638_call = mutated_mod.get_global_var('func_7638')
call_13040 = relay.TupleGetItem(func_7636_call(), 0)
call_13041 = relay.TupleGetItem(func_7638_call(), 0)
output = relay.Tuple([call_13006,call_13009,call_13038,call_13040,])
output2 = relay.Tuple([call_13007,call_13010,call_13039,call_13041,])
func_13045 = relay.Function([], output)
mod['func_13045'] = func_13045
mod = relay.transform.InferType()(mod)
mutated_mod['func_13045'] = func_13045
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13045_call = mutated_mod.get_global_var('func_13045')
call_13046 = func_13045_call()
output = call_13046
func_13047 = relay.Function([], output)
mutated_mod['func_13047'] = func_13047
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7966_call = mod.get_global_var('func_7966')
func_7968_call = mutated_mod.get_global_var('func_7968')
call_13051 = relay.TupleGetItem(func_7966_call(), 0)
call_13052 = relay.TupleGetItem(func_7968_call(), 0)
output = relay.Tuple([call_13051,])
output2 = relay.Tuple([call_13052,])
func_13064 = relay.Function([], output)
mod['func_13064'] = func_13064
mod = relay.transform.InferType()(mod)
mutated_mod['func_13064'] = func_13064
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13064_call = mutated_mod.get_global_var('func_13064')
call_13065 = func_13064_call()
output = call_13065
func_13066 = relay.Function([], output)
mutated_mod['func_13066'] = func_13066
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4958_call = mod.get_global_var('func_4958')
func_4959_call = mutated_mod.get_global_var('func_4959')
call_13098 = func_4958_call()
call_13099 = func_4958_call()
output = relay.Tuple([call_13098,])
output2 = relay.Tuple([call_13099,])
func_13115 = relay.Function([], output)
mod['func_13115'] = func_13115
mod = relay.transform.InferType()(mod)
mutated_mod['func_13115'] = func_13115
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13115_call = mutated_mod.get_global_var('func_13115')
call_13116 = func_13115_call()
output = call_13116
func_13117 = relay.Function([], output)
mutated_mod['func_13117'] = func_13117
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6065_call = mod.get_global_var('func_6065')
func_6067_call = mutated_mod.get_global_var('func_6067')
call_13155 = relay.TupleGetItem(func_6065_call(), 0)
call_13156 = relay.TupleGetItem(func_6067_call(), 0)
output = call_13155
output2 = call_13156
func_13194 = relay.Function([], output)
mod['func_13194'] = func_13194
mod = relay.transform.InferType()(mod)
output = func_13194()
func_13195 = relay.Function([], output)
mutated_mod['func_13195'] = func_13195
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8411_call = mod.get_global_var('func_8411')
func_8413_call = mutated_mod.get_global_var('func_8413')
call_13272 = relay.TupleGetItem(func_8411_call(), 1)
call_13273 = relay.TupleGetItem(func_8413_call(), 1)
output = call_13272
output2 = call_13273
func_13274 = relay.Function([], output)
mod['func_13274'] = func_13274
mod = relay.transform.InferType()(mod)
output = func_13274()
func_13275 = relay.Function([], output)
mutated_mod['func_13275'] = func_13275
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4088_call = mod.get_global_var('func_4088')
func_4090_call = mutated_mod.get_global_var('func_4090')
call_13314 = relay.TupleGetItem(func_4088_call(), 1)
call_13315 = relay.TupleGetItem(func_4090_call(), 1)
func_6847_call = mod.get_global_var('func_6847')
func_6849_call = mutated_mod.get_global_var('func_6849')
call_13318 = relay.TupleGetItem(func_6847_call(), 1)
call_13319 = relay.TupleGetItem(func_6849_call(), 1)
func_12559_call = mod.get_global_var('func_12559')
func_12563_call = mutated_mod.get_global_var('func_12563')
const_13335 = relay.const([6,3,10,-9,4,-1,-7,6,3,-7,10,5,-9,-3,4,2,5,2,-3,-2,-8,3,-7,-7,6,-1,3,10,-8,6,-5,4,6,-5,-8,5,2,-3,8,1,-5,10,-10,-9,3,2,6,8,-5,-10,-2,9,4,4,4,-7,8,7,10,-8,-1,-3,-10,10,5,-6,-6,10,-7,-3,-10,9,10,7,2,-2,-6,4,5,-9,6,9,2,-6,-4,1,-9,-3,6,8,-5,-3,-7,-7,10,5,5,10,3,-6,4,2,-8,2,-5,4,-1,1,3,-10,-7,-9,-9,10,4,9,-3,-1,6,-7,-4,-10,-5,2,-2,8,-9,2,7,-8,-9,-7,5,-5,1,-3,10,-9,6,-2,-6,-6,9,-1,-1,5,5,2,10,-3,7,6,-9,10,-8,2,5,7,7,8,6,-5,9,-10,-3,2,9,7,4,-1,-10,-4,-10,-8,-10,4,4,-6,-7,2,1,1,-1,-8,-4,7,4,10,4,-3,-6,10], dtype = "uint32")#candidate|13335|(192,)|const|uint32
call_13334 = relay.TupleGetItem(func_12559_call(relay.reshape(const_13335.astype('uint32'), [2, 12, 8]), relay.reshape(const_13335.astype('uint32'), [2, 12, 8]), ), 2)
call_13336 = relay.TupleGetItem(func_12563_call(relay.reshape(const_13335.astype('uint32'), [2, 12, 8]), relay.reshape(const_13335.astype('uint32'), [2, 12, 8]), ), 2)
output = relay.Tuple([call_13314,call_13318,call_13334,const_13335,])
output2 = relay.Tuple([call_13315,call_13319,call_13336,const_13335,])
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
func_3859_call = mod.get_global_var('func_3859')
func_3861_call = mutated_mod.get_global_var('func_3861')
call_13345 = relay.TupleGetItem(func_3859_call(), 0)
call_13346 = relay.TupleGetItem(func_3861_call(), 0)
output = relay.Tuple([call_13345,])
output2 = relay.Tuple([call_13346,])
func_13347 = relay.Function([], output)
mod['func_13347'] = func_13347
mod = relay.transform.InferType()(mod)
output = func_13347()
func_13348 = relay.Function([], output)
mutated_mod['func_13348'] = func_13348
mutated_mod = relay.transform.InferType()(mutated_mod)
var_13356 = relay.var("var_13356", dtype = "uint8", shape = ())#candidate|13356|()|var|uint8
const_13357 = relay.const([[[-1],[-3],[7],[-8]],[[-7],[-5],[-8],[7]],[[-2],[9],[-2],[7]],[[5],[5],[8],[7]],[[4],[10],[-1],[8]],[[-9],[3],[7],[3]],[[6],[5],[-8],[-10]],[[-8],[-2],[2],[-6]],[[9],[-10],[4],[8]]], dtype = "uint8")#candidate|13357|(9, 4, 1)|const|uint8
bop_13358 = relay.logical_xor(var_13356.astype('uint8'), const_13357.astype('uint8')) # shape=(9, 4, 1)
func_10616_call = mod.get_global_var('func_10616')
func_10618_call = mutated_mod.get_global_var('func_10618')
call_13362 = relay.TupleGetItem(func_10616_call(), 0)
call_13363 = relay.TupleGetItem(func_10618_call(), 0)
bop_13368 = relay.maximum(call_13362.astype('uint8'), const_13357.astype('uint8')) # shape=(9, 4, 468)
bop_13371 = relay.maximum(call_13363.astype('uint8'), const_13357.astype('uint8')) # shape=(9, 4, 468)
bop_13373 = relay.multiply(bop_13358.astype('uint16'), bop_13368.astype('uint16')) # shape=(9, 4, 468)
bop_13376 = relay.multiply(bop_13358.astype('uint16'), bop_13371.astype('uint16')) # shape=(9, 4, 468)
func_9983_call = mod.get_global_var('func_9983')
func_9984_call = mutated_mod.get_global_var('func_9984')
call_13382 = relay.TupleGetItem(func_9983_call(), 2)
call_13383 = relay.TupleGetItem(func_9984_call(), 2)
uop_13388 = relay.erf(bop_13373.astype('float64')) # shape=(9, 4, 468)
uop_13390 = relay.erf(bop_13376.astype('float64')) # shape=(9, 4, 468)
func_5914_call = mod.get_global_var('func_5914')
func_5918_call = mutated_mod.get_global_var('func_5918')
call_13399 = relay.TupleGetItem(func_5914_call(relay.reshape(call_13382.astype('float32'), [11, 2, 10]), relay.reshape(call_13382.astype('float32'), [11, 2, 10]), ), 0)
call_13400 = relay.TupleGetItem(func_5918_call(relay.reshape(call_13382.astype('float32'), [11, 2, 10]), relay.reshape(call_13382.astype('float32'), [11, 2, 10]), ), 0)
output = relay.Tuple([call_13382,uop_13388,call_13399,])
output2 = relay.Tuple([call_13383,uop_13390,call_13400,])
func_13401 = relay.Function([var_13356,], output)
mod['func_13401'] = func_13401
mod = relay.transform.InferType()(mod)
var_13402 = relay.var("var_13402", dtype = "uint8", shape = ())#candidate|13402|()|var|uint8
output = func_13401(var_13402)
func_13403 = relay.Function([var_13402], output)
mutated_mod['func_13403'] = func_13403
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7855_call = mod.get_global_var('func_7855')
func_7856_call = mutated_mod.get_global_var('func_7856')
call_13415 = relay.TupleGetItem(func_7855_call(), 0)
call_13416 = relay.TupleGetItem(func_7856_call(), 0)
output = call_13415
output2 = call_13416
func_13429 = relay.Function([], output)
mod['func_13429'] = func_13429
mod = relay.transform.InferType()(mod)
mutated_mod['func_13429'] = func_13429
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13429_call = mutated_mod.get_global_var('func_13429')
call_13430 = func_13429_call()
output = call_13430
func_13431 = relay.Function([], output)
mutated_mod['func_13431'] = func_13431
mutated_mod = relay.transform.InferType()(mutated_mod)
const_13520 = relay.const(-1.804373, dtype = "float32")#candidate|13520|()|const|float32
const_13521 = relay.const([[[-5.092662],[4.770672],[0.422310]],[[5.563379],[4.517992],[-9.940196]],[[9.682514],[5.730345],[-9.699730]]], dtype = "float32")#candidate|13521|(3, 3, 1)|const|float32
bop_13522 = relay.floor_mod(const_13520.astype('float32'), const_13521.astype('float32')) # shape=(3, 3, 1)
bop_13529 = relay.multiply(const_13521.astype('uint64'), const_13520.astype('uint64')) # shape=(3, 3, 1)
output = relay.Tuple([bop_13522,bop_13529,])
output2 = relay.Tuple([bop_13522,bop_13529,])
func_13534 = relay.Function([], output)
mod['func_13534'] = func_13534
mod = relay.transform.InferType()(mod)
output = func_13534()
func_13535 = relay.Function([], output)
mutated_mod['func_13535'] = func_13535
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7014_call = mod.get_global_var('func_7014')
func_7016_call = mutated_mod.get_global_var('func_7016')
call_13574 = relay.TupleGetItem(func_7014_call(), 0)
call_13575 = relay.TupleGetItem(func_7016_call(), 0)
output = call_13574
output2 = call_13575
func_13592 = relay.Function([], output)
mod['func_13592'] = func_13592
mod = relay.transform.InferType()(mod)
mutated_mod['func_13592'] = func_13592
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13592_call = mutated_mod.get_global_var('func_13592')
call_13593 = func_13592_call()
output = call_13593
func_13594 = relay.Function([], output)
mutated_mod['func_13594'] = func_13594
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7559_call = mod.get_global_var('func_7559')
func_7560_call = mutated_mod.get_global_var('func_7560')
call_13740 = func_7559_call()
call_13741 = func_7559_call()
output = call_13740
output2 = call_13741
func_13742 = relay.Function([], output)
mod['func_13742'] = func_13742
mod = relay.transform.InferType()(mod)
output = func_13742()
func_13743 = relay.Function([], output)
mutated_mod['func_13743'] = func_13743
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10030_call = mod.get_global_var('func_10030')
func_10031_call = mutated_mod.get_global_var('func_10031')
call_13752 = relay.TupleGetItem(func_10030_call(), 1)
call_13753 = relay.TupleGetItem(func_10031_call(), 1)
func_12139_call = mod.get_global_var('func_12139')
func_12143_call = mutated_mod.get_global_var('func_12143')
const_13762 = relay.const(-2, dtype = "uint64")#candidate|13762|()|const|uint64
const_13763 = relay.const([6,-4,-4,-4,-3,7,10,8,-10,9,2,4,-1,-8,-9,8,4,-6,10,-3,-8,8,4,9,6,10,9,2,4,10,6,-9,-9,1,6,4,-6,1,-8,-6,10,6,7,-9,7,6,-9,-6,-1,-10,2,-10,6,-10,10,1,-9,9,-3,1,-10,-3,-4,-9,-9,2,3,-2,1,-3,8,-3,1,5,2,3,-4,1,9,-3,-9,2,4,10,7,-8,-1,2,-5,-3,-6,7,5,10,-7,2,7,-7,9,-8,-5,1,-9,6,-3,-9,7,9,-5,8,1,8,-6,-8,-2,-1,-3,1,-7,-6,-7,-9,2,-8,8,-10,8,6,-1,-8,1,2,-4,-7,-1,3,-7,-4,-2,-7,8,9,3,1,10,-9,-1,-6,-3,9,-4,-1,5,-2,-8,7,-4,4,-2,3,4,-4,2,-1,-4,10,3,1,-7,-4,1,2,8,5,3,-3,-2,4,-8,3,-7,10,-2,-7,3,5,3,-9,5,10,-6,5,-9,-5,5,-6,9,-2,6,-2,-1,3,6,4,10,9,6,-5,4,9,-8,-2,3,-9,-3,10,-8,9,-6,5,-6,3,10,-6,-8,4,2,-10,-9,-3,-10,8,5,3,-10,-1,-5,-10,-2,1,-1,-3,-2,7,-4,4,3,-5,9,4,-8,-10,9,10,-8,9,-8,2,9,-1,-10,-10,-9,5,-3,-1,-4,-4,1,-2,6,8,-6,-4,-10,2,2,-6,7,10,8,10,2,-3,-7,4,8,7,-2,3,-8,5,4,-10,1,-10,-3,3,4,10,2,-7,4,6,-7,-2,-1,4,8,-8,-5,-10,-9,-4,8,6,-8,10,-9,9,-5,-2,8,4,3,5,-10,-8,7,-6,8,4,-7,7,3,5,-9,-6,6,-4,-2,8,-5,3,-8,6,-2,-1,9,4,-4,-1,7,-1,-7,-1,6,-3,4,3,-6,10,-3,5,-9,-5,-10,-7,8,-10,-4,4,-10,1,4,8,4,5,8,-1,-3,-9,7,-1,-5,9,-4,7,1,-8,3,4,3,-7,1,8,-6,-6,5,9,-10,9,-3,-8,6,9,3,7,5,8,1,10,5,4,7,1,-2,-1,-7,-9,-6,-2,-4,-6,-2,6,10,-5,-4,-6,2,8,10,-1,10,-1,10,7,2,-4,-6,10,-8,3,-3,3,-10,1,2,-8,4,3,3,-2,3,-1,-8,-7,5,-8,-2,-6,-6,2,-1,-2,-10,-10,5,1,-8,9,3,-2,-9,-7,-5,-3,1,1,-6,8,-8,-2,-10,2,-3,-6,10,-5,2,10,-4,-8,-8,9,-2,1,-5,6,6,-5,-1,-5,1,-10,1,-10,-2,-2,-9,-4,7,-4,8,10,-8,-3,8,-1,-10,-3,10,-8,6,-1,-2,-8,10,-5,-2,2,-2,10,-5,-10,-2,5,-8,2,-4,9,-10,7,10,10,-7,-1,-9,8,2,8,10,-5,6,-2,-4,6,-1,4,5,3,-6,8,7,-9,5,-4,1,-5,9,-7,10,7,-6,-3,6,-2,2,8,-9,2,-6,-9,8,-4,-1,1,4,-5,2,-3,5,1,-9,-1,-7,10,-1,-10,3,7,-5,-5,10,-3,-7,-1,4,-2,-2,-1,5,-4,-2,-5,-8,-9,3,-4,-4,-5,3,-5,-7,-2,-9,-10,6,-9,8,-5,6,-9,-8,2,-10,-4,5,2,6,3,-10,-10,-8,-7,2,-5,4,9,-7,-5,-10,-1,-8,-10,-8,-2,7,5,2,2,-3,-4,10,-8,-6,7,-2,2,-1,8,5,-8,-3,-8,6,-1,-8,6,8,-9,9,-10,-4,2,-5,7,-10,2,9,-8,-1,-5,-4,9,7,6,-5,8,9,5,8,-5,6,-4,7,-1,3,-9,7,10,-9,-1,-5,2,-8,-9,6,7,-1,-8,-4,-9,4,-5,10,-6,-2,-3,-5,2,-3,-2,-4,10,9,-6,-6,-2,-6,1,2,7,4,2,7,5,-2,-9,-5,2,9,-8,4,3,-7,-6,-2,3,-2,-5,7,-7,4,-7,-4,-4,-6,8,-2,-10,5,-8,-6,3,5,5,6,1,9,-1,-7,-8,7,5,-6,8,8,10,-6,1,9,-3,1,6,-4,-5,-4,-5,10,2,-6,9,8,-9,-2,-6,-10,7,3,-1,4,7,10,9,-4,8,-3,6,-8,-6,7,3,-8,-7,6,7,8,8,-6,10,9,-3,-4,-4,4,-1,1,-8,-4,10,-5,-10,1,-10,6,-10,-7,9,-10,2,-4,-6,-8,-4,9,4,10,-8,-3,-9,-10,4,-10,7,-8,7,-3,-7,-7,-3,4,4,-1,-7,3,-3,-5,-8,-2,8,-3,1,7,-5,6,5,-5,-8,-1,3,2,-5,-5,-3,-8,-6,-3,-5,3,-7,9,-3,-10,3,5,-3,1,6,-3,-2,10,-9,3,5,5,-6,-5,1,7,5,1,1,-10,-10,5,-1,8,-8,-6,-8,7,9,3,7,5,4,-2,10,3,2,-9,-3,-4,1,-5,5,3,6,-2,-7,-5,-5,-7,10,4,-8,-6,2,-9,2,-2,-8,8,2,-6,-1,2,-7,-10,9,-8,6,5,6,3,-1,-6,3,-2,-8,-5,-7,-4,8,-3,5,-5,7,-3,7,2,2,-7,-2,9,7,-8,3,-1,3,9,7,-2,-5,7,10,9,7,-4,-5,10,9,6,-9,4,-3,3,10,-2,10,-6,-1,10,-3,7,-9,9,7,3,-2,-8,-1,-3,-6,-5,-6,-5,-8,-5,1,-8,-10,-2,2,-3,-2,9,3,6,9,-6,-4,4,-7,-4,10,3,-9,-7,10,-7,-2,-10,10,-4,7,8,2,3,8,2,-9,7,1,3,5,-6,6], dtype = "int64")#candidate|13763|(1080,)|const|int64
call_13761 = relay.TupleGetItem(func_12139_call(relay.reshape(const_13762.astype('uint64'), []), relay.reshape(const_13763.astype('int64'), [1080,]), ), 6)
call_13764 = relay.TupleGetItem(func_12143_call(relay.reshape(const_13762.astype('uint64'), []), relay.reshape(const_13763.astype('int64'), [1080,]), ), 6)
output = relay.Tuple([call_13752,call_13761,const_13762,const_13763,])
output2 = relay.Tuple([call_13753,call_13764,const_13762,const_13763,])
func_13765 = relay.Function([], output)
mod['func_13765'] = func_13765
mod = relay.transform.InferType()(mod)
output = func_13765()
func_13766 = relay.Function([], output)
mutated_mod['func_13766'] = func_13766
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4738_call = mod.get_global_var('func_4738')
func_4740_call = mutated_mod.get_global_var('func_4740')
call_13779 = relay.TupleGetItem(func_4738_call(), 1)
call_13780 = relay.TupleGetItem(func_4740_call(), 1)
func_10662_call = mod.get_global_var('func_10662')
func_10663_call = mutated_mod.get_global_var('func_10663')
call_13812 = func_10662_call()
call_13813 = func_10662_call()
func_10078_call = mod.get_global_var('func_10078')
func_10080_call = mutated_mod.get_global_var('func_10080')
call_13821 = func_10078_call()
call_13822 = func_10078_call()
func_7144_call = mod.get_global_var('func_7144')
func_7145_call = mutated_mod.get_global_var('func_7145')
call_13829 = relay.TupleGetItem(func_7144_call(), 0)
call_13830 = relay.TupleGetItem(func_7145_call(), 0)
func_13274_call = mod.get_global_var('func_13274')
func_13275_call = mutated_mod.get_global_var('func_13275')
call_13832 = func_13274_call()
call_13833 = func_13274_call()
func_4450_call = mod.get_global_var('func_4450')
func_4452_call = mutated_mod.get_global_var('func_4452')
call_13844 = relay.TupleGetItem(func_4450_call(relay.reshape(call_13779.astype('float32'), [78, 6])), 4)
call_13845 = relay.TupleGetItem(func_4452_call(relay.reshape(call_13779.astype('float32'), [78, 6])), 4)
func_8835_call = mod.get_global_var('func_8835')
func_8840_call = mutated_mod.get_global_var('func_8840')
const_13858 = relay.const(9, dtype = "uint64")#candidate|13858|()|const|uint64
const_13859 = relay.const([-5,7,3,2,2,-8,-8,-4,5,-6,-7,5,7,1,-9,-4,-9,8,3,-9,-2,5,-1,10,7,4,-10,10,-7,3,3,4,-8,-5,2,8,-10,-6,4,-7,-10,6,10,-7,-9,6,-8,6,-1,-9,-3,-9,-1,-6,-10,9,3,-2,-3,1,9,-6,8,-5,10,-3,10,-10,8,-10,-8,-10,4,8,-9,9,-8,7,6,-4,5,-1,-3,9,-6,2,8,9,-2,-9,-5,2,-5,9,2,-6,-5,3,-8,1,-1,-8,-5,-1,3,1,-10,3,-4,7,-8,-5,9,-10,2,1,-4,-2,-5,9,5,-5,-5,-2,-1,-6,-3,-1,-9,-1,4,-4,-10,-9,-1,4,8,-3,-10,-1,6,-1,8,-1,-4,-10,4,-7,10,1,4,-9,5,-5,-7,-5,2,1,-9,-9,-5,-3,10,-5,-8,4,-10,-4,5,1,4,6,-3,7,9,8,2,-5,3,-5,-6,1,-3,2,-4,9,-10,-5,-2,-6,-8,-7,6,-5,3,8,-10,-5,5,1,2,-7,-5,-5,7,-7,6,5,7,-8,1,-10,-8,6,-2,-5,4,-5,6,-5,-1,-8,-8,6,-7,8,4,-1,-2,-8,-3,-7,6,-8,-3,-7,-7,1,10,-5,-6,6,-10,4,5,6,-6,-7,-6,5,9,-6,-7,-6,-8,5,-3,-6,8,-6,-4,1,5,10,-2,-5,-7,9,-9,2,-5,1,-5,-4,-7,-6,-3,10,-4,1,7,8,6,9,-4,1,7,-9,9,7,-4,-6,7,-6,6,6,-3,9,-2,3,1,-5,-5,1,10,9,-1,4,1,-9,-7,-10,9,-8,-8,-9,6,-7,2,7,8,-7,-3,4,-1,8,-10,-6,8,2,-4,2,6,-1,9,-10,5,3,10,-9,2,9,-6,3,-1,-9,-5,-5,2,9,7,8,7,-8,-1,-8,-4,7,1,5,4,-7,7,-1,-1,2,-2,-9,-2,-7,-4,7,3,-2,-3,-6,-3,9,-8,-10,-3,-8,1,-5,4,7,7,8,8,-4,-6,-10,-7,8,-9,6,-1,6,-2,6,-3,4,4,9,1,-3,-6,-6,9,-8,-2,-10,-3,-6,7,2,4,-9,-9,10,-2,7,-7,-10,-6,-7,-7,3,5,-4,1,4,2,-4,2,1,9,1,-2,4,-1,10,8,-5,-3,7,7,-7,-7,-9,7,4,-1,-1,7,-1,-6,6,4,-7,4,-1,7,7,-1,2,10,3,10,4,-1,6,8,9,7,9,2,-10,1,1,-8,1,9,-1,10,-6,10,6,8,-10,-3,-6,-10,-4,-6,5,9,3,-2,7,-10,4,-7,-8,8,-1,6,8,4,8,-10,-7,1,-7,4,6,8,-4,2,3,-9,-3,-10,4,4,7,7,2,-3,2,4,-3,-9,1,-10,-3,9,-7,-8,4,-3,7,4,-7,-10,-6,8,-1,8,-10,6,-1,-9,3,-7,1,-7,-9,10,8,6,4,-5,1,-7,-4,-4,10,-5,-3,2,-4,4,2,9,4,5,-9,5,4,3,-6,6,4,-1,-4,3,-3,-9,-1,-6,6,-4,-4,7,10,-9,-10,-6,-4,1,1,-6,-3,1,5,-10,1,-8,-3,-4,-6,3,7,10,6,9,-7,2,-2,-5,-10,-2,1,5,-4,8,3,-7,1,-10,-9,4,8,6,-9,-8,8,-10,-7,-4,8,-4,5,9,-7,3,-10,3,-5,7,-4,2,5,2,9,-5,-7,-7,-10,-8,-5,-4,10,-4,-8,8,6,-3,-4,-4,-10,1,10,8,2,9,-9,-4,-2,-3,-9,-4,2,7,4,-8,-2,2,7,-2,-5,6,-5,2,-7,10,7,3,3,3,1,2,2,-5,-3,8,7,-4,2,-2,1,9,7,-7,-3,-8,4,10,-3,7,-2,-5,-8,-3,-5,1,6,5,-3,-4,3,-1,-3,6,-3,-1,7,8,-7,6,-8,7,9,9,-4,-6,-4,-7,7,-2,-4,7,-3,7,-8,9,9,1,-1,10,3,4,7,6,-3,-4,5,10,-10,5,9,-5,-3,-8,9,10,8,-1,3,8,-8,-7,-6,1,6,-4,-4,-5,7,1,-3,-8,-5,5,6,8,-6,9,1,-9,-7,-2,-4,-8,-2,9,-10,-8,5,6,9,-7,8,6,-5,-6,10,1,-5,-6,-8,2,-1,-4,6,-10,-4,7,-5,1,1,-2,5,4,-2,7,-3,-9,-1,-1,-5,-9,9,10,2,2,9,2,-9,4,-7,3,-1,-4,-7,9,-7,-10,-6,-10,6,-2,8,-10,10,-8,6,7,-4,-2,-8,-3,-9,1,7,-6,5,-7,9,10,3,8,-1,-9,-6,6,-1,-8,5,-8,5,5,-9,5,-2,-1,4,4,-2,10,3,-1,6,7,-3,4,-8,-5,3,-6,6,-10,7,-8,7,7,6,4,-9,5,-3,-9,-8,-9,6,-6,5,3,-9,10,-8,6,7,8,-1,10,-10,7,3,8,1,2,-9,-7,5,-6,6,-7,-2,-1,-7,-6,-9,-4,-9,2,8,10,-8,-8,4,-5,6,3,8,10,4,2,-1,8,1,-3,-3,-8,8,3,2,4,4,5,-1,7,2,-1,-8,-4,6,-9,10,1,7,-2,3,-6,-3,-9,9,10,-5,-6,-7,-1,-8,5,10,-8,9,6,5,-9,5,5,-5,-5,5,3,-2,8,-7,-9,-6,-3,-6,6,-1,2,-4,9,-1,10,-6,9,-9,9,7,-4,5,-7,-8,-4,2,6,2,-5,-10,10,-10,-5,5,9,-1,4,-2,-7,-8,1,7,-3,-5,-6,7,-4,-5,8,-2,-2,1,9,1,-6,-8,-6,-6,-6,9,-7,-7,5,-9,-4,1,-6,-5,6,2,2,10,-7,-7,9,-6,-4,9,-9,-4,1,-10,-8,1,-9,-5,-7,9,1,-6,5,9,6,-1,-6,7,-10,2,2,-1,10,-1,1,8,7,-4,-7,2,-9,-10,7,2,-4,7,-10,6,6,-5,-9,-1,-9,1,-8,-1,5,3,9,-3,-10,9,-9,-7,2,2,-5,10,-7,-9,-3,3,-4,-3,-2,5,5,1,7,-8,10,-2,2,8,-4,-6,1,-6,8,5,-6,-3,4,-6,1,-2,4,7,-8,7,4,-9,-7,-8,-6,8,-5,6,4,-2,8,8,-10,9,-10,9,4,-10,5,-5,-3,7,-3,-9,7,-5,-7,-8,-8,2,7,-5,-1,9,3,1,8,-5,-2,-9,-8,-5,-7,-10,4,-6,-5,-10,-4,-4,-5,-2,-2,-4,-3,-3,-7,-8,3,-1,1,-8,6,5,-8,-8,4,6,9,8,4,7,-10,-8,-2,-2,6,-1,7,-6,-5,-8,4,-2,-3,-7,2,10,6,6,7,-2,7,9,9,1], dtype = "uint64")#candidate|13859|(1280,)|const|uint64
var_13860 = relay.var("var_13860", dtype = "int64", shape = (1080,))#candidate|13860|(1080,)|var|int64
call_13857 = relay.TupleGetItem(func_8835_call(relay.reshape(call_13832.astype('float32'), [468,]), relay.reshape(const_13858.astype('uint64'), []), relay.reshape(const_13859.astype('uint64'), [2, 640]), relay.reshape(var_13860.astype('int64'), [1080,]), ), 9)
call_13861 = relay.TupleGetItem(func_8840_call(relay.reshape(call_13832.astype('float32'), [468,]), relay.reshape(const_13858.astype('uint64'), []), relay.reshape(const_13859.astype('uint64'), [2, 640]), relay.reshape(var_13860.astype('int64'), [1080,]), ), 9)
func_5570_call = mod.get_global_var('func_5570')
func_5572_call = mutated_mod.get_global_var('func_5572')
call_13877 = relay.TupleGetItem(func_5570_call(), 0)
call_13878 = relay.TupleGetItem(func_5572_call(), 0)
func_13194_call = mod.get_global_var('func_13194')
func_13195_call = mutated_mod.get_global_var('func_13195')
call_13880 = func_13194_call()
call_13881 = func_13194_call()
output = relay.Tuple([call_13779,call_13812,call_13821,call_13829,call_13832,call_13844,call_13857,const_13858,const_13859,var_13860,call_13877,call_13880,])
output2 = relay.Tuple([call_13780,call_13813,call_13822,call_13830,call_13833,call_13845,call_13861,const_13858,const_13859,var_13860,call_13878,call_13881,])
func_13882 = relay.Function([var_13860,], output)
mod['func_13882'] = func_13882
mod = relay.transform.InferType()(mod)
mutated_mod['func_13882'] = func_13882
mutated_mod = relay.transform.InferType()(mutated_mod)
var_13883 = relay.var("var_13883", dtype = "int64", shape = (1080,))#candidate|13883|(1080,)|var|int64
func_13882_call = mutated_mod.get_global_var('func_13882')
call_13884 = func_13882_call(var_13883)
output = call_13884
func_13885 = relay.Function([var_13883], output)
mutated_mod['func_13885'] = func_13885
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4464_call = mod.get_global_var('func_4464')
func_4465_call = mutated_mod.get_global_var('func_4465')
call_13943 = func_4464_call()
call_13944 = func_4464_call()
func_10616_call = mod.get_global_var('func_10616')
func_10618_call = mutated_mod.get_global_var('func_10618')
call_13953 = relay.TupleGetItem(func_10616_call(), 1)
call_13954 = relay.TupleGetItem(func_10618_call(), 1)
output = relay.Tuple([call_13943,call_13953,])
output2 = relay.Tuple([call_13944,call_13954,])
func_13962 = relay.Function([], output)
mod['func_13962'] = func_13962
mod = relay.transform.InferType()(mod)
mutated_mod['func_13962'] = func_13962
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13962_call = mutated_mod.get_global_var('func_13962')
call_13963 = func_13962_call()
output = call_13963
func_13964 = relay.Function([], output)
mutated_mod['func_13964'] = func_13964
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6065_call = mod.get_global_var('func_6065')
func_6067_call = mutated_mod.get_global_var('func_6067')
call_14028 = relay.TupleGetItem(func_6065_call(), 0)
call_14029 = relay.TupleGetItem(func_6067_call(), 0)
output = call_14028
output2 = call_14029
func_14036 = relay.Function([], output)
mod['func_14036'] = func_14036
mod = relay.transform.InferType()(mod)
output = func_14036()
func_14037 = relay.Function([], output)
mutated_mod['func_14037'] = func_14037
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3794_call = mod.get_global_var('func_3794')
func_3795_call = mutated_mod.get_global_var('func_3795')
call_14046 = relay.TupleGetItem(func_3794_call(), 0)
call_14047 = relay.TupleGetItem(func_3795_call(), 0)
output = relay.Tuple([call_14046,])
output2 = relay.Tuple([call_14047,])
func_14048 = relay.Function([], output)
mod['func_14048'] = func_14048
mod = relay.transform.InferType()(mod)
mutated_mod['func_14048'] = func_14048
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14048_call = mutated_mod.get_global_var('func_14048')
call_14049 = func_14048_call()
output = call_14049
func_14050 = relay.Function([], output)
mutated_mod['func_14050'] = func_14050
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8445_call = mod.get_global_var('func_8445')
func_8446_call = mutated_mod.get_global_var('func_8446')
call_14077 = func_8445_call()
call_14078 = func_8445_call()
func_842_call = mod.get_global_var('func_842')
func_847_call = mutated_mod.get_global_var('func_847')
const_14099 = relay.const([-4.481454,-9.261265,-8.096880,-0.249140,5.092852,-9.270612,-6.463252,-0.134272,5.619698,7.432674,-6.847804,-1.233775,-2.726549,6.957016,-8.868004,6.802988,-9.453864,5.884167,7.190256,5.354354,-5.590502,5.585432,-3.542247,-4.573010,-0.300250,-8.389634,-9.918186,6.404351,-7.897732,-3.666863,9.430663,4.439682,0.032920,-2.724751,0.135701,-6.250258,3.078687,-7.764763,8.401359,5.827046,-0.567866,-2.333042,4.263433,1.496228,-7.680962,-1.756517,-7.892819,-2.924580,-0.611323,-6.017859,-3.185541,0.280966,-7.885499,-4.667692,-4.677473,-4.385118,0.507181,-9.618101,-7.119369,-0.773816,5.110784,6.773799,-8.406998,-9.696391,-5.324220,-2.978934,7.023198,9.703299,6.021066,8.262864,2.921347,-3.308135,-4.916535,3.618332,9.553995,-4.508153,-4.926362,-7.971553,6.784687,-6.639531,6.875404,-2.732180,-3.375128,2.183051,4.335615,-7.415301,-3.401088,1.365208,4.953200,6.472731,-0.306472,3.132424,7.458937,-1.499890,-3.342659,8.963030,0.383785,-4.179707,3.437427,-4.239620,-2.256399,3.107203,5.188434,-2.027078,-1.999326,4.330078,4.711254,0.477078,-8.116065,7.406562,-0.485274,1.512523], dtype = "float64")#candidate|14099|(112,)|const|float64
var_14100 = relay.var("var_14100", dtype = "float32", shape = (468,))#candidate|14100|(468,)|var|float32
call_14098 = relay.TupleGetItem(func_842_call(relay.reshape(const_14099.astype('float64'), [4, 4, 7]), relay.reshape(const_14099.astype('float64'), [4, 4, 7]), relay.reshape(var_14100.astype('float32'), [1, 468]), ), 1)
call_14101 = relay.TupleGetItem(func_847_call(relay.reshape(const_14099.astype('float64'), [4, 4, 7]), relay.reshape(const_14099.astype('float64'), [4, 4, 7]), relay.reshape(var_14100.astype('float32'), [1, 468]), ), 1)
output = relay.Tuple([call_14077,call_14098,const_14099,var_14100,])
output2 = relay.Tuple([call_14078,call_14101,const_14099,var_14100,])
func_14104 = relay.Function([var_14100,], output)
mod['func_14104'] = func_14104
mod = relay.transform.InferType()(mod)
mutated_mod['func_14104'] = func_14104
mutated_mod = relay.transform.InferType()(mutated_mod)
var_14105 = relay.var("var_14105", dtype = "float32", shape = (468,))#candidate|14105|(468,)|var|float32
func_14104_call = mutated_mod.get_global_var('func_14104')
call_14106 = func_14104_call(var_14105)
output = call_14106
func_14107 = relay.Function([var_14105], output)
mutated_mod['func_14107'] = func_14107
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7107_call = mod.get_global_var('func_7107')
func_7109_call = mutated_mod.get_global_var('func_7109')
call_14120 = relay.TupleGetItem(func_7107_call(), 0)
call_14121 = relay.TupleGetItem(func_7109_call(), 0)
var_14130 = relay.var("var_14130", dtype = "bool", shape = (15, 8, 468))#candidate|14130|(15, 8, 468)|var|bool
bop_14131 = relay.power(call_14120.astype('float32'), relay.reshape(var_14130.astype('float32'), relay.shape_of(call_14120))) # shape=(15, 8, 468)
bop_14134 = relay.power(call_14121.astype('float32'), relay.reshape(var_14130.astype('float32'), relay.shape_of(call_14121))) # shape=(15, 8, 468)
func_8736_call = mod.get_global_var('func_8736')
func_8737_call = mutated_mod.get_global_var('func_8737')
call_14151 = relay.TupleGetItem(func_8736_call(), 3)
call_14152 = relay.TupleGetItem(func_8737_call(), 3)
func_10190_call = mod.get_global_var('func_10190')
func_10196_call = mutated_mod.get_global_var('func_10196')
const_14154 = relay.const([[7.727704,-9.920099,1.839157],[8.786069,1.030956,-8.595991],[4.832997,-7.681303,7.217203],[5.523836,-0.959907,9.106171],[7.770450,-6.534033,5.993232],[-5.468097,5.552990,-0.416742],[-5.523277,1.264605,4.558628],[6.340183,-2.216301,-9.669957],[-3.715780,-2.412465,6.303902],[-3.067616,-0.083580,5.970375],[-7.085554,8.737477,-0.199633],[6.298658,1.744569,-1.242828],[-4.143321,2.750886,-2.114547],[-4.564963,-8.939691,7.043815],[-2.150048,-8.898069,-0.222591],[9.965925,-3.604116,-3.077996],[-9.976176,3.989165,-3.603960],[8.582480,5.431241,9.664466],[-6.195680,6.107764,-5.140707],[9.639579,-9.578601,-8.868200],[1.087972,-3.884265,-2.481800],[-0.627658,-7.134736,-9.166202],[-2.052378,0.761802,-3.281176],[6.968838,-3.742476,2.462570],[7.688376,2.301916,5.528670],[-1.770481,8.784353,-0.043766],[-8.038105,8.353627,-9.237894],[0.879645,9.672171,2.756985],[-6.258647,-3.380607,0.829094],[7.187182,-8.410674,-8.872658],[-7.567727,-6.647015,9.223914],[2.766743,-4.964747,-4.855440],[-3.369327,6.545415,-9.785417],[-7.030568,0.531724,8.884082],[-9.588552,4.484859,-3.600289],[-4.943583,-5.529842,-7.047756],[2.121200,0.415713,-9.255042],[8.978597,-8.315950,-2.778316],[1.604210,6.732466,-3.274836],[6.888323,4.240728,8.439791],[-4.915298,2.300867,5.403028],[7.913121,0.040936,-5.894727],[-9.724470,9.733019,-9.459074],[-1.721565,-4.807205,-6.046229],[-3.209602,7.392830,-6.790105],[8.955747,9.025309,8.352823],[7.402127,1.606073,-4.005562],[-7.696730,8.965313,1.684045],[-6.364534,4.915837,6.844321],[7.394915,5.609840,0.105665],[9.136126,1.232757,3.907395],[5.303872,5.796952,-6.910669],[-9.105795,-9.331487,-9.754087],[9.847095,8.040793,7.816787],[-7.964409,9.225172,6.174783],[0.674496,8.717542,7.693772],[-9.925812,8.828810,-0.699882],[5.215189,9.233258,-9.505708],[0.400939,-2.922260,9.101724],[9.144085,-3.658327,9.065976],[8.003230,-3.755038,0.411615],[-0.896003,4.230415,7.478486],[4.534303,-2.550783,1.387297],[-7.461326,1.911121,5.821865],[-4.689217,-9.595172,0.550788],[-3.235977,8.776257,-5.007038],[1.439679,-4.422644,-0.982120],[-0.376053,-6.322466,-5.307490],[7.381860,-4.912523,7.911300],[6.149379,-2.290848,-1.016339],[-4.666139,-3.150037,-3.346780],[-9.985186,8.414482,-8.904567],[5.519275,5.629180,1.123440],[9.059201,-8.577843,4.763001],[0.440894,3.235107,7.445435],[-4.768893,9.465223,6.456984],[1.556600,3.900015,-8.184891],[-8.614571,-9.989013,0.824377],[-2.518980,-7.515809,-8.133940],[-4.882091,3.247930,6.079881],[-6.579324,-9.458924,-8.029151],[7.033812,1.632629,9.308200],[-4.319149,5.180993,4.841894],[-8.936906,4.236366,7.264837],[4.805910,-4.961702,6.205867],[2.261028,9.682201,6.597758],[2.947895,0.623825,4.630490],[-9.993326,-8.867779,-8.591080],[-2.693860,6.575315,-5.291752],[0.839593,4.144923,-2.234594],[4.643748,-8.954320,3.694799],[-2.007083,-5.370293,2.953953],[-7.143639,7.498685,-1.405796],[8.462780,-3.692152,-9.916103],[5.100495,-5.454372,7.335350],[0.413018,-9.737475,1.499755],[-4.523163,-8.968105,6.369702],[-6.599924,3.600170,7.777476],[-8.161758,-4.191727,2.657528],[8.483040,-4.659838,3.235170],[-6.151174,-8.351617,-3.064382],[-0.150676,-6.338611,0.574544],[-6.187634,7.468456,6.570078],[3.152056,6.945275,0.867242],[8.410471,3.570110,-2.554247]], dtype = "float64")#candidate|14154|(105, 3)|const|float64
const_14155 = relay.const([True,True,False,False,True,True,True,True,False,False,False,False,False,False,True,True,False,False,False,False,False,True,True,False,True,True,False,False,False,True,True,True,False,True,False,True,False,True,True,True,True,True,True,True,True,True,True,True,True,True,False,True,False,True,False,False,False,False,False,False,True,True,False,True,False,False,True,False,True,False,True,False,True,True,False,False,False,True,False,True,False,False,True,True,True,True,True,True,True,True,True,True,False,True,False,False,True,True,False,False,True,False,True,False,True,True,True,True,False,True,False,False,True,True,True,False,False,False,True,False,True,False,True,True,False,True,True,True,True,False,False,False,False,True,True,True,False,False,False,False,True,False,False,False,False,False,False,False,False,True,False,False,True,True,True,True,True,True,True,False,True,True,False,True,False,True,False,False,True,False,False,False,False,False,False,False,False,False,True,True,True,True,True,True,True,False,False,False,True,True,False,False,False,False,True,False,False,True,False,True,True,False,False,False,True,False,False,True,True,True,False,False,True,True,True,False,False,False,False,True,True,False,False,False,False,True,False,False,True,True,False,False,True,False,False,False,False,True,False,True,False,False,False,True,False,True,True,False,True,True,True,True,True,True,True,False,True,True,False,False,False,False,False,False,False,True,False,True,False,False,False,False,True,False,False,True,False,True,True,True,True,False,False,False,False,True,False,True,True,True,True,True,True,True,True,False,False,False,True,False,False,True,True,True,False,True,False,False,False,True,True,True,False,False,False,False,True,False,True,False,True,False,False,True,True,True,True,False,True,False,False,False,True,True,True,True,False,False,True,True,True,True,False,True,True,False,True,False,True,False,True,False,False,True,True,False,False,False,False,False,False,False,False,False,False,True,True,False,True,True,True,True,False,False,False,True,False,False,True,True,False,False,False,True,True,True,True,False,False,True,False,False,True,False,False,True,True,False,False,True,True,True,False,True,True,False,False,False,False,True,True,True,False,True,False,True,True,True,True,True,False,True,True,True,True,False,True,True,False,True,False,True,False,False,False,False,False,False,False,True,True,True,False,True,True,False,True,False,True,False,True,True,False,False,False,True,False,True,False,False,False,False,True,True,False,True,True,True,True,True,False,True,False,False,False,True,False,True,True,True,False,False,False,False,True,False,True,True,False,False,False,False,False,True,True,True,True,False,False,False,True,False,True,False,False,False,True,False,True,True,True,True,True,True,True,False,True,True,False,True,True,False,False,True,True,True,False,False,False,False,True,True,False,False,True,False,False,True,False,False,False,True,True,True,False,True,False,False,False,False,True,True,False,True,False,True,True,True,False,True,True,True,False,False,True,False,False,False,True,True,False,True,False,True,False,True,False,False,True,False,False,False,True,False,False,False,False,True,True,False,False,False,True,False,False,False,False,True,False,True,False,False,False,False,False,True,True,False,True,False,True,False,True,False,False,True,False,False,False,True,False,False,False,True,False,False,False,True,True,False,False,True,True,True,False,True,False,True,True,True,False,False,True,True,True,False,False,True,False,False,True,True,False,True,False,False,True,False,True,True,True,False,False,False,True,False,True,True,False,False,False,False,True,False,True,False,False,True,True,False,True,False,True,True,True,False,True,True,False,True,False,True,True,False,True,False,True,False,True,True,True,True,True,False,True,False,False,True,True,True,False,False,False,True,True,True,True,False,False,False,True,False,True,False,True,True,False,False,True,True,True,False,True,False,False,False,False,False,False,True,False,False,True,False,True,False,True,True,False,False,True,False,False,False,False,True,True,True,True,True,False,False,True,True,False,False,False,False,False,False,True,False,False,False,False,True,False,False,False,True,False,True,True,False,False,True,False,True,False,True,False,True,False,False,False,False,False,False,True,False,False,False,True,False,True,True,False,True,True,False,False,True,False,True,False,False,True,False,True,True,True,False,False,True,False,True,False,False,True,True,False,False,True,True,False,False,True,False,False,False,True,False,False,True,False,False,True,True,False,False,False,True,False,True,True,False,False,True,False,True,False,True,True,True,False,False,False,True,False,False,False,True,False,False,False,False,False,True,True,False,False,False,True,False,True,False,True,True,True,True,False,True,False,False,True,True,False,True,False,False,True,False,False,True,False,False,False,False,False,True,False,False,True,False,False,False,False,True,True,False,True,False,True,True,False,False,False,False,True,True,False,False,True,False,False,False,True,False,False,True,True,True,True,True,True,True,True,True,True,True,True,False,True,True,True,True,True,False,True,True,True,True,True,False,False,True,False,True,True,True,False,True,False,True,False,True,False,True,False,True,False,False,True,True,True,True,False,False,True,True,True,False,True,True,False,True,False,True,False,False,False,False,True,False,True,True,True,True,False,True,True,True,True,False,False,False,True,True,True,False,False,False,False,True,True,True,False,False,False,False,False,False,False,True,False,True,False,True,True,False,False,False,True,False,False,False,False,False,True,True,False,True,False,True,True,True,False,True,True,False,False,True,False,False,False,False,False,False,True,True,True,True,True,False,True,True,False,False,True,True,True,False,True,True,True,False,True,True,True,False,True,True,False,True,False,False,True,False,True,False,True,False,True,False,False,True,True,True,True,True,False,False,True,True,False,False,True,True,True,True,True,False,False,True,True,False,False,False,False,True,False,True,True,True,True,True,False,True,False,True,False,True,False,True,False,False,True,False,True,False,True,False,False,True,False,True,False,False,True,False,True,True,False,False,False,True,True,True,False,False,False,False,True,False,True,True,False,False,True,True,False,False,False,False,False,False,True,False,False,False,False,True,True,False,True,False,False,False,True,False,False,True,True,True,False,False,True,False,True,False,False,True,True,False,False,True,False,True,True,False,False,True,True,True,False,False,True,False,False,False,False,True,False,True,False,False,False,True,False,True,False,False,False,True,False,False,False,False,False,True,False,False,False,True,True,False,True,True,False,False,True,True,True,True,False,True,True,False,True,False,True,True,False,False,False,True,False,False,True,False,True,False,False,True,True,False,False,True,True,False,True,False,True,False,False,False,True,True,False,False,True,False,True,False,False,True,True,False,True,False,True,False,False,True,False,False,True,False,True,False,False,False,True,False,False,True,False,True,False,False,False,False,False,True,False,False,True,True,True,False,True,False,True,False,True,True,False,True,True,True,True,True,True,False,True,True,True,True,False,False,False,False,False,False,False,False,True,True,True,False,True,False,False,False,False,True,True,False,False,False,True,False,False,False,False,True,True,False,True,False,False,True,False,False,True,False,False,False,True,True,False,True,True,False,True,False,False,True,False,False,True,False,False,True,False,True,True,False,True,False,False,True,True,False,True,False,True,True,True,False,False,True,True,True,False,True,True,False,False,False,False,True,False,True,True,False,False,False,False,True,False,False,False,True,True,True,True,False,False,False,False,False,False,False,True,False,True,True,False,True,True,False,False,True,True,True,True,True,True,False,False,True,False,False,False,True,True,False,True,True,False,False,True,False,False,True,False,True,False,False,False,True,True,False,False,False,False,True,False,True,True,False,True,False,True,True,True,False,True,True,False,False,True,True,False,True,False,True,False,False,True,False,True,False,False,True,True,False,True,True,False,False,True,True,False,False,False,False,True,False,True,True,False,False,False,False,True,True,True,True,True,True,True,True,True,True,False,False,False,True,True,False,False,True,True,False,True,True,False,False,True,True,True,True,True,False,False,False,True,True,True,False,False,False,True,False,False,False,False,False,True,False,False,True,True,True,False,False,False,False,True,False,False,False,True,True,False,True,False,True,True,True,False,True,False,True,True,False,True,False,False,True,False,False,False,True,True,False,True,True,True,False,True,True,True,True,False,True,False,False,True,True,False,True,True,False,False,False,False,False,False,False,True,False,False,True,True,True,False,True,False,True,True,False,False,False,True,False,False,True,True,True,True,True,False,False,True,False,False,True,False,True,True,True,True,True,True,True,False,True,False,False,False,True,False,False,False,True,False,False,True,True,True,False,False,True,False,True,True,False,False,False,True,True,True,True,False,False,False,False,True,False,True,True,True,True,True,True,True,False,True,False,True,False,False,False,True,False,True,True,False,False,True,False,True,False,True,False,True,True,False,False,True,True,False,False,True,True,False,False,True,True,False,True,False,False,True,True,False,False,False,False,False,True,False,False,False,True,False,True,False,False,True,True,False,True,False,True,True,False,True,False,True,True,True,True,True,False,True,True,True,True,True,True,True,False,True,True,True,True,False,False,False,True,True,False,True,True,True,False,True,False,False,True,True,False,False,False,False,True,True,True,True,False,True,False,False,False,True,False,False,True,False,False,False,True,False,True,True,True,True,False,True,False,True,False,False,False,False,False,True,True,False,False,True,True,False,False,True,True,False,True,False,False,True,True,True,True,False,False,False,False,True,True,False,False,True,False,False,True,False,False,False,False,False,False,True,True,False,True,False,False,False,True,False,False,False,True,True,False,False,False,False,True,True,False,True,True,False,False,False,True,False,True,True,False,True,True,True,True,False,False,True,False,True,True,False,True,False,False,True,False,False,False,True,True,False,True,False,True,True,True,False,True,False,True,True,True,False,True,False,False,True,True,True,False,False,True,True,False,True,False,True,True,False,False,True,True,True,True,False,False,False,False,True,False,True,True,True,False,False,True,False,True,False,True,True,False,True,False,True,False,False,False,False,True,False,True,False,False,False,False,False,True,False,False,True,True,True,True,True,True,False,False,False,True,True,True,True,False,True,False,True,True,False,True,False,True,False,False,True,False,False,True,True,False,True,True,False,False,False,True,True,False,True,True,True,True,False,True,True,True,True,False,True,False,True,True,True,True,False,False,False,False,True,True,True,True,False,True,True,False,False,True,True,False,False,False,True,True,True,False,False,True,True,True,True,False,True,False,False,True,False,False,True,True,True,False,False,False,True,False,False,False,True,True,False,True,False,True,False,True,True,True,False,False,False,True,True,True,True,True,False,True,True,False,True,False,False,True,False,False,True,True,False,False,False,False,False,False,True,False,False,False,True,False,True,False,False,False,True,True,True,False,True,False,False,False,False,False,True,True,False,True,False,False,True,False,False,True,True,True,False,True,False,True,True,True,True,True,True,True,True,False,True,False,False,True,False,False,True,True,True,False,False,True,False,False,False,True,True,True,False,True,False,False,True,True,True,False,True,False,True,False,False,False,False,False,True,False,True,True,True,False,True,False,False,True,False,False,False,True,True,True,True,True,True,False,False,True,False,True,True,False,True,False,False,True,False,False,True,True,True,True,False,False,True,False,True,True,False,False,False,True,True,True,False,False,True,False,True,False,False,True,False,True,True,False,True,True,False,False,True,True,True,True,True,False,True,True,True,True,True,False,False,False,True,False,False,True,False,False,True,False,True,True,False,False,True,True,True,False,True,False,True,True,True,True,True,False,False,True,True,True,True,True,True,False,True,True,True,False,True,False,False,False,True,False,False,True,True,False,True,True,False,False,False,False,True,True,False,True,False,False,False,True,True,True,False,True,True,True,True,False,False,True,True,True,False,True,False,True,True,True,False,False,False,False,False,True,False,False,True,False,False,True,False,False,True,False,True,False,True,False,False,True,True,True,True,True,True,True,True,False,True,True,False,True,False,False,False,False,True,True,False,True,True,False,True,False,False,False,False,False,False,False,True,False,False,False,True,True,False,False,True,True,False,False,False,False,False,False,False,True,False,False,True,True,True,False,True,True,True,True,True,True,True,True,True,True,True,True,False,True,True,False,False,True,False,False,True,False,True,True,False,True,False,True,False,True,True,True,False,False,False,False,False,True,True,True,True,False,False,True,False,False,True,False,True,True,True,True,False,False,False,False,True,False,True,True,True,False,False,False,True,False,False,True,True,True,False,False,True,True,False,True,True,True,False,False,True,True,True,True,True,False,True,False,False,False,True,False,False,True,False,True,True,False,False,False,True,True,True,False,False,True,False,True,False,False,True,True,True,True,False,False,True,True,False,True,True,True,True,False,False,True,True,True,True,False,True,False,True,False,True,True,True,True,False,False,True,True,True,False,False,False,False,True,True,False,True,True,True,False,True,True,False,False,False,True,False,True,False,True,False,True,False,True,False,False,True,True,False,True,True,False,True,True,False,False,True,True,True,False,True,False,True,True,True,True,True,True,False,True,True,False,False,True,False,False,False,True,True,False,False,False,False,True,True,False,False,False,True,True,False,True,False,True,False,True,False,True,False,False,False,True,True,False,True,True,False,True,False,True,True,True,True,True,False,False,False,False,False,True,False,False,False,False,True,True,True,True,False,True,False,True,True,True,True,False,False,False,True,False,True,False,True,True,True,False,True,True,False,False,True,False,False,True,False,False,False,True,True,True,True,True,False,False,False,True,False,False,True,True,True,True,True,False,False,False,False,True,False,True,True,True,True,False,False,False,False,True,True,True,False,False,True,False,False,True,True,False,False,True,True,True,False,False,True,False,True,False,True,True,True,True,False,False,True,False,False,True,True,False,False,True,False,True,True,True,True,True,True,True,False,True,False,False,True,True,False,False,True,True,True,False,False,True,True,True,False,True,False,True,True,True,True,False,False,False,True,True,True,False,False,True,True,False,True,True,False,True,True,True,True,True,False,True,False,True,True,False,False,True,False,False,False,True,False,True,True,True,False,True,True,True,False,True,True,False,False,True,True,True,True,False,False,True,False,True,False,True,True,False,False,True,False,True,False,False,False,False,True,False,True,True,True,True,False,True,True,False,False,True,True], dtype = "bool")#candidate|14155|(2925,)|const|bool
var_14156 = relay.var("var_14156", dtype = "uint64", shape = ())#candidate|14156|()|var|uint64
var_14157 = relay.var("var_14157", dtype = "uint64", shape = (1280,))#candidate|14157|(1280,)|var|uint64
const_14158 = relay.const([4,9,-10,-7,5,1,-9,-7,3,8,6,-9,6,-6,-3,-5,-7,-4,-9,3,1,3,7,1,-7,-10,-6,-4,8,-7,2,-9,6,-5,-4,-8,-4,-5,1,1,-6,1,-7,6,-4,10,3,-7,1,-6,10,-10,-5,3,2,5,4,1,2,1,-10,-4,-10,-4,2,-6,5,5,2,5,-4,3,8,-1,3,6,5,-6,2,-6,1,-7,9,-6,1,-4,-4,3,2,2,-8,-9,-2,-7,-5,9,4,-2,-7,3,-2,3,7,7,9,-5,8,3,-8,-4,-3,1,-8,-2,1,-5,6,8,3,1,5,-1,1,-2,-4,6,-1,7,-9,-8,-6,-5,8,-4,-9,3,4,-8,9,5,-8,3,7,-1,-8,-9,2,7,-9,1,7,-3,-1,7,1,-5,5,8,-7,10,-10,2,-5,1,9,4,-7,8,-6,-8,-8,-5,1,7,-6,3,-8,-5,-3,8,8,9,-9,-3,-3,3,4,-4,-3,2,10,3,-10,2,5,-7,-4,-10,3,-7,4,8,7,-10,-5,-8,-10,4,9,5,-7,-1,-7,3,4,-6,1,-6,-6,-9,-1,-7,-7,-10,10,-4,-8,-10,-6,6,-5,8,-6,4,-5,4,-9,-6,5,-5,-3,-4,4,5,6,-9,4,7,-4,-4,6,-4,3,1,9,-3,-5,-3,-10,6,-2,7,2,7,-6,6,1,7,1,-9,4,-3,10,7,-4,6,-9,3,-8,9,9,8,-5,-3,-10,7,6,-4,-5,6,5,-7,-6,6,-1,10,10,10,-10,2,-7,8,10,-2,3,8,2,2,6,-2,3,-8,9,-6,3,10,10,1,-10,-7,-1,-10,-10,2,10,-4,-5,6,10,-4,-2,1,4,2,-7,6,-1,2,1,-7,8,-6,4,9,-5,-5,9,1,-9,7,1,3,-10,-3,-9,-3,-4,1,2,1,7,4,-1,-9,-7,4,10,10,-4,-2,-7,-1,-4,10,4,-3,7,-7,2,9,-2,5,-2,-3,-10,-1,-8,8,5,-9,-9,-10,-8,5,2,-9,-6,-10,1,-5,6,8,8,-7,-5,-4,7,-3,10,6,1,-8,-2,-5,10,4,8,2,-9,1,-5,10,-6,8,-10,-7,10,6,-6,2,3,-3,-7,6,-4,-2,1,-1,-5,-2,3,-4,7,-4,-2,-10,-4,5,10,9,-10,2,-3,8,-2,-10,4,-8,5,5,-8,-4,7,-6,-5,-10,-6,-8,-5,-6,1,-2,2,-5,1,6,-4,-6,2,-8,6,3,2,2,10,-6,4,3,9,-4,-5,-4,3,-9,-1,-1,9,-1,-5,-8,-1,-5,4,2,5,6,6,-10,7,3,8,-4,-10,-8,8,-2,-2,-3,-7,2,10,-2,7,5,-1,3,-4,8,2,1,-4,10,-1,6,9,-2,7,5,-7,-9,9,-10,9,-9,6,2,4,-7,4,-7,-3,-1,-2,-6,7,7,-9,10,-7,-8,10,4,-1,-3,6,7,-8,4,5,8,7,-7,-4,-4,-8,5,-4,4,-2,10,8,9,-8,-3,-3,4,-6,-6,-9,-1,-5,-7,-5,-6,-9,-5,6,2,-7,8,7,1,4,-4,-2,-10,-1,-7,7,3,10,4,2,-1,-10,-10,-2,10,10,8,3,8,6,-2,7,-2,1,-2,-9,-3,-3,-8,4,10,6,-6,8,2,-7,9,-8,-2,7,4,-6,-7,-2,3,-6,9,-1,-8,-9,4,-5,-10,6,-3,-6,8,-6,3,1,5,9,7,9,10,8,-3,-9,-7,7,-7,-9,-6,-10,-4,-7,8,10,-7,-5,-8,2,-5,4,-5,1,3,5,-4,10,-7,4,-4,-3,5,7,10,-3,-8,6,-10,-5,7,-4,-6,7,-1,9,7,-6,9,-6,-3,-3,-7,-6,7,10,1,5,8,9,4,7,-9,4,6,-6,-8,-10,9,4,5,-10,-7,4,-8,9,2,-1,-8,-8,4,1,-2,-9,-7,6,6,-10,10,2,-6,8,-4,-8,6,7,1,-4,-9,5,5,-9,7,3,3,5,-6,-9,6,5,3,-3,-9,9,-9,5,-6,-4,6,-2,5,-2,2,3,9,1,-9,-8,3,-8,2,6,-2,10,-10,-8,-2,7,-2,-2,-8,2,-9,-6,8,3,-9,-7,-1,-8,-3,-7,-7,-9,-3,-9,-5,-8,3,-5,10,-2,-10,10,10,-2,6,-6,-4,-3,7,7,5,4,-9,-3,-8,-10,6,10,9,8,3,-8,10,-3,-5,7,-6,-10,-2,8,7,-10,7,8,-6,-1,2,-6,-1,9,1,-8,9,-4,2,-4,-9,2,6,1,-8,-1,-4,-3,7,-2,8,-5,-7,-9,-2,-8,7,8,1,7,4,2,-6,2,8,4,-4,-4,-10,8,6,-5,-5,8,4,7,-5,5,-5,7,-1,-1,1,-5,-8,3,8,-7,-10,-1,2,2,9,1,6,-9,-10,-1,-6,2,-1,8,-2,4,-3,8,-3,3,8,7,-3,-1,7,-3,-10,6,9,-1,-2,5,-10,-1,1,-6,-9,3,9,4,-7,8,-2,-9,8,-4,-4,6,-1,-8,10,-3,9,10,1,-6,2,6,-8,-7,-4,9,-9,2,1,-4,8,-1,-7,-6,6,5,-8,2,-5,-4,-9,4,9,9,10,4,-3,4,7,-8,-4,1,-5,7,1,6,-8,9,8,1,1,5,-2,6,1,-2,-9,6,-7,2,8,-9,8,-4,-4,-6,10,-3,-2,-2,4,-9,-9,7,-10,6,-6,-4,1,-5,-5,-3,4,-9,-4,-9,-7,1,5,-3,-8,-5,-2,-1,9,9,6,-2,8,7,2,-2,4,6,3,4,-6,6,-8,-2,-2,4,5], dtype = "int64")#candidate|14158|(1080,)|const|int64
call_14153 = relay.TupleGetItem(func_10190_call(relay.reshape(const_14154.astype('float64'), [315,]), relay.reshape(const_14155.astype('bool'), [5, 585]), relay.reshape(var_14156.astype('uint64'), []), relay.reshape(var_14157.astype('uint64'), [320, 4]), relay.reshape(const_14158.astype('int64'), [90, 12]), ), 0)
call_14159 = relay.TupleGetItem(func_10196_call(relay.reshape(const_14154.astype('float64'), [315,]), relay.reshape(const_14155.astype('bool'), [5, 585]), relay.reshape(var_14156.astype('uint64'), []), relay.reshape(var_14157.astype('uint64'), [320, 4]), relay.reshape(const_14158.astype('int64'), [90, 12]), ), 0)
func_10635_call = mod.get_global_var('func_10635')
func_10637_call = mutated_mod.get_global_var('func_10637')
call_14160 = relay.TupleGetItem(func_10635_call(), 0)
call_14161 = relay.TupleGetItem(func_10637_call(), 0)
output = relay.Tuple([bop_14131,call_14151,call_14153,const_14154,const_14155,var_14156,var_14157,const_14158,call_14160,])
output2 = relay.Tuple([bop_14134,call_14152,call_14159,const_14154,const_14155,var_14156,var_14157,const_14158,call_14161,])
func_14163 = relay.Function([var_14130,var_14156,var_14157,], output)
mod['func_14163'] = func_14163
mod = relay.transform.InferType()(mod)
var_14164 = relay.var("var_14164", dtype = "bool", shape = (15, 8, 468))#candidate|14164|(15, 8, 468)|var|bool
var_14165 = relay.var("var_14165", dtype = "uint64", shape = ())#candidate|14165|()|var|uint64
var_14166 = relay.var("var_14166", dtype = "uint64", shape = (1280,))#candidate|14166|(1280,)|var|uint64
output = func_14163(var_14164,var_14165,var_14166,)
func_14167 = relay.Function([var_14164,var_14165,var_14166,], output)
mutated_mod['func_14167'] = func_14167
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9187_call = mod.get_global_var('func_9187')
func_9189_call = mutated_mod.get_global_var('func_9189')
call_14279 = relay.TupleGetItem(func_9187_call(), 2)
call_14280 = relay.TupleGetItem(func_9189_call(), 2)
uop_14291 = relay.rsqrt(call_14279.astype('float64')) # shape=(4, 28)
uop_14293 = relay.rsqrt(call_14280.astype('float64')) # shape=(4, 28)
func_2037_call = mod.get_global_var('func_2037')
func_2040_call = mutated_mod.get_global_var('func_2040')
const_14307 = relay.const([-3.634833,-8.420460,-8.888303,2.803746,-2.925296,-2.807013,-7.242037,5.553805,3.107754,9.031247,-3.826068,-0.145771,-1.723016,-3.878623,0.646124,-8.677686,-8.872751,-4.300479,-0.764670,-9.434588,9.042811,-7.724209,3.265050,6.976496,-7.371305,0.161437,-4.624810,-2.158462,2.834555,8.749902,6.510748,-7.028180,-5.432135,-3.889994,8.684229,9.194199,-4.888012,-0.442677,-6.328707,-1.405340,3.342873,7.109437,1.798901,-8.286526,-9.504522,8.407968,1.776428,5.376027,2.450170,2.434303,-0.024814,4.516519,-0.776603,-4.307743,5.066673,4.262610,-3.176210,7.427586,-6.932752,2.835132,4.614194,-9.939747,-1.571201,-9.990608,-8.048185,-9.937414,5.297212,3.963432,-3.390400,-5.129806,-2.279210,-5.650058,-7.569465,0.938154,4.334771,2.603932,1.656088,-9.366687,9.699142,0.122845,-5.232110,7.940647,0.643083,0.260429,-2.796860,-0.315346,3.068747,-1.085772,-1.806354,-2.771281,-4.314565,-1.576343,-4.169831,2.310412,6.684148,1.516093,6.236842,2.097441,0.655793,-1.549030,-8.630421,-7.814643,3.788523,3.768153,-0.652213,2.046859,3.661278,8.232784,-7.244521,-4.562748,4.770219,2.974141,-8.060253,-0.921996,3.972508,9.735349,9.300226,5.987397,-7.926115,-1.577902,7.004835,9.498645,7.300850,-5.638229,-2.250439,0.324577,-7.250209,-7.559553,-1.479272,-0.703917,6.982855,9.993775,3.686952,6.002780,-8.291239,6.728816,9.989346,-0.109057,0.058016,5.204842,8.798582,9.746452,9.733892,-2.889357,-3.464530,-4.997520,8.701388,-3.921324,-0.259563,-2.070239,3.361818,-4.221359,1.940162,0.479927,6.665256,-7.908591,-8.421459,-1.737652,8.044713,0.132639,1.555437,0.205895,7.277075,-1.206528,1.726468,-8.815536,-6.773002,4.884862,-4.240136,-8.522550,3.824975,-7.899059,-3.851894,-3.736473,-4.118499,-8.745170,7.702918,-9.179657,0.041882,-2.303904,4.253727,-9.548336,-3.195550,1.602686,-3.668388,-9.280227,-6.996939,1.810647,-3.488631,-5.263410,4.561369,-9.799845,-4.403426,-6.804473,8.912044,-6.707281,5.529311,-8.895118,4.238439,-3.465464,7.491438,2.334217,-0.878027,8.236824,-0.017302,6.742192,-7.870509,-3.742664,-3.454492,-9.706192,-5.687041,-3.589309,2.815887,7.025604,1.396598,0.984294,-6.431391,-8.213458,7.326461,9.686927,-8.858085,-3.820550,9.353377,7.602745,7.904945,3.165738,3.397991,1.123193,4.554418,3.269209,7.152671,1.057836,9.316254,-4.484105,5.958812,7.795539,-8.163512,-5.625204,-4.761462,7.350859,-1.570267,3.825391,-8.595614,-4.249793,9.153572,-0.897268,-5.996081,3.146569,-3.149129,4.126107,5.554646,8.637326,-4.486704,2.673458,1.855570,-3.351509,-0.915108,3.346771,-2.796989,-6.221065,0.101536,-9.492042,-2.664382,-2.801894,6.522514,7.123837,-8.358098,-6.703523,-7.872287,7.213189,-1.993091,9.102345,-3.132098,-2.776903,8.390092,-0.689240,4.944443,-6.004880,-7.340241,-3.113196,-2.913620,1.032761,-5.412438,4.008700,6.965314,7.495372,-0.649428,-0.719880], dtype = "float32")#candidate|14307|(288,)|const|float32
const_14308 = relay.const([[-0.678874,2.682584,6.338267,1.251225,-4.263819,8.738625,-1.066258,8.654002,-5.031604,-5.401629,7.087228,1.368071,9.237194,-1.319141,3.990416,7.740770,-1.092645,-6.573179,-1.043804,-6.544673,-3.413435,-9.366981,2.135290,-9.945551,0.001642,7.151668,-9.670285,-7.745687,-6.164226,6.087779,0.368483,3.981772,8.806605,0.005341,0.497383,-1.800871,7.877200,-9.809557,3.443588,-8.945432,5.966286,3.048255,-0.425499,-3.956435,-1.588395,-2.247889,-1.985336,2.927756,-4.856281,5.279207,-2.125894,8.953931,0.288067,5.775033,-2.429431,9.988226,9.208492,8.868519,-3.658547,-8.004039,6.054822,-5.408352,-8.088760,-7.880041,-3.334829,-2.267657,0.266260,-2.265858,6.344138,8.958717,-1.688979,-3.272764,6.206994,1.948571,1.668502,-1.737465,3.170782,-0.839930],[3.101367,-2.760427,-7.617702,-4.124974,-5.100815,-1.382740,-0.140242,1.173965,-9.440787,5.595292,-5.003213,-5.173105,-8.578315,-8.921866,9.720498,-5.805689,7.857225,6.369932,8.942237,-4.986971,-4.828078,-2.985467,-6.974748,0.452451,4.257024,5.922766,-2.295788,4.087931,-3.067235,-0.241472,-5.488595,-4.190325,9.295120,3.408844,-5.840590,-6.808573,7.154220,4.345035,-4.465058,-8.787598,4.882232,4.817686,3.652056,0.687122,5.433936,-6.275224,-6.420624,6.382258,-6.690702,-1.407035,-7.540694,1.250867,7.169863,-4.717724,-6.774994,6.406070,-5.426985,9.358998,8.999627,0.255070,-3.512906,-4.361927,6.364670,-8.709884,8.156437,-0.470054,2.736697,8.617178,-0.107854,-4.662336,-1.073786,5.028303,6.671745,5.465410,7.127877,7.060956,-4.944755,-8.393840],[9.749447,2.519348,4.098110,9.069588,8.130118,-2.925802,-9.329694,-6.849206,-5.690775,9.241186,-7.663605,2.326108,4.982777,6.324259,-9.080128,6.557650,-7.916071,-0.807663,-0.348776,-6.034181,-4.143912,-8.764886,-8.311458,-8.076555,-0.532332,-3.542928,-8.342769,-1.160004,-8.753233,1.458012,9.577141,-7.252964,2.193695,8.475882,-2.012974,4.111126,-3.053167,3.690055,3.268965,-9.627712,6.584754,-9.758852,-7.589488,-2.174668,5.282483,0.419503,-9.059817,-9.412341,5.153375,-6.363857,-6.960565,-1.337395,1.485750,8.567399,5.127255,-9.038838,-2.241655,-1.693025,6.164115,3.260058,-4.308463,0.597119,-9.566525,-7.885875,7.207199,-0.864564,8.101723,6.526929,-2.219203,6.813059,-1.083734,1.072621,-5.322979,6.237545,-7.183260,-3.042737,8.342823,8.798717],[-1.628297,0.128676,-6.447167,1.498723,8.352485,-9.061938,9.787020,3.595030,2.635510,-7.218479,7.077802,1.832034,-0.971829,-2.817955,2.751515,8.487474,-9.260234,-3.683537,-4.826693,-9.584465,-2.543063,-3.555349,-1.777230,2.389608,-6.399035,3.206483,8.362839,4.153055,6.432290,5.470795,9.979218,-2.874904,-4.677068,1.687215,-4.713843,-2.923091,-4.918994,-3.206870,-2.665641,9.031701,9.531447,-3.590037,0.159377,-0.262745,-8.564224,-3.489360,-9.337669,7.799306,6.104472,-6.507973,-3.266423,-2.499356,5.772792,6.726240,-7.047726,-8.655912,5.709784,-2.009273,-7.300607,7.518513,-8.809843,-9.803934,-4.982572,9.836783,-6.118344,3.624979,-0.652092,-0.547502,-2.523046,-2.173559,-4.727363,-4.422500,3.153100,-0.972311,6.863391,-3.890158,4.767725,0.279377],[-5.618577,7.887252,-3.723091,6.846905,-2.057988,-7.856337,5.357631,4.564018,3.718431,-2.096061,-8.998759,-9.827355,-3.013236,-6.199168,3.087158,-9.691256,-4.585620,0.869537,-5.339116,-3.119127,-6.905501,-8.059057,7.201443,9.662949,4.277842,8.519948,-0.139890,-0.024722,6.680413,0.593532,-8.948675,-4.645701,9.456812,1.218719,6.259169,0.849899,-3.058583,8.341428,4.755925,-9.214248,-8.334472,2.484195,3.493953,-0.631354,-2.374862,0.474472,6.882109,9.671438,6.818882,-7.314293,-2.929769,-6.633650,9.891478,-0.299145,-8.689275,-9.701973,9.608862,-6.128551,0.896933,3.481384,-6.458225,-0.968106,-7.943483,-6.494246,-8.393480,-6.641728,-4.112828,6.890462,6.374368,3.464756,-0.944495,-7.472774,1.399068,-3.560959,7.152320,-3.318387,-0.035345,4.585440],[-7.519145,9.768940,0.946669,-7.858729,-2.325219,2.617819,9.646299,-0.547434,-5.007007,1.764759,5.768891,-5.495530,4.976129,-2.882198,9.187691,9.694931,6.163504,-2.538342,-4.883627,7.744995,-7.781377,-2.706717,1.182820,7.391534,-5.965485,0.979196,-5.984851,-9.778204,-7.620514,-5.205945,3.668018,0.175013,-6.056380,4.292561,-1.572535,7.751210,2.250313,4.545038,-9.111310,1.537821,6.720586,-1.100020,-0.495935,-5.467183,4.477939,0.744367,-5.315447,-4.274785,-8.736874,4.168814,-6.946928,-2.769927,3.903611,-0.393371,-8.272627,-2.455894,-6.201302,-9.791395,2.451601,6.975910,1.106162,5.301342,9.300478,-8.663030,9.207608,8.846893,-4.561682,-5.630949,7.217256,-5.177718,-9.091799,9.027254,4.439228,9.516191,-4.395832,-7.518364,3.325191,9.455099]], dtype = "float32")#candidate|14308|(6, 78)|const|float32
call_14306 = relay.TupleGetItem(func_2037_call(relay.reshape(const_14307.astype('float32'), [3, 6, 16]), relay.reshape(const_14308.astype('float32'), [468,]), ), 2)
call_14309 = relay.TupleGetItem(func_2040_call(relay.reshape(const_14307.astype('float32'), [3, 6, 16]), relay.reshape(const_14308.astype('float32'), [468,]), ), 2)
uop_14310 = relay.sqrt(uop_14291.astype('float64')) # shape=(4, 28)
uop_14312 = relay.sqrt(uop_14293.astype('float64')) # shape=(4, 28)
func_7107_call = mod.get_global_var('func_7107')
func_7109_call = mutated_mod.get_global_var('func_7109')
call_14314 = relay.TupleGetItem(func_7107_call(), 3)
call_14315 = relay.TupleGetItem(func_7109_call(), 3)
func_13194_call = mod.get_global_var('func_13194')
func_13195_call = mutated_mod.get_global_var('func_13195')
call_14325 = func_13194_call()
call_14326 = func_13194_call()
func_5501_call = mod.get_global_var('func_5501')
func_5502_call = mutated_mod.get_global_var('func_5502')
call_14330 = func_5501_call()
call_14331 = func_5501_call()
output = relay.Tuple([call_14306,const_14307,const_14308,uop_14310,call_14314,call_14325,call_14330,])
output2 = relay.Tuple([call_14309,const_14307,const_14308,uop_14312,call_14315,call_14326,call_14331,])
func_14334 = relay.Function([], output)
mod['func_14334'] = func_14334
mod = relay.transform.InferType()(mod)
mutated_mod['func_14334'] = func_14334
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14334_call = mutated_mod.get_global_var('func_14334')
call_14335 = func_14334_call()
output = call_14335
func_14336 = relay.Function([], output)
mutated_mod['func_14336'] = func_14336
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11090_call = mod.get_global_var('func_11090')
func_11092_call = mutated_mod.get_global_var('func_11092')
call_14419 = relay.TupleGetItem(func_11090_call(), 0)
call_14420 = relay.TupleGetItem(func_11092_call(), 0)
output = call_14419
output2 = call_14420
func_14427 = relay.Function([], output)
mod['func_14427'] = func_14427
mod = relay.transform.InferType()(mod)
mutated_mod['func_14427'] = func_14427
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14427_call = mutated_mod.get_global_var('func_14427')
call_14428 = func_14427_call()
output = call_14428
func_14429 = relay.Function([], output)
mutated_mod['func_14429'] = func_14429
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3302_call = mod.get_global_var('func_3302')
func_3303_call = mutated_mod.get_global_var('func_3303')
call_14445 = relay.TupleGetItem(func_3302_call(), 0)
call_14446 = relay.TupleGetItem(func_3303_call(), 0)
func_4519_call = mod.get_global_var('func_4519')
func_4523_call = mutated_mod.get_global_var('func_4523')
var_14456 = relay.var("var_14456", dtype = "float64", shape = (112,))#candidate|14456|(112,)|var|float64
const_14457 = relay.const([True,True,False,True,False,True,True,False,True,True,False,False,True,True,False,False,False,True,False,False,True,True,True,False,False,False,True,True,False,True,False,True,False,False,True,True,False,False,True,True,False,True,False,True,False,False,True,False,False,True,False,True,True,False,True,True,False,False,True,False,True,True,False,False,True,True,True,True,True,False,True,True,True,True,True,True,True,False,True,True,False,True,False,True,True,True,False,True,True,True,False,True,False,False,True,False,True,False,True,False,False,False,False,True,True,True,False,True,True,True,False,True,False,True,False,False,False,True,True,False,False,True,True,True,True,False,True,False,False,False,True,False,True,True,True,False,False,True,True,True,False,False,True,False,True,True,False,True,False,False,True,True,True,False,False,True,False,True,True,False,True,False,False,False,True,True,True,True,False,False,True,False,False,False,True,True,True,True,True,False,True,False,True,True,True,True,False,True,False,True,False,True,False,False,False,True,False,True,True,False,True,False,True,False,False,False,True,True,True,False,True,True,True,False,False,False,True,False,True,True,True,True,True,True,False,True,True,False,False,False,False,True,False,True,True,False,True,True,True,True,True,True,False,False,True,False,False,True,False,False,False,True,True,True,True,True,False,False,True,False,False,False,False,False,True,True,False,True,False,True,False,False,False,False,False,False,False,True,True,False,True,True,True,False,True,False,False,True,False,True,False,False,True,False,False,True,True,False,False,False,False,False,False,False,False,False,False,False,True,True,False,False,True,True,True,False,False,True,True,False,False,True,True,False,True,True,True,True,False,True,True,False,True,True,False,True,True,True,True,True,False,True,True,True,False,False,True,False,True,True,True,False,False,False,False,False,True,True,True,True,False,False,True,True,True,False,False,False,True,True,True,True,False,True,True,False,True,False,True,True,True,False,True,False,False,True,False,True,False,True,True,False,True,False,True,False,False,True,False,True,False,False,True,False,True,False,False,False,False,True,True,False,True,False,False,True,True,False,True,True,True,False,True,False,False,False,False,True,True,False,False,True,False,True,True,True,True,False,False,False,True,True,False,True,False,False,False,True,False,True,True,True,True,False,True,False,True,True,True,False,True,True,False,False,True,True,True,False], dtype = "bool")#candidate|14457|(468,)|const|bool
call_14455 = relay.TupleGetItem(func_4519_call(relay.reshape(var_14456.astype('float64'), [112,]), relay.reshape(const_14457.astype('bool'), [12, 13, 3]), relay.reshape(const_14457.astype('bool'), [12, 13, 3]), ), 0)
call_14458 = relay.TupleGetItem(func_4523_call(relay.reshape(var_14456.astype('float64'), [112,]), relay.reshape(const_14457.astype('bool'), [12, 13, 3]), relay.reshape(const_14457.astype('bool'), [12, 13, 3]), ), 0)
output = relay.Tuple([call_14445,call_14455,var_14456,const_14457,])
output2 = relay.Tuple([call_14446,call_14458,var_14456,const_14457,])
func_14459 = relay.Function([var_14456,], output)
mod['func_14459'] = func_14459
mod = relay.transform.InferType()(mod)
mutated_mod['func_14459'] = func_14459
mutated_mod = relay.transform.InferType()(mutated_mod)
var_14460 = relay.var("var_14460", dtype = "float64", shape = (112,))#candidate|14460|(112,)|var|float64
func_14459_call = mutated_mod.get_global_var('func_14459')
call_14461 = func_14459_call(var_14460)
output = call_14461
func_14462 = relay.Function([var_14460], output)
mutated_mod['func_14462'] = func_14462
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11404_call = mod.get_global_var('func_11404')
func_11405_call = mutated_mod.get_global_var('func_11405')
call_14484 = relay.TupleGetItem(func_11404_call(), 2)
call_14485 = relay.TupleGetItem(func_11405_call(), 2)
output = relay.Tuple([call_14484,])
output2 = relay.Tuple([call_14485,])
func_14495 = relay.Function([], output)
mod['func_14495'] = func_14495
mod = relay.transform.InferType()(mod)
mutated_mod['func_14495'] = func_14495
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14495_call = mutated_mod.get_global_var('func_14495')
call_14496 = func_14495_call()
output = call_14496
func_14497 = relay.Function([], output)
mutated_mod['func_14497'] = func_14497
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11090_call = mod.get_global_var('func_11090')
func_11092_call = mutated_mod.get_global_var('func_11092')
call_14530 = relay.TupleGetItem(func_11090_call(), 0)
call_14531 = relay.TupleGetItem(func_11092_call(), 0)
func_5243_call = mod.get_global_var('func_5243')
func_5244_call = mutated_mod.get_global_var('func_5244')
call_14536 = relay.TupleGetItem(func_5243_call(), 0)
call_14537 = relay.TupleGetItem(func_5244_call(), 0)
output = relay.Tuple([call_14530,call_14536,])
output2 = relay.Tuple([call_14531,call_14537,])
func_14538 = relay.Function([], output)
mod['func_14538'] = func_14538
mod = relay.transform.InferType()(mod)
output = func_14538()
func_14539 = relay.Function([], output)
mutated_mod['func_14539'] = func_14539
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11267_call = mod.get_global_var('func_11267')
func_11269_call = mutated_mod.get_global_var('func_11269')
call_14542 = relay.TupleGetItem(func_11267_call(), 0)
call_14543 = relay.TupleGetItem(func_11269_call(), 0)
func_11141_call = mod.get_global_var('func_11141')
func_11142_call = mutated_mod.get_global_var('func_11142')
call_14559 = func_11141_call()
call_14560 = func_11141_call()
func_568_call = mod.get_global_var('func_568')
func_572_call = mutated_mod.get_global_var('func_572')
var_14572 = relay.var("var_14572", dtype = "float64", shape = (315,))#candidate|14572|(315,)|var|float64
call_14571 = relay.TupleGetItem(func_568_call(relay.reshape(var_14572.astype('float64'), [3, 7, 15]), relay.reshape(var_14572.astype('float64'), [3, 7, 15]), ), 1)
call_14573 = relay.TupleGetItem(func_572_call(relay.reshape(var_14572.astype('float64'), [3, 7, 15]), relay.reshape(var_14572.astype('float64'), [3, 7, 15]), ), 1)
output = relay.Tuple([call_14542,call_14559,call_14571,var_14572,])
output2 = relay.Tuple([call_14543,call_14560,call_14573,var_14572,])
func_14604 = relay.Function([var_14572,], output)
mod['func_14604'] = func_14604
mod = relay.transform.InferType()(mod)
var_14605 = relay.var("var_14605", dtype = "float64", shape = (315,))#candidate|14605|(315,)|var|float64
output = func_14604(var_14605)
func_14606 = relay.Function([var_14605], output)
mutated_mod['func_14606'] = func_14606
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9707_call = mod.get_global_var('func_9707')
func_9709_call = mutated_mod.get_global_var('func_9709')
call_14618 = relay.TupleGetItem(func_9707_call(), 1)
call_14619 = relay.TupleGetItem(func_9709_call(), 1)
func_4519_call = mod.get_global_var('func_4519')
func_4523_call = mutated_mod.get_global_var('func_4523')
const_14634 = relay.const([3.691310,5.952507,-6.296932,-0.448723,3.694046,4.781920,-2.968207,1.698694,-9.494124,-8.456830,-9.166837,9.319637,-9.518764,-9.923687,5.435405,-1.073484,3.518490,-8.382459,9.250022,7.393955,-2.812650,-5.100442,-4.125699,-2.541269,2.072993,-7.415369,3.770180,0.217950,2.562922,6.978666,-6.949828,5.272701,-4.177148,9.806059,-5.948309,-0.049939,6.978245,3.229283,-7.165936,-7.130806,8.747601,9.781115,8.598296,-3.372446,-4.079301,1.825735,9.967415,5.948714,-8.944512,-3.537270,9.050460,-8.352376,0.686715,-3.135890,3.351166,2.481139,4.993740,4.288669,0.894480,1.410519,-5.105210,-4.715698,9.387298,2.814581,0.995485,6.931841,-4.834918,2.603378,4.096160,6.790042,4.374394,5.928664,4.682320,7.737117,-2.948055,8.644147,0.877175,0.914236,2.563642,-4.044624,-5.841668,3.357370,6.493522,-2.984984,-8.794287,1.901087,-2.453464,3.593654,-6.785473,-2.220472,8.041431,9.261543,-7.832192,-3.072464,9.939407,-4.425347,-4.356111,-3.463481,-6.297566,-2.779379,-6.337442,-8.601481,6.791067,-7.573160,-8.024172,-4.102998,-6.600476,-1.826884,-6.448515,-0.891322,-1.878310,4.582160], dtype = "float64")#candidate|14634|(112,)|const|float64
var_14635 = relay.var("var_14635", dtype = "bool", shape = (78, 6))#candidate|14635|(78, 6)|var|bool
call_14633 = relay.TupleGetItem(func_4519_call(relay.reshape(const_14634.astype('float64'), [112,]), relay.reshape(var_14635.astype('bool'), [12, 13, 3]), relay.reshape(var_14635.astype('bool'), [12, 13, 3]), ), 2)
call_14636 = relay.TupleGetItem(func_4523_call(relay.reshape(const_14634.astype('float64'), [112,]), relay.reshape(var_14635.astype('bool'), [12, 13, 3]), relay.reshape(var_14635.astype('bool'), [12, 13, 3]), ), 2)
output = relay.Tuple([call_14618,call_14633,const_14634,var_14635,])
output2 = relay.Tuple([call_14619,call_14636,const_14634,var_14635,])
func_14639 = relay.Function([var_14635,], output)
mod['func_14639'] = func_14639
mod = relay.transform.InferType()(mod)
mutated_mod['func_14639'] = func_14639
mutated_mod = relay.transform.InferType()(mutated_mod)
var_14640 = relay.var("var_14640", dtype = "bool", shape = (78, 6))#candidate|14640|(78, 6)|var|bool
func_14639_call = mutated_mod.get_global_var('func_14639')
call_14641 = func_14639_call(var_14640)
output = call_14641
func_14642 = relay.Function([var_14640], output)
mutated_mod['func_14642'] = func_14642
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14427_call = mod.get_global_var('func_14427')
func_14429_call = mutated_mod.get_global_var('func_14429')
call_14676 = func_14427_call()
call_14677 = func_14427_call()
func_9122_call = mod.get_global_var('func_9122')
func_9124_call = mutated_mod.get_global_var('func_9124')
call_14680 = func_9122_call()
call_14681 = func_9122_call()
func_7317_call = mod.get_global_var('func_7317')
func_7318_call = mutated_mod.get_global_var('func_7318')
call_14684 = relay.TupleGetItem(func_7317_call(), 2)
call_14685 = relay.TupleGetItem(func_7318_call(), 2)
func_3483_call = mod.get_global_var('func_3483')
func_3485_call = mutated_mod.get_global_var('func_3485')
call_14687 = relay.TupleGetItem(func_3483_call(), 0)
call_14688 = relay.TupleGetItem(func_3485_call(), 0)
uop_14705 = relay.log2(call_14680.astype('float64')) # shape=(12, 9, 10)
uop_14707 = relay.log2(call_14681.astype('float64')) # shape=(12, 9, 10)
output = relay.Tuple([call_14676,call_14684,call_14687,uop_14705,])
output2 = relay.Tuple([call_14677,call_14685,call_14688,uop_14707,])
func_14724 = relay.Function([], output)
mod['func_14724'] = func_14724
mod = relay.transform.InferType()(mod)
output = func_14724()
func_14725 = relay.Function([], output)
mutated_mod['func_14725'] = func_14725
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13534_call = mod.get_global_var('func_13534')
func_13535_call = mutated_mod.get_global_var('func_13535')
call_14777 = relay.TupleGetItem(func_13534_call(), 0)
call_14778 = relay.TupleGetItem(func_13535_call(), 0)
output = call_14777
output2 = call_14778
func_14785 = relay.Function([], output)
mod['func_14785'] = func_14785
mod = relay.transform.InferType()(mod)
mutated_mod['func_14785'] = func_14785
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14785_call = mutated_mod.get_global_var('func_14785')
call_14786 = func_14785_call()
output = call_14786
func_14787 = relay.Function([], output)
mutated_mod['func_14787'] = func_14787
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7636_call = mod.get_global_var('func_7636')
func_7638_call = mutated_mod.get_global_var('func_7638')
call_14808 = relay.TupleGetItem(func_7636_call(), 0)
call_14809 = relay.TupleGetItem(func_7638_call(), 0)
output = relay.Tuple([call_14808,])
output2 = relay.Tuple([call_14809,])
func_14821 = relay.Function([], output)
mod['func_14821'] = func_14821
mod = relay.transform.InferType()(mod)
mutated_mod['func_14821'] = func_14821
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14821_call = mutated_mod.get_global_var('func_14821')
call_14822 = func_14821_call()
output = call_14822
func_14823 = relay.Function([], output)
mutated_mod['func_14823'] = func_14823
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7855_call = mod.get_global_var('func_7855')
func_7856_call = mutated_mod.get_global_var('func_7856')
call_14830 = relay.TupleGetItem(func_7855_call(), 0)
call_14831 = relay.TupleGetItem(func_7856_call(), 0)
func_9076_call = mod.get_global_var('func_9076')
func_9077_call = mutated_mod.get_global_var('func_9077')
call_14832 = func_9076_call()
call_14833 = func_9076_call()
func_6579_call = mod.get_global_var('func_6579')
func_6581_call = mutated_mod.get_global_var('func_6581')
call_14834 = relay.TupleGetItem(func_6579_call(), 0)
call_14835 = relay.TupleGetItem(func_6581_call(), 0)
output = relay.Tuple([call_14830,call_14832,call_14834,])
output2 = relay.Tuple([call_14831,call_14833,call_14835,])
func_14856 = relay.Function([], output)
mod['func_14856'] = func_14856
mod = relay.transform.InferType()(mod)
output = func_14856()
func_14857 = relay.Function([], output)
mutated_mod['func_14857'] = func_14857
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2899_call = mod.get_global_var('func_2899')
func_2900_call = mutated_mod.get_global_var('func_2900')
call_14880 = relay.TupleGetItem(func_2899_call(), 0)
call_14881 = relay.TupleGetItem(func_2900_call(), 0)
output = call_14880
output2 = call_14881
func_14884 = relay.Function([], output)
mod['func_14884'] = func_14884
mod = relay.transform.InferType()(mod)
mutated_mod['func_14884'] = func_14884
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14884_call = mutated_mod.get_global_var('func_14884')
call_14885 = func_14884_call()
output = call_14885
func_14886 = relay.Function([], output)
mutated_mod['func_14886'] = func_14886
mutated_mod = relay.transform.InferType()(mutated_mod)
var_14929 = relay.var("var_14929", dtype = "float32", shape = (9, 16, 16))#candidate|14929|(9, 16, 16)|var|float32
uop_14930 = relay.acos(var_14929.astype('float32')) # shape=(9, 16, 16)
output = relay.Tuple([uop_14930,])
output2 = relay.Tuple([uop_14930,])
F = relay.Function([var_14929,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_14929,], output2)
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
