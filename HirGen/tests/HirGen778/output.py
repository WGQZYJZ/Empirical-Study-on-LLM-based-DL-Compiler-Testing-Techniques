import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_0 = relay.var("var_0", dtype = "uint16", shape = (15, 15, 1))#candidate|0|(15, 15, 1)|var|uint16
var_1 = relay.var("var_1", dtype = "uint16", shape = (15, 15, 6))#candidate|1|(15, 15, 6)|var|uint16
bop_2 = relay.not_equal(var_0.astype('bool'), var_1.astype('bool')) # shape=(15, 15, 6)
output = relay.Tuple([bop_2,])
output2 = relay.Tuple([bop_2,])
func_11 = relay.Function([var_0,var_1,], output)
mod['func_11'] = func_11
mod = relay.transform.InferType()(mod)
mutated_mod['func_11'] = func_11
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11_call = mutated_mod.get_global_var('func_11')
var_13 = relay.var("var_13", dtype = "uint16", shape = (15, 15, 1))#candidate|13|(15, 15, 1)|var|uint16
var_14 = relay.var("var_14", dtype = "uint16", shape = (15, 15, 6))#candidate|14|(15, 15, 6)|var|uint16
call_12 = func_11_call(var_13,var_14,)
output = call_12
func_15 = relay.Function([var_13,var_14,], output)
mutated_mod['func_15'] = func_15
mutated_mod = relay.transform.InferType()(mutated_mod)
var_211 = relay.var("var_211", dtype = "float32", shape = (1, 3, 4))#candidate|211|(1, 3, 4)|var|float32
uop_212 = relay.sqrt(var_211.astype('float32')) # shape=(1, 3, 4)
func_11_call = mod.get_global_var('func_11')
func_15_call = mutated_mod.get_global_var('func_15')
var_216 = relay.var("var_216", dtype = "uint16", shape = (225,))#candidate|216|(225,)|var|uint16
const_217 = relay.const([-8,-1,-10,-9,-10,1,1,-4,-8,2,6,-5,5,-7,7,-7,4,-7,-4,7,5,2,7,6,1,-9,6,-3,9,3,9,-2,1,-5,4,-8,9,-7,-6,-4,-5,-5,8,-9,5,3,-5,6,4,8,5,-9,8,3,-10,-2,-9,-5,2,-3,7,2,1,-7,-3,-3,3,-5,7,-6,4,-4,-2,1,5,10,10,-8,-1,-3,2,-3,7,7,-3,-5,-10,1,9,3,-3,-8,6,-3,-10,9,2,10,-9,5,1,-10,-8,10,-2,1,-7,-8,6,-10,-8,2,-1,9,-1,-4,4,-3,5,-10,-8,4,-2,8,6,6,-7,3,-1,1,-1,-2,9,7,-9,-2,-8,4,-1,-7,10,-10,-2,-8,9,4,-4,-3,4,-8,-7,-1,7,4,-6,4,8,7,-6,2,-4,-3,3,-1,8,-1,2,-9,-5,-8,5,9,3,-3,2,-4,4,-5,3,-5,9,-5,5,-9,-8,1,6,-7,7,8,7,-6,-9,-9,8,5,-7,-8,6,-3,2,-8,-4,-9,-6,10,1,6,8,-4,9,-6,10,9,9,10,5,-4,-4,-2,2,-8,8,2,-9,-2,6,7,2,-3,9,6,3,5,-3,-8,10,5,-9,-6,3,-1,8,4,3,10,-1,7,6,-1,-8,-3,6,8,7,6,-4,9,-4,-1,-10,-10,-9,7,9,-4,7,-7,7,8,3,-4,-2,10,-7,6,6,-10,-3,10,-5,10,4,-4,-7,5,-8,-7,-3,8,-10,9,2,-10,-8,-8,-9,-6,-8,-5,3,-4,-2,-1,2,7,6,7,-9,3,-1,2,-9,-4,9,3,1,4,10,8,-7,-5,3,10,-1,9,4,-2,10,-2,-7,-4,2,-2,5,6,7,6,-3,1,-9,-8,2,8,7,-4,4,-1,-7,-3,-4,-4,-2,10,7,1,-2,3,-8,7,-10,8,-8,-2,-3,-7,4,8,2,-3,-9,-8,-3,4,-1,-7,-1,-5,-7,6,-4,8,4,5,-6,-8,-3,6,7,-7,3,7,10,-5,-3,-8,-3,4,-2,5,5,3,-10,-4,-2,-5,-5,-9,6,-4,4,-5,-8,-6,6,-8,-5,-1,-3,3,-5,8,-1,-7,-2,8,-2,-5,-10,9,-2,-10,-2,-5,-3,-10,-7,8,-7,6,5,5,7,-6,-9,-6,3,-2,-5,10,3,6,-8,7,7,-5,9,10,8,-2,10,-9,-2,-10,8,-4,-1,3,5,7,5,-6,9,-10,-9,-5,-2,4,7,-2,-5,6,-7,7,8,5,5,-8,5,-3,-10,-5,-5,6,-4,-7,-5,9,3,-5,2,-4,1,-1,-2,3,5,4,-9,-1,1,6,-2,-1,10,6,7,-7,4,7,4,-7,1,8,4,-5,-9,2,-5,-6,10,-7,4,5,5,5,5,-8,-7,-6,-8,-7,-3,8,-3,-5,8,10,-7,3,9,1,2,-8,-8,10,-7,-2,-8,-10,-9,-4,6,-1,8,-5,2,1,-5,-2,3,-8,-1,-3,-5,7,-10,10,-4,-1,7,-9,1,-4,7,9,8,-4,-10,-7,2,8,7,-9,3,1,-5,-8,8,-3,7,-9,-9,-5,10,5,-6,-3,3,3,-2,-5,-5,-3,2,-2,-8,-6,-3,-8,-3,-6,-6,-3,1,-6,-10,-9,-1,-10,8,5,-2,-3,-2,-10,3,-5,5,9,-3,10,-5,10,3,2,1,-9,6,8,4,4,-1,6,6,5,-2,3,-6,-3,3,4,1,-7,-7,9,-2,-9,-10,1,2,-7,1,-2,-3,9,10,-9,7,2,-2,5,1,-7,1,-1,1,7,-6,-10,4,6,-3,9,-3,-5,-9,7,6,-5,1,10,-1,-6,8,7,-7,9,10,-1,-6,-7,9,-9,9,4,7,4,2,7,9,-3,-7,-8,10,-9,8,-3,4,-1,-3,7,-10,-10,-2,-4,10,-9,2,3,9,-8,2,3,3,-2,-9,-8,9,-3,4,-4,-7,-1,-2,-10,-8,5,10,-9,2,-9,10,1,-7,2,2,-8,-9,-7,-5,2,-5,-5,-7,-6,-6,1,4,3,8,5,-1,10,-1,-3,-6,-2,-3,4,1,-10,-6,-3,7,-2,-3,-7,-9,6,-6,6,5,-10,5,8,-5,5,1,2,3,-3,2,-1,-8,10,-6,-7,6,-9,3,-1,8,-10,3,7,7,-4,-1,-7,-4,5,5,10,9,-4,-9,-1,-10,-5,4,-1,-3,7,2,5,2,3,-9,-1,-4,-1,2,1,-4,7,10,6,-4,9,8,9,3,-9,7,-3,7,-6,-7,-4,-3,6,8,-9,6,8,4,-3,-1,9,4,-1,-5,1,5,-2,6,-4,-1,-7,-2,2,2,1,8,1,4,-5,2,1,-1,6,1,4,-4,1,-7,2,-8,5,4,10,-10,7,10,9,-10,-1,-6,5,5,6,8,-3,2,4,4,4,-8,-7,-10,2,-1,3,9,9,-3,-7,-4,7,8,4,3,7,-10,2,1,9,8,-3,-9,10,-9,3,9,1,-9,-1,-2,6,5,9,-1,-9,-2,7,-7,3,5,-9,-6,-4,-5,1,-3,7,-4,-3,-7,-7,7,8,10,9,-9,-2,9,2,-8,1,-10,9,-5,1,7,10,-10,9,2,-7,-8,-8,2,-3,2,4,-2,-6,-7,10,-4,9,9,-8,-8,5,-4,3,2,-8,9,6,7,10,-10,-8,-9,2,5,-2,-5,-8,-10,4,-8,6,-6,-1,-6,-7,-9,5,-1,7,-9,10,-8,2,3,9,10,-9,10,1,8,4,-2,7,-8,-1,5,-10,2,-10,9,6,-5,-6,-4,-10,-5,-2,-5,-10,3,-1,-5,-3,6,1,3,5,-2,-10,7,1,-6,1,-1,-6,2,-3,10,-3,-9,2,-2,9,-7,10,-1,-8,-3,-8,-9,9,2,8,9,-10,6,2,8,-1,2,-1,-4,10,9,4,-2,1,6,-8,3,-5,10,6,-1,-3,10,-6,2,-2,5,10,8,1,-1,10,5,-4,5,10,-8,-10,6,5,-3,-10,-2,6,-2,-5,-4,-8,2,-3,-3,-2,-8,9,8,4,10,2,2,5,2,8,7,-4,-7,6,2,1,10,-5,-6,2,1,-10,-1,-9,-7,9,-3,10,2,10,-4,5,2,6,9,4,3,6,-2,-7,4,-2,-8,8,10,5,8,-2,10,-10,6,-8,9,3,1,-10,-5,-1,-7,-5,7,-3,-10,7,2,8,1,-9,1,6,1,6,-10,-2,-6,-6,-7,-1,-3,-6,6,-3,9,1,-3,2,3,-1,-7,-10,10,-7,4,-3,-6,1,2,-3,5,2,1,3,4,-8,7,-3,5,-5,5,5,-6,5,2,10,2,-7,-6,8,6,-10,-6,-1,10,-10,-3,-10,3,6,3,-7,8,9,-6,-5,-5,-5,-7,-9,-10,3,6,-2,-9,8,-6,9,9,-9,7,7,-10,-2,-7,-3,-2,10,-2,-8,-3,-4,-1,5,5,7,10,5,-6,-7,9,-4,8,8,-8,-2,-5,10,-1,8,-8,9,10,-8,-8,3,-6,-10,-1,-4,-7,8], dtype = "uint16")#candidate|217|(1350,)|const|uint16
call_215 = relay.TupleGetItem(func_11_call(relay.reshape(var_216.astype('uint16'), [15, 15, 1]), relay.reshape(const_217.astype('uint16'), [15, 15, 6]), ), 0)
call_218 = relay.TupleGetItem(func_15_call(relay.reshape(var_216.astype('uint16'), [15, 15, 1]), relay.reshape(const_217.astype('uint16'), [15, 15, 6]), ), 0)
func_11_call = mod.get_global_var('func_11')
func_15_call = mutated_mod.get_global_var('func_15')
call_234 = relay.TupleGetItem(func_11_call(relay.reshape(var_216.astype('uint16'), [15, 15, 1]), relay.reshape(call_215.astype('uint16'), [15, 15, 6]), ), 0)
call_235 = relay.TupleGetItem(func_15_call(relay.reshape(var_216.astype('uint16'), [15, 15, 1]), relay.reshape(call_215.astype('uint16'), [15, 15, 6]), ), 0)
output = relay.Tuple([uop_212,call_215,var_216,const_217,call_234,])
output2 = relay.Tuple([uop_212,call_218,var_216,const_217,call_235,])
func_254 = relay.Function([var_211,var_216,], output)
mod['func_254'] = func_254
mod = relay.transform.InferType()(mod)
var_255 = relay.var("var_255", dtype = "float32", shape = (1, 3, 4))#candidate|255|(1, 3, 4)|var|float32
var_256 = relay.var("var_256", dtype = "uint16", shape = (225,))#candidate|256|(225,)|var|uint16
output = func_254(var_255,var_256,)
func_257 = relay.Function([var_255,var_256,], output)
mutated_mod['func_257'] = func_257
mutated_mod = relay.transform.InferType()(mutated_mod)
var_310 = relay.var("var_310", dtype = "uint64", shape = (11, 12, 10))#candidate|310|(11, 12, 10)|var|uint64
var_311 = relay.var("var_311", dtype = "uint64", shape = (11, 12, 10))#candidate|311|(11, 12, 10)|var|uint64
bop_312 = relay.add(var_310.astype('uint64'), relay.reshape(var_311.astype('uint64'), relay.shape_of(var_310))) # shape=(11, 12, 10)
func_11_call = mod.get_global_var('func_11')
func_15_call = mutated_mod.get_global_var('func_15')
var_323 = relay.var("var_323", dtype = "uint16", shape = (225,))#candidate|323|(225,)|var|uint16
const_324 = relay.const([-7,-3,-3,-8,1,-6,6,-1,2,2,10,-6,-9,-10,-6,-1,3,6,5,5,-7,-4,-3,-8,2,9,-9,4,8,2,-5,9,-8,-2,-8,-9,-1,9,-2,1,6,-6,2,2,4,-4,-8,-6,7,-1,6,1,5,-1,9,-10,1,8,6,3,-6,10,1,2,4,4,-3,9,-7,4,-4,10,10,9,10,7,-1,1,1,-10,9,6,9,10,8,1,-8,-5,1,-4,10,-8,-8,-2,4,-5,6,-5,-9,-10,-8,-6,3,7,-9,-6,2,-9,5,-1,-7,-2,-10,-7,-1,-5,-1,-7,6,10,-5,-4,10,-7,-9,4,5,-9,2,-3,7,3,-10,-4,-2,-2,1,-4,-1,8,1,6,-9,-10,-2,-5,2,-5,-6,-1,-3,5,-10,9,-2,-3,-10,-7,-3,1,4,2,-3,10,-8,-8,-3,9,4,5,6,6,-5,6,-4,5,4,-3,8,6,4,9,9,-1,7,-8,1,2,9,-6,-6,10,-10,-6,-6,-4,-8,-10,-2,-1,-4,-5,-5,3,-4,8,1,9,10,-10,10,1,-1,-3,9,-6,-3,7,8,3,-8,4,-8,3,-10,6,-10,-6,-7,4,4,-8,10,6,-7,2,9,-7,10,-5,-4,10,2,-3,-8,-5,-8,1,10,6,8,5,3,-4,-1,-1,4,8,-9,4,-9,-10,-4,5,-2,-3,8,-8,7,1,-5,-2,-8,-6,1,-4,9,-9,9,-8,4,9,-7,-4,3,2,-2,8,7,6,-3,10,6,-6,-1,6,-4,-1,4,-5,1,-4,6,-2,5,8,-8,-2,8,-3,-2,6,4,9,3,6,3,-6,3,9,5,7,-8,2,-9,-4,-4,9,10,-7,-1,-6,4,-3,-1,8,-4,3,-6,-7,-2,5,3,-3,1,-5,-4,7,4,-8,4,5,10,9,5,-10,9,10,-1,-5,4,5,3,-7,-3,6,-10,7,-8,-6,4,-7,-3,-5,1,-7,3,2,-3,5,-5,-3,-1,-5,-7,-2,-6,4,-8,-6,-2,-2,6,-1,5,6,4,-3,10,-5,-8,9,-6,7,-3,-2,9,-10,-10,-5,6,4,-1,-6,-6,9,8,2,-3,7,-4,-3,-3,-8,-5,-7,-2,-10,8,5,6,10,6,-5,10,6,-1,5,-3,4,-3,6,1,-10,1,3,-3,-9,-4,5,6,-6,-2,10,5,3,6,7,5,-6,-5,2,-3,-5,5,9,-3,2,-9,1,8,-3,-3,-4,8,-3,-1,8,-7,-1,5,8,6,-3,2,-8,-8,-9,-9,-9,4,-7,6,9,10,-8,9,-5,5,1,-4,10,-7,-4,1,-3,-5,10,-8,7,-10,-5,10,-7,9,-2,4,-6,-10,-7,-4,-6,3,-10,-6,10,-1,-6,-6,4,10,10,-8,4,7,-9,-4,-9,10,9,-4,3,-6,6,1,-9,6,4,6,-1,1,-3,4,3,1,9,5,-1,-10,-4,9,-3,-3,-10,-7,1,3,-5,7,-3,4,-4,-6,9,-3,1,6,-6,3,7,7,9,3,-8,-4,7,-5,-6,-7,6,-7,2,1,2,6,-3,7,-4,6,1,3,7,-10,-8,7,8,9,7,10,5,7,8,9,-4,-3,4,-4,5,-3,10,-7,4,-8,7,10,-1,-9,1,-10,1,-2,1,-8,-10,9,3,-8,-1,9,6,9,6,-8,-4,-4,4,-3,-1,-3,-2,-1,-8,3,9,9,-1,3,-6,4,9,-8,3,-10,-10,7,5,8,-1,5,3,3,2,-1,9,10,-3,-1,-10,3,3,-2,10,-2,-1,10,10,-5,-1,3,-2,-8,-3,-3,1,3,-8,10,4,-8,8,-8,1,-3,10,2,10,8,8,-6,-7,-3,-3,2,7,-4,-8,-3,4,1,1,9,-3,5,-8,10,-10,-2,-6,-2,-2,7,-7,-9,6,8,-3,-9,5,8,4,1,-1,-7,-5,9,5,9,8,-4,10,-2,-8,9,-4,7,7,2,-10,4,-9,-5,10,-6,-4,3,-2,-8,5,-4,-6,-8,8,10,10,5,6,-4,6,5,2,-5,-2,-5,-2,-7,-1,-1,9,-8,5,10,3,-10,-6,8,-4,2,-8,2,-7,10,7,6,-5,5,-8,-3,-1,-10,9,-6,-3,-8,7,-2,-10,2,-8,-3,5,-2,5,3,-10,4,1,4,-8,6,4,-10,2,6,-2,-2,-9,1,-10,9,-7,3,2,-3,-2,8,9,-4,1,1,-9,2,5,-1,8,-9,4,5,1,-8,9,1,-3,-10,-5,10,2,-9,3,-6,-1,-6,-6,10,-10,-10,-6,10,-8,-6,9,-4,-5,-10,4,-1,-10,9,-9,7,9,2,-10,7,-1,10,6,-1,-8,3,-8,8,-1,-5,-10,-2,2,4,-6,-10,3,-7,4,4,-10,6,1,-5,5,-5,-4,3,2,-8,10,7,5,-4,3,-3,-3,10,-4,-6,-7,-3,-9,9,-6,2,-2,-9,3,8,-1,1,-9,-8,8,-4,-7,9,7,-9,-2,1,2,-3,-5,-2,-9,10,6,2,4,-2,-7,10,9,-7,2,7,9,-10,-8,-1,-9,-4,9,-10,4,-7,-5,4,-8,-4,-10,6,-8,6,-1,2,9,5,-4,2,-1,10,6,9,-7,-4,-4,8,7,10,2,7,10,9,9,5,-2,5,10,-2,6,4,8,-4,6,4,7,-7,-5,4,-10,5,5,10,3,2,9,1,-10,4,-10,3,-10,-8,-9,-9,3,-10,4,-4,1,-6,4,8,4,-9,10,6,4,-5,6,3,7,-10,1,-8,3,-3,-3,8,-4,-4,1,-4,-3,10,-4,1,-6,2,8,-2,-4,-6,9,-6,3,9,9,-8,4,-4,-3,-8,9,-10,10,5,-8,-4,-9,2,-10,5,-6,-4,5,7,-4,-6,-8,9,8,-3,9,7,-8,9,10,9,-8,-6,-10,10,-1,8,-5,-7,-3,1,-10,9,9,-5,-1,-7,-9,4,8,-5,2,-6,2,-10,-6,8,-1,-3,2,-9,6,4,9,-5,3,5,5,10,7,-4,-1,10,-7,2,2,-4,9,4,-7,-6,8,4,5,3,-4,-6,1,-6,-8,10,2,-10,6,-9,-2,-3,-8,-6,-3,-6,9,-1,-7,-9,-7,-7,-6,10,-1,-5,5,3,-9,8,-1,-10,-6,1,9,-8,-2,7,-2,-10,-5,-5,-6,-6,9,-6,8,-1,8,6,3,-8,-9,-10,10,-3,6,-9,-8,7,1,-8,-1,3,-2,-1,-5,9,-3,-6,-1,-10,-8,-9,-6,-4,2,-5,-4,2,-7,10,-1,-7,-9,7,-1,9,8,8,6,10,-5,-1,-1,-4,8,-2,2,-5,-2,3,1,-7,-1,2,6,-5,5,7,-9,-8,-4,7,-10,10,-5,9,6,5,-8,7,9,2,-10,-1,1,-7,10,2,-6,-3,-5,7,8,-1,10,-10,-1,-10,5,-9,1,-1,2,10,-8,-1,7,6,-1,-2,4,8,8,6,1,10,-3,-2,8,3,7,1,-1,9,-4,2,7,-5,10,-8,7,3,-3,-3,9,9,9,7,-6], dtype = "uint16")#candidate|324|(1350,)|const|uint16
call_322 = relay.TupleGetItem(func_11_call(relay.reshape(var_323.astype('uint16'), [15, 15, 1]), relay.reshape(const_324.astype('uint16'), [15, 15, 6]), ), 0)
call_325 = relay.TupleGetItem(func_15_call(relay.reshape(var_323.astype('uint16'), [15, 15, 1]), relay.reshape(const_324.astype('uint16'), [15, 15, 6]), ), 0)
func_254_call = mod.get_global_var('func_254')
func_257_call = mutated_mod.get_global_var('func_257')
const_337 = relay.const([[-8.523205],[-5.563623],[-3.880004],[-1.616844],[-1.924732],[-3.461788],[6.164091],[6.911102],[-4.378393],[-7.664664],[-6.255410],[-3.059308]], dtype = "float32")#candidate|337|(12, 1)|const|float32
call_336 = relay.TupleGetItem(func_254_call(relay.reshape(const_337.astype('float32'), [1, 3, 4]), relay.reshape(var_323.astype('uint16'), [225,]), ), 2)
call_338 = relay.TupleGetItem(func_257_call(relay.reshape(const_337.astype('float32'), [1, 3, 4]), relay.reshape(var_323.astype('uint16'), [225,]), ), 2)
output = relay.Tuple([bop_312,call_322,var_323,const_324,call_336,const_337,])
output2 = relay.Tuple([bop_312,call_325,var_323,const_324,call_338,const_337,])
func_349 = relay.Function([var_310,var_311,var_323,], output)
mod['func_349'] = func_349
mod = relay.transform.InferType()(mod)
mutated_mod['func_349'] = func_349
mutated_mod = relay.transform.InferType()(mutated_mod)
func_349_call = mutated_mod.get_global_var('func_349')
var_351 = relay.var("var_351", dtype = "uint64", shape = (11, 12, 10))#candidate|351|(11, 12, 10)|var|uint64
var_352 = relay.var("var_352", dtype = "uint64", shape = (11, 12, 10))#candidate|352|(11, 12, 10)|var|uint64
var_353 = relay.var("var_353", dtype = "uint16", shape = (225,))#candidate|353|(225,)|var|uint16
call_350 = func_349_call(var_351,var_352,var_353,)
output = call_350
func_354 = relay.Function([var_351,var_352,var_353,], output)
mutated_mod['func_354'] = func_354
mutated_mod = relay.transform.InferType()(mutated_mod)
var_992 = relay.var("var_992", dtype = "bool", shape = (7, 13, 16))#candidate|992|(7, 13, 16)|var|bool
var_993 = relay.var("var_993", dtype = "bool", shape = (7, 13, 16))#candidate|993|(7, 13, 16)|var|bool
bop_994 = relay.logical_and(var_992.astype('bool'), relay.reshape(var_993.astype('bool'), relay.shape_of(var_992))) # shape=(7, 13, 16)
func_254_call = mod.get_global_var('func_254')
func_257_call = mutated_mod.get_global_var('func_257')
var_999 = relay.var("var_999", dtype = "float32", shape = (12, 1))#candidate|999|(12, 1)|var|float32
const_1000 = relay.const([[1,1,5,2,6,-5,-8,-8,5,10,-9,3,-8,4,6,-4,-10,-10,4,-4,-9,-3,-1,5,-8,-3,10,6,10,1,-10,10,1,-6,-2,-7,9,-8,-10,4,10,9,-7,7,7],[-1,2,-6,1,-9,-2,6,6,-10,8,6,-5,-9,10,-10,-5,-5,-4,1,-4,-2,5,-8,1,7,3,-1,-6,1,-6,4,-3,10,9,5,-10,-8,5,5,-3,7,-4,4,-9,-6],[7,-8,-9,10,-8,9,-1,2,-4,-4,-7,-5,-9,3,-6,-5,-10,-7,-1,-5,3,-8,3,-2,7,6,-7,7,9,-6,-10,10,-5,-7,4,-7,5,3,5,7,-3,8,-3,8,6],[9,-6,-5,5,-9,-3,-10,-2,-8,-10,9,-7,3,-5,-4,-6,8,-1,5,5,9,-10,8,-1,9,3,-3,8,-2,7,-5,-8,-5,7,7,5,2,4,-9,8,4,-9,-2,1,9],[10,10,-10,7,8,1,-1,-9,5,-7,8,-4,8,-4,-10,8,-9,-7,5,8,9,7,4,-2,5,-4,1,-10,2,8,6,-1,6,8,2,-5,7,1,-9,2,2,-9,-4,4,2]], dtype = "uint16")#candidate|1000|(5, 45)|const|uint16
call_998 = relay.TupleGetItem(func_254_call(relay.reshape(var_999.astype('float32'), [1, 3, 4]), relay.reshape(const_1000.astype('uint16'), [225,]), ), 3)
call_1001 = relay.TupleGetItem(func_257_call(relay.reshape(var_999.astype('float32'), [1, 3, 4]), relay.reshape(const_1000.astype('uint16'), [225,]), ), 3)
output = relay.Tuple([bop_994,call_998,var_999,const_1000,])
output2 = relay.Tuple([bop_994,call_1001,var_999,const_1000,])
func_1009 = relay.Function([var_992,var_993,var_999,], output)
mod['func_1009'] = func_1009
mod = relay.transform.InferType()(mod)
var_1010 = relay.var("var_1010", dtype = "bool", shape = (7, 13, 16))#candidate|1010|(7, 13, 16)|var|bool
var_1011 = relay.var("var_1011", dtype = "bool", shape = (7, 13, 16))#candidate|1011|(7, 13, 16)|var|bool
var_1012 = relay.var("var_1012", dtype = "float32", shape = (12, 1))#candidate|1012|(12, 1)|var|float32
output = func_1009(var_1010,var_1011,var_1012,)
func_1013 = relay.Function([var_1010,var_1011,var_1012,], output)
mutated_mod['func_1013'] = func_1013
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1995 = relay.var("var_1995", dtype = "float64", shape = (5, 12, 5))#candidate|1995|(5, 12, 5)|var|float64
uop_1996 = relay.asin(var_1995.astype('float64')) # shape=(5, 12, 5)
output = uop_1996
output2 = uop_1996
func_2005 = relay.Function([var_1995,], output)
mod['func_2005'] = func_2005
mod = relay.transform.InferType()(mod)
mutated_mod['func_2005'] = func_2005
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2006 = relay.var("var_2006", dtype = "float64", shape = (5, 12, 5))#candidate|2006|(5, 12, 5)|var|float64
func_2005_call = mutated_mod.get_global_var('func_2005')
call_2007 = func_2005_call(var_2006)
output = call_2007
func_2008 = relay.Function([var_2006], output)
mutated_mod['func_2008'] = func_2008
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2291 = relay.var("var_2291", dtype = "float32", shape = ())#candidate|2291|()|var|float32
var_2292 = relay.var("var_2292", dtype = "float32", shape = (11, 5, 4))#candidate|2292|(11, 5, 4)|var|float32
bop_2293 = relay.subtract(var_2291.astype('float32'), var_2292.astype('float32')) # shape=(11, 5, 4)
output = bop_2293
output2 = bop_2293
func_2297 = relay.Function([var_2291,var_2292,], output)
mod['func_2297'] = func_2297
mod = relay.transform.InferType()(mod)
var_2298 = relay.var("var_2298", dtype = "float32", shape = ())#candidate|2298|()|var|float32
var_2299 = relay.var("var_2299", dtype = "float32", shape = (11, 5, 4))#candidate|2299|(11, 5, 4)|var|float32
output = func_2297(var_2298,var_2299,)
func_2300 = relay.Function([var_2298,var_2299,], output)
mutated_mod['func_2300'] = func_2300
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2481 = relay.const([[[2.426650,6.189764,8.427009,-3.488434,0.555471,-1.811313,-3.381525,-7.130807,9.379919,4.182276,4.399220,-5.078617,0.764363],[3.265610,5.419090,-5.612933,8.349291,-7.438140,6.694752,-9.540070,-4.219305,-4.613587,3.921070,2.736536,6.493787,-4.649179],[-2.306571,-1.222149,6.558733,-9.019518,-8.331221,5.987972,2.451540,-5.920179,5.611086,4.355430,1.256015,-9.975753,-2.720538],[2.025048,-6.192736,-0.570291,-9.701704,-6.449014,4.078769,-2.362913,-8.407192,3.973957,6.245596,-6.317354,-3.768637,-6.421796],[1.972298,-1.888506,-2.947094,0.227691,9.589207,4.317637,-2.975917,1.251142,6.064500,4.121493,-9.881788,0.463752,6.028510],[-8.648774,4.236658,6.409202,0.636926,3.350750,-4.463942,-0.628871,-7.257388,6.297875,-0.659159,-5.899296,2.482146,2.407617],[-9.851253,4.451191,-6.947220,3.162357,3.942953,-7.482444,-9.339963,-0.876559,7.655538,6.607824,2.151400,-7.645292,7.348082],[8.627148,1.605598,-6.172169,4.186681,7.096582,0.171372,0.271167,6.855908,9.419877,3.096075,-7.112173,4.810260,8.315238],[8.679713,-4.978563,-5.754696,3.164560,-4.894972,-0.419133,1.699835,2.941642,-6.719442,0.516523,-3.702596,-6.666958,5.822232],[-9.940541,-5.202152,0.175429,-9.405529,-7.668142,1.868306,-8.601994,-6.439541,6.382278,-9.820255,-4.505141,9.680722,-1.283495],[4.511630,-4.036214,-5.486556,8.732282,-2.555020,-3.253870,-5.881599,5.242182,-2.969983,0.384351,-6.567513,-3.693372,8.452521],[-4.375171,5.715677,-0.320656,6.711104,3.079258,-8.967647,-3.039608,6.774382,8.478151,3.532724,1.558291,-5.472360,-1.659722],[3.387054,5.708643,-3.425056,7.218775,-5.950347,-5.279178,-3.558968,3.585766,-9.581781,0.994870,-2.914262,1.792411,-7.805341],[0.483623,3.382477,9.639916,3.641039,2.925759,-5.983440,3.418317,-3.878029,-2.032530,9.770228,0.931105,3.611906,1.061605],[2.152965,-8.582492,0.579476,-7.267765,2.101561,7.174805,-3.203882,-6.583495,0.559529,-3.065956,2.462592,5.094394,-4.968929]],[[-5.198441,1.604005,-7.902050,-9.317025,-2.606513,-5.498725,-6.283451,4.559949,-6.867906,-9.400891,-4.567925,-2.128481,-4.252586],[-2.908082,-8.904376,-6.468770,-8.777742,-6.789767,9.448140,1.726890,-6.482406,-3.442473,-7.354741,-4.246584,-1.305994,7.007968],[9.627865,2.661818,-0.455319,8.646455,-5.350935,6.525790,2.871373,0.976733,3.297005,6.253670,9.117677,-1.832790,0.866534],[-2.071713,-9.376466,-0.774243,-5.510790,7.800320,2.398079,5.999731,-5.785857,7.740763,1.003106,-5.883290,2.422670,-7.510559],[-1.694057,-0.431601,-1.115496,8.767112,0.501902,-7.390919,4.150361,-0.498761,-5.188874,-0.729599,-5.274992,-9.051096,4.157702],[-0.680132,-0.718018,4.676323,-8.834592,-9.649925,-2.557212,7.306770,-5.783858,5.266832,9.020252,-4.302161,-7.752352,-5.772213],[-1.944337,-9.319799,-0.395100,8.733087,8.993688,0.929346,-2.187445,-6.444035,3.277569,-6.412888,7.215597,7.774129,2.131285],[-7.685023,-2.116846,6.889174,-0.479221,-9.681548,-5.189452,1.240912,-8.231754,1.934828,3.528573,-0.841744,5.945573,-5.321275],[-2.094501,4.620565,1.227869,1.571352,2.608448,9.999991,-3.745116,-7.583132,8.358169,2.792584,-2.982609,-3.922446,-5.289674],[-3.131226,-1.524415,9.997800,-2.620125,-7.804654,-6.408665,3.460959,-9.681811,2.532457,2.702954,-3.123712,-6.455203,-9.872128],[-2.861294,-3.696865,1.294664,2.880700,1.199088,3.090020,8.603211,5.252317,3.334045,9.145918,6.118800,5.188347,-5.993751],[5.868986,0.872968,2.027074,8.766004,-0.273584,-7.671047,-6.295104,-6.805923,2.210502,9.463551,-7.624598,-5.421144,3.667651],[-4.357621,-8.775371,-1.633407,8.908480,3.807061,8.453180,-4.989191,-9.048350,2.416823,-8.190066,-1.377935,-1.810601,0.013288],[-4.730314,-1.971743,0.614745,-6.478581,-0.497725,-5.325570,-1.895893,-2.428674,-1.147323,-2.340437,-8.633461,6.961823,9.271795],[-1.290097,7.489583,-3.005438,0.350288,3.137161,-0.017381,-6.706758,-4.386390,-3.255896,2.907824,9.992807,-7.871634,-1.644286]],[[2.382880,1.588911,6.066009,-1.698676,3.039435,-4.601033,-1.252013,-5.884112,-9.887327,7.275421,6.811255,6.744395,-0.897052],[-0.425871,-6.353338,1.921434,-8.985653,4.885430,4.934453,-6.119416,-7.598776,9.019204,4.753191,6.438018,2.094733,-1.457049],[3.633441,0.091692,-7.620468,-5.454300,-4.498822,6.688591,-9.280080,-3.290092,-1.232386,2.966540,5.971054,0.614211,-3.104624],[-2.598463,1.233876,-5.152746,5.658023,9.889337,4.967791,-0.705494,9.264903,-8.197064,-0.422950,8.462649,4.935493,-0.253239],[-4.974374,5.337589,-7.618133,-8.921211,6.400203,-8.421933,-3.657137,-3.920432,4.210715,3.195665,-1.485351,1.253806,-3.440775],[-2.338726,5.361185,-3.662509,-6.528073,-3.741842,-5.139427,5.480214,9.451884,-0.889458,3.358591,4.744065,5.072105,6.033792],[-5.627883,6.820303,-6.214371,-6.173295,-2.703337,8.568678,3.464334,8.174136,-8.076260,8.937570,4.694366,1.505942,-9.582411],[1.670762,4.288687,-5.178756,2.975603,-0.839018,3.647793,1.239504,1.992583,-5.193010,-0.196743,-4.974492,-9.287009,-2.507531],[7.592359,-3.264404,-7.090219,-2.927267,9.565367,1.712461,-0.271091,-1.366936,1.632049,1.441066,-4.732977,7.544445,9.681091],[1.300271,5.679271,2.296935,3.568495,-6.179466,-6.300247,5.004942,9.036622,-1.113821,-7.181215,7.824546,1.476944,-7.908458],[1.196247,-9.352140,-1.380317,-8.111386,-8.229462,-4.864907,-6.045708,9.826248,8.618687,-5.071266,-8.169663,-6.353691,9.522147],[-9.770966,-2.427979,-3.750567,-1.557047,8.731338,-3.449772,-1.617990,0.921694,-4.783422,7.273115,-0.787992,-8.485249,-1.326871],[-3.100955,8.933682,-5.822696,-4.621084,-1.261349,-8.772387,9.905021,8.196749,-7.724037,-0.897908,0.411014,9.127042,1.448480],[1.932489,-2.866141,-1.842093,6.877569,-2.965271,7.441547,-3.074243,6.409283,-7.374769,-2.913031,-6.061385,7.741326,2.457437],[3.828017,6.812507,-3.439083,-8.061328,-8.905827,0.329396,-2.504321,-9.270966,-4.129189,6.197688,9.601036,5.024806,-0.384998]],[[-5.612153,-8.770883,-6.046195,-6.077350,-6.522482,-1.526703,1.796690,9.278425,-7.797871,-6.348507,2.342702,-0.071508,-0.853472],[-3.833676,7.856674,0.420138,-0.559699,3.720911,0.679561,4.708842,6.095669,-4.402963,-9.640971,3.326903,2.543560,4.363005],[2.748528,-8.554646,-7.920581,4.679359,0.100990,5.190522,-2.583068,-9.171724,5.398786,-5.579831,4.354644,0.217586,-4.408237],[2.555100,2.045954,7.870601,-0.320687,-4.897173,-2.308764,-2.426236,5.035733,-0.291657,3.439670,6.181150,-8.463085,0.248089],[6.813965,8.525063,8.941622,8.348454,-5.849656,0.120512,-1.157231,6.267438,5.078490,-4.399645,4.927595,2.729203,4.548717],[4.296359,-4.731132,-6.213333,-1.226845,1.776198,-4.227482,-8.281947,0.655438,3.213363,5.132184,2.049525,-5.179176,7.759409],[-1.112379,-9.197290,-3.388012,4.082229,-6.821001,-7.990661,5.491625,9.828396,-7.430658,-2.495791,1.664148,-8.262304,-1.732667],[-8.851584,5.543879,4.773453,-7.470044,-7.169448,0.728321,9.778094,7.578307,-1.191646,7.629069,-0.470563,1.179143,-5.711453],[-7.240903,-2.576849,-0.529102,6.805717,-8.901725,8.806911,2.666853,2.543952,5.435519,-5.895992,-0.773146,9.434037,-6.004083],[-3.369498,6.026627,8.723182,5.212411,-4.807874,-6.770750,7.814217,-6.178141,0.455017,-5.199583,7.111756,5.194209,-1.723925],[-5.551741,5.345605,4.874860,1.739282,-8.226998,-3.569966,-5.821393,0.575202,3.849229,7.182855,4.495320,5.601325,-5.507946],[8.548398,-2.922367,4.428784,-7.021977,-0.193598,-0.375623,-6.875893,-6.963203,-2.846320,9.617995,6.695445,6.254715,0.432810],[0.251208,-3.202656,8.478674,6.559654,-1.074096,-4.270403,8.493578,-0.781375,-2.131830,2.934954,-8.941228,9.332305,3.198892],[-0.230271,-3.002015,-0.955387,-2.989928,1.153533,-1.369315,1.481323,9.515176,2.715887,-8.685894,7.642556,-1.174047,1.311860],[-0.826001,0.336854,7.926289,-8.489548,5.114833,8.425251,-0.040929,8.390505,1.792021,1.959281,-0.418466,-0.954334,-1.959835]]], dtype = "float32")#candidate|2481|(4, 15, 13)|const|float32
uop_2482 = relay.atan(const_2481.astype('float32')) # shape=(4, 15, 13)
func_2297_call = mod.get_global_var('func_2297')
func_2300_call = mutated_mod.get_global_var('func_2300')
var_2494 = relay.var("var_2494", dtype = "float32", shape = ())#candidate|2494|()|var|float32
const_2495 = relay.const([6.966745,-2.282553,2.160601,-0.246981,-4.041518,-7.527669,-6.422243,-7.018949,-4.692703,-5.786838,-8.481997,-9.268822,4.714374,-0.143596,-5.102542,-6.986805,9.605542,-1.920514,1.144129,-9.460437,-9.682626,-2.001602,-6.995512,-0.427387,-0.058287,-8.081128,4.392762,1.249088,3.167152,7.273903,0.548385,9.230606,-4.316052,-4.377269,-2.145468,6.467525,1.921851,-2.722786,-1.725217,-5.715749,8.367734,9.028165,3.583084,-1.121828,-6.792582,6.463263,5.736084,5.263519,-3.287640,9.214077,-2.944068,0.710935,-9.797771,8.360976,1.092198,-0.976746,-1.875432,9.367951,-2.473399,2.983078,4.459320,4.661633,4.077531,7.849180,-9.975622,7.513329,1.165652,-5.387905,-5.837741,2.044398,-5.169335,-3.348063,4.825753,-7.558476,8.485418,9.644760,-3.343730,-7.571344,3.205368,9.107026,-8.128213,-4.173612,-3.803068,-3.266582,-0.004386,-3.169447,5.765092,5.937061,-8.696898,-7.037817,7.610466,-3.887120,-7.789654,-4.600766,-9.330090,3.300036,-8.135471,9.698062,1.735727,9.897995,9.761399,-8.765327,-2.916393,0.794731,9.721260,0.880962,2.805068,8.296046,-5.667398,5.191135,3.934843,3.302187,-4.946189,-7.755612,-9.327956,5.645354,0.395925,-6.240995,-6.433335,-5.325448,-2.267376,-9.098097,-9.526573,6.841951,0.016562,5.175934,-6.979508,-2.196827,2.507456,-0.337293,-1.118382,9.026315,2.230257,-7.014777,-4.812428,8.806106,-8.965606,-6.271744,4.350762,1.643450,5.260465,-6.693967,7.864494,-0.463151,9.235578,2.429059,7.273899,-8.507813,-3.974942,-4.538469,7.450462,9.697872,1.520955,-7.084115,-2.925910,-8.882100,9.813873,5.626811,6.263940,2.018982,-6.119972,9.090118,-6.344285,-0.222590,-9.722741,0.709292,-7.057188,3.998018,-2.594835,9.646220,2.686920,-3.298297,-9.791016,6.346903,-3.169545,-5.568007,6.603800,-5.155037,7.119134,3.148993,8.544909,-5.303687,7.580359,4.703871,1.491515,-1.317077,-0.801730,9.545025,-0.373291,7.022868,-3.089566,9.697542,8.350974,3.612324,-2.685893,-0.061686,0.964980,-6.345669,-7.032486,-9.278564,-6.985918,-4.040977,-6.325857,6.808370,-4.588946,1.128599,-0.381758,3.091977,-3.877221,2.564823,5.518973,-2.363077,-9.593593,3.574733,-8.475693,-2.925631,8.797639,-2.221483,6.599515,-6.740663], dtype = "float32")#candidate|2495|(220,)|const|float32
call_2493 = func_2297_call(relay.reshape(var_2494.astype('float32'), []), relay.reshape(const_2495.astype('float32'), [11, 5, 4]), )
call_2496 = func_2297_call(relay.reshape(var_2494.astype('float32'), []), relay.reshape(const_2495.astype('float32'), [11, 5, 4]), )
func_11_call = mod.get_global_var('func_11')
func_15_call = mutated_mod.get_global_var('func_15')
var_2502 = relay.var("var_2502", dtype = "uint16", shape = (225,))#candidate|2502|(225,)|var|uint16
const_2503 = relay.const([[6,10,-8,1,-4,-2,2,7,-1,5,-1,3,-6,-1,-6,4,9,-9,6,-7,-8,5,2,-1,7,9,3,-2,-2,6,3,9,3,9,9,-2,-6,6,-10,-1,3,5,-1,-8,3,8,-3,-6,-8,-10,2,3,-10,3,5,7,5,5,2,-6,7,-8,4,9,-10,8,-2,9,-1,-1,8,4,1,-7,3,5,9,8,-9,5,7,-1,-8,10,3,-4,9,-2,9,3,-3,10,4,-7,-7,10,10,5,-2,-5,-6,3,1,8,-5,10,9,-1,-9,6,5,-4,-7,-2,1,3,-10,-5,-2,-1,-3,-4,-2,-7,-7,9,-9,6,-1,7,8,1,6,9,8,4,10,6,-7,2,-6,-6,5,4,-10,8,-1,-8,-5,-5,-4,4,9,5,-5,-9,-10,-9,-7,-1,-2,-7,-9,1,1,-7,-7,6,-3,5,7,-2,-9,4,-1,-4,-5,7,-7,8,-6,-10,7,2,-8,9,-9,4,9,-5,-6,-5,-10,-5,-1,-3,-9,2,1,-6,-1,6,-6,-9,10,-7,-10,7,7,7,6,-6,4,-1,-2,-6,1,-2,-2,-4,-2,9,3,4,-10,7,4,3,3,-5,-8,-7,-2,-6,1,-5,10,7,-9,-5,-5,-9,8,-6,-5,-6,-3,3,-4,-8,-8,-10,-8,-2,-7,10,-1,-10,10,-10,9,7,10,9,-9,-1,-1,-5,-7,10,6,-7,-8,8,2,-2,-7,-7,10,-5,3,6,-6,-5,-10,6,-6,6,1,-3,-3,6,-5,-9,6,-2,9,-5,10,7,-8,9,7,9,1,-10,6,-6,-10,-3,-8,-7,6,-1,3,-10,10,-2,-5,6,-4,10,-2,-10,1,1,2,-6,8,-7,-3,2,6,-4,-7,-9,-5,-1,-7,-1,6,-8,8,9,1,-8,4,-2,6,-5,4,-1,5,8,-5,-2,3,-3,6,-8,9,3,-8,6,-9,-6,-5,4,1,3,2,-8,7,-5,-5,-10,-3,-8,8,-6,4,-1,-10,-10,6,-6,-1,3,-10,-1,-3,9,-5,-6,2,-3,-5,7,7,4,-3,2,-9,-1,3,-1,-4,2,-7,6,2,6,-4,-3,-2,-6,9,8,3,6,1,4,-10,-9,-7,-8,6,8,-9,-9,-8,-6,3,7,-1,-5,4,2,-8,-3,-7,5,7,1,4,6,7,1,4,-9],[4,-1,-5,-2,-5,-9,-8,-6,-8,10,1,8,-8,1,8,10,5,-10,-6,5,-9,-6,7,-1,-10,-10,9,-2,-6,2,2,8,5,10,-10,3,-7,6,10,10,-8,-5,-8,-5,-8,10,1,9,-6,7,2,-5,8,5,-9,-10,-7,6,-1,-2,10,-3,2,8,1,-3,-5,3,10,-3,-3,7,-9,-5,-6,1,3,-8,4,-4,-1,-9,9,-10,-10,-7,-8,-2,7,-7,-8,-8,2,7,-2,-2,-2,-9,-5,-10,-4,7,-3,-10,8,-3,8,9,-7,-8,1,-4,-3,4,4,2,-10,1,-9,4,-2,8,-8,10,5,-6,7,9,-3,-7,-6,-4,-9,-10,9,10,10,-1,-2,6,10,4,-4,-9,-4,3,-5,-6,5,5,-1,5,-2,4,1,1,-3,-1,8,3,6,1,4,-8,-7,-3,9,-2,8,4,7,3,2,5,3,3,-4,3,-6,-7,5,1,-9,4,10,-7,7,5,3,1,-9,-5,1,-1,10,-9,-7,2,5,3,6,-2,-7,2,8,6,-10,-10,-3,-9,8,-2,8,1,10,7,-4,-8,-8,3,-6,3,3,6,-4,-9,-2,-9,2,2,-4,9,9,-10,-10,3,3,-3,-1,10,-5,-10,-9,5,-9,-7,-9,-2,4,7,5,1,8,-4,-4,-6,3,-5,-7,8,-9,-10,1,-9,3,10,-6,8,8,4,-6,10,10,-6,6,-4,8,5,5,-6,-10,8,1,3,-8,1,1,5,-5,-8,-4,-7,-8,4,8,4,10,5,10,1,7,3,-3,9,7,10,2,4,2,3,-9,10,-1,-1,5,10,-5,-9,-9,-8,-8,10,8,9,-1,1,-1,1,10,-4,5,-8,-7,1,-7,-4,7,-4,7,6,8,-10,-10,1,-3,6,9,10,-3,1,10,-5,-1,-4,4,6,7,1,9,9,8,-1,9,2,4,4,-1,3,-9,10,-6,7,4,-3,1,6,5,-6,-1,-8,4,-1,2,6,-2,7,5,-3,2,-4,6,-2,-7,9,9,-5,1,7,-1,-5,1,2,7,-9,-1,-2,4,10,-6,-1,8,7,9,1,9,4,-1,8,-10,-7,-9,-10,4,-4,8,-5,-9,-6,-6,-10,-4,-3,-9,-2,-7,1,-7,6,-10,-4,-6,-7,-9,3,9,-8,-10,-9,-3,9],[8,-5,3,-10,2,3,1,2,2,-7,1,-3,10,9,3,-3,-1,7,10,5,9,1,-8,4,-10,-1,8,-3,8,-2,-1,-1,5,-6,-5,-10,-9,-8,6,6,-3,-9,1,-9,-4,-9,8,-9,9,-10,6,-3,-3,-1,3,4,-4,-6,3,-5,10,3,-3,-3,-10,9,4,-9,2,-3,9,10,-10,-8,4,1,-7,-4,-9,-5,9,-4,-5,-10,-5,2,10,-7,8,5,-7,8,1,4,-8,-10,2,-1,-9,4,4,7,-7,6,10,-9,-8,-10,-10,2,5,6,7,6,8,9,-7,-10,3,-10,-7,-1,-8,3,-7,-4,6,2,9,9,-2,-1,-9,3,-7,6,-4,7,7,-7,-7,-9,-3,8,2,9,-10,-3,1,2,9,-2,-2,-4,-10,-5,4,-2,6,-10,9,-10,-2,-7,-9,3,-6,2,3,-7,8,2,6,10,-3,-10,-2,3,-3,8,-9,3,-5,3,2,-3,-6,2,-8,-5,3,-5,-6,-8,9,5,7,5,-3,-2,-2,5,1,-9,-2,-1,-10,9,-7,6,-4,-5,-9,5,-1,-8,5,9,1,-6,-2,9,5,9,4,9,-8,-1,5,2,-6,-6,-4,-6,5,-9,8,1,3,-9,-7,8,-3,6,-6,3,-7,-10,6,-5,7,1,1,3,6,-4,8,-10,-1,-8,-3,9,-10,10,-7,10,-8,-1,7,-2,6,3,7,7,-10,-3,6,10,2,-5,-4,3,7,10,10,4,7,1,3,-2,-3,-3,-8,4,-4,7,3,1,-5,-4,4,-2,7,6,1,2,-4,10,1,-10,-4,-6,-10,-7,-7,-2,10,3,9,-7,9,2,-8,3,-10,-8,-3,-1,9,-8,10,-9,-5,-8,-6,-5,-8,-6,3,8,4,8,-10,8,1,-10,-7,-3,-3,-9,8,2,2,2,9,9,-10,9,-7,1,-5,1,10,-6,-5,-2,10,-6,-3,-8,-2,6,-5,2,-3,2,-4,2,6,-6,7,-1,3,-1,-10,1,-7,6,3,6,10,6,10,5,7,7,9,-1,7,-9,1,1,-8,-10,4,8,5,-8,-3,-2,-6,2,-9,8,-5,5,8,3,-10,8,10,-7,-2,-3,10,3,6,-9,-10,-3,5,-10,3,-10,8,-8,-6,5,-10,10,4,5,-3,-7,3,-8,7,3,1,2]], dtype = "uint16")#candidate|2503|(3, 450)|const|uint16
call_2501 = relay.TupleGetItem(func_11_call(relay.reshape(var_2502.astype('uint16'), [15, 15, 1]), relay.reshape(const_2503.astype('uint16'), [15, 15, 6]), ), 0)
call_2504 = relay.TupleGetItem(func_15_call(relay.reshape(var_2502.astype('uint16'), [15, 15, 1]), relay.reshape(const_2503.astype('uint16'), [15, 15, 6]), ), 0)
func_11_call = mod.get_global_var('func_11')
func_15_call = mutated_mod.get_global_var('func_15')
call_2515 = relay.TupleGetItem(func_11_call(relay.reshape(var_2502.astype('uint16'), [15, 15, 1]), relay.reshape(const_2503.astype('uint16'), [15, 15, 6]), ), 0)
call_2516 = relay.TupleGetItem(func_15_call(relay.reshape(var_2502.astype('uint16'), [15, 15, 1]), relay.reshape(const_2503.astype('uint16'), [15, 15, 6]), ), 0)
func_1009_call = mod.get_global_var('func_1009')
func_1013_call = mutated_mod.get_global_var('func_1013')
const_2547 = relay.const([True,False,False,False,True,False,False,True,True,False,False,False,True,False,True,False,True,True,False,False,False,True,True,False,True,True,False,False,True,False,False,False,False,False,True,True,False,True,True,True,True,True,False,False,True,True,False,False,True,False,False,True,True,False,True,False,True,True,True,False,True,True,False,True,True,True,True,True,False,False,False,True,True,False,True,True,False,False,True,True,False,False,False,False,False,True,False,True,True,True,True,False,False,True,False,True,True,True,False,True,True,True,True,False,True,False,True,True,False,True,False,True,True,False,True,True,False,True,False,True,True,True,True,True,False,True,True,True,False,True,True,True,False,False,False,False,False,True,True,True,False,False,False,True,False,True,False,False,False,False,True,True,True,True,True,False,False,False,True,True,True,False,False,False,False,False,False,True,False,True,False,False,True,False,False,False,True,False,False,True,True,False,True,False,True,False,False,True,False,False,False,True,False,True,True,True,True,True,False,True,True,False,False,False,False,False,False,True,False,True,False,True,True,True,False,False,True,False,True,True,False,False,True,True,True,False,False,False,False,False,False,True,False,False,True,False,False,False,True,False,True,True,False,False,True,False,False,False,False,True,False,True,True,True,False,False,True,False,True,True,False,True,False,False,True,False,False,True,False,True,True,True,False,True,True,True,True,True,False,False,False,False,True,False,True,True,False,False,True,True,False,True,False,False,True,True,False,True,False,False,False,False,True,False,True,False,False,True,True,False,True,False,False,False,False,True,True,False,True,False,False,True,True,False,False,False,False,False,True,False,True,True,False,False,True,False,True,True,True,False,True,False,False,True,False,False,False,True,True,False,True,True,True,False,True,True,False,True,False,True,False,True,False,False,True,True,False,False,True,True,True,False,True,True,False,True,False,False,False,True,False,True,False,False,True,True,True,True,True,True,False,True,False,False,True,False,False,False,False,True,True,True,True,True,True,True,False,True,False,True,False,False,False,False,False,False,True,False,True,False,True,False,True,False,False,True,False,False,True,False,True,False,False,True,True,True,False,False,False,False,True,False,True,True,False,True,True,True,True,True,False,True,True,True,True,True,False,True,False,True,True,True,False,True,False,True,False,True,True,False,True,False,False,False,False,False,False,True,False,True,False,False,False,True,True,True,True,False,False,True,True,False,False,True,True,True,True,False,False,False,False,True,True,True,False,True,True,False,False,True,True,True,True,False,False,True,True,True,True,False,False,False,False,True,False,True,False,True,True,False,True,False,True,False,True,True,True,False,True,False,False,True,True,True,True,True,False,False,True,True,False,True,False,False,False,False,False,False,True,True,False,False,True,False,True,False,True,False,True,True,False,True,False,True,False,True,True,True,True,False,False,False,True,False,False,False,False,False,False,True,False,True,False,True,True,True,False,False,True,True,True,False,False,True,True,False,False,False,True,False,False,False,False,False,False,False,False,True,True,False,False,True,True,False,False,False,True,False,True,True,True,False,True,True,False,False,False,False,True,True,False,True,True,False,True,False,True,True,True,False,False,True,True,True,False,True,False,True,False,True,False,True,True,True,True,True,False,True,False,True,False,False,False,False,True,False,False,False,True,True,False,True,False,True,True,False,False,True,False,False,False,False,False,True,False,True,True,False,False,True,True,False,True,True,False,False,True,False,False,True,True,False,False,False,True,True,False,False,False,False,False,False,True,False,False,True,True,True,True,True,False,False,False,True,True,False,False,True,True,False,False,False,True,False,False,False,False,True,False,False,True,True,True,False,True,True,True,True,False,False,False,False,False,False,True,False,True,True,True,False,False,True,False,True,True,True,True,True,False,False,False,True,True,True,False,False,False,True,True,False,False,False,False,False,False,True,False,True,True,True,True,True,False,False,False,False,True,True,True,True,True,True,False,False,False,False,True,False,False,False,False,False,False,False,False,True,False,True,False,True,False,False,False,True,False,False,True,True,True,False,False,True,False,False,True,False,True,False,True,True,True,True,True,True,False,True,False,False,False,True,True,True,True,True,False,True,True,True,False,False,True,False,True,True,False,True,False,True,True,True,False,False,False,True,False,False,True,False,False,True,True,True,False,False,False,False,True,True,True,True,False,True,True,True,False,False,False,False,True,False,True,False,False,False,True,False,False,False,True,True,False,False,False,False,True,True,True,False,False,False,False,False,True,True,False,False,True,False,False,True,False,False,True,True,False,False,True,False,True,False,True,True,True,False,True,False,True,False,False,True,True,False,False,False,False,False,False,True,False,True,False,True,True,True,False,True,False,True,True,True,False,True,False,True,True,True,True,False,False,True,True,True,False,True,True,False,True,False,True,False,True,False,True,False,True,True,True,True,False,False,False,False,True,False,True,False,False,False,False,False,False,False,True,False,True,False,False,True,False,True,True,True,True,False,True,True,True,False,False,True,True,True,False,False,True,True,True,True,False,True,True,False,True,False,False,True,True,False,False,True,True,True,True,True,True,False,False,False,True,False,True,False,True,True,False,True,True,True,False,True,True,False,True,False,False,True,True,True,True,True,True,False,False,False,True,True,False,True,True,True,False,True,True,True,False,False,False,True,True,True,False,False,True,True,True,True,False,False,True,True,False,False,False,False,False,True,False,False,True,True,False,True,False,True,False,True,True,True,False,True,False,True,True,True,False,False,False,True,True,True,False,True,True,False,True,True,False,True,False,True,True,False,False,True,True,False,False,True,True,True,False,True,False,True,False,False,False,True,True,True,False,False,False,False,False,True,True,False,True,True,True,False,True,True,True,True,False,False,False,True,True,False,True,True,True,True,True,True,False,True,False,True,True,False,True,True,False,False,False,True,False,True,True,True,True,False,False,True,False,False,False,True,False,True,False,False,True,False,True,True,True,False,False,False,False,True,True,False,False,True,True,False,True,False,True,False,True,False,True,True,False,True,True,True,True,True,True,False,True,False,True,False,False,False,False,True,True,False,True,True,True,True,True,False,True,True,False,False,True,True,False,True,True,True,False,False,False,True,False,False,False,True,False,False,True,True,True,True,True,True,False,False,False,False,True,True,True,True,False,False,True,False,True,False,True,False,False,True,True,False,True,True,True,False,False,True,True,True,False,False,False,False,False,False,False,True,False,True,True,False,True,False,False,True,False,True,True,False,False,False,False,False,False,True,False,False,False,True,True,False,True,False,True,True,False,True,True,False,True,False,False,False,False,False,True,False,True,False,False,False,True,False,False,True,True,False,True,False,True,False,False,False,False,True,True,True,True,False,True,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,True,False,True,False,False,True,False,False,False,True,True,True,True,True,True,True,True,False,True,True,False,True,False,True,True,True,True,True,False], dtype = "bool")#candidate|2547|(1456,)|const|bool
var_2548 = relay.var("var_2548", dtype = "float32", shape = (12, 1))#candidate|2548|(12, 1)|var|float32
call_2546 = relay.TupleGetItem(func_1009_call(relay.reshape(const_2547.astype('bool'), [7, 13, 16]), relay.reshape(const_2547.astype('bool'), [7, 13, 16]), relay.reshape(var_2548.astype('float32'), [12, 1]), ), 0)
call_2549 = relay.TupleGetItem(func_1013_call(relay.reshape(const_2547.astype('bool'), [7, 13, 16]), relay.reshape(const_2547.astype('bool'), [7, 13, 16]), relay.reshape(var_2548.astype('float32'), [12, 1]), ), 0)
func_1009_call = mod.get_global_var('func_1009')
func_1013_call = mutated_mod.get_global_var('func_1013')
call_2553 = relay.TupleGetItem(func_1009_call(relay.reshape(call_2546.astype('bool'), [7, 13, 16]), relay.reshape(const_2547.astype('bool'), [7, 13, 16]), relay.reshape(var_2548.astype('float32'), [12, 1]), ), 1)
call_2554 = relay.TupleGetItem(func_1013_call(relay.reshape(call_2546.astype('bool'), [7, 13, 16]), relay.reshape(const_2547.astype('bool'), [7, 13, 16]), relay.reshape(var_2548.astype('float32'), [12, 1]), ), 1)
func_349_call = mod.get_global_var('func_349')
func_354_call = mutated_mod.get_global_var('func_354')
var_2557 = relay.var("var_2557", dtype = "uint64", shape = (1320,))#candidate|2557|(1320,)|var|uint64
call_2556 = relay.TupleGetItem(func_349_call(relay.reshape(var_2557.astype('uint64'), [11, 12, 10]), relay.reshape(var_2557.astype('uint64'), [11, 12, 10]), relay.reshape(var_2502.astype('uint16'), [225,]), ), 1)
call_2558 = relay.TupleGetItem(func_354_call(relay.reshape(var_2557.astype('uint64'), [11, 12, 10]), relay.reshape(var_2557.astype('uint64'), [11, 12, 10]), relay.reshape(var_2502.astype('uint16'), [225,]), ), 1)
func_1009_call = mod.get_global_var('func_1009')
func_1013_call = mutated_mod.get_global_var('func_1013')
call_2577 = relay.TupleGetItem(func_1009_call(relay.reshape(const_2547.astype('bool'), [7, 13, 16]), relay.reshape(const_2547.astype('bool'), [7, 13, 16]), relay.reshape(var_2548.astype('float32'), [12, 1]), ), 3)
call_2578 = relay.TupleGetItem(func_1013_call(relay.reshape(const_2547.astype('bool'), [7, 13, 16]), relay.reshape(const_2547.astype('bool'), [7, 13, 16]), relay.reshape(var_2548.astype('float32'), [12, 1]), ), 3)
func_11_call = mod.get_global_var('func_11')
func_15_call = mutated_mod.get_global_var('func_15')
call_2580 = relay.TupleGetItem(func_11_call(relay.reshape(call_2577.astype('uint16'), [15, 15, 1]), relay.reshape(call_2553.astype('uint16'), [15, 15, 6]), ), 0)
call_2581 = relay.TupleGetItem(func_15_call(relay.reshape(call_2577.astype('uint16'), [15, 15, 1]), relay.reshape(call_2553.astype('uint16'), [15, 15, 6]), ), 0)
output = relay.Tuple([uop_2482,call_2493,var_2494,const_2495,call_2501,var_2502,const_2503,call_2515,call_2546,const_2547,var_2548,call_2553,call_2556,var_2557,call_2577,call_2580,])
output2 = relay.Tuple([uop_2482,call_2496,var_2494,const_2495,call_2504,var_2502,const_2503,call_2516,call_2549,const_2547,var_2548,call_2554,call_2558,var_2557,call_2578,call_2581,])
func_2582 = relay.Function([var_2494,var_2502,var_2548,var_2557,], output)
mod['func_2582'] = func_2582
mod = relay.transform.InferType()(mod)
mutated_mod['func_2582'] = func_2582
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2582_call = mutated_mod.get_global_var('func_2582')
var_2584 = relay.var("var_2584", dtype = "float32", shape = ())#candidate|2584|()|var|float32
var_2585 = relay.var("var_2585", dtype = "uint16", shape = (225,))#candidate|2585|(225,)|var|uint16
var_2586 = relay.var("var_2586", dtype = "float32", shape = (12, 1))#candidate|2586|(12, 1)|var|float32
var_2587 = relay.var("var_2587", dtype = "uint64", shape = (1320,))#candidate|2587|(1320,)|var|uint64
call_2583 = func_2582_call(var_2584,var_2585,var_2586,var_2587,)
output = call_2583
func_2588 = relay.Function([var_2584,var_2585,var_2586,var_2587,], output)
mutated_mod['func_2588'] = func_2588
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2813 = relay.var("var_2813", dtype = "int64", shape = (12, 13, 12))#candidate|2813|(12, 13, 12)|var|int64
var_2814 = relay.var("var_2814", dtype = "int64", shape = (12, 13, 12))#candidate|2814|(12, 13, 12)|var|int64
bop_2815 = relay.bitwise_or(var_2813.astype('int64'), relay.reshape(var_2814.astype('int64'), relay.shape_of(var_2813))) # shape=(12, 13, 12)
func_11_call = mod.get_global_var('func_11')
func_15_call = mutated_mod.get_global_var('func_15')
var_2847 = relay.var("var_2847", dtype = "uint16", shape = (225,))#candidate|2847|(225,)|var|uint16
const_2848 = relay.const([[7,-6,-6,3,-2,-7,-7,-2,7,3,-10,7,10,10,9,6,9,-9,4,5,6,5,-10,6,-4,-9,-7,-4,-2,-6,6,8,-6,2,-8,-8,-8,-2,9,8,-9,10,5,-3,-10,-9,3,-2,6,-8],[1,-1,-10,7,-10,-5,-6,-5,10,-6,-8,-7,-4,-9,2,-5,7,10,-8,7,6,9,8,10,3,-10,-3,-6,-5,7,4,10,7,-9,9,-7,1,-6,9,6,-6,-6,3,-7,-7,-6,4,4,-6,-8],[-2,-3,-10,-1,6,4,-4,-2,2,-5,-4,10,7,-1,9,-1,4,-2,-2,5,10,2,10,1,3,-1,-9,7,6,-10,-7,6,4,8,-10,-5,-2,6,-1,2,-7,1,3,-3,-5,-6,5,-6,9,-6],[-6,-1,8,-8,8,-2,-4,-10,-10,8,5,8,5,8,5,-4,5,-1,7,-1,-1,8,6,2,9,1,-5,4,10,-5,8,-10,-7,5,10,6,8,7,-4,-10,-1,8,10,8,-6,7,-2,-6,-7,10],[-6,9,2,10,4,-8,-2,3,-8,4,-3,7,-9,4,-3,-3,3,-7,-5,1,-6,6,-7,2,1,-1,-6,-4,1,-2,2,-5,5,-10,-8,2,3,-4,9,6,-3,-8,5,-5,-8,3,10,7,-10,8],[9,4,7,2,5,8,5,6,-6,8,-7,5,1,-5,-10,-10,2,-1,-3,7,-3,5,-10,1,1,-1,-2,-8,-8,-5,5,-7,9,-5,3,10,6,-5,6,2,5,8,10,10,6,-6,1,7,3,2],[-6,5,8,10,-6,-3,-8,10,-6,7,6,-4,-9,8,-3,-10,-5,-2,-5,-10,5,-3,6,-2,-4,4,-2,-10,9,3,-8,-10,-7,7,5,4,1,-4,1,-9,2,-6,4,-5,3,5,-10,6,9,9],[3,3,-1,2,2,-6,7,-1,7,3,4,3,5,1,-7,8,-6,-7,-10,6,10,-8,-3,9,-5,-3,-2,-4,8,-3,-6,6,-1,-8,1,3,-5,10,2,-1,10,7,-10,1,6,4,4,-3,-2,8],[-4,-7,-5,-10,-4,3,3,-8,-9,-1,-4,9,7,-6,3,-4,-6,10,6,8,1,6,9,8,-6,5,6,-7,-5,1,7,-9,-4,6,-8,-4,6,-2,-5,-5,1,-10,-3,7,-9,10,-4,3,-7,-10],[5,-4,3,6,-8,10,2,-6,6,-4,4,3,2,-7,-6,4,2,-2,5,4,10,5,-1,-6,-8,4,-4,-1,-4,5,-5,3,8,2,-5,9,10,7,6,-10,4,6,10,6,6,-6,-2,-10,-6,4],[-1,-9,6,6,-1,-6,-10,-5,-10,6,4,-8,-1,-9,-1,10,-5,-4,-7,2,-7,-3,3,-9,10,-10,7,5,6,-7,-6,-10,-6,-3,-5,10,-3,8,2,-10,3,1,8,10,-9,-1,-1,-7,5,1],[4,1,8,-5,7,5,3,-1,-1,5,7,-6,-8,7,-2,3,-2,3,-4,-10,-4,-4,-2,-8,-8,-4,2,1,-2,3,-9,-8,-3,-10,-1,-9,-9,2,7,-6,-6,10,-10,-7,-1,8,1,10,-9,10],[-5,5,-1,5,8,3,-10,1,3,-6,-10,-4,-10,-2,5,1,10,-3,-2,1,8,5,8,-1,3,5,10,4,-4,-1,10,-10,-7,-3,9,-10,-7,-6,10,-6,-5,-8,-2,6,-3,-6,6,-7,-9,3],[-4,7,-7,-8,2,-2,9,-3,4,-9,-4,-2,-3,5,-9,9,1,-9,-1,-7,-3,10,-3,-2,-2,-6,10,-9,6,4,-4,1,1,8,-6,-6,6,-10,-9,-5,-7,-9,8,-7,-4,2,-6,-7,-2,10],[10,7,-2,-4,-1,-3,-10,3,-10,6,3,-4,-10,7,-4,2,-1,-9,-7,-5,3,-9,10,-3,-4,6,7,-8,9,-3,-2,-6,-5,7,9,4,-4,5,5,-6,-8,-6,-10,-6,-10,3,-3,5,5,3],[8,6,-10,-5,10,2,2,5,-4,1,7,6,-3,1,6,4,3,3,-10,6,10,9,8,1,2,-6,6,-2,-6,8,9,6,-1,-5,9,-2,1,-8,5,1,-3,-8,-2,9,5,9,-9,-6,-6,-3],[4,4,9,4,-3,-3,3,-7,-4,-2,4,-3,-8,3,-3,9,-6,-5,-6,2,6,-6,-9,-4,9,-3,7,6,-6,9,7,-9,2,-9,2,8,9,7,-8,2,-6,8,1,-1,5,8,-8,7,10,-8],[9,10,-1,5,-9,7,-10,-1,1,1,1,-7,6,-1,-10,-9,-9,7,6,-9,7,-2,-3,9,4,7,9,6,-8,2,-10,-6,-9,-8,3,2,5,8,-7,-1,6,8,-2,1,-3,-7,-5,1,4,-3],[-7,8,10,-2,-2,10,1,-5,2,2,-10,-10,9,-9,9,1,-6,9,-6,3,-4,-6,-10,-7,-7,-2,5,2,-1,9,2,9,-1,-5,1,-5,-4,-9,3,9,-2,-7,-2,3,9,-7,-1,2,-5,9],[9,-3,6,-7,8,9,8,-9,4,-6,-1,5,-9,6,-5,2,-10,7,4,6,-2,2,-10,2,2,-6,-1,6,1,-4,8,2,-8,5,5,-4,4,-8,-8,8,-8,-2,9,-9,-2,9,-8,6,-2,-9],[-2,-7,-10,1,-5,9,-5,-6,-1,-5,9,-10,4,4,9,-6,-8,-7,8,-8,7,8,-8,-6,-1,-9,4,-9,7,8,-9,-7,5,-7,2,-6,3,-2,-10,10,-9,2,-10,4,4,-3,6,10,-4,4],[2,-4,6,4,4,5,-2,-9,-6,10,-4,-3,-3,-2,9,2,6,6,3,5,-3,1,9,-10,2,7,2,-6,2,-3,-4,4,-2,1,2,3,8,3,-5,-4,-2,4,-10,1,8,7,-9,-1,3,6],[-10,1,4,-7,4,5,4,-1,10,8,-6,-10,-8,-7,5,-4,-2,-2,6,5,-3,-9,-2,3,4,9,-8,6,4,-7,-7,-3,-6,5,-6,-6,-3,-8,-5,4,-2,-1,4,6,-1,6,-2,6,3,1],[-2,-10,2,-7,-7,-10,5,-9,9,8,6,7,-2,7,-4,7,-7,-8,-5,10,7,-2,9,5,7,-7,9,5,7,-9,2,7,-4,-10,2,-4,-8,-5,-10,-7,4,-3,10,-6,-10,9,2,-3,1,-7],[5,-3,-8,2,-7,-6,-4,5,7,-2,6,-10,7,5,1,10,5,-9,-2,-10,3,-1,5,3,-9,8,8,4,-3,3,2,10,-7,-10,-1,7,10,-2,-7,-8,10,10,6,-3,-4,5,-10,-3,3,5],[6,9,-3,1,-6,4,5,-5,-7,-1,7,-7,8,-5,3,-8,-3,5,8,5,6,-1,3,-1,-6,-3,8,-9,2,-1,3,6,-6,3,-8,9,8,-5,8,3,-10,-7,8,7,2,-5,-7,5,3,-7],[-6,6,-6,5,1,-8,-6,-1,2,4,-8,-1,3,8,3,8,-2,1,9,4,6,1,8,8,-10,6,-5,-10,-2,-4,-6,2,1,7,-1,-10,-4,3,-2,4,5,-9,4,9,-10,8,-9,3,6,-10]], dtype = "uint16")#candidate|2848|(27, 50)|const|uint16
call_2846 = relay.TupleGetItem(func_11_call(relay.reshape(var_2847.astype('uint16'), [15, 15, 1]), relay.reshape(const_2848.astype('uint16'), [15, 15, 6]), ), 0)
call_2849 = relay.TupleGetItem(func_15_call(relay.reshape(var_2847.astype('uint16'), [15, 15, 1]), relay.reshape(const_2848.astype('uint16'), [15, 15, 6]), ), 0)
output = relay.Tuple([bop_2815,call_2846,var_2847,const_2848,])
output2 = relay.Tuple([bop_2815,call_2849,var_2847,const_2848,])
func_2851 = relay.Function([var_2813,var_2814,var_2847,], output)
mod['func_2851'] = func_2851
mod = relay.transform.InferType()(mod)
var_2852 = relay.var("var_2852", dtype = "int64", shape = (12, 13, 12))#candidate|2852|(12, 13, 12)|var|int64
var_2853 = relay.var("var_2853", dtype = "int64", shape = (12, 13, 12))#candidate|2853|(12, 13, 12)|var|int64
var_2854 = relay.var("var_2854", dtype = "uint16", shape = (225,))#candidate|2854|(225,)|var|uint16
output = func_2851(var_2852,var_2853,var_2854,)
func_2855 = relay.Function([var_2852,var_2853,var_2854,], output)
mutated_mod['func_2855'] = func_2855
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3029 = relay.var("var_3029", dtype = "float32", shape = (16, 7, 4))#candidate|3029|(16, 7, 4)|var|float32
uop_3030 = relay.sqrt(var_3029.astype('float32')) # shape=(16, 7, 4)
output = uop_3030
output2 = uop_3030
func_3039 = relay.Function([var_3029,], output)
mod['func_3039'] = func_3039
mod = relay.transform.InferType()(mod)
var_3040 = relay.var("var_3040", dtype = "float32", shape = (16, 7, 4))#candidate|3040|(16, 7, 4)|var|float32
output = func_3039(var_3040)
func_3041 = relay.Function([var_3040], output)
mutated_mod['func_3041'] = func_3041
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3337 = relay.var("var_3337", dtype = "float64", shape = (10, 2, 2))#candidate|3337|(10, 2, 2)|var|float64
uop_3338 = relay.exp(var_3337.astype('float64')) # shape=(10, 2, 2)
output = relay.Tuple([uop_3338,])
output2 = relay.Tuple([uop_3338,])
func_3347 = relay.Function([var_3337,], output)
mod['func_3347'] = func_3347
mod = relay.transform.InferType()(mod)
mutated_mod['func_3347'] = func_3347
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3348 = relay.var("var_3348", dtype = "float64", shape = (10, 2, 2))#candidate|3348|(10, 2, 2)|var|float64
func_3347_call = mutated_mod.get_global_var('func_3347')
call_3349 = func_3347_call(var_3348)
output = call_3349
func_3350 = relay.Function([var_3348], output)
mutated_mod['func_3350'] = func_3350
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3663 = relay.const([[[2,-4],[-10,4],[4,-5],[2,6],[7,2],[-5,4],[-2,3],[-5,-4],[8,-4],[4,2],[5,-7],[-1,5],[-5,7],[-10,3],[5,7],[-9,-7]],[[-6,-5],[10,-8],[-5,1],[2,-3],[3,-8],[-10,-4],[-9,6],[-2,2],[5,-10],[-7,9],[-5,-9],[6,-5],[-9,-3],[-6,-5],[-10,2],[6,-1]],[[3,6],[-10,-5],[5,6],[-3,10],[6,4],[-2,8],[2,3],[-3,-6],[6,8],[7,4],[7,-3],[1,-4],[-9,-10],[7,-5],[7,4],[-2,6]],[[-4,-7],[8,-3],[1,5],[1,10],[8,-1],[9,2],[3,4],[8,-7],[-4,3],[4,-9],[2,-7],[-5,-3],[9,8],[1,4],[7,1],[-9,10]],[[-1,-7],[1,-1],[2,-7],[7,10],[5,5],[-7,2],[-8,3],[-1,1],[8,-8],[8,3],[9,8],[2,-1],[-5,5],[-3,10],[-7,-9],[6,2]],[[-1,-2],[-2,-8],[-6,7],[6,5],[2,5],[-6,-9],[10,3],[1,9],[-8,9],[-7,-10],[-5,1],[5,-3],[7,-6],[-7,-5],[-4,-2],[-4,5]],[[3,3],[-4,2],[-2,-1],[8,-5],[5,7],[-6,-8],[1,-5],[10,-8],[-7,10],[-3,-1],[5,1],[-9,10],[10,6],[10,-8],[2,5],[-5,-3]],[[-1,4],[-7,-9],[8,-8],[10,10],[5,-6],[8,5],[7,-1],[2,-7],[-9,9],[7,-10],[1,3],[-6,-1],[-9,-8],[-1,6],[-5,-2],[-3,2]],[[-7,9],[2,-10],[-9,-4],[4,-8],[2,-9],[-10,-1],[-5,4],[2,-3],[-8,3],[-4,-2],[-6,8],[4,2],[-3,-9],[9,10],[2,4],[-9,-3]],[[9,-4],[10,6],[4,7],[-3,2],[-1,10],[2,6],[3,10],[-6,8],[2,10],[10,10],[-3,2],[6,-1],[6,9],[-3,-1],[-4,10],[-5,-7]],[[2,1],[-7,-8],[7,-6],[1,-2],[-1,4],[-5,-10],[-8,-10],[1,-2],[-9,7],[-3,6],[-4,-3],[-10,-3],[-5,4],[-1,-10],[9,4],[9,4]],[[-6,-2],[7,-8],[-2,5],[5,2],[-4,9],[-3,6],[9,1],[-5,-6],[8,-1],[9,6],[-10,3],[9,-5],[-2,-10],[-5,6],[-6,4],[3,-4]],[[1,6],[5,-1],[-2,-2],[10,6],[4,-8],[2,-5],[-2,-10],[10,-6],[1,10],[3,-3],[-4,10],[6,7],[-1,1],[10,2],[2,8],[7,-2]],[[7,6],[-3,-7],[-6,2],[-2,-2],[-5,-8],[6,8],[-3,-1],[-4,1],[-4,3],[6,6],[-8,3],[-7,-5],[-9,-7],[5,6],[-6,10],[-1,1]]], dtype = "int64")#candidate|3663|(14, 16, 2)|const|int64
var_3664 = relay.var("var_3664", dtype = "int64", shape = (14, 16, 2))#candidate|3664|(14, 16, 2)|var|int64
bop_3665 = relay.less_equal(const_3663.astype('bool'), relay.reshape(var_3664.astype('bool'), relay.shape_of(const_3663))) # shape=(14, 16, 2)
func_2005_call = mod.get_global_var('func_2005')
func_2008_call = mutated_mod.get_global_var('func_2008')
var_3673 = relay.var("var_3673", dtype = "float64", shape = (300,))#candidate|3673|(300,)|var|float64
call_3672 = func_2005_call(relay.reshape(var_3673.astype('float64'), [5, 12, 5]))
call_3674 = func_2005_call(relay.reshape(var_3673.astype('float64'), [5, 12, 5]))
func_254_call = mod.get_global_var('func_254')
func_257_call = mutated_mod.get_global_var('func_257')
var_3678 = relay.var("var_3678", dtype = "float32", shape = (12,))#candidate|3678|(12,)|var|float32
var_3679 = relay.var("var_3679", dtype = "uint16", shape = (25, 9))#candidate|3679|(25, 9)|var|uint16
call_3677 = relay.TupleGetItem(func_254_call(relay.reshape(var_3678.astype('float32'), [1, 3, 4]), relay.reshape(var_3679.astype('uint16'), [225,]), ), 0)
call_3680 = relay.TupleGetItem(func_257_call(relay.reshape(var_3678.astype('float32'), [1, 3, 4]), relay.reshape(var_3679.astype('uint16'), [225,]), ), 0)
uop_3689 = relay.sin(var_3679.astype('float64')) # shape=(25, 9)
uop_3695 = relay.log(uop_3689.astype('float32')) # shape=(25, 9)
func_349_call = mod.get_global_var('func_349')
func_354_call = mutated_mod.get_global_var('func_354')
const_3698 = relay.const([7,-9,3,-9,-7,-6,5,4,-5,4,4,8,-9,1,-6,-2,-4,-8,-6,-1,-1,9,-8,-1,7,-7,-3,3,9,8,10,10,10,10,4,-1,10,-10,7,1,7,3,3,4,3,9,1,-9,7,8,-1,-6,-1,9,-6,-9,10,-2,9,-7,7,6,-3,-10,-4,-2,7,6,-4,5,-9,4,-8,4,-4,10,7,1,2,-2,8,-1,-2,3,4,-8,2,-4,-2,-8,1,8,-7,-8,8,7,-4,1,7,-3,-1,6,5,-6,10,3,-3,9,-10,8,7,-6,-4,-6,-2,-4,2,-10,1,3,-7,3,9,-9,9,7,-3,-6,1,-9,-2,9,2,10,3,-5,2,-2,9,8,-1,3,-1,2,-2,-6,-2,8,-4,7,2,2,7,-4,5,6,8,-1,-10,-10,2,7,-1,-9,-1,-4,6,8,-10,-10,6,-3,7,5,7,-10,-3,4,-9,-1,-7,7,3,-7,-10,1,4,2,8,-7,-3,3,-1,10,-7,-4,7,8,-9,-4,1,-6,-9,-6,-4,-3,9,2,2,2,2,6,1,1,8,-10,-1,5,3,-7,2,3,-8,3,-7,-1,-3,10,2,4,7,10,10,-5,7,-9,4,10,5,1,-8,-10,-1,7,-2,-5,6,-6,-1,9,-7,-6,-8,-2,-2,6,-7,-3,9,-2,-10,1,-2,-2,9,10,-8,6,5,-3,-3,6,-7,8,8,6,-7,-6,3,-4,1,-8,-2,-7,4,-3,8,5,-6,-1,3,4,4,10,10,-4,8,10,-8,-7,6,9,7,1,-7,10,10,1,-6,5,-3,-4,9,-10,-2,1,-5,4,-4,-9,-5,-2,-5,-1,4,-6,3,7,-6,10,4,-6,2,4,4,9,-2,-8,-4,7,-5,4,-5,-1,-7,-8,4,1,5,2,-9,-3,-1,-8,-8,-10,10,-10,-4,5,-3,4,1,5,-3,7,9,-4,9,-5,9,-1,-9,5,5,7,-4,-7,-10,-3,1,-6,-8,-1,4,-7,1,-3,10,-6,-7,2,7,6,-4,-2,-9,-5,1,-5,2,-10,-1,-3,-9,5,-3,-7,8,10,4,-1,2,-1,2,10,9,6,2,-10,-8,7,4,2,9,6,-3,6,2,8,5,-9,9,4,-3,-4,-9,-2,5,5,-7,-9,7,-6,5,5,6,-4,-9,6,-3,5,-1,3,5,2,-8,-2,10,-3,4,7,-4,-2,-9,9,1,2,-2,-8,2,9,-2,-2,-9,-9,7,-2,7,5,4,-8,7,5,-4,8,-4,3,-10,-10,3,1,-5,10,6,-8,9,-7,7,-10,6,6,-5,-8,7,3,7,-10,8,6,5,-6,9,3,-5,6,10,-1,-4,-9,9,1,-7,-10,-10,9,-8,2,-8,5,7,-5,5,2,-7,10,-5,1,1,7,6,9,-2,-5,-3,4,-2,-6,6,-6,-9,8,5,-5,1,-8,-1,4,7,4,10,1,-8,8,-3,9,-9,5,6,-2,4,-5,8,-8,7,-4,-1,-8,10,-5,10,-4,-10,-5,-10,3,-7,-1,-8,-10,3,1,-9,-5,4,-3,-5,-3,7,-3,-5,3,7,-8,2,-9,4,-1,10,3,5,10,2,-6,1,7,6,-1,3,5,9,-2,-5,-5,6,-10,-3,-2,-4,-5,-6,5,2,2,-5,-3,-2,-5,-6,3,-10,7,-3,-10,7,-6,-10,6,6,9,6,4,-7,-6,-3,8,-4,-5,-4,-6,2,4,4,6,-8,1,-9,4,6,-10,3,-2,-3,-3,-4,7,-4,8,3,-6,-10,-8,2,4,4,-8,-4,-3,7,-5,7,-7,-5,9,-8,10,1,-5,-10,2,-7,-10,-9,9,10,-9,5,8,-8,9,-1,3,5,-5,-1,8,7,10,-4,4,-4,-1,-6,1,7,1,7,9,2,-8,3,10,5,-6,8,2,-4,10,-3,5,9,7,-9,-9,-10,-3,-2,-3,-2,7,-2,1,4,-5,2,-5,7,8,-8,-9,3,-3,7,-5,6,1,3,-1,5,1,9,10,-10,4,-7,-6,8,-9,-5,6,-6,-9,-10,5,-8,5,-4,5,-3,-2,5,3,9,-8,4,-8,-2,-1,-9,10,-5,-7,9,-5,-3,3,6,1,7,2,3,6,-8,10,5,5,2,-1,5,3,2,8,-3,-1,-8,4,2,-9,-6,8,-8,3,6,-10,7,-1,-1,-5,7,7,-1,-1,2,5,-8,1,-7,-5,-6,4,-10,4,-3,10,-9,9,9,-4,9,-2,4,10,-8,2,2,9,2,-5,-4,-7,3,2,-6,-6,-8,2,10,1,9,-3,-3,2,8,10,-4,5,-5,-3,5,-7,-6,3,3,5,1,-2,10,8,3,2,-7,9,5,-6,-9,-3,4,-10,-2,-8,3,-7,-3,-3,-5,6,-3,5,-6,10,5,-10,-9,-3,-5,6,-10,3,10,-2,2,-8,-2,2,-5,3,6,-7,4,-8,3,-9,8,8,9,-4,7,-7,-6,-9,1,-9,5,-4,7,8,-7,-5,-10,-5,-5,3,1,-1,8,8,-1,-6,4,-5,-3,3,1,-7,4,-3,2,-9,3,10,1,1,-4,10,9,10,-8,2,-4,-2,10,7,9,-7,-7,4,-4,4,1,9,-9,2,4,9,-10,8,8,3,1,-2,6,8,2,-9,4,-3,-7,-2,-8,10,-4,1,2,-1,-4,1,8,2,-1,-3,1,10,2,10,3,-9,8,10,3,-3,4,-9,-5,-2,-3,3,-4,3,-5,7,5,-6,3,-5,7,3,5,-4,4,7,3,-3,-3,5,3,5,-6,-3,8,7,-7,7,-4,-2,-8,-6,-9,10,-7,-7,6,10,-6,3,10,-9,10,-1,-8,-3,-4,-1,-9,-4,-7,9,-4,5,2,3,-6,3,10,-10,-6,9,3,-2,1,1,8,3,-10,3,-6,6,-9,-10,10,1,5,8,8,-2,-8,8,2,-8,-10,4,7,2,6,7,3,6,6,8,5,-6,1,-9,-5,-7,7,-5,-3,2,-8,-7,-9,-9,-6,10,6,-2,-9,-2,-9,-3,2,3,-2,5,6,-1,3,-1,-8,10,-8,-1,-3,-3,-3,1,4,-1,8,8,-5,10,-2,9,-1,-4,-1,-8,-7,9,9,5,3,-4,1,-5,-3,-8,-6,-5,-6,-8,3,3,8,1,-3,5,-4,5,10,-4,4,8,-9,-7,-9,1,-10,3,8,7,2,-5,10,-2,1,1,-7,5,1,10,6,3,8,6,-2,9,-7,-10,6,7,-7,-3,9,-10,-10,2,4,4,1,-7,-4,-7,-3,-8,-1,8,-3,-4,-9,-3,-7,-4,10,2,-7,6,-7,4,2,-9,-9,10,-8,-6,-1,7,-4,8,1,7,8,1,8,5,9,2,-1,-2,9,5,7,-7,-2,-6,2,3,7,-5,-9,-3,-4,-10,9,3,10,-7,1,1,-8,8,-8,-2,-5,8,-7,4,-9,-8], dtype = "uint64")#candidate|3698|(1320,)|const|uint64
call_3697 = relay.TupleGetItem(func_349_call(relay.reshape(const_3698.astype('uint64'), [11, 12, 10]), relay.reshape(const_3698.astype('uint64'), [11, 12, 10]), relay.reshape(var_3679.astype('uint16'), [225,]), ), 0)
call_3699 = relay.TupleGetItem(func_354_call(relay.reshape(const_3698.astype('uint64'), [11, 12, 10]), relay.reshape(const_3698.astype('uint64'), [11, 12, 10]), relay.reshape(var_3679.astype('uint16'), [225,]), ), 0)
output = relay.Tuple([bop_3665,call_3672,var_3673,call_3677,var_3678,uop_3695,call_3697,const_3698,])
output2 = relay.Tuple([bop_3665,call_3674,var_3673,call_3680,var_3678,uop_3695,call_3699,const_3698,])
func_3702 = relay.Function([var_3664,var_3673,var_3678,var_3679,], output)
mod['func_3702'] = func_3702
mod = relay.transform.InferType()(mod)
var_3703 = relay.var("var_3703", dtype = "int64", shape = (14, 16, 2))#candidate|3703|(14, 16, 2)|var|int64
var_3704 = relay.var("var_3704", dtype = "float64", shape = (300,))#candidate|3704|(300,)|var|float64
var_3705 = relay.var("var_3705", dtype = "float32", shape = (12,))#candidate|3705|(12,)|var|float32
var_3706 = relay.var("var_3706", dtype = "uint16", shape = (25, 9))#candidate|3706|(25, 9)|var|uint16
output = func_3702(var_3703,var_3704,var_3705,var_3706,)
func_3707 = relay.Function([var_3703,var_3704,var_3705,var_3706,], output)
mutated_mod['func_3707'] = func_3707
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4394 = relay.var("var_4394", dtype = "int8", shape = (1, 6, 4))#candidate|4394|(1, 6, 4)|var|int8
const_4395 = relay.const([[[-4,8,3,2],[3,-7,-6,3],[8,-8,-4,-2],[-3,1,1,-1],[-8,-5,-2,-2],[-9,-6,-5,-8]],[[-8,7,1,-7],[8,4,-10,6],[-5,-1,-10,-1],[-10,-3,-10,8],[-7,-2,-4,-5],[-4,2,3,4]],[[-9,-6,-5,-7],[6,2,10,5],[-4,-8,-3,1],[-1,3,-2,-5],[-1,-9,9,-1],[-7,2,2,-7]],[[-4,7,9,9],[10,5,1,5],[10,-6,2,-4],[2,-8,-5,3],[1,7,7,-1],[7,10,-5,-8]],[[9,-4,5,1],[5,-2,-4,8],[-6,-9,-2,-1],[-6,7,-6,-6],[2,7,9,-3],[-7,5,-3,-1]],[[1,-1,10,-1],[4,8,6,-6],[-8,-6,-3,3],[7,5,2,-8],[-6,5,-2,2],[8,-8,8,5]],[[-7,2,9,1],[-3,5,-2,8],[1,-4,4,8],[8,8,-8,-9],[-1,6,-6,7],[3,5,-4,-3]]], dtype = "int8")#candidate|4395|(7, 6, 4)|const|int8
bop_4396 = relay.greater_equal(var_4394.astype('bool'), const_4395.astype('bool')) # shape=(7, 6, 4)
output = bop_4396
output2 = bop_4396
func_4399 = relay.Function([var_4394,], output)
mod['func_4399'] = func_4399
mod = relay.transform.InferType()(mod)
mutated_mod['func_4399'] = func_4399
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4400 = relay.var("var_4400", dtype = "int8", shape = (1, 6, 4))#candidate|4400|(1, 6, 4)|var|int8
func_4399_call = mutated_mod.get_global_var('func_4399')
call_4401 = func_4399_call(var_4400)
output = call_4401
func_4402 = relay.Function([var_4400], output)
mutated_mod['func_4402'] = func_4402
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4528 = relay.var("var_4528", dtype = "float64", shape = (3, 2, 1))#candidate|4528|(3, 2, 1)|var|float64
uop_4529 = relay.asin(var_4528.astype('float64')) # shape=(3, 2, 1)
func_3347_call = mod.get_global_var('func_3347')
func_3350_call = mutated_mod.get_global_var('func_3350')
var_4541 = relay.var("var_4541", dtype = "float64", shape = (40,))#candidate|4541|(40,)|var|float64
call_4540 = relay.TupleGetItem(func_3347_call(relay.reshape(var_4541.astype('float64'), [10, 2, 2])), 0)
call_4542 = relay.TupleGetItem(func_3350_call(relay.reshape(var_4541.astype('float64'), [10, 2, 2])), 0)
func_2005_call = mod.get_global_var('func_2005')
func_2008_call = mutated_mod.get_global_var('func_2008')
const_4549 = relay.const([[7.555778],[9.760925],[8.770317],[-0.044538],[-4.552987],[5.569171],[-8.254868],[-7.762352],[-1.274667],[-4.958261],[6.191105],[-2.479457],[7.490331],[-9.557497],[-9.454213],[-4.684576],[-2.359869],[-5.106679],[-5.317597],[2.341746],[-4.925490],[3.285328],[-1.863314],[0.368763],[6.249764],[0.050418],[-6.902924],[6.440771],[0.312038],[6.993039],[-6.837938],[8.809758],[6.917673],[-5.701533],[2.342876],[-6.391921],[1.944780],[-7.148152],[2.873621],[-0.127057],[3.105377],[-6.140007],[7.474470],[9.179311],[7.544329],[-4.436179],[-2.349388],[-7.479781],[-1.367930],[3.472756],[-4.741539],[2.803510],[-4.730656],[3.972905],[2.181194],[-0.676604],[-3.438677],[-1.203481],[-8.962376],[-5.560163],[-2.852499],[-1.304371],[5.397024],[1.262996],[6.505450],[2.539859],[-9.675939],[2.056387],[-6.681195],[2.153674],[-5.301957],[-7.092098],[-0.383879],[-1.076359],[-0.954804],[-8.644735],[-0.682857],[5.208825],[-4.894076],[1.759999],[2.174721],[3.472001],[3.701838],[-1.255701],[-9.279807],[-1.970041],[0.122026],[6.982665],[8.296253],[7.408827],[-3.253522],[6.005773],[-9.444613],[-4.348491],[2.527428],[-6.467345],[-1.846402],[-2.889140],[8.816441],[0.919811],[-3.496802],[-2.172093],[-3.811805],[2.617592],[-9.859615],[4.480225],[7.857004],[8.500314],[9.004333],[-1.279988],[4.240670],[-0.142870],[-8.953915],[4.127214],[2.842225],[8.539841],[-8.613660],[-4.129209],[3.367977],[0.634981],[-2.613310],[4.998836],[4.164562],[4.050569],[-8.735770],[9.591923],[-7.025999],[-1.791594],[-2.604261],[-6.057008],[-1.812465],[-4.659691],[-2.780575],[-9.381086],[-9.766228],[5.646496],[-2.280856],[-9.444164],[6.155647],[0.553022],[4.084264],[1.982553],[-2.015240],[1.109327],[0.474172],[-2.670447],[6.662300],[3.445106],[1.531109],[-8.132414],[8.918807],[-7.704525],[-7.383140],[9.053887],[-5.615969],[3.108957],[0.354904],[-1.516426],[-1.276852],[-0.420932],[1.037771],[-0.954054],[2.245490],[-0.796948],[7.026661],[4.003245],[-9.956235],[-3.697621],[-2.217452],[-8.480466],[-4.450735],[7.577155],[-5.066475],[6.181839],[9.812486],[0.820250],[9.789589],[9.320157],[6.533580],[5.346941],[-0.112752],[3.188772],[3.513276],[9.028528],[6.869459],[-3.893907],[-4.289698],[2.614576],[9.135477],[3.284486],[-6.359024],[-0.556935],[-3.794371],[4.184284],[2.176743],[-2.783444],[7.454710],[1.959703],[-7.630553],[-0.815589],[-8.734830],[8.400676],[-0.010064],[-9.707498],[-0.768167],[-3.797723],[-1.603665],[-6.059741],[9.791228],[-7.950539],[-2.540591],[-6.179140],[-5.189667],[-3.933159],[4.092168],[-6.322391],[-4.454550],[-2.027538],[-5.133655],[-8.283330],[-4.161382],[6.517771],[2.992113],[-7.046890],[7.284390],[-6.022868],[1.193781],[9.098480],[-0.822102],[-8.721833],[2.753714],[3.563758],[6.065355],[-2.477684],[-4.028014],[-3.101064],[-2.883249],[5.103671],[4.313327],[-7.889070],[-4.057993],[-0.115485],[2.321222],[4.525725],[-7.853125],[4.129503],[-1.468506],[2.075826],[-3.900190],[1.791429],[-2.072326],[-1.050747],[-4.303150],[0.531126],[4.206268],[-6.896246],[-8.606618],[2.962355],[0.545872],[6.828948],[8.768087],[4.586487],[2.576154],[5.903767],[-6.910442],[1.332220],[-5.402366],[1.154354],[1.550757],[-3.699726],[-3.839638],[9.904325],[4.425405],[8.546580],[5.700924],[-0.498378],[7.277121],[4.079537],[-1.179719],[7.926890],[3.252029],[-9.657646],[-8.665439],[-1.396444],[-6.106336],[-8.170739],[-1.796307],[3.009386],[-0.469238],[-0.018943],[3.771113],[-2.112957],[-8.785590],[0.020797],[-5.363927],[2.489563],[4.390040],[1.293916],[-2.198506],[-9.541563]], dtype = "float64")#candidate|4549|(300, 1)|const|float64
call_4548 = func_2005_call(relay.reshape(const_4549.astype('float64'), [5, 12, 5]))
call_4550 = func_2005_call(relay.reshape(const_4549.astype('float64'), [5, 12, 5]))
func_2297_call = mod.get_global_var('func_2297')
func_2300_call = mutated_mod.get_global_var('func_2300')
var_4553 = relay.var("var_4553", dtype = "float32", shape = ())#candidate|4553|()|var|float32
var_4554 = relay.var("var_4554", dtype = "float32", shape = (220,))#candidate|4554|(220,)|var|float32
call_4552 = func_2297_call(relay.reshape(var_4553.astype('float32'), []), relay.reshape(var_4554.astype('float32'), [11, 5, 4]), )
call_4555 = func_2297_call(relay.reshape(var_4553.astype('float32'), []), relay.reshape(var_4554.astype('float32'), [11, 5, 4]), )
func_3347_call = mod.get_global_var('func_3347')
func_3350_call = mutated_mod.get_global_var('func_3350')
call_4574 = relay.TupleGetItem(func_3347_call(relay.reshape(call_4540.astype('float64'), [10, 2, 2])), 0)
call_4575 = relay.TupleGetItem(func_3350_call(relay.reshape(call_4540.astype('float64'), [10, 2, 2])), 0)
bop_4581 = relay.floor_divide(uop_4529.astype('float32'), var_4553.astype('float32')) # shape=(3, 2, 1)
func_2582_call = mod.get_global_var('func_2582')
func_2588_call = mutated_mod.get_global_var('func_2588')
const_4588 = relay.const([-5,-1,-7,-7,-3,-1,-10,-2,-1,6,-10,-3,3,-4,-10,9,8,-10,-1,4,-7,10,-1,2,9,-1,5,1,6,10,-6,1,-9,1,-2,-5,1,6,8,-6,-6,-5,-1,-10,6,2,1,6,-8,1,3,9,-1,-7,-3,-5,-10,-3,-7,-9,-2,-4,8,-2,-10,-8,-9,8,2,-9,10,5,4,-2,-10,5,4,3,-1,8,-8,-4,-3,-6,-10,1,1,-10,3,-10,-3,-5,6,8,-2,9,-5,4,-7,-5,9,9,-2,-7,-2,-10,-3,3,2,7,10,-2,10,2,-10,8,-3,-9,7,3,-4,4,7,-7,1,-3,-1,-5,-4,-10,-6,-4,-5,-5,9,-2,3,8,-5,1,8,-6,-2,10,10,2,10,4,-7,10,8,-6,-9,-1,1,4,-7,-8,3,-6,-10,8,2,-7,-4,-4,-8,3,9,6,7,9,10,6,-7,-6,-1,-9,8,-6,3,-5,2,-2,2,-9,6,7,-7,-9,5,3,10,1,-10,-10,-6,-5,3,-9,5,-5,8,-7,5,9,-1,-8,-4,9,-7,-8,6,-3,-1,5,4,7,4,-9,1,-10,10,-1,8], dtype = "uint16")#candidate|4588|(225,)|const|uint16
var_4589 = relay.var("var_4589", dtype = "float32", shape = (6, 2))#candidate|4589|(6, 2)|var|float32
var_4590 = relay.var("var_4590", dtype = "uint64", shape = (1320,))#candidate|4590|(1320,)|var|uint64
call_4587 = relay.TupleGetItem(func_2582_call(relay.reshape(var_4553.astype('float32'), []), relay.reshape(const_4588.astype('uint16'), [225,]), relay.reshape(var_4589.astype('float32'), [12, 1]), relay.reshape(var_4590.astype('uint64'), [1320,]), ), 5)
call_4591 = relay.TupleGetItem(func_2588_call(relay.reshape(var_4553.astype('float32'), []), relay.reshape(const_4588.astype('uint16'), [225,]), relay.reshape(var_4589.astype('float32'), [12, 1]), relay.reshape(var_4590.astype('uint64'), [1320,]), ), 5)
output = relay.Tuple([call_4540,var_4541,call_4548,const_4549,call_4552,var_4554,call_4574,bop_4581,call_4587,const_4588,var_4589,var_4590,])
output2 = relay.Tuple([call_4542,var_4541,call_4550,const_4549,call_4555,var_4554,call_4575,bop_4581,call_4591,const_4588,var_4589,var_4590,])
func_4602 = relay.Function([var_4528,var_4541,var_4553,var_4554,var_4589,var_4590,], output)
mod['func_4602'] = func_4602
mod = relay.transform.InferType()(mod)
var_4603 = relay.var("var_4603", dtype = "float64", shape = (3, 2, 1))#candidate|4603|(3, 2, 1)|var|float64
var_4604 = relay.var("var_4604", dtype = "float64", shape = (40,))#candidate|4604|(40,)|var|float64
var_4605 = relay.var("var_4605", dtype = "float32", shape = ())#candidate|4605|()|var|float32
var_4606 = relay.var("var_4606", dtype = "float32", shape = (220,))#candidate|4606|(220,)|var|float32
var_4607 = relay.var("var_4607", dtype = "float32", shape = (6, 2))#candidate|4607|(6, 2)|var|float32
var_4608 = relay.var("var_4608", dtype = "uint64", shape = (1320,))#candidate|4608|(1320,)|var|uint64
output = func_4602(var_4603,var_4604,var_4605,var_4606,var_4607,var_4608,)
func_4609 = relay.Function([var_4603,var_4604,var_4605,var_4606,var_4607,var_4608,], output)
mutated_mod['func_4609'] = func_4609
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5024 = relay.var("var_5024", dtype = "float32", shape = (12, 2, 11))#candidate|5024|(12, 2, 11)|var|float32
uop_5025 = relay.asinh(var_5024.astype('float32')) # shape=(12, 2, 11)
func_2005_call = mod.get_global_var('func_2005')
func_2008_call = mutated_mod.get_global_var('func_2008')
var_5028 = relay.var("var_5028", dtype = "float64", shape = (300,))#candidate|5028|(300,)|var|float64
call_5027 = func_2005_call(relay.reshape(var_5028.astype('float64'), [5, 12, 5]))
call_5029 = func_2005_call(relay.reshape(var_5028.astype('float64'), [5, 12, 5]))
uop_5034 = relay.sin(uop_5025.astype('float32')) # shape=(12, 2, 11)
func_3702_call = mod.get_global_var('func_3702')
func_3707_call = mutated_mod.get_global_var('func_3707')
var_5055 = relay.var("var_5055", dtype = "int64", shape = (224, 2))#candidate|5055|(224, 2)|var|int64
const_5056 = relay.const([-7.344560,-1.392070,0.991872,4.234450,-9.916065,-3.955296,0.858627,1.038283,-6.340999,-1.643893,1.861355,0.412988], dtype = "float32")#candidate|5056|(12,)|const|float32
const_5057 = relay.const([-8,-7,-10,-3,7,-6,-6,3,6,-2,5,7,-3,2,-6,3,5,-4,-4,-7,-7,-6,-7,-6,-2,-1,2,8,10,1,-6,-10,4,-5,3,9,-4,-2,-6,5,1,-5,-3,-10,3,-7,-8,2,-4,-10,1,-8,-6,8,-9,10,-9,2,-9,3,6,3,-10,5,5,3,-9,-3,-9,7,-5,9,1,6,-6,4,-10,7,3,5,1,6,-9,3,1,8,-6,-10,10,8,4,7,8,-7,8,-1,-10,-9,7,8,1,-5,-5,-5,-2,9,5,-3,4,6,-2,10,-5,10,10,-3,4,-9,5,-1,9,7,10,8,10,7,-10,-3,-8,10,-2,1,1,6,6,-6,-1,-10,3,-6,-2,4,-10,1,-3,-7,2,-3,-10,2,6,2,1,8,-9,-6,7,-5,8,-6,4,5,3,-2,7,-10,4,-10,-5,-10,5,7,7,-9,-7,5,10,1,2,-4,-7,-3,8,7,-4,-8,-2,-8,-7,3,4,7,-2,7,2,-2,-6,10,-8,7,-4,8,-10,-3,7,-2,6,5,8,1,-3,-8,5,5,7,-5,7,-4,-2,-5,-5,-10,-6,10,-6], dtype = "uint16")#candidate|5057|(225,)|const|uint16
call_5054 = relay.TupleGetItem(func_3702_call(relay.reshape(var_5055.astype('int64'), [14, 16, 2]), relay.reshape(call_5027.astype('float64'), [300,]), relay.reshape(const_5056.astype('float32'), [12,]), relay.reshape(const_5057.astype('uint16'), [25, 9]), ), 6)
call_5058 = relay.TupleGetItem(func_3707_call(relay.reshape(var_5055.astype('int64'), [14, 16, 2]), relay.reshape(call_5027.astype('float64'), [300,]), relay.reshape(const_5056.astype('float32'), [12,]), relay.reshape(const_5057.astype('uint16'), [25, 9]), ), 6)
func_1009_call = mod.get_global_var('func_1009')
func_1013_call = mutated_mod.get_global_var('func_1013')
const_5065 = relay.const([[False,False,False,True,True,False,True,False,True,True,True,True,True,True,True,True,False,True,False,False,False,False,False,True,False,False,True,True,False,True,True,False,True,True,False,False,True,True,False,False,True,False,True,False,True,True,True,True,False,True,True,True,True,False,False,False,False,False,True,False,True,False,False,False,True,False,False,True,False,True,True,True,True,True,True,False,False,True,True,False,False,True,True,False,True,False,False,True,False,True,True,True,False,True,True,True,False,True,False,False,False,False,True,True,True,False,True,True,True,True,True,False,False,True,False,True,True,False,False,True,True,True,False,True,False,True,True,False,False,True,False,True,True,True,False,False,False,False,True,True,True,True,True,True,False,True,False,True,True,False,False,True,True,False,False,True,True,True,False,True,True,False,False,False,False,True,True,False,True,False,True,False,True,True,True,True,False,True,False,False,True,False,True,False,False,True,True,True,True,True,True,False,False,True,False,False,False,True,False,True,False,True,True,True,False,False,True,True,True,True,True,False,False,False,False,False,True,False,False,False,True,True,False,True,False,True,True,True,False,True,False,False,True,False,False,True,False,True,False,False,False,True,False,False,True,True,True,True,True,True,True,False,False,False,False,False,True,True,True,True,True,False,False,False,False,False,True,False,True,False,False,True,True,True,False,True,False,True,False,True,False,True,True,False,True,True,False,False,True,False,False,False,False,False,False,False,False,True,False,True,True,True,False,True,False,False,False,False,True,False,True,True,True,False,True,True,False,False,True,True,False,True,True,False,True,True,False,True,False,False,False,False,True,True,True,True,True,True,True,True,True,False,False,False,True,False,True,True,False,True,False,False,False,True,False,False,False,False,True,False,False,False,False,False],[True,True,True,False,False,True,True,True,True,False,False,False,False,True,True,False,False,True,False,True,False,False,True,False,False,False,True,False,False,True,False,True,True,False,False,True,True,True,True,False,True,True,True,True,False,False,True,True,False,True,False,False,True,True,True,True,True,False,False,False,True,False,True,False,False,True,False,True,True,True,False,False,False,True,False,False,True,True,True,True,True,True,False,False,False,True,False,False,True,False,False,False,False,True,True,True,True,True,False,False,False,False,False,False,True,False,False,True,False,False,False,True,True,False,True,False,True,True,False,False,True,False,True,False,True,False,True,False,True,True,False,True,False,True,True,True,True,True,False,True,True,True,False,True,True,False,True,True,True,True,True,True,True,False,True,False,False,False,True,True,True,True,False,True,False,True,True,False,True,True,True,False,False,False,True,False,False,False,True,True,True,False,False,False,True,True,True,True,True,False,True,True,True,True,False,False,True,True,False,False,True,True,False,True,True,False,True,True,False,False,True,False,True,True,False,False,True,True,True,False,True,False,True,True,False,False,True,True,True,True,True,False,False,True,False,False,True,True,True,False,False,False,False,True,False,False,True,True,False,False,True,True,True,True,False,True,True,True,False,False,False,True,True,True,False,True,True,False,False,False,False,False,True,False,True,True,False,False,False,False,True,True,False,False,False,False,True,True,False,True,False,False,False,True,True,False,False,False,False,False,True,False,True,False,False,False,True,True,True,True,True,False,False,True,False,True,False,True,False,False,False,False,False,False,True,False,False,True,False,True,False,True,True,True,True,False,True,False,True,False,True,False,False,False,False,False,True,False,True,True,False,True,False,False,True,True,False,False,True,True,True,True,False,False],[False,False,False,True,False,True,False,False,False,False,False,False,True,True,False,False,False,False,False,False,False,True,False,True,True,True,False,False,False,False,True,False,False,True,True,True,True,True,True,True,False,True,True,True,False,True,True,False,True,True,True,True,True,True,False,False,False,False,True,False,True,False,False,True,True,True,False,False,True,True,True,True,False,False,False,False,True,True,True,False,True,False,False,False,True,False,False,True,True,True,True,False,True,True,True,True,False,False,True,True,True,True,False,False,True,False,False,True,False,True,True,True,True,True,True,False,False,True,True,True,True,False,True,False,True,False,True,False,False,True,True,False,False,False,False,True,False,False,False,False,False,False,True,True,True,False,False,True,False,True,False,True,False,True,True,True,False,True,True,False,False,True,False,False,True,False,True,True,True,False,False,True,False,True,False,True,False,False,True,False,False,True,True,False,True,False,True,True,True,True,True,True,False,False,True,True,False,True,False,True,True,False,False,True,False,True,False,False,True,True,False,True,True,True,True,False,True,True,True,True,False,False,False,False,False,False,True,True,True,True,False,False,False,True,True,False,False,True,False,True,True,False,True,False,True,False,False,False,True,True,True,True,True,False,True,False,False,False,True,True,False,True,True,False,False,False,False,False,True,False,False,False,False,True,False,True,True,False,True,True,True,True,False,True,True,False,True,True,False,False,False,False,True,True,False,False,True,False,False,False,False,False,True,False,True,True,True,True,False,True,False,True,False,False,False,True,False,True,False,True,True,False,True,True,True,False,True,False,False,True,False,True,False,True,True,True,True,True,False,True,False,False,False,False,True,True,True,True,False,True,False,False,True,False,True,False,False,False,False,False,True,False,True,True],[False,True,True,True,False,True,False,False,False,False,False,True,True,True,False,False,False,True,False,True,True,True,True,True,True,True,True,False,True,True,False,True,False,True,False,False,False,False,False,False,True,False,True,False,True,False,False,True,True,False,False,False,True,True,True,False,False,False,True,True,True,True,True,True,False,True,True,False,False,True,True,True,True,False,True,False,False,False,True,True,False,True,True,False,False,False,False,False,True,True,False,False,False,True,False,False,False,True,True,False,True,False,True,False,False,True,True,True,True,False,False,True,False,False,True,False,False,False,True,True,True,True,False,False,False,False,False,False,True,True,True,False,True,False,True,False,True,False,True,False,False,True,False,False,True,True,True,False,True,False,True,True,True,True,True,True,True,True,True,True,True,False,True,False,True,False,False,False,False,True,True,True,True,True,True,False,False,False,False,False,False,False,True,True,True,False,False,True,True,False,False,False,False,True,True,True,False,True,False,False,True,True,True,False,False,True,False,False,True,True,False,False,True,True,True,False,True,False,True,True,False,True,True,False,True,False,False,True,False,False,True,True,True,True,True,True,False,True,True,True,False,False,True,True,True,True,False,True,True,True,False,True,True,True,True,False,False,True,True,False,True,False,True,False,True,False,True,True,True,True,True,False,True,False,True,False,True,True,True,False,True,True,True,False,True,True,False,True,False,True,True,False,True,False,False,True,False,False,False,True,True,True,True,False,False,True,False,True,False,False,False,True,True,True,True,False,False,True,True,True,False,False,True,False,False,True,True,False,True,True,False,False,True,True,False,True,False,True,False,True,True,False,False,False,False,False,True,False,True,False,True,False,True,False,False,True,False,True,False,True,False,False,False,True]], dtype = "bool")#candidate|5065|(4, 364)|const|bool
call_5064 = relay.TupleGetItem(func_1009_call(relay.reshape(const_5065.astype('bool'), [7, 13, 16]), relay.reshape(const_5065.astype('bool'), [7, 13, 16]), relay.reshape(const_5056.astype('float32'), [12, 1]), ), 1)
call_5066 = relay.TupleGetItem(func_1013_call(relay.reshape(const_5065.astype('bool'), [7, 13, 16]), relay.reshape(const_5065.astype('bool'), [7, 13, 16]), relay.reshape(const_5056.astype('float32'), [12, 1]), ), 1)
output = relay.Tuple([call_5027,var_5028,uop_5034,call_5054,var_5055,const_5056,const_5057,call_5064,const_5065,])
output2 = relay.Tuple([call_5029,var_5028,uop_5034,call_5058,var_5055,const_5056,const_5057,call_5066,const_5065,])
func_5067 = relay.Function([var_5024,var_5028,var_5055,], output)
mod['func_5067'] = func_5067
mod = relay.transform.InferType()(mod)
mutated_mod['func_5067'] = func_5067
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5067_call = mutated_mod.get_global_var('func_5067')
var_5069 = relay.var("var_5069", dtype = "float32", shape = (12, 2, 11))#candidate|5069|(12, 2, 11)|var|float32
var_5070 = relay.var("var_5070", dtype = "float64", shape = (300,))#candidate|5070|(300,)|var|float64
var_5071 = relay.var("var_5071", dtype = "int64", shape = (224, 2))#candidate|5071|(224, 2)|var|int64
call_5068 = func_5067_call(var_5069,var_5070,var_5071,)
output = call_5068
func_5072 = relay.Function([var_5069,var_5070,var_5071,], output)
mutated_mod['func_5072'] = func_5072
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5105 = relay.var("var_5105", dtype = "uint32", shape = ())#candidate|5105|()|var|uint32
const_5106 = relay.const([[[9,-10,-9,-4,8,7,-7,-9,-9,2,10,-5,7,9,5,9]],[[7,2,-4,5,4,-8,-6,9,-6,5,9,2,-9,6,-6,-10]],[[4,9,10,2,5,-6,8,6,4,-9,-3,-1,-2,8,3,1]]], dtype = "uint32")#candidate|5106|(3, 1, 16)|const|uint32
bop_5107 = relay.add(var_5105.astype('uint32'), const_5106.astype('uint32')) # shape=(3, 1, 16)
output = relay.Tuple([bop_5107,])
output2 = relay.Tuple([bop_5107,])
func_5115 = relay.Function([var_5105,], output)
mod['func_5115'] = func_5115
mod = relay.transform.InferType()(mod)
var_5116 = relay.var("var_5116", dtype = "uint32", shape = ())#candidate|5116|()|var|uint32
output = func_5115(var_5116)
func_5117 = relay.Function([var_5116], output)
mutated_mod['func_5117'] = func_5117
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5301 = relay.const([[[-4,10,6,7,4]],[[4,-7,-1,-4,2]],[[8,9,6,2,4]],[[5,-10,5,10,8]],[[1,-10,-2,-3,-3]],[[-4,-10,-6,3,-4]],[[-1,4,-3,-1,-2]]], dtype = "int16")#candidate|5301|(7, 1, 5)|const|int16
var_5302 = relay.var("var_5302", dtype = "int16", shape = (7, 6, 5))#candidate|5302|(7, 6, 5)|var|int16
bop_5303 = relay.bitwise_or(const_5301.astype('int16'), var_5302.astype('int16')) # shape=(7, 6, 5)
uop_5315 = relay.sinh(var_5302.astype('float64')) # shape=(7, 6, 5)
output = relay.Tuple([bop_5303,uop_5315,])
output2 = relay.Tuple([bop_5303,uop_5315,])
func_5320 = relay.Function([var_5302,], output)
mod['func_5320'] = func_5320
mod = relay.transform.InferType()(mod)
mutated_mod['func_5320'] = func_5320
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5321 = relay.var("var_5321", dtype = "int16", shape = (7, 6, 5))#candidate|5321|(7, 6, 5)|var|int16
func_5320_call = mutated_mod.get_global_var('func_5320')
call_5322 = func_5320_call(var_5321)
output = call_5322
func_5323 = relay.Function([var_5321], output)
mutated_mod['func_5323'] = func_5323
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6045 = relay.var("var_6045", dtype = "uint16", shape = (10, 10, 12))#candidate|6045|(10, 10, 12)|var|uint16
var_6046 = relay.var("var_6046", dtype = "uint16", shape = (10, 10, 12))#candidate|6046|(10, 10, 12)|var|uint16
bop_6047 = relay.left_shift(var_6045.astype('uint16'), relay.reshape(var_6046.astype('uint16'), relay.shape_of(var_6045))) # shape=(10, 10, 12)
output = bop_6047
output2 = bop_6047
func_6053 = relay.Function([var_6045,var_6046,], output)
mod['func_6053'] = func_6053
mod = relay.transform.InferType()(mod)
var_6054 = relay.var("var_6054", dtype = "uint16", shape = (10, 10, 12))#candidate|6054|(10, 10, 12)|var|uint16
var_6055 = relay.var("var_6055", dtype = "uint16", shape = (10, 10, 12))#candidate|6055|(10, 10, 12)|var|uint16
output = func_6053(var_6054,var_6055,)
func_6056 = relay.Function([var_6054,var_6055,], output)
mutated_mod['func_6056'] = func_6056
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6233 = relay.var("var_6233", dtype = "float32", shape = (2, 4, 12))#candidate|6233|(2, 4, 12)|var|float32
uop_6234 = relay.atan(var_6233.astype('float32')) # shape=(2, 4, 12)
output = uop_6234
output2 = uop_6234
func_6236 = relay.Function([var_6233,], output)
mod['func_6236'] = func_6236
mod = relay.transform.InferType()(mod)
var_6237 = relay.var("var_6237", dtype = "float32", shape = (2, 4, 12))#candidate|6237|(2, 4, 12)|var|float32
output = func_6236(var_6237)
func_6238 = relay.Function([var_6237], output)
mutated_mod['func_6238'] = func_6238
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6246 = relay.var("var_6246", dtype = "float32", shape = (1, 15, 10))#candidate|6246|(1, 15, 10)|var|float32
uop_6247 = relay.cos(var_6246.astype('float32')) # shape=(1, 15, 10)
func_349_call = mod.get_global_var('func_349')
func_354_call = mutated_mod.get_global_var('func_354')
const_6253 = relay.const([2,-7,-6,6,-5,-5,3,1,9,9,-6,-3,-2,-1,3,7,9,-8,6,-3,6,4,-1,5,6,-4,-5,-9,5,8,-6,-3,6,2,-5,5,-2,-3,3,3,-2,-4,-5,5,-4,9,-7,-7,-6,-9,5,-4,-4,-9,5,-8,10,-5,6,-6,3,2,-2,7,9,8,-9,-10,1,7,1,4,-9,8,-9,6,2,3,9,3,-3,4,5,-2,3,-4,-7,8,9,1,-10,9,-5,7,2,1,-1,7,7,4,-1,6,1,5,-10,6,-3,4,-9,9,-1,7,3,9,5,4,4,-7,-6,2,9,5,-7,8,-10,-7,9,-4,-8,-4,6,1,10,4,-8,-1,8,-9,-7,-1,5,-9,-10,7,-7,2,-1,-5,1,-6,-10,8,-6,-3,3,1,1,-4,-4,10,-4,-5,7,3,-1,-7,-7,-1,9,8,-9,3,9,-1,-8,6,-7,-4,-3,10,-7,7,1,9,-1,5,-5,9,6,9,-3,6,6,-4,-9,2,-3,-2,-6,-6,7,6,10,8,-5,1,-1,-10,9,3,2,5,-6,-2,7,9,1,-8,3,8,2,-8,6,-8,-5,2,10,-3,-4,7,2,9,-3,6,-2,4,4,5,-3,7,-7,5,8,-4,-10,-6,-8,8,2,9,-8,6,-6,-4,-7,7,3,1,-8,4,5,4,6,7,4,10,9,-4,10,-4,-10,-2,2,4,8,10,9,9,4,3,-1,1,-2,5,-4,8,-1,-7,-4,3,-3,7,6,9,-3,-1,-5,4,-7,1,9,5,2,3,7,9,-8,1,-4,6,-3,2,9,-7,-7,8,-8,6,-7,5,4,3,2,-7,-4,-4,2,-5,3,5,-10,8,6,-7,4,8,-8,1,2,-6,3,-3,7,-5,-10,2,5,-8,-3,-5,-9,-6,-1,8,-5,2,-6,4,-1,-8,9,-10,10,-5,-3,2,3,-10,5,10,2,-1,-6,-6,3,-7,3,-7,7,10,2,3,-9,2,1,-7,5,-5,-10,8,-6,6,-4,4,4,-1,-5,-4,9,10,9,5,3,4,3,-9,-7,-8,-7,-2,4,9,-10,-4,10,-1,1,-4,-5,10,-10,-7,-5,8,5,2,5,-1,-4,-6,-10,5,2,-8,10,7,8,-7,-8,4,4,7,7,8,4,8,-2,7,-4,3,4,4,-5,-4,5,-8,-2,-10,-4,10,4,-4,-1,-2,-8,1,-6,-4,3,6,4,6,-1,-4,-9,-3,-4,-1,7,-2,-10,-7,-7,9,-8,9,-1,9,5,6,-10,7,5,-9,-3,9,3,2,-8,-1,10,-10,6,2,3,-3,9,6,-10,-6,5,8,3,1,3,-2,1,5,-1,9,6,-8,-4,9,-1,-6,-2,6,4,-9,-9,-1,2,10,-2,-1,10,5,4,-5,9,-3,6,8,-9,9,9,10,6,7,8,-8,7,-2,7,6,-1,-9,-8,-8,-6,-7,-5,-6,-7,-8,-1,5,10,-9,-7,3,5,8,10,2,-1,1,-4,-8,2,-7,-4,10,-2,-3,5,-8,9,-4,1,5,5,-9,-6,1,5,-10,-10,7,1,-10,5,7,-5,-4,-6,-10,6,-1,8,-10,-10,4,-3,2,10,-2,-4,-10,9,7,3,-6,9,-1,9,-2,2,-9,-8,10,-6,4,9,-1,7,4,7,1,9,-3,-1,-7,10,9,10,-5,-2,-6,-2,-1,-5,1,9,8,-1,-8,5,-7,-3,4,-8,8,9,-2,3,1,2,-1,-3,-1,-9,9,4,2,4,1,-8,-3,4,-9,-1,-6,2,6,-6,10,-5,3,6,-9,3,4,10,8,3,3,-8,8,6,-5,-10,10,-5,9,8,4,9,-5,-5,4,-2,1,6,10,-3,6,2,-1,9,-8,9,10,-2,-6,10,3,7,-2,3,-6,-8,2,-10,-7,-4,-8,9,-10,5,-5,7,8,4,-10,-3,5,-1,-3,9,-10,5,5,-7,4,-2,8,-9,-7,6,1,-6,-1,1,-7,-4,-5,-4,2,5,5,6,-9,8,7,-3,-3,3,5,-10,6,9,2,2,-9,1,-6,-7,-2,-3,9,5,5,10,4,4,3,-3,-1,10,-2,3,-9,-3,5,8,-1,10,1,-10,9,4,9,8,2,9,-2,-2,-3,10,2,-4,2,-3,-3,7,4,3,-1,-3,-2,9,-5,2,7,-5,-3,3,4,-6,8,-8,-7,6,-3,-10,-3,8,-1,5,-6,8,1,3,-9,2,-4,-10,1,-8,-6,1,7,-7,-10,8,-5,3,10,-3,7,-8,4,-2,5,1,-8,1,2,6,10,-7,-10,3,8,-3,-9,-6,9,2,-7,5,5,-3,-6,6,10,-3,6,4,-1,-9,-8,-5,-4,-10,10,-8,-3,-10,7,7,1,-2,5,1,3,-6,6,5,-8,2,-2,3,-9,-8,-10,8,4,-8,-5,5,-8,6,-2,-3,8,10,-6,-7,3,3,-10,-7,-8,3,4,1,1,-6,-10,5,4,10,-6,5,4,-5,7,-1,6,10,4,-2,1,-7,-8,-1,-6,2,-9,3,7,10,-9,10,-4,5,-6,-2,6,-7,2,7,-8,9,-8,-3,-10,8,3,-7,2,5,-1,-4,8,9,9,5,-7,-7,9,-1,-2,-10,-8,-1,1,10,-5,-6,4,-3,3,10,-4,-4,-6,4,3,2,3,6,1,3,-8,1,6,7,-1,7,4,10,6,10,2,-5,-5,-8,-4,-4,-1,6,-8,5,10,9,-3,5,-5,-3,7,1,-6,10,-9,2,-3,5,1,-3,2,-4,10,-8,-4,-1,6,5,-10,-2,1,-9,2,6,-6,4,-10,6,-8,7,5,5,10,5,-4,1,1,-10,7,-8,-6,4,-3,-5,5,4,-10,3,-8,-3,5,8,5,-3,-5,-5,5,6,-10,-10,-5,-8,5,6,-2,-4,3,5,9,10,10,4,7,-5,2,-5,-2,-3,-4,10,8,-3,7,8,-5,-9,-6,-10,4,-1,3,-5,-6,-3,7,-6,-9,-7,8,-2,6,8,6,-4,-3,9,8,2,4,6,-9,10,3,4,-5,-4,8,2,10,-4,-10,1,-9,-3,6,-6,-4,-3,-2,-10,-3,-7,-6,5,-4,1,2,-1,4,-3,3,-5,4,8,9,4,-4,-3,9,-8,-6,4,-2,-10,8,7,5,-10,4,-6,8,4,-10,-4,-6,-9,-5,4,-7,-4,-10,-6,-4,3,-6,2,-10,6,3,10,-6,4,1,9,-2,4,-5,-6,-9,-9,-9,-9,-7,-10,8,-2,8,-4,-5,10,-5,1,5,10,-8,8,-10,-8,-5,9,-10,-6,10,1,4,-3,4,-10,1,4,9,-9,-1,9,-9,7,-1,10,-4,7,10,8,3,-6,8,-8,-2,-9,5,-8,6,6,10,-1,6,-4,-7,4,-10,8,8,8,-2,4,-7,-6,10,2,-7,-6,-10,-1,5,-9,-4,7,-3], dtype = "uint64")#candidate|6253|(1320,)|const|uint64
var_6254 = relay.var("var_6254", dtype = "uint16", shape = (1, 225))#candidate|6254|(1, 225)|var|uint16
call_6252 = relay.TupleGetItem(func_349_call(relay.reshape(const_6253.astype('uint64'), [11, 12, 10]), relay.reshape(const_6253.astype('uint64'), [11, 12, 10]), relay.reshape(var_6254.astype('uint16'), [225,]), ), 5)
call_6255 = relay.TupleGetItem(func_354_call(relay.reshape(const_6253.astype('uint64'), [11, 12, 10]), relay.reshape(const_6253.astype('uint64'), [11, 12, 10]), relay.reshape(var_6254.astype('uint16'), [225,]), ), 5)
bop_6258 = relay.floor_mod(uop_6247.astype('float64'), relay.reshape(var_6246.astype('float64'), relay.shape_of(uop_6247))) # shape=(1, 15, 10)
func_11_call = mod.get_global_var('func_11')
func_15_call = mutated_mod.get_global_var('func_15')
const_6267 = relay.const([6,2,4,-3,-7,6,-5,9,7,-5,6,1,8,7,-9,-2,4,9,9,-1,-4,-4,1,10,-1,-10,1,-2,9,7,-4,3,2,8,-7,-10,7,9,-9,5,-6,-6,-6,-7,10,3,2,-3,-9,8,1,6,-1,-5,5,-10,-7,-9,-7,-8,-2,-2,-6,-1,-10,-2,4,-1,4,-7,8,-4,-6,-9,-9,1,-7,-6,-9,-1,-5,-2,-2,5,-8,7,-10,10,3,-8,-6,6,1,10,10,-3,-4,-3,5,-2,-10,1,-1,-3,-2,-9,-1,4,8,4,-7,10,-1,10,2,-10,-1,2,2,6,-8,2,9,-1,-4,-2,3,2,8,-9,4,-5,-8,8,-4,-4,1,-2,-4,7,2,-8,-5,9,2,4,-7,2,-5,5,-7,2,7,-6,10,10,5,7,10,-3,-3,-10,-7,-6,-5,4,2,-7,1,-1,-1,3,8,-7,-5,3,-9,-8,7,3,-7,-3,-2,-7,6,-3,10,2,-7,8,-1,-10,4,-1,4,-3,8,9,6,2,-3,-8,5,10,-1,4,9,-4,-5,-2,-6,7,10,-5,-1,8,-4,-8,-8,-2,7,3,-1,-9,-2,5,-7,-4,-10,1,6,7,6,2,4,-5,10,-8,-6,7,-7,8,5,-9,2,6,9,-1,-9,-9,5,-3,-3,-3,-8,-7,-3,9,8,2,-9,-10,-2,-5,2,-3,9,1,8,9,6,-1,10,8,-9,9,-1,-8,8,5,7,-6,-7,-6,-10,-1,2,5,5,1,-4,-3,9,-9,5,6,1,8,-8,-2,-1,7,8,-5,-5,-6,7,5,1,3,-5,7,3,-5,4,-3,2,-8,2,-3,2,-10,-1,6,-9,9,2,-2,-3,-7,-6,-2,2,9,5,-3,-5,9,9,7,6,4,2,-2,4,-4,2,9,7,-8,-3,-1,-5,4,6,2,7,-10,1,-8,3,-5,7,9,-3,-6,9,5,-8,9,-10,7,-6,-8,1,4,-7,1,5,8,8,-4,-1,-2,-8,6,2,7,10,-7,-3,-7,1,4,7,-6,6,-1,-1,-10,3,-6,7,5,9,2,-2,-2,-4,-1,-8,5,8,-3,-8,7,6,6,-9,5,-2,1,4,9,2,1,8,6,-2,7,3,-1,1,6,-8,-9,-8,4,-6,1,4,9,-10,2,-5,1,-4,9,-2,5,-6,8,-5,-5,7,8,-2,5,-2,-3,7,5,10,7,10,10,6,-9,2,3,-2,3,8,5,7,6,-5,3,6,-7,-4,2,7,-3,5,-8,-7,-10,-9,2,4,7,-1,-5,4,3,9,8,-7,4,-6,-9,-3,7,-6,7,-7,9,9,-6,8,-1,-7,10,9,-7,8,10,-7,-5,-6,-4,1,10,9,-2,-5,3,-1,5,-9,-9,-8,-8,3,-9,8,-1,-7,8,7,3,3,6,-1,6,-3,6,-3,10,10,5,3,6,9,7,5,9,-8,-2,6,-6,4,-4,-8,2,-2,-5,-5,4,-6,9,1,-9,-3,-7,-10,9,4,-10,-8,10,1,6,10,-9,2,-8,-8,-3,10,1,10,-6,5,-9,-8,6,4,-5,-3,1,-4,10,9,-4,-1,1,-7,10,-4,-9,-5,4,-7,6,-5,9,7,1,3,7,10,-9,-6,1,5,-2,2,-2,5,3,6,-9,-1,8,-4,8,-2,1,6,-8,1,-3,-6,-6,-4,10,10,2,-10,3,-7,9,10,7,-3,6,5,-9,-6,-1,-3,-8,-2,2,1,5,-10,7,-8,7,1,7,5,-4,-10,-9,8,6,8,-2,-5,6,3,7,-10,-5,8,-7,-8,1,-8,1,-8,7,-6,4,6,-9,7,-2,-8,10,-9,-6,9,-6,-8,6,5,1,-10,3,8,9,-7,2,10,-9,10,7,-3,-8,-10,-6,-6,4,-3,-6,-10,6,-5,-1,4,-5,7,4,3,-10,4,7,4,-8,10,-10,8,-8,-6,-2,-2,5,-9,9,10,-6,-5,6,4,-6,9,-7,-4,4,5,-10,-10,-6,3,2,5,10,9,-9,2,-7,5,-10,8,-7,-7,-2,4,-8,3,2,8,-8,-8,9,-6,2,2,-8,-3,7,-6,9,-9,8,-6,10,6,2,6,-5,10,4,7,-4,9,-2,-10,-4,7,1,-6,-1,8,6,5,-8,9,8,-6,-8,-4,9,-1,-5,6,-6,-6,7,-10,-1,6,-9,1,-1,-2,1,1,-1,4,-3,-3,-5,7,6,6,-10,7,7,9,-7,9,6,-8,4,-5,2,-7,-9,-10,-2,10,-9,5,7,6,-4,1,-4,-9,1,-7,-3,2,9,-5,-8,-4,4,-5,-3,2,-3,-9,2,-7,-3,-7,-9,6,-3,-10,8,10,-3,-2,3,4,-8,6,3,2,8,-2,-10,-6,1,-4,9,-2,8,-9,-7,10,7,5,9,-6,9,-3,-8,10,6,10,-9,-8,-8,9,-9,1,2,6,5,8,1,3,-2,-1,-8,-4,5,1,8,-9,8,2,7,-1,1,-8,-1,-2,-5,-3,-5,-7,8,4,-9,-2,-4,-7,4,5,7,10,6,3,6,-4,5,-1,-3,-7,-9,-9,3,6,-4,-3,-8,-9,4,8,9,2,5,-7,10,1,2,4,8,3,5,-2,-10,9,-6,5,-7,1,10,-8,-1,2,1,-1,10,-10,1,-7,-7,-6,-1,10,5,2,1,-8,1,8,-7,-10,2,-9,-3,3,-3,3,-9,4,6,1,-5,10,8,7,-6,10,6,10,-8,-9,3,6,7,-5,-5,-2,5,6,1,-7,-10,-4,8,6,-8,-6,-7,2,2,10,-4,-8,6,10,-1,4,-6,8,2,-8,8,-3,8,-2,-3,-8,7,-7,3,-10,-6,6,3,-6,9,-7,-9,4,6,-8,10,-7,3,10,3,10,2,-5,-1,10,-6,7,-7,-5,-10,-1,8,-7,-6,-6,-5,-10,2,4,6,-3,10,10,-2,-10,5,-3,3,-5,-5,8,7,8,5,5,5,6,8,5,-10,-4,-10,9,5,2,6,1,-2,-5,1,10,9,-3,3,-9,-7,-9,8,-10,-3,4,-4,5,3,5,-1,10,-3,7,3,1,6,6,-10,-8,9,-4,-6,1,8,-3,-10,-9,8,-1,1,-2,1,-3,-6,-6,5,-10,-1,-10,6,10,-10,1,4,-10,5,1,2,9,-7,3,-6,-2,-5,-10,8,8,-8,6,4,-6,-10,5,1,9,10,7,-4,-5,-3,-1,4,1,-2,-3,-4,3,3,7,-3,-1,10,-9,7,5,-8,1,8,1,10,4,2,-8,-9,-1,3,3,8,-8,-5,-4,-9,-2,-8,5,-8,2,10,7,6,10,-7,-3,-5,1,5,-3,-2,-1,10,10,7,-8,-3,4,2,-1,7,4,-6,-3,10,-5,-1,-5,-10,-8,7,4,2,9,2,-1,-3,-4,-9,10,-3,4,-1,6,5,10,2,2,-10,6,-1,4,3,5,-4,-3,-1,-10,7,-4,10,4,6,5,-9,1,-1,5,2,6,-8,3,-8,-2,1,-7,1,-4,-9,4,-2,-9,-1], dtype = "uint16")#candidate|6267|(1350,)|const|uint16
call_6266 = relay.TupleGetItem(func_11_call(relay.reshape(var_6254.astype('uint16'), [15, 15, 1]), relay.reshape(const_6267.astype('uint16'), [15, 15, 6]), ), 0)
call_6268 = relay.TupleGetItem(func_15_call(relay.reshape(var_6254.astype('uint16'), [15, 15, 1]), relay.reshape(const_6267.astype('uint16'), [15, 15, 6]), ), 0)
var_6284 = relay.var("var_6284", dtype = "uint16", shape = (5, 225))#candidate|6284|(5, 225)|var|uint16
bop_6285 = relay.logical_and(var_6254.astype('bool'), var_6284.astype('bool')) # shape=(5, 225)
output = relay.Tuple([call_6252,const_6253,bop_6258,call_6266,const_6267,bop_6285,])
output2 = relay.Tuple([call_6255,const_6253,bop_6258,call_6268,const_6267,bop_6285,])
func_6298 = relay.Function([var_6246,var_6254,var_6284,], output)
mod['func_6298'] = func_6298
mod = relay.transform.InferType()(mod)
mutated_mod['func_6298'] = func_6298
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6298_call = mutated_mod.get_global_var('func_6298')
var_6300 = relay.var("var_6300", dtype = "float32", shape = (1, 15, 10))#candidate|6300|(1, 15, 10)|var|float32
var_6301 = relay.var("var_6301", dtype = "uint16", shape = (1, 225))#candidate|6301|(1, 225)|var|uint16
var_6302 = relay.var("var_6302", dtype = "uint16", shape = (5, 225))#candidate|6302|(5, 225)|var|uint16
call_6299 = func_6298_call(var_6300,var_6301,var_6302,)
output = call_6299
func_6303 = relay.Function([var_6300,var_6301,var_6302,], output)
mutated_mod['func_6303'] = func_6303
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6555 = relay.var("var_6555", dtype = "float32", shape = (14, 16, 13))#candidate|6555|(14, 16, 13)|var|float32
uop_6556 = relay.sqrt(var_6555.astype('float32')) # shape=(14, 16, 13)
output = relay.Tuple([uop_6556,])
output2 = relay.Tuple([uop_6556,])
func_6563 = relay.Function([var_6555,], output)
mod['func_6563'] = func_6563
mod = relay.transform.InferType()(mod)
var_6564 = relay.var("var_6564", dtype = "float32", shape = (14, 16, 13))#candidate|6564|(14, 16, 13)|var|float32
output = func_6563(var_6564)
func_6565 = relay.Function([var_6564], output)
mutated_mod['func_6565'] = func_6565
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6883 = relay.var("var_6883", dtype = "float32", shape = (1, 9, 14))#candidate|6883|(1, 9, 14)|var|float32
uop_6884 = relay.log2(var_6883.astype('float32')) # shape=(1, 9, 14)
uop_6889 = relay.atanh(uop_6884.astype('float64')) # shape=(1, 9, 14)
output = uop_6889
output2 = uop_6889
func_6906 = relay.Function([var_6883,], output)
mod['func_6906'] = func_6906
mod = relay.transform.InferType()(mod)
mutated_mod['func_6906'] = func_6906
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6907 = relay.var("var_6907", dtype = "float32", shape = (1, 9, 14))#candidate|6907|(1, 9, 14)|var|float32
func_6906_call = mutated_mod.get_global_var('func_6906')
call_6908 = func_6906_call(var_6907)
output = call_6908
func_6909 = relay.Function([var_6907], output)
mutated_mod['func_6909'] = func_6909
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7525 = relay.var("var_7525", dtype = "float32", shape = (13, 3, 15))#candidate|7525|(13, 3, 15)|var|float32
uop_7526 = relay.atanh(var_7525.astype('float32')) # shape=(13, 3, 15)
func_5320_call = mod.get_global_var('func_5320')
func_5323_call = mutated_mod.get_global_var('func_5323')
const_7529 = relay.const([-5,-7,-10,6,5,-8,8,6,-7,-2,5,-9,4,10,-1,9,-8,5,-7,7,-6,10,9,3,7,10,-7,-4,-9,2,5,-7,8,-2,-5,-8,2,-7,4,-8,5,4,-7,5,-3,7,10,3,-6,-4,2,3,10,6,10,-4,1,9,6,-5,10,-7,6,8,-2,2,-4,9,-5,-7,-8,1,9,-9,-5,4,-8,6,10,3,-8,-8,-10,-8,2,9,8,-9,-4,-4,5,-4,10,5,6,3,-5,-6,-10,7,2,1,-9,-9,-7,2,10,4,-6,9,9,5,5,-6,-6,6,-2,-7,5,6,8,5,3,-9,10,-2,4,-10,9,-3,-2,4,-5,-5,-9,-4,10,-7,1,-4,8,10,3,10,-8,8,3,2,-3,8,-9,-8,-6,-1,-5,-7,-3,4,7,-10,6,-4,10,-6,-6,-4,9,-5,-9,1,3,6,7,4,5,-8,1,-9,-10,3,-1,3,7,6,-4,1,-7,3,-8,-7,-10,3,10,2,8,6,-10,-1,6,-4,-4,-8,-3,-6,-8,1,9,9,7,9], dtype = "int16")#candidate|7529|(210,)|const|int16
call_7528 = relay.TupleGetItem(func_5320_call(relay.reshape(const_7529.astype('int16'), [7, 6, 5])), 1)
call_7530 = relay.TupleGetItem(func_5323_call(relay.reshape(const_7529.astype('int16'), [7, 6, 5])), 1)
func_2297_call = mod.get_global_var('func_2297')
func_2300_call = mutated_mod.get_global_var('func_2300')
var_7537 = relay.var("var_7537", dtype = "float32", shape = ())#candidate|7537|()|var|float32
var_7538 = relay.var("var_7538", dtype = "float32", shape = (55, 4))#candidate|7538|(55, 4)|var|float32
call_7536 = func_2297_call(relay.reshape(var_7537.astype('float32'), []), relay.reshape(var_7538.astype('float32'), [11, 5, 4]), )
call_7539 = func_2297_call(relay.reshape(var_7537.astype('float32'), []), relay.reshape(var_7538.astype('float32'), [11, 5, 4]), )
func_2851_call = mod.get_global_var('func_2851')
func_2855_call = mutated_mod.get_global_var('func_2855')
var_7542 = relay.var("var_7542", dtype = "int64", shape = (12, 156))#candidate|7542|(12, 156)|var|int64
const_7543 = relay.const([3,1,5,-3,-3,4,-10,10,-9,8,-9,8,-7,-10,-8,-6,-8,3,1,8,6,5,6,6,4,-7,-8,-8,5,-2,4,-6,-8,-8,4,10,9,-5,-1,-10,-7,-7,4,-2,1,4,3,-10,8,8,3,3,5,6,-3,10,7,-2,1,2,7,9,-7,-3,-6,-10,-10,10,-2,-1,5,2,-9,5,-10,1,-4,-9,9,7,-2,-4,-9,-8,-3,8,10,-1,4,-8,2,2,-10,-6,-3,-4,-1,1,-5,5,-10,7,10,-9,-6,1,-8,4,5,9,-5,7,3,8,-7,-7,3,-6,-6,1,6,7,-4,2,-3,9,5,-5,-4,-8,5,7,-1,-5,2,6,6,1,-8,-3,-5,-8,10,9,-8,4,-2,3,6,10,-4,5,4,3,-9,1,-9,-2,-4,-1,-10,6,-6,7,9,-1,6,4,-1,1,1,2,3,-9,9,-1,-4,10,8,-5,7,-9,-1,-4,-7,-2,9,8,-10,-2,6,-7,-8,4,4,-2,-5,-5,-3,-9,-6,-1,-7,-8,6,7,1,2,-10,-7,6,-5,-4,7,9,-10,-9,9,-9,-4,-7,7,-2,1,-7], dtype = "uint16")#candidate|7543|(225,)|const|uint16
call_7541 = relay.TupleGetItem(func_2851_call(relay.reshape(var_7542.astype('int64'), [12, 13, 12]), relay.reshape(var_7542.astype('int64'), [12, 13, 12]), relay.reshape(const_7543.astype('uint16'), [225,]), ), 3)
call_7544 = relay.TupleGetItem(func_2855_call(relay.reshape(var_7542.astype('int64'), [12, 13, 12]), relay.reshape(var_7542.astype('int64'), [12, 13, 12]), relay.reshape(const_7543.astype('uint16'), [225,]), ), 3)
output = relay.Tuple([uop_7526,call_7528,const_7529,call_7536,var_7537,var_7538,call_7541,var_7542,const_7543,])
output2 = relay.Tuple([uop_7526,call_7530,const_7529,call_7539,var_7537,var_7538,call_7544,var_7542,const_7543,])
func_7546 = relay.Function([var_7525,var_7537,var_7538,var_7542,], output)
mod['func_7546'] = func_7546
mod = relay.transform.InferType()(mod)
var_7547 = relay.var("var_7547", dtype = "float32", shape = (13, 3, 15))#candidate|7547|(13, 3, 15)|var|float32
var_7548 = relay.var("var_7548", dtype = "float32", shape = ())#candidate|7548|()|var|float32
var_7549 = relay.var("var_7549", dtype = "float32", shape = (55, 4))#candidate|7549|(55, 4)|var|float32
var_7550 = relay.var("var_7550", dtype = "int64", shape = (12, 156))#candidate|7550|(12, 156)|var|int64
output = func_7546(var_7547,var_7548,var_7549,var_7550,)
func_7551 = relay.Function([var_7547,var_7548,var_7549,var_7550,], output)
mutated_mod['func_7551'] = func_7551
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8288 = relay.var("var_8288", dtype = "float32", shape = (15, 12, 3))#candidate|8288|(15, 12, 3)|var|float32
uop_8289 = relay.sigmoid(var_8288.astype('float32')) # shape=(15, 12, 3)
output = uop_8289
output2 = uop_8289
func_8304 = relay.Function([var_8288,], output)
mod['func_8304'] = func_8304
mod = relay.transform.InferType()(mod)
mutated_mod['func_8304'] = func_8304
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8305 = relay.var("var_8305", dtype = "float32", shape = (15, 12, 3))#candidate|8305|(15, 12, 3)|var|float32
func_8304_call = mutated_mod.get_global_var('func_8304')
call_8306 = func_8304_call(var_8305)
output = call_8306
func_8307 = relay.Function([var_8305], output)
mutated_mod['func_8307'] = func_8307
mutated_mod = relay.transform.InferType()(mutated_mod)
const_8452 = relay.const([[[-1.485470,8.508779,-9.678810,-1.463091,3.828881,5.178299,1.116690,-7.927308,0.401182,-7.415345,2.110269],[4.695772,2.712344,3.040056,-9.650964,9.768784,3.828118,7.279023,-2.568646,-5.532249,4.602105,8.009918]],[[1.248049,-1.020445,-5.852829,3.064744,4.123420,1.840010,-1.662166,-9.127214,-0.044994,-7.262770,-6.414615],[2.894267,6.810038,-3.491383,-8.174198,2.145437,5.854425,-1.577682,-2.758102,-7.504903,-8.459732,4.275606]],[[-0.900638,1.344573,3.524698,-3.867613,-9.187970,-2.032857,-0.751492,-2.077292,5.265891,-4.218880,-5.319462],[-0.113515,-4.727173,-4.580858,7.568304,0.774471,5.294838,-4.629546,-0.853940,-7.442555,-1.610250,-2.161946]],[[7.292187,1.305905,0.306471,-6.054255,-3.223739,-2.872414,0.852572,-5.613430,-0.502706,-3.694526,-7.585602],[8.736450,-2.246240,4.758159,-9.191565,4.864171,9.253660,-8.598130,-1.130926,-6.075494,-4.476279,3.575420]]], dtype = "float64")#candidate|8452|(4, 2, 11)|const|float64
uop_8453 = relay.log(const_8452.astype('float64')) # shape=(4, 2, 11)
func_8304_call = mod.get_global_var('func_8304')
func_8307_call = mutated_mod.get_global_var('func_8307')
var_8458 = relay.var("var_8458", dtype = "float32", shape = (540,))#candidate|8458|(540,)|var|float32
call_8457 = func_8304_call(relay.reshape(var_8458.astype('float32'), [15, 12, 3]))
call_8459 = func_8304_call(relay.reshape(var_8458.astype('float32'), [15, 12, 3]))
var_8460 = relay.var("var_8460", dtype = "float32", shape = (15, 12, 3))#candidate|8460|(15, 12, 3)|var|float32
bop_8461 = relay.bitwise_or(call_8457.astype('uint8'), relay.reshape(var_8460.astype('uint8'), relay.shape_of(call_8457))) # shape=(15, 12, 3)
bop_8464 = relay.bitwise_or(call_8459.astype('uint8'), relay.reshape(var_8460.astype('uint8'), relay.shape_of(call_8459))) # shape=(15, 12, 3)
func_254_call = mod.get_global_var('func_254')
func_257_call = mutated_mod.get_global_var('func_257')
var_8467 = relay.var("var_8467", dtype = "float32", shape = (1, 12))#candidate|8467|(1, 12)|var|float32
var_8468 = relay.var("var_8468", dtype = "uint16", shape = (225,))#candidate|8468|(225,)|var|uint16
call_8466 = relay.TupleGetItem(func_254_call(relay.reshape(var_8467.astype('float32'), [1, 3, 4]), relay.reshape(var_8468.astype('uint16'), [225,]), ), 2)
call_8469 = relay.TupleGetItem(func_257_call(relay.reshape(var_8467.astype('float32'), [1, 3, 4]), relay.reshape(var_8468.astype('uint16'), [225,]), ), 2)
output = relay.Tuple([uop_8453,var_8458,bop_8461,call_8466,var_8467,var_8468,])
output2 = relay.Tuple([uop_8453,var_8458,bop_8464,call_8469,var_8467,var_8468,])
func_8470 = relay.Function([var_8458,var_8460,var_8467,var_8468,], output)
mod['func_8470'] = func_8470
mod = relay.transform.InferType()(mod)
mutated_mod['func_8470'] = func_8470
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8470_call = mutated_mod.get_global_var('func_8470')
var_8472 = relay.var("var_8472", dtype = "float32", shape = (540,))#candidate|8472|(540,)|var|float32
var_8473 = relay.var("var_8473", dtype = "float32", shape = (15, 12, 3))#candidate|8473|(15, 12, 3)|var|float32
var_8474 = relay.var("var_8474", dtype = "float32", shape = (1, 12))#candidate|8474|(1, 12)|var|float32
var_8475 = relay.var("var_8475", dtype = "uint16", shape = (225,))#candidate|8475|(225,)|var|uint16
call_8471 = func_8470_call(var_8472,var_8473,var_8474,var_8475,)
output = call_8471
func_8476 = relay.Function([var_8472,var_8473,var_8474,var_8475,], output)
mutated_mod['func_8476'] = func_8476
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8690 = relay.var("var_8690", dtype = "float64", shape = (8, 14, 4))#candidate|8690|(8, 14, 4)|var|float64
uop_8691 = relay.acos(var_8690.astype('float64')) # shape=(8, 14, 4)
output = uop_8691
output2 = uop_8691
func_8697 = relay.Function([var_8690,], output)
mod['func_8697'] = func_8697
mod = relay.transform.InferType()(mod)
mutated_mod['func_8697'] = func_8697
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8698 = relay.var("var_8698", dtype = "float64", shape = (8, 14, 4))#candidate|8698|(8, 14, 4)|var|float64
func_8697_call = mutated_mod.get_global_var('func_8697')
call_8699 = func_8697_call(var_8698)
output = call_8699
func_8700 = relay.Function([var_8698], output)
mutated_mod['func_8700'] = func_8700
mutated_mod = relay.transform.InferType()(mutated_mod)
const_8709 = relay.const([[[-7.012850,-0.118616,-3.839622],[8.629501,-4.384430,-1.680511],[3.172708,-9.427120,6.091395],[1.365131,-8.667208,3.399822],[6.379721,3.507914,-4.350792],[3.757397,9.354837,-2.893556],[9.147057,-6.312557,-6.176352],[0.255535,-7.436798,7.390531],[3.244768,-4.720524,-9.334550],[-3.341474,4.819935,-2.423204],[-3.843906,-0.640300,9.318114],[1.047041,-2.218393,6.258416],[8.196049,6.010655,-8.802669],[0.909707,9.284799,6.551145],[2.851899,-2.753869,-2.916339]],[[-1.626192,-7.209683,-3.436561],[4.745495,-2.893893,-4.906550],[6.386641,-4.835833,8.431116],[1.694265,8.248044,-9.797347],[-9.375706,-3.150091,-9.076119],[9.816060,9.110271,-4.649175],[-2.328472,0.898029,4.101596],[-3.484187,7.577939,4.455429],[3.040313,0.055658,-4.934347],[6.396187,7.375498,4.241928],[-8.898655,-4.212533,-7.139390],[-4.963113,3.290917,1.836887],[4.556384,6.863796,-5.921409],[8.422393,2.549945,-2.459632],[-5.847668,-8.545542,5.968184]],[[-3.266237,-3.129541,9.088756],[6.658982,4.094796,-4.317501],[6.457893,-0.202073,-8.722452],[-0.789075,-9.007937,1.521973],[9.772182,9.455328,3.634475],[7.579494,-4.470799,8.040997],[-5.261343,5.189445,6.194558],[-3.432913,7.295995,3.071604],[6.348667,5.473934,4.965760],[2.342608,4.509199,-0.220437],[8.223676,-0.457259,4.275901],[-3.053192,-0.925717,-0.498146],[9.780958,-3.819791,3.091568],[-9.063350,4.682258,4.501442],[-7.717743,9.985642,8.826001]],[[0.762460,5.369345,-1.265260],[5.818031,-6.946637,2.793643],[4.374749,4.718728,5.130213],[1.913766,-0.433768,-7.102917],[7.164005,-9.499410,-1.310785],[-7.927480,-3.221656,9.053105],[-3.345725,9.473113,-1.483420],[1.930812,6.707027,0.215018],[-3.985089,1.381276,-7.023141],[-1.566257,-8.132220,-7.972633],[-4.117427,-6.713824,4.698179],[0.039052,-0.417136,-9.692406],[8.007324,-2.676301,8.825674],[-9.163414,-0.219288,-7.375687],[1.352798,-1.744457,6.192233]],[[-3.242041,0.073009,-2.216310],[-9.985048,0.669568,3.102281],[0.064478,2.712334,6.772379],[4.928256,-4.833227,7.971615],[-4.480928,5.936153,4.267307],[-8.228236,-0.853652,-5.978865],[-4.920445,7.365778,-6.589844],[1.506892,5.219277,8.196772],[1.525715,-3.050763,3.312351],[-6.413742,-4.967851,-5.895513],[-0.475829,9.820679,3.716496],[-0.033496,-8.436944,9.447329],[-7.186748,-4.992666,7.403452],[-8.996579,5.627840,6.140134],[2.455588,-3.249672,9.876205]],[[3.546558,9.198590,6.175060],[-3.560696,-9.081641,7.571939],[8.405258,4.825554,8.643358],[-5.612190,1.806704,9.462053],[-8.334945,1.071855,-8.691793],[4.711802,-8.332133,8.904479],[5.795307,3.763530,-7.375110],[7.509867,-4.042652,-8.706910],[-4.748917,-5.231186,-5.846970],[-5.242226,-6.605274,6.135208],[-8.989053,-1.465433,-0.599369],[-7.623045,0.094307,5.714342],[-5.411186,-2.270609,0.451913],[1.818780,9.690519,-7.438178],[7.426549,-3.404553,-8.265957]],[[-7.106721,-7.650225,8.617342],[-9.635069,8.074551,-8.085415],[-3.407130,2.480529,7.771820],[0.325847,-6.148486,-5.094837],[-8.860143,3.077591,7.058460],[-4.037169,6.040538,-8.555802],[5.467880,-4.520085,7.127602],[-5.179082,-9.873090,-7.407629],[-0.948318,-1.161863,-8.683418],[2.912497,-0.888685,7.329462],[-7.709866,0.851544,-5.391435],[1.340784,1.792773,-9.485918],[-1.862734,-9.931056,7.860722],[-3.312836,-9.476892,-4.909364],[-3.426607,5.772334,0.841310]],[[-9.741458,-9.751917,5.683545],[-6.248325,4.700040,-5.777872],[-9.512942,-2.644452,3.303374],[9.310586,1.369592,-1.529481],[-2.944624,-3.787299,2.981028],[-1.459432,4.141663,-1.238055],[6.717513,8.841320,-3.116031],[0.573353,-8.500901,0.100771],[3.277236,-7.477397,-4.334933],[-3.119159,0.779748,-7.648454],[-4.837171,-8.151314,2.294522],[-5.266755,6.824664,8.252063],[-9.007251,-6.585872,-9.228592],[-3.579616,-7.722047,4.067594],[-6.943664,8.272864,-3.763378]],[[-0.071195,-0.175568,-4.841718],[4.208050,2.231283,7.404417],[-4.592029,9.188637,-4.207154],[-6.525191,2.697629,2.915658],[7.157160,-6.658908,1.289113],[-3.475096,-9.326073,4.307347],[8.398655,8.439895,9.468159],[1.327210,-9.733452,1.417862],[8.768945,-4.328187,-6.559513],[7.073215,5.318833,5.543733],[-6.489410,-3.648214,-0.850703],[6.579205,9.056520,-8.733079],[3.289049,-0.148854,-0.092704],[9.067355,-2.181770,-7.995780],[6.877637,-0.574200,-6.145867]]], dtype = "float64")#candidate|8709|(9, 15, 3)|const|float64
uop_8710 = relay.log2(const_8709.astype('float64')) # shape=(9, 15, 3)
func_6906_call = mod.get_global_var('func_6906')
func_6909_call = mutated_mod.get_global_var('func_6909')
var_8716 = relay.var("var_8716", dtype = "float32", shape = (126,))#candidate|8716|(126,)|var|float32
call_8715 = func_6906_call(relay.reshape(var_8716.astype('float32'), [1, 9, 14]))
call_8717 = func_6906_call(relay.reshape(var_8716.astype('float32'), [1, 9, 14]))
func_3039_call = mod.get_global_var('func_3039')
func_3041_call = mutated_mod.get_global_var('func_3041')
var_8726 = relay.var("var_8726", dtype = "float32", shape = (448,))#candidate|8726|(448,)|var|float32
call_8725 = func_3039_call(relay.reshape(var_8726.astype('float32'), [16, 7, 4]))
call_8727 = func_3039_call(relay.reshape(var_8726.astype('float32'), [16, 7, 4]))
func_6236_call = mod.get_global_var('func_6236')
func_6238_call = mutated_mod.get_global_var('func_6238')
const_8739 = relay.const([[6.770168,-8.848643],[0.467607,7.205533],[-6.306529,-5.484857],[4.351719,-6.391736],[3.615677,1.491803],[2.316455,-4.980755],[-3.774741,7.326625],[1.515518,-9.059152],[2.065984,9.080251],[-4.130834,-4.161676],[-6.187536,-3.619956],[-5.236826,0.196975],[-4.247480,-8.201143],[-2.272334,4.130429],[-6.826185,5.625418],[5.474634,-0.160409],[-5.291118,-2.461039],[9.501561,7.085049],[4.150048,5.501331],[6.400861,8.979245],[0.290873,9.149455],[-1.527932,-5.647046],[0.495577,-6.778251],[5.637501,7.658481],[8.563580,9.131142],[-9.470898,-9.666141],[-4.204259,-3.819754],[-1.020490,3.990433],[4.987634,7.962601],[-4.855227,-3.199339],[4.937759,-8.627852],[6.584301,-6.394911],[0.497242,9.217330],[-2.077605,4.043574],[-5.763547,-6.755471],[-2.255862,-2.035379],[-9.445051,9.090003],[-7.597368,-0.605017],[5.020139,-7.319487],[-0.288382,3.950976],[-8.541125,-2.921224],[-5.896267,7.815307],[6.483740,3.983895],[-8.280102,0.692694],[7.367724,6.397888],[-9.337098,3.784786],[-4.419719,-6.493449],[-9.688404,9.036139]], dtype = "float32")#candidate|8739|(48, 2)|const|float32
call_8738 = func_6236_call(relay.reshape(const_8739.astype('float32'), [2, 4, 12]))
call_8740 = func_6236_call(relay.reshape(const_8739.astype('float32'), [2, 4, 12]))
func_4399_call = mod.get_global_var('func_4399')
func_4402_call = mutated_mod.get_global_var('func_4402')
var_8754 = relay.var("var_8754", dtype = "int8", shape = (24,))#candidate|8754|(24,)|var|int8
call_8753 = func_4399_call(relay.reshape(var_8754.astype('int8'), [1, 6, 4]))
call_8755 = func_4399_call(relay.reshape(var_8754.astype('int8'), [1, 6, 4]))
func_11_call = mod.get_global_var('func_11')
func_15_call = mutated_mod.get_global_var('func_15')
var_8761 = relay.var("var_8761", dtype = "uint16", shape = (225,))#candidate|8761|(225,)|var|uint16
var_8762 = relay.var("var_8762", dtype = "uint16", shape = (1350,))#candidate|8762|(1350,)|var|uint16
call_8760 = relay.TupleGetItem(func_11_call(relay.reshape(var_8761.astype('uint16'), [15, 15, 1]), relay.reshape(var_8762.astype('uint16'), [15, 15, 6]), ), 0)
call_8763 = relay.TupleGetItem(func_15_call(relay.reshape(var_8761.astype('uint16'), [15, 15, 1]), relay.reshape(var_8762.astype('uint16'), [15, 15, 6]), ), 0)
func_2582_call = mod.get_global_var('func_2582')
func_2588_call = mutated_mod.get_global_var('func_2588')
const_8778 = relay.const(-6.254253, dtype = "float32")#candidate|8778|()|const|float32
var_8779 = relay.var("var_8779", dtype = "float32", shape = (12,))#candidate|8779|(12,)|var|float32
const_8780 = relay.const([7,2,8,-10,-2,-8,6,8,-7,3,-1,7,10,2,-8,3,8,-1,-5,-7,-3,-5,2,-8,4,-8,10,-8,5,-6,2,-8,5,9,10,8,-10,4,-8,-10,4,9,5,4,-9,1,-2,-2,-10,-8,6,6,10,-5,-10,1,4,10,7,-7,6,10,1,-4,2,1,-7,1,5,-6,-2,1,-6,5,-4,-2,4,-8,-3,-4,-4,2,-2,-9,-2,3,9,-1,-6,-8,9,-3,-1,8,3,8,8,7,4,8,10,-9,-5,3,7,4,-3,-8,5,-8,-9,6,-6,-7,10,6,7,8,-8,-5,-6,10,3,-6,6,-7,-10,-10,5,-1,-3,4,4,3,-6,-6,7,-4,6,9,3,4,-8,-4,-4,-9,-1,8,-6,7,9,-6,1,-7,1,-6,-3,-10,7,-5,8,-7,-8,4,5,-7,7,3,7,-3,-5,3,-1,8,-8,8,-6,2,-1,-7,10,-3,1,-4,-5,5,8,-9,-2,7,-9,-3,-2,-10,-3,-9,4,7,7,2,-8,5,6,7,10,-7,10,7,-6,5,5,2,6,-5,-3,-7,5,-9,4,8,-1,-5,4,5,9,1,3,-5,3,2,-6,-8,-10,1,-4,-10,-3,-8,-6,-9,2,-1,1,4,6,1,6,3,6,-10,1,3,-6,1,5,-7,9,-4,3,-6,3,-1,7,-4,7,1,-5,-2,-7,-1,4,-9,-7,3,10,-1,7,3,7,6,1,-4,2,-7,10,1,-7,8,3,6,-3,8,10,-5,-7,2,6,6,1,-7,1,-6,-8,4,6,-7,-8,10,-6,-6,-3,3,-2,7,4,4,-4,6,7,-5,2,3,-9,-10,5,8,-4,-9,-3,2,2,3,-8,-10,-10,7,7,4,2,-8,1,7,10,4,4,-1,3,4,2,6,7,4,7,9,-3,6,-7,-1,-9,-2,-4,9,6,9,-5,2,2,7,3,7,-5,1,-6,-10,-1,5,-5,3,10,-9,-8,-9,6,-8,-2,-8,9,-10,4,-9,-2,2,-1,-7,6,-5,9,-3,-10,8,7,10,5,-1,1,6,4,-9,5,-5,-5,5,4,1,-10,-7,-2,3,8,6,3,1,2,-2,9,7,-6,8,-10,-4,-9,-9,10,10,-7,-5,10,8,9,10,7,-10,10,5,-10,-2,1,-9,3,-7,8,3,-2,-2,10,9,-1,-2,-8,1,-5,-6,-2,7,8,8,-8,4,1,-2,-1,-8,-9,-1,7,-6,5,-9,9,-4,10,3,-2,-9,-6,-4,10,-7,-4,8,10,-4,-6,-2,8,3,8,5,2,3,-5,-3,10,-3,-10,-8,5,-5,-4,5,3,-2,-4,10,-3,4,-9,2,-8,-6,6,-9,5,-1,3,2,5,-6,1,5,-9,1,-7,-7,-5,-5,8,-3,10,-1,1,-10,9,5,3,3,10,-10,-4,4,-2,4,5,-3,9,-9,-9,-7,4,-8,4,7,-5,1,-5,-3,-5,5,2,6,-1,-4,-3,-9,-4,4,-8,2,-9,7,9,9,4,-6,3,10,9,6,-6,7,-2,8,3,7,2,-3,1,6,7,4,6,-6,7,-4,-7,-2,3,2,9,-7,-3,-3,2,2,3,-9,-9,3,9,6,2,6,8,-1,-9,-2,-9,-9,-6,10,8,-8,6,-10,1,-10,5,-8,8,-4,8,-1,10,-7,4,4,9,-8,7,2,7,-1,-2,9,-10,8,8,-6,3,3,-1,1,2,8,9,-7,4,1,9,-5,-3,-7,-4,9,6,-7,10,-8,-7,-2,-8,5,9,7,5,6,-7,-1,4,8,-2,9,-3,6,5,8,-9,3,-8,5,-2,-3,4,10,4,7,5,7,5,9,3,1,-8,-9,5,-10,-5,-6,7,-6,-5,6,-1,7,-8,3,-2,3,-9,6,8,-2,1,1,-3,-10,2,-8,8,-10,-2,8,-9,5,3,3,1,4,1,-1,-2,3,-8,-8,6,5,-3,3,-3,-10,-4,-8,8,7,7,4,-1,-5,7,7,3,3,-4,8,7,-4,2,-5,3,-2,10,-2,-4,-1,-4,6,10,-5,-6,-2,4,-3,9,7,-10,4,4,4,-5,-10,-3,6,6,8,6,-4,-7,7,4,9,2,5,-9,5,-4,-5,-1,-2,2,-8,1,9,10,-3,-9,-10,6,-8,-4,3,7,-7,-8,-5,9,1,7,8,-5,4,5,-6,9,8,-8,-3,8,5,-7,6,-6,-5,-8,-10,4,-8,8,-2,1,-4,2,6,-9,7,5,-3,-2,-6,1,-5,2,6,9,-8,-7,-1,-2,-10,-10,-9,10,-6,10,3,9,-6,1,-2,-9,3,5,-6,9,-9,1,-3,-10,3,2,9,2,-4,-9,-3,7,4,-10,-10,-6,-9,7,-8,-3,-6,7,-8,-3,3,-1,8,-2,1,-3,-2,-9,6,3,4,-6,-10,-6,-1,-3,10,-3,-1,3,7,-2,-6,10,-9,-7,6,3,-4,6,-7,2,-2,-6,-9,4,6,7,-9,4,-9,-2,2,-2,-6,6,9,1,-4,-4,-7,-3,4,-4,8,-2,-7,-3,-2,7,-3,-1,2,4,10,-1,8,-1,3,-7,3,9,6,1,6,3,-5,-4,6,-3,7,5,-7,8,-4,-4,-6,9,4,7,-1,9,-5,-3,2,7,-1,5,-9,-1,-7,9,7,-5,-9,-8,3,6,-4,-8,6,-6,-8,-6,-3,1,1,3,-10,-8,-1,9,8,1,-2,-6,2,5,2,-8,-10,5,9,-1,6,-5,-8,8,-10,5,8,10,5,2,9,-2,-7,2,7,-4,-3,-10,5,-4,-7,-7,-2,6,2,-5,-6,-2,8,-8,5,7,-2,8,5,10,-1,-8,4,10,-4,9,-6,4,4,10,-5,-1,4,-2,-1,2,1,-7,-7,-3,6,10,4,7,-5,1,-3,-7,-2,-7,-3,-5,2,9,10,10,-5,-7,2,9,2,7,2,4,5,7,4,-2,3,-6,3,-9,4,-7,2,6,-8,1,9,6,-9,-1,4,-9,-5,9,1,-8,6,3,-5,-3,-4,-5,-2,-6,-3,-3,-10,-5,9,7,-4,5,4,9,5,-2,-6,1,-9,8,3,10,-6,-10,-9,-5,2,2,-5,5,2,-8,-6,4,-5,-7,6,10,2,-6,-7,-3,-8,4,5,3,7,-6,10,8,4,4,5,-9,5,8,-6,-10,-4,-8,-4,-6,4,-3,2,2,1,6,-9,2,2,-4,9,-3,-8,3,3,2,3,-4,1,3,-9,7,-3,1,-9,4,-1,-2,-9,1,-6,1,-10,-4,-2,-2,-5,-10,8,-6,8,-4,6,-10,-10,-10,5,6,8,-8,-7,1,9,-2,5,-3,-7,-4,2,-1,4,-1,-3,-4,-6,-1,-3,7,-8,-1,9,5,-3,-1,10,9,1,1,-6,-7,7,5,4,2,-3,2,6,-7,4,-6,-10,-8,-5,-7,4,-3,-3,1,-2], dtype = "uint64")#candidate|8780|(1320,)|const|uint64
call_8777 = relay.TupleGetItem(func_2582_call(relay.reshape(const_8778.astype('float32'), []), relay.reshape(var_8761.astype('uint16'), [225,]), relay.reshape(var_8779.astype('float32'), [12, 1]), relay.reshape(const_8780.astype('uint64'), [1320,]), ), 2)
call_8781 = relay.TupleGetItem(func_2588_call(relay.reshape(const_8778.astype('float32'), []), relay.reshape(var_8761.astype('uint16'), [225,]), relay.reshape(var_8779.astype('float32'), [12, 1]), relay.reshape(const_8780.astype('uint64'), [1320,]), ), 2)
output = relay.Tuple([uop_8710,call_8715,var_8716,call_8725,var_8726,call_8738,const_8739,call_8753,var_8754,call_8760,var_8761,var_8762,call_8777,const_8778,var_8779,const_8780,])
output2 = relay.Tuple([uop_8710,call_8717,var_8716,call_8727,var_8726,call_8740,const_8739,call_8755,var_8754,call_8763,var_8761,var_8762,call_8781,const_8778,var_8779,const_8780,])
func_8788 = relay.Function([var_8716,var_8726,var_8754,var_8761,var_8762,var_8779,], output)
mod['func_8788'] = func_8788
mod = relay.transform.InferType()(mod)
var_8789 = relay.var("var_8789", dtype = "float32", shape = (126,))#candidate|8789|(126,)|var|float32
var_8790 = relay.var("var_8790", dtype = "float32", shape = (448,))#candidate|8790|(448,)|var|float32
var_8791 = relay.var("var_8791", dtype = "int8", shape = (24,))#candidate|8791|(24,)|var|int8
var_8792 = relay.var("var_8792", dtype = "uint16", shape = (225,))#candidate|8792|(225,)|var|uint16
var_8793 = relay.var("var_8793", dtype = "uint16", shape = (1350,))#candidate|8793|(1350,)|var|uint16
var_8794 = relay.var("var_8794", dtype = "float32", shape = (12,))#candidate|8794|(12,)|var|float32
output = func_8788(var_8789,var_8790,var_8791,var_8792,var_8793,var_8794,)
func_8795 = relay.Function([var_8789,var_8790,var_8791,var_8792,var_8793,var_8794,], output)
mutated_mod['func_8795'] = func_8795
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8933 = relay.var("var_8933", dtype = "float32", shape = (12, 1, 5))#candidate|8933|(12, 1, 5)|var|float32
uop_8934 = relay.log2(var_8933.astype('float32')) # shape=(12, 1, 5)
bop_8941 = relay.floor_divide(var_8933.astype('float32'), relay.reshape(uop_8934.astype('float32'), relay.shape_of(var_8933))) # shape=(12, 1, 5)
output = relay.Tuple([bop_8941,])
output2 = relay.Tuple([bop_8941,])
func_8951 = relay.Function([var_8933,], output)
mod['func_8951'] = func_8951
mod = relay.transform.InferType()(mod)
mutated_mod['func_8951'] = func_8951
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8952 = relay.var("var_8952", dtype = "float32", shape = (12, 1, 5))#candidate|8952|(12, 1, 5)|var|float32
func_8951_call = mutated_mod.get_global_var('func_8951')
call_8953 = func_8951_call(var_8952)
output = call_8953
func_8954 = relay.Function([var_8952], output)
mutated_mod['func_8954'] = func_8954
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9040 = relay.var("var_9040", dtype = "float32", shape = (6, 6, 10))#candidate|9040|(6, 6, 10)|var|float32
var_9041 = relay.var("var_9041", dtype = "float32", shape = (6, 6, 10))#candidate|9041|(6, 6, 10)|var|float32
bop_9042 = relay.floor_divide(var_9040.astype('float32'), relay.reshape(var_9041.astype('float32'), relay.shape_of(var_9040))) # shape=(6, 6, 10)
output = relay.Tuple([bop_9042,])
output2 = relay.Tuple([bop_9042,])
func_9051 = relay.Function([var_9040,var_9041,], output)
mod['func_9051'] = func_9051
mod = relay.transform.InferType()(mod)
mutated_mod['func_9051'] = func_9051
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9051_call = mutated_mod.get_global_var('func_9051')
var_9053 = relay.var("var_9053", dtype = "float32", shape = (6, 6, 10))#candidate|9053|(6, 6, 10)|var|float32
var_9054 = relay.var("var_9054", dtype = "float32", shape = (6, 6, 10))#candidate|9054|(6, 6, 10)|var|float32
call_9052 = func_9051_call(var_9053,var_9054,)
output = call_9052
func_9055 = relay.Function([var_9053,var_9054,], output)
mutated_mod['func_9055'] = func_9055
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9302 = relay.var("var_9302", dtype = "uint64", shape = (7, 8, 7))#candidate|9302|(7, 8, 7)|var|uint64
var_9303 = relay.var("var_9303", dtype = "uint64", shape = (7, 8, 7))#candidate|9303|(7, 8, 7)|var|uint64
bop_9304 = relay.right_shift(var_9302.astype('uint64'), relay.reshape(var_9303.astype('uint64'), relay.shape_of(var_9302))) # shape=(7, 8, 7)
func_9051_call = mod.get_global_var('func_9051')
func_9055_call = mutated_mod.get_global_var('func_9055')
const_9314 = relay.const([6.170369,2.235980,2.530650,-2.706990,2.940988,7.311261,-2.896846,4.596595,3.320993,2.755280,4.097366,9.253130,5.272447,9.019303,-9.736174,-9.476823,2.357404,9.227098,-5.869623,-6.309105,-9.145817,-8.866562,-4.470380,-8.485354,-4.975312,8.726593,0.425479,7.935166,-7.782052,6.265844,-1.723122,2.647291,7.340200,-1.224540,-0.634480,-3.256272,-9.529795,8.819114,-8.762171,-2.967047,-2.926355,-9.582514,8.740112,-4.215485,-2.701084,-0.693493,-4.316607,8.753482,-1.385690,3.374704,-2.787083,7.725402,3.344116,0.345895,2.939297,-4.626844,7.177401,0.188776,3.691089,-0.512323,6.705811,-9.058955,-7.453820,-8.658817,6.218199,-9.705111,9.357626,5.902710,-2.194347,-6.423111,-6.553945,8.408974,7.852106,-7.315832,5.580537,2.615459,0.968487,-0.970735,6.249781,5.233789,-9.734896,-9.813083,9.957854,-6.918242,-8.165293,9.247230,-6.621370,-9.474530,7.729653,-2.400775,2.059694,-5.581865,7.291794,9.998314,3.394208,9.185912,-7.174369,3.735203,6.371364,8.789949,-3.995787,7.271847,-9.294527,-9.651366,-1.425299,-0.518117,-7.390479,8.415767,8.522802,-7.493801,2.501182,-9.901329,2.991666,0.202589,-4.669606,-5.727866,-8.609084,8.485637,9.858291,-8.710172,-2.949049,-9.975299,7.132080,-2.629820,-2.683446,3.429803,-1.044117,6.221954,3.123308,4.506850,0.606448,-9.121507,5.916510,-3.515719,-8.256272,-8.474906,7.575856,4.177901,-7.028640,9.729364,3.475449,-4.813784,8.821653,3.306012,6.192055,-9.210841,7.616847,-1.117436,-7.807960,8.247258,2.736526,9.399065,-8.000032,-2.793453,-2.133760,0.216246,-8.207843,0.548104,5.531834,8.931679,7.826937,-0.651821,-3.724235,2.248292,2.538178,3.229197,9.195727,-4.894251,-5.342845,-5.349623,-9.025354,-2.876410,-9.212202,-6.123510,-4.794399,-3.455593,4.905872,-0.658169,4.574324,-1.636191,7.206312,2.628527,-1.532298,-2.902493,-0.201600,6.713858,2.671929,-3.007685,-7.001090,6.562425,-9.256280,-3.862070,-9.136099,4.356286,6.850808,1.506389,-1.559778,6.144535,-9.281072,3.453923,-3.004257,4.637056,-0.950573,4.658342,4.370130,9.056362,-5.854872,8.713331,6.853097,-0.621366,0.959705,5.640545,5.773754,-9.389185,-4.382975,-9.954047,2.054663,-8.342005,9.690336,-4.495586,9.863230,-2.986419,4.035373,-9.458309,8.242864,5.799794,-0.493796,-0.526353,4.646389,7.462768,-0.548106,5.346812,-6.717553,2.604359,5.384877,-3.305714,0.130764,6.236894,-6.919086,3.931758,-9.736316,-5.495315,3.395616,-0.143215,-7.240139,9.365961,-5.530497,-9.346129,-6.114180,-8.913889,4.434158,-0.435296,-2.454859,8.801377,-6.376880,-1.455231,-3.207608,5.785196,7.023270,-7.675946,-3.600267,-2.313221,-3.128731,6.438273,-9.493774,7.079793,-5.184751,-2.091155,2.716339,5.432418,8.325126,-6.961267,1.432866,9.184326,-5.334596,-4.835473,8.493145,9.549558,1.557752,9.992928,-4.417004,6.658838,-5.998542,3.574269,8.707139,4.591226,-6.347484,-4.832440,-1.646550,-6.132686,-3.366444,5.962886,1.536928,8.517126,2.305937,-9.876296,3.876462,-6.707431,-1.141346,3.067929,-9.611284,-6.899256,2.574051,-8.417486,-9.283888,-6.747316,6.424501,2.478359,-8.999516,1.565413,6.462757,7.620486,4.574118,-6.000692,-1.746123,-7.136696,5.826610,3.432159,9.619723,-8.319143,3.012245,-1.415996,-7.766300,8.971482,4.869036,-9.158656,4.479343,9.661361,3.285549,-2.631399,-2.937059,-5.019890,2.146065,-6.309783,-5.082454,-2.509350,1.222373,-4.734604,-4.593993,-3.687155,1.953755,-7.565921,-5.250543,7.939060,-5.661453,7.805148,-1.548141,-5.821502,-4.611610,7.982842,0.506401,-5.489496,-7.156360,-2.016389,-4.792127,-4.235015,3.873330,-2.710258,5.135665,0.162752], dtype = "float32")#candidate|9314|(360,)|const|float32
call_9313 = relay.TupleGetItem(func_9051_call(relay.reshape(const_9314.astype('float32'), [6, 6, 10]), relay.reshape(const_9314.astype('float32'), [6, 6, 10]), ), 0)
call_9315 = relay.TupleGetItem(func_9055_call(relay.reshape(const_9314.astype('float32'), [6, 6, 10]), relay.reshape(const_9314.astype('float32'), [6, 6, 10]), ), 0)
func_3039_call = mod.get_global_var('func_3039')
func_3041_call = mutated_mod.get_global_var('func_3041')
var_9332 = relay.var("var_9332", dtype = "float32", shape = (448,))#candidate|9332|(448,)|var|float32
call_9331 = func_3039_call(relay.reshape(var_9332.astype('float32'), [16, 7, 4]))
call_9333 = func_3039_call(relay.reshape(var_9332.astype('float32'), [16, 7, 4]))
output = relay.Tuple([bop_9304,call_9313,const_9314,call_9331,var_9332,])
output2 = relay.Tuple([bop_9304,call_9315,const_9314,call_9333,var_9332,])
func_9335 = relay.Function([var_9302,var_9303,var_9332,], output)
mod['func_9335'] = func_9335
mod = relay.transform.InferType()(mod)
mutated_mod['func_9335'] = func_9335
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9335_call = mutated_mod.get_global_var('func_9335')
var_9337 = relay.var("var_9337", dtype = "uint64", shape = (7, 8, 7))#candidate|9337|(7, 8, 7)|var|uint64
var_9338 = relay.var("var_9338", dtype = "uint64", shape = (7, 8, 7))#candidate|9338|(7, 8, 7)|var|uint64
var_9339 = relay.var("var_9339", dtype = "float32", shape = (448,))#candidate|9339|(448,)|var|float32
call_9336 = func_9335_call(var_9337,var_9338,var_9339,)
output = call_9336
func_9340 = relay.Function([var_9337,var_9338,var_9339,], output)
mutated_mod['func_9340'] = func_9340
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9361 = relay.var("var_9361", dtype = "int8", shape = (14, 6, 15))#candidate|9361|(14, 6, 15)|var|int8
const_9362 = relay.const([[[1,-9,10,-4,4,1,-7,8,-10,1,-6,-2,6,9,6],[-7,8,1,-8,2,-5,1,5,1,6,-3,-10,-7,6,2],[7,-10,-5,-4,4,-7,8,4,-9,9,4,-10,-6,3,-4],[-4,4,10,5,-4,-8,1,-9,9,7,-5,-7,-7,3,-5],[-5,-2,4,-2,-3,-1,7,7,6,-4,-4,-6,-4,-6,-3],[6,1,-8,-7,8,-7,1,1,-10,5,-2,4,2,10,-7]],[[-10,-8,-10,-7,-9,6,-4,-9,-8,1,-4,-4,2,-10,-5],[-3,9,-7,-10,-5,9,-4,-10,-9,-2,4,5,8,-4,-8],[-5,-8,-4,5,-9,-4,4,3,-1,-4,3,10,-6,5,-7],[2,6,10,3,6,8,2,8,-9,10,-5,-3,-10,5,10],[-8,6,2,-4,3,-1,-9,-6,10,9,9,2,-9,3,-8],[6,7,2,7,-6,-5,3,10,5,5,2,8,-7,6,10]],[[5,2,7,-3,9,7,8,1,9,10,10,7,-5,6,6],[-5,-2,-3,2,-3,5,8,2,-1,-5,-7,2,4,10,-9],[6,5,3,-6,4,-10,1,-4,7,-8,-8,-9,8,-8,-3],[-5,10,-8,-8,2,4,-2,-7,-10,4,7,2,2,9,-8],[-6,-5,3,-1,-8,4,4,6,2,8,-5,-8,2,7,-10],[8,-10,-4,6,3,-8,-3,2,-6,9,-2,10,1,8,3]],[[-7,-5,4,9,5,-2,-8,7,-6,6,-8,2,-6,8,-3],[5,-4,6,-8,-5,-6,5,-4,5,5,9,-8,1,-4,-2],[-4,8,5,-5,10,5,-9,-1,3,6,7,-5,-4,1,-7],[-6,9,-8,-7,-9,-3,2,-5,6,1,9,-7,3,1,9],[10,-9,-9,-5,-10,-3,9,6,2,-5,5,-9,10,-4,-9],[-1,8,7,-6,4,-7,10,6,-3,9,-9,1,7,-1,4]],[[-3,10,4,-1,-10,-8,-5,4,-6,10,-4,-2,-7,8,-9],[2,5,5,9,-2,2,7,-10,-9,-9,-4,7,8,2,-6],[8,4,9,-5,-7,9,-6,-9,9,-3,-8,-9,-2,1,-5],[-6,6,-8,-9,-3,-1,6,-9,4,-4,4,5,-8,-2,-2],[7,-2,7,-8,-5,3,-5,3,-5,-2,3,2,3,6,9],[4,5,-9,-6,-9,7,-8,2,-6,6,7,-8,-9,10,-6]],[[-3,-7,6,3,10,-6,-5,-9,4,5,7,-3,-4,6,8],[-5,4,-1,5,-4,-5,1,-3,-8,-10,-8,8,4,4,6],[-3,6,10,-8,1,-9,10,-10,-4,1,3,3,-1,-1,-8],[-8,9,-8,3,-3,8,5,-6,3,3,-6,-3,6,-7,-10],[8,-7,2,-4,-3,-1,3,-9,9,8,5,-6,2,-2,-3],[-7,-10,5,-10,-9,8,-4,-4,-9,-6,-4,-9,-9,4,-4]],[[-6,5,-5,-10,-9,-10,6,9,10,2,-3,6,9,-6,1],[-8,-1,2,3,-3,-10,-1,-8,8,-8,-3,-9,6,-6,-8],[4,-3,1,3,5,8,10,2,2,5,2,-5,-6,-6,-3],[9,-2,-4,-8,-7,-2,8,6,9,2,2,-3,5,-5,-2],[-5,8,5,-10,-9,-6,6,5,8,2,10,-3,8,-2,9],[3,-7,3,3,5,-2,4,-6,10,5,-3,-7,-9,4,-9]],[[-7,7,5,8,-3,1,3,-5,-4,-3,10,-7,-10,-9,-8],[-7,3,9,-4,-6,-9,4,10,-10,-8,-7,-7,-3,-9,-3],[-3,3,4,1,-8,-7,-4,10,-2,-10,5,9,2,-3,4],[-1,8,-2,6,2,-2,3,-10,2,5,-4,-1,-4,-5,-7],[3,-8,2,3,7,1,2,5,-9,6,1,6,-5,5,5],[10,2,9,2,-9,5,8,6,-9,-2,-10,-7,5,9,3]],[[-3,-4,-3,-6,-2,3,7,-5,7,-1,-1,2,-9,1,8],[-2,6,-6,6,3,-1,5,8,-2,-4,-3,-3,-6,-3,-10],[10,2,7,-5,3,3,4,3,-8,4,9,-10,4,7,-10],[6,1,5,9,-3,8,6,5,-2,4,6,5,6,-9,-5],[-1,10,3,2,-7,-4,-2,-9,-10,10,8,7,-10,-3,7],[-8,10,-10,5,-5,-8,9,9,-7,-8,-3,10,2,-5,9]],[[-2,2,-6,5,6,-4,-8,4,-1,-4,-5,7,-9,5,3],[-7,2,-7,2,10,3,-2,-8,-8,-7,-8,-1,10,-6,-3],[-9,-4,-10,9,-6,-9,2,-9,10,-9,-10,-9,-6,9,4],[-10,4,3,-6,5,-1,10,8,6,-7,-4,6,5,6,1],[-10,4,5,-6,-2,-5,-7,-8,4,-4,-9,-7,-6,6,-8],[2,9,2,3,-7,8,8,6,-2,-10,-1,-5,-5,-1,-2]],[[7,9,-10,-2,-8,8,10,3,1,-6,2,-1,6,-1,-6],[-7,7,-1,-8,9,-1,-4,-4,8,-4,8,4,4,-5,8],[-8,-4,-3,-1,7,5,-9,-10,-7,8,-7,-7,6,-10,6],[2,-2,-10,-1,-6,-1,8,-1,2,-9,7,-7,-4,6,5],[3,-8,4,-10,9,5,6,-9,-2,-4,1,4,6,2,5],[5,-3,-2,1,3,-9,-1,2,3,2,2,9,-3,5,6]],[[-3,7,-4,-4,-5,6,-5,-3,6,8,5,1,-7,8,10],[-3,5,-8,3,5,-10,3,7,-4,-4,-10,4,3,-8,5],[-7,2,2,-4,-3,-4,9,10,-5,-8,7,-8,-3,-2,3],[10,10,5,-1,9,-7,7,-2,1,-1,8,9,7,-8,3],[-10,5,-3,4,-9,-10,-7,10,5,-9,-10,-4,-5,-9,2],[6,4,-2,4,-3,-8,-7,3,4,-1,-4,-10,-10,-9,-9]],[[2,3,-9,-5,10,3,-2,-2,-2,-2,-9,-5,-7,5,-5],[-9,10,-5,8,1,7,-5,-8,3,-3,-2,3,1,-4,10],[-1,-8,-2,1,2,-7,7,7,10,5,5,6,-7,-2,5],[2,-10,8,-5,9,2,6,9,-7,3,2,3,8,5,3],[-1,-8,7,-10,-7,-2,6,-10,-3,-3,3,4,3,6,-3],[8,5,-4,3,9,-4,9,-10,4,10,-10,1,6,8,-2]],[[2,7,-7,2,-5,-10,-3,-7,-1,-6,8,-3,2,5,-3],[2,-8,-5,-10,-6,9,1,4,4,-1,-6,6,8,-1,7],[9,-1,8,3,-4,-2,5,-4,-3,6,-7,-1,-4,-1,3],[8,1,2,-3,9,3,10,-5,9,-1,10,-7,-2,-3,5],[5,1,-1,5,-7,3,4,-8,-8,-6,1,-8,10,-9,-3],[8,-6,-3,-1,10,1,-6,7,-5,-2,-3,-7,-9,-8,-10]]], dtype = "int8")#candidate|9362|(14, 6, 15)|const|int8
bop_9363 = relay.bitwise_and(var_9361.astype('int8'), relay.reshape(const_9362.astype('int8'), relay.shape_of(var_9361))) # shape=(14, 6, 15)
uop_9370 = relay.cosh(bop_9363.astype('float64')) # shape=(14, 6, 15)
func_9335_call = mod.get_global_var('func_9335')
func_9340_call = mutated_mod.get_global_var('func_9340')
const_9373 = relay.const([3,-3,9,-8,6,3,5,-3,3,-1,4,-2,3,-9,3,6,-5,-8,4,5,2,-5,3,7,1,8,10,-10,-4,-7,-2,-3,-2,3,9,-6,-5,9,9,5,-4,7,-5,-8,-7,-5,9,-6,-1,7,-7,2,-3,2,-6,4,-2,-3,-10,-7,5,-8,10,-5,2,-10,4,1,-2,9,-7,-6,-6,7,10,-4,6,7,-5,6,4,-6,-5,-8,-7,-4,10,7,-9,-1,-10,1,-9,1,-3,-3,10,-7,-6,3,10,10,-7,7,1,4,4,-7,-6,-7,5,5,-9,2,7,-9,-3,8,-7,-6,2,-2,-5,-1,9,-1,-8,-2,1,4,-1,5,-3,-6,8,9,-1,-8,9,-9,-7,-3,-7,6,10,5,3,9,-3,-4,-4,2,-3,-2,-2,-9,1,8,8,5,-1,1,-2,-10,5,7,9,5,-2,4,-7,-2,6,6,1,-4,-4,8,7,-1,6,-4,-7,-8,-5,2,-7,10,-4,1,-10,2,4,-9,10,5,-10,-2,5,8,4,4,6,-7,4,8,5,-9,-1,-9,-10,6,3,-9,-8,10,8,-3,2,5,-10,-2,-4,-3,9,4,6,9,10,10,8,-9,-6,1,2,5,-8,6,-6,-6,1,-4,2,8,5,9,10,8,-10,-5,4,6,-7,-5,-1,9,3,-3,-9,6,-1,-7,-4,-8,-3,-9,-2,-10,-7,-5,-6,-4,-10,-3,-2,-2,5,-5,-4,5,5,-6,-9,8,-1,-6,-9,-3,9,-7,4,-3,9,-10,-10,-2,-1,2,3,7,6,1,6,-6,10,8,-5,5,-1,-8,-1,6,9,3,-9,-7,4,10,-2,6,10,-5,5,10,6,6,10,-1,-9,10,5,-3,-5,-8,9,-8,8,-5,-3,8,5,-9,6,-4,6,-5,1,-7,-10,3,1,-10,5,1,-4,-9,4,6,2,7,3,-7,9,-3,1,10,-7,10,-8,2,-1,-3,-3,-5,8,-10,-3,7,1,10,-8,-7,-1,-7,-9,10,-1,2,-3,-8,-8,-4], dtype = "uint64")#candidate|9373|(392,)|const|uint64
var_9374 = relay.var("var_9374", dtype = "float32", shape = (448,))#candidate|9374|(448,)|var|float32
call_9372 = relay.TupleGetItem(func_9335_call(relay.reshape(const_9373.astype('uint64'), [7, 8, 7]), relay.reshape(const_9373.astype('uint64'), [7, 8, 7]), relay.reshape(var_9374.astype('float32'), [448,]), ), 0)
call_9375 = relay.TupleGetItem(func_9340_call(relay.reshape(const_9373.astype('uint64'), [7, 8, 7]), relay.reshape(const_9373.astype('uint64'), [7, 8, 7]), relay.reshape(var_9374.astype('float32'), [448,]), ), 0)
func_8470_call = mod.get_global_var('func_8470')
func_8476_call = mutated_mod.get_global_var('func_8476')
const_9377 = relay.const([5.663790,9.456166,2.145805,0.369862,-5.935646,6.884769,-3.924858,-9.209154,-5.711155,5.550448,-2.681858,4.905374,4.279942,-6.933560,0.234906,7.923369,1.952872,6.274218,6.937058,7.442797,-8.916597,-9.991471,-2.471423,-2.616218,3.521130,-9.428553,8.676967,9.153200,2.186235,6.349581,-9.412243,0.986223,-8.584757,7.918923,1.638024,1.934227,7.216405,-6.385977,8.946323,1.863188,-2.106385,-8.973229,4.449035,-0.521292,7.304825,8.552322,2.847915,-3.094769,1.996018,5.840225,-3.860352,-8.804437,-0.390084,9.827969,-2.522437,-8.657729,-7.223365,-8.496767,6.906870,-8.944788,-8.315180,-5.271141,-4.843525,7.071852,-9.406923,-7.388351,-7.571141,4.384060,6.886845,-9.403085,6.449911,5.413973,2.886429,6.462010,-7.452156,-9.217881,9.689872,-2.288560,6.807078,-8.136807,-4.167504,-3.597614,4.200382,4.800439,-0.189838,-1.536781,9.045030,-6.686000,7.342350,3.743391,6.453797,9.362315,-3.948797,7.609772,4.509660,-5.428995,-3.366389,-8.968780,-5.255979,2.088535,2.240139,-0.622071,7.628334,-5.073473,-8.863404,-9.516001,5.240946,-0.966300,-6.540547,1.339585,2.812070,3.628254,-5.172585,-5.576634,-2.046590,6.914679,8.063863,-4.905077,-6.641749,-0.144480,-2.631314,5.346147,-8.003098,2.004537,6.949553,-8.369203,-4.547784,-2.671746,-7.002374,3.135871,-5.960187,-1.707992,-4.091086,-2.416059,6.232503,1.801059,-4.090821,2.091282,2.229949,8.011982,6.718309,2.288727,9.274086,-7.959761,-5.535709,-0.361700,5.663992,5.658701,5.708091,-3.670171,-6.388295,-9.071957,-9.030302,4.560849,9.867789,-9.307657,-5.196155,-6.512405,-6.699617,5.578356,2.066655,9.838536,1.545676,-3.163546,3.502145,5.287936,8.364915,-7.380921,-9.731577,3.207414,-3.112277,-9.447066,3.440583,-6.655475,-1.406477,6.355241,-1.742388,-6.158195,7.400355,-7.006992,1.598921,-6.618861,-0.652637,7.511803,-8.603024,-0.083326,-8.783611,5.050762,3.593700,9.677886,-1.428429,1.030560,-1.417018,-9.030854,6.213096,-5.584591,-4.435657,3.125746,8.463847,1.053441,0.462849,-0.790796,7.944356,7.582377,1.239890,-9.139828,3.385005,-3.868659,2.987292,8.243074,-1.184507,8.647413,-6.853110,7.439614,0.438147,8.129621,-6.892488,6.861851,-6.045255,-7.379374,1.348671,6.182666,8.323616,-8.501704,-8.548525,5.572079,9.529283,2.858601,4.396214,4.468912,-5.088133,9.890467,-2.319821,-2.261784,5.317209,5.429023,8.145603,-4.713661,-7.209026,1.154245,-1.221212,7.735807,2.188451,-6.402339,1.914909,-5.639112,-5.453734,-4.847674,-6.492543,6.961530,-3.620212,-8.746623,5.415615,-0.170858,-6.872451,-3.545371,-8.023577,-0.162677,6.333463,-6.232617,3.039930,-8.115349,-8.951054,-4.463621,3.194351,-3.030405,-4.634195,6.495884,1.780485,-2.477103,2.908334,1.552951,-1.428921,9.638777,-1.694230,0.939534,-2.107066,4.945815,-8.851525,3.902740,-3.397481,4.387821,8.986492,-5.732323,-9.447126,-5.464748,-3.788137,8.269507,9.002330,-8.831118,-4.690854,9.285702,6.151854,1.412569,8.659676,2.946369,7.655601,-9.325520,3.170045,1.689937,7.939023,9.059682,8.202482,5.164128,9.382553,-1.540342,9.072335,8.252620,1.113846,-5.539603,3.070629,-8.377283,9.015146,5.113393,4.650449,-5.631733,-3.943106,-5.635922,6.274717,6.587626,4.871670,-0.801228,5.759381,4.526422,2.344821,7.123654,3.247522,9.353083,9.174509,9.176129,3.039354,2.071836,0.230110,-7.482473,2.370503,-3.074199,8.051846,8.249772,-6.081509,1.936575,7.173190,-4.769674,-0.782597,8.412539,1.398640,2.892668,-1.781011,-1.083820,-6.781585,-7.762436,-8.345962,8.843404,-5.909199,6.596003,6.031495,-1.144954,0.464945,-5.119375,-8.065458,8.876626,-8.742871,-3.673092,-2.904924,9.158189,4.585625,-3.166918,-1.146002,-6.434091,5.648588,5.883021,-3.144907,4.313351,-3.545210,-6.583222,5.060132,-1.444815,-9.607992,-8.106646,-9.005665,5.523193,-5.760934,2.257526,5.530944,7.316648,8.917948,-4.105294,-7.070356,-2.794277,8.233335,3.955154,-8.340971,-5.576913,-3.456617,1.488356,-8.407110,5.566004,1.332635,9.147829,-2.811130,9.474804,9.416181,3.149223,6.300029,3.454281,-9.704020,0.792829,-9.243176,0.826844,-7.393596,6.320397,-7.121525,5.969439,-0.203046,-4.577959,5.786233,-5.539322,3.663729,-1.776221,0.866814,8.005456,-2.235112,2.635891,9.615706,-4.892533,3.325967,-5.288047,-8.504803,9.869780,0.610496,0.313709,9.232871,2.139975,2.412449,4.012428,6.609375,6.277765,7.875197,9.997743,1.641926,2.650066,3.452422,-1.248788,1.857750,-6.880889,-4.657694,-9.953534,-6.778193,-6.147231,4.941308,-7.691841,6.253804,9.241071,-5.270829,8.975283,-3.953594,2.434521,-1.645558,5.358676,9.958188,-9.751052,2.194618,-4.046294,0.170382,8.081258,-9.496519,6.944534,8.965811,0.397931,2.938458,-1.955878,6.114264,-4.581013,7.963451,3.571592,0.369472,-0.532827,-5.333371,-6.977266,-0.567956,4.479804,-0.041300,-5.537924,4.112887,7.588285,-6.257129,-4.169300,2.944332,7.317140,-5.039171,-1.761568,9.369657,-2.263849,7.144482,0.098422,-6.370903,-8.277007,6.287562,8.780504,-1.892561,-2.040147,-6.403049,-3.069732,2.291776,-0.847286,1.458047,7.776160,-3.971427,-4.352682,4.601826,4.776953,-7.368396,-8.741815,-3.780015,-2.419294,-5.418055,3.275803,6.430490,0.919398,9.804610,-5.590532,-8.752280,6.844619,4.695737,-0.673368,9.950406,1.221549,2.137695,-7.156331,5.685194,9.159741,8.378738,-2.459708,-6.570701,6.986223,8.600980,-4.072462,1.633647,-2.279125,-6.887858,6.262491], dtype = "float32")#candidate|9377|(540,)|const|float32
const_9378 = relay.const([[8.092199,-3.825803],[5.179439,7.222902],[-8.250418,-4.747986],[7.477775,5.664901],[-9.325422,4.762870],[-1.763504,6.652500]], dtype = "float32")#candidate|9378|(6, 2)|const|float32
const_9379 = relay.const([2,-8,-10,4,-7,-10,-9,-3,10,3,-9,6,6,8,-9,-3,-9,-9,-1,-10,-4,-1,1,-5,-7,-8,3,6,2,-7,5,2,-1,2,-4,2,5,2,-5,-8,-5,-9,-10,10,-1,5,-7,1,-7,-1,9,10,7,9,9,6,-4,4,2,-8,-3,10,-9,1,5,-1,-7,8,3,10,7,-7,1,-8,9,5,-10,-3,7,7,10,-8,-8,-3,-8,-4,8,-7,-7,1,3,-8,-2,-4,-7,-3,-8,3,9,-1,-10,-3,8,-5,-7,1,-4,-2,9,5,6,4,3,4,-5,1,9,4,-4,-2,-7,10,3,-8,-8,10,-5,10,4,-9,8,-6,4,4,-1,10,1,-1,-3,-7,-4,-7,-3,-6,-2,8,5,-4,-2,-8,5,2,7,10,-2,3,8,-4,6,8,5,7,-7,-10,9,5,7,2,1,-5,1,-9,-7,-9,-3,2,-2,9,-10,-2,8,-3,-5,8,-8,-8,-1,7,-8,-1,-1,8,-2,5,-5,-10,-6,-7,-1,6,-9,6,9,-8,-8,-9,-3,-6,-3,8,-10,2,-5,-7,-5,-4,5,-4,5,-3,-4,4,1,-4,-3], dtype = "uint16")#candidate|9379|(225,)|const|uint16
call_9376 = relay.TupleGetItem(func_8470_call(relay.reshape(const_9377.astype('float32'), [540,]), relay.reshape(const_9377.astype('float32'), [15, 12, 3]), relay.reshape(const_9378.astype('float32'), [1, 12]), relay.reshape(const_9379.astype('uint16'), [225,]), ), 3)
call_9380 = relay.TupleGetItem(func_8476_call(relay.reshape(const_9377.astype('float32'), [540,]), relay.reshape(const_9377.astype('float32'), [15, 12, 3]), relay.reshape(const_9378.astype('float32'), [1, 12]), relay.reshape(const_9379.astype('uint16'), [225,]), ), 3)
func_349_call = mod.get_global_var('func_349')
func_354_call = mutated_mod.get_global_var('func_354')
const_9397 = relay.const([-8,10,10,4,7,2,-7,10,6,6,5,10,3,2,-9,-7,-4,4,-9,9,-10,1,-7,5,-2,1,6,7,-7,7,6,5,-10,-3,7,6,4,-5,8,-4,3,-10,-7,10,-5,-2,-10,-10,-5,-1,4,10,-5,-9,-6,-7,-8,-10,3,-1,-7,-1,9,7,-4,-6,6,-6,-2,-7,-8,7,-1,-5,7,5,10,-10,5,4,-8,8,8,-6,-9,-7,5,-6,-9,1,8,1,-1,-8,-10,6,3,-1,-9,1,8,-6,-2,-7,3,8,-5,-9,9,5,-2,-7,-6,-7,-3,-3,-6,4,-9,-8,3,4,-6,6,-4,5,1,-2,10,4,-10,8,5,-6,5,9,-2,7,7,3,2,9,2,2,3,-7,2,10,7,2,-10,1,-3,9,-2,3,-10,9,4,-4,-7,9,-8,7,-3,-9,-9,2,-3,-1,-1,8,5,-3,-9,3,8,7,10,-3,-2,-3,-5,10,8,-2,6,-2,9,9,2,6,-7,-8,-9,-8,-3,10,10,5,-5,-6,-9,1,2,6,5,6,6,-9,-2,4,9,-3,-7,-4,-7,3,-9,-4,8,6,3,-5,5,4,10,3,5,8,-6,4,5,1,-4,4,6,-5,-4,-8,6,-6,-9,8,5,-5,10,-6,9,-8,2,-4,6,5,-2,8,-4,-4,3,10,8,1,-7,5,-2,-10,7,-1,3,-2,1,-3,-4,2,9,-5,7,6,-1,-9,-4,-7,3,3,-6,-3,4,-3,-6,-6,-7,3,7,10,-10,10,10,-4,-7,-10,-3,1,-10,-6,9,3,-2,-2,6,4,-10,10,4,-2,-5,4,-5,7,-9,-4,-4,-8,3,-5,1,5,-6,3,2,-2,8,-5,1,2,5,-10,-5,7,-10,7,2,5,8,7,-5,-7,5,8,5,7,8,-1,8,10,-8,1,8,5,6,-6,-3,4,6,-5,1,-1,1,-1,7,9,6,-5,-6,2,6,-10,2,6,-5,-1,5,7,-3,7,8,7,-5,-10,-5,-2,-2,-10,8,4,-9,2,-6,-1,7,-1,3,-9,-10,-1,3,8,8,10,5,3,-9,-9,-4,-4,-8,6,-2,-2,-5,-9,-6,2,6,4,-7,7,-2,1,-7,-6,1,-8,8,5,-3,-10,3,7,-5,3,7,-8,-6,-4,-7,10,4,-10,8,-6,2,-1,7,8,-8,3,-1,-4,-3,2,3,-7,1,-9,-5,-1,-10,-3,2,-10,2,-8,6,8,2,-1,-3,2,-8,-3,8,9,8,-5,-3,3,-8,-6,4,-8,-5,1,-9,-2,-8,1,10,-3,2,-9,3,-10,-2,7,-2,4,6,-9,-2,4,-7,3,-5,-4,-4,-1,6,10,-10,5,4,1,-7,-6,1,-9,7,6,8,-8,-4,1,-10,9,10,2,-5,3,-5,-1,9,7,-1,7,-4,6,-3,7,10,3,-9,-3,2,-6,-4,-5,6,8,-4,9,-9,-5,3,-6,-9,-2,-6,3,-10,-4,8,7,3,3,2,7,-8,4,6,4,-10,4,-1,5,5,-6,-1,7,8,-3,-4,2,3,-3,5,-4,6,-3,2,10,7,2,-7,-2,-9,-5,-5,6,2,-7,-9,-4,-9,-3,2,10,-9,7,-1,1,6,-4,-5,-9,10,-4,8,-7,4,10,5,-7,-2,10,-7,-5,9,4,-10,10,2,10,-5,-9,-8,7,6,-6,2,2,-1,2,4,5,-10,5,-1,2,-3,5,7,-3,-9,3,-8,-1,-10,10,-1,-10,-10,-3,-4,-6,-5,8,-4,8,3,5,4,2,-10,-10,5,-4,-8,7,3,9,-6,-1,-2,-6,-10,-8,-8,2,3,1,-3,5,1,3,5,1,1,-4,2,-9,2,9,-10,-7,3,10,-10,-7,-7,4,-2,-3,-6,-7,-8,1,6,7,-10,-8,2,-1,5,5,8,-3,-2,-5,-5,5,1,-1,-7,-4,5,-2,-1,9,-10,-7,-4,1,7,2,-2,-5,-6,-1,-7,2,8,6,8,5,-2,8,-3,9,7,-3,-2,-2,-5,1,-10,1,-8,7,-4,4,5,1,-3,9,6,10,8,-6,9,-4,-10,-6,2,4,6,-4,-2,-10,-7,-8,10,-1,-2,-1,6,-9,-10,7,-8,2,9,-6,2,7,-6,-2,-2,5,2,6,-1,6,-10,7,-4,-4,4,-5,8,6,8,2,-5,-6,3,6,-5,-9,-5,-2,5,3,8,8,9,-1,3,9,-10,-4,-6,-9,5,7,4,1,7,-1,-2,-2,2,-8,-9,-3,-1,-2,-9,10,-10,-4,-6,4,-6,8,-3,-1,-6,-9,7,3,-9,4,7,2,1,-2,10,8,-2,-6,-9,-7,5,7,8,-9,-5,6,7,1,-3,-4,-10,1,-1,4,-1,4,-9,-7,10,-7,-8,-1,3,4,-5,-1,3,7,-8,-3,-4,-4,-9,-3,6,8,-2,-1,-10,-3,5,2,-5,-1,1,-1,-2,-9,7,-10,1,6,-6,8,-4,-3,-4,-5,5,3,2,1,8,-5,-4,-7,4,6,-2,7,7,7,8,-2,9,-9,9,3,1,-2,4,8,7,-7,10,7,6,1,-7,7,8,7,7,5,-9,-3,-10,-8,-6,-6,-10,6,-8,-10,-9,10,-4,-7,6,-8,-10,-5,-3,7,-9,10,7,-5,-4,-7,3,-4,-4,-7,2,-3,-8,3,3,-5,-3,2,-2,3,4,-10,-1,6,-3,4,-2,-8,-9,-4,-10,-7,-5,-3,7,-2,9,-10,6,4,2,-7,-8,5,-3,-10,-9,6,-7,10,4,-5,-5,1,-2,3,4,-8,-2,-10,3,9,-8,-7,-3,-6,-10,2,-7,-9,10,3,-9,-8,4,-7,9,-1,3,9,5,-5,-6,2,-9,-4,-2,-5,-10,3,3,10,-6,-7,9,4,-1,10,-5,-5,-3,3,6,6,5,9,-9,-9,2,-5,2,-6,8,4,-10,8,-6,3,-3,9,10,5,10,6,10,6,3,-6,-10,6,9,-7,7,10,-9,-7,10,-8,-5,-4,-8,-6,-2,3,5,4,-5,1,-3,3,2,10,-3,-2,-5,-3,7,-5,2,-3,-9,-2,-1,6,6,5,3,-9,6,-5,10,-3,7,-7,7,-7,8,9,-2,3,-8,7,-4,8,-10,8,-2,10,-2,-8,9,-3,5,-8,9,-7,10,8,10,1,-8,-1,-3,-2,8,-1,-7,5,8,-9,5,-6,9,8,-10,9,-9,10,1,-6,-2,-7,-5,1,6,-2,7,7,-4,5,-5,5,5,7,-9,-7,1,-2,-6,2,4,-4,-4,8,7,5,8,-5,5,-8,-6,5,-9,-6,1,-7,-1,-7,2,-4,-9,-1,9,9,-10,8,2,-3,-2,3,6,10,1,-2,-5,3,7,10,-4,10,5,-9,-5,5,-3,3,-10,-5,-2,-5,-7,-8,6,2,6,1,-4,-8,5,6,-6,5,4,7,1,1,-4,-4,-9,-8,10,8,-2,-3], dtype = "uint64")#candidate|9397|(1320,)|const|uint64
call_9396 = relay.TupleGetItem(func_349_call(relay.reshape(const_9397.astype('uint64'), [11, 12, 10]), relay.reshape(const_9397.astype('uint64'), [11, 12, 10]), relay.reshape(call_9376.astype('uint16'), [225,]), ), 5)
call_9398 = relay.TupleGetItem(func_354_call(relay.reshape(const_9397.astype('uint64'), [11, 12, 10]), relay.reshape(const_9397.astype('uint64'), [11, 12, 10]), relay.reshape(call_9376.astype('uint16'), [225,]), ), 5)
output = relay.Tuple([uop_9370,call_9372,const_9373,var_9374,call_9376,const_9377,const_9378,const_9379,call_9396,const_9397,])
output2 = relay.Tuple([uop_9370,call_9375,const_9373,var_9374,call_9380,const_9377,const_9378,const_9379,call_9398,const_9397,])
func_9400 = relay.Function([var_9361,var_9374,], output)
mod['func_9400'] = func_9400
mod = relay.transform.InferType()(mod)
mutated_mod['func_9400'] = func_9400
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9400_call = mutated_mod.get_global_var('func_9400')
var_9402 = relay.var("var_9402", dtype = "int8", shape = (14, 6, 15))#candidate|9402|(14, 6, 15)|var|int8
var_9403 = relay.var("var_9403", dtype = "float32", shape = (448,))#candidate|9403|(448,)|var|float32
call_9401 = func_9400_call(var_9402,var_9403,)
output = call_9401
func_9404 = relay.Function([var_9402,var_9403,], output)
mutated_mod['func_9404'] = func_9404
mutated_mod = relay.transform.InferType()(mutated_mod)
const_9892 = relay.const([[[6,-1,4,6,6,-7,1,8,-7,8],[2,2,-5,2,10,1,-1,-10,8,9]],[[4,-1,-1,10,9,1,-9,-7,-4,10],[-4,-7,-7,9,7,-9,1,-7,-10,8]],[[8,1,6,4,6,1,6,4,-9,9],[1,8,-2,4,-3,-3,6,8,1,-2]],[[-5,6,5,5,5,1,-3,-7,5,9],[8,8,-6,-5,-8,6,2,-5,4,-2]],[[-7,2,-5,7,2,9,-7,-1,-5,10],[7,-7,7,-7,-5,9,-3,1,2,7]],[[5,-2,-3,5,-3,-1,2,9,-1,2],[5,-7,-2,6,8,6,1,6,-4,2]],[[-6,6,-1,9,1,-10,-1,-7,-7,7],[-10,9,-4,3,-5,-3,-8,-1,6,-2]],[[9,5,9,7,7,-1,8,8,6,7],[-8,4,-1,-6,-5,4,-10,-6,-1,5]],[[6,6,-8,5,8,7,4,2,6,-10],[6,-5,-3,5,5,-3,-8,6,-5,-9]],[[-4,-9,-8,2,10,-5,8,-5,2,-6],[-2,9,-7,-5,5,-5,2,7,-4,-4]],[[-3,-3,10,3,-7,-8,-7,8,-1,8],[9,-4,7,9,-2,-8,-3,-7,8,-4]],[[10,-6,10,-3,-9,8,4,6,-5,3],[-1,4,1,-6,5,5,-3,-4,-7,5]],[[-10,3,-7,3,6,-1,6,-1,-9,5],[-7,9,3,5,2,7,3,4,-1,-5]],[[-5,-3,4,-8,-9,6,5,-7,9,-10],[2,-3,-9,6,-3,6,9,-9,-3,5]],[[9,-9,-9,5,-8,10,-2,4,7,-1],[3,8,-5,7,3,-10,-5,9,7,1]],[[6,-5,4,10,-1,2,6,-10,-9,1],[-8,4,-3,-7,-6,-6,-2,3,-2,7]]], dtype = "uint32")#candidate|9892|(16, 2, 10)|const|uint32
var_9893 = relay.var("var_9893", dtype = "uint32", shape = (16, 2, 10))#candidate|9893|(16, 2, 10)|var|uint32
bop_9894 = relay.maximum(const_9892.astype('uint32'), relay.reshape(var_9893.astype('uint32'), relay.shape_of(const_9892))) # shape=(16, 2, 10)
func_3702_call = mod.get_global_var('func_3702')
func_3707_call = mutated_mod.get_global_var('func_3707')
var_9901 = relay.var("var_9901", dtype = "int64", shape = (1, 448))#candidate|9901|(1, 448)|var|int64
const_9902 = relay.const([7.997832,-1.275218,4.914546,-5.696085,-3.988533,3.493318,-5.000825,-3.225325,8.132824,-2.701813,-4.847614,3.959378,-7.210942,-2.169105,8.375738,6.424356,-6.072697,0.519929,-4.226492,-1.122462,6.043225,6.978967,-0.553723,-8.539020,1.998961,4.651976,0.993605,-4.606105,4.914918,-2.288370,-1.722415,7.981100,4.527572,-0.967621,-0.263146,-5.661100,-2.235116,2.854133,9.498921,2.900313,7.398421,-2.077004,4.475714,-0.951201,3.387024,6.229859,-3.599007,3.570660,-7.870103,0.593102,-7.652367,-8.316367,5.370559,0.534269,4.993615,0.868828,9.027052,-1.513786,-1.670905,5.568997,3.875080,-2.175259,8.282329,1.400842,5.651039,-7.010831,-6.136070,1.480115,9.364758,8.497647,5.952600,9.949460,-3.558251,6.382608,-2.956699,5.384337,9.064125,7.166462,2.565359,-6.462272,-1.570794,-0.623946,-0.535316,-0.813008,8.056454,-4.570378,1.877056,4.490623,3.458044,-7.015791,-4.045339,4.583631,3.812151,-5.284901,8.310810,-7.392700,-1.061036,8.597088,-4.085142,-2.987594,0.165834,-4.018841,-0.638123,-6.931984,-5.724039,0.399733,-7.326491,-6.034645,1.219399,-9.564619,-0.237643,-4.894393,-9.859527,5.588800,-5.199345,-8.531101,-4.512392,-7.568493,-7.805526,1.112403,7.677481,6.454922,7.138314,-4.437720,8.063336,-3.914599,8.746040,-4.172807,-4.847559,-6.009200,1.993639,-1.968101,2.089993,-5.472623,0.752290,-4.144607,-7.046523,0.452371,0.037537,-6.268891,-5.675603,-7.844489,-2.448520,2.915801,-4.698332,2.499731,-1.270916,-8.170584,-6.333118,-4.749049,-8.159363,-6.459442,-6.016617,-0.404692,5.247397,-7.536262,7.293142,5.973103,8.113571,-6.205881,-7.820899,1.913174,2.014209,-5.618057,-7.645057,-0.868986,8.921478,7.801762,-0.554199,-2.668822,8.751203,2.940079,4.908754,-5.025019,-2.769253,1.065127,-3.927431,2.492705,-6.447219,0.800804,-9.784116,2.539647,-9.488457,-6.392050,-7.140602,7.886192,3.490287,0.907568,3.335762,-5.671627,-5.254746,1.065614,-3.916964,9.407624,-9.401782,-6.256557,-8.092636,6.028427,-6.393992,7.851427,-9.839229,-7.481881,1.252112,-0.977653,1.920242,-6.351431,-1.128619,-8.558491,7.719696,1.262619,-5.953127,-0.675973,0.253647,-8.266459,6.474290,3.141983,-0.974109,-6.767699,0.938894,-7.764192,4.798598,-9.779231,-8.594067,-2.287948,-6.429304,-5.706791,4.067717,0.057204,-9.034413,1.079415,9.754999,3.571057,-0.063751,-8.866607,-7.186255,2.508165,4.293005,-6.977551,-8.443044,8.782819,-4.392016,-1.188809,2.939041,7.706019,1.878347,6.128192,1.024117,-4.197205,-1.392931,2.385812,2.922920,-0.582699,-8.954894,2.472215,-4.850720,-2.680896,-6.265947,-3.317686,-6.203155,3.659116,-2.696186,1.110478,0.493783,-1.450292,-8.336963,-4.914886,-5.463087,-9.499594,4.623863,7.747162,4.115916,1.586550,-4.547447,3.669614,0.447235,-6.017553,6.780293,5.442518,5.432510,9.123018,3.515632,-7.311678,-4.565280,-5.250537,-9.923214,6.026898,2.782295,1.961841,0.513093,9.225203,3.036885,-3.127442,3.860590,1.532715,1.866581,-7.925733,-4.822722,-6.809357,5.911972,5.087921], dtype = "float64")#candidate|9902|(300,)|const|float64
const_9903 = relay.const([0.827466,-5.010623,7.356465,2.885986,-0.528736,-6.233243,9.960610,-0.430657,-3.619133,1.543144,4.880372,1.093306], dtype = "float32")#candidate|9903|(12,)|const|float32
var_9904 = relay.var("var_9904", dtype = "uint16", shape = (225, 1))#candidate|9904|(225, 1)|var|uint16
call_9900 = relay.TupleGetItem(func_3702_call(relay.reshape(var_9901.astype('int64'), [14, 16, 2]), relay.reshape(const_9902.astype('float64'), [300,]), relay.reshape(const_9903.astype('float32'), [12,]), relay.reshape(var_9904.astype('uint16'), [25, 9]), ), 1)
call_9905 = relay.TupleGetItem(func_3707_call(relay.reshape(var_9901.astype('int64'), [14, 16, 2]), relay.reshape(const_9902.astype('float64'), [300,]), relay.reshape(const_9903.astype('float32'), [12,]), relay.reshape(var_9904.astype('uint16'), [25, 9]), ), 1)
output = relay.Tuple([bop_9894,call_9900,var_9901,const_9902,const_9903,var_9904,])
output2 = relay.Tuple([bop_9894,call_9905,var_9901,const_9902,const_9903,var_9904,])
func_9908 = relay.Function([var_9893,var_9901,var_9904,], output)
mod['func_9908'] = func_9908
mod = relay.transform.InferType()(mod)
mutated_mod['func_9908'] = func_9908
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9908_call = mutated_mod.get_global_var('func_9908')
var_9910 = relay.var("var_9910", dtype = "uint32", shape = (16, 2, 10))#candidate|9910|(16, 2, 10)|var|uint32
var_9911 = relay.var("var_9911", dtype = "int64", shape = (1, 448))#candidate|9911|(1, 448)|var|int64
var_9912 = relay.var("var_9912", dtype = "uint16", shape = (225, 1))#candidate|9912|(225, 1)|var|uint16
call_9909 = func_9908_call(var_9910,var_9911,var_9912,)
output = call_9909
func_9913 = relay.Function([var_9910,var_9911,var_9912,], output)
mutated_mod['func_9913'] = func_9913
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9928 = relay.var("var_9928", dtype = "float64", shape = (9, 10, 2))#candidate|9928|(9, 10, 2)|var|float64
var_9929 = relay.var("var_9929", dtype = "float64", shape = (9, 10, 2))#candidate|9929|(9, 10, 2)|var|float64
bop_9930 = relay.divide(var_9928.astype('float64'), relay.reshape(var_9929.astype('float64'), relay.shape_of(var_9928))) # shape=(9, 10, 2)
uop_9938 = relay.cos(bop_9930.astype('float32')) # shape=(9, 10, 2)
bop_9950 = relay.bitwise_xor(uop_9938.astype('int8'), relay.reshape(bop_9930.astype('int8'), relay.shape_of(uop_9938))) # shape=(9, 10, 2)
uop_9964 = relay.exp(bop_9950.astype('float64')) # shape=(9, 10, 2)
output = uop_9964
output2 = uop_9964
func_9975 = relay.Function([var_9928,var_9929,], output)
mod['func_9975'] = func_9975
mod = relay.transform.InferType()(mod)
var_9976 = relay.var("var_9976", dtype = "float64", shape = (9, 10, 2))#candidate|9976|(9, 10, 2)|var|float64
var_9977 = relay.var("var_9977", dtype = "float64", shape = (9, 10, 2))#candidate|9977|(9, 10, 2)|var|float64
output = func_9975(var_9976,var_9977,)
func_9978 = relay.Function([var_9976,var_9977,], output)
mutated_mod['func_9978'] = func_9978
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10217 = relay.var("var_10217", dtype = "float32", shape = (5, 1, 3))#candidate|10217|(5, 1, 3)|var|float32
uop_10218 = relay.log10(var_10217.astype('float32')) # shape=(5, 1, 3)
output = relay.Tuple([uop_10218,])
output2 = relay.Tuple([uop_10218,])
func_10225 = relay.Function([var_10217,], output)
mod['func_10225'] = func_10225
mod = relay.transform.InferType()(mod)
mutated_mod['func_10225'] = func_10225
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10226 = relay.var("var_10226", dtype = "float32", shape = (5, 1, 3))#candidate|10226|(5, 1, 3)|var|float32
func_10225_call = mutated_mod.get_global_var('func_10225')
call_10227 = func_10225_call(var_10226)
output = call_10227
func_10228 = relay.Function([var_10226], output)
mutated_mod['func_10228'] = func_10228
mutated_mod = relay.transform.InferType()(mutated_mod)
const_10263 = relay.const([[[-7.361437,5.479482,9.365223,6.816885,4.438735,-2.918582,3.743906,7.013602,6.579447,-2.030862],[8.073066,-5.819472,-3.159411,0.049774,1.949301,-9.894633,-1.413940,-1.165575,-1.544647,0.741339],[7.445479,-7.194071,9.924974,9.643795,5.242742,-5.397415,7.610983,-1.983622,8.371910,-9.379831],[0.140247,-4.310167,3.438976,8.739309,8.713787,4.476660,-1.920721,6.882609,-3.961428,-5.484919],[-2.195382,-4.297112,-1.057434,-9.783139,-6.061642,-0.989243,4.273787,9.451886,3.319268,-0.246387],[-0.767473,2.469251,7.485819,-3.106297,-2.512528,1.903589,0.936062,-3.027358,4.042781,9.754528],[1.932751,6.185949,8.981319,0.765507,9.316914,6.231755,-9.318899,-8.392308,7.161082,1.599877],[6.098621,3.428665,-7.508700,-5.375739,-9.590115,5.834429,8.116424,-6.776122,4.088687,9.022386],[7.184881,-2.501710,-7.128891,8.859931,4.530310,1.817558,-0.148889,-8.689258,-3.028512,-7.721932],[-0.059966,-6.221271,-3.615115,-4.128305,0.184899,-7.905979,-1.919467,-7.714746,4.091740,6.331861],[-4.636722,3.332263,0.916296,9.332590,8.469520,-2.788031,6.374789,2.694580,0.691539,7.357071],[-5.013235,8.044740,8.496658,3.306073,5.746406,6.810563,2.330959,-2.389046,-2.776546,-0.117516],[1.759849,-0.723258,5.409515,-5.344517,3.884832,9.233230,1.501160,2.320810,-8.529004,5.099617],[7.882794,9.225366,-7.782465,8.699026,0.757061,-3.707814,-2.656903,7.576631,-8.189687,-3.591199],[-1.912141,2.763476,-8.503531,-2.732564,1.682307,-9.604848,-8.484965,9.549588,-4.093154,-1.222026]],[[-9.689485,-8.025950,8.793820,1.368819,-3.781307,7.877789,7.233787,-2.790203,6.915310,1.321224],[8.547428,6.962011,1.234578,-2.801490,4.567183,-6.374604,5.459307,-6.356224,-1.726890,-3.310310],[2.035788,5.145216,5.891646,-6.453949,-1.571738,1.926871,-4.781489,-3.623066,-0.300716,2.042357],[8.248952,1.630740,-2.525962,5.310568,3.232058,6.708193,5.617771,-7.039713,2.849415,-7.451001],[-9.617912,8.859973,-7.849054,-9.988105,-1.227153,4.237202,7.524636,-7.598137,-3.881676,7.774737],[7.115424,0.345534,1.639875,4.069696,-2.748477,1.770944,-3.616540,5.233161,-5.395141,0.758983],[6.993049,-5.505623,2.952969,5.406007,-4.484048,-0.777035,7.714342,-3.803166,1.872880,9.829749],[1.525548,-2.502817,3.909267,3.638480,6.942824,-8.505185,1.703726,-4.321381,4.367612,-3.325155],[-5.706763,-1.150873,-0.981083,-5.441832,-4.273336,-6.508063,-2.178439,8.399547,-6.403201,1.540900],[0.898580,7.460491,-0.059174,-0.386931,7.383055,7.206478,5.877586,5.599167,5.311067,7.531259],[-2.313910,8.304554,-5.512689,-3.214653,3.671199,-4.844443,-5.939770,0.703329,2.891907,-8.228952],[8.140879,-1.656909,5.687363,-4.693994,-8.649074,3.968884,1.251352,8.388067,3.016691,1.578670],[-4.320685,-7.226462,4.986905,3.309255,6.580724,4.816761,-1.453069,9.739853,2.457028,-3.901239],[1.400827,-8.726686,-7.588292,-3.302734,-5.163201,7.285872,0.006995,3.694330,0.577863,-8.281618],[-0.887461,7.337020,2.765433,4.830227,2.181739,-2.977389,8.896926,6.460954,4.264322,1.370212]],[[7.898097,-5.403036,-3.487986,6.162850,-6.634296,-1.198105,8.378857,8.044298,-5.543951,-4.773043],[-7.415889,-7.431272,0.067561,-6.167366,0.374119,-7.454334,-1.429239,-9.407048,-1.795474,-2.441503],[9.024033,-8.267320,7.337929,7.431179,-4.265531,9.769787,7.247352,-2.644298,1.113548,9.622430],[-6.058899,-6.848547,-4.115739,-6.166751,-2.106573,7.252602,3.311915,2.848482,-1.565612,8.285386],[-3.026656,4.197428,-2.316778,-7.488251,-9.471533,2.345150,-0.872532,3.733225,-0.543246,6.652650],[4.851144,-9.613609,-0.503307,7.269968,-1.167742,9.386068,1.046056,-7.959324,-8.049343,3.212536],[-0.306816,-4.433953,-4.860172,1.685803,3.976247,-9.900012,-8.493998,0.314241,-8.387520,8.181685],[8.241542,3.233990,3.681436,6.877681,-6.106423,0.032249,4.869882,0.580266,7.208042,-2.931193],[-2.631451,0.649186,6.685463,3.493078,7.689451,-0.430426,-3.971048,8.308731,-8.245223,3.498248],[-5.489036,0.918628,-6.364842,9.759089,-0.654575,-7.848086,-3.327485,6.867520,6.681287,4.509729],[2.300884,1.015337,7.698472,0.379632,5.696790,0.315388,6.913585,0.621204,4.447400,-2.469390],[-6.306222,-3.584642,-5.174484,-7.146478,8.427041,6.182852,-7.456994,-8.154047,0.275508,4.608587],[-4.806489,-2.919947,5.450067,-9.712032,7.103623,-7.767231,0.742918,-1.633578,-0.995660,1.238958],[3.280814,-0.732387,-1.056993,8.958436,3.107721,-8.790377,2.231458,0.842633,3.107257,-4.366467],[-4.126742,-0.276635,0.779221,-2.577677,-3.664149,2.960806,-3.065597,1.015554,-9.154727,-9.496766]],[[9.896982,-1.721127,-8.433636,0.948109,6.236659,-9.072587,5.044277,7.327390,4.938041,-4.491331],[-4.717159,2.531017,-7.468601,7.909404,-7.105637,-0.006101,-4.698046,-1.688070,-0.354996,-3.070157],[5.174706,-0.555105,-6.304615,-9.170063,5.849888,0.681184,-9.500342,-6.361389,6.825841,-9.504887],[2.705042,2.440093,1.592011,-4.266479,7.667349,8.924966,4.819476,9.026400,8.188862,-7.674563],[8.609136,-0.729261,-3.334079,-5.679657,-8.331177,2.837575,0.297996,-6.876242,6.013310,-9.536668],[9.111031,6.794817,0.496960,-7.488335,-7.942249,6.664751,-4.405125,-8.291422,-4.019028,-1.075114],[6.701262,8.992496,-0.744961,1.567706,-3.042893,2.048895,6.969990,6.419029,2.405883,2.515623],[-1.271115,6.174492,2.704944,3.922993,-2.102411,-0.025571,-9.182066,-7.465480,9.741197,-8.300399],[-8.752810,-2.165117,-0.729788,-4.882072,4.092705,-2.445784,8.791318,5.039270,6.698933,-8.166709],[-3.027561,6.604238,-0.093158,-9.444089,6.976400,-2.556867,-6.557073,7.754068,-1.874086,-8.780924],[9.385361,3.080806,5.892630,7.224654,1.571688,-9.100451,5.672688,-4.239537,-4.966376,9.350874],[7.621810,2.887084,-9.803886,8.806299,-3.800940,6.448116,-5.654222,-8.081890,6.374260,-9.347209],[-2.617325,-2.557818,-0.766916,7.338117,8.708993,-3.450713,-0.162595,-1.308855,-1.444888,0.864200],[-9.031196,-1.274997,8.048473,-3.472436,2.143462,-9.938668,6.941487,5.510108,9.218350,-1.534483],[2.814593,-4.859952,-2.765867,3.097479,-5.841330,-8.415693,2.506352,4.207441,2.799672,0.051753]],[[-8.946477,-7.643983,-3.578793,2.872141,1.704816,1.526833,-0.306022,-3.250557,-4.195833,7.790246],[5.425517,5.784168,-2.544821,3.041146,-6.301708,-2.377647,-4.515058,6.742763,-4.572346,4.177650],[-4.921074,5.084810,-1.534496,-7.664797,7.603258,0.002903,0.773645,7.398124,2.810278,5.341584],[9.541898,-6.241997,6.746674,-5.231113,-2.976444,5.005560,-8.085765,7.919610,-7.592680,-9.657975],[8.146573,-8.538750,-6.801570,-5.317157,0.543895,-1.479593,-5.477571,-6.975666,-8.994151,6.687354],[-9.117374,5.589526,6.769468,4.281920,-6.075340,7.338821,5.669041,-6.493375,8.516310,9.014309],[3.263470,7.298239,-6.554305,2.087588,8.097359,6.943746,3.929687,-6.901143,4.915471,-8.736530],[4.017511,7.866265,-6.944370,3.592139,9.557957,-8.314831,-4.605785,-0.264933,8.964577,5.930576],[-4.173214,8.812512,4.789604,3.596198,9.732086,1.943536,9.528519,-3.479098,-6.293027,-0.524467],[-0.039951,-6.823546,-0.050107,-7.427510,-0.208089,-7.732295,-9.089885,-8.479011,-1.627047,0.857056],[-7.332964,-1.490445,1.066098,5.350475,-7.976523,3.476027,-5.440197,3.555210,-5.015769,-7.953665],[3.142667,-3.105991,-4.425191,-0.132240,-9.615916,4.661489,-9.919406,-7.742380,-0.963669,5.435150],[0.703519,0.763032,9.739295,5.719125,-6.470235,-4.173086,-6.816170,-5.687032,-4.635397,0.644816],[-0.052866,1.689077,4.737924,-2.338749,4.348046,-6.860529,9.254279,-0.072951,3.976045,-2.309859],[1.204270,8.997792,4.241218,2.860256,-8.935031,-4.086562,8.675125,3.698859,-4.498045,-3.853606]],[[-0.711344,-1.544876,-4.465282,-7.785112,-4.819708,-9.770162,8.710644,-1.783770,5.888148,-1.878739],[-2.047401,-9.332348,-8.476376,-4.328799,4.221332,-5.301883,-2.365082,9.615500,5.763594,-4.935736],[3.082147,-2.503476,-9.611301,9.571219,-5.999152,-1.867374,7.128995,-3.888145,-7.470355,-8.988058],[3.998442,0.569037,5.378635,-6.937949,-2.315154,0.341149,7.513916,4.588122,-4.496973,6.268760],[-6.301607,8.694763,-1.318713,-3.392201,6.172000,9.453187,6.627726,-2.530480,0.420175,-4.251402],[0.429770,5.079182,9.971738,-7.364769,-2.611007,-0.727133,2.459975,-3.931213,7.445997,4.066182],[9.286179,4.293640,0.069106,2.602711,-5.998245,4.677867,8.103738,3.599347,7.126465,-1.543808],[4.710241,-8.464979,7.695057,9.431742,4.835000,4.780020,9.520787,-9.607465,-6.829202,4.670292],[0.691250,-7.922950,-3.366555,7.802588,6.802522,0.478148,-0.554889,-9.269801,-2.067710,-6.104466],[-7.369926,-7.216121,-6.949975,-5.194354,-0.083257,8.914355,-0.758522,1.812734,4.594564,-8.583421],[-8.040335,-6.490033,-3.616424,-2.849429,-5.160193,-8.404269,-7.767538,-8.920501,7.754981,9.736719],[-8.647504,7.887608,-9.536376,9.284526,3.622018,7.087974,7.042538,-8.895198,-8.421428,-6.420666],[1.978038,5.684309,7.471339,-4.913124,-8.356740,8.359463,3.964178,-8.719149,7.785289,4.113663],[1.022221,-7.023984,-7.471765,-4.361865,-6.327050,0.870559,-7.070948,7.561892,-0.076518,-8.383438],[-5.484010,-9.140451,8.782623,1.511818,-4.826693,8.764717,1.649766,2.924480,4.056018,-6.020917]],[[-5.690972,5.868385,-9.152901,9.997237,1.068139,-1.631292,0.667110,5.894569,3.935721,6.032420],[2.874457,9.805765,-0.695422,7.020123,2.318414,2.332159,1.855130,-4.418312,-6.031657,1.874634],[8.856441,6.869839,-5.205656,5.755711,0.856974,0.707592,-6.500662,-1.492224,9.618812,-8.138989],[4.965642,3.882084,-8.770743,1.181611,8.712659,-5.215395,-3.246069,5.374113,-3.614960,-5.953706],[3.288534,8.696274,-8.159834,-5.206999,8.080909,-3.593255,5.193527,9.716390,9.241648,-0.765196],[0.880946,-8.991677,-3.078434,-1.906511,-3.045009,-5.857246,2.454476,9.073138,2.191219,1.797551],[-3.441453,-1.114697,5.272103,-8.787476,-9.509769,7.216691,7.793280,7.284781,5.317306,5.568792],[-3.211320,7.668961,7.238789,7.000381,1.015746,5.530063,2.068147,2.864692,5.589955,0.392480],[-0.115928,-4.804867,-1.135451,7.381385,1.542028,-1.917111,-7.773013,1.985618,-8.314678,4.287503],[-6.915171,-1.602593,-6.851945,-6.209430,4.689132,4.568238,9.335531,0.301694,5.440135,2.418154],[1.578560,-9.358693,-0.824181,6.468644,-3.468016,-8.185393,1.490130,-2.304596,-9.342364,-7.159348],[2.745029,6.210879,0.609385,-7.122218,9.011161,9.132389,7.080917,-6.573345,-0.397370,1.676388],[-2.832762,2.708941,-1.388769,5.924251,-5.131362,-4.246853,7.355308,-2.479438,-3.602628,3.400936],[7.721143,9.955671,-3.493008,-0.654214,0.428073,-5.678862,8.846506,-6.659067,8.912896,-3.995052],[2.162024,8.236995,-0.643749,7.034733,3.188613,-0.439182,1.154349,8.725377,9.771045,-7.067068]],[[7.550769,6.151238,-8.559453,-1.939238,0.171582,-6.686067,4.251906,-0.609157,5.585054,7.462868],[-3.711620,1.198878,0.341403,-0.854376,-4.530829,8.745047,2.191190,-4.141117,-4.596029,0.421620],[1.488099,-0.091936,-2.533414,-0.038685,-5.142740,-2.815405,4.845702,6.891944,-0.698874,-0.185474],[-0.058371,5.397549,-3.864194,-7.997885,-5.398465,-9.579023,7.115675,7.753304,5.342028,4.523657],[0.762569,8.005783,-7.042981,8.574611,-0.214117,6.853767,5.274473,-7.618597,9.917754,4.354768],[-2.776123,9.006744,-3.537449,3.693002,2.809737,-9.652476,-2.408493,9.472386,-4.367162,-2.071840],[-8.536518,7.309266,-2.044379,7.554280,-6.711049,9.027885,2.185842,-1.900774,9.357773,8.519490],[5.678687,4.496419,2.187302,-1.818659,7.341555,-7.029875,-4.217481,-9.964515,1.976219,-8.297642],[-9.190930,7.299543,3.073411,6.936422,5.591168,0.389463,-3.322657,8.350561,6.796277,4.785929],[-1.219998,4.415033,-6.609463,8.998606,3.232145,3.473618,9.956466,9.599461,0.220786,-4.943802],[-5.644756,7.939911,-2.272856,-6.943139,-5.149722,0.617806,-1.194033,9.201308,-9.939426,-7.098440],[9.466642,0.662884,-0.553679,7.631868,2.056231,3.980278,4.297010,9.123079,3.679809,7.880744],[0.042981,-0.610577,7.718610,-4.366737,-6.494979,-3.155260,9.647397,-5.267635,-0.487786,9.493823],[6.890602,1.477893,0.630411,7.743895,0.374684,-7.833873,9.898968,-8.082811,-3.075406,-8.316040],[2.962309,-3.205405,-8.164269,4.782334,-9.889856,-5.983157,3.791377,-7.204672,-3.037550,1.816582]],[[6.997198,6.870284,-7.828002,7.772480,-2.103910,2.694573,-6.039932,-0.620218,-8.081170,-3.857095],[-8.339971,2.779548,-0.185873,-4.694184,5.102462,-8.920250,2.941896,9.460030,5.587728,9.593811],[-7.442489,-8.538970,-5.501231,5.796641,-0.515603,-3.056408,-6.747425,-5.974579,0.245162,-3.360297],[-3.917642,3.455522,-0.587543,1.083249,-6.287728,3.247287,5.614703,7.939894,4.971583,-7.870212],[-7.677386,-4.655547,-7.983512,-3.283570,-2.289470,-4.059296,2.456934,-7.981285,-9.237208,-7.500980],[-9.911557,7.236122,2.812938,-9.756178,4.702443,-3.085695,1.734625,8.572659,2.556543,1.396272],[-9.856325,-0.074838,-2.375981,7.025406,-0.769029,6.626568,2.819629,-2.811788,3.061483,7.915679],[2.231339,8.153706,9.872495,4.317766,-1.475758,-7.441431,-9.693664,-7.455330,4.077665,-1.466392],[9.638379,1.882917,-7.492623,4.691863,-4.403502,3.093719,-4.920150,-4.097663,0.217364,-4.080053],[-9.712557,-8.964588,5.398032,2.883709,-1.371524,-0.125180,5.031848,-8.994093,3.920773,-7.321013],[4.653877,-4.931004,-3.862230,5.949638,-2.926987,1.763172,-7.848140,7.591095,-6.508218,-5.122532],[-2.355422,7.771585,-8.743054,-2.255303,9.794735,3.641483,-5.225974,3.751067,-1.357931,-7.442979],[-4.929590,-7.011811,9.724084,1.077828,-8.244247,-6.812932,-7.799251,8.672726,9.627625,3.252411],[-5.081544,5.307725,-4.878812,5.272957,1.532344,5.507979,1.960078,-5.039407,2.725549,-0.759289],[-6.335715,4.501651,-6.547980,0.480009,-1.084788,9.851800,-2.578463,2.157939,6.420823,2.077548]],[[-8.843079,-5.075501,-7.466632,-8.685338,-9.140602,-0.664421,6.083559,-6.093201,-9.781675,7.547118],[-1.691647,8.873411,-0.563929,6.039230,1.105994,-5.998074,4.130374,2.485322,-2.002061,1.133863],[-3.953531,3.638551,7.907487,-1.320118,1.555771,-0.074363,-4.868674,-3.684606,-0.347352,-0.091991],[5.741254,2.024896,5.267064,-8.554037,-9.522872,7.528549,1.478935,-7.918076,-8.142595,-4.030686],[2.410130,2.077706,-8.947430,-6.455857,7.635469,-6.733253,9.594814,9.145421,-3.691039,-7.551174],[1.231017,-8.535216,-6.132346,-5.170124,0.748903,1.343348,4.662476,-1.124937,-8.713356,6.199669],[4.133254,-9.556539,7.009660,7.291769,-9.859210,7.623238,1.531039,-3.431193,-0.211180,-3.215205],[-5.763808,-3.852487,-3.998901,1.885191,9.569122,-8.703421,9.950945,-9.433489,-2.925606,-1.833738],[3.607824,0.375787,5.079680,1.857670,-6.997797,5.535307,8.993484,-4.880944,-3.933730,-9.838437],[-8.869808,-0.499897,-5.113229,7.662308,0.606391,8.398848,1.429993,9.832653,-9.046051,-4.859951],[5.907884,5.918622,-2.118488,-3.954461,-8.394649,-9.909403,-3.253649,-0.085878,5.598932,8.481104],[4.155720,-7.591468,9.296476,-7.984967,-4.592511,-6.220224,-4.493728,-9.222374,-1.861840,-3.204418],[7.731490,2.966584,0.796455,-2.215012,7.136838,9.824881,-4.277945,4.183953,-5.514396,-1.632878],[3.183491,-6.559640,-3.641282,-4.123490,0.550077,5.743955,3.769587,-3.066920,-6.707399,-5.412686],[9.310714,3.907713,0.872052,9.938161,-3.695262,-6.539440,0.629157,1.315577,6.886834,-5.070059]],[[-9.347369,4.797667,-5.028772,7.587625,6.178728,7.798571,2.813030,-4.430059,2.489252,-5.566259],[3.015871,7.000592,9.146370,2.704101,-7.889006,-7.851144,0.983771,7.342747,2.657872,9.342742],[-5.713441,5.509372,0.050818,-6.121217,-0.570979,-6.656787,5.857052,-5.406349,-5.666063,6.335250],[1.566617,-9.879608,2.017585,-2.928154,-0.303172,5.063706,-9.441282,-1.001380,1.827182,9.575494],[-7.329270,6.075909,8.697627,-4.815816,9.809411,7.697922,2.970364,-3.431108,0.314493,-6.521391],[-1.936449,-3.280421,-7.599804,-2.830671,5.066488,4.031611,5.221778,7.047133,-9.242982,-4.773928],[1.079437,-5.397767,4.740640,0.491790,-3.083130,-6.908401,-4.309207,5.280864,-2.294297,-8.139412],[7.233706,6.958028,-9.585462,-8.467184,-6.487367,9.658386,-2.930194,6.983905,-4.196549,-5.030114],[-1.863086,2.233772,8.224247,2.350464,-6.259806,3.022687,-1.358622,-5.627746,2.062368,3.200570],[8.897915,5.899279,5.422681,-2.126355,4.626444,-9.512913,6.864556,-8.333019,-9.893981,-6.760979],[7.044657,9.036622,-0.543657,1.700142,-5.817146,-6.158180,6.707172,4.522152,-9.578863,-4.946491],[-4.959886,2.694655,-1.430806,-5.771852,4.917187,4.663674,-4.539572,-0.199298,-6.084929,-8.044734],[4.645240,-5.064484,-0.438965,8.068854,8.539403,-9.795098,-0.709292,-1.071424,-2.038945,3.219755],[2.512014,-8.455091,6.045158,7.817501,-1.647308,-6.864908,-9.558546,-5.017315,-1.809877,9.165640],[2.684604,9.262893,3.761130,-9.172203,-7.023288,2.082385,-3.527265,1.062776,0.225351,4.784405]],[[-9.531931,7.829673,6.802480,3.533254,8.220809,1.293952,2.832289,-8.291933,-7.206405,-3.209309],[-8.824622,4.599019,6.617173,1.489882,8.781783,0.298008,-0.009894,-6.842495,-6.141867,-8.311672],[-5.173852,0.669471,-0.145976,-3.252714,-9.181015,-8.863060,-1.899539,-8.443602,-2.709009,-0.614840],[-7.602787,-2.485024,-6.492417,-1.393565,-2.776121,-8.785152,6.452206,-0.076055,3.408436,-6.349068],[6.178992,2.158492,-2.177473,-5.696236,3.468708,-7.657037,-6.063566,-5.564285,6.121698,7.202662],[0.377248,-7.261575,7.646372,3.403926,2.970755,8.976716,-0.746801,5.169950,-2.489027,0.260903],[-3.620600,3.565471,-3.400618,-3.217633,6.265168,-9.026698,8.381753,5.688198,2.529291,-5.200799],[-1.398191,-6.415279,-2.895678,-9.904156,6.422591,-6.748737,7.685512,-7.480971,3.534199,-3.673809],[-0.368701,-6.637130,2.488317,2.679240,-4.944614,-8.603394,0.674765,8.966529,-8.404141,-4.702277],[7.794670,5.183643,-3.733562,7.848439,-1.471016,-4.970803,-0.427833,0.893868,-3.994931,-2.832702],[-5.268782,-2.655669,1.835859,5.864442,0.031779,1.265747,-9.032346,2.968640,-3.844237,-6.119063],[-8.251322,-4.811297,9.259684,9.404832,-3.665842,-8.772055,-3.333029,-6.686218,-5.828299,8.867762],[3.612848,6.261938,3.193680,-4.710443,8.317142,3.806139,-9.830983,-0.193052,7.202444,6.851724],[0.429763,-1.886278,-1.685671,-7.589114,-0.432632,-9.379498,-1.665502,2.811587,1.130925,-1.825389],[-6.096925,-6.199652,6.779013,8.572213,-6.745757,-3.869122,-1.981914,3.067472,4.852796,-0.145750]],[[8.772025,2.118524,-0.751046,-4.393162,-8.870641,-2.654473,-2.810006,5.140327,1.864550,-7.033120],[-1.998641,0.842842,6.100196,4.479601,-1.755999,-9.299399,0.955520,-2.690215,-0.368789,6.012924],[5.095385,1.296993,-4.776924,9.501950,0.372328,-3.488072,-2.409827,8.412308,-7.971953,-4.582220],[-9.864026,3.409961,-7.686303,6.280793,-6.981628,3.434288,-3.645712,4.156727,-0.134657,-1.936548],[-7.694405,8.520321,-3.913135,-5.767492,6.917504,-6.040689,1.940471,3.583654,2.531512,-1.438031],[7.066738,5.504688,-3.795294,8.492237,5.380945,7.091006,-0.120029,-0.750321,4.913901,2.434787],[8.079647,-9.613489,8.631190,-8.663597,-0.603039,-5.009397,-8.896882,0.270005,-7.406318,6.199666],[-5.477649,9.493040,4.988602,1.135179,-8.951137,-8.917227,-3.082779,-5.127439,-8.897240,-1.485628],[5.806165,2.534374,-0.693572,4.948547,5.817339,-5.193434,9.942530,-4.450542,1.852732,2.472679],[-0.495361,2.587341,-4.515749,7.352596,-3.834681,3.388294,-4.958829,-2.165039,2.080317,-2.346442],[-8.253851,-9.619920,-1.939871,9.215906,-6.377521,-1.596330,-3.177862,-0.226449,0.607625,7.266695],[6.517645,-3.224715,8.812824,5.822184,-7.538666,4.428576,-4.233817,-9.223171,-8.207645,7.325180],[-9.418599,-2.523484,8.723765,2.597642,-9.494332,1.970207,4.209435,9.988605,-7.831824,6.529133],[-4.359094,6.952181,-5.688230,-6.874563,2.140861,1.283883,6.778883,-9.466384,-2.697000,9.085634],[7.982313,9.539085,-4.961259,8.347321,1.404352,1.026235,-1.718906,-9.305098,-9.093784,7.161103]],[[-6.603434,3.879217,-9.511392,6.745088,0.359752,5.619148,8.470496,6.783730,-6.854766,-2.746609],[8.435674,0.217676,-0.462165,-2.585273,-0.377813,5.830174,8.229600,-8.023761,-9.936101,-4.106952],[5.921098,-1.881077,-8.106828,-1.499902,7.446772,-3.100476,5.515626,-5.200158,-7.257411,-1.084263],[-2.981816,5.411190,8.984648,-0.083785,2.031468,2.416236,-6.663416,2.961490,-9.755457,1.965802],[-3.201343,-8.190446,-5.409980,-9.367793,-2.362234,7.469654,-8.121621,-9.608527,6.862306,7.828736],[5.570703,7.492860,6.624760,2.854297,-7.299464,4.618888,-1.555631,-7.964854,-3.798481,2.471854],[-3.095356,6.512202,-7.756019,-3.431049,-5.104298,-4.230684,-6.664854,-5.799624,8.670270,0.359913],[-5.461803,-2.810931,8.460111,6.645314,3.077486,-9.484909,-7.849290,-3.378892,4.642178,-6.400503],[5.725539,5.117792,-2.500908,5.988329,6.625837,7.413030,4.479538,2.386084,9.221742,-5.127401],[6.252836,-8.442431,-0.709074,-3.736204,2.140133,-4.981181,-6.420855,-1.983844,1.898465,-0.587415],[4.592385,-0.141603,4.361488,3.687741,8.722269,-9.378853,-6.126419,-9.564223,6.259369,-3.677257],[3.812074,5.351263,-3.361445,-2.591914,5.202050,9.527449,-9.009609,9.144420,1.716776,-2.381371],[-9.013229,5.768504,4.969587,-6.594849,0.318212,8.722791,4.792391,-4.402025,8.067578,3.327132],[4.974898,0.219615,-7.221543,0.926015,0.020826,-1.711614,-4.815427,-9.518813,7.730974,8.981516],[8.040964,2.565762,6.876738,-9.730764,-1.617393,-7.700380,-5.113649,-6.180048,-5.376157,-1.526320]]], dtype = "float32")#candidate|10263|(14, 15, 10)|const|float32
uop_10264 = relay.erf(const_10263.astype('float32')) # shape=(14, 15, 10)
uop_10270 = relay.atan(const_10263.astype('float32')) # shape=(14, 15, 10)
func_6906_call = mod.get_global_var('func_6906')
func_6909_call = mutated_mod.get_global_var('func_6909')
var_10275 = relay.var("var_10275", dtype = "float32", shape = (126,))#candidate|10275|(126,)|var|float32
call_10274 = func_6906_call(relay.reshape(var_10275.astype('float32'), [1, 9, 14]))
call_10276 = func_6906_call(relay.reshape(var_10275.astype('float32'), [1, 9, 14]))
output = relay.Tuple([uop_10264,uop_10270,call_10274,var_10275,])
output2 = relay.Tuple([uop_10264,uop_10270,call_10276,var_10275,])
func_10280 = relay.Function([var_10275,], output)
mod['func_10280'] = func_10280
mod = relay.transform.InferType()(mod)
mutated_mod['func_10280'] = func_10280
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10281 = relay.var("var_10281", dtype = "float32", shape = (126,))#candidate|10281|(126,)|var|float32
func_10280_call = mutated_mod.get_global_var('func_10280')
call_10282 = func_10280_call(var_10281)
output = call_10282
func_10283 = relay.Function([var_10281], output)
mutated_mod['func_10283'] = func_10283
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10789 = relay.var("var_10789", dtype = "float64", shape = (11, 1, 13))#candidate|10789|(11, 1, 13)|var|float64
uop_10790 = relay.asinh(var_10789.astype('float64')) # shape=(11, 1, 13)
func_10280_call = mod.get_global_var('func_10280')
func_10283_call = mutated_mod.get_global_var('func_10283')
const_10801 = relay.const([-0.157441,6.414042,-3.935466,0.002524,-7.887226,3.208529,8.067508,-0.365600,-6.096124,4.802763,-6.466119,-6.870066,6.751774,2.342505,-3.061506,1.736533,9.526604,2.611403,9.075483,0.467313,-7.305908,-3.172911,-3.887592,6.889022,-3.927370,-4.466838,-0.212519,6.072173,1.021468,-9.947480,9.658579,-4.051655,8.388708,-2.132340,5.930194,-1.329534,-2.117155,1.182579,-7.036457,0.315033,9.219716,7.483787,-8.475129,-3.475179,-2.522118,5.082253,-2.360450,-2.148651,-6.038443,2.588773,-2.736382,3.838596,-3.633166,-1.148567,2.996551,1.044015,7.004316,9.379557,2.333664,-0.292728,-9.986596,0.282785,4.079694,-2.065040,4.117915,9.548232,-5.100206,-4.157683,5.348053,2.221194,7.172347,-9.339217,3.619984,-2.718575,5.479623,-7.243812,2.339063,-5.244496,-4.699776,-4.775888,-3.107836,6.595278,-2.316924,8.009036,-2.137931,-6.270430,8.465175,5.854936,-2.466731,-1.388963,-1.725129,-3.555856,-0.301271,-9.089305,9.966502,-5.126136,9.087636,-6.616698,-6.062337,4.371703,-9.023867,-4.302637,-4.828850,9.971210,4.384974,-2.301072,-3.982825,8.309660,-9.803190,4.858864,-0.094753,1.109266,-9.711335,4.459201,-2.231267,1.894109,0.381637,-1.758338,6.238355,-7.468043,3.024825,-6.436495,9.838626,5.362638,-9.333414,-1.144087], dtype = "float32")#candidate|10801|(126,)|const|float32
call_10800 = relay.TupleGetItem(func_10280_call(relay.reshape(const_10801.astype('float32'), [126,])), 1)
call_10802 = relay.TupleGetItem(func_10283_call(relay.reshape(const_10801.astype('float32'), [126,])), 1)
output = relay.Tuple([uop_10790,call_10800,const_10801,])
output2 = relay.Tuple([uop_10790,call_10802,const_10801,])
func_10803 = relay.Function([var_10789,], output)
mod['func_10803'] = func_10803
mod = relay.transform.InferType()(mod)
var_10804 = relay.var("var_10804", dtype = "float64", shape = (11, 1, 13))#candidate|10804|(11, 1, 13)|var|float64
output = func_10803(var_10804)
func_10805 = relay.Function([var_10804], output)
mutated_mod['func_10805'] = func_10805
mutated_mod = relay.transform.InferType()(mutated_mod)
const_11029 = relay.const([[[-9.253993,5.578011,-1.926634,5.753857,-5.139285,-1.125586,-5.634711,-8.464988,-0.143832,6.946090,-5.383907,6.691423,-6.879485,0.813183,-5.309675,4.020350],[5.398431,4.477383,3.932994,5.166106,-9.536337,-6.546599,-7.158899,6.898740,9.834661,6.795468,9.691302,9.309622,7.763855,-2.734612,0.227249,-0.330875],[-7.844678,7.821167,-0.648220,9.587281,-7.030884,9.783846,9.765919,-7.697125,4.951210,-3.044846,-5.334788,-1.470608,-2.782493,-3.501464,-7.288931,-5.744107],[-5.143105,-3.320161,-5.488503,6.468089,9.069629,-1.559382,-3.542919,-5.948103,-5.492324,-2.611912,-3.279851,-0.922189,9.853519,7.856527,0.619780,0.136582],[9.368945,9.550789,2.749326,-8.839036,1.263833,8.624307,5.760647,-3.740453,5.220623,8.966500,1.684417,-4.022948,-5.094694,5.746667,-3.578141,8.652940],[-3.695345,5.694650,8.386976,6.203148,-9.472238,-3.511553,-4.275932,-4.017432,9.330803,2.151837,4.623157,-0.701246,4.219983,-5.630236,-7.063613,5.110603],[-0.167640,-3.956103,1.133492,-4.383543,6.830232,1.685611,9.591291,0.253596,9.284415,-4.249624,-7.723677,-0.771459,-8.594962,4.052973,-7.615787,0.503148],[-3.678222,0.292137,8.837157,1.376522,-7.224188,-0.363270,-2.769756,8.533477,1.569896,9.121776,-0.033324,7.901484,-8.401467,4.901272,-7.425794,4.341803],[-5.991407,-8.394938,-7.383419,-6.828304,-1.627291,9.620319,-0.360082,9.206323,-1.262116,-9.956069,-2.472872,4.073907,-4.284265,-3.774228,1.991204,6.900520],[-6.242020,-7.046056,-8.106989,8.316940,1.184346,3.890217,4.078978,5.708501,7.807656,-2.216559,-6.131172,-3.018847,-0.686557,6.908111,-5.724074,-6.132030],[-6.778307,-0.213282,2.698000,9.297851,-6.385525,9.873752,4.127887,4.558315,-9.649960,3.625354,0.721373,2.427410,-9.433132,0.396261,-1.793065,1.616347],[-2.241751,9.614159,7.680992,4.098143,0.202063,-6.171742,8.855338,-2.498129,4.442725,-4.132543,3.686456,0.339820,-3.240211,2.696543,-4.721095,9.400921]]], dtype = "float32")#candidate|11029|(1, 12, 16)|const|float32
uop_11030 = relay.asin(const_11029.astype('float32')) # shape=(1, 12, 16)
func_9335_call = mod.get_global_var('func_9335')
func_9340_call = mutated_mod.get_global_var('func_9340')
var_11034 = relay.var("var_11034", dtype = "uint64", shape = (392,))#candidate|11034|(392,)|var|uint64
const_11035 = relay.const([4.509432,2.402307,4.000388,2.749391,-5.278714,4.652873,9.469611,6.417982,2.423857,-9.192045,7.715934,3.181934,5.237898,5.242827,-7.823348,7.164355,-7.531680,1.831358,-9.029686,-2.276690,-8.524888,-5.846508,5.572721,4.864923,-9.802753,-1.005159,7.044791,-1.927284,2.486934,6.472577,-6.248826,8.253084,-3.424428,-2.033000,3.630437,1.049131,-0.429672,8.745777,6.375987,3.510831,5.923445,1.147300,1.037222,4.543000,-7.179042,-7.591043,2.606972,1.333011,-7.390834,-7.308075,-6.468061,1.464497,7.882009,9.580123,-2.617621,-9.613497,-6.666210,-0.525226,0.443369,-1.087528,-8.129861,-1.142886,-3.241254,9.137001,-1.162340,-0.063350,9.651030,3.907750,-9.471814,0.285656,0.855645,-7.300883,-3.588358,0.695363,-6.268472,0.385586,3.698136,-7.177364,9.693364,-9.595280,5.762606,8.555209,2.234038,0.110401,3.863365,-3.293959,-7.572307,-7.916042,5.523873,-8.908293,5.613425,-5.513608,-6.412692,-2.003504,3.700535,3.180897,1.289438,9.353158,7.441958,-7.462102,-2.196237,-9.848789,-1.434976,7.871605,-9.510813,6.265331,2.933415,-3.273066,1.073230,9.241034,-8.950559,9.065135,6.090058,-9.370060,-8.487325,2.298312,7.403621,2.654242,-1.725473,8.529324,7.002457,-8.845970,-5.358442,-5.850541,7.416896,-5.979559,-1.383017,4.925122,6.050685,-0.473395,3.548332,-4.615243,5.840830,-8.740721,-8.274387,6.038265,-7.742038,-2.169068,-1.504200,-8.579047,-0.612727,8.666104,4.744635,0.455153,-0.932944,-6.453092,6.085133,-9.630399,-1.010038,8.061745,-1.362453,-9.753852,-9.950599,-2.030310,1.184773,0.518766,9.544284,-1.130911,1.986432,7.720848,-6.254876,6.884115,-1.074606,-5.871342,-3.916604,9.906440,-1.691930,-4.023945,-8.150108,-3.982944,3.562905,-0.446174,-9.509431,7.075468,-0.572752,-6.359372,-0.933225,-3.059091,0.107967,-5.603834,-3.061059,7.591787,2.695848,-2.225902,-8.111890,-3.534085,-3.126070,-2.940801,5.172380,-3.773526,8.379343,-6.672671,3.453220,-2.388229,-3.745735,-5.893741,1.283714,8.450153,1.331674,-1.789878,-3.688650,-6.626880,7.171395,-3.863505,-7.480752,-8.285039,2.348072,-4.475677,-6.498641,6.509873,8.487301,8.215475,2.809023,6.271617,-5.947153,-4.319337,-4.685412,2.831970,-9.742820,9.714431,4.695272,-9.532026,-1.663374,7.866732,5.871416,0.648269,-8.800872,9.943311,-1.175280,4.143957,3.707552,9.958941,-2.435450,4.183408,-1.228287,8.661767,1.789554,-9.848131,-7.771359,-1.072852,3.210177,-4.156027,-6.222591,2.676990,2.340040,-1.165989,6.500248,-1.630705,-1.780519,-3.360034,-6.925725,-9.663035,8.593872,-2.813309,-1.900387,3.791942,-2.519459,-5.344006,-1.061737,6.587158,-8.875106,-4.061019,-5.184612,0.770668,-7.710672,4.961775,7.195476,-1.066733,9.984850,2.052125,7.301645,4.857424,-4.659883,0.086256,6.230140,-1.199815,-5.263990,6.941619,-7.196696,2.259363,-3.666311,9.865176,6.403632,-6.534627,-3.948798,-1.147680,0.928550,-0.433407,1.416685,-1.806118,-2.082127,-4.592672,2.623471,8.192360,-6.908177,-9.645151,-2.860186,7.250936,-7.121142,-9.081690,5.414640,-3.532128,-7.318790,-9.599107,-9.052983,-1.211863,-8.698360,4.560559,5.877962,7.362530,-9.570998,-7.418810,5.821328,-6.770004,-3.437456,6.750773,9.526234,-8.047685,-4.290856,-8.597669,6.219868,2.227260,7.895400,0.999687,-7.583867,1.672474,-5.079633,2.314252,6.649343,2.564020,-8.077609,5.576425,4.676563,9.527499,-1.203565,-1.736511,-7.480401,6.453437,9.809048,-5.602808,1.298507,-4.272727,-5.459723,-0.016274,0.884490,8.968208,-8.529910,8.622012,-6.754816,4.846856,-4.081706,-2.656704,9.478035,8.044696,-9.924577,-5.160843,7.433297,1.633000,-9.857932,7.820526,-0.581039,0.469279,4.249954,-4.469244,9.405623,-9.713684,4.056518,7.455355,3.038824,0.876220,-0.247057,4.200912,-6.617211,3.635917,-1.900426,-2.707224,2.556994,0.446892,9.095871,-5.708410,8.146710,-8.841985,3.372382,-7.826227,-3.322588,-6.128833,5.276856,-9.630942,1.477481,6.687913,-1.036623,-9.110421,2.143727,-3.015748,2.166808,-1.877551,-7.916107,0.804067,-4.913897,-2.311632,-0.346982,2.798204,-0.227316,4.633400,-6.364570,-8.193736,3.162265,-5.159557,-9.119804,0.452139,-7.253765,2.330638,-1.889584,-4.195528,-9.498782,-9.492528,-5.176646,-3.686767,6.075613,-3.965999,-2.874952,9.885720,4.869287,5.251797,-5.113149,3.880578,-2.546528,7.304591,6.230096,2.740463,-1.830281,-9.335824,1.309037,-8.843534,7.236360,-1.198350,3.533082,1.885113,-6.451126,-8.406071,7.610397,2.640688,-2.089458,-0.373822,-3.499510,1.226708,9.522560,9.100931], dtype = "float32")#candidate|11035|(448,)|const|float32
call_11033 = relay.TupleGetItem(func_9335_call(relay.reshape(var_11034.astype('uint64'), [7, 8, 7]), relay.reshape(var_11034.astype('uint64'), [7, 8, 7]), relay.reshape(const_11035.astype('float32'), [448,]), ), 1)
call_11036 = relay.TupleGetItem(func_9340_call(relay.reshape(var_11034.astype('uint64'), [7, 8, 7]), relay.reshape(var_11034.astype('uint64'), [7, 8, 7]), relay.reshape(const_11035.astype('float32'), [448,]), ), 1)
func_10803_call = mod.get_global_var('func_10803')
func_10805_call = mutated_mod.get_global_var('func_10805')
const_11052 = relay.const([[7.311677],[1.838415],[-5.489946],[-4.713636],[6.508201],[0.330000],[-7.107772],[9.633796],[5.115001],[-8.963887],[-9.981349],[-0.022064],[-9.769607],[7.307505],[-7.589619],[-7.780745],[2.630964],[2.695287],[4.825239],[3.107796],[6.959904],[1.225555],[9.716912],[8.583344],[7.839469],[7.690445],[6.917287],[-9.738604],[2.744838],[-2.377471],[8.418702],[7.454072],[-4.150862],[-9.626687],[-8.534907],[-7.157931],[-8.192563],[-7.023151],[8.725773],[3.160019],[5.630644],[-1.871207],[-0.079999],[1.499333],[-6.465774],[5.326590],[-7.716207],[-5.019214],[7.478756],[-4.084054],[-7.266383],[-7.617161],[-7.386528],[3.876544],[-1.104620],[6.641368],[0.808331],[-1.058528],[-7.770333],[9.006185],[7.354528],[-8.206612],[-1.354055],[-3.749924],[5.609881],[0.748834],[8.482572],[9.563999],[-7.366768],[2.350463],[4.291480],[5.912597],[-2.704791],[-6.804439],[3.011332],[2.946967],[5.297783],[-8.292216],[-3.826297],[0.605529],[5.482204],[-3.287937],[-6.248981],[-8.045266],[-6.337695],[8.927936],[-8.007361],[-6.373696],[-9.923454],[-9.987387],[-4.001034],[-4.474109],[5.090701],[1.604244],[8.383060],[-3.589548],[-4.082259],[-1.226385],[-9.408577],[2.682896],[-1.789719],[-3.745426],[8.283719],[-1.242712],[7.288150],[3.159401],[-0.065958],[1.111164],[-3.814127],[-9.309948],[-0.015727],[-6.580054],[9.495564],[7.058843],[-3.189037],[-7.467581],[-3.280739],[1.855520],[2.825017],[6.732035],[-8.035278],[-3.090868],[8.122794],[5.102528],[2.272499],[9.083503],[-7.759995],[-5.511131],[-6.406876],[8.459949],[-5.595934],[-6.195331],[-9.860117],[6.076694],[2.701594],[-0.369348],[8.232321],[-4.055284],[3.807740],[4.514805],[5.706110],[-3.784430],[-6.011459]], dtype = "float64")#candidate|11052|(143, 1)|const|float64
call_11051 = relay.TupleGetItem(func_10803_call(relay.reshape(const_11052.astype('float64'), [11, 1, 13])), 0)
call_11053 = relay.TupleGetItem(func_10805_call(relay.reshape(const_11052.astype('float64'), [11, 1, 13])), 0)
output = relay.Tuple([uop_11030,call_11033,var_11034,const_11035,call_11051,const_11052,])
output2 = relay.Tuple([uop_11030,call_11036,var_11034,const_11035,call_11053,const_11052,])
func_11057 = relay.Function([var_11034,], output)
mod['func_11057'] = func_11057
mod = relay.transform.InferType()(mod)
mutated_mod['func_11057'] = func_11057
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11058 = relay.var("var_11058", dtype = "uint64", shape = (392,))#candidate|11058|(392,)|var|uint64
func_11057_call = mutated_mod.get_global_var('func_11057')
call_11059 = func_11057_call(var_11058)
output = call_11059
func_11060 = relay.Function([var_11058], output)
mutated_mod['func_11060'] = func_11060
mutated_mod = relay.transform.InferType()(mutated_mod)
const_11489 = relay.const([[[-1.233081,7.584399,7.555806,3.846723,6.013373,3.137197,0.883733,2.449412,6.338877,7.996610,3.779489,7.301297],[8.819377,-5.371970,-2.348621,-5.783222,3.926604,-0.064552,-7.030550,4.484702,-6.120286,-1.312600,7.387035,2.835629],[8.096628,-6.126393,-8.116754,5.351703,-3.354441,4.451015,-7.433747,-2.237407,2.018363,-6.299864,-6.371223,0.759764]],[[0.876728,4.524555,7.078654,2.885969,1.113933,0.560994,-4.900655,-0.202615,-3.474631,7.163675,1.278508,2.242887],[-6.262337,-1.645292,9.324743,7.261417,4.090141,5.349462,9.114230,2.487865,-7.142301,-1.107649,-8.456454,-9.348418],[-1.177623,0.305041,3.372195,-1.544462,-1.858035,-9.257737,-2.709914,-9.573297,-3.833165,-7.106265,0.203902,2.836346]],[[4.366021,-0.268509,-9.356839,-3.821650,-2.239708,-6.053622,-2.334619,-5.356103,-3.272462,3.003305,-6.828255,-0.217108],[2.193324,9.748270,5.675064,8.272464,-0.217567,-5.450187,-9.078975,-8.603235,-2.599526,-5.520774,0.458214,6.246911],[6.345052,4.759409,5.423593,0.045281,-6.891262,5.974416,1.079740,-5.481989,-9.811227,-1.639355,-7.018167,0.180103]],[[7.097560,7.002980,-3.066675,-5.120937,7.723613,-4.181526,-6.443625,-3.615005,-1.279389,-5.340895,-4.855861,7.656445],[9.305427,3.271463,-3.287710,-2.345599,-2.287760,9.137591,-9.198191,-0.582781,6.500796,-4.854350,-4.376908,-2.361706],[-9.829216,-7.905976,-2.853115,0.342687,6.118402,5.279281,-1.503112,-8.521386,2.897763,0.602150,9.753625,-1.268447]],[[-5.647669,-3.841382,3.893348,4.931993,1.156917,-6.333797,-7.415763,3.316648,-1.166989,9.696129,-8.725937,1.882689],[7.237011,-7.968587,-8.053416,6.426790,9.979396,-9.053560,4.518120,8.781925,5.016240,-8.401321,0.511828,-8.087273],[-8.524365,-6.560675,7.664374,-1.603502,9.446000,4.215827,7.313535,-7.960026,8.051888,2.339940,4.677770,5.639194]],[[-5.747213,-8.662620,-7.220113,2.881605,-6.488582,1.895918,7.392890,1.670448,-3.436971,5.884664,5.098540,2.833154],[-2.040400,9.744645,4.291625,-0.777252,-7.846108,9.141332,6.400661,7.725356,9.390902,8.405127,9.615813,6.131250],[-4.655754,1.532161,-1.420067,-4.672513,-3.336133,-7.781817,-4.346433,9.247379,1.310492,1.168984,-9.110322,9.146432]],[[-6.461451,-9.437327,9.745364,6.477551,-7.353812,8.639782,4.137705,7.211495,-5.972524,1.873374,1.611494,1.967453],[-1.689987,4.661534,-7.930359,-9.676194,-3.707767,-2.534630,-2.106823,8.564102,-9.923019,3.104738,-5.588426,6.750810],[1.172814,5.155644,-0.600348,7.078239,-5.996243,7.478475,0.752369,0.178411,-8.940397,7.398272,8.780915,-9.606771]]], dtype = "float32")#candidate|11489|(7, 3, 12)|const|float32
uop_11490 = relay.atan(const_11489.astype('float32')) # shape=(7, 3, 12)
func_9400_call = mod.get_global_var('func_9400')
func_9404_call = mutated_mod.get_global_var('func_9404')
var_11493 = relay.var("var_11493", dtype = "int8", shape = (1260, 1))#candidate|11493|(1260, 1)|var|int8
const_11494 = relay.const([-9.120941,-1.006986,-2.883015,0.028374,9.521096,-1.386713,9.506748,-6.653752,7.891305,7.806487,-4.071556,7.443368,-2.152184,-8.695145,-7.862472,-7.745619,8.095930,-3.335660,-5.893172,8.913049,8.485991,9.804195,-9.946615,-7.465147,-2.839714,-8.012340,3.234510,-1.905598,3.433315,-5.987545,-4.889422,-6.700140,8.228551,0.881506,2.057928,-8.064769,-6.201277,9.566030,0.161921,-1.232312,0.822815,-3.675989,-7.602452,3.704890,6.190790,-5.076409,-2.795616,0.233839,3.472800,6.637538,-0.285702,8.799656,9.071453,7.972325,-8.285457,5.305094,9.012748,1.580277,-7.351073,9.472444,-4.232756,1.829490,-4.449866,-3.661214,1.071524,-2.863510,6.958714,-8.734505,-1.082789,9.922777,8.264983,4.690783,-4.575118,-7.509201,0.883833,9.729042,4.577656,-4.467142,6.638761,-9.423528,1.105982,-1.356222,-0.149209,7.172709,4.596028,-9.031022,3.459803,0.135318,-8.173412,-5.248725,4.689072,4.395042,-6.300703,-2.540286,-8.420945,-0.125726,-3.327187,6.143157,9.906077,1.222085,5.651099,3.548172,7.919817,1.145670,9.096941,9.033659,4.447648,0.484762,3.742116,5.048572,-0.039215,8.616748,6.474564,-9.565219,4.709661,0.339953,1.645211,-2.213673,6.768009,-8.687758,5.895105,0.197049,-6.515250,7.534468,-5.061705,8.414486,-4.287300,5.922877,8.205016,9.390688,-0.240608,-1.688112,2.601923,-2.881046,-5.832587,0.899613,8.989051,-2.380939,-4.884201,1.519320,-4.724482,1.795080,8.610611,-8.736701,-0.773005,1.567592,-9.251621,-6.805423,-1.255423,-0.347465,8.891837,0.296507,-7.511386,-0.691912,2.907174,-1.287907,8.602059,-4.934224,-9.478146,1.464909,-9.630347,9.869344,-6.857638,0.827588,9.131989,1.444974,8.059723,7.089176,-7.403225,-5.999113,5.407153,-7.688215,9.814821,4.212007,8.328663,-2.920063,2.959584,8.420078,-2.348328,4.072245,-0.345650,-8.354520,6.513697,-5.857171,-6.834512,0.848081,9.489146,-8.209163,-3.441538,-3.542031,-5.064648,-9.112747,2.710221,-5.561723,-0.355583,1.919029,-7.713802,-4.810525,4.090467,-9.117527,-0.030594,8.872180,5.462526,-5.974131,9.212770,6.809132,5.705255,0.113264,0.482421,-8.137878,1.759805,4.284268,-6.758996,8.582327,-0.707524,4.414804,7.725306,-5.865458,-2.320818,7.443354,2.960255,5.125379,-6.120146,8.729230,-8.242763,0.174665,2.279851,-6.894668,-0.550879,9.813913,3.439987,2.572921,7.673149,4.920382,-5.898684,4.071888,2.811688,1.277334,-7.766907,-7.285318,-5.662741,-1.573545,-6.223766,3.338596,7.015337,1.601824,2.266296,8.418563,-4.860463,-0.511319,0.972137,-2.893954,1.594683,-4.542763,5.930060,-5.003153,-4.425531,3.092483,8.678889,-6.949934,-8.244806,3.925539,-4.200276,-6.772300,8.068652,-2.406599,2.370744,-1.289834,-9.812892,-0.248948,1.496999,2.874087,4.970820,-4.075749,-4.428809,9.823911,-6.944577,-0.570332,-4.802960,9.431101,-5.548980,-3.021648,-0.697647,-6.769831,-2.836990,-9.640740,7.039795,8.786983,7.265023,-0.760408,-8.879380,-0.527817,-6.358584,-4.485639,9.109642,8.975274,7.828792,4.820014,-6.678108,-7.775191,-5.668839,-5.945561,-0.688697,5.685518,6.020883,8.600902,3.996109,-7.535441,8.380889,-0.549887,-4.704060,-0.686575,-8.482725,9.097231,9.473168,3.629844,6.194974,5.515254,1.227145,8.973497,-8.092884,5.403276,-9.516607,-2.954566,-3.233587,-0.769752,-6.827898,-1.634482,0.082357,9.848860,1.560506,-0.287416,-6.505999,-2.927106,-5.004127,-2.370688,8.605199,5.236265,6.560485,4.249791,-6.338847,-5.894737,-3.007099,1.868330,-8.007431,-8.441427,6.669680,-2.146512,-4.162904,-5.843236,-1.339987,-1.725921,-1.633171,7.694226,5.704225,8.129733,7.728015,-1.454973,-9.158218,9.766749,-7.479249,-4.000016,-8.838071,1.050251,0.546413,-3.770667,-0.475128,7.630763,-4.456802,-3.687305,3.057018,4.456657,0.277260,-1.745895,-8.330466,-3.622047,3.018277,-4.003397,-4.634160,2.871124,1.494875,6.809524,-3.574451,-4.126076,-0.938619,-3.591704,-3.163950,-4.520332,9.509149,3.352166,-8.584043,-2.595499,-7.278544,9.723724,-1.167617,1.212093,-1.978440,2.747616,6.282016,4.088670,-2.774210,-6.645646,-6.799274,-6.837220,2.981070,1.281539,1.916753,-1.292952,-4.273637,-2.635508,-1.311511,8.897502,4.392245,8.806176,-6.244555,-4.033411,-7.481769,-8.523448,7.870263,-8.186837,-2.063599,-5.374336,1.904373,-1.486671,-5.829301,-9.341342,-8.331257,-6.306235,-0.176733,-9.688448,-7.154511,4.808383,2.639965,1.097611,-4.374914,-3.880267,0.910430,-1.700829,5.487889,3.032310,-2.463136,-3.933543,6.906334,-5.935044,-5.488597,-8.314377,5.038716,9.827773], dtype = "float32")#candidate|11494|(448,)|const|float32
call_11492 = relay.TupleGetItem(func_9400_call(relay.reshape(var_11493.astype('int8'), [14, 6, 15]), relay.reshape(const_11494.astype('float32'), [448,]), ), 4)
call_11495 = relay.TupleGetItem(func_9404_call(relay.reshape(var_11493.astype('int8'), [14, 6, 15]), relay.reshape(const_11494.astype('float32'), [448,]), ), 4)
func_5320_call = mod.get_global_var('func_5320')
func_5323_call = mutated_mod.get_global_var('func_5323')
var_11502 = relay.var("var_11502", dtype = "int16", shape = (210,))#candidate|11502|(210,)|var|int16
call_11501 = relay.TupleGetItem(func_5320_call(relay.reshape(var_11502.astype('int16'), [7, 6, 5])), 0)
call_11503 = relay.TupleGetItem(func_5323_call(relay.reshape(var_11502.astype('int16'), [7, 6, 5])), 0)
func_3039_call = mod.get_global_var('func_3039')
func_3041_call = mutated_mod.get_global_var('func_3041')
call_11505 = func_3039_call(relay.reshape(const_11494.astype('float32'), [16, 7, 4]))
call_11506 = func_3039_call(relay.reshape(const_11494.astype('float32'), [16, 7, 4]))
var_11507 = relay.var("var_11507", dtype = "float32", shape = (7, 3, 12))#candidate|11507|(7, 3, 12)|var|float32
bop_11508 = relay.bitwise_or(uop_11490.astype('uint8'), relay.reshape(var_11507.astype('uint8'), relay.shape_of(uop_11490))) # shape=(7, 3, 12)
func_9400_call = mod.get_global_var('func_9400')
func_9404_call = mutated_mod.get_global_var('func_9404')
call_11513 = relay.TupleGetItem(func_9400_call(relay.reshape(var_11493.astype('int8'), [14, 6, 15]), relay.reshape(const_11494.astype('float32'), [448,]), ), 6)
call_11514 = relay.TupleGetItem(func_9404_call(relay.reshape(var_11493.astype('int8'), [14, 6, 15]), relay.reshape(const_11494.astype('float32'), [448,]), ), 6)
uop_11516 = relay.rsqrt(bop_11508.astype('float32')) # shape=(7, 3, 12)
func_10225_call = mod.get_global_var('func_10225')
func_10228_call = mutated_mod.get_global_var('func_10228')
const_11528 = relay.const([-8.397167,-9.162240,9.277586,-7.789349,-4.242503,-6.901562,-8.365761,-0.045341,-6.279681,-9.045851,-7.917705,-4.134892,-8.287983,-7.430275,6.842166], dtype = "float32")#candidate|11528|(15,)|const|float32
call_11527 = relay.TupleGetItem(func_10225_call(relay.reshape(const_11528.astype('float32'), [5, 1, 3])), 0)
call_11529 = relay.TupleGetItem(func_10228_call(relay.reshape(const_11528.astype('float32'), [5, 1, 3])), 0)
output = relay.Tuple([call_11492,var_11493,const_11494,call_11501,var_11502,call_11505,call_11513,uop_11516,call_11527,const_11528,])
output2 = relay.Tuple([call_11495,var_11493,const_11494,call_11503,var_11502,call_11506,call_11514,uop_11516,call_11529,const_11528,])
func_11531 = relay.Function([var_11493,var_11502,var_11507,], output)
mod['func_11531'] = func_11531
mod = relay.transform.InferType()(mod)
mutated_mod['func_11531'] = func_11531
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11531_call = mutated_mod.get_global_var('func_11531')
var_11533 = relay.var("var_11533", dtype = "int8", shape = (1260, 1))#candidate|11533|(1260, 1)|var|int8
var_11534 = relay.var("var_11534", dtype = "int16", shape = (210,))#candidate|11534|(210,)|var|int16
var_11535 = relay.var("var_11535", dtype = "float32", shape = (7, 3, 12))#candidate|11535|(7, 3, 12)|var|float32
call_11532 = func_11531_call(var_11533,var_11534,var_11535,)
output = call_11532
func_11536 = relay.Function([var_11533,var_11534,var_11535,], output)
mutated_mod['func_11536'] = func_11536
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11610 = relay.var("var_11610", dtype = "float64", shape = (13, 15, 5))#candidate|11610|(13, 15, 5)|var|float64
uop_11611 = relay.sigmoid(var_11610.astype('float64')) # shape=(13, 15, 5)
func_2582_call = mod.get_global_var('func_2582')
func_2588_call = mutated_mod.get_global_var('func_2588')
var_11620 = relay.var("var_11620", dtype = "float32", shape = ())#candidate|11620|()|var|float32
const_11621 = relay.const([-8,8,8,-7,-8,3,2,-7,-5,-2,3,-3,-8,8,-7,-2,7,-6,8,3,6,10,-8,-7,-5,-3,10,7,-4,1,-5,8,-5,-9,10,8,6,7,4,6,3,-2,-3,3,3,1,-1,9,5,-10,2,4,8,1,-5,3,-4,1,3,7,1,3,-8,7,-2,8,-5,-1,4,-6,9,-7,4,4,-5,5,-8,-8,-3,-10,2,-9,2,1,-4,-5,6,-9,1,10,-6,-9,-3,3,-2,1,10,-4,-3,-10,-1,3,-8,-8,8,2,2,8,-10,1,3,9,-3,-8,7,-3,-5,-6,9,-2,3,-10,-7,2,9,-1,-5,-6,1,-7,3,7,-6,-1,-8,-3,6,5,4,-1,1,5,-2,6,-8,4,-3,-9,5,-8,-2,-3,6,4,-7,3,8,-6,3,-6,7,2,10,-2,1,9,1,-4,1,-9,4,8,1,2,8,-5,-9,-8,8,5,10,-3,-5,-9,4,3,-9,-9,5,-6,-1,-1,-10,9,-8,7,6,8,6,8,-5,-7,-1,7,-8,-2,-8,7,-1,7,-1,-5,6,-10,1,2,8,2,-4,9,2,10,4,7,6], dtype = "uint16")#candidate|11621|(225,)|const|uint16
const_11622 = relay.const([[7.250760,6.225844,-4.554010,7.099685],[2.035895,4.025655,1.158090,1.740536],[-8.405558,-2.785749,6.481439,-7.724842]], dtype = "float32")#candidate|11622|(3, 4)|const|float32
const_11623 = relay.const([7,5,8,-1,3,6,-6,7,10,1,6,-7,-6,-9,-10,-8,-2,7,3,6,7,-9,2,6,-3,-9,7,-2,-3,-7,-5,-3,9,6,7,1,5,6,3,-9,-1,5,-4,-2,-8,-1,-3,10,6,8,-2,-9,9,6,9,10,4,9,-2,7,1,3,-4,-10,2,4,-6,-1,-8,1,-2,7,-10,-8,-9,-2,-2,-6,1,7,-1,9,3,6,-7,-1,10,9,-6,2,-1,-6,3,-9,6,-10,-10,8,-9,7,3,-8,-5,5,-3,7,-3,-7,6,3,-6,1,-1,7,3,-7,1,-9,4,10,-1,1,1,-4,-6,9,1,-5,-10,2,8,10,-9,-10,3,10,8,-1,1,-7,2,8,7,4,8,1,-9,9,-9,1,-10,7,-2,8,4,10,-3,-7,-4,10,-1,9,-1,10,-9,2,-1,7,7,-9,-3,7,9,-8,7,6,8,-9,-4,-7,-7,-2,9,-2,-9,7,1,-7,8,-5,3,4,-5,-10,-10,-5,5,-7,-9,1,1,-9,4,3,3,-8,9,10,2,6,7,1,9,6,-7,5,7,-8,-9,-2,3,9,-1,-6,8,-5,3,7,-1,7,2,-6,5,-1,-9,7,2,-1,-4,5,1,7,5,-6,-10,6,7,2,-8,-6,-3,-6,-6,7,-8,-4,-4,2,8,8,1,8,8,9,3,2,6,-3,6,4,4,-2,-10,8,2,-4,1,-10,3,4,3,-2,-3,1,4,-3,5,7,-10,3,-2,-5,-2,10,2,-3,-10,-4,-9,4,10,4,-5,-1,7,-8,-5,-1,-6,2,7,-5,-10,1,3,7,-5,1,3,6,7,10,-7,-9,-2,-2,-8,-5,3,-10,-1,2,-7,7,-6,-1,-9,7,9,-8,10,-9,5,9,-10,-6,5,9,4,3,1,5,4,-5,-9,-6,-2,-5,9,-7,-2,-9,5,-2,-6,-7,10,8,-3,9,-7,-10,9,8,-1,8,9,4,-7,-3,1,1,-3,7,5,9,-10,3,-4,1,5,1,-7,10,-9,-9,4,-4,-1,2,-7,-10,-9,8,5,1,9,5,-6,9,9,-8,10,-9,-2,-8,1,-6,2,-4,-5,6,6,9,-8,7,-8,10,8,-8,-10,7,-4,-2,9,1,2,6,-1,-9,-5,8,-3,9,10,2,-2,1,-2,-2,8,2,3,7,-5,6,-3,3,-5,-5,-10,4,6,9,8,-10,7,8,2,-7,-10,-8,9,8,6,10,-10,1,2,5,-3,6,-9,-1,10,9,-3,2,2,10,3,5,6,3,-6,-8,3,9,8,4,-2,-9,-2,8,3,4,-10,1,-3,-2,3,7,5,10,8,3,-9,-4,3,4,2,2,-7,7,-9,10,-10,2,3,-9,7,2,4,6,-9,-5,-8,-2,2,-4,10,-7,-1,4,-10,-8,6,-3,-3,8,-9,5,-2,2,-8,-6,-10,-9,-1,-8,7,-8,-3,3,-9,-10,-6,4,3,1,-4,-10,-2,-7,3,4,1,-4,2,-2,8,9,-8,3,1,-5,-3,-1,-5,5,-6,-9,-10,3,8,-5,9,4,1,1,1,6,2,-8,8,6,-4,-10,5,8,-1,2,1,9,3,-3,-7,-8,-8,7,-2,9,5,-10,-5,4,5,5,-3,-7,6,1,-9,-2,7,-3,10,3,-1,6,3,-1,-9,4,3,-10,-9,2,-2,-7,4,8,-1,-1,-5,-10,10,-7,-2,-1,-2,3,4,1,10,6,7,-1,-4,3,-3,10,-6,2,-7,2,6,1,3,-7,-10,-8,-5,-9,3,-10,7,-8,6,1,-5,-1,10,-2,-3,-5,-9,2,-2,-7,-3,1,-9,-2,-1,8,-8,8,2,1,8,-10,9,-3,7,7,-8,-9,-7,2,6,5,-1,-3,2,10,-8,-7,6,-9,9,-2,-4,2,4,1,-3,5,1,7,-2,3,7,8,-9,6,-4,-5,-9,-4,-2,-4,-3,-1,9,-10,-4,2,5,7,-10,4,-1,-6,9,-5,7,7,10,-6,3,3,-1,1,6,1,-10,4,5,4,-10,-4,10,-8,-9,-1,-2,-2,-1,10,10,5,-8,5,-9,-9,10,5,-7,10,9,8,8,-6,-2,6,10,6,-10,-5,-10,5,10,-9,5,2,-3,-5,2,-7,10,8,5,-1,-5,-4,-3,-6,-1,9,-4,-9,-3,5,-8,2,8,-7,6,-9,-4,-9,-4,-9,9,2,-1,8,7,-1,-10,10,-3,-4,-7,-1,8,8,-4,-6,5,4,-8,9,-10,8,-3,7,-7,6,-5,-5,-8,2,9,5,-5,9,-3,-9,-3,2,-7,-4,1,-10,-7,-9,9,-7,1,-2,2,2,-4,-10,-7,-2,5,-1,-6,-3,6,-9,5,-3,9,3,-1,-7,-5,3,-1,-8,-1,-3,10,9,9,-2,6,-1,5,4,-10,-2,-10,-8,-1,7,7,-10,-7,-6,-9,-3,8,-7,7,-10,4,3,-8,-7,9,-3,-6,-7,2,-1,4,5,7,4,5,2,-7,-7,8,-3,10,5,-9,-10,6,3,7,-1,-1,-10,-8,-8,-7,-9,9,-2,-8,-6,9,-1,1,-4,-1,3,-9,-10,7,-1,3,1,-2,2,2,-10,-7,-6,2,-7,7,6,-4,3,4,-6,-4,10,2,7,-3,-4,7,-9,2,-3,-5,-4,-5,10,3,-10,-7,-4,-4,10,9,8,-6,4,-2,-6,5,-5,7,4,5,6,4,-8,2,-8,6,4,2,7,-4,-8,-2,-1,-2,6,7,-7,1,-1,-7,-3,-2,2,-4,7,-3,7,10,2,-3,9,-10,2,4,-4,10,-6,4,-8,9,8,-2,9,5,6,-2,1,-1,-5,6,-10,9,-3,-3,3,8,-6,-8,-4,8,4,-5,6,-6,3,-4,-10,-8,-8,-4,3,-6,-2,-7,9,6,-9,-6,5,6,6,2,5,-9,-10,-5,6,-5,-6,-5,-8,-10,-10,-2,10,6,9,4,-9,-8,7,-2,-5,-1,9,-9,9,-4,6,7,-5,4,2,-8,2,-7,-1,3,-8,-8,2,-6,7,-1,7,10,10,5,-3,-2,1,5,-10,8,3,-5,-5,8,-10,-8,-9,-8,-4,1,-8,-4,2,-2,8,-10,-8,-7,-7,-9,-4,-3,-5,1,6,7,-7,-4,10,1,6,6,8,10,-8,2,6,-6,8,10,-3,7,-10,7,9,-6,1,10,7,5,-9,-9,2,-5,5,4,4,6,-4,-2,2,7,-1,-3,7,4,-2,-10,-8,-7,-2,-1,-4,-2,1,-3,-3,-6,-9,3,-4,-3,-9,3,10,10,-10,-8,-9,7,6,3,-2,4,-8,9,-3,8,-5,-9,10,-7,-2,7,7,1,3,1,-3,-9,1,4,-10,5,-5,10,-6,6,-2,-9,-6,-2,-6,-6,-9,1,1,-1,-8,-6,-1,-8,3,-4,8,6,6,7,-3,3,6,-2,-1,-9,1,4,4,-8,-8,6,8], dtype = "uint64")#candidate|11623|(1320,)|const|uint64
call_11619 = relay.TupleGetItem(func_2582_call(relay.reshape(var_11620.astype('float32'), []), relay.reshape(const_11621.astype('uint16'), [225,]), relay.reshape(const_11622.astype('float32'), [12, 1]), relay.reshape(const_11623.astype('uint64'), [1320,]), ), 3)
call_11624 = relay.TupleGetItem(func_2588_call(relay.reshape(var_11620.astype('float32'), []), relay.reshape(const_11621.astype('uint16'), [225,]), relay.reshape(const_11622.astype('float32'), [12, 1]), relay.reshape(const_11623.astype('uint64'), [1320,]), ), 3)
output = relay.Tuple([uop_11611,call_11619,var_11620,const_11621,const_11622,const_11623,])
output2 = relay.Tuple([uop_11611,call_11624,var_11620,const_11621,const_11622,const_11623,])
func_11630 = relay.Function([var_11610,var_11620,], output)
mod['func_11630'] = func_11630
mod = relay.transform.InferType()(mod)
var_11631 = relay.var("var_11631", dtype = "float64", shape = (13, 15, 5))#candidate|11631|(13, 15, 5)|var|float64
var_11632 = relay.var("var_11632", dtype = "float32", shape = ())#candidate|11632|()|var|float32
output = func_11630(var_11631,var_11632,)
func_11633 = relay.Function([var_11631,var_11632,], output)
mutated_mod['func_11633'] = func_11633
mutated_mod = relay.transform.InferType()(mutated_mod)
const_11822 = relay.const([[[5.374934,-6.922890,-6.344286,-7.476595,1.848467,-4.559192,-7.587936,6.667472,1.009523,-2.741341,-8.483951],[-0.757467,2.643214,-2.221301,-3.964143,3.685524,-0.076022,1.488721,-8.345218,-0.625026,4.541632,-3.939291],[-6.929876,9.730314,8.731140,-9.360003,-8.454363,8.280718,2.957773,-7.093022,7.256120,-1.179147,6.671875],[-7.181742,0.931774,8.576793,-5.296834,1.132293,-9.394282,-5.532972,-2.363001,9.655391,1.356535,-1.987162],[-8.110581,-7.779340,-7.268925,8.237052,-6.353741,-7.681291,-2.018510,-5.214649,9.678715,8.142907,-4.666380],[1.746493,-0.472004,0.449532,7.368122,1.145674,-3.411699,-6.141370,-2.561455,-6.918419,6.224433,-9.679028]],[[2.713168,-8.087287,-2.205729,-2.038786,9.584525,2.351375,-4.024114,6.558892,8.157954,7.087086,-2.380149],[-5.760586,3.041827,3.435311,9.984163,-2.771155,-2.357752,4.282765,1.274744,8.230995,-4.152242,-8.023843],[8.115119,-7.224564,-9.788765,-8.262472,7.401236,4.737353,-1.281911,-5.530806,4.228842,-2.318361,7.654776],[-3.105504,1.095764,-2.531076,8.561781,-2.873320,-6.875039,6.194680,-5.046426,-8.252569,-4.121213,-6.828903],[-1.508390,6.378778,7.631274,-3.760642,2.148229,1.899989,-8.321464,-5.930623,7.833554,2.669615,-2.196945],[-3.546271,-9.659739,-3.334314,8.237650,7.144457,8.928397,9.653602,-2.875408,-0.875178,-4.193480,-2.292131]]], dtype = "float64")#candidate|11822|(2, 6, 11)|const|float64
uop_11823 = relay.cosh(const_11822.astype('float64')) # shape=(2, 6, 11)
output = relay.Tuple([uop_11823,])
output2 = relay.Tuple([uop_11823,])
func_11837 = relay.Function([], output)
mod['func_11837'] = func_11837
mod = relay.transform.InferType()(mod)
output = func_11837()
func_11838 = relay.Function([], output)
mutated_mod['func_11838'] = func_11838
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11837_call = mod.get_global_var('func_11837')
func_11838_call = mutated_mod.get_global_var('func_11838')
call_11853 = relay.TupleGetItem(func_11837_call(), 0)
call_11854 = relay.TupleGetItem(func_11838_call(), 0)
func_11630_call = mod.get_global_var('func_11630')
func_11633_call = mutated_mod.get_global_var('func_11633')
const_11863 = relay.const([1.112144,-6.082688,3.287535,5.589045,-5.012550,-1.760883,-9.689639,3.712807,1.820349,6.377240,-6.679619,3.221433,7.699963,5.766925,2.193612,6.148234,-5.779467,-7.928340,6.441366,-9.259214,3.199293,-5.459415,-0.088314,8.040052,8.206071,2.347499,-5.781617,4.758020,3.834715,5.181236,-0.799097,1.063157,-5.318068,-0.451564,2.010803,0.337961,-4.565177,-5.069819,3.721167,-7.780998,-6.979936,7.826109,-9.127415,-2.203917,5.256435,-6.422506,3.315562,-4.710086,-5.287167,6.156074,-2.301157,-2.929945,-2.123896,5.580384,-2.984408,1.704762,9.347607,-6.510491,4.426738,0.215255,-4.702206,-3.452169,0.669355,5.809998,-2.888061,6.312731,-1.037789,1.016563,-9.208395,-1.633270,-2.507068,4.509038,-0.249128,-2.548662,4.859526,9.535613,1.894193,7.252320,-1.970977,-1.326112,1.161772,6.338235,9.593241,-2.801927,5.390182,3.689593,-5.985166,-2.990603,-2.479352,-8.454503,-9.432866,4.953674,-1.155441,1.395524,9.497369,4.732479,5.341219,-7.724084,9.388529,7.234373,-1.461953,-0.654506,5.858567,4.641594,5.120024,8.985659,1.444928,-2.292426,4.053810,7.697669,7.139744,3.275969,2.003495,-7.579528,0.188006,-5.237903,-8.637575,-9.153469,8.630254,6.697204,-6.434377,-5.596264,7.542773,4.710406,-2.036359,5.929233,0.742514,7.630336,7.053765,9.138918,2.355531,-2.863164,-4.319588,7.863374,-3.870698,9.326307,-7.065805,0.120658,-9.936774,-3.691481,5.614103,-4.237039,1.423821,2.369014,2.358099,0.007705,-0.390408,-3.290984,-7.270713,-3.190614,-0.201887,1.329759,-2.664077,-0.607175,5.407060,4.236503,7.329254,1.561383,9.455649,6.165446,6.058578,5.392057,-2.986885,0.059233,-5.638283,3.295314,4.257341,0.774258,0.771665,-5.358354,-8.000764,7.145746,1.718486,-2.051791,-0.244116,-6.914704,-7.189723,9.314096,4.306771,-0.659230,6.674353,3.649978,-2.885820,-0.335199,-3.067125,6.551601,-7.957169,-2.882437,1.920781,6.261072,-3.629847,-8.333351,9.247562,5.411253,-2.960553,-7.688532,-6.201118,-6.194797,-9.472658,-2.910733,8.566731,-7.865684,7.853446,2.738795,5.595142,-5.512932,-9.753591,4.613777,-5.413202,9.880499,-2.370640,-1.840025,8.064426,8.310547,5.257604,-2.000761,8.816461,9.609470,-7.787610,-6.178623,2.323623,9.124578,0.532329,5.177603,-0.952398,-0.735474,5.988810,6.754100,4.220829,-7.031587,-5.763642,9.960687,3.722195,-0.041951,1.149338,-8.815561,9.808277,4.569961,-2.828148,7.036292,4.458970,3.524499,-4.415300,9.574098,8.772642,6.523275,-7.177533,-2.161724,2.906454,2.531969,0.284226,8.812109,-0.410761,2.739163,1.836496,2.564203,-4.788737,3.776595,4.358764,-0.598365,0.231820,-6.381963,-4.391495,9.753654,-9.067175,-7.265717,-3.481036,-2.186328,-7.599916,1.290348,-7.141140,-6.899157,4.028395,-5.918128,-6.446766,-2.361843,-5.158199,-7.424771,8.188305,-8.918695,-0.756239,0.408442,-8.996657,7.429939,2.187284,-5.617574,6.621562,-6.802567,0.163514,9.589271,1.716095,4.240098,1.945101,-5.603746,6.840948,-2.114107,4.933107,6.506320,7.826378,9.568657,5.795064,3.385697,-6.333615,-6.038711,-6.382196,-0.489773,5.383665,0.077381,3.409417,6.756048,-5.728042,-8.361056,3.503544,5.482319,7.800441,8.373557,-3.045513,8.140373,-8.071813,-2.702516,-5.974890,-3.221026,-6.300495,-4.840810,6.243856,9.586542,9.646618,8.445762,3.874857,6.031779,4.644423,1.576321,4.249273,1.561641,-8.936267,-0.849566,-9.773302,-7.167198,-7.564609,-0.819618,-4.405313,9.557282,6.863654,-6.367656,7.547740,1.121830,-0.170350,8.096918,-3.408509,4.577435,-7.525769,9.038065,-8.538681,-4.072679,-5.453899,-6.743678,-5.823772,-3.701898,9.002247,-6.010310,-8.380168,2.349369,-1.087805,3.206891,7.305291,-1.988473,-4.946655,-0.414572,9.195065,-9.640172,8.562235,4.671655,-5.863512,-7.270948,-5.268008,7.255384,-6.199192,-7.256525,2.700780,3.943568,-1.554792,-2.083402,1.784390,-6.344891,8.059979,-9.600700,6.787029,-1.905369,0.187426,0.866187,5.481526,2.424172,-4.803529,4.604290,7.894161,-8.058172,-0.591565,-5.416498,-1.724609,-7.765158,9.013231,-6.039779,-1.747148,5.884853,5.381647,-6.315132,2.443996,3.921840,0.531540,2.537390,0.045547,-0.307356,-8.572698,-2.146195,8.332667,2.937303,8.721520,-0.807566,-9.889558,-8.800234,-0.255169,1.289871,-8.268394,6.322052,1.052611,-3.728324,3.978207,-2.816530,0.660128,-8.307275,6.353938,-5.262822,5.177631,4.316658,-9.249202,-9.434144,-6.616404,-6.674355,-2.874215,-7.105706,-8.103119,-7.179846,0.859927,4.975082,1.508625,-5.350588,0.353449,-5.605443,2.116126,8.080147,1.290277,-7.826514,1.731025,-8.643389,1.350207,1.231635,8.038780,7.229011,-5.810224,6.255512,-9.539162,-2.261232,-0.648310,-6.967697,-5.301288,2.674347,5.173970,4.532415,-2.167288,-3.140328,-2.349362,9.029570,-0.420583,8.948414,-1.278775,-3.792225,-7.550687,-3.819901,5.137696,-4.984638,-0.861459,6.930444,9.783729,-5.138481,-8.401997,8.534959,-8.109162,-8.289873,4.537251,3.881547,8.530110,-3.115718,2.813184,-6.111108,-5.983310,-8.116608,9.850832,-1.716050,0.762593,-9.358380,-2.126626,-1.338596,3.777612,4.397961,-1.436957,-8.131387,-8.058853,3.252670,4.384360,0.798112,-6.611784,7.788062,4.111462,1.138508,-5.322844,2.238895,0.267679,-4.821911,-5.282133,-3.821823,-4.848968,-9.964501,7.891938,-6.202372,-7.456770,-2.981521,-0.345043,-9.571476,-9.043140,-5.234289,3.682250,4.420911,9.228004,4.318309,3.855191,1.015102,-5.892450,-7.586205,4.874569,9.647940,-8.134154,2.458613,2.200524,1.172426,8.891299,-4.878531,4.670783,6.374709,4.315536,-1.132478,-9.229872,9.473213,-5.883800,7.759602,-8.841167,5.034265,-0.058402,5.386861,-4.337626,9.900117,-5.361696,-2.208462,6.199596,6.011761,6.882455,0.562056,3.914297,-9.877674,6.977557,1.829307,-0.730553,-8.428409,4.383449,-9.696032,-6.790207,3.406441,-7.800668,-9.797216,-2.631420,-0.128640,-0.248130,1.102096,-7.383439,2.324419,3.678024,-0.218789,6.807072,6.727010,-7.210353,-6.779297,5.981400,-1.131911,0.579684,-2.168102,-0.339753,9.502106,-4.554871,-9.244591,6.407944,-9.597033,-2.698445,-2.151494,-6.719128,9.227032,-5.653264,2.053530,1.013622,9.373001,0.462708,-7.859838,-5.155679,-3.266582,8.663156,-2.163359,-1.435352,1.736843,5.189687,-6.298127,1.186200,-6.281740,8.529706,-2.961612,1.548177,7.066489,7.748679,-3.219493,-0.795896,-5.156211,1.089591,-7.165295,-9.186472,9.108024,7.218413,1.846949,5.467339,-9.270062,4.414847,1.840870,-3.278626,4.739436,3.413277,-7.553211,-7.373715,5.269675,7.154839,1.659800,4.366377,7.050933,-7.742928,-5.521316,-7.903163,-9.458358,8.038452,4.468932,3.379858,6.589311,-6.757439,-3.524303,-8.485044,0.039413,3.739464,6.186742,5.716096,1.333763,7.024044,9.499841,4.593484,-4.989395,3.792308,-5.181586,-0.891494,5.324411,9.869004,-5.458010,4.751460,6.657762,-2.333608,-5.224097,1.524481,-6.148873,3.893042,7.445356,1.132001,2.436099,7.888101,8.347528,0.554407,-3.605355,-4.506771,-2.170599,-2.417435,-5.937076,0.307176,-9.263205,8.094764,7.521802,-4.896582,9.139098,-8.591277,6.325735,-4.761832,-7.325564,7.143784,0.850149,6.818036,-5.739600,4.504683,-2.224657,8.335259,-1.990403,8.563103,3.232041,-6.808637,-9.131542,1.852829,-9.331952,-8.862028,9.503053,1.366191,-3.951645,-1.163244,0.855893,1.473790,-4.794929,-2.988047,9.216109,3.290272,-1.814654,8.442084,-7.492246,-8.515257,8.935068,9.620984,-1.245795,0.303023,8.823738,9.680721,7.788426,8.504702,2.383509,-3.467881,5.187007,9.570888,9.734762,-7.012002,5.667359,-6.726550,-1.677402,0.976687,6.714815,2.029759,9.569718,2.834279,7.881030,-4.857978,-9.812240,-4.625991,-5.904679,1.639460,-9.881915,-3.955910,-7.405059,-2.526926,-5.972485,-9.153438,-8.860212,8.718067,-5.837863,4.083815,0.428641,4.257030,-4.842411,2.103497,7.507922,7.481014,3.769674,-6.864409,-7.344034,-1.556914,-4.090950,-8.755108,-0.263625,-5.086015,-9.162985,-2.070537,-6.996809,-2.599208,0.287917,9.487787,-4.828828,8.320586,-0.586097,-6.409087,-0.640327,-3.489523,8.335389,-8.517083,-3.003508,-5.767134,-9.260847,-7.544933,-0.662759,6.572176,-3.425159,5.214707,3.612979,-2.691473,-1.005396,2.141925,2.512886,9.050272,-3.678900,-5.794292,7.115762,-3.801349,-8.032525,-4.490738,8.779229,-1.905690,-3.542050,-0.898750,-4.761971,-0.093431,4.631871,-8.432425,8.096161,4.739275,9.467441,-8.801210,0.803882,-4.045001,8.429438,-9.411811,-0.541736,-7.125887,-6.339175,1.238738,-4.542012,6.232860,1.157423,-2.839733,-2.734035,-4.495473,-3.369421,-0.594276,2.846448,7.951155,2.743856,7.187979,-2.856899,-2.232723,0.926710,-7.699159,3.574353,0.316105,0.654095,8.796632,-2.968732,1.014857,-8.213623,-2.704018,-9.776145,-6.707892,8.168378,4.137355,-6.941317,5.086245,4.744416,4.787684,8.891019,3.881927,-5.129177,-2.531506,6.689090,6.607099,5.663195,5.504154,1.954433,1.305157,-7.123980,8.737145,4.104169,-1.628923,-0.708406,2.143895,-4.237467,-9.324772,-9.104897,7.094360,-6.026788,5.857259,-1.607887,7.906936,8.139535,3.073277,3.931806,-8.219097,9.129103,-1.545207,-0.684633,0.273466,-1.169169,8.377024,3.070378,-4.996457,-8.959648,8.100052,7.437698,-1.540949,-9.393308,-3.741726,-6.711068,-0.699579,1.042173,9.614665,-1.797865,-8.899931,-1.546250,5.816155,6.470927,1.209550,-6.407655,-0.033853,4.485321,-9.022813,-7.969977,-5.637935,1.297811,-3.611350,2.942443,-3.362964,7.177590,-0.437908,-6.189859,3.306920,-0.270274,7.528241,4.965232,-8.845939,9.144463,-4.556342,7.875330,-1.058849,4.748165,2.284300,6.334149,4.743654,-1.797011,-9.959402,7.845751,-1.925419,6.793844,-0.797249,-4.762532,7.943169,7.849444,3.517439,-0.808235,4.774560,6.697594,-7.214485,-6.897041,4.616325,-1.553693,-8.348255,6.019633,3.185589,-5.844809,6.330675,-6.976617,-8.385169,1.141803,-9.273291,-3.713008,0.670280], dtype = "float64")#candidate|11863|(975,)|const|float64
var_11864 = relay.var("var_11864", dtype = "float32", shape = ())#candidate|11864|()|var|float32
call_11862 = relay.TupleGetItem(func_11630_call(relay.reshape(const_11863.astype('float64'), [13, 15, 5]), relay.reshape(var_11864.astype('float32'), []), ), 5)
call_11865 = relay.TupleGetItem(func_11633_call(relay.reshape(const_11863.astype('float64'), [13, 15, 5]), relay.reshape(var_11864.astype('float32'), []), ), 5)
func_9975_call = mod.get_global_var('func_9975')
func_9978_call = mutated_mod.get_global_var('func_9978')
var_11882 = relay.var("var_11882", dtype = "float64", shape = (180,))#candidate|11882|(180,)|var|float64
call_11881 = func_9975_call(relay.reshape(var_11882.astype('float64'), [9, 10, 2]), relay.reshape(var_11882.astype('float64'), [9, 10, 2]), )
call_11883 = func_9975_call(relay.reshape(var_11882.astype('float64'), [9, 10, 2]), relay.reshape(var_11882.astype('float64'), [9, 10, 2]), )
func_2851_call = mod.get_global_var('func_2851')
func_2855_call = mutated_mod.get_global_var('func_2855')
var_11885 = relay.var("var_11885", dtype = "int64", shape = (1872,))#candidate|11885|(1872,)|var|int64
const_11886 = relay.const([-1,-10,-8,-1,3,8,-6,-6,4,-7,6,-6,3,1,-1,4,5,1,7,2,-9,-5,-5,-8,-3,-9,6,10,-9,-5,1,-2,-7,10,7,5,4,-9,-1,1,-3,2,6,-9,3,5,7,-10,2,-8,4,7,3,1,4,-9,2,8,-3,3,5,10,9,4,-10,4,-6,-3,6,5,6,9,-7,-6,-8,-8,10,2,-10,3,-9,-3,6,5,4,2,-6,-7,-9,-7,3,9,5,-3,10,-4,-4,5,7,-4,2,8,-8,-2,8,-6,-5,6,-8,5,-6,-8,-8,-2,5,-3,-1,-4,7,-10,7,8,2,-4,-3,-8,-9,-1,1,9,9,-10,4,1,-2,-8,8,-1,-10,-3,-5,5,-9,-1,10,-4,-4,1,-10,1,5,3,5,-6,-10,-7,-1,-8,-9,-9,-1,-9,-9,4,5,3,5,5,-9,-3,1,-3,4,-3,2,-3,-8,7,5,7,9,9,-4,-1,7,-2,-8,3,8,-7,1,-1,-4,-6,-2,-8,3,-2,-4,-1,-9,-1,8,10,-3,4,9,-3,-6,2,2,-8,7,-1,4,-2,-5,-1,9,10,-10,-6,-4,2,7], dtype = "uint16")#candidate|11886|(225,)|const|uint16
call_11884 = relay.TupleGetItem(func_2851_call(relay.reshape(var_11885.astype('int64'), [12, 13, 12]), relay.reshape(var_11885.astype('int64'), [12, 13, 12]), relay.reshape(const_11886.astype('uint16'), [225,]), ), 1)
call_11887 = relay.TupleGetItem(func_2855_call(relay.reshape(var_11885.astype('int64'), [12, 13, 12]), relay.reshape(var_11885.astype('int64'), [12, 13, 12]), relay.reshape(const_11886.astype('uint16'), [225,]), ), 1)
bop_11899 = relay.floor_divide(var_11864.astype('float32'), var_11885.astype('float32')) # shape=(1872,)
output = relay.Tuple([call_11853,call_11862,const_11863,call_11881,var_11882,call_11884,const_11886,bop_11899,])
output2 = relay.Tuple([call_11854,call_11865,const_11863,call_11883,var_11882,call_11887,const_11886,bop_11899,])
func_11903 = relay.Function([var_11864,var_11882,var_11885,], output)
mod['func_11903'] = func_11903
mod = relay.transform.InferType()(mod)
var_11904 = relay.var("var_11904", dtype = "float32", shape = ())#candidate|11904|()|var|float32
var_11905 = relay.var("var_11905", dtype = "float64", shape = (180,))#candidate|11905|(180,)|var|float64
var_11906 = relay.var("var_11906", dtype = "int64", shape = (1872,))#candidate|11906|(1872,)|var|int64
output = func_11903(var_11904,var_11905,var_11906,)
func_11907 = relay.Function([var_11904,var_11905,var_11906,], output)
mutated_mod['func_11907'] = func_11907
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11837_call = mod.get_global_var('func_11837')
func_11838_call = mutated_mod.get_global_var('func_11838')
call_11987 = relay.TupleGetItem(func_11837_call(), 0)
call_11988 = relay.TupleGetItem(func_11838_call(), 0)
func_11837_call = mod.get_global_var('func_11837')
func_11838_call = mutated_mod.get_global_var('func_11838')
call_12003 = relay.TupleGetItem(func_11837_call(), 0)
call_12004 = relay.TupleGetItem(func_11838_call(), 0)
output = relay.Tuple([call_11987,call_12003,])
output2 = relay.Tuple([call_11988,call_12004,])
func_12011 = relay.Function([], output)
mod['func_12011'] = func_12011
mod = relay.transform.InferType()(mod)
output = func_12011()
func_12012 = relay.Function([], output)
mutated_mod['func_12012'] = func_12012
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11837_call = mod.get_global_var('func_11837')
func_11838_call = mutated_mod.get_global_var('func_11838')
call_12038 = relay.TupleGetItem(func_11837_call(), 0)
call_12039 = relay.TupleGetItem(func_11838_call(), 0)
func_9400_call = mod.get_global_var('func_9400')
func_9404_call = mutated_mod.get_global_var('func_9404')
const_12044 = relay.const([-10,8,7,-2,3,9,-9,4,9,9,5,-6,-6,6,-9,-6,1,4,-9,7,4,-2,9,9,9,6,3,-10,2,-3,-2,-2,2,-3,6,-4,9,5,3,4,4,-9,-5,-8,-4,7,-9,-1,9,-3,-5,5,-5,10,4,2,-7,7,-10,6,-5,2,-4,-8,-6,-5,-9,4,1,-2,1,5,4,7,-8,-8,6,8,4,4,-6,-2,9,9,-2,-7,6,1,5,-6,1,-5,-5,-8,8,8,2,8,-5,-3,9,-10,-3,5,-8,-8,-4,-7,-7,-7,-8,-8,-4,-2,-5,-6,5,1,8,4,6,7,7,10,-9,-9,-1,-7,-5,-4,2,-7,9,-4,4,4,-2,-4,5,4,-3,2,2,-1,-6,9,4,-6,-6,9,-10,3,-4,-4,-3,4,3,-1,3,2,-4,1,1,-2,-10,8,-8,6,6,-2,8,4,-1,-6,7,-6,-1,3,-6,8,8,10,6,7,-3,2,4,-3,-3,9,-9,2,-4,3,-10,8,8,5,1,8,10,5,8,-10,9,10,4,9,7,-8,4,6,-3,5,-2,7,-3,-7,-4,-1,-4,-10,-4,-8,10,7,-1,5,-1,-7,-5,4,-1,-10,-8,8,3,2,-9,-8,6,5,6,3,-2,10,-7,7,7,-2,10,7,-10,-1,-1,9,4,-7,6,8,10,-7,-4,6,-2,4,-8,5,4,-8,7,-4,-3,-1,-1,-7,7,-10,8,2,-4,-2,-9,-2,-5,10,10,-2,7,2,-10,-10,4,-10,6,4,10,2,-5,4,7,-1,-2,-9,-6,-8,9,7,-10,6,1,-7,8,-10,-6,-4,-2,9,9,2,9,4,-10,1,-8,-7,9,-9,3,-1,-6,1,1,2,8,-5,-4,4,10,3,2,-6,-3,-9,4,5,-6,-10,6,7,7,-10,-3,-6,-10,10,10,5,10,-10,-8,6,3,1,9,-5,1,9,2,8,6,-5,3,10,6,8,6,7,2,-1,5,-1,-3,-4,-6,8,2,8,3,-9,-7,4,2,3,9,-7,1,-3,-8,9,1,8,1,9,2,-3,-4,4,-8,10,-2,2,-4,-8,-3,-8,6,-8,-10,1,4,2,-2,-3,-3,8,1,1,-6,-10,7,5,-2,2,-1,-5,-8,-2,3,-1,-2,4,-10,1,-5,4,10,9,2,3,4,-8,-5,5,8,4,6,5,4,-1,-8,-3,4,-10,3,2,1,2,-10,4,2,10,-10,5,3,-3,8,-9,7,-1,-3,8,2,-2,6,2,7,-7,7,1,5,-10,1,7,9,10,8,-5,-9,-3,-4,4,-9,8,-2,-7,-4,-10,-6,-5,-5,-4,5,5,10,-9,-5,8,4,9,7,-3,-2,-6,-1,5,5,9,1,-4,-2,-5,-7,-10,-1,7,6,8,2,-8,4,9,3,1,-3,-6,9,-1,-6,-9,9,-4,-3,-5,-6,-10,-6,-4,-8,-2,-2,-6,-10,9,-10,-3,-2,6,-9,4,1,8,2,6,-6,1,-9,-1,3,-6,-8,-2,6,-10,6,-2,6,6,-1,10,-3,9,7,2,10,3,-7,-2,4,7,4,10,-9,-9,-9,2,-9,3,-1,-8,-2,-2,-9,-1,-4,4,10,-9,-10,-1,-9,-10,-6,-8,7,9,-8,-8,5,9,-10,7,-5,-8,9,4,6,10,-5,8,-2,-1,8,-7,-9,-2,7,6,8,-9,-7,6,-6,-3,5,-5,8,7,-5,7,-1,10,8,2,-4,-4,-5,-4,7,4,-1,-8,4,3,4,-3,10,-2,3,-6,-8,-10,3,6,3,1,-8,1,8,3,-5,-6,-4,-3,6,-8,2,-9,-1,-4,-4,8,-5,6,-4,-7,7,-8,-4,10,2,6,5,6,8,-2,-4,4,1,7,9,8,9,-9,-7,-3,-6,-1,-4,-8,-9,-7,-1,4,-1,9,7,7,1,9,4,7,2,-2,-6,-1,9,8,8,-1,-7,10,8,-1,1,9,5,7,5,-6,-8,-8,6,8,-9,5,-9,-1,-2,8,-4,1,4,-9,-5,-1,-3,-1,-4,4,-8,-1,-4,6,9,-9,2,4,-8,-4,-7,8,-4,2,-6,3,-5,-10,1,7,9,-2,-6,6,7,-8,5,-8,-3,-8,7,4,6,-3,10,-6,5,-10,2,6,-6,-6,10,-1,-4,-3,-8,3,3,-2,5,3,-4,3,-9,-5,-3,7,7,-6,6,-2,-10,-10,-2,-5,-2,10,-1,4,-2,-6,-2,-10,-10,-9,-8,1,-7,-1,5,9,4,3,-2,7,8,9,-4,-8,-5,-9,8,-3,10,8,-1,3,6,-1,5,-10,-1,10,10,-10,-6,2,-10,1,-10,-7,5,6,-6,-10,7,3,-1,-3,-2,7,-3,-2,-5,-3,3,6,10,9,-1,8,-9,3,-5,-2,-1,-6,10,-5,2,-10,10,3,7,5,-1,5,-5,3,-7,8,5,-2,2,2,7,-9,7,4,-3,6,-3,5,1,7,-4,8,1,-6,7,-8,-9,1,8,4,6,7,-10,9,-2,-1,-3,6,9,6,-2,-10,1,9,-7,-3,4,4,4,-5,-2,-3,-5,9,-4,10,9,-9,1,2,-2,3,-6,-7,-2,7,1,9,2,10,4,2,-7,-4,10,6,-2,5,8,8,-8,-6,-8,5,-4,6,2,-1,-10,7,4,1,6,2,9,6,7,-6,-8,3,-5,-1,-10,6,-9,1,10,-9,-9,2,1,7,1,-10,-6,10,5,-6,4,-8,-9,-8,2,-7,8,-1,9,-6,-1,7,3,-9,-9,-5,9,9,4,-10,5,-7,9,4,6,-6,8,4,-3,2,-8,-6,-2,-8,2,-1,5,2,6,2,7,8,-3,9,-5,-7,-9,3,-8,6,-9,7,-6,8,4,-5,9,-8,-6,-8,9,-8,-8,8,10,-6,-4,4,1,-4,-3,-7,2,5,-4,1,-6,-2,9,-10,5,-9,8,-8,5,-5,-1,-9,10,1,6,-5,-2,-9,-8,-10,-5,-1,10,2,-3,4,-1,-9,6,3,3,-4,-7,-5,-4,-8,-4,1,-10,1,-4,-1,7,-4,-9,5,-8,-6,4,10,6,6,-8,-6,-2,6,-10,-10,5,10,-2,-8,5,-7,-5,6,8,-1,-1,-7,-4,10,9,8,4,10,2,10,1,-6,-6,-10,-6,-1,8,9,-2,-5,-9,-9,-1,-10,-8,-2,-8,5,-3,-6,-6,6,-6,7,4,-1,4,-7,-10,2,7,-4,2,-9,-6,6,4,7,6,10,-7,4,-10,10,8,-5,-6,2,-2,-5,-9,-2,2,3,-7,-10,5,-6,7,-4,-8,3], dtype = "int8")#candidate|12044|(1260,)|const|int8
const_12045 = relay.const([[7.284483,7.227582],[1.627728,-7.735312],[-7.009867,-5.547468],[7.902441,5.446900],[4.991134,3.391249],[7.901093,-8.074247],[-1.288644,-7.344558],[6.957691,4.580550],[-6.235220,2.617614],[-7.033249,5.898350],[3.011348,-3.937222],[-9.327596,-9.408082],[6.565840,9.797412],[3.750644,8.937372],[-7.377715,-0.611159],[-4.563697,-0.454613],[3.412893,-4.669592],[0.745164,-7.193816],[-4.509998,1.908641],[-8.424903,-7.650198],[-1.844187,7.899861],[4.457610,6.779969],[-8.340823,1.237265],[4.679466,-0.355669],[-7.600872,-4.862304],[-6.702016,-2.507284],[7.633848,-9.592093],[-1.376035,-2.852722],[-1.961070,-6.757991],[-7.347770,7.576857],[0.471042,9.721033],[-4.469566,6.092856],[1.001009,-9.943445],[-4.293797,-4.872787],[4.045169,-8.160044],[3.364643,-5.544745],[-1.769608,-6.130603],[-2.730855,9.469535],[-4.474271,-9.353455],[-4.157704,5.775313],[4.667862,-8.911205],[6.208201,8.843959],[8.350603,-2.888326],[-2.627395,-0.715099],[6.008095,-7.790525],[3.135882,3.286207],[-2.869379,-0.394959],[-4.825038,-6.745609],[-4.636787,0.058815],[9.535585,-6.400758],[-1.691324,-6.001378],[2.177549,2.756467],[9.679671,-1.012893],[-0.111900,-6.319659],[3.903796,0.134382],[9.268077,0.295249],[-4.178803,0.268854],[2.611915,-6.050900],[-6.911170,2.324636],[-5.387200,-6.855972],[-0.519053,-1.958571],[-0.714826,5.263910],[8.488875,0.464890],[2.010137,-3.765473],[-3.438240,1.497403],[8.322614,7.905050],[-7.105855,9.714232],[-7.836042,-1.548148],[-8.202892,7.241157],[-9.275297,-9.533129],[6.101542,-2.401795],[-3.947729,0.505584],[-7.003162,6.913574],[-0.127031,5.082137],[2.610787,7.804559],[-6.478730,-7.565058],[-4.038083,4.214857],[-6.826964,2.850875],[-0.664943,-9.343838],[-3.530299,1.126158],[8.968745,9.938514],[5.926513,-5.689274],[3.667080,-1.327263],[-6.044450,3.477380],[-3.960524,6.986155],[-3.234278,2.657401],[-4.026443,-5.148683],[6.051526,7.630197],[-3.282764,-1.200993],[4.493129,-9.822075],[7.215004,-2.178876],[6.762783,-3.369231],[-5.954536,-1.882702],[-2.466465,7.260349],[-6.209418,-0.497022],[4.333854,-9.559959],[-2.070990,-2.707050],[1.152021,-1.797651],[0.607072,-4.517076],[-8.359278,4.240154],[-8.965257,-5.213554],[1.336270,3.322459],[8.461134,3.573182],[6.225826,-0.319180],[-3.147314,5.544809],[0.692926,-7.031609],[-0.922904,8.810782],[-5.639707,-0.708944],[-3.026390,8.644558],[-2.254668,9.556857],[-1.422454,0.816362],[-1.565939,5.704510],[-8.191049,9.691221],[7.701824,-5.009757],[-4.181799,-6.075982],[-4.811729,-3.934185],[6.073789,-2.226843],[-9.123156,9.477162],[-3.900281,7.534060],[-7.440289,-9.549168],[9.217038,-5.603810],[6.335295,9.599224],[-0.568894,-8.727707],[-4.879422,-3.522236],[6.346641,1.718949],[-7.441173,-8.487870],[5.581464,-9.033789],[6.608599,-4.996542],[-2.068344,5.519343],[-1.160605,9.440605],[-7.117971,7.452388],[-1.736780,1.091208],[6.595505,-8.353980],[0.232414,-0.719987],[-1.831861,3.336580],[1.221656,-0.711849],[-8.082319,-3.797979],[-8.153694,-3.851253],[2.028759,6.601645],[8.684689,8.846710],[-0.592687,-0.076126],[4.599299,-8.578471],[7.420408,6.156801],[-0.100861,-5.276058],[3.665668,4.050979],[8.034761,-4.187284],[4.177995,-2.990166],[-3.571666,7.642969],[5.211791,2.768087],[9.419865,-0.235584],[0.768218,4.334678],[-5.398571,-9.615278],[-9.025298,6.335224],[0.440485,4.456654],[-8.710587,9.818506],[5.488943,1.040746],[4.363027,8.884815],[-0.720069,2.759253],[5.182522,4.652614],[6.136570,2.088492],[6.378686,6.050527],[8.370866,-2.440424],[-6.795198,-4.643937],[-0.481804,8.662171],[-1.941907,-5.074628],[-3.699131,-1.795070],[0.239294,5.019513],[-6.113060,-8.474014],[-8.781448,-4.823491],[-8.785723,1.699438],[4.183638,9.502076],[0.746611,9.803670],[0.070544,-5.258194],[7.657985,-1.896405],[4.044832,2.602314],[-2.269399,5.481699],[9.222806,-7.733718],[-5.121567,1.107382],[-8.713586,-3.529143],[4.133574,9.069964],[0.183270,-8.430335],[8.804014,4.598963],[9.418948,-7.879413],[7.464537,-6.735254],[0.392562,-9.127419],[-8.724649,4.908346],[-3.038633,-7.443206],[2.544689,4.040520],[5.761364,-1.025887],[-6.263777,6.785102],[-8.540153,9.541882],[-0.823157,9.360113],[1.092336,5.646336],[8.417159,-8.436112],[-3.403070,3.766419],[-7.374816,4.581379],[-9.221347,-1.604391],[2.353413,-6.402670],[1.209271,5.164712],[8.508892,-9.650066],[0.563851,-8.311655],[-6.205581,-2.704426],[7.849373,7.937612],[-7.059201,-4.347926],[-0.141248,5.734658],[-1.491130,5.479053],[-0.817424,8.139304],[0.388026,-2.522197],[-6.094289,8.243193],[3.601487,7.694497],[3.166192,-6.271780],[9.733729,0.889369],[-4.868544,-2.197581],[-0.996137,-4.717493],[-4.808209,0.707343],[9.365795,-1.993941],[-6.136601,8.167057],[-9.501890,5.878692],[8.009247,3.603717],[-8.027996,-7.561983],[-6.008281,1.155837],[-1.411650,3.077754],[-2.733295,0.399492],[-9.256294,3.094584]], dtype = "float32")#candidate|12045|(224, 2)|const|float32
call_12043 = relay.TupleGetItem(func_9400_call(relay.reshape(const_12044.astype('int8'), [14, 6, 15]), relay.reshape(const_12045.astype('float32'), [448,]), ), 1)
call_12046 = relay.TupleGetItem(func_9404_call(relay.reshape(const_12044.astype('int8'), [14, 6, 15]), relay.reshape(const_12045.astype('float32'), [448,]), ), 1)
var_12052 = relay.var("var_12052", dtype = "int8", shape = (1260,))#candidate|12052|(1260,)|var|int8
bop_12053 = relay.bitwise_and(const_12044.astype('uint64'), relay.reshape(var_12052.astype('uint64'), relay.shape_of(const_12044))) # shape=(1260,)
func_4602_call = mod.get_global_var('func_4602')
func_4609_call = mutated_mod.get_global_var('func_4609')
const_12078 = relay.const([-1.139701,0.895205,0.337561,-2.574019,6.955672,3.282145], dtype = "float64")#candidate|12078|(6,)|const|float64
var_12079 = relay.var("var_12079", dtype = "float64", shape = (40,))#candidate|12079|(40,)|var|float64
const_12080 = relay.const(-1.265979, dtype = "float32")#candidate|12080|()|const|float32
var_12081 = relay.var("var_12081", dtype = "float32", shape = (220,))#candidate|12081|(220,)|var|float32
const_12082 = relay.const([1.664385,-1.392648,-3.838457,-7.376451,5.730567,9.094691,6.616276,0.675329,-6.687291,-1.112201,1.302400,0.111275], dtype = "float32")#candidate|12082|(12,)|const|float32
var_12083 = relay.var("var_12083", dtype = "uint64", shape = (1320,))#candidate|12083|(1320,)|var|uint64
call_12077 = relay.TupleGetItem(func_4602_call(relay.reshape(const_12078.astype('float64'), [3, 2, 1]), relay.reshape(var_12079.astype('float64'), [40,]), relay.reshape(const_12080.astype('float32'), []), relay.reshape(var_12081.astype('float32'), [220,]), relay.reshape(const_12082.astype('float32'), [6, 2]), relay.reshape(var_12083.astype('uint64'), [1320,]), ), 8)
call_12084 = relay.TupleGetItem(func_4609_call(relay.reshape(const_12078.astype('float64'), [3, 2, 1]), relay.reshape(var_12079.astype('float64'), [40,]), relay.reshape(const_12080.astype('float32'), []), relay.reshape(var_12081.astype('float32'), [220,]), relay.reshape(const_12082.astype('float32'), [6, 2]), relay.reshape(var_12083.astype('uint64'), [1320,]), ), 8)
func_4602_call = mod.get_global_var('func_4602')
func_4609_call = mutated_mod.get_global_var('func_4609')
call_12085 = relay.TupleGetItem(func_4602_call(relay.reshape(const_12078.astype('float64'), [3, 2, 1]), relay.reshape(var_12079.astype('float64'), [40,]), relay.reshape(const_12080.astype('float32'), []), relay.reshape(var_12081.astype('float32'), [220,]), relay.reshape(const_12082.astype('float32'), [6, 2]), relay.reshape(var_12083.astype('uint64'), [1320,]), ), 7)
call_12086 = relay.TupleGetItem(func_4609_call(relay.reshape(const_12078.astype('float64'), [3, 2, 1]), relay.reshape(var_12079.astype('float64'), [40,]), relay.reshape(const_12080.astype('float32'), []), relay.reshape(var_12081.astype('float32'), [220,]), relay.reshape(const_12082.astype('float32'), [6, 2]), relay.reshape(var_12083.astype('uint64'), [1320,]), ), 7)
output = relay.Tuple([call_12038,call_12043,const_12045,bop_12053,call_12077,const_12078,var_12079,const_12080,var_12081,const_12082,var_12083,call_12085,])
output2 = relay.Tuple([call_12039,call_12046,const_12045,bop_12053,call_12084,const_12078,var_12079,const_12080,var_12081,const_12082,var_12083,call_12086,])
func_12105 = relay.Function([var_12052,var_12079,var_12081,var_12083,], output)
mod['func_12105'] = func_12105
mod = relay.transform.InferType()(mod)
var_12106 = relay.var("var_12106", dtype = "int8", shape = (1260,))#candidate|12106|(1260,)|var|int8
var_12107 = relay.var("var_12107", dtype = "float64", shape = (40,))#candidate|12107|(40,)|var|float64
var_12108 = relay.var("var_12108", dtype = "float32", shape = (220,))#candidate|12108|(220,)|var|float32
var_12109 = relay.var("var_12109", dtype = "uint64", shape = (1320,))#candidate|12109|(1320,)|var|uint64
output = func_12105(var_12106,var_12107,var_12108,var_12109,)
func_12110 = relay.Function([var_12106,var_12107,var_12108,var_12109,], output)
mutated_mod['func_12110'] = func_12110
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12011_call = mod.get_global_var('func_12011')
func_12012_call = mutated_mod.get_global_var('func_12012')
call_12115 = relay.TupleGetItem(func_12011_call(), 1)
call_12116 = relay.TupleGetItem(func_12012_call(), 1)
output = relay.Tuple([call_12115,])
output2 = relay.Tuple([call_12116,])
func_12121 = relay.Function([], output)
mod['func_12121'] = func_12121
mod = relay.transform.InferType()(mod)
mutated_mod['func_12121'] = func_12121
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12121_call = mutated_mod.get_global_var('func_12121')
call_12122 = func_12121_call()
output = call_12122
func_12123 = relay.Function([], output)
mutated_mod['func_12123'] = func_12123
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12121_call = mod.get_global_var('func_12121')
func_12123_call = mutated_mod.get_global_var('func_12123')
call_12150 = relay.TupleGetItem(func_12121_call(), 0)
call_12151 = relay.TupleGetItem(func_12123_call(), 0)
var_12154 = relay.var("var_12154", dtype = "float64", shape = (2, 6, 11))#candidate|12154|(2, 6, 11)|var|float64
bop_12155 = relay.logical_and(call_12150.astype('bool'), relay.reshape(var_12154.astype('bool'), relay.shape_of(call_12150))) # shape=(2, 6, 11)
bop_12158 = relay.logical_and(call_12151.astype('bool'), relay.reshape(var_12154.astype('bool'), relay.shape_of(call_12151))) # shape=(2, 6, 11)
output = relay.Tuple([bop_12155,])
output2 = relay.Tuple([bop_12158,])
func_12166 = relay.Function([var_12154,], output)
mod['func_12166'] = func_12166
mod = relay.transform.InferType()(mod)
mutated_mod['func_12166'] = func_12166
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12167 = relay.var("var_12167", dtype = "float64", shape = (2, 6, 11))#candidate|12167|(2, 6, 11)|var|float64
func_12166_call = mutated_mod.get_global_var('func_12166')
call_12168 = func_12166_call(var_12167)
output = call_12168
func_12169 = relay.Function([var_12167], output)
mutated_mod['func_12169'] = func_12169
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12011_call = mod.get_global_var('func_12011')
func_12012_call = mutated_mod.get_global_var('func_12012')
call_12213 = relay.TupleGetItem(func_12011_call(), 1)
call_12214 = relay.TupleGetItem(func_12012_call(), 1)
var_12216 = relay.var("var_12216", dtype = "float64", shape = (2, 6, 11))#candidate|12216|(2, 6, 11)|var|float64
bop_12217 = relay.logical_or(call_12213.astype('bool'), relay.reshape(var_12216.astype('bool'), relay.shape_of(call_12213))) # shape=(2, 6, 11)
bop_12220 = relay.logical_or(call_12214.astype('bool'), relay.reshape(var_12216.astype('bool'), relay.shape_of(call_12214))) # shape=(2, 6, 11)
output = relay.Tuple([bop_12217,])
output2 = relay.Tuple([bop_12220,])
func_12230 = relay.Function([var_12216,], output)
mod['func_12230'] = func_12230
mod = relay.transform.InferType()(mod)
mutated_mod['func_12230'] = func_12230
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12231 = relay.var("var_12231", dtype = "float64", shape = (2, 6, 11))#candidate|12231|(2, 6, 11)|var|float64
func_12230_call = mutated_mod.get_global_var('func_12230')
call_12232 = func_12230_call(var_12231)
output = call_12232
func_12233 = relay.Function([var_12231], output)
mutated_mod['func_12233'] = func_12233
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11837_call = mod.get_global_var('func_11837')
func_11838_call = mutated_mod.get_global_var('func_11838')
call_12240 = relay.TupleGetItem(func_11837_call(), 0)
call_12241 = relay.TupleGetItem(func_11838_call(), 0)
func_8304_call = mod.get_global_var('func_8304')
func_8307_call = mutated_mod.get_global_var('func_8307')
const_12247 = relay.const([6.513572,5.499652,-6.989727,-8.842815,3.157242,-2.846173,-8.878441,-1.964514,6.283201,-7.411300,9.097309,-1.424657,4.052863,6.807911,6.884350,-1.195912,0.814181,-8.192902,-8.989365,-3.246623,9.745541,-8.839583,9.902046,8.667484,-3.397809,7.438067,9.566978,3.225999,-4.438301,2.282756,-7.169870,-8.280858,-4.937205,-9.747098,9.120246,-0.868320,1.748713,-3.703985,3.605988,9.874942,8.560969,9.727128,-0.071635,6.087403,5.957605,-6.950469,-4.866944,-6.637042,-6.725284,5.414886,0.531353,-6.777390,6.123289,-5.163763,3.362976,-2.104322,-1.826598,9.950365,6.323317,8.033595,-3.045880,-2.020513,-1.855937,7.989016,8.012074,-2.561106,-9.618565,5.372810,-4.765273,-1.860436,-3.635402,-7.696486,-1.027219,8.766516,4.565504,0.774048,6.444581,-8.038041,-6.806442,-2.659647,6.997462,-6.815148,3.282375,0.885971,1.180839,8.332398,-1.809471,7.351801,-0.485663,-9.410916,0.182551,9.109444,-3.544766,1.069091,6.377564,-9.398627,-0.686183,-0.961241,2.019616,1.136315,2.216585,-9.913764,5.396780,-1.236699,-6.553058,4.684754,-2.852396,-1.286002,-1.572406,2.745718,9.632623,-3.107508,8.873410,-5.280557,-4.555579,7.306555,-6.673379,-6.624376,7.992420,9.671993,0.296538,-2.652929,5.930677,-8.037387,-6.961533,5.309625,-0.896308,7.689009,-0.724191,-0.877685,-2.890207,-2.724721,3.408294,-2.593935,-3.551764,-0.543919,-8.069783,2.127817,-0.939554,8.320191,-6.469721,-3.740181,6.108282,-8.959829,3.256994,-8.647679,-6.514733,1.617905,1.835966,7.045829,8.188935,-4.682899,-6.861974,-3.088780,2.527484,3.233446,-6.443487,-7.808406,7.198846,-7.510554,0.562277,-8.032502,0.217665,8.430640,4.830048,-2.359704,6.329647,-5.525080,5.180943,-9.333262,9.154498,-7.595523,9.726657,0.475037,9.797304,-1.686725,-1.609100,-9.086994,-3.918696,8.791464,-2.758063,-9.307931,-3.725612,1.364589,8.006923,-3.856281,0.889587,8.037865,-4.833468,-8.440090,-7.834637,-6.242924,5.887415,-7.136857,3.864331,-1.488792,-8.299775,8.208986,1.183731,-6.746581,-3.755021,8.731736,7.840884,-3.304961,8.642947,9.361941,8.484751,4.453749,-7.653482,-9.200050,4.263962,-6.172261,-5.830858,-2.256034,-6.572837,-8.182660,8.799007,4.928764,-2.057666,-0.678805,-9.435271,7.307857,-7.271878,-5.622448,9.121999,-4.830248,5.864152,-7.504388,-6.951463,-0.302033,4.887494,8.849446,-7.365402,6.696165,-6.454621,8.611629,9.120733,9.302883,5.850190,-9.099442,-0.777759,3.089966,8.382582,1.147620,-6.912813,2.649125,1.466110,-9.739916,1.913262,-8.390794,-1.172167,-0.704918,9.640961,2.863038,2.955795,5.478771,-1.500419,-4.823398,-3.025485,4.738694,2.642420,-4.966495,8.318316,-0.060923,-4.945159,-1.214925,-3.423375,-9.764015,-7.950056,-9.724909,5.504763,-0.402245,-5.888879,-5.744604,-5.061143,2.881792,-4.658717,-1.463383,5.027982,-6.749180,-0.719942,-8.158697,0.108181,-0.828371,-6.890385,0.218365,-7.373060,1.048672,-1.027350,8.914409,2.932174,-6.183587,-5.698138,4.563166,-4.817513,2.730467,-4.233966,8.077770,-2.590683,-4.091330,3.662043,-1.677545,9.159803,-7.453191,5.502134,-1.740894,4.176852,-9.605536,-0.784099,7.432065,8.533850,2.240510,-2.572615,4.146494,-2.733193,0.913262,-2.163460,9.787052,2.770900,7.781918,2.166775,6.929888,7.283419,-8.706399,2.982169,-5.033373,-2.151671,-2.492741,-0.257550,6.972387,6.989709,-2.492342,-0.640029,1.607097,-8.565233,9.134967,3.051052,-7.223842,-6.547321,-7.920414,-1.166727,6.253380,-9.632188,3.062414,8.749719,4.864102,6.095266,-9.145366,8.663650,9.814106,1.587762,3.121360,3.181247,1.499614,-8.481030,5.324814,-0.840290,9.100461,-9.055627,4.109625,9.552448,8.184847,3.175429,-5.171296,3.825143,-7.236499,-5.957915,8.545603,9.149990,-9.071482,-9.108546,-9.039885,-0.040256,5.746745,-3.337199,-6.577437,9.443906,-0.102800,-3.314017,7.563150,-9.084134,-3.349570,0.190610,-7.928919,-0.185316,-9.491985,-3.950220,6.638737,-5.031016,5.244199,2.875393,-6.547148,9.468732,7.432941,-7.555803,-5.052834,-7.910317,2.597377,-7.436412,-6.511447,-0.546277,-4.041716,7.546012,6.856904,-5.290571,-7.253120,2.174382,5.401401,0.641592,-4.260529,5.553243,-4.591541,1.100687,-2.213369,5.752715,-9.315402,9.842778,-8.898464,-2.004466,1.740015,8.480990,-3.557447,-2.507068,3.170132,6.097577,0.075389,-4.359474,-9.487123,-6.778434,-9.553400,-3.351762,6.917042,4.732795,-1.782207,-0.204887,-9.280454,-1.184153,-6.679401,-8.071671,-2.076099,6.400268,6.431527,-1.720133,7.911816,-6.499745,-5.944467,-4.457884,-8.187179,-1.479465,3.277485,-9.066566,-7.430906,-8.875304,-8.880508,-8.422929,-1.819109,-1.315849,-8.884698,-4.118298,5.687073,5.237084,5.362642,-9.980047,5.854749,-9.022443,9.043862,-8.193744,6.995564,-1.432942,-7.927999,5.611064,-6.817530,-1.933988,-9.971073,-1.746687,5.964420,0.002432,6.737612,-8.973849,-0.055977,7.192566,-3.438235,0.631644,-6.512832,7.779275,2.459783,-2.031407,-9.940528,-1.659264,9.042342,6.069308,-8.833190,9.843806,-6.598617,-7.394193,-8.510857,-4.816388,3.302667,8.020672,8.335263,-9.280834,4.029125,-7.084837,0.601714,-8.127177,3.427503,7.907566,-7.003260,3.555623,0.104246,-0.266818,1.087806,-0.165114,-2.937431,-4.026282,-6.449688,-4.390485,9.133009,3.886317,2.769670,4.361786,5.621560,-6.596003,7.008466,-7.533568,6.941096,3.448883,0.363768,-4.762753,9.276337,8.685075,4.662216,2.144889,-2.915502,-5.436761,-2.694026,-9.570561,-5.811471,9.965718,-8.224835], dtype = "float32")#candidate|12247|(540,)|const|float32
call_12246 = func_8304_call(relay.reshape(const_12247.astype('float32'), [15, 12, 3]))
call_12248 = func_8304_call(relay.reshape(const_12247.astype('float32'), [15, 12, 3]))
func_11_call = mod.get_global_var('func_11')
func_15_call = mutated_mod.get_global_var('func_15')
const_12250 = relay.const([[6,6,4,1,1,2,3,-5,9],[-1,6,2,4,-4,10,9,-4,9],[-8,3,-2,-7,-6,1,-6,-6,8],[10,4,2,-6,1,-6,1,9,-5],[-1,-9,-7,-4,-3,-5,-10,4,-9],[-9,-9,-6,-1,1,2,-2,-10,-2],[1,10,-10,-6,-2,-6,7,7,-8],[-1,1,-8,7,8,10,4,9,7],[3,-10,4,-7,3,-6,-8,-7,-10],[1,-4,-5,-10,6,-7,9,-4,4],[-4,10,-4,8,5,8,-2,-5,2],[1,-10,-1,7,6,8,-1,10,2],[8,-3,-7,10,-4,6,-4,-7,-1],[3,8,-1,-1,9,-2,5,-8,6],[-3,-5,-3,2,7,4,-6,5,-8],[10,-9,-3,7,2,10,1,6,10],[-8,-7,-10,2,-9,1,5,1,10],[4,5,3,6,9,-9,-1,1,-1],[-10,8,9,-9,3,-8,-5,8,-2],[5,4,-2,-3,1,1,-5,-2,10],[-4,-8,8,-8,2,-3,7,-2,10],[-4,-5,6,-7,-6,-4,2,5,3],[-8,8,-6,-2,-9,-4,8,-3,-2],[-10,-8,8,5,9,2,7,2,-9],[6,-1,-8,5,4,-3,-7,-5,-1]], dtype = "uint16")#candidate|12250|(25, 9)|const|uint16
var_12251 = relay.var("var_12251", dtype = "uint16", shape = (1350,))#candidate|12251|(1350,)|var|uint16
call_12249 = relay.TupleGetItem(func_11_call(relay.reshape(const_12250.astype('uint16'), [15, 15, 1]), relay.reshape(var_12251.astype('uint16'), [15, 15, 6]), ), 0)
call_12252 = relay.TupleGetItem(func_15_call(relay.reshape(const_12250.astype('uint16'), [15, 15, 1]), relay.reshape(var_12251.astype('uint16'), [15, 15, 6]), ), 0)
output = relay.Tuple([call_12240,call_12246,const_12247,call_12249,const_12250,var_12251,])
output2 = relay.Tuple([call_12241,call_12248,const_12247,call_12252,const_12250,var_12251,])
func_12272 = relay.Function([var_12251,], output)
mod['func_12272'] = func_12272
mod = relay.transform.InferType()(mod)
var_12273 = relay.var("var_12273", dtype = "uint16", shape = (1350,))#candidate|12273|(1350,)|var|uint16
output = func_12272(var_12273)
func_12274 = relay.Function([var_12273], output)
mutated_mod['func_12274'] = func_12274
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12011_call = mod.get_global_var('func_12011')
func_12012_call = mutated_mod.get_global_var('func_12012')
call_12406 = relay.TupleGetItem(func_12011_call(), 1)
call_12407 = relay.TupleGetItem(func_12012_call(), 1)
func_3702_call = mod.get_global_var('func_3702')
func_3707_call = mutated_mod.get_global_var('func_3707')
const_12413 = relay.const([-7,5,9,-5,-9,8,3,-8,7,8,-9,-8,9,10,5,7,2,-6,-3,-3,1,-4,7,3,-10,-7,3,9,1,9,-5,-9,-8,5,-7,-6,2,-3,2,5,1,10,-9,6,-8,-7,-3,9,-3,-5,-5,-1,2,5,1,7,-2,-6,6,1,8,7,6,3,10,-2,-8,1,-8,-4,-6,3,-8,7,10,7,7,9,2,5,-7,-7,1,-5,-6,-9,9,-10,-8,2,8,6,-7,-9,7,1,10,-1,7,9,4,-8,8,2,7,-6,7,-10,-8,-1,2,1,1,-4,-5,-4,3,-1,-1,8,1,5,-7,2,4,10,-7,-10,2,-9,-7,5,-6,-10,3,7,2,-2,8,4,-9,-10,7,7,3,6,10,1,-10,-4,-1,-7,-4,-3,4,6,2,-4,-5,-6,-8,2,4,5,-4,-6,-2,9,-1,10,-8,1,-2,10,-5,-10,1,-2,-5,8,5,-6,9,5,-6,7,1,5,-2,-5,-1,1,-6,6,9,-1,-10,-1,2,10,9,3,5,5,3,6,4,-6,2,4,-8,4,-1,10,1,1,-5,-3,-2,-10,10,-9,-7,7,-10,1,-5,7,-1,1,-7,3,-7,-4,5,-6,-4,-1,1,-10,-8,-9,7,-1,5,10,4,-3,10,-2,5,-1,-2,-2,10,-3,5,1,10,-8,-4,6,-4,9,-8,10,-8,2,3,4,-6,-2,-1,-10,-7,-5,-9,-8,-1,6,9,-3,-6,8,9,-3,-9,5,-9,10,-5,6,-7,8,1,-7,7,9,7,3,7,10,-2,-5,-1,-5,-9,4,-5,-2,-4,9,1,7,3,-3,-7,-6,9,9,4,8,-5,9,-5,-8,-2,-4,-3,10,-4,-6,-3,9,-4,3,2,-3,-6,-9,-3,-1,2,-9,-8,-10,-9,5,-1,-5,-3,-4,10,2,-10,-8,-7,-10,-6,-3,8,-9,2,-1,8,-9,-4,6,2,1,-10,-9,-10,6,-7,-4,-4,2,-9,-10,-8,-10,4,8,5,-10,-2,1,-7,10,8,1,-9,8,5,-6,9,-7,1,10,9,-10,10,-3,-8,3,8,-8,6,-8,-5,5,-10,8,-10,-9,8,-7,1,-5,4,-7,-1,-1,10,-7,-6,1,-5,-9,-5,1,6,-4,-10,7,9,8,6,7,1,-3,6,-2,2,3,10,5], dtype = "int64")#candidate|12413|(448,)|const|int64
var_12414 = relay.var("var_12414", dtype = "float64", shape = (300,))#candidate|12414|(300,)|var|float64
var_12415 = relay.var("var_12415", dtype = "float32", shape = (12,))#candidate|12415|(12,)|var|float32
const_12416 = relay.const([1,3,-8,-3,7,6,-2,5,-3,-7,-6,-2,2,1,-5,-3,8,10,-4,-8,-8,2,-7,5,-6,6,-7,5,8,3,4,-2,3,8,-4,8,-1,9,9,-9,6,7,6,5,7,7,-6,-6,10,8,-10,-3,9,8,8,1,3,-9,9,2,2,7,-10,-8,-7,-4,5,8,3,-9,5,7,9,8,-2,6,-4,3,-8,-6,-9,1,-10,-5,-7,8,-6,2,2,7,-2,7,6,10,3,10,-8,6,-2,-3,-7,10,7,-3,4,3,1,-2,10,-2,7,6,2,3,3,2,-8,-5,6,2,-6,-6,4,7,-9,8,-10,1,-6,-8,2,-9,4,-3,-4,10,1,8,-3,9,3,-10,-4,6,5,9,6,8,-3,-10,-8,-6,8,4,8,-5,-3,-5,6,-4,-5,-8,10,1,-9,-2,-1,5,4,-1,3,5,-1,-4,2,-7,1,-8,-3,8,-9,-8,9,-2,-1,7,-10,-1,-1,-9,-2,-9,-4,-8,7,-9,-6,-9,-8,-10,-5,-4,-7,8,-1,10,3,-8,8,4,-10,6,-9,1,-7,10,-7,-6,1,-4,-1,6,6,9,-10], dtype = "uint16")#candidate|12416|(225,)|const|uint16
call_12412 = relay.TupleGetItem(func_3702_call(relay.reshape(const_12413.astype('int64'), [14, 16, 2]), relay.reshape(var_12414.astype('float64'), [300,]), relay.reshape(var_12415.astype('float32'), [12,]), relay.reshape(const_12416.astype('uint16'), [25, 9]), ), 0)
call_12417 = relay.TupleGetItem(func_3707_call(relay.reshape(const_12413.astype('int64'), [14, 16, 2]), relay.reshape(var_12414.astype('float64'), [300,]), relay.reshape(var_12415.astype('float32'), [12,]), relay.reshape(const_12416.astype('uint16'), [25, 9]), ), 0)
output = relay.Tuple([call_12406,call_12412,const_12413,var_12414,var_12415,const_12416,])
output2 = relay.Tuple([call_12407,call_12417,const_12413,var_12414,var_12415,const_12416,])
func_12418 = relay.Function([var_12414,var_12415,], output)
mod['func_12418'] = func_12418
mod = relay.transform.InferType()(mod)
mutated_mod['func_12418'] = func_12418
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12418_call = mutated_mod.get_global_var('func_12418')
var_12420 = relay.var("var_12420", dtype = "float64", shape = (300,))#candidate|12420|(300,)|var|float64
var_12421 = relay.var("var_12421", dtype = "float32", shape = (12,))#candidate|12421|(12,)|var|float32
call_12419 = func_12418_call(var_12420,var_12421,)
output = call_12419
func_12422 = relay.Function([var_12420,var_12421,], output)
mutated_mod['func_12422'] = func_12422
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12011_call = mod.get_global_var('func_12011')
func_12012_call = mutated_mod.get_global_var('func_12012')
call_12428 = relay.TupleGetItem(func_12011_call(), 1)
call_12429 = relay.TupleGetItem(func_12012_call(), 1)
const_12439 = relay.const([[[-9.186685,6.865301,-1.326783,6.807002,-3.742279,-4.378413,-4.822202,8.157691,1.017395,-6.034901,-2.771324],[-8.455556,-8.078061,2.010475,-5.091450,4.022604,6.793028,-3.128555,-7.298292,4.503389,7.294520,4.594528],[5.177905,4.209491,5.528973,-9.983880,7.726101,-7.656602,4.461984,-4.238308,-3.467832,-0.538616,1.774337],[-3.214269,6.734879,-6.717276,0.212358,-7.793491,-3.399226,-7.271254,-5.248710,2.217550,2.510192,4.827556],[-7.651640,-7.033846,3.543916,-9.033731,7.389478,-7.038446,-4.832963,-3.985848,-7.837792,-5.507420,-7.781987],[-6.827591,9.312721,-6.417034,-8.794634,8.295429,-6.602050,0.543505,8.678104,-6.585197,-4.453513,3.874935]],[[8.194260,2.469051,-1.510309,-0.421196,-7.669187,7.909602,-9.943281,-5.628747,-5.904128,3.010162,-5.065482],[-1.668345,-3.498328,-8.536025,-4.793635,8.007190,2.615475,5.983612,9.631579,-2.937095,2.285148,6.214229],[-7.255842,-0.134722,-5.788476,3.125779,-0.519208,-2.463316,-0.174209,-1.614521,-2.909538,-4.983806,-2.503163],[5.434255,0.518650,2.163085,-6.338931,-5.631239,-6.243139,7.466929,6.212902,0.755181,-0.661458,-3.032586],[7.536951,6.141007,2.969487,3.645081,-7.880556,4.087562,1.082798,-1.530686,2.773907,-0.663568,6.514005],[-1.926983,-9.005013,-7.784662,8.546518,9.056211,1.821490,-4.482979,-4.552305,-6.861034,7.721172,-3.086157]]], dtype = "float64")#candidate|12439|(2, 6, 11)|const|float64
bop_12440 = relay.greater(call_12428.astype('bool'), relay.reshape(const_12439.astype('bool'), relay.shape_of(call_12428))) # shape=(2, 6, 11)
bop_12443 = relay.greater(call_12429.astype('bool'), relay.reshape(const_12439.astype('bool'), relay.shape_of(call_12429))) # shape=(2, 6, 11)
output = relay.Tuple([bop_12440,])
output2 = relay.Tuple([bop_12443,])
func_12448 = relay.Function([], output)
mod['func_12448'] = func_12448
mod = relay.transform.InferType()(mod)
mutated_mod['func_12448'] = func_12448
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12448_call = mutated_mod.get_global_var('func_12448')
call_12449 = func_12448_call()
output = call_12449
func_12450 = relay.Function([], output)
mutated_mod['func_12450'] = func_12450
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12121_call = mod.get_global_var('func_12121')
func_12123_call = mutated_mod.get_global_var('func_12123')
call_12489 = relay.TupleGetItem(func_12121_call(), 0)
call_12490 = relay.TupleGetItem(func_12123_call(), 0)
func_8697_call = mod.get_global_var('func_8697')
func_8700_call = mutated_mod.get_global_var('func_8700')
const_12503 = relay.const([0.214787,-5.960243,3.058942,4.306102,-4.305606,-9.989943,8.215058,7.453435,-9.233621,-3.831586,-0.807407,4.915493,0.954902,5.593620,-5.977643,-8.113660,-5.590139,-3.068530,8.736744,2.966218,-0.831187,-5.112151,3.313975,-4.251724,4.947316,-2.082607,-2.708163,-7.043198,-3.682203,-6.860300,-5.288725,-8.264823,5.566103,-2.494328,-0.857909,-0.915164,1.890585,-4.462820,-1.943429,-6.621585,-8.733143,-0.823648,7.278933,-1.339543,-1.102837,-9.798901,-5.684436,6.135186,6.110635,-4.117031,1.270234,2.239629,3.915971,9.479611,-9.271223,-8.331922,4.028167,9.982797,2.692913,-5.345657,-6.513171,-7.444041,-8.681341,3.152095,5.753803,8.166592,-5.607796,5.540516,1.748653,-8.922008,-0.516775,-9.370345,3.889061,-3.910196,7.887585,-5.957042,0.168178,-0.566198,-6.402523,-4.888045,8.697111,-6.696389,-2.827534,-8.429592,-2.989157,4.024007,6.215401,-0.314033,-7.818422,8.241533,-1.925867,8.284263,-2.960252,4.792769,3.192759,-5.133658,5.497091,3.452658,-7.824107,1.372407,-8.685916,3.157522,-3.741734,-1.479207,1.695422,4.444385,5.111207,6.766721,-7.283650,-1.521125,-6.573685,1.796812,0.933515,8.538119,-8.017728,-3.639341,-3.312688,-7.708149,-5.861791,0.652202,-9.933604,8.453994,0.831107,5.311193,6.477839,-3.298908,-9.941734,5.139833,-1.971666,1.673541,-7.534699,7.011293,8.166980,6.940921,-4.154222,3.477573,3.492086,-9.588541,-8.391276,7.298958,5.792296,5.411871,9.572573,6.165748,-0.698467,-6.109547,-9.854348,9.431692,5.984041,5.517242,2.647413,-3.255803,7.761984,5.086851,-2.819029,6.196808,-3.019517,4.533522,-4.044096,4.290080,0.457438,2.622269,6.206327,3.796365,7.648070,-2.621642,-4.800250,-4.959459,0.923779,3.580112,-8.807177,3.255773,3.377230,-5.206420,6.091538,-9.129167,4.714591,5.164080,-1.205553,2.255228,7.076938,-9.027327,-8.345206,-7.788432,9.612988,5.017875,-6.005111,-8.450562,7.791142,2.837436,8.677999,2.336374,1.916932,6.671183,7.881738,-7.226223,7.251679,-0.958445,6.257385,0.018372,-6.449264,-3.572719,-0.915327,9.415887,2.584581,-4.209967,-2.525101,5.407589,-6.181151,-4.856711,2.039633,4.759450,8.346680,-4.034484,-2.979886,1.252556,-1.094345,0.951234,4.527345,-9.743389,-6.192288,7.241089,-2.123435,-8.272610,9.745739,-0.881922,0.571541,5.066657,-4.062431,5.030920,-6.424770,4.198233,-1.574774,3.826110,7.076225,-5.955829,-1.023742,9.300595,-8.935188,-1.734413,-1.249986,-6.914980,-7.963179,-2.006944,7.117451,3.509672,4.496665,-5.317696,9.231525,7.501733,2.047988,-0.350907,5.407828,-7.623706,-0.864514,8.204601,-8.811670,-1.295358,-3.449039,4.364442,4.615112,9.042904,1.612492,-5.371122,3.282106,-8.210807,-1.913114,-2.797138,-4.077841,7.020711,1.678223,9.620824,4.816440,-3.785922,-3.891914,4.939112,-7.492765,-4.118723,2.416787,5.397817,-2.827436,5.652742,-7.468760,-3.267709,4.393021,2.363700,6.549432,-6.054122,1.583606,-7.239904,-4.250866,1.820189,-7.831952,-8.484046,-5.550668,-2.271188,3.768340,2.875185,9.304190,-7.573248,-3.154974,-0.525337,-9.125908,-1.890313,1.205641,-5.913272,-2.853730,6.547320,2.536307,-0.994557,8.404676,1.076321,1.524506,-0.777250,-9.820622,8.704084,8.121308,-0.876987,-4.197548,8.716618,9.123939,5.281001,2.947325,-6.287436,-3.822207,-5.792768,7.605534,4.767150,6.350055,-4.462279,-7.749038,-3.270483,3.263922,-5.455799,4.080117,0.791926,3.301114,-5.273926,0.125458,1.705813,-3.705567,3.244479,9.680064,-8.902512,0.500558,2.898769,-1.011229,4.181814,-1.624522,3.347160,0.172306,0.248273,1.851106,5.793610,-4.559825,-1.322836,-5.126096,0.649856,-6.413437,-9.050489,-9.442449,-2.696005,0.116686,-7.476302,6.360093,7.893733,-3.797735,6.291472,6.700560,4.776364,4.965470,-7.700255,6.159776,-3.990797,5.269283,1.898300,-8.986243,-5.388460,1.635307,7.975757,-7.039026,0.696188,1.839144,-7.043195,9.948315,8.313640,9.629251,8.762862,9.983247,6.952604,-5.017514,-1.826325,-0.253204,3.523839,7.978988,-4.642035,0.716999,-0.797611,-6.208000,1.897261,-3.327811,-1.703177,-5.932452,6.905195,4.995195,-2.357039,1.750143,-3.044170,4.669230,-7.226204,0.751145,-5.775406,-9.264045,5.048170,5.025894,4.346351,8.036150,-0.515568,1.570134,6.843530,-4.399635,-6.874557,-3.111204,0.296650,-4.563614,-4.026432,-8.670847,8.281123,-4.502792,9.805737,6.174557,8.018711,-4.542122,8.315926,3.735928,5.676115,-7.774229,-1.580261,-3.228708,2.765059,1.956408,-1.839756,-0.475786,-8.536915,2.732753,7.445861,-2.434767,6.296123], dtype = "float64")#candidate|12503|(448,)|const|float64
call_12502 = func_8697_call(relay.reshape(const_12503.astype('float64'), [8, 14, 4]))
call_12504 = func_8697_call(relay.reshape(const_12503.astype('float64'), [8, 14, 4]))
output = relay.Tuple([call_12489,call_12502,const_12503,])
output2 = relay.Tuple([call_12490,call_12504,const_12503,])
func_12513 = relay.Function([], output)
mod['func_12513'] = func_12513
mod = relay.transform.InferType()(mod)
output = func_12513()
func_12514 = relay.Function([], output)
mutated_mod['func_12514'] = func_12514
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12011_call = mod.get_global_var('func_12011')
func_12012_call = mutated_mod.get_global_var('func_12012')
call_12561 = relay.TupleGetItem(func_12011_call(), 1)
call_12562 = relay.TupleGetItem(func_12012_call(), 1)
output = relay.Tuple([call_12561,])
output2 = relay.Tuple([call_12562,])
func_12563 = relay.Function([], output)
mod['func_12563'] = func_12563
mod = relay.transform.InferType()(mod)
mutated_mod['func_12563'] = func_12563
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12563_call = mutated_mod.get_global_var('func_12563')
call_12564 = func_12563_call()
output = call_12564
func_12565 = relay.Function([], output)
mutated_mod['func_12565'] = func_12565
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12011_call = mod.get_global_var('func_12011')
func_12012_call = mutated_mod.get_global_var('func_12012')
call_12719 = relay.TupleGetItem(func_12011_call(), 0)
call_12720 = relay.TupleGetItem(func_12012_call(), 0)
output = call_12719
output2 = call_12720
func_12722 = relay.Function([], output)
mod['func_12722'] = func_12722
mod = relay.transform.InferType()(mod)
mutated_mod['func_12722'] = func_12722
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12722_call = mutated_mod.get_global_var('func_12722')
call_12723 = func_12722_call()
output = call_12723
func_12724 = relay.Function([], output)
mutated_mod['func_12724'] = func_12724
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12563_call = mod.get_global_var('func_12563')
func_12565_call = mutated_mod.get_global_var('func_12565')
call_12728 = relay.TupleGetItem(func_12563_call(), 0)
call_12729 = relay.TupleGetItem(func_12565_call(), 0)
uop_12732 = relay.erf(call_12728.astype('float64')) # shape=(2, 6, 11)
uop_12734 = relay.erf(call_12729.astype('float64')) # shape=(2, 6, 11)
output = uop_12732
output2 = uop_12734
func_12737 = relay.Function([], output)
mod['func_12737'] = func_12737
mod = relay.transform.InferType()(mod)
mutated_mod['func_12737'] = func_12737
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12737_call = mutated_mod.get_global_var('func_12737')
call_12738 = func_12737_call()
output = call_12738
func_12739 = relay.Function([], output)
mutated_mod['func_12739'] = func_12739
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12563_call = mod.get_global_var('func_12563')
func_12565_call = mutated_mod.get_global_var('func_12565')
call_12829 = relay.TupleGetItem(func_12563_call(), 0)
call_12830 = relay.TupleGetItem(func_12565_call(), 0)
output = relay.Tuple([call_12829,])
output2 = relay.Tuple([call_12830,])
func_12838 = relay.Function([], output)
mod['func_12838'] = func_12838
mod = relay.transform.InferType()(mod)
mutated_mod['func_12838'] = func_12838
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12838_call = mutated_mod.get_global_var('func_12838')
call_12839 = func_12838_call()
output = call_12839
func_12840 = relay.Function([], output)
mutated_mod['func_12840'] = func_12840
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12838_call = mod.get_global_var('func_12838')
func_12840_call = mutated_mod.get_global_var('func_12840')
call_12862 = relay.TupleGetItem(func_12838_call(), 0)
call_12863 = relay.TupleGetItem(func_12840_call(), 0)
func_12722_call = mod.get_global_var('func_12722')
func_12724_call = mutated_mod.get_global_var('func_12724')
call_12864 = func_12722_call()
call_12865 = func_12722_call()
output = relay.Tuple([call_12862,call_12864,])
output2 = relay.Tuple([call_12863,call_12865,])
func_12866 = relay.Function([], output)
mod['func_12866'] = func_12866
mod = relay.transform.InferType()(mod)
output = func_12866()
func_12867 = relay.Function([], output)
mutated_mod['func_12867'] = func_12867
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12121_call = mod.get_global_var('func_12121')
func_12123_call = mutated_mod.get_global_var('func_12123')
call_12950 = relay.TupleGetItem(func_12121_call(), 0)
call_12951 = relay.TupleGetItem(func_12123_call(), 0)
func_10225_call = mod.get_global_var('func_10225')
func_10228_call = mutated_mod.get_global_var('func_10228')
const_12965 = relay.const([0.335152,-0.282576,2.824969,5.144256,8.416488,-6.599106,1.209958,-2.930195,2.445383,2.592807,8.300771,1.822331,-3.209258,-1.981313,3.552146], dtype = "float32")#candidate|12965|(15,)|const|float32
call_12964 = relay.TupleGetItem(func_10225_call(relay.reshape(const_12965.astype('float32'), [5, 1, 3])), 0)
call_12966 = relay.TupleGetItem(func_10228_call(relay.reshape(const_12965.astype('float32'), [5, 1, 3])), 0)
uop_12988 = relay.asin(call_12964.astype('float32')) # shape=(5, 1, 3)
uop_12990 = relay.asin(call_12966.astype('float32')) # shape=(5, 1, 3)
output = relay.Tuple([call_12950,const_12965,uop_12988,])
output2 = relay.Tuple([call_12951,const_12965,uop_12990,])
func_12993 = relay.Function([], output)
mod['func_12993'] = func_12993
mod = relay.transform.InferType()(mod)
output = func_12993()
func_12994 = relay.Function([], output)
mutated_mod['func_12994'] = func_12994
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12737_call = mod.get_global_var('func_12737')
func_12739_call = mutated_mod.get_global_var('func_12739')
call_13026 = func_12737_call()
call_13027 = func_12737_call()
var_13038 = relay.var("var_13038", dtype = "float64", shape = (2, 6, 11))#candidate|13038|(2, 6, 11)|var|float64
bop_13039 = relay.bitwise_or(call_13026.astype('uint32'), relay.reshape(var_13038.astype('uint32'), relay.shape_of(call_13026))) # shape=(2, 6, 11)
bop_13042 = relay.bitwise_or(call_13027.astype('uint32'), relay.reshape(var_13038.astype('uint32'), relay.shape_of(call_13027))) # shape=(2, 6, 11)
func_6906_call = mod.get_global_var('func_6906')
func_6909_call = mutated_mod.get_global_var('func_6909')
var_13054 = relay.var("var_13054", dtype = "float32", shape = (126, 1))#candidate|13054|(126, 1)|var|float32
call_13053 = func_6906_call(relay.reshape(var_13054.astype('float32'), [1, 9, 14]))
call_13055 = func_6906_call(relay.reshape(var_13054.astype('float32'), [1, 9, 14]))
output = relay.Tuple([bop_13039,call_13053,var_13054,])
output2 = relay.Tuple([bop_13042,call_13055,var_13054,])
func_13058 = relay.Function([var_13038,var_13054,], output)
mod['func_13058'] = func_13058
mod = relay.transform.InferType()(mod)
mutated_mod['func_13058'] = func_13058
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13058_call = mutated_mod.get_global_var('func_13058')
var_13060 = relay.var("var_13060", dtype = "float64", shape = (2, 6, 11))#candidate|13060|(2, 6, 11)|var|float64
var_13061 = relay.var("var_13061", dtype = "float32", shape = (126, 1))#candidate|13061|(126, 1)|var|float32
call_13059 = func_13058_call(var_13060,var_13061,)
output = call_13059
func_13062 = relay.Function([var_13060,var_13061,], output)
mutated_mod['func_13062'] = func_13062
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12993_call = mod.get_global_var('func_12993')
func_12994_call = mutated_mod.get_global_var('func_12994')
call_13064 = relay.TupleGetItem(func_12993_call(), 2)
call_13065 = relay.TupleGetItem(func_12994_call(), 2)
output = relay.Tuple([call_13064,])
output2 = relay.Tuple([call_13065,])
func_13081 = relay.Function([], output)
mod['func_13081'] = func_13081
mod = relay.transform.InferType()(mod)
mutated_mod['func_13081'] = func_13081
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13081_call = mutated_mod.get_global_var('func_13081')
call_13082 = func_13081_call()
output = call_13082
func_13083 = relay.Function([], output)
mutated_mod['func_13083'] = func_13083
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12011_call = mod.get_global_var('func_12011')
func_12012_call = mutated_mod.get_global_var('func_12012')
call_13098 = relay.TupleGetItem(func_12011_call(), 1)
call_13099 = relay.TupleGetItem(func_12012_call(), 1)
func_12272_call = mod.get_global_var('func_12272')
func_12274_call = mutated_mod.get_global_var('func_12274')
const_13131 = relay.const([2,-6,8,4,-5,6,2,-1,6,6,8,5,-8,-3,2,9,-1,-3,-8,-10,3,-4,9,-10,1,-6,-3,-2,-1,-8,-10,-9,4,1,10,-5,-5,-7,-6,-3,2,-9,-10,10,7,-6,-6,1,-8,2,-2,-8,7,3,-2,-2,6,1,-4,1,8,-2,2,-4,4,6,-2,4,10,3,-6,6,8,-1,-8,-6,8,1,-1,-2,-5,-10,-5,-6,-2,6,-8,9,2,10,10,6,-4,-2,6,-10,2,-7,4,3,4,3,4,8,2,7,4,4,4,6,9,10,6,10,3,-8,-3,-1,-5,-4,-8,2,6,-3,1,-2,-5,-2,2,-3,-3,5,3,4,6,-4,-1,-8,2,7,1,2,2,7,5,-10,-10,-4,-3,-1,-6,-5,1,4,-5,7,-10,1,2,-7,-5,-5,4,-10,-10,5,-5,-3,-4,-2,-7,6,-7,-3,-3,7,-9,-7,-4,9,-7,9,5,-10,6,9,-2,-3,1,9,-8,6,-1,-10,9,10,-4,-7,9,-9,3,10,-4,-4,1,-1,-2,-6,-9,7,-8,1,5,10,-9,-1,-8,10,8,-8,-7,-9,7,1,4,3,6,3,-6,-7,3,-9,-1,-4,1,1,5,9,7,-8,-8,2,-7,-5,-9,7,-10,-4,5,3,4,-8,-4,-10,6,4,1,10,-3,10,-7,6,5,-2,2,8,9,-4,10,-8,2,-10,9,10,5,6,8,1,3,-2,1,2,6,5,-10,2,-4,-4,2,-5,-5,-1,2,-6,7,4,8,8,-2,9,5,-1,-6,1,2,-5,4,9,1,-5,-3,-8,4,6,10,-5,9,-3,-4,2,-8,-2,4,2,-7,6,7,3,-10,7,-6,-3,10,-9,10,-10,-8,-5,-4,-10,4,-10,-7,-2,2,5,2,1,5,6,-9,8,-9,-2,9,-3,-5,4,4,9,7,-3,5,1,-4,-9,-5,2,7,-6,-5,9,-2,4,-1,3,8,-7,10,6,6,8,-10,5,4,6,-10,9,-10,-9,5,-10,-8,9,4,-1,-9,-2,-9,10,8,-3,1,-2,7,5,-7,-7,2,4,-1,6,6,-1,-5,-8,-9,3,5,2,-9,3,1,-1,-8,-9,-2,9,5,10,-2,-4,1,10,3,9,-10,7,4,2,-5,-1,8,-4,1,-4,4,6,5,3,-10,9,-7,-1,8,-3,4,9,-3,4,7,-8,6,-8,10,9,6,-9,-6,-1,4,7,-7,2,1,5,6,1,-5,-2,-10,4,1,-6,4,3,-3,-7,-9,2,5,-8,-1,2,5,3,-7,1,10,6,7,3,-10,-10,-7,6,2,-2,10,8,-10,-3,8,6,1,4,-9,-8,7,-7,2,8,-7,6,-6,7,7,-2,3,-3,-10,-4,5,-10,-2,7,-2,8,5,9,8,7,5,10,-9,-4,-1,-2,2,7,10,-8,10,2,-1,7,6,-7,-5,-8,-2,-7,-1,-9,10,-7,-1,3,-4,-7,5,-4,-9,-1,-10,1,1,4,7,-5,9,-7,8,2,-4,-6,-2,-7,3,-7,7,4,-6,-10,-10,-1,-8,7,-8,-9,-7,-1,-7,-2,-6,-5,7,-1,-6,7,7,-4,4,-10,-2,7,5,-8,6,-5,7,7,7,-6,-8,-8,-10,-9,-4,9,9,-3,3,7,1,2,-1,-3,-7,-1,3,2,-10,10,-10,-7,-4,-5,6,-4,5,-7,5,3,3,6,3,-9,-7,-6,7,-7,-6,8,6,10,-10,-8,-9,4,4,5,-6,-10,-5,-3,10,3,-4,-9,-5,-2,6,-7,-10,4,-2,1,7,-2,-6,3,7,-3,7,1,-8,6,-4,8,5,-10,-3,5,-2,2,-4,-5,1,1,-9,1,-7,1,9,5,-1,2,-6,6,6,8,-3,10,-1,3,1,-9,-10,-2,-10,-6,2,7,-5,-7,-2,-10,8,-10,-10,10,8,2,10,8,10,2,-2,-1,-3,9,-3,-2,-10,3,7,3,-3,-3,8,-4,9,-10,7,9,10,-7,6,8,-2,-8,-4,-4,4,1,-3,10,-1,1,4,9,-8,10,8,2,7,-8,-8,8,-2,-6,4,-4,-10,4,-7,-1,1,-10,9,10,-1,7,-3,-5,-3,-7,-9,-1,-8,-3,8,-1,-5,-8,5,10,-6,-7,-3,-1,3,3,-3,-1,9,-7,9,-6,8,-9,-9,1,6,-4,10,5,-7,7,5,10,-3,-1,-4,-9,8,-5,6,4,-4,3,6,-9,-8,-1,-6,7,8,6,-2,2,10,8,-5,-10,-3,-5,10,-1,4,-3,5,-2,7,-2,-10,2,-4,-7,-5,10,-9,8,-10,-10,-3,5,-5,8,4,3,-4,7,5,9,-1,9,-5,-9,-6,-7,2,-4,10,10,-1,1,8,-5,2,-5,4,-2,1,-4,-10,5,-5,-10,-2,-1,3,-10,10,8,-1,4,8,-4,7,7,1,1,2,2,-4,-7,-7,-10,2,10,2,9,-1,-1,5,8,-10,3,-4,8,-2,-5,-1,7,-4,9,2,-7,2,-3,-6,4,-4,9,-6,6,-1,-6,-7,-6,-1,-10,-2,5,-3,-3,-1,-6,-6,3,-10,-7,-9,3,-7,10,5,-10,-4,-5,3,-7,-6,1,8,1,2,-10,4,-8,6,8,7,10,-3,10,4,-2,2,2,7,9,3,10,-7,-10,-6,6,-8,-5,-3,1,-4,-8,6,6,3,-3,-9,6,1,6,-8,-1,1,9,10,-9,-3,-1,-7,4,-4,-6,10,-8,-10,8,-9,4,4,-1,-5,9,9,1,-8,-4,2,7,4,4,-10,-1,1,6,-3,2,-9,-8,-2,2,3,-4,8,8,-7,-5,5,7,-1,3,-9,-2,7,-7,-8,-1,-7,-4,8,-4,-4,-5,4,7,2,1,-9,2,-2,5,7,9,-10,-8,6,-7,-10,-1,2,-2,-2,-8,6,6,-8,-8,-4,-9,-1,-7,9,-9,-4,-5,-2,3,-8,4,-2,1,-1,4,-5,4,-10,-5,2,-7,-6,-5,9,-2,-10,2,9,1,-2,5,-8,5,9,6,-2,10,-7,-8,-4,7,9,5,5,-7,-10,6,3,-5,-1,-6,6,-3,-2,1,-1,1,10,-9,-1,-3,3,9,1,10,5,-5,3,-3,-8,2,-3,-1,-10,-7,9,2,-9,9,4,-4,-5,-9,-8,3,9,7,-10,-4,-3,1,-10,5,5,1,-5,-10,3,-9,4,-9,9,4,8,-10,-8,2,-6,-7,-3,10,-3,-8,-2,1,3,8,8,3,-7,-9,-4,4,10,-10,-2,-10,-1,-5,-9,8,6,4,-7,2,-10,10,1,-5,-7,-3,5,6,-6,-10,5,5,-5,7,-5,-5,-7,-10,-9,9,-10,-5,-8,3,-1,-8,-3,10,-1,-8,-4,-3,8,-9,-8,10,-3,-3,5,-6,10,-3,-7,3,-9,-8,3,-6,-5,-7,5,3,4,8,3,-6,-10,-10,-3,6,-3,7,-6,-7,9,-5,3,10,-5,7,-4,5,-3,10,-5,9,3,-5,10,1,6,-4,6,-4,-4,-1,3,10,-10,-3,-9,4,-10,-10], dtype = "uint16")#candidate|13131|(1350,)|const|uint16
call_13130 = relay.TupleGetItem(func_12272_call(relay.reshape(const_13131.astype('uint16'), [1350,])), 0)
call_13132 = relay.TupleGetItem(func_12274_call(relay.reshape(const_13131.astype('uint16'), [1350,])), 0)
func_11630_call = mod.get_global_var('func_11630')
func_11633_call = mutated_mod.get_global_var('func_11633')
var_13134 = relay.var("var_13134", dtype = "float64", shape = (975, 1))#candidate|13134|(975, 1)|var|float64
const_13135 = relay.const(8.966554, dtype = "float32")#candidate|13135|()|const|float32
call_13133 = relay.TupleGetItem(func_11630_call(relay.reshape(var_13134.astype('float64'), [13, 15, 5]), relay.reshape(const_13135.astype('float32'), []), ), 3)
call_13136 = relay.TupleGetItem(func_11633_call(relay.reshape(var_13134.astype('float64'), [13, 15, 5]), relay.reshape(const_13135.astype('float32'), []), ), 3)
output = relay.Tuple([call_13098,call_13130,const_13131,call_13133,var_13134,const_13135,])
output2 = relay.Tuple([call_13099,call_13132,const_13131,call_13136,var_13134,const_13135,])
func_13137 = relay.Function([var_13134,], output)
mod['func_13137'] = func_13137
mod = relay.transform.InferType()(mod)
mutated_mod['func_13137'] = func_13137
mutated_mod = relay.transform.InferType()(mutated_mod)
var_13138 = relay.var("var_13138", dtype = "float64", shape = (975, 1))#candidate|13138|(975, 1)|var|float64
func_13137_call = mutated_mod.get_global_var('func_13137')
call_13139 = func_13137_call(var_13138)
output = call_13139
func_13140 = relay.Function([var_13138], output)
mutated_mod['func_13140'] = func_13140
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12121_call = mod.get_global_var('func_12121')
func_12123_call = mutated_mod.get_global_var('func_12123')
call_13169 = relay.TupleGetItem(func_12121_call(), 0)
call_13170 = relay.TupleGetItem(func_12123_call(), 0)
func_6236_call = mod.get_global_var('func_6236')
func_6238_call = mutated_mod.get_global_var('func_6238')
const_13178 = relay.const([4.913751,1.750528,2.077808,-2.096881,4.932619,2.375134,-2.063473,-2.164168,9.232450,5.948003,-2.860155,6.358128,5.301321,-1.626503,4.990166,2.575287,5.219436,1.553009,-7.423231,-6.938592,-5.109941,-8.219931,5.649470,9.516330,-3.758180,3.424094,-0.775902,-5.477703,-5.560311,3.968772,1.094413,-4.728695,2.815374,0.712727,2.708353,-1.741272,6.162729,9.017742,6.536260,9.860721,5.732214,-6.324542,5.337826,5.997550,5.106118,5.521853,4.226179,-5.536790,8.102762,-9.011874,6.744861,-8.820200,-7.507814,-0.926824,1.284359,8.934955,-0.749799,-9.453128,-8.954130,8.335586,-5.506207,-8.089953,-1.785992,5.589851,-7.528495,-0.437347,-5.049811,5.045080,-3.330960,-7.945840,6.457530,1.982488,0.351549,-5.834599,7.379714,-0.798298,-8.770660,-4.622854,7.382561,9.442117,4.874648,3.639372,-0.253535,-5.415480,-2.146011,-7.271529,3.683593,5.881749,-9.801369,-7.466000,4.662484,1.447018,-9.509108,-0.235425,0.427912,1.287560], dtype = "float32")#candidate|13178|(96,)|const|float32
call_13177 = func_6236_call(relay.reshape(const_13178.astype('float32'), [2, 4, 12]))
call_13179 = func_6236_call(relay.reshape(const_13178.astype('float32'), [2, 4, 12]))
func_12272_call = mod.get_global_var('func_12272')
func_12274_call = mutated_mod.get_global_var('func_12274')
var_13187 = relay.var("var_13187", dtype = "uint16", shape = (1350,))#candidate|13187|(1350,)|var|uint16
call_13186 = relay.TupleGetItem(func_12272_call(relay.reshape(var_13187.astype('uint16'), [1350,])), 5)
call_13188 = relay.TupleGetItem(func_12274_call(relay.reshape(var_13187.astype('uint16'), [1350,])), 5)
func_2297_call = mod.get_global_var('func_2297')
func_2300_call = mutated_mod.get_global_var('func_2300')
const_13192 = relay.const(-3.202567, dtype = "float32")#candidate|13192|()|const|float32
var_13193 = relay.var("var_13193", dtype = "float32", shape = (220,))#candidate|13193|(220,)|var|float32
call_13191 = func_2297_call(relay.reshape(const_13192.astype('float32'), []), relay.reshape(var_13193.astype('float32'), [11, 5, 4]), )
call_13194 = func_2297_call(relay.reshape(const_13192.astype('float32'), []), relay.reshape(var_13193.astype('float32'), [11, 5, 4]), )
func_8697_call = mod.get_global_var('func_8697')
func_8700_call = mutated_mod.get_global_var('func_8700')
var_13201 = relay.var("var_13201", dtype = "float64", shape = (56, 8))#candidate|13201|(56, 8)|var|float64
call_13200 = func_8697_call(relay.reshape(var_13201.astype('float64'), [8, 14, 4]))
call_13202 = func_8697_call(relay.reshape(var_13201.astype('float64'), [8, 14, 4]))
uop_13203 = relay.cos(call_13169.astype('float32')) # shape=(2, 6, 11)
uop_13205 = relay.cos(call_13170.astype('float32')) # shape=(2, 6, 11)
func_12448_call = mod.get_global_var('func_12448')
func_12450_call = mutated_mod.get_global_var('func_12450')
call_13218 = relay.TupleGetItem(func_12448_call(), 0)
call_13219 = relay.TupleGetItem(func_12450_call(), 0)
output = relay.Tuple([call_13177,const_13178,call_13186,var_13187,call_13191,const_13192,var_13193,call_13200,var_13201,uop_13203,call_13218,])
output2 = relay.Tuple([call_13179,const_13178,call_13188,var_13187,call_13194,const_13192,var_13193,call_13202,var_13201,uop_13205,call_13219,])
func_13223 = relay.Function([var_13187,var_13193,var_13201,], output)
mod['func_13223'] = func_13223
mod = relay.transform.InferType()(mod)
var_13224 = relay.var("var_13224", dtype = "uint16", shape = (1350,))#candidate|13224|(1350,)|var|uint16
var_13225 = relay.var("var_13225", dtype = "float32", shape = (220,))#candidate|13225|(220,)|var|float32
var_13226 = relay.var("var_13226", dtype = "float64", shape = (56, 8))#candidate|13226|(56, 8)|var|float64
output = func_13223(var_13224,var_13225,var_13226,)
func_13227 = relay.Function([var_13224,var_13225,var_13226,], output)
mutated_mod['func_13227'] = func_13227
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12737_call = mod.get_global_var('func_12737')
func_12739_call = mutated_mod.get_global_var('func_12739')
call_13232 = func_12737_call()
call_13233 = func_12737_call()
var_13248 = relay.var("var_13248", dtype = "float64", shape = (2, 6, 11))#candidate|13248|(2, 6, 11)|var|float64
bop_13249 = relay.mod(call_13232.astype('float32'), relay.reshape(var_13248.astype('float32'), relay.shape_of(call_13232))) # shape=(2, 6, 11)
bop_13252 = relay.mod(call_13233.astype('float32'), relay.reshape(var_13248.astype('float32'), relay.shape_of(call_13233))) # shape=(2, 6, 11)
output = relay.Tuple([bop_13249,])
output2 = relay.Tuple([bop_13252,])
func_13256 = relay.Function([var_13248,], output)
mod['func_13256'] = func_13256
mod = relay.transform.InferType()(mod)
var_13257 = relay.var("var_13257", dtype = "float64", shape = (2, 6, 11))#candidate|13257|(2, 6, 11)|var|float64
output = func_13256(var_13257)
func_13258 = relay.Function([var_13257], output)
mutated_mod['func_13258'] = func_13258
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12838_call = mod.get_global_var('func_12838')
func_12840_call = mutated_mod.get_global_var('func_12840')
call_13290 = relay.TupleGetItem(func_12838_call(), 0)
call_13291 = relay.TupleGetItem(func_12840_call(), 0)
var_13292 = relay.var("var_13292", dtype = "float64", shape = (2, 6, 11))#candidate|13292|(2, 6, 11)|var|float64
bop_13293 = relay.not_equal(call_13290.astype('bool'), relay.reshape(var_13292.astype('bool'), relay.shape_of(call_13290))) # shape=(2, 6, 11)
bop_13296 = relay.not_equal(call_13291.astype('bool'), relay.reshape(var_13292.astype('bool'), relay.shape_of(call_13291))) # shape=(2, 6, 11)
output = bop_13293
output2 = bop_13296
func_13298 = relay.Function([var_13292,], output)
mod['func_13298'] = func_13298
mod = relay.transform.InferType()(mod)
var_13299 = relay.var("var_13299", dtype = "float64", shape = (2, 6, 11))#candidate|13299|(2, 6, 11)|var|float64
output = func_13298(var_13299)
func_13300 = relay.Function([var_13299], output)
mutated_mod['func_13300'] = func_13300
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11837_call = mod.get_global_var('func_11837')
func_11838_call = mutated_mod.get_global_var('func_11838')
call_13398 = relay.TupleGetItem(func_11837_call(), 0)
call_13399 = relay.TupleGetItem(func_11838_call(), 0)
func_5067_call = mod.get_global_var('func_5067')
func_5072_call = mutated_mod.get_global_var('func_5072')
var_13404 = relay.var("var_13404", dtype = "float32", shape = (132, 2))#candidate|13404|(132, 2)|var|float32
const_13405 = relay.const([9.838382,1.718004,5.278093,9.341182,1.363924,-5.048179,6.864536,-9.956660,0.080612,-1.071641,1.799221,5.896319,7.059495,-3.384167,5.918546,1.429728,7.358679,-1.912993,4.864908,2.170436,-0.714664,-9.513086,5.482071,1.275650,4.261155,-4.696958,1.854395,0.347177,-0.048108,5.863622,-5.071031,6.206073,3.726931,-7.435862,2.424605,4.669286,6.361573,-2.183456,-6.630280,-9.296805,3.431079,-1.234894,-9.750154,1.926859,-5.852384,0.463099,-0.523940,-4.721895,-9.642260,-4.842099,8.221299,-7.614704,-2.669369,5.677022,-4.450856,-4.784285,4.938502,-0.761953,-2.224395,-1.155847,-3.758391,3.177463,-8.847029,3.021088,1.135138,8.464244,3.792882,3.716566,-7.140126,8.782671,-6.720494,-3.433493,-8.052775,-1.598449,9.917068,7.535012,-2.104626,-0.040656,1.758129,9.887157,6.082033,4.439506,-5.411154,-7.083356,2.329200,-3.645586,-0.829563,3.711517,6.942590,4.446322,1.732583,8.310861,-3.065393,-7.263725,9.246659,-7.081133,-3.877444,8.017813,-8.835606,0.728463,7.942562,-7.624565,9.546638,8.618616,2.790438,7.061693,9.918347,-2.280947,-6.822100,5.824476,-6.146807,-3.264117,4.068192,-2.536781,-2.035302,-0.178519,4.332407,4.312717,-1.398104,6.638629,5.234131,-2.369433,3.117737,-7.589561,-9.675380,1.671622,7.259140,3.646885,-3.167924,3.483970,-7.691524,-9.281175,-6.126389,-9.875866,-1.912225,-6.069239,-5.814699,2.122592,6.866850,3.188961,7.734512,-7.940564,-7.699107,-6.528934,9.355026,2.510194,9.530278,5.626421,2.078159,-8.599231,-3.580850,-7.946872,-7.342227,-1.599591,8.456419,7.572689,2.051348,-4.236956,7.066100,-3.704241,-7.408537,-0.128898,8.454296,4.540387,6.715489,2.140772,-5.997806,-0.151478,6.168840,-8.715489,-6.001620,0.974557,3.748243,-8.189035,-9.716664,-3.974283,-0.907157,-9.432809,-6.948763,5.109682,-8.629408,3.784423,-0.970369,6.674381,8.147298,-2.534387,5.255295,0.939009,2.970621,3.653461,-0.211085,-5.536346,4.092038,-5.696807,-9.179069,8.009567,-6.013930,2.174943,3.574192,-4.266467,-1.772771,-5.487727,2.926315,2.112557,4.742501,-7.663484,-2.399389,0.664058,-4.195285,4.273388,1.586746,1.341762,-8.267475,-9.861329,3.277715,-3.407465,2.056202,5.835891,-2.378132,-8.217893,1.495828,6.666927,1.553675,4.012214,-1.831863,8.943155,-8.344098,-0.109646,6.619542,-7.592291,8.812676,8.574234,6.257337,3.140434,5.064719,-7.949238,8.430425,-1.996347,-4.102290,-3.069784,-5.428566,-7.398652,-2.410755,4.425164,4.351123,-9.117316,-6.650889,3.998570,-3.863555,7.641611,-3.194100,-7.872877,6.732743,4.665011,8.347456,2.797472,8.654952,-2.561404,-5.238795,9.386222,5.480044,-5.012602,2.390601,8.429442,2.481195,1.716394,-3.049697,9.544233,-0.601429,2.107481,-4.757543,-6.838705,-8.808597,6.931919,-5.015396,-3.482254,-6.286892,-9.814677,9.256872,2.378156,-3.517604,-0.955864,-9.796619,8.317107,-9.275330,-6.783824,3.205075,-0.769646,8.672372,-6.251331,2.351277,8.428224,6.815505,5.807180,-4.769544,7.456491,-0.200504,7.166626,1.733832,4.029504], dtype = "float64")#candidate|13405|(300,)|const|float64
var_13406 = relay.var("var_13406", dtype = "int64", shape = (8, 56))#candidate|13406|(8, 56)|var|int64
call_13403 = relay.TupleGetItem(func_5067_call(relay.reshape(var_13404.astype('float32'), [12, 2, 11]), relay.reshape(const_13405.astype('float64'), [300,]), relay.reshape(var_13406.astype('int64'), [224, 2]), ), 1)
call_13407 = relay.TupleGetItem(func_5072_call(relay.reshape(var_13404.astype('float32'), [12, 2, 11]), relay.reshape(const_13405.astype('float64'), [300,]), relay.reshape(var_13406.astype('int64'), [224, 2]), ), 1)
func_13298_call = mod.get_global_var('func_13298')
func_13300_call = mutated_mod.get_global_var('func_13300')
call_13408 = func_13298_call(relay.reshape(call_13398.astype('float64'), [2, 6, 11]))
call_13409 = func_13298_call(relay.reshape(call_13398.astype('float64'), [2, 6, 11]))
output = relay.Tuple([call_13398,call_13403,var_13404,const_13405,var_13406,call_13408,])
output2 = relay.Tuple([call_13399,call_13407,var_13404,const_13405,var_13406,call_13409,])
func_13412 = relay.Function([var_13404,var_13406,], output)
mod['func_13412'] = func_13412
mod = relay.transform.InferType()(mod)
mutated_mod['func_13412'] = func_13412
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13412_call = mutated_mod.get_global_var('func_13412')
var_13414 = relay.var("var_13414", dtype = "float32", shape = (132, 2))#candidate|13414|(132, 2)|var|float32
var_13415 = relay.var("var_13415", dtype = "int64", shape = (8, 56))#candidate|13415|(8, 56)|var|int64
call_13413 = func_13412_call(var_13414,var_13415,)
output = call_13413
func_13416 = relay.Function([var_13414,var_13415,], output)
mutated_mod['func_13416'] = func_13416
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11837_call = mod.get_global_var('func_11837')
func_11838_call = mutated_mod.get_global_var('func_11838')
call_13420 = relay.TupleGetItem(func_11837_call(), 0)
call_13421 = relay.TupleGetItem(func_11838_call(), 0)
output = relay.Tuple([call_13420,])
output2 = relay.Tuple([call_13421,])
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
func_12121_call = mod.get_global_var('func_12121')
func_12123_call = mutated_mod.get_global_var('func_12123')
call_13455 = relay.TupleGetItem(func_12121_call(), 0)
call_13456 = relay.TupleGetItem(func_12123_call(), 0)
func_5320_call = mod.get_global_var('func_5320')
func_5323_call = mutated_mod.get_global_var('func_5323')
const_13470 = relay.const([-10,-2,-7,6,5,3,7,-5,10,10,-10,-7,-9,-6,-4,6,7,-5,-4,-6,-2,1,6,-6,7,-10,10,-5,-4,4,1,-3,1,-3,-8,-3,7,4,1,-2,7,5,-1,-6,3,-2,1,3,3,6,4,-6,5,-6,1,5,4,-3,2,10,3,-10,-7,-6,-6,4,2,-2,-9,5,10,7,-10,7,-4,-7,-8,9,7,-6,8,2,-9,8,5,-9,3,-7,8,5,2,7,7,5,-3,-7,-2,-10,-5,10,-2,-5,7,-6,-7,-7,2,-8,1,-3,8,-5,2,3,6,7,4,-2,5,8,-10,-10,-10,-1,6,7,-5,4,2,5,3,-5,-6,-10,5,-5,-4,7,-5,-6,2,5,-8,5,8,-7,5,-8,6,-4,-7,-8,-3,-6,3,9,5,-5,5,-4,-1,4,2,-7,-3,1,-9,2,6,-10,9,-6,-7,9,2,-5,-4,-9,2,-7,8,-6,9,-8,-3,5,2,-6,2,-1,1,-9,4,1,5,-2,8,-9,3,3,8,9,9,8,-3,8,-2,8,5,3], dtype = "int16")#candidate|13470|(210,)|const|int16
call_13469 = relay.TupleGetItem(func_5320_call(relay.reshape(const_13470.astype('int16'), [7, 6, 5])), 0)
call_13471 = relay.TupleGetItem(func_5323_call(relay.reshape(const_13470.astype('int16'), [7, 6, 5])), 0)
output = relay.Tuple([call_13455,call_13469,const_13470,])
output2 = relay.Tuple([call_13456,call_13471,const_13470,])
func_13499 = relay.Function([], output)
mod['func_13499'] = func_13499
mod = relay.transform.InferType()(mod)
output = func_13499()
func_13500 = relay.Function([], output)
mutated_mod['func_13500'] = func_13500
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12448_call = mod.get_global_var('func_12448')
func_12450_call = mutated_mod.get_global_var('func_12450')
call_13545 = relay.TupleGetItem(func_12448_call(), 0)
call_13546 = relay.TupleGetItem(func_12450_call(), 0)
func_12166_call = mod.get_global_var('func_12166')
func_12169_call = mutated_mod.get_global_var('func_12169')
call_13572 = relay.TupleGetItem(func_12166_call(relay.reshape(call_13545.astype('float64'), [2, 6, 11])), 0)
call_13573 = relay.TupleGetItem(func_12169_call(relay.reshape(call_13545.astype('float64'), [2, 6, 11])), 0)
output = relay.Tuple([call_13545,call_13572,])
output2 = relay.Tuple([call_13546,call_13573,])
func_13582 = relay.Function([], output)
mod['func_13582'] = func_13582
mod = relay.transform.InferType()(mod)
output = func_13582()
func_13583 = relay.Function([], output)
mutated_mod['func_13583'] = func_13583
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12563_call = mod.get_global_var('func_12563')
func_12565_call = mutated_mod.get_global_var('func_12565')
call_13630 = relay.TupleGetItem(func_12563_call(), 0)
call_13631 = relay.TupleGetItem(func_12565_call(), 0)
output = relay.Tuple([call_13630,])
output2 = relay.Tuple([call_13631,])
func_13645 = relay.Function([], output)
mod['func_13645'] = func_13645
mod = relay.transform.InferType()(mod)
output = func_13645()
func_13646 = relay.Function([], output)
mutated_mod['func_13646'] = func_13646
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13582_call = mod.get_global_var('func_13582')
func_13583_call = mutated_mod.get_global_var('func_13583')
call_13683 = relay.TupleGetItem(func_13582_call(), 1)
call_13684 = relay.TupleGetItem(func_13583_call(), 1)
func_12838_call = mod.get_global_var('func_12838')
func_12840_call = mutated_mod.get_global_var('func_12840')
call_13702 = relay.TupleGetItem(func_12838_call(), 0)
call_13703 = relay.TupleGetItem(func_12840_call(), 0)
func_12513_call = mod.get_global_var('func_12513')
func_12514_call = mutated_mod.get_global_var('func_12514')
call_13718 = relay.TupleGetItem(func_12513_call(), 0)
call_13719 = relay.TupleGetItem(func_12514_call(), 0)
output = relay.Tuple([call_13683,call_13702,call_13718,])
output2 = relay.Tuple([call_13684,call_13703,call_13719,])
func_13726 = relay.Function([], output)
mod['func_13726'] = func_13726
mod = relay.transform.InferType()(mod)
output = func_13726()
func_13727 = relay.Function([], output)
mutated_mod['func_13727'] = func_13727
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12838_call = mod.get_global_var('func_12838')
func_12840_call = mutated_mod.get_global_var('func_12840')
call_13738 = relay.TupleGetItem(func_12838_call(), 0)
call_13739 = relay.TupleGetItem(func_12840_call(), 0)
output = relay.Tuple([call_13738,])
output2 = relay.Tuple([call_13739,])
func_13753 = relay.Function([], output)
mod['func_13753'] = func_13753
mod = relay.transform.InferType()(mod)
mutated_mod['func_13753'] = func_13753
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13753_call = mutated_mod.get_global_var('func_13753')
call_13754 = func_13753_call()
output = call_13754
func_13755 = relay.Function([], output)
mutated_mod['func_13755'] = func_13755
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13582_call = mod.get_global_var('func_13582')
func_13583_call = mutated_mod.get_global_var('func_13583')
call_13762 = relay.TupleGetItem(func_13582_call(), 1)
call_13763 = relay.TupleGetItem(func_13583_call(), 1)
func_8304_call = mod.get_global_var('func_8304')
func_8307_call = mutated_mod.get_global_var('func_8307')
var_13796 = relay.var("var_13796", dtype = "float32", shape = (540,))#candidate|13796|(540,)|var|float32
call_13795 = func_8304_call(relay.reshape(var_13796.astype('float32'), [15, 12, 3]))
call_13797 = func_8304_call(relay.reshape(var_13796.astype('float32'), [15, 12, 3]))
func_2005_call = mod.get_global_var('func_2005')
func_2008_call = mutated_mod.get_global_var('func_2008')
const_13799 = relay.const([[6.679959,-3.611262,1.674948,1.544685,-7.026265,-3.434686,4.339691,1.746827,-4.082716,9.000403,-7.385665,6.853433,3.456464,5.546260,1.491362,-8.011425,8.141296,0.913448,-7.420807,1.215839,5.976626,-8.929257,3.793295,2.023803,7.503422,0.373758,-3.827232,4.455848,-5.908729,3.751593],[5.435148,-1.946874,-6.133091,7.362898,-3.090466,8.022575,-3.702108,-7.627701,-5.279704,4.232642,-3.491135,0.112247,-9.202248,-5.577626,8.990161,-8.827273,-5.937299,2.240783,5.388355,3.030694,2.060776,4.563525,-6.472159,-0.591010,8.088816,9.777960,-2.652775,-1.758823,9.456467,3.992158],[8.332629,-0.005596,9.409628,-6.076385,-1.089599,-0.108514,2.780775,-1.267034,-8.880716,-4.927143,-1.745681,0.012559,-5.498910,7.012054,3.504883,-8.178512,3.860972,-5.010612,-1.820274,2.418817,-4.894239,9.345832,2.568278,-0.261859,-9.070489,2.236109,-7.048306,9.662677,7.763226,-9.670125],[-7.003311,4.443926,5.430816,-9.537747,-5.043342,6.412295,3.231591,-5.344373,-9.603928,-4.964568,2.364292,3.001995,0.333526,-4.742530,-8.220112,5.090644,9.310136,-5.266075,-5.045403,4.792022,-3.406056,0.741981,9.742796,-2.705594,-9.651110,-8.966511,-3.482861,8.665998,-8.744212,-8.657095],[6.046119,4.632224,-9.979434,6.302409,-7.232082,-2.023008,7.835661,5.131257,4.518540,-9.474787,-0.639651,-7.454372,6.239998,-8.875271,9.938105,-8.380480,-4.642914,-0.789377,6.216314,5.296892,-9.025441,-2.312135,-9.982628,-1.479591,0.790713,7.562269,5.640776,-9.999683,-7.106278,-3.113386],[-0.335995,-5.236078,6.828411,2.909040,-5.255384,-1.550166,-3.852733,6.021688,-7.453921,7.645836,-7.391323,-5.496872,-7.606578,-4.777008,9.712470,-1.117805,4.566227,6.257256,8.204240,7.999352,6.262861,-9.162483,-7.185720,-9.773583,1.847297,-6.209587,4.628624,9.367584,-0.668281,-6.915331],[5.735596,9.337370,5.788150,1.897544,3.161361,-4.836485,-9.678538,0.584969,-7.597905,-5.515104,0.714705,-6.969591,1.224916,-8.161198,3.005392,1.289579,3.560374,-3.806882,1.446146,-3.040024,-2.100552,-6.540505,4.001537,-6.556307,8.750547,-8.039941,2.049741,4.839710,-8.322923,-3.959090],[-3.750995,-0.519386,-5.769908,-0.126766,-4.883591,2.076735,-8.700551,-2.908812,8.550544,6.681537,8.890654,4.509416,-3.172979,1.497112,-0.969104,1.608269,3.543575,-7.722764,-6.747685,-3.229443,7.553748,6.094786,7.173968,-3.506820,-2.507163,0.540141,5.433558,1.005031,-1.836142,-9.654547],[-5.545731,2.306330,-8.570432,-9.435366,8.767420,0.059664,-5.447261,-7.626635,-6.458031,-0.744821,-7.432097,-6.722729,-7.288411,-4.271247,-0.093257,4.038913,-6.700541,5.154867,-1.019153,1.384516,-5.839395,3.416882,2.471092,-1.008313,-6.511278,8.650729,-4.137878,-6.270674,7.102495,2.166781],[7.204384,-0.163319,-9.926333,-9.815638,7.044864,-1.861241,0.105313,-4.408400,5.163235,-9.918546,3.615105,-1.683949,-5.091886,-1.049769,4.126787,3.056743,-5.776968,-7.394823,6.815094,-6.278086,-7.525690,-1.644104,-3.451797,3.366767,2.312596,5.303125,6.136213,3.778747,-4.893578,1.108714]], dtype = "float64")#candidate|13799|(10, 30)|const|float64
call_13798 = func_2005_call(relay.reshape(const_13799.astype('float64'), [5, 12, 5]))
call_13800 = func_2005_call(relay.reshape(const_13799.astype('float64'), [5, 12, 5]))
bop_13806 = relay.maximum(const_13799.astype('uint8'), relay.reshape(call_13798.astype('uint8'), relay.shape_of(const_13799))) # shape=(10, 30)
bop_13809 = relay.maximum(const_13799.astype('uint8'), relay.reshape(call_13800.astype('uint8'), relay.shape_of(const_13799))) # shape=(10, 30)
uop_13812 = relay.cos(bop_13806.astype('float64')) # shape=(10, 30)
uop_13814 = relay.cos(bop_13809.astype('float64')) # shape=(10, 30)
const_13819 = relay.const([[5.874533,8.586965,-8.462332,-2.644532,1.544607,-6.974320,-8.481403,-0.577293,-4.745233,2.506251,1.474158,1.991508,-0.278567,-5.582528,5.483662,-2.575591,-1.836472,8.757459,9.618662,5.922329,5.659574,2.534413,5.668735,3.625672,8.795988,-3.406153,1.377589,-6.347221,2.805667,-4.524256],[-8.925796,7.482063,-9.496043,6.332690,0.432093,-7.040682,-1.859896,-1.029792,4.762525,-1.651003,-7.329134,0.928926,-7.579872,-6.769630,-3.365261,-5.991825,5.770990,1.564472,1.027526,5.979855,8.568206,2.035668,-2.683433,-7.461165,2.037125,-6.010267,2.234429,-3.296282,-9.132980,9.114455],[7.050661,9.302440,1.349419,-0.779464,-3.175692,5.691933,-6.777260,4.641994,4.146278,-1.943270,-8.508639,-5.207018,2.960329,8.126022,2.608608,-5.761359,6.880553,6.469615,7.889721,8.418306,-4.666917,1.126553,3.642037,8.368902,-1.760940,-6.260625,-6.368062,-1.068770,5.629584,0.839882],[-8.921916,2.405203,-2.697286,8.849269,-8.818754,2.890432,2.534299,4.478091,8.949222,4.878146,9.951677,2.945527,0.767182,7.812433,2.185689,9.741055,-2.904759,5.711818,-0.839073,-2.347436,1.303324,7.153144,9.532427,-6.056258,7.984160,-1.508839,4.604814,-6.148448,-5.713083,7.623294],[0.359453,6.073860,0.256377,-5.114683,9.344263,-9.250040,-6.181852,-6.817148,7.721930,-3.308144,-2.219632,3.686821,-7.161518,-9.951695,4.790935,3.612669,9.242005,-7.432371,8.209472,-9.115777,-3.566052,-1.588445,-0.019657,-2.866890,8.739107,-0.223374,5.123708,8.840074,1.071537,-4.789237],[9.106687,4.899623,1.862727,5.355853,-0.632423,1.253950,-7.066631,8.604702,-4.126820,-1.813568,2.907510,-8.083643,-4.159098,-4.420746,5.671287,-8.458039,-4.228254,6.081744,-7.650191,5.588402,-6.930483,2.934065,-7.914302,8.876336,-1.771979,-5.753170,-3.180062,-0.005870,-4.205122,4.125567],[-9.432218,-0.488594,7.211598,-0.260698,-3.863110,1.821864,-5.952803,7.784737,1.618578,-6.547524,7.073180,9.207029,6.747190,-0.297895,5.500277,2.854372,-4.809227,-2.485120,-2.961090,8.616948,-1.023415,2.268830,2.786864,6.430626,-8.557413,-5.736026,-4.141952,5.136642,6.339114,4.429288],[3.061058,-2.053200,-8.293721,-7.915540,6.678527,3.754693,-4.711928,6.782720,-5.079129,-0.159592,-1.780937,-3.187725,1.665833,-7.365169,4.569039,3.372014,-2.232094,-5.050827,-0.802714,1.199892,-0.822424,-3.196769,-3.168110,-1.040173,-4.385956,7.581881,2.145749,-5.639169,7.478335,-3.562207],[-9.620903,-2.112387,4.251053,-9.023956,2.808153,-3.146085,-8.344066,-9.674336,-4.104207,0.864411,0.131895,5.980952,-2.140442,8.010798,-9.177186,1.359968,5.990431,6.520597,-9.340579,9.290308,-4.243093,-3.108449,-5.875500,1.611986,5.313814,7.610495,2.202080,-3.314666,-5.130939,8.845500],[6.878435,-0.944458,-1.037606,5.599171,7.821881,-6.608262,-4.301045,-1.270952,1.888833,7.667259,6.273994,-8.424984,8.159740,-0.594794,-2.920685,-4.377855,-9.050181,7.533710,3.535959,-9.426245,9.544231,-0.573120,6.429705,-1.372655,-4.445962,5.785009,-2.045052,-7.445470,-2.763297,-4.170336]], dtype = "float64")#candidate|13819|(10, 30)|const|float64
bop_13820 = relay.logical_or(uop_13812.astype('bool'), relay.reshape(const_13819.astype('bool'), relay.shape_of(uop_13812))) # shape=(10, 30)
bop_13823 = relay.logical_or(uop_13814.astype('bool'), relay.reshape(const_13819.astype('bool'), relay.shape_of(uop_13814))) # shape=(10, 30)
uop_13824 = relay.rsqrt(uop_13812.astype('float64')) # shape=(10, 30)
uop_13826 = relay.rsqrt(uop_13814.astype('float64')) # shape=(10, 30)
func_12105_call = mod.get_global_var('func_12105')
func_12110_call = mutated_mod.get_global_var('func_12110')
const_13838 = relay.const([8,-3,8,-10,6,-3,-8,-5,10,10,-3,-4,1,4,-8,9,-10,2,-8,3,8,-9,5,-7,-8,-7,-1,-6,8,8,-2,-4,9,10,-6,-3,9,5,6,8,-10,6,5,-4,1,1,-10,8,8,-9,1,3,2,5,-1,-3,-8,-4,1,6,-1,7,-1,-1,3,5,1,-5,7,2,-2,9,-4,-3,-3,6,7,5,8,-6,5,-4,-1,-1,8,-4,-6,10,-8,-4,-3,4,4,5,7,-1,-3,1,2,10,-5,10,-1,-3,3,-9,8,4,5,1,1,6,-7,-7,1,8,-4,-7,-9,4,-8,6,-8,-5,2,-5,-8,-4,-10,-3,-8,6,1,9,-4,2,7,7,10,8,-7,-4,8,1,9,-8,7,3,7,-8,6,-4,-9,8,-4,3,3,-8,5,8,3,5,10,-8,9,-2,7,5,7,-5,-4,-2,-4,-6,2,-5,10,5,-7,8,10,-8,-6,-2,8,3,6,9,-8,10,-8,4,-6,-7,3,-8,5,-9,1,-3,-9,-3,6,6,4,5,-3,-10,-8,-4,4,4,-8,-2,6,-9,6,9,-1,-5,1,9,-8,2,9,9,-8,5,-9,6,-4,8,5,9,2,-5,5,6,-4,-1,4,6,-6,7,-8,9,-8,-10,-6,-10,-5,1,10,5,-6,9,-10,-2,-6,10,-4,3,-7,4,4,-4,-3,-10,10,7,6,8,10,10,10,9,-10,5,-5,-5,-7,9,1,10,-7,-9,-4,-8,-6,-10,10,-2,2,-2,-8,-8,-3,4,-8,-7,-3,9,5,2,6,2,1,-6,1,10,2,-6,-4,-1,5,7,-6,7,-2,7,-3,3,2,7,-9,7,-2,8,-3,10,7,-8,-4,8,-8,-5,5,4,-9,-5,7,-10,2,7,-7,5,-4,10,-10,5,5,-10,10,-10,-5,7,-6,3,7,5,-6,-1,-3,-10,9,-2,5,-5,-6,-4,-1,-4,-2,-6,8,-6,-10,-7,-5,-6,10,9,8,2,2,-6,9,-1,-7,-1,-6,1,1,9,-3,-2,-2,10,-6,5,-8,-10,-3,9,8,6,8,-2,-3,7,-7,-1,-2,1,3,6,9,10,9,-3,-1,2,4,8,-4,-3,6,10,-5,5,-8,-9,1,10,-9,6,10,7,10,1,-2,5,-10,-5,-5,-3,3,2,1,3,-3,-10,-7,-8,4,-2,-6,4,1,3,10,-9,-7,-5,10,-10,7,7,7,-2,7,-7,3,10,-1,-8,-8,3,5,-6,8,-10,-4,-10,4,-1,-7,5,10,-4,8,-1,8,-2,4,9,-1,-8,8,5,-9,3,7,-8,1,7,3,-6,5,-5,5,2,3,-1,7,2,-4,-4,1,7,1,3,-5,-6,-6,-9,4,-7,9,-7,5,2,4,-2,7,1,5,-3,-5,-1,9,2,-9,-10,6,-7,-9,-2,-7,2,-6,-4,-6,-3,6,-2,4,-10,-2,3,8,-10,-1,1,-7,-1,-5,5,-2,2,4,4,-7,-1,5,-6,-4,-1,9,10,-7,10,-4,3,5,5,-9,-5,3,5,10,2,-10,-8,7,6,8,7,-2,9,6,-7,5,1,-10,6,10,5,-1,8,10,3,9,-2,-10,10,-5,3,1,-7,-10,2,-1,9,-9,-3,10,-4,5,4,7,3,1,1,10,6,3,2,-4,-7,10,1,-5,1,-1,7,-8,-1,6,2,1,6,5,-9,8,3,7,10,-9,4,-7,-7,1,4,9,3,-4,-6,-6,-2,-1,4,9,2,4,-7,6,4,1,7,5,-1,-9,-10,2,-9,6,-10,5,2,-7,10,2,-5,3,-4,1,9,-4,5,2,-8,-7,-5,2,2,8,-5,8,-7,1,1,-9,-2,-1,9,-10,4,-5,8,10,-7,5,-1,1,4,-1,3,-5,-3,1,2,6,7,-6,-1,8,-7,1,4,7,-3,4,8,-3,8,2,-5,5,-2,-8,9,10,-9,-7,-2,-2,5,-2,-7,-4,9,2,-4,6,10,-8,2,-9,6,3,-10,-2,-2,8,9,4,-7,2,5,-7,3,-6,-3,5,10,-7,4,-5,-4,-8,6,1,-8,7,2,-8,1,-10,-8,-2,-3,-9,8,5,-9,-3,5,-10,-8,6,-3,4,8,-8,9,3,1,-10,5,1,10,-1,-9,-10,10,-4,2,-6,-2,-7,4,-4,1,4,-3,2,-8,-10,5,-3,-6,5,6,8,-6,10,2,-7,-2,-1,-5,-8,-7,1,6,7,10,10,5,-6,3,-3,2,10,-10,-8,-5,9,5,-3,1,-5,-4,-8,4,-2,-2,2,6,9,-4,-2,-3,10,-8,-9,5,-1,-10,7,-5,-3,-3,-10,-8,4,5,-10,6,6,-4,-4,-2,9,-6,-8,-3,-9,-5,-5,9,2,5,2,-1,-5,7,6,-4,1,-1,-2,-7,1,9,2,5,-2,5,4,-4,5,-8,-9,7,-4,-9,1,7,-8,9,-6,4,-9,-2,9,1,7,6,-4,8,-9,4,10,3,-8,8,9,2,4,-10,-9,-6,2,4,5,4,6,-6,-7,-6,3,9,-7,1,-4,-4,-2,9,4,-10,7,3,-9,-2,7,-3,2,-4,2,8,-6,1,5,-4,5,-8,-7,6,1,4,5,-8,-1,6,10,1,8,-8,2,-4,7,9,-4,-3,4,2,-5,8,5,-1,-8,4,2,1,-5,3,6,7,-7,-4,8,-2,-6,-10,4,9,4,10,-7,-4,-5,-6,6,-10,6,6,9,8,8,-8,1,-4,3,3,-4,-4,-1,-9,-6,4,2,5,-9,9,-2,2,6,-8,-2,1,-9,7,7,-9,-5,-4,-4,-10,-3,4,6,9,-2,3,10,-9,10,9,2,-10,-4,5,3,-2,-4,2,-2,2,-9,-7,-10,8,-2,7,6,10,2,-9,-1,-1,-7,5,-5,-3,-3,-3,-7,-2,9,-3,-7,-6,-10,-5,-6,-8,-3,-4,1,1,10,-4,5,7,7,1,-5,-4,10,10,10,-10,-2,-9,4,6,6,-2,-7,-6,-9,10,-4,2,6,1,-1,-6,5,-7,-7,-2,2,7,1,6,2,5,-10,1,9,9,3,5,3,7,-5,-7,1,8,1,3,8,1,-6,-4,-6,-7,2,-7,3,7,2,-7,-1,-4,-9,-6,-6,-6,3,7,5,-10,-5,-4,-10,-8,-6,-5,10,-7,-8,-5,-4,-5,1,6,-8,-4,3,3,8,8,-8,1,4,-4,-5,-7,2,-3,5,-10,4,-6,-4,2,4,-8,-5,-10,-10,-3,5,-3,-3,-9,-6,3,-5,-8,-2,10,2,-8,-8,-8], dtype = "int8")#candidate|13838|(1260,)|const|int8
const_13839 = relay.const([0.954796,6.400816,6.049095,-8.926571,7.775377,8.985566,5.172546,4.026938,-7.375825,-0.064796,8.380891,3.021040,-4.257111,0.505536,-2.982299,3.246461,-6.334039,1.948125,-3.173604,3.288018,-9.263505,-7.586272,-6.525097,4.356168,6.192863,0.140048,-4.342617,-4.740725,-2.262860,-9.943227,-9.813978,6.321534,4.409137,-3.659610,-4.016102,1.784517,-9.952283,-6.494814,4.646734,-8.103171], dtype = "float64")#candidate|13839|(40,)|const|float64
const_13840 = relay.const([-2.053928,-3.263422,5.387255,5.924205,-5.766569,-0.430884,-3.022743,-6.218996,3.535715,7.481329,6.361793,-9.724248,5.874753,2.368919,-8.554720,7.303294,6.831953,-0.455647,-1.409546,-5.902438,-5.119789,-1.106273,2.433805,8.670649,-1.827108,-0.750244,-1.810514,1.628377,8.129616,-5.872772,1.058126,-0.407103,9.841846,-7.501751,3.348965,-2.094045,7.442728,-2.039867,3.547874,7.694146,-4.011566,5.760017,-5.203664,-2.830032,-2.676809,-5.608803,-4.531470,-8.319349,8.450027,-4.674945,9.113909,-9.302868,0.759941,3.657779,-9.233145,6.267230,-6.588917,2.563042,8.838419,7.280906,-1.696509,5.880468,-9.875598,-0.351885,-3.963627,-3.495510,3.762547,1.952481,5.822991,-5.703833,5.456114,-1.393340,-9.963150,6.309255,-7.652271,6.240592,-1.990873,6.503800,-8.509950,-4.497458,-0.471496,-9.128410,8.810717,9.417512,-0.476129,-8.103541,5.027269,-3.892674,-3.286346,8.638334,-2.868570,1.184848,7.425607,0.877010,-1.397516,1.749532,4.397937,-0.825541,2.161386,4.534801,6.352163,5.695991,6.890064,9.600555,8.980169,-9.448440,7.853995,-7.170737,-3.583496,0.145428,8.099312,-5.424397,-2.408558,6.961260,-1.634256,-2.157070,-3.172917,-8.650546,1.279959,4.270812,-4.984909,-0.149109,7.384392,-1.540055,-2.998378,-0.629898,-6.651524,-6.635593,-8.620684,-4.708373,4.054856,-0.387393,5.586559,5.737372,-9.507111,0.043119,-3.477303,9.979486,6.591097,1.730767,5.575669,6.545458,-8.235148,-0.661788,-6.678958,8.338432,4.551105,8.079079,-9.155516,0.696722,-7.116006,5.726776,-6.644469,-0.418066,6.752149,-3.026118,-3.968171,-3.716929,6.701721,9.578841,-6.019718,8.197650,-1.931032,-2.447886,2.154561,-6.463794,-1.522223,-2.912213,-7.529951,-3.413758,5.202118,-5.574978,4.498186,-4.534586,0.698271,-7.958454,1.716657,-0.384643,-7.492492,-1.829393,-6.539520,2.342161,5.626767,-8.206038,8.001760,8.224214,8.480780,-3.050373,-9.707444,3.819902,-6.963934,4.259821,-9.981997,9.161452,-9.124490,-6.520060,-6.826244,-3.774549,-7.736884,1.174740,7.401808,-1.308018,-6.224837,7.498199,6.651829,2.935344,-4.731712,7.578684,-0.748861,-1.948219,6.107726,0.046428,-4.854804,7.599330,-1.938700,-4.758098,8.873195,-6.136850,0.451920,-1.004619], dtype = "float32")#candidate|13840|(220,)|const|float32
const_13841 = relay.const([[2,10],[4,2],[4,-4],[-6,-8],[3,-10],[-10,-3],[8,-8],[-7,-8],[6,10],[-10,1],[10,8],[4,1],[-3,2],[-6,6],[4,-4],[10,1],[2,6],[-4,5],[-10,-10],[-9,6],[1,-5],[-4,-3],[-5,-1],[-3,-1],[-4,6],[-1,5],[-1,8],[5,-2],[-3,-7],[8,-5],[-9,9],[9,-6],[4,4],[-2,-1],[-2,-3],[-4,-5],[-1,-3],[-2,-1],[-5,6],[10,-8],[3,-2],[-10,8],[-3,-1],[5,3],[10,-5],[4,-7],[8,-6],[5,-3],[-7,3],[-9,1],[3,8],[-2,4],[-6,-6],[4,-3],[9,1],[3,-2],[8,-8],[-10,8],[3,-1],[-8,6],[-3,8],[8,-2],[-1,10],[-6,4],[10,2],[3,3],[-7,-8],[9,-2],[-8,2],[2,-2],[-6,6],[-7,-5],[-2,-8],[6,-10],[8,-9],[-4,7],[-1,-10],[2,5],[6,-9],[2,3],[10,1],[-5,-10],[-1,-7],[-10,-8],[5,4],[-2,5],[-8,3],[8,-6],[-5,4],[-7,2],[3,-4],[-6,-4],[2,10],[6,-10],[-10,4],[6,8],[-6,3],[7,3],[7,-5],[-2,3],[6,6],[9,-6],[-10,6],[-2,-1],[-7,4],[-2,-7],[6,1],[10,2],[7,8],[5,-4],[-4,-2],[7,7],[-8,1],[7,8],[-10,1],[-2,6],[10,-7],[9,1],[4,-2],[-7,-6],[-9,6],[2,1],[-4,2],[7,7],[-3,4],[6,5],[-9,10],[5,2],[10,2],[-1,-6],[7,-2],[5,2],[4,1],[-3,1],[-3,-9],[-6,4],[6,-1],[-1,3],[4,-2],[5,-8],[4,-10],[-6,-9],[3,-9],[7,-6],[-1,4],[-4,2],[4,-7],[-10,9],[-4,10],[-3,1],[9,4],[5,-10],[9,-8],[3,-10],[-4,8],[-4,9],[-10,-2],[-10,-9],[-2,4],[5,4],[2,-6],[10,3],[-7,-9],[2,2],[6,4],[-4,-4],[6,-6],[4,2],[1,-2],[-7,4],[-8,6],[-10,-1],[-10,-2],[-8,5],[-6,2],[10,-7],[-5,2],[4,8],[9,-9],[2,-5],[4,9],[6,5],[-4,2],[-2,-4],[6,9],[-2,-1],[8,-1],[-3,-3],[6,9],[7,-1],[-1,-4],[10,10],[-4,9],[3,-8],[-3,3],[5,-10],[-1,10],[5,8],[4,8],[2,3],[6,-5],[-1,2],[-1,-7],[3,9],[8,-2],[3,-8],[-4,3],[4,-5],[6,-9],[-2,-1],[6,-1],[-5,2],[2,-6],[-6,3],[1,-5],[2,3],[-7,-4],[-3,-3],[-3,7],[5,-1],[7,-3],[2,-10],[-4,7],[-6,-3],[-3,3],[-4,-7],[1,4],[7,-4],[-3,-5],[6,7],[4,-5],[4,-5],[-5,-5],[5,5],[-7,-1],[-6,-7],[5,-3],[1,1],[4,6],[-2,-7],[9,7],[5,9],[2,-4],[-6,-7],[-7,2],[-2,3],[-8,6],[-2,-8],[-6,-5],[8,-2],[-6,1],[1,3],[-10,-8],[-9,-2],[2,7],[-2,6],[-2,2],[-7,-4],[-3,2],[-3,-4],[3,9],[2,9],[1,1],[2,5],[8,-6],[2,-7],[3,10],[8,2],[7,3],[5,5],[-9,9],[-4,5],[-2,7],[9,10],[5,1],[-6,-3],[6,-2],[8,-5],[6,8],[10,1],[4,-7],[-2,-8],[-9,-10],[-2,9],[9,-9],[1,-5],[7,6],[-9,-1],[-5,-8],[5,5],[5,-10],[8,-4],[-1,7],[-6,8],[8,-3],[10,-1],[-4,1],[-5,5],[2,6],[5,9],[5,-7],[-8,6],[-8,4],[7,-3],[6,-2],[10,10],[3,2],[-10,-1],[6,-7],[2,4],[-4,-9],[6,2],[6,3],[-1,10],[1,-1],[4,5],[1,-8],[-5,6],[3,-2],[7,-2],[-10,-3],[-10,-7],[6,3],[2,-1],[1,-10],[4,-6],[1,-7],[-4,3],[6,4],[-8,8],[-9,-3],[-10,-5],[-6,5],[-3,6],[-1,-4],[9,-8],[3,10],[3,5],[-8,4],[-3,-9],[8,-8],[7,4],[-4,-6],[6,-10],[7,2],[10,3],[-6,-8],[-10,1],[-10,-8],[2,8],[10,10],[7,-5],[-4,4],[4,3],[-8,2],[-9,5],[-9,-8],[-5,-8],[-8,1],[10,10],[2,-7],[-3,8],[-3,-9],[-3,-2],[9,5],[6,-1],[2,10],[5,-8],[-3,-5],[7,-8],[-6,-5],[-3,-5],[-6,-8],[-6,9],[-10,-1],[-10,-4],[-6,-9],[-4,5],[8,-3],[4,-5],[8,7],[4,-1],[-6,9],[-1,-6],[4,10],[-6,10],[-3,-5],[10,-1],[5,2],[3,-4],[-6,-2],[-8,6],[8,9],[-2,-8],[-1,4],[-2,10],[5,9],[-5,-7],[-7,-10],[1,-6],[3,-3],[-6,10],[3,-9],[-2,-4],[-2,5],[7,-8],[2,1],[7,4],[-5,-5],[-7,8],[-2,7],[-9,1],[6,-7],[-9,-1],[-7,8],[-10,-4],[-9,-5],[7,-6],[-2,4],[-4,1],[2,-6],[6,-6],[10,7],[-4,4],[-1,10],[10,-8],[9,-4],[-7,-6],[2,2],[9,-1],[1,6],[8,-1],[-7,-6],[8,-1],[-5,3],[-9,-1],[-1,9],[10,-9],[-7,-8],[-7,5],[-1,2],[6,-8],[8,1],[10,-8],[-6,1],[8,-8],[-6,-3],[5,-6],[-8,6],[4,5],[5,9],[9,-6],[-8,-2],[8,-5],[-6,5],[6,-10],[2,8],[-9,-7],[-10,-10],[8,3],[-3,-4],[5,-3],[-8,4],[2,8],[-1,-9],[9,5],[-4,8],[8,-8],[8,-2],[-1,-6],[3,-1],[-6,-10],[-5,-9],[5,-6],[8,-1],[-7,9],[-10,10],[6,-8],[-8,8],[10,-2],[5,1],[-5,8],[-1,4],[-7,3],[6,9],[-9,-4],[8,4],[-10,-2],[8,-6],[8,-8],[5,7],[9,-1],[3,-8],[1,-3],[4,8],[4,8],[3,4],[-9,2],[-8,-8],[-1,1],[-1,10],[3,-2],[1,-10],[9,-4],[3,4],[2,-6],[9,7],[-4,-5],[9,8],[9,6],[7,-4],[5,9],[-7,10],[10,-2],[-1,-8],[7,-2],[9,8],[-8,-9],[-2,3],[10,-5],[-4,-8],[2,-5],[1,2],[9,6],[-3,-7],[9,-8],[-10,8],[1,-8],[-10,-1],[-8,-7],[-2,-9],[-2,10],[-9,6],[4,7],[-3,3],[-8,-10],[7,1],[10,4],[-9,-4],[8,-6],[-2,3],[6,-9],[8,-2],[-10,5],[6,5],[-7,9],[-4,9],[-8,8],[-7,5],[4,-2],[-3,-9],[9,-2],[-1,8],[-8,6],[-1,-3],[-9,-6],[-4,10],[4,-8],[-8,-9],[10,-9],[-10,1],[-5,1],[1,4],[5,-4],[2,4],[-8,10],[1,3],[5,-4],[-1,5],[3,4],[10,-2],[8,3],[-2,6],[1,-7],[9,4],[2,-1],[5,10],[1,-10],[10,7],[9,-9],[-9,2],[5,2],[9,-8],[-4,-5],[4,-6],[9,-10],[-7,-10],[7,9],[8,-5],[1,5],[-3,-5],[1,-5],[7,-9],[-9,-7],[6,-5],[9,-10],[-5,10],[-4,8],[-7,4],[4,2],[-3,8],[-10,8],[-4,-10],[7,2],[8,-10],[6,-10],[2,10],[5,7],[-2,2],[2,9],[-5,3],[-2,-3],[-6,1],[-4,4],[6,2],[-3,-1],[-8,9],[3,7],[1,-9],[4,3],[9,-1],[-6,-9],[-6,-4],[-1,-6],[-8,-8],[6,-10],[-7,8],[-2,-3],[-5,-4],[-9,3],[-1,8],[4,3],[-10,-4],[8,3],[-4,7],[2,-9],[-6,9],[-3,3],[-1,-7],[5,-6],[1,-1],[-5,-4],[-5,-7],[3,-7],[-6,-4],[-1,4],[-8,-5],[-3,7],[-1,2],[-3,5],[9,7],[7,-5],[-10,-3],[-6,3],[9,6],[-8,-5],[1,3],[6,-2],[-9,1],[2,-8]], dtype = "uint64")#candidate|13841|(660, 2)|const|uint64
call_13837 = relay.TupleGetItem(func_12105_call(relay.reshape(const_13838.astype('int8'), [1260,]), relay.reshape(const_13839.astype('float64'), [40,]), relay.reshape(const_13840.astype('float32'), [220,]), relay.reshape(const_13841.astype('uint64'), [1320,]), ), 7)
call_13842 = relay.TupleGetItem(func_12110_call(relay.reshape(const_13838.astype('int8'), [1260,]), relay.reshape(const_13839.astype('float64'), [40,]), relay.reshape(const_13840.astype('float32'), [220,]), relay.reshape(const_13841.astype('uint64'), [1320,]), ), 7)
func_12866_call = mod.get_global_var('func_12866')
func_12867_call = mutated_mod.get_global_var('func_12867')
call_13853 = relay.TupleGetItem(func_12866_call(), 1)
call_13854 = relay.TupleGetItem(func_12867_call(), 1)
uop_13859 = relay.exp(uop_13824.astype('float64')) # shape=(10, 30)
uop_13861 = relay.exp(uop_13826.astype('float64')) # shape=(10, 30)
func_7546_call = mod.get_global_var('func_7546')
func_7551_call = mutated_mod.get_global_var('func_7551')
const_13866 = relay.const([[2.231658,0.959604,-3.217213,-2.548301,0.401524,-8.129990,-1.811084,-2.407468,9.116323],[-3.302196,9.764088,4.708822,3.934620,-9.098908,7.505301,4.017295,8.057645,-2.037908],[2.471356,-4.254762,6.483274,-4.212594,-8.507217,6.058823,9.811438,2.355604,-9.304456],[-7.511817,-8.979088,3.466908,-3.584309,-4.911493,1.224323,8.488125,4.948728,7.829577],[-4.430229,8.342216,5.861564,0.932338,-8.941471,3.110236,5.522968,0.668103,-7.038120],[3.091304,5.615941,-6.718237,-7.745465,6.711656,8.076524,-1.529439,-9.197512,-2.868852],[-7.626555,-9.189047,7.011025,-6.476105,-8.196501,-3.250025,-6.572750,3.282720,9.443981],[7.509205,4.939126,-8.222157,7.253099,-5.181962,-1.658903,1.681657,-8.599068,0.199850],[9.668252,-0.017949,6.879865,9.259334,-0.087015,6.729943,-5.721962,9.039040,9.288270],[8.427342,-8.315289,9.352450,-0.815353,-2.929799,-7.182499,-1.908146,2.991474,7.338337],[4.869963,-9.432518,0.518548,-6.677518,-3.436131,6.158555,3.192037,8.332559,1.271673],[-5.529257,7.111582,-4.091138,-5.144380,-0.981913,-9.105911,2.025245,-1.648027,7.580136],[6.854968,5.781950,-3.067755,-2.893347,9.802166,6.883930,-2.361506,5.001814,-2.248621],[2.167972,-1.942936,-0.151239,-2.706594,5.124050,-9.878832,-6.173746,-9.082701,9.750331],[1.871668,-3.776415,1.999901,5.510693,3.742534,-2.666105,-3.067442,-5.601807,7.903552],[9.343628,-7.747888,-0.508513,-0.090667,5.751562,-8.535138,6.502099,-1.728478,8.308689],[2.594893,9.212499,7.277222,3.064262,8.614704,-7.636122,-6.118530,-5.969535,-5.529192],[2.634571,-6.537160,6.669283,-9.356986,-5.515182,-0.739735,-7.506069,-8.224286,-4.258214],[2.804523,7.486022,-4.032530,9.503575,-9.142487,2.622558,-0.473257,9.480741,1.724398],[-2.690751,9.569701,-3.724974,-2.276459,7.873812,-9.521185,-2.464048,2.670601,3.957866],[8.708988,0.442198,-2.762475,1.302148,4.467291,4.951795,5.083656,-6.135039,-6.910638],[3.367152,-7.082597,7.350967,-5.181917,-4.331165,-9.494293,3.671528,6.394472,7.484907],[-4.810415,-6.755606,4.949510,-0.820677,7.267812,0.868122,-0.453656,-0.962359,6.298805],[8.070235,7.469535,-2.258235,7.143480,-5.092853,-0.819169,1.413005,-6.453255,-8.783141],[7.744995,-7.886016,-4.810723,6.481069,-8.138413,9.805693,9.858981,-1.491563,-4.604603],[-0.414398,-2.074241,-4.069094,-2.699262,1.559410,-8.186884,-0.200431,2.769115,-1.785501],[-7.177872,-1.838672,-8.613086,5.496052,-9.209263,-6.817238,-9.829477,1.441513,3.576513],[8.821135,7.234335,-8.398878,-2.001508,1.323437,-2.505249,9.241732,2.872205,6.803930],[8.252899,-7.144148,-6.027633,7.782968,0.712796,-0.542574,-6.361700,6.983314,-7.011741],[7.082550,-9.665103,-7.242591,1.163130,-1.597705,5.821826,-5.421116,-7.199883,8.703244],[5.112327,2.641165,9.180630,-0.477764,9.609556,8.641506,7.329829,-1.960520,4.719898],[-2.013602,8.068146,-7.835932,9.989441,9.178344,3.095916,-4.070595,3.171900,3.910833],[8.420170,5.426526,6.638941,5.858051,5.252571,1.516939,-9.428287,2.815298,-8.187321],[2.950967,-9.045752,6.668039,4.092177,6.224802,0.658615,6.412519,-7.632676,7.407514],[0.055525,-5.480847,-3.316078,7.625292,-5.783798,-7.151935,-1.977581,-5.017613,5.080872],[-8.101744,3.886153,7.312494,5.997883,-4.958370,3.197682,1.901263,-0.502951,-8.938000],[5.052641,5.380491,-1.536554,-7.479703,6.226365,-9.122424,-8.843662,5.699517,-8.761433],[-3.363200,4.680773,5.691002,-6.585567,0.970790,-2.335180,-4.120431,-5.036237,1.043935],[4.107207,3.348665,-6.962935,9.972647,5.539546,5.940338,-0.898710,5.571199,-2.243732],[-4.579580,0.380698,3.110082,5.501799,-4.932915,8.114811,5.119152,8.701723,-6.815475],[-8.747975,0.583694,-6.532693,7.483894,-7.485260,1.985401,0.181707,-0.411076,8.516020],[-2.422522,1.811056,-0.125483,5.914308,2.018269,8.054819,-6.696666,-6.164739,2.863970],[-5.068991,2.281036,0.195651,7.755941,-5.982097,4.524882,1.712563,0.829928,-8.018421],[-5.827698,9.147156,0.377144,2.213753,-0.166553,8.912069,-3.809131,-8.372915,-4.566920],[-3.133915,-6.566777,9.973402,0.655042,5.532800,0.923909,-6.942943,0.600329,-5.103157],[-9.893977,3.820489,8.967257,-2.222679,-0.431540,4.923726,-1.976950,4.958516,-4.296146],[6.402319,4.045973,-4.533247,-4.048944,-5.644424,-5.264463,-0.764382,-0.346607,9.217874],[-5.723634,-9.289000,-5.578393,-9.332122,1.530379,0.165029,-0.562984,5.417308,-8.387366],[5.593325,3.441577,-9.740634,-2.899279,-0.981096,-2.296090,-2.620397,-0.660983,-3.457641],[-5.231263,1.762179,-4.452960,9.264598,3.824409,-1.840416,7.752579,6.542722,-5.929369],[-5.554328,-2.597218,9.819821,3.295055,-1.697106,-4.603897,-8.292030,5.851242,5.496290],[4.725376,-7.996492,2.305179,-2.561613,-3.594306,2.574258,2.624137,3.939952,8.798040],[0.740821,-1.938583,-8.994394,-4.167911,3.318210,-1.917158,2.904938,-9.277795,4.765006],[-6.976854,-1.495613,0.738860,2.734277,4.307420,-4.197926,-6.700041,8.847046,3.110857],[8.952084,5.684500,8.366516,3.493842,9.954110,2.518959,-4.233324,-1.108994,-1.841477],[-5.646152,-3.257231,4.720370,-3.837007,-0.515274,-3.497280,3.617715,2.759900,5.386441],[7.651863,0.346425,-5.894563,4.673282,6.031753,5.826750,3.126557,0.002978,4.182622],[-3.906124,-6.432807,-2.588952,7.707268,9.203608,-0.053299,4.921699,0.917251,-6.708689],[4.969994,-8.140193,5.979266,2.999138,-9.112974,-9.269703,5.635924,0.024606,-8.152261],[-4.968942,-1.621472,-7.504222,-8.431129,-6.228520,1.327117,1.431111,-0.507339,1.360734],[8.080014,-3.404896,6.357388,-7.245139,3.431963,6.831975,9.923436,9.514003,6.204112],[-1.731686,-9.333584,5.892229,2.619972,-5.220583,5.734425,0.282081,-4.834574,-7.353721],[-0.021205,-7.702990,-9.634711,3.486357,-0.544543,8.152805,7.811684,9.854310,-9.934358],[9.564974,-4.386116,5.682284,9.117431,-2.428324,-0.129794,2.230295,9.884174,2.890148],[0.213040,3.696143,0.151798,7.789939,-2.532042,-3.744396,-0.194488,-1.491250,-0.718837]], dtype = "float32")#candidate|13866|(65, 9)|const|float32
const_13867 = relay.const([2,-2,6,-10,-4,1,8,6,-9,-7,-9,-9,1,-3,-8,2,10,5,-7,2,4,9,-1,9,-4,-8,7,3,-7,-8,5,-5,1,-2,4,2,-9,10,-7,-10,5,5,-9,9,-7,3,6,8,9,-8,5,-1,-2,-6,9,-2,-6,-6,5,3,4,-5,-3,8,2,4,-7,-2,3,-7,-4,7,-6,-6,-10,-5,2,-5,-1,-6,-10,-10,5,-5,10,3,3,-7,-4,-9,2,9,2,-1,-8,7,9,-4,-1,-5,2,-8,-7,-1,-8,5,4,3,7,-2,3,2,1,8,-4,-7,-10,-1,-10,6,-5,-5,5,9,-2,-9,-2,-6,-7,-7,7,9,-8,2,5,3,9,2,-6,7,4,2,7,1,2,8,1,-9,-10,-5,9,8,6,3,3,-9,-6,-4,-8,-10,4,-2,-5,-6,-1,1,-8,1,9,5,4,8,4,-6,9,-3,-1,-10,7,3,-6,10,-3,10,-5,-5,-1,-10,5,7,1,8,6,-8,3,-3,-6,-3,-3,3,7,8,9,3,5,1,-10,8,7,1,9,-9,6,-4,-2,-9,-2,-1,9,8,-3,-10,8,-1,5,-6,-5,-9,-4,9,7,9,7,2,-3,9,-1,-1,8,7,5,10,-8,-8,-2,-10,-7,10,-8,-9,7,9,7,-9,3,10,9,5,-9,-10,1,9,3,-1,6,-2,-8,-8,-2,-1,3,10,-1,7,-9,2,1,10,-3,-4,1,-9,-8,5,6,-2,7,-10,8,-10,-6,-1,-6,-10,-3,7,10,-4,-6,8,-5,10,-4,-2,-8,1,7,-3,-4,9,5,1,3,-6,6,-1,-2,-3,-3,-1,9,5,6,6,-10,7,-2,-3,-8,4,-10,-5,7,-1,4,1,5,-7,5,1,8,-1,8,5,-2,8,-5,-6,-2,5,10,7,-2,-4,-8,2,-3,-8,10,5,-6,4,5,-6,-9,-2,6,2,-4,7,-1,1,6,5,5,-8,4,-4,1,5,-2,-9,-6,8,-9,-3,-6,6,-4,-7,-2,1,4,6,-7,7,10,8,9,6,-1,-10,-5,-8,-9,1,-10,9,10,-1,-6,8,6,-2,2,-5,-10,1,-3,-6,5,-8,-2,9,2,-8,-10,-6,4,3,7,10,-5,3,-1,-10,8,9,5,-1,8,7,8,4,1,-8,7,6,-9,8,7,6,8,-3,-3,-1,-4,9,-4,-3,-10,3,-7,9,-5,-7,9,-8,-7,1,7,-1,4,4,2,-3,6,-10,-3,10,8,-4,9,3,5,5,9,5,-5,9,6,-8,8,-5,8,2,-1,2,-8,-7,2,7,8,-5,2,-8,8,1,7,8,1,3,6,-3,2,-9,2,6,-9,2,-4,10,-8,7,-6,1,5,-9,-1,5,-2,10,10,3,6,1,-6,4,-1,-9,6,-4,6,-1,-10,2,1,-6,-9,-10,-6,7,-3,6,-9,-3,-7,-5,-4,3,5,6,9,-8,-2,-3,1,-10,10,10,-1,6,2,2,-2,-8,2,2,5,-10,-8,7,5,-6,1,8,-1,-1,-8,8,10,6,9,3,-9,5,6,-9,-7,-7,10,-2,10,5,8,9,-7,-10,-6,-4,-6,2,-9,4,-5,6,-8,8,6,7,5,4,2,2,-8,1,-3,7,-4,-10,4,6,-6,10,-8,-8,3,-6,-7,-3,5,1,8,10,3,-3,-7,8,3,-7,-7,3,8,-6,-10,-2,-6,-2,4,-8,-5,-1,10,-6,-9,2,-10,7,8,3,-4,-2,-9,-5,-10,10,-4,6,2,6,6,9,-5,-4,-10,1,-5,2,-9,8,10,5,-9,-7,-4,4,1,8,10,10,-2,-1,4,-2,10,4,-8,-3,1,-9,3,7,-7,-1,-10,6,-10,10,2,-8,-3,-2,1,-7,-7,9,10,-3,4,3,-5,-7,-7,10,10,2,10,4,1,-6,-8,6,3,-4,-5,1,7,4,5,-5,-2,8,-3,7,-6,10,-8,-1,-8,-7,3,3,-4,-5,-1,-5,9,8,10,4,8,9,10,6,4,-9,9,-8,-8,-5,-5,-3,6,6,7,-1,4,1,-7,-10,-10,9,-2,4,9,-1,2,7,-7,3,3,-9,3,8,6,-10,-10,6,5,4,-1,-6,-10,10,-8,-1,8,-7,-9,10,7,-10,8,-9,-7,-7,-9,-3,8,6,8,-8,-7,-7,3,10,7,7,9,10,-10,-6,10,7,3,-7,-3,7,-1,8,10,-4,-9,2,-8,4,9,-6,-9,8,-10,-3,9,5,-4,6,1,3,-10,8,7,-5,-1,-7,7,4,-10,10,-9,-3,-8,-9,8,8,8,7,9,-2,-4,3,-4,-7,-4,-8,-4,5,2,10,7,10,-6,-1,-7,-5,3,2,-3,-6,8,9,6,5,-2,-8,4,4,-2,-5,9,-10,8,-2,3,-1,1,-4,-5,-3,-5,-8,6,1,9,9,-7,-10,2,-9,7,7,-9,-5,1,3,-10,7,3,5,3,9,2,-7,9,-1,-6,-6,-9,-1,-10,6,-5,5,-10,-1,-2,-5,8,-1,7,-7,10,10,-4,-10,7,-4,1,-2,10,4,-4,8,-8,-2,3,-2,3,-10,4,5,8,-4,9,-7,-1,-10,-9,-8,-9,4,10,-5,-7,-3,-5,-2,6,-1,4,-3,-1,10,3,-7,-8,6,-6,-4,6,-5,4,7,3,-6,-7,2,5,-8,-1,3,-5,-9,2,7,1,-2,-7,-8,6,-7,-4,-3,-10,7,5,1,3,-2,-5,6,8,10,6,8,-1,-8,-2,4,-1,3,3,5,-6,-2,5,7,-5,-3,-5,4,5,-3,-3,1,9,10,-10,9,-4,-8,-10,-4,-4,-5,-7,-6,-1,9,7,-7,-4,2,2,1,-4,-4,-6,9,-7,-8,3,7,3,9,-6,8,-3,-5,4,10,-6,2,5,3,-6,-6,-5,5,9,-9,10,6,-8,10,-8,1,5,8,-7,-3,2,-1,2,-2,-2,7,-8,5,5,-1,-6,-7,-8,-2,-7,-7,4,-3,-6,1,-8,9,-3,-6,-10,1,9,-8,4,1,4,-8,6,7,10,1,6,6,4,8,-8,9,-7,-4,6,-2,-3,-1,6,4,-5,4,3,-5,-1,-1,1,6,-9,-1,-8,-5,5,-10,5,-7,-9,6,-8,-8,-3,9,1,4,-8,4,7,-4,7,-5,10,-5,-10,10,1,10,9,7,-5,-1,-5,-6,6,9,8,8,-6,6,5,6,5,7,5,5,5,10,1,-6,-8,2,9,-3,-2,-10,6,-2,-2,-7,5,7,-10,-3,5,-9,4,-8,-9,7,1,-10,-3,-7,5,4,-10,1,-9,10,-4,6,10,1,4,-5,-5,-1,-9,-5,-6,4,1,-5,-10,4,-6,3,4,-7,2,-3,-7,7,-7,-10,-3,-9,2,7,-9,-9,9,10,6,2,-9,4,3,2,4,-3,10,5,5,5,3,8,-6,5,-8,-9,-6,-1,-6,9,8,-1,3,10,6,-2,1,-10,10,8,-4,3,2,9,8,10,-9,4,-4,1,-2,-10,-3,-10,8,9,5,-2,-7,-4,8,-2,-4,-2,-1,-10,-6,-5,-3,-1,3,10,5,2,4,8,-2,10,7,6,-7,-2,-9,3,2,-10,6,-10,6,3,-1,-2,9,1,-6,-3,-5,7,2,7,-3,-8,1,-10,-1,4,1,-7,10,8,4,10,-8,7,-6,-3,-1,6,10,-8,-8,-5,8,1,9,-5,-3,-4,1,-3,6,-6,9,-1,-7,-2,-1,5,-8,-7,-10,-1,9,-5,7,-7,-4,-9,4,-3,-9,9,-1,-9,-3,-7,-1,5,2,-10,8,1,2,-6,-2,-9,-4,-10,3,4,-6,-8,-9,-6,-2,1,6,3,-4,4,8,6,4,-6,5,-2,1,9,2,1,4,8,-4,7,10,3,-7,-9,-4,7,-5,10,8,5,5,-7,-10,8,-6,1,6,-3,2,5,8,-3,10,8,3,1,-3,-6,3,-4,-8,-4,-8,9,-10,-4,-6,-1,4,-6,5,6,6,-1,-7,6,10,10,-9,-8,1,7,-2,-4,10,-3,7,-2,-3,-2,8,6,7,5,-2,5,6,-3,-10,3,8,4,-7,-10,1,-3,-9,-8,2,4,-8,-1,1,-3,10,-3,-3,-6,5,-1,6,-9,2,3,3,-1,-6,-7,6,-10,-5,-5,-1,-9,6,5,3,-9,1,10,-9,9,3,2,6,-4,-6,1,1,-4,-9,1,2,8,1,-1,1,8,6,1,-6,6,5,9,-7,-5,1,10,-7,1,8,-10,2,3,10,1,-9,7,-6,2,-9,-10,4,-8,-2,-10,-10,1,10,1,6,-5,-1,-10,9,10,10,8,2,6,-4,-6,9,-8,9,-9,3,9,8,-1,-3,5,-3,-9,1,-10,-4,-1,2,-3,9,8,-8,8,-6,3,1,3,2,-10,-9,-10,-5,-7,-2,-9,-2,5,-4,8,-3,1,10,10,8,-9,-10,-10,-1,5,-7,4,-1,-1,-1,7,1,-10,2,5,3,6,2,-10,3,6,-10,-1,-7,-8,-1,-4,2,3,7,-3,1,-4,5,8,1,-2,-4,6,5,-2,6,7,2,-2,-8,-9,-4,6,1,9,-9,7,-4,-5,-4,5,2,7,-2,5,4,2,9,9,-3,-3,1,-6,-10,4,-7,-5,-1,-5,3,-6,3,7,8,-5,-8,5,-8,-6,1,4,9,7,4,-6,9,4,-1,-8,-10,-2,-9,8,8,-8,6,-5,5,-6,3,6,5,5,-2,5,-4,-10,1,-4,4,6,-6,-6,4,-10,5,8,-5,-3,6,10,-2,4,-2,2,2,7,-2,9,-4,-4,4,-8,7,-7,-9,4,9,7,-8,-7,-9,-8,-7,7,-5,-10,-5,7,10,-4,1,10,-5,1,-6,-4,3,5,9,3,7,5], dtype = "int64")#candidate|13867|(1872,)|const|int64
call_13865 = relay.TupleGetItem(func_7546_call(relay.reshape(const_13866.astype('float32'), [13, 3, 15]), relay.reshape(call_13837.astype('float32'), []), relay.reshape(const_13840.astype('float32'), [55, 4]), relay.reshape(const_13867.astype('int64'), [12, 156]), ), 2)
call_13868 = relay.TupleGetItem(func_7551_call(relay.reshape(const_13866.astype('float32'), [13, 3, 15]), relay.reshape(call_13837.astype('float32'), []), relay.reshape(const_13840.astype('float32'), [55, 4]), relay.reshape(const_13867.astype('int64'), [12, 156]), ), 2)
output = relay.Tuple([call_13762,call_13795,var_13796,bop_13820,call_13837,const_13838,const_13839,const_13840,const_13841,call_13853,uop_13859,call_13865,const_13866,const_13867,])
output2 = relay.Tuple([call_13763,call_13797,var_13796,bop_13823,call_13842,const_13838,const_13839,const_13840,const_13841,call_13854,uop_13861,call_13868,const_13866,const_13867,])
func_13876 = relay.Function([var_13796,], output)
mod['func_13876'] = func_13876
mod = relay.transform.InferType()(mod)
mutated_mod['func_13876'] = func_13876
mutated_mod = relay.transform.InferType()(mutated_mod)
var_13877 = relay.var("var_13877", dtype = "float32", shape = (540,))#candidate|13877|(540,)|var|float32
func_13876_call = mutated_mod.get_global_var('func_13876')
call_13878 = func_13876_call(var_13877)
output = call_13878
func_13879 = relay.Function([var_13877], output)
mutated_mod['func_13879'] = func_13879
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12563_call = mod.get_global_var('func_12563')
func_12565_call = mutated_mod.get_global_var('func_12565')
call_13904 = relay.TupleGetItem(func_12563_call(), 0)
call_13905 = relay.TupleGetItem(func_12565_call(), 0)
func_11837_call = mod.get_global_var('func_11837')
func_11838_call = mutated_mod.get_global_var('func_11838')
call_13930 = relay.TupleGetItem(func_11837_call(), 0)
call_13931 = relay.TupleGetItem(func_11838_call(), 0)
uop_13938 = relay.sin(call_13904.astype('float32')) # shape=(2, 6, 11)
uop_13940 = relay.sin(call_13905.astype('float32')) # shape=(2, 6, 11)
output = relay.Tuple([call_13930,uop_13938,])
output2 = relay.Tuple([call_13931,uop_13940,])
func_13950 = relay.Function([], output)
mod['func_13950'] = func_13950
mod = relay.transform.InferType()(mod)
mutated_mod['func_13950'] = func_13950
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13950_call = mutated_mod.get_global_var('func_13950')
call_13951 = func_13950_call()
output = call_13951
func_13952 = relay.Function([], output)
mutated_mod['func_13952'] = func_13952
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13582_call = mod.get_global_var('func_13582')
func_13583_call = mutated_mod.get_global_var('func_13583')
call_13963 = relay.TupleGetItem(func_13582_call(), 0)
call_13964 = relay.TupleGetItem(func_13583_call(), 0)
output = relay.Tuple([call_13963,])
output2 = relay.Tuple([call_13964,])
func_13965 = relay.Function([], output)
mod['func_13965'] = func_13965
mod = relay.transform.InferType()(mod)
output = func_13965()
func_13966 = relay.Function([], output)
mutated_mod['func_13966'] = func_13966
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12121_call = mod.get_global_var('func_12121')
func_12123_call = mutated_mod.get_global_var('func_12123')
call_14003 = relay.TupleGetItem(func_12121_call(), 0)
call_14004 = relay.TupleGetItem(func_12123_call(), 0)
func_5115_call = mod.get_global_var('func_5115')
func_5117_call = mutated_mod.get_global_var('func_5117')
var_14010 = relay.var("var_14010", dtype = "uint32", shape = ())#candidate|14010|()|var|uint32
call_14009 = relay.TupleGetItem(func_5115_call(relay.reshape(var_14010.astype('uint32'), [])), 0)
call_14011 = relay.TupleGetItem(func_5117_call(relay.reshape(var_14010.astype('uint32'), [])), 0)
bop_14012 = relay.multiply(call_14009.astype('uint16'), var_14010.astype('uint16')) # shape=(3, 1, 16)
bop_14015 = relay.multiply(call_14011.astype('uint16'), var_14010.astype('uint16')) # shape=(3, 1, 16)
output = relay.Tuple([call_14003,bop_14012,])
output2 = relay.Tuple([call_14004,bop_14015,])
func_14016 = relay.Function([var_14010,], output)
mod['func_14016'] = func_14016
mod = relay.transform.InferType()(mod)
var_14017 = relay.var("var_14017", dtype = "uint32", shape = ())#candidate|14017|()|var|uint32
output = func_14016(var_14017)
func_14018 = relay.Function([var_14017], output)
mutated_mod['func_14018'] = func_14018
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12448_call = mod.get_global_var('func_12448')
func_12450_call = mutated_mod.get_global_var('func_12450')
call_14114 = relay.TupleGetItem(func_12448_call(), 0)
call_14115 = relay.TupleGetItem(func_12450_call(), 0)
output = call_14114
output2 = call_14115
func_14124 = relay.Function([], output)
mod['func_14124'] = func_14124
mod = relay.transform.InferType()(mod)
output = func_14124()
func_14125 = relay.Function([], output)
mutated_mod['func_14125'] = func_14125
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12563_call = mod.get_global_var('func_12563')
func_12565_call = mutated_mod.get_global_var('func_12565')
call_14131 = relay.TupleGetItem(func_12563_call(), 0)
call_14132 = relay.TupleGetItem(func_12565_call(), 0)
output = call_14131
output2 = call_14132
func_14169 = relay.Function([], output)
mod['func_14169'] = func_14169
mod = relay.transform.InferType()(mod)
output = func_14169()
func_14170 = relay.Function([], output)
mutated_mod['func_14170'] = func_14170
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14169_call = mod.get_global_var('func_14169')
func_14170_call = mutated_mod.get_global_var('func_14170')
call_14185 = func_14169_call()
call_14186 = func_14169_call()
func_2005_call = mod.get_global_var('func_2005')
func_2008_call = mutated_mod.get_global_var('func_2008')
const_14190 = relay.const([1.579400,-0.622950,8.721413,4.671358,8.261013,-4.595050,-6.825130,-4.384316,-1.818530,-7.951368,-1.557606,-2.421241,7.724118,-1.267519,2.990658,0.163564,7.993271,-4.404879,-7.383865,3.234806,-1.623214,5.830108,-1.080700,-6.614786,-0.066813,-9.395575,0.101817,6.242837,-1.526669,3.303614,0.544801,-2.183865,-3.584465,3.195358,6.319382,9.263948,-6.711484,-5.725646,-2.739959,7.385894,-2.735076,5.846523,-1.597320,-1.564219,3.057178,8.574451,-8.290203,0.112963,-8.783009,8.757234,9.890801,5.738144,-2.086572,2.617249,6.409160,9.167718,-5.397625,4.684816,9.499775,3.745489,-6.561852,2.587938,-2.875013,6.770904,6.305254,-2.338600,8.076098,-9.723691,-9.415867,-8.937445,5.964885,4.621822,9.169838,-3.092278,-8.982104,3.561939,-0.393637,-5.381616,2.628171,-5.054495,-8.291040,-7.258869,-8.178036,5.370452,-9.634213,-2.237819,-4.826609,3.224020,2.572373,-4.143865,6.836913,-0.667770,7.300533,-1.030513,-2.471650,7.404015,-2.709055,2.611144,9.810032,9.185344,-0.252229,4.514208,3.418400,-3.840149,-9.996568,-4.939809,-7.704830,-8.804910,6.743478,8.900478,6.256362,5.947196,-6.450359,-1.893749,0.680119,5.258333,-4.753864,-2.923525,1.741768,-3.818778,-5.134681,7.735629,5.600170,-4.395214,-3.291042,-4.388600,-2.620712,5.531395,-9.716988,-1.394800,0.996645,-3.504535,-8.081693,6.811619,1.341661,-1.913358,7.129437,7.380437,5.279103,3.824340,1.206995,1.439353,9.638592,-9.360758,-2.210407,-5.878591,-5.726724,3.456130,7.520015,-0.422352,-0.016423,-1.081128,-3.040318,-7.627725,7.376407,7.516916,-0.513652,6.418824,-2.148181,8.674806,-0.140620,-2.431690,-7.492651,-4.176732,4.678606,4.497656,6.231697,2.615422,5.632008,6.797853,0.832530,6.724690,7.248055,-1.808557,-1.481168,-9.321076,9.658974,9.615412,7.299291,9.353479,-6.802161,-5.387487,1.204118,3.673291,-1.104678,4.407020,1.267414,8.337883,0.327069,-8.213651,9.473513,7.147960,-1.832631,5.264793,-7.725989,-4.625218,8.239971,-8.315320,-0.626757,0.665652,-7.903473,-5.323067,9.919409,-4.362003,9.558545,-4.618528,5.640975,3.388953,-8.057401,7.084893,-2.968480,7.046953,6.378469,-1.567336,8.638353,-2.920208,-7.495225,7.688161,-8.374738,8.052047,3.603019,-6.954864,3.388176,-0.536071,-2.282946,-2.908640,4.046085,-7.267424,7.213689,-5.968762,-2.974976,-2.345207,3.789654,-4.119126,8.435802,-7.369987,6.864772,1.842501,-2.864818,-1.166801,-4.287680,8.242291,-1.454604,-3.801064,-0.789201,-5.833222,1.565657,-5.328856,1.565891,-9.514527,-8.214685,9.923094,1.312401,-0.541847,-9.181981,9.067454,1.541864,-1.625294,-0.027421,6.167063,5.205973,-2.825344,-6.940422,1.945017,6.665165,-5.936156,-5.241940,-8.019974,-1.283859,-6.843984,6.737095,4.059988,-7.829105,5.437573,-2.887691,-4.942991,-0.094438,-9.806032,8.732616,-0.392289,4.634838,-0.913541,-5.192103,-5.918266,4.692859,9.610570,-3.185935,7.343759,-4.647557,7.662363,6.663312,-4.802242,-8.810846,-5.950069,0.083626,2.469566,3.604966,-3.954358,-0.105095,-0.406486], dtype = "float64")#candidate|14190|(300,)|const|float64
call_14189 = func_2005_call(relay.reshape(const_14190.astype('float64'), [5, 12, 5]))
call_14191 = func_2005_call(relay.reshape(const_14190.astype('float64'), [5, 12, 5]))
func_13058_call = mod.get_global_var('func_13058')
func_13062_call = mutated_mod.get_global_var('func_13062')
const_14214 = relay.const([-9.251746,-0.004470,2.333580,-4.509508,6.532808,3.996340,8.638681,-8.937213,7.783751,-5.878431,0.172860,-0.471481,8.696995,5.916456,-0.598086,2.082152,-4.070846,0.906362,-5.947162,-8.706134,-3.637595,-9.820346,8.215066,8.160346,1.083434,-8.218541,-6.432502,-3.479721,8.915112,-2.002891,-3.753333,-6.653749,2.572627,-8.073668,2.884656,-7.648809,-9.735090,-2.975184,0.449966,-9.422960,8.960412,8.302510,6.066374,5.915600,-1.134097,-5.585561,2.134033,5.346408,-2.383009,-4.391274,-9.109476,-1.178037,8.318222,8.093277,-3.405356,-8.866803,-4.734977,4.575524,6.246922,-9.190804,-1.413724,-5.232662,-3.755516,-8.633045,2.056474,-5.720079,1.140731,-6.815432,9.850539,-6.744597,7.210936,-9.153675,-7.626299,5.561436,-4.028163,4.439272,-7.272888,8.542667,-8.237314,4.991701,-5.843200,0.266674,-7.102689,5.779511,6.853607,9.442680,-0.805887,-8.111146,4.303977,-4.495231,-5.896874,-9.456748,8.181581,3.372176,-8.370518,8.937423,-4.261034,-9.133385,-5.079879,1.216261,6.188612,-3.188571,-9.066499,8.197508,-8.378560,6.558964,9.260236,3.993515,4.464588,-4.129756,4.078647,6.242793,7.493792,2.931619,9.263697,9.269165,3.491726,-4.086596,3.572551,-0.129912,7.965467,-1.334433,1.416842,1.433965,-5.248646,-6.397639], dtype = "float32")#candidate|14214|(126,)|const|float32
call_14213 = relay.TupleGetItem(func_13058_call(relay.reshape(call_14185.astype('float64'), [2, 6, 11]), relay.reshape(const_14214.astype('float32'), [126, 1]), ), 1)
call_14215 = relay.TupleGetItem(func_13062_call(relay.reshape(call_14185.astype('float64'), [2, 6, 11]), relay.reshape(const_14214.astype('float32'), [126, 1]), ), 1)
func_12513_call = mod.get_global_var('func_12513')
func_12514_call = mutated_mod.get_global_var('func_12514')
call_14233 = relay.TupleGetItem(func_12513_call(), 2)
call_14234 = relay.TupleGetItem(func_12514_call(), 2)
output = relay.Tuple([call_14185,call_14189,const_14190,call_14213,const_14214,call_14233,])
output2 = relay.Tuple([call_14186,call_14191,const_14190,call_14215,const_14214,call_14234,])
func_14248 = relay.Function([], output)
mod['func_14248'] = func_14248
mod = relay.transform.InferType()(mod)
output = func_14248()
func_14249 = relay.Function([], output)
mutated_mod['func_14249'] = func_14249
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13499_call = mod.get_global_var('func_13499')
func_13500_call = mutated_mod.get_global_var('func_13500')
call_14255 = relay.TupleGetItem(func_13499_call(), 0)
call_14256 = relay.TupleGetItem(func_13500_call(), 0)
output = relay.Tuple([call_14255,])
output2 = relay.Tuple([call_14256,])
func_14268 = relay.Function([], output)
mod['func_14268'] = func_14268
mod = relay.transform.InferType()(mod)
mutated_mod['func_14268'] = func_14268
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14268_call = mutated_mod.get_global_var('func_14268')
call_14269 = func_14268_call()
output = call_14269
func_14270 = relay.Function([], output)
mutated_mod['func_14270'] = func_14270
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12866_call = mod.get_global_var('func_12866')
func_12867_call = mutated_mod.get_global_var('func_12867')
call_14296 = relay.TupleGetItem(func_12866_call(), 1)
call_14297 = relay.TupleGetItem(func_12867_call(), 1)
output = relay.Tuple([call_14296,])
output2 = relay.Tuple([call_14297,])
func_14308 = relay.Function([], output)
mod['func_14308'] = func_14308
mod = relay.transform.InferType()(mod)
mutated_mod['func_14308'] = func_14308
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14308_call = mutated_mod.get_global_var('func_14308')
call_14309 = func_14308_call()
output = call_14309
func_14310 = relay.Function([], output)
mutated_mod['func_14310'] = func_14310
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11837_call = mod.get_global_var('func_11837')
func_11838_call = mutated_mod.get_global_var('func_11838')
call_14324 = relay.TupleGetItem(func_11837_call(), 0)
call_14325 = relay.TupleGetItem(func_11838_call(), 0)
output = relay.Tuple([call_14324,])
output2 = relay.Tuple([call_14325,])
func_14342 = relay.Function([], output)
mod['func_14342'] = func_14342
mod = relay.transform.InferType()(mod)
output = func_14342()
func_14343 = relay.Function([], output)
mutated_mod['func_14343'] = func_14343
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14268_call = mod.get_global_var('func_14268')
func_14270_call = mutated_mod.get_global_var('func_14270')
call_14392 = relay.TupleGetItem(func_14268_call(), 0)
call_14393 = relay.TupleGetItem(func_14270_call(), 0)
output = call_14392
output2 = call_14393
func_14400 = relay.Function([], output)
mod['func_14400'] = func_14400
mod = relay.transform.InferType()(mod)
output = func_14400()
func_14401 = relay.Function([], output)
mutated_mod['func_14401'] = func_14401
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14124_call = mod.get_global_var('func_14124')
func_14125_call = mutated_mod.get_global_var('func_14125')
call_14416 = func_14124_call()
call_14417 = func_14124_call()
output = relay.Tuple([call_14416,])
output2 = relay.Tuple([call_14417,])
func_14418 = relay.Function([], output)
mod['func_14418'] = func_14418
mod = relay.transform.InferType()(mod)
mutated_mod['func_14418'] = func_14418
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14418_call = mutated_mod.get_global_var('func_14418')
call_14419 = func_14418_call()
output = call_14419
func_14420 = relay.Function([], output)
mutated_mod['func_14420'] = func_14420
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13950_call = mod.get_global_var('func_13950')
func_13952_call = mutated_mod.get_global_var('func_13952')
call_14438 = relay.TupleGetItem(func_13950_call(), 1)
call_14439 = relay.TupleGetItem(func_13952_call(), 1)
func_6053_call = mod.get_global_var('func_6053')
func_6056_call = mutated_mod.get_global_var('func_6056')
const_14443 = relay.const([[-9,-4,-5,-4,-6,5,-4,1,2,2,-5,-9,-4,4,8,-8,5,2,1,-4,8,4,-2,-5,6,2,-2,-4,-8,10,2,-1,-10,-7,-8,-9,-10,-8,9,5,-3,-7,-8,1,-1,9,7,-8,-4,-1,8,3,-4,-10,-6,-8,-2,4,-6,-5,4,-8,-8,1,5,-8,-1,-3,-10,9,10,5,-2,3,3,-5,-3,-1,3,-5,-3,1,2,8,9,-9,5,-10,-2,7,10,-4,8,6,-7,-8,-3,-2,-7,10,10,-4,3,3,6,5,-5,10,4,5,-8,10,3,10,-4,5,-10,-10,2,2,-7,-3,4,6,-3,9,-5,5,-1,-10,-3,-1,-4,8,6,4,-5,-6,4,8,4,-9,6,-6,6,6,-1,-4,7,10,2,-5,-1,-9,-4,2,-6,-4,2,-1,-6,-10,3,-1,-8,4,-5,10,-1,-2,-7,10,3,6,-3,-6,6,-7,9,-7,-1,8,1,3,-6,4,7,-5,-7,-8,1,-1,-9,4,-8,-7,-4,-2,-3,-5,-10,-10,-3,1,-9,-10,2,-5,-2,3,2,7,-4,-10,-6,6,4,-4,3,4,-4,-4,6,1,10,7,1,9,5,-4,4,8,6,-2,-7,4,-3,-10,-8,6,-3,2,-7,3,8,-4,5,-10,-3,-3,9,4,4,10,4,-1,-10,-5,4,2,3,-6,-5,-3,-9,9,-4,9,-8,3,8,1,7,-9,-5,-2,-5,1,3,10,-10,9,3,-5,10,3,10,-7,1,7,-7,4,-7,1,9,-3,2,5,3,-4,-8,10,10,-6,-5,9,-1,-1,-8,-10,8,7,7,-3,4,5,6,-1,-5,9,9,10,-1,-8,-7,-5,4,-3,6,1,-5,3,2,-8,-8,-6,5,6,-9,4,-3,-1,2,7,-1,-7,7,-8,3,-9,-4,-9,3,4,10,-9,6,-1,5,-6,10,-5,-3,-9,10,7,-3,1,-2,9,3,-8,-10,-7,10,-3,5,9,-10,6,8,-4,-2,8,-1,7,-7,-3,5,-3,-1,5,-4,-8,5,-4,7,-6,4,2,-3,7,3,10,-10,-5,1,9,-4,-2,8,4,4,4,-3,3,-5,-7,-2,8,-10,-3,3,-6,8,8,4,3,3,7,-4,-2,-1,-7,6,7,8,-6,-3,-10,10,8,1,1,-1,-9,-9,1,-2,4,-6,3,-10,-5,-1,3,2,-3,-7,8,-5,10,-8,3,-1,-7,8,1,8,1,2,9,7,8,8,-9,-2,6,-2,-1,6,2,-7,1,10,3,6,-7,-5,7,10,8,-9,-4,-1,-5,-3,2,9,-5,7,-10,-1,-8,-3,-2,4,-7,-2,3,-3,4,-5,-6,-2,-5,1,2,4,10,6,10,-4,5,7,-1,6,8,2,8,-9,10,8,-3,3,-10,7,-1,1,7,3,10,-5,-3,-6,-10,-5,4,6,6,3,10,-9,1,8,8,9,-3,10,-1,8,-3,6,6,5,3,1,-7,6,-10,7,-6,-10,1,6,8,7,-8,-9,7,8,1,1,2,10,-2,2,5,8,1,10,-9,-1,10,-1,3,4,1,-3,-7],[-4,2,-6,9,-1,-9,2,-7,-2,2,-3,7,8,-7,10,6,2,4,-4,-3,3,-7,-7,-7,-1,-6,-1,-6,-10,4,6,6,7,-5,2,6,-9,10,7,-6,-6,5,-5,10,3,-5,-3,4,-10,-3,-8,-6,3,-2,5,9,2,1,-4,-1,3,5,-5,-8,-1,-7,-9,5,-1,2,-6,-7,6,6,-9,8,-2,-9,-3,4,-7,2,-4,-10,5,8,3,-4,3,9,-6,3,-2,-7,-9,-9,-9,-2,2,-7,4,-10,1,3,3,-8,-1,-9,3,-7,4,-9,-1,-6,-3,-9,8,-3,5,-7,-10,-9,5,-5,1,-3,10,-10,2,-3,10,-3,3,-9,2,7,8,4,-4,-4,-2,4,8,6,-9,-5,1,9,-4,10,-4,-7,-7,-8,3,-7,-8,1,-4,-5,4,-4,-10,8,-1,7,7,10,8,-6,1,-5,4,-6,-3,-3,-3,-1,-10,-4,-9,-8,6,2,-7,4,-10,8,7,4,5,6,-6,8,7,-9,-4,5,-7,3,-3,-2,7,1,-4,-3,-4,-6,9,-6,-7,-3,6,-10,-4,6,9,2,-10,2,-8,4,6,-2,-5,1,5,-10,3,3,2,-5,-9,-8,8,6,7,-7,9,7,-8,-5,-4,4,-6,5,8,10,-6,8,-10,-1,-4,1,-10,9,-9,-2,1,2,-3,-5,6,-10,-6,6,5,-3,8,6,4,-5,-2,-6,5,8,5,-10,-9,-1,1,10,-7,-6,-9,-2,-8,6,5,10,-1,7,4,-7,10,-7,-7,6,10,-6,4,1,-4,3,8,9,-4,7,8,10,-2,-6,1,-3,-5,1,-7,-3,-7,2,10,9,2,3,-8,5,-9,10,-6,-3,2,-10,4,9,10,1,5,-5,5,-6,-10,-4,-5,-10,-7,-1,7,-7,-5,-4,-10,-6,-6,3,-8,4,-1,8,3,6,-1,9,8,-8,-4,9,-9,8,-5,-7,-1,2,1,9,-8,-6,-4,4,2,-7,6,10,-9,3,1,-9,-2,6,1,-9,-2,5,-1,8,-4,-8,10,-8,-6,3,2,2,2,-9,-7,1,3,-5,-6,-8,9,1,-5,8,-1,-1,-2,-10,4,7,-8,-1,4,-7,-1,1,2,9,2,-9,8,-7,-4,7,6,9,2,-9,8,-7,1,-8,3,-8,-5,-9,8,3,2,-2,-4,4,-3,-10,-7,7,-6,-10,-2,-3,5,10,-7,7,-3,-8,2,-10,-3,5,9,9,-8,-6,7,-9,-3,-8,-2,-10,4,1,-9,10,-3,-5,6,10,3,4,7,-4,2,1,-7,-8,-8,-6,10,-3,2,5,-2,-1,1,8,-9,-6,-4,-5,-7,-1,-2,4,-6,2,4,5,-2,-2,-2,-1,-3,-1,4,-8,-9,-6,10,2,6,4,-3,8,3,-10,-10,-5,-8,10,4,-2,8,5,-9,-4,3,7,-6,1,4,-4,2,9,-8,3,8,-7,5,-6,1,3,9,9,-2,-5,-4,3,8,8,-1,-8,-6,5,6,-10,-3,-10,1,-8,-10,1,1,1,-4,-3,-8,3,-5,7,-2,-10,-8,-9,-10,5,-1,-5,10,2]], dtype = "uint16")#candidate|14443|(2, 600)|const|uint16
call_14442 = func_6053_call(relay.reshape(const_14443.astype('uint16'), [10, 10, 12]), relay.reshape(const_14443.astype('uint16'), [10, 10, 12]), )
call_14444 = func_6053_call(relay.reshape(const_14443.astype('uint16'), [10, 10, 12]), relay.reshape(const_14443.astype('uint16'), [10, 10, 12]), )
output = relay.Tuple([call_14438,call_14442,const_14443,])
output2 = relay.Tuple([call_14439,call_14444,const_14443,])
func_14445 = relay.Function([], output)
mod['func_14445'] = func_14445
mod = relay.transform.InferType()(mod)
output = func_14445()
func_14446 = relay.Function([], output)
mutated_mod['func_14446'] = func_14446
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14445_call = mod.get_global_var('func_14445')
func_14446_call = mutated_mod.get_global_var('func_14446')
call_14447 = relay.TupleGetItem(func_14445_call(), 1)
call_14448 = relay.TupleGetItem(func_14446_call(), 1)
output = relay.Tuple([call_14447,])
output2 = relay.Tuple([call_14448,])
func_14458 = relay.Function([], output)
mod['func_14458'] = func_14458
mod = relay.transform.InferType()(mod)
mutated_mod['func_14458'] = func_14458
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14458_call = mutated_mod.get_global_var('func_14458')
call_14459 = func_14458_call()
output = call_14459
func_14460 = relay.Function([], output)
mutated_mod['func_14460'] = func_14460
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14248_call = mod.get_global_var('func_14248')
func_14249_call = mutated_mod.get_global_var('func_14249')
call_14502 = relay.TupleGetItem(func_14248_call(), 4)
call_14503 = relay.TupleGetItem(func_14249_call(), 4)
output = call_14502
output2 = call_14503
func_14508 = relay.Function([], output)
mod['func_14508'] = func_14508
mod = relay.transform.InferType()(mod)
mutated_mod['func_14508'] = func_14508
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14508_call = mutated_mod.get_global_var('func_14508')
call_14509 = func_14508_call()
output = call_14509
func_14510 = relay.Function([], output)
mutated_mod['func_14510'] = func_14510
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12838_call = mod.get_global_var('func_12838')
func_12840_call = mutated_mod.get_global_var('func_12840')
call_14690 = relay.TupleGetItem(func_12838_call(), 0)
call_14691 = relay.TupleGetItem(func_12840_call(), 0)
output = call_14690
output2 = call_14691
func_14719 = relay.Function([], output)
mod['func_14719'] = func_14719
mod = relay.transform.InferType()(mod)
mutated_mod['func_14719'] = func_14719
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14719_call = mutated_mod.get_global_var('func_14719')
call_14720 = func_14719_call()
output = call_14720
func_14721 = relay.Function([], output)
mutated_mod['func_14721'] = func_14721
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14400_call = mod.get_global_var('func_14400')
func_14401_call = mutated_mod.get_global_var('func_14401')
call_14725 = func_14400_call()
call_14726 = func_14400_call()
output = relay.Tuple([call_14725,])
output2 = relay.Tuple([call_14726,])
func_14761 = relay.Function([], output)
mod['func_14761'] = func_14761
mod = relay.transform.InferType()(mod)
output = func_14761()
func_14762 = relay.Function([], output)
mutated_mod['func_14762'] = func_14762
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14308_call = mod.get_global_var('func_14308')
func_14310_call = mutated_mod.get_global_var('func_14310')
call_14790 = relay.TupleGetItem(func_14308_call(), 0)
call_14791 = relay.TupleGetItem(func_14310_call(), 0)
output = call_14790
output2 = call_14791
func_14795 = relay.Function([], output)
mod['func_14795'] = func_14795
mod = relay.transform.InferType()(mod)
output = func_14795()
func_14796 = relay.Function([], output)
mutated_mod['func_14796'] = func_14796
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14719_call = mod.get_global_var('func_14719')
func_14721_call = mutated_mod.get_global_var('func_14721')
call_14835 = func_14719_call()
call_14836 = func_14719_call()
output = call_14835
output2 = call_14836
func_14839 = relay.Function([], output)
mod['func_14839'] = func_14839
mod = relay.transform.InferType()(mod)
output = func_14839()
func_14840 = relay.Function([], output)
mutated_mod['func_14840'] = func_14840
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14445_call = mod.get_global_var('func_14445')
func_14446_call = mutated_mod.get_global_var('func_14446')
call_14879 = relay.TupleGetItem(func_14445_call(), 2)
call_14880 = relay.TupleGetItem(func_14446_call(), 2)
var_14889 = relay.var("var_14889", dtype = "uint16", shape = (2, 600))#candidate|14889|(2, 600)|var|uint16
bop_14890 = relay.right_shift(call_14879.astype('int8'), relay.reshape(var_14889.astype('int8'), relay.shape_of(call_14879))) # shape=(2, 600)
bop_14893 = relay.right_shift(call_14880.astype('int8'), relay.reshape(var_14889.astype('int8'), relay.shape_of(call_14880))) # shape=(2, 600)
uop_14904 = relay.log2(var_14889.astype('float32')) # shape=(2, 600)
output = relay.Tuple([bop_14890,uop_14904,])
output2 = relay.Tuple([bop_14893,uop_14904,])
func_14907 = relay.Function([var_14889,], output)
mod['func_14907'] = func_14907
mod = relay.transform.InferType()(mod)
mutated_mod['func_14907'] = func_14907
mutated_mod = relay.transform.InferType()(mutated_mod)
var_14908 = relay.var("var_14908", dtype = "uint16", shape = (2, 600))#candidate|14908|(2, 600)|var|uint16
func_14907_call = mutated_mod.get_global_var('func_14907')
call_14909 = func_14907_call(var_14908)
output = call_14909
func_14910 = relay.Function([var_14908], output)
mutated_mod['func_14910'] = func_14910
mutated_mod = relay.transform.InferType()(mutated_mod)
var_14912 = relay.var("var_14912", dtype = "float32", shape = (11, 16, 6))#candidate|14912|(11, 16, 6)|var|float32
uop_14913 = relay.log2(var_14912.astype('float32')) # shape=(11, 16, 6)
output = uop_14913
output2 = uop_14913
func_14917 = relay.Function([var_14912,], output)
mod['func_14917'] = func_14917
mod = relay.transform.InferType()(mod)
mutated_mod['func_14917'] = func_14917
mutated_mod = relay.transform.InferType()(mutated_mod)
var_14918 = relay.var("var_14918", dtype = "float32", shape = (11, 16, 6))#candidate|14918|(11, 16, 6)|var|float32
func_14917_call = mutated_mod.get_global_var('func_14917')
call_14919 = func_14917_call(var_14918)
output = call_14919
func_14920 = relay.Function([var_14918], output)
mutated_mod['func_14920'] = func_14920
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12011_call = mod.get_global_var('func_12011')
func_12012_call = mutated_mod.get_global_var('func_12012')
call_14941 = relay.TupleGetItem(func_12011_call(), 1)
call_14942 = relay.TupleGetItem(func_12012_call(), 1)
output = relay.Tuple([call_14941,])
output2 = relay.Tuple([call_14942,])
func_14965 = relay.Function([], output)
mod['func_14965'] = func_14965
mod = relay.transform.InferType()(mod)
mutated_mod['func_14965'] = func_14965
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14965_call = mutated_mod.get_global_var('func_14965')
call_14966 = func_14965_call()
output = call_14966
func_14967 = relay.Function([], output)
mutated_mod['func_14967'] = func_14967
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12011_call = mod.get_global_var('func_12011')
func_12012_call = mutated_mod.get_global_var('func_12012')
call_15016 = relay.TupleGetItem(func_12011_call(), 0)
call_15017 = relay.TupleGetItem(func_12012_call(), 0)
func_13412_call = mod.get_global_var('func_13412')
func_13416_call = mutated_mod.get_global_var('func_13416')
var_15022 = relay.var("var_15022", dtype = "float32", shape = (264,))#candidate|15022|(264,)|var|float32
var_15023 = relay.var("var_15023", dtype = "int64", shape = (224, 2))#candidate|15023|(224, 2)|var|int64
call_15021 = relay.TupleGetItem(func_13412_call(relay.reshape(var_15022.astype('float32'), [132, 2]), relay.reshape(var_15023.astype('int64'), [8, 56]), ), 2)
call_15024 = relay.TupleGetItem(func_13416_call(relay.reshape(var_15022.astype('float32'), [132, 2]), relay.reshape(var_15023.astype('int64'), [8, 56]), ), 2)
func_12105_call = mod.get_global_var('func_12105')
func_12110_call = mutated_mod.get_global_var('func_12110')
var_15027 = relay.var("var_15027", dtype = "int8", shape = (1260,))#candidate|15027|(1260,)|var|int8
const_15028 = relay.const([[5.021560],[-4.608300],[1.382941],[5.264983],[0.778164],[-1.846424],[5.478925],[8.347338],[0.491538],[-7.870982],[3.589762],[8.656283],[-6.158352],[-5.513986],[0.209104],[6.762435],[-1.438419],[0.193035],[2.353873],[8.015291],[-3.807082],[1.712720],[8.572509],[9.049570],[-0.585964],[-7.974620],[8.531539],[-9.600360],[-8.841959],[-0.510815],[-8.026642],[2.567017],[-9.532239],[-2.072433],[9.666383],[-8.066940],[0.138466],[-1.830014],[-7.774827],[-5.940251]], dtype = "float64")#candidate|15028|(40, 1)|const|float64
const_15029 = relay.const([-3.141586,7.521966,-3.115658,-6.426088,0.905338,9.056046,-3.089545,0.459619,-2.089345,6.976003,-1.417478,-9.810424,7.850166,4.847406,-4.482089,6.380396,7.749467,5.192165,9.614358,-5.917703,9.296045,-7.629268,1.020099,-8.583592,1.229224,-6.704842,4.016212,-1.210415,1.939913,5.336062,-0.741759,-2.932974,6.904135,-4.086344,0.337029,-9.030531,-1.093253,-1.040439,-1.706453,3.786837,-4.287592,1.429855,4.168980,-6.118293,-2.383442,-2.184670,0.098404,-9.707708,-4.228337,8.152883,9.307955,2.458577,-6.410169,1.444923,-8.609973,-3.226255,-9.904291,-0.805577,2.259676,-4.263607,-2.739904,7.078981,1.680693,6.432041,-1.527256,7.815446,-5.744452,2.427837,-7.487455,2.681294,-3.433288,2.011174,-6.588072,-9.414916,3.075128,9.932752,2.061912,7.294360,-8.363195,-4.307422,0.909225,-0.800724,-4.079484,-8.093183,-5.556266,4.463699,7.582652,-2.647492,-0.864311,2.309610,4.534848,-2.811394,3.004802,-9.664445,-2.345406,-3.209678,-2.198942,3.644830,8.527808,-0.692429,5.915522,-0.544584,-8.483007,-9.072574,5.174227,-8.024661,-5.231912,9.599517,-8.957512,8.445998,-4.289083,-6.138701,-3.721878,-2.857228,0.179631,-1.650248,-0.856964,6.531223,7.769947,-8.841723,-5.849285,7.116117,2.001634,-7.360566,-3.031587,-8.372495,-6.339317,-5.492378,-7.599728,-8.553231,4.831077,-2.104242,6.290015,-2.363879,-8.666413,8.495149,-2.290711,8.502833,2.858598,7.788958,-8.444763,-6.241610,0.859076,1.199947,0.509080,8.300923,-4.213149,8.821703,-8.176997,-4.451722,-8.601665,9.672499,7.693294,-4.862232,-6.863848,-0.553380,5.935781,9.069139,3.468329,-7.599840,-9.765712,9.652099,2.659678,-6.981780,0.762230,-0.400388,-1.306710,-5.770270,5.937767,-4.357148,-9.502814,-6.524697,-3.054745,-0.897883,-6.464735,-3.027255,7.580302,-7.565278,-0.616197,-8.295712,7.880739,1.053731,-1.681398,8.794361,-7.477676,9.400046,0.948458,-4.465550,-9.982145,7.549365,6.661079,8.184668,-6.159130,-1.957146,8.070507,-6.948367,3.522662,-5.976931,7.734589,4.007774,-1.911087,-3.692591,-4.435085,5.794587,-6.930941,-0.441057,-8.765193,-9.372184,2.588317,-2.825498,4.960764,5.426199,-7.639454,-7.987387,-8.379542,-4.683802,-5.456094,-2.681604,1.166418,6.867478], dtype = "float32")#candidate|15029|(220,)|const|float32
var_15030 = relay.var("var_15030", dtype = "uint64", shape = (1320,))#candidate|15030|(1320,)|var|uint64
call_15026 = relay.TupleGetItem(func_12105_call(relay.reshape(var_15027.astype('int8'), [1260,]), relay.reshape(const_15028.astype('float64'), [40,]), relay.reshape(const_15029.astype('float32'), [220,]), relay.reshape(var_15030.astype('uint64'), [1320,]), ), 7)
call_15031 = relay.TupleGetItem(func_12110_call(relay.reshape(var_15027.astype('int8'), [1260,]), relay.reshape(const_15028.astype('float64'), [40,]), relay.reshape(const_15029.astype('float32'), [220,]), relay.reshape(var_15030.astype('uint64'), [1320,]), ), 7)
uop_15047 = relay.sinh(call_15021.astype('float32')) # shape=(132, 2)
uop_15049 = relay.sinh(call_15024.astype('float32')) # shape=(132, 2)
output = relay.Tuple([call_15016,var_15022,var_15023,call_15026,var_15027,const_15028,const_15029,var_15030,uop_15047,])
output2 = relay.Tuple([call_15017,var_15022,var_15023,call_15031,var_15027,const_15028,const_15029,var_15030,uop_15049,])
func_15053 = relay.Function([var_15022,var_15023,var_15027,var_15030,], output)
mod['func_15053'] = func_15053
mod = relay.transform.InferType()(mod)
mutated_mod['func_15053'] = func_15053
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15053_call = mutated_mod.get_global_var('func_15053')
var_15055 = relay.var("var_15055", dtype = "float32", shape = (264,))#candidate|15055|(264,)|var|float32
var_15056 = relay.var("var_15056", dtype = "int64", shape = (224, 2))#candidate|15056|(224, 2)|var|int64
var_15057 = relay.var("var_15057", dtype = "int8", shape = (1260,))#candidate|15057|(1260,)|var|int8
var_15058 = relay.var("var_15058", dtype = "uint64", shape = (1320,))#candidate|15058|(1320,)|var|uint64
call_15054 = func_15053_call(var_15055,var_15056,var_15057,var_15058,)
output = call_15054
func_15059 = relay.Function([var_15055,var_15056,var_15057,var_15058,], output)
mutated_mod['func_15059'] = func_15059
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14248_call = mod.get_global_var('func_14248')
func_14249_call = mutated_mod.get_global_var('func_14249')
call_15072 = relay.TupleGetItem(func_14248_call(), 2)
call_15073 = relay.TupleGetItem(func_14249_call(), 2)
output = relay.Tuple([call_15072,])
output2 = relay.Tuple([call_15073,])
func_15108 = relay.Function([], output)
mod['func_15108'] = func_15108
mod = relay.transform.InferType()(mod)
output = func_15108()
func_15109 = relay.Function([], output)
mutated_mod['func_15109'] = func_15109
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12722_call = mod.get_global_var('func_12722')
func_12724_call = mutated_mod.get_global_var('func_12724')
call_15117 = func_12722_call()
call_15118 = func_12722_call()
output = call_15117
output2 = call_15118
func_15169 = relay.Function([], output)
mod['func_15169'] = func_15169
mod = relay.transform.InferType()(mod)
mutated_mod['func_15169'] = func_15169
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15169_call = mutated_mod.get_global_var('func_15169')
call_15170 = func_15169_call()
output = call_15170
func_15171 = relay.Function([], output)
mutated_mod['func_15171'] = func_15171
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12866_call = mod.get_global_var('func_12866')
func_12867_call = mutated_mod.get_global_var('func_12867')
call_15179 = relay.TupleGetItem(func_12866_call(), 1)
call_15180 = relay.TupleGetItem(func_12867_call(), 1)
func_14268_call = mod.get_global_var('func_14268')
func_14270_call = mutated_mod.get_global_var('func_14270')
call_15181 = relay.TupleGetItem(func_14268_call(), 0)
call_15182 = relay.TupleGetItem(func_14270_call(), 0)
output = relay.Tuple([call_15179,call_15181,])
output2 = relay.Tuple([call_15180,call_15182,])
func_15203 = relay.Function([], output)
mod['func_15203'] = func_15203
mod = relay.transform.InferType()(mod)
mutated_mod['func_15203'] = func_15203
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15203_call = mutated_mod.get_global_var('func_15203')
call_15204 = func_15203_call()
output = call_15204
func_15205 = relay.Function([], output)
mutated_mod['func_15205'] = func_15205
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12737_call = mod.get_global_var('func_12737')
func_12739_call = mutated_mod.get_global_var('func_12739')
call_15268 = func_12737_call()
call_15269 = func_12737_call()
output = call_15268
output2 = call_15269
func_15280 = relay.Function([], output)
mod['func_15280'] = func_15280
mod = relay.transform.InferType()(mod)
mutated_mod['func_15280'] = func_15280
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15280_call = mutated_mod.get_global_var('func_15280')
call_15281 = func_15280_call()
output = call_15281
func_15282 = relay.Function([], output)
mutated_mod['func_15282'] = func_15282
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13645_call = mod.get_global_var('func_13645')
func_13646_call = mutated_mod.get_global_var('func_13646')
call_15328 = relay.TupleGetItem(func_13645_call(), 0)
call_15329 = relay.TupleGetItem(func_13646_call(), 0)
output = relay.Tuple([call_15328,])
output2 = relay.Tuple([call_15329,])
func_15330 = relay.Function([], output)
mod['func_15330'] = func_15330
mod = relay.transform.InferType()(mod)
output = func_15330()
func_15331 = relay.Function([], output)
mutated_mod['func_15331'] = func_15331
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15169_call = mod.get_global_var('func_15169')
func_15171_call = mutated_mod.get_global_var('func_15171')
call_15332 = func_15169_call()
call_15333 = func_15169_call()
func_5115_call = mod.get_global_var('func_5115')
func_5117_call = mutated_mod.get_global_var('func_5117')
var_15355 = relay.var("var_15355", dtype = "uint32", shape = ())#candidate|15355|()|var|uint32
call_15354 = relay.TupleGetItem(func_5115_call(relay.reshape(var_15355.astype('uint32'), [])), 0)
call_15356 = relay.TupleGetItem(func_5117_call(relay.reshape(var_15355.astype('uint32'), [])), 0)
output = relay.Tuple([call_15332,call_15354,var_15355,])
output2 = relay.Tuple([call_15333,call_15356,var_15355,])
func_15361 = relay.Function([var_15355,], output)
mod['func_15361'] = func_15361
mod = relay.transform.InferType()(mod)
mutated_mod['func_15361'] = func_15361
mutated_mod = relay.transform.InferType()(mutated_mod)
var_15362 = relay.var("var_15362", dtype = "uint32", shape = ())#candidate|15362|()|var|uint32
func_15361_call = mutated_mod.get_global_var('func_15361')
call_15363 = func_15361_call(var_15362)
output = call_15363
func_15364 = relay.Function([var_15362], output)
mutated_mod['func_15364'] = func_15364
mutated_mod = relay.transform.InferType()(mutated_mod)
const_15377 = relay.const([[[False,False,False,False]],[[True,True,False,False]],[[True,True,False,True]],[[False,False,False,True]],[[False,True,False,False]],[[True,False,True,False]],[[True,True,True,False]],[[True,True,False,True]],[[True,True,False,False]],[[False,False,True,True]],[[True,True,False,True]],[[False,False,False,False]],[[False,False,False,True]],[[False,False,True,True]],[[True,True,True,False]],[[False,False,False,True]]], dtype = "bool")#candidate|15377|(16, 1, 4)|const|bool
var_15378 = relay.var("var_15378", dtype = "bool", shape = (16, 12, 4))#candidate|15378|(16, 12, 4)|var|bool
bop_15379 = relay.logical_and(const_15377.astype('bool'), var_15378.astype('bool')) # shape=(16, 12, 4)
func_12166_call = mod.get_global_var('func_12166')
func_12169_call = mutated_mod.get_global_var('func_12169')
var_15385 = relay.var("var_15385", dtype = "float64", shape = (132,))#candidate|15385|(132,)|var|float64
call_15384 = relay.TupleGetItem(func_12166_call(relay.reshape(var_15385.astype('float64'), [2, 6, 11])), 0)
call_15386 = relay.TupleGetItem(func_12169_call(relay.reshape(var_15385.astype('float64'), [2, 6, 11])), 0)
var_15399 = relay.var("var_15399", dtype = "bool", shape = (16, 10, 4))#candidate|15399|(16, 10, 4)|var|bool
bop_15400 = relay.floor_mod(const_15377.astype('float64'), var_15399.astype('float64')) # shape=(16, 10, 4)
output = relay.Tuple([bop_15379,call_15384,var_15385,bop_15400,])
output2 = relay.Tuple([bop_15379,call_15386,var_15385,bop_15400,])
func_15404 = relay.Function([var_15378,var_15385,var_15399,], output)
mod['func_15404'] = func_15404
mod = relay.transform.InferType()(mod)
mutated_mod['func_15404'] = func_15404
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15404_call = mutated_mod.get_global_var('func_15404')
var_15406 = relay.var("var_15406", dtype = "bool", shape = (16, 12, 4))#candidate|15406|(16, 12, 4)|var|bool
var_15407 = relay.var("var_15407", dtype = "float64", shape = (132,))#candidate|15407|(132,)|var|float64
var_15408 = relay.var("var_15408", dtype = "bool", shape = (16, 10, 4))#candidate|15408|(16, 10, 4)|var|bool
call_15405 = func_15404_call(var_15406,var_15407,var_15408,)
output = call_15405
func_15409 = relay.Function([var_15406,var_15407,var_15408,], output)
mutated_mod['func_15409'] = func_15409
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13726_call = mod.get_global_var('func_13726')
func_13727_call = mutated_mod.get_global_var('func_13727')
call_15444 = relay.TupleGetItem(func_13726_call(), 1)
call_15445 = relay.TupleGetItem(func_13727_call(), 1)
func_13876_call = mod.get_global_var('func_13876')
func_13879_call = mutated_mod.get_global_var('func_13879')
var_15453 = relay.var("var_15453", dtype = "float32", shape = (540, 1))#candidate|15453|(540, 1)|var|float32
call_15452 = relay.TupleGetItem(func_13876_call(relay.reshape(var_15453.astype('float32'), [540,])), 12)
call_15454 = relay.TupleGetItem(func_13879_call(relay.reshape(var_15453.astype('float32'), [540,])), 12)
output = relay.Tuple([call_15444,call_15452,var_15453,])
output2 = relay.Tuple([call_15445,call_15454,var_15453,])
func_15458 = relay.Function([var_15453,], output)
mod['func_15458'] = func_15458
mod = relay.transform.InferType()(mod)
var_15459 = relay.var("var_15459", dtype = "float32", shape = (540, 1))#candidate|15459|(540, 1)|var|float32
output = func_15458(var_15459)
func_15460 = relay.Function([var_15459], output)
mutated_mod['func_15460'] = func_15460
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12121_call = mod.get_global_var('func_12121')
func_12123_call = mutated_mod.get_global_var('func_12123')
call_15477 = relay.TupleGetItem(func_12121_call(), 0)
call_15478 = relay.TupleGetItem(func_12123_call(), 0)
func_13645_call = mod.get_global_var('func_13645')
func_13646_call = mutated_mod.get_global_var('func_13646')
call_15480 = relay.TupleGetItem(func_13645_call(), 0)
call_15481 = relay.TupleGetItem(func_13646_call(), 0)
output = relay.Tuple([call_15477,call_15480,])
output2 = relay.Tuple([call_15478,call_15481,])
func_15483 = relay.Function([], output)
mod['func_15483'] = func_15483
mod = relay.transform.InferType()(mod)
output = func_15483()
func_15484 = relay.Function([], output)
mutated_mod['func_15484'] = func_15484
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14508_call = mod.get_global_var('func_14508')
func_14510_call = mutated_mod.get_global_var('func_14510')
call_15485 = func_14508_call()
call_15486 = func_14508_call()
output = call_15485
output2 = call_15486
func_15489 = relay.Function([], output)
mod['func_15489'] = func_15489
mod = relay.transform.InferType()(mod)
mutated_mod['func_15489'] = func_15489
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15489_call = mutated_mod.get_global_var('func_15489')
call_15490 = func_15489_call()
output = call_15490
func_15491 = relay.Function([], output)
mutated_mod['func_15491'] = func_15491
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14445_call = mod.get_global_var('func_14445')
func_14446_call = mutated_mod.get_global_var('func_14446')
call_15502 = relay.TupleGetItem(func_14445_call(), 1)
call_15503 = relay.TupleGetItem(func_14446_call(), 1)
output = relay.Tuple([call_15502,])
output2 = relay.Tuple([call_15503,])
func_15506 = relay.Function([], output)
mod['func_15506'] = func_15506
mod = relay.transform.InferType()(mod)
mutated_mod['func_15506'] = func_15506
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15506_call = mutated_mod.get_global_var('func_15506')
call_15507 = func_15506_call()
output = call_15507
func_15508 = relay.Function([], output)
mutated_mod['func_15508'] = func_15508
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14719_call = mod.get_global_var('func_14719')
func_14721_call = mutated_mod.get_global_var('func_14721')
call_15568 = func_14719_call()
call_15569 = func_14719_call()
output = call_15568
output2 = call_15569
func_15598 = relay.Function([], output)
mod['func_15598'] = func_15598
mod = relay.transform.InferType()(mod)
mutated_mod['func_15598'] = func_15598
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15598_call = mutated_mod.get_global_var('func_15598')
call_15599 = func_15598_call()
output = call_15599
func_15600 = relay.Function([], output)
mutated_mod['func_15600'] = func_15600
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12513_call = mod.get_global_var('func_12513')
func_12514_call = mutated_mod.get_global_var('func_12514')
call_15634 = relay.TupleGetItem(func_12513_call(), 0)
call_15635 = relay.TupleGetItem(func_12514_call(), 0)
func_8304_call = mod.get_global_var('func_8304')
func_8307_call = mutated_mod.get_global_var('func_8307')
var_15647 = relay.var("var_15647", dtype = "float32", shape = (54, 10))#candidate|15647|(54, 10)|var|float32
call_15646 = func_8304_call(relay.reshape(var_15647.astype('float32'), [15, 12, 3]))
call_15648 = func_8304_call(relay.reshape(var_15647.astype('float32'), [15, 12, 3]))
bop_15649 = relay.bitwise_and(var_15647.astype('int64'), relay.reshape(call_15646.astype('int64'), relay.shape_of(var_15647))) # shape=(54, 10)
bop_15652 = relay.bitwise_and(var_15647.astype('int64'), relay.reshape(call_15648.astype('int64'), relay.shape_of(var_15647))) # shape=(54, 10)
uop_15653 = relay.atanh(var_15647.astype('float64')) # shape=(54, 10)
output = relay.Tuple([call_15634,bop_15649,uop_15653,])
output2 = relay.Tuple([call_15635,bop_15652,uop_15653,])
func_15656 = relay.Function([var_15647,], output)
mod['func_15656'] = func_15656
mod = relay.transform.InferType()(mod)
mutated_mod['func_15656'] = func_15656
mutated_mod = relay.transform.InferType()(mutated_mod)
var_15657 = relay.var("var_15657", dtype = "float32", shape = (54, 10))#candidate|15657|(54, 10)|var|float32
func_15656_call = mutated_mod.get_global_var('func_15656')
call_15658 = func_15656_call(var_15657)
output = call_15658
func_15659 = relay.Function([var_15657], output)
mutated_mod['func_15659'] = func_15659
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12866_call = mod.get_global_var('func_12866')
func_12867_call = mutated_mod.get_global_var('func_12867')
call_15681 = relay.TupleGetItem(func_12866_call(), 1)
call_15682 = relay.TupleGetItem(func_12867_call(), 1)
var_15696 = relay.var("var_15696", dtype = "float64", shape = (2, 6, 11))#candidate|15696|(2, 6, 11)|var|float64
bop_15697 = relay.logical_xor(call_15681.astype('int16'), relay.reshape(var_15696.astype('int16'), relay.shape_of(call_15681))) # shape=(2, 6, 11)
bop_15700 = relay.logical_xor(call_15682.astype('int16'), relay.reshape(var_15696.astype('int16'), relay.shape_of(call_15682))) # shape=(2, 6, 11)
uop_15704 = relay.tan(bop_15697.astype('float64')) # shape=(2, 6, 11)
uop_15706 = relay.tan(bop_15700.astype('float64')) # shape=(2, 6, 11)
output = uop_15704
output2 = uop_15706
func_15720 = relay.Function([var_15696,], output)
mod['func_15720'] = func_15720
mod = relay.transform.InferType()(mod)
var_15721 = relay.var("var_15721", dtype = "float64", shape = (2, 6, 11))#candidate|15721|(2, 6, 11)|var|float64
output = func_15720(var_15721)
func_15722 = relay.Function([var_15721], output)
mutated_mod['func_15722'] = func_15722
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13499_call = mod.get_global_var('func_13499')
func_13500_call = mutated_mod.get_global_var('func_13500')
call_15860 = relay.TupleGetItem(func_13499_call(), 1)
call_15861 = relay.TupleGetItem(func_13500_call(), 1)
output = call_15860
output2 = call_15861
func_15872 = relay.Function([], output)
mod['func_15872'] = func_15872
mod = relay.transform.InferType()(mod)
mutated_mod['func_15872'] = func_15872
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15872_call = mutated_mod.get_global_var('func_15872')
call_15873 = func_15872_call()
output = call_15873
func_15874 = relay.Function([], output)
mutated_mod['func_15874'] = func_15874
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14839_call = mod.get_global_var('func_14839')
func_14840_call = mutated_mod.get_global_var('func_14840')
call_15944 = func_14839_call()
call_15945 = func_14839_call()
output = relay.Tuple([call_15944,])
output2 = relay.Tuple([call_15945,])
func_15964 = relay.Function([], output)
mod['func_15964'] = func_15964
mod = relay.transform.InferType()(mod)
mutated_mod['func_15964'] = func_15964
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15964_call = mutated_mod.get_global_var('func_15964')
call_15965 = func_15964_call()
output = call_15965
func_15966 = relay.Function([], output)
mutated_mod['func_15966'] = func_15966
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12866_call = mod.get_global_var('func_12866')
func_12867_call = mutated_mod.get_global_var('func_12867')
call_16001 = relay.TupleGetItem(func_12866_call(), 0)
call_16002 = relay.TupleGetItem(func_12867_call(), 0)
output = relay.Tuple([call_16001,])
output2 = relay.Tuple([call_16002,])
func_16005 = relay.Function([], output)
mod['func_16005'] = func_16005
mod = relay.transform.InferType()(mod)
mutated_mod['func_16005'] = func_16005
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16005_call = mutated_mod.get_global_var('func_16005')
call_16006 = func_16005_call()
output = call_16006
func_16007 = relay.Function([], output)
mutated_mod['func_16007'] = func_16007
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14248_call = mod.get_global_var('func_14248')
func_14249_call = mutated_mod.get_global_var('func_14249')
call_16008 = relay.TupleGetItem(func_14248_call(), 5)
call_16009 = relay.TupleGetItem(func_14249_call(), 5)
output = call_16008
output2 = call_16009
func_16017 = relay.Function([], output)
mod['func_16017'] = func_16017
mod = relay.transform.InferType()(mod)
mutated_mod['func_16017'] = func_16017
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16017_call = mutated_mod.get_global_var('func_16017')
call_16018 = func_16017_call()
output = call_16018
func_16019 = relay.Function([], output)
mutated_mod['func_16019'] = func_16019
mutated_mod = relay.transform.InferType()(mutated_mod)
var_16023 = relay.var("var_16023", dtype = "float64", shape = (16, 11, 16))#candidate|16023|(16, 11, 16)|var|float64
uop_16024 = relay.erf(var_16023.astype('float64')) # shape=(16, 11, 16)
func_2297_call = mod.get_global_var('func_2297')
func_2300_call = mutated_mod.get_global_var('func_2300')
const_16027 = relay.const(-0.541343, dtype = "float32")#candidate|16027|()|const|float32
const_16028 = relay.const([[4.757400,5.059208,7.018321,3.884028,3.647214,-8.065981,9.840178,7.955387,-4.318666,9.814122,-7.639849,-6.648015,1.218369,-2.581539,3.471562,-0.848815,-7.594331,9.148522,3.645570,6.080608,-4.215816,4.732460,-0.331844,2.302221,0.687699,4.034928,4.539760,-1.323034,4.694618,-5.020102,9.855772,-2.562493,-3.387872,2.552517,-4.084307,-0.863384,5.087995,-8.550147,-8.495640,-6.564707,-5.016043,-7.865889,-5.278077,6.190468,0.347483,-3.853516,-9.335323,-4.153888,-4.095529,3.915089,-3.941796,3.634340,9.578657,6.542882,-9.964936,5.770786,-6.976002,-1.449044,-9.956915,-0.601028,-9.936784,-9.498342,5.381186,4.206473,-0.167756,-0.129322,9.879268,-8.817518,-7.806959,-7.296890,-7.126321,4.140243,1.820376,1.754946,4.044547,-6.420917,-4.305749,8.415699,0.732474,0.009105,6.697837,1.553691,-7.679745,1.094729,0.087802,5.240216,1.717543,-9.857127,-2.867133,-2.222208,-3.303910,0.997248,3.792458,-1.211679,-3.944832,-8.222727,-2.864516,-4.581143,-9.712502,4.974884,7.506726,9.255744,0.289180,-0.024403,3.415362,-0.977139,1.369139,-9.497895,-8.481582,5.431855,-0.637808,-6.677614,2.321125,0.903439,-7.821170,-0.506477,4.690610,-8.412613,2.485107,9.675991,9.408115,-2.132948,9.184134,4.706663,-1.588737,-6.371814,-1.153622,5.061210,6.849958,5.481381,4.264859,-7.613266,2.348393,4.941365,0.179616,6.654447,-7.467322,9.063977,-3.109905,5.903679,8.771703,-7.207515,-5.486433,-5.617085,-9.261505,5.070945,2.627320,7.368020,-2.440045,4.153139,9.915683,-9.461235,5.877948,5.169162,-1.605672,-6.470475,5.567070,-5.322505,-9.659260,5.833543,-4.272215,-2.517049,-3.657575,8.976863,-3.136642,-9.801951,4.974705,-8.222342,-1.378385,8.236695,-9.686026,5.430940,-8.348395,-0.203946,-3.400899,2.658733,-0.351338,-7.332733,3.647188,-3.020793,-1.420515,9.870497,6.348259,-5.722910,-0.359567,3.809860,3.747872,-5.148633,-0.248061,-0.274371,-2.409444,4.112755,9.015421,-3.842815,5.424931,2.362992,4.646729,-9.340076,-8.756391,0.240228,-2.971274,6.492210,1.344028,7.013308,-2.525984,-6.754833,9.399467,-1.964444,5.986648,-1.691485,4.328304,-5.559225,-1.397383,6.833773,-4.441463,1.457917,3.160078,-6.015139,-8.280621,-0.945985]], dtype = "float32")#candidate|16028|(1, 220)|const|float32
call_16026 = func_2297_call(relay.reshape(const_16027.astype('float32'), []), relay.reshape(const_16028.astype('float32'), [11, 5, 4]), )
call_16029 = func_2297_call(relay.reshape(const_16027.astype('float32'), []), relay.reshape(const_16028.astype('float32'), [11, 5, 4]), )
func_13950_call = mod.get_global_var('func_13950')
func_13952_call = mutated_mod.get_global_var('func_13952')
call_16033 = relay.TupleGetItem(func_13950_call(), 1)
call_16034 = relay.TupleGetItem(func_13952_call(), 1)
output = relay.Tuple([uop_16024,call_16026,const_16027,const_16028,call_16033,])
output2 = relay.Tuple([uop_16024,call_16029,const_16027,const_16028,call_16034,])
func_16040 = relay.Function([var_16023,], output)
mod['func_16040'] = func_16040
mod = relay.transform.InferType()(mod)
var_16041 = relay.var("var_16041", dtype = "float64", shape = (16, 11, 16))#candidate|16041|(16, 11, 16)|var|float64
output = func_16040(var_16041)
func_16042 = relay.Function([var_16041], output)
mutated_mod['func_16042'] = func_16042
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11837_call = mod.get_global_var('func_11837')
func_11838_call = mutated_mod.get_global_var('func_11838')
call_16128 = relay.TupleGetItem(func_11837_call(), 0)
call_16129 = relay.TupleGetItem(func_11838_call(), 0)
output = call_16128
output2 = call_16129
func_16145 = relay.Function([], output)
mod['func_16145'] = func_16145
mod = relay.transform.InferType()(mod)
mutated_mod['func_16145'] = func_16145
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16145_call = mutated_mod.get_global_var('func_16145')
call_16146 = func_16145_call()
output = call_16146
func_16147 = relay.Function([], output)
mutated_mod['func_16147'] = func_16147
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13081_call = mod.get_global_var('func_13081')
func_13083_call = mutated_mod.get_global_var('func_13083')
call_16157 = relay.TupleGetItem(func_13081_call(), 0)
call_16158 = relay.TupleGetItem(func_13083_call(), 0)
output = relay.Tuple([call_16157,])
output2 = relay.Tuple([call_16158,])
func_16168 = relay.Function([], output)
mod['func_16168'] = func_16168
mod = relay.transform.InferType()(mod)
mutated_mod['func_16168'] = func_16168
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16168_call = mutated_mod.get_global_var('func_16168')
call_16169 = func_16168_call()
output = call_16169
func_16170 = relay.Function([], output)
mutated_mod['func_16170'] = func_16170
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15108_call = mod.get_global_var('func_15108')
func_15109_call = mutated_mod.get_global_var('func_15109')
call_16181 = relay.TupleGetItem(func_15108_call(), 0)
call_16182 = relay.TupleGetItem(func_15109_call(), 0)
output = relay.Tuple([call_16181,])
output2 = relay.Tuple([call_16182,])
func_16193 = relay.Function([], output)
mod['func_16193'] = func_16193
mod = relay.transform.InferType()(mod)
output = func_16193()
func_16194 = relay.Function([], output)
mutated_mod['func_16194'] = func_16194
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12866_call = mod.get_global_var('func_12866')
func_12867_call = mutated_mod.get_global_var('func_12867')
call_16232 = relay.TupleGetItem(func_12866_call(), 0)
call_16233 = relay.TupleGetItem(func_12867_call(), 0)
output = call_16232
output2 = call_16233
func_16244 = relay.Function([], output)
mod['func_16244'] = func_16244
mod = relay.transform.InferType()(mod)
mutated_mod['func_16244'] = func_16244
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16244_call = mutated_mod.get_global_var('func_16244')
call_16245 = func_16244_call()
output = call_16245
func_16246 = relay.Function([], output)
mutated_mod['func_16246'] = func_16246
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15506_call = mod.get_global_var('func_15506')
func_15508_call = mutated_mod.get_global_var('func_15508')
call_16257 = relay.TupleGetItem(func_15506_call(), 0)
call_16258 = relay.TupleGetItem(func_15508_call(), 0)
func_13256_call = mod.get_global_var('func_13256')
func_13258_call = mutated_mod.get_global_var('func_13258')
const_16285 = relay.const([-2.645219,6.862210,8.537936,-6.078639,-6.362171,0.822478,1.091214,4.655233,6.012076,-0.328950,4.868930,-9.006544,4.999584,-0.753743,-3.804619,1.788672,5.103583,-8.526844,-0.312173,0.028136,-7.421029,4.001484,0.109021,-6.178599,-0.405172,-3.586122,8.839877,4.755713,-7.887697,1.287789,-4.359409,3.693140,3.463193,-0.863287,-6.135070,-0.633351,2.832749,9.639954,1.362727,8.075803,-3.841979,3.971101,1.163065,7.543888,-5.963240,-5.869734,2.366489,-7.895475,7.777691,3.679227,-7.701936,-8.004428,1.847548,2.978483,-0.377748,-3.901971,-0.477166,-0.161386,8.023416,8.435788,-6.206880,-0.417728,-0.064492,1.548907,7.766154,1.771992,-2.437092,1.428134,7.710993,-1.095805,-9.348517,2.029844,-2.230227,-4.397382,4.580454,0.047903,9.299615,9.098319,-0.370936,-8.207785,6.528601,-7.661236,0.969519,-3.316106,-9.381429,-6.556412,3.658766,1.122991,9.629266,5.434621,-8.552338,3.172686,-0.064684,5.537057,9.063046,3.949573,9.853570,-9.931268,3.742198,-4.935705,-8.718251,-7.298482,-7.457871,6.740963,7.519978,-4.517575,-3.833130,-0.408672,-2.819089,7.318199,1.765843,4.142215,-4.772215,7.282196,-8.745352,3.569340,5.867941,-7.923777,-9.287736,6.797272,2.711975,1.666624,6.423678,-0.031433,5.160044,4.595239,-6.392194,2.324730,4.579118,6.294186,-1.582271,-9.824796], dtype = "float64")#candidate|16285|(132,)|const|float64
call_16284 = relay.TupleGetItem(func_13256_call(relay.reshape(const_16285.astype('float64'), [2, 6, 11])), 0)
call_16286 = relay.TupleGetItem(func_13258_call(relay.reshape(const_16285.astype('float64'), [2, 6, 11])), 0)
output = relay.Tuple([call_16257,call_16284,const_16285,])
output2 = relay.Tuple([call_16258,call_16286,const_16285,])
func_16292 = relay.Function([], output)
mod['func_16292'] = func_16292
mod = relay.transform.InferType()(mod)
mutated_mod['func_16292'] = func_16292
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16292_call = mutated_mod.get_global_var('func_16292')
call_16293 = func_16292_call()
output = call_16293
func_16294 = relay.Function([], output)
mutated_mod['func_16294'] = func_16294
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13965_call = mod.get_global_var('func_13965')
func_13966_call = mutated_mod.get_global_var('func_13966')
call_16317 = relay.TupleGetItem(func_13965_call(), 0)
call_16318 = relay.TupleGetItem(func_13966_call(), 0)
func_16040_call = mod.get_global_var('func_16040')
func_16042_call = mutated_mod.get_global_var('func_16042')
var_16368 = relay.var("var_16368", dtype = "float64", shape = (2816,))#candidate|16368|(2816,)|var|float64
call_16367 = relay.TupleGetItem(func_16040_call(relay.reshape(var_16368.astype('float64'), [16, 11, 16])), 1)
call_16369 = relay.TupleGetItem(func_16042_call(relay.reshape(var_16368.astype('float64'), [16, 11, 16])), 1)
func_5115_call = mod.get_global_var('func_5115')
func_5117_call = mutated_mod.get_global_var('func_5117')
var_16377 = relay.var("var_16377", dtype = "uint32", shape = ())#candidate|16377|()|var|uint32
call_16376 = relay.TupleGetItem(func_5115_call(relay.reshape(var_16377.astype('uint32'), [])), 0)
call_16378 = relay.TupleGetItem(func_5117_call(relay.reshape(var_16377.astype('uint32'), [])), 0)
output = relay.Tuple([call_16317,call_16367,var_16368,call_16376,var_16377,])
output2 = relay.Tuple([call_16318,call_16369,var_16368,call_16378,var_16377,])
func_16398 = relay.Function([var_16368,var_16377,], output)
mod['func_16398'] = func_16398
mod = relay.transform.InferType()(mod)
var_16399 = relay.var("var_16399", dtype = "float64", shape = (2816,))#candidate|16399|(2816,)|var|float64
var_16400 = relay.var("var_16400", dtype = "uint32", shape = ())#candidate|16400|()|var|uint32
output = func_16398(var_16399,var_16400,)
func_16401 = relay.Function([var_16399,var_16400,], output)
mutated_mod['func_16401'] = func_16401
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15108_call = mod.get_global_var('func_15108')
func_15109_call = mutated_mod.get_global_var('func_15109')
call_16409 = relay.TupleGetItem(func_15108_call(), 0)
call_16410 = relay.TupleGetItem(func_15109_call(), 0)
output = call_16409
output2 = call_16410
func_16415 = relay.Function([], output)
mod['func_16415'] = func_16415
mod = relay.transform.InferType()(mod)
mutated_mod['func_16415'] = func_16415
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16415_call = mutated_mod.get_global_var('func_16415')
call_16416 = func_16415_call()
output = call_16416
func_16417 = relay.Function([], output)
mutated_mod['func_16417'] = func_16417
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13645_call = mod.get_global_var('func_13645')
func_13646_call = mutated_mod.get_global_var('func_13646')
call_16426 = relay.TupleGetItem(func_13645_call(), 0)
call_16427 = relay.TupleGetItem(func_13646_call(), 0)
output = call_16426
output2 = call_16427
func_16445 = relay.Function([], output)
mod['func_16445'] = func_16445
mod = relay.transform.InferType()(mod)
mutated_mod['func_16445'] = func_16445
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16445_call = mutated_mod.get_global_var('func_16445')
call_16446 = func_16445_call()
output = call_16446
func_16447 = relay.Function([], output)
mutated_mod['func_16447'] = func_16447
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15280_call = mod.get_global_var('func_15280')
func_15282_call = mutated_mod.get_global_var('func_15282')
call_16514 = func_15280_call()
call_16515 = func_15280_call()
func_13876_call = mod.get_global_var('func_13876')
func_13879_call = mutated_mod.get_global_var('func_13879')
var_16535 = relay.var("var_16535", dtype = "float32", shape = (540,))#candidate|16535|(540,)|var|float32
call_16534 = relay.TupleGetItem(func_13876_call(relay.reshape(var_16535.astype('float32'), [540,])), 2)
call_16536 = relay.TupleGetItem(func_13879_call(relay.reshape(var_16535.astype('float32'), [540,])), 2)
func_14308_call = mod.get_global_var('func_14308')
func_14310_call = mutated_mod.get_global_var('func_14310')
call_16544 = relay.TupleGetItem(func_14308_call(), 0)
call_16545 = relay.TupleGetItem(func_14310_call(), 0)
func_12105_call = mod.get_global_var('func_12105')
func_12110_call = mutated_mod.get_global_var('func_12110')
const_16553 = relay.const([1,9,-2,-9,3,9,-7,-3,5,7,-3,-7,-7,-10,-8,-3,5,-9,4,-5,7,-5,7,9,6,-6,-2,-3,7,-3,-8,-6,-6,-9,4,-7,6,-7,2,6,3,-8,-6,-5,-6,-10,3,-5,-10,1,-8,4,2,6,-9,-3,-6,-9,-2,7,-1,2,2,4,4,5,4,8,3,2,-8,-6,8,9,8,-9,1,-4,1,-5,3,-8,1,5,-10,6,5,-4,-7,-2,9,3,-3,2,-5,10,9,7,2,4,2,-1,3,-10,6,-7,-3,4,-9,9,-7,4,-7,-8,6,2,-3,4,6,-8,6,-9,8,-5,2,-1,-3,7,-7,-8,6,-10,2,-6,-8,1,2,2,-3,-6,-3,6,-1,7,-5,-2,6,9,-6,4,-1,-7,-5,2,-10,-5,-5,-10,-3,8,-1,-8,-10,2,-5,-9,3,1,7,-6,-4,-9,-1,7,5,1,-6,2,9,2,-2,10,7,3,-5,-2,-3,7,-9,9,2,1,-10,-3,-8,-1,-6,-6,-2,-10,2,-7,-2,-9,1,-6,-8,10,-9,-5,10,7,-6,-10,4,5,-1,-10,-7,5,-5,-2,9,10,-6,4,10,-3,-6,3,2,-7,2,-7,6,-8,4,-3,1,10,-8,-5,-8,3,1,6,-7,8,10,-8,-9,7,-6,8,-6,7,7,-10,-10,10,2,5,-1,-9,-10,9,-3,5,-9,-7,5,8,-5,6,-3,7,4,-7,6,-10,-2,8,-5,5,7,-10,-7,2,-7,9,7,-9,9,8,1,2,6,9,2,-7,5,1,6,-3,-2,-6,8,9,-1,-3,-6,-6,-4,4,-10,-6,8,6,-1,-8,-3,3,8,-1,1,-1,-8,9,-3,-9,-4,9,-2,-6,8,-7,8,4,-2,-7,8,9,-9,9,1,-7,5,-7,-1,-10,-8,-9,5,-4,-8,-1,1,2,8,1,9,4,-2,-1,-7,3,7,2,3,2,-7,8,3,-7,1,-10,-6,4,-9,-4,-7,-2,6,10,-9,3,-3,5,10,7,-2,2,3,-9,-1,9,-9,-4,-4,-6,-5,1,9,4,-10,1,-9,-3,8,-5,4,-9,-4,7,5,10,-2,10,7,-3,4,-2,-6,5,4,5,5,-10,-4,6,-10,-1,-5,6,-6,2,4,3,6,5,10,-9,-1,4,6,9,4,8,3,-5,4,9,1,7,-1,-9,-2,6,9,-3,9,1,-1,5,5,-5,9,-7,5,8,-6,-7,-7,-4,-2,-1,8,-4,-3,5,9,6,-3,8,9,-3,5,3,-10,10,5,-1,-3,2,-4,-3,8,-2,-4,-8,-8,-8,-9,-7,-10,-3,6,8,10,5,-8,8,-2,6,3,-1,-4,-4,-1,-6,-5,6,2,3,5,-6,8,10,6,-6,-1,-10,3,2,2,-5,-4,10,-6,-9,-1,-5,-1,-7,-2,-8,7,9,-9,-5,6,9,4,7,-10,-2,-3,10,-3,-5,-9,7,-10,-7,5,1,4,3,-9,10,9,2,3,8,-8,-1,5,-2,-4,5,1,-3,7,-6,8,-10,10,-3,-6,8,-3,1,-7,-4,-2,-10,-8,-1,-1,-3,-3,-10,-7,-5,-3,6,-10,-5,-10,7,1,-6,-2,-3,-1,6,1,6,-8,-10,-4,6,-5,-2,-1,8,8,-10,-8,5,-9,-3,6,8,-2,4,7,1,-2,-9,-4,4,9,-2,7,8,10,-8,-3,-2,-7,3,8,-5,7,-3,1,2,-3,8,-4,10,10,-4,-4,-9,5,-2,4,-3,-3,3,-8,-3,9,-3,-10,1,-10,-2,-3,3,3,-1,7,9,2,4,-6,3,10,10,-10,9,-6,-4,4,-7,5,3,3,9,-3,-7,2,4,-7,-4,-5,-9,-6,2,-10,-4,-8,-4,10,-8,8,1,7,-6,2,-5,4,10,5,-9,-10,8,1,-8,-7,5,-4,-9,-4,9,-6,-4,6,-10,3,-8,4,8,-9,-10,3,-6,-2,9,-10,3,-3,-8,-1,2,8,7,-5,1,3,2,7,-4,3,-6,-4,-10,-5,7,-7,-10,-8,-10,1,-9,-3,2,-9,6,2,6,2,-2,-6,-3,-10,9,9,5,9,6,-6,-1,-5,-8,10,2,4,8,-6,3,3,4,-1,4,2,3,10,-3,-10,1,-9,-1,10,-2,-10,2,9,7,-6,10,-3,-6,-7,-8,-3,9,6,2,-9,2,-1,3,10,-10,1,4,4,-6,10,10,-5,-5,10,4,-6,-9,3,-7,-1,9,6,7,5,1,-9,1,1,-2,-7,-10,-5,8,-8,10,1,-3,-5,4,-6,-9,7,9,-10,-9,-9,8,8,3,2,-9,-5,7,-5,-3,-8,-5,2,3,5,9,-2,10,-6,8,-6,-2,-9,2,1,-6,6,2,-7,2,-8,6,9,-2,6,-4,8,3,4,-3,1,-2,3,8,10,2,2,-9,-3,-7,-2,-3,-6,8,-4,-5,-2,-3,-4,5,-3,-3,4,-8,-5,-9,-8,7,-1,-4,-8,3,7,-5,8,-4,-8,8,10,-10,-4,2,-3,6,6,2,-10,-5,10,-7,-1,-1,-7,-10,6,-10,1,2,10,2,7,-9,-7,-3,4,7,-10,-4,-9,2,6,-6,5,-3,-6,-1,8,-2,-4,-4,-5,-4,1,-2,4,-6,7,9,9,-6,-8,-8,9,-3,-4,-3,-10,-4,7,-9,-9,1,-6,7,-2,-8,10,-7,5,3,-7,-10,3,7,-9,1,3,3,2,-5,-3,-5,1,3,3,7,2,6,1,-7,10,-8,2,2,-1,8,-10,-6,-8,6,7,-1,1,4,9,-2,-9,-3,4,-5,-2,1,-8,4,-8,-7,-6,-1,4,-10,-7,5,5,-7,3,5,4,9,5,-10,-6,7,3,-10,5,3,2,-10,-6,-5,-8,6,6,-6,1,-5,2,10,10,-4,9,1,-7,-8,7,-4,6,10,7,5,1,6,10,9,-5,-8,-4,8,9,4,1,-2,-8,-9,8,3,-3,-3,5,6,-8,-8,3,-2,2,-8,-4,10,-3,-6,-2,-10,-8,-10,6,-6,-10,5,-10,4,2,7,-2,-7,5,-6,2,3,-1,-4,-9,-9,7,-2,2,-1,10,10,6,-7,-1,-9,10,-3,-5,8,-7,2,-3,-1,2,1,3,-2,-9,7,5,-4,-7,8,4,-5,4,-5,4,4,-1,8,6,-10,-10,-6,-4,-1,-7,-3,4,-10,-9,-7,-4,-1,-6,6,8,9,-4,2,-5,-10,-2,3,-5,4,9,-7,4,7,-6,2,-8,9,-5,-1,5,-5,6,-3,-1,5,10,-5,1,-6,3,-8,-10,7,1,10,-1,1], dtype = "int8")#candidate|16553|(1260,)|const|int8
var_16554 = relay.var("var_16554", dtype = "float64", shape = (40,))#candidate|16554|(40,)|var|float64
var_16555 = relay.var("var_16555", dtype = "float32", shape = (220,))#candidate|16555|(220,)|var|float32
var_16556 = relay.var("var_16556", dtype = "uint64", shape = (1320, 1))#candidate|16556|(1320, 1)|var|uint64
call_16552 = relay.TupleGetItem(func_12105_call(relay.reshape(const_16553.astype('int8'), [1260,]), relay.reshape(var_16554.astype('float64'), [40,]), relay.reshape(var_16555.astype('float32'), [220,]), relay.reshape(var_16556.astype('uint64'), [1320,]), ), 2)
call_16557 = relay.TupleGetItem(func_12110_call(relay.reshape(const_16553.astype('int8'), [1260,]), relay.reshape(var_16554.astype('float64'), [40,]), relay.reshape(var_16555.astype('float32'), [220,]), relay.reshape(var_16556.astype('uint64'), [1320,]), ), 2)
output = relay.Tuple([call_16514,call_16534,var_16535,call_16544,call_16552,const_16553,var_16554,var_16555,var_16556,])
output2 = relay.Tuple([call_16515,call_16536,var_16535,call_16545,call_16557,const_16553,var_16554,var_16555,var_16556,])
func_16567 = relay.Function([var_16535,var_16554,var_16555,var_16556,], output)
mod['func_16567'] = func_16567
mod = relay.transform.InferType()(mod)
mutated_mod['func_16567'] = func_16567
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16567_call = mutated_mod.get_global_var('func_16567')
var_16569 = relay.var("var_16569", dtype = "float32", shape = (540,))#candidate|16569|(540,)|var|float32
var_16570 = relay.var("var_16570", dtype = "float64", shape = (40,))#candidate|16570|(40,)|var|float64
var_16571 = relay.var("var_16571", dtype = "float32", shape = (220,))#candidate|16571|(220,)|var|float32
var_16572 = relay.var("var_16572", dtype = "uint64", shape = (1320, 1))#candidate|16572|(1320, 1)|var|uint64
call_16568 = func_16567_call(var_16569,var_16570,var_16571,var_16572,)
output = call_16568
func_16573 = relay.Function([var_16569,var_16570,var_16571,var_16572,], output)
mutated_mod['func_16573'] = func_16573
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13726_call = mod.get_global_var('func_13726')
func_13727_call = mutated_mod.get_global_var('func_13727')
call_16587 = relay.TupleGetItem(func_13726_call(), 2)
call_16588 = relay.TupleGetItem(func_13727_call(), 2)
func_13412_call = mod.get_global_var('func_13412')
func_13416_call = mutated_mod.get_global_var('func_13416')
var_16605 = relay.var("var_16605", dtype = "float32", shape = (264,))#candidate|16605|(264,)|var|float32
var_16606 = relay.var("var_16606", dtype = "int64", shape = (448,))#candidate|16606|(448,)|var|int64
call_16604 = relay.TupleGetItem(func_13412_call(relay.reshape(var_16605.astype('float32'), [132, 2]), relay.reshape(var_16606.astype('int64'), [8, 56]), ), 1)
call_16607 = relay.TupleGetItem(func_13416_call(relay.reshape(var_16605.astype('float32'), [132, 2]), relay.reshape(var_16606.astype('int64'), [8, 56]), ), 1)
output = relay.Tuple([call_16587,call_16604,var_16605,var_16606,])
output2 = relay.Tuple([call_16588,call_16607,var_16605,var_16606,])
func_16608 = relay.Function([var_16605,var_16606,], output)
mod['func_16608'] = func_16608
mod = relay.transform.InferType()(mod)
mutated_mod['func_16608'] = func_16608
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16608_call = mutated_mod.get_global_var('func_16608')
var_16610 = relay.var("var_16610", dtype = "float32", shape = (264,))#candidate|16610|(264,)|var|float32
var_16611 = relay.var("var_16611", dtype = "int64", shape = (448,))#candidate|16611|(448,)|var|int64
call_16609 = func_16608_call(var_16610,var_16611,)
output = call_16609
func_16612 = relay.Function([var_16610,var_16611,], output)
mutated_mod['func_16612'] = func_16612
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14445_call = mod.get_global_var('func_14445')
func_14446_call = mutated_mod.get_global_var('func_14446')
call_16651 = relay.TupleGetItem(func_14445_call(), 2)
call_16652 = relay.TupleGetItem(func_14446_call(), 2)
output = call_16651
output2 = call_16652
func_16689 = relay.Function([], output)
mod['func_16689'] = func_16689
mod = relay.transform.InferType()(mod)
mutated_mod['func_16689'] = func_16689
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16689_call = mutated_mod.get_global_var('func_16689')
call_16690 = func_16689_call()
output = call_16690
func_16691 = relay.Function([], output)
mutated_mod['func_16691'] = func_16691
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13582_call = mod.get_global_var('func_13582')
func_13583_call = mutated_mod.get_global_var('func_13583')
call_16740 = relay.TupleGetItem(func_13582_call(), 0)
call_16741 = relay.TupleGetItem(func_13583_call(), 0)
func_13412_call = mod.get_global_var('func_13412')
func_13416_call = mutated_mod.get_global_var('func_13416')
const_16752 = relay.const([-5.581964,-7.769072,-3.042389,6.234522,-2.713569,8.478964,-3.218768,-8.690468,-8.784132,2.200427,-0.723799,-6.381663,-4.101285,-2.319567,-1.973080,-4.430264,2.356275,4.341319,-8.165755,-2.953822,-0.762199,-2.806551,3.859209,5.692177,-7.053443,3.686308,-4.987695,-0.200206,1.052703,-4.519437,5.384806,7.124457,2.655971,-6.812585,4.027601,4.321660,-8.684708,-6.674674,-5.150508,2.779786,2.966661,-4.842540,4.234658,-6.042704,4.733441,-0.767094,6.232187,0.779129,-7.090392,-2.081542,8.587275,-5.052795,-7.959332,9.333370,-6.054368,1.352561,3.365179,4.589456,4.940532,4.067822,-8.895152,1.019436,9.050745,-1.890693,-7.676318,-0.646228,-0.849483,6.965894,1.323782,-5.896426,-5.154101,2.643682,1.655025,-8.727945,5.212496,2.200829,5.643732,4.565004,-4.945076,-1.457626,8.874036,-7.429276,0.215312,-2.054053,-8.585473,-7.156811,-6.252041,-8.669252,-3.400987,-7.542787,-5.937465,5.888728,-9.883090,8.479440,0.399834,1.060088,-0.538789,-3.072632,-8.277255,-4.016205,8.038918,9.000497,0.560801,9.845654,-7.856365,6.284313,-0.297408,-6.538433,1.055336,0.665482,1.455127,5.253117,-2.072113,-9.301547,-4.527399,9.096341,3.017305,-9.545651,-0.176145,1.735256,3.426844,2.487025,7.707982,9.758019,8.492141,9.598998,6.915078,-9.802358,7.793269,-9.909006,-5.268671,4.230907,-7.990145,-0.141077,-7.378326,5.099586,-5.858973,5.840555,-4.578741,-3.076192,4.944634,9.997856,1.100161,-5.212837,-4.002633,-4.475170,-5.034782,-0.010980,4.491810,5.237833,-9.036326,-8.364326,3.783651,4.563332,-7.674604,-9.357541,1.407343,-3.558875,1.534118,6.954624,-1.040173,-4.382378,-9.831759,1.991021,7.479044,8.630340,-8.241973,-6.504155,6.941901,1.794455,-9.761802,4.887116,1.532868,-9.436768,-9.579485,-0.292140,4.324343,0.942123,-0.145942,-9.119338,8.372096,0.846659,2.219354,5.290082,8.379111,-9.739302,-3.676615,-2.688284,2.213968,7.168618,-6.529369,-0.626712,-4.809174,3.661247,8.913497,8.234461,5.236276,-9.582825,-7.499172,7.178749,-4.950832,5.885257,8.999667,4.276744,-8.316841,-6.303853,-7.998382,0.327494,-7.245981,7.698846,-8.493284,-8.926346,-3.090123,-0.673613,8.952794,-0.482991,6.583370,-2.071495,7.831814,9.207601,-3.161877,0.648632,0.492776,-0.469202,5.747661,8.669977,-5.382204,-9.256174,-8.706186,2.736188,-5.385170,8.546430,-3.866367,0.662374,4.759980,1.608267,-1.026884,2.627561,3.126745,-9.899977,4.178541,-8.182524,2.395476,-7.477898,7.922775,9.359181,-3.095831,2.562784,7.486666,-5.243889,-2.189916,-8.738927,-2.499095,-4.648433,3.396342,0.301062,-6.263310,-2.410236,-9.678045,2.766863,2.352063,6.603891,2.240026,-4.770917], dtype = "float32")#candidate|16752|(264,)|const|float32
const_16753 = relay.const([[-9],[-7],[-6],[-10],[3],[3],[-7],[-8],[6],[-5],[-4],[-9],[2],[7],[-2],[-5],[3],[-9],[-6],[-3],[4],[-9],[-1],[-2],[-5],[-1],[7],[4],[-5],[-5],[5],[9],[1],[6],[7],[-8],[-9],[2],[6],[-6],[-10],[-7],[-8],[8],[1],[2],[5],[-5],[9],[6],[3],[9],[-1],[-10],[2],[7],[5],[-10],[-9],[8],[-2],[-8],[-4],[-3],[-4],[-1],[3],[7],[-8],[2],[-4],[-3],[-6],[-2],[9],[-5],[-10],[8],[-5],[7],[2],[-4],[-7],[-10],[9],[6],[-10],[2],[1],[-1],[2],[3],[-8],[-6],[-4],[4],[-2],[-10],[1],[-3],[-1],[-4],[7],[8],[-8],[10],[4],[3],[-4],[9],[-1],[-5],[-1],[-1],[6],[-3],[-2],[-9],[2],[9],[-6],[-3],[-2],[-6],[-5],[-6],[8],[-1],[-8],[-1],[6],[-1],[-2],[-9],[8],[8],[7],[-8],[-6],[-7],[9],[-9],[-7],[-6],[-3],[-9],[-3],[-9],[-1],[-1],[6],[-6],[-9],[-2],[-9],[7],[-4],[-7],[-9],[6],[-1],[2],[5],[9],[10],[8],[-7],[9],[-7],[2],[1],[5],[8],[-6],[6],[8],[7],[1],[1],[-10],[2],[-7],[2],[-7],[-10],[-6],[10],[6],[-3],[4],[4],[-7],[4],[-3],[-2],[6],[-2],[-2],[-10],[3],[8],[10],[-3],[6],[1],[-5],[4],[4],[-4],[10],[9],[-9],[-8],[5],[-8],[7],[10],[-3],[-8],[-8],[9],[-1],[-9],[-10],[1],[10],[-8],[1],[8],[6],[-6],[1],[4],[10],[-3],[8],[6],[-4],[4],[10],[7],[-5],[9],[-1],[-4],[4],[-1],[10],[8],[-5],[10],[2],[5],[-3],[-1],[-4],[6],[-3],[7],[-1],[-2],[5],[-9],[7],[6],[-8],[-7],[4],[-6],[1],[-3],[6],[-6],[4],[5],[-8],[-10],[10],[-7],[7],[-3],[2],[3],[2],[-5],[9],[-9],[9],[5],[1],[-9],[-9],[-2],[-10],[-8],[-2],[2],[-10],[2],[-6],[-6],[6],[1],[-1],[9],[8],[-10],[8],[-8],[1],[-5],[-6],[9],[-4],[8],[7],[-7],[9],[8],[-6],[-1],[4],[-1],[-3],[9],[4],[9],[3],[-6],[8],[-10],[-9],[-7],[7],[-10],[10],[-7],[-5],[7],[9],[4],[-3],[3],[-10],[4],[-4],[10],[-3],[6],[2],[-3],[9],[9],[8],[6],[3],[1],[2],[4],[5],[-7],[-2],[4],[5],[5],[8],[-2],[-8],[3],[-6],[-5],[10],[6],[2],[-3],[8],[5],[8],[-7],[-9],[-10],[2],[4],[-2],[8],[-9],[-10],[-1],[-10],[-8],[9],[4],[8],[-3],[-4],[-7],[1],[-8],[-9],[-5],[2],[-2],[-2],[1],[-5],[4],[7],[-9],[-9],[9],[-7],[2],[8],[-7],[4],[-6],[6],[1],[10],[-10],[2],[-10],[-6],[-3],[-1],[2],[1],[-8],[-6],[7],[-6],[8],[-10],[2],[2],[-4],[9],[-5],[-3],[10],[3],[4],[6],[2],[-8],[3],[2],[8]], dtype = "int64")#candidate|16753|(448, 1)|const|int64
call_16751 = relay.TupleGetItem(func_13412_call(relay.reshape(const_16752.astype('float32'), [132, 2]), relay.reshape(const_16753.astype('int64'), [8, 56]), ), 2)
call_16754 = relay.TupleGetItem(func_13416_call(relay.reshape(const_16752.astype('float32'), [132, 2]), relay.reshape(const_16753.astype('int64'), [8, 56]), ), 2)
var_16761 = relay.var("var_16761", dtype = "float32", shape = (132, 2))#candidate|16761|(132, 2)|var|float32
bop_16762 = relay.less_equal(call_16751.astype('bool'), relay.reshape(var_16761.astype('bool'), relay.shape_of(call_16751))) # shape=(132, 2)
bop_16765 = relay.less_equal(call_16754.astype('bool'), relay.reshape(var_16761.astype('bool'), relay.shape_of(call_16754))) # shape=(132, 2)
bop_16769 = relay.divide(var_16761.astype('float32'), relay.reshape(call_16751.astype('float32'), relay.shape_of(var_16761))) # shape=(132, 2)
bop_16772 = relay.divide(var_16761.astype('float32'), relay.reshape(call_16754.astype('float32'), relay.shape_of(var_16761))) # shape=(132, 2)
output = relay.Tuple([call_16740,const_16752,const_16753,bop_16762,bop_16769,])
output2 = relay.Tuple([call_16741,const_16752,const_16753,bop_16765,bop_16772,])
func_16789 = relay.Function([var_16761,], output)
mod['func_16789'] = func_16789
mod = relay.transform.InferType()(mod)
var_16790 = relay.var("var_16790", dtype = "float32", shape = (132, 2))#candidate|16790|(132, 2)|var|float32
output = func_16789(var_16790)
func_16791 = relay.Function([var_16790], output)
mutated_mod['func_16791'] = func_16791
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16689_call = mod.get_global_var('func_16689')
func_16691_call = mutated_mod.get_global_var('func_16691')
call_16808 = func_16689_call()
call_16809 = func_16689_call()
var_16810 = relay.var("var_16810", dtype = "uint16", shape = (2, 600))#candidate|16810|(2, 600)|var|uint16
bop_16811 = relay.floor_divide(call_16808.astype('float64'), relay.reshape(var_16810.astype('float64'), relay.shape_of(call_16808))) # shape=(2, 600)
bop_16814 = relay.floor_divide(call_16809.astype('float64'), relay.reshape(var_16810.astype('float64'), relay.shape_of(call_16809))) # shape=(2, 600)
bop_16817 = relay.not_equal(call_16808.astype('bool'), relay.reshape(var_16810.astype('bool'), relay.shape_of(call_16808))) # shape=(2, 600)
bop_16820 = relay.not_equal(call_16809.astype('bool'), relay.reshape(var_16810.astype('bool'), relay.shape_of(call_16809))) # shape=(2, 600)
func_15053_call = mod.get_global_var('func_15053')
func_15059_call = mutated_mod.get_global_var('func_15059')
var_16824 = relay.var("var_16824", dtype = "float32", shape = (264,))#candidate|16824|(264,)|var|float32
const_16825 = relay.const([-5,4,10,-10,1,4,6,4,-2,-4,3,9,5,3,2,-9,-8,9,-3,7,-10,5,-3,-1,-3,3,-2,6,-8,-1,2,9,3,7,9,-1,5,5,5,4,-1,-6,9,10,-2,10,-1,3,9,9,4,-4,-5,8,5,10,10,8,-9,-7,-1,6,-5,5,8,9,3,-2,4,-10,5,6,-5,5,7,8,10,-10,-2,-7,1,6,-3,4,-10,10,-2,1,3,5,9,-9,-5,1,6,-2,8,-2,-6,-10,-1,-4,-7,2,10,-1,9,7,1,-5,-10,5,-5,-8,-3,1,-7,9,-9,-5,8,-9,5,5,6,2,-9,3,-4,-8,9,3,4,1,2,-4,1,-1,1,-2,-8,-4,-1,-10,10,-2,-7,7,6,3,-4,-2,2,1,1,-2,-8,-3,-5,-4,3,4,-10,9,10,7,1,-1,5,4,-7,-3,5,6,3,5,-3,-3,-1,-2,-4,-7,10,-6,1,-1,8,-5,-3,3,8,-9,-6,-7,-5,-9,10,6,5,-7,3,5,5,6,-1,-4,-6,4,-5,10,10,1,-5,-1,8,-7,7,4,-3,10,9,7,-6,7,1,-3,7,2,10,2,-3,-1,-2,4,7,-3,9,4,-10,9,10,-2,-6,1,-10,-6,-4,3,5,-3,-3,-1,-8,-8,-7,8,8,6,-6,2,10,9,6,-1,-9,-5,3,-7,-10,9,-1,-7,-9,-5,-10,1,4,5,1,-2,2,-5,3,6,-8,-3,4,-9,2,7,10,1,9,-5,10,3,7,9,-1,-5,9,-7,7,5,-10,3,-4,4,-8,2,-8,-2,-4,-5,7,1,8,-1,3,-6,10,-3,-4,8,5,2,6,6,-8,-2,-1,-10,-2,-3,7,-10,-1,-1,-9,6,10,5,5,-3,-2,-7,9,-1,-6,-6,6,-2,-8,-1,-4,8,7,10,-5,-7,10,-10,-1,8,5,-2,1,-7,9,-5,-5,8,8,-7,3,-10,8,-9,-10,6,-2,-6,4,-3,1,7,3,-1,-5,4,4,8,3,-1,-6,-8,-7,5,-8,-4,6,-7,7,2,8,-10,1,4,-7,6,-2,-4,-1,-10,-7,9,6,-4,6,6,3,6,-4,-7,3,-4,10,-4,9,1,8,1,6,10,-3,-5,4,10,2,-9,-3,-10,3,5,9,7,-7,-5], dtype = "int64")#candidate|16825|(448,)|const|int64
var_16826 = relay.var("var_16826", dtype = "int8", shape = (1260,))#candidate|16826|(1260,)|var|int8
var_16827 = relay.var("var_16827", dtype = "uint64", shape = (1320,))#candidate|16827|(1320,)|var|uint64
call_16823 = relay.TupleGetItem(func_15053_call(relay.reshape(var_16824.astype('float32'), [264,]), relay.reshape(const_16825.astype('int64'), [224, 2]), relay.reshape(var_16826.astype('int8'), [1260,]), relay.reshape(var_16827.astype('uint64'), [1320,]), ), 5)
call_16828 = relay.TupleGetItem(func_15059_call(relay.reshape(var_16824.astype('float32'), [264,]), relay.reshape(const_16825.astype('int64'), [224, 2]), relay.reshape(var_16826.astype('int8'), [1260,]), relay.reshape(var_16827.astype('uint64'), [1320,]), ), 5)
bop_16849 = relay.minimum(var_16826.astype('int8'), call_16823.astype('int8')) # shape=(40, 1260)
bop_16852 = relay.minimum(var_16826.astype('int8'), call_16828.astype('int8')) # shape=(40, 1260)
func_13256_call = mod.get_global_var('func_13256')
func_13258_call = mutated_mod.get_global_var('func_13258')
var_16876 = relay.var("var_16876", dtype = "float64", shape = (132,))#candidate|16876|(132,)|var|float64
call_16875 = relay.TupleGetItem(func_13256_call(relay.reshape(var_16876.astype('float64'), [2, 6, 11])), 0)
call_16877 = relay.TupleGetItem(func_13258_call(relay.reshape(var_16876.astype('float64'), [2, 6, 11])), 0)
output = relay.Tuple([bop_16811,bop_16817,var_16824,const_16825,var_16827,bop_16849,call_16875,var_16876,])
output2 = relay.Tuple([bop_16814,bop_16820,var_16824,const_16825,var_16827,bop_16852,call_16877,var_16876,])
func_16882 = relay.Function([var_16810,var_16824,var_16826,var_16827,var_16876,], output)
mod['func_16882'] = func_16882
mod = relay.transform.InferType()(mod)
mutated_mod['func_16882'] = func_16882
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16882_call = mutated_mod.get_global_var('func_16882')
var_16884 = relay.var("var_16884", dtype = "uint16", shape = (2, 600))#candidate|16884|(2, 600)|var|uint16
var_16885 = relay.var("var_16885", dtype = "float32", shape = (264,))#candidate|16885|(264,)|var|float32
var_16886 = relay.var("var_16886", dtype = "int8", shape = (1260,))#candidate|16886|(1260,)|var|int8
var_16887 = relay.var("var_16887", dtype = "uint64", shape = (1320,))#candidate|16887|(1320,)|var|uint64
var_16888 = relay.var("var_16888", dtype = "float64", shape = (132,))#candidate|16888|(132,)|var|float64
call_16883 = func_16882_call(var_16884,var_16885,var_16886,var_16887,var_16888,)
output = call_16883
func_16889 = relay.Function([var_16884,var_16885,var_16886,var_16887,var_16888,], output)
mutated_mod['func_16889'] = func_16889
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12993_call = mod.get_global_var('func_12993')
func_12994_call = mutated_mod.get_global_var('func_12994')
call_16901 = relay.TupleGetItem(func_12993_call(), 1)
call_16902 = relay.TupleGetItem(func_12994_call(), 1)
output = call_16901
output2 = call_16902
func_16930 = relay.Function([], output)
mod['func_16930'] = func_16930
mod = relay.transform.InferType()(mod)
mutated_mod['func_16930'] = func_16930
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16930_call = mutated_mod.get_global_var('func_16930')
call_16931 = func_16930_call()
output = call_16931
func_16932 = relay.Function([], output)
mutated_mod['func_16932'] = func_16932
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14400_call = mod.get_global_var('func_14400')
func_14401_call = mutated_mod.get_global_var('func_14401')
call_16941 = func_14400_call()
call_16942 = func_14400_call()
func_6298_call = mod.get_global_var('func_6298')
func_6303_call = mutated_mod.get_global_var('func_6303')
var_16949 = relay.var("var_16949", dtype = "float32", shape = (150,))#candidate|16949|(150,)|var|float32
const_16950 = relay.const([10,-9,5,9,4,1,-2,-10,3,-7,1,-2,-3,-8,1,-10,-1,7,5,-1,-8,10,1,8,2,-8,-9,7,5,9,-1,8,8,-7,-9,-1,-5,9,-1,-9,-4,9,9,-7,3,2,-7,-5,-4,-7,5,10,-10,-3,7,5,10,5,2,-4,10,-9,6,1,8,-3,-7,-10,-1,10,-6,-9,1,-6,6,7,7,2,-10,1,2,-9,-6,-7,-4,7,4,-8,10,7,7,-5,-10,6,-1,-5,3,-3,5,-10,-9,-10,-4,7,4,3,7,-4,4,-4,8,-7,3,2,2,-6,-8,1,5,-8,-1,8,7,-5,-3,6,-8,2,5,-1,7,-7,6,-7,-7,9,3,7,9,-1,-3,-6,1,4,4,-2,-7,-6,-6,-1,7,2,7,-2,-1,1,-1,5,-6,8,6,-9,-1,-5,7,10,8,-7,-1,-3,3,6,-2,-8,2,6,-7,3,1,5,-6,3,-8,8,9,-4,5,8,3,-6,1,-4,-9,8,-5,-8,-1,2,9,-1,-1,-1,-6,-6,5,5,5,6,-4,-4,7,-9,-2,10,-3,2,-7,-2,3,4,-9,-4,8,-10,4], dtype = "uint16")#candidate|16950|(225,)|const|uint16
const_16951 = relay.const([-7,2,7,5,-4,-6,1,5,-4,-2,10,9,5,2,3,-3,-10,-10,-6,7,-1,10,-10,7,-6,7,4,3,5,-9,1,-9,-8,7,3,5,-8,-7,9,-10,-3,-10,5,6,-9,8,-8,10,-5,9,1,-5,8,5,8,-4,-4,-7,10,-1,-8,-8,8,-2,2,-3,3,2,-10,1,-4,-8,-9,-1,8,-9,-3,-3,-4,-3,6,1,-2,3,2,9,-8,8,1,8,3,6,-4,-6,5,5,5,-3,1,-10,-1,-2,-5,-10,-10,-4,8,9,-8,-10,-4,6,-3,8,-6,-8,5,-10,10,7,-10,5,10,2,10,-2,-9,6,9,5,-10,4,2,-8,-6,4,-3,-6,4,-2,9,1,-2,9,10,-7,-8,-10,9,-3,-10,-2,8,7,-7,-6,-2,-6,3,8,-1,8,7,10,-5,-10,-1,-9,2,1,-4,10,4,-4,3,-2,6,4,9,1,8,-8,-6,8,-10,9,-3,-4,5,4,8,2,10,-7,-9,-3,-10,6,6,5,-2,-4,3,4,3,-6,7,-5,2,-6,-2,8,7,-9,-7,-1,-9,5,-10,-10,8,4,-1,-2,2,-4,6,6,5,6,-10,-4,-1,-10,10,6,5,-5,8,9,-5,4,-6,-5,-8,6,10,-8,9,-6,8,-6,1,-9,-1,10,-5,7,9,-4,-5,-6,10,-9,-9,-7,6,-2,-7,9,1,-3,-6,-8,4,-1,-2,-7,-10,-9,-1,8,2,-8,10,6,-7,-8,9,9,5,4,8,10,-8,-6,7,-10,-3,7,-6,-5,-2,-9,8,-6,-7,-2,4,2,1,4,-10,-7,3,-6,-7,-1,3,-1,7,4,10,10,8,-7,-7,-6,-5,2,9,6,-1,6,-8,-5,-6,10,6,1,1,-2,-1,9,-3,4,9,1,-9,-3,6,2,8,-10,-4,-6,-3,7,-7,1,-7,6,-7,5,-4,2,8,-5,-8,9,-8,-8,5,6,-4,-4,2,-7,6,4,2,-1,-10,7,3,-9,-4,3,-6,1,-4,1,4,-4,1,10,1,-8,-10,-8,-2,4,-6,3,-4,2,-9,5,-10,-6,6,-8,9,-10,10,10,5,-6,-10,2,5,-3,4,10,6,7,-1,-1,-1,-9,-8,-3,-2,-3,1,-6,9,3,-9,9,8,-9,3,1,-10,-6,-9,1,-9,-6,10,-7,3,-2,4,8,-9,2,7,-7,2,-5,-6,4,3,-8,-4,-1,6,9,-7,9,-4,-10,-4,7,-4,-9,-1,6,5,-6,-8,7,-2,-1,5,-9,-2,-9,-7,4,-1,2,10,-5,-9,-5,9,10,-10,4,-2,4,1,-2,-4,-10,1,-8,-9,5,5,4,4,7,6,9,4,1,1,-4,10,-9,-5,2,-9,1,-9,-9,-10,8,8,1,3,7,-5,-6,-4,-6,1,2,-6,-5,9,-7,2,2,-5,4,-7,1,-2,9,-3,7,-4,3,4,-3,5,10,7,9,-5,9,6,3,6,-5,8,2,-1,-10,-6,7,-4,9,9,3,-5,-7,2,-8,-4,9,5,4,8,-2,-6,6,-6,-1,-6,-2,-7,-9,-2,7,-2,-10,8,2,5,-10,4,10,2,-6,8,-7,-10,-3,-5,-8,5,-3,-1,8,-10,-8,-6,-4,-2,7,2,-2,-2,3,-5,6,1,4,-6,-2,3,-3,-8,7,1,9,-8,4,-8,-7,9,5,-3,-6,3,9,7,5,3,7,-6,7,-9,-1,-9,-2,-2,-2,5,-7,-5,-6,-10,-10,-3,-7,3,-10,-7,1,-9,-4,-9,-7,-4,5,-3,-4,10,-6,-2,1,-8,-10,-1,-9,-4,-3,-1,7,7,7,-1,-2,6,5,2,-5,-8,-5,6,9,-1,2,5,9,1,3,-8,6,-5,-4,-8,9,-4,5,10,-9,-8,-5,2,8,-10,9,6,-6,8,-7,-10,2,-3,-5,3,-6,-7,-6,2,4,5,-4,1,-1,3,-7,4,-9,8,-10,10,-2,6,7,3,2,7,8,-7,8,5,-2,-7,-8,5,-6,3,-1,9,6,9,10,7,5,5,5,9,10,10,-10,5,9,5,8,-10,-6,4,5,1,7,-3,7,2,5,7,-7,1,-2,-10,10,7,-8,-1,-4,3,10,6,8,-5,9,8,6,-6,8,1,3,-6,-8,-4,-1,6,2,9,9,3,-7,6,4,2,-7,10,8,10,4,10,10,-5,9,4,-7,8,2,7,-5,6,9,-1,-3,-5,-5,-2,-1,1,10,-8,4,1,1,2,7,9,7,5,10,-8,-6,-2,-7,7,-10,-4,-2,-2,5,10,-3,9,8,1,7,5,-10,-10,-1,4,-5,-6,5,1,-4,-3,-1,-9,10,9,1,-9,-2,-8,8,-2,10,10,-8,7,-2,-8,-5,-2,-9,10,-4,1,-10,6,-2,-10,8,8,-1,-7,5,7,-2,-5,-9,-1,6,8,-2,5,-5,-6,7,1,1,2,-5,6,-8,-10,-5,-10,4,10,-4,-2,2,-4,-4,-4,4,10,4,7,-6,9,-8,4,-8,-10,9,-3,-9,-9,-3,7,10,-9,3,6,-4,3,-5,6,1,-6,-5,3,-8,-7,5,10,-1,-10,6,-6,-3,4,5,-9,-3,9,6,2,-4,4,-2,7,-5,8,4,-4,2,-5,8,-3,1,-9,-4,10,1,-9,10,6,4,-1,-9,-7,4,8,-10,-1,5,-7,-4,-8,2,-7,5,10,-1,-2,-7,-3,-3,-1,2,-3,3,-7,-8,1,6,4,5,-3,-4,-9,3,10,-3,-8,-4,-3,10,3,6,-10,5,-4,-8,9,1,3,-9,10,5,-4,-7,-3,6,-7,-3,5,-2,8,-5,2,-6,9,-7,5,5,8,-8,-10,-10,-9,7,10,-4,-7,-9,4,-3,9,2,-1,-3,10,1,-8,-9,5,2,5,-8,-4,1,-10,-2,4,3,10,4,9,-2,-10,3,-6], dtype = "uint16")#candidate|16951|(1125,)|const|uint16
call_16948 = relay.TupleGetItem(func_6298_call(relay.reshape(var_16949.astype('float32'), [1, 15, 10]), relay.reshape(const_16950.astype('uint16'), [1, 225]), relay.reshape(const_16951.astype('uint16'), [5, 225]), ), 2)
call_16952 = relay.TupleGetItem(func_6303_call(relay.reshape(var_16949.astype('float32'), [1, 15, 10]), relay.reshape(const_16950.astype('uint16'), [1, 225]), relay.reshape(const_16951.astype('uint16'), [5, 225]), ), 2)
bop_16956 = relay.floor_divide(call_16948.astype('float64'), relay.reshape(var_16949.astype('float64'), relay.shape_of(call_16948))) # shape=(1, 15, 10)
bop_16959 = relay.floor_divide(call_16952.astype('float64'), relay.reshape(var_16949.astype('float64'), relay.shape_of(call_16952))) # shape=(1, 15, 10)
func_3702_call = mod.get_global_var('func_3702')
func_3707_call = mutated_mod.get_global_var('func_3707')
const_16965 = relay.const([9,-10,-10,-8,-7,5,10,-4,5,10,-2,-5,9,-10,1,-9,-5,-7,-1,4,-1,-7,-8,-2,4,9,5,10,-1,8,-4,-10,-5,3,-1,-4,-7,-5,-4,10,-1,6,2,-1,4,2,-6,4,1,-7,-6,9,4,10,3,7,-8,1,7,-2,-3,9,-9,1,2,-4,-1,-2,9,6,-2,7,6,-10,1,-3,6,-6,-7,-7,-8,-7,-6,-5,-3,-6,-4,6,10,-2,-10,9,-9,3,1,4,2,8,4,-2,6,3,2,7,-9,-5,6,-7,9,10,1,-1,7,1,-5,-8,3,-9,3,9,7,-1,9,7,-7,8,-10,8,-8,-9,-6,-4,-8,-5,10,-3,7,-9,9,4,2,-3,-3,-2,-4,4,7,8,-2,8,-7,9,4,-2,-8,10,-10,-4,6,4,6,7,-7,-1,-7,10,-10,10,9,-9,-8,-6,-2,1,-6,-7,2,-8,-10,-5,5,-1,-6,-9,4,-1,6,1,10,5,5,-10,7,-6,-6,2,-8,-6,-7,-9,-2,-3,2,6,6,-1,3,-9,-9,7,-8,7,-3,10,10,1,4,2,-8,9,10,-6,-1,-5,-2,8,-1,-7,9,-6,-9,-5,-1,-10,-3,-2,8,8,-6,2,3,-7,-6,-1,-2,-6,-4,-5,-7,-3,-5,-5,-4,4,6,-6,-5,-7,9,-6,5,-5,4,-5,6,-3,-10,4,3,-3,-4,-2,-4,-10,7,8,-9,-2,-3,-3,-2,10,9,7,3,-3,-1,-8,1,9,-3,9,-8,-4,-7,-9,-7,2,-4,8,-9,8,5,4,-3,6,-10,9,-8,-10,-4,-6,10,5,-7,5,5,5,-7,-5,-3,-8,8,2,2,10,3,-7,4,-8,6,-6,-5,8,-1,4,-6,9,-4,9,-5,4,-5,-10,2,9,-9,6,7,10,10,3,8,9,5,10,5,9,-2,8,-6,1,-1,1,-4,5,7,-10,-2,-9,-5,8,-10,1,-5,-7,5,8,6,3,2,-3,-7,-4,-10,-7,-1,-8,-1,4,-9,9,-10,1,8,-7,3,9,-3,-9,7,1,-1,2,7,10,-8,9,7,5,3,8,-4,-5,4,-1,10,-1,-10,-4,9,-2,-4,5,10,-9,-4,8,-5,-4,-5,-10,-6,5,-3,2,3,-9,6,10,-5,-8,5,-6,8,-7,-4,9], dtype = "int64")#candidate|16965|(448,)|const|int64
const_16966 = relay.const([3.113742,-0.148690,5.174106,-7.155515,-9.609440,2.317459,-7.316842,-3.803584,-6.547490,3.215156,-6.156346,-8.654531,1.199623,0.120872,1.745663,-5.244029,-6.225915,-3.530754,-6.718697,-6.376214,8.141820,-3.233932,-0.727271,0.138339,6.040304,-8.969336,7.691434,-4.751789,-8.859451,5.083804,-8.954208,0.402669,-1.560315,-1.928752,-1.852492,-5.101443,-6.330202,-8.113298,0.836311,-5.992264,-2.704909,7.751439,9.941901,0.608465,3.334128,0.403491,-5.729306,-8.680900,-0.091416,-9.669644,8.374775,-6.175823,3.311387,0.941019,5.628054,5.250118,-1.097276,5.944179,-5.335523,3.885472,9.507277,-2.243658,1.398701,4.926548,6.980685,1.633762,-9.499351,2.422722,-4.134280,-4.438858,-2.484236,3.510215,-2.810996,-9.841094,3.056174,-4.794964,-6.882178,6.784941,-4.007034,-7.535221,-2.020519,-5.826588,2.279046,-7.746838,-6.740515,2.356469,-8.589841,8.542143,9.360362,-0.396919,-2.344998,-9.256934,7.530450,-6.526432,-3.339911,0.021063,-3.224404,7.427525,3.887134,1.737439,-6.662170,-7.056470,-8.817810,-3.868847,8.231220,-9.746219,8.629021,2.830659,-2.177315,-2.586353,-0.135332,7.397733,-9.345625,-9.868005,-1.796752,6.870178,3.297678,-4.302479,-2.143358,1.064374,8.731115,4.622385,-0.118184,8.875967,-3.252151,9.390450,6.131450,-8.612867,7.433798,-5.033987,-4.424370,8.375024,4.587036,0.567305,-6.284656,-2.523318,0.514962,-9.565807,-0.367421,-9.194196,-4.204380,6.385376,1.431658,4.181598,-9.853456,-8.895897,6.896704,-8.195279,4.565030,-8.696205,3.190117,4.119767,-4.109116,-2.599571,6.445261,-9.475198,1.802226,-7.379058,5.492942,5.138317,4.673796,-9.639513,1.796268,5.016807,1.835648,-1.939128,-9.643239,5.495141,-7.633487,3.230814,-2.825690,7.166608,2.810105,-6.978309,8.333032,6.982651,-9.429235,3.247906,-1.459478,-1.257118,4.417102,-7.327291,5.909509,-1.574097,-8.511705,3.197762,8.718048,-5.041835,-5.733548,9.065246,-1.062058,-4.436285,6.169446,6.088501,5.567444,8.498953,-1.191975,-8.458654,4.876445,8.215214,1.194936,-7.588341,9.949441,3.902428,-0.050545,3.173224,9.643975,1.534203,-9.310962,1.661983,-3.647813,-6.960393,-4.319704,-7.394056,5.159211,3.202975,7.716495,-1.549928,-5.804726,-5.792540,-5.019501,-3.248855,-8.330502,-1.692668,-0.550291,-7.810188,-2.722008,1.374480,6.517918,-3.832399,-9.641973,4.764367,-5.580342,-8.497282,-5.593068,4.353526,4.417830,-1.719350,3.887071,-6.204828,-0.212502,-4.551151,9.745850,-8.247293,-3.872954,7.284438,-8.067322,-5.908991,-6.696802,-0.375017,4.361662,-3.926741,4.467853,-8.019703,4.691157,-7.306421,0.958100,8.481957,-5.575062,-2.376790,-7.265074,6.855616,-5.312904,9.959175,2.783146,8.953051,5.955466,3.567045,2.647793,5.608326,-2.659801,-1.711546,7.428793,-1.264907,5.477068,-8.729993,-0.557720,5.903298,2.953686,-9.177426,-8.357080,3.721023,0.571233,-4.542453,3.310341,1.531059,2.504965,1.423472,2.010125,-7.618799,-8.177248,5.912084,5.796007,-0.613914,8.728948,7.361293,-1.959432,-9.300138,1.820682,-4.831202], dtype = "float64")#candidate|16966|(300,)|const|float64
var_16967 = relay.var("var_16967", dtype = "float32", shape = (12,))#candidate|16967|(12,)|var|float32
call_16964 = relay.TupleGetItem(func_3702_call(relay.reshape(const_16965.astype('int64'), [14, 16, 2]), relay.reshape(const_16966.astype('float64'), [300,]), relay.reshape(var_16967.astype('float32'), [12,]), relay.reshape(const_16950.astype('uint16'), [25, 9]), ), 2)
call_16968 = relay.TupleGetItem(func_3707_call(relay.reshape(const_16965.astype('int64'), [14, 16, 2]), relay.reshape(const_16966.astype('float64'), [300,]), relay.reshape(var_16967.astype('float32'), [12,]), relay.reshape(const_16950.astype('uint16'), [25, 9]), ), 2)
func_11903_call = mod.get_global_var('func_11903')
func_11907_call = mutated_mod.get_global_var('func_11907')
var_16994 = relay.var("var_16994", dtype = "float32", shape = ())#candidate|16994|()|var|float32
var_16995 = relay.var("var_16995", dtype = "float64", shape = (180, 1))#candidate|16995|(180, 1)|var|float64
const_16996 = relay.const([-5,9,3,-10,7,-1,-7,-7,-3,-4,9,6,7,-6,1,5,4,-1,1,7,-3,9,7,6,10,4,4,-7,-4,-9,10,10,-9,4,4,10,-2,-7,4,8,-5,-5,4,1,3,-2,7,9,-5,-8,4,6,8,4,-9,7,-7,-5,4,-9,-8,-2,-3,3,-3,8,-10,5,10,-1,4,-2,-10,-3,3,-3,-3,7,5,-5,-10,10,-1,-7,6,9,6,2,10,-2,5,5,-10,5,10,-8,5,10,2,-7,5,-10,-9,7,-6,-2,4,-1,10,10,6,-10,-5,-6,-8,-7,9,4,-10,7,1,8,-7,-10,7,-6,-7,3,-7,-10,2,-9,-5,-8,5,-10,7,4,9,10,5,8,-4,-5,-1,-7,-4,-3,1,-5,-9,5,-5,1,-2,-9,-8,-8,-9,5,-9,3,9,2,9,6,-2,-5,9,-2,-8,-9,-7,1,1,-6,-6,-4,4,5,-5,5,-2,-6,-8,-4,-9,-5,2,-2,9,5,-6,-2,-7,6,-8,1,3,2,6,-10,-9,-1,10,-3,-1,6,-9,10,7,-8,-8,4,-6,5,-2,-7,9,-3,-1,-9,7,10,6,-10,5,-8,8,-4,-8,-6,-3,3,-9,2,3,2,7,-5,-3,5,-4,-3,-5,-7,-8,-3,-6,-5,-3,6,-8,-5,4,9,-7,-7,7,3,9,-5,3,-9,8,-5,-1,-6,-1,6,-3,3,1,-10,10,-10,-3,5,7,-6,-8,-6,4,-7,-7,10,-8,-9,-1,-7,4,9,6,-7,7,-8,6,1,-7,5,-1,-3,8,-10,-5,-9,8,-8,1,7,-9,-1,8,5,2,9,-6,6,6,-2,-5,-10,10,-5,-1,9,7,5,1,1,3,-9,-4,-3,-1,3,-8,8,3,7,8,-6,-5,10,-2,-1,3,-3,5,9,-1,-1,-7,4,-2,4,8,-5,-2,3,6,-6,-6,-7,-5,6,-9,2,7,6,1,-1,1,-4,-1,-6,10,7,2,-8,8,-2,2,5,-2,-1,4,-1,-6,-9,-1,5,6,1,3,5,-5,10,-1,-7,7,-7,7,-5,5,1,8,1,-5,-4,-2,-2,5,4,-9,2,-8,9,9,2,10,1,-1,-2,5,-7,-6,-3,2,-9,-10,-1,10,-8,3,-2,-5,-1,-5,3,10,8,10,8,-1,-5,8,1,-7,8,1,5,4,2,-10,9,4,7,-9,6,-2,2,8,-9,-2,-6,-8,9,-6,1,-6,5,10,-4,7,-10,2,10,-5,6,7,-10,-1,-6,10,3,10,3,-2,-2,6,9,-5,-9,-7,8,5,8,9,-4,-3,-4,-7,-6,6,9,9,-10,-6,-5,-4,-8,10,-4,1,-7,-7,1,10,4,-7,-7,-4,1,8,4,8,8,7,1,3,6,1,-3,-7,6,-3,-10,-10,6,8,9,-1,8,-10,-10,6,-3,5,7,-5,6,4,5,-1,-3,1,7,-10,2,3,-2,-5,-6,-3,4,4,7,8,-5,3,7,1,-7,-10,-10,10,2,7,8,2,7,10,5,6,-6,-9,6,-9,-8,2,10,10,-7,-3,-6,-7,-1,8,6,6,-4,6,-5,-5,-2,3,-8,7,9,-2,-2,-1,-7,-9,-3,-6,-9,7,7,-9,10,4,-2,-5,10,-9,8,7,6,-10,-2,6,-9,7,6,7,-5,-3,-2,9,10,6,7,5,7,4,2,-1,4,8,-4,-5,-6,6,-9,-1,5,8,9,9,1,-5,1,5,-6,5,-6,8,9,1,1,10,7,9,-3,2,-10,-6,-7,-8,4,2,4,-3,4,-4,5,-2,-9,-8,9,-6,-9,4,3,-10,5,-6,-3,-3,-2,1,-8,2,4,-2,2,-6,2,8,1,-2,-9,7,-9,9,7,1,-5,-7,-2,5,-8,-4,2,6,9,10,-10,2,-7,-5,4,-2,-10,1,-7,-6,9,5,-4,-5,-3,-3,-3,-4,-9,-7,-4,4,-5,6,3,-6,3,-4,-4,-2,-5,2,1,8,-3,-4,3,1,-5,9,8,-10,9,-8,2,-2,4,-5,-7,6,10,-9,10,-1,6,10,-5,6,4,-9,-3,-3,4,-5,-1,-3,3,-3,3,-5,-2,-6,5,3,6,-6,-2,8,-5,6,-4,-8,-4,-7,3,-7,-6,3,3,-3,-9,-7,-5,8,-8,7,-7,8,-4,-6,8,3,6,-9,4,-9,-8,8,3,-3,-4,4,7,-1,-10,9,2,-4,-8,1,-3,-8,9,4,4,7,-10,-7,5,-10,-7,-3,-1,-9,-9,4,1,3,-10,5,6,1,-5,5,-8,-6,-3,6,-7,-4,5,10,-10,9,-4,3,8,-8,-4,-4,-7,9,-9,-6,10,-7,-8,3,2,7,6,-5,-3,7,7,4,-2,-6,10,9,3,-6,-5,-8,-1,-2,-4,3,-2,-7,-4,5,-7,-6,4,-8,-3,6,5,4,9,-5,7,-2,-10,9,1,-9,4,5,3,3,-10,-6,4,-1,6,-8,5,1,9,1,-4,10,8,-4,-1,-10,7,-3,4,4,1,-4,-1,6,-6,2,9,-8,7,1,10,-8,5,-7,-7,-10,4,7,-8,-5,-1,-4,7,9,-3,-2,10,-9,-3,-4,9,1,6,9,10,-10,-1,3,-6,3,-3,-4,7,9,-2,-10,-7,-4,-8,8,-9,1,3,-9,6,-2,-7,3,-2,3,5,4,-4,-4,-3,2,-3,1,9,-8,-10,-6,-7,-2,-9,-2,10,-6,-6,9,-7,1,-6,-7,-10,9,-5,10,4,-8,9,-9,8,5,8,-3,-9,-4,-7,-9,5,-9,-5,-2,-3,3,-2,2,8,4,-3,10,1,6,-6,-5,7,1,4,-2,-6,8,-5,-8,8,-10,8,5,-5,-7,10,-4,-7,8,8,10,-4,2,9,-4,-1,-1,4,8,9,-2,7,-5,-1,-8,4,5,-8,-7,6,-7,-4,7,4,-9,9,1,5,2,10,5,2,2,-4,9,8,10,-4,-2,-10,-3,-10,7,-4,-1,3,-10,3,-4,-1,-10,1,-3,-5,-7,-5,6,-7,-3,5,5,10,-10,-7,2,9,9,2,-7,8,-3,-4,-2,-3,-2,-9,-4,-2,1,-3,7,5,-4,-9,-3,6,-2,5,1,-9,6,-10,8,-9,1,-4,-3,-4,7,9,2,7,6,-8,-2,2,6,10,-7,-2,2,7,-4,-4,6,-2,1,-2,9,-5,-8,9,-2,9,2,8,-9,1,7,6,-1,4,6,-8,-8,8,-2,4,-9,-3,-6,5,5,-1,-1,10,3,-3,-1,-6,4,9,-2,-1,-5,2,-5,-9,2,5,-4,5,-8,-8,1,-8,-9,-2,9,2,10,-7,10,5,3,5,-2,7,-1,9,-9,9,-5,9,-4,9,-4,9,2,5,-4,5,1,8,-6,-5,5,5,5,-3,4,3,8,-1,5,-6,-4,-7,-2,10,1,3,7,3,1,-1,7,2,-7,6,6,-3,2,7,4,-1,3,10,-1,4,-8,-6,10,-2,10,-2,-9,-9,6,6,3,4,1,-8,6,6,-6,3,-2,-6,3,9,3,-5,-5,-9,-8,6,9,-4,5,-1,4,-10,8,-9,4,-3,7,5,2,-10,-9,2,2,2,-5,10,-6,-6,-8,3,4,-10,7,2,-1,10,1,-7,7,10,-4,-3,-5,-3,3,-5,-6,-9,2,4,6,-3,-7,9,10,8,-2,-4,-8,-9,5,-2,-1,-7,4,4,7,-8,8,8,9,-3,7,-7,6,-9,-2,-5,-2,5,2,-8,7,-3,3,6,-9,4,-8,-2,9,-7,-2,3,3,-2,7,5,-5,-10,2,-2,-7,-9,-9,9,-6,-10,-7,4,1,6,-5,-2,9,-1,-10,-4,-3,-3,-7,2,-9,2,5,9,-4,-4,5,-1,1,-7,-9,9,-7,-4,-7,8,1,3,9,-4,6,-4,-7,7,-9,9,7,-9,2,-1,-2,-4,-10,-10,10,2,3,9,10,-8,-10,6,6,-2,-9,-7,1,-3,-10,-1,-7,8,-8,-10,1,-7,4,10,9,2,4,-8,-3,-9,-3,3,3,8,8,-2,-5,-4,4,-2,-6,10,4,-9,10,9,-8,3,-6,5,-10,-7,-5,7,2,2,-4,8,-4,-4,-4,-10,-5,-6,-6,7,9,3,2,5,9,-2,2,10,6,2,5,4,3,-1,2,-4,-1,-7,7,4,1,-9,-5,-1,-1,3,-3,7,5,-4,7,8,-5,10,-8,7,2,2,-5,10,-4,-3,8,-2,2,-1,-5,9,-5,3,-3,3,-6,-3,-8,8,-4,10,3,-4,-9,3,4,-6,-1,2,-9,9,10,8,-5,-1,-7,10,2,-4,10,4,1,5,-9,6,-4,7,7,1,2,-2,2,1,-7,-2,4,3,6,-9,-4,6,2,-1,9,-2,5,-1,7,10,7,-2,-10,10,2,-2,6,6,9,8,1,-10,5,5,3,7,9,-5,-4,-4,6,-5,-4,-4,-10,3,-4,10,-6,3,-2,3,2,10,-3,-4,-10,5,2,7,2,3,-2,-9,-8,10,-5,-1,1,2,-6,4,5,-10,-9,-7,6,10,3,-8,2,-4,9,3,-9,-3,-9,-10,8,-1,6,1,2,-10,1,-7,-4,-1,8,-4,-8,1,7,4,-3,4,7,-1,-7,3,9,-2,-2,-7,-6,7,-9,1,-2,-1,2,-6,3,7,8,-9,-9,-1,3,-3,-2,-10,9,-7,6,7,5,8,-1,-9,2,-8,-10,-6,-1,-9,9,4,-3,-10,10,9,-9,7,-10,10,6,-5,-1,7,-9,-4,8,-6,-2,-9,4,-2,-5,-4,3,6,-4,-6,-3,-6,1,-1,-2,7,-5,-8,4,-3,-7,3,3,-1,-2,3,-10,-10,-10,8,-9,-6,3,3,-2,-6,5,10,1,-4,-8,10,5,9,-10,7,-5,-4,-7,-6,3,-9], dtype = "int64")#candidate|16996|(1872,)|const|int64
call_16993 = relay.TupleGetItem(func_11903_call(relay.reshape(var_16994.astype('float32'), []), relay.reshape(var_16995.astype('float64'), [180,]), relay.reshape(const_16996.astype('int64'), [1872,]), ), 5)
call_16997 = relay.TupleGetItem(func_11907_call(relay.reshape(var_16994.astype('float32'), []), relay.reshape(var_16995.astype('float64'), [180,]), relay.reshape(const_16996.astype('int64'), [1872,]), ), 5)
func_14268_call = mod.get_global_var('func_14268')
func_14270_call = mutated_mod.get_global_var('func_14270')
call_17001 = relay.TupleGetItem(func_14268_call(), 0)
call_17002 = relay.TupleGetItem(func_14270_call(), 0)
output = relay.Tuple([call_16941,const_16950,const_16951,bop_16956,call_16964,const_16965,const_16966,var_16967,call_16993,var_16994,var_16995,const_16996,call_17001,])
output2 = relay.Tuple([call_16942,const_16950,const_16951,bop_16959,call_16968,const_16965,const_16966,var_16967,call_16997,var_16994,var_16995,const_16996,call_17002,])
func_17023 = relay.Function([var_16949,var_16967,var_16994,var_16995,], output)
mod['func_17023'] = func_17023
mod = relay.transform.InferType()(mod)
mutated_mod['func_17023'] = func_17023
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17023_call = mutated_mod.get_global_var('func_17023')
var_17025 = relay.var("var_17025", dtype = "float32", shape = (150,))#candidate|17025|(150,)|var|float32
var_17026 = relay.var("var_17026", dtype = "float32", shape = (12,))#candidate|17026|(12,)|var|float32
var_17027 = relay.var("var_17027", dtype = "float32", shape = ())#candidate|17027|()|var|float32
var_17028 = relay.var("var_17028", dtype = "float64", shape = (180, 1))#candidate|17028|(180, 1)|var|float64
call_17024 = func_17023_call(var_17025,var_17026,var_17027,var_17028,)
output = call_17024
func_17029 = relay.Function([var_17025,var_17026,var_17027,var_17028,], output)
mutated_mod['func_17029'] = func_17029
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14458_call = mod.get_global_var('func_14458')
func_14460_call = mutated_mod.get_global_var('func_14460')
call_17079 = relay.TupleGetItem(func_14458_call(), 0)
call_17080 = relay.TupleGetItem(func_14460_call(), 0)
output = call_17079
output2 = call_17080
func_17091 = relay.Function([], output)
mod['func_17091'] = func_17091
mod = relay.transform.InferType()(mod)
output = func_17091()
func_17092 = relay.Function([], output)
mutated_mod['func_17092'] = func_17092
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14839_call = mod.get_global_var('func_14839')
func_14840_call = mutated_mod.get_global_var('func_14840')
call_17227 = func_14839_call()
call_17228 = func_14839_call()
output = call_17227
output2 = call_17228
func_17235 = relay.Function([], output)
mod['func_17235'] = func_17235
mod = relay.transform.InferType()(mod)
mutated_mod['func_17235'] = func_17235
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17235_call = mutated_mod.get_global_var('func_17235')
call_17236 = func_17235_call()
output = call_17236
func_17237 = relay.Function([], output)
mutated_mod['func_17237'] = func_17237
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12563_call = mod.get_global_var('func_12563')
func_12565_call = mutated_mod.get_global_var('func_12565')
call_17254 = relay.TupleGetItem(func_12563_call(), 0)
call_17255 = relay.TupleGetItem(func_12565_call(), 0)
func_14124_call = mod.get_global_var('func_14124')
func_14125_call = mutated_mod.get_global_var('func_14125')
call_17257 = func_14124_call()
call_17258 = func_14124_call()
func_2297_call = mod.get_global_var('func_2297')
func_2300_call = mutated_mod.get_global_var('func_2300')
const_17260 = relay.const(-9.414973, dtype = "float32")#candidate|17260|()|const|float32
const_17261 = relay.const([-1.256041,5.476407,-5.563019,5.222542,-7.392845,8.312209,1.193359,6.899901,-3.212657,6.481867,-3.077954,3.956885,-1.432512,5.780079,-6.074376,-9.888061,4.043997,8.136089,-8.249037,-5.760325,-5.200594,-2.459527,6.746671,2.242672,-9.518731,-2.321878,-7.943703,-1.960087,8.636342,-7.523816,7.873192,2.937094,-3.132867,-8.456094,6.025457,8.403129,8.164365,2.208039,3.345030,-2.429088,1.175832,-6.862258,-2.501837,-9.767984,7.823897,3.390283,-6.082007,8.223612,8.664619,4.426180,4.561635,-5.831862,-2.204988,1.356406,4.401042,-9.898150,-1.340186,-6.283387,9.658187,7.373765,8.766815,5.725320,7.660768,7.734005,2.898790,6.179654,0.312574,0.138245,6.535990,-5.430380,-8.418216,3.609487,6.529695,-9.539087,-4.194735,5.738207,-6.625716,6.628549,-8.575353,1.924262,2.334984,-1.078418,-7.642926,4.432590,-5.931451,-7.702928,-3.716595,-0.682920,5.778916,-3.406492,-4.967330,-9.094854,9.281417,-8.968561,-7.965208,0.073560,-1.506067,-7.673961,6.964011,-9.380895,9.264195,-5.959803,-2.427749,-2.033748,8.691766,3.647780,-1.627900,1.933740,-1.366510,4.927296,8.077128,-4.373484,-9.546923,-8.929627,-1.980905,-7.038435,-7.262396,9.214137,2.313399,-1.475850,2.579599,-9.957002,9.639294,8.631162,6.457607,-7.471915,9.273357,-5.650828,-4.428875,4.334838,2.255109,-1.106435,-8.935801,-4.679629,4.994139,9.683711,-1.892876,0.543339,9.417788,2.052645,4.500641,0.267781,2.509097,3.408746,-4.938585,-1.182940,-6.123849,1.377591,5.659606,-0.828612,3.158323,2.399511,4.854875,7.113673,2.382754,4.726725,0.894302,0.769865,-0.309358,-4.616589,9.390936,-7.860514,2.824272,-2.435505,6.096047,-9.575902,-9.891557,-3.580263,-9.598451,-9.306372,6.622024,-8.883449,-7.170371,1.141073,-0.795248,-4.094830,-8.295862,4.489025,-7.157140,-5.584277,-9.594997,-6.224831,-7.321704,-9.765069,4.086812,-0.699612,-9.158240,6.645965,-7.449903,0.692465,-1.711206,-8.131577,-6.120984,-5.411104,-0.084152,-2.044247,0.375467,9.409308,-1.478735,-2.687354,6.554265,-3.051585,-9.489956,-0.337311,-3.350751,9.442798,7.765095,6.700032,-4.850010,7.670060,2.156422,2.666581,-4.629216,-6.680807,0.941054,-1.491970,-9.085549,-5.048106,-7.888959,5.557166], dtype = "float32")#candidate|17261|(220,)|const|float32
call_17259 = func_2297_call(relay.reshape(const_17260.astype('float32'), []), relay.reshape(const_17261.astype('float32'), [11, 5, 4]), )
call_17262 = func_2297_call(relay.reshape(const_17260.astype('float32'), []), relay.reshape(const_17261.astype('float32'), [11, 5, 4]), )
output = relay.Tuple([call_17254,call_17257,call_17259,const_17260,const_17261,])
output2 = relay.Tuple([call_17255,call_17258,call_17262,const_17260,const_17261,])
func_17271 = relay.Function([], output)
mod['func_17271'] = func_17271
mod = relay.transform.InferType()(mod)
mutated_mod['func_17271'] = func_17271
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17271_call = mutated_mod.get_global_var('func_17271')
call_17272 = func_17271_call()
output = call_17272
func_17273 = relay.Function([], output)
mutated_mod['func_17273'] = func_17273
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15506_call = mod.get_global_var('func_15506')
func_15508_call = mutated_mod.get_global_var('func_15508')
call_17291 = relay.TupleGetItem(func_15506_call(), 0)
call_17292 = relay.TupleGetItem(func_15508_call(), 0)
func_13412_call = mod.get_global_var('func_13412')
func_13416_call = mutated_mod.get_global_var('func_13416')
var_17321 = relay.var("var_17321", dtype = "float32", shape = (264,))#candidate|17321|(264,)|var|float32
var_17322 = relay.var("var_17322", dtype = "int64", shape = (448,))#candidate|17322|(448,)|var|int64
call_17320 = relay.TupleGetItem(func_13412_call(relay.reshape(var_17321.astype('float32'), [132, 2]), relay.reshape(var_17322.astype('int64'), [8, 56]), ), 2)
call_17323 = relay.TupleGetItem(func_13416_call(relay.reshape(var_17321.astype('float32'), [132, 2]), relay.reshape(var_17322.astype('int64'), [8, 56]), ), 2)
func_12166_call = mod.get_global_var('func_12166')
func_12169_call = mutated_mod.get_global_var('func_12169')
var_17337 = relay.var("var_17337", dtype = "float64", shape = (132,))#candidate|17337|(132,)|var|float64
call_17336 = relay.TupleGetItem(func_12166_call(relay.reshape(var_17337.astype('float64'), [2, 6, 11])), 0)
call_17338 = relay.TupleGetItem(func_12169_call(relay.reshape(var_17337.astype('float64'), [2, 6, 11])), 0)
uop_17341 = relay.rsqrt(call_17320.astype('float64')) # shape=(132, 2)
uop_17343 = relay.rsqrt(call_17323.astype('float64')) # shape=(132, 2)
func_8304_call = mod.get_global_var('func_8304')
func_8307_call = mutated_mod.get_global_var('func_8307')
var_17347 = relay.var("var_17347", dtype = "float32", shape = (9, 60))#candidate|17347|(9, 60)|var|float32
call_17346 = func_8304_call(relay.reshape(var_17347.astype('float32'), [15, 12, 3]))
call_17348 = func_8304_call(relay.reshape(var_17347.astype('float32'), [15, 12, 3]))
func_3702_call = mod.get_global_var('func_3702')
func_3707_call = mutated_mod.get_global_var('func_3707')
var_17350 = relay.var("var_17350", dtype = "float64", shape = (300,))#candidate|17350|(300,)|var|float64
var_17351 = relay.var("var_17351", dtype = "float32", shape = (1, 12))#candidate|17351|(1, 12)|var|float32
var_17352 = relay.var("var_17352", dtype = "uint16", shape = (225,))#candidate|17352|(225,)|var|uint16
call_17349 = relay.TupleGetItem(func_3702_call(relay.reshape(var_17322.astype('int64'), [14, 16, 2]), relay.reshape(var_17350.astype('float64'), [300,]), relay.reshape(var_17351.astype('float32'), [12,]), relay.reshape(var_17352.astype('uint16'), [25, 9]), ), 3)
call_17353 = relay.TupleGetItem(func_3707_call(relay.reshape(var_17322.astype('int64'), [14, 16, 2]), relay.reshape(var_17350.astype('float64'), [300,]), relay.reshape(var_17351.astype('float32'), [12,]), relay.reshape(var_17352.astype('uint16'), [25, 9]), ), 3)
output = relay.Tuple([call_17291,var_17321,var_17322,call_17336,var_17337,uop_17341,call_17346,var_17347,call_17349,var_17350,var_17351,var_17352,])
output2 = relay.Tuple([call_17292,var_17321,var_17322,call_17338,var_17337,uop_17343,call_17348,var_17347,call_17353,var_17350,var_17351,var_17352,])
func_17363 = relay.Function([var_17321,var_17322,var_17337,var_17347,var_17350,var_17351,var_17352,], output)
mod['func_17363'] = func_17363
mod = relay.transform.InferType()(mod)
mutated_mod['func_17363'] = func_17363
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17363_call = mutated_mod.get_global_var('func_17363')
var_17365 = relay.var("var_17365", dtype = "float32", shape = (264,))#candidate|17365|(264,)|var|float32
var_17366 = relay.var("var_17366", dtype = "int64", shape = (448,))#candidate|17366|(448,)|var|int64
var_17367 = relay.var("var_17367", dtype = "float64", shape = (132,))#candidate|17367|(132,)|var|float64
var_17368 = relay.var("var_17368", dtype = "float32", shape = (9, 60))#candidate|17368|(9, 60)|var|float32
var_17369 = relay.var("var_17369", dtype = "float64", shape = (300,))#candidate|17369|(300,)|var|float64
var_17370 = relay.var("var_17370", dtype = "float32", shape = (1, 12))#candidate|17370|(1, 12)|var|float32
var_17371 = relay.var("var_17371", dtype = "uint16", shape = (225,))#candidate|17371|(225,)|var|uint16
call_17364 = func_17363_call(var_17365,var_17366,var_17367,var_17368,var_17369,var_17370,var_17371,)
output = call_17364
func_17372 = relay.Function([var_17365,var_17366,var_17367,var_17368,var_17369,var_17370,var_17371,], output)
mutated_mod['func_17372'] = func_17372
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12011_call = mod.get_global_var('func_12011')
func_12012_call = mutated_mod.get_global_var('func_12012')
call_17391 = relay.TupleGetItem(func_12011_call(), 0)
call_17392 = relay.TupleGetItem(func_12012_call(), 0)
uop_17407 = relay.rsqrt(call_17391.astype('float64')) # shape=(2, 6, 11)
uop_17409 = relay.rsqrt(call_17392.astype('float64')) # shape=(2, 6, 11)
output = uop_17407
output2 = uop_17409
func_17414 = relay.Function([], output)
mod['func_17414'] = func_17414
mod = relay.transform.InferType()(mod)
mutated_mod['func_17414'] = func_17414
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17414_call = mutated_mod.get_global_var('func_17414')
call_17415 = func_17414_call()
output = call_17415
func_17416 = relay.Function([], output)
mutated_mod['func_17416'] = func_17416
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12866_call = mod.get_global_var('func_12866')
func_12867_call = mutated_mod.get_global_var('func_12867')
call_17475 = relay.TupleGetItem(func_12866_call(), 1)
call_17476 = relay.TupleGetItem(func_12867_call(), 1)
output = call_17475
output2 = call_17476
func_17486 = relay.Function([], output)
mod['func_17486'] = func_17486
mod = relay.transform.InferType()(mod)
mutated_mod['func_17486'] = func_17486
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17486_call = mutated_mod.get_global_var('func_17486')
call_17487 = func_17486_call()
output = call_17487
func_17488 = relay.Function([], output)
mutated_mod['func_17488'] = func_17488
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14508_call = mod.get_global_var('func_14508')
func_14510_call = mutated_mod.get_global_var('func_14510')
call_17501 = func_14508_call()
call_17502 = func_14508_call()
output = relay.Tuple([call_17501,])
output2 = relay.Tuple([call_17502,])
func_17531 = relay.Function([], output)
mod['func_17531'] = func_17531
mod = relay.transform.InferType()(mod)
mutated_mod['func_17531'] = func_17531
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17531_call = mutated_mod.get_global_var('func_17531')
call_17532 = func_17531_call()
output = call_17532
func_17533 = relay.Function([], output)
mutated_mod['func_17533'] = func_17533
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15964_call = mod.get_global_var('func_15964')
func_15966_call = mutated_mod.get_global_var('func_15966')
call_17594 = relay.TupleGetItem(func_15964_call(), 0)
call_17595 = relay.TupleGetItem(func_15966_call(), 0)
func_9908_call = mod.get_global_var('func_9908')
func_9913_call = mutated_mod.get_global_var('func_9913')
var_17610 = relay.var("var_17610", dtype = "uint32", shape = (320,))#candidate|17610|(320,)|var|uint32
const_17611 = relay.const([-8,-3,10,4,8,1,1,3,10,-10,-3,5,2,3,1,2,-8,10,-1,-9,-2,-3,4,-7,-5,1,10,3,7,7,-3,-9,4,-8,4,5,2,10,-5,-10,-8,8,8,-7,9,-5,3,-3,3,-3,1,-2,-8,-8,-1,-3,9,4,-3,4,-7,2,5,8,-7,5,-10,2,1,-3,8,1,7,7,-8,-2,2,-4,1,4,-4,-9,-6,-4,-3,-9,-5,8,-6,2,6,7,-7,-2,3,-8,5,-3,8,-7,-4,-2,5,-1,-5,-4,-6,-8,4,-3,5,3,-1,-10,4,10,4,-9,3,9,-2,8,4,2,5,-4,-9,2,-3,-8,2,7,1,-4,-5,-2,-5,-4,6,8,1,2,9,9,8,3,7,-5,-5,5,-1,-4,7,5,3,-5,-5,6,2,-10,-5,10,2,-2,-2,6,2,-10,-9,2,-8,8,-3,9,-10,-6,3,-8,-9,1,-5,-5,-8,-8,9,9,-9,3,3,-7,-5,7,7,1,6,-9,1,-10,6,6,-9,5,3,-10,-1,9,-10,-2,-4,4,8,-10,7,8,7,-1,8,-4,3,7,-1,-10,3,-9,-8,6,8,5,-6,-1,6,1,7,4,1,5,-6,-2,-8,7,-6,2,-8,1,7,-9,1,6,7,-9,-1,-10,-9,7,5,-3,-4,-7,9,6,-8,-10,5,9,8,-2,-10,6,-5,9,5,-5,5,1,1,-4,2,-10,-2,1,-6,-6,3,8,-3,2,-8,-8,8,-9,-7,-8,8,8,-8,7,9,-2,3,4,8,-5,2,1,5,9,-4,-2,8,10,6,1,1,2,5,2,-2,2,-4,-6,-5,-10,-3,-9,10,-8,-7,6,2,3,-3,-5,-4,1,-1,7,-3,5,7,8,5,6,2,-1,-9,4,-9,-9,7,3,8,-4,-4,6,2,9,-7,-1,-6,-5,-7,6,-9,3,6,4,5,-4,6,2,-3,7,-7,-1,3,7,9,9,10,-6,7,2,-9,-5,-10,6,10,-5,4,-10,-6,-8,-2,-2,9,1,-1,10,-1,6,-1,-5,6,6,8,6,4,-8,8,-9,2,-3,-2,3,-9,5,3,-9,-3,-8,2,6,7,2,-6,4,-8,-8,-1,6,-2,-10,-4,-4,5,-8,8,-4,-8,2,-7,9,-5,-8,8,6,6,2], dtype = "int64")#candidate|17611|(448,)|const|int64
var_17612 = relay.var("var_17612", dtype = "uint16", shape = (225,))#candidate|17612|(225,)|var|uint16
call_17609 = relay.TupleGetItem(func_9908_call(relay.reshape(var_17610.astype('uint32'), [16, 2, 10]), relay.reshape(const_17611.astype('int64'), [1, 448]), relay.reshape(var_17612.astype('uint16'), [225, 1]), ), 0)
call_17613 = relay.TupleGetItem(func_9913_call(relay.reshape(var_17610.astype('uint32'), [16, 2, 10]), relay.reshape(const_17611.astype('int64'), [1, 448]), relay.reshape(var_17612.astype('uint16'), [225, 1]), ), 0)
output = relay.Tuple([call_17594,call_17609,var_17610,const_17611,var_17612,])
output2 = relay.Tuple([call_17595,call_17613,var_17610,const_17611,var_17612,])
func_17631 = relay.Function([var_17610,var_17612,], output)
mod['func_17631'] = func_17631
mod = relay.transform.InferType()(mod)
var_17632 = relay.var("var_17632", dtype = "uint32", shape = (320,))#candidate|17632|(320,)|var|uint32
var_17633 = relay.var("var_17633", dtype = "uint16", shape = (225,))#candidate|17633|(225,)|var|uint16
output = func_17631(var_17632,var_17633,)
func_17634 = relay.Function([var_17632,var_17633,], output)
mutated_mod['func_17634'] = func_17634
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17091_call = mod.get_global_var('func_17091')
func_17092_call = mutated_mod.get_global_var('func_17092')
call_17636 = func_17091_call()
call_17637 = func_17091_call()
output = relay.Tuple([call_17636,])
output2 = relay.Tuple([call_17637,])
func_17640 = relay.Function([], output)
mod['func_17640'] = func_17640
mod = relay.transform.InferType()(mod)
mutated_mod['func_17640'] = func_17640
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17640_call = mutated_mod.get_global_var('func_17640')
call_17641 = func_17640_call()
output = call_17641
func_17642 = relay.Function([], output)
mutated_mod['func_17642'] = func_17642
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13081_call = mod.get_global_var('func_13081')
func_13083_call = mutated_mod.get_global_var('func_13083')
call_17649 = relay.TupleGetItem(func_13081_call(), 0)
call_17650 = relay.TupleGetItem(func_13083_call(), 0)
func_349_call = mod.get_global_var('func_349')
func_354_call = mutated_mod.get_global_var('func_354')
const_17681 = relay.const([1,10,-1,-4,-7,-4,3,-2,-9,2,-1,-10,1,-8,-7,8,8,-10,9,9,-4,-6,9,3,-4,9,-7,-10,3,3,-9,-10,6,-4,-3,-10,-10,-5,4,-6,-2,4,3,2,-4,-8,3,-7,-5,6,8,4,-10,-6,6,3,-6,-1,-2,7,-7,6,10,-1,-6,2,10,-3,-6,5,2,1,-4,7,5,-2,8,2,-3,2,7,5,-1,-10,-9,10,-2,9,5,-3,-1,-3,-5,6,6,-1,-5,2,7,4,6,7,-7,7,-2,2,-7,2,-8,4,-10,10,-3,3,4,-6,-1,10,7,10,10,-3,-5,-3,-5,8,1,-1,10,-4,1,-7,-3,2,6,1,4,-5,1,3,-4,-3,8,-1,10,-5,5,5,10,-10,-1,-6,-7,3,10,5,-6,-1,6,5,7,-9,1,-10,3,-1,1,1,-8,-5,10,-4,-10,-3,7,2,-9,8,-7,2,10,-6,3,-8,-2,1,3,-10,-10,-9,2,-3,-2,-10,-1,1,-8,-2,-4,1,-3,10,8,1,7,-7,3,2,2,6,-6,5,-6,6,9,-8,2,10,-9,7,5,5,-3,3,8,-9,8,2,-2,4,6,4,9,7,9,4,-10,-1,-5,-10,-6,1,4,-6,10,8,1,5,7,9,-7,-9,-1,10,7,-3,9,-4,7,-9,-3,6,-8,5,-2,1,-7,-4,3,6,-6,-2,5,9,-10,-1,-5,7,8,1,6,9,4,-10,9,-8,7,9,-8,3,7,10,-1,-7,7,-8,10,6,1,3,-4,-7,3,-2,-6,-8,9,7,5,10,10,6,-5,5,6,10,-1,10,2,-4,7,1,9,7,-2,7,4,3,4,7,-6,-2,1,10,6,-4,-5,8,-3,-8,-1,-8,-8,4,8,2,8,2,7,-5,-5,3,-5,4,7,4,8,-5,-2,-8,2,-8,-3,-2,-2,1,-7,5,-9,-10,4,-8,-4,9,-2,8,-7,2,7,-10,2,-6,10,-9,-2,-7,10,9,8,4,4,-2,10,-3,-10,6,6,1,3,7,10,2,-1,6,10,9,-3,7,7,-10,4,-2,-6,-8,-4,4,3,4,8,3,-1,2,-5,7,10,2,-3,-6,-7,8,1,3,-10,10,-6,-4,5,-3,6,4,-7,-9,9,9,-10,-7,-1,-7,-5,8,7,-2,-1,-7,-5,2,7,10,7,-4,-8,-7,9,-9,8,10,1,-2,-5,9,9,-1,3,2,3,-4,-7,10,-7,-2,8,2,4,-2,-2,10,-2,-8,2,-4,8,-6,3,10,-4,-2,-6,2,10,-8,6,-4,9,-5,3,-6,1,5,9,-1,2,7,-2,6,4,-2,4,-3,7,-3,-9,-1,-4,-4,6,6,-3,-3,-2,4,-7,-10,-2,3,1,2,-7,-2,-3,-4,4,-6,2,1,-10,-4,1,7,7,7,-8,-9,3,-7,-8,5,10,-10,-3,-10,3,-10,-8,-10,-9,-10,-5,3,10,6,3,-3,-5,7,1,-10,1,-1,-9,1,-7,6,-2,9,2,-4,-9,8,-10,-1,-4,9,3,4,2,-1,-10,10,7,-8,7,4,10,9,10,-3,2,-2,2,6,-3,1,-5,9,-2,-1,-8,-4,-8,8,-2,-2,3,-9,10,-8,-4,8,2,1,4,-3,-8,1,-8,2,10,-6,6,9,-3,-8,-6,6,4,1,9,10,-1,-3,-2,10,-9,-6,-2,-2,9,-1,8,4,3,2,1,1,-5,-10,-1,10,7,-4,10,-3,8,6,1,10,7,-8,-5,8,-5,-6,1,6,-1,-8,-8,10,6,2,5,-1,-3,9,-2,-8,9,3,10,-7,-2,10,7,6,5,9,9,2,-1,-9,-2,-9,-3,-9,4,5,-3,5,-4,-1,8,-1,-2,-8,6,5,8,-6,-8,5,-3,9,-5,5,-5,10,-10,10,-2,6,-10,5,-9,-9,8,-1,2,8,-6,7,-3,7,-6,7,7,-7,6,-3,2,2,-3,2,2,-3,7,10,-6,3,-3,-1,4,7,1,5,-1,-7,9,-2,-1,1,-4,8,-7,-4,-3,-3,5,1,2,-1,-2,-9,-8,-3,-5,-9,-5,-1,-1,-7,1,3,1,-4,-9,-4,-3,-1,-4,-2,-9,10,-9,10,-7,4,6,4,1,-8,2,1,-7,-8,9,1,-2,-3,3,9,-10,-10,2,4,3,-6,-6,-2,-1,3,2,-7,-5,5,6,10,9,-10,5,4,6,2,-7,2,-7,-8,-8,-5,-7,-9,-4,-7,-10,-4,3,-10,8,-8,8,-4,6,6,-7,5,1,9,6,10,4,-8,4,3,-1,8,4,8,4,-4,-5,6,-6,3,10,-5,-7,-9,-10,-2,7,2,-2,3,-4,-6,9,-7,7,-6,-5,-1,-5,-3,5,8,7,-3,-10,-4,5,-5,4,-9,6,-5,-6,3,-7,6,2,-5,-4,8,7,10,4,4,9,-6,-9,-6,-9,6,-3,-9,-6,6,3,4,7,-1,1,-8,9,7,-7,2,-10,-4,-1,-10,9,7,-1,3,-6,9,-10,-10,-1,6,8,5,-8,-2,6,-8,-9,7,7,-8,-2,2,3,2,7,-5,-8,4,1,-7,-10,-2,-9,9,-8,-10,-5,4,-4,-6,-4,5,-1,-8,-7,-9,-9,5,9,5,-2,-8,7,9,-8,-2,5,-4,10,-1,6,-1,-1,2,-10,-9,-10,-1,1,-10,-4,1,4,6,-7,9,6,-8,-6,-9,5,-3,7,6,6,6,10,9,-5,8,-1,5,8,-4,-2,-3,3,4,1,-7,-3,7,4,-9,-3,9,3,1,7,-6,-10,-6,6,-2,-7,6,-6,7,-10,-7,1,-5,1,-8,1,7,-4,4,-2,-8,9,-3,8,-3,4,1,7,4,2,-6,5,-6,-6,-10,1,9,4,3,10,10,7,3,-7,-3,6,-6,5,-1,-4,-1,-3,-5,10,10,-7,6,-2,-9,4,2,3,5,9,9,1,10,-8,-2,4,-10,4,4,-5,-7,-5,10,-4,-6,-3,8,-4,-7,-5,1,-2,-10,-7,2,-9,10,7,-2,7,8,2,5,4,8,-2,9,-2,-10,-7,-10,3,-2,3,3,-1,-1,7,-9,-9,-10,-8,7,-2,-10,9,-7,1,5,3,-4,-1,9,3,10,-9,-5,3,-8,8,4,-7,2,-10,1,-6,-10,-4,-6,-1,10,-9,6,4,-7,-1,2,3,7,10,7,-7,-3,-9,7,-5,9,-10,6,-10,-8,3,10,-3,-9,5,9,4,2,-2,5,-3,-3,-1,9,-1,4,-9,10,-9,5,7,-5,-9,-6,5,-2,6,-1,6,10,-1,3,-7,1,2,-2,-1,9,4,-5,-7,-7,-2,-1,10,-8,-4,-10,4,8,9,-4,-7,-2,-10,-1,-2,1,-9,-4,6,2,3,-2,3,-10,10,-3,-8,-9,2,7,-8,-1,5,-6,7,2,9,-6,3,-3,1,9,10,10], dtype = "uint64")#candidate|17681|(1320,)|const|uint64
var_17682 = relay.var("var_17682", dtype = "uint16", shape = (225,))#candidate|17682|(225,)|var|uint16
call_17680 = relay.TupleGetItem(func_349_call(relay.reshape(const_17681.astype('uint64'), [11, 12, 10]), relay.reshape(const_17681.astype('uint64'), [11, 12, 10]), relay.reshape(var_17682.astype('uint16'), [225,]), ), 4)
call_17683 = relay.TupleGetItem(func_354_call(relay.reshape(const_17681.astype('uint64'), [11, 12, 10]), relay.reshape(const_17681.astype('uint64'), [11, 12, 10]), relay.reshape(var_17682.astype('uint16'), [225,]), ), 4)
output = relay.Tuple([call_17649,call_17680,const_17681,var_17682,])
output2 = relay.Tuple([call_17650,call_17683,const_17681,var_17682,])
func_17688 = relay.Function([var_17682,], output)
mod['func_17688'] = func_17688
mod = relay.transform.InferType()(mod)
var_17689 = relay.var("var_17689", dtype = "uint16", shape = (225,))#candidate|17689|(225,)|var|uint16
output = func_17688(var_17689)
func_17690 = relay.Function([var_17689], output)
mutated_mod['func_17690'] = func_17690
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12838_call = mod.get_global_var('func_12838')
func_12840_call = mutated_mod.get_global_var('func_12840')
call_17696 = relay.TupleGetItem(func_12838_call(), 0)
call_17697 = relay.TupleGetItem(func_12840_call(), 0)
func_14917_call = mod.get_global_var('func_14917')
func_14920_call = mutated_mod.get_global_var('func_14920')
var_17699 = relay.var("var_17699", dtype = "float32", shape = (1056,))#candidate|17699|(1056,)|var|float32
call_17698 = func_14917_call(relay.reshape(var_17699.astype('float32'), [11, 16, 6]))
call_17700 = func_14917_call(relay.reshape(var_17699.astype('float32'), [11, 16, 6]))
func_12448_call = mod.get_global_var('func_12448')
func_12450_call = mutated_mod.get_global_var('func_12450')
call_17705 = relay.TupleGetItem(func_12448_call(), 0)
call_17706 = relay.TupleGetItem(func_12450_call(), 0)
output = relay.Tuple([call_17696,call_17698,var_17699,call_17705,])
output2 = relay.Tuple([call_17697,call_17700,var_17699,call_17706,])
func_17710 = relay.Function([var_17699,], output)
mod['func_17710'] = func_17710
mod = relay.transform.InferType()(mod)
mutated_mod['func_17710'] = func_17710
mutated_mod = relay.transform.InferType()(mutated_mod)
var_17711 = relay.var("var_17711", dtype = "float32", shape = (1056,))#candidate|17711|(1056,)|var|float32
func_17710_call = mutated_mod.get_global_var('func_17710')
call_17712 = func_17710_call(var_17711)
output = call_17712
func_17713 = relay.Function([var_17711], output)
mutated_mod['func_17713'] = func_17713
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14342_call = mod.get_global_var('func_14342')
func_14343_call = mutated_mod.get_global_var('func_14343')
call_17724 = relay.TupleGetItem(func_14342_call(), 0)
call_17725 = relay.TupleGetItem(func_14343_call(), 0)
func_12448_call = mod.get_global_var('func_12448')
func_12450_call = mutated_mod.get_global_var('func_12450')
call_17742 = relay.TupleGetItem(func_12448_call(), 0)
call_17743 = relay.TupleGetItem(func_12450_call(), 0)
output = relay.Tuple([call_17724,call_17742,])
output2 = relay.Tuple([call_17725,call_17743,])
func_17744 = relay.Function([], output)
mod['func_17744'] = func_17744
mod = relay.transform.InferType()(mod)
mutated_mod['func_17744'] = func_17744
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17744_call = mutated_mod.get_global_var('func_17744')
call_17745 = func_17744_call()
output = call_17745
func_17746 = relay.Function([], output)
mutated_mod['func_17746'] = func_17746
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15203_call = mod.get_global_var('func_15203')
func_15205_call = mutated_mod.get_global_var('func_15205')
call_17807 = relay.TupleGetItem(func_15203_call(), 0)
call_17808 = relay.TupleGetItem(func_15205_call(), 0)
func_12272_call = mod.get_global_var('func_12272')
func_12274_call = mutated_mod.get_global_var('func_12274')
const_17821 = relay.const([-2,-1,-7,-3,-4,-4,9,-1,3,8,-6,4,-9,9,10,1,2,-1,6,7,-9,2,8,4,-3,-1,-1,8,-8,7,-4,2,-2,-6,-4,-8,-2,5,-6,-1,1,9,7,-1,-4,-2,9,-4,-6,-9,1,-5,2,5,1,6,-10,-4,-4,-1,-5,9,-7,-5,1,-3,-5,-9,10,-4,10,5,-7,-6,-5,-3,9,4,-3,9,5,10,2,-7,-3,-5,1,2,8,2,4,6,7,7,1,8,8,7,7,-4,5,3,9,5,-5,1,-4,3,8,-1,-8,6,7,7,7,4,1,9,5,5,3,-9,4,-6,2,1,6,-5,1,5,-1,10,-6,-10,-3,1,3,-2,-10,9,-8,9,8,-7,5,-6,2,-8,5,9,5,7,-8,4,7,-1,4,9,5,8,9,-6,-10,-9,-2,-6,-8,6,-1,-7,4,5,7,7,-1,10,8,1,10,-6,10,-1,4,8,8,4,-1,-9,5,10,10,6,-6,8,6,-10,8,5,-1,-7,-8,2,-10,-8,4,10,10,3,-2,-3,7,-5,7,6,4,-10,4,2,10,10,-7,-9,8,-2,5,7,1,8,3,-7,-7,7,-8,7,8,3,10,4,-7,6,-4,-5,-6,-2,-7,6,-7,-5,-2,4,-2,5,10,-1,8,1,2,-4,9,9,-6,-9,-10,7,-9,-9,-9,-4,-8,7,2,-5,-4,-5,6,10,-1,-6,-5,2,-5,4,9,-2,-1,-10,-7,-9,5,-7,-2,-4,7,-5,-4,-6,-7,-2,8,-3,5,4,-10,6,-9,-8,-9,3,6,-8,-4,-1,5,-9,-9,2,8,7,-10,-5,5,9,8,2,1,-4,4,-10,-9,2,1,-2,-1,-9,4,-2,-5,-5,-7,7,-8,-5,-6,-3,-3,-3,-10,-5,5,-4,6,-8,-8,-8,-3,-3,5,5,-2,-6,-5,1,-3,-6,10,7,-5,9,-9,6,-1,3,8,9,6,7,6,7,-4,-10,-1,10,-2,-7,5,3,4,-4,-3,2,-10,-3,7,-8,10,-5,6,7,6,9,9,7,-9,6,4,1,9,10,3,8,7,6,-1,-1,7,6,5,9,-4,4,-7,4,3,3,-4,-9,6,-6,8,-4,9,-1,5,8,9,9,-9,1,7,-7,-6,-3,4,1,-7,7,5,10,-1,1,-10,-3,5,2,9,4,8,10,-7,3,6,-9,9,-2,8,8,6,-9,-7,-5,-10,2,6,-9,-2,6,2,8,-5,-10,6,10,-1,-4,-10,5,-10,8,-10,9,-9,10,10,-3,-8,5,2,7,6,4,-2,6,7,-8,-10,8,1,3,6,4,10,8,-7,-9,-8,-9,-1,4,6,4,-8,7,2,1,-7,-2,6,-1,6,-6,-3,9,-9,-4,3,-2,2,-10,-9,-10,8,5,3,7,-8,-6,-9,4,5,2,8,3,-3,-4,-6,1,8,5,2,1,-6,-10,9,2,4,6,-8,-1,1,-3,2,8,10,9,7,1,-6,-8,-4,1,-4,9,-5,3,6,3,-2,5,-8,3,6,-1,-4,7,1,8,-4,-7,7,-7,6,10,2,-9,2,6,-5,-8,5,-8,1,2,-3,8,-7,-3,-4,-10,-8,9,-10,-6,3,5,-9,-6,1,10,7,3,3,-6,9,-5,4,7,-10,-8,-8,3,-9,10,5,3,-7,5,-6,-7,8,4,-6,7,-5,-9,9,4,10,-8,-3,-6,-9,10,-3,-10,9,-4,-6,-2,-5,8,4,-2,6,-9,10,1,6,5,-8,-10,-1,-1,5,-10,4,-2,7,-3,3,2,-5,3,4,-3,-4,-9,-9,-4,4,3,-9,6,-1,9,-1,9,3,9,1,8,-7,2,7,-2,-9,9,-2,-4,-6,-10,3,4,1,-1,-7,8,8,-4,8,-6,-1,-3,-1,-9,-9,5,8,7,-5,10,7,-10,1,-10,7,4,-10,-2,-5,10,-10,7,6,-7,-10,3,-8,4,6,-6,7,-3,-10,-10,8,10,-6,-7,-1,-1,5,2,-8,1,-10,7,1,-6,6,6,7,5,-5,4,-9,8,-1,-5,7,-1,7,4,-9,-6,6,1,10,-5,-8,-10,3,1,8,-3,4,-10,1,8,4,-4,-8,4,-1,-10,7,4,-7,6,-10,8,2,-6,4,2,10,8,3,5,-10,-10,6,-9,-10,-8,-3,-6,-6,7,-8,8,6,-5,6,2,-4,5,8,-3,-10,-1,-7,7,1,3,-6,7,-7,-1,-2,-10,-7,6,-8,4,-10,-10,-3,-10,4,2,-4,-2,-1,3,7,-10,10,-10,5,-6,-10,-1,7,7,-5,-1,-10,-10,-5,-4,8,-9,-2,-7,-4,3,1,-8,5,2,-6,9,-6,-7,-3,5,7,-2,-2,7,3,-1,5,-5,-5,-10,-9,-7,9,-8,-4,-8,7,-1,8,-5,1,-7,5,7,-10,3,10,-6,3,-3,-7,10,-10,2,-1,1,3,8,-2,10,-4,3,2,-4,3,1,-8,-5,4,-8,-2,-8,-9,-3,-3,-4,5,-2,-7,1,4,2,-5,-2,-2,-5,-3,1,1,-4,-8,-3,6,-9,4,4,2,-1,1,-5,6,-1,-4,3,-8,-2,-9,-9,-2,9,8,3,-9,8,-8,7,6,-4,-10,-8,8,-3,4,-2,-2,-2,6,2,-10,5,5,3,-10,2,8,6,-9,-2,3,-1,9,-5,1,-8,10,-10,-7,-6,1,-7,-7,6,-2,-1,6,-9,-5,8,4,6,1,-10,-10,5,6,2,-5,-1,9,-3,4,-8,6,7,-3,-5,1,-3,4,4,-2,-5,-5,5,10,8,7,7,3,-7,-8,-9,10,2,3,-7,-4,-1,1,-4,-3,-9,8,6,-9,-6,-7,-8,10,-4,7,8,-4,-10,-7,7,5,-10,9,6,1,7,-8,7,-6,-1,-10,4,-7,8,9,4,1,-10,-2,-10,-8,-2,-3,-6,-10,4,5,-4,4,-6,7,-8,-6,9,-3,-10,8,-1,1,-2,4,10,3,4,8,-10,-2,5,7,5,-5,-4,6,-5,-3,-5,2,10,1,-5,-4,6,-5,5,7,3,6,6,-3,9,8,4,-1,-9,8,1,-1,9,10,-2,-5,-8,4,-3,6,4,-7,-6,-3,-1,1,5,1,-9,-10,-7,-8,6,-10,9,-2,-10,1,7,2,-7,2,-4,7,-5,6,4,8,4,-10,3,-5,-8,2,-10,-3,-7,10,9,9,-6,5,-7,-9,-10,5,10,-8,-6,-4,-5,5,4,-7,5,-7,9,1,7,-10,-9,-2,-4,-9,-3,9,2,3,-3,10,-6,-1,3,4,3,8,-8,-3,5,3,5,-7,7,-4,10,-8,-5,3,10,7,-9,5,9,10,-10,-1,6,-1,-10,5,2,-6,2,-4,-7,8,-8,-3,-1,-1,9,-5,4,10,-4,3,8,-3,-1,3,-8,3,-3,4,-1,-8,-9,-5,-10,6,-2,2,-10,-10,-1,-8,5,-6,-8,-6,-5,9,-7,6,3,-3,-9,-5,-9,-2,10,-1,1,-7,8,-2,-8,-7,-7,-4,3,7,4], dtype = "uint16")#candidate|17821|(1350,)|const|uint16
call_17820 = relay.TupleGetItem(func_12272_call(relay.reshape(const_17821.astype('uint16'), [1350,])), 2)
call_17822 = relay.TupleGetItem(func_12274_call(relay.reshape(const_17821.astype('uint16'), [1350,])), 2)
func_16292_call = mod.get_global_var('func_16292')
func_16294_call = mutated_mod.get_global_var('func_16294')
call_17862 = relay.TupleGetItem(func_16292_call(), 2)
call_17863 = relay.TupleGetItem(func_16294_call(), 2)
output = relay.Tuple([call_17807,call_17820,const_17821,call_17862,])
output2 = relay.Tuple([call_17808,call_17822,const_17821,call_17863,])
func_17864 = relay.Function([], output)
mod['func_17864'] = func_17864
mod = relay.transform.InferType()(mod)
mutated_mod['func_17864'] = func_17864
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17864_call = mutated_mod.get_global_var('func_17864')
call_17865 = func_17864_call()
output = call_17865
func_17866 = relay.Function([], output)
mutated_mod['func_17866'] = func_17866
mutated_mod = relay.transform.InferType()(mutated_mod)
var_17927 = relay.var("var_17927", dtype = "float32", shape = (1, 9, 3))#candidate|17927|(1, 9, 3)|var|float32
var_17928 = relay.var("var_17928", dtype = "float32", shape = (8, 9, 3))#candidate|17928|(8, 9, 3)|var|float32
bop_17929 = relay.floor_divide(var_17927.astype('float32'), var_17928.astype('float32')) # shape=(8, 9, 3)
output = bop_17929
output2 = bop_17929
func_17945 = relay.Function([var_17927,var_17928,], output)
mod['func_17945'] = func_17945
mod = relay.transform.InferType()(mod)
var_17946 = relay.var("var_17946", dtype = "float32", shape = (1, 9, 3))#candidate|17946|(1, 9, 3)|var|float32
var_17947 = relay.var("var_17947", dtype = "float32", shape = (8, 9, 3))#candidate|17947|(8, 9, 3)|var|float32
output = func_17945(var_17946,var_17947,)
func_17948 = relay.Function([var_17946,var_17947,], output)
mutated_mod['func_17948'] = func_17948
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12011_call = mod.get_global_var('func_12011')
func_12012_call = mutated_mod.get_global_var('func_12012')
call_17968 = relay.TupleGetItem(func_12011_call(), 1)
call_17969 = relay.TupleGetItem(func_12012_call(), 1)
output = call_17968
output2 = call_17969
func_17970 = relay.Function([], output)
mod['func_17970'] = func_17970
mod = relay.transform.InferType()(mod)
output = func_17970()
func_17971 = relay.Function([], output)
mutated_mod['func_17971'] = func_17971
mutated_mod = relay.transform.InferType()(mutated_mod)
var_18000 = relay.var("var_18000", dtype = "float32", shape = (16, 11, 6))#candidate|18000|(16, 11, 6)|var|float32
uop_18001 = relay.rsqrt(var_18000.astype('float32')) # shape=(16, 11, 6)
func_9975_call = mod.get_global_var('func_9975')
func_9978_call = mutated_mod.get_global_var('func_9978')
var_18009 = relay.var("var_18009", dtype = "float64", shape = (180,))#candidate|18009|(180,)|var|float64
call_18008 = func_9975_call(relay.reshape(var_18009.astype('float64'), [9, 10, 2]), relay.reshape(var_18009.astype('float64'), [9, 10, 2]), )
call_18010 = func_9975_call(relay.reshape(var_18009.astype('float64'), [9, 10, 2]), relay.reshape(var_18009.astype('float64'), [9, 10, 2]), )
func_12838_call = mod.get_global_var('func_12838')
func_12840_call = mutated_mod.get_global_var('func_12840')
call_18011 = relay.TupleGetItem(func_12838_call(), 0)
call_18012 = relay.TupleGetItem(func_12840_call(), 0)
func_17531_call = mod.get_global_var('func_17531')
func_17533_call = mutated_mod.get_global_var('func_17533')
call_18023 = relay.TupleGetItem(func_17531_call(), 0)
call_18024 = relay.TupleGetItem(func_17533_call(), 0)
output = relay.Tuple([uop_18001,call_18008,var_18009,call_18011,call_18023,])
output2 = relay.Tuple([uop_18001,call_18010,var_18009,call_18012,call_18024,])
func_18025 = relay.Function([var_18000,var_18009,], output)
mod['func_18025'] = func_18025
mod = relay.transform.InferType()(mod)
var_18026 = relay.var("var_18026", dtype = "float32", shape = (16, 11, 6))#candidate|18026|(16, 11, 6)|var|float32
var_18027 = relay.var("var_18027", dtype = "float64", shape = (180,))#candidate|18027|(180,)|var|float64
output = func_18025(var_18026,var_18027,)
func_18028 = relay.Function([var_18026,var_18027,], output)
mutated_mod['func_18028'] = func_18028
mutated_mod = relay.transform.InferType()(mutated_mod)
const_18059 = relay.const([[[3.184977,-3.614456,-9.433145,1.275917,3.961488,-1.954362,-0.578718,7.022144,7.206989,9.488051,-9.853977]],[[-3.611183,-6.031899,-3.024053,-1.884829,-5.969952,0.588091,7.911066,-8.604106,-6.609821,6.704889,7.575728]]], dtype = "float32")#candidate|18059|(2, 1, 11)|const|float32
uop_18060 = relay.asinh(const_18059.astype('float32')) # shape=(2, 1, 11)
func_15330_call = mod.get_global_var('func_15330')
func_15331_call = mutated_mod.get_global_var('func_15331')
call_18062 = relay.TupleGetItem(func_15330_call(), 0)
call_18063 = relay.TupleGetItem(func_15331_call(), 0)
func_6563_call = mod.get_global_var('func_6563')
func_6565_call = mutated_mod.get_global_var('func_6565')
var_18079 = relay.var("var_18079", dtype = "float32", shape = (104, 28))#candidate|18079|(104, 28)|var|float32
call_18078 = relay.TupleGetItem(func_6563_call(relay.reshape(var_18079.astype('float32'), [14, 16, 13])), 0)
call_18080 = relay.TupleGetItem(func_6565_call(relay.reshape(var_18079.astype('float32'), [14, 16, 13])), 0)
func_9335_call = mod.get_global_var('func_9335')
func_9340_call = mutated_mod.get_global_var('func_9340')
const_18093 = relay.const([4,-1,-6,-10,-9,7,-6,4,-3,6,10,-1,-6,8,7,-5,-7,-1,9,-3,-6,6,1,1,2,7,-7,3,-3,9,8,2,10,10,7,-2,4,-3,7,-10,-1,-2,-5,-4,-10,10,-6,-3,8,-10,7,-5,7,7,-4,-2,3,-5,-1,-9,-3,8,1,-10,5,3,-1,2,-8,3,-5,9,10,-10,-7,3,8,-1,-3,10,-10,-9,-1,10,-1,5,7,7,2,-8,4,8,3,5,-10,-5,7,-1,6,-2,-2,4,-3,-7,-6,-1,-6,-6,-8,-6,-5,-9,4,3,-3,8,1,7,3,-8,-10,-3,10,7,10,8,-4,-8,-9,8,-5,7,8,-10,9,2,-9,-6,-4,-10,-6,-10,7,9,-10,-10,-3,10,3,2,10,-9,-1,-1,-10,1,-7,-8,-10,2,4,-6,-9,8,-10,3,-6,-10,-9,-4,-10,-9,-6,5,4,10,9,4,-4,-1,-3,-4,-9,8,5,-1,4,6,-4,8,8,5,3,7,-2,-10,5,5,-10,5,4,-2,3,10,1,-9,-5,-8,6,6,4,-4,-1,4,-2,7,-5,6,-1,9,-4,10,-3,-8,4,6,9,8,8,1,2,-8,1,7,10,-1,-2,-2,1,-3,-3,2,10,-5,-3,10,6,-2,-4,8,-3,-6,4,-2,-9,8,8,7,-2,-6,-9,-2,-6,4,1,4,3,-1,-10,-9,-9,-1,1,-3,-10,-9,7,6,6,-7,-1,3,3,-2,6,-1,10,-2,-2,5,-5,-1,-10,10,-6,-2,-8,-3,-6,3,6,-9,-8,1,-7,1,5,-6,8,8,5,-3,5,-5,2,-5,3,-9,4,-10,6,-4,-3,5,-8,-7,3,7,9,8,-1,-2,-8,5,2,-2,-9,1,-7,-5,-7,10,-4,9,1,5,-2,-6,1,-2,-1,1,-3,9,-9,8,7,-8,-7,4,-4,-9,9,7,-9,3,7,7,6,-3,2,-1,-9,2,3,3,-9,6,-8,-8,-3,-8,-4,-4,4,-5,9,7,-2,6,-9,7], dtype = "uint64")#candidate|18093|(392,)|const|uint64
var_18094 = relay.var("var_18094", dtype = "float32", shape = (448,))#candidate|18094|(448,)|var|float32
call_18092 = relay.TupleGetItem(func_9335_call(relay.reshape(const_18093.astype('uint64'), [7, 8, 7]), relay.reshape(const_18093.astype('uint64'), [7, 8, 7]), relay.reshape(var_18094.astype('float32'), [448,]), ), 0)
call_18095 = relay.TupleGetItem(func_9340_call(relay.reshape(const_18093.astype('uint64'), [7, 8, 7]), relay.reshape(const_18093.astype('uint64'), [7, 8, 7]), relay.reshape(var_18094.astype('float32'), [448,]), ), 0)
output = relay.Tuple([uop_18060,call_18062,call_18078,var_18079,call_18092,const_18093,var_18094,])
output2 = relay.Tuple([uop_18060,call_18063,call_18080,var_18079,call_18095,const_18093,var_18094,])
func_18102 = relay.Function([var_18079,var_18094,], output)
mod['func_18102'] = func_18102
mod = relay.transform.InferType()(mod)
mutated_mod['func_18102'] = func_18102
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18102_call = mutated_mod.get_global_var('func_18102')
var_18104 = relay.var("var_18104", dtype = "float32", shape = (104, 28))#candidate|18104|(104, 28)|var|float32
var_18105 = relay.var("var_18105", dtype = "float32", shape = (448,))#candidate|18105|(448,)|var|float32
call_18103 = func_18102_call(var_18104,var_18105,)
output = call_18103
func_18106 = relay.Function([var_18104,var_18105,], output)
mutated_mod['func_18106'] = func_18106
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15598_call = mod.get_global_var('func_15598')
func_15600_call = mutated_mod.get_global_var('func_15600')
call_18126 = func_15598_call()
call_18127 = func_15598_call()
output = relay.Tuple([call_18126,])
output2 = relay.Tuple([call_18127,])
func_18130 = relay.Function([], output)
mod['func_18130'] = func_18130
mod = relay.transform.InferType()(mod)
output = func_18130()
func_18131 = relay.Function([], output)
mutated_mod['func_18131'] = func_18131
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14839_call = mod.get_global_var('func_14839')
func_14840_call = mutated_mod.get_global_var('func_14840')
call_18183 = func_14839_call()
call_18184 = func_14839_call()
var_18194 = relay.var("var_18194", dtype = "float64", shape = (2, 6, 11))#candidate|18194|(2, 6, 11)|var|float64
bop_18195 = relay.add(call_18183.astype('int16'), relay.reshape(var_18194.astype('int16'), relay.shape_of(call_18183))) # shape=(2, 6, 11)
bop_18198 = relay.add(call_18184.astype('int16'), relay.reshape(var_18194.astype('int16'), relay.shape_of(call_18184))) # shape=(2, 6, 11)
output = bop_18195
output2 = bop_18198
func_18200 = relay.Function([var_18194,], output)
mod['func_18200'] = func_18200
mod = relay.transform.InferType()(mod)
var_18201 = relay.var("var_18201", dtype = "float64", shape = (2, 6, 11))#candidate|18201|(2, 6, 11)|var|float64
output = func_18200(var_18201)
func_18202 = relay.Function([var_18201], output)
mutated_mod['func_18202'] = func_18202
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13753_call = mod.get_global_var('func_13753')
func_13755_call = mutated_mod.get_global_var('func_13755')
call_18207 = relay.TupleGetItem(func_13753_call(), 0)
call_18208 = relay.TupleGetItem(func_13755_call(), 0)
output = relay.Tuple([call_18207,])
output2 = relay.Tuple([call_18208,])
func_18210 = relay.Function([], output)
mod['func_18210'] = func_18210
mod = relay.transform.InferType()(mod)
output = func_18210()
func_18211 = relay.Function([], output)
mutated_mod['func_18211'] = func_18211
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13726_call = mod.get_global_var('func_13726')
func_13727_call = mutated_mod.get_global_var('func_13727')
call_18257 = relay.TupleGetItem(func_13726_call(), 0)
call_18258 = relay.TupleGetItem(func_13727_call(), 0)
func_18025_call = mod.get_global_var('func_18025')
func_18028_call = mutated_mod.get_global_var('func_18028')
var_18264 = relay.var("var_18264", dtype = "float32", shape = (264, 4))#candidate|18264|(264, 4)|var|float32
var_18265 = relay.var("var_18265", dtype = "float64", shape = (180,))#candidate|18265|(180,)|var|float64
call_18263 = relay.TupleGetItem(func_18025_call(relay.reshape(var_18264.astype('float32'), [16, 11, 6]), relay.reshape(var_18265.astype('float64'), [180,]), ), 4)
call_18266 = relay.TupleGetItem(func_18028_call(relay.reshape(var_18264.astype('float32'), [16, 11, 6]), relay.reshape(var_18265.astype('float64'), [180,]), ), 4)
func_254_call = mod.get_global_var('func_254')
func_257_call = mutated_mod.get_global_var('func_257')
const_18271 = relay.const([1.250213,-3.479704,7.466827,0.555536,-3.203417,-4.417447,-9.084872,5.251470,5.096273,0.072085,3.817176,0.929216], dtype = "float32")#candidate|18271|(12,)|const|float32
var_18272 = relay.var("var_18272", dtype = "uint16", shape = (75, 3))#candidate|18272|(75, 3)|var|uint16
call_18270 = relay.TupleGetItem(func_254_call(relay.reshape(const_18271.astype('float32'), [1, 3, 4]), relay.reshape(var_18272.astype('uint16'), [225,]), ), 3)
call_18273 = relay.TupleGetItem(func_257_call(relay.reshape(const_18271.astype('float32'), [1, 3, 4]), relay.reshape(var_18272.astype('uint16'), [225,]), ), 3)
output = relay.Tuple([call_18257,call_18263,var_18264,var_18265,call_18270,const_18271,var_18272,])
output2 = relay.Tuple([call_18258,call_18266,var_18264,var_18265,call_18273,const_18271,var_18272,])
func_18278 = relay.Function([var_18264,var_18265,var_18272,], output)
mod['func_18278'] = func_18278
mod = relay.transform.InferType()(mod)
mutated_mod['func_18278'] = func_18278
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18278_call = mutated_mod.get_global_var('func_18278')
var_18280 = relay.var("var_18280", dtype = "float32", shape = (264, 4))#candidate|18280|(264, 4)|var|float32
var_18281 = relay.var("var_18281", dtype = "float64", shape = (180,))#candidate|18281|(180,)|var|float64
var_18282 = relay.var("var_18282", dtype = "uint16", shape = (75, 3))#candidate|18282|(75, 3)|var|uint16
call_18279 = func_18278_call(var_18280,var_18281,var_18282,)
output = call_18279
func_18283 = relay.Function([var_18280,var_18281,var_18282,], output)
mutated_mod['func_18283'] = func_18283
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13965_call = mod.get_global_var('func_13965')
func_13966_call = mutated_mod.get_global_var('func_13966')
call_18313 = relay.TupleGetItem(func_13965_call(), 0)
call_18314 = relay.TupleGetItem(func_13966_call(), 0)
func_12272_call = mod.get_global_var('func_12272')
func_12274_call = mutated_mod.get_global_var('func_12274')
const_18360 = relay.const([2,-10,-8,-5,-1,9,6,9,9,10,6,8,6,-3,6,3,-9,2,-3,-8,9,-10,1,-7,-7,-4,6,1,9,-6,-1,-2,1,-8,9,1,-5,-3,2,9,-8,2,-6,-3,10,2,8,4,8,-4,-7,-6,-5,9,10,7,-2,9,-4,6,4,7,-2,9,-2,8,7,-2,-5,-10,-10,3,5,-1,-6,3,5,-2,-1,-8,6,-2,1,5,-6,3,1,-9,9,5,7,5,-10,-10,10,3,5,8,9,6,-10,3,-4,-10,-2,-10,5,-10,4,5,9,9,3,-2,3,-8,-6,8,3,4,-3,4,-10,2,-6,8,-4,1,-6,-8,10,4,8,9,10,-7,-8,10,9,1,-8,3,8,9,-5,-3,-6,-5,8,6,-7,-10,5,-2,3,-10,-4,5,4,-4,-3,-8,-3,-1,-6,1,-9,-6,-3,1,-2,7,5,-8,5,10,6,-7,2,1,7,1,3,2,-6,1,3,5,-1,-7,-4,6,-6,10,1,5,-5,3,6,3,-8,3,4,9,3,-4,6,9,-3,1,-2,1,5,-5,-9,2,-7,-1,2,-8,8,2,-10,-6,-1,6,-3,3,10,8,8,-9,4,-6,1,-3,-6,3,-5,-10,7,-10,-2,10,-2,-3,10,-5,-1,-3,7,-1,1,10,4,2,5,-2,6,-10,10,-9,5,-5,9,9,3,10,8,2,9,3,-8,2,7,-4,-3,-9,9,7,3,-5,-7,-4,4,-7,10,8,5,5,9,-2,4,-3,7,-2,-5,9,-1,-7,9,-7,-5,6,-2,3,2,-6,-7,1,8,-6,-2,4,-10,-6,8,5,-8,-3,-5,4,2,-4,-10,4,-10,-10,5,-6,9,-1,5,10,10,6,10,3,-9,-2,1,8,4,6,3,4,5,-9,-3,6,10,9,1,3,-6,-10,9,-2,5,2,-1,-8,-2,-9,-5,8,-6,-7,-6,8,5,3,-5,9,-3,5,-7,-2,-1,-4,5,-4,-7,-7,-1,-7,2,-2,-4,-4,2,-3,-4,8,4,-2,3,10,-6,3,10,6,1,-9,-9,-2,-2,-9,-7,-4,8,10,1,-1,4,6,7,8,-2,-1,-9,1,7,2,9,-5,-1,8,4,2,-5,-6,10,10,-2,-2,-5,4,5,8,-1,2,-1,-7,2,-2,6,1,3,-10,4,6,9,3,-6,-9,-7,1,1,-10,-5,-2,-4,9,-4,-10,2,-8,-6,4,-4,-8,-2,-9,-7,8,3,3,10,-5,-10,3,-3,-3,-1,-2,8,6,-1,4,5,-7,1,8,-1,-8,-9,5,1,10,2,9,-4,-1,9,10,-9,-2,9,4,2,5,2,-3,5,-4,-5,-9,7,3,-7,-2,2,-9,-6,4,-4,1,-6,-8,8,-8,-5,2,-6,10,10,2,-7,-4,3,-3,5,-4,6,2,3,9,-8,2,7,-9,-5,8,1,5,8,-10,9,5,-5,-9,8,8,10,2,-3,2,-4,-8,-2,9,-8,-4,3,4,6,-8,-3,2,8,9,-9,-7,-3,5,9,-5,5,6,9,-7,5,-1,4,2,-1,3,-3,-10,7,-10,-1,5,-4,-5,-3,8,-8,8,4,3,-2,3,7,2,1,2,6,-10,-10,-3,-7,-1,-2,8,9,-9,-6,-6,8,-10,-9,4,10,8,-9,5,6,3,-4,-1,-2,6,5,-4,-10,-5,-5,-6,3,6,-9,-9,6,-2,-5,-7,-5,7,-5,-4,-3,5,8,-4,-9,2,-3,4,5,2,-9,8,-2,-6,4,-3,1,-7,-3,-9,-3,-2,-3,8,2,-9,8,3,-10,6,-10,-5,1,7,4,8,-6,6,9,-9,-1,-2,-6,9,-5,-2,-8,-4,-8,4,-7,-1,-7,6,10,-6,2,2,-2,-3,-5,-10,3,-1,6,-5,10,-10,3,-2,9,-6,6,10,6,-5,-10,6,-10,8,-4,1,-9,10,4,4,2,6,-7,-5,2,6,8,7,10,-6,-8,-10,-7,-8,-4,6,-4,3,-9,-2,10,-2,1,6,5,-6,10,-10,8,-8,2,-10,8,-6,4,9,10,-4,-3,10,4,-2,4,1,-2,8,-5,-10,4,2,-6,3,4,-6,-8,6,-4,6,2,4,6,-8,10,6,4,3,-8,-5,-4,9,7,5,6,3,-1,-2,9,-10,5,-5,3,-8,-4,3,-6,-1,-10,6,10,-3,-8,-9,-4,8,-4,-10,-10,-10,-3,-4,7,-2,4,4,9,4,-4,-4,2,10,4,-5,-8,1,-7,-10,2,5,2,-7,-9,-8,-6,3,-4,-5,3,-3,4,4,-10,-10,-8,6,4,-3,-6,6,-3,1,-2,-6,-6,-9,4,2,10,6,-6,-10,-8,1,-3,-8,-6,2,5,4,-8,10,6,5,3,-6,6,9,-8,-9,-9,-5,-6,-2,6,2,7,-5,-5,9,-2,9,2,3,8,8,9,-2,-2,-7,10,-4,1,-10,-10,6,-5,-1,1,-4,3,6,-7,8,3,-2,7,10,5,-6,-10,-6,-5,1,-10,7,-10,9,3,1,-5,1,-6,1,2,6,-10,-6,-9,3,5,-7,2,2,-3,3,5,1,-4,5,-10,7,-3,-4,-1,4,-6,-1,-6,4,-8,-7,-3,-6,-9,-3,10,-10,3,7,-1,-2,-1,5,-7,-5,10,-10,10,-7,5,-9,-10,-9,-3,6,7,-2,10,6,-10,4,4,-2,8,-3,-9,-9,1,3,2,1,9,8,3,-7,-6,3,-5,-4,4,7,2,-6,3,9,9,7,-3,7,8,1,5,3,10,-2,-7,-2,4,-1,7,2,-2,-2,-3,-5,3,4,1,-9,-7,7,-1,-2,-7,1,5,-10,2,5,2,-8,-3,4,-2,-7,7,2,3,2,8,-5,-7,-3,-6,-6,-6,3,7,-5,2,9,-8,-7,6,2,-3,9,2,8,-10,-6,1,8,-9,-6,-7,-2,5,-5,-9,6,-5,-1,-7,-7,-7,5,-4,-5,-8,-6,5,1,9,2,-6,-1,5,10,-5,1,9,8,-9,-6,4,-5,10,-3,-3,-7,5,-1,-2,-2,-7,-6,7,10,9,-4,-10,3,6,-10,-1,9,7,-6,-9,5,-9,4,7,3,-2,10,-7,-3,-9,1,10,-7,8,-5,10,-4,-10,-7,2,2,9,7,5,7,1,-5,6,9,3,-4,3,-4,-6,-10,10,-4,6,-3,9,6,-9,-2,-10,10,6,-8,2,2,2,-6,-7,-1,2,-5,-5,-3,-1,1,8,7,-5,-3,-9,-5,-10,-5,-3,-10,-2,8,-8,-2,-7,-10,-4,1,6,-6,-10,7,-6,-6,1,-6,5,-8,6,-1,3,-10,-10,8,-6,2,7,-9,-2,-4,5,5,3,-2,-5,3,-2,-7,-7,-10,-9,-10,-10,1,-4,-6,-2,-8,4,7,-10,-9,5,-7,-1,5,7,-8,4,2,2,-8,1,-3,-5,6,9,10,-9,6,5,-10,5,-1,7,1,-3,6,-7,9,-9,9,-10,2,7,-9,-9,7,7,5,3,-3,-8,-10,-10,-9,6,7,-9,3,-8,10,-1,1], dtype = "uint16")#candidate|18360|(1350,)|const|uint16
call_18359 = relay.TupleGetItem(func_12272_call(relay.reshape(const_18360.astype('uint16'), [1350,])), 2)
call_18361 = relay.TupleGetItem(func_12274_call(relay.reshape(const_18360.astype('uint16'), [1350,])), 2)
output = relay.Tuple([call_18313,call_18359,const_18360,])
output2 = relay.Tuple([call_18314,call_18361,const_18360,])
func_18369 = relay.Function([], output)
mod['func_18369'] = func_18369
mod = relay.transform.InferType()(mod)
mutated_mod['func_18369'] = func_18369
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18369_call = mutated_mod.get_global_var('func_18369')
call_18370 = func_18369_call()
output = call_18370
func_18371 = relay.Function([], output)
mutated_mod['func_18371'] = func_18371
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12722_call = mod.get_global_var('func_12722')
func_12724_call = mutated_mod.get_global_var('func_12724')
call_18372 = func_12722_call()
call_18373 = func_12722_call()
func_16608_call = mod.get_global_var('func_16608')
func_16612_call = mutated_mod.get_global_var('func_16612')
var_18379 = relay.var("var_18379", dtype = "float32", shape = (264,))#candidate|18379|(264,)|var|float32
const_18380 = relay.const([9,-10,-2,-5,10,7,6,6,7,-8,-1,-7,-2,-6,2,7,-9,-2,-10,1,-9,-7,-8,-8,-1,3,7,10,8,-8,-3,-10,1,-1,-10,-9,3,-1,1,5,6,-1,-8,4,8,4,6,6,-9,8,-1,6,5,4,-9,-5,7,-9,8,10,-5,9,-2,7,-2,-1,-4,-9,-6,-4,-2,-1,-6,5,-2,-1,-9,8,-7,-3,2,4,-10,-4,5,-3,-8,7,3,-9,7,5,4,9,8,10,5,7,-6,4,-10,10,9,3,9,10,4,4,-9,-9,7,9,5,7,-7,-5,-8,-5,2,3,-10,1,-8,-3,-10,-6,-2,-8,10,-8,-8,6,-6,3,10,3,-8,-5,-9,-5,-1,-5,5,7,1,-4,8,3,4,-4,-1,-6,1,-7,-2,-1,-1,-5,2,-4,7,3,10,1,-3,6,-4,-5,6,5,-4,10,-5,-4,6,1,5,-1,10,-7,-9,-9,7,-5,-7,10,9,9,-6,-2,-2,-8,-6,2,-2,-9,3,-1,-1,5,1,9,9,5,-4,6,1,-3,-4,3,5,7,1,10,6,-9,-3,6,-10,-5,-9,10,-6,7,7,8,-3,10,2,-3,5,5,4,-10,-6,9,-8,5,4,-8,3,5,-8,7,4,10,6,9,-9,-6,-6,10,6,9,-1,-10,-2,10,9,2,9,-5,9,5,-3,-3,-6,4,-10,1,-10,6,8,-4,3,-2,-7,-5,3,4,-1,-4,2,8,-2,5,-3,-6,7,10,5,10,1,10,-7,7,-1,-4,2,7,4,6,1,8,9,7,10,-5,5,2,-10,-8,3,-6,-6,6,2,-5,3,2,1,-5,-7,1,-8,3,-5,10,3,-4,-8,-6,4,5,7,7,-7,1,5,-7,7,10,1,2,4,2,8,-4,1,8,-7,6,-9,1,8,-6,7,9,-4,9,-8,-3,9,9,-7,6,5,-9,8,10,-7,1,2,10,-2,5,-2,-8,-6,-10,5,-4,-9,-5,-4,-1,9,4,1,-7,-5,-2,-3,-7,-7,-9,-3,3,7,-7,10,1,-9,1,9,2,2,-10,-4,1,3,6,-4,-8,-4,1,2,-3,9,10,4,3,-5,1,9,3,-4,10,7,-9,2,6,4,-8,5,-10,-9,7,5,7,3,-9,-10,-5,6,9,5,-3], dtype = "int64")#candidate|18380|(448,)|const|int64
call_18378 = relay.TupleGetItem(func_16608_call(relay.reshape(var_18379.astype('float32'), [264,]), relay.reshape(const_18380.astype('int64'), [448,]), ), 0)
call_18381 = relay.TupleGetItem(func_16612_call(relay.reshape(var_18379.astype('float32'), [264,]), relay.reshape(const_18380.astype('int64'), [448,]), ), 0)
output = relay.Tuple([call_18372,call_18378,var_18379,const_18380,])
output2 = relay.Tuple([call_18373,call_18381,var_18379,const_18380,])
func_18387 = relay.Function([var_18379,], output)
mod['func_18387'] = func_18387
mod = relay.transform.InferType()(mod)
mutated_mod['func_18387'] = func_18387
mutated_mod = relay.transform.InferType()(mutated_mod)
var_18388 = relay.var("var_18388", dtype = "float32", shape = (264,))#candidate|18388|(264,)|var|float32
func_18387_call = mutated_mod.get_global_var('func_18387')
call_18389 = func_18387_call(var_18388)
output = call_18389
func_18390 = relay.Function([var_18388], output)
mutated_mod['func_18390'] = func_18390
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18210_call = mod.get_global_var('func_18210')
func_18211_call = mutated_mod.get_global_var('func_18211')
call_18410 = relay.TupleGetItem(func_18210_call(), 0)
call_18411 = relay.TupleGetItem(func_18211_call(), 0)
output = relay.Tuple([call_18410,])
output2 = relay.Tuple([call_18411,])
func_18414 = relay.Function([], output)
mod['func_18414'] = func_18414
mod = relay.transform.InferType()(mod)
mutated_mod['func_18414'] = func_18414
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18414_call = mutated_mod.get_global_var('func_18414')
call_18415 = func_18414_call()
output = call_18415
func_18416 = relay.Function([], output)
mutated_mod['func_18416'] = func_18416
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13429_call = mod.get_global_var('func_13429')
func_13431_call = mutated_mod.get_global_var('func_13431')
call_18435 = relay.TupleGetItem(func_13429_call(), 0)
call_18436 = relay.TupleGetItem(func_13431_call(), 0)
output = call_18435
output2 = call_18436
func_18437 = relay.Function([], output)
mod['func_18437'] = func_18437
mod = relay.transform.InferType()(mod)
output = func_18437()
func_18438 = relay.Function([], output)
mutated_mod['func_18438'] = func_18438
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12737_call = mod.get_global_var('func_12737')
func_12739_call = mutated_mod.get_global_var('func_12739')
call_18456 = func_12737_call()
call_18457 = func_12737_call()
output = call_18456
output2 = call_18457
func_18530 = relay.Function([], output)
mod['func_18530'] = func_18530
mod = relay.transform.InferType()(mod)
output = func_18530()
func_18531 = relay.Function([], output)
mutated_mod['func_18531'] = func_18531
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13965_call = mod.get_global_var('func_13965')
func_13966_call = mutated_mod.get_global_var('func_13966')
call_18550 = relay.TupleGetItem(func_13965_call(), 0)
call_18551 = relay.TupleGetItem(func_13966_call(), 0)
output = call_18550
output2 = call_18551
func_18562 = relay.Function([], output)
mod['func_18562'] = func_18562
mod = relay.transform.InferType()(mod)
output = func_18562()
func_18563 = relay.Function([], output)
mutated_mod['func_18563'] = func_18563
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14761_call = mod.get_global_var('func_14761')
func_14762_call = mutated_mod.get_global_var('func_14762')
call_18566 = relay.TupleGetItem(func_14761_call(), 0)
call_18567 = relay.TupleGetItem(func_14762_call(), 0)
func_15053_call = mod.get_global_var('func_15053')
func_15059_call = mutated_mod.get_global_var('func_15059')
const_18596 = relay.const([-6.071510,3.993900,4.383283,7.371121,-7.278677,-3.263495,-3.865389,7.589405,-2.501449,2.000594,-1.981378,6.712022,1.264072,-9.674012,9.918520,-9.498304,-5.041134,-5.514838,8.386517,-5.149735,4.222761,-2.688084,8.452928,9.078447,7.669636,4.379999,7.002221,5.051913,-9.730018,8.688496,5.120487,7.765543,-8.732761,-9.615694,5.037056,2.696322,3.895827,8.030730,-2.034436,-6.450527,1.719276,7.400727,-3.604999,-3.669351,-9.963957,5.915573,8.742975,0.841527,-9.461050,7.907894,7.054591,-9.110399,-8.663008,4.133052,-2.271497,0.805135,1.701158,-8.209914,0.763961,-8.943048,4.940197,-0.540009,2.715408,-3.139939,9.212465,7.320542,-3.282996,4.836274,8.365481,1.311900,-3.668212,-5.411318,-4.806415,-9.083174,9.729739,1.503253,-7.474940,2.545762,-6.639079,7.443590,-2.898509,-2.092192,7.689566,4.615568,-8.248540,-1.196713,6.786964,-6.235657,-0.363838,-2.731143,7.583744,-1.613858,3.441209,6.651298,3.166542,5.905679,-2.211852,-7.687687,7.205112,-8.216057,0.147729,-9.153638,2.260818,-4.596221,8.826878,1.108991,-9.999702,-7.576436,-1.009959,1.990012,6.914310,0.685261,-2.700538,5.215553,4.366948,3.440729,-3.383073,-2.838024,-7.297900,0.392905,3.681075,1.443960,-3.801119,6.321550,8.925790,-5.716542,2.188962,-1.320058,-3.949867,3.152518,-8.043850,-7.095756,-4.931839,-8.123969,4.375091,8.406220,2.368149,-0.647439,-7.615561,-6.587435,1.931529,-1.264172,-3.477862,-8.043009,-6.269922,-8.505249,5.566781,-1.228280,3.571494,-2.564664,-9.701743,3.698100,-9.418675,-8.454997,0.554280,7.293614,4.679805,0.220847,-1.903285,-6.876154,0.106429,0.756369,7.493907,8.720062,1.514331,5.320338,2.062730,7.391446,1.884373,-0.968919,-0.357849,8.117761,-8.431676,3.852085,-1.308711,6.735673,-7.890137,-3.211747,-5.222977,4.793169,-8.802304,-1.807008,1.462384,1.246475,2.764733,-7.704922,5.446020,8.031261,-0.586316,4.339401,8.182551,2.979122,9.824041,8.415336,0.895293,4.030545,-5.845521,9.537988,7.866755,-0.551620,-0.866091,-9.279169,-3.303758,4.307819,-0.975502,1.108369,-9.351103,-0.024165,9.778082,0.945233,-1.700830,-3.411157,-2.693416,-5.239569,-0.822667,-8.945661,1.281996,3.450165,4.706596,5.534212,7.683131,5.159738,1.333352,4.204198,3.590862,7.901170,-1.182411,-6.853015,6.516374,-4.875167,8.598527,-7.141385,-6.374113,-0.129817,5.352630,2.417323,2.444837,-8.795768,-1.025153,9.142534,-7.796533,8.422247,-4.509039,-4.223283,6.649461,9.067776,6.720330,1.287667,0.732835,2.698376,1.788630,7.719270,2.331506,2.759065,-3.748291,-0.178556,1.602051,1.019759,1.012942,3.143507,-9.505121,-6.927584,7.216033,5.295262], dtype = "float32")#candidate|18596|(264,)|const|float32
const_18597 = relay.const([6,4,1,-4,-10,9,10,9,-10,7,-5,5,-8,-6,9,-6,7,-10,8,5,4,-9,-2,4,-9,1,1,5,4,-2,-7,7,8,2,5,4,-5,-6,5,8,-10,5,-6,-3,-4,-1,-1,6,-10,-5,-8,-6,4,-10,1,3,9,-3,10,5,-8,4,-7,-9,1,-3,5,-3,-1,-9,3,4,-10,8,2,4,10,-1,10,-5,8,-9,-7,-3,5,1,-6,3,1,-5,-7,-6,7,-5,1,-6,-7,-1,7,-3,10,4,8,-1,3,5,-3,6,-8,6,10,-8,7,1,5,-10,-7,-10,-4,-7,7,6,3,-9,-4,2,-9,10,2,-1,7,-2,8,1,-1,8,2,-7,5,-8,2,-2,4,8,5,-3,-3,-7,6,-2,8,-6,-3,7,-10,-6,9,-5,9,-7,5,5,4,8,1,9,-1,2,-8,1,-6,-4,4,-5,3,5,3,-5,-3,-9,4,-6,2,6,-6,10,5,-4,3,9,-3,-5,6,5,2,6,3,10,9,-7,-4,-5,-1,5,-8,2,-3,-10,-9,-10,9,9,-9,7,-5,-3,1,8,-8,-8,1,10,8,-3,-4,-10,-1,5,7,10,-8,1,-2,3,-5,-8,2,-10,-9,9,-8,-6,-5,-10,7,-4,-4,6,7,-8,2,-1,-6,-5,6,8,-3,6,9,2,-8,1,-3,-10,6,-3,3,-3,6,4,3,7,-8,6,9,-3,2,10,3,-6,-9,-9,2,1,-1,-10,-9,-2,10,-4,4,7,-3,3,-9,9,7,-10,10,-7,-10,-7,3,-6,5,-3,1,-7,1,2,-9,9,9,-5,3,-3,-10,-2,10,-8,-1,-6,-5,9,-4,-7,4,-1,5,3,9,-3,-6,1,-6,-1,-10,-9,1,-10,-1,-10,-10,7,8,-5,5,5,4,7,5,-7,6,-9,-6,-4,7,-1,4,4,7,8,-9,3,-8,-5,10,-9,2,3,-8,-6,-10,2,6,-7,-7,-6,9,2,-2,2,1,-6,9,10,6,-2,4,10,2,-10,2,7,-7,-9,-8,-9,-10,1,-6,-7,-8,7,-5,-9,-2,-3,-6,6,-9,-2,-3,5,8,5,8,4,-2,-7,8,1,-6,-4,7,6,4,3,1,-5,8,2,-1,-2,-9,-10,-5,-7,-5,3,-3,-8,-1,6,-2,10,8,-6], dtype = "int64")#candidate|18597|(448,)|const|int64
var_18598 = relay.var("var_18598", dtype = "int8", shape = (1260,))#candidate|18598|(1260,)|var|int8
var_18599 = relay.var("var_18599", dtype = "uint64", shape = (1320,))#candidate|18599|(1320,)|var|uint64
call_18595 = relay.TupleGetItem(func_15053_call(relay.reshape(const_18596.astype('float32'), [264,]), relay.reshape(const_18597.astype('int64'), [224, 2]), relay.reshape(var_18598.astype('int8'), [1260,]), relay.reshape(var_18599.astype('uint64'), [1320,]), ), 8)
call_18600 = relay.TupleGetItem(func_15059_call(relay.reshape(const_18596.astype('float32'), [264,]), relay.reshape(const_18597.astype('int64'), [224, 2]), relay.reshape(var_18598.astype('int8'), [1260,]), relay.reshape(var_18599.astype('uint64'), [1320,]), ), 8)
uop_18603 = relay.acos(call_18595.astype('float64')) # shape=(132, 2)
uop_18605 = relay.acos(call_18600.astype('float64')) # shape=(132, 2)
output = relay.Tuple([call_18566,const_18596,const_18597,var_18598,var_18599,uop_18603,])
output2 = relay.Tuple([call_18567,const_18596,const_18597,var_18598,var_18599,uop_18605,])
func_18616 = relay.Function([var_18598,var_18599,], output)
mod['func_18616'] = func_18616
mod = relay.transform.InferType()(mod)
var_18617 = relay.var("var_18617", dtype = "int8", shape = (1260,))#candidate|18617|(1260,)|var|int8
var_18618 = relay.var("var_18618", dtype = "uint64", shape = (1320,))#candidate|18618|(1320,)|var|uint64
output = func_18616(var_18617,var_18618,)
func_18619 = relay.Function([var_18617,var_18618,], output)
mutated_mod['func_18619'] = func_18619
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17414_call = mod.get_global_var('func_17414')
func_17416_call = mutated_mod.get_global_var('func_17416')
call_18675 = func_17414_call()
call_18676 = func_17414_call()
func_14248_call = mod.get_global_var('func_14248')
func_14249_call = mutated_mod.get_global_var('func_14249')
call_18683 = relay.TupleGetItem(func_14248_call(), 3)
call_18684 = relay.TupleGetItem(func_14249_call(), 3)
output = relay.Tuple([call_18675,call_18683,])
output2 = relay.Tuple([call_18676,call_18684,])
func_18688 = relay.Function([], output)
mod['func_18688'] = func_18688
mod = relay.transform.InferType()(mod)
mutated_mod['func_18688'] = func_18688
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18688_call = mutated_mod.get_global_var('func_18688')
call_18689 = func_18688_call()
output = call_18689
func_18690 = relay.Function([], output)
mutated_mod['func_18690'] = func_18690
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18530_call = mod.get_global_var('func_18530')
func_18531_call = mutated_mod.get_global_var('func_18531')
call_18757 = func_18530_call()
call_18758 = func_18530_call()
output = call_18757
output2 = call_18758
func_18767 = relay.Function([], output)
mod['func_18767'] = func_18767
mod = relay.transform.InferType()(mod)
output = func_18767()
func_18768 = relay.Function([], output)
mutated_mod['func_18768'] = func_18768
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14965_call = mod.get_global_var('func_14965')
func_14967_call = mutated_mod.get_global_var('func_14967')
call_18769 = relay.TupleGetItem(func_14965_call(), 0)
call_18770 = relay.TupleGetItem(func_14967_call(), 0)
output = relay.Tuple([call_18769,])
output2 = relay.Tuple([call_18770,])
func_18774 = relay.Function([], output)
mod['func_18774'] = func_18774
mod = relay.transform.InferType()(mod)
mutated_mod['func_18774'] = func_18774
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18774_call = mutated_mod.get_global_var('func_18774')
call_18775 = func_18774_call()
output = call_18775
func_18776 = relay.Function([], output)
mutated_mod['func_18776'] = func_18776
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16689_call = mod.get_global_var('func_16689')
func_16691_call = mutated_mod.get_global_var('func_16691')
call_18777 = func_16689_call()
call_18778 = func_16689_call()
uop_18802 = relay.tan(call_18777.astype('float64')) # shape=(2, 600)
uop_18804 = relay.tan(call_18778.astype('float64')) # shape=(2, 600)
output = relay.Tuple([uop_18802,])
output2 = relay.Tuple([uop_18804,])
func_18815 = relay.Function([], output)
mod['func_18815'] = func_18815
mod = relay.transform.InferType()(mod)
mutated_mod['func_18815'] = func_18815
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18815_call = mutated_mod.get_global_var('func_18815')
call_18816 = func_18815_call()
output = call_18816
func_18817 = relay.Function([], output)
mutated_mod['func_18817'] = func_18817
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14445_call = mod.get_global_var('func_14445')
func_14446_call = mutated_mod.get_global_var('func_14446')
call_18829 = relay.TupleGetItem(func_14445_call(), 1)
call_18830 = relay.TupleGetItem(func_14446_call(), 1)
var_18859 = relay.var("var_18859", dtype = "uint16", shape = (10, 10, 12))#candidate|18859|(10, 10, 12)|var|uint16
bop_18860 = relay.less_equal(call_18829.astype('bool'), relay.reshape(var_18859.astype('bool'), relay.shape_of(call_18829))) # shape=(10, 10, 12)
bop_18863 = relay.less_equal(call_18830.astype('bool'), relay.reshape(var_18859.astype('bool'), relay.shape_of(call_18830))) # shape=(10, 10, 12)
output = bop_18860
output2 = bop_18863
F = relay.Function([var_18859,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_18859,], output2)
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
