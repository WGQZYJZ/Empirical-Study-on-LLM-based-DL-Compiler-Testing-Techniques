import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_77 = relay.var("var_77", dtype = "float64", shape = (9, 15, 1))#candidate|77|(9, 15, 1)|var|float64
uop_78 = relay.cos(var_77.astype('float64')) # shape=(9, 15, 1)
output = uop_78
output2 = uop_78
func_114 = relay.Function([var_77,], output)
mod['func_114'] = func_114
mod = relay.transform.InferType()(mod)
mutated_mod['func_114'] = func_114
mutated_mod = relay.transform.InferType()(mutated_mod)
var_115 = relay.var("var_115", dtype = "float64", shape = (9, 15, 1))#candidate|115|(9, 15, 1)|var|float64
func_114_call = mutated_mod.get_global_var('func_114')
call_116 = func_114_call(var_115)
output = call_116
func_117 = relay.Function([var_115], output)
mutated_mod['func_117'] = func_117
mutated_mod = relay.transform.InferType()(mutated_mod)
const_127 = relay.const([[[False,True,False,False,True,True,True,True],[False,False,False,False,True,True,False,False],[False,False,True,False,True,False,False,True],[False,True,False,True,False,True,False,False],[False,False,True,True,True,False,True,True],[False,True,True,False,True,True,False,True],[True,False,True,True,False,True,False,False]],[[True,False,True,True,False,True,True,False],[True,False,False,False,True,True,True,True],[False,True,True,True,False,False,False,False],[False,True,True,False,True,True,False,False],[True,True,True,True,True,False,False,False],[True,False,True,False,True,False,True,True],[True,True,True,False,True,True,False,True]],[[True,True,True,False,False,True,False,True],[False,True,True,True,True,True,False,False],[True,True,False,False,True,False,True,True],[True,False,True,False,False,True,True,True],[False,False,True,False,True,True,True,True],[False,False,True,True,True,True,False,False],[False,False,False,True,False,False,False,True]],[[False,True,True,False,False,False,True,False],[False,False,False,True,True,False,True,True],[False,False,True,False,True,True,False,True],[True,True,False,False,True,True,True,True],[False,True,False,True,True,True,True,False],[False,False,True,True,False,False,True,False],[False,False,False,True,True,True,False,False]],[[False,True,False,True,False,False,False,False],[True,False,True,False,False,True,False,False],[True,False,True,True,False,False,True,True],[False,False,False,True,True,True,False,True],[False,False,False,False,False,False,False,True],[True,False,False,True,True,False,True,False],[False,False,True,True,True,False,False,True]],[[False,False,True,True,True,True,False,True],[True,False,True,False,True,False,True,False],[False,True,True,True,False,False,True,False],[False,False,True,True,False,True,True,True],[False,False,False,True,True,True,True,False],[True,False,False,False,False,False,False,False],[True,True,True,True,True,False,False,False]],[[False,True,True,True,True,False,False,True],[False,False,False,True,True,True,False,True],[False,False,True,False,False,False,True,False],[True,False,True,True,True,True,True,True],[True,False,False,False,True,False,True,True],[True,True,True,False,True,True,True,True],[True,True,True,False,True,False,False,False]],[[True,True,True,False,True,False,True,False],[True,False,False,False,False,True,True,True],[False,False,False,True,True,True,False,True],[False,False,True,True,False,True,False,True],[False,True,True,True,False,True,True,True],[True,True,True,True,False,False,True,True],[True,True,False,False,False,True,True,True]],[[True,False,False,True,True,False,True,False],[False,False,True,False,True,True,True,False],[False,False,False,True,False,True,False,True],[False,False,False,False,True,True,True,False],[False,False,False,True,False,True,True,False],[True,True,False,True,False,True,True,False],[True,True,True,False,False,True,True,False]],[[False,True,True,True,True,False,False,True],[False,False,False,True,True,False,True,False],[True,False,True,True,True,True,True,True],[False,True,True,True,False,False,True,False],[False,False,False,True,True,False,False,True],[False,False,False,True,False,False,True,True],[False,True,False,True,False,False,False,False]],[[True,True,True,True,False,True,False,False],[True,False,True,False,False,True,False,False],[True,False,True,False,False,False,True,False],[True,False,False,True,False,False,False,True],[False,True,False,False,False,False,False,False],[False,True,False,False,False,False,False,True],[True,True,True,True,False,True,False,True]],[[True,False,True,True,False,True,False,False],[False,False,False,True,True,False,True,True],[True,True,False,True,False,False,True,True],[False,False,False,False,True,False,True,False],[False,False,True,True,True,True,True,False],[False,False,True,True,False,False,False,False],[True,False,True,True,True,False,False,True]],[[True,True,True,False,True,False,True,False],[True,False,True,False,False,False,False,False],[False,True,True,True,True,True,True,True],[False,False,False,True,True,True,False,False],[False,True,False,True,True,True,True,False],[False,False,True,False,True,True,False,True],[True,True,False,False,False,True,True,False]],[[False,False,True,True,True,True,True,True],[False,True,False,False,True,False,False,True],[False,True,True,True,True,True,True,False],[False,True,False,False,True,False,True,True],[False,False,False,True,False,True,False,False],[False,False,False,True,False,True,False,True],[False,True,False,True,False,True,True,False]],[[True,False,True,False,False,False,True,False],[False,True,True,False,False,True,True,False],[True,True,False,False,False,False,True,True],[False,True,False,False,True,False,True,False],[False,False,False,False,False,True,False,False],[False,True,True,False,False,False,False,True],[True,False,True,False,True,False,True,True]],[[False,True,True,True,True,False,True,True],[False,True,True,False,False,True,True,False],[False,False,False,False,False,False,False,True],[True,True,True,False,False,False,True,False],[False,False,True,True,True,False,True,True],[True,False,False,True,False,True,True,False],[True,True,True,True,True,True,False,False]]], dtype = "bool")#candidate|127|(16, 7, 8)|const|bool
const_128 = relay.const([[[False,False,False,False,True,False,False,False],[True,False,True,True,True,False,False,True],[False,True,True,True,False,False,False,True],[True,True,True,False,False,True,False,False],[False,True,False,True,True,True,True,True],[True,False,False,False,True,True,True,True],[False,True,True,True,True,True,False,False]],[[True,True,False,True,True,False,True,True],[True,True,False,True,False,False,False,True],[False,False,True,True,True,True,True,False],[False,False,True,True,True,True,True,False],[True,True,True,False,True,False,True,True],[False,True,False,False,True,False,False,False],[False,True,True,False,False,False,False,False]],[[False,True,True,False,False,False,False,True],[True,False,True,True,False,False,False,False],[False,False,True,True,False,True,True,False],[False,True,False,True,True,False,True,False],[True,True,False,False,True,False,True,True],[False,True,False,True,True,False,True,True],[False,False,True,False,True,False,False,False]],[[True,True,True,True,True,False,True,True],[True,True,True,True,True,False,False,False],[True,False,True,True,False,False,False,False],[True,True,False,False,False,False,False,True],[True,True,False,True,False,True,False,True],[False,True,False,False,True,False,False,True],[False,True,False,False,True,False,False,False]],[[False,False,True,False,True,True,True,False],[True,False,True,True,True,True,False,False],[False,True,False,False,True,False,True,False],[True,True,False,False,True,True,True,True],[True,False,True,False,True,True,True,False],[True,False,True,False,False,False,False,False],[True,False,False,False,False,True,False,True]],[[False,True,False,False,False,True,True,True],[True,True,False,False,False,True,True,True],[True,False,True,True,False,False,False,True],[False,False,False,True,False,False,False,False],[True,False,False,True,True,False,True,False],[True,True,True,True,False,False,False,True],[False,True,True,True,True,True,False,False]],[[True,False,True,True,True,True,False,False],[False,False,False,True,False,True,False,True],[False,True,False,False,True,False,True,True],[False,False,False,True,True,True,True,True],[True,False,False,False,False,False,True,False],[True,True,True,True,False,True,True,False],[False,True,False,True,False,True,True,False]],[[False,True,True,True,False,True,False,False],[True,True,False,True,True,True,True,False],[False,True,False,False,False,True,False,True],[False,False,False,False,False,True,False,False],[True,False,True,True,True,False,True,False],[True,False,False,False,True,True,True,False],[False,True,False,True,False,True,False,False]],[[True,False,True,True,False,True,True,True],[True,True,False,False,True,False,True,False],[False,True,False,True,False,True,True,True],[False,False,False,False,True,False,True,False],[False,False,False,False,True,True,True,True],[False,False,True,True,False,False,True,False],[True,False,True,False,True,True,True,False]],[[True,True,False,False,True,True,False,True],[True,False,False,True,False,True,False,False],[True,True,False,True,False,True,True,True],[True,True,True,True,False,False,True,True],[True,True,True,False,True,True,False,False],[False,False,True,False,True,True,False,True],[True,False,False,True,False,False,False,True]],[[True,False,False,True,False,True,False,False],[True,True,False,False,False,False,False,False],[False,False,False,False,True,True,True,False],[True,True,True,True,True,False,True,False],[False,True,True,False,True,True,False,False],[False,True,False,True,True,False,True,False],[False,False,False,False,True,True,False,False]],[[False,False,False,False,False,True,False,False],[False,False,False,True,True,True,True,False],[False,True,True,True,False,False,True,False],[False,True,False,True,False,True,False,True],[True,False,True,True,True,True,True,True],[True,True,True,True,False,False,True,False],[False,False,False,False,False,True,False,True]],[[True,True,False,True,False,False,False,True],[False,True,False,True,True,True,True,False],[False,False,True,True,False,False,True,False],[False,True,False,True,True,True,False,False],[False,False,True,False,True,False,True,True],[True,True,True,False,False,False,True,False],[False,False,True,False,True,True,True,True]],[[False,True,False,True,False,False,True,False],[True,True,False,False,True,True,True,False],[False,False,True,False,False,False,True,False],[False,False,True,True,True,False,True,False],[True,True,True,False,False,True,False,True],[False,True,True,True,False,False,True,True],[True,False,True,True,False,False,False,True]],[[True,True,False,False,True,True,False,False],[True,False,False,True,True,True,False,True],[False,True,False,False,True,True,True,False],[False,True,False,False,True,False,True,False],[True,False,True,False,True,True,False,False],[True,True,True,False,False,True,True,False],[False,True,False,False,True,False,False,True]],[[True,False,True,False,False,True,True,True],[True,False,True,False,True,False,True,True],[True,False,True,True,False,True,True,False],[False,True,False,True,True,True,False,False],[True,False,True,False,True,False,True,False],[False,True,False,True,True,True,False,False],[False,False,True,False,True,False,False,True]]], dtype = "bool")#candidate|128|(16, 7, 8)|const|bool
bop_129 = relay.logical_or(const_127.astype('bool'), relay.reshape(const_128.astype('bool'), relay.shape_of(const_127))) # shape=(16, 7, 8)
var_140 = relay.var("var_140", dtype = "bool", shape = (16, 7, 8))#candidate|140|(16, 7, 8)|var|bool
bop_141 = relay.greater(const_128.astype('bool'), relay.reshape(var_140.astype('bool'), relay.shape_of(const_128))) # shape=(16, 7, 8)
output = relay.Tuple([bop_129,bop_141,])
output2 = relay.Tuple([bop_129,bop_141,])
func_151 = relay.Function([var_140,], output)
mod['func_151'] = func_151
mod = relay.transform.InferType()(mod)
mutated_mod['func_151'] = func_151
mutated_mod = relay.transform.InferType()(mutated_mod)
var_152 = relay.var("var_152", dtype = "bool", shape = (16, 7, 8))#candidate|152|(16, 7, 8)|var|bool
func_151_call = mutated_mod.get_global_var('func_151')
call_153 = func_151_call(var_152)
output = call_153
func_154 = relay.Function([var_152], output)
mutated_mod['func_154'] = func_154
mutated_mod = relay.transform.InferType()(mutated_mod)
var_192 = relay.var("var_192", dtype = "float32", shape = (15, 4, 3))#candidate|192|(15, 4, 3)|var|float32
var_193 = relay.var("var_193", dtype = "float32", shape = (15, 4, 3))#candidate|193|(15, 4, 3)|var|float32
bop_194 = relay.subtract(var_192.astype('float32'), relay.reshape(var_193.astype('float32'), relay.shape_of(var_192))) # shape=(15, 4, 3)
func_151_call = mod.get_global_var('func_151')
func_154_call = mutated_mod.get_global_var('func_154')
var_203 = relay.var("var_203", dtype = "bool", shape = (56, 16))#candidate|203|(56, 16)|var|bool
call_202 = relay.TupleGetItem(func_151_call(relay.reshape(var_203.astype('bool'), [16, 7, 8])), 1)
call_204 = relay.TupleGetItem(func_154_call(relay.reshape(var_203.astype('bool'), [16, 7, 8])), 1)
output = relay.Tuple([bop_194,call_202,var_203,])
output2 = relay.Tuple([bop_194,call_204,var_203,])
func_214 = relay.Function([var_192,var_193,var_203,], output)
mod['func_214'] = func_214
mod = relay.transform.InferType()(mod)
mutated_mod['func_214'] = func_214
mutated_mod = relay.transform.InferType()(mutated_mod)
func_214_call = mutated_mod.get_global_var('func_214')
var_216 = relay.var("var_216", dtype = "float32", shape = (15, 4, 3))#candidate|216|(15, 4, 3)|var|float32
var_217 = relay.var("var_217", dtype = "float32", shape = (15, 4, 3))#candidate|217|(15, 4, 3)|var|float32
var_218 = relay.var("var_218", dtype = "bool", shape = (56, 16))#candidate|218|(56, 16)|var|bool
call_215 = func_214_call(var_216,var_217,var_218,)
output = call_215
func_219 = relay.Function([var_216,var_217,var_218,], output)
mutated_mod['func_219'] = func_219
mutated_mod = relay.transform.InferType()(mutated_mod)
var_334 = relay.var("var_334", dtype = "float64", shape = (16, 15, 12))#candidate|334|(16, 15, 12)|var|float64
uop_335 = relay.sqrt(var_334.astype('float64')) # shape=(16, 15, 12)
func_214_call = mod.get_global_var('func_214')
func_219_call = mutated_mod.get_global_var('func_219')
var_341 = relay.var("var_341", dtype = "float32", shape = (180,))#candidate|341|(180,)|var|float32
const_342 = relay.const([True,True,False,True,False,True,False,False,True,False,True,True,True,False,False,False,False,False,False,True,True,True,True,False,False,True,True,False,False,False,False,False,True,True,True,True,False,True,False,True,True,True,False,False,True,False,False,True,False,False,False,False,False,False,False,False,True,True,False,False,True,True,False,False,False,True,False,False,False,False,True,True,True,True,True,False,True,True,True,True,False,True,True,False,True,True,False,True,True,False,True,False,True,True,True,True,False,True,True,False,True,False,True,False,True,False,False,False,True,True,False,True,False,True,True,False,True,True,True,False,False,False,False,True,True,True,True,True,False,False,True,True,True,False,True,False,False,True,True,True,False,True,True,True,False,False,True,True,False,False,True,False,False,False,True,True,True,False,False,False,True,True,True,False,True,True,False,True,False,True,False,True,False,True,False,True,False,True,False,False,True,False,False,True,False,True,False,True,False,False,True,True,True,True,True,False,False,True,True,False,True,True,True,True,True,True,False,True,False,True,True,True,True,True,False,True,False,False,False,False,False,False,True,True,True,False,True,True,False,False,True,True,False,True,False,True,False,True,False,True,False,True,False,True,False,True,False,False,True,False,True,False,False,False,True,True,True,True,False,True,True,False,False,True,True,False,False,True,True,False,False,True,True,True,False,True,False,False,False,True,True,True,True,True,True,True,True,False,False,True,True,True,True,True,True,False,False,True,False,True,False,False,True,True,True,True,True,True,False,True,True,True,False,False,False,True,True,True,False,True,True,True,True,False,True,False,True,True,True,True,False,True,True,True,True,True,True,False,False,True,True,True,False,True,False,False,False,True,False,False,True,True,False,False,True,True,False,False,False,True,True,False,True,True,False,False,False,True,False,False,False,True,False,False,False,False,False,False,True,False,True,False,True,True,False,True,False,False,True,False,False,True,False,True,False,False,True,False,True,True,False,True,False,False,True,False,False,False,False,False,False,True,False,False,False,True,True,False,True,False,False,True,True,True,False,True,True,True,True,True,False,False,False,False,False,False,False,True,False,True,True,False,False,True,False,True,False,True,True,False,False,False,True,True,True,False,True,False,True,False,True,False,False,False,False,True,False,True,False,False,False,True,False,False,False,True,True,True,False,True,True,False,True,False,False,False,False,True,False,False,True,False,False,False,False,False,True,False,True,True,False,True,False,False,False,False,True,True,True,False,False,False,False,True,True,False,True,True,True,False,True,True,False,True,True,False,False,False,False,True,True,False,True,True,False,True,True,False,False,True,False,True,True,False,False,False,True,False,False,False,False,True,True,False,True,False,False,True,False,False,False,True,False,True,False,False,False,False,False,True,True,False,False,False,True,False,True,False,False,True,False,False,False,False,False,True,False,False,False,True,False,True,False,False,False,True,True,True,True,True,False,False,False,False,False,True,False,True,True,True,False,True,True,True,True,False,False,False,False,True,True,True,False,True,True,False,False,False,True,True,False,True,True,False,True,False,True,False,True,False,True,False,True,False,True,True,False,True,True,True,False,False,False,False,True,True,True,False,False,False,True,False,False,True,False,True,True,True,True,False,True,False,False,False,True,True,True,True,True,False,False,True,False,False,False,False,False,True,False,False,True,True,False,True,False,False,True,True,True,False,False,False,True,False,False,False,False,False,True,True,False,False,False,True,False,False,True,False,True,True,False,True,False,False,False,True,False,True,False,True,False,False,True,True,True,False,True,True,False,False,False,False,False,False,True,True,True,False,True,False,True,False,True,False,False,False,True,True,True,True,False,True,False,False,False,True,False,True,False,False,False,False,False,False,False,False,True,True,False,True,False,False,True,True,False,True,True,True,False,True,False,True,False,False,True,True,True,True,False,True,True,False,True,True,True,False,True,False,True,False,True,True,False,False,True,False,False,False,True,False,True,True,True,False,False,False,True,True,True,True,True,False,False,False,False,True,False,True,True,False,True,True,True,True,True,False,True,True,True,False,False,False,False,True,False,False,False,True,True,True,True,False,False,True,True,False,False,True,True,True,True,True,False,True,False,False,True,False,True,False,False,True,True,False,True,True,False,True,True,False,False,False,False,False,True,True], dtype = "bool")#candidate|342|(896,)|const|bool
call_340 = relay.TupleGetItem(func_214_call(relay.reshape(var_341.astype('float32'), [15, 4, 3]), relay.reshape(var_341.astype('float32'), [15, 4, 3]), relay.reshape(const_342.astype('bool'), [56, 16]), ), 1)
call_343 = relay.TupleGetItem(func_219_call(relay.reshape(var_341.astype('float32'), [15, 4, 3]), relay.reshape(var_341.astype('float32'), [15, 4, 3]), relay.reshape(const_342.astype('bool'), [56, 16]), ), 1)
bop_346 = relay.greater_equal(uop_335.astype('bool'), relay.reshape(var_334.astype('bool'), relay.shape_of(uop_335))) # shape=(16, 15, 12)
func_151_call = mod.get_global_var('func_151')
func_154_call = mutated_mod.get_global_var('func_154')
call_357 = relay.TupleGetItem(func_151_call(relay.reshape(call_340.astype('bool'), [16, 7, 8])), 0)
call_358 = relay.TupleGetItem(func_154_call(relay.reshape(call_340.astype('bool'), [16, 7, 8])), 0)
func_214_call = mod.get_global_var('func_214')
func_219_call = mutated_mod.get_global_var('func_219')
call_363 = relay.TupleGetItem(func_214_call(relay.reshape(var_341.astype('float32'), [15, 4, 3]), relay.reshape(var_341.astype('float32'), [15, 4, 3]), relay.reshape(call_340.astype('bool'), [56, 16]), ), 0)
call_364 = relay.TupleGetItem(func_219_call(relay.reshape(var_341.astype('float32'), [15, 4, 3]), relay.reshape(var_341.astype('float32'), [15, 4, 3]), relay.reshape(call_340.astype('bool'), [56, 16]), ), 0)
output = relay.Tuple([call_340,var_341,const_342,bop_346,call_357,call_363,])
output2 = relay.Tuple([call_343,var_341,const_342,bop_346,call_358,call_364,])
func_375 = relay.Function([var_334,var_341,], output)
mod['func_375'] = func_375
mod = relay.transform.InferType()(mod)
var_376 = relay.var("var_376", dtype = "float64", shape = (16, 15, 12))#candidate|376|(16, 15, 12)|var|float64
var_377 = relay.var("var_377", dtype = "float32", shape = (180,))#candidate|377|(180,)|var|float32
output = func_375(var_376,var_377,)
func_378 = relay.Function([var_376,var_377,], output)
mutated_mod['func_378'] = func_378
mutated_mod = relay.transform.InferType()(mutated_mod)
var_425 = relay.var("var_425", dtype = "int8", shape = ())#candidate|425|()|var|int8
const_426 = relay.const([[[-8,7,5,7,-4,7,-5,5,-6,1,8,-4],[-7,5,-9,1,-5,5,6,3,-6,6,-3,-5],[4,8,9,-10,4,4,6,1,2,3,-7,7],[-9,9,2,2,-9,9,-4,-2,-4,-2,-10,2],[-10,-1,3,4,-9,-5,4,-10,-2,1,-7,4],[1,-4,10,4,-2,9,-1,9,-6,4,4,5],[2,-1,10,2,1,2,-1,3,1,1,7,-3],[-4,4,-10,3,-8,-1,-10,-2,7,4,2,3]],[[1,5,-6,2,-7,8,-9,7,7,-6,1,2],[1,7,-3,-7,6,2,-2,2,1,9,4,5],[-4,-2,10,2,-8,-5,1,5,5,1,-10,-9],[4,-2,3,-2,10,-3,-6,2,-6,-4,10,-4],[5,-2,-10,-9,-10,3,-8,-2,8,9,-10,7],[9,-3,-1,1,4,-4,-6,-7,1,2,6,10],[-7,8,-1,3,6,-6,-3,-4,4,-1,10,9],[-9,-3,-2,9,-1,1,1,1,-2,-6,-7,3]],[[-10,-2,-2,4,-1,-10,-1,6,-7,-5,1,-8],[4,-9,6,-2,6,-9,-4,-2,3,10,3,7],[3,10,1,-8,-2,7,8,-6,-3,3,-9,4],[8,-5,2,-1,-7,10,9,-4,4,2,-1,6],[-5,-1,3,8,1,-4,-7,-7,-8,-4,-4,1],[-8,-2,3,-2,7,3,-1,3,4,7,4,10],[1,-10,-10,7,-4,-8,-6,-5,6,-3,9,-2],[-5,8,3,1,2,10,-2,2,5,5,4,4]],[[-8,-10,-5,3,9,9,-9,-5,4,3,-2,4],[-8,-9,-6,4,-10,-2,5,4,9,6,-6,9],[8,-5,-10,8,-5,2,-7,-9,9,1,9,9],[-1,-5,8,6,-9,-8,10,-7,-2,10,5,8],[1,9,-7,7,3,-6,6,-9,-4,4,-1,-3],[-1,-4,-2,-2,4,-2,-10,-10,9,-4,-1,-1],[-7,1,7,-3,-4,-7,-9,-9,10,5,-10,-3],[-2,-5,-1,8,-3,-8,-10,9,9,-2,6,-1]],[[-5,-6,-1,4,-9,6,9,-10,2,3,10,-8],[9,-7,-3,1,7,3,-10,1,7,-9,-3,9],[6,7,-5,5,5,8,10,-6,-1,-5,5,10],[7,-10,-6,-6,-10,-8,-10,-10,-5,-2,10,-4],[-4,-1,6,3,-1,-4,10,1,4,7,-4,-8],[-5,-6,8,-7,-10,1,10,-9,-5,-7,-6,-8],[-8,6,-10,-3,-5,-2,-10,5,-7,-5,-10,-7],[-9,3,3,-8,4,4,-8,-1,-5,-6,-3,-4]],[[7,7,-4,-4,9,8,9,-2,10,9,1,1],[-4,-3,-7,-7,-4,4,1,1,-7,9,-7,-9],[6,-2,-1,-5,1,-3,-2,-5,-7,6,-6,5],[8,-9,8,9,-9,1,8,-4,3,-7,8,-3],[8,-2,-8,2,-2,10,-1,3,4,10,1,10],[1,-1,7,5,-5,4,3,-9,6,-4,10,9],[-3,-5,4,8,-1,6,3,7,-6,1,-4,-4],[-2,9,8,-6,-8,-5,8,-10,10,-9,7,1]],[[7,-5,-2,3,-9,-6,4,-10,-4,-7,-6,-3],[2,9,10,-3,2,7,-6,10,7,-4,7,-3],[9,-5,-4,-1,-2,6,-2,6,8,2,6,-1],[5,3,-9,4,6,-3,10,9,-8,-2,5,-8],[3,-6,9,3,-3,7,5,-10,-5,-3,8,-6],[8,-9,-6,-5,7,10,-9,2,-9,3,-4,-5],[7,3,10,4,-7,-3,1,4,1,4,6,3],[-6,-7,1,-9,-10,6,10,-9,2,-2,2,-1]]], dtype = "int8")#candidate|426|(7, 8, 12)|const|int8
bop_427 = relay.equal(var_425.astype('bool'), const_426.astype('bool')) # shape=(7, 8, 12)
uop_431 = relay.atan(const_426.astype('float32')) # shape=(7, 8, 12)
var_433 = relay.var("var_433", dtype = "int8", shape = (7, 8, 12))#candidate|433|(7, 8, 12)|var|int8
bop_434 = relay.left_shift(const_426.astype('int32'), relay.reshape(var_433.astype('int32'), relay.shape_of(const_426))) # shape=(7, 8, 12)
func_375_call = mod.get_global_var('func_375')
func_378_call = mutated_mod.get_global_var('func_378')
const_443 = relay.const([-8.607667,-9.483425,4.105422,-3.187551,-7.443596,0.622683,-7.305202,-8.290973,-8.645964,-1.882446,-2.606072,-4.536522,-3.293053,4.887013,9.935787,3.643574,3.098844,-9.177812,-6.635417,0.634558,9.341929,5.255165,5.767011,-8.786376,-6.934320,-4.873296,-5.119134,8.029661,-5.628740,7.332399,2.979535,-2.183127,-8.827654,8.623846,3.249107,-7.557107,9.422515,-4.756703,1.231787,-2.778109,9.330012,-9.880707,-0.744335,-6.915110,-7.662378,-8.895523,-0.411585,8.115507,2.826753,5.639633,2.966200,1.784211,-2.287255,3.172543,-1.376034,6.310054,4.286985,-5.257710,-1.401509,-3.474427,-2.180738,-3.939323,7.813994,0.181943,7.508228,9.928745,-8.773000,8.434202,-2.839909,-7.241762,1.328908,4.059390,-3.082741,-5.499165,-5.292554,9.224344,3.582121,-3.316476,8.707431,0.485457,-2.137817,-1.413975,-6.608987,5.448933,-1.108012,7.904331,-4.832107,-1.994157,-3.397852,2.830965,-5.098120,9.514990,-2.189825,-3.402783,-3.845003,-0.406962,5.402862,5.365994,0.325863,-6.178500,5.044341,5.956292,-2.069705,-4.279042,-1.349231,-5.223398,-4.962853,-7.304953,6.518597,8.040365,-8.573895,-5.744312,-6.351234,4.786757,9.206395,9.045097,-1.471856,-1.412043,2.727266,7.425657,-8.005690,-6.766019,-9.069851,1.153684,5.487064,0.839589,5.556606,6.617341,1.494273,4.731988,3.212377,4.854379,5.267670,-4.891776,-6.044683,-9.289885,8.756362,-2.175203,4.060921,4.857187,-3.689115,-0.654620,8.207005,8.879337,5.044603,2.755983,3.357052,-5.805613,-0.792748,6.833690,-0.686210,7.837138,-3.387749,4.387315,3.879756,5.276446,1.451677,3.036253,5.188343,-7.113806,0.091631,1.170276,-8.242778,2.447564,1.735130,-5.274798,-7.216536,7.379802,0.499750,-1.869437,-5.857764,-5.059789,-6.180952,-4.975120,-2.693880,-8.961951,-8.585817,-1.807027,8.732763,3.555263,9.160203,-7.041801,1.987317,-0.488222,9.003023,3.366241,-0.831086,2.544487,-2.136368,3.007820,-7.865106,-1.033305,8.717397,-7.864023,5.516434,6.149563,9.616229,-7.724460,-9.150286,9.281133,-7.425671,0.893697,-9.190544,1.810972,-5.239488,1.118222,-8.671263,4.666486,-0.701539,-1.360205,1.120641,-5.694704,2.146351,7.580956,-4.807075,5.861621,1.970286,3.463794,-8.276306,-4.409411,6.353762,1.960078,-8.218360,-0.230915,-1.985084,-0.810542,-1.607623,-1.085994,3.590053,2.182148,-6.097369,-8.124081,9.496353,9.534930,-1.150459,-0.953599,9.709622,6.616541,-9.499378,7.328614,-5.221277,-4.766202,-1.543889,6.176674,-4.854064,5.246565,1.748149,8.975063,-6.860942,-2.355045,-1.742666,-6.244788,1.224368,2.253288,5.325742,-7.077785,-7.995465,7.957833,-2.434424,1.284179,8.461673,9.912086,-2.694687,-7.097480,-1.761986,-6.903117,2.508181,-5.459776,-3.114565,4.692198,-9.243354,-1.453645,-8.921297,-9.973293,-1.568005,-2.467249,-6.902011,-1.001470,-1.178787,5.640152,-8.718785,5.809778,2.934867,-1.733701,-6.454656,2.176317,4.131153,5.793418,4.067026,-5.904100,4.716732,-0.428515,3.138038,4.206610,1.413202,-0.280866,-8.252346,2.869578,8.557568,1.119557,1.501116,6.107664,-0.211189,0.260995,-1.798390,1.821930,-4.825840,4.779297,4.551744,5.616353,-4.653603,-4.309703,9.323486,-9.479312,3.089300,-1.738934,-8.861137,1.553529,6.591583,7.121325,0.379988,0.787513,-5.897464,0.934934,4.316477,-3.585270,-7.897850,-2.356449,-7.665284,-9.817512,9.268661,0.437345,-8.507309,-8.531190,3.393315,9.351064,8.739011,-5.986010,-7.240670,5.461061,-4.174311,2.663574,-2.858768,-5.139837,-2.221502,-9.204067,-7.529997,7.731443,-2.520374,-8.728823,1.223823,-2.977909,-8.246916,-9.507600,-8.553349,1.999940,0.715836,8.088800,-7.724467,2.911104,2.330044,-1.031642,5.455642,-8.867924,-7.433141,6.177976,1.349368,-4.117483,-0.616210,-2.758355,-1.201320,0.919073,-2.453299,8.366698,-9.064843,7.181239,-4.453793,4.700836,0.951882,8.329030,-6.397923,-1.405366,8.422613,-4.503568,3.808738,-6.094411,-6.042744,-9.526543,8.525221,2.087478,-8.215884,7.608487,0.677365,-9.179701,-9.106713,-7.216189,-8.457819,-3.250393,1.914682,4.308497,2.844660,-5.515023,2.688091,-5.865859,-2.532841,-6.751299,-7.086844,4.389667,4.378762,4.935854,9.580148,-5.614016,-3.690791,7.480633,6.212510,-0.584364,2.894716,-8.771791,8.248781,2.574695,8.139785,-1.556901,1.117082,4.765915,2.597060,-6.800891,-5.072652,-4.827975,-4.186484,-3.909311,-7.024158,-0.097443,3.532369,-0.573513,-7.673589,-7.237446,-3.349985,3.649003,-2.200388,-7.697553,2.662517,-7.591250,5.594272,-7.539808,6.630796,-5.113513,-2.273011,0.695362,6.138883,-5.789912,1.724410,6.149868,-3.940636,8.021304,8.099953,-7.398447,-8.723629,-3.871552,-4.786523,6.351925,3.049054,6.953896,4.887543,4.181922,1.400353,-1.961502,-8.921960,-3.234283,-9.548934,4.055042,5.101578,8.225722,8.631511,8.114214,-4.981862,6.896353,-0.761369,7.043365,8.400819,7.839932,3.564053,9.155550,6.269036,-9.437484,1.618832,-8.436789,8.045772,-8.665739,1.841564,-4.478914,0.226909,-8.944172,1.089399,0.480483,-9.086811,3.529224,-0.016568,-3.782739,-0.546517,3.021797,-0.931432,-1.410074,6.399237,-2.938676,-7.607699,1.080787,-2.540604,-1.401385,8.710838,-8.627983,-5.129841,7.740138,-9.742271,-0.180451,-9.316688,-1.153651,0.569438,7.940998,-4.181378,-7.680773,-4.225252,-3.521853,7.304968,-0.405927,-5.963825,-2.109508,-2.510864,2.838453,8.637302,5.041869,0.389089,8.994393,-8.407598,-3.190952,-2.125859,-4.107750,-1.449084,-1.148712,5.885266,-1.558258,5.971832,-9.514583,2.746334,5.771276,3.056393,-6.421080,-7.489727,-3.739601,-0.338100,2.119870,6.411805,-4.141747,-7.759708,1.985579,2.869257,3.283017,-4.336805,7.292739,8.801682,0.096070,9.998883,-0.487473,2.722542,3.597871,7.281929,-7.475846,-5.482006,-3.962906,9.034181,-8.263400,6.494504,-8.344018,2.311623,1.594342,-0.976226,2.885135,7.540565,6.329392,-5.793703,-1.711734,-9.391084,-3.056578,7.296779,5.430446,-9.529954,-4.578299,-4.699129,-2.708380,-2.558191,-4.119064,-7.721505,-0.602562,8.887787,-6.660590,-7.399730,2.496502,9.910785,4.453694,-2.090239,-3.704817,-7.512634,7.447809,1.010494,-6.160248,4.501033,-6.876836,7.442640,8.133137,-3.554322,-4.684414,4.428150,7.154491,-1.299169,5.384182,-5.896720,9.063169,-9.175344,4.717466,-6.897226,3.662560,-5.829422,0.943896,4.246343,1.268762,-0.414020,-5.081624,7.424667,2.940220,2.142951,2.236504,-1.359406,-0.791066,5.015281,-7.944327,-1.294204,8.620493,7.000145,-5.478787,-5.620422,-5.902207,5.884394,-2.882176,1.151701,-7.741583,-2.235240,-1.632516,6.247887,-6.312676,-6.251138,-4.838568,-3.431215,9.244603,9.526851,-7.528628,4.503755,-8.698087,-7.375376,-3.141949,-4.637923,-4.941014,-3.922529,1.107829,5.481985,-8.375065,-7.834356,-7.262940,-2.224404,-6.622579,4.259778,7.572984,-2.649808,-4.328961,-0.322322,-6.330091,1.728772,-8.334785,2.723813,3.195512,7.163245,-1.293184,4.268018,-8.874205,-9.287936,3.356323,-8.903373,7.495222,-3.937559,1.772045,-6.030060,-0.993175,-5.701067,2.571680,-4.097590,-0.920545,-1.557362,-2.100385,-2.539853,5.123767,9.683994,-5.469715,-9.465321,-5.770415,1.919966,1.822307,5.397795,-4.653912,-3.460131,9.893785,-6.320716,-3.320357,-4.805792,-5.445567,-9.775560,-8.131696,-7.059992,8.884847,-2.691803,-3.767453,6.079871,0.604081,9.811976,-3.218789,8.986882,-3.770809,1.504522,-6.897806,0.860241,-7.354907,-7.575597,-0.848363,-0.046944,7.876536,2.744483,-6.135234,-4.112964,-2.490408,3.000476,4.296773,-3.768750,8.034768,9.192611,-4.380699,-2.562692,-8.751175,4.466555,-5.235521,-9.151510,-1.831510,8.534912,-7.781912,-4.210938,6.980465,0.689889,-1.269580,-5.896590,6.638776,2.677022,7.417335,5.514727,-9.246368,-7.184677,-7.149733,9.378214,-3.880011,3.114271,-6.416395,8.174514,-7.930965,-1.640413,7.503699,-7.759025,-3.242643,-6.928358,9.634026,8.305603,-8.798483,-9.124632,-9.285908,5.002733,-5.900019,4.373704,-4.972421,-4.727714,0.073921,5.846046,-9.291314,-4.600342,7.495386,-5.230201,-0.329178,-7.767988,1.077758,7.139397,-2.627810,-1.985659,5.589491,6.343989,0.590351,-0.564630,0.782355,2.931647,0.708719,-3.900056,-2.227810,-1.028772,1.202545,9.347457,5.112107,-8.667892,6.253760,6.262679,8.370414,-7.946483,-2.729689,9.266608,-9.458343,6.309589,-6.139032,-6.006342,-8.186561,0.307045,3.545232,-5.174650,2.636390,8.073208,-9.821933,-3.892295,7.765484,-8.306177,6.886342,2.120651,-0.445509,-4.693327,1.845347,2.369290,6.238000,5.254856,9.448893,9.417439,-5.391475,0.896071,3.865798,-6.673384,-1.826580,5.953866,0.736269,1.557717,0.369284,-8.194678,-2.887485,5.115368,4.547358,-8.690992,-9.816286,6.607765,-7.488602,3.953021,-1.478519,6.792119,-9.667678,0.043249,8.924585,7.635325,-5.740052,3.934441,5.232257,-1.857063,9.447665,6.254566,-3.341723,9.090616,1.819311,2.095024,-8.994936,-8.794180,0.757646,-4.285464,-9.237934,3.612393,-8.149730,2.693022,3.968952,-2.797275,9.308670,1.170443,-5.415989,-9.910851,8.785700,-2.386138,-0.439985,1.921308,-7.221008,1.755512,3.991129,2.180362,0.238622,-9.055879,-2.198217,-4.346723,-1.616265,9.655884,-4.484464,8.829307,4.004943,0.859534,-9.887934,6.531555,4.440864,-7.534075,-5.955848,-3.350456,-9.005937,-0.505017,5.326369,-5.066783,-2.793854,-5.198246,-4.661375,2.114307,6.976846,0.769192,6.393024,-8.243957,4.318032,4.181793,-4.630966,-8.099433,-9.418274,2.694414,6.035295,-1.957922,-8.455152,-2.672892,-1.758646,-7.060216,-7.668400,4.288786,0.457434,-7.781653,-6.227694,-3.537670,6.418717,-4.601860,8.056544,1.827926,7.842523,4.361768,8.278831,-5.893412,0.634323,2.077201,4.634645,2.079357,6.584899,3.122207,8.780833,-4.769310,-4.342590,4.958750,4.890013,-5.654149,-4.687401,-6.379177,2.610349,7.369770,9.012186,9.660151,5.363234,6.619544,-5.100083,2.223419,-3.193161,8.801760,-4.828308,6.854467,3.808382,-6.852700,5.126099,5.758116,-0.761287,0.431634,-1.420567,-2.681248,3.361414,-2.977064,-7.318573,7.807365,0.042420,-3.158196,5.183853,7.457609,2.866613,-7.841806,-6.212305,-5.355324,-7.310686,8.704447,-7.255122,0.136131,5.604805,6.189239,9.718755,2.411208,7.420611,-4.915301,4.147558,-4.177025,9.804899,4.790800,-4.231684,-7.913499,9.636799,1.757726,0.981900,5.394170,-1.184781,7.272225,8.585818,8.952932,-3.369306,-9.209421,5.839426,-0.504530,9.898255,6.431986,7.202116,7.858035,6.323213,-6.987642,7.290108,8.291783,6.498942,0.001134,4.448009,2.220485,-2.708303,9.943362,-0.751480,-0.882334,2.609392,-2.918167,-7.341435,8.155593,-5.511098,-7.806545,7.334714,-1.608867,-8.611929,-9.402411,-5.489716,9.940799,3.770854,-6.913412,7.870712,7.858842,-6.771098,3.147238,5.274690,-8.916459,5.433747,4.434238,1.768023,7.104781,6.877186,3.593443,8.658980,-0.013047,-2.374934,9.646908,-9.348355,-5.748326,-5.737612,8.648596,0.833809,6.225962,-4.177532,3.630186,-8.902812,-7.193458,-2.255198,7.860640,-1.252056,-6.444825,8.919851,-9.651062,2.864914,-0.805143,2.079109,9.475281,-5.355059,3.228569,-6.603473,-2.205406,9.078318,-8.920132,-1.061335,2.033084,-0.913086,7.111922,9.455625,1.377549,2.348574,-1.910500,0.697756,8.242756,3.785344,-8.006196,3.759449,-2.048641,3.876545,5.567924,5.258614,0.668620,-5.173676,8.245514,-2.184484,-8.391737,-5.208902,-0.644790,8.287943,7.906220,-0.811567,-1.227332,-0.679762,-6.599289,5.165767,-4.125013,9.050186,-2.876052,-6.424267,9.755715,-2.583606,-2.797633,4.747635,-4.587527,-7.821229,1.544191,-5.726557,5.694309,-3.671578,-7.696688,4.945671,-2.619688,-9.149193,-7.810641,-1.266379,-3.745685,-7.382595,-7.647425,0.206215,-1.965495,-3.389156,9.797566,4.195804,-7.762552,-2.764447,7.525496,2.531647,-5.291626,6.367165,-9.731240,1.804566,-7.197893,-2.817991,9.792434,-9.350308,7.206279,9.699593,1.151323,5.765217,-7.405789,-4.850822,2.224303,-0.531286,-1.087647,0.769467,7.483974,3.291689,-9.632514,-7.057336,6.769914,7.747661,-9.679102,2.007809,2.919042,7.102950,2.539743,5.699739,1.294448,-9.969907,6.460345,-5.094367,-7.316514,1.751909,2.322790,-7.481005,-4.259099,-0.689829,-4.170922,-7.803296,-8.571304,-5.127270,1.257731,8.856542,9.929470,-5.975550,6.757221,9.098551,-4.693999,-2.573309,8.580091,2.885983,-9.776322,-0.951800,5.064513,-4.939384,-5.653867,5.314261,-3.860441,-6.279301,7.624574,2.045923,6.538577,-7.050936,5.536439,-4.119922,-4.732353,-1.124850,4.501151,5.309952,6.009936,-3.784860,-2.530252,1.238830,-2.520253,-8.957420,1.117850,-0.989967,5.404874,-8.362414,5.909399,5.729456,-1.011254,-7.205488,-9.103183,1.167584,0.202942,4.179060,1.226415,6.706910,-8.940867,5.074872,9.109363,-9.290102,2.067668,4.635474,9.114765,-5.966158,-4.069357,9.633094,-4.748624,-7.106900,1.511401,-8.926443,-4.126474,-3.225448,6.810630,-3.316984,-3.045324,3.111138,-9.103542,-3.428493,3.782097,8.922390,-9.618403,-3.699410,1.708950,-7.993292,-1.547851,-7.773248,-3.106820,2.982574,-7.569941,-1.312174,6.700637,-2.168175,-3.234941,9.060377,1.758180,2.326540,-6.446723,7.662105,-8.347311,-0.791003,-7.642196,-1.894352,2.134498,-8.177213,1.870685,-8.650706,7.611796,-8.159768,-3.418047,7.806044,0.098968,0.904279,7.044761,1.461273,-9.274162,-5.054077,-3.918477,-3.339677,0.086270,-5.184064,5.890803,1.288674,3.512585,3.265489,8.650101,-3.585840,3.295371,-3.003762,-0.395089,3.472004,1.737639,4.629766,-4.150628,-2.151473,-3.854313,-9.153671,1.318723,-8.028166,-5.139194,-3.908138,7.174401,-0.046028,-5.116394,4.878159,-0.633557,-6.210279,-0.247134,-3.098692,5.569225,-7.058354,5.647737,2.755052,-6.456716,4.576232,2.429815,8.671302,-4.159740,-5.333515,-8.889906,4.549916,-8.483222,0.375171,8.668053,7.227031,-9.249423,8.010754,-2.534845,-3.237281,-8.085501,9.029212,-2.694005,-6.074075,-1.015913,1.554892,-2.790541,-4.498719,-4.027078,-8.430650,5.279015,-2.985797,5.235173,5.029726,0.655159,5.312972,6.435273,7.741624,8.187451,0.530495,-4.833593,-0.609451,4.465734,1.819775,-1.594083,-1.354404,0.168443,4.494741,-2.343609,4.368631,1.751722,1.394757,3.692027,-3.856640,1.284384,5.023818,-2.616392,-1.379433,-9.168973,-8.935501,4.298858,-8.699640,0.829423,-6.174059,-1.340106,5.587300,-1.940402,-2.021135,-0.995683,-3.876056,-3.449549,7.668975,4.564888,0.678944,-1.546755,0.143879,-5.058055,-9.949699,9.213476,8.235057,-0.884349,8.067186,7.999961,8.388432,-6.365805,7.747758,4.899575,-4.049993,3.229840,-6.400273,7.357983,0.080616,8.073620,2.259622,-6.400927,-3.107057,-6.046837,8.859549,9.028517,6.940911,-1.767898,4.050970,5.690924,1.186843,4.346401,-7.845152,3.661892,-9.439526,-1.607983,0.142116,-4.776304,5.445496,-6.355438,-7.895290,3.144515,2.883007,0.443447,8.795538,-4.685142,3.755382,-5.302817,-3.044470,6.775207,-2.942376,1.776172,9.483814,9.372085,-7.783680,2.538798,-5.204688,-8.936379,2.138113,-5.350697,-6.652749,8.546518,-0.771540,-1.218428,5.481633,0.746064,5.769779,6.629424,-6.647534,1.342568,-6.624501,5.220841,-8.873262,0.015680,5.480477,-6.612873,-1.575642,2.466832,-3.666018,-7.575201,-8.314447,7.549322,-4.097983,-1.439663,-1.113106,7.218355,-2.257655,6.705878,-8.888330,-0.001525,-8.859263,7.554896,-8.448702,0.069309,-2.061978,-2.120824,2.870642,-9.707300,0.646458,-5.789058,8.296058,-2.808332,-0.669209,-2.319042,-5.241184,4.860116,3.794832,-3.912659,9.704420,-8.841093,0.813665,-5.667419,1.402408,-3.944742,3.966784,-3.364573,-8.806707,0.650035,-7.773358,4.622483,-6.910468,8.625849,4.517373,-1.997525,9.257890,8.944976,3.793541,6.783778,-3.372908,2.840789,-0.129057,-2.020565,9.577902,0.697276,5.465585,-7.517226,8.614677,-7.337205,9.596534,-1.031384,0.579350,2.694502,7.456797,7.992416,-0.800820,-2.993427,-2.596488,5.915772,-4.172249,4.317450,1.381988,2.232490,5.176532,-3.660330,-2.808707,7.614089,-0.394600,2.400352,4.796744,8.344580,0.540999,-8.527427,4.257525,0.992455,0.677529,8.860016,5.072248,6.046566,-8.511584,3.305116,-4.862577,6.088371,-9.857125,3.935132,7.882508,3.520720,-9.201827,6.179437,-7.966214,7.607824,2.183353,-6.970415,1.757921,-7.494637,6.943760,6.806979,-5.928831,-6.173435,0.880386,1.217207,9.981651,6.080534,-6.393818,0.571758,-6.446343,-6.411179,9.608074,-9.750917,8.791187,6.148299,-5.964227,-8.135435,1.537879,6.115630,-6.383343,3.463776,-5.530346,5.183778,3.172165,4.415402,3.022844,-3.128963,-5.620587,-7.439947,9.872715,8.877420,-5.880231,-2.242494,-4.219430,-4.226188,-9.885773,-3.397485,-7.361175,-1.219764,-3.815773,0.635256,5.518271,3.833516,-7.909642,4.476257,6.407290,-6.505856,8.788153,6.184570,-6.113865,-9.632766,3.532914,6.954460,9.568833,-3.942109,2.521554,5.154639,3.853846,3.035953,-9.400348,0.620798,7.291645,4.357328,-2.939371,-9.672683,-5.367806,-8.511454,-5.452160,-2.986662,0.264122,5.092347,-5.932409,7.462612,8.565545,-6.235175,-1.782451,4.658791,3.952284,-7.783563,4.896444,-5.246521,7.443228,-9.969768,6.984229,4.978396,8.448881,2.643806,-5.990888,0.617133,1.110138,2.614021,4.385476,4.236425,-6.453146,-5.721820,4.540940,5.451258,3.992413,-6.925767,-7.453518,8.987792,-5.500969,-2.340067,-2.855378,4.023565,4.941404,2.566947,3.743033,8.733603,-2.796258,-5.761468,-4.987316,-3.250774,4.432846,-0.369140,2.063304,5.103747,6.856385,-6.037200,5.783542,3.508003,-9.992813,7.029891,-4.196312,0.865508,-6.181559,-6.737409,-0.414514,6.906923,0.283658,6.325794,3.029167,-1.272577,-1.932691,-4.981436,-8.885845,-5.044028,-0.634564,3.357808,-9.924198,7.455117,-5.196182,-4.069458,4.951971,-4.554031,5.501170,7.936433,-4.041221,5.452354,-3.283599,-2.733432,-3.278074,6.342364,-4.845331,9.808598,-7.756534,3.143207,-0.251326,4.183367,4.046494,-9.718540,9.678969,-3.981386,5.517235,4.660638,5.217461,7.090369,-9.795445,4.678798,1.929784,-2.729161,7.369576,-0.027345,7.382882,8.712218,7.682603,6.895254,5.067162,-9.105880,-6.838075,-0.926109,5.341695,5.022238,6.829685,-0.175620,5.376065,-9.374566,-5.370232,-8.649687,-6.273696,4.510584,7.317755,-1.852235,-3.085826,7.395971,-1.720697,-5.882326,5.208629,-1.908242,-2.713693,8.899436,0.272638,3.574817,-0.081540,6.061405,9.149874,-7.082170,2.647152,-4.366582,1.679685,-9.881327,5.649353,0.913484,-8.172271,8.890048,-6.060076,-8.982426,-5.740772,-1.872578,8.223779,6.041197,-2.086274,6.384461,7.226595,9.279691,-7.900480,-1.144210,-8.225916,-7.807198,2.949415,-7.311660,1.547604,7.399591,-4.499492,-8.970008,6.670376,-1.436836,-3.422890,-9.654859,0.395589,-7.926853,1.031581,-7.129846,8.027989,2.797124,-8.721310,-1.175107,-8.513517,-7.750107,5.692993,0.210380,-6.614854,-3.546935,6.682137,-3.455377,-9.987689,-9.292040,-2.753692,-0.585962,-9.426768,-0.156419,7.470050,-7.140867,0.321000,-1.869820,1.102845,6.469881,2.515094,-9.423237,-2.133468,-4.857943,-9.410755,4.431128,7.918189,-3.628269,6.695877,-5.580651,5.288392,-7.537542,6.716768,-1.322341,-2.640744,8.455588,7.974706,6.703182,-0.350676,7.729558,-0.363960,0.475148,-1.076266,4.203951,0.288209,-2.550933,-4.632059,0.856527,6.573265,7.960449,1.128707,4.056488,-0.399887,4.960182,-9.454606,7.519227,3.771548,-5.031382,-2.962025,1.974451,-9.044993,9.749355,-3.754943,-7.397510,-0.858917,-7.815961,-9.622224,-0.059416,-0.763676,-7.953643,-5.494065,9.002335,-5.158684,3.914060,-8.186043,-6.680358,-0.423156,2.604402,-3.028433,-2.373451,8.287949,5.243427,1.837770,6.562511,7.599761,-3.161940,8.354761,0.543762,-0.692471,4.591842,5.991575,3.566169,5.348101,-0.626529,-1.820407,-3.046224,5.372690,-9.234454,4.868312,-4.773053,7.543114,1.984931,7.270131,-2.404404,8.927934,-0.506213,-6.798188,2.745367,-3.201199,0.965862,-2.443479,7.120981,0.013138,-8.636561,9.822590,3.734017,-2.275057,7.358121,9.162698,4.338315,1.790597,0.563966,0.166405,2.773095,2.289911,-6.919675,-0.900941,4.072755,2.735052,0.166451,2.576154,9.434834,4.633983,8.879972,1.625773,6.286137,-6.246081,-6.308577,5.140560,3.973203,-7.283598,5.976186,3.759336,8.444898,-1.062926,6.595572,7.879841,2.737380,-5.558534,-8.379913,9.018829,-1.116015,-1.309424,7.185846,4.179274,-8.673707,6.822321,-7.666820,7.182663,7.288094,-5.565830,5.111591,-1.583568,-5.861833,4.499861,-6.085355,4.490828,-6.080133,4.275654,0.264416,-7.688251,-8.956905,7.107879,7.792501,-9.334362,7.886374,3.617432,4.368048,1.515401,-7.894187,-9.737884,-4.272014,-6.612873,5.594702,-6.447545,-3.871076,2.579691,-5.509068,7.129254,7.996299,9.668593,1.586960,6.762415,-5.656013,-8.330057,5.118374,5.700144,-2.901026,-9.633031,7.855105,0.319505,6.610243,-3.110455,5.235849,4.664864,-1.933741,4.350035,-9.837071,-1.477275,-1.017199,5.558390,8.684719,1.850215,-9.964470,2.410023,-1.842665,8.122389,1.279772,-4.806492,-1.145040,9.491149,-7.312709,-6.530440,2.522836,0.031207,6.473454,4.984343,3.688136,6.844441,-1.734475,5.363986,2.181274,4.541154,-7.846955,0.772387,0.540099,1.241609,-2.394208,-3.453154,-8.089901,6.753262,9.112813,-5.683078,9.932898,-7.807687,4.067553,-6.921761,0.600289,6.439475,3.014317,-5.404973,-2.642327,-9.537559,6.034019,-3.101639,-2.568861,7.196419,6.641756,-9.322021,5.460053,-2.712015,-8.666596,6.618942,-6.719635,-5.467273,-8.848750,6.051810,-5.877525,2.671723,-0.365531,-3.132915,5.945515,-9.954777,8.005640,4.774206,-2.899603,5.902963,-8.606901,-0.452532,-4.230355,5.189981,5.037054,3.611493,-7.932722,3.459624,-4.402386,-1.823126,4.516864,-1.773073,0.192998,-0.087620,-6.215081,0.935200,-0.192320,3.041473,-7.098396,9.107781,8.796764,5.714649,0.003707,4.812641,-4.037252,6.719492,-9.191519,1.487524,2.499327,2.266724,5.329593,8.409654,-5.810796,-3.845133,1.555364,-0.491991,-7.398486,-8.230443,-0.108158,-7.924580,0.262932,1.510030,7.439259,-0.505203,-0.802484,-7.962530,-0.207270,6.128038,2.532319,9.833466,-4.979975,1.491665,6.548380,-8.353416,8.107123,7.601794,1.170330,3.178485,4.045003,8.861785,7.281128,4.472376,0.729825,9.614444,6.464597,4.011005,-4.900093,-5.013282,9.137389,-1.723234,2.045165,9.269412,-3.205863,-6.253388,-9.035083,3.129866,8.457631,6.471422,0.997939,6.801294,9.050220,-6.034416,-3.721797,-2.285137,-8.740174,-5.709408,-2.798277,-9.406245,-0.127193,-3.438812,-5.497545,7.710494,-8.966476,7.568162,2.918772,-8.927300,1.294666,-8.229134,-6.129684,7.602577,0.546487,-3.387230,-1.180074,-1.042314,5.120254,0.963015,-9.194793,-3.326813,-3.309192,3.999494,-4.356063,-6.190418,-0.046804,9.144487,3.619520,4.183972,2.998915,-4.239246,-5.486683,-0.655667,6.591003,-1.326390,-3.334665,2.902258,-8.089835,-4.122901,-4.190847,-9.788888,-6.406179,2.122825,0.272624,-5.449462,9.831834,-3.540386,-3.590420,0.975093,-4.198590,0.402544,-0.968649,9.072809,8.592691,-0.143556,3.430960,8.386011,-1.773702,9.444099,3.583347,-1.972921,3.117096,5.412361,-4.180914,5.091568,-7.044689,4.739309,2.003732,0.787650,5.205521,5.649622,-2.002205,-7.554082,8.633511,-7.178539,9.538719,6.691954,1.257800,-4.133255,-3.980496,6.514755,5.833348,4.662261,7.138020,0.920047,-4.341689,2.217350,3.895749,-2.857258,-6.702988,-1.899781,6.036037,-6.433101,-6.889036,-2.220096,-6.145604,2.694390,7.800096,4.906890,8.137491,7.347181,0.103504,-3.322807,-8.038718,1.274211,-3.054979,-3.558071,-5.801701,-8.098204,-1.418588,8.316684,-7.568223,-5.481992,5.268779,6.547927,-0.827364,4.528649,1.338486,5.959397,-4.484522,-2.217863,-2.011986,-3.284593,3.939140,1.861214,-5.017243,0.195227,2.974296,-7.503638,9.397881,5.270783,-5.637126,8.483228,-4.464372,1.412987,3.524622,9.352953,-0.626410,-8.883932,5.541215,7.520063,-0.039276,-6.647467,-3.755229,2.185498,-6.154752,-9.331351,8.607467,8.320829,-5.698527,-7.900062,-1.993091,9.610735,7.911358,4.805139,9.864417,-6.538069,2.461161,1.608288,0.625949,0.106146,0.623387,-8.647514,3.338298,-3.043790,-5.686228,3.487927,4.970462,-1.655026,1.440998,2.564077,-1.565365,-8.206744,-3.824608,-1.134618,-7.415199,-0.532417,0.063801,-5.922624,-9.655267,-7.730632,9.559825,8.055258,-9.681832,-2.943054,5.782347,-1.988342,3.367049,3.990464,-2.232068,-8.337010,0.392142,-9.165116,4.980851,6.514676,4.633912,6.514301,-3.196596,7.278129,-0.028427,-7.829058,6.918825,3.888595,8.970570,7.164689,-0.927161,1.244100,-6.405409,-6.259932,-4.449577,2.325636,7.806086,2.385624,4.422028,-4.478129,-9.728053,-9.190100,1.429895,-6.719076,-7.405545,-6.506828,4.198504,3.711635,4.251707,-1.078631,3.534444,-0.808599,-4.641451,-6.544696,-2.117741,4.550728,7.431562,6.695646,9.260786,-2.857047,1.572358,7.869574,-7.045325,-6.213103,-0.435465,8.836327,-4.846322,2.293868,3.538395,-8.464462,-5.612219,-9.604295,3.141181,2.566793,-6.281420,4.193234,-8.416170,-6.232223,6.887584,0.015262,1.785223,6.958617,-8.918262,-2.465776,2.758126,2.056085,-8.485627,8.497746,2.939551,9.791327,-1.034972,7.558427,9.182348,1.901075,-8.288346,-5.626934,-0.300081,8.390861,-9.816562,-4.812437,2.382661,-3.040533,-0.087577,5.291973,-2.403279,6.135728,0.626415,8.798050,-7.753867,8.194328,8.797202,7.725091,-7.262252,-9.232315,-8.058483,-7.740859,7.550250,-3.845202,-9.671162,6.715092,-5.697267,-5.796126,-0.745762,-9.549663,-5.867676,4.398827,1.000308,7.137455,-4.760816,6.090561,9.085906,-8.365665,-2.046346,-6.958346,-3.821903,9.908930,-7.550735,1.971033,7.014004,7.366593,1.488727,-0.560904,3.079944,-6.492875,9.388587,7.511360,8.851087,9.560544,-8.046296,6.376462,-5.202328,4.305904,-8.323302,6.773489,-8.151667,1.288447,0.779134,-1.551102,-7.507229,-2.057191,-8.529555,-7.492918,7.826345,8.082489,3.604933,2.022912,8.736660,-6.577145,0.432629,-0.023517,-8.389806,3.821639,8.873018,8.772898,7.670911,3.258761,6.480717,5.177558,-0.161184,-5.108943,5.839641,5.863499,-8.003517,-2.321092,0.345189,4.242408,5.529419,2.762032,-6.633425,-7.952071,7.767883,-6.055271,1.610157,2.183531,-9.180296,7.273294,4.801874,1.498205,-5.332658,6.611161,-5.863732,5.693418,-3.831193,-5.834794,4.448127,-7.952205,-2.560421,5.360255,-9.615376,3.778009,-8.700856,3.483089,0.732668,7.967581,-8.912734,3.650416,2.338308,-3.479417,-2.291787,9.097625,4.845703,-0.341593,-2.561508,3.648271,-0.551319,8.309404,1.784858,2.344882,0.616543,-1.252818,6.131928,-9.016144,6.682004,-9.522312,6.303699,3.486445,8.103968,2.270143,-5.365014,7.149392,4.106142,9.954636,7.371342,-7.126407,-6.332963,-9.428915,-3.458673,-1.324933,-6.425550,7.456783,-2.301623,-8.635252,-5.689974,8.867212,6.580651,-9.554556,-7.502639,1.984190,-6.944068,-8.772632,0.169521,-2.466513,-5.121772,5.227954,-8.226998,-5.226375,2.848142,-4.744624,-5.114527,-0.417878,-4.454760,6.082639,6.254037,-0.848789,-9.998614,-7.873229,-8.594799,1.780561,7.059614,5.615560,-8.022726,6.786633,-7.184866,4.999234,9.420904,-6.519990,-1.469866,-8.135422,2.903207,3.444791,-3.502314,8.088354,1.910097,2.519605,2.019813,-0.877064,-0.009116,5.638733,9.944469,-3.449933,5.804294,2.878428,-9.924724,4.269155,-2.947193,2.874789,-7.115649,6.290400,3.063715,-1.446323,5.029784,-6.971322,-0.842633,2.903446,3.848321,8.806348,-2.827399,-9.818616,-3.723637,-8.066602,1.164212,8.350771,-3.533832,7.408479,4.646497,-2.575327,-6.056124,1.856911,5.867867,-2.811330,-9.001264,9.359829,-1.656168,9.851419,0.705227,-5.608482,9.813337,-2.896956,-6.804883,5.481035,8.427819,5.007544,4.933769,0.852923,1.410949,3.612206,6.817804,-1.369263,-7.241816,-9.741398,-0.841013,-4.852529,8.578984,2.611114,-0.123781,0.235410,6.003379,6.796874,9.880567,2.334982,7.229684,-9.357866,8.285042,-8.601248,-9.809993,3.645643,3.536588,-9.248992,-3.978468,9.160291,4.259898,-2.153027,6.982937,8.548519,-9.819073,9.073450,8.716149,-3.700470,-6.446476,-4.117111,-9.317830,3.634372,-7.530949,-3.361722,-8.158645,1.504705,-1.822308,-2.685834,-9.467403,9.899116,-3.824362,-4.225234,-9.411245,-2.886785,7.386670,-9.259927,-2.644053,-5.063313,7.267787,6.878924,-9.617585,5.248857,-2.379565,-0.446725,6.695689,-6.002538,-7.753300,3.032202,4.384774,1.085233,9.664528,-0.586924,-8.031539,-1.933332,1.072424,0.464573,-6.374294,7.231672,-9.833079,6.504380,4.883408,4.048774,-9.179598,-8.344243,-5.951305,6.289977,7.002833,0.390342,-0.279663,-6.776175,6.107127,5.031417,-7.746641,-1.067639,-6.704163,3.699186,6.211584,4.757851,3.389765,-9.214274,6.970363,5.285809,8.080785,-9.069832,-2.201767,-9.910986,-9.265087,-0.498703,-6.241475,6.076048,-1.829366,-9.568649,4.478790,-7.153084,4.593848,-8.010582,-3.044834,-5.992180,-6.470636,7.358540,6.650848,-9.987767,0.562143,-5.023692,-5.102396,-0.499055,-2.088240,-8.143610,-3.522576,5.908200,9.980857,-2.396449,1.351137,-9.592252,-4.837902,2.382669,9.470962,2.755029,-1.998673,-5.527371,-0.850269,5.852245,8.981055,-9.143223,-8.178244,0.729155,-3.767524,9.845074,-9.634543,1.183422,7.739302,-7.264768,1.443636,8.681426], dtype = "float64")#candidate|443|(2880,)|const|float64
var_444 = relay.var("var_444", dtype = "float32", shape = (180,))#candidate|444|(180,)|var|float32
call_442 = relay.TupleGetItem(func_375_call(relay.reshape(const_443.astype('float64'), [16, 15, 12]), relay.reshape(var_444.astype('float32'), [180,]), ), 0)
call_445 = relay.TupleGetItem(func_378_call(relay.reshape(const_443.astype('float64'), [16, 15, 12]), relay.reshape(var_444.astype('float32'), [180,]), ), 0)
func_375_call = mod.get_global_var('func_375')
func_378_call = mutated_mod.get_global_var('func_378')
call_447 = relay.TupleGetItem(func_375_call(relay.reshape(const_443.astype('float64'), [16, 15, 12]), relay.reshape(var_444.astype('float32'), [180,]), ), 4)
call_448 = relay.TupleGetItem(func_378_call(relay.reshape(const_443.astype('float64'), [16, 15, 12]), relay.reshape(var_444.astype('float32'), [180,]), ), 4)
output = relay.Tuple([bop_427,uop_431,bop_434,call_442,const_443,var_444,call_447,])
output2 = relay.Tuple([bop_427,uop_431,bop_434,call_445,const_443,var_444,call_448,])
func_449 = relay.Function([var_425,var_433,var_444,], output)
mod['func_449'] = func_449
mod = relay.transform.InferType()(mod)
var_450 = relay.var("var_450", dtype = "int8", shape = ())#candidate|450|()|var|int8
var_451 = relay.var("var_451", dtype = "int8", shape = (7, 8, 12))#candidate|451|(7, 8, 12)|var|int8
var_452 = relay.var("var_452", dtype = "float32", shape = (180,))#candidate|452|(180,)|var|float32
output = func_449(var_450,var_451,var_452,)
func_453 = relay.Function([var_450,var_451,var_452,], output)
mutated_mod['func_453'] = func_453
mutated_mod = relay.transform.InferType()(mutated_mod)
var_512 = relay.var("var_512", dtype = "int8", shape = (16, 7, 14))#candidate|512|(16, 7, 14)|var|int8
const_513 = relay.const([[[-6,8,6,9,-9,-9,-6,-4,-1,8,10,4,5,3],[1,-9,-4,3,8,1,6,2,5,8,-1,-6,10,-2],[-7,8,5,-7,4,-9,1,2,2,-1,10,-2,6,1],[-7,-2,8,-4,-9,1,10,8,2,1,5,-10,1,-3],[2,-4,5,-3,8,-7,8,-10,10,2,-1,-5,-6,9],[-8,4,-4,-9,6,5,9,1,-10,6,3,9,4,8],[10,5,10,10,-10,7,10,10,-4,7,-3,3,2,10]],[[7,-3,-5,-8,10,3,6,-7,-3,-6,-9,-2,-5,-8],[8,-2,-6,-3,7,-8,-1,8,2,-6,2,4,6,-4],[1,-9,-2,4,-9,-10,10,5,10,9,-9,-9,-8,2],[8,-4,-2,8,7,1,-10,-2,1,-2,-9,7,7,-10],[-10,8,10,9,-6,-5,10,6,-9,2,6,-4,-6,-4],[8,5,-6,-8,-4,8,7,-2,-9,8,-7,-1,4,-9],[-8,-3,-6,-4,1,9,-2,-7,10,5,8,-9,-4,9]],[[8,8,4,10,-2,-2,-10,-10,10,1,-7,-9,-2,1],[1,-5,1,-4,-7,-4,-1,-1,9,-3,-1,7,3,-4],[-6,-2,-8,-7,2,-3,-8,-7,-5,-1,-2,-3,1,2],[8,8,2,5,6,-10,-5,-7,-9,-5,-3,-9,3,7],[-2,7,-4,7,6,7,-6,-2,9,6,-2,-4,-5,7],[5,-3,2,8,-6,1,7,-8,4,-3,-7,-2,-8,-5],[9,5,7,-10,8,4,-5,10,2,6,-5,-10,-8,5]],[[-9,2,-2,2,3,-6,-4,-6,5,2,1,-5,4,3],[8,-9,6,-6,6,-8,2,1,6,4,1,-1,3,-1],[3,-1,1,1,1,8,5,-8,1,10,7,1,9,10],[-9,-9,6,7,-9,-7,-4,-8,2,-6,5,10,-2,-10],[4,3,5,-8,-3,10,-1,-2,3,-6,6,-8,5,-5],[-1,-10,-6,-10,6,-2,1,2,-1,9,-4,9,-4,-3],[8,-10,2,6,2,9,-2,-8,4,-8,-6,-1,1,-2]],[[-8,8,4,7,-5,-6,-6,6,7,-2,-5,8,-7,-4],[10,7,-3,-5,2,-5,-2,-7,-7,6,-6,6,7,3],[-4,4,2,-1,-6,-2,-6,-9,-9,7,-7,9,-9,5],[1,-2,2,9,5,7,-6,-10,-9,3,5,-3,10,6],[-8,-7,-6,6,-3,1,4,-9,-8,-7,10,-4,-7,-7],[-8,-8,1,-7,-4,-4,7,7,5,4,-9,-2,-8,-3],[-3,3,3,-2,-9,-3,2,-2,-5,10,6,-3,4,3]],[[-4,-8,9,10,5,8,1,-10,1,9,2,-5,-1,5],[-6,7,9,6,-9,9,8,-1,-9,9,-3,-5,6,-7],[-10,4,3,5,1,9,10,3,5,5,4,-3,4,4],[-10,1,-3,6,-8,-9,4,8,-8,-2,-6,-9,2,-9],[-2,6,-4,-1,-2,7,8,1,-4,6,10,6,-6,6],[7,-4,-8,2,-7,-1,8,1,3,-9,-10,10,-4,6],[9,8,9,6,2,9,9,-8,-9,-6,-10,-9,4,10]],[[6,-8,10,-3,-7,6,9,7,-9,-6,6,9,8,8],[-9,-10,6,10,-3,7,-3,9,2,9,-3,-8,-8,-6],[-8,6,5,-2,3,7,6,8,-6,-9,-5,10,3,8],[6,8,10,-1,10,-6,-9,3,-4,3,7,10,2,1],[-7,-7,-5,-7,8,2,3,-5,10,8,-8,-7,4,-7],[5,-2,-9,5,3,-10,10,-3,1,-7,-5,-6,5,7],[1,4,2,-8,4,-4,3,-1,10,-10,-1,4,2,-8]],[[5,6,9,-2,7,-1,-3,-1,-3,-1,-6,3,-8,3],[9,8,-7,10,8,7,3,-8,5,5,2,10,-9,-5],[-4,-8,2,-8,2,-4,-1,-8,1,1,5,-5,-3,5],[9,-8,10,5,4,2,-3,-8,9,1,10,-5,9,4],[-6,4,10,-8,10,2,-9,1,1,8,-3,-10,-4,-2],[7,-5,-6,6,-2,6,-10,-9,-3,2,-10,-3,-1,10],[10,-8,-9,-7,3,10,-10,9,-7,8,1,-5,10,5]],[[-3,-5,-6,-9,6,-9,3,-6,10,-2,6,-8,-2,7],[4,-3,5,-1,3,-8,-10,-9,10,4,1,-8,10,3],[10,-3,-1,3,-6,-9,-6,7,-5,7,-2,-7,8,1],[1,9,-3,8,-9,-2,-5,4,-9,7,9,-1,-4,-3],[4,-2,9,10,4,-6,9,7,-8,-5,-6,-2,4,-6],[-2,5,-5,2,-8,6,10,-4,1,-3,4,7,-8,-5],[-2,3,9,9,4,-8,6,2,-7,5,10,6,-3,6]],[[-1,4,-1,7,-4,4,10,10,-5,1,1,-9,-3,-6],[7,8,2,-3,-10,1,-9,-3,8,-6,-6,-4,-5,9],[-7,4,7,-3,-5,-2,-9,8,9,-10,5,-9,-4,-9],[5,1,-4,-5,9,2,8,-9,-8,-6,8,-3,1,5],[4,-8,-3,10,-4,-10,6,-6,-5,-1,2,9,3,-5],[3,-2,2,-7,-7,-2,-5,5,-4,6,-6,4,6,7],[5,-4,2,7,-3,10,-1,-4,-5,-8,8,2,-2,-1]],[[2,-8,2,5,-7,7,-7,2,9,4,5,-5,-5,6],[-5,-8,4,4,-7,9,1,5,-1,6,5,6,-2,-10],[9,-6,2,1,-9,4,-6,-1,-9,7,-5,1,-2,7],[-7,-1,-4,3,3,4,1,-10,-10,-5,9,-10,4,-4],[8,10,-8,-4,-10,-8,10,-4,9,9,-7,10,-4,-2],[-4,5,-6,7,-6,6,-7,8,6,10,8,-7,-2,2],[-1,-4,-9,-5,2,10,-3,3,-9,-7,2,10,-5,-6]],[[-8,-2,-1,2,-3,-6,8,-2,-2,-1,7,6,3,1],[5,-4,-4,-9,-3,8,7,1,-1,6,-10,-2,5,8],[4,-6,7,-9,6,-9,-9,5,10,-3,10,4,-8,-1],[-4,1,-10,-8,-8,-9,7,5,4,3,-7,7,-10,9],[7,1,9,-3,10,6,-8,-2,5,-4,7,-5,6,4],[-2,3,3,5,7,-2,7,5,-5,4,-4,8,-6,8],[6,-9,6,-10,-10,-2,-2,6,-4,-7,-7,8,-9,-7]],[[-3,8,-8,10,1,-5,-4,7,-3,7,3,-6,-7,6],[-3,3,-9,-5,-10,-2,-6,9,6,-8,-1,6,-9,6],[7,1,4,-7,-5,-1,7,3,10,3,-1,5,-6,-6],[5,8,-2,3,-1,9,3,10,-3,5,-8,-1,1,-1],[-9,9,-6,6,-4,-4,-1,2,4,6,-8,1,9,-4],[-8,-5,-1,10,1,-5,-7,1,-5,2,6,5,8,9],[5,-10,-8,1,1,-7,9,5,-5,6,1,7,7,-1]],[[-7,-4,4,7,-1,1,10,-2,4,-5,-6,-6,8,-4],[7,-1,4,7,1,9,-2,4,2,9,5,-2,-4,10],[4,-8,-7,-5,6,10,8,3,-2,4,-5,8,8,3],[-10,5,-6,7,5,8,-6,1,8,5,-1,1,-1,-5],[1,-10,-2,-7,9,-4,5,-6,-10,6,2,-5,-10,8],[7,10,-3,3,7,-4,3,1,-1,1,-5,-7,-8,-10],[1,2,1,-10,-2,10,2,-8,-5,2,-7,7,-2,10]],[[1,8,10,-1,-2,7,-3,-5,-4,-7,3,5,4,3],[8,-6,5,-10,6,8,-2,3,-4,8,3,-7,9,-6],[1,1,-5,8,-2,5,-10,5,-1,-7,9,3,3,10],[-1,6,-6,-3,1,10,-10,1,-1,-1,-7,7,4,-9],[1,10,6,6,-3,4,10,9,-3,9,-9,6,9,-3],[5,-1,-3,-10,8,-2,5,-7,2,-3,6,-10,-2,-2],[-2,-3,9,7,8,-1,-3,7,9,-1,10,7,-7,3]],[[-5,-8,2,-6,-7,4,-10,2,-8,-9,5,-9,3,-4],[-4,10,4,8,1,-8,9,-6,7,-2,10,-1,1,-1],[7,-7,-2,2,-6,3,-8,-8,3,6,1,-2,-1,-6],[-4,-9,2,-3,4,2,8,7,-4,-3,-6,-6,8,10],[2,4,-4,-6,10,3,-5,-3,-10,-10,-5,3,3,2],[9,3,-7,9,9,-10,-7,4,-9,6,9,-6,-9,10],[8,5,2,-3,2,-10,9,1,-4,7,-2,-3,-1,7]]], dtype = "int8")#candidate|513|(16, 7, 14)|const|int8
bop_514 = relay.logical_xor(var_512.astype('int8'), relay.reshape(const_513.astype('int8'), relay.shape_of(var_512))) # shape=(16, 7, 14)
func_114_call = mod.get_global_var('func_114')
func_117_call = mutated_mod.get_global_var('func_117')
const_519 = relay.const([-8.903796,9.520909,3.366206,7.252360,-0.606409,5.284664,-5.294996,-6.651455,7.486557,8.230391,5.851565,5.134248,-9.752348,-0.084096,8.610957,-6.281493,-1.469574,-2.695244,-8.094326,-4.174815,-0.986406,-0.846563,9.055323,-2.703662,-7.821786,-9.398800,-1.154694,6.572590,1.843401,-2.450914,1.766244,-4.629582,0.448855,9.935719,0.488391,-9.959635,-6.907694,-9.286295,0.189358,-8.279775,-2.733519,2.224408,-4.411665,-5.021879,1.069933,-5.175839,2.627102,-8.144865,7.241224,-5.242441,-3.444695,-9.925701,5.176202,-7.784436,-4.173021,-2.134074,1.706773,9.382029,-6.632168,4.473742,6.240788,0.150989,9.720102,0.540066,0.946425,3.560937,-8.160727,-6.697099,-9.457389,-9.808457,1.179191,0.081221,9.612023,-1.182674,-8.681514,1.791852,9.825431,-2.084024,-2.403774,0.820643,-6.374330,8.984881,9.243979,-0.689092,-2.248059,-6.185943,-9.748315,-5.958085,-6.500931,6.359633,3.637627,-1.357371,2.957059,3.344935,-2.262558,-8.848788,7.824539,9.660262,5.498152,-1.707686,5.537218,-0.063272,-4.643770,1.561495,8.540542,-7.558446,8.769809,-9.592052,1.144665,-2.793119,-9.329202,-0.448464,8.034388,-3.311564,-2.853366,-5.985582,5.722950,4.042956,-8.964884,2.297906,7.288153,-2.293429,-2.242569,-6.622751,-4.609240,-6.634260,6.736039,-6.649575,-7.977714,4.863041,4.958587,-6.876924,-3.202183,-0.282889,-6.251979], dtype = "float64")#candidate|519|(135,)|const|float64
call_518 = func_114_call(relay.reshape(const_519.astype('float64'), [9, 15, 1]))
call_520 = func_114_call(relay.reshape(const_519.astype('float64'), [9, 15, 1]))
output = relay.Tuple([bop_514,call_518,const_519,])
output2 = relay.Tuple([bop_514,call_520,const_519,])
func_534 = relay.Function([var_512,], output)
mod['func_534'] = func_534
mod = relay.transform.InferType()(mod)
mutated_mod['func_534'] = func_534
mutated_mod = relay.transform.InferType()(mutated_mod)
var_535 = relay.var("var_535", dtype = "int8", shape = (16, 7, 14))#candidate|535|(16, 7, 14)|var|int8
func_534_call = mutated_mod.get_global_var('func_534')
call_536 = func_534_call(var_535)
output = call_536
func_537 = relay.Function([var_535], output)
mutated_mod['func_537'] = func_537
mutated_mod = relay.transform.InferType()(mutated_mod)
var_647 = relay.var("var_647", dtype = "uint32", shape = (2, 2, 15))#candidate|647|(2, 2, 15)|var|uint32
const_648 = relay.const([[[-7,-4,4,-2,10,9,7,8,9,-7,8,-6,1,-2,8],[-10,8,7,-6,6,8,-5,-7,-2,-2,5,-1,7,-6,6]],[[10,10,-1,-3,9,-4,-3,3,3,-10,-6,-7,5,10,4],[7,1,-3,6,9,5,2,2,10,1,-2,-3,6,4,9]]], dtype = "uint32")#candidate|648|(2, 2, 15)|const|uint32
bop_649 = relay.right_shift(var_647.astype('uint32'), relay.reshape(const_648.astype('uint32'), relay.shape_of(var_647))) # shape=(2, 2, 15)
func_214_call = mod.get_global_var('func_214')
func_219_call = mutated_mod.get_global_var('func_219')
var_654 = relay.var("var_654", dtype = "float32", shape = (180,))#candidate|654|(180,)|var|float32
var_655 = relay.var("var_655", dtype = "bool", shape = (896,))#candidate|655|(896,)|var|bool
call_653 = relay.TupleGetItem(func_214_call(relay.reshape(var_654.astype('float32'), [15, 4, 3]), relay.reshape(var_654.astype('float32'), [15, 4, 3]), relay.reshape(var_655.astype('bool'), [56, 16]), ), 0)
call_656 = relay.TupleGetItem(func_219_call(relay.reshape(var_654.astype('float32'), [15, 4, 3]), relay.reshape(var_654.astype('float32'), [15, 4, 3]), relay.reshape(var_655.astype('bool'), [56, 16]), ), 0)
func_534_call = mod.get_global_var('func_534')
func_537_call = mutated_mod.get_global_var('func_537')
var_659 = relay.var("var_659", dtype = "int8", shape = (1568,))#candidate|659|(1568,)|var|int8
call_658 = relay.TupleGetItem(func_534_call(relay.reshape(var_659.astype('int8'), [16, 7, 14])), 0)
call_660 = relay.TupleGetItem(func_537_call(relay.reshape(var_659.astype('int8'), [16, 7, 14])), 0)
bop_662 = relay.add(bop_649.astype('int16'), relay.reshape(var_647.astype('int16'), relay.shape_of(bop_649))) # shape=(2, 2, 15)
output = relay.Tuple([call_653,var_654,var_655,call_658,var_659,bop_662,])
output2 = relay.Tuple([call_656,var_654,var_655,call_660,var_659,bop_662,])
func_690 = relay.Function([var_647,var_654,var_655,var_659,], output)
mod['func_690'] = func_690
mod = relay.transform.InferType()(mod)
var_691 = relay.var("var_691", dtype = "uint32", shape = (2, 2, 15))#candidate|691|(2, 2, 15)|var|uint32
var_692 = relay.var("var_692", dtype = "float32", shape = (180,))#candidate|692|(180,)|var|float32
var_693 = relay.var("var_693", dtype = "bool", shape = (896,))#candidate|693|(896,)|var|bool
var_694 = relay.var("var_694", dtype = "int8", shape = (1568,))#candidate|694|(1568,)|var|int8
output = func_690(var_691,var_692,var_693,var_694,)
func_695 = relay.Function([var_691,var_692,var_693,var_694,], output)
mutated_mod['func_695'] = func_695
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1237 = relay.var("var_1237", dtype = "int64", shape = (5, 13, 13))#candidate|1237|(5, 13, 13)|var|int64
const_1238 = relay.const([[[8,10,-10,-6,-5,-1,-1,-10,-5,-6,-1,-8,3],[6,8,7,-7,9,-10,-2,-1,6,1,-10,-10,-7],[-9,7,-10,3,-6,3,9,-1,-1,8,9,8,1],[-8,-6,3,1,5,-4,9,-3,1,8,-1,-8,-3],[-4,-7,-8,-7,2,-10,-9,-6,5,2,10,8,-9],[7,1,-4,-8,7,8,10,3,4,-5,6,6,8],[3,-1,8,-8,7,-1,5,-3,-3,4,3,9,-8],[9,-4,7,-2,10,8,6,-1,2,-6,-8,8,-4],[-10,10,-1,2,-4,3,-9,6,10,-3,-3,-7,-10],[8,7,-8,7,6,6,3,7,8,8,3,9,9],[1,-1,-8,-8,10,-5,5,-5,9,3,-4,4,-8],[-10,-5,9,2,8,6,9,1,3,5,-8,-7,-2],[3,-5,-5,6,-3,-7,-4,8,-8,-7,1,6,1]],[[-10,-5,9,10,-7,-10,-4,-9,-9,5,-6,-2,-5],[-7,9,-5,6,3,5,1,8,-4,-4,5,-7,-1],[-7,-8,-8,-3,2,-7,-5,-6,-4,2,-8,-6,3],[-10,-4,-5,-5,-5,-7,1,-6,8,9,-4,2,-2],[-6,5,-10,10,-5,8,8,-7,2,6,6,-9,-9],[5,3,-2,-8,8,3,5,-3,-9,6,9,4,6],[-1,-5,10,-4,9,-1,4,-8,-7,4,-6,4,7],[-10,9,10,-2,2,7,6,3,-5,-7,1,-6,4],[8,-5,-1,5,-2,-2,2,-6,-2,-4,-10,-2,-4],[10,10,3,4,-2,-5,-5,-3,-1,4,1,2,3],[-6,10,7,-9,6,4,2,-4,-2,5,-9,10,6],[9,7,-1,-6,1,10,2,-4,5,10,-2,-10,8],[3,-1,9,6,-2,9,7,1,1,-5,-8,10,10]],[[10,9,1,6,-1,-2,3,4,-1,-3,10,4,9],[-6,1,1,7,-1,-1,10,4,-9,-7,-8,-3,1],[-4,-9,-8,-2,-2,-2,4,-9,2,5,3,-4,6],[-1,2,-4,-8,9,-9,-6,-7,-10,-4,4,-10,4],[2,6,-10,6,-10,8,3,-7,-2,3,-3,-10,4],[3,-2,7,-4,3,1,-6,10,-10,-5,7,-10,-7],[-7,-10,-9,-5,9,-7,7,5,-9,-1,-6,6,-8],[9,5,-2,2,-3,4,-4,-2,-6,-2,6,-1,-2],[8,8,-1,5,-2,-10,1,-7,-3,-10,3,3,6],[-5,-8,5,5,3,2,-1,9,9,5,6,7,3],[3,-5,9,7,-9,5,-8,9,8,-6,-1,8,-3],[8,-2,9,-8,4,4,-7,6,6,-10,-5,5,7],[6,-6,2,8,4,3,4,9,1,-1,-8,10,-2]],[[-8,6,-2,3,-3,1,-2,1,-7,3,2,-4,10],[2,9,4,-8,5,5,10,-4,1,4,-9,6,-6],[5,-3,-1,-4,-6,8,-1,6,10,5,-4,7,-8],[-8,-8,5,6,8,-1,-8,1,1,-8,7,2,9],[6,-6,2,-1,10,-6,1,4,6,-1,7,-8,-10],[10,-5,-7,-6,-7,7,-1,-3,-3,-2,-8,-8,-7],[10,9,-10,-1,-9,10,-1,4,-7,5,3,-4,-5],[-5,-1,8,-10,1,-6,-7,-1,8,3,10,-6,-10],[2,-6,-8,2,5,-1,6,7,2,-9,-10,-5,-9],[-5,-1,-6,8,-2,4,6,-5,-6,-8,-5,6,3],[10,-9,4,-6,8,8,5,-2,5,10,-4,-10,-1],[3,8,-1,6,9,-5,-7,-10,-7,-6,-6,7,-10],[6,3,5,-3,2,1,-6,-9,7,2,-2,4,9]],[[8,8,9,8,-1,8,7,-10,9,1,6,6,7],[10,6,3,-7,4,7,8,6,-2,7,3,9,-5],[-4,-7,-7,-2,6,8,6,-9,-3,-1,-4,-4,-8],[-6,1,-3,10,-5,5,-1,5,-4,1,-6,-10,-5],[-1,-5,6,-7,3,-1,8,-2,-3,5,4,9,-1],[-2,-1,7,-8,2,-4,-2,-6,9,-6,8,4,7],[3,3,-10,-6,4,4,6,7,-2,-6,-9,-6,-8],[6,10,-9,-9,6,9,-10,-7,-6,-8,-4,3,3],[-7,-9,-3,-6,-8,5,-1,-7,-5,5,1,7,-6],[2,-3,1,3,-4,7,-1,-6,4,-7,8,-8,-4],[-6,-8,1,2,-4,3,-7,6,-8,-8,-5,-4,3],[-6,8,-10,2,7,-8,7,-5,1,-9,5,6,-6],[8,-3,3,-2,1,5,9,-5,4,9,2,3,-9]]], dtype = "int64")#candidate|1238|(5, 13, 13)|const|int64
bop_1239 = relay.greater_equal(var_1237.astype('bool'), relay.reshape(const_1238.astype('bool'), relay.shape_of(var_1237))) # shape=(5, 13, 13)
func_690_call = mod.get_global_var('func_690')
func_695_call = mutated_mod.get_global_var('func_695')
const_1254 = relay.const([4,4,5,6,6,-3,8,-4,5,-1,-2,-7,1,-7,5,8,7,-3,-9,2,-10,4,7,2,1,-10,-2,-2,-6,2,5,3,1,6,4,-7,-3,4,-10,-3,-2,4,9,-6,4,-8,-9,5,-6,-10,-9,7,-10,3,1,-1,-8,-6,-10,5], dtype = "uint32")#candidate|1254|(60,)|const|uint32
var_1255 = relay.var("var_1255", dtype = "float32", shape = (180,))#candidate|1255|(180,)|var|float32
const_1256 = relay.const([True,False,False,True,True,True,False,True,True,False,True,False,True,True,False,False,True,False,True,False,True,True,True,False,False,False,True,True,False,True,True,True,True,False,False,False,True,False,False,False,False,True,False,False,True,True,False,False,True,True,True,True,False,False,True,False,False,False,False,False,True,True,False,False,True,False,True,True,True,True,True,True,False,False,True,True,True,True,False,False,True,True,True,True,True,True,False,False,True,False,False,True,True,False,True,True,True,False,False,False,True,True,True,False,True,True,True,False,False,True,True,True,False,False,True,False,True,True,False,True,True,False,False,False,True,True,True,False,False,True,False,True,True,True,True,False,False,True,True,True,False,False,False,True,False,True,True,False,False,True,True,True,True,True,False,False,False,True,False,False,True,False,False,False,False,True,False,False,False,True,True,True,True,False,False,False,True,True,False,False,False,True,True,True,False,True,False,False,True,False,True,False,True,True,False,True,False,False,True,True,False,True,False,True,True,False,True,False,True,True,False,True,False,False,False,False,True,False,True,False,True,False,False,False,True,False,True,True,True,False,False,True,True,False,False,False,False,False,True,True,True,True,False,False,True,True,False,True,True,True,True,False,True,False,False,False,False,True,False,True,False,False,False,True,True,True,False,True,True,True,True,False,False,True,False,False,False,True,True,False,False,False,False,False,False,True,False,True,False,False,False,False,True,True,False,False,False,False,True,True,True,False,True,True,False,False,True,False,True,False,False,True,True,True,True,True,False,False,False,False,False,True,True,True,False,True,True,False,True,True,True,False,True,False,True,True,False,True,False,True,True,False,True,False,True,False,False,True,False,False,False,True,True,True,False,True,False,False,True,True,True,False,True,False,True,False,False,True,True,False,True,True,False,False,True,False,False,True,True,True,False,True,False,True,False,False,True,False,False,False,True,True,True,False,False,False,True,False,True,False,False,False,True,False,False,True,False,True,False,False,False,False,True,False,False,False,False,True,False,True,True,False,False,False,False,False,False,True,False,False,False,False,False,True,True,True,False,True,False,True,True,False,True,True,False,True,True,False,False,True,True,False,True,False,False,False,False,True,True,True,True,True,True,True,True,False,False,True,False,False,False,True,False,False,False,False,True,True,True,False,True,False,False,False,False,False,False,True,True,False,False,False,True,True,False,False,False,False,False,False,True,False,True,True,False,False,False,False,True,True,False,False,True,False,True,False,False,True,True,False,True,True,False,True,False,False,True,False,True,True,False,False,False,False,True,False,False,True,False,True,False,False,False,False,False,True,False,True,False,True,True,False,False,True,True,False,False,False,True,True,False,True,True,False,True,False,False,True,False,True,True,False,True,True,False,False,False,False,True,False,True,False,False,True,True,True,False,True,False,True,False,False,False,True,False,False,False,False,True,False,True,False,False,True,True,True,True,True,True,False,False,True,False,False,False,True,False,False,True,False,True,True,False,False,True,False,False,True,False,True,True,False,False,True,True,True,False,False,True,False,False,True,True,False,True,True,True,True,False,False,True,True,False,True,True,True,True,True,False,False,True,True,False,True,False,True,False,True,True,True,True,True,False,False,True,False,True,False,True,True,True,True,True,True,False,False,False,False,False,False,False,True,True,False,False,True,True,False,False,False,False,True,True,False,True,False,False,True,False,False,False,True,True,True,False,True,False,False,True,False,False,True,True,True,True,True,True,False,True,True,False,True,True,True,False,False,True,False,True,False,False,False,True,True,True,False,True,True,False,False,True,True,False,False,False,True,True,True,False,True,True,False,False,False,False,False,False,True,True,False,True,True,False,True,True,True,True,False,True,True,False,False,False,False,True,True,False,False,False,False,True,True,False,False,True,False,False,False,False,True,False,True,True,False,False,False,True,True,False,False,True,False,True,True,True,False,False,True,False,True,True,False,False,True,False,False,False,False,False,False,False,False,True,True,False,False,True,True,True,True,False,False,True,True,False,False,True,False,True,True,True,False,True,False,False,True,False,False,False,False,False,False,False,True,True,False,True,False,True,True,True,True,True,False,False,True,True,True,False,False,True,True,True,False,True,True,False,True,True,False,True,True,False,True,False,True], dtype = "bool")#candidate|1256|(896,)|const|bool
var_1257 = relay.var("var_1257", dtype = "int8", shape = (1568,))#candidate|1257|(1568,)|var|int8
call_1253 = relay.TupleGetItem(func_690_call(relay.reshape(const_1254.astype('uint32'), [2, 2, 15]), relay.reshape(var_1255.astype('float32'), [180,]), relay.reshape(const_1256.astype('bool'), [896,]), relay.reshape(var_1257.astype('int8'), [1568,]), ), 0)
call_1258 = relay.TupleGetItem(func_695_call(relay.reshape(const_1254.astype('uint32'), [2, 2, 15]), relay.reshape(var_1255.astype('float32'), [180,]), relay.reshape(const_1256.astype('bool'), [896,]), relay.reshape(var_1257.astype('int8'), [1568,]), ), 0)
output = relay.Tuple([bop_1239,call_1253,const_1254,var_1255,const_1256,var_1257,])
output2 = relay.Tuple([bop_1239,call_1258,const_1254,var_1255,const_1256,var_1257,])
func_1259 = relay.Function([var_1237,var_1255,var_1257,], output)
mod['func_1259'] = func_1259
mod = relay.transform.InferType()(mod)
var_1260 = relay.var("var_1260", dtype = "int64", shape = (5, 13, 13))#candidate|1260|(5, 13, 13)|var|int64
var_1261 = relay.var("var_1261", dtype = "float32", shape = (180,))#candidate|1261|(180,)|var|float32
var_1262 = relay.var("var_1262", dtype = "int8", shape = (1568,))#candidate|1262|(1568,)|var|int8
output = func_1259(var_1260,var_1261,var_1262,)
func_1263 = relay.Function([var_1260,var_1261,var_1262,], output)
mutated_mod['func_1263'] = func_1263
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1640 = relay.var("var_1640", dtype = "float32", shape = (15, 1, 14))#candidate|1640|(15, 1, 14)|var|float32
var_1641 = relay.var("var_1641", dtype = "float32", shape = (15, 3, 14))#candidate|1641|(15, 3, 14)|var|float32
bop_1642 = relay.greater(var_1640.astype('bool'), var_1641.astype('bool')) # shape=(15, 3, 14)
output = bop_1642
output2 = bop_1642
func_1652 = relay.Function([var_1640,var_1641,], output)
mod['func_1652'] = func_1652
mod = relay.transform.InferType()(mod)
var_1653 = relay.var("var_1653", dtype = "float32", shape = (15, 1, 14))#candidate|1653|(15, 1, 14)|var|float32
var_1654 = relay.var("var_1654", dtype = "float32", shape = (15, 3, 14))#candidate|1654|(15, 3, 14)|var|float32
output = func_1652(var_1653,var_1654,)
func_1655 = relay.Function([var_1653,var_1654,], output)
mutated_mod['func_1655'] = func_1655
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2199 = relay.var("var_2199", dtype = "float64", shape = (12, 2, 10))#candidate|2199|(12, 2, 10)|var|float64
uop_2200 = relay.cosh(var_2199.astype('float64')) # shape=(12, 2, 10)
output = uop_2200
output2 = uop_2200
func_2208 = relay.Function([var_2199,], output)
mod['func_2208'] = func_2208
mod = relay.transform.InferType()(mod)
mutated_mod['func_2208'] = func_2208
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2209 = relay.var("var_2209", dtype = "float64", shape = (12, 2, 10))#candidate|2209|(12, 2, 10)|var|float64
func_2208_call = mutated_mod.get_global_var('func_2208')
call_2210 = func_2208_call(var_2209)
output = call_2210
func_2211 = relay.Function([var_2209], output)
mutated_mod['func_2211'] = func_2211
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2330 = relay.const(-8, dtype = "int16")#candidate|2330|()|const|int16
var_2331 = relay.var("var_2331", dtype = "int16", shape = (2, 13, 1))#candidate|2331|(2, 13, 1)|var|int16
bop_2332 = relay.bitwise_or(const_2330.astype('int16'), var_2331.astype('int16')) # shape=(2, 13, 1)
func_375_call = mod.get_global_var('func_375')
func_378_call = mutated_mod.get_global_var('func_378')
const_2342 = relay.const([[3.490244,6.796578],[-7.593558,8.695303],[-0.376618,4.245866],[1.940899,-2.731545],[-8.161549,3.204215],[8.877943,-7.116216],[-2.788174,-9.513488],[-6.573203,6.976046],[-6.674476,-3.306621],[7.239801,-2.714747],[0.204242,8.064572],[3.258057,5.936606],[-0.350350,-8.383173],[-1.740677,-7.410038],[-5.011794,8.942275],[-4.298795,-9.779758],[-2.714472,-3.249173],[6.045165,3.849845],[-3.596798,2.282689],[-5.393131,-8.387713],[3.575581,-4.224249],[8.387239,-9.555350],[-2.249979,-2.754335],[-8.965839,6.590398],[8.783179,9.222407],[-1.083491,-4.637152],[7.371511,-9.758745],[-5.217663,-3.150130],[-5.921836,1.301166],[3.536577,7.947174],[-9.918770,5.784338],[0.856886,3.378542],[-1.014392,6.427266],[4.223549,1.218739],[0.734334,0.408365],[-5.308143,9.246220],[-4.159750,8.925363],[-0.237620,9.398626],[-2.860941,-3.858367],[-3.731383,7.803377],[-2.430266,7.524731],[-8.975885,-2.854833],[4.641794,2.877686],[7.272424,-9.696905],[2.211978,-5.876942],[-7.571891,-7.108318],[-0.971463,-5.459629],[-8.124757,2.080296],[-1.382687,4.337530],[3.804397,-0.142026],[5.103227,8.900058],[-2.619800,-7.528596],[9.420273,-9.195871],[2.263672,-5.667330],[0.031328,-7.786503],[-8.549149,-4.349858],[-3.564432,7.405770],[1.966619,-0.365757],[8.511151,8.214135],[0.242569,-6.184473],[-9.534998,9.796207],[9.618674,2.305338],[-6.835074,4.719692],[1.750627,-4.321806],[0.612592,-2.792994],[5.787537,5.836286],[-1.999453,9.521322],[-0.065521,-3.160682],[-5.228770,-9.512274],[1.055880,-8.873381],[3.343371,2.828001],[9.453796,2.482918],[8.157988,8.076705],[-2.005817,-0.983710],[5.317160,7.573429],[0.391171,5.566287],[7.025855,3.147019],[6.148148,-4.479142],[3.376225,-9.519665],[7.168289,1.905529],[1.972556,-6.788286],[1.337248,-1.637905],[-9.107668,3.901469],[9.073839,9.150688],[-0.283693,5.747665],[-2.002548,4.408299],[5.968246,-9.672614],[9.817636,-1.168091],[-5.639373,-8.536392],[6.459967,-5.785212],[-0.189237,2.943049],[-4.939702,-4.757894],[4.460779,1.830845],[-5.266080,-1.814747],[-7.212435,-1.132549],[-9.491468,-0.219692],[0.805532,1.974536],[4.702700,-3.128020],[1.647240,0.536806],[-7.939598,-9.435975],[9.578779,8.372732],[-7.466059,-7.293272],[-6.480309,-0.713208],[7.423064,1.416060],[-9.129424,9.561439],[5.422146,4.875497],[4.857374,-3.403191],[3.822979,1.191608],[-3.653675,-1.469137],[-9.886907,5.053836],[9.126935,-7.657182],[-0.605590,-6.550964],[-3.019851,-9.757793],[4.911837,-4.865717],[-1.611894,5.718733],[3.092339,1.724800],[6.685917,2.467183],[-4.529121,7.104050],[-3.006602,-4.721682],[3.659174,9.984159],[-5.940734,4.096104],[-9.156852,-1.417251],[2.169799,-8.759056],[-4.887868,-6.211117],[1.165426,-2.698104],[3.040384,3.891811],[2.781841,-2.747318],[-1.414703,-9.476405],[-6.125678,2.443147],[3.216873,1.366507],[6.481576,0.318279],[9.344326,7.049525],[5.820772,-6.198327],[5.909290,7.989909],[6.254317,-5.148885],[9.757312,-3.593010],[-0.015799,-5.905828],[1.596152,-6.640334],[9.399017,4.813626],[-3.123808,3.854357],[-5.763054,-6.540691],[-3.784536,-3.618815],[6.157050,8.012942],[0.450115,-5.054183],[5.696962,9.506788],[0.026855,4.187292],[7.348171,8.320304],[-7.820831,-6.046588],[7.831746,-3.874817],[-9.876477,4.188847],[4.563442,-0.131606],[8.831148,3.858863],[-0.502160,8.535926],[-5.257503,-6.245763],[9.753973,7.706688],[6.800285,-9.043625],[-5.147898,-6.516913],[7.075256,0.052631],[-9.937625,0.581695],[-9.216107,2.393845],[4.663637,-4.156929],[0.975934,-8.082293],[8.408661,-9.897628],[5.376543,9.638276],[-5.793763,-9.439615],[7.604973,-1.966044],[6.233876,1.153881],[-3.914135,-4.677348],[-4.035103,-7.955201],[-2.565166,-7.428925],[-0.450852,-6.977417],[-8.883289,-4.991989],[7.407424,-7.373752],[-9.926916,-4.117989],[0.723118,3.010717],[-3.321267,9.304723],[0.149248,8.800608],[-6.824698,8.002991],[-3.812506,-5.838152],[9.886037,2.699609],[8.757722,1.789549],[4.315866,-3.851079],[-9.066475,-7.931314],[2.406001,3.476563],[5.646913,-8.699299],[-9.669090,4.739309],[5.551204,8.399840],[-2.695291,4.945156],[0.837520,9.703299],[6.606282,7.323382],[7.904357,-8.359538],[1.393280,2.221341],[-9.721617,7.100615],[9.331941,-2.153804],[-0.562445,8.627309],[-0.613313,9.245666],[-2.571391,-7.478808],[-9.027304,7.018927],[-2.850205,-2.321089],[9.061623,-3.679597],[-1.186885,-4.439833],[-1.642172,-0.546745],[2.750103,3.653136],[0.082098,5.901540],[3.007179,2.621320],[3.071754,-6.858120],[-4.917979,8.320279],[-7.230394,-2.700925],[6.911412,9.262454],[5.140474,9.621320],[8.192526,-9.159317],[0.642001,-2.094986],[-9.873380,-1.669425],[-7.130899,9.921105],[7.446432,-7.427646],[-3.526092,-2.167967],[-7.249101,-3.445274],[-8.932894,-5.260015],[-2.271766,-5.680312],[-8.018703,2.504238],[-7.470216,-3.729606],[-5.233921,6.003935],[-4.127147,0.923599],[-9.120514,4.843453],[6.220417,-1.918051],[0.133869,-6.673308],[-0.535711,0.060963],[2.940095,2.537481],[-6.527276,8.861751],[5.117828,-6.446146],[-1.313926,-6.697842],[-6.890167,0.307749],[1.073965,0.414442],[-9.725795,5.686639],[-1.278754,9.208070],[1.982196,7.375987],[-3.137823,-8.292407],[5.023765,-3.157614],[-3.581666,3.347687],[-5.769399,4.662286],[-7.087339,-3.397424],[-2.544992,0.467289],[-8.647211,-7.294079],[6.729623,6.469318],[-3.591468,1.365934],[-4.177343,-3.453160],[8.924727,7.411146],[-0.261212,5.200531],[3.975799,-4.040267],[9.662318,-7.545382],[-8.961474,2.961070],[-1.015111,-7.143927],[-6.998556,0.060008],[5.789263,-5.223479],[8.341330,-5.814764],[-6.785565,-2.011529],[5.171356,5.775113],[1.749512,-2.793827],[-1.789095,6.982074],[-4.656888,-6.712755],[-9.625941,1.981601],[7.189826,-9.541786],[-2.080013,-2.734881],[-3.376741,-5.555189],[4.934754,1.827127],[-4.267264,3.087866],[1.256690,8.032998],[-4.379153,4.272232],[9.962353,-3.807196],[-5.627718,6.528505],[5.671997,1.858996],[1.776117,8.684080],[9.283861,5.229352],[-9.923695,-4.359957],[3.864604,8.588944],[3.409656,-8.260456],[1.438769,1.527620],[6.483016,-5.421129],[3.184993,8.149683],[-6.779562,1.021801],[5.909341,2.014604],[8.472441,4.531876],[6.976881,-9.371427],[5.441865,-4.951020],[8.662943,-7.629792],[-0.635536,2.449833],[-2.610749,-1.868131],[0.003136,-5.927305],[-4.987680,-3.695926],[-5.405236,8.366284],[-1.231194,-7.127826],[-2.071309,3.272670],[5.017154,7.332370],[-1.787741,1.873619],[3.446335,5.199045],[2.528301,5.795403],[8.737173,-7.892530],[9.601722,-2.777443],[3.226315,-8.251970],[9.900260,-0.553103],[4.670417,-4.173029],[-5.860314,6.599377],[-6.681988,9.735010],[-6.905106,9.553890],[-3.742939,6.563652],[7.955065,-1.740364],[5.315671,0.420389],[-7.667954,8.542199],[1.344568,0.819106],[4.411904,7.537264],[-4.006871,5.633882],[1.517451,-9.036694],[-4.366268,1.961438],[5.234469,9.306672],[-2.244848,6.777224],[-7.502119,1.474191],[6.889116,9.043218],[8.065130,-7.370312],[5.396370,-8.130344],[-8.237754,4.649634],[6.153068,3.613114],[-9.961867,3.492510],[5.512999,3.749065],[5.632828,0.489111],[8.367615,0.829651],[7.770220,-0.912974],[5.111847,6.502344],[-5.301031,8.960446],[1.213946,-3.916856],[4.981934,0.370077],[0.999715,-5.151199],[4.795583,9.356191],[-4.477314,0.513940],[-3.366146,6.591410],[-0.165688,4.205256],[1.085189,-1.307534],[4.952109,-2.215891],[-1.155598,4.721540],[-9.555538,-6.408110],[6.707555,-2.663303],[-5.666493,3.370985],[-7.754457,8.501576],[2.916986,7.816733],[5.055292,-9.561723],[-0.671021,5.508362],[-3.510951,-9.445956],[-2.157306,-4.242569],[-2.996623,3.507485],[-3.191386,1.332185],[8.592530,8.867002],[-7.470796,2.033781],[2.045795,-1.949202],[-1.215843,-5.283633],[2.849991,4.612392],[-4.871446,0.405811],[9.290712,8.767770],[-2.212942,-1.202399],[3.814603,-1.871134],[-3.537216,5.200685],[9.196306,3.488388],[7.382035,-4.889564],[6.240517,-1.044415],[1.514741,-9.252399],[3.860417,-0.567890],[7.730850,4.415755],[8.940944,-3.552247],[-6.267945,6.402830],[7.085271,5.150587],[-0.128241,1.426753],[-1.092316,9.645019],[-5.779700,-5.580701],[-8.971870,6.659992],[9.585718,-1.094829],[-1.325182,-5.982357],[0.777518,4.599905],[-1.005113,4.293349],[-1.669516,-9.021499],[7.498275,9.433919],[-9.155580,8.189324],[-8.623473,-8.256090],[4.187842,-9.215789],[7.761631,-3.019664],[-0.786419,9.539268],[8.959957,-3.189467],[-0.587879,-3.132048],[-2.496142,7.547129],[3.997581,3.955213],[4.678389,2.635762],[2.522056,-2.781075],[-5.865191,4.889372],[-3.839749,6.286801],[9.310514,-9.458287],[7.075630,5.220248],[-0.980132,-0.171094],[4.953218,2.636763],[1.673717,-8.136325],[8.782977,6.473001],[1.496977,-1.697345],[7.933531,4.031808],[7.545479,-9.834339],[-5.653974,8.443189],[-8.169674,-0.402398],[7.902141,-7.800817],[-1.599907,1.908274],[-9.042596,9.876326],[4.095037,9.932799],[-7.349148,-7.441026],[-1.036265,-6.440064],[-8.212325,9.648229],[5.200273,3.019794],[-7.650881,8.525153],[-4.392048,-3.448683],[0.200514,-5.423793],[6.671196,8.074767],[2.663377,-1.858259],[9.125181,-8.420456],[-1.379542,-5.128151],[-4.655972,-8.919193],[-1.570974,4.815563],[2.566383,2.767354],[-6.301594,8.140669],[6.240965,3.176252],[-3.282338,2.754845],[-1.031918,-5.548501],[3.398384,-8.203804],[-7.560011,-1.023231],[-1.714012,3.677804],[0.727315,-1.014421],[-4.944010,-5.832379],[-3.982479,-4.610777],[6.410784,-4.881880],[-3.547810,-2.230165],[-6.826280,8.629520],[2.141246,1.904329],[0.585713,6.010769],[1.837181,-7.806100],[-1.773830,3.994066],[-5.007220,7.654125],[2.631633,4.244839],[-8.281171,-0.536155],[-2.926818,6.561463],[0.298612,0.583257],[7.517007,-4.737465],[-1.293277,0.910214],[9.575122,-4.620520],[-5.203241,4.952606],[5.909035,2.902604],[-8.669179,-0.781342],[3.097318,-1.254957],[-9.524774,-2.288004],[7.307549,-3.187012],[4.467772,-3.632630],[8.545791,5.278964],[-8.480313,0.525518],[8.556889,-3.848804],[-8.911094,9.733731],[-3.437721,3.973409],[8.706296,9.384370],[-5.476394,9.301638],[6.366800,-0.955893],[-7.235125,-4.898791],[-9.387214,-2.371209],[3.828019,3.773236],[-1.225626,7.012978],[-0.030306,4.601357],[-9.022381,-8.974479],[5.201777,8.050862],[2.589978,3.278217],[0.766793,9.788481],[5.971173,1.634061],[-8.152002,0.799752],[7.411380,7.504708],[2.543894,-1.773151],[2.087928,-4.824285],[-1.738251,1.320249],[2.963599,7.617872],[3.779688,-2.289829],[-1.610853,9.365835],[-9.269347,8.077184],[4.526134,7.960694],[-5.210415,5.220830],[7.555352,-7.996012],[9.052144,6.725191],[-2.992395,6.292963],[8.390960,-4.209973],[9.483113,-6.586297],[-3.300188,-4.063821],[4.780935,-5.852607],[7.861209,6.746034],[8.820847,-2.458477],[-6.982528,7.457238],[-7.726542,-2.968588],[-5.743182,6.096670],[-0.339229,1.313849],[-1.370304,-2.479368],[-0.295572,0.701901],[-4.882415,-7.657667],[-6.354425,-4.137104],[-1.308973,5.520870],[-6.996798,3.735964],[-6.346302,2.728857],[-8.392332,-4.948769],[-1.553949,-8.776412],[4.400723,-2.186002],[9.517506,-8.054129],[6.022961,-0.498587],[-5.418907,-9.752996],[0.857420,-6.856080],[-5.310175,-9.202107],[-4.165208,1.958852],[8.731530,8.341715],[9.894100,1.781365],[-5.557929,-5.480707],[-1.796106,-9.154651],[-1.990642,-0.917545],[-9.297564,-8.941222],[-2.403281,2.148959],[6.722319,0.144970],[4.986301,7.302739],[-0.723429,2.008080],[-6.812412,-1.859782],[-8.082690,-6.421708],[6.358307,-9.040759],[6.848988,-5.917647],[4.007306,-8.750067],[6.642797,9.096640],[8.980120,4.865860],[7.068889,-9.060348],[1.110385,1.080420],[5.949465,-3.108062],[-6.408099,-4.841410],[1.230741,4.404633],[7.987177,6.175026],[3.344075,0.606228],[-6.683321,-0.382820],[5.348165,7.923940],[0.112721,-0.441449],[-3.103457,3.277389],[9.512170,-8.911961],[-0.772376,2.268471],[-9.620874,-6.658200],[7.702436,-0.391749],[3.114017,-1.069186],[5.628707,5.879713],[-8.221805,-7.434651],[-5.688805,0.548449],[4.609746,8.372053],[8.406238,1.725350],[5.181527,2.280695],[5.604089,-1.133519],[-7.852459,3.884097],[7.263684,-7.145115],[-1.915260,-3.828040],[-5.967530,-5.302818],[-8.593970,0.279965],[-5.100419,4.465285],[3.399545,6.097162],[-6.420884,5.260452],[-7.103863,-1.420408],[8.985524,8.638274],[7.413063,-4.716108],[5.687529,-3.613417],[-9.526531,3.161778],[-2.140870,5.101790],[7.428986,0.229372],[-4.261568,-3.849482],[7.778769,-2.785695],[5.728752,1.036334],[-9.133924,-0.710014],[-9.997951,2.205942],[-6.168559,-8.865304],[7.887919,-8.069436],[-4.636622,-1.834694],[-8.019215,3.242996],[7.090671,-6.956258],[5.760434,-6.737856],[-1.729063,0.303371],[3.484379,2.691346],[7.158408,-4.193536],[8.834615,3.963740],[-2.962631,3.803953],[-7.160150,2.988817],[-1.485801,-7.273850],[0.306834,8.821598],[8.825259,-0.864892],[9.792660,-4.310844],[8.377634,0.706865],[-9.741697,-0.482222],[-1.542233,4.692574],[-9.917350,8.785159],[2.309653,-7.630716],[-5.658008,-9.353034],[-0.406104,-0.223734],[-4.865646,-1.870309],[5.138746,0.749994],[-1.579873,6.077244],[5.490850,5.238655],[3.275470,-9.489504],[-4.816244,2.017777],[3.937094,-2.131757],[-9.495249,5.931939],[-6.262029,7.706492],[-6.933267,0.882779],[-4.750576,0.724539],[9.935381,-1.436053],[2.057896,6.140651],[9.602666,-4.260278],[-7.527644,5.385973],[0.414181,-1.761475],[-1.688199,-0.678025],[-8.494855,-4.833738],[-7.411416,-6.359304],[-7.154195,-0.520414],[5.632939,-1.640697],[-9.563533,3.774998],[1.019863,2.681504],[-9.786256,-9.939602],[3.193410,7.148821],[-2.061061,3.978974],[6.608941,4.702022],[-9.186031,-6.285447],[3.032616,-8.239884],[7.785663,3.708259],[-9.223266,-4.642816],[-0.867589,-9.717658],[2.673128,9.374245],[4.372046,-7.022450],[-5.517376,-6.032242],[0.834301,-5.267966],[0.157339,-5.083877],[8.714666,-4.892053],[-8.998890,-2.014891],[2.318068,1.567302],[-7.765438,7.472309],[7.547372,-8.603255],[4.998912,-2.161236],[2.228769,7.111640],[9.351545,-1.006694],[2.237428,2.324856],[9.618814,-4.695258],[-7.355569,5.772849],[-2.472670,-1.388056],[-5.034443,4.112473],[5.705359,-7.069157],[4.582782,-4.564155],[0.396047,6.054850],[7.989563,-5.282264],[-2.300288,9.628771],[-4.572824,4.999734],[8.819957,-6.010398],[-0.742008,5.254703],[9.746669,1.228791],[-6.574336,-9.175453],[-1.761589,-8.765091],[-8.238944,-2.819179],[-4.907825,7.185719],[-6.516168,0.406220],[-7.069814,7.032679],[-1.040247,-3.704615],[-8.210293,-0.006728],[5.045448,-0.982202],[-5.502192,0.469321],[1.866383,2.008585],[-0.510404,2.923937],[5.311661,-8.389501],[-3.746152,-0.684678],[9.638335,9.626295],[-0.452192,-2.422537],[-1.432561,8.751198],[0.379020,0.840060],[-6.228285,-1.803702],[5.301807,2.984453],[9.740881,-5.078571],[3.739790,-2.583246],[1.014099,-7.378925],[1.017261,-2.935648],[2.170263,-7.882411],[-6.730612,-8.616723],[-5.508628,3.448206],[-5.329432,-9.979444],[3.839346,2.498773],[7.196017,4.615763],[6.455803,2.301471],[-7.579916,-4.186675],[5.231304,-6.652787],[-4.985142,5.405269],[-3.923474,-7.107902],[2.750356,-1.083808],[6.748850,-6.490387],[2.153725,-6.110909],[2.265534,3.018083],[3.667617,-6.298211],[-9.649685,-8.435759],[4.946310,6.131950],[8.534470,-0.338788],[-5.009832,5.285890],[-9.242464,-8.954851],[3.618004,9.342771],[-1.316235,-1.295037],[-7.988979,8.276783],[0.389231,-0.756457],[3.493444,-7.999904],[1.870775,7.172736],[0.209867,-8.059841],[-9.997543,5.240171],[0.403476,0.443244],[8.075209,8.743204],[-1.114769,-6.156104],[-9.426960,-2.472242],[-3.321940,-7.482087],[1.590354,5.034641],[-1.809415,-1.670999],[4.601578,-0.955211],[-2.489003,-2.970254],[3.894701,-6.153866],[-0.012241,-2.505441],[8.349650,-3.181415],[1.157235,5.989624],[9.182491,-6.981216],[-7.939868,-0.970354],[-3.926159,-5.828595],[-3.609003,1.942232],[-7.587218,4.242909],[-3.933000,-8.869705],[-4.999119,-2.941922],[6.041332,-5.609386],[-7.508115,5.872286],[-3.575032,-7.375240],[-2.350797,4.260801],[-2.406702,0.859531],[-6.349041,2.350077],[-3.563210,-1.560318],[0.919955,-6.144537],[8.805356,7.849467],[0.433701,-8.356398],[-2.857988,9.957548],[-2.078994,-8.041810],[8.401175,3.960930],[-6.813278,-9.548309],[-8.535867,-4.960075],[8.431477,6.268678],[7.420637,3.961074],[7.665990,-9.277820],[-1.842960,-1.631593],[7.763750,2.059068],[-5.383663,-8.204279],[-0.063060,2.978152],[-2.444491,-4.924790],[8.799452,-0.856341],[-8.045262,7.070040],[3.368388,1.361223],[3.194302,-7.542333],[-2.643749,0.889373],[2.903242,-3.972450],[3.750312,-4.117433],[0.323668,9.865811],[-8.918807,7.677618],[3.541669,-9.698226],[6.009448,9.160105],[-4.252387,5.695067],[2.427801,7.167448],[-4.554712,-0.677879],[-3.644343,1.818312],[9.236776,-7.096293],[-8.847908,-6.484081],[-3.951650,5.536490],[8.290989,2.643804],[-2.994519,-1.432480],[5.626642,-8.854074],[6.350782,7.969069],[-6.143635,1.146759],[-1.473110,0.499755],[-6.068187,-1.987076],[4.146252,-6.859440],[-0.816452,-0.846011],[-7.900673,9.249765],[-3.140126,4.053176],[-7.771226,4.492348],[-9.070831,5.129156],[-6.302997,5.122105],[-9.711567,-5.454218],[1.720238,-9.710679],[-9.079215,8.643346],[-5.919144,-1.779792],[-6.387649,-8.209573],[7.285920,9.779942],[7.653779,-5.322795],[-6.686606,-8.078665],[3.903448,-9.186892],[4.263367,1.222459],[9.534095,-6.760629],[5.269534,-2.908185],[-3.414671,-7.131299],[5.332812,9.747837],[-6.301736,-3.351554],[-7.421578,-9.096868],[4.920540,-4.494740],[5.521552,-2.561189],[-7.514440,-1.196408],[-3.139417,-6.056813],[-0.390555,-4.265703],[-3.756752,-4.574242],[6.264886,6.624970],[1.048619,5.879473],[-1.391706,2.273692],[6.235105,-4.234534],[-2.509564,9.475151],[-8.630515,5.648538],[2.673750,-1.082599],[-4.384882,-2.427546],[3.341147,7.688600],[8.368450,-4.540414],[-6.846159,-8.491032],[3.051679,-0.407984],[8.116764,-8.271917],[3.606873,-2.546705],[8.541623,-1.532428],[2.308686,2.344910],[9.283763,3.799311],[-1.089214,-2.497987],[9.912660,-4.567849],[-9.756521,-6.896933],[2.964481,6.536893],[4.333033,0.496286],[-6.425316,-6.102286],[-3.155481,-1.487213],[-1.302682,6.793801],[0.002517,5.736167],[-9.483784,-5.145334],[-9.584111,-7.063214],[9.444550,-4.661586],[-7.003045,-0.356709],[-2.089486,-6.182034],[-1.142285,-5.039222],[3.065620,1.089252],[5.543582,2.529249],[7.641376,-4.056578],[9.332675,5.223135],[-2.120925,2.349425],[5.073649,3.071127],[-1.132614,-0.855725],[8.082361,6.686845],[-3.932902,7.577666],[8.302224,9.623169],[-9.636251,4.760653],[4.805737,0.252912],[-4.311874,-7.376994],[-6.463562,3.456592],[5.254608,6.527707],[-1.568070,5.378641],[-9.658191,9.787724],[-9.571100,-7.091890],[-7.335747,-4.462255],[-7.360034,-0.082680],[-6.612774,-9.639995],[-7.463709,3.438085],[2.168569,-9.064141],[2.412580,6.042191],[8.222570,8.403852],[0.974192,-3.119345],[6.255917,6.149642],[-6.582514,1.879667],[-6.518181,7.816908],[0.276263,0.194835],[-5.640066,4.744061],[8.057600,8.575799],[0.360391,-9.510497],[-4.546278,-3.467509],[2.029863,1.170482],[6.670790,-4.299680],[-2.769415,2.777371],[-6.703980,-7.712438],[-7.807672,-4.370105],[-9.389491,-9.897918],[4.905877,6.967910],[-3.765786,9.584799],[0.930415,2.840269],[6.042830,9.816333],[-2.142282,-1.141068],[2.889597,1.568856],[-5.926927,1.674578],[0.714025,-3.553999],[1.168946,-8.841646],[6.368910,9.214174],[-0.368802,-2.109203],[7.673326,2.150542],[-8.811902,-4.520428],[-1.225824,4.902261],[-0.133737,-8.541744],[4.785099,-0.334941],[-0.016256,-9.059603],[-3.740985,-6.651785],[-9.064167,5.234273],[-3.667083,1.228260],[-7.105443,-6.975006],[6.652136,7.906353],[8.131449,8.525609],[-2.942160,8.774511],[-5.860623,-5.860261],[1.173807,9.729690],[7.286079,9.934048],[8.591866,-1.366798],[7.077994,5.326386],[4.710339,-8.068723],[-2.931784,6.210032],[7.072042,4.857308],[-6.394620,-1.187269],[-4.124869,7.053957],[-7.712840,-0.163477],[-2.229794,3.622651],[4.465823,-2.699111],[1.983716,0.852736],[6.032395,-1.967888],[7.778253,-2.411257],[-4.009352,-1.309550],[8.448413,-3.541336],[-4.960877,4.327958],[-0.553679,-1.657144],[2.988876,-9.579533],[5.577956,-8.606355],[-7.823468,6.981666],[-6.458130,5.091789],[8.415925,-7.279582],[9.699053,-7.870959],[6.508273,-6.625557],[6.625492,2.551331],[-5.999856,1.768491],[-9.367787,-8.912098],[7.471914,-1.168750],[9.539653,-1.408165],[9.035411,5.357639],[5.563868,7.146298],[-8.787459,-1.568526],[-8.008388,-0.188293],[2.524561,6.906601],[-0.480395,-9.380301],[6.279051,6.869774],[-0.604816,8.004116],[-5.854473,4.866806],[0.266582,-0.428313],[-1.851921,4.745138],[9.759312,2.972677],[7.277547,-1.816142],[-6.195859,3.202297],[4.960372,7.519346],[-8.756714,-7.917040],[6.562818,1.370124],[-5.235027,-8.725755],[-4.024803,8.819227],[-0.307751,2.687247],[1.011730,5.792205],[-4.526173,-1.302756],[9.833187,-0.493176],[-5.680430,4.321859],[-5.677186,-5.570147],[-1.814085,7.281653],[-9.765422,-4.472589],[-1.038809,4.179716],[5.334560,1.925218],[6.106618,-5.639950],[0.865944,5.765124],[3.323038,-4.325590],[2.128342,-9.212761],[5.213586,-9.263143],[-7.610236,-1.560393],[-7.599865,0.896411],[-4.315475,-2.992827],[-5.530822,4.511929],[1.734481,6.996917],[8.191613,-1.265078],[5.452886,-6.816618],[-2.901088,-9.556175],[-8.677043,2.856888],[-3.400104,-7.073793],[-9.348557,9.453119],[6.261022,-8.735944],[2.334717,6.523452],[6.843066,4.296270],[-9.860101,-9.880003],[-0.675019,-2.749016],[3.670614,-9.599258],[-9.047213,3.087215],[1.919193,1.660265],[6.367471,6.709367],[5.422412,2.402915],[-7.182349,1.883833],[-4.341212,9.704728],[8.664352,5.947371],[-6.014260,-7.069894],[8.892249,7.977236],[-3.344526,1.634451],[-6.096247,-5.898541],[-2.894140,0.647190],[-1.111397,8.452921],[-2.561962,-4.422699],[-9.262120,-3.380604],[9.645068,6.498739],[-2.525415,2.209918],[3.948630,-7.871278],[4.722720,-2.439943],[-5.107785,-8.995050],[-4.894864,-8.678105],[-3.028488,-3.880692],[-8.650040,2.574786],[-5.689804,-6.428890],[7.980109,3.693790],[5.519832,4.221231],[2.889033,-0.215222],[5.858692,-5.643314],[-8.335199,-1.031806],[3.463225,-7.132131],[7.339233,4.615054],[-3.421964,0.500255],[0.340078,9.382262],[-5.002709,1.741268],[-5.093485,-3.891489],[-2.515058,3.151827],[8.019876,-9.706152],[7.029437,-6.489626],[-8.406358,-9.254516],[-1.033772,0.164046],[-9.419936,-8.701322],[1.962372,-1.625873],[8.925375,8.047915],[-9.318553,-9.873160],[-1.795296,-2.326697],[3.823587,-8.884194],[3.289855,1.531644],[-3.415011,3.844738],[3.808595,-0.582343],[-3.457985,-4.738035],[6.259003,0.535716],[-1.354268,0.765666],[-7.673356,-9.214358],[-6.463756,-4.915466],[3.749318,3.695175],[-0.167094,5.368269],[-0.674202,-4.920059],[-9.927239,-9.550604],[-8.461775,9.704452],[-2.528925,5.853691],[6.957700,-7.230748],[-9.642093,7.980688],[-4.477937,-1.799001],[6.604515,-6.170456],[4.674462,-4.828022],[6.385170,8.589462],[1.928955,4.336181],[2.986809,-9.456060],[-4.674064,-8.927130],[0.454004,7.011152],[4.765068,-4.214242],[8.801371,-8.053798],[7.171581,-0.897180],[-2.568990,-6.383579],[4.888075,8.533675],[-4.707278,0.220142],[-1.868519,-0.336259],[4.424771,-0.321553],[9.480453,2.575316],[7.596022,6.839519],[3.416823,-1.038153],[8.325868,2.924861],[-2.756624,3.607871],[-6.122863,3.094601],[-1.798234,4.269915],[8.074372,-0.636166],[-3.499843,3.734710],[-0.720293,4.534118],[3.939935,2.458266],[-2.873051,9.717856],[4.029464,-4.627737],[0.767097,-9.960884],[2.445779,4.711965],[4.261457,1.944909],[0.707547,-1.774710],[4.559184,9.664113],[7.810406,8.064859],[2.025737,-5.450079],[1.378507,7.966561],[-0.594259,-4.175000],[1.987187,7.240616],[-6.038427,-6.476222],[2.047985,5.404141],[-7.628138,2.573174],[4.806928,-6.709093],[1.513033,5.872979],[1.412405,0.254501],[-3.913338,7.824823],[7.720735,3.001161],[7.458371,-6.497101],[-4.970749,8.121466],[-4.834009,-3.991427],[7.500602,0.950667],[5.573442,4.047847],[8.569259,-4.058204],[-5.350411,8.598080],[-0.338454,5.011549],[-1.930187,9.805576],[6.707332,-0.878545],[0.884001,8.977871],[2.510894,-8.441276],[3.340323,5.511596],[-9.652634,4.084934],[3.539335,7.457472],[0.350944,2.367824],[-9.984288,-6.086811],[7.497278,6.716228],[0.261654,4.108453],[0.879388,2.904605],[8.211386,3.938583],[-4.324110,-9.144525],[1.099701,-9.992812],[9.832475,5.856002],[-7.872776,5.958996],[-0.555837,-5.617765],[-5.556891,-5.215562],[8.163009,-3.911674],[-6.486581,5.229732],[-3.779425,-2.164474],[8.739740,-5.421562],[-5.339293,-0.594345],[1.978257,-4.464311],[-4.394302,2.558185],[-2.796394,8.920495],[5.633292,-0.894267],[2.976359,1.282699],[2.709404,-3.473873],[-9.646051,3.002878],[-8.989427,0.789678],[-4.917167,2.794499],[-4.278984,4.428371],[-2.275228,9.392847],[-0.511713,2.101655],[7.728475,-4.094399],[-7.970959,4.280843],[5.304606,4.454793],[-7.089716,-0.394618],[-2.898013,5.397764],[-0.288195,6.423061],[1.059329,6.966776],[-8.754909,-6.861984],[2.646307,-5.124265],[2.519210,-0.417487],[7.807805,-2.391637],[-7.335641,-6.206258],[-7.721425,4.549143],[-6.066056,3.317848],[0.227017,7.942246],[1.057867,3.165623],[-3.855981,-3.923798],[3.973945,9.573681],[-7.867281,-0.704217],[-7.226399,2.082879],[8.167510,1.808494],[2.192584,7.635123],[8.373991,-5.561785],[-3.591432,5.444633],[2.195702,-1.511701],[-6.137805,3.574369],[9.469715,2.568358],[-2.424150,-2.153157],[-7.909746,6.615457],[-1.952920,-1.583203],[-8.252003,-1.567884],[4.035107,2.471997],[7.331184,9.839837],[4.340830,-2.626147],[0.549879,-5.233733],[-0.451564,3.089888],[2.549215,-8.683421],[5.022018,0.453841],[3.828070,0.483838],[-4.222680,-8.198296],[-1.534006,8.768015],[-8.030830,8.146027],[-9.835032,-0.286310],[-8.934356,6.511855],[-7.327824,-6.888559],[-2.296723,4.304966],[8.791365,-8.508766],[-9.983965,-9.422805],[4.606049,-0.293859],[4.876185,5.632602],[-4.408623,9.387394],[6.322687,-4.251838],[-5.207748,5.197110],[-7.840619,5.002694],[4.394995,5.053612],[-1.321566,5.454036],[-7.813097,6.971172],[3.695050,1.219342],[-8.490603,-2.251567],[2.489235,-9.551255],[2.849414,-5.056287],[-4.941529,-6.804012],[-3.068662,8.085362],[0.614560,-4.820060],[3.167773,8.582693],[-9.040694,-8.938094],[3.333529,-9.558907],[7.497141,1.377525],[-5.763778,-1.900768],[2.206985,8.594548],[7.746947,-8.614902],[0.567021,-8.158145],[-1.999349,8.298004],[-7.772030,-3.244066],[-3.678816,-7.624406],[3.227455,6.575213],[0.260396,-8.595228],[-1.203917,-8.516698],[5.873901,-7.258938],[5.957164,0.448672],[-9.674950,-0.973135],[-6.354802,4.338671],[8.945984,-7.992575],[3.860304,8.764524],[0.455418,9.636170],[3.940819,2.898047],[-2.946242,8.330507],[-8.311774,0.802009],[1.262165,2.118884],[-8.949695,-6.527577],[-5.536370,-2.252765],[-1.321492,9.540290],[-0.225133,2.570051],[-2.730571,-5.230528],[-1.665509,0.979104],[-7.792744,-8.696001],[-5.494971,5.580955],[-1.666474,9.509807],[-7.123924,-3.172041],[9.741734,-0.988950],[-6.682429,0.212281],[6.233744,5.173465],[4.274685,-7.798362],[2.025181,8.926276],[2.026433,9.014542],[-9.598354,-8.927825],[-0.407635,-9.300755],[-7.503993,2.455951],[-6.553366,-5.327308],[-7.890719,-4.129434],[-5.536135,2.157197],[4.243041,5.519832],[8.985399,-3.806373],[8.550661,-6.947664],[3.222309,4.842101],[-1.035219,-5.616157],[7.481958,-5.377475],[-6.363909,0.379756],[6.352588,-4.414917],[5.962693,8.536242],[-9.878413,3.848927],[0.442571,-7.564630],[-3.845988,-4.140398],[-6.735334,9.858040],[6.263136,-1.574456],[-3.397773,-2.767766],[-1.410330,-1.545821],[8.423986,2.066374],[6.400916,7.746417],[-2.798760,9.300959],[-0.606576,0.187883],[-7.615752,-9.822091],[-8.729654,9.202222],[5.211452,2.529895],[0.662683,0.476958],[6.286694,-0.200512],[7.393689,7.144349],[0.738611,-5.024977],[2.172653,4.660471],[8.981442,4.941153],[-7.567092,-9.546607],[4.569699,1.752870],[-9.277264,5.735545],[3.800919,-0.678800],[0.870789,5.400019],[7.521995,-9.683824],[9.643947,-6.810813],[-4.491902,3.349931],[4.477310,-1.057921],[3.236779,7.195586],[-0.645825,3.234753],[-8.510186,3.682924],[-3.037109,2.933749],[-5.179301,-4.136086],[0.728649,-7.786661],[-8.181806,-3.608315],[-8.396268,-3.046282],[-2.676770,1.557973],[-5.097584,5.163981],[-6.067150,0.769493],[1.868942,-8.181693],[-9.060900,2.680440],[-7.487777,7.661570],[9.146361,-0.321660],[-9.048851,1.516758],[-5.922749,-1.432854],[-1.091326,2.014106],[-0.804376,9.655817],[6.832260,9.073982],[-3.780064,4.403509],[7.490620,5.285590],[-2.603739,-8.253534],[3.295248,-3.542228],[-4.630448,-3.602133],[-5.771308,0.005238],[-0.699339,-4.725894],[8.661205,-6.163286],[-1.907473,-0.629713],[-3.750307,3.080278],[6.700321,-7.222769],[3.706647,-6.866232],[8.006915,-3.943874],[-0.171122,-6.343540],[-2.520433,4.942882],[-9.056176,6.845192],[6.143545,-7.347210],[-6.769160,9.139930],[1.098755,-2.695331],[-7.739891,-3.072825],[1.902501,9.360338],[7.263170,3.953820],[-4.611911,7.574248],[-1.020009,4.870244],[-9.229912,7.435125],[3.753284,-2.398086],[-6.983497,-2.084787],[2.893155,-1.558643],[8.777148,-3.464884],[8.254395,1.191304],[-1.158690,1.068858],[7.254284,6.906376],[-4.947942,-2.668981],[1.468147,9.386630],[8.514128,-5.189288],[-8.028856,-3.485811],[-5.164421,-7.626388],[-3.649468,0.265922],[-2.896104,4.906256],[6.224309,8.276103],[2.023023,-6.194379],[-1.343164,7.562465],[5.731273,-6.430752],[-2.431905,1.636614],[-3.570908,0.783483],[1.114421,8.948405],[5.713861,-9.969708],[2.247023,-5.992458],[5.094338,5.124507],[-9.736926,-5.210704],[-6.452380,-9.253074],[7.736926,0.893366],[0.505363,-9.082157],[1.662934,6.612989],[-6.333909,-6.172922],[2.872195,-1.991485],[3.845103,0.760767],[-4.329188,9.516880],[-6.171888,-8.072537],[4.945907,2.771518],[-9.784027,-7.189824],[-6.771307,-9.233582],[4.972010,-8.919650],[0.400002,9.287449],[2.064055,2.912465],[-4.035969,-1.491930],[-8.300907,-4.230061],[2.552129,-2.765354],[2.206798,4.232531],[-2.108435,-0.774044],[-0.217272,6.507108],[-7.961722,-4.739064],[2.295641,4.921433],[-6.681838,-3.481151],[-9.560997,6.888240],[2.965209,5.266293],[-8.144730,-5.902899],[-6.161137,-4.961505],[0.136927,7.561613],[-3.708842,6.874933],[9.690315,-5.036955],[9.011616,-6.639793],[6.327023,0.629482],[8.317464,-0.781875],[3.329289,4.802991],[5.994932,0.746570],[5.361862,-1.212931],[-3.434505,0.403851],[2.782610,-0.740157],[-0.319985,-7.149161],[-1.899707,-8.964930],[2.984961,2.936963],[0.489476,-0.090616],[-3.800010,-9.671876],[-4.035050,9.443539],[-6.506437,-9.296035],[-8.720041,-2.187396],[3.843941,1.395007],[-5.332659,-2.387897],[-2.130393,3.107943],[-5.063053,-0.527539],[2.227665,-8.244569],[-4.601619,-5.504291],[-3.793887,-6.528847],[8.351541,7.861870],[7.364051,-9.085266],[9.165110,6.704545],[-2.913252,7.247323],[4.178505,0.149319],[-9.749747,-0.285985],[-2.824804,-1.127569],[-5.010967,1.697036],[9.928336,-6.775740],[5.897837,2.826784],[0.655410,-7.926994],[1.741225,-3.868841],[-2.956372,2.762178],[2.946638,1.853011],[-7.150974,-7.498098],[-9.111435,9.331044],[6.831160,-3.627282],[-5.909293,2.257272],[1.108899,-7.563713],[5.155280,3.284709],[-1.008478,6.875924],[-7.792190,9.033960],[-3.720807,1.194017],[-5.531255,-9.232392],[2.005238,-1.672806],[-0.574492,5.750838],[-3.039302,-7.086468],[2.995982,3.069598],[-2.081601,3.807889],[7.710028,-3.443338],[0.257628,-5.452934],[-2.129801,7.457917],[3.929449,5.915283]], dtype = "float64")#candidate|2342|(1440, 2)|const|float64
const_2343 = relay.const([-4.803275,4.828431,3.327459,-1.017652,3.455713,5.495083,-4.384478,-5.377612,2.237464,8.908133,-6.499877,8.332921,7.481058,5.872078,-1.450650,-6.630734,1.323137,-5.771949,-3.595114,-3.245751,-3.244824,-9.840076,8.752915,-2.487978,8.069569,-4.251982,-0.189145,7.144743,5.524537,-9.046214,-0.415504,-1.563013,2.128279,-4.441854,9.607070,5.914000,-9.905192,2.824831,3.726478,2.532848,9.212734,-5.557143,0.955258,9.356309,-2.207406,-8.909890,-3.846078,-9.512363,7.840739,4.535008,-7.452307,9.003404,-0.420846,-0.885902,-1.104085,-9.960147,-0.693454,-7.909678,8.821802,-9.383138,1.868447,-0.074405,0.194335,7.587428,5.706824,-8.222456,-8.717518,8.104502,-9.992309,-0.941130,3.342084,-0.466995,3.283059,3.492629,0.629500,-0.361897,7.719194,-4.537619,-9.864181,0.520684,4.272912,5.754500,4.082663,-8.979100,-7.417740,8.650690,-0.870239,1.962409,-3.150736,-0.694668,-4.670943,-3.425511,0.199618,0.950338,7.706019,6.237389,-5.174356,-9.244295,0.314384,3.472153,0.508096,8.411833,-5.132262,7.314899,-3.211188,-4.579084,-5.501875,-3.113454,-8.422055,4.541192,-7.435308,-0.611511,7.116220,3.414531,4.397098,1.157679,0.425138,-5.673067,4.155470,-6.184150,0.352886,1.208222,1.395276,8.923170,8.724472,6.007486,-0.827920,-9.237074,-5.538091,-1.447080,-9.244507,-3.048374,8.989452,9.780909,-8.622410,-7.148278,5.895246,-0.533631,9.787811,-8.311876,-2.204224,-6.375685,3.345495,4.755928,-1.054534,1.079017,1.818197,-8.172142,0.344930,6.212996,2.674065,2.846294,8.255025,-0.819494,-7.493600,7.642166,-5.651886,9.199499,-5.537485,-2.027533,-2.330348,4.574186,1.179835,-2.056774,-1.138082,9.631012,1.313467,-5.696558,-0.496825,2.397507,6.908332,5.562225,1.529196,6.211871,7.611650,-6.468540,9.203744,9.944809,-3.882267,4.613377], dtype = "float32")#candidate|2343|(180,)|const|float32
call_2341 = relay.TupleGetItem(func_375_call(relay.reshape(const_2342.astype('float64'), [16, 15, 12]), relay.reshape(const_2343.astype('float32'), [180,]), ), 1)
call_2344 = relay.TupleGetItem(func_378_call(relay.reshape(const_2342.astype('float64'), [16, 15, 12]), relay.reshape(const_2343.astype('float32'), [180,]), ), 1)
func_114_call = mod.get_global_var('func_114')
func_117_call = mutated_mod.get_global_var('func_117')
var_2348 = relay.var("var_2348", dtype = "float64", shape = (135,))#candidate|2348|(135,)|var|float64
call_2347 = func_114_call(relay.reshape(var_2348.astype('float64'), [9, 15, 1]))
call_2349 = func_114_call(relay.reshape(var_2348.astype('float64'), [9, 15, 1]))
func_1652_call = mod.get_global_var('func_1652')
func_1655_call = mutated_mod.get_global_var('func_1655')
var_2355 = relay.var("var_2355", dtype = "float32", shape = (105, 2))#candidate|2355|(105, 2)|var|float32
var_2356 = relay.var("var_2356", dtype = "float32", shape = (630,))#candidate|2356|(630,)|var|float32
call_2354 = func_1652_call(relay.reshape(var_2355.astype('float32'), [15, 1, 14]), relay.reshape(var_2356.astype('float32'), [15, 3, 14]), )
call_2357 = func_1652_call(relay.reshape(var_2355.astype('float32'), [15, 1, 14]), relay.reshape(var_2356.astype('float32'), [15, 3, 14]), )
bop_2362 = relay.mod(var_2348.astype('float64'), bop_2332.astype('float64')) # shape=(2, 13, 135)
output = relay.Tuple([call_2341,const_2342,const_2343,call_2347,call_2354,var_2355,var_2356,bop_2362,])
output2 = relay.Tuple([call_2344,const_2342,const_2343,call_2349,call_2357,var_2355,var_2356,bop_2362,])
func_2366 = relay.Function([var_2331,var_2348,var_2355,var_2356,], output)
mod['func_2366'] = func_2366
mod = relay.transform.InferType()(mod)
var_2367 = relay.var("var_2367", dtype = "int16", shape = (2, 13, 1))#candidate|2367|(2, 13, 1)|var|int16
var_2368 = relay.var("var_2368", dtype = "float64", shape = (135,))#candidate|2368|(135,)|var|float64
var_2369 = relay.var("var_2369", dtype = "float32", shape = (105, 2))#candidate|2369|(105, 2)|var|float32
var_2370 = relay.var("var_2370", dtype = "float32", shape = (630,))#candidate|2370|(630,)|var|float32
output = func_2366(var_2367,var_2368,var_2369,var_2370,)
func_2371 = relay.Function([var_2367,var_2368,var_2369,var_2370,], output)
mutated_mod['func_2371'] = func_2371
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2815 = relay.var("var_2815", dtype = "float64", shape = (4, 9, 2))#candidate|2815|(4, 9, 2)|var|float64
uop_2816 = relay.tan(var_2815.astype('float64')) # shape=(4, 9, 2)
output = uop_2816
output2 = uop_2816
func_2822 = relay.Function([var_2815,], output)
mod['func_2822'] = func_2822
mod = relay.transform.InferType()(mod)
mutated_mod['func_2822'] = func_2822
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2823 = relay.var("var_2823", dtype = "float64", shape = (4, 9, 2))#candidate|2823|(4, 9, 2)|var|float64
func_2822_call = mutated_mod.get_global_var('func_2822')
call_2824 = func_2822_call(var_2823)
output = call_2824
func_2825 = relay.Function([var_2823], output)
mutated_mod['func_2825'] = func_2825
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2846 = relay.var("var_2846", dtype = "float64", shape = (4, 3, 10))#candidate|2846|(4, 3, 10)|var|float64
var_2847 = relay.var("var_2847", dtype = "float64", shape = (4, 3, 10))#candidate|2847|(4, 3, 10)|var|float64
bop_2848 = relay.less(var_2846.astype('bool'), relay.reshape(var_2847.astype('bool'), relay.shape_of(var_2846))) # shape=(4, 3, 10)
output = relay.Tuple([bop_2848,])
output2 = relay.Tuple([bop_2848,])
func_2871 = relay.Function([var_2846,var_2847,], output)
mod['func_2871'] = func_2871
mod = relay.transform.InferType()(mod)
mutated_mod['func_2871'] = func_2871
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2871_call = mutated_mod.get_global_var('func_2871')
var_2873 = relay.var("var_2873", dtype = "float64", shape = (4, 3, 10))#candidate|2873|(4, 3, 10)|var|float64
var_2874 = relay.var("var_2874", dtype = "float64", shape = (4, 3, 10))#candidate|2874|(4, 3, 10)|var|float64
call_2872 = func_2871_call(var_2873,var_2874,)
output = call_2872
func_2875 = relay.Function([var_2873,var_2874,], output)
mutated_mod['func_2875'] = func_2875
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3202 = relay.var("var_3202", dtype = "float64", shape = (15, 2, 16))#candidate|3202|(15, 2, 16)|var|float64
uop_3203 = relay.sqrt(var_3202.astype('float64')) # shape=(15, 2, 16)
uop_3221 = relay.cos(uop_3203.astype('float64')) # shape=(15, 2, 16)
func_1259_call = mod.get_global_var('func_1259')
func_1263_call = mutated_mod.get_global_var('func_1263')
var_3224 = relay.var("var_3224", dtype = "int64", shape = (845,))#candidate|3224|(845,)|var|int64
var_3225 = relay.var("var_3225", dtype = "float32", shape = (180,))#candidate|3225|(180,)|var|float32
const_3226 = relay.const([-9,7,-2,1,3,8,-6,1,-9,-9,-1,-10,10,1,9,-10,-8,-6,2,-6,-5,8,-9,-1,4,-7,-10,2,-4,5,-8,-2,3,-1,-7,-3,9,-2,-2,1,4,3,-7,-3,7,-6,6,-5,8,-6,-1,7,-2,-10,-5,-2,-9,2,-1,8,-6,5,2,1,-4,-7,7,6,-5,4,9,9,-3,5,8,10,-8,6,-6,2,-5,6,-2,-9,-3,5,1,2,-4,5,-10,8,1,10,2,-7,2,6,8,-9,10,-4,7,-2,3,-7,-4,3,-10,3,6,8,5,-1,1,5,7,2,-3,7,4,9,8,3,6,9,-6,-3,10,6,-6,-3,-10,7,1,-9,9,-5,3,-6,-4,2,-1,-2,9,-4,-9,-7,6,-2,1,4,-1,-8,6,3,10,-9,10,-4,9,5,-7,-5,-10,9,-10,3,3,6,-5,7,-6,-6,10,-9,-10,-7,9,-9,10,-10,3,2,3,5,-10,-5,1,-5,1,-9,8,-7,7,6,6,-10,7,4,3,-2,-2,-9,8,3,10,2,8,-7,-5,-6,6,1,7,7,-7,-3,4,1,8,3,7,-7,5,4,4,-3,6,-6,-1,3,2,6,-7,-9,-2,2,8,-8,3,4,-2,10,3,10,-10,10,6,7,-5,-8,-7,-8,-10,-7,-8,4,8,-7,1,4,8,-1,-2,-8,3,1,6,6,-6,3,-5,-4,-9,3,6,-1,-1,-9,-1,7,-2,-7,-10,6,-7,9,-6,-5,2,6,7,-2,-2,-1,-9,8,-1,-2,9,10,-9,-9,2,9,-4,-3,2,1,-8,6,3,1,-10,-8,10,-6,6,1,9,-3,-5,-4,-6,9,-7,3,1,-7,-4,-2,2,-3,-3,-8,4,-5,-2,6,-6,-3,-1,7,10,-3,-1,-9,2,3,8,-8,-5,-1,-4,4,-3,-4,-3,6,-7,6,-5,10,10,-3,-7,1,3,-6,9,8,-6,6,-3,1,-1,-5,5,-4,-1,1,9,9,-4,-1,-4,6,-1,-9,7,2,8,-6,7,8,-8,-7,1,-1,10,1,-2,5,-1,8,4,-6,9,7,-4,5,4,-1,7,-3,5,-2,2,10,2,1,-10,-10,1,-7,2,8,-4,-4,-10,-8,2,-4,7,-6,-2,7,-6,-10,-6,-3,-1,-6,-10,5,-7,7,-5,4,4,3,8,9,6,-4,-8,-1,-6,3,-7,-5,5,6,2,-4,-1,-4,6,5,-5,-4,-6,2,-4,-7,5,-9,-6,10,6,-4,-10,6,-4,-10,1,-1,-1,-8,-10,-7,-9,-5,3,2,-9,6,9,-9,-6,1,5,2,-5,-2,-5,1,-7,-10,-2,-10,1,2,10,10,-10,-1,2,-10,4,-3,-3,7,-1,-8,9,3,4,9,-7,-7,-1,10,4,2,6,-10,-10,-8,-4,-3,6,3,1,3,-3,3,-1,-9,6,2,7,-8,-7,-1,3,-3,9,-9,2,-6,-2,-10,3,7,-1,1,9,6,-8,-8,-10,-9,9,-9,2,5,-6,7,4,-1,3,4,3,-9,-8,1,-7,7,10,6,-1,6,-8,7,8,-9,-9,-2,-3,-1,-7,-9,3,-10,-9,-5,-1,-8,-5,-3,2,-4,4,-5,-7,8,-1,6,-10,-8,-7,1,-5,7,1,-3,-1,-8,-2,-2,9,3,-4,5,7,4,6,2,-2,1,8,-10,8,-3,-9,9,4,10,-1,3,6,-4,3,-6,-4,2,-9,-2,-10,-9,-10,9,-2,-2,-3,3,-4,-4,4,4,6,-1,-8,-6,-9,-9,5,5,-8,10,-1,1,-9,-2,6,2,-2,9,-7,-8,9,-7,7,10,8,5,3,7,-2,9,-7,-1,6,-8,-4,1,-6,-8,10,-8,-9,2,-10,8,-9,1,-7,-2,-4,-6,-9,-2,5,9,9,6,10,-4,6,-4,8,-9,-10,10,3,2,2,8,5,5,-5,-4,8,5,9,-10,-7,-5,-2,-10,-8,-1,-8,10,-6,-7,-7,-6,-8,-10,2,-5,-9,-7,5,9,2,6,9,-3,-10,-8,9,1,-4,-6,2,-7,-4,-3,-6,4,2,-7,-5,-8,1,1,7,-9,6,-1,-9,-9,-5,-3,5,-8,-5,-8,7,7,-1,8,-2,-10,4,-5,2,-7,-6,-7,-8,-8,1,-5,-1,6,1,-9,-5,-3,2,2,-4,8,-9,-1,-9,-10,-4,-1,-7,6,-3,3,5,6,6,1,9,1,6,5,-10,8,-1,-10,5,10,-10,7,1,-3,3,8,-5,2,-1,-7,-5,7,-3,6,-3,-8,-9,10,-10,8,9,7,-5,5,5,8,-4,-8,2,-5,-10,9,9,1,4,-5,7,9,1,7,4,8,10,7,7,6,6,-9,7,-6,-1,-6,-1,10,8,7,-3,-4,-8,5,-4,5,8,-6,-5,-8,1,3,-10,3,-10,-2,7,8,-6,3,7,9,-3,10,5,-4,-3,-10,10,1,-6,-5,-8,10,-7,3,2,-1,6,3,-1,-10,6,5,3,-7,8,4,4,-1,7,-7,5,4,-9,-3,-5,-3,2,6,6,6,5,4,-4,-4,-7,7,-9,3,9,-10,-8,-7,3,-6,7,4,2,3,3,6,-8,-3,-6,-7,-10,-1,-2,-9,-2,-5,-4,2,7,1,-1,-1,10,8,-8,-2,1,-7,2,9,10,4,3,2,-1,1,10,3,-5,7,-5,2,-2,1,6,9,-2,-9,-9,8,-6,2,-10,-7,5,8,4,-5,2,4,6,3,-6,-4,5,-5,-10,6,-3,6,-8,-7,6,-3,-10,6,8,-3,-6,-1,8,2,4,-9,-3,-6,-1,5,7,-8,3,-2,-5,-9,-9,-2,8,-4,-3,1,9,-9,10,-10,4,-5,-3,-9,-9,9,-9,-4,6,9,-2,7,8,2,2,9,1,2,-9,2,1,6,4,-7,10,2,-6,3,-5,-6,-10,-4,6,-7,-8,5,-2,-9,2,9,-4,4,-7,6,4,2,6,5,1,9,10,-9,4,1,6,8,8,-1,-2,1,-10,10,-9,10,-8,1,10,4,-10,9,-4,7,10,-9,9,-8,4,-5,-6,5,3,-6,8,6,-5,-5,2,1,3,6,-1,-9,4,-8,-10,-6,8,5,-2,-3,5,-3,3,-3,-5,6,-3,1,-10,10,1,-4,-10,7,7,-6,-2,-1,5,9,3,6,-2,-5,-5,6,-3,-8,-7,-4,7,-9,10,-3,-6,-5,-10,6,7,6,-10,-7,-1,5,-10,-6,-10,-5,7,-5,2,5,-2,-6,4,-10,-4,-7,-4,5,-3,10,-8,-4,-6,-9,1,-10,4,-4,8,3,3,-9,4,10,6,1,-8,8,-3,2,-2,-9,-10,7,8,-10,-9,7,-4,1,10,4,6,-4,3,-3,2,-3,4,10,1,-3,10,4,-9,-6,6,9,-3,10,-10,-3,6,3,-8,-4,-7,-7,-8,-3,-7,-10,-8,-4,-1,-9,1,3,7,-1,-1,4,-3,4,-4,-10,7,-4,8,-8,-6,2,-8,-7,1,2,3,1,-6,7,4,-1,-9,8,4,-8,4,8,-5,8,4,-9,3,3,4,9,1,-1,-4,-8,4,1,-8,-1,-5,-8,-9,6,-6,1,-10,10,-2,-2,7,-7,5,-10,-6,-5,-9,1,-9,-8,-5,5,-1,7,-5,10,-8,-4,4,8,-4,-2,-8,-1,-8,-2,-9,-10,-3,6,7,-9,-2,2,8,3,-4,6,-7,-1,-5,-10,1,9,-1,1,10,7,-4,5,10,3,-4,-8,-6,-6,3,9,9,7,10,10,-1,-1,5,-6,-5,-2,9,-10,8,-8,-5,4,-3,-4,2,-5,10,-7,-2,-1,-3,-6,3,-5,-5,4,10,-1,-1,-7,8,6,-8,2,-6,-6,8,-1,-1,3,-1,-5,-5,1,-3,10,10,9,1,-7,6,7,-9,-4,5,8,2,-5,2,-4,-6,-4,10,-6,5,-7,-1,5,-3,2,-6,-3,4,7,6,8,-6,10,-8,-7,10,-5,8,-10,-1,-8,3,-7,-1,-4,6,9,-6,7,5,-6,10,3,3,1,-8,-1,2,9,-2,10,-4,-9,-10,-4,-10,8,-4,-10,-6,3,9,4,-1,7,-3,1,-8,8,9,-2,2,1,-3,-3,1,5], dtype = "int8")#candidate|3226|(1568,)|const|int8
call_3223 = relay.TupleGetItem(func_1259_call(relay.reshape(var_3224.astype('int64'), [5, 13, 13]), relay.reshape(var_3225.astype('float32'), [180,]), relay.reshape(const_3226.astype('int8'), [1568,]), ), 0)
call_3227 = relay.TupleGetItem(func_1263_call(relay.reshape(var_3224.astype('int64'), [5, 13, 13]), relay.reshape(var_3225.astype('float32'), [180,]), relay.reshape(const_3226.astype('int8'), [1568,]), ), 0)
output = relay.Tuple([uop_3221,call_3223,var_3224,var_3225,const_3226,])
output2 = relay.Tuple([uop_3221,call_3227,var_3224,var_3225,const_3226,])
func_3230 = relay.Function([var_3202,var_3224,var_3225,], output)
mod['func_3230'] = func_3230
mod = relay.transform.InferType()(mod)
var_3231 = relay.var("var_3231", dtype = "float64", shape = (15, 2, 16))#candidate|3231|(15, 2, 16)|var|float64
var_3232 = relay.var("var_3232", dtype = "int64", shape = (845,))#candidate|3232|(845,)|var|int64
var_3233 = relay.var("var_3233", dtype = "float32", shape = (180,))#candidate|3233|(180,)|var|float32
output = func_3230(var_3231,var_3232,var_3233,)
func_3234 = relay.Function([var_3231,var_3232,var_3233,], output)
mutated_mod['func_3234'] = func_3234
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3311 = relay.var("var_3311", dtype = "uint16", shape = ())#candidate|3311|()|var|uint16
const_3312 = relay.const([[[7,9,-2,9,9,5,-2,-6,5,1,10,8,1],[-10,10,-5,7,4,-9,5,9,-9,-8,-8,-8,9],[-2,-1,10,6,-1,6,-4,-7,-3,2,6,-7,-8],[-5,3,2,10,10,9,1,6,-7,-10,-5,1,-9],[1,-9,-10,-3,8,-10,-1,10,8,-9,1,-7,4],[-7,1,10,-1,-9,5,4,9,2,6,-9,3,9],[8,6,7,-7,-9,-10,-7,-1,-1,6,1,-10,-9],[-1,1,-6,-7,-10,-6,-5,-3,-5,-4,-5,-1,4]],[[8,-9,7,9,4,-6,10,7,5,10,7,-10,-10],[-5,-7,-3,7,2,-3,-1,-8,8,-6,-3,7,9],[-1,-4,-6,-3,9,8,7,-1,2,-9,-10,-6,2],[-7,7,4,7,-10,-6,-7,-9,3,6,-8,8,9],[-4,6,6,-6,1,10,7,-2,1,10,-6,-5,10],[3,1,-6,6,-1,-5,-5,7,4,-5,9,-8,7],[-5,-8,-8,-1,-2,-3,6,3,3,8,3,-5,6],[8,4,-10,10,4,-9,-4,-1,-1,3,10,2,-5]],[[8,7,4,10,1,-7,-7,6,3,9,8,-2,-6],[6,-10,4,1,-6,5,2,-7,6,7,10,-3,-7],[2,2,4,5,9,6,1,6,7,3,-7,7,-10],[-6,-9,5,-4,1,-7,4,8,-7,-9,8,-10,-1],[9,-1,-9,3,1,1,-5,3,-9,-7,6,-7,-6],[4,-5,3,5,4,-2,-1,-2,-10,5,6,-2,-2],[-8,3,3,10,-4,-1,-6,4,1,-2,-8,-10,6],[6,1,-6,6,-3,-7,-6,-5,-10,3,10,9,-6]],[[4,1,-2,-8,4,1,3,10,6,-3,-4,-5,-6],[2,-9,-6,2,3,-4,-8,4,10,-3,9,6,-2],[4,-9,2,-8,8,4,-1,6,7,-6,3,-10,4],[-6,9,3,5,6,3,-10,7,-3,-10,-6,4,10],[7,4,1,-4,-9,-6,8,6,5,2,-10,2,3],[9,-1,-5,-10,10,10,-2,2,3,-7,3,5,-3],[10,4,-5,-3,1,5,-8,3,-10,4,2,-1,-8],[-10,-10,7,10,5,4,4,-7,-7,3,-10,-4,4]],[[-6,4,1,-7,8,-1,5,8,6,-5,10,-6,9],[-7,-2,6,7,-2,-5,-9,4,3,-8,9,2,6],[3,4,-10,6,1,-2,3,5,4,10,6,7,2],[-7,-1,6,-7,-7,-9,-8,4,-9,3,-2,-9,-5],[6,8,-10,-2,-10,-7,7,3,-7,-8,-1,8,2],[1,4,4,-9,-8,9,-10,-8,-7,10,-5,-1,10],[2,5,9,3,1,-3,-2,-9,-3,-2,-7,8,-9],[6,5,-1,3,-1,2,-6,-3,-1,-2,-8,1,-7]],[[-10,-6,5,-8,-8,-7,5,-3,-2,-9,-10,2,3],[10,-1,-2,10,-10,2,5,-9,2,10,2,-4,7],[-3,9,-2,-2,4,3,-4,8,3,7,-6,7,-4],[-6,-1,-4,5,-10,10,9,6,7,7,7,7,-3],[4,-8,2,-7,-8,-5,4,-7,9,-8,8,-6,-9],[6,-8,-10,10,1,2,4,10,-3,7,9,-8,1],[-2,-10,10,10,6,2,-8,9,-2,-1,4,-7,6],[7,2,-9,-6,7,6,6,7,-9,3,-8,10,-1]],[[5,-7,5,4,-3,4,-3,-7,-8,2,-3,2,-8],[-4,10,-7,3,-6,8,-8,5,2,4,-9,-4,-8],[2,2,-8,2,-2,-3,-1,-7,-6,-3,8,-9,7],[-3,-10,6,10,-4,6,6,-5,7,7,6,-9,-6],[-6,-9,4,-2,2,-6,7,3,-8,-5,10,-10,6],[-10,-6,-3,-3,5,-4,-2,6,1,8,9,2,8],[6,9,-5,-10,-9,-3,-3,8,5,4,-7,-5,6],[2,7,-2,-9,8,3,-5,9,3,-6,9,-2,-1]],[[7,-6,9,3,-8,-1,-9,3,7,4,-5,7,-9],[-3,1,-2,9,3,5,-5,2,-2,-5,1,-10,-7],[4,-6,-2,6,2,-4,-5,10,3,-3,-3,4,-7],[-1,1,-3,4,10,8,-1,-3,5,10,-7,3,7],[-4,-6,-9,-1,-5,-7,-6,2,10,-6,8,2,7],[10,9,5,-10,6,8,-2,-2,9,-4,3,6,-9],[-9,2,-10,7,2,3,-3,-3,-8,3,2,9,-4],[-1,2,-5,-1,-8,-1,-10,-6,-9,6,9,7,-8]],[[-3,6,-1,-8,-7,3,-1,-2,-7,7,7,-2,8],[-1,-5,-3,-5,-8,5,9,-10,-3,5,-3,-8,-6],[8,2,-3,-10,-1,9,-3,-4,4,2,8,-4,3],[-7,-10,7,-5,4,9,8,-9,8,5,-2,-5,-2],[-2,-8,-6,5,10,-3,-1,2,-3,2,7,-3,1],[-1,10,9,-2,6,-4,3,2,-8,5,3,-8,9],[4,-10,-7,-1,-6,8,9,-5,6,-6,6,-1,2],[8,-10,9,-8,9,8,2,-2,2,-6,-4,-7,-3]],[[4,5,-10,10,-1,-6,-6,6,-4,-7,-1,-10,8],[-1,4,-9,10,6,10,-1,-5,-3,1,4,-10,-4],[2,1,-7,6,-8,2,2,7,-6,-2,-3,-1,-4],[2,5,-6,9,8,10,9,-2,6,-9,-5,-1,-5],[4,1,-10,-4,8,-4,7,-2,10,5,-10,-6,-3],[-7,10,1,7,-1,-2,4,5,6,3,-9,7,7],[-6,-10,5,-5,9,-8,7,-5,-4,-8,10,3,2],[-8,-7,-8,-9,-5,-6,-9,8,1,-7,-4,-9,10]],[[-8,3,-4,-9,-10,-5,3,-5,-2,-4,-2,-4,3],[-7,-2,-2,-1,-10,-9,-7,4,-8,-4,8,7,-4],[8,5,-10,4,1,-4,-2,-9,-1,-10,8,6,2],[8,7,-6,4,6,6,-5,9,-9,-4,-4,5,-4],[3,-7,-5,4,-10,6,-4,7,-4,6,4,4,6],[-4,1,7,7,1,-10,-3,7,-4,4,2,-6,1],[6,5,-5,-6,-9,2,-7,-8,-10,-9,2,2,7],[-4,-2,10,-2,3,-7,4,2,-2,1,-7,-2,-1]],[[-4,-10,5,-3,-9,-7,1,8,9,-4,10,-9,3],[-3,4,9,7,8,-3,2,-7,3,-1,6,3,-10],[-3,3,4,-2,1,6,-1,3,7,-6,-4,-2,9],[4,9,6,-2,-1,6,7,-7,9,-9,-3,-6,3],[-7,-7,-5,2,-5,-8,-9,5,4,-5,5,8,6],[2,-2,4,-2,-8,9,2,10,3,1,-5,8,-4],[5,8,-5,3,-7,-7,-7,-5,8,-2,-9,8,-1],[-3,-4,-3,-2,10,1,-5,4,7,-10,10,10,-6]],[[9,7,4,10,-8,9,-5,-7,6,-7,7,-2,6],[5,-5,5,3,-3,-3,-7,7,-2,6,-1,5,-3],[-9,9,6,-1,3,3,9,4,-3,6,-8,-4,-10],[-9,2,7,-4,9,10,-8,-6,-10,-1,9,-9,5],[3,-4,-4,-10,-2,8,-5,5,-8,10,-8,-1,7],[2,-2,3,-4,-10,7,-5,-7,4,-1,-7,4,3],[8,-10,3,-2,6,-2,-4,1,2,-2,-2,-9,7],[-1,3,-4,9,9,5,9,-9,-4,-3,6,-4,4]],[[-5,8,-9,5,-7,5,3,8,-7,9,-9,-9,-1],[-10,3,10,7,2,-9,9,5,1,-10,-6,-7,-3],[10,-1,-8,8,4,-9,-6,-8,7,-8,-5,-10,8],[-10,-1,-1,4,3,-2,-3,-9,-7,5,-9,-7,5],[-5,-5,-1,10,-7,-6,-5,-4,2,-3,-2,-5,10],[-9,10,-6,-1,2,7,5,-4,-8,-9,-4,-2,1],[9,-2,1,-3,7,8,4,9,3,-5,4,4,6],[4,6,3,-3,-4,6,5,-1,-9,-4,-6,4,-2]],[[7,-4,5,-2,-5,-8,-9,3,4,-7,5,-9,8],[-6,7,1,-5,8,4,4,-4,-8,-7,-6,-2,-7],[1,-6,3,1,1,5,-8,-9,-2,2,5,7,-4],[4,-8,-3,-9,7,-10,-4,-4,-8,-2,7,-9,-8],[-2,8,-7,-3,5,3,-4,8,3,-6,2,9,10],[6,6,4,8,-3,-4,10,-2,-5,-7,4,-8,-7],[4,-2,4,4,9,-8,-7,4,9,1,8,2,3],[-5,4,-9,8,3,-9,-1,-2,-7,-2,-2,-6,-4]],[[1,2,-2,4,9,-4,-7,10,-5,-8,4,8,8],[-8,-5,9,-10,1,-9,8,10,-6,1,7,-9,-5],[-10,-8,4,-3,10,-4,-4,-10,10,1,-2,-1,3],[8,-2,-4,7,1,9,10,-7,-10,9,-3,10,1],[1,4,1,-5,-7,5,4,-5,1,2,10,-8,4],[8,-5,5,-2,-7,10,-3,-4,3,6,1,-3,-5],[9,-4,5,6,-10,4,-9,-4,-7,-6,-7,1,6],[3,6,-6,1,7,-1,-8,3,4,6,-1,-5,4]]], dtype = "uint16")#candidate|3312|(16, 8, 13)|const|uint16
bop_3313 = relay.right_shift(var_3311.astype('uint16'), const_3312.astype('uint16')) # shape=(16, 8, 13)
uop_3316 = relay.log2(bop_3313.astype('float64')) # shape=(16, 8, 13)
uop_3323 = relay.sin(uop_3316.astype('float64')) # shape=(16, 8, 13)
bop_3335 = relay.logical_or(uop_3323.astype('bool'), relay.reshape(uop_3316.astype('bool'), relay.shape_of(uop_3323))) # shape=(16, 8, 13)
output = relay.Tuple([bop_3335,])
output2 = relay.Tuple([bop_3335,])
func_3344 = relay.Function([var_3311,], output)
mod['func_3344'] = func_3344
mod = relay.transform.InferType()(mod)
mutated_mod['func_3344'] = func_3344
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3345 = relay.var("var_3345", dtype = "uint16", shape = ())#candidate|3345|()|var|uint16
func_3344_call = mutated_mod.get_global_var('func_3344')
call_3346 = func_3344_call(var_3345)
output = call_3346
func_3347 = relay.Function([var_3345], output)
mutated_mod['func_3347'] = func_3347
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3448 = relay.var("var_3448", dtype = "uint16", shape = (5, 4, 6))#candidate|3448|(5, 4, 6)|var|uint16
var_3449 = relay.var("var_3449", dtype = "uint16", shape = (5, 4, 6))#candidate|3449|(5, 4, 6)|var|uint16
bop_3450 = relay.right_shift(var_3448.astype('uint16'), relay.reshape(var_3449.astype('uint16'), relay.shape_of(var_3448))) # shape=(5, 4, 6)
uop_3454 = relay.asin(var_3448.astype('float64')) # shape=(5, 4, 6)
output = relay.Tuple([bop_3450,uop_3454,])
output2 = relay.Tuple([bop_3450,uop_3454,])
func_3460 = relay.Function([var_3448,var_3449,], output)
mod['func_3460'] = func_3460
mod = relay.transform.InferType()(mod)
mutated_mod['func_3460'] = func_3460
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3460_call = mutated_mod.get_global_var('func_3460')
var_3462 = relay.var("var_3462", dtype = "uint16", shape = (5, 4, 6))#candidate|3462|(5, 4, 6)|var|uint16
var_3463 = relay.var("var_3463", dtype = "uint16", shape = (5, 4, 6))#candidate|3463|(5, 4, 6)|var|uint16
call_3461 = func_3460_call(var_3462,var_3463,)
output = call_3461
func_3464 = relay.Function([var_3462,var_3463,], output)
mutated_mod['func_3464'] = func_3464
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3862 = relay.const([[[-8.526205,9.400758,4.618330,-6.113306,-2.871046,-6.014655,6.745864,7.695168,8.497420,4.665928,-5.308286,-4.597935],[-9.075878,2.817289,-3.065624,5.007412,7.892450,-6.456083,-8.549973,1.371592,4.087443,-7.858557,-9.497035,-0.965636],[3.433495,-7.487004,2.278425,-4.277893,5.082344,0.190511,-8.462659,-9.480706,6.298067,-5.675246,3.483324,-5.070752],[8.914201,0.865973,2.167208,-9.033837,5.256880,-8.990280,2.876247,4.265076,-9.858750,4.347563,2.880524,5.474138],[-8.712235,8.231952,7.762406,1.063539,-7.272050,4.288183,-3.177679,-2.672791,-6.997656,9.787388,8.647785,-9.005092],[8.567137,-8.695126,7.456230,6.521811,8.233402,4.079650,-1.465827,-2.105977,0.943665,-8.754504,3.743783,-2.905483],[-4.582356,0.533419,-4.952268,8.517706,6.103409,-2.830670,0.312318,9.221079,-4.358502,-7.464645,7.994417,6.298413],[-7.511111,-2.244200,0.521667,4.979797,-1.082745,6.986742,-7.995624,-0.872482,8.968873,-6.034335,-7.670434,5.980488],[-8.244719,-3.185335,-6.764830,-2.855291,4.970674,-9.561744,8.439231,-5.620705,1.559015,-8.594071,4.924990,6.799012],[-1.111488,7.830712,9.062377,6.119628,-3.102122,5.858680,-1.256331,2.658814,0.902191,-9.042241,6.652942,-2.452886],[-4.996400,-0.258965,-8.690992,-6.730360,7.767800,3.818968,1.861827,-6.656577,-6.315921,-6.227651,-0.319936,1.457265],[-0.553223,-9.045513,-1.875090,-4.158760,-3.573457,-4.244269,-9.280792,1.675530,0.491753,7.186163,1.027849,-9.059209],[6.189696,-5.800694,5.603885,7.183277,2.322956,7.881756,0.817263,9.649734,1.367499,-1.372742,-9.723481,9.792050],[-0.129917,-6.958573,3.481416,-1.568260,-4.580442,-8.593122,-6.142962,4.117976,2.287360,8.806350,-4.269996,-7.661623]],[[1.559504,1.864214,-2.056626,3.067653,3.699808,2.315103,-5.805317,-7.441907,-9.686551,-4.001499,-2.628891,2.295771],[0.651385,-9.135920,2.755921,6.636779,4.926026,-7.350420,8.701949,5.426184,-3.807426,6.323092,-9.119634,7.544005],[-2.473080,5.858130,9.764433,0.167969,3.970087,-5.146280,-3.843519,0.619619,-4.283221,-6.863805,0.406399,8.458991],[-8.515551,3.153415,-5.013433,8.721956,-4.796094,3.850869,4.293231,-9.576167,0.964563,0.609509,-7.162438,0.611194],[4.858029,5.256966,8.046802,-6.695323,4.008726,-8.875178,-9.505036,0.520075,-1.004934,-5.072133,0.061188,2.783470],[7.948267,-0.722811,4.841775,-1.767277,9.843237,-6.161520,-6.489704,-7.461044,-9.946433,7.521338,4.970729,8.235876],[-9.810204,7.362757,2.838172,-4.940494,-7.622109,-0.578341,-8.518260,-9.211228,-2.923044,0.442134,9.329767,2.154039],[-5.779973,-2.197743,6.232295,-8.955958,2.654128,1.500085,-1.517402,3.034555,-8.655628,-1.125459,-8.198863,5.312482],[7.869126,-9.164792,-4.710834,-3.514141,-1.622861,-5.353985,3.848228,8.795775,8.521308,2.711580,-7.709668,-7.776332],[-3.486513,-5.533063,0.258039,-4.931056,-8.479251,2.032087,-8.574564,8.930913,-4.130754,-3.713109,-6.498930,-4.981266],[-3.096473,5.366198,-4.196530,8.072358,0.228562,2.166318,8.908529,0.273701,-8.978495,8.297679,0.388661,-7.370622],[-3.586901,7.994768,-8.649194,-0.399198,5.671393,-6.592160,7.258389,-2.241257,0.707678,2.780846,3.450962,-8.777469],[9.966047,-7.914232,-5.362000,-7.357711,2.844194,-5.744419,0.636816,-4.524183,-7.894151,-9.238839,2.218428,-7.039075],[2.638337,8.746373,9.611719,-8.558278,9.838638,5.277032,8.817324,3.571606,8.132702,4.774711,-9.803103,4.578686]],[[-8.783020,7.041113,-2.830549,-8.182116,6.930519,7.773705,6.200379,-7.757233,-8.713653,-2.975507,7.788981,4.656637],[3.586020,-2.786088,-7.822850,8.937454,7.432423,-6.129960,-5.129232,6.584485,9.561294,-6.280763,0.205678,6.975809],[-5.839617,3.466054,5.975677,-3.050087,6.905542,9.859769,-0.347876,-9.051634,6.326076,-5.638044,6.238686,4.727072],[-4.250624,5.169576,-5.916181,2.235653,4.235930,4.439652,4.676842,5.685525,-6.281955,8.552362,7.831222,-6.364705],[-3.103378,5.736434,0.537277,-9.728913,-1.823641,9.506881,9.231558,-9.602711,4.800169,2.352119,5.397477,-6.050636],[5.028238,8.917240,5.966823,1.407145,-8.214262,-4.177225,-0.395457,5.996960,-6.234356,5.162744,7.428716,-0.131118],[8.409168,-7.082378,2.983507,-6.668146,-6.239340,3.077850,-7.777636,9.829397,9.709500,-8.824093,2.390844,1.032639],[-8.070248,5.067163,-7.846410,-4.536798,8.461279,-9.689100,6.778460,-6.062059,-4.842153,-1.516764,-5.136980,7.012184],[3.923949,1.278486,9.458155,-7.520131,-8.427149,-2.122482,-6.557324,-8.439454,3.590917,-8.712460,-4.630702,-6.612072],[-7.893081,3.319942,-8.635495,9.658545,-3.727225,-8.511846,9.235771,7.809522,-4.830425,-9.185989,-5.856546,1.720439],[5.650777,0.088403,-0.188216,2.556691,-5.523261,0.578075,9.219634,-4.283010,-7.521459,-6.973269,3.620370,1.241873],[1.863152,-7.909343,-9.602449,1.350677,2.873372,5.620733,-7.853158,3.093470,1.413472,1.845496,1.777714,-2.185321],[7.080578,8.982361,-6.692228,-2.004443,-6.541887,-4.934811,-1.265929,-5.614080,-8.578237,0.642939,-8.603010,2.053274],[-3.146459,5.626930,-5.519096,1.776813,-3.589647,-0.679982,1.623948,-0.005885,-6.886980,-8.531956,-1.153533,-7.118013]],[[1.018963,2.565290,-1.881707,0.978942,1.689138,-2.378083,1.487344,1.164472,-8.452551,-4.579513,8.017605,7.099324],[1.089113,-2.712802,4.828579,-0.516511,9.930113,-8.792167,-7.160933,-2.856292,-4.905563,9.929074,-4.584923,3.658722],[8.463277,-8.050055,-8.930464,-3.743683,4.221026,5.983046,1.550984,6.966620,9.082295,9.342767,-6.589171,-9.184265],[-4.342327,-3.786553,-7.103831,-8.244797,5.666661,-1.276583,-3.129832,-6.123624,-9.646388,-2.043644,6.295618,-9.000787],[-2.607556,4.148967,1.227675,5.610218,3.281238,-0.405071,-1.139823,5.621320,8.953713,2.888577,-5.220203,7.414382],[-5.214241,3.197906,-6.339337,-5.325294,6.210815,3.996782,8.913874,-5.752906,-2.437969,4.179014,4.250703,-4.820136],[-8.161509,6.279502,0.405217,2.305358,-4.394976,-8.808760,-9.410655,7.210035,-1.084925,-5.341439,-2.833995,-5.952347],[5.119856,7.471875,7.740194,3.655964,9.491021,-1.406942,-4.279346,-9.021878,-0.931702,8.008706,-7.462733,-4.432379],[5.391395,-3.419173,-4.150062,-9.970169,-0.610706,-6.663548,4.814391,-4.548895,-9.403832,-9.223784,-3.740364,-9.087416],[5.021572,-8.155304,-0.908878,-5.753367,2.255054,2.956019,6.419086,-8.371426,3.031519,2.382990,-2.589783,-3.966525],[1.737046,6.512626,1.448792,-2.724031,5.070247,-1.878392,-1.718982,4.330242,-7.699899,1.124727,-1.959376,7.990640],[-9.789224,5.611689,-1.394678,-2.186974,-0.604267,-9.634809,7.448787,-0.113284,6.615017,-4.425072,7.407734,7.025398],[7.246789,2.168879,-1.697355,0.035676,-0.563388,-8.772116,-9.409792,-0.881411,-8.403827,9.965989,7.152731,3.946819],[-5.998632,-1.054038,2.208462,3.589397,-2.235633,4.885102,-7.980651,-6.543020,3.642541,3.422598,8.601134,-8.860371]],[[-9.791971,8.468666,1.431960,-2.292453,-7.608980,6.225524,2.089826,-0.294940,7.262872,-6.926764,0.286443,-2.077898],[0.700596,-0.600067,8.521780,1.114636,-8.895126,-2.346769,7.184921,-1.876597,9.547537,1.705418,-1.232136,3.140447],[0.344237,4.181740,-9.928124,5.073597,-0.484218,-9.260516,-6.982861,9.566886,-4.256358,-0.439626,6.207282,2.267200],[-8.457475,2.493403,4.216175,5.550056,-2.955887,7.398969,-7.874053,7.067708,-9.783459,9.262258,2.815959,-5.755993],[-7.677390,1.432069,2.974712,-9.352943,4.162760,-9.020353,-3.669936,-5.512806,8.677741,4.188240,-3.930875,-7.309836],[-2.811580,-0.889051,-4.283892,3.107507,5.808432,-1.831858,-3.889320,0.844294,-6.133166,-7.679855,1.264644,-2.960976],[-8.111523,-8.936860,-4.475390,5.174791,-3.810132,-5.429425,-0.870046,6.557938,-3.576714,-5.541251,0.782311,-1.437647],[-4.450014,-1.202205,4.499147,-7.220402,9.293939,5.829219,0.923313,-5.419973,-8.721410,-9.841093,8.921118,-3.430577],[-0.981545,-6.298866,-8.777459,9.780388,3.836834,-5.341494,-6.935484,-1.715433,-6.728297,7.212329,-7.972029,1.314733],[-0.505660,-1.482108,-6.900313,3.963175,7.721273,-5.821166,4.938358,-3.339167,6.750948,4.023210,5.086256,0.713573],[7.234070,3.996367,7.109433,-2.267996,0.828820,8.498195,-5.203324,-6.821199,-3.122011,6.552712,-2.651777,-5.862283],[5.539991,-4.412604,4.337714,-7.089734,-4.738638,-0.041625,-2.313065,-4.960010,3.216837,3.893122,-1.343314,-9.396078],[-5.879551,-6.842131,4.373347,6.225855,3.942416,-1.215431,9.757032,1.190888,-7.729326,8.010514,9.871802,-2.704948],[6.963440,-0.975040,5.281514,-7.843254,-2.198318,4.115403,5.529535,-8.414016,-2.958534,5.290430,8.656085,5.617892]],[[1.652742,5.201687,-9.227679,1.099768,8.716876,-2.063867,-4.099178,5.787138,6.054682,9.426698,9.220840,9.567545],[-8.503676,2.815720,-2.411887,6.548234,-4.811629,-3.718097,8.515910,-5.218990,7.431881,0.732378,-3.513356,-2.243555],[2.365638,-5.937106,-2.069923,-2.822456,8.417654,-1.011509,8.462739,2.843058,-7.649471,-6.373132,8.881032,4.880746],[1.309732,2.302064,2.614449,-8.039966,3.845604,6.523169,-1.533935,-5.100744,5.824108,3.348146,-6.876986,-2.254319],[-8.195326,-3.007594,-1.417993,-5.645746,0.681760,9.594308,-0.090896,6.962043,-7.987221,3.932309,9.842613,-3.154914],[-9.010248,7.178272,-1.419401,-6.924601,-4.136862,1.816796,-2.013138,2.344353,9.059839,-2.164567,-5.233659,0.202144],[-1.327953,9.254180,-4.903877,-0.600400,-7.325360,5.347167,-7.972587,5.489878,8.636083,7.926736,2.809720,2.845759],[5.526234,-2.266409,0.281862,-1.039558,-5.229791,9.242985,-1.257034,9.547084,9.619087,6.681322,-6.591707,2.606998],[7.780817,7.536126,6.949855,4.673188,-0.293886,-8.628710,6.538790,5.898413,-1.208270,-8.394153,3.394213,5.307617],[8.889271,-6.784537,-0.642353,2.437375,-2.837158,-2.936622,8.756582,-7.599131,7.922785,2.614905,7.726810,-4.502543],[-2.541562,-8.737666,-0.514116,-9.617173,0.384789,-0.457985,-2.695366,7.147852,-0.806174,-7.682421,-3.485280,-8.315023],[7.824904,-1.628932,-4.248147,1.229032,-8.600054,-2.388633,9.608452,-9.467418,8.886758,-9.391923,-4.997382,-6.559092],[0.384154,-7.847881,2.344795,0.664865,-1.680154,-6.073641,-7.573835,3.729489,5.700795,-8.177413,3.922275,8.770308],[2.326747,-5.830449,-9.905826,-9.965760,-6.503164,1.111702,2.794023,-3.788841,-5.987541,5.723405,-1.355687,5.846787]],[[-2.860549,4.548174,-1.535268,8.752727,-3.848794,5.490626,-5.239082,3.213148,-8.454127,0.054151,0.240121,-0.630207],[-9.080491,6.382116,-9.226540,-0.623899,-3.371674,-9.096649,4.874118,-9.003572,-2.829472,-9.250823,2.250292,2.273684],[-4.563232,-7.354967,-4.052131,5.047600,-3.255274,-8.574627,-4.608905,9.027983,-7.460165,0.173047,3.217902,4.775576],[-3.091657,9.521201,1.439547,7.540771,1.075573,-9.639128,-1.022003,-7.424745,-6.957872,-9.095500,1.270822,3.827580],[2.530078,5.206996,-1.149401,-0.580638,-2.900584,-8.826612,-4.482216,3.111523,0.246533,-4.190190,-5.843668,-9.620729],[9.351487,8.549549,5.122786,-5.646366,0.870547,8.102160,-1.684751,-1.341489,1.265795,0.682519,3.975452,3.109754],[-8.083807,-3.250479,-5.152527,5.595243,2.344703,4.804738,6.524000,-7.063341,3.945156,-5.819614,3.116876,7.820443],[8.305281,1.172632,6.779056,-8.032140,-1.419108,-3.802846,8.392311,-8.748241,-5.641677,9.670801,8.132207,9.991111],[-0.689629,-0.297403,-4.021864,-0.595946,-9.476643,-5.451450,4.043833,4.532388,-6.313348,-9.620464,7.411210,-5.210703],[-6.886553,5.473713,3.098730,6.137435,-6.991777,-2.764775,9.633897,9.968946,-3.395243,1.559323,-6.003942,5.524148],[6.402383,-3.414217,-3.375994,-2.680890,5.489616,-5.212267,-4.190178,-5.706506,7.812345,-5.194030,5.723764,5.947431],[8.909733,5.807104,5.019768,-2.505362,4.196191,-6.668312,-4.354062,-9.089290,-4.745446,-9.298773,-2.483639,-2.968445],[9.735695,-8.352563,-9.029235,-9.930438,7.367697,5.110497,-8.197642,3.661126,-2.479743,1.510653,-7.259645,-0.943369],[-7.755645,-5.245002,2.554256,6.229074,7.262379,-3.405684,9.138824,2.188116,-5.344975,2.412628,3.842310,-6.713153]],[[-3.093507,-7.846683,-0.722698,-8.119324,6.451156,5.621759,9.017450,-6.889878,9.205207,-2.535154,5.490603,5.998848],[-3.117028,7.800403,7.657654,3.624736,1.149949,-6.695580,5.755015,3.171429,0.593660,6.235526,2.055131,5.298439],[-8.884967,1.590943,-4.928204,-8.289796,9.063050,-9.895890,4.178828,3.973624,5.911016,-7.308704,-6.799694,4.889383],[0.488094,-6.826269,-8.084960,3.588802,7.542384,4.406491,6.459646,-7.322425,8.917762,9.911029,-9.485807,0.068575],[-2.488411,-4.985006,1.082416,3.127094,5.684848,8.198405,1.273744,-9.879258,2.298164,-2.553542,6.509546,-9.003714],[7.578098,-0.333141,-7.432591,6.401019,4.161467,8.578372,-8.430830,7.165926,-8.312488,0.319434,4.190179,-4.953493],[5.285627,3.850362,9.198258,8.894843,1.910459,-1.048277,-7.688991,8.707144,-1.768609,-2.624568,0.279471,-5.923590],[2.892318,0.845576,5.792672,8.054142,3.663791,-5.386055,-9.683327,2.555067,1.823889,5.272523,-4.690067,6.838925],[7.012631,9.823615,-4.839212,-6.673085,3.231836,-9.028705,9.680555,-0.260939,0.346664,3.368376,-7.431164,6.224302],[1.111987,5.533297,4.614981,-6.897860,3.974373,2.656001,2.108096,9.851380,-3.282102,5.945957,2.961553,-6.557486],[-7.560270,8.376500,-8.709565,-5.764739,4.023038,9.828755,4.160978,-2.426811,5.240223,-3.171948,6.254897,-8.712741],[5.151701,-6.826356,4.566959,8.498774,-2.297159,-1.275823,-7.351519,-6.453642,7.410965,-4.394961,7.901905,5.002536],[6.473644,7.497619,6.511315,-1.016995,-3.427721,7.665924,0.234201,1.631888,6.462283,-1.678042,0.767541,-2.549614],[6.607856,5.911453,8.148705,9.122205,-3.873397,5.510936,-3.502855,-2.849922,-9.657849,-6.652450,5.339054,-7.742715]],[[-4.125277,-4.197867,4.818207,-8.825004,6.576148,-1.115635,-1.231733,6.229570,-2.315966,-6.614530,-9.346579,0.956172],[-3.882625,-2.416064,-3.823841,2.640333,-7.597863,-9.943840,-0.420130,-3.790881,-0.209116,-0.982703,-6.336651,0.834637],[-2.002821,-2.251343,-4.828127,-0.759363,8.796683,-5.339296,8.649867,-9.550738,8.034317,3.428059,3.378621,-1.192129],[-8.476202,-3.584856,-7.009965,-2.561291,7.158359,-2.281411,-0.769208,4.785934,8.820825,9.794354,9.208341,-7.543308],[-1.395477,-8.621710,0.304500,3.115935,8.909615,3.962358,2.760101,-3.917367,-1.227984,1.298204,2.948246,-4.145373],[-3.077959,2.643830,-9.245273,9.191068,-3.568603,-0.298267,-9.661492,3.484897,-8.275646,4.563003,-6.561925,-9.988040],[-6.147688,-3.944944,-0.438715,4.384787,-9.751691,-6.939848,-3.347157,-7.896124,2.082225,9.705628,-0.389735,0.306444],[8.006658,8.445906,8.535718,-4.995537,0.276230,9.225327,0.228838,-3.148265,-4.851689,-9.080771,-7.015005,4.698220],[-1.864187,6.448437,0.091684,5.715525,-7.623219,0.875154,-2.488169,8.871721,-0.423974,-6.285466,3.300735,0.595291],[9.572151,9.966759,-2.072617,-1.564876,0.683790,-0.986427,-7.468819,2.627967,-3.310795,-0.857782,-8.712743,-3.684277],[0.447722,-1.131401,2.970999,-4.324245,-1.302015,7.428729,-3.196072,4.338025,8.944703,-2.947982,0.640902,-0.167330],[-8.666128,-0.123904,1.180252,6.735916,6.327698,5.776399,-6.696704,-3.320287,5.006326,7.238679,0.463647,3.904197],[-8.815074,-5.685274,7.801094,8.948092,-7.854215,-9.969117,-2.730167,-6.962002,-8.083665,0.998396,0.882643,2.474890],[6.892393,-3.827299,9.148721,5.196551,0.176385,9.067423,6.200708,0.595095,-2.817455,0.202235,0.067575,8.208244]],[[1.021880,-7.073509,-1.080815,-2.572245,8.652636,-3.351996,-6.719836,-8.082898,7.905060,9.672243,7.960098,-8.748720],[-1.949910,-9.329401,9.458517,3.314999,-7.233481,8.029877,7.967537,-2.415153,-0.322313,6.993132,2.625719,7.839320],[0.453889,3.098736,5.709589,9.803282,5.270240,8.434846,5.627905,6.265530,9.842338,-1.204712,-4.427175,7.094108],[0.027306,-6.714192,-8.287729,0.055302,-5.180121,-9.732340,2.987055,6.281263,-2.030940,7.024180,-6.757008,9.892160],[-9.924230,-7.860735,2.726046,0.003464,6.625074,6.568755,5.898767,9.832278,5.416205,5.913103,0.343504,9.135832],[-1.669005,5.012779,5.748775,-7.878177,-2.496318,3.312893,-9.335921,-5.605901,-1.132400,6.051248,3.883189,7.708723],[1.718790,5.095495,7.424979,-1.278317,8.761745,-4.012303,-7.347186,-7.160073,-3.408542,-1.810471,9.084508,-7.723452],[-5.534415,0.956619,-1.864273,-4.968141,-6.280292,2.260848,-6.317248,7.377789,5.054768,9.595598,-9.480204,8.762390],[6.791691,6.768970,-9.884720,-7.913538,8.812697,-2.375061,-8.158528,8.483603,-8.315962,-4.772153,-9.088909,0.364496],[-6.892737,-6.164012,-1.633615,8.920091,0.952726,-3.429712,-7.431145,0.770608,4.609251,1.181622,-4.593561,-4.963979],[6.660838,-9.752145,-1.993441,-5.772392,-9.627893,7.266144,-8.030215,-8.037086,5.913937,7.867434,8.452939,3.233217],[8.952417,-0.527586,-5.143742,-4.496371,6.430523,9.355569,-6.252145,-3.117660,-9.079636,-5.485960,-2.652236,4.797723],[8.746166,3.017915,7.975691,3.691483,-8.510870,-5.930320,-9.794504,-8.131748,2.781930,6.326544,0.360010,-5.918635],[1.701604,-3.577016,4.168159,5.199427,3.224832,7.898030,-0.940606,2.527447,-9.372681,6.820358,-9.544441,8.582725]],[[7.213805,-2.336757,-8.772695,3.170335,4.218826,-7.224839,7.937789,5.761161,-6.253128,9.776284,-2.127699,6.887865],[-3.521078,7.986514,3.081723,5.397387,-4.499345,8.005224,-9.174138,-4.442921,0.478523,7.180048,1.847307,0.682531],[0.657709,-8.906563,1.474787,2.731084,-7.623548,-1.852786,5.403292,-4.773708,8.144341,-2.804501,-0.995817,2.227618],[9.433028,-7.355593,-4.646833,3.486552,-3.386156,4.932855,0.816594,-0.694135,3.426437,9.336295,-6.700663,-1.393558],[-7.557622,9.350328,-2.557307,-4.647161,5.250754,-0.317023,-9.983515,-1.614497,1.963241,-4.282440,-8.961519,-5.927634],[8.653823,-0.006458,4.774344,-5.146993,5.051605,4.608557,-8.567041,-4.715363,-5.345896,8.730463,-0.454961,-7.469035],[9.716233,-6.612638,2.258008,-7.133317,1.526175,-4.755569,9.801334,-3.633922,-1.412799,-6.675897,3.770208,3.566053],[9.549301,-2.778617,-7.327248,1.291525,2.130945,1.408339,-7.981533,3.277324,-9.606511,1.552036,-7.969024,-0.755064],[9.856875,-8.649923,7.463513,-2.679422,-0.458148,-3.158471,8.125171,6.875834,-2.770718,4.215261,-8.719107,-8.393506],[-2.422907,-6.120234,4.016593,-7.487448,-5.319330,5.763049,-9.652400,-5.739803,-2.652203,4.291064,3.614730,-3.508714],[2.925061,-4.984504,-8.174509,-4.399177,-4.906866,-6.527573,4.849528,-2.651499,0.413156,-8.881224,-4.974397,-3.080163],[3.455862,-3.054615,-0.453107,-8.883223,6.343768,2.881703,9.450643,-5.694007,4.309116,9.545575,5.532949,-8.782662],[2.081103,-4.371385,1.891887,-9.378354,-3.105622,5.087518,6.564938,-8.123757,2.748866,2.225477,1.811792,-2.717212],[-6.410608,-8.505232,-3.027783,-0.947685,6.327502,5.279171,6.208331,1.071350,-3.483385,2.911894,0.123078,-6.269719]]], dtype = "float32")#candidate|3862|(11, 14, 12)|const|float32
uop_3863 = relay.log2(const_3862.astype('float32')) # shape=(11, 14, 12)
output = uop_3863
output2 = uop_3863
func_3874 = relay.Function([], output)
mod['func_3874'] = func_3874
mod = relay.transform.InferType()(mod)
output = func_3874()
func_3875 = relay.Function([], output)
mutated_mod['func_3875'] = func_3875
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3874_call = mod.get_global_var('func_3874')
func_3875_call = mutated_mod.get_global_var('func_3875')
call_3941 = func_3874_call()
call_3942 = func_3874_call()
var_3949 = relay.var("var_3949", dtype = "float32", shape = (11, 14, 12))#candidate|3949|(11, 14, 12)|var|float32
bop_3950 = relay.logical_and(call_3941.astype('bool'), relay.reshape(var_3949.astype('bool'), relay.shape_of(call_3941))) # shape=(11, 14, 12)
bop_3953 = relay.logical_and(call_3942.astype('bool'), relay.reshape(var_3949.astype('bool'), relay.shape_of(call_3942))) # shape=(11, 14, 12)
var_3967 = relay.var("var_3967", dtype = "bool", shape = (11, 14, 12))#candidate|3967|(11, 14, 12)|var|bool
bop_3968 = relay.left_shift(bop_3950.astype('uint64'), relay.reshape(var_3967.astype('uint64'), relay.shape_of(bop_3950))) # shape=(11, 14, 12)
bop_3971 = relay.left_shift(bop_3953.astype('uint64'), relay.reshape(var_3967.astype('uint64'), relay.shape_of(bop_3953))) # shape=(11, 14, 12)
output = bop_3968
output2 = bop_3971
func_3973 = relay.Function([var_3949,var_3967,], output)
mod['func_3973'] = func_3973
mod = relay.transform.InferType()(mod)
mutated_mod['func_3973'] = func_3973
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3973_call = mutated_mod.get_global_var('func_3973')
var_3975 = relay.var("var_3975", dtype = "float32", shape = (11, 14, 12))#candidate|3975|(11, 14, 12)|var|float32
var_3976 = relay.var("var_3976", dtype = "bool", shape = (11, 14, 12))#candidate|3976|(11, 14, 12)|var|bool
call_3974 = func_3973_call(var_3975,var_3976,)
output = call_3974
func_3977 = relay.Function([var_3975,var_3976,], output)
mutated_mod['func_3977'] = func_3977
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3874_call = mod.get_global_var('func_3874')
func_3875_call = mutated_mod.get_global_var('func_3875')
call_4002 = func_3874_call()
call_4003 = func_3874_call()
output = relay.Tuple([call_4002,])
output2 = relay.Tuple([call_4003,])
func_4017 = relay.Function([], output)
mod['func_4017'] = func_4017
mod = relay.transform.InferType()(mod)
output = func_4017()
func_4018 = relay.Function([], output)
mutated_mod['func_4018'] = func_4018
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3874_call = mod.get_global_var('func_3874')
func_3875_call = mutated_mod.get_global_var('func_3875')
call_4082 = func_3874_call()
call_4083 = func_3874_call()
const_4084 = relay.const([[[-3.962917,1.421827,2.579476,-1.395615,3.416175,-0.421823,5.742275,4.791628,-6.418739,-0.394507,-5.306382,-7.593996],[2.150505,2.081784,9.898510,8.668090,1.589561,3.600640,-9.657461,-3.907513,-7.381652,-4.963763,-6.382571,7.602923],[-3.801560,3.152681,8.180858,6.650366,-9.860592,7.625934,2.273253,8.233342,6.788336,-3.116657,-3.348208,-1.106765],[0.723660,4.318304,-7.700590,1.554266,-1.271404,3.320414,-1.366354,-3.988294,-8.712711,8.004354,-4.116104,-9.431394],[8.815585,9.219415,-9.843326,-2.172714,-9.336530,7.418756,-1.984088,-0.895238,0.068182,-7.386833,-7.110318,-8.948451],[-2.884121,9.164265,3.568652,7.215666,-5.376457,-3.568726,-7.823069,-4.043721,-3.254807,3.019073,-1.774195,1.101431],[1.855023,-0.133257,7.484633,-9.945058,-3.753045,-5.314793,-6.548712,-0.265201,4.595279,4.686962,9.391241,-7.797629],[1.903986,-6.452323,5.956539,-1.168644,-8.883121,2.647319,3.281447,5.111903,1.923655,0.872739,8.069476,-3.956222],[5.943392,-9.366075,7.637531,-8.829491,-4.229670,5.090812,7.678486,7.315218,-0.665785,9.112950,-8.069123,5.509877],[-1.466868,0.565945,-6.760917,-1.204889,4.987132,-3.601308,-1.969313,-0.192868,8.796572,-8.161976,1.233376,-2.331607],[-1.976188,5.545222,7.860452,-7.843598,-5.604687,4.919925,0.840865,-7.807409,9.177243,-2.332969,3.242747,-1.938965],[-2.288181,8.223146,-3.431131,9.035946,3.453494,-4.245265,8.489112,7.642233,-5.058493,-0.020196,-1.256011,0.213381],[0.632838,4.157587,-2.537563,7.099495,0.916979,-0.184038,4.614722,-3.070752,-1.833899,8.793476,-2.554478,7.721366],[2.935103,-2.467064,-8.694411,1.769470,5.560267,3.939384,8.966823,-1.233996,7.564619,-5.677727,-2.572149,-0.308116]],[[0.277240,-0.820515,-8.758974,3.013831,8.232812,7.339094,0.179411,8.390960,-9.148962,-0.772079,-8.092183,-5.067713],[4.915930,-6.340083,5.396066,-9.186085,-0.762411,-0.543325,4.822605,-8.854877,-5.445137,-3.706086,6.040548,-7.620229],[-6.518003,4.960958,-5.880443,4.085498,-4.630957,6.853813,-3.384010,7.582482,2.932860,9.951066,1.886241,7.769690],[9.926831,4.513145,-2.490849,-4.479387,-4.053672,8.890663,2.801777,-0.937714,-5.889006,-6.412753,8.691080,1.699492],[6.532371,7.857986,-2.623036,-6.318588,3.393066,-8.485209,-5.800176,-5.349250,-5.935651,0.125276,-0.329666,-0.913553],[3.998241,8.461095,-9.615830,5.767542,0.191724,-3.156654,-8.138064,-6.085050,-6.345477,9.575801,5.755815,5.542704],[3.259812,-6.855518,-5.615503,-8.953706,2.536590,-0.993946,-5.775757,7.494481,7.334990,8.084180,5.591154,7.192579],[5.412592,-6.808021,-7.286044,-3.552513,-5.271033,-8.426788,5.148983,-6.309060,-3.195608,-5.944076,3.379474,1.493712],[6.884389,-7.884356,-6.008444,-4.619268,-2.125881,-1.576237,-9.923613,-3.097946,1.247526,5.399137,8.541134,9.916543],[0.747123,-7.391528,-4.516319,0.060410,-7.043730,-9.425222,3.665683,-7.974093,2.991222,-0.029042,-1.051736,-2.804229],[8.091467,-3.111895,4.226491,3.924236,-2.780687,0.647073,7.789586,-4.245880,-7.458785,-9.448728,-2.052239,2.069434],[9.214931,1.722399,-6.411269,-5.826091,-9.816180,-8.050072,-7.331975,-7.031866,0.639737,1.901519,-8.455198,5.397351],[-2.760093,-3.600281,-5.163817,-1.054586,0.801740,4.646064,8.303099,-1.146213,9.126992,-2.543804,-4.048888,-9.902862],[-3.247975,-6.828802,4.906306,-7.009288,6.533449,-6.256039,-2.777190,3.425029,3.993808,-8.643934,-4.912617,-4.325512]],[[8.922225,-6.945988,9.159191,-1.402029,-3.687650,-3.831406,-6.213769,-9.954960,8.371016,3.336513,2.351129,5.372781],[-8.350073,-5.674222,-5.009598,-3.643545,0.238433,3.714019,7.655378,-8.249049,-5.401557,9.901807,9.382966,-5.363785],[7.306817,2.169485,2.132755,5.595842,-7.969005,-0.813976,-7.122339,-8.156174,0.604516,-0.412402,2.251555,8.272027],[2.538843,-9.654556,-3.656962,3.124547,5.535496,-8.431984,5.698308,-5.011775,7.388967,7.202669,7.784053,4.172147],[0.413297,4.379677,5.574316,6.049824,0.921593,1.176471,-9.991001,9.669495,6.171191,-6.217892,4.719715,-4.454684],[-9.906501,-5.620715,-2.106284,-2.010600,1.190646,-4.115144,-2.055288,2.213724,-4.851451,9.117949,1.031301,-8.387492],[7.671841,-0.549607,3.519215,5.767296,-5.406464,8.064332,-9.992752,-8.090433,4.619401,-1.731559,-8.192914,8.059555],[-7.683353,-7.812583,-6.775192,7.725933,8.343948,-1.200967,-6.309665,-9.458831,-4.615955,6.287297,-9.067833,-5.958213],[9.422559,8.098720,0.819085,-6.871075,-6.114523,3.619932,8.205008,-4.472070,-0.029847,8.679338,-2.603799,2.073191],[3.784507,9.612025,5.362965,0.224164,-0.112494,-6.163564,6.642662,-8.918925,1.899832,-2.003754,-9.218476,-0.044270],[-8.564243,1.496176,8.445115,5.323820,-0.261652,-5.521868,-7.231234,-4.379052,9.702167,-9.691158,6.358024,-2.266558],[2.221279,1.983224,8.029664,-8.404658,2.134951,-8.861029,5.467490,6.903878,4.603384,8.483405,1.057441,-0.620305],[-4.745681,8.207892,4.648675,2.852808,3.476436,-7.354855,-6.466778,-6.417502,1.629339,-5.634246,-8.905157,-2.839487],[-7.984610,1.178565,7.596173,-6.372314,6.551616,3.846775,0.980333,0.543330,9.836354,5.516800,-8.635403,5.159407]],[[-8.760346,-0.443582,1.977806,-4.234728,-8.457287,3.226097,-9.538941,-4.702826,7.393412,-4.348878,-2.158713,8.760536],[-7.661478,5.452028,-2.447761,-5.044630,-6.080908,2.510256,7.684249,0.827512,-7.193931,2.823962,-2.307623,-2.832742],[7.102092,-9.072311,-7.529414,0.191716,-4.951643,9.902298,2.365772,-2.894404,1.905582,0.310863,0.309079,-6.170844],[6.518938,-9.214531,2.321442,0.361514,-5.592403,-1.412953,-1.806743,2.873193,-6.128190,7.743176,-7.047177,-3.042933],[-0.193687,-9.737693,-2.570645,8.948473,-2.298401,-5.602392,-8.054203,-7.173106,8.628444,3.862113,-4.089548,3.917375],[1.431589,-7.020485,-9.888185,2.675797,-7.157305,-3.869766,0.771034,-4.684453,-9.869929,8.212142,-8.804028,9.189628],[4.737784,1.406824,9.548409,-2.319243,-8.668136,-1.167477,4.982076,9.239107,2.945106,0.395363,0.806417,-3.590603],[-0.473272,-9.520712,4.525780,-5.421894,-5.911196,-7.441475,-4.439798,-6.416852,3.421825,5.365089,8.230867,-1.751745],[2.011387,6.346439,5.151638,-1.627373,6.525002,-1.400644,-8.193299,2.836154,1.997623,-4.073176,8.323041,-0.245340],[0.686077,0.638357,-4.353247,6.713319,6.429964,-9.902274,-6.911005,-6.313858,8.225011,-7.305055,-8.602889,-3.578024],[3.248998,5.566479,1.043820,2.039410,-7.240606,5.078370,-1.805139,-7.179994,2.588209,-8.764103,5.823982,-7.661779],[1.038237,-4.140171,-9.343689,0.988771,5.940158,-9.480003,-0.059715,4.446848,8.788308,8.859050,2.968768,5.059198],[-0.634285,-7.053586,1.285959,-1.756867,4.946418,-1.735963,1.415295,5.801130,-1.522714,-2.145769,8.623201,4.818664],[-8.589317,-5.787402,-3.025495,9.335904,6.679009,-1.959487,-5.664885,2.727638,3.893881,3.603280,-7.042239,3.019137]],[[6.678301,9.510778,5.360144,2.275274,-7.328818,7.323883,4.335478,7.835869,-8.184749,2.719886,2.279557,-9.927397],[-6.616610,4.530704,-8.456630,-1.151788,-3.757507,-5.087608,-1.618521,-7.089572,8.030270,-7.207990,-5.373145,6.571034],[3.142859,5.047194,-3.679268,-5.431547,2.804297,7.002526,-8.999387,9.345800,2.413942,8.299080,7.456357,-5.437159],[7.487352,-6.318631,6.896462,3.723864,-9.221042,5.082002,-2.480160,-2.730800,7.994524,-9.812662,4.748166,7.702244],[9.674358,-6.013338,-6.927318,-8.296367,5.812270,7.120580,-6.738499,-7.609691,2.370269,6.067434,4.137972,5.728611],[1.109258,-4.450537,-5.739962,-9.820295,-3.977719,-3.518883,6.236971,5.505611,8.988782,7.083602,5.722654,9.677713],[1.530799,-8.457562,-5.200831,-7.936249,6.319425,-4.779562,-9.934892,-7.003728,3.171790,9.931179,9.906411,-7.895693],[6.900353,-1.240300,9.796133,1.234196,0.150162,1.799952,7.722665,2.181518,-0.978463,-6.007895,-5.741897,-7.499245],[-6.632771,3.887473,-2.437366,-6.726580,7.665907,-3.057970,-3.945478,-6.628272,1.644554,5.906280,9.548201,-1.727512],[-4.524086,-3.518079,1.242908,2.885357,-0.143861,1.106163,-6.721873,-0.798308,-7.075056,-8.209615,-5.158546,-4.884637],[-2.985826,-2.475223,2.903306,1.535124,-9.798784,-5.707041,-4.946195,2.050132,-6.830427,3.667203,-7.216742,3.698383],[-4.436631,-1.210896,-9.408173,0.660676,-3.265204,-9.984037,-7.543331,-6.289684,3.299982,-9.698088,-0.991360,-9.627821],[-6.813781,4.994780,3.445352,7.032737,-9.812726,-3.202722,7.613485,4.796840,5.355484,8.984240,4.348787,-4.689964],[-4.239800,3.855358,-7.755154,-4.474819,3.235913,-2.317338,-4.922955,7.913078,2.242560,8.816952,9.886542,-3.426459]],[[-7.359480,-3.033461,3.951283,-5.443893,5.860166,-7.140592,5.462965,-0.636369,-3.772719,5.849931,-7.179966,0.507044],[-2.882126,-0.895308,9.669528,-9.212928,-1.595792,-0.964522,-8.577027,-2.118701,-3.883375,3.182803,8.237234,-3.526056],[-6.811036,-4.853011,-2.085939,-7.635378,-7.787638,-2.997915,-9.395991,9.785021,0.813629,-1.676824,-4.878591,0.307473],[-7.489506,-0.051047,-8.631044,8.572750,-5.800431,-4.438596,-4.974924,8.061515,9.649019,-5.494117,-5.478009,4.784597],[6.949936,2.688810,-4.895419,-0.072391,-3.073867,-7.170688,-0.046253,0.746118,6.685994,6.181328,4.664179,-2.880561],[3.240612,-5.208030,-1.876372,6.486867,6.295580,8.829793,-6.986903,-6.567677,-4.434024,7.870600,6.431915,7.073124],[-2.855099,-1.733171,9.230472,4.420765,8.185146,-5.688098,3.383945,-4.645101,2.037827,-0.605893,5.557640,-2.378907],[3.446007,-3.936515,-5.690898,3.850330,4.586227,-1.642830,-1.978032,7.594979,4.023769,8.668243,3.080507,-8.101102],[6.403228,-1.380082,8.426877,-9.477597,5.763795,7.806592,-0.577561,-7.087306,-5.836171,-2.312974,-5.720172,3.889851],[7.671189,-8.502185,-8.532737,2.558463,9.720708,-4.831447,-1.845474,4.242224,-2.189504,-9.848771,5.854301,-6.435893],[2.288812,-0.780522,-4.631931,-1.965634,-9.619885,-9.863464,2.304333,-7.583942,-1.763139,6.594458,7.778681,-5.955944],[-1.487779,-1.580076,3.665900,5.833110,3.242457,9.731319,8.097281,-6.739682,-5.682563,-5.120487,-7.652092,7.219923],[-0.529258,-9.501257,6.425183,3.110780,0.005428,-1.839093,-5.577939,8.960536,4.450796,9.266549,-6.418595,1.260575],[-5.808315,-1.568281,-3.898064,6.998311,4.014019,3.203621,-5.984124,-5.129808,-9.101723,2.297662,-1.908660,1.437869]],[[6.023419,2.163382,-3.139760,-5.595362,-3.389190,8.046929,-2.875348,1.714675,-7.553433,6.936352,4.523438,-4.383079],[-1.395134,-1.662508,8.124304,-3.096357,-2.141591,-6.686846,-1.976978,-2.866960,-4.436976,-8.352714,-8.553487,-3.018253],[-4.050412,-2.493463,5.751260,8.049547,-0.103781,-8.995157,3.480648,-9.642855,-0.109562,-7.610160,3.892882,-3.952728],[2.681970,5.737756,-5.636123,-1.084942,3.995983,0.708318,-4.197979,-3.033311,-2.327729,-2.867121,7.033491,-2.620938],[5.521900,8.786263,5.833953,-5.640007,-2.938404,-4.412855,6.039196,3.540466,6.920912,7.048842,3.199781,-3.912350],[6.470094,-0.856730,1.353944,-5.641257,8.441124,-5.463906,2.021171,0.096244,-8.816047,4.936069,0.912320,-1.873335],[4.729763,-7.388740,1.242244,-9.497070,9.420987,8.626607,8.744923,4.847190,9.041114,6.171026,7.396531,-8.088580],[4.294837,5.112757,-7.233010,6.777294,-7.292028,5.315122,0.917769,-3.605377,-4.663960,5.152244,5.726653,-5.695692],[-7.037623,-4.729806,2.128144,3.804091,-3.138294,4.235977,-1.981438,-6.140900,-6.921790,-5.037646,4.740359,-4.887030],[9.877220,-4.694048,-7.937608,4.047263,-0.077410,-0.343263,1.006749,-2.051315,2.518630,-2.603540,6.536563,-2.311963],[-4.944160,5.291497,4.401168,4.700236,0.626871,4.890983,8.551609,5.652075,-4.072832,9.313318,3.120483,5.596398],[5.335806,7.404087,-8.116393,-4.465822,-1.773421,3.565791,1.766859,-8.467025,-8.406141,-2.403518,2.857340,9.661374],[-4.976105,5.947832,7.555167,-2.658421,-5.156959,9.859787,6.001477,-2.854645,6.547492,2.977752,-1.498456,3.979364],[8.727572,-7.695042,5.147909,5.059042,-6.115795,-7.945233,5.612202,-1.622724,-3.102989,7.651773,3.251184,0.885274]],[[6.892186,4.819056,3.613229,-5.810106,2.717668,0.070050,-5.679864,-2.841778,8.826013,-3.348958,5.270691,-5.536403],[-4.886472,1.082902,2.328292,-3.117531,6.275078,2.125482,4.865144,0.441396,-2.938904,0.961624,6.071586,-1.871759],[-2.823383,-2.505408,9.337536,8.472986,-5.722624,-7.423851,-9.645303,-5.938335,-8.020350,-2.146931,5.673632,-2.622993],[-8.926807,-9.192603,0.285954,-0.761147,-2.726589,2.669174,8.739977,1.974225,0.518258,-8.410067,1.986827,6.495732],[-9.752178,3.871166,-8.778542,8.606400,4.334872,-5.371246,-7.972066,6.405266,9.699693,8.962263,7.000401,-4.515386],[-1.481701,-5.823608,5.438413,5.532752,0.708811,3.305464,2.104241,-2.770903,0.037535,1.740317,5.242982,-1.570530],[-6.194441,-3.652155,-0.818108,-0.723920,0.676660,-7.572410,8.296520,-4.644405,-3.385993,-9.161523,-4.615651,0.381344],[3.170789,-6.233721,3.767418,-2.362774,-2.625249,4.785475,6.034328,1.443763,3.809459,-2.455493,4.540756,9.704866],[-7.123242,5.754250,4.886471,-8.137954,-5.915386,6.276540,4.580612,8.294241,-6.821554,2.181862,-9.141106,-8.533111],[-6.894421,-8.844662,5.824866,-2.176688,6.008230,0.316956,-7.266181,-4.106413,-1.256639,-8.556045,0.787566,6.768666],[-5.880654,4.709853,1.937865,-4.093213,-9.179514,8.230321,8.045321,-0.059921,-8.116105,8.872270,0.829608,3.440252],[1.476754,-3.453685,6.878098,5.139889,-3.675022,-6.494615,-1.403864,8.916909,-5.115599,9.313734,-4.579398,-2.774456],[0.879536,6.891432,4.458857,-2.805755,-7.634827,8.791001,-0.678264,-5.762409,-6.780097,-5.524099,0.302472,9.769084],[-0.309361,3.457762,-9.030600,5.889378,2.943892,0.831756,0.606422,-2.882881,-4.787130,7.474044,-9.969589,4.706127]],[[9.595631,4.996592,6.222238,-2.447149,4.274364,9.317684,9.388549,7.718751,5.301720,-4.807060,-5.940168,5.279011],[-6.226479,3.604163,-9.390997,3.949400,-5.183194,-5.634298,-0.543724,-2.648235,8.923808,2.140503,-1.116958,2.550779],[5.490141,8.521314,-4.874835,-9.491483,3.162701,8.391890,-0.056669,7.561414,-6.772634,8.459766,-7.548420,-0.070780],[0.004469,5.959702,2.604351,5.827450,-5.991015,-4.036318,4.947860,6.173157,9.307135,-2.515279,-1.829803,-2.388311],[-7.714420,2.384911,4.292029,-3.956730,6.228567,8.493767,-8.689431,-5.688979,4.159965,-9.104084,7.864525,4.824561],[-7.773178,5.273733,-5.812584,0.251512,7.573612,4.607939,3.920728,5.349837,0.350546,9.258486,4.217840,-4.472048],[-5.979769,-3.332150,9.604785,-5.983416,9.570797,-9.203542,-7.063052,-4.729565,-6.127364,-5.259702,1.157134,-1.357175],[-3.999354,1.439708,8.953147,-8.465616,-4.207301,-3.607295,2.126409,3.158038,-4.562328,-9.262613,-8.839306,-3.802125],[-9.174753,-8.641774,-4.914145,3.669381,-8.986242,-1.216771,-2.008937,2.308859,2.621816,-8.378012,4.776770,-3.809400],[4.750635,-6.992791,1.340813,-6.671492,5.394217,-3.119133,-0.222165,5.366321,-4.922932,-9.800828,-9.559647,1.950588],[9.426002,-8.715601,8.888477,-0.252187,7.018729,-9.074432,7.453161,1.831925,9.772718,-1.994078,9.507683,-1.835728],[-1.533498,-3.010536,5.039610,-1.004719,-7.784201,7.988416,5.144914,-4.638187,-5.177640,-0.201181,-4.377864,-3.956847],[3.366019,0.449458,-8.401577,-6.738188,-5.803768,-0.942199,-6.513754,1.474930,8.735256,-7.247939,-5.260147,-8.963096],[-3.145862,5.396764,-1.639465,-1.511636,-6.374481,-5.736319,-1.331035,8.680038,6.638419,-6.802107,7.081543,-8.036668]],[[-0.314303,2.417469,-8.911008,2.126269,-9.719670,4.393881,-5.549140,-8.008518,1.161474,-8.351852,3.170172,-5.494681],[8.385798,-6.208536,-0.455260,6.296962,-1.909044,-3.148981,-3.742418,4.558471,-9.902177,7.956112,-4.231377,8.214572],[-0.703214,9.704700,-0.943116,0.154112,-5.071717,-0.388468,-9.247565,2.528538,-1.867852,8.336500,3.538664,-7.947445],[7.153832,8.930122,3.823521,8.698992,-6.120735,-5.819617,9.129655,-1.941794,6.403899,-3.071146,-3.564952,-7.588146],[8.631573,-7.617178,-7.842035,-1.484148,-8.420608,-8.976277,6.149258,-4.859737,-6.784304,-1.915018,-3.738906,-9.193531],[1.411197,1.349478,-7.691808,-5.053537,-6.770590,7.897501,2.990620,-8.145875,4.090255,-1.018405,4.464380,-4.378738],[7.994707,2.764946,8.588590,1.232940,-6.030335,-5.877024,8.441309,2.123756,8.126437,-6.312665,-6.161101,7.344698],[5.423341,-5.072642,-3.657357,0.193123,1.043249,7.670521,-3.791807,8.177596,4.506785,0.378984,4.169956,-9.653773],[7.271032,2.932065,-0.722739,0.824705,-8.478145,-2.932182,-6.415584,-5.580136,-0.141974,-0.854106,1.077656,2.235527],[-9.058332,7.862361,0.699338,-1.064079,-7.951318,8.034809,-4.556488,9.197068,-7.817704,3.597143,4.730173,1.506637],[7.766443,-5.890027,1.671140,-4.303806,-6.332079,1.090897,4.286940,6.941592,-7.422692,-1.059133,1.700636,0.961824],[7.485759,7.780756,9.074620,-0.655963,-0.508296,9.667988,0.808815,3.891749,9.420225,5.611453,0.972272,-8.005795],[3.780505,-0.539303,-9.666416,4.199570,9.245600,-3.941529,0.901226,6.460292,4.200908,6.166529,-8.346036,1.423749],[-7.910297,3.407979,7.488264,0.227719,-4.416723,3.991890,8.741876,6.165462,3.940666,7.621095,-0.039080,3.678634]],[[0.637935,-8.853567,5.416426,6.456781,5.010026,3.486621,1.221970,8.098522,9.413213,-4.080437,3.822465,3.293897],[-5.703249,9.776592,2.688930,-1.538552,-9.534075,8.944612,-1.573889,8.232612,8.229155,-2.147727,9.988594,-0.368341],[2.406267,1.508973,-4.483783,2.334814,-6.325834,-5.919286,4.354545,-1.246298,8.485175,-3.520095,0.508445,3.766835],[-4.820283,5.625035,-6.945540,-4.022102,-0.769628,-3.824626,-6.572677,2.312922,5.493177,9.191645,0.254890,-3.732374],[9.588853,-1.796442,-9.405248,7.157940,-6.413855,-9.865396,-3.353005,-4.866002,-5.774072,-5.373205,-2.299908,2.673040],[3.372875,4.612641,3.129512,4.107395,-4.774817,4.777726,-1.735531,0.159451,9.434088,0.375977,6.387943,-8.211990],[-4.128229,-6.183344,0.442239,-9.232344,-7.628436,5.180455,2.152597,-8.031402,-9.125497,-7.408331,-7.962159,0.087648],[9.165162,-7.623832,-7.401991,2.728691,5.070506,-1.812596,0.275600,7.280844,-0.751582,6.161028,4.941641,0.111524],[5.532278,-4.107323,1.686232,1.580659,-6.191310,9.339377,9.916466,-3.661097,6.604417,1.652315,3.169478,-4.515281],[7.244097,-4.675003,-8.464278,-5.354492,1.695016,1.429465,4.299955,-0.380303,-8.415263,-8.355656,-7.788281,-4.433872],[6.957466,-8.739145,-5.602174,-1.853810,4.483601,8.137395,-2.846048,0.542502,-5.663798,8.122889,-0.466926,-3.548377],[3.407256,-3.079976,5.638383,5.320830,-5.588195,6.540473,5.525070,-1.690939,-9.105137,-5.134707,4.282648,1.172993],[-8.126454,4.161693,-7.593455,-6.291929,0.413880,0.069037,8.805656,3.919270,-8.930244,9.100123,3.488669,-6.423667],[8.560731,-6.957036,1.050551,-3.184431,-1.093428,-1.104775,9.485596,4.659938,2.154616,2.845244,1.155913,-4.670427]]], dtype = "float32")#candidate|4084|(11, 14, 12)|const|float32
bop_4085 = relay.mod(call_4082.astype('float32'), relay.reshape(const_4084.astype('float32'), relay.shape_of(call_4082))) # shape=(11, 14, 12)
bop_4088 = relay.mod(call_4083.astype('float32'), relay.reshape(const_4084.astype('float32'), relay.shape_of(call_4083))) # shape=(11, 14, 12)
output = bop_4085
output2 = bop_4088
func_4089 = relay.Function([], output)
mod['func_4089'] = func_4089
mod = relay.transform.InferType()(mod)
mutated_mod['func_4089'] = func_4089
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4089_call = mutated_mod.get_global_var('func_4089')
call_4090 = func_4089_call()
output = call_4090
func_4091 = relay.Function([], output)
mutated_mod['func_4091'] = func_4091
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4104 = relay.var("var_4104", dtype = "float32", shape = (14, 3, 1))#candidate|4104|(14, 3, 1)|var|float32
uop_4105 = relay.tan(var_4104.astype('float32')) # shape=(14, 3, 1)
func_3874_call = mod.get_global_var('func_3874')
func_3875_call = mutated_mod.get_global_var('func_3875')
call_4114 = func_3874_call()
call_4115 = func_3874_call()
func_2822_call = mod.get_global_var('func_2822')
func_2825_call = mutated_mod.get_global_var('func_2825')
const_4135 = relay.const([-2.279920,2.333930,-3.980977,-6.338857,3.510173,-9.978033,-4.517356,3.406109,6.688836,-6.857291,-6.594268,1.291745,-4.379889,7.962672,-0.021296,3.159065,9.392803,-5.943895,0.546234,-9.105607,6.845987,-7.343088,6.738945,9.427675,9.102977,1.403413,1.001249,7.664400,3.015407,0.305023,2.280428,-4.330017,-7.267449,-7.290615,5.919696,-5.586596,0.828924,6.162384,-1.333242,9.779103,-2.066458,5.791170,-5.015060,3.521440,4.852859,4.268049,-8.802481,9.513169,9.381622,-5.567366,8.659198,3.029415,6.115385,1.007734,1.172697,-1.303786,-6.781724,7.295093,-4.416133,-4.470756,-0.609322,-5.090503,2.394854,5.963753,8.987327,7.760452,-2.247341,7.477850,8.207894,9.470912,9.755715,-1.223485], dtype = "float64")#candidate|4135|(72,)|const|float64
call_4134 = func_2822_call(relay.reshape(const_4135.astype('float64'), [4, 9, 2]))
call_4136 = func_2822_call(relay.reshape(const_4135.astype('float64'), [4, 9, 2]))
func_449_call = mod.get_global_var('func_449')
func_453_call = mutated_mod.get_global_var('func_453')
var_4142 = relay.var("var_4142", dtype = "int8", shape = ())#candidate|4142|()|var|int8
const_4143 = relay.const([-1,1,10,-7,7,10,2,-3,6,-9,1,-4,-2,-8,-7,2,-5,-2,-1,5,2,9,7,2,5,8,3,1,-2,2,-2,-7,-9,6,-9,-7,8,4,-5,1,-2,-6,-10,-8,-7,-2,-7,8,10,-6,-6,-2,7,2,-6,2,1,-3,-4,-1,-3,10,4,6,3,-4,2,-3,-4,3,-7,10,-2,9,5,-8,5,-8,9,2,3,1,2,6,-1,7,-5,-8,-1,-4,-6,-5,-2,9,-7,1,7,-7,8,-6,-4,8,2,-6,-2,-1,3,-1,-9,4,9,5,-1,-4,8,9,5,-1,5,1,-8,-8,-10,-5,9,-4,9,4,-2,9,10,-1,-7,-3,-10,8,9,-10,-4,8,6,-4,1,-7,8,-2,3,-7,-8,1,-7,7,-8,6,3,7,-6,-6,-9,-10,8,9,-9,-4,-7,6,-7,-1,-1,-6,3,-4,2,-5,-3,-2,-9,2,7,7,-2,-9,6,-1,9,9,-9,-8,-3,6,10,-6,-10,8,-4,-3,-8,3,-4,-10,2,-2,2,-5,-3,-10,-8,-3,-5,-10,-6,7,-7,7,-7,-2,-6,-1,4,-5,5,-9,4,-5,-3,-1,-8,-2,-9,4,-5,4,-1,-4,-10,-2,-6,10,-3,2,10,6,10,-2,-8,-6,3,6,4,6,1,-1,-9,9,-7,-9,-4,4,-4,6,3,6,-1,-9,-4,-9,3,2,-10,-7,3,6,2,5,8,-9,-1,-8,-9,7,4,-8,7,-10,-10,8,2,3,3,1,9,-2,-2,3,7,-5,-10,-7,-3,-8,5,-8,-7,10,-1,1,8,-2,-4,-4,-7,-4,-1,5,-2,-9,-6,-4,2,-3,5,-4,-7,-5,-1,6,9,-6,2,6,-4,-1,-4,5,8,-10,2,-6,-10,2,2,-1,9,-3,9,-7,8,7,-2,9,-2,3,-1,-5,-1,-2,6,-6,-1,5,2,-6,9,-2,6,3,10,-2,-6,-4,3,-2,1,3,6,-3,10,-9,-1,-2,-4,-4,10,9,-2,-4,1,5,1,4,-6,8,-4,-4,1,3,2,2,-5,9,4,-4,7,-6,7,-8,5,-10,-4,-6,-2,-10,6,6,3,-9,-7,3,-4,2,9,6,-5,-2,3,-2,7,-9,4,-4,-3,5,8,3,4,-3,5,-6,-6,-9,-8,-5,-5,-8,2,-5,7,-4,-5,-6,4,4,9,-2,-10,-7,4,-3,-6,7,3,4,1,6,9,-8,1,4,4,8,-7,-4,7,-9,6,-3,-7,10,9,5,-8,-2,-7,-1,-2,-6,-4,-1,6,3,5,3,-7,1,1,-5,-1,9,3,10,1,-8,6,5,9,-8,-8,-8,5,10,-5,4,1,-5,-3,2,3,-8,-9,-5,-5,-5,-3,5,-2,4,1,5,-1,-10,9,8,-2,-3,3,1,8,-8,-7,-6,1,6,8,-6,6,-3,8,7,2,-2,5,-3,-7,3,-8,-5,-1,-3,-4,7,-4,5,4,3,9,10,-9,8,-8,2,-1,6,-7,10,7,3,8,7,-7,7,-8,-1,-4,4,9,-9,-4,2,-6,-5,10,8,6,-9,6,1,2,2,1,9,4,2,-5,-9,9,-3,4,6,-7,-2,-8,8,5,8,-5,-7,5,7,6,-2,-2,3,-6,-5,-3,-7,-2,-2,2,2,-9,6,-10,5,-1,-2,-1,10,-5,2,3,-8,-4,-1,-2,-4,4,6,-5,2,7,-8,3,8,4,-8,1,4,-8,-10,10,3,5,9,-10,5,-7,6,10,9,-3,-5], dtype = "int8")#candidate|4143|(672,)|const|int8
const_4144 = relay.const([[-1.860889],[5.370676],[8.346092],[1.881744],[-2.855607],[2.330558],[-8.432457],[-7.206894],[4.458694],[-5.149617],[3.505539],[-2.539830],[2.975284],[-9.243657],[-6.443561],[0.812384],[-0.562874],[-6.687304],[-1.163657],[-2.975102],[1.412954],[-4.979927],[5.248294],[-8.498139],[8.860672],[-1.556988],[-1.194137],[-6.492662],[-2.068394],[2.530038],[7.472496],[-8.651030],[5.817058],[4.826813],[-4.649646],[1.898307],[8.082987],[1.387093],[-0.085212],[1.112020],[-9.948608],[-1.289178],[-5.313604],[3.807295],[-4.555827],[-2.044901],[2.983031],[5.308873],[2.722464],[2.776855],[0.799589],[3.594972],[-4.238993],[6.245953],[-5.130483],[-0.934154],[-8.577425],[5.036789],[2.520479],[-6.426872],[1.586713],[4.097254],[1.860267],[-5.781845],[4.962771],[-4.453984],[-1.976286],[8.046729],[6.624853],[6.667179],[-4.697899],[-3.022775],[1.376689],[1.013895],[-4.764681],[-5.024606],[-4.225027],[7.717325],[-7.601342],[-3.812378],[7.829817],[-5.612930],[4.227691],[-5.523528],[-7.275508],[-8.010438],[-0.938226],[-2.939352],[5.369818],[-9.505279],[5.089404],[2.135660],[4.813145],[1.688148],[-0.299957],[3.295624],[-8.568213],[9.631455],[-2.198955],[-3.928991],[-8.772294],[0.431627],[-4.471559],[-5.792811],[1.546133],[1.924873],[9.066800],[9.153990],[7.604756],[-4.885173],[-7.359068],[9.974556],[-7.497533],[-9.079732],[0.815686],[9.459764],[-6.378648],[-1.316973],[-8.848627],[-4.271964],[9.160314],[-4.986482],[-6.214366],[3.201177],[-7.286547],[-1.316276],[-3.065084],[-3.232013],[-4.716046],[5.234793],[1.409906],[3.871026],[8.723755],[-5.337576],[-3.928540],[6.776343],[1.445726],[-5.736301],[4.767275],[6.670302],[-7.000493],[6.140402],[-7.167102],[6.727468],[-5.571325],[-2.451032],[6.310816],[5.810720],[3.895170],[4.645872],[-3.046347],[1.691378],[-9.111804],[-6.487048],[-8.593078],[-5.585276],[6.011212],[7.326235],[4.033987],[-0.721665],[9.977083],[9.824623],[4.478579],[5.872874],[5.384440],[-3.789512],[8.374181],[6.431925],[-9.969783],[-0.692068],[3.898244],[3.084226],[-6.669821],[-1.871971],[8.080128],[5.219758],[2.966398],[0.013276],[-1.283545],[6.219978]], dtype = "float32")#candidate|4144|(180, 1)|const|float32
call_4141 = relay.TupleGetItem(func_449_call(relay.reshape(var_4142.astype('int8'), []), relay.reshape(const_4143.astype('int8'), [7, 8, 12]), relay.reshape(const_4144.astype('float32'), [180,]), ), 2)
call_4145 = relay.TupleGetItem(func_453_call(relay.reshape(var_4142.astype('int8'), []), relay.reshape(const_4143.astype('int8'), [7, 8, 12]), relay.reshape(const_4144.astype('float32'), [180,]), ), 2)
func_151_call = mod.get_global_var('func_151')
func_154_call = mutated_mod.get_global_var('func_154')
var_4149 = relay.var("var_4149", dtype = "bool", shape = (896,))#candidate|4149|(896,)|var|bool
call_4148 = relay.TupleGetItem(func_151_call(relay.reshape(var_4149.astype('bool'), [16, 7, 8])), 0)
call_4150 = relay.TupleGetItem(func_154_call(relay.reshape(var_4149.astype('bool'), [16, 7, 8])), 0)
uop_4159 = relay.asinh(uop_4105.astype('float64')) # shape=(14, 3, 1)
func_4089_call = mod.get_global_var('func_4089')
func_4091_call = mutated_mod.get_global_var('func_4091')
call_4179 = func_4089_call()
call_4180 = func_4089_call()
uop_4192 = relay.asin(uop_4159.astype('float32')) # shape=(14, 3, 1)
uop_4194 = relay.sinh(uop_4159.astype('float32')) # shape=(14, 3, 1)
output = relay.Tuple([call_4114,call_4134,const_4135,call_4141,var_4142,const_4143,const_4144,call_4148,var_4149,call_4179,uop_4192,uop_4194,])
output2 = relay.Tuple([call_4115,call_4136,const_4135,call_4145,var_4142,const_4143,const_4144,call_4150,var_4149,call_4180,uop_4192,uop_4194,])
func_4201 = relay.Function([var_4104,var_4142,var_4149,], output)
mod['func_4201'] = func_4201
mod = relay.transform.InferType()(mod)
var_4202 = relay.var("var_4202", dtype = "float32", shape = (14, 3, 1))#candidate|4202|(14, 3, 1)|var|float32
var_4203 = relay.var("var_4203", dtype = "int8", shape = ())#candidate|4203|()|var|int8
var_4204 = relay.var("var_4204", dtype = "bool", shape = (896,))#candidate|4204|(896,)|var|bool
output = func_4201(var_4202,var_4203,var_4204,)
func_4205 = relay.Function([var_4202,var_4203,var_4204,], output)
mutated_mod['func_4205'] = func_4205
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3874_call = mod.get_global_var('func_3874')
func_3875_call = mutated_mod.get_global_var('func_3875')
call_4323 = func_3874_call()
call_4324 = func_3874_call()
func_3973_call = mod.get_global_var('func_3973')
func_3977_call = mutated_mod.get_global_var('func_3977')
call_4354 = func_3973_call(relay.reshape(call_4323.astype('float32'), [11, 14, 12]), relay.reshape(call_4323.astype('bool'), [11, 14, 12]), )
call_4355 = func_3973_call(relay.reshape(call_4323.astype('float32'), [11, 14, 12]), relay.reshape(call_4323.astype('bool'), [11, 14, 12]), )
uop_4361 = relay.asin(call_4323.astype('float32')) # shape=(11, 14, 12)
uop_4363 = relay.asin(call_4324.astype('float32')) # shape=(11, 14, 12)
func_690_call = mod.get_global_var('func_690')
func_695_call = mutated_mod.get_global_var('func_695')
var_4365 = relay.var("var_4365", dtype = "uint32", shape = (60,))#candidate|4365|(60,)|var|uint32
var_4366 = relay.var("var_4366", dtype = "float32", shape = (180,))#candidate|4366|(180,)|var|float32
const_4367 = relay.const([True,True,False,True,True,False,False,False,True,True,False,True,False,False,False,False,True,False,True,False,True,True,False,False,True,False,True,True,False,True,False,True,False,False,False,True,False,False,False,True,True,False,False,True,True,True,False,False,True,True,False,False,False,True,False,False,True,True,True,True,True,True,False,True,True,False,True,True,False,True,True,True,True,True,False,False,False,False,True,False,False,True,False,False,False,True,False,True,False,True,False,True,False,False,True,True,False,False,True,False,True,False,True,False,True,False,True,False,False,False,False,False,True,False,True,False,True,True,True,False,True,False,True,True,False,False,True,True,False,False,True,True,False,True,False,True,True,True,True,True,True,True,False,False,False,True,False,True,False,False,True,True,False,True,True,False,True,False,True,False,False,True,True,False,False,True,True,True,False,True,False,True,False,False,False,False,True,False,False,False,False,True,True,False,False,False,True,False,False,False,False,False,True,True,False,True,True,False,False,True,True,True,True,True,True,True,False,True,True,False,True,False,True,False,False,False,True,True,False,True,False,False,False,True,True,False,True,False,False,True,False,True,False,True,True,False,False,True,True,True,True,False,True,False,False,False,False,True,True,False,True,True,False,True,True,False,True,False,False,False,True,False,True,False,True,False,False,True,True,True,True,False,True,False,True,True,False,True,True,False,False,False,True,False,True,False,False,False,False,True,False,False,True,False,False,True,False,False,False,False,True,True,False,False,False,True,True,False,True,False,False,True,False,False,True,True,False,False,False,True,True,False,True,False,False,True,True,True,True,False,True,False,True,True,False,True,True,True,False,False,False,False,True,False,False,False,False,True,False,False,False,True,False,True,False,True,False,True,False,True,True,True,True,True,False,True,False,True,False,False,True,False,True,False,True,True,True,True,False,True,True,False,True,True,True,True,False,True,False,False,False,False,True,True,True,False,False,True,True,True,False,True,True,True,True,False,False,False,True,True,False,False,True,True,False,True,False,False,False,False,True,True,False,False,False,True,False,True,True,False,False,True,True,True,False,False,False,False,True,True,True,True,False,True,False,False,False,False,False,False,False,True,True,True,False,False,False,False,True,True,False,True,False,True,False,False,False,False,True,True,False,False,False,False,True,False,False,True,False,False,False,False,False,True,True,False,True,False,False,False,True,True,True,False,False,False,False,False,False,True,True,False,False,True,False,True,True,False,True,True,True,True,False,True,False,True,True,False,True,True,False,True,False,False,True,True,False,True,True,False,True,True,True,True,False,True,False,False,False,True,True,True,False,True,False,True,True,True,True,False,False,True,True,True,True,False,False,True,False,True,False,True,False,True,False,True,False,False,True,False,False,False,True,False,False,True,True,True,False,False,True,True,False,True,False,True,True,False,True,True,True,True,False,False,False,False,True,False,True,False,True,True,False,False,True,False,False,True,True,False,True,True,True,True,False,True,True,True,True,False,True,True,True,True,True,True,False,False,True,True,False,False,False,False,True,True,True,True,False,False,True,False,True,True,True,True,False,False,True,False,False,False,True,True,True,False,False,True,False,False,False,False,False,False,False,True,False,True,False,False,False,False,False,True,True,False,True,True,False,False,True,True,False,False,False,True,False,True,True,False,True,True,False,True,False,True,True,False,False,True,False,False,True,True,False,False,True,True,False,True,True,True,False,True,False,True,False,False,False,True,True,True,True,True,False,True,False,True,True,True,True,True,True,False,False,True,True,True,False,True,True,True,False,True,False,False,False,True,True,False,False,False,True,True,True,False,False,False,True,True,True,False,True,False,True,True,False,False,True,False,True,False,False,True,True,False,False,False,True,True,False,False,True,False,True,False,False,False,False,True,True,True,False,False,False,True,False,False,True,True,False,False,True,False,True,False,True,True,False,False,False,True,False,True,True,False,False,True,False,False,False,True,False,False,False,False,True,False,False,False,True,False,False,False,True,False,False,False,True,True,False,False,False,True,True,True,True,True,False,True,False,False,False,False,True,False,False,False,False,False,True,True,False,True,True,True,True,False,True,True,True,False,True,True,True,False,False,False,False,False,True,False,False,True,False,True,False,False,False,False,False,True,False,False,False,True], dtype = "bool")#candidate|4367|(896,)|const|bool
const_4368 = relay.const([-10,4,8,2,-7,1,-2,7,6,-6,-3,8,-3,-8,-8,4,1,10,5,9,-7,-8,-7,-2,-1,7,1,-6,8,7,-10,-6,10,-2,5,8,2,-1,-3,4,-1,-7,-6,-7,4,10,8,9,-1,-2,2,8,-6,-5,-2,-10,-9,7,10,10,1,-2,-6,-4,1,3,6,7,2,10,10,1,8,7,-4,-6,6,2,6,-9,4,10,7,1,-1,5,2,3,4,10,6,4,1,-6,-4,3,10,7,1,7,8,3,8,9,-7,-1,-4,-7,-1,-1,-1,-4,-8,-6,-8,10,5,-7,1,-6,-7,-3,1,6,-4,-8,5,-6,2,1,7,7,7,4,10,-8,6,-7,-1,9,-4,-2,9,-2,-2,-9,6,-10,10,3,-3,-6,-2,5,10,9,-1,2,9,-8,-9,-9,-5,-8,-4,-6,3,5,6,7,2,-1,8,-2,9,9,1,3,-10,2,3,10,-9,-1,3,-3,5,9,-7,-4,2,-6,-3,10,1,7,7,2,-10,-1,1,9,5,-3,10,-1,-1,7,6,-9,-7,-3,-4,10,-5,1,4,6,-10,4,-6,-6,3,-5,3,6,-2,6,-3,2,-9,6,2,3,-2,-4,3,7,5,7,-6,8,3,6,10,3,-10,3,2,-4,4,-5,9,-4,-4,10,3,9,-4,1,-2,3,5,4,1,-4,-7,3,8,8,-6,3,-8,7,-9,6,-5,3,-7,9,-6,-5,9,9,-3,1,-7,3,1,9,-8,-3,-6,-5,5,2,-5,4,-5,3,-2,-9,1,8,2,3,-4,5,3,4,-1,9,3,4,-8,8,-3,1,-9,-7,-6,-10,-5,10,-2,3,-3,3,-8,6,4,-6,-8,-1,5,7,6,-2,10,-8,8,-10,-6,7,-10,9,-6,10,-3,-3,9,-2,7,8,7,2,9,-8,-6,10,7,-1,8,9,2,-2,1,-6,7,6,1,-1,3,-7,4,7,9,-6,-9,8,8,2,3,8,3,-8,-3,7,8,-4,-3,6,9,1,-1,-9,9,8,1,-4,9,1,10,-7,5,-3,-2,-2,-4,-1,10,-2,1,-2,6,-7,9,9,7,8,-7,10,-1,-2,-5,-8,3,7,1,-8,-7,-4,-6,-4,6,5,-4,-5,-1,-7,-2,-3,-8,10,-10,-6,7,1,-2,-6,-10,4,-8,-8,7,-5,-2,-5,9,-10,6,-5,-8,6,-5,10,3,-9,6,2,-3,-4,5,7,-5,-4,7,-5,8,-6,-6,-8,2,-2,5,2,10,6,5,9,2,-2,3,-3,3,-3,8,7,-1,8,2,-5,-8,-6,-2,-3,-10,-3,-6,-3,-8,7,-10,-5,3,6,-5,-6,9,4,-8,-8,-5,1,-9,-10,3,-2,4,-1,-1,2,7,7,-3,9,-9,2,-10,-7,7,8,7,-2,-7,9,1,2,-1,-2,-1,8,8,5,-4,6,10,-1,4,-7,6,7,-7,-5,-9,5,-10,1,4,5,-6,9,-7,-2,-6,1,5,1,-8,-2,-5,-8,-3,-2,-5,-7,10,-9,-8,9,10,-8,-10,6,-5,-7,-9,-5,6,-9,6,3,2,4,-1,-6,5,-7,-2,2,-3,-10,-8,5,4,-4,-10,8,-9,3,-7,2,-2,-4,-1,-4,7,-9,10,-10,7,-3,-1,10,3,-1,-2,-2,-1,9,-5,8,-8,9,-10,10,-3,4,-6,-5,8,1,8,-2,-10,-2,-7,-8,-9,3,-6,-7,-8,6,-5,-2,8,1,-7,-6,8,-1,-10,10,-8,7,3,-6,4,6,-4,2,-2,-9,-10,7,4,-2,8,2,-2,1,-4,8,-8,9,3,-1,6,7,6,-3,1,-3,-7,7,5,-7,-5,-6,1,3,7,-10,-6,1,10,-10,-1,-2,-9,10,-6,-2,-3,-4,-4,-8,-2,7,7,10,4,-10,5,3,-2,-10,9,-9,-2,5,-9,8,3,-9,-3,-10,1,2,-4,3,-8,-4,7,-9,6,5,-9,7,10,2,7,2,2,7,1,-1,3,5,-9,-6,-8,-2,-6,9,-7,1,3,-3,9,2,-9,8,10,-1,8,4,10,5,5,4,-6,-7,10,7,-1,7,4,2,-1,-3,-10,-6,-4,-6,8,-2,-7,-5,-10,-4,1,-1,-9,9,7,10,10,8,9,-3,-6,-3,-4,7,1,5,7,7,10,-7,-9,-4,2,-2,-8,2,-2,8,-1,9,10,-4,-1,-4,-8,-10,9,7,-8,6,8,3,-1,5,5,6,10,-2,-2,6,1,-8,-1,-2,7,-6,-6,-2,-9,-2,1,-2,9,-3,-2,2,4,4,8,4,-5,-8,-1,-9,7,9,-9,-10,6,-1,4,-4,5,4,3,9,-10,1,7,-6,-1,-4,-5,-1,10,1,-7,-4,10,-8,-8,3,1,-1,-3,-3,-3,7,1,-1,9,-7,-7,-1,-9,-4,-3,4,10,-2,-6,9,4,-7,3,-8,-2,-1,5,7,-10,-10,-7,-6,-4,2,-5,-9,-7,4,6,4,-6,-8,8,5,-6,2,-3,-2,9,5,7,5,-10,-5,2,6,-8,-10,-2,6,-2,-3,7,10,-1,1,10,-3,-4,9,-8,5,1,-2,-10,3,5,7,-3,-7,3,-4,4,5,6,8,-3,9,6,-9,2,-8,-9,-10,-1,1,-6,7,4,2,8,-3,-10,-6,-6,3,-6,4,4,-10,-10,9,5,8,9,-7,-7,-9,5,-3,8,-10,5,-2,7,-3,10,-4,7,-2,9,5,-4,-3,8,1,-10,-2,6,-5,5,-1,-10,-10,7,3,-3,-4,-3,-7,10,8,-8,6,-4,8,-9,-4,6,-3,-6,-10,7,8,-10,-8,3,-2,-6,-7,-1,2,4,6,10,2,8,-6,8,2,1,8,-7,6,-3,8,8,4,5,-1,-9,-10,-4,1,-2,-10,6,6,-2,-9,-5,-9,-8,-4,-10,6,7,8,4,-5,-4,-1,3,-6,-10,-10,-3,-10,9,-1,-9,10,-7,-9,-10,7,-9,6,6,9,-6,-2,5,9,-8,-4,-1,4,5,-9,10,-8,-6,3,4,-9,10,-1,-5,-10,5,1,10,-4,-1,-9,10,-1,2,10,5,-10,3,9,-4,-3,3,-4,9,8,-10,-2,4,7,-7,-6,6,-7,-7,-7,3,7,3,-9,-9,4,-5,10,-10,-7,-5,9,-7,2,-1,5,10,2,-3,-8,9,2,8,3,-10,-5,3,8,-2,-4,-1,9,-10,7,-3,6,4,-5,-1,-10,-1,7,1,-2,8,-6,-4,2,-7,5,-1,1,10,-10,6,-3,-7,9,-8,2,8,6,-4,-3,-7,-10,-3,6,7,-6,7,10,-2,3,3,-5,-7,2,-9,-4,-7,-7,-5,4,8,-7,-9,-9,9,10,-9,-2,8,-8,2,5,6,8,4,5,3,-5,2,-5,7,-4,2,3,-1,1,4,-1,-8,4,-2,-4,-3,-9,-2,-8,2,5,8,-8,-8,-2,-4,3,-5,-4,7,4,-6,7,-9,-8,6,7,-1,5,-3,-4,-4,-9,-5,6,10,2,-4,5,-5,-6,-8,9,7,1,-2,9,1,5,-2,5,-2,9,9,9,8,-7,8,6,-9,-7,1,9,3,-5,4,6,-1,1,-8,-4,-8,3,-8,-3,-7,9,8,7,1,-6,-3,2,7,6,6,4,-2,9,-7,6,-3,-9,3,2,-9,9,-1,10,4,5,-5,-3,-7,6,5,7,6,-8,-3,3,9,8,4,-9,-1,10,5,-4,6,-8,1,-8,3,-6,-6,-10,10,6,5,2,-4,-3,-8,3,6,-4,5,4,7,6,-8,10,-6,3,4,9,-10,4,9,1,-9,2,4,-1,7,-4,-4,6,1,-1,-5,-10,3,2,-3,7,7,-5,-9,-1,6,3,2,-1,-9,7,-5,10,4,9,-6,-9,-10,-3,5,-5,-1,-2,-10,-7,9,2,2,-1,-5,-2,-1,-1,9,9,-7,-4,5,-1,-1,5,-2,-4,-10,-9,-9,3,5,-10,7,6,-4,-2,8,-7,4,9,-8,10,-9,-2,-3,-8,-8,-1,-8,8,-9,2,-6,6,-10,7,1,-7,-10,1,-3,-10,-7,-7,-1,-8,5,-10,10,4,3,9,1,-6,-6,-2,4,-1,6,8], dtype = "int8")#candidate|4368|(1568,)|const|int8
call_4364 = relay.TupleGetItem(func_690_call(relay.reshape(var_4365.astype('uint32'), [2, 2, 15]), relay.reshape(var_4366.astype('float32'), [180,]), relay.reshape(const_4367.astype('bool'), [896,]), relay.reshape(const_4368.astype('int8'), [1568,]), ), 2)
call_4369 = relay.TupleGetItem(func_695_call(relay.reshape(var_4365.astype('uint32'), [2, 2, 15]), relay.reshape(var_4366.astype('float32'), [180,]), relay.reshape(const_4367.astype('bool'), [896,]), relay.reshape(const_4368.astype('int8'), [1568,]), ), 2)
func_3230_call = mod.get_global_var('func_3230')
func_3234_call = mutated_mod.get_global_var('func_3234')
const_4383 = relay.const([-0.659625,-4.701001,-7.776357,-0.555442,-1.410082,9.193751,8.824684,1.440941,6.794535,-0.852497,-7.921470,5.171243,-3.995095,-7.837138,-7.389178,-7.245605,2.002430,3.266382,1.863387,-9.897557,2.651497,9.549895,-1.699055,3.794261,-3.989674,2.813822,9.185725,7.715857,8.801798,8.686800,8.328415,-1.479271,-0.568083,-2.195232,-4.445997,7.736495,-9.806928,-5.765892,-4.273448,-3.201183,5.312981,2.358145,-7.342311,2.094321,4.956454,-4.486753,-4.003529,5.846018,-5.460548,3.461746,-7.382312,-3.155365,2.232833,-7.214927,-8.096002,-1.677105,-3.685591,-6.277723,-4.055920,-5.998642,-3.677738,-5.486242,4.544659,-4.564949,6.529511,-7.478116,-5.118569,6.566966,9.838817,8.949936,-9.092505,-4.585233,-6.387225,-2.430518,-5.822642,-3.328332,6.964875,8.451575,-8.927786,-5.397241,7.838811,8.715895,1.147195,2.092034,-0.482965,-4.891719,-1.113932,0.249688,6.092753,1.132738,-0.149065,-3.479085,-6.706255,1.252681,4.444712,5.826287,-0.483115,4.013336,5.356660,7.395207,2.055090,-3.860135,-1.104592,-2.127013,2.444600,9.343947,8.012477,5.767385,2.223814,-9.586057,-7.083720,-5.537103,4.620095,-9.515915,-9.815851,-4.173755,8.951476,-8.584679,2.657571,5.897444,-9.184124,-4.857765,3.993861,-8.752719,-7.827117,4.166629,-8.414720,-9.285384,1.551312,-7.795272,-9.466425,-5.119747,2.678262,2.857733,3.878251,-7.565009,7.358907,-2.674885,-5.945836,8.141691,7.862055,-0.131630,-8.972935,6.982278,5.650412,-8.246557,3.034642,-1.595831,3.369118,8.634443,-8.178161,-7.376959,-6.460053,-7.674374,6.240914,-3.710460,9.696394,-7.835666,6.708603,8.516175,7.973737,-8.304179,-8.444661,-7.002853,-9.377112,5.843200,3.565960,-8.742398,-6.050532,-8.994632,-0.097895,-6.410544,6.308896,-8.649247,6.929867,-5.044522,3.758292,0.072074,9.127660,4.073945,3.916977,-3.137110,-5.501648,-2.506765,-3.717491,2.094571,0.334068,-3.320032,-3.663363,1.487051,-9.943147,4.117012,-9.867520,-9.699345,-4.210919,9.411767,-5.760336,-4.990911,-9.534167,1.035458,8.120362,-5.224351,-0.182418,-1.904642,5.613503,-5.392688,3.106702,1.047332,-5.222381,8.617348,0.170447,-1.566656,-7.493546,-8.922635,-2.105070,4.552357,-9.831951,-2.850211,-2.154969,-6.803897,7.746915,-6.872529,-6.915651,-2.781424,3.545903,7.987548,0.255980,-3.544107,-1.059005,-2.926443,-2.867416,-0.515398,0.002993,9.428872,7.533815,4.864086,5.231657,4.418577,8.446241,-5.882593,8.752828,9.032208,-1.913297,0.284886,1.478013,5.939597,5.312427,-7.347759,-1.208277,3.956320,7.523377,-4.945795,-1.431960,-4.115239,-8.674448,-8.947719,-3.625348,-1.023072,7.520148,7.240957,6.687393,-5.533826,5.162656,-9.622128,-9.265383,3.887503,-6.455361,-7.168207,-1.352849,3.973610,-9.362448,-1.972493,3.928689,8.857822,-6.272763,9.815341,2.124989,2.494399,6.591714,-1.720660,4.435620,4.827021,-8.760394,-8.754726,0.179331,0.567252,1.716839,-4.837123,-9.845397,2.131041,7.946237,-8.095667,-6.560692,9.595881,1.008567,7.227280,1.912443,7.101246,9.210157,-0.275191,6.588912,-0.214960,-0.106686,4.078991,-8.534147,2.969270,-1.495815,-8.746533,6.604319,-2.392526,1.388869,5.077039,-7.322688,-8.633601,-1.535849,-0.820421,-7.693813,-9.235513,-7.570217,5.859543,-0.051356,-0.722987,0.139142,1.606784,-4.353846,5.843447,-9.759817,-3.879223,3.993115,-3.561007,-6.476285,7.000035,7.553406,4.846604,-9.478623,-0.232788,6.044235,1.921335,2.554209,-7.091692,-4.115217,1.533454,-2.140782,2.805176,7.155528,-4.157876,8.902788,-7.535233,7.485867,-8.794225,2.317589,5.384577,3.485374,4.240261,5.650050,-6.561457,8.041798,-3.788268,3.842140,-8.802712,9.075900,-3.281284,-0.840902,5.997331,-3.250375,7.699388,-5.704262,7.536657,7.924221,-5.791545,-4.968267,-4.933399,5.032510,3.005360,9.725546,6.374345,-6.297449,8.790843,-7.895908,7.002732,-9.195827,-5.842880,9.629777,-8.008594,-0.051393,9.531860,4.870978,8.938325,0.139393,7.124920,-1.113616,8.443385,9.359061,8.682395,-3.621646,-1.907608,-3.188531,2.463473,-3.125855,-0.929218,9.394618,3.718746,-1.262532,2.455500,-0.829969,-6.219549,0.322015,3.070029,-1.673842,-6.368174,5.070192,3.472154,-0.760275,7.205752,-3.869522,4.892765,-3.183622,-9.241871,6.986139,-3.468244,-9.823629,-5.086260,-5.201385,-7.468631,6.704315,2.274542,-7.623559,-9.230059,-8.665630,2.601595,4.144294,-0.393939,-0.056946,-6.779760,-5.439896,0.126427,8.512650,-2.132628,7.836144,-3.852334,7.448156,-3.563840,-2.130193,-5.042135,-8.772761,2.561111,3.201108,5.432365,-7.490405,7.282692,-3.797255,-2.162712,6.240314,-4.193399,3.648468,4.159009,-3.362996,-7.029200,-4.266518,3.506811,2.717342,-0.124400,-0.960054,-7.502939,-0.619662,9.361972,-8.845815,-0.896006,-0.763743,-1.299903,-2.975800,5.849159,8.459568,2.716161,-6.740948,2.474914,-0.724589,-3.863024,8.247504,4.943102], dtype = "float64")#candidate|4383|(480,)|const|float64
const_4384 = relay.const([8,10,5,-10,-6,3,-9,-6,6,4,-9,7,-2,8,-3,-3,-4,-10,-8,9,-1,-4,1,-5,-7,-10,4,6,2,-1,7,-8,6,-2,-8,10,3,-10,-3,-1,2,5,-1,-1,-4,-8,6,-2,3,7,-4,1,-1,2,-3,-4,-6,-2,1,2,6,6,5,4,-1,9,10,-3,-8,6,-9,8,-1,-4,4,8,7,9,2,-2,-4,8,-1,-6,-7,-2,-3,4,1,-6,6,-4,-10,7,-8,-6,-9,8,-7,-1,-9,1,-3,7,4,2,9,-3,1,-2,-8,-5,3,7,10,-4,-10,10,-3,9,2,7,7,2,-9,-1,1,4,-9,-3,8,7,-6,1,-6,5,4,-1,2,-1,8,-10,7,-2,-4,7,-4,-1,-5,-10,-5,-1,10,9,5,-5,-3,-1,-8,9,10,7,2,6,10,-8,-4,-3,-1,6,-4,1,5,-10,-5,-8,-6,-10,-3,-6,4,-8,-3,1,-3,3,10,-7,-6,-2,9,-7,-5,3,-3,2,1,4,-1,9,3,-1,6,8,8,-4,-9,10,-5,-3,10,-6,5,6,-4,-10,-6,10,3,-3,-7,8,7,-2,-2,3,-2,4,8,3,-6,-10,6,-6,9,9,-6,2,6,-8,-10,-10,-7,-10,-6,-8,10,7,-8,-4,-2,-3,-2,4,10,4,-10,-4,9,-3,-9,-9,8,4,9,-3,4,1,-2,4,4,3,4,-4,-1,2,-9,10,7,3,5,6,3,-5,-2,-8,9,-2,-9,10,5,-10,10,-2,-6,-2,-3,8,10,1,-4,-10,-10,-10,9,9,-9,-8,10,6,5,7,-10,3,10,-10,5,-9,-2,-6,-6,-9,-5,-4,7,1,9,1,2,-9,-10,-9,1,-1,-7,-6,-9,10,1,9,5,1,7,-5,-8,1,5,2,-8,-9,-8,-9,-9,3,4,-2,-3,7,7,-8,8,10,9,-7,4,3,-2,-1,1,3,-7,6,-9,9,-5,-8,6,6,1,4,1,9,8,-6,-7,6,-5,-5,3,8,-1,-3,-6,4,-4,7,6,1,-8,-4,-6,-1,3,5,2,-6,-2,1,9,7,6,1,2,5,-8,6,-1,7,5,-2,7,-1,8,-7,9,-10,-10,6,-2,-1,-2,-6,-6,-7,-9,9,6,3,1,-10,-5,-3,1,6,-10,4,6,5,7,4,-2,1,2,-3,-5,-1,-3,-5,6,6,8,8,-3,5,-8,7,-3,-1,4,8,-6,10,-5,-4,6,-7,-3,8,1,-8,-4,10,-3,2,4,7,-9,1,-3,5,8,-8,10,-7,-1,1,-9,-5,-3,-10,-7,8,5,1,8,-1,-1,-5,5,1,8,3,2,-10,7,3,10,-1,5,-4,2,-7,-6,-2,-6,-9,5,-2,2,-4,-3,-4,-10,-7,-10,6,-10,-3,-9,5,9,10,8,5,-5,10,7,10,-2,2,1,4,-5,6,-5,9,-7,-10,-10,-6,5,4,1,-3,2,4,5,5,-4,-4,-3,3,-2,6,9,9,-5,9,-7,-8,-8,-4,-10,-5,-3,-3,3,-8,-2,-7,6,8,6,-9,10,4,10,2,-1,4,9,-2,-5,5,7,-10,-7,4,6,8,3,-3,-2,-10,-6,-8,-4,-5,-1,6,-4,8,-5,-5,-10,-4,-7,-3,-5,-5,-9,-6,-1,2,3,9,6,-9,2,1,-8,-2,-5,-7,9,-1,-3,9,-2,-8,-1,-4,-4,8,-6,-9,-6,-1,-7,-1,-8,-5,3,-7,-7,10,3,4,7,-5,-3,-7,-7,-9,-7,-1,3,10,-9,1,-3,1,4,-3,-9,6,-5,8,3,4,-8,-7,-10,6,-3,3,-9,3,-10,-6,7,1,-5,3,8,8,-4,-6,-1,2,-1,-3,1,-6,2,-2,-2,-2,1,4,7,-7,8,-7,-8,-6,-6,-9,-5,-8,7,-10,2,-7,-9,4,7,-9,5,-6,5,-3,-3,9,-9,4,6,4,-8,-3,-6,-5,10,-7,-1,9,-7,8,5,5,-4,-10,5,-10,-7,-1,4,5,1,-1,5,10,-2,-9,6,3,-4,-2,-6,-3,-9,-5,10,7,10,-4,9,6,-2,8,-8,10,3,3,6,2,8,-6,-7,-10,2,3,-7,3,-3,-7,-4,-5,9,-6,-3,8,-6,-2,9,4,-5,3,6,-1,-6,2,-3,7,-4,-7,-1,-10,9,-2,3,10,-2,10,-10,1,-9,-8,-1,-6,-5,-3,8,-5,-3], dtype = "int64")#candidate|4384|(845,)|const|int64
call_4382 = relay.TupleGetItem(func_3230_call(relay.reshape(const_4383.astype('float64'), [15, 2, 16]), relay.reshape(const_4384.astype('int64'), [845,]), relay.reshape(var_4366.astype('float32'), [180,]), ), 4)
call_4385 = relay.TupleGetItem(func_3234_call(relay.reshape(const_4383.astype('float64'), [15, 2, 16]), relay.reshape(const_4384.astype('int64'), [845,]), relay.reshape(var_4366.astype('float32'), [180,]), ), 4)
func_3460_call = mod.get_global_var('func_3460')
func_3464_call = mutated_mod.get_global_var('func_3464')
const_4393 = relay.const([-10,-2,6,-10,-10,-10,10,2,2,5,4,-8,3,8,4,-4,10,9,-1,9,-9,-8,10,-10,-1,8,1,6,-4,1,-6,4,-1,4,-4,-5,-5,4,3,8,1,9,2,7,2,3,2,-7,-10,9,5,-9,-7,6,6,-3,-1,-8,-10,8,2,-1,9,-9,9,3,10,-4,4,6,-5,-5,-1,-9,6,2,-7,2,1,4,-9,-3,8,7,-9,-2,-2,-1,9,-4,7,5,-1,9,8,9,10,-8,1,-2,10,5,2,5,-7,-6,-6,-6,8,8,-1,-5,1,1,1,-4,-1,3,6,3], dtype = "uint16")#candidate|4393|(120,)|const|uint16
call_4392 = relay.TupleGetItem(func_3460_call(relay.reshape(const_4393.astype('uint16'), [5, 4, 6]), relay.reshape(const_4393.astype('uint16'), [5, 4, 6]), ), 1)
call_4394 = relay.TupleGetItem(func_3464_call(relay.reshape(const_4393.astype('uint16'), [5, 4, 6]), relay.reshape(const_4393.astype('uint16'), [5, 4, 6]), ), 1)
output = relay.Tuple([call_4354,uop_4361,call_4364,var_4365,var_4366,const_4367,const_4368,call_4382,const_4383,const_4384,call_4392,const_4393,])
output2 = relay.Tuple([call_4355,uop_4363,call_4369,var_4365,var_4366,const_4367,const_4368,call_4385,const_4383,const_4384,call_4394,const_4393,])
func_4398 = relay.Function([var_4365,var_4366,], output)
mod['func_4398'] = func_4398
mod = relay.transform.InferType()(mod)
var_4399 = relay.var("var_4399", dtype = "uint32", shape = (60,))#candidate|4399|(60,)|var|uint32
var_4400 = relay.var("var_4400", dtype = "float32", shape = (180,))#candidate|4400|(180,)|var|float32
output = func_4398(var_4399,var_4400,)
func_4401 = relay.Function([var_4399,var_4400,], output)
mutated_mod['func_4401'] = func_4401
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4089_call = mod.get_global_var('func_4089')
func_4091_call = mutated_mod.get_global_var('func_4091')
call_4405 = func_4089_call()
call_4406 = func_4089_call()
uop_4412 = relay.tan(call_4405.astype('float64')) # shape=(11, 14, 12)
uop_4414 = relay.tan(call_4406.astype('float64')) # shape=(11, 14, 12)
func_534_call = mod.get_global_var('func_534')
func_537_call = mutated_mod.get_global_var('func_537')
var_4422 = relay.var("var_4422", dtype = "int8", shape = (1568,))#candidate|4422|(1568,)|var|int8
call_4421 = relay.TupleGetItem(func_534_call(relay.reshape(var_4422.astype('int8'), [16, 7, 14])), 1)
call_4423 = relay.TupleGetItem(func_537_call(relay.reshape(var_4422.astype('int8'), [16, 7, 14])), 1)
func_534_call = mod.get_global_var('func_534')
func_537_call = mutated_mod.get_global_var('func_537')
call_4433 = relay.TupleGetItem(func_534_call(relay.reshape(var_4422.astype('int8'), [16, 7, 14])), 2)
call_4434 = relay.TupleGetItem(func_537_call(relay.reshape(var_4422.astype('int8'), [16, 7, 14])), 2)
func_4017_call = mod.get_global_var('func_4017')
func_4018_call = mutated_mod.get_global_var('func_4018')
call_4438 = relay.TupleGetItem(func_4017_call(), 0)
call_4439 = relay.TupleGetItem(func_4018_call(), 0)
uop_4449 = relay.sigmoid(call_4421.astype('float32')) # shape=(9, 15, 1)
uop_4451 = relay.sigmoid(call_4423.astype('float32')) # shape=(9, 15, 1)
func_4201_call = mod.get_global_var('func_4201')
func_4205_call = mutated_mod.get_global_var('func_4205')
const_4454 = relay.const([7.115401,6.146870,1.790917,9.041999,-7.786721,-0.430685,5.365412,5.837525,0.206571,2.717865,-4.621187,-9.025942,1.665084,-6.903298,0.581193,8.388302,-0.643814,-2.203655,-2.572992,6.941776,-4.291399,2.995866,-1.313151,-5.036698,1.671851,0.308822,7.257370,1.710676,-2.797715,-2.087281,5.148305,-1.725538,-3.624828,-5.440107,5.053534,-3.053159,6.104259,0.906317,-4.419146,8.170419,2.620630,6.788879], dtype = "float32")#candidate|4454|(42,)|const|float32
var_4455 = relay.var("var_4455", dtype = "int8", shape = ())#candidate|4455|()|var|int8
const_4456 = relay.const([True,False,True,False,True,True,True,False,False,False,False,True,False,False,False,True,False,False,True,True,False,False,True,False,True,True,True,False,False,True,True,True,False,False,True,True,True,False,True,False,False,True,True,True,True,True,False,False,True,True,True,True,True,True,False,True,False,True,True,True,False,False,False,False,True,False,False,False,False,True,False,True,True,True,False,False,True,False,False,False,False,False,False,True,True,False,False,True,True,True,False,True,False,True,False,True,True,False,True,True,True,False,False,False,True,False,True,False,True,True,True,True,True,True,False,False,True,True,False,False,False,False,True,False,True,True,True,False,True,True,False,True,True,False,True,False,True,False,True,False,False,False,True,True,True,True,False,False,False,False,False,True,False,True,True,False,True,True,False,False,False,False,True,True,True,True,True,False,True,False,False,True,False,True,True,True,False,True,True,True,True,True,False,True,True,True,True,False,False,False,False,False,False,False,True,True,True,True,True,False,True,True,False,False,False,True,True,True,False,True,False,True,False,False,False,True,True,False,True,False,False,False,False,False,False,False,False,True,True,True,True,False,True,True,False,True,False,False,False,False,True,False,True,True,False,False,True,False,False,False,False,False,False,False,False,False,False,False,True,True,False,True,False,True,False,False,False,True,False,True,True,True,True,True,True,False,True,False,False,True,False,False,True,True,False,True,True,True,False,True,False,False,False,False,True,False,True,True,True,True,False,True,True,False,False,False,False,True,False,False,False,False,False,True,True,False,False,True,True,False,False,False,False,False,False,True,False,True,True,False,True,True,True,False,True,True,False,True,False,False,True,False,False,True,True,False,False,True,True,True,False,True,True,False,True,False,False,True,True,True,True,False,False,False,False,False,True,False,True,True,False,True,True,True,False,False,True,False,False,False,False,False,True,True,False,False,True,False,True,True,True,True,True,False,True,False,False,True,False,True,False,True,False,False,False,True,False,True,True,False,True,True,False,False,True,True,False,False,True,True,True,True,False,True,True,False,True,True,True,True,False,True,False,True,True,False,False,False,True,True,False,False,True,True,False,False,False,False,False,True,False,False,False,False,True,True,False,False,False,True,True,True,True,False,False,False,False,False,False,False,True,True,False,False,False,True,False,False,True,True,True,True,True,False,False,False,True,False,False,False,False,True,True,True,True,True,True,False,True,False,False,False,True,False,True,True,True,True,True,True,False,False,False,True,False,False,True,False,True,True,False,True,True,True,False,False,False,True,False,True,True,False,True,False,True,False,True,False,False,False,True,False,True,False,False,True,False,True,True,True,True,True,False,False,False,False,False,False,False,True,True,True,True,True,False,False,True,True,True,True,False,False,False,True,False,False,False,True,True,False,False,False,True,True,False,False,True,True,False,True,False,False,True,True,True,True,False,False,False,True,False,False,True,False,True,False,False,False,True,True,False,True,False,True,False,False,True,False,True,False,True,True,False,False,True,True,True,True,True,False,False,True,False,True,True,False,True,True,False,False,True,False,False,True,True,False,True,True,False,True,True,False,False,True,False,True,False,False,False,True,False,False,True,False,False,False,False,True,False,False,False,True,False,False,False,False,False,True,True,True,False,False,True,True,True,True,False,True,True,True,False,True,True,True,False,True,False,False,True,False,True,True,True,True,True,True,True,True,False,False,False,True,False,True,False,True,True,False,False,False,True,True,False,True,False,False,False,False,False,True,False,True,False,True,True,True,False,False,True,True,True,True,False,True,True,False,True,False,False,True,False,False,False,False,True,True,False,True,True,True,True,False,False,True,True,True,True,False,False,False,True,True,True,True,False,False,True,True,False,True,True,True,True,True,True,False,False,False,False,False,True,True,False,True,False,True,True,True,True,True,True,False,False,True,True,False,True,False,False,False,False,True,True,True,False,False,False,True,False,False,True,True,True,True,True,True,False,False,True,False,True,False,False,True,True,False,True,True,False,True,True,False,False,False,False,True,False,False,False,True,False,True,False,True,False,True,False,False,True,True,False,False,False,True,True,True,True,True,False,True,False,True,False,True,True,False,False,False,False,False,True,False,True,True,True,True,True,True,True,False,True,False,True,True,True,False], dtype = "bool")#candidate|4456|(896,)|const|bool
call_4453 = relay.TupleGetItem(func_4201_call(relay.reshape(const_4454.astype('float32'), [14, 3, 1]), relay.reshape(var_4455.astype('int8'), []), relay.reshape(const_4456.astype('bool'), [896,]), ), 7)
call_4457 = relay.TupleGetItem(func_4205_call(relay.reshape(const_4454.astype('float32'), [14, 3, 1]), relay.reshape(var_4455.astype('int8'), []), relay.reshape(const_4456.astype('bool'), [896,]), ), 7)
output = relay.Tuple([uop_4412,var_4422,call_4433,call_4438,uop_4449,call_4453,const_4454,var_4455,const_4456,])
output2 = relay.Tuple([uop_4414,var_4422,call_4434,call_4439,uop_4451,call_4457,const_4454,var_4455,const_4456,])
func_4459 = relay.Function([var_4422,var_4455,], output)
mod['func_4459'] = func_4459
mod = relay.transform.InferType()(mod)
mutated_mod['func_4459'] = func_4459
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4459_call = mutated_mod.get_global_var('func_4459')
var_4461 = relay.var("var_4461", dtype = "int8", shape = (1568,))#candidate|4461|(1568,)|var|int8
var_4462 = relay.var("var_4462", dtype = "int8", shape = ())#candidate|4462|()|var|int8
call_4460 = func_4459_call(var_4461,var_4462,)
output = call_4460
func_4463 = relay.Function([var_4461,var_4462,], output)
mutated_mod['func_4463'] = func_4463
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3874_call = mod.get_global_var('func_3874')
func_3875_call = mutated_mod.get_global_var('func_3875')
call_4570 = func_3874_call()
call_4571 = func_3874_call()
func_449_call = mod.get_global_var('func_449')
func_453_call = mutated_mod.get_global_var('func_453')
const_4592 = relay.const(6, dtype = "int8")#candidate|4592|()|const|int8
const_4593 = relay.const([[-3,9],[7,9],[6,3],[7,5],[-2,8],[-5,5],[1,-10],[8,-10],[-2,-6],[-3,-8],[-8,8],[-6,-1],[-9,-6],[-5,8],[7,-10],[7,-5],[-9,10],[5,2],[9,-3],[2,-3],[-2,-5],[-2,-2],[-4,-3],[2,-2],[8,-2],[1,8],[-3,-5],[4,6],[-1,-4],[-6,3],[9,-3],[-3,-2],[6,-3],[10,-7],[4,-6],[3,8],[-4,6],[-9,2],[-4,-10],[9,-7],[-8,3],[4,10],[5,-6],[-9,10],[-7,3],[-5,7],[-1,4],[1,-6],[2,6],[1,-3],[4,-5],[-6,-6],[1,-10],[-8,4],[3,9],[1,-2],[5,8],[6,4],[-3,-4],[-2,-3],[-4,9],[-9,9],[-3,6],[4,-7],[-10,6],[-8,-7],[-9,-1],[3,-6],[-8,-7],[8,-1],[-6,2],[-6,8],[-4,1],[7,3],[9,9],[-10,9],[9,-5],[3,5],[4,7],[6,6],[-4,-10],[-7,8],[-8,9],[3,-6],[-3,-7],[-8,4],[-2,1],[-10,6],[6,-6],[-10,10],[-3,-8],[5,9],[6,4],[10,7],[3,-8],[5,-7],[-1,-5],[-7,-8],[1,7],[1,-6],[1,2],[-10,-3],[-5,5],[6,-4],[-3,7],[1,10],[-3,-10],[10,1],[5,-5],[2,-7],[-1,-8],[2,-6],[-8,-7],[-10,3],[-4,8],[-6,-7],[2,-8],[-10,-1],[5,9],[-3,6],[-10,2],[-10,3],[-5,-9],[-10,4],[8,6],[4,10],[9,1],[-6,3],[10,6],[-10,5],[8,8],[10,-1],[1,8],[-7,9],[10,7],[-6,2],[8,7],[6,5],[8,3],[-3,-8],[-2,-4],[-5,-4],[-2,10],[5,-6],[-9,3],[9,-1],[-9,-4],[-9,-1],[-9,1],[-7,-8],[7,-8],[10,-7],[9,6],[8,-2],[2,-3],[2,-1],[8,-6],[6,-3],[2,9],[-5,4],[-6,9],[-8,3],[1,-10],[-10,4],[2,3],[4,4],[5,-1],[-10,4],[5,-2],[-6,-4],[10,8],[4,8],[-1,-7],[6,4],[-7,-4],[10,-4],[1,2],[10,-4],[10,10],[3,-4],[-8,-3],[4,-8],[2,9],[9,-1],[-9,8],[6,10],[4,-2],[8,5],[-6,-10],[8,3],[-1,-4],[-8,-1],[-7,-6],[10,1],[-6,3],[6,9],[8,2],[9,-6],[8,1],[4,-2],[-10,5],[4,6],[-6,3],[-10,-4],[4,-4],[1,-3],[9,-6],[-5,-5],[-9,-7],[-4,-5],[3,-4],[10,1],[4,-7],[5,-8],[4,-7],[-4,-6],[-3,-6],[-5,9],[8,-2],[1,-2],[-1,2],[9,-10],[5,3],[-2,-10],[1,1],[-6,-5],[4,-5],[-3,10],[6,-9],[3,7],[7,-5],[9,3],[3,6],[-6,6],[-8,-5],[-5,-6],[8,-5],[5,8],[4,-2],[-9,4],[2,-1],[-1,-8],[-7,-2],[9,-3],[-3,7],[2,1],[-9,10],[-9,9],[-4,-10],[9,-4],[3,9],[5,-9],[10,-8],[9,10],[-2,7],[-3,-5],[-9,2],[6,-4],[-5,1],[5,-8],[-3,-9],[6,2],[10,-3],[8,-1],[-4,-4],[-10,-9],[9,5],[-9,-1],[9,-7],[-1,-5],[10,5],[-6,4],[-1,10],[7,6],[-7,-2],[-6,-9],[6,2],[-8,-10],[2,8],[-4,-8],[1,8],[-7,-5],[-7,-1],[1,8],[9,-7],[-4,5],[4,6],[8,-3],[-3,-8],[-5,-5],[10,-5],[-7,10],[-2,2],[6,4],[3,-10],[-5,1],[-5,-10],[-1,-5],[10,-4],[3,-4],[-5,-3],[-6,-2],[8,-9],[4,2],[-8,-2],[-7,10],[6,-6],[-9,6],[-9,-2],[-5,-3],[6,-7],[-3,-2],[1,-9],[-10,6],[2,7],[-4,-3],[3,5],[2,2],[-1,8],[5,-6],[3,-3],[-2,-1],[10,-4],[-2,-7],[-4,4],[2,4],[2,-1],[2,-3],[1,-10],[-6,-9],[-6,3],[2,4],[4,-10],[1,-4],[-5,-9],[-2,-4]], dtype = "int8")#candidate|4593|(336, 2)|const|int8
var_4594 = relay.var("var_4594", dtype = "float32", shape = (180,))#candidate|4594|(180,)|var|float32
call_4591 = relay.TupleGetItem(func_449_call(relay.reshape(const_4592.astype('int8'), []), relay.reshape(const_4593.astype('int8'), [7, 8, 12]), relay.reshape(var_4594.astype('float32'), [180,]), ), 0)
call_4595 = relay.TupleGetItem(func_453_call(relay.reshape(const_4592.astype('int8'), []), relay.reshape(const_4593.astype('int8'), [7, 8, 12]), relay.reshape(var_4594.astype('float32'), [180,]), ), 0)
uop_4597 = relay.asin(const_4593.astype('float64')) # shape=(336, 2)
output = relay.Tuple([call_4570,call_4591,const_4592,var_4594,uop_4597,])
output2 = relay.Tuple([call_4571,call_4595,const_4592,var_4594,uop_4597,])
func_4619 = relay.Function([var_4594,], output)
mod['func_4619'] = func_4619
mod = relay.transform.InferType()(mod)
mutated_mod['func_4619'] = func_4619
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4620 = relay.var("var_4620", dtype = "float32", shape = (180,))#candidate|4620|(180,)|var|float32
func_4619_call = mutated_mod.get_global_var('func_4619')
call_4621 = func_4619_call(var_4620)
output = call_4621
func_4622 = relay.Function([var_4620], output)
mutated_mod['func_4622'] = func_4622
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3874_call = mod.get_global_var('func_3874')
func_3875_call = mutated_mod.get_global_var('func_3875')
call_4662 = func_3874_call()
call_4663 = func_3874_call()
var_4675 = relay.var("var_4675", dtype = "float32", shape = (11, 14, 12))#candidate|4675|(11, 14, 12)|var|float32
bop_4676 = relay.floor_divide(call_4662.astype('float64'), relay.reshape(var_4675.astype('float64'), relay.shape_of(call_4662))) # shape=(11, 14, 12)
bop_4679 = relay.floor_divide(call_4663.astype('float64'), relay.reshape(var_4675.astype('float64'), relay.shape_of(call_4663))) # shape=(11, 14, 12)
func_3973_call = mod.get_global_var('func_3973')
func_3977_call = mutated_mod.get_global_var('func_3977')
call_4684 = func_3973_call(relay.reshape(call_4662.astype('float32'), [11, 14, 12]), relay.reshape(var_4675.astype('bool'), [11, 14, 12]), )
call_4685 = func_3973_call(relay.reshape(call_4662.astype('float32'), [11, 14, 12]), relay.reshape(var_4675.astype('bool'), [11, 14, 12]), )
func_4201_call = mod.get_global_var('func_4201')
func_4205_call = mutated_mod.get_global_var('func_4205')
const_4694 = relay.const([-9.757711,-7.755095,5.358147,7.432284,-3.598488,7.443778,7.535079,-4.900776,0.333192,8.390534,-1.693859,-6.493087,0.238956,-9.073304,4.517151,-3.953417,4.220585,-2.873618,4.511014,-1.559338,4.728848,-0.609116,-0.995968,-8.658474,1.453062,-8.711194,-2.855950,8.503214,6.929513,-4.712270,-1.730662,-8.108512,-1.237615,-2.690184,-5.151078,9.152304,-6.416445,-7.592674,-2.903597,2.500789,-4.897875,6.428042], dtype = "float32")#candidate|4694|(42,)|const|float32
var_4695 = relay.var("var_4695", dtype = "int8", shape = ())#candidate|4695|()|var|int8
const_4696 = relay.const([True,True,True,False,True,True,True,False,False,False,False,True,True,False,True,False,False,False,True,True,False,True,True,True,False,True,True,False,False,True,True,False,False,True,False,True,False,True,False,False,True,False,False,False,True,True,True,True,False,False,False,False,False,True,True,False,False,False,True,True,True,False,True,True,True,True,True,True,True,True,False,False,True,False,True,False,True,False,True,True,False,False,True,False,True,True,True,False,True,False,True,True,False,False,False,False,True,True,True,False,False,True,True,False,True,False,False,True,False,False,False,False,False,False,True,True,True,False,True,False,False,False,True,False,False,False,False,False,True,False,False,False,True,True,False,True,True,False,False,True,False,False,False,False,False,True,False,True,True,True,False,True,False,True,True,False,True,False,False,True,False,True,True,True,False,True,False,False,True,False,True,False,True,True,False,True,False,False,True,True,False,True,False,False,False,False,False,False,False,True,True,False,False,False,True,False,True,False,False,False,False,False,False,True,True,True,True,False,True,False,True,True,True,False,True,True,False,False,True,False,True,False,False,True,False,True,True,True,True,False,False,False,False,False,True,True,True,False,True,True,False,True,False,True,True,False,True,True,False,False,True,True,True,True,False,True,False,True,True,False,True,True,False,True,True,True,True,True,False,False,False,False,True,False,False,False,False,True,True,False,True,False,True,False,True,True,False,False,True,True,False,False,False,False,False,True,True,True,False,True,True,False,False,True,True,False,True,True,True,True,False,False,True,True,True,True,True,True,True,False,False,True,False,False,True,False,True,False,True,False,False,True,False,False,False,True,False,True,True,True,False,True,True,False,False,False,True,True,True,False,True,True,True,False,True,False,False,True,False,False,True,False,True,True,False,True,True,False,False,False,True,True,True,True,True,True,True,False,True,True,False,False,False,True,False,False,True,True,True,True,True,False,False,False,True,False,True,False,True,True,False,False,False,True,True,True,True,True,True,False,False,True,False,False,False,True,False,True,False,True,True,True,True,True,True,True,True,False,True,False,True,False,True,False,True,False,True,False,True,True,False,True,False,True,False,True,False,False,False,False,False,True,True,True,False,False,False,False,False,False,False,True,False,True,True,True,False,True,False,True,False,False,True,False,True,True,True,True,True,False,True,True,True,False,True,False,False,True,False,False,True,False,False,True,False,True,True,False,False,True,True,False,True,False,True,True,True,False,False,True,False,False,False,False,False,True,False,True,True,False,True,False,False,True,False,False,True,True,False,True,False,False,False,True,False,True,False,False,True,True,True,False,True,True,False,True,True,False,False,False,False,False,False,False,True,False,True,False,True,True,False,True,True,False,True,False,True,True,False,False,False,True,False,True,False,False,True,True,False,True,True,False,True,False,True,True,False,False,True,False,True,True,True,True,True,False,True,False,False,True,True,False,False,True,False,False,False,True,False,False,False,True,True,False,True,False,True,False,False,False,False,True,False,True,False,True,False,True,False,False,False,True,False,False,False,False,True,False,True,True,True,False,False,False,False,False,False,True,False,False,True,False,True,True,True,False,True,True,True,True,True,False,False,False,False,False,False,True,True,False,False,False,False,True,False,False,True,False,True,True,False,False,True,True,False,False,True,True,False,True,False,True,True,False,True,True,False,False,True,True,False,True,True,False,False,True,False,True,True,True,False,True,True,True,True,True,False,False,False,False,True,False,True,False,False,True,False,True,True,True,False,True,False,False,True,True,True,True,False,True,False,True,False,True,False,True,True,False,False,True,False,True,False,False,False,False,True,False,True,False,True,False,True,True,False,False,False,True,True,True,False,True,False,True,False,False,False,True,True,False,True,True,False,True,True,False,True,False,False,True,False,True,True,True,False,True,True,True,False,False,False,True,True,False,False,False,False,False,True,True,True,False,True,True,True,False,True,True,True,True,False,True,False,True,True,False,False,False,True,False,True,True,True,False,True,True,False,False,False,False,True,True,False,False,False,False,True,True,True,False,False,True,True,False,False,False,False,False,True,False,False,False,True,False,False,True,True,True,True,True,True,False,False,True,True,False,True,False,True,False,False,True,True,True,True,True,False,False,True,True,False,False,True,True,False,True], dtype = "bool")#candidate|4696|(896,)|const|bool
call_4693 = relay.TupleGetItem(func_4201_call(relay.reshape(const_4694.astype('float32'), [14, 3, 1]), relay.reshape(var_4695.astype('int8'), []), relay.reshape(const_4696.astype('bool'), [896,]), ), 1)
call_4697 = relay.TupleGetItem(func_4205_call(relay.reshape(const_4694.astype('float32'), [14, 3, 1]), relay.reshape(var_4695.astype('int8'), []), relay.reshape(const_4696.astype('bool'), [896,]), ), 1)
output = relay.Tuple([bop_4676,call_4684,call_4693,const_4694,var_4695,const_4696,])
output2 = relay.Tuple([bop_4679,call_4685,call_4697,const_4694,var_4695,const_4696,])
func_4700 = relay.Function([var_4675,var_4695,], output)
mod['func_4700'] = func_4700
mod = relay.transform.InferType()(mod)
mutated_mod['func_4700'] = func_4700
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4700_call = mutated_mod.get_global_var('func_4700')
var_4702 = relay.var("var_4702", dtype = "float32", shape = (11, 14, 12))#candidate|4702|(11, 14, 12)|var|float32
var_4703 = relay.var("var_4703", dtype = "int8", shape = ())#candidate|4703|()|var|int8
call_4701 = func_4700_call(var_4702,var_4703,)
output = call_4701
func_4704 = relay.Function([var_4702,var_4703,], output)
mutated_mod['func_4704'] = func_4704
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3874_call = mod.get_global_var('func_3874')
func_3875_call = mutated_mod.get_global_var('func_3875')
call_4789 = func_3874_call()
call_4790 = func_3874_call()
output = call_4789
output2 = call_4790
func_4800 = relay.Function([], output)
mod['func_4800'] = func_4800
mod = relay.transform.InferType()(mod)
mutated_mod['func_4800'] = func_4800
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4800_call = mutated_mod.get_global_var('func_4800')
call_4801 = func_4800_call()
output = call_4801
func_4802 = relay.Function([], output)
mutated_mod['func_4802'] = func_4802
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4089_call = mod.get_global_var('func_4089')
func_4091_call = mutated_mod.get_global_var('func_4091')
call_4916 = func_4089_call()
call_4917 = func_4089_call()
output = call_4916
output2 = call_4917
func_4925 = relay.Function([], output)
mod['func_4925'] = func_4925
mod = relay.transform.InferType()(mod)
output = func_4925()
func_4926 = relay.Function([], output)
mutated_mod['func_4926'] = func_4926
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4973 = relay.const([[[8,-8,-2,7,-8,-5,7,-6,-10,-9,8,4,-7,6],[9,4,5,-4,-6,-9,6,-9,6,2,-4,4,-2,-9],[-1,-5,-1,8,10,3,2,2,7,-9,-7,-8,-1,-5],[5,4,-9,6,7,-5,7,4,-1,-5,10,-1,6,-9],[4,-2,10,-4,-6,-8,-8,1,-5,3,3,-6,4,9],[-9,-9,-2,1,-6,10,9,4,-5,1,9,-7,1,-3],[-3,7,3,-4,-4,7,-3,-3,-9,8,-1,5,4,-10],[5,2,-8,-9,-4,5,1,-9,3,7,-8,-7,5,-8],[-1,-5,-4,4,7,-2,-8,8,-3,4,-10,7,7,8],[-5,2,-5,-4,-6,-10,4,4,2,-3,-3,-10,-9,5]]], dtype = "int16")#candidate|4973|(1, 10, 14)|const|int16
var_4974 = relay.var("var_4974", dtype = "int16", shape = (12, 10, 14))#candidate|4974|(12, 10, 14)|var|int16
bop_4975 = relay.less_equal(const_4973.astype('bool'), var_4974.astype('bool')) # shape=(12, 10, 14)
func_2871_call = mod.get_global_var('func_2871')
func_2875_call = mutated_mod.get_global_var('func_2875')
var_4984 = relay.var("var_4984", dtype = "float64", shape = (60, 2))#candidate|4984|(60, 2)|var|float64
call_4983 = relay.TupleGetItem(func_2871_call(relay.reshape(var_4984.astype('float64'), [4, 3, 10]), relay.reshape(var_4984.astype('float64'), [4, 3, 10]), ), 0)
call_4985 = relay.TupleGetItem(func_2875_call(relay.reshape(var_4984.astype('float64'), [4, 3, 10]), relay.reshape(var_4984.astype('float64'), [4, 3, 10]), ), 0)
output = relay.Tuple([bop_4975,call_4983,var_4984,])
output2 = relay.Tuple([bop_4975,call_4985,var_4984,])
func_4989 = relay.Function([var_4974,var_4984,], output)
mod['func_4989'] = func_4989
mod = relay.transform.InferType()(mod)
var_4990 = relay.var("var_4990", dtype = "int16", shape = (12, 10, 14))#candidate|4990|(12, 10, 14)|var|int16
var_4991 = relay.var("var_4991", dtype = "float64", shape = (60, 2))#candidate|4991|(60, 2)|var|float64
output = func_4989(var_4990,var_4991,)
func_4992 = relay.Function([var_4990,var_4991,], output)
mutated_mod['func_4992'] = func_4992
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4089_call = mod.get_global_var('func_4089')
func_4091_call = mutated_mod.get_global_var('func_4091')
call_5040 = func_4089_call()
call_5041 = func_4089_call()
var_5050 = relay.var("var_5050", dtype = "float32", shape = (11, 14, 12))#candidate|5050|(11, 14, 12)|var|float32
bop_5051 = relay.bitwise_xor(call_5040.astype('int32'), relay.reshape(var_5050.astype('int32'), relay.shape_of(call_5040))) # shape=(11, 14, 12)
bop_5054 = relay.bitwise_xor(call_5041.astype('int32'), relay.reshape(var_5050.astype('int32'), relay.shape_of(call_5041))) # shape=(11, 14, 12)
uop_5086 = relay.cos(var_5050.astype('float32')) # shape=(11, 14, 12)
output = relay.Tuple([bop_5051,uop_5086,])
output2 = relay.Tuple([bop_5054,uop_5086,])
func_5088 = relay.Function([var_5050,], output)
mod['func_5088'] = func_5088
mod = relay.transform.InferType()(mod)
var_5089 = relay.var("var_5089", dtype = "float32", shape = (11, 14, 12))#candidate|5089|(11, 14, 12)|var|float32
output = func_5088(var_5089)
func_5090 = relay.Function([var_5089], output)
mutated_mod['func_5090'] = func_5090
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3874_call = mod.get_global_var('func_3874')
func_3875_call = mutated_mod.get_global_var('func_3875')
call_5152 = func_3874_call()
call_5153 = func_3874_call()
func_534_call = mod.get_global_var('func_534')
func_537_call = mutated_mod.get_global_var('func_537')
var_5157 = relay.var("var_5157", dtype = "int8", shape = (1, 1568))#candidate|5157|(1, 1568)|var|int8
call_5156 = relay.TupleGetItem(func_534_call(relay.reshape(var_5157.astype('int8'), [16, 7, 14])), 1)
call_5158 = relay.TupleGetItem(func_537_call(relay.reshape(var_5157.astype('int8'), [16, 7, 14])), 1)
output = relay.Tuple([call_5152,call_5156,var_5157,])
output2 = relay.Tuple([call_5153,call_5158,var_5157,])
func_5171 = relay.Function([var_5157,], output)
mod['func_5171'] = func_5171
mod = relay.transform.InferType()(mod)
var_5172 = relay.var("var_5172", dtype = "int8", shape = (1, 1568))#candidate|5172|(1, 1568)|var|int8
output = func_5171(var_5172)
func_5173 = relay.Function([var_5172], output)
mutated_mod['func_5173'] = func_5173
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4800_call = mod.get_global_var('func_4800')
func_4802_call = mutated_mod.get_global_var('func_4802')
call_5177 = func_4800_call()
call_5178 = func_4800_call()
func_4800_call = mod.get_global_var('func_4800')
func_4802_call = mutated_mod.get_global_var('func_4802')
call_5185 = func_4800_call()
call_5186 = func_4800_call()
bop_5196 = relay.power(call_5177.astype('float32'), relay.reshape(call_5185.astype('float32'), relay.shape_of(call_5177))) # shape=(11, 14, 12)
bop_5199 = relay.power(call_5178.astype('float32'), relay.reshape(call_5186.astype('float32'), relay.shape_of(call_5178))) # shape=(11, 14, 12)
uop_5202 = relay.atan(bop_5196.astype('float32')) # shape=(11, 14, 12)
uop_5204 = relay.atan(bop_5199.astype('float32')) # shape=(11, 14, 12)
bop_5213 = relay.equal(uop_5202.astype('bool'), relay.reshape(bop_5196.astype('bool'), relay.shape_of(uop_5202))) # shape=(11, 14, 12)
bop_5216 = relay.equal(uop_5204.astype('bool'), relay.reshape(bop_5199.astype('bool'), relay.shape_of(uop_5204))) # shape=(11, 14, 12)
func_4800_call = mod.get_global_var('func_4800')
func_4802_call = mutated_mod.get_global_var('func_4802')
call_5226 = func_4800_call()
call_5227 = func_4800_call()
output = relay.Tuple([bop_5213,call_5226,])
output2 = relay.Tuple([bop_5216,call_5227,])
func_5240 = relay.Function([], output)
mod['func_5240'] = func_5240
mod = relay.transform.InferType()(mod)
mutated_mod['func_5240'] = func_5240
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5240_call = mutated_mod.get_global_var('func_5240')
call_5241 = func_5240_call()
output = call_5241
func_5242 = relay.Function([], output)
mutated_mod['func_5242'] = func_5242
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5240_call = mod.get_global_var('func_5240')
func_5242_call = mutated_mod.get_global_var('func_5242')
call_5245 = relay.TupleGetItem(func_5240_call(), 0)
call_5246 = relay.TupleGetItem(func_5242_call(), 0)
output = call_5245
output2 = call_5246
func_5249 = relay.Function([], output)
mod['func_5249'] = func_5249
mod = relay.transform.InferType()(mod)
mutated_mod['func_5249'] = func_5249
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5249_call = mutated_mod.get_global_var('func_5249')
call_5250 = func_5249_call()
output = call_5250
func_5251 = relay.Function([], output)
mutated_mod['func_5251'] = func_5251
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5256 = relay.var("var_5256", dtype = "float64", shape = (5, 6, 3))#candidate|5256|(5, 6, 3)|var|float64
var_5257 = relay.var("var_5257", dtype = "float64", shape = (5, 6, 3))#candidate|5257|(5, 6, 3)|var|float64
bop_5258 = relay.divide(var_5256.astype('float64'), relay.reshape(var_5257.astype('float64'), relay.shape_of(var_5256))) # shape=(5, 6, 3)
uop_5272 = relay.asinh(var_5257.astype('float64')) # shape=(5, 6, 3)
func_4201_call = mod.get_global_var('func_4201')
func_4205_call = mutated_mod.get_global_var('func_4205')
const_5279 = relay.const([-5.747604,-9.041558,9.003213,-4.761108,2.849014,-7.549002,5.322826,3.470407,-3.589981,7.691218,-4.765234,-6.058297,2.504498,-4.517217,-0.282512,-7.361229,1.681939,4.378118,8.334477,-2.515369,-2.776426,-9.956871,-5.464455,-9.176349,-7.490575,-9.483203,1.649644,-6.392741,-3.451297,0.013374,4.064235,7.406419,-6.588293,-9.379138,-8.104665,0.123553,6.181887,-8.452567,9.892312,1.926782,-7.425667,-7.391818], dtype = "float32")#candidate|5279|(42,)|const|float32
var_5280 = relay.var("var_5280", dtype = "int8", shape = ())#candidate|5280|()|var|int8
var_5281 = relay.var("var_5281", dtype = "bool", shape = (896,))#candidate|5281|(896,)|var|bool
call_5278 = relay.TupleGetItem(func_4201_call(relay.reshape(const_5279.astype('float32'), [14, 3, 1]), relay.reshape(var_5280.astype('int8'), []), relay.reshape(var_5281.astype('bool'), [896,]), ), 0)
call_5282 = relay.TupleGetItem(func_4205_call(relay.reshape(const_5279.astype('float32'), [14, 3, 1]), relay.reshape(var_5280.astype('int8'), []), relay.reshape(var_5281.astype('bool'), [896,]), ), 0)
func_2208_call = mod.get_global_var('func_2208')
func_2211_call = mutated_mod.get_global_var('func_2211')
const_5287 = relay.const([-2.596816,8.887340,4.409455,1.199931,2.896295,8.463531,-1.352020,5.384652,-0.689505,8.114843,-2.101084,1.092675,0.127416,8.949549,2.275911,9.041048,-7.917673,7.535934,9.351421,5.496867,-9.495187,2.704940,8.377483,9.065693,0.691382,8.689283,-8.848451,-9.895101,-5.279204,-2.719616,6.679269,-7.858989,-3.217779,-1.788190,-6.142934,9.106490,-9.647305,5.118621,1.984900,5.499939,6.783839,-0.928466,1.819594,-0.223198,-5.328135,-9.998142,-0.261221,5.477609,-4.073889,-6.706326,-5.828272,-6.196701,0.095688,-8.036740,-4.048223,7.709266,-6.598934,7.909082,-3.164823,9.877821,-1.420937,3.947043,-1.396513,9.182957,-9.074284,8.473300,8.596669,9.664314,-8.551150,3.638213,4.745014,-0.251984,-7.302238,-4.849445,2.168918,-0.296778,7.781326,4.456413,-9.745319,-3.419136,-7.872465,1.875292,5.724783,-1.029107,-1.460410,-4.630166,-5.916965,3.200600,-6.385241,-6.987470,-0.387339,4.223557,-1.811914,3.958455,-6.327544,2.996713,-8.778172,-3.956775,2.777313,7.771168,7.498981,7.192773,-8.430392,-7.327104,-2.087934,5.124413,2.737259,-0.423156,5.837073,3.606444,-9.164922,-3.634788,4.388221,-0.472674,-5.093617,6.130562,-9.474107,3.221699,6.886747,7.403277,-1.800409,-6.931628,-4.726635,4.025472,3.171669,5.502564,1.568753,-5.134029,-3.489708,2.419988,-2.626224,-0.349735,-1.265978,4.236786,-8.357567,3.042959,7.772528,-8.107958,2.236010,7.753846,-7.660951,-6.227703,6.637665,2.803322,1.153525,-3.316442,6.522350,-2.243635,-6.442599,8.790833,3.666748,-3.395647,1.724804,-0.301669,-2.284077,9.040966,-7.316801,8.645965,-3.902926,2.751469,8.397272,3.308155,5.031966,-7.138420,2.127102,-5.233324,8.214508,-9.958149,6.478386,7.518181,-9.349238,2.168076,-1.473331,-9.771932,7.353493,-0.102589,1.078146,2.334484,-8.096738,4.397100,4.833306,-3.584962,-9.174360,0.662537,3.764912,3.096356,8.232019,-7.879407,5.363582,-4.095392,-0.282513,-8.677544,-5.779141,-2.968793,1.975967,3.218747,2.877411,3.004592,-5.798763,-4.331906,9.150882,0.774592,-0.034337,-1.465601,8.819382,-3.318035,-5.328555,6.589374,-9.753196,9.716875,4.418598,-3.230873,-3.009943,-9.968031,0.019887,-9.927873,4.881476,0.131340,9.593304,9.099298,5.404694,-7.220803,-1.568292,-7.692283,-5.456302,1.483034,-3.910440,-5.120373,6.355005,6.808944,2.412804,-5.205615,-6.831448,-7.084328,9.681671,-4.846727,5.274349,-5.292911,-3.050792,-0.824392], dtype = "float64")#candidate|5287|(240,)|const|float64
call_5286 = func_2208_call(relay.reshape(const_5287.astype('float64'), [12, 2, 10]))
call_5288 = func_2208_call(relay.reshape(const_5287.astype('float64'), [12, 2, 10]))
func_534_call = mod.get_global_var('func_534')
func_537_call = mutated_mod.get_global_var('func_537')
const_5291 = relay.const([[-2,-1,-9,-5,-1,-3,-2,-9,-1,1,-9,-1,-3,6,4,-4,-4,1,5,6,-6,-7,5,9,10,4,-2,10,3,3,-2,6,-1,9,-3,-4,-7,1,8,8,2,9,4,-9,7,-6,8,-3,1,7,-9,4,3,-8,3,-10,5,-9,1,9,8,5,9,7,1,3,6,-6,3,3,-7,3,4,-2,-7,-1,8,5,3,7,-5,-6,8,-1,5,8,-6,-7,-10,3,1,6,-9,5,10,-8,2,7,7,2,-1,5,9,10,-10,-9,-9,10,-6,2,9,-3,5,3,-8,-3,5,-8,1,-4,-1,1,7,-7,-8,-9,10,-8,-1,-8,-5,-8,10,-3,-4,-1,-1,4,-6,3,10,1,-5,7,-9,5,-8,4,-8,9,7,8,6,8,-1,-8,-4,-10,-9,6,-4,3,3,9,6,5,10,1,-3,10,1,-6,-6,-5,5,-4,-2,10,2,-7,9,-2,-7,-7,-4,-6,-4,10,-1,6,8,-5,-4,-6,-4,7],[-6,4,-3,-6,7,-2,4,-10,8,-1,3,9,-10,-6,-7,-8,3,8,3,3,-4,1,-8,3,7,4,-9,-9,-7,3,-9,9,-5,8,-9,-9,7,-2,-3,2,-10,-1,-1,-8,-7,-2,-4,-6,6,-8,-8,-9,-9,1,10,1,2,-1,-4,9,9,-6,2,1,-10,4,-6,-3,6,6,-7,-7,10,-2,-4,6,4,-8,7,-4,-8,5,3,-8,3,-6,2,-1,-9,7,-6,1,-8,-6,-6,-4,-9,8,-8,-3,-10,-3,-2,5,9,-7,8,5,-4,-2,1,5,-6,4,-1,7,5,4,-6,9,4,10,-3,-7,-8,-9,7,-1,-1,7,1,3,-1,3,7,-3,-9,10,-2,1,8,-10,-8,-7,5,8,5,-4,-8,6,-1,4,-3,-2,-3,-6,-6,7,-7,-2,-6,2,2,8,5,5,2,-5,-6,-2,1,2,-4,1,3,6,4,1,-4,-5,-4,6,-2,2,10,-10,2,8,3,9,-3,-7,3,-2,-8,9],[-9,-9,5,-2,-5,-6,4,-5,5,5,1,4,10,4,-5,4,-7,7,-2,7,-1,6,-8,2,-7,1,9,-5,-3,10,3,2,-7,-9,7,-6,-8,-4,5,10,-5,3,10,4,8,-1,-10,-8,1,-5,3,7,-4,-8,6,-3,2,-4,6,6,-4,5,-10,-10,-2,1,6,9,-8,-1,6,7,9,-10,1,-9,1,-10,6,-3,-5,-4,-4,-1,9,-9,5,2,-9,-1,8,-7,5,-1,-7,9,-1,-1,5,7,3,10,-2,-3,7,-1,-5,4,-6,-1,1,5,3,7,9,4,10,3,8,-4,2,-10,4,7,2,4,-9,5,6,-2,8,8,-9,1,-7,-2,2,5,7,9,1,-3,10,-2,4,1,9,-1,10,-6,8,-5,-2,-10,4,10,-1,-8,3,-7,-6,-8,-10,3,-10,7,9,-10,-2,-1,8,-4,6,-1,-1,-7,-9,-2,-3,-8,-4,-5,-7,-5,5,-5,-9,3,-8,4,5,8,6,2,5,-4],[-7,3,4,-10,3,-4,-2,-8,3,4,1,1,-4,-9,-3,9,2,3,-9,6,8,-6,1,5,-6,-2,-2,6,-4,-4,-8,8,-2,-9,-3,5,-7,4,-5,-3,-7,-9,6,3,-10,10,8,1,10,-3,5,6,6,-1,8,-1,-7,-4,-8,4,3,-10,-3,-3,1,7,1,-9,5,10,-3,10,3,-6,10,1,-5,6,-1,2,2,-7,5,2,5,-7,2,2,-3,8,-8,9,-9,-1,2,2,3,9,-5,-9,-2,3,-4,-1,1,10,-8,3,4,8,9,3,1,-9,-4,9,5,-2,-6,7,4,-9,6,2,7,-7,-1,-6,2,-9,6,-4,1,-3,1,-2,-7,1,-2,5,-4,6,3,-10,-9,-3,8,-9,3,3,2,-3,8,-4,7,-2,4,-8,9,-3,-6,5,-4,-2,6,3,3,-9,-9,3,-4,9,-2,6,3,-2,-8,3,-1,8,-10,-5,8,4,-9,-5,2,3,-1,5,-10,2,-4,-1,10,2],[2,-3,-3,8,-3,-5,7,9,6,-1,-1,-6,10,9,7,-1,1,7,-2,8,-8,-2,-8,2,-7,4,-7,-2,-8,-10,4,-3,-7,1,-7,-5,-1,-1,-10,-4,-7,-2,9,-5,6,-3,7,7,10,1,6,-4,5,-7,10,9,-2,-4,-6,7,2,-2,7,3,7,7,-2,-2,6,-9,1,-4,10,3,6,-7,3,9,7,9,6,9,7,-4,-1,9,-10,6,-4,-5,10,-1,1,2,4,2,-7,7,-2,-7,3,-4,3,-4,-8,7,10,10,-10,9,-4,-3,6,5,2,-9,-1,9,-3,-9,1,-1,-6,4,3,-7,8,2,-3,-10,-10,-9,3,5,10,-1,1,-3,2,10,-3,-6,10,-5,-4,5,5,7,3,-6,-5,5,-8,3,-10,-7,2,3,9,5,2,-1,8,-5,-7,6,-9,-8,-1,-6,5,-3,-7,1,4,-1,-5,-1,8,4,6,-9,-2,1,9,-4,1,1,6,3,-7,-4,9,-7,-3,4],[10,-4,2,6,5,8,-1,-3,3,5,-2,-2,6,10,2,-9,-9,5,-10,-5,-2,10,-3,10,-1,-6,6,6,9,1,1,-4,-5,-4,-1,-10,3,8,-3,2,5,-6,5,-3,7,-6,6,-9,-10,-5,-3,3,5,1,-10,-1,-10,6,-1,2,4,8,-7,-2,1,7,4,-9,-1,-8,-3,8,10,-9,-2,8,-8,-8,5,-3,9,10,9,-4,-2,-5,-5,-8,-6,3,7,-6,10,-1,7,-3,5,-2,5,-9,10,1,5,-8,6,1,-7,-8,4,-3,-7,-7,-10,-7,5,-1,9,10,-1,7,4,-9,-6,7,8,10,8,8,-6,-4,-2,-8,7,7,10,5,1,-4,-3,-6,3,-8,3,9,-2,2,10,-7,10,6,5,4,5,4,9,9,-7,-2,-3,-2,6,1,6,4,9,7,-9,-1,-7,2,-6,-7,-8,-3,-10,7,3,-3,-3,6,-6,7,4,-2,2,8,-5,-1,3,-5,3,10,-10,-4,1,7],[4,5,-10,10,10,-2,-2,1,10,-10,-10,10,5,-4,-5,4,-3,-7,5,-8,7,2,-4,-5,-9,-1,5,-8,5,-7,-1,8,-9,8,6,8,6,1,3,8,2,10,1,10,-9,4,7,5,-1,-9,-1,-8,-9,8,-8,-1,-6,-8,10,-2,-4,-1,10,-8,-1,8,5,10,7,-5,4,3,-8,8,-8,9,5,-2,7,6,10,1,-9,9,-7,-1,10,-3,-7,-6,-9,7,-4,1,-1,-9,-10,-6,1,7,2,1,1,10,-6,3,3,1,10,-9,8,2,10,9,7,-9,3,9,-5,10,-7,-7,2,8,-10,3,-6,-8,-6,8,-4,-10,-9,8,10,-7,4,9,-2,8,-5,1,-7,-10,7,-6,-6,-7,7,-1,7,6,-2,7,-4,-9,5,2,1,7,-9,1,9,-10,-7,-5,-9,-6,-8,6,-6,-10,-6,-5,4,7,4,9,-9,-2,-8,-1,-10,7,-7,-7,-9,-6,-3,2,-4,1,10,-5,-8,3],[4,2,-10,1,3,10,6,7,-8,7,1,-4,-9,-7,-6,3,-6,-5,4,-4,3,-1,2,10,-8,-4,6,-7,6,2,-8,-1,9,-1,-9,2,-8,3,-10,2,10,6,-5,-1,-8,-3,5,3,8,-7,-8,1,1,-8,6,8,7,2,-8,4,-3,4,-1,-1,10,7,8,-6,3,7,-5,5,-8,7,-7,4,8,-9,-5,-7,10,-3,-6,-5,-2,-8,7,10,-8,3,-7,-5,-7,3,7,-6,-6,3,-7,-10,-3,7,-10,9,-3,-5,-1,5,-7,9,10,10,2,9,4,-8,6,8,2,5,-10,-8,-3,9,3,3,-1,9,-6,3,-8,6,-8,-3,2,6,10,-2,-8,2,-7,5,6,3,4,2,9,-7,4,7,-10,7,8,-1,-10,-8,-8,7,8,-5,-8,-6,7,-3,-5,-7,5,5,3,10,10,10,-2,9,-7,-6,-1,1,8,-9,4,10,-9,-3,-2,6,2,10,-3,7,5,-6,-8,4,-10,-10]], dtype = "int8")#candidate|5291|(8, 196)|const|int8
call_5290 = relay.TupleGetItem(func_534_call(relay.reshape(const_5291.astype('int8'), [16, 7, 14])), 1)
call_5292 = relay.TupleGetItem(func_537_call(relay.reshape(const_5291.astype('int8'), [16, 7, 14])), 1)
func_1259_call = mod.get_global_var('func_1259')
func_1263_call = mutated_mod.get_global_var('func_1263')
var_5309 = relay.var("var_5309", dtype = "int64", shape = (845,))#candidate|5309|(845,)|var|int64
var_5310 = relay.var("var_5310", dtype = "float32", shape = (180,))#candidate|5310|(180,)|var|float32
call_5308 = relay.TupleGetItem(func_1259_call(relay.reshape(var_5309.astype('int64'), [5, 13, 13]), relay.reshape(var_5310.astype('float32'), [180,]), relay.reshape(const_5291.astype('int8'), [1568,]), ), 4)
call_5311 = relay.TupleGetItem(func_1263_call(relay.reshape(var_5309.astype('int64'), [5, 13, 13]), relay.reshape(var_5310.astype('float32'), [180,]), relay.reshape(const_5291.astype('int8'), [1568,]), ), 4)
uop_5312 = relay.tan(const_5291.astype('float64')) # shape=(8, 196)
uop_5314 = relay.log(uop_5312.astype('float64')) # shape=(8, 196)
bop_5320 = relay.left_shift(const_5291.astype('int8'), var_5280.astype('int8')) # shape=(8, 196)
var_5332 = relay.var("var_5332", dtype = "float64", shape = (8, 196))#candidate|5332|(8, 196)|var|float64
bop_5333 = relay.multiply(uop_5314.astype('uint32'), relay.reshape(var_5332.astype('uint32'), relay.shape_of(uop_5314))) # shape=(8, 196)
bop_5336 = relay.floor_mod(uop_5314.astype('float32'), relay.reshape(bop_5320.astype('float32'), relay.shape_of(uop_5314))) # shape=(8, 196)
const_5340 = relay.const([[8.069903,0.801579,-8.776166,1.714455,9.558340,8.303313,5.162374,9.012058,6.833440,-7.402054,8.825587,-4.085666,6.414502,4.147220,7.691279,-5.412759,3.266478,9.078075,-5.222575,2.304393,8.316191,8.654684,-4.239030,7.147272,-9.792761,-3.036448,-6.685264,0.211992,-3.757074,1.867974,-8.499885,-3.331750,5.407627,5.615829,9.786807,9.840429,2.444361,0.983760,-5.991758,-8.990159,-7.515509,-4.051610,0.905676,-7.211330,-6.734140,-8.765651,7.193344,-7.940763,-1.264223,-2.628943,-4.053820,-9.341873,4.748187,-6.533975,-5.217667,-6.002955,8.557528,-7.045833,-5.574700,-7.671676,-4.803566,6.996560,-7.069830,1.372436,-1.206702,-4.905302,4.553060,-3.478900,-9.429070,-0.812227,1.267793,4.528335,6.948216,-9.767733,3.186135,-1.053518,8.570108,0.404207,-3.350271,-2.395289,7.652720,0.046241,5.271189,6.000227,-1.216772,-5.336830,-0.029149,0.850245,9.881075,9.335707,-2.505666,6.212613,-2.836380,8.198162,6.273388,7.981041,-4.572149,0.301144,-2.852277,1.472592,6.938610,0.795340,-2.012277,1.463057,-3.637385,-8.067728,9.019416,-6.385717,-2.354440,-2.995421,2.319928,-4.759683,-8.036768,8.261950,-9.832352,-9.683724,-5.379590,7.949138,-1.730421,8.794873,-9.000990,4.689134,6.150129,6.051187,-8.179533,7.526536,6.556251,8.553853,5.031214,-2.585298,-7.454376,1.543796,-6.811387,0.773093,-2.041359,2.913086,-6.231435,-6.643401,-1.277047,6.827562,7.634756,-5.627009,2.519729,-3.239660,-5.364803,-9.938059,6.733644,-9.959347,1.395954,-7.678116,-7.455918,-6.402026,5.431039,-0.610025,-0.365384,-7.670544,-2.752718,-5.220644,-3.201245,-9.552896,7.946285,5.244851,6.273823,0.448532,4.044218,-0.314078,1.626912,-0.788955,9.075043,9.669375,4.447745,3.970826,-1.805877,0.360424,-0.368014,-7.172068,-0.996527,6.307630,2.178789,-7.235393,-5.336240,-2.935314,3.595181,-1.251023,5.695740,-0.486080,0.703449,-7.871383,5.767190,8.518707,4.706838,-9.527597,7.158811,9.782972,-5.111106,-5.725530],[-3.158611,-2.542104,6.363970,-8.029848,-6.603923,5.964255,-9.093415,-9.821153,3.484043,-6.982062,2.222216,2.097878,-2.251747,0.924473,-9.262586,2.489775,-9.650371,2.485731,4.448959,-3.793005,-2.176512,7.466830,7.509679,3.390110,3.657448,1.076394,-7.192454,-1.467453,-7.545450,1.329262,8.223242,6.238810,-6.335445,2.462675,6.091928,-5.805209,-4.976432,-2.378793,0.202080,-9.310681,8.644569,7.613431,-5.838655,-9.085197,9.120184,-5.284138,0.714010,-7.906255,-3.002396,1.371119,4.152277,8.167648,1.219778,1.870424,6.086321,-0.769444,9.289751,-7.641660,8.592532,-6.666509,-0.322292,4.021187,4.970374,-5.743861,8.918410,2.767835,1.059225,-2.139982,-4.457465,1.544186,-6.310330,6.596260,3.794590,4.016966,-2.031116,8.106009,-2.503076,-5.094923,-6.719299,2.304847,-1.085328,-4.576771,-4.151338,8.511758,-2.922587,-2.523171,-8.661870,-2.292048,-6.896531,-9.434933,-7.822564,4.470369,-2.427828,-0.302992,-7.266380,-1.622717,-3.189148,-2.249175,-8.611254,7.407999,-3.376789,1.972556,0.107140,-5.778040,7.097745,2.966545,-9.824028,6.270782,-5.353738,9.481734,0.952328,-2.200398,-1.246067,-7.392961,-0.960717,1.410016,-2.693116,2.185071,6.776748,0.383273,-1.820149,-9.982831,1.653438,5.224616,5.117576,8.916342,-2.894744,-3.733413,-4.574265,5.926106,-4.160089,-8.618197,2.284465,7.892166,5.791878,-1.886834,2.018864,5.167866,-5.015591,-0.974308,2.308157,-8.033451,4.237368,4.526263,-2.742539,-2.457972,2.315720,6.410728,-4.392563,0.315735,8.777525,2.093444,-2.670453,6.615595,4.410139,-4.698662,0.281158,8.121581,1.732401,9.400800,6.284878,4.344007,-1.950009,-4.253541,8.797571,-5.212893,8.046359,9.595282,-8.569598,-9.037934,-8.843828,7.352882,8.054606,4.290359,7.889005,-7.448136,-0.806638,9.020973,-8.130348,-0.515202,-7.370277,-6.997221,-8.529366,1.032968,1.394313,1.688059,1.368342,5.896196,3.359316,6.214922,2.192864,0.706830,9.379747,-6.418736,-7.599166,5.455700],[-9.478357,-7.401919,6.330095,0.358875,7.113318,1.789803,0.859432,-1.939116,4.112149,1.529036,9.081071,-9.140162,-6.359663,0.526773,2.829146,0.529980,-1.312158,6.144609,9.883154,-3.235941,3.129607,8.362857,1.838781,8.438760,-7.768619,9.150582,7.862434,-3.592773,2.550014,8.185749,4.646996,-3.288512,-7.257207,7.851299,-9.929705,7.830736,4.077796,9.676238,-2.067406,9.603567,3.322556,-0.782186,4.739909,-1.211160,-6.687807,7.307973,-0.514915,-4.090038,5.468157,7.890063,2.667543,7.269319,4.083930,0.889640,3.180942,-9.090787,-5.492593,-4.044178,-1.595579,-6.755701,-8.863704,-6.041540,1.999923,0.634740,-7.056841,-5.818178,4.772090,2.322692,-9.372015,-0.178323,4.588558,8.003276,-8.530657,3.969039,-8.551203,6.247412,-8.882446,-5.063236,-7.204497,-8.629196,-1.208916,5.365691,5.915644,-4.147806,0.143410,3.932874,-4.904693,-8.865945,-6.688701,6.745123,4.560862,9.880332,-8.924356,7.522858,-5.988500,4.326217,1.919953,-0.881060,7.863686,-9.486824,-1.683571,-7.463539,-2.592777,6.461500,-3.910935,-2.699754,8.313331,3.559942,2.543434,0.966679,0.350751,-2.951611,4.201688,9.925577,6.320797,0.995468,8.207830,-1.085693,1.674224,6.429841,-3.894263,3.596673,3.766271,2.387688,-0.224789,-7.168769,-2.548606,-7.118155,-2.514515,-2.826105,3.525786,3.703039,6.263462,2.863242,4.392856,6.778844,-2.288358,2.091115,5.390850,-1.533045,2.195932,5.090802,2.873854,9.025397,8.289142,1.216826,-9.969946,-5.344440,0.377010,-2.363273,-8.445771,-7.641961,-3.400646,-2.734408,4.980237,9.928362,-4.212174,-3.959035,-9.682066,9.518977,1.054126,9.302826,8.728415,-1.185023,7.302913,0.960874,-2.447247,-4.232095,3.681497,-6.265774,5.934410,-6.696709,7.482539,8.582757,-4.732667,2.134950,4.308991,0.752918,-6.949649,5.836656,-5.726325,5.845986,9.013461,-3.372878,6.975176,3.095423,-2.818627,-0.730130,-0.330221,-2.487309,-2.175529,-7.445117,-7.120951,-8.506084,9.061227,-0.411927],[-4.334149,-1.666909,8.161439,-4.302584,-4.886417,1.622260,0.915008,-2.857583,6.876486,8.925757,-4.416912,3.336403,8.786420,-3.978372,-6.197059,1.123930,-3.059586,-5.262434,-8.525188,-8.253157,-6.941404,8.340901,7.815609,5.223154,-9.766570,-3.046848,-5.503004,4.932707,2.742280,8.436709,-4.351426,-0.373808,-9.676020,-7.716264,-8.778951,7.434988,-7.777974,-5.104053,-6.240161,-7.823366,-6.877436,-2.121801,3.631801,9.723304,4.150480,-1.904471,4.861966,-0.235626,2.739632,-7.804688,-5.744041,-2.113333,-2.323391,-9.490388,-1.055584,-2.875448,-4.203245,6.158921,-7.379010,-2.650701,8.340764,-6.637119,-7.694248,2.987156,1.198258,9.145012,2.826135,4.832468,-0.867450,5.352837,-2.441152,-4.765580,-9.885836,-0.980592,-4.813564,-1.942478,2.160878,-0.871601,5.288731,8.902337,0.773008,-8.616794,-8.575569,-4.405004,-9.751473,5.506319,5.128515,8.305281,-7.457004,8.164758,-9.106390,-8.542394,-2.245625,1.289315,-8.432030,-2.742101,7.993505,5.409966,-9.237076,2.866624,5.947326,-4.528129,-3.866363,-5.568890,0.813035,2.353205,4.577158,-8.070281,-3.985017,6.372261,-0.029246,-6.556983,7.745417,-2.570814,9.314923,-3.609824,-4.965249,-6.596868,-0.199272,4.150266,-1.753110,3.768150,9.548993,8.039489,-8.082697,-6.486031,-4.987968,-9.905164,-4.347060,-6.466602,-3.157189,-4.756931,4.525024,6.844986,7.467505,0.263966,9.703017,3.798620,-0.738581,-7.927122,-6.377641,-7.425428,5.897268,-5.614416,6.660845,-4.880597,5.109381,-9.257303,9.246680,-7.540906,8.827366,-0.572878,-7.310308,9.548622,-6.503137,3.308501,-7.542583,5.811418,8.010155,-5.695775,-2.895082,-7.966730,7.503449,-2.235467,8.187086,-6.728222,8.564603,5.372587,-3.326857,-0.194517,3.567537,9.245916,4.987966,0.895942,-6.020971,2.331831,-5.757011,-8.378950,8.339333,-3.613121,0.005927,6.988538,1.849409,4.034220,7.596712,-7.640341,2.730906,-1.616677,7.322034,0.397389,3.469447,-5.851754,9.059654,-5.916058,-4.146404,2.615521],[7.950130,-3.443400,5.252161,-7.840334,0.849548,8.846643,6.559223,-0.954101,-7.997761,-4.155346,-5.122728,3.787433,-1.300582,-0.305803,8.794606,-7.939101,-4.530279,5.725815,-2.208971,-2.454303,4.154338,2.794784,-9.793964,5.267239,2.979039,-1.974381,-0.015896,7.663090,5.465281,7.569321,5.576210,9.907249,-7.746899,-9.313609,8.054939,9.077444,-8.442486,9.179522,-0.640079,7.407488,-8.291659,2.932390,-7.818106,7.664135,7.299541,-2.464123,2.228710,-9.579911,-8.969632,-9.737294,-2.865360,-8.612560,-2.432016,8.316072,-9.384932,7.209269,-3.816957,-4.395507,0.275780,3.342605,-0.374449,-2.690243,1.635326,-9.960902,8.448760,9.061477,-4.654906,-8.792530,5.227219,5.170767,5.947286,1.326794,3.437280,-3.708413,8.281923,6.988549,8.765158,6.963317,8.502910,-7.652678,2.108305,-8.729888,-0.837851,-3.462732,-0.564014,9.539623,-8.271834,0.312421,-3.129492,1.200235,2.771337,-6.660496,-7.719514,-9.210798,6.666940,-2.004989,-1.689278,-5.739295,6.034293,5.707158,-0.191998,2.061644,0.507180,-0.909043,-1.214575,6.633046,9.503145,-6.242029,-8.217804,6.956506,-8.432913,-1.415415,-0.621464,9.494924,6.663928,2.950640,3.227089,9.336961,8.518643,4.913045,7.046120,-2.557746,-3.551056,-9.715508,6.605624,-8.560933,5.709477,-0.195510,0.490838,1.880565,-8.915314,-1.188210,-5.049874,-7.044874,7.587238,5.298951,9.650771,9.620807,4.305977,-1.030047,0.484697,-8.387712,1.110609,-3.154085,-6.893157,2.500653,-7.779613,-5.798332,9.787385,3.184474,-9.569802,4.714195,-4.990202,0.965513,-7.921555,-5.166332,-3.021292,-2.913211,1.594904,-8.189111,7.889074,7.701394,1.611216,-9.284326,-9.821910,-9.357117,-3.076724,-1.885599,-9.717371,-7.790862,8.633486,6.557076,7.082766,7.469248,-4.038233,-8.134896,-6.088803,-4.613522,-4.171970,-5.995522,-5.875409,8.973065,1.722337,1.713483,-9.795230,-0.872840,-1.113021,4.128729,-7.263003,-6.576428,5.791718,-5.730867,-6.963844,6.215023,5.444167,-1.225869],[-2.790287,-2.637814,9.220445,-4.701057,-8.708065,-0.247046,-2.401647,-1.144174,-2.433280,1.938633,-4.477067,0.092497,-1.324216,8.114807,4.455841,4.550736,9.227333,2.671570,2.158669,-8.082093,-4.915337,-6.402171,8.403959,3.786517,-4.156447,6.615638,-0.420200,3.662270,4.838148,-7.279841,-1.250067,8.443240,-0.870954,3.488846,-2.452830,9.217711,-5.702151,9.772551,-2.722057,4.860284,5.002102,7.814122,-0.785382,3.352951,8.582577,-6.357175,8.480215,-5.218083,-1.752454,-2.552765,0.429639,1.845612,6.058344,5.970019,-5.557228,-3.998839,3.121773,1.434696,9.648110,-8.939951,6.856118,-4.495168,-7.274331,-7.633139,-4.703808,8.551661,-1.617964,6.029947,8.729547,4.297955,-2.851284,7.174850,-3.303823,2.118905,4.896191,-1.135585,-2.479026,-9.526093,4.570532,0.873591,1.346465,-0.074884,9.643406,6.249627,-4.805227,-0.852848,4.562940,5.286460,7.161861,0.454397,-2.168309,4.256722,-2.612485,9.525980,-4.621647,-5.862209,1.119520,8.428655,-2.171823,2.863034,8.881702,9.752484,9.025424,-1.658437,3.386910,-1.165051,-0.998528,-4.073316,6.340851,-5.867792,-3.307706,6.748566,1.799014,8.076538,8.833423,7.938306,-3.793193,3.979901,1.068947,-9.094476,2.067342,-0.817210,-3.784530,0.210579,-2.694156,7.209128,-7.388381,-0.139761,4.904380,3.824599,-0.129992,-2.582852,-9.470299,-7.404373,8.100984,-2.184807,9.525481,-7.354786,-6.546115,1.683068,-8.516507,4.060695,6.106224,-2.522162,2.790014,-6.718674,-4.015799,6.005058,-7.345310,-2.325559,-8.095391,9.350041,4.947889,-3.429474,9.034964,-9.211029,-5.277539,-7.271215,8.902953,0.538660,-8.213886,-1.292691,-6.645731,0.681054,-7.282716,-2.905995,8.099967,-8.532491,-9.315757,-8.838510,8.780328,7.912033,-4.628145,5.365675,-4.061456,1.968411,-8.240386,-6.412011,5.137031,-7.721138,0.088481,-6.891020,-8.704928,-6.681678,9.442834,-7.190440,1.615730,2.829792,2.060147,-0.236614,2.350343,-3.076259,6.168890,-8.867537,1.514834,-5.230951],[8.555097,5.206731,-9.557649,-2.218415,-8.243412,-5.426554,-7.745928,4.502056,-9.833625,-9.364765,1.828852,-4.439539,8.056568,3.458432,6.220549,1.012509,3.377527,-9.155785,-1.491794,6.151899,4.699040,0.397601,4.805310,5.561584,-9.307335,3.881101,-3.632296,-2.460467,-7.487893,-2.076978,-4.823854,4.159248,-3.867598,1.387724,-7.221173,4.087873,-9.643086,-4.372765,-7.651419,6.116656,3.445821,-8.423275,-9.305419,0.824595,7.086657,-0.331220,8.301416,8.097851,9.943925,9.594775,2.944797,3.702783,7.384168,-6.506212,6.140062,-0.328555,-6.136238,3.353677,8.752478,-6.690134,-9.786940,-8.430607,-0.642135,-4.632579,-0.441560,1.003328,-8.187897,8.013750,-5.922192,7.215956,-0.796399,-6.708289,5.954204,6.135470,-7.683486,4.745008,7.014346,6.646317,1.843157,9.245303,4.237135,5.368472,-7.449389,3.665961,-7.364310,-4.120342,-4.390495,-5.436697,-6.207089,-3.244504,2.503683,-7.835504,-8.862428,-9.990028,1.686963,7.461346,-1.455765,-9.300716,-9.683816,-3.872278,9.992619,1.588220,2.958789,5.398370,9.123267,5.763186,9.502053,6.658182,1.508803,9.920708,-5.093112,5.820460,5.095274,3.914356,9.662615,7.601597,-3.320500,-2.051796,-3.084363,-9.448002,3.056465,-9.781271,4.716789,-9.844099,0.233164,5.714249,4.518367,-8.772545,-6.710189,-0.174113,4.216429,-7.736785,-0.186525,-8.497681,-2.922804,-5.852820,-9.891967,-1.662834,0.080488,-2.461857,-8.048587,-5.050751,-6.691876,3.604501,-0.280192,-5.970346,7.361183,2.292494,3.842480,-8.956837,-9.791337,5.305700,7.004868,-1.273916,0.766760,4.165699,-9.962954,1.548101,-9.749770,-9.140946,-6.248580,5.562402,9.160918,1.975603,-5.977636,2.811799,-0.087383,6.220972,-5.856293,-1.319776,-0.752461,-1.569019,2.865366,8.069987,-0.114478,-7.958323,-4.195884,-1.106208,9.543268,-5.112430,3.332603,-0.722592,-0.310039,6.392904,-5.807874,-0.634853,9.745978,8.300750,-3.048123,-4.098143,-0.836503,1.853543,-7.957596,4.640430,1.223901,4.542662],[1.909083,9.732803,2.836664,-5.513926,-0.449829,-8.741355,2.919875,5.464378,-0.743225,-0.586544,-2.741134,1.069696,2.290580,-5.607131,-9.145066,6.330634,-2.459781,-0.466730,9.099646,2.300392,3.923705,4.246653,2.770427,1.438769,7.054796,0.741660,7.037653,-9.461726,7.650044,-1.066319,4.491448,4.069541,-3.837845,2.232745,-1.290768,2.377208,6.372908,7.339229,3.990507,-1.192109,-1.223912,8.516223,1.358626,9.774346,-8.448634,-8.688633,7.710388,5.066588,4.116759,-8.538617,2.142315,-0.354984,-8.573250,-9.856035,-9.991571,-5.491636,-8.442641,-1.079456,-3.931274,-6.601474,1.636043,-6.228676,-6.450890,-1.953977,-7.267032,9.714116,5.233916,-3.133161,2.277593,1.930626,-9.671110,9.961422,9.564570,-8.943179,0.653392,9.582453,0.855948,4.908371,2.366485,-2.772501,-5.198813,-2.939422,0.004456,-1.196931,4.028966,-9.021180,9.613084,-9.708443,9.325251,-0.969557,4.749305,-7.390932,9.251957,-8.235783,9.162561,7.971652,-3.824021,3.739266,-7.820156,1.952926,-4.329587,3.907123,6.861775,-4.732202,-9.509050,4.422867,-6.491434,4.620065,8.621034,0.698653,-7.143585,9.683918,-6.139490,-3.941453,-1.644146,-1.530931,8.038352,-7.883218,6.282324,8.725232,-5.812313,6.194463,-5.380156,-7.836383,-8.803620,5.717949,-5.711064,0.503796,3.547180,-7.428138,5.339618,-8.217166,-5.260553,7.200494,-1.164925,-5.140766,0.368790,4.796714,-1.202726,-8.208732,5.575498,1.917586,-7.402396,-4.691973,-8.264982,0.665313,7.505872,-9.854071,-5.087180,1.903661,-6.215520,5.989462,9.530734,-5.551671,6.717356,-2.864396,-5.909727,-7.208757,1.033400,-5.637356,5.962799,2.630289,-1.653780,9.743921,-5.897351,0.760732,-6.069588,-1.778912,1.615812,0.374799,6.743427,-3.766099,5.183571,-1.495017,6.708047,-2.469678,-7.162790,-5.563885,4.263351,-6.706612,-2.818553,-8.128794,-5.856983,1.150545,7.152578,-8.941729,-5.045501,-9.521946,-7.381823,-6.544176,-5.832483,-0.331196,8.178928,9.373039,-8.947624,-6.786677]], dtype = "float32")#candidate|5340|(8, 196)|const|float32
bop_5341 = relay.mod(bop_5336.astype('float32'), relay.reshape(const_5340.astype('float32'), relay.shape_of(bop_5336))) # shape=(8, 196)
func_3874_call = mod.get_global_var('func_3874')
func_3875_call = mutated_mod.get_global_var('func_3875')
call_5349 = func_3874_call()
call_5350 = func_3874_call()
output = relay.Tuple([bop_5258,uop_5272,call_5278,const_5279,var_5281,call_5286,const_5287,call_5290,call_5308,var_5309,var_5310,bop_5333,bop_5341,call_5349,])
output2 = relay.Tuple([bop_5258,uop_5272,call_5282,const_5279,var_5281,call_5288,const_5287,call_5292,call_5311,var_5309,var_5310,bop_5333,bop_5341,call_5350,])
func_5351 = relay.Function([var_5256,var_5257,var_5280,var_5281,var_5309,var_5310,var_5332,], output)
mod['func_5351'] = func_5351
mod = relay.transform.InferType()(mod)
mutated_mod['func_5351'] = func_5351
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5351_call = mutated_mod.get_global_var('func_5351')
var_5353 = relay.var("var_5353", dtype = "float64", shape = (5, 6, 3))#candidate|5353|(5, 6, 3)|var|float64
var_5354 = relay.var("var_5354", dtype = "float64", shape = (5, 6, 3))#candidate|5354|(5, 6, 3)|var|float64
var_5355 = relay.var("var_5355", dtype = "int8", shape = ())#candidate|5355|()|var|int8
var_5356 = relay.var("var_5356", dtype = "bool", shape = (896,))#candidate|5356|(896,)|var|bool
var_5357 = relay.var("var_5357", dtype = "int64", shape = (845,))#candidate|5357|(845,)|var|int64
var_5358 = relay.var("var_5358", dtype = "float32", shape = (180,))#candidate|5358|(180,)|var|float32
var_5359 = relay.var("var_5359", dtype = "float64", shape = (8, 196))#candidate|5359|(8, 196)|var|float64
call_5352 = func_5351_call(var_5353,var_5354,var_5355,var_5356,var_5357,var_5358,var_5359,)
output = call_5352
func_5360 = relay.Function([var_5353,var_5354,var_5355,var_5356,var_5357,var_5358,var_5359,], output)
mutated_mod['func_5360'] = func_5360
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4017_call = mod.get_global_var('func_4017')
func_4018_call = mutated_mod.get_global_var('func_4018')
call_5362 = relay.TupleGetItem(func_4017_call(), 0)
call_5363 = relay.TupleGetItem(func_4018_call(), 0)
func_4089_call = mod.get_global_var('func_4089')
func_4091_call = mutated_mod.get_global_var('func_4091')
call_5369 = func_4089_call()
call_5370 = func_4089_call()
output = relay.Tuple([call_5362,call_5369,])
output2 = relay.Tuple([call_5363,call_5370,])
func_5389 = relay.Function([], output)
mod['func_5389'] = func_5389
mod = relay.transform.InferType()(mod)
output = func_5389()
func_5390 = relay.Function([], output)
mutated_mod['func_5390'] = func_5390
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5389_call = mod.get_global_var('func_5389')
func_5390_call = mutated_mod.get_global_var('func_5390')
call_5414 = relay.TupleGetItem(func_5389_call(), 0)
call_5415 = relay.TupleGetItem(func_5390_call(), 0)
func_534_call = mod.get_global_var('func_534')
func_537_call = mutated_mod.get_global_var('func_537')
const_5432 = relay.const([6,3,-3,3,6,-9,6,10,2,8,-3,10,8,-7,3,-2,8,-9,4,-4,-1,-5,5,-4,9,-7,-1,-2,-8,-7,7,-1,7,-5,-3,3,-2,-9,-8,-5,5,1,6,6,2,-6,3,3,7,-2,7,-2,-8,7,6,-2,2,6,1,-2,3,10,-5,-7,1,3,-7,-6,-8,10,2,6,9,2,3,-1,-3,-4,5,1,1,3,-8,2,3,1,-7,-1,-8,4,-10,10,9,-4,-5,10,10,3,-4,6,-8,5,4,2,9,-3,-5,2,7,8,-2,8,-2,8,8,3,2,3,-4,-8,-3,1,6,-1,9,4,6,1,-1,-5,-6,-4,8,2,2,-4,3,-4,9,9,-3,-9,-5,8,-3,4,5,6,7,5,10,-6,-5,1,6,-3,-4,-9,-7,4,1,-9,-10,-2,-7,-10,-8,-9,7,-8,1,-1,6,-6,8,-2,2,5,-10,-10,-4,1,7,5,-1,8,-6,1,-10,4,-6,6,10,9,10,5,2,-8,-10,-4,7,5,4,3,2,1,-6,6,-2,-7,8,8,2,8,8,2,-5,-7,2,10,-1,-4,2,4,8,-6,-5,-4,-10,-6,-4,6,-7,8,-6,5,-1,-4,-8,-7,-10,-3,-9,10,1,10,6,7,-10,3,3,-3,5,-7,4,9,9,8,9,9,-8,7,8,5,7,4,-6,-4,2,5,-7,1,8,-8,-1,-9,8,1,8,-4,6,4,-4,-2,-2,-4,3,7,-7,10,-1,-5,5,-5,-3,-9,-6,10,3,-4,-1,4,-4,-5,7,8,-4,-9,10,3,2,2,-5,5,4,-3,-10,9,9,6,1,3,7,-6,7,-10,-1,6,5,-6,-3,-4,-5,8,8,9,7,5,-6,-1,-10,2,1,9,-9,5,-5,6,3,-3,7,-10,-6,8,-6,6,10,-9,-6,-9,5,-1,-4,-10,1,7,7,-4,-2,6,-3,-6,-2,6,-5,-5,10,1,-2,-10,-6,3,-4,-6,-1,-4,9,-7,-7,9,9,-4,-1,-10,8,8,-7,-7,9,-7,10,-5,3,9,9,6,3,5,-5,-9,-7,8,9,4,9,-6,-3,7,7,10,6,-1,3,5,5,4,-2,-7,-6,-8,-4,-5,9,5,-9,-9,-10,-4,-8,-5,-6,6,-9,-10,6,1,4,7,9,-9,-8,3,-1,-2,-7,-4,4,-10,3,-10,-8,8,-9,5,-8,6,3,5,8,2,4,6,-6,-3,-6,7,-3,8,-10,10,7,6,-7,3,6,-1,-1,-10,-3,5,5,-5,-7,-2,8,-6,10,-7,3,-4,-7,-1,2,-7,-4,8,6,-8,8,1,4,1,9,2,-7,-3,1,-5,5,2,4,-9,-5,5,-8,9,6,-3,7,-9,2,-1,5,-8,9,8,-9,-6,-5,-8,-7,-3,7,8,-3,-8,-8,-10,6,3,-9,1,-9,2,5,-7,7,7,-7,-5,3,-5,-6,-6,-6,-10,-2,-3,-7,5,7,6,9,5,8,6,7,4,10,-10,9,-9,10,-1,9,10,-5,7,10,2,5,-1,1,8,3,8,-7,-2,9,5,-7,-1,1,-10,3,1,4,-10,5,-8,7,10,-3,2,-6,-9,4,-9,9,6,-5,-9,8,4,9,-2,8,-10,-6,2,-9,-7,2,-8,7,-4,-2,1,-2,3,-9,-8,9,-9,-10,9,3,-2,1,-7,-5,-3,5,7,9,1,-7,6,-6,-10,-7,6,4,6,-2,-6,-7,6,-2,-9,4,-10,6,-4,-2,-9,-5,2,4,7,-4,-3,-3,-1,1,-8,8,6,6,8,-6,9,-1,1,1,-1,2,-4,-2,-1,-4,8,5,-8,3,8,-5,1,10,-3,-3,-5,-8,-9,3,3,-9,1,-6,4,7,1,3,-9,-5,3,7,-2,-7,7,-2,-9,-5,4,9,1,2,-7,-3,7,9,5,-9,2,9,-8,-2,-4,7,-8,-8,2,10,-4,-6,-10,-2,-2,3,9,-3,-7,-5,-4,8,1,-1,-5,-4,2,1,-6,9,6,-2,-8,-3,2,3,-4,-7,7,8,7,-1,4,2,-7,-8,5,-9,6,7,1,3,-2,-10,8,-1,10,7,3,3,-2,-4,-2,-1,4,6,7,3,-2,8,-1,-9,10,4,-7,5,10,6,2,-10,-5,-4,-8,2,9,3,1,-2,8,-4,5,-4,-9,-6,-8,-7,-3,-7,-7,-10,-1,8,-5,-2,-8,-7,6,-5,4,3,-8,-6,1,-9,-4,-7,-1,6,-7,10,5,-8,1,-3,7,-8,6,5,7,8,-4,-6,-3,-3,-3,8,2,-6,-1,7,-4,-4,-1,2,2,1,6,-1,4,-3,-6,-2,9,9,-6,10,5,4,1,-6,-5,-9,6,4,-1,-4,8,-5,-3,-6,3,1,-10,-6,9,5,8,-7,-3,6,-7,-3,8,1,2,-2,-5,-7,-8,-7,-4,2,-8,8,-1,-9,7,-3,-10,8,-2,-1,5,-4,-8,9,5,5,2,9,10,-4,-10,3,3,-1,6,-4,9,-2,-8,10,6,-1,1,-4,5,-9,6,4,7,-4,9,-2,5,9,8,-9,7,3,-9,10,-4,1,-10,7,2,10,9,-2,-7,8,-2,-8,-6,-8,7,-8,-6,-10,2,4,1,7,-6,-4,2,6,8,5,-6,-6,-1,-3,1,-3,-3,9,1,-3,7,-9,9,2,-3,9,10,-2,8,-5,-3,4,-7,1,10,-6,1,-7,5,8,-8,7,2,8,7,1,-4,-5,9,-9,-9,-8,-10,-3,-4,-3,7,10,-9,9,2,7,2,-4,-9,-2,8,1,2,-3,4,-9,-7,-8,5,-4,7,2,-3,-2,9,-9,3,7,3,-4,-7,7,1,-10,-5,5,4,-1,6,-7,7,-6,-7,8,2,-8,4,-2,-5,3,-7,-1,-10,7,-6,-2,2,5,-10,1,4,8,-9,5,3,1,8,10,-4,5,1,7,7,5,5,-7,9,9,6,-9,1,8,2,9,-4,10,-2,-1,8,-4,1,-4,-7,-8,6,-3,-7,-8,10,9,-2,1,3,-2,-7,-4,8,-1,-10,9,4,2,-6,2,-8,3,-9,3,-6,3,-9,-4,-4,3,1,9,-5,-9,-1,-10,6,-10,-8,7,6,-9,-8,4,-7,-7,1,8,-6,9,-9,-10,-2,10,-1,-4,-8,4,6,-7,6,-5,-9,-3,9,-4,-10,-5,-3,2,1,-3,-9,-2,-4,1,-2,-7,9,-8,3,-7,8,-7,7,7,5,7,-6,10,10,1,8,-7,-9,3,8,-7,4,-7,3,-8,-3,-4,-6,10,6,1,1,-10,2,-4,-5,-5,9,9,6,-2,-4,10,1,-7,-1,-2,6,-7,-7,-9,4,-3,-5,-4,-2,4,3,6,-3,-2,1,1,5,-4,-8,5,6,-4,-10,6,5,8,3,3,-4,4,-10,-1,-10,-7,9,-10,-2,7,-3,6,4,-9,5,-5,-8,6,-4,2,3,2,-5,-8,9,1,-10,-1,10,-1,3,-5,5,-8,10,2,-3,-7,9,5,1,-9,4,3,-1,2,2,-4,1,-5,3,-4,4,-5,7,10,-10,8,10,-10,8,4,1,7,1,3,-1,-2,-10,-9,-9,-6,-9,-2,8,1,-8,-7,4,-1,6,-3,-2,-4,-2,-9,2,-1,-10,2,-9,-3,8,3,4,9,9,8,6,4,-3,-10,-8,5,-4,-5,10,9,8,9,8,-3,-9,8,1,3,3,-10,-4,9,2,2,-2,9,5,-3,8,-9,6,-4,7,2,3,-3,7,-9,-5,-2,-4,-8,-10,1,8,-7,-5,-3,10,-4,-7,10,-6,4,1,-8,-6,-3,7,4,-6,-10,-4,3,8,5,-4,-9,5,2,9,3,6,4,2,9,-9,-8,1,6,-1,-3,7,5,-9,-10,-7,-6,10,6,-7,9,3,-10,-3,4,-5,-8,10,6,2,-8,8,-4,3,10,7,8,9,6,2,5,-6,-2,10,-8,2,3,-1,8,-7,5,-8,-3,9,-8,-9,10,9,4,10,2,-9,3,10,-5,8,10,-3,2,4,2,-4,-1,-4,2,8,-5,-7,-8,-10,3,-4,-5,-7,6,-6,7,3,-4,-6,1,8,-2,6], dtype = "int8")#candidate|5432|(1568,)|const|int8
call_5431 = relay.TupleGetItem(func_534_call(relay.reshape(const_5432.astype('int8'), [16, 7, 14])), 1)
call_5433 = relay.TupleGetItem(func_537_call(relay.reshape(const_5432.astype('int8'), [16, 7, 14])), 1)
output = relay.Tuple([call_5414,call_5431,const_5432,])
output2 = relay.Tuple([call_5415,call_5433,const_5432,])
func_5443 = relay.Function([], output)
mod['func_5443'] = func_5443
mod = relay.transform.InferType()(mod)
mutated_mod['func_5443'] = func_5443
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5443_call = mutated_mod.get_global_var('func_5443')
call_5444 = func_5443_call()
output = call_5444
func_5445 = relay.Function([], output)
mutated_mod['func_5445'] = func_5445
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5240_call = mod.get_global_var('func_5240')
func_5242_call = mutated_mod.get_global_var('func_5242')
call_5602 = relay.TupleGetItem(func_5240_call(), 0)
call_5603 = relay.TupleGetItem(func_5242_call(), 0)
uop_5616 = relay.acosh(call_5602.astype('float32')) # shape=(11, 14, 12)
uop_5618 = relay.acosh(call_5603.astype('float32')) # shape=(11, 14, 12)
output = uop_5616
output2 = uop_5618
func_5625 = relay.Function([], output)
mod['func_5625'] = func_5625
mod = relay.transform.InferType()(mod)
mutated_mod['func_5625'] = func_5625
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5625_call = mutated_mod.get_global_var('func_5625')
call_5626 = func_5625_call()
output = call_5626
func_5627 = relay.Function([], output)
mutated_mod['func_5627'] = func_5627
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4017_call = mod.get_global_var('func_4017')
func_4018_call = mutated_mod.get_global_var('func_4018')
call_5630 = relay.TupleGetItem(func_4017_call(), 0)
call_5631 = relay.TupleGetItem(func_4018_call(), 0)
func_5171_call = mod.get_global_var('func_5171')
func_5173_call = mutated_mod.get_global_var('func_5173')
var_5635 = relay.var("var_5635", dtype = "int8", shape = (1568,))#candidate|5635|(1568,)|var|int8
call_5634 = relay.TupleGetItem(func_5171_call(relay.reshape(var_5635.astype('int8'), [1, 1568])), 0)
call_5636 = relay.TupleGetItem(func_5173_call(relay.reshape(var_5635.astype('int8'), [1, 1568])), 0)
func_3344_call = mod.get_global_var('func_3344')
func_3347_call = mutated_mod.get_global_var('func_3347')
const_5641 = relay.const(7, dtype = "uint16")#candidate|5641|()|const|uint16
call_5640 = relay.TupleGetItem(func_3344_call(relay.reshape(const_5641.astype('uint16'), [])), 0)
call_5642 = relay.TupleGetItem(func_3347_call(relay.reshape(const_5641.astype('uint16'), [])), 0)
func_5249_call = mod.get_global_var('func_5249')
func_5251_call = mutated_mod.get_global_var('func_5251')
call_5646 = func_5249_call()
call_5647 = func_5249_call()
uop_5651 = relay.rsqrt(call_5646.astype('float64')) # shape=(11, 14, 12)
uop_5653 = relay.rsqrt(call_5647.astype('float64')) # shape=(11, 14, 12)
var_5666 = relay.var("var_5666", dtype = "float64", shape = (11, 14, 12))#candidate|5666|(11, 14, 12)|var|float64
bop_5667 = relay.greater_equal(uop_5651.astype('bool'), relay.reshape(var_5666.astype('bool'), relay.shape_of(uop_5651))) # shape=(11, 14, 12)
bop_5670 = relay.greater_equal(uop_5653.astype('bool'), relay.reshape(var_5666.astype('bool'), relay.shape_of(uop_5653))) # shape=(11, 14, 12)
output = relay.Tuple([call_5630,call_5634,var_5635,call_5640,const_5641,bop_5667,])
output2 = relay.Tuple([call_5631,call_5636,var_5635,call_5642,const_5641,bop_5670,])
func_5671 = relay.Function([var_5635,var_5666,], output)
mod['func_5671'] = func_5671
mod = relay.transform.InferType()(mod)
var_5672 = relay.var("var_5672", dtype = "int8", shape = (1568,))#candidate|5672|(1568,)|var|int8
var_5673 = relay.var("var_5673", dtype = "float64", shape = (11, 14, 12))#candidate|5673|(11, 14, 12)|var|float64
output = func_5671(var_5672,var_5673,)
func_5674 = relay.Function([var_5672,var_5673,], output)
mutated_mod['func_5674'] = func_5674
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4089_call = mod.get_global_var('func_4089')
func_4091_call = mutated_mod.get_global_var('func_4091')
call_5710 = func_4089_call()
call_5711 = func_4089_call()
func_5249_call = mod.get_global_var('func_5249')
func_5251_call = mutated_mod.get_global_var('func_5251')
call_5724 = func_5249_call()
call_5725 = func_5249_call()
bop_5727 = relay.maximum(call_5710.astype('float32'), relay.reshape(call_5724.astype('float32'), relay.shape_of(call_5710))) # shape=(11, 14, 12)
bop_5730 = relay.maximum(call_5711.astype('float32'), relay.reshape(call_5725.astype('float32'), relay.shape_of(call_5711))) # shape=(11, 14, 12)
output = relay.Tuple([bop_5727,])
output2 = relay.Tuple([bop_5730,])
func_5732 = relay.Function([], output)
mod['func_5732'] = func_5732
mod = relay.transform.InferType()(mod)
output = func_5732()
func_5733 = relay.Function([], output)
mutated_mod['func_5733'] = func_5733
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4925_call = mod.get_global_var('func_4925')
func_4926_call = mutated_mod.get_global_var('func_4926')
call_5743 = func_4925_call()
call_5744 = func_4925_call()
func_3230_call = mod.get_global_var('func_3230')
func_3234_call = mutated_mod.get_global_var('func_3234')
const_5768 = relay.const([-0.410421,-8.127037,-6.297178,-7.607508,2.721209,6.823787,8.799575,-1.309764,-3.836585,4.017035,-0.263382,-7.215852,-6.573305,-8.660110,-0.083548,-7.563925,-8.575107,-5.561643,-9.667040,9.609087,6.029904,-7.022323,-1.258526,4.817821,9.217703,3.896678,-9.256535,5.694191,-4.040410,-0.370559,2.160214,9.773762,9.635359,4.734582,-7.418760,9.543371,0.512222,-3.669081,8.078600,-1.939092,-3.931691,-1.596029,-5.151424,-4.101583,4.517920,0.913846,9.413202,0.033314,-7.985115,-9.566098,5.801948,-0.128352,7.185433,-1.522065,4.726345,3.763435,3.705518,-8.664541,9.138625,-8.640329,0.583612,-6.971995,9.779091,6.082052,-2.053663,-8.159067,-0.002626,-0.703794,-8.770561,-7.668131,-7.293352,5.141715,2.729286,4.257583,-0.303148,-3.828517,3.098880,-1.982211,-0.351314,-4.251138,8.865723,-9.971159,6.519086,5.294880,-8.259176,7.252987,-0.300714,-8.099924,-9.346345,-8.512080,8.628347,-6.662377,0.457111,6.047519,3.500604,-8.896919,2.504703,-5.270460,-7.339702,-3.981162,1.955456,4.902442,-3.357845,1.002477,3.326880,-6.407496,-0.566325,5.284567,7.450378,7.356541,-4.767610,-0.489677,4.588970,-2.238143,-6.198886,-7.257543,7.690170,9.101730,6.856111,-3.106297,9.227484,0.458640,-6.886135,4.827237,-8.837487,-7.385019,4.955123,-5.902965,5.713295,-6.299619,3.152491,5.950096,-1.331095,-0.309623,3.516146,-1.509602,0.555765,7.066684,-9.490921,-3.016911,8.133063,2.248121,2.556926,0.219799,-1.483003,-8.523237,-6.117905,-5.603895,1.435505,-4.075669,-6.723398,3.701143,2.138336,3.347447,2.009874,-2.760531,-1.404974,6.427590,4.911324,-6.544754,-1.968315,4.657366,-9.681322,9.812650,-7.335989,-9.137233,-4.590715,0.973422,-7.005819,9.826966,-0.122721,0.068649,1.691961,-7.279000,8.866768,5.838472,7.318602,8.229498,-9.891367,6.007060,-2.640200,6.656865,1.317532,-2.871094,9.957189,-3.225434,9.864996,-2.763325,-3.107499,7.385266,8.934940,-1.435943,6.172407,-9.445735,-7.536069,7.641285,-0.733553,-0.275405,9.062506,7.836814,-8.324469,-8.248209,1.237911,0.354744,3.120697,-6.862288,8.101618,3.531066,-0.928356,-9.601588,-0.746981,0.956628,3.499436,-5.684094,2.380567,0.620159,2.015925,0.930556,5.753073,5.615467,-9.584019,8.493343,-7.899197,-8.247476,1.052800,0.503178,-6.102928,-0.940428,-6.484812,-0.235705,-0.943561,-2.863112,8.755870,6.817468,-4.136247,8.416386,-2.415594,-5.292646,-6.338246,9.837703,1.184533,7.768521,2.578740,7.015875,-6.290090,0.332185,-3.556315,8.163615,-1.534321,-1.553578,8.886403,9.448775,-0.950837,-7.285472,-3.176919,-3.657686,-4.042279,-9.509385,4.702791,-6.046663,7.713076,0.595549,4.221486,-7.664891,2.644546,-5.939222,-5.339073,-4.220257,0.227023,3.384018,-9.966702,0.378125,4.003643,-0.255602,-9.601894,7.384031,4.829334,3.145603,3.257965,-9.570426,-0.729768,3.806742,-7.220518,9.954219,-5.824253,9.584866,6.853671,9.831351,-3.037880,7.431583,-7.385341,1.591687,2.470771,-1.675724,-9.384204,9.650562,2.865489,7.500707,-4.592316,6.848603,-7.424479,1.526868,-3.846813,-8.466474,6.274855,9.316661,-5.698008,2.502503,5.668956,-6.913909,-2.255603,-0.075622,-3.037483,8.360201,-1.882683,0.473679,8.424252,-3.354390,-8.876743,2.136627,2.401061,2.617118,3.297066,7.994869,2.549672,-9.395882,-9.211648,3.445184,-0.963933,0.401749,-3.029920,8.837871,-9.473299,7.002572,7.885536,-8.011865,5.883416,-8.092314,-9.233645,0.322754,-9.544754,5.083375,-5.250748,7.767836,2.597931,6.798872,-8.036897,7.946788,3.973957,8.044191,8.517483,6.037005,6.651790,7.722432,2.578750,4.242555,-9.229457,-5.793890,-2.326485,-3.533927,8.275994,7.286510,-9.333544,-1.392347,6.458442,-9.981143,1.706658,9.518282,-4.953588,-7.689413,0.832486,2.764100,-9.944127,-8.341440,0.300788,-8.594800,-5.325036,-9.816030,-1.654123,-4.876405,-4.405071,9.267431,-1.665136,7.279468,3.621981,9.608052,9.693710,8.989991,-7.231583,-9.835522,-4.658378,-9.104050,-4.158229,5.838919,5.204681,-4.321072,2.822385,3.974628,-7.859917,-3.285136,-9.100899,-4.658376,-3.480419,2.416494,7.955297,-3.848926,-2.831989,8.463643,-2.549630,-5.149398,-8.251539,7.836730,-8.002908,-5.859042,0.866526,-6.208247,-4.636165,-1.045890,-8.791321,8.159232,9.895593,2.169626,1.384928,5.706486,-2.378243,6.593863,-4.819761,-1.697905,-4.989455,-6.190516,2.839124,3.002125,2.400656,-3.591146,-6.339326,-9.435203,6.172985,9.519598,-3.881994,-7.122774,-8.841964,3.772474,7.065843,1.537521,-8.927211,3.466713,0.011774,3.508924,-0.177021,-9.906447,-8.146158,9.516853,5.442674,-3.668151,5.187720,-1.892944,-9.547994,-8.263732,8.913892,3.995213,4.691337,6.495582,-4.774734,-9.064882,-2.032374,5.597203,1.733306,-7.592611,6.908976,-8.047995,-0.745437,4.622793,-9.194227,-7.813145,4.308364,-1.112933,-6.978775,8.252177,-6.562619,-5.970445], dtype = "float64")#candidate|5768|(480,)|const|float64
const_5769 = relay.const([2,-10,-2,-3,-2,6,3,7,-2,6,6,-8,-4,-3,5,-10,-1,-9,1,-1,-6,-5,8,6,8,10,8,9,4,-2,-5,9,3,8,-10,8,-7,-7,-7,-4,5,-9,4,8,-9,9,3,3,-6,1,-1,1,6,-6,3,5,6,2,3,7,10,-9,4,10,-2,-5,4,4,8,-10,-10,10,1,3,1,6,-6,6,-7,-9,7,-4,1,-10,6,9,-5,1,10,9,-5,-5,-10,-2,-7,-5,-6,7,7,-8,7,10,-8,-9,-6,-10,-3,-6,5,-1,-1,-9,5,8,-3,-4,6,6,4,2,4,-5,-8,4,-10,-8,-1,-2,2,8,-6,10,6,-8,1,-2,-2,6,9,7,-6,10,1,6,2,3,-6,-2,8,3,-9,-6,2,-5,3,10,-7,7,-2,3,6,-2,8,-3,3,6,10,5,6,-3,-1,10,-3,4,-9,9,-5,-6,-6,-9,-6,3,9,-10,-9,7,7,-6,2,8,-8,-7,-10,6,-5,-5,2,-8,7,9,10,3,-1,10,8,-7,4,1,-10,-8,-4,5,-2,-8,-1,-2,-2,8,6,7,5,2,9,-1,-8,3,3,-7,-2,-3,-3,4,2,9,2,-1,1,6,7,-10,-8,7,2,8,1,7,-8,9,6,9,-3,5,-6,-3,-10,-7,7,-2,2,-3,3,6,4,3,-3,-6,-5,-10,3,3,8,2,6,4,-7,-10,10,4,-3,-2,9,3,-10,-4,-8,-6,7,-2,5,-8,5,-3,-3,-7,-3,-3,8,6,-10,-2,-7,5,-8,6,4,-6,-9,-4,-7,9,3,-4,-9,-10,3,7,10,-4,10,-4,4,-5,-10,-5,3,8,-7,6,3,5,10,7,-4,10,1,-8,3,-7,-4,9,10,3,10,-3,7,-10,-10,7,-8,-5,1,3,9,-5,4,-2,3,-2,-7,7,-5,-9,6,8,-2,-4,-8,-7,8,-4,7,-9,-3,3,-7,2,-9,-8,8,8,9,-7,8,-6,7,9,7,-6,10,-10,2,-1,-4,6,3,6,-8,10,6,-4,-5,-6,-2,3,-4,7,5,-6,6,-3,-10,2,-1,-5,6,9,-2,-6,-9,-4,-9,8,-10,-5,8,7,8,-5,-2,7,10,1,-2,4,-5,-2,-3,10,-5,-2,-4,3,8,2,-8,8,-4,-10,6,-8,4,5,10,-1,-10,-10,-1,6,-10,-7,-7,8,6,8,4,2,5,7,3,-4,10,5,6,-1,2,-7,-7,-10,5,-4,5,-8,3,10,3,9,8,7,7,-2,-9,6,8,-8,8,-3,-6,-7,-4,7,1,-3,9,-4,-1,5,-7,-6,1,-7,4,3,-1,-10,-7,4,-2,6,-10,-10,-9,1,-8,-1,10,7,10,-5,10,7,4,-5,10,-10,4,-3,4,8,-10,-8,-9,-4,5,-1,7,-4,9,9,-3,-4,-10,-1,-9,-6,-10,-1,1,9,5,3,-7,-4,6,-8,4,-7,8,-1,-7,-8,-3,-5,4,-4,-3,4,-4,6,4,3,7,4,-8,-4,4,-3,1,-3,3,8,6,3,10,2,-3,-6,4,6,7,-10,-2,-7,-10,-9,-10,8,9,-6,1,5,-4,6,10,-2,2,7,-5,-6,-7,-10,4,-10,9,1,5,-6,8,-7,-4,7,-10,-9,-1,10,9,-4,7,-5,-2,-8,6,-8,-6,5,3,-7,8,-8,8,-6,9,2,-6,4,-5,8,6,6,-10,-3,2,-6,5,-9,3,2,7,-9,10,4,-4,7,-8,-4,-1,-1,-9,3,-2,-5,-8,-8,10,8,1,-7,4,-6,6,-9,9,2,-9,-9,7,-8,2,10,5,4,-1,2,-7,-8,-10,-4,8,-6,2,10,1,6,5,-7,-7,-8,-4,-6,1,-7,-10,2,8,-7,-5,-4,4,-10,-10,-9,8,5,-10,-4,-4,3,-4,4,-3,6,7,-4,10,7,-1,-6,6,2,2,-8,-8,2,6,-6,6,-6,-2,3,-6,-3,-9,-5,-10,-2,2,-1,-10,4,1,-4,-2,10,-3,-7,5,6,-6,-2,10,1,5,4,-8,-1,8,6,8,-3,10,1,-7,1,10,2,-7,-3,8,8,-6,3,-6,4,-6,6,7,9,-8,9,-4,-9,-7,-3,-10,3,2,9,-6,4,2,-5,-1,4,7,-9,-6,1,-1,-10,-7,-8,-8,9,-10,3,-4,10,5,5,7,2,-2,-9,-9,-5,-2], dtype = "int64")#candidate|5769|(845,)|const|int64
const_5770 = relay.const([-7.773603,3.066143,-1.505297,1.275278,-0.020382,-3.489190,7.124679,-3.737404,6.673935,-4.764751,-5.264331,6.816091,-3.612964,-8.908965,3.714779,5.162221,-4.843904,-9.192738,9.418326,-0.302608,-1.481785,1.144502,7.318125,-9.308940,-8.905432,-5.252725,9.533497,2.214740,2.323988,-6.729489,-5.860525,-3.284060,-8.840325,7.977076,-5.294529,-4.985521,-5.444633,-4.621056,9.801894,5.741591,5.561538,-3.545599,3.761840,4.115444,6.953997,-4.302194,3.762323,-0.246276,1.778384,6.346309,6.468066,-9.420478,6.119389,-3.936070,-0.800223,-4.005909,8.081027,-8.984650,4.009161,5.087596,3.694248,-6.071249,0.969175,4.502238,-1.732063,-8.629075,-7.807126,9.658677,-2.805185,-4.171773,4.451372,-2.804049,3.166553,-7.697134,-5.064222,9.825799,3.654270,-5.817851,-8.105419,2.139959,-7.014833,3.105664,0.139692,-5.522187,-1.089775,-3.860750,-2.910775,-7.275940,6.377449,-5.513060,-4.202981,-5.411028,8.587689,-7.065103,-6.553478,-6.299050,-0.251010,5.918410,-5.445703,4.259464,-9.714094,6.673973,-9.785092,-0.629441,-2.524329,-1.550724,-7.912632,-9.758981,8.013576,4.131242,-8.523419,3.719219,3.590288,-2.463313,-1.764954,-5.160643,6.208999,6.115498,5.652730,-7.267067,-6.828720,4.816023,2.949686,-1.824130,-1.955729,-7.895390,9.233111,4.404156,-6.157237,8.031863,0.050574,3.567887,5.542897,3.153516,-6.630727,-0.462902,-0.522309,3.895155,4.969965,-9.908694,3.539751,-2.218384,-8.560510,-1.468994,-8.889897,-6.323047,9.104146,-2.268126,-3.815082,-9.569641,2.664111,-8.069816,-3.963368,2.584413,2.056148,1.721138,-7.443580,-7.447334,-1.182174,6.937987,-5.615862,-8.034154,0.032143,-3.926348,-8.530900,-6.926416,1.098841,2.546837,-3.359210,8.425741,9.165302,1.483948,-4.778195,-9.698789,-2.643947,0.274699,1.284997,-5.486009,9.002001,6.912010], dtype = "float32")#candidate|5770|(180,)|const|float32
call_5767 = relay.TupleGetItem(func_3230_call(relay.reshape(const_5768.astype('float64'), [15, 2, 16]), relay.reshape(const_5769.astype('int64'), [845,]), relay.reshape(const_5770.astype('float32'), [180,]), ), 0)
call_5771 = relay.TupleGetItem(func_3234_call(relay.reshape(const_5768.astype('float64'), [15, 2, 16]), relay.reshape(const_5769.astype('int64'), [845,]), relay.reshape(const_5770.astype('float32'), [180,]), ), 0)
func_690_call = mod.get_global_var('func_690')
func_695_call = mutated_mod.get_global_var('func_695')
const_5785 = relay.const([-9,10,3,-3,3,-4,2,5,-5,-9,-2,4,-8,-3,10,-8,8,-2,-9,-5,-1,-7,1,10,6,2,-2,7,3,-3,-7,1,-2,-6,9,3,-2,-2,-4,-8,-10,6,7,1,5,-4,-6,10,9,1,9,8,4,-4,-2,1,-5,5,-2,3], dtype = "uint32")#candidate|5785|(60,)|const|uint32
var_5786 = relay.var("var_5786", dtype = "bool", shape = (28, 32))#candidate|5786|(28, 32)|var|bool
const_5787 = relay.const([8,-7,-9,-1,-8,5,-7,4,-1,7,-2,-2,-8,1,5,-1,-3,-10,-7,-7,9,-6,-1,4,-1,9,10,6,8,-8,-1,-5,-9,5,7,-8,-6,-3,-7,2,-8,1,4,3,-5,4,10,-10,-6,5,-9,-2,-9,5,-3,-4,-9,8,2,-7,4,5,-3,-3,10,-2,10,7,10,5,-10,-4,-2,4,6,3,7,4,-2,8,-2,2,-6,-1,-2,8,3,-9,-6,1,6,-4,3,-2,-2,9,-3,-7,-2,3,-3,4,-7,-5,7,7,-1,6,-6,10,-1,3,10,10,8,-5,-6,-1,5,-6,-1,8,3,-7,-4,-8,-6,8,-2,-1,4,3,7,3,-7,4,3,3,8,4,9,-7,-4,4,-5,-6,2,-9,1,-1,-4,-10,9,-2,5,10,-9,-10,4,-8,-8,-8,-2,-9,2,5,9,4,9,6,3,8,3,-6,4,7,-8,4,3,-5,7,2,3,3,-3,8,7,1,-5,-8,-1,-1,-2,-9,10,4,3,-1,-2,-10,7,3,1,-5,-1,5,10,2,-3,-8,4,8,6,4,8,-6,-10,-9,3,9,-9,-5,-2,-10,8,8,8,1,-9,-5,-9,-4,-10,-1,-8,-6,-7,-3,-9,-6,1,-1,3,-4,-7,1,-7,-6,-9,9,-7,2,7,-5,-10,-5,6,-9,-8,-3,-1,-2,1,-7,-4,6,3,-7,5,9,4,8,10,3,10,6,2,10,-5,-2,5,-2,7,-1,3,2,3,-1,7,2,2,9,-5,5,-7,-1,-8,3,4,10,3,7,1,-9,-4,6,-9,7,-5,6,-3,4,-1,7,-10,-3,10,-1,9,-9,-10,-8,1,5,-2,-8,9,6,-1,-5,9,-6,-9,-10,-6,3,6,-7,9,-1,-4,-3,2,-4,2,6,9,-2,10,7,3,-1,1,5,1,-10,6,-9,3,-3,-3,8,-4,10,-4,-7,-9,5,-8,2,6,-4,5,3,7,5,-7,-3,5,3,10,-8,10,-1,-6,10,2,4,-9,7,3,7,-7,10,-4,1,5,-5,3,-5,-6,10,-1,7,-3,10,-8,-7,9,-7,2,-7,9,4,-7,-10,-6,-2,7,10,6,8,-7,1,4,-9,7,-1,-9,8,-6,10,1,10,5,-1,-10,-7,6,2,-5,4,8,-10,-2,4,9,9,-8,-1,9,-4,-1,-5,-8,-6,-10,8,-10,7,-9,2,-9,-9,2,-9,-1,9,5,-2,-2,9,3,-2,-6,-6,1,2,-1,-8,2,-5,2,9,-1,-2,9,5,-1,-4,-7,1,-10,-10,7,-5,5,3,5,7,-3,7,2,-6,2,-1,10,-8,8,-1,-8,-3,-6,10,-8,-5,8,5,-7,-5,10,-7,8,1,5,-1,10,-6,10,-8,-5,-9,9,4,-4,-5,5,-5,9,-10,-1,7,-5,-8,9,3,-10,-4,8,-3,7,9,9,-6,1,3,7,3,-1,4,8,-1,-2,5,4,-2,-7,-4,4,-7,6,-9,9,2,5,-9,5,-9,-8,-7,-4,5,2,10,-9,-3,6,-5,-3,5,5,1,8,7,4,-8,4,10,3,4,-6,5,10,-6,-9,3,7,-3,1,8,-3,4,2,-5,-5,-6,-7,-2,3,10,-1,5,4,-2,6,-2,8,10,1,4,-6,6,3,10,8,-7,4,4,10,5,-5,6,-5,5,2,2,2,-1,8,3,3,4,2,5,3,7,-7,3,-9,-9,-8,1,1,-4,-3,-6,7,-4,-7,2,-9,9,-1,-9,1,-5,1,8,8,-2,1,9,-7,8,2,-5,6,-8,-6,-1,-6,-7,-2,8,9,5,7,9,-9,-9,4,3,-8,10,1,-3,8,4,5,4,-2,-7,4,-5,10,5,10,5,-10,-3,8,8,6,-8,5,-8,-2,8,-8,1,10,3,6,9,-4,-9,-8,8,10,-6,9,-2,8,9,4,5,7,-6,-7,3,5,4,8,9,8,-2,1,10,-7,-5,-8,-7,-8,2,-5,-7,-4,8,-2,1,-4,9,-1,7,5,-9,2,-1,-8,-6,-5,-5,-3,-4,-10,5,10,-1,2,-8,-10,1,4,4,3,7,4,-9,-7,-4,-8,2,4,10,1,-2,-7,-5,-4,-5,1,-7,5,6,10,10,-8,7,-6,-9,-5,10,-5,-4,-3,8,-10,3,-2,9,6,2,-4,9,8,-8,8,-6,2,1,-9,-1,5,-8,2,1,-9,-3,5,-2,7,-7,-10,7,-5,9,-9,-4,-4,-1,10,-4,6,1,-9,-4,4,3,-4,-6,-1,2,-5,4,9,-6,7,7,7,-5,-2,5,10,-10,6,-3,10,9,-4,-3,-8,1,10,1,7,-6,-4,-6,6,-9,1,1,9,-5,3,-5,8,6,-5,5,-2,-10,-1,1,2,2,-1,-5,3,3,-9,-6,-4,6,1,1,4,2,-8,3,-10,-5,7,1,-1,5,3,-10,-4,-6,10,10,9,-1,4,8,10,7,3,-9,-2,-6,-8,2,3,-8,-5,8,2,-10,-5,10,-2,-3,5,-1,6,2,6,-5,3,-3,-4,2,-10,10,-3,-1,1,1,-5,3,-4,5,-2,-8,-6,3,1,3,10,-7,8,-9,1,5,4,5,-6,7,-3,-10,5,-8,-1,-10,-6,3,4,-3,3,8,7,-5,-6,-10,7,-9,-5,1,-7,6,-7,-9,2,5,-3,5,8,2,2,4,-4,-4,-7,-5,-7,10,-2,4,-5,3,1,8,6,3,4,1,-8,4,-1,4,10,1,-4,-9,-1,-7,-8,2,-6,6,-2,-5,4,-10,10,3,7,-3,-7,2,-5,-2,7,-9,-1,-3,3,-5,-9,10,-6,-1,-8,-6,9,5,-10,-8,-3,9,3,-6,2,-1,-4,-2,5,5,-10,-10,-2,2,4,-10,7,10,3,-8,5,8,2,2,-3,-3,-2,1,-8,6,1,8,5,-1,1,-3,-7,-8,1,8,-8,9,2,4,3,1,-5,-5,6,-1,3,5,-5,1,-2,-1,10,10,2,-1,3,-8,-2,1,8,6,5,3,4,-5,-3,-9,-8,4,-5,4,8,8,-6,-7,-10,8,-4,-3,-5,7,7,-2,6,-7,-4,9,-5,-3,4,9,-2,-9,-8,-7,3,4,9,-6,-3,-6,-6,-8,-9,-3,-10,9,9,-10,-10,-1,-10,-4,-2,-6,3,-1,-6,-9,-1,-10,-9,5,-6,-5,4,3,3,-5,-6,-10,-10,10,-2,-2,3,4,-10,-10,-3,-7,4,-1,7,-2,6,4,4,3,-2,9,-7,-9,-1,5,7,3,4,-6,1,-4,1,4,-3,-9,1,2,2,-5,2,9,4,1,-7,8,7,6,1,1,-6,-9,-2,-3,4,-5,9,-8,-7,2,-5,3,-6,10,-8,1,5,1,3,-10,-3,7,-1,7,-3,-4,-3,10,6,7,3,8,-10,-5,-2,-3,-2,-8,-5,-2,8,-7,-3,-2,-9,10,9,-3,-6,3,5,-6,-4,1,3,-8,-1,4,3,10,-3,7,-10,-10,-9,8,-8,-1,1,4,7,-3,-8,-2,-2,-3,7,-6,10,-5,10,-1,10,-3,-5,-2,-8,1,-3,6,-7,10,-1,-1,4,-10,-1,-5,2,-1,6,1,8,9,-7,7,-6,-8,-3,7,-6,6,-5,-10,10,8,-3,-9,9,4,-2,9,-10,-4,7,2,6,3,-10,2,2,-5,7,10,3,3,7,-5,1,9,1,-3,1,10,-7,-3,-4,-8,2,8,-1,3,5,2,7,5,-5,7,-4,-9,-1,2,9,-6,-7,8,-7,4,9,1,-9,4,-5,-10,-9,-10,9,4,1,3,-6,5,-2,-7,-5,8,5,8,4,8,6,2,9,5,9,9,-9,-1,1,3,-6,-2,5,-2,-9,-2,8,10,3,-9,-5,10,-3,6,-8,-2,2,-7,5,7,10,8,-5,-5,-6,-3,-3,5,-3,-9,-10,7,-6,-8,-6,4,-6,1,-3,-2,-1,1,9,7,7,-6,7,-10,10,6,4,-1,2,-2,2,-5,-2,-6,-2,-4,9,5,-5,-2,2,-2,-6,7,-9,-7,4,2,6,-6,3,7,-1,-9,-7,1,9,-8,-8,-4,-3,-6,3,-2,9,9,-7,3,9,4], dtype = "int8")#candidate|5787|(1568,)|const|int8
call_5784 = relay.TupleGetItem(func_690_call(relay.reshape(const_5785.astype('uint32'), [2, 2, 15]), relay.reshape(const_5770.astype('float32'), [180,]), relay.reshape(var_5786.astype('bool'), [896,]), relay.reshape(const_5787.astype('int8'), [1568,]), ), 4)
call_5788 = relay.TupleGetItem(func_695_call(relay.reshape(const_5785.astype('uint32'), [2, 2, 15]), relay.reshape(const_5770.astype('float32'), [180,]), relay.reshape(var_5786.astype('bool'), [896,]), relay.reshape(const_5787.astype('int8'), [1568,]), ), 4)
output = relay.Tuple([call_5743,call_5767,const_5768,const_5769,const_5770,call_5784,const_5785,var_5786,const_5787,])
output2 = relay.Tuple([call_5744,call_5771,const_5768,const_5769,const_5770,call_5788,const_5785,var_5786,const_5787,])
func_5799 = relay.Function([var_5786,], output)
mod['func_5799'] = func_5799
mod = relay.transform.InferType()(mod)
var_5800 = relay.var("var_5800", dtype = "bool", shape = (28, 32))#candidate|5800|(28, 32)|var|bool
output = func_5799(var_5800)
func_5801 = relay.Function([var_5800], output)
mutated_mod['func_5801'] = func_5801
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5867 = relay.var("var_5867", dtype = "uint16", shape = (15, 14, 10))#candidate|5867|(15, 14, 10)|var|uint16
var_5868 = relay.var("var_5868", dtype = "uint16", shape = (15, 14, 10))#candidate|5868|(15, 14, 10)|var|uint16
bop_5869 = relay.equal(var_5867.astype('bool'), relay.reshape(var_5868.astype('bool'), relay.shape_of(var_5867))) # shape=(15, 14, 10)
output = bop_5869
output2 = bop_5869
func_5878 = relay.Function([var_5867,var_5868,], output)
mod['func_5878'] = func_5878
mod = relay.transform.InferType()(mod)
mutated_mod['func_5878'] = func_5878
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5878_call = mutated_mod.get_global_var('func_5878')
var_5880 = relay.var("var_5880", dtype = "uint16", shape = (15, 14, 10))#candidate|5880|(15, 14, 10)|var|uint16
var_5881 = relay.var("var_5881", dtype = "uint16", shape = (15, 14, 10))#candidate|5881|(15, 14, 10)|var|uint16
call_5879 = func_5878_call(var_5880,var_5881,)
output = call_5879
func_5882 = relay.Function([var_5880,var_5881,], output)
mutated_mod['func_5882'] = func_5882
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3874_call = mod.get_global_var('func_3874')
func_3875_call = mutated_mod.get_global_var('func_3875')
call_5897 = func_3874_call()
call_5898 = func_3874_call()
output = relay.Tuple([call_5897,])
output2 = relay.Tuple([call_5898,])
func_5900 = relay.Function([], output)
mod['func_5900'] = func_5900
mod = relay.transform.InferType()(mod)
output = func_5900()
func_5901 = relay.Function([], output)
mutated_mod['func_5901'] = func_5901
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4800_call = mod.get_global_var('func_4800')
func_4802_call = mutated_mod.get_global_var('func_4802')
call_5958 = func_4800_call()
call_5959 = func_4800_call()
func_4017_call = mod.get_global_var('func_4017')
func_4018_call = mutated_mod.get_global_var('func_4018')
call_5986 = relay.TupleGetItem(func_4017_call(), 0)
call_5987 = relay.TupleGetItem(func_4018_call(), 0)
output = relay.Tuple([call_5958,call_5986,])
output2 = relay.Tuple([call_5959,call_5987,])
func_5992 = relay.Function([], output)
mod['func_5992'] = func_5992
mod = relay.transform.InferType()(mod)
output = func_5992()
func_5993 = relay.Function([], output)
mutated_mod['func_5993'] = func_5993
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5625_call = mod.get_global_var('func_5625')
func_5627_call = mutated_mod.get_global_var('func_5627')
call_5994 = func_5625_call()
call_5995 = func_5625_call()
output = relay.Tuple([call_5994,])
output2 = relay.Tuple([call_5995,])
func_5997 = relay.Function([], output)
mod['func_5997'] = func_5997
mod = relay.transform.InferType()(mod)
mutated_mod['func_5997'] = func_5997
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5997_call = mutated_mod.get_global_var('func_5997')
call_5998 = func_5997_call()
output = call_5998
func_5999 = relay.Function([], output)
mutated_mod['func_5999'] = func_5999
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4017_call = mod.get_global_var('func_4017')
func_4018_call = mutated_mod.get_global_var('func_4018')
call_6006 = relay.TupleGetItem(func_4017_call(), 0)
call_6007 = relay.TupleGetItem(func_4018_call(), 0)
const_6008 = relay.const([[[9.969667,-6.286434,9.022036,-3.050611,7.008111,-2.958656,-1.249538,3.360128,-7.391382,-9.410562,-2.094585,-6.398395],[1.534685,-9.889380,-6.761174,4.552147,3.479469,-1.105292,8.690382,-4.769787,1.828759,8.162271,-5.666216,-8.131466],[-6.554343,5.629809,4.334823,-4.894366,-1.705451,-1.474023,8.196262,-0.772873,4.595729,3.354293,-9.206431,0.220286],[-0.416633,7.765891,-9.152381,1.439480,-4.301689,1.158955,-7.988987,-0.617427,2.465788,3.547481,-5.424834,0.892083],[-0.809142,7.202217,-4.225302,7.521029,6.539326,4.007019,-6.288027,-8.172100,0.548398,6.185769,8.550264,3.434640],[-1.801359,1.875194,-5.186496,-5.958270,-7.305718,6.296020,-2.068373,9.063330,2.331932,6.149367,-8.742239,-5.057730],[-1.035533,2.716304,-2.218587,-2.269466,-4.315622,9.174788,-1.783628,7.529089,9.556470,4.112244,0.685921,6.761361],[-4.501505,9.975522,-9.683281,-3.502193,5.992401,8.727636,-8.129738,-9.193707,1.089944,-9.278916,8.850277,-9.101468],[-8.341145,-0.149324,7.440912,8.928564,0.746009,-4.078495,-3.969971,-7.762096,-6.076439,2.163119,4.208901,8.227418],[-0.165667,-1.753337,-1.808500,-2.022339,-0.397029,-7.819087,7.313280,4.525682,-1.611697,-2.546878,8.107615,-3.256059],[-8.570732,-9.679242,2.888480,9.046541,9.037109,1.486114,-3.077172,8.883910,3.799307,-3.436998,4.588552,8.556743],[8.726225,-9.023923,-2.369004,2.263242,6.526798,-4.643892,6.486305,-5.707000,2.895479,-0.873447,1.991952,-8.916914],[-5.420500,7.701353,6.445421,4.687783,2.956923,0.990651,6.241399,-9.985225,-0.771689,7.226341,-7.851318,9.354647],[-8.730115,-8.401912,9.784814,-5.455601,1.913606,2.074197,-0.699409,-5.524193,-7.375174,5.743565,-9.054010,-2.559784]],[[-0.248749,-0.597834,6.873575,-7.740467,-1.178428,-3.603370,5.462859,8.258867,-3.795487,1.764550,6.823134,-8.628781],[3.494141,3.072700,-9.210806,9.415471,-7.170933,2.206847,9.171538,9.842482,-5.604816,9.379738,-7.953016,2.361278],[5.401114,8.818445,-0.893281,-5.968524,0.720518,2.889081,-7.149829,-8.772347,-7.819505,-0.242654,2.383781,2.232951],[7.950798,2.183446,2.761575,8.924268,-9.058704,-8.992852,-8.030440,-1.564428,-4.511417,3.382922,-6.204500,9.824358],[-8.095035,-9.371003,3.452122,7.406629,-0.778883,-0.520513,7.799918,-4.060302,-5.364182,-8.855977,-1.117085,-6.165658],[-6.078674,3.180642,8.901020,-8.155128,-0.849338,8.338746,-7.168127,6.015951,-9.042764,0.123446,6.874228,1.537430],[-5.617725,-3.158021,-7.454012,2.524330,1.445916,-5.082258,-1.290300,-2.551278,4.286446,-6.875044,-5.905377,9.123711],[-4.992523,8.933487,-9.113998,0.057413,-2.817941,0.685057,9.909959,-3.703974,4.268745,6.549908,8.420968,2.469411],[-4.799389,-8.967408,7.375841,1.263261,-1.377447,1.462058,8.588614,8.973840,-4.593559,-6.025393,-5.535213,-6.687782],[1.281376,1.913351,2.688774,-8.605588,-3.586753,9.565515,-9.503863,5.500785,1.359937,7.905668,-2.113736,-0.150854],[-8.052793,-1.159223,9.134123,-8.127829,-1.215965,9.957645,-7.130659,9.807084,2.005763,-4.679239,1.672837,-1.233937],[-5.535554,5.258163,1.920153,-3.100005,3.682537,-2.169251,5.395108,9.789948,-9.563227,-8.889293,-1.586868,0.453362],[-6.197114,4.711034,-3.673320,-3.770531,-1.320382,9.345003,8.310865,8.167358,-2.852201,-8.865692,-5.123075,3.297732],[-8.971878,-3.368091,-6.547395,-3.103990,7.720738,-9.908620,-5.506614,7.238129,3.724870,-5.556385,-2.280987,6.659771]],[[7.214367,-0.814591,2.812471,-2.462927,3.046391,0.106013,-8.301762,-8.650787,5.827250,9.367930,7.218656,-7.123693],[9.879958,-8.876040,-0.165548,-0.077448,1.419350,-6.722373,0.482511,-7.469857,0.453839,-3.117289,-5.925678,4.708888],[9.325005,4.972179,0.735696,5.491206,-1.765823,-2.616189,0.403643,-6.600984,-6.514864,-7.610066,2.279344,-1.534407],[-5.138980,-1.327693,-6.393056,-1.522706,2.193451,-7.490371,-7.644940,9.388533,3.337767,9.663911,9.555407,5.400101],[-0.413510,4.535921,8.018234,-5.273010,-8.830630,-8.709031,4.739383,-2.084046,-2.325249,3.805927,7.660955,0.032174],[7.788522,5.127656,-5.421989,-1.799628,-5.369968,-7.690207,5.639570,1.140738,5.479388,-4.661491,0.243532,6.214115],[-0.660506,-9.579546,-5.148378,-7.681310,-5.223940,-2.506226,6.499400,-2.922277,-3.591767,5.067622,2.332313,7.003542],[-5.409030,6.078831,-9.317415,9.890059,-8.308527,-5.210637,7.650751,-2.402583,9.750180,-5.594412,5.386111,-7.815045],[7.053343,0.430687,8.039504,6.696055,3.121466,9.840331,-6.591511,-0.771129,-2.513046,1.197037,8.960298,8.862971],[-0.109605,1.832689,-3.213378,9.314808,7.608551,4.415277,4.845457,-7.256742,0.474906,-2.900964,-2.690913,-5.351883],[-8.671247,-9.674919,2.971756,-9.063659,5.755549,9.113939,0.598543,6.189364,-8.912635,8.795520,-7.317437,-5.458652],[5.481831,9.900458,8.295003,-4.942311,0.520856,9.503026,6.553927,-2.592851,-2.605936,-0.783655,-7.939093,-8.602707],[-4.611832,-5.807254,-0.184269,3.245132,4.242260,4.996211,-6.833727,-9.286797,8.846253,0.390247,0.407445,7.535942],[4.636678,-6.594249,-9.425943,-6.975181,-1.626498,2.538918,8.496153,7.916652,4.860073,0.448773,-3.882842,0.801433]],[[-7.708065,-7.645514,-6.009824,9.312956,-8.073907,4.955976,-4.473886,4.528110,-1.082521,2.850378,4.954089,-5.865851],[-8.447773,2.913022,-9.835137,-3.198734,5.064820,-2.685077,-8.192536,4.896883,6.748239,4.289564,8.252535,1.219139],[7.411825,2.779868,8.760507,9.935454,-8.338425,-4.147030,2.215484,0.243666,-4.489736,-6.159388,5.186242,9.399299],[-5.151154,-5.331232,7.390156,3.564659,0.268197,-2.137224,1.667003,-0.068973,-4.018171,-7.611357,2.537360,-3.981865],[1.174238,-5.413259,-2.512814,-3.476462,4.554969,-5.327171,-3.457555,5.247041,5.782407,-3.984452,-6.685573,-8.638189],[3.772445,-2.646151,-0.755768,-6.054724,-7.959279,-7.677830,-6.110982,9.401437,5.074949,5.883423,-4.839056,4.326852],[-6.747951,-7.126022,-6.702618,1.925784,0.608382,-2.082099,-7.362221,6.149747,-7.215781,8.990853,-5.925160,-0.802561],[9.563511,0.900368,-9.022211,0.173422,-1.621549,4.618907,-3.006752,2.733346,1.060043,0.595219,-9.714995,-9.403658],[-8.866632,-9.912556,-6.974883,-1.986826,-6.905759,3.753613,6.196779,0.350903,-9.713283,-9.620405,1.606796,-9.752894],[-8.863171,-9.043374,9.426737,7.204151,-6.802305,-2.431281,-5.232685,-4.347212,5.484326,9.040542,-0.275544,-0.755432],[-4.335674,2.711839,-5.661330,-3.102397,6.402990,-3.833582,2.546355,-9.966545,2.482147,-0.059708,-1.562487,-9.072446],[5.619348,-8.848704,-2.285902,-5.189315,2.336223,-7.259406,-2.627020,-3.764618,2.913715,-1.082865,-2.242817,-2.610995],[6.552187,2.060077,-1.409583,4.979223,-2.992059,0.512488,1.444289,5.812352,-3.817464,-3.267593,-7.694638,-1.035711],[8.624763,-2.694841,-2.512685,3.773519,0.618890,5.766993,-0.344863,9.298372,-5.657195,0.255928,6.674830,-8.509241]],[[-5.745842,-3.035807,-0.242299,-3.635967,8.161599,5.468288,-5.654208,5.649112,-4.511603,3.638918,-7.006488,1.884439],[4.684293,-3.884696,7.643279,-2.582009,5.514727,-9.004035,-2.223782,-3.254137,3.305384,4.611676,-1.875783,4.681114],[8.864940,-4.846538,-5.616230,-2.419446,-3.105826,-4.110654,7.571280,-4.342352,2.041001,-9.659891,7.715441,3.911955],[6.614952,-8.682468,1.211586,-3.312254,-4.704332,-7.690016,-6.425586,4.512471,0.083364,-7.300852,-2.029121,-0.680954],[9.728150,2.377457,2.460555,8.558047,6.754610,-9.695347,1.879779,7.887743,5.437162,-8.889160,-3.470109,6.772690],[2.489422,4.480399,-0.040366,1.753933,-2.998850,-9.215018,1.575153,-6.569471,-8.178457,-6.543730,0.710597,0.503055],[2.295318,-4.316040,0.164259,-2.726230,9.825676,2.743842,3.605463,5.408777,3.662108,6.490738,9.266358,-7.295116],[-1.539958,-2.564486,-1.232348,8.993459,6.902262,-7.087216,9.434017,-9.271808,-8.343574,-6.417439,-3.058727,0.293243],[4.128840,3.098100,7.333578,-4.142296,-6.016738,2.791202,8.881500,-8.832275,5.376174,5.074125,4.612618,6.924343],[5.805957,7.579426,-6.379211,-6.704309,7.973438,-9.195723,8.940355,8.600967,2.629744,-7.097623,8.382777,-9.347026],[3.777796,6.718246,2.561363,-0.514999,-9.470779,-7.121822,7.787685,-0.229419,-5.226632,6.170357,-4.546710,7.049174],[8.583479,-4.385082,8.590360,7.366710,-6.102100,4.910189,-4.076178,3.971029,-4.406624,2.091740,-6.459713,-9.552840],[-8.575209,-3.728140,-7.495262,3.060965,7.557426,-5.970633,-9.597675,-5.301655,-8.744826,-2.398540,5.475157,3.339963],[5.181475,2.460221,6.312459,4.032846,1.025484,-0.181400,1.574999,-3.617826,8.263538,5.913862,-9.543413,-6.131212]],[[-1.190139,0.749668,-6.757099,2.074999,8.117564,2.578442,-7.549539,4.046004,-2.217689,-2.015274,8.869049,5.542281],[3.292882,-0.783103,-1.993998,6.267079,8.853596,-9.887822,1.062053,0.825910,9.269955,7.000535,5.409685,7.833175],[-0.032481,-2.768481,-5.363818,-5.708850,-7.523292,-2.424808,-8.240222,5.951633,-8.339078,1.752004,8.069876,8.986793],[-0.432350,3.840429,1.229629,9.831164,-1.468956,7.026116,8.244804,-5.798619,-9.537553,-8.323593,-4.209911,-4.127011],[-4.359648,6.910135,-5.604538,-7.781936,8.055255,6.584200,-3.318501,4.557884,-7.555774,-7.112575,-3.432237,2.378463],[3.723978,8.457386,-6.201508,-0.938626,-0.441393,-3.206384,-4.771823,8.906049,-1.255662,-2.776803,1.978276,3.332730],[-8.964639,-5.339828,1.357093,6.864554,4.078020,-4.736330,-1.267261,-9.454141,-2.290840,-7.353752,1.461249,6.120111],[-0.725356,4.879837,3.493657,0.121205,-8.277919,-0.069349,8.813970,-1.085658,5.125205,-1.929318,0.206879,-4.197265],[-5.076631,4.787404,-7.903488,3.302826,-0.610011,-6.882589,-6.025677,-7.599191,7.869979,-6.116928,-9.773659,-6.181571],[2.569288,-5.625844,1.496632,7.904761,8.232266,-4.554726,6.694846,-0.202885,-0.902305,4.044176,-8.671905,0.780975],[-3.726385,-6.817124,-6.511650,-7.982026,-4.234149,-0.251260,2.958376,6.526490,-0.806108,-1.018681,0.768406,-4.348220],[-0.994033,-6.146229,7.681450,-5.600740,0.700512,-4.079195,5.543013,-2.650274,3.112216,-3.779246,-0.886134,3.644640],[9.968547,-6.728179,-3.932578,-9.186569,-8.216133,8.514531,-9.027582,1.727863,9.954101,3.741541,8.759687,-3.273123],[-2.835153,0.212004,-0.663417,-6.951252,0.618504,-8.189071,3.497356,-1.915757,-8.469990,3.039341,5.122570,-6.794184]],[[-0.636045,-3.951320,3.622930,0.441562,7.468834,-3.241999,2.733778,1.112153,5.072121,2.551448,-8.695514,-7.370729],[8.660229,3.437267,9.801834,7.183774,7.793761,3.312098,-2.990877,-0.680715,1.775968,5.435493,0.226716,3.747137],[4.654058,9.444536,-3.152204,-2.396359,2.459324,8.642144,1.287865,5.450421,-3.155858,-9.740295,0.828825,-5.428242],[6.373717,5.590397,-9.091287,-4.520849,3.357193,9.477121,4.715708,-6.118191,9.838888,2.736901,-4.915441,4.032907],[7.037258,-5.691734,-5.839376,-5.065244,-3.922154,5.525048,-3.116112,-1.924495,0.032746,-2.027072,9.533797,-3.181159],[-0.171081,-4.179112,-9.706964,2.856954,6.902285,-0.128563,-8.146220,3.364002,-6.198443,4.619572,-2.210746,3.077107],[2.755244,3.009749,-1.056808,3.457080,1.452411,8.277403,6.900950,-4.974937,-6.086968,-9.538566,6.462524,-0.926729],[-8.934715,-3.644173,4.566151,9.114121,8.293598,-5.069369,-2.696384,-1.056868,0.348773,0.958667,-3.757144,8.051808],[-2.432458,2.389897,8.738513,0.719698,7.257724,7.931768,5.477425,7.181394,3.832268,-2.541417,3.143784,9.228944],[9.625101,0.939490,-4.147178,-7.225012,2.886360,-0.182066,4.494150,-4.612670,-7.142193,-2.793672,-1.867352,-1.326789],[5.654336,7.693051,-6.739015,4.257324,0.415248,0.942053,8.277173,-1.601519,-5.590121,9.586449,8.084267,-8.942933],[0.115442,7.870242,4.800265,0.008613,6.987089,2.804253,-1.227841,4.496133,-1.911921,8.636475,-4.882600,-6.664481],[7.667209,4.171515,6.547750,-7.213941,-4.481356,8.482016,6.519194,-8.628340,7.487666,-5.824251,-6.822445,-5.613373],[5.252897,-5.831310,7.514238,-9.107153,-5.620227,4.351950,7.466823,2.521240,-4.318691,6.963366,0.677240,-5.688045]],[[-9.522916,-8.466543,-1.462658,8.428833,5.270474,2.572150,-1.277952,6.658142,6.415197,-3.876801,-9.109678,-8.870315],[-0.700839,-3.887224,5.392171,1.467271,-7.816552,-1.227209,-2.355297,-1.285960,9.763958,-6.515578,4.599813,5.900708],[0.853230,7.066425,6.144643,-8.756810,-5.471481,9.163577,9.255557,5.867708,1.804045,-0.503848,1.325905,5.689715],[-7.979668,-2.045660,2.074793,7.886146,3.520796,-4.227376,-3.904964,9.723617,3.203145,6.666776,5.671875,-9.087848],[-3.277253,-2.523728,9.674151,3.690477,0.186934,9.123854,7.939629,4.266551,-0.290797,9.242265,-5.909368,3.061165],[0.736817,-7.796113,0.319881,2.083712,7.046822,3.599596,4.804813,9.218285,-2.280681,6.056266,3.067411,-1.555875],[-9.906453,-9.729652,-7.957414,7.102251,-4.957985,-7.694792,-6.017499,-8.347391,3.997116,8.791070,-7.175424,-7.336795],[8.928054,-5.091816,-6.957958,-5.559932,-0.123351,-7.961440,-0.339095,-3.752726,0.090288,-1.686300,7.926147,-5.484608],[-6.112587,9.323361,-6.717905,3.239925,-4.373461,-5.764799,6.597537,7.961070,3.235589,-1.150360,1.945583,3.057502],[-1.385189,8.748481,-4.818492,-6.655840,2.296124,2.639356,7.203431,0.020136,-9.362277,2.347617,2.648124,7.038463],[-1.859261,-9.726848,-6.010984,-2.267771,-1.657712,-2.538536,6.911543,0.452799,6.050605,-5.552822,-8.080884,-3.369001],[8.996111,-3.406631,-5.677731,-7.952608,0.130248,3.676892,-8.851488,-2.446149,6.201340,3.399776,-7.726124,6.764068],[6.239881,-9.960242,7.207357,-3.964102,-7.959102,3.889492,-7.404818,6.819652,5.086263,4.324505,7.423489,-9.342304],[1.140684,8.158302,-3.921189,4.357016,6.557092,8.697512,-1.508397,3.546169,-2.456118,4.517666,-1.238460,2.085400]],[[6.856356,4.636694,-8.952454,0.969291,6.683752,0.748008,8.548312,6.806184,1.731270,-9.730224,-9.291808,-1.806256],[-6.097301,2.702783,4.302940,-5.028928,-5.087938,9.620159,7.905473,-6.006191,8.742121,2.008815,-6.022184,2.590596],[0.128514,7.186425,-6.582861,2.812704,7.374920,8.324868,3.519226,-2.719994,-7.919943,-9.166434,-5.068347,-9.002177],[7.645220,7.913219,3.405199,0.515102,-0.290595,-2.454056,-1.679496,2.805070,6.964545,-2.191813,1.478154,-5.352012],[-2.941225,1.296729,4.267518,0.481908,5.782134,-0.699952,1.634436,-7.198242,-0.692949,-7.898503,-1.989284,-3.152946],[4.883432,-7.065759,4.729609,-1.597055,9.026874,4.981321,6.349695,1.271969,6.181621,3.531170,2.069550,-8.708193],[8.631074,4.283476,-0.557747,5.688743,-3.098243,-7.162981,-1.499086,-7.188254,8.674379,-6.186537,-9.558038,7.392540],[8.355438,-3.892795,-7.961246,-9.898277,-0.216128,0.353035,7.872033,-2.294798,-1.241283,-1.786234,9.401941,6.953208],[-0.327944,2.001962,9.340009,-1.038277,-0.446974,-8.007843,6.977261,-7.854506,-1.648512,-8.348130,-5.582277,0.248096],[-4.635534,2.500015,-9.657930,-5.729315,-9.283969,1.408778,-8.029021,-2.491009,3.009134,-6.948371,9.356163,-2.111216],[-4.730885,8.442985,8.114584,-3.398920,-6.247889,1.131468,-9.940200,1.430296,8.062037,-3.690243,-1.553494,-1.947380],[4.591547,-1.038455,5.934276,-8.155750,-8.623278,-7.014316,9.123062,1.593157,-9.541318,-5.784489,-6.306116,1.192294],[0.080613,7.327414,-4.798348,6.355926,-4.559957,-3.214850,-9.018676,-8.421296,2.899955,-6.727388,7.346591,-9.398940],[-6.778704,-8.686738,6.243645,-2.343908,9.331493,-3.343078,-8.649596,-5.817678,-0.744775,-9.981164,2.019098,5.346259]],[[-7.866972,7.715238,1.289305,2.663361,0.649993,-9.097814,-3.021543,3.312982,-0.821072,0.908295,2.943831,-7.896059],[6.171898,-3.060965,6.152442,6.267132,6.324804,0.573979,-1.327715,-5.259867,-3.622917,-5.393760,4.514801,-3.263315],[-2.968743,-6.330318,5.013361,6.445159,-7.693751,-5.308783,2.612250,0.049551,-7.638368,5.882453,4.220200,-6.361733],[-8.969489,-0.569950,-5.053862,6.413580,2.165005,-6.784447,-1.388243,0.391220,0.616953,-9.982155,2.192846,3.212321],[-9.396460,-5.892180,-1.004553,2.506497,-3.365004,9.739562,6.745102,4.627409,-8.899425,8.913033,0.513367,6.327887],[-8.856694,5.693158,1.777541,-0.041395,6.952286,-0.147150,7.398909,-6.018963,2.651265,0.712254,-5.378325,3.794022],[-3.350600,-2.609053,5.167373,4.313646,5.276646,8.701627,1.154203,6.702869,8.037952,0.682092,9.444540,-7.048316],[3.101416,8.315056,-1.974525,-3.383230,-1.059617,-5.843569,6.177302,2.754224,-7.617064,0.839184,-6.772437,-7.777255],[-0.061430,8.434271,5.201893,8.162003,1.077475,-6.218953,8.078753,-8.797290,0.880485,-0.744146,-7.628428,-2.858357],[-0.420807,8.565218,-0.273295,-3.029782,1.800831,-8.944073,3.075308,0.118021,9.542608,-1.973901,-0.823676,-8.445073],[6.763535,-3.416606,-0.557543,-3.630275,5.141482,-6.481571,5.408844,-9.494681,-2.605325,9.384460,-1.671052,-7.722087],[3.539132,7.825924,6.465661,9.071309,-8.731671,2.982975,-7.092514,3.296748,9.728166,4.201852,7.405236,8.463306],[6.854240,6.274826,2.575001,5.839076,1.036982,-2.187563,-3.013299,8.452158,-6.135995,1.704439,6.704996,-6.697351],[-0.625766,3.654471,0.943067,1.510632,-4.618889,0.833883,-0.336933,-6.326997,6.380103,5.161497,-7.642157,-0.383550]],[[6.538878,-6.141804,-9.568471,0.217097,-2.551757,-9.678772,9.520134,-6.851047,6.784491,2.450644,-9.781017,8.428499],[-5.807791,0.760390,8.532192,7.244307,-2.169896,6.427247,-3.820858,5.916951,-9.314824,4.264718,-6.845350,4.362408],[0.056919,1.650604,-5.705201,6.981382,2.595743,4.036274,-0.536991,4.981471,-7.362459,5.528782,8.776145,-3.693070],[3.687278,0.495976,1.317566,7.605215,2.780445,4.588222,2.957028,3.666070,5.229140,0.132868,9.778729,-0.915967],[-7.793343,8.196765,6.111756,6.838658,4.622207,-1.929936,5.940292,3.289831,-8.379381,-1.385012,6.353654,8.785384],[-7.569846,-3.841159,0.460043,-1.648768,-4.049732,-3.361048,5.475420,-0.738669,-8.592682,6.084837,-4.893263,1.317406],[7.685599,-0.618256,2.565481,-1.480759,8.870647,6.795867,2.131167,-4.949265,7.434939,1.322856,-5.857815,9.806082],[-3.450455,-0.652777,1.881727,-9.884684,2.972689,1.913431,-0.731048,-9.744398,-0.495974,-0.080557,7.418489,-5.829715],[4.213967,2.063085,4.867001,3.568583,-4.514279,3.794335,9.841777,-6.795712,-8.684200,3.913710,6.516811,-8.879891],[3.610777,-3.942959,8.016631,-7.175269,-4.885444,-3.084814,-4.571490,-1.854043,1.710036,6.582415,3.179832,5.142962],[6.372827,-8.217782,2.526867,3.671912,4.563709,5.749541,-0.411101,-4.659108,-3.443413,-6.267483,-4.083148,8.789100],[-4.863816,-7.759703,-7.858085,-3.808381,-9.743326,7.796926,5.086852,-4.864520,-9.525964,-3.422198,5.317809,2.965907],[2.868867,2.322343,-2.070600,-8.180217,4.864912,-6.460681,-3.566476,4.885647,4.673435,-7.727244,6.843464,-0.138542],[6.896497,-1.905422,2.892612,-3.007220,-7.066303,-8.289586,-7.668005,7.691645,1.505725,0.034263,-3.111090,-1.677428]]], dtype = "float32")#candidate|6008|(11, 14, 12)|const|float32
bop_6009 = relay.logical_or(call_6006.astype('bool'), relay.reshape(const_6008.astype('bool'), relay.shape_of(call_6006))) # shape=(11, 14, 12)
bop_6012 = relay.logical_or(call_6007.astype('bool'), relay.reshape(const_6008.astype('bool'), relay.shape_of(call_6007))) # shape=(11, 14, 12)
output = bop_6009
output2 = bop_6012
func_6015 = relay.Function([], output)
mod['func_6015'] = func_6015
mod = relay.transform.InferType()(mod)
output = func_6015()
func_6016 = relay.Function([], output)
mutated_mod['func_6016'] = func_6016
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4017_call = mod.get_global_var('func_4017')
func_4018_call = mutated_mod.get_global_var('func_4018')
call_6044 = relay.TupleGetItem(func_4017_call(), 0)
call_6045 = relay.TupleGetItem(func_4018_call(), 0)
output = call_6044
output2 = call_6045
func_6048 = relay.Function([], output)
mod['func_6048'] = func_6048
mod = relay.transform.InferType()(mod)
mutated_mod['func_6048'] = func_6048
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6048_call = mutated_mod.get_global_var('func_6048')
call_6049 = func_6048_call()
output = call_6049
func_6050 = relay.Function([], output)
mutated_mod['func_6050'] = func_6050
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6048_call = mod.get_global_var('func_6048')
func_6050_call = mutated_mod.get_global_var('func_6050')
call_6056 = func_6048_call()
call_6057 = func_6048_call()
output = call_6056
output2 = call_6057
func_6061 = relay.Function([], output)
mod['func_6061'] = func_6061
mod = relay.transform.InferType()(mod)
output = func_6061()
func_6062 = relay.Function([], output)
mutated_mod['func_6062'] = func_6062
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6102 = relay.var("var_6102", dtype = "uint64", shape = ())#candidate|6102|()|var|uint64
var_6103 = relay.var("var_6103", dtype = "uint64", shape = (6, 7, 8))#candidate|6103|(6, 7, 8)|var|uint64
bop_6104 = relay.bitwise_or(var_6102.astype('uint64'), var_6103.astype('uint64')) # shape=(6, 7, 8)
output = relay.Tuple([bop_6104,])
output2 = relay.Tuple([bop_6104,])
func_6117 = relay.Function([var_6102,var_6103,], output)
mod['func_6117'] = func_6117
mod = relay.transform.InferType()(mod)
mutated_mod['func_6117'] = func_6117
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6117_call = mutated_mod.get_global_var('func_6117')
var_6119 = relay.var("var_6119", dtype = "uint64", shape = ())#candidate|6119|()|var|uint64
var_6120 = relay.var("var_6120", dtype = "uint64", shape = (6, 7, 8))#candidate|6120|(6, 7, 8)|var|uint64
call_6118 = func_6117_call(var_6119,var_6120,)
output = call_6118
func_6121 = relay.Function([var_6119,var_6120,], output)
mutated_mod['func_6121'] = func_6121
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5900_call = mod.get_global_var('func_5900')
func_5901_call = mutated_mod.get_global_var('func_5901')
call_6133 = relay.TupleGetItem(func_5900_call(), 0)
call_6134 = relay.TupleGetItem(func_5901_call(), 0)
output = relay.Tuple([call_6133,])
output2 = relay.Tuple([call_6134,])
func_6141 = relay.Function([], output)
mod['func_6141'] = func_6141
mod = relay.transform.InferType()(mod)
mutated_mod['func_6141'] = func_6141
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6141_call = mutated_mod.get_global_var('func_6141')
call_6142 = func_6141_call()
output = call_6142
func_6143 = relay.Function([], output)
mutated_mod['func_6143'] = func_6143
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5900_call = mod.get_global_var('func_5900')
func_5901_call = mutated_mod.get_global_var('func_5901')
call_6169 = relay.TupleGetItem(func_5900_call(), 0)
call_6170 = relay.TupleGetItem(func_5901_call(), 0)
output = call_6169
output2 = call_6170
func_6173 = relay.Function([], output)
mod['func_6173'] = func_6173
mod = relay.transform.InferType()(mod)
mutated_mod['func_6173'] = func_6173
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6173_call = mutated_mod.get_global_var('func_6173')
call_6174 = func_6173_call()
output = call_6174
func_6175 = relay.Function([], output)
mutated_mod['func_6175'] = func_6175
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6173_call = mod.get_global_var('func_6173')
func_6175_call = mutated_mod.get_global_var('func_6175')
call_6225 = func_6173_call()
call_6226 = func_6173_call()
output = call_6225
output2 = call_6226
func_6233 = relay.Function([], output)
mod['func_6233'] = func_6233
mod = relay.transform.InferType()(mod)
output = func_6233()
func_6234 = relay.Function([], output)
mutated_mod['func_6234'] = func_6234
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5992_call = mod.get_global_var('func_5992')
func_5993_call = mutated_mod.get_global_var('func_5993')
call_6313 = relay.TupleGetItem(func_5992_call(), 1)
call_6314 = relay.TupleGetItem(func_5993_call(), 1)
var_6317 = relay.var("var_6317", dtype = "float32", shape = (11, 14, 12))#candidate|6317|(11, 14, 12)|var|float32
bop_6318 = relay.less_equal(call_6313.astype('bool'), relay.reshape(var_6317.astype('bool'), relay.shape_of(call_6313))) # shape=(11, 14, 12)
bop_6321 = relay.less_equal(call_6314.astype('bool'), relay.reshape(var_6317.astype('bool'), relay.shape_of(call_6314))) # shape=(11, 14, 12)
func_6141_call = mod.get_global_var('func_6141')
func_6143_call = mutated_mod.get_global_var('func_6143')
call_6346 = relay.TupleGetItem(func_6141_call(), 0)
call_6347 = relay.TupleGetItem(func_6143_call(), 0)
output = relay.Tuple([bop_6318,call_6346,])
output2 = relay.Tuple([bop_6321,call_6347,])
func_6361 = relay.Function([var_6317,], output)
mod['func_6361'] = func_6361
mod = relay.transform.InferType()(mod)
mutated_mod['func_6361'] = func_6361
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6362 = relay.var("var_6362", dtype = "float32", shape = (11, 14, 12))#candidate|6362|(11, 14, 12)|var|float32
func_6361_call = mutated_mod.get_global_var('func_6361')
call_6363 = func_6361_call(var_6362)
output = call_6363
func_6364 = relay.Function([var_6362], output)
mutated_mod['func_6364'] = func_6364
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4800_call = mod.get_global_var('func_4800')
func_4802_call = mutated_mod.get_global_var('func_4802')
call_6386 = func_4800_call()
call_6387 = func_4800_call()
var_6404 = relay.var("var_6404", dtype = "float32", shape = (11, 14, 12))#candidate|6404|(11, 14, 12)|var|float32
bop_6405 = relay.logical_xor(call_6386.astype('uint64'), relay.reshape(var_6404.astype('uint64'), relay.shape_of(call_6386))) # shape=(11, 14, 12)
bop_6408 = relay.logical_xor(call_6387.astype('uint64'), relay.reshape(var_6404.astype('uint64'), relay.shape_of(call_6387))) # shape=(11, 14, 12)
func_4398_call = mod.get_global_var('func_4398')
func_4401_call = mutated_mod.get_global_var('func_4401')
const_6410 = relay.const([-8,-5,3,-6,5,-8,5,-2,-5,-8,9,6,-3,-8,5,-9,10,-5,5,1,5,1,-1,10,-5,5,-8,-4,8,-3,7,-7,-7,-10,-4,-2,-8,-9,-4,-7,7,-5,-2,5,-8,4,4,2,6,4,3,-8,-7,-2,-4,-3,10,8,-6,-2], dtype = "uint32")#candidate|6410|(60,)|const|uint32
const_6411 = relay.const([-1.374680,2.577275,4.002259,1.687048,4.281153,-4.223312,-8.440349,-3.025466,-4.228069,-1.783893,-7.930751,-9.504072,4.902199,-8.409481,0.392198,-0.590843,1.202510,-7.658300,1.274503,-5.038800,-8.114866,-7.747703,-8.407419,2.618135,9.169187,-2.994120,-8.419558,-1.099931,6.190107,9.922250,-3.436222,-5.480493,1.019041,5.823909,-8.584456,6.403679,-5.324451,4.915235,-1.869333,-6.681563,-4.585979,6.652444,8.838691,9.898323,5.555046,3.288188,-3.173581,5.381815,3.258582,8.582397,-2.792293,-0.146224,-6.232261,-1.413635,-6.354429,-7.854754,2.946737,7.234288,8.317551,3.489873,1.851531,0.573835,-1.585785,7.831739,2.624989,0.321658,5.337471,-5.226151,-7.856541,-7.359824,3.899252,0.539052,4.758367,8.731971,7.566964,5.367830,-9.716510,7.183946,6.740462,-2.154722,9.567918,3.118104,7.848159,-7.931346,-1.446187,-8.012880,-5.006188,-6.627976,-9.962161,-3.570384,-7.650943,7.345211,-4.659241,4.581364,2.191981,-1.791689,6.374023,-9.549918,-8.120147,-5.595321,4.556510,-4.879401,7.025781,5.274079,5.560633,6.202929,9.781422,-6.625143,4.082307,-4.183108,3.861080,2.458438,-0.015573,7.442065,9.731397,5.151780,-4.487190,-1.131585,-5.820824,5.469197,0.259253,5.107867,1.142313,4.153024,9.888416,-9.262182,-8.403443,2.100727,0.947152,1.452694,7.224793,4.548611,0.250833,2.018452,-3.817218,1.346072,6.712129,-4.591722,-3.051453,-7.257551,0.556422,-3.025690,-7.633563,-3.668985,-0.448146,-8.432765,-1.008355,6.242070,7.384438,7.739120,6.140429,-6.816655,4.700103,-7.583886,-2.446621,9.476802,4.293096,3.319101,-9.555105,4.372751,-5.460043,-3.586131,5.509204,-9.680354,-7.326580,-2.608033,-0.730348,-8.942021,-6.110526,3.953645,0.891688,-9.649119,-0.260676,3.584943,-4.198298,3.716489,-1.011767,9.640292,5.969543,3.375703], dtype = "float32")#candidate|6411|(180,)|const|float32
call_6409 = relay.TupleGetItem(func_4398_call(relay.reshape(const_6410.astype('uint32'), [60,]), relay.reshape(const_6411.astype('float32'), [180,]), ), 10)
call_6412 = relay.TupleGetItem(func_4401_call(relay.reshape(const_6410.astype('uint32'), [60,]), relay.reshape(const_6411.astype('float32'), [180,]), ), 10)
func_2208_call = mod.get_global_var('func_2208')
func_2211_call = mutated_mod.get_global_var('func_2211')
const_6421 = relay.const([3.169972,1.807340,1.361867,-2.389858,-2.469906,5.190912,9.465194,-7.467460,4.168123,0.768549,7.723888,-9.930531,-3.637286,-2.194013,-9.300230,-4.588566,4.412542,7.105529,-8.506718,-7.625701,3.476403,-6.686782,-5.315412,-6.707795,-7.528985,-9.048814,1.332373,5.198598,9.368121,-0.741127,7.333010,0.817225,-6.092848,2.889693,-7.561747,-8.618069,3.702517,1.673005,8.596230,7.081403,7.158691,4.595800,-2.716502,-9.301949,1.594004,3.722155,-2.808596,1.545961,4.790806,8.193572,-8.887845,-9.967370,-3.791445,9.642654,5.170223,-9.222721,2.100386,-3.320059,-7.474224,3.703705,5.080191,-5.505885,4.735167,-0.942550,7.740673,5.544951,2.404248,1.973202,2.944588,-2.105601,-5.910563,0.212835,-0.146577,1.459301,-6.749572,-3.439069,-8.270469,0.443172,-3.673658,-1.075173,2.698806,-2.238002,4.935939,4.215066,-8.852862,-2.063602,-1.694626,-2.883494,1.646023,5.934033,-7.335486,0.709993,4.603779,0.464461,-8.011510,2.956252,3.339669,4.261811,3.386097,2.190687,-0.285203,-2.215492,6.263205,6.517996,7.029973,-9.710745,5.981297,-2.670526,4.355574,-1.857263,1.984116,7.083158,1.958306,-9.257774,7.198060,5.598178,5.638686,-3.539819,-5.838589,8.557565,8.146085,-3.933688,4.057867,6.180635,-6.080432,-5.021221,2.103145,-9.815518,-5.496252,2.429617,-0.168696,5.693097,9.457348,-2.230299,-9.104421,9.053400,4.640144,-4.816132,-3.020749,5.571922,9.583794,-2.446989,-6.111466,-2.608838,1.912415,-0.092627,-1.369962,1.002818,-3.656083,2.442936,4.705729,-5.611569,-2.449238,8.228381,-1.782967,3.835454,9.452614,-9.395776,-8.559185,-2.887624,-3.475475,8.926542,5.498944,-0.397205,-7.685208,-7.190446,-0.564967,9.860455,5.198475,7.615849,1.946919,7.968868,3.144524,-7.990894,-0.619896,8.929523,-9.348406,3.803236,-6.943065,5.831118,-5.650324,-1.069234,-6.643787,7.251619,6.214782,9.813455,-9.603735,9.628497,-8.470298,0.751436,-4.662881,9.865740,-6.900027,-4.613987,4.828549,9.493001,6.812769,-3.532210,5.357171,7.561127,3.571806,-0.362113,-6.175317,4.884693,1.799000,3.038148,5.961125,-2.895889,-8.086943,-6.908625,-8.551226,3.118854,-5.682099,3.024119,2.609615,-4.606863,1.783762,-2.635171,-8.895697,-0.559019,1.164478,5.312611,9.936683,-2.172478,9.608958,1.348056,-5.688935,2.268729,-5.391766,2.995950,-5.199124,-1.657865,-2.096591,2.591745,-8.198148,-1.098492,9.981517,2.833094,-6.926456,-6.530170], dtype = "float64")#candidate|6421|(240,)|const|float64
call_6420 = func_2208_call(relay.reshape(const_6421.astype('float64'), [12, 2, 10]))
call_6422 = func_2208_call(relay.reshape(const_6421.astype('float64'), [12, 2, 10]))
func_4989_call = mod.get_global_var('func_4989')
func_4992_call = mutated_mod.get_global_var('func_4992')
var_6426 = relay.var("var_6426", dtype = "int16", shape = (4, 420))#candidate|6426|(4, 420)|var|int16
call_6425 = relay.TupleGetItem(func_4989_call(relay.reshape(var_6426.astype('int16'), [12, 10, 14]), relay.reshape(call_6409.astype('float64'), [60, 2]), ), 0)
call_6427 = relay.TupleGetItem(func_4992_call(relay.reshape(var_6426.astype('int16'), [12, 10, 14]), relay.reshape(call_6409.astype('float64'), [60, 2]), ), 0)
output = relay.Tuple([bop_6405,call_6409,const_6410,const_6411,call_6420,const_6421,call_6425,var_6426,])
output2 = relay.Tuple([bop_6408,call_6412,const_6410,const_6411,call_6422,const_6421,call_6427,var_6426,])
func_6431 = relay.Function([var_6404,var_6426,], output)
mod['func_6431'] = func_6431
mod = relay.transform.InferType()(mod)
var_6432 = relay.var("var_6432", dtype = "float32", shape = (11, 14, 12))#candidate|6432|(11, 14, 12)|var|float32
var_6433 = relay.var("var_6433", dtype = "int16", shape = (4, 420))#candidate|6433|(4, 420)|var|int16
output = func_6431(var_6432,var_6433,)
func_6434 = relay.Function([var_6432,var_6433,], output)
mutated_mod['func_6434'] = func_6434
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5240_call = mod.get_global_var('func_5240')
func_5242_call = mutated_mod.get_global_var('func_5242')
call_6439 = relay.TupleGetItem(func_5240_call(), 0)
call_6440 = relay.TupleGetItem(func_5242_call(), 0)
func_1259_call = mod.get_global_var('func_1259')
func_1263_call = mutated_mod.get_global_var('func_1263')
var_6449 = relay.var("var_6449", dtype = "int64", shape = (845, 1))#candidate|6449|(845, 1)|var|int64
var_6450 = relay.var("var_6450", dtype = "float32", shape = (180, 1))#candidate|6450|(180, 1)|var|float32
const_6451 = relay.const([-3,2,2,3,3,-9,-7,-1,9,1,-8,4,10,9,7,6,3,-7,6,-2,-7,10,-3,-2,-10,6,10,4,-8,-9,-8,-4,2,7,-3,-9,-1,-6,-1,-1,-3,-10,8,2,-6,-2,-5,7,-10,-7,7,-3,6,-5,10,-7,2,8,1,10,3,4,-10,7,-9,-3,2,-3,7,-7,-5,-10,2,-8,7,2,2,10,-1,4,-1,4,-4,6,-6,-10,7,-9,7,-6,7,-6,6,-3,-3,4,-5,-1,-7,2,-8,-6,2,6,3,8,1,-9,2,-3,10,-10,10,-3,8,2,-10,3,-2,-3,-2,-4,-5,-10,-6,3,-4,8,4,-1,-9,-10,-9,-10,1,-7,6,-6,4,-7,2,-4,-3,-2,-6,-1,6,-3,-4,8,-8,-8,6,-5,-3,1,-4,-4,9,-6,-9,-1,10,-3,-9,-10,6,3,-4,-2,-5,-4,10,-8,6,-4,-2,-1,9,7,-5,-6,4,4,-2,-7,-3,-3,-1,-10,6,-3,8,-3,7,6,-6,4,-4,8,-9,2,-9,3,-8,8,-8,2,-4,3,-4,5,3,-10,10,-4,6,-10,-1,-3,-7,-2,-2,3,1,9,-6,7,-6,8,-8,6,8,-7,3,9,2,7,8,-2,-5,-8,7,-10,-6,-10,1,-6,-4,-10,-4,-8,-10,2,4,-1,-7,10,8,-7,-8,-9,-5,-8,10,7,-6,-10,-10,6,-6,-3,-8,9,2,-10,-4,-9,-6,9,4,-9,3,-7,-2,8,-10,5,5,3,9,-8,-2,4,-4,3,-1,8,-2,10,6,5,1,3,1,5,-1,3,-10,3,-9,1,7,-5,-4,4,-3,5,9,1,-8,-10,-9,-2,1,4,2,-4,-7,-7,-6,-1,1,4,-6,10,1,-2,-4,-9,2,8,9,2,-1,-6,-3,5,-3,-2,5,-4,1,-5,4,1,-7,1,-1,3,5,10,-4,-10,5,9,-3,4,-1,-8,-5,3,9,2,-7,1,-4,-10,5,7,-1,8,9,7,-3,5,5,3,-1,4,-10,2,6,-4,1,1,-8,-7,4,-7,2,-8,9,10,6,10,9,-2,1,7,7,-5,10,-4,-7,-1,4,-5,-1,-4,1,7,-3,6,-6,9,3,-10,5,7,-4,2,-10,-2,-4,-9,2,4,6,-1,-2,-6,4,8,-8,3,3,-4,4,3,-4,-10,10,-2,-3,7,-3,2,6,9,5,10,9,1,9,9,6,-10,5,-1,6,6,10,9,8,-2,1,-8,-5,2,-3,-7,-2,5,10,-8,5,-8,-1,-1,-6,-9,4,-5,-8,-2,2,2,-8,-3,-3,9,-4,3,5,-4,6,5,-5,-6,1,-6,9,7,4,-8,-3,-5,3,2,-1,-6,-2,-4,3,-1,-9,-7,4,-6,6,-5,10,-7,7,8,8,4,6,8,-9,-6,-6,9,-7,-8,10,3,3,-10,9,-10,-3,-8,2,10,5,-4,-9,2,-7,-10,-2,-6,2,7,3,10,-10,6,-6,-7,-2,-3,3,6,6,8,8,-2,9,6,7,-9,6,-10,4,3,-10,7,-4,5,1,-9,-7,-3,-2,-10,5,-7,7,-3,-7,-8,-7,-10,2,-2,-9,1,-3,4,-3,4,6,-9,9,5,-10,-2,-2,7,-8,-4,-9,-4,-1,-6,3,-2,-1,1,3,-5,10,8,-10,3,-4,-4,4,-5,-8,-9,3,9,2,-4,-7,8,6,1,-4,1,-5,-3,5,-4,-3,4,-6,-1,-5,5,-4,3,-2,-4,-1,4,-2,-5,-7,1,-5,5,8,-2,-1,-6,2,4,6,-10,-5,-2,-3,7,9,-7,3,-6,8,-5,-4,3,-2,10,7,4,-6,10,-5,-7,-2,-9,-8,5,4,4,-1,-4,4,-1,-5,2,3,-1,8,3,6,-5,8,2,-2,-9,-5,-7,10,1,-3,9,6,4,-9,6,-2,2,2,3,-2,8,7,8,3,3,4,-4,1,6,7,-7,-4,-1,5,-2,-6,4,-4,-3,6,3,-7,2,-4,-9,-10,-2,-5,3,-8,-7,-3,-10,-5,-4,-8,-1,-3,-4,-1,10,9,-8,-6,4,-5,-10,2,-5,-2,8,-5,6,3,-7,-1,8,10,4,-6,-9,7,-9,-9,6,5,-3,6,-10,-9,3,-3,-10,8,8,2,7,9,10,2,1,-3,-8,4,-8,-5,3,-4,1,-10,-8,-8,-4,4,-5,4,-4,10,6,1,7,4,6,-6,2,9,8,6,4,-8,6,5,-10,3,-9,9,2,7,-3,-8,8,-4,5,-10,2,8,-1,10,-7,7,-7,3,10,-1,2,-6,7,7,-2,10,5,1,-10,7,-4,-5,-1,-2,8,-3,-1,3,9,-9,-8,-4,-7,-1,6,6,4,-10,-10,5,-6,-10,-7,6,-6,-8,3,9,7,-9,-10,2,8,9,6,6,2,8,1,-5,8,1,-3,5,10,4,1,-6,-10,5,-8,-8,8,-8,-10,6,-6,3,-9,1,4,-1,-5,-4,-1,3,-1,-2,6,10,2,-8,-4,10,-1,3,8,8,1,2,-10,-3,-5,2,4,-1,-7,-7,-2,-2,-9,6,-9,3,-8,-3,-10,-1,-3,8,4,-6,-8,10,1,3,-9,9,5,7,9,-2,-8,5,8,9,-3,-1,-9,3,6,-1,-4,2,-2,-5,-1,-1,-1,-2,-8,-9,7,5,4,7,-3,5,-9,-9,8,-6,-2,-7,1,-2,-2,1,-4,7,-4,7,5,7,1,-8,1,-7,1,5,-5,1,9,-9,10,-8,2,-2,-1,2,-6,-10,-6,-9,1,7,1,3,3,1,-8,8,8,7,-10,9,1,2,-6,-4,-4,-3,10,7,10,7,-10,-7,8,6,-3,3,-6,-1,7,-9,6,-10,-10,2,-6,7,5,-4,6,-10,-7,-4,1,5,-3,-10,8,9,-6,7,9,8,6,8,2,-4,2,-3,-7,10,-5,-3,2,-1,1,2,2,6,4,1,-2,6,-4,7,-7,3,7,5,6,-8,3,-8,2,2,-8,1,-9,1,5,-7,5,6,-8,3,-6,2,3,-2,-6,10,-9,-1,9,2,-2,-8,-2,10,5,3,-4,-1,-9,-3,-9,-8,-3,7,-2,6,9,-2,-8,9,6,5,1,9,2,4,5,10,-2,10,7,10,1,4,-4,3,9,2,-7,-1,-2,-10,8,5,-8,-5,-2,-10,-7,-2,-9,3,-4,-9,5,-10,6,4,-2,7,-5,-5,-7,9,1,-9,6,-10,4,-1,-3,7,-1,-7,-1,2,-7,2,4,-10,-3,-7,10,9,-9,4,-9,3,-4,-10,-3,3,-1,-3,-6,-10,-3,-8,-4,-4,7,-7,1,-6,-10,-9,1,2,7,-7,-10,4,3,6,-10,10,-10,-4,7,-3,-6,-10,4,-9,9,6,2,-5,-3,-2,-1,10,9,2,4,3,-2,7,6,7,-3,-9,4,-3,6,1,8,-1,-5,-5,2,7,2,10,-3,7,1,-4,-1,3,2,5,5,-9,2,-7,3,-6,1,6,4,-1,-9,-1,2,6,-10,-6,-10,7,-8,-4,-2,9,-8,-7,-8,9,-5,-6,6,3,-6,3,3,-5,6,-5,2,10,-8,-2,9,-4,2,3,3,-6,-4,-4,-10,-9,10,3,-7,4,3,-2,9,-7,7,1,-8,10,7,-1,6,-3,6,-8,2,10,10,-8,-9,2,-6,5,-9,6,-10,-4,8,3,-7,7,-5,-5,-1,3,-9,-4,-7,9,-6,5,3,-4,-9,5,10,-3,10,-9,2,-9,-9,8,-5,-4,-3,9,-10,-6,-10,3,4,-4,-8,3,8,-3,-6,5,-9,2,-9,7,-6,8,-6,5,-9,-2,5,-6,-7,2,-9,5,-7,9,10,7,3,-1,8,-8,-6,-5,8,-3,-10,10,-3,7,-6,10,-6,-9,4,-7,7,-1,-10,3,6,6,-5,7,-3,-8,5,-4,-6,-10,-4,-3,6,3,8,3,4,-4,-6,-6,7,10,3,3,-7,-10,-9,2,-6,-1,-3,-10,6,7,-5,2,9,4,-8,-3,-9,7,-5,5,-6,-6,3,-7,10,-2,8,-8,8,1,10,-2,-5,9,10,1,-2,-6,-5,-3,-6,9,-9,-1,9,-4,5,8,-2,2,-2,-7,-2], dtype = "int8")#candidate|6451|(1568,)|const|int8
call_6448 = relay.TupleGetItem(func_1259_call(relay.reshape(var_6449.astype('int64'), [5, 13, 13]), relay.reshape(var_6450.astype('float32'), [180,]), relay.reshape(const_6451.astype('int8'), [1568,]), ), 1)
call_6452 = relay.TupleGetItem(func_1263_call(relay.reshape(var_6449.astype('int64'), [5, 13, 13]), relay.reshape(var_6450.astype('float32'), [180,]), relay.reshape(const_6451.astype('int8'), [1568,]), ), 1)
func_4201_call = mod.get_global_var('func_4201')
func_4205_call = mutated_mod.get_global_var('func_4205')
const_6459 = relay.const([0.494257,2.574747,7.160035,-2.660130,-3.566432,-4.994638,4.682645,5.936715,9.497848,-4.705092,-7.810927,-4.404413,-8.429202,9.724453,-4.576732,-2.676299,5.989823,4.222513,-6.826711,2.143068,-6.702413,1.417847,5.402822,1.126732,-2.851593,-8.246370,3.511923,-4.188498,7.541017,4.461838,0.763466,7.813592,-9.702690,-2.492647,-7.531964,0.130659,7.766424,3.247079,0.770025,5.296813,-9.452867,-4.457486], dtype = "float32")#candidate|6459|(42,)|const|float32
var_6460 = relay.var("var_6460", dtype = "int8", shape = ())#candidate|6460|()|var|int8
var_6461 = relay.var("var_6461", dtype = "bool", shape = (896,))#candidate|6461|(896,)|var|bool
call_6458 = relay.TupleGetItem(func_4201_call(relay.reshape(const_6459.astype('float32'), [14, 3, 1]), relay.reshape(var_6460.astype('int8'), []), relay.reshape(var_6461.astype('bool'), [896,]), ), 1)
call_6462 = relay.TupleGetItem(func_4205_call(relay.reshape(const_6459.astype('float32'), [14, 3, 1]), relay.reshape(var_6460.astype('int8'), []), relay.reshape(var_6461.astype('bool'), [896,]), ), 1)
const_6464 = relay.const([True,True,False,True,True,False,False,False,False,False,True,False,True,True,True,False,True,False,False,False,True,True,True,False,False,True,False,True,False,False,False,True,True,False,False,False,True,True,True,True,True,False,True,False,True,False,True,False,True,True,False,False,False,True,False,False,True,True,False,True,True,False,False,False,False,False,False,True,True,True,False,True,True,True,True,True,False,False,True,True,False,False,True,False,True,True,True,False,False,True,True,True,True,True,True,True,False,False,True,True,True,True,False,True,True,False,False,True,False,True,False,False,True,True,True,True,False,False,True,True,True,True,False,False,False,False,True,False,False,False,False,True,False,False,False,True,False,False,False,True,False,False,True,True,True,False,False,True,False,False,False,True,True,True,True,True,True,True,False,True,True,False,False,True,False,True,False,True,True,False,False,True,False,True,True,True,False,True,True,False,True,True,False,False,False,True,False,True,False,False,False,False,False,True,True,False,False,False,True,True,False,True,True,True,True,False,False,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,False,True,False,False,True,True,False,True,True,True,False,False,True,True,True,False,False,False,True,True,False,True,True,True,False,False,False,False,True,False,True,False,True,True,False,False,True,False,True,False,True,False,False,False,True,True,True,True,True,False,True,True,True,False,False,False,False,True,False,True,True,True,True,False,True,False,False,False,False,True,False,False,True,False,False,False,True,True,False,False,False,True,False,True,True,False,True,True,True,True,False,False,True,False,False,False,False,False,False,False,False,False,False,True,False,True,False,True,False,False,True,False,True,True,False,False,False,True,True,True,True,True,False,False,True,False,False,True,True,False,False,True,False,False,False,False,True,False,True,False,False,False,False,True,False,False,True,False,False,False,True,True,False,True,True,True,False,True,True,True,True,True,False,True,True,False,True,True,True,False,True,True,False,True,True,False,False,False,False,False,True,False,True,True,True,False,False,True,True,True,False,False,False,False,True,False,True,False,True,False,False,False,True,False,True,False,True,True,True,True,True,False,True,False,True,True,False,True,False,True,True,True,True,True,True,False,True,False,False,False,False,False,False,False,True,False,False,False,True,True,True,True,True,True,True,False,False,False,False,False,True,True,True,True,False,True,True,False,True,False,False,False,False,True,False,True,True,False,True,False,False,True,True,True,False,True,False,False,True,False,False,False,True,False,True,True,True,True,True,False,True,False,False,True,True,False,True,False,True,False,False,True,True,False,False,True,True,False,True,False,False,False,False,True,False,False,True,True,True,False,True,False,False,False,True,True,False,False,True,True,True,False,False,False,False,True,False,True,True,True,True,False,True,True,True,True,True,False,False,False,True,False,False,True,False,False,True,False,False,False,False,True,False,False,False,False,True,False,True,True,True,False,True,True,False,False,False,True,True,True,False,False,True,False,True,True,False,False,True,True,True,True,False,True,False,False,False,True,False,True,False,False,False,True,True,False,False,True,True,True,False,True,True,True,False,False,False,False,True,False,True,False,True,False,True,True,False,True,True,True,True,True,True,True,True,False,True,True,True,False,False,False,False,True,True,False,True,False,False,False,False,False,False,True,False,False,True,False,True,False,True,False,True,False,True,False,False,False,True,False,True,True,False,True,False,True,True,False,True,True,False,True,True,True,True,True,True,False,False,False,False,True,True,True,False,False,False,False,True,True,False,False,True,False,True,True,False,False,True,True,True,False,True,True,True,False,False,False,False,False,False,False,False,True,True,False,False,True,False,True,True,True,True,False,True,False,True,True,False,True,True,True,True,False,False,False,False,True,False,False,True,False,False,True,False,True,True,False,True,False,True,False,True,False,False,False,False,True,False,False,False,True,True,True,True,False,True,True,True,True,True,False,False,True,False,False,False,True,False,True,True,True,True,False,True,True,True,True,True,True,True,True,False,False,True,True,False,False,False,True,False,True,False,False,False,False,False,False,True,False,False,True,True,True,True,False,True,False,True,False,True,False,True,True,False,False,False,True,True,False,False,True,True,False,True,True,False,True,False,False,True,False,True,False,True,False,False,False,True,True,False,False,True,False,False,True,False,False,False,True,True,True], dtype = "bool")#candidate|6464|(896,)|const|bool
bop_6465 = relay.logical_xor(var_6461.astype('int16'), relay.reshape(const_6464.astype('int16'), relay.shape_of(var_6461))) # shape=(896,)
bop_6468 = relay.subtract(var_6449.astype('uint16'), const_6464.astype('uint16')) # shape=(845, 896)
output = relay.Tuple([call_6439,call_6448,var_6450,const_6451,call_6458,const_6459,var_6460,bop_6465,bop_6468,])
output2 = relay.Tuple([call_6440,call_6452,var_6450,const_6451,call_6462,const_6459,var_6460,bop_6465,bop_6468,])
func_6478 = relay.Function([var_6449,var_6450,var_6460,var_6461,], output)
mod['func_6478'] = func_6478
mod = relay.transform.InferType()(mod)
var_6479 = relay.var("var_6479", dtype = "int64", shape = (845, 1))#candidate|6479|(845, 1)|var|int64
var_6480 = relay.var("var_6480", dtype = "float32", shape = (180, 1))#candidate|6480|(180, 1)|var|float32
var_6481 = relay.var("var_6481", dtype = "int8", shape = ())#candidate|6481|()|var|int8
var_6482 = relay.var("var_6482", dtype = "bool", shape = (896,))#candidate|6482|(896,)|var|bool
output = func_6478(var_6479,var_6480,var_6481,var_6482,)
func_6483 = relay.Function([var_6479,var_6480,var_6481,var_6482,], output)
mutated_mod['func_6483'] = func_6483
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4089_call = mod.get_global_var('func_4089')
func_4091_call = mutated_mod.get_global_var('func_4091')
call_6488 = func_4089_call()
call_6489 = func_4089_call()
output = call_6488
output2 = call_6489
func_6490 = relay.Function([], output)
mod['func_6490'] = func_6490
mod = relay.transform.InferType()(mod)
output = func_6490()
func_6491 = relay.Function([], output)
mutated_mod['func_6491'] = func_6491
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5389_call = mod.get_global_var('func_5389')
func_5390_call = mutated_mod.get_global_var('func_5390')
call_6557 = relay.TupleGetItem(func_5389_call(), 0)
call_6558 = relay.TupleGetItem(func_5390_call(), 0)
output = call_6557
output2 = call_6558
func_6562 = relay.Function([], output)
mod['func_6562'] = func_6562
mod = relay.transform.InferType()(mod)
output = func_6562()
func_6563 = relay.Function([], output)
mutated_mod['func_6563'] = func_6563
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5732_call = mod.get_global_var('func_5732')
func_5733_call = mutated_mod.get_global_var('func_5733')
call_6578 = relay.TupleGetItem(func_5732_call(), 0)
call_6579 = relay.TupleGetItem(func_5733_call(), 0)
output = relay.Tuple([call_6578,])
output2 = relay.Tuple([call_6579,])
func_6581 = relay.Function([], output)
mod['func_6581'] = func_6581
mod = relay.transform.InferType()(mod)
output = func_6581()
func_6582 = relay.Function([], output)
mutated_mod['func_6582'] = func_6582
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6173_call = mod.get_global_var('func_6173')
func_6175_call = mutated_mod.get_global_var('func_6175')
call_6589 = func_6173_call()
call_6590 = func_6173_call()
func_3973_call = mod.get_global_var('func_3973')
func_3977_call = mutated_mod.get_global_var('func_3977')
call_6596 = func_3973_call(relay.reshape(call_6589.astype('float32'), [11, 14, 12]), relay.reshape(call_6589.astype('bool'), [11, 14, 12]), )
call_6597 = func_3973_call(relay.reshape(call_6589.astype('float32'), [11, 14, 12]), relay.reshape(call_6589.astype('bool'), [11, 14, 12]), )
output = relay.Tuple([call_6589,call_6596,])
output2 = relay.Tuple([call_6590,call_6597,])
func_6610 = relay.Function([], output)
mod['func_6610'] = func_6610
mod = relay.transform.InferType()(mod)
output = func_6610()
func_6611 = relay.Function([], output)
mutated_mod['func_6611'] = func_6611
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4800_call = mod.get_global_var('func_4800')
func_4802_call = mutated_mod.get_global_var('func_4802')
call_6630 = func_4800_call()
call_6631 = func_4800_call()
func_5799_call = mod.get_global_var('func_5799')
func_5801_call = mutated_mod.get_global_var('func_5801')
var_6635 = relay.var("var_6635", dtype = "bool", shape = (28, 32))#candidate|6635|(28, 32)|var|bool
call_6634 = relay.TupleGetItem(func_5799_call(relay.reshape(var_6635.astype('bool'), [28, 32])), 1)
call_6636 = relay.TupleGetItem(func_5801_call(relay.reshape(var_6635.astype('bool'), [28, 32])), 1)
const_6652 = relay.const([[[-6.944582,1.998103,-2.644307,6.195843,-6.319569,-8.678864,-9.719753,-3.974617,-4.006324,8.438248,4.616278,3.868083],[9.826332,3.592474,8.505098,5.811317,-6.092156,5.301740,9.006201,1.875724,2.617587,-3.347542,5.242130,1.795941],[3.390570,3.963833,8.625885,-4.260858,1.320449,-6.959835,-6.496205,5.713666,-4.809525,5.486491,1.911344,5.719931],[-7.445397,5.361345,-0.310854,1.053620,2.730327,-1.001221,-3.418463,6.453298,1.332364,-2.266849,-9.563546,-9.071075],[4.965635,-2.253070,-3.393263,7.081568,4.824161,-3.860226,-1.592398,9.978213,-9.215736,-2.914882,-2.010354,3.827192],[2.260456,9.666424,3.867463,-4.554152,8.230439,6.678041,-0.036233,-5.151225,5.039869,-9.327801,3.203294,-5.928117],[2.218439,-6.906363,-8.298477,1.620226,3.551316,3.296376,-2.572533,6.764918,4.453068,-4.390342,-5.135662,5.227122],[0.911694,3.687649,-5.720368,0.333072,-9.194327,4.682744,3.650519,6.530946,-5.182898,5.161541,-3.686658,-3.154476],[8.671461,-4.084317,-4.407739,-6.328574,1.749976,-9.836959,6.393480,8.321514,4.431815,-0.205143,-3.012442,2.267461],[4.201717,3.049517,-6.987915,6.524869,-9.309174,0.421085,7.960164,0.978091,2.794721,-4.686248,4.935755,-9.526908],[9.357245,5.944234,-2.309072,-2.809671,6.321346,-0.179171,5.859628,2.995404,9.196344,-1.072380,-5.507442,9.350585],[2.196476,-9.669676,1.284673,8.212443,-7.713476,-4.477209,-3.691397,-0.262819,8.649380,0.426705,-7.541479,-1.825779],[8.460841,-5.129252,-4.750082,4.430299,-0.939506,-0.932719,-4.432413,-9.776645,-2.821095,-2.854469,1.795660,-4.481827],[8.200474,2.777718,2.011282,4.791768,7.430888,-5.643709,4.608808,7.526950,-4.325260,0.588791,-2.815103,6.105614]],[[9.567519,2.702215,-9.858663,7.112434,4.005434,4.320404,-7.924666,2.762264,-0.328845,-6.922811,4.796349,6.739567],[4.530034,-7.029879,-8.091629,8.321861,3.251564,-4.375822,-4.313714,9.260135,1.069269,-3.432789,2.192030,8.195187],[-0.893598,8.899553,1.053798,9.880821,-7.087410,-3.543957,1.395416,-0.678362,-9.032027,-8.046859,-6.461972,-1.382210],[-5.176592,9.244443,-9.768456,6.027845,-7.088339,-6.314809,-5.302968,1.840572,-3.463132,6.880411,1.634675,-5.446076],[8.413876,-1.843028,9.522825,1.528504,-0.927850,4.766937,3.448703,4.688262,-8.444335,1.129305,3.541396,3.626330],[0.056235,3.916611,-5.930054,-1.775755,-9.991986,8.986967,-2.040084,6.017007,3.870583,7.735602,1.938738,6.710818],[5.907232,-6.192033,2.524560,-0.336834,1.108198,1.398363,3.926604,7.388792,-1.398149,7.818026,9.099172,9.293196],[-7.464512,2.873986,5.526207,8.046674,9.396436,7.159004,5.317745,2.922743,8.032337,-1.380300,6.678457,-5.817660],[-2.407814,-2.283260,-1.384878,-6.957749,-5.585875,3.211091,-5.764848,-1.625725,-9.509216,-1.120367,5.275607,-1.398248],[-1.340254,-8.886906,-1.071971,-3.862389,-9.300499,-4.054575,-0.365679,0.210584,-1.963925,9.327774,6.747490,3.285171],[9.817244,0.828229,0.966553,-3.713954,-2.687242,9.420759,3.997869,9.952501,-9.178981,9.263431,7.146680,-2.615035],[0.379354,-3.823515,1.483129,-5.573749,-8.888073,-2.016176,-7.179849,5.990848,5.855209,7.744530,-2.030895,-9.608136],[5.394090,-3.673758,3.484825,-1.650950,-7.645862,8.920598,-2.674275,-7.571893,-8.314791,9.472820,4.266487,5.739997],[0.593796,-3.276913,-2.909915,5.568257,-4.220038,-0.027850,-9.882756,-4.463926,8.042489,-2.166778,1.945398,-7.863104]],[[0.070902,-2.980470,0.548008,6.668564,6.917013,-7.845938,7.651078,8.115375,5.075783,8.350650,-3.065914,-7.114435],[8.351418,-4.867780,-7.958033,-8.046714,-7.280597,-5.531108,4.229967,-8.765730,5.769808,-5.416725,-1.757148,-6.699651],[6.131297,5.329223,6.000637,0.582502,3.191591,-3.891208,1.644107,0.059171,3.893540,1.355874,-8.572687,1.481347],[-6.648176,-1.159431,1.933395,2.709729,-5.363237,6.433463,-3.497149,-7.340688,-3.005733,4.648048,-7.921742,3.745935],[1.446380,-1.551153,-8.135314,0.898432,7.210450,-2.187041,0.256454,7.988871,-0.219931,7.926771,4.288937,-8.351559],[-5.114980,5.325091,2.933256,7.478258,3.688028,-8.138984,5.888436,6.450350,1.363652,-7.415224,6.477849,-8.678325],[-1.780193,-8.523480,4.589506,7.389209,2.429606,-4.420197,4.480673,9.798127,5.640984,-0.338433,5.830653,3.569640],[7.711482,7.305667,1.040222,3.694098,-5.793596,-8.738004,-8.882547,1.983736,-0.297668,-3.412649,3.591475,0.599970],[0.621355,-6.468981,8.359823,4.324982,6.724356,9.625755,-8.287337,-3.727583,-4.020502,8.985271,-7.832162,-2.710640],[-9.306201,-6.211475,-3.305471,5.494613,4.199679,1.195337,1.347150,-3.514061,0.716250,-7.253202,-0.343578,-9.650817],[9.357824,8.225636,9.997451,-7.332203,3.101142,3.830667,-4.024910,6.669646,-6.135161,-9.569066,-4.211843,-9.385637],[-8.204890,3.601997,6.671706,-1.882808,5.921027,-5.774237,8.771708,3.545828,5.147730,9.359926,7.806013,-5.915563],[7.688842,9.891954,9.839096,8.622491,-1.739941,-7.814818,4.163660,-8.163473,-2.223699,6.027929,-5.067505,-1.011175],[6.608914,9.132908,2.679485,3.318197,3.302048,-5.777767,-7.452408,-3.778561,-4.975492,9.761510,5.157592,6.001509]],[[-6.658881,-5.625942,8.492143,3.298801,-0.786527,4.696739,-5.394797,-3.661591,7.128246,-8.075656,-7.367953,9.464155],[7.142389,-6.732672,-8.002664,-1.013268,-7.920550,7.510393,-6.897468,0.550409,-8.794847,-7.720206,3.581921,-7.596136],[7.893571,-4.407714,1.974920,-8.910048,-0.173404,-3.874242,-5.489732,-0.698293,6.755228,-2.177609,-0.538250,-3.630073],[-1.157793,5.034221,5.751475,2.248552,-8.529377,-4.871976,5.428284,-6.783873,-1.280074,-4.560907,4.010164,9.165405],[2.426771,-0.593450,7.655808,-1.880751,8.746964,0.159352,6.350853,9.186918,8.782148,7.518421,3.355971,-9.043546],[-4.105382,-0.435979,0.932620,-0.221978,-7.252667,-2.927811,4.170143,9.683556,-7.878803,3.247634,6.401221,7.238072],[3.945327,5.079118,-1.681776,-1.907566,8.519534,4.739238,-5.097828,8.341415,-5.587110,8.748432,-7.904771,2.646907],[5.940611,-7.457863,0.912605,5.858481,-6.251682,3.297322,8.110606,-9.176027,4.999296,2.189575,6.374089,-1.290455],[8.669426,-9.360976,-9.672697,-8.550330,-1.760300,0.496406,5.605310,-9.702976,4.352819,-3.289813,4.771846,2.727096],[-2.746449,5.452970,8.020307,-0.010818,0.091846,-7.641940,-0.004998,5.533115,0.544112,-3.419904,-7.702390,1.002174],[9.518000,-0.086623,-9.403200,6.308256,-6.508385,-7.174787,-6.389069,-6.575142,5.496245,8.357913,-6.101641,7.396608],[9.032838,-0.722980,-9.708698,-7.647644,2.772203,0.244957,-8.579341,8.000311,2.852368,3.417129,-6.949099,2.934807],[-4.571034,3.715261,0.440795,5.147039,-7.670398,-9.214773,2.222881,-4.534170,4.697984,-2.168745,-1.537961,3.153527],[9.972961,9.681397,-7.272533,-9.584710,-2.664568,6.623751,-0.220342,-4.934613,-4.105875,4.158049,2.934779,4.396941]],[[8.963579,3.459921,6.225956,9.135984,2.373186,-3.456805,3.899399,-4.873897,-6.813440,-5.071557,-9.529696,8.305143],[3.561113,-6.367732,8.909319,-7.508838,7.916442,-7.757195,-8.033018,-9.768575,0.224252,6.670709,5.247097,-9.396086],[-3.861841,-2.730989,5.820970,0.866029,-0.449190,-7.209033,9.562412,5.601852,-0.761830,1.176951,6.534009,-0.157450],[-6.112696,-8.762244,4.447329,6.908686,7.323357,8.770671,-2.719067,3.478002,-3.660995,-3.193575,-5.119725,8.119692],[9.482426,3.328618,-0.862229,4.593731,-8.887488,-3.961412,-6.500216,8.654463,1.591725,5.980185,9.174415,-2.526554],[-9.983820,-1.370558,-6.853079,6.659846,-0.249875,9.625082,-7.819642,-6.421546,-2.276752,-7.739486,-4.855029,-4.957667],[-0.938607,2.173383,-0.402882,-8.862605,-4.062011,-7.594156,-3.818889,3.625989,-0.108514,7.109486,1.208778,9.926836],[-1.531844,2.198331,6.886576,-3.554257,1.358190,-4.481594,1.073489,-3.911904,0.108235,3.790801,-1.079698,-4.144436],[5.212388,7.622962,2.525436,-6.067923,-8.337486,8.838919,8.727141,-9.411894,2.469123,-4.206561,0.802698,3.740633],[9.529041,-6.782146,1.311736,1.812049,-8.808685,2.686287,3.977270,0.541346,5.019097,-0.435197,-2.055795,9.177128],[5.681335,-5.987389,-8.341790,5.653656,-0.827526,2.291740,-6.826314,-9.504483,2.985338,3.176854,6.835178,4.345527],[9.528445,7.296712,-6.782601,5.356236,9.282594,-4.594520,3.886310,1.305128,1.492821,0.567778,4.265876,-3.464762],[-9.055501,-3.913394,-6.553705,-9.497033,1.317102,7.410600,4.589914,8.802610,-7.848004,-7.760777,7.222597,-3.567211],[7.138739,-0.018830,0.485724,1.511172,-5.119323,-2.118114,7.853339,-5.084109,-8.322568,-5.096494,0.854165,-7.784681]],[[5.129539,5.857441,9.952521,2.221426,-0.226554,0.174785,-7.682310,1.109151,-9.115372,1.313329,-6.801211,-9.976299],[4.772297,-6.687437,-6.348898,9.760591,-3.339259,-2.794775,-7.584704,-4.048490,-9.585894,-1.556187,-6.269002,3.529966],[3.983515,4.073137,3.842954,2.191989,-6.591381,8.471185,-3.935926,1.009909,5.768949,-4.256531,2.655798,-6.324012],[4.532270,1.681348,-3.406130,-0.524106,7.625880,-5.065172,-4.561380,-5.254098,6.497355,6.301075,-0.840702,-2.837572],[0.013238,1.804815,2.171700,-8.436439,-5.896026,8.908541,-7.806837,7.530781,1.437741,-3.821263,4.650357,-9.126256],[-4.841076,-4.955685,-0.708385,5.691866,-9.586526,6.868075,-2.250344,-9.618570,9.536576,-7.210597,8.655827,5.662451],[2.986095,-1.510720,-5.630213,2.186082,6.605838,6.861002,7.276544,5.935281,1.112051,3.788915,-1.302043,4.382516],[0.986362,2.028757,5.265563,4.616480,4.452198,8.123264,5.406050,-8.369687,-0.189979,-4.145540,-3.628370,7.481684],[-5.308913,-7.438548,-1.439441,-4.134291,6.208480,5.352703,6.981838,6.090227,-9.625742,-3.305983,9.846476,-2.700920],[8.633337,8.994820,-2.074206,3.278057,-2.138201,4.232763,4.774793,-6.044365,-7.238752,6.711288,9.223548,-7.989907],[3.794624,8.864716,2.918093,6.997065,-7.703188,5.501133,0.980904,-7.921511,-8.037779,9.971718,4.954930,-4.520781],[8.784257,6.625923,-6.749214,-7.126828,0.577568,-2.058859,-6.927686,1.968499,6.049390,6.392406,3.734347,-7.898900],[-6.193242,-9.290791,9.075466,8.649762,-1.368834,0.639526,-1.685781,4.581746,3.257472,-7.735397,6.917638,9.329084],[-2.564699,3.869619,-2.372021,7.328547,2.426069,-4.731430,-6.049342,5.611931,0.703816,8.443004,0.401067,8.723862]],[[2.302758,-5.164276,7.623881,4.521632,-7.937984,8.193817,-5.552491,4.712663,-9.236049,-8.499005,4.369110,-1.432806],[6.594733,-4.931051,-7.677287,8.315685,-2.362785,-5.899241,1.900297,6.731277,-3.906886,-5.024259,-8.512607,0.141351],[-2.538983,0.314211,4.949461,-4.028167,-2.096520,8.389962,-8.263150,-7.413185,-1.212665,-7.582571,-9.061542,-6.843267],[-7.740009,6.023505,-2.832541,-7.657329,-1.626412,3.501655,2.786434,-0.393846,-2.195373,-5.875290,0.168798,0.724685],[4.522191,8.325577,-3.497439,-9.242307,1.506035,9.134820,-7.652485,-1.422371,8.524160,4.570614,3.155458,-4.293192],[8.121695,-9.563513,4.768411,3.730858,6.934440,-1.685718,-6.897453,-2.535918,-5.571747,5.833706,9.793575,-7.793764],[3.760154,3.105117,6.030692,3.880595,-3.191695,7.178901,4.590494,-9.916859,-7.394059,-6.881602,-5.830185,-7.248034],[-3.691004,8.337826,3.024840,7.135288,5.208036,2.511534,-8.466037,-6.359808,-3.713907,2.936849,-4.937721,-1.660626],[-7.677439,7.499094,5.108783,-4.479190,2.818964,-4.139910,7.177717,-1.244883,-3.158095,1.239269,-5.544498,-0.615878],[-0.328963,-7.050658,7.910465,4.161294,-3.859091,-3.928327,-6.201787,5.150802,1.734141,-2.182536,4.117173,1.974234],[-5.517908,7.685744,-2.163612,3.702442,1.305777,2.571632,-3.282547,-6.525569,4.961916,-5.429456,3.579511,-2.710601],[3.484063,3.192265,5.358149,5.913705,-9.835670,-1.977600,-6.581974,4.424541,6.972746,-4.727559,4.448103,-4.081866],[-2.831432,-1.566226,2.806296,-1.198626,1.820219,4.008785,-0.090180,-3.431853,5.003617,-7.731828,-4.231834,0.710796],[-4.754720,5.765052,0.736513,3.672063,-0.129900,7.212106,-3.732835,9.765399,-1.427269,-2.811147,0.608561,6.085404]],[[7.518998,-6.787547,4.939795,4.616193,2.893371,0.443992,0.372095,-0.225395,-7.180930,5.015623,4.106929,-3.538392],[3.487416,0.550664,3.032414,-2.097020,-4.053953,-5.501413,-7.865496,8.670378,-0.423602,-9.682134,4.985859,3.739580],[1.767943,-4.299321,9.238850,-7.682490,8.528241,8.898921,-1.836276,6.340301,-1.589403,-4.970610,-5.288537,6.976157],[-8.529725,-6.951674,-5.587254,3.530690,-4.085856,0.413107,-4.148074,-0.716227,0.433873,-0.493003,0.120517,-6.141210],[4.792023,6.034112,-8.043829,-7.730630,-9.217480,8.419944,-8.261453,-4.172871,-4.814211,8.436855,5.846819,4.024093],[5.769715,-6.661089,9.763898,1.430745,6.456191,-5.650535,1.244502,-6.295836,7.375667,-2.955582,-5.368498,-8.754258],[-1.943161,9.858591,-9.029530,-1.503159,-2.139887,-6.668753,9.581174,-4.816091,-5.520440,7.449806,5.887484,-3.363785],[0.081167,9.071848,0.051308,-2.181881,8.330138,-4.199756,-1.017983,3.804246,3.865658,3.063695,9.593790,-0.103609],[-6.417173,1.779621,8.886784,9.908034,6.372588,1.320329,-8.111406,-3.672674,7.184573,1.581736,-8.984296,4.648343],[0.192013,-0.822530,-7.631619,-7.718468,-8.040055,2.727614,5.883070,-4.865888,8.317372,-2.053337,-7.036881,4.593238],[3.555743,1.581573,0.292027,6.353311,7.874807,-7.654155,-4.997875,1.332609,-9.786480,0.603850,7.159983,-5.714889],[0.786533,-6.186125,-0.118227,1.939725,9.997119,9.162176,7.130539,7.308462,-1.308990,1.285190,-7.996666,-8.923752],[4.437742,9.324390,2.708443,0.445976,-6.603775,-9.786931,0.662905,-5.711671,2.868244,8.703782,-9.438852,9.126378],[-9.903371,-6.695718,8.124778,-4.600424,-9.945615,8.335885,2.309757,-7.739309,5.097177,-4.361093,-1.177799,1.549884]],[[-8.076770,5.086196,4.428963,-0.835906,6.180164,-5.829373,4.995121,1.004735,-1.428615,3.408003,5.597694,7.743480],[1.534067,7.384263,-3.989302,2.113400,9.343767,-7.822944,2.075609,1.712945,9.741084,-1.645922,-7.593726,-4.164396],[-0.379140,-4.087794,6.161650,-8.894272,-2.882553,-4.397854,-4.892690,2.584177,-9.937766,-9.807712,-7.824327,-8.352848],[-3.669376,-6.578971,-8.531040,9.811126,6.595049,-4.781819,-9.819599,7.410862,-4.565556,8.176942,1.892171,6.926996],[-5.287347,7.285323,2.032324,-9.408439,-8.744184,-8.788267,7.118852,-3.031343,7.458266,4.804903,3.382778,-6.404908],[0.452080,2.314514,0.663963,-8.846050,-9.131772,-6.961479,-9.344814,5.253333,-8.955788,9.672102,-1.583419,-0.209506],[1.344598,3.521248,-5.012171,-4.599686,5.281749,-1.128670,-4.859155,7.701726,-9.125948,-8.054677,-6.319880,-2.538322],[9.360911,2.012608,6.737697,-5.144799,3.124563,9.136959,0.053864,3.109919,9.139784,0.627463,7.110270,4.920381],[3.813666,-1.426093,1.545702,-2.622600,-5.933069,-1.540818,5.543918,-0.608256,-7.063910,-8.441948,-6.133768,1.973748],[8.004932,5.663416,4.137636,-3.364866,6.812535,-5.739418,8.092540,5.751411,-7.421242,9.136554,-1.565043,8.217067],[-4.548055,7.406335,9.223933,-4.422191,1.874925,2.875273,-7.974642,3.685428,-3.311257,5.374092,-1.225899,-2.284050],[-6.705481,-4.959832,3.340714,-0.190373,2.503357,-6.737486,-7.806655,6.267437,6.607485,-9.050004,0.429952,0.379176],[6.286927,6.228504,2.524218,8.031063,-4.910024,2.668205,5.390048,0.314206,2.473647,1.898482,-7.283636,0.867897],[-7.737161,-6.405912,-5.921308,8.605328,-5.702302,2.024463,-1.028162,8.881767,0.653535,8.332066,-0.062736,8.778225]],[[-7.950546,7.226871,-4.054147,-8.542351,-5.120511,-0.500324,-3.135677,3.398252,-5.231607,2.409885,0.194968,1.016418],[5.311895,6.634759,9.939475,5.718597,5.911604,2.403912,8.197419,-1.751155,-4.552292,-5.724306,6.549268,4.940896],[1.152046,-7.397778,5.680405,2.559178,-5.473997,4.567641,2.488231,-3.986785,8.846223,-2.772814,5.458268,5.723421],[5.449994,9.113395,6.424013,3.999310,5.183269,3.672957,0.063584,8.667915,4.107645,-6.634247,5.438771,1.900545],[-5.648850,2.523526,7.311195,1.638921,8.851462,2.205076,2.129155,1.784465,-3.326354,1.885712,8.187331,-8.652436],[2.364290,2.938501,2.645986,-2.590541,0.486620,6.813401,-7.339946,0.573686,3.262136,-3.130968,9.812348,5.489748],[-7.464269,-6.796827,0.290265,-2.693021,3.656223,1.095622,-0.761239,-6.838458,-8.608256,-6.757687,-5.642687,-1.874610],[-8.800958,-2.103552,-3.662485,-4.151366,-4.306055,-0.870261,8.536427,7.381317,-7.848230,6.478885,-4.158874,-5.041818],[5.224636,6.941631,3.846426,-5.290330,-0.290806,3.434490,-7.540210,4.442151,-8.419116,4.522629,-9.871119,-4.568263],[6.520936,7.470396,8.193858,-7.144756,4.346666,-1.383874,8.892913,-1.148312,9.870578,-8.143493,9.074765,7.878982],[9.784881,4.816884,6.626390,1.370548,0.974098,-1.957221,-4.849154,-3.277877,-1.131233,-9.919168,8.878960,7.375416],[4.746789,-8.332045,4.176092,-6.967958,-1.829242,-2.568115,-9.776713,3.786760,-3.587607,-8.552064,-2.853179,-2.313566],[-3.227897,7.864480,-6.475831,-2.676184,-4.860353,-7.444435,-7.535376,4.420511,4.262928,-0.870422,2.157059,0.514371],[0.420773,-3.147852,-9.900618,-9.265862,-7.626758,-5.693550,-7.420345,-8.015862,-9.628719,-7.930135,5.762582,7.202926]],[[7.862394,-8.857365,1.824233,1.987304,-2.001708,2.128900,-5.871549,1.629981,8.735019,7.583576,-5.695879,-1.676340],[4.878670,-2.130286,-5.070476,1.357713,8.086037,-0.667403,3.997614,-7.344974,-7.291792,1.400246,7.140254,6.636447],[-8.790225,5.546620,-7.411209,9.744362,-6.813965,-1.355026,-5.901086,9.532595,-3.485807,-4.607770,0.581590,7.807305],[-2.532061,-3.868097,1.534196,-5.362226,3.315205,-3.044495,-0.305243,6.428341,3.458938,3.115081,4.500373,-9.779486],[5.216480,8.280279,9.789704,-0.213549,2.826948,4.779093,-6.805216,3.023000,1.426227,9.017582,3.204033,9.030071],[-3.452096,-3.521981,2.933163,3.022315,-9.519140,1.517245,8.444075,8.902881,-0.968505,0.199952,7.401323,-0.494514],[9.976219,-2.894038,-7.545262,2.919895,-7.114973,-1.179431,-5.308048,-0.430028,4.079048,-8.954227,7.086078,1.143872],[2.839023,-3.586261,6.408735,0.733177,-5.168834,-6.946181,2.971293,-2.125488,4.718744,5.235391,-9.706319,-7.492536],[5.085387,5.259048,3.287132,9.229822,8.875865,7.234717,-0.485189,6.878517,-1.983850,-3.808718,-6.593957,2.158696],[3.017803,9.117220,6.724212,6.937826,5.097072,4.276130,-4.303261,9.035338,9.307076,-7.759082,5.113795,-2.132418],[8.952752,-5.741203,3.583831,-4.316681,-3.680651,4.500946,8.900283,3.552008,3.150018,1.613045,1.929835,1.714758],[6.689173,-1.908240,-1.956782,-5.095281,5.514073,9.351893,3.074684,-5.566297,5.355106,3.090473,-7.832750,8.820508],[4.695363,3.423879,9.597751,2.238716,0.987521,-3.298551,0.792504,3.726291,8.918260,8.500370,-0.443924,-9.421473],[2.312604,8.930509,-7.639069,1.668834,9.376436,-2.181911,-8.971032,-7.774117,-9.996784,6.883362,6.026762,-7.721569]]], dtype = "float32")#candidate|6652|(11, 14, 12)|const|float32
bop_6653 = relay.less(call_6630.astype('bool'), relay.reshape(const_6652.astype('bool'), relay.shape_of(call_6630))) # shape=(11, 14, 12)
bop_6656 = relay.less(call_6631.astype('bool'), relay.reshape(const_6652.astype('bool'), relay.shape_of(call_6631))) # shape=(11, 14, 12)
uop_6661 = relay.sigmoid(call_6630.astype('float64')) # shape=(11, 14, 12)
uop_6663 = relay.sigmoid(call_6631.astype('float64')) # shape=(11, 14, 12)
func_3973_call = mod.get_global_var('func_3973')
func_3977_call = mutated_mod.get_global_var('func_3977')
call_6679 = func_3973_call(relay.reshape(call_6630.astype('float32'), [11, 14, 12]), relay.reshape(bop_6653.astype('bool'), [11, 14, 12]), )
call_6680 = func_3973_call(relay.reshape(call_6630.astype('float32'), [11, 14, 12]), relay.reshape(bop_6653.astype('bool'), [11, 14, 12]), )
func_5997_call = mod.get_global_var('func_5997')
func_5999_call = mutated_mod.get_global_var('func_5999')
call_6696 = relay.TupleGetItem(func_5997_call(), 0)
call_6697 = relay.TupleGetItem(func_5999_call(), 0)
output = relay.Tuple([call_6634,var_6635,bop_6653,uop_6661,call_6679,call_6696,])
output2 = relay.Tuple([call_6636,var_6635,bop_6656,uop_6663,call_6680,call_6697,])
func_6700 = relay.Function([var_6635,], output)
mod['func_6700'] = func_6700
mod = relay.transform.InferType()(mod)
mutated_mod['func_6700'] = func_6700
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6701 = relay.var("var_6701", dtype = "bool", shape = (28, 32))#candidate|6701|(28, 32)|var|bool
func_6700_call = mutated_mod.get_global_var('func_6700')
call_6702 = func_6700_call(var_6701)
output = call_6702
func_6703 = relay.Function([var_6701], output)
mutated_mod['func_6703'] = func_6703
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3874_call = mod.get_global_var('func_3874')
func_3875_call = mutated_mod.get_global_var('func_3875')
call_6768 = func_3874_call()
call_6769 = func_3874_call()
output = relay.Tuple([call_6768,])
output2 = relay.Tuple([call_6769,])
func_6775 = relay.Function([], output)
mod['func_6775'] = func_6775
mod = relay.transform.InferType()(mod)
mutated_mod['func_6775'] = func_6775
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6775_call = mutated_mod.get_global_var('func_6775')
call_6776 = func_6775_call()
output = call_6776
func_6777 = relay.Function([], output)
mutated_mod['func_6777'] = func_6777
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6784 = relay.var("var_6784", dtype = "uint32", shape = ())#candidate|6784|()|var|uint32
const_6785 = relay.const([[[-7,-6,-9,-3,4,8,9,2,-5,-10,4],[6,-9,-8,7,7,-10,-6,2,7,-9,-1]],[[-10,-10,-8,5,-4,-5,-4,-8,-8,5,-9],[-6,-10,6,7,-10,2,3,10,3,9,-7]],[[-9,-3,9,5,-1,-9,-6,-2,6,-2,-2],[10,3,6,-9,6,-9,7,9,7,4,10]],[[-5,-5,-4,1,1,8,5,7,-8,-6,-4],[-6,-6,2,9,2,-6,-4,1,6,7,10]],[[-9,-7,-2,5,-5,-8,4,-3,-1,8,9],[8,7,5,-6,-5,-4,2,-7,-9,-10,5]],[[6,-8,2,-4,5,-4,4,6,6,6,6],[-3,7,-7,-10,2,2,-3,-5,9,1,-4]],[[-5,-6,4,1,2,-4,8,7,-6,4,-8],[-4,5,2,-7,10,7,-2,-10,2,9,-10]],[[-9,-4,7,-3,-6,7,-10,-9,5,8,-9],[-2,7,10,10,-10,-8,-2,-4,-9,3,4]]], dtype = "uint32")#candidate|6785|(8, 2, 11)|const|uint32
bop_6786 = relay.bitwise_and(var_6784.astype('uint32'), const_6785.astype('uint32')) # shape=(8, 2, 11)
func_5732_call = mod.get_global_var('func_5732')
func_5733_call = mutated_mod.get_global_var('func_5733')
call_6789 = relay.TupleGetItem(func_5732_call(), 0)
call_6790 = relay.TupleGetItem(func_5733_call(), 0)
func_5878_call = mod.get_global_var('func_5878')
func_5882_call = mutated_mod.get_global_var('func_5882')
var_6799 = relay.var("var_6799", dtype = "uint16", shape = (30, 70))#candidate|6799|(30, 70)|var|uint16
call_6798 = func_5878_call(relay.reshape(var_6799.astype('uint16'), [15, 14, 10]), relay.reshape(var_6799.astype('uint16'), [15, 14, 10]), )
call_6800 = func_5878_call(relay.reshape(var_6799.astype('uint16'), [15, 14, 10]), relay.reshape(var_6799.astype('uint16'), [15, 14, 10]), )
output = relay.Tuple([bop_6786,call_6789,call_6798,var_6799,])
output2 = relay.Tuple([bop_6786,call_6790,call_6800,var_6799,])
func_6827 = relay.Function([var_6784,var_6799,], output)
mod['func_6827'] = func_6827
mod = relay.transform.InferType()(mod)
var_6828 = relay.var("var_6828", dtype = "uint32", shape = ())#candidate|6828|()|var|uint32
var_6829 = relay.var("var_6829", dtype = "uint16", shape = (30, 70))#candidate|6829|(30, 70)|var|uint16
output = func_6827(var_6828,var_6829,)
func_6830 = relay.Function([var_6828,var_6829,], output)
mutated_mod['func_6830'] = func_6830
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3874_call = mod.get_global_var('func_3874')
func_3875_call = mutated_mod.get_global_var('func_3875')
call_6880 = func_3874_call()
call_6881 = func_3874_call()
var_6894 = relay.var("var_6894", dtype = "float32", shape = (11, 14, 12))#candidate|6894|(11, 14, 12)|var|float32
bop_6895 = relay.subtract(call_6880.astype('uint8'), relay.reshape(var_6894.astype('uint8'), relay.shape_of(call_6880))) # shape=(11, 14, 12)
bop_6898 = relay.subtract(call_6881.astype('uint8'), relay.reshape(var_6894.astype('uint8'), relay.shape_of(call_6881))) # shape=(11, 14, 12)
output = relay.Tuple([bop_6895,])
output2 = relay.Tuple([bop_6898,])
func_6902 = relay.Function([var_6894,], output)
mod['func_6902'] = func_6902
mod = relay.transform.InferType()(mod)
mutated_mod['func_6902'] = func_6902
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6903 = relay.var("var_6903", dtype = "float32", shape = (11, 14, 12))#candidate|6903|(11, 14, 12)|var|float32
func_6902_call = mutated_mod.get_global_var('func_6902')
call_6904 = func_6902_call(var_6903)
output = call_6904
func_6905 = relay.Function([var_6903], output)
mutated_mod['func_6905'] = func_6905
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6233_call = mod.get_global_var('func_6233')
func_6234_call = mutated_mod.get_global_var('func_6234')
call_6920 = func_6233_call()
call_6921 = func_6233_call()
output = relay.Tuple([call_6920,])
output2 = relay.Tuple([call_6921,])
func_6924 = relay.Function([], output)
mod['func_6924'] = func_6924
mod = relay.transform.InferType()(mod)
mutated_mod['func_6924'] = func_6924
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6924_call = mutated_mod.get_global_var('func_6924')
call_6925 = func_6924_call()
output = call_6925
func_6926 = relay.Function([], output)
mutated_mod['func_6926'] = func_6926
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5240_call = mod.get_global_var('func_5240')
func_5242_call = mutated_mod.get_global_var('func_5242')
call_6948 = relay.TupleGetItem(func_5240_call(), 1)
call_6949 = relay.TupleGetItem(func_5242_call(), 1)
func_3874_call = mod.get_global_var('func_3874')
func_3875_call = mutated_mod.get_global_var('func_3875')
call_6953 = func_3874_call()
call_6954 = func_3874_call()
func_6490_call = mod.get_global_var('func_6490')
func_6491_call = mutated_mod.get_global_var('func_6491')
call_6988 = func_6490_call()
call_6989 = func_6490_call()
func_2366_call = mod.get_global_var('func_2366')
func_2371_call = mutated_mod.get_global_var('func_2371')
const_6994 = relay.const([-9,3,-6,-8,7,-1,5,1,-6,8,8,2,-10,-2,7,-10,2,4,10,-5,9,3,5,5,-6,-9], dtype = "int16")#candidate|6994|(26,)|const|int16
var_6995 = relay.var("var_6995", dtype = "float64", shape = (1, 135))#candidate|6995|(1, 135)|var|float64
const_6996 = relay.const([1.932556,7.673896,-7.636767,8.459530,-7.455605,9.899609,-9.348645,-7.466683,-2.932710,1.775664,8.619390,-6.919513,9.088912,-5.938595,-7.246501,4.356753,0.184690,-0.193494,0.556322,5.345103,4.242260,9.953606,7.082907,-8.151619,8.536191,-4.436347,-6.424736,2.592592,7.309799,-4.786560,7.599135,1.545570,-9.272176,-6.715130,-2.667209,-7.823375,-5.601591,2.405386,5.076939,4.731703,7.258380,-7.127912,-3.936122,4.293065,2.761851,9.432266,1.443805,6.192955,8.363739,-3.614347,-3.151945,6.814126,-8.984971,-5.292755,-7.195292,6.084995,2.995663,8.031950,7.125209,0.659846,4.312083,7.720526,8.550488,-1.902820,6.342413,-3.318713,7.303555,-9.643110,9.417195,-6.781776,7.903715,8.932066,5.300308,-3.035344,-6.856339,2.322780,5.774406,-1.810239,-0.403088,5.175625,3.705784,4.587877,9.599127,1.327612,-9.048526,-9.722886,6.821711,-4.318423,6.986718,5.486162,-9.493948,3.841105,9.732554,-9.550662,-1.402488,4.054905,-5.634178,9.969199,9.679888,-9.226591,-5.103396,0.363233,-1.147630,-6.539605,-0.773352,8.257589,-5.859495,-2.793775,1.421139,3.825659,-0.029720,0.271492,5.314178,-1.934928,4.773755,-9.186906,-8.990603,4.939970,2.909543,-2.481359,1.168005,-9.259617,-6.343014,-8.649540,-6.084354,2.736033,-7.046383,1.633796,5.941277,-0.615449,-5.302055,-1.895235,-4.278468,6.017579,9.672201,-6.064308,-5.220829,7.107034,6.434990,-6.684687,4.755581,4.905155,-8.277167,-8.056953,-8.307290,8.395127,0.346469,9.429852,3.461605,-9.513638,-4.229893,-7.234741,0.440049,5.160334,1.879204,-5.563680,-1.355911,-3.020002,-5.373431,-5.313677,-6.668156,2.169043,-1.469493,1.767067,-5.658337,-8.530710,-7.158093,3.043112,-9.014834,3.313988,-3.520917,8.545645,5.099614,8.692302,-9.155319,-1.338020,1.502898,-9.771459,5.267529,-2.901926,8.142863,-9.798995,9.530311,-7.600198,9.815296,1.670666,2.589973,-7.785796,-4.139982,2.550903,0.642542,2.494198,5.943113,-4.406291,-7.095923,-7.202133,-8.651577,0.440520,-8.504691,3.743170,1.864698,2.768328,5.322168,8.916487,-0.795536,-6.917798,9.864348,-8.317452,-3.843031,3.818986], dtype = "float32")#candidate|6996|(210,)|const|float32
const_6997 = relay.const([[0.589765,0.832523,-5.010994,0.807680,-9.286788,9.268140,3.922625,-2.732608,-6.751215],[3.711537,-1.223292,4.642981,-9.610164,-7.689652,-4.149084,4.583226,4.092946,8.763284],[6.223670,-2.071434,4.345114,-7.321765,2.607755,6.039263,-3.936509,-1.621230,-6.167656],[-8.273648,0.490840,1.299284,4.241134,4.607001,-8.419301,9.770883,-4.626786,4.863890],[6.778553,-1.530440,-2.132331,-6.437096,-3.899949,1.153383,7.081732,-3.279617,-8.825172],[-4.567455,-7.628286,5.358196,-6.739686,-0.967954,-3.899099,8.577818,0.527472,-5.070636],[9.114743,-2.132672,7.963514,-3.173857,2.440127,6.328236,-9.042315,-5.685134,-6.383677],[4.568399,-4.401156,0.198987,2.109744,-4.785543,-2.007307,-2.553460,-9.789310,4.458428],[1.125222,-3.624943,-1.913529,-3.050951,8.189765,6.442587,-6.575100,7.299423,1.080264],[3.858080,9.634590,7.520228,-1.252931,0.324982,0.101808,3.415647,-4.749902,6.877412],[7.093042,6.428558,-1.748022,-5.899198,-4.273577,9.791518,-7.363295,-7.010564,1.462167],[5.517981,-6.173597,-5.158731,-6.074492,-7.590218,3.728819,5.663217,5.903047,5.653546],[-5.106349,2.774531,9.007207,-2.441967,2.638734,8.619923,-1.946513,9.675024,1.060943],[-1.437668,4.191504,-7.206958,0.505101,1.799387,7.178361,-8.723684,1.572697,-8.381139],[5.214465,-4.177452,1.422200,5.083571,1.766837,-7.390390,-3.696086,-8.392969,2.604607],[-6.873526,-2.904680,-4.471590,-0.429895,7.457558,-3.649076,9.282203,-1.680916,-7.542255],[3.762409,-1.768774,-6.294207,-6.897142,8.380927,-0.076931,5.614839,2.632990,7.147656],[8.741032,6.021270,3.958360,-0.988937,4.577784,-0.878137,2.558760,8.565803,-9.989863],[-2.233868,-3.470624,0.828634,2.682792,3.005581,6.956273,-6.305287,-9.772764,0.792481],[7.025134,-2.944218,4.519031,-6.634533,1.853401,-9.276131,-0.990897,-2.437469,-4.671426],[5.038378,-5.277536,3.802493,8.274345,1.910262,7.362491,6.999608,-9.581519,3.589780],[6.104406,-8.945654,9.027770,-3.637084,-6.404840,-7.592346,9.285267,-4.919008,-7.530502],[8.026833,1.660835,1.505727,7.342054,8.492232,9.036633,8.593456,-3.666788,9.987751],[-1.387194,7.403763,-4.174093,-3.563460,-7.267539,7.042250,-9.710649,-2.196514,0.322899],[-8.432893,7.071564,1.596663,-2.547770,5.969759,-1.004691,-1.307816,-8.615455,8.352820],[0.827765,-1.553010,-3.205731,-6.680516,-1.341995,-1.559440,-2.651178,7.530797,-5.885089],[-4.351342,5.335335,-1.332729,-3.123087,5.780909,-7.913430,4.754670,-8.529040,2.641252],[-8.040079,9.883955,4.304805,-5.130618,-0.754976,0.863149,-6.357893,8.066080,1.230556],[-6.681330,-2.172755,-5.496897,-5.948608,-4.124731,-7.423693,-7.364234,3.297449,1.892199],[1.448254,-9.123589,5.068512,8.133580,-4.819198,-1.320930,-0.325750,4.221427,-0.350545],[1.027699,-8.909844,5.689486,-4.246792,9.551510,7.836850,-0.461505,-8.788003,-7.586921],[-8.671333,-7.703987,-0.779108,-0.958311,6.419175,1.449388,5.641061,-6.254160,-2.661131],[-7.755087,5.758714,-5.564411,9.471112,-1.083240,8.665735,6.363856,-5.776247,-7.933124],[-6.621324,7.637635,4.010363,8.665523,9.157361,-8.488438,3.125037,-3.532932,-7.641578],[4.726298,9.579611,9.666525,-5.757023,-8.387242,-5.739163,5.808933,5.549326,-4.458363],[6.775183,-4.145866,-4.186191,-2.091859,2.250258,-4.302268,4.118493,2.904610,1.304590],[-8.274615,-5.404191,-6.193702,7.126234,4.359901,-3.275727,5.025386,-8.471327,9.682426],[-4.903952,-9.666339,-0.282663,0.487208,8.427236,4.501748,-3.450420,-6.583783,-5.625452],[4.647032,5.201781,5.292586,3.403759,3.113553,-1.296726,-6.407729,0.560506,-1.329030],[6.879833,0.525473,1.259117,-0.920447,-1.126175,-7.598351,2.258806,4.731522,-2.471981],[3.561902,8.062869,2.101606,2.767237,5.586019,0.807783,-6.673087,9.448781,6.727930],[-6.475858,-1.243684,-3.346354,-4.926332,7.940373,-9.627513,-3.726802,7.408675,4.086380],[7.625072,-3.456366,8.126474,-1.696864,-5.598722,8.225038,-5.992502,8.907879,0.559807],[7.761012,-0.822300,5.504711,6.256106,-7.842159,9.245343,3.590981,-7.847495,4.662933],[4.591838,8.109723,-5.949277,0.493874,8.963481,2.035889,6.186428,-7.921523,8.205626],[-9.724398,5.584842,3.107313,-4.133738,6.154937,-9.307896,-2.855346,-9.251372,-2.265902],[2.303547,-8.156851,-6.287878,5.852954,-5.442532,1.918967,9.970314,-8.168319,-9.327405],[3.314357,2.742609,2.854504,-6.682176,1.834641,-0.070389,8.919411,-3.870456,-2.258611],[4.812979,-0.431270,7.614183,-1.758823,5.973827,0.485735,-4.368292,4.919219,5.399417],[-7.165182,-1.850695,-1.329506,2.966639,-9.889321,3.454446,-2.671387,-7.370700,7.351685],[8.919461,-3.413504,-9.640737,-3.034685,3.203133,-1.807749,7.246503,-3.853725,5.461231],[-8.293225,-6.028600,-2.601694,0.430639,-4.707715,6.837086,8.007494,9.452857,2.509913],[6.021925,4.456656,0.069522,9.048218,-8.781794,3.800181,-5.861614,-6.497512,-5.868909],[8.005477,0.209805,-6.225675,5.326203,9.524518,1.508686,-0.816497,4.823480,7.817267],[-5.899775,0.964039,-5.328701,-6.616662,-1.563638,4.924226,0.225395,-2.879253,6.314526],[3.674996,-0.097279,6.843039,8.855669,-5.348585,9.686540,-4.602128,-1.076726,-0.408441],[-3.933500,5.914036,8.595446,2.518845,0.614347,-2.306096,-7.613436,2.013012,-5.310081],[2.295740,8.233049,-7.697267,4.360721,-6.523870,-1.341873,1.883210,8.434597,5.749464],[0.351046,4.845967,-5.246423,6.091237,3.480704,8.223665,-0.791805,6.592407,-1.974540],[-2.030743,-2.203466,7.146777,-3.733277,3.156803,-8.950355,-6.318141,-5.204510,-6.205706],[2.147934,6.095697,8.865858,4.450913,5.548257,8.479061,-1.566055,-3.920554,-7.810806],[-0.709405,-8.502462,-5.109684,-1.090280,-5.389279,-4.489352,-9.545178,5.830472,-1.163223],[-1.662417,-1.310407,-0.239359,-8.326618,5.154229,-0.014656,-2.466212,-6.636543,-6.999059],[8.033703,-5.210435,2.035163,5.317578,-1.203041,-2.854991,1.785010,-1.335343,-8.870756],[0.504843,-0.137474,0.523467,-8.538235,6.616385,-3.447333,5.646350,-6.289145,-4.977963],[-3.918184,9.837363,-3.254516,4.948127,4.262351,9.958969,-4.765112,-2.330379,8.381733],[0.127201,0.519898,9.441333,6.586904,-8.448252,-2.047101,4.972290,-8.785025,1.308533],[-0.733712,-8.507150,0.382742,-2.568245,-8.257025,-2.319897,-0.792482,2.927637,-3.216745],[-2.466010,9.442051,2.478560,9.636762,-7.054982,-1.425516,-3.770999,-3.349968,-7.849218],[-9.134811,7.742769,0.667642,-2.454178,-4.418845,2.538245,-0.140169,-8.177774,-4.454815]], dtype = "float32")#candidate|6997|(70, 9)|const|float32
call_6993 = relay.TupleGetItem(func_2366_call(relay.reshape(const_6994.astype('int16'), [2, 13, 1]), relay.reshape(var_6995.astype('float64'), [135,]), relay.reshape(const_6996.astype('float32'), [105, 2]), relay.reshape(const_6997.astype('float32'), [630,]), ), 5)
call_6998 = relay.TupleGetItem(func_2371_call(relay.reshape(const_6994.astype('int16'), [2, 13, 1]), relay.reshape(var_6995.astype('float64'), [135,]), relay.reshape(const_6996.astype('float32'), [105, 2]), relay.reshape(const_6997.astype('float32'), [630,]), ), 5)
var_7001 = relay.var("var_7001", dtype = "int16", shape = (26,))#candidate|7001|(26,)|var|int16
bop_7002 = relay.greater_equal(const_6994.astype('bool'), relay.reshape(var_7001.astype('bool'), relay.shape_of(const_6994))) # shape=(26,)
uop_7017 = relay.log10(bop_7002.astype('float64')) # shape=(26,)
output = relay.Tuple([call_6948,call_6953,call_6988,call_6993,var_6995,const_6996,const_6997,uop_7017,])
output2 = relay.Tuple([call_6949,call_6954,call_6989,call_6998,var_6995,const_6996,const_6997,uop_7017,])
func_7019 = relay.Function([var_6995,var_7001,], output)
mod['func_7019'] = func_7019
mod = relay.transform.InferType()(mod)
mutated_mod['func_7019'] = func_7019
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7019_call = mutated_mod.get_global_var('func_7019')
var_7021 = relay.var("var_7021", dtype = "float64", shape = (1, 135))#candidate|7021|(1, 135)|var|float64
var_7022 = relay.var("var_7022", dtype = "int16", shape = (26,))#candidate|7022|(26,)|var|int16
call_7020 = func_7019_call(var_7021,var_7022,)
output = call_7020
func_7023 = relay.Function([var_7021,var_7022,], output)
mutated_mod['func_7023'] = func_7023
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4017_call = mod.get_global_var('func_4017')
func_4018_call = mutated_mod.get_global_var('func_4018')
call_7047 = relay.TupleGetItem(func_4017_call(), 0)
call_7048 = relay.TupleGetItem(func_4018_call(), 0)
output = relay.Tuple([call_7047,])
output2 = relay.Tuple([call_7048,])
func_7063 = relay.Function([], output)
mod['func_7063'] = func_7063
mod = relay.transform.InferType()(mod)
output = func_7063()
func_7064 = relay.Function([], output)
mutated_mod['func_7064'] = func_7064
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5443_call = mod.get_global_var('func_5443')
func_5445_call = mutated_mod.get_global_var('func_5445')
call_7097 = relay.TupleGetItem(func_5443_call(), 1)
call_7098 = relay.TupleGetItem(func_5445_call(), 1)
func_6361_call = mod.get_global_var('func_6361')
func_6364_call = mutated_mod.get_global_var('func_6364')
const_7107 = relay.const([-9.837009,-8.334122,-8.706197,5.119498,8.924217,-8.205125,9.972434,2.685518,-3.624943,-4.524174,-9.909899,0.780699,-6.998389,-1.717395,1.542658,0.139507,3.798940,8.371420,-5.349292,9.686075,-7.074438,-3.761816,8.493185,8.355254,-1.362003,-6.217896,0.684631,-9.590302,9.924633,7.515293,5.266962,-4.987012,8.148105,-4.411632,-4.301877,9.339406,7.454516,-3.788993,-9.615588,8.945706,-8.182118,3.683833,4.025107,9.252899,-3.579000,3.999938,-8.528169,-7.731021,4.444542,3.472768,-7.694363,-0.341984,-2.354789,7.839382,0.257085,6.885518,-4.434672,1.748180,-8.292061,0.905178,9.903216,-6.281252,-0.120454,8.427529,7.030857,-3.592350,-2.700105,-2.731381,3.846763,4.753184,-3.577123,-0.511528,0.196627,-9.374712,2.216969,-6.630692,-4.936983,-7.517185,-2.378086,-6.231523,-2.754227,9.514369,-9.119956,-3.839433,3.792847,-1.377783,-8.876031,6.706376,-6.089408,-5.042282,1.454278,-1.470253,3.343668,-8.052927,1.512207,-7.665121,8.346997,-4.295520,1.499942,-0.510816,-1.503286,-1.224994,6.606592,-4.231121,5.330691,7.981457,2.113547,-6.602574,-3.883153,-3.002573,6.546281,-9.089504,1.564860,-6.845906,2.292452,1.786626,2.806945,-1.554668,9.209699,-7.938472,9.690457,6.406375,-5.677561,-0.915378,1.945885,-7.231074,2.916643,8.936693,2.170888,8.264829,-2.023733,-5.758439,-2.638593,7.912974,9.215619,-5.569495,2.418154,3.610613,2.002023,7.368219,8.870091,3.733240,-8.773323,6.634815,0.755049,-3.555690,2.591219,5.125756,8.779148,-3.895051,5.935786,-6.444802,-5.387095,-8.613161,7.950821,-8.341230,6.562210,1.731347,9.623004,8.600464,0.451526,-7.787745,-0.210698,-0.779978,-7.762715,-7.943464,3.697404,2.291557,-4.991055,5.369387,7.892930,-3.051198,4.764784,-2.952567,-3.891290,7.802058,4.843047,1.047215,-0.575300,8.916064,-9.372991,-6.110615,-6.700181,9.637251,9.694340,-6.869749,1.999335,4.662701,-3.719484,8.688067,4.821431,-7.185615,-4.785023,-3.586966,0.915093,-7.055725,1.972920,6.944124,-1.247519,-3.270964,6.642683,-3.617436,-3.331065,-3.531424,8.650572,0.608059,-5.399505,7.048500,0.868393,5.321592,5.169659,-8.775593,-6.340370,6.062738,0.229453,-5.469445,-9.081114,2.096869,-0.538777,-5.599670,8.067369,-1.043679,0.053743,-2.266043,6.998300,-0.786010,0.070976,7.254542,-5.166456,-7.104187,5.874317,5.461807,9.349038,-0.553336,-9.797299,2.161018,-0.213149,7.873072,7.320832,6.022631,-6.630813,-9.781171,-2.056237,3.258080,-1.367485,-9.402771,1.762807,6.998991,-2.247236,-3.052874,-7.406643,-9.268232,-9.628738,0.526394,-9.305057,-6.957107,-9.776637,-0.258675,2.695581,8.146284,-8.810777,1.139381,9.408999,-1.323530,-0.395009,-1.968627,0.540450,3.943862,5.132351,1.686006,6.077633,-9.076919,-2.402816,9.386518,-3.533862,8.391241,-2.022806,-5.673557,-7.697486,-8.247686,-2.841371,0.266538,7.885752,9.984437,1.566236,-8.931343,-7.364543,-0.779205,-3.953582,-8.636139,2.075735,5.167808,-0.394146,5.434021,-9.979460,1.384372,3.511992,-0.560948,-9.097147,1.864350,3.513324,-1.728378,-0.060006,-8.084425,-5.413865,6.268726,3.321419,-0.998739,3.897471,-2.869016,1.533301,-6.860205,-4.560152,6.863583,-9.840618,9.682824,7.072654,9.984398,-3.008128,-9.236757,6.015252,-5.596933,-2.907964,-8.586233,9.608933,4.479817,8.738903,3.719335,5.144299,-6.881043,7.898596,0.939156,0.084228,-2.725875,-3.059400,6.080036,-0.176946,-5.323027,-6.628993,-9.690605,9.510636,-4.764926,0.186011,7.284089,-0.289758,-9.711102,6.505785,-5.892019,6.416843,-1.094772,5.986962,5.300655,-4.582596,-9.790880,-6.781268,-1.077929,5.532028,-3.249496,-0.080413,0.731140,3.286557,-0.358908,9.723070,-3.822245,8.801970,-4.756540,-5.717698,-6.362783,-0.491498,7.950348,-5.171857,-6.278610,-3.609575,-2.197900,-7.531435,7.433180,-7.493792,-8.088445,0.873208,-8.649083,-2.229088,5.510963,-6.014735,2.776942,7.556636,1.116406,-9.997288,1.653793,8.594717,2.856875,3.875078,9.864844,-2.896363,3.771410,-4.996900,-9.514448,-5.911020,3.809585,7.282264,1.130101,3.264213,-0.442687,9.772667,-6.307053,-8.954909,-9.215355,6.837438,6.895881,-6.829588,6.520495,-1.372594,7.429161,8.351359,2.796208,2.292375,5.481480,7.449326,-1.559077,5.928355,9.145529,-3.853186,4.878491,-6.269402,0.807334,7.500983,3.886261,-0.663088,9.827997,-0.786333,-4.162823,3.293917,-7.554945,-0.394306,7.949171,-6.666101,5.659317,9.751507,-5.864170,0.376847,-4.359715,-4.239381,-9.511156,-9.463386,-8.882265,-7.771514,-3.074862,9.318746,-1.094666,8.501832,7.282489,2.134087,-3.895842,-7.497968,-1.516427,-4.568311,-2.906433,-7.094869,9.939459,-6.895588,1.952604,-7.519573,4.226038,7.290492,2.442076,3.660176,-5.289477,7.598066,3.387348,3.397344,6.081858,-9.358338,-2.752448,-4.063737,2.237251,1.120718,7.293527,-6.840096,2.226807,0.906957,-6.849394,-3.460722,9.949701,3.539382,6.745186,-1.382771,-0.953217,-2.870546,1.476312,-2.756516,-4.303847,-9.957195,-6.814882,-6.823456,-8.145845,-9.500924,-8.806220,6.356490,6.710089,2.113050,5.254137,7.614587,-2.581565,-0.634459,8.457561,7.232690,-1.591424,2.307687,-4.863916,0.414239,4.735342,-5.755662,-7.094492,7.129249,-4.140594,-0.399100,-0.064283,-8.226721,3.955132,3.860394,4.576888,-1.012585,-2.316874,-7.421675,5.506174,4.707236,-1.598415,1.710162,1.418974,-3.763497,8.025420,5.024156,-4.308508,-7.965097,-3.359702,-6.621363,-1.994032,9.210008,8.159892,-8.929084,8.834512,8.833943,4.145651,-5.882398,-5.123178,-5.026165,4.583682,6.204855,7.702851,-9.631749,0.396913,-9.482190,5.819803,-4.773013,0.478805,-2.114810,-8.748746,-7.801931,-9.708931,-5.897182,1.208229,-1.522327,-0.292061,0.463500,4.750306,2.526242,-0.107889,0.059444,-5.647052,-6.243712,-9.251276,-1.640064,9.317743,-1.645878,-3.710999,-1.549119,4.037216,-6.059467,-5.514318,-0.973117,9.575602,8.789883,6.889990,-9.386228,-3.786542,4.268392,0.174047,-0.434370,1.985825,-6.952535,2.196262,4.063807,5.789365,9.884654,2.321266,1.345687,2.606353,5.961631,8.145615,-2.926675,-5.132961,-0.780153,-9.087672,-6.616994,4.715864,4.619456,5.472996,-3.594724,-5.961545,3.356187,8.728101,9.021642,5.928070,0.331822,-0.120464,-2.636151,8.543829,-4.953095,4.974297,4.949481,4.868751,-8.090123,-6.420233,5.270358,-3.596747,-0.493257,0.861030,-5.156162,-5.853924,-3.014214,-2.867214,-4.073129,0.237311,4.877109,9.355852,-9.616821,2.572625,-4.576381,3.704545,-4.387905,-6.995539,9.875542,-7.527843,-0.997855,5.446891,7.762395,9.931036,2.263362,-8.164684,-5.253363,-0.910461,-8.483858,0.171813,6.254389,-6.230368,-2.419907,-9.568590,2.075739,9.451262,-9.691797,-9.579182,-0.455745,2.643270,-1.802572,-1.553059,4.792281,5.043456,-0.957394,-8.422910,6.530528,-0.675281,8.844900,3.765416,0.080946,-5.549349,9.153954,-4.694010,2.427418,-0.975553,4.285895,-6.690892,3.840203,9.035507,-2.252284,6.660811,-5.776343,8.004217,-3.470352,-4.814211,7.210863,4.122886,8.097198,6.863118,4.997627,4.841645,-3.031782,-7.500456,9.915164,-6.087576,7.076227,-5.333974,9.558931,-9.271706,-4.731046,8.838453,5.896692,3.704200,-8.233792,5.292063,-6.846553,3.570595,-8.035859,-3.845032,5.936021,2.696523,-4.174024,-6.678064,1.027164,3.671500,-1.990883,-1.586488,-5.139199,-0.552790,-9.571666,-6.140733,-5.785441,3.130910,3.861183,0.204734,-5.705462,-1.033634,-5.632200,-7.016596,7.315457,5.947479,3.898011,3.476497,8.466215,-1.593561,-6.308630,-4.507497,-8.691525,3.811657,6.730050,-9.230353,-9.835308,-3.478404,-7.945452,-9.961220,5.860498,6.886052,7.860424,-3.009509,-1.309182,-2.100096,9.915481,-8.900803,1.194825,-7.476363,-7.300017,-0.885955,3.494942,9.959058,-4.267526,8.214205,6.799960,-6.767379,2.483211,-1.620093,7.204693,-2.318786,9.236799,3.207732,0.765421,-3.116241,-6.525513,-7.058031,1.500109,5.502949,6.193701,7.203222,6.530843,-3.495872,-3.311645,6.734897,1.165302,7.249335,-2.793524,9.786153,-8.488798,4.773808,4.017512,-1.170561,6.444296,-9.825734,-1.723974,2.877167,7.968655,-6.980256,-6.894636,5.044340,-6.365910,4.583800,2.493547,-2.687607,-8.246124,4.588998,6.355505,-3.475388,2.204889,6.475050,3.489298,-5.650415,-0.467922,-4.359153,-6.338659,9.300699,-6.962800,6.451445,5.077447,2.463380,2.208951,7.747856,-9.008049,1.703609,-8.276695,4.252337,7.176451,-7.123584,1.918497,6.027548,8.921407,-0.584254,4.185801,9.733089,1.704123,-7.125545,8.389355,9.008722,4.349500,-7.013673,4.357560,5.871967,1.310334,3.245201,9.569435,-3.733838,3.939895,-7.019694,-9.036261,6.760851,4.836744,-2.464776,-3.607779,-9.861285,-6.743052,1.732898,2.627266,-9.979300,7.958042,5.712573,-7.564886,8.585225,-9.050722,-2.292289,5.197117,-6.862062,4.580091,-0.854230,-9.830295,-1.340718,1.924808,-2.787766,-8.978392,3.269499,-6.934257,-7.174748,-9.130347,-7.238104,-9.809405,7.646531,3.048329,-8.610478,-7.171524,-3.647220,9.447193,2.102902,-3.896123,6.433763,-2.349400,-2.242742,4.135362,-6.958542,-6.437321,-1.673193,0.778893,9.158360,7.499896,-2.128040,-0.559340,-0.477959,7.333891,-6.663338,-2.477929,-1.635584,-0.143567,2.426880,-7.138242,4.720394,1.870789,6.150912,9.378362,9.120217,-8.716908,-3.586238,-5.333910,-5.051369,-3.812752,5.999901,2.045724,0.423902,9.991437,2.392482,-8.463820,-2.294819,3.615415,1.684196,-6.893607,8.343521,-2.656386,4.544087,0.434619,-9.070108,-2.962698,-1.547938,6.190823,4.760748,-4.213878,-6.323690,5.743791,-9.695377,-9.601217,8.808703,-3.446963,6.377309,-8.185481,2.874438,3.247379,6.164891,-6.503009,8.937056,-7.794797,-4.592728,7.260406,5.762940,2.311722,5.300760,9.139741,9.788882,-2.667214,-5.454672,5.077241,-3.732986,5.738764,4.705540,4.393278,-6.304377,2.763734,-7.958939,6.435094,-8.440981,-5.361402,2.511957,-5.414021,1.937512,9.951274,-3.749256,-4.302706,3.088398,-3.735802,2.442253,8.597299,9.508655,-1.103888,-4.809840,-5.976093,-0.384104,-5.660980,-7.060705,-5.252148,5.325031,-1.963618,1.180309,-9.371000,-7.054156,0.112914,-9.930283,3.696296,3.134459,-0.915853,-2.253456,-9.033020,3.937523,-6.291515,-0.808428,2.239569,-1.412895,3.180024,-0.460278,8.180649,-2.161066,-4.942866,8.581197,3.421613,4.053552,-0.917733,-6.667223,0.950175,-5.856935,9.603570,-0.514603,-4.804925,-5.325745,-5.847617,-5.931706,-3.883952,-8.241469,9.411004,-8.288067,1.646755,-8.967884,1.440426,-1.918736,-8.187243,-8.885489,1.021850,4.708620,-3.512177,9.019619,-0.246886,-4.391891,6.818644,-8.331748,-8.917237,2.196164,-6.021619,-0.608708,-2.636163,-3.946785,1.903131,-8.467944,-9.622587,-3.665112,-1.383253,7.496811,1.909159,7.101220,2.621398,-0.253318,-3.433559,6.153239,3.126897,4.557889,-1.178816,0.623707,-1.984145,2.674007,4.159815,2.528990,8.294526,-7.151582,-5.906381,0.951674,8.791669,-0.995507,5.365940,4.716587,4.456747,-9.115660,-3.739227,3.534916,-5.857614,0.807718,-8.357499,1.792528,-2.839224,8.290496,3.517139,-6.571194,-3.329273,-5.951306,-5.378965,-0.230519,-9.598584,1.717263,-8.230240,-9.519501,9.435492,-5.901920,-8.271474,-7.456915,-8.589901,-7.132608,-4.824583,-1.597166,5.973692,8.922818,-4.058591,1.872169,-3.012864,-4.157331,4.906314,2.196629,-1.096025,-0.377362,1.475450,9.194673,-3.878321,8.156817,-6.032030,7.685657,2.774586,8.767572,1.625186,-7.539579,-6.716925,-6.814358,8.750581,-4.679272,-0.465558,0.100185,7.926164,7.818230,-7.558188,6.965778,-1.898395,-5.113078,5.315604,-6.429748,-1.181080,-2.850656,6.365905,-2.659142,1.507979,-8.656887,9.101423,0.606271,2.016933,8.461706,-0.643945,-5.537061,9.509286,-7.415052,3.970518,5.046932,8.190312,-0.580971,3.003888,-9.968124,6.589127,-1.601429,-1.021345,-0.135408,-3.458539,6.388605,-6.248223,9.515663,-2.745025,-2.788779,-8.717917,0.284845,9.655574,-5.985308,-1.302298,7.628587,-7.106849,-4.191404,-3.039369,-4.859536,-2.917479,0.468387,1.328181,7.140274,-2.602657,6.760445,1.134772,-9.761072,-9.400171,4.077037,5.997036,4.416924,-6.923493,-2.580795,-9.202995,1.573289,-6.535729,6.406239,-8.268258,4.508773,-3.734135,3.237049,5.639868,-7.811911,3.706937,-2.601610,1.109682,-5.938528,-8.228820,-5.296826,1.605362,0.737202,-4.285217,6.181539,1.440697,9.011164,-7.218189,-0.104885,-2.562380,1.795636,-6.711081,6.774602,0.164952,-1.703208,-4.183977,-8.767431,-9.067628,-9.906898,-3.227243,2.872953,-2.816217,7.173837,-4.575643,6.159721,8.911165,-2.546597,-6.540852,4.378740,3.021301,6.736832,-5.769146,8.312328,-8.498719,9.730956,3.377464,-0.566204,6.577715,-7.084084,0.989055,-2.899396,6.290856,9.322989,-9.302119,6.949920,-3.264754,-6.625070,5.719536,4.463637,8.397533,-5.732975,-3.330461,-5.579164,6.148049,5.641720,-6.300786,7.406018,-7.637133,-1.169475,0.296538,-8.870099,-5.563874,-8.916562,-9.231879,9.954683,-8.459555,-4.408894,4.852919,-1.182985,-7.142723,5.933637,6.524673,-8.689862,5.872903,1.726438,-3.167779,-2.289777,-0.581474,-8.940401,2.786983,-1.881475,-7.882022,-3.346459,2.758167,-6.166519,-0.771020,0.604544,-5.856861,0.839737,-5.004226,-2.711649,-9.225539,0.429749,0.397968,7.146991,-0.634075,-3.429106,-0.556205,-8.169771,1.166429,2.594838,-0.849407,5.616165,-3.762929,9.235574,4.151925,-3.492877,-6.325467,-5.831588,6.083750,-6.102406,9.489062,-2.262546,0.160343,-6.565793,1.163567,-0.508642,-7.057772,-7.161982,-4.212715,9.647588,2.477594,3.411294,8.301932,8.951387,4.359323,-6.419855,-0.873028,1.673681,2.212794,-3.505291,9.835790,1.947618,4.489382,5.608333,4.543807,2.306832,-4.922589,-4.550584,3.750374,-3.128141,-2.903957,1.727645,-0.355390,-8.398621,-7.291875,-4.482727,-7.062494,3.750257,-8.233752,4.791113,2.170492,-2.036335,-7.373803,-6.055387,3.986029,-0.776261,3.142468,-9.625287,-3.715755,-1.019111,-8.364343,6.288037,-8.382025,-8.091685,2.812362,-5.659431,-6.391052,-6.858571,1.371043,-3.473919,0.611423,-3.760340,0.446109,-9.252339,-0.003590,-6.235560,-7.374564,5.336676,7.473871,5.091783,0.921444,9.745828,-5.753582,-1.332869,-5.724819,-5.902752,-1.468806,6.940545,-7.995875,9.770171,-2.668107,8.872252,5.119342,9.435962,-2.539076,9.335023,-0.648918,1.644280,-1.991981,-4.631996,4.156187,1.241075,-2.610117,4.536235,-7.043903,1.440756,-9.783362,4.541595,3.390127,-7.840948,5.316113,0.571924,8.215873,5.420278,1.875444,-6.589698,-5.660178,-1.887013,-1.417846,4.583878,-2.669182,5.526431,7.466369,4.100252,3.815347,-8.397159,3.056837,-1.129563,3.074704,3.636547,-0.008018,7.923407,1.570348,4.046057,2.592194,-8.312988,5.730673,-5.234390,6.836746,2.440870,-6.657095,2.944949,2.295576,-1.641211,9.000199,5.174749,1.844246,4.015792,-4.674326,5.231456,2.204039,-9.189219,0.740498,-3.002157,-0.954331,-4.518685,6.703196,-2.643134,8.099802,4.658436,-6.802841,-5.291064,3.709831,-8.300726,-1.939840,7.079202,-6.271557,-4.349476,8.971244,-1.486569,-5.391077,-5.239271,-9.833921,4.861702,4.081279,6.161993,0.900138,4.668037,5.691067,5.545099,3.574917,1.940363,-9.002421,-5.789277,-3.050683,1.309601,7.399114,9.402885,-0.682440,6.075417,5.553888,-3.645556,8.593068,-9.618314,5.757769,-1.423815,-1.381576,-5.874921,-3.433255,-5.394684,4.963559,1.975987,2.910821,0.983007,6.787941,5.970795,2.989979,-2.933966,-8.173705,4.555120,-9.278438,-0.324886,3.431726,2.794944,2.923550,7.591063,6.100360,8.826604,0.798617,-9.202488,-4.103409,9.163648,2.152859,-7.528891,-7.073411,-2.698614,6.833356,-5.571445,0.143420,-4.908761,9.514638,-3.107446,7.678758,-3.662284,-5.822186,1.728654,-5.451684,-5.379337,-4.971019,1.294372,-8.923773,6.311027,3.505383,-7.522117,7.863631,4.878778,-5.743956,8.264757,-2.011132,-3.389554,7.607786,3.308558,9.398554,8.121042,-9.457723,-1.536189,-8.828936,-7.214383,7.513813,6.287484,-0.428263,-5.986049,-5.720142,-5.983516,3.832388,0.985207,-1.406700,-8.219261,-2.178407,-0.190155,3.777650,7.771075,-7.222998,5.596597,-5.246429,8.561154,8.923830,-4.194689,3.533375,-5.965272,1.638664,2.494098,-9.891672,8.396517,-9.544685,8.061387,8.044724,9.538075,8.924396,0.177456,9.544300,-2.020359,-5.422931,-0.609094,7.381309,-0.863119,-5.852535,-9.414892,-9.274920,1.957657,1.683030,-4.600979,6.906845,6.524937,-5.972575,9.746203,1.205775,-7.035451,-3.943407,4.980911,-9.269437,-8.494480,-5.514779,8.257430,4.398775,7.983056,-3.548255,4.885964,5.411031,-5.472881,4.966599,-4.431093,9.411678,7.891815,7.625061,3.278572,-6.936591,1.109810,-2.314757,8.002933,2.493457,7.696397,-5.789847,-7.469752,8.980793,5.906869,-0.553271,6.256806,1.364544,7.618321,9.710255,-1.498717,-7.593269,-6.241773,-8.763534,-7.238164,-1.659160,6.196029,-7.390157,4.008046,-1.390939,3.752382,-7.583076,-1.811630,8.685023,-8.931761,-5.533192,-8.553598,-9.433485,-5.295258,4.785517,2.906197,-1.717424,-9.970418,-6.978123,-3.365424,8.630942,4.234075,-6.182778,2.101513,1.622820,-6.072016,-7.442379,-6.545524,-1.394250,3.896000,-7.461926,4.458434,-1.767827,9.493422,0.583522,7.009993,7.991421,-8.844550,3.045991,8.037158,-8.509886,-9.115741,0.800478,8.635992,4.388331,4.917778,2.041865,-0.928789,-6.744856,-8.454826,0.888763,-9.203186,-2.103146,-7.808903,-9.096103,-0.256683,-7.671596,9.768642,-0.098596,0.153107,-7.662612,4.572630,3.295305,9.979963,8.581095,-0.558767,5.097998,-8.679195,1.588919,9.913530,-9.529589,-4.699966,3.555237,-1.107875,4.840407,7.854613,-9.554959,5.122550,2.966310,-0.579138,6.760653,7.968271,0.732403,-4.377460,9.332001,4.571989,-3.497771,-6.567435,3.914897,3.358127,-6.499606,-7.516025,7.640792,-2.150660,-2.065487,4.799244,8.661944,4.340924,-0.296522,-7.730472,5.214957,-0.034569,7.534901,6.744280,0.600405,8.987734,-9.022758,6.084167,-1.477482,-2.536227,-5.166569,-2.078658,-5.327346,-0.371258,6.405978,-9.230508,-1.229395,-9.706663,0.554525,1.314939,-2.096846,-7.406914,-2.748743,-0.323791,-0.253073,-4.038269,4.999319,-5.377690,-1.646946,-8.748661,0.079294,-8.899454,6.340781,-5.273695,6.065465,-3.262583,-9.510377,-5.983193,-1.895680,5.351500,6.525294,7.029144,-7.660134,-8.534103,-4.498068,0.111817,-3.440534,-3.090842,-3.714558,-3.267484,-5.311065,-5.904455,-9.565411,1.337024,8.211372,0.939790,-1.910295,6.817353,-1.686541,8.096826,5.928437,5.779282,2.898172,6.753828,-3.017106,8.873186,-2.733423,7.816747,-7.777258,3.151960,-6.148703,-9.553416,4.645387,7.676452,7.557277,2.212897,6.548094,-7.105785,-5.809932,9.107875,-9.707038,8.848830,-3.216318,1.129167,6.643115,-5.290949,4.105659,0.234435,7.243524,-9.431472,3.426782,5.715854,-9.077816,8.085389], dtype = "float32")#candidate|7107|(1848,)|const|float32
call_7106 = relay.TupleGetItem(func_6361_call(relay.reshape(const_7107.astype('float32'), [11, 14, 12])), 1)
call_7108 = relay.TupleGetItem(func_6364_call(relay.reshape(const_7107.astype('float32'), [11, 14, 12])), 1)
output = relay.Tuple([call_7097,call_7106,const_7107,])
output2 = relay.Tuple([call_7098,call_7108,const_7107,])
func_7136 = relay.Function([], output)
mod['func_7136'] = func_7136
mod = relay.transform.InferType()(mod)
output = func_7136()
func_7137 = relay.Function([], output)
mutated_mod['func_7137'] = func_7137
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5240_call = mod.get_global_var('func_5240')
func_5242_call = mutated_mod.get_global_var('func_5242')
call_7151 = relay.TupleGetItem(func_5240_call(), 1)
call_7152 = relay.TupleGetItem(func_5242_call(), 1)
func_4201_call = mod.get_global_var('func_4201')
func_4205_call = mutated_mod.get_global_var('func_4205')
var_7156 = relay.var("var_7156", dtype = "float32", shape = (42,))#candidate|7156|(42,)|var|float32
var_7157 = relay.var("var_7157", dtype = "int8", shape = ())#candidate|7157|()|var|int8
const_7158 = relay.const([True,True,False,False,True,False,False,True,True,True,False,False,True,False,True,True,False,True,True,False,False,False,True,False,True,True,True,False,False,True,False,True,False,False,False,False,True,False,True,False,True,True,False,True,True,True,False,True,True,True,True,True,False,True,True,True,False,False,True,False,False,False,False,False,False,False,False,True,False,True,False,False,True,False,True,False,False,True,False,True,False,True,False,False,False,True,False,False,True,True,True,True,True,True,False,False,True,False,True,True,False,True,True,True,False,False,True,False,True,True,True,False,True,True,False,True,False,False,False,True,False,True,True,True,False,True,True,True,True,True,False,True,False,False,False,False,False,False,False,False,True,True,False,False,False,False,False,False,True,False,False,True,True,True,False,True,False,False,False,True,True,False,True,True,False,True,False,True,True,False,True,True,False,True,True,False,True,True,True,False,True,True,True,False,False,False,True,False,False,True,True,True,False,False,False,False,False,False,True,True,True,False,False,True,True,False,True,True,True,False,True,True,True,True,True,True,True,True,True,True,False,True,False,False,True,False,True,True,True,False,True,False,True,True,True,False,True,False,True,True,True,True,False,False,False,True,False,True,False,True,False,True,False,False,True,False,False,False,True,True,True,False,True,False,False,False,False,True,True,False,False,False,True,False,False,True,False,False,False,False,False,False,True,False,False,True,False,False,True,False,False,False,False,True,False,False,False,True,False,True,True,False,True,False,True,True,True,True,False,True,True,False,True,True,False,True,False,True,True,True,True,True,False,True,True,False,False,True,True,False,False,False,False,True,False,True,False,True,False,False,False,False,False,True,True,True,False,True,False,False,False,True,True,False,False,False,True,False,True,False,False,True,True,True,False,True,False,True,True,True,True,True,True,False,True,False,True,True,True,True,True,True,False,True,False,False,True,True,True,True,True,True,False,False,False,True,False,True,False,True,False,True,False,True,True,True,True,False,True,False,True,False,True,True,True,True,False,True,False,True,False,False,False,False,False,True,True,False,False,True,True,False,True,False,True,False,True,False,True,False,False,False,True,True,False,False,True,False,True,True,True,True,True,True,False,False,False,True,False,False,True,False,False,False,False,True,False,True,True,True,False,True,False,True,True,False,True,False,False,True,True,True,False,True,False,False,True,True,False,True,True,True,True,False,True,True,True,True,True,True,True,True,False,True,False,True,True,True,True,True,False,True,False,True,False,False,True,True,True,True,False,True,False,False,True,True,True,False,True,False,True,False,True,False,True,True,True,False,True,True,True,True,False,True,False,False,True,False,True,True,True,True,False,False,True,True,True,True,True,False,True,True,False,True,True,True,False,False,True,True,True,False,True,True,True,True,True,True,True,False,False,True,False,False,True,True,True,False,False,False,True,False,True,True,True,False,True,True,True,False,True,False,True,False,False,False,True,True,True,True,False,True,False,False,True,True,True,False,True,False,True,False,False,False,False,True,True,True,False,False,True,True,False,False,True,False,True,True,False,False,False,False,False,False,False,True,True,True,False,False,True,True,True,True,True,True,False,False,False,True,False,True,False,True,False,False,True,True,True,True,True,True,True,True,True,True,True,False,True,True,False,False,False,True,False,True,False,False,False,False,True,False,False,False,True,False,False,True,True,True,False,False,False,False,False,True,True,True,True,False,False,True,True,False,True,True,True,True,True,True,False,True,False,False,True,True,False,True,False,True,False,True,True,False,True,True,True,False,False,False,True,False,True,False,False,False,True,False,False,False,True,False,True,True,False,False,True,False,True,True,True,True,False,False,True,True,False,False,False,False,False,True,True,False,True,True,False,False,True,False,False,True,False,False,False,False,False,True,False,False,True,True,True,True,False,True,True,False,True,True,False,False,False,True,False,True,True,False,True,False,True,True,True,True,True,False,False,False,True,False,False,False,False,True,False,False,False,True,False,False,False,False,False,False,False,False,True,True,False,False,True,True,True,True,True,True,True,True,True,False,True,True,True,True,False,True,True,True,False,True,True,False,False,True,False,False,True,True,True,True,True,False,True,False,True,False,True,False,True,False,True,False,True,False,False,False,True,True,True,True,True,False,True,True,True,True], dtype = "bool")#candidate|7158|(896,)|const|bool
call_7155 = relay.TupleGetItem(func_4201_call(relay.reshape(var_7156.astype('float32'), [14, 3, 1]), relay.reshape(var_7157.astype('int8'), []), relay.reshape(const_7158.astype('bool'), [896,]), ), 7)
call_7159 = relay.TupleGetItem(func_4205_call(relay.reshape(var_7156.astype('float32'), [14, 3, 1]), relay.reshape(var_7157.astype('int8'), []), relay.reshape(const_7158.astype('bool'), [896,]), ), 7)
func_5900_call = mod.get_global_var('func_5900')
func_5901_call = mutated_mod.get_global_var('func_5901')
call_7160 = relay.TupleGetItem(func_5900_call(), 0)
call_7161 = relay.TupleGetItem(func_5901_call(), 0)
func_5900_call = mod.get_global_var('func_5900')
func_5901_call = mutated_mod.get_global_var('func_5901')
call_7165 = relay.TupleGetItem(func_5900_call(), 0)
call_7166 = relay.TupleGetItem(func_5901_call(), 0)
output = relay.Tuple([call_7151,call_7155,var_7156,var_7157,const_7158,call_7160,call_7165,])
output2 = relay.Tuple([call_7152,call_7159,var_7156,var_7157,const_7158,call_7161,call_7166,])
func_7170 = relay.Function([var_7156,var_7157,], output)
mod['func_7170'] = func_7170
mod = relay.transform.InferType()(mod)
var_7171 = relay.var("var_7171", dtype = "float32", shape = (42,))#candidate|7171|(42,)|var|float32
var_7172 = relay.var("var_7172", dtype = "int8", shape = ())#candidate|7172|()|var|int8
output = func_7170(var_7171,var_7172,)
func_7173 = relay.Function([var_7171,var_7172,], output)
mutated_mod['func_7173'] = func_7173
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5389_call = mod.get_global_var('func_5389')
func_5390_call = mutated_mod.get_global_var('func_5390')
call_7227 = relay.TupleGetItem(func_5389_call(), 1)
call_7228 = relay.TupleGetItem(func_5390_call(), 1)
func_690_call = mod.get_global_var('func_690')
func_695_call = mutated_mod.get_global_var('func_695')
const_7265 = relay.const([[-3,7],[-10,10],[-3,1],[-1,8],[-8,6],[-10,-7],[2,-2],[2,-3],[9,-9],[-2,-7],[9,1],[-2,-7],[8,2],[-10,10],[4,2],[-8,-3],[8,5],[10,9],[1,9],[-8,4],[4,4],[6,7],[-6,10],[-5,-8],[-4,4],[-7,5],[-10,-1],[-5,-6],[2,4],[-6,10]], dtype = "uint32")#candidate|7265|(30, 2)|const|uint32
const_7266 = relay.const([1.241504,5.864279,-3.988782,-4.305889,-4.637158,4.296418,9.903841,1.705948,5.901237,5.431059,2.739104,-4.365141,-0.490770,-4.640344,9.876450,-7.756991,3.840819,8.943035,-4.207510,5.976306,-5.030291,5.471321,2.455166,6.555024,-4.201574,-6.573164,-5.969503,3.618158,-3.143613,-2.463020,1.038764,-7.435377,-3.902163,-9.946328,8.141020,3.103972,-4.324683,-5.407398,4.744813,-5.779360,-1.281353,3.400476,5.921849,2.439900,5.275257,8.284801,2.425287,6.833669,2.205914,-9.560881,1.610639,-2.865038,-4.665181,-9.387975,-8.717065,2.647256,9.838801,2.466412,8.191498,9.099778,-3.248848,6.735601,-0.443702,5.626366,-1.594724,9.221291,4.146671,2.500304,-1.849738,-9.566858,3.557548,5.386272,-1.089112,0.272600,-2.240016,-0.277259,-9.033770,-1.114067,9.255388,-0.412179,6.023814,8.046412,-2.766577,-3.580022,-7.417936,7.491214,0.538108,1.660835,-2.382329,1.337862,3.800056,7.290708,-9.009170,-3.258187,-6.718296,7.900415,-7.930702,-2.415420,-4.592899,2.094125,8.306482,-0.069166,-6.172720,0.181290,-7.305531,5.490385,-0.751606,1.595833,-6.299512,-7.493010,5.856404,-1.820331,9.662217,-1.994239,4.287254,-5.160614,-0.933018,7.914513,-9.188619,5.950029,-8.331415,-9.217759,-6.636307,4.908102,-2.399971,4.286538,0.988625,2.279776,-7.458137,-9.355071,-6.115693,3.944463,5.357151,6.169731,0.016810,3.525100,0.083898,-4.230530,3.208539,-8.306933,-9.151065,9.210303,4.233345,-3.596096,-3.161791,0.760113,9.709820,-2.082199,-4.701176,3.758700,-5.373547,3.874275,-1.784385,8.472084,6.469643,3.177706,1.034471,3.208074,-2.092019,3.503336,1.935269,6.855753,9.642345,6.075804,4.511571,4.442429,5.858915,5.710953,-8.544387,-1.076459,-9.401337,2.314600,-5.001921,-8.350688,-3.291997,-3.996331,-4.766638,8.672812,4.868345,1.771122], dtype = "float32")#candidate|7266|(180,)|const|float32
const_7267 = relay.const([[True,False],[False,False],[False,True],[True,False],[True,True],[False,True],[True,False],[False,True],[False,True],[False,False],[False,True],[False,True],[False,False],[True,True],[False,True],[True,True],[True,False],[True,True],[True,False],[False,False],[True,False],[True,False],[True,True],[True,True],[False,True],[True,True],[False,True],[False,True],[True,False],[False,True],[True,True],[True,False],[True,False],[True,False],[True,True],[False,False],[False,False],[True,True],[True,False],[False,False],[False,True],[True,False],[True,True],[True,False],[True,True],[False,False],[True,True],[False,False],[True,False],[True,False],[True,True],[True,True],[True,False],[False,True],[False,False],[True,False],[False,False],[True,True],[True,False],[True,True],[False,True],[True,True],[False,False],[True,False],[False,False],[False,True],[False,True],[True,True],[True,True],[False,False],[False,True],[False,False],[True,True],[True,True],[False,False],[False,False],[False,True],[True,False],[True,False],[False,True],[True,True],[True,True],[False,False],[False,False],[True,True],[False,True],[False,False],[True,False],[False,False],[True,False],[True,True],[False,True],[False,True],[True,False],[True,False],[True,False],[True,False],[True,True],[False,False],[True,False],[True,True],[True,True],[False,True],[True,False],[True,False],[False,False],[True,False],[True,False],[True,True],[False,False],[True,True],[True,False],[False,False],[True,False],[False,True],[False,True],[False,False],[True,False],[True,False],[False,False],[True,False],[True,False],[False,False],[False,True],[True,False],[False,False],[False,True],[False,False],[True,False],[False,False],[True,True],[True,True],[True,False],[False,False],[True,False],[False,False],[True,True],[False,True],[False,True],[True,True],[True,True],[False,True],[False,False],[True,True],[False,False],[True,True],[True,True],[True,False],[True,True],[False,False],[True,False],[False,False],[False,True],[False,False],[False,True],[True,True],[False,True],[True,False],[False,False],[True,False],[False,True],[False,True],[False,True],[True,True],[False,True],[False,True],[False,False],[False,False],[True,False],[False,True],[True,True],[True,True],[True,False],[True,True],[False,False],[True,True],[True,True],[False,True],[False,False],[True,False],[True,True],[False,True],[True,False],[True,True],[False,True],[False,True],[True,True],[False,False],[True,True],[True,False],[True,False],[True,True],[False,True],[False,False],[True,True],[True,True],[False,True],[False,False],[True,False],[True,True],[True,True],[False,False],[True,False],[False,False],[True,True],[False,False],[False,True],[True,False],[True,False],[False,False],[True,True],[True,False],[False,False],[False,True],[False,True],[False,True],[False,False],[False,True],[False,False],[False,True],[False,False],[False,False],[False,True],[False,True],[True,False],[True,True],[False,True],[True,False],[True,True],[False,True],[False,False],[False,False],[True,False],[False,True],[True,False],[True,True],[False,True],[True,False],[False,True],[True,False],[True,True],[True,True],[False,False],[False,True],[True,False],[False,True],[False,False],[True,True],[True,True],[True,False],[True,False],[True,False],[True,False],[False,True],[True,False],[True,False],[True,False],[False,True],[False,False],[False,True],[False,False],[False,False],[False,False],[False,True],[True,True],[True,True],[True,False],[True,False],[False,True],[True,True],[True,True],[False,False],[True,False],[True,False],[False,True],[True,False],[True,False],[False,False],[False,False],[True,True],[True,True],[False,False],[True,True],[False,False],[True,False],[True,False],[True,True],[True,False],[True,False],[False,True],[False,False],[True,True],[False,False],[True,False],[False,True],[True,False],[False,False],[False,True],[True,True],[True,False],[True,True],[True,False],[False,False],[False,False],[False,True],[True,False],[True,True],[False,True],[True,True],[True,True],[False,False],[True,False],[False,False],[False,False],[True,True],[False,False],[False,True],[False,True],[True,False],[True,False],[True,False],[False,False],[True,False],[True,False],[False,False],[False,False],[True,True],[True,True],[True,True],[True,False],[False,False],[False,True],[True,False],[False,True],[True,True],[True,False],[True,True],[True,True],[False,False],[True,False],[True,True],[False,False],[True,True],[True,False],[False,True],[True,True],[True,True],[False,False],[False,False],[True,True],[True,False],[True,False],[False,False],[True,False],[True,True],[False,False],[False,False],[False,True],[False,True],[False,False],[False,True],[True,True],[False,True],[False,False],[True,True],[True,False],[False,True],[True,False],[True,False],[False,False],[True,False],[False,False],[False,False],[True,False],[False,True],[True,False],[False,False],[False,True],[False,False],[True,True],[True,True],[False,True],[False,True],[True,True],[True,True],[False,True],[True,False],[True,False],[True,False],[False,True],[False,True],[True,False],[False,True],[True,False],[True,True],[True,True],[False,True],[False,False],[False,False],[True,False],[True,True],[True,True],[False,False],[True,True],[False,True],[False,False],[True,True],[True,True],[True,False],[True,False],[True,False],[True,True],[False,False],[True,False],[False,True],[False,True],[False,True],[False,False],[True,True],[True,False],[True,True],[False,False],[True,True],[True,False],[False,False],[False,True],[False,False],[True,False],[False,False],[True,False],[True,True],[True,False],[True,False],[False,False],[True,False],[False,False],[True,True],[False,False],[False,True],[False,False],[True,True],[False,False],[True,True],[False,True],[True,True],[True,True],[True,False],[True,False]], dtype = "bool")#candidate|7267|(448, 2)|const|bool
const_7268 = relay.const([9,-2,-3,-5,4,7,4,-10,5,7,-8,5,-1,-5,-10,-8,2,-9,4,-3,-4,6,8,-2,-5,-4,-5,-4,-9,-3,-5,-10,-3,-4,-1,-3,-7,-2,4,-9,6,-1,-6,7,-8,-2,1,10,1,1,8,8,5,-2,7,-8,-7,-3,-6,6,-9,6,4,-4,-9,8,2,-5,-9,6,8,-8,4,8,2,-5,6,-10,9,-5,2,-8,-3,-9,-7,10,-10,-10,2,8,4,2,7,10,8,4,3,2,4,10,-8,-7,-1,-5,-7,-4,6,-2,-9,-9,-2,-7,-7,-2,-2,-2,-5,1,8,-8,8,-9,-9,7,5,-5,9,3,2,-6,-10,-9,7,-2,5,-1,3,5,-3,1,8,-5,9,4,-5,-10,-9,1,-6,-1,4,-3,-4,-10,3,-4,-9,-2,9,4,6,-1,2,1,5,-10,-5,-8,3,7,1,-9,-2,-1,-6,-7,8,7,9,9,-1,-5,-1,-7,-2,2,-6,6,-1,9,3,-10,-3,2,-5,6,-9,2,3,-6,-6,10,9,-9,6,-8,5,3,-2,-8,5,3,-6,-6,6,5,10,3,-5,8,2,2,3,-5,-2,2,-8,3,-1,2,1,-9,-5,10,5,-3,3,6,3,-1,-4,-2,9,4,-6,-5,-6,-8,7,4,8,-2,-5,9,8,2,-4,-4,-2,2,7,-5,-2,-7,-2,4,8,-3,2,10,-1,-6,9,-7,-10,-8,-6,1,5,10,7,-7,8,8,1,4,2,-6,-7,1,2,6,10,8,5,3,2,9,-2,-1,-4,-3,-2,7,-2,9,-6,1,-2,1,7,-1,8,10,-6,-10,-4,7,4,7,2,7,1,-4,-7,10,1,-4,1,8,4,10,-3,-6,-2,-2,-9,2,6,-2,-3,8,4,-2,7,6,9,3,-4,-10,2,-3,-10,-2,3,9,6,9,-3,-9,-2,-4,-1,-5,-6,1,5,-10,9,3,-7,5,2,-7,6,7,-1,8,-10,6,6,-5,-1,7,-8,-1,5,-10,1,-1,-3,2,-1,-5,3,-6,-9,3,-7,-10,-3,2,9,2,-9,-7,-3,-10,1,-5,9,5,-4,7,-9,8,8,-7,-2,-6,-3,-7,2,-3,3,7,-3,9,9,1,-3,-9,7,-7,-4,-1,-6,7,6,-8,2,-10,-8,-2,-4,-4,-2,-9,8,9,1,-2,10,4,9,-6,9,-6,6,-5,-1,-7,-1,-1,6,-2,-1,3,-2,-9,1,2,1,9,5,6,-3,8,-3,3,-10,6,9,-5,8,-4,7,-1,3,4,5,4,6,2,-3,-9,-1,-6,-6,-1,-3,5,10,-8,7,-3,-5,10,2,-3,6,10,8,-8,-7,1,6,1,2,-3,5,-3,4,2,-5,1,-8,9,-8,-2,-9,-8,9,-3,1,1,-1,-4,6,-10,-2,2,-3,10,9,-8,-7,5,6,-6,-3,2,-9,-10,-6,-6,3,-10,1,10,6,-10,4,6,3,-8,-8,10,-9,-2,3,3,8,-4,7,-10,-2,3,-4,-10,2,-3,8,-8,6,-2,-2,6,-10,8,4,10,8,4,2,-1,1,7,-7,-8,8,3,9,-9,-8,8,-5,-10,10,7,7,10,-9,-9,3,1,-1,9,-2,1,-7,1,-7,-5,4,-1,-9,1,10,-6,9,-4,10,2,-4,-3,2,-3,7,-6,-1,4,-9,-7,6,2,9,-8,9,-2,-3,-4,-8,-3,-4,-6,5,-4,-6,3,-4,-7,-1,1,-9,3,-7,6,-1,-10,8,-1,-7,-7,-7,3,7,2,9,6,-8,9,-5,3,-5,-2,-1,6,-9,1,7,-5,5,10,3,-1,6,-8,-4,8,6,-2,4,-4,-3,9,10,4,-5,9,-4,-1,-2,-1,2,8,1,4,10,-8,-5,-2,-3,10,3,-8,-2,7,-9,-2,10,-8,10,4,-2,-2,1,1,2,-4,3,-2,-10,-10,-9,-8,2,10,8,9,-10,6,-7,-5,-8,-6,10,5,8,9,-8,8,4,10,-6,3,-4,-7,-8,1,-3,7,6,-5,9,-6,10,-7,-4,6,9,-5,-8,3,-5,2,-3,1,-2,8,10,-10,-7,-3,-5,-10,6,-9,-8,-10,9,10,2,-3,-10,8,4,10,-5,2,-2,6,10,4,-8,-10,6,-10,3,-3,-6,-3,-8,-2,6,7,-8,5,10,5,-4,6,-7,10,-2,5,5,10,10,10,-8,5,-10,6,-10,10,10,-7,4,6,-2,4,8,-3,-6,8,8,3,-4,1,-2,9,9,-8,5,9,-5,-7,6,3,10,7,-5,-9,-1,-2,-1,4,8,3,6,-1,4,5,-7,-4,-10,-7,3,-3,-6,7,5,-9,3,-6,-1,-1,-6,-7,-7,-10,-3,-1,2,-1,8,-10,-9,-7,9,3,-2,-7,3,1,-4,-6,-7,3,2,2,2,-4,-8,-3,-4,-9,3,7,1,-7,-7,1,-1,-5,-10,2,8,-1,6,-5,2,-9,1,4,-3,8,3,6,-6,6,10,8,-3,4,2,-10,-3,-1,4,-8,-6,7,-8,3,5,-9,-7,-3,-5,8,6,6,-8,6,2,-10,-10,8,-1,-1,-10,3,9,-6,3,-6,5,-8,8,-6,8,1,-5,8,-9,4,9,-5,-3,5,-6,-7,-2,5,-9,-10,-6,-6,9,-7,-3,8,-10,2,-5,-3,9,-1,3,1,-6,10,4,-3,2,-1,-4,-8,-1,10,-1,-6,-3,9,2,9,-1,-2,-8,7,-6,6,-7,-6,7,2,-1,8,7,1,7,9,-10,2,7,-8,8,-5,-8,-3,7,3,-6,-3,8,2,3,-3,2,10,7,-4,-10,1,-10,-3,2,6,-6,-10,-2,-10,-4,7,-2,-7,3,-7,-10,2,-3,-6,2,-4,10,3,-6,4,-9,8,-8,-2,8,-5,-8,-8,-2,7,-8,-2,-2,-10,-1,-8,7,-2,3,-7,3,-1,1,-1,6,8,-8,-2,-7,-1,-1,1,-7,5,8,2,6,-2,3,-1,-3,2,-9,-4,-1,9,3,9,4,1,6,5,7,8,-3,10,5,-9,-8,-5,7,-2,1,-2,5,-6,9,4,1,7,-10,9,-8,-2,-1,-7,10,-9,-1,5,-6,-9,-6,-10,-5,-10,3,10,10,-8,-10,9,4,-10,-9,-3,10,10,6,-1,-9,8,2,1,-2,1,6,2,8,-7,9,-3,-3,-4,-7,2,8,7,-7,-10,-9,-3,-2,7,6,-8,3,3,8,-6,4,10,7,-10,8,-5,4,2,-2,-8,2,-5,-1,2,6,4,-8,-2,4,3,-3,-8,6,-2,8,9,10,-4,2,10,-8,8,1,-4,1,4,6,10,2,2,-6,2,5,-4,-6,7,-1,9,-6,-4,10,10,1,-10,5,-5,-3,4,-6,6,-5,3,9,-5,-5,-9,-8,-1,-2,4,-2,-6,-7,-6,-1,5,5,-3,10,-9,-8,1,1,6,4,-9,-10,-3,7,2,-2,-7,4,3,-7,-10,3,10,-7,5,6,-10,-1,3,-2,10,-1,5,5,9,2,-7,-3,7,5,1,-8,-10,-4,8,10,-2,-3,4,6,-1,3,1,9,5,-2,7,-5,-8,2,5,-4,-2,-5,-6,-10,-9,-7,10,-10,9,-1,-1,-5,-5,7,-10,-8,-7,-9,-6,-9,5,-5,1,-9,-9,-9,7,1,3,-4,10,-5,7,-1,-4,-7,-6,3,-10,-10,-3,9,-4,-1,-2,-2,-7,9,-3,-6,-3,-8,-7,-6,5,4,-6,-7,-5,1,-5,10,-10,-7,-1,1,-8,-3,-10,-2,7,-3,10,5,-2,5,-9,-9,-5,-3,-1,-10,-5,-4,2,-2,-1,-3,-6,-8,-7,6,-9,-5,3,-1,-4,5,-4,6,4,-6,-2,-8,9,9,-1,2,-1,-4,-8,-1,6,4,3,-5,-8,2,9,-10,-7,6,3,-10,6,-9,9,-7,-5,4,-10,5,-9,8,8,-8,-9,7,-2,-8,-8,-3,8,1,-10,1,3,8,4,10,5,1,2,-8,2,3,5,-1,7,-8,9,4,5,4,7,-5,1,8,3,-8,-4,-7,8,-5,9,1,-3,10,9,9,-7,10,-10,9,-6,8,-1,-10,4,3,9,3,-1,9,-6,-5,5,-9,4,8,-9], dtype = "int8")#candidate|7268|(1568,)|const|int8
call_7264 = relay.TupleGetItem(func_690_call(relay.reshape(const_7265.astype('uint32'), [2, 2, 15]), relay.reshape(const_7266.astype('float32'), [180,]), relay.reshape(const_7267.astype('bool'), [896,]), relay.reshape(const_7268.astype('int8'), [1568,]), ), 0)
call_7269 = relay.TupleGetItem(func_695_call(relay.reshape(const_7265.astype('uint32'), [2, 2, 15]), relay.reshape(const_7266.astype('float32'), [180,]), relay.reshape(const_7267.astype('bool'), [896,]), relay.reshape(const_7268.astype('int8'), [1568,]), ), 0)
output = relay.Tuple([call_7227,call_7264,const_7265,const_7266,const_7267,const_7268,])
output2 = relay.Tuple([call_7228,call_7269,const_7265,const_7266,const_7267,const_7268,])
func_7281 = relay.Function([], output)
mod['func_7281'] = func_7281
mod = relay.transform.InferType()(mod)
output = func_7281()
func_7282 = relay.Function([], output)
mutated_mod['func_7282'] = func_7282
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4017_call = mod.get_global_var('func_4017')
func_4018_call = mutated_mod.get_global_var('func_4018')
call_7291 = relay.TupleGetItem(func_4017_call(), 0)
call_7292 = relay.TupleGetItem(func_4018_call(), 0)
uop_7306 = relay.sin(call_7291.astype('float32')) # shape=(11, 14, 12)
uop_7308 = relay.sin(call_7292.astype('float32')) # shape=(11, 14, 12)
output = relay.Tuple([uop_7306,])
output2 = relay.Tuple([uop_7308,])
func_7309 = relay.Function([], output)
mod['func_7309'] = func_7309
mod = relay.transform.InferType()(mod)
mutated_mod['func_7309'] = func_7309
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7309_call = mutated_mod.get_global_var('func_7309')
call_7310 = func_7309_call()
output = call_7310
func_7311 = relay.Function([], output)
mutated_mod['func_7311'] = func_7311
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3874_call = mod.get_global_var('func_3874')
func_3875_call = mutated_mod.get_global_var('func_3875')
call_7364 = func_3874_call()
call_7365 = func_3874_call()
func_6478_call = mod.get_global_var('func_6478')
func_6483_call = mutated_mod.get_global_var('func_6483')
const_7395 = relay.const([[-3,5,4,-6,-8,6,-3,-7,-5,1,8,7,-1,3,8,-4,6,5,-9,10,8,-3,-10,9,-5,-9,-6,2,7,-7,3,-5,9,9,-3,-5,-7,-1,1,2,10,-9,-10,-2,-8,-3,8,-2,-8,-7,9,1,10,-3,-9,9,8,6,10,-6,-6,-1,-7,-5,1],[-7,2,6,-9,5,6,9,-3,-4,2,-1,-9,7,5,-10,-2,9,-4,-9,6,2,9,7,-6,-5,1,1,10,5,-7,-4,-3,-6,9,-1,-7,-8,4,-10,-8,-1,3,-10,-9,10,1,7,-6,2,-6,10,-8,2,4,4,-7,3,-6,-4,-8,-1,8,-3,-10,-10],[10,10,8,1,3,6,-10,-1,9,-3,10,6,-3,2,5,-8,2,4,3,2,1,-8,-6,-1,-4,2,8,2,8,-3,-6,10,2,-7,-9,2,8,5,9,-9,-8,-7,-10,8,-2,10,5,-7,-4,-1,-5,7,3,7,5,6,-10,2,3,7,4,-5,-7,-5,9],[6,-8,-7,-4,-4,-2,-4,3,-4,9,-4,-9,9,3,9,-9,4,-7,-10,-7,9,5,4,1,-6,7,5,-1,4,-8,4,7,7,-10,2,-1,9,-6,4,8,10,-10,-5,-9,4,3,9,9,3,-2,9,8,9,-10,1,-5,-5,-6,-7,-1,-4,-1,4,8,-1],[4,4,-7,-6,-8,-7,8,1,4,8,-10,-10,5,3,3,4,4,-1,-2,10,-4,6,-10,-5,-4,-2,9,-5,7,-8,10,10,-1,-6,8,7,-4,-3,8,9,-4,4,4,-8,7,-3,-9,2,-6,4,-6,-5,2,5,9,-1,4,4,7,8,7,1,-6,5,1],[7,10,8,-3,3,-8,3,-4,-1,-9,4,-2,-4,-10,-2,10,-2,5,-2,4,8,-10,3,10,-4,5,-6,7,-7,1,-1,3,1,3,4,-1,-7,-3,-4,6,-1,9,10,-9,2,8,-3,7,7,-9,5,-5,-10,5,-3,-3,-6,4,-8,-2,-7,4,-1,3,-8],[1,4,-8,-6,10,7,-4,6,6,-2,-4,1,8,10,-4,-6,4,2,-6,-6,-6,10,4,9,-9,2,-10,3,9,-1,-2,9,-9,-9,-9,-3,-7,-6,-10,5,-6,5,10,-5,-3,-1,3,2,-8,9,7,-4,-7,-7,5,-6,-7,-8,3,7,2,-1,-7,-9,6],[-2,-1,7,-7,5,-4,-5,-6,-9,8,2,-3,7,8,5,-5,6,5,8,-8,4,-5,-5,1,9,10,-1,8,3,3,9,6,8,1,-3,-8,-10,-7,-6,-7,-10,-8,-1,9,4,1,2,1,9,5,-10,3,7,-3,8,10,8,-1,6,-3,1,-4,-1,4,-8],[6,-5,-5,8,-7,-9,-6,-7,-8,-6,3,-4,4,-5,-9,-9,-10,3,9,5,-8,5,3,-1,-4,1,6,-8,3,9,6,-7,4,-4,-9,-9,5,-1,5,-9,-8,-8,-6,-5,10,10,-1,2,7,8,-5,3,2,-8,5,-6,6,7,10,10,5,-8,7,4,8],[-9,3,-4,-7,2,10,5,3,9,-6,-5,-10,-9,-5,-10,9,7,-3,-6,5,-2,-5,-4,-9,-2,-3,7,-2,-10,-1,9,4,-1,10,9,5,-2,-8,-9,-9,-3,-9,-4,7,7,6,10,-3,7,10,1,-7,6,-9,-2,5,1,-6,-5,10,-2,8,-6,-3,-6],[-9,8,10,-1,6,-7,9,-7,4,-7,-1,-3,-1,10,4,-8,-1,-8,8,-9,-3,7,6,-8,-3,-7,3,3,-10,9,7,6,-2,10,-4,-6,7,10,9,-8,-2,-9,6,1,3,10,7,-1,-10,1,-9,-10,2,4,9,-4,-6,8,-4,-7,-8,10,-3,-6,-1],[-7,-4,1,-9,7,-4,9,-5,1,7,-8,-5,2,-9,-2,-3,-3,6,-3,6,4,-3,9,1,9,9,3,-6,-3,3,-7,2,3,5,-4,-10,-2,-1,-2,2,10,-1,-5,-8,-3,-4,7,-2,4,10,10,-6,4,-5,2,8,-9,5,-7,2,3,-2,-2,3,-4],[5,3,-8,3,-3,-1,6,-1,5,3,-8,3,-9,4,10,4,-4,9,6,-5,6,2,-7,-1,3,-10,-10,-10,-8,10,-4,3,5,-10,-5,-2,5,1,10,-6,5,1,9,-6,-6,4,5,8,1,-3,-4,-5,10,3,-5,-1,3,10,5,-8,4,-3,-9,-9,10]], dtype = "int64")#candidate|7395|(13, 65)|const|int64
const_7396 = relay.const([-5.146911,3.593825,7.199743,4.655560,-1.172189,2.679487,1.614808,-2.478349,-7.887099,3.316547,0.214188,-4.374280,-3.040490,-9.004684,-2.759248,-0.406046,4.336123,5.629091,-6.315758,-3.564638,-6.355772,-6.138113,-2.758421,-8.120513,9.654644,-1.649925,7.403090,-9.028513,-3.774357,8.758172,-3.991023,4.359032,-5.616412,-3.544817,3.130474,3.937602,-4.570471,7.681785,-5.080804,-1.067943,-9.103749,2.364096,4.852948,1.774338,-5.725022,9.885145,-9.580966,-3.720439,6.385523,8.675565,-3.443569,-0.254312,-4.493794,8.445376,-6.175448,-3.594243,-2.186059,-6.450022,9.112418,7.295954,7.347769,8.363071,3.274720,-6.219854,-4.966963,1.678709,-2.769446,-4.320425,3.520402,9.699635,5.338676,-5.556273,5.625880,2.932873,-9.613404,6.466763,5.218542,-1.846492,-7.731718,-2.698347,-3.976355,6.293357,2.704159,-1.403644,8.216532,-3.626875,9.298461,-7.629792,-8.806753,-2.837941,-8.047499,-7.609471,-7.009150,-9.187984,9.217688,4.658283,-0.690321,-2.801767,-0.090144,8.481984,-0.047842,-8.938114,-9.078582,3.523276,6.614032,-0.290637,0.692183,1.177088,4.314347,-0.718998,-2.573207,-2.627490,6.014863,8.190326,4.933500,9.652556,-1.494135,-8.959753,6.847294,5.940087,2.560806,-6.378630,-9.410549,-3.721124,-5.322836,-7.959895,-8.823121,9.151746,2.960402,-8.069401,7.630408,3.538035,0.195387,2.135172,6.589203,0.400017,-7.072780,9.519509,-5.223821,-6.381386,-7.937721,2.049973,1.196126,-5.900596,2.505490,-6.575042,9.417264,1.655193,1.928809,0.890556,5.324312,7.301361,-2.589255,0.246389,-4.211631,1.478945,-2.457870,9.716899,-6.789327,8.888292,-9.257787,-3.956675,2.233522,0.331571,-0.559378,0.067299,0.960615,8.144513,3.829823,-7.507210,-6.774350,-5.456337,3.002417,6.631463,-6.618682,6.826333,-8.609052,-3.455635,2.962085,-2.789827], dtype = "float32")#candidate|7396|(180,)|const|float32
var_7397 = relay.var("var_7397", dtype = "int8", shape = ())#candidate|7397|()|var|int8
var_7398 = relay.var("var_7398", dtype = "bool", shape = (896,))#candidate|7398|(896,)|var|bool
call_7394 = relay.TupleGetItem(func_6478_call(relay.reshape(const_7395.astype('int64'), [845, 1]), relay.reshape(const_7396.astype('float32'), [180, 1]), relay.reshape(var_7397.astype('int8'), []), relay.reshape(var_7398.astype('bool'), [896,]), ), 5)
call_7399 = relay.TupleGetItem(func_6483_call(relay.reshape(const_7395.astype('int64'), [845, 1]), relay.reshape(const_7396.astype('float32'), [180, 1]), relay.reshape(var_7397.astype('int8'), []), relay.reshape(var_7398.astype('bool'), [896,]), ), 5)
output = relay.Tuple([call_7364,call_7394,const_7395,const_7396,var_7397,var_7398,])
output2 = relay.Tuple([call_7365,call_7399,const_7395,const_7396,var_7397,var_7398,])
func_7401 = relay.Function([var_7397,var_7398,], output)
mod['func_7401'] = func_7401
mod = relay.transform.InferType()(mod)
mutated_mod['func_7401'] = func_7401
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7401_call = mutated_mod.get_global_var('func_7401')
var_7403 = relay.var("var_7403", dtype = "int8", shape = ())#candidate|7403|()|var|int8
var_7404 = relay.var("var_7404", dtype = "bool", shape = (896,))#candidate|7404|(896,)|var|bool
call_7402 = func_7401_call(var_7403,var_7404,)
output = call_7402
func_7405 = relay.Function([var_7403,var_7404,], output)
mutated_mod['func_7405'] = func_7405
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5732_call = mod.get_global_var('func_5732')
func_5733_call = mutated_mod.get_global_var('func_5733')
call_7413 = relay.TupleGetItem(func_5732_call(), 0)
call_7414 = relay.TupleGetItem(func_5733_call(), 0)
output = relay.Tuple([call_7413,])
output2 = relay.Tuple([call_7414,])
func_7428 = relay.Function([], output)
mod['func_7428'] = func_7428
mod = relay.transform.InferType()(mod)
output = func_7428()
func_7429 = relay.Function([], output)
mutated_mod['func_7429'] = func_7429
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6924_call = mod.get_global_var('func_6924')
func_6926_call = mutated_mod.get_global_var('func_6926')
call_7467 = relay.TupleGetItem(func_6924_call(), 0)
call_7468 = relay.TupleGetItem(func_6926_call(), 0)
func_7401_call = mod.get_global_var('func_7401')
func_7405_call = mutated_mod.get_global_var('func_7405')
var_7499 = relay.var("var_7499", dtype = "int8", shape = ())#candidate|7499|()|var|int8
const_7500 = relay.const([True,False,False,True,True,True,False,False,False,True,False,True,False,False,False,False,False,False,True,False,True,True,True,False,False,False,False,False,False,False,True,True,False,True,False,False,False,True,False,False,False,False,False,True,True,False,True,True,False,False,True,False,True,True,False,True,True,False,True,True,False,False,False,True,False,True,True,False,False,True,True,False,False,True,True,True,True,False,False,False,False,False,False,True,True,False,False,False,False,False,False,False,False,False,True,False,True,False,True,True,False,False,False,False,True,True,True,False,False,True,False,False,True,False,False,False,False,False,True,False,False,True,True,True,True,False,True,True,True,False,False,True,False,False,True,True,False,False,False,False,True,False,False,True,True,False,True,True,True,False,False,True,True,True,False,True,True,False,False,False,False,False,True,True,True,False,False,True,False,False,True,False,True,True,True,False,False,False,True,True,True,True,False,False,False,True,True,False,True,True,False,True,False,False,False,True,False,True,False,True,True,True,True,False,False,False,False,False,False,False,True,True,True,False,False,False,True,True,False,False,True,False,True,True,False,False,False,True,True,False,False,False,True,True,True,True,True,True,False,True,True,True,True,True,True,True,True,False,False,True,False,True,True,False,False,False,False,False,True,True,False,True,True,True,False,False,True,True,False,True,False,True,False,True,False,False,False,True,False,True,False,True,False,False,True,True,False,True,True,True,False,False,False,True,True,False,False,False,True,False,True,True,True,False,True,False,False,True,True,False,False,False,True,True,False,False,False,False,True,True,True,True,True,True,True,True,True,True,True,False,True,True,True,False,True,False,False,True,False,False,True,False,False,True,True,False,True,True,False,True,True,True,False,False,False,True,True,True,False,True,True,True,False,False,False,True,True,False,False,True,False,True,True,False,False,True,False,False,False,False,True,True,True,True,False,True,True,True,False,True,False,True,True,False,False,True,True,True,True,True,False,False,True,True,False,True,False,True,True,True,True,False,False,True,False,False,False,True,False,True,False,False,False,True,True,False,False,False,True,False,False,True,False,True,True,False,False,True,True,False,False,True,False,True,False,False,True,False,True,True,True,False,False,False,True,True,False,False,True,False,False,True,True,False,False,False,False,True,False,False,True,False,True,True,True,True,False,True,True,True,False,True,True,False,True,True,True,True,True,True,True,True,False,True,True,True,True,True,False,True,True,True,False,False,False,True,True,False,False,True,False,True,False,True,True,True,False,True,False,True,False,False,False,False,True,True,True,False,True,True,False,False,False,False,True,True,True,False,True,False,True,True,True,True,True,False,False,True,True,True,True,True,True,True,False,False,True,True,False,False,True,False,False,True,False,True,False,False,False,False,False,True,True,True,True,False,True,True,False,True,False,True,False,True,False,False,True,True,False,False,True,True,False,False,False,True,True,True,True,True,True,True,True,False,False,False,True,True,True,True,False,False,False,True,True,False,True,True,False,True,True,True,False,True,True,True,False,True,False,True,False,True,False,True,True,False,True,False,False,True,True,False,True,True,True,False,False,True,True,False,False,False,True,True,False,True,False,False,False,False,False,False,True,False,False,False,True,True,True,True,False,False,True,True,False,True,False,False,False,True,False,False,False,True,True,False,False,True,False,False,True,False,True,False,True,True,True,False,False,False,True,True,False,False,False,False,True,False,False,True,False,False,False,False,False,True,False,False,True,False,True,False,True,False,True,False,True,False,False,True,False,True,False,False,True,True,True,True,True,True,False,True,False,False,True,False,False,True,False,True,False,True,True,True,True,False,True,False,False,True,False,False,False,False,True,True,True,False,False,True,True,True,False,True,True,False,True,True,True,False,False,True,True,False,False,True,False,True,True,True,False,True,True,False,False,False,False,True,False,False,False,False,True,True,True,True,True,True,False,False,True,True,False,False,True,False,True,True,False,True,False,False,False,False,True,False,False,True,False,True,True,False,True,True,True,False,False,False,True,False,True,False,True,True,True,False,True,False,False,True,True,False,False,False,False,True,False,True,False,False,False,True,True,True,False,False,True,False,True,True,True,False,True,False,True,False,True,False,True,True,False,False,True,False,False,False,True,True,True,True,True,True,False,False,False,True], dtype = "bool")#candidate|7500|(896,)|const|bool
call_7498 = relay.TupleGetItem(func_7401_call(relay.reshape(var_7499.astype('int8'), []), relay.reshape(const_7500.astype('bool'), [896,]), ), 0)
call_7501 = relay.TupleGetItem(func_7405_call(relay.reshape(var_7499.astype('int8'), []), relay.reshape(const_7500.astype('bool'), [896,]), ), 0)
output = relay.Tuple([call_7467,call_7498,var_7499,const_7500,])
output2 = relay.Tuple([call_7468,call_7501,var_7499,const_7500,])
func_7502 = relay.Function([var_7499,], output)
mod['func_7502'] = func_7502
mod = relay.transform.InferType()(mod)
var_7503 = relay.var("var_7503", dtype = "int8", shape = ())#candidate|7503|()|var|int8
output = func_7502(var_7503)
func_7504 = relay.Function([var_7503], output)
mutated_mod['func_7504'] = func_7504
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4089_call = mod.get_global_var('func_4089')
func_4091_call = mutated_mod.get_global_var('func_4091')
call_7525 = func_4089_call()
call_7526 = func_4089_call()
output = relay.Tuple([call_7525,])
output2 = relay.Tuple([call_7526,])
func_7534 = relay.Function([], output)
mod['func_7534'] = func_7534
mod = relay.transform.InferType()(mod)
mutated_mod['func_7534'] = func_7534
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7534_call = mutated_mod.get_global_var('func_7534')
call_7535 = func_7534_call()
output = call_7535
func_7536 = relay.Function([], output)
mutated_mod['func_7536'] = func_7536
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6048_call = mod.get_global_var('func_6048')
func_6050_call = mutated_mod.get_global_var('func_6050')
call_7560 = func_6048_call()
call_7561 = func_6048_call()
output = relay.Tuple([call_7560,])
output2 = relay.Tuple([call_7561,])
func_7563 = relay.Function([], output)
mod['func_7563'] = func_7563
mod = relay.transform.InferType()(mod)
output = func_7563()
func_7564 = relay.Function([], output)
mutated_mod['func_7564'] = func_7564
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7602 = relay.var("var_7602", dtype = "float64", shape = (2, 9, 12))#candidate|7602|(2, 9, 12)|var|float64
uop_7603 = relay.atanh(var_7602.astype('float64')) # shape=(2, 9, 12)
output = uop_7603
output2 = uop_7603
func_7615 = relay.Function([var_7602,], output)
mod['func_7615'] = func_7615
mod = relay.transform.InferType()(mod)
var_7616 = relay.var("var_7616", dtype = "float64", shape = (2, 9, 12))#candidate|7616|(2, 9, 12)|var|float64
output = func_7615(var_7616)
func_7617 = relay.Function([var_7616], output)
mutated_mod['func_7617'] = func_7617
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4017_call = mod.get_global_var('func_4017')
func_4018_call = mutated_mod.get_global_var('func_4018')
call_7654 = relay.TupleGetItem(func_4017_call(), 0)
call_7655 = relay.TupleGetItem(func_4018_call(), 0)
output = relay.Tuple([call_7654,])
output2 = relay.Tuple([call_7655,])
func_7658 = relay.Function([], output)
mod['func_7658'] = func_7658
mod = relay.transform.InferType()(mod)
output = func_7658()
func_7659 = relay.Function([], output)
mutated_mod['func_7659'] = func_7659
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5992_call = mod.get_global_var('func_5992')
func_5993_call = mutated_mod.get_global_var('func_5993')
call_7709 = relay.TupleGetItem(func_5992_call(), 0)
call_7710 = relay.TupleGetItem(func_5993_call(), 0)
func_3460_call = mod.get_global_var('func_3460')
func_3464_call = mutated_mod.get_global_var('func_3464')
var_7735 = relay.var("var_7735", dtype = "uint16", shape = (120,))#candidate|7735|(120,)|var|uint16
call_7734 = relay.TupleGetItem(func_3460_call(relay.reshape(var_7735.astype('uint16'), [5, 4, 6]), relay.reshape(var_7735.astype('uint16'), [5, 4, 6]), ), 0)
call_7736 = relay.TupleGetItem(func_3464_call(relay.reshape(var_7735.astype('uint16'), [5, 4, 6]), relay.reshape(var_7735.astype('uint16'), [5, 4, 6]), ), 0)
output = relay.Tuple([call_7709,call_7734,var_7735,])
output2 = relay.Tuple([call_7710,call_7736,var_7735,])
func_7740 = relay.Function([var_7735,], output)
mod['func_7740'] = func_7740
mod = relay.transform.InferType()(mod)
mutated_mod['func_7740'] = func_7740
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7741 = relay.var("var_7741", dtype = "uint16", shape = (120,))#candidate|7741|(120,)|var|uint16
func_7740_call = mutated_mod.get_global_var('func_7740')
call_7742 = func_7740_call(var_7741)
output = call_7742
func_7743 = relay.Function([var_7741], output)
mutated_mod['func_7743'] = func_7743
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7748 = relay.var("var_7748", dtype = "bool", shape = (6, 12, 12))#candidate|7748|(6, 12, 12)|var|bool
var_7749 = relay.var("var_7749", dtype = "bool", shape = (6, 12, 12))#candidate|7749|(6, 12, 12)|var|bool
bop_7750 = relay.logical_and(var_7748.astype('bool'), relay.reshape(var_7749.astype('bool'), relay.shape_of(var_7748))) # shape=(6, 12, 12)
func_5389_call = mod.get_global_var('func_5389')
func_5390_call = mutated_mod.get_global_var('func_5390')
call_7754 = relay.TupleGetItem(func_5389_call(), 0)
call_7755 = relay.TupleGetItem(func_5390_call(), 0)
func_4089_call = mod.get_global_var('func_4089')
func_4091_call = mutated_mod.get_global_var('func_4091')
call_7756 = func_4089_call()
call_7757 = func_4089_call()
func_6700_call = mod.get_global_var('func_6700')
func_6703_call = mutated_mod.get_global_var('func_6703')
var_7765 = relay.var("var_7765", dtype = "bool", shape = (2, 448))#candidate|7765|(2, 448)|var|bool
call_7764 = relay.TupleGetItem(func_6700_call(relay.reshape(var_7765.astype('bool'), [28, 32])), 1)
call_7766 = relay.TupleGetItem(func_6703_call(relay.reshape(var_7765.astype('bool'), [28, 32])), 1)
uop_7768 = relay.acosh(var_7765.astype('float64')) # shape=(2, 448)
func_7063_call = mod.get_global_var('func_7063')
func_7064_call = mutated_mod.get_global_var('func_7064')
call_7771 = relay.TupleGetItem(func_7063_call(), 0)
call_7772 = relay.TupleGetItem(func_7064_call(), 0)
uop_7773 = relay.sin(uop_7768.astype('float64')) # shape=(2, 448)
bop_7782 = relay.left_shift(uop_7768.astype('int16'), relay.reshape(uop_7773.astype('int16'), relay.shape_of(uop_7768))) # shape=(2, 448)
output = relay.Tuple([bop_7750,call_7754,call_7756,call_7764,call_7771,bop_7782,])
output2 = relay.Tuple([bop_7750,call_7755,call_7757,call_7766,call_7772,bop_7782,])
func_7786 = relay.Function([var_7748,var_7749,var_7765,], output)
mod['func_7786'] = func_7786
mod = relay.transform.InferType()(mod)
var_7787 = relay.var("var_7787", dtype = "bool", shape = (6, 12, 12))#candidate|7787|(6, 12, 12)|var|bool
var_7788 = relay.var("var_7788", dtype = "bool", shape = (6, 12, 12))#candidate|7788|(6, 12, 12)|var|bool
var_7789 = relay.var("var_7789", dtype = "bool", shape = (2, 448))#candidate|7789|(2, 448)|var|bool
output = func_7786(var_7787,var_7788,var_7789,)
func_7790 = relay.Function([var_7787,var_7788,var_7789,], output)
mutated_mod['func_7790'] = func_7790
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6610_call = mod.get_global_var('func_6610')
func_6611_call = mutated_mod.get_global_var('func_6611')
call_7832 = relay.TupleGetItem(func_6610_call(), 0)
call_7833 = relay.TupleGetItem(func_6611_call(), 0)
func_6610_call = mod.get_global_var('func_6610')
func_6611_call = mutated_mod.get_global_var('func_6611')
call_7857 = relay.TupleGetItem(func_6610_call(), 0)
call_7858 = relay.TupleGetItem(func_6611_call(), 0)
func_5799_call = mod.get_global_var('func_5799')
func_5801_call = mutated_mod.get_global_var('func_5801')
var_7863 = relay.var("var_7863", dtype = "bool", shape = (896,))#candidate|7863|(896,)|var|bool
call_7862 = relay.TupleGetItem(func_5799_call(relay.reshape(var_7863.astype('bool'), [28, 32])), 8)
call_7864 = relay.TupleGetItem(func_5801_call(relay.reshape(var_7863.astype('bool'), [28, 32])), 8)
func_114_call = mod.get_global_var('func_114')
func_117_call = mutated_mod.get_global_var('func_117')
const_7923 = relay.const([[2.965847,-9.447599,-6.023878,-4.596846,7.051458,3.412364,-5.289736,4.760370,8.813301,7.237275,2.715802,-9.488465,3.722419,2.830825,-5.645848,9.461626,-8.334727,7.790710,3.039862,-2.330353,3.799424,-5.465143,-7.622890,8.710974,1.788672,-9.892848,3.843461,-1.067894,-2.060155,8.349731,-1.311980,9.905206,-3.127658,5.091891,-2.121566,-0.643970,-5.113174,4.967628,-4.936147,-3.147130,-4.242375,-4.061232,4.459141,-8.103130,5.491577,-3.899507,-5.352211,-2.061636,-3.557025,-6.443486,8.308226,-7.150181,6.056460,-7.286952,-7.471226,7.984565,-6.027005,8.460119,7.588314,6.070916,9.261447,-0.513527,0.202264,-9.361390,-4.188091,5.875858,7.700083,7.239270,6.813972,1.256498,-6.578979,-0.027276,-5.149080,-2.127237,3.019250,-8.519944,8.287084,-2.781316,-2.208159,-9.967304,8.460208,-2.280130,1.189490,7.690646,-4.371692,8.513494,-3.209488,5.464073,4.660647,-1.929184,3.185509,3.923274,7.590694,-0.676433,-1.927617,-9.749749,-4.208070,-4.455382,0.643791,-6.929554,-1.766937,-8.916313,-2.831536,-1.172900,-2.042948,-9.889847,4.850716,-2.333143,-2.554113,-6.961772,-1.925863,-7.493310,-3.076138,-9.608648,5.827473,0.936572,-2.349462,-2.273121,9.285811,-4.814897,3.112758,1.824200,-8.168352,1.512540,-1.626950,9.336078,-0.972871,7.830208,9.730230,-7.614588,1.966532,-0.734909,-3.495479,-6.455491,8.579921]], dtype = "float64")#candidate|7923|(1, 135)|const|float64
call_7922 = func_114_call(relay.reshape(const_7923.astype('float64'), [9, 15, 1]))
call_7924 = func_114_call(relay.reshape(const_7923.astype('float64'), [9, 15, 1]))
output = relay.Tuple([call_7832,call_7857,call_7862,var_7863,call_7922,const_7923,])
output2 = relay.Tuple([call_7833,call_7858,call_7864,var_7863,call_7924,const_7923,])
func_7938 = relay.Function([var_7863,], output)
mod['func_7938'] = func_7938
mod = relay.transform.InferType()(mod)
mutated_mod['func_7938'] = func_7938
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7939 = relay.var("var_7939", dtype = "bool", shape = (896,))#candidate|7939|(896,)|var|bool
func_7938_call = mutated_mod.get_global_var('func_7938')
call_7940 = func_7938_call(var_7939)
output = call_7940
func_7941 = relay.Function([var_7939], output)
mutated_mod['func_7941'] = func_7941
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7563_call = mod.get_global_var('func_7563')
func_7564_call = mutated_mod.get_global_var('func_7564')
call_7968 = relay.TupleGetItem(func_7563_call(), 0)
call_7969 = relay.TupleGetItem(func_7564_call(), 0)
func_534_call = mod.get_global_var('func_534')
func_537_call = mutated_mod.get_global_var('func_537')
var_7973 = relay.var("var_7973", dtype = "int8", shape = (1568,))#candidate|7973|(1568,)|var|int8
call_7972 = relay.TupleGetItem(func_534_call(relay.reshape(var_7973.astype('int8'), [16, 7, 14])), 2)
call_7974 = relay.TupleGetItem(func_537_call(relay.reshape(var_7973.astype('int8'), [16, 7, 14])), 2)
var_7975 = relay.var("var_7975", dtype = "float64", shape = (135,))#candidate|7975|(135,)|var|float64
bop_7976 = relay.bitwise_and(call_7972.astype('int32'), relay.reshape(var_7975.astype('int32'), relay.shape_of(call_7972))) # shape=(135,)
bop_7979 = relay.bitwise_and(call_7974.astype('int32'), relay.reshape(var_7975.astype('int32'), relay.shape_of(call_7974))) # shape=(135,)
func_7938_call = mod.get_global_var('func_7938')
func_7941_call = mutated_mod.get_global_var('func_7941')
var_7984 = relay.var("var_7984", dtype = "bool", shape = (896,))#candidate|7984|(896,)|var|bool
call_7983 = relay.TupleGetItem(func_7938_call(relay.reshape(var_7984.astype('bool'), [896,])), 5)
call_7985 = relay.TupleGetItem(func_7941_call(relay.reshape(var_7984.astype('bool'), [896,])), 5)
func_1652_call = mod.get_global_var('func_1652')
func_1655_call = mutated_mod.get_global_var('func_1655')
const_7987 = relay.const([[3.331151],[5.032839],[0.355893],[1.277583],[4.947969],[4.792294],[9.000497],[3.622921],[-0.207048],[1.603866],[-3.025585],[9.966448],[-2.495884],[2.088845],[-7.710398],[2.489297],[1.704690],[1.595551],[7.994168],[9.543460],[5.359856],[4.316631],[2.970460],[-0.828098],[-0.190800],[6.398279],[9.953378],[5.764921],[0.475460],[2.435624],[9.034799],[3.184655],[5.675896],[9.938609],[-7.904585],[0.598963],[6.363967],[-9.028301],[-3.303652],[-3.195034],[-4.005760],[1.675042],[8.426486],[5.827722],[0.823725],[-0.551755],[1.035021],[0.901083],[6.742686],[-3.542405],[-3.514787],[7.782438],[-0.040797],[-9.953270],[3.019099],[3.248341],[-9.482754],[7.584313],[0.734704],[9.941417],[6.227665],[6.430858],[9.266369],[-1.455134],[0.980352],[-5.879217],[-8.311308],[3.821759],[7.410354],[3.828237],[5.587645],[2.937087],[5.609872],[0.039604],[6.130690],[7.305817],[-0.577332],[-7.963186],[-3.388725],[-0.501595],[0.694622],[1.355267],[0.843725],[-0.745769],[-1.379979],[3.452396],[-7.677663],[1.017964],[4.896661],[3.795741],[1.290625],[-4.064010],[8.391717],[-7.964659],[2.725953],[-1.947921],[7.730359],[-8.772533],[-8.976372],[-1.405921],[4.318944],[-1.917069],[-3.761000],[9.962639],[-4.134457],[-9.931184],[-0.064492],[-5.239452],[5.695042],[2.020657],[1.152936],[9.163845],[4.243618],[4.517353],[-6.758145],[-6.228023],[7.474877],[-6.052065],[-9.676598],[-8.322348],[-3.466049],[0.759051],[6.567600],[-6.255724],[-1.419462],[5.084609],[4.323674],[-8.546746],[-2.470373],[8.994674],[1.936358],[-6.664334],[-4.514290],[-7.841079],[4.951125],[-9.650268],[-0.050773],[-8.118467],[0.175886],[-8.944326],[-7.418532],[0.029561],[7.209128],[-9.811123],[-6.022843],[-3.216377],[2.089993],[-9.173511],[0.383526],[-9.575127],[4.428989],[-8.666780],[-8.665793],[5.959763],[-2.584768],[4.527637],[7.323413],[-5.163363],[6.522534],[7.151775],[-9.472238],[5.412147],[-3.166196],[-3.547413],[4.468910],[-7.278637],[5.464902],[-0.707175],[0.335144],[1.997509],[3.925351],[-5.872118],[8.909171],[7.659194],[2.682812],[-8.285957],[4.204671],[5.212046],[-2.422518],[8.583169],[9.881605],[-3.268811],[9.069726],[-4.236517],[7.634080],[-4.934114],[4.369127],[9.903250],[0.027391],[2.279120],[5.460911],[2.554610],[7.183085],[9.374755],[-5.559799],[4.251452],[-2.746854],[-5.279137],[-6.267644],[7.566477],[-6.310579],[3.749535],[-5.981331],[-1.815846],[0.527982],[7.870180],[-8.282631],[8.328069],[4.666938],[6.960444]], dtype = "float32")#candidate|7987|(210, 1)|const|float32
var_7988 = relay.var("var_7988", dtype = "float32", shape = (630,))#candidate|7988|(630,)|var|float32
call_7986 = func_1652_call(relay.reshape(const_7987.astype('float32'), [15, 1, 14]), relay.reshape(var_7988.astype('float32'), [15, 3, 14]), )
call_7989 = func_1652_call(relay.reshape(const_7987.astype('float32'), [15, 1, 14]), relay.reshape(var_7988.astype('float32'), [15, 3, 14]), )
output = relay.Tuple([call_7968,var_7973,bop_7976,call_7983,var_7984,call_7986,const_7987,var_7988,])
output2 = relay.Tuple([call_7969,var_7973,bop_7979,call_7985,var_7984,call_7989,const_7987,var_7988,])
func_7998 = relay.Function([var_7973,var_7975,var_7984,var_7988,], output)
mod['func_7998'] = func_7998
mod = relay.transform.InferType()(mod)
mutated_mod['func_7998'] = func_7998
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7998_call = mutated_mod.get_global_var('func_7998')
var_8000 = relay.var("var_8000", dtype = "int8", shape = (1568,))#candidate|8000|(1568,)|var|int8
var_8001 = relay.var("var_8001", dtype = "float64", shape = (135,))#candidate|8001|(135,)|var|float64
var_8002 = relay.var("var_8002", dtype = "bool", shape = (896,))#candidate|8002|(896,)|var|bool
var_8003 = relay.var("var_8003", dtype = "float32", shape = (630,))#candidate|8003|(630,)|var|float32
call_7999 = func_7998_call(var_8000,var_8001,var_8002,var_8003,)
output = call_7999
func_8004 = relay.Function([var_8000,var_8001,var_8002,var_8003,], output)
mutated_mod['func_8004'] = func_8004
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6610_call = mod.get_global_var('func_6610')
func_6611_call = mutated_mod.get_global_var('func_6611')
call_8042 = relay.TupleGetItem(func_6610_call(), 1)
call_8043 = relay.TupleGetItem(func_6611_call(), 1)
output = relay.Tuple([call_8042,])
output2 = relay.Tuple([call_8043,])
func_8044 = relay.Function([], output)
mod['func_8044'] = func_8044
mod = relay.transform.InferType()(mod)
output = func_8044()
func_8045 = relay.Function([], output)
mutated_mod['func_8045'] = func_8045
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5992_call = mod.get_global_var('func_5992')
func_5993_call = mutated_mod.get_global_var('func_5993')
call_8070 = relay.TupleGetItem(func_5992_call(), 0)
call_8071 = relay.TupleGetItem(func_5993_call(), 0)
output = call_8070
output2 = call_8071
func_8082 = relay.Function([], output)
mod['func_8082'] = func_8082
mod = relay.transform.InferType()(mod)
output = func_8082()
func_8083 = relay.Function([], output)
mutated_mod['func_8083'] = func_8083
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7534_call = mod.get_global_var('func_7534')
func_7536_call = mutated_mod.get_global_var('func_7536')
call_8087 = relay.TupleGetItem(func_7534_call(), 0)
call_8088 = relay.TupleGetItem(func_7536_call(), 0)
func_214_call = mod.get_global_var('func_214')
func_219_call = mutated_mod.get_global_var('func_219')
const_8095 = relay.const([[4.443291,8.895550,6.094600,2.125233,7.159553,7.103436,-3.001067,-0.089842,-8.280436,-7.166696,3.115899,2.594583,-0.037927,-0.398210,0.210001,1.986288,-8.517235,8.056760,1.929166,4.654133,0.771878,4.792442,2.910728,0.863583,6.703097,-3.713822,5.732808,1.152110,-3.819790,-4.823033],[6.034558,-3.909654,-7.221899,4.510779,0.125838,-2.218337,-5.577001,-7.054431,8.083714,8.647608,-5.307742,8.188095,-0.844987,1.292623,-6.613476,-9.386931,6.731736,-5.526971,-6.953739,7.946741,-3.428237,-6.170148,-9.421245,-6.595688,-4.958455,-0.956978,-0.748941,-8.010777,-0.388118,1.887892],[-2.983720,-6.516786,8.455326,5.040191,-4.415583,9.749109,2.527965,1.738591,-3.567363,8.781671,-6.462083,2.957424,-5.343551,5.775258,6.635132,4.410730,-0.237639,1.609812,-8.910676,5.043918,-0.585432,-4.334435,1.092987,2.775132,7.518182,-8.453293,-3.531807,-5.958981,-3.804573,5.717542],[2.413619,6.788104,-3.000005,1.245890,7.087016,3.889524,9.584515,2.778776,-9.815884,-7.466821,-3.030265,0.541887,4.466560,7.901783,0.655718,6.016970,4.813026,-5.353301,-6.753406,1.176729,-3.694275,3.614688,-2.866365,-2.774970,1.334430,-4.425286,-3.714474,-0.036717,-8.094854,8.533690],[-1.931158,-2.668030,5.429533,7.629757,-2.625757,9.044421,3.160671,-8.530757,-9.057243,-7.048300,5.992859,9.949048,-5.261137,6.710769,2.012213,-8.468592,-7.032064,9.908106,9.514242,7.206882,2.920478,9.605853,4.601967,-8.741105,-0.933575,4.019053,-4.995935,1.667406,-2.492484,9.421815],[2.557014,7.747403,-0.210436,3.168216,0.939182,7.810538,-0.627804,0.324961,-9.517277,3.808760,2.420818,-9.883617,9.665629,-5.991558,3.123914,1.635312,-6.693217,-7.471172,3.245995,-8.825927,-2.976651,-8.285962,-2.764571,-3.806418,9.791404,-2.459088,-6.988652,-2.555016,-8.482209,1.906086]], dtype = "float32")#candidate|8095|(6, 30)|const|float32
const_8096 = relay.const([False,False,False,False,True,False,True,True,False,True,True,False,True,True,True,False,False,False,True,True,False,False,True,True,True,True,False,True,False,False,True,True,True,True,True,False,True,True,False,False,False,True,False,True,True,True,True,True,True,False,False,True,False,True,False,True,False,True,False,True,True,True,False,False,False,True,True,True,False,True,True,False,False,True,True,True,False,False,False,False,False,False,True,False,False,False,True,False,True,True,True,False,False,True,True,False,True,False,False,True,True,True,False,True,True,True,True,True,False,True,True,False,False,True,True,False,True,False,False,False,False,False,False,False,True,True,True,False,True,True,False,False,False,False,False,True,True,True,True,True,False,False,False,False,True,True,False,False,True,True,False,True,True,True,False,False,False,True,True,False,False,True,False,False,True,False,False,False,True,True,False,False,True,False,False,True,True,True,True,False,False,False,False,True,True,False,True,True,True,False,True,True,True,False,True,False,False,True,True,False,False,True,False,False,True,False,True,False,True,False,False,True,False,False,False,True,False,False,True,True,False,False,False,False,False,False,False,True,True,True,True,False,False,True,False,True,True,True,True,True,True,False,False,False,False,True,True,True,True,False,False,True,True,True,True,True,True,False,False,False,True,True,False,False,False,False,True,False,True,True,True,True,True,True,True,True,False,False,False,True,True,True,True,False,False,False,True,True,False,False,True,False,True,False,False,False,False,True,False,False,False,True,True,True,False,False,True,True,False,True,False,True,False,True,True,False,False,True,True,False,True,True,False,False,True,False,False,True,False,False,True,False,True,False,False,False,False,True,True,True,False,True,False,True,True,False,True,True,True,True,True,False,False,False,False,True,False,True,False,False,True,False,True,True,False,True,True,True,False,False,False,False,True,False,True,False,False,True,True,True,False,True,True,False,True,False,True,True,True,True,False,False,True,True,True,False,False,False,True,False,False,True,False,False,True,False,False,False,True,False,True,True,True,True,True,False,True,False,True,False,True,True,False,True,False,False,True,False,False,False,False,True,True,True,True,False,True,True,False,False,True,False,True,False,True,False,False,False,False,False,False,True,True,False,False,False,False,True,False,True,True,True,False,False,False,True,True,True,False,True,True,False,True,False,False,False,False,True,False,False,True,False,True,False,True,False,False,True,True,True,False,True,False,False,True,False,True,False,True,False,False,False,False,True,False,False,False,False,True,False,False,False,True,True,True,False,True,True,True,True,False,False,False,False,False,True,False,False,False,True,False,False,True,False,True,True,False,True,True,False,False,True,False,True,True,True,True,False,True,False,True,True,False,True,False,True,True,False,True,True,False,True,True,True,True,False,True,True,False,False,True,False,False,False,True,True,True,False,True,False,False,True,False,True,False,False,False,True,False,True,False,False,False,True,False,True,False,True,False,False,True,False,False,True,False,True,False,True,True,False,False,True,True,False,False,True,False,False,True,False,True,True,True,True,True,True,False,True,False,True,True,True,True,True,True,True,False,True,False,True,True,False,False,False,False,True,False,False,True,True,True,True,False,False,False,True,True,True,False,True,False,True,False,True,False,True,False,False,True,False,True,False,True,False,True,True,True,True,False,False,False,True,True,False,True,False,False,False,True,False,True,True,False,True,False,False,True,False,True,False,False,False,False,True,False,True,True,True,False,True,False,False,False,True,True,True,True,True,True,False,True,False,True,True,True,True,False,False,True,True,False,False,True,True,True,False,False,False,True,True,True,True,True,True,True,False,False,False,True,True,True,True,True,False,False,True,False,False,True,True,True,False,True,True,True,True,True,True,True,False,False,True,False,False,False,True,False,True,True,False,False,False,True,False,True,True,True,True,False,False,False,True,False,False,False,True,True,True,True,False,False,True,True,False,True,False,True,False,True,False,False,True,True,True,True,False,False,False,True,False,True,True,False,True,True,False,True,False,False,False,True,False,True,False,False,True,False,True,True,True,True,True,True,False,False,False,False,False,True,True,True,False,True,True,True,False,True,False,True,True,False,False,True,False,False,True,True,True,False,False,False,False,True,True,False,True,False,True,True,True,False,False,True,True,True,False,False,True,True,True,False,True,True,False,True,True], dtype = "bool")#candidate|8096|(896,)|const|bool
call_8094 = relay.TupleGetItem(func_214_call(relay.reshape(const_8095.astype('float32'), [15, 4, 3]), relay.reshape(const_8095.astype('float32'), [15, 4, 3]), relay.reshape(const_8096.astype('bool'), [56, 16]), ), 2)
call_8097 = relay.TupleGetItem(func_219_call(relay.reshape(const_8095.astype('float32'), [15, 4, 3]), relay.reshape(const_8095.astype('float32'), [15, 4, 3]), relay.reshape(const_8096.astype('bool'), [56, 16]), ), 2)
func_5088_call = mod.get_global_var('func_5088')
func_5090_call = mutated_mod.get_global_var('func_5090')
call_8100 = relay.TupleGetItem(func_5088_call(relay.reshape(call_8087.astype('float32'), [11, 14, 12])), 0)
call_8101 = relay.TupleGetItem(func_5090_call(relay.reshape(call_8087.astype('float32'), [11, 14, 12])), 0)
output = relay.Tuple([call_8087,call_8094,const_8095,const_8096,call_8100,])
output2 = relay.Tuple([call_8088,call_8097,const_8095,const_8096,call_8101,])
func_8106 = relay.Function([], output)
mod['func_8106'] = func_8106
mod = relay.transform.InferType()(mod)
output = func_8106()
func_8107 = relay.Function([], output)
mutated_mod['func_8107'] = func_8107
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6581_call = mod.get_global_var('func_6581')
func_6582_call = mutated_mod.get_global_var('func_6582')
call_8146 = relay.TupleGetItem(func_6581_call(), 0)
call_8147 = relay.TupleGetItem(func_6582_call(), 0)
func_6061_call = mod.get_global_var('func_6061')
func_6062_call = mutated_mod.get_global_var('func_6062')
call_8150 = func_6061_call()
call_8151 = func_6061_call()
output = relay.Tuple([call_8146,call_8150,])
output2 = relay.Tuple([call_8147,call_8151,])
func_8171 = relay.Function([], output)
mod['func_8171'] = func_8171
mod = relay.transform.InferType()(mod)
mutated_mod['func_8171'] = func_8171
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8171_call = mutated_mod.get_global_var('func_8171')
call_8172 = func_8171_call()
output = call_8172
func_8173 = relay.Function([], output)
mutated_mod['func_8173'] = func_8173
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7563_call = mod.get_global_var('func_7563')
func_7564_call = mutated_mod.get_global_var('func_7564')
call_8184 = relay.TupleGetItem(func_7563_call(), 0)
call_8185 = relay.TupleGetItem(func_7564_call(), 0)
func_5732_call = mod.get_global_var('func_5732')
func_5733_call = mutated_mod.get_global_var('func_5733')
call_8197 = relay.TupleGetItem(func_5732_call(), 0)
call_8198 = relay.TupleGetItem(func_5733_call(), 0)
output = relay.Tuple([call_8184,call_8197,])
output2 = relay.Tuple([call_8185,call_8198,])
func_8205 = relay.Function([], output)
mod['func_8205'] = func_8205
mod = relay.transform.InferType()(mod)
mutated_mod['func_8205'] = func_8205
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8205_call = mutated_mod.get_global_var('func_8205')
call_8206 = func_8205_call()
output = call_8206
func_8207 = relay.Function([], output)
mutated_mod['func_8207'] = func_8207
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8242 = relay.var("var_8242", dtype = "float64", shape = (2, 13, 6))#candidate|8242|(2, 13, 6)|var|float64
uop_8243 = relay.asin(var_8242.astype('float64')) # shape=(2, 13, 6)
func_6141_call = mod.get_global_var('func_6141')
func_6143_call = mutated_mod.get_global_var('func_6143')
call_8246 = relay.TupleGetItem(func_6141_call(), 0)
call_8247 = relay.TupleGetItem(func_6143_call(), 0)
output = relay.Tuple([uop_8243,call_8246,])
output2 = relay.Tuple([uop_8243,call_8247,])
func_8253 = relay.Function([var_8242,], output)
mod['func_8253'] = func_8253
mod = relay.transform.InferType()(mod)
mutated_mod['func_8253'] = func_8253
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8254 = relay.var("var_8254", dtype = "float64", shape = (2, 13, 6))#candidate|8254|(2, 13, 6)|var|float64
func_8253_call = mutated_mod.get_global_var('func_8253')
call_8255 = func_8253_call(var_8254)
output = call_8255
func_8256 = relay.Function([var_8254], output)
mutated_mod['func_8256'] = func_8256
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5625_call = mod.get_global_var('func_5625')
func_5627_call = mutated_mod.get_global_var('func_5627')
call_8263 = func_5625_call()
call_8264 = func_5625_call()
func_4089_call = mod.get_global_var('func_4089')
func_4091_call = mutated_mod.get_global_var('func_4091')
call_8267 = func_4089_call()
call_8268 = func_4089_call()
uop_8281 = relay.atanh(call_8267.astype('float32')) # shape=(11, 14, 12)
uop_8283 = relay.atanh(call_8268.astype('float32')) # shape=(11, 14, 12)
func_4459_call = mod.get_global_var('func_4459')
func_4463_call = mutated_mod.get_global_var('func_4463')
const_8310 = relay.const([2,-1,2,4,-10,1,-10,3,2,-3,2,-4,-3,6,9,-1,9,7,5,-5,-4,-7,5,-4,-7,-8,5,4,2,-5,-7,-6,-2,8,-4,-4,-9,-5,-5,1,-3,3,-5,-7,-8,8,3,-10,6,-4,-2,1,3,8,-4,-2,-10,-7,1,-1,-6,-2,2,-4,1,9,8,7,-7,-9,-5,-7,3,1,-8,1,-9,3,-7,10,-4,-3,10,-4,-6,5,2,-8,6,1,10,-7,6,-2,6,-9,10,3,-4,6,-9,-1,3,-8,-9,-2,-10,7,9,-7,1,5,9,-1,4,3,8,-4,5,1,-8,2,4,-4,-9,9,-6,-1,-2,-8,-2,2,8,3,10,7,9,-8,9,7,10,5,-10,-10,1,-1,-2,-2,-2,2,-9,10,8,-2,-7,-2,4,-4,6,-7,6,9,-2,6,6,-6,7,-4,3,2,4,8,5,-2,-7,-9,6,1,-1,-4,5,1,-7,8,10,1,-6,-1,2,-2,-2,-4,-1,10,1,6,-5,7,5,-1,7,-10,-2,6,6,-5,-10,-9,-3,10,3,10,-6,-2,-2,5,-7,-4,6,3,7,10,-8,-6,-6,-4,4,-8,1,-1,-5,4,-1,-10,-6,9,-2,1,-8,10,-5,6,10,-10,-4,-4,7,-10,6,-5,5,-6,-5,-7,-5,-10,1,10,9,-2,2,3,-6,8,-3,4,9,2,-6,8,6,-2,3,10,-3,-7,2,6,1,2,9,1,-6,3,-4,5,-10,-8,-10,-6,-3,-2,3,5,-4,-9,2,2,-4,2,-7,-7,6,1,-4,-1,-2,-1,10,8,-2,-8,6,2,4,-8,-3,-9,10,4,-1,-2,9,7,-9,5,3,-6,1,8,4,-8,3,-5,-1,9,-8,-4,-4,8,7,9,-7,8,-4,5,6,-4,-5,2,-2,6,3,8,-3,5,10,-10,8,6,6,-10,7,9,-5,-5,-3,-8,3,6,-2,5,-2,10,-3,-9,-8,-9,-5,6,-1,-8,4,-3,-1,4,-7,-9,4,-10,-6,3,-10,-8,3,4,6,10,-9,8,1,7,-3,-10,4,1,9,-3,-8,-3,-6,7,-10,-4,2,-10,6,-3,-4,3,3,9,9,10,-4,8,-9,-3,-2,9,-9,-6,-8,3,4,-9,1,8,1,-7,10,-4,2,7,4,-7,6,-9,6,6,9,8,5,-2,-3,-9,8,-3,3,-4,7,10,-9,-8,3,5,-9,-4,9,1,6,-7,5,3,-10,-3,-10,-10,3,4,-2,-10,3,5,9,-6,-6,-9,2,9,1,-1,-8,-4,9,-9,-8,-1,-2,-3,-4,7,-3,-3,10,-1,5,-6,4,-3,7,-3,-10,5,5,-4,8,-9,10,10,-3,3,-2,10,-6,-9,7,-7,10,-1,-2,4,-8,3,-4,-8,-3,-6,9,-2,-10,-9,5,-6,-7,-10,5,9,6,3,-6,-10,1,7,-3,-6,-10,-2,8,9,-8,-6,-2,8,8,9,-4,4,-4,-7,10,2,6,-4,-5,-2,2,7,5,-10,-9,-9,-8,8,6,9,-7,-3,-4,-9,-9,-1,1,3,-5,10,-3,-5,-4,1,8,-5,8,8,-4,-10,-10,-4,-10,8,1,7,7,-3,7,-10,-1,-8,2,2,6,10,4,8,10,-7,-4,-3,8,-3,-9,8,9,-10,5,-8,5,-5,-10,10,9,-1,2,3,9,5,-10,-9,-10,-7,-2,-3,2,5,-3,2,-4,4,-8,-8,-4,6,-5,-10,-5,-7,3,-5,10,-7,-6,-2,3,-8,4,9,-8,-9,-1,5,7,4,-4,2,-2,4,9,10,-3,-4,-4,-2,-9,3,-9,5,-2,5,-1,-9,-8,-3,-8,-1,-1,7,-10,-8,-9,9,1,5,5,1,-7,-9,3,3,6,4,9,-5,-10,7,5,-9,-10,-4,-4,-10,-5,-7,-2,-4,2,-6,-9,1,-5,9,4,8,2,-8,-7,7,-9,2,3,-10,4,-8,-8,-2,-9,2,-9,-7,2,-7,-4,-1,-7,6,1,-6,3,-7,5,3,10,-7,-6,2,-2,5,1,10,-10,-9,10,3,-9,4,2,10,-3,-3,-3,-8,-1,-10,-10,-2,7,-9,-7,2,-7,-10,4,-10,-8,7,-5,-8,-8,1,-1,6,6,-6,-2,-9,-3,-5,-10,5,6,-1,8,9,8,-4,5,-6,7,-4,-10,-7,1,-1,7,-10,9,5,-1,-3,-4,-9,-7,4,6,-5,10,-9,-4,-3,-8,3,4,-7,2,-3,7,9,-6,-1,10,1,10,2,-2,-6,-8,10,-8,-7,8,-9,4,2,1,-4,-9,-1,-5,-6,6,7,-2,-7,7,1,6,2,-9,9,6,-1,6,-8,4,8,-4,5,-4,-6,-6,8,-8,1,-3,-7,4,5,-1,1,-7,-5,-3,-8,-3,-10,3,5,8,-1,8,9,-8,-4,-9,4,3,10,-10,-7,-3,5,4,-1,6,3,-2,6,9,10,-6,-8,4,6,-4,-8,-9,7,3,-8,-10,2,5,3,-9,-6,7,-3,9,6,10,4,-7,5,-9,-8,3,-2,-8,-4,5,-10,-1,-3,2,-8,3,4,-5,1,-3,4,7,-6,-10,-3,-10,7,-6,4,2,-4,5,7,8,-5,-5,9,-4,8,-7,9,4,9,-10,1,4,-7,3,9,1,4,-5,-9,-2,-5,10,4,-1,7,5,-5,3,-8,-7,-10,2,-4,9,-8,-2,9,6,-7,6,10,2,-10,7,-1,-4,-3,-5,5,-2,-6,-5,-8,8,-8,9,-6,3,-6,-2,7,8,-6,8,-8,4,5,-6,-10,10,9,-6,-2,8,3,7,-10,9,7,-7,6,-6,1,-5,10,-7,-7,-3,5,-9,5,-6,10,-1,1,-1,-7,1,2,-9,3,1,-2,-1,10,-5,7,-10,-7,3,6,8,-10,3,4,4,9,-9,10,6,-1,4,2,-6,-4,-10,2,8,-4,-6,3,6,-5,-3,-5,4,-1,8,4,-4,-3,-1,-2,-9,-1,7,-4,8,-7,4,-9,10,9,-5,1,3,4,9,6,4,-4,1,-3,-5,9,4,10,-10,-3,-3,-4,8,-4,-6,6,6,-3,8,-6,-8,-2,3,-8,10,7,6,2,1,-1,-6,9,7,-1,-9,7,1,2,3,8,1,-9,-9,9,8,-7,8,-6,-9,9,-3,-7,-8,-10,-9,8,-4,-7,9,2,-7,-2,6,-2,-3,7,9,-10,-5,10,9,-5,7,7,-9,3,-10,3,-1,5,7,-1,5,3,-4,-5,-3,7,6,5,-4,3,3,2,-10,9,-8,-4,-4,5,4,-2,-4,-8,-4,4,-3,-6,5,-10,4,4,2,6,-5,-5,-3,-7,-7,-5,-7,-2,8,-7,-5,-7,8,2,-7,7,9,2,-10,-7,1,-1,1,-1,1,-9,4,-7,7,-2,8,-8,-3,9,9,-10,7,3,5,6,-9,-4,3,7,3,-6,-9,9,7,5,3,-8,-7,8,-4,-9,1,8,-7,4,4,-4,-4,-5,1,9,-5,4,-8,7,-7,7,-2,-10,9,2,5,4,-6,-2,-9,1,-8,8,-5,9,1,-10,10,5,-5,1,-10,-1,8,-5,6,2,1,1,-7,10,8,-3,9,8,-5,-5,-7,-3,-4,1,4,-4,-5,1,-7,10,-10,-4,2,-2,-4,-2,-5,-8,-1,9,-4,10,-7,-1,-1,-10,7,9,-7,-6,10,-3,-3,6,-10,9,7,5,-2,10,9,-4,3,4,6,10,8,-3,-4,4,5,10,-5,-7,1,-10,-7,-7,-2,10,-2,6,-6,10,-9,6,2,-7,10,3,1,-2,-10,9,-9,-9,-9,-1,-3,5,-9,-7,8,7,-8,-1,-6,7,1,9,3,3,5,7,6,2,-4,6,1,-1,-8,7,-5,-1,10,-8,-9,7,4,-4,7,-6,6,-6,-7,-7,-9,-8,-1,-3,-10,6,-4,5,-8,-8,8,-9,-8,-3,-9,-8,5,5,7,-6,8,8,6,2,6,-10,-6,9,1,-8,10,-1,4,-10,-1,-7,10,-3,-9,-10,-6,9,7,-5,10,1,9,-7,-5,1,-5,6,-4,-2,5,1,-2,3,-10,10,-2,-10,-10,-2,-3,-10,5,-4,9,5,-7,7,-7,-9,-9,-5,-9,-1], dtype = "int8")#candidate|8310|(1568,)|const|int8
const_8311 = relay.const(4, dtype = "int8")#candidate|8311|()|const|int8
call_8309 = relay.TupleGetItem(func_4459_call(relay.reshape(const_8310.astype('int8'), [1568,]), relay.reshape(const_8311.astype('int8'), []), ), 2)
call_8312 = relay.TupleGetItem(func_4463_call(relay.reshape(const_8310.astype('int8'), [1568,]), relay.reshape(const_8311.astype('int8'), []), ), 2)
uop_8322 = relay.log10(uop_8281.astype('float32')) # shape=(11, 14, 12)
uop_8324 = relay.log10(uop_8283.astype('float32')) # shape=(11, 14, 12)
output = relay.Tuple([call_8263,call_8309,const_8310,const_8311,uop_8322,])
output2 = relay.Tuple([call_8264,call_8312,const_8310,const_8311,uop_8324,])
func_8327 = relay.Function([], output)
mod['func_8327'] = func_8327
mod = relay.transform.InferType()(mod)
mutated_mod['func_8327'] = func_8327
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8327_call = mutated_mod.get_global_var('func_8327')
call_8328 = func_8327_call()
output = call_8328
func_8329 = relay.Function([], output)
mutated_mod['func_8329'] = func_8329
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4800_call = mod.get_global_var('func_4800')
func_4802_call = mutated_mod.get_global_var('func_4802')
call_8410 = func_4800_call()
call_8411 = func_4800_call()
output = call_8410
output2 = call_8411
func_8439 = relay.Function([], output)
mod['func_8439'] = func_8439
mod = relay.transform.InferType()(mod)
output = func_8439()
func_8440 = relay.Function([], output)
mutated_mod['func_8440'] = func_8440
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8205_call = mod.get_global_var('func_8205')
func_8207_call = mutated_mod.get_global_var('func_8207')
call_8449 = relay.TupleGetItem(func_8205_call(), 0)
call_8450 = relay.TupleGetItem(func_8207_call(), 0)
func_7281_call = mod.get_global_var('func_7281')
func_7282_call = mutated_mod.get_global_var('func_7282')
call_8455 = relay.TupleGetItem(func_7281_call(), 1)
call_8456 = relay.TupleGetItem(func_7282_call(), 1)
output = relay.Tuple([call_8449,call_8455,])
output2 = relay.Tuple([call_8450,call_8456,])
func_8459 = relay.Function([], output)
mod['func_8459'] = func_8459
mod = relay.transform.InferType()(mod)
output = func_8459()
func_8460 = relay.Function([], output)
mutated_mod['func_8460'] = func_8460
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6141_call = mod.get_global_var('func_6141')
func_6143_call = mutated_mod.get_global_var('func_6143')
call_8477 = relay.TupleGetItem(func_6141_call(), 0)
call_8478 = relay.TupleGetItem(func_6143_call(), 0)
output = call_8477
output2 = call_8478
func_8479 = relay.Function([], output)
mod['func_8479'] = func_8479
mod = relay.transform.InferType()(mod)
mutated_mod['func_8479'] = func_8479
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8479_call = mutated_mod.get_global_var('func_8479')
call_8480 = func_8479_call()
output = call_8480
func_8481 = relay.Function([], output)
mutated_mod['func_8481'] = func_8481
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8515 = relay.var("var_8515", dtype = "float32", shape = (9, 13, 15))#candidate|8515|(9, 13, 15)|var|float32
uop_8516 = relay.exp(var_8515.astype('float32')) # shape=(9, 13, 15)
output = uop_8516
output2 = uop_8516
func_8518 = relay.Function([var_8515,], output)
mod['func_8518'] = func_8518
mod = relay.transform.InferType()(mod)
mutated_mod['func_8518'] = func_8518
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8519 = relay.var("var_8519", dtype = "float32", shape = (9, 13, 15))#candidate|8519|(9, 13, 15)|var|float32
func_8518_call = mutated_mod.get_global_var('func_8518')
call_8520 = func_8518_call(var_8519)
output = call_8520
func_8521 = relay.Function([var_8519], output)
mutated_mod['func_8521'] = func_8521
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7309_call = mod.get_global_var('func_7309')
func_7311_call = mutated_mod.get_global_var('func_7311')
call_8576 = relay.TupleGetItem(func_7309_call(), 0)
call_8577 = relay.TupleGetItem(func_7311_call(), 0)
func_6141_call = mod.get_global_var('func_6141')
func_6143_call = mutated_mod.get_global_var('func_6143')
call_8588 = relay.TupleGetItem(func_6141_call(), 0)
call_8589 = relay.TupleGetItem(func_6143_call(), 0)
output = relay.Tuple([call_8576,call_8588,])
output2 = relay.Tuple([call_8577,call_8589,])
func_8595 = relay.Function([], output)
mod['func_8595'] = func_8595
mod = relay.transform.InferType()(mod)
mutated_mod['func_8595'] = func_8595
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8595_call = mutated_mod.get_global_var('func_8595')
call_8596 = func_8595_call()
output = call_8596
func_8597 = relay.Function([], output)
mutated_mod['func_8597'] = func_8597
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7563_call = mod.get_global_var('func_7563')
func_7564_call = mutated_mod.get_global_var('func_7564')
call_8613 = relay.TupleGetItem(func_7563_call(), 0)
call_8614 = relay.TupleGetItem(func_7564_call(), 0)
func_6562_call = mod.get_global_var('func_6562')
func_6563_call = mutated_mod.get_global_var('func_6563')
call_8627 = func_6562_call()
call_8628 = func_6562_call()
output = relay.Tuple([call_8613,call_8627,])
output2 = relay.Tuple([call_8614,call_8628,])
func_8630 = relay.Function([], output)
mod['func_8630'] = func_8630
mod = relay.transform.InferType()(mod)
mutated_mod['func_8630'] = func_8630
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8630_call = mutated_mod.get_global_var('func_8630')
call_8631 = func_8630_call()
output = call_8631
func_8632 = relay.Function([], output)
mutated_mod['func_8632'] = func_8632
mutated_mod = relay.transform.InferType()(mutated_mod)
const_8633 = relay.const([[[-8,-8,-7,2,1,-8,-8,4,8,1,-3,2],[1,9,-3,-7,3,-9,4,10,-5,-10,7,-4],[-2,-4,-9,-4,-8,8,2,-2,3,-7,5,2],[-6,-3,-6,8,2,-4,-10,-3,1,-10,9,8],[-3,8,-2,10,-3,-3,-9,-9,-4,-6,-1,-3],[-2,-3,-6,2,-6,9,-1,8,-1,-4,-1,-3],[-6,-9,8,7,-8,-1,-1,-4,-5,7,-10,-1],[5,1,-10,2,5,-1,7,5,10,10,10,8],[-4,1,-9,5,10,1,2,6,-7,10,-6,-9],[-10,-8,10,-6,-3,8,-3,-6,-7,-5,-2,-6],[-7,-3,3,7,-1,-6,3,5,10,7,-6,-8],[-2,4,1,5,8,1,1,9,-5,5,8,3],[5,3,3,-4,4,10,-10,5,4,1,6,-9],[4,10,-6,-10,-10,-2,-4,-9,4,4,-6,-2],[-5,-8,-3,-3,-1,-9,-5,-7,1,10,-6,4]],[[10,-6,6,-9,-2,-5,3,4,-10,-10,1,10],[9,-7,-10,-6,8,-1,9,7,-6,-8,10,-1],[-2,-7,-10,-5,8,-5,3,-3,5,-5,-3,-8],[7,-5,6,9,-9,-3,3,2,-1,2,-10,7],[8,-2,6,-9,5,-10,-2,-1,5,-3,-3,10],[2,10,-6,9,-10,-4,-4,1,-6,2,-2,-10],[8,-3,-6,7,-4,2,-5,-3,-6,1,-9,9],[3,-3,6,-10,-7,-9,8,3,-4,-4,-7,-2],[-6,-3,3,-2,5,1,-9,8,-6,8,-3,-7],[-5,-6,10,5,10,2,-10,-2,-10,-6,4,4],[1,3,3,2,1,-10,5,8,3,-1,-4,8],[7,-2,8,-10,-10,-2,3,2,-2,-4,10,-4],[-1,8,1,-9,7,-9,9,-3,-2,-3,1,-6],[10,1,1,-2,2,8,-5,-10,-8,9,-8,-8],[9,3,7,-4,9,-6,1,-3,-10,-6,7,7]],[[-7,-7,-9,3,-8,-10,8,-3,-9,9,9,-5],[-4,3,-7,9,7,8,2,-7,-10,5,-3,6],[7,6,-7,4,1,5,8,-3,1,-4,-5,-1],[-10,-6,5,6,7,-10,2,8,-1,-3,-6,-7],[-10,-9,-4,3,-9,8,8,7,-8,2,1,5],[-10,3,7,-2,-5,-3,1,4,4,3,-5,-9],[-7,5,10,10,-8,-5,-6,-3,8,-9,-3,-1],[4,3,6,4,-5,-3,-7,-5,7,2,-7,-4],[3,5,6,-5,2,10,9,3,-1,9,9,-4],[1,4,1,4,1,9,7,-8,1,-9,1,4],[-10,1,4,8,3,5,9,-9,-1,10,4,7],[5,6,9,10,-3,-9,-10,4,8,-9,-1,9],[-9,-9,8,-6,3,-1,-2,-2,-3,3,7,-7],[7,3,-6,-9,3,8,4,-4,-8,9,-5,-4],[-1,4,-4,-4,8,-8,-2,-9,-7,-4,-1,-9]],[[-3,-8,9,-9,-10,-10,-5,-5,2,7,-4,-8],[-5,1,-1,4,1,4,-5,2,-7,2,-5,-5],[4,-2,10,7,-2,-9,1,7,-7,-1,4,-10],[6,-3,10,-9,-9,1,10,-3,10,-5,9,-2],[3,-1,-9,-9,2,5,1,-6,-4,10,-7,-6],[8,8,3,2,-7,2,3,-8,-5,-8,-6,7],[-1,6,1,-5,-5,-4,6,2,-10,-7,8,-7],[10,-1,2,-8,4,-3,10,-2,2,1,4,1],[-2,5,8,4,1,-6,-3,6,-10,2,6,5],[2,7,-1,-7,9,-2,-8,-4,-2,-2,7,-2],[-6,7,8,9,7,-5,-4,-1,6,1,10,5],[-6,-8,-4,9,5,-1,9,-3,5,7,2,-6],[9,-4,-3,-2,-5,-3,1,10,-2,-10,-10,7],[3,-9,-2,-3,2,-2,6,3,6,-2,-10,4],[-5,2,7,3,5,-5,8,-8,5,5,-5,5]],[[-6,10,-1,-9,9,4,-1,8,-10,1,-10,8],[8,-9,4,4,-2,6,-9,2,6,-5,-4,5],[7,3,6,7,7,-6,-9,-10,3,8,3,-9],[7,-8,-9,4,8,5,1,7,-7,8,3,9],[-6,-9,9,7,-4,-5,-7,-10,8,-10,-7,-8],[2,-2,-6,3,10,-10,-10,2,-2,-6,6,6],[1,-5,-3,-3,-9,-1,8,6,4,4,10,7],[-3,-1,-8,2,-2,-8,-10,-1,-5,-3,-4,8],[2,3,8,-6,-2,-9,-3,-8,8,10,-6,-6],[-3,6,5,-9,-8,10,2,-6,-4,-5,-5,-2],[10,2,4,8,8,-7,10,1,10,-5,-9,7],[5,10,6,7,-5,3,-9,-7,7,-2,-1,6],[-6,4,-1,9,-2,7,3,5,5,7,8,-2],[9,-1,-7,-4,7,6,-8,3,-8,-9,6,-8],[1,-4,-1,-4,-10,-3,-2,-10,4,5,3,-3]],[[10,-1,-7,5,6,4,10,6,-3,-7,-5,-1],[4,-10,-6,7,4,-2,7,-8,9,-10,2,-10],[-4,-9,5,9,-10,6,1,-1,1,7,-3,3],[-9,-2,9,-7,9,6,-7,-3,4,-2,3,4],[-9,4,-8,-3,-9,9,4,-3,-3,9,1,-7],[-1,2,4,-8,8,2,-8,-4,-7,5,2,-8],[-6,-5,9,4,2,-4,3,-9,3,-7,-6,9],[8,9,-1,-3,4,-6,1,-2,5,1,-9,8],[-4,4,8,7,7,-5,3,-7,-9,9,-10,-5],[9,4,-10,2,9,-6,-9,-4,1,5,9,-2],[-3,-10,-1,2,3,-8,8,7,-5,-4,-9,1],[10,-5,-9,9,7,-7,-4,-10,4,-8,-7,-2],[9,9,6,10,-7,7,4,-8,-3,1,5,-4],[9,-5,-8,-3,5,-7,-3,7,1,-5,-9,-6],[-9,10,8,7,8,8,-9,5,2,-4,-8,-2]],[[-6,6,2,-10,10,-7,5,-8,5,9,4,7],[5,-10,2,-3,-10,6,2,-5,5,3,-7,3],[6,6,-3,7,-4,-10,-8,7,-4,10,-8,-10],[-8,-4,-3,-8,6,-8,-9,-8,1,-1,3,-7],[-2,4,-1,-4,-5,-5,-5,7,9,4,-2,10],[10,-2,-1,9,5,7,8,-6,-2,-3,-4,-2],[-8,10,9,-3,5,-2,-4,2,-6,5,10,9],[2,1,-2,10,7,2,-4,-5,-10,-5,-9,2],[-8,9,8,-2,-10,10,-5,-4,4,10,-10,-7],[3,-3,-1,-8,-3,8,5,-4,2,8,4,-2],[9,6,-9,10,-5,4,9,4,9,1,-10,8],[9,-1,-10,-1,9,6,10,-1,8,-10,7,9],[4,9,-7,9,-7,-10,5,3,1,-3,-7,4],[8,-4,-8,3,5,7,3,9,-6,4,-10,-5],[-10,2,3,-7,-9,-7,6,-8,-2,-4,-9,-2]]], dtype = "uint8")#candidate|8633|(7, 15, 12)|const|uint8
const_8634 = relay.const([[[-7,-3,-3,-6,-5,6,2,2,1,-10,7,-3],[-6,2,-1,2,-5,4,9,-2,4,6,3,-10],[6,-7,2,3,10,-8,4,-8,4,-9,-2,7],[9,2,9,-6,-3,-7,-4,1,-8,4,8,2],[-4,4,2,-1,-7,2,-8,3,3,4,-2,1],[5,-3,9,-6,-6,8,4,-8,-6,-8,-7,4],[1,-7,-5,3,6,-5,-1,8,1,-3,7,7],[10,-6,6,-8,9,10,-6,4,-8,8,9,-5],[4,-7,-9,-4,2,7,1,-5,-3,-4,7,-2],[8,4,-8,8,-9,4,-1,-7,8,9,1,10],[10,-2,2,3,8,7,-8,-9,-10,-5,1,2],[-7,-1,-6,2,-4,2,-10,6,-2,-3,8,7],[5,8,5,-9,2,1,-10,-3,-7,2,10,5],[-1,-2,10,-6,1,-5,6,1,2,6,-4,8],[-6,9,8,-7,2,-7,-1,1,1,-10,-10,4]],[[2,-5,1,-8,-4,2,-2,-1,10,-1,5,5],[-8,10,8,9,6,-6,7,-3,-2,-1,7,3],[1,10,-5,-9,-2,10,-5,-9,1,7,1,9],[8,-10,-1,2,-6,-10,-9,-4,10,-10,1,5],[5,1,3,-9,-9,3,3,-4,10,-10,2,10],[5,6,-1,9,-4,-4,-10,5,-6,-9,-4,8],[8,-2,1,2,-4,-2,-1,3,-3,10,3,-3],[4,6,7,-3,-1,5,9,-7,-6,-9,2,-2],[-2,10,-8,2,7,3,3,10,2,-7,-3,-5],[-5,-7,10,-4,4,8,9,5,10,-1,-5,-9],[6,-10,-10,1,-1,4,10,6,2,-7,7,-6],[-1,2,-9,2,8,-6,7,6,8,3,-6,3],[4,10,1,8,4,-5,-2,-10,-7,9,-6,3],[-2,3,5,9,-3,1,-6,5,1,-5,-6,-1],[1,-8,4,-2,-8,-6,10,-4,-4,-8,-6,-10]],[[-4,-9,-8,-7,2,-8,7,-5,-7,-9,4,-10],[8,9,-3,-2,4,9,-4,2,2,-4,-4,-5],[10,5,-7,4,-5,9,2,8,5,-9,-6,8],[-3,-8,-3,-5,6,9,-7,9,8,3,-1,7],[8,4,-4,-1,-5,3,1,3,10,-3,4,2],[-9,-3,5,4,-3,9,-3,6,9,-7,1,-10],[-1,9,-4,-9,-5,-3,2,8,-10,-5,-7,-2],[-4,1,-1,6,5,-9,-6,1,-1,-4,4,8],[-8,6,6,4,-8,-5,7,1,5,-10,-10,-2],[5,-4,7,2,7,-1,-7,2,9,4,-9,7],[-7,-4,-7,-8,4,3,3,7,5,-2,-10,-8],[4,-6,-1,6,7,6,8,-6,5,-4,-5,8],[-8,2,5,-8,4,-3,-4,-2,10,-4,-10,-3],[-10,-3,9,-4,-2,-4,6,7,5,-2,8,3],[-2,8,-9,-6,9,5,3,-6,6,3,3,2]],[[9,-10,-8,4,-10,-1,-3,-10,-10,-2,-6,7],[10,4,1,3,1,-6,-6,10,-3,7,-10,10],[-3,3,3,-1,-2,-6,2,3,-3,-4,-7,7],[5,-8,10,-5,10,-2,9,-6,8,-6,-1,6],[5,-5,2,4,5,-2,-10,9,6,3,-5,-8],[10,3,-2,7,9,-2,5,10,-8,6,1,9],[9,3,-2,-8,7,-6,-10,-8,7,2,6,10],[4,5,5,3,6,7,8,-2,7,-6,1,8],[4,7,-1,7,7,1,3,-6,-1,-9,-10,-6],[9,6,5,-7,7,8,-5,3,6,1,-9,10],[-10,9,-10,-7,-4,-10,-10,-8,2,-4,3,-6],[3,-10,-4,2,-1,-4,-5,-3,-5,-8,9,9],[-3,8,-10,7,-4,8,7,-4,1,3,-8,-5],[-7,-7,2,-10,8,-1,4,4,4,6,1,2],[-7,-8,-1,-7,7,-7,-9,-3,6,-7,-1,8]],[[10,7,-5,3,-5,-6,-3,9,6,-10,4,4],[-9,-10,-2,6,-4,3,-5,1,9,-10,-2,-4],[-2,5,-2,-6,10,1,-4,-3,-3,10,-7,10],[10,-8,-9,-3,1,-7,-9,-3,-10,-2,-3,-5],[-5,8,7,6,8,-10,-6,-7,2,-9,-10,-1],[-7,7,10,-10,-8,-7,-6,2,6,-2,6,-1],[-5,9,-3,8,-3,-1,6,10,-8,10,-9,-10],[6,-9,-1,-1,1,2,10,3,4,8,5,-7],[-4,-9,-1,8,-10,8,-5,6,8,-1,9,-4],[10,-6,-2,2,-9,-9,-1,-8,1,-10,6,4],[5,4,1,-10,2,10,10,9,4,-10,4,3],[5,-4,1,-4,-5,-4,-6,1,-2,-1,-2,2],[8,-10,1,8,1,6,9,-10,-8,-5,9,-4],[7,-3,-6,7,-6,-8,4,-2,7,-7,-6,3],[1,10,-1,3,10,9,1,-9,4,-4,3,-3]],[[2,9,7,5,9,8,-10,10,-6,-5,4,4],[3,-8,3,-7,1,4,7,6,5,-7,-6,4],[-7,-9,-2,1,-2,-4,-8,10,8,-7,-5,2],[-8,4,8,-6,-6,-6,-9,-6,5,5,-10,5],[1,2,7,-6,2,9,-8,5,-3,4,9,4],[-9,-9,6,-6,8,-2,3,9,8,7,4,-1],[4,-10,7,-9,5,-7,4,7,-3,-4,-9,-4],[-1,-4,-1,-6,2,10,-2,-8,-8,5,10,1],[-2,-2,8,-7,-6,-7,-10,4,9,-3,-2,5],[8,2,-5,-5,-8,8,-4,-6,-8,7,-4,-1],[-6,3,7,-10,9,5,2,10,9,-5,-5,-5],[-4,2,-5,2,-7,-9,-4,-9,10,-8,6,-2],[8,-1,-8,7,-9,1,-1,-5,-7,-5,5,3],[-2,8,9,-4,-7,9,1,9,-6,-6,-3,-9],[7,-1,-10,10,5,9,-9,-2,-9,-4,-8,2]],[[3,-3,1,9,6,2,4,7,9,-5,10,-5],[-10,-3,1,-4,-5,3,7,-4,1,8,-8,-5],[10,5,9,10,8,10,1,6,-1,2,2,-2],[3,-6,-4,10,-3,3,-5,-3,-8,-4,7,5],[-2,7,-4,-5,-8,10,4,-5,4,-10,4,-4],[4,-1,10,10,-4,4,-7,-7,-1,-6,-8,5],[10,-3,-7,-7,6,6,6,6,5,10,-10,-7],[-7,-10,-6,8,-8,-8,-1,10,3,-1,-1,10],[8,8,-8,-1,-9,-1,3,9,-4,10,4,-1],[5,-7,-1,-2,9,-7,6,6,-6,-8,-8,-2],[-8,6,-2,10,-10,-2,7,10,-6,7,-4,5],[9,2,-4,8,7,-3,-4,6,1,-7,-4,6],[-5,-1,-3,-10,2,10,8,-8,-5,-6,6,-2],[-10,7,5,3,6,10,10,4,4,8,3,7],[-6,8,2,1,9,7,1,6,4,9,-8,8]]], dtype = "uint8")#candidate|8634|(7, 15, 12)|const|uint8
bop_8635 = relay.logical_xor(const_8633.astype('uint8'), relay.reshape(const_8634.astype('uint8'), relay.shape_of(const_8633))) # shape=(7, 15, 12)
output = bop_8635
output2 = bop_8635
func_8638 = relay.Function([], output)
mod['func_8638'] = func_8638
mod = relay.transform.InferType()(mod)
output = func_8638()
func_8639 = relay.Function([], output)
mutated_mod['func_8639'] = func_8639
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8205_call = mod.get_global_var('func_8205')
func_8207_call = mutated_mod.get_global_var('func_8207')
call_8668 = relay.TupleGetItem(func_8205_call(), 1)
call_8669 = relay.TupleGetItem(func_8207_call(), 1)
func_4925_call = mod.get_global_var('func_4925')
func_4926_call = mutated_mod.get_global_var('func_4926')
call_8711 = func_4925_call()
call_8712 = func_4925_call()
func_5249_call = mod.get_global_var('func_5249')
func_5251_call = mutated_mod.get_global_var('func_5251')
call_8715 = func_5249_call()
call_8716 = func_5249_call()
func_4800_call = mod.get_global_var('func_4800')
func_4802_call = mutated_mod.get_global_var('func_4802')
call_8717 = func_4800_call()
call_8718 = func_4800_call()
output = relay.Tuple([call_8668,call_8711,call_8715,call_8717,])
output2 = relay.Tuple([call_8669,call_8712,call_8716,call_8718,])
func_8719 = relay.Function([], output)
mod['func_8719'] = func_8719
mod = relay.transform.InferType()(mod)
mutated_mod['func_8719'] = func_8719
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8719_call = mutated_mod.get_global_var('func_8719')
call_8720 = func_8719_call()
output = call_8720
func_8721 = relay.Function([], output)
mutated_mod['func_8721'] = func_8721
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7309_call = mod.get_global_var('func_7309')
func_7311_call = mutated_mod.get_global_var('func_7311')
call_8735 = relay.TupleGetItem(func_7309_call(), 0)
call_8736 = relay.TupleGetItem(func_7311_call(), 0)
output = call_8735
output2 = call_8736
func_8779 = relay.Function([], output)
mod['func_8779'] = func_8779
mod = relay.transform.InferType()(mod)
output = func_8779()
func_8780 = relay.Function([], output)
mutated_mod['func_8780'] = func_8780
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5625_call = mod.get_global_var('func_5625')
func_5627_call = mutated_mod.get_global_var('func_5627')
call_8918 = func_5625_call()
call_8919 = func_5625_call()
output = call_8918
output2 = call_8919
func_8929 = relay.Function([], output)
mod['func_8929'] = func_8929
mod = relay.transform.InferType()(mod)
output = func_8929()
func_8930 = relay.Function([], output)
mutated_mod['func_8930'] = func_8930
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8961 = relay.var("var_8961", dtype = "float64", shape = (12, 4, 5))#candidate|8961|(12, 4, 5)|var|float64
uop_8962 = relay.sinh(var_8961.astype('float64')) # shape=(12, 4, 5)
bop_8970 = relay.left_shift(var_8961.astype('int8'), relay.reshape(uop_8962.astype('int8'), relay.shape_of(var_8961))) # shape=(12, 4, 5)
func_5249_call = mod.get_global_var('func_5249')
func_5251_call = mutated_mod.get_global_var('func_5251')
call_8974 = func_5249_call()
call_8975 = func_5249_call()
func_7401_call = mod.get_global_var('func_7401')
func_7405_call = mutated_mod.get_global_var('func_7405')
const_8987 = relay.const(4, dtype = "int8")#candidate|8987|()|const|int8
var_8988 = relay.var("var_8988", dtype = "bool", shape = (896,))#candidate|8988|(896,)|var|bool
call_8986 = relay.TupleGetItem(func_7401_call(relay.reshape(const_8987.astype('int8'), []), relay.reshape(var_8988.astype('bool'), [896,]), ), 0)
call_8989 = relay.TupleGetItem(func_7405_call(relay.reshape(const_8987.astype('int8'), []), relay.reshape(var_8988.astype('bool'), [896,]), ), 0)
bop_8991 = relay.bitwise_xor(uop_8962.astype('uint32'), relay.reshape(bop_8970.astype('uint32'), relay.shape_of(uop_8962))) # shape=(12, 4, 5)
func_7786_call = mod.get_global_var('func_7786')
func_7790_call = mutated_mod.get_global_var('func_7790')
var_8997 = relay.var("var_8997", dtype = "bool", shape = (864,))#candidate|8997|(864,)|var|bool
call_8996 = relay.TupleGetItem(func_7786_call(relay.reshape(var_8997.astype('bool'), [6, 12, 12]), relay.reshape(var_8997.astype('bool'), [6, 12, 12]), relay.reshape(var_8988.astype('bool'), [2, 448]), ), 2)
call_8998 = relay.TupleGetItem(func_7790_call(relay.reshape(var_8997.astype('bool'), [6, 12, 12]), relay.reshape(var_8997.astype('bool'), [6, 12, 12]), relay.reshape(var_8988.astype('bool'), [2, 448]), ), 2)
bop_8999 = relay.maximum(bop_8991.astype('int64'), relay.reshape(uop_8962.astype('int64'), relay.shape_of(bop_8991))) # shape=(12, 4, 5)
output = relay.Tuple([call_8974,call_8986,const_8987,var_8988,call_8996,var_8997,bop_8999,])
output2 = relay.Tuple([call_8975,call_8989,const_8987,var_8988,call_8998,var_8997,bop_8999,])
func_9002 = relay.Function([var_8961,var_8988,var_8997,], output)
mod['func_9002'] = func_9002
mod = relay.transform.InferType()(mod)
mutated_mod['func_9002'] = func_9002
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9002_call = mutated_mod.get_global_var('func_9002')
var_9004 = relay.var("var_9004", dtype = "float64", shape = (12, 4, 5))#candidate|9004|(12, 4, 5)|var|float64
var_9005 = relay.var("var_9005", dtype = "bool", shape = (896,))#candidate|9005|(896,)|var|bool
var_9006 = relay.var("var_9006", dtype = "bool", shape = (864,))#candidate|9006|(864,)|var|bool
call_9003 = func_9002_call(var_9004,var_9005,var_9006,)
output = call_9003
func_9007 = relay.Function([var_9004,var_9005,var_9006,], output)
mutated_mod['func_9007'] = func_9007
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5249_call = mod.get_global_var('func_5249')
func_5251_call = mutated_mod.get_global_var('func_5251')
call_9028 = func_5249_call()
call_9029 = func_5249_call()
func_5997_call = mod.get_global_var('func_5997')
func_5999_call = mutated_mod.get_global_var('func_5999')
call_9033 = relay.TupleGetItem(func_5997_call(), 0)
call_9034 = relay.TupleGetItem(func_5999_call(), 0)
func_5249_call = mod.get_global_var('func_5249')
func_5251_call = mutated_mod.get_global_var('func_5251')
call_9040 = func_5249_call()
call_9041 = func_5249_call()
func_7136_call = mod.get_global_var('func_7136')
func_7137_call = mutated_mod.get_global_var('func_7137')
call_9049 = relay.TupleGetItem(func_7136_call(), 0)
call_9050 = relay.TupleGetItem(func_7137_call(), 0)
func_6827_call = mod.get_global_var('func_6827')
func_6830_call = mutated_mod.get_global_var('func_6830')
const_9057 = relay.const(-1, dtype = "uint32")#candidate|9057|()|const|uint32
var_9058 = relay.var("var_9058", dtype = "uint16", shape = (150, 14))#candidate|9058|(150, 14)|var|uint16
call_9056 = relay.TupleGetItem(func_6827_call(relay.reshape(const_9057.astype('uint32'), []), relay.reshape(var_9058.astype('uint16'), [30, 70]), ), 0)
call_9059 = relay.TupleGetItem(func_6830_call(relay.reshape(const_9057.astype('uint32'), []), relay.reshape(var_9058.astype('uint16'), [30, 70]), ), 0)
func_4089_call = mod.get_global_var('func_4089')
func_4091_call = mutated_mod.get_global_var('func_4091')
call_9068 = func_4089_call()
call_9069 = func_4089_call()
output = relay.Tuple([call_9028,call_9033,call_9040,call_9049,call_9056,const_9057,var_9058,call_9068,])
output2 = relay.Tuple([call_9029,call_9034,call_9041,call_9050,call_9059,const_9057,var_9058,call_9069,])
func_9076 = relay.Function([var_9058,], output)
mod['func_9076'] = func_9076
mod = relay.transform.InferType()(mod)
var_9077 = relay.var("var_9077", dtype = "uint16", shape = (150, 14))#candidate|9077|(150, 14)|var|uint16
output = func_9076(var_9077)
func_9078 = relay.Function([var_9077], output)
mutated_mod['func_9078'] = func_9078
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9092 = relay.var("var_9092", dtype = "float64", shape = (7, 11, 1))#candidate|9092|(7, 11, 1)|var|float64
uop_9093 = relay.erf(var_9092.astype('float64')) # shape=(7, 11, 1)
bop_9097 = relay.logical_xor(var_9092.astype('uint32'), relay.reshape(uop_9093.astype('uint32'), relay.shape_of(var_9092))) # shape=(7, 11, 1)
func_2366_call = mod.get_global_var('func_2366')
func_2371_call = mutated_mod.get_global_var('func_2371')
var_9101 = relay.var("var_9101", dtype = "int16", shape = (1, 26))#candidate|9101|(1, 26)|var|int16
var_9102 = relay.var("var_9102", dtype = "float64", shape = (1, 135))#candidate|9102|(1, 135)|var|float64
var_9103 = relay.var("var_9103", dtype = "float32", shape = (210,))#candidate|9103|(210,)|var|float32
const_9104 = relay.const([[4.215604],[3.256033],[-9.953144],[0.292582],[7.378309],[5.112310],[-2.862342],[-4.849344],[2.621998],[7.171717],[-1.259133],[9.749014],[-2.517669],[-8.567283],[-5.089175],[5.767520],[1.555606],[-4.496766],[-2.786134],[1.113160],[3.078841],[3.049662],[2.435016],[-0.304296],[-5.662437],[6.758231],[2.712369],[-9.517808],[-8.353705],[-5.341892],[7.271163],[-5.696777],[0.128481],[-2.528573],[-7.631350],[6.862148],[-4.073754],[-9.366340],[-5.636353],[-6.110763],[-7.666462],[8.673745],[-9.215264],[3.197096],[-5.133232],[3.501560],[-8.002778],[-1.151327],[-0.379078],[4.394612],[-4.912390],[-4.216911],[4.358857],[-4.224333],[-8.094520],[-2.208428],[6.700897],[-4.581844],[4.877202],[-9.121079],[-6.443373],[6.285371],[9.548511],[-0.098867],[-8.832043],[-0.689186],[-4.957313],[3.246280],[6.666778],[4.834936],[1.721611],[4.845380],[2.473933],[-2.557489],[4.495888],[-4.786214],[0.948878],[-2.107299],[4.904241],[-9.992014],[-5.210157],[3.046822],[-3.314303],[-7.605275],[-1.207362],[7.022523],[-9.243163],[-0.989810],[-2.245611],[-2.979270],[9.693998],[8.948899],[4.725360],[0.739141],[-8.101313],[-7.268156],[9.676749],[2.844329],[9.883488],[6.090180],[9.834098],[7.420099],[8.341105],[7.580496],[-2.900639],[-4.310452],[-0.727455],[-1.744740],[2.797756],[0.403190],[-0.025155],[3.201577],[4.966220],[7.837620],[-0.357534],[-2.769839],[1.781866],[9.660421],[-6.983482],[-3.886572],[9.322517],[-2.406402],[0.327389],[9.199653],[9.471209],[-3.638015],[-2.282469],[9.805301],[6.034233],[-3.016753],[3.483555],[6.007649],[-0.837290],[-7.251725],[-1.914485],[-4.962700],[1.523698],[8.385094],[1.503307],[5.410557],[8.555998],[-3.667286],[9.080275],[2.019603],[-4.333577],[7.467506],[6.056558],[-0.408143],[0.319397],[-0.912187],[-1.179146],[2.302622],[4.106875],[-5.341673],[0.997397],[5.094382],[2.445298],[5.758998],[2.165927],[1.128012],[-1.213832],[-8.288169],[-2.134052],[-7.062682],[1.011758],[8.661447],[4.120764],[4.770671],[8.565705],[4.916182],[6.900859],[-6.908023],[9.665093],[-3.253736],[-1.211729],[-5.654386],[-4.537890],[-6.175473],[-7.414213],[-1.458857],[0.023633],[8.191961],[9.099067],[-9.273540],[-9.966952],[1.365071],[-5.440699],[-0.620434],[8.481634],[7.231543],[5.902938],[9.784894],[-5.278937],[-9.270263],[-4.489131],[-6.929623],[-6.005500],[-1.236050],[-2.093907],[-8.640384],[-0.250212],[-3.453128],[7.299658],[-5.696857],[1.963829],[0.435493],[-0.354585],[-1.755832],[-1.417428],[0.651495],[-0.901962],[1.167687],[3.260704],[-0.312348],[-9.971696],[-8.370098],[-6.636007],[6.668298],[9.083183],[6.450026],[0.495783],[4.955162],[3.942123],[-8.483648],[-6.994971],[-6.163226],[3.269065],[4.085234],[6.592827],[-7.072449],[5.164246],[-7.990604],[-9.321311],[4.788473],[-9.002688],[-9.752956],[4.093836],[2.574199],[-0.950160],[9.846215],[1.847086],[4.598936],[0.144852],[3.931363],[-0.999124],[-5.047773],[-5.667270],[3.884628],[-6.711014],[-2.403028],[5.744518],[7.063770],[2.154856],[9.015711],[-3.851069],[-4.314815],[-0.259016],[4.700147],[9.478051],[-9.147621],[-6.278317],[3.447081],[-4.506252],[7.139780],[1.568842],[8.901463],[6.491870],[-2.858077],[6.381894],[-8.626228],[-0.021576],[7.253918],[-7.345507],[-2.917553],[7.556368],[5.685549],[8.710362],[-8.730915],[9.795330],[-0.883114],[0.770980],[-9.567338],[-6.167954],[6.075117],[-9.321752],[-5.177519],[2.461967],[-3.066144],[-1.098082],[5.508915],[0.815641],[3.367224],[5.620629],[-4.684199],[-8.240000],[3.904749],[-5.032767],[-7.213643],[-7.851827],[-2.891843],[1.324303],[4.571287],[-4.189951],[-2.901568],[-1.233880],[-8.268278],[-9.955972],[-7.133950],[8.256339],[-0.531564],[-5.499815],[-0.971989],[5.732805],[9.958780],[-0.046279],[1.838777],[-0.537632],[-7.245535],[-9.433821],[9.056979],[-9.019142],[-6.085908],[-1.346789],[-4.529417],[-3.952457],[8.316234],[8.331747],[1.852902],[-4.865759],[-8.515185],[9.217856],[-1.578001],[8.129751],[-8.556311],[9.592873],[-4.498669],[-2.600340],[-9.579390],[-9.272155],[-5.251957],[7.242495],[6.222438],[7.532225],[-7.316901],[7.517256],[9.988259],[-0.644633],[3.067454],[-6.536658],[9.598645],[7.164713],[-9.037451],[-3.678286],[-9.633227],[3.704113],[5.897263],[-4.202886],[9.931585],[-2.557715],[0.116393],[6.679768],[-9.360939],[-3.523181],[8.834000],[6.709975],[-4.495260],[-5.284908],[-8.813110],[2.410194],[8.930233],[-2.425326],[-1.682519],[5.421678],[-4.371871],[5.221373],[-0.222061],[-0.001554],[-3.394543],[-9.985454],[-6.639018],[-4.133807],[-6.833297],[4.310776],[0.135431],[-9.443435],[1.813145],[-4.584630],[0.821180],[-9.502227],[3.445401],[-3.211352],[-4.039075],[-9.495890],[3.309749],[-4.079653],[-7.612776],[9.476311],[6.502532],[-4.599519],[5.611060],[-4.684731],[9.591316],[-9.439001],[-7.429731],[-8.682749],[-8.159805],[7.255008],[-2.583770],[7.654484],[-4.324648],[6.768870],[-3.078966],[-5.469078],[4.475006],[8.004945],[1.434487],[9.875847],[-9.038355],[3.058884],[-7.750028],[-1.084885],[-8.005769],[4.539865],[5.902812],[6.688567],[-4.174581],[-5.937118],[9.281798],[8.160008],[3.895124],[9.556066],[-3.080191],[8.827831],[4.017423],[4.293668],[5.361933],[-8.221284],[-7.873991],[-7.748934],[8.121091],[8.483072],[-9.281894],[-7.243878],[-5.977948],[-5.754578],[-0.007232],[-3.578977],[-8.418517],[5.251318],[9.456873],[-8.504355],[-5.985435],[-9.370276],[-9.567332],[-6.739881],[-8.536301],[-7.751820],[-5.528986],[-1.798139],[-1.926802],[-7.146630],[0.781900],[0.225378],[5.591006],[0.015638],[9.062979],[9.527375],[-3.280379],[-7.973042],[-4.402933],[-2.410471],[1.677195],[0.360874],[-9.322271],[-1.447196],[-0.514731],[7.757314],[-6.804101],[4.797979],[-0.074079],[-8.253436],[-5.534931],[7.173017],[8.473712],[-3.289253],[0.240894],[1.746015],[9.863039],[-6.735812],[-8.896408],[-3.680323],[9.486278],[-5.642651],[-8.277341],[4.380994],[-5.776480],[-7.514630],[0.047655],[-0.851750],[-9.367862],[-6.579133],[8.810267],[-6.966831],[-9.533780],[-1.967285],[3.056975],[4.920084],[5.637516],[-0.001865],[-4.993349],[-9.027447],[7.196214],[4.443569],[-6.020098],[-6.016571],[-7.242984],[-9.428374],[-1.021099],[-4.254694],[2.627341],[8.396984],[2.614725],[-4.088284],[8.128735],[-5.644432],[-9.756787],[-2.867305],[-1.617953],[6.372715],[9.480415],[9.279252],[-9.883297],[-8.458771],[-2.938257],[-4.465137],[0.103370],[-3.559023],[-9.570401],[2.152578],[-0.221441],[6.763981],[-1.130104],[-7.914726],[-5.928449],[-2.860846],[1.985941],[0.919662],[3.562734],[-9.126525],[7.834777],[-1.821964],[7.920060],[5.132497],[9.205577],[6.666566],[3.414510],[-0.707023],[-8.000972],[-2.457427],[-3.216961],[0.819083],[-7.444563],[-8.535692],[-8.853204],[9.880202],[6.057841],[-6.521766],[-7.326824],[-4.677386],[7.451158],[0.138193],[3.019071],[-3.318708],[4.461918],[-0.982716],[3.871921],[6.494689],[-4.419319],[-2.692838],[4.259455],[-2.988257],[8.929806],[1.910307],[9.263516],[8.975900],[6.876589],[3.661202],[-3.618928],[-5.601088],[-6.107411],[-3.979900],[-5.880323],[4.138506],[5.373636],[0.068035],[8.118427],[4.594395],[1.720856],[-4.401456],[-5.905011],[8.285816],[2.726346],[-6.547786],[-6.688333],[0.603765],[2.558543],[3.032707],[9.181444],[8.591072],[-9.395064],[1.779780],[-6.466251],[-4.142641],[1.900667],[-0.450659],[-5.777624],[2.368033],[-0.992916],[8.562261],[5.884189],[3.886850],[-5.391748],[-7.294236],[6.185343],[-7.075056],[5.453803],[2.688922],[-4.041546],[5.144866],[3.509486]], dtype = "float32")#candidate|9104|(630, 1)|const|float32
call_9100 = relay.TupleGetItem(func_2366_call(relay.reshape(var_9101.astype('int16'), [2, 13, 1]), relay.reshape(var_9102.astype('float64'), [135,]), relay.reshape(var_9103.astype('float32'), [105, 2]), relay.reshape(const_9104.astype('float32'), [630,]), ), 3)
call_9105 = relay.TupleGetItem(func_2371_call(relay.reshape(var_9101.astype('int16'), [2, 13, 1]), relay.reshape(var_9102.astype('float64'), [135,]), relay.reshape(var_9103.astype('float32'), [105, 2]), relay.reshape(const_9104.astype('float32'), [630,]), ), 3)
func_151_call = mod.get_global_var('func_151')
func_154_call = mutated_mod.get_global_var('func_154')
const_9108 = relay.const([False,True,False,True,True,False,False,False,True,True,False,False,False,True,False,False,True,True,True,True,True,False,True,True,True,True,True,False,False,True,True,True,False,True,False,False,True,True,False,True,False,False,True,False,True,True,False,True,False,False,False,True,False,False,False,True,True,True,True,True,True,False,False,True,False,True,True,True,False,True,False,False,True,True,False,True,True,True,False,True,True,False,True,True,False,True,True,True,True,False,True,False,True,True,True,True,False,True,False,False,False,True,False,False,False,True,True,True,False,True,True,True,True,False,False,False,True,True,True,False,False,False,False,True,False,False,False,False,True,False,True,True,True,True,True,False,False,False,True,False,True,False,True,True,False,False,True,False,True,False,False,True,True,True,False,True,True,False,True,False,True,False,True,False,False,True,False,False,True,False,True,True,False,False,False,True,False,True,True,False,True,True,True,False,False,False,True,True,False,True,True,True,True,True,False,True,False,False,False,True,False,True,False,True,True,False,False,False,True,True,False,True,False,True,True,True,True,True,False,False,False,False,True,True,True,True,True,True,False,True,False,False,False,True,True,True,True,True,True,True,False,True,False,True,True,True,False,False,False,False,False,False,False,False,False,True,True,True,False,True,False,True,False,False,False,True,True,True,True,True,False,True,False,False,False,True,False,False,False,False,True,False,True,True,False,True,True,False,False,True,True,False,False,True,False,False,True,True,False,False,False,False,True,True,True,False,False,True,False,False,True,True,True,False,True,True,True,False,True,True,True,True,True,False,False,True,False,True,True,False,True,True,True,True,False,False,True,True,True,True,True,False,True,False,True,False,False,False,False,True,False,True,False,True,True,True,True,False,False,False,False,False,True,True,True,False,True,False,True,False,True,False,True,False,True,False,False,True,False,False,False,False,False,True,False,True,False,True,True,False,True,False,False,False,True,True,False,True,True,True,True,True,False,False,True,True,False,False,False,True,False,False,True,False,True,True,False,True,False,True,False,True,True,False,False,True,False,False,False,True,False,True,False,False,False,False,True,False,False,True,True,False,True,True,True,True,False,True,False,True,False,False,False,False,True,False,True,True,True,True,False,True,False,True,True,False,True,False,True,True,True,False,True,False,True,False,True,False,True,False,True,False,False,True,False,True,False,True,False,True,False,True,False,False,False,True,True,True,True,False,False,False,False,True,False,False,False,False,False,True,False,True,True,False,False,True,False,False,False,False,True,False,True,True,True,True,False,False,False,True,False,False,True,False,False,False,False,False,False,False,True,False,True,True,False,False,False,False,False,True,True,False,True,False,True,False,False,False,False,False,True,False,True,True,True,True,True,True,True,True,False,False,True,True,True,True,True,False,False,False,True,True,False,False,True,True,True,True,True,True,False,True,False,True,False,True,False,True,False,True,False,False,True,True,False,True,False,True,True,False,True,False,True,True,False,True,True,True,False,False,True,False,True,True,True,True,False,True,False,False,False,False,True,False,True,True,True,False,False,False,False,False,False,False,True,False,True,False,False,True,True,True,False,False,False,True,False,False,True,False,False,True,True,True,True,False,False,False,False,True,False,True,True,False,True,False,True,False,True,True,True,False,False,True,False,False,True,False,False,False,True,False,True,False,False,True,False,False,True,True,True,False,False,False,False,True,True,True,True,False,False,False,False,False,False,False,False,True,True,False,True,False,True,False,False,True,True,False,True,True,True,True,True,True,True,True,False,False,True,True,False,True,False,False,False,False,True,False,True,False,True,False,False,False,False,False,True,False,False,False,True,False,True,False,True,True,True,False,True,False,True,False,False,True,False,False,True,True,False,False,True,True,False,True,True,True,True,False,True,False,True,False,False,False,False,True,True,True,True,True,False,True,True,False,False,True,False,False,True,False,False,False,False,True,False,True,False,True,False,True,True,True,True,True,True,True,True,True,False,False,False,False,True,True,False,False,False,False,False,True,True,False,False,True,True,False,False,True,True,False,False,True,True,True,False,True,False,True,False,True,False,False,True,True,True,False,True,True,False,True,True,True,False,True,False,True,True,True,True,False,True,True,True,True,True,False,False,True,True,False,False,True,False,False,True,True], dtype = "bool")#candidate|9108|(896,)|const|bool
call_9107 = relay.TupleGetItem(func_151_call(relay.reshape(const_9108.astype('bool'), [16, 7, 8])), 1)
call_9109 = relay.TupleGetItem(func_154_call(relay.reshape(const_9108.astype('bool'), [16, 7, 8])), 1)
output = relay.Tuple([bop_9097,call_9100,var_9101,var_9102,var_9103,const_9104,call_9107,const_9108,])
output2 = relay.Tuple([bop_9097,call_9105,var_9101,var_9102,var_9103,const_9104,call_9109,const_9108,])
func_9116 = relay.Function([var_9092,var_9101,var_9102,var_9103,], output)
mod['func_9116'] = func_9116
mod = relay.transform.InferType()(mod)
mutated_mod['func_9116'] = func_9116
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9116_call = mutated_mod.get_global_var('func_9116')
var_9118 = relay.var("var_9118", dtype = "float64", shape = (7, 11, 1))#candidate|9118|(7, 11, 1)|var|float64
var_9119 = relay.var("var_9119", dtype = "int16", shape = (1, 26))#candidate|9119|(1, 26)|var|int16
var_9120 = relay.var("var_9120", dtype = "float64", shape = (1, 135))#candidate|9120|(1, 135)|var|float64
var_9121 = relay.var("var_9121", dtype = "float32", shape = (210,))#candidate|9121|(210,)|var|float32
call_9117 = func_9116_call(var_9118,var_9119,var_9120,var_9121,)
output = call_9117
func_9122 = relay.Function([var_9118,var_9119,var_9120,var_9121,], output)
mutated_mod['func_9122'] = func_9122
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9133 = relay.var("var_9133", dtype = "float32", shape = (10, 15, 13))#candidate|9133|(10, 15, 13)|var|float32
uop_9134 = relay.log(var_9133.astype('float32')) # shape=(10, 15, 13)
output = relay.Tuple([uop_9134,])
output2 = relay.Tuple([uop_9134,])
func_9137 = relay.Function([var_9133,], output)
mod['func_9137'] = func_9137
mod = relay.transform.InferType()(mod)
var_9138 = relay.var("var_9138", dtype = "float32", shape = (10, 15, 13))#candidate|9138|(10, 15, 13)|var|float32
output = func_9137(var_9138)
func_9139 = relay.Function([var_9138], output)
mutated_mod['func_9139'] = func_9139
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9186 = relay.var("var_9186", dtype = "float32", shape = (16, 2, 12))#candidate|9186|(16, 2, 12)|var|float32
uop_9187 = relay.erf(var_9186.astype('float32')) # shape=(16, 2, 12)
uop_9189 = relay.rsqrt(uop_9187.astype('float32')) # shape=(16, 2, 12)
func_8205_call = mod.get_global_var('func_8205')
func_8207_call = mutated_mod.get_global_var('func_8207')
call_9205 = relay.TupleGetItem(func_8205_call(), 1)
call_9206 = relay.TupleGetItem(func_8207_call(), 1)
uop_9211 = relay.sigmoid(uop_9189.astype('float32')) # shape=(16, 2, 12)
func_6827_call = mod.get_global_var('func_6827')
func_6830_call = mutated_mod.get_global_var('func_6830')
var_9221 = relay.var("var_9221", dtype = "uint32", shape = ())#candidate|9221|()|var|uint32
var_9222 = relay.var("var_9222", dtype = "uint16", shape = (2100,))#candidate|9222|(2100,)|var|uint16
call_9220 = relay.TupleGetItem(func_6827_call(relay.reshape(var_9221.astype('uint32'), []), relay.reshape(var_9222.astype('uint16'), [30, 70]), ), 0)
call_9223 = relay.TupleGetItem(func_6830_call(relay.reshape(var_9221.astype('uint32'), []), relay.reshape(var_9222.astype('uint16'), [30, 70]), ), 0)
output = relay.Tuple([call_9205,uop_9211,call_9220,var_9221,var_9222,])
output2 = relay.Tuple([call_9206,uop_9211,call_9223,var_9221,var_9222,])
func_9230 = relay.Function([var_9186,var_9221,var_9222,], output)
mod['func_9230'] = func_9230
mod = relay.transform.InferType()(mod)
var_9231 = relay.var("var_9231", dtype = "float32", shape = (16, 2, 12))#candidate|9231|(16, 2, 12)|var|float32
var_9232 = relay.var("var_9232", dtype = "uint32", shape = ())#candidate|9232|()|var|uint32
var_9233 = relay.var("var_9233", dtype = "uint16", shape = (2100,))#candidate|9233|(2100,)|var|uint16
output = func_9230(var_9231,var_9232,var_9233,)
func_9234 = relay.Function([var_9231,var_9232,var_9233,], output)
mutated_mod['func_9234'] = func_9234
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8327_call = mod.get_global_var('func_8327')
func_8329_call = mutated_mod.get_global_var('func_8329')
call_9306 = relay.TupleGetItem(func_8327_call(), 1)
call_9307 = relay.TupleGetItem(func_8329_call(), 1)
func_7615_call = mod.get_global_var('func_7615')
func_7617_call = mutated_mod.get_global_var('func_7617')
const_9318 = relay.const([[-8.346988,-0.549165,-7.135597,-7.355541,5.830414,-0.090496,-0.673519,-6.489985,7.135141,0.683043,6.562438,9.591582,-4.313041,8.340589,2.918066,-3.120031,6.528929,-3.177453],[-0.249916,-2.136247,5.300172,5.981197,7.359438,5.000908,4.290286,-7.042614,-1.100529,-9.225248,-0.239127,9.180270,3.951018,4.614762,8.200724,-7.769631,-9.548215,3.011239],[8.395445,3.300623,-9.328756,6.299137,3.172786,-3.599671,0.861384,-3.808024,-6.320495,8.782177,9.313655,-2.893622,-0.363547,4.983219,3.673064,1.012003,5.359997,1.413870],[4.673337,1.666072,-9.102681,-8.982891,-7.422220,8.049622,-6.016427,5.961338,8.317672,-2.139206,-3.970808,-2.036977,-5.195459,0.578497,-5.259958,5.452523,3.734616,-3.700110],[-9.867808,-3.715356,7.930183,6.363462,-8.558421,-9.229617,6.523534,-2.158656,-8.431037,3.207797,-7.405955,-5.633426,-5.876308,-0.684592,0.948485,8.168713,3.223891,-7.322638],[-1.688767,-1.025801,-8.782596,-9.941468,-9.498108,-0.132154,-3.881214,1.338487,-5.657731,2.459456,-9.499318,-9.573143,0.149588,8.758025,0.184427,6.351692,-9.451138,4.714316],[-5.655166,-6.413449,-1.153656,5.914746,-3.867199,3.062318,2.367100,9.756334,-5.666282,7.125036,-8.759013,-6.337554,-9.882269,6.703584,8.767801,-9.353634,-9.195455,-1.524169],[8.940895,3.241324,1.821512,-7.467373,-2.304360,-8.129569,4.776253,-7.452491,-5.566509,-2.091346,-2.870858,1.327151,-6.438627,-8.977168,-0.046791,3.266325,-3.786692,-2.058655],[0.765330,-2.434455,-8.636410,-4.286409,-1.492991,4.968369,9.088811,-3.559323,6.501349,9.856713,7.499436,7.898980,8.277444,1.771013,7.649405,7.743176,-0.273102,-7.035062],[-9.909040,-7.320004,1.311139,2.401944,2.212162,3.454838,-5.185847,-3.414251,-1.322908,1.463035,-5.708423,6.370160,-3.355415,-7.958441,2.130762,-2.546660,7.876447,-6.006349],[-6.817525,2.582980,7.884670,3.893994,-9.808769,0.922952,2.069833,-4.741038,4.042118,9.481133,-7.202625,-8.470663,9.336657,8.926179,-4.888024,1.583145,3.834325,-9.640334],[6.692161,-2.414717,-8.852875,-5.330460,7.299923,9.108031,4.367710,-8.248514,6.014961,4.585744,7.945117,4.227827,-9.534401,8.468459,-0.896022,6.770747,8.626692,2.750318]], dtype = "float64")#candidate|9318|(12, 18)|const|float64
call_9317 = func_7615_call(relay.reshape(const_9318.astype('float64'), [2, 9, 12]))
call_9319 = func_7615_call(relay.reshape(const_9318.astype('float64'), [2, 9, 12]))
output = relay.Tuple([call_9306,call_9317,const_9318,])
output2 = relay.Tuple([call_9307,call_9319,const_9318,])
func_9320 = relay.Function([], output)
mod['func_9320'] = func_9320
mod = relay.transform.InferType()(mod)
mutated_mod['func_9320'] = func_9320
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9320_call = mutated_mod.get_global_var('func_9320')
call_9321 = func_9320_call()
output = call_9321
func_9322 = relay.Function([], output)
mutated_mod['func_9322'] = func_9322
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9383 = relay.var("var_9383", dtype = "int64", shape = (1, 9, 2))#candidate|9383|(1, 9, 2)|var|int64
var_9384 = relay.var("var_9384", dtype = "int64", shape = (10, 9, 2))#candidate|9384|(10, 9, 2)|var|int64
bop_9385 = relay.multiply(var_9383.astype('int64'), var_9384.astype('int64')) # shape=(10, 9, 2)
output = bop_9385
output2 = bop_9385
func_9395 = relay.Function([var_9383,var_9384,], output)
mod['func_9395'] = func_9395
mod = relay.transform.InferType()(mod)
mutated_mod['func_9395'] = func_9395
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9395_call = mutated_mod.get_global_var('func_9395')
var_9397 = relay.var("var_9397", dtype = "int64", shape = (1, 9, 2))#candidate|9397|(1, 9, 2)|var|int64
var_9398 = relay.var("var_9398", dtype = "int64", shape = (10, 9, 2))#candidate|9398|(10, 9, 2)|var|int64
call_9396 = func_9395_call(var_9397,var_9398,)
output = call_9396
func_9399 = relay.Function([var_9397,var_9398,], output)
mutated_mod['func_9399'] = func_9399
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8171_call = mod.get_global_var('func_8171')
func_8173_call = mutated_mod.get_global_var('func_8173')
call_9420 = relay.TupleGetItem(func_8171_call(), 0)
call_9421 = relay.TupleGetItem(func_8173_call(), 0)
func_5249_call = mod.get_global_var('func_5249')
func_5251_call = mutated_mod.get_global_var('func_5251')
call_9433 = func_5249_call()
call_9434 = func_5249_call()
output = relay.Tuple([call_9420,call_9433,])
output2 = relay.Tuple([call_9421,call_9434,])
func_9438 = relay.Function([], output)
mod['func_9438'] = func_9438
mod = relay.transform.InferType()(mod)
output = func_9438()
func_9439 = relay.Function([], output)
mutated_mod['func_9439'] = func_9439
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6775_call = mod.get_global_var('func_6775')
func_6777_call = mutated_mod.get_global_var('func_6777')
call_9467 = relay.TupleGetItem(func_6775_call(), 0)
call_9468 = relay.TupleGetItem(func_6777_call(), 0)
func_6490_call = mod.get_global_var('func_6490')
func_6491_call = mutated_mod.get_global_var('func_6491')
call_9473 = func_6490_call()
call_9474 = func_6490_call()
output = relay.Tuple([call_9467,call_9473,])
output2 = relay.Tuple([call_9468,call_9474,])
func_9477 = relay.Function([], output)
mod['func_9477'] = func_9477
mod = relay.transform.InferType()(mod)
output = func_9477()
func_9478 = relay.Function([], output)
mutated_mod['func_9478'] = func_9478
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6173_call = mod.get_global_var('func_6173')
func_6175_call = mutated_mod.get_global_var('func_6175')
call_9482 = func_6173_call()
call_9483 = func_6173_call()
func_7309_call = mod.get_global_var('func_7309')
func_7311_call = mutated_mod.get_global_var('func_7311')
call_9505 = relay.TupleGetItem(func_7309_call(), 0)
call_9506 = relay.TupleGetItem(func_7311_call(), 0)
output = relay.Tuple([call_9482,call_9505,])
output2 = relay.Tuple([call_9483,call_9506,])
func_9513 = relay.Function([], output)
mod['func_9513'] = func_9513
mod = relay.transform.InferType()(mod)
mutated_mod['func_9513'] = func_9513
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9513_call = mutated_mod.get_global_var('func_9513')
call_9514 = func_9513_call()
output = call_9514
func_9515 = relay.Function([], output)
mutated_mod['func_9515'] = func_9515
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7563_call = mod.get_global_var('func_7563')
func_7564_call = mutated_mod.get_global_var('func_7564')
call_9529 = relay.TupleGetItem(func_7563_call(), 0)
call_9530 = relay.TupleGetItem(func_7564_call(), 0)
func_1652_call = mod.get_global_var('func_1652')
func_1655_call = mutated_mod.get_global_var('func_1655')
const_9533 = relay.const([[-2.025209,-4.106619,-3.689538,1.992111,5.318133,7.788945],[0.613043,2.207042,8.784312,-4.499316,-6.816933,1.784742],[-0.341719,-1.005708,-6.738076,5.272616,8.576285,1.284678],[-5.455808,3.965129,-3.985946,-3.136925,2.532456,4.995369],[-9.869330,-4.239532,-7.157851,-4.923582,5.292933,9.324919],[3.665348,-2.165157,-1.299286,-0.275571,-7.324727,-5.369428],[-6.804324,-8.163559,-5.599561,-1.917819,-3.664495,9.203322],[-2.204886,6.660528,-3.183786,6.321140,3.038935,2.635873],[-1.159256,-4.104994,5.299273,6.272495,-0.883046,-3.557970],[5.299374,7.023363,3.435094,-1.556233,-1.542641,8.638122],[-4.298081,-3.372130,2.030692,4.302790,2.568547,-9.269347],[-6.520583,-2.742792,-6.852524,5.065815,8.353306,0.546108],[6.459335,4.725441,1.660724,-1.069020,7.041909,4.876096],[-8.926988,-9.815612,-0.272415,6.442366,-3.043145,8.711516],[-6.986386,-8.227155,1.257933,-9.154581,4.507466,9.401728],[6.568777,-8.057347,-0.717599,2.693294,-8.780332,3.438916],[-5.065816,7.795667,-0.609501,3.597168,8.897703,0.364223],[9.617638,2.813353,9.085056,1.370056,6.699860,4.255148],[2.068822,-1.695734,7.464565,8.413836,-9.763867,-5.510241],[2.073666,7.866524,-0.609652,-8.575709,2.966543,-7.184651],[-5.195604,6.520378,-8.668876,6.706694,8.451271,9.311895],[4.532323,-9.340484,-0.438642,5.181089,5.297838,-3.949484],[3.485214,7.207115,3.207070,1.091867,-4.083672,0.421361],[8.854276,-4.008727,-4.344261,3.547009,-8.748385,-3.195854],[0.058821,3.031194,-8.248865,-1.059226,-5.248975,-3.140376],[4.077031,6.127178,-9.514345,-2.640591,4.326454,-3.045457],[8.736271,-1.698843,-9.067680,-4.375599,-0.462688,-4.215305],[3.245701,-5.782948,-7.010259,4.260089,-6.648716,7.145192],[5.433934,-3.236723,2.017388,2.438407,9.777756,-1.179386],[-7.430141,9.919517,-3.593006,7.392922,-5.183206,0.243640],[8.589679,-6.936064,2.006517,-6.192649,-8.735982,-8.795194],[-9.611036,-9.671489,8.188899,7.462109,3.503110,-6.950284],[-5.337959,4.226379,3.147216,2.785454,-3.464763,-1.886033],[-3.562094,-0.734807,1.568718,-7.006028,-4.274083,5.902280],[6.814574,3.464506,2.357726,5.797617,-1.347410,-6.172865]], dtype = "float32")#candidate|9533|(35, 6)|const|float32
const_9534 = relay.const([[-2.755413],[1.558862],[3.620354],[1.215154],[-9.330747],[-4.545227],[0.143315],[-7.577802],[-0.873293],[-2.713217],[9.453016],[-0.144670],[-1.473286],[-7.526819],[7.085000],[1.826351],[1.800612],[2.231668],[6.272663],[-2.561578],[-1.971782],[-6.636515],[-6.002422],[1.118308],[-4.520862],[-0.365259],[-6.943756],[-3.493995],[1.419732],[2.589085],[3.501538],[-3.723749],[2.897089],[7.688815],[-1.099341],[4.513768],[-0.220055],[-3.274208],[-3.718615],[0.241176],[9.290525],[3.291348],[-8.619341],[-9.714527],[-1.036983],[0.306209],[-2.813493],[-0.402560],[1.597970],[-2.351803],[8.751962],[-5.055949],[1.279625],[-1.277574],[-1.375138],[1.749309],[-2.080065],[2.037576],[-4.605217],[-8.444266],[1.213839],[-7.477811],[4.520887],[-9.602047],[-0.406534],[-5.881381],[-6.238686],[4.968305],[1.710912],[5.339452],[3.474515],[3.752084],[8.344120],[-5.942817],[-3.295748],[-2.410006],[-3.047669],[0.523500],[6.297451],[-2.345340],[-0.597444],[6.816787],[-5.446841],[8.399146],[6.365947],[1.407362],[9.480336],[-9.271794],[-5.918877],[-0.024425],[1.187442],[-9.387555],[6.027182],[1.151227],[7.472087],[-8.098841],[-7.144021],[-7.660192],[-5.991467],[-7.803934],[2.952333],[-5.816550],[-8.334434],[0.762279],[9.741045],[4.753383],[0.746762],[5.439085],[4.701156],[2.634517],[-3.148667],[-9.017844],[-6.757896],[7.726887],[-8.642902],[-5.763759],[-9.190619],[-1.810779],[4.269709],[9.192311],[7.091847],[7.241606],[-7.912600],[2.496966],[9.764744],[4.074765],[-4.527008],[-5.620107],[-1.035440],[8.799951],[7.275462],[-6.604183],[-7.263167],[-3.103401],[6.915441],[4.399323],[-2.899203],[4.840228],[7.315639],[-1.386201],[3.564129],[-0.973607],[7.049265],[-5.954231],[7.004723],[1.010033],[0.367773],[-2.864512],[-6.606823],[1.414034],[-4.897730],[0.383957],[0.920626],[6.035664],[5.900827],[4.059394],[5.605724],[5.940646],[-3.539060],[7.065360],[4.965660],[-2.009078],[-7.953973],[3.498353],[8.162219],[-7.992969],[7.686601],[-6.161248],[-2.066503],[9.037062],[4.763700],[0.406512],[-6.653065],[-0.232946],[-7.706229],[-6.825986],[-4.125969],[2.201170],[3.556858],[3.184046],[4.698427],[-4.463168],[9.667980],[-3.468267],[3.649279],[-1.855502],[-5.495431],[5.213762],[-3.506384],[-3.153930],[6.093837],[-2.761856],[2.738536],[4.690830],[-0.767227],[-9.128186],[-4.377449],[-6.389772],[5.842699],[-9.346986],[-2.218005],[-5.445120],[-2.623720],[-0.301080],[2.306752],[7.982737],[7.260028],[-2.265581],[6.012106],[-0.962390],[-4.705905],[-8.080826],[6.843569],[3.421630],[2.332170],[6.770471],[-3.226912],[-8.105811],[-0.709663],[2.510163],[9.246569],[-5.864353],[-3.327964],[-6.090318],[-2.730336],[-6.660753],[1.378464],[-3.895038],[7.020844],[2.651809],[8.872941],[8.334683],[-7.458984],[-7.379419],[-5.469964],[-3.308393],[-8.272434],[-0.699690],[5.664675],[8.572049],[1.539088],[1.772960],[-8.324719],[-3.694072],[7.954667],[-6.169837],[-6.293695],[-6.235271],[9.727118],[7.052134],[-9.029400],[-0.935038],[4.949797],[8.208219],[8.281922],[-1.754456],[-4.578904],[3.356026],[2.170810],[2.006362],[6.823247],[6.453841],[1.127032],[5.585658],[-6.256837],[-4.765907],[-5.294189],[-4.018390],[1.700128],[1.795335],[-7.627914],[-2.495421],[0.731859],[1.792182],[0.152360],[0.106662],[-0.171894],[-8.509096],[-9.553982],[-6.672175],[4.993746],[6.916152],[2.715606],[8.380264],[0.778887],[1.110347],[-7.625932],[8.491662],[3.867284],[2.400621],[0.159094],[-9.673737],[1.528874],[3.403184],[-2.267019],[8.040256],[-7.545574],[0.430696],[-3.549871],[-0.272576],[0.170003],[3.005372],[3.975464],[4.195777],[0.014755],[6.748259],[5.197297],[-3.077396],[9.781501],[-9.901350],[9.001268],[1.332036],[-8.385990],[-4.260555],[7.087911],[1.255218],[-3.470829],[-4.218119],[1.540341],[9.954031],[-9.189059],[8.828652],[-3.092498],[5.926582],[0.714620],[9.476878],[5.087336],[-5.536167],[1.348828],[-8.014792],[8.663662],[-3.699226],[-4.469818],[-1.273281],[-8.119600],[-2.734401],[-6.076311],[5.575039],[6.079315],[-8.505582],[-0.776810],[8.724869],[-8.803340],[-8.318469],[-6.355768],[-7.782732],[-3.012893],[-0.830315],[-0.033080],[-3.521248],[-3.654409],[0.056867],[-8.881827],[8.064011],[2.130766],[-6.078738],[5.724317],[7.924842],[7.945435],[5.226192],[-9.282867],[6.339495],[-8.175126],[7.457126],[-7.554227],[-8.163018],[-4.894761],[-5.441363],[-3.552234],[-3.688387],[7.283105],[6.913905],[4.504067],[9.733674],[-4.180575],[-9.066333],[-5.335597],[8.326501],[3.794308],[4.172776],[-0.599958],[-8.393805],[-0.833082],[6.004116],[-0.529486],[-2.493285],[-2.807410],[-9.671036],[6.726957],[-9.796904],[8.738805],[-5.985965],[2.423541],[-9.035437],[7.916582],[-2.468569],[7.149269],[-0.432206],[2.849003],[-3.284833],[-1.016315],[-4.373298],[1.690912],[-2.722151],[-5.703269],[-1.562959],[4.122466],[2.146632],[0.325005],[-8.848835],[-0.560628],[-6.071511],[2.786136],[7.878441],[7.958869],[1.403909],[-6.373779],[-0.365768],[-2.602769],[-8.880161],[-1.795970],[-6.580450],[-0.529204],[-1.764377],[-3.857673],[-8.437903],[5.980385],[-6.101362],[6.530213],[-7.181573],[-5.429126],[-7.185566],[4.608489],[-0.058996],[3.110965],[-8.176446],[7.623346],[-1.116225],[-6.816673],[3.021531],[9.685646],[0.821818],[4.927543],[6.289719],[9.783701],[4.836844],[0.033448],[8.216366],[-0.939018],[1.467620],[-0.171284],[3.093972],[-6.086200],[2.809007],[-2.287592],[8.974495],[-8.362248],[3.946913],[9.273829],[4.018855],[-9.898159],[-5.866070],[-1.559173],[-9.132164],[8.209280],[1.114015],[0.077815],[4.936869],[-2.410173],[-3.144385],[-1.889609],[-4.758487],[4.449308],[-3.088771],[-1.696553],[0.997163],[-5.930702],[6.012274],[8.526854],[8.337568],[6.708476],[1.590853],[-7.020432],[-2.423910],[1.344229],[2.282202],[1.112245],[3.377951],[4.878266],[9.667743],[8.746495],[-2.273023],[-0.230061],[-7.432911],[8.814543],[-0.843418],[-5.448649],[9.708537],[-7.104567],[1.416544],[4.746164],[1.840235],[-8.525385],[2.603986],[-4.930892],[-9.229961],[8.569952],[2.059787],[-2.876442],[-8.486935],[-1.335107],[-0.071432],[-6.001995],[5.288591],[3.900576],[-3.418889],[3.613651],[4.053166],[-2.006820],[-2.719321],[9.556262],[-9.100530],[2.760488],[-6.291326],[-2.937507],[-0.744106],[8.325395],[6.136059],[-9.007756],[5.221044],[-4.451818],[-0.185988],[6.609095],[1.268518],[-1.807234],[9.249866],[-5.750398],[3.806653],[7.702114],[8.682673],[-7.746202],[-4.659262],[-5.020293],[0.097746],[-9.105017],[8.997673],[-2.154458],[1.121663],[6.168506],[-8.310829],[-8.553990],[-6.640250],[1.043568],[-9.795463],[9.558335],[-8.881079],[9.878447],[-3.879337],[9.694336],[2.407396],[-3.807009],[-0.920429],[-4.456130],[-7.213977],[-7.715558],[-2.259416],[-4.416455],[-0.800274],[-2.312736],[8.615362],[-5.134363],[4.589953],[-1.072595],[-5.389328],[8.255923],[-3.874195],[-4.749511],[-5.106969],[-2.733881],[-0.854711],[0.473873],[0.136592],[8.002979],[-5.932593],[-9.988950],[-8.226197],[9.076319],[3.671443],[6.030807],[8.183422],[3.260021],[-2.361894],[-5.606962],[-0.957826],[3.151569],[-5.747176],[7.405692],[3.315581],[8.929719],[-8.303344],[1.913615],[-5.007781],[-5.240571],[-2.338394],[6.106613],[-7.188480],[1.823835],[-8.934644],[-3.706205],[-4.122236],[-4.695636],[-9.311682],[-7.149879],[-2.567447],[8.449867],[-7.713756],[0.133823],[-1.240329],[-0.253167],[8.244566],[-2.716166],[-2.518717],[-9.453217],[-1.848287],[3.019543],[3.070738],[5.839242],[-6.622839],[6.948176],[4.472219]], dtype = "float32")#candidate|9534|(630, 1)|const|float32
call_9532 = func_1652_call(relay.reshape(const_9533.astype('float32'), [15, 1, 14]), relay.reshape(const_9534.astype('float32'), [15, 3, 14]), )
call_9535 = func_1652_call(relay.reshape(const_9533.astype('float32'), [15, 1, 14]), relay.reshape(const_9534.astype('float32'), [15, 3, 14]), )
output = relay.Tuple([call_9529,call_9532,const_9533,const_9534,])
output2 = relay.Tuple([call_9530,call_9535,const_9533,const_9534,])
func_9540 = relay.Function([], output)
mod['func_9540'] = func_9540
mod = relay.transform.InferType()(mod)
output = func_9540()
func_9541 = relay.Function([], output)
mutated_mod['func_9541'] = func_9541
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6048_call = mod.get_global_var('func_6048')
func_6050_call = mutated_mod.get_global_var('func_6050')
call_9542 = func_6048_call()
call_9543 = func_6048_call()
output = call_9542
output2 = call_9543
func_9554 = relay.Function([], output)
mod['func_9554'] = func_9554
mod = relay.transform.InferType()(mod)
mutated_mod['func_9554'] = func_9554
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9554_call = mutated_mod.get_global_var('func_9554')
call_9555 = func_9554_call()
output = call_9555
func_9556 = relay.Function([], output)
mutated_mod['func_9556'] = func_9556
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9554_call = mod.get_global_var('func_9554')
func_9556_call = mutated_mod.get_global_var('func_9556')
call_9557 = func_9554_call()
call_9558 = func_9554_call()
func_534_call = mod.get_global_var('func_534')
func_537_call = mutated_mod.get_global_var('func_537')
var_9583 = relay.var("var_9583", dtype = "int8", shape = (1568,))#candidate|9583|(1568,)|var|int8
call_9582 = relay.TupleGetItem(func_534_call(relay.reshape(var_9583.astype('int8'), [16, 7, 14])), 0)
call_9584 = relay.TupleGetItem(func_537_call(relay.reshape(var_9583.astype('int8'), [16, 7, 14])), 0)
func_5171_call = mod.get_global_var('func_5171')
func_5173_call = mutated_mod.get_global_var('func_5173')
call_9602 = relay.TupleGetItem(func_5171_call(relay.reshape(call_9582.astype('int8'), [1, 1568])), 0)
call_9603 = relay.TupleGetItem(func_5173_call(relay.reshape(call_9582.astype('int8'), [1, 1568])), 0)
output = relay.Tuple([call_9557,call_9582,var_9583,call_9602,])
output2 = relay.Tuple([call_9558,call_9584,var_9583,call_9603,])
func_9607 = relay.Function([var_9583,], output)
mod['func_9607'] = func_9607
mod = relay.transform.InferType()(mod)
var_9608 = relay.var("var_9608", dtype = "int8", shape = (1568,))#candidate|9608|(1568,)|var|int8
output = func_9607(var_9608)
func_9609 = relay.Function([var_9608], output)
mutated_mod['func_9609'] = func_9609
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9654 = relay.var("var_9654", dtype = "uint32", shape = ())#candidate|9654|()|var|uint32
var_9655 = relay.var("var_9655", dtype = "uint32", shape = (6, 15, 1))#candidate|9655|(6, 15, 1)|var|uint32
bop_9656 = relay.greater(var_9654.astype('bool'), var_9655.astype('bool')) # shape=(6, 15, 1)
func_8327_call = mod.get_global_var('func_8327')
func_8329_call = mutated_mod.get_global_var('func_8329')
call_9662 = relay.TupleGetItem(func_8327_call(), 3)
call_9663 = relay.TupleGetItem(func_8329_call(), 3)
var_9666 = relay.var("var_9666", dtype = "uint32", shape = (6, 15, 8))#candidate|9666|(6, 15, 8)|var|uint32
bop_9667 = relay.not_equal(var_9655.astype('bool'), var_9666.astype('bool')) # shape=(6, 15, 8)
func_1652_call = mod.get_global_var('func_1652')
func_1655_call = mutated_mod.get_global_var('func_1655')
const_9672 = relay.const([[4.352870,5.904865,7.278901,6.985193,-5.980413,2.972504,9.652396,9.263695,8.890013,-7.678177,-9.870687,-9.710020,-6.642761,5.012005,9.116564,-8.945304,7.510967,1.942145,-0.419572,-5.582762,-0.970842,-7.334057,-6.254750,3.614163,6.608652,-8.787266,4.681490,5.608146,7.486853,-6.239062,7.388856,2.377089,9.963390,4.329763,4.550020,-5.643867,1.111086,4.297460,9.414298,-3.525469,-5.045010,-4.724639,1.196353,-3.584156,4.825323,-6.767364,4.377191,1.412063,-8.658975,-1.865914,-4.690406,0.572435,3.080430,-9.093443,7.934173,5.106923,9.884706,-3.540027,8.366340,8.240767,1.910583,3.405341,7.146055,1.278127,-5.502164,4.617078,8.218128,-3.425813,6.276452,2.271048,0.196191,1.420054,-0.751191,-7.762369,-9.141875,-0.206911,7.658943,-9.603864,-7.902032,-0.172627,9.989395,-9.640945,-9.672252,2.312463,1.875543,-4.399116,-9.202135,7.540291,8.428571,-8.361731,-1.505696,-0.894307,8.537669,-0.225670,-4.895093,-6.777652,2.584386,-9.130520,0.204745,8.535550,-0.677553,-6.045578,0.138018,-3.489215,4.740566,-2.792076,9.815523,2.331779,1.719315,6.851635,-3.877295,0.498518,-0.539061,1.849666,-3.770755,-3.110362,-8.189775,1.701541,-7.944272,2.054886,-4.918586,5.992076,-1.552729,-2.240944,5.466433,4.978180,5.395998,2.166206,7.588835,-8.555133,1.441048,-0.289839,6.295048,-9.981532,3.575680,5.813317,0.497490,-7.880409,1.773645,-8.423046,-7.403781,-9.514506,-8.512320,9.115765,-8.134356,6.606551,-4.727168,1.680686,7.184746,7.869831,4.557559,9.945814,-7.117480,-0.138040,-5.727328,-0.143014,2.242269,2.661382,-3.108853,6.734376,-7.209396,-9.204871,-8.108765,-7.674531,3.970437,2.972901,-4.534215,-8.472894,-0.697915,-8.116877,0.882591,6.172703,2.766557,-8.751312,0.037731,-0.525399,9.995257,-9.659940,-2.857353,4.343909,-7.047322,7.841809,0.668293,0.008559,-7.979701,8.539609,-1.416349,-7.951233,6.880252,2.873374,-5.383310,-4.368920,6.516478,-9.623305,4.122728,8.760788,-1.157444,-5.777898,-8.641127,9.772672,7.569119,-5.467348,0.129369,6.879579,-3.739830,3.080289,-4.795759,-8.596828,-6.919575,9.660255]], dtype = "float32")#candidate|9672|(1, 210)|const|float32
var_9673 = relay.var("var_9673", dtype = "float32", shape = (630,))#candidate|9673|(630,)|var|float32
call_9671 = func_1652_call(relay.reshape(const_9672.astype('float32'), [15, 1, 14]), relay.reshape(var_9673.astype('float32'), [15, 3, 14]), )
call_9674 = func_1652_call(relay.reshape(const_9672.astype('float32'), [15, 1, 14]), relay.reshape(var_9673.astype('float32'), [15, 3, 14]), )
output = relay.Tuple([bop_9656,call_9662,bop_9667,call_9671,const_9672,var_9673,])
output2 = relay.Tuple([bop_9656,call_9663,bop_9667,call_9674,const_9672,var_9673,])
func_9695 = relay.Function([var_9654,var_9655,var_9666,var_9673,], output)
mod['func_9695'] = func_9695
mod = relay.transform.InferType()(mod)
mutated_mod['func_9695'] = func_9695
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9695_call = mutated_mod.get_global_var('func_9695')
var_9697 = relay.var("var_9697", dtype = "uint32", shape = ())#candidate|9697|()|var|uint32
var_9698 = relay.var("var_9698", dtype = "uint32", shape = (6, 15, 1))#candidate|9698|(6, 15, 1)|var|uint32
var_9699 = relay.var("var_9699", dtype = "uint32", shape = (6, 15, 8))#candidate|9699|(6, 15, 8)|var|uint32
var_9700 = relay.var("var_9700", dtype = "float32", shape = (630,))#candidate|9700|(630,)|var|float32
call_9696 = func_9695_call(var_9697,var_9698,var_9699,var_9700,)
output = call_9696
func_9701 = relay.Function([var_9697,var_9698,var_9699,var_9700,], output)
mutated_mod['func_9701'] = func_9701
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9438_call = mod.get_global_var('func_9438')
func_9439_call = mutated_mod.get_global_var('func_9439')
call_9748 = relay.TupleGetItem(func_9438_call(), 1)
call_9749 = relay.TupleGetItem(func_9439_call(), 1)
func_4619_call = mod.get_global_var('func_4619')
func_4622_call = mutated_mod.get_global_var('func_4622')
var_9753 = relay.var("var_9753", dtype = "float32", shape = (180,))#candidate|9753|(180,)|var|float32
call_9752 = relay.TupleGetItem(func_4619_call(relay.reshape(var_9753.astype('float32'), [180,])), 4)
call_9754 = relay.TupleGetItem(func_4622_call(relay.reshape(var_9753.astype('float32'), [180,])), 4)
output = relay.Tuple([call_9748,call_9752,var_9753,])
output2 = relay.Tuple([call_9749,call_9754,var_9753,])
func_9761 = relay.Function([var_9753,], output)
mod['func_9761'] = func_9761
mod = relay.transform.InferType()(mod)
mutated_mod['func_9761'] = func_9761
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9762 = relay.var("var_9762", dtype = "float32", shape = (180,))#candidate|9762|(180,)|var|float32
func_9761_call = mutated_mod.get_global_var('func_9761')
call_9763 = func_9761_call(var_9762)
output = call_9763
func_9764 = relay.Function([var_9762], output)
mutated_mod['func_9764'] = func_9764
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8082_call = mod.get_global_var('func_8082')
func_8083_call = mutated_mod.get_global_var('func_8083')
call_9766 = func_8082_call()
call_9767 = func_8082_call()
output = call_9766
output2 = call_9767
func_9768 = relay.Function([], output)
mod['func_9768'] = func_9768
mod = relay.transform.InferType()(mod)
output = func_9768()
func_9769 = relay.Function([], output)
mutated_mod['func_9769'] = func_9769
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9320_call = mod.get_global_var('func_9320')
func_9322_call = mutated_mod.get_global_var('func_9322')
call_9776 = relay.TupleGetItem(func_9320_call(), 2)
call_9777 = relay.TupleGetItem(func_9322_call(), 2)
func_7428_call = mod.get_global_var('func_7428')
func_7429_call = mutated_mod.get_global_var('func_7429')
call_9779 = relay.TupleGetItem(func_7428_call(), 0)
call_9780 = relay.TupleGetItem(func_7429_call(), 0)
output = relay.Tuple([call_9776,call_9779,])
output2 = relay.Tuple([call_9777,call_9780,])
func_9792 = relay.Function([], output)
mod['func_9792'] = func_9792
mod = relay.transform.InferType()(mod)
mutated_mod['func_9792'] = func_9792
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9792_call = mutated_mod.get_global_var('func_9792')
call_9793 = func_9792_call()
output = call_9793
func_9794 = relay.Function([], output)
mutated_mod['func_9794'] = func_9794
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6490_call = mod.get_global_var('func_6490')
func_6491_call = mutated_mod.get_global_var('func_6491')
call_9826 = func_6490_call()
call_9827 = func_6490_call()
func_7938_call = mod.get_global_var('func_7938')
func_7941_call = mutated_mod.get_global_var('func_7941')
var_9835 = relay.var("var_9835", dtype = "bool", shape = (896,))#candidate|9835|(896,)|var|bool
call_9834 = relay.TupleGetItem(func_7938_call(relay.reshape(var_9835.astype('bool'), [896,])), 4)
call_9836 = relay.TupleGetItem(func_7941_call(relay.reshape(var_9835.astype('bool'), [896,])), 4)
func_7998_call = mod.get_global_var('func_7998')
func_8004_call = mutated_mod.get_global_var('func_8004')
const_9839 = relay.const([[2,-7,-5,-6,8,9,6,-5,4,-8,2,1,-4,-4,8,2,9,8,-10,2,-8,9,3,-1,-7,-10,-2,8,1,-6,1,-8,9,2,-2,9,-5,6,-4,7,-7,-2,-7,4,2,6,1,-4,1,2,-10,7,-1,3,1,9,-6,-8,1,2,5,-7,-1,-5,-8,-10,-9,-6,-2,-6,-1,-3,-5,-2,3,2,-2,-4,-1,-9,-7,-9,-6,5,-6,-10,-7,5,-4,-10,3,-6,-2,-9,-9,-4,-7,-3,10,10,-10,-2,-5,-8,-4,-7,10,-1,4,-7,-8,1,6,10,-3,-1,-3,7,9,-7,4,1,9,-6,2,8,-8,7,5,1,8,-1,4,8,-3,-8,1,1,-9,-5,-4,-5,5,6,9,-8,-9,7,8,7,-2,-8,-4,5,8,8,-6,-4,-5,1,-8,-3,9,-10,-7,8,-4,6,-7,-1,2,7,-2,-7,1,-3,8,-6,5,-3,3,-6,10,-4,3,-2,-7,-1,1,-6,-9,-3,-4,-3,7,3,-9,-8,9,6,9,4,-10,-3,-6,-5,-7,-1,9,9,-2,-7,-1,2,7,1,9,-2,-2,-1,-5,5,-7,4,-10,4,-7,-5,-6,-8,8,-10,5,-7,6,-9,-4,-4,9,-9,-3,3,5,-8,-8,5,6,-4,-5,1,-6,-4,-5,3,6,-2,-6,7,-4,2,1,-7,-3,9,-9,3,3,8,-4,1,-3,-9,8,10,-2,4,-10,-2,10,-4,4,-8,5,-2,-7,10,-5,-8,-6,-7,-1,-4,1,-7,-7,-2,10,-7,-8,-3,1,-6,4,-1,4,-3,-6,9,2,10,9,-2,4,2,-8,8,10,-6,-1,9,5,-2,6,10,-9,9,2,5,-9,-9,-3,6,2,2,-1,1,-2,6,-6,7,-7,-3,6,-7,4,3,5,-5,-3,2,-7,-9,8,8,-4,-1,-1,-1,10,-1,-6,-6,-4,-1,7,1,8,4,5,-2,-6,9,-7,2,10,6,10,10,2,-2,-5,-4,3,1,-1,-9,7,-2,-10,-4,2,8],[-1,-7,-10,-3,-2,-9,6,-2,-4,3,9,-8,2,9,1,7,6,4,-4,10,-5,-10,-9,-7,5,4,5,-5,3,2,-1,-7,-6,-4,9,6,-3,4,-1,4,-9,10,-10,3,-8,7,-6,10,-7,-2,-6,-10,-5,10,-3,3,-3,-8,-7,4,7,-9,-8,-7,-1,3,7,8,-6,-9,-3,3,-5,-8,-3,10,-6,5,5,-2,8,6,9,-9,-2,-5,1,2,-2,-10,3,-7,8,4,1,-2,1,8,3,4,6,-2,-9,4,-5,6,-4,-6,2,-8,7,-6,9,6,-1,-9,2,-3,8,-10,-2,10,7,8,5,6,5,8,-6,-8,-9,-4,-10,9,6,10,8,-2,3,6,-4,-10,4,7,-6,-9,-3,5,-1,1,4,3,-1,-8,-5,-4,7,-9,6,5,10,7,6,-7,6,2,9,-3,10,-5,-6,-3,-3,-7,8,-2,-5,-4,-1,-8,10,1,5,2,-5,-10,7,7,-6,10,-8,4,1,4,2,-1,4,-4,5,-6,-4,-3,-8,1,-5,-9,3,-6,-3,6,-4,6,6,9,-7,-2,-9,-1,3,2,5,1,-5,10,-9,1,-1,1,10,-1,-5,7,-5,-3,-2,-10,-8,-5,-10,-1,1,-2,1,-4,-3,8,-5,2,-5,10,-1,6,-1,-2,-4,-10,5,1,-3,-8,7,4,5,2,2,9,2,5,-4,6,10,-7,6,-2,1,7,10,-8,9,6,3,7,1,-1,-8,7,3,-2,9,9,-8,8,8,-2,9,10,-5,9,8,-3,9,2,-1,2,-10,2,5,-5,-9,2,7,9,-9,-8,-8,-3,10,-10,2,2,1,10,-7,1,-4,-3,-6,-2,1,-2,-2,6,10,2,-8,-6,2,4,-10,5,-1,6,-1,2,10,-10,9,-2,-4,5,-1,-8,4,4,1,2,10,-9,6,-2,5,9,-10,7,7,3,-10,3,-4,-1,-6,9,9,-6,7,-1,4,8,-3,7,6,10,-2,9,-9,3,3,3,7,-7,9,-9],[-2,-6,-4,4,2,6,-8,10,-5,-5,2,-10,-7,-5,9,-9,5,-5,-8,-8,5,-4,9,10,-6,2,-3,9,1,8,2,-8,-5,-5,-2,-5,7,9,3,9,4,-9,4,-7,-4,3,-2,-2,-6,2,-9,4,-6,1,-2,-9,2,3,6,10,-5,-7,-8,8,5,1,-6,-2,-9,10,-5,-8,-6,4,-1,5,1,-6,10,-2,-1,1,-9,-10,7,-10,10,1,6,-10,-4,-4,-5,-6,4,2,-1,5,-9,8,4,10,3,9,-1,-8,-4,-1,-5,-5,-5,4,-3,5,3,-8,1,-10,1,6,10,6,8,-4,6,-10,8,8,3,3,-9,5,-9,4,6,-10,4,10,-5,3,-6,4,-8,-7,-6,-9,1,4,-8,-10,8,9,-7,-2,-3,-6,7,-3,10,6,-10,10,-8,3,-5,-8,-2,5,-8,-4,1,2,-9,4,6,-5,6,2,-4,-8,6,1,5,-7,-10,-7,-10,2,-5,9,8,-10,3,-8,4,5,-4,-10,-2,-3,10,5,9,1,4,7,-6,-6,-8,-8,-10,6,9,4,-5,-4,-7,6,8,1,-7,-6,5,4,8,-8,4,4,-10,-7,-5,9,-1,1,-10,1,-1,2,1,-9,-7,9,1,-7,10,-5,2,-9,8,-2,2,-6,4,-7,4,-6,-5,2,-6,8,-10,1,8,7,-1,4,6,-4,-8,5,-9,10,-4,9,-1,6,-1,-3,10,-4,-1,-2,-8,5,-9,7,1,-1,2,-5,-8,-2,9,-9,7,7,2,5,8,-6,-2,5,2,8,-8,7,-5,5,6,2,9,-3,3,-1,-2,7,9,9,10,7,2,3,3,-3,4,-4,9,4,-9,-4,-3,7,5,-5,-5,2,-6,-7,5,-10,9,1,-3,-9,-1,5,4,-6,-10,-5,-3,2,-1,6,3,4,2,-10,-2,9,-4,5,-8,8,-2,-1,-1,2,-6,-10,6,10,9,3,1,-5,8,-4,1,-2,-4,-7,10,8,2,4,2,-8,-6,-4,-4,-3],[-9,9,-6,6,-6,6,4,1,-10,6,10,4,-6,4,-7,4,-1,-9,-4,10,8,5,10,8,2,1,-9,-8,3,-6,-1,6,3,-1,-10,8,-7,-10,8,6,-3,2,3,-8,3,9,-6,8,-2,-6,-1,8,7,6,5,7,-2,1,-10,4,-5,-9,-7,10,-7,-2,3,6,-10,-7,-6,-5,7,4,7,3,10,-10,-3,8,7,8,-10,1,-9,-4,-5,1,-7,1,2,3,-8,-1,-5,10,-7,-3,-3,8,3,4,1,1,-2,-1,6,8,-10,4,-8,-9,-3,5,-7,5,-4,-9,8,-4,-10,-7,-2,-10,-6,8,-9,2,-1,7,9,-9,4,-8,8,3,7,-4,-4,1,-1,7,-8,-3,5,9,3,-5,-8,9,4,-3,1,2,-4,-9,-2,6,-3,-2,-8,-2,-9,-9,-9,2,-10,6,4,1,1,-4,4,6,8,8,9,8,9,6,8,3,4,-1,9,6,-2,4,10,-5,-8,-8,-7,4,6,5,-7,-1,-10,-7,4,9,-6,4,-5,-8,-4,-7,-3,-8,-8,-2,-1,-5,-7,2,-8,9,-5,1,2,2,-8,-8,9,-1,-8,3,-7,-2,1,-8,-6,4,-8,1,6,7,-2,4,-10,8,7,-9,10,-1,-7,9,-5,-5,7,2,-1,7,3,-3,-4,3,4,8,-5,-4,-9,8,-5,-7,-10,8,-8,-5,6,-6,-10,-4,2,8,-2,-2,7,-4,-6,7,-10,7,9,10,9,6,6,-4,3,-8,6,7,-1,-8,-2,4,9,9,-5,-3,-7,-6,8,-3,-3,7,10,-5,-5,-9,9,8,-5,5,-7,4,7,9,1,-8,3,-6,-7,6,-5,8,10,-1,4,7,-6,7,1,1,-10,-6,2,7,-4,-3,10,2,-9,7,9,-5,4,-8,-10,9,-6,4,-9,-7,-4,2,2,-5,5,2,-3,8,-1,-4,-3,-2,8,-7,6,9,-6,3,-5,7,-10,5,-10,-5,-9,-3,-10,3,2,2,-8,8,-4,-10,-3,10]], dtype = "int8")#candidate|9839|(4, 392)|const|int8
const_9840 = relay.const([0.930753,8.422994,0.630231,-0.351912,-5.807368,7.981805,9.820948,2.489784,-8.077567,0.995864,5.552421,5.241243,-2.603892,-2.710917,-4.269539,3.535819,-6.643026,2.694856,3.630743,9.177131,-4.933016,-5.725191,-7.313153,8.890419,5.566575,2.848966,6.155991,-8.771633,-0.321728,6.240585,6.601498,-3.576116,0.146843,-0.982633,7.172918,-1.899110,-2.848056,5.288989,2.485592,-5.577523,-9.671162,8.757513,-2.010307,6.394779,9.110377,9.681661,1.804195,-5.696245,3.974991,6.694862,-8.234131,6.012864,0.062844,5.205951,9.348140,0.859271,9.851613,8.694854,-5.721744,-0.642938,4.506560,5.596955,1.164415,8.001531,-1.602297,-2.172973,-8.885990,2.773731,-3.516875,-9.144695,-7.695797,7.442502,3.129824,-3.940862,0.056179,9.654172,-8.382101,4.049815,-6.128536,1.339973,-1.579779,5.233920,2.369970,-1.173750,9.124894,2.437209,-7.924499,5.155885,6.918816,-7.522778,-2.616686,8.959782,-2.907430,-6.902178,2.151462,6.903714,5.736783,-4.227095,1.661437,2.305912,-0.255777,9.536020,3.719401,-7.282992,-6.083684,-3.424630,-6.173198,5.811563,-5.169816,9.679874,7.926202,6.846496,9.849220,5.467051,-4.945311,2.312293,5.190526,-3.164266,7.153123,0.931816,3.905244,-7.672360,6.856743,-5.970951,8.522009,8.948508,-6.686939,-0.119878,1.707261,-2.355208,-6.267932,-1.907611,-0.864613,-2.199165,9.425988,3.480744,7.637900,-6.476680,-1.043622,5.315759,-0.173909,-3.075976,7.804279,-8.573756,8.854593,4.246943,-0.943247,1.404498,-4.364263,-4.098506,-0.531971,-8.906995,9.411751,-2.286353,3.301832,4.548851,5.458192,-0.733468,-0.461378,8.983443,3.593687,4.393559,-3.429604,7.396534,2.896812,-2.998810,1.570966,4.693146,5.390730,-6.720478,7.099621,-2.166166,-8.598691,-2.385299,0.552106,-7.086017,-4.869432,-2.457448,-9.981871,7.174185,7.775616,8.026480,-3.952399,1.982210,6.895203,-9.389300,0.535350,4.947036,1.723321,9.048171,5.217797,6.170521,4.545693,-2.261148,5.660475,6.861776,3.845138,-9.302260,-5.925941,5.542276,9.209220,-6.242004,-4.363668,-5.534325,6.768678,-0.822190,9.686504,-0.729546,2.054234,3.227853,-8.010961,4.883432,8.040566,9.178445,3.966875,8.415078,-7.648104,1.248156,1.523143,-1.696927,6.184742,9.105864,3.090459,-4.111404,-4.490736,6.049757,-7.130654,-0.899117,-4.487022,3.476564,-4.036298,8.377660,7.473000,2.516902,-7.272249,1.782340,-2.577593,9.883078,2.536301,-2.040706,9.840860,-5.922777,-9.935808,4.178524,8.130479,-3.508588,-2.173263,-9.873097,0.374722,-6.033067,-3.127086,3.581001,0.739226,-0.029434,-9.012221,-0.588841,-6.385973,-4.704286,-7.374666,-2.704463,-5.214780,7.923074,-4.293586,-0.726864,-9.923057,9.964075,2.634811,5.701405,0.794735,6.580258,5.610284,6.029445,-5.285388,-1.828360,-0.766937,-2.005097,-3.884293,3.480751,-1.165764,-0.788974,-5.815795,0.730117,-3.864980,-8.313567,-2.703382,-6.497271,-7.355893,6.048900,7.965142,1.907032,-9.649494,-1.476690,8.878641,2.039292,-6.418305,-3.502163,-8.788290,-6.515798,4.344937,-5.453816,-4.471785,4.227334,3.446804,7.496543,-2.876799,-0.593051,2.083691,3.642354,-6.777409,-3.158842,-3.953332,2.265413,-4.723495,-1.493066,4.745360,7.512770,6.956092,-7.593580,1.240879,7.872043,-8.037192,7.653796,-4.659389,-1.436400,8.387888,5.741149,-3.219883,-4.301122,-6.129602,-7.881639,-8.578707,3.357523,-3.891945,-8.289166,-6.992224,1.114705,4.323013,-8.352078,-6.112156,-6.413988,5.407830,7.629706,-7.096917,-2.578853,-3.421046,-4.540222,-8.638149,-5.691232,7.068130,-8.091054,-7.300733,-3.141042,-8.629177,-6.948832,-4.647952,8.412436,-0.346928,0.855934,-7.892374,-0.494644,-0.558085,1.174093,-2.680761,0.726739,-5.104995,9.843226,3.462776,-1.383504,-6.765553,-9.076395,3.805281,-3.823110,5.597294,2.705339,5.558855,-7.202088,-7.739482,-9.737943,-4.415298,0.260385,-3.933442,2.888471,-6.921854,8.183074,-4.911026,1.116136,8.975407,-2.601047,0.411817,2.691682,2.350350,-6.162237,9.337082,-5.207166,-5.376716,0.100697,7.459433,2.485394,-3.204574,-3.914737,-4.690087,0.180401,-9.469593,-8.705418,1.737163,-3.912330,-0.769678,-0.132627,-3.720205,0.807381,-8.188290,0.508960,5.410577,-2.408981,1.883627,3.845021,-4.932913,-6.580089,-0.223408,9.443694,-3.351466,-2.501207,-8.991193,-8.627286,8.333646,-0.301576,-4.126053,9.356071,-1.358177,-8.821688,3.505898,9.023696,-8.379640,-9.298444,7.199830,-8.420099,0.198173,-1.862226,9.190743,-2.782661,-8.694437,8.392855,-9.308344,-4.834270,-0.574407,0.448503,-8.023066,8.687521,-0.642121,2.710949,0.344163,1.600069,-4.292998,8.343473,-9.324237,8.102314,-6.417987,-0.738484,5.531246,7.993990,9.124960,4.710172,0.769106,-8.646485,-2.782652,8.281497,9.982161,3.680520,-0.281213,3.878413,-4.418686,1.162492,1.934962,-6.307612,3.467941,-8.042436,-1.655586,-0.755049,8.016303,7.873854,5.232243,8.111609,9.423710,-7.681070,4.418689,-8.022311,-4.029061,-6.157229,6.793680,6.952224,-1.226724,9.384380,8.966755,3.326926,-6.139845,6.129195,5.950273,-6.383174,1.004018,6.549613,7.393207,-0.211271,5.290015,7.997385,8.330647,3.519035,4.238734,-8.869324,8.625892,2.066770,-2.664742,7.533307,3.845651,-0.945937,-8.821763,-3.834172,-9.324880,-1.845137,5.155796,-5.565882,-7.759302,1.327484,3.475718,-0.784026,5.111754,-4.226162,-8.685766,0.823498,-9.640640,-0.939459,5.398313,-5.580840,-4.685615,-5.798627,-2.000611,-1.247527,-7.213786,-3.467411,-8.132500,-0.005099,-0.013302,8.477757,-4.437477,5.219893,3.839164,-7.021853,-0.044801,-4.823196,5.137797,-6.747269,8.356709,-8.461908,-5.017584,2.577703,2.540366,-2.752173,8.116338,5.418400,0.929402,-7.339136,-8.229266,1.135019,3.318369,5.649831,-6.623922,-2.690998,6.166148,-9.249229,-9.882680,-5.163228,2.566511,3.930158,-3.167374,6.527413,5.187870,-8.999217,-3.555588,-2.701203,7.015145,-5.705787,-9.168613,-0.851195,7.665609,9.770740,-3.301195,3.484313,4.392063,-1.670026,5.183619,6.437525,1.343945,0.831345,9.456958,1.530209,0.185343,9.037214,5.871622,7.504781,-8.124088,-8.111313,-5.370452,-3.797733,-7.776796,-8.841071,-9.184682,2.918321,8.555908,3.214594,-2.692309,-4.533061,-4.935599,8.670991,1.679883,-0.552700,-7.476811,-0.578793,7.244704,-0.495932,-6.810173,2.412961,-8.788814,-4.215878,7.576083,-1.284429,2.095377,-8.266800,-7.831656,3.068457,-0.753720,9.197171], dtype = "float32")#candidate|9840|(630,)|const|float32
call_9838 = relay.TupleGetItem(func_7998_call(relay.reshape(const_9839.astype('int8'), [1568,]), relay.reshape(call_9834.astype('float64'), [135,]), relay.reshape(var_9835.astype('bool'), [896,]), relay.reshape(const_9840.astype('float32'), [630,]), ), 6)
call_9841 = relay.TupleGetItem(func_8004_call(relay.reshape(const_9839.astype('int8'), [1568,]), relay.reshape(call_9834.astype('float64'), [135,]), relay.reshape(var_9835.astype('bool'), [896,]), relay.reshape(const_9840.astype('float32'), [630,]), ), 6)
func_5732_call = mod.get_global_var('func_5732')
func_5733_call = mutated_mod.get_global_var('func_5733')
call_9848 = relay.TupleGetItem(func_5732_call(), 0)
call_9849 = relay.TupleGetItem(func_5733_call(), 0)
bop_9852 = relay.less_equal(call_9834.astype('bool'), var_9835.astype('bool')) # shape=(9, 15, 896)
bop_9855 = relay.less_equal(call_9836.astype('bool'), var_9835.astype('bool')) # shape=(9, 15, 896)
func_4619_call = mod.get_global_var('func_4619')
func_4622_call = mutated_mod.get_global_var('func_4622')
const_9862 = relay.const([-8.047086,2.173240,9.050776,7.645426,2.404274,0.173285,9.037152,2.778302,-5.151285,9.614870,-3.250348,-7.326149,-4.555081,-8.357514,2.803543,9.920556,7.961155,2.648611,2.561195,9.513133,1.123505,9.485403,7.601057,-7.011307,-6.179097,5.742050,0.520513,5.088843,-7.058687,4.258015,9.839011,7.454922,-1.273103,-5.020410,3.128992,-4.513380,-5.021611,0.934478,-2.671180,9.106320,-3.384428,-6.992244,-8.823846,0.022455,9.789815,0.110611,0.021201,-6.486944,4.425432,3.132088,-8.785412,6.203364,2.532207,-3.092074,-0.443117,0.086147,-2.918071,-2.435082,5.508453,7.185052,6.329943,4.461877,4.808262,-4.172086,-2.774048,9.503947,2.127056,2.859289,-5.130469,-7.874919,8.853910,9.746506,8.493440,1.335180,1.128894,-8.325595,9.266522,-0.700126,3.330328,6.872833,-5.336162,-9.328437,-9.378871,3.932426,5.525692,3.768831,3.142162,-1.278545,9.962209,2.277364,-5.803494,4.510605,7.079502,-2.346623,-6.905156,7.158443,-9.231237,-7.581189,5.246768,1.324084,6.149873,-2.679442,2.873480,-2.916412,-8.448977,-9.905386,4.792696,-9.054745,6.389311,9.590072,-6.968663,-2.124871,-7.615403,1.210900,-4.442517,-9.038385,-4.978959,-8.243505,5.026231,-3.737373,-4.411713,-9.291586,-6.613810,8.976832,6.592032,6.989914,3.990241,-6.660148,-3.923261,1.010844,0.511119,-9.591660,-3.320240,5.589986,9.934142,6.130456,-9.256401,9.337758,-8.347202,-0.630338,7.935848,-9.563417,-5.224767,-8.043145,-3.492077,4.093204,3.909867,7.431771,1.085461,5.540241,-2.621439,-0.469132,-9.395693,9.174507,-3.780040,-1.907845,2.792870,-1.982684,-3.051593,-1.046013,5.911695,-4.774683,-5.859474,-7.950155,-2.027114,-8.072573,4.723895,-0.095197,4.845064,-9.437133,5.946864,4.341024,4.263036,-0.253910,6.439679,9.631411,1.325131,6.497569,2.810563,8.943781], dtype = "float32")#candidate|9862|(180,)|const|float32
call_9861 = relay.TupleGetItem(func_4619_call(relay.reshape(const_9862.astype('float32'), [180,])), 1)
call_9863 = relay.TupleGetItem(func_4622_call(relay.reshape(const_9862.astype('float32'), [180,])), 1)
output = relay.Tuple([call_9826,call_9838,const_9839,const_9840,call_9848,bop_9852,call_9861,const_9862,])
output2 = relay.Tuple([call_9827,call_9841,const_9839,const_9840,call_9849,bop_9855,call_9863,const_9862,])
func_9867 = relay.Function([var_9835,], output)
mod['func_9867'] = func_9867
mod = relay.transform.InferType()(mod)
var_9868 = relay.var("var_9868", dtype = "bool", shape = (896,))#candidate|9868|(896,)|var|bool
output = func_9867(var_9868)
func_9869 = relay.Function([var_9868], output)
mutated_mod['func_9869'] = func_9869
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8929_call = mod.get_global_var('func_8929')
func_8930_call = mutated_mod.get_global_var('func_8930')
call_9923 = func_8929_call()
call_9924 = func_8929_call()
output = call_9923
output2 = call_9924
func_9933 = relay.Function([], output)
mod['func_9933'] = func_9933
mod = relay.transform.InferType()(mod)
mutated_mod['func_9933'] = func_9933
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9933_call = mutated_mod.get_global_var('func_9933')
call_9934 = func_9933_call()
output = call_9934
func_9935 = relay.Function([], output)
mutated_mod['func_9935'] = func_9935
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4925_call = mod.get_global_var('func_4925')
func_4926_call = mutated_mod.get_global_var('func_4926')
call_9942 = func_4925_call()
call_9943 = func_4925_call()
func_5997_call = mod.get_global_var('func_5997')
func_5999_call = mutated_mod.get_global_var('func_5999')
call_9947 = relay.TupleGetItem(func_5997_call(), 0)
call_9948 = relay.TupleGetItem(func_5999_call(), 0)
output = relay.Tuple([call_9942,call_9947,])
output2 = relay.Tuple([call_9943,call_9948,])
func_9962 = relay.Function([], output)
mod['func_9962'] = func_9962
mod = relay.transform.InferType()(mod)
mutated_mod['func_9962'] = func_9962
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9962_call = mutated_mod.get_global_var('func_9962')
call_9963 = func_9962_call()
output = call_9963
func_9964 = relay.Function([], output)
mutated_mod['func_9964'] = func_9964
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6061_call = mod.get_global_var('func_6061')
func_6062_call = mutated_mod.get_global_var('func_6062')
call_9972 = func_6061_call()
call_9973 = func_6061_call()
output = relay.Tuple([call_9972,])
output2 = relay.Tuple([call_9973,])
func_9975 = relay.Function([], output)
mod['func_9975'] = func_9975
mod = relay.transform.InferType()(mod)
mutated_mod['func_9975'] = func_9975
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9975_call = mutated_mod.get_global_var('func_9975')
call_9976 = func_9975_call()
output = call_9976
func_9977 = relay.Function([], output)
mutated_mod['func_9977'] = func_9977
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9994 = relay.var("var_9994", dtype = "int8", shape = (12, 6, 13))#candidate|9994|(12, 6, 13)|var|int8
var_9995 = relay.var("var_9995", dtype = "int8", shape = (12, 6, 13))#candidate|9995|(12, 6, 13)|var|int8
bop_9996 = relay.minimum(var_9994.astype('int8'), relay.reshape(var_9995.astype('int8'), relay.shape_of(var_9994))) # shape=(12, 6, 13)
func_7401_call = mod.get_global_var('func_7401')
func_7405_call = mutated_mod.get_global_var('func_7405')
const_10000 = relay.const(-3, dtype = "int8")#candidate|10000|()|const|int8
var_10001 = relay.var("var_10001", dtype = "bool", shape = (896,))#candidate|10001|(896,)|var|bool
call_9999 = relay.TupleGetItem(func_7401_call(relay.reshape(const_10000.astype('int8'), []), relay.reshape(var_10001.astype('bool'), [896,]), ), 4)
call_10002 = relay.TupleGetItem(func_7405_call(relay.reshape(const_10000.astype('int8'), []), relay.reshape(var_10001.astype('bool'), [896,]), ), 4)
func_7534_call = mod.get_global_var('func_7534')
func_7536_call = mutated_mod.get_global_var('func_7536')
call_10012 = relay.TupleGetItem(func_7534_call(), 0)
call_10013 = relay.TupleGetItem(func_7536_call(), 0)
func_9554_call = mod.get_global_var('func_9554')
func_9556_call = mutated_mod.get_global_var('func_9556')
call_10020 = func_9554_call()
call_10021 = func_9554_call()
output = relay.Tuple([bop_9996,call_9999,const_10000,var_10001,call_10012,call_10020,])
output2 = relay.Tuple([bop_9996,call_10002,const_10000,var_10001,call_10013,call_10021,])
func_10024 = relay.Function([var_9994,var_9995,var_10001,], output)
mod['func_10024'] = func_10024
mod = relay.transform.InferType()(mod)
var_10025 = relay.var("var_10025", dtype = "int8", shape = (12, 6, 13))#candidate|10025|(12, 6, 13)|var|int8
var_10026 = relay.var("var_10026", dtype = "int8", shape = (12, 6, 13))#candidate|10026|(12, 6, 13)|var|int8
var_10027 = relay.var("var_10027", dtype = "bool", shape = (896,))#candidate|10027|(896,)|var|bool
output = func_10024(var_10025,var_10026,var_10027,)
func_10028 = relay.Function([var_10025,var_10026,var_10027,], output)
mutated_mod['func_10028'] = func_10028
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10193 = relay.var("var_10193", dtype = "float64", shape = (2, 14, 5))#candidate|10193|(2, 14, 5)|var|float64
var_10194 = relay.var("var_10194", dtype = "float64", shape = (2, 14, 5))#candidate|10194|(2, 14, 5)|var|float64
bop_10195 = relay.add(var_10193.astype('float64'), relay.reshape(var_10194.astype('float64'), relay.shape_of(var_10193))) # shape=(2, 14, 5)
func_6562_call = mod.get_global_var('func_6562')
func_6563_call = mutated_mod.get_global_var('func_6563')
call_10198 = func_6562_call()
call_10199 = func_6562_call()
output = relay.Tuple([bop_10195,call_10198,])
output2 = relay.Tuple([bop_10195,call_10199,])
func_10200 = relay.Function([var_10193,var_10194,], output)
mod['func_10200'] = func_10200
mod = relay.transform.InferType()(mod)
mutated_mod['func_10200'] = func_10200
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10200_call = mutated_mod.get_global_var('func_10200')
var_10202 = relay.var("var_10202", dtype = "float64", shape = (2, 14, 5))#candidate|10202|(2, 14, 5)|var|float64
var_10203 = relay.var("var_10203", dtype = "float64", shape = (2, 14, 5))#candidate|10203|(2, 14, 5)|var|float64
call_10201 = func_10200_call(var_10202,var_10203,)
output = call_10201
func_10204 = relay.Function([var_10202,var_10203,], output)
mutated_mod['func_10204'] = func_10204
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10213 = relay.var("var_10213", dtype = "float64", shape = (3, 1, 2))#candidate|10213|(3, 1, 2)|var|float64
uop_10214 = relay.atanh(var_10213.astype('float64')) # shape=(3, 1, 2)
output = relay.Tuple([uop_10214,])
output2 = relay.Tuple([uop_10214,])
F = relay.Function([var_10213,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_10213,], output2)
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
