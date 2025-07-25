import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_275 = relay.var("var_275", dtype = "int32", shape = (6, 7, 3))#candidate|275|(6, 7, 3)|var|int32
var_276 = relay.var("var_276", dtype = "int32", shape = (6, 7, 3))#candidate|276|(6, 7, 3)|var|int32
bop_277 = relay.left_shift(var_275.astype('int32'), relay.reshape(var_276.astype('int32'), relay.shape_of(var_275))) # shape=(6, 7, 3)
output = relay.Tuple([bop_277,])
output2 = relay.Tuple([bop_277,])
func_286 = relay.Function([var_275,var_276,], output)
mod['func_286'] = func_286
mod = relay.transform.InferType()(mod)
var_287 = relay.var("var_287", dtype = "int32", shape = (6, 7, 3))#candidate|287|(6, 7, 3)|var|int32
var_288 = relay.var("var_288", dtype = "int32", shape = (6, 7, 3))#candidate|288|(6, 7, 3)|var|int32
output = func_286(var_287,var_288,)
func_289 = relay.Function([var_287,var_288,], output)
mutated_mod['func_289'] = func_289
mutated_mod = relay.transform.InferType()(mutated_mod)
var_399 = relay.var("var_399", dtype = "bool", shape = (16, 16, 12))#candidate|399|(16, 16, 12)|var|bool
const_400 = relay.const([[[False,True,True,False,True,False,False,False,True,True,True,False],[False,False,True,True,False,False,True,True,False,False,False,False],[True,False,False,False,True,True,False,True,False,False,True,True],[False,True,True,True,False,True,False,False,True,True,False,False],[True,True,True,False,False,False,False,True,False,False,False,True],[True,False,False,True,False,False,False,False,True,False,False,False],[True,False,False,False,True,False,False,True,False,False,True,False],[False,True,True,False,False,True,True,True,False,True,True,False],[True,True,True,True,True,True,True,False,True,True,True,False],[False,True,True,False,True,False,False,True,False,True,True,False],[True,False,True,True,False,False,True,True,False,False,False,True],[True,True,False,False,True,True,True,True,False,False,True,False],[True,True,True,True,False,True,True,True,True,False,False,True],[True,False,True,True,False,True,False,False,True,False,False,False],[True,True,True,False,False,False,False,True,True,True,False,True],[False,True,True,False,True,True,True,False,True,False,True,False]],[[False,False,False,True,False,False,True,False,False,False,False,False],[False,False,True,True,True,True,False,False,False,True,False,True],[True,True,False,False,False,True,False,False,True,False,True,False],[True,False,False,True,False,False,True,False,False,False,True,True],[True,True,True,True,True,True,False,False,True,False,False,True],[False,True,True,True,True,False,True,False,False,True,True,False],[True,False,False,True,False,True,True,True,False,False,False,True],[False,True,True,True,True,False,False,True,True,True,True,False],[True,False,True,True,False,False,True,True,True,True,True,True],[False,False,True,False,False,True,False,False,False,True,True,False],[True,True,True,False,False,False,True,True,True,False,False,True],[False,True,False,True,False,True,True,False,True,False,True,False],[True,True,False,False,False,False,False,False,True,True,False,False],[False,True,True,True,True,False,False,False,True,False,True,False],[False,False,False,True,False,True,True,False,False,False,False,True],[False,False,True,True,True,True,True,True,True,True,False,False]],[[True,False,False,False,True,False,False,True,False,True,False,True],[False,False,True,True,False,True,False,False,True,True,True,False],[False,True,False,True,False,False,False,True,True,False,True,False],[False,False,True,True,True,True,False,True,True,True,False,True],[False,False,True,True,True,True,True,False,False,True,True,False],[False,True,True,True,False,False,True,False,False,False,True,True],[True,True,True,True,False,True,False,False,False,False,True,True],[True,True,True,True,False,True,True,False,False,False,True,False],[False,False,True,True,False,False,False,False,False,True,True,False],[True,True,True,True,True,False,False,False,True,False,True,False],[True,False,False,True,False,False,False,True,False,True,False,True],[True,False,True,True,False,False,False,True,True,True,False,True],[True,False,True,True,False,True,True,True,True,True,True,False],[True,True,True,False,False,True,True,True,True,False,True,True],[False,True,False,True,False,False,False,True,True,False,False,True],[True,True,True,False,True,False,False,False,True,True,False,True]],[[False,True,False,False,True,True,True,True,False,False,True,False],[False,True,False,True,True,False,True,False,False,False,True,True],[False,True,True,True,True,False,False,True,True,False,True,True],[False,True,False,False,True,True,True,True,True,True,True,False],[True,False,True,True,False,False,False,False,True,False,True,False],[False,True,False,True,True,True,False,True,False,True,False,True],[False,True,True,True,False,False,False,True,False,True,True,False],[True,True,False,False,True,True,True,True,False,True,True,True],[False,True,True,True,False,True,False,True,False,True,False,False],[True,False,True,True,True,False,True,False,False,True,True,True],[False,False,True,False,True,False,False,True,True,True,False,False],[False,True,True,False,False,True,False,False,False,True,True,True],[False,True,False,False,False,True,True,True,True,False,True,False],[False,True,True,False,False,False,False,False,True,True,False,True],[False,False,True,False,False,True,False,False,False,False,False,False],[True,True,True,False,False,True,False,False,False,True,False,True]],[[True,False,True,False,True,False,False,False,False,True,False,False],[False,False,False,False,False,False,True,True,False,False,True,False],[True,True,False,False,True,True,True,False,True,False,True,True],[False,True,True,True,False,True,True,True,False,False,True,False],[False,False,False,False,True,True,False,False,True,True,False,False],[False,True,False,True,False,True,False,False,False,True,True,True],[True,True,False,True,True,True,True,True,False,True,False,True],[True,False,True,False,True,False,False,True,True,False,True,True],[False,True,False,False,True,True,True,False,False,True,True,True],[True,False,True,True,False,True,False,True,True,True,True,True],[True,True,False,True,True,True,False,True,True,False,False,False],[False,True,False,False,True,True,False,False,True,True,True,True],[False,True,False,True,False,True,False,False,False,True,True,False],[False,True,True,True,False,True,True,False,True,True,False,False],[False,False,False,False,True,True,True,True,False,False,True,False],[True,True,False,False,False,True,False,True,True,True,False,True]],[[True,False,True,False,True,True,False,False,False,False,False,True],[True,True,True,True,True,False,True,True,True,False,True,False],[True,True,True,False,False,True,True,True,True,False,True,True],[False,True,True,False,True,True,True,False,False,False,True,False],[False,True,True,False,True,False,False,False,True,True,True,True],[False,False,True,False,True,False,True,True,False,False,True,True],[True,False,False,True,True,True,True,True,False,False,True,True],[False,True,False,True,False,True,True,True,True,False,True,False],[False,False,True,False,False,False,False,True,True,False,False,False],[True,False,True,False,False,True,True,True,False,True,False,True],[False,True,False,False,True,True,False,False,True,False,False,True],[False,False,False,True,False,False,True,False,False,True,False,True],[False,True,False,False,True,False,True,True,False,True,True,True],[False,False,True,True,False,False,False,False,False,False,False,True],[True,True,True,True,False,True,False,False,False,False,True,True],[True,False,True,True,False,False,False,False,False,False,False,False]],[[False,False,True,False,True,True,True,False,False,False,True,True],[True,False,True,False,False,False,True,True,True,False,False,True],[True,True,True,True,True,True,False,True,False,True,True,True],[False,True,True,False,True,False,True,True,False,True,True,True],[True,False,False,False,True,True,True,False,False,True,True,True],[False,True,False,False,False,True,True,False,False,False,True,False],[True,False,True,True,True,False,False,True,False,True,True,True],[False,True,True,False,False,True,True,False,False,True,True,True],[False,False,True,True,True,False,True,False,True,False,True,False],[False,False,True,False,True,True,False,True,False,True,True,False],[False,False,False,True,True,True,False,True,False,True,False,True],[False,True,True,True,True,False,True,True,False,True,False,True],[False,False,False,False,True,True,False,False,True,False,True,False],[False,True,False,False,False,False,True,False,False,False,True,True],[False,True,True,True,False,True,False,False,True,True,False,False],[False,False,False,False,False,True,False,False,False,False,False,True]],[[True,True,True,True,True,True,False,False,False,True,True,False],[False,True,False,True,False,False,False,True,False,False,True,False],[False,True,True,False,False,True,True,True,True,True,False,False],[False,False,False,False,False,True,False,False,True,False,False,True],[False,False,False,False,False,True,False,False,True,True,True,True],[True,False,False,False,True,False,False,True,False,True,True,False],[False,True,True,True,True,True,True,True,True,True,True,True],[True,False,False,False,True,True,True,False,True,True,False,True],[True,True,False,True,False,False,False,False,True,True,False,True],[False,True,False,True,False,False,False,True,False,False,True,True],[True,False,False,True,True,False,False,False,True,False,False,True],[False,False,False,False,True,False,True,True,True,True,False,True],[True,False,True,True,True,False,True,False,True,True,True,False],[True,True,True,True,False,True,False,False,True,False,False,False],[False,True,True,True,True,True,True,False,True,False,False,False],[False,True,True,True,False,False,False,True,False,True,False,False]],[[False,True,False,True,True,True,True,False,False,False,True,True],[True,False,False,False,False,False,True,True,True,False,False,True],[False,False,False,False,True,True,False,True,False,True,False,True],[False,True,True,False,True,True,False,False,True,False,True,False],[False,False,True,True,False,True,False,False,False,False,True,True],[True,True,True,True,False,True,True,False,True,False,True,False],[True,True,True,True,True,False,True,True,False,False,False,False],[True,False,False,True,False,True,True,False,True,False,True,True],[True,False,False,False,True,True,True,False,False,False,True,True],[False,False,False,False,False,False,False,False,False,False,True,False],[False,False,False,True,False,False,False,False,False,False,False,True],[True,True,False,True,True,True,False,True,False,False,True,False],[False,True,False,False,False,False,True,False,False,True,True,True],[True,True,True,False,False,True,True,True,True,True,True,False],[True,True,False,True,False,True,True,False,True,False,True,True],[False,False,True,False,True,False,True,True,True,False,True,True]],[[False,False,True,True,False,False,True,True,True,True,False,True],[True,True,False,False,True,True,True,True,True,False,False,False],[False,True,True,True,False,False,True,False,True,False,True,True],[False,False,False,True,False,False,True,True,True,True,True,True],[False,False,False,True,False,False,True,False,False,True,True,False],[True,False,False,False,False,True,True,False,True,True,False,True],[True,True,False,True,False,True,False,False,True,False,True,True],[True,False,True,True,True,True,True,True,True,True,True,False],[False,True,False,True,False,False,True,False,True,True,True,True],[True,True,True,False,True,False,False,False,True,True,True,False],[False,False,True,False,True,True,False,True,False,False,True,False],[True,False,False,False,True,True,False,False,False,True,True,False],[False,True,False,True,False,False,True,True,False,True,True,False],[False,True,True,False,True,False,False,False,False,True,True,False],[False,True,False,True,False,True,True,False,False,True,True,True],[True,True,False,False,False,True,False,False,False,True,False,True]],[[False,False,False,False,True,True,False,False,False,True,True,False],[False,False,True,True,True,False,False,True,True,False,True,True],[True,True,True,True,False,True,False,False,False,False,True,True],[True,True,True,True,False,False,False,True,False,True,False,False],[True,False,True,True,False,False,False,True,True,False,False,True],[True,False,False,True,True,True,True,False,False,False,False,True],[True,False,False,True,True,False,True,False,False,False,True,False],[False,False,True,True,False,True,True,True,True,True,True,False],[False,False,True,False,False,True,True,True,True,True,True,False],[True,False,False,True,True,False,True,True,False,False,True,False],[True,False,True,True,True,False,True,True,False,False,True,True],[True,True,False,False,False,True,False,False,False,True,True,True],[True,True,False,True,True,True,True,True,True,False,False,False],[True,True,True,True,False,True,False,True,False,True,False,False],[False,False,False,False,True,False,True,False,True,False,True,False],[True,False,True,True,True,True,True,False,True,True,True,True]],[[False,False,False,False,True,False,False,True,True,True,False,False],[True,True,True,False,True,False,False,True,True,False,False,False],[True,True,False,False,False,True,True,False,True,False,False,False],[False,True,False,True,False,False,False,True,True,True,True,True],[True,True,False,False,True,False,False,True,True,False,True,False],[False,True,False,True,True,True,False,True,False,False,True,False],[False,True,True,True,False,False,False,True,True,False,False,True],[False,False,False,False,True,True,False,True,False,False,False,True],[True,False,True,True,False,False,True,False,True,False,False,True],[False,False,False,False,True,False,True,True,True,True,True,False],[False,True,True,True,False,True,False,True,False,True,True,False],[True,False,True,False,True,True,True,True,True,False,True,False],[False,False,False,True,True,True,True,False,True,False,True,True],[False,True,False,False,True,True,False,False,False,True,True,True],[False,False,False,False,False,False,False,True,False,False,False,False],[False,False,False,True,False,True,False,False,False,False,False,True]],[[False,True,False,False,False,True,True,True,True,True,True,False],[True,True,True,False,False,True,False,False,True,False,True,False],[True,True,False,True,True,True,True,True,False,True,True,False],[False,False,True,True,False,False,True,True,False,False,True,False],[False,True,False,True,True,True,True,False,False,False,False,True],[True,True,True,True,False,False,True,False,True,True,True,True],[True,True,False,True,True,False,True,True,True,True,True,True],[False,False,True,False,False,True,False,True,False,True,False,False],[True,False,False,False,True,False,True,False,True,False,False,False],[False,True,False,True,True,True,False,True,True,False,False,False],[True,False,True,False,True,False,False,False,False,True,True,True],[True,False,True,False,False,True,False,False,True,False,False,False],[True,False,True,True,False,True,True,False,True,False,False,False],[False,False,True,False,True,False,True,False,False,True,False,True],[False,True,True,True,True,True,True,True,False,True,False,False],[False,True,False,False,True,False,False,False,True,True,False,False]],[[True,False,True,False,True,True,True,True,False,False,True,False],[False,False,True,False,True,True,False,False,False,True,False,True],[True,False,True,False,False,False,True,True,False,False,True,True],[True,False,False,False,True,True,False,True,False,True,True,True],[False,True,True,False,False,True,True,False,False,True,False,False],[True,True,True,True,True,True,False,True,True,False,True,False],[False,True,True,False,False,False,True,False,False,True,False,False],[False,True,False,False,False,True,False,True,False,False,False,False],[True,False,True,False,True,False,True,True,True,False,True,True],[True,False,True,True,True,True,True,False,False,False,False,True],[True,True,False,True,True,True,True,False,True,False,False,False],[False,True,True,True,False,False,False,True,True,True,False,False],[False,True,False,True,True,True,False,False,False,False,False,True],[True,True,True,True,False,True,True,False,True,True,False,True],[True,False,False,False,False,False,True,False,True,True,True,True],[False,True,True,False,False,True,True,True,True,False,False,True]],[[False,False,True,True,True,True,False,False,False,False,True,False],[False,False,False,True,True,False,False,False,True,False,False,True],[True,False,True,False,False,True,True,False,True,True,True,False],[False,True,True,False,True,False,False,True,False,True,True,True],[True,True,True,False,True,False,False,True,False,True,True,False],[False,True,True,False,False,False,False,False,False,True,True,True],[True,True,True,True,False,False,True,True,True,False,False,True],[False,False,False,False,True,True,True,True,False,False,True,False],[False,False,True,False,True,False,False,True,True,True,False,False],[True,True,True,False,False,True,True,False,True,True,True,False],[True,False,False,True,False,True,False,False,True,True,True,True],[True,True,False,False,False,False,False,True,False,False,True,False],[True,True,False,True,False,True,True,True,True,True,True,True],[True,True,False,False,False,True,True,True,False,True,True,False],[False,False,True,False,False,False,False,True,True,False,False,False],[False,False,True,True,True,False,True,False,True,True,True,True]],[[False,False,False,False,False,False,False,False,False,True,False,False],[True,False,True,True,False,False,True,False,False,False,False,True],[True,True,False,False,False,True,False,False,True,False,False,True],[False,False,True,False,True,True,False,False,True,False,True,False],[False,False,False,False,True,False,True,False,True,True,False,True],[False,False,True,False,True,True,True,True,True,True,False,False],[False,False,True,False,False,False,False,False,True,False,False,False],[True,False,False,False,True,False,False,False,True,True,False,False],[True,True,True,False,False,True,True,True,False,False,True,False],[False,True,True,True,True,True,True,False,True,True,True,True],[False,True,True,True,False,True,True,True,False,False,False,True],[False,True,False,False,True,True,False,True,False,True,True,True],[True,False,False,False,False,True,True,False,False,False,True,False],[True,False,False,False,False,False,True,False,True,True,False,False],[False,True,True,False,False,False,True,True,True,True,False,True],[False,True,True,False,False,False,True,True,False,True,True,False]]], dtype = "bool")#candidate|400|(16, 16, 12)|const|bool
bop_401 = relay.logical_or(var_399.astype('bool'), relay.reshape(const_400.astype('bool'), relay.shape_of(var_399))) # shape=(16, 16, 12)
uop_414 = relay.sigmoid(const_400.astype('float64')) # shape=(16, 16, 12)
func_286_call = mod.get_global_var('func_286')
func_289_call = mutated_mod.get_global_var('func_289')
var_417 = relay.var("var_417", dtype = "int32", shape = (63, 2))#candidate|417|(63, 2)|var|int32
call_416 = relay.TupleGetItem(func_286_call(relay.reshape(var_417.astype('int32'), [6, 7, 3]), relay.reshape(var_417.astype('int32'), [6, 7, 3]), ), 0)
call_418 = relay.TupleGetItem(func_289_call(relay.reshape(var_417.astype('int32'), [6, 7, 3]), relay.reshape(var_417.astype('int32'), [6, 7, 3]), ), 0)
func_286_call = mod.get_global_var('func_286')
func_289_call = mutated_mod.get_global_var('func_289')
call_421 = relay.TupleGetItem(func_286_call(relay.reshape(call_416.astype('int32'), [6, 7, 3]), relay.reshape(call_416.astype('int32'), [6, 7, 3]), ), 0)
call_422 = relay.TupleGetItem(func_289_call(relay.reshape(call_416.astype('int32'), [6, 7, 3]), relay.reshape(call_416.astype('int32'), [6, 7, 3]), ), 0)
bop_426 = relay.left_shift(uop_414.astype('int64'), relay.reshape(const_400.astype('int64'), relay.shape_of(uop_414))) # shape=(16, 16, 12)
uop_437 = relay.sinh(var_399.astype('float64')) # shape=(16, 16, 12)
output = relay.Tuple([bop_401,call_416,var_417,call_421,bop_426,uop_437,])
output2 = relay.Tuple([bop_401,call_418,var_417,call_422,bop_426,uop_437,])
func_451 = relay.Function([var_399,var_417,], output)
mod['func_451'] = func_451
mod = relay.transform.InferType()(mod)
mutated_mod['func_451'] = func_451
mutated_mod = relay.transform.InferType()(mutated_mod)
func_451_call = mutated_mod.get_global_var('func_451')
var_453 = relay.var("var_453", dtype = "bool", shape = (16, 16, 12))#candidate|453|(16, 16, 12)|var|bool
var_454 = relay.var("var_454", dtype = "int32", shape = (63, 2))#candidate|454|(63, 2)|var|int32
call_452 = func_451_call(var_453,var_454,)
output = call_452
func_455 = relay.Function([var_453,var_454,], output)
mutated_mod['func_455'] = func_455
mutated_mod = relay.transform.InferType()(mutated_mod)
const_465 = relay.const([[-2,-3,-4,7,5,-6,5,-4,-9],[10,-9,-9,-7,1,7,-3,10,8],[-10,2,10,10,1,-2,-8,6,-9],[6,-7,4,-10,2,5,-7,-4,-2]], dtype = "uint64")#candidate|465|(4, 9)|const|uint64
var_466 = relay.var("var_466", dtype = "uint64", shape = (4, 9))#candidate|466|(4, 9)|var|uint64
bop_467 = relay.less_equal(const_465.astype('bool'), relay.reshape(var_466.astype('bool'), relay.shape_of(const_465))) # shape=(4, 9)
func_451_call = mod.get_global_var('func_451')
func_455_call = mutated_mod.get_global_var('func_455')
const_474 = relay.const([False,True,True,False,False,False,True,False,False,True,True,False,False,True,False,True,False,True,False,True,False,False,True,False,False,True,True,False,False,True,False,False,False,True,True,False,False,False,False,False,False,True,False,False,False,True,False,True,False,False,False,True,True,True,True,True,False,False,True,False,True,True,True,False,True,False,False,True,False,True,True,False,False,False,True,True,True,True,False,True,True,False,False,False,True,False,False,False,False,True,False,False,True,True,False,False,True,False,True,False,True,False,False,False,False,True,True,True,False,True,True,False,True,True,False,False,True,False,False,False,False,True,False,True,False,False,True,False,False,False,False,False,False,False,False,True,False,True,False,False,False,True,False,True,True,True,True,False,True,False,False,True,True,False,False,True,False,True,True,True,True,True,True,False,False,True,True,False,False,True,False,False,True,True,True,False,False,False,False,True,False,True,True,True,True,True,True,False,True,False,True,False,False,False,False,False,True,True,False,True,True,False,True,False,True,False,False,True,False,False,True,True,True,False,False,True,True,True,True,False,False,False,True,False,False,True,False,True,True,False,False,False,False,True,False,False,True,False,True,True,False,False,False,False,False,True,True,False,False,False,False,False,False,True,False,False,True,False,True,False,False,True,False,True,False,False,True,True,False,False,False,False,True,True,False,True,False,True,True,False,True,False,True,True,True,True,True,False,False,False,False,False,True,False,True,True,False,False,False,False,True,True,True,False,False,True,True,False,True,True,False,False,True,True,False,False,True,True,True,True,False,True,True,True,False,True,True,False,True,True,True,False,False,False,False,False,True,False,False,False,True,True,True,False,False,True,False,True,False,True,False,False,True,False,False,True,True,True,True,False,False,False,True,True,False,True,True,False,True,False,False,False,True,True,False,True,False,True,True,True,False,True,True,True,True,True,False,False,False,False,True,True,False,False,False,True,True,True,True,True,True,True,True,False,True,False,False,True,True,True,False,True,False,False,True,False,True,True,False,False,True,True,True,False,True,True,True,True,False,False,False,False,True,True,False,False,True,False,False,False,True,False,False,False,False,True,False,False,False,False,False,False,False,True,False,True,False,True,False,False,True,False,False,False,False,True,True,True,True,True,False,True,True,False,True,False,True,True,False,True,True,False,True,True,True,True,True,True,False,True,True,True,False,False,False,False,True,True,True,False,False,True,True,True,True,False,True,False,True,True,False,True,True,True,False,False,True,True,True,True,True,True,True,True,True,True,True,False,False,False,False,False,False,False,True,True,False,True,False,False,False,False,True,False,True,True,False,False,True,False,False,False,True,True,True,False,False,False,False,False,False,False,False,False,False,True,False,True,False,False,True,True,False,False,True,True,True,True,False,False,True,False,False,False,True,True,False,True,True,False,True,False,True,True,False,True,False,False,False,True,False,True,False,False,True,True,False,True,False,False,True,False,False,False,False,True,True,True,False,True,True,True,True,False,False,True,False,False,False,False,True,False,False,True,True,True,False,True,False,True,True,False,True,True,False,True,False,True,False,False,False,False,True,True,False,True,True,False,True,True,True,True,True,True,False,False,False,True,True,True,False,False,True,True,True,True,False,True,False,True,True,True,True,False,False,True,True,True,False,True,False,True,False,False,False,False,False,False,True,False,True,True,False,False,False,False,True,True,True,False,False,True,True,True,True,True,False,True,True,False,False,True,True,False,True,True,False,False,False,False,False,True,True,False,False,False,False,True,True,False,True,True,True,False,False,False,False,False,True,True,True,True,False,False,True,False,False,False,False,False,False,False,True,True,False,True,True,True,True,False,True,False,True,False,True,True,False,True,False,False,False,True,True,False,True,True,False,True,True,False,True,True,False,True,False,True,False,False,False,True,False,True,False,False,True,True,True,True,False,True,True,False,False,True,False,False,False,True,True,True,True,True,False,False,False,False,True,False,False,True,False,True,False,False,True,True,True,False,False,True,False,False,True,False,True,True,False,True,False,False,False,False,True,False,False,True,False,True,True,True,False,True,False,False,True,True,True,False,True,True,True,True,True,False,False,False,False,False,True,False,False,True,False,True,True,False,False,False,True,False,True,True,True,True,True,True,False,False,True,True,False,True,True,True,True,True,False,True,True,True,False,False,True,False,True,False,True,False,False,False,False,True,False,True,False,True,False,False,False,False,False,False,True,True,True,False,False,True,False,True,True,False,True,False,False,True,False,True,True,True,False,True,False,False,False,True,True,True,True,True,True,True,True,False,False,True,False,False,False,False,False,True,False,True,True,True,False,False,False,True,True,False,False,True,False,True,False,False,False,False,True,True,True,True,True,False,False,True,False,False,False,False,False,False,False,True,True,False,True,False,False,False,False,False,False,True,True,False,True,True,False,False,False,False,True,True,False,True,True,False,False,True,True,False,True,True,True,True,True,True,True,True,True,True,False,True,False,True,False,True,True,False,False,True,False,True,True,False,True,False,True,True,True,False,True,False,True,False,True,False,True,False,False,True,False,False,False,False,True,False,False,False,True,False,False,True,True,True,False,False,True,True,True,False,True,False,False,False,True,False,False,False,False,False,True,False,False,False,True,False,False,True,False,True,True,False,True,False,True,True,True,False,False,False,False,True,True,True,True,False,True,True,False,True,False,False,False,False,False,True,False,False,False,True,False,True,True,True,True,True,False,False,True,False,True,False,True,False,True,False,False,False,True,False,True,True,False,True,False,False,False,False,True,False,True,True,True,True,False,True,False,False,True,True,False,False,True,True,False,False,True,False,False,False,True,False,False,True,True,False,False,False,False,True,False,False,False,False,True,False,True,True,False,False,False,False,True,False,True,True,False,False,False,True,False,True,True,False,False,False,False,False,False,True,True,True,True,True,True,False,True,False,True,True,False,True,True,True,True,False,True,False,False,True,True,True,False,False,True,False,False,False,True,True,True,False,False,False,False,True,False,True,True,True,True,True,False,False,True,False,True,False,False,True,True,True,False,True,True,False,True,True,False,False,False,True,True,False,True,True,True,True,False,False,False,True,False,False,False,True,False,True,True,False,False,False,True,True,True,False,True,False,False,True,True,False,False,False,True,True,True,False,False,True,True,False,True,True,False,True,False,True,False,True,True,False,True,True,True,False,True,False,False,True,True,True,False,True,True,True,False,False,True,False,False,False,False,True,True,True,False,True,False,False,False,True,False,True,False,False,True,False,False,False,True,False,True,True,True,True,False,False,True,False,False,True,False,True,False,False,False,False,True,False,False,False,True,True,True,False,True,True,False,True,True,True,True,False,True,True,True,True,True,True,True,True,False,False,False,True,False,False,True,True,False,False,True,False,True,True,False,False,False,False,True,True,True,True,True,False,False,True,False,True,False,True,False,False,True,True,True,True,True,True,True,False,True,False,False,False,True,False,False,True,False,True,False,True,False,False,False,False,True,False,True,True,True,False,True,True,True,True,False,False,False,True,False,True,False,False,True,True,False,True,True,False,False,True,False,True,True,False,True,False,False,True,True,True,True,True,False,False,False,True,False,False,False,True,True,False,True,False,False,False,True,True,False,True,False,False,False,False,False,False,False,False,True,False,False,False,True,False,False,True,True,False,True,False,True,False,False,True,False,False,True,True,True,True,False,False,False,True,False,False,True,False,True,False,False,True,False,True,True,False,False,True,False,True,True,False,True,True,True,True,False,False,False,True,True,True,True,True,False,True,False,True,False,True,True,False,False,True,False,True,True,False,False,True,False,True,True,True,True,False,True,True,False,True,False,False,False,False,True,False,True,True,True,True,False,False,False,False,True,False,False,False,False,False,False,False,False,True,False,True,False,True,False,False,False,False,False,True,False,False,True,False,True,True,True,False,True,True,False,True,True,False,True,False,True,True,False,True,True,False,False,True,True,False,True,False,False,False,True,True,False,False,True,True,True,False,True,True,False,False,False,True,False,True,True,True,True,False,False,False,False,False,True,False,False,False,False,True,False,True,False,False,True,True,False,True,True,True,False,True,True,False,True,False,True,False,True,False,False,False,False,True,False,True,True,True,False,True,False,False,False,False,True,True,True,True,False,False,False,False,False,False,False,True,False,False,True,True,False,False,True,True,True,False,False,False,True,False,True,True,True,True,True,False,False,False,True,True,False,True,True,False,True,False,True,True,False,True,True,False,True,False,True,False,False,False,False,True,False,True,False,True,False,True,True,False,True,False,True,False,False,True,False,True,True,False,True,True,True,False,True,False,False,True,False,True,True,False,False,True,True,True,True,True,False,False,True,False,True,True,False,True,False,False,False,True,False,True,False,True,True,True,True,False,False,True,True,True,True,True,True,False,False,False,True,True,False,True,True,True,False,True,False,False,True,True,True,False,False,True,True,False,False,True,False,True,False,True,False,False,False,True,False,True,True,False,False,False,True,True,True,True,False,False,True,True,True,False,True,True,True,True,True,True,False,True,False,False,False,True,False,True,False,True,False,False,True,False,False,False,True,True,True,True,True,False,False,False,False,False,False,True,True,True,False,True,True,True,True,True,False,False,False,False,True,False,False,False,False,False,False,True,False,True,False,True,True,True,False,True,True,False,False,False,True,False,True,False,True,False,False,True,False,False,False,True,True,False,True,True,True,True,True,True,False,True,False,True,False,False,False,True,False,False,True,False,True,False,False,False,True,False,False,True,True,False,True,False,False,False,True,True,False,False,False,False,False,True,False,False,True,False,False,False,True,True,False,False,False,False,False,True,True,False,False,False,False,True,False,True,False,True,False,False,False,True,False,False,False,False,False,True,True,False,True,False,False,True,False,False,False,False,True,True,True,True,True,True,True,True,False,True,False,True,True,False,False,True,False,False,False,True,True,True,True,True,True,True,False,True,True,False,True,False,True,False,False,False,False,True,True,False,False,False,True,True,False,True,False,True,True,False,False,True,True,True,False,False,True,False,True,False,True,True,True,False,True,True,True,True,False,False,False,False,False,True,True,True,True,True,False,False,False,False,True,True,True,True,False,False,False,True,True,True,False,False,True,False,True,False,True,True,True,True,True,True,True,False,False,False,True,False,False,True,False,False,True,False,True,True,False,True,False,True,False,True,True,False,True,False,False,False,True,True,False,False,True,True,False,True,True,False,False,True,True,False,True,False,False,True,True,True,False,False,False,True,True,False,True,False,False,True,False,False,True,False,False,False,True,True,True,False,True,True,False,False,False,True,True,False,False,False,True,True,False,False,False,True,False,True,True,False,False,False,False,True,False,True,True,False,False,True,False,True,False,False,True,False,False,False,True,False,True,False,True,True,False,True,True,False,False,False,True,True,False,True,False,True,False,False,True,False,True,True,True,True,False,True,False,False,True,True,False,False,True,False,False,False,True,True,False,False,True,True,True,False,True,True,True,True,True,False,False,False,True,True,False,True,False,False,True,False,True,False,False,False,False,False,False,True,True,True,True,True,False,False,True,True,False,False,True,True,False,True,False,True,False,False,True,True,False,False,True,True,False,True,True,False,False,False,False,True,True,True,False,True,False,True,True,False,True,False,True,True,True,True,True,True,True,False,False,True,False,True,False,True,True,False,True,True,False,True,False,True,True,True,False,True,False,True,True,False,True,False,True,False,False,False,False,True,False,False,True,True,False,True,False,True,True,True,False,True,True,False,False,False,True,True,True,False,False,False,False,False,False,True,False,False,False,False,False,False,True,True,True,True,False,True,False,False,True,False,True,False,False,False,False,False,True,True,False,True,True,False,True,True,True,False,False,True,False,False,False,True,True,True,False,True,True,False,True,False,False,True,False,True,True,False,True,False,True,True,True,False,True,True,True,False,True,True,False,True,True,False,True,False,True,True,False,False,False,True,False,False,False,False,True,True,False,False,True,True,True,True,True,False,False,True,True,True,False,True,False,False,True,True,False,False,True,False,True,True,False,True,True,False,False,True,False,False,True,True,False,True,False,True,True,False,False,False,True,True,True,False,True,False,True,True,True,False,False,False,True,False,True,True,False,True,False,False,False,True,False,False,False,False,True,False,True,False,False,False,True,False,False,False,False,False,True,True,False,True,True,False,True,True,True,False,False,True,False,False,False,False,False,True,True,False,True,False,False,True,False,True,True,True,True,False,True,False,True,True,False,True,True,True,False,False,True,False,True,False,True,False,False,True,True,True,True,False,True,True,True,False,False,True,True,True,True,False,False,False,True,False,True,True,True,True,True,True,False,True,True,True,True,True,False,False,True,False,False,False,True,True,False,False,False,True,True,True,True,True,False,True,True,True,False,True,True,True,False,True,False,True,False,True,False,False,True,True,False,True,False,False,True,False,False,True,False,True,True,True,True,True,False,False,False,False,True,True,False,True,False,False,False,False,False,True,True,True,False,True,True,False,True,False,True,True,True,True,True,False,False,False,True,True,False,False,True,False,True,True,True,False,False,False,False,False,True,True,True,True,True,False,False,False,False,True,False,False,False,True,False,False,True,False,True,True,False,True,True,True,False,True,True,False,True,False,False,False,True,False,True,False,False,True,True,True,False,True,True,False,False,True,True,True,True,False,False,True,True,False,True,False,True,False,False,False,False,True,False,False,True,True,False,True,True,True,False,True,False,True,False,False,True,True,True,False,True,False,False,True,False,True,True,True,True,True,True,False,False,True,False,True,False,False,True,True,False,True,True,False,True,True,True,False,False,False,False,True,False,False,False,False,True,True,True,True,True,False,True,True,True,True,True,False,True,False,True,True,True,False,False,False,True,True,False,True,True,True,True,False,True,True,False,True,True,False,False,False,False,True,True,False,False,False,False,True,False,True,True,False,False,True,False,True,False,True,True,True,False,False,True,True,True,False,False,False,False,False,False,False,True,False,False,True,False,False,True,True,False,False,True,False,True,True,True,True,False,False,False,False,False,False,False,False,False,False,False,False,True,True,False,False,True,True,False,True,True,True,False,True,True,True,True,False,True,True,True,True,True,True,False,False,True,False,False,True,False,False,True,True,True,False,False,False,True,False,False,False,True,False,False,False,False,True,False,True,False,True,False,False,False,False,False,False,False,False], dtype = "bool")#candidate|474|(3072,)|const|bool
var_475 = relay.var("var_475", dtype = "int32", shape = (126,))#candidate|475|(126,)|var|int32
call_473 = relay.TupleGetItem(func_451_call(relay.reshape(const_474.astype('bool'), [16, 16, 12]), relay.reshape(var_475.astype('int32'), [63, 2]), ), 1)
call_476 = relay.TupleGetItem(func_455_call(relay.reshape(const_474.astype('bool'), [16, 16, 12]), relay.reshape(var_475.astype('int32'), [63, 2]), ), 1)
const_482 = relay.const([True,False,False,False,False,True,False,False,False,False,False,True,False,False,False,True,False,True,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,True,False,True,False,False,True,False,True,True,False,True,True,False,False,True,True,True,True,True,True,False,True,True,False,False,True,True,False,False,True,True,True,False,False,True,False,True,True,True,False,True,False,True,True,True,True,False,False,False,True,True,False,True,True,False,True,False,True,True,False,True,False,True,True,False,False,True,True,False,True,True,True,True,True,True,False,False,True,False,False,True,False,True,False,True,True,True,True,True,False,False,False,True,True,True,True,False,False,True,False,True,False,True,True,True,False,True,True,False,False,False,True,False,True,True,True,False,False,False,True,False,False,True,True,False,False,True,False,True,False,False,False,False,True,True,False,False,True,True,False,True,True,True,True,False,False,False,True,False,False,False,False,True,False,False,True,False,True,True,True,True,True,False,True,False,True,True,False,False,True,False,True,False,True,False,True,True,False,False,True,True,False,False,False,False,False,True,True,True,False,False,False,True,False,True,True,False,True,False,False,False,False,False,False,False,False,True,True,True,True,True,False,False,True,False,False,True,True,True,False,True,False,False,False,False,True,True,False,False,True,True,False,False,True,True,False,True,False,True,False,False,False,False,False,True,False,False,False,True,False,False,False,False,False,False,False,False,False,True,False,True,False,True,True,True,False,True,False,False,True,True,False,True,True,False,True,False,True,True,True,True,False,False,True,False,False,True,False,False,False,True,False,False,False,True,True,False,True,False,False,False,True,True,True,False,True,False,False,False,False,False,True,False,False,False,False,False,False,True,True,False,False,True,True,False,False,False,False,True,False,False,True,True,True,True,False,True,True,False,True,True,False,True,True,False,True,False,True,True,True,False,False,True,True,True,True,True,True,True,True,False,True,False,True,True,True,True,False,True,False,True,False,False,False,False,True,False,False,False,True,True,False,True,False,True,False,True,False,False,False,True,False,True,False,True,False,True,True,False,False,True,False,True,True,False,True,False,False,True,False,False,False,False,True,False,True,False,True,False,False,True,True,False,False,True,True,True,True,False,True,True,True,True,False,True,False,True,True,False,False,False,False,False,False,False,False,False,False,True,False,False,False,True,False,True,True,True,False,False,False,True,True,True,True,False,False,True,True,False,True,False,False,False,False,False,False,True,False,False,False,False,False,True,False,False,False,True,True,False,True,True,True,False,True,False,False,True,True,False,True,True,False,True,True,False,False,True,True,False,True,False,True,True,True,True,True,True,False,False,True,True,False,False,True,True,True,False,False,False,False,False,True,False,True,False,False,True,True,False,False,False,False,True,True,True,False,False,False,False,True,True,True,True,True,False,False,False,False,False,True,False,False,False,False,False,True,True,True,False,True,True,True,True,False,False,False,False,True,False,False,False,True,True,True,False,False,True,True,False,True,False,True,False,False,True,False,True,False,True,False,True,True,True,False,True,True,False,False,False,False,False,False,True,False,True,False,False,False,True,False,False,True,True,False,True,True,False,True,True,True,True,True,False,False,True,False,True,False,False,False,False,False,False,False,False,False,False,False,False,True,True,False,False,False,False,True,True,False,False,True,False,True,False,False,True,True,False,True,True,False,True,False,True,True,False,True,True,False,False,False,True,True,False,True,True,True,False,True,True,True,False,True,False,False,False,False,True,False,True,True,True,False,True,False,True,True,True,True,True,True,True,False,False,True,True,False,False,True,True,False,False,True,True,True,True,True,True,False,False,False,True,True,False,False,True,True,True,False,False,False,False,True,False,False,True,True,False,True,True,True,True,True,False,True,False,True,False,True,False,False,True,True,True,True,False,False,True,True,True,True,False,True,True,False,True,False,False,False,True,True,True,True,False,False,False,True,True,False,False,True,True,False,True,False,True,True,True,False,False,False,False,False,True,True,True,False,True,True,False,False,False,False,True,False,False,True,True,True,False,False,True,True,False,False,True,True,True,False,False,True,False,False,False,True,True,True,False,False,False,False,False,False,False,False,False,False,True,False,False,True,False,True,False,False,True,False,True,False,False,True,True,True,True,True,False,False,False,False,False,False,True,True,False,True,True,True,False,False,True,False,False,True,True,False,True,False,False,False,False,True,False,True,False,True,True,False,False,True,True,False,False,False,True,False,True,False,True,True,True,False,True,True,True,False,True,False,False,False,True,False,True,True,False,True,False,True,True,False,False,False,True,False,False,False,True,False,True,False,True,False,True,True,True,False,True,False,True,False,False,False,False,True,True,False,False,True,True,False,False,False,False,True,False,True,True,True,True,False,False,False,False,True,True,True,True,True,False,False,True,False,False,True,False,True,False,False,True,True,False,True,True,True,False,False,False,True,True,True,False,True,True,False,False,True,False,False,False,False,False,True,False,True,False,False,False,False,True,True,False,True,False,True,False,False,True,False,False,True,True,False,False,True,False,True,False,False,True,False,False,True,True,True,False,True,True,True,False,False,False,False,False,True,True,False,True,True,True,True,False,False,True,False,True,False,True,True,False,False,True,True,False,False,False,False,False,True,True,False,False,False,False,False,True,True,False,False,False,True,False,False,False,True,True,True,True,False,True,False,True,False,True,True,True,True,True,True,False,True,True,False,True,True,False,False,False,True,False,True,False,False,True,False,False,False,False,True,True,True,True,False,True,False,True,False,True,False,True,False,True,False,False,False,True,True,False,False,False,True,True,False,True,False,True,True,True,True,True,False,False,False,False,True,True,True,False,False,True,True,False,True,False,True,True,True,False,False,True,False,True,False,False,False,True,True,False,False,False,True,False,False,True,False,False,False,True,False,True,False,True,True,True,True,False,True,True,False,True,False,False,False,True,True,False,False,False,False,False,True,True,False,True,True,False,True,True,True,True,False,True,True,False,True,False,False,False,True,True,True,False,True,True,True,False,True,True,True,False,True,False,True,True,True,False,True,True,False,False,False,False,True,True,False,False,False,True,False,True,False,True,True,True,False,False,False,False,True,True,False,False,True,True,True,False,False,False,True,False,False,False,False,False,True,True,False,True,False,True,True,False,False,False,True,True,True,True,True,False,False,True,True,True,False,False,False,False,True,True,False,True,True,True,True,True,False,False,False,False,True,True,False,True,False,True,False,True,True,True,True,True,False,False,True,True,True,True,True,False,False,False,True,False,True,True,True,True,True,True,True,False,True,True,True,True,False,False,False,True,True,True,True,False,False,False,True,True,True,False,True,True,False,False,True,True,True,False,False,False,False,True,False,True,False,False,False,True,False,False,False,True,True,True,True,True,True,False,False,False,True,True,False,True,False,True,True,True,False,True,False,False,True,False,True,True,False,True,False,False,True,True,False,False,False,True,False,False,False,False,False,True,False,False,False,False,False,True,True,False,True,True,False,False,False,True,True,False,False,False,True,True,True,True,True,True,False,True,True,False,False,False,True,False,False,False,False,False,True,True,False,False,True,False,False,True,True,False,True,True,False,False,False,True,True,False,False,False,True,False,False,True,False,False,True,False,False,True,True,True,True,True,False,False,False,False,True,True,False,False,True,False,True,True,True,False,True,False,False,True,False,True,False,False,True,False,False,True,True,True,False,False,True,False,False,True,True,True,False,True,False,True,False,True,True,True,True,False,True,False,True,True,True,False,True,False,False,False,True,True,True,True,False,False,False,False,True,True,False,False,False,False,True,False,True,False,False,False,True,True,False,False,True,True,False,False,True,False,False,False,False,False,False,False,False,False,False,False,True,False,False,True,False,True,False,True,False,False,False,True,True,False,True,False,False,False,True,True,False,True,False,False,True,False,False,False,False,True,False,True,True,False,False,False,True,False,True,True,False,True,False,False,False,False,False,False,False,True,True,False,True,True,True,False,True,True,False,True,False,False,False,False,False,True,False,False,True,True,True,False,True,False,False,True,False,False,True,False,False,False,False,True,False,True,True,True,True,False,True,True,False,True,True,True,False,True,True,False,True,False,False,False,False,False,True,False,False,False,False,False,False,True,True,False,False,True,False,True,True,True,True,True,False,False,False,True,False,True,True,True,False,True,True,False,True,False,True,True,False,True,False,False,False,True,True,True,False,True,False,True,False,True,True,False,False,True,True,False,True,False,True,True,True,False,True,False,False,False,False,False,False,False,False,False,True,True,True,False,False,False,True,False,True,False,True,True,False,False,True,True,True,False,False,False,False,True,True,False,False,True,False,False,True,True,False,False,False,False,False,True,False,False,True,True,False,False,True,False,True,False,True,False,True,True,False,True,True,True,False,True,False,False,True,True,True,True,False,False,True,False,True,True,False,False,True,True,True,False,True,False,False,True,False,True,False,False,True,True,False,True,False,False,True,True,False,True,True,False,True,False,False,False,False,True,False,True,False,True,True,True,True,True,False,True,True,True,False,False,False,False,True,True,False,False,False,False,True,True,False,False,False,True,False,False,False,True,True,False,False,False,True,False,True,False,True,False,True,True,False,True,True,True,False,False,False,True,False,True,False,True,False,False,False,False,False,False,True,True,False,False,True,True,False,True,True,True,True,False,True,False,False,False,True,False,False,True,True,True,True,False,False,True,False,False,True,True,False,True,False,False,True,False,True,True,True,True,False,False,True,True,False,True,False,False,False,False,True,True,True,False,True,True,True,False,True,True,True,True,False,True,True,True,True,True,False,False,False,False,True,True,False,True,True,False,True,True,False,True,False,False,True,False,True,True,False,True,False,True,False,False,False,False,True,False,True,True,False,True,True,True,False,True,True,True,True,False,False,False,True,True,False,True,True,True,False,True,False,False,False,True,False,False,True,True,False,False,False,True,True,True,False,True,True,True,True,False,False,True,False,True,False,False,False,True,False,False,False,False,False,False,True,False,True,False,True,True,False,True,False,True,True,True,True,False,False,False,False,False,True,True,False,False,True,False,True,True,True,False,False,True,False,True,False,True,False,True,True,False,True,True,False,False,False,True,False,True,True,False,True,False,True,True,False,True,False,False,False,True,False,False,False,False,False,False,False,False,False,True,False,True,False,False,True,True,True,True,False,False,True,True,True,True,True,True,False,True,True,False,False,True,True,False,False,True,True,False,True,True,True,True,False,True,False,True,False,True,False,False,False,True,False,True,False,True,False,False,False,False,True,False,True,False,False,True,True,True,True,False,False,False,True,False,False,True,True,False,True,True,True,True,True,True,False,True,False,False,False,False,False,True,False,False,True,False,True,False,False,True,False,False,True,True,True,True,True,False,False,False,False,True,True,True,False,True,False,False,True,False,False,False,True,False,False,False,False,True,False,False,False,False,True,False,False,False,True,True,False,True,True,False,False,False,True,False,True,False,False,False,False,False,False,False,False,False,False,True,False,True,True,False,True,False,False,True,False,False,False,True,True,True,True,False,True,True,False,False,True,True,True,True,True,True,True,False,False,False,True,False,True,False,False,False,True,True,False,True,True,False,False,False,False,False,False,True,True,True,False,False,False,True,True,True,False,True,True,False,True,False,False,False,True,True,False,False,False,False,True,True,True,False,True,True,False,False,False,True,True,False,True,True,True,False,False,False,True,False,False,False,False,True,False,True,False,True,True,False,True,True,True,False,True,False,True,True,False,False,False,True,False,True,False,False,True,True,False,True,True,False,True,True,True,False,True,True,True,False,True,False,True,False,True,False,True,False,True,True,False,True,True,True,False,True,True,False,False,True,True,True,True,False,True,True,False,False,False,True,False,False,False,False,False,True,False,True,True,False,True,False,True,False,True,False,True,False,False,False,True,True,True,False,True,False,True,False,False,False,True,True,False,True,True,False,False,True,False,False,True,True,False,True,True,True,True,False,True,True,False,False,False,False,False,True,False,False,True,True,False,True,False,False,False,True,False,True,False,False,True,False,True,True,True,False,False,False,True,True,True,True,True,True,True,True,False,False,True,False,True,True,True,True,True,True,False,False,False,False,False,True,False,False,False,True,False,False,True,True,True,False,True,False,True,False,False,False,False,True,False,True,True,True,False,False,False,False,False,True,True,True,False,True,True,True,True,True,True,False,True,True,True,False,True,False,False,True,False,True,True,False,False,False,True,True,False,False,True,True,True,False,False,True,False,True,False,True,False,False,True,True,True,False,True,False,True,False,False,True,True,True,False,True,True,True,False,True,True,False,False,False,False,False,False,False,True,False,True,False,False,True,True,True,True,True,False,False,True,False,False,False,True,False,True,False,True,False,True,True,False,False,True,False,False,True,True,False,False,False,False,False,True,True,False,True,False,False,True,True,False,True,True,True,True,True,True,True,True,False,False,True,False,True,True,True,True,False,True,True,True,True,True,False,False,True,True,True,True,True,False,True,False,False,False,False,True,True,True,False,False,True,True,False,False,False,True,True,True,False,False,False,True,False,False,False,True,False,True,True,True,True,False,True,True,True,True,False,False,False,False,False,True,True,True,False,False,False,True,True,True,False,True,False,False,True,False,True,True,True,False,False,True,True,False,False,False,True,True,False,False,True,True,True,True,False,True,True,False,True,False,True,True,True,False,True,False,False,False,False,False,True,False,True,False,False,True,False,False,False,False,False,False,True,True,True,True,True,False,False,False,False,True,True,True,True,False,True,False,False,True,False,True,False,True,True,False,False,True,False,True,False,False,True,True,False,False,True,True,False,True,True,False,False,False,True,False,False,False,False,False,False,False,False,False,True,True,False,True,True,True,False,True,True,True,False,True,True,True,False,True,False,True,True,True,True,False,True,True,True,True,False,True,True,False,True,False,True,True,True,False,False,False,True,False,True,False,True,True,True,False,False,False,True,False,True,True,False,False,False,True,True,False,False,False,False,True,False,False,True,True,False,True,True,False,True,True,False,True,False,True,True,False,True,False,False,False,True,True,False,False,False,True,False,True,True,True,False,True,True,True,True,True,True,False,True,False,True,True,True,True,True,False,False,False,True,False,True,False,True,True,False,False,True,True,True,False,False,True,False,True,True,True,False,False,True,False,False,True,True,False,False,False,False,False,True], dtype = "bool")#candidate|482|(3072,)|const|bool
bop_483 = relay.right_shift(const_474.astype('int8'), relay.reshape(const_482.astype('int8'), relay.shape_of(const_474))) # shape=(3072,)
func_286_call = mod.get_global_var('func_286')
func_289_call = mutated_mod.get_global_var('func_289')
call_490 = relay.TupleGetItem(func_286_call(relay.reshape(call_473.astype('int32'), [6, 7, 3]), relay.reshape(call_473.astype('int32'), [6, 7, 3]), ), 0)
call_491 = relay.TupleGetItem(func_289_call(relay.reshape(call_473.astype('int32'), [6, 7, 3]), relay.reshape(call_473.astype('int32'), [6, 7, 3]), ), 0)
uop_492 = relay.log(bop_483.astype('float64')) # shape=(3072,)
var_495 = relay.var("var_495", dtype = "float64", shape = (3072,))#candidate|495|(3072,)|var|float64
bop_496 = relay.maximum(uop_492.astype('int64'), relay.reshape(var_495.astype('int64'), relay.shape_of(uop_492))) # shape=(3072,)
output = relay.Tuple([bop_467,call_473,var_475,call_490,bop_496,])
output2 = relay.Tuple([bop_467,call_476,var_475,call_491,bop_496,])
func_500 = relay.Function([var_466,var_475,var_495,], output)
mod['func_500'] = func_500
mod = relay.transform.InferType()(mod)
mutated_mod['func_500'] = func_500
mutated_mod = relay.transform.InferType()(mutated_mod)
func_500_call = mutated_mod.get_global_var('func_500')
var_502 = relay.var("var_502", dtype = "uint64", shape = (4, 9))#candidate|502|(4, 9)|var|uint64
var_503 = relay.var("var_503", dtype = "int32", shape = (126,))#candidate|503|(126,)|var|int32
var_504 = relay.var("var_504", dtype = "float64", shape = (3072,))#candidate|504|(3072,)|var|float64
call_501 = func_500_call(var_502,var_503,var_504,)
output = call_501
func_505 = relay.Function([var_502,var_503,var_504,], output)
mutated_mod['func_505'] = func_505
mutated_mod = relay.transform.InferType()(mutated_mod)
var_697 = relay.var("var_697", dtype = "float64", shape = (15, 4, 10))#candidate|697|(15, 4, 10)|var|float64
uop_698 = relay.sin(var_697.astype('float64')) # shape=(15, 4, 10)
output = relay.Tuple([uop_698,])
output2 = relay.Tuple([uop_698,])
func_703 = relay.Function([var_697,], output)
mod['func_703'] = func_703
mod = relay.transform.InferType()(mod)
var_704 = relay.var("var_704", dtype = "float64", shape = (15, 4, 10))#candidate|704|(15, 4, 10)|var|float64
output = func_703(var_704)
func_705 = relay.Function([var_704], output)
mutated_mod['func_705'] = func_705
mutated_mod = relay.transform.InferType()(mutated_mod)
const_801 = relay.const([[[6,7,10,-5,-5,2,-1,-1,-7,-1,8],[6,-6,-5,9,-10,-6,10,10,-4,4,-2],[4,10,-10,8,3,-3,1,5,-2,6,-1],[-7,-2,9,7,-5,-5,-4,-3,10,-6,-7],[3,-10,-7,4,-5,-3,3,4,-3,1,-3],[-10,7,4,-3,4,-3,10,1,9,8,-2],[2,-1,7,1,-8,8,-1,1,-3,1,-9],[7,-6,5,-6,4,-5,3,6,-3,6,-10],[-4,-2,-5,-5,3,-4,8,-4,-8,-2,-3]],[[6,10,-6,1,-5,8,-1,8,7,8,2],[-3,-10,-5,4,9,9,-9,8,-2,4,8],[-5,3,-10,7,7,-6,-9,-9,-1,2,10],[7,-3,10,-1,5,7,-1,-7,6,-6,-10],[5,7,6,4,-5,3,-1,5,3,9,-8],[-4,-9,-10,5,10,-9,-4,8,-10,-10,-1],[8,-5,8,9,-6,-2,5,8,3,-2,6],[-7,5,-9,2,7,10,1,10,5,-4,1],[-10,-3,-8,5,-10,-10,10,1,-1,-2,-2]],[[8,-4,10,-1,-9,-1,-6,-7,2,-1,-10],[4,-5,-10,6,9,-8,7,10,8,-1,-4],[-5,-7,-6,-3,-1,10,2,2,-5,-1,5],[8,8,-7,-2,-3,9,8,-8,6,8,5],[5,9,8,3,-10,1,7,-4,-6,-10,6],[-4,8,6,-3,9,8,-2,-10,2,-5,7],[-10,3,-9,-2,-10,3,-6,8,-10,1,-7],[-8,5,-8,-4,2,-7,9,7,-2,10,7],[-4,7,-1,6,1,-6,4,9,-8,-2,-8]],[[-10,-4,4,-2,2,-7,2,9,-8,1,-7],[6,5,-8,9,-9,3,-5,-9,-9,3,-10],[-5,-4,-9,7,-2,-3,8,-7,9,8,-9],[-10,-10,-1,-6,9,-10,-4,-7,-7,7,9],[3,-2,10,-8,-5,-1,-9,9,3,-7,-2],[-4,-6,-10,-10,8,-5,-10,2,-7,-6,3],[9,3,3,-7,-4,4,1,-1,-4,-8,9],[5,-6,10,9,9,7,-3,1,5,-10,-5],[4,-2,7,9,-8,7,5,5,-3,5,6]],[[2,8,5,8,-7,-8,-3,10,8,4,-9],[-7,6,-1,-1,9,-6,-1,-4,-1,-1,1],[3,-4,7,-8,-1,-3,4,8,-10,-9,3],[-7,8,8,-6,-3,-10,2,7,8,-5,-4],[4,6,-10,-10,4,-10,7,2,-10,-4,4],[-10,6,-10,10,1,8,9,2,-1,-9,9],[-10,9,5,-2,9,-1,-1,-7,-5,-4,6],[10,-3,2,-1,-7,-1,-3,-10,-7,-7,6],[-9,9,-9,-6,-6,-3,-7,-2,8,-1,6]],[[7,-7,6,3,1,3,6,3,-9,10,10],[8,8,-9,-5,3,10,-6,-3,8,-1,-6],[-5,10,-7,-5,-8,9,1,4,-5,-9,4],[-3,6,-5,-4,-5,9,2,-6,5,2,-1],[-5,8,-10,7,4,-5,3,9,-8,-6,-2],[2,-7,-3,2,1,-6,9,8,2,-6,-4],[6,6,-10,10,1,9,1,-7,5,-2,9],[-9,-7,-10,-9,-2,8,8,10,-9,9,9],[1,5,-3,8,-10,10,-9,8,5,-2,8]],[[10,-5,-1,8,-6,-5,4,2,2,1,7],[2,-10,7,-1,-2,-5,1,-5,5,7,-4],[9,-5,8,-5,-7,-10,6,-1,-2,-10,-1],[-4,-10,-8,10,10,-10,2,-10,-2,-4,6],[-10,6,9,1,-9,-6,6,7,-8,5,1],[-7,-4,10,9,-7,10,-3,1,8,-10,2],[10,10,-8,7,4,-2,3,4,5,-3,7],[5,9,-10,8,3,-3,6,-9,1,-7,10],[3,3,7,5,9,4,3,-7,7,-7,-4]],[[-10,-7,6,3,5,-2,-4,-2,5,-8,1],[2,-2,-7,-9,-3,-6,9,-6,10,8,10],[2,-4,-5,-3,-6,4,4,-7,6,4,-2],[-4,7,2,5,-9,5,-4,-6,9,-2,9],[8,-10,8,6,9,10,5,1,-5,-7,-6],[3,7,-3,8,-6,-10,3,-2,-9,1,9],[1,-6,-2,9,5,7,7,-1,-4,3,7],[3,7,2,-3,-5,-9,-3,5,9,5,4],[-8,6,3,-9,7,10,5,-3,-1,5,1]],[[-4,-1,8,9,-5,-8,10,-10,2,10,-3],[-3,5,9,7,9,6,-2,-3,8,-7,-1],[-8,3,-10,1,10,-4,-10,-5,2,-6,-4],[-5,-9,-9,9,-3,-10,-6,-1,-8,1,-8],[-4,5,8,4,-2,-1,6,-1,-9,-4,3],[3,-7,7,-4,6,-9,-4,6,9,1,-1],[3,1,-6,-2,5,3,8,-9,-6,-10,7],[1,6,-1,1,3,6,5,9,1,5,-7],[5,-5,2,-5,1,-4,6,-3,9,-3,10]],[[-9,7,4,-5,7,6,4,-9,-6,-4,7],[-8,-1,6,4,-3,-4,4,-2,-6,2,3],[7,4,2,6,10,-2,10,4,-2,8,7],[2,2,10,-10,-9,-5,-4,3,-8,1,3],[-6,7,5,-5,-5,4,7,-1,-9,5,3],[10,-9,-8,-8,4,-1,-5,-6,9,-7,1],[8,-2,2,2,-9,1,3,-8,2,7,5],[-10,-2,2,-5,-5,5,-2,7,4,6,-3],[7,-10,-3,4,8,-9,-4,-2,-4,-4,8]]], dtype = "int8")#candidate|801|(10, 9, 11)|const|int8
var_802 = relay.var("var_802", dtype = "int8", shape = (10, 9, 11))#candidate|802|(10, 9, 11)|var|int8
bop_803 = relay.minimum(const_801.astype('int8'), relay.reshape(var_802.astype('int8'), relay.shape_of(const_801))) # shape=(10, 9, 11)
uop_812 = relay.sinh(bop_803.astype('float32')) # shape=(10, 9, 11)
bop_816 = relay.not_equal(uop_812.astype('bool'), relay.reshape(bop_803.astype('bool'), relay.shape_of(uop_812))) # shape=(10, 9, 11)
output = relay.Tuple([bop_816,])
output2 = relay.Tuple([bop_816,])
func_821 = relay.Function([var_802,], output)
mod['func_821'] = func_821
mod = relay.transform.InferType()(mod)
mutated_mod['func_821'] = func_821
mutated_mod = relay.transform.InferType()(mutated_mod)
var_822 = relay.var("var_822", dtype = "int8", shape = (10, 9, 11))#candidate|822|(10, 9, 11)|var|int8
func_821_call = mutated_mod.get_global_var('func_821')
call_823 = func_821_call(var_822)
output = call_823
func_824 = relay.Function([var_822], output)
mutated_mod['func_824'] = func_824
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1059 = relay.const([[[-1.167697,-9.701190,-4.779158,4.134154,-7.837395,3.949706,6.345305,6.678657,-5.840091,-1.799992,1.978292,1.631961,5.610171],[8.864764,-9.582750,-5.588514,-2.257847,7.222680,3.918615,-2.692409,5.399437,-9.924036,5.393478,0.629489,-8.703160,1.502929],[-3.930638,8.915710,-5.190264,-5.074670,-5.000568,3.988562,-8.274811,9.250617,0.024328,1.881767,4.758210,4.372226,3.646171],[-0.917405,0.931596,4.181421,6.301213,6.181978,0.622987,-3.217595,-5.402421,-7.364785,-5.423506,-1.012271,8.422015,1.430625],[5.856142,2.835234,0.668055,-7.097294,5.416094,5.637275,1.254724,-5.541884,-1.393340,-1.339069,4.241945,6.620993,-7.075531],[5.976886,2.830559,-3.473889,-8.949252,-2.229656,-7.126439,-3.599642,-6.122177,-2.661593,-0.246173,6.454730,7.628886,1.664467],[-1.137752,-8.615626,-7.885382,8.650450,-8.526802,-9.546097,2.081434,7.766303,-3.764469,-7.982393,7.420387,-7.921588,4.378283],[-0.426845,1.532470,4.499446,5.396927,-7.482541,-4.340772,0.385263,7.280658,3.018922,-8.077130,-6.878073,-0.672142,-6.533579],[0.010738,0.514306,-8.034954,5.782477,4.718231,7.489123,5.688806,-7.104119,6.250819,-6.574989,8.894688,-9.594278,-4.206243],[-0.670918,2.411802,-4.220231,7.239263,2.823018,-7.682981,6.887165,-9.460913,-4.224748,-7.130451,4.266596,-7.080800,5.933606],[0.070860,-7.097829,-2.242296,-8.090844,4.243868,8.895810,-5.187099,-8.979874,7.873789,-1.871782,-0.093711,6.971128,9.223597],[1.636471,5.798238,1.594836,-5.289216,-1.720488,5.918212,-6.713865,-2.595784,3.521480,-2.194269,5.790118,-7.089434,5.225360],[-7.022285,0.645272,4.416831,8.093650,0.451912,9.907726,-1.729692,8.848084,-4.886398,-0.370622,9.868540,7.836312,4.314369],[6.061699,-3.987829,4.663276,-9.939464,-3.612046,0.829126,-4.877767,1.775425,-8.113682,5.758496,0.775199,3.301792,-7.385052]],[[8.519088,-9.857256,-6.726136,-0.276791,1.201277,1.100607,3.901985,7.265941,-0.720344,1.084943,-0.071963,2.714271,1.875910],[4.076262,0.198762,4.272974,-0.919853,5.974847,-0.467183,6.980773,8.539796,2.332981,5.551589,2.014690,-6.010117,0.770636],[-9.535392,-5.866675,7.080021,-6.841583,-2.602697,6.181668,-8.958641,0.188899,7.578200,-8.230431,-4.696825,2.045339,-2.400526],[7.210301,7.184954,9.638242,4.465938,-2.705431,-0.453067,0.284096,-3.704004,1.371162,-9.940242,4.080719,4.910072,-5.491981],[3.481892,0.665958,5.966994,-0.543638,5.223834,-5.198081,-8.954715,2.574166,-1.367039,4.954547,-9.700013,7.052029,4.990739],[-8.053988,-9.592922,-4.887370,-7.739183,6.640422,-0.397855,-6.132050,-8.626815,6.536213,9.047888,0.622475,3.784166,4.575817],[2.117845,-2.761054,0.923736,4.922965,-9.965080,-9.743283,-4.487480,-8.067732,7.722944,-3.909498,4.334015,-5.165000,8.216426],[-5.769452,-6.746774,-8.523525,-2.778644,9.011279,7.892347,1.194183,-4.994123,-7.435897,-1.354683,-4.771082,6.961197,6.987362],[-9.163624,-8.671934,7.317381,-7.509613,-0.437670,8.399463,-2.458217,-7.373468,7.424163,1.088422,6.545384,-1.607392,-1.027624],[-7.707065,-3.761234,-6.429743,3.688831,-8.294087,-7.652188,4.449720,3.463634,7.259912,6.328377,0.214183,-8.069121,-0.421289],[-9.364639,3.204836,0.049090,-6.730177,0.486994,-0.534791,7.235316,2.869650,-3.346160,-1.826685,4.133530,6.844043,-4.185189],[1.776054,7.399771,-7.106419,6.296520,-0.835204,1.579732,-1.082566,1.018261,-0.660796,3.295024,-5.034970,-9.995303,4.318273],[8.029012,-3.458772,2.471891,-3.983130,1.697442,-7.769433,-9.616229,-0.540428,8.965121,-6.812299,9.275937,-3.617563,-3.087147],[-0.492858,2.819104,-0.341297,-2.850905,-9.696490,-7.193813,-8.502694,-8.317659,-9.200998,4.323750,-3.060722,9.794589,-2.411223]],[[5.660787,5.288991,6.350901,-7.643515,8.150001,9.060651,8.790109,4.808622,-0.948054,-7.498736,-3.814300,3.966560,3.637931],[7.880332,-0.175446,4.578556,-6.794456,5.095852,0.906571,-9.728965,-0.581208,-6.910278,-0.364726,-4.143275,-3.293266,6.933515],[3.299908,-4.762202,-7.528177,-1.221287,5.951831,1.806299,-6.265577,-3.538057,-1.968582,2.847373,-7.564063,3.202876,4.478888],[-9.697282,-6.988267,2.813757,-8.190907,-7.275513,5.410953,-5.222350,-6.438903,-7.984602,-2.966777,-5.383609,3.798118,-0.799027],[-4.976147,-7.449580,6.435229,2.579039,-0.595338,6.977136,-8.571482,-5.079991,-5.972369,4.751554,-9.139892,-6.378934,-7.043220],[6.532529,-1.988128,6.895989,8.585596,-3.606738,-8.041924,-3.557723,-8.969352,-6.486376,7.894545,-9.317527,5.648837,3.070762],[7.180942,-7.452256,-1.201813,-9.142768,2.576373,9.797600,7.912752,9.935830,4.227550,7.593221,-6.174256,3.529076,-0.664868],[4.305647,0.517660,8.500516,-2.884657,-8.817846,2.084466,8.423452,-1.476421,-9.694925,9.436404,-1.904444,5.589506,-5.982024],[7.773926,-4.785651,-0.223958,8.724064,-2.617840,-5.589333,-9.655249,6.635950,6.103668,6.018725,-8.581910,-4.236356,2.528604],[-9.679206,-3.846609,-5.803490,-2.482079,7.204898,8.037662,-0.653508,8.550806,-4.973345,0.274671,3.486331,7.744161,5.012431],[-3.198769,2.918012,-5.167379,5.766622,-9.723624,-6.884371,-7.102713,5.247576,-2.571574,9.335394,7.987124,5.092596,7.074331],[9.157677,9.793084,-2.629274,-8.477000,-7.196160,-0.445861,4.869777,2.102874,8.809525,9.612164,9.420929,9.098072,9.001022],[6.162185,2.134385,-7.851275,9.969043,7.680660,8.825479,8.975510,-0.080826,0.968825,-7.601760,5.108685,-8.388880,9.900940],[-1.101153,-3.903540,8.863508,4.895656,2.149522,1.421270,4.161940,-4.957930,1.423693,-1.445167,0.284718,4.962285,0.871284]],[[-8.166600,-9.120320,9.947386,-1.635353,-7.573123,7.806246,-0.060362,9.927692,0.193337,0.722531,-7.684712,6.789909,-6.555568],[-7.344617,4.822266,6.378983,-8.100535,9.653926,-1.329250,1.803964,8.399178,-9.963988,1.450087,8.723732,6.323054,7.191121],[4.524097,-5.885384,5.602814,-3.997522,-1.557672,-4.465241,5.950250,7.707904,0.435893,-1.021046,5.776248,2.895881,0.706070],[-2.129755,9.839510,-3.146107,-9.224521,-1.007743,9.807321,-9.112511,-5.102934,-7.729271,-5.446554,-5.411068,7.340742,-0.791960],[1.377051,9.692179,6.462046,8.302224,3.610971,9.363050,8.842905,-3.287157,-0.766054,-5.063583,8.677538,-5.910578,-6.424394],[-2.532304,-5.942336,0.292294,-5.804110,-8.623119,-7.101728,-6.150571,1.418472,8.235232,0.641073,7.546907,8.709725,3.317231],[6.090081,-1.593336,-2.145251,0.582836,-3.017018,-5.229042,1.591194,-7.627431,8.074739,-4.014711,-4.704665,6.065323,1.667327],[-6.576617,-1.112270,2.124500,9.154743,-8.833696,-4.459249,-8.200995,-5.098502,1.522416,1.106409,4.157846,-1.472696,1.052102],[9.389976,7.115154,-8.792056,4.357742,9.679660,-1.358200,2.103690,-8.361359,-9.250370,-3.852853,4.493493,-9.259843,2.953150],[9.348185,6.193258,-4.872044,0.058652,9.213527,9.322155,0.113320,-2.241815,-8.187000,-1.625460,6.206807,8.003449,6.947746],[-1.143929,-4.776067,3.356732,8.690170,-0.880862,0.530085,5.516353,4.798666,-5.350018,9.791750,-1.831392,-4.422264,-1.301944],[3.019217,4.884536,9.768159,4.543688,1.761051,9.779790,1.928724,-1.664181,-7.890250,-1.515217,9.527994,-7.062538,1.921317],[-6.112545,2.220998,1.461269,-1.701031,5.639614,-0.787760,1.847629,3.633645,1.183586,2.143666,4.886959,0.868820,6.230893],[-5.478585,-9.802661,4.995351,0.056526,4.802254,4.929538,8.165238,6.952566,0.260903,9.521706,-7.815011,-3.284643,0.475791]],[[4.500909,6.438754,9.471954,-5.676673,0.702711,-0.937743,-1.466718,1.616230,7.198755,-7.382486,1.712748,-1.415056,-0.315708],[4.910084,-0.565272,-0.386995,9.694548,-6.524050,-9.695004,-4.596247,-2.887853,-6.927835,1.119177,3.306003,9.342788,7.456997],[1.827310,4.322133,-6.450655,-8.679221,5.449516,-6.738401,-9.199651,9.826108,9.956754,-0.850024,-8.282762,-7.948521,2.669207],[0.652194,7.560340,1.415826,-7.975661,-3.669067,1.261154,0.654026,-0.784589,2.317691,-2.087781,8.284993,6.382585,-7.151385],[-3.203739,0.796061,-7.365188,-7.041575,0.579927,-9.827737,0.859214,0.314657,-6.544687,0.894551,-3.702620,6.747255,-4.722083],[3.707873,6.544879,5.510508,-8.298959,7.125892,8.905346,5.897350,0.990642,-5.121757,-0.136298,3.580877,-1.298852,1.015420],[8.953994,-9.585044,8.534553,6.570891,5.751360,0.907207,8.370301,-7.768143,-0.722867,-6.594722,4.888700,-7.086475,-0.145828],[-6.802643,6.065236,9.418587,0.701782,-9.592996,9.615304,0.268849,-1.985896,5.669825,3.133314,1.708288,4.945987,1.473462],[-9.286739,-2.855972,0.755284,-8.889641,0.722791,3.278318,5.084530,0.441052,-5.353613,2.600271,5.158069,-0.662476,-8.540667],[1.368177,2.756720,-8.700946,-5.467051,-0.746321,-2.847311,-7.533259,7.835008,-9.374970,9.379056,4.727655,-2.566869,4.042862],[6.069434,-7.545790,2.789042,6.055307,-2.893571,-7.863039,7.998246,-5.845145,9.566940,9.510461,-9.786873,0.610675,3.376434],[1.336946,3.406603,-0.469790,0.958112,-9.061641,-7.402204,1.246505,-7.448569,7.830991,6.977735,3.308162,1.501861,4.621119],[-7.660381,5.384793,9.717578,9.847714,0.692159,-2.189775,-3.334980,0.782581,-0.317916,4.378978,1.149390,-3.554899,-8.930973],[2.365141,-1.747515,1.543454,-6.032551,4.051807,-1.271554,-8.137674,-4.465640,-0.741249,-4.717913,8.347917,-2.581098,9.459267]],[[2.425965,-0.555313,5.234968,8.724880,-2.236087,-0.762217,-2.305745,6.826336,-2.420558,-5.712281,-7.623641,6.721912,1.389478],[8.240347,8.996186,8.732640,4.392933,-3.381716,7.152551,-4.398658,-6.414721,-0.105210,-3.621411,6.580999,-2.143148,9.618344],[-2.416496,6.024488,8.157527,-2.156078,5.904480,-0.555866,5.814586,1.956997,-9.528873,9.788750,-9.718806,4.781329,7.527705],[0.786967,6.885934,-0.343045,6.990826,4.295770,-6.070194,7.277109,1.294025,-8.214959,-5.861891,4.899420,-7.061070,1.250531],[2.821469,3.624873,-8.638893,-3.895985,-5.547598,2.114162,-7.337432,-3.614486,-9.969197,-2.346805,4.420276,2.438156,-4.269223],[5.507748,3.229206,8.806559,1.947060,7.967868,3.866966,4.710520,-7.615504,0.852818,5.184145,5.256751,0.335176,6.080710],[6.911901,-0.225438,-8.364663,-5.175370,-1.689061,-2.354119,-3.036052,7.756420,6.198010,9.000569,-1.822888,-2.949379,5.929076],[0.956386,4.816329,3.411436,9.886114,-5.463994,0.483528,0.260324,-5.982651,-4.037730,7.756213,-6.060897,-8.085052,-6.783904],[-2.765334,8.442312,7.872611,-8.640513,3.648483,3.055375,4.720515,-3.204672,-4.730965,-7.604757,8.742508,6.264197,2.775063],[9.767145,-1.268041,-8.345467,-5.047536,-2.409924,-4.130765,-3.563182,-0.278746,0.564183,8.438473,3.624017,2.591664,-2.464079],[-2.513266,-9.727352,0.136966,8.013710,2.458455,-1.614980,6.104978,5.226571,2.870066,-9.886498,0.457054,1.157904,2.000038],[-8.677184,7.736656,-2.174507,3.611388,9.520522,-5.570087,-6.149964,-9.069624,-1.553638,1.267354,0.148403,8.064798,-2.858729],[0.917480,-8.778460,-7.285064,-2.634213,4.057664,4.002277,4.981256,-5.144499,-0.458065,5.147523,5.316334,-4.969395,-4.437479],[-1.335944,3.815799,-3.012196,-9.704670,-8.706163,-2.862917,-5.621069,5.144581,-5.491485,-5.918395,-0.860202,7.826244,1.811482]],[[2.960491,3.441908,-2.992074,-1.253673,-4.173651,-5.014914,7.054167,-0.432921,6.930608,5.986233,-5.930618,8.432331,-9.465222],[3.967345,-2.961166,2.965191,2.886156,5.795991,-8.281440,5.176564,-8.698151,6.627463,-0.244256,7.208098,5.571723,-6.791330],[-4.133898,-6.182093,-9.285761,-6.330512,0.014124,-5.116462,-4.457668,-7.709465,4.186845,-2.065094,4.065481,8.489464,9.215499],[-1.342544,-2.269828,-3.247125,-8.988205,5.458757,1.963187,3.013462,5.669840,3.433912,4.281839,-2.500441,7.866232,4.076129],[9.909764,4.752654,9.981455,0.984342,-7.197373,7.600585,-5.533432,1.414117,-9.556362,-0.147997,2.190151,-9.452016,0.119452],[2.691197,8.647589,-5.056813,-5.388954,7.186155,4.819621,0.993755,-5.384912,-4.914486,0.356959,-8.043028,2.651013,-9.137610],[-3.469317,4.541201,2.987692,0.477745,5.439296,3.991589,1.070696,-0.657657,3.302452,-8.654293,-4.697974,2.754614,5.485619],[2.919662,-8.852259,1.856733,-0.355837,4.555142,8.761108,-4.356798,-5.296898,-9.625593,-0.010099,-6.155022,-8.721742,-5.431851],[1.777386,4.314575,4.203011,3.680392,-4.311826,4.277130,-1.614132,-7.718963,3.371247,-7.853923,9.474950,6.664497,2.698643],[6.717279,-4.851708,-9.606066,2.713828,-2.098456,7.814611,8.987836,-6.624560,-5.918837,3.476635,9.541544,-4.428925,-7.576242],[-2.628359,6.409123,9.098036,-7.654690,-3.633618,6.959973,-5.983443,6.297783,-3.107479,4.400494,8.899910,7.069033,-3.306826],[8.833406,-7.398994,-0.515896,3.883276,2.178041,6.474835,-3.458254,-5.705856,2.529489,-8.285791,-3.431350,4.498517,2.632086],[-8.790714,0.019393,9.287288,1.379874,-9.874754,8.542007,7.782264,-7.498315,-2.844894,2.570002,6.514859,9.592532,2.412794],[-6.352396,2.295558,3.496681,-9.898945,-7.017808,7.768197,8.172664,-4.297453,7.696628,7.969097,-7.364951,-3.785044,1.636692]],[[-1.799543,3.762911,-6.456122,2.956388,-7.502322,6.711858,1.243213,-2.077518,0.411550,0.482207,-5.156680,-3.365933,-7.490293],[0.929116,-4.276113,-9.302141,4.040199,-8.977481,9.417957,3.328609,-0.332412,-1.995672,4.821987,-3.412157,5.877613,-5.281398],[-8.166327,6.535692,9.901220,8.127868,4.595133,-0.538594,-8.291893,9.979864,-2.422721,0.345262,2.513387,8.316357,-7.494352],[-2.904844,2.456351,-0.397528,2.151638,-8.099664,-7.993205,-8.263772,-4.420809,3.176767,5.914276,-4.181604,1.385438,-2.490077],[-9.125018,5.224301,8.579111,-5.148547,-0.069628,-6.593358,-1.650245,-7.049156,-7.337168,7.310728,-6.999021,6.348219,7.488939],[2.268427,0.588134,0.161064,1.647900,3.657840,-5.281679,4.488886,-9.424995,-4.819834,2.381436,4.856914,4.313579,-1.834804],[0.612378,9.186254,3.555700,-9.092076,-8.954531,-9.926151,-4.378960,-1.242280,6.483744,-0.891913,7.928251,0.996273,7.063066],[0.407066,8.323745,-6.102654,9.877591,9.615937,7.729751,-7.698904,3.955642,3.395926,-0.019234,7.617896,-9.088801,1.059377],[-2.033952,-5.511219,0.269431,6.673110,5.754702,-4.150642,3.952420,5.651351,8.108709,5.159937,7.690471,-1.270805,-4.606880],[5.315965,0.265884,6.496390,1.882456,-0.226255,1.312623,9.084202,7.794674,7.767047,2.905187,0.183641,-5.114337,-4.470376],[-6.888027,9.420150,-6.696107,1.579203,5.686014,4.576769,-3.221343,-8.993121,6.598633,-9.584584,7.259514,-7.304132,-0.324174],[1.415107,-7.473470,-4.058605,-9.674539,0.557722,0.131110,2.668336,0.735379,2.640942,-1.682039,8.148477,-4.404211,-9.134188],[-2.478095,-2.450127,9.192255,7.586729,3.461263,-7.227381,-9.821757,-0.979809,-6.278156,-0.584248,0.663123,6.936187,5.013544],[4.454008,-7.593316,2.843672,-9.247314,5.014018,6.838447,2.290001,3.212268,4.423896,-5.756551,7.639676,1.633082,-2.199290]],[[8.552164,-4.390741,8.168014,-4.500374,5.642722,-0.566848,-5.037716,0.303837,-2.315797,-8.313530,-6.145124,9.819570,-2.037093],[3.282357,9.205496,-4.738919,6.002002,9.035700,-8.090808,-8.432123,-2.044683,-3.456527,9.766763,-9.623305,-9.670029,3.581049],[-8.600903,0.967276,6.497368,-1.227522,9.735498,0.041585,3.802928,8.440780,4.109287,-0.592252,-6.413696,-1.553797,-5.693294],[0.147616,7.130365,-4.862932,-0.704673,-6.315439,-6.570318,-7.383319,2.450681,4.772879,-8.385366,7.248108,-4.741569,3.368925],[-6.740722,-6.338013,6.333190,5.865292,-2.171516,-8.748759,-9.990873,-7.133992,-1.554789,-1.794112,8.540128,-1.181107,-6.271286],[4.285843,4.376329,5.327899,-5.863956,2.825491,2.522867,-7.964879,-0.494182,-2.456843,-3.270799,9.887466,2.511865,-2.136840],[7.120333,9.590078,-2.687901,0.301478,0.919307,3.057756,-6.578455,3.239250,-1.713479,-0.384704,1.360239,1.535485,1.980736],[-6.526064,-3.972247,2.023558,0.375951,5.459374,1.834332,-8.442397,2.458661,-3.526421,-0.508503,1.474161,-6.049261,4.014002],[0.858032,2.877850,5.309973,1.231594,-1.579671,-5.302400,5.527075,-6.173521,-0.497223,-1.039188,-7.131429,0.302142,-6.380701],[5.974004,-4.291339,-2.141813,8.108188,0.821690,0.787914,-5.331143,4.197585,-4.581811,-2.876148,-7.949247,4.408201,-6.959866],[3.571083,-7.719005,7.034519,-8.921274,-9.153243,6.744459,-8.444975,-8.089187,2.377398,-3.812824,5.719231,-6.031334,6.555020],[-5.894463,6.938285,-2.046010,1.005056,-1.645773,6.247454,-5.776929,-2.980947,8.022649,-5.116242,-4.444225,1.381146,6.522758],[2.601465,-8.934383,-6.218724,4.081121,-2.429903,-9.829945,-5.337482,-3.139288,-0.477839,5.125923,-0.859373,3.423987,8.324574],[-6.655601,-7.286200,3.865560,2.422535,-8.919737,0.565895,1.222247,-9.200039,0.758632,0.973093,-7.406020,-8.212114,-2.043355]],[[-5.609121,-4.451737,8.579700,-0.418072,-7.390118,-6.000073,-5.749150,4.506602,-5.962148,9.865353,-0.478085,-3.598898,-7.208312],[8.280515,-3.692723,7.978985,-5.531022,-8.671905,-5.431103,2.156582,2.253599,9.799825,2.533779,7.205491,6.414598,-8.949211],[8.241024,7.961859,6.424095,-3.396459,-7.620490,-6.581378,2.161591,2.309390,-2.651971,-6.494060,-3.450495,7.942001,-8.684051],[1.651263,7.236540,-9.033667,-7.002483,-8.206471,-8.803467,-7.837426,-8.316936,8.954067,1.411368,8.255817,-6.851874,7.222985],[5.892154,-0.570166,6.233109,-2.847135,4.394980,7.351143,-4.986785,6.516759,7.640837,-7.338515,-5.545246,6.296252,-1.464049],[4.562523,8.821481,5.265437,0.940645,-2.951414,7.370571,1.227868,9.900617,4.661650,-0.610048,3.091388,-8.333264,3.576225],[0.526215,-8.827293,-2.519220,-0.363687,5.618925,-3.165007,6.861473,0.211628,3.324725,4.977825,-6.441770,8.698578,4.145822],[-0.182697,-8.788582,1.391121,-8.725187,1.748108,5.168751,-5.643226,6.503915,-9.650259,-5.765125,1.469169,-8.123560,-0.972681],[1.528344,-8.858367,-6.478077,-0.096102,-1.343041,4.983899,-3.280160,6.844906,-1.351409,-1.636480,5.286526,6.259779,-6.317764],[8.803254,1.217368,0.234831,2.924228,-0.298979,-0.900876,-3.762991,-6.055478,-6.793707,-5.372152,-2.705585,6.297283,-9.770682],[3.313830,-5.197833,5.951198,8.828322,-0.373071,8.319027,-6.739679,4.669697,0.714256,7.338770,3.798720,-1.146218,-9.637872],[3.274451,0.228932,-7.604797,6.700461,-3.318452,-5.076113,2.540802,9.994876,3.531588,-2.184918,-1.998468,-7.696172,3.050941],[4.372464,-9.272876,8.166245,-9.695103,0.922288,3.619524,9.950184,1.597966,6.723650,-9.303580,-2.703021,-9.321738,0.084803],[-2.099318,2.199786,2.102736,3.851320,-8.778606,3.315408,8.186825,9.348444,2.967192,-9.345616,-5.546873,-1.159196,-5.566930]]], dtype = "float64")#candidate|1059|(10, 14, 13)|const|float64
uop_1060 = relay.tan(const_1059.astype('float64')) # shape=(10, 14, 13)
output = relay.Tuple([uop_1060,])
output2 = relay.Tuple([uop_1060,])
func_1066 = relay.Function([], output)
mod['func_1066'] = func_1066
mod = relay.transform.InferType()(mod)
mutated_mod['func_1066'] = func_1066
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1066_call = mutated_mod.get_global_var('func_1066')
call_1067 = func_1066_call()
output = call_1067
func_1068 = relay.Function([], output)
mutated_mod['func_1068'] = func_1068
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1066_call = mod.get_global_var('func_1066')
func_1068_call = mutated_mod.get_global_var('func_1068')
call_1117 = relay.TupleGetItem(func_1066_call(), 0)
call_1118 = relay.TupleGetItem(func_1068_call(), 0)
output = relay.Tuple([call_1117,])
output2 = relay.Tuple([call_1118,])
func_1120 = relay.Function([], output)
mod['func_1120'] = func_1120
mod = relay.transform.InferType()(mod)
mutated_mod['func_1120'] = func_1120
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1120_call = mutated_mod.get_global_var('func_1120')
call_1121 = func_1120_call()
output = call_1121
func_1122 = relay.Function([], output)
mutated_mod['func_1122'] = func_1122
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1066_call = mod.get_global_var('func_1066')
func_1068_call = mutated_mod.get_global_var('func_1068')
call_1175 = relay.TupleGetItem(func_1066_call(), 0)
call_1176 = relay.TupleGetItem(func_1068_call(), 0)
output = call_1175
output2 = call_1176
func_1188 = relay.Function([], output)
mod['func_1188'] = func_1188
mod = relay.transform.InferType()(mod)
mutated_mod['func_1188'] = func_1188
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1188_call = mutated_mod.get_global_var('func_1188')
call_1189 = func_1188_call()
output = call_1189
func_1190 = relay.Function([], output)
mutated_mod['func_1190'] = func_1190
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1188_call = mod.get_global_var('func_1188')
func_1190_call = mutated_mod.get_global_var('func_1190')
call_1210 = func_1188_call()
call_1211 = func_1188_call()
output = relay.Tuple([call_1210,])
output2 = relay.Tuple([call_1211,])
func_1216 = relay.Function([], output)
mod['func_1216'] = func_1216
mod = relay.transform.InferType()(mod)
output = func_1216()
func_1217 = relay.Function([], output)
mutated_mod['func_1217'] = func_1217
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1216_call = mod.get_global_var('func_1216')
func_1217_call = mutated_mod.get_global_var('func_1217')
call_1233 = relay.TupleGetItem(func_1216_call(), 0)
call_1234 = relay.TupleGetItem(func_1217_call(), 0)
var_1235 = relay.var("var_1235", dtype = "float64", shape = (10, 14, 13))#candidate|1235|(10, 14, 13)|var|float64
bop_1236 = relay.floor_mod(call_1233.astype('float64'), relay.reshape(var_1235.astype('float64'), relay.shape_of(call_1233))) # shape=(10, 14, 13)
bop_1239 = relay.floor_mod(call_1234.astype('float64'), relay.reshape(var_1235.astype('float64'), relay.shape_of(call_1234))) # shape=(10, 14, 13)
output = relay.Tuple([bop_1236,])
output2 = relay.Tuple([bop_1239,])
func_1241 = relay.Function([var_1235,], output)
mod['func_1241'] = func_1241
mod = relay.transform.InferType()(mod)
var_1242 = relay.var("var_1242", dtype = "float64", shape = (10, 14, 13))#candidate|1242|(10, 14, 13)|var|float64
output = func_1241(var_1242)
func_1243 = relay.Function([var_1242], output)
mutated_mod['func_1243'] = func_1243
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1066_call = mod.get_global_var('func_1066')
func_1068_call = mutated_mod.get_global_var('func_1068')
call_1298 = relay.TupleGetItem(func_1066_call(), 0)
call_1299 = relay.TupleGetItem(func_1068_call(), 0)
output = relay.Tuple([call_1298,])
output2 = relay.Tuple([call_1299,])
func_1300 = relay.Function([], output)
mod['func_1300'] = func_1300
mod = relay.transform.InferType()(mod)
mutated_mod['func_1300'] = func_1300
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1300_call = mutated_mod.get_global_var('func_1300')
call_1301 = func_1300_call()
output = call_1301
func_1302 = relay.Function([], output)
mutated_mod['func_1302'] = func_1302
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1120_call = mod.get_global_var('func_1120')
func_1122_call = mutated_mod.get_global_var('func_1122')
call_1331 = relay.TupleGetItem(func_1120_call(), 0)
call_1332 = relay.TupleGetItem(func_1122_call(), 0)
uop_1345 = relay.log(call_1331.astype('float64')) # shape=(10, 14, 13)
uop_1347 = relay.log(call_1332.astype('float64')) # shape=(10, 14, 13)
uop_1349 = relay.asinh(uop_1345.astype('float64')) # shape=(10, 14, 13)
uop_1351 = relay.asinh(uop_1347.astype('float64')) # shape=(10, 14, 13)
func_703_call = mod.get_global_var('func_703')
func_705_call = mutated_mod.get_global_var('func_705')
var_1353 = relay.var("var_1353", dtype = "float64", shape = (600,))#candidate|1353|(600,)|var|float64
call_1352 = relay.TupleGetItem(func_703_call(relay.reshape(var_1353.astype('float64'), [15, 4, 10])), 0)
call_1354 = relay.TupleGetItem(func_705_call(relay.reshape(var_1353.astype('float64'), [15, 4, 10])), 0)
var_1359 = relay.var("var_1359", dtype = "float64", shape = (10, 14, 13))#candidate|1359|(10, 14, 13)|var|float64
bop_1360 = relay.power(uop_1349.astype('float32'), relay.reshape(var_1359.astype('float32'), relay.shape_of(uop_1349))) # shape=(10, 14, 13)
bop_1363 = relay.power(uop_1351.astype('float32'), relay.reshape(var_1359.astype('float32'), relay.shape_of(uop_1351))) # shape=(10, 14, 13)
bop_1372 = relay.right_shift(var_1359.astype('uint32'), relay.reshape(bop_1360.astype('uint32'), relay.shape_of(var_1359))) # shape=(10, 14, 13)
bop_1375 = relay.right_shift(var_1359.astype('uint32'), relay.reshape(bop_1363.astype('uint32'), relay.shape_of(var_1359))) # shape=(10, 14, 13)
var_1389 = relay.var("var_1389", dtype = "float64", shape = (10, 14, 13))#candidate|1389|(10, 14, 13)|var|float64
bop_1390 = relay.logical_or(uop_1349.astype('bool'), relay.reshape(var_1389.astype('bool'), relay.shape_of(uop_1349))) # shape=(10, 14, 13)
bop_1393 = relay.logical_or(uop_1351.astype('bool'), relay.reshape(var_1389.astype('bool'), relay.shape_of(uop_1351))) # shape=(10, 14, 13)
func_703_call = mod.get_global_var('func_703')
func_705_call = mutated_mod.get_global_var('func_705')
call_1394 = relay.TupleGetItem(func_703_call(relay.reshape(call_1352.astype('float64'), [15, 4, 10])), 0)
call_1395 = relay.TupleGetItem(func_705_call(relay.reshape(call_1352.astype('float64'), [15, 4, 10])), 0)
output = relay.Tuple([call_1352,var_1353,bop_1372,bop_1390,call_1394,])
output2 = relay.Tuple([call_1354,var_1353,bop_1375,bop_1393,call_1395,])
func_1396 = relay.Function([var_1353,var_1359,var_1389,], output)
mod['func_1396'] = func_1396
mod = relay.transform.InferType()(mod)
mutated_mod['func_1396'] = func_1396
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1396_call = mutated_mod.get_global_var('func_1396')
var_1398 = relay.var("var_1398", dtype = "float64", shape = (600,))#candidate|1398|(600,)|var|float64
var_1399 = relay.var("var_1399", dtype = "float64", shape = (10, 14, 13))#candidate|1399|(10, 14, 13)|var|float64
var_1400 = relay.var("var_1400", dtype = "float64", shape = (10, 14, 13))#candidate|1400|(10, 14, 13)|var|float64
call_1397 = func_1396_call(var_1398,var_1399,var_1400,)
output = call_1397
func_1401 = relay.Function([var_1398,var_1399,var_1400,], output)
mutated_mod['func_1401'] = func_1401
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1120_call = mod.get_global_var('func_1120')
func_1122_call = mutated_mod.get_global_var('func_1122')
call_1476 = relay.TupleGetItem(func_1120_call(), 0)
call_1477 = relay.TupleGetItem(func_1122_call(), 0)
func_703_call = mod.get_global_var('func_703')
func_705_call = mutated_mod.get_global_var('func_705')
var_1484 = relay.var("var_1484", dtype = "float64", shape = (600,))#candidate|1484|(600,)|var|float64
call_1483 = relay.TupleGetItem(func_703_call(relay.reshape(var_1484.astype('float64'), [15, 4, 10])), 0)
call_1485 = relay.TupleGetItem(func_705_call(relay.reshape(var_1484.astype('float64'), [15, 4, 10])), 0)
output = relay.Tuple([call_1476,call_1483,var_1484,])
output2 = relay.Tuple([call_1477,call_1485,var_1484,])
func_1490 = relay.Function([var_1484,], output)
mod['func_1490'] = func_1490
mod = relay.transform.InferType()(mod)
mutated_mod['func_1490'] = func_1490
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1491 = relay.var("var_1491", dtype = "float64", shape = (600,))#candidate|1491|(600,)|var|float64
func_1490_call = mutated_mod.get_global_var('func_1490')
call_1492 = func_1490_call(var_1491)
output = call_1492
func_1493 = relay.Function([var_1491], output)
mutated_mod['func_1493'] = func_1493
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1510 = relay.var("var_1510", dtype = "uint8", shape = (2, 7, 1))#candidate|1510|(2, 7, 1)|var|uint8
var_1511 = relay.var("var_1511", dtype = "uint8", shape = (2, 7, 8))#candidate|1511|(2, 7, 8)|var|uint8
bop_1512 = relay.left_shift(var_1510.astype('uint8'), var_1511.astype('uint8')) # shape=(2, 7, 8)
var_1519 = relay.var("var_1519", dtype = "uint8", shape = (2, 7, 10))#candidate|1519|(2, 7, 10)|var|uint8
bop_1520 = relay.less(var_1510.astype('bool'), var_1519.astype('bool')) # shape=(2, 7, 10)
output = relay.Tuple([bop_1512,bop_1520,])
output2 = relay.Tuple([bop_1512,bop_1520,])
func_1530 = relay.Function([var_1510,var_1511,var_1519,], output)
mod['func_1530'] = func_1530
mod = relay.transform.InferType()(mod)
var_1531 = relay.var("var_1531", dtype = "uint8", shape = (2, 7, 1))#candidate|1531|(2, 7, 1)|var|uint8
var_1532 = relay.var("var_1532", dtype = "uint8", shape = (2, 7, 8))#candidate|1532|(2, 7, 8)|var|uint8
var_1533 = relay.var("var_1533", dtype = "uint8", shape = (2, 7, 10))#candidate|1533|(2, 7, 10)|var|uint8
output = func_1530(var_1531,var_1532,var_1533,)
func_1534 = relay.Function([var_1531,var_1532,var_1533,], output)
mutated_mod['func_1534'] = func_1534
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1300_call = mod.get_global_var('func_1300')
func_1302_call = mutated_mod.get_global_var('func_1302')
call_1560 = relay.TupleGetItem(func_1300_call(), 0)
call_1561 = relay.TupleGetItem(func_1302_call(), 0)
const_1569 = relay.const([[[7.190866,-5.993676,2.277388,6.413307,2.612024,-6.920750,-2.964118,1.836386,8.095956,3.422963,4.618178,9.196620,4.960505],[-5.540348,-3.212638,7.429519,5.986161,7.559598,-6.687860,-2.829224,-0.654096,7.730736,-3.531710,-2.222872,2.469495,2.739016],[0.401357,1.408594,-2.132135,0.772222,3.368414,-6.545484,-0.945397,-6.285641,-0.769095,3.102406,7.853364,-3.703333,3.878641],[2.593741,-4.056997,0.979315,-7.238390,-2.522142,-2.728135,6.274467,-5.498787,5.805600,4.918920,-3.742767,-8.434144,8.708602],[-1.665348,-7.862417,-9.815847,-8.546404,-4.024841,-8.477883,4.874595,-6.107585,-4.776610,8.156949,5.949545,-1.003715,-1.733246],[4.686201,-7.868002,-0.611903,-6.047911,-4.337165,3.438787,5.151477,-5.088198,-0.671644,0.992000,-3.947587,-9.985667,-5.695447],[-1.998369,3.234349,1.023735,8.119791,5.082868,7.269834,-3.612742,-2.218161,-2.050626,-0.306871,-5.536483,-2.802636,2.763103],[5.977973,9.124243,0.314491,-2.421823,-0.420361,8.340494,0.514774,-4.209685,-7.694228,-5.887002,-1.331538,8.826844,-6.047492],[0.976920,3.655774,2.070651,-9.445523,-9.708586,-9.347120,-5.085870,4.051166,-7.873877,-8.143804,7.946468,-1.303633,-0.134714],[-5.515241,5.196624,9.325788,-4.866126,9.125605,0.252319,-5.725540,6.281778,8.790133,0.785768,-2.454038,5.345948,-7.860438],[6.743011,9.603906,4.853193,1.713556,-9.527918,8.461384,5.683573,-5.730481,5.977812,5.356796,6.604899,-5.759404,1.981610],[-8.091857,-8.933576,3.641661,2.208132,6.670281,-1.649616,9.368053,2.166030,8.212711,7.415517,9.303120,-7.716201,-6.815957],[3.726009,9.248720,2.283779,-5.212911,-7.404158,1.410606,-0.836446,1.954875,-9.967563,3.110159,9.405346,-7.917648,-0.564138],[4.266181,-3.307685,-6.351906,8.696065,-6.185501,2.132960,-6.759240,-9.820829,-3.362561,-1.560903,-2.562820,-1.376463,-6.113543]],[[-1.718289,6.254434,-3.712624,-1.697760,-9.116048,9.414679,-5.122842,-5.469561,-4.846590,2.296208,-1.518900,4.993849,6.557234],[4.467787,7.135009,-8.085906,8.090941,-2.305684,-4.713371,-4.014601,6.473769,-1.210862,-2.794444,0.544448,7.135175,9.536488],[-5.682178,-4.325991,-5.016692,-1.058799,3.823768,-1.486019,-6.527308,1.874203,5.194869,8.472815,1.621907,-2.099739,-2.755260],[-9.198465,-3.866644,9.242872,-6.999828,6.669403,-3.867257,-7.849188,-5.910307,-2.718819,1.231369,4.838535,6.115968,3.678995],[0.361714,-9.887828,3.110166,5.890282,5.137165,3.373653,2.373056,-4.485422,-7.040267,2.844248,1.678642,0.997941,9.192800],[0.485153,7.998291,7.214416,-4.282460,-8.305838,-9.374345,-6.751546,-1.744196,8.755310,-1.093792,1.483465,-5.446750,4.296461],[-2.547934,-8.303058,5.436605,3.649525,-1.632998,6.460393,-3.046015,4.187268,-1.658363,-5.069012,9.301420,-0.255872,-4.776708],[-7.714036,-6.344293,-2.923357,-3.180409,7.559875,5.723088,-6.247806,0.168321,-4.329340,6.624587,0.592531,7.356378,-5.987134],[7.275711,-6.518988,8.335478,4.153679,-3.970506,-7.731560,-5.627633,1.950540,-9.914482,-1.034030,6.838175,-2.911911,-1.808277],[-7.253442,3.502557,-7.430848,8.111136,-4.387185,3.045310,8.764472,-7.395048,-4.472385,7.475202,-9.454751,7.429782,5.949043],[9.370697,2.562258,9.271192,-4.705200,-6.883739,-2.433405,3.540860,-9.213334,-6.763248,4.348415,-9.810125,3.092183,8.357429],[5.395372,-8.556859,8.314624,-9.876535,4.507846,6.936292,7.950899,-1.863749,4.580573,-1.742694,-5.980218,9.391831,8.514149],[0.822452,9.162981,-1.643998,8.869532,-2.674118,4.548589,1.533664,-3.113797,-8.056356,3.590035,6.220578,-6.526179,-9.794619],[-6.182299,-2.855950,3.054111,3.014553,-4.671174,-8.988711,-7.446790,8.442086,6.638506,1.100519,1.164790,6.440504,-4.537297]],[[4.094267,4.985884,-9.199418,-4.161844,5.484548,-8.755750,-8.103773,6.367147,2.705224,7.266785,0.176133,2.228829,1.089576],[-1.461522,1.485224,3.985228,2.454157,2.369576,7.576489,0.994538,4.417299,4.627127,-3.720452,-6.802940,-9.412949,-9.882025],[0.912388,-5.384932,-0.021587,5.119701,-2.952135,9.994428,1.107517,8.637670,-1.756495,-0.302263,-3.535535,7.083790,-3.920184],[-6.138960,-8.004169,-0.568407,6.795632,-4.919170,9.596512,7.020470,-3.865824,0.211069,2.321389,-4.867757,9.416569,-1.880651],[-9.677295,1.543144,9.725088,-2.068708,-2.357607,5.085759,6.695065,-4.071922,-6.101956,-0.326973,-3.603363,-4.901832,-6.403507],[2.495742,5.671207,-8.794726,9.371320,-5.080724,2.233460,-5.082570,3.511466,2.347655,7.616387,0.016254,-8.176428,6.165564],[-3.218199,-7.385174,-4.406945,-6.732090,7.257098,-2.803247,-5.638114,-3.009780,1.000883,-2.370151,-6.087940,7.253782,6.531511],[8.197252,9.372008,-8.801749,0.003367,-6.187199,-0.722957,8.596110,8.150550,-2.740565,2.023445,-1.110533,-6.732794,1.560197],[-2.007336,-6.068141,-5.860830,1.948540,-3.920657,1.161894,2.265526,-6.184349,-4.673260,8.719148,7.234665,-4.570389,-3.055525],[9.480741,9.991379,-7.504979,6.964578,0.179538,-9.820379,9.932944,-1.327247,-6.744415,1.174095,5.682613,9.466076,8.698807],[-3.274818,0.157710,-4.828889,0.146634,8.919223,-1.523072,3.144399,-1.663732,-9.656467,-1.052657,-2.700056,-1.567436,3.977887],[-0.574056,9.808321,7.036282,4.326546,-0.026405,1.062546,9.449880,6.779980,-0.595336,3.364334,4.637869,-1.430509,-5.741957],[-8.109931,-7.433162,-1.671400,-0.625066,2.189603,4.419455,-5.178139,-2.750817,-1.673493,7.973041,9.388548,-3.383100,-7.792624],[8.501514,3.747828,-3.807456,-6.805889,-7.836372,1.679665,-5.288329,-4.698234,5.670819,-3.891206,7.968323,3.314362,-8.506210]],[[-9.397249,6.282367,-7.114016,3.563736,-9.609242,-0.507970,7.576247,9.101513,1.676090,6.778729,1.274367,4.686646,-0.759331],[-7.782733,9.618821,7.697368,3.255682,-8.619469,8.968392,-7.155051,1.143104,-5.958464,2.074918,2.504533,-3.127702,-3.880527],[9.843417,1.309704,-1.635697,0.729439,-3.941785,3.084182,3.021516,-2.851641,-6.784653,-4.354767,6.449111,-3.758321,-1.432993],[5.698222,-5.024556,4.024999,9.416322,9.774622,-7.907205,4.251823,0.201229,2.288778,9.601526,3.830520,-4.830045,3.975635],[6.466206,-5.570914,-4.998327,-1.984897,1.718334,-5.591371,-0.209447,7.974818,1.538805,2.195423,9.550937,6.411897,-0.842003],[-9.460685,0.553044,-0.949359,9.676310,-0.881424,8.295056,-6.234378,-9.661358,9.915594,7.105355,-9.505988,-7.282536,8.824074],[-1.826219,-8.357804,-1.036920,6.266017,-6.315527,-9.492936,-8.356307,4.414535,4.526927,-2.538322,3.603948,-5.709889,-8.912944],[7.106971,-1.016151,5.043568,7.004217,-4.839697,-5.375069,1.925477,8.338881,6.137497,7.932188,9.755503,-8.073069,-8.872898],[-7.831277,-3.935699,9.535131,7.995959,8.693104,-9.834430,-2.454184,-2.623316,-5.211834,0.551507,4.061463,7.625251,-4.856877],[9.769841,0.190199,-4.443028,-8.501182,-4.921932,-0.262869,8.310920,-2.456964,-8.586983,-0.584172,-5.354001,2.785100,8.883829],[-4.404866,6.281738,8.174239,3.812427,-4.444873,-9.627045,3.277556,4.065450,-1.394766,7.748623,-6.202657,9.652343,-1.522385],[-3.164549,-3.051654,-1.438286,-7.920004,7.781850,-9.140948,-1.749309,-4.544461,7.470726,-2.164949,8.859956,9.944713,5.043173],[-7.993910,4.031412,-3.150475,-4.849083,9.014569,5.336534,-9.702897,6.645666,-4.199528,-8.628217,2.102848,-4.548413,-8.356502],[-2.534586,-3.468848,2.823893,5.907751,4.501092,-7.935330,-2.727278,-3.411140,-0.099979,-7.161828,4.565052,5.741968,6.817616]],[[0.492273,-8.759149,3.639098,9.759176,5.557288,-4.857144,5.271023,-7.869670,-3.445731,7.538984,6.068464,5.399861,-3.723934],[-2.197948,-3.094085,-6.994397,3.666925,4.820255,7.251445,-3.542867,-4.516749,2.941803,-5.217553,7.184089,-5.140780,5.604977],[-3.942917,5.614117,5.892765,2.142833,4.335027,4.260044,-4.539145,8.474281,9.168941,-1.035342,0.100659,-8.864795,-4.275182],[-1.163265,-9.719889,-3.063549,-2.153114,5.891034,5.305293,-6.949055,-1.345328,7.305739,-3.723797,0.230974,-5.763077,2.056322],[3.444986,0.213517,-3.222498,8.658162,7.791831,5.729514,7.828181,5.928256,6.036535,-4.124438,0.259925,0.221771,-5.238611],[0.271194,-5.801313,-6.408772,-8.074214,8.892862,8.199101,-6.629101,-2.646118,1.099194,-8.000704,-9.291044,-4.638970,-9.834818],[-0.516467,7.903611,-9.045420,2.061857,-8.284184,-2.920131,4.422329,3.656831,-4.585749,9.503712,6.049492,4.552055,3.674609],[-3.603744,-5.438200,9.501581,-0.519103,4.048959,-4.415459,9.677719,1.743753,3.280180,-3.913367,4.686715,-5.369632,9.171023],[8.646539,-6.788469,7.938689,-7.939940,5.753330,-6.316675,4.206615,-5.942391,8.169607,-9.896134,2.602525,1.139766,-5.892195],[2.991923,-1.069388,-8.677456,2.842991,-4.105693,2.174021,-6.678458,7.669858,-2.876097,-1.632656,-8.121187,1.881519,-5.228934],[-5.706451,-7.587826,1.523480,-5.892980,-9.594724,7.337503,3.797701,-8.000268,7.044864,8.310784,-4.698626,5.796961,-7.710237],[-5.998750,-0.804222,-1.520815,-4.959132,3.628166,-9.596450,9.128429,-2.617135,-1.302720,1.607268,4.068140,4.039210,2.479456],[-6.795964,4.342369,-9.355650,-4.556761,-6.069669,5.411355,0.770901,-4.317488,-8.532925,0.427518,7.623281,-7.711914,-1.442198],[5.637772,-7.549112,0.349420,2.037518,2.550967,-4.651742,-6.119353,0.777892,-9.252972,-1.846134,-2.351621,-6.963330,2.386696]],[[-9.736996,-9.809594,7.699006,-8.892506,-7.982243,9.598761,-3.074484,6.941316,-8.829136,-0.954124,-6.660142,0.179428,9.235416],[2.302341,5.873488,9.325749,0.946860,-0.735474,6.745983,-0.761561,9.352021,2.140726,6.843495,-6.876175,-9.065816,8.989585],[7.942303,0.545388,-5.174243,8.582725,-0.791088,0.213978,-3.450168,-2.809116,8.254487,-8.004289,-6.517737,-0.926779,-1.604598],[-0.257730,6.420694,3.616357,-6.295150,-3.001204,-4.000911,-5.413498,-0.020534,-4.362606,6.199455,6.262939,5.276333,5.696756],[1.956672,7.748461,0.332793,1.688114,6.643235,0.033216,0.942928,5.410171,7.409729,-9.881527,7.780527,2.608339,-9.885846],[4.489471,-7.988347,3.186103,1.745144,7.427798,-5.892635,0.852553,-8.807671,2.322421,-6.518828,7.213825,-7.554060,-3.425800],[-5.479957,3.085643,-0.017656,-1.016145,8.901398,-0.540336,7.175827,1.391708,-0.909649,8.557457,-5.165004,0.051380,5.674991],[-8.459429,-0.099781,-6.804761,-9.204975,9.670292,-0.296867,7.469307,-2.538659,-2.690086,-6.489241,9.225222,2.074284,9.296847],[-3.917543,-3.192987,1.228609,1.764902,0.777563,-9.363777,1.117894,-2.290108,4.790008,-3.217812,-9.218755,7.901249,-0.036529],[0.873598,-6.600257,3.961246,6.379466,-3.478150,8.012983,2.202932,6.588872,-3.489690,6.284369,3.405722,3.308571,-2.200784],[-5.258112,-8.892904,0.915197,-8.531814,-8.457226,-7.328947,-6.840470,-5.483961,-7.125912,-7.763883,7.351207,5.552063,-9.275653],[8.757456,-5.967555,7.098640,-9.675377,3.506857,6.558477,8.377741,-5.388401,-3.573721,-2.347087,-3.609507,-4.172794,2.161718],[7.149666,-8.348214,9.653188,0.578056,-3.567164,-7.923010,-1.042208,-4.313434,-1.798646,0.766315,7.652014,0.101542,-8.740168],[-3.845974,-7.924767,-6.087761,-1.369069,7.847433,8.250933,5.859011,4.697248,-6.596925,-6.664583,-9.321902,-5.651980,8.925286]],[[9.716396,3.789939,-3.627389,-1.039621,9.779806,-7.217812,5.353658,7.749407,4.712712,-6.540432,4.596014,-2.416194,4.872015],[-4.144454,4.698199,2.750327,-3.848259,-8.866877,1.353657,8.937910,-3.088525,-8.383098,-9.189589,-3.078977,4.971059,-4.903014],[2.245525,-4.340659,6.376247,-9.716684,-3.969988,6.292334,-1.020995,9.917597,-8.333718,9.067294,-9.034371,2.534368,1.545093],[-1.049323,-2.853345,0.077481,-2.642428,7.918512,-3.816332,-3.637594,0.063927,1.706544,7.805512,1.047167,-9.959362,-4.848721],[0.968121,8.365556,7.134738,9.377761,-1.082738,4.884327,-1.898854,0.226876,-3.517859,4.980243,5.396088,-0.988586,6.095570],[4.893917,-2.664324,-9.333471,9.515525,-6.423428,-3.119210,-3.901747,4.110699,5.635401,-0.095684,-7.595357,-1.278663,0.916506],[2.725212,-8.147965,3.600910,-0.052264,-7.718384,3.208702,-8.966634,-1.541900,2.102892,6.072711,6.649729,-6.893181,8.400324],[-0.279970,-4.969132,-5.239965,9.599476,-4.440628,-4.135457,-2.690530,-9.117884,-4.832190,-4.781929,5.537165,0.500761,-6.729256],[0.244993,9.255058,2.573685,-3.586790,0.105311,6.094490,0.468577,2.614221,-1.912126,-7.924794,-4.794602,1.018047,-9.472065],[-0.591238,-6.504995,-1.832831,-9.129334,-9.977927,8.439929,7.033030,9.053149,-1.277066,7.318332,-6.366122,2.687297,-0.902034],[6.834261,-4.701271,-5.800559,-8.311062,0.730483,-1.645555,-6.235972,-0.571696,5.049278,-7.429793,-8.075228,4.704813,-4.369405],[-8.880203,8.555048,1.706469,-1.094267,-2.785504,7.592670,8.133609,3.854638,-4.723447,3.871495,1.990419,-8.291103,2.107357],[-7.300071,-3.952885,0.654858,3.671588,2.799029,5.839583,-3.318862,-2.763072,-3.055297,7.841992,5.808697,5.404813,-6.202645],[6.547634,-7.032095,1.155229,-5.013767,-6.231862,-1.630002,-4.594887,-5.996680,-3.611482,0.050122,-3.606090,-6.336635,7.149061]],[[6.162570,-4.617777,4.687413,3.686507,9.058065,9.216800,-1.871226,0.314483,6.471581,3.899776,0.987246,-3.233675,-1.574025],[5.786258,-9.349825,9.612210,1.590402,8.140118,1.415770,8.075550,-8.070947,-7.366745,-8.318394,8.785119,4.036614,0.637064],[-8.854898,2.932387,2.089083,-1.213264,9.762866,8.680647,7.813214,-9.576807,6.986886,6.655083,-4.143612,6.510663,8.947946],[-9.089305,8.628771,-9.552541,9.726257,-5.807836,-8.503100,0.148571,-7.607788,-7.924327,7.933823,5.587481,-8.281805,-7.806356],[-0.224526,7.697462,9.431460,9.544035,-2.060614,-4.387012,1.869097,-7.052876,5.852027,-7.839173,-5.078618,-5.434712,9.182796],[0.478106,-9.205401,-8.106322,2.843432,5.269573,7.280851,3.345021,-1.107633,8.241422,-3.060015,2.096766,5.098289,-6.842105],[-4.536993,-7.128069,-3.686780,-9.596687,7.534433,8.480508,-5.109192,8.998513,7.011387,1.750959,4.506741,-4.325192,-1.860442],[7.449336,2.201839,-9.110765,-1.716616,5.581517,-9.823117,-6.624395,-7.825592,-6.519254,-1.711893,-0.392761,-7.220654,2.750038],[-5.259082,6.953039,3.519085,6.080110,-5.184775,-4.280896,-5.087228,6.050794,8.044064,-2.960014,-9.498557,7.497538,3.633959],[-1.864276,6.528387,5.597161,1.516942,4.394030,4.562696,2.671994,-7.020398,0.686123,1.281858,1.664670,-3.890617,-3.610835],[-5.232250,6.483588,3.475123,4.557228,0.380418,7.260571,5.729740,6.416468,9.712424,2.417509,-7.447946,-5.938620,2.045999],[6.165660,6.613344,-2.853671,1.777922,8.915388,-3.403067,0.044742,7.390302,-1.226157,5.677759,-3.224554,8.714580,-8.843917],[-9.468148,3.727464,-6.780811,0.148716,7.947426,8.156398,6.435354,2.494417,4.843198,1.447276,5.482133,-4.698425,3.782746],[7.486971,-0.402369,-5.432151,-0.750544,-1.040708,-5.425246,5.889881,-1.223989,-9.657457,2.998028,2.504154,4.989079,-1.427373]],[[-2.723769,5.080197,4.922169,-6.839405,3.345519,-7.781464,5.403875,-7.821771,-5.237027,3.914910,1.097886,-7.102847,6.004421],[9.957663,-6.864416,-7.638908,-2.858019,-5.432023,-7.741121,8.905072,0.782618,-7.459655,3.134431,3.448324,-2.081963,-3.089960],[-0.809422,-4.447789,-6.593303,-4.046695,6.972612,8.554288,4.946983,8.461407,9.784751,9.346919,-5.199466,1.369700,-3.000719],[1.598353,8.212798,-7.065413,-3.363546,4.245771,2.360949,0.574500,-4.364945,-0.922212,-9.555808,-6.028774,2.648690,5.832449],[0.490846,7.311403,6.751228,-8.331762,-9.815781,-4.189832,9.051886,9.207722,-3.044264,-0.027381,6.029116,-3.701524,-6.788433],[6.315333,-9.178630,-9.114150,7.371952,2.632819,-8.812773,0.740925,5.161576,-2.115618,-8.886129,8.396127,-6.412742,9.311162],[-3.854823,-0.645595,-7.371774,-1.461112,-5.310580,-1.004355,-4.646876,-6.810515,5.213567,8.601872,3.037267,-0.988603,3.465532],[-3.196002,8.372104,-0.201148,0.212872,-0.305729,-4.492942,-6.697637,1.580556,0.404774,3.583526,3.119396,9.144224,2.700695],[-2.235118,-3.431672,1.386289,2.744888,5.642155,-6.701168,-7.465736,-7.433206,-2.002656,4.605076,-6.684864,5.573302,-7.465035],[-8.362557,-3.710321,4.963683,0.334740,-1.872171,-8.843234,9.829898,0.855129,9.595859,1.530852,1.181123,-6.227380,1.567868],[5.404721,-3.346141,2.364139,4.891832,-8.947744,-4.281821,1.025293,-2.899587,8.032640,7.942349,-5.414045,-1.438256,-5.991050],[7.933440,4.755595,0.187266,0.224173,-1.432331,4.256184,-1.314817,-6.675090,8.623186,-3.622708,-8.847387,-0.819864,-0.328179],[-6.451485,-1.889418,-2.552850,4.745359,-7.586338,-9.674258,4.086263,7.361675,2.743708,-3.745825,-7.910737,4.855712,-9.891716],[-4.530856,1.706586,7.992326,-5.036851,-2.040718,1.752609,-1.018322,0.899712,3.929974,9.537173,8.561189,1.336764,7.523001]],[[6.213539,-0.941701,-1.026454,-5.301782,0.146866,5.308341,3.204318,3.827962,5.680941,8.639163,-1.289244,7.991811,8.466926],[-0.596668,5.703657,-2.039149,-9.853696,-5.555396,-9.603424,-7.280844,-3.177089,3.414689,-8.536640,-7.062185,-1.853880,-0.887038],[-0.128049,-8.871056,-4.365080,-2.954787,-4.281309,-2.361019,7.492999,3.747388,-2.978275,-4.320208,2.204405,-2.199815,-9.586110],[-8.061263,-3.591570,3.478964,-9.566105,-1.202765,2.794567,-7.619939,-1.486188,-5.826670,2.934647,8.213352,-7.554940,-1.791166],[0.051536,6.066305,0.997189,-0.439373,-4.888110,0.185074,1.059757,6.421704,-4.899237,4.991750,-4.701124,8.241371,2.701012],[0.186266,-6.318331,-3.982117,9.271038,0.955692,1.590204,-0.089383,5.795923,-5.161009,-1.993083,9.080081,-9.571803,5.596535],[3.777478,-3.250411,6.852011,-7.722465,-0.312337,0.690451,-8.367743,-8.559384,-7.791377,0.034703,-2.467553,-0.980082,7.258217],[-7.764500,-2.515148,-5.412058,-9.476792,7.231771,7.745530,8.403161,-6.480529,9.679753,4.424787,-2.468179,-8.241093,2.441197],[4.268209,0.680801,-2.424841,-2.944019,0.885472,-5.190850,-8.867434,1.419972,9.622735,6.196744,2.285275,-3.480449,-2.444799],[-8.949502,-8.561570,-9.618746,-9.566337,-8.514628,4.439527,7.015917,2.964899,-5.377779,4.285676,6.631901,-5.418930,-6.492251],[2.520471,-4.157121,6.994374,7.344825,-4.970208,-6.804812,1.906308,8.236695,0.206141,-3.947616,-6.412674,-4.407354,-6.215060],[-7.354521,-7.516444,5.408602,3.651934,-1.663249,-3.236254,-8.682430,8.934414,0.015877,1.070585,0.575805,-1.141639,-3.393873],[-1.133381,-4.744788,-4.797686,1.531474,-6.038701,2.275645,-5.215710,-8.408573,6.227652,3.309820,6.787844,0.118094,-7.662605],[-2.400183,-9.110762,2.149232,9.860357,-4.314801,8.664061,3.396296,-3.706801,0.293800,-6.392122,4.565661,0.941157,-7.601729]]], dtype = "float64")#candidate|1569|(10, 14, 13)|const|float64
bop_1570 = relay.mod(call_1560.astype('float64'), relay.reshape(const_1569.astype('float64'), relay.shape_of(call_1560))) # shape=(10, 14, 13)
bop_1573 = relay.mod(call_1561.astype('float64'), relay.reshape(const_1569.astype('float64'), relay.shape_of(call_1561))) # shape=(10, 14, 13)
bop_1593 = relay.bitwise_or(call_1560.astype('uint16'), relay.reshape(const_1569.astype('uint16'), relay.shape_of(call_1560))) # shape=(10, 14, 13)
bop_1596 = relay.bitwise_or(call_1561.astype('uint16'), relay.reshape(const_1569.astype('uint16'), relay.shape_of(call_1561))) # shape=(10, 14, 13)
bop_1598 = relay.floor_divide(bop_1570.astype('float64'), relay.reshape(call_1560.astype('float64'), relay.shape_of(bop_1570))) # shape=(10, 14, 13)
bop_1601 = relay.floor_divide(bop_1573.astype('float64'), relay.reshape(call_1561.astype('float64'), relay.shape_of(bop_1573))) # shape=(10, 14, 13)
func_1120_call = mod.get_global_var('func_1120')
func_1122_call = mutated_mod.get_global_var('func_1122')
call_1615 = relay.TupleGetItem(func_1120_call(), 0)
call_1616 = relay.TupleGetItem(func_1122_call(), 0)
output = relay.Tuple([bop_1593,bop_1598,call_1615,])
output2 = relay.Tuple([bop_1596,bop_1601,call_1616,])
func_1634 = relay.Function([], output)
mod['func_1634'] = func_1634
mod = relay.transform.InferType()(mod)
mutated_mod['func_1634'] = func_1634
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1634_call = mutated_mod.get_global_var('func_1634')
call_1635 = func_1634_call()
output = call_1635
func_1636 = relay.Function([], output)
mutated_mod['func_1636'] = func_1636
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1188_call = mod.get_global_var('func_1188')
func_1190_call = mutated_mod.get_global_var('func_1190')
call_1640 = func_1188_call()
call_1641 = func_1188_call()
output = call_1640
output2 = call_1641
func_1659 = relay.Function([], output)
mod['func_1659'] = func_1659
mod = relay.transform.InferType()(mod)
mutated_mod['func_1659'] = func_1659
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1659_call = mutated_mod.get_global_var('func_1659')
call_1660 = func_1659_call()
output = call_1660
func_1661 = relay.Function([], output)
mutated_mod['func_1661'] = func_1661
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1300_call = mod.get_global_var('func_1300')
func_1302_call = mutated_mod.get_global_var('func_1302')
call_1684 = relay.TupleGetItem(func_1300_call(), 0)
call_1685 = relay.TupleGetItem(func_1302_call(), 0)
output = call_1684
output2 = call_1685
func_1686 = relay.Function([], output)
mod['func_1686'] = func_1686
mod = relay.transform.InferType()(mod)
mutated_mod['func_1686'] = func_1686
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1686_call = mutated_mod.get_global_var('func_1686')
call_1687 = func_1686_call()
output = call_1687
func_1688 = relay.Function([], output)
mutated_mod['func_1688'] = func_1688
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1120_call = mod.get_global_var('func_1120')
func_1122_call = mutated_mod.get_global_var('func_1122')
call_1714 = relay.TupleGetItem(func_1120_call(), 0)
call_1715 = relay.TupleGetItem(func_1122_call(), 0)
var_1720 = relay.var("var_1720", dtype = "float64", shape = (10, 14, 13))#candidate|1720|(10, 14, 13)|var|float64
bop_1721 = relay.minimum(call_1714.astype('int32'), relay.reshape(var_1720.astype('int32'), relay.shape_of(call_1714))) # shape=(10, 14, 13)
bop_1724 = relay.minimum(call_1715.astype('int32'), relay.reshape(var_1720.astype('int32'), relay.shape_of(call_1715))) # shape=(10, 14, 13)
func_1530_call = mod.get_global_var('func_1530')
func_1534_call = mutated_mod.get_global_var('func_1534')
const_1740 = relay.const([-10,2,1,-5,-7,6,-2,2,-3,-2,3,6,4,8], dtype = "uint8")#candidate|1740|(14,)|const|uint8
const_1741 = relay.const([-2,-5,10,-8,4,-7,-3,-3,6,9,2,7,6,3,7,4,3,-4,7,8,-9,2,-4,6,-2,10,-7,-2,-10,6,1,9,-1,-6,6,8,1,-7,6,4,8,-1,-3,-7,-2,-2,-3,4,5,2,6,-9,1,-9,-1,4,9,6,10,4,-6,-4,9,-3,-8,8,-7,8,-4,5,-1,7,-6,-3,6,-10,-6,-3,2,1,-5,3,-7,7,9,-9,3,-4,8,-5,3,-9,10,5,-2,-2,-7,-8,-6,-10,-9,9,4,8,9,6,-1,-2,-1,-2,3,-1], dtype = "uint8")#candidate|1741|(112,)|const|uint8
const_1742 = relay.const([[4,8],[1,2],[-10,-1],[4,-8],[7,-9],[-7,-7],[-9,-2],[10,10],[4,-5],[-5,-9],[1,-3],[-5,1],[7,10],[-7,7],[-9,-8],[9,-2],[7,9],[4,4],[-7,2],[2,-5],[-3,4],[-2,-7],[-10,-10],[4,-3],[9,2],[2,-1],[-5,-3],[6,5],[-3,-1],[-10,7],[-3,10],[-7,8],[-6,1],[6,-7],[7,-9],[9,6],[5,-6],[6,-4],[8,-6],[-8,5],[5,-2],[-10,-6],[-10,-1],[9,9],[-5,-8],[8,-9],[9,-5],[2,-8],[8,9],[-8,4],[-10,-5],[4,-4],[10,-9],[-5,9],[6,8],[6,4],[-8,1],[-8,4],[-1,6],[4,4],[1,4],[-2,1],[-9,-3],[-6,8],[-9,-10],[3,4],[2,1],[9,1],[9,-7],[2,-8]], dtype = "uint8")#candidate|1742|(70, 2)|const|uint8
call_1739 = relay.TupleGetItem(func_1530_call(relay.reshape(const_1740.astype('uint8'), [2, 7, 1]), relay.reshape(const_1741.astype('uint8'), [2, 7, 8]), relay.reshape(const_1742.astype('uint8'), [2, 7, 10]), ), 0)
call_1743 = relay.TupleGetItem(func_1534_call(relay.reshape(const_1740.astype('uint8'), [2, 7, 1]), relay.reshape(const_1741.astype('uint8'), [2, 7, 8]), relay.reshape(const_1742.astype('uint8'), [2, 7, 10]), ), 0)
output = relay.Tuple([bop_1721,call_1739,const_1740,const_1741,const_1742,])
output2 = relay.Tuple([bop_1724,call_1743,const_1740,const_1741,const_1742,])
func_1744 = relay.Function([var_1720,], output)
mod['func_1744'] = func_1744
mod = relay.transform.InferType()(mod)
var_1745 = relay.var("var_1745", dtype = "float64", shape = (10, 14, 13))#candidate|1745|(10, 14, 13)|var|float64
output = func_1744(var_1745)
func_1746 = relay.Function([var_1745], output)
mutated_mod['func_1746'] = func_1746
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1066_call = mod.get_global_var('func_1066')
func_1068_call = mutated_mod.get_global_var('func_1068')
call_1871 = relay.TupleGetItem(func_1066_call(), 0)
call_1872 = relay.TupleGetItem(func_1068_call(), 0)
output = relay.Tuple([call_1871,])
output2 = relay.Tuple([call_1872,])
func_1873 = relay.Function([], output)
mod['func_1873'] = func_1873
mod = relay.transform.InferType()(mod)
mutated_mod['func_1873'] = func_1873
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1873_call = mutated_mod.get_global_var('func_1873')
call_1874 = func_1873_call()
output = call_1874
func_1875 = relay.Function([], output)
mutated_mod['func_1875'] = func_1875
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1300_call = mod.get_global_var('func_1300')
func_1302_call = mutated_mod.get_global_var('func_1302')
call_1944 = relay.TupleGetItem(func_1300_call(), 0)
call_1945 = relay.TupleGetItem(func_1302_call(), 0)
output = relay.Tuple([call_1944,])
output2 = relay.Tuple([call_1945,])
func_1955 = relay.Function([], output)
mod['func_1955'] = func_1955
mod = relay.transform.InferType()(mod)
mutated_mod['func_1955'] = func_1955
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1955_call = mutated_mod.get_global_var('func_1955')
call_1956 = func_1955_call()
output = call_1956
func_1957 = relay.Function([], output)
mutated_mod['func_1957'] = func_1957
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1686_call = mod.get_global_var('func_1686')
func_1688_call = mutated_mod.get_global_var('func_1688')
call_1990 = func_1686_call()
call_1991 = func_1686_call()
uop_1998 = relay.exp(call_1990.astype('float64')) # shape=(10, 14, 13)
uop_2000 = relay.exp(call_1991.astype('float64')) # shape=(10, 14, 13)
uop_2003 = relay.cos(uop_1998.astype('float64')) # shape=(10, 14, 13)
uop_2005 = relay.cos(uop_2000.astype('float64')) # shape=(10, 14, 13)
output = relay.Tuple([uop_2003,])
output2 = relay.Tuple([uop_2005,])
func_2010 = relay.Function([], output)
mod['func_2010'] = func_2010
mod = relay.transform.InferType()(mod)
output = func_2010()
func_2011 = relay.Function([], output)
mutated_mod['func_2011'] = func_2011
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2021 = relay.var("var_2021", dtype = "float32", shape = (9, 13, 11))#candidate|2021|(9, 13, 11)|var|float32
uop_2022 = relay.asin(var_2021.astype('float32')) # shape=(9, 13, 11)
output = relay.Tuple([uop_2022,])
output2 = relay.Tuple([uop_2022,])
func_2024 = relay.Function([var_2021,], output)
mod['func_2024'] = func_2024
mod = relay.transform.InferType()(mod)
var_2025 = relay.var("var_2025", dtype = "float32", shape = (9, 13, 11))#candidate|2025|(9, 13, 11)|var|float32
output = func_2024(var_2025)
func_2026 = relay.Function([var_2025], output)
mutated_mod['func_2026'] = func_2026
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1300_call = mod.get_global_var('func_1300')
func_1302_call = mutated_mod.get_global_var('func_1302')
call_2115 = relay.TupleGetItem(func_1300_call(), 0)
call_2116 = relay.TupleGetItem(func_1302_call(), 0)
const_2119 = relay.const([[[9.325254,-4.506993,-0.622295,-2.636619,-9.995750,6.601279,-8.657299,2.676516,-7.937537,5.154666,3.180300,-8.332568,-9.654218],[-9.397007,-2.322322,8.513412,-6.251861,4.137603,-7.153558,3.862256,6.736042,-3.502172,-3.500499,-7.338267,2.997898,-1.042733],[4.106047,0.550621,5.920860,4.346206,7.202445,9.549517,-8.752925,-8.076054,6.854650,3.047290,-7.320449,-4.406357,-5.479722],[4.989299,4.646514,-6.897561,4.290763,-5.519250,7.834005,-7.905244,8.772173,-8.906904,-3.787703,-6.898440,8.147417,-0.358730],[6.338349,-2.344239,-8.866978,-2.393699,4.280353,-3.112384,-9.216208,-4.033763,-4.516203,-4.201670,-7.171090,-7.188532,2.320136],[-1.056692,-5.589476,2.006198,-5.873827,0.347054,8.112383,-7.271498,-1.273923,4.330705,2.129813,4.855914,-6.379726,3.381610],[-2.133123,3.971874,-1.132946,-8.413785,1.241581,4.508347,-2.155768,-0.471860,-8.408726,-0.882113,7.551689,7.425857,0.441021],[4.012901,-5.778778,5.608387,-8.927488,-4.964350,-1.494620,4.208876,-8.637038,5.596973,-8.982963,4.850299,-8.830580,7.109864],[8.579866,2.489502,9.705988,3.115821,0.524763,7.933649,2.044411,8.147578,-6.791498,8.119362,9.332206,3.109878,-7.542547],[-7.727103,1.581295,7.425076,-2.594605,0.077747,0.733420,7.211638,2.840169,-4.410327,-3.930239,3.448906,-2.880874,-1.798277],[9.344156,1.574691,-6.364105,4.524394,-2.834082,-5.525951,4.778405,-6.884933,-3.355083,5.340225,-6.925120,7.627534,2.686903],[-0.435741,5.919773,1.354973,-4.568807,9.509411,-0.318511,-4.488911,0.718634,4.409871,6.852048,5.335526,6.587667,6.306535],[-3.875733,5.847686,7.426475,4.780143,-9.909121,-0.395313,-9.416679,4.252424,-6.633669,9.821508,-8.623908,-5.868657,-1.780356],[-7.007698,-9.956719,-3.511918,-7.641721,9.930643,0.863588,-0.904161,0.961051,-6.709502,-1.267508,9.822394,-9.262968,-6.186441]],[[3.269796,-4.318214,-4.010361,-8.898265,-4.786150,6.583934,-9.034152,2.476294,-7.547371,5.911567,-8.395287,4.922451,9.507405],[8.835193,1.654613,-1.075688,-8.817983,-5.926488,5.087616,4.312157,9.684394,-9.721443,9.573571,7.246242,-0.276741,-6.521387],[4.653431,3.705325,-4.250330,-1.557571,6.725525,-5.870402,4.811212,-2.442707,7.324113,-0.376473,6.022975,-0.836918,-6.761730],[-4.552259,-0.055665,2.548728,-1.163919,-9.624728,2.853819,-6.240150,-1.822365,-3.383170,4.760152,-2.784577,8.896133,-3.041390],[-6.317567,7.272092,-5.026888,5.005820,-1.416329,-9.252326,2.570584,4.716436,2.581729,2.317117,0.264858,2.870406,4.608159],[1.168044,9.096634,5.631672,1.067369,-6.026944,-2.416415,-0.407268,5.981988,5.037493,-8.300855,2.400116,-7.161143,0.916824],[4.542691,-8.365544,-6.839646,8.606303,3.382506,2.108311,3.569092,6.773248,5.977435,3.985708,-0.362531,-5.840636,0.256705],[2.286003,-9.298881,1.786104,1.969222,-7.953986,-4.014038,5.530858,-8.844182,-4.795866,2.737929,3.355259,0.541749,4.537821],[8.293133,-5.590447,8.731572,-9.354017,-0.241797,8.887164,-7.914474,-8.726102,1.299200,-5.489497,-8.041083,-0.007502,-7.013069],[3.642492,-1.630383,-7.111143,-3.934688,-6.688707,-7.383809,7.326201,2.760335,-0.070937,5.668292,-4.215419,8.762281,-3.074632],[0.646947,6.441182,8.276142,4.034170,0.159689,1.990058,8.954040,0.408963,6.308791,-7.962000,-6.118905,-6.761681,3.876880],[-3.101508,9.928229,7.101645,3.880430,4.169952,9.449631,-5.369342,-0.174983,-2.853913,-2.157495,7.401542,-8.705426,-4.006453],[-6.649122,-8.545548,3.940581,-8.409369,-3.058069,6.707931,-8.739971,-5.697388,9.174407,-5.686284,-7.426290,3.215098,2.718488],[-2.879521,7.564472,-4.681383,3.619080,9.689275,9.233845,-3.118102,9.025870,-7.238259,-0.764463,8.047268,3.939068,1.491946]],[[-0.413720,-9.373295,9.459306,-9.615375,9.070994,-6.240521,7.552460,4.796554,-8.052443,-1.205204,9.316584,3.049026,9.664691],[-9.485481,3.635985,8.989572,-2.733243,0.517466,-1.653721,-7.049099,-5.764298,3.391488,8.348478,-4.313633,-5.565711,2.534046],[8.755280,1.556486,-6.654367,-1.735814,9.180089,6.106977,3.480185,7.565863,-2.982265,-4.174493,-9.344543,0.751872,-4.662775],[3.925782,-1.163211,0.159658,-8.500263,4.580021,-1.211996,-8.486128,1.961782,8.515087,-3.338246,-8.863628,7.158930,5.209625],[-7.287295,7.167442,-9.444924,8.102944,6.527829,9.744598,7.678180,-1.743737,-0.202970,5.098028,7.266625,-5.050889,7.844002],[-2.966715,0.878283,8.125457,-0.605031,8.430515,1.918533,-1.468864,9.097177,-9.310725,-0.030071,-9.889783,2.504504,-3.971259],[-4.667239,-9.796947,3.600714,-1.275190,-9.971242,6.934920,-9.948588,-4.051262,7.467853,7.552853,-6.680195,-9.247525,-2.253692],[5.907371,-5.986688,-8.935849,-3.546270,2.482895,-4.985065,5.717715,6.088786,0.975045,6.123278,2.465880,-5.085305,0.905162],[5.434762,4.318235,-2.270912,8.964774,-2.708051,1.176150,4.676480,2.917256,4.565756,-8.766912,9.158180,-5.795563,2.461508],[3.422729,-4.880955,-6.143047,-5.813552,-7.198932,-6.595704,-9.271636,8.985087,-7.642205,-8.353029,-6.749590,-8.430996,-6.405012],[9.568175,-8.110115,-9.987192,-6.393954,-0.664155,-6.873804,6.320612,6.055639,2.350154,-5.919134,3.947382,1.746986,-2.639844],[4.991096,-7.774056,-6.511074,8.165655,2.379307,9.191678,-8.725244,-2.243245,-8.435420,5.517122,-2.283248,5.276665,-7.674635],[9.019905,-1.879007,1.969208,-9.783953,2.889236,9.235917,5.411035,0.735787,1.989225,-2.840487,-9.742935,2.360175,-5.889129],[-4.138427,-3.806132,-2.860593,-3.617606,-3.477868,2.036597,-2.754071,7.269340,5.134087,-0.708230,1.684414,-0.495267,7.409055]],[[1.250424,1.277547,-8.694479,2.836491,-5.639355,-1.970723,1.114328,-6.136295,9.997735,3.655696,2.285499,6.218062,9.907903],[9.186934,-3.566935,6.449316,2.678355,9.763402,-3.383038,-1.318559,6.195268,-7.132961,1.580865,0.797750,7.987626,-2.333602],[3.606205,-0.476428,-4.828976,-8.905880,-5.399898,-4.317048,-8.326497,-1.290562,4.196834,7.904890,7.954907,1.580934,9.069951],[-4.251789,4.123837,9.391435,-9.854574,-4.736113,0.329598,-7.096300,-1.011831,7.041194,-5.336702,0.208707,-3.692513,-9.611328],[-7.254267,7.240608,-3.287161,-8.400054,-9.961044,-8.713996,3.354429,9.381887,-7.994759,8.103009,5.512865,9.254283,-5.183347],[9.114597,-2.367851,-8.273035,1.823597,-4.195226,3.585140,4.444518,-7.259700,5.094892,-6.230480,-8.140041,-7.509335,1.912920],[-2.923752,8.212601,-9.443100,2.089358,6.026572,1.395021,8.518550,-8.367946,5.313718,-8.414343,-2.577886,1.847081,3.511660],[1.871490,3.219087,3.063750,7.945696,-7.331398,4.318558,-0.356305,-6.080926,2.162526,8.799441,-0.179855,3.115824,-9.196321],[-8.645710,6.817790,5.161487,2.084632,7.323873,-0.673755,-2.843128,-5.230396,4.034876,-8.921031,9.324872,7.164031,6.871910],[3.122514,7.284654,-7.212620,3.979268,0.028629,-1.739104,-4.527362,7.190445,7.102669,2.494954,4.320792,-5.824561,-7.420905],[6.589759,1.970982,-7.125190,8.244631,-7.093276,9.373664,0.489689,1.306787,-2.502712,-9.074817,-4.828034,0.399026,9.060015],[-6.879215,-7.955664,0.338804,8.061609,-6.372244,3.413802,4.379471,-7.299401,-0.875582,7.025956,1.279026,0.785908,1.450667],[1.209952,0.759672,9.220968,4.883320,7.494026,0.010445,0.696967,-5.822338,9.753172,-6.427493,-9.946371,-5.387375,-1.296714],[5.856134,9.491407,-7.745552,0.321854,5.604884,0.898936,-4.333646,-6.117147,5.141758,-5.408871,-6.096634,5.798120,1.635022]],[[0.443278,1.577311,7.616582,2.649022,8.828548,-0.652829,-9.353262,6.017791,-7.594195,-2.176109,2.385472,-8.625824,1.583398],[-0.220511,2.351214,-6.935483,8.011154,6.580679,9.992537,3.817794,-1.842300,0.278037,8.109448,-8.571724,5.886107,-6.321438],[5.282151,-9.770277,-3.975905,2.838357,-9.398017,-1.198818,-0.597043,-9.458482,6.100278,-1.342422,4.855608,-7.463699,3.767750],[-2.088600,5.151057,2.256688,2.353169,8.428922,-9.688322,-4.598662,-1.931291,-4.708434,-1.306895,-0.043903,-5.728591,7.696731],[0.683909,7.412476,-1.081849,2.744006,-3.557880,-5.493409,-0.841831,0.754117,0.300320,6.065224,9.580095,-3.574650,-8.219408],[1.144335,2.712774,6.881738,-0.428558,8.366172,-3.338136,-7.904403,-7.873784,9.838210,-2.503994,9.495284,-6.801961,9.709949],[8.794069,5.125644,6.540339,-9.137907,9.576127,8.148051,-7.699310,-4.128110,4.765628,-1.532241,-7.804500,-9.341238,-6.485731],[-7.782636,-0.933924,-8.560985,7.923043,0.529378,-8.055209,1.549953,5.773610,6.986049,-9.826447,5.716494,-5.835039,3.906464],[7.901270,1.004106,7.715266,-1.707168,-3.967043,0.648898,-3.768752,-7.828395,9.325427,-0.615906,-4.240624,-8.406371,7.485064],[-9.853209,3.512030,-3.305870,8.945144,4.530268,5.934631,-4.991808,-5.599441,4.264395,-5.609551,-4.178291,-1.441439,0.094852],[-3.484113,2.910892,5.632575,-8.482679,6.505609,4.009711,-1.834436,6.813618,-0.632574,5.644029,-9.313115,3.067481,-5.257883],[-5.508783,-9.245725,4.223349,7.851475,-4.802931,-2.130767,-0.554197,-3.565299,-1.200496,-8.638454,-1.954727,8.512768,3.178332],[3.681083,2.345530,-7.170524,-1.044475,6.874161,-8.990826,-7.816756,7.590592,3.268498,-6.890556,4.820275,-9.486068,-8.049596],[-5.877770,0.148745,8.797709,-9.993170,-7.169939,-8.473721,1.625265,6.087105,6.944142,-4.024008,-9.410096,-1.039907,7.207127]],[[-1.072910,5.035514,7.709389,-9.235443,0.482551,0.122529,-9.306345,7.075067,-5.268762,-9.220250,-4.583800,2.915269,-8.730605],[-1.696676,-1.815152,-5.913545,8.216235,1.903903,3.001452,0.535549,-6.988547,-8.413086,5.447244,1.150415,-2.763474,0.357579],[5.007615,-4.454908,-1.704209,-1.583513,-2.970956,7.914678,-6.177811,-7.208030,3.991764,1.585054,-2.940713,-0.662612,4.688820],[2.786268,-0.043663,-9.863605,7.664287,2.931294,9.248363,-0.135846,9.736852,4.922380,9.860378,3.823764,-6.529964,-4.084856],[6.743743,-0.815783,-2.646552,-8.291728,-3.229117,6.713966,3.031025,3.867857,-0.081329,9.384198,-9.701410,-7.435417,-7.574816],[-3.210068,-8.824773,-7.813051,4.357227,-3.747091,-9.390575,-3.516656,9.772446,2.697575,8.471534,6.621057,-8.955266,0.440193],[9.714909,-3.340354,1.323983,-1.611129,2.322935,9.506451,3.484077,6.443843,4.331244,-4.313652,7.673618,9.011464,9.453050],[-5.488821,5.235514,-8.086605,0.880642,1.053353,5.037342,-0.292817,-5.832588,8.907296,5.369348,8.878559,4.677305,2.426537],[1.965707,6.939029,5.644436,0.634885,8.246185,-4.445592,-0.309117,6.097631,2.678154,1.369910,-3.984093,-6.798843,9.296100],[-2.001523,8.619962,2.577547,-4.346710,1.611345,-2.953784,7.836683,-2.713323,7.647577,9.519861,-0.657590,-8.218719,-0.630573],[0.092014,4.055366,-5.590296,5.396156,9.154891,0.511375,5.411800,-8.727717,5.185959,5.336188,2.506588,-3.588126,0.516097],[6.787081,-7.519452,-1.646836,-5.008566,-4.255930,0.272115,0.639610,-1.394655,0.372835,2.468730,-8.703135,5.929368,1.890599],[-7.142911,3.091557,-0.827006,6.294876,-5.343196,-7.101555,8.124554,6.092541,-7.551630,-7.468151,1.563567,-9.874960,3.270095],[5.750955,-0.614016,0.549007,6.492100,2.883679,8.000952,-2.448190,-7.792802,6.054041,-6.455366,0.249798,1.685896,1.444621]],[[0.589979,5.325438,-3.114469,8.832864,5.009750,6.742266,0.639937,0.309395,-8.508450,-6.477895,-6.073289,-6.567472,-7.000127],[-6.357753,5.524050,9.967254,8.783231,6.862061,4.540468,7.507393,6.507166,0.821711,5.712394,-9.595667,0.307544,-7.618864],[-2.664152,-4.573702,-9.140379,-9.202851,-8.850748,-0.480095,-5.548039,-4.573679,-9.649179,9.650445,-7.236442,-9.427371,1.330608],[3.525505,4.678552,-7.994782,0.716128,1.486618,2.186364,9.509058,1.792269,-5.996074,-3.827475,8.086216,-6.054624,-3.364143],[-7.582630,-9.904880,0.259753,-3.768837,8.337704,-0.076491,2.172442,0.691006,2.928354,-6.611704,-2.193328,9.463831,6.684137],[-0.253598,2.127713,4.484224,1.580054,3.045983,9.640451,-1.991545,-0.099062,9.709818,-9.204655,5.885551,-6.963467,-8.186003],[-7.169177,1.806750,-3.748966,3.923758,-1.046020,6.929099,-3.399009,9.635861,-9.136203,-2.808574,-6.591969,-9.396349,-7.323530],[5.807516,-2.933611,-2.138171,7.491024,-0.717434,9.317673,1.767350,-3.351205,5.047131,5.179264,9.204903,-5.299550,-9.370081],[3.824106,2.593344,-8.047161,-1.814106,-2.176456,9.609243,-4.826036,-5.195940,9.390013,-8.967910,-1.999733,-3.980927,-4.359616],[-2.047525,-2.948423,8.770868,7.308825,2.872846,3.872141,-3.394802,-4.246246,6.982743,-2.093341,-3.565280,8.416825,7.583982],[8.626010,9.310093,1.199431,-2.580914,9.593243,-6.855142,8.450942,-2.596310,4.759491,-7.439128,9.531697,5.168251,4.592093],[9.540733,-2.913334,6.274679,6.177833,8.621430,-2.507512,-1.211195,3.727074,-6.541589,-4.808577,-3.046134,-9.824820,-8.317701],[-8.851055,6.436842,8.100870,1.135543,1.212754,1.829713,1.221609,-3.495207,8.464005,1.873492,0.142805,0.652287,0.337839],[9.498206,-1.429724,7.572438,9.005741,7.237223,4.584569,-9.309514,1.510659,0.582078,-0.560895,-2.980083,-6.326098,4.457633]],[[2.516729,-4.342476,-9.112685,-3.996947,2.804034,4.626854,-6.361146,4.665872,0.728503,5.354287,-3.057537,-5.864144,-9.395520],[-1.303322,-5.867668,-0.866711,-4.285622,-3.383858,-6.999911,4.992463,-4.964645,8.000922,1.408510,7.365664,-0.649137,2.282948],[4.677080,-5.491207,-1.298880,4.928476,-9.956717,6.106915,-5.230310,3.210277,-6.797561,-1.983738,0.111561,-5.731307,-0.215462],[-2.502817,-7.258433,7.801173,6.665819,4.322026,-0.456497,-9.041499,-4.326628,5.965997,-0.353138,7.182603,-5.657073,5.840369],[9.805594,-2.418546,4.769512,9.189732,6.531078,-9.490679,-8.297707,-2.808735,-7.574568,5.684479,-6.217373,5.388995,8.686651],[-4.642116,-4.018396,3.913907,2.335894,4.669314,-3.189412,-0.008075,-7.297142,-6.459462,-5.985043,2.145230,-9.252375,9.108500],[-2.151781,4.764796,7.007204,4.912319,8.842190,-4.362018,-1.571573,-2.643195,-4.038753,-1.440385,5.878046,9.606612,-7.270603],[-4.944574,5.868967,3.062119,-7.818849,9.607684,-1.757071,0.765690,5.244888,-8.193851,7.941337,1.282340,7.433891,-0.313129],[-6.065306,-4.188046,5.404387,6.801320,-9.819449,-5.338894,3.355393,2.035749,-6.294662,-6.448144,-1.018632,8.358683,7.088220],[5.248651,9.952542,1.206986,2.716724,-9.100518,-5.437546,6.038875,-3.236515,5.471792,1.514349,-7.759998,7.787232,0.766970],[9.255679,1.368204,6.929002,-8.201264,8.095653,5.780430,1.248186,8.377866,2.750551,3.273761,-4.054808,-7.949112,1.584637],[4.408492,9.432971,-2.530459,9.953615,0.851069,-0.293240,9.527524,3.349633,-8.572157,-1.946724,-7.632859,-9.145378,-7.533540],[-7.992406,-0.469172,8.539125,-9.271152,-0.185890,1.787242,-5.257894,3.419903,-7.774976,-8.946865,3.320446,7.795262,-2.593052],[8.652359,2.484606,3.435679,-6.905051,6.857368,3.794045,-3.492021,-6.363491,-6.652625,-5.022300,7.383089,-9.803823,-3.455051]],[[-6.698641,-3.488674,2.950148,7.969024,5.527352,-1.604284,-4.832194,2.304196,9.261470,9.271449,8.365322,4.890086,4.162140],[7.629253,-8.765648,8.278503,2.313659,-7.737964,-3.423085,2.311964,-4.427465,9.187796,1.171843,5.721024,5.486097,-1.066894],[-1.784779,-6.141610,-6.697131,5.885182,-6.579512,7.576628,-9.030065,-9.765147,7.875219,-8.641677,-1.408865,-6.453736,-8.134154],[-1.619072,-9.441895,8.461505,-6.303944,7.786988,7.119457,-7.493967,4.579786,6.299140,9.753780,-9.948968,6.712493,-0.120765],[0.519836,1.904208,-7.143799,5.553892,-5.444611,9.651636,-0.350694,3.843247,-2.030807,7.807956,1.396710,6.685491,6.686335],[2.086222,2.399704,-1.103254,-0.070136,-4.482578,0.449025,7.879883,-6.826220,4.210897,9.650069,-7.345489,-9.553254,-3.081509],[-2.948514,-8.397519,2.418851,-9.455717,2.122373,0.003972,-0.833656,0.570431,2.581191,6.961731,8.534222,4.426677,4.811600],[-7.585608,9.414305,4.608133,4.972670,1.935102,0.953001,6.196448,-2.947310,-8.830335,-9.410132,7.601635,1.270635,-2.051733],[3.526524,6.841817,5.595803,-4.659636,-1.134275,6.879489,0.762890,5.711336,-0.483834,5.250200,9.988989,-3.983729,3.719496],[-4.032986,-4.524780,-7.171951,-2.641892,0.659205,5.900506,-8.507619,6.445430,7.003650,7.057245,-1.612716,5.464554,-6.713032],[8.401808,3.632441,-1.297529,5.302094,-9.644431,-0.914812,-3.483879,-5.543259,8.660254,9.950064,-3.028492,8.991934,6.033214],[-6.085888,-2.930957,-3.396490,0.699368,-5.749427,4.702839,-0.474259,8.573419,-0.440775,-7.980967,-0.469150,1.437093,5.895917],[-1.074766,9.235587,-1.258174,8.679022,8.525760,-2.985732,3.096708,-7.831389,6.305858,-3.146507,-6.504572,-3.731930,3.460115],[-6.258125,-6.763419,1.211924,4.638609,3.340852,-0.419654,-3.113820,-8.616540,-1.878525,0.574428,-8.544606,3.635032,-6.871897]],[[1.463754,9.823891,2.791695,2.453612,7.590829,-8.106408,-6.349550,-4.561432,-0.776096,-1.068653,3.628444,-0.529512,8.768107],[0.697169,9.076360,-8.455532,-3.569576,-6.809369,-1.245422,-2.632615,-8.831266,-9.410201,-9.094405,1.478562,6.870974,9.663350],[-9.854866,3.144614,-5.671690,-4.887473,-6.604197,-7.676038,-0.241313,-8.351410,-1.052415,-9.634652,-0.170582,8.408849,5.757854],[6.527752,-1.820893,-8.253156,1.545805,2.074399,-6.323030,8.889003,-1.376574,-9.593181,-9.542580,3.744682,9.757727,0.682538],[-2.454689,-0.997581,0.669288,-1.427351,-3.474068,-3.957646,4.910187,7.894013,-8.803533,-8.024622,-6.777058,9.518368,-1.031107],[8.957917,7.821510,8.601933,-1.756574,6.753006,3.895949,3.379736,-9.955342,3.499583,9.829577,-6.973795,-5.179528,9.275837],[8.277993,6.433987,0.779420,3.614971,-9.083042,8.824691,-0.117575,-7.061801,-8.055917,6.040119,-1.049595,-6.639382,7.923310],[2.421383,-7.741014,-0.687850,9.513826,9.477875,-8.654345,2.609513,5.575045,9.003819,-9.098195,1.201624,-5.102719,0.471313],[-5.140904,-2.150512,-1.887951,1.772533,-7.446312,-1.788905,7.543799,2.284379,-7.359907,-9.293755,3.509221,6.533582,-9.989960],[-1.544115,3.106375,4.197192,-3.593118,8.694869,9.856090,0.140834,-3.788581,2.460116,4.368594,-6.901219,-2.508578,9.377710],[-2.067675,1.597636,7.868950,8.570170,8.852348,-5.906903,4.297356,3.332061,-3.037418,-0.043173,-5.560425,4.819638,-8.927541],[-4.115586,-3.643768,-3.337083,-5.093108,8.150779,-4.115862,1.126628,1.548006,6.418340,6.581739,2.404249,3.511721,2.699685],[-3.612256,3.589153,-7.162286,5.628775,3.961530,6.731383,8.852769,6.494014,-7.449104,2.226839,0.257301,-1.391021,1.356771],[-6.059108,0.855728,7.533840,-1.097659,0.557567,-5.231422,-8.030947,-5.764106,8.061889,-9.012957,3.640755,7.342743,6.256107]]], dtype = "float64")#candidate|2119|(10, 14, 13)|const|float64
bop_2120 = relay.logical_xor(call_2115.astype('uint32'), relay.reshape(const_2119.astype('uint32'), relay.shape_of(call_2115))) # shape=(10, 14, 13)
bop_2123 = relay.logical_xor(call_2116.astype('uint32'), relay.reshape(const_2119.astype('uint32'), relay.shape_of(call_2116))) # shape=(10, 14, 13)
uop_2137 = relay.asin(bop_2120.astype('float32')) # shape=(10, 14, 13)
uop_2139 = relay.asin(bop_2123.astype('float32')) # shape=(10, 14, 13)
uop_2161 = relay.acosh(const_2119.astype('float64')) # shape=(10, 14, 13)
bop_2164 = relay.maximum(uop_2161.astype('int32'), relay.reshape(bop_2120.astype('int32'), relay.shape_of(uop_2161))) # shape=(10, 14, 13)
bop_2167 = relay.maximum(uop_2161.astype('int32'), relay.reshape(bop_2123.astype('int32'), relay.shape_of(uop_2161))) # shape=(10, 14, 13)
func_286_call = mod.get_global_var('func_286')
func_289_call = mutated_mod.get_global_var('func_289')
var_2176 = relay.var("var_2176", dtype = "int32", shape = (126,))#candidate|2176|(126,)|var|int32
call_2175 = relay.TupleGetItem(func_286_call(relay.reshape(var_2176.astype('int32'), [6, 7, 3]), relay.reshape(var_2176.astype('int32'), [6, 7, 3]), ), 0)
call_2177 = relay.TupleGetItem(func_289_call(relay.reshape(var_2176.astype('int32'), [6, 7, 3]), relay.reshape(var_2176.astype('int32'), [6, 7, 3]), ), 0)
uop_2180 = relay.acos(bop_2164.astype('float64')) # shape=(10, 14, 13)
uop_2182 = relay.acos(bop_2167.astype('float64')) # shape=(10, 14, 13)
output = relay.Tuple([uop_2137,call_2175,var_2176,uop_2180,])
output2 = relay.Tuple([uop_2139,call_2177,var_2176,uop_2182,])
func_2188 = relay.Function([var_2176,], output)
mod['func_2188'] = func_2188
mod = relay.transform.InferType()(mod)
var_2189 = relay.var("var_2189", dtype = "int32", shape = (126,))#candidate|2189|(126,)|var|int32
output = func_2188(var_2189)
func_2190 = relay.Function([var_2189], output)
mutated_mod['func_2190'] = func_2190
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1300_call = mod.get_global_var('func_1300')
func_1302_call = mutated_mod.get_global_var('func_1302')
call_2195 = relay.TupleGetItem(func_1300_call(), 0)
call_2196 = relay.TupleGetItem(func_1302_call(), 0)
uop_2202 = relay.sigmoid(call_2195.astype('float64')) # shape=(10, 14, 13)
uop_2204 = relay.sigmoid(call_2196.astype('float64')) # shape=(10, 14, 13)
output = uop_2202
output2 = uop_2204
func_2212 = relay.Function([], output)
mod['func_2212'] = func_2212
mod = relay.transform.InferType()(mod)
mutated_mod['func_2212'] = func_2212
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2212_call = mutated_mod.get_global_var('func_2212')
call_2213 = func_2212_call()
output = call_2213
func_2214 = relay.Function([], output)
mutated_mod['func_2214'] = func_2214
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1066_call = mod.get_global_var('func_1066')
func_1068_call = mutated_mod.get_global_var('func_1068')
call_2282 = relay.TupleGetItem(func_1066_call(), 0)
call_2283 = relay.TupleGetItem(func_1068_call(), 0)
uop_2294 = relay.rsqrt(call_2282.astype('float32')) # shape=(10, 14, 13)
uop_2296 = relay.rsqrt(call_2283.astype('float32')) # shape=(10, 14, 13)
func_1744_call = mod.get_global_var('func_1744')
func_1746_call = mutated_mod.get_global_var('func_1746')
call_2300 = relay.TupleGetItem(func_1744_call(relay.reshape(call_2282.astype('float64'), [10, 14, 13])), 2)
call_2301 = relay.TupleGetItem(func_1746_call(relay.reshape(call_2282.astype('float64'), [10, 14, 13])), 2)
var_2307 = relay.var("var_2307", dtype = "float32", shape = (10, 14, 13))#candidate|2307|(10, 14, 13)|var|float32
bop_2308 = relay.greater(uop_2294.astype('bool'), relay.reshape(var_2307.astype('bool'), relay.shape_of(uop_2294))) # shape=(10, 14, 13)
bop_2311 = relay.greater(uop_2296.astype('bool'), relay.reshape(var_2307.astype('bool'), relay.shape_of(uop_2296))) # shape=(10, 14, 13)
output = relay.Tuple([call_2300,bop_2308,])
output2 = relay.Tuple([call_2301,bop_2311,])
func_2313 = relay.Function([var_2307,], output)
mod['func_2313'] = func_2313
mod = relay.transform.InferType()(mod)
mutated_mod['func_2313'] = func_2313
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2314 = relay.var("var_2314", dtype = "float32", shape = (10, 14, 13))#candidate|2314|(10, 14, 13)|var|float32
func_2313_call = mutated_mod.get_global_var('func_2313')
call_2315 = func_2313_call(var_2314)
output = call_2315
func_2316 = relay.Function([var_2314], output)
mutated_mod['func_2316'] = func_2316
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1300_call = mod.get_global_var('func_1300')
func_1302_call = mutated_mod.get_global_var('func_1302')
call_2318 = relay.TupleGetItem(func_1300_call(), 0)
call_2319 = relay.TupleGetItem(func_1302_call(), 0)
output = relay.Tuple([call_2318,])
output2 = relay.Tuple([call_2319,])
func_2324 = relay.Function([], output)
mod['func_2324'] = func_2324
mod = relay.transform.InferType()(mod)
mutated_mod['func_2324'] = func_2324
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2324_call = mutated_mod.get_global_var('func_2324')
call_2325 = func_2324_call()
output = call_2325
func_2326 = relay.Function([], output)
mutated_mod['func_2326'] = func_2326
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1188_call = mod.get_global_var('func_1188')
func_1190_call = mutated_mod.get_global_var('func_1190')
call_2350 = func_1188_call()
call_2351 = func_1188_call()
output = call_2350
output2 = call_2351
func_2359 = relay.Function([], output)
mod['func_2359'] = func_2359
mod = relay.transform.InferType()(mod)
output = func_2359()
func_2360 = relay.Function([], output)
mutated_mod['func_2360'] = func_2360
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1120_call = mod.get_global_var('func_1120')
func_1122_call = mutated_mod.get_global_var('func_1122')
call_2396 = relay.TupleGetItem(func_1120_call(), 0)
call_2397 = relay.TupleGetItem(func_1122_call(), 0)
output = relay.Tuple([call_2396,])
output2 = relay.Tuple([call_2397,])
func_2407 = relay.Function([], output)
mod['func_2407'] = func_2407
mod = relay.transform.InferType()(mod)
mutated_mod['func_2407'] = func_2407
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2407_call = mutated_mod.get_global_var('func_2407')
call_2408 = func_2407_call()
output = call_2408
func_2409 = relay.Function([], output)
mutated_mod['func_2409'] = func_2409
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2537 = relay.var("var_2537", dtype = "float64", shape = (3, 7, 15))#candidate|2537|(3, 7, 15)|var|float64
uop_2538 = relay.atan(var_2537.astype('float64')) # shape=(3, 7, 15)
var_2540 = relay.var("var_2540", dtype = "float64", shape = (3, 7, 15))#candidate|2540|(3, 7, 15)|var|float64
bop_2541 = relay.less_equal(var_2537.astype('bool'), relay.reshape(var_2540.astype('bool'), relay.shape_of(var_2537))) # shape=(3, 7, 15)
output = relay.Tuple([uop_2538,bop_2541,])
output2 = relay.Tuple([uop_2538,bop_2541,])
func_2544 = relay.Function([var_2537,var_2540,], output)
mod['func_2544'] = func_2544
mod = relay.transform.InferType()(mod)
var_2545 = relay.var("var_2545", dtype = "float64", shape = (3, 7, 15))#candidate|2545|(3, 7, 15)|var|float64
var_2546 = relay.var("var_2546", dtype = "float64", shape = (3, 7, 15))#candidate|2546|(3, 7, 15)|var|float64
output = func_2544(var_2545,var_2546,)
func_2547 = relay.Function([var_2545,var_2546,], output)
mutated_mod['func_2547'] = func_2547
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2551 = relay.const([[[8.792967,-6.804959,1.813462,-7.881716],[5.950989,-3.473185,-9.964273,4.339481],[-9.363466,-9.939673,-4.156448,-0.552380]],[[-3.925698,6.814551,0.790827,1.171785],[5.919620,-2.064020,-5.971640,-4.300184],[-6.541125,-9.558840,0.022800,0.098852]],[[-9.883162,-4.454969,8.626678,9.148185],[1.275646,-7.998360,2.641469,1.069900],[-7.324374,6.349160,3.494297,-2.605280]],[[-0.429471,-6.346257,-1.338874,-6.662901],[7.835620,8.573504,3.458846,1.922761],[-3.061401,-8.720530,4.750718,-3.670615]],[[0.384047,-1.894152,6.625886,7.129982],[1.591634,5.481957,2.059724,5.081154],[0.205988,2.097974,2.219395,7.567882]],[[7.265630,7.208606,6.398887,-0.917524],[-5.447081,6.377022,7.152127,8.320521],[5.745444,-8.313504,-8.929964,3.166080]],[[-3.647573,3.749094,8.070837,1.294426],[-9.671693,9.734684,-3.564099,-3.938121],[2.161023,0.974661,-7.825932,3.201297]],[[1.975963,2.274626,9.023628,5.584198],[7.950120,4.656181,2.096672,4.101147],[-0.510937,-5.523442,-4.198327,7.127203]],[[-6.372501,-1.791381,5.772496,-5.972546],[1.615509,1.635821,0.867494,9.632661],[4.882999,0.122232,1.089969,-1.257450]]], dtype = "float32")#candidate|2551|(9, 3, 4)|const|float32
var_2552 = relay.var("var_2552", dtype = "float32", shape = (9, 3, 4))#candidate|2552|(9, 3, 4)|var|float32
bop_2553 = relay.floor_mod(const_2551.astype('float32'), relay.reshape(var_2552.astype('float32'), relay.shape_of(const_2551))) # shape=(9, 3, 4)
const_2556 = relay.const([[[1.925656,6.379412,-0.441773,9.193808],[7.942338,-5.523021,-6.901247,-4.031301],[4.175183,6.865981,-5.270321,4.871350]],[[8.645627,3.571339,-2.911540,2.995495],[0.409320,-4.021773,7.622112,2.218688],[6.661610,-2.187805,-1.804957,-8.146689]],[[-4.823845,-4.106725,3.070827,-1.009178],[-8.835365,-1.981521,-0.713516,-7.776474],[-5.983039,3.096551,3.998243,1.194154]],[[2.044555,-4.993416,-2.001086,8.773105],[-6.431887,-6.235059,1.765412,-6.799016],[-2.431966,8.096573,4.140603,-7.567842]],[[-0.428247,8.983988,-6.479588,-0.138031],[-2.354556,3.531858,8.221082,0.155338],[-0.972001,4.957634,-2.102824,-7.513564]],[[1.668785,-4.851999,1.103435,-4.732987],[-4.392892,1.668021,-5.046672,-6.254316],[-9.735372,-3.636572,0.219335,-5.905427]],[[6.147078,3.032168,2.933152,-6.473171],[8.582905,0.385834,6.232448,3.542493],[-6.447184,-8.050193,-7.456098,9.687143]],[[-7.773857,3.015966,-9.320650,6.948996],[5.370359,3.538303,-6.350788,4.152361],[-7.102064,3.939538,0.885438,-3.631196]],[[1.681931,-5.304893,5.001982,5.618204],[7.239262,0.317433,-8.469794,6.801324],[-3.341758,-4.813136,-8.430881,-5.944207]]], dtype = "float32")#candidate|2556|(9, 3, 4)|const|float32
bop_2557 = relay.equal(const_2551.astype('bool'), relay.reshape(const_2556.astype('bool'), relay.shape_of(const_2551))) # shape=(9, 3, 4)
func_2188_call = mod.get_global_var('func_2188')
func_2190_call = mutated_mod.get_global_var('func_2190')
const_2567 = relay.const([[4,-2,1,8,6,9],[-9,3,-6,2,7,-7],[-1,9,-8,-8,5,9],[-10,1,3,9,-4,-8],[9,4,-3,-7,1,6],[10,-10,-3,-10,-6,-10],[2,-10,6,-7,-2,-2],[-1,1,-4,-9,-10,1],[10,8,-6,-6,2,7],[6,2,6,-2,3,-8],[10,-3,-8,4,10,5],[-2,4,-9,-1,-4,2],[7,6,-7,8,4,6],[8,2,-3,1,8,-7],[-6,-1,-1,10,-8,9],[3,-3,-9,-8,10,-2],[-7,-8,10,-1,6,-1],[-6,5,9,9,1,8],[-2,4,4,-7,-3,-5],[10,3,9,-3,5,7],[3,-6,8,2,-8,-4]], dtype = "int32")#candidate|2567|(21, 6)|const|int32
call_2566 = relay.TupleGetItem(func_2188_call(relay.reshape(const_2567.astype('int32'), [126,])), 3)
call_2568 = relay.TupleGetItem(func_2190_call(relay.reshape(const_2567.astype('int32'), [126,])), 3)
output = relay.Tuple([bop_2553,bop_2557,call_2566,const_2567,])
output2 = relay.Tuple([bop_2553,bop_2557,call_2568,const_2567,])
func_2578 = relay.Function([var_2552,], output)
mod['func_2578'] = func_2578
mod = relay.transform.InferType()(mod)
var_2579 = relay.var("var_2579", dtype = "float32", shape = (9, 3, 4))#candidate|2579|(9, 3, 4)|var|float32
output = func_2578(var_2579)
func_2580 = relay.Function([var_2579], output)
mutated_mod['func_2580'] = func_2580
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1216_call = mod.get_global_var('func_1216')
func_1217_call = mutated_mod.get_global_var('func_1217')
call_2584 = relay.TupleGetItem(func_1216_call(), 0)
call_2585 = relay.TupleGetItem(func_1217_call(), 0)
const_2594 = relay.const([[[-1.040647,-1.219387,-1.272205,-8.611339,-3.019467,-6.707791,6.641303,3.343413,8.257141,0.443428,2.339201,0.743800,9.821577],[2.305945,8.336113,-4.851674,-3.151074,7.892120,0.143414,-9.302629,4.616078,7.290853,-2.751657,-7.017849,5.169890,-5.766217],[0.243539,-4.906184,8.785022,-0.571558,-0.116100,-9.002855,7.732778,-5.633991,5.545945,4.003565,9.506290,4.244005,0.783202],[1.479946,0.625704,5.267782,8.270991,2.486091,2.895623,8.094008,1.742055,-3.612328,2.720844,7.829207,9.976392,-1.634797],[8.162557,-2.580256,3.983859,6.626831,-6.443066,-0.034354,3.557459,-3.944913,3.454161,-0.635130,0.073958,8.729025,4.794036],[1.828298,8.089168,-4.487964,-3.940959,8.704026,-7.546067,-2.803739,4.974478,6.036773,9.022471,-3.421509,9.105921,1.628173],[2.567927,-3.259883,0.054648,-7.413384,1.291872,6.774988,3.044506,7.694741,8.924500,-7.784072,-5.941331,9.841817,1.237655],[-1.361066,3.890842,2.665890,8.011476,8.206130,-4.858327,7.951153,-4.883841,7.312281,-0.736385,-2.039199,-6.525585,-1.229964],[-1.668337,-3.277199,4.110228,-8.279125,-0.621005,-2.096255,0.111851,-0.077484,6.725661,1.305460,-0.521316,2.221274,-3.689113],[9.866264,1.222545,0.708295,3.339030,7.094643,0.907387,4.512697,-5.589893,7.427783,-2.768131,8.393640,3.378805,5.106961],[0.602426,-6.713373,-0.412056,-8.635370,-7.317651,4.029401,-8.237593,-0.288936,8.129739,1.450392,4.103357,4.645683,6.944225],[3.984352,-8.225643,-9.111997,-2.398330,4.662748,-0.911662,-1.493841,4.034255,5.916511,-8.665792,1.707097,3.675463,3.306636],[5.813891,-6.190539,0.375073,-8.220402,8.020133,7.138988,1.644134,-0.457206,3.482841,-6.734802,9.436417,-9.062922,-6.402323],[9.804583,-6.976096,-6.994363,3.221288,-1.372859,0.497717,-7.746129,-1.392250,-7.652464,-6.142637,5.069538,9.643383,9.651898]],[[7.771031,-4.979726,4.410878,-6.698646,9.715012,-9.362819,9.294051,4.161668,2.354438,1.304868,-8.933698,8.510988,4.489850],[-1.960325,4.992657,1.639858,8.969752,-8.500243,8.333514,-7.556786,3.748093,5.576339,-5.849550,0.550686,9.397699,2.370200],[-7.955666,-9.715166,6.494555,-3.040890,-4.705435,-6.665329,-3.242453,7.803585,4.426332,-9.106552,-8.128230,8.830976,-9.891377],[-3.817885,-1.370174,8.307128,-5.731444,-8.095247,-8.828053,-4.612945,-8.197875,-9.054306,7.984076,-2.882841,-2.910949,-2.015305],[-0.956518,3.662385,-8.894507,-4.049663,4.282822,-8.232927,-4.527801,8.464760,9.195438,3.352292,-1.970829,-0.890269,0.773789],[-6.676042,2.162587,-4.246643,5.962002,7.162280,1.123334,-7.972837,2.809072,3.301416,6.503007,6.962960,-2.095517,-4.364068],[-3.950306,7.673435,1.079782,7.191901,-7.892555,-0.560444,3.370399,4.082588,-7.488497,6.376879,-6.713480,9.217861,-8.932742],[8.555330,6.861793,1.509392,-2.152128,-0.877525,6.872104,5.620933,8.430684,1.762498,2.068179,-2.330320,-0.663290,2.858571],[-4.744633,-5.119747,0.395973,0.722898,1.332995,3.050393,3.846791,2.703512,6.634862,-3.411851,-1.543578,-6.421031,5.430951],[4.366820,-9.073621,-3.015271,5.265703,6.140231,-5.720403,-3.674496,-1.972785,-5.940767,9.173021,-9.716603,-0.240384,1.061945],[-9.781718,-7.002380,-4.862451,5.092015,-3.991716,9.231514,-7.423106,7.471931,-8.246139,-9.150322,6.214796,-2.429227,-8.917828],[5.710090,-9.720409,9.641937,-7.578454,-2.731016,-0.704565,-2.562346,0.126907,-1.697274,-0.018518,6.835385,4.476678,0.708974],[-1.634299,3.578348,-2.951933,9.130296,-7.035813,3.537215,-0.285574,5.271012,8.991717,5.999129,-3.626483,-4.656938,4.816652],[7.373241,0.067568,7.198204,-3.679546,-3.347917,-6.728525,4.691040,3.435566,4.366509,-7.248599,-5.446359,-1.334286,1.062308]],[[3.400865,-7.303230,2.104102,-1.143317,-6.278637,-7.236030,-3.438122,-2.851896,-9.017996,8.782102,-7.718729,1.050286,-9.394465],[2.976924,5.276571,4.434061,-1.151753,-3.117035,9.695273,1.585225,-5.942683,-8.199281,-0.850631,5.910331,3.069292,-3.063032],[-6.469256,-5.314383,1.923901,5.152919,-0.940163,-5.453708,-9.290024,-7.203194,9.004809,-4.577929,3.315071,-1.364309,4.112180],[-8.937910,1.118247,-0.825944,-1.462422,-3.818701,-3.303454,2.913089,-2.495335,-5.425267,-9.654568,-4.135836,-4.376873,5.245730],[9.754763,6.695394,-6.999882,3.624000,8.782824,8.361899,3.950704,0.462185,1.911372,-0.883341,-4.757103,5.870574,-4.765884],[-0.630573,-1.003674,-6.138806,-4.574705,-6.430640,-0.657701,-4.534893,0.734703,2.785839,8.601293,7.903518,0.719066,-2.644564],[-0.300631,-8.516219,2.443806,5.102149,8.639036,7.658882,5.244998,-8.532939,-5.989951,9.899480,-0.835248,-0.164497,-8.665148],[-4.085961,7.512590,5.269966,-2.235290,-1.097596,4.548869,8.689127,-4.701470,-6.041749,-9.730515,9.728057,7.752822,2.264523],[4.583788,6.838053,4.482729,-8.887784,-5.887298,-8.236118,4.621001,-5.951822,-2.124228,6.971523,-0.059628,-9.402229,-4.753366],[6.364302,5.504133,8.307990,-4.393643,-5.612922,0.676230,5.168267,-5.852645,-7.309072,-9.982823,-1.744025,8.692783,7.889785],[3.634360,-6.476230,7.418680,1.559000,-9.702845,-9.378006,4.585962,-5.930006,2.105894,-9.191611,8.735294,6.838826,1.081128],[-1.362876,-9.675386,3.545550,-2.439436,0.726644,2.804794,-3.525552,-8.622387,1.470317,2.564971,-7.450321,9.999748,-5.945865],[0.663731,-8.641001,-2.944727,3.430620,7.074969,-3.341918,3.465820,2.044242,0.183421,-0.503834,-3.131768,6.653996,-9.486142],[-4.810984,5.291532,-3.974055,9.410354,1.302423,-4.555857,-0.959270,5.464289,6.323579,-6.942578,-7.182729,-8.355404,8.602738]],[[-3.491346,-3.214489,-8.595784,-6.199317,2.253823,5.009606,9.255250,-0.029087,7.244281,9.245098,-0.457886,9.061548,-5.812423],[-5.633333,1.559454,9.813610,-6.926593,-3.400882,7.558249,-4.998904,4.481366,0.779072,8.507546,-4.098342,-7.761353,6.251508],[-1.583390,0.839018,-1.965015,0.776998,-4.045300,7.336944,-9.451415,2.694050,-8.067278,7.096408,0.630939,9.316344,-2.049314],[-7.979935,6.954186,1.417391,-7.133616,-4.043737,-2.607294,-0.711897,6.177602,-4.480598,3.342189,1.118783,3.078590,-8.148343],[5.223183,1.237287,1.225692,-0.517299,-4.966201,3.086225,-1.944501,2.248724,4.973052,5.222260,-0.415020,7.473679,-4.637743],[9.108591,5.095302,-5.687639,5.533053,-1.776186,2.448254,-6.777796,9.689726,5.351505,6.954190,-5.324191,-8.162750,2.688120],[7.181986,7.384207,4.302639,-2.261314,-4.679377,0.566195,-0.232184,-5.481974,-4.558471,4.818180,-6.948504,-2.813824,-5.135053],[9.470931,-6.873901,1.398891,7.767834,3.808573,2.658206,4.925167,2.026125,-7.024164,-2.311446,6.780761,3.217636,-7.836111],[9.667482,4.572150,-8.089117,4.177366,-1.094844,-6.788652,9.235248,-1.971630,2.001468,-3.838994,5.562999,6.885180,6.599612],[-6.954777,6.370762,3.416311,7.311814,-4.517741,2.727212,5.745962,-9.424844,2.810774,3.013206,2.184392,3.252526,0.764924],[-6.224138,-6.519323,-3.487707,-6.904897,-2.279170,-6.722989,-7.684336,1.252722,-5.947119,5.708917,-9.331065,-9.589642,7.192720],[4.892146,6.943732,2.414894,3.667112,-1.720087,-0.224751,1.942739,-5.081662,5.207378,5.149348,-1.893512,9.055761,-1.052719],[-3.989979,2.448569,-4.596933,-5.556887,-8.660908,5.564225,2.422749,4.406526,-2.860575,-5.737663,-2.546739,-7.054127,-0.521439],[-6.227308,-2.020350,-9.835636,5.458892,-3.708283,-6.050222,-9.934244,-0.505909,-3.345711,8.520883,-3.753713,-4.775083,-6.829198]],[[-5.491289,-8.470995,9.644482,-6.729224,-9.697569,-0.112565,-0.276901,4.154425,3.775826,8.201297,-3.719361,5.647531,9.343653],[1.295629,9.057878,9.061827,-6.066655,-6.370032,-4.134409,-8.340071,2.183725,-4.317095,9.038051,-5.720578,6.072041,3.778996],[5.227196,0.458618,-3.304039,3.134330,-2.197518,8.105092,-9.106529,-7.299161,-2.968566,1.438977,0.451790,2.246720,-5.564694],[5.255145,-6.238728,8.303789,-7.653561,-3.341403,2.926656,-9.390333,-5.727868,8.800844,1.104875,0.085672,-9.688053,-8.557648],[6.882290,-1.410712,0.452350,4.883794,-4.304589,-0.821087,-7.339426,8.876877,-0.276890,8.248377,9.068565,7.143044,3.328685],[-8.008458,-7.913307,8.863967,0.128043,9.933199,-0.934081,-1.657943,7.362321,4.183052,0.199559,3.553828,-6.801964,3.361214],[6.521384,-9.807588,5.580521,-2.269942,4.246482,9.633521,-3.312341,-0.258148,-4.258188,1.876980,5.503369,1.258573,-5.871249],[-3.048179,7.563824,-5.618902,-5.159825,4.461760,-7.101778,0.078729,-4.410348,-4.827400,2.494745,7.412564,6.498271,6.370286],[5.478249,9.482990,-3.511617,-3.583307,9.030828,-1.432782,4.508999,-0.776343,-9.673175,-0.567138,-1.866131,8.498541,5.294775],[8.245331,9.177786,1.395238,9.303334,-2.516388,-4.585387,-3.003174,-6.274063,6.567383,-4.598246,4.938022,-7.112090,9.528487],[-0.860324,-1.589386,9.581809,-4.688647,7.919855,3.278156,-2.328767,-4.962635,-5.092905,6.267306,7.542869,0.043214,-7.033748],[-9.130439,-3.469085,8.056594,-7.095258,-2.045071,-4.953965,0.526918,-2.647462,-2.766224,-8.445663,7.583866,2.334469,9.697395],[7.724772,5.516461,3.950653,-1.598555,0.963012,-0.263145,-2.566533,-7.750119,0.341567,-9.659033,-1.911859,4.045127,3.909701],[-3.651593,2.551724,9.487124,-0.850279,-0.507468,7.344456,1.546306,-7.666708,-7.700521,-7.783621,0.617650,-1.668203,0.911508]],[[8.775868,-7.815611,2.357501,6.270158,-5.026925,0.537360,7.225861,7.591364,4.455525,-2.897522,-2.603301,-9.659004,7.254778],[8.173728,0.416169,-4.203975,6.996428,8.373262,9.371378,4.056002,0.067672,-0.728610,-7.946760,7.431216,-3.250751,8.229876],[7.196692,7.388706,-4.071952,-3.485011,7.433896,-9.618231,9.810705,9.695846,-5.175988,0.282619,-7.814365,5.358860,7.073740],[-2.165810,-2.565189,-3.760413,9.576047,-6.057311,-2.782909,0.430787,2.013745,-3.394700,2.724275,-0.203365,-0.227739,0.564659],[5.833363,5.912129,-8.128250,9.198696,-5.999559,-9.167612,7.870547,1.275082,2.635305,-7.549379,-5.772557,-4.987415,-3.794397],[2.178560,-0.073678,8.369003,4.752322,-5.354097,-7.870130,-4.874953,5.185753,-3.197778,9.183428,6.525604,-7.327101,-9.781558],[-1.525566,-1.702244,8.497394,-0.215655,9.406793,7.799806,-8.564003,-4.740339,0.150778,1.121346,1.318241,-5.778644,3.874048],[7.255152,2.452403,-4.167909,-7.530617,-3.873711,2.362685,3.636198,9.235154,0.387018,-5.001166,-8.953432,7.293740,6.996944],[-2.049973,6.999532,7.190850,5.466003,-5.602000,-6.495216,7.361748,-1.753242,3.062197,5.900045,1.723412,1.656921,-5.394025],[8.464685,6.287037,-4.134835,-6.747572,-1.702755,-2.555326,-7.786960,7.836011,-9.337265,-6.247388,2.409667,-8.508752,-9.789106],[-3.906575,-3.835756,2.320550,-7.407285,-1.258413,-1.291884,-1.794049,-9.690359,0.432198,-7.299486,3.571147,6.295640,7.466574],[-3.247969,8.252222,6.586164,-7.913264,-9.615605,-0.519296,-8.849549,8.411203,5.698718,6.741888,-8.184980,6.104551,-8.924617],[5.197610,-7.245394,-4.239383,2.213510,4.414852,5.935741,-4.699246,1.142776,-7.323033,0.911879,0.915760,-2.883782,-4.299704],[5.469887,5.111765,-0.858014,2.862208,0.107634,1.789372,3.205772,-2.956041,-3.948653,-8.113634,6.324308,-8.316645,-4.766652]],[[1.285610,-5.877062,0.186160,9.642066,8.572193,-9.340464,-1.798138,6.727548,-7.054621,-6.405262,5.392546,8.388440,2.633912],[9.802643,4.379737,2.219422,-4.747823,-1.690264,4.916484,-7.729815,4.478682,8.093075,-1.269898,-5.848264,0.124104,6.318162],[5.654806,-7.080549,6.514213,-2.673189,5.323967,-5.551108,-3.512346,9.779870,-9.422065,-0.531918,-3.803249,-5.534880,-4.512228],[7.365651,1.753458,6.424092,4.618517,9.132693,9.900841,9.415196,6.315000,-6.148812,-5.241292,9.907205,2.509865,9.805875],[5.627186,-6.735659,-1.729325,1.553939,3.576055,-4.637952,-9.411380,6.739726,-5.888873,-4.055684,-5.691923,1.175044,6.267801],[-0.414702,-1.888074,-3.315978,3.167056,-8.932438,1.988483,6.783943,-2.195827,2.402303,-9.065493,-4.977858,-8.758049,-6.345892],[0.737799,7.129282,7.614443,6.672260,0.934728,9.689966,-0.339445,-1.663997,-1.872840,-4.811689,-3.883125,3.745579,1.431756],[5.719976,1.046903,-0.440750,4.076410,7.009800,7.988570,-3.893395,-7.821532,8.286695,5.138387,-8.733588,-4.620567,-0.377091],[0.013928,1.409478,3.894068,-2.096449,-1.252884,5.020777,-8.433018,-2.067578,9.122396,1.795987,5.180766,1.707175,-1.036952],[-5.806427,-8.549718,2.678673,-6.387420,-9.667125,9.983620,-1.818671,-0.819560,7.391613,-5.366911,-7.523094,3.088242,-0.252275],[7.999395,2.589205,6.263587,-3.802362,5.396549,7.651051,-0.559038,6.067580,-5.947273,4.281332,-2.055126,-3.191850,6.809333],[-3.290086,-0.930201,5.534215,-9.884331,0.518170,-1.774846,-6.605866,-0.980174,1.046052,6.127689,-8.452583,7.745731,-4.893779],[1.449228,-6.366709,-6.310464,6.612986,2.678601,-3.293355,3.373369,-7.151747,6.574802,0.878575,-5.914840,-9.474237,-5.180362],[-0.288586,-5.779160,1.487127,9.634075,-7.628854,-4.840184,-2.265057,-4.629824,-0.559005,-8.799092,3.383503,7.813490,0.106582]],[[-5.586422,7.200597,0.585117,-1.895064,3.903903,8.442468,1.654219,-1.872420,6.280494,-5.152201,4.874983,3.358842,9.849612],[2.282764,-5.417506,-1.074690,-7.138834,1.965994,5.122312,5.468840,8.348943,4.403330,8.634732,-2.280858,-8.697788,-6.674819],[5.818604,-5.007352,8.808925,1.580431,-4.706059,-8.688730,-6.544821,-3.486007,7.334407,-0.650225,-9.289459,9.641565,0.770296],[-4.416990,-7.021787,8.499984,9.427655,-2.944652,0.152163,-0.479705,-8.774077,-7.984659,-1.798611,-8.167595,-2.941061,-1.451469],[3.365753,-9.042298,6.366773,-2.480478,-6.502923,-1.803751,4.863424,-2.643209,-8.462226,5.741879,7.104139,9.172529,-0.523303],[8.709646,-8.088476,-3.523846,4.588838,-2.736647,8.938384,9.476807,-6.801854,9.061527,-7.013608,-1.380837,-6.814293,9.364639],[3.075082,0.445512,9.541755,8.112818,-1.324628,9.991703,-0.011244,4.359727,-7.209557,7.404537,-4.472039,2.276520,-1.681345],[2.109008,6.729834,-9.103541,-0.500609,-9.857610,-2.972768,8.754916,6.413091,1.874383,0.125082,-7.600963,4.161329,-4.015172],[-6.054428,-4.608798,-1.044727,-1.751900,7.708498,-0.553065,-7.245719,5.418627,-6.437644,-0.763954,2.506815,-8.718790,-1.345505],[-2.455291,-0.637959,0.981063,-1.263573,-5.955905,8.763505,-4.425234,6.740080,-4.897325,-9.343954,2.791837,6.176445,-6.397530],[0.547940,4.528114,0.405819,8.971036,-2.123882,5.479780,-2.598839,9.678913,-4.346854,-7.961556,8.125386,1.224972,-6.668040],[-9.431791,-9.157976,-0.115809,4.681681,6.642585,-7.961328,7.476674,2.746784,0.535182,-8.120739,-6.366077,3.726133,-9.507535],[2.753967,-3.209316,-5.097121,6.913691,3.394066,-3.282056,9.748280,-9.719731,-6.861458,4.042207,-8.525012,-4.609380,8.808271],[7.698551,8.576073,0.875787,0.718213,6.512133,3.919440,6.011736,-7.958649,2.724887,8.605865,3.788845,4.977418,-5.184702]],[[-5.611176,-7.809972,1.370047,-0.125205,-7.920052,9.549940,9.632046,8.039390,-5.775460,0.736564,7.460942,-3.041895,-6.780108],[-2.162578,-3.926318,6.762679,2.590880,5.772891,7.392137,-8.269218,3.924170,-1.788735,-2.136204,7.086783,-7.238893,2.807220],[-6.204128,-1.850736,-7.616424,-9.933879,3.424676,1.231529,-2.579357,1.581379,-8.898102,0.386136,-7.644855,-7.352303,0.489859],[8.976940,-8.342596,0.675820,-3.177870,-8.115513,1.360624,-4.786338,-0.093861,3.883864,-2.271351,8.915698,-5.136040,-0.579062],[-4.201200,0.603679,3.846881,3.515842,-9.919797,-9.676778,-6.929681,0.271424,1.133995,8.230725,9.069938,-7.716466,1.086828],[-8.599050,-5.951265,-9.172220,4.442777,1.734747,-2.497853,-3.028814,4.347123,-9.951421,1.331015,4.927384,8.278992,7.781682],[-6.947376,-0.246728,3.497657,3.371962,5.342696,-4.395453,-9.895477,9.941926,-0.970417,3.312568,-7.725411,2.925994,4.887337],[9.038966,4.573322,4.528190,-8.156674,-7.913336,-0.238485,-7.487707,8.807064,-6.572790,-8.057835,5.520043,2.054458,-5.979241],[-0.590056,-0.949836,2.988316,-9.492329,-2.961333,-0.363878,8.663957,-4.506064,-5.448142,0.767052,3.755473,6.276452,-1.084297],[-6.673417,6.397673,5.613164,-8.061805,6.645556,7.525560,4.481269,5.280088,2.782545,-8.517711,-9.549817,-6.879424,-1.456523],[9.999012,7.717628,-3.377515,-5.655628,-6.727159,2.440658,1.716038,-5.772796,-3.879206,-0.311724,7.251004,-0.302661,3.287936],[2.901089,7.635594,4.507603,3.455692,-6.602043,-8.961679,-2.875075,-0.875661,1.280939,-8.927817,3.411479,4.925201,7.738511],[7.318940,-2.564113,-0.197566,-7.162571,-2.542833,1.417973,-1.195023,4.747260,-4.164358,1.311766,-9.681397,-8.952663,6.248417],[2.042834,3.750487,6.765589,0.803047,8.539062,3.916699,1.371054,2.331574,-8.472226,-9.325680,-5.615619,2.222758,1.394039]],[[-9.814265,-4.979191,7.807343,0.966263,-2.460348,7.728700,-8.006123,-9.752162,-3.590147,5.299148,-7.481694,4.283256,-7.646612],[5.753902,-4.178824,8.043028,-3.572599,-8.732438,0.931332,-0.395176,-6.347352,9.834492,-6.742368,9.786321,4.169396,-7.995655],[-0.069433,-0.569157,9.167744,-2.386914,0.261021,-1.306908,2.177655,3.335223,-2.848830,9.253341,-7.344067,-1.157059,-5.743374],[1.681079,-5.843905,1.231617,-9.235979,2.430468,9.326987,7.584208,2.433529,-0.647148,-2.762775,-0.508228,9.627143,6.156102],[-5.565727,-3.006221,3.237086,6.545761,0.406729,-9.548004,-8.423835,0.491463,2.002729,-5.187091,-3.409874,-2.332643,4.641314],[-4.846262,-0.744731,-5.780617,5.173641,3.092914,-4.232035,-0.994765,5.348417,2.084022,1.472743,8.400738,1.012361,3.122912],[-3.869721,-2.985297,-0.522638,-7.140113,6.018218,-9.539405,8.615262,1.592188,-3.513437,9.767186,1.459767,6.474061,0.319551],[1.771905,7.738658,-6.344746,-4.318958,7.390585,9.899533,8.707200,-3.868738,9.521193,4.154607,8.564901,8.627056,5.773975],[-5.884182,9.112286,0.252087,-1.662722,5.362984,-6.432582,-6.306118,9.474184,3.126207,-9.838611,-6.897330,7.838588,-3.184333],[0.561150,0.306214,-3.176192,5.803283,2.686053,3.678401,6.832404,3.210228,-6.932308,9.217088,0.606263,3.589535,-0.685919],[-1.878806,9.428591,8.090605,-0.258684,-8.203457,-3.106053,-1.133754,-9.614167,3.920371,-2.870816,-2.431637,-8.405260,-0.517802],[-9.852675,0.667502,5.843713,9.393318,3.939282,3.022365,1.352084,-6.316888,-4.526193,-6.066329,-4.416151,-7.310345,-4.384869],[-3.826076,2.666296,-8.575017,-0.543871,-3.495366,9.102731,-3.299713,-7.491127,-4.350580,9.182794,2.005105,0.066954,9.845923],[-9.979228,0.935480,-9.563813,2.737576,-6.498484,5.574619,-5.028151,3.684639,1.666096,-4.267531,0.177468,-3.119633,9.418939]]], dtype = "float64")#candidate|2594|(10, 14, 13)|const|float64
bop_2595 = relay.logical_and(call_2584.astype('bool'), relay.reshape(const_2594.astype('bool'), relay.shape_of(call_2584))) # shape=(10, 14, 13)
bop_2598 = relay.logical_and(call_2585.astype('bool'), relay.reshape(const_2594.astype('bool'), relay.shape_of(call_2585))) # shape=(10, 14, 13)
func_1396_call = mod.get_global_var('func_1396')
func_1401_call = mutated_mod.get_global_var('func_1401')
const_2601 = relay.const([-3.877165,-1.490716,9.362567,6.254224,8.634486,4.189255,-9.707651,0.759291,-6.515703,-8.768329,-4.779514,6.602549,6.583576,-4.662120,-8.878123,6.546215,1.647646,9.544583,-1.489086,-3.942347,6.948683,7.550155,-7.362773,9.301349,-8.869776,5.658637,-9.516417,3.122918,2.984193,-1.686889,-0.530473,-6.389645,-0.693653,-5.454317,0.944172,-2.728505,-1.578830,-1.040271,-5.560320,-7.668505,8.480847,0.332856,-8.049443,9.180918,-0.120728,2.747740,-5.862104,-5.200211,1.297160,1.964590,5.256561,8.876249,6.610398,-2.730119,-9.484444,0.407331,-5.085333,8.014553,9.057543,6.481330,6.937555,-2.059681,-3.588917,-3.313074,9.406313,-8.458370,9.779335,8.771742,3.190795,-7.193840,-3.332794,2.980639,-3.286481,4.253287,-5.028027,4.624887,2.874472,6.769352,6.353365,0.956186,4.150452,8.307657,1.780446,6.471071,2.402352,-6.942757,9.795430,-8.427051,3.653156,-7.338971,-4.864457,0.405534,4.662513,-5.012314,-2.128767,-3.008004,7.379010,-7.330422,-8.980769,-6.874143,8.349139,3.092428,-0.949522,-5.344011,4.946231,0.259871,-7.604939,2.742773,6.838534,-0.217665,7.878656,9.575967,4.845993,6.648743,-1.886935,7.140046,2.097753,-4.274528,-0.656874,4.067466,2.962916,-2.292067,3.628287,-0.578777,5.524897,-1.093110,6.342667,4.250688,3.680575,-5.456211,-5.426125,3.208771,-3.276098,-0.279376,-1.372268,-4.880424,-7.180742,6.846984,-1.639330,8.326470,4.673734,-2.723113,1.573497,2.579630,-3.560225,-1.510048,9.736784,-2.239441,-9.072558,-1.615338,-0.261391,-0.440220,7.029148,-6.409517,8.139939,9.312381,7.553161,4.007509,-2.839440,2.824890,-4.412698,3.879865,3.701002,4.820130,-0.006760,-6.363295,-9.917639,-5.216320,0.441963,3.420913,-5.644613,3.273522,-6.067917,-1.886648,4.487685,-5.288102,-2.675419,4.924708,9.907179,0.582257,-1.207693,5.154552,-7.623963,9.595222,-1.265331,7.822149,7.871432,8.864347,3.405843,-9.729507,1.284164,6.239235,4.178690,-2.905877,3.703433,-4.502989,8.806245,1.755148,7.621931,0.768082,3.184904,-1.503356,0.429883,5.928215,-2.724988,4.194423,-4.014348,0.755807,1.185618,-1.127400,6.588300,1.340385,-7.102454,-6.653475,4.801450,-6.234414,-7.418458,0.352342,-4.872117,3.983886,1.774470,-6.496970,8.316494,6.495664,8.903899,2.931240,-4.206361,-9.569120,0.150596,0.026797,-5.433788,-3.108675,-8.649829,5.022906,-8.307100,6.273939,4.353182,7.784335,9.138941,-5.238875,-8.275214,3.924761,-1.251391,-7.225546,2.292440,-3.492134,2.599457,-8.218123,-0.041541,-8.136549,-7.572425,-8.592098,6.553357,-2.866781,-9.232199,-8.954499,1.532902,-1.859612,0.639004,4.619843,-2.861675,-3.726263,-9.160941,2.019590,-3.472404,4.277761,-9.402557,2.223938,3.867520,-6.063803,-0.545513,8.930760,3.251881,6.995921,-9.250902,6.555215,-9.471769,-5.927827,-1.239208,3.336104,4.166742,-3.582379,2.230385,3.525001,6.379075,-0.627874,-3.845219,4.325973,5.387953,-1.505098,-4.262588,-8.140964,-8.079485,2.020039,8.491151,9.551457,-9.587482,-5.197391,4.635226,-5.816440,1.516977,-8.105727,-5.663349,4.765505,-6.143936,8.255843,6.068952,9.994875,-1.717439,2.160553,-4.764706,-7.528945,-8.152304,-2.343946,2.702806,-1.311301,9.542657,-3.762088,6.242826,-7.188980,-2.295705,-2.119506,3.032199,0.641264,-7.709484,6.080078,8.953105,3.710580,-3.435382,-2.720055,5.854588,9.008644,8.609881,-8.991865,5.114585,5.391910,2.356966,-1.008409,8.543863,-4.691011,-2.978064,-5.467688,-5.810693,8.797662,0.637825,-5.531803,-2.690528,-6.826226,6.670359,-5.767124,7.204418,-8.090812,7.946311,4.197063,-1.466948,9.339743,-4.865069,9.820776,8.149330,0.839189,-0.629614,9.976835,5.677812,-8.591207,3.937468,-1.104218,-7.320559,3.772156,8.289047,9.450248,-9.802524,-5.836051,-1.105589,8.020050,-8.418193,0.239902,-7.088678,7.269319,-4.743082,3.040236,8.172483,-0.721017,-1.708152,2.060009,-1.852843,-5.326316,1.706905,0.003764,-7.082636,-1.247502,-2.081303,3.595528,-7.711446,-3.830423,-6.094840,-4.742439,5.894317,-0.230112,-0.594206,4.399736,-1.953450,-9.122382,-3.263588,0.250178,-3.157008,6.067238,6.203104,-0.483597,-1.637233,-5.712376,-9.904361,-1.290183,5.114491,4.709939,-4.245126,4.678205,-3.800571,3.139374,9.571961,3.046793,-2.642042,-1.288611,4.663566,4.322944,-2.757516,1.185705,1.494843,-5.175016,-0.225370,-5.343384,6.374850,6.174764,1.888496,-4.775334,8.277132,6.044087,8.564953,-3.768574,-2.725624,-8.367509,2.426093,8.225359,0.557258,-8.070714,4.093361,-5.682251,-8.776093,9.790018,-6.420869,-3.651528,0.672860,8.400224,-4.947532,-0.068650,-6.674884,0.808197,-3.828526,-2.732655,-8.317171,1.216754,2.048550,-3.550176,2.384177,-7.712936,-6.936025,0.615117,-1.750821,-7.866107,-0.159057,6.702015,9.142829,3.076334,2.204705,0.134163,-9.219301,6.901224,-9.739991,1.683621,5.580228,-8.494160,-4.517293,-6.623552,-1.984163,7.463702,9.436436,4.398159,9.377776,-7.527186,-5.809214,1.047030,-8.978816,8.987983,-7.186145,-0.396640,-7.818395,0.504039,-6.085595,4.047237,-0.285911,-9.137399,7.047424,-7.225368,-8.483326,0.521537,-2.175920,6.729264,8.734000,-2.293182,0.927779,-7.174200,2.350887,-2.610074,9.405350,-8.079298,8.944773,5.633686,1.171931,2.670377,-9.600243,-6.999600,9.066388,6.816927,-8.565102,6.708630,-1.891028,7.508913,9.258925,6.009035,1.032383,3.142148,-5.993796,8.480546,-9.677511,8.501219,9.485628,-5.447085,9.960693,-6.080114,3.103222,0.230217,0.016153,0.723042,9.638039,8.208271,-0.379964,2.460140,2.288831,-6.602500,4.379199,-7.574254,-4.763479,-4.554161,-1.322312,0.781540,-9.449998,9.195554,-5.946674,-7.768511,2.713243,-2.609821,-4.778363,4.747515,0.321530,-0.525068,5.809035,3.028702,8.588424,-2.837490,-8.159204,8.053033,-8.579106,-6.534880,0.547969,-9.494745,-7.332771,-8.112408,-9.464126,-4.321292,-4.447962,5.245467,4.246290,5.555613,-5.777392,-7.269009,4.965877,0.619582,-4.563164,-8.536864,-6.082393,4.758850,-9.489012,-5.571467,8.047136,-9.586554,6.152485,8.562705,-3.287178,7.389679,-9.024431,-8.468158], dtype = "float64")#candidate|2601|(600,)|const|float64
call_2600 = relay.TupleGetItem(func_1396_call(relay.reshape(const_2601.astype('float64'), [600,]), relay.reshape(bop_2595.astype('float64'), [10, 14, 13]), relay.reshape(call_2584.astype('float64'), [10, 14, 13]), ), 4)
call_2602 = relay.TupleGetItem(func_1401_call(relay.reshape(const_2601.astype('float64'), [600,]), relay.reshape(bop_2595.astype('float64'), [10, 14, 13]), relay.reshape(call_2584.astype('float64'), [10, 14, 13]), ), 4)
func_703_call = mod.get_global_var('func_703')
func_705_call = mutated_mod.get_global_var('func_705')
call_2604 = relay.TupleGetItem(func_703_call(relay.reshape(const_2601.astype('float64'), [15, 4, 10])), 0)
call_2605 = relay.TupleGetItem(func_705_call(relay.reshape(const_2601.astype('float64'), [15, 4, 10])), 0)
func_1530_call = mod.get_global_var('func_1530')
func_1534_call = mutated_mod.get_global_var('func_1534')
const_2608 = relay.const([[-10,-5,6,-10,-8,-1,6,-4,-3,10,8,6,6,-2]], dtype = "uint8")#candidate|2608|(1, 14)|const|uint8
var_2609 = relay.var("var_2609", dtype = "uint8", shape = (112,))#candidate|2609|(112,)|var|uint8
var_2610 = relay.var("var_2610", dtype = "uint8", shape = (140,))#candidate|2610|(140,)|var|uint8
call_2607 = relay.TupleGetItem(func_1530_call(relay.reshape(const_2608.astype('uint8'), [2, 7, 1]), relay.reshape(var_2609.astype('uint8'), [2, 7, 8]), relay.reshape(var_2610.astype('uint8'), [2, 7, 10]), ), 0)
call_2611 = relay.TupleGetItem(func_1534_call(relay.reshape(const_2608.astype('uint8'), [2, 7, 1]), relay.reshape(var_2609.astype('uint8'), [2, 7, 8]), relay.reshape(var_2610.astype('uint8'), [2, 7, 10]), ), 0)
output = relay.Tuple([bop_2595,call_2600,const_2601,call_2604,call_2607,const_2608,var_2609,var_2610,])
output2 = relay.Tuple([bop_2598,call_2602,const_2601,call_2605,call_2611,const_2608,var_2609,var_2610,])
func_2616 = relay.Function([var_2609,var_2610,], output)
mod['func_2616'] = func_2616
mod = relay.transform.InferType()(mod)
mutated_mod['func_2616'] = func_2616
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2616_call = mutated_mod.get_global_var('func_2616')
var_2618 = relay.var("var_2618", dtype = "uint8", shape = (112,))#candidate|2618|(112,)|var|uint8
var_2619 = relay.var("var_2619", dtype = "uint8", shape = (140,))#candidate|2619|(140,)|var|uint8
call_2617 = func_2616_call(var_2618,var_2619,)
output = call_2617
func_2620 = relay.Function([var_2618,var_2619,], output)
mutated_mod['func_2620'] = func_2620
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2622 = relay.var("var_2622", dtype = "float32", shape = (4, 9, 5))#candidate|2622|(4, 9, 5)|var|float32
uop_2623 = relay.atanh(var_2622.astype('float32')) # shape=(4, 9, 5)
uop_2625 = relay.cosh(var_2622.astype('float64')) # shape=(4, 9, 5)
func_1396_call = mod.get_global_var('func_1396')
func_1401_call = mutated_mod.get_global_var('func_1401')
const_2628 = relay.const([7.901006,8.552514,2.637672,-2.173869,3.912532,9.366997,0.915127,-3.926635,-9.916386,-0.431154,2.694147,0.880736,6.660885,-3.068147,-8.852264,-6.298762,0.284812,-6.801335,-2.495773,7.740559,-6.457763,-8.939032,5.021118,-4.538040,-5.927869,-4.730728,7.077564,-2.054996,6.569685,-0.503972,-0.677073,-5.735205,-6.718837,-2.219840,4.280371,6.197310,-5.084312,5.661285,-6.326440,7.434809,5.053026,-0.681240,9.149081,4.104467,6.843167,7.693842,4.941339,-2.013420,-0.609242,-3.756757,-8.435823,1.854846,4.533269,-0.659353,-1.257760,1.564100,-1.597280,1.086121,-4.067171,-3.983156,-0.137447,2.124271,6.419915,4.353680,-2.521467,-9.997206,9.762037,6.576406,-1.445356,-0.898247,-0.942582,-1.824454,5.744842,-2.053517,0.787747,-8.545297,-4.536655,9.169837,6.379099,-1.134727,-9.122204,-9.830511,-6.222569,9.033161,3.484878,-3.079152,0.375552,-0.985125,-5.406931,-4.351624,-6.502572,8.505687,4.931277,-4.180696,6.257523,-9.041460,8.550551,-7.295356,0.146077,8.916902,7.616929,-3.556051,-6.768188,-7.999811,4.562221,-5.839916,0.307639,8.005188,-7.030536,3.664887,-8.633251,-5.896815,-4.458327,7.097385,-3.363567,-5.173749,-6.194059,-1.960436,-1.950565,9.467156,5.313497,0.758190,9.124348,1.642316,-5.085840,-9.411159,3.621852,2.332690,6.741631,8.391201,6.898373,6.168931,-1.025397,-1.810991,-2.386357,-3.266704,-9.425378,-3.633225,-2.051666,9.732876,-5.851669,5.072138,-1.449603,0.870382,-8.006592,3.602889,3.113773,0.408234,-4.526079,-1.724134,-1.726062,0.312149,-6.860843,-1.557176,8.588787,0.416887,8.720251,0.600209,1.865549,5.365031,8.562565,9.371228,-3.346385,-3.008433,8.367799,6.403611,-4.080337,-8.643298,2.104164,2.061306,-4.436804,-1.855712,-1.032481,-4.848746,5.456409,1.910989,-5.232761,8.699645,2.379936,-9.265772,-7.419167,-8.827182,-5.766385,5.761391,-3.786703,-7.375826,5.582120,-9.621672,5.214698,-4.604570,4.151831,3.924010,-8.819864,-4.145491,4.690650,-0.771736,-6.666785,-1.768738,8.994529,-4.354178,-4.346375,4.003788,-4.478371,9.949902,-5.432955,-5.872071,8.087628,0.526599,-8.600438,-4.324169,-4.744949,8.220644,3.615981,6.624558,4.242762,-2.090522,9.098904,3.868456,-6.250642,2.745095,-8.494712,-5.426478,5.026294,-5.721389,3.928624,9.446478,9.637550,-5.093627,-3.110118,-1.578527,-1.011279,-5.764405,-5.337655,0.245492,-1.845096,8.202740,-0.076697,8.655313,4.557415,2.209773,-9.206500,3.844172,6.220131,-7.638653,7.270832,1.244178,-5.846698,9.004973,6.554540,2.411739,8.733378,7.865617,-5.329910,-7.846458,-9.902596,-2.144543,-1.475264,-9.440201,8.437972,-7.707727,9.356789,-1.475166,0.324154,-1.418617,-9.601203,-9.941636,-6.043907,9.036675,-9.763382,8.053124,3.669500,7.084997,5.252018,8.947468,3.721109,5.146359,6.836306,-2.534539,-5.271143,-4.813465,-7.196854,-0.653904,-5.324952,8.831682,5.427548,0.014014,-1.506917,8.338943,-4.237148,-4.266900,-5.032328,9.229177,-4.712164,-6.514334,-8.048684,4.232166,8.465545,-9.088204,-2.889665,6.938832,-0.001030,-5.916081,3.992227,-6.837379,6.698357,2.973187,-6.339429,2.254261,-6.309363,0.463846,-0.990402,2.432797,8.318738,3.887513,9.694189,0.356811,8.914765,-1.614513,6.664401,1.220054,-2.850006,-2.869824,9.771696,5.990680,9.007581,-9.699147,1.730609,-0.179505,3.298484,-1.978931,-6.099367,-1.555187,-5.051417,-4.843692,6.520790,-2.697392,9.486493,5.888531,-7.918567,-9.054655,3.152659,-4.142945,0.847976,9.601077,-9.787200,9.016750,-6.583193,7.522859,7.523759,-3.578570,0.835481,-4.288917,-3.940643,5.972811,-3.796155,-3.485305,-2.741244,-4.957790,4.950805,2.953721,-6.831097,-9.837611,-2.955857,9.299925,-8.211048,3.352116,-3.630596,-3.096329,5.968464,3.939729,1.460278,7.995454,-6.590521,5.555537,-5.786003,-6.526700,-0.741518,1.013926,-6.204411,-7.381878,-7.587184,-6.942858,0.804760,3.014752,-6.100489,-4.428279,1.712738,5.235865,7.431538,8.075370,6.124717,-9.343814,3.302826,8.271458,-7.836425,-7.298947,3.229074,8.377803,1.506375,0.893078,-6.800974,3.150269,4.281001,6.310330,-0.763567,-5.067192,-6.643197,0.568316,-0.911883,9.184973,-6.421883,-7.540867,-2.704791,-1.438558,-9.008963,5.478497,2.900348,-0.035291,-4.268186,1.627815,7.815844,-7.166944,9.135262,3.972900,-9.363372,-3.482639,-6.531784,-1.615292,5.378276,-2.531329,-1.246590,-3.368326,-4.174596,8.069858,-5.312587,7.036159,-4.937959,-7.097034,2.423780,-5.962736,-4.661173,-5.002136,4.449896,-4.558723,7.408491,-4.727292,-5.247192,2.018600,-9.923753,5.902935,-9.835555,-8.822565,5.001015,-9.111052,-0.060066,-7.947266,4.555185,6.564578,-2.045395,4.554976,-6.243892,8.976197,-4.174003,9.112892,2.333491,-7.227056,-8.571449,9.645116,4.953880,-1.283478,-2.872639,-9.207067,-5.069516,-9.630814,3.899584,-8.905100,7.014946,9.284120,0.737815,-5.697277,4.166359,-9.546572,8.301185,5.164881,1.490003,-6.105669,9.362467,7.551203,-3.351480,-5.121275,-1.416360,1.290958,-0.683017,1.497815,-5.433275,6.093426,-4.635431,6.969713,4.722945,-0.385293,-6.663311,-5.120586,-3.655407,9.608603,7.436544,-2.968805,0.078413,5.916129,-5.129067,6.645249,6.107764,1.395090,-6.993540,2.535562,2.395085,-3.517866,6.021481,5.528993,-7.227513,-4.615751,-8.648230,5.914575,5.040371,-0.131432,-4.459450,-4.115819,-5.087517,3.670494,-2.151958,-6.091097,5.604751,6.846056,9.099660,-7.433892,-9.558066,4.074157,1.033496,-0.012719,0.465775,1.613509,-2.822290,4.249790,7.951917,4.581062,-7.478563,3.042281,-1.398800,-9.205455,-8.586604,1.980726,6.499885,3.535417,-1.772149,9.364104,-1.341834,7.992694,-2.150592,0.182737,4.499847,8.201976,-7.917047,7.087054,-5.098126,-2.854324,-0.158358,8.608138,-1.743523,4.975702,-7.414678,4.273589,1.278335,8.231230,1.191603,3.039722,2.009251,-9.821387,3.673842,-5.560938,8.663424,-5.905829,-6.167685,-7.730092,0.224106,2.402277,-9.359554,-3.864297,6.052223,-1.475812,9.964572,-0.832681,-8.460891,-6.205124,-6.158167,0.801428,-6.784323,-9.019314,9.354083,4.178367,-9.280576,-9.191863], dtype = "float64")#candidate|2628|(600,)|const|float64
const_2629 = relay.const([-4.260698,-5.060488,-0.429437,-2.521286,1.996959,-9.432440,5.570096,-4.046244,-9.895150,3.133301,0.764352,-2.181637,8.422263,-5.891792,1.132030,-7.644144,8.664641,7.190089,3.346554,6.582823,4.028618,-1.790776,0.017275,-0.545718,9.981326,-4.514459,-0.397495,-5.121826,3.844602,4.133048,1.482959,0.263905,-9.563036,-0.252638,-5.871538,-5.357448,-4.997039,5.986204,9.007678,4.578859,2.260707,6.706939,-8.198255,2.082187,1.909138,-1.317795,-9.557969,7.290819,6.574466,-6.629437,7.434563,3.442188,-4.833487,-2.074158,-8.366103,-8.991798,4.954764,6.002361,-0.171377,8.825150,8.869372,-1.615384,9.138461,-9.987573,-7.115527,6.156584,-3.845632,8.581852,9.243033,-6.275948,4.329015,6.614925,3.830199,-9.973035,3.367159,7.505244,6.256696,5.718730,1.551346,2.514014,-2.157534,-1.809298,7.638879,1.270712,6.026911,-8.509799,5.220105,8.209634,2.521524,-3.592752,2.163024,3.271197,6.366937,-3.598955,0.654886,-7.047421,-9.697837,-9.810802,-5.067755,-0.121879,6.945568,-2.901612,-4.058520,2.426012,1.954122,-4.006231,0.785623,-5.573357,-0.118031,-0.771278,-5.211694,-9.394147,0.941691,3.368261,-7.379919,7.845637,-4.650970,-9.086000,9.700173,-0.630007,9.600431,6.598748,0.625909,-9.794193,-2.147059,9.301207,3.244341,1.102461,-2.288545,1.566689,-3.365253,-1.644729,-3.050240,3.141062,9.077026,6.721318,1.583879,5.407618,-6.225679,-6.497334,-4.008479,4.587892,7.102491,-2.716183,4.332943,2.510856,-7.018032,9.337861,-8.321051,-8.093909,-8.778864,6.539762,8.589232,-2.347621,-1.481038,-6.253294,-6.188245,-1.088348,0.621586,5.909103,-2.006373,-3.692397,1.298919,-3.448748,7.262268,2.511850,-8.260891,2.264380,1.588266,6.365968,-5.900556,3.784208,3.074175,5.077366,-7.535509,-3.597348,8.855262,-2.081507,-7.294643,-8.311824,9.431295,5.503355,-1.863863,7.058782,9.697123,2.061354,0.862797,-4.672724,4.753588,2.697441,3.803552,-1.409764,-1.231275,0.160676,3.426038,-9.843322,5.880833,-7.748866,-3.997228,2.212880,-4.196129,-6.734284,3.480742,4.635416,-2.644453,5.721326,-3.679083,-9.466614,-1.928363,6.461544,8.752610,-1.896627,6.030187,2.781328,2.060428,9.287347,0.552861,1.870008,0.259859,0.562006,6.437497,5.223743,4.686695,-7.435900,1.632753,4.630752,-1.311313,9.852927,0.341987,4.005248,8.284125,-4.575404,-9.416333,-3.913103,-4.923032,9.269039,-3.070560,4.988755,-8.407851,9.815603,7.093273,2.174517,-4.440442,-7.177139,8.695875,-3.603506,-1.487619,1.174494,-1.700975,-8.000304,-6.455235,-6.012116,-9.921591,-7.094048,-4.465230,-6.817694,-8.756793,4.579217,-6.131897,-6.320221,0.334762,7.255801,-2.433951,5.358359,-7.178950,1.485042,2.871227,2.291208,-6.311996,7.467183,5.829388,-8.192355,9.819851,-0.421661,6.490208,0.089568,-6.627751,3.101286,2.678794,8.154268,-5.906362,-3.126826,2.759915,-3.465051,7.989889,-6.136108,9.681204,5.071993,-3.782827,8.112547,-6.019022,-0.373334,6.566906,0.690772,-2.097378,-4.181560,-3.474608,4.497698,-7.369326,8.289038,2.753655,-4.937950,-5.146823,1.467072,1.250992,4.525046,6.502230,-1.232723,7.620884,2.067497,0.539288,-3.472063,1.995949,0.076847,5.109626,0.695153,-9.207146,-7.255689,5.177376,7.103323,-0.580286,4.297927,-1.264621,-4.856887,4.371956,-5.338000,3.954331,-2.309254,-6.522106,-4.324065,-6.774006,-6.950480,2.197654,-3.716230,-8.024618,7.906769,-1.667884,-4.416515,5.756004,-0.838830,-6.856647,9.036661,8.430789,-6.618335,3.723570,-8.435760,3.320684,-5.412248,0.456113,8.014264,-2.030201,-2.756468,8.166796,5.699138,1.995420,-4.740713,-7.228838,9.546052,2.402149,7.825867,-0.217692,4.857506,-6.819330,-1.210238,-1.070906,3.252881,-2.900509,9.266341,-2.667285,-7.761095,-4.316340,-3.558289,-8.455226,-8.261634,5.586581,-2.114353,2.755868,1.177641,2.305790,3.629158,-4.855364,-1.549450,-9.196321,-2.507075,4.936582,-8.727644,5.815776,-1.634147,-6.245343,-8.552773,8.134421,3.581604,-1.355706,-5.334248,-9.748738,8.776398,4.512151,-5.429084,8.275803,-7.377506,5.439885,-8.970552,5.346509,4.716438,1.663335,-9.984785,-8.574175,-1.832698,-1.783798,8.627013,-0.903700,9.868364,-7.676923,-1.416286,6.130281,-4.826899,4.695080,6.207502,-5.576410,2.023181,-3.783086,-3.865057,4.734857,6.822301,0.291967,7.133862,9.995656,7.869914,-2.273440,8.546543,3.786292,-3.144229,-1.338557,3.272218,-7.733788,7.973007,-9.342657,-0.916895,-4.839226,-8.449734,-2.854250,9.693153,-6.086422,1.572211,-9.695533,-8.504341,9.768732,1.496036,5.609258,-0.300793,8.308995,-3.542972,0.067114,4.793267,3.379232,8.430188,8.861277,4.484003,-3.039956,-0.717193,-9.033187,-1.676728,-9.422776,3.445656,-6.879255,5.257889,3.202526,-2.253644,-2.870982,-7.602935,2.415398,8.770855,2.521414,-8.286584,-2.623698,-4.572895,-1.331022,-3.736861,-8.441843,-1.918198,2.843275,-3.651349,1.854805,9.303800,6.987925,0.147506,5.668262,5.062484,-6.207351,-1.637578,2.668768,3.086720,8.394679,-0.913326,8.497782,7.939566,-1.226584,-3.276588,-2.155350,-4.936630,8.278045,-2.234577,-4.272296,4.085906,8.916571,4.135833,8.019731,-7.372403,-0.527364,-4.423608,8.942832,-8.309921,-0.419095,-9.152269,-7.423748,-8.383817,-2.492539,9.269371,-8.045390,5.352508,-9.758872,-2.323015,1.309474,7.922685,4.831076,-4.999989,8.750860,3.385975,0.247165,-3.161762,-4.068576,6.848107,9.808358,7.227967,-9.249756,0.210609,-2.833783,-4.775849,7.553305,7.098155,8.050405,7.787729,6.525201,-6.564241,-2.024468,-1.930849,3.038679,-4.826934,-9.887972,2.380146,-7.263673,-8.746516,-8.831865,2.091352,-2.453928,2.399281,-0.799730,-1.840914,3.979612,-0.914499,0.796173,-0.525934,-1.442762,9.647785,-6.932596,8.827795,8.374403,6.707902,-6.296521,5.314711,-4.406556,3.385344,-8.158810,-0.761192,-0.774620,4.871396,1.981778,1.102143,-1.324589,6.446069,1.379095,-6.905729,-2.310519,-9.144213,-5.354882,0.485819,-7.208536,7.029455,-5.287614,-5.243213,-5.420577,-4.696281,3.595548,6.582068,-7.015888,7.272228,-7.231798,-7.804722,0.560830,1.552432,8.283885,-1.394921,5.012932,-2.424202,4.422453,2.089973,-4.602581,-0.167149,2.534227,-2.706390,-6.903834,9.857036,8.301548,1.021504,-9.734542,-1.133272,1.714322,-7.570139,-0.330442,-2.967099,6.124500,5.652164,9.174338,-5.585352,1.941039,-9.552623,-9.128526,-1.694403,5.443262,-9.921647,2.870681,5.967775,-1.193926,7.573682,-7.936176,-2.675685,0.193522,-1.211856,3.625313,0.097682,7.262819,-8.794374,1.857255,4.267141,-0.493643,3.929641,-9.700361,-1.557764,-5.716857,3.823271,0.362802,-7.430571,5.951562,5.439717,5.324826,2.341303,-1.442246,-6.675847,4.987588,0.288398,-8.296435,9.869417,3.382917,4.245865,5.403915,5.564194,-9.399060,-8.283019,-4.126818,8.170451,-1.999319,-0.637210,-6.464193,4.367301,-3.694829,-4.509148,7.077060,0.510499,3.860353,-9.084510,1.778629,-5.774297,2.862810,1.360710,-3.973722,-0.381982,6.867752,-1.312358,1.689015,0.954424,-9.342236,-1.889923,0.191390,-6.931054,-1.749753,-7.116611,-0.718385,-1.375274,2.016358,0.428901,-1.885567,-6.128843,-4.819609,9.665266,-0.518411,5.009606,-0.780767,-0.353076,3.867682,7.496517,5.931059,0.901856,-7.123036,-0.414446,7.745827,9.409418,0.789704,-5.536815,-1.448582,1.102584,-2.048205,2.828108,7.193659,9.908299,9.753575,-2.157004,-0.498759,-5.315706,9.161483,-2.670011,8.882710,-8.945792,3.102749,-6.532607,6.426201,2.980605,8.270271,-9.343798,-3.448488,0.046568,-8.834416,1.272785,-7.541790,6.660692,-2.306294,-8.966347,-8.804368,-6.077348,4.927574,5.923216,-8.162979,7.492400,-8.510301,-1.464099,4.353635,-5.926624,-6.210471,-7.770628,1.354331,-1.088079,6.325371,8.065395,-4.596216,9.771659,9.391186,-5.804990,4.053765,1.869224,9.730434,2.163217,9.708881,5.551635,2.061828,-0.373045,1.360709,-0.899936,-1.533259,-3.370036,0.796641,-1.966313,8.857677,-7.908726,-1.474693,-8.065490,-9.747654,-5.401535,9.503644,8.843081,0.889753,8.269563,-7.968166,8.389645,-2.028702,9.675589,-6.478161,-2.494871,-8.718747,-6.000905,-3.295265,4.401823,-9.248127,-7.234223,6.820830,-3.486325,-1.132442,5.955579,1.649087,3.713469,3.167887,1.266059,-8.441416,0.963620,0.816078,-3.908639,-6.133209,-4.703387,8.148875,-5.981033,-4.246041,-4.190543,-6.670084,3.175711,-1.965464,9.487091,-4.029695,2.668002,-3.938385,8.975345,9.067363,2.929916,1.592917,-3.274187,5.733410,1.819974,-7.447694,-7.964889,-0.080919,-4.567809,-2.253668,-9.761710,2.197272,5.211211,-3.903145,8.876450,-0.607189,1.737017,-1.083115,1.578144,-0.337573,1.915320,-9.125876,5.873111,2.131234,0.124896,-3.380830,-2.135479,-6.942629,5.737502,0.215576,-8.336511,-6.068071,4.019762,2.142414,-6.428085,-5.492648,-3.302558,1.747723,7.628188,-5.953690,-6.156190,-0.855126,-6.927373,-2.878074,0.477870,-4.444221,-3.623807,0.961630,9.242335,-7.875403,-1.796042,6.805944,4.121998,-2.235133,1.414886,8.502776,4.586512,3.618662,-5.967035,-7.826031,2.486087,7.762304,9.250267,2.344476,-7.694931,-7.171892,-5.873083,9.824280,-0.271845,-3.089598,-3.446376,9.663672,7.441167,6.263741,-0.985298,7.681343,-5.174553,9.575972,7.593224,-2.146612,-9.799580,-7.742696,-7.075858,-2.665436,-9.223784,8.409480,9.030841,-3.589492,3.800594,-5.666764,9.335935,3.123405,5.708721,5.114686,0.692595,-5.822945,-1.367228,7.743671,-1.116774,0.706304,-2.260645,-9.076841,7.640481,9.099412,-0.388463,9.322526,3.603127,-3.349446,0.747711,-6.106404,8.516561,1.104214,0.928591,1.178352,-3.091448,-1.624895,7.972724,-9.264586,-4.755452,5.445266,-7.729496,-1.083480,0.818205,-9.835805,6.738150,8.219659,7.275559,-1.448606,5.003128,-3.834801,4.812102,1.519359,9.185530,4.888077,8.085095,1.238707,0.558619,0.671959,-4.447705,-4.858812,-4.742714,-9.136866,-0.552894,5.015626,-3.479419,0.465927,-9.106697,-0.776716,1.258235,0.963221,-7.370278,-7.334839,6.054199,-8.223262,4.683164,5.684593,9.133079,0.609502,-8.723176,3.440989,-4.032218,-8.508694,9.794014,7.967488,9.226991,7.193051,5.157730,6.955664,-4.996237,-9.438291,-7.642996,5.380788,1.350961,4.248775,2.137984,2.719347,-5.911164,7.174246,-1.469853,-7.369377,2.126045,-3.567312,7.878557,8.165497,5.711146,4.061670,5.432231,3.009791,2.070192,7.690791,-1.417135,-7.202644,-4.425449,-0.839271,-9.030255,-9.694619,7.452467,-0.501732,7.776568,-6.342050,4.079785,-1.904884,-4.024293,-7.845226,5.394644,5.241401,-6.973228,-9.636236,0.119230,9.032857,1.282840,8.923172,-3.357238,2.464835,-9.138177,3.697695,7.211757,-4.476192,7.004265,8.649756,-8.694165,-2.753858,-4.919780,-8.625551,-8.102336,-9.861482,0.873354,-5.280723,5.158809,0.113916,0.257818,-2.258051,2.935245,-3.127471,5.906056,6.915208,-7.759960,-2.592819,-4.219632,-4.561405,-0.970145,-0.500750,3.906912,-5.591755,-0.714183,-6.781139,-2.140357,-8.278894,3.780980,-6.415094,-2.558741,1.900396,-0.175053,9.925689,-4.043502,8.898171,-2.652142,-8.877056,-7.718946,9.195600,7.810287,-4.723037,-7.557845,7.116832,9.109630,-7.411732,6.780096,1.231023,4.695306,-5.175563,-9.168835,-2.893183,4.239597,-4.542846,5.094858,-0.396145,1.951926,-7.946739,5.816766,-1.228412,-2.109591,-1.917350,-9.025758,8.400143,-8.048036,7.529774,4.568156,-6.584044,-5.726421,-3.234499,-1.896259,-4.245705,8.882148,2.344634,-0.797177,6.314088,-9.404674,-7.047743,4.408918,-6.808958,6.955720,2.953766,2.310361,8.207371,-2.331084,-8.315744,-2.575365,3.333329,9.398982,-8.986167,-3.727207,-4.440379,5.420572,5.903893,-7.451511,6.770181,0.371035,-3.381840,-8.542579,-1.566509,3.418991,3.534415,-8.543334,1.145750,4.027431,4.138916,-7.779838,-1.501605,9.796319,-1.461621,0.627209,2.802292,-4.540268,0.897049,-1.456768,-0.284069,-7.974304,0.628857,-5.757841,0.260235,7.281436,4.803109,-8.532119,2.615774,3.641526,-4.713465,7.673318,7.013449,4.786214,-8.956457,-3.537919,-0.036003,-6.279471,0.103200,-8.120103,-8.880938,-4.221105,7.157456,2.652138,-5.982342,4.830478,0.352248,-6.134058,-2.083432,-8.324571,9.616008,1.270560,5.075551,-2.743150,-5.855658,5.969621,-5.886357,-6.821464,2.134046,-3.183658,-6.875656,-1.292405,0.271738,-9.116277,-9.243177,-0.433219,-2.730191,4.914058,-1.947964,-3.300474,4.257902,1.071178,2.619876,6.815719,-5.334082,-0.579727,7.093705,-8.436159,-2.955499,0.738877,4.610563,-7.315535,3.884866,-5.318697,7.092809,2.583118,-9.219932,-5.916645,-0.971246,-4.229248,-3.417472,-6.951772,3.941014,-4.350687,5.949322,0.890027,4.310601,-6.905072,7.283765,-7.069273,-3.382148,3.109352,6.111133,-0.055970,-9.883092,-7.233386,-0.916312,-8.742414,0.016302,2.506757,-3.771259,-1.733442,-4.893162,0.555355,4.107990,5.603278,8.992106,-7.951725,-9.445014,-8.957785,-8.617016,5.479497,7.947243,-6.927147,-1.730017,-7.502643,-6.928917,3.748899,3.533044,4.078635,-9.070389,-4.131478,6.675225,-8.818927,-9.286056,-8.022510,1.814483,0.489862,-8.303229,-3.841031,4.718911,3.402505,9.506465,-5.686419,4.460836,1.888954,-2.383210,5.226504,-0.196481,-7.568527,5.267023,8.788617,-4.951095,3.044570,5.236607,-3.932838,-6.005018,-5.180943,-7.246747,7.113502,-1.134221,1.564299,-7.706959,2.439849,5.199792,2.001695,-9.534087,0.955084,6.145938,0.817095,-0.093203,9.693055,-8.843373,-4.133312,1.173800,-0.866838,-1.839256,-9.829323,9.952618,-5.006820,7.663554,6.893914,-6.352641,4.202006,2.258990,-8.966443,-1.174428,2.983121,-4.651128,4.568130,5.711959,7.558115,8.683068,-9.343823,2.251779,6.461113,0.350208,6.438567,-6.521704,0.393165,3.149034,2.035493,-9.906854,-6.951109,8.314142,-7.104092,-4.003578,-9.815554,6.221393,-7.136395,2.050855,-7.489243,-4.985776,8.984676,-6.061127,-5.215595,-4.093791,3.398113,-0.097180,6.017286,6.229094,-8.790243,-7.507242,4.036049,-4.545713,-2.814609,-9.304487,-5.209099,-6.854713,4.154507,-3.644000,0.634517,7.292124,5.366363,-1.063664,0.137239,-2.213961,6.978279,4.619836,9.641590,-0.356498,5.248666,-2.795925,6.893522,9.277662,6.403819,0.706775,4.855718,7.204528,-1.873852,7.287859,5.149827,-2.678973,-7.134516,7.154822,3.017618,-7.400231,-2.902021,-1.273769,2.896246,-2.708142,9.141747,4.945801,2.405463,-0.282464,3.921961,7.591182,4.842975,8.517345,7.145128,8.993260,0.150564,-2.200582,-3.206757,0.733231,-5.879767,-3.738690,7.489986,-3.818761,-4.846391,9.090187,4.355959,-6.757243,-4.530558,-4.626707,3.825664,-3.344678,5.589220,-6.167325,1.626461,-7.337068,-5.453800,7.072224,-3.894753,-9.547889,-7.021366,-2.299159,-8.478771,3.691092,3.516510,2.227953,7.258987,7.845345,-5.863124,4.573114,7.355659,1.450833,-8.229166,-4.811818,3.466880,-7.141304,-7.236378,9.766712,4.621359,5.288381,-4.196818,7.309922,-7.830897,8.030007,9.636287,-1.480411,-4.532929,-7.154345,-8.274570,4.424504,7.880170,-2.462735,0.119861,-4.888913,-4.923851,5.946922,-4.411176,-6.046263,3.269033,1.444688,-7.579926,6.620643,-5.046302,-6.126864,-8.726697,-1.057418,5.287973,2.056822,-1.195302,8.877340,7.063762,9.350523,-2.679695,-4.529289,6.450361,-6.417981,6.853601,-1.910983,3.900357,2.714537,6.504757,1.621188,-5.564821,3.238245,-2.796713,9.625068,3.685389,-6.332874,-8.756939,8.625542,-4.357208,-2.894283,4.736374,0.702700,7.387633,5.989338,-0.386682,2.162130,1.127549,9.953699,5.807159,-7.374693,-7.578896,-9.241621,3.112496,-4.101831,2.373697,-1.096227,-0.524363,3.234342,-4.968144,-0.049687,9.009281,7.047456,-1.534711,3.391289,0.590618,-8.282942,-4.177771,-3.324704,-4.995072,5.506133,9.784203,-4.752745,-6.046197,4.137389,-9.616418,1.661759,8.418975,9.051862,-1.560736,-7.659280,-3.436773,3.584476,9.232863,-0.187372,-9.875618,-7.229197,5.086373,3.682144,-2.156168,-2.235587,-1.392673,6.038827,-7.049613,2.399066,4.457213,-2.807777,-4.005574,-0.148984,-1.904575,7.303422,-9.673167,-3.143564,6.577254,9.432979,9.358244,-4.371366,-2.737127,8.398687,-9.045930,4.526605,-7.967645,1.532697,5.497471,9.220475,5.820059,-2.032259,-0.244361,4.214451,0.766405,1.366703,1.763571,-0.764798,9.724516,-8.029159,4.267749,7.738080,-1.922572,-0.474884,-5.148971,0.605877,7.720253,-3.207901,-5.119892,7.229387,-3.144968,-5.301854,-9.722714,9.158514,4.140638,-8.588032,7.529369,-8.563649,-9.488911,8.706810,-1.246537,-4.584226,6.836648,7.254676,6.761651,1.693409,-5.762258,9.404213,-0.573845,-3.811738,-7.702870,-6.803365,5.575593,6.912500,-3.636002,-4.742985,7.220361,-6.918834,0.985060,9.545627,-4.234454,3.528097,-8.170531,2.929862,4.159077,-0.302453,-8.256615,-7.682726,-9.049485,-3.809135,-9.039176,4.369944,2.664215,-9.022835,-6.942302,9.661558,-8.280667,2.748050,4.563489,-8.944973,-1.299104,3.647038,2.264503,-9.786383,7.272681,-7.589959,-4.409813,-5.254136,0.617082,-9.771078,-5.841879,-0.042228,-2.518217,0.201336,9.389090,8.390064,3.536886,-4.248749,-7.398231,-5.902807,9.138064,2.582330,-7.190621,-2.073711,6.189019,9.557759,-4.463647,-8.461966,8.593681,9.833795,0.312230,9.146785,6.033776,-1.865641,-1.484160,1.273113,7.814681,4.795032,-7.917505,-2.722385,9.445703,1.787300,7.422240,-8.626183,-3.003141,1.238338,-7.702455,-2.677300,8.016705,4.523657,6.350615,2.966497,-5.536284,-6.675581,-9.523550,-6.863818,3.656369,-0.215721,0.093224,1.650288,-0.824524,-0.882109,5.322424,-0.853166,2.208759,4.485907,-3.865620,6.599048,3.333797,-5.058772,-7.829173,9.913377,-3.876602,3.532641,6.810828,4.622552,6.710819,-6.818546,-6.638949,5.276473,5.841129,-7.853856,-1.871055,-7.241304,-2.758042,3.903330,7.087411,-1.097848,-6.509547,4.648455,-2.010945,1.228798,-1.433502,0.801391,-7.325854,-0.728443,1.658183,-3.345299,0.183283,5.613790,0.815114,-1.288801,-3.100046,-6.178640,-5.897622,-8.605760,1.834376,5.871257,5.445849,-8.757596,7.558459,9.992212,-0.973380,-1.751332,-5.428129,8.341755,9.710723,-3.066795,-8.232641,-4.625828,7.209004,7.044115,8.809877,-4.498081,0.928691,-4.494909,-8.572018,6.661470,5.428826,-7.418733,-0.191258,3.448054,1.519036,1.300084,2.583850,9.118284,-9.102388,0.056232,3.569685,-8.769348,-8.401083,3.093905,2.668482,4.948041,5.769198,-0.777773,2.611242,1.382874,-3.479026,-4.943159,-1.765148,-7.568990,3.229441,-3.107126,2.649483,9.233007,-9.141125,-8.291346,-5.712714,-8.109484,0.249599,4.720677,4.450914,-1.891082,3.754843], dtype = "float64")#candidate|2629|(1820,)|const|float64
call_2627 = relay.TupleGetItem(func_1396_call(relay.reshape(const_2628.astype('float64'), [600,]), relay.reshape(const_2629.astype('float64'), [10, 14, 13]), relay.reshape(const_2629.astype('float64'), [10, 14, 13]), ), 2)
call_2630 = relay.TupleGetItem(func_1401_call(relay.reshape(const_2628.astype('float64'), [600,]), relay.reshape(const_2629.astype('float64'), [10, 14, 13]), relay.reshape(const_2629.astype('float64'), [10, 14, 13]), ), 2)
func_1188_call = mod.get_global_var('func_1188')
func_1190_call = mutated_mod.get_global_var('func_1190')
call_2634 = func_1188_call()
call_2635 = func_1188_call()
uop_2638 = relay.acos(uop_2623.astype('float64')) # shape=(4, 9, 5)
func_2324_call = mod.get_global_var('func_2324')
func_2326_call = mutated_mod.get_global_var('func_2326')
call_2645 = relay.TupleGetItem(func_2324_call(), 0)
call_2646 = relay.TupleGetItem(func_2326_call(), 0)
output = relay.Tuple([uop_2625,call_2627,const_2628,const_2629,call_2634,uop_2638,call_2645,])
output2 = relay.Tuple([uop_2625,call_2630,const_2628,const_2629,call_2635,uop_2638,call_2646,])
func_2647 = relay.Function([var_2622,], output)
mod['func_2647'] = func_2647
mod = relay.transform.InferType()(mod)
mutated_mod['func_2647'] = func_2647
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2648 = relay.var("var_2648", dtype = "float32", shape = (4, 9, 5))#candidate|2648|(4, 9, 5)|var|float32
func_2647_call = mutated_mod.get_global_var('func_2647')
call_2649 = func_2647_call(var_2648)
output = call_2649
func_2650 = relay.Function([var_2648], output)
mutated_mod['func_2650'] = func_2650
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2658 = relay.const([[[4.366543,-6.383511,-7.479175,-2.984635,-8.617533,1.856644],[8.640405,-1.603879,-1.001711,-2.076356,-2.986520,5.014695],[1.452229,-9.381186,-9.351253,2.068107,9.844806,3.037875],[3.077881,-5.032579,-8.440546,-9.152615,5.612516,6.643909],[-5.578324,3.524177,-6.659016,-4.178235,0.310421,-5.322637],[-7.810071,0.196817,3.860613,0.409332,-8.992994,-5.838022],[3.825358,7.476004,1.348046,-5.243409,-4.310612,7.759991],[-0.015075,-8.086823,-2.767515,4.480795,-0.835694,-5.796095],[-6.609465,-3.187473,5.927938,9.434084,6.330167,-4.946082],[-6.611204,-2.762878,-8.296093,8.379572,2.019799,-9.522796],[-7.608615,-8.408984,-1.406283,6.751455,2.734292,4.422973]],[[-2.358119,7.612789,4.381342,4.669459,0.565971,-8.122026],[4.097191,-5.537158,0.976745,-8.939515,3.739263,-9.134943],[1.705174,-2.225314,0.714906,1.090141,-4.403775,-4.175725],[-5.783142,3.046413,8.948991,2.901134,-4.685067,-6.088629],[-8.892655,3.530642,3.425343,2.252285,7.666363,3.122604],[-7.901791,8.696682,-5.864977,-9.302950,6.871855,-0.940747],[-5.929650,7.685439,4.554845,-7.200897,-8.665795,5.332924],[-2.625533,-8.528177,-3.598643,-1.010630,-9.318168,-7.451814],[6.045342,-8.786140,-5.802917,-7.850439,-3.578721,1.979847],[8.579483,-9.879328,-6.124752,6.736078,-4.577101,-5.866618],[-6.703476,1.503551,-8.329027,1.816776,3.175243,-3.240387]],[[-5.517307,-7.078110,-3.918785,-1.533974,0.739888,5.034740],[9.774410,-1.568350,-7.946187,-5.786441,-2.028554,-7.933103],[8.631996,-0.887844,6.615326,0.302219,5.842172,-0.614892],[1.582087,1.196832,1.810260,-7.662391,-3.353851,4.573548],[-1.113650,8.521410,4.577011,5.949905,4.563399,4.848006],[0.233166,-0.026999,-3.842784,-8.479351,5.274327,4.888542],[1.117380,7.921443,-8.018683,-3.744155,8.271199,6.784170],[3.785827,8.495005,0.939481,8.936225,9.701962,1.913060],[7.142215,-7.692758,-0.788843,8.174397,0.278150,4.629952],[2.132645,-0.018317,0.122711,-7.302210,9.822855,2.103373],[-6.217396,7.807422,-7.100869,-6.011582,-7.180631,-1.996555]],[[-8.983443,-4.358896,1.339043,4.788191,-2.435567,0.468458],[-5.415261,-9.595627,0.652936,-7.088000,0.745044,-6.598662],[-2.884959,7.972137,0.185069,4.194568,5.971431,7.430503],[9.993432,-2.859063,6.674312,6.851911,6.420840,5.551799],[9.321919,-4.417786,9.172216,-8.519107,9.537435,-6.085466],[-6.511044,-8.726613,-1.210153,-1.468684,4.887065,8.066277],[-6.439304,-8.617568,-0.560008,-0.939990,4.212021,-5.182461],[5.128766,-6.587141,-2.047436,2.740542,8.651513,6.001199],[-1.192759,5.771839,-9.494439,-2.744767,-0.431869,-5.941763],[-9.141496,-4.612772,6.665739,-8.800681,-6.259882,-1.193955],[0.320310,8.692915,4.381539,-7.858754,-0.806693,8.054632]],[[-9.314116,9.380700,-6.668711,-4.764535,-7.208463,-3.745352],[1.129688,6.515905,-1.174882,0.028648,5.773187,-5.056466],[0.561291,-6.533834,-3.354332,-6.054581,7.607018,0.425607],[3.609030,-7.536636,8.673508,4.555625,0.174404,-1.719867],[-6.964898,-4.088874,-1.745496,5.488794,7.796011,1.603903],[9.163608,8.595881,5.794988,4.893848,-9.940616,-8.952336],[-6.055008,-9.841849,-1.314385,9.691595,-3.237979,3.780644],[-2.320779,-1.348978,-4.606633,-1.575137,3.509059,7.106951],[-7.426811,4.929868,-3.775736,-8.907457,-5.741711,5.550229],[8.274255,2.493849,-1.438177,-8.582861,1.857925,-7.865989],[-3.364173,-0.725845,-7.761522,-4.925510,-3.339573,5.254733]],[[-8.611666,3.872152,0.182350,7.840301,-4.218660,-6.876091],[0.463860,8.309512,-6.040419,6.739560,-4.693626,-2.032904],[7.651390,-9.629657,3.990265,-7.247598,0.122187,-4.910252],[-0.282160,-9.157016,-0.631467,0.554900,8.812150,0.997259],[3.486209,2.436403,-7.522940,-8.381804,-3.744466,1.466456],[0.744067,6.649285,6.704167,9.766961,-2.279180,-4.525733],[-2.474978,-1.848512,8.424453,1.915600,-2.245482,-0.891571],[6.678308,-7.176569,2.039385,1.292399,-1.501664,-6.770994],[-7.338884,7.114408,3.839441,2.505803,-2.998860,5.188760],[5.421171,-7.113731,7.505587,-2.675412,9.283438,8.951098],[-6.252412,1.467691,1.646739,3.796963,3.631216,-8.460551]],[[-9.809219,7.514240,-0.396726,-4.945491,0.603507,3.583387],[-1.431052,5.063013,8.696158,-0.487688,4.516064,-9.946053],[6.292697,-2.509365,-8.275091,5.661172,5.792359,9.737072],[-3.880683,0.880393,-8.986703,-5.197288,8.978901,1.366503],[-3.992308,-0.528311,5.050736,3.356435,-5.033569,-6.062260],[-6.393328,-9.105559,-2.823207,9.316016,1.925582,-0.024470],[-0.805476,-7.789661,7.513402,-3.458209,-0.245429,0.516969],[7.115443,-2.822255,7.448824,-6.338273,9.381380,5.750751],[5.643575,-4.892995,0.919737,-9.544596,4.004334,6.732757],[-3.535571,4.913392,6.678943,3.272070,4.543479,-2.383856],[-6.749141,-9.549439,1.048618,3.818483,8.301993,-8.499902]],[[-2.945669,-4.243480,6.258530,-1.729066,6.756180,-8.940880],[4.997985,6.972079,-0.027212,5.808668,-9.182910,-9.835944],[7.857550,-7.554823,9.214199,2.213405,-7.655261,7.040918],[-6.173749,5.549404,2.497488,-0.531264,2.327619,0.032596],[6.441614,-1.934816,3.544046,-1.737606,-6.841265,4.666560],[3.475880,-9.181972,-5.508928,7.759441,2.362752,-4.823020],[4.491606,6.732311,-4.083529,-3.495370,6.904448,6.767174],[1.950482,6.877416,4.467051,2.332051,-4.191115,-2.920511],[5.198597,0.918477,-4.002733,-5.419446,-7.053459,5.279877],[-4.319926,-5.956433,-1.183112,-0.630095,5.616206,-9.929682],[-1.852434,7.476029,9.161833,9.199593,-1.659858,4.465917]],[[-2.942844,-9.603117,-7.389472,5.983688,8.684492,-6.670917],[-8.948342,6.811997,9.940643,-5.750683,9.382958,-2.139712],[3.264357,8.135941,-8.850647,-0.431647,-6.030454,7.915154],[-0.949045,-0.768505,-9.241281,-3.479566,2.871920,8.989766],[0.768131,7.745140,7.159494,0.572941,2.232302,-4.426649],[9.984209,8.294085,9.843462,-0.314659,2.796237,8.318420],[-6.349073,-9.265633,7.931572,-9.647966,2.144847,1.807052],[3.011900,0.003914,-5.229847,-5.985071,4.567858,5.255086],[-1.487482,-6.717544,-9.017883,1.395898,6.387709,2.666480],[0.115283,2.674671,1.747018,-9.004894,0.546488,5.561375],[3.467170,-8.928330,2.826829,-9.520187,1.749646,-6.815206]],[[-1.308313,-3.726827,7.260829,3.557253,8.274821,-4.728724],[4.279194,9.920197,-7.759610,-2.115329,-9.093853,-6.300517],[6.870448,6.912381,-9.410695,-0.798087,-9.437189,-3.271295],[-2.814844,-1.584480,0.697658,-1.990298,6.169426,7.466090],[2.258929,-4.954812,-2.670337,1.000099,4.680833,9.464140],[-9.580462,-6.123718,-4.345481,8.056733,-8.562416,2.628917],[-9.866806,4.395435,4.471226,5.644769,-7.482018,3.640048],[6.904338,-7.555008,0.049205,-0.908310,-9.515191,-4.633153],[3.759083,9.823019,-2.403391,9.490721,1.567870,-6.895982],[-3.088784,7.764808,2.948218,7.435615,9.146822,4.755352],[3.070399,4.793743,2.641517,7.740575,0.490200,-6.146165]],[[2.598974,-5.457878,-0.704570,2.383305,-0.130168,-9.296926],[9.030008,-3.826970,4.868416,-9.652814,2.148962,-9.968452],[3.522040,-5.152028,2.707642,-9.349358,-9.234304,4.819925],[-6.376548,8.989472,2.639889,-8.658971,-4.430435,8.606206],[0.383654,-9.595935,3.622794,2.385587,-2.633780,6.060866],[-4.753418,-8.074304,-4.907351,-5.373555,4.477831,-0.467091],[5.894730,5.269645,9.928607,3.532753,-3.394052,-7.915639],[8.442791,2.425245,3.833943,4.351736,-7.847148,-2.149550],[7.286106,0.862339,8.823939,7.998061,4.345361,-8.631595],[1.551913,1.377936,3.492915,-1.884505,8.737787,3.553865],[-6.888800,-3.463975,-1.657939,-4.799189,3.175137,-4.446892]],[[2.515508,4.869808,5.592629,8.992579,-6.337798,-5.504626],[-3.700351,-0.564241,-6.351940,-7.443047,-8.245371,-4.967751],[-2.564124,-7.604821,-6.666340,-1.310372,-3.921508,-4.438390],[3.054703,-0.045863,-5.394339,0.112917,7.081495,-5.194522],[9.867293,0.450117,-1.145166,7.490966,-2.604290,-5.861635],[-1.082742,-6.434501,0.841527,-4.215131,-4.992604,-9.599679],[-4.164164,-0.897337,6.739929,5.682326,4.789341,-3.813822],[-3.962585,-7.061899,9.675295,-3.438677,3.349154,-6.634236],[4.405661,6.273929,8.407169,8.888817,-7.314064,-7.905107],[-6.891123,-2.089079,-9.009475,0.782875,-0.373696,4.164559],[3.247059,-8.672067,-9.494002,7.149804,2.586533,0.430914]],[[-7.128378,-5.525850,-9.512824,-4.565743,9.006258,4.305275],[1.990903,-7.392955,-4.443290,9.052708,4.917580,4.240249],[-9.788344,-4.306868,0.835018,-0.211097,-9.128360,-8.355001],[8.691657,6.311389,-9.369883,-0.320482,-6.756657,9.235187],[-7.386817,-2.889906,-5.581705,6.586999,-6.957979,5.238443],[-8.388386,7.389522,-8.335662,5.717278,-8.657203,-2.459800],[1.736104,-0.101904,-8.763571,4.672678,-6.108711,-0.556515],[2.368021,6.712828,9.483420,3.167230,-9.073093,-9.875259],[7.137502,3.135348,3.244045,-8.397844,-7.759509,-2.837775],[-4.562296,-6.222485,7.022747,-0.283048,-5.267549,-7.421846],[-1.796516,8.392927,-8.399030,8.341120,-9.700929,6.149419]],[[9.482439,-4.376228,-5.721828,-2.635632,-4.755637,5.445210],[6.326395,-8.602930,0.226937,-8.346943,7.818243,-7.883948],[0.815450,0.345807,-6.438964,6.951236,-9.037513,-5.450265],[-1.289798,9.344672,2.690120,-6.400544,-2.849213,-6.807138],[1.014697,5.482548,4.269403,-8.739371,-0.128327,-5.783898],[-1.898728,-5.798689,1.051046,6.814755,4.292759,4.364721],[4.533200,6.033540,-2.313109,4.426154,-4.182704,-6.847905],[9.400681,3.362262,-1.893597,-1.472497,3.521179,9.615139],[4.596666,8.406583,-6.695938,6.229923,-1.871963,8.516110],[3.313261,0.076447,-7.641304,7.487602,-3.169420,1.262346],[-8.651740,-0.256506,-2.488361,-8.955145,-1.820602,-2.839750]],[[-5.269411,7.051170,-0.729534,-3.033708,6.222105,-9.967791],[7.618959,7.618497,-5.003921,5.569163,2.888457,-3.079933],[3.937605,5.151155,-8.609127,-7.168063,-3.731868,-3.515039],[6.386992,-2.569398,-8.567583,-7.251074,-1.110549,2.092285],[-8.749223,7.240144,-6.177609,8.797893,-9.024416,-4.704825],[-8.510347,-9.193767,-0.605114,6.166549,4.591980,-2.410756],[-4.653798,4.036975,2.373360,0.127413,3.187607,0.306553],[6.538730,-0.036141,5.876580,-3.667104,2.838905,-8.265148],[9.137273,6.915890,0.129741,-6.522549,-5.751390,-3.892984],[0.917537,7.805416,-9.386810,-1.343541,2.366220,-8.173146],[3.588436,-2.971517,4.043153,-0.115919,3.020484,2.639002]]], dtype = "float32")#candidate|2658|(15, 11, 6)|const|float32
uop_2659 = relay.atan(const_2658.astype('float32')) # shape=(15, 11, 6)
output = relay.Tuple([uop_2659,])
output2 = relay.Tuple([uop_2659,])
func_2679 = relay.Function([], output)
mod['func_2679'] = func_2679
mod = relay.transform.InferType()(mod)
mutated_mod['func_2679'] = func_2679
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2679_call = mutated_mod.get_global_var('func_2679')
call_2680 = func_2679_call()
output = call_2680
func_2681 = relay.Function([], output)
mutated_mod['func_2681'] = func_2681
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1120_call = mod.get_global_var('func_1120')
func_1122_call = mutated_mod.get_global_var('func_1122')
call_2692 = relay.TupleGetItem(func_1120_call(), 0)
call_2693 = relay.TupleGetItem(func_1122_call(), 0)
var_2703 = relay.var("var_2703", dtype = "float64", shape = (10, 14, 13))#candidate|2703|(10, 14, 13)|var|float64
bop_2704 = relay.multiply(call_2692.astype('float64'), relay.reshape(var_2703.astype('float64'), relay.shape_of(call_2692))) # shape=(10, 14, 13)
bop_2707 = relay.multiply(call_2693.astype('float64'), relay.reshape(var_2703.astype('float64'), relay.shape_of(call_2693))) # shape=(10, 14, 13)
func_1300_call = mod.get_global_var('func_1300')
func_1302_call = mutated_mod.get_global_var('func_1302')
call_2712 = relay.TupleGetItem(func_1300_call(), 0)
call_2713 = relay.TupleGetItem(func_1302_call(), 0)
func_1530_call = mod.get_global_var('func_1530')
func_1534_call = mutated_mod.get_global_var('func_1534')
const_2727 = relay.const([5,-7,-7,-8,-3,-2,-8,3,-1,-3,-1,-1,5,-7], dtype = "uint8")#candidate|2727|(14,)|const|uint8
var_2728 = relay.var("var_2728", dtype = "uint8", shape = (112,))#candidate|2728|(112,)|var|uint8
var_2729 = relay.var("var_2729", dtype = "uint8", shape = (35, 4))#candidate|2729|(35, 4)|var|uint8
call_2726 = relay.TupleGetItem(func_1530_call(relay.reshape(const_2727.astype('uint8'), [2, 7, 1]), relay.reshape(var_2728.astype('uint8'), [2, 7, 8]), relay.reshape(var_2729.astype('uint8'), [2, 7, 10]), ), 0)
call_2730 = relay.TupleGetItem(func_1534_call(relay.reshape(const_2727.astype('uint8'), [2, 7, 1]), relay.reshape(var_2728.astype('uint8'), [2, 7, 8]), relay.reshape(var_2729.astype('uint8'), [2, 7, 10]), ), 0)
output = relay.Tuple([bop_2704,call_2712,call_2726,const_2727,var_2728,var_2729,])
output2 = relay.Tuple([bop_2707,call_2713,call_2730,const_2727,var_2728,var_2729,])
func_2736 = relay.Function([var_2703,var_2728,var_2729,], output)
mod['func_2736'] = func_2736
mod = relay.transform.InferType()(mod)
var_2737 = relay.var("var_2737", dtype = "float64", shape = (10, 14, 13))#candidate|2737|(10, 14, 13)|var|float64
var_2738 = relay.var("var_2738", dtype = "uint8", shape = (112,))#candidate|2738|(112,)|var|uint8
var_2739 = relay.var("var_2739", dtype = "uint8", shape = (35, 4))#candidate|2739|(35, 4)|var|uint8
output = func_2736(var_2737,var_2738,var_2739,)
func_2740 = relay.Function([var_2737,var_2738,var_2739,], output)
mutated_mod['func_2740'] = func_2740
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2324_call = mod.get_global_var('func_2324')
func_2326_call = mutated_mod.get_global_var('func_2326')
call_2752 = relay.TupleGetItem(func_2324_call(), 0)
call_2753 = relay.TupleGetItem(func_2326_call(), 0)
output = relay.Tuple([call_2752,])
output2 = relay.Tuple([call_2753,])
func_2760 = relay.Function([], output)
mod['func_2760'] = func_2760
mod = relay.transform.InferType()(mod)
output = func_2760()
func_2761 = relay.Function([], output)
mutated_mod['func_2761'] = func_2761
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2760_call = mod.get_global_var('func_2760')
func_2761_call = mutated_mod.get_global_var('func_2761')
call_2864 = relay.TupleGetItem(func_2760_call(), 0)
call_2865 = relay.TupleGetItem(func_2761_call(), 0)
output = call_2864
output2 = call_2865
func_2866 = relay.Function([], output)
mod['func_2866'] = func_2866
mod = relay.transform.InferType()(mod)
output = func_2866()
func_2867 = relay.Function([], output)
mutated_mod['func_2867'] = func_2867
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2212_call = mod.get_global_var('func_2212')
func_2214_call = mutated_mod.get_global_var('func_2214')
call_2924 = func_2212_call()
call_2925 = func_2212_call()
output = relay.Tuple([call_2924,])
output2 = relay.Tuple([call_2925,])
func_2947 = relay.Function([], output)
mod['func_2947'] = func_2947
mod = relay.transform.InferType()(mod)
mutated_mod['func_2947'] = func_2947
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2947_call = mutated_mod.get_global_var('func_2947')
call_2948 = func_2947_call()
output = call_2948
func_2949 = relay.Function([], output)
mutated_mod['func_2949'] = func_2949
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1686_call = mod.get_global_var('func_1686')
func_1688_call = mutated_mod.get_global_var('func_1688')
call_3011 = func_1686_call()
call_3012 = func_1686_call()
output = relay.Tuple([call_3011,])
output2 = relay.Tuple([call_3012,])
func_3024 = relay.Function([], output)
mod['func_3024'] = func_3024
mod = relay.transform.InferType()(mod)
output = func_3024()
func_3025 = relay.Function([], output)
mutated_mod['func_3025'] = func_3025
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3042 = relay.var("var_3042", dtype = "uint8", shape = ())#candidate|3042|()|var|uint8
const_3043 = relay.const([[[-5,-6,4,-4,8,-3,-7],[-9,5,9,-6,1,-8,10],[-9,9,6,4,1,-2,9],[2,-6,4,4,3,4,9],[5,3,2,7,-9,-10,6],[-9,-7,3,-1,-7,10,6],[1,5,5,-9,10,-9,-4],[7,-10,7,7,-3,6,-3],[9,2,5,6,-5,-8,-9]],[[-2,-5,5,7,-5,1,-3],[9,7,5,7,-7,9,8],[-5,-2,9,9,-3,5,3],[9,7,1,-7,3,4,7],[-2,-9,-1,7,8,-4,-4],[-10,-7,10,6,-7,-6,7],[2,5,10,-2,-7,-10,7],[-6,3,6,3,-3,7,-4],[-10,-7,6,6,-8,-4,9]],[[9,-8,-5,-9,10,-8,2],[10,-10,-6,3,-1,-7,-9],[-1,7,-4,-5,7,-1,7],[-9,-7,-5,-1,6,-5,5],[5,5,2,-5,8,-7,-5],[9,8,-3,6,3,-2,-1],[7,9,10,7,-5,-8,4],[7,4,3,3,-8,-5,8],[2,-2,-5,-1,6,-7,-10]],[[-5,2,6,-7,7,-5,1],[-8,5,6,8,-2,-8,-7],[-9,-4,3,-6,10,-6,-3],[4,10,1,-1,-5,-2,-8],[-5,-7,-3,-1,-5,-5,-10],[3,-3,7,8,-1,7,-8],[2,9,-4,-4,-5,3,-1],[6,9,-5,6,-8,-10,-5],[-4,5,-10,5,-9,1,3]],[[-4,2,8,-9,4,6,2],[-10,4,10,9,-4,-6,-3],[-8,10,-3,-4,-4,5,-8],[9,-9,-7,-2,-4,10,3],[-10,-2,-3,2,3,-8,-7],[-4,-5,9,3,-7,-4,3],[-9,-10,5,9,2,-5,-5],[1,-5,1,9,4,-5,-6],[1,2,10,-9,4,2,-7]],[[-1,9,8,-9,3,-8,-2],[7,-1,9,-8,-7,-1,-7],[7,9,8,-3,3,-5,10],[3,-4,9,-9,-3,5,-8],[-1,1,-8,-7,10,5,2],[8,-1,3,1,5,10,1],[-7,4,-3,-7,7,9,6],[9,-4,-9,9,-2,-5,4],[-4,3,-3,9,-1,-5,2]],[[4,-8,3,1,6,-5,-2],[-7,8,-1,-3,5,8,-10],[-4,9,-10,4,-10,7,-7],[-4,5,-7,-3,3,3,-9],[5,8,-4,9,5,-5,-8],[-10,-7,6,-8,-6,-3,8],[-6,-9,-8,2,5,4,-5],[-6,5,8,2,5,-8,10],[9,-7,7,-8,4,-9,-9]],[[10,5,-7,-2,2,2,2],[8,1,-4,-2,6,-7,8],[-1,10,3,9,-4,6,5],[-3,7,-10,7,-5,-6,1],[-3,-1,5,8,-7,-9,-6],[-6,2,9,-1,6,-3,-10],[-3,-2,7,-1,-5,2,5],[-4,6,-3,1,6,1,1],[4,-4,-10,3,10,-2,4]],[[8,7,2,1,-2,7,4],[1,-3,7,-3,-4,6,2],[-10,6,-8,9,6,7,-2],[-9,4,4,-6,3,-7,6],[10,3,-6,7,10,6,-5],[8,-7,6,7,-9,10,-10],[8,2,4,5,2,4,5],[2,2,7,-6,-3,2,4],[1,-9,-10,6,-6,-1,-2]],[[-2,4,-8,3,6,-10,-2],[10,-4,-2,1,-4,5,7],[-8,-3,-7,-6,5,-10,-9],[-1,-3,-9,-1,2,2,-8],[-7,4,-3,8,6,-5,-3],[4,-7,5,6,-9,-2,1],[-6,-2,4,-8,5,-7,10],[-3,-8,5,2,7,3,-4],[-6,8,4,5,-5,6,-9]]], dtype = "uint8")#candidate|3043|(10, 9, 7)|const|uint8
bop_3044 = relay.bitwise_and(var_3042.astype('uint8'), const_3043.astype('uint8')) # shape=(10, 9, 7)
func_1066_call = mod.get_global_var('func_1066')
func_1068_call = mutated_mod.get_global_var('func_1068')
call_3055 = relay.TupleGetItem(func_1066_call(), 0)
call_3056 = relay.TupleGetItem(func_1068_call(), 0)
output = relay.Tuple([bop_3044,call_3055,])
output2 = relay.Tuple([bop_3044,call_3056,])
func_3062 = relay.Function([var_3042,], output)
mod['func_3062'] = func_3062
mod = relay.transform.InferType()(mod)
mutated_mod['func_3062'] = func_3062
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3063 = relay.var("var_3063", dtype = "uint8", shape = ())#candidate|3063|()|var|uint8
func_3062_call = mutated_mod.get_global_var('func_3062')
call_3064 = func_3062_call(var_3063)
output = call_3064
func_3065 = relay.Function([var_3063], output)
mutated_mod['func_3065'] = func_3065
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3067 = relay.var("var_3067", dtype = "uint32", shape = ())#candidate|3067|()|var|uint32
const_3068 = relay.const([[[7],[9],[-8],[3],[7],[3],[9]]], dtype = "uint32")#candidate|3068|(1, 7, 1)|const|uint32
bop_3069 = relay.multiply(var_3067.astype('uint32'), const_3068.astype('uint32')) # shape=(1, 7, 1)
bop_3072 = relay.add(bop_3069.astype('int64'), relay.reshape(const_3068.astype('int64'), relay.shape_of(bop_3069))) # shape=(1, 7, 1)
func_1686_call = mod.get_global_var('func_1686')
func_1688_call = mutated_mod.get_global_var('func_1688')
call_3085 = func_1686_call()
call_3086 = func_1686_call()
func_1188_call = mod.get_global_var('func_1188')
func_1190_call = mutated_mod.get_global_var('func_1190')
call_3097 = func_1188_call()
call_3098 = func_1188_call()
func_2736_call = mod.get_global_var('func_2736')
func_2740_call = mutated_mod.get_global_var('func_2740')
var_3101 = relay.var("var_3101", dtype = "uint8", shape = (28, 4))#candidate|3101|(28, 4)|var|uint8
var_3102 = relay.var("var_3102", dtype = "uint8", shape = (140,))#candidate|3102|(140,)|var|uint8
call_3100 = relay.TupleGetItem(func_2736_call(relay.reshape(call_3085.astype('float64'), [10, 14, 13]), relay.reshape(var_3101.astype('uint8'), [112,]), relay.reshape(var_3102.astype('uint8'), [35, 4]), ), 0)
call_3103 = relay.TupleGetItem(func_2740_call(relay.reshape(call_3085.astype('float64'), [10, 14, 13]), relay.reshape(var_3101.astype('uint8'), [112,]), relay.reshape(var_3102.astype('uint8'), [35, 4]), ), 0)
var_3109 = relay.var("var_3109", dtype = "uint8", shape = (140,))#candidate|3109|(140,)|var|uint8
bop_3110 = relay.multiply(var_3102.astype('int8'), relay.reshape(var_3109.astype('int8'), relay.shape_of(var_3102))) # shape=(140,)
bop_3113 = relay.divide(bop_3110.astype('float64'), bop_3069.astype('float64')) # shape=(1, 7, 140)
func_1634_call = mod.get_global_var('func_1634')
func_1636_call = mutated_mod.get_global_var('func_1636')
call_3116 = relay.TupleGetItem(func_1634_call(), 2)
call_3117 = relay.TupleGetItem(func_1636_call(), 2)
func_1188_call = mod.get_global_var('func_1188')
func_1190_call = mutated_mod.get_global_var('func_1190')
call_3118 = func_1188_call()
call_3119 = func_1188_call()
uop_3125 = relay.asinh(const_3068.astype('float32')) # shape=(1, 7, 1)
func_1873_call = mod.get_global_var('func_1873')
func_1875_call = mutated_mod.get_global_var('func_1875')
call_3134 = relay.TupleGetItem(func_1873_call(), 0)
call_3135 = relay.TupleGetItem(func_1875_call(), 0)
output = relay.Tuple([bop_3072,call_3085,call_3097,call_3100,var_3101,bop_3113,call_3116,call_3118,uop_3125,call_3134,])
output2 = relay.Tuple([bop_3072,call_3086,call_3098,call_3103,var_3101,bop_3113,call_3117,call_3119,uop_3125,call_3135,])
func_3143 = relay.Function([var_3067,var_3101,var_3102,var_3109,], output)
mod['func_3143'] = func_3143
mod = relay.transform.InferType()(mod)
mutated_mod['func_3143'] = func_3143
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3143_call = mutated_mod.get_global_var('func_3143')
var_3145 = relay.var("var_3145", dtype = "uint32", shape = ())#candidate|3145|()|var|uint32
var_3146 = relay.var("var_3146", dtype = "uint8", shape = (28, 4))#candidate|3146|(28, 4)|var|uint8
var_3147 = relay.var("var_3147", dtype = "uint8", shape = (140,))#candidate|3147|(140,)|var|uint8
var_3148 = relay.var("var_3148", dtype = "uint8", shape = (140,))#candidate|3148|(140,)|var|uint8
call_3144 = func_3143_call(var_3145,var_3146,var_3147,var_3148,)
output = call_3144
func_3149 = relay.Function([var_3145,var_3146,var_3147,var_3148,], output)
mutated_mod['func_3149'] = func_3149
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2760_call = mod.get_global_var('func_2760')
func_2761_call = mutated_mod.get_global_var('func_2761')
call_3180 = relay.TupleGetItem(func_2760_call(), 0)
call_3181 = relay.TupleGetItem(func_2761_call(), 0)
output = call_3180
output2 = call_3181
func_3183 = relay.Function([], output)
mod['func_3183'] = func_3183
mod = relay.transform.InferType()(mod)
mutated_mod['func_3183'] = func_3183
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3183_call = mutated_mod.get_global_var('func_3183')
call_3184 = func_3183_call()
output = call_3184
func_3185 = relay.Function([], output)
mutated_mod['func_3185'] = func_3185
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2760_call = mod.get_global_var('func_2760')
func_2761_call = mutated_mod.get_global_var('func_2761')
call_3186 = relay.TupleGetItem(func_2760_call(), 0)
call_3187 = relay.TupleGetItem(func_2761_call(), 0)
output = call_3186
output2 = call_3187
func_3188 = relay.Function([], output)
mod['func_3188'] = func_3188
mod = relay.transform.InferType()(mod)
output = func_3188()
func_3189 = relay.Function([], output)
mutated_mod['func_3189'] = func_3189
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3024_call = mod.get_global_var('func_3024')
func_3025_call = mutated_mod.get_global_var('func_3025')
call_3211 = relay.TupleGetItem(func_3024_call(), 0)
call_3212 = relay.TupleGetItem(func_3025_call(), 0)
output = call_3211
output2 = call_3212
func_3214 = relay.Function([], output)
mod['func_3214'] = func_3214
mod = relay.transform.InferType()(mod)
output = func_3214()
func_3215 = relay.Function([], output)
mutated_mod['func_3215'] = func_3215
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2947_call = mod.get_global_var('func_2947')
func_2949_call = mutated_mod.get_global_var('func_2949')
call_3218 = relay.TupleGetItem(func_2947_call(), 0)
call_3219 = relay.TupleGetItem(func_2949_call(), 0)
output = call_3218
output2 = call_3219
func_3222 = relay.Function([], output)
mod['func_3222'] = func_3222
mod = relay.transform.InferType()(mod)
output = func_3222()
func_3223 = relay.Function([], output)
mutated_mod['func_3223'] = func_3223
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2866_call = mod.get_global_var('func_2866')
func_2867_call = mutated_mod.get_global_var('func_2867')
call_3232 = func_2866_call()
call_3233 = func_2866_call()
output = relay.Tuple([call_3232,])
output2 = relay.Tuple([call_3233,])
func_3234 = relay.Function([], output)
mod['func_3234'] = func_3234
mod = relay.transform.InferType()(mod)
mutated_mod['func_3234'] = func_3234
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3234_call = mutated_mod.get_global_var('func_3234')
call_3235 = func_3234_call()
output = call_3235
func_3236 = relay.Function([], output)
mutated_mod['func_3236'] = func_3236
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2866_call = mod.get_global_var('func_2866')
func_2867_call = mutated_mod.get_global_var('func_2867')
call_3262 = func_2866_call()
call_3263 = func_2866_call()
output = relay.Tuple([call_3262,])
output2 = relay.Tuple([call_3263,])
func_3268 = relay.Function([], output)
mod['func_3268'] = func_3268
mod = relay.transform.InferType()(mod)
output = func_3268()
func_3269 = relay.Function([], output)
mutated_mod['func_3269'] = func_3269
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3024_call = mod.get_global_var('func_3024')
func_3025_call = mutated_mod.get_global_var('func_3025')
call_3276 = relay.TupleGetItem(func_3024_call(), 0)
call_3277 = relay.TupleGetItem(func_3025_call(), 0)
output = call_3276
output2 = call_3277
func_3290 = relay.Function([], output)
mod['func_3290'] = func_3290
mod = relay.transform.InferType()(mod)
mutated_mod['func_3290'] = func_3290
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3290_call = mutated_mod.get_global_var('func_3290')
call_3291 = func_3290_call()
output = call_3291
func_3292 = relay.Function([], output)
mutated_mod['func_3292'] = func_3292
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3301 = relay.const([[[False,False,False,True,True,False,False,True,False,False,False,False,True],[True,False,True,True,True,True,False,False,False,False,False,True,True],[False,True,True,False,True,True,False,False,True,True,False,True,False],[True,False,False,True,True,True,False,False,True,True,True,True,True],[True,True,True,True,False,True,False,False,False,True,True,False,True],[False,False,False,False,False,True,False,True,False,True,False,False,True],[True,True,False,True,False,True,False,False,False,True,True,False,True],[True,False,False,False,True,True,False,True,True,False,False,True,True],[True,False,False,True,True,True,True,True,False,True,False,True,True]],[[True,False,True,True,True,False,True,True,False,True,False,False,False],[True,True,True,False,False,False,False,False,True,True,False,False,False],[False,False,True,True,True,False,True,False,True,False,True,True,False],[True,False,False,False,False,False,True,True,False,True,True,True,False],[True,False,False,True,True,False,True,False,False,True,False,True,True],[True,False,False,False,False,False,False,False,False,True,False,True,False],[True,False,False,False,False,True,False,False,False,True,True,False,True],[True,True,True,False,False,True,False,True,True,False,True,False,True],[True,True,True,False,True,False,False,True,False,True,False,True,True]]], dtype = "bool")#candidate|3301|(2, 9, 13)|const|bool
var_3302 = relay.var("var_3302", dtype = "bool", shape = (2, 9, 13))#candidate|3302|(2, 9, 13)|var|bool
bop_3303 = relay.logical_and(const_3301.astype('bool'), relay.reshape(var_3302.astype('bool'), relay.shape_of(const_3301))) # shape=(2, 9, 13)
func_3222_call = mod.get_global_var('func_3222')
func_3223_call = mutated_mod.get_global_var('func_3223')
call_3307 = func_3222_call()
call_3308 = func_3222_call()
bop_3315 = relay.logical_xor(const_3301.astype('int16'), relay.reshape(var_3302.astype('int16'), relay.shape_of(const_3301))) # shape=(2, 9, 13)
bop_3321 = relay.equal(const_3301.astype('bool'), relay.reshape(bop_3315.astype('bool'), relay.shape_of(const_3301))) # shape=(2, 9, 13)
func_2616_call = mod.get_global_var('func_2616')
func_2620_call = mutated_mod.get_global_var('func_2620')
const_3325 = relay.const([[-10],[1],[8],[-10],[-9],[3],[-10],[-8],[-2],[-1],[8],[9],[1],[-7],[-10],[4],[-9],[-1],[-9],[7],[8],[7],[6],[5],[4],[10],[7],[-8],[-1],[-7],[-7],[3],[8],[-2],[-7],[-4],[8],[4],[-7],[-4],[7],[5],[-1],[-10],[7],[3],[10],[9],[-2],[-6],[-7],[-3],[-4],[-8],[8],[-3],[4],[-6],[-8],[-9],[-8],[10],[-10],[10],[9],[2],[-6],[2],[-6],[2],[2],[6],[3],[3],[2],[8],[-6],[-10],[7],[-2],[-3],[2],[-3],[-3],[5],[-10],[1],[5],[10],[5],[1],[2],[2],[-6],[1],[5],[4],[5],[-4],[-4],[-4],[-7],[10],[8],[1],[-10],[9],[-2],[3],[1],[-9],[7]], dtype = "uint8")#candidate|3325|(112, 1)|const|uint8
var_3326 = relay.var("var_3326", dtype = "uint8", shape = (140,))#candidate|3326|(140,)|var|uint8
call_3324 = relay.TupleGetItem(func_2616_call(relay.reshape(const_3325.astype('uint8'), [112,]), relay.reshape(var_3326.astype('uint8'), [140,]), ), 1)
call_3327 = relay.TupleGetItem(func_2620_call(relay.reshape(const_3325.astype('uint8'), [112,]), relay.reshape(var_3326.astype('uint8'), [140,]), ), 1)
func_500_call = mod.get_global_var('func_500')
func_505_call = mutated_mod.get_global_var('func_505')
var_3350 = relay.var("var_3350", dtype = "uint64", shape = (36,))#candidate|3350|(36,)|var|uint64
var_3351 = relay.var("var_3351", dtype = "int32", shape = (126,))#candidate|3351|(126,)|var|int32
const_3352 = relay.const([-5.198387,4.749642,-6.556186,-8.417802,-9.803339,-1.964637,-4.756927,4.699758,-1.456943,-9.237349,-1.514933,-8.377335,6.263654,-0.475633,-6.994102,-0.535767,-2.341981,-9.577938,-1.594837,1.467867,-2.025039,2.649706,5.405834,9.039027,-9.656447,-2.089342,3.954908,-3.098928,-2.990358,9.260340,-7.235928,4.119406,6.050795,8.163422,7.912267,-0.227439,-1.353894,-9.073688,1.272355,-8.928643,8.418171,-9.339445,2.355225,7.074630,-0.330965,-1.578395,-0.240969,3.509987,7.162006,5.969183,1.502841,6.498082,4.622520,4.455262,0.309291,0.946778,-8.671214,6.839112,-8.152225,9.665814,5.274614,9.385351,-1.452936,5.339536,-2.580150,-9.666400,0.821783,0.002665,7.571051,7.582736,-2.966453,7.398134,-5.922771,5.806459,-9.744353,3.105594,-8.941841,7.803179,0.749566,5.485917,-1.797910,2.111607,0.743156,-4.719080,9.259299,7.774891,-2.744002,5.374456,9.312772,6.816769,6.666434,1.089179,-3.100155,-5.919733,9.179869,4.862939,9.605028,6.900662,9.966161,5.849182,2.197089,0.155921,-7.157477,5.623850,9.473143,1.410632,8.723596,-5.412303,5.409699,-1.901429,-8.212556,-9.841812,-3.378483,-5.768708,-0.907677,1.756125,-8.014307,7.609043,9.554001,-2.685014,-7.386549,1.295953,-5.497147,7.036211,8.281706,9.733034,4.511352,3.460934,2.360913,7.671393,-7.500948,-5.816700,8.150206,0.774924,-8.467137,4.112208,1.565592,-3.411627,6.294582,7.580964,8.244041,-7.671848,7.555046,8.421401,-6.702633,-3.494150,8.032623,7.065985,-5.854119,8.968482,9.551366,8.067415,3.043176,-6.266394,9.971406,5.954158,-1.063060,7.290301,-2.617750,1.694228,-8.743639,7.000397,-7.161044,-2.251626,4.918321,2.301544,2.829342,6.252241,-1.174428,6.300583,6.077181,2.630065,-9.129947,5.216917,0.290028,8.320721,-4.633070,6.286430,-0.148196,-7.781148,6.989323,-0.923664,-3.239647,1.680601,9.503332,0.406163,-5.253346,0.822902,6.534940,3.656502,2.413324,-0.050733,9.178095,-1.864504,-8.315400,4.299647,-9.477797,-5.085257,5.542390,3.255407,-4.345239,9.150676,4.688633,4.384237,-9.776714,0.840892,-3.983390,9.762142,8.304007,7.902749,-6.945170,4.041159,-6.511028,-8.596852,-2.627713,-6.149395,-4.626042,6.707213,-8.642982,-5.164746,8.246058,-2.187134,-9.326314,2.166515,8.038402,9.300804,2.452288,-2.943723,-8.931243,9.128027,9.610313,5.213206,7.210906,9.742735,2.132149,-3.842709,-1.521779,-6.079230,3.682869,-3.918729,-1.838277,-5.600244,7.905770,0.881503,4.716286,-2.366613,2.091645,-4.738760,-1.656856,-1.142567,-9.293432,-7.856344,-5.453039,9.922874,-3.160307,-7.521497,9.044844,-7.083477,-7.011591,-9.760326,-5.503861,-0.895687,-0.087597,-9.129663,-2.544633,-2.488416,-6.064296,6.807618,-3.476930,-1.552821,7.653584,0.712991,0.876268,9.425634,-1.662618,-6.721563,-5.953864,-2.643509,8.721989,0.380440,2.806874,-2.203042,-0.564370,-9.443331,-3.822532,2.543080,-2.737912,-2.238460,-6.238562,9.198214,5.157902,2.097421,-1.047279,-8.440797,-9.141238,1.457581,-6.125994,8.594508,-6.632463,5.625021,-5.001085,-4.485756,4.869045,4.065509,-7.629301,-6.651729,-0.437914,5.739818,6.549936,-3.775301,6.256299,-1.940207,-3.785500,-8.886868,5.152424,9.742283,-8.152185,-4.554124,3.932528,2.533558,-0.492218,1.184325,4.299690,7.021762,0.459214,-6.740325,-1.187361,-1.695921,0.438864,7.049722,-5.792871,-3.221983,-3.316162,-2.598101,-8.731808,7.203524,-4.595472,4.650780,7.803759,-8.365050,2.007337,5.441558,2.249656,-2.004436,-1.937064,-2.267344,-6.790888,0.627928,3.829941,-0.490536,6.771897,0.018429,4.084107,3.403229,0.920757,8.393517,-6.661018,-4.322230,-7.162315,-4.703134,-9.309591,0.326807,-9.332357,3.922455,-1.367461,2.631996,2.800756,7.309550,-9.883953,1.379787,3.893880,-4.105637,7.471401,7.937840,2.516658,-3.590622,-9.693929,-4.390804,-1.585512,8.642371,-9.408849,-5.457255,0.747081,-8.913676,-6.758602,7.022412,-1.079447,-5.370172,6.262276,4.248098,2.722345,-1.383057,8.943283,-7.262898,6.753288,-3.690746,2.585501,3.905967,1.962739,-3.248202,-7.668001,2.726485,1.005831,-9.262269,6.244722,2.943009,-1.374105,8.191338,-2.379291,8.727246,0.572655,9.355851,2.148213,9.371610,-1.211900,-2.667227,6.478033,8.435593,3.108516,9.508067,6.327929,-5.031863,9.435369,8.409336,2.561123,0.035243,4.276877,3.138489,9.374713,3.525635,-3.628170,-6.838874,3.798683,-1.303636,-4.897234,6.719535,-7.935891,9.301204,5.304435,-4.930414,1.124863,7.876120,-3.736223,0.260887,1.759726,-7.864260,5.147941,-8.701000,-5.153964,4.984336,-5.787054,0.976746,-4.618585,-4.077890,0.474342,5.955642,-6.392232,8.448377,4.264179,8.562065,0.067278,1.594580,-5.656924,3.341060,-2.657327,0.408262,-3.111909,-1.397435,3.267766,-0.217443,2.462321,-1.260749,7.485456,-6.141061,-5.267358,9.815179,8.233135,-4.963249,-4.663637,4.719397,9.699352,-7.623893,6.778891,-6.990267,2.037405,4.957368,-7.982585,6.635977,-3.382187,0.111987,4.162390,-0.957856,9.072452,-4.700505,5.238987,-2.565410,1.597913,-7.666426,6.329242,4.229957,5.518572,1.555571,-7.526333,4.304355,5.206482,-6.587080,-4.930386,5.813550,1.574157,8.161912,1.279507,5.111373,-1.923919,6.778563,1.434685,7.324722,-8.755389,-0.823529,3.159765,9.375490,-6.781697,8.956175,-9.791146,-6.307142,-5.316981,-5.042732,-4.328206,-0.852147,7.612862,-8.295763,1.158244,-4.722766,6.226349,-9.366030,-4.582584,1.493964,0.375624,6.084420,9.469532,-2.975267,-2.742085,-3.722429,-8.056655,3.004294,-5.595683,-9.678142,8.470500,3.325512,-6.193561,7.354625,8.561601,5.840875,4.094061,5.374938,8.443089,6.862436,-1.783682,-8.277146,-2.456530,1.353431,6.878705,-1.131602,-0.234416,8.401851,-8.400096,8.642088,4.324519,-0.648684,-4.678758,-0.738230,7.539530,3.580682,3.428953,4.234065,8.903439,-5.279676,-1.842516,-0.461953,1.645479,3.646784,-0.156181,2.711591,-2.224062,3.141663,7.949125,-8.289907,5.603725,7.474660,3.633578,-2.027996,4.392164,4.771716,-3.647939,-0.348092,-9.051312,3.310897,-0.749110,-8.510846,-2.037778,9.424122,9.215961,7.515664,4.556909,8.242357,8.326006,-2.137889,5.361949,-3.331405,0.350224,9.977784,5.638041,-6.663739,1.812717,-9.726683,-8.539205,-5.486926,8.687536,-0.890921,-9.120028,4.702407,-8.383478,-5.316199,4.456487,9.424637,5.931635,-6.500764,1.717614,-8.401486,-4.832505,-4.545190,7.641617,-0.597061,-2.221308,0.548520,4.317684,-1.434039,-4.932067,6.402067,-6.952532,-0.525523,3.651926,-6.324387,-5.391418,5.686856,7.150827,9.786730,-9.164472,4.340120,8.610084,1.516848,0.505241,-7.129053,-0.513535,7.363908,-6.298161,-7.685638,2.334792,-9.426504,-3.572573,-8.162020,7.059605,-3.570401,3.026285,5.965546,-3.994584,8.009565,-9.761838,-3.322770,4.655857,7.100120,2.997181,8.072743,-6.852260,-0.963872,-6.359930,-9.214929,3.513808,2.137663,-9.193435,2.651962,-0.164090,-0.888722,-6.247800,3.857928,9.844356,1.555571,0.734970,7.549721,-9.548182,-6.064304,-4.659203,-7.035976,2.927450,-0.660085,-6.159158,-5.209724,2.170929,-4.450659,2.372744,9.614840,-9.702281,-2.296496,-9.678711,-9.410908,0.935255,0.440729,1.259268,0.446832,5.529698,5.561268,2.194992,-4.151659,-5.371785,-9.358081,9.568387,-6.535156,-8.418680,2.782992,-3.409155,0.898715,-1.829392,9.221022,2.764711,-4.865159,1.051975,-6.044792,1.977259,5.673759,2.738245,-2.207443,9.723343,6.067191,6.730208,-9.626119,-0.078967,1.102602,-1.857547,-4.615297,-0.892715,1.752952,-3.547845,-4.165906,-1.859951,-7.819187,-6.564114,-6.332504,2.195250,4.963983,-6.155554,3.251378,-9.767153,7.670041,5.049254,-6.702223,-6.207147,1.976896,2.197393,5.655065,9.404709,-9.102449,-8.875357,-5.332361,-8.311959,-4.357951,3.114879,4.393512,-3.260213,0.554457,-8.816087,6.598102,2.753613,-9.881004,6.186919,-8.267438,1.568742,-2.554332,-8.575373,5.679426,-4.813669,8.366701,7.585236,9.201945,-1.801802,-3.991042,-3.594005,3.629597,-3.513544,1.840105,9.367398,7.695045,-9.405889,-9.612461,-1.225811,1.889971,4.743529,-7.057216,1.111250,5.490141,-0.497361,-3.916358,1.327655,-9.301256,7.035301,9.741887,-8.109286,6.677288,-8.951977,4.897671,-7.329074,-1.082713,5.923906,-4.423120,-9.525611,-4.218402,4.844350,-5.563053,0.766101,3.833497,-9.147929,5.162763,8.144295,9.005659,7.686768,-6.211479,6.516661,8.229123,4.850498,3.456277,1.642618,3.060659,-4.550013,-6.843259,-8.546219,0.069313,-4.012837,3.859838,7.322758,-2.611094,2.755735,-5.338124,1.087823,-7.000088,-7.043576,-9.006118,6.614245,-2.945650,3.387202,8.925322,-3.069165,-7.388344,-9.377620,-2.258196,-5.770580,-2.779078,6.497751,-3.774350,-1.176945,-3.546312,-9.510751,0.919139,-1.307202,-2.851694,-0.086582,7.311130,-0.214669,4.656139,-1.966691,-4.835968,-5.235759,-5.221126,-4.244696,-5.371872,3.237776,7.841243,-3.577513,-4.318490,-9.099895,-2.529554,-8.988053,-6.171230,-6.456139,6.966294,5.641552,9.526025,-4.163080,-2.991651,7.911521,-1.559603,2.166878,-4.895282,-1.238395,-7.773283,8.523918,2.886245,-8.072707,-9.729601,3.862822,9.304620,-2.203233,0.873727,9.145827,5.356878,-7.571708,5.789085,0.612836,1.253741,-5.435569,-4.585026,1.028839,-7.398625,3.940950,-3.807883,-2.748401,-0.064786,-1.725247,-4.052811,0.037728,-6.602012,4.399154,7.150324,-9.111686,-9.695887,-9.247002,-1.020683,-2.614095,3.986900,-8.942637,-7.775431,-6.378649,0.739496,-9.941781,-7.787229,8.917979,-4.536655,-7.055596,1.783152,-9.445863,-8.541104,-8.827721,-8.365771,8.015183,1.525032,4.884436,-2.045399,-8.307707,6.134063,7.877735,-0.005846,-7.677971,4.007090,-3.365844,9.666205,-6.154523,3.893858,7.526442,7.641984,0.627592,-2.756262,2.002849,-9.621392,-9.418349,-6.967993,8.946986,-2.721795,6.903574,5.276183,-0.034709,9.502175,-0.289172,3.397970,-4.104248,-6.445372,7.002095,8.300176,6.494866,-3.102371,2.120990,-9.236398,2.711320,-6.706778,-2.475389,-7.032776,2.405008,-3.959271,-1.732781,8.058647,-4.545307,7.698928,-4.053057,-4.555347,-5.440340,7.967690,-5.799986,1.388354,-4.837398,-0.495036,1.314728,5.371355,-9.842949,-5.826895,0.154139,-2.991479,0.466973,-5.145982,-7.801257,5.639475,7.768422,-3.000539,-0.372931,-1.888860,6.289817,-5.219204,8.128754,6.172444,9.978755,1.808152,0.127721,-0.617330,5.519195,-5.959783,-2.022462,-5.042537,-2.937074,9.000123,-4.970143,5.158093,-2.581386,-4.917072,6.185922,-7.312878,5.540216,-4.685636,2.918725,5.392415,9.226978,-9.661038,-2.037420,3.770223,4.749817,8.179189,-2.243304,6.190317,-6.797049,3.468416,-2.076363,-5.769679,8.484111,-8.953552,-3.141627,0.058032,-4.591710,1.682288,-8.231904,2.197457,5.605113,-3.321500,-7.716579,-8.647896,0.829441,-8.654814,4.803462,-3.887645,9.775663,0.523216,-1.653001,8.302317,-0.555832,7.789732,-9.064091,-9.102546,-9.645313,7.511002,8.615183,4.306483,9.402002,-4.645946,5.122639,4.051086,7.044914,-3.744959,5.952823,-4.466106,-4.733353,6.910157,6.311031,-7.036355,-4.712964,-9.121649,7.409298,-5.544810,2.303135,-2.352038,8.619507,-2.506953,-4.077460,7.066186,-6.009894,-3.569360,3.428253,6.681155,6.227230,-7.010217,-7.265578,7.606803,9.997327,-9.944841,-4.449569,2.656094,3.156903,2.482894,-3.113697,9.907902,-3.452672,4.076086,3.973084,-6.791284,-0.545966,-8.903422,2.611131,-9.939835,-4.081244,-2.019498,6.085834,-7.771455,8.818121,7.613644,-9.283197,-1.563342,-1.357824,9.426104,4.404363,-8.099857,-3.060507,-8.514414,0.452695,-1.796467,0.761665,-4.676234,-8.835394,3.051887,-2.046897,2.730842,-9.927770,-1.422783,6.636326,-7.825908,3.568928,-7.829373,-8.887917,-5.264924,-9.808807,0.755605,6.013275,-2.550133,-0.875127,3.104375,-8.855994,-1.431666,-3.146521,4.012938,-5.109477,-9.341083,7.874115,6.220015,8.605345,2.009968,7.128771,-0.445800,-8.523786,-1.649729,-9.373762,-5.734553,7.118924,4.042488,7.033402,8.543013,8.029272,1.245149,6.744498,-3.928491,-4.389778,-4.865362,-3.565418,-8.014575,0.611401,1.305436,-3.708314,6.896479,-4.653157,-9.459640,9.465307,2.479601,5.311827,6.607276,-3.255368,-4.939838,8.440999,-5.869061,5.536315,9.380258,7.462065,-3.920299,-3.597632,7.658597,5.932673,-2.021246,-1.830359,5.742377,-1.676982,-2.953609,-6.935896,-9.626992,5.249024,7.935428,9.188676,0.753356,7.138008,9.688892,5.992060,1.543806,-6.652588,-8.288440,7.502597,-9.783464,-0.831626,-1.621855,4.884370,1.893750,3.007854,8.704052,0.581212,-9.087358,7.429749,-4.425249,-6.446189,5.330425,8.712397,3.440149,9.904756,-3.128577,-3.555762,-2.362499,3.499193,-8.426931,-4.330376,-0.488814,1.735158,-6.607773,-1.595289,9.909049,-9.712136,4.581495,-3.600670,9.446318,-3.262113,-0.014366,-2.236687,5.772269,-0.968413,4.781198,4.957965,-0.562880,-5.489882,0.926456,3.158853,2.914427,1.489502,4.839182,-3.392713,6.104934,-3.148160,1.131288,-8.594917,2.343604,5.883014,8.857902,-8.150858,4.433470,5.419417,8.382342,3.234395,-1.887986,2.367724,2.204582,-1.477025,-1.741501,-3.303619,-2.881133,-7.764458,8.910262,-3.380062,9.517956,-8.169176,4.715970,4.285265,-6.417162,5.916955,-2.749730,-3.918278,-6.106483,-7.692456,5.409671,9.496797,-0.826583,2.333838,6.780872,-4.340239,-9.660477,0.661028,-8.148512,-9.055118,0.108196,-9.209972,-9.464230,4.386986,7.333382,-7.818157,-7.187331,-3.148432,6.036946,-6.460773,6.858275,2.877299,5.007822,3.516716,-4.048879,-9.748407,-0.702613,5.215317,5.096912,5.573990,-5.037697,-0.831679,6.451250,4.974860,-3.867786,0.401708,6.559007,-3.816175,8.525093,-4.291810,3.554083,-8.116004,9.909038,4.346971,-1.753950,-3.310642,-4.715944,-7.950218,3.530348,-1.390061,6.787611,-3.091312,8.766700,-3.193687,-2.898686,-7.898965,7.694546,7.100073,-3.753956,-3.937311,-2.157411,1.276502,7.502038,-1.757069,-9.966956,-7.924215,0.716876,-7.118796,7.415391,6.621041,6.298382,-6.389085,-3.557505,-3.405645,-4.884907,-0.124740,1.326804,7.136453,2.511285,9.005516,-4.255057,6.367906,-7.348743,-9.447880,-4.910442,-8.402334,0.114944,5.951753,-8.001429,-0.165916,-7.513379,5.198182,9.567285,-6.348680,7.605627,-4.875435,3.244257,0.853473,9.729919,-8.099674,8.557239,9.681569,4.210795,4.480649,-1.212288,-0.670670,-9.413914,-0.203169,-4.619967,-0.517562,3.246563,9.616009,-1.075325,-8.867831,6.793413,-8.625529,2.088172,5.003535,-9.481966,3.483138,7.612630,5.048188,1.742202,8.069559,-2.410983,3.601437,-7.752882,-9.485537,2.753525,-3.673962,1.155842,-4.695779,-7.964951,1.601036,-9.245217,-0.052970,-7.744122,6.409979,8.639797,6.618088,-7.191610,8.992007,-3.632586,4.395952,1.459796,-9.347418,-4.636731,3.515621,-0.493989,1.624143,5.999893,-3.169659,9.072655,-3.802253,-8.034290,-3.892296,-3.503185,2.390905,-4.293749,3.665383,-0.318109,-4.579701,-7.604204,-5.860590,2.939281,4.984787,8.247954,-9.905298,9.729909,3.722586,1.035872,-3.227621,-7.532371,-6.157692,-8.832520,-1.527751,4.507135,-8.942441,-7.846789,-2.402071,-9.130570,8.379396,-1.558582,6.147814,-2.355837,3.047901,-9.057748,7.756581,-9.864704,4.127744,6.915538,8.124732,3.267527,-7.587067,-7.768376,6.439674,-7.073956,-1.673739,-6.465545,-0.637082,9.705279,-6.525164,6.555261,-3.854995,6.353604,6.449975,7.519306,1.455752,-1.261951,-3.452965,3.471323,6.947538,-9.894015,-9.487695,3.763007,3.456685,-4.187202,5.046619,-6.289993,8.537111,2.880296,-3.611763,-3.590514,8.342939,-5.347282,3.445851,0.001706,6.089451,6.360303,3.079438,2.502683,5.235788,-5.181014,6.001055,-9.008140,2.809119,9.250272,-6.564207,5.848620,-7.355378,8.525957,7.959304,3.129261,5.874648,-9.793682,7.145437,6.098531,-4.760855,1.575274,-2.660474,-1.898392,-1.999485,-0.243597,2.303170,-7.602837,0.600891,-7.789044,5.875453,5.886081,-2.695722,4.832995,5.396687,-1.793228,-5.599747,-4.084076,1.303428,-0.686289,-6.011715,-0.074176,1.980174,-0.053920,-1.901787,0.986787,-1.721389,-9.498253,2.217276,-4.120178,0.064583,-2.908031,6.049952,-2.336417,5.738098,-0.557090,8.986551,-4.280708,8.156329,5.621196,6.224320,0.609319,-5.358187,-9.324520,4.461023,-2.075590,9.966144,1.776770,5.510804,4.057916,-6.423375,0.839281,-2.003945,-9.066101,-3.519595,4.030168,8.870747,6.100133,6.981472,9.154309,-7.151817,3.500802,-3.611348,-2.973933,-6.577565,-4.974115,9.261001,4.261107,6.662100,-0.857796,4.763122,4.830920,-9.296073,-7.158334,-5.152671,2.645234,-7.647737,-2.888414,5.353190,-9.886903,-9.625914,-8.408959,-8.265879,7.227292,-5.531791,7.546334,-2.343875,-8.149428,9.809456,-4.242825,-6.631541,8.363294,-9.944184,2.177040,-2.576796,1.932267,-2.978450,3.577674,3.699765,8.796352,-4.654252,-3.047293,9.405310,8.484475,2.682159,0.842183,6.416858,-6.684939,-8.644417,3.864223,-6.776220,-9.695477,9.799134,9.911425,-9.723117,-7.902849,-0.790363,4.479002,2.339586,-9.708588,-8.029199,-8.226205,-0.723665,6.319610,-8.337352,-2.858097,-1.211636,3.755040,-1.990931,-2.620135,6.950455,8.380216,5.620447,-5.393792,3.216798,-2.153376,-0.033771,-0.395334,2.042652,6.356056,-0.106743,-7.349208,-4.502792,-5.525101,2.799641,-5.552615,7.963811,-6.222525,-3.509857,7.592362,6.778636,-6.691660,-6.155897,5.576256,-5.848811,8.470240,-3.105088,4.330013,-5.162550,5.135183,0.595632,-2.512481,5.669419,7.455656,5.640122,7.712815,-7.446537,-6.124776,-8.759819,8.536631,5.913440,-8.765494,-6.199563,-6.619002,0.373499,-0.171494,5.700254,-9.259063,7.130507,7.065213,-0.121953,-0.746191,-6.275834,-2.604256,-5.707226,9.298112,-9.837724,9.636511,-7.105727,3.891302,8.653349,-7.555480,7.543726,1.117423,-9.329977,5.364084,7.169521,-1.152614,8.360283,3.281243,-8.624913,7.555090,-4.208824,7.852373,-8.062486,-6.444456,9.458622,4.122178,8.811446,6.509947,6.096789,7.047253,-4.294557,-5.026323,-0.337398,4.432358,-7.996869,8.895808,7.288594,8.859443,-3.086196,0.599749,-6.753114,-6.034929,0.354468,-0.889925,-0.394769,-9.954296,4.693851,-3.480309,-4.196287,-8.693744,-5.417638,1.195518,-7.277703,-2.881700,-8.122196,-5.010720,-1.601411,9.681101,8.761768,-4.891474,6.602583,-3.752745,7.816308,-7.648941,9.640788,-9.382231,-7.570702,2.891860,6.196182,4.717120,-7.361568,-6.486789,-3.180502,-9.244917,0.036705,-9.740492,8.611284,5.042665,6.202702,-5.806896,-7.916898,5.378077,-5.941385,-8.286788,-5.276196,-9.624974,1.120107,6.429165,-2.045438,8.317246,-1.924211,-3.664225,2.448823,-1.490257,8.172166,4.486402,6.556820,-3.775112,3.637037,6.992591,7.147339,-8.114598,9.289461,-6.881239,-9.552828,7.252731,6.956691,-8.095756,-5.263695,-7.648271,-2.470532,0.764482,-6.230138,3.667357,-7.084589,2.379210,-3.391729,0.501622,2.327688,2.464821,5.681152,-2.598160,-2.042725,9.987933,5.252675,-2.547718,8.743761,4.606765,-0.815923,-6.220840,-8.078911,-2.889535,3.847959,-9.751742,7.870264,-0.758498,-5.321513,-9.434158,-6.062126,4.392775,0.019200,9.232200,-7.153957,-1.866404,4.701231,8.458683,-2.645851,1.001559,3.961441,-5.788102,1.988624,-9.179882,8.168871,2.434642,-7.787266,5.350790,-9.745681,9.815689,4.664515,0.607277,-8.995708,-1.107748,-3.667543,-9.637396,1.902617,3.375099,-5.478620,1.462752,-5.239871,5.930301,8.128401,-6.371540,8.790120,-6.537804,9.845602,9.396700,1.602214,-5.443843,0.755188,2.521293,4.054736,-4.052042,-5.002047,0.881366,-6.208572,-4.552503,4.672678,9.745313,-2.733358,3.623980,-8.442783,2.502311,3.759776,1.245384,-8.275305,7.333433,9.143615,6.967161,0.605428,-7.320532,3.868337,-0.519720,6.685509,4.850480,0.485321,6.959408,-9.750296,7.261211,-2.721389,-0.847993,-2.711017,-1.192689,3.412240,8.686747,-8.603276,-6.695431,-6.501752,-4.204300,0.263838,3.288585,2.431968,-7.836625,1.783216,1.586028,-3.084853,7.575428,4.630092,4.097980,6.044545,-5.641244,-7.617711,-7.948901,3.426707,5.331699,-5.966375,2.787186,0.152322,5.214933,-9.097913,7.309159,1.271167,6.167504,-2.241262,9.909039,0.720927,-1.232981,9.973668,7.274362,4.205574,3.173160,1.353543,6.642639,-1.706138,-8.031079,3.245195,3.520314,-6.096904,-8.137905,8.015260,-5.212923,4.212674,6.694098,0.515638,9.037054,6.056623,2.701004,8.570081,0.505101,8.996818,-0.620967,9.820003,9.589088,-7.700258,3.987058,-4.242308,4.493473,-7.441531,-4.101963,6.108040,-2.885755,-7.288839,6.826032,6.890641,3.322439,-3.247767,8.536232,8.607331,7.467348,-1.813114,-8.352832,9.164391,-8.231174,-2.436682,7.775137,-8.095851,-3.905450,3.503542,0.946196,-7.438262,-3.352729,-7.337905,6.148375,-1.523061,-3.293666,9.479857,8.674790,-1.093577,-1.889993,-9.332974,-4.453003,3.477239,1.575425,-8.290288,4.600681,2.185788,-8.383063,-9.966812,-8.914858,-2.293635,1.245556,9.841998,-9.370870,5.317288,-8.601221,2.080945,-1.782855,1.635259,0.654111,-7.077630,-2.036900,-6.151298,-5.022232,-5.621080,-4.697903,2.410257,-0.045608,-4.635911,-0.430143,7.809981,-3.885909,1.729485,-8.410605,-7.592828,-4.785242,-4.518511,3.528390,1.653296,3.999236,-2.424089,8.268194,-7.504768,-2.856863,-3.598325,-6.751311,5.447554,-5.407068,9.834578,7.217566,5.054842,0.205061,-5.081515,-2.502591,-5.302335,-5.715353,0.835261,-6.385265,0.660681,6.996043,3.115581,-6.409879,-0.912109,5.886326,9.340831,6.566107,-0.270015,-3.191095,6.762061,9.734050,2.294630,-4.061271,1.719580,-3.913131,2.760883,-8.468158,6.392735,1.291740,-5.755963,1.359766,1.284703,-6.876162,6.256385,2.273168,8.222300,-4.459568,-9.365908,-9.062753,1.501092,-8.012510,-2.438066,4.402511,3.038843,2.407604,2.832218,9.754288,3.150290,2.417533,4.401513,-6.654837,7.419952,8.540543,9.836662,6.448315,-9.567789,-7.495503,-4.668769,-4.156037,-3.779892,0.525332,-5.506687,5.550752,-3.048269,1.243217,4.441435,0.051861,-6.085780,-9.126099,-1.512637,1.249540,1.726314,0.169518,8.656677,-9.079402,2.342301,-8.929904,-6.487962,8.164475,-6.090339,-9.824902,-7.735125,-2.002705,-5.137599,8.374608,-2.743644,9.802579,-5.766239,4.334492,-8.668911,4.668401,-0.263568,-7.081437,7.519327,7.918165,-3.658481,1.473799,7.779633,9.916072,-0.708077,-9.680763,1.015080,3.803965,-2.366716,-4.828709,-5.582340,-2.669496,3.328834,9.188547,2.854788,-4.369999,8.225923,-7.504026,5.812259,-7.238684,-7.498464,-5.219285,0.593889,8.358501,-3.425100,-0.694774,-8.793461,5.726948,8.953457,-4.483063,-1.657426,-1.344499,8.869517,-9.800011,9.193957,-0.478421,-1.282030,1.967886,-4.829641,1.495201,-7.640202,0.927489,1.220333,-6.524443,-9.984153,6.382556,9.445636,-3.533810,-8.908814,3.123066,6.334254,-1.531347,-6.527201,0.750685,-2.059785,-8.052949,6.694070,3.653732,-9.804444,5.137152,3.621417,7.834040,3.028929,4.708841,1.373867,4.186557,-2.785188,-0.776624,0.808265,-3.673523,-6.846599,5.589752,-7.833940,-7.422813,-8.021713,7.492799,-9.819211,2.168470,-3.524532,-1.806599,6.112277,6.807644,0.186465,4.669613,5.559747,-2.017614,-5.615706,1.667001,4.301635,5.778171,-3.722617,3.835500,-9.451160,-2.982285,6.076619,-6.300705,-2.088464,-2.293018,0.178554,-7.259767,1.012983,-1.992287,-1.259879,9.033714,-3.902876,-2.644326,0.475127,6.399861,-7.521620,7.368719,-5.192383,-0.908738,2.244379,-7.092589,-5.293311,8.613622,-1.059729,2.017086,-6.621626,-9.003342,-5.537524,0.481019,-2.645474,1.158876,-5.973184,-4.383916,-8.413431,9.327319,9.018289,-0.340801,-8.291074,-6.015472,6.045858,-0.084441,-6.135440,-6.954188,5.480388,-6.435604,3.467992,-3.327125,-5.940534,-8.719771,2.202400,-5.335155,-5.937046,4.092494,7.170095,8.011658,4.220739,-9.514739,-6.227782,-8.876049,-2.242173,4.781492,-4.617800,6.044173,-4.452564,1.150524,7.033300,-4.426537,-3.158867,-4.354214,3.710764,9.815502,5.731146,-0.388440,-3.843472,1.913882,-7.960384,-4.497389,-3.852330,0.660759,-1.557581,2.495933,0.296029,0.885289,2.418065,3.424782,6.358017,5.856578,-4.122538,-0.151527,0.837696,7.048047,-7.475618,-7.838236,2.447604,7.807193,1.183540,7.428108,-9.041407,-8.645076,-2.419807,8.838810,-8.268106,9.892589,-3.519689,-6.164743,4.554022,0.059910,3.318763,7.669972,-7.389662,-2.358690,0.543398,-2.341793,-9.540140,2.896587,-7.459154,-1.039992,3.811197,1.699634,1.026926,7.776617,4.722663,-2.681350,5.053238,7.887025,-9.921796,9.422697,0.734041,-7.411851,-0.749976,-0.430993,-1.261888,-6.397066,-2.858446,1.245015,7.469015,5.387578,-4.481796,5.106100,5.420562,7.378026,9.789770,7.097428,-4.738779,-6.542711,7.710884,5.393094,-7.442800,7.738198,0.756231,-6.513214,-2.206403,1.939021,-7.225116,-8.523992,6.627578,3.830028,-6.321601,6.743296,-1.671928,4.193131,-1.613983,7.544020,-8.976535,-0.339816,-2.832966,-2.071818,-1.097313,3.082040,0.533543,-2.243784,2.391285,9.478600,-4.370704,-7.825251,-8.671987,-5.568922,-0.940189,7.014531,-6.576722,-8.819080,1.876521,5.311165,-7.691410,-1.785622,-4.449173,-2.828654,-4.896965,6.307869,-4.259002,-6.749451,-9.819005,7.720866,-2.500879,7.441238,-5.380617,2.888702,0.832637,8.918035,5.100756,4.973437,-2.556450,2.098553,8.814748,1.982501,-0.021101,-9.503450,-6.269855,5.986576,3.678385,-6.059058,-9.784952,3.759264,-2.487517,2.926217,-3.290604,-1.306358,-6.477719,2.343606,-9.923206,0.835418,-6.291770,8.211247,-7.709112,-3.468199,-0.157239,0.545872,-2.408896,-3.401034,-0.542922,1.818122,-2.020887,9.210359,3.965266,-9.287901,-0.052924,9.712146,4.040976,5.416464,8.231877,2.848057,-2.085980,3.799130,5.800436,-9.620134,9.047824,-5.695953,8.696083,6.556824,9.665110,-5.562181,6.797099,-9.639952,0.801187,-9.217082,0.387773,-8.361326,8.893391,1.458255,8.887462,-3.481650,6.821474,-3.349524,-6.330943,9.271249,1.535927,9.767729,3.616151,8.702489,-4.925422,-8.740565,-7.045035,3.483147,-8.446817,-9.741191,-5.587323,-3.884286,-7.504298,-9.142639,-8.783123,-7.024357,-4.672632,1.469248,5.738309,-4.814744,-1.580379,-2.980349,6.628599,-0.033888,-6.406280,9.522305,7.441167,-6.133387,-5.465642,2.125526,-4.939868,-6.524947,0.637393,1.955830,-9.416582,-4.016624,-4.607089,1.389861,2.227890,0.134756,8.526701,-8.731443,-9.122449,-2.233613,-8.825908,-7.106402,7.208717,2.274211,-8.878269,4.630829,-4.115567,8.508204,-3.169407,-5.490287,8.570560,4.971419,-5.837197,5.847971,-6.437850,7.837548,8.317121,-7.660228,-0.855140,-6.428872,-2.324538,1.893520,8.813202,3.889420,-8.906311,0.897774,7.261661,-3.867834,3.460040,-7.948733,8.049740,-4.332773,5.547304,2.125441,-2.469444,-7.340761,6.624252,1.753586,3.361763,0.561851,-8.721253,7.839556,3.466330,8.823787,8.460906,2.228150,7.491680,-5.636978,-0.743523,-1.780278,6.652633,1.957595,-7.901449,5.595017,3.803460,6.739632,-2.809770,5.432150,-7.972411,-0.354389,-3.976864,-3.909790,2.381519,4.975384,-2.907474,-8.513065,-4.812482,8.986607,-1.788116,-7.892470,9.436248,3.677523,-8.855840,5.845420,6.273534,3.040007,7.143413,3.657711,-7.997335,-8.677136,-5.277630,-4.370732,-7.553370,1.745704,-5.500940,-6.133440,-6.088676,0.940599,-9.730346,4.375935,-6.120951,-2.556900,7.574871,-9.641574,-6.746060,-6.028064,3.810870,7.475674,-5.200362,-1.573552,5.580541,-2.576107,-2.145691,-0.923153,6.049838,-1.841347,-8.641783,4.848830,-1.789374,7.996504,5.776411,7.498615,-7.475878,-3.922513,-7.187845,-1.714010,-8.136538,5.789163,-3.069177,3.174542,0.992786,-4.968473,-0.029054,4.272242,3.305329,8.569900,5.038261,-1.847701,-1.936454,-8.384531,8.043889,-1.452870,-1.309257,1.917118,0.697485,-4.351222,-2.435813,7.484930,-8.717569,-1.739817,4.608551,-0.876235,-4.819599,3.279611,-5.372001,9.829967,-0.436597,8.279198,1.160452,0.023417,8.511641,-7.976798,-2.904592,0.355046,-2.441971,6.130313,5.542239,-6.579994,-5.505639,-0.558395,-0.690979,-4.980609,6.592273,9.069713,-0.543591,-8.917573,-2.276881,-5.318627,-3.470598,8.271242,2.791787,-4.471771,2.342782,-3.756822,-4.882370,-2.116846,8.082507,3.380111,-3.000662,0.849727,-5.633461,-0.573966,-9.233936,6.041969,-5.471439,-8.149538,4.071681,8.628635,9.740686,-9.125041,-8.678856,-6.245948,-6.826822,9.275920,-0.375365,8.696283,-9.097072,4.379309,-4.187645,5.373247,-0.048572,-5.107982,-2.679633,-4.358580,-6.048148,-7.133513,8.229009,-6.520923,-1.872224,-7.359254,-5.336172,2.578740,8.186671,-6.425945,-7.972507,1.237066,3.287419,-0.026397,3.465850,0.046049,-0.501622,-3.142008,8.180091,7.186727,-0.380807,-3.281747,7.158384,8.215404,9.186939,3.979794,2.932545,-1.112730,-6.972032,0.273045,8.812531,0.942702,-5.484772,1.738776,-2.513382,3.418505,-8.946592,-1.707182,-3.407459,-4.383232,5.690823,4.024477,-5.550357,4.700601,-3.946486,-1.732564,6.922083,9.298768,-1.056122,7.351419,0.700178,7.403088,8.607784,-8.588292,-3.999023,3.529540,-9.466835,-0.863727,-9.723304,6.925892,-7.493493,-5.669123,-2.350688,3.877338,-5.502367,0.377022,-5.423895,7.225918,-4.391305,8.028891,-5.365125,-2.744919,4.511457,-9.946924,-6.757730,-3.212559,7.303726,5.379887,3.342483,-3.142250,5.217545,8.981045,8.832249,5.984182,-4.240202,-7.960437,1.689377,1.472340,5.483874,-2.253252,-4.271270,5.141101,2.026714,2.061964,2.167650,-7.904743,1.546343,-0.701542,-2.865832,2.990409,-7.897684,-4.174142,-8.692047,-9.659707,6.963415,-3.599878,-8.605578,4.944021,-5.591383,-2.731749,8.397434,-4.306632,-5.934805,8.824426,1.347803,-8.504878,-1.413870,7.275043,-0.954591,-6.135468,4.559254,5.957475,-3.444346,6.162631,4.716666,8.016598,7.551128,-4.085915,-8.533558,-9.194669,-4.958984,-3.174621,5.773495,8.900545,0.126579,7.515541,-5.885328,-6.731661,-2.312014,8.242180,7.141857,-9.936513,2.319761,5.487435,-5.493174,1.426389,-4.038782,4.306861,8.141506,9.749488,-6.948764,0.304927,-7.615389,-5.103167,-4.598880,-3.314834,-4.716863,-0.990882,3.791297,8.676274,7.805413,-4.959135,-8.102610,-3.739426,3.283879,9.549040,-5.256909,-0.267152,-9.127459,7.926970,6.718738,6.042934,-4.939456,8.503061,0.528362,6.656844,9.284563,-3.179560,1.254768,3.030890,-8.406132,8.763225,-2.752822,9.522758,-7.456584,5.300675,0.658126,8.566988,-4.965961,6.006297,5.448427,-8.461388,9.132550,2.783770,5.448914,6.439904,7.240532,3.456673,-0.907145,-2.965127,6.085070,-6.548348,-1.337907,3.284903,-5.743877,-5.238376,1.633417,-5.690867,1.278619,-6.874926,0.834517,8.677464,-7.715906,-4.112666,8.230169,8.613343,-9.535816,3.631711,4.581856,0.684431,-4.473055,3.692096,-4.103768,-7.062705,1.645376,0.554240,-8.570516,1.242391,0.346652,3.078876,6.401437,0.108995,0.180329,-4.288180,0.916431,-1.578124,-3.224670,-6.405785,-1.884273,-1.363488,0.057455,-8.320505,-0.115158,-0.367246,7.349352,4.848621,-3.750651,-8.561722,3.492588,-7.365732,-9.742576,-6.358493,-7.970268,9.850403,7.779203,2.878153,6.713241,-6.953105,0.734485,9.513637,9.157246,8.463799,-2.721669,2.266961,7.234899,-4.832001,-5.337721,-1.175715,4.060614,6.381477,3.892024,6.573287,-1.316284,2.191212,-2.571881,-2.497484,8.470552,2.130336,7.080718,7.214153,-9.455229,-1.519405,7.956738,-3.330661], dtype = "float64")#candidate|3352|(3072,)|const|float64
call_3349 = relay.TupleGetItem(func_500_call(relay.reshape(var_3350.astype('uint64'), [4, 9]), relay.reshape(var_3351.astype('int32'), [126,]), relay.reshape(const_3352.astype('float64'), [3072,]), ), 4)
call_3353 = relay.TupleGetItem(func_505_call(relay.reshape(var_3350.astype('uint64'), [4, 9]), relay.reshape(var_3351.astype('int32'), [126,]), relay.reshape(const_3352.astype('float64'), [3072,]), ), 4)
output = relay.Tuple([bop_3303,call_3307,bop_3321,call_3324,const_3325,var_3326,call_3349,var_3350,var_3351,const_3352,])
output2 = relay.Tuple([bop_3303,call_3308,bop_3321,call_3327,const_3325,var_3326,call_3353,var_3350,var_3351,const_3352,])
func_3360 = relay.Function([var_3302,var_3326,var_3350,var_3351,], output)
mod['func_3360'] = func_3360
mod = relay.transform.InferType()(mod)
mutated_mod['func_3360'] = func_3360
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3360_call = mutated_mod.get_global_var('func_3360')
var_3362 = relay.var("var_3362", dtype = "bool", shape = (2, 9, 13))#candidate|3362|(2, 9, 13)|var|bool
var_3363 = relay.var("var_3363", dtype = "uint8", shape = (140,))#candidate|3363|(140,)|var|uint8
var_3364 = relay.var("var_3364", dtype = "uint64", shape = (36,))#candidate|3364|(36,)|var|uint64
var_3365 = relay.var("var_3365", dtype = "int32", shape = (126,))#candidate|3365|(126,)|var|int32
call_3361 = func_3360_call(var_3362,var_3363,var_3364,var_3365,)
output = call_3361
func_3366 = relay.Function([var_3362,var_3363,var_3364,var_3365,], output)
mutated_mod['func_3366'] = func_3366
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2212_call = mod.get_global_var('func_2212')
func_2214_call = mutated_mod.get_global_var('func_2214')
call_3374 = func_2212_call()
call_3375 = func_2212_call()
var_3379 = relay.var("var_3379", dtype = "float64", shape = (10, 14, 13))#candidate|3379|(10, 14, 13)|var|float64
bop_3380 = relay.bitwise_xor(call_3374.astype('uint16'), relay.reshape(var_3379.astype('uint16'), relay.shape_of(call_3374))) # shape=(10, 14, 13)
bop_3383 = relay.bitwise_xor(call_3375.astype('uint16'), relay.reshape(var_3379.astype('uint16'), relay.shape_of(call_3375))) # shape=(10, 14, 13)
output = bop_3380
output2 = bop_3383
func_3420 = relay.Function([var_3379,], output)
mod['func_3420'] = func_3420
mod = relay.transform.InferType()(mod)
mutated_mod['func_3420'] = func_3420
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3421 = relay.var("var_3421", dtype = "float64", shape = (10, 14, 13))#candidate|3421|(10, 14, 13)|var|float64
func_3420_call = mutated_mod.get_global_var('func_3420')
call_3422 = func_3420_call(var_3421)
output = call_3422
func_3423 = relay.Function([var_3421], output)
mutated_mod['func_3423'] = func_3423
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2359_call = mod.get_global_var('func_2359')
func_2360_call = mutated_mod.get_global_var('func_2360')
call_3430 = func_2359_call()
call_3431 = func_2359_call()
func_1300_call = mod.get_global_var('func_1300')
func_1302_call = mutated_mod.get_global_var('func_1302')
call_3433 = relay.TupleGetItem(func_1300_call(), 0)
call_3434 = relay.TupleGetItem(func_1302_call(), 0)
func_1490_call = mod.get_global_var('func_1490')
func_1493_call = mutated_mod.get_global_var('func_1493')
var_3437 = relay.var("var_3437", dtype = "float64", shape = (300, 2))#candidate|3437|(300, 2)|var|float64
call_3436 = relay.TupleGetItem(func_1490_call(relay.reshape(var_3437.astype('float64'), [600,])), 1)
call_3438 = relay.TupleGetItem(func_1493_call(relay.reshape(var_3437.astype('float64'), [600,])), 1)
output = relay.Tuple([call_3430,call_3433,call_3436,var_3437,])
output2 = relay.Tuple([call_3431,call_3434,call_3438,var_3437,])
func_3440 = relay.Function([var_3437,], output)
mod['func_3440'] = func_3440
mod = relay.transform.InferType()(mod)
mutated_mod['func_3440'] = func_3440
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3441 = relay.var("var_3441", dtype = "float64", shape = (300, 2))#candidate|3441|(300, 2)|var|float64
func_3440_call = mutated_mod.get_global_var('func_3440')
call_3442 = func_3440_call(var_3441)
output = call_3442
func_3443 = relay.Function([var_3441], output)
mutated_mod['func_3443'] = func_3443
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2010_call = mod.get_global_var('func_2010')
func_2011_call = mutated_mod.get_global_var('func_2011')
call_3452 = relay.TupleGetItem(func_2010_call(), 0)
call_3453 = relay.TupleGetItem(func_2011_call(), 0)
func_2947_call = mod.get_global_var('func_2947')
func_2949_call = mutated_mod.get_global_var('func_2949')
call_3462 = relay.TupleGetItem(func_2947_call(), 0)
call_3463 = relay.TupleGetItem(func_2949_call(), 0)
bop_3476 = relay.greater_equal(call_3452.astype('bool'), relay.reshape(call_3462.astype('bool'), relay.shape_of(call_3452))) # shape=(10, 14, 13)
bop_3479 = relay.greater_equal(call_3453.astype('bool'), relay.reshape(call_3463.astype('bool'), relay.shape_of(call_3453))) # shape=(10, 14, 13)
output = relay.Tuple([bop_3476,])
output2 = relay.Tuple([bop_3479,])
func_3480 = relay.Function([], output)
mod['func_3480'] = func_3480
mod = relay.transform.InferType()(mod)
output = func_3480()
func_3481 = relay.Function([], output)
mutated_mod['func_3481'] = func_3481
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3485 = relay.var("var_3485", dtype = "bool", shape = ())#candidate|3485|()|var|bool
var_3486 = relay.var("var_3486", dtype = "bool", shape = (1, 5, 16))#candidate|3486|(1, 5, 16)|var|bool
bop_3487 = relay.logical_or(var_3485.astype('bool'), var_3486.astype('bool')) # shape=(1, 5, 16)
output = bop_3487
output2 = bop_3487
func_3491 = relay.Function([var_3485,var_3486,], output)
mod['func_3491'] = func_3491
mod = relay.transform.InferType()(mod)
mutated_mod['func_3491'] = func_3491
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3491_call = mutated_mod.get_global_var('func_3491')
var_3493 = relay.var("var_3493", dtype = "bool", shape = ())#candidate|3493|()|var|bool
var_3494 = relay.var("var_3494", dtype = "bool", shape = (1, 5, 16))#candidate|3494|(1, 5, 16)|var|bool
call_3492 = func_3491_call(var_3493,var_3494,)
output = call_3492
func_3495 = relay.Function([var_3493,var_3494,], output)
mutated_mod['func_3495'] = func_3495
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1955_call = mod.get_global_var('func_1955')
func_1957_call = mutated_mod.get_global_var('func_1957')
call_3533 = relay.TupleGetItem(func_1955_call(), 0)
call_3534 = relay.TupleGetItem(func_1957_call(), 0)
output = call_3533
output2 = call_3534
func_3538 = relay.Function([], output)
mod['func_3538'] = func_3538
mod = relay.transform.InferType()(mod)
output = func_3538()
func_3539 = relay.Function([], output)
mutated_mod['func_3539'] = func_3539
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3545 = relay.var("var_3545", dtype = "float64", shape = (3, 6, 4))#candidate|3545|(3, 6, 4)|var|float64
uop_3546 = relay.sigmoid(var_3545.astype('float64')) # shape=(3, 6, 4)
output = uop_3546
output2 = uop_3546
func_3556 = relay.Function([var_3545,], output)
mod['func_3556'] = func_3556
mod = relay.transform.InferType()(mod)
var_3557 = relay.var("var_3557", dtype = "float64", shape = (3, 6, 4))#candidate|3557|(3, 6, 4)|var|float64
output = func_3556(var_3557)
func_3558 = relay.Function([var_3557], output)
mutated_mod['func_3558'] = func_3558
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3591 = relay.var("var_3591", dtype = "int32", shape = (8, 1, 15))#candidate|3591|(8, 1, 15)|var|int32
var_3592 = relay.var("var_3592", dtype = "int32", shape = (8, 3, 15))#candidate|3592|(8, 3, 15)|var|int32
bop_3593 = relay.maximum(var_3591.astype('int32'), var_3592.astype('int32')) # shape=(8, 3, 15)
uop_3598 = relay.asin(var_3591.astype('float32')) # shape=(8, 1, 15)
func_3222_call = mod.get_global_var('func_3222')
func_3223_call = mutated_mod.get_global_var('func_3223')
call_3604 = func_3222_call()
call_3605 = func_3222_call()
func_1300_call = mod.get_global_var('func_1300')
func_1302_call = mutated_mod.get_global_var('func_1302')
call_3618 = relay.TupleGetItem(func_1300_call(), 0)
call_3619 = relay.TupleGetItem(func_1302_call(), 0)
output = relay.Tuple([bop_3593,uop_3598,call_3604,call_3618,])
output2 = relay.Tuple([bop_3593,uop_3598,call_3605,call_3619,])
func_3621 = relay.Function([var_3591,var_3592,], output)
mod['func_3621'] = func_3621
mod = relay.transform.InferType()(mod)
var_3622 = relay.var("var_3622", dtype = "int32", shape = (8, 1, 15))#candidate|3622|(8, 1, 15)|var|int32
var_3623 = relay.var("var_3623", dtype = "int32", shape = (8, 3, 15))#candidate|3623|(8, 3, 15)|var|int32
output = func_3621(var_3622,var_3623,)
func_3624 = relay.Function([var_3622,var_3623,], output)
mutated_mod['func_3624'] = func_3624
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3538_call = mod.get_global_var('func_3538')
func_3539_call = mutated_mod.get_global_var('func_3539')
call_3626 = func_3538_call()
call_3627 = func_3538_call()
func_1873_call = mod.get_global_var('func_1873')
func_1875_call = mutated_mod.get_global_var('func_1875')
call_3638 = relay.TupleGetItem(func_1873_call(), 0)
call_3639 = relay.TupleGetItem(func_1875_call(), 0)
func_3183_call = mod.get_global_var('func_3183')
func_3185_call = mutated_mod.get_global_var('func_3185')
call_3641 = func_3183_call()
call_3642 = func_3183_call()
func_2313_call = mod.get_global_var('func_2313')
func_2316_call = mutated_mod.get_global_var('func_2316')
call_3643 = relay.TupleGetItem(func_2313_call(relay.reshape(call_3638.astype('float32'), [10, 14, 13])), 1)
call_3644 = relay.TupleGetItem(func_2316_call(relay.reshape(call_3638.astype('float32'), [10, 14, 13])), 1)
func_3360_call = mod.get_global_var('func_3360')
func_3366_call = mutated_mod.get_global_var('func_3366')
var_3649 = relay.var("var_3649", dtype = "bool", shape = (234,))#candidate|3649|(234,)|var|bool
var_3650 = relay.var("var_3650", dtype = "uint8", shape = (140,))#candidate|3650|(140,)|var|uint8
var_3651 = relay.var("var_3651", dtype = "uint64", shape = (36,))#candidate|3651|(36,)|var|uint64
var_3652 = relay.var("var_3652", dtype = "int32", shape = (126,))#candidate|3652|(126,)|var|int32
call_3648 = relay.TupleGetItem(func_3360_call(relay.reshape(var_3649.astype('bool'), [2, 9, 13]), relay.reshape(var_3650.astype('uint8'), [140,]), relay.reshape(var_3651.astype('uint64'), [36,]), relay.reshape(var_3652.astype('int32'), [126,]), ), 2)
call_3653 = relay.TupleGetItem(func_3366_call(relay.reshape(var_3649.astype('bool'), [2, 9, 13]), relay.reshape(var_3650.astype('uint8'), [140,]), relay.reshape(var_3651.astype('uint64'), [36,]), relay.reshape(var_3652.astype('int32'), [126,]), ), 2)
output = relay.Tuple([call_3626,call_3638,call_3641,call_3643,call_3648,var_3649,var_3650,var_3651,var_3652,])
output2 = relay.Tuple([call_3627,call_3639,call_3642,call_3644,call_3653,var_3649,var_3650,var_3651,var_3652,])
func_3661 = relay.Function([var_3649,var_3650,var_3651,var_3652,], output)
mod['func_3661'] = func_3661
mod = relay.transform.InferType()(mod)
mutated_mod['func_3661'] = func_3661
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3661_call = mutated_mod.get_global_var('func_3661')
var_3663 = relay.var("var_3663", dtype = "bool", shape = (234,))#candidate|3663|(234,)|var|bool
var_3664 = relay.var("var_3664", dtype = "uint8", shape = (140,))#candidate|3664|(140,)|var|uint8
var_3665 = relay.var("var_3665", dtype = "uint64", shape = (36,))#candidate|3665|(36,)|var|uint64
var_3666 = relay.var("var_3666", dtype = "int32", shape = (126,))#candidate|3666|(126,)|var|int32
call_3662 = func_3661_call(var_3663,var_3664,var_3665,var_3666,)
output = call_3662
func_3667 = relay.Function([var_3663,var_3664,var_3665,var_3666,], output)
mutated_mod['func_3667'] = func_3667
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2407_call = mod.get_global_var('func_2407')
func_2409_call = mutated_mod.get_global_var('func_2409')
call_3674 = relay.TupleGetItem(func_2407_call(), 0)
call_3675 = relay.TupleGetItem(func_2409_call(), 0)
output = relay.Tuple([call_3674,])
output2 = relay.Tuple([call_3675,])
func_3676 = relay.Function([], output)
mod['func_3676'] = func_3676
mod = relay.transform.InferType()(mod)
mutated_mod['func_3676'] = func_3676
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3676_call = mutated_mod.get_global_var('func_3676')
call_3677 = func_3676_call()
output = call_3677
func_3678 = relay.Function([], output)
mutated_mod['func_3678'] = func_3678
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3480_call = mod.get_global_var('func_3480')
func_3481_call = mutated_mod.get_global_var('func_3481')
call_3713 = relay.TupleGetItem(func_3480_call(), 0)
call_3714 = relay.TupleGetItem(func_3481_call(), 0)
output = call_3713
output2 = call_3714
func_3723 = relay.Function([], output)
mod['func_3723'] = func_3723
mod = relay.transform.InferType()(mod)
mutated_mod['func_3723'] = func_3723
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3723_call = mutated_mod.get_global_var('func_3723')
call_3724 = func_3723_call()
output = call_3724
func_3725 = relay.Function([], output)
mutated_mod['func_3725'] = func_3725
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1216_call = mod.get_global_var('func_1216')
func_1217_call = mutated_mod.get_global_var('func_1217')
call_3735 = relay.TupleGetItem(func_1216_call(), 0)
call_3736 = relay.TupleGetItem(func_1217_call(), 0)
func_2866_call = mod.get_global_var('func_2866')
func_2867_call = mutated_mod.get_global_var('func_2867')
call_3738 = func_2866_call()
call_3739 = func_2866_call()
uop_3741 = relay.cosh(call_3735.astype('float64')) # shape=(10, 14, 13)
uop_3743 = relay.cosh(call_3736.astype('float64')) # shape=(10, 14, 13)
output = relay.Tuple([call_3738,uop_3741,])
output2 = relay.Tuple([call_3739,uop_3743,])
func_3749 = relay.Function([], output)
mod['func_3749'] = func_3749
mod = relay.transform.InferType()(mod)
mutated_mod['func_3749'] = func_3749
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3749_call = mutated_mod.get_global_var('func_3749')
call_3750 = func_3749_call()
output = call_3750
func_3751 = relay.Function([], output)
mutated_mod['func_3751'] = func_3751
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2010_call = mod.get_global_var('func_2010')
func_2011_call = mutated_mod.get_global_var('func_2011')
call_3766 = relay.TupleGetItem(func_2010_call(), 0)
call_3767 = relay.TupleGetItem(func_2011_call(), 0)
func_3222_call = mod.get_global_var('func_3222')
func_3223_call = mutated_mod.get_global_var('func_3223')
call_3779 = func_3222_call()
call_3780 = func_3222_call()
func_2010_call = mod.get_global_var('func_2010')
func_2011_call = mutated_mod.get_global_var('func_2011')
call_3795 = relay.TupleGetItem(func_2010_call(), 0)
call_3796 = relay.TupleGetItem(func_2011_call(), 0)
func_1120_call = mod.get_global_var('func_1120')
func_1122_call = mutated_mod.get_global_var('func_1122')
call_3800 = relay.TupleGetItem(func_1120_call(), 0)
call_3801 = relay.TupleGetItem(func_1122_call(), 0)
output = relay.Tuple([call_3766,call_3779,call_3795,call_3800,])
output2 = relay.Tuple([call_3767,call_3780,call_3796,call_3801,])
func_3808 = relay.Function([], output)
mod['func_3808'] = func_3808
mod = relay.transform.InferType()(mod)
output = func_3808()
func_3809 = relay.Function([], output)
mutated_mod['func_3809'] = func_3809
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3830 = relay.var("var_3830", dtype = "int32", shape = ())#candidate|3830|()|var|int32
var_3831 = relay.var("var_3831", dtype = "int32", shape = (4, 10, 6))#candidate|3831|(4, 10, 6)|var|int32
bop_3832 = relay.greater(var_3830.astype('bool'), var_3831.astype('bool')) # shape=(4, 10, 6)
output = relay.Tuple([bop_3832,])
output2 = relay.Tuple([bop_3832,])
func_3855 = relay.Function([var_3830,var_3831,], output)
mod['func_3855'] = func_3855
mod = relay.transform.InferType()(mod)
mutated_mod['func_3855'] = func_3855
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3855_call = mutated_mod.get_global_var('func_3855')
var_3857 = relay.var("var_3857", dtype = "int32", shape = ())#candidate|3857|()|var|int32
var_3858 = relay.var("var_3858", dtype = "int32", shape = (4, 10, 6))#candidate|3858|(4, 10, 6)|var|int32
call_3856 = func_3855_call(var_3857,var_3858,)
output = call_3856
func_3859 = relay.Function([var_3857,var_3858,], output)
mutated_mod['func_3859'] = func_3859
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1216_call = mod.get_global_var('func_1216')
func_1217_call = mutated_mod.get_global_var('func_1217')
call_3903 = relay.TupleGetItem(func_1216_call(), 0)
call_3904 = relay.TupleGetItem(func_1217_call(), 0)
uop_3906 = relay.atan(call_3903.astype('float32')) # shape=(10, 14, 13)
uop_3908 = relay.atan(call_3904.astype('float32')) # shape=(10, 14, 13)
func_2760_call = mod.get_global_var('func_2760')
func_2761_call = mutated_mod.get_global_var('func_2761')
call_3918 = relay.TupleGetItem(func_2760_call(), 0)
call_3919 = relay.TupleGetItem(func_2761_call(), 0)
func_3556_call = mod.get_global_var('func_3556')
func_3558_call = mutated_mod.get_global_var('func_3558')
var_3931 = relay.var("var_3931", dtype = "float64", shape = (72,))#candidate|3931|(72,)|var|float64
call_3930 = func_3556_call(relay.reshape(var_3931.astype('float64'), [3, 6, 4]))
call_3932 = func_3556_call(relay.reshape(var_3931.astype('float64'), [3, 6, 4]))
uop_3933 = relay.log10(uop_3906.astype('float32')) # shape=(10, 14, 13)
uop_3935 = relay.log10(uop_3908.astype('float32')) # shape=(10, 14, 13)
output = relay.Tuple([call_3918,call_3930,var_3931,uop_3933,])
output2 = relay.Tuple([call_3919,call_3932,var_3931,uop_3935,])
func_3944 = relay.Function([var_3931,], output)
mod['func_3944'] = func_3944
mod = relay.transform.InferType()(mod)
var_3945 = relay.var("var_3945", dtype = "float64", shape = (72,))#candidate|3945|(72,)|var|float64
output = func_3944(var_3945)
func_3946 = relay.Function([var_3945], output)
mutated_mod['func_3946'] = func_3946
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3964 = relay.const([[[5,1,-9,4,-7,-5,10,-5,4,10],[9,10,-2,2,4,2,-2,-5,-1,-1],[2,3,3,-6,-5,-2,8,10,10,-1],[-5,-4,-6,-10,-10,5,8,-3,-6,-7],[-9,-3,-10,6,8,6,10,2,1,-5],[4,2,-8,2,-5,-2,7,-3,2,-9],[-9,-4,7,7,10,6,1,-8,2,-2],[-1,3,-10,7,6,-2,2,-3,6,4],[3,-9,-9,-5,9,10,-2,9,1,-3],[3,3,-3,-4,-10,4,10,10,-2,-2],[2,2,7,5,-7,-9,6,-6,10,-10],[8,-4,9,10,10,-6,-4,-8,10,-10],[-4,7,-1,-10,3,-3,-6,-3,-2,-10],[-5,-7,-7,-9,-8,5,-10,-3,5,3],[-5,-3,3,10,9,10,-8,-10,-3,1]],[[-1,-5,-9,3,-2,-4,-5,10,2,-5],[-1,2,3,-4,2,10,-10,-4,1,-2],[8,-2,4,-10,5,7,2,5,3,4],[5,-1,-6,5,-4,4,5,-4,-9,5],[-2,10,-2,-1,-4,-10,-8,-5,6,6],[5,2,6,-8,10,9,-4,8,-3,10],[-4,8,3,-8,1,1,-2,7,10,-2],[-9,-4,1,-10,3,-4,2,8,-5,-6],[-10,4,1,9,9,4,4,2,10,-2],[3,9,-7,-3,-5,1,-6,-7,-8,-8],[10,6,10,1,-1,-4,-10,10,-1,-2],[-9,-2,-9,2,5,-6,-2,3,2,3],[-9,-6,9,6,8,-6,10,4,7,9],[-7,-1,9,4,-9,3,-3,7,-6,4],[1,-10,10,-10,-1,-10,-4,-1,6,4]],[[-10,1,7,-7,-1,6,-1,-4,-2,7],[-5,-4,-10,4,8,-1,-5,4,-10,-7],[-10,-4,-9,1,3,7,-6,9,-3,4],[-8,-2,7,7,6,2,-6,6,-5,9],[6,-7,4,-8,6,-10,9,9,9,5],[9,1,4,-1,6,-8,-3,-3,-1,-7],[7,5,-1,-1,-10,6,-4,5,4,-10],[3,1,4,-6,-6,-4,-2,8,3,6],[6,3,6,-1,-3,1,8,3,-7,-7],[-3,8,9,-1,-5,-6,-8,4,-6,-6],[-5,-4,-10,-3,7,4,2,-5,7,-3],[-2,7,9,-8,4,5,-3,-2,-7,4],[6,4,-9,9,5,-10,5,1,-7,-1],[2,-2,-7,10,1,8,9,5,10,-3],[10,-4,-1,8,-3,-2,-9,10,1,9]],[[-3,7,-8,-9,8,5,-7,2,-5,9],[1,3,-8,-5,-4,-8,3,8,-10,2],[-10,8,10,-9,-2,3,10,5,-2,6],[7,2,9,-3,-8,1,-4,9,-10,-8],[-5,-6,-8,4,3,5,-1,-2,-8,3],[2,6,-2,-1,-1,5,-2,2,3,-10],[-5,-8,4,9,5,-8,8,4,-8,2],[-3,-7,9,-5,-7,-1,-3,-1,1,9],[-3,-6,10,1,-4,-7,-2,-4,-8,-5],[5,9,9,5,1,-7,-10,5,2,7],[-1,-4,1,-5,-8,-3,-8,-3,2,6],[-3,-8,-7,-2,-1,8,-3,4,-2,-2],[1,3,10,6,-5,7,-7,-10,8,-5],[9,10,8,8,6,8,7,-5,-9,-9],[3,-4,-1,-5,6,-9,-5,-9,-4,1]],[[-6,5,4,10,-1,10,5,4,-8,-4],[-1,1,1,-9,8,-6,10,-8,3,8],[7,10,1,7,-3,6,-5,1,9,-4],[7,1,-1,-2,7,8,5,7,2,-7],[-8,-10,-2,-2,1,7,-3,-5,-9,1],[-6,-1,9,-9,5,-7,-1,-7,-7,5],[2,6,-2,4,-10,9,-3,9,10,2],[-5,8,5,-10,-2,-10,9,-4,9,-4],[10,-6,-4,7,-2,7,10,-3,9,-7],[8,-7,-5,10,6,6,-7,-3,7,3],[10,7,5,3,1,9,9,-10,7,-2],[-6,-1,1,4,-5,-9,8,3,4,-1],[7,-8,-6,-5,-10,5,5,9,-1,8],[-1,-1,1,-4,1,1,5,-6,-8,3],[-10,-4,-8,3,-5,7,7,6,-1,2]],[[8,-10,3,-4,-9,-6,7,3,2,-5],[8,4,-10,-3,3,-1,-7,1,-6,-10],[4,-3,-8,6,-4,-9,-5,-8,-5,5],[4,-8,8,-2,6,9,-10,3,-1,-7],[2,-7,-1,9,6,8,2,5,-7,2],[3,-5,6,-10,-7,-1,-5,5,5,-5],[-9,-5,9,9,-10,-9,-4,3,-2,-8],[4,-9,2,-6,-7,-10,-6,-5,8,8],[7,-9,2,3,-9,-5,2,1,-8,-1],[-9,-3,-9,-7,4,-4,-5,-2,-9,2],[-7,10,-5,-5,7,9,-10,-1,1,-5],[7,6,6,-10,-4,-2,1,4,10,-8],[7,5,10,-6,7,-7,-5,-6,-2,6],[9,9,-8,8,2,9,5,-9,-1,7],[-10,-2,-7,6,7,5,7,-9,-7,-7]],[[3,10,-9,5,4,7,6,9,-10,-3],[8,-4,-2,-2,-8,-7,4,-10,-6,10],[-7,-6,-8,6,-1,-4,9,-3,-9,-9],[5,-9,-3,9,-4,-1,-8,3,3,4],[10,-4,4,-9,4,9,4,-8,8,8],[8,2,8,4,7,-7,5,-6,-9,-3],[1,-2,-1,5,8,1,5,-4,9,6],[5,2,5,9,1,4,-4,-8,-7,-4],[6,-2,9,6,5,3,-5,10,-3,1],[10,7,-6,-1,-7,9,-10,-6,9,4],[-6,-2,4,-1,2,10,-9,-6,-3,7],[1,5,7,8,-5,-9,-1,-2,-4,3],[-4,6,1,10,8,-4,-5,10,-2,7],[-1,8,7,1,10,-7,-7,10,4,2],[7,-3,-6,-4,1,4,8,-6,-2,6]],[[10,-6,6,-7,-6,-6,-6,7,2,-10],[3,-5,-8,7,9,-1,7,-8,-3,-5],[5,-4,-8,4,-2,-5,10,7,-2,-7],[-8,-1,-6,-7,-3,8,2,10,-2,-2],[-1,-1,-6,1,5,-10,-8,7,10,-3],[-6,3,-4,10,1,2,8,5,4,-5],[-7,9,5,-9,9,10,-4,3,-7,-4],[4,2,-9,-9,4,9,6,7,5,-10],[8,10,-2,2,8,10,1,-6,-1,-5],[-7,-6,-4,8,-9,-6,6,-10,10,2],[7,-10,5,1,8,-1,-10,-10,10,-6],[4,-9,-7,-3,-3,3,-6,-10,-8,7],[7,-1,-4,5,-8,-4,-2,-5,4,-6],[-2,6,-3,-8,-7,4,-2,-5,7,10],[-1,-8,-1,-2,10,1,8,-9,-4,-9]],[[-4,7,10,-2,-9,10,1,3,-2,5],[2,5,3,-8,-5,-8,-1,-4,-6,-6],[9,5,6,9,2,4,-2,-5,-5,4],[1,6,8,3,-6,-10,-6,4,4,4],[9,-1,6,-6,8,-10,3,-1,8,4],[2,7,-1,-2,4,3,3,-6,10,8],[1,9,6,4,5,-5,4,-6,5,-9],[3,4,-6,5,-2,5,2,9,5,9],[-3,-6,-8,-1,-10,4,2,1,8,-5],[-8,-8,-6,6,2,3,10,2,2,1],[-4,5,-2,-6,-10,-3,-5,9,-7,5],[2,5,-7,-10,-10,1,3,-2,2,-5],[10,5,8,9,10,-5,3,-4,6,-1],[4,-10,10,2,-9,6,-7,-7,6,-2],[-9,9,-8,-4,7,-3,-7,-10,5,9]],[[-2,-7,8,6,9,10,-9,-2,4,-3],[9,-3,-9,3,4,-1,-7,-7,-10,6],[-1,7,-7,-6,5,1,-7,2,7,1],[-5,10,-1,-4,-8,-10,9,10,8,-7],[7,-9,-2,10,4,1,-6,-1,7,-7],[8,-7,-7,-4,-5,2,-7,-8,-1,8],[-2,7,9,-4,-5,-3,-8,-1,9,4],[6,-6,6,-4,4,2,-1,3,-9,8],[8,7,4,-1,-3,7,-10,2,8,-2],[-8,-8,5,8,-8,6,-10,10,-2,6],[-7,-5,-7,2,3,-8,8,7,-5,7],[-5,-7,-9,10,-1,5,1,-6,6,-4],[4,9,5,-7,-5,6,-1,-5,-2,-10],[-3,-3,-6,5,-7,-1,10,-2,8,-7],[-6,-2,-6,7,-2,-2,-3,-1,4,-3]],[[4,3,-5,-9,4,7,7,-9,6,2],[3,5,1,-7,2,7,3,10,-4,-1],[2,-2,-7,3,-5,1,3,5,4,10],[-1,1,-8,2,-9,4,-4,10,5,5],[10,-9,-4,8,6,3,6,1,-5,8],[9,5,6,5,1,-3,-7,-6,5,-8],[-2,10,5,2,6,3,-1,1,6,-3],[5,9,-6,-1,-9,-4,10,-8,7,4],[-1,-1,5,-2,-7,9,-8,-3,7,9],[-5,-8,-7,9,-8,9,9,-2,3,7],[-8,1,-9,2,8,-2,4,-7,6,-7],[8,4,6,-4,-9,-9,9,10,-4,-4],[4,5,-5,9,8,-8,1,-6,5,8],[-10,8,8,-9,-4,5,10,6,-4,-7],[-2,-1,-6,-2,4,6,8,5,-3,8]],[[-1,5,-5,-5,5,-1,8,10,6,6],[1,-6,-5,4,-7,-7,-5,10,-3,-7],[8,5,-10,1,-6,-8,8,-7,4,2],[4,-2,2,-9,6,3,-5,-3,3,1],[-2,10,10,4,1,-9,-5,-5,2,10],[-1,-3,1,-1,1,-6,10,2,1,8],[-2,-8,8,4,7,-10,-8,7,1,4],[10,3,-3,-4,3,-8,-6,1,-10,-4],[10,-7,8,-8,2,9,9,3,-8,-8],[-6,-5,-1,-8,3,9,-7,2,10,2],[-9,1,-6,-9,1,5,-4,-2,9,7],[2,-5,-2,-4,-6,-2,1,2,10,-2],[-1,-8,9,9,10,2,-1,2,-6,6],[5,9,-3,-1,-4,-6,2,-9,4,1],[-5,-5,-3,-2,3,3,5,-6,-2,-3]],[[-2,3,-3,-4,-4,10,-7,-10,3,-9],[9,6,3,2,1,-6,-2,-6,5,1],[-3,1,-9,-2,10,-1,-5,-2,-1,6],[10,4,2,9,7,9,5,2,10,6],[-7,-10,4,-1,-6,6,2,10,-7,1],[10,-6,9,-9,-3,-8,2,3,10,10],[2,4,5,7,-4,7,-10,1,10,10],[-4,4,-6,1,-10,2,6,-5,9,-4],[4,-8,-4,-6,10,-10,4,-10,8,6],[2,-9,3,3,9,6,-1,-10,5,1],[-3,2,4,8,5,1,4,-8,-5,-1],[-10,-8,1,-6,-3,6,10,3,-1,-10],[-9,-6,1,9,6,-10,5,5,-3,6],[10,2,-1,-7,-10,-9,-8,-9,10,4],[-8,-2,2,10,-10,3,-10,3,-4,4]],[[-7,-10,-9,-3,8,6,-4,10,-8,3],[-9,-2,-3,-10,5,-10,8,-5,-2,-7],[8,8,-2,7,-9,9,-7,6,-4,-9],[-10,-1,-1,-5,-7,-3,6,4,-8,-7],[1,4,5,-10,-6,-7,-5,5,5,9],[2,6,1,-5,2,5,-8,-1,-7,-1],[9,-9,6,-10,-6,2,1,8,-9,1],[5,-3,3,5,7,4,3,10,-9,-10],[-1,5,-2,4,-7,3,10,-6,-1,6],[-6,4,6,-9,-6,2,-3,1,-3,9],[9,4,9,4,-1,-10,9,-6,-9,1],[-4,-5,1,6,-1,4,8,-1,7,7],[-4,-7,-2,-9,8,8,-5,10,-1,2],[1,3,-3,6,-10,10,-1,-8,-9,-4],[8,-2,-5,1,-9,9,8,-1,6,2]],[[2,1,-8,8,7,8,-6,-10,-3,8],[-3,-5,-8,-9,6,10,3,3,10,3],[-5,-5,-1,1,-6,-7,-3,8,-1,-6],[8,4,9,7,1,9,10,7,8,7],[-7,1,-7,3,-5,4,7,9,7,9],[3,-4,-1,6,8,-1,8,-5,10,4],[9,1,5,-3,-5,10,10,4,-4,-9],[4,7,2,6,2,-7,9,6,-9,8],[-3,5,4,-5,8,1,5,-3,-10,9],[10,-2,6,-2,-8,3,9,-5,5,-1],[5,6,-10,7,7,-1,-3,-5,10,8],[-10,-9,8,1,-7,10,-6,4,-5,-7],[8,-1,-2,10,6,10,-8,6,-5,1],[1,6,8,-3,-10,5,-10,-6,5,-2],[5,-6,3,1,8,9,-3,-9,4,4]],[[-4,-1,5,7,-5,-2,3,5,1,3],[8,-1,9,-2,3,7,6,2,-5,-3],[7,5,3,-3,6,4,-10,-6,6,-9],[5,4,4,-3,4,3,9,-9,-6,9],[-10,7,-9,-8,1,3,5,-5,5,10],[-4,-9,9,-7,4,-8,-8,-4,-7,1],[-2,-6,-2,-6,1,-6,-6,-7,-5,-9],[-10,-3,3,-5,-4,2,1,-2,9,1],[1,6,-4,-2,7,10,-2,8,-2,8],[9,1,8,-6,1,-8,5,-2,6,8],[7,3,-10,-7,-3,-10,4,4,-5,8],[8,-8,9,1,-4,-1,6,-2,-4,-1],[-3,1,2,-9,6,3,-5,-8,-1,-2],[-8,9,6,10,-2,8,10,5,5,-9],[3,-6,2,-5,-2,9,-9,-2,2,6]]], dtype = "int16")#candidate|3964|(16, 15, 10)|const|int16
const_3965 = relay.const([[[3,2,-3,-7,-2,-10,7,6,3,-3],[10,8,6,10,-10,1,-3,7,-5,4],[-5,-10,4,2,-8,6,-9,-7,-10,-4],[-3,4,-5,-2,5,-10,2,-3,-8,4],[4,-3,6,-7,10,-7,-4,9,-9,-2],[8,-9,3,-7,-8,6,-2,-4,2,5],[3,-5,10,-10,8,7,5,-8,-9,9],[5,1,8,-6,-9,2,-2,10,-4,2],[2,8,7,-6,-1,4,-4,-3,-10,-3],[-7,-8,-4,10,-9,-8,6,-10,1,7],[-5,-8,-6,1,8,-3,-9,-6,3,8],[2,5,-1,-1,3,6,1,-6,5,-2],[-1,9,-8,-10,-3,-3,4,5,4,-2],[3,6,-10,-10,-10,-7,7,-1,-3,8],[-1,4,-10,5,-2,3,-4,9,1,-8]],[[-2,-4,-3,6,7,-5,-6,6,-6,1],[7,-3,-1,5,-10,5,-2,-10,5,2],[-1,-2,5,-2,10,-9,7,8,-4,2],[-9,-5,5,5,-3,-1,3,-9,3,9],[7,10,2,2,4,10,-10,-2,2,4],[-4,10,-8,6,-2,-5,-5,-3,-5,-2],[10,10,-7,-4,10,4,10,-3,-5,-2],[-6,-8,-9,7,-7,-3,-1,6,5,-6],[-5,-1,6,-7,-3,-8,3,-1,6,-8],[-8,-9,-4,-6,-4,-6,-7,-5,-2,-4],[1,-5,9,-9,-5,7,8,2,-2,2],[3,4,-6,-2,3,-5,-9,9,6,4],[-4,7,-8,3,9,3,-3,1,8,-8],[-3,-5,3,2,-1,3,7,7,-8,5],[-4,-9,-9,-6,6,-8,-7,1,7,1]],[[10,-3,-3,4,9,-9,10,-1,10,6],[1,7,6,-2,-3,-1,7,10,6,-3],[3,-9,-2,4,8,-8,-3,-9,-4,2],[-3,10,10,-2,-4,-1,-9,-2,9,-2],[5,5,6,-8,4,8,4,-9,-8,9],[8,-10,10,-9,-9,7,-3,-3,8,-9],[-1,2,-5,-10,-2,6,8,-8,-10,-7],[-9,5,7,-3,7,-9,-3,4,2,2],[2,5,-5,-8,1,6,-10,-6,-6,1],[-4,-2,1,-4,7,-6,-3,-8,-3,3],[-2,6,7,10,-2,9,-1,-1,-6,-5],[9,3,-2,10,7,-9,-2,2,6,7],[3,4,-6,8,7,6,-5,-2,9,-2],[7,5,6,-1,7,2,3,-6,8,10],[7,5,-4,-9,-9,9,-2,-5,2,-5]],[[-3,9,-3,-4,8,8,1,-9,2,-10],[-1,-9,3,-3,10,-4,-3,1,-9,-8],[-9,4,2,5,-3,7,3,-7,1,-1],[-8,-6,-1,8,9,9,-2,10,-6,10],[-1,3,6,-10,10,8,10,10,10,-1],[1,9,-3,-9,-5,10,9,-9,3,-10],[3,-2,1,-2,7,-9,3,4,-8,-5],[-4,-8,8,8,7,6,-7,2,-8,8],[-10,-6,9,-9,4,10,10,-3,-5,2],[10,-3,6,-4,2,4,10,-6,-1,-6],[10,-5,3,-3,-10,10,2,-8,9,-5],[-5,-4,8,-4,5,-5,5,9,9,-8],[-6,-10,2,-7,1,3,-10,3,-6,-8],[-8,-10,-3,2,-1,-1,-9,-3,9,5],[3,-8,-6,2,9,-7,-3,9,-5,7]],[[1,3,9,4,-10,-9,-8,6,7,8],[-8,-10,-1,8,-10,-2,-3,3,-4,1],[6,5,-7,8,8,10,10,-8,1,-6],[9,3,4,-5,3,-2,-5,4,7,6],[9,-3,7,9,5,10,5,7,9,10],[7,-4,-9,2,2,1,-3,-10,6,-8],[-7,5,2,-5,-4,-7,-7,1,9,1],[-3,-3,-9,-7,-4,-5,5,-5,2,2],[-5,6,9,-9,3,2,-4,-4,-7,7],[-8,-2,-2,2,7,9,2,-5,3,1],[-3,3,5,-10,8,4,10,1,-3,6],[-6,3,10,-8,1,10,10,1,1,-10],[1,-7,9,2,2,1,5,-5,-1,10],[2,-6,-3,2,10,-7,5,1,3,-8],[-5,10,-1,5,-9,6,2,4,10,-3]],[[9,1,-5,9,-10,-2,6,-3,8,10],[2,7,-7,3,-8,-8,-8,10,-5,-1],[6,10,-5,10,2,1,4,-7,-10,8],[7,-6,9,8,6,9,-3,5,-1,-3],[5,-6,-3,-9,3,2,5,7,-3,8],[-6,-3,-5,1,3,8,8,-6,4,4],[7,9,4,-8,1,-8,2,-8,-2,-10],[2,3,-9,-3,-6,-2,2,7,-9,5],[-10,9,-4,6,5,-1,5,9,4,-8],[-8,5,4,-8,-6,3,5,7,-8,-7],[2,-1,3,10,-9,-10,-1,-9,-9,-9],[9,3,5,-5,-5,-9,-10,4,8,3],[-2,-6,-7,1,-1,3,6,6,-5,6],[3,9,-6,9,4,-3,4,-3,-4,7],[7,-7,-5,4,-4,-2,-8,2,-3,-7]],[[-2,5,-10,7,3,1,-3,10,-1,-9],[-7,-10,3,6,-3,-3,3,-1,8,-9],[1,10,-8,5,7,4,7,8,8,-6],[-8,5,10,-4,-3,1,3,-1,4,-2],[-10,-6,2,8,1,-10,4,-2,-3,-5],[1,4,7,-7,-9,-3,-7,5,4,-9],[7,6,7,8,-4,8,-8,9,8,-6],[7,6,-8,-5,-6,9,-6,-9,-1,-6],[-1,-10,7,-4,-7,3,-10,2,-2,2],[1,-5,4,-1,10,-10,2,-2,1,-7],[8,6,9,-8,5,10,1,5,7,2],[5,-10,4,-9,8,5,4,-4,9,5],[-1,-10,-10,10,2,7,-6,4,9,-6],[7,-2,5,5,7,-8,5,-3,-2,4],[-6,1,10,-1,9,7,-1,1,5,9]],[[-6,-2,-6,7,7,4,-4,5,-10,-4],[-4,-9,2,-10,-5,-10,-6,5,-7,-2],[6,8,-8,-6,9,-9,3,-9,-7,-1],[-8,7,-3,-7,-5,-5,-2,-10,7,-1],[8,-1,-10,-7,9,-1,-10,10,1,4],[-6,-4,3,1,2,8,3,-2,-2,-2],[-8,8,3,1,-7,7,-3,4,-9,-6],[6,-2,5,-2,4,8,8,9,-5,-5],[-3,-8,7,2,4,8,6,-6,5,-8],[3,10,3,5,10,-10,6,1,7,-9],[5,-10,-9,-2,6,5,5,5,7,-5],[1,1,-3,-1,8,-1,9,-2,10,3],[3,7,5,5,3,-8,5,-2,-2,9],[6,10,1,-4,-5,7,6,7,6,-1],[4,-3,-9,-7,1,8,6,-3,-2,-8]],[[-3,-7,10,10,8,7,3,10,7,4],[3,-5,1,-6,2,-10,-10,6,10,8],[-9,9,4,-5,-5,9,2,7,-2,4],[8,1,-2,-9,-4,10,3,7,-9,10],[-3,3,5,-9,-2,10,-9,-9,-7,3],[7,-7,5,10,8,7,1,7,8,10],[10,-10,-1,10,-7,-9,6,-9,-10,4],[-10,-9,9,-4,3,8,6,-2,9,4],[5,-4,-9,-4,1,7,9,10,-4,-8],[2,4,-6,-2,-10,-2,-10,-8,9,-8],[-1,2,10,1,-8,-5,-5,-6,-5,7],[-5,-10,7,-3,-1,-7,-5,4,10,-1],[4,-9,-5,1,5,5,9,6,3,-4],[-2,9,-1,5,8,-2,-4,-3,-5,-8],[4,-4,-9,1,-2,6,-8,-1,8,10]],[[2,2,2,4,10,10,7,7,4,8],[4,8,-9,-9,-5,-6,-1,-2,2,10],[9,-5,4,2,1,2,2,-7,10,-9],[-5,3,-1,-8,-2,6,8,10,7,-10],[10,4,-3,-6,-7,10,-9,-7,-8,5],[3,3,-5,1,-3,-10,2,-8,5,10],[8,-5,2,7,-6,2,-4,-1,6,-8],[-3,-3,-2,-2,4,8,-3,-8,4,-9],[-8,2,-5,-8,6,-1,4,-8,6,3],[3,3,6,-2,-7,-3,-3,-6,9,-9],[-1,8,6,-4,-5,2,2,-5,-7,9],[10,-8,8,-1,-7,5,-3,-5,-6,-1],[8,10,-9,8,-2,9,-10,6,2,-6],[8,-8,4,-9,-4,3,2,-2,8,6],[-9,-3,3,-7,-7,-5,-4,-5,6,-1]],[[4,2,7,8,8,-7,-2,-3,2,-1],[3,-3,9,-5,3,7,10,-5,7,-2],[9,9,-2,6,2,-4,-3,2,-8,-9],[1,-10,5,-7,9,5,-1,-9,7,-8],[3,4,10,10,-2,-8,-4,5,-2,-2],[-4,-10,3,9,-5,3,-10,5,-4,9],[-3,1,5,-7,-10,9,9,-8,-7,4],[-7,-1,3,-8,-1,3,4,-3,9,6],[-10,1,4,-2,10,4,-3,6,-1,5],[3,-7,-1,8,10,-9,-10,-8,4,5],[5,3,4,-6,-6,-8,10,-8,6,10],[9,-6,10,3,-3,-9,-10,6,2,1],[-4,8,6,4,-3,8,4,3,8,-9],[6,9,8,10,-9,9,1,7,7,-9],[-6,4,-3,-3,5,-1,-9,5,-8,-9]],[[-7,10,10,-3,-9,-7,9,4,-10,-2],[10,-4,-6,8,5,10,-10,9,-10,-4],[7,5,-5,-10,7,-10,7,-5,4,-6],[-3,-10,-9,-10,3,9,7,6,2,-7],[-7,-3,10,9,1,2,4,-6,2,1],[10,-5,-3,-1,6,1,2,10,-3,-5],[-4,10,-8,10,-2,7,-2,-1,5,7],[7,-5,-3,-4,-3,1,-5,-3,7,4],[6,-1,6,-3,-1,10,-10,10,3,-10],[-2,-2,-3,-1,2,-8,-9,-9,1,3],[6,-2,2,2,6,10,4,-5,10,-7],[-1,1,4,-4,3,8,3,-6,4,10],[9,-9,5,1,-2,-6,-1,-5,-6,-1],[6,-6,1,-6,9,6,10,-2,3,-10],[10,-10,-4,10,-5,1,-10,2,1,8]],[[-8,10,2,-2,-5,-2,10,-10,8,-4],[-10,-4,-4,-4,8,4,8,3,6,-7],[-8,8,2,10,-5,-4,-1,-7,-7,-9],[5,-1,7,-3,9,-4,10,5,-7,3],[-1,-8,5,9,-8,-9,2,-8,-3,-2],[2,9,7,5,9,7,-6,4,10,-5],[4,5,-1,-6,1,-7,5,6,-8,-5],[10,-8,-7,-8,-10,9,-5,9,-5,-2],[-3,1,5,-10,-10,-1,-9,5,-3,-6],[5,6,-10,-8,10,-5,-1,10,6,10],[-5,6,-9,-1,-5,-7,2,10,6,9],[10,-8,-10,4,8,-2,4,-8,-9,9],[-6,2,-8,2,-2,2,4,-10,8,-2],[9,-3,2,-10,-2,2,-5,-8,1,-7],[-10,5,-8,-2,-1,7,8,7,-1,8]],[[-5,-1,-9,1,8,2,-8,-6,4,-5],[10,-6,-9,-8,-9,-4,-1,5,6,1],[-8,2,2,2,-5,2,6,6,3,6],[4,-8,-6,6,-3,-6,2,4,-5,1],[-1,7,-4,-3,-9,-1,-2,8,6,-10],[1,-7,-5,8,-9,-1,-5,-10,-1,6],[-5,-3,-7,-4,2,-9,1,7,-1,7],[-7,2,7,9,-6,-8,-1,7,1,-9],[9,-8,-6,-6,2,-6,-2,-1,10,-8],[4,-9,-6,-2,-2,-10,1,-9,4,3],[-1,-7,9,3,-7,-8,-9,-7,-7,-2],[10,-8,-1,-9,6,-5,2,1,1,1],[-7,10,-9,-2,5,-3,-7,7,10,7],[9,3,3,3,10,-3,-4,-6,9,7],[-2,-1,3,-1,4,-9,1,4,-7,-9]],[[10,7,-2,-5,9,-4,-6,3,3,-4],[-3,1,6,7,2,-4,5,-4,-4,-7],[5,-5,-8,-10,-2,1,-9,7,-8,1],[-10,10,-4,-2,7,3,-5,-3,-7,-6],[-9,-4,9,-4,-8,7,-7,3,5,-2],[-9,4,-3,6,2,-1,-1,9,-10,9],[7,-8,-6,8,10,-4,6,2,-7,-3],[2,-1,-1,-7,5,-1,-3,-7,-1,2],[8,8,-6,-5,-9,-3,2,-6,-6,6],[-8,-4,-5,1,9,-5,9,-10,6,-7],[6,7,-4,3,-7,-1,-7,9,-7,7],[-6,-2,-10,2,-10,2,-9,-5,6,-2],[8,-10,-6,6,1,-9,10,4,6,5],[-4,-3,5,-5,8,4,9,-3,-2,10],[4,2,3,-1,1,4,-2,8,4,6]],[[1,8,-3,6,-9,1,-8,-9,-9,1],[-8,-7,9,-6,9,5,-4,-9,-3,4],[-3,-7,-10,-5,7,-2,8,-5,-5,2],[-5,-5,7,5,10,3,-8,6,7,10],[-7,10,2,-2,6,-10,-10,-7,-10,8],[6,5,2,-2,5,6,4,7,1,2],[5,8,8,2,-10,8,-2,9,-6,-6],[5,-3,7,-5,-9,-6,9,-10,9,-5],[-4,6,7,1,-8,-4,-6,4,-9,2],[7,4,1,-5,6,9,4,-6,-3,-6],[-4,6,9,3,-2,-6,4,7,4,4],[-1,-1,-10,-5,4,4,2,-7,-3,-9],[-7,5,6,5,-1,1,-5,6,1,-8],[3,-2,3,7,2,-2,2,-10,-9,-10],[5,-2,-6,-6,2,-2,6,-9,5,-7]]], dtype = "int16")#candidate|3965|(16, 15, 10)|const|int16
bop_3966 = relay.less(const_3964.astype('bool'), relay.reshape(const_3965.astype('bool'), relay.shape_of(const_3964))) # shape=(16, 15, 10)
output = relay.Tuple([bop_3966,])
output2 = relay.Tuple([bop_3966,])
func_3974 = relay.Function([], output)
mod['func_3974'] = func_3974
mod = relay.transform.InferType()(mod)
output = func_3974()
func_3975 = relay.Function([], output)
mutated_mod['func_3975'] = func_3975
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2010_call = mod.get_global_var('func_2010')
func_2011_call = mutated_mod.get_global_var('func_2011')
call_3984 = relay.TupleGetItem(func_2010_call(), 0)
call_3985 = relay.TupleGetItem(func_2011_call(), 0)
func_3268_call = mod.get_global_var('func_3268')
func_3269_call = mutated_mod.get_global_var('func_3269')
call_4003 = relay.TupleGetItem(func_3268_call(), 0)
call_4004 = relay.TupleGetItem(func_3269_call(), 0)
output = relay.Tuple([call_3984,call_4003,])
output2 = relay.Tuple([call_3985,call_4004,])
func_4005 = relay.Function([], output)
mod['func_4005'] = func_4005
mod = relay.transform.InferType()(mod)
output = func_4005()
func_4006 = relay.Function([], output)
mutated_mod['func_4006'] = func_4006
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2866_call = mod.get_global_var('func_2866')
func_2867_call = mutated_mod.get_global_var('func_2867')
call_4039 = func_2866_call()
call_4040 = func_2866_call()
func_3808_call = mod.get_global_var('func_3808')
func_3809_call = mutated_mod.get_global_var('func_3809')
call_4046 = relay.TupleGetItem(func_3808_call(), 2)
call_4047 = relay.TupleGetItem(func_3809_call(), 2)
func_2616_call = mod.get_global_var('func_2616')
func_2620_call = mutated_mod.get_global_var('func_2620')
var_4051 = relay.var("var_4051", dtype = "uint8", shape = (112,))#candidate|4051|(112,)|var|uint8
var_4052 = relay.var("var_4052", dtype = "uint8", shape = (70, 2))#candidate|4052|(70, 2)|var|uint8
call_4050 = relay.TupleGetItem(func_2616_call(relay.reshape(var_4051.astype('uint8'), [112,]), relay.reshape(var_4052.astype('uint8'), [140,]), ), 7)
call_4053 = relay.TupleGetItem(func_2620_call(relay.reshape(var_4051.astype('uint8'), [112,]), relay.reshape(var_4052.astype('uint8'), [140,]), ), 7)
output = relay.Tuple([call_4039,call_4046,call_4050,var_4051,var_4052,])
output2 = relay.Tuple([call_4040,call_4047,call_4053,var_4051,var_4052,])
func_4061 = relay.Function([var_4051,var_4052,], output)
mod['func_4061'] = func_4061
mod = relay.transform.InferType()(mod)
mutated_mod['func_4061'] = func_4061
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4061_call = mutated_mod.get_global_var('func_4061')
var_4063 = relay.var("var_4063", dtype = "uint8", shape = (112,))#candidate|4063|(112,)|var|uint8
var_4064 = relay.var("var_4064", dtype = "uint8", shape = (70, 2))#candidate|4064|(70, 2)|var|uint8
call_4062 = func_4061_call(var_4063,var_4064,)
output = call_4062
func_4065 = relay.Function([var_4063,var_4064,], output)
mutated_mod['func_4065'] = func_4065
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4144 = relay.const([[[-8.030495,-9.996840],[0.280002,-4.905358],[-5.016510,3.478927],[-9.445042,-9.468702],[-5.336256,-2.591016],[-1.466405,-7.392563],[2.236619,-7.828262],[-2.981976,9.685078],[9.136355,6.979598],[6.351736,6.691274],[-7.783559,0.547017],[6.232571,1.604656],[5.517688,-4.495721]],[[-8.962008,-0.237584],[0.880680,6.085126],[2.407500,-3.727450],[3.823281,6.018207],[3.943808,-7.367709],[3.275519,7.660072],[5.332672,-7.382186],[-6.513702,3.241555],[-5.599672,-2.021794],[-1.495626,4.639713],[-8.595033,7.399453],[9.874589,6.171891],[7.408334,-0.455577]],[[6.191841,9.502767],[-6.592050,-1.463479],[6.955845,6.120457],[2.305202,6.691244],[6.563853,5.728735],[-4.160148,9.631239],[2.158222,8.628335],[-9.097249,-4.181125],[1.809424,4.454426],[1.166377,-5.314611],[5.633173,-4.193897],[0.080482,-7.133029],[-8.013580,-7.895166]],[[-2.459718,-0.150055],[-7.605558,-4.470230],[3.262320,8.372620],[8.855386,-4.029341],[-3.749814,9.725128],[-0.261397,-3.767023],[6.525648,9.819936],[1.435667,-3.788601],[3.318761,1.617623],[-3.538684,4.415797],[-6.871306,-0.176472],[5.346273,9.092127],[3.261989,4.088112]],[[-2.518805,8.459475],[-6.397694,-0.179316],[2.815193,-9.874457],[6.402916,-3.861708],[0.771207,-9.115287],[-0.198149,6.307093],[9.481274,1.812559],[2.645928,4.805503],[0.564080,9.899478],[1.034334,4.472044],[7.446657,7.433440],[4.907895,-2.906748],[3.848447,9.792944]],[[-7.769663,4.834808],[1.100507,-2.993824],[0.184202,-8.641789],[8.293546,3.043324],[3.404278,5.661117],[-2.230131,-6.829985],[-8.254452,-9.952023],[2.767043,-9.193887],[2.701694,1.627038],[-5.394747,7.418998],[9.935156,-6.457690],[-3.603818,1.766612],[-1.915170,-1.408080]],[[-5.808583,3.602927],[0.708273,-8.498664],[3.717074,-5.056781],[5.434286,6.170243],[-4.109417,4.082389],[-1.858469,-2.925991],[8.122966,9.384904],[-2.567996,-0.143015],[-9.816468,9.155739],[-7.605279,-7.253635],[-0.432787,-6.684586],[-5.751692,-2.963176],[-4.280144,1.319553]],[[3.063025,8.398202],[5.630777,7.386604],[-7.492462,-9.614007],[0.225954,4.768809],[-3.290919,0.837862],[-6.266878,-2.755609],[0.241504,7.703339],[-3.397013,-5.097431],[-4.707457,4.843627],[-6.141556,0.256109],[-4.441078,9.632389],[-8.077425,5.280470],[-6.910666,1.071255]],[[-3.008592,-9.435010],[-6.828452,-9.251894],[-8.071067,6.406677],[-9.608639,-7.022097],[3.911423,-5.928101],[-5.709513,6.058802],[-6.489166,1.668122],[0.764401,7.210547],[-1.933988,9.771992],[-1.359386,2.821664],[-1.098397,6.167711],[9.613004,-8.410152],[-3.520387,8.766154]],[[-5.149180,1.469302],[4.729749,-0.067163],[0.924074,4.796531],[8.777767,5.527500],[-2.407964,-2.490491],[2.258917,4.852234],[6.031161,8.085054],[-2.758645,-7.149139],[2.183482,5.304505],[-0.047528,9.346234],[-9.368763,4.279765],[3.114653,5.652265],[-7.118092,-9.155595]],[[6.984719,-6.161096],[0.715480,-1.556573],[-8.891467,8.181319],[-4.154322,7.123722],[-6.528987,3.749689],[8.838549,-8.260472],[3.899663,-5.562534],[1.710236,9.354295],[-0.700125,4.205129],[6.202790,-4.020460],[1.206341,4.406654],[-5.937740,-7.120401],[6.673309,8.835478]],[[3.976278,6.585460],[6.218806,-8.398687],[-6.315874,-1.132309],[3.800205,8.197654],[2.160571,1.302667],[4.188740,5.984363],[0.065281,-7.913945],[8.467688,8.962603],[6.754313,6.296184],[-1.420543,6.842545],[5.470071,7.017716],[1.318052,0.675278],[-1.385354,9.362915]],[[1.521158,-3.548230],[7.609745,4.471664],[-3.402105,9.822757],[3.176988,0.630760],[-0.888596,-1.373543],[-8.659584,-1.374088],[-5.612278,-1.199214],[-2.476220,-0.039643],[-0.725159,-6.306635],[7.722337,-7.166708],[-1.510260,4.503132],[-8.437778,1.127346],[7.024998,-8.969644]],[[-9.176318,-2.016320],[-8.050201,6.438677],[-1.606982,-7.054942],[-6.577290,-6.667083],[-6.291526,-0.033921],[-1.705826,-0.008391],[-0.096699,0.951885],[-3.997535,9.470822],[1.567932,1.629218],[-7.256968,-8.627060],[4.079531,-9.025640],[-2.458533,4.996147],[9.227814,5.156612]],[[-0.444958,8.293675],[-5.265836,-9.765458],[-9.990113,9.053023],[4.581623,-8.391613],[0.582247,1.268383],[4.570344,1.223515],[-7.012105,5.249571],[-9.204248,-4.814356],[-5.804213,6.416144],[-7.840681,0.740670],[6.418634,-0.626692],[-9.512828,-2.570152],[-8.224605,-1.445486]],[[6.800758,6.253182],[-7.536435,-7.487624],[8.682161,2.519796],[-6.246529,-2.983550],[4.820753,7.085893],[-2.108706,9.869736],[-5.315789,6.232240],[2.137008,7.411696],[0.344168,4.279271],[6.495940,-7.478473],[-3.798127,-1.424924],[-1.010728,5.215129],[6.004214,-9.023040]]], dtype = "float32")#candidate|4144|(16, 13, 2)|const|float32
uop_4145 = relay.exp(const_4144.astype('float32')) # shape=(16, 13, 2)
output = relay.Tuple([uop_4145,])
output2 = relay.Tuple([uop_4145,])
func_4150 = relay.Function([], output)
mod['func_4150'] = func_4150
mod = relay.transform.InferType()(mod)
mutated_mod['func_4150'] = func_4150
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4150_call = mutated_mod.get_global_var('func_4150')
call_4151 = func_4150_call()
output = call_4151
func_4152 = relay.Function([], output)
mutated_mod['func_4152'] = func_4152
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1066_call = mod.get_global_var('func_1066')
func_1068_call = mutated_mod.get_global_var('func_1068')
call_4158 = relay.TupleGetItem(func_1066_call(), 0)
call_4159 = relay.TupleGetItem(func_1068_call(), 0)
uop_4162 = relay.sqrt(call_4158.astype('float32')) # shape=(10, 14, 13)
uop_4164 = relay.sqrt(call_4159.astype('float32')) # shape=(10, 14, 13)
bop_4173 = relay.bitwise_and(uop_4162.astype('uint8'), relay.reshape(call_4158.astype('uint8'), relay.shape_of(uop_4162))) # shape=(10, 14, 13)
bop_4176 = relay.bitwise_and(uop_4164.astype('uint8'), relay.reshape(call_4159.astype('uint8'), relay.shape_of(uop_4164))) # shape=(10, 14, 13)
func_3491_call = mod.get_global_var('func_3491')
func_3495_call = mutated_mod.get_global_var('func_3495')
var_4184 = relay.var("var_4184", dtype = "bool", shape = ())#candidate|4184|()|var|bool
var_4185 = relay.var("var_4185", dtype = "bool", shape = (80,))#candidate|4185|(80,)|var|bool
call_4183 = func_3491_call(relay.reshape(var_4184.astype('bool'), []), relay.reshape(var_4185.astype('bool'), [1, 5, 16]), )
call_4186 = func_3491_call(relay.reshape(var_4184.astype('bool'), []), relay.reshape(var_4185.astype('bool'), [1, 5, 16]), )
func_3974_call = mod.get_global_var('func_3974')
func_3975_call = mutated_mod.get_global_var('func_3975')
call_4190 = relay.TupleGetItem(func_3974_call(), 0)
call_4191 = relay.TupleGetItem(func_3975_call(), 0)
output = relay.Tuple([bop_4173,call_4183,var_4184,var_4185,call_4190,])
output2 = relay.Tuple([bop_4176,call_4186,var_4184,var_4185,call_4191,])
func_4193 = relay.Function([var_4184,var_4185,], output)
mod['func_4193'] = func_4193
mod = relay.transform.InferType()(mod)
var_4194 = relay.var("var_4194", dtype = "bool", shape = ())#candidate|4194|()|var|bool
var_4195 = relay.var("var_4195", dtype = "bool", shape = (80,))#candidate|4195|(80,)|var|bool
output = func_4193(var_4194,var_4195,)
func_4196 = relay.Function([var_4194,var_4195,], output)
mutated_mod['func_4196'] = func_4196
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3024_call = mod.get_global_var('func_3024')
func_3025_call = mutated_mod.get_global_var('func_3025')
call_4201 = relay.TupleGetItem(func_3024_call(), 0)
call_4202 = relay.TupleGetItem(func_3025_call(), 0)
var_4214 = relay.var("var_4214", dtype = "float64", shape = (10, 14, 13))#candidate|4214|(10, 14, 13)|var|float64
bop_4215 = relay.add(call_4201.astype('uint32'), relay.reshape(var_4214.astype('uint32'), relay.shape_of(call_4201))) # shape=(10, 14, 13)
bop_4218 = relay.add(call_4202.astype('uint32'), relay.reshape(var_4214.astype('uint32'), relay.shape_of(call_4202))) # shape=(10, 14, 13)
bop_4224 = relay.less(bop_4215.astype('bool'), relay.reshape(call_4201.astype('bool'), relay.shape_of(bop_4215))) # shape=(10, 14, 13)
bop_4227 = relay.less(bop_4218.astype('bool'), relay.reshape(call_4202.astype('bool'), relay.shape_of(bop_4218))) # shape=(10, 14, 13)
func_3183_call = mod.get_global_var('func_3183')
func_3185_call = mutated_mod.get_global_var('func_3185')
call_4250 = func_3183_call()
call_4251 = func_3183_call()
output = relay.Tuple([bop_4224,call_4250,])
output2 = relay.Tuple([bop_4227,call_4251,])
func_4254 = relay.Function([var_4214,], output)
mod['func_4254'] = func_4254
mod = relay.transform.InferType()(mod)
mutated_mod['func_4254'] = func_4254
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4255 = relay.var("var_4255", dtype = "float64", shape = (10, 14, 13))#candidate|4255|(10, 14, 13)|var|float64
func_4254_call = mutated_mod.get_global_var('func_4254')
call_4256 = func_4254_call(var_4255)
output = call_4256
func_4257 = relay.Function([var_4255], output)
mutated_mod['func_4257'] = func_4257
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2407_call = mod.get_global_var('func_2407')
func_2409_call = mutated_mod.get_global_var('func_2409')
call_4273 = relay.TupleGetItem(func_2407_call(), 0)
call_4274 = relay.TupleGetItem(func_2409_call(), 0)
output = call_4273
output2 = call_4274
func_4284 = relay.Function([], output)
mod['func_4284'] = func_4284
mod = relay.transform.InferType()(mod)
output = func_4284()
func_4285 = relay.Function([], output)
mutated_mod['func_4285'] = func_4285
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1873_call = mod.get_global_var('func_1873')
func_1875_call = mutated_mod.get_global_var('func_1875')
call_4347 = relay.TupleGetItem(func_1873_call(), 0)
call_4348 = relay.TupleGetItem(func_1875_call(), 0)
output = relay.Tuple([call_4347,])
output2 = relay.Tuple([call_4348,])
func_4355 = relay.Function([], output)
mod['func_4355'] = func_4355
mod = relay.transform.InferType()(mod)
mutated_mod['func_4355'] = func_4355
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4355_call = mutated_mod.get_global_var('func_4355')
call_4356 = func_4355_call()
output = call_4356
func_4357 = relay.Function([], output)
mutated_mod['func_4357'] = func_4357
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2679_call = mod.get_global_var('func_2679')
func_2681_call = mutated_mod.get_global_var('func_2681')
call_4382 = relay.TupleGetItem(func_2679_call(), 0)
call_4383 = relay.TupleGetItem(func_2681_call(), 0)
output = relay.Tuple([call_4382,])
output2 = relay.Tuple([call_4383,])
func_4384 = relay.Function([], output)
mod['func_4384'] = func_4384
mod = relay.transform.InferType()(mod)
output = func_4384()
func_4385 = relay.Function([], output)
mutated_mod['func_4385'] = func_4385
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4386 = relay.var("var_4386", dtype = "int16", shape = (13, 3, 10))#candidate|4386|(13, 3, 10)|var|int16
var_4387 = relay.var("var_4387", dtype = "int16", shape = (13, 3, 10))#candidate|4387|(13, 3, 10)|var|int16
bop_4388 = relay.not_equal(var_4386.astype('bool'), relay.reshape(var_4387.astype('bool'), relay.shape_of(var_4386))) # shape=(13, 3, 10)
var_4391 = relay.var("var_4391", dtype = "int16", shape = (13, 3, 10))#candidate|4391|(13, 3, 10)|var|int16
bop_4392 = relay.bitwise_and(var_4386.astype('uint32'), relay.reshape(var_4391.astype('uint32'), relay.shape_of(var_4386))) # shape=(13, 3, 10)
output = relay.Tuple([bop_4388,bop_4392,])
output2 = relay.Tuple([bop_4388,bop_4392,])
func_4399 = relay.Function([var_4386,var_4387,var_4391,], output)
mod['func_4399'] = func_4399
mod = relay.transform.InferType()(mod)
var_4400 = relay.var("var_4400", dtype = "int16", shape = (13, 3, 10))#candidate|4400|(13, 3, 10)|var|int16
var_4401 = relay.var("var_4401", dtype = "int16", shape = (13, 3, 10))#candidate|4401|(13, 3, 10)|var|int16
var_4402 = relay.var("var_4402", dtype = "int16", shape = (13, 3, 10))#candidate|4402|(13, 3, 10)|var|int16
output = func_4399(var_4400,var_4401,var_4402,)
func_4403 = relay.Function([var_4400,var_4401,var_4402,], output)
mutated_mod['func_4403'] = func_4403
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4355_call = mod.get_global_var('func_4355')
func_4357_call = mutated_mod.get_global_var('func_4357')
call_4443 = relay.TupleGetItem(func_4355_call(), 0)
call_4444 = relay.TupleGetItem(func_4357_call(), 0)
func_3723_call = mod.get_global_var('func_3723')
func_3725_call = mutated_mod.get_global_var('func_3725')
call_4486 = func_3723_call()
call_4487 = func_3723_call()
output = relay.Tuple([call_4443,call_4486,])
output2 = relay.Tuple([call_4444,call_4487,])
func_4496 = relay.Function([], output)
mod['func_4496'] = func_4496
mod = relay.transform.InferType()(mod)
output = func_4496()
func_4497 = relay.Function([], output)
mutated_mod['func_4497'] = func_4497
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3183_call = mod.get_global_var('func_3183')
func_3185_call = mutated_mod.get_global_var('func_3185')
call_4514 = func_3183_call()
call_4515 = func_3183_call()
uop_4537 = relay.erf(call_4514.astype('float32')) # shape=(10, 14, 13)
uop_4539 = relay.erf(call_4515.astype('float32')) # shape=(10, 14, 13)
func_2313_call = mod.get_global_var('func_2313')
func_2316_call = mutated_mod.get_global_var('func_2316')
call_4545 = relay.TupleGetItem(func_2313_call(relay.reshape(call_4514.astype('float32'), [10, 14, 13])), 1)
call_4546 = relay.TupleGetItem(func_2316_call(relay.reshape(call_4514.astype('float32'), [10, 14, 13])), 1)
func_2324_call = mod.get_global_var('func_2324')
func_2326_call = mutated_mod.get_global_var('func_2326')
call_4571 = relay.TupleGetItem(func_2324_call(), 0)
call_4572 = relay.TupleGetItem(func_2326_call(), 0)
output = relay.Tuple([uop_4537,call_4545,call_4571,])
output2 = relay.Tuple([uop_4539,call_4546,call_4572,])
func_4582 = relay.Function([], output)
mod['func_4582'] = func_4582
mod = relay.transform.InferType()(mod)
output = func_4582()
func_4583 = relay.Function([], output)
mutated_mod['func_4583'] = func_4583
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3808_call = mod.get_global_var('func_3808')
func_3809_call = mutated_mod.get_global_var('func_3809')
call_4651 = relay.TupleGetItem(func_3808_call(), 2)
call_4652 = relay.TupleGetItem(func_3809_call(), 2)
uop_4659 = relay.atanh(call_4651.astype('float32')) # shape=(10, 14, 13)
uop_4661 = relay.atanh(call_4652.astype('float32')) # shape=(10, 14, 13)
output = uop_4659
output2 = uop_4661
func_4683 = relay.Function([], output)
mod['func_4683'] = func_4683
mod = relay.transform.InferType()(mod)
output = func_4683()
func_4684 = relay.Function([], output)
mutated_mod['func_4684'] = func_4684
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4690 = relay.var("var_4690", dtype = "float64", shape = (14, 6, 9))#candidate|4690|(14, 6, 9)|var|float64
var_4691 = relay.var("var_4691", dtype = "float64", shape = (14, 6, 9))#candidate|4691|(14, 6, 9)|var|float64
bop_4692 = relay.power(var_4690.astype('float64'), relay.reshape(var_4691.astype('float64'), relay.shape_of(var_4690))) # shape=(14, 6, 9)
output = bop_4692
output2 = bop_4692
func_4702 = relay.Function([var_4690,var_4691,], output)
mod['func_4702'] = func_4702
mod = relay.transform.InferType()(mod)
mutated_mod['func_4702'] = func_4702
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4702_call = mutated_mod.get_global_var('func_4702')
var_4704 = relay.var("var_4704", dtype = "float64", shape = (14, 6, 9))#candidate|4704|(14, 6, 9)|var|float64
var_4705 = relay.var("var_4705", dtype = "float64", shape = (14, 6, 9))#candidate|4705|(14, 6, 9)|var|float64
call_4703 = func_4702_call(var_4704,var_4705,)
output = call_4703
func_4706 = relay.Function([var_4704,var_4705,], output)
mutated_mod['func_4706'] = func_4706
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4794 = relay.var("var_4794", dtype = "float32", shape = (8, 6, 5))#candidate|4794|(8, 6, 5)|var|float32
uop_4795 = relay.atanh(var_4794.astype('float32')) # shape=(8, 6, 5)
var_4804 = relay.var("var_4804", dtype = "float32", shape = (8, 6, 5))#candidate|4804|(8, 6, 5)|var|float32
bop_4805 = relay.not_equal(uop_4795.astype('bool'), relay.reshape(var_4804.astype('bool'), relay.shape_of(uop_4795))) # shape=(8, 6, 5)
bop_4811 = relay.bitwise_or(var_4794.astype('int16'), relay.reshape(uop_4795.astype('int16'), relay.shape_of(var_4794))) # shape=(8, 6, 5)
var_4816 = relay.var("var_4816", dtype = "bool", shape = (8, 6, 5))#candidate|4816|(8, 6, 5)|var|bool
bop_4817 = relay.less(bop_4805.astype('bool'), relay.reshape(var_4816.astype('bool'), relay.shape_of(bop_4805))) # shape=(8, 6, 5)
output = relay.Tuple([bop_4811,bop_4817,])
output2 = relay.Tuple([bop_4811,bop_4817,])
func_4820 = relay.Function([var_4794,var_4804,var_4816,], output)
mod['func_4820'] = func_4820
mod = relay.transform.InferType()(mod)
var_4821 = relay.var("var_4821", dtype = "float32", shape = (8, 6, 5))#candidate|4821|(8, 6, 5)|var|float32
var_4822 = relay.var("var_4822", dtype = "float32", shape = (8, 6, 5))#candidate|4822|(8, 6, 5)|var|float32
var_4823 = relay.var("var_4823", dtype = "bool", shape = (8, 6, 5))#candidate|4823|(8, 6, 5)|var|bool
output = func_4820(var_4821,var_4822,var_4823,)
func_4824 = relay.Function([var_4821,var_4822,var_4823,], output)
mutated_mod['func_4824'] = func_4824
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3538_call = mod.get_global_var('func_3538')
func_3539_call = mutated_mod.get_global_var('func_3539')
call_4868 = func_3538_call()
call_4869 = func_3538_call()
func_3214_call = mod.get_global_var('func_3214')
func_3215_call = mutated_mod.get_global_var('func_3215')
call_4870 = func_3214_call()
call_4871 = func_3214_call()
output = relay.Tuple([call_4868,call_4870,])
output2 = relay.Tuple([call_4869,call_4871,])
func_4881 = relay.Function([], output)
mod['func_4881'] = func_4881
mod = relay.transform.InferType()(mod)
mutated_mod['func_4881'] = func_4881
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4881_call = mutated_mod.get_global_var('func_4881')
call_4882 = func_4881_call()
output = call_4882
func_4883 = relay.Function([], output)
mutated_mod['func_4883'] = func_4883
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4384_call = mod.get_global_var('func_4384')
func_4385_call = mutated_mod.get_global_var('func_4385')
call_4902 = relay.TupleGetItem(func_4384_call(), 0)
call_4903 = relay.TupleGetItem(func_4385_call(), 0)
output = relay.Tuple([call_4902,])
output2 = relay.Tuple([call_4903,])
func_4904 = relay.Function([], output)
mod['func_4904'] = func_4904
mod = relay.transform.InferType()(mod)
mutated_mod['func_4904'] = func_4904
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4904_call = mutated_mod.get_global_var('func_4904')
call_4905 = func_4904_call()
output = call_4905
func_4906 = relay.Function([], output)
mutated_mod['func_4906'] = func_4906
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3183_call = mod.get_global_var('func_3183')
func_3185_call = mutated_mod.get_global_var('func_3185')
call_4945 = func_3183_call()
call_4946 = func_3183_call()
func_4702_call = mod.get_global_var('func_4702')
func_4706_call = mutated_mod.get_global_var('func_4706')
const_4957 = relay.const([4.449891,2.656413,6.352588,-5.733773,7.754374,7.415802,4.271797,-2.433514,3.410840,-5.151164,-1.861938,-0.127990,-1.259742,-3.479577,1.329946,8.505447,-9.562975,-5.808026,-0.046837,-9.395851,1.871234,1.341041,-4.993625,-2.757066,6.910426,-3.971804,9.080602,-1.773422,7.202032,2.313020,5.595824,-9.720424,-0.825745,-3.252195,9.855933,-7.020967,-9.610522,-4.934443,4.273014,-5.454802,9.336212,-8.119875,-3.602161,5.982725,6.170500,-6.564682,3.640706,9.300059,-4.374695,-4.644100,-9.633697,-7.527880,-6.343098,4.158686,2.456402,9.863284,1.604050,6.769780,-1.511337,0.380613,-5.708475,4.293770,-7.896186,4.503746,-7.787982,9.422481,-4.609305,3.953259,-3.896889,-7.515972,3.450807,-1.550221,-0.977127,-5.344520,-6.279821,-4.938893,7.621396,-8.036276,-1.348166,-9.358852,-2.356997,1.757536,-6.009993,8.093428,-6.446729,-3.457747,4.253429,-1.253425,9.962586,2.265398,-3.643949,-7.918203,8.711831,-7.438548,-0.557959,-7.280012,-0.430759,6.413341,-5.418336,8.018643,-5.100847,-2.574516,-6.022374,4.777733,2.698618,-1.664220,0.487747,-1.625363,0.961138,-5.281083,3.105149,-6.650965,8.747765,-0.268743,9.521102,-5.445511,-5.548946,8.462243,1.154549,-1.477030,8.430606,-1.014911,1.696034,7.247787,8.979584,-9.668841,-8.068195,-1.794775,-5.124315,-7.432601,-7.830940,1.027536,2.464524,-4.420346,-4.384203,-4.550565,3.795170,-4.817158,2.397515,0.172223,8.683725,3.179567,9.407931,2.559541,7.691113,1.814826,-7.628287,-6.137033,0.919416,-6.527976,3.249259,-6.495487,-1.068721,2.277622,-0.599489,-4.967353,-9.285706,-0.554861,-4.831686,8.356945,7.725704,9.450704,0.907412,8.530735,-2.697505,-3.192895,-3.598607,-7.968087,9.025912,-9.213737,8.299580,-1.332892,2.973067,1.502987,-6.784563,4.908915,5.073149,-3.610936,-8.068451,6.162404,5.285978,-2.616410,-8.624026,-9.739574,-3.234382,-1.211625,-5.841516,2.844632,6.153142,9.702017,2.315719,7.695269,7.106024,9.227827,9.925254,8.589303,3.681167,8.725856,-1.161922,4.839149,-3.468206,-5.343267,-1.089228,-4.712022,-5.334405,-6.064861,-1.031735,-1.652839,1.547675,2.964371,8.102759,3.351000,-6.153986,-5.138769,7.169411,7.476693,1.514365,-8.392683,5.364732,8.670281,-7.018110,0.910016,9.207984,-4.182408,-6.402125,-8.434383,-1.015642,-6.817610,-4.932506,-0.377219,-6.493829,4.811675,3.590741,-1.461184,6.421510,0.010931,9.361740,-1.224665,-2.331675,1.671202,9.762478,-4.346943,4.699894,-3.577770,-8.783675,8.022468,6.321243,-5.035898,-0.933262,4.766888,6.734788,0.507861,-5.134142,0.182057,4.048260,5.128703,-5.183855,-2.378530,-0.604005,3.807368,7.517640,1.817688,-8.756317,-4.270140,-7.753049,-3.657635,-2.449563,-8.340869,7.894883,0.456611,-2.765406,6.982143,4.865631,3.986842,8.653827,-3.502982,9.881494,2.322680,8.233353,6.079027,3.583658,6.695237,2.344423,-3.692078,-7.744874,7.609536,-6.183406,9.137004,3.698278,3.824753,-5.943411,5.951853,-1.760666,6.141817,-3.284137,1.842967,-9.340970,3.825114,4.293829,-4.962261,-6.482043,-3.600295,7.252161,-1.506284,-7.713446,0.587810,7.961233,5.752797,8.446879,5.534859,4.019357,2.741033,-8.829308,0.114416,2.832600,2.548549,-6.113678,-0.792021,3.417591,-3.550159,9.384917,-1.816963,-2.028776,-6.845128,-5.993192,-5.275395,-0.732977,8.442173,-1.657854,-3.880369,1.453903,8.597645,-4.504360,7.701434,-4.714559,4.089851,2.870711,-7.670161,2.108071,9.509628,5.674263,0.073839,2.596249,-9.729221,-8.981383,3.082455,-9.261329,9.138141,5.028762,-3.637141,-0.897346,2.393873,-7.164106,2.691310,-8.386849,0.768606,-6.929079,7.049743,-5.406609,-4.154383,9.018654,-8.204386,-9.232526,-6.776034,-9.914808,-6.701286,-7.551192,-9.968843,8.844997,7.863980,-4.770000,4.932351,1.838258,-5.293459,-3.946844,-6.045116,1.155238,0.599900,-5.700708,4.162594,2.872916,0.061470,5.509411,-3.707518,-2.976258,-6.325357,-0.445620,4.193087,-9.595532,9.670547,-6.107230,-1.618199,-1.456607,-0.364821,5.064473,6.109258,1.230184,0.037525,-0.272318,9.342917,6.501971,2.239906,-8.848222,7.400174,9.127416,3.110877,7.616765,8.718681,-4.670891,-5.634412,6.583590,-5.003076,0.194827,3.338206,2.331568,-0.024394,-5.485327,-5.942382,-6.221123,3.268423,9.481294,-3.624774,0.651113,-3.224419,0.819284,8.667132,2.006411,5.326048,1.964350,-8.766339,9.679249,6.550895,6.558333,-6.550195,-8.719607,5.167410,5.313727,-4.060918,1.907702,-3.581531,2.325479,7.887237,1.458138,5.284568,2.616400,8.917459,-6.916625,-0.732324,-1.250645,-2.608013,-5.133345,-5.417459,1.930949,-3.056648,-1.252081,5.359294,5.807840,-3.698904,5.762001,0.963816,1.743346,3.439390,-2.129637,2.871916,4.140105,1.088405,2.683795,6.327515,-7.370300,2.322903,-8.807738,-9.133626,2.746096,-0.997421,3.941668,7.774486,-2.448491,-2.149795,-0.317619,9.001523,1.949044,-1.392541,9.648161,6.250930,0.439465,-1.399557,3.885569,7.234554,2.441658,1.577610,-0.248464,1.684908,-9.341104,7.185641,-8.531086,-4.550331,8.725821,-0.494450,-3.435044,-4.784756,7.533491,3.817792,6.532503,1.679092,-9.831953,9.880767,-5.352449,9.536477,9.698094,7.491942,7.507138,6.700348,-1.143454,4.373973,-5.982354,7.399392,-6.192133,-8.795469,9.556981,-4.562424,6.106812,-3.566635,9.094835,-5.032703,-5.122007,-3.096041,7.031251,-0.167632,2.988822,-3.562184,3.129561,5.315611,-0.428890,-4.453489,-4.292331,8.856048,-8.708359,5.418075,7.054796,-0.461642,0.150986,2.228422,1.152239,5.611783,-6.638943,-4.698742,9.956835,7.541084,3.812761,7.882102,8.129812,0.830736,4.206739,4.115513,-4.099688,-1.262243,-1.905337,-9.718183,-1.707062,-1.773740,4.398992,-0.559775,6.195916,-9.492578,4.968605,-9.640172,-0.399547,5.371606,-4.041057,-2.863054,-0.326834,-1.575699,7.162720,-3.515836,-0.464396,-7.534923,9.760988,-3.499186,-4.907384,-1.061286,9.802046,-2.153275,-8.316419,9.971294,-6.148364,-5.229951,-7.298194,8.138814,1.368482,3.566681,4.824894,-8.165492,8.511814,0.177616,5.110124,1.230654,-8.778924,7.477346,6.631373,3.229221,-7.918672,0.388346,-9.594151,-2.777301,-6.030836,-5.043422,5.322403,1.190594,2.113172,4.500601,-4.925040,3.700252,-5.122632,0.928095,2.664514,-8.449747,-5.728272,2.863807,-5.366260,1.846992,0.216642,-4.632120,-5.217850,6.325138,-2.024642,-4.519783,-1.084400,4.508164,-5.797077,-7.718382,2.801402,-1.735098,-2.913162,3.337498,3.376689,-8.586803,-7.941372,-9.711577,-4.428473,-3.479707,-1.031611,8.616632,4.377770,4.992389,0.561011,7.702397,-1.857247,0.214757,4.067098,-9.687628,3.937594,-3.728587,3.018524,-6.251593,-9.367182,0.318678,6.611565,6.247372,8.721685,3.581212,2.364650,-9.085167,-1.407353,-1.252939,-2.397882,-6.327988,7.716838,8.421919,3.039629,-1.622752,-5.006129,-8.151550,-0.808074,-0.840514,6.177538,3.075196,3.171054,-5.978329,6.246733,2.638051,2.187827,0.608154,-4.687302,-1.236468,-1.439350,-8.205368,-3.268279,-4.355700,-5.083303,-5.901217,-4.005361,-8.384482,8.242421,6.787948,-8.332532,-9.471745,3.114899,-7.892984,-3.080398,2.412260,-6.683300,-6.111198,7.606303,8.770312,8.946553,0.317607,7.817626,8.490504,-3.471080,4.335486,-7.329663,1.445793,1.147661,5.749634,-2.089451,-8.372516,-1.865745,5.317412,-5.950864,-5.638556,-0.338013,4.076656,9.869193,7.722611,-8.462890,-8.313225,-8.189291,-1.878577,-6.144705,-8.558018,-0.222205,7.624011,9.037337,-6.490671,7.688430,8.476763,-4.755456,-1.891629,-8.988731,-3.243570,-4.618384,5.823845,-0.615338,7.010510,6.204751,9.615553,-7.747846,6.296793,5.134059,3.884166,-8.292678,-5.473108,-9.043107,-0.908931,-4.798704,6.582812], dtype = "float64")#candidate|4957|(756,)|const|float64
call_4956 = func_4702_call(relay.reshape(const_4957.astype('float64'), [14, 6, 9]), relay.reshape(const_4957.astype('float64'), [14, 6, 9]), )
call_4958 = func_4702_call(relay.reshape(const_4957.astype('float64'), [14, 6, 9]), relay.reshape(const_4957.astype('float64'), [14, 6, 9]), )
output = relay.Tuple([call_4945,call_4956,const_4957,])
output2 = relay.Tuple([call_4946,call_4958,const_4957,])
func_4961 = relay.Function([], output)
mod['func_4961'] = func_4961
mod = relay.transform.InferType()(mod)
mutated_mod['func_4961'] = func_4961
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4961_call = mutated_mod.get_global_var('func_4961')
call_4962 = func_4961_call()
output = call_4962
func_4963 = relay.Function([], output)
mutated_mod['func_4963'] = func_4963
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4961_call = mod.get_global_var('func_4961')
func_4963_call = mutated_mod.get_global_var('func_4963')
call_5007 = relay.TupleGetItem(func_4961_call(), 2)
call_5008 = relay.TupleGetItem(func_4963_call(), 2)
output = call_5007
output2 = call_5008
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
func_2359_call = mod.get_global_var('func_2359')
func_2360_call = mutated_mod.get_global_var('func_2360')
call_5031 = func_2359_call()
call_5032 = func_2359_call()
func_1686_call = mod.get_global_var('func_1686')
func_1688_call = mutated_mod.get_global_var('func_1688')
call_5069 = func_1686_call()
call_5070 = func_1686_call()
output = relay.Tuple([call_5031,call_5069,])
output2 = relay.Tuple([call_5032,call_5070,])
func_5072 = relay.Function([], output)
mod['func_5072'] = func_5072
mod = relay.transform.InferType()(mod)
output = func_5072()
func_5073 = relay.Function([], output)
mutated_mod['func_5073'] = func_5073
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2359_call = mod.get_global_var('func_2359')
func_2360_call = mutated_mod.get_global_var('func_2360')
call_5089 = func_2359_call()
call_5090 = func_2359_call()
func_3222_call = mod.get_global_var('func_3222')
func_3223_call = mutated_mod.get_global_var('func_3223')
call_5093 = func_3222_call()
call_5094 = func_3222_call()
output = relay.Tuple([call_5089,call_5093,])
output2 = relay.Tuple([call_5090,call_5094,])
func_5095 = relay.Function([], output)
mod['func_5095'] = func_5095
mod = relay.transform.InferType()(mod)
output = func_5095()
func_5096 = relay.Function([], output)
mutated_mod['func_5096'] = func_5096
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3808_call = mod.get_global_var('func_3808')
func_3809_call = mutated_mod.get_global_var('func_3809')
call_5160 = relay.TupleGetItem(func_3808_call(), 0)
call_5161 = relay.TupleGetItem(func_3809_call(), 0)
func_3538_call = mod.get_global_var('func_3538')
func_3539_call = mutated_mod.get_global_var('func_3539')
call_5165 = func_3538_call()
call_5166 = func_3538_call()
func_4193_call = mod.get_global_var('func_4193')
func_4196_call = mutated_mod.get_global_var('func_4196')
const_5171 = relay.const(True, dtype = "bool")#candidate|5171|()|const|bool
var_5172 = relay.var("var_5172", dtype = "bool", shape = (80,))#candidate|5172|(80,)|var|bool
call_5170 = relay.TupleGetItem(func_4193_call(relay.reshape(const_5171.astype('bool'), []), relay.reshape(var_5172.astype('bool'), [80,]), ), 1)
call_5173 = relay.TupleGetItem(func_4196_call(relay.reshape(const_5171.astype('bool'), []), relay.reshape(var_5172.astype('bool'), [80,]), ), 1)
output = relay.Tuple([call_5160,call_5165,call_5170,const_5171,var_5172,])
output2 = relay.Tuple([call_5161,call_5166,call_5173,const_5171,var_5172,])
func_5175 = relay.Function([var_5172,], output)
mod['func_5175'] = func_5175
mod = relay.transform.InferType()(mod)
mutated_mod['func_5175'] = func_5175
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5176 = relay.var("var_5176", dtype = "bool", shape = (80,))#candidate|5176|(80,)|var|bool
func_5175_call = mutated_mod.get_global_var('func_5175')
call_5177 = func_5175_call(var_5176)
output = call_5177
func_5178 = relay.Function([var_5176], output)
mutated_mod['func_5178'] = func_5178
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4496_call = mod.get_global_var('func_4496')
func_4497_call = mutated_mod.get_global_var('func_4497')
call_5221 = relay.TupleGetItem(func_4496_call(), 0)
call_5222 = relay.TupleGetItem(func_4497_call(), 0)
func_3491_call = mod.get_global_var('func_3491')
func_3495_call = mutated_mod.get_global_var('func_3495')
var_5227 = relay.var("var_5227", dtype = "bool", shape = ())#candidate|5227|()|var|bool
const_5228 = relay.const([[False,True],[True,False],[False,False],[True,False],[True,True],[False,True],[True,True],[False,False],[True,True],[True,False],[False,False],[False,True],[True,True],[False,False],[False,True],[False,False],[True,True],[False,True],[True,True],[False,False],[False,False],[False,False],[True,False],[False,False],[False,True],[False,False],[True,True],[True,False],[False,True],[False,False],[True,False],[True,False],[False,True],[True,True],[True,True],[False,True],[True,False],[True,False],[False,True],[False,False]], dtype = "bool")#candidate|5228|(40, 2)|const|bool
call_5226 = func_3491_call(relay.reshape(var_5227.astype('bool'), []), relay.reshape(const_5228.astype('bool'), [1, 5, 16]), )
call_5229 = func_3491_call(relay.reshape(var_5227.astype('bool'), []), relay.reshape(const_5228.astype('bool'), [1, 5, 16]), )
uop_5234 = relay.rsqrt(const_5228.astype('float64')) # shape=(40, 2)
output = relay.Tuple([call_5221,call_5226,var_5227,uop_5234,])
output2 = relay.Tuple([call_5222,call_5229,var_5227,uop_5234,])
func_5237 = relay.Function([var_5227,], output)
mod['func_5237'] = func_5237
mod = relay.transform.InferType()(mod)
mutated_mod['func_5237'] = func_5237
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5238 = relay.var("var_5238", dtype = "bool", shape = ())#candidate|5238|()|var|bool
func_5237_call = mutated_mod.get_global_var('func_5237')
call_5239 = func_5237_call(var_5238)
output = call_5239
func_5240 = relay.Function([var_5238], output)
mutated_mod['func_5240'] = func_5240
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3808_call = mod.get_global_var('func_3808')
func_3809_call = mutated_mod.get_global_var('func_3809')
call_5307 = relay.TupleGetItem(func_3808_call(), 2)
call_5308 = relay.TupleGetItem(func_3809_call(), 2)
func_3723_call = mod.get_global_var('func_3723')
func_3725_call = mutated_mod.get_global_var('func_3725')
call_5324 = func_3723_call()
call_5325 = func_3723_call()
func_2324_call = mod.get_global_var('func_2324')
func_2326_call = mutated_mod.get_global_var('func_2326')
call_5330 = relay.TupleGetItem(func_2324_call(), 0)
call_5331 = relay.TupleGetItem(func_2326_call(), 0)
output = relay.Tuple([call_5307,call_5324,call_5330,])
output2 = relay.Tuple([call_5308,call_5325,call_5331,])
func_5339 = relay.Function([], output)
mod['func_5339'] = func_5339
mod = relay.transform.InferType()(mod)
mutated_mod['func_5339'] = func_5339
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5339_call = mutated_mod.get_global_var('func_5339')
call_5340 = func_5339_call()
output = call_5340
func_5341 = relay.Function([], output)
mutated_mod['func_5341'] = func_5341
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4881_call = mod.get_global_var('func_4881')
func_4883_call = mutated_mod.get_global_var('func_4883')
call_5396 = relay.TupleGetItem(func_4881_call(), 1)
call_5397 = relay.TupleGetItem(func_4883_call(), 1)
output = call_5396
output2 = call_5397
func_5404 = relay.Function([], output)
mod['func_5404'] = func_5404
mod = relay.transform.InferType()(mod)
output = func_5404()
func_5405 = relay.Function([], output)
mutated_mod['func_5405'] = func_5405
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4384_call = mod.get_global_var('func_4384')
func_4385_call = mutated_mod.get_global_var('func_4385')
call_5412 = relay.TupleGetItem(func_4384_call(), 0)
call_5413 = relay.TupleGetItem(func_4385_call(), 0)
var_5414 = relay.var("var_5414", dtype = "float32", shape = (15, 11, 6))#candidate|5414|(15, 11, 6)|var|float32
bop_5415 = relay.logical_xor(call_5412.astype('uint8'), relay.reshape(var_5414.astype('uint8'), relay.shape_of(call_5412))) # shape=(15, 11, 6)
bop_5418 = relay.logical_xor(call_5413.astype('uint8'), relay.reshape(var_5414.astype('uint8'), relay.shape_of(call_5413))) # shape=(15, 11, 6)
bop_5424 = relay.right_shift(bop_5415.astype('int32'), relay.reshape(var_5414.astype('int32'), relay.shape_of(bop_5415))) # shape=(15, 11, 6)
bop_5427 = relay.right_shift(bop_5418.astype('int32'), relay.reshape(var_5414.astype('int32'), relay.shape_of(bop_5418))) # shape=(15, 11, 6)
func_3183_call = mod.get_global_var('func_3183')
func_3185_call = mutated_mod.get_global_var('func_3185')
call_5436 = func_3183_call()
call_5437 = func_3183_call()
func_2407_call = mod.get_global_var('func_2407')
func_2409_call = mutated_mod.get_global_var('func_2409')
call_5441 = relay.TupleGetItem(func_2407_call(), 0)
call_5442 = relay.TupleGetItem(func_2409_call(), 0)
var_5462 = relay.var("var_5462", dtype = "uint8", shape = (15, 11, 6))#candidate|5462|(15, 11, 6)|var|uint8
bop_5463 = relay.equal(bop_5415.astype('bool'), relay.reshape(var_5462.astype('bool'), relay.shape_of(bop_5415))) # shape=(15, 11, 6)
bop_5466 = relay.equal(bop_5418.astype('bool'), relay.reshape(var_5462.astype('bool'), relay.shape_of(bop_5418))) # shape=(15, 11, 6)
output = relay.Tuple([bop_5424,call_5436,call_5441,bop_5463,])
output2 = relay.Tuple([bop_5427,call_5437,call_5442,bop_5466,])
func_5474 = relay.Function([var_5414,var_5462,], output)
mod['func_5474'] = func_5474
mod = relay.transform.InferType()(mod)
var_5475 = relay.var("var_5475", dtype = "float32", shape = (15, 11, 6))#candidate|5475|(15, 11, 6)|var|float32
var_5476 = relay.var("var_5476", dtype = "uint8", shape = (15, 11, 6))#candidate|5476|(15, 11, 6)|var|uint8
output = func_5474(var_5475,var_5476,)
func_5477 = relay.Function([var_5475,var_5476,], output)
mutated_mod['func_5477'] = func_5477
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3808_call = mod.get_global_var('func_3808')
func_3809_call = mutated_mod.get_global_var('func_3809')
call_5532 = relay.TupleGetItem(func_3808_call(), 2)
call_5533 = relay.TupleGetItem(func_3809_call(), 2)
output = call_5532
output2 = call_5533
func_5543 = relay.Function([], output)
mod['func_5543'] = func_5543
mod = relay.transform.InferType()(mod)
output = func_5543()
func_5544 = relay.Function([], output)
mutated_mod['func_5544'] = func_5544
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5553 = relay.var("var_5553", dtype = "float32", shape = (8, 8, 10))#candidate|5553|(8, 8, 10)|var|float32
uop_5554 = relay.tan(var_5553.astype('float32')) # shape=(8, 8, 10)
bop_5556 = relay.bitwise_and(var_5553.astype('uint16'), relay.reshape(uop_5554.astype('uint16'), relay.shape_of(var_5553))) # shape=(8, 8, 10)
var_5568 = relay.var("var_5568", dtype = "uint16", shape = (8, 8, 10))#candidate|5568|(8, 8, 10)|var|uint16
bop_5569 = relay.minimum(bop_5556.astype('uint64'), relay.reshape(var_5568.astype('uint64'), relay.shape_of(bop_5556))) # shape=(8, 8, 10)
output = relay.Tuple([bop_5569,])
output2 = relay.Tuple([bop_5569,])
func_5585 = relay.Function([var_5553,var_5568,], output)
mod['func_5585'] = func_5585
mod = relay.transform.InferType()(mod)
mutated_mod['func_5585'] = func_5585
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5585_call = mutated_mod.get_global_var('func_5585')
var_5587 = relay.var("var_5587", dtype = "float32", shape = (8, 8, 10))#candidate|5587|(8, 8, 10)|var|float32
var_5588 = relay.var("var_5588", dtype = "uint16", shape = (8, 8, 10))#candidate|5588|(8, 8, 10)|var|uint16
call_5586 = func_5585_call(var_5587,var_5588,)
output = call_5586
func_5589 = relay.Function([var_5587,var_5588,], output)
mutated_mod['func_5589'] = func_5589
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5404_call = mod.get_global_var('func_5404')
func_5405_call = mutated_mod.get_global_var('func_5405')
call_5602 = func_5404_call()
call_5603 = func_5404_call()
output = relay.Tuple([call_5602,])
output2 = relay.Tuple([call_5603,])
func_5608 = relay.Function([], output)
mod['func_5608'] = func_5608
mod = relay.transform.InferType()(mod)
mutated_mod['func_5608'] = func_5608
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5608_call = mutated_mod.get_global_var('func_5608')
call_5609 = func_5608_call()
output = call_5609
func_5610 = relay.Function([], output)
mutated_mod['func_5610'] = func_5610
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2866_call = mod.get_global_var('func_2866')
func_2867_call = mutated_mod.get_global_var('func_2867')
call_5713 = func_2866_call()
call_5714 = func_2866_call()
const_5718 = relay.const([[[4.504600,2.894979,9.476886,9.606523,4.341465,3.872617,-5.804038,-8.211997,-5.588870,-4.066210,8.838279,-0.158217,6.484454],[-6.662850,0.235598,-5.496407,-6.780523,8.804547,6.592514,-0.740725,-7.647148,-2.827251,-4.516864,9.902023,4.003271,-9.428471],[0.895667,3.640408,-0.002168,9.078602,-3.683749,-7.581902,7.427709,-8.929271,-0.822035,-2.995202,-7.521880,-8.449641,4.642063],[4.493573,8.093108,4.546112,-9.557724,2.796986,-7.828677,6.646010,-6.626402,6.707255,9.168107,-2.623050,-2.738112,-8.892671],[-1.819825,1.124942,-5.149836,-7.095395,-7.109196,9.106151,-3.036320,3.364855,9.353159,9.608370,4.343723,4.932305,-6.515953],[-3.125079,-1.656826,-7.365975,8.368767,2.870701,-7.468295,7.312754,1.104339,-3.102705,0.674399,4.756552,-9.834131,-0.490243],[2.496431,-6.823842,-0.404580,0.188087,9.482882,7.738899,6.279245,-7.111819,-6.367860,8.811709,-4.627952,0.883944,3.523999],[-5.641870,-0.521083,9.095547,6.170240,7.388743,4.210037,-6.427449,-2.736478,1.268496,-3.371207,-8.904217,-0.508923,8.886694],[0.302323,-4.163634,0.553361,-8.279051,-7.851699,5.393866,6.804434,6.735139,9.645594,5.169435,5.000300,-8.382448,-6.548448],[-9.913059,-9.593938,-7.368661,-1.232410,-2.461176,9.035529,0.274345,3.621974,4.567554,-5.476034,9.380417,3.891836,4.125971],[0.805251,-7.177641,-2.477934,-3.270632,-9.702639,-8.294142,-6.163719,-5.905505,3.570148,4.832197,0.740884,9.146501,3.484243],[0.864306,2.937568,1.030027,-2.518372,7.983579,-4.691383,4.222685,-4.893683,2.983895,1.168116,-9.057309,-6.562262,1.489128],[6.119475,1.476501,3.801087,1.447602,6.604684,5.670174,-8.527148,7.066561,9.443509,-2.575201,-9.373523,-2.185338,4.145938],[0.270546,-7.308647,9.247722,6.020925,-6.232942,-4.106096,-4.944304,-3.410046,6.062412,-8.998377,6.555182,-8.423495,9.629123]],[[5.439543,-5.231728,-5.373359,-0.607726,-0.042879,-7.013013,-2.244239,-9.498112,-3.671158,7.759793,-1.552840,-3.143131,2.059638],[-6.120299,2.365269,-9.429470,1.225244,9.308958,-6.298588,-7.668069,-2.003042,8.646993,3.317229,5.451133,-5.670383,-3.346990],[0.510716,6.749841,-9.875678,-4.186079,0.633666,8.646955,6.825044,-1.237747,-3.692439,-7.442517,-3.265257,-4.124989,8.827921],[9.231362,-1.218097,7.238243,-3.847182,-2.437592,-2.992753,-8.151115,0.383969,7.300038,1.167048,9.819314,-2.174847,-8.940224],[6.161360,6.997370,-4.563707,-3.993877,-4.205204,-2.908277,-2.559754,-7.508991,-9.521608,-5.643821,-8.388612,-7.382675,4.156951],[9.074592,-6.243112,-2.739136,-4.994614,-7.248740,4.666619,8.707526,-5.284688,-5.929093,-2.098505,-1.503119,-6.688880,1.540815],[-5.260870,-7.453774,3.720072,7.515575,6.754084,0.955539,6.751397,-8.430812,-9.317371,1.016137,2.066874,4.327198,-8.618477],[-9.953589,-3.683162,5.426522,-9.919207,-4.485276,4.420974,0.726665,-5.819075,2.017662,-2.293961,-1.779088,3.629230,-0.353779],[4.717187,8.932998,4.334484,-5.915787,3.759282,-4.155217,4.766370,0.059334,-1.780064,9.990436,1.963306,8.336983,-0.578334],[-1.769124,4.161367,9.979926,-1.713495,-3.245061,-1.024322,2.790275,-5.006207,5.386982,-6.763509,-1.342000,8.506332,5.819100],[-5.934190,6.029786,-9.874600,9.712721,-8.230483,2.896745,7.159834,-3.769107,-6.083417,0.838106,5.710107,2.147290,1.852919],[-1.126352,9.200659,1.149259,-7.618193,7.766836,-8.384445,-7.131376,6.924172,7.105920,6.558584,-6.675767,5.189566,-7.513827],[1.456206,-5.797678,-0.373858,8.932237,5.335732,5.058186,9.494266,-9.213855,7.592836,-1.457212,-9.657777,3.472109,7.760227],[-5.114390,2.722859,0.866495,-4.979582,7.582626,5.950240,-1.862736,7.196065,-1.931060,-6.490246,-0.690072,-4.663722,-3.874937]],[[-3.480580,-4.085871,-4.090167,-8.510179,-6.018752,-0.783256,-0.804998,7.939728,-4.456908,-7.637822,4.490634,2.311497,7.383532],[-5.297518,-0.590494,5.952211,-9.694474,7.008413,-9.746935,3.076436,4.328398,6.401551,8.048819,3.781139,-4.536970,-9.524654],[0.882330,-3.047355,8.742501,-0.365981,6.000378,2.952023,7.882920,-5.832882,-0.426473,-0.575554,4.041793,1.073744,-7.705830],[4.147538,-2.423128,9.937928,8.740108,8.609672,-2.874359,-8.744762,4.269572,7.071939,-3.788927,-8.693041,6.127687,6.704450],[-1.568203,-9.902638,1.448930,5.169009,3.806245,1.908831,-0.616290,9.819690,-0.177238,1.958295,3.215883,4.552390,-2.757234],[4.776390,-1.408113,3.327044,9.934755,-2.088616,5.105904,3.223176,-9.943622,5.655987,8.773498,5.039238,-7.349386,4.232696],[6.068883,-6.670128,-3.794995,-5.321084,-1.287223,1.609543,2.562529,-8.081423,1.841224,3.500726,2.997875,7.173466,0.591512],[-3.751706,0.333542,-5.402032,-8.727853,-1.847637,-2.227200,-9.790912,-4.147500,-2.549848,8.134944,-1.792268,-0.646155,-6.018922],[-4.230985,-9.524494,-4.733646,-5.442903,-1.922774,-6.161836,7.243839,6.455499,7.933452,-3.927103,6.584498,8.502012,9.099322],[-7.873602,9.908907,6.592609,-6.662781,-8.291366,1.399991,-5.367070,7.313601,-0.127437,8.281747,-0.204639,3.550406,7.246451],[8.816863,9.071144,-1.936902,4.227880,-1.806279,-6.346584,-3.698023,2.435490,5.818389,-3.752499,2.795782,0.767147,-6.311160],[0.329441,-1.968552,3.658111,-0.898151,-2.668392,-3.791023,-2.467809,9.246021,7.056201,5.987672,1.088122,-8.071391,0.655456],[-5.694305,-8.511092,-2.614457,1.148509,-0.987367,7.125811,6.080431,-6.907464,9.584738,9.099345,9.155233,-7.404210,5.544523],[5.079118,6.186866,9.930866,1.215062,6.039914,-6.498069,-6.941918,8.948461,8.581988,1.313350,-9.221022,-6.980361,3.545195]],[[-4.573127,9.639409,9.509544,4.757893,0.784558,8.651613,-2.430912,9.682752,0.030421,-3.247489,2.849520,3.416630,4.554906],[4.863329,8.136856,1.266827,-2.604810,-8.843479,2.334452,2.567068,-3.676293,9.133261,6.634335,6.830832,-3.000400,3.654829],[9.187862,-2.838394,-6.101795,1.748881,3.965795,6.114324,1.398212,0.995424,9.542722,0.130616,9.399623,-1.559872,6.629122],[2.112659,0.667996,5.858017,-7.757786,6.918570,1.261047,-8.265321,7.256805,4.227686,7.108580,3.798743,7.291377,9.107581],[7.235373,0.067909,7.692313,-1.308995,9.962298,-9.988977,-4.828429,-4.671540,-3.981118,-5.991705,-4.706868,-4.528841,-7.870522],[-8.975956,-5.265656,5.361501,2.925472,3.038808,9.596487,-1.727678,7.001475,-7.099317,-8.783168,-4.134453,-2.465857,0.667156],[-8.543708,-4.767735,3.946685,-3.953389,-5.199598,-7.272453,-0.106784,8.507918,4.860259,-7.683006,-9.891015,-6.630162,3.885328],[6.783262,0.684759,-0.693701,-6.400419,3.992720,8.914755,3.699572,3.162601,1.365031,6.376647,2.213395,-1.639679,-9.007739],[2.887089,-5.604462,3.862325,-0.240337,-3.694445,-7.661632,7.296455,-4.394302,7.927177,2.705065,8.448317,-0.753940,9.867455],[-6.365314,3.118282,-7.925461,0.190516,0.911255,-3.647291,-0.620334,-5.118370,9.674165,-1.577739,-0.458797,8.048664,-6.767972],[-6.654087,-3.257671,-9.332470,-6.807070,2.843781,-4.367422,5.982149,6.714517,1.584261,-2.781351,-6.648130,-9.311932,4.747676],[-8.203525,-7.049377,-4.469355,3.354125,-2.017536,6.179341,0.140632,9.680915,5.849935,0.894285,-2.732816,-2.739791,-8.348906],[-7.161914,1.328385,2.091941,-5.293971,-1.840323,-3.814741,1.837347,-1.838386,8.981874,1.356139,9.979323,1.058945,1.679950],[-8.038162,-2.379713,-2.276361,3.069873,8.103297,8.762720,-4.864044,-3.591417,6.173518,6.531998,-8.708179,1.659837,7.405700]],[[-4.575337,7.436011,-3.969773,-9.695304,-8.577498,2.009336,-0.267056,-4.646490,-0.441936,-8.157672,-7.154115,3.305519,1.870422],[-4.780244,9.097842,5.799769,7.020642,-6.687739,-0.999833,-4.786416,5.094201,-6.208509,-0.019002,-9.072218,2.332858,0.275035],[-6.318786,3.052123,-9.894657,5.279807,6.804383,-6.516097,2.972854,-1.747611,5.025053,8.374117,-3.017910,-4.667699,-3.287559],[-1.766338,1.974572,7.575145,-6.365790,2.453791,0.929906,-8.382746,-3.804646,2.099538,1.452375,5.600794,-1.311032,-6.719724],[1.322043,-9.343963,3.309404,5.390317,-2.817011,-9.021245,-7.293275,-3.741089,-5.681122,-9.625597,3.225715,3.172396,-8.942780],[2.253570,0.432440,6.098315,-5.709647,-8.427751,-1.526299,7.440080,0.422280,5.042295,5.963463,6.034508,9.058672,-1.970054],[6.144979,5.629482,9.802261,-6.687777,-1.671656,7.497165,0.535156,-7.132432,1.366333,3.861512,-4.183297,-2.128184,-5.713995],[9.545890,-4.600396,-9.494054,1.430732,9.663536,-6.999697,1.927331,2.809268,7.614716,8.978573,1.944710,0.468583,9.027041],[2.418729,-0.958926,2.819252,6.678740,8.981764,7.968134,-2.205768,4.503731,-6.130637,5.762151,4.911041,0.160808,3.186234],[-5.189978,1.185247,-7.424965,6.715102,-7.535006,-1.132041,-7.640398,0.966379,1.730947,-2.810690,-9.569052,0.118148,9.547565],[-3.300974,4.388332,3.196434,9.502072,6.527856,8.823327,-0.519153,5.242856,-9.701664,-8.568636,7.607035,0.580624,6.610900],[4.910154,2.245290,0.638496,9.938908,5.456658,-3.295981,2.516575,-2.648666,8.240755,-7.571320,-9.056070,-8.981252,-3.735632],[-4.718612,-0.808269,7.137353,-0.113857,-8.079146,-9.264021,1.597080,-4.043497,-6.096199,8.666256,-7.551229,1.479465,-4.440306],[6.917982,3.407272,-2.936525,0.214544,5.703517,-1.121377,-4.381778,5.448390,-3.587881,-7.133926,3.408136,-7.934316,-4.944595]],[[2.840517,5.054147,3.580703,-6.317346,-5.772719,-0.544051,6.015561,-4.234597,6.671720,-7.049982,-3.539429,0.646926,1.645486],[9.272472,-2.197453,5.024976,-9.619158,5.392173,4.376308,-1.757570,-7.127882,-8.413422,-8.195608,-0.107152,8.136577,-6.341705],[6.187476,-4.809062,-1.534796,6.629273,8.753354,-8.061143,1.722820,7.640155,-4.911566,9.829517,-5.714002,-6.405549,-9.098782],[0.247828,-8.096656,4.601073,5.411893,-4.703515,-5.973868,-6.316759,-8.411763,4.025704,-9.820197,6.351647,-6.461469,-0.218568],[-3.847018,9.210452,4.675904,-3.660800,-9.297359,3.564304,8.622606,-4.822346,3.463848,-7.986438,0.925561,-0.325657,-5.392360],[-1.043181,-4.298200,-7.955015,-3.730743,6.121435,-4.010395,2.207933,-4.984037,-7.320916,-4.484466,2.934796,-7.130188,-3.914199],[7.913108,1.522605,-4.619341,-3.162386,-7.017836,3.670308,-1.789991,-1.131052,-6.546377,8.259655,5.881357,-6.108251,-7.762107],[3.152306,7.590895,4.826018,-4.193979,9.314894,-5.864838,2.465991,-4.913152,0.142697,-6.676598,2.448954,0.834343,0.011071],[-1.106150,9.758415,1.334500,4.493366,-9.382120,5.498840,-0.963551,8.569639,-1.978231,2.344863,8.439468,0.181798,7.077588],[-7.248828,0.003698,1.737654,3.947241,4.782071,1.511202,-6.927904,7.261276,3.053190,-9.041461,-6.237586,4.062001,6.248873],[2.280972,-6.025015,7.262799,1.808930,-0.412912,-4.393300,3.903989,-2.652657,1.695628,-2.584964,-1.893816,-1.086535,-7.621974],[2.915429,-7.998499,-8.259978,1.014053,-4.130761,1.104652,-3.821695,-0.616224,-6.858229,-9.928048,3.190629,5.541394,-7.443149],[4.030021,-5.691216,7.386348,1.138183,-3.121030,5.817401,8.299502,-5.697167,-2.609773,-5.713539,7.478277,-1.724954,-0.714280],[7.127805,-4.798297,0.284407,-9.426019,0.429812,-9.087585,-9.639200,7.131925,-2.471352,9.612561,8.932583,5.149542,0.467517]],[[-6.159760,-6.068853,8.510797,-3.141207,3.718046,2.752664,0.792345,-2.839289,5.364254,-2.476485,-4.066301,1.036122,4.749003],[1.309868,7.180386,-6.513041,1.485306,-7.447917,-2.771373,-4.251737,-0.432991,-7.165612,-8.585200,5.787276,5.069100,-1.124453],[5.195835,6.763969,9.051782,5.965746,8.944887,-7.815495,0.914493,6.293850,-3.518785,0.405259,6.346340,-2.812399,-3.315537],[-3.298899,-5.592567,-6.439344,-4.442348,-7.293904,-8.221887,-5.353271,0.074140,-2.073334,5.236524,0.145582,2.964259,2.319775],[-9.996636,0.699146,5.526116,-5.504795,-3.571622,0.995540,-5.634789,-8.975624,-0.913656,2.165607,-8.597913,-5.713026,8.025597],[8.420037,-3.455318,-3.555611,-9.069149,-2.999003,4.711283,5.984573,8.512005,-1.501303,0.898602,-7.405661,-8.448953,6.884360],[-1.504957,-2.042352,4.698537,-3.019922,-9.624993,-2.869241,-8.136482,0.248072,5.346427,-5.698877,6.785861,2.693272,8.966798],[-8.177838,4.544302,-5.954619,0.833560,0.323296,-0.297183,2.697597,-9.887782,-8.961065,-1.764020,-8.266096,-2.279378,-1.461193],[-4.305606,-2.857284,8.993990,6.175320,5.699221,-8.581358,-3.003734,3.745330,-8.242878,-8.571987,7.875521,4.010766,-7.485470],[6.405873,-6.110079,-3.480339,6.941363,7.027271,-2.504240,2.296172,-4.872113,-3.933369,-9.313899,-9.013504,-2.994870,7.991760],[2.835542,4.263572,3.363663,-5.977949,-0.206722,-3.114530,-2.948517,6.838870,-5.451143,-4.548286,-9.127339,5.340576,-0.010137],[6.084379,-9.184963,-8.672690,-2.911583,5.755389,2.465661,1.200410,9.773900,9.271256,6.179033,-2.268209,-2.351152,4.508295],[5.447732,6.986192,-1.508203,3.681992,1.916788,-5.122024,3.376775,5.138181,0.814876,8.720392,-8.052108,-1.151274,1.561923],[7.177184,8.973177,-1.805435,-4.911853,7.781198,1.935303,5.011118,-4.792581,-8.524065,-2.944173,-1.644163,-2.182660,-6.443384]],[[7.811562,1.280217,2.774808,-1.380484,4.969088,7.990205,-0.501279,-8.261824,9.714974,-3.204575,3.536710,-5.112842,9.147432],[7.541209,-4.809908,-8.466940,0.812345,-0.980548,7.591844,3.725444,6.716323,-6.199089,5.672717,7.561395,-1.362357,8.410564],[-9.523128,6.323733,-7.765182,-9.847101,-7.067765,-8.809552,-2.290445,-5.998223,5.799046,-8.115458,9.679978,-6.965419,4.876980],[3.156414,-1.578776,3.675217,-8.965203,-4.622996,2.686602,0.490564,3.879328,9.902052,-8.465734,6.782178,-0.216081,1.362168],[-1.457685,-6.505488,6.069647,-2.438768,-0.825334,5.011067,-4.319522,-8.741884,-3.886102,-4.181457,9.296413,3.834952,6.463154],[-8.105789,-1.582697,3.962872,9.205130,-0.958587,-0.677060,-8.309577,-3.503220,2.783367,5.132169,-8.160104,-1.544881,-4.234453],[6.198268,8.725042,-6.935785,-9.854401,0.389181,-3.538679,9.652096,-2.017393,5.906366,1.050251,-8.991281,-8.775969,-3.139935],[1.792857,1.166566,-9.518729,1.104364,-6.375922,0.363130,-6.619647,-5.569496,-1.636276,0.501328,8.010759,7.430095,-3.922332],[-2.295831,-8.139080,2.085267,7.582759,4.815805,1.479907,0.725089,-0.974693,-1.014940,-1.385924,4.049862,7.791101,8.359633],[7.242208,0.071312,-4.830761,1.375883,-3.702834,-1.479094,0.847340,8.545094,-1.128532,-3.339352,-9.392862,1.218940,-6.003357],[3.974518,4.858029,-0.151103,7.030404,-5.886304,7.165085,-7.859781,-6.735690,4.963927,-0.150370,5.611502,-4.635431,-3.641557],[-2.828343,2.553922,-0.862335,-1.294745,5.077933,8.756331,-2.105646,-8.514131,6.300057,8.215701,3.465775,8.138042,-8.096554],[-6.884386,3.736215,3.487888,-7.234327,-8.944455,2.121721,-1.137558,6.881791,8.205044,4.348258,-9.692782,5.095409,-2.086674],[-9.649261,-3.130848,-8.225263,3.670734,3.119871,-8.674169,1.867940,3.152243,2.106681,4.641858,8.321481,2.199360,-5.126339]],[[0.882066,3.864643,-8.635456,7.915470,-3.803609,7.322009,4.888239,-4.940674,-9.911309,-4.070729,-6.420851,1.482414,1.941348],[6.739430,5.934981,-0.665297,1.486730,9.628632,5.279590,-1.782879,-0.641810,-6.702688,9.020671,6.174881,-9.388757,7.069195],[-3.499516,3.389482,1.272355,-9.603630,-2.369323,9.657180,-9.913124,-7.740799,1.602122,-5.954639,-4.161585,-3.654219,4.063494],[-6.840999,6.715607,5.159013,-2.226502,3.885125,4.764216,1.237242,-6.793904,1.211017,7.762635,8.002353,-2.782649,-0.394338],[-2.724504,-5.766621,8.573766,4.281844,-5.194880,-5.864129,5.225156,-3.491724,2.359934,9.794610,-5.186487,-1.564577,-1.161110],[3.062058,1.198020,2.320780,-2.713163,-8.258331,-9.289109,-7.682236,-4.874777,-1.623417,5.932075,-2.571959,-8.663633,-8.189040],[-7.631333,-5.619558,-2.603720,6.040643,0.388329,5.415948,3.239469,0.856304,-1.601413,-8.806397,-5.920887,-3.117310,-1.782596],[-6.294874,-1.996520,4.769710,-6.423949,8.045541,5.009440,-4.291526,-7.969634,-8.334963,3.044999,7.339097,-4.870146,-0.759763],[-1.548561,-9.583521,4.059629,9.452562,5.623687,-0.863305,-2.272861,6.824139,4.184383,8.043010,3.609493,2.757598,1.487713],[-3.639059,-8.877296,0.970928,-0.885343,9.826195,-4.157377,1.978430,-8.985962,4.344452,-7.583632,-8.398670,4.869643,0.020702],[-8.818229,6.251991,9.675326,0.361513,0.662562,6.573090,-0.680942,2.935557,4.718056,-6.206298,7.637605,7.181426,-4.999963],[5.899314,3.699642,7.143458,6.563219,6.389304,-8.681308,-9.086342,0.756466,0.362506,6.442637,5.015519,-4.241881,-0.472434],[6.108388,6.971360,5.817636,8.698534,4.832297,-4.339001,-3.338808,6.399686,-7.226992,-5.137638,8.924583,0.879715,-2.292645],[-7.410714,3.674644,-0.888129,-2.956691,-7.410389,-6.388307,-3.245145,-3.890780,-3.743948,-3.479014,-4.535234,-3.590693,4.451734]],[[-9.763626,-1.504990,4.928121,3.582223,4.233604,1.431924,6.453236,5.938581,-6.512560,6.639725,8.573529,5.418805,-4.373908],[-7.964658,-0.453618,-9.557264,0.546652,0.949605,2.008940,9.729639,2.711537,-3.944071,-5.836887,-4.319542,3.300699,-6.350585],[-0.969414,9.175075,3.492124,0.587709,9.504087,-2.353294,-7.002581,2.256390,2.799538,-3.359679,2.023444,3.252919,-9.637711],[-9.545243,-9.097906,-8.558237,-2.412458,4.298662,-0.985524,6.600828,-9.199551,-3.254558,-3.867200,0.988499,-3.645688,-7.979639],[-3.433863,1.111389,8.123064,7.513014,-9.122602,-0.106284,8.960525,-1.426551,-2.679193,0.025305,-0.871576,6.458405,9.880159],[-9.484073,-7.195830,9.261943,-5.767128,-3.619774,1.709754,7.244976,0.501393,-2.523478,5.344768,-7.735145,6.772376,0.468061],[2.258962,-3.107382,3.302250,-0.809248,5.418748,-7.936668,7.183557,3.599976,-6.287838,-3.050691,4.737307,-4.126367,-5.115642],[-5.690210,-3.854249,8.536901,8.540847,-6.056183,-9.353376,-9.216878,9.041882,5.198057,3.195846,8.881790,-2.747850,-7.718108],[-7.236976,-4.276745,6.133472,-8.181729,-2.154525,-5.976078,5.013035,-0.990529,6.142443,5.007454,-7.775040,4.925759,-3.296679],[5.312078,3.609545,-1.873946,9.174299,-8.753437,4.516866,-5.329610,-4.071417,0.453276,-1.639762,0.359560,0.760993,-5.146443],[8.826442,1.176224,-5.725091,-3.323389,-3.022738,4.819978,-8.048288,2.408269,2.066979,4.923309,-2.333599,1.952358,0.302388],[-2.077568,-7.388581,-9.541307,9.431344,6.376884,-7.075492,8.027609,-3.270582,-1.138526,-8.327292,-5.309154,-7.522492,8.036865],[9.345512,4.823047,3.225009,4.881197,-3.989726,4.847559,0.283145,9.426866,8.316346,3.066892,5.474203,-6.579917,5.675523],[9.158917,-9.523151,-8.078671,-3.375296,-8.352045,1.214531,4.684237,1.568232,7.030630,7.761146,5.327242,9.828102,-1.315281]]], dtype = "float64")#candidate|5718|(10, 14, 13)|const|float64
bop_5719 = relay.subtract(call_5713.astype('int8'), relay.reshape(const_5718.astype('int8'), relay.shape_of(call_5713))) # shape=(10, 14, 13)
bop_5722 = relay.subtract(call_5714.astype('int8'), relay.reshape(const_5718.astype('int8'), relay.shape_of(call_5714))) # shape=(10, 14, 13)
output = relay.Tuple([bop_5719,])
output2 = relay.Tuple([bop_5722,])
func_5725 = relay.Function([], output)
mod['func_5725'] = func_5725
mod = relay.transform.InferType()(mod)
output = func_5725()
func_5726 = relay.Function([], output)
mutated_mod['func_5726'] = func_5726
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1634_call = mod.get_global_var('func_1634')
func_1636_call = mutated_mod.get_global_var('func_1636')
call_5739 = relay.TupleGetItem(func_1634_call(), 1)
call_5740 = relay.TupleGetItem(func_1636_call(), 1)
func_4582_call = mod.get_global_var('func_4582')
func_4583_call = mutated_mod.get_global_var('func_4583')
call_5741 = relay.TupleGetItem(func_4582_call(), 2)
call_5742 = relay.TupleGetItem(func_4583_call(), 2)
output = relay.Tuple([call_5739,call_5741,])
output2 = relay.Tuple([call_5740,call_5742,])
func_5756 = relay.Function([], output)
mod['func_5756'] = func_5756
mod = relay.transform.InferType()(mod)
mutated_mod['func_5756'] = func_5756
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5756_call = mutated_mod.get_global_var('func_5756')
call_5757 = func_5756_call()
output = call_5757
func_5758 = relay.Function([], output)
mutated_mod['func_5758'] = func_5758
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3538_call = mod.get_global_var('func_3538')
func_3539_call = mutated_mod.get_global_var('func_3539')
call_5766 = func_3538_call()
call_5767 = func_3538_call()
func_451_call = mod.get_global_var('func_451')
func_455_call = mutated_mod.get_global_var('func_455')
var_5798 = relay.var("var_5798", dtype = "bool", shape = (3072,))#candidate|5798|(3072,)|var|bool
const_5799 = relay.const([9,10,-9,2,9,8,8,8,2,3,-7,-6,7,-6,-5,2,2,1,-10,7,-3,-3,-1,-8,-1,6,6,-4,-7,3,-1,5,5,-7,1,8,-9,2,4,-4,2,2,1,10,-8,10,-6,-3,1,9,5,7,-8,3,-10,6,8,-10,4,7,-3,-9,3,1,3,-7,7,2,2,5,2,-4,9,-9,5,3,6,6,-8,-3,-9,9,2,-9,-7,-8,8,-1,-7,-10,-10,-8,-8,6,-3,7,9,6,-9,8,1,-9,8,-8,2,-5,2,9,-10,-4,-5,-3,-8,6,5,-5,7,-7,-4,2,-4,10,-2,6,5,-5], dtype = "int32")#candidate|5799|(126,)|const|int32
call_5797 = relay.TupleGetItem(func_451_call(relay.reshape(var_5798.astype('bool'), [16, 16, 12]), relay.reshape(const_5799.astype('int32'), [63, 2]), ), 0)
call_5800 = relay.TupleGetItem(func_455_call(relay.reshape(var_5798.astype('bool'), [16, 16, 12]), relay.reshape(const_5799.astype('int32'), [63, 2]), ), 0)
output = relay.Tuple([call_5766,call_5797,var_5798,const_5799,])
output2 = relay.Tuple([call_5767,call_5800,var_5798,const_5799,])
func_5804 = relay.Function([var_5798,], output)
mod['func_5804'] = func_5804
mod = relay.transform.InferType()(mod)
var_5805 = relay.var("var_5805", dtype = "bool", shape = (3072,))#candidate|5805|(3072,)|var|bool
output = func_5804(var_5805)
func_5806 = relay.Function([var_5805], output)
mutated_mod['func_5806'] = func_5806
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4683_call = mod.get_global_var('func_4683')
func_4684_call = mutated_mod.get_global_var('func_4684')
call_5863 = func_4683_call()
call_5864 = func_4683_call()
func_1744_call = mod.get_global_var('func_1744')
func_1746_call = mutated_mod.get_global_var('func_1746')
call_5874 = relay.TupleGetItem(func_1744_call(relay.reshape(call_5863.astype('float64'), [10, 14, 13])), 4)
call_5875 = relay.TupleGetItem(func_1746_call(relay.reshape(call_5863.astype('float64'), [10, 14, 13])), 4)
output = relay.Tuple([call_5863,call_5874,])
output2 = relay.Tuple([call_5864,call_5875,])
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
var_5897 = relay.var("var_5897", dtype = "float32", shape = (9, 15))#candidate|5897|(9, 15)|var|float32
uop_5898 = relay.sqrt(var_5897.astype('float32')) # shape=(9, 15)
func_1490_call = mod.get_global_var('func_1490')
func_1493_call = mutated_mod.get_global_var('func_1493')
var_5911 = relay.var("var_5911", dtype = "float64", shape = (600,))#candidate|5911|(600,)|var|float64
call_5910 = relay.TupleGetItem(func_1490_call(relay.reshape(var_5911.astype('float64'), [600,])), 1)
call_5912 = relay.TupleGetItem(func_1493_call(relay.reshape(var_5911.astype('float64'), [600,])), 1)
func_3556_call = mod.get_global_var('func_3556')
func_3558_call = mutated_mod.get_global_var('func_3558')
const_5922 = relay.const([[-7.196491,8.967277,-5.768168,8.185828,-9.999802,9.555275,-2.074371,-7.294740,-6.274106,4.897639,0.310676,-0.221253],[-8.598826,2.036827,8.077985,6.505141,2.365278,-4.017600,8.981351,-8.765861,-9.809843,3.629432,-4.907769,-3.494625],[6.507076,-3.014738,0.030558,1.418949,-9.139229,-3.223069,-2.231075,0.612587,7.421992,6.476368,-9.458146,-3.575493],[0.827446,3.033104,-0.578388,-8.578641,5.764682,-2.304120,2.330636,8.558436,-2.359801,-0.729820,5.264174,-6.010120],[3.992615,2.876597,5.679296,-7.602047,0.416970,6.990635,2.653418,6.546209,-9.371039,6.443350,-7.648394,2.305884],[9.804982,3.022982,0.412119,4.488388,6.228860,-6.718667,-1.460554,6.746044,-8.957051,4.144215,-0.750927,9.209639]], dtype = "float64")#candidate|5922|(6, 12)|const|float64
call_5921 = func_3556_call(relay.reshape(const_5922.astype('float64'), [3, 6, 4]))
call_5923 = func_3556_call(relay.reshape(const_5922.astype('float64'), [3, 6, 4]))
output = relay.Tuple([uop_5898,call_5910,var_5911,call_5921,const_5922,])
output2 = relay.Tuple([uop_5898,call_5912,var_5911,call_5923,const_5922,])
func_5928 = relay.Function([var_5897,var_5911,], output)
mod['func_5928'] = func_5928
mod = relay.transform.InferType()(mod)
mutated_mod['func_5928'] = func_5928
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5928_call = mutated_mod.get_global_var('func_5928')
var_5930 = relay.var("var_5930", dtype = "float32", shape = (9, 15))#candidate|5930|(9, 15)|var|float32
var_5931 = relay.var("var_5931", dtype = "float64", shape = (600,))#candidate|5931|(600,)|var|float64
call_5929 = func_5928_call(var_5930,var_5931,)
output = call_5929
func_5932 = relay.Function([var_5930,var_5931,], output)
mutated_mod['func_5932'] = func_5932
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1659_call = mod.get_global_var('func_1659')
func_1661_call = mutated_mod.get_global_var('func_1661')
call_5940 = func_1659_call()
call_5941 = func_1659_call()
func_5017_call = mod.get_global_var('func_5017')
func_5019_call = mutated_mod.get_global_var('func_5019')
call_5953 = func_5017_call()
call_5954 = func_5017_call()
func_5404_call = mod.get_global_var('func_5404')
func_5405_call = mutated_mod.get_global_var('func_5405')
call_5955 = func_5404_call()
call_5956 = func_5404_call()
func_4193_call = mod.get_global_var('func_4193')
func_4196_call = mutated_mod.get_global_var('func_4196')
var_5965 = relay.var("var_5965", dtype = "bool", shape = ())#candidate|5965|()|var|bool
var_5966 = relay.var("var_5966", dtype = "bool", shape = (80,))#candidate|5966|(80,)|var|bool
call_5964 = relay.TupleGetItem(func_4193_call(relay.reshape(var_5965.astype('bool'), []), relay.reshape(var_5966.astype('bool'), [80,]), ), 3)
call_5967 = relay.TupleGetItem(func_4196_call(relay.reshape(var_5965.astype('bool'), []), relay.reshape(var_5966.astype('bool'), [80,]), ), 3)
output = relay.Tuple([call_5940,call_5953,call_5955,call_5964,var_5965,var_5966,])
output2 = relay.Tuple([call_5941,call_5954,call_5956,call_5967,var_5965,var_5966,])
func_5977 = relay.Function([var_5965,var_5966,], output)
mod['func_5977'] = func_5977
mod = relay.transform.InferType()(mod)
mutated_mod['func_5977'] = func_5977
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5977_call = mutated_mod.get_global_var('func_5977')
var_5979 = relay.var("var_5979", dtype = "bool", shape = ())#candidate|5979|()|var|bool
var_5980 = relay.var("var_5980", dtype = "bool", shape = (80,))#candidate|5980|(80,)|var|bool
call_5978 = func_5977_call(var_5979,var_5980,)
output = call_5978
func_5981 = relay.Function([var_5979,var_5980,], output)
mutated_mod['func_5981'] = func_5981
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2359_call = mod.get_global_var('func_2359')
func_2360_call = mutated_mod.get_global_var('func_2360')
call_6014 = func_2359_call()
call_6015 = func_2359_call()
func_1188_call = mod.get_global_var('func_1188')
func_1190_call = mutated_mod.get_global_var('func_1190')
call_6025 = func_1188_call()
call_6026 = func_1188_call()
func_3268_call = mod.get_global_var('func_3268')
func_3269_call = mutated_mod.get_global_var('func_3269')
call_6034 = relay.TupleGetItem(func_3268_call(), 0)
call_6035 = relay.TupleGetItem(func_3269_call(), 0)
func_3556_call = mod.get_global_var('func_3556')
func_3558_call = mutated_mod.get_global_var('func_3558')
var_6071 = relay.var("var_6071", dtype = "float64", shape = (72,))#candidate|6071|(72,)|var|float64
call_6070 = func_3556_call(relay.reshape(var_6071.astype('float64'), [3, 6, 4]))
call_6072 = func_3556_call(relay.reshape(var_6071.astype('float64'), [3, 6, 4]))
output = relay.Tuple([call_6014,call_6025,call_6034,call_6070,var_6071,])
output2 = relay.Tuple([call_6015,call_6026,call_6035,call_6072,var_6071,])
func_6083 = relay.Function([var_6071,], output)
mod['func_6083'] = func_6083
mod = relay.transform.InferType()(mod)
mutated_mod['func_6083'] = func_6083
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6084 = relay.var("var_6084", dtype = "float64", shape = (72,))#candidate|6084|(72,)|var|float64
func_6083_call = mutated_mod.get_global_var('func_6083')
call_6085 = func_6083_call(var_6084)
output = call_6085
func_6086 = relay.Function([var_6084], output)
mutated_mod['func_6086'] = func_6086
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3234_call = mod.get_global_var('func_3234')
func_3236_call = mutated_mod.get_global_var('func_3236')
call_6117 = relay.TupleGetItem(func_3234_call(), 0)
call_6118 = relay.TupleGetItem(func_3236_call(), 0)
func_2212_call = mod.get_global_var('func_2212')
func_2214_call = mutated_mod.get_global_var('func_2214')
call_6157 = func_2212_call()
call_6158 = func_2212_call()
output = relay.Tuple([call_6117,call_6157,])
output2 = relay.Tuple([call_6118,call_6158,])
func_6162 = relay.Function([], output)
mod['func_6162'] = func_6162
mod = relay.transform.InferType()(mod)
output = func_6162()
func_6163 = relay.Function([], output)
mutated_mod['func_6163'] = func_6163
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4496_call = mod.get_global_var('func_4496')
func_4497_call = mutated_mod.get_global_var('func_4497')
call_6173 = relay.TupleGetItem(func_4496_call(), 1)
call_6174 = relay.TupleGetItem(func_4497_call(), 1)
uop_6191 = relay.log2(call_6173.astype('float32')) # shape=(10, 14, 13)
uop_6193 = relay.log2(call_6174.astype('float32')) # shape=(10, 14, 13)
output = uop_6191
output2 = uop_6193
func_6195 = relay.Function([], output)
mod['func_6195'] = func_6195
mod = relay.transform.InferType()(mod)
mutated_mod['func_6195'] = func_6195
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6195_call = mutated_mod.get_global_var('func_6195')
call_6196 = func_6195_call()
output = call_6196
func_6197 = relay.Function([], output)
mutated_mod['func_6197'] = func_6197
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3268_call = mod.get_global_var('func_3268')
func_3269_call = mutated_mod.get_global_var('func_3269')
call_6221 = relay.TupleGetItem(func_3268_call(), 0)
call_6222 = relay.TupleGetItem(func_3269_call(), 0)
output = relay.Tuple([call_6221,])
output2 = relay.Tuple([call_6222,])
func_6223 = relay.Function([], output)
mod['func_6223'] = func_6223
mod = relay.transform.InferType()(mod)
mutated_mod['func_6223'] = func_6223
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6223_call = mutated_mod.get_global_var('func_6223')
call_6224 = func_6223_call()
output = call_6224
func_6225 = relay.Function([], output)
mutated_mod['func_6225'] = func_6225
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3024_call = mod.get_global_var('func_3024')
func_3025_call = mutated_mod.get_global_var('func_3025')
call_6228 = relay.TupleGetItem(func_3024_call(), 0)
call_6229 = relay.TupleGetItem(func_3025_call(), 0)
output = call_6228
output2 = call_6229
func_6230 = relay.Function([], output)
mod['func_6230'] = func_6230
mod = relay.transform.InferType()(mod)
mutated_mod['func_6230'] = func_6230
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6230_call = mutated_mod.get_global_var('func_6230')
call_6231 = func_6230_call()
output = call_6231
func_6232 = relay.Function([], output)
mutated_mod['func_6232'] = func_6232
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5725_call = mod.get_global_var('func_5725')
func_5726_call = mutated_mod.get_global_var('func_5726')
call_6236 = relay.TupleGetItem(func_5725_call(), 0)
call_6237 = relay.TupleGetItem(func_5726_call(), 0)
func_6195_call = mod.get_global_var('func_6195')
func_6197_call = mutated_mod.get_global_var('func_6197')
call_6240 = func_6195_call()
call_6241 = func_6195_call()
func_1241_call = mod.get_global_var('func_1241')
func_1243_call = mutated_mod.get_global_var('func_1243')
call_6245 = relay.TupleGetItem(func_1241_call(relay.reshape(call_6240.astype('float64'), [10, 14, 13])), 0)
call_6246 = relay.TupleGetItem(func_1243_call(relay.reshape(call_6240.astype('float64'), [10, 14, 13])), 0)
output = relay.Tuple([call_6236,call_6240,call_6245,])
output2 = relay.Tuple([call_6237,call_6241,call_6246,])
func_6254 = relay.Function([], output)
mod['func_6254'] = func_6254
mod = relay.transform.InferType()(mod)
output = func_6254()
func_6255 = relay.Function([], output)
mutated_mod['func_6255'] = func_6255
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6195_call = mod.get_global_var('func_6195')
func_6197_call = mutated_mod.get_global_var('func_6197')
call_6334 = func_6195_call()
call_6335 = func_6195_call()
output = call_6334
output2 = call_6335
func_6349 = relay.Function([], output)
mod['func_6349'] = func_6349
mod = relay.transform.InferType()(mod)
mutated_mod['func_6349'] = func_6349
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6349_call = mutated_mod.get_global_var('func_6349')
call_6350 = func_6349_call()
output = call_6350
func_6351 = relay.Function([], output)
mutated_mod['func_6351'] = func_6351
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6398 = relay.var("var_6398", dtype = "uint64", shape = (7, 1, 16))#candidate|6398|(7, 1, 16)|var|uint64
const_6399 = relay.const([[[-3,-4,-3,-8,-1,-10,-9,-5,-4,6,1,7,-3,-7,9,8],[4,-3,-7,5,-1,10,-5,-9,-10,-7,10,-6,6,10,9,-7],[2,-1,10,-4,-10,-3,1,-1,6,4,4,9,-7,5,-8,10],[-2,-6,-6,5,9,8,9,-9,-9,-1,4,3,2,7,2,-8],[8,-7,8,-8,-10,-5,10,-4,-8,4,-8,5,-6,-7,-2,3],[3,-4,-3,-6,-3,-4,6,3,-4,7,-5,1,7,-10,-5,10],[-4,-8,1,4,8,6,-5,-9,-6,-10,-1,2,8,-8,4,4],[-2,-9,-8,-6,8,-10,3,-1,-6,-9,1,-4,3,6,7,9],[10,-6,-8,5,-4,-10,-4,5,-1,4,6,-1,-9,-10,6,-8],[7,7,6,-3,8,-9,-4,10,-1,-5,2,9,4,-10,9,7]],[[1,9,-5,-2,-6,5,7,3,-10,8,8,-5,-7,3,4,9],[-5,5,-3,-2,9,-8,3,-6,-4,8,2,-4,-10,-2,-10,-10],[-1,4,-3,2,-6,-8,-2,3,-1,-7,8,-9,-2,-3,-1,-5],[9,4,-8,3,7,-2,-10,-6,-9,1,6,-6,-10,-1,3,1],[9,-5,2,-10,3,-9,-10,1,9,7,-3,-6,-1,2,-6,7],[10,4,-1,-2,-8,-7,-7,-8,-2,4,7,8,10,3,3,-3],[3,5,-2,8,10,-8,6,3,-2,-5,8,8,-3,6,-2,-1],[4,9,-4,6,4,1,2,10,-3,-5,-8,9,-6,1,3,3],[9,3,-8,-9,3,-2,4,-10,-5,-7,8,8,2,1,1,-5],[5,8,-9,6,5,-8,8,-5,3,-9,10,8,-7,9,3,10]],[[4,-3,-5,4,7,-10,-9,1,10,6,7,4,-3,4,9,-5],[-4,-3,-7,10,8,-10,-6,1,-3,6,1,6,4,-9,5,-3],[2,7,-2,5,8,9,8,-10,8,-1,-7,-2,-6,-4,-7,-8],[-5,-10,4,9,1,-6,7,-10,-5,4,5,-4,7,9,-7,4],[-6,8,-10,-1,-6,-1,-6,-10,9,2,-9,4,6,-3,4,2],[-2,9,-9,2,-1,10,4,-8,-5,-9,-9,-4,8,-6,3,-2],[10,6,4,-7,-2,4,-9,9,3,10,-10,-4,2,-1,-8,1],[-4,9,4,5,-5,2,-1,9,10,5,4,10,-1,-10,-4,9],[7,-8,-6,-8,3,-6,-2,10,4,4,7,3,-5,-9,5,8],[5,-2,-2,3,-10,-2,6,6,9,10,-4,-6,-8,-9,-2,-5]],[[-3,-10,-9,2,2,6,8,-7,-2,5,-10,6,-3,-2,-1,1],[-8,-1,-4,10,7,-3,8,9,9,-7,-4,-8,7,1,-9,-4],[-3,-3,5,4,-9,-4,9,8,-9,8,9,2,5,6,8,-10],[4,-10,9,1,-3,7,-2,1,-2,-7,-4,-7,-4,5,-4,3],[-10,-6,-8,-9,6,4,-10,1,5,-3,9,-10,-4,3,1,7],[-10,2,-2,9,-6,-5,-8,-10,-4,-2,2,6,-6,-7,8,10],[-7,-5,5,4,-5,-8,5,5,-1,-4,6,3,10,3,-2,-5],[-7,-7,-2,-4,9,-1,-1,6,1,7,10,3,7,-10,-9,9],[5,8,8,6,5,-4,2,-8,-9,-2,2,3,-1,2,7,-10],[9,2,2,-5,-5,-3,8,-2,6,-8,-1,-10,1,4,3,-4]],[[4,10,-4,-2,5,-6,7,-9,-3,-1,-7,7,-1,8,7,-10],[8,6,6,-10,1,3,-5,-1,1,-5,1,6,4,-9,8,1],[-9,7,-5,8,7,4,-6,-2,-8,-3,8,-2,5,-3,-3,10],[-3,9,6,-4,1,-4,-4,1,-3,1,-6,-4,-8,-6,5,-3],[5,-6,1,3,-7,-6,5,-5,4,2,10,-2,4,9,4,-8],[8,-9,2,-1,-2,2,-8,8,4,3,5,-4,3,-10,5,-7],[10,2,-9,2,3,9,-2,3,-6,-10,2,-1,7,-4,-9,-7],[-7,4,-5,-9,2,-8,-4,10,9,-2,6,-4,7,5,-8,-9],[-3,-3,1,7,-10,10,7,-6,4,5,-3,2,8,-10,-2,-1],[3,-3,8,10,4,1,-1,-8,-7,4,-4,4,4,6,4,-10]],[[3,-1,-3,8,10,9,-10,-6,-9,-9,-5,-5,-6,4,10,8],[7,-6,-10,-8,-6,4,5,3,10,-7,4,5,-4,-1,-5,10],[8,-4,10,3,-2,-4,-6,-1,8,5,-1,-5,3,9,-6,-2],[5,-5,10,3,-4,9,3,-8,7,6,-6,-2,8,7,-10,-8],[-6,10,-10,8,-1,4,6,-6,7,-2,4,2,-7,3,9,-2],[6,-1,-6,-10,5,-10,8,-5,-1,-8,2,6,2,-7,-3,-3],[1,-5,2,-4,1,-7,4,-4,10,-8,5,-2,-5,5,7,7],[2,5,-7,-3,2,7,-4,9,-4,-6,2,5,8,5,10,1],[4,-7,4,-1,-10,2,-1,7,1,6,3,1,1,-7,8,2],[6,4,9,-6,-6,-4,1,-2,-9,6,-10,-5,6,2,10,7]],[[5,-5,7,-5,10,-7,3,3,-2,5,-9,2,2,1,-10,-7],[-8,-9,-4,7,4,-6,7,-10,-10,10,-3,7,10,7,-6,5],[9,-10,-8,6,5,10,3,1,-5,5,5,3,-9,5,7,1],[6,8,8,-8,7,-5,10,-6,-8,4,2,-1,10,-8,8,2],[1,-9,-7,2,-9,-6,4,5,-2,9,6,7,-8,4,6,-1],[7,8,9,10,8,8,-8,7,-1,4,-6,5,9,1,5,-4],[4,-8,1,-2,4,4,2,-1,-6,4,9,-6,-9,4,9,-8],[-10,-7,-4,2,10,3,-7,-8,-1,-5,-10,-9,-9,2,-2,2],[-7,-5,-9,-1,4,2,-8,4,-3,-2,-1,-1,-5,-8,-5,1],[1,-3,4,9,9,9,4,-9,-4,1,3,6,6,6,-6,3]]], dtype = "uint64")#candidate|6399|(7, 10, 16)|const|uint64
bop_6400 = relay.add(var_6398.astype('uint64'), const_6399.astype('uint64')) # shape=(7, 10, 16)
output = bop_6400
output2 = bop_6400
func_6413 = relay.Function([var_6398,], output)
mod['func_6413'] = func_6413
mod = relay.transform.InferType()(mod)
mutated_mod['func_6413'] = func_6413
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6414 = relay.var("var_6414", dtype = "uint64", shape = (7, 1, 16))#candidate|6414|(7, 1, 16)|var|uint64
func_6413_call = mutated_mod.get_global_var('func_6413')
call_6415 = func_6413_call(var_6414)
output = call_6415
func_6416 = relay.Function([var_6414], output)
mutated_mod['func_6416'] = func_6416
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3214_call = mod.get_global_var('func_3214')
func_3215_call = mutated_mod.get_global_var('func_3215')
call_6444 = func_3214_call()
call_6445 = func_3214_call()
output = relay.Tuple([call_6444,])
output2 = relay.Tuple([call_6445,])
func_6449 = relay.Function([], output)
mod['func_6449'] = func_6449
mod = relay.transform.InferType()(mod)
output = func_6449()
func_6450 = relay.Function([], output)
mutated_mod['func_6450'] = func_6450
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3676_call = mod.get_global_var('func_3676')
func_3678_call = mutated_mod.get_global_var('func_3678')
call_6480 = relay.TupleGetItem(func_3676_call(), 0)
call_6481 = relay.TupleGetItem(func_3678_call(), 0)
output = call_6480
output2 = call_6481
func_6501 = relay.Function([], output)
mod['func_6501'] = func_6501
mod = relay.transform.InferType()(mod)
output = func_6501()
func_6502 = relay.Function([], output)
mutated_mod['func_6502'] = func_6502
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6223_call = mod.get_global_var('func_6223')
func_6225_call = mutated_mod.get_global_var('func_6225')
call_6567 = relay.TupleGetItem(func_6223_call(), 0)
call_6568 = relay.TupleGetItem(func_6225_call(), 0)
func_5175_call = mod.get_global_var('func_5175')
func_5178_call = mutated_mod.get_global_var('func_5178')
const_6593 = relay.const([[False,True,True,False,False,False,False,False,True,False,False,True,False,False,True,True,True,True,True,False,False,False,True,True,True,False,False,False,False,True,False,True,False,True,True,False,False,False,False,True,False,True,False,True,True,True,False,True,True,False,True,True,False,True,False,True,True,True,True,True,False,True,False,True,True,False,True,True,False,False,False,False,True,True,True,False,False,False,True,True]], dtype = "bool")#candidate|6593|(1, 80)|const|bool
call_6592 = relay.TupleGetItem(func_5175_call(relay.reshape(const_6593.astype('bool'), [80,])), 1)
call_6594 = relay.TupleGetItem(func_5178_call(relay.reshape(const_6593.astype('bool'), [80,])), 1)
output = relay.Tuple([call_6567,call_6592,const_6593,])
output2 = relay.Tuple([call_6568,call_6594,const_6593,])
func_6598 = relay.Function([], output)
mod['func_6598'] = func_6598
mod = relay.transform.InferType()(mod)
output = func_6598()
func_6599 = relay.Function([], output)
mutated_mod['func_6599'] = func_6599
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3676_call = mod.get_global_var('func_3676')
func_3678_call = mutated_mod.get_global_var('func_3678')
call_6605 = relay.TupleGetItem(func_3676_call(), 0)
call_6606 = relay.TupleGetItem(func_3678_call(), 0)
func_3143_call = mod.get_global_var('func_3143')
func_3149_call = mutated_mod.get_global_var('func_3149')
var_6608 = relay.var("var_6608", dtype = "uint32", shape = ())#candidate|6608|()|var|uint32
const_6609 = relay.const([10,4,1,1,4,1,9,-1,-8,10,-1,-2,9,5,5,-3,-8,-8,3,-4,-7,8,9,-6,8,-7,-10,-2,-5,3,7,-4,4,-7,1,5,6,-5,-5,-10,-7,-1,-7,6,-2,-3,-4,7,1,7,5,4,-5,6,2,-2,4,5,-8,7,-9,-8,-7,3,9,2,1,-5,6,8,-7,4,4,7,10,2,2,2,-7,1,-2,1,-10,-2,10,-2,-2,10,-8,8,1,-7,1,4,4,-5,-8,-2,3,-5,-5,1,7,-3,-10,-5,2,4,9,1,-5,10], dtype = "uint8")#candidate|6609|(112,)|const|uint8
const_6610 = relay.const([4,-7,10,-7,-9,-4,-1,5,5,-8,-1,1,2,10,-9,-5,10,3,-4,-3,-7,3,-1,-4,6,-9,8,-10,-6,-2,5,8,-9,-5,3,4,-5,8,7,-6,3,-1,5,-1,4,-6,1,6,8,1,-1,9,-3,-4,10,-3,-7,-2,-8,5,-6,-2,-8,-7,2,-6,-2,-9,-6,5,-4,7,-3,-6,-3,4,6,8,-4,10,10,1,3,-7,4,4,-8,-1,-1,-3,-2,6,3,-1,7,-5,7,1,7,-8,-7,10,3,-10,2,9,-8,-1,-8,-10,-2,-4,-2,-9,-10,-7,-1,-6,-10,-1,8,6,4,1,-8,7,-5,-10,-5,-3,8,-3,8,-5,6,3,-3,-3,6,1], dtype = "uint8")#candidate|6610|(140,)|const|uint8
call_6607 = relay.TupleGetItem(func_3143_call(relay.reshape(var_6608.astype('uint32'), []), relay.reshape(const_6609.astype('uint8'), [28, 4]), relay.reshape(const_6610.astype('uint8'), [140,]), relay.reshape(const_6610.astype('uint8'), [140,]), ), 4)
call_6611 = relay.TupleGetItem(func_3149_call(relay.reshape(var_6608.astype('uint32'), []), relay.reshape(const_6609.astype('uint8'), [28, 4]), relay.reshape(const_6610.astype('uint8'), [140,]), relay.reshape(const_6610.astype('uint8'), [140,]), ), 4)
output = relay.Tuple([call_6605,call_6607,var_6608,const_6609,const_6610,])
output2 = relay.Tuple([call_6606,call_6611,var_6608,const_6609,const_6610,])
func_6619 = relay.Function([var_6608,], output)
mod['func_6619'] = func_6619
mod = relay.transform.InferType()(mod)
mutated_mod['func_6619'] = func_6619
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6620 = relay.var("var_6620", dtype = "uint32", shape = ())#candidate|6620|()|var|uint32
func_6619_call = mutated_mod.get_global_var('func_6619')
call_6621 = func_6619_call(var_6620)
output = call_6621
func_6622 = relay.Function([var_6620], output)
mutated_mod['func_6622'] = func_6622
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6195_call = mod.get_global_var('func_6195')
func_6197_call = mutated_mod.get_global_var('func_6197')
call_6624 = func_6195_call()
call_6625 = func_6195_call()
func_2736_call = mod.get_global_var('func_2736')
func_2740_call = mutated_mod.get_global_var('func_2740')
var_6627 = relay.var("var_6627", dtype = "uint8", shape = (112,))#candidate|6627|(112,)|var|uint8
var_6628 = relay.var("var_6628", dtype = "uint8", shape = (140,))#candidate|6628|(140,)|var|uint8
call_6626 = relay.TupleGetItem(func_2736_call(relay.reshape(call_6624.astype('float64'), [10, 14, 13]), relay.reshape(var_6627.astype('uint8'), [112,]), relay.reshape(var_6628.astype('uint8'), [35, 4]), ), 5)
call_6629 = relay.TupleGetItem(func_2740_call(relay.reshape(call_6624.astype('float64'), [10, 14, 13]), relay.reshape(var_6627.astype('uint8'), [112,]), relay.reshape(var_6628.astype('uint8'), [35, 4]), ), 5)
func_3024_call = mod.get_global_var('func_3024')
func_3025_call = mutated_mod.get_global_var('func_3025')
call_6646 = relay.TupleGetItem(func_3024_call(), 0)
call_6647 = relay.TupleGetItem(func_3025_call(), 0)
func_3214_call = mod.get_global_var('func_3214')
func_3215_call = mutated_mod.get_global_var('func_3215')
call_6654 = func_3214_call()
call_6655 = func_3214_call()
func_3491_call = mod.get_global_var('func_3491')
func_3495_call = mutated_mod.get_global_var('func_3495')
var_6657 = relay.var("var_6657", dtype = "bool", shape = ())#candidate|6657|()|var|bool
var_6658 = relay.var("var_6658", dtype = "bool", shape = (80,))#candidate|6658|(80,)|var|bool
call_6656 = func_3491_call(relay.reshape(var_6657.astype('bool'), []), relay.reshape(var_6658.astype('bool'), [1, 5, 16]), )
call_6659 = func_3491_call(relay.reshape(var_6657.astype('bool'), []), relay.reshape(var_6658.astype('bool'), [1, 5, 16]), )
bop_6673 = relay.divide(call_6654.astype('float32'), relay.reshape(call_6624.astype('float32'), relay.shape_of(call_6654))) # shape=(10, 14, 13)
bop_6676 = relay.divide(call_6655.astype('float32'), relay.reshape(call_6625.astype('float32'), relay.shape_of(call_6655))) # shape=(10, 14, 13)
func_5804_call = mod.get_global_var('func_5804')
func_5806_call = mutated_mod.get_global_var('func_5806')
var_6681 = relay.var("var_6681", dtype = "bool", shape = (3072,))#candidate|6681|(3072,)|var|bool
call_6680 = relay.TupleGetItem(func_5804_call(relay.reshape(var_6681.astype('bool'), [3072,])), 2)
call_6682 = relay.TupleGetItem(func_5806_call(relay.reshape(var_6681.astype('bool'), [3072,])), 2)
output = relay.Tuple([call_6626,var_6627,var_6628,call_6646,call_6656,var_6657,var_6658,bop_6673,call_6680,var_6681,])
output2 = relay.Tuple([call_6629,var_6627,var_6628,call_6647,call_6659,var_6657,var_6658,bop_6676,call_6682,var_6681,])
func_6686 = relay.Function([var_6627,var_6628,var_6657,var_6658,var_6681,], output)
mod['func_6686'] = func_6686
mod = relay.transform.InferType()(mod)
var_6687 = relay.var("var_6687", dtype = "uint8", shape = (112,))#candidate|6687|(112,)|var|uint8
var_6688 = relay.var("var_6688", dtype = "uint8", shape = (140,))#candidate|6688|(140,)|var|uint8
var_6689 = relay.var("var_6689", dtype = "bool", shape = ())#candidate|6689|()|var|bool
var_6690 = relay.var("var_6690", dtype = "bool", shape = (80,))#candidate|6690|(80,)|var|bool
var_6691 = relay.var("var_6691", dtype = "bool", shape = (3072,))#candidate|6691|(3072,)|var|bool
output = func_6686(var_6687,var_6688,var_6689,var_6690,var_6691,)
func_6692 = relay.Function([var_6687,var_6688,var_6689,var_6690,var_6691,], output)
mutated_mod['func_6692'] = func_6692
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4005_call = mod.get_global_var('func_4005')
func_4006_call = mutated_mod.get_global_var('func_4006')
call_6729 = relay.TupleGetItem(func_4005_call(), 0)
call_6730 = relay.TupleGetItem(func_4006_call(), 0)
func_286_call = mod.get_global_var('func_286')
func_289_call = mutated_mod.get_global_var('func_289')
var_6734 = relay.var("var_6734", dtype = "int32", shape = (126,))#candidate|6734|(126,)|var|int32
call_6733 = relay.TupleGetItem(func_286_call(relay.reshape(var_6734.astype('int32'), [6, 7, 3]), relay.reshape(var_6734.astype('int32'), [6, 7, 3]), ), 0)
call_6735 = relay.TupleGetItem(func_289_call(relay.reshape(var_6734.astype('int32'), [6, 7, 3]), relay.reshape(var_6734.astype('int32'), [6, 7, 3]), ), 0)
func_6223_call = mod.get_global_var('func_6223')
func_6225_call = mutated_mod.get_global_var('func_6225')
call_6738 = relay.TupleGetItem(func_6223_call(), 0)
call_6739 = relay.TupleGetItem(func_6225_call(), 0)
output = relay.Tuple([call_6729,call_6733,var_6734,call_6738,])
output2 = relay.Tuple([call_6730,call_6735,var_6734,call_6739,])
func_6756 = relay.Function([var_6734,], output)
mod['func_6756'] = func_6756
mod = relay.transform.InferType()(mod)
mutated_mod['func_6756'] = func_6756
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6757 = relay.var("var_6757", dtype = "int32", shape = (126,))#candidate|6757|(126,)|var|int32
func_6756_call = mutated_mod.get_global_var('func_6756')
call_6758 = func_6756_call(var_6757)
output = call_6758
func_6759 = relay.Function([var_6757], output)
mutated_mod['func_6759'] = func_6759
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6795 = relay.const([[[-0.432977,2.770425,0.256502,2.456699,3.329671,-8.204032,3.115581,5.860031,1.103801,-7.228777],[1.167981,0.294211,6.887587,-5.425560,5.385216,6.838276,1.534162,-2.909484,5.336163,8.581793],[9.260578,-9.087380,5.008099,-5.709257,3.772086,-0.603465,4.258954,7.240044,-1.214133,-3.761503]]], dtype = "float64")#candidate|6795|(1, 3, 10)|const|float64
uop_6796 = relay.sigmoid(const_6795.astype('float64')) # shape=(1, 3, 10)
output = relay.Tuple([uop_6796,])
output2 = relay.Tuple([uop_6796,])
func_6802 = relay.Function([], output)
mod['func_6802'] = func_6802
mod = relay.transform.InferType()(mod)
output = func_6802()
func_6803 = relay.Function([], output)
mutated_mod['func_6803'] = func_6803
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3749_call = mod.get_global_var('func_3749')
func_3751_call = mutated_mod.get_global_var('func_3751')
call_6826 = relay.TupleGetItem(func_3749_call(), 1)
call_6827 = relay.TupleGetItem(func_3751_call(), 1)
func_6413_call = mod.get_global_var('func_6413')
func_6416_call = mutated_mod.get_global_var('func_6416')
const_6841 = relay.const([[7,2],[-8,7],[8,-6],[9,-6],[-10,1],[9,7],[-9,-10],[1,8],[7,-9],[-4,-8],[-10,-9],[-10,7],[4,-5],[-2,-8],[7,5],[7,6],[-3,8],[1,-4],[-2,2],[-7,-1],[-9,-5],[-3,3],[-4,-8],[2,-4],[6,6],[10,10],[2,4],[-1,4],[5,10],[-4,-8],[1,-1],[7,-2],[7,-2],[-8,1],[-4,-1],[1,-4],[5,-4],[7,9],[-7,5],[-6,-9],[-4,2],[-3,2],[-7,10],[-8,-6],[-8,-4],[-4,5],[3,-5],[6,2],[3,2],[6,-3],[6,-2],[-8,9],[-1,-3],[8,-6],[9,-10],[3,4]], dtype = "uint64")#candidate|6841|(56, 2)|const|uint64
call_6840 = func_6413_call(relay.reshape(const_6841.astype('uint64'), [7, 1, 16]))
call_6842 = func_6413_call(relay.reshape(const_6841.astype('uint64'), [7, 1, 16]))
output = relay.Tuple([call_6826,call_6840,const_6841,])
output2 = relay.Tuple([call_6827,call_6842,const_6841,])
func_6849 = relay.Function([], output)
mod['func_6849'] = func_6849
mod = relay.transform.InferType()(mod)
output = func_6849()
func_6850 = relay.Function([], output)
mutated_mod['func_6850'] = func_6850
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1659_call = mod.get_global_var('func_1659')
func_1661_call = mutated_mod.get_global_var('func_1661')
call_6851 = func_1659_call()
call_6852 = func_1659_call()
output = relay.Tuple([call_6851,])
output2 = relay.Tuple([call_6852,])
func_6883 = relay.Function([], output)
mod['func_6883'] = func_6883
mod = relay.transform.InferType()(mod)
mutated_mod['func_6883'] = func_6883
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6883_call = mutated_mod.get_global_var('func_6883')
call_6884 = func_6883_call()
output = call_6884
func_6885 = relay.Function([], output)
mutated_mod['func_6885'] = func_6885
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3183_call = mod.get_global_var('func_3183')
func_3185_call = mutated_mod.get_global_var('func_3185')
call_6903 = func_3183_call()
call_6904 = func_3183_call()
func_3360_call = mod.get_global_var('func_3360')
func_3366_call = mutated_mod.get_global_var('func_3366')
const_6919 = relay.const([[True,False,False,True,False,False,True,False,False,False,False,True,False,False,True,False,False,False,True,True,True,True,False,True,False,False,True,True,False,False,True,False,False,False,True,False,False,False,False,False,False,True,True,False,True,True,False,False,True,False,True,True,True,True,False,True,True,True,True,False,True,False,False,True,False,True,False,True,True,False,True,True,True,True,True,True,False,False,True,True,False,False,False,True,True,True,True,True,False,False,True,False,False,True,True,True,False,True,False,True,False,True,False,True,False,True,False,False,True,True,False,True,True,False,True,True,True,False,False,False,False,True,False,False,False,True,True,False,True,True,True,True,True,True,False,True,False,True,False,False,False,False,True,False,False,False,True,False,False,True,False,False,False,False,True,False,True,False,False,False,False,True,True,True,False,False,False,False,True,False,False,True,False,False,True,True,False,False,True,True,True,True,True,True,True,False,True,False,True,True,True,True,False,False,False,False,False,False,True,True,True,True,True,True,True,False,False,False,True,True,True,False,False,False,False,True,True,True,False,False,True,True,True,True,True,True,False,False,True,True,True,False,False,False]], dtype = "bool")#candidate|6919|(1, 234)|const|bool
const_6920 = relay.const([2,3,-5,3,8,5,9,-1,-10,3,9,7,4,5,1,-3,8,-10,4,4,-5,6,-4,6,6,-8,-1,2,8,5,1,-4,-5,-5,8,-2,10,-5,-5,-6,4,7,1,-9,7,8,-5,1,5,-8,7,3,10,-10,3,-9,2,-10,-3,1,6,-10,-2,-10,8,9,10,1,-4,-8,-10,3,10,6,4,-5,-7,-1,7,5,1,-1,5,-2,4,5,-6,-8,2,2,-1,6,4,-6,-1,6,-2,3,-8,8,7,-8,10,7,-7,-9,6,6,-5,2,-1,7,5,3,-7,7,-2,6,8,5,-4,4,2,-1,10,4,-2,-7,5,10,10,-7,-2,-6,6,-6,8,10,9,8], dtype = "uint8")#candidate|6920|(140,)|const|uint8
const_6921 = relay.const([-3,6,-1,9,-2,-1,-9,2,3,-9,-8,-8,8,2,-7,9,-3,7,6,7,2,7,-1,9,6,-1,-6,7,-6,-9,7,10,-4,3,-2,-8], dtype = "uint64")#candidate|6921|(36,)|const|uint64
var_6922 = relay.var("var_6922", dtype = "int32", shape = (126, 1))#candidate|6922|(126, 1)|var|int32
call_6918 = relay.TupleGetItem(func_3360_call(relay.reshape(const_6919.astype('bool'), [2, 9, 13]), relay.reshape(const_6920.astype('uint8'), [140,]), relay.reshape(const_6921.astype('uint64'), [36,]), relay.reshape(var_6922.astype('int32'), [126,]), ), 5)
call_6923 = relay.TupleGetItem(func_3366_call(relay.reshape(const_6919.astype('bool'), [2, 9, 13]), relay.reshape(const_6920.astype('uint8'), [140,]), relay.reshape(const_6921.astype('uint64'), [36,]), relay.reshape(var_6922.astype('int32'), [126,]), ), 5)
output = relay.Tuple([call_6903,call_6918,const_6919,const_6920,const_6921,var_6922,])
output2 = relay.Tuple([call_6904,call_6923,const_6919,const_6920,const_6921,var_6922,])
func_6936 = relay.Function([var_6922,], output)
mod['func_6936'] = func_6936
mod = relay.transform.InferType()(mod)
var_6937 = relay.var("var_6937", dtype = "int32", shape = (126, 1))#candidate|6937|(126, 1)|var|int32
output = func_6936(var_6937)
func_6938 = relay.Function([var_6937], output)
mutated_mod['func_6938'] = func_6938
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2212_call = mod.get_global_var('func_2212')
func_2214_call = mutated_mod.get_global_var('func_2214')
call_6985 = func_2212_call()
call_6986 = func_2212_call()
func_4702_call = mod.get_global_var('func_4702')
func_4706_call = mutated_mod.get_global_var('func_4706')
const_7004 = relay.const([-6.532495,-5.744772,8.962260,1.791238,-0.848957,-2.153611,6.137418,-0.269173,6.809505,-4.902120,-8.950163,-6.327337,0.866630,-2.712576,0.027911,-7.088440,1.022866,-2.806165,-0.459164,6.400254,-2.327323,1.973437,-8.044324,-4.932438,-2.070908,7.859645,-1.732218,0.581763,3.563300,9.965760,5.896851,-7.407507,-3.811571,9.286852,-2.225560,9.153480,-9.826113,8.839555,-7.504729,-1.824410,-4.372204,-2.256058,-9.375797,-8.933340,2.808383,-1.767478,-9.577884,-2.809892,-4.542238,2.618841,-7.832023,5.028780,-6.506724,7.256129,-6.247821,9.680137,7.076936,9.968063,8.578296,-7.563436,6.477925,0.877541,8.371186,-7.103259,3.038643,0.913124,-3.705937,6.669919,7.413497,-8.889086,-3.153392,-7.355040,3.857436,4.331954,3.214228,1.518044,0.435881,-4.558243,-4.641395,-4.376049,4.680668,-7.770552,-3.208838,-2.452893,-8.396228,6.145166,-3.172265,7.658948,1.319486,-7.328927,-1.382989,-7.660426,1.698654,-2.322694,1.968461,4.846848,-6.434320,0.567576,4.264474,-0.261441,-3.173646,3.232479,6.268303,-0.413026,3.707582,-5.818892,-6.105586,7.436315,5.853551,-4.571154,-6.646727,6.494531,9.779651,6.453564,-9.391574,-2.088939,2.530742,6.093882,-5.450429,-0.542434,3.038234,5.444309,0.922733,0.531700,3.814726,8.528974,2.049088,-8.843395,6.740168,-8.085131,-0.262537,-8.091778,-6.907048,-3.945045,4.389905,-7.560976,4.801734,5.423072,3.015041,-7.677046,-3.178347,-2.438279,-1.201398,-4.101907,4.449224,-3.604605,3.749440,0.038082,-3.205817,0.799361,-5.319718,-9.577250,7.739449,-5.669328,-0.823995,4.518715,4.488275,2.030854,3.922959,3.809158,-7.931318,-8.855921,4.928688,5.062370,2.714748,2.010499,-6.572740,-9.007266,2.026242,-5.752056,7.204131,-5.864514,-3.935916,-7.781406,3.664238,-6.708344,0.758347,-1.218691,-5.554129,4.072454,-9.752524,-6.895592,-0.446403,-2.488986,9.965791,-3.052743,3.933694,5.012017,-8.789480,8.967787,-4.647579,1.980584,-8.910738,-0.160420,5.526495,-3.644705,-8.528539,-5.591735,4.706257,7.940658,-9.721742,8.747571,-6.685575,7.864289,2.745982,7.911684,-2.566017,0.720465,-7.773621,3.267178,9.959817,3.658696,-1.369654,1.518288,-1.638475,9.203269,-9.107947,-4.587902,9.953775,5.281528,-0.035556,-0.106556,6.837371,7.581225,0.702136,0.778748,6.872500,6.710183,-5.972428,9.111164,4.633840,4.987595,-7.275300,-5.973131,2.613039,-2.534468,-7.302417,-3.012112,-4.907773,1.424512,3.304741,3.620157,0.522692,-7.812722,6.038214,4.541886,-8.241385,-2.908189,-7.584333,4.724343,-7.570896,-4.211192,-3.240625,-9.498745,-2.586953,2.917125,-7.298837,-8.524336,4.318515,5.949916,7.286179,6.060644,-7.439468,-3.011676,-7.197941,-0.174853,2.124915,-4.713421,-2.961698,-0.324603,-5.280027,-0.404692,-2.473843,8.738181,2.926507,-3.115117,4.715475,3.592751,7.943618,-3.836085,1.948239,-8.658533,7.900633,-7.377179,2.548432,7.028377,-3.927390,-1.759672,-7.040584,-5.240966,6.743001,-2.177493,-2.823962,-5.907132,7.758010,-2.605535,8.076298,4.652389,2.190999,-9.962508,7.851777,-5.097778,8.535284,-8.931311,-4.958412,-2.720889,-0.825790,-8.402681,-5.904415,-7.372549,-7.348162,-6.993858,-7.462555,-2.410321,8.925068,-9.244433,-8.743821,0.943758,-8.779311,-4.486492,-0.496939,-4.392950,0.167999,-1.265424,5.114615,-7.884693,9.185054,1.373529,-2.724105,7.366706,7.917694,-0.345771,-9.259593,8.869520,-9.433399,-4.372358,-8.348198,0.435814,3.203334,5.441425,-3.128454,-6.287862,-5.727377,4.917320,-5.856175,4.218553,2.020863,8.378193,7.311065,-2.636709,-7.414250,-8.875150,1.550892,0.379568,6.815381,0.958587,-4.133006,2.549194,8.370091,1.296643,6.879568,8.332398,1.474910,4.037052,-1.459261,-3.773237,-7.547159,7.531758,-4.472069,-4.458721,-9.647937,9.633705,-4.102830,8.154198,-2.375887,1.997076,2.878293,-3.948152,7.764079,7.491794,8.202874,6.698645,0.650289,3.815628,6.133199,2.452010,9.975508,-3.885526,-2.861958,6.652592,-4.282468,-2.879897,-5.595738,-4.010299,-1.607567,4.940887,0.681574,2.022982,5.868022,-5.568398,0.135111,-8.448748,7.559503,-2.982704,1.724464,-5.679189,-8.695369,1.634617,4.752645,-2.281112,-0.880569,9.051456,-1.590578,-3.547087,9.178083,-0.285907,-2.046352,6.311153,5.436215,2.543215,4.998855,7.117457,6.286198,-3.522947,-4.667126,-0.867607,-2.505057,5.989360,9.493169,7.054635,-4.862188,1.110477,-3.836264,-7.053300,-2.856187,-8.943084,5.101609,8.476022,4.763457,5.797491,-8.614658,-1.583056,1.577500,-5.119059,1.561326,7.605505,8.516087,-3.360736,0.471913,-0.894489,9.043463,-5.474556,-6.132526,1.524850,3.162028,6.515981,-9.571008,2.104519,4.146349,-2.229388,5.745943,0.766686,-5.309224,-3.535195,-3.265503,2.811747,-9.980574,4.928387,2.800137,-0.726180,5.181570,1.688348,8.844526,-9.576919,-6.410491,5.587835,-4.207221,-5.892414,-1.147149,9.044963,4.927565,-4.949016,-0.919403,-0.468341,-8.926883,-4.753699,4.977918,-5.144071,-8.757512,2.611946,2.555615,-3.422736,1.066613,8.387836,-1.966022,8.651645,2.680353,6.869705,3.562036,-8.380424,-2.599773,1.796054,-8.977955,-9.724427,-1.147289,5.284650,-6.658732,-2.841268,-2.891877,1.855759,-7.274468,9.254169,4.121725,0.818832,-1.940756,-2.825910,-6.151292,-9.092120,5.123890,-1.110405,0.115161,-6.062748,1.819312,2.605276,-5.559000,-9.920560,8.276107,-9.163592,-0.594693,3.574294,8.357064,6.326540,-2.228471,-5.896549,-4.243673,4.998565,-3.659340,3.204966,-9.334514,-5.506812,-5.254698,7.143478,-5.080355,-1.033014,2.055435,8.006489,5.405861,8.885441,4.906742,-6.907998,-2.450207,7.617917,0.588383,-6.139322,8.565704,-6.899933,-9.644569,-2.755106,3.083587,8.755366,-1.157664,-0.073799,-1.013717,7.004950,8.351542,2.646854,-3.658726,2.246727,-2.165025,9.735984,-8.368194,9.510414,-4.403219,6.249775,-7.863026,-8.617000,5.863342,-5.876117,-2.172636,1.782316,4.621554,6.816164,5.765369,1.721195,2.512678,-0.987737,-6.492477,-3.245867,5.858662,3.648106,-2.521310,-9.067348,-9.738319,5.419179,9.828406,-7.243618,-3.190644,-1.342000,-1.211300,5.083858,-1.046440,7.502522,8.474528,6.653488,0.906516,-1.473507,9.488390,-6.187304,3.516706,-3.998729,-0.208697,-0.420027,5.131942,9.013647,-7.705558,0.834407,-4.641827,-7.843520,-5.750960,-0.482669,-8.006836,0.909296,9.895381,8.324634,-9.239426,2.201791,-7.095126,4.638097,-3.882683,-3.903145,3.728460,-0.899485,-8.916813,6.568065,-8.366525,3.856612,-7.594443,-8.805110,-8.781447,-7.179933,-6.313649,9.224954,5.547763,-3.943378,2.550592,0.649409,-8.579931,-2.924440,-7.713446,7.274430,0.168148,8.408830,0.300061,-2.161951,6.599485,-2.323670,-7.053141,-5.462324,-6.901845,-5.478443,8.501452,-0.559255,1.974892,7.594151,-8.491623,-1.538805,4.025390,8.690651,-9.533637,-0.527899,2.336863,9.965797,-9.875737,9.460730,-3.778187,4.386326,1.024998,5.922558,-0.180537,-5.656227,3.081632,4.087078,-9.119671,0.028916,-3.022035,-4.800351,5.824132,3.813102,-2.842469,-2.019236,-1.119875,-8.423103,-2.327344,-1.638822,-6.610548,6.151542,-0.095038,-3.530537,-1.577772,9.753482,4.969185,-9.497972,5.849637,4.527053,-2.594104,-0.704386,8.668250,6.135942,-2.350315,-7.476106,-9.700755,-2.082639,-5.584862,-8.095511,-6.744338,0.235209,1.196512,-1.896287,-7.171897,-4.106120,-7.819169,0.116087,-1.977130,1.289841,9.181376,8.945946,6.078259,-8.132687,0.029727,-7.978938,-3.070960,3.851409,3.240041,-1.270410,8.797069,3.917031,2.131800,6.167785,5.670392,-1.765371,9.581851,-9.661633,1.129962,-8.855788,8.022115,-0.690087,5.067740,-1.388860,-2.700827,-4.951097,4.078105,9.546959,-1.982360,-5.906426,9.474521,-7.407944], dtype = "float64")#candidate|7004|(756,)|const|float64
call_7003 = func_4702_call(relay.reshape(const_7004.astype('float64'), [14, 6, 9]), relay.reshape(const_7004.astype('float64'), [14, 6, 9]), )
call_7005 = func_4702_call(relay.reshape(const_7004.astype('float64'), [14, 6, 9]), relay.reshape(const_7004.astype('float64'), [14, 6, 9]), )
func_703_call = mod.get_global_var('func_703')
func_705_call = mutated_mod.get_global_var('func_705')
var_7009 = relay.var("var_7009", dtype = "float64", shape = (12, 50))#candidate|7009|(12, 50)|var|float64
call_7008 = relay.TupleGetItem(func_703_call(relay.reshape(var_7009.astype('float64'), [15, 4, 10])), 0)
call_7010 = relay.TupleGetItem(func_705_call(relay.reshape(var_7009.astype('float64'), [15, 4, 10])), 0)
output = relay.Tuple([call_6985,call_7003,const_7004,call_7008,var_7009,])
output2 = relay.Tuple([call_6986,call_7005,const_7004,call_7010,var_7009,])
func_7020 = relay.Function([var_7009,], output)
mod['func_7020'] = func_7020
mod = relay.transform.InferType()(mod)
mutated_mod['func_7020'] = func_7020
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7021 = relay.var("var_7021", dtype = "float64", shape = (12, 50))#candidate|7021|(12, 50)|var|float64
func_7020_call = mutated_mod.get_global_var('func_7020')
call_7022 = func_7020_call(var_7021)
output = call_7022
func_7023 = relay.Function([var_7021], output)
mutated_mod['func_7023'] = func_7023
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4355_call = mod.get_global_var('func_4355')
func_4357_call = mutated_mod.get_global_var('func_4357')
call_7038 = relay.TupleGetItem(func_4355_call(), 0)
call_7039 = relay.TupleGetItem(func_4357_call(), 0)
func_3661_call = mod.get_global_var('func_3661')
func_3667_call = mutated_mod.get_global_var('func_3667')
var_7042 = relay.var("var_7042", dtype = "bool", shape = (234,))#candidate|7042|(234,)|var|bool
const_7043 = relay.const([-8,6,1,8,-8,10,6,6,-7,-9,2,-8,5,-7,3,-3,-6,4,-9,-5,-3,2,2,-3,-3,-1,-10,-6,-7,10,-10,10,-3,3,9,10,6,1,-2,-8,-9,-7,-8,-3,-3,-4,7,-9,8,-2,-2,9,6,8,6,-2,5,-3,-2,9,-1,-10,-4,-9,-3,-1,5,4,2,1,8,-5,3,-9,6,4,-8,6,-5,8,7,-4,-1,-6,-2,3,10,-6,-5,2,10,9,-2,4,9,7,3,-10,4,7,3,-8,7,-10,7,-4,-9,9,-7,9,4,3,9,-2,-9,9,-9,9,-10,-6,2,-8,-2,-2,-9,-6,9,2,5,3,3,10,-10,7,7,-9,-5,9,5,8], dtype = "uint8")#candidate|7043|(140,)|const|uint8
var_7044 = relay.var("var_7044", dtype = "uint64", shape = (1, 36))#candidate|7044|(1, 36)|var|uint64
var_7045 = relay.var("var_7045", dtype = "int32", shape = (126, 1))#candidate|7045|(126, 1)|var|int32
call_7041 = relay.TupleGetItem(func_3661_call(relay.reshape(var_7042.astype('bool'), [234,]), relay.reshape(const_7043.astype('uint8'), [140,]), relay.reshape(var_7044.astype('uint64'), [36,]), relay.reshape(var_7045.astype('int32'), [126,]), ), 3)
call_7046 = relay.TupleGetItem(func_3667_call(relay.reshape(var_7042.astype('bool'), [234,]), relay.reshape(const_7043.astype('uint8'), [140,]), relay.reshape(var_7044.astype('uint64'), [36,]), relay.reshape(var_7045.astype('int32'), [126,]), ), 3)
uop_7048 = relay.sqrt(var_7042.astype('float64')) # shape=(234,)
output = relay.Tuple([call_7038,call_7041,const_7043,var_7044,var_7045,uop_7048,])
output2 = relay.Tuple([call_7039,call_7046,const_7043,var_7044,var_7045,uop_7048,])
func_7050 = relay.Function([var_7042,var_7044,var_7045,], output)
mod['func_7050'] = func_7050
mod = relay.transform.InferType()(mod)
mutated_mod['func_7050'] = func_7050
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7050_call = mutated_mod.get_global_var('func_7050')
var_7052 = relay.var("var_7052", dtype = "bool", shape = (234,))#candidate|7052|(234,)|var|bool
var_7053 = relay.var("var_7053", dtype = "uint64", shape = (1, 36))#candidate|7053|(1, 36)|var|uint64
var_7054 = relay.var("var_7054", dtype = "int32", shape = (126, 1))#candidate|7054|(126, 1)|var|int32
call_7051 = func_7050_call(var_7052,var_7053,var_7054,)
output = call_7051
func_7055 = relay.Function([var_7052,var_7053,var_7054,], output)
mutated_mod['func_7055'] = func_7055
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2947_call = mod.get_global_var('func_2947')
func_2949_call = mutated_mod.get_global_var('func_2949')
call_7102 = relay.TupleGetItem(func_2947_call(), 0)
call_7103 = relay.TupleGetItem(func_2949_call(), 0)
func_3538_call = mod.get_global_var('func_3538')
func_3539_call = mutated_mod.get_global_var('func_3539')
call_7110 = func_3538_call()
call_7111 = func_3538_call()
output = relay.Tuple([call_7102,call_7110,])
output2 = relay.Tuple([call_7103,call_7111,])
func_7118 = relay.Function([], output)
mod['func_7118'] = func_7118
mod = relay.transform.InferType()(mod)
mutated_mod['func_7118'] = func_7118
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7118_call = mutated_mod.get_global_var('func_7118')
call_7119 = func_7118_call()
output = call_7119
func_7120 = relay.Function([], output)
mutated_mod['func_7120'] = func_7120
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7163 = relay.var("var_7163", dtype = "float64", shape = (9, 13, 11))#candidate|7163|(9, 13, 11)|var|float64
var_7164 = relay.var("var_7164", dtype = "float64", shape = (9, 13, 11))#candidate|7164|(9, 13, 11)|var|float64
bop_7165 = relay.power(var_7163.astype('float64'), relay.reshape(var_7164.astype('float64'), relay.shape_of(var_7163))) # shape=(9, 13, 11)
uop_7174 = relay.tan(var_7164.astype('float32')) # shape=(9, 13, 11)
func_3214_call = mod.get_global_var('func_3214')
func_3215_call = mutated_mod.get_global_var('func_3215')
call_7176 = func_3214_call()
call_7177 = func_3214_call()
uop_7180 = relay.asinh(var_7163.astype('float32')) # shape=(9, 13, 11)
output = relay.Tuple([bop_7165,uop_7174,call_7176,uop_7180,])
output2 = relay.Tuple([bop_7165,uop_7174,call_7177,uop_7180,])
func_7201 = relay.Function([var_7163,var_7164,], output)
mod['func_7201'] = func_7201
mod = relay.transform.InferType()(mod)
var_7202 = relay.var("var_7202", dtype = "float64", shape = (9, 13, 11))#candidate|7202|(9, 13, 11)|var|float64
var_7203 = relay.var("var_7203", dtype = "float64", shape = (9, 13, 11))#candidate|7203|(9, 13, 11)|var|float64
output = func_7201(var_7202,var_7203,)
func_7204 = relay.Function([var_7202,var_7203,], output)
mutated_mod['func_7204'] = func_7204
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4961_call = mod.get_global_var('func_4961')
func_4963_call = mutated_mod.get_global_var('func_4963')
call_7268 = relay.TupleGetItem(func_4961_call(), 2)
call_7269 = relay.TupleGetItem(func_4963_call(), 2)
func_4961_call = mod.get_global_var('func_4961')
func_4963_call = mutated_mod.get_global_var('func_4963')
call_7270 = relay.TupleGetItem(func_4961_call(), 0)
call_7271 = relay.TupleGetItem(func_4963_call(), 0)
output = relay.Tuple([call_7268,call_7270,])
output2 = relay.Tuple([call_7269,call_7271,])
func_7273 = relay.Function([], output)
mod['func_7273'] = func_7273
mod = relay.transform.InferType()(mod)
mutated_mod['func_7273'] = func_7273
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7273_call = mutated_mod.get_global_var('func_7273')
call_7274 = func_7273_call()
output = call_7274
func_7275 = relay.Function([], output)
mutated_mod['func_7275'] = func_7275
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5017_call = mod.get_global_var('func_5017')
func_5019_call = mutated_mod.get_global_var('func_5019')
call_7365 = func_5017_call()
call_7366 = func_5017_call()
func_2324_call = mod.get_global_var('func_2324')
func_2326_call = mutated_mod.get_global_var('func_2326')
call_7368 = relay.TupleGetItem(func_2324_call(), 0)
call_7369 = relay.TupleGetItem(func_2326_call(), 0)
func_5474_call = mod.get_global_var('func_5474')
func_5477_call = mutated_mod.get_global_var('func_5477')
const_7372 = relay.const([[7.565554,-6.613182,-6.493331,-6.273440,8.811208,-9.676605,6.720562,4.912757,1.679091,-5.820672,8.166213,-3.443037,0.026927,-7.551523,4.734669,-1.645299,-8.543210,-2.493245,-5.492666,9.075775,4.112216,1.005270,8.960474,5.649700,-0.891559,-7.725857,-8.436445,-8.864072,-3.111790,-4.130875,1.828754,-4.876746,3.139897,-4.342985,-8.656716,9.860136,-8.704867,-8.539967,5.431968,-6.561168,0.881644,9.059618,5.914473,1.299301,-6.870673,-6.318903,8.394997,5.525685,2.896440,-9.724388,7.287303,0.138003,-0.999438,1.181518,2.217331,4.078745,-4.209004,1.075898,8.774549,-1.629155,-1.625051,1.762803,4.674237,-7.916629,1.474146,-2.600669,-4.253270,-3.559672,0.611481,-3.646858,3.676778,-1.516323,-9.199670,-3.739817,-4.103705,2.481757,0.518257,-6.544639,1.069385,5.700824,0.370214,5.094013,1.732226,-4.777724,5.100374,0.451355,4.324189,-3.167056,7.445391,3.972886,9.283433,-8.919121,2.395311,-3.180307,5.418188,9.579268,9.969104,-1.574508,-8.217717,-0.622530,1.513893,5.505243,0.554968,-7.290728,-0.341925,-3.185775,-1.860209,-8.553199,-5.914347,-4.363303,-1.903606,-9.960778,-7.590275,-9.892186,-8.252964,-3.204127,-0.247781,-3.934433,-2.242547,0.883368,-8.991135,-6.587006,-5.272034,-9.984862,2.791233,0.216167,3.155471,-0.368389,-3.091973,-2.118487,6.855478,8.556605,-7.556252,3.764830,-9.467632,6.056008,-7.223622,-9.984786,-1.159384,5.650464,1.643138,0.262399,0.852189,2.202381,-2.703870,-6.676503,-4.739998,-1.112947,0.085320,9.731485,-0.573805,-7.570592,3.763669,9.431993,2.236743,9.458106,3.059003,3.256471,-8.885869,9.937797,0.512846,-1.340325,6.447253,-7.500398,-9.845538,-8.306658,0.031437,-5.518848,6.590828,-2.176036,-6.194836,-6.818325,5.389537,-5.235091,-6.290259,-8.762996,9.205007,3.339876,2.126189,8.903422,-4.518244,-9.999498,-2.225094,-7.383709,7.718821,8.144896,-5.433760,0.147413,9.803571,-2.896916,0.248491,6.630255,2.784712,3.655712,2.220682,9.638980,3.232231,3.350245],[-9.206670,6.260990,-6.191621,7.159745,-9.531583,-9.985922,0.352999,1.318074,-7.818967,6.493283,-8.229068,-9.721129,-2.846826,9.592233,-3.365924,1.042588,-2.997311,-4.134284,2.770901,1.467397,-9.174363,-9.169745,-5.073322,9.162651,-7.302252,6.906831,4.714014,-3.101967,5.398165,1.245045,-3.410901,-4.119842,-6.965804,-2.430037,-5.314713,2.895351,4.345529,-3.307103,-2.308431,-7.295247,9.405879,4.616027,-8.015046,-5.119493,4.715451,1.525893,-4.994506,-3.013186,-4.730947,6.448452,-2.224666,0.565190,-7.916183,-3.222568,1.773463,0.014797,-9.348072,-4.662587,6.004695,-2.187039,-6.490856,-6.621343,3.554059,5.493848,7.890374,-3.125950,-8.673581,-3.953041,-0.872777,4.667564,1.256389,-7.063777,5.111218,-5.717877,6.794317,4.637111,-0.573098,-8.652133,-7.471562,3.230598,-9.983370,0.921228,-7.119858,9.845828,-9.469522,-7.265844,-3.934238,5.407443,5.794975,-5.204941,-5.614350,0.517865,1.782027,-8.956443,7.154341,-1.799176,-7.887668,-7.297639,0.273114,3.075445,-9.632130,4.379649,-4.837954,-2.786788,7.935889,-0.645692,-7.248300,-5.921391,1.773097,6.241938,5.417918,3.711004,-5.359961,-5.165217,2.919763,6.205123,5.618783,-5.983331,-8.423565,-2.337770,1.628376,5.697870,-1.728041,-5.245977,5.710333,-2.103077,5.343891,-8.934145,-6.368748,5.378876,-6.534004,9.986879,5.108017,8.931895,7.939231,8.460683,-6.061066,-6.616415,5.936280,-2.760443,1.849744,9.816526,-6.324374,-8.285781,-9.836482,0.343507,-6.107644,-4.046655,-4.606258,4.962029,1.486662,2.640730,-3.815024,-0.877709,-9.489674,-2.963468,-4.809166,-3.235661,7.535400,5.823968,-8.041424,-2.167346,5.543633,-9.259304,-4.563504,7.895328,8.395823,4.737098,5.725955,5.428250,-7.254423,8.174366,6.936992,-4.997820,-5.256844,-4.327975,-7.396291,4.617296,7.248832,9.561597,-8.446239,-6.903225,3.392818,0.699407,8.643834,-1.040841,-5.337828,-6.016059,5.511367,-2.042350,-2.815765,-1.075432,2.170158,4.770576,-0.157853,-8.851224,3.912909,-7.707822],[-7.473427,0.860814,-9.909620,6.711333,0.516762,-3.456975,-8.421616,-0.431118,4.162492,5.567114,2.620724,2.261992,-2.681131,-7.275493,-1.544428,-9.915369,-6.741606,1.567940,-8.875631,9.224018,-0.168533,-4.150425,-3.728055,-4.621052,-3.422820,-0.103417,-8.776265,8.016405,6.570385,-3.044203,-1.628473,-6.143977,9.226673,1.773110,-2.823159,1.676252,-6.187888,-2.977475,3.102992,-6.196265,-9.520093,8.992078,-1.468697,8.233581,-2.960985,-6.455952,3.160579,6.305671,-5.467997,-8.455469,3.788302,2.119677,4.844664,-6.922165,-2.221762,-7.218553,4.369663,8.748941,-2.543915,9.921705,1.067403,1.243734,-4.337642,1.325023,7.241555,6.141996,6.600644,-5.177588,-0.433240,0.366989,3.150310,-0.692014,0.847484,4.672002,-0.877296,-3.946656,-2.893671,-9.949175,-2.383322,6.128596,2.236890,-3.877787,7.846631,-2.417436,0.651632,0.613621,1.487240,9.299776,5.482998,3.026129,5.740123,4.977712,9.104395,-3.300519,1.179444,-8.829585,1.612169,-2.331823,1.333358,-5.015504,-4.823992,-3.308415,4.560018,1.957753,-7.738896,6.115051,-7.423346,3.447915,-4.165920,-2.787232,9.111527,4.806809,3.821738,6.964518,-2.237552,-9.018692,6.901914,-2.392203,-9.842073,-7.258490,-3.443794,4.016107,-0.854899,2.494768,-5.145268,3.158304,-3.467192,-5.766471,-5.619761,-5.007234,-1.603233,1.319202,1.044172,-0.645396,5.600137,-7.812249,-1.325071,5.396936,-0.309533,-9.559025,-1.469341,-9.177453,-0.659218,-8.523571,5.656494,2.927247,5.012594,5.292541,-2.554983,2.285679,-2.947809,-7.828167,1.766016,-4.377465,-6.463820,-5.074825,-1.381334,4.077553,-7.164775,4.767592,-5.035962,6.487946,8.962026,0.505863,-1.293410,-7.914779,-9.251305,-4.729134,-9.807823,-9.311370,5.087475,6.004488,3.456663,-4.365258,-5.835583,4.455048,-5.231558,4.599572,-0.706637,8.031208,6.433458,1.556982,-9.134950,7.596328,-9.148787,2.459242,-3.653496,2.756313,0.144697,8.235932,3.675026,0.362086,5.598412,-1.982647,2.483494,2.542307,8.654751,-4.833652],[-1.158750,-0.852737,1.084129,-1.996926,-2.846145,-2.605645,6.544696,5.489920,-8.431504,-4.789934,4.799250,3.162342,-5.530185,4.873406,-1.462055,-7.582172,6.169318,0.656951,-4.658962,7.054244,-9.157632,7.373067,8.928336,-3.480015,5.156578,-1.170991,2.103229,0.528593,-3.049937,7.649599,-3.782153,9.581503,-2.633445,5.275096,-5.303987,7.273695,-7.607707,-4.558781,-1.681383,8.733539,1.756708,-5.861088,-6.608452,-1.751209,4.188174,8.877721,9.536557,1.803719,4.306559,7.897708,0.184965,-3.586511,6.555492,-2.274693,-1.352067,6.952896,2.375392,-6.224395,4.073491,-1.733329,5.724046,-8.621271,-3.003276,-0.572459,-1.163667,2.920600,1.347908,6.992634,-6.603187,-3.405071,-4.724899,-5.406024,8.834730,3.651285,1.114663,5.125697,7.819693,-6.131709,-2.394754,0.609452,-0.382876,-5.696478,9.167086,-8.236838,6.124852,-1.365429,-3.435224,7.415342,3.633926,-8.579537,-8.326105,2.733091,2.449938,3.131684,9.142031,8.206321,7.051941,8.125516,7.584562,-9.415386,-6.244742,-2.893283,2.989424,-6.995890,-8.241813,-2.083525,1.947404,-6.925021,4.450603,-0.304663,2.285682,-6.818815,9.242125,4.909481,2.478313,-7.890033,-1.503780,-5.385599,-5.579045,-1.168536,1.825852,-3.791907,4.887035,2.205291,-2.127796,0.978458,3.902379,1.568730,7.315332,-1.944233,-9.557743,-6.899405,7.333623,5.991527,0.089148,2.553746,-4.376789,7.733349,-8.136307,-4.216553,-8.180181,-1.155687,1.318593,0.616247,-5.987757,4.635428,-8.790670,3.204864,-6.808483,6.222131,5.638870,-7.447419,-1.494645,7.582814,-6.811667,-8.288749,6.019650,7.162815,-7.452520,5.518061,-9.414222,7.550578,-3.376957,-2.524110,2.088357,-4.457752,-2.915886,-4.156490,1.366642,-5.529503,2.905261,-1.412547,8.430944,8.309566,-9.649922,2.788297,2.162489,2.141489,2.031035,-1.567272,-9.528262,1.408132,8.142860,5.866223,9.400066,0.950211,-7.001566,5.295871,1.761838,7.953412,4.704044,-7.459179,-6.191114,-1.849649,8.753622,-9.214431,-8.014258,3.535359],[-1.185727,-5.418703,-4.787392,-2.343069,2.018938,-0.383662,7.606050,9.714951,-8.492088,6.749095,8.123204,1.105860,5.784200,-2.798325,1.231220,0.348837,6.420377,-9.223160,0.881266,-9.925096,-0.653830,8.962564,6.179514,7.917921,-3.427710,-9.849485,-9.834615,0.953243,8.196083,5.388885,6.923321,-5.331251,-5.929109,-5.435728,-7.451923,4.604705,0.288274,-1.640383,0.730845,1.570332,-4.345614,1.901035,6.039947,-9.184730,0.598834,8.296475,5.612093,3.565322,-8.760616,5.780090,-9.602341,-7.413620,-5.231511,-6.028500,-7.686569,8.127803,1.586046,5.892382,4.552318,-8.054785,-3.841186,4.090624,5.510768,0.066216,-9.272415,-5.382734,2.539255,8.968676,4.113646,0.562422,3.716248,1.462864,-1.610396,3.407602,-9.815802,-2.445988,1.736594,-1.630153,-5.959397,4.392592,2.861241,5.850589,-0.045626,-3.176181,0.370233,6.100263,-3.784015,9.107281,3.525814,2.842511,-2.136042,-1.830609,8.449265,7.163336,2.046242,4.914910,-6.751541,1.067519,6.915186,3.070744,-9.183729,0.352502,9.888504,6.799856,5.251219,-5.414178,-8.412448,3.893315,-8.032728,1.027470,8.677458,-1.278055,3.440232,-6.218107,8.727576,3.071249,-0.030912,-1.485801,-2.813420,2.119197,-9.734770,5.296880,-5.830250,2.260984,7.377347,-4.335644,9.062084,6.275947,1.132739,6.013213,9.962862,-5.337504,6.285602,1.356697,-8.839883,2.978481,-5.779645,7.741694,9.718021,2.220431,6.715007,-0.683254,-1.125851,6.854036,8.137143,-8.045745,-6.872053,9.219607,-0.017795,7.177957,9.577717,6.697192,9.479495,-8.303010,2.691676,-8.471308,-0.371896,5.703712,-8.548430,-7.285611,8.979053,-8.184936,4.550811,7.220667,-0.138742,-0.651966,2.546276,6.753942,-1.601566,-3.974146,-5.505867,-6.921064,2.180032,2.406876,-1.346101,6.262856,2.342180,1.340611,8.936194,-2.022779,2.247830,8.055782,-8.582379,-3.842003,4.272080,8.338920,1.450353,-8.061283,5.856446,-9.100230,7.491074,-4.079878,4.040473,9.258607,-2.640450,-0.842635,-1.380641,5.768186]], dtype = "float32")#candidate|7372|(5, 198)|const|float32
call_7371 = relay.TupleGetItem(func_5474_call(relay.reshape(const_7372.astype('float32'), [15, 11, 6]), relay.reshape(const_7372.astype('uint8'), [15, 11, 6]), ), 2)
call_7373 = relay.TupleGetItem(func_5477_call(relay.reshape(const_7372.astype('float32'), [15, 11, 6]), relay.reshape(const_7372.astype('uint8'), [15, 11, 6]), ), 2)
output = relay.Tuple([call_7365,call_7368,call_7371,const_7372,])
output2 = relay.Tuple([call_7366,call_7369,call_7373,const_7372,])
func_7378 = relay.Function([], output)
mod['func_7378'] = func_7378
mod = relay.transform.InferType()(mod)
mutated_mod['func_7378'] = func_7378
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7378_call = mutated_mod.get_global_var('func_7378')
call_7379 = func_7378_call()
output = call_7379
func_7380 = relay.Function([], output)
mutated_mod['func_7380'] = func_7380
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7387 = relay.var("var_7387", dtype = "float64", shape = (13, 15, 7))#candidate|7387|(13, 15, 7)|var|float64
uop_7388 = relay.tan(var_7387.astype('float64')) # shape=(13, 15, 7)
output = relay.Tuple([uop_7388,])
output2 = relay.Tuple([uop_7388,])
func_7400 = relay.Function([var_7387,], output)
mod['func_7400'] = func_7400
mod = relay.transform.InferType()(mod)
var_7401 = relay.var("var_7401", dtype = "float64", shape = (13, 15, 7))#candidate|7401|(13, 15, 7)|var|float64
output = func_7400(var_7401)
func_7402 = relay.Function([var_7401], output)
mutated_mod['func_7402'] = func_7402
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7479 = relay.const([[[-7.314881,7.112975,6.623529,5.759312,7.316480,-9.663624,-0.439933,3.984934,-6.430772,0.374505,-8.654075,6.302888,-6.011048],[4.132358,-0.155602,1.701217,8.999840,1.018523,-7.754832,1.491814,4.122474,7.598402,-8.480476,8.224238,6.718695,-8.247066],[2.335203,3.752021,-2.452016,0.668351,4.624138,5.179557,6.980517,-4.119981,0.156255,3.569305,5.820309,9.547876,6.050795],[-5.099171,2.265029,-0.313496,-6.686696,-5.125916,8.444216,6.598398,-7.426576,4.603119,9.586977,-1.504516,5.139439,0.574625],[-2.376785,8.730421,-7.056854,-5.409779,-6.254887,-4.986649,-7.949796,3.917448,-2.459224,6.980675,-5.761013,-3.416857,-8.283153],[-1.879187,-3.007888,-3.701719,-7.636403,-0.003912,5.091005,5.887165,0.686390,6.831824,-6.007556,1.209510,7.348244,-0.480249],[4.511305,-0.695792,4.631259,-8.303410,-0.548489,-8.500628,-2.513296,4.213514,9.914424,6.927453,-3.665249,5.066686,5.809090],[8.683557,3.938332,-4.440135,-1.671204,-1.670391,-0.429655,4.651546,2.655250,9.527095,-1.127470,9.709380,4.651770,2.588879],[1.166706,4.923488,6.366261,-2.120860,-0.810518,-1.932015,9.357081,-3.854356,8.916572,-1.160164,7.294302,-9.239850,7.849698]],[[7.658033,-8.117435,-4.359060,6.761030,-8.788821,4.050336,5.482333,-0.384188,-4.451911,-9.249911,3.905836,4.829915,-3.628111],[3.085290,-3.490556,2.725158,-8.299534,-1.582636,2.604278,-9.211411,1.963120,-3.297153,9.582655,-8.789043,-2.171177,-3.119456],[-4.779255,-0.335228,-3.945159,4.780880,-8.990990,-7.599738,-4.870343,4.445889,4.079024,1.636397,5.394168,4.020093,-9.960298],[1.635282,3.035197,-5.737266,1.782746,-5.751188,5.170257,-7.220234,-3.583906,-8.894807,-5.296583,4.354311,5.150716,-7.766616],[-9.248659,8.796823,3.106993,-2.699201,-8.313721,-8.702023,7.451155,1.516619,-2.160975,-6.587412,-4.181332,7.274149,-6.260720],[-9.841848,6.332219,9.524629,1.769356,7.760485,8.671328,8.569786,-8.089540,6.742299,-3.280726,-7.359586,-2.404722,-9.000251],[0.024807,3.386888,-1.875360,5.671521,-5.984257,5.401324,3.430903,-8.140862,-5.119554,-1.646352,5.609620,-6.204110,-8.667278],[-3.087168,9.197870,-7.614241,-0.351201,1.713118,9.935773,6.755730,2.004152,6.982797,1.203930,0.688853,4.156521,-8.811130],[9.751174,9.197873,-0.978063,-9.635081,-3.245230,-4.414360,0.401763,3.870495,1.409107,-7.233826,8.108216,7.341261,-6.933364]],[[5.764920,6.219389,-3.708962,-5.852205,-0.184195,-2.926898,4.343362,8.542974,5.806001,4.508005,-4.346584,0.555458,4.182113],[-8.022867,7.579339,9.032679,5.007415,8.252722,9.200242,6.454955,-6.788197,-2.504403,-7.332084,9.174458,-3.350042,-0.561515],[7.397153,-0.998810,-0.500496,-9.007076,6.867264,-6.609465,-3.570581,-0.978568,-4.850645,1.516924,4.533309,-8.169180,-6.284973],[-0.266775,-1.268939,5.917258,-6.396147,-2.034516,-6.859941,5.905358,-3.070551,-4.194868,5.943033,-8.914620,-3.927160,-7.148304],[1.158727,2.148103,-1.010476,3.426479,-7.592252,6.292703,-5.782277,-8.322399,-5.320438,-5.039055,3.059556,4.940822,1.244418],[-7.239687,4.229184,-8.229913,1.671225,-2.353311,4.457695,-8.298453,-2.566242,-8.741846,0.546743,-5.447346,-8.882413,-2.529871],[9.432778,-7.501581,0.472562,7.957730,9.918949,-4.065049,2.268690,5.951503,-2.335503,4.944843,8.487359,8.567474,-8.425746],[-9.287407,-7.212958,-6.147749,-8.081020,-6.644539,-5.517417,-0.244492,8.797103,-2.595054,-2.948610,6.633572,-5.153785,5.485959],[3.771021,-9.476955,-1.515252,-4.319576,-0.677065,9.466878,-1.700943,-8.323176,4.489471,-2.185080,9.810885,7.413596,-7.475444]],[[-1.697933,4.403365,-9.099351,-9.838754,-9.634507,5.410314,4.028559,-8.498715,-0.806746,3.745090,1.160659,-8.136369,0.182402],[-7.887769,1.367983,-8.210192,6.451542,6.884954,-4.641192,4.067148,0.571648,3.566566,-4.559651,8.344286,-3.065876,3.276189],[6.835341,-2.403229,-7.645009,1.618172,1.075224,0.084130,-0.551333,7.316364,0.320107,7.628709,8.833223,8.824980,-5.266012],[4.987440,0.047311,-9.675297,-8.294780,-9.961649,-8.988293,-1.278816,6.372207,-4.318587,-3.860906,-6.903675,-8.072611,-1.649820],[-3.762168,5.270344,-3.108502,-4.865412,-0.539764,-9.095378,3.477751,8.137087,4.120862,6.674050,9.258490,-0.140502,5.829125],[0.489460,-4.367841,-6.384900,-6.163553,-6.098136,-1.127676,-8.198080,1.243253,9.108100,7.814511,-3.283825,-6.693051,0.512551],[-3.515381,8.268657,-5.695559,6.561933,8.818118,-6.815007,-6.096895,-3.914718,2.660051,5.686419,-2.541450,2.907338,1.026992],[-0.287000,4.327450,8.105382,7.259487,-3.334356,-9.024352,-2.578715,3.467206,5.417782,0.260680,-6.981218,-3.011214,-6.124679],[-7.611716,8.361615,1.711561,4.520287,9.035229,-7.552094,1.548349,8.008366,4.648419,0.297429,-7.715588,-0.089997,4.809678]],[[-2.118510,-9.753087,-5.877938,-2.811984,-4.175590,8.659062,-5.538290,-6.488956,0.471751,3.025876,7.651418,-2.550871,2.248755],[7.848321,8.312326,-4.001404,9.547386,-5.827758,7.341569,5.103793,-9.838137,6.229378,2.364845,-5.273892,-1.781321,0.506532],[-3.078222,-6.034505,-3.604192,6.068435,-6.653977,9.899247,-4.840903,9.559614,-7.080346,6.219328,7.681457,-8.700965,-6.682578],[9.577196,-0.816525,5.602198,1.325154,8.273586,9.365103,8.601260,-3.297984,2.576868,-9.884500,9.940554,2.821388,2.318260],[6.540795,-1.457495,-7.702867,-9.317403,-1.918850,4.563364,-7.991059,-5.338235,2.544151,4.915690,-5.664143,-4.287818,-3.997875],[-7.374619,-8.791995,-4.724429,8.662948,-2.521947,2.641651,-5.663722,-0.628693,9.291852,-3.781135,-1.296977,2.891103,-0.103895],[8.341995,-5.897726,-6.962420,5.283342,-9.323220,-2.185666,-4.703486,-0.492928,-0.322729,-5.769693,-4.648268,3.684319,9.180782],[1.228065,3.005197,-2.299363,-0.369555,-2.207368,0.520135,-0.561044,-5.970188,6.893396,6.738588,-0.019132,7.847076,-5.967021],[-4.147132,-7.885194,6.586855,-3.345151,8.756080,5.810485,7.741931,-9.780348,-7.801332,-4.983574,-1.306053,1.110169,1.276499]],[[1.371699,-5.491500,7.205712,9.970559,-8.459595,7.775508,8.286848,-3.994108,-9.650747,2.110010,-7.323629,6.513476,-1.415324],[9.577127,5.349473,9.536537,1.584338,-1.425751,-9.820013,-5.898733,5.314581,3.018225,1.263492,1.579959,1.997979,-0.419641],[-5.118262,-9.499904,4.407393,7.889498,1.677255,7.683544,-8.623075,2.914142,6.838054,-4.094254,4.478076,-6.212426,2.727414],[-5.449319,-2.143223,-7.503660,4.379301,5.837153,-0.582073,0.740898,9.178600,-5.048667,7.216705,-7.501380,-2.482808,8.111750],[-0.195162,-1.447308,9.579824,-5.734907,1.526190,8.694680,3.952477,-8.700198,5.063257,6.257613,-4.709636,-1.539515,4.845559],[8.089939,5.247931,0.720930,-7.832528,9.276845,7.580599,2.218976,2.583281,6.401451,5.521686,-9.960076,3.202950,3.798126],[-3.418262,7.958158,-5.867231,5.219621,0.494584,0.183428,-2.631533,-3.133098,-2.945805,-6.181999,-8.653713,-2.890697,1.374254],[-7.057072,9.714884,7.710584,3.969983,4.175607,3.001958,-5.070722,-7.531685,-8.053134,-2.032390,-7.871791,-7.866716,-0.693539],[-9.533033,-8.567510,-0.423326,-1.638817,-3.153381,7.702119,5.069810,3.580404,7.186733,4.063850,8.168293,-5.825791,-8.389669]],[[-2.295633,8.788085,1.194517,5.472908,-9.527510,-7.738402,3.928561,-9.586962,2.879707,-5.048955,-3.363574,-0.557956,0.861933],[7.646724,3.086931,-9.691017,-8.146664,0.170620,2.446328,3.629263,-0.869893,-0.758407,-7.507656,-7.782110,-9.203908,-0.644868],[-2.981794,4.195695,-4.333214,7.108026,-7.715215,3.049098,3.242711,1.287959,7.811055,-0.962357,-1.979995,-4.471393,3.272587],[-2.261271,5.411000,-9.548126,4.281090,1.806218,-1.230670,-5.571272,-0.002963,3.719187,-3.327950,-1.587889,7.382477,3.141908],[6.949710,-1.150348,-7.258221,4.641431,8.677389,0.297739,4.478859,-2.270275,8.781931,-5.195129,-8.697964,2.335499,-1.234845],[8.067416,3.947458,-3.605501,-5.369182,2.327626,5.041083,-7.646419,6.587922,-9.280914,-8.732656,-6.171111,5.767209,7.115217],[3.093904,-2.225359,-1.282854,5.292147,-8.643661,-9.496398,9.435218,1.576037,-4.919855,7.768821,6.213546,-4.865542,8.512317],[2.905840,-1.691565,-8.673996,6.549557,7.093747,-2.944045,5.963020,-5.904306,0.720178,-7.008689,3.262033,-6.404726,-9.884667],[-0.309917,6.079248,6.848365,-7.833651,5.109807,7.211776,3.689744,-7.979337,-1.361537,-6.992882,-4.171423,-6.829031,-5.530889]],[[2.401300,-8.168109,-5.275606,7.200964,-2.190889,-5.297143,-6.047676,-0.394704,-8.681781,-3.055037,8.721487,3.507529,-4.792640],[-5.511250,-1.491542,-6.816723,2.686573,5.856334,5.029129,-0.484667,0.273847,-9.158880,-6.446483,-3.924060,-9.731909,-9.051420],[3.291813,4.536106,8.582201,-2.224790,-5.978389,9.943495,1.547180,6.827810,7.284181,0.420629,-5.923200,-1.458065,-1.164292],[4.377020,-0.474683,-2.730995,9.442144,4.189559,3.948354,-2.894427,-7.139745,-2.210943,-4.746102,-7.305505,7.811193,5.504341],[9.845500,-6.699406,-0.857890,-7.602229,3.643069,-8.670839,-9.469028,1.273505,6.278818,8.587030,-4.495775,0.802545,1.666118],[-4.706533,2.904617,-0.094755,-4.916374,-8.121501,-9.128102,8.151523,-9.831101,9.834199,5.225741,-3.872182,-1.204534,-6.395893],[4.964053,-9.596341,6.486451,7.075831,-8.498550,4.954706,6.239663,2.781641,-3.476254,4.781483,-9.450804,5.736278,-2.397214],[-6.475638,1.343850,9.702904,-5.905145,2.840351,-3.442569,3.544561,-5.102432,6.017275,-1.023096,3.064590,4.435315,7.745063],[5.323679,9.123178,1.254819,8.834391,-9.461368,4.505828,-0.788334,-6.784046,-9.262733,6.637826,-5.516752,-4.390358,3.866980]],[[4.167043,-4.906645,-9.812428,6.878052,4.280105,0.882171,2.576408,8.614735,-7.285977,6.378756,0.877195,-4.753193,-9.475069],[2.595216,-5.603935,0.539976,-2.255960,-6.948061,4.321819,-8.528502,-2.562176,0.018048,-6.394086,4.182553,-6.569653,9.068474],[-0.273742,-3.932021,5.904597,5.422404,-8.107684,1.281055,-3.776527,5.518328,-7.893837,1.908663,8.819411,-4.190365,4.787284],[1.960612,4.299941,8.788171,-6.185368,-1.767301,-5.518360,5.949279,-2.423628,0.988691,4.769639,3.397746,-7.895922,-8.339474],[6.026803,9.163173,-3.354176,4.270151,-3.806164,3.714751,-5.809491,-8.600796,9.615621,-3.793828,-5.639081,0.561555,-1.975188],[9.760508,6.621864,1.315293,4.023709,2.435064,4.983506,9.475058,-1.831934,-8.173479,-8.675262,1.024216,0.001991,-1.753984],[3.327812,7.051623,-2.137382,-2.155782,-4.461143,-2.478231,3.607734,-1.622175,-5.029569,-6.532541,-5.540610,-2.586876,0.300112],[1.793394,7.517275,-0.680242,2.500213,-7.836676,5.288830,3.491008,-6.154815,8.727129,7.652378,-7.601832,2.814064,-4.769162],[-5.508446,-2.932673,-5.498150,-3.998439,5.834955,-0.388298,-5.688771,-5.288026,-4.305780,5.291473,-1.187409,-2.709909,-4.549055]],[[2.180356,5.707857,-2.713858,-1.344479,4.124842,-1.367851,-4.441612,-0.536187,-8.773745,-9.567482,-2.107261,-8.103633,1.040665],[-6.495985,-9.302306,2.840114,-1.218593,-3.216227,-0.898324,-9.726327,7.813530,5.428869,-0.018817,1.339589,-7.408046,-3.821275],[-4.469185,-3.597325,5.552643,3.077723,-5.629725,9.648867,7.101731,0.464346,6.660836,5.627396,-3.001559,-8.224588,-3.824652],[3.073219,0.434704,-8.538074,-8.750445,-3.573498,4.646910,1.491859,-2.749249,3.274791,-7.319289,9.184270,-1.826816,2.230492],[7.156810,2.784049,1.325218,-2.205367,-0.120639,-9.571533,4.385641,-1.326679,-3.343790,-9.452073,2.673553,-2.395293,-5.858334],[2.807939,-8.226054,5.545529,-0.502603,1.511393,4.052677,2.598192,-7.829173,-0.705165,-9.951816,5.169849,5.637441,0.188990],[5.700400,-7.519724,4.395298,-5.257783,-0.202749,6.081966,-8.386976,-7.253375,-9.744321,-7.385837,6.469994,-2.252742,1.403973],[-4.074768,-8.600657,1.041772,9.848129,3.019554,2.058210,-8.634890,-1.664524,9.926684,5.040030,-0.877318,5.185233,-5.856441],[-9.661429,-6.734764,-1.559799,-4.818257,-6.146923,-9.563288,8.059385,-6.834768,2.031550,7.636663,-7.728700,4.199965,-4.750033]]], dtype = "float32")#candidate|7479|(10, 9, 13)|const|float32
var_7480 = relay.var("var_7480", dtype = "float32", shape = (10, 9, 13))#candidate|7480|(10, 9, 13)|var|float32
bop_7481 = relay.floor_divide(const_7479.astype('float32'), relay.reshape(var_7480.astype('float32'), relay.shape_of(const_7479))) # shape=(10, 9, 13)
output = bop_7481
output2 = bop_7481
F = relay.Function([var_7480,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_7480,], output2)
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
