import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_61 = relay.var("var_61", dtype = "int16", shape = (9, 13, 13))#candidate|61|(9, 13, 13)|var|int16
var_62 = relay.var("var_62", dtype = "int16", shape = (9, 13, 13))#candidate|62|(9, 13, 13)|var|int16
bop_63 = relay.not_equal(var_61.astype('bool'), relay.reshape(var_62.astype('bool'), relay.shape_of(var_61))) # shape=(9, 13, 13)
output = relay.Tuple([bop_63,])
output2 = relay.Tuple([bop_63,])
func_68 = relay.Function([var_61,var_62,], output)
mod['func_68'] = func_68
mod = relay.transform.InferType()(mod)
mutated_mod['func_68'] = func_68
mutated_mod = relay.transform.InferType()(mutated_mod)
func_68_call = mutated_mod.get_global_var('func_68')
var_70 = relay.var("var_70", dtype = "int16", shape = (9, 13, 13))#candidate|70|(9, 13, 13)|var|int16
var_71 = relay.var("var_71", dtype = "int16", shape = (9, 13, 13))#candidate|71|(9, 13, 13)|var|int16
call_69 = func_68_call(var_70,var_71,)
output = call_69
func_72 = relay.Function([var_70,var_71,], output)
mutated_mod['func_72'] = func_72
mutated_mod = relay.transform.InferType()(mutated_mod)
var_87 = relay.var("var_87", dtype = "int64", shape = (5, 10, 5))#candidate|87|(5, 10, 5)|var|int64
const_88 = relay.const([[[-1,6,-3,-10,-7],[-8,4,-10,9,-2],[7,-7,4,1,-1],[-7,-5,4,10,-3],[-10,6,10,-1,-4],[-7,-8,4,-10,-7],[7,-7,-9,-2,-3],[-7,-7,-7,1,-7],[-4,5,-7,-4,-5],[-9,-5,7,-7,4]],[[-4,-5,2,-8,-1],[-7,7,6,3,4],[1,10,-2,-1,-6],[1,3,-8,7,9],[1,4,8,-6,8],[-6,-3,-4,-5,-6],[-9,10,-2,-7,6],[-8,2,7,-9,-8],[2,5,-4,2,3],[10,-4,4,-1,-6]],[[8,6,-3,-7,-7],[-1,-1,-6,-7,-4],[-6,-2,7,8,-8],[-6,8,4,4,-6],[-8,-10,3,-4,2],[-1,-4,-1,-3,-10],[-3,5,8,-5,-5],[-3,-7,-4,7,-1],[7,9,8,-4,-1],[10,-3,-7,8,-5]],[[-2,6,9,10,-7],[7,4,5,6,-3],[-6,-2,1,1,-1],[2,5,3,-7,2],[-3,-8,-2,10,-6],[6,-7,-2,8,-8],[2,-2,-8,-2,7],[1,-10,-10,-3,4],[-5,-1,1,-1,-9],[-9,8,7,-8,1]],[[3,-7,2,-7,8],[-4,2,-5,1,3],[4,-2,-3,8,-9],[7,10,5,3,-7],[-3,-4,-10,-9,7],[-2,4,-3,2,8],[-2,-3,3,4,-10],[-7,-6,2,-1,7],[-5,-1,3,-3,7],[6,8,-2,5,-7]]], dtype = "int64")#candidate|88|(5, 10, 5)|const|int64
bop_89 = relay.less_equal(var_87.astype('bool'), relay.reshape(const_88.astype('bool'), relay.shape_of(var_87))) # shape=(5, 10, 5)
var_102 = relay.var("var_102", dtype = "int64", shape = (5, 10, 5))#candidate|102|(5, 10, 5)|var|int64
bop_103 = relay.power(const_88.astype('float32'), relay.reshape(var_102.astype('float32'), relay.shape_of(const_88))) # shape=(5, 10, 5)
func_68_call = mod.get_global_var('func_68')
func_72_call = mutated_mod.get_global_var('func_72')
var_116 = relay.var("var_116", dtype = "int16", shape = (1521,))#candidate|116|(1521,)|var|int16
call_115 = relay.TupleGetItem(func_68_call(relay.reshape(var_116.astype('int16'), [9, 13, 13]), relay.reshape(var_116.astype('int16'), [9, 13, 13]), ), 0)
call_117 = relay.TupleGetItem(func_72_call(relay.reshape(var_116.astype('int16'), [9, 13, 13]), relay.reshape(var_116.astype('int16'), [9, 13, 13]), ), 0)
output = relay.Tuple([bop_89,bop_103,call_115,var_116,])
output2 = relay.Tuple([bop_89,bop_103,call_117,var_116,])
func_118 = relay.Function([var_87,var_102,var_116,], output)
mod['func_118'] = func_118
mod = relay.transform.InferType()(mod)
mutated_mod['func_118'] = func_118
mutated_mod = relay.transform.InferType()(mutated_mod)
func_118_call = mutated_mod.get_global_var('func_118')
var_120 = relay.var("var_120", dtype = "int64", shape = (5, 10, 5))#candidate|120|(5, 10, 5)|var|int64
var_121 = relay.var("var_121", dtype = "int64", shape = (5, 10, 5))#candidate|121|(5, 10, 5)|var|int64
var_122 = relay.var("var_122", dtype = "int16", shape = (1521,))#candidate|122|(1521,)|var|int16
call_119 = func_118_call(var_120,var_121,var_122,)
output = call_119
func_123 = relay.Function([var_120,var_121,var_122,], output)
mutated_mod['func_123'] = func_123
mutated_mod = relay.transform.InferType()(mutated_mod)
var_163 = relay.var("var_163", dtype = "float32", shape = (12, 3, 2))#candidate|163|(12, 3, 2)|var|float32
uop_164 = relay.asinh(var_163.astype('float32')) # shape=(12, 3, 2)
func_118_call = mod.get_global_var('func_118')
func_123_call = mutated_mod.get_global_var('func_123')
var_170 = relay.var("var_170", dtype = "int64", shape = (25, 10))#candidate|170|(25, 10)|var|int64
const_171 = relay.const([[-6,-6,2,-5,4,-3,5,-2,-4,-3,2,-9,-8,6,3,-6,-1,-9,8,7,2,-10,6,3,9,-4,3,-4,4,-10,10,-10,-8,-1,5,-8,-10,3,10,-7,3,2,7,-8,7,-2,5,9,2,-8,10,5,6,-5,5,7,-3,5,-4,3,-2,2,4,1,-3,-5,6,-4,-8,-9,3,3,5,-6,-3,-4,-3,-6,-8,-4,-7,4,1,-8,-9,3,4,-7,-6,-10,1,7,10,10,-10,9,-5,3,-2,-4,7,-10,5,-10,10,1,-1,7,2,9,4,-9,2,-5,-2,-7,8,10,5,-4,7,8,6,1,-3,-9,-10,-5,2,-9,9,-3,-3,10,-10,-7,-10,7,10,-3,10,-1,-4,-5,6,-3,1,-2,1,-6,-4,10,-8,1,4,-5,8,5,2,-10,-5,3,-9,2,-7,-10,1,-7,8,-9,2,9,9,3,5,8,-4,-5,6,-4,-6,-5,6,-6,-10,7,8,-3,9,6,9,3,7,-8,-9,-7,9,-2,4,1,4,7,3,10,-5,-5,2,-8,8,-3,10,-2,2,6,-5,-7,5,4,3,10,-10,-4,3,-5,-8,9,-8,9,-8,-3,1,3,-5,4,9,-10,8,-5,-4,5,-9,-1,7,7,6,8,4,-5,-6,-9,-2,-8,-10,1,-1,9,-3,7,2,-5,5,-6,-5,-10,-10,8,7,-2,8,5,2,-9,4,-2,1,-3,-1,5,-1,-6,3,1,-9,1,8,9,9,2,-6,-10,-4,-5,-3,8,7,-5,8,-4,-8,-6,-10,6,-5,-5,-5,-9,-7,1,-5,5,2,4,-5,9,-3,2,2,-3,6,-9,2,-7,2,-10,-6,-1,-7,10,-3,-7,-8,10,-5,-8,-10,2,-4,-10,7,-5,6,-3,5,5,6,4,9,5,-6,6,9,7,-7,2,-8,-6,5,7,7,-7,2,-7,7,8,3,1,-4,-5,-7,4,6,-10,-1,10,-9,-9,10,5,-7,3,8,4,-4,2,8,9,-6,-4,7,5,2,-10,-1,2,-7,10,10,-7,4,8,-5,-5,-9,8,-4,-4,8,-1,-7,8,7,-1,-5,1,-8,-3,-7,4,9,2,6,10,-9,6,3,2,-4,-4,1,-8,4,2,2,-5,-9,-2,4,10,4,-9,-9,-6,-6,-4,6,6,5,-3,-3,6,7,8,4,5,3,5,-7,-7,-1,-9,-4,1,2,-6,4,8,2,3,1,5,3,8,-1,4,5,-3,10,-8,-7,7,8,3,1,-7,-5,8,2,-10,8,-7,9,4,3,2,-10,-3,6,10,3,10,10,10,2,7,5,-7,-3,4,4,-5,-4,-3,-6,8,10,1,-3,-6,-10,9,4,-10,6,2,-7,-4,-7,1,-2,5,6,6,7,-6,-2,2,8,4,3,4,6,3,9,-9,5,-2,1,10,-7,-3,-1,8,7,5,-9,2,-1,1,10,-8,5,6,8,-2,-4,8,1,9,8,-10,5,4,-6,5,-4,-1,-6,5,-4,-1,-5,4,-4,8,6,-1,-9,-8,-10,2,-7,5,9,9,10,-2,8,-4,10,6,-7,9,-2,2,-2,-7,7,-4,5,-2,3,1,1,-6,7,-8,-1,-2,-6,6,-9,8,-9,4,6,-1,9,2,7,-10,-4,-9,-5,-9,-5,8,-9,2,1,-4,-2,-9,6,1,-1,-8,-1,-9,9,-9,2,8,6,-1,-6,7,9,8,-7,-1,-2,-3,-7,1,-10,-10,-10,6,-10,4,-4,-3,6,10,-2,10,-1,9,7,4,2,2,4,-7,-4,10,3,3,-5,-1,-8,-3,5,-9,-3,2,8,-7,-9,-7,-5,-3,10,-8,-2,4,-1,9,10,-10,10,10,3,10,-10,-9,2,5,-9,-9,-1,9,1,-10,5,-7,2,-2,-3,-1,9,-1,-9,5,9,-8,-8,-6,4,-1,8,3,5,6,-8,-2,4,-10,-10,-2,-8,1,5,6,-5,-8,4,2,-7,-7,5,3,-1,-4,-7,-9,-7,4,10,-3,6,-8,3,10,-10,6,-4,-7,-4,-5,-9,10,7,-10,-2,3,-6,-8,3,-10,5,-8,-7,-4,-6,-3,-5,3,-5,-8,7,4,-4,-6,-2,-8,4,-4,9,-3,-8,9,9,5,6,2,-7,-9,-1,-6,1,10,9,10,3,-4,2,-6,7,5,-5,5,5,2,8,9,-1,-7,-2,-8,-10,7,8,-1,5,6,-4,3,-6,-5,5,6,-4,6,-9,2,9,-1,5,1,9,3,8,-3,4,-1,-6,5,-9,8,9,7,-3,6,8,9,5,-3,1,9,5,-2,-6,-3,-10,-3,10,7,-6,-1,-8,-4,-6,8,-4,-3,-7,-2,-2,10,-5,-8,-2,-8,8,3,-4,1,-5,-7,5,1,-5,-7,-7,8,9,-9,-5,-9,8,8,-10,-4,-9,-7,-3,6,-1,-6,1,2,-3,3,10,10,-6,2,9,-3,10,-1,-8,2,4,-8,5,-9,3,-6,-5,-10,5,7,9,2,-9,4,-4,5,-6,4,-6,-10,4,1,4,-10,-5,-5,-6,6,2,1,8,-5,-2,8,10,7,5,5,9,-8,-2,-9,-10,2,-4,-7,2,7,-10,9,2,-6,-4,-8,-6,-5,9,-7,-6,-10,-5,-3,10,-8,-4,2,5,-4,-1,-9,-9,7,8,-7,-4,-7,6,3,-9,-6,-10,-8,6,-1,4,-4,-6,-1,7,-1,2,10,-5,4,6,6,8,-2,-7,3,-4,-4,-10,-5,2,-7,-3,2,10,3,-8,5,-2,-2,1,-10,-2,5,1,8,9,8,10,9,8,9,2,1,10,-5,-9,-6,-1,-3,-5,6,4,-6,-3,-8,9,-4,1,7,1,2,6,10,-1,2,6,9,-9,6,-10,-1,-2,-1,4,-4,-7,4,-8,-3,-1,-6,2,-5,-2,2,-7,-2,10,2,1,-9,-6,-4,-9,-3,1,-5,9,-3,-5,5,-8,1,-2,1,2,-2,3,3,2,-2,7,5,9,7,10,6,-8,-5,-9,-4,4,-9,1,-9,-8,-5,8,3,7,-1,-1,-5,3,9,-6,-3,8,-9,4,9,1,-10,-3,8,2,-9,8,2,-5,3,4,6,-10,9,5,9,-4,-6,-4,9,8,9,-1,7,-1,-9,-10,5,10,-5,3,-10,5,-4,-4,4,-8,-8,-5,-4,7,1,8,9,-1,-2,10,-9,-2,3,3,-8,4,1,10,6,-9,-7,5,7,-10,-10,3,-5,-2,8,10,8,1,3,-5,3,10,-2,-5,2,-8,-8,-4,5,-3,-3,9,9,1,3,3,-1,-5,-7,-4,10,1,-4,-10,1,1,8,-7,2,-9,5,3,6,-1,-10,1,-10,7,9,2,-3,-8,-5,-8,-5,5,8,8,-6,6,-5,-6,-3,-8,2,-6,4,-8,9,9,-2,3,-10,5,-1,2,1,-10,2,-9,-1,1,-1,6,4,3,2,5,9,8,2,6,1,-8,-8,-9,-3,4,-1,3,8,9,-4,-3,-6,-4,2,-2,8,8,-6,-2,-7,-3,9,-4,-2,8,-9,2,4,4,6,9,-5,-9,-3,-1,9,1,-10,8,7,-9,-9,-2,6,8,-3,7,5,-10,-9,1,7,-10,6,-8,-4,-9,-7,-5,-6,-5,10,-8,8,-3,1,6,5,-4,4,4,-10,-10,-6,1,5,-3,-10,10,-9,6,7,5,-10,5,-2,1,-3,-10,-5,1,9,-7,-4,-6,9,10,-5,-10,-7,-8,-5,2,9,7,3,6,-1,-10,9,8,9,6,7,1,-2,-3,-10,-4,-7,5,-8,-3,-1,6,10,-7,-5,4,-10,4,-4,10,-3,2,-5,1,5,4,8,5,-5,-8,-5,10,5,-9,4,10,-4,-7,-9,-4,-4,-10,8,10,-8,-4,9,2,2,3,-3,-3,-7,-7,9,-1,-10,3,8,1,-4,-3,-1,-8,-8,-8,8,-9,-10,-3,8,1,-7,-5,-10,3,3,8,10,-6,-1,-1,-8,3]], dtype = "int16")#candidate|171|(1, 1521)|const|int16
call_169 = relay.TupleGetItem(func_118_call(relay.reshape(var_170.astype('int64'), [5, 10, 5]), relay.reshape(var_170.astype('int64'), [5, 10, 5]), relay.reshape(const_171.astype('int16'), [1521,]), ), 0)
call_172 = relay.TupleGetItem(func_123_call(relay.reshape(var_170.astype('int64'), [5, 10, 5]), relay.reshape(var_170.astype('int64'), [5, 10, 5]), relay.reshape(const_171.astype('int16'), [1521,]), ), 0)
func_118_call = mod.get_global_var('func_118')
func_123_call = mutated_mod.get_global_var('func_123')
call_175 = relay.TupleGetItem(func_118_call(relay.reshape(call_169.astype('int64'), [5, 10, 5]), relay.reshape(call_169.astype('int64'), [5, 10, 5]), relay.reshape(const_171.astype('int16'), [1521,]), ), 2)
call_176 = relay.TupleGetItem(func_123_call(relay.reshape(call_169.astype('int64'), [5, 10, 5]), relay.reshape(call_169.astype('int64'), [5, 10, 5]), relay.reshape(const_171.astype('int16'), [1521,]), ), 2)
uop_180 = relay.cos(const_171.astype('float32')) # shape=(1, 1521)
output = relay.Tuple([uop_164,call_169,var_170,call_175,uop_180,])
output2 = relay.Tuple([uop_164,call_172,var_170,call_176,uop_180,])
func_183 = relay.Function([var_163,var_170,], output)
mod['func_183'] = func_183
mod = relay.transform.InferType()(mod)
mutated_mod['func_183'] = func_183
mutated_mod = relay.transform.InferType()(mutated_mod)
func_183_call = mutated_mod.get_global_var('func_183')
var_185 = relay.var("var_185", dtype = "float32", shape = (12, 3, 2))#candidate|185|(12, 3, 2)|var|float32
var_186 = relay.var("var_186", dtype = "int64", shape = (25, 10))#candidate|186|(25, 10)|var|int64
call_184 = func_183_call(var_185,var_186,)
output = call_184
func_187 = relay.Function([var_185,var_186,], output)
mutated_mod['func_187'] = func_187
mutated_mod = relay.transform.InferType()(mutated_mod)
var_313 = relay.var("var_313", dtype = "float64", shape = (9, 2, 14))#candidate|313|(9, 2, 14)|var|float64
uop_314 = relay.log(var_313.astype('float64')) # shape=(9, 2, 14)
bop_316 = relay.bitwise_xor(uop_314.astype('int32'), relay.reshape(var_313.astype('int32'), relay.shape_of(uop_314))) # shape=(9, 2, 14)
uop_320 = relay.atanh(bop_316.astype('float64')) # shape=(9, 2, 14)
bop_329 = relay.maximum(uop_314.astype('uint8'), relay.reshape(uop_320.astype('uint8'), relay.shape_of(uop_314))) # shape=(9, 2, 14)
func_68_call = mod.get_global_var('func_68')
func_72_call = mutated_mod.get_global_var('func_72')
var_333 = relay.var("var_333", dtype = "int16", shape = (1, 1521))#candidate|333|(1, 1521)|var|int16
call_332 = relay.TupleGetItem(func_68_call(relay.reshape(var_333.astype('int16'), [9, 13, 13]), relay.reshape(var_333.astype('int16'), [9, 13, 13]), ), 0)
call_334 = relay.TupleGetItem(func_72_call(relay.reshape(var_333.astype('int16'), [9, 13, 13]), relay.reshape(var_333.astype('int16'), [9, 13, 13]), ), 0)
uop_353 = relay.asinh(bop_329.astype('float32')) # shape=(9, 2, 14)
uop_357 = relay.atan(bop_329.astype('float64')) # shape=(9, 2, 14)
func_118_call = mod.get_global_var('func_118')
func_123_call = mutated_mod.get_global_var('func_123')
var_363 = relay.var("var_363", dtype = "int64", shape = (250,))#candidate|363|(250,)|var|int64
call_362 = relay.TupleGetItem(func_118_call(relay.reshape(var_363.astype('int64'), [5, 10, 5]), relay.reshape(var_363.astype('int64'), [5, 10, 5]), relay.reshape(call_332.astype('int16'), [1521,]), ), 0)
call_364 = relay.TupleGetItem(func_123_call(relay.reshape(var_363.astype('int64'), [5, 10, 5]), relay.reshape(var_363.astype('int64'), [5, 10, 5]), relay.reshape(call_332.astype('int16'), [1521,]), ), 0)
output = relay.Tuple([call_332,var_333,uop_353,uop_357,call_362,var_363,])
output2 = relay.Tuple([call_334,var_333,uop_353,uop_357,call_364,var_363,])
func_366 = relay.Function([var_313,var_333,var_363,], output)
mod['func_366'] = func_366
mod = relay.transform.InferType()(mod)
var_367 = relay.var("var_367", dtype = "float64", shape = (9, 2, 14))#candidate|367|(9, 2, 14)|var|float64
var_368 = relay.var("var_368", dtype = "int16", shape = (1, 1521))#candidate|368|(1, 1521)|var|int16
var_369 = relay.var("var_369", dtype = "int64", shape = (250,))#candidate|369|(250,)|var|int64
output = func_366(var_367,var_368,var_369,)
func_370 = relay.Function([var_367,var_368,var_369,], output)
mutated_mod['func_370'] = func_370
mutated_mod = relay.transform.InferType()(mutated_mod)
var_510 = relay.var("var_510", dtype = "int8", shape = (10, 1, 4))#candidate|510|(10, 1, 4)|var|int8
var_511 = relay.var("var_511", dtype = "int8", shape = (10, 10, 4))#candidate|511|(10, 10, 4)|var|int8
bop_512 = relay.minimum(var_510.astype('int8'), var_511.astype('int8')) # shape=(10, 10, 4)
bop_534 = relay.add(bop_512.astype('uint8'), relay.reshape(var_511.astype('uint8'), relay.shape_of(bop_512))) # shape=(10, 10, 4)
output = bop_534
output2 = bop_534
func_541 = relay.Function([var_510,var_511,], output)
mod['func_541'] = func_541
mod = relay.transform.InferType()(mod)
var_542 = relay.var("var_542", dtype = "int8", shape = (10, 1, 4))#candidate|542|(10, 1, 4)|var|int8
var_543 = relay.var("var_543", dtype = "int8", shape = (10, 10, 4))#candidate|543|(10, 10, 4)|var|int8
output = func_541(var_542,var_543,)
func_544 = relay.Function([var_542,var_543,], output)
mutated_mod['func_544'] = func_544
mutated_mod = relay.transform.InferType()(mutated_mod)
var_553 = relay.var("var_553", dtype = "float32", shape = (6, 1, 16))#candidate|553|(6, 1, 16)|var|float32
uop_554 = relay.sqrt(var_553.astype('float32')) # shape=(6, 1, 16)
func_541_call = mod.get_global_var('func_541')
func_544_call = mutated_mod.get_global_var('func_544')
var_565 = relay.var("var_565", dtype = "int8", shape = (40,))#candidate|565|(40,)|var|int8
const_566 = relay.const([9,-1,1,-2,-8,9,4,-8,4,8,7,5,-6,1,1,1,-6,-1,-6,-10,-7,-2,8,8,3,9,-7,-6,-3,8,7,-1,10,9,-6,2,7,-2,5,-9,7,8,4,-8,-1,8,6,10,-3,3,8,-1,-1,-2,-5,7,-10,-6,1,9,2,3,-9,5,-3,-9,4,-8,3,3,2,7,-9,4,9,-5,3,9,10,-3,-2,4,2,-3,1,-2,10,-4,-4,-8,-2,-4,-10,6,-4,-2,1,2,-9,8,-5,-2,-4,1,-5,-3,-3,-3,-9,-10,7,-1,10,-4,10,-9,-4,9,7,10,-10,-2,-9,3,-3,-2,7,-3,-7,-7,8,-4,-7,4,3,-8,6,-6,-5,2,-4,-2,-8,-1,9,1,-4,-2,8,-4,10,3,-4,-9,-8,6,-7,-6,-3,-9,-4,4,7,-6,-1,-3,-4,7,5,-6,-8,8,3,10,10,-2,2,-2,-9,-2,-1,-3,3,-5,-5,5,5,1,-7,6,2,4,2,-3,-4,-5,-3,-2,-8,7,7,-1,5,-10,4,-10,4,2,-9,8,1,-8,2,1,4,5,9,-4,7,7,-10,8,2,-9,-7,4,-8,2,-10,-2,-2,6,3,8,-3,-1,-3,-8,-3,5,4,7,10,4,6,-4,10,-2,1,-5,4,-1,9,9,4,1,3,-2,9,3,-9,-4,1,4,-3,-8,6,-3,9,-6,-7,-3,-5,3,8,-9,-7,7,-8,-9,3,9,9,6,-3,-2,-1,3,9,-2,-4,-5,-4,6,-5,-3,6,-10,4,-4,-8,9,1,-7,-6,7,-10,10,7,7,2,-10,2,5,6,4,8,-5,-3,-9,-3,-10,1,10,7,1,7,-10,-3,-6,-8,5,4,-5,4,8,2,-2,-2,-4,8,-10,7,6,7,-9,2,1,3,3,-9,5,-2,8,-9,-1,-6,-4,1,4,-9,4,-6,7,8,9,10,-1,-10,6,-9,-8,10,-9,1,-10,6,-4,-9,-4,-1,-4,-6,5,4,-9,10,2,-1,-10,6,-5,-4,-7,-9,7,5,-3,8,8], dtype = "int8")#candidate|566|(400,)|const|int8
call_564 = func_541_call(relay.reshape(var_565.astype('int8'), [10, 1, 4]), relay.reshape(const_566.astype('int8'), [10, 10, 4]), )
call_567 = func_541_call(relay.reshape(var_565.astype('int8'), [10, 1, 4]), relay.reshape(const_566.astype('int8'), [10, 10, 4]), )
output = relay.Tuple([uop_554,call_564,var_565,const_566,])
output2 = relay.Tuple([uop_554,call_567,var_565,const_566,])
func_575 = relay.Function([var_553,var_565,], output)
mod['func_575'] = func_575
mod = relay.transform.InferType()(mod)
mutated_mod['func_575'] = func_575
mutated_mod = relay.transform.InferType()(mutated_mod)
func_575_call = mutated_mod.get_global_var('func_575')
var_577 = relay.var("var_577", dtype = "float32", shape = (6, 1, 16))#candidate|577|(6, 1, 16)|var|float32
var_578 = relay.var("var_578", dtype = "int8", shape = (40,))#candidate|578|(40,)|var|int8
call_576 = func_575_call(var_577,var_578,)
output = call_576
func_579 = relay.Function([var_577,var_578,], output)
mutated_mod['func_579'] = func_579
mutated_mod = relay.transform.InferType()(mutated_mod)
var_744 = relay.var("var_744", dtype = "float32", shape = (11, 2, 10))#candidate|744|(11, 2, 10)|var|float32
var_745 = relay.var("var_745", dtype = "float32", shape = (11, 2, 10))#candidate|745|(11, 2, 10)|var|float32
bop_746 = relay.floor_mod(var_744.astype('float32'), relay.reshape(var_745.astype('float32'), relay.shape_of(var_744))) # shape=(11, 2, 10)
output = relay.Tuple([bop_746,])
output2 = relay.Tuple([bop_746,])
func_755 = relay.Function([var_744,var_745,], output)
mod['func_755'] = func_755
mod = relay.transform.InferType()(mod)
var_756 = relay.var("var_756", dtype = "float32", shape = (11, 2, 10))#candidate|756|(11, 2, 10)|var|float32
var_757 = relay.var("var_757", dtype = "float32", shape = (11, 2, 10))#candidate|757|(11, 2, 10)|var|float32
output = func_755(var_756,var_757,)
func_758 = relay.Function([var_756,var_757,], output)
mutated_mod['func_758'] = func_758
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1076 = relay.var("var_1076", dtype = "int16", shape = (6, 15, 2))#candidate|1076|(6, 15, 2)|var|int16
var_1077 = relay.var("var_1077", dtype = "int16", shape = (6, 15, 2))#candidate|1077|(6, 15, 2)|var|int16
bop_1078 = relay.bitwise_and(var_1076.astype('int16'), relay.reshape(var_1077.astype('int16'), relay.shape_of(var_1076))) # shape=(6, 15, 2)
var_1101 = relay.var("var_1101", dtype = "int16", shape = (6, 15, 2))#candidate|1101|(6, 15, 2)|var|int16
bop_1102 = relay.subtract(bop_1078.astype('float32'), relay.reshape(var_1101.astype('float32'), relay.shape_of(bop_1078))) # shape=(6, 15, 2)
uop_1107 = relay.sqrt(var_1076.astype('float32')) # shape=(6, 15, 2)
uop_1110 = relay.exp(uop_1107.astype('float32')) # shape=(6, 15, 2)
output = relay.Tuple([bop_1102,uop_1110,])
output2 = relay.Tuple([bop_1102,uop_1110,])
func_1112 = relay.Function([var_1076,var_1077,var_1101,], output)
mod['func_1112'] = func_1112
mod = relay.transform.InferType()(mod)
var_1113 = relay.var("var_1113", dtype = "int16", shape = (6, 15, 2))#candidate|1113|(6, 15, 2)|var|int16
var_1114 = relay.var("var_1114", dtype = "int16", shape = (6, 15, 2))#candidate|1114|(6, 15, 2)|var|int16
var_1115 = relay.var("var_1115", dtype = "int16", shape = (6, 15, 2))#candidate|1115|(6, 15, 2)|var|int16
output = func_1112(var_1113,var_1114,var_1115,)
func_1116 = relay.Function([var_1113,var_1114,var_1115,], output)
mutated_mod['func_1116'] = func_1116
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1514 = relay.var("var_1514", dtype = "float32", shape = (5, 13, 2))#candidate|1514|(5, 13, 2)|var|float32
uop_1515 = relay.sigmoid(var_1514.astype('float32')) # shape=(5, 13, 2)
output = uop_1515
output2 = uop_1515
func_1519 = relay.Function([var_1514,], output)
mod['func_1519'] = func_1519
mod = relay.transform.InferType()(mod)
mutated_mod['func_1519'] = func_1519
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1520 = relay.var("var_1520", dtype = "float32", shape = (5, 13, 2))#candidate|1520|(5, 13, 2)|var|float32
func_1519_call = mutated_mod.get_global_var('func_1519')
call_1521 = func_1519_call(var_1520)
output = call_1521
func_1522 = relay.Function([var_1520], output)
mutated_mod['func_1522'] = func_1522
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2036 = relay.const([[[2,1],[6,-8]],[[5,7],[-1,-9]],[[3,-5],[-10,4]],[[-2,-7],[-1,2]],[[-10,-1],[9,1]],[[7,1],[10,10]],[[-10,10],[-8,1]],[[5,7],[-10,-1]],[[-2,-7],[2,-8]]], dtype = "uint16")#candidate|2036|(9, 2, 2)|const|uint16
const_2037 = relay.const([[[-9,7],[7,8]],[[-10,10],[-1,9]],[[-4,-9],[-8,5]],[[-6,-2],[3,4]],[[-8,4],[10,-9]],[[-1,4],[9,1]],[[10,8],[-10,10]],[[9,2],[-6,8]],[[7,1],[3,10]]], dtype = "uint16")#candidate|2037|(9, 2, 2)|const|uint16
bop_2038 = relay.maximum(const_2036.astype('uint16'), relay.reshape(const_2037.astype('uint16'), relay.shape_of(const_2036))) # shape=(9, 2, 2)
output = relay.Tuple([bop_2038,])
output2 = relay.Tuple([bop_2038,])
func_2042 = relay.Function([], output)
mod['func_2042'] = func_2042
mod = relay.transform.InferType()(mod)
mutated_mod['func_2042'] = func_2042
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2042_call = mutated_mod.get_global_var('func_2042')
call_2043 = func_2042_call()
output = call_2043
func_2044 = relay.Function([], output)
mutated_mod['func_2044'] = func_2044
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2042_call = mod.get_global_var('func_2042')
func_2044_call = mutated_mod.get_global_var('func_2044')
call_2118 = relay.TupleGetItem(func_2042_call(), 0)
call_2119 = relay.TupleGetItem(func_2044_call(), 0)
uop_2120 = relay.log(call_2118.astype('float64')) # shape=(9, 2, 2)
uop_2122 = relay.log(call_2119.astype('float64')) # shape=(9, 2, 2)
func_575_call = mod.get_global_var('func_575')
func_579_call = mutated_mod.get_global_var('func_579')
const_2137 = relay.const([5.512584,7.903836,-4.273639,-8.259070,-1.749564,4.781950,4.498055,5.142741,-3.056956,6.560788,4.622574,-7.118803,-8.899269,-3.057939,4.634838,-8.445815,-8.889898,4.398040,8.053975,2.392724,6.209222,-8.577885,-4.232540,-1.254831,-6.959753,5.401599,-2.654889,7.191139,5.287815,-6.518666,0.904122,4.549673,2.525668,0.172121,3.168337,-8.764553,7.981399,9.557266,-1.388055,3.211306,9.826436,-4.836846,-3.437054,-3.067924,1.808879,-2.225231,4.948684,3.994037,-7.856448,7.599551,5.602511,6.000478,-0.135059,3.780283,-4.890933,1.071911,3.747634,0.580778,3.920542,3.923339,8.166683,-9.292965,-9.154413,8.813724,-4.938207,-6.599424,-3.569805,-4.120341,-9.258163,6.571986,-9.586425,-9.172116,1.770491,5.268561,5.619912,2.827557,-8.787768,3.731706,1.751114,-8.480408,2.245046,-8.212348,-1.426371,-7.492301,-5.594773,9.355961,-5.668281,-8.489994,-6.116874,-2.114483,8.105022,-0.272199,3.372003,-0.569637,-3.977641,-2.863784], dtype = "float32")#candidate|2137|(96,)|const|float32
const_2138 = relay.const([-4,7,9,10,8,-5,10,5,-2,6,10,-4,6,5,10,5,4,-8,6,6,-5,8,10,3,-4,5,-4,4,-2,-7,2,6,4,10,3,-3,-8,8,-4,-9], dtype = "int8")#candidate|2138|(40,)|const|int8
call_2136 = relay.TupleGetItem(func_575_call(relay.reshape(const_2137.astype('float32'), [6, 1, 16]), relay.reshape(const_2138.astype('int8'), [40,]), ), 1)
call_2139 = relay.TupleGetItem(func_579_call(relay.reshape(const_2137.astype('float32'), [6, 1, 16]), relay.reshape(const_2138.astype('int8'), [40,]), ), 1)
output = relay.Tuple([uop_2120,call_2136,const_2137,const_2138,])
output2 = relay.Tuple([uop_2122,call_2139,const_2137,const_2138,])
func_2145 = relay.Function([], output)
mod['func_2145'] = func_2145
mod = relay.transform.InferType()(mod)
mutated_mod['func_2145'] = func_2145
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2145_call = mutated_mod.get_global_var('func_2145')
call_2146 = func_2145_call()
output = call_2146
func_2147 = relay.Function([], output)
mutated_mod['func_2147'] = func_2147
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2042_call = mod.get_global_var('func_2042')
func_2044_call = mutated_mod.get_global_var('func_2044')
call_2165 = relay.TupleGetItem(func_2042_call(), 0)
call_2166 = relay.TupleGetItem(func_2044_call(), 0)
func_1112_call = mod.get_global_var('func_1112')
func_1116_call = mutated_mod.get_global_var('func_1116')
var_2174 = relay.var("var_2174", dtype = "int16", shape = (30, 6))#candidate|2174|(30, 6)|var|int16
call_2173 = relay.TupleGetItem(func_1112_call(relay.reshape(var_2174.astype('int16'), [6, 15, 2]), relay.reshape(var_2174.astype('int16'), [6, 15, 2]), relay.reshape(var_2174.astype('int16'), [6, 15, 2]), ), 1)
call_2175 = relay.TupleGetItem(func_1116_call(relay.reshape(var_2174.astype('int16'), [6, 15, 2]), relay.reshape(var_2174.astype('int16'), [6, 15, 2]), relay.reshape(var_2174.astype('int16'), [6, 15, 2]), ), 1)
output = relay.Tuple([call_2165,call_2173,var_2174,])
output2 = relay.Tuple([call_2166,call_2175,var_2174,])
func_2178 = relay.Function([var_2174,], output)
mod['func_2178'] = func_2178
mod = relay.transform.InferType()(mod)
mutated_mod['func_2178'] = func_2178
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2179 = relay.var("var_2179", dtype = "int16", shape = (30, 6))#candidate|2179|(30, 6)|var|int16
func_2178_call = mutated_mod.get_global_var('func_2178')
call_2180 = func_2178_call(var_2179)
output = call_2180
func_2181 = relay.Function([var_2179], output)
mutated_mod['func_2181'] = func_2181
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2042_call = mod.get_global_var('func_2042')
func_2044_call = mutated_mod.get_global_var('func_2044')
call_2188 = relay.TupleGetItem(func_2042_call(), 0)
call_2189 = relay.TupleGetItem(func_2044_call(), 0)
func_1519_call = mod.get_global_var('func_1519')
func_1522_call = mutated_mod.get_global_var('func_1522')
const_2191 = relay.const([[5.125617,5.849929,8.487971,-0.815847,-7.321546,-2.351917,-2.128159,-2.058117,8.686678,3.307097],[3.394063,3.174492,-4.783579,-9.612019,3.597557,-7.951353,8.103514,7.562904,-4.966986,3.118274],[0.401845,-5.286005,5.328314,6.768109,-0.471515,6.688450,5.792109,-8.488512,6.957742,-6.450666],[9.996739,4.089754,-8.343786,-7.271704,5.784415,-0.725229,8.693974,-1.951083,8.178201,4.736731],[-8.140137,1.873779,7.343168,5.820452,5.101148,4.847248,1.533360,4.305020,-5.311862,-6.409862],[6.175570,-3.647748,-2.892895,2.539570,-6.589781,5.139943,4.246118,-6.470499,0.106690,5.528622],[9.570603,5.137374,-9.717072,8.381144,-8.642535,-6.160008,-5.056063,4.845463,4.723486,-5.941638],[7.419999,-0.561652,5.340935,-5.550134,-2.749081,4.160742,-4.657498,-6.490707,3.728598,1.357618],[-8.617030,7.372172,3.491227,4.346601,9.545375,-9.744063,7.185105,9.482710,-5.192431,0.989966],[0.391129,-0.883644,-9.738560,-8.984464,-9.966155,7.499854,2.147500,9.354005,1.792993,8.940209],[1.288292,-2.722422,-0.705882,4.055344,0.399862,-5.922245,7.230926,-7.921169,7.002277,4.950788],[2.779191,-6.968143,1.626016,2.079740,-6.468292,1.087656,-6.754510,7.780392,1.546770,4.316425],[1.638928,5.153840,0.806862,-4.086878,8.499542,-2.644311,8.903997,1.718065,1.212762,5.655508]], dtype = "float32")#candidate|2191|(13, 10)|const|float32
call_2190 = func_1519_call(relay.reshape(const_2191.astype('float32'), [5, 13, 2]))
call_2192 = func_1519_call(relay.reshape(const_2191.astype('float32'), [5, 13, 2]))
output = relay.Tuple([call_2188,call_2190,const_2191,])
output2 = relay.Tuple([call_2189,call_2192,const_2191,])
func_2201 = relay.Function([], output)
mod['func_2201'] = func_2201
mod = relay.transform.InferType()(mod)
mutated_mod['func_2201'] = func_2201
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2201_call = mutated_mod.get_global_var('func_2201')
call_2202 = func_2201_call()
output = call_2202
func_2203 = relay.Function([], output)
mutated_mod['func_2203'] = func_2203
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2042_call = mod.get_global_var('func_2042')
func_2044_call = mutated_mod.get_global_var('func_2044')
call_2224 = relay.TupleGetItem(func_2042_call(), 0)
call_2225 = relay.TupleGetItem(func_2044_call(), 0)
output = call_2224
output2 = call_2225
func_2226 = relay.Function([], output)
mod['func_2226'] = func_2226
mod = relay.transform.InferType()(mod)
output = func_2226()
func_2227 = relay.Function([], output)
mutated_mod['func_2227'] = func_2227
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2245 = relay.var("var_2245", dtype = "float32", shape = (1, 14, 8))#candidate|2245|(1, 14, 8)|var|float32
uop_2246 = relay.cos(var_2245.astype('float32')) # shape=(1, 14, 8)
output = uop_2246
output2 = uop_2246
func_2248 = relay.Function([var_2245,], output)
mod['func_2248'] = func_2248
mod = relay.transform.InferType()(mod)
mutated_mod['func_2248'] = func_2248
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2249 = relay.var("var_2249", dtype = "float32", shape = (1, 14, 8))#candidate|2249|(1, 14, 8)|var|float32
func_2248_call = mutated_mod.get_global_var('func_2248')
call_2250 = func_2248_call(var_2249)
output = call_2250
func_2251 = relay.Function([var_2249], output)
mutated_mod['func_2251'] = func_2251
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2201_call = mod.get_global_var('func_2201')
func_2203_call = mutated_mod.get_global_var('func_2203')
call_2265 = relay.TupleGetItem(func_2201_call(), 2)
call_2266 = relay.TupleGetItem(func_2203_call(), 2)
output = call_2265
output2 = call_2266
func_2275 = relay.Function([], output)
mod['func_2275'] = func_2275
mod = relay.transform.InferType()(mod)
output = func_2275()
func_2276 = relay.Function([], output)
mutated_mod['func_2276'] = func_2276
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2042_call = mod.get_global_var('func_2042')
func_2044_call = mutated_mod.get_global_var('func_2044')
call_2300 = relay.TupleGetItem(func_2042_call(), 0)
call_2301 = relay.TupleGetItem(func_2044_call(), 0)
output = relay.Tuple([call_2300,])
output2 = relay.Tuple([call_2301,])
func_2304 = relay.Function([], output)
mod['func_2304'] = func_2304
mod = relay.transform.InferType()(mod)
mutated_mod['func_2304'] = func_2304
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2304_call = mutated_mod.get_global_var('func_2304')
call_2305 = func_2304_call()
output = call_2305
func_2306 = relay.Function([], output)
mutated_mod['func_2306'] = func_2306
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2145_call = mod.get_global_var('func_2145')
func_2147_call = mutated_mod.get_global_var('func_2147')
call_2313 = relay.TupleGetItem(func_2145_call(), 1)
call_2314 = relay.TupleGetItem(func_2147_call(), 1)
output = relay.Tuple([call_2313,])
output2 = relay.Tuple([call_2314,])
func_2316 = relay.Function([], output)
mod['func_2316'] = func_2316
mod = relay.transform.InferType()(mod)
output = func_2316()
func_2317 = relay.Function([], output)
mutated_mod['func_2317'] = func_2317
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2201_call = mod.get_global_var('func_2201')
func_2203_call = mutated_mod.get_global_var('func_2203')
call_2368 = relay.TupleGetItem(func_2201_call(), 0)
call_2369 = relay.TupleGetItem(func_2203_call(), 0)
func_2201_call = mod.get_global_var('func_2201')
func_2203_call = mutated_mod.get_global_var('func_2203')
call_2383 = relay.TupleGetItem(func_2201_call(), 0)
call_2384 = relay.TupleGetItem(func_2203_call(), 0)
func_2178_call = mod.get_global_var('func_2178')
func_2181_call = mutated_mod.get_global_var('func_2181')
const_2391 = relay.const([8,3,-5,4,10,-9,-3,1,-4,-7,-7,8,-5,9,7,-9,-7,6,7,9,-10,-10,-3,-4,-4,-7,-4,-6,-1,2,6,-2,-4,-7,10,10,8,-5,-1,-8,-8,7,-4,-4,-5,-1,-6,7,1,4,-2,3,4,-1,-5,-1,5,-8,10,-4,-8,9,-7,-5,10,2,-4,2,-3,3,1,4,2,7,-3,9,5,5,-4,-2,2,6,1,3,2,-5,-2,1,10,-7,6,-4,6,2,-2,2,-10,-1,8,-8,-2,5,1,-7,3,-6,10,9,3,-5,8,10,-8,1,-5,-6,2,-8,-7,-6,8,9,-3,-5,-2,1,10,7,2,-3,9,-3,-3,5,-7,2,4,7,-2,6,-5,-1,10,-10,-8,-1,-4,-7,5,-9,-5,-8,-2,8,7,5,1,-6,6,3,-9,-10,-9,10,-8,-6,9,2,1,3,-2,-2,8,3,-4,-7,-3,7,-3,5], dtype = "int16")#candidate|2391|(180,)|const|int16
call_2390 = relay.TupleGetItem(func_2178_call(relay.reshape(const_2391.astype('int16'), [30, 6])), 1)
call_2392 = relay.TupleGetItem(func_2181_call(relay.reshape(const_2391.astype('int16'), [30, 6])), 1)
output = relay.Tuple([call_2368,call_2383,call_2390,const_2391,])
output2 = relay.Tuple([call_2369,call_2384,call_2392,const_2391,])
func_2393 = relay.Function([], output)
mod['func_2393'] = func_2393
mod = relay.transform.InferType()(mod)
mutated_mod['func_2393'] = func_2393
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2393_call = mutated_mod.get_global_var('func_2393')
call_2394 = func_2393_call()
output = call_2394
func_2395 = relay.Function([], output)
mutated_mod['func_2395'] = func_2395
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2275_call = mod.get_global_var('func_2275')
func_2276_call = mutated_mod.get_global_var('func_2276')
call_2458 = func_2275_call()
call_2459 = func_2275_call()
output = call_2458
output2 = call_2459
func_2486 = relay.Function([], output)
mod['func_2486'] = func_2486
mod = relay.transform.InferType()(mod)
output = func_2486()
func_2487 = relay.Function([], output)
mutated_mod['func_2487'] = func_2487
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2226_call = mod.get_global_var('func_2226')
func_2227_call = mutated_mod.get_global_var('func_2227')
call_2532 = func_2226_call()
call_2533 = func_2226_call()
output = relay.Tuple([call_2532,])
output2 = relay.Tuple([call_2533,])
func_2545 = relay.Function([], output)
mod['func_2545'] = func_2545
mod = relay.transform.InferType()(mod)
output = func_2545()
func_2546 = relay.Function([], output)
mutated_mod['func_2546'] = func_2546
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2201_call = mod.get_global_var('func_2201')
func_2203_call = mutated_mod.get_global_var('func_2203')
call_2553 = relay.TupleGetItem(func_2201_call(), 2)
call_2554 = relay.TupleGetItem(func_2203_call(), 2)
output = call_2553
output2 = call_2554
func_2562 = relay.Function([], output)
mod['func_2562'] = func_2562
mod = relay.transform.InferType()(mod)
mutated_mod['func_2562'] = func_2562
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2562_call = mutated_mod.get_global_var('func_2562')
call_2563 = func_2562_call()
output = call_2563
func_2564 = relay.Function([], output)
mutated_mod['func_2564'] = func_2564
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2304_call = mod.get_global_var('func_2304')
func_2306_call = mutated_mod.get_global_var('func_2306')
call_2571 = relay.TupleGetItem(func_2304_call(), 0)
call_2572 = relay.TupleGetItem(func_2306_call(), 0)
var_2577 = relay.var("var_2577", dtype = "uint16", shape = (9, 2, 2))#candidate|2577|(9, 2, 2)|var|uint16
bop_2578 = relay.minimum(call_2571.astype('uint64'), relay.reshape(var_2577.astype('uint64'), relay.shape_of(call_2571))) # shape=(9, 2, 2)
bop_2581 = relay.minimum(call_2572.astype('uint64'), relay.reshape(var_2577.astype('uint64'), relay.shape_of(call_2572))) # shape=(9, 2, 2)
func_2316_call = mod.get_global_var('func_2316')
func_2317_call = mutated_mod.get_global_var('func_2317')
call_2592 = relay.TupleGetItem(func_2316_call(), 0)
call_2593 = relay.TupleGetItem(func_2317_call(), 0)
func_68_call = mod.get_global_var('func_68')
func_72_call = mutated_mod.get_global_var('func_72')
var_2610 = relay.var("var_2610", dtype = "int16", shape = (1521,))#candidate|2610|(1521,)|var|int16
call_2609 = relay.TupleGetItem(func_68_call(relay.reshape(var_2610.astype('int16'), [9, 13, 13]), relay.reshape(var_2610.astype('int16'), [9, 13, 13]), ), 0)
call_2611 = relay.TupleGetItem(func_72_call(relay.reshape(var_2610.astype('int16'), [9, 13, 13]), relay.reshape(var_2610.astype('int16'), [9, 13, 13]), ), 0)
func_2393_call = mod.get_global_var('func_2393')
func_2395_call = mutated_mod.get_global_var('func_2395')
call_2631 = relay.TupleGetItem(func_2393_call(), 3)
call_2632 = relay.TupleGetItem(func_2395_call(), 3)
output = relay.Tuple([bop_2578,call_2592,call_2609,var_2610,call_2631,])
output2 = relay.Tuple([bop_2581,call_2593,call_2611,var_2610,call_2632,])
func_2639 = relay.Function([var_2577,var_2610,], output)
mod['func_2639'] = func_2639
mod = relay.transform.InferType()(mod)
var_2640 = relay.var("var_2640", dtype = "uint16", shape = (9, 2, 2))#candidate|2640|(9, 2, 2)|var|uint16
var_2641 = relay.var("var_2641", dtype = "int16", shape = (1521,))#candidate|2641|(1521,)|var|int16
output = func_2639(var_2640,var_2641,)
func_2642 = relay.Function([var_2640,var_2641,], output)
mutated_mod['func_2642'] = func_2642
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2545_call = mod.get_global_var('func_2545')
func_2546_call = mutated_mod.get_global_var('func_2546')
call_2660 = relay.TupleGetItem(func_2545_call(), 0)
call_2661 = relay.TupleGetItem(func_2546_call(), 0)
uop_2664 = relay.atan(call_2660.astype('float32')) # shape=(9, 2, 2)
uop_2666 = relay.atan(call_2661.astype('float32')) # shape=(9, 2, 2)
func_183_call = mod.get_global_var('func_183')
func_187_call = mutated_mod.get_global_var('func_187')
const_2670 = relay.const([[-8.949618,-7.278978,-2.473500,-0.783887,-8.974524,-7.895726,4.312060,5.564763,-6.944031,-4.315735,-2.203227,-2.049052,1.038015,0.418826,-0.178239,7.576993,-8.176246,4.731251,-3.976781,8.647604,-3.636310,7.215670,7.557126,-9.276114],[-1.240347,-5.113821,-3.485688,-8.358355,6.348532,2.145858,3.909032,-0.095636,4.408655,2.161137,-9.581372,-9.038327,-1.736549,-4.860391,-7.994870,4.937472,2.937753,5.760153,7.961064,-8.881795,-6.601005,-2.613192,-4.482984,0.482566],[-1.467347,-0.950395,9.319411,9.462075,-5.613926,1.925061,-0.191741,-0.247207,-0.157030,-0.820990,8.956185,-3.222442,-7.206742,-2.704288,-6.013312,-5.667904,-0.837539,0.764164,0.734357,2.082712,-3.544287,-7.259732,3.546781,-8.932518]], dtype = "float32")#candidate|2670|(3, 24)|const|float32
const_2671 = relay.const([-3,4,6,-6,10,4,4,6,-5,-4,5,-4,7,1,2,2,6,5,-10,6,8,-7,2,-4,2,-3,-3,7,-8,5,-4,-5,3,-2,-10,-4,-10,3,-2,10,-4,-1,9,-8,-8,-9,2,-5,-6,7,-7,8,-9,1,7,-7,8,1,-8,6,-2,10,-1,-8,-4,-6,-5,10,5,-7,-7,-7,-4,10,-7,-10,3,4,7,-2,-8,-1,3,7,3,4,8,-4,-2,-6,3,10,8,-10,10,5,2,-1,7,5,-1,1,2,4,10,-3,-6,8,10,8,-10,8,-8,7,6,-7,-4,-8,4,10,-2,8,7,3,-2,9,-5,-3,5,-10,5,8,8,4,8,7,-9,9,10,5,-4,-5,-9,-3,10,7,-5,-3,-1,-4,-2,-10,-5,-9,2,9,6,6,-2,-2,-4,-8,-4,-1,-9,-5,-5,4,-5,-7,4,-2,9,8,6,-4,10,9,-10,-2,-5,-1,-3,4,-5,4,8,2,5,7,-1,-2,-2,7,-3,-2,-8,-9,-8,-9,-6,4,1,9,5,5,-8,9,2,-3,-6,3,8,5,5,-8,-6,-4,8,3,1,1,7,-9,-7,3,-7,-9,8,-2,-7,5,5,-2,-3,6,3,3,-7,-10,-5,10,-1,9,-3,4,1,5,9,9], dtype = "int64")#candidate|2671|(250,)|const|int64
call_2669 = relay.TupleGetItem(func_183_call(relay.reshape(const_2670.astype('float32'), [12, 3, 2]), relay.reshape(const_2671.astype('int64'), [25, 10]), ), 3)
call_2672 = relay.TupleGetItem(func_187_call(relay.reshape(const_2670.astype('float32'), [12, 3, 2]), relay.reshape(const_2671.astype('int64'), [25, 10]), ), 3)
func_2042_call = mod.get_global_var('func_2042')
func_2044_call = mutated_mod.get_global_var('func_2044')
call_2677 = relay.TupleGetItem(func_2042_call(), 0)
call_2678 = relay.TupleGetItem(func_2044_call(), 0)
func_2275_call = mod.get_global_var('func_2275')
func_2276_call = mutated_mod.get_global_var('func_2276')
call_2684 = func_2275_call()
call_2685 = func_2275_call()
func_2545_call = mod.get_global_var('func_2545')
func_2546_call = mutated_mod.get_global_var('func_2546')
call_2698 = relay.TupleGetItem(func_2545_call(), 0)
call_2699 = relay.TupleGetItem(func_2546_call(), 0)
output = relay.Tuple([uop_2664,call_2669,const_2670,const_2671,call_2677,call_2684,call_2698,])
output2 = relay.Tuple([uop_2666,call_2672,const_2670,const_2671,call_2678,call_2685,call_2699,])
func_2702 = relay.Function([], output)
mod['func_2702'] = func_2702
mod = relay.transform.InferType()(mod)
output = func_2702()
func_2703 = relay.Function([], output)
mutated_mod['func_2703'] = func_2703
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2731 = relay.var("var_2731", dtype = "uint32", shape = (3, 2, 14))#candidate|2731|(3, 2, 14)|var|uint32
const_2732 = relay.const([[[5,-5,4,1,8,3,5,-2,-8,10,-7,-1,-1,-10],[-1,1,1,-2,-7,-1,10,6,-10,2,3,9,6,-5]],[[-2,4,-6,-3,2,-1,8,-1,-8,6,5,7,1,-10],[-6,5,-7,-3,-3,-1,-4,1,4,2,1,3,9,4]],[[6,6,8,-1,-10,10,-3,-8,5,10,-1,3,-2,10],[6,3,9,-3,-1,-1,-9,6,-6,-10,2,-10,2,-9]]], dtype = "uint32")#candidate|2732|(3, 2, 14)|const|uint32
bop_2733 = relay.bitwise_or(var_2731.astype('uint32'), relay.reshape(const_2732.astype('uint32'), relay.shape_of(var_2731))) # shape=(3, 2, 14)
func_118_call = mod.get_global_var('func_118')
func_123_call = mutated_mod.get_global_var('func_123')
var_2753 = relay.var("var_2753", dtype = "int64", shape = (250,))#candidate|2753|(250,)|var|int64
const_2754 = relay.const([[-8,8,-3,8,-9,-1,-1,3,7,-9,-5,-6,1,-7,-7,-8,5,-8,3,4,-4,8,7,-1,-9,-9,-1,3,10,3,-1,4,-7,4,10,-3,3,2,-5,6,-5,2,1,6,-3,1,-1,10,9,1,-2,-4,8,-8,-10,8,-9,-1,-6,-4,-7,-5,-3,-10,2,2,6,10,-5,-10,3,10,10,4,10,7,6,8,8,2,9,-6,1,10,4,-10,-10,9,-4,4,-3,-1,-4,8,7,3,-3,3,-5,-1,5,-4,-4,2,7,1,-8,9,-1,5,-5,4,-7,4,-1,1,-8],[10,-9,1,-10,-4,-5,2,9,6,8,-4,8,-9,4,-5,-6,-4,7,8,8,-6,6,8,7,-1,-3,-2,-4,-2,-2,9,-1,-10,8,6,2,8,-1,-5,-2,3,-3,8,5,-4,-6,2,7,8,2,3,5,3,-10,4,7,9,10,9,-9,2,-7,-5,-8,2,-6,-3,-8,8,-9,2,-8,7,-2,5,9,-9,4,3,-4,2,-3,2,3,1,-10,9,-8,8,-3,1,2,2,-3,-6,1,-8,2,8,-8,9,-4,8,7,1,-10,-5,6,6,2,8,-9,10,4,1,6,2],[2,-3,-7,-8,1,-7,1,-6,-7,-6,9,-10,-3,9,-4,-1,-2,-5,3,3,-7,10,-6,-10,-9,9,-4,2,-1,9,1,-2,-6,-9,-10,-2,-5,-6,-7,3,-5,-3,-1,-6,-4,-10,7,-6,-8,-2,1,9,6,-6,6,-10,-10,-9,6,5,-2,-6,6,-2,9,7,9,6,3,-10,-1,-9,-3,-4,-8,10,-2,9,-10,-6,-4,-9,-9,10,-8,3,3,10,2,7,-3,-10,-3,4,-7,-4,-3,5,9,8,-8,-5,-4,-6,-9,6,10,-6,4,-10,-2,3,-7,-1,-6,2,-9],[6,3,2,7,-5,-4,3,3,-1,6,-4,4,9,-4,5,-7,-9,-7,4,8,2,-10,-2,-6,2,8,-7,9,2,5,9,2,-4,-10,2,10,2,7,-7,-8,7,2,6,-9,7,10,8,7,-1,-4,4,5,4,-1,-6,-9,-3,-6,4,-9,-9,-8,-9,3,-9,2,-9,-1,-8,-7,9,7,6,-1,1,9,7,1,2,7,-10,-7,6,5,10,10,5,1,5,10,-2,-7,8,-8,-1,2,-5,-10,8,-7,-7,-10,-6,-4,5,-8,4,-7,-5,-3,-1,8,7,-9,5,-3,-4],[-5,-4,-3,2,7,7,8,-8,-8,7,6,-8,-9,2,-5,7,-9,8,1,5,4,1,-4,5,9,-10,8,-10,10,10,-10,-5,7,3,3,-5,10,1,4,-5,-9,-10,2,-3,3,8,-10,2,-6,5,-3,-8,-6,-4,-6,5,-4,2,8,8,9,-7,-9,-6,4,-6,-2,9,-3,10,3,-5,-2,-5,-2,-4,-7,2,9,-2,-9,-1,3,1,-4,7,8,-6,-1,-3,-4,-6,7,8,5,-1,10,-9,2,3,3,-5,4,-3,2,9,-4,-10,4,9,10,6,-1,-5,5,1,7],[-8,7,7,-9,9,3,6,-9,-7,-4,1,7,10,-3,1,7,3,3,7,-6,9,6,-7,10,-4,-8,-10,2,-9,1,6,-9,1,-9,-8,-5,-6,-2,-5,-8,7,-5,-1,4,-3,9,-2,8,-2,4,-4,7,-9,5,-1,5,9,4,-9,1,3,1,10,-1,-8,4,-3,4,-2,-7,3,1,-2,-3,5,-6,6,6,-9,-8,-1,9,-3,-7,1,8,-4,6,-5,-10,5,-9,-3,4,-9,7,5,3,8,-1,-1,-10,7,4,7,2,-8,-2,3,3,8,-1,5,-1,5,-1,-2],[-3,7,2,-1,-5,-3,-2,-2,-8,6,-5,5,-3,9,-9,4,-9,9,-6,-6,-1,-7,3,7,-2,-3,3,5,8,-1,5,9,8,-5,-10,5,-10,-4,10,6,-6,8,-7,-9,-7,2,-8,5,-8,-10,1,-10,6,6,9,9,-1,9,10,-2,8,8,-4,-4,3,-3,-9,-7,-8,4,-5,5,10,3,-1,8,1,-7,-6,9,5,6,-4,-3,-8,-4,-8,8,-2,-1,-9,4,4,7,2,-1,-8,5,2,8,2,2,10,1,10,-7,-8,9,4,-2,-1,-5,2,3,-5,3,-3],[-9,-4,5,10,-4,-2,-2,8,3,1,-10,-10,-8,-4,-4,5,-7,4,4,5,4,-3,-4,-4,-2,-8,7,-5,-3,-7,3,-8,2,4,6,6,-7,-10,-9,1,-1,-2,-7,3,-6,-4,-2,-1,6,2,7,6,6,8,-2,7,-7,2,-5,-1,5,2,-2,6,2,-2,6,4,5,7,8,1,-2,9,-7,-10,8,2,7,-7,-5,-8,10,5,2,3,8,7,-6,-9,7,-7,-1,4,-8,5,-2,6,-4,7,5,-8,-5,-2,1,4,-3,4,2,2,-9,-3,1,-2,2,-3,-1],[-9,7,-5,-5,8,-2,3,-8,-5,-3,9,10,1,3,7,4,-8,9,9,6,3,-10,3,-1,-7,9,-2,-1,10,-8,8,5,3,1,8,-9,-7,-7,-9,1,7,-5,-8,4,10,5,4,-4,-1,-10,4,2,-10,-2,-9,6,10,7,-8,5,4,6,9,-4,-6,-1,-4,10,2,-5,-4,1,4,3,10,10,10,-2,7,-9,-10,1,-5,-10,-2,10,-7,9,8,3,-10,1,-10,-8,9,-8,-2,-5,-10,4,1,8,-6,9,-9,-3,7,10,5,4,9,-2,-5,-8,3,8,9],[-2,-5,10,-3,-4,4,-10,5,-2,-8,-7,-1,-9,-8,-6,3,3,-1,3,-5,6,4,-8,-10,3,-5,2,-5,8,-7,2,4,-9,6,1,-8,1,-3,-1,1,4,6,2,8,-9,-6,-7,4,-7,6,4,-5,8,-5,-10,6,-2,1,-8,-4,1,5,2,4,4,5,7,-2,-7,-5,5,2,-6,5,-9,-10,-1,-10,8,10,5,-9,-7,-7,-10,-3,6,6,6,7,-10,-8,3,4,2,-3,-1,-9,-3,-5,1,-10,3,10,-7,5,-7,10,2,3,-8,-3,7,1,8,-5,-4],[-5,-4,6,-5,1,-5,2,-5,-3,1,3,-8,10,-10,5,3,-9,-7,8,-6,-4,10,-10,2,9,9,-3,-6,-5,9,10,-1,9,-6,2,6,4,-5,-10,-10,-2,10,-8,-10,5,-4,-3,8,5,-7,-7,-4,-10,7,-7,8,6,5,-8,-6,4,10,4,-9,1,7,-10,10,9,-9,-4,6,-7,-5,-3,8,2,-5,5,7,-2,5,-3,-10,-6,-1,-6,-2,7,7,-10,-9,4,-9,10,6,-8,3,-8,8,-4,4,-7,4,-6,5,-8,6,-2,1,-1,-5,-8,2,1,-1,8],[-6,4,8,1,-3,10,10,-6,-4,-8,8,7,-3,10,5,9,-5,-1,10,8,4,-5,-10,7,-10,4,2,-7,-2,-9,9,10,9,-8,-7,4,-6,6,-2,3,8,7,1,-3,3,1,9,5,-5,1,-1,1,-6,7,-10,9,8,-5,1,3,1,-5,7,10,-5,4,-6,5,-2,1,5,-9,7,3,4,-4,-9,-7,1,6,8,3,-5,-7,3,10,-7,10,-4,2,6,-5,6,-1,1,4,9,5,-6,-2,10,4,2,-1,-6,8,-10,-8,7,5,7,7,-5,-10,5,-9,-6],[2,8,8,-8,-7,-9,7,4,-4,-1,7,-3,8,-10,5,-1,-8,2,-4,-2,1,4,7,-1,-9,2,-2,-4,5,9,-2,8,-1,5,1,4,9,3,6,-7,-8,-10,3,1,7,-7,2,8,6,-9,-1,2,-1,-5,8,-1,-10,7,4,-1,-9,10,6,5,1,2,6,-1,-8,3,10,-2,-6,4,-8,1,-7,-7,8,8,5,-3,-5,-8,-3,-1,-7,-5,-4,3,6,-7,4,8,7,3,-8,-5,-3,8,-5,10,5,-5,2,1,3,-3,-6,-10,8,7,2,-1,-4,-10,9]], dtype = "int16")#candidate|2754|(13, 117)|const|int16
call_2752 = relay.TupleGetItem(func_118_call(relay.reshape(var_2753.astype('int64'), [5, 10, 5]), relay.reshape(var_2753.astype('int64'), [5, 10, 5]), relay.reshape(const_2754.astype('int16'), [1521,]), ), 3)
call_2755 = relay.TupleGetItem(func_123_call(relay.reshape(var_2753.astype('int64'), [5, 10, 5]), relay.reshape(var_2753.astype('int64'), [5, 10, 5]), relay.reshape(const_2754.astype('int16'), [1521,]), ), 3)
uop_2758 = relay.rsqrt(call_2752.astype('float64')) # shape=(1521,)
uop_2760 = relay.rsqrt(call_2755.astype('float64')) # shape=(1521,)
func_1112_call = mod.get_global_var('func_1112')
func_1116_call = mutated_mod.get_global_var('func_1116')
const_2766 = relay.const([8,-8,-6,-8,-5,-8,5,-8,-4,-3,2,-8,10,-10,-8,3,3,-8,10,5,-8,-10,10,-1,10,-5,-5,5,-10,8,-7,3,-2,-8,1,-8,6,-2,-5,1,9,10,-10,-1,-9,10,2,8,6,-6,9,6,3,-2,-2,-6,8,7,10,-10,-7,-4,6,2,-8,-9,-4,4,2,8,10,5,9,-10,9,7,-2,4,-3,-10,-7,-1,3,-10,3,8,-1,5,-6,6,-5,-1,4,-3,-6,-9,1,5,7,-8,5,-6,-1,-4,-6,-2,3,-7,3,-5,2,-1,6,-8,5,-3,-4,-7,-2,3,3,-10,-1,5,-7,-4,-6,4,2,5,8,10,-9,-6,-7,-10,4,-1,6,-2,8,-4,10,-6,-7,-2,1,6,8,-4,3,-7,5,-4,4,6,10,6,-5,4,7,9,-7,-9,-1,10,-6,-10,5,-4,10,2,-7,1,3,5,3,-8,-3,5], dtype = "int16")#candidate|2766|(180,)|const|int16
call_2765 = relay.TupleGetItem(func_1112_call(relay.reshape(const_2766.astype('int16'), [6, 15, 2]), relay.reshape(const_2766.astype('int16'), [6, 15, 2]), relay.reshape(const_2766.astype('int16'), [6, 15, 2]), ), 1)
call_2767 = relay.TupleGetItem(func_1116_call(relay.reshape(const_2766.astype('int16'), [6, 15, 2]), relay.reshape(const_2766.astype('int16'), [6, 15, 2]), relay.reshape(const_2766.astype('int16'), [6, 15, 2]), ), 1)
var_2776 = relay.var("var_2776", dtype = "uint32", shape = (3, 2, 14))#candidate|2776|(3, 2, 14)|var|uint32
bop_2777 = relay.mod(const_2732.astype('float32'), relay.reshape(var_2776.astype('float32'), relay.shape_of(const_2732))) # shape=(3, 2, 14)
output = relay.Tuple([bop_2733,var_2753,const_2754,uop_2758,call_2765,const_2766,bop_2777,])
output2 = relay.Tuple([bop_2733,var_2753,const_2754,uop_2760,call_2767,const_2766,bop_2777,])
func_2780 = relay.Function([var_2731,var_2753,var_2776,], output)
mod['func_2780'] = func_2780
mod = relay.transform.InferType()(mod)
mutated_mod['func_2780'] = func_2780
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2780_call = mutated_mod.get_global_var('func_2780')
var_2782 = relay.var("var_2782", dtype = "uint32", shape = (3, 2, 14))#candidate|2782|(3, 2, 14)|var|uint32
var_2783 = relay.var("var_2783", dtype = "int64", shape = (250,))#candidate|2783|(250,)|var|int64
var_2784 = relay.var("var_2784", dtype = "uint32", shape = (3, 2, 14))#candidate|2784|(3, 2, 14)|var|uint32
call_2781 = func_2780_call(var_2782,var_2783,var_2784,)
output = call_2781
func_2785 = relay.Function([var_2782,var_2783,var_2784,], output)
mutated_mod['func_2785'] = func_2785
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2201_call = mod.get_global_var('func_2201')
func_2203_call = mutated_mod.get_global_var('func_2203')
call_2856 = relay.TupleGetItem(func_2201_call(), 1)
call_2857 = relay.TupleGetItem(func_2203_call(), 1)
uop_2874 = relay.log(call_2856.astype('float32')) # shape=(5, 13, 2)
uop_2876 = relay.log(call_2857.astype('float32')) # shape=(5, 13, 2)
func_68_call = mod.get_global_var('func_68')
func_72_call = mutated_mod.get_global_var('func_72')
const_2881 = relay.const([3,-4,7,-7,4,2,-8,4,-7,10,5,7,7,-1,-7,-4,10,-9,2,8,4,3,8,-6,2,1,1,5,5,-10,-6,-3,6,7,-9,-4,-4,-5,-4,-1,8,2,-10,-9,6,-9,6,1,5,-2,3,-7,2,-1,-4,-3,-4,4,-5,-9,2,3,2,-4,4,-1,-1,-5,-2,-1,9,-1,-10,-5,7,6,-3,-9,-5,-2,-8,-7,5,2,-8,-6,-9,-10,-1,6,10,-9,-10,-10,3,5,8,8,2,3,-5,9,-7,4,3,-5,-1,9,-5,8,2,-7,3,-4,-7,9,7,5,4,-1,1,-1,2,-4,9,-5,5,-1,-7,-7,3,8,1,-3,5,1,4,6,2,-3,4,-9,-1,-7,-7,-5,-8,2,6,-6,3,-7,-9,-3,5,-9,-5,7,-3,4,-9,-2,-2,8,-4,-1,2,-4,-10,-2,-2,-3,-1,2,-5,4,5,-2,-4,7,5,-5,-5,-9,-3,-10,-2,-1,-5,7,-9,-3,8,-3,8,-10,-7,1,3,7,-9,-10,-3,-3,6,-8,2,-3,-7,-5,-8,9,10,-7,9,9,-4,10,2,6,5,6,5,8,-8,8,-7,-9,-4,10,-4,-1,7,-8,5,8,-7,-7,-6,4,-9,-7,-9,3,-7,-7,1,-1,-9,7,10,6,-2,10,10,-1,8,7,-6,-1,3,-4,-7,-3,2,2,7,-1,-5,-8,-9,-5,-9,-6,-3,6,6,2,-4,2,7,2,-4,-7,-6,-3,6,-3,10,-7,-6,-1,-4,-8,8,-8,3,-10,-3,-7,2,7,8,2,-9,5,4,10,8,8,-5,4,-6,-7,1,-1,4,2,6,-3,3,-10,1,4,-7,9,9,-2,-6,-6,-2,4,3,-7,-10,-5,8,1,-5,-1,1,4,1,-5,-4,-6,7,10,7,-8,10,1,9,7,1,8,-8,-2,-8,-8,9,9,-5,6,8,1,9,8,-6,-4,5,-8,6,-5,-6,-9,8,-1,-8,-7,2,6,9,-1,-1,3,7,-2,-1,9,10,4,-5,3,5,10,7,9,2,-3,5,2,7,-6,8,8,3,-6,-1,4,8,-3,1,-10,-2,-7,-9,10,2,-6,3,-8,10,-7,-4,4,4,-6,-1,-10,-1,9,-8,10,5,2,-2,4,-6,-10,3,-2,-3,-4,9,7,-4,2,5,4,7,-10,8,-10,7,7,-6,-9,-9,5,-8,8,9,4,1,8,3,9,-3,6,-9,-2,-1,-5,-3,-8,3,10,7,9,-3,-8,-6,10,7,9,-10,-10,9,3,6,-2,-9,-2,-8,4,10,10,2,5,-7,-3,5,-7,-9,-8,-4,-5,-3,-9,1,-4,9,7,5,9,6,6,7,6,6,2,-2,-4,7,-6,1,9,4,-1,8,1,-4,-3,-2,7,-3,-1,8,-2,3,3,-7,-3,-8,2,-6,8,-9,9,2,-3,-2,1,-2,-5,10,8,-8,-10,5,2,6,9,3,-9,3,1,8,5,3,-2,8,10,-1,4,-4,-9,-8,-6,-8,7,8,-7,8,-6,-2,3,8,-7,8,7,8,2,4,-7,4,-4,-10,9,-2,10,-3,5,-8,2,-4,8,7,-5,10,3,-4,8,-7,3,-2,-3,-5,8,-3,-1,-1,6,-1,-1,5,-6,-1,4,-1,-7,-9,8,3,9,-8,10,9,9,10,-2,-4,-3,-3,4,5,9,-6,-8,-4,-2,7,-4,-1,-8,-3,-6,-1,3,-8,-9,10,7,-4,-4,1,-3,-9,7,-3,1,-7,4,-7,-1,-8,8,-8,-4,9,5,4,-10,-6,-5,4,-7,-4,-9,10,8,2,-5,-2,-7,9,-2,-9,-7,9,-5,9,-4,-3,-6,4,-10,-1,-9,6,-5,-5,1,9,-10,-2,-3,-7,6,1,4,7,2,-2,2,-6,-4,-5,-4,3,-5,8,-7,-7,6,4,-1,-5,10,3,-5,10,9,-6,-2,-6,-5,-6,-9,3,9,7,-8,-3,2,-2,-5,8,-8,7,-3,-6,9,-1,5,6,-1,3,7,-10,4,-8,4,4,-10,1,-6,-4,-1,5,-10,9,6,-3,-8,2,4,-10,5,8,9,-3,-8,-1,-5,-4,-7,-4,-3,-6,9,2,9,2,7,3,1,10,6,-8,-8,-4,5,8,7,8,3,1,-3,-7,-5,8,-8,-5,2,3,-8,-6,7,1,-9,1,-1,5,-5,6,-5,-6,-5,-7,-6,8,9,7,8,-9,-8,-1,3,5,-2,-8,7,2,-6,-10,1,-8,-10,6,4,-6,-6,-1,7,-6,9,8,9,8,10,8,4,4,1,-5,-7,-7,-10,-1,8,-5,-1,-3,-4,-6,8,8,1,9,1,-7,3,-1,-6,-9,8,-1,9,-1,-4,-9,-10,4,8,3,7,8,-8,2,-9,-10,7,10,-5,10,8,10,6,-9,-9,-4,6,6,-10,10,1,10,9,-5,1,-4,7,-6,1,-9,-10,9,-6,-10,5,-10,7,-6,10,-3,-1,7,-10,-10,8,1,2,-6,5,7,-5,8,-6,2,-8,-4,-9,-6,4,10,-5,2,1,8,-5,5,3,-3,10,5,-10,6,2,10,7,-1,-5,2,10,-3,8,-4,3,-9,5,-8,5,-6,-5,-6,-10,-5,-10,10,-8,7,-1,6,-2,-5,-1,2,9,6,6,-8,-8,9,9,-2,-10,-2,1,5,3,10,4,-9,-2,9,-6,2,10,-4,1,-8,4,-4,-10,-8,-8,6,-4,9,9,-4,6,8,9,7,-7,-3,-6,6,5,-8,4,-8,-10,-4,6,-3,6,-8,-5,-7,1,1,-8,-5,3,-7,-9,5,4,6,9,-10,-3,10,-3,-10,6,4,-10,-6,-4,10,-9,-1,-8,3,-10,-2,1,-3,-6,3,-6,-5,-5,1,-3,-3,8,7,2,-3,3,5,5,2,-3,-5,-1,-7,-1,-6,-9,-1,2,5,8,-6,1,-6,-1,2,-3,-3,9,-1,-10,7,5,-10,-5,-10,-1,5,8,-2,8,-3,1,3,9,10,-10,-3,-6,1,8,-6,8,2,-1,-6,-6,-1,-6,7,-10,-7,4,5,-2,3,8,10,-1,3,-7,-4,-10,2,-9,3,3,-2,-1,9,5,-5,1,10,-8,-7,-4,7,-4,-3,-7,-6,8,9,5,7,10,-3,-7,-5,8,9,-1,-7,7,-1,8,-7,5,8,-4,10,-6,4,-7,-10,1,8,-8,-8,-7,-1,8,1,-4,3,-3,1,-9,-5,-6,-1,6,8,6,-1,8,-8,-10,10,-6,-1,8,-10,-8,3,-2,10,6,2,-5,5,-4,10,9,-7,2,8,9,7,5,-9,4,6,9,-2,-2,-8,9,10,7,-7,-3,-1,2,-10,-7,5,10,3,-1,4,3,10,3,2,-5,-10,-3,-1,-8,2,-1,7,8,1,-7,3,-10,-4,10,2,6,-4,-1,-1,-5,4,-10,9,3,9,6,1,-4,-8,2,10,10,-6,8,-9,2,10,4,-4,-1,8,5,-5,6,-1,-1,-8,-2,3,-4,4,-6,2,6,-1,-6,-4,8,-10,-3,3,-2,5,5,-6,2,7,-4,10,-4,7,-9,3,-10,-2,-3,-7,5,-1,-1,1,6,-1,-8,2,-1,-6,-10,8,3,3,6,-3,3,3,-10,5,-4,-10,-7,-6,1,-9,-10,-3,10,9,7,8,5,-3,-6,4,-7,2,-7,2,-8,-1,1,-1,1,6,-1,9,6,10,-4,-3,9,5,-4,5,2,-2,9,4,3,-1,6,8,-4,5,-3,1,2,7,4,9,8,-1,-3,9,6,-10,-2,4,7,5,8,3,1,7,3,-3,7,10,-8,-8,10,9,-4,-7,-2,2,-8,1,4,5,2,-8,10,1,-8,-4,-4,-8,6,9,8,8,-6,-5,7,-10,6,9,8,5,6,-4,-10,9,10,4,1,3,-2,-2,8,7,-1,-9,-4,-5,-4,1,1,-8,9,-8,5,-10,2,4,-3,4,-9,3,7,-6,-6,5,-8,-10], dtype = "int16")#candidate|2881|(1521,)|const|int16
call_2880 = relay.TupleGetItem(func_68_call(relay.reshape(const_2881.astype('int16'), [9, 13, 13]), relay.reshape(const_2881.astype('int16'), [9, 13, 13]), ), 0)
call_2882 = relay.TupleGetItem(func_72_call(relay.reshape(const_2881.astype('int16'), [9, 13, 13]), relay.reshape(const_2881.astype('int16'), [9, 13, 13]), ), 0)
func_366_call = mod.get_global_var('func_366')
func_370_call = mutated_mod.get_global_var('func_370')
var_2884 = relay.var("var_2884", dtype = "float64", shape = (6, 42))#candidate|2884|(6, 42)|var|float64
var_2885 = relay.var("var_2885", dtype = "int64", shape = (25, 10))#candidate|2885|(25, 10)|var|int64
call_2883 = relay.TupleGetItem(func_366_call(relay.reshape(var_2884.astype('float64'), [9, 2, 14]), relay.reshape(const_2881.astype('int16'), [1, 1521]), relay.reshape(var_2885.astype('int64'), [250,]), ), 3)
call_2886 = relay.TupleGetItem(func_370_call(relay.reshape(var_2884.astype('float64'), [9, 2, 14]), relay.reshape(const_2881.astype('int16'), [1, 1521]), relay.reshape(var_2885.astype('int64'), [250,]), ), 3)
func_2275_call = mod.get_global_var('func_2275')
func_2276_call = mutated_mod.get_global_var('func_2276')
call_2888 = func_2275_call()
call_2889 = func_2275_call()
func_68_call = mod.get_global_var('func_68')
func_72_call = mutated_mod.get_global_var('func_72')
call_2894 = relay.TupleGetItem(func_68_call(relay.reshape(call_2880.astype('int16'), [9, 13, 13]), relay.reshape(call_2880.astype('int16'), [9, 13, 13]), ), 0)
call_2895 = relay.TupleGetItem(func_72_call(relay.reshape(call_2880.astype('int16'), [9, 13, 13]), relay.reshape(call_2880.astype('int16'), [9, 13, 13]), ), 0)
output = relay.Tuple([uop_2874,call_2880,const_2881,call_2883,var_2884,var_2885,call_2888,call_2894,])
output2 = relay.Tuple([uop_2876,call_2882,const_2881,call_2886,var_2884,var_2885,call_2889,call_2895,])
func_2909 = relay.Function([var_2884,var_2885,], output)
mod['func_2909'] = func_2909
mod = relay.transform.InferType()(mod)
var_2910 = relay.var("var_2910", dtype = "float64", shape = (6, 42))#candidate|2910|(6, 42)|var|float64
var_2911 = relay.var("var_2911", dtype = "int64", shape = (25, 10))#candidate|2911|(25, 10)|var|int64
output = func_2909(var_2910,var_2911,)
func_2912 = relay.Function([var_2910,var_2911,], output)
mutated_mod['func_2912'] = func_2912
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2562_call = mod.get_global_var('func_2562')
func_2564_call = mutated_mod.get_global_var('func_2564')
call_2959 = func_2562_call()
call_2960 = func_2562_call()
func_2304_call = mod.get_global_var('func_2304')
func_2306_call = mutated_mod.get_global_var('func_2306')
call_2979 = relay.TupleGetItem(func_2304_call(), 0)
call_2980 = relay.TupleGetItem(func_2306_call(), 0)
func_68_call = mod.get_global_var('func_68')
func_72_call = mutated_mod.get_global_var('func_72')
const_2985 = relay.const([9,7,-10,-6,9,-2,-8,-2,-9,6,8,-6,-3,3,-7,-9,2,2,4,-2,-3,9,-3,-8,8,4,2,-4,9,8,-4,6,-10,8,6,8,-4,1,-9,-4,2,5,-9,8,6,6,2,6,10,-9,-7,6,-5,-1,-5,-1,2,-3,-5,-9,-9,-3,-8,-5,6,-7,-3,4,-1,2,9,-4,-9,4,-8,-7,1,-9,10,7,10,-10,-8,-10,-9,-6,-4,-3,-7,-9,3,3,-7,-3,6,4,6,8,-8,5,-1,-8,-3,-9,8,-7,-5,5,5,-8,9,-9,-8,1,5,3,-8,2,2,2,-9,-2,-1,4,-4,7,8,8,-2,10,-6,-5,4,4,7,7,-4,10,-4,1,1,-1,3,5,-10,-7,9,-9,-7,8,-8,2,4,9,-10,-7,-8,10,-10,1,9,6,-7,-1,-9,-2,4,3,8,5,2,-9,-10,6,-3,4,4,-9,7,7,9,-7,5,-2,-1,3,8,-6,2,-2,8,6,-6,-4,5,2,-3,8,8,1,4,5,-7,-2,-4,3,-10,3,-5,10,-8,-5,-9,9,10,1,5,8,8,10,-6,-1,3,2,-10,-10,-5,9,6,3,9,10,9,-5,-9,6,-7,2,2,-10,6,-3,4,5,2,-6,2,-5,3,8,7,7,-1,-6,3,-5,5,-10,-10,9,-4,2,-10,-9,-9,4,10,-1,-10,-6,-2,-2,9,-8,-10,2,3,-2,-3,5,-9,-1,2,-2,9,-5,-8,-2,10,5,-8,-4,3,1,10,-1,8,-7,-1,5,6,-3,-7,-9,-6,9,-3,2,-10,3,2,8,-5,-2,-4,10,-7,2,9,-4,-10,-6,5,-1,4,4,10,-6,5,-3,5,10,-8,7,-6,10,-2,-8,-8,-2,3,-8,6,-9,-2,-3,-8,8,-5,-1,7,-4,-2,6,9,4,-5,-8,6,3,2,6,9,5,-10,3,-10,6,9,-3,3,-2,-10,9,-8,6,10,-9,6,3,10,5,4,3,-7,-2,4,7,4,9,-10,-1,7,-9,2,2,9,4,-1,7,-3,-8,-10,-10,3,-6,6,-3,-7,-9,6,3,-1,1,1,-1,4,1,6,-10,-3,-6,-4,-4,-3,10,-6,-7,9,8,5,-6,9,-6,-3,8,5,-6,2,9,-5,-7,3,8,1,4,5,8,1,3,-10,-1,4,3,-9,3,3,-7,-3,10,8,1,-8,-9,3,-3,2,10,-3,-4,-7,-6,-5,9,-5,4,-5,-9,6,-3,10,3,-2,-8,8,-5,8,-7,6,3,-7,7,1,-6,-5,-7,-7,-9,-5,-3,-8,10,-2,9,5,9,8,-5,-5,-8,-1,7,7,-6,2,9,-8,6,-6,-7,-8,4,-4,6,9,10,-1,8,1,-2,3,-3,-8,10,5,-6,6,10,8,-9,-10,-7,-4,-8,-10,9,10,4,-2,-4,4,9,-2,9,-5,-7,5,-5,-10,5,-1,-5,8,-1,-6,5,-6,1,5,6,-6,4,-8,4,2,-9,-6,6,-6,2,1,-3,4,-3,-1,7,-5,-3,-10,2,-6,6,5,-4,8,-2,-5,-4,-8,6,-9,9,5,-4,8,-8,-8,6,8,-6,-8,-5,-3,2,9,1,2,-9,-1,-2,10,-3,4,-2,1,-1,8,2,7,3,1,-4,-5,9,-8,6,9,-6,9,7,8,1,-6,-7,8,-10,5,3,9,-7,1,4,-1,6,10,3,3,-6,-8,3,5,6,-9,10,-9,2,-10,-3,-9,-4,4,9,-1,6,7,3,3,2,8,-10,10,-8,-10,-1,10,10,-3,1,1,1,-7,10,6,3,-7,-1,-7,-7,-10,6,6,-3,-4,-2,2,-2,10,10,-7,9,8,-1,1,-1,-8,2,-2,2,-9,-10,-8,1,-6,1,6,5,10,-8,-4,3,-4,6,9,-2,4,1,-6,-7,3,-6,-10,2,9,-2,-9,-4,9,10,10,6,6,6,-8,-4,5,-2,5,6,6,-6,2,-7,-4,8,-1,-9,-2,8,-10,-2,6,-9,-10,4,2,8,-2,6,1,1,10,8,-5,-3,1,-7,3,-6,2,8,10,9,-10,9,10,-5,7,4,10,-6,-7,5,-10,3,-3,-7,7,-8,-2,-10,6,-5,-7,-7,-10,-7,8,7,5,10,-10,-4,3,-4,8,9,9,6,-7,-2,-4,4,-1,1,-10,7,-8,-7,-2,9,-6,3,-4,-1,10,6,2,-9,10,10,-1,-1,7,-1,10,-8,-8,-2,-10,3,-4,-7,8,9,3,1,-8,2,-2,-4,-5,-3,-5,-5,-5,6,-7,8,-8,5,-8,-3,1,-2,10,-9,2,10,-4,2,-3,-1,-3,8,-7,1,9,2,3,3,1,10,4,1,-5,7,3,-8,8,6,-9,9,-4,8,-6,-3,-4,8,-3,6,-2,-5,3,-1,-9,6,-7,6,7,-1,6,8,8,-10,7,-6,10,-5,-5,6,5,-4,7,6,-3,-5,-2,2,10,-9,-7,7,-8,-2,9,9,-10,-8,2,-8,-2,7,-7,4,-1,6,9,7,6,-4,-9,-10,-7,-3,2,-5,6,8,1,3,-4,9,-2,5,-8,-4,-2,-6,-1,-8,-2,-7,5,2,-5,7,3,5,4,5,6,3,-4,-7,-9,7,-9,10,8,-9,8,-4,-4,8,6,-2,-3,-2,-3,1,7,-3,-2,10,6,5,-5,-7,-6,9,-8,-8,-7,7,1,-1,-6,5,-9,10,-2,1,1,-8,-3,-3,-9,2,-9,-5,-7,-9,3,2,8,-9,-6,10,10,-6,-7,2,8,-2,-2,-1,3,3,5,10,-7,4,1,3,-5,4,8,10,9,6,8,10,7,-7,-1,6,10,-1,5,4,-5,-2,4,10,3,-5,-3,-10,8,-5,-8,7,10,-9,-4,-2,1,1,-7,7,8,9,-6,-4,-10,-5,7,-6,-2,1,-8,-6,-9,4,-1,-4,-4,-10,3,9,2,-2,6,7,3,-7,-3,1,1,7,-10,-10,-7,-9,6,-4,9,-9,-1,4,-4,-6,3,10,7,-7,10,3,10,8,7,-4,7,3,10,4,6,3,-9,3,-10,-1,10,10,6,-5,9,1,-3,-3,-10,8,-7,5,-2,10,-3,-2,6,10,-9,7,4,-3,-10,1,3,8,-2,6,5,6,8,8,2,-8,-3,-1,2,-8,-2,4,10,-5,-7,6,6,10,4,6,8,-8,-8,1,-3,-6,-8,10,4,-10,-6,-5,-8,4,6,7,5,-6,4,-7,-6,4,3,10,1,10,-6,-10,1,8,6,-3,3,-6,-9,-6,5,-7,-3,-4,8,-2,9,1,-5,-1,-6,-4,4,-8,4,-5,3,5,-10,-2,5,3,5,-7,-6,-1,-1,-3,-6,9,4,-7,8,5,-3,6,-9,1,6,-4,6,-5,2,-3,1,-6,-6,2,-5,1,3,5,6,-8,5,3,9,8,7,10,5,-3,-1,4,3,3,1,-2,3,1,3,-9,3,-6,1,10,-3,7,-9,9,6,-10,1,6,-1,4,-1,6,2,-6,-7,-9,9,-6,8,-10,9,-3,-1,4,6,-4,1,-2,-2,-8,-7,3,4,6,-5,6,6,4,-8,7,-6,-2,-1,-2,5,3,-8,9,6,-3,2,4,-9,-3,-7,-1,-3,4,7,6,7,-5,-8,6,-2,2,8,-9,-6,-4,-7,8,5,-4,7,6,1,-8,10,10,2,-3,10,7,-8,-9,-3,-3,-8,-5,-6,10,4,6,-1,-5,10,3,-2,6,-1,-5,9,-7,6,3,-2,-1,10,-10,6,3,-3,-6,9,5,4,-8,-9,-1,4,-8,6,5,-1,-8,-10,2,1,8,-9,-2,4,-7,5,-9,3,-7,1,8,5,-8,9,8,-8,-8,1,2,-9,8,1,3,9,7,-2,-1,-1,3,8,7,-8,-5,-8,4,-9,3,4,-8,-8,2,-9,6,-1,-9,-10,7,5,9,-2,-1,9,-3,-10,5,-5,5,-1,4,-1], dtype = "int16")#candidate|2985|(1521,)|const|int16
call_2984 = relay.TupleGetItem(func_68_call(relay.reshape(const_2985.astype('int16'), [9, 13, 13]), relay.reshape(const_2985.astype('int16'), [9, 13, 13]), ), 0)
call_2986 = relay.TupleGetItem(func_72_call(relay.reshape(const_2985.astype('int16'), [9, 13, 13]), relay.reshape(const_2985.astype('int16'), [9, 13, 13]), ), 0)
output = relay.Tuple([call_2959,call_2979,call_2984,const_2985,])
output2 = relay.Tuple([call_2960,call_2980,call_2986,const_2985,])
func_2993 = relay.Function([], output)
mod['func_2993'] = func_2993
mod = relay.transform.InferType()(mod)
mutated_mod['func_2993'] = func_2993
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2993_call = mutated_mod.get_global_var('func_2993')
call_2994 = func_2993_call()
output = call_2994
func_2995 = relay.Function([], output)
mutated_mod['func_2995'] = func_2995
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2562_call = mod.get_global_var('func_2562')
func_2564_call = mutated_mod.get_global_var('func_2564')
call_3025 = func_2562_call()
call_3026 = func_2562_call()
output = relay.Tuple([call_3025,])
output2 = relay.Tuple([call_3026,])
func_3034 = relay.Function([], output)
mod['func_3034'] = func_3034
mod = relay.transform.InferType()(mod)
mutated_mod['func_3034'] = func_3034
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3034_call = mutated_mod.get_global_var('func_3034')
call_3035 = func_3034_call()
output = call_3035
func_3036 = relay.Function([], output)
mutated_mod['func_3036'] = func_3036
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3047 = relay.var("var_3047", dtype = "uint32", shape = ())#candidate|3047|()|var|uint32
var_3048 = relay.var("var_3048", dtype = "uint32", shape = (6, 10, 9))#candidate|3048|(6, 10, 9)|var|uint32
bop_3049 = relay.greater(var_3047.astype('bool'), var_3048.astype('bool')) # shape=(6, 10, 9)
func_3034_call = mod.get_global_var('func_3034')
func_3036_call = mutated_mod.get_global_var('func_3036')
call_3056 = relay.TupleGetItem(func_3034_call(), 0)
call_3057 = relay.TupleGetItem(func_3036_call(), 0)
output = relay.Tuple([bop_3049,call_3056,])
output2 = relay.Tuple([bop_3049,call_3057,])
func_3059 = relay.Function([var_3047,var_3048,], output)
mod['func_3059'] = func_3059
mod = relay.transform.InferType()(mod)
var_3060 = relay.var("var_3060", dtype = "uint32", shape = ())#candidate|3060|()|var|uint32
var_3061 = relay.var("var_3061", dtype = "uint32", shape = (6, 10, 9))#candidate|3061|(6, 10, 9)|var|uint32
output = func_3059(var_3060,var_3061,)
func_3062 = relay.Function([var_3060,var_3061,], output)
mutated_mod['func_3062'] = func_3062
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3093 = relay.var("var_3093", dtype = "int32", shape = (11, 13, 8))#candidate|3093|(11, 13, 8)|var|int32
var_3094 = relay.var("var_3094", dtype = "int32", shape = (11, 13, 8))#candidate|3094|(11, 13, 8)|var|int32
bop_3095 = relay.maximum(var_3093.astype('int32'), relay.reshape(var_3094.astype('int32'), relay.shape_of(var_3093))) # shape=(11, 13, 8)
func_3034_call = mod.get_global_var('func_3034')
func_3036_call = mutated_mod.get_global_var('func_3036')
call_3099 = relay.TupleGetItem(func_3034_call(), 0)
call_3100 = relay.TupleGetItem(func_3036_call(), 0)
const_3125 = relay.const([[[-2,5,-8,-4,2,5,-4,1],[7,-1,6,6,-2,-10,7,-6],[-8,-4,-9,5,2,7,-2,-10],[-2,1,9,-1,4,-3,3,-1],[10,7,6,3,1,-6,10,3],[-8,-1,-2,7,-2,-9,10,7],[-7,-1,8,1,-6,4,2,10],[-2,7,1,-1,4,1,-2,-2],[-3,-4,-9,-10,-3,-10,10,4],[-9,5,7,-7,6,3,-4,-8],[9,8,8,-10,-2,5,10,-5],[2,-3,6,8,-7,1,-5,10],[5,-2,8,4,-4,-6,-8,-5]],[[1,-7,-9,-10,-7,10,3,6],[10,1,-1,1,-1,10,-8,-10],[-7,5,-4,-2,7,3,-2,8],[-8,-1,3,4,9,-3,-3,5],[2,5,6,-6,-7,-4,9,-2],[-2,-8,7,9,8,-2,-5,-2],[-6,2,4,6,7,2,-6,5],[-7,3,4,9,-3,4,9,-6],[3,-8,6,-8,-6,8,-3,9],[5,6,-5,-1,10,-8,-1,4],[2,9,-8,10,-7,5,3,-2],[8,-6,-6,1,2,5,-6,7],[10,4,5,1,2,2,4,4]],[[5,-4,8,-7,7,-6,-10,8],[3,8,-6,9,-9,-3,-8,-4],[6,-4,-3,7,-2,2,-7,1],[-4,7,-2,-8,-1,3,-10,2],[2,2,-8,7,3,-1,-2,10],[5,-6,8,-9,8,10,-8,-4],[10,-8,-5,10,6,8,-6,-4],[10,10,-7,-8,-3,-1,-3,-1],[-10,-3,6,5,-7,-8,3,-5],[-3,10,-6,-4,-9,9,-9,4],[9,-6,-3,7,-6,-2,-8,-2],[6,2,2,-2,-1,2,-1,-1],[6,-5,10,8,8,5,-8,6]],[[2,-7,-4,-5,8,-6,6,1],[-5,-2,10,-3,9,-2,-6,3],[10,2,9,-8,-9,-7,-2,-8],[5,-5,7,3,7,-6,-6,3],[-1,10,6,-10,-4,9,-7,4],[6,-9,7,-10,-7,-7,7,1],[-5,-1,-10,-6,-10,-2,-2,1],[4,-1,-1,-5,-9,-3,2,-6],[4,-10,8,1,-2,7,9,-2],[-5,6,-7,-4,3,3,-1,2],[8,-4,-9,6,-9,-7,-10,-3],[-3,-1,-8,-7,4,6,-2,-5],[-4,9,-5,5,10,2,3,5]],[[4,8,-2,-5,-6,-4,-1,9],[7,9,4,5,7,4,-3,-8],[6,1,1,-6,6,5,8,-5],[1,10,9,1,-3,8,3,-6],[-9,7,-2,-7,3,-8,-8,-10],[6,-6,5,2,2,5,3,-4],[-8,-6,-4,-1,-7,-9,-1,-3],[9,3,-7,-2,-3,4,-10,-2],[-1,-9,1,3,-8,-2,3,7],[7,6,2,-4,-4,-3,-9,3],[5,-5,1,-4,-2,9,4,-7],[-3,-6,10,-2,-8,-9,1,-7],[3,3,-1,4,-5,-9,8,-1]],[[-9,-9,-9,-3,7,-6,-5,5],[6,-3,-4,10,-1,-2,7,3],[-2,-6,1,-10,3,-7,10,6],[9,-2,-10,6,-3,2,2,9],[6,-7,-5,7,4,6,-5,9],[-6,9,-5,-9,3,-10,7,-9],[5,3,-2,9,4,9,10,7],[8,3,-3,2,4,-1,1,5],[3,-7,-8,-10,-2,4,-6,1],[9,7,-6,7,1,2,-5,10],[-7,-4,3,-9,-4,8,-6,-4],[-3,-6,-10,-3,-1,4,6,-6],[1,7,-6,9,-9,-8,8,-9]],[[-2,3,10,-2,-1,-8,10,-9],[6,3,2,1,-2,8,2,-2],[4,6,-9,4,-5,-8,-6,6],[-3,-3,-4,6,-3,4,2,2],[1,-2,8,-2,-10,-10,7,8],[6,5,-8,-3,-7,-6,5,7],[-6,6,-6,-7,-9,3,-2,4],[-4,5,1,-3,-7,7,9,-5],[2,-8,-10,-3,3,-2,8,-4],[-6,4,-9,6,-8,-7,7,-3],[-5,-7,10,-3,7,10,5,10],[5,9,-3,-1,7,9,1,-5],[4,1,-2,-7,-4,-6,2,-10]],[[-10,-2,-5,-5,2,8,-5,-10],[-5,-3,9,-7,6,10,9,-5],[-1,3,2,10,-3,7,-3,9],[10,-4,9,-2,5,2,-3,5],[6,2,6,-1,-2,7,5,-3],[7,6,9,10,1,9,1,-10],[2,4,-5,6,-3,-5,10,-7],[-5,4,10,-1,-8,-7,-4,3],[-8,-1,3,-2,-2,-7,5,9],[9,-8,-7,-2,-9,1,3,-7],[-2,3,6,2,-2,-10,4,-9],[-5,2,7,-7,10,-8,-4,3],[5,-3,-1,1,-5,10,-2,-10]],[[7,-9,5,-1,-5,-7,5,-7],[8,-1,5,10,-5,-7,9,-4],[-1,-1,10,-1,-10,-4,-10,5],[-10,-7,-10,-5,7,-4,3,-5],[2,1,9,-6,4,-5,-2,-2],[-9,-9,6,-6,10,-9,7,-9],[1,2,4,10,10,2,-6,-6],[5,-5,-3,-2,-8,-8,-7,5],[-7,-8,5,-8,-3,-8,-7,5],[-4,-3,-1,2,7,6,6,-2],[6,-5,7,-7,6,-9,-2,4],[-7,4,1,-7,5,2,5,-6],[3,-4,-7,-1,8,5,-6,-5]],[[4,-9,5,-3,1,4,1,-9],[-3,7,3,10,-7,1,-4,6],[-8,-2,5,5,-3,2,-9,8],[-5,2,2,9,-9,-5,-9,-2],[8,-9,-1,8,3,8,2,-4],[1,-5,9,2,-6,-2,10,1],[-8,-8,7,5,-8,4,10,-5],[5,4,3,4,7,-4,10,2],[10,-8,-9,-8,5,5,9,6],[9,8,8,-3,7,-1,-7,-4],[-6,-3,-5,-10,-1,6,4,-2],[4,6,3,8,-9,7,-3,-2],[-3,-1,-5,9,-5,-8,6,3]],[[1,3,-1,1,1,7,-9,10],[5,10,-2,8,3,6,5,3],[-9,9,9,-1,10,-4,-6,-2],[-8,2,1,-9,5,8,-7,9],[7,-7,10,7,-5,-2,5,-3],[-8,3,7,6,9,6,-2,1],[3,-6,-3,4,5,-10,-9,3],[10,-7,-10,-8,8,5,9,1],[-4,-4,1,-7,-3,9,2,9],[10,8,10,10,-10,-10,-3,-10],[8,-5,1,7,9,-5,-8,2],[2,-9,-5,-2,6,-5,-3,-7],[8,-1,-4,-2,2,5,-6,7]]], dtype = "int32")#candidate|3125|(11, 13, 8)|const|int32
bop_3126 = relay.bitwise_and(bop_3095.astype('uint32'), relay.reshape(const_3125.astype('uint32'), relay.shape_of(bop_3095))) # shape=(11, 13, 8)
output = relay.Tuple([call_3099,bop_3126,])
output2 = relay.Tuple([call_3100,bop_3126,])
func_3151 = relay.Function([var_3093,var_3094,], output)
mod['func_3151'] = func_3151
mod = relay.transform.InferType()(mod)
mutated_mod['func_3151'] = func_3151
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3151_call = mutated_mod.get_global_var('func_3151')
var_3153 = relay.var("var_3153", dtype = "int32", shape = (11, 13, 8))#candidate|3153|(11, 13, 8)|var|int32
var_3154 = relay.var("var_3154", dtype = "int32", shape = (11, 13, 8))#candidate|3154|(11, 13, 8)|var|int32
call_3152 = func_3151_call(var_3153,var_3154,)
output = call_3152
func_3155 = relay.Function([var_3153,var_3154,], output)
mutated_mod['func_3155'] = func_3155
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2145_call = mod.get_global_var('func_2145')
func_2147_call = mutated_mod.get_global_var('func_2147')
call_3201 = relay.TupleGetItem(func_2145_call(), 0)
call_3202 = relay.TupleGetItem(func_2147_call(), 0)
output = call_3201
output2 = call_3202
func_3217 = relay.Function([], output)
mod['func_3217'] = func_3217
mod = relay.transform.InferType()(mod)
mutated_mod['func_3217'] = func_3217
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3217_call = mutated_mod.get_global_var('func_3217')
call_3218 = func_3217_call()
output = call_3218
func_3219 = relay.Function([], output)
mutated_mod['func_3219'] = func_3219
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2275_call = mod.get_global_var('func_2275')
func_2276_call = mutated_mod.get_global_var('func_2276')
call_3234 = func_2275_call()
call_3235 = func_2275_call()
func_2486_call = mod.get_global_var('func_2486')
func_2487_call = mutated_mod.get_global_var('func_2487')
call_3254 = func_2486_call()
call_3255 = func_2486_call()
output = relay.Tuple([call_3234,call_3254,])
output2 = relay.Tuple([call_3235,call_3255,])
func_3258 = relay.Function([], output)
mod['func_3258'] = func_3258
mod = relay.transform.InferType()(mod)
output = func_3258()
func_3259 = relay.Function([], output)
mutated_mod['func_3259'] = func_3259
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3316 = relay.var("var_3316", dtype = "float32", shape = (9, 15, 12))#candidate|3316|(9, 15, 12)|var|float32
uop_3317 = relay.erf(var_3316.astype('float32')) # shape=(9, 15, 12)
func_2316_call = mod.get_global_var('func_2316')
func_2317_call = mutated_mod.get_global_var('func_2317')
call_3326 = relay.TupleGetItem(func_2316_call(), 0)
call_3327 = relay.TupleGetItem(func_2317_call(), 0)
func_2393_call = mod.get_global_var('func_2393')
func_2395_call = mutated_mod.get_global_var('func_2395')
call_3330 = relay.TupleGetItem(func_2393_call(), 0)
call_3331 = relay.TupleGetItem(func_2395_call(), 0)
func_2316_call = mod.get_global_var('func_2316')
func_2317_call = mutated_mod.get_global_var('func_2317')
call_3332 = relay.TupleGetItem(func_2316_call(), 0)
call_3333 = relay.TupleGetItem(func_2317_call(), 0)
uop_3343 = relay.asinh(uop_3317.astype('float32')) # shape=(9, 15, 12)
uop_3375 = relay.sin(uop_3343.astype('float32')) # shape=(9, 15, 12)
output = relay.Tuple([call_3326,call_3330,call_3332,uop_3375,])
output2 = relay.Tuple([call_3327,call_3331,call_3333,uop_3375,])
func_3382 = relay.Function([var_3316,], output)
mod['func_3382'] = func_3382
mod = relay.transform.InferType()(mod)
mutated_mod['func_3382'] = func_3382
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3383 = relay.var("var_3383", dtype = "float32", shape = (9, 15, 12))#candidate|3383|(9, 15, 12)|var|float32
func_3382_call = mutated_mod.get_global_var('func_3382')
call_3384 = func_3382_call(var_3383)
output = call_3384
func_3385 = relay.Function([var_3383], output)
mutated_mod['func_3385'] = func_3385
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2316_call = mod.get_global_var('func_2316')
func_2317_call = mutated_mod.get_global_var('func_2317')
call_3416 = relay.TupleGetItem(func_2316_call(), 0)
call_3417 = relay.TupleGetItem(func_2317_call(), 0)
output = relay.Tuple([call_3416,])
output2 = relay.Tuple([call_3417,])
func_3422 = relay.Function([], output)
mod['func_3422'] = func_3422
mod = relay.transform.InferType()(mod)
mutated_mod['func_3422'] = func_3422
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3422_call = mutated_mod.get_global_var('func_3422')
call_3423 = func_3422_call()
output = call_3423
func_3424 = relay.Function([], output)
mutated_mod['func_3424'] = func_3424
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2145_call = mod.get_global_var('func_2145')
func_2147_call = mutated_mod.get_global_var('func_2147')
call_3439 = relay.TupleGetItem(func_2145_call(), 2)
call_3440 = relay.TupleGetItem(func_2147_call(), 2)
func_2042_call = mod.get_global_var('func_2042')
func_2044_call = mutated_mod.get_global_var('func_2044')
call_3447 = relay.TupleGetItem(func_2042_call(), 0)
call_3448 = relay.TupleGetItem(func_2044_call(), 0)
uop_3455 = relay.tan(call_3447.astype('float64')) # shape=(9, 2, 2)
uop_3457 = relay.tan(call_3448.astype('float64')) # shape=(9, 2, 2)
output = relay.Tuple([call_3439,uop_3455,])
output2 = relay.Tuple([call_3440,uop_3457,])
func_3468 = relay.Function([], output)
mod['func_3468'] = func_3468
mod = relay.transform.InferType()(mod)
output = func_3468()
func_3469 = relay.Function([], output)
mutated_mod['func_3469'] = func_3469
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2201_call = mod.get_global_var('func_2201')
func_2203_call = mutated_mod.get_global_var('func_2203')
call_3519 = relay.TupleGetItem(func_2201_call(), 2)
call_3520 = relay.TupleGetItem(func_2203_call(), 2)
func_3034_call = mod.get_global_var('func_3034')
func_3036_call = mutated_mod.get_global_var('func_3036')
call_3522 = relay.TupleGetItem(func_3034_call(), 0)
call_3523 = relay.TupleGetItem(func_3036_call(), 0)
func_3034_call = mod.get_global_var('func_3034')
func_3036_call = mutated_mod.get_global_var('func_3036')
call_3526 = relay.TupleGetItem(func_3034_call(), 0)
call_3527 = relay.TupleGetItem(func_3036_call(), 0)
output = relay.Tuple([call_3519,call_3522,call_3526,])
output2 = relay.Tuple([call_3520,call_3523,call_3527,])
func_3532 = relay.Function([], output)
mod['func_3532'] = func_3532
mod = relay.transform.InferType()(mod)
output = func_3532()
func_3533 = relay.Function([], output)
mutated_mod['func_3533'] = func_3533
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2201_call = mod.get_global_var('func_2201')
func_2203_call = mutated_mod.get_global_var('func_2203')
call_3539 = relay.TupleGetItem(func_2201_call(), 0)
call_3540 = relay.TupleGetItem(func_2203_call(), 0)
func_575_call = mod.get_global_var('func_575')
func_579_call = mutated_mod.get_global_var('func_579')
const_3565 = relay.const([-6.772760,-6.716474,-9.364141,3.016624,-7.640422,-1.778072,-0.322973,0.401624,-3.771378,4.680186,6.806469,6.790166,-3.840705,-1.180065,8.963737,-0.056476,-9.845096,-1.400383,-9.351294,7.726622,6.813522,-0.412663,-8.114664,-1.928882,-8.703194,-6.231964,8.024361,-5.982607,8.458061,0.196000,-7.490220,-5.654639,7.812826,-0.669197,-1.307582,-4.667179,2.624035,7.531677,3.837299,3.538619,3.272730,7.375890,5.711744,0.185865,8.903271,9.072866,-8.115833,-4.161423,-7.131701,8.842978,-3.622487,3.731164,-0.909626,-5.937102,-0.527223,-0.004918,2.586422,-7.080069,1.033014,7.865072,2.369173,-7.970281,-5.216620,0.312442,1.382798,2.701165,-5.190457,-1.699159,-9.641277,-3.438479,-8.775288,-4.759582,5.932113,-8.449568,-2.659239,9.548541,-7.129953,0.482472,-9.185820,6.801696,6.184529,-3.196751,7.121513,4.859849,6.821038,2.074949,-4.090506,5.281952,-4.041076,-5.952954,9.625854,-9.020418,3.180524,-2.312449,-8.260256,-8.216072], dtype = "float32")#candidate|3565|(96,)|const|float32
var_3566 = relay.var("var_3566", dtype = "int8", shape = (2, 20))#candidate|3566|(2, 20)|var|int8
call_3564 = relay.TupleGetItem(func_575_call(relay.reshape(const_3565.astype('float32'), [6, 1, 16]), relay.reshape(var_3566.astype('int8'), [40,]), ), 3)
call_3567 = relay.TupleGetItem(func_579_call(relay.reshape(const_3565.astype('float32'), [6, 1, 16]), relay.reshape(var_3566.astype('int8'), [40,]), ), 3)
uop_3590 = relay.sqrt(call_3564.astype('float32')) # shape=(400,)
uop_3592 = relay.sqrt(call_3567.astype('float32')) # shape=(400,)
uop_3596 = relay.cos(call_3539.astype('float32')) # shape=(9, 2, 2)
uop_3598 = relay.cos(call_3540.astype('float32')) # shape=(9, 2, 2)
func_3059_call = mod.get_global_var('func_3059')
func_3062_call = mutated_mod.get_global_var('func_3062')
const_3600 = relay.const(-5, dtype = "uint32")#candidate|3600|()|const|uint32
const_3601 = relay.const([2,9,-7,-4,-7,-3,6,-4,3,-5,-1,5,-8,-9,5,-3,3,2,-10,-8,3,5,-9,8,-8,-6,-3,10,-5,-6,-8,9,2,5,8,-10,-7,10,3,8,9,10,-7,5,9,4,2,-3,3,-6,-1,1,9,-4,9,4,7,2,-4,10,8,-3,5,5,-1,-2,5,-10,5,9,-5,-2,8,-8,10,-6,-10,-9,2,-7,-4,5,2,-6,-7,-1,-7,-5,-8,7,-1,-6,-1,-9,10,-8,-5,-4,8,4,-2,-10,-1,-3,-9,6,-3,-4,9,9,-1,4,10,3,-5,-3,-5,7,9,-4,2,10,-4,2,-10,-5,-10,7,4,-5,-6,-7,3,-6,3,1,-9,3,-5,-9,7,-6,-10,4,2,4,-10,-8,4,-5,3,4,-9,7,3,-1,-7,-5,9,-2,1,-8,6,5,-9,9,-8,-5,-4,-3,6,5,-8,-2,-2,-7,-10,-7,10,-6,-4,-2,-2,1,9,10,7,-3,-8,3,9,6,-4,6,4,-6,1,-5,7,6,2,-5,3,-4,-5,4,7,-5,-2,-9,-5,7,3,8,9,-7,-1,-10,2,-9,10,-1,3,2,-7,2,-5,7,-2,-9,-10,-2,3,-7,-5,-2,-10,-4,8,-6,6,-8,-6,1,1,-9,-10,-2,-2,-8,5,-1,-2,8,10,7,-4,9,2,-10,-3,4,1,-6,6,1,5,-8,9,-1,2,7,4,7,-7,9,-5,3,2,2,-5,-1,5,9,7,-4,-7,4,8,-7,8,5,10,3,7,-10,-6,-5,2,6,-4,-8,-3,2,6,6,-7,9,-9,1,-8,10,-4,7,-9,-5,5,-5,10,8,9,9,-5,3,-3,-1,5,-6,-8,-5,6,-1,-5,-9,-6,-10,1,10,2,-1,8,-7,-5,4,-6,2,2,2,2,2,-8,-2,6,6,-5,-4,-9,8,3,-9,2,10,-7,-1,4,6,10,3,-9,-3,-6,-7,-7,2,8,7,-3,6,-9,-10,2,7,5,7,8,10,6,-2,-4,-3,4,-6,6,10,9,-10,-7,5,6,-7,6,2,-7,-5,7,-5,9,-9,-3,10,-10,-5,7,10,-5,-10,4,-3,4,-4,-7,1,2,10,-10,7,1,6,3,-1,-3,-1,1,-10,3,6,-2,-7,9,-10,-8,-1,-9,6,5,2,8,-6,7,-4,9,2,8,-6,7,-8,-4,-3,-7,7,-8,-1,4,5,-3,-4,8,-4,5,3,-7,-6,-9,-4,-10,10,1,6,9,9,-10,-2,8,7,5,5,3,3,-2,10,-7,2,4,-5,9,2,-6,-2,-10,8,-2,-9,6,-9,-10,-10,1,-7,2,-7,6,4,4,6,6,-3,-9,-3,6,-1,3,5,5,-1,4,8,7,-1,8,9,1,4,4,-5,1,9,7,-10,-4,9], dtype = "uint32")#candidate|3601|(540,)|const|uint32
call_3599 = relay.TupleGetItem(func_3059_call(relay.reshape(const_3600.astype('uint32'), []), relay.reshape(const_3601.astype('uint32'), [6, 10, 9]), ), 1)
call_3602 = relay.TupleGetItem(func_3062_call(relay.reshape(const_3600.astype('uint32'), []), relay.reshape(const_3601.astype('uint32'), [6, 10, 9]), ), 1)
func_2545_call = mod.get_global_var('func_2545')
func_2546_call = mutated_mod.get_global_var('func_2546')
call_3610 = relay.TupleGetItem(func_2545_call(), 0)
call_3611 = relay.TupleGetItem(func_2546_call(), 0)
func_1112_call = mod.get_global_var('func_1112')
func_1116_call = mutated_mod.get_global_var('func_1116')
const_3634 = relay.const([[4],[-3],[-2],[2],[-5],[-5],[-1],[5],[-10],[3],[-2],[4],[-3],[8],[4],[6],[-10],[2],[-9],[-3],[5],[5],[3],[-9],[4],[7],[-2],[5],[3],[9],[-1],[-7],[5],[-4],[-4],[-9],[5],[4],[-5],[10],[-7],[-5],[-7],[-8],[-4],[-10],[-1],[-6],[4],[1],[5],[6],[3],[7],[-5],[7],[-2],[-2],[-3],[-9],[-7],[-9],[-6],[5],[5],[10],[5],[7],[6],[-5],[-10],[4],[5],[1],[8],[2],[-3],[-4],[-8],[-8],[4],[-10],[-4],[6],[-2],[10],[3],[6],[-1],[3],[-10],[-3],[-8],[9],[7],[-8],[5],[-9],[-8],[8],[3],[-3],[-3],[-4],[5],[4],[-2],[6],[5],[7],[-5],[2],[-4],[1],[-5],[3],[-1],[6],[-5],[-10],[6],[8],[10],[-8],[-3],[6],[10],[10],[-8],[-8],[-1],[1],[-7],[-8],[7],[-5],[-2],[1],[-8],[9],[-5],[-9],[-5],[-9],[-9],[-6],[-7],[-2],[5],[-9],[8],[5],[10],[1],[6],[9],[-5],[6],[-9],[-4],[3],[-9],[-8],[5],[3],[-8],[-1],[-10],[-1],[-8],[1],[8],[-8],[-7],[-1],[-5],[1],[-5],[7],[6]], dtype = "int16")#candidate|3634|(180, 1)|const|int16
call_3633 = relay.TupleGetItem(func_1112_call(relay.reshape(const_3634.astype('int16'), [6, 15, 2]), relay.reshape(const_3634.astype('int16'), [6, 15, 2]), relay.reshape(const_3634.astype('int16'), [6, 15, 2]), ), 1)
call_3635 = relay.TupleGetItem(func_1116_call(relay.reshape(const_3634.astype('int16'), [6, 15, 2]), relay.reshape(const_3634.astype('int16'), [6, 15, 2]), relay.reshape(const_3634.astype('int16'), [6, 15, 2]), ), 1)
output = relay.Tuple([const_3565,var_3566,uop_3590,uop_3596,call_3599,const_3600,const_3601,call_3610,call_3633,const_3634,])
output2 = relay.Tuple([const_3565,var_3566,uop_3592,uop_3598,call_3602,const_3600,const_3601,call_3611,call_3635,const_3634,])
func_3638 = relay.Function([var_3566,], output)
mod['func_3638'] = func_3638
mod = relay.transform.InferType()(mod)
var_3639 = relay.var("var_3639", dtype = "int8", shape = (2, 20))#candidate|3639|(2, 20)|var|int8
output = func_3638(var_3639)
func_3640 = relay.Function([var_3639], output)
mutated_mod['func_3640'] = func_3640
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2562_call = mod.get_global_var('func_2562')
func_2564_call = mutated_mod.get_global_var('func_2564')
call_3647 = func_2562_call()
call_3648 = func_2562_call()
output = call_3647
output2 = call_3648
func_3650 = relay.Function([], output)
mod['func_3650'] = func_3650
mod = relay.transform.InferType()(mod)
mutated_mod['func_3650'] = func_3650
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3650_call = mutated_mod.get_global_var('func_3650')
call_3651 = func_3650_call()
output = call_3651
func_3652 = relay.Function([], output)
mutated_mod['func_3652'] = func_3652
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3650_call = mod.get_global_var('func_3650')
func_3652_call = mutated_mod.get_global_var('func_3652')
call_3653 = func_3650_call()
call_3654 = func_3650_call()
output = call_3653
output2 = call_3654
func_3659 = relay.Function([], output)
mod['func_3659'] = func_3659
mod = relay.transform.InferType()(mod)
output = func_3659()
func_3660 = relay.Function([], output)
mutated_mod['func_3660'] = func_3660
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3468_call = mod.get_global_var('func_3468')
func_3469_call = mutated_mod.get_global_var('func_3469')
call_3678 = relay.TupleGetItem(func_3468_call(), 0)
call_3679 = relay.TupleGetItem(func_3469_call(), 0)
output = relay.Tuple([call_3678,])
output2 = relay.Tuple([call_3679,])
func_3694 = relay.Function([], output)
mod['func_3694'] = func_3694
mod = relay.transform.InferType()(mod)
output = func_3694()
func_3695 = relay.Function([], output)
mutated_mod['func_3695'] = func_3695
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2042_call = mod.get_global_var('func_2042')
func_2044_call = mutated_mod.get_global_var('func_2044')
call_3707 = relay.TupleGetItem(func_2042_call(), 0)
call_3708 = relay.TupleGetItem(func_2044_call(), 0)
func_2042_call = mod.get_global_var('func_2042')
func_2044_call = mutated_mod.get_global_var('func_2044')
call_3711 = relay.TupleGetItem(func_2042_call(), 0)
call_3712 = relay.TupleGetItem(func_2044_call(), 0)
func_3468_call = mod.get_global_var('func_3468')
func_3469_call = mutated_mod.get_global_var('func_3469')
call_3717 = relay.TupleGetItem(func_3468_call(), 0)
call_3718 = relay.TupleGetItem(func_3469_call(), 0)
func_183_call = mod.get_global_var('func_183')
func_187_call = mutated_mod.get_global_var('func_187')
var_3721 = relay.var("var_3721", dtype = "float32", shape = (72,))#candidate|3721|(72,)|var|float32
const_3722 = relay.const([10,4,1,8,-8,-9,8,-6,-1,8,-5,-6,-6,5,5,-8,6,-6,10,8,-10,7,-5,2,5,7,-9,-7,3,7,-3,-2,-8,7,6,-8,-4,-6,-7,4,-2,-1,5,-4,-9,-8,-5,-5,-9,-1,-8,1,5,1,-8,3,8,-9,-2,-3,3,5,-2,-10,-3,-7,-3,4,-8,9,2,3,6,2,6,-10,7,-8,-6,-1,3,-1,-8,4,2,1,-7,-3,-8,-10,-2,-5,8,9,4,-4,-10,1,1,-4,-9,6,-9,9,-6,4,-1,-9,2,4,2,3,4,1,-9,8,-10,-6,-5,-10,5,-9,3,-5,7,-3,7,10,1,-7,-6,10,1,-9,-2,9,3,4,-5,-4,-8,3,4,7,7,-8,8,1,6,8,-10,-3,-5,10,-6,4,5,9,3,7,-7,2,-2,7,-4,-4,-1,7,4,8,6,-3,-1,10,-6,5,9,1,2,-7,-2,-3,10,1,-1,-3,10,6,8,-7,-3,10,-10,5,-8,10,-5,-6,-5,8,-3,3,-1,-9,6,-5,-8,3,7,-2,10,8,-9,2,-9,-9,5,10,-10,-5,4,-7,7,2,8,1,-10,-5,3,-10,-10,-5,-1,-9,3,-9,-5,9,6,10,-5,-2,-9,-3,-6,5,4,-1,6,-7], dtype = "int64")#candidate|3722|(250,)|const|int64
call_3720 = relay.TupleGetItem(func_183_call(relay.reshape(var_3721.astype('float32'), [12, 3, 2]), relay.reshape(const_3722.astype('int64'), [25, 10]), ), 1)
call_3723 = relay.TupleGetItem(func_187_call(relay.reshape(var_3721.astype('float32'), [12, 3, 2]), relay.reshape(const_3722.astype('int64'), [25, 10]), ), 1)
output = relay.Tuple([call_3707,call_3711,call_3717,call_3720,var_3721,const_3722,])
output2 = relay.Tuple([call_3708,call_3712,call_3718,call_3723,var_3721,const_3722,])
func_3731 = relay.Function([var_3721,], output)
mod['func_3731'] = func_3731
mod = relay.transform.InferType()(mod)
mutated_mod['func_3731'] = func_3731
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3732 = relay.var("var_3732", dtype = "float32", shape = (72,))#candidate|3732|(72,)|var|float32
func_3731_call = mutated_mod.get_global_var('func_3731')
call_3733 = func_3731_call(var_3732)
output = call_3733
func_3734 = relay.Function([var_3732], output)
mutated_mod['func_3734'] = func_3734
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3468_call = mod.get_global_var('func_3468')
func_3469_call = mutated_mod.get_global_var('func_3469')
call_3777 = relay.TupleGetItem(func_3468_call(), 1)
call_3778 = relay.TupleGetItem(func_3469_call(), 1)
var_3790 = relay.var("var_3790", dtype = "float64", shape = (9, 2, 2))#candidate|3790|(9, 2, 2)|var|float64
bop_3791 = relay.equal(call_3777.astype('bool'), relay.reshape(var_3790.astype('bool'), relay.shape_of(call_3777))) # shape=(9, 2, 2)
bop_3794 = relay.equal(call_3778.astype('bool'), relay.reshape(var_3790.astype('bool'), relay.shape_of(call_3778))) # shape=(9, 2, 2)
func_3650_call = mod.get_global_var('func_3650')
func_3652_call = mutated_mod.get_global_var('func_3652')
call_3796 = func_3650_call()
call_3797 = func_3650_call()
func_2248_call = mod.get_global_var('func_2248')
func_2251_call = mutated_mod.get_global_var('func_2251')
const_3818 = relay.const([2.727949,1.751052,-5.461705,5.243235,9.918511,5.998091,-9.500531,-8.465472,-8.090665,3.865615,9.541071,-2.738869,9.969183,-5.800875,-0.356997,0.970775,6.435421,-1.680898,-7.983449,4.934154,-7.614094,-5.965357,-9.022683,5.917455,-7.369249,-0.351359,3.265533,9.001122,-1.640838,2.276456,6.138947,0.543274,6.324574,-2.326296,8.509819,-0.855357,-9.197480,-3.686721,2.973069,-4.869214,-4.457252,3.325047,2.567424,-1.566806,-4.327290,-0.693428,-3.639012,0.633003,2.345421,0.624939,8.526541,0.752642,-2.094100,-5.541806,8.131409,6.403449,8.803831,7.800082,9.465890,0.253544,3.230459,5.780402,7.946570,-3.590680,-9.198438,4.392980,1.832032,-3.316582,5.793296,3.728360,5.070033,-4.864647,6.342036,8.109595,-3.011667,-9.373342,-6.042852,4.002713,-1.910873,7.413426,-2.568410,0.863421,1.856281,5.637481,-5.177786,6.657747,-0.387608,9.890141,-0.845616,-0.432040,9.728205,-1.512171,6.555925,4.031137,2.257955,-8.524636,9.900984,7.859162,4.423646,3.289807,8.991464,4.664910,2.179570,8.853560,9.005891,-1.135018,6.324643,6.646448,-4.347403,-7.116498,7.833083,1.424552], dtype = "float32")#candidate|3818|(112,)|const|float32
call_3817 = func_2248_call(relay.reshape(const_3818.astype('float32'), [1, 14, 8]))
call_3819 = func_2248_call(relay.reshape(const_3818.astype('float32'), [1, 14, 8]))
output = relay.Tuple([bop_3791,call_3796,call_3817,const_3818,])
output2 = relay.Tuple([bop_3794,call_3797,call_3819,const_3818,])
func_3829 = relay.Function([var_3790,], output)
mod['func_3829'] = func_3829
mod = relay.transform.InferType()(mod)
var_3830 = relay.var("var_3830", dtype = "float64", shape = (9, 2, 2))#candidate|3830|(9, 2, 2)|var|float64
output = func_3829(var_3830)
func_3831 = relay.Function([var_3830], output)
mutated_mod['func_3831'] = func_3831
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2201_call = mod.get_global_var('func_2201')
func_2203_call = mutated_mod.get_global_var('func_2203')
call_3906 = relay.TupleGetItem(func_2201_call(), 2)
call_3907 = relay.TupleGetItem(func_2203_call(), 2)
output = relay.Tuple([call_3906,])
output2 = relay.Tuple([call_3907,])
func_3908 = relay.Function([], output)
mod['func_3908'] = func_3908
mod = relay.transform.InferType()(mod)
mutated_mod['func_3908'] = func_3908
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3908_call = mutated_mod.get_global_var('func_3908')
call_3909 = func_3908_call()
output = call_3909
func_3910 = relay.Function([], output)
mutated_mod['func_3910'] = func_3910
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3422_call = mod.get_global_var('func_3422')
func_3424_call = mutated_mod.get_global_var('func_3424')
call_3918 = relay.TupleGetItem(func_3422_call(), 0)
call_3919 = relay.TupleGetItem(func_3424_call(), 0)
output = relay.Tuple([call_3918,])
output2 = relay.Tuple([call_3919,])
func_3920 = relay.Function([], output)
mod['func_3920'] = func_3920
mod = relay.transform.InferType()(mod)
mutated_mod['func_3920'] = func_3920
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3920_call = mutated_mod.get_global_var('func_3920')
call_3921 = func_3920_call()
output = call_3921
func_3922 = relay.Function([], output)
mutated_mod['func_3922'] = func_3922
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3694_call = mod.get_global_var('func_3694')
func_3695_call = mutated_mod.get_global_var('func_3695')
call_3926 = relay.TupleGetItem(func_3694_call(), 0)
call_3927 = relay.TupleGetItem(func_3695_call(), 0)
output = call_3926
output2 = call_3927
func_3930 = relay.Function([], output)
mod['func_3930'] = func_3930
mod = relay.transform.InferType()(mod)
mutated_mod['func_3930'] = func_3930
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3930_call = mutated_mod.get_global_var('func_3930')
call_3931 = func_3930_call()
output = call_3931
func_3932 = relay.Function([], output)
mutated_mod['func_3932'] = func_3932
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3532_call = mod.get_global_var('func_3532')
func_3533_call = mutated_mod.get_global_var('func_3533')
call_3953 = relay.TupleGetItem(func_3532_call(), 0)
call_3954 = relay.TupleGetItem(func_3533_call(), 0)
output = call_3953
output2 = call_3954
func_3961 = relay.Function([], output)
mod['func_3961'] = func_3961
mod = relay.transform.InferType()(mod)
mutated_mod['func_3961'] = func_3961
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3961_call = mutated_mod.get_global_var('func_3961')
call_3962 = func_3961_call()
output = call_3962
func_3963 = relay.Function([], output)
mutated_mod['func_3963'] = func_3963
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3468_call = mod.get_global_var('func_3468')
func_3469_call = mutated_mod.get_global_var('func_3469')
call_3969 = relay.TupleGetItem(func_3468_call(), 1)
call_3970 = relay.TupleGetItem(func_3469_call(), 1)
output = call_3969
output2 = call_3970
func_3995 = relay.Function([], output)
mod['func_3995'] = func_3995
mod = relay.transform.InferType()(mod)
output = func_3995()
func_3996 = relay.Function([], output)
mutated_mod['func_3996'] = func_3996
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3468_call = mod.get_global_var('func_3468')
func_3469_call = mutated_mod.get_global_var('func_3469')
call_4004 = relay.TupleGetItem(func_3468_call(), 1)
call_4005 = relay.TupleGetItem(func_3469_call(), 1)
output = relay.Tuple([call_4004,])
output2 = relay.Tuple([call_4005,])
func_4009 = relay.Function([], output)
mod['func_4009'] = func_4009
mod = relay.transform.InferType()(mod)
output = func_4009()
func_4010 = relay.Function([], output)
mutated_mod['func_4010'] = func_4010
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4013 = relay.var("var_4013", dtype = "int16", shape = ())#candidate|4013|()|var|int16
var_4014 = relay.var("var_4014", dtype = "int16", shape = (1, 11, 1))#candidate|4014|(1, 11, 1)|var|int16
bop_4015 = relay.subtract(var_4013.astype('int16'), var_4014.astype('int16')) # shape=(1, 11, 1)
output = relay.Tuple([bop_4015,])
output2 = relay.Tuple([bop_4015,])
func_4029 = relay.Function([var_4013,var_4014,], output)
mod['func_4029'] = func_4029
mod = relay.transform.InferType()(mod)
var_4030 = relay.var("var_4030", dtype = "int16", shape = ())#candidate|4030|()|var|int16
var_4031 = relay.var("var_4031", dtype = "int16", shape = (1, 11, 1))#candidate|4031|(1, 11, 1)|var|int16
output = func_4029(var_4030,var_4031,)
func_4032 = relay.Function([var_4030,var_4031,], output)
mutated_mod['func_4032'] = func_4032
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3217_call = mod.get_global_var('func_3217')
func_3219_call = mutated_mod.get_global_var('func_3219')
call_4113 = func_3217_call()
call_4114 = func_3217_call()
output = relay.Tuple([call_4113,])
output2 = relay.Tuple([call_4114,])
func_4115 = relay.Function([], output)
mod['func_4115'] = func_4115
mod = relay.transform.InferType()(mod)
mutated_mod['func_4115'] = func_4115
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4115_call = mutated_mod.get_global_var('func_4115')
call_4116 = func_4115_call()
output = call_4116
func_4117 = relay.Function([], output)
mutated_mod['func_4117'] = func_4117
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2275_call = mod.get_global_var('func_2275')
func_2276_call = mutated_mod.get_global_var('func_2276')
call_4209 = func_2275_call()
call_4210 = func_2275_call()
output = call_4209
output2 = call_4210
func_4218 = relay.Function([], output)
mod['func_4218'] = func_4218
mod = relay.transform.InferType()(mod)
mutated_mod['func_4218'] = func_4218
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4218_call = mutated_mod.get_global_var('func_4218')
call_4219 = func_4218_call()
output = call_4219
func_4220 = relay.Function([], output)
mutated_mod['func_4220'] = func_4220
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4400 = relay.var("var_4400", dtype = "float32", shape = (9, 16, 9))#candidate|4400|(9, 16, 9)|var|float32
const_4401 = relay.const([[[2.666837,9.063646,1.966137,-2.488572,7.121967,-4.528956,0.982649,-2.861442,2.644166],[4.308183,-6.984308,0.381716,-1.369082,-6.477117,1.447560,-3.970500,-5.405673,5.821576],[-7.469136,-3.545258,-8.633661,-6.422922,4.316745,5.211289,6.398420,-0.233818,0.098681],[-1.814141,-1.456984,-0.187517,-0.131890,-1.846761,-5.408439,-7.136034,-1.577096,-3.972647],[0.008112,-3.765460,3.478955,8.423285,-1.381068,4.800441,9.569562,9.929565,-7.122859],[5.780857,-3.178169,0.863091,3.944801,7.680757,0.509135,4.297703,-7.682883,8.391964],[2.030577,-7.346718,-3.896554,8.996285,-0.442515,4.018047,-4.014810,4.258759,8.329441],[-4.380119,3.351152,-6.112433,6.782660,2.589464,3.799848,-0.358911,-8.813403,-3.158624],[-4.709639,-7.124464,4.957040,1.292978,3.696299,-9.301105,3.060161,2.870450,4.724639],[3.543357,4.145911,-6.445089,3.852742,9.750479,-8.171960,-9.723436,3.849478,9.065684],[2.943730,4.948985,4.788043,1.095173,-3.726638,1.803498,-1.776542,-1.798735,-5.175614],[-2.755458,4.953434,6.774351,3.956725,-1.090406,-2.416088,8.984964,-7.567212,-1.867803],[6.736582,9.853958,2.395524,0.324896,2.412615,9.009800,-7.656449,-8.662979,-5.603818],[3.861091,4.359416,-8.403237,4.285233,3.756241,-3.819390,-8.584755,1.761159,6.914688],[-1.972028,-3.648756,9.559770,2.533681,1.723214,2.601743,5.400644,-2.880931,7.446036],[5.908178,-9.534435,-2.518683,-4.053105,-2.631862,-4.580688,-0.804770,-5.505946,9.506942]],[[9.501024,-7.608335,-8.256623,-4.601620,-8.393147,-8.367432,0.399087,2.407132,1.109758],[5.269793,-8.643474,3.005283,1.355157,9.655834,9.880373,7.387947,-7.941183,5.917425],[-2.347705,-2.011384,-8.770917,-4.542167,-1.596765,-9.042695,0.804888,-2.740543,6.783985],[9.586196,2.000635,0.468475,3.620992,4.754844,-4.318034,-0.249322,-5.634501,2.842413],[8.846076,8.911637,5.484043,9.476920,0.320799,-5.992242,-8.822286,4.210339,6.025202],[-2.595628,-2.006154,-2.852525,-6.696130,8.444743,9.875684,-9.586106,-9.239675,3.377657],[1.353796,-4.043960,-4.402637,6.397866,-5.626184,-1.889076,4.457221,-1.706068,8.378262],[-0.627535,6.002498,-7.123106,9.004274,-6.167527,-2.318818,4.536937,-2.551245,-7.181123],[0.656728,5.357214,8.562252,5.665259,-4.223294,-8.036335,-5.602063,-6.400265,-9.726355],[-1.796162,2.550648,0.102313,-6.226958,6.334697,-8.467527,6.437607,5.549724,-9.804459],[4.984688,-1.080767,2.277387,2.885767,5.785038,-3.114299,-9.129618,8.020753,8.399314],[-0.235593,-7.290491,-3.692929,2.768869,-6.653742,6.704886,0.259151,-9.616531,-9.002407],[-2.808763,9.209905,3.471164,6.288964,-7.380244,5.041901,9.673638,-6.492703,1.115732],[5.131966,-1.620082,-7.618778,-8.378409,-2.016284,8.380183,-1.319977,-1.288165,6.471639],[2.623247,-1.970958,-5.440775,1.544092,0.205898,6.763121,3.361564,3.833404,-7.377688],[0.164224,-6.112561,9.307739,-1.443222,3.809930,8.524305,2.172161,-9.628766,-5.813252]],[[9.192587,-5.645538,7.775416,-7.101304,-5.623904,0.232650,2.752065,5.802007,-5.213493],[1.715479,8.909672,-2.790504,1.362375,2.840074,6.786408,-1.809587,-2.523654,0.227492],[-1.390073,-8.221519,5.998932,7.325138,-3.430161,-9.558030,8.939094,3.721053,8.400931],[6.541935,0.943786,-7.147804,3.885989,-6.705754,7.224627,6.037242,8.984802,9.751512],[7.770700,7.671012,5.565161,3.401416,5.235961,1.497769,-5.627992,0.597014,-1.091349],[-8.686320,7.288016,0.163344,-3.552422,-3.842697,-0.069148,-9.209809,3.483807,0.186874],[-4.910899,5.008563,9.368532,-5.282363,-5.909309,-9.349837,8.255862,-6.032579,9.774370],[3.137141,-6.488739,3.041677,9.819226,8.135003,2.671567,-3.006366,6.234980,0.399957],[-1.027011,-9.123988,7.127249,7.915460,6.274006,6.342705,4.663482,-0.499206,3.587104],[-1.527531,8.073425,1.731767,-0.613288,-1.097957,3.761081,4.064294,0.956522,-2.905571],[-8.930238,9.892793,1.144035,-5.441583,-2.402243,8.754563,-5.827496,-6.513683,4.025977],[-9.352598,7.993879,9.385221,-1.701472,8.030439,-8.360328,-4.760784,5.986966,-9.330668],[6.146057,-7.241849,0.137826,6.778284,1.964679,4.312896,1.355683,8.132062,3.406317],[1.241718,0.913232,2.632439,4.872752,-2.102968,-7.551759,1.307048,5.051790,2.994133],[8.120082,-8.232469,-0.213952,5.994227,2.369806,1.900737,2.605118,-0.523149,9.390751],[-5.930400,0.251307,3.938022,5.351117,9.911055,-1.618392,0.138278,4.379844,6.412193]],[[-7.254480,0.658659,5.608186,-5.394269,-8.150244,4.158126,-7.483811,-5.903732,-3.786365],[8.957656,-4.484822,-6.123659,1.587000,8.612046,5.439973,9.241566,7.432462,6.364412],[7.264563,-6.949645,-1.475276,3.079028,1.341861,-3.472014,1.315179,-8.156422,6.536314],[6.470552,-5.784404,7.025416,3.228697,6.446578,-4.755884,3.440740,-0.100082,0.411290],[6.109570,-0.870553,-3.454601,-7.317035,-5.321888,6.070308,9.272082,1.607281,3.153550],[2.647667,2.758625,-6.470669,2.514425,0.318351,8.738040,-9.457086,3.564570,0.919175],[1.568286,8.680326,-7.081666,8.607304,4.745924,-7.006025,-3.738743,5.765664,-4.530525],[9.284502,2.717782,-9.769076,1.662748,9.510207,9.061999,-9.193799,-8.771750,-8.159134],[-2.455176,-4.689921,-1.887029,1.709772,-1.348206,-5.980337,-2.057693,-7.791656,-5.867376],[-4.071867,8.739615,-7.371243,-1.603884,-8.203071,7.658446,-6.263585,-1.545708,1.208900],[5.831170,1.159214,-7.561017,-8.642252,7.755080,-8.907238,8.190373,9.695513,6.306624],[8.686585,-4.479035,-3.527380,3.633486,-9.757508,-4.067934,-4.516416,-1.395842,3.625550],[-7.896806,9.372098,2.266303,6.694587,-4.979722,8.589789,4.052482,1.283201,-8.633014],[6.284801,-0.121722,-6.749839,6.807891,-0.554663,-6.675346,-1.012887,-0.230079,9.205446],[-9.228463,-2.163206,1.135947,-6.514192,5.951673,3.481991,3.249597,7.316441,-7.348043],[-7.191489,-8.748584,1.756789,9.196887,6.842896,3.475951,3.537528,-3.244088,-8.439802]],[[9.862099,-2.853870,-0.280142,1.032491,-5.917653,-4.487608,-9.288835,-7.323199,8.613733],[0.354891,-9.823504,-5.858869,1.111931,3.089422,-7.633565,-1.742151,-4.677755,-4.964942],[-5.845096,-3.816589,-0.387796,0.890240,-6.778175,0.992919,7.247836,-0.515394,-0.272151],[1.537789,-5.848876,7.500506,-0.570578,-0.496376,-9.077693,0.801524,-5.520361,9.363252],[-1.790645,0.357367,-1.973865,2.446542,-7.786435,7.681315,-4.072717,-5.450943,2.751744],[0.225537,1.442644,-2.325884,-1.930551,-2.436647,-6.412378,1.097474,-6.735618,3.091704],[-2.292634,-4.368692,-9.823827,9.375490,-5.852862,2.572527,9.774524,2.192045,-9.135873],[-1.161185,-4.690908,-7.766823,-5.049096,9.154982,-2.130428,4.550975,0.819217,2.529957],[-1.543771,4.079834,7.690589,-8.555782,2.939431,9.183156,-4.156518,1.307454,2.331749],[4.447219,1.637305,-8.739001,4.191378,-8.655485,-4.434800,-2.863392,-9.722305,0.870529],[-2.483051,-4.698424,-1.640662,9.639124,9.658894,2.358497,-9.041700,-3.203177,7.758933],[-2.403793,2.127131,-0.783521,-9.483796,-3.747723,-6.184292,-8.819980,9.309085,-3.723181],[7.945773,-0.317444,-4.810501,8.126231,-0.389999,8.064766,-9.231979,-3.147334,-8.795580],[8.901420,0.268814,-0.842056,-0.411821,-0.519143,1.809871,8.464348,6.636910,-4.744597],[3.376551,-7.134869,3.565580,2.336266,1.161874,0.143633,-0.754712,6.074836,-1.344573],[4.022361,-7.757457,4.477799,6.180603,-3.019542,-9.978972,-6.935545,-2.879984,-0.067937]],[[-7.050725,-9.795079,3.488357,-8.436727,-7.659724,-3.826831,9.906986,7.430495,6.209179],[6.074405,2.187088,9.176339,-1.565064,0.743600,8.995613,0.264660,-7.525269,1.764428],[4.464871,7.752571,8.359218,9.704737,-0.419533,6.508457,3.660286,-8.341884,-5.752095],[-7.796303,8.428318,-8.105562,9.958209,7.819301,6.209959,-1.644782,-8.891122,-8.627601],[1.097030,-1.293977,9.142715,1.314812,-6.114268,6.554414,-2.093838,-8.997689,-7.959384],[-2.137332,-9.338348,7.478237,-9.104580,-1.956425,8.079837,9.153604,-7.669154,-2.220303],[1.146872,-2.451410,1.807882,-3.482125,-7.205252,-7.930498,0.938476,-5.772818,-6.286924],[8.287607,3.274810,5.700546,5.450243,1.472101,-6.443927,2.255333,-6.547161,5.231210],[7.999134,7.886784,-1.554275,-8.026178,-3.381685,4.001614,-7.744067,7.416222,5.635415],[2.289438,2.193016,-2.506538,-7.018346,0.847308,-0.943049,6.456609,0.092505,7.230741],[-3.601816,1.499306,-6.626459,1.807406,-6.500311,3.491395,5.513622,-4.807805,7.859344],[-4.509786,-2.738833,-6.177233,-6.042192,-4.831378,-7.424463,-4.541936,-1.076086,2.148009],[-8.976986,8.438272,-3.136691,-8.955963,4.404427,-2.221886,-7.164673,1.805329,8.818740],[2.881910,8.816831,6.584821,6.782377,-4.064803,1.744130,-9.177523,-6.309307,-0.223979],[-5.420362,-4.562019,3.511240,2.218443,5.981218,-9.006882,-8.537026,-9.622894,-8.036507],[-2.507761,9.722589,3.769024,-7.500370,3.293791,7.206500,6.295376,-7.747467,-9.529928]],[[0.330876,4.116425,-0.640329,0.849337,7.734588,-3.511629,0.241016,9.937020,9.432419],[5.321957,3.691650,-3.696330,3.762580,-4.571142,1.135393,5.895466,-0.686492,9.917636],[4.399173,-0.866691,-4.321848,-8.114101,6.397598,9.404242,-4.394892,-9.739094,9.067408],[-0.934934,6.633197,-2.961404,3.374706,9.604079,9.820602,-6.673686,8.752706,1.803305],[9.057873,1.797740,-4.988982,9.849921,0.508606,-3.744736,-8.296756,4.006418,2.116070],[-2.024994,-6.653641,6.199489,-8.959086,-7.296192,-8.812526,-5.184205,4.102945,-3.549952],[-4.987639,-5.724664,6.233462,-8.985709,5.085479,8.379662,7.163414,-2.907748,0.769757],[2.711110,4.078144,8.490907,-8.352225,-3.444740,7.067717,6.270871,-8.614599,-3.449763],[-1.943009,-4.990366,-5.639178,-8.214351,5.779072,0.965974,-4.756972,0.499035,-1.980180],[5.531772,-9.753895,-0.153578,-0.774700,4.216051,0.524596,5.849843,-0.451588,-2.793626],[0.339666,-7.273203,1.321583,-4.350376,8.163062,1.903775,-1.253321,-5.221484,-0.948715],[1.355947,-7.563705,-7.014798,-8.065043,4.359540,1.732929,3.740687,-4.633501,3.993407],[-2.320505,-5.311980,8.567327,4.211630,-1.518652,-7.718303,8.479934,-3.194634,-1.638930],[0.116973,-9.399428,4.618600,-4.729143,-3.207585,2.995177,-8.437768,9.388082,8.208106],[0.263620,5.075370,-8.199103,-1.137375,5.186527,9.513619,3.904143,-8.673858,3.562233],[9.502673,-3.739699,-4.434560,-4.772450,9.326957,1.063478,-9.210025,-3.643103,7.946197]],[[-3.507620,-6.086852,-7.103863,9.868189,-3.381836,4.582846,-9.253191,-5.025694,-8.008307],[-0.455156,6.659229,8.122175,-3.033685,8.908943,0.870633,6.602602,5.051491,5.693544],[1.238122,9.441745,-2.602835,5.476907,-9.069022,3.251372,-1.477893,5.699258,-8.076440],[7.608947,-5.255215,8.490103,0.640275,9.671031,-1.835717,-9.829432,-5.398243,9.784036],[-1.182098,8.767015,-1.883248,8.600269,-3.517218,8.886844,6.506563,7.401427,1.144718],[1.571045,5.611235,5.882990,3.236085,8.468890,-4.741155,-5.128563,0.601217,5.201763],[1.657141,-3.614882,1.590506,-9.730182,-4.653473,-1.984136,-4.348358,-6.956947,7.274011],[9.002219,1.994555,-0.437930,8.510944,-8.575742,-5.903307,2.608835,2.760289,9.513136],[0.079179,9.493354,7.679329,8.028527,-9.967250,8.378754,-2.606188,-4.408166,7.909154],[3.105695,-4.499606,3.101689,8.492847,-4.314242,-1.671637,1.240892,3.353775,-9.967351],[-9.009714,-8.187754,8.705105,-4.065556,-7.890558,-7.857872,2.365862,-1.524805,9.790514],[-4.496451,-3.917847,4.820257,-0.607514,-0.936831,-6.879647,-4.850792,7.862611,9.773352],[-0.453659,-0.699922,-8.036291,-2.343625,-5.780118,6.021915,-9.838595,-1.081886,-3.934976],[-0.696166,-8.467273,-7.003515,3.297966,3.465681,8.835619,1.478826,3.832320,-9.172630],[-1.158249,5.777936,-0.472405,6.000839,4.919065,5.407051,9.717073,-5.515441,7.950293],[-4.911063,-4.913860,8.712810,-2.420493,3.157035,-2.345644,-1.479704,9.940971,0.934791]],[[-6.023370,-0.700005,-3.895742,-5.266229,7.655939,0.203226,1.864873,2.625284,5.513489],[-8.326697,-9.193821,1.046418,1.792505,4.268657,-2.868392,-8.745768,2.343110,-9.877613],[9.258114,-0.155448,2.652999,8.910787,3.217795,-4.104422,4.428205,2.319605,8.502915],[-7.032412,-5.225519,4.656061,-1.598083,2.162149,-6.999592,7.028576,-4.192611,7.551913],[0.434068,7.640404,1.772692,9.813902,-1.762481,-6.008221,-2.475421,-7.076192,1.971174],[8.684503,-8.963888,5.993976,-5.685006,-3.526464,-4.667475,-5.166504,-0.571455,3.586308],[-3.881139,-3.346936,3.529508,-0.285891,8.781080,-2.930359,-2.306938,-5.444010,-3.159484],[2.527565,-7.675379,-8.159232,8.973155,-5.737631,-0.808573,-5.782826,-2.967246,0.408082],[5.004574,0.482652,-0.387131,0.833613,1.032632,1.874062,-0.340946,-5.399336,-7.957608],[2.675831,-0.374970,6.026536,0.289440,2.452753,-3.865498,2.531501,-6.114561,-5.147204],[-3.442089,5.318484,5.963717,-8.051275,2.185596,-9.856073,6.328463,-1.479683,7.870026],[-1.983749,3.349013,1.667383,-4.721449,8.265214,9.381948,4.435783,-7.853965,-4.232063],[-3.133715,7.396867,5.199746,3.398862,7.528366,-1.335949,-2.295260,-6.225636,-0.254723],[9.347392,-3.159962,7.588768,7.680162,-9.234810,6.424271,7.181071,4.246042,-8.593027],[6.260549,8.007013,9.330321,6.206468,-9.976959,2.128570,1.115642,5.361217,7.705121],[-6.129128,8.243050,-9.915241,0.976735,-0.517800,-3.943723,8.044425,1.991825,4.963251]]], dtype = "float32")#candidate|4401|(9, 16, 9)|const|float32
bop_4402 = relay.power(var_4400.astype('float32'), relay.reshape(const_4401.astype('float32'), relay.shape_of(var_4400))) # shape=(9, 16, 9)
func_3908_call = mod.get_global_var('func_3908')
func_3910_call = mutated_mod.get_global_var('func_3910')
call_4405 = relay.TupleGetItem(func_3908_call(), 0)
call_4406 = relay.TupleGetItem(func_3910_call(), 0)
var_4423 = relay.var("var_4423", dtype = "float32", shape = (9, 16, 9))#candidate|4423|(9, 16, 9)|var|float32
bop_4424 = relay.logical_and(const_4401.astype('bool'), relay.reshape(var_4423.astype('bool'), relay.shape_of(const_4401))) # shape=(9, 16, 9)
func_2702_call = mod.get_global_var('func_2702')
func_2703_call = mutated_mod.get_global_var('func_2703')
call_4430 = relay.TupleGetItem(func_2702_call(), 2)
call_4431 = relay.TupleGetItem(func_2703_call(), 2)
output = relay.Tuple([bop_4402,call_4405,bop_4424,call_4430,])
output2 = relay.Tuple([bop_4402,call_4406,bop_4424,call_4431,])
func_4437 = relay.Function([var_4400,var_4423,], output)
mod['func_4437'] = func_4437
mod = relay.transform.InferType()(mod)
var_4438 = relay.var("var_4438", dtype = "float32", shape = (9, 16, 9))#candidate|4438|(9, 16, 9)|var|float32
var_4439 = relay.var("var_4439", dtype = "float32", shape = (9, 16, 9))#candidate|4439|(9, 16, 9)|var|float32
output = func_4437(var_4438,var_4439,)
func_4440 = relay.Function([var_4438,var_4439,], output)
mutated_mod['func_4440'] = func_4440
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2993_call = mod.get_global_var('func_2993')
func_2995_call = mutated_mod.get_global_var('func_2995')
call_4523 = relay.TupleGetItem(func_2993_call(), 3)
call_4524 = relay.TupleGetItem(func_2995_call(), 3)
func_4115_call = mod.get_global_var('func_4115')
func_4117_call = mutated_mod.get_global_var('func_4117')
call_4530 = relay.TupleGetItem(func_4115_call(), 0)
call_4531 = relay.TupleGetItem(func_4117_call(), 0)
output = relay.Tuple([call_4523,call_4530,])
output2 = relay.Tuple([call_4524,call_4531,])
func_4544 = relay.Function([], output)
mod['func_4544'] = func_4544
mod = relay.transform.InferType()(mod)
output = func_4544()
func_4545 = relay.Function([], output)
mutated_mod['func_4545'] = func_4545
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2545_call = mod.get_global_var('func_2545')
func_2546_call = mutated_mod.get_global_var('func_2546')
call_4571 = relay.TupleGetItem(func_2545_call(), 0)
call_4572 = relay.TupleGetItem(func_2546_call(), 0)
func_2226_call = mod.get_global_var('func_2226')
func_2227_call = mutated_mod.get_global_var('func_2227')
call_4584 = func_2226_call()
call_4585 = func_2226_call()
func_2275_call = mod.get_global_var('func_2275')
func_2276_call = mutated_mod.get_global_var('func_2276')
call_4587 = func_2275_call()
call_4588 = func_2275_call()
output = relay.Tuple([call_4571,call_4584,call_4587,])
output2 = relay.Tuple([call_4572,call_4585,call_4588,])
func_4593 = relay.Function([], output)
mod['func_4593'] = func_4593
mod = relay.transform.InferType()(mod)
output = func_4593()
func_4594 = relay.Function([], output)
mutated_mod['func_4594'] = func_4594
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3532_call = mod.get_global_var('func_3532')
func_3533_call = mutated_mod.get_global_var('func_3533')
call_4790 = relay.TupleGetItem(func_3532_call(), 0)
call_4791 = relay.TupleGetItem(func_3533_call(), 0)
func_3059_call = mod.get_global_var('func_3059')
func_3062_call = mutated_mod.get_global_var('func_3062')
const_4806 = relay.const(-2, dtype = "uint32")#candidate|4806|()|const|uint32
const_4807 = relay.const([-10,7,-7,10,10,-8,-9,-1,-3,5,-1,-10,10,5,6,1,6,-1,4,6,-5,-10,9,-3,8,-2,2,2,-1,-8,-10,5,6,8,7,-3,-8,7,6,-4,9,-1,-9,4,9,-8,-10,4,1,5,8,10,-3,-7,-8,-1,-6,-7,7,-6,-5,5,7,3,-3,-6,8,-9,3,-8,-7,-6,-5,-2,6,9,2,9,5,-9,-10,-9,9,7,-6,-2,8,-7,-3,-5,7,-10,-10,-10,1,-3,-2,-9,-2,4,-3,-10,6,-2,-6,-8,3,-4,9,1,-1,2,9,-8,-8,-7,-1,-2,4,-6,2,-5,-5,1,-3,5,7,1,9,-4,-4,-7,-8,3,-2,-4,4,1,-10,-5,-5,1,8,-7,-3,-5,4,1,-1,-5,3,9,-1,-9,7,6,-4,5,8,10,-4,8,7,1,-4,-2,6,-6,-6,-7,-9,-4,-1,7,-2,1,-4,-6,-8,8,3,-1,-3,-7,-4,-1,-9,-9,3,-10,-5,-1,-7,7,-3,-7,8,5,-7,-2,9,5,8,8,10,-6,-6,1,3,-9,6,3,6,-5,2,-5,1,-9,-5,-10,-3,-1,5,-4,-1,-5,1,-1,7,1,3,10,-9,5,-6,-9,3,-7,4,-7,4,-2,-9,5,10,5,3,9,6,6,-1,10,6,4,-9,-5,-2,-2,-1,-7,5,8,9,2,3,7,4,10,5,10,-5,-10,3,8,-1,6,-8,5,-2,-5,4,9,-7,8,2,-7,2,-2,9,8,6,5,-8,1,7,5,8,-9,-2,9,4,9,-3,-10,10,2,4,9,-8,-2,-8,6,10,1,2,-5,5,-6,-4,1,-6,1,-2,2,5,-5,-8,9,6,-9,9,9,-8,2,-3,10,-10,9,-3,4,-2,1,1,7,9,8,-2,3,3,-5,-10,4,-8,-2,2,1,6,-6,-1,4,1,-7,10,4,-5,8,6,7,-6,4,-6,4,6,-9,-2,-6,-7,-5,-5,10,10,7,-1,7,-3,7,-8,1,8,-3,-3,3,-6,-8,-9,-2,8,4,-4,-7,6,6,5,-9,7,3,-5,-1,7,1,-8,7,-2,5,2,5,-6,-3,10,5,-6,-9,-7,1,2,1,6,-5,-9,-6,-2,10,-4,10,6,1,-6,-2,-1,-8,-6,-2,-7,3,-7,8,2,9,2,9,-7,-10,9,7,-7,-4,3,7,2,7,-3,-7,4,10,-7,2,9,6,-3,1,-7,-5,10,-2,6,-10,-6,-3,-4,6,3,-5,9,-2,6,4,-6,-4,3,-7,-7,5,5,-4,10,-10,10,-5,9,-1,9,-8,4,-1,10,-5,6,-10,7,-10,6,10,-7,4,2,-1,-1,-8,-1,-4,-9,-7,1,10,3,-7,-1,-4,-3,4,-4,-6,6,-1,-3,9,6,-8,3,-4], dtype = "uint32")#candidate|4807|(540,)|const|uint32
call_4805 = relay.TupleGetItem(func_3059_call(relay.reshape(const_4806.astype('uint32'), []), relay.reshape(const_4807.astype('uint32'), [6, 10, 9]), ), 1)
call_4808 = relay.TupleGetItem(func_3062_call(relay.reshape(const_4806.astype('uint32'), []), relay.reshape(const_4807.astype('uint32'), [6, 10, 9]), ), 1)
func_4009_call = mod.get_global_var('func_4009')
func_4010_call = mutated_mod.get_global_var('func_4010')
call_4810 = relay.TupleGetItem(func_4009_call(), 0)
call_4811 = relay.TupleGetItem(func_4010_call(), 0)
func_4115_call = mod.get_global_var('func_4115')
func_4117_call = mutated_mod.get_global_var('func_4117')
call_4813 = relay.TupleGetItem(func_4115_call(), 0)
call_4814 = relay.TupleGetItem(func_4117_call(), 0)
func_3650_call = mod.get_global_var('func_3650')
func_3652_call = mutated_mod.get_global_var('func_3652')
call_4815 = func_3650_call()
call_4816 = func_3650_call()
func_3217_call = mod.get_global_var('func_3217')
func_3219_call = mutated_mod.get_global_var('func_3219')
call_4839 = func_3217_call()
call_4840 = func_3217_call()
uop_4847 = relay.asin(call_4810.astype('float32')) # shape=(9, 2, 2)
uop_4849 = relay.asin(call_4811.astype('float32')) # shape=(9, 2, 2)
func_2545_call = mod.get_global_var('func_2545')
func_2546_call = mutated_mod.get_global_var('func_2546')
call_4853 = relay.TupleGetItem(func_2545_call(), 0)
call_4854 = relay.TupleGetItem(func_2546_call(), 0)
func_2393_call = mod.get_global_var('func_2393')
func_2395_call = mutated_mod.get_global_var('func_2395')
call_4869 = relay.TupleGetItem(func_2393_call(), 2)
call_4870 = relay.TupleGetItem(func_2395_call(), 2)
func_4544_call = mod.get_global_var('func_4544')
func_4545_call = mutated_mod.get_global_var('func_4545')
call_4871 = relay.TupleGetItem(func_4544_call(), 1)
call_4872 = relay.TupleGetItem(func_4545_call(), 1)
output = relay.Tuple([call_4790,call_4805,const_4806,const_4807,call_4813,call_4815,call_4839,uop_4847,call_4853,call_4869,call_4871,])
output2 = relay.Tuple([call_4791,call_4808,const_4806,const_4807,call_4814,call_4816,call_4840,uop_4849,call_4854,call_4870,call_4872,])
func_4876 = relay.Function([], output)
mod['func_4876'] = func_4876
mod = relay.transform.InferType()(mod)
mutated_mod['func_4876'] = func_4876
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4876_call = mutated_mod.get_global_var('func_4876')
call_4877 = func_4876_call()
output = call_4877
func_4878 = relay.Function([], output)
mutated_mod['func_4878'] = func_4878
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2993_call = mod.get_global_var('func_2993')
func_2995_call = mutated_mod.get_global_var('func_2995')
call_4906 = relay.TupleGetItem(func_2993_call(), 0)
call_4907 = relay.TupleGetItem(func_2995_call(), 0)
func_4029_call = mod.get_global_var('func_4029')
func_4032_call = mutated_mod.get_global_var('func_4032')
var_4915 = relay.var("var_4915", dtype = "int16", shape = ())#candidate|4915|()|var|int16
var_4916 = relay.var("var_4916", dtype = "int16", shape = (11,))#candidate|4916|(11,)|var|int16
call_4914 = relay.TupleGetItem(func_4029_call(relay.reshape(var_4915.astype('int16'), []), relay.reshape(var_4916.astype('int16'), [1, 11, 1]), ), 0)
call_4917 = relay.TupleGetItem(func_4032_call(relay.reshape(var_4915.astype('int16'), []), relay.reshape(var_4916.astype('int16'), [1, 11, 1]), ), 0)
output = relay.Tuple([call_4906,call_4914,var_4915,var_4916,])
output2 = relay.Tuple([call_4907,call_4917,var_4915,var_4916,])
func_4934 = relay.Function([var_4915,var_4916,], output)
mod['func_4934'] = func_4934
mod = relay.transform.InferType()(mod)
mutated_mod['func_4934'] = func_4934
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4934_call = mutated_mod.get_global_var('func_4934')
var_4936 = relay.var("var_4936", dtype = "int16", shape = ())#candidate|4936|()|var|int16
var_4937 = relay.var("var_4937", dtype = "int16", shape = (11,))#candidate|4937|(11,)|var|int16
call_4935 = func_4934_call(var_4936,var_4937,)
output = call_4935
func_4938 = relay.Function([var_4936,var_4937,], output)
mutated_mod['func_4938'] = func_4938
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3995_call = mod.get_global_var('func_3995')
func_3996_call = mutated_mod.get_global_var('func_3996')
call_4963 = func_3995_call()
call_4964 = func_3995_call()
output = relay.Tuple([call_4963,])
output2 = relay.Tuple([call_4964,])
func_4965 = relay.Function([], output)
mod['func_4965'] = func_4965
mod = relay.transform.InferType()(mod)
output = func_4965()
func_4966 = relay.Function([], output)
mutated_mod['func_4966'] = func_4966
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4593_call = mod.get_global_var('func_4593')
func_4594_call = mutated_mod.get_global_var('func_4594')
call_5004 = relay.TupleGetItem(func_4593_call(), 2)
call_5005 = relay.TupleGetItem(func_4594_call(), 2)
output = relay.Tuple([call_5004,])
output2 = relay.Tuple([call_5005,])
func_5010 = relay.Function([], output)
mod['func_5010'] = func_5010
mod = relay.transform.InferType()(mod)
output = func_5010()
func_5011 = relay.Function([], output)
mutated_mod['func_5011'] = func_5011
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2486_call = mod.get_global_var('func_2486')
func_2487_call = mutated_mod.get_global_var('func_2487')
call_5073 = func_2486_call()
call_5074 = func_2486_call()
output = relay.Tuple([call_5073,])
output2 = relay.Tuple([call_5074,])
func_5079 = relay.Function([], output)
mod['func_5079'] = func_5079
mod = relay.transform.InferType()(mod)
output = func_5079()
func_5080 = relay.Function([], output)
mutated_mod['func_5080'] = func_5080
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3532_call = mod.get_global_var('func_3532')
func_3533_call = mutated_mod.get_global_var('func_3533')
call_5084 = relay.TupleGetItem(func_3532_call(), 2)
call_5085 = relay.TupleGetItem(func_3533_call(), 2)
output = relay.Tuple([call_5084,])
output2 = relay.Tuple([call_5085,])
func_5086 = relay.Function([], output)
mod['func_5086'] = func_5086
mod = relay.transform.InferType()(mod)
mutated_mod['func_5086'] = func_5086
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5086_call = mutated_mod.get_global_var('func_5086')
call_5087 = func_5086_call()
output = call_5087
func_5088 = relay.Function([], output)
mutated_mod['func_5088'] = func_5088
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2702_call = mod.get_global_var('func_2702')
func_2703_call = mutated_mod.get_global_var('func_2703')
call_5178 = relay.TupleGetItem(func_2702_call(), 0)
call_5179 = relay.TupleGetItem(func_2703_call(), 0)
output = relay.Tuple([call_5178,])
output2 = relay.Tuple([call_5179,])
func_5189 = relay.Function([], output)
mod['func_5189'] = func_5189
mod = relay.transform.InferType()(mod)
output = func_5189()
func_5190 = relay.Function([], output)
mutated_mod['func_5190'] = func_5190
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3995_call = mod.get_global_var('func_3995')
func_3996_call = mutated_mod.get_global_var('func_3996')
call_5223 = func_3995_call()
call_5224 = func_3995_call()
output = relay.Tuple([call_5223,])
output2 = relay.Tuple([call_5224,])
func_5233 = relay.Function([], output)
mod['func_5233'] = func_5233
mod = relay.transform.InferType()(mod)
mutated_mod['func_5233'] = func_5233
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5233_call = mutated_mod.get_global_var('func_5233')
call_5234 = func_5233_call()
output = call_5234
func_5235 = relay.Function([], output)
mutated_mod['func_5235'] = func_5235
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2993_call = mod.get_global_var('func_2993')
func_2995_call = mutated_mod.get_global_var('func_2995')
call_5247 = relay.TupleGetItem(func_2993_call(), 1)
call_5248 = relay.TupleGetItem(func_2995_call(), 1)
var_5259 = relay.var("var_5259", dtype = "uint16", shape = (9, 2, 2))#candidate|5259|(9, 2, 2)|var|uint16
bop_5260 = relay.logical_xor(call_5247.astype('int64'), relay.reshape(var_5259.astype('int64'), relay.shape_of(call_5247))) # shape=(9, 2, 2)
bop_5263 = relay.logical_xor(call_5248.astype('int64'), relay.reshape(var_5259.astype('int64'), relay.shape_of(call_5248))) # shape=(9, 2, 2)
output = bop_5260
output2 = bop_5263
func_5265 = relay.Function([var_5259,], output)
mod['func_5265'] = func_5265
mod = relay.transform.InferType()(mod)
mutated_mod['func_5265'] = func_5265
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5266 = relay.var("var_5266", dtype = "uint16", shape = (9, 2, 2))#candidate|5266|(9, 2, 2)|var|uint16
func_5265_call = mutated_mod.get_global_var('func_5265')
call_5267 = func_5265_call(var_5266)
output = call_5267
func_5268 = relay.Function([var_5266], output)
mutated_mod['func_5268'] = func_5268
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2226_call = mod.get_global_var('func_2226')
func_2227_call = mutated_mod.get_global_var('func_2227')
call_5289 = func_2226_call()
call_5290 = func_2226_call()
output = relay.Tuple([call_5289,])
output2 = relay.Tuple([call_5290,])
func_5295 = relay.Function([], output)
mod['func_5295'] = func_5295
mod = relay.transform.InferType()(mod)
mutated_mod['func_5295'] = func_5295
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5295_call = mutated_mod.get_global_var('func_5295')
call_5296 = func_5295_call()
output = call_5296
func_5297 = relay.Function([], output)
mutated_mod['func_5297'] = func_5297
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3217_call = mod.get_global_var('func_3217')
func_3219_call = mutated_mod.get_global_var('func_3219')
call_5326 = func_3217_call()
call_5327 = func_3217_call()
func_3468_call = mod.get_global_var('func_3468')
func_3469_call = mutated_mod.get_global_var('func_3469')
call_5330 = relay.TupleGetItem(func_3468_call(), 1)
call_5331 = relay.TupleGetItem(func_3469_call(), 1)
func_3468_call = mod.get_global_var('func_3468')
func_3469_call = mutated_mod.get_global_var('func_3469')
call_5355 = relay.TupleGetItem(func_3468_call(), 1)
call_5356 = relay.TupleGetItem(func_3469_call(), 1)
uop_5367 = relay.sqrt(call_5326.astype('float64')) # shape=(9, 2, 2)
uop_5369 = relay.sqrt(call_5327.astype('float64')) # shape=(9, 2, 2)
func_5086_call = mod.get_global_var('func_5086')
func_5088_call = mutated_mod.get_global_var('func_5088')
call_5371 = relay.TupleGetItem(func_5086_call(), 0)
call_5372 = relay.TupleGetItem(func_5088_call(), 0)
output = relay.Tuple([call_5330,call_5355,uop_5367,call_5371,])
output2 = relay.Tuple([call_5331,call_5356,uop_5369,call_5372,])
func_5375 = relay.Function([], output)
mod['func_5375'] = func_5375
mod = relay.transform.InferType()(mod)
output = func_5375()
func_5376 = relay.Function([], output)
mutated_mod['func_5376'] = func_5376
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3920_call = mod.get_global_var('func_3920')
func_3922_call = mutated_mod.get_global_var('func_3922')
call_5394 = relay.TupleGetItem(func_3920_call(), 0)
call_5395 = relay.TupleGetItem(func_3922_call(), 0)
output = relay.Tuple([call_5394,])
output2 = relay.Tuple([call_5395,])
func_5408 = relay.Function([], output)
mod['func_5408'] = func_5408
mod = relay.transform.InferType()(mod)
mutated_mod['func_5408'] = func_5408
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5408_call = mutated_mod.get_global_var('func_5408')
call_5409 = func_5408_call()
output = call_5409
func_5410 = relay.Function([], output)
mutated_mod['func_5410'] = func_5410
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3908_call = mod.get_global_var('func_3908')
func_3910_call = mutated_mod.get_global_var('func_3910')
call_5440 = relay.TupleGetItem(func_3908_call(), 0)
call_5441 = relay.TupleGetItem(func_3910_call(), 0)
output = call_5440
output2 = call_5441
func_5457 = relay.Function([], output)
mod['func_5457'] = func_5457
mod = relay.transform.InferType()(mod)
mutated_mod['func_5457'] = func_5457
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5457_call = mutated_mod.get_global_var('func_5457')
call_5458 = func_5457_call()
output = call_5458
func_5459 = relay.Function([], output)
mutated_mod['func_5459'] = func_5459
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3920_call = mod.get_global_var('func_3920')
func_3922_call = mutated_mod.get_global_var('func_3922')
call_5495 = relay.TupleGetItem(func_3920_call(), 0)
call_5496 = relay.TupleGetItem(func_3922_call(), 0)
var_5512 = relay.var("var_5512", dtype = "uint8", shape = (10, 10, 4))#candidate|5512|(10, 10, 4)|var|uint8
bop_5513 = relay.mod(call_5495.astype('float64'), relay.reshape(var_5512.astype('float64'), relay.shape_of(call_5495))) # shape=(10, 10, 4)
bop_5516 = relay.mod(call_5496.astype('float64'), relay.reshape(var_5512.astype('float64'), relay.shape_of(call_5496))) # shape=(10, 10, 4)
const_5517 = relay.const([[[-4,-8,-10,-9],[9,-9,-6,-7],[-4,-1,6,9],[6,-1,-7,-6],[2,2,-8,-9],[4,-3,2,-5],[5,-7,-2,6],[-2,-8,6,10],[7,7,4,-4],[3,7,5,4]],[[-9,-10,-7,8],[5,-10,7,-8],[3,2,3,-8],[-1,-4,8,-6],[-8,8,3,7],[-2,-1,-9,5],[-6,1,-1,8],[5,-8,-1,-2],[1,8,-5,-1],[2,-6,-1,-4]],[[6,-8,4,10],[-9,4,3,3],[-5,-7,6,5],[-10,-10,2,9],[9,8,5,-5],[-6,-6,-5,10],[-10,8,5,-5],[-8,7,6,9],[-3,-1,5,-3],[-4,-8,10,9]],[[-7,7,4,-8],[-6,2,2,9],[10,-4,-5,4],[7,-8,-3,10],[-4,5,-10,8],[-9,10,-4,7],[-1,9,-9,5],[6,-5,-10,3],[2,2,1,10],[4,3,10,-2]],[[-2,-5,3,-7],[5,1,8,1],[-2,-4,7,-6],[1,-9,-1,2],[-1,4,-8,4],[-4,-1,9,-2],[7,3,-7,4],[-8,1,-3,5],[-1,-9,-2,4],[-8,-10,-9,7]],[[8,9,-10,-7],[6,-8,-2,-3],[3,-4,5,-3],[-3,9,5,7],[7,-3,6,3],[-10,1,5,-7],[-5,3,8,-4],[-9,2,-8,-9],[4,-2,-4,2],[-8,-5,6,5]],[[-2,-3,6,-1],[10,-1,4,-5],[-4,9,-2,9],[6,6,8,5],[-10,10,6,9],[9,-4,9,-1],[6,8,-3,-9],[5,-10,5,-2],[-4,10,-8,-5],[10,9,-1,-2]],[[-2,-5,1,5],[7,8,-1,-8],[-5,-4,-7,1],[10,-7,-10,-8],[-3,-1,-4,10],[-2,-5,1,7],[-2,-10,-1,6],[-8,-2,6,-5],[10,-5,2,8],[-4,-4,-8,10]],[[3,-9,-10,4],[2,8,-6,8],[9,-2,9,-5],[-5,-7,-2,-3],[6,7,-10,3],[7,-9,6,-8],[-1,8,-2,-10],[-1,-2,-5,-6],[-8,8,-6,-10],[-4,-5,-6,-9]],[[-7,6,9,-6],[4,-1,-2,1],[-2,8,2,10],[-6,-8,1,-3],[2,8,7,2],[-2,2,2,6],[4,1,-3,-2],[9,5,-7,8],[6,-3,-10,6],[-7,-7,-4,4]]], dtype = "uint8")#candidate|5517|(10, 10, 4)|const|uint8
bop_5518 = relay.divide(call_5495.astype('float32'), relay.reshape(const_5517.astype('float32'), relay.shape_of(call_5495))) # shape=(10, 10, 4)
bop_5521 = relay.divide(call_5496.astype('float32'), relay.reshape(const_5517.astype('float32'), relay.shape_of(call_5496))) # shape=(10, 10, 4)
var_5523 = relay.var("var_5523", dtype = "uint8", shape = (10, 10, 4))#candidate|5523|(10, 10, 4)|var|uint8
bop_5524 = relay.greater(var_5512.astype('bool'), relay.reshape(var_5523.astype('bool'), relay.shape_of(var_5512))) # shape=(10, 10, 4)
output = relay.Tuple([bop_5513,bop_5518,bop_5524,])
output2 = relay.Tuple([bop_5516,bop_5521,bop_5524,])
func_5529 = relay.Function([var_5512,var_5523,], output)
mod['func_5529'] = func_5529
mod = relay.transform.InferType()(mod)
mutated_mod['func_5529'] = func_5529
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5529_call = mutated_mod.get_global_var('func_5529')
var_5531 = relay.var("var_5531", dtype = "uint8", shape = (10, 10, 4))#candidate|5531|(10, 10, 4)|var|uint8
var_5532 = relay.var("var_5532", dtype = "uint8", shape = (10, 10, 4))#candidate|5532|(10, 10, 4)|var|uint8
call_5530 = func_5529_call(var_5531,var_5532,)
output = call_5530
func_5533 = relay.Function([var_5531,var_5532,], output)
mutated_mod['func_5533'] = func_5533
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2393_call = mod.get_global_var('func_2393')
func_2395_call = mutated_mod.get_global_var('func_2395')
call_5590 = relay.TupleGetItem(func_2393_call(), 2)
call_5591 = relay.TupleGetItem(func_2395_call(), 2)
output = call_5590
output2 = call_5591
func_5608 = relay.Function([], output)
mod['func_5608'] = func_5608
mod = relay.transform.InferType()(mod)
output = func_5608()
func_5609 = relay.Function([], output)
mutated_mod['func_5609'] = func_5609
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5079_call = mod.get_global_var('func_5079')
func_5080_call = mutated_mod.get_global_var('func_5080')
call_5698 = relay.TupleGetItem(func_5079_call(), 0)
call_5699 = relay.TupleGetItem(func_5080_call(), 0)
func_3034_call = mod.get_global_var('func_3034')
func_3036_call = mutated_mod.get_global_var('func_3036')
call_5707 = relay.TupleGetItem(func_3034_call(), 0)
call_5708 = relay.TupleGetItem(func_3036_call(), 0)
func_4009_call = mod.get_global_var('func_4009')
func_4010_call = mutated_mod.get_global_var('func_4010')
call_5724 = relay.TupleGetItem(func_4009_call(), 0)
call_5725 = relay.TupleGetItem(func_4010_call(), 0)
output = relay.Tuple([call_5698,call_5707,call_5724,])
output2 = relay.Tuple([call_5699,call_5708,call_5725,])
func_5734 = relay.Function([], output)
mod['func_5734'] = func_5734
mod = relay.transform.InferType()(mod)
mutated_mod['func_5734'] = func_5734
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5734_call = mutated_mod.get_global_var('func_5734')
call_5735 = func_5734_call()
output = call_5735
func_5736 = relay.Function([], output)
mutated_mod['func_5736'] = func_5736
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3034_call = mod.get_global_var('func_3034')
func_3036_call = mutated_mod.get_global_var('func_3036')
call_5737 = relay.TupleGetItem(func_3034_call(), 0)
call_5738 = relay.TupleGetItem(func_3036_call(), 0)
func_3217_call = mod.get_global_var('func_3217')
func_3219_call = mutated_mod.get_global_var('func_3219')
call_5752 = func_3217_call()
call_5753 = func_3217_call()
output = relay.Tuple([call_5737,call_5752,])
output2 = relay.Tuple([call_5738,call_5753,])
func_5778 = relay.Function([], output)
mod['func_5778'] = func_5778
mod = relay.transform.InferType()(mod)
output = func_5778()
func_5779 = relay.Function([], output)
mutated_mod['func_5779'] = func_5779
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4115_call = mod.get_global_var('func_4115')
func_4117_call = mutated_mod.get_global_var('func_4117')
call_5800 = relay.TupleGetItem(func_4115_call(), 0)
call_5801 = relay.TupleGetItem(func_4117_call(), 0)
func_3468_call = mod.get_global_var('func_3468')
func_3469_call = mutated_mod.get_global_var('func_3469')
call_5811 = relay.TupleGetItem(func_3468_call(), 1)
call_5812 = relay.TupleGetItem(func_3469_call(), 1)
func_5265_call = mod.get_global_var('func_5265')
func_5268_call = mutated_mod.get_global_var('func_5268')
call_5814 = func_5265_call(relay.reshape(call_5811.astype('uint16'), [9, 2, 2]))
call_5815 = func_5265_call(relay.reshape(call_5811.astype('uint16'), [9, 2, 2]))
output = relay.Tuple([call_5800,call_5811,call_5814,])
output2 = relay.Tuple([call_5801,call_5812,call_5815,])
func_5816 = relay.Function([], output)
mod['func_5816'] = func_5816
mod = relay.transform.InferType()(mod)
mutated_mod['func_5816'] = func_5816
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5816_call = mutated_mod.get_global_var('func_5816')
call_5817 = func_5816_call()
output = call_5817
func_5818 = relay.Function([], output)
mutated_mod['func_5818'] = func_5818
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5079_call = mod.get_global_var('func_5079')
func_5080_call = mutated_mod.get_global_var('func_5080')
call_5819 = relay.TupleGetItem(func_5079_call(), 0)
call_5820 = relay.TupleGetItem(func_5080_call(), 0)
func_5457_call = mod.get_global_var('func_5457')
func_5459_call = mutated_mod.get_global_var('func_5459')
call_5858 = func_5457_call()
call_5859 = func_5457_call()
output = relay.Tuple([call_5819,call_5858,])
output2 = relay.Tuple([call_5820,call_5859,])
func_5900 = relay.Function([], output)
mod['func_5900'] = func_5900
mod = relay.transform.InferType()(mod)
mutated_mod['func_5900'] = func_5900
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5900_call = mutated_mod.get_global_var('func_5900')
call_5901 = func_5900_call()
output = call_5901
func_5902 = relay.Function([], output)
mutated_mod['func_5902'] = func_5902
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2201_call = mod.get_global_var('func_2201')
func_2203_call = mutated_mod.get_global_var('func_2203')
call_5997 = relay.TupleGetItem(func_2201_call(), 0)
call_5998 = relay.TupleGetItem(func_2203_call(), 0)
output = call_5997
output2 = call_5998
func_6010 = relay.Function([], output)
mod['func_6010'] = func_6010
mod = relay.transform.InferType()(mod)
output = func_6010()
func_6011 = relay.Function([], output)
mutated_mod['func_6011'] = func_6011
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5816_call = mod.get_global_var('func_5816')
func_5818_call = mutated_mod.get_global_var('func_5818')
call_6058 = relay.TupleGetItem(func_5816_call(), 2)
call_6059 = relay.TupleGetItem(func_5818_call(), 2)
output = call_6058
output2 = call_6059
func_6068 = relay.Function([], output)
mod['func_6068'] = func_6068
mod = relay.transform.InferType()(mod)
mutated_mod['func_6068'] = func_6068
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6068_call = mutated_mod.get_global_var('func_6068')
call_6069 = func_6068_call()
output = call_6069
func_6070 = relay.Function([], output)
mutated_mod['func_6070'] = func_6070
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3995_call = mod.get_global_var('func_3995')
func_3996_call = mutated_mod.get_global_var('func_3996')
call_6134 = func_3995_call()
call_6135 = func_3995_call()
func_3258_call = mod.get_global_var('func_3258')
func_3259_call = mutated_mod.get_global_var('func_3259')
call_6141 = relay.TupleGetItem(func_3258_call(), 1)
call_6142 = relay.TupleGetItem(func_3259_call(), 1)
output = relay.Tuple([call_6134,call_6141,])
output2 = relay.Tuple([call_6135,call_6142,])
func_6143 = relay.Function([], output)
mod['func_6143'] = func_6143
mod = relay.transform.InferType()(mod)
output = func_6143()
func_6144 = relay.Function([], output)
mutated_mod['func_6144'] = func_6144
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2993_call = mod.get_global_var('func_2993')
func_2995_call = mutated_mod.get_global_var('func_2995')
call_6248 = relay.TupleGetItem(func_2993_call(), 0)
call_6249 = relay.TupleGetItem(func_2995_call(), 0)
output = call_6248
output2 = call_6249
func_6263 = relay.Function([], output)
mod['func_6263'] = func_6263
mod = relay.transform.InferType()(mod)
mutated_mod['func_6263'] = func_6263
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6263_call = mutated_mod.get_global_var('func_6263')
call_6264 = func_6263_call()
output = call_6264
func_6265 = relay.Function([], output)
mutated_mod['func_6265'] = func_6265
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3650_call = mod.get_global_var('func_3650')
func_3652_call = mutated_mod.get_global_var('func_3652')
call_6304 = func_3650_call()
call_6305 = func_3650_call()
output = call_6304
output2 = call_6305
func_6313 = relay.Function([], output)
mod['func_6313'] = func_6313
mod = relay.transform.InferType()(mod)
output = func_6313()
func_6314 = relay.Function([], output)
mutated_mod['func_6314'] = func_6314
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4876_call = mod.get_global_var('func_4876')
func_4878_call = mutated_mod.get_global_var('func_4878')
call_6362 = relay.TupleGetItem(func_4876_call(), 2)
call_6363 = relay.TupleGetItem(func_4878_call(), 2)
func_3151_call = mod.get_global_var('func_3151')
func_3155_call = mutated_mod.get_global_var('func_3155')
var_6365 = relay.var("var_6365", dtype = "int32", shape = (1144,))#candidate|6365|(1144,)|var|int32
call_6364 = relay.TupleGetItem(func_3151_call(relay.reshape(var_6365.astype('int32'), [11, 13, 8]), relay.reshape(var_6365.astype('int32'), [11, 13, 8]), ), 0)
call_6366 = relay.TupleGetItem(func_3155_call(relay.reshape(var_6365.astype('int32'), [11, 13, 8]), relay.reshape(var_6365.astype('int32'), [11, 13, 8]), ), 0)
func_541_call = mod.get_global_var('func_541')
func_544_call = mutated_mod.get_global_var('func_544')
var_6382 = relay.var("var_6382", dtype = "int8", shape = (40,))#candidate|6382|(40,)|var|int8
var_6383 = relay.var("var_6383", dtype = "int8", shape = (1, 400))#candidate|6383|(1, 400)|var|int8
call_6381 = func_541_call(relay.reshape(var_6382.astype('int8'), [10, 1, 4]), relay.reshape(var_6383.astype('int8'), [10, 10, 4]), )
call_6384 = func_541_call(relay.reshape(var_6382.astype('int8'), [10, 1, 4]), relay.reshape(var_6383.astype('int8'), [10, 10, 4]), )
func_5233_call = mod.get_global_var('func_5233')
func_5235_call = mutated_mod.get_global_var('func_5235')
call_6393 = relay.TupleGetItem(func_5233_call(), 0)
call_6394 = relay.TupleGetItem(func_5235_call(), 0)
output = relay.Tuple([call_6362,call_6364,var_6365,call_6381,var_6382,var_6383,call_6393,])
output2 = relay.Tuple([call_6363,call_6366,var_6365,call_6384,var_6382,var_6383,call_6394,])
func_6399 = relay.Function([var_6365,var_6382,var_6383,], output)
mod['func_6399'] = func_6399
mod = relay.transform.InferType()(mod)
var_6400 = relay.var("var_6400", dtype = "int32", shape = (1144,))#candidate|6400|(1144,)|var|int32
var_6401 = relay.var("var_6401", dtype = "int8", shape = (40,))#candidate|6401|(40,)|var|int8
var_6402 = relay.var("var_6402", dtype = "int8", shape = (1, 400))#candidate|6402|(1, 400)|var|int8
output = func_6399(var_6400,var_6401,var_6402,)
func_6403 = relay.Function([var_6400,var_6401,var_6402,], output)
mutated_mod['func_6403'] = func_6403
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5010_call = mod.get_global_var('func_5010')
func_5011_call = mutated_mod.get_global_var('func_5011')
call_6410 = relay.TupleGetItem(func_5010_call(), 0)
call_6411 = relay.TupleGetItem(func_5011_call(), 0)
output = relay.Tuple([call_6410,])
output2 = relay.Tuple([call_6411,])
func_6412 = relay.Function([], output)
mod['func_6412'] = func_6412
mod = relay.transform.InferType()(mod)
mutated_mod['func_6412'] = func_6412
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6412_call = mutated_mod.get_global_var('func_6412')
call_6413 = func_6412_call()
output = call_6413
func_6414 = relay.Function([], output)
mutated_mod['func_6414'] = func_6414
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5608_call = mod.get_global_var('func_5608')
func_5609_call = mutated_mod.get_global_var('func_5609')
call_6503 = func_5608_call()
call_6504 = func_5608_call()
func_3920_call = mod.get_global_var('func_3920')
func_3922_call = mutated_mod.get_global_var('func_3922')
call_6540 = relay.TupleGetItem(func_3920_call(), 0)
call_6541 = relay.TupleGetItem(func_3922_call(), 0)
uop_6547 = relay.acos(call_6540.astype('float32')) # shape=(10, 10, 4)
uop_6549 = relay.acos(call_6541.astype('float32')) # shape=(10, 10, 4)
func_6412_call = mod.get_global_var('func_6412')
func_6414_call = mutated_mod.get_global_var('func_6414')
call_6563 = relay.TupleGetItem(func_6412_call(), 0)
call_6564 = relay.TupleGetItem(func_6414_call(), 0)
output = relay.Tuple([call_6503,uop_6547,call_6563,])
output2 = relay.Tuple([call_6504,uop_6549,call_6564,])
func_6567 = relay.Function([], output)
mod['func_6567'] = func_6567
mod = relay.transform.InferType()(mod)
output = func_6567()
func_6568 = relay.Function([], output)
mutated_mod['func_6568'] = func_6568
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6263_call = mod.get_global_var('func_6263')
func_6265_call = mutated_mod.get_global_var('func_6265')
call_6611 = func_6263_call()
call_6612 = func_6263_call()
output = relay.Tuple([call_6611,])
output2 = relay.Tuple([call_6612,])
func_6619 = relay.Function([], output)
mod['func_6619'] = func_6619
mod = relay.transform.InferType()(mod)
mutated_mod['func_6619'] = func_6619
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6619_call = mutated_mod.get_global_var('func_6619')
call_6620 = func_6619_call()
output = call_6620
func_6621 = relay.Function([], output)
mutated_mod['func_6621'] = func_6621
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6143_call = mod.get_global_var('func_6143')
func_6144_call = mutated_mod.get_global_var('func_6144')
call_6630 = relay.TupleGetItem(func_6143_call(), 0)
call_6631 = relay.TupleGetItem(func_6144_call(), 0)
output = relay.Tuple([call_6630,])
output2 = relay.Tuple([call_6631,])
func_6643 = relay.Function([], output)
mod['func_6643'] = func_6643
mod = relay.transform.InferType()(mod)
output = func_6643()
func_6644 = relay.Function([], output)
mutated_mod['func_6644'] = func_6644
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3920_call = mod.get_global_var('func_3920')
func_3922_call = mutated_mod.get_global_var('func_3922')
call_6685 = relay.TupleGetItem(func_3920_call(), 0)
call_6686 = relay.TupleGetItem(func_3922_call(), 0)
func_5900_call = mod.get_global_var('func_5900')
func_5902_call = mutated_mod.get_global_var('func_5902')
call_6692 = relay.TupleGetItem(func_5900_call(), 1)
call_6693 = relay.TupleGetItem(func_5902_call(), 1)
output = relay.Tuple([call_6685,call_6692,])
output2 = relay.Tuple([call_6686,call_6693,])
func_6717 = relay.Function([], output)
mod['func_6717'] = func_6717
mod = relay.transform.InferType()(mod)
mutated_mod['func_6717'] = func_6717
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6717_call = mutated_mod.get_global_var('func_6717')
call_6718 = func_6717_call()
output = call_6718
func_6719 = relay.Function([], output)
mutated_mod['func_6719'] = func_6719
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2304_call = mod.get_global_var('func_2304')
func_2306_call = mutated_mod.get_global_var('func_2306')
call_6774 = relay.TupleGetItem(func_2304_call(), 0)
call_6775 = relay.TupleGetItem(func_2306_call(), 0)
func_366_call = mod.get_global_var('func_366')
func_370_call = mutated_mod.get_global_var('func_370')
var_6793 = relay.var("var_6793", dtype = "float64", shape = (252,))#candidate|6793|(252,)|var|float64
var_6794 = relay.var("var_6794", dtype = "int16", shape = (1, 1521))#candidate|6794|(1, 1521)|var|int16
var_6795 = relay.var("var_6795", dtype = "int64", shape = (250,))#candidate|6795|(250,)|var|int64
call_6792 = relay.TupleGetItem(func_366_call(relay.reshape(var_6793.astype('float64'), [9, 2, 14]), relay.reshape(var_6794.astype('int16'), [1, 1521]), relay.reshape(var_6795.astype('int64'), [250,]), ), 2)
call_6796 = relay.TupleGetItem(func_370_call(relay.reshape(var_6793.astype('float64'), [9, 2, 14]), relay.reshape(var_6794.astype('int16'), [1, 1521]), relay.reshape(var_6795.astype('int64'), [250,]), ), 2)
uop_6800 = relay.sin(var_6794.astype('float32')) # shape=(1, 1521)
func_3059_call = mod.get_global_var('func_3059')
func_3062_call = mutated_mod.get_global_var('func_3062')
const_6803 = relay.const(1, dtype = "uint32")#candidate|6803|()|const|uint32
const_6804 = relay.const([-2,1,-4,5,2,8,7,-4,-3,-10,-7,8,-10,-6,-4,2,-5,-9,6,2,-6,-5,-8,4,3,8,6,3,-6,1,-7,5,8,10,-2,9,5,-2,4,-4,-7,-6,-8,-1,8,-4,4,7,-5,-7,1,4,-1,-9,-4,1,-5,6,-6,8,10,-10,-3,-8,6,-5,3,-1,8,9,-2,3,7,-1,-8,-8,-10,3,-7,-2,-8,8,-8,6,-8,8,-3,-7,4,-3,6,-1,2,-10,8,-4,10,-8,2,4,6,9,-7,-2,-2,-3,8,5,-1,1,-10,6,8,6,-5,-9,6,-2,4,-4,-9,-7,5,9,10,5,-6,7,2,-5,8,2,3,7,-10,-8,-9,7,8,2,-7,-5,8,10,-7,-9,-10,9,6,3,-6,-4,5,-1,-9,-8,-9,-1,8,7,4,-10,-8,10,-4,8,3,5,5,-10,10,-1,2,6,-1,5,10,2,6,-1,-4,-8,-5,4,10,4,-1,-7,-7,2,7,-3,-5,-6,-6,9,10,-6,2,-2,-1,10,-1,4,-3,6,-6,-6,6,9,-1,-4,6,3,-10,-8,-3,-5,-9,-4,7,-10,-1,-3,-2,-10,1,-3,6,4,-3,8,-3,4,-4,-4,-10,-6,-3,-9,1,8,-5,-8,-9,6,-7,9,9,-1,6,6,2,-7,2,1,-7,-5,10,-5,8,-10,-6,-4,-6,10,2,8,-7,-8,2,2,8,4,-3,-8,10,5,-9,-3,-3,9,-8,-9,1,-5,7,-4,9,5,-9,-2,-1,9,5,6,-6,5,-9,2,-2,-5,-6,-5,9,6,3,10,-6,-3,-2,3,4,-3,-2,7,4,4,2,-7,-1,10,-3,-5,1,2,-7,-1,-4,-7,1,-2,-5,5,8,-8,-4,-1,1,8,4,-5,-6,5,3,6,-6,-9,5,-8,-5,-1,5,6,10,7,-3,-6,-9,6,-4,5,1,1,-5,10,-5,9,-3,-5,-10,-8,3,1,-6,3,1,2,-10,-7,-1,-5,6,-6,2,3,-4,-2,-6,8,-1,-1,-6,2,7,-1,6,7,-3,-4,-4,4,9,-4,10,-6,10,-3,2,2,-7,-8,-10,-7,-7,7,-10,-1,8,2,7,1,7,6,1,7,-5,-3,9,10,-10,7,-10,9,-4,-8,-10,10,4,5,8,-5,8,-7,-7,10,6,7,6,3,-8,-2,-9,6,-10,1,4,10,4,-8,6,8,5,-5,-3,4,-1,-10,9,-6,-6,5,-2,1,-2,-7,-6,10,2,6,-6,-7,-5,9,-10,2,-3,5,2,1,4,4,-5,-3,10,2,-8,-4,5,-8,10,2,-7,-9,6,4,-10,-2,-3,-3,2,2,6,4,1,10,-2,-3,1,7,-1,-7,-9,9,-4,6,8,10,4,-7,8,6,-2,-6,-10,2,3,-6,10,4], dtype = "uint32")#candidate|6804|(540,)|const|uint32
call_6802 = relay.TupleGetItem(func_3059_call(relay.reshape(const_6803.astype('uint32'), []), relay.reshape(const_6804.astype('uint32'), [6, 10, 9]), ), 0)
call_6805 = relay.TupleGetItem(func_3062_call(relay.reshape(const_6803.astype('uint32'), []), relay.reshape(const_6804.astype('uint32'), [6, 10, 9]), ), 0)
bop_6815 = relay.subtract(uop_6800.astype('float32'), relay.reshape(var_6794.astype('float32'), relay.shape_of(uop_6800))) # shape=(1, 1521)
uop_6828 = relay.exp(bop_6815.astype('float32')) # shape=(1, 1521)
uop_6830 = relay.acosh(uop_6828.astype('float32')) # shape=(1, 1521)
func_118_call = mod.get_global_var('func_118')
func_123_call = mutated_mod.get_global_var('func_123')
call_6832 = relay.TupleGetItem(func_118_call(relay.reshape(var_6795.astype('int64'), [5, 10, 5]), relay.reshape(var_6795.astype('int64'), [5, 10, 5]), relay.reshape(uop_6800.astype('int16'), [1521,]), ), 2)
call_6833 = relay.TupleGetItem(func_123_call(relay.reshape(var_6795.astype('int64'), [5, 10, 5]), relay.reshape(var_6795.astype('int64'), [5, 10, 5]), relay.reshape(uop_6800.astype('int16'), [1521,]), ), 2)
var_6835 = relay.var("var_6835", dtype = "float32", shape = (11, 1521))#candidate|6835|(11, 1521)|var|float32
bop_6836 = relay.maximum(uop_6830.astype('uint32'), var_6835.astype('uint32')) # shape=(11, 1521)
uop_6839 = relay.asinh(uop_6830.astype('float32')) # shape=(1, 1521)
const_6846 = relay.const([[6.944499,2.391454,-9.392308,2.754475,1.412736,9.125685,2.176696,0.539012,8.769779,1.274724,9.654107,0.145311,-3.496905,-8.416064,-9.600919,-1.533477,7.105568,7.781729,-0.914073,-7.389844,6.072130,4.943002,-6.175351,5.737301,-8.745549,5.530836,3.285579,8.082590,-2.702127,1.739523,4.195295,-6.576858,-2.203617,-3.821832,-2.513863,-8.704232,-6.856461,4.906617,1.429110,-5.426703,7.870945,5.622651,4.180826,-9.094653,-1.772429,-0.806769,1.525792,-2.105189,-5.137351,-5.220349,-4.890173,-3.315835,3.416588,8.363900,-8.693083,-7.212992,-1.265092,-1.104209,-7.365656,2.156541,5.178226,-3.200424,-8.752551,-0.229778,7.042171,8.321094,5.258375,7.502818,2.533084,7.626132,-4.727478,-1.077462,-3.580180,-5.882878,2.173556,8.615483,6.648833,-0.715316,4.453281,5.333181,2.652958,-1.352454,-5.289954,0.624598,-3.311880,-1.115945,7.972644,7.150400,2.966580,-0.693504,0.360187,9.974490,-8.741864,-8.708453,-3.394620,-1.855890,9.882167,9.881758,-6.042202,5.964368,4.390700,-8.601169,-5.227134,-3.164179,4.652978,9.004463,6.366637,-1.761259,-9.284233,4.384947,-0.492129,-4.029896,-1.784188,6.347822,3.872912,1.182979,-0.204973,3.447706,-0.532015,9.009687,-8.361267,-5.632950,7.361869,2.953676,-3.103667,9.165709,8.259234,-2.244435,6.998912,-5.386213,-8.679044,7.108728,1.892228,-7.459870,9.957378,-8.937533,-7.118967,9.394191,9.219451,4.241899,4.466802,-1.630063,-0.472662,-2.811316,-5.402751,-8.395663,-3.106542,-4.966195,-6.602655,8.555166,-8.339530,-6.536798,7.900119,-1.393682,-8.117678,-1.752481,-9.920643,-5.002362,6.099466,-9.640698,-4.611687,-3.401367,7.892874,-8.652987,6.908727,9.656480,0.990687,-5.154238,2.162569,6.158902,-4.906985,3.500516,-6.702737,-4.880551,-9.287871,-0.911510,0.570154,9.926109,7.725938,5.836625,-5.190017,-4.198259,-3.910238,-5.233325,4.833324,3.961479,3.652791,6.067826,5.224256,4.926824,-1.257070,-2.442746,-4.008609,-1.600800,3.389159,9.385620,-0.121322,-3.877645,-1.784822,-4.216359,-3.238277,-0.002810,-5.366755,-8.971748,2.876977,5.766796,7.121722,9.157062,-5.995669,8.934629,0.485676,5.305451,-4.474507,-8.664392,-7.238231,-4.719802,0.390586,-5.482718,-8.561268,3.935628,-4.507224,-6.402002,-8.806502,3.332629,4.885307,-9.483157,5.778455,0.012480,1.946827,8.318762,-1.413716,6.065593,-2.833232,-0.241001,-0.236034,-3.838967,-4.904191,-2.679842,-9.909211,0.814840,-8.419877,0.021672,5.128720,0.421550,-5.023502,-9.342746,-9.211017,-3.043666,0.834441,-4.447944,-7.869078,-9.491134,9.643731,4.269508,0.862447,3.233481,4.205173,3.443121,4.085735,0.647479,1.423668,9.348468,1.215993,-1.436992,-1.854560,-3.462755,5.720872,5.052549,5.231075,7.644220,-3.867792,-1.189993,7.145260,-4.465517,-3.147014,-1.447827,-1.040597,-4.612929,-2.743345,-0.523583,3.492532,2.426355,-2.483415,4.796895,-2.910184,-9.830633,4.317065,-0.940067,-5.743793,-1.211338,-0.774848,5.882784,-8.004297,3.508492,-6.762323,9.478248,-8.893041,3.110203,1.215017,8.687872,6.143168,-7.146030,-8.111529,6.022372,-2.361966,-1.379761,-2.214439,8.036621,9.239261,7.054337,-9.303931,1.233249,-7.697989,0.214962,5.040426,7.222035,-6.814858,2.698635,-1.205022,-4.834985,-5.578311,9.502975,-5.672174,5.300077,4.112492,7.029427,3.256519,2.676172,6.228842,-0.947497,3.687281,6.374839,7.044293,-3.300521,9.145870,-2.886654,6.010466,8.437949,-5.741397,9.187060,8.644309,-3.632008,0.480390,-7.932538,-6.305494,7.744198,-0.958998,-2.546154,-6.182348,0.600231,5.246886,2.818389,-6.414363,-0.738815,-2.648278,-3.581043,-4.373899,-7.351711,-4.156172,0.492333,7.137993,-8.735058,1.745691,-1.891474,-3.095609,-8.277671,6.351065,-6.938606,-2.167522,7.970414,1.532914,-5.022719,-6.460395,7.156090,-1.888640,4.635343,-2.137373,8.196789,-8.972967,8.588453,-0.079134,-5.737616,4.506889,2.126256,7.520318,-0.714741,-5.984670,4.945936,-5.856083,-4.299460,9.036623,-3.373644,7.202516,4.722196,7.809744,-3.259960,-4.271411,-1.214822,-0.839935,1.935773,-6.869159,-0.645653,9.808105,6.808387,-6.258266,-9.316847,9.789451,4.441908,-5.350348,3.366464,9.646961,6.038201,-1.166775,-2.730043,2.526825,2.910757,4.369448,5.857035,3.219049,-9.311135,-5.298853,2.911491,-4.850315,-7.188710,1.706260,-6.333707,-6.581715,6.420989,2.206413,0.050956,3.410212,-1.079248,-4.756928,8.726852,-0.499840,1.092088,-0.821548,9.580906,-7.482714,-3.228054,6.834236,-7.073751,-2.747609,-4.951305,5.727758,6.477839,-5.304605,-5.985313,7.177762,-0.030755,5.420852,-8.221772,-0.002998,-2.307212,4.135690,7.696138,-1.163897,-6.306024,6.232335,-2.740635,-0.921100,9.170976,-4.071627,0.191499,-5.521722,8.783508,-3.096503,5.543087,4.955890,3.376393,-5.466379,9.283581,-3.350045,-0.638651,7.426253,1.376643,-9.657620,-8.760211,-2.377399,-8.255582,-3.925794,-5.009884,6.045478,6.616994,-4.414334,0.830425,0.637855,3.901361,1.266865,8.285847,-0.831335,-9.381347,-0.361358,4.616544,4.781426,2.570475,-0.336762,-5.531384,6.688750,-6.708058,-1.540450,7.479164,0.350137,0.722521,-2.269097,8.998825,9.198222,7.673424,-7.647406,-1.017063,-6.844391,6.027483,-2.833545,-8.404978,-4.370614,6.548533,-9.194700,-1.330604,2.537738,-0.779347,7.790035,-4.621332,-3.095257,-2.616576,2.057712,-0.214805,-2.727110,-8.006102,7.199815,-6.699075,5.094685,-5.955790,-2.328343,9.608689,-8.592471,5.518155,0.974926,2.363297,9.133235,8.528450,-6.102235,-3.500321,3.790932,9.684450,7.479255,-4.501006,4.419416,5.693770,-6.751740,5.999584,-8.825395,-9.700329,2.134923,4.965451,1.477324,2.558831,-7.536412,-2.850130,-8.714094,-9.562160,5.783324,-1.658045,3.251934,8.846139,7.219510,8.167885,8.630491,7.199321,5.763498,-7.948779,6.417597,-9.786706,0.636029,-1.324116,8.808128,-2.950348,4.827496,9.279049,-9.664304,-1.724436,-4.191845,1.982543,2.814118,-6.074927,-4.664692,0.393614,-1.983350,3.079652,-1.942269,6.288885,0.237935,9.169283,-5.307171,5.585220,3.001602,-9.477242,3.234579,7.983900,6.081004,9.414036,-6.726611,1.473866,7.874206,2.618692,-9.833417,2.075866,-8.815997,8.455503,3.471837,1.365426,-2.234592,-6.142625,8.148286,9.938823,9.592320,-7.473256,4.619002,-6.271032,4.347071,9.039788,-0.138092,9.865143,2.574332,-6.705587,3.765890,7.084318,6.281316,-6.296973,0.185371,1.113088,-0.865682,0.103269,-3.848946,-4.524971,7.697809,1.418155,-3.344559,-5.466745,3.665034,6.101541,-3.041299,2.408585,-3.167894,-5.728036,4.275869,2.809297,-5.413359,6.269577,-6.263223,-9.066493,8.853407,-1.729268,-9.503158,0.809083,8.823018,-2.875970,1.638516,4.308222,7.617269,-6.051726,-4.356409,2.784476,-4.738634,6.947821,-4.636000,-0.709063,0.783408,-3.032797,7.723761,-9.833384,-1.831651,-3.601074,-6.076743,1.427463,2.298844,-4.379793,5.123177,-4.330692,-4.939223,5.964293,0.397802,8.330092,-9.349776,-7.035198,1.346539,-4.421950,-7.017305,-0.084124,-2.221472,-9.134846,4.662706,2.153497,-6.180178,-6.519096,5.793448,-0.555712,7.224171,-7.875993,7.053363,2.661424,8.066344,-7.464628,-1.895809,-9.495168,-7.623661,-4.190578,8.644831,4.445221,-3.665360,-0.318606,2.076303,-4.088389,-4.490385,-5.458557,-7.690330,9.772503,5.643499,0.415202,-7.033372,-8.112484,-8.196414,-9.068743,7.930441,-7.108910,7.140608,0.751602,9.412153,0.873708,-1.216496,3.097706,6.574514,-9.534141,-5.946060,-4.809666,9.717015,1.841327,0.058979,9.092872,7.797534,-6.897997,7.393976,0.614359,-6.895773,-1.531235,-6.289199,6.081295,-0.857205,-2.882476,6.655153,8.394820,-4.098546,-0.806224,-1.153618,-5.246431,5.802651,-8.697213,-2.753399,4.892679,-0.447611,-3.080113,2.285716,-7.461659,8.736012,-6.645049,4.148477,-3.537144,7.523557,-7.813596,-6.749808,9.961306,2.113026,-2.568207,-7.960804,-0.326004,-6.737156,5.719287,-2.516451,5.617669,4.336682,-6.482600,-4.686698,-3.205930,-4.443591,3.094531,2.919560,-8.270784,6.866679,-9.391330,9.522560,-8.241976,2.597589,6.249610,-2.339801,-5.540384,1.728084,-8.094022,8.330212,6.403047,7.963977,-0.044114,7.035115,-7.664508,-2.851058,-9.039061,8.081529,8.511829,3.272249,5.410660,2.156719,1.422284,-6.432088,-4.137779,-2.178886,5.875517,7.128592,-4.440011,4.716138,5.384448,1.521086,7.085776,-3.582239,-4.270431,8.663892,5.380354,2.415616,8.631497,5.055809,1.617556,6.502580,5.135418,-6.394021,-2.585053,-4.455362,8.284577,9.167437,8.720855,3.917488,2.883266,7.857520,-3.314793,9.434926,-9.492167,1.574720,-8.038983,5.206751,9.776490,1.443440,2.631994,8.373684,-4.059659,5.477568,8.101274,6.840208,0.449594,8.607134,6.258990,-4.801723,9.675881,9.723691,-3.796294,-3.813009,-9.877518,3.679984,6.451593,5.370014,-2.122163,1.805354,0.774437,-6.861575,2.728686,-4.588624,3.513987,6.811375,7.870921,-2.093472,6.705003,6.715797,7.998476,9.769573,-2.499845,-2.117355,7.368822,-0.429469,-4.228956,0.648773,-2.843488,-8.685455,-5.713111,4.667945,-3.111267,-6.278373,-7.945351,8.725062,-6.868532,-1.007331,2.390946,6.573023,3.625973,-1.408859,4.499443,7.043534,8.504441,6.719235,3.699324,9.298046,-1.463681,1.789528,-6.768040,-7.824399,5.795495,5.658971,3.945105,2.355360,-9.273210,-9.706992,-9.916261,0.536481,2.734157,9.088881,3.434203,-1.922730,-7.437399,-8.238035,0.949045,-6.408196,-8.764818,5.502346,-0.557457,-5.176199,-8.980699,-8.907155,-7.897060,5.211164,-8.431527,2.488105,5.446625,-6.920174,3.781502,-0.035319,5.421811,-4.296410,-9.982110,-2.714647,-9.272054,0.794333,3.170702,7.499134,-6.311494,-3.723270,-8.999244,-2.183554,3.349566,5.171582,-9.570012,7.191645,-1.763432,0.658037,-6.937667,-3.448588,-0.788973,3.813132,2.625727,0.127135,5.288757,6.989924,2.599077,-0.576102,-8.046166,-1.283869,3.515753,-9.896232,3.850331,4.373640,9.051721,-4.116913,3.369259,-2.600724,0.181618,-4.476531,2.627878,-9.004593,-4.858193,1.822855,-3.374469,7.935750,-8.788714,-1.663296,6.093010,1.135758,7.468310,-9.878061,5.757908,1.397594,-1.906858,-0.739887,2.600359,3.545863,1.230496,-9.356183,-2.450622,6.183818,-7.613854,-6.294750,0.256608,-4.402183,8.121663,-5.614254,2.311663,1.583448,9.727094,8.663241,-5.055420,-6.781775,-8.917515,-2.579133,-2.183838,6.417600,2.042077,-2.605048,2.005055,8.723195,5.716692,3.981218,8.974348,8.780399,-6.064795,-1.663762,9.070171,-7.606136,0.924696,-2.284428,7.290507,-9.727835,8.713964,1.466011,-0.827598,1.501621,-6.037003,-6.698173,-1.437142,9.614739,5.973406,6.074240,-1.158277,-8.751106,-6.112632,-8.364206,-8.279678,-1.006226,8.079806,-6.245466,-7.327062,-1.907356,-2.401715,5.530392,-1.313494,-9.231592,-1.428222,-6.375215,0.171514,-5.509257,4.735926,0.859195,-8.229384,0.494904,-9.533868,8.419823,9.105912,5.305829,-8.430639,-3.195076,9.582930,-9.470801,3.832031,9.254466,7.931182,-3.216378,-8.927486,-9.022417,-2.175724,-8.190992,2.567307,0.746532,3.770889,9.498938,0.301330,-5.689544,-8.388891,-4.672842,8.066418,-8.019809,-6.582721,2.759204,7.895649,1.135386,6.531697,-6.990978,2.597655,-0.005536,-7.602424,-6.106462,3.994799,9.959524,-5.352195,0.583000,6.735114,-5.489742,3.670726,-5.440955,-3.753326,-3.427647,5.919223,-4.262026,-7.540782,-9.394134,-4.841515,8.919621,8.212476,0.943145,-6.965563,-3.280082,4.691025,3.861242,-2.277670,2.761047,3.494554,4.532662,-8.007217,9.580422,-9.568081,4.835673,2.754883,-2.950929,9.886687,-2.776265,4.375473,6.553060,8.687248,4.467192,-8.153634,-4.349604,-3.186626,9.363641,-8.276659,0.152665,-7.879110,0.299628,4.226367,-3.731878,-9.830343,0.490992,2.823422,-3.410105,4.367316,4.532327,-7.980064,-2.613627,4.274001,6.956607,-3.089905,-2.867823,4.173747,-0.329786,3.510267,-7.441717,0.390353,3.747511,-2.435935,-2.682530,7.893356,-3.816628,9.887431,-5.012682,-4.838459,-2.500010,4.664743,1.970159,3.363373,1.014840,-2.729859,-5.294648,7.130989,2.150346,8.842250,-6.564080,9.304861,-0.941492,2.615464,7.275213,-5.437117,-2.212142,-2.784121,-8.595368,-5.832222,-8.909153,3.232374,-6.352597,2.368580,1.274469,0.136570,0.615481,-9.856643,-2.016596,7.261970,0.366777,6.496966,4.305744,9.042278,6.937001,2.370570,-6.628432,-2.401055,-2.164668,-8.599074,-5.144554,5.109549,-3.043619,6.555371,5.652940,-2.389314,-5.142969,-2.639094,4.078247,-3.645970,7.289849,8.701630,-1.673007,7.324408,2.281001,-7.398241,0.275948,5.899590,5.159169,-4.630891,7.921383,4.837660,3.444394,9.951479,8.337531,1.087521,-4.898317,1.318918,1.726184,0.873142,-6.281700,-9.845142,7.096536,-1.120949,0.947489,1.075514,6.166162,-2.112037,-2.132706,-3.836555,8.820025,7.805665,-5.004375,4.283968,9.032290,-1.868133,-5.583112,0.162398,-9.178512,0.029111,9.580855,7.452769,5.715980,5.329728,7.430210,-6.324769,2.836567,-9.154206,-1.601262,7.268143,-2.984656,5.038677,1.953952,-5.164328,-0.913194,4.335666,-7.862578,9.251449,-7.890377,-4.013628,-9.268607,8.055840,-9.393076,6.944078,5.707367,-7.807369,-4.350809,-3.802325,-0.350580,4.129243,-2.333425,-3.795961,8.772752,1.886631,-7.664984,-3.580992,-3.775880,3.700518,2.144931,7.000265,5.437221,7.178624,2.946032,6.224041,-2.244393,4.479900,5.391458,-4.468130,5.669830,3.533443,9.199746,-0.561185,4.526768,-2.957096,-6.194427,0.337363,3.033751,7.282764,-0.112926,-9.241196,2.641433,-5.613537,-4.948597,-0.584857,-2.514312,3.934552,2.851112,1.558755,6.957025,0.356272,0.763777,-2.158538,5.482197,4.709612,-4.585792,9.607219,3.841849,1.085865,-0.627536,2.405402,2.670989,-4.416054,-2.103711,3.940665,4.696449,4.545112,6.602681,3.811829,2.181794,-3.434511,-9.920694,-5.199574,8.314073,0.815640,3.211012,-2.548664,-0.518738,8.159851,-9.082401,-1.742901,3.809450,-6.788126,6.247340,-7.449866,4.331566,7.460873,-6.843841,9.071592,5.006694,3.313745,-4.101245,8.777726,-5.631660,4.295937,9.345384,-0.281320,-1.386666,6.055938,-2.156606,-2.567115,-5.072483,5.040255,9.952455,8.493256,-5.799398,8.371632,-9.086258,3.789158,1.277868,-6.699901,-5.335370,-6.512535,1.005411,0.486128,1.738694,3.945474,1.840603,-1.650177,-2.912566,9.265004,-1.377433,6.056367,5.083534,5.724940,3.861400,1.262327,-4.933672,-4.237768,9.235423,8.509782,-2.042879,-6.425042,4.464517,-6.696616,-8.358605,-0.543025,5.151132,-4.986383,-1.342558,4.253150,0.014681,-5.469462,-2.589970,7.899856,-7.940385,-3.166623,-0.829150,-8.932161,7.370908,8.037917,-8.550742,-0.770036,6.054515,-1.880091,-3.804284,1.823819,-3.062187,6.366029,9.242648,-2.520353,0.238644,-8.725159,8.629464,-2.497778,1.840552,1.572259,6.518007,8.413634,-0.572420,5.237478,-3.749103,-1.902265,-5.282269,0.906659,-9.655329,5.375228,7.149027,8.894057,-7.925222,0.702296,4.699493,1.073397,4.191385,7.243086,-9.350959,-6.403938,-3.363950,6.316267,8.657935,-2.083848,-0.046362,8.395749,2.693589,-3.087214,-6.591731,1.494883,-9.484090,4.710601,-5.795061,4.163998,0.193005,1.666879,-8.044553,-0.194825,5.414729,-5.268172,-4.007634,9.226715,-2.190906,0.281815,-4.122108,2.368379,7.644709,-1.743992,9.743570,-1.983151,7.537017,-8.682110,-0.253173,2.562503,5.743464,2.417103,-4.878784,9.907371,-1.097468,4.585113,-0.990982,-0.204839,5.535435,8.304753,-2.554192,1.871530,5.477437,-2.953645,-3.964037,6.696184,6.654190],[1.432330,-1.226229,-8.452220,0.773476,2.986689,-1.530432,0.088722,-7.581906,5.028378,-7.020307,-5.060289,-9.458433,6.224735,5.750562,8.851040,7.720754,-1.625530,2.693370,6.427177,-0.358972,-4.565966,-7.282093,5.734461,-0.967608,6.797905,3.215819,-6.499607,-0.471493,7.386286,8.629241,-4.539142,3.694348,-6.261165,-6.327165,-2.920735,-1.163618,9.382639,-2.880056,9.774306,1.251857,-7.907606,-1.142144,8.450444,-2.935312,-1.479108,8.812652,2.101833,2.541160,3.950668,2.839797,7.896730,3.682702,-3.298564,2.843069,-1.596601,-9.078070,4.112834,-3.180284,-8.555455,3.785940,-0.548110,9.916228,-8.485403,1.796658,-1.855984,3.597072,-9.145857,7.781814,-5.044592,-7.517811,7.264434,3.295052,4.963279,8.337703,5.194254,7.057986,8.104517,2.703446,3.050301,-0.666126,0.507885,0.829972,-6.702560,-6.541428,2.318965,9.518352,6.736928,-6.355607,-8.573695,-6.573387,-8.598203,9.911046,6.878155,9.231212,8.224141,-0.863046,4.102599,-2.089655,-2.888832,4.295193,6.546009,0.991931,9.843621,-7.095416,0.098125,1.933350,-2.408604,-3.407632,1.972192,-5.031441,2.446136,9.619070,0.165961,-1.889230,-3.383933,4.630924,-5.760377,0.914755,-0.165136,-8.674239,-4.427207,-1.881849,-8.216661,-1.147873,-8.896967,1.594628,-1.724423,1.291040,-5.319261,8.092976,3.543199,9.333134,1.325681,1.457724,-4.672257,-3.947583,-4.795080,5.358269,1.270695,-9.531162,-3.816490,8.321204,1.718341,-1.759200,-2.718075,-4.256576,1.898129,3.897349,-2.201923,-2.200314,-2.686897,-8.500556,9.750953,-1.503395,2.954754,0.642577,-6.278930,-3.569876,3.021778,0.054178,2.481702,7.340006,9.797376,1.395465,3.348590,-7.694417,-3.719058,-2.002270,-9.920217,-5.462657,-5.545765,-3.166844,-3.009131,-1.273710,9.073176,5.075660,5.012162,3.193588,-4.995621,6.168948,3.648090,4.886428,-6.720971,6.970148,-5.594959,-9.160881,2.493257,1.282414,-0.805716,5.260308,-2.518573,-7.085483,4.597123,-5.128125,-6.040445,-9.295726,-5.757082,-5.523505,9.404150,0.505231,6.120402,-6.813765,-9.915671,6.045775,9.245368,2.910417,7.559576,-0.961634,3.350955,-5.550562,-7.440632,6.108004,8.235340,2.539534,-8.337483,-4.697959,-2.836160,-9.271249,4.942386,8.189028,6.538698,-6.726950,-2.112271,4.284054,0.850829,-8.609287,-0.214936,-0.253700,3.740809,0.181252,8.274587,0.610669,-1.624574,-7.812026,4.855734,9.673889,-1.160970,-0.364732,-0.314774,7.796584,9.353430,9.594831,0.301783,2.628988,2.396252,-1.500080,9.009078,-1.680908,-1.507079,3.626065,3.735384,-9.371833,-0.307420,-7.044273,-4.800360,-7.465266,0.571291,-8.359572,-1.513310,3.140975,-4.709631,-6.511325,-6.260189,6.609781,4.206334,-9.352085,9.805553,6.387263,0.595282,-4.037944,0.049216,-9.871345,-6.207868,7.680411,-0.969759,-0.101629,9.062749,-6.950935,-6.039184,-2.049733,-9.913361,-4.320121,7.871193,6.467935,7.511539,-6.730867,8.681155,-0.834499,9.508927,-4.267063,-3.524050,-0.201975,0.633968,1.707703,4.803575,4.794616,1.258465,1.646121,1.406312,6.796401,8.528459,2.938175,-3.608777,-5.446193,-5.143745,-6.755229,-8.182417,-2.549427,8.833628,6.879034,3.048807,1.106388,-2.762674,6.761566,5.419486,-4.319033,-7.799729,2.258827,7.468852,1.892916,-9.248810,8.337377,-4.307832,-4.301279,0.387833,-1.764424,4.786334,0.325398,8.745206,4.526617,-8.148638,2.144814,-8.273706,3.672699,-1.850048,3.425613,-6.393385,4.521767,-7.774715,9.439673,9.596672,-6.192254,8.696701,-4.383443,-4.361777,3.848711,-8.799086,7.701312,-5.880561,-1.515490,3.605890,2.284004,-2.798256,9.284297,2.874034,3.336215,-2.908006,5.410730,7.231205,-2.951108,4.516359,-9.375014,-3.721356,-8.003803,1.988585,-0.010271,-2.370659,-4.350279,-3.556326,8.681849,-4.396173,8.342561,-3.697743,-0.223598,-2.315166,3.577154,4.422233,8.660227,-5.260754,-6.506196,1.171316,-8.414992,-8.725780,-1.369695,-4.387145,-5.925766,-0.281810,-6.261496,-2.090178,9.746156,3.146317,1.564143,-7.643635,1.714333,-7.089834,-1.338491,-3.292353,-5.568326,-0.270705,7.313546,-1.829085,8.407932,6.562480,-4.817753,7.097833,8.280715,-7.397675,7.711656,7.777038,0.565947,-6.403234,1.506201,6.051278,2.159480,3.790746,-6.915880,5.759920,-2.390651,0.680543,-6.958250,-6.228570,-5.102743,-2.462340,-0.219319,-2.012097,-1.854884,7.119888,1.545359,5.177653,-9.105295,3.397701,-1.278162,7.977051,-7.269946,9.492760,6.507701,-0.428923,0.465426,9.792218,-5.805157,2.425926,-0.380678,0.377169,3.982090,-9.677450,5.501326,6.430822,-4.358342,-8.648846,1.141520,-6.503128,-2.973017,-2.179478,9.924683,4.374442,0.517071,-8.735519,8.172065,8.703028,-5.716402,2.244745,-1.605074,-0.857113,5.419420,4.285399,-1.253604,5.834454,-8.688054,-4.862944,7.747506,2.112295,6.091327,-8.323693,4.772092,8.791354,1.029903,3.061362,0.234314,8.322052,0.385370,-0.118498,-1.328049,-1.964381,8.696480,-8.226472,-2.411940,-6.896316,-7.014438,-6.303129,-6.547810,9.187672,-1.682973,0.457225,-3.219200,-6.097649,4.458985,-5.427432,-3.058551,-0.831751,5.142282,-9.930285,8.281581,9.163233,6.543453,2.951175,-9.114270,-4.503487,-2.724134,-4.715834,-3.957206,-5.427953,8.144120,9.550446,8.154312,-5.085742,-5.484511,-9.447653,7.340550,2.219849,6.082010,-8.604424,-6.431640,7.926332,4.365304,0.582674,-7.067588,7.607940,-8.803877,-2.952158,0.472999,4.195101,8.156709,5.463136,4.333174,-2.685469,4.303190,-6.201215,8.615958,-4.290345,-0.473476,-3.778954,1.188929,-2.086039,-0.158359,9.756077,0.804199,3.832026,-5.008919,2.813107,-4.900170,8.096398,2.884347,0.618063,2.433464,7.076075,2.192644,-1.035468,3.360694,6.473218,1.470175,2.765017,4.729836,-0.186678,8.558254,3.516841,2.990268,-6.566041,2.490064,2.379938,3.115928,-0.781597,-7.749613,-7.978204,3.963558,4.445240,-2.620503,-5.808034,8.494959,-9.756792,-8.614786,-3.749888,-8.298880,-9.823609,-1.787585,-3.767093,-3.645956,8.524467,0.834723,9.193863,4.407021,-6.428128,2.337031,9.764863,3.213389,-3.898912,8.405396,3.164144,8.173761,6.571291,5.934710,5.373599,-8.363572,-7.135499,-3.260406,5.321961,-9.001175,-8.822309,-2.382625,-4.498131,1.823341,3.673081,-5.937031,-9.206871,7.489362,1.569212,7.441236,-6.377452,3.602851,0.273940,-0.046674,7.026765,-8.956667,8.776012,4.401929,-6.126685,-6.972313,-8.957854,-6.856808,-4.697392,-4.560617,-0.921746,-2.166526,-7.757743,4.773979,-9.638247,-4.765560,-6.382290,8.817000,3.211771,-8.384875,4.232747,7.308386,8.750360,-9.518406,2.310978,8.986356,-2.166326,3.218473,-6.917917,-9.976704,-5.930770,-5.051884,-7.663894,-8.731530,7.513706,6.746395,8.504696,-6.941623,4.908385,-2.709707,1.854276,-1.209997,-5.063976,-1.347933,2.355014,7.788031,9.151625,-1.125326,0.978852,6.434193,8.563104,1.462097,-8.592128,6.784438,-1.476766,-0.422051,-4.845275,2.033334,-2.403530,8.746454,-7.956241,-6.419893,-1.325147,5.283509,0.249089,-4.069750,-2.646804,-7.032754,3.578054,-2.572400,4.581501,-1.455647,1.928457,-0.557129,6.619429,3.551077,-5.127224,-9.974342,4.207787,-2.221875,-7.600970,9.892663,-8.083817,7.566136,-9.729970,9.069308,2.515632,2.213217,9.258368,-4.652132,5.656762,9.149780,8.011972,-0.640171,4.188459,-3.918247,-5.127214,-7.815143,2.719649,-2.116669,8.605550,4.181149,2.183582,-4.937213,4.483074,-7.712555,-5.171214,-3.935005,9.636390,-2.538171,-9.536308,-1.899036,2.394829,1.767704,2.692024,-6.018289,-0.851828,6.217270,-3.182909,-7.764989,-6.165806,-0.390782,-8.804893,8.025580,8.603203,8.456300,-8.094395,-7.428164,-6.087353,-9.531829,-6.217073,6.406066,-6.027458,-3.898409,-5.105432,-1.000515,4.470003,8.111738,-1.259301,2.293384,1.363865,2.146641,3.791845,6.615600,8.730652,4.596598,-7.589058,-1.140040,0.753659,4.075149,-5.835697,-7.607692,-8.641774,8.285061,-4.622030,-8.925338,6.958425,6.792980,-3.136373,4.820970,-6.008084,3.531608,2.427288,-9.914423,-9.588663,-2.198889,7.062262,3.162263,-0.634882,-3.771612,2.277831,-0.778678,-4.579715,0.749015,-2.288482,1.376669,4.901191,1.814858,-6.610290,0.899350,3.694064,1.931764,2.762212,-7.412362,-4.752094,-1.257108,-1.590937,-0.456361,9.984257,4.641756,-3.036736,-8.606995,7.023887,-3.309486,3.232215,-5.214566,8.454602,-2.089562,-3.840555,0.500445,8.779430,8.800279,-2.003408,7.181570,8.322239,-2.590421,6.242954,-5.363731,-3.888657,-5.036971,-3.666173,5.112112,3.013336,-1.412380,-3.182770,-8.619838,-7.025457,4.340123,6.300599,-7.755115,3.079951,4.904021,9.276376,9.537040,-9.988694,-9.311874,4.916417,3.520790,9.781518,-8.146259,5.035647,6.355865,-9.796213,-7.909747,8.117405,1.367913,4.425364,2.850380,-1.536847,6.762841,4.631312,5.668549,9.671534,4.322607,9.477322,-6.882000,-3.149164,-3.422873,1.002814,-3.957087,4.543830,4.466399,-7.922808,8.150352,-3.509065,-1.307230,-0.054110,-1.412492,-7.309782,-1.669340,0.531411,-6.676301,8.600697,9.268052,6.134380,9.506650,0.838237,-0.255192,-2.587512,-9.207567,-3.266517,-0.509284,-7.816609,-0.897428,-4.621373,-9.774158,4.229129,0.511746,6.323192,7.656238,-2.432617,9.121416,-6.035929,-5.517448,-7.307024,8.347779,3.859917,6.046754,-0.687176,-7.552239,7.417181,-2.189823,2.935265,5.901025,-7.489433,0.881289,7.827611,-0.699267,-0.293531,-6.694647,4.949873,0.554981,9.008320,4.891231,-8.577193,-8.860213,-4.151228,9.757010,-6.191701,8.312184,8.824752,-9.722019,4.301657,-2.191257,7.481458,-1.990623,-8.184650,5.168778,3.238464,0.541092,-0.017267,5.737580,2.889215,-2.530170,4.221167,-0.495149,-2.832964,1.103614,-1.172161,-1.588673,5.475311,-3.324951,-0.112581,6.136660,-2.919950,-8.042641,7.446709,-1.140022,-6.406963,-7.926953,-9.361488,-0.079862,1.321162,-7.294163,-9.963767,9.688868,-6.530198,2.631674,6.471531,-3.789622,-1.388819,-2.488664,-0.535635,-3.645293,5.572455,-6.991523,0.884594,6.517042,-5.290176,-2.666131,-1.107890,-8.264395,-7.737451,9.441623,2.479640,9.312842,-9.848157,3.119760,-4.452829,7.393081,-0.364906,4.840224,2.844303,1.899574,2.200750,-0.984945,2.955295,-8.547333,-2.117718,-4.742529,5.517250,3.683459,9.757191,-3.093236,-8.811499,-6.482176,1.068305,2.770749,-6.633830,-6.821922,-3.448036,3.919425,-1.754202,8.373723,4.168924,-1.100928,-4.249445,7.262870,-6.015727,1.784126,1.303697,4.029422,-3.460390,5.909064,1.111397,-9.971107,-8.193305,-3.117568,0.844643,-6.832830,1.329276,4.790748,-5.703218,5.340626,-8.831517,-8.575599,-7.537519,-4.712934,-5.951111,7.817595,2.676438,6.966288,0.324581,-0.199954,-5.970158,-6.548719,0.362561,6.026999,-9.636587,-8.037979,7.680796,-0.825610,0.893647,-3.796805,5.583581,9.414302,8.585257,-1.997055,-3.641034,5.455661,8.190217,-1.850870,1.126177,1.755347,7.358817,-6.029548,-4.255290,-0.210038,6.259828,6.660928,4.336821,-9.568525,2.897233,6.696997,9.958142,-0.504173,-2.732639,-5.552329,-6.861620,0.822019,9.618380,0.277955,1.791277,4.249545,-4.259413,5.848328,-2.547669,9.095011,-4.776656,0.703469,3.360001,6.915365,0.870201,-0.679944,4.529806,1.157542,6.754406,-1.936699,-7.357487,-3.261218,-3.298660,-0.950846,8.708969,-7.834430,4.726248,5.256023,-0.714819,-6.720887,-7.280920,1.158774,9.083794,1.037224,6.708453,6.697135,7.070648,5.330299,8.034200,-6.835715,9.661561,-8.160216,2.830313,2.830581,-2.705395,9.338740,-7.146914,-2.006295,1.919786,8.375900,8.478001,-6.932913,-2.174940,-6.386211,-5.508322,-1.933724,-9.213866,-0.362814,-5.506270,6.854980,3.219872,-0.770013,7.145641,6.558015,-6.758895,-3.894276,1.395206,-1.687560,-2.144683,9.512883,-1.706244,-5.501268,0.857264,-3.434893,-2.684679,-7.157742,-5.529069,-5.075717,-3.714792,-0.403733,-2.170455,-7.838183,3.921360,8.728906,-6.997086,-2.358569,-2.714090,6.280221,5.746386,6.450837,3.828085,-8.149603,-4.974534,2.235044,-9.816179,8.329755,-4.243598,1.164070,0.357678,4.588044,7.604652,-9.441532,-4.566155,2.592305,4.788900,-5.201636,0.433326,-9.058595,3.969394,-2.590149,1.050379,-2.343165,3.472582,3.625684,-3.114946,-2.948370,6.913999,1.795672,-9.177361,0.283598,9.593299,-3.651065,-5.103038,6.547739,4.383896,-7.142866,8.013883,-0.800609,-2.158580,5.456934,4.500707,-0.054379,-1.961329,-3.508427,8.697765,-9.735338,1.576054,9.488599,6.597272,8.880738,-2.894086,1.658875,-5.239134,-3.276899,-1.967765,7.855769,-6.925662,-1.353223,6.314436,3.723943,-2.800465,-6.524936,8.274415,-3.340689,-6.207468,1.256109,4.733137,-0.268187,-3.355960,-2.786931,9.652725,-7.972998,3.552270,-9.707770,-8.023276,2.836824,-4.531863,-4.511311,5.338992,-4.730489,2.725975,-2.778142,8.200464,-5.813256,-9.476460,-8.306893,8.260272,5.184178,3.678443,5.279265,7.227120,-3.442726,-9.888050,6.095133,7.992208,0.782864,1.652035,7.279807,6.544024,7.544069,-0.662557,9.261988,-6.553833,5.725731,-0.118366,3.241488,6.160295,7.166978,5.090393,-3.867318,4.426160,1.400084,6.818861,1.698780,-7.381015,-6.783106,-7.648339,-5.745836,-3.494003,-8.376143,3.029442,8.106105,8.457462,-5.073793,4.663720,-0.941888,2.067040,-6.957993,-2.032187,0.474015,-8.451116,-4.250445,2.236783,3.619243,-5.957722,-8.521215,-0.651365,-5.751955,2.617135,-5.806967,5.341512,3.443033,-1.357319,-1.362597,5.477451,0.177779,6.057951,-7.027565,3.005557,7.585039,6.651845,9.661553,0.426452,2.087499,-2.773711,9.353939,-1.450651,-8.215500,-2.662933,-3.903279,-9.584302,9.130595,5.131935,-9.483933,-3.671210,-6.339842,-1.220379,7.333355,8.907644,-2.808716,-2.608485,-3.492462,-0.368959,8.363707,3.507441,-3.919900,0.694637,1.964283,9.089128,4.110182,0.462882,0.973030,0.906091,9.229274,4.420311,0.261628,-8.327710,1.731327,-9.845742,6.504301,-3.306867,-8.881752,-8.009001,-4.037870,3.879717,8.376709,6.664630,-7.775227,4.736057,6.029411,4.840981,-5.777335,-0.892121,-7.548463,-3.505034,-5.674432,0.628710,-2.634059,0.086871,9.817724,2.086420,6.989560,6.129162,8.589697,-3.188813,-5.702912,1.326188,5.010717,-6.527414,3.522934,5.137879,1.656911,-6.886940,-1.869025,-0.362179,-9.319943,-2.834228,-0.895582,-1.235851,-1.744800,-4.260726,-5.829311,6.571345,-0.406469,-9.432476,-3.450848,7.255571,-6.392987,-3.287523,8.800890,2.133026,-1.810552,-6.669894,7.301642,-1.872436,2.365092,-5.470467,1.336851,6.581533,3.541834,0.248535,0.523722,6.989215,-1.805456,6.826938,-6.216081,3.846363,-1.583818,9.975960,-8.831155,-4.743260,1.564065,-3.274013,-6.956478,-6.800390,1.925174,-6.200789,-2.302530,-5.852446,7.458534,8.402313,-8.982607,-5.911756,-3.962699,2.418976,5.869171,-4.191655,-7.920134,5.995315,-0.766940,7.417825,1.380025,-3.834194,6.345288,-4.825327,-3.792083,2.474159,2.707978,-0.546246,0.023410,-2.950424,0.748148,2.146619,8.421744,-8.061363,-5.042431,0.785502,7.034036,-3.931976,4.549102,2.191587,-8.384718,-8.765865,-4.448143,6.228915,-2.728465,0.539245,-7.798110,-0.710557,9.615461,2.686375,-9.591566,-5.376754,-1.668309,-4.530079,8.585396,-2.510140,-2.323986,4.092196,1.219006,0.020177,3.000958,9.613962,8.981646,8.525652,-4.117105,8.778042,-6.372390,3.524298,-1.520218,-4.405204,6.590291,5.412306,1.365572,4.807577,2.026743,1.580311,5.725393,-3.135222,-4.966248,6.739263,-7.658806,7.675688,-4.020345,0.955255,-8.953899,0.448682,-4.194994,-6.372169,4.389034,-8.783503,-1.450334,3.392862],[-6.552979,-2.026458,-8.565706,-3.614377,-7.843709,6.222566,-6.106666,6.187426,-0.874512,-7.397260,7.277717,-0.216010,-0.475070,6.741518,-3.891316,-5.965515,-9.929180,4.526394,4.690311,9.917130,0.831895,-8.112489,-4.527089,6.605943,-2.110154,6.844350,-1.631692,9.444197,2.339470,3.055900,1.883531,-0.111334,-4.412511,-2.432730,3.378286,-9.486694,-3.398234,-4.738877,-7.102335,9.378959,-8.570852,1.409252,9.394334,8.190699,5.134219,-6.033206,7.313714,4.807687,8.340785,7.717442,6.303148,5.239971,-6.952270,-2.665946,9.250868,-4.812256,1.682068,-7.068418,-4.022927,8.281294,-8.537073,-0.324228,-1.715696,-7.361570,-6.057670,8.541146,9.352347,1.598753,-6.051240,-3.565556,-6.295870,3.479269,-3.685373,-6.848022,-4.952488,7.352579,7.061162,-0.815312,1.787668,6.255654,-7.328152,4.474625,-7.192347,2.213433,1.937681,-2.618970,-9.352230,9.871566,-6.091678,6.004394,2.259336,7.058299,2.590441,-4.526074,-7.786207,-5.607865,-5.424559,-7.431446,-9.330234,-3.682029,-9.972980,1.563816,-3.669553,5.285391,-9.471498,1.028814,7.239855,0.627636,-9.222106,3.603203,2.990447,4.021575,-8.945028,-9.475459,-1.007050,-2.250151,-3.895108,1.575742,-1.550914,5.073357,-3.608508,-0.660330,7.643525,-1.171360,0.940732,5.441105,4.537988,8.369078,-3.941878,-0.432872,-1.896467,4.037548,7.254644,3.503047,-1.805006,-3.565080,-0.463121,-0.572773,-4.535990,5.857628,7.920970,9.706600,-8.644124,-5.764858,-0.757235,6.650629,3.445391,6.623443,7.802089,-8.690354,6.541144,-6.541445,6.327095,-4.027870,5.924662,0.153376,-4.669546,7.436032,1.960019,2.466383,7.143772,-3.387003,-0.406196,1.037350,9.724053,2.545373,-0.485229,-2.465316,-2.531840,-9.901632,-6.764887,-5.119560,-6.765697,0.498641,6.477504,8.652372,4.361978,4.556335,-1.683435,-6.779701,-5.118916,-1.309057,0.641841,-4.942989,1.248848,-5.643321,4.204712,-6.564027,-9.007054,7.993476,8.296574,-0.949331,6.671517,-8.360397,-2.308366,9.448445,-3.010758,-3.484994,-0.196975,7.454060,0.093800,8.641621,7.280705,-9.887817,-1.608600,7.927311,-7.961600,-7.029430,-1.562617,4.148421,2.562948,6.305465,6.719720,-5.695909,2.373169,8.484212,4.615163,4.348334,2.106857,-5.642474,8.109957,9.888894,-7.118453,1.219695,-6.620308,5.413686,7.340981,4.174558,-7.090856,-5.778689,2.316318,-4.435235,6.866022,4.143467,0.874927,-0.898044,-7.335010,6.178002,1.481203,5.019917,7.515528,-1.174220,6.015166,2.108898,5.237688,4.674901,-6.283127,2.230754,7.273634,-6.448690,-2.180688,-1.936590,-5.425300,2.618686,-9.107979,5.364150,-4.861815,3.986724,7.362101,1.017580,-3.088510,4.061315,0.701054,-3.199385,-9.475108,0.290563,5.548313,1.773387,5.610558,-6.200921,8.880935,-8.940755,9.799230,2.405487,-7.434055,0.028119,-0.759237,9.820458,4.393113,-8.912730,-5.708603,-8.761405,8.999816,9.591324,7.820995,2.093813,9.307808,-1.736896,6.750737,3.534771,-5.617541,-6.754170,-4.963565,-4.088836,-6.715594,7.743992,9.884440,-5.054761,9.540336,5.832777,7.107544,3.436978,-2.673819,4.311101,6.911157,-7.979058,6.273222,-4.003588,-7.494534,6.481626,-9.593410,-3.513569,1.416389,-0.674448,-5.422994,8.860582,-4.713521,0.099237,-2.228072,-6.072018,4.430325,8.320240,-3.528476,-0.002207,8.525701,5.205736,-8.814356,2.931230,-9.439130,-8.846035,8.302529,5.495518,-4.585184,0.368454,5.429111,7.352901,-1.510235,-8.921874,-2.496237,8.680114,-3.178469,4.488940,-5.149530,-8.888849,6.352322,-2.843570,-0.714277,-5.959279,-5.998739,2.741506,-6.106572,-6.384822,-6.546818,8.152966,-1.019465,-6.437709,6.113808,6.277587,-8.353291,-6.047969,2.342693,-3.022159,-7.595132,-7.147998,-0.680665,3.841546,-4.173433,0.867216,-7.510060,-7.333348,-4.736960,8.667066,-1.892135,6.550196,5.327582,-2.836321,-5.124917,-3.849038,-8.744455,1.068388,0.396502,8.812724,2.490274,-0.284031,0.306250,-2.523904,5.380759,7.066974,-6.628786,-8.904406,-1.708133,-3.836343,5.230153,-6.141851,-0.325812,1.436287,-8.919327,8.744220,6.214284,9.769204,-2.111414,-4.582532,7.011641,-8.167378,9.348670,5.190354,7.874482,-1.280898,5.059016,-0.125631,7.399295,0.333466,-0.507989,8.603930,-8.164139,-5.236334,-1.299825,-9.010293,-2.683393,4.296486,3.217988,-9.239517,3.333546,3.736530,7.170022,-1.725064,6.534186,-3.355693,-7.998215,-9.176247,-9.696583,-0.330620,4.172988,-1.834169,1.802118,3.745556,5.383597,1.612496,9.957783,8.859132,9.602532,1.883001,5.952802,-8.698859,5.141557,-6.788625,-8.545238,-6.148473,3.931035,4.058729,-1.649812,9.673581,-0.384301,-5.789987,3.022753,-3.754714,9.529528,-1.559377,1.091174,9.428442,6.713874,-3.231713,-8.480276,7.321217,-2.511918,-7.356872,-7.719156,-4.227457,-9.079049,-4.579271,-8.227641,-5.174089,-9.428569,-5.209981,-4.065361,-9.323459,2.673372,8.248966,7.016986,2.485600,0.466569,-1.615626,6.773498,2.893027,-0.740216,2.846390,-2.128514,-3.784302,-6.187929,3.142481,-5.376593,-7.088313,-2.408378,9.021564,9.589792,0.320169,-9.252579,-7.406292,-6.167315,-8.456770,7.299385,5.355507,5.608706,-4.417403,-6.375016,-6.094165,7.454291,-0.042219,-0.653289,6.749520,-5.178064,3.935780,-2.167074,-0.536306,5.117070,7.611064,1.848753,-6.190220,3.036064,-4.454804,-2.090567,-0.668113,-5.023362,-2.374221,3.957062,-3.558864,-3.149937,-5.137550,3.519147,-6.200265,8.684855,4.572308,-7.776348,-2.884794,-4.902833,-7.151392,8.541104,-7.361240,1.769382,3.741580,-1.444376,0.043084,0.108247,9.590982,-3.976198,5.774163,-0.783531,-4.071615,-5.395381,-2.363786,-1.052101,-3.043639,3.930839,5.643935,7.568866,3.802981,-3.437681,-0.560888,9.496733,-1.388442,8.535066,0.849612,-2.813590,1.102984,-7.204468,7.176664,-6.124595,4.850493,-5.300727,-7.214959,5.278076,0.283945,-2.330234,4.392072,4.602205,-1.706194,6.835372,-6.196302,5.796123,-7.610430,9.550252,-9.727318,3.383161,-3.290295,-7.248012,0.338507,-4.397999,7.356387,6.154684,-7.106352,-0.399830,4.016206,5.181321,5.831974,3.571280,-7.449088,1.319538,-3.719559,-8.500349,-0.201780,-8.508401,-6.904993,-7.332760,5.296128,-8.291880,5.422941,-6.251500,-9.592449,-6.336152,9.089845,-0.303860,7.589514,-0.079209,-0.304216,-3.393883,-6.245000,2.431962,6.615441,-4.071998,2.377142,8.816845,-5.176351,4.474147,0.247609,-5.769749,-9.669559,-3.388143,4.052310,0.313513,-9.743485,-6.655148,-4.608834,3.745741,-5.427460,3.439790,1.746758,-9.183422,-3.691145,-8.680071,2.003607,-1.458155,0.523318,7.142691,-9.175104,5.690161,-1.741809,5.803157,7.669617,7.791481,-9.150432,7.849667,7.187617,2.684277,9.134727,8.669112,6.250023,-2.528381,-1.213939,6.048340,6.187953,4.196794,-9.895237,-0.878334,-7.444457,5.710502,-0.971829,-2.983027,-0.941098,-3.991059,1.017173,0.316796,1.702517,-0.358157,7.124634,-1.531245,-9.188206,3.212264,-4.375019,-7.788307,0.226067,-0.819928,-5.195442,6.214261,-6.572444,-9.540127,4.081236,-4.116055,-2.903298,-1.808840,-1.821709,-3.526557,3.078611,-3.513964,1.909216,-3.549410,-6.698092,6.252313,7.565935,-2.183981,-9.629910,9.308925,-0.454401,-8.732028,-6.491259,-5.925689,-7.502784,7.625414,-1.372486,9.417317,-9.062797,-0.545547,-3.437671,4.024684,-6.763081,-9.994076,0.675242,-5.734738,8.732212,-9.870932,-1.742536,5.819964,7.556775,-5.426187,-5.746977,9.477578,6.967222,1.091373,2.910414,2.205823,-2.613215,-0.243616,0.602887,1.095956,-4.168348,8.340030,1.561551,4.889215,8.402804,-7.241482,4.270806,1.445363,-9.336515,0.949156,2.991531,9.852774,-6.829987,0.255138,0.436217,-2.643509,-8.934521,-1.707303,-0.213812,-7.397977,8.690314,7.133616,4.515023,5.382642,-8.324554,9.970171,6.877718,5.413638,4.114573,1.890824,-6.870639,-7.971934,5.181408,-1.139172,-9.901069,-5.945761,2.863420,-2.757122,-5.772056,-4.641388,-5.679795,-3.012958,7.067250,2.330897,9.492665,8.060041,4.075145,-3.014806,-5.940177,-8.183134,-0.086810,-5.412717,9.049844,-7.759193,-3.717215,-0.442229,-9.892249,-6.500867,-5.217432,-9.626524,-9.662218,4.854135,6.810571,7.821291,-0.379416,-1.507590,-2.391241,3.466342,-0.816765,2.722207,-6.956368,6.706808,-0.019379,-7.701927,-7.955621,-0.702702,-2.175581,-3.410023,-4.421170,8.424823,5.487021,2.261153,-4.721904,4.246739,-1.478345,8.290978,-7.888041,8.314542,-3.833869,-8.162911,4.012863,-7.511102,-0.728251,3.880460,-8.629954,-7.802142,4.285619,8.992299,-7.956655,-4.347439,4.270383,0.337138,-5.426972,-4.174036,2.073545,3.642438,-5.488704,-5.943133,-2.315502,4.097891,8.182347,1.865340,7.445923,-9.808120,2.241341,-9.300092,3.869587,1.969426,-6.149819,-0.994592,-9.350412,-1.334327,4.125247,4.514842,5.874756,-0.101498,-8.845934,8.431308,-2.709784,6.362329,-2.514351,-3.950583,-3.052686,6.743061,-2.045422,-6.628254,-9.979901,6.077602,1.234299,2.759171,8.610030,0.136685,1.329121,8.234354,0.741269,-4.133169,-8.301355,6.274417,-2.332471,1.192054,-6.042942,8.923678,5.543894,8.590597,7.946073,1.083784,-9.425051,5.847259,8.322854,-6.140677,9.420298,-5.403130,9.469443,-7.238991,-2.000762,-1.771405,8.150258,3.882915,-3.393824,-9.064041,-7.888789,-7.588458,-4.636918,-1.915624,-0.989638,-0.511386,7.877047,8.992803,-7.249776,-8.369222,-7.332871,-9.796303,-5.220321,-5.722316,-0.992893,5.858541,-3.302032,3.220611,2.163261,-3.086636,-5.290051,3.027170,0.546466,6.277242,6.539032,-9.203727,-0.317265,2.712565,7.229496,-4.269108,-3.451708,-1.959325,0.083233,-6.903440,4.695061,8.826973,7.520487,-8.012995,8.171120,7.464544,7.371600,-3.504226,-0.706996,2.767074,2.697586,2.725246,5.144970,-2.855670,1.759977,0.072828,5.008376,5.386126,3.170647,2.127121,7.040662,7.882005,9.532764,-4.411114,-5.499171,0.406724,9.157089,0.696337,-3.694574,-2.006288,-2.722835,-8.507149,-0.819054,8.396320,4.877398,-9.787834,9.831039,-6.495929,-9.981751,-7.176265,-8.075436,-7.494329,-7.474374,-6.947562,-0.086365,-5.408677,-0.702467,-5.530059,-2.250761,-7.961077,9.563464,-8.164438,5.702933,4.030688,-1.471428,-6.951302,6.577502,-6.245521,-3.786386,-3.507332,2.795333,-8.234085,3.044692,-3.161858,-5.926488,-2.757926,-3.415034,-7.988023,2.411476,6.804429,8.624271,-9.702268,-0.955192,-4.438690,6.717579,7.443612,7.440742,-7.788657,4.858747,0.125301,2.833916,3.037289,-9.543468,8.860810,9.229249,2.750295,-2.360986,9.802594,1.932618,-6.610498,-2.047295,2.144121,3.253503,-2.366151,6.430858,-2.448165,3.716529,-2.511301,0.829135,2.947528,-6.562134,9.322525,-3.453687,4.841461,-4.115937,-0.568899,-5.684929,-8.624171,3.267007,-2.678609,-3.510092,-8.510182,-4.624569,-7.484843,-4.735029,-2.783046,-3.393771,-0.257037,-0.102074,-8.502605,1.010371,8.727769,2.046657,5.506598,-7.172351,4.993267,-4.992675,9.269066,-5.412644,-9.780354,1.370899,1.898678,-9.084224,0.152868,3.382375,9.593943,-3.171140,-7.394208,-1.854659,0.303970,9.046068,-1.587582,-6.778097,-0.156613,9.330185,4.886278,2.596379,-0.171332,-8.858972,-7.958945,-1.712576,-2.822705,-0.683760,-2.825157,-0.738590,-9.399740,-9.984321,4.195734,-0.845320,0.515307,-9.340129,-8.022676,8.173764,9.534882,-7.446989,6.475490,0.766498,-1.750849,2.673824,5.340341,-8.087154,5.754389,-9.925125,6.153486,3.597583,-4.749696,2.399525,7.586178,7.135848,1.993414,2.290000,-7.770574,-8.972051,-9.646484,2.993882,-5.989650,5.012109,-9.653107,-9.470491,-7.388126,-0.291327,-9.728008,-9.259035,-3.114625,-3.216675,9.841054,6.408191,3.885604,-2.219388,0.881097,0.769036,0.400519,7.998437,-9.879472,8.664032,9.153514,1.219010,-3.376074,-2.227231,0.187462,-3.378212,-9.628653,6.236133,0.553916,4.215698,4.542555,-3.668236,-9.423375,5.188829,-6.959636,2.538721,-6.750571,0.966524,-6.714339,-5.080767,-7.644944,8.018642,-4.209862,-6.541295,-4.711233,-9.120711,-2.319696,6.658944,-9.855590,1.061380,6.681484,5.634510,9.166515,-5.257197,-1.251329,-8.694370,0.369827,8.534135,-3.348836,-4.705283,0.798400,-0.507661,1.668155,-1.536731,-3.777086,-7.220027,6.654793,-0.777362,-6.697125,-2.371340,9.258583,-7.976551,-0.971684,-6.502680,6.520085,-0.013710,1.539682,0.607498,-7.246647,-8.219427,2.012412,-3.217277,-0.451756,-8.323130,-6.149538,8.599785,3.679008,-7.317231,3.304023,-6.498768,8.297452,-7.831065,6.315466,-8.947912,1.652125,7.817739,8.367490,6.172829,-5.342856,4.400132,6.399964,-7.690241,-4.401012,-4.353246,8.821431,-2.857775,9.406142,6.985807,-3.938670,-6.553167,-2.830030,7.846792,-9.099417,-8.828171,-1.444815,5.287961,-4.416074,-0.580400,-8.497243,7.278774,7.023784,7.436717,-6.051390,7.326803,-4.185685,-5.830580,4.936871,-0.691577,2.712746,-3.826669,-2.878676,4.204210,3.663832,4.364152,-3.326162,5.030731,0.300911,7.799479,4.385499,-0.767338,-7.469659,4.644163,-7.436799,7.569271,-7.613761,3.168698,7.402352,5.473452,-5.068319,2.534707,4.324271,-3.061892,1.346697,-4.905941,5.787718,-8.403323,-9.059906,0.380705,9.609829,-1.672012,0.346484,9.377224,-3.592071,0.011743,1.101580,8.417946,-1.147713,4.712816,9.581784,-9.842356,6.988352,9.043687,-3.577425,-2.921430,1.359428,9.655909,9.185588,-2.279905,-0.571044,-3.366286,-8.102984,-9.487407,-5.060955,-0.465871,-1.501807,-2.555594,0.861901,0.923618,-4.757298,1.991241,-1.530026,-9.707392,4.564307,2.088625,0.738031,-6.305887,5.654232,-3.423308,-8.008174,-2.172266,6.969107,-6.241414,-6.584012,1.762112,-7.688156,-8.534434,5.607337,-8.296916,7.291443,-9.249443,0.794903,-2.589220,-2.211429,-6.231409,5.229279,8.310062,0.931190,7.699806,3.310416,6.200925,-2.011661,-0.912068,-4.360388,-7.944089,-4.915298,-1.973669,1.584933,-9.647522,3.805733,4.439380,7.604852,-3.418944,-0.744493,-2.679869,-5.158633,3.881976,-5.805526,-1.372461,-9.427210,-5.242698,-0.286554,7.164254,-4.030095,2.140857,-7.566979,-8.573031,0.753148,6.630241,3.464103,0.522231,7.746684,-7.349033,-7.800301,-6.823865,1.407207,6.276974,-2.120679,-0.570028,-6.096100,-3.021633,-7.743069,7.562545,1.493621,2.456609,-7.360697,-2.796850,-9.971495,8.329014,-4.231875,7.781111,1.778777,3.659163,7.429747,-0.965813,6.417170,0.116675,2.221596,9.802882,5.951660,3.294681,2.879486,1.548818,-6.390274,-6.058989,-5.071456,7.793250,-9.488970,9.652961,-5.390134,7.607823,4.590095,7.396706,6.690616,5.885383,3.675477,8.571024,5.280903,-1.702395,5.653070,-8.530225,2.224973,6.769960,-5.576722,3.235211,-0.435518,-5.012213,9.502449,3.594033,-1.941678,3.789175,1.686444,-8.129002,1.279919,4.345211,7.583657,2.535534,6.045962,-5.820165,0.220201,-4.610649,-2.620640,2.634812,-1.237868,0.386697,-1.171826,-8.224593,4.104022,-8.676667,-1.870957,6.916861,5.646638,-8.059881,-2.109904,-8.142132,-7.884456,0.763886,6.345130,4.749456,4.522728,-6.832377,5.008699,-5.092838,0.484692,-3.614336,-1.724339,2.588234,-8.541156,-9.302982,-8.010021,-2.430477,6.935964,1.586178,4.716028,-1.582121,5.642633,-2.560806,4.481695,5.973772,9.141303,-6.057345,-9.944786,0.205257,5.923354,4.165333,-1.041754,1.950114,0.989521,-3.156798,5.471118,-1.339210,1.643204,9.158559,7.438189,0.320761,-6.424755,-1.786758,5.368376,0.472900,6.891779,-2.677020,0.282236,0.391339,-3.331150,3.527578,-9.754203,9.999365,-9.584472,-3.568405,1.797653,-5.419843,-4.870035,-4.437981,-9.028075,-5.680017,-1.569542,6.268894,-3.759329,4.841633,-6.409687],[-6.343581,-7.085334,-3.099456,4.107291,-3.267227,-2.915420,-5.857076,7.568604,-5.569477,4.391556,6.168832,8.359731,2.582244,5.035196,-0.848137,8.117503,-1.505224,-7.216460,-8.192455,5.763873,7.158022,1.647779,-1.218671,-9.729393,-8.743891,-4.569808,-6.356615,-1.409708,1.008408,-8.593745,6.490798,2.819283,7.363496,-8.583112,9.348255,-2.144224,7.923737,-4.804301,-3.035466,-1.722172,-2.233490,-7.814513,-7.105955,-5.255449,-5.164134,5.611333,-8.928843,6.275531,9.404772,3.820666,5.152971,3.506283,1.341009,0.460603,-9.428913,-1.586962,-5.545848,9.439511,8.354365,-7.448892,-0.473902,9.837196,-7.682136,-8.050936,-2.449592,-1.072418,2.849317,-3.699855,-3.212662,-8.969373,7.076068,8.382352,2.330049,-1.597770,8.298769,-4.241627,7.077102,-9.961670,-5.832903,3.499074,4.871455,5.039626,9.901523,1.716783,9.149790,-9.157805,6.522040,-3.119643,6.877550,5.995759,6.106978,-9.943125,-0.458920,0.323965,-1.054242,6.400043,-6.006949,-8.602325,4.836572,1.205060,-5.883701,3.279110,-8.268635,-1.051596,5.413185,-5.541041,-2.552281,4.553218,9.345751,9.208207,7.070178,3.022214,1.497907,8.968744,-6.075913,2.069569,-8.976289,-7.119321,-5.490911,-1.520175,-5.360248,1.005549,-2.920077,9.097346,6.475465,0.109428,-8.413212,-8.358279,-5.834784,-8.866933,1.357029,4.923438,-5.305031,-0.799674,6.776539,-5.732030,6.870575,-5.799708,-0.875903,4.233246,-3.754895,-5.035339,-6.542155,7.412189,-4.375992,6.629761,0.428881,-9.271196,-9.709017,1.779819,0.367164,7.837468,0.758575,-9.483083,-2.526493,5.800987,-6.596641,1.478372,-1.047614,-4.321281,-4.625634,-1.419157,-6.259921,6.928648,7.036184,-1.059932,7.340567,1.644512,2.958972,-8.796105,-0.352182,7.382295,-9.562359,5.640515,7.580637,0.603678,5.181271,4.986764,-1.650388,-7.684551,3.012759,1.902098,-8.367675,2.117724,-1.843087,1.676196,8.267738,-7.873646,9.853658,8.874459,5.356017,-5.541337,-2.883644,-0.493897,4.532418,4.844490,-9.900089,4.828354,2.290741,-6.348965,-3.000646,-5.648926,-2.435348,7.650017,-8.666703,-5.311539,-2.405115,-9.633401,3.120130,4.897353,6.519551,9.094223,7.136784,9.475063,-2.065455,9.024385,7.951694,-9.387031,-0.865345,-4.403065,-3.617656,-2.542157,1.528104,-0.074847,7.239970,7.578842,-2.960906,-0.348126,7.055835,-9.631278,-0.434373,5.703490,-2.516337,1.533503,7.796105,1.855447,6.161244,-3.934043,7.093211,0.021990,7.095022,3.523312,3.437691,4.066209,2.141431,-8.222007,2.350370,-9.970144,-0.555202,-7.349112,3.886059,5.387711,6.665291,3.177088,-1.213959,-2.196463,-0.378969,7.569458,2.219335,-2.002482,1.831135,-1.030916,-6.382808,-1.463918,7.981819,3.500472,-2.595875,1.962110,-8.352340,-0.781713,0.955386,-5.464871,7.882329,3.412872,1.868859,1.877999,1.290379,5.266625,-6.668969,-5.885403,1.259624,-1.644879,-5.747136,1.941584,7.001019,-2.435659,-4.455623,-5.941016,-2.882494,2.747873,1.927021,-3.947804,-2.973101,4.718049,4.621959,-7.791317,5.277786,9.893831,-1.748683,-4.324193,-5.796810,-4.418079,-3.818789,-0.900424,4.189965,-5.595995,8.959827,9.070830,-6.118599,-4.804814,-3.847848,-8.267048,-7.573743,2.299133,6.923666,-0.827396,-5.265006,-2.536156,7.517374,-2.993992,-4.823770,5.625749,4.879895,-0.567237,3.689378,-8.212977,6.025175,9.146107,-5.489120,7.203447,0.199628,4.796122,-1.492679,-3.916788,7.945732,-2.125481,0.492388,7.510921,-0.774853,-2.742835,-8.792123,1.583046,-4.130006,2.970599,-9.958739,-5.951831,-8.553370,0.300644,5.823845,-2.446840,-7.007951,1.037458,2.122466,4.288318,-0.136689,7.076653,-9.515134,-4.703352,-5.347618,9.315681,-5.956650,-5.415287,8.596539,-2.566666,1.390170,2.472049,8.740929,3.885565,0.673529,0.630888,-8.314650,8.568848,0.322863,9.371271,3.102480,-5.404762,-5.074781,9.724450,7.442494,7.983364,-7.428292,-9.969289,2.278939,-3.587896,-5.128899,-4.601980,4.229731,9.091754,9.805870,-8.048792,5.734225,9.222336,2.833225,-9.712855,-1.116626,7.320449,-0.104406,-6.693872,4.402903,3.400214,-2.287582,-2.163510,8.821302,6.560055,2.536412,8.193578,-1.554487,-3.731113,7.425325,-8.573290,-3.433094,3.280652,-0.291040,-9.683189,-7.700955,1.040238,3.427023,-9.366551,-4.666871,-9.048597,8.158246,-8.482254,-3.965579,6.507263,4.589492,1.524147,0.661442,8.183825,-6.227901,0.636179,8.669189,-9.030830,6.936959,6.293941,-9.161199,3.756035,1.674706,9.694533,-4.829293,-4.891278,2.066577,-5.687201,-4.686574,-5.164411,9.202078,8.911463,-1.906002,-4.917342,6.283386,6.121175,8.259468,9.583847,9.160703,-5.580957,-2.183462,6.101809,-3.855978,-5.414419,4.623865,2.034110,8.993746,1.295994,-4.147587,8.390910,2.365543,7.692144,6.862215,-7.212119,-7.785938,-8.305253,2.805332,-5.671398,2.843009,-3.920529,2.725948,-7.280738,-6.214097,-1.476015,0.880292,-5.711114,8.587198,8.615485,2.418887,0.174972,-1.551437,-6.053851,8.733660,4.367813,7.665715,-0.491885,9.401822,1.735660,-4.185432,3.052476,5.439487,1.139214,8.037663,7.060190,-4.632117,-8.573121,2.968110,-4.116547,9.578885,1.368157,9.102620,9.146156,-8.875525,-5.194391,4.003345,-7.781285,-6.990532,0.230951,-1.499166,-3.292908,3.147361,8.287798,0.303382,2.119137,1.891705,4.873641,-3.721011,-1.006789,-0.954559,-5.049654,-0.386479,-9.034939,-8.321154,-4.326565,5.029673,4.169809,-3.881387,4.371055,-8.938755,-9.663862,4.058088,-2.814217,2.326594,5.589079,4.677813,3.607202,-9.476803,-7.176667,9.530528,-5.946252,9.078033,8.776184,-6.054257,8.537065,5.861004,7.924804,-9.554512,5.087045,-5.085650,1.946847,-5.720409,5.753407,-0.208972,7.585308,-1.589660,-2.011520,6.349535,6.597680,-9.402640,-3.573082,2.836290,9.787488,2.138312,2.994758,0.244774,1.282366,2.549008,-1.593262,6.312748,1.633248,2.371792,0.078041,6.953115,5.322997,-6.323953,2.483607,3.242981,5.378617,9.655930,-3.998026,3.654140,-2.410328,-7.914472,-3.944631,-1.682619,9.207540,-8.841142,-8.634002,-4.868789,2.060423,5.918058,-2.338689,9.692687,2.793533,-0.668186,6.708249,-2.408413,-3.028980,2.894213,-5.308690,-9.001365,6.013701,-2.557408,-4.745536,3.962415,4.118341,-8.630485,2.406942,7.263026,9.614658,-0.213687,9.220546,-8.659210,6.210431,1.905048,-9.854559,-5.176596,-1.665271,6.846947,4.961571,-0.521656,-4.041370,-6.988711,6.392253,-2.746069,7.721340,6.849583,6.284253,-4.976907,7.362807,-1.467308,7.649122,-4.386957,-9.304988,-3.805359,-1.846265,-7.323541,3.129717,7.760983,7.927358,0.977524,-5.714554,7.006525,8.795119,8.937926,5.565392,-9.068471,-5.571170,-9.221437,-2.273100,-2.592673,-7.987546,6.197765,7.422972,-4.654895,5.809918,1.473284,-2.180771,0.821767,-8.313557,9.196983,4.563825,-9.607905,-4.904892,-3.390718,4.339890,0.273373,9.039265,0.336245,7.063892,5.073009,-2.403995,2.389289,-7.111600,-0.847424,0.255203,-6.901117,5.099096,-1.060864,-1.920562,-0.421121,0.797963,7.533182,2.288416,7.098139,-9.345270,2.859001,1.888534,4.225778,6.717911,-7.478942,5.655982,4.346149,3.050246,-2.871833,-4.760343,5.663769,0.368873,7.769377,9.484780,9.825714,2.478433,-3.987539,8.472662,-8.346969,1.998738,5.550778,-3.415791,6.203808,-4.197411,9.242800,9.110701,-3.276748,9.712299,1.807891,-4.731984,-0.019991,2.245386,-8.629480,-3.457395,8.863591,7.454162,1.029646,-2.323872,1.348944,-8.587068,5.150360,3.708949,-4.772422,5.255457,-6.411945,9.837679,-2.766787,0.541758,6.801585,1.703428,-6.224241,-7.443085,-7.911940,-6.376554,5.786143,-5.543228,-2.240547,4.778732,-8.348186,-9.421134,-4.436316,7.820188,-2.180458,-9.168294,8.157990,4.059114,-6.890312,7.857217,-7.948802,7.429376,-8.362108,-0.547318,9.899422,-9.637803,3.508647,-6.146508,-9.343559,-7.126457,7.162647,-8.143998,-5.929125,-1.063535,0.891861,-1.761179,6.559757,-2.172951,5.710595,8.213002,-8.153092,7.275428,-3.535544,7.902143,4.937110,-0.199109,-7.230660,9.956193,-0.555980,-4.722402,2.214143,8.654105,-1.317298,7.625263,-0.375914,-1.417693,-8.199534,-7.865733,-9.654008,9.665931,0.234012,-9.258395,-3.229339,7.154158,7.057894,6.428205,-0.603777,9.654754,-8.534606,-2.798360,8.961191,2.639374,-7.010334,1.601370,6.455511,7.701811,-8.599140,8.702447,9.937804,0.426757,-4.312250,-3.480031,1.086313,0.829339,-9.564120,-1.551910,-1.791465,4.851655,-8.486828,5.390050,8.858702,-9.807952,-1.802671,-1.073952,-2.702552,-5.758435,-8.253193,9.005094,2.876495,3.169693,4.046186,5.237033,0.467532,-3.677959,2.847666,-6.660497,-1.966251,-1.004338,-3.493917,5.261406,-3.313795,6.639328,-7.710726,-5.806672,5.595995,5.546836,-2.435786,-5.396839,9.217259,1.688645,2.917460,1.581311,-2.909253,-7.365790,-1.974849,-4.464087,-3.812012,-9.196883,-9.558745,-5.944764,-8.637782,-1.111719,-2.127878,5.233879,-9.912910,4.345618,-0.840750,0.831630,-3.900456,4.714940,5.120565,-8.411545,0.344249,-0.765019,5.249804,1.254911,-2.443622,-5.269591,-5.455567,-4.397048,-4.878105,-3.908783,-9.612013,-3.662584,-1.050385,-6.171411,2.259552,2.689915,5.191896,-4.440722,-7.594324,-1.789972,-2.437424,9.352186,-7.987631,2.584423,1.504972,4.886217,7.389920,5.623614,2.511672,-4.194218,-0.608402,8.204732,4.775171,-9.503830,5.703718,6.431597,-2.706060,9.738424,-2.776656,2.474470,-3.969002,-9.460671,-6.135399,5.688397,7.098217,-0.263967,9.875254,6.385012,-7.501972,-3.716266,-7.056581,7.410659,0.536765,-2.185155,7.637382,4.481595,-0.450145,3.722305,0.883052,6.906429,-9.195172,-7.678615,3.080437,8.788263,-2.709001,-8.140448,8.948035,8.708758,-7.573406,-0.419934,8.320218,1.774167,4.537075,9.821378,-0.679890,6.799845,-9.343642,-9.022516,7.881358,8.303624,-9.997290,1.557016,4.300508,-9.990843,-6.757154,1.421158,-6.957131,4.840624,-4.109239,5.987779,2.829329,2.835412,-4.385374,-4.614581,6.724241,3.526066,0.714785,4.249509,7.892495,-4.861913,9.233050,-1.621026,-2.245517,2.302787,-8.938998,6.510139,-6.765097,0.304425,6.775459,-6.371258,-9.012958,-0.237226,-0.705599,-7.026999,6.107679,3.672579,9.219969,-5.013318,-4.451604,-9.451601,-5.015375,-2.315672,-1.915306,-0.639860,3.008437,3.170459,-6.678322,4.003803,9.998279,3.431386,-3.060088,4.154971,-2.882413,-7.583012,-8.175444,8.138580,-7.256857,7.699042,2.718877,-9.121231,-6.730933,-3.545856,1.655174,-4.955076,-9.477127,5.007265,-8.061276,-9.904140,5.757585,4.456011,5.393353,-5.571425,8.883476,-5.197656,6.067087,1.736761,-0.224826,0.857774,-6.058284,3.449029,6.817158,1.702552,0.665909,-3.814025,-3.907104,-8.182460,-9.591419,-7.405650,-6.421469,-3.569481,0.095557,-6.969623,-8.638492,-8.192701,1.187577,8.675911,-5.243297,-5.679357,-8.104483,-5.408187,6.563881,-4.411580,-2.845426,4.917565,5.243421,-9.704807,3.243706,2.791475,-9.878703,-2.089443,3.070631,-5.460451,0.385599,3.246092,3.947519,-8.626308,0.493506,-5.812493,4.455969,-3.913011,-7.258381,-2.675949,6.194754,9.689976,0.859643,4.061498,7.296146,-4.507351,1.543779,-0.329861,-7.257013,9.770406,6.820874,6.460289,4.169252,5.441054,-6.118042,3.667102,5.705965,-1.941160,5.054921,9.218221,7.282858,5.618763,-2.138417,-9.433748,-7.882332,-2.944650,5.696127,4.003752,5.118350,-0.911525,-9.678226,-1.541654,-3.204546,-2.929270,-7.149749,-6.613906,7.617384,-6.611321,9.989267,-9.143650,-9.483042,8.383451,-7.485044,-8.799499,-7.891165,-2.203503,3.698603,-0.634743,9.695648,1.861727,4.017935,3.108363,2.954470,-4.514592,-1.605102,-9.854095,6.622008,3.311564,-6.079065,3.189614,-1.519219,4.178549,-6.643587,-6.737007,-2.456321,-7.273909,9.058502,4.654306,5.816341,-5.893386,-3.269852,8.928793,-7.051951,-4.700001,-0.528440,2.449704,1.872606,-6.112957,2.034583,3.923468,-4.025616,6.838324,9.774723,-5.844970,-3.905387,3.666538,-0.509997,-3.488099,6.065297,4.191334,-7.190031,-9.516920,-8.480724,-9.872688,7.873307,1.977610,7.451876,-5.274618,3.175118,3.947843,9.724856,1.856506,2.606527,-4.061395,-2.170757,2.117856,5.107427,-3.734809,-2.620743,0.635063,-6.123038,-8.629748,7.720815,-3.961462,6.359899,-4.351191,-8.970402,-5.002758,9.204837,-7.675271,3.368263,-1.657125,-8.316780,-9.183845,4.775377,-8.801992,-2.381281,2.820742,9.283093,7.316289,-8.974758,0.945019,8.132974,-5.835754,3.053459,-8.424404,-2.222260,4.619059,4.696319,-1.772449,3.092525,-1.902716,0.656338,9.048800,6.564017,2.431812,-8.019337,7.715762,3.304793,-5.111869,-4.791675,9.710215,2.511759,3.323324,-3.549060,-7.677888,3.884070,2.697001,-2.437364,4.647343,5.784288,3.268290,-0.982643,3.203227,7.849053,-0.246788,-6.345800,-8.776377,-6.634120,-9.572944,5.248403,-6.114130,2.523003,9.087180,-9.055976,-7.574954,-7.217619,4.383111,-9.321560,-3.996620,-2.293798,3.234534,-2.279960,-2.729680,-7.040183,2.951090,8.911328,-5.543600,2.844834,7.982655,-0.111572,-6.681812,0.991070,7.584626,-8.022451,9.858572,-0.990762,-4.544386,3.324477,1.605607,0.554532,7.743160,-9.723268,-4.796919,-7.320132,4.068875,6.797298,9.792376,3.750379,-6.468130,-7.006385,-1.578251,-6.784092,0.350870,-6.963688,8.470420,7.782408,-9.836592,-5.310944,3.075150,-7.227082,-6.341700,-9.432170,3.668611,-1.146882,-0.292135,4.748888,-0.956255,1.492883,7.093587,-1.308973,4.447003,-6.032547,-1.048276,-3.110522,3.911116,-4.873620,-6.555224,2.450835,2.599889,6.860045,-2.822439,-0.120093,7.715231,-5.046105,8.336752,3.633167,-0.321941,2.857990,9.080346,-5.660042,-9.288970,-9.701129,-4.450513,-2.271054,8.315509,3.765019,1.758703,-0.891215,7.501440,4.371614,-8.444892,4.777924,-0.678214,8.329137,1.746507,-9.055861,-2.652464,-6.495206,-2.946209,-3.528867,8.293799,1.643418,-7.347477,6.804222,-2.840261,-6.799272,3.395433,3.453502,-5.881953,7.783967,4.931847,-1.704568,-3.144199,-5.911143,1.115543,2.259757,-9.777903,5.141620,-6.248039,-8.940051,-6.719984,8.372933,-5.701422,6.640826,5.308734,-8.173490,2.647684,6.020672,-4.483079,-5.876086,-3.961373,-9.320317,7.513712,8.912825,-8.903560,-1.372844,4.306651,-4.320746,3.559957,-2.073843,6.763547,7.015175,3.216928,-8.777653,-3.080649,-7.128196,-7.552518,5.579030,-6.270423,-2.822191,-3.583733,0.121358,-4.790149,0.546621,-4.892356,4.086330,3.692753,-0.889335,8.628720,-6.932110,2.040799,-1.094229,1.772300,9.752224,7.328180,-9.062363,8.852814,7.190770,8.005288,6.477700,-0.608999,4.732282,2.644104,6.412175,9.045552,-4.765840,-5.718057,-4.593842,-0.828662,6.388942,7.739174,6.523463,-5.752978,5.317765,5.473390,3.483851,0.727667,0.830648,-7.869519,0.535889,-1.296842,-6.533999,-1.286789,-4.559651,8.591325,-1.604167,2.606364,3.895372,-7.757594,-5.832701,4.540780,-1.645329,-0.434341,3.422716,-9.815814,-0.946225,-5.654303,6.430014,-2.964452,4.311686,7.952797,-6.142288,8.237183,-7.785682,-1.585948,2.132759,-9.833740,-7.926926,-2.803292,8.438257,-0.310214,0.030430,0.606343,-6.418199,2.660307,4.855021,4.524826,9.652825,8.747058,6.426529,-7.231635,0.287966,-9.658170,-8.909846,4.985200,9.111976,2.072256,-3.326869,0.016893,-2.614637,-8.617382,1.678123,-2.567811,-2.718806,1.897271,6.505580,-5.466369,-7.587873,8.384894,6.346460,7.019761,-6.366075,-7.132380,5.766231,8.149210,-0.993915,8.475643,-5.505372,-1.638079,1.008693,-8.057101,-8.779753,5.840367,6.155459,6.950893,6.448550,4.261795,3.471635],[-2.687180,2.139516,6.442030,6.691530,4.321958,-0.410963,-5.852759,6.605031,-4.367494,4.510204,0.865341,-6.480204,-6.744518,9.427929,-7.135699,5.525622,8.555620,-4.018032,-4.681842,0.427787,6.984043,9.433702,6.874960,-2.247414,-1.050954,3.819592,-6.669940,-1.753244,4.330472,-3.808688,7.119428,-3.242038,-1.604177,1.023772,-3.836728,4.793251,-0.880362,6.343075,4.114155,4.765163,5.814164,2.615072,9.416001,-8.565666,5.936085,-7.856823,-5.376566,6.470982,4.562909,3.038910,1.704181,-3.911782,-7.134832,0.759047,7.339349,0.941681,5.766121,9.584353,2.540842,3.615957,-5.485393,0.421206,-1.075444,-1.492693,5.219177,8.441556,-5.965260,-2.002352,1.344915,-8.138374,-2.055656,-0.372232,7.297400,-4.287379,3.042259,2.395928,8.024815,3.465282,-1.046889,-8.778238,3.479852,-1.495321,4.523106,-7.120900,3.828750,1.748707,8.815470,4.408641,0.895406,3.666110,-4.471193,6.973570,1.099418,4.577642,-4.175740,0.103210,-0.279289,2.884105,-9.899614,-1.161264,-2.055430,9.684951,2.038294,-9.767211,4.697660,-8.052031,6.687797,9.275586,-2.876839,-3.899720,-5.890476,-5.690847,1.004306,-5.116370,-8.862012,0.193964,6.336284,-1.720813,-2.884079,1.543648,-4.374905,3.205314,7.474150,-5.204340,4.165510,-1.690591,-1.350921,-4.275240,-0.224931,2.325049,-1.494134,-4.592258,7.974082,-4.265320,1.552626,8.561278,2.308959,6.266796,-5.176777,-1.228783,-9.187155,3.682601,-2.556164,5.571984,6.291186,2.955686,5.776973,7.999024,-2.805405,-2.267603,6.785563,0.503045,-5.779971,-5.033020,-2.330402,3.219183,0.202441,3.522814,-7.149053,9.145720,5.926670,8.244471,-3.207942,8.973708,7.570183,-7.020174,-5.430424,2.923490,6.664580,4.464905,2.936816,-0.731533,4.338753,-1.555269,-9.128523,6.626736,-8.779915,5.560410,8.800532,6.110818,-8.921651,-0.662590,4.107558,-5.503791,7.918751,-8.679092,-5.626664,2.364324,-7.277680,8.645441,9.801696,-0.104697,-2.921894,-4.958929,-5.117835,-2.107100,-6.137353,8.736802,-9.465896,-1.101854,9.207039,-4.675865,4.671629,-5.276076,8.137168,0.746192,-9.361681,-1.821061,0.642532,2.089628,-2.692764,-3.576609,-5.130166,-3.061511,5.936017,-4.024960,6.962759,-5.427407,-6.256637,-1.406013,7.922572,0.905384,6.026564,-8.512782,-1.878255,6.385402,2.677966,8.074467,2.349748,-5.703516,-8.918773,-5.605789,-1.770217,7.381175,5.281762,-6.401314,1.810730,-9.169654,-3.507978,9.496334,-5.531037,1.164529,-6.940101,8.376260,6.831145,5.011642,-1.063534,9.554971,-8.594631,-5.641612,8.581091,-4.249544,-5.317872,1.125529,7.233127,1.110907,5.434908,5.141964,-3.206561,-7.402309,0.499627,9.903476,6.385023,-7.999695,9.963134,5.792236,2.556273,8.553325,-3.216221,-9.481647,1.060074,-0.229157,2.822736,2.545760,-1.880261,3.832673,1.411554,-6.137719,4.919148,-5.639204,5.460103,6.009303,-7.166664,-1.684466,-8.126967,-1.785792,-1.295658,-4.273762,5.124122,0.408759,3.980948,4.925053,-9.849596,9.370252,-6.183609,-3.000897,9.455607,-4.953151,7.354571,9.160159,-5.211439,3.201376,-6.807892,-8.243768,1.030080,4.044966,-6.619048,1.580257,-6.256201,-3.517715,8.022353,-2.617873,5.763342,-6.409049,7.726477,-5.485813,2.275505,0.802635,1.023446,1.368972,4.933407,-1.109040,9.208846,-5.512027,-5.285905,-9.468310,-6.625934,6.114931,-3.595665,-3.422886,7.504514,3.732968,-7.146864,-8.065945,-6.829310,2.218731,-5.659705,7.066329,3.899084,-0.922773,-0.201183,7.969558,5.658705,-7.572743,-1.669132,-3.451526,7.874149,1.231133,-0.232168,-9.465753,2.984022,-3.289074,9.450501,-7.044912,-8.161059,-7.650463,3.899830,0.023102,-0.530916,-9.894264,-2.131974,-2.764481,-1.736008,5.750605,7.245041,0.806797,1.406227,7.874729,5.498627,-4.656689,-4.992941,9.197188,-5.406735,-0.076015,-4.789677,-4.144108,3.454994,5.825204,-8.299298,-1.504002,-6.076739,-0.142775,-9.453063,-0.144455,8.994859,9.052309,5.541927,-3.596731,0.165924,5.122200,6.632089,-0.221934,-4.119535,7.811686,-7.559315,6.711173,7.948853,0.641404,8.966901,-4.962087,-6.400200,-7.236553,-0.148877,3.703656,0.161398,5.663287,-7.058374,-6.774181,9.888802,3.383191,0.903626,-7.341277,9.914796,-4.483781,7.829237,4.076400,-8.902796,-4.504757,-2.233942,-6.534604,-5.357694,8.886491,7.880939,3.675225,7.408330,4.633395,7.141710,2.614932,1.035202,8.515406,-5.752727,-6.680813,-3.459160,5.513731,-4.620027,8.957204,-1.510117,-0.445239,-7.225645,-7.494798,-6.645758,-4.568118,-5.445576,-4.909422,-2.693178,-6.790854,7.980688,1.228197,3.049455,-2.663174,4.798447,-9.681237,-6.405386,1.136663,6.520397,-8.841343,7.596559,1.396744,4.347793,3.132009,-6.343770,-5.909630,-9.475202,8.112774,2.814522,-5.910024,1.173808,-3.635422,7.778907,-3.625154,5.157333,-0.910408,-1.232217,-7.073016,-7.893717,4.300776,-1.887738,-8.053821,7.409478,-8.277254,5.324962,0.983896,-2.360179,8.694500,-7.590376,-2.946312,-8.215735,-9.188918,-9.205850,-0.094059,6.208983,0.906973,-1.426349,-3.256887,-6.801541,-0.278129,2.478197,-9.506125,9.263306,4.115831,-3.207676,9.321142,7.676396,7.089017,0.757506,-3.066633,4.126017,-7.938536,2.923915,9.809951,8.965223,4.521297,-2.706129,-4.251332,1.749254,1.343338,9.914566,0.244743,-4.005921,1.927503,-9.236998,-8.322818,3.031534,9.480350,-3.462563,-5.690477,-0.288933,-4.591615,-9.386566,-1.474192,1.990313,3.969447,8.016158,8.116733,9.907437,0.916656,-3.207453,5.913493,-9.880584,-6.249124,8.243047,-6.789541,-7.630191,-1.292499,-5.116316,7.339656,-8.428772,-4.040156,8.519860,-7.787779,-7.293038,-1.653559,3.861803,7.200757,8.635657,-9.271604,-1.203307,-3.310062,-4.466570,6.572876,-0.845824,-2.720260,1.065621,-8.558779,-5.126795,1.994528,-1.740022,5.064228,0.391257,6.696293,-1.729268,-4.810701,-9.192451,1.945448,8.124064,8.361693,1.593369,3.204670,0.567265,6.777255,-6.019943,-3.694755,5.174610,-6.216068,-7.999897,5.158206,-9.656843,-0.416650,-2.108834,1.764920,-9.238350,0.420766,-1.915691,3.056472,-0.864854,1.465601,4.196068,3.424678,3.193562,-3.309852,7.034713,-6.428904,2.027666,1.285289,-3.335822,9.020902,8.405812,8.091171,5.349071,8.422585,1.679806,-1.804730,0.443989,1.195966,-2.543323,-6.520020,6.885648,8.973720,2.573912,3.589522,4.546100,7.218685,9.353753,-0.479720,4.555070,3.296879,-3.399381,9.867839,3.358988,-0.365302,-2.220381,-3.257244,8.599823,-8.612075,-4.252650,-8.349138,4.672498,-7.815611,-9.132587,8.394125,8.669709,7.157048,3.292662,0.150360,7.025452,-0.210599,-9.012870,-5.783085,-2.015794,7.290195,-7.945854,-9.968091,7.822987,-1.045187,3.392876,5.644863,-8.007396,-6.118252,1.065094,0.620829,8.276243,7.746809,-8.449508,3.118037,-5.720577,9.262138,-7.367160,-2.484292,-0.729799,-4.683294,2.988693,-3.467464,-8.126265,2.207132,-8.508807,-8.444141,-0.436295,-1.473692,5.932506,9.568756,-2.256567,-1.690423,-6.994667,-8.717143,-5.156717,-2.137025,-6.394710,1.898616,5.141292,-3.288036,8.039336,9.276610,-6.436587,-4.976339,6.007588,-7.980781,-9.392895,-4.943569,7.762015,-2.546239,5.725977,7.906123,5.614102,-8.239667,6.741295,1.151927,-3.726843,-6.769973,-1.655453,-5.913009,-2.640947,9.323873,-1.101413,9.682180,-0.361254,2.962298,-3.015073,2.919651,8.364038,-1.072902,-9.516120,-4.075842,-2.355725,-2.120931,8.502151,-6.419576,2.894157,8.352382,-6.229047,3.860259,-9.894066,-8.399197,-2.306424,-6.099941,-7.179124,-5.555404,-9.086199,0.341918,-6.959221,3.088552,-7.304105,3.671370,9.458635,0.311939,-0.505145,-2.884157,3.989625,6.586245,-8.840608,-3.472369,6.735354,-8.031249,6.687863,-8.633926,5.635692,8.361914,-1.939892,5.304194,3.501625,7.059650,2.401443,-4.021466,-8.844231,-1.137534,-3.680649,7.997679,-7.467543,0.029482,6.528488,3.914134,-3.212933,9.263195,0.192693,-3.132138,1.280201,-8.879889,-2.752090,-5.601721,3.925153,2.538426,4.851734,8.766339,-6.370319,5.120374,-8.463695,-6.990532,5.777740,8.820119,-3.087977,-8.164263,8.540315,3.525459,6.546209,5.431578,-7.831290,-1.487586,2.173289,4.801313,8.098777,-7.634343,1.490827,-3.181777,-3.663271,-6.917454,4.824075,-2.924106,5.237812,-4.945979,5.369557,8.149097,9.573120,4.635980,0.213731,-7.371604,4.251216,4.262011,-8.841555,-5.035913,2.307579,9.267881,1.975268,-3.175476,1.796725,0.302272,-8.918779,8.693754,1.714507,-2.461696,0.103719,4.240576,0.540701,-3.804265,-2.060992,-6.645957,7.687389,-2.366302,-4.819852,5.703560,-1.479505,-9.693212,-6.394763,-3.510951,7.535671,-3.350351,5.431128,5.243362,-0.388997,-5.942375,-8.614323,0.655165,2.573233,-3.691033,-4.476134,3.044753,4.866395,0.622542,3.979410,6.045156,-3.542302,-1.173015,1.923861,3.062941,8.652951,-2.331685,-1.299678,4.510351,4.957213,4.102056,3.091942,-2.056402,1.015084,-8.502673,0.910307,2.952311,-6.961367,-9.518953,5.622674,6.331691,6.678145,7.175744,5.122119,7.970169,-7.040371,-0.246036,-7.074903,-9.122017,-5.701747,-6.740806,-0.025049,-0.568039,7.433689,-1.793121,-1.545191,4.258921,0.034430,4.233957,6.880036,-8.110358,-8.622495,-7.271959,5.040780,-4.227464,6.572255,-9.398832,-7.086795,-9.885734,9.974778,-3.675055,0.429825,2.620691,-3.482585,2.657091,-8.672962,-2.380027,4.684440,2.101489,5.367120,-9.751885,-6.900263,1.635087,9.936488,8.582484,-4.616812,-3.895458,6.733027,2.867844,5.748209,-0.966726,-7.705297,-8.251291,0.765132,-6.903785,2.151716,1.884445,3.018109,-0.299991,5.674811,8.247566,0.178558,9.009756,-9.551338,0.722859,4.530763,0.862346,-8.235220,3.812953,3.254221,-2.923174,2.910305,-9.922934,-9.346894,7.981102,-4.198063,-8.131881,5.017742,6.137651,-2.953047,0.758405,-4.730604,2.097319,-7.855281,-9.542997,-0.681407,-6.620227,-9.381154,3.112868,7.762437,-7.226899,5.233338,0.684704,-9.041880,-9.505838,2.302399,5.616277,-5.536962,-7.200167,4.093806,-6.226841,-6.558565,5.925414,-6.156054,8.245329,-2.634273,0.773491,-0.419426,-9.939486,2.169197,4.164989,-1.102756,-6.511737,8.778795,3.201568,9.405027,8.304680,-2.107346,4.026919,4.439517,-1.489608,-0.963788,0.310215,-2.175820,-1.046581,0.506544,1.999174,-0.537271,-6.387849,-1.381400,-3.047917,-1.689161,5.299469,5.828555,9.584245,-4.475439,-9.760549,9.878855,3.493756,8.862158,-2.067726,-1.393135,-6.846823,1.407594,-2.142996,-7.591604,-5.711140,-6.392417,8.091303,-4.567060,-7.069655,-0.016596,0.032473,3.207407,2.143220,-5.664484,2.411962,6.504883,0.424627,-3.341445,6.164817,4.648651,1.437251,2.236361,1.509137,9.631800,-8.986798,-2.558693,-3.257755,6.414939,-7.526435,0.488187,-9.860296,1.660826,3.300651,4.586726,-3.396800,-1.901984,5.131489,-4.963945,1.919250,-9.946611,1.623262,-9.786536,-8.826595,4.039759,8.679938,-7.610109,-3.765709,-8.021382,-3.026336,-2.780469,-0.469515,-3.221994,-2.937150,-8.819751,1.577111,-9.601476,0.036525,-2.399337,-4.476633,-6.068708,-0.931948,4.297854,-3.240054,-3.652567,2.218174,4.694486,-9.279616,2.267191,-6.331674,-8.464150,8.275848,-0.295953,6.514102,-7.179933,-5.428156,-7.851979,-2.778209,8.486683,5.079356,1.613709,-7.269973,-1.288129,-3.945418,-3.248843,8.492508,-5.115967,9.858523,8.026419,4.642860,-1.961102,-1.908678,-5.429792,-6.483465,0.236348,-2.789099,-8.437544,3.897268,7.335409,7.844014,-9.316089,-5.253445,3.997765,1.652435,6.415117,-7.294795,-6.046058,-1.471907,8.878948,9.737578,-1.522258,7.005313,-5.561352,6.081448,8.227614,9.758017,5.935795,-6.403666,0.798603,1.898694,5.056821,-0.585628,-7.912713,-5.182634,7.788735,-7.152134,5.480000,0.118715,-4.219398,8.690546,4.654924,6.200464,4.725144,3.621739,3.313325,8.910554,-3.611101,-4.186845,-6.564596,3.385785,-2.466348,0.856564,4.730449,-3.187955,1.895146,9.324866,-3.284658,4.414820,1.183550,9.017744,0.152755,5.681744,-7.420248,-0.224098,-5.522814,5.584073,6.692751,5.819689,3.506822,-4.378710,3.753458,0.728664,-1.381255,5.237667,8.423161,-8.254195,4.926420,-9.958766,1.256661,-8.891009,-2.704695,7.195805,-5.503740,8.664611,-2.145581,-3.278830,3.275999,1.469514,-4.958182,3.260505,1.370848,-8.317460,5.612920,3.814015,5.507258,9.560935,4.920728,0.409482,2.500615,2.836087,-7.339660,8.061067,0.755742,2.444721,-5.708324,6.006319,-3.713710,-6.004906,-8.522539,5.112470,-5.159073,-8.382304,2.219032,8.410766,-3.010998,-6.345460,3.269479,-7.167786,-1.919377,-3.672114,7.684734,9.972249,-8.537133,8.629376,9.317361,-2.041559,7.772665,4.284183,2.954970,2.020754,2.183621,-5.233532,-9.699172,5.763030,4.678082,3.780850,9.819733,-1.186120,-3.855944,-5.086308,-2.346819,2.415624,2.480899,-6.769772,-4.124897,-8.792223,6.578451,-8.255045,-3.784512,0.047418,6.534498,-4.451831,5.040458,-2.456465,-4.316336,9.977871,-4.042590,5.634981,1.096524,-3.657622,6.508701,6.097762,1.505888,-8.991557,1.585920,8.729172,-4.425177,5.105969,3.603503,-2.427500,-4.055442,-7.464385,-1.792412,4.609172,-3.089262,7.444214,-7.415863,-7.538567,-1.811243,3.556923,-4.951409,4.989113,-0.962170,-4.113256,-6.054440,-9.301691,-6.032131,7.421278,-3.473468,-4.703974,-6.827338,-8.158569,-2.952858,0.209929,-7.347437,-6.576134,3.663289,5.460329,-4.677945,6.382347,-7.042033,-7.540990,4.494069,-7.704592,-3.884264,-0.551858,-2.392235,1.420527,8.175485,-5.881977,-4.886152,8.499714,-5.670350,2.197927,-3.075015,9.811823,-6.014136,-8.645624,-4.963841,4.008906,0.348435,8.846477,7.085032,7.788515,2.991760,-0.411390,-0.813490,-7.972516,-5.217883,-8.097338,-1.022374,-3.034632,4.624112,-8.626480,6.140012,-9.000812,2.728119,-6.481655,-9.873577,-8.091949,1.954144,9.102405,-7.254875,-6.353949,-4.503200,2.385194,6.601238,0.753990,-9.496060,-2.779058,-8.078779,4.020750,-4.034108,-3.110823,0.462555,1.895455,1.096219,-1.674868,-3.639386,-9.498001,3.035808,9.690329,8.949161,0.832828,0.578084,5.687874,-8.231080,6.752163,2.281957,-2.140403,-3.083026,2.762297,-6.484783,1.210554,2.082029,3.706555,-2.940752,2.824884,-7.827140,8.242417,-1.134134,6.842514,9.130842,8.600068,-1.475803,0.105997,1.374627,-3.448195,7.459029,-9.915004,9.974892,6.677743,6.842446,-4.077144,-2.745337,3.188814,-1.421288,0.969362,2.102741,-7.141715,-7.899388,7.485386,6.350400,-8.273578,3.264975,1.329308,-8.248868,-2.708183,9.537345,1.297278,6.920387,-5.917076,1.440209,7.038718,-0.819829,-3.857686,-7.738256,6.484587,7.456326,-1.535319,-2.527651,-9.352906,-8.946607,-9.220073,5.919458,0.380800,-4.513143,-1.061282,-1.206174,3.129804,-4.045598,7.405393,1.905207,-5.439966,-4.925354,4.661469,-4.414404,-9.102247,6.991835,-8.016243,-1.697570,0.381823,1.787009,7.969751,7.541851,-6.779000,-4.927991,-1.728608,-6.753487,2.372661,3.888841,-2.562792,-3.573767,2.011693,3.386819,-2.902310,1.341305,2.818984,1.329257,-6.457113,5.444869,-2.681966,2.468526,8.295111,9.348261,-7.146975,0.238703,-2.053407,9.709347,6.439986,4.166681,0.081710,0.163600,8.918936,3.314828,-9.042034,7.585900,-4.018384,0.150285,-5.706386,-7.357653,-0.319068,9.411999,5.504361,-5.288415,-1.609941,-2.273658,-4.908295,-4.178230,2.501456,-9.527015,-9.307213,-8.378259,-3.135183,-6.274227,1.611503,0.288220,-3.988618,-4.464262,-8.675916,2.420849,4.320213,-4.916750,9.606431,7.092814,-8.303070,-7.364597,7.716889,1.725552,7.942831,5.470527,7.002420,-4.400676],[1.456268,6.189373,3.073816,-2.684616,9.490248,-9.171654,6.914146,5.414183,1.439210,-2.667066,-0.836454,-5.622540,6.312632,-7.370549,0.864826,3.370072,-3.336782,-6.260410,4.928934,-5.540838,0.593873,0.288324,-7.400645,-8.232232,3.068540,3.811278,-7.150627,2.010868,3.342398,-8.852293,-7.835604,0.380861,6.665923,-2.561719,6.077876,7.107150,1.734722,5.457801,3.892686,-7.506565,9.163425,-1.893522,2.245914,2.898542,-6.236290,8.207470,8.227662,2.757038,-1.667538,9.974542,-7.625311,-0.290659,-3.238880,9.698005,6.067258,-0.682814,4.202276,2.572265,-9.132761,9.503409,-8.898910,1.050852,-8.713084,-0.993665,-5.154015,-5.743843,-3.996164,-1.395264,-6.509536,-9.955118,2.711264,-8.173626,-7.906135,-9.802324,2.776509,0.038585,-3.753471,1.074407,9.515200,-9.753626,-6.640545,-1.501599,4.591719,9.034298,-7.406623,-1.692194,-5.010150,2.128423,-8.127428,8.843093,2.338926,7.830996,0.404221,-9.743182,6.623972,-6.794685,6.815097,-6.121385,6.779389,3.282599,-4.978040,-4.536706,-5.366995,2.612805,3.057997,-7.227459,0.638990,-6.863173,5.584365,7.488236,5.069474,-6.069358,-4.143655,-1.787128,-0.389742,1.106513,9.502283,6.061982,8.720385,-1.505296,9.285626,-8.464490,-2.909868,3.030946,6.834547,-0.385254,-5.078521,-7.970873,-2.554202,-3.074542,-8.834568,1.400116,4.444445,8.918981,2.648342,7.929341,6.956937,9.251896,5.613327,8.601844,1.889386,2.408245,-8.388786,-5.889177,-6.264110,7.253557,-8.182776,-5.067953,3.366229,0.311678,2.619650,5.635132,-6.067457,2.186012,1.598646,-9.245904,-1.869265,-9.945302,3.795112,6.930050,1.514607,-8.086996,9.771431,-8.746093,1.726844,9.456562,-0.509858,8.959116,1.281193,-6.066956,5.817063,5.681758,1.801599,-4.367939,-4.718957,-0.832755,-6.628804,-3.700116,-0.755575,-8.720363,-3.579399,-1.343297,-7.428883,7.540228,-9.833941,-8.398007,-6.349839,-5.381839,9.166999,2.706448,-5.342331,8.659418,-3.302637,8.956767,-8.844298,-2.363104,3.218978,-1.462003,-9.619728,-1.091280,5.075052,-5.532737,-9.338148,1.337282,3.611551,-5.561305,6.596712,-7.927363,9.990444,-0.038744,1.690432,-5.494224,6.351256,-1.009616,-9.114793,2.361520,6.673749,1.421945,-4.819807,7.912893,1.099922,7.954518,-3.454232,6.164506,3.198816,8.699872,-4.115512,-1.879995,-7.880049,-2.028702,0.773853,8.028159,1.987475,-7.983364,8.155338,-9.747773,9.953632,6.990511,4.144949,3.631138,-1.854447,-8.095774,-7.408635,2.174398,2.064924,3.457383,3.782165,-8.715542,-9.163975,-4.469754,-0.274486,-7.222938,-6.245400,3.100539,-6.425464,3.973985,-5.944821,-0.392811,-2.251011,8.132939,7.959469,-8.085341,0.840298,1.817559,8.361897,-5.355060,-8.999074,-7.430501,-6.229896,8.064681,-6.933762,-6.319213,-4.925105,-9.595377,-1.823334,-2.846762,-1.486102,-6.507843,5.255602,0.576287,9.083702,9.293521,5.097778,-6.413821,6.873143,-1.332094,-7.638494,-1.037059,9.979507,2.906841,7.083590,9.481383,-6.385814,8.262769,-6.998001,6.234086,-7.163801,8.060122,-6.120482,-4.960687,8.568148,8.507165,6.969416,-1.760198,-8.353600,-5.767353,-9.085563,-5.007717,0.978870,-9.588932,-8.409379,3.772939,-8.754583,-6.041732,-1.202226,4.166862,-1.003284,-1.397571,-5.865520,-1.074792,-7.619740,-0.377226,8.799600,-3.916330,0.965969,-9.865323,-4.947102,-5.841929,-4.126091,3.947686,0.319092,5.849056,8.556715,6.508034,-5.482878,0.911297,-1.650788,0.797092,-3.828759,-0.422113,0.471582,8.568963,-2.332765,-5.532805,9.607361,-1.928514,-2.641087,-3.526710,5.897121,-2.317028,0.371685,-3.539407,9.359957,8.615650,8.103800,8.205772,-5.205412,-7.363269,8.762499,-2.540798,-6.640624,2.218119,-4.593215,0.221586,-1.690076,5.178807,6.698573,4.608958,-8.971040,-7.313378,4.316600,-7.714068,-7.382315,-0.079432,4.169255,-0.350487,6.875699,7.068105,0.031238,2.947893,-4.028760,-8.440683,4.674980,-4.134460,-4.587859,8.302503,7.144271,-3.421486,4.291167,4.433897,4.259819,-7.237089,5.376122,-1.948349,-2.881467,-6.420099,-2.845674,-7.435323,9.272365,0.727546,0.580215,4.140247,-3.955097,8.712365,-1.074104,3.925245,-1.448649,1.052705,7.046348,4.419474,5.709648,-3.316647,-7.309198,2.734581,7.010659,7.443395,-8.886231,1.577220,-2.013392,-8.725187,4.573623,-5.564982,1.163111,-7.332339,7.444569,8.982831,5.947689,5.559873,-3.208557,9.167014,5.595405,7.541738,6.320968,2.486896,9.648660,6.642846,4.249176,-0.437896,7.481578,5.451467,-9.064718,0.107941,-4.273260,8.718605,-0.318455,-1.085835,-5.692283,6.876107,7.450862,5.571033,-9.714144,4.073027,0.171290,-7.071237,-9.740082,0.176712,-0.309362,3.828872,4.431726,-7.610390,2.649424,-4.775564,-0.962141,-2.739258,-2.075244,-4.178869,-0.907546,-7.788772,9.971013,-0.584621,-5.318945,2.272935,-1.741272,3.823615,9.099416,6.801363,-3.429073,-2.909604,4.115658,-6.056877,7.655028,-3.801098,7.027978,3.669238,-7.959184,-0.320938,7.320392,7.393286,-5.963429,-7.436392,-7.877442,1.348890,8.304570,8.843157,-0.304561,-1.682524,-2.806116,7.364732,2.043922,3.553255,-4.376870,-3.792258,1.912625,4.089950,-3.033339,1.171420,-3.816805,6.107662,2.207149,-8.328772,1.884492,9.656115,-5.564789,1.441743,7.757421,8.696631,-0.190391,0.062619,6.646817,-6.664410,-7.757404,1.834856,-5.395000,-4.878027,1.793307,5.609260,8.449753,4.805681,6.523036,2.114067,1.255163,-1.314637,-4.412477,1.126234,-9.428091,2.618284,0.004154,9.840776,-0.143375,9.732335,6.846456,-9.768419,7.289791,-3.237313,-9.126605,8.254747,-6.430802,0.276015,-5.124121,-9.349932,-1.025085,9.072560,-5.925230,9.504155,5.647994,6.041381,5.390710,1.778716,2.349024,6.951699,-2.060457,6.466095,-5.213784,6.005514,0.570504,-0.923435,-7.704684,2.423343,-9.615019,2.784489,-0.893667,-5.509679,-1.064036,-3.667383,9.778600,5.280735,8.802066,-9.918168,5.696509,-7.914782,-7.144192,5.718732,-3.187435,8.900957,3.273431,-2.852482,5.793112,-2.540749,7.420715,4.949985,-4.361267,-7.289966,0.880149,-3.420940,-4.276768,8.071293,0.335095,1.962526,-6.531373,-4.395685,5.929078,6.872253,-3.261054,-8.104568,-7.692393,-3.364408,-5.126419,-6.100800,-0.731194,0.946269,1.692626,8.393115,5.743012,4.342867,9.943097,5.849889,-0.051053,-5.823783,-7.704846,-4.209338,-2.594175,-0.612491,6.364503,5.838474,1.683607,1.579742,8.375240,2.959238,7.755341,-2.142632,-2.768449,-0.954104,-8.446401,9.930598,6.483721,-1.163540,7.139119,4.827105,3.405447,-8.396242,6.516747,-7.728064,-8.250552,6.129109,-1.659350,-6.380892,8.155946,5.568375,5.882441,0.166267,4.751428,1.407500,-6.714722,1.865677,5.474950,-9.655151,8.123376,2.719102,-6.439548,-0.186226,6.718117,3.132044,2.824923,-3.491122,-3.017229,6.674786,2.027331,-7.982852,5.199975,-1.721911,1.055007,5.870992,1.048221,-3.464882,8.034346,-0.308243,3.668233,-3.615241,-1.707294,-4.316031,-3.648595,-3.916957,-8.571343,5.123838,0.405014,-8.454044,-8.749833,3.366183,-5.205234,5.707011,-3.507080,-0.849158,1.767195,-6.816895,-5.755806,-0.209588,2.710650,-1.947830,2.100599,9.968442,9.555113,7.924734,-1.253412,9.331777,-5.432088,-2.179053,-1.555446,0.211925,7.466600,-1.613477,-5.832626,-1.426075,1.016226,8.930950,-1.550280,6.990087,-0.138268,8.729423,-3.237146,7.628910,6.934233,2.077190,7.822972,-6.539378,4.850079,-0.265399,0.969890,7.589375,1.299340,-5.902497,3.013283,-7.118818,-0.996051,-2.714040,-2.606475,-5.425961,-1.445758,-1.342276,-2.979903,-1.381663,4.080951,9.751288,-5.557809,3.169000,2.170964,3.319832,-0.106787,-7.356163,-2.022715,2.669803,-4.477536,-5.637626,8.500404,-4.686445,6.599082,3.223405,7.629687,-6.820030,9.275206,-3.427422,5.426651,-9.613556,3.555143,-6.402297,3.473814,-3.424568,8.088400,-1.485564,9.129353,-8.872950,-4.399453,5.621801,-5.367499,1.325346,-3.321419,-0.832573,2.973817,6.088190,7.416822,-0.902978,2.863267,9.268167,-9.892777,6.317484,-0.545300,-5.087611,-9.959128,0.634321,8.424123,-6.774057,-5.894906,8.909406,0.678300,-6.974509,1.592047,-4.033848,5.530919,0.020203,1.284008,-1.809628,2.667152,-2.584033,-1.130810,-0.091862,-2.907223,0.847296,-7.249600,2.238332,9.057500,-5.529051,-7.902024,0.195182,-7.879236,2.800725,-8.134323,-4.930551,0.901364,5.258753,-3.112298,4.541187,-4.151022,4.843144,-3.342826,2.226735,-6.563777,-1.632691,-8.176129,-2.031523,-2.140202,-8.370621,7.339659,-8.795291,-2.748095,2.146349,-0.462900,1.722565,9.093858,3.777176,2.107374,-2.786987,-2.743343,0.116045,-9.910419,-7.570732,3.700135,2.382792,5.634394,7.259181,8.072750,-0.517905,-4.458958,5.568633,-8.976747,0.327966,3.598088,4.973038,-4.108371,-8.282513,-8.673516,2.269633,1.902547,0.215557,7.020737,-9.794896,2.960915,-0.234762,0.501060,5.415731,-9.522701,4.107366,-4.088294,5.627750,1.683450,-3.730696,-9.394910,-0.995557,-3.347596,-2.448739,-8.270060,1.707612,8.086509,6.699352,6.288874,-5.098157,9.228588,2.165091,-6.605648,-5.299294,-7.307087,-9.711777,8.896347,-0.733127,-1.897913,4.467337,-5.582203,-8.221438,-2.636848,-6.035040,-7.026863,7.140166,-9.633263,-9.108723,4.217610,4.906271,3.050787,8.374198,-8.019964,-9.242008,-3.173375,8.680656,-6.179481,7.824570,-3.819811,-5.462699,-0.858841,-3.991807,-6.437317,-5.348739,-9.572441,0.933595,5.080639,-0.451811,2.283663,-6.665240,-8.737988,-2.873388,9.277549,3.376438,0.180007,-0.545208,5.228153,-6.264774,3.197505,7.815723,-6.392738,2.950717,1.675415,9.569382,7.565850,7.358084,-6.050231,-6.003383,1.016533,2.584821,-1.739759,-8.139441,-2.211181,4.400702,6.485922,3.822897,-2.747230,7.100757,-6.011194,-1.087713,-8.846002,9.053939,3.114494,-5.519297,1.610693,9.431101,-6.241010,6.173208,-7.962400,-9.372756,-0.767243,-3.099355,6.524834,-3.464908,-8.808280,5.196889,-6.743925,6.234503,-6.744342,-1.749663,4.589358,2.511608,-1.551071,0.723104,-3.787718,-8.568119,0.295978,2.156058,5.332040,8.828026,-4.700836,-6.298903,9.237580,-5.058913,-2.335119,-0.427816,-5.177171,4.315041,-9.744253,8.321873,-9.105598,7.077063,-4.307262,-8.541364,7.012251,-7.728661,-4.037797,-1.189607,-5.695971,-0.351784,-9.003037,8.094063,-0.594077,4.803497,4.389899,7.635310,-0.471127,5.926654,9.845058,-0.358870,0.204159,-7.579674,-9.857987,-0.669311,0.193090,7.537125,8.454298,-6.665437,4.899518,-9.469188,7.544109,-3.504345,3.467177,-1.209417,-4.111538,8.030712,7.296037,0.150391,-8.665875,4.287777,-2.885769,9.234523,4.763957,-2.220577,7.460397,2.562418,-9.668445,6.359044,0.274322,4.512384,-2.218129,-8.245607,-0.604979,0.963825,1.435947,2.959568,4.119243,4.853009,-1.952228,4.131232,-1.022289,-5.738548,6.568947,-7.724100,-3.438723,-0.975038,-7.856431,-5.793079,-8.271981,-8.843497,-2.634301,-7.853038,-0.954309,-6.031974,6.709233,1.117552,-2.303055,-1.806097,8.863244,1.689305,-7.370150,-0.261326,-4.836787,-2.799565,9.811524,-9.848182,-7.921117,3.424643,-1.042308,1.016790,-3.775784,2.506965,6.706504,-1.161505,6.903815,-8.599465,3.450524,-2.673984,9.238618,-4.598061,0.710525,4.766784,9.181348,7.652848,-2.793405,3.060676,1.265868,-6.351298,1.277743,1.588268,-3.993179,-6.193299,-9.896262,2.340469,3.904077,-8.958452,-3.058456,-6.504149,2.386975,8.742853,2.162524,-5.632212,9.510538,8.495366,2.391389,3.085970,-3.156242,4.752089,5.276029,-0.530282,-1.267414,8.271540,-7.830952,5.219499,5.302586,-4.928684,2.824978,2.016925,4.431045,0.363824,7.560906,-8.070703,7.348477,2.176945,-4.624646,2.859779,-3.455231,4.279509,2.753260,-6.315059,6.756363,8.711444,0.614948,5.329876,7.661175,7.567170,-3.914272,-8.120301,9.075717,-7.063223,6.743780,5.326028,-3.459506,6.094091,3.924460,7.773118,-8.682522,3.919060,1.503633,-3.350819,-0.721725,-8.049972,5.461906,-3.897851,-2.705147,-6.834398,-7.492718,4.288877,-7.929468,-5.060266,1.523234,-3.080707,-2.922045,1.752745,-1.756453,-7.958720,-1.811553,0.497846,2.495086,-2.054605,-5.955952,-9.083947,-4.066306,-5.269981,-9.484228,-1.588019,-2.529928,2.625245,7.375300,-2.897674,-8.585288,-7.515165,1.028608,-5.162543,9.621225,-8.603404,1.431047,-8.315641,5.009979,-2.525828,-4.802652,2.170629,9.233517,4.200341,1.727653,-6.437205,5.772401,-8.016181,9.093934,4.348204,-5.175236,-8.040004,-5.107700,2.717328,3.056940,6.608957,0.946236,-2.427152,2.888517,9.593473,-4.406437,-8.694827,-8.111206,-5.885801,9.377507,-9.008541,-3.300439,7.121970,2.657300,-7.012695,-3.558727,-4.017922,-0.920997,-1.387808,4.833916,-4.554673,-6.275218,7.864966,-6.236973,-8.207144,1.363844,9.513374,4.828188,4.821740,6.246632,-3.272218,2.408591,6.777888,1.199421,-3.098655,4.713947,-8.084967,0.715470,-7.077941,-5.421940,-1.827472,3.612609,7.373799,-8.113202,-7.739359,-3.244011,-5.799907,6.386426,2.042952,3.569303,8.335380,-3.478904,-4.020258,5.156353,1.304927,6.383537,-5.381331,3.631652,-0.765350,-9.885762,-8.049664,1.414291,-4.286709,-2.459536,7.815223,9.381560,4.703046,4.559626,-5.689912,-0.260630,-5.088758,5.008263,3.687302,-0.982758,-6.951531,-1.582128,5.369158,5.332862,-5.781845,4.034183,-5.937464,2.922039,-6.541396,5.489135,9.970633,7.067826,-1.697666,-3.079238,3.437092,5.000880,8.395234,-6.750327,4.932210,8.949115,-9.669317,0.610887,4.586281,-1.405461,1.163561,-9.591475,1.271431,-2.018553,-5.459267,0.946245,6.189524,-4.635440,-1.994808,2.165516,-1.462730,-6.550543,3.033940,9.276734,-0.103123,9.041212,-9.136037,-6.912330,2.415119,8.568255,-1.034150,2.667651,2.613815,-3.664973,8.520908,6.190692,-4.429494,-3.051435,3.546416,5.058444,2.532077,-3.909861,-5.592780,4.330927,4.170801,-9.328104,-2.299535,-6.841779,1.518557,4.150133,-9.202446,-1.767736,-4.165527,7.948257,8.112705,0.555776,7.491422,-5.668639,0.635906,0.940566,-5.100070,-7.808296,2.582474,-0.022641,1.226421,1.411208,-0.054624,4.359058,-6.087017,-4.922025,7.820024,-6.221151,2.348960,-6.736758,3.470227,-4.204327,0.612937,-1.431060,4.556721,5.413280,-6.429090,-5.161302,5.865810,-7.224253,-2.307894,6.628728,-6.348123,-0.659647,-8.982600,-1.589393,-2.899078,0.389262,2.476948,1.335664,-5.528464,-8.955726,9.531917,2.775816,-5.850059,3.327639,-7.293256,-9.183790,-3.531898,8.484306,1.035087,-9.760856,-0.691089,-6.526134,3.942129,-6.356943,-9.180601,5.847021,7.702616,-4.412251,-4.877276,7.534296,-4.910926,4.081374,-3.708377,8.170550,1.803126,-2.929118,5.604219,2.831608,-1.318661,-4.077206,-3.051613,-5.579772,-4.041650,6.708849,-6.621637,-3.710449,-8.898358,-2.529528,-6.580556,8.983124,4.343834,5.012184,-9.988438,-7.141557,-1.979994,1.724620,-9.140373,-6.389781,6.926535,6.950461,-0.162164,-0.314578,2.838406,-8.111487,6.486973,2.512495,9.287580,0.841751,-8.560621,-5.896057,5.967558,9.853264,9.653232,-2.878013,-0.668947,1.288587,4.380490,1.593708,-3.757855,-8.049868,0.517270,-5.036325,-3.294908,-1.497115,7.354510,3.290151,1.448050,-4.015892,7.277812,8.751387,-2.286344,-7.575842,-4.849454,8.260689,3.170852,-9.643706,6.223708,1.475700,8.614055,-3.322294,-7.766092,5.017303,5.540379,0.603818,-6.797653,-7.370273,4.989045,4.744129,-2.638810,-8.492576,-7.566031,5.411098,6.205226,-9.111435,-0.261838,-5.647907,-0.040952,-9.227794,9.679279,-2.862691,-8.082590,5.803619,-5.276541,-3.367276,8.173378,-9.415281,5.344223,4.734562],[5.754690,0.854938,6.752538,-4.460808,1.848452,4.867740,-1.913226,6.827657,-9.304237,-3.651972,9.403512,7.693901,8.214332,-7.868116,8.754645,-2.817660,9.385773,6.386329,8.915753,5.304285,-7.412086,2.793876,-7.007366,-9.258586,0.980932,7.588760,9.822852,3.994674,6.872455,8.680949,-9.402880,3.894339,-9.095925,-7.643756,-1.594958,-6.338156,-3.300187,-9.048034,-9.556346,6.040863,2.720821,-5.984825,3.132183,-9.484468,-5.358088,-0.024402,9.138510,-9.397171,-7.113171,6.037386,-5.774490,8.708480,9.656063,-4.475285,-6.134822,-7.800440,-2.522539,-1.626025,-4.903994,-5.374740,8.655525,8.674968,-7.589912,-6.571118,-9.689664,-9.232895,2.597698,0.092885,6.486393,6.527260,4.413125,0.652300,-4.756488,-1.829741,-0.879877,7.925712,7.274589,-7.252703,0.711734,-7.823390,-1.645066,-8.730522,-4.869616,8.188333,2.682385,-5.915830,-7.182251,3.134934,4.064901,6.656230,-1.035654,4.863610,-2.831743,-0.621484,-5.955554,3.048634,4.862585,9.757818,-8.024252,8.276082,7.395885,-1.124484,0.846422,-8.431581,6.814453,4.647373,5.851779,7.753172,-5.810227,6.731725,-5.412692,-7.659486,-8.542888,-3.213690,-2.996528,3.805254,9.101366,5.881822,6.010746,1.281643,0.772544,-0.993956,-9.369655,-0.982874,4.578545,6.774887,4.885093,8.561474,8.569617,-3.619535,7.961027,9.530730,6.651131,-7.794414,6.977855,-7.828575,-7.431768,1.893628,-5.816931,4.960756,8.465914,-6.362856,-0.567380,-0.511901,0.058886,6.405644,-5.913882,4.930336,9.980181,-1.402228,8.806280,-8.423881,-3.892339,-0.366002,2.723695,-1.748744,4.817223,5.831795,2.677156,8.298468,-7.606980,8.709259,-3.054316,2.692791,-9.117603,-1.564861,-5.610552,6.509338,-1.513993,9.400089,-7.680730,-5.101382,-2.897566,2.870284,9.387240,-1.185481,-8.481859,9.431647,-3.666634,-5.969117,-9.997776,6.371338,2.631560,1.336028,-5.034979,-1.422179,8.158623,-5.860463,-6.009126,6.923072,5.492601,-6.616091,8.723817,-8.777817,-0.605780,4.085398,8.687600,3.178421,5.030491,-9.866312,5.815355,-7.447279,5.526774,4.570111,5.645896,0.600463,-5.210094,-3.565954,0.055960,-9.184419,4.395611,0.752828,-0.261261,-4.235520,8.214020,4.822158,8.132453,3.744178,6.788282,-4.583448,2.958291,0.789457,8.900727,-4.241323,-1.080723,-8.542895,-7.647855,-1.731542,-4.905425,-6.370535,2.462519,6.754808,-7.432191,1.420435,5.569435,-7.615005,9.859485,-1.355739,7.866419,-0.425425,6.787103,3.250738,-2.870577,-3.868029,-5.121396,-3.556302,4.482066,-7.852320,4.487553,5.757870,-6.441360,2.327466,6.797732,-7.711146,-4.902042,-3.779790,-9.735319,6.857869,0.875973,9.191486,0.455619,1.938583,0.466308,-1.085287,9.338282,8.902966,3.374128,6.306206,0.266996,0.902421,-3.916378,8.797103,4.097888,9.263985,4.280357,0.289292,5.449119,1.590190,-8.114738,5.280385,6.123755,8.470364,8.722805,5.293842,8.239366,0.531170,-0.633913,-4.337610,3.883379,-9.460345,-0.262780,1.281457,-2.207504,8.687260,-4.393315,-5.529424,4.984936,-8.838824,-0.199978,2.437311,-4.191681,-2.099378,-3.967272,9.501253,-9.716981,-2.826342,3.825527,-0.919023,-1.532692,-7.085234,-4.872986,-5.700903,0.134102,5.909043,-2.905617,8.031891,7.790825,2.736299,-4.410432,2.788787,-1.423421,6.520635,-8.158239,9.975895,9.260241,8.934488,-3.425069,-4.192321,6.448541,3.137352,-4.479947,-5.203949,-8.501627,0.572982,-5.407577,-5.304089,-6.607432,-2.698888,8.579953,1.781099,-7.271837,2.555034,-5.940888,-4.688806,5.899438,6.211294,-0.391178,3.176740,8.364171,1.517737,2.346526,-7.863593,0.893310,-2.600446,-0.543715,-2.783576,6.047938,5.800458,1.938091,0.418700,-9.368606,-9.072449,-2.501236,7.237312,8.207630,-5.580671,-6.802387,-7.205278,8.780965,1.838194,8.827349,-9.925302,4.383513,-1.326271,5.536100,5.249120,2.607480,-3.280447,1.663456,9.690286,-3.624537,6.898508,6.643915,4.422858,1.742338,-5.686587,-7.390633,7.531390,0.881344,-9.306406,2.358928,-5.241053,3.784056,-9.865193,-1.544386,4.611540,6.447238,-7.840108,2.988931,-3.474318,-2.234290,7.758008,6.803970,-4.176174,-5.303037,-6.968890,-6.126604,-3.366198,2.675995,-9.125610,1.902368,7.011449,-4.146651,0.955713,3.418066,-1.991701,-5.927407,-2.530251,-9.664105,-7.059991,9.269843,-7.203242,3.409705,6.835768,-5.447560,6.838298,-6.606751,-2.938219,-1.274667,-8.511297,5.812322,3.406888,-4.157582,-7.163171,-9.211430,4.620238,3.042384,4.425234,2.787261,7.526281,-4.983671,1.453810,6.192876,0.109779,0.405387,1.881793,3.052205,-1.192385,-4.912239,-4.428089,-7.588478,-1.601852,-2.666662,-0.156416,6.052680,5.906869,-4.353303,-2.390832,-4.407298,4.161547,6.690437,1.195876,5.580846,-8.235601,-4.689602,-0.718225,-1.699923,-1.876838,-3.676975,-8.036131,-5.339485,3.156629,-1.228794,0.101330,-0.593839,-7.859716,1.001274,-2.069471,-8.678616,8.884759,1.271188,3.259124,-8.974580,-9.703197,-6.731016,-2.351865,-6.985900,-9.346087,0.595125,-6.793515,-6.392543,9.701979,-6.007860,5.013527,-5.933152,9.158946,-2.396487,-4.021014,-4.838084,-5.135348,2.010733,6.614898,-8.622798,6.170075,9.095033,5.089796,-1.509610,-1.044557,-7.933088,5.455529,-5.441051,9.499933,2.614632,3.088061,-9.164293,0.164932,2.109022,-3.386049,-6.080861,7.000572,4.468562,2.403034,-6.408707,-0.410195,9.937552,6.931319,-7.886925,5.715416,-3.006627,6.777049,-1.759569,0.462031,2.463028,4.196467,6.250849,-1.373429,-8.035115,-9.381559,9.765971,2.725030,6.682915,-8.836346,9.451791,5.416834,-6.284253,9.460282,1.793974,-9.263790,-8.911610,-2.118245,4.394649,-6.356945,8.433243,-6.712815,5.399129,1.967042,-3.000405,-3.463829,4.903202,-6.305067,-1.232239,-7.729535,-0.711045,-6.730091,3.844680,-3.182407,3.719916,-5.181588,5.367672,8.445028,-7.016960,9.341505,-1.592359,6.570391,-1.665534,-7.486558,2.060766,-3.727994,5.078426,-2.960065,-9.928488,2.227956,4.206288,-4.020750,-8.113799,5.644174,-7.238345,-0.953862,-8.011325,3.045528,8.046038,4.590736,-5.143550,-6.553404,-7.971749,-8.108900,5.575265,4.272104,6.419820,6.846687,1.425489,1.100225,-5.221475,7.345966,4.692066,4.343684,-8.399691,9.670705,-4.934708,-6.544103,-6.061076,6.690835,5.702079,-6.798519,-7.890055,-3.393481,-7.933167,-7.378739,6.575998,4.970593,-0.890306,4.674161,4.090675,0.365483,-4.350033,-8.655661,9.482471,-1.186504,-1.516727,5.389691,7.629935,9.263554,1.116842,-0.041415,6.090484,4.272809,-4.127753,-6.091349,5.921336,6.077041,0.908884,-5.323621,-2.280300,1.358673,2.228656,8.803356,8.216053,-8.920717,-2.519862,4.425255,-3.471973,8.052424,-0.829272,-2.805462,-1.733118,0.625005,-6.722090,-2.587640,5.447350,4.137514,-9.579422,7.390896,8.286906,8.062606,-2.123947,7.151265,1.268634,5.342358,-2.260941,-0.634273,3.284589,1.271264,3.078982,-8.926348,5.571410,-9.003275,6.721055,7.070515,5.007936,-7.105364,-8.412674,4.805658,5.642565,0.501465,-4.461835,-6.513982,9.990564,5.060466,6.480816,3.092521,-0.815851,-8.682994,8.571857,-4.912450,-4.346510,-9.269813,7.794530,8.500372,-9.068139,-2.330705,-4.359139,1.212541,-9.989930,-5.274402,-9.374125,2.733638,7.008846,-5.131784,2.036626,-6.139177,-1.466868,-5.256197,-2.380467,-7.688003,-3.088223,9.022979,7.513275,5.694633,-6.370817,8.765549,2.159053,2.940810,-8.561215,-1.850505,-9.834808,-8.074614,5.453919,-2.596761,-4.862855,3.797552,-2.805828,4.751833,3.549116,8.493603,-0.180030,-5.030789,1.061196,9.959132,-6.291221,-3.542762,-8.980438,6.447945,0.960521,5.872863,-7.722181,7.051599,5.203464,-6.301098,5.709252,-0.865098,-2.500843,6.996352,-6.452866,9.214578,-0.088142,-2.510112,-9.616503,3.957302,7.234829,6.771931,5.212555,-5.753108,5.639109,6.640732,5.978143,4.040452,-1.564930,7.180925,3.981495,3.076075,-0.209975,-7.124754,2.910805,7.691277,-8.855371,-0.756541,2.916134,-6.008313,3.358100,0.795182,-1.361663,-2.011841,6.658286,9.545269,4.028003,0.169182,-8.409695,-0.647394,7.064291,0.962561,3.791532,4.025244,-1.313348,0.784230,7.887672,-9.179187,8.713199,-0.098533,5.183922,6.084664,9.521135,-2.804211,-3.808998,4.049946,-2.765382,0.694429,1.159807,-4.210444,2.093526,3.042690,-9.317309,-0.712183,9.118470,6.824472,-0.732847,5.465402,3.988653,-3.953829,-7.919868,8.232481,-0.324775,-7.951519,5.198305,1.995106,4.421893,0.361160,9.689549,2.965764,-2.923833,9.813017,-9.618646,-6.317846,-7.747528,8.079930,7.731558,-8.293715,-9.989757,6.098806,2.759662,-2.980946,9.314584,1.046785,7.564064,7.253103,6.921097,-5.924682,6.818398,0.770189,1.109067,8.011852,5.357601,-8.354138,-9.162381,2.454369,4.106063,-9.438077,8.772228,7.864423,0.310669,-8.892965,5.544179,-2.843414,-4.145834,-0.104710,-9.270624,-6.612012,8.078501,3.903600,-5.200330,-4.961896,-0.572257,-5.665559,-8.106397,-2.339463,7.790984,-1.813564,-3.349948,3.798272,-4.737443,-4.651726,8.497096,-4.283564,-3.868797,0.478710,-6.151645,-8.720919,-8.323584,-7.474236,-4.367860,-6.003464,3.062635,-6.133269,5.210441,-0.306027,4.597174,0.462546,2.160967,-9.358963,1.374385,-1.233036,8.990078,4.372300,-0.420906,-0.837001,-2.777450,-5.373399,2.096543,4.578174,-4.888685,-4.689964,3.023564,8.070206,4.252720,-3.723139,4.376283,-9.651239,1.920709,-5.010702,4.239852,-0.173711,-6.222616,3.244187,2.713164,-8.640377,2.801304,6.048766,-8.100620,8.423702,-1.484234,2.261786,1.191185,-3.208424,2.677468,-6.018463,7.032404,-7.721913,4.896877,9.017459,4.856017,-1.936860,-0.672512,9.653016,-3.621390,-0.941319,-0.102420,-1.186002,1.829711,-4.836272,-6.533723,2.716935,0.850797,3.075727,-5.064696,4.926311,-5.701793,-8.935616,1.243262,-0.782940,-0.074108,4.550638,-5.330110,-9.675448,-5.646962,-4.865923,0.902451,3.929078,2.649770,9.130308,1.329972,3.573742,4.464239,5.048438,5.826794,-4.201900,-8.677485,-6.607658,-0.533098,6.344218,0.941559,5.912310,7.109783,6.800223,2.323014,-3.493989,5.570776,-3.008825,0.922470,-9.560903,9.704330,2.765612,-2.644000,-2.082688,-3.171763,2.625984,7.611645,8.031550,9.067531,-7.411340,5.658759,-5.259095,-1.498501,2.696988,-0.472237,5.893401,7.366237,5.532362,-6.722158,-0.286642,5.028864,2.873838,-6.946241,-7.950211,5.923649,-4.807078,8.892124,-1.756500,1.130508,-4.554709,5.762145,-3.430813,-6.452239,-9.370483,8.411630,1.210322,-0.760042,-6.208248,0.383643,5.202635,9.729227,-4.188615,-7.388433,-4.501927,-7.038374,7.819511,-5.796268,-8.082286,0.752699,-5.464870,5.745217,-2.814032,-8.062201,-9.215855,9.664718,-3.606126,0.097556,1.709042,2.453837,-9.047100,-0.729112,1.905708,7.189626,7.982169,-3.549141,1.298477,-1.110766,-1.705798,-0.411079,-8.390835,-7.131923,-9.091645,6.931334,4.426076,-1.801105,8.095059,2.652124,1.119192,-5.883565,9.621678,-6.312482,0.253807,-0.298588,3.786045,-2.763879,-6.725445,4.924622,4.789414,6.792503,5.298225,-3.888837,-7.331136,-0.800574,-6.219588,1.678066,3.833214,-7.127795,-6.020257,-6.752700,-1.869966,8.402804,4.541369,7.217344,-5.737366,8.002339,-0.467832,-4.239377,9.722306,8.227020,1.347721,-1.564913,-9.364233,2.645681,0.442005,2.638593,0.162279,4.598400,4.887812,5.149950,3.065588,1.218758,-9.984923,-0.549155,-0.883066,0.076596,-3.835468,5.134833,-4.820527,7.062720,-0.860806,5.373176,-1.176198,4.635779,-7.827303,1.100075,8.928730,8.432651,-9.933648,-1.830480,5.831599,-7.012557,2.836929,9.925509,6.588219,3.865285,8.448203,1.846845,6.247500,9.038215,1.359758,6.560254,9.275091,-0.581353,8.789324,0.471550,-6.635264,-2.301700,1.031300,2.858855,0.823077,-7.800143,-3.937010,-6.962181,-3.610850,2.738143,-3.055928,1.767059,3.504176,1.796186,-3.352953,-2.076605,-4.312534,-6.781335,-8.431628,-6.768971,-9.631984,-4.446048,-4.691929,6.553473,-5.897845,-2.904230,3.291433,-5.393959,8.962151,5.871391,-6.438335,-2.472862,1.972838,-8.433273,8.461377,9.449548,-3.444907,-9.921489,-8.521509,0.478848,-2.995039,2.408768,9.507787,-7.345836,2.706950,-7.313402,5.548216,-0.805057,3.495023,-7.726883,-2.120618,0.913431,0.705853,0.204865,8.096862,-9.159182,0.216920,3.686698,-9.575714,8.876227,-0.011384,2.767395,8.394333,-2.591411,2.741498,9.192623,-7.914392,-8.808886,-4.861450,2.196057,-9.078659,7.740887,8.307938,6.132617,-2.470628,1.924193,-9.069875,6.601951,-8.992802,6.563520,-4.977294,2.422775,5.729081,4.392319,-4.960408,7.841170,-1.829801,-9.076134,1.953023,5.509121,-0.469341,-3.401301,-8.849984,-5.987728,1.321784,-9.697216,-7.659360,-6.554913,6.623308,1.770311,-1.181374,-8.552278,9.364141,-7.668445,-3.489978,3.890594,-4.227107,-2.440370,5.240299,-8.244595,-7.580001,-2.291621,-5.987969,-7.955906,-5.478365,1.587755,-0.176264,-4.423364,-8.257732,-7.955586,-7.581339,-4.088016,-5.456576,1.091263,0.561337,-2.120408,-0.820709,2.496201,-2.673654,-5.021558,6.362645,9.599749,-4.009496,-7.134593,0.364949,7.689529,-3.455128,-3.644752,-3.547250,-8.171080,2.332099,9.139320,7.554895,9.545092,-3.459025,1.416605,2.669664,0.310536,-6.445549,7.973595,1.147020,1.266831,-8.206158,-1.856127,-8.063766,-0.160697,4.736484,9.686233,-5.895148,-6.877033,5.939243,6.986458,0.482139,-4.911330,-4.028305,7.252931,-2.271634,0.103363,-6.488371,-7.178526,-9.497470,6.933657,-4.312005,-5.059826,0.869529,-4.198704,-4.089772,8.617560,-1.269481,6.919313,6.194971,-6.989553,-0.684128,-5.085779,7.149738,5.580178,-9.362353,-1.410714,0.712002,5.484324,8.218346,1.442568,9.457002,8.497138,-1.678990,-5.477985,5.161536,-4.617911,-2.443432,8.058207,5.474454,2.483917,4.940744,-0.271975,6.712371,0.632139,1.794096,-7.426000,5.645389,1.445369,8.927216,-2.646978,-9.059794,-4.659025,5.241180,9.638391,-8.389408,-7.083549,-6.062017,-9.547540,1.119088,-1.777700,0.863972,8.318847,2.017637,-0.127216,7.017620,4.918400,2.009350,-9.548816,3.798329,9.526641,5.056195,5.927808,4.722198,7.706095,7.142224,3.591882,-8.754929,-9.699415,5.040577,-4.100253,3.794217,9.842529,5.214002,2.017289,2.123829,-4.205346,5.664232,-4.900689,-5.919768,6.136269,6.690903,-5.466812,2.870462,3.371967,1.316050,9.009920,-4.751318,-5.134812,5.934067,-6.501967,-8.285424,1.489047,6.369787,-8.906532,9.395485,8.948157,6.804193,-6.391414,-5.374497,4.294415,-5.916388,-8.158356,6.266180,-1.790680,1.046148,9.485638,-1.439493,4.004432,-9.953697,6.637417,4.705453,2.307806,-0.728912,2.085853,6.806681,-7.848995,-4.976272,-3.249438,8.899597,-7.782517,-9.557414,3.382951,-6.510994,-7.826535,-9.050141,-7.479640,-3.307563,-8.882441,1.947014,-0.775363,3.515668,-5.447109,0.689827,7.614774,-1.290128,1.584079,-4.471558,2.256824,8.234064,9.226079,7.460773,3.940422,4.487213,-1.287379,-6.738639,-8.443662,2.358568,4.121832,8.698842,-4.229020,-3.543995,-3.571753,-9.336956,7.664073,8.308021,3.099751,-6.899122,7.381958,3.325752,-1.328377,-8.295201,6.612547,-8.266890,-5.071632,4.388180,0.635035,3.063723,-0.284786,2.421786,8.153103,1.663805,6.725818,-5.647669,2.094015,-3.580357,3.561210,-9.395475,-9.144023,1.674467,5.766768,2.197047,-6.775855,-2.131478,-9.217905,-2.039355,0.695942,9.521808,1.333411,9.926139,3.845250,-5.303150,-4.325513,5.741717,4.656237,4.318560,1.137091,5.203595,7.489836,1.632867,7.031271,-0.717263,3.690211,7.545385,9.205607,4.847937,-5.134814]], dtype = "float32")#candidate|6846|(7, 1521)|const|float32
bop_6847 = relay.mod(uop_6839.astype('float32'), const_6846.astype('float32')) # shape=(7, 1521)
output = relay.Tuple([call_6774,call_6792,var_6793,var_6795,call_6802,const_6803,const_6804,call_6832,bop_6836,bop_6847,])
output2 = relay.Tuple([call_6775,call_6796,var_6793,var_6795,call_6805,const_6803,const_6804,call_6833,bop_6836,bop_6847,])
func_6855 = relay.Function([var_6793,var_6794,var_6795,var_6835,], output)
mod['func_6855'] = func_6855
mod = relay.transform.InferType()(mod)
var_6856 = relay.var("var_6856", dtype = "float64", shape = (252,))#candidate|6856|(252,)|var|float64
var_6857 = relay.var("var_6857", dtype = "int16", shape = (1, 1521))#candidate|6857|(1, 1521)|var|int16
var_6858 = relay.var("var_6858", dtype = "int64", shape = (250,))#candidate|6858|(250,)|var|int64
var_6859 = relay.var("var_6859", dtype = "float32", shape = (11, 1521))#candidate|6859|(11, 1521)|var|float32
output = func_6855(var_6856,var_6857,var_6858,var_6859,)
func_6860 = relay.Function([var_6856,var_6857,var_6858,var_6859,], output)
mutated_mod['func_6860'] = func_6860
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6313_call = mod.get_global_var('func_6313')
func_6314_call = mutated_mod.get_global_var('func_6314')
call_6926 = func_6313_call()
call_6927 = func_6313_call()
output = call_6926
output2 = call_6927
func_6934 = relay.Function([], output)
mod['func_6934'] = func_6934
mod = relay.transform.InferType()(mod)
mutated_mod['func_6934'] = func_6934
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6934_call = mutated_mod.get_global_var('func_6934')
call_6935 = func_6934_call()
output = call_6935
func_6936 = relay.Function([], output)
mutated_mod['func_6936'] = func_6936
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3995_call = mod.get_global_var('func_3995')
func_3996_call = mutated_mod.get_global_var('func_3996')
call_7030 = func_3995_call()
call_7031 = func_3995_call()
output = call_7030
output2 = call_7031
func_7058 = relay.Function([], output)
mod['func_7058'] = func_7058
mod = relay.transform.InferType()(mod)
output = func_7058()
func_7059 = relay.Function([], output)
mutated_mod['func_7059'] = func_7059
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6619_call = mod.get_global_var('func_6619')
func_6621_call = mutated_mod.get_global_var('func_6621')
call_7105 = relay.TupleGetItem(func_6619_call(), 0)
call_7106 = relay.TupleGetItem(func_6621_call(), 0)
func_3217_call = mod.get_global_var('func_3217')
func_3219_call = mutated_mod.get_global_var('func_3219')
call_7119 = func_3217_call()
call_7120 = func_3217_call()
var_7137 = relay.var("var_7137", dtype = "float64", shape = (9, 2, 2))#candidate|7137|(9, 2, 2)|var|float64
bop_7138 = relay.less_equal(call_7119.astype('bool'), relay.reshape(var_7137.astype('bool'), relay.shape_of(call_7119))) # shape=(9, 2, 2)
bop_7141 = relay.less_equal(call_7120.astype('bool'), relay.reshape(var_7137.astype('bool'), relay.shape_of(call_7120))) # shape=(9, 2, 2)
func_2145_call = mod.get_global_var('func_2145')
func_2147_call = mutated_mod.get_global_var('func_2147')
call_7142 = relay.TupleGetItem(func_2145_call(), 1)
call_7143 = relay.TupleGetItem(func_2147_call(), 1)
output = relay.Tuple([call_7105,bop_7138,call_7142,])
output2 = relay.Tuple([call_7106,bop_7141,call_7143,])
func_7144 = relay.Function([var_7137,], output)
mod['func_7144'] = func_7144
mod = relay.transform.InferType()(mod)
var_7145 = relay.var("var_7145", dtype = "float64", shape = (9, 2, 2))#candidate|7145|(9, 2, 2)|var|float64
output = func_7144(var_7145)
func_7146 = relay.Function([var_7145], output)
mutated_mod['func_7146'] = func_7146
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3930_call = mod.get_global_var('func_3930')
func_3932_call = mutated_mod.get_global_var('func_3932')
call_7150 = func_3930_call()
call_7151 = func_3930_call()
output = relay.Tuple([call_7150,])
output2 = relay.Tuple([call_7151,])
func_7160 = relay.Function([], output)
mod['func_7160'] = func_7160
mod = relay.transform.InferType()(mod)
output = func_7160()
func_7161 = relay.Function([], output)
mutated_mod['func_7161'] = func_7161
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4218_call = mod.get_global_var('func_4218')
func_4220_call = mutated_mod.get_global_var('func_4220')
call_7162 = func_4218_call()
call_7163 = func_4218_call()
output = relay.Tuple([call_7162,])
output2 = relay.Tuple([call_7163,])
func_7169 = relay.Function([], output)
mod['func_7169'] = func_7169
mod = relay.transform.InferType()(mod)
mutated_mod['func_7169'] = func_7169
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7169_call = mutated_mod.get_global_var('func_7169')
call_7170 = func_7169_call()
output = call_7170
func_7171 = relay.Function([], output)
mutated_mod['func_7171'] = func_7171
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5778_call = mod.get_global_var('func_5778')
func_5779_call = mutated_mod.get_global_var('func_5779')
call_7175 = relay.TupleGetItem(func_5778_call(), 0)
call_7176 = relay.TupleGetItem(func_5779_call(), 0)
func_2275_call = mod.get_global_var('func_2275')
func_2276_call = mutated_mod.get_global_var('func_2276')
call_7187 = func_2275_call()
call_7188 = func_2275_call()
func_2393_call = mod.get_global_var('func_2393')
func_2395_call = mutated_mod.get_global_var('func_2395')
call_7191 = relay.TupleGetItem(func_2393_call(), 0)
call_7192 = relay.TupleGetItem(func_2395_call(), 0)
output = relay.Tuple([call_7175,call_7187,call_7191,])
output2 = relay.Tuple([call_7176,call_7188,call_7192,])
func_7198 = relay.Function([], output)
mod['func_7198'] = func_7198
mod = relay.transform.InferType()(mod)
mutated_mod['func_7198'] = func_7198
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7198_call = mutated_mod.get_global_var('func_7198')
call_7199 = func_7198_call()
output = call_7199
func_7200 = relay.Function([], output)
mutated_mod['func_7200'] = func_7200
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4876_call = mod.get_global_var('func_4876')
func_4878_call = mutated_mod.get_global_var('func_4878')
call_7219 = relay.TupleGetItem(func_4876_call(), 7)
call_7220 = relay.TupleGetItem(func_4878_call(), 7)
func_3258_call = mod.get_global_var('func_3258')
func_3259_call = mutated_mod.get_global_var('func_3259')
call_7221 = relay.TupleGetItem(func_3258_call(), 0)
call_7222 = relay.TupleGetItem(func_3259_call(), 0)
func_3638_call = mod.get_global_var('func_3638')
func_3640_call = mutated_mod.get_global_var('func_3640')
var_7227 = relay.var("var_7227", dtype = "int8", shape = (40,))#candidate|7227|(40,)|var|int8
call_7226 = relay.TupleGetItem(func_3638_call(relay.reshape(var_7227.astype('int8'), [2, 20])), 3)
call_7228 = relay.TupleGetItem(func_3640_call(relay.reshape(var_7227.astype('int8'), [2, 20])), 3)
uop_7251 = relay.atanh(call_7226.astype('float32')) # shape=(9, 2, 2)
uop_7253 = relay.atanh(call_7228.astype('float32')) # shape=(9, 2, 2)
func_3382_call = mod.get_global_var('func_3382')
func_3385_call = mutated_mod.get_global_var('func_3385')
const_7267 = relay.const([9.523943,0.950850,-2.455279,0.648896,-7.756884,6.486670,5.822813,2.839861,3.756804,9.208398,-6.612416,-2.570503,-2.925899,8.036561,-6.729444,-3.138159,4.565282,6.861785,5.112169,-4.309651,9.464707,-3.041673,-1.566867,1.842507,-6.618707,-0.033560,-2.790186,0.103865,-4.997898,-4.699903,7.481337,-3.097867,3.618064,0.644712,6.027946,-7.678646,1.563634,4.047931,9.907975,-5.528892,9.358644,-9.070711,6.419776,-1.609916,-4.879380,-6.711614,5.804381,-8.012012,4.097248,3.627494,2.519720,5.742262,-7.723132,-8.657325,-3.502928,-3.470573,-7.017447,6.830652,-2.485216,4.551848,-4.453286,-6.422398,-1.081157,-5.254309,-1.792572,-6.817405,-4.865574,6.124856,-3.688678,-6.680128,-1.921952,-2.997098,4.377734,-8.557409,6.192851,-3.315037,5.278751,7.581185,3.335925,7.017937,6.148731,8.588462,-2.929556,0.298720,3.775731,0.677552,-6.697044,-1.629972,8.057520,5.601874,-4.062503,-6.157343,-0.978983,8.645926,-8.637614,-4.777501,4.259939,2.327160,-4.454954,-5.673663,-3.400827,8.228024,-7.780479,-1.429158,-3.167797,-2.951759,2.131423,-0.380088,5.142590,7.787412,5.868576,6.229146,6.334283,-0.616496,7.570596,2.270153,-8.833249,-1.063217,-6.889531,-5.059351,-0.510852,5.122365,1.736257,-1.368866,-6.661886,-9.446679,6.073674,-8.993607,-9.749147,-4.364624,2.859414,4.371840,-5.611524,-9.812265,-0.710922,4.416069,-6.100052,-8.789647,-5.623411,-4.899269,-8.696302,-2.621683,-5.658826,4.504164,6.119698,1.742414,1.140601,-0.926472,-9.736032,7.001465,4.692300,-3.432890,1.483010,-9.066457,6.473715,-4.894450,3.371928,6.967279,7.073815,8.349207,-8.974683,-6.011119,5.576083,5.974420,4.483484,4.017401,1.837799,-7.249617,-4.811638,-3.139686,5.837574,-9.648379,-9.519613,3.169258,-4.171525,-9.333721,2.792505,-1.294268,-0.132327,-0.472977,-5.970328,-5.689781,5.431634,2.099112,8.714563,5.753944,-5.354024,-0.303702,7.065797,2.094091,-9.057848,-3.630248,-3.061483,-1.483302,-3.958130,-5.988526,-4.080628,-1.282478,-4.311083,-5.017875,-1.351854,-6.078495,7.567389,0.507581,-2.213536,-9.995968,-2.105206,-5.287605,9.728246,2.323632,-1.010742,8.745180,0.039298,-7.115381,8.961378,0.610891,5.676661,-8.571561,-7.152423,6.113393,-7.617612,5.168582,1.874826,3.044530,8.533397,-4.410672,8.636610,-5.197045,-9.139281,-2.165606,4.626436,8.141064,3.426062,3.637327,5.912189,4.792821,-7.099954,-0.900491,-0.262904,1.144510,8.500421,0.779171,8.063125,1.561907,0.671622,0.713935,5.332158,8.760531,-6.258807,2.198428,3.117631,-6.205555,9.529669,3.240995,-3.157194,6.515578,1.185006,-1.813726,1.395727,-3.658446,7.835186,7.273931,-3.219835,-2.973931,-5.734345,-8.979599,-0.193836,2.232637,1.836285,9.924891,0.404567,1.948303,-2.207088,4.367234,3.496611,-5.596935,1.637687,-2.044377,-4.084426,6.246722,-1.763741,-2.873755,-0.230724,-3.625455,8.220560,4.783568,2.826860,5.352529,8.013186,2.075774,-4.312927,2.849732,8.648215,8.299485,-1.017550,-5.813527,-0.618118,8.682389,2.033786,-1.202557,-9.257656,7.371539,8.795128,5.342196,-7.586384,7.759436,-6.412111,-3.268579,-7.884357,3.938148,-8.778815,9.754640,-6.021427,5.781300,7.323682,-4.826325,-6.766342,5.907137,-6.088149,-7.572722,2.149710,9.098545,-7.558404,7.677726,5.286317,-5.265097,6.832153,-6.104803,-8.242766,1.887708,-4.540255,1.208902,3.103654,-1.076080,5.953730,-9.890937,-6.147673,-3.580260,-7.600506,-4.193479,-5.501839,0.122381,-4.522495,-3.282331,-3.929107,-3.907517,5.396664,6.710764,-6.549887,0.727368,-2.822848,-4.212032,3.546200,3.659135,2.962861,-9.520947,-5.068907,2.578113,5.122699,-9.086813,6.212517,-4.376061,-6.473420,9.458673,1.841527,6.099154,9.025882,1.437583,-6.126465,-0.560272,-0.828682,-1.706043,-6.652288,2.212818,3.295364,2.168087,6.113591,8.580905,7.254582,-0.178654,3.386103,-5.173087,-9.723305,-8.610460,9.195538,-5.968361,4.380483,-3.800424,-1.409703,3.899728,9.224391,-1.186389,8.413599,7.122326,-4.764347,1.903136,0.098366,-5.884923,3.504775,-7.304961,1.971367,-6.688406,6.364163,1.286018,8.231068,0.277846,0.960196,4.881916,-0.750373,-1.116658,-6.657829,-3.137497,6.272112,0.183225,7.825490,2.192125,-8.256237,9.042411,7.904878,2.638045,-9.716157,1.753860,-2.667971,-1.961476,7.996662,-4.769177,-7.551367,4.005604,6.401230,5.586393,7.915578,-1.989838,-3.359532,7.092329,-5.545150,-1.443433,-1.331770,-6.090822,-3.839374,2.645524,2.188960,-0.678036,-7.852494,-7.936259,-3.113947,8.344643,-4.043353,-4.254671,9.573104,-4.801430,-1.586814,-0.790422,2.970379,-7.431381,3.092681,4.281286,5.926108,7.114063,-9.515952,4.099559,0.377184,-2.578367,-2.639032,-0.577770,-4.173971,1.110412,-9.428684,5.029679,8.975799,6.078257,0.712083,6.787773,-3.023497,8.863357,-6.819312,-8.801252,2.500061,-6.531144,2.077840,0.894762,3.208629,-6.539968,0.567461,0.569193,5.659930,8.077451,-8.178711,7.437359,2.162970,4.858034,-0.973902,8.363355,-5.445454,9.132591,9.893829,9.885280,-7.172957,-0.215797,-1.619817,-9.909912,-1.246943,-4.576483,-7.301628,-1.940746,-3.365746,-7.517167,8.923263,-1.807107,9.239680,7.172974,6.630930,0.422077,-3.941865,3.079154,-3.919837,0.794804,4.165482,3.658393,8.562661,-6.278415,9.335927,-5.343227,-9.503333,-8.799069,2.413780,-8.891525,-7.288364,-4.272297,4.187757,0.650828,8.206492,3.900704,6.255215,-8.820650,-1.572947,-3.208937,1.593675,-8.624177,-4.761567,0.592747,-1.123774,-3.050261,-2.360198,0.975419,-0.255691,5.668553,3.398123,-4.553761,0.532850,-5.549724,4.974953,3.542405,7.913981,0.382445,-0.927174,9.924717,-5.589955,2.347546,-8.497491,8.347698,-2.576284,-4.757635,6.438784,-6.072384,-6.460205,-2.356512,1.966250,-7.299845,7.003733,-3.214756,0.333870,-3.024153,6.880438,-2.059624,-0.465063,-3.342848,-4.415695,4.376604,-1.536494,-1.327680,-2.275671,-9.944914,-1.604447,-4.085354,-8.065967,5.216620,7.422219,-5.861215,5.351866,-7.486322,-9.723495,-9.321280,-2.890890,-2.814140,0.095645,3.723934,6.415672,-3.098770,-8.322535,7.754042,8.446154,-9.382055,-0.845109,-3.354214,5.489834,4.418455,0.024748,-6.195035,5.502145,-6.618621,6.685451,-9.138186,-9.020177,-6.818725,-9.671374,6.991957,-7.520284,-9.768394,-2.830771,6.926189,6.713404,0.781754,-1.246507,-0.504791,-7.826519,3.142353,-0.194019,-4.107558,-0.855298,-7.789412,-3.162199,-2.460088,9.764077,6.274338,6.389136,-4.972879,-2.504542,-3.601093,1.050955,-9.160743,8.499771,-4.860662,-3.561614,-3.657734,9.086089,1.643215,7.479833,3.204327,-7.862282,-7.515918,0.801430,-7.591836,8.147469,-4.115575,-0.618681,-8.723452,-0.890655,8.361736,-2.278018,7.433122,-4.188005,8.670152,9.955183,5.157236,-1.723924,0.272208,-1.282320,5.025063,-5.199059,-7.315509,-8.957846,5.586636,2.518922,6.616136,-5.504048,-9.048324,0.094119,-3.804934,-7.938153,-6.656297,-4.481236,-7.088256,-8.425502,-0.652445,0.554389,5.738142,5.843194,0.553984,1.172551,-6.096772,7.770142,6.183517,7.117506,1.728146,2.368192,-1.819459,-8.263315,-1.095815,-8.133586,3.762305,8.641050,9.007315,9.590239,-1.597300,-3.583359,3.705596,9.540776,-9.690643,-4.442924,-7.462267,-3.751607,2.142777,0.324125,6.276051,-5.031079,4.930645,6.408947,2.023391,6.413248,5.773675,-3.405192,-8.973489,0.102475,-0.066357,-9.170547,8.509023,8.489665,4.878546,-8.294058,-6.733032,-3.312061,8.539772,7.583277,-4.068490,-4.261893,-9.054466,-1.715488,-7.115588,2.060706,-3.198390,5.249299,-4.964624,-7.718769,4.440751,-3.627382,-7.515264,2.955218,-9.012399,-6.874276,-8.122053,4.548984,4.096917,6.544658,9.642122,5.245353,-7.022776,-0.426537,1.970729,9.892447,2.083234,1.303264,-8.048799,9.735066,6.354934,1.980183,-2.490698,-1.094414,3.276548,6.539053,-7.749449,-9.364972,5.268758,-4.839513,2.421686,8.127594,9.621898,-5.764276,-2.452577,2.187535,9.300353,8.556610,2.954827,-8.237308,9.649926,4.345586,-8.763151,-0.744533,-1.555543,-0.314234,-6.788810,5.425407,-9.600299,3.844710,7.175585,-7.268334,-9.828862,8.114848,8.858792,-2.735117,6.320270,1.721916,1.360225,-8.229688,-8.343932,4.525501,-1.994471,-4.219325,5.812198,9.824268,-0.725067,9.698700,1.096930,-7.093352,-4.879153,3.698105,5.621599,6.081535,7.005626,-3.069202,0.316150,-4.182068,-0.968633,-8.931814,2.566312,5.777457,-7.446488,-7.456662,5.670638,-7.405454,0.618116,6.182630,-2.781502,4.440375,-5.024375,0.099791,8.806369,-0.683434,3.891005,4.283647,-6.733552,-0.311621,-9.280780,1.709680,-2.835692,1.442857,6.406113,-2.062713,-0.868733,2.985814,5.799300,-6.606835,3.829282,3.219752,5.431508,5.304953,1.840277,-6.076138,-1.593445,0.041985,-2.309779,-0.792720,7.680461,0.656013,-5.112912,9.926701,-0.658463,-5.714871,-4.098518,-3.968849,8.270087,5.799854,3.604119,-2.264048,9.743274,-1.069019,-4.133275,-3.779957,0.304598,7.434215,-4.876143,-2.817938,-7.107465,-0.570965,-3.423224,4.536171,-8.220196,-1.462910,-2.243073,3.768730,-9.671354,3.065764,-2.113082,-7.938046,-9.971800,8.265308,-7.883492,9.056644,9.698921,8.115146,-0.152782,8.480121,-8.903149,-8.329513,-5.783163,-4.815824,-0.367210,4.132920,0.605859,-8.005998,-1.265814,2.903808,5.915769,2.931939,-8.525752,-1.717435,1.411222,-4.097944,1.654889,0.859499,-5.740511,-1.944517,0.747375,-5.247639,-5.856242,-3.223920,-3.466390,0.199857,-3.759497,-9.679889,-1.456662,3.613871,-2.550079,6.466689,0.356643,4.196833,-3.709883,-3.571086,-3.466407,6.386094,5.697736,2.505441,8.873079,-8.651374,0.063429,-6.311793,8.033661,-6.028325,8.909968,-9.692098,-0.751767,2.523910,7.864659,-7.408760,-7.057011,-2.329898,-5.174094,9.711612,0.144235,8.060312,4.043869,-7.910269,-6.707948,-5.787564,-1.174223,-5.598945,9.846133,3.503260,5.564554,-8.597241,6.964620,9.366283,-9.556246,7.103806,-7.925351,-1.280801,4.806880,0.077824,9.048352,4.052214,-2.550322,-9.963151,8.313315,-4.037233,-8.363693,-4.353830,-0.389114,6.875706,7.031500,-7.161090,1.002113,8.496878,7.462140,-6.214815,-5.207041,-8.263021,2.805840,-1.840398,-2.821601,2.016999,5.050431,2.460877,-6.018665,-8.981465,3.954455,3.540442,-8.217155,2.550007,5.852594,-3.716407,-8.254887,-8.850676,-2.127127,-5.358925,-5.064878,8.353148,-5.994977,9.576533,3.520312,-3.474799,-5.564598,8.669739,-2.417868,-4.414867,1.846403,1.411932,2.382776,1.237389,8.462113,-1.279473,-8.820894,7.313763,-2.531230,2.343221,3.382901,3.509743,8.805892,-0.726156,7.475340,-7.479071,2.380889,-8.044743,3.805474,-4.455247,-7.295344,-1.407431,-7.121269,6.054609,-2.915694,-3.551533,-7.965027,0.015585,0.526841,6.932979,-2.714514,2.428970,5.040919,-5.471235,6.940265,0.304756,-5.611228,-9.072831,-8.359281,9.749559,-6.670202,-7.958020,6.230356,0.020501,3.867722,-7.893716,-6.903818,7.379275,1.873508,-7.128587,8.868963,-3.145933,-6.841181,-8.311163,-9.259376,5.845707,-8.889402,6.488798,-5.385011,-5.725253,0.946148,7.253742,-7.594987,-1.327114,2.796587,-6.438711,-8.934464,-5.443614,-1.561347,3.692389,-1.221483,1.143442,-2.615400,8.054668,0.376855,-2.697068,-3.974370,-0.651379,5.746924,-6.838882,-4.161818,4.880114,-3.005911,7.606963,-5.392806,6.686804,2.869039,2.736258,-8.196999,-4.811230,-3.060575,-9.126114,5.734797,0.080197,6.240971,9.415271,1.298770,7.151374,-8.200021,-4.955960,9.622658,4.379471,-2.125239,6.386803,0.522905,3.774247,-8.888232,-6.632702,-3.942065,-4.664835,-3.128714,1.997078,-0.023592,8.079661,7.533261,-2.379710,7.874358,-6.670050,-5.788768,-3.329677,9.985676,-6.071622,-3.621360,6.357671,-0.623627,-8.639725,2.675328,-9.866230,-7.506470,-7.548952,2.238559,8.354272,1.875365,3.745304,7.417007,9.574889,2.122420,-6.753686,6.362626,-7.335476,-8.654475,-8.890724,8.012086,4.240349,-3.486178,6.580753,-5.040263,-7.270716,-3.982364,-2.220963,-8.478524,9.470486,9.926711,3.750543,4.986827,-2.664570,-1.954148,-8.152465,-0.355420,-4.022138,9.252005,-3.248004,-8.649455,7.477659,-6.393077,-0.837644,-0.621642,-1.927362,9.203514,-6.876553,-4.175174,-4.594265,6.641149,-8.398326,1.815857,-3.232565,-1.247330,-5.456406,5.661798,-5.078578,5.377429,-9.741176,-5.437549,3.594727,-1.921685,-3.687004,4.951796,-7.048975,7.031622,-8.523053,5.885497,-7.983840,3.065500,-1.242955,-7.567384,3.704089,3.581785,6.532019,-8.458190,0.814830,-6.933435,6.624482,2.474785,-9.862850,-8.900492,0.725327,3.047044,-0.222598,-0.473949,-6.032070,8.917770,5.428889,6.275799,-2.037984,7.336643,3.779369,0.944651,7.638342,-4.772164,-9.284158,-5.557118,-0.992912,5.389506,5.311107,1.240995,-4.051324,4.041613,4.926036,4.614605,-0.988769,5.169140,-9.513916,5.769792,7.451244,-7.825546,-0.963446,1.983836,-4.517370,4.318425,0.782473,6.000482,6.398291,7.269155,-8.463545,-8.112388,1.342706,-8.974143,2.577984,-9.847103,8.497318,-3.775403,3.891182,-3.764360,-4.348130,6.063554,-1.463069,6.674177,7.016049,-9.992101,0.058273,3.262201,-6.036894,9.392899,1.053366,2.441820,-8.928017,-9.232457,5.525694,3.013915,5.964013,5.263418,-9.408648,8.370723,5.995070,9.627220,2.851077,-0.043068,-0.350877,7.890476,0.449093,-0.518220,-2.196792,9.491046,2.687716,5.327453,-2.778858,-3.602246,7.436555,-8.711817,9.592131,-4.654659,-7.826180,-4.908684,-4.629571,-3.619233,-2.307924,1.127624,-3.906390,6.938823,1.719373,-7.895403,5.659271,-4.757868,-0.797170,-9.071521,-4.241771,-0.477874,7.500344,8.561990,-6.216650,4.796966,-0.488628,9.879680,9.482045,-4.697163,5.611176,-5.617496,8.257813,-3.984349,-3.978158,3.759419,1.798749,7.510959,2.908375,-0.920265,0.584796,-2.318381,-2.254575,-3.350629,-7.970454,-0.352470,0.728599,5.918436,-2.461252,-5.689394,-1.470419,3.709050,-9.548331,-9.370893,-0.730503,8.754360,-5.291585,5.486348,-2.061652,-2.541697,3.870815,-2.551690,-2.602374,9.686668,0.293491,6.956875,-0.727965,7.088208,9.070854,-8.135451,-0.724564,1.093560,6.046067,4.484062,-2.698350,0.673041,3.317767,-4.486749,7.827221,-1.566209,-3.096980,-0.416914,-9.010411,4.511510,5.112663,3.185272,1.586562,-3.378119,-2.165176,-3.995425,5.090851,-1.414316,-6.106905,-4.570756,-3.484535,-0.786041,-4.044798,7.037251,7.332724,2.631724,-1.323116,-5.112630,6.156208,4.877166,6.595818,4.748882,2.516220,4.645176,-2.374264,1.053900,-2.869133,5.196929,-4.033197,1.293237,9.593014,-3.662152,-6.580592,-0.954765,5.534501,0.933265,5.915395,4.226003,-0.305793,-4.311162,8.368151,1.879225,-2.699282,-4.260037,-4.850862,-1.375453,-2.573726,8.204254,1.668790,5.566586,6.122618,6.640508,3.752869,8.397876,9.595818,-6.279028,4.938588,-8.873948,7.492504,-9.127408,5.248740,1.126176,9.882353,-2.813366,-0.426827,8.726367,-8.755711,5.775676,-1.038508,5.696819,-1.647119,-9.613857,7.127612,3.574786,7.406785,-6.656684,-9.483554,8.892197,6.575333,9.719915,9.163700,0.726411,4.706106,7.329961,-0.905496,-0.447381,-3.001070,-8.271721,5.323687,-1.114196,-3.126808,2.253095,9.377907,-5.865294,-6.647130,-1.939148,4.771186,2.881187,-8.820091,-5.375892,1.083068,-5.374776,1.330984,-2.207652,-6.888257,5.389823,1.967272,-5.370472,1.623516,1.996839,-1.787198,0.949897,-2.420851,-6.674022,8.250694,3.675184,2.129667,2.810505,-4.363045,-4.635344,-6.887149,9.534483,-2.113055,-7.357906,3.963802,-3.576033,-0.103050,1.834413,-2.615631,7.449339,-2.784822,8.355284,-5.813146,-1.449099,-2.971746,-9.770405,-6.975229,-4.342054,3.146912,9.137074,5.870665,-3.534051,6.708486,-5.065013,1.700032,-1.573448,-6.104219,-3.324891,-0.270354,2.944447,6.569298,8.336518,-8.982547,-2.890860,9.027136,-0.404127,0.060688,-7.786902,-8.406553,9.803952,-8.751233,4.632063,5.251462,-2.989838,-2.997309,-4.067968,1.767574,3.278963,4.249341,3.932953,1.873303,3.859401,-9.249538,-3.105990,-9.079895,-0.784394,7.610905,7.058640,6.471090,-8.923975,-4.596159,3.776277,-8.550014,4.674375,6.737809,-1.114419,-6.885410,3.035610,6.395120,0.997979,3.740346,2.861189,9.063102,0.999416,-5.271925,-5.819191,-4.513636,-6.864840,-7.600505,0.607016,-5.600453,0.742779,9.879838,5.605845,-6.488784,8.341388,-9.854146,-3.476829,4.992585,5.629239,8.815090,-9.995787,2.243387,-8.414107,-1.743100,5.113872,-9.952610,3.440166,-4.191306,-1.153641,4.003365,-9.055773,-4.584498,5.048992,5.837032,3.529581,-9.209834,-8.109460], dtype = "float32")#candidate|7267|(1620,)|const|float32
call_7266 = relay.TupleGetItem(func_3382_call(relay.reshape(const_7267.astype('float32'), [9, 15, 12])), 1)
call_7268 = relay.TupleGetItem(func_3385_call(relay.reshape(const_7267.astype('float32'), [9, 15, 12])), 1)
var_7284 = relay.var("var_7284", dtype = "float32", shape = (9, 2, 2))#candidate|7284|(9, 2, 2)|var|float32
bop_7285 = relay.subtract(uop_7251.astype('uint64'), relay.reshape(var_7284.astype('uint64'), relay.shape_of(uop_7251))) # shape=(9, 2, 2)
bop_7288 = relay.subtract(uop_7253.astype('uint64'), relay.reshape(var_7284.astype('uint64'), relay.shape_of(uop_7253))) # shape=(9, 2, 2)
func_6934_call = mod.get_global_var('func_6934')
func_6936_call = mutated_mod.get_global_var('func_6936')
call_7296 = func_6934_call()
call_7297 = func_6934_call()
var_7316 = relay.var("var_7316", dtype = "uint64", shape = (9, 2, 2))#candidate|7316|(9, 2, 2)|var|uint64
bop_7317 = relay.bitwise_or(bop_7285.astype('int16'), relay.reshape(var_7316.astype('int16'), relay.shape_of(bop_7285))) # shape=(9, 2, 2)
bop_7320 = relay.bitwise_or(bop_7288.astype('int16'), relay.reshape(var_7316.astype('int16'), relay.shape_of(bop_7288))) # shape=(9, 2, 2)
func_3930_call = mod.get_global_var('func_3930')
func_3932_call = mutated_mod.get_global_var('func_3932')
call_7321 = func_3930_call()
call_7322 = func_3930_call()
output = relay.Tuple([call_7219,call_7221,var_7227,call_7266,const_7267,call_7296,bop_7317,call_7321,])
output2 = relay.Tuple([call_7220,call_7222,var_7227,call_7268,const_7267,call_7297,bop_7320,call_7322,])
func_7338 = relay.Function([var_7227,var_7284,var_7316,], output)
mod['func_7338'] = func_7338
mod = relay.transform.InferType()(mod)
var_7339 = relay.var("var_7339", dtype = "int8", shape = (40,))#candidate|7339|(40,)|var|int8
var_7340 = relay.var("var_7340", dtype = "float32", shape = (9, 2, 2))#candidate|7340|(9, 2, 2)|var|float32
var_7341 = relay.var("var_7341", dtype = "uint64", shape = (9, 2, 2))#candidate|7341|(9, 2, 2)|var|uint64
output = func_7338(var_7339,var_7340,var_7341,)
func_7342 = relay.Function([var_7339,var_7340,var_7341,], output)
mutated_mod['func_7342'] = func_7342
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6934_call = mod.get_global_var('func_6934')
func_6936_call = mutated_mod.get_global_var('func_6936')
call_7346 = func_6934_call()
call_7347 = func_6934_call()
func_5778_call = mod.get_global_var('func_5778')
func_5779_call = mutated_mod.get_global_var('func_5779')
call_7354 = relay.TupleGetItem(func_5778_call(), 1)
call_7355 = relay.TupleGetItem(func_5779_call(), 1)
output = relay.Tuple([call_7346,call_7354,])
output2 = relay.Tuple([call_7347,call_7355,])
func_7369 = relay.Function([], output)
mod['func_7369'] = func_7369
mod = relay.transform.InferType()(mod)
mutated_mod['func_7369'] = func_7369
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7369_call = mutated_mod.get_global_var('func_7369')
call_7370 = func_7369_call()
output = call_7370
func_7371 = relay.Function([], output)
mutated_mod['func_7371'] = func_7371
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5608_call = mod.get_global_var('func_5608')
func_5609_call = mutated_mod.get_global_var('func_5609')
call_7387 = func_5608_call()
call_7388 = func_5608_call()
output = call_7387
output2 = call_7388
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
func_6010_call = mod.get_global_var('func_6010')
func_6011_call = mutated_mod.get_global_var('func_6011')
call_7445 = func_6010_call()
call_7446 = func_6010_call()
output = relay.Tuple([call_7445,])
output2 = relay.Tuple([call_7446,])
func_7451 = relay.Function([], output)
mod['func_7451'] = func_7451
mod = relay.transform.InferType()(mod)
mutated_mod['func_7451'] = func_7451
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7451_call = mutated_mod.get_global_var('func_7451')
call_7452 = func_7451_call()
output = call_7452
func_7453 = relay.Function([], output)
mutated_mod['func_7453'] = func_7453
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5778_call = mod.get_global_var('func_5778')
func_5779_call = mutated_mod.get_global_var('func_5779')
call_7506 = relay.TupleGetItem(func_5778_call(), 1)
call_7507 = relay.TupleGetItem(func_5779_call(), 1)
func_5457_call = mod.get_global_var('func_5457')
func_5459_call = mutated_mod.get_global_var('func_5459')
call_7508 = func_5457_call()
call_7509 = func_5457_call()
output = relay.Tuple([call_7506,call_7508,])
output2 = relay.Tuple([call_7507,call_7509,])
func_7512 = relay.Function([], output)
mod['func_7512'] = func_7512
mod = relay.transform.InferType()(mod)
mutated_mod['func_7512'] = func_7512
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7512_call = mutated_mod.get_global_var('func_7512')
call_7513 = func_7512_call()
output = call_7513
func_7514 = relay.Function([], output)
mutated_mod['func_7514'] = func_7514
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2226_call = mod.get_global_var('func_2226')
func_2227_call = mutated_mod.get_global_var('func_2227')
call_7521 = func_2226_call()
call_7522 = func_2226_call()
var_7571 = relay.var("var_7571", dtype = "uint16", shape = (9, 2, 2))#candidate|7571|(9, 2, 2)|var|uint16
bop_7572 = relay.power(call_7521.astype('float32'), relay.reshape(var_7571.astype('float32'), relay.shape_of(call_7521))) # shape=(9, 2, 2)
bop_7575 = relay.power(call_7522.astype('float32'), relay.reshape(var_7571.astype('float32'), relay.shape_of(call_7522))) # shape=(9, 2, 2)
func_3059_call = mod.get_global_var('func_3059')
func_3062_call = mutated_mod.get_global_var('func_3062')
const_7589 = relay.const(9, dtype = "uint32")#candidate|7589|()|const|uint32
var_7590 = relay.var("var_7590", dtype = "uint32", shape = (540,))#candidate|7590|(540,)|var|uint32
call_7588 = relay.TupleGetItem(func_3059_call(relay.reshape(const_7589.astype('uint32'), []), relay.reshape(var_7590.astype('uint32'), [6, 10, 9]), ), 0)
call_7591 = relay.TupleGetItem(func_3062_call(relay.reshape(const_7589.astype('uint32'), []), relay.reshape(var_7590.astype('uint32'), [6, 10, 9]), ), 0)
output = relay.Tuple([bop_7572,call_7588,const_7589,var_7590,])
output2 = relay.Tuple([bop_7575,call_7591,const_7589,var_7590,])
func_7592 = relay.Function([var_7571,var_7590,], output)
mod['func_7592'] = func_7592
mod = relay.transform.InferType()(mod)
mutated_mod['func_7592'] = func_7592
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7592_call = mutated_mod.get_global_var('func_7592')
var_7594 = relay.var("var_7594", dtype = "uint16", shape = (9, 2, 2))#candidate|7594|(9, 2, 2)|var|uint16
var_7595 = relay.var("var_7595", dtype = "uint32", shape = (540,))#candidate|7595|(540,)|var|uint32
call_7593 = func_7592_call(var_7594,var_7595,)
output = call_7593
func_7596 = relay.Function([var_7594,var_7595,], output)
mutated_mod['func_7596'] = func_7596
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4218_call = mod.get_global_var('func_4218')
func_4220_call = mutated_mod.get_global_var('func_4220')
call_7699 = func_4218_call()
call_7700 = func_4218_call()
func_2909_call = mod.get_global_var('func_2909')
func_2912_call = mutated_mod.get_global_var('func_2912')
var_7704 = relay.var("var_7704", dtype = "float64", shape = (252,))#candidate|7704|(252,)|var|float64
var_7705 = relay.var("var_7705", dtype = "int64", shape = (250,))#candidate|7705|(250,)|var|int64
call_7703 = relay.TupleGetItem(func_2909_call(relay.reshape(var_7704.astype('float64'), [6, 42]), relay.reshape(var_7705.astype('int64'), [25, 10]), ), 5)
call_7706 = relay.TupleGetItem(func_2912_call(relay.reshape(var_7704.astype('float64'), [6, 42]), relay.reshape(var_7705.astype('int64'), [25, 10]), ), 5)
output = relay.Tuple([call_7699,call_7703,var_7704,var_7705,])
output2 = relay.Tuple([call_7700,call_7706,var_7704,var_7705,])
func_7707 = relay.Function([var_7704,var_7705,], output)
mod['func_7707'] = func_7707
mod = relay.transform.InferType()(mod)
var_7708 = relay.var("var_7708", dtype = "float64", shape = (252,))#candidate|7708|(252,)|var|float64
var_7709 = relay.var("var_7709", dtype = "int64", shape = (250,))#candidate|7709|(250,)|var|int64
output = func_7707(var_7708,var_7709,)
func_7710 = relay.Function([var_7708,var_7709,], output)
mutated_mod['func_7710'] = func_7710
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6143_call = mod.get_global_var('func_6143')
func_6144_call = mutated_mod.get_global_var('func_6144')
call_7721 = relay.TupleGetItem(func_6143_call(), 0)
call_7722 = relay.TupleGetItem(func_6144_call(), 0)
uop_7745 = relay.sigmoid(call_7721.astype('float32')) # shape=(9, 2, 2)
uop_7747 = relay.sigmoid(call_7722.astype('float32')) # shape=(9, 2, 2)
output = relay.Tuple([uop_7745,])
output2 = relay.Tuple([uop_7747,])
func_7753 = relay.Function([], output)
mod['func_7753'] = func_7753
mod = relay.transform.InferType()(mod)
output = func_7753()
func_7754 = relay.Function([], output)
mutated_mod['func_7754'] = func_7754
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2486_call = mod.get_global_var('func_2486')
func_2487_call = mutated_mod.get_global_var('func_2487')
call_7798 = func_2486_call()
call_7799 = func_2486_call()
output = relay.Tuple([call_7798,])
output2 = relay.Tuple([call_7799,])
func_7819 = relay.Function([], output)
mod['func_7819'] = func_7819
mod = relay.transform.InferType()(mod)
output = func_7819()
func_7820 = relay.Function([], output)
mutated_mod['func_7820'] = func_7820
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5457_call = mod.get_global_var('func_5457')
func_5459_call = mutated_mod.get_global_var('func_5459')
call_7879 = func_5457_call()
call_7880 = func_5457_call()
output = relay.Tuple([call_7879,])
output2 = relay.Tuple([call_7880,])
func_7893 = relay.Function([], output)
mod['func_7893'] = func_7893
mod = relay.transform.InferType()(mod)
mutated_mod['func_7893'] = func_7893
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7893_call = mutated_mod.get_global_var('func_7893')
call_7894 = func_7893_call()
output = call_7894
func_7895 = relay.Function([], output)
mutated_mod['func_7895'] = func_7895
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7898 = relay.var("var_7898", dtype = "float64", shape = (12, 14, 7))#candidate|7898|(12, 14, 7)|var|float64
uop_7899 = relay.sqrt(var_7898.astype('float64')) # shape=(12, 14, 7)
output = uop_7899
output2 = uop_7899
func_7918 = relay.Function([var_7898,], output)
mod['func_7918'] = func_7918
mod = relay.transform.InferType()(mod)
mutated_mod['func_7918'] = func_7918
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7919 = relay.var("var_7919", dtype = "float64", shape = (12, 14, 7))#candidate|7919|(12, 14, 7)|var|float64
func_7918_call = mutated_mod.get_global_var('func_7918')
call_7920 = func_7918_call(var_7919)
output = call_7920
func_7921 = relay.Function([var_7919], output)
mutated_mod['func_7921'] = func_7921
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2316_call = mod.get_global_var('func_2316')
func_2317_call = mutated_mod.get_global_var('func_2317')
call_7981 = relay.TupleGetItem(func_2316_call(), 0)
call_7982 = relay.TupleGetItem(func_2317_call(), 0)
func_7338_call = mod.get_global_var('func_7338')
func_7342_call = mutated_mod.get_global_var('func_7342')
var_7990 = relay.var("var_7990", dtype = "int8", shape = (10, 4))#candidate|7990|(10, 4)|var|int8
const_7991 = relay.const([[-3.883643],[8.898528],[3.475191],[4.428421],[-3.885235],[-5.915938],[-6.229710],[8.247553],[5.066630],[2.526290],[-0.386677],[4.289852],[3.645605],[-9.643390],[1.543385],[-5.752087],[-5.215051],[0.207107],[1.880527],[8.693345],[-6.806734],[1.562859],[-0.458936],[8.467636],[4.807584],[1.145121],[-8.193938],[-2.151858],[3.678623],[-2.079204],[9.803712],[7.977000],[-4.801620],[8.913033],[3.615121],[4.453117]], dtype = "float32")#candidate|7991|(36, 1)|const|float32
call_7989 = relay.TupleGetItem(func_7338_call(relay.reshape(var_7990.astype('int8'), [40,]), relay.reshape(const_7991.astype('float32'), [9, 2, 2]), relay.reshape(const_7991.astype('uint64'), [9, 2, 2]), ), 6)
call_7992 = relay.TupleGetItem(func_7342_call(relay.reshape(var_7990.astype('int8'), [40,]), relay.reshape(const_7991.astype('float32'), [9, 2, 2]), relay.reshape(const_7991.astype('uint64'), [9, 2, 2]), ), 6)
output = relay.Tuple([call_7981,call_7989,var_7990,const_7991,])
output2 = relay.Tuple([call_7982,call_7992,var_7990,const_7991,])
func_8006 = relay.Function([var_7990,], output)
mod['func_8006'] = func_8006
mod = relay.transform.InferType()(mod)
var_8007 = relay.var("var_8007", dtype = "int8", shape = (10, 4))#candidate|8007|(10, 4)|var|int8
output = func_8006(var_8007)
func_8008 = relay.Function([var_8007], output)
mutated_mod['func_8008'] = func_8008
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2201_call = mod.get_global_var('func_2201')
func_2203_call = mutated_mod.get_global_var('func_2203')
call_8042 = relay.TupleGetItem(func_2201_call(), 0)
call_8043 = relay.TupleGetItem(func_2203_call(), 0)
output = call_8042
output2 = call_8043
func_8052 = relay.Function([], output)
mod['func_8052'] = func_8052
mod = relay.transform.InferType()(mod)
mutated_mod['func_8052'] = func_8052
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8052_call = mutated_mod.get_global_var('func_8052')
call_8053 = func_8052_call()
output = call_8053
func_8054 = relay.Function([], output)
mutated_mod['func_8054'] = func_8054
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8097 = relay.var("var_8097", dtype = "uint64", shape = (3, 3, 1))#candidate|8097|(3, 3, 1)|var|uint64
var_8098 = relay.var("var_8098", dtype = "uint64", shape = (3, 3, 14))#candidate|8098|(3, 3, 14)|var|uint64
bop_8099 = relay.equal(var_8097.astype('bool'), var_8098.astype('bool')) # shape=(3, 3, 14)
output = bop_8099
output2 = bop_8099
func_8129 = relay.Function([var_8097,var_8098,], output)
mod['func_8129'] = func_8129
mod = relay.transform.InferType()(mod)
mutated_mod['func_8129'] = func_8129
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8129_call = mutated_mod.get_global_var('func_8129')
var_8131 = relay.var("var_8131", dtype = "uint64", shape = (3, 3, 1))#candidate|8131|(3, 3, 1)|var|uint64
var_8132 = relay.var("var_8132", dtype = "uint64", shape = (3, 3, 14))#candidate|8132|(3, 3, 14)|var|uint64
call_8130 = func_8129_call(var_8131,var_8132,)
output = call_8130
func_8133 = relay.Function([var_8131,var_8132,], output)
mutated_mod['func_8133'] = func_8133
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4876_call = mod.get_global_var('func_4876')
func_4878_call = mutated_mod.get_global_var('func_4878')
call_8142 = relay.TupleGetItem(func_4876_call(), 10)
call_8143 = relay.TupleGetItem(func_4878_call(), 10)
func_2178_call = mod.get_global_var('func_2178')
func_2181_call = mutated_mod.get_global_var('func_2181')
var_8166 = relay.var("var_8166", dtype = "int16", shape = (1, 180))#candidate|8166|(1, 180)|var|int16
call_8165 = relay.TupleGetItem(func_2178_call(relay.reshape(var_8166.astype('int16'), [30, 6])), 2)
call_8167 = relay.TupleGetItem(func_2181_call(relay.reshape(var_8166.astype('int16'), [30, 6])), 2)
func_8129_call = mod.get_global_var('func_8129')
func_8133_call = mutated_mod.get_global_var('func_8133')
const_8174 = relay.const([-8,-3,-9,-3,-8,-1,-10,-9,-1], dtype = "uint64")#candidate|8174|(9,)|const|uint64
const_8175 = relay.const([10,-7,-3,-1,7,-10,-3,7,2,2,-10,-6,-5,-9,7,-10,-2,-10,-5,-1,1,1,-4,7,-8,-7,-1,-1,10,-3,-10,4,1,-6,4,-9,9,-10,-8,-9,5,-7,1,-3,7,-7,-8,-10,-4,-5,4,-5,6,7,2,2,-4,-6,-6,7,4,2,-5,-2,9,-1,-1,-9,2,1,-4,3,-2,4,-7,-3,4,-4,-10,-2,-4,-3,7,-2,-7,-5,5,-2,1,7,8,-1,-7,-3,-1,-5,6,-10,7,-6,-4,-7,2,-8,-5,1,4,6,-4,8,4,10,1,-6,1,-5,4,-6,3,-7,8,4,9,5,10,9], dtype = "uint64")#candidate|8175|(126,)|const|uint64
call_8173 = func_8129_call(relay.reshape(const_8174.astype('uint64'), [3, 3, 1]), relay.reshape(const_8175.astype('uint64'), [3, 3, 14]), )
call_8176 = func_8129_call(relay.reshape(const_8174.astype('uint64'), [3, 3, 1]), relay.reshape(const_8175.astype('uint64'), [3, 3, 14]), )
func_7058_call = mod.get_global_var('func_7058')
func_7059_call = mutated_mod.get_global_var('func_7059')
call_8181 = func_7058_call()
call_8182 = func_7058_call()
output = relay.Tuple([call_8142,call_8165,var_8166,call_8173,const_8174,const_8175,call_8181,])
output2 = relay.Tuple([call_8143,call_8167,var_8166,call_8176,const_8174,const_8175,call_8182,])
func_8192 = relay.Function([var_8166,], output)
mod['func_8192'] = func_8192
mod = relay.transform.InferType()(mod)
mutated_mod['func_8192'] = func_8192
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8193 = relay.var("var_8193", dtype = "int16", shape = (1, 180))#candidate|8193|(1, 180)|var|int16
func_8192_call = mutated_mod.get_global_var('func_8192')
call_8194 = func_8192_call(var_8193)
output = call_8194
func_8195 = relay.Function([var_8193], output)
mutated_mod['func_8195'] = func_8195
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8282 = relay.var("var_8282", dtype = "int32", shape = ())#candidate|8282|()|var|int32
var_8283 = relay.var("var_8283", dtype = "int32", shape = (16, 4, 2))#candidate|8283|(16, 4, 2)|var|int32
bop_8284 = relay.not_equal(var_8282.astype('bool'), var_8283.astype('bool')) # shape=(16, 4, 2)
func_3829_call = mod.get_global_var('func_3829')
func_3831_call = mutated_mod.get_global_var('func_3831')
const_8324 = relay.const([4.201294,2.759081,1.484436,2.850869,-1.047231,2.825087,-2.906190,4.743017,9.406678,4.519283,-7.333577,5.102182,-9.392765,-1.048939,6.647220,-1.967761,0.659973,-6.290818,-1.687824,-6.069468,3.053188,-8.993326,-8.135525,8.541889,9.142853,2.199280,-2.490718,-6.720523,1.382158,7.076034,1.694565,1.320208,9.997334,1.266789,3.873241,2.648611], dtype = "float64")#candidate|8324|(36,)|const|float64
call_8323 = relay.TupleGetItem(func_3829_call(relay.reshape(const_8324.astype('float64'), [9, 2, 2])), 3)
call_8325 = relay.TupleGetItem(func_3831_call(relay.reshape(const_8324.astype('float64'), [9, 2, 2])), 3)
func_2702_call = mod.get_global_var('func_2702')
func_2703_call = mutated_mod.get_global_var('func_2703')
call_8326 = relay.TupleGetItem(func_2702_call(), 2)
call_8327 = relay.TupleGetItem(func_2703_call(), 2)
func_2304_call = mod.get_global_var('func_2304')
func_2306_call = mutated_mod.get_global_var('func_2306')
call_8341 = relay.TupleGetItem(func_2304_call(), 0)
call_8342 = relay.TupleGetItem(func_2306_call(), 0)
func_3650_call = mod.get_global_var('func_3650')
func_3652_call = mutated_mod.get_global_var('func_3652')
call_8348 = func_3650_call()
call_8349 = func_3650_call()
func_6399_call = mod.get_global_var('func_6399')
func_6403_call = mutated_mod.get_global_var('func_6403')
var_8354 = relay.var("var_8354", dtype = "int32", shape = (1144,))#candidate|8354|(1144,)|var|int32
const_8355 = relay.const([5,8,-10,5,8,-6,-9,3,-2,-5,-8,-3,10,7,1,9,-9,-6,-9,1,-8,4,-3,-7,4,2,-8,5,4,4,-9,3,-1,-8,-2,8,8,-7,9,-6], dtype = "int8")#candidate|8355|(40,)|const|int8
const_8356 = relay.const([6,-4,5,-2,-5,-3,-10,-9,-7,-7,-1,8,-6,4,-1,9,-8,8,-4,6,9,10,-8,-8,-10,-9,-2,10,4,-1,5,-2,-4,10,-9,7,-8,9,-8,8,-2,10,3,-3,4,-2,3,-3,4,-4,10,1,10,3,-7,-5,-9,4,-5,-1,-2,-7,6,-1,-5,-3,8,-2,-6,-8,5,3,-8,-6,-7,-1,9,-3,8,-7,-10,-8,8,1,-5,8,-2,-6,1,5,-10,-6,-2,5,-2,-3,-7,-5,8,-1,-4,-7,-4,-9,6,3,-10,-4,-8,2,-3,4,-3,5,4,-8,-6,7,9,-5,9,2,6,2,7,4,1,10,-9,-9,2,3,4,8,-5,-10,-10,4,10,-10,1,7,-1,8,-3,-3,4,-4,6,-4,4,5,-8,-2,4,3,5,7,-8,-6,-2,7,6,6,5,3,6,5,-7,-2,8,-6,7,9,-2,8,5,-2,1,5,10,5,-7,1,9,5,-9,2,-6,-5,5,2,1,3,4,7,-5,3,5,4,-7,5,1,4,-6,6,4,-3,4,8,3,5,8,-10,1,-10,4,-6,3,-2,1,-2,8,10,3,-3,3,-4,7,5,7,-6,-1,6,2,-2,-8,8,2,-9,5,-1,1,9,-9,-3,10,-9,-2,4,3,-9,-10,8,-4,-7,8,-7,-3,-6,-1,-9,10,1,-3,8,-10,-8,1,-4,-2,3,-9,10,7,4,-4,-8,-1,6,5,-1,-8,-7,4,3,-2,-5,-9,3,-10,5,-2,-6,-3,6,-4,-2,5,-3,-9,-6,-5,4,-7,-1,5,-8,-10,-9,-9,-10,1,7,-1,6,7,3,-2,-5,5,5,3,-9,10,-7,-3,3,-10,2,3,1,10,3,2,-3,5,9,1,-2,-5,1,-5,-2,9,6,1,-3,3,5,5,2,-3,-7,-10,9,-7,1,-7,6,-6,9,10,-8,-9,8,-10,1,3,2,-10,-9,1,8,3,-7,8,6,-9,3,-9,1,3,-7,-3,-2,-9,-7,-10,-10,3,-2,3,-1,4,10,4,5,5,-4], dtype = "int8")#candidate|8356|(400,)|const|int8
call_8353 = relay.TupleGetItem(func_6399_call(relay.reshape(var_8354.astype('int32'), [1144,]), relay.reshape(const_8355.astype('int8'), [40,]), relay.reshape(const_8356.astype('int8'), [1, 400]), ), 4)
call_8357 = relay.TupleGetItem(func_6403_call(relay.reshape(var_8354.astype('int32'), [1144,]), relay.reshape(const_8355.astype('int8'), [40,]), relay.reshape(const_8356.astype('int8'), [1, 400]), ), 4)
output = relay.Tuple([bop_8284,call_8323,const_8324,call_8326,call_8341,call_8348,call_8353,var_8354,const_8355,const_8356,])
output2 = relay.Tuple([bop_8284,call_8325,const_8324,call_8327,call_8342,call_8349,call_8357,var_8354,const_8355,const_8356,])
func_8366 = relay.Function([var_8282,var_8283,var_8354,], output)
mod['func_8366'] = func_8366
mod = relay.transform.InferType()(mod)
mutated_mod['func_8366'] = func_8366
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8366_call = mutated_mod.get_global_var('func_8366')
var_8368 = relay.var("var_8368", dtype = "int32", shape = ())#candidate|8368|()|var|int32
var_8369 = relay.var("var_8369", dtype = "int32", shape = (16, 4, 2))#candidate|8369|(16, 4, 2)|var|int32
var_8370 = relay.var("var_8370", dtype = "int32", shape = (1144,))#candidate|8370|(1144,)|var|int32
call_8367 = func_8366_call(var_8368,var_8369,var_8370,)
output = call_8367
func_8371 = relay.Function([var_8368,var_8369,var_8370,], output)
mutated_mod['func_8371'] = func_8371
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2993_call = mod.get_global_var('func_2993')
func_2995_call = mutated_mod.get_global_var('func_2995')
call_8400 = relay.TupleGetItem(func_2993_call(), 3)
call_8401 = relay.TupleGetItem(func_2995_call(), 3)
func_6717_call = mod.get_global_var('func_6717')
func_6719_call = mutated_mod.get_global_var('func_6719')
call_8431 = relay.TupleGetItem(func_6717_call(), 0)
call_8432 = relay.TupleGetItem(func_6719_call(), 0)
output = relay.Tuple([call_8400,call_8431,])
output2 = relay.Tuple([call_8401,call_8432,])
func_8440 = relay.Function([], output)
mod['func_8440'] = func_8440
mod = relay.transform.InferType()(mod)
mutated_mod['func_8440'] = func_8440
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8440_call = mutated_mod.get_global_var('func_8440')
call_8441 = func_8440_call()
output = call_8441
func_8442 = relay.Function([], output)
mutated_mod['func_8442'] = func_8442
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3034_call = mod.get_global_var('func_3034')
func_3036_call = mutated_mod.get_global_var('func_3036')
call_8451 = relay.TupleGetItem(func_3034_call(), 0)
call_8452 = relay.TupleGetItem(func_3036_call(), 0)
output = call_8451
output2 = call_8452
func_8458 = relay.Function([], output)
mod['func_8458'] = func_8458
mod = relay.transform.InferType()(mod)
mutated_mod['func_8458'] = func_8458
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8458_call = mutated_mod.get_global_var('func_8458')
call_8459 = func_8458_call()
output = call_8459
func_8460 = relay.Function([], output)
mutated_mod['func_8460'] = func_8460
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4115_call = mod.get_global_var('func_4115')
func_4117_call = mutated_mod.get_global_var('func_4117')
call_8473 = relay.TupleGetItem(func_4115_call(), 0)
call_8474 = relay.TupleGetItem(func_4117_call(), 0)
func_5079_call = mod.get_global_var('func_5079')
func_5080_call = mutated_mod.get_global_var('func_5080')
call_8475 = relay.TupleGetItem(func_5079_call(), 0)
call_8476 = relay.TupleGetItem(func_5080_call(), 0)
func_3961_call = mod.get_global_var('func_3961')
func_3963_call = mutated_mod.get_global_var('func_3963')
call_8483 = func_3961_call()
call_8484 = func_3961_call()
output = relay.Tuple([call_8473,call_8475,call_8483,])
output2 = relay.Tuple([call_8474,call_8476,call_8484,])
func_8491 = relay.Function([], output)
mod['func_8491'] = func_8491
mod = relay.transform.InferType()(mod)
mutated_mod['func_8491'] = func_8491
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8491_call = mutated_mod.get_global_var('func_8491')
call_8492 = func_8491_call()
output = call_8492
func_8493 = relay.Function([], output)
mutated_mod['func_8493'] = func_8493
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8458_call = mod.get_global_var('func_8458')
func_8460_call = mutated_mod.get_global_var('func_8460')
call_8528 = func_8458_call()
call_8529 = func_8458_call()
output = relay.Tuple([call_8528,])
output2 = relay.Tuple([call_8529,])
func_8532 = relay.Function([], output)
mod['func_8532'] = func_8532
mod = relay.transform.InferType()(mod)
output = func_8532()
func_8533 = relay.Function([], output)
mutated_mod['func_8533'] = func_8533
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3217_call = mod.get_global_var('func_3217')
func_3219_call = mutated_mod.get_global_var('func_3219')
call_8539 = func_3217_call()
call_8540 = func_3217_call()
output = call_8539
output2 = call_8540
func_8541 = relay.Function([], output)
mod['func_8541'] = func_8541
mod = relay.transform.InferType()(mod)
mutated_mod['func_8541'] = func_8541
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8541_call = mutated_mod.get_global_var('func_8541')
call_8542 = func_8541_call()
output = call_8542
func_8543 = relay.Function([], output)
mutated_mod['func_8543'] = func_8543
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8585 = relay.var("var_8585", dtype = "float32", shape = (11, 15, 13))#candidate|8585|(11, 15, 13)|var|float32
uop_8586 = relay.rsqrt(var_8585.astype('float32')) # shape=(11, 15, 13)
output = relay.Tuple([uop_8586,])
output2 = relay.Tuple([uop_8586,])
func_8603 = relay.Function([var_8585,], output)
mod['func_8603'] = func_8603
mod = relay.transform.InferType()(mod)
mutated_mod['func_8603'] = func_8603
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8604 = relay.var("var_8604", dtype = "float32", shape = (11, 15, 13))#candidate|8604|(11, 15, 13)|var|float32
func_8603_call = mutated_mod.get_global_var('func_8603')
call_8605 = func_8603_call(var_8604)
output = call_8605
func_8606 = relay.Function([var_8604], output)
mutated_mod['func_8606'] = func_8606
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5010_call = mod.get_global_var('func_5010')
func_5011_call = mutated_mod.get_global_var('func_5011')
call_8693 = relay.TupleGetItem(func_5010_call(), 0)
call_8694 = relay.TupleGetItem(func_5011_call(), 0)
output = call_8693
output2 = call_8694
func_8698 = relay.Function([], output)
mod['func_8698'] = func_8698
mod = relay.transform.InferType()(mod)
output = func_8698()
func_8699 = relay.Function([], output)
mutated_mod['func_8699'] = func_8699
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3034_call = mod.get_global_var('func_3034')
func_3036_call = mutated_mod.get_global_var('func_3036')
call_8731 = relay.TupleGetItem(func_3034_call(), 0)
call_8732 = relay.TupleGetItem(func_3036_call(), 0)
func_4934_call = mod.get_global_var('func_4934')
func_4938_call = mutated_mod.get_global_var('func_4938')
const_8738 = relay.const(9, dtype = "int16")#candidate|8738|()|const|int16
var_8739 = relay.var("var_8739", dtype = "int16", shape = (11,))#candidate|8739|(11,)|var|int16
call_8737 = relay.TupleGetItem(func_4934_call(relay.reshape(const_8738.astype('int16'), []), relay.reshape(var_8739.astype('int16'), [11,]), ), 0)
call_8740 = relay.TupleGetItem(func_4938_call(relay.reshape(const_8738.astype('int16'), []), relay.reshape(var_8739.astype('int16'), [11,]), ), 0)
output = relay.Tuple([call_8731,call_8737,const_8738,var_8739,])
output2 = relay.Tuple([call_8732,call_8740,const_8738,var_8739,])
func_8741 = relay.Function([var_8739,], output)
mod['func_8741'] = func_8741
mod = relay.transform.InferType()(mod)
mutated_mod['func_8741'] = func_8741
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8742 = relay.var("var_8742", dtype = "int16", shape = (11,))#candidate|8742|(11,)|var|int16
func_8741_call = mutated_mod.get_global_var('func_8741')
call_8743 = func_8741_call(var_8742)
output = call_8743
func_8744 = relay.Function([var_8742], output)
mutated_mod['func_8744'] = func_8744
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2562_call = mod.get_global_var('func_2562')
func_2564_call = mutated_mod.get_global_var('func_2564')
call_8820 = func_2562_call()
call_8821 = func_2562_call()
func_2316_call = mod.get_global_var('func_2316')
func_2317_call = mutated_mod.get_global_var('func_2317')
call_8849 = relay.TupleGetItem(func_2316_call(), 0)
call_8850 = relay.TupleGetItem(func_2317_call(), 0)
func_2042_call = mod.get_global_var('func_2042')
func_2044_call = mutated_mod.get_global_var('func_2044')
call_8859 = relay.TupleGetItem(func_2042_call(), 0)
call_8860 = relay.TupleGetItem(func_2044_call(), 0)
uop_8874 = relay.acosh(call_8849.astype('float32')) # shape=(10, 10, 4)
uop_8876 = relay.acosh(call_8850.astype('float32')) # shape=(10, 10, 4)
uop_8887 = relay.cos(uop_8874.astype('float32')) # shape=(10, 10, 4)
uop_8889 = relay.cos(uop_8876.astype('float32')) # shape=(10, 10, 4)
func_7512_call = mod.get_global_var('func_7512')
func_7514_call = mutated_mod.get_global_var('func_7514')
call_8903 = relay.TupleGetItem(func_7512_call(), 1)
call_8904 = relay.TupleGetItem(func_7514_call(), 1)
func_3382_call = mod.get_global_var('func_3382')
func_3385_call = mutated_mod.get_global_var('func_3385')
const_8909 = relay.const([8.986557,-5.093907,9.589550,-7.221115,-6.283571,-4.687853,5.992538,0.583023,9.640369,4.920232,-1.532438,-9.996924,7.201468,6.093570,9.272079,-7.747609,-0.290225,0.313290,8.803357,-4.128960,-2.187852,-7.997993,-6.364071,-8.276961,-3.167465,-0.941529,-5.192363,1.996636,1.575900,-6.213757,-9.778174,1.362818,3.124052,-7.718711,-8.892829,-5.652857,2.189156,-9.208852,9.095700,8.786404,-9.500447,-1.741245,0.472855,-0.203697,7.572441,3.553164,7.158603,-4.772128,-8.679918,-5.658671,1.222045,7.741161,1.162679,-6.137596,1.843809,8.998934,7.763210,-3.087302,8.070530,-0.040463,3.336030,-2.207407,-1.826502,6.464666,-9.306884,-3.866658,9.932139,-2.860698,8.797080,8.740795,0.511057,5.070994,-5.053389,0.435536,-4.925224,-5.523827,8.574195,8.277141,7.186826,-5.189757,-7.014853,6.448442,7.128950,-6.103828,7.954125,5.018279,-8.451780,3.835916,-3.355215,8.249240,-6.020597,-8.814812,-7.020104,-8.012785,-3.265006,4.646981,7.090145,-6.985154,1.328602,2.273854,-6.167588,6.682963,5.361097,-6.961244,6.824198,7.730745,7.182221,5.918816,6.424345,-6.456039,8.735173,-7.495437,-7.321312,1.304093,1.500791,-6.068816,6.927276,7.891920,8.407392,-5.445923,8.132522,-3.764337,7.415680,-7.459961,4.959027,-1.612496,3.266306,3.372970,-8.130848,9.676165,-5.535100,0.243456,1.883258,-0.001505,-1.630452,7.272876,-1.206346,0.499740,4.228328,-8.894119,-3.481727,9.406334,7.498306,2.662676,1.951373,-5.750621,4.867396,2.607970,-1.327242,1.794936,-2.091947,-9.587230,-1.414532,-7.310495,1.555383,6.545119,-3.754341,6.362839,8.485739,8.801393,2.693602,-6.717355,3.654951,1.726710,-1.007714,5.186856,8.905115,4.851277,0.463623,-5.477281,4.102157,-6.464008,-1.549873,2.127940,-5.764227,3.580334,-4.555041,-6.255309,3.480675,1.622756,-6.215979,2.363360,-4.184251,-2.417217,-2.831653,1.650481,-3.014293,6.334702,8.698942,-8.502408,6.424902,-3.357555,-7.611930,-7.227315,-1.303436,8.041338,-9.339306,2.275399,2.415141,-6.215890,-2.476688,5.153600,2.813415,2.705031,-1.519844,-5.764763,8.066649,6.580642,-1.863830,-4.048027,-0.585604,7.382852,-3.270615,6.604249,-2.835598,6.344247,7.104726,1.781623,-8.251184,-4.829257,1.682733,-8.833382,1.467306,-0.338331,6.035913,-7.150577,-9.086949,-0.421091,-1.175988,-0.415616,4.695734,4.254647,4.758747,3.988376,-2.531109,-1.992838,1.072533,-9.165089,-0.542924,-4.702863,4.104821,8.646864,-1.097937,-5.517218,-1.459680,-1.217193,1.886249,-6.452486,-3.298047,-1.964651,1.278548,-4.577127,4.336653,4.088885,0.764010,-4.697870,5.564312,-9.823677,7.147671,-3.376160,-6.205613,-2.354559,3.324013,-7.823807,-3.403209,-5.081832,3.920580,-8.005918,1.565306,-5.838463,7.875322,-1.752908,9.399618,6.010739,6.853865,-5.890563,-3.300557,0.955614,9.536677,7.679549,-8.980236,-4.729795,7.159774,6.307548,-4.098788,8.123142,-0.002665,-5.595196,8.184058,-6.753520,-3.318138,-7.388875,9.706331,-3.594275,7.640054,9.961642,5.970995,2.784317,-0.824496,2.405768,-6.703048,2.887188,-3.280780,-4.089892,3.394210,2.950776,6.290201,-7.542436,8.974820,-2.546535,-7.447415,3.577994,1.975727,-9.456074,4.395292,-0.409853,0.088329,-7.096241,-7.046617,9.784427,2.521339,6.271435,-7.701807,-9.467679,-6.021485,-1.925134,-5.723146,-4.879067,-1.934110,3.765356,-9.460192,9.518096,9.149473,-7.199722,7.585106,1.357360,-4.095231,0.213451,-1.035326,-1.003330,-1.328392,-8.236813,-0.450817,-9.977144,9.274557,-4.484160,-2.664685,5.655239,3.528780,1.936965,0.020474,-6.481481,4.250375,-8.341028,5.761999,-2.431492,0.013647,-6.537100,8.977257,-9.844976,-6.724397,-8.919574,9.136641,5.424916,2.848954,7.916672,7.087077,-7.272673,5.021144,4.845569,-6.681429,0.472900,-4.916373,5.146762,-6.361088,-3.611333,3.853925,5.290609,8.195451,4.442790,7.457631,9.905385,-3.113196,5.457823,4.806531,-1.968125,-0.397976,8.477314,3.082696,-1.908401,0.856777,1.109710,-2.544741,3.653966,7.065633,-4.106298,5.396833,6.883957,-2.846377,4.839097,9.803049,1.318236,4.440541,-5.829305,7.530277,4.309245,-2.811935,1.539476,4.855505,-3.186321,-2.498075,-9.408803,-0.513647,2.276145,-0.498684,-6.054665,7.552580,-2.711083,6.976012,4.728656,4.474842,9.443068,1.945550,-5.661191,1.885247,1.557014,-0.275685,9.770855,-0.632207,1.569833,2.651693,-7.754119,2.135499,-3.568938,-8.405571,4.914974,-4.340231,2.875741,-9.847505,-4.134754,-1.880784,7.414637,2.255613,5.706642,9.579975,7.886567,8.055508,9.103437,-3.980957,1.074322,-3.397562,-0.689583,1.552704,-7.726579,-4.024261,2.944325,0.259600,8.439627,5.269823,-1.043633,3.116135,7.649826,4.635969,1.421122,-4.028652,-7.000219,2.426087,4.349589,-9.755734,-7.868697,9.852363,1.781704,-2.460756,4.283993,-5.383538,0.546390,7.585029,-8.048995,1.682902,-6.037852,-5.928138,-7.750231,-3.940471,-6.271549,-5.993785,1.143594,-4.335794,-9.560672,9.404875,-9.454557,0.086534,2.850711,-8.107902,3.208206,5.516620,-9.395631,1.532697,2.718035,-5.780976,-1.093207,5.020779,-8.805279,7.835081,-0.374897,7.470201,-0.512684,-3.202132,1.441007,6.196281,5.509360,5.196553,-1.879223,-8.756094,-7.956117,2.765624,3.154031,-9.460583,-7.581470,-4.920870,-3.048543,2.459101,-4.566967,-6.900882,-6.497698,4.533151,-0.172829,2.613033,5.477523,-4.156582,1.765149,-4.746235,-1.398069,-7.920720,-7.030340,-8.856464,-8.782915,2.752791,3.247413,0.982649,1.791662,8.334821,6.438821,-5.769457,5.781936,-9.261400,-9.732057,6.126306,9.271402,2.030699,2.424062,-2.958473,2.687003,-2.757951,1.281535,3.208695,-9.121099,-6.347489,7.840277,-2.706066,6.258545,2.994214,-9.808972,2.425671,3.147225,3.638011,-6.113236,-3.662665,-9.578760,-0.739502,-9.936311,-6.483510,6.324615,-7.620604,-9.347649,7.342740,8.452629,8.052672,6.797465,9.127497,-5.094895,5.973386,-9.839271,-4.533525,6.809910,-5.675594,-3.905992,-9.089026,4.929405,7.318544,-8.266913,-4.265887,5.557215,3.922274,-5.175047,1.187313,6.088994,1.934389,9.514886,-7.969053,-8.785451,-9.365739,-6.673939,-9.950209,-1.635849,6.462649,-6.940151,-3.685771,0.586918,2.379780,2.761182,-2.757035,2.197233,-5.533226,-1.041539,6.108342,-3.654118,3.623568,2.279386,-2.621812,3.527787,-0.632558,9.372765,-6.094048,-0.755302,-7.446386,-0.812327,-4.434701,-1.523064,-1.850408,-5.085530,-8.984078,-3.774939,5.403248,6.806080,7.326036,5.329931,0.513076,-1.192210,0.711948,9.424685,-8.113489,3.498222,7.684343,-5.884008,-3.574742,-2.945457,9.216687,-3.398545,-8.594542,-9.432958,8.008703,3.842542,0.165322,-3.693086,-2.550598,-8.983681,1.508800,9.100053,-4.793325,8.264656,-9.477386,4.308568,-9.137520,-7.156944,6.048857,-3.045066,-8.107688,4.813804,3.771732,4.038929,1.387334,2.668160,2.916574,-1.877786,-4.842753,-1.296718,6.749900,-9.687364,3.081609,-3.437943,4.217170,9.808721,-3.134662,8.788800,-0.190599,1.314849,5.236069,0.295005,8.964642,-7.144481,5.774121,0.574419,-4.499319,-5.703103,-4.133670,-9.726264,2.538567,-1.566547,2.311149,5.047589,-5.792087,9.601012,9.654535,-0.747200,-2.326514,-3.443065,0.650944,-0.041502,3.997480,9.377704,2.327520,-6.527069,-7.223676,-7.450964,-3.602485,5.702756,-0.784851,-5.058902,5.075841,9.970481,4.522673,2.234121,2.266900,-1.498333,-8.004581,-3.512387,-4.163494,-3.266315,5.600555,-1.804990,7.195530,-8.782974,-9.198736,9.812443,8.675888,-9.774758,6.304095,1.573243,3.400545,4.910421,-3.669884,-8.456560,-6.988038,4.247454,7.949158,-1.808249,5.101793,4.960844,4.729348,-7.157271,7.600192,-2.791836,-4.704515,6.777635,1.625788,-7.755879,-9.782740,-4.167499,7.046227,2.648391,9.662651,2.937299,-1.758005,0.274331,-2.696117,9.608879,-4.761208,-2.201810,1.267154,-8.214038,-8.280329,-1.075484,6.079463,-0.677697,-4.713131,-0.836977,2.784225,4.504417,-8.111984,4.083849,-3.169337,-8.838995,-4.511678,8.945942,-5.061716,8.975972,-4.010160,2.643989,-8.330226,5.590799,7.214079,1.379527,9.502731,7.081170,9.105544,-6.824746,7.273756,-9.985994,4.080222,7.906152,1.793233,4.571889,0.778306,-5.330544,-9.647654,-6.226363,9.105690,-6.097478,-0.388565,-6.066543,-3.057854,7.918240,2.916691,-9.432489,-6.736468,-6.124649,-2.802527,0.989081,-0.075882,0.163203,0.040208,8.685333,6.738624,-1.265049,6.722335,6.438166,3.871795,8.974709,-6.305670,-5.908060,2.399452,2.635490,-4.168012,1.884680,-6.876170,3.053054,9.088301,-9.101492,-7.660801,-4.375349,0.022184,5.422852,0.238236,4.125390,-8.081506,-5.149240,-1.234169,5.044186,-1.454571,4.365798,-9.970191,8.215215,6.752626,-4.035704,-2.568383,1.669762,1.407957,-2.483949,7.110575,-7.786881,1.581687,-0.368744,-8.792832,-5.500196,-2.791641,3.339027,-9.551046,-3.087754,-8.524442,8.418185,-9.883958,-2.459636,-2.795087,-2.637905,-1.121127,9.147966,2.572015,5.959988,-7.493588,-1.326441,-1.722530,1.967618,-3.930975,-9.793432,-0.232538,8.806063,0.104761,-6.893276,6.985226,0.850834,-0.495696,2.025030,-2.191557,0.452440,8.195259,-7.287045,-5.319930,-2.499181,2.457014,5.300164,8.151890,-9.398792,7.001654,-4.837691,2.678620,-4.029044,-1.061213,0.508243,2.860543,7.727257,8.831582,-4.375964,9.035934,-2.513237,2.864836,1.385569,6.490884,5.771276,-1.399071,6.707964,-4.762264,4.523576,3.398740,4.443811,-7.935081,3.836731,-9.253101,8.127105,0.874108,7.246609,1.595064,3.794514,-4.585561,6.508416,-2.155133,5.257875,9.272843,4.953697,8.400699,8.286416,-6.372365,9.987574,-3.520192,-8.753272,6.647578,-1.258595,-0.831169,8.441424,0.031900,-5.218712,8.695959,-1.239271,-0.167941,6.063654,-0.421643,8.714399,-7.191503,-3.022138,4.483004,-2.729345,-5.875258,-7.437639,-2.719559,5.824579,-6.168367,3.878823,0.042388,-0.124421,8.828458,-0.065163,-1.576523,-7.185657,-2.933249,5.193190,-7.516974,-8.851285,7.993624,4.173064,-1.813135,6.662485,-6.111256,-2.126343,-4.947295,-1.013199,6.105927,8.630780,-6.664829,-3.862200,-6.410121,2.097530,5.727610,3.374715,-2.541525,-0.168722,-8.988118,7.748937,-8.300151,-8.613372,8.196151,-2.851879,3.833827,-7.508680,-9.033675,6.113305,9.424749,7.995897,-6.192172,9.940318,8.354960,-9.117982,2.766015,4.899413,7.215387,-9.988012,-6.573335,7.121489,-5.040861,7.438162,-2.568101,-7.369978,8.153601,-9.484121,-3.497665,-8.201845,1.560671,0.008591,5.942854,-1.968464,9.438059,8.569516,-7.167703,3.718735,-2.211548,4.923928,1.996116,-6.847260,3.371488,7.948077,-3.369436,0.193549,-8.993050,-6.873857,2.899640,-1.282246,5.128985,-8.992134,2.971347,1.247722,1.063203,-8.142743,-4.413077,2.222077,-4.692526,7.692736,2.256385,-9.360720,-4.393013,4.084060,-4.904461,-6.497531,8.541913,9.320310,-7.203191,-1.071614,6.712130,7.685545,-6.791177,7.799258,7.016866,1.470880,4.981084,-8.748486,8.924198,-5.529418,4.306447,0.510189,8.779440,9.657578,3.450569,1.692797,2.010419,-1.673980,-8.627385,-6.772150,9.032396,-9.967152,2.302662,-4.500667,-4.486998,-5.241461,2.582018,-9.857363,-5.982815,-0.771323,9.903879,-4.546057,-5.009029,-1.050976,-6.795425,-7.514478,9.613761,1.601362,5.412195,6.556087,-3.877359,-2.697623,8.934742,-2.394087,-3.490393,-7.203120,1.420063,-8.243582,5.966095,-5.147097,2.168607,3.680827,6.470693,-4.432350,-2.391068,-3.805997,8.502586,-7.144827,6.347721,4.215685,-7.527949,2.990442,-7.304195,2.724341,6.358752,-5.779191,8.964297,8.776389,-9.315326,5.156839,0.963909,1.401124,-7.382041,0.501306,-4.950696,-8.460064,-2.660352,-4.809082,1.862697,1.528958,9.198614,-6.308397,1.504424,5.434797,6.754786,1.086990,-3.446585,4.110591,-4.076884,-7.173529,3.049309,5.279050,5.581730,0.290563,-4.879694,1.034842,-2.586041,-1.554763,8.321871,5.248451,-1.636137,4.411886,5.792330,-1.672875,0.725250,-4.461300,3.265654,5.037275,-6.819451,2.985239,8.681905,-9.680795,-6.725984,3.297962,9.398256,-4.528106,9.986361,-8.614373,8.535285,9.887523,-5.861836,2.349913,8.427819,-6.157473,8.501715,-1.642630,-9.462562,-8.355293,8.458966,-0.835059,-0.779716,3.797875,-6.429891,-9.195806,-3.823257,-8.811572,-2.048378,-5.373209,-2.099815,5.274307,-1.770289,-7.336292,-7.065476,-3.651011,4.396953,-1.990734,0.700141,9.601896,-7.531820,9.105285,1.770414,8.505132,-9.296696,-3.092302,-8.262112,-1.082603,3.251934,2.090727,-3.252834,-6.624245,-7.001357,5.307871,-8.493470,1.746673,7.711571,9.930020,-9.703925,-4.761270,-2.679413,-8.632084,-0.221642,1.602216,8.129020,0.434388,-6.555304,1.194183,7.485009,6.590310,-2.074856,-9.381008,0.544689,-5.769136,-7.134846,-7.838916,8.012099,2.804163,-4.671924,-6.399846,2.152825,4.829196,0.212724,-0.592058,4.867367,-8.217889,-0.440344,1.259784,-9.520458,6.428282,-8.131680,0.984570,-1.762821,1.105372,7.935208,3.278441,-7.984268,3.360126,6.881382,-7.825602,1.270778,-7.698930,2.639045,1.682719,-8.609635,-0.321896,4.070561,-0.927674,-8.900607,-2.686898,6.651025,-8.871419,-5.617092,8.755771,6.275111,-9.980209,-6.838649,-1.004458,3.193763,9.196275,-6.943257,-4.857864,2.472476,-2.791670,5.671599,-9.930241,-1.088804,-2.126557,-5.161163,-4.294957,5.511799,-8.588592,-4.458863,3.991433,-6.849606,1.198196,-9.343751,-2.535316,-7.101546,0.685001,5.122781,5.785158,-7.652228,-4.663126,2.949187,-4.989562,-3.237871,4.860221,8.862703,-0.856754,3.216402,-5.157994,4.798260,-4.613924,9.231700,8.304313,1.621413,-3.798945,-5.622956,-2.978303,-0.404765,-4.971321,6.099761,8.625940,-9.933350,-2.891005,7.145811,7.636533,-7.094552,-4.733620,5.985278,-9.241201,-8.166421,-7.800830,-3.173204,9.193249,5.473315,2.641563,1.428381,9.282872,-8.445211,6.345967,3.787143,-5.871558,-7.286467,6.552435,2.200283,-6.565417,1.179944,-9.963746,6.682871,-6.793140,-2.241126,9.608531,-9.484201,9.134852,0.729051,-4.173132,-0.941362,-0.448785,9.868309,-2.878434,9.805907,3.866175,-2.725088,-2.325184,3.723058,-1.408543,-9.440715,6.561114,0.311427,4.157022,0.994134,4.105851,1.344797,3.231493,9.270796,9.173395,-5.894977,3.073391,-8.826486,6.464160,-9.387050,6.957929,1.951638,2.798940,-2.002971,0.753813,-1.778408,4.691102,-3.289266,7.551125,-3.338575,3.586425,7.385275,6.904601,-0.636553,3.403554,4.737225,-5.686439,4.874761,0.188839,-1.344107,1.416942,1.289307,-2.358702,4.734412,8.930615,-1.210383,0.837392,-0.820398,-5.900152,3.103500,0.683084,-7.663346,1.780613,-6.222549,6.866101,-7.738329,8.492150,8.562340,5.091080,0.192251,2.193615,4.042407,7.559173,4.017933,3.423006,1.037458,8.712906,-5.759443,1.334776,7.653544,5.989755,-5.309639,6.946774,1.029001,-6.196809,-9.204293,-9.401791,-9.339647,5.533741,4.483701,-3.892073,5.627487,7.608296,2.855700,-9.947099,9.960561,-2.788617,6.425094,-0.455694,-9.458257,6.389504,-6.999502,4.158522,-2.155669,-8.982991,1.081312,-9.495373,3.869889,-8.837477,5.982362,1.679931,-2.553251,-9.233997,-7.281725,-9.289817,7.052121,1.472656,-6.319662,4.198934,3.767883,-7.662779,-0.892991,4.731385,-1.383685,-4.693907,9.743556,0.523764,5.705946,0.729779,-7.013192,8.331287,7.033954,3.943045,0.560765,-5.432155,-5.589418,3.032749,-8.431809,-1.980728,-1.235108,-2.775287,4.006580,2.384091,6.108944,-0.188277,7.797811,9.434139,-6.689121,-4.500752,4.938123,-2.832143,2.772043,9.077033,-2.761190,0.052162,-7.233219,-9.819627,6.324708,2.438363,-6.525557,-7.157387,5.264582,4.903554,-1.524079,9.002251,-1.997265,6.515711,5.976417,6.389270,2.242144,-3.343802,-3.272282,3.103537,-0.986897,-3.628564,-3.844382,-6.151893,2.915197,8.224464,0.582441,7.655455,-1.360208,-8.587462,4.889058,2.121708,-5.401905,0.185689,3.647058,-6.707879,3.485675,-3.009594,5.383013,3.389235,-1.702816,-0.221411,6.747563,-1.258861,-0.131809,5.705823,-1.874824,-1.316557,-7.615575,-4.708006,-8.748275,7.902124,0.117499,4.226499,5.345579,4.009510,8.279903,6.465033,-0.328806,-7.784202,-2.250643,-4.478995,3.851386,3.842770,-5.230897,9.101248,-2.085061,-8.384436,-3.893859,-5.016386,-2.143718,-1.458760,4.328583,-1.296275,8.657956,4.605835,-2.374949,-2.282721,-7.638228,3.326573,1.499609,-8.057879,-9.562520,-8.313837,-9.921318,-8.213937,-2.120530,6.381707,-9.859483,6.925555,-9.594048,-9.318485,6.492329,-0.145699,-5.964328,-6.943349,-9.170140,-4.928921,-3.422392,-6.380627,1.073687,2.545789], dtype = "float32")#candidate|8909|(1620,)|const|float32
call_8908 = relay.TupleGetItem(func_3382_call(relay.reshape(const_8909.astype('float32'), [9, 15, 12])), 3)
call_8910 = relay.TupleGetItem(func_3385_call(relay.reshape(const_8909.astype('float32'), [9, 15, 12])), 3)
func_6619_call = mod.get_global_var('func_6619')
func_6621_call = mutated_mod.get_global_var('func_6621')
call_8917 = relay.TupleGetItem(func_6619_call(), 0)
call_8918 = relay.TupleGetItem(func_6621_call(), 0)
func_2316_call = mod.get_global_var('func_2316')
func_2317_call = mutated_mod.get_global_var('func_2317')
call_8921 = relay.TupleGetItem(func_2316_call(), 0)
call_8922 = relay.TupleGetItem(func_2317_call(), 0)
output = relay.Tuple([call_8820,call_8859,uop_8887,call_8903,call_8908,const_8909,call_8917,call_8921,])
output2 = relay.Tuple([call_8821,call_8860,uop_8889,call_8904,call_8910,const_8909,call_8918,call_8922,])
func_8937 = relay.Function([], output)
mod['func_8937'] = func_8937
mod = relay.transform.InferType()(mod)
mutated_mod['func_8937'] = func_8937
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8937_call = mutated_mod.get_global_var('func_8937')
call_8938 = func_8937_call()
output = call_8938
func_8939 = relay.Function([], output)
mutated_mod['func_8939'] = func_8939
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3422_call = mod.get_global_var('func_3422')
func_3424_call = mutated_mod.get_global_var('func_3424')
call_8953 = relay.TupleGetItem(func_3422_call(), 0)
call_8954 = relay.TupleGetItem(func_3424_call(), 0)
output = relay.Tuple([call_8953,])
output2 = relay.Tuple([call_8954,])
func_8973 = relay.Function([], output)
mod['func_8973'] = func_8973
mod = relay.transform.InferType()(mod)
output = func_8973()
func_8974 = relay.Function([], output)
mutated_mod['func_8974'] = func_8974
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9025 = relay.var("var_9025", dtype = "float32", shape = (1, 8, 7))#candidate|9025|(1, 8, 7)|var|float32
uop_9026 = relay.atan(var_9025.astype('float32')) # shape=(1, 8, 7)
func_3638_call = mod.get_global_var('func_3638')
func_3640_call = mutated_mod.get_global_var('func_3640')
const_9032 = relay.const([-10,-4,1,1,3,10,8,-10,-7,-9,-10,4,3,-4,-10,1,-7,-6,8,-4,-3,-6,2,-3,-10,5,3,9,-9,-8,-9,-10,-5,9,-6,-6,-9,-10,-8,-2], dtype = "int8")#candidate|9032|(40,)|const|int8
call_9031 = relay.TupleGetItem(func_3638_call(relay.reshape(const_9032.astype('int8'), [2, 20])), 1)
call_9033 = relay.TupleGetItem(func_3640_call(relay.reshape(const_9032.astype('int8'), [2, 20])), 1)
uop_9036 = relay.sigmoid(call_9031.astype('float64')) # shape=(2, 20)
uop_9038 = relay.sigmoid(call_9033.astype('float64')) # shape=(2, 20)
func_8440_call = mod.get_global_var('func_8440')
func_8442_call = mutated_mod.get_global_var('func_8442')
call_9040 = relay.TupleGetItem(func_8440_call(), 0)
call_9041 = relay.TupleGetItem(func_8442_call(), 0)
output = relay.Tuple([uop_9026,const_9032,uop_9036,call_9040,])
output2 = relay.Tuple([uop_9026,const_9032,uop_9038,call_9041,])
func_9043 = relay.Function([var_9025,], output)
mod['func_9043'] = func_9043
mod = relay.transform.InferType()(mod)
mutated_mod['func_9043'] = func_9043
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9044 = relay.var("var_9044", dtype = "float32", shape = (1, 8, 7))#candidate|9044|(1, 8, 7)|var|float32
func_9043_call = mutated_mod.get_global_var('func_9043')
call_9045 = func_9043_call(var_9044)
output = call_9045
func_9046 = relay.Function([var_9044], output)
mutated_mod['func_9046'] = func_9046
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5375_call = mod.get_global_var('func_5375')
func_5376_call = mutated_mod.get_global_var('func_5376')
call_9048 = relay.TupleGetItem(func_5375_call(), 2)
call_9049 = relay.TupleGetItem(func_5376_call(), 2)
uop_9063 = relay.log2(call_9048.astype('float32')) # shape=(9, 2, 2)
uop_9065 = relay.log2(call_9049.astype('float32')) # shape=(9, 2, 2)
func_2304_call = mod.get_global_var('func_2304')
func_2306_call = mutated_mod.get_global_var('func_2306')
call_9077 = relay.TupleGetItem(func_2304_call(), 0)
call_9078 = relay.TupleGetItem(func_2306_call(), 0)
func_2275_call = mod.get_global_var('func_2275')
func_2276_call = mutated_mod.get_global_var('func_2276')
call_9087 = func_2275_call()
call_9088 = func_2275_call()
uop_9098 = relay.sinh(uop_9063.astype('float64')) # shape=(9, 2, 2)
uop_9100 = relay.sinh(uop_9065.astype('float64')) # shape=(9, 2, 2)
output = relay.Tuple([call_9077,call_9087,uop_9098,])
output2 = relay.Tuple([call_9078,call_9088,uop_9100,])
func_9105 = relay.Function([], output)
mod['func_9105'] = func_9105
mod = relay.transform.InferType()(mod)
mutated_mod['func_9105'] = func_9105
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9105_call = mutated_mod.get_global_var('func_9105')
call_9106 = func_9105_call()
output = call_9106
func_9107 = relay.Function([], output)
mutated_mod['func_9107'] = func_9107
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9127 = relay.var("var_9127", dtype = "float32", shape = (13, 2, 15))#candidate|9127|(13, 2, 15)|var|float32
const_9128 = relay.const([[[-5.138472,6.468747,-9.554678,0.565002,5.512884,-3.016243,7.391711,-9.444544,9.893888,-4.714100,-4.009002,-1.011936,6.797083,0.794205,6.415925],[-8.814953,-1.558916,-0.888986,9.185129,0.508959,-8.554567,-1.321639,-6.701750,2.416742,5.940275,6.117301,-6.596648,-8.092610,6.302503,7.479805]],[[0.616039,-8.089791,1.418411,-3.028179,-8.411103,3.816482,3.484436,-3.225482,0.176169,7.606710,-7.393095,-3.533628,1.140755,-0.445896,-6.340349],[6.883639,3.342360,9.559328,2.850826,4.417142,5.926489,-6.044817,-4.797204,-4.748487,2.269670,-1.433621,0.932383,-0.691681,-4.652284,7.444558]],[[-2.947098,-5.581424,0.472550,0.159952,4.671284,-9.143962,3.755204,4.078038,-7.618427,0.895889,-9.876507,1.858538,-5.876849,-8.745261,-3.026710],[4.931226,-9.205891,-3.957938,-2.506128,-1.417621,-6.445339,-6.525006,-3.658679,-5.858978,-9.108502,-9.376183,3.243828,-4.399071,7.983113,-8.176434]],[[-3.605842,-4.256857,4.433855,-5.189311,-5.677814,4.710242,-4.115740,7.336245,-1.809548,3.455000,9.572555,9.043295,6.120661,0.029705,-1.130374],[-3.978452,2.449709,6.481189,4.140634,-4.100267,1.555018,-3.414824,-8.461481,-8.129299,5.261507,8.803852,0.068887,-4.229277,-7.327881,0.630587]],[[3.799885,8.210919,-9.907648,-7.805777,0.301924,-4.098536,-7.440233,-4.909366,-2.603852,2.216203,-9.031078,-0.052559,7.332342,-1.024153,-7.459957],[-9.022444,8.134431,8.873592,4.107201,5.206968,-7.067084,4.164065,-7.271146,3.338880,-3.251308,1.964232,1.848153,-9.905816,-9.294112,-2.497826]],[[-8.428691,-5.735484,8.751320,0.498585,3.846036,4.601593,-9.978329,9.916025,-6.750778,1.112657,7.743392,8.916596,8.043178,-3.114950,-3.957786],[-9.175901,0.604294,-3.789835,-8.980700,3.099483,-1.380630,-6.660673,5.565760,6.190008,-2.571568,-6.698134,1.126463,0.038956,2.740898,-6.677820]],[[-4.712315,-0.329318,-7.874688,-8.451832,4.603376,-7.315856,-4.692944,-1.529827,-6.667986,6.423095,9.995978,5.885007,4.255654,4.513359,-0.095812],[-5.354011,-3.479177,-7.005612,4.044552,-9.643128,3.434500,-0.026562,9.190264,2.263841,6.444817,-1.420930,9.721915,6.393340,-6.030550,4.671755]],[[3.001967,-6.084526,9.923279,-5.579800,3.923334,4.979672,6.631745,5.783770,-5.412934,6.905872,9.002935,-1.280106,1.238577,-0.714009,-6.290738],[-2.733490,1.059034,-0.792477,3.307991,-8.772172,8.495474,5.450977,9.573651,4.077493,-6.481298,1.968211,-4.598803,-0.629947,-8.013755,-6.862550]],[[-4.825891,-5.405066,7.485133,-4.848951,7.994874,1.269069,-7.496446,6.595178,8.415386,-5.444013,9.702233,-9.412217,7.281524,2.471433,0.796767],[6.340882,-5.184801,6.192613,-9.482629,8.705849,-8.723326,-6.550620,4.430290,2.938475,-1.585706,-2.618065,0.153558,3.796480,5.155872,-6.484106]],[[-9.421933,0.021562,8.771528,-1.217377,-6.722161,5.137665,1.819660,-1.937119,-2.020748,8.207452,6.638050,-7.486356,-5.907100,4.673979,4.061255],[-7.359729,1.684492,-1.870262,5.968124,-7.404097,-3.350789,-2.252374,0.375442,1.344135,-7.350857,-5.114245,-8.265363,1.908647,7.362410,2.891216]],[[-1.762317,-1.404266,2.315012,4.404089,-6.184993,-5.412006,2.723438,-5.882989,6.890289,-5.324932,-2.248638,1.534849,-5.843329,-3.491113,-5.810657],[-0.350050,4.304283,-1.077609,8.885321,8.470348,-3.425887,5.837796,5.140305,-7.248692,7.140149,-1.430612,-9.370793,-3.579851,-8.050480,-3.301011]],[[-5.397934,-2.069927,3.733971,-8.899684,-3.992363,-4.893065,-9.073943,-4.531545,7.247431,-2.957487,-5.259130,4.826353,1.854193,7.900600,-6.294564],[-1.844023,-6.803077,-5.692822,4.839654,-1.979267,0.260366,-5.497418,-1.025993,7.182874,-1.503650,-5.470613,-3.905368,2.660531,-0.730669,-1.477165]],[[-2.544409,2.758170,2.859083,-7.346683,2.665411,-1.435938,-6.494450,-0.562704,1.151036,-8.907564,5.607830,-4.228155,-0.304401,4.753295,-0.390356],[3.704675,-9.364577,3.273182,6.791586,2.587277,9.009561,7.419753,-4.946291,-1.276213,1.270162,6.863591,-4.739783,-5.868797,2.999215,4.311603]]], dtype = "float32")#candidate|9128|(13, 2, 15)|const|float32
bop_9129 = relay.subtract(var_9127.astype('float32'), relay.reshape(const_9128.astype('float32'), relay.shape_of(var_9127))) # shape=(13, 2, 15)
output = bop_9129
output2 = bop_9129
func_9138 = relay.Function([var_9127,], output)
mod['func_9138'] = func_9138
mod = relay.transform.InferType()(mod)
mutated_mod['func_9138'] = func_9138
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9139 = relay.var("var_9139", dtype = "float32", shape = (13, 2, 15))#candidate|9139|(13, 2, 15)|var|float32
func_9138_call = mutated_mod.get_global_var('func_9138')
call_9140 = func_9138_call(var_9139)
output = call_9140
func_9141 = relay.Function([var_9139], output)
mutated_mod['func_9141'] = func_9141
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7169_call = mod.get_global_var('func_7169')
func_7171_call = mutated_mod.get_global_var('func_7171')
call_9236 = relay.TupleGetItem(func_7169_call(), 0)
call_9237 = relay.TupleGetItem(func_7171_call(), 0)
output = call_9236
output2 = call_9237
func_9238 = relay.Function([], output)
mod['func_9238'] = func_9238
mod = relay.transform.InferType()(mod)
mutated_mod['func_9238'] = func_9238
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9238_call = mutated_mod.get_global_var('func_9238')
call_9239 = func_9238_call()
output = call_9239
func_9240 = relay.Function([], output)
mutated_mod['func_9240'] = func_9240
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6143_call = mod.get_global_var('func_6143')
func_6144_call = mutated_mod.get_global_var('func_6144')
call_9247 = relay.TupleGetItem(func_6143_call(), 0)
call_9248 = relay.TupleGetItem(func_6144_call(), 0)
output = call_9247
output2 = call_9248
func_9250 = relay.Function([], output)
mod['func_9250'] = func_9250
mod = relay.transform.InferType()(mod)
output = func_9250()
func_9251 = relay.Function([], output)
mutated_mod['func_9251'] = func_9251
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8532_call = mod.get_global_var('func_8532')
func_8533_call = mutated_mod.get_global_var('func_8533')
call_9280 = relay.TupleGetItem(func_8532_call(), 0)
call_9281 = relay.TupleGetItem(func_8533_call(), 0)
output = relay.Tuple([call_9280,])
output2 = relay.Tuple([call_9281,])
func_9293 = relay.Function([], output)
mod['func_9293'] = func_9293
mod = relay.transform.InferType()(mod)
mutated_mod['func_9293'] = func_9293
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9293_call = mutated_mod.get_global_var('func_9293')
call_9294 = func_9293_call()
output = call_9294
func_9295 = relay.Function([], output)
mutated_mod['func_9295'] = func_9295
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8532_call = mod.get_global_var('func_8532')
func_8533_call = mutated_mod.get_global_var('func_8533')
call_9298 = relay.TupleGetItem(func_8532_call(), 0)
call_9299 = relay.TupleGetItem(func_8533_call(), 0)
output = relay.Tuple([call_9298,])
output2 = relay.Tuple([call_9299,])
func_9342 = relay.Function([], output)
mod['func_9342'] = func_9342
mod = relay.transform.InferType()(mod)
output = func_9342()
func_9343 = relay.Function([], output)
mutated_mod['func_9343'] = func_9343
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8532_call = mod.get_global_var('func_8532')
func_8533_call = mutated_mod.get_global_var('func_8533')
call_9355 = relay.TupleGetItem(func_8532_call(), 0)
call_9356 = relay.TupleGetItem(func_8533_call(), 0)
output = call_9355
output2 = call_9356
func_9371 = relay.Function([], output)
mod['func_9371'] = func_9371
mod = relay.transform.InferType()(mod)
output = func_9371()
func_9372 = relay.Function([], output)
mutated_mod['func_9372'] = func_9372
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9379 = relay.var("var_9379", dtype = "uint32", shape = (5, 1, 6))#candidate|9379|(5, 1, 6)|var|uint32
var_9380 = relay.var("var_9380", dtype = "uint32", shape = (5, 15, 6))#candidate|9380|(5, 15, 6)|var|uint32
bop_9381 = relay.logical_xor(var_9379.astype('uint32'), var_9380.astype('uint32')) # shape=(5, 15, 6)
uop_9385 = relay.cos(var_9380.astype('float32')) # shape=(5, 15, 6)
func_7198_call = mod.get_global_var('func_7198')
func_7200_call = mutated_mod.get_global_var('func_7200')
call_9387 = relay.TupleGetItem(func_7198_call(), 2)
call_9388 = relay.TupleGetItem(func_7200_call(), 2)
func_2304_call = mod.get_global_var('func_2304')
func_2306_call = mutated_mod.get_global_var('func_2306')
call_9391 = relay.TupleGetItem(func_2304_call(), 0)
call_9392 = relay.TupleGetItem(func_2306_call(), 0)
output = relay.Tuple([bop_9381,uop_9385,call_9387,call_9391,])
output2 = relay.Tuple([bop_9381,uop_9385,call_9388,call_9392,])
func_9407 = relay.Function([var_9379,var_9380,], output)
mod['func_9407'] = func_9407
mod = relay.transform.InferType()(mod)
mutated_mod['func_9407'] = func_9407
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9407_call = mutated_mod.get_global_var('func_9407')
var_9409 = relay.var("var_9409", dtype = "uint32", shape = (5, 1, 6))#candidate|9409|(5, 1, 6)|var|uint32
var_9410 = relay.var("var_9410", dtype = "uint32", shape = (5, 15, 6))#candidate|9410|(5, 15, 6)|var|uint32
call_9408 = func_9407_call(var_9409,var_9410,)
output = call_9408
func_9411 = relay.Function([var_9409,var_9410,], output)
mutated_mod['func_9411'] = func_9411
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8440_call = mod.get_global_var('func_8440')
func_8442_call = mutated_mod.get_global_var('func_8442')
call_9425 = relay.TupleGetItem(func_8440_call(), 1)
call_9426 = relay.TupleGetItem(func_8442_call(), 1)
output = relay.Tuple([call_9425,])
output2 = relay.Tuple([call_9426,])
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
func_7451_call = mod.get_global_var('func_7451')
func_7453_call = mutated_mod.get_global_var('func_7453')
call_9449 = relay.TupleGetItem(func_7451_call(), 0)
call_9450 = relay.TupleGetItem(func_7453_call(), 0)
func_1519_call = mod.get_global_var('func_1519')
func_1522_call = mutated_mod.get_global_var('func_1522')
var_9456 = relay.var("var_9456", dtype = "float32", shape = (130, 1))#candidate|9456|(130, 1)|var|float32
call_9455 = func_1519_call(relay.reshape(var_9456.astype('float32'), [5, 13, 2]))
call_9457 = func_1519_call(relay.reshape(var_9456.astype('float32'), [5, 13, 2]))
uop_9459 = relay.sigmoid(var_9456.astype('float32')) # shape=(130, 1)
func_6934_call = mod.get_global_var('func_6934')
func_6936_call = mutated_mod.get_global_var('func_6936')
call_9466 = func_6934_call()
call_9467 = func_6934_call()
uop_9468 = relay.atan(uop_9459.astype('float64')) # shape=(130, 1)
output = relay.Tuple([call_9449,call_9455,call_9466,uop_9468,])
output2 = relay.Tuple([call_9450,call_9457,call_9467,uop_9468,])
func_9470 = relay.Function([var_9456,], output)
mod['func_9470'] = func_9470
mod = relay.transform.InferType()(mod)
var_9471 = relay.var("var_9471", dtype = "float32", shape = (130, 1))#candidate|9471|(130, 1)|var|float32
output = func_9470(var_9471)
func_9472 = relay.Function([var_9471], output)
mutated_mod['func_9472'] = func_9472
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9503 = relay.var("var_9503", dtype = "float32", shape = ())#candidate|9503|()|var|float32
var_9504 = relay.var("var_9504", dtype = "float32", shape = (10, 8, 1))#candidate|9504|(10, 8, 1)|var|float32
bop_9505 = relay.power(var_9503.astype('float32'), var_9504.astype('float32')) # shape=(10, 8, 1)
func_7144_call = mod.get_global_var('func_7144')
func_7146_call = mutated_mod.get_global_var('func_7146')
var_9527 = relay.var("var_9527", dtype = "float64", shape = (36,))#candidate|9527|(36,)|var|float64
call_9526 = relay.TupleGetItem(func_7144_call(relay.reshape(var_9527.astype('float64'), [9, 2, 2])), 0)
call_9528 = relay.TupleGetItem(func_7146_call(relay.reshape(var_9527.astype('float64'), [9, 2, 2])), 0)
output = relay.Tuple([bop_9505,call_9526,var_9527,])
output2 = relay.Tuple([bop_9505,call_9528,var_9527,])
func_9534 = relay.Function([var_9503,var_9504,var_9527,], output)
mod['func_9534'] = func_9534
mod = relay.transform.InferType()(mod)
mutated_mod['func_9534'] = func_9534
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9534_call = mutated_mod.get_global_var('func_9534')
var_9536 = relay.var("var_9536", dtype = "float32", shape = ())#candidate|9536|()|var|float32
var_9537 = relay.var("var_9537", dtype = "float32", shape = (10, 8, 1))#candidate|9537|(10, 8, 1)|var|float32
var_9538 = relay.var("var_9538", dtype = "float64", shape = (36,))#candidate|9538|(36,)|var|float64
call_9535 = func_9534_call(var_9536,var_9537,var_9538,)
output = call_9535
func_9539 = relay.Function([var_9536,var_9537,var_9538,], output)
mutated_mod['func_9539'] = func_9539
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4115_call = mod.get_global_var('func_4115')
func_4117_call = mutated_mod.get_global_var('func_4117')
call_9549 = relay.TupleGetItem(func_4115_call(), 0)
call_9550 = relay.TupleGetItem(func_4117_call(), 0)
func_3650_call = mod.get_global_var('func_3650')
func_3652_call = mutated_mod.get_global_var('func_3652')
call_9556 = func_3650_call()
call_9557 = func_3650_call()
func_3034_call = mod.get_global_var('func_3034')
func_3036_call = mutated_mod.get_global_var('func_3036')
call_9570 = relay.TupleGetItem(func_3034_call(), 0)
call_9571 = relay.TupleGetItem(func_3036_call(), 0)
func_2780_call = mod.get_global_var('func_2780')
func_2785_call = mutated_mod.get_global_var('func_2785')
const_9577 = relay.const([[-6],[-6],[8],[7],[-7],[1],[-10],[-3],[5],[-5],[10],[5],[6],[5],[-5],[-7],[5],[10],[-3],[9],[5],[-6],[-4],[-5],[4],[5],[-1],[-5],[-2],[1],[5],[-8],[3],[6],[-6],[-6],[4],[7],[10],[6],[-1],[10],[-1],[3],[7],[-1],[-9],[-5],[-9],[-8],[7],[-6],[-5],[-8],[7],[1],[-4],[2],[-9],[-7],[6],[-1],[8],[-1],[8],[-2],[3],[-5],[-2],[-5],[6],[7],[-10],[3],[5],[-8],[-9],[7],[-6],[2],[8],[-10],[-3],[1]], dtype = "uint32")#candidate|9577|(84, 1)|const|uint32
const_9578 = relay.const([-4,-4,-10,1,4,5,-6,10,10,4,1,-8,-2,5,8,-10,2,3,-8,7,-8,-3,-7,-8,10,-2,3,-1,3,-10,7,-3,-4,3,9,-6,-4,-3,-4,9,4,-7,1,2,6,-7,2,2,-4,-7,-8,-4,-2,7,-8,1,8,-7,-6,7,2,4,1,9,-4,-2,1,-7,3,-8,10,2,-7,-9,9,6,-9,7,-8,-9,5,5,9,9,-3,2,-8,3,3,-2,-9,6,-1,-10,-9,1,2,10,-7,-5,7,6,-10,-5,-3,7,-7,10,6,-9,10,-1,-8,-8,-3,9,-8,7,6,-3,1,10,3,-6,-9,5,4,6,10,-9,4,-5,3,-2,-6,-5,-5,2,5,8,-2,-7,-1,-8,-6,-4,-3,5,-2,2,-4,-4,-3,6,4,-2,-6,-3,-2,8,6,-10,-2,4,6,2,6,-8,4,-5,-7,-5,9,-2,10,1,-3,-6,10,10,7,-5,-10,2,-6,-4,-7,7,-8,-7,10,-4,-10,9,10,7,3,-10,4,9,-8,-4,2,1,2,-8,-5,-5,-3,-7,4,-2,-6,10,-4,-10,1,-9,7,3,-7,2,-3,9,1,-9,-9,-10,3,5,-10,-2,-2,4,-3,1,-7,-2,-1,-6,-4,-7,-4,-10,-8,4,3,-9,-1,6], dtype = "int64")#candidate|9578|(250,)|const|int64
call_9576 = relay.TupleGetItem(func_2780_call(relay.reshape(const_9577.astype('uint32'), [3, 2, 14]), relay.reshape(const_9578.astype('int64'), [250,]), relay.reshape(const_9577.astype('uint32'), [3, 2, 14]), ), 2)
call_9579 = relay.TupleGetItem(func_2785_call(relay.reshape(const_9577.astype('uint32'), [3, 2, 14]), relay.reshape(const_9578.astype('int64'), [250,]), relay.reshape(const_9577.astype('uint32'), [3, 2, 14]), ), 2)
func_8698_call = mod.get_global_var('func_8698')
func_8699_call = mutated_mod.get_global_var('func_8699')
call_9583 = func_8698_call()
call_9584 = func_8698_call()
output = relay.Tuple([call_9549,call_9556,call_9570,call_9576,const_9577,const_9578,call_9583,])
output2 = relay.Tuple([call_9550,call_9557,call_9571,call_9579,const_9577,const_9578,call_9584,])
func_9609 = relay.Function([], output)
mod['func_9609'] = func_9609
mod = relay.transform.InferType()(mod)
output = func_9609()
func_9610 = relay.Function([], output)
mutated_mod['func_9610'] = func_9610
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9371_call = mod.get_global_var('func_9371')
func_9372_call = mutated_mod.get_global_var('func_9372')
call_9677 = func_9371_call()
call_9678 = func_9371_call()
output = call_9677
output2 = call_9678
func_9683 = relay.Function([], output)
mod['func_9683'] = func_9683
mod = relay.transform.InferType()(mod)
mutated_mod['func_9683'] = func_9683
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9683_call = mutated_mod.get_global_var('func_9683')
call_9684 = func_9683_call()
output = call_9684
func_9685 = relay.Function([], output)
mutated_mod['func_9685'] = func_9685
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9105_call = mod.get_global_var('func_9105')
func_9107_call = mutated_mod.get_global_var('func_9107')
call_9694 = relay.TupleGetItem(func_9105_call(), 2)
call_9695 = relay.TupleGetItem(func_9107_call(), 2)
output = call_9694
output2 = call_9695
func_9710 = relay.Function([], output)
mod['func_9710'] = func_9710
mod = relay.transform.InferType()(mod)
mutated_mod['func_9710'] = func_9710
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9710_call = mutated_mod.get_global_var('func_9710')
call_9711 = func_9710_call()
output = call_9711
func_9712 = relay.Function([], output)
mutated_mod['func_9712'] = func_9712
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3650_call = mod.get_global_var('func_3650')
func_3652_call = mutated_mod.get_global_var('func_3652')
call_9753 = func_3650_call()
call_9754 = func_3650_call()
func_7592_call = mod.get_global_var('func_7592')
func_7596_call = mutated_mod.get_global_var('func_7596')
const_9758 = relay.const([1,-1,3,-1,-2,2,9,-7,-5,4,2,9,6,1,3,3,4,-10,-3,-2,4,-9,8,-9,-1,-8,6,-6,5,2,-7,-9,-1,10,2,7], dtype = "uint16")#candidate|9758|(36,)|const|uint16
const_9759 = relay.const([-10,-5,2,3,-10,-9,1,-4,-1,10,-6,1,-4,-7,8,10,3,-8,-3,4,9,-10,9,-5,-6,10,-7,7,3,-4,-10,-8,8,-7,-8,4,8,10,-9,8,4,-5,-9,2,-8,1,-9,-10,-7,-9,10,4,9,-5,-3,-4,-1,7,3,9,6,-7,1,3,6,4,-9,-4,-6,-7,-2,-3,-1,-10,-2,4,-1,2,-10,-1,-10,2,7,10,-7,-10,7,9,-6,2,9,5,-9,-3,5,-5,1,6,7,9,2,-2,-5,-9,-1,-10,-7,2,5,4,9,4,-1,8,-4,-2,8,-5,7,7,-5,10,-3,9,-8,-7,4,-7,-2,3,-3,4,10,-6,5,5,-2,3,7,-3,-7,-4,-2,8,-7,1,7,-1,7,2,-3,-2,-1,-2,1,5,-8,8,1,5,6,-6,-1,10,8,-10,8,-8,10,-9,-5,-6,-3,-2,-2,-10,3,3,-7,-2,6,6,5,-3,1,-4,6,9,6,-2,8,-9,10,-5,-5,-1,-10,-5,8,9,-1,8,-5,-7,-10,-1,2,1,4,-8,6,9,6,-2,3,-8,6,-2,-4,-4,-7,-7,9,-1,-6,1,2,-10,6,-5,-5,5,-8,4,7,8,-5,5,5,-6,-8,-4,6,7,8,-1,4,4,-5,5,8,-8,-10,-8,8,7,8,-4,-7,-6,-4,8,3,1,-2,-1,-10,5,1,-5,7,5,-5,-10,2,7,-3,8,-9,-5,5,-3,-7,9,2,-7,7,-4,2,5,10,-2,9,8,-10,10,2,-2,-4,7,6,2,-7,-4,-10,3,-2,-2,6,8,-4,-1,4,5,6,-3,-5,6,3,3,10,3,4,3,-7,5,-1,-8,-4,2,-3,4,10,-4,-1,-6,2,5,7,5,8,5,-8,2,-4,-4,9,-6,10,-2,6,4,-9,3,4,10,-10,1,6,4,10,-6,7,-8,4,8,9,-8,-10,6,1,-7,-1,-2,2,6,3,-10,7,-5,-9,-9,-4,9,-7,9,-1,2,-3,-8,8,6,9,10,-4,-5,8,3,2,-8,-7,9,-1,9,-5,10,4,-5,-10,8,-1,-6,8,3,-1,9,7,-7,10,4,-6,9,8,2,-8,-3,3,2,-9,3,7,10,-1,2,-5,-5,1,-9,-7,-9,1,-7,-1,10,-3,10,7,4,6,-9,4,-2,-9,6,-3,-2,6,1,-6,7,-3,7,-6,-8,-7,-5,-3,6,9,-8,8,7,9,3,-8,-3,9,3,-3,10,-9,10,4,-6,1,-5,5,-5,1,-10,-8,2,-6,-3,-9,8,-1,-2,6,8,-5,6,-7,6,7,-7,-2,-4,-5,7,1,-1,-4,7,-4,-9,10,-1,-4,-2,-5,-10,7,7,-3,5,-2,8,3,7,-2,6,-2,6,-4,-9,-7,-7,-4,-8], dtype = "uint32")#candidate|9759|(540,)|const|uint32
call_9757 = relay.TupleGetItem(func_7592_call(relay.reshape(const_9758.astype('uint16'), [9, 2, 2]), relay.reshape(const_9759.astype('uint32'), [540,]), ), 0)
call_9760 = relay.TupleGetItem(func_7596_call(relay.reshape(const_9758.astype('uint16'), [9, 2, 2]), relay.reshape(const_9759.astype('uint32'), [540,]), ), 0)
output = relay.Tuple([call_9753,call_9757,const_9758,const_9759,])
output2 = relay.Tuple([call_9754,call_9760,const_9758,const_9759,])
func_9761 = relay.Function([], output)
mod['func_9761'] = func_9761
mod = relay.transform.InferType()(mod)
mutated_mod['func_9761'] = func_9761
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9761_call = mutated_mod.get_global_var('func_9761')
call_9762 = func_9761_call()
output = call_9762
func_9763 = relay.Function([], output)
mutated_mod['func_9763'] = func_9763
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6567_call = mod.get_global_var('func_6567')
func_6568_call = mutated_mod.get_global_var('func_6568')
call_9827 = relay.TupleGetItem(func_6567_call(), 2)
call_9828 = relay.TupleGetItem(func_6568_call(), 2)
func_7058_call = mod.get_global_var('func_7058')
func_7059_call = mutated_mod.get_global_var('func_7059')
call_9837 = func_7058_call()
call_9838 = func_7058_call()
output = relay.Tuple([call_9827,call_9837,])
output2 = relay.Tuple([call_9828,call_9838,])
func_9864 = relay.Function([], output)
mod['func_9864'] = func_9864
mod = relay.transform.InferType()(mod)
output = func_9864()
func_9865 = relay.Function([], output)
mutated_mod['func_9865'] = func_9865
mutated_mod = relay.transform.InferType()(mutated_mod)
const_9889 = relay.const([[[-7.576861,-7.085646,-5.387642,-0.933681,-8.397370,3.247908,-7.290523],[-4.587583,-9.842995,5.749542,-4.258860,-2.469191,-3.463315,1.555016],[-4.275266,7.213503,-6.481855,7.900834,9.113904,-6.333982,-5.509627],[-8.977769,-6.843265,9.105123,9.797488,-2.369276,4.885125,3.498948],[6.192553,2.510560,3.563294,-2.761046,7.941176,2.080465,-2.416088],[-2.817706,8.219772,5.518577,-8.829974,-0.113898,8.540833,4.789767],[3.342436,-2.571270,4.666933,-8.228054,-6.776528,-1.940437,9.636108],[-6.656774,-2.439519,-2.539107,-0.798153,7.575761,9.034981,-2.140032],[-7.988848,5.885193,0.976629,3.623587,8.367189,3.437708,-7.497644],[5.752900,2.341343,7.552907,6.504060,6.927613,4.889384,-3.573094],[-5.361349,8.729558,-7.132386,-3.867009,-0.878216,-7.107338,-9.311611],[-1.439205,-0.388285,-5.933804,5.438796,7.584894,6.442160,-2.471088],[4.441712,9.100665,-4.731337,9.648586,1.742030,-8.235657,7.621762],[-0.662632,-5.858747,-0.110772,-0.998287,8.291643,6.534245,-2.338476]],[[2.593852,7.560110,4.339034,5.730492,-9.402334,-0.205871,-1.020083],[8.151210,-7.258025,8.361436,-3.168707,9.749952,-4.559104,8.760056],[1.748259,8.981952,-9.447259,5.904345,6.970171,9.184742,5.111058],[-3.879072,-3.669826,6.911187,1.542961,-3.309328,0.786613,-3.280638],[-1.625891,4.839546,-6.520559,-5.833277,8.394512,-4.988413,-5.722767],[-2.253176,-1.802610,-0.630292,6.068778,2.113419,-9.197244,-1.147575],[6.348269,-3.277877,-3.332875,8.090520,-7.829875,-3.588284,4.172962],[-0.812597,-8.653448,-2.730542,9.845060,-8.506824,-8.780190,1.906237],[5.604704,-1.063438,9.773991,-8.902672,-9.107128,-5.668980,5.343015],[9.057314,3.071832,6.527282,-6.667412,-5.581114,-1.341747,-1.095491],[-0.039254,5.667060,-7.248455,-6.044322,-2.446134,0.249077,-3.840166],[4.805141,-3.217938,4.894651,3.068758,-5.157389,-3.386169,9.316028],[3.378460,2.624560,-3.405565,4.061384,4.573890,-0.083202,-0.418607],[-0.192389,1.828532,-8.170265,-4.497589,5.864822,-7.014853,-9.702113]],[[3.096992,3.390538,1.468057,-2.618314,-8.048735,-8.083560,-1.901212],[9.667279,9.399570,7.572080,-3.198179,-0.819532,8.096144,-6.152532],[4.647667,-5.266102,-6.195718,5.916276,3.130081,8.314389,3.843741],[1.521323,-5.677812,-8.323814,-8.476349,-0.676510,-2.835285,-6.323623],[8.787891,9.202613,0.156865,7.998067,-3.661377,7.699799,-3.797156],[3.789550,9.260187,7.311465,8.817468,6.121294,-6.438043,-1.451931],[-2.957784,-5.240974,3.380522,3.642315,-2.230711,5.708517,6.959222],[-0.086421,7.860103,-3.039086,-7.062858,8.517764,2.383237,7.924431],[-1.417860,-2.547546,-7.092460,-7.423886,0.109179,-8.628961,-1.694979],[-8.753131,2.269278,-7.756507,-1.884447,5.275909,-0.384309,-2.632830],[5.505097,0.619455,-9.634764,-4.298844,5.444700,-4.020019,-7.996654],[-9.749047,-3.214863,5.595678,0.708552,1.246473,-9.731819,-9.390689],[9.467475,-1.865103,-7.856963,-1.129765,-7.225461,-5.166756,-0.834650],[-5.478007,1.603348,6.598624,4.780597,4.375888,-8.651354,-5.582366]],[[7.246580,-9.962140,4.440638,2.021293,-4.604629,-4.865900,7.337812],[-2.388085,-2.988530,-3.719666,7.364556,2.913456,-8.923447,3.676582],[8.565781,2.018899,-4.315635,7.626207,1.876810,-9.811315,3.203073],[-8.529874,3.688519,-9.669576,0.323203,0.784154,-7.076029,1.773624],[-0.763249,-9.555487,-4.071907,-8.850862,9.182327,-0.061160,0.934921],[-4.333001,-4.790882,8.018396,-1.591449,7.357598,-2.293266,-4.952123],[2.135875,-6.461995,7.913492,-7.181908,-9.086425,-7.601612,-7.325942],[-3.048074,1.573480,-4.556300,9.806853,2.855405,6.353381,7.663513],[-2.250054,0.308009,1.801625,0.137120,-4.142203,-7.096232,-4.756077],[-9.558144,-9.028480,-0.594986,8.744056,2.979023,-6.883051,-0.659453],[4.682820,-3.774021,-3.703717,4.074424,5.674793,-7.747345,-5.464995],[-9.446071,2.234281,-7.881151,-3.746202,-8.683350,9.882826,-0.975827],[-5.259861,-2.186285,9.942930,1.017840,-5.977517,4.327471,7.877971],[1.322694,1.445424,6.794210,-5.635213,-7.552826,-3.378287,-5.672505]],[[-9.454404,-5.070517,-9.667831,-6.667758,4.403184,3.844487,-5.992534],[4.158515,-6.922970,-2.028587,-2.030212,-7.854776,6.690716,8.886303],[7.576847,8.529755,1.398845,6.880925,-8.976081,6.965118,0.969264],[9.577162,6.327396,-7.746251,8.109191,3.975070,-2.922754,-8.744858],[-6.158330,6.271346,-4.560729,5.844784,-2.608179,7.528603,-1.203489],[-8.811331,7.226844,-7.432301,-8.776994,-1.572143,4.095997,-3.300381],[9.878624,2.213532,-1.918217,-9.738987,7.538876,-4.585229,-7.402883],[3.026117,-0.441292,-4.972119,9.345037,7.376816,9.925813,-9.392236],[2.761338,-8.129679,0.865650,6.666262,3.735393,-9.939182,2.631966],[-3.909357,-5.168787,8.956467,-5.065997,-5.456584,-4.332059,3.156703],[6.018553,-4.810732,-9.888264,-3.500814,-7.311789,-0.615988,7.472841],[-8.225002,6.703295,-4.173395,-6.222272,1.758418,9.578902,9.730893],[2.914522,-6.216921,-8.299889,0.590567,7.369549,-2.667296,7.138378],[9.980255,-0.306791,-6.171338,5.677654,2.381194,-8.425978,-5.604586]],[[9.865920,5.525578,-6.750061,3.943308,-1.789307,-9.966904,-7.486360],[0.623032,0.328595,-3.831166,-3.939005,6.612829,8.485394,-7.222663],[8.134451,-2.815709,-6.236008,5.385770,7.548469,9.535724,-1.428017],[3.209429,-9.625279,-7.497778,-4.154082,1.637766,8.892966,-5.210107],[-4.062705,-8.505250,9.236536,-3.904446,-3.962090,-4.557135,-8.027427],[0.776345,0.076827,-3.307765,0.826505,7.004526,8.171068,6.638124],[-8.218376,-2.248014,-8.731809,-2.802826,3.810918,3.198826,9.123480],[5.140822,8.213349,-1.753682,3.557859,-7.092971,1.088568,-9.414851],[6.095163,-4.311362,4.170071,-3.230514,3.582173,7.481029,5.110604],[0.691795,3.267715,-9.026761,2.786871,5.067573,2.045389,-8.642961],[-7.949625,-8.125467,-1.987199,2.761067,0.954829,8.837338,-1.420602],[0.867966,4.193781,-4.727325,9.511449,3.296319,9.229651,2.591848],[-2.753283,-9.044121,9.603454,-1.737024,4.983383,8.032503,8.825825],[3.336490,-8.445859,9.541804,4.180701,-2.942151,6.176930,-2.477735]],[[-9.947040,4.293077,7.971608,0.538319,-8.248725,-5.265255,7.759505],[-5.523753,-6.961395,7.626764,-8.771028,-9.836858,-0.357861,-6.659489],[-3.545319,0.837760,7.825478,1.648924,-0.787031,3.600073,0.613967],[-4.168593,4.043127,9.055794,-8.203824,-3.855675,-8.536050,3.900659],[1.921473,-4.277956,-1.361263,2.914665,-0.842291,-7.795706,4.971826],[-9.382060,0.416582,-2.346225,6.686276,-2.537144,-7.820616,5.320984],[7.090349,4.099459,-8.911570,-5.845029,7.316984,-3.887031,-5.030896],[-5.879992,-6.432006,-9.941280,9.377989,9.773677,6.290592,6.131923],[-0.988370,-6.837315,6.557256,0.202910,8.265255,-8.514853,4.296437],[-8.584520,5.416167,6.565073,3.059288,1.993976,-5.495226,-0.804072],[-9.701347,0.032618,-9.052837,-3.605826,-0.613136,1.064947,2.330774],[-3.678932,1.406420,-1.356465,-7.544346,-3.122691,-0.555573,-8.450291],[-8.996724,-5.036395,-9.444291,-7.069081,4.254946,-8.625765,-9.742582],[9.854261,5.408545,-8.714639,-5.452952,6.667054,-1.172669,5.732346]],[[2.113535,-7.459800,-9.072612,-9.493985,-4.955741,0.971115,6.637289],[9.345938,2.149767,9.023748,5.651191,0.641432,9.565905,-3.071265],[8.326211,-3.538786,4.061026,-6.846488,0.898798,2.232521,9.996047],[2.753454,-7.650669,-1.101433,9.852844,7.746215,6.933778,-4.563060],[8.455761,3.971890,-2.761126,-4.646796,-4.572579,7.455465,2.329906],[5.014274,2.936934,-9.467121,-2.878354,-8.344307,-7.881488,-2.774384],[-8.948894,-6.479955,8.936325,-9.017992,2.934664,4.236737,-4.944804],[3.794793,7.126202,-7.824948,6.231659,6.233127,-0.317398,1.582774],[4.505910,-1.383627,5.022870,7.041070,-2.247220,-4.043875,-8.632536],[9.008123,9.232050,6.754196,-0.088332,7.955151,-5.550022,8.819346],[-0.789691,9.707284,-5.721194,-7.392081,4.293917,-1.846264,0.569094],[0.791667,-9.723729,-2.613949,-7.530589,8.803408,-1.200768,-9.131296],[6.717511,3.928699,8.736542,0.422642,-0.785041,3.588820,8.199222],[-4.303612,-8.709095,6.437091,-7.568727,-1.491286,8.704906,7.211520]],[[3.883653,-1.444308,0.184714,-8.297067,-3.778169,-9.837179,8.307641],[-5.824987,1.763721,-9.463763,5.046844,1.109280,9.193085,-1.250369],[4.620913,-0.310643,8.219904,4.963497,-9.714435,3.355594,5.661431],[-6.365059,3.802127,6.869367,3.189576,5.630233,0.739741,-1.531491],[-5.598632,1.479386,1.099708,-3.124315,-4.875004,6.888445,-3.704719],[-5.428673,4.031813,-2.331524,7.603246,4.229874,1.288161,7.021669],[4.761622,-4.348815,-4.969161,9.078871,0.337648,9.030991,0.914973],[0.092085,8.411953,5.494277,-0.589728,-4.701321,-5.756326,-4.504389],[-1.882554,-7.259459,0.246678,1.744447,9.615523,9.124336,4.045308],[-9.708882,-6.613901,-4.678002,6.712611,-1.388589,9.811065,-8.346990],[-9.999979,-4.847295,-0.940548,1.325187,3.785392,-2.222478,3.988457],[2.709413,-5.799797,-2.116165,9.621297,-5.576652,-9.700074,-9.431536],[2.294598,7.672667,2.044758,-7.814474,8.407331,-0.221330,5.964950],[3.430086,-8.337829,9.518737,-1.814511,5.401961,-2.003788,8.794988]],[[-9.328097,-6.154690,-1.254423,-9.726342,7.462644,4.450170,-7.354389],[6.340246,-9.227552,-8.403083,-0.817498,1.372752,8.431088,-0.444990],[0.013966,5.756762,-4.202464,6.860871,4.324929,-7.643696,6.071722],[7.977637,7.151854,7.535605,8.753249,9.606127,0.239853,1.791941],[1.167061,-8.231185,7.404941,2.378765,0.286891,-9.906099,-3.457134],[-3.980491,-2.552594,2.810272,-5.505674,-8.974418,-9.640222,5.342697],[-0.984937,3.267487,2.192876,-7.332985,5.713511,-1.817572,2.944567],[2.243331,0.315996,8.074479,-0.321211,-1.935713,2.753119,-0.440415],[-0.111680,1.020411,-7.306605,-8.586066,-0.298468,-7.164392,-3.345483],[-2.113615,9.539747,4.441676,4.761762,4.798740,9.739789,6.258343],[-2.408521,7.452176,6.792830,8.738629,9.385509,4.509799,1.316026],[8.247132,-5.957701,7.106342,7.683121,5.089002,0.488235,-3.717572],[-5.676082,5.889336,-2.645404,4.529807,4.558120,7.489702,-1.467609],[-8.671677,0.973004,-4.218183,6.710833,6.952448,-7.259201,-0.586360]],[[4.825844,9.505092,-0.060298,-4.892176,8.190134,-8.138228,5.771471],[4.331952,8.563062,1.593447,8.423681,-0.268295,0.821522,6.814869],[-7.768306,0.003376,4.237733,0.722791,3.671825,-7.683388,5.282277],[2.953520,-8.680388,6.146687,-2.623084,-9.945882,-1.617166,-6.662523],[9.401533,0.126623,0.070323,4.957700,3.457622,-9.437954,0.326617],[3.417082,-6.401864,6.049826,1.651381,-8.148352,5.339005,8.656647],[9.614218,0.906506,-7.886910,1.384976,3.480037,-2.575395,7.447948],[6.767345,1.703247,-7.135498,9.598578,-0.707567,-1.604534,-2.819322],[-4.231921,7.337082,3.838363,-9.506909,7.959185,-7.561131,-8.919478],[-6.415035,9.003863,-0.983563,-5.313906,-2.841348,-3.998493,7.108498],[6.816883,-8.461472,4.057365,-3.989526,-2.027913,-8.123973,-4.805630],[-1.259856,9.256191,-4.502935,-5.381610,6.158089,3.494712,-1.996749],[3.468071,-9.953904,2.720302,-5.955367,-2.263561,-5.562049,9.220348],[2.818656,2.047029,-6.192072,-4.555040,9.247130,-8.922443,2.182374]],[[5.374956,5.931622,1.606996,9.077192,3.160099,-8.637785,-0.470605],[-2.338520,0.607645,7.867122,-1.932311,-2.988549,8.925317,5.729334],[-1.851220,6.776492,0.146294,-6.011444,7.024655,6.776949,4.990535],[-3.145862,-6.706441,3.248539,-6.840391,-4.152175,9.727206,0.913756],[7.849436,-9.871039,-3.662201,1.735902,-3.681438,-4.715984,6.365875],[-0.625174,7.360406,7.528593,-5.442987,-5.231804,7.347898,3.449044],[1.104494,3.433418,0.537293,-1.843753,-5.787797,5.032889,-9.758794],[-9.312604,-7.134995,-3.990495,7.475539,5.357167,4.053505,4.488499],[8.530032,0.747945,2.989780,2.854459,-8.427889,-4.291184,7.623574],[4.039457,-8.970845,4.629711,9.870415,-3.482474,1.355364,-1.182636],[9.511747,-0.071680,-7.426466,0.507639,-1.824502,-0.122163,1.972704],[5.374086,1.029122,-0.515568,-2.723302,-3.531823,9.844882,8.346017],[-5.521624,9.433277,8.356837,-8.402523,6.386608,1.232259,-2.688920],[-9.819066,1.997967,-3.112979,7.247210,-6.298097,2.673415,1.473966]],[[9.834213,3.445192,-1.336011,-0.225023,-5.934677,8.346027,-6.364589],[-2.667445,-6.094048,-7.325157,-0.578862,-2.566045,7.248893,-3.962343],[1.451093,-4.756898,-3.921458,5.456642,-7.456504,-0.027629,-4.302545],[8.831063,-2.125336,-2.785061,-3.105994,-1.514947,7.926871,-9.464172],[1.559032,9.608857,-3.241834,-2.083799,-5.189492,8.992588,1.962985],[9.294813,7.963157,-1.325677,-8.172205,5.944047,-0.628523,-1.234857],[-6.819315,-1.301160,1.736912,2.069444,3.766311,-3.122231,0.757196],[4.509701,6.225165,-4.440021,3.215812,-0.463399,3.398353,-0.435861],[-1.177814,-8.002220,-3.868074,-1.991530,-9.689244,1.720813,1.403765],[0.431313,-3.111122,0.285560,-7.581105,-5.391959,9.006321,4.365200],[-3.813539,-0.449732,-6.675621,-5.726650,5.171283,-9.109627,-7.936204],[-7.649411,5.109271,-9.888761,-6.617611,9.738583,1.742471,-8.957408],[0.823881,-7.361400,4.292149,-1.555259,7.219116,-4.674169,6.555930],[-5.957489,5.819009,-8.293832,6.729993,-0.445290,-5.951010,-0.968858]]], dtype = "float32")#candidate|9889|(13, 14, 7)|const|float32
uop_9890 = relay.log2(const_9889.astype('float32')) # shape=(13, 14, 7)
func_3731_call = mod.get_global_var('func_3731')
func_3734_call = mutated_mod.get_global_var('func_3734')
const_9898 = relay.const([1.874515,3.715575,-3.780736,-4.738950,-9.454154,-6.279148,-9.528648,3.399247,-9.870184,-1.359344,-7.588131,5.071929,4.020413,5.898246,6.116925,8.625700,-7.764495,-7.812396,-5.717656,2.000501,-8.465788,-9.890977,4.823586,-5.597617,6.294028,5.481746,9.362808,9.329371,-8.704153,9.193026,2.285370,-0.750736,5.443921,-8.645790,-6.435944,-0.407116,3.814379,6.445906,-1.685266,3.235894,-3.730269,-7.288279,2.342936,3.841909,-1.368478,-9.521417,6.124348,8.163352,0.924283,7.425214,9.801134,-8.068599,-9.968728,9.597527,-6.900131,-8.155172,-9.135415,-4.405925,-4.059416,9.989374,-7.608694,-2.479544,0.750484,-7.221717,6.671875,-7.265227,6.413293,-6.691105,-2.251433,-3.480011,-1.733251,7.953482], dtype = "float32")#candidate|9898|(72,)|const|float32
call_9897 = relay.TupleGetItem(func_3731_call(relay.reshape(const_9898.astype('float32'), [72,])), 1)
call_9899 = relay.TupleGetItem(func_3734_call(relay.reshape(const_9898.astype('float32'), [72,])), 1)
func_9043_call = mod.get_global_var('func_9043')
func_9046_call = mutated_mod.get_global_var('func_9046')
var_9910 = relay.var("var_9910", dtype = "float32", shape = (56,))#candidate|9910|(56,)|var|float32
call_9909 = relay.TupleGetItem(func_9043_call(relay.reshape(var_9910.astype('float32'), [1, 8, 7])), 2)
call_9911 = relay.TupleGetItem(func_9046_call(relay.reshape(var_9910.astype('float32'), [1, 8, 7])), 2)
output = relay.Tuple([uop_9890,call_9897,const_9898,call_9909,var_9910,])
output2 = relay.Tuple([uop_9890,call_9899,const_9898,call_9911,var_9910,])
func_9915 = relay.Function([var_9910,], output)
mod['func_9915'] = func_9915
mod = relay.transform.InferType()(mod)
var_9916 = relay.var("var_9916", dtype = "float32", shape = (56,))#candidate|9916|(56,)|var|float32
output = func_9915(var_9916)
func_9917 = relay.Function([var_9916], output)
mutated_mod['func_9917'] = func_9917
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9864_call = mod.get_global_var('func_9864')
func_9865_call = mutated_mod.get_global_var('func_9865')
call_10004 = relay.TupleGetItem(func_9864_call(), 0)
call_10005 = relay.TupleGetItem(func_9865_call(), 0)
output = call_10004
output2 = call_10005
func_10032 = relay.Function([], output)
mod['func_10032'] = func_10032
mod = relay.transform.InferType()(mod)
output = func_10032()
func_10033 = relay.Function([], output)
mutated_mod['func_10033'] = func_10033
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5900_call = mod.get_global_var('func_5900')
func_5902_call = mutated_mod.get_global_var('func_5902')
call_10034 = relay.TupleGetItem(func_5900_call(), 0)
call_10035 = relay.TupleGetItem(func_5902_call(), 0)
func_3059_call = mod.get_global_var('func_3059')
func_3062_call = mutated_mod.get_global_var('func_3062')
const_10054 = relay.const(4, dtype = "uint32")#candidate|10054|()|const|uint32
const_10055 = relay.const([-8,3,-8,6,-5,4,8,-5,-6,3,5,-1,3,6,-1,-2,-10,3,-8,-7,7,2,5,-4,10,-3,7,-1,-9,8,4,9,4,3,8,-8,-3,10,-8,1,4,-4,7,1,-2,5,8,-1,5,-8,-4,-10,9,-7,6,6,3,3,7,5,5,-7,-6,-9,2,6,8,-7,5,3,-3,3,8,5,2,-5,1,-1,-2,-10,10,2,-1,4,-4,-7,-5,-4,-6,8,-10,4,7,-10,8,3,5,5,-6,-4,-5,9,3,2,-2,-7,7,6,7,-3,10,-4,-5,3,-7,2,-9,-1,-4,-2,-5,-1,-10,-6,-4,3,-9,9,5,3,-8,-3,6,9,-7,6,-10,6,-3,9,3,3,9,4,-5,-6,-6,2,-3,1,2,3,6,1,2,-9,2,-5,-6,-4,9,-6,9,6,8,1,7,-1,-3,-2,-2,10,-5,-6,-7,3,-10,-1,-6,-10,-4,-6,7,6,2,5,-1,10,1,8,-6,-3,2,7,1,-4,-10,-8,8,9,1,3,-10,-9,-9,-10,-10,5,-7,9,2,4,4,1,5,-3,3,-10,9,5,-8,4,7,1,-2,3,4,7,9,-1,7,3,-9,4,-4,-7,3,-2,1,-6,4,6,-7,9,3,2,-3,4,10,2,-7,6,-8,-2,-4,1,-10,-9,4,-4,-5,8,3,-1,-2,-7,-10,10,-3,-9,3,-4,-9,-9,-10,-1,-3,-4,3,-9,8,3,-9,8,-9,9,-6,-4,-8,1,8,-1,-1,7,-10,-8,-2,-8,7,-3,2,-8,-4,7,-7,-8,-8,-8,-5,4,1,8,6,4,-10,10,8,-2,10,6,8,4,4,7,-5,9,-5,-1,10,6,4,-4,4,9,-7,-3,9,-1,9,4,-10,-2,-9,6,10,-3,-8,9,5,9,-2,-7,2,-6,5,-7,-5,10,3,5,-9,-10,-5,10,6,2,-2,7,-6,-6,-4,-5,-1,-3,2,10,8,8,-6,5,-10,9,5,-7,-10,-1,-4,-1,1,1,-4,5,-8,7,-3,-7,-7,-4,-2,-3,-4,7,1,4,4,5,8,-1,-3,2,9,9,-8,10,2,4,-8,-3,-9,-2,4,-2,-9,1,-9,10,-4,6,9,-2,9,-8,-7,7,10,10,1,6,-2,4,2,1,-4,-8,1,6,7,9,5,-3,-9,8,-4,-2,3,-2,-1,-3,-8,-7,-2,-10,-7,7,9,6,3,-8,10,7,-5,10,-10,2,-3,-8,4,-6,-9,2,2,-3,-3,6,-10,-9,-2,2,10,-1,-3,-10,8,-9,-10,2,10,-9,-8,-6,-9,-5,2,6,-3,8,7,4,-3,-10,-3,-5,10,6,10,-6,7,-4,9,4,7,10,8,-9,5,4,-4,1,-4,9,8,-4,7,5,-6,-9,-9,-8,3,9], dtype = "uint32")#candidate|10055|(540,)|const|uint32
call_10053 = relay.TupleGetItem(func_3059_call(relay.reshape(const_10054.astype('uint32'), []), relay.reshape(const_10055.astype('uint32'), [6, 10, 9]), ), 0)
call_10056 = relay.TupleGetItem(func_3062_call(relay.reshape(const_10054.astype('uint32'), []), relay.reshape(const_10055.astype('uint32'), [6, 10, 9]), ), 0)
func_9407_call = mod.get_global_var('func_9407')
func_9411_call = mutated_mod.get_global_var('func_9411')
var_10059 = relay.var("var_10059", dtype = "uint32", shape = (30, 1))#candidate|10059|(30, 1)|var|uint32
var_10060 = relay.var("var_10060", dtype = "uint32", shape = (150, 3))#candidate|10060|(150, 3)|var|uint32
call_10058 = relay.TupleGetItem(func_9407_call(relay.reshape(var_10059.astype('uint32'), [5, 1, 6]), relay.reshape(var_10060.astype('uint32'), [5, 15, 6]), ), 3)
call_10061 = relay.TupleGetItem(func_9411_call(relay.reshape(var_10059.astype('uint32'), [5, 1, 6]), relay.reshape(var_10060.astype('uint32'), [5, 15, 6]), ), 3)
output = relay.Tuple([call_10034,call_10053,const_10054,const_10055,call_10058,var_10059,var_10060,])
output2 = relay.Tuple([call_10035,call_10056,const_10054,const_10055,call_10061,var_10059,var_10060,])
func_10063 = relay.Function([var_10059,var_10060,], output)
mod['func_10063'] = func_10063
mod = relay.transform.InferType()(mod)
mutated_mod['func_10063'] = func_10063
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10063_call = mutated_mod.get_global_var('func_10063')
var_10065 = relay.var("var_10065", dtype = "uint32", shape = (30, 1))#candidate|10065|(30, 1)|var|uint32
var_10066 = relay.var("var_10066", dtype = "uint32", shape = (150, 3))#candidate|10066|(150, 3)|var|uint32
call_10064 = func_10063_call(var_10065,var_10066,)
output = call_10064
func_10067 = relay.Function([var_10065,var_10066,], output)
mutated_mod['func_10067'] = func_10067
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5375_call = mod.get_global_var('func_5375')
func_5376_call = mutated_mod.get_global_var('func_5376')
call_10091 = relay.TupleGetItem(func_5375_call(), 0)
call_10092 = relay.TupleGetItem(func_5376_call(), 0)
output = relay.Tuple([call_10091,])
output2 = relay.Tuple([call_10092,])
func_10097 = relay.Function([], output)
mod['func_10097'] = func_10097
mod = relay.transform.InferType()(mod)
output = func_10097()
func_10098 = relay.Function([], output)
mutated_mod['func_10098'] = func_10098
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7058_call = mod.get_global_var('func_7058')
func_7059_call = mutated_mod.get_global_var('func_7059')
call_10108 = func_7058_call()
call_10109 = func_7058_call()
func_8532_call = mod.get_global_var('func_8532')
func_8533_call = mutated_mod.get_global_var('func_8533')
call_10111 = relay.TupleGetItem(func_8532_call(), 0)
call_10112 = relay.TupleGetItem(func_8533_call(), 0)
func_7169_call = mod.get_global_var('func_7169')
func_7171_call = mutated_mod.get_global_var('func_7171')
call_10116 = relay.TupleGetItem(func_7169_call(), 0)
call_10117 = relay.TupleGetItem(func_7171_call(), 0)
output = relay.Tuple([call_10108,call_10111,call_10116,])
output2 = relay.Tuple([call_10109,call_10112,call_10117,])
func_10123 = relay.Function([], output)
mod['func_10123'] = func_10123
mod = relay.transform.InferType()(mod)
output = func_10123()
func_10124 = relay.Function([], output)
mutated_mod['func_10124'] = func_10124
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7058_call = mod.get_global_var('func_7058')
func_7059_call = mutated_mod.get_global_var('func_7059')
call_10217 = func_7058_call()
call_10218 = func_7058_call()
const_10226 = relay.const([[[4.972900,4.933578],[-8.604826,3.990335]],[[-4.704641,4.452606],[-7.540700,-0.109979]],[[-6.031027,-6.615284],[-8.975445,-8.559255]],[[-3.116277,6.071329],[7.068778,-1.760001]],[[9.917041,-5.759917],[-7.275550,9.090216]],[[-6.949583,-7.158329],[-0.658323,5.831124]],[[-5.799774,-4.064934],[-2.788547,-8.008892]],[[-9.938970,-2.302947],[-8.645668,0.584262]],[[4.128528,6.466388],[1.447734,-7.714289]]], dtype = "float64")#candidate|10226|(9, 2, 2)|const|float64
bop_10227 = relay.not_equal(call_10217.astype('bool'), relay.reshape(const_10226.astype('bool'), relay.shape_of(call_10217))) # shape=(9, 2, 2)
bop_10230 = relay.not_equal(call_10218.astype('bool'), relay.reshape(const_10226.astype('bool'), relay.shape_of(call_10218))) # shape=(9, 2, 2)
func_4437_call = mod.get_global_var('func_4437')
func_4440_call = mutated_mod.get_global_var('func_4440')
var_10236 = relay.var("var_10236", dtype = "float32", shape = (1296,))#candidate|10236|(1296,)|var|float32
call_10235 = relay.TupleGetItem(func_4437_call(relay.reshape(var_10236.astype('float32'), [9, 16, 9]), relay.reshape(var_10236.astype('float32'), [9, 16, 9]), ), 1)
call_10237 = relay.TupleGetItem(func_4440_call(relay.reshape(var_10236.astype('float32'), [9, 16, 9]), relay.reshape(var_10236.astype('float32'), [9, 16, 9]), ), 1)
uop_10244 = relay.cosh(var_10236.astype('float32')) # shape=(1296,)
func_5900_call = mod.get_global_var('func_5900')
func_5902_call = mutated_mod.get_global_var('func_5902')
call_10256 = relay.TupleGetItem(func_5900_call(), 1)
call_10257 = relay.TupleGetItem(func_5902_call(), 1)
func_755_call = mod.get_global_var('func_755')
func_758_call = mutated_mod.get_global_var('func_758')
var_10263 = relay.var("var_10263", dtype = "float32", shape = (220,))#candidate|10263|(220,)|var|float32
call_10262 = relay.TupleGetItem(func_755_call(relay.reshape(var_10263.astype('float32'), [11, 2, 10]), relay.reshape(var_10263.astype('float32'), [11, 2, 10]), ), 0)
call_10264 = relay.TupleGetItem(func_758_call(relay.reshape(var_10263.astype('float32'), [11, 2, 10]), relay.reshape(var_10263.astype('float32'), [11, 2, 10]), ), 0)
var_10266 = relay.var("var_10266", dtype = "float32", shape = (1296,))#candidate|10266|(1296,)|var|float32
bop_10267 = relay.logical_xor(uop_10244.astype('int64'), relay.reshape(var_10266.astype('int64'), relay.shape_of(uop_10244))) # shape=(1296,)
output = relay.Tuple([bop_10227,call_10235,call_10256,call_10262,var_10263,bop_10267,])
output2 = relay.Tuple([bop_10230,call_10237,call_10257,call_10264,var_10263,bop_10267,])
func_10272 = relay.Function([var_10236,var_10263,var_10266,], output)
mod['func_10272'] = func_10272
mod = relay.transform.InferType()(mod)
mutated_mod['func_10272'] = func_10272
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10272_call = mutated_mod.get_global_var('func_10272')
var_10274 = relay.var("var_10274", dtype = "float32", shape = (1296,))#candidate|10274|(1296,)|var|float32
var_10275 = relay.var("var_10275", dtype = "float32", shape = (220,))#candidate|10275|(220,)|var|float32
var_10276 = relay.var("var_10276", dtype = "float32", shape = (1296,))#candidate|10276|(1296,)|var|float32
call_10273 = func_10272_call(var_10274,var_10275,var_10276,)
output = call_10273
func_10277 = relay.Function([var_10274,var_10275,var_10276,], output)
mutated_mod['func_10277'] = func_10277
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8532_call = mod.get_global_var('func_8532')
func_8533_call = mutated_mod.get_global_var('func_8533')
call_10282 = relay.TupleGetItem(func_8532_call(), 0)
call_10283 = relay.TupleGetItem(func_8533_call(), 0)
output = relay.Tuple([call_10282,])
output2 = relay.Tuple([call_10283,])
func_10286 = relay.Function([], output)
mod['func_10286'] = func_10286
mod = relay.transform.InferType()(mod)
output = func_10286()
func_10287 = relay.Function([], output)
mutated_mod['func_10287'] = func_10287
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6717_call = mod.get_global_var('func_6717')
func_6719_call = mutated_mod.get_global_var('func_6719')
call_10330 = relay.TupleGetItem(func_6717_call(), 0)
call_10331 = relay.TupleGetItem(func_6719_call(), 0)
func_7169_call = mod.get_global_var('func_7169')
func_7171_call = mutated_mod.get_global_var('func_7171')
call_10334 = relay.TupleGetItem(func_7169_call(), 0)
call_10335 = relay.TupleGetItem(func_7171_call(), 0)
func_7058_call = mod.get_global_var('func_7058')
func_7059_call = mutated_mod.get_global_var('func_7059')
call_10372 = func_7058_call()
call_10373 = func_7058_call()
output = relay.Tuple([call_10330,call_10334,call_10372,])
output2 = relay.Tuple([call_10331,call_10335,call_10373,])
func_10375 = relay.Function([], output)
mod['func_10375'] = func_10375
mod = relay.transform.InferType()(mod)
output = func_10375()
func_10376 = relay.Function([], output)
mutated_mod['func_10376'] = func_10376
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2226_call = mod.get_global_var('func_2226')
func_2227_call = mutated_mod.get_global_var('func_2227')
call_10390 = func_2226_call()
call_10391 = func_2226_call()
func_2316_call = mod.get_global_var('func_2316')
func_2317_call = mutated_mod.get_global_var('func_2317')
call_10393 = relay.TupleGetItem(func_2316_call(), 0)
call_10394 = relay.TupleGetItem(func_2317_call(), 0)
output = relay.Tuple([call_10390,call_10393,])
output2 = relay.Tuple([call_10391,call_10394,])
func_10409 = relay.Function([], output)
mod['func_10409'] = func_10409
mod = relay.transform.InferType()(mod)
mutated_mod['func_10409'] = func_10409
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10409_call = mutated_mod.get_global_var('func_10409')
call_10410 = func_10409_call()
output = call_10410
func_10411 = relay.Function([], output)
mutated_mod['func_10411'] = func_10411
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10412 = relay.var("var_10412", dtype = "uint16", shape = (3, 7, 1))#candidate|10412|(3, 7, 1)|var|uint16
var_10413 = relay.var("var_10413", dtype = "uint16", shape = (3, 7, 6))#candidate|10413|(3, 7, 6)|var|uint16
bop_10414 = relay.add(var_10412.astype('uint16'), var_10413.astype('uint16')) # shape=(3, 7, 6)
uop_10428 = relay.erf(var_10412.astype('float32')) # shape=(3, 7, 1)
output = relay.Tuple([bop_10414,uop_10428,])
output2 = relay.Tuple([bop_10414,uop_10428,])
func_10437 = relay.Function([var_10412,var_10413,], output)
mod['func_10437'] = func_10437
mod = relay.transform.InferType()(mod)
var_10438 = relay.var("var_10438", dtype = "uint16", shape = (3, 7, 1))#candidate|10438|(3, 7, 1)|var|uint16
var_10439 = relay.var("var_10439", dtype = "uint16", shape = (3, 7, 6))#candidate|10439|(3, 7, 6)|var|uint16
output = func_10437(var_10438,var_10439,)
func_10440 = relay.Function([var_10438,var_10439,], output)
mutated_mod['func_10440'] = func_10440
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10375_call = mod.get_global_var('func_10375')
func_10376_call = mutated_mod.get_global_var('func_10376')
call_10455 = relay.TupleGetItem(func_10375_call(), 2)
call_10456 = relay.TupleGetItem(func_10376_call(), 2)
output = call_10455
output2 = call_10456
func_10458 = relay.Function([], output)
mod['func_10458'] = func_10458
mod = relay.transform.InferType()(mod)
mutated_mod['func_10458'] = func_10458
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10458_call = mutated_mod.get_global_var('func_10458')
call_10459 = func_10458_call()
output = call_10459
func_10460 = relay.Function([], output)
mutated_mod['func_10460'] = func_10460
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10466 = relay.var("var_10466", dtype = "float64", shape = (1, 4, 8))#candidate|10466|(1, 4, 8)|var|float64
const_10467 = relay.const([[[2.639955,-9.175241,0.964322,4.419974,-5.758037,6.732635,5.598415,-0.868666],[2.414119,-0.894860,-8.338127,-0.038413,-4.102679,-0.606363,4.441469,9.764040],[3.064807,-3.855981,-2.771501,4.653897,5.924973,0.879771,6.287175,0.232436],[-8.911070,3.035546,-1.669555,0.906478,3.239848,-0.996757,0.688299,9.890861]],[[8.914729,9.858078,1.100707,5.192092,-7.184814,7.487494,-0.017486,-3.299321],[-2.359830,6.269761,2.572539,-9.740140,-3.197029,0.410038,-1.133470,-5.709557],[0.791708,8.236541,-9.701372,9.382043,8.990676,-1.303588,-6.552575,-6.391281],[2.513912,3.836310,8.094918,9.377890,-8.651694,7.745286,9.677398,5.616171]],[[-5.911446,-1.417031,9.248798,8.057175,-7.494811,-1.726559,-4.813195,-6.014676],[-8.672655,-1.572334,4.018995,-9.788111,5.887207,-5.731168,7.234844,3.570473],[-6.925153,9.224672,3.356453,0.262115,-6.471110,-6.925815,-1.342284,-0.030656],[4.928432,-9.462770,-4.753883,-3.787986,5.387171,5.984425,-2.636454,-4.660986]],[[-3.798700,-4.550921,-9.067615,7.913394,1.136306,2.212956,-5.423841,6.320075],[-5.653296,-0.896876,-6.345221,-6.715441,8.399641,-0.964011,-8.100174,3.274332],[-3.869797,3.788986,8.380093,-0.472433,-8.552045,-7.097138,2.853245,-1.289684],[-5.758666,6.303357,-7.292417,-2.710997,5.077748,9.546966,8.190801,-8.897091]],[[7.814620,-6.129586,-6.687444,6.180501,-1.846030,-4.418989,3.833029,0.291233],[1.757265,-8.045895,4.791319,-7.205138,-1.357371,-7.689557,-9.512725,3.671130],[-0.120785,-6.478302,-0.056739,-1.396881,4.671559,1.293976,8.620788,-2.062137],[8.219831,-8.606024,2.738854,2.441899,8.860981,0.292543,-7.217121,2.897689]],[[-8.272819,9.453634,2.935170,6.615716,-9.551447,-3.338125,-7.252855,7.819170],[3.121786,-5.879034,-1.746518,-4.411894,8.831518,9.113596,8.352674,6.314633],[-2.120607,-0.599301,-5.729651,-9.401067,-7.790967,-8.032867,-1.867299,-6.862196],[-4.414494,-6.761579,-9.066568,-3.521695,2.234736,1.381490,-4.479576,-1.141320]],[[-9.796395,-6.080301,3.409560,3.250405,2.289477,-4.075462,6.121146,-6.308508],[3.127712,-0.427036,1.333945,1.512993,-9.299197,9.381279,4.060449,0.887027],[7.621808,-6.764980,1.720444,-5.724877,-9.402932,-6.050366,-1.351391,2.860262],[4.164732,3.063433,-5.696337,9.386398,-9.141363,4.194293,6.185754,4.088951]],[[-1.357547,9.921493,5.883352,1.279778,-5.631614,-1.240540,-6.135325,-5.477235],[0.826127,-0.126691,-8.749882,4.250481,5.185551,7.334680,4.238593,5.754813],[-1.693772,2.519081,-8.225495,1.907709,-2.227246,6.540958,5.152743,2.594354],[-3.018023,-4.498983,2.189520,3.298056,-4.034092,5.692897,8.882012,-0.053661]],[[5.042957,6.495186,-9.343034,-7.494332,-3.951597,9.060016,6.548206,3.249148],[-4.705600,8.727811,5.575239,-9.561860,2.615026,2.146122,-6.518071,-3.909010],[-8.370866,-3.400460,1.513757,4.365693,-9.915068,7.037894,4.177730,8.676353],[5.486939,-0.584370,6.588880,-6.205766,-0.325470,3.784845,0.728003,9.324773]],[[-3.546640,-6.656652,-4.427430,8.118869,-5.764276,6.748308,0.533738,-1.238319],[3.317326,8.577799,0.037899,2.706370,-8.521738,4.057147,-0.812048,5.665062],[-8.768106,-7.080204,9.153024,0.578463,3.603435,-9.455604,-9.138926,6.129359],[5.291840,-4.030417,-9.966289,-3.488341,3.731683,7.368680,-0.735837,-1.365920]],[[-7.553440,-8.412723,-2.526923,-8.864204,-1.106306,0.520045,4.030377,-0.337923],[7.238013,3.702246,-6.611889,-7.022690,6.410014,1.498381,-2.884853,-3.286249],[3.096014,4.471607,4.520860,5.164059,-1.282483,-9.320077,7.259417,-3.846428],[1.247826,-0.118562,8.122165,4.395809,-1.725273,7.477371,-5.408945,-0.306273]],[[-2.496113,-9.028937,5.873212,5.185321,-0.485702,3.855695,-7.741708,-8.227497],[3.848807,6.531212,-0.141104,-1.561982,8.401330,5.216517,9.405572,1.312588],[3.197691,7.520751,6.794024,-2.636401,-6.204077,1.981257,5.402731,4.348412],[2.761236,-7.871972,5.485082,-7.500738,-1.981836,4.128306,9.302026,2.969449]],[[-1.874612,7.301066,3.258188,7.366172,9.797561,-3.712497,-4.235192,-8.403186],[-0.523001,2.757487,5.373654,-3.414733,-2.660414,9.909757,9.244541,-7.967118],[-9.983685,4.837679,-1.038492,5.013204,-0.947268,-5.467416,0.866295,-9.371062],[3.723801,-8.434356,2.245092,-1.785509,-7.829041,-8.146535,-8.117429,1.068943]],[[-6.385097,-5.302649,5.071278,8.716034,5.456842,-0.533188,-4.281587,-3.080746],[0.058264,-7.594110,-7.554690,-7.114643,-8.383475,-6.924724,9.214290,5.053940],[-6.029613,-6.250318,-3.361348,9.960248,-8.766545,-7.334256,-2.090568,-5.409841],[8.378270,3.256650,-9.322047,-7.040091,-0.896848,3.056435,-9.510709,6.720729]]], dtype = "float64")#candidate|10467|(14, 4, 8)|const|float64
bop_10468 = relay.floor_divide(var_10466.astype('float64'), const_10467.astype('float64')) # shape=(14, 4, 8)
uop_10474 = relay.sqrt(bop_10468.astype('float64')) # shape=(14, 4, 8)
output = uop_10474
output2 = uop_10474
func_10490 = relay.Function([var_10466,], output)
mod['func_10490'] = func_10490
mod = relay.transform.InferType()(mod)
mutated_mod['func_10490'] = func_10490
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10491 = relay.var("var_10491", dtype = "float64", shape = (1, 4, 8))#candidate|10491|(1, 4, 8)|var|float64
func_10490_call = mutated_mod.get_global_var('func_10490')
call_10492 = func_10490_call(var_10491)
output = call_10492
func_10493 = relay.Function([var_10491], output)
mutated_mod['func_10493'] = func_10493
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5816_call = mod.get_global_var('func_5816')
func_5818_call = mutated_mod.get_global_var('func_5818')
call_10495 = relay.TupleGetItem(func_5816_call(), 0)
call_10496 = relay.TupleGetItem(func_5818_call(), 0)
output = call_10495
output2 = call_10496
func_10498 = relay.Function([], output)
mod['func_10498'] = func_10498
mod = relay.transform.InferType()(mod)
mutated_mod['func_10498'] = func_10498
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10498_call = mutated_mod.get_global_var('func_10498')
call_10499 = func_10498_call()
output = call_10499
func_10500 = relay.Function([], output)
mutated_mod['func_10500'] = func_10500
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10503 = relay.var("var_10503", dtype = "float64", shape = ())#candidate|10503|()|var|float64
var_10504 = relay.var("var_10504", dtype = "float64", shape = (2, 16, 15))#candidate|10504|(2, 16, 15)|var|float64
bop_10505 = relay.mod(var_10503.astype('float64'), var_10504.astype('float64')) # shape=(2, 16, 15)
uop_10514 = relay.sin(bop_10505.astype('float32')) # shape=(2, 16, 15)
output = relay.Tuple([uop_10514,])
output2 = relay.Tuple([uop_10514,])
func_10525 = relay.Function([var_10503,var_10504,], output)
mod['func_10525'] = func_10525
mod = relay.transform.InferType()(mod)
var_10526 = relay.var("var_10526", dtype = "float64", shape = ())#candidate|10526|()|var|float64
var_10527 = relay.var("var_10527", dtype = "float64", shape = (2, 16, 15))#candidate|10527|(2, 16, 15)|var|float64
output = func_10525(var_10526,var_10527,)
func_10528 = relay.Function([var_10526,var_10527,], output)
mutated_mod['func_10528'] = func_10528
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6412_call = mod.get_global_var('func_6412')
func_6414_call = mutated_mod.get_global_var('func_6414')
call_10548 = relay.TupleGetItem(func_6412_call(), 0)
call_10549 = relay.TupleGetItem(func_6414_call(), 0)
output = call_10548
output2 = call_10549
func_10556 = relay.Function([], output)
mod['func_10556'] = func_10556
mod = relay.transform.InferType()(mod)
output = func_10556()
func_10557 = relay.Function([], output)
mutated_mod['func_10557'] = func_10557
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9371_call = mod.get_global_var('func_9371')
func_9372_call = mutated_mod.get_global_var('func_9372')
call_10582 = func_9371_call()
call_10583 = func_9371_call()
output = call_10582
output2 = call_10583
func_10584 = relay.Function([], output)
mod['func_10584'] = func_10584
mod = relay.transform.InferType()(mod)
mutated_mod['func_10584'] = func_10584
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10584_call = mutated_mod.get_global_var('func_10584')
call_10585 = func_10584_call()
output = call_10585
func_10586 = relay.Function([], output)
mutated_mod['func_10586'] = func_10586
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6717_call = mod.get_global_var('func_6717')
func_6719_call = mutated_mod.get_global_var('func_6719')
call_10607 = relay.TupleGetItem(func_6717_call(), 1)
call_10608 = relay.TupleGetItem(func_6719_call(), 1)
func_8006_call = mod.get_global_var('func_8006')
func_8008_call = mutated_mod.get_global_var('func_8008')
const_10624 = relay.const([8,1,-2,6,-2,-3,10,10,-5,-8,2,8,-10,10,-4,5,3,-1,2,-6,-6,3,-7,1,-6,4,6,-6,4,10,-10,-9,-10,2,8,8,7,1,6,5], dtype = "int8")#candidate|10624|(40,)|const|int8
call_10623 = relay.TupleGetItem(func_8006_call(relay.reshape(const_10624.astype('int8'), [10, 4])), 0)
call_10625 = relay.TupleGetItem(func_8008_call(relay.reshape(const_10624.astype('int8'), [10, 4])), 0)
const_10629 = relay.const([[[-1,-5,6,-2],[-7,-8,-2,4],[-2,-5,10,2],[-1,-8,-10,-6],[-5,-1,3,9],[-4,4,10,8],[-3,-6,1,10],[9,-10,10,-1],[4,-7,7,-9],[-3,-7,-1,2]],[[7,8,-8,-1],[-8,-9,4,-5],[-1,-7,8,-9],[9,1,-2,5],[-3,-9,-5,1],[3,2,-7,8],[-9,8,3,6],[3,3,2,-5],[4,7,8,1],[-7,9,-9,-4]],[[3,6,9,-7],[9,8,-9,8],[10,-3,7,-10],[-8,-8,7,7],[-6,-6,-5,7],[-3,9,1,7],[7,10,5,-6],[-8,-4,-10,4],[6,-1,3,6],[5,9,-5,7]],[[-6,5,4,4],[8,8,-9,-4],[-4,-5,-4,-4],[8,-7,10,4],[9,-7,1,-9],[-1,8,1,6],[-8,-4,-4,3],[6,7,-4,-3],[-10,-9,4,-3],[5,7,-5,5]],[[4,8,-10,9],[1,-1,7,-9],[6,2,-6,-5],[6,10,4,5],[-5,-5,-3,2],[-8,-10,-8,-4],[9,-4,-8,-9],[-2,-6,-4,-4],[3,5,-4,10],[9,7,-1,2]],[[6,6,-7,-8],[5,5,4,-8],[1,-5,-2,6],[-6,-1,-5,-8],[8,-5,-10,4],[-9,-5,-10,-2],[-8,-7,1,-4],[-8,6,7,-6],[-10,10,4,-5],[4,-5,-3,-7]],[[-3,1,-8,1],[-9,1,10,1],[-8,10,-6,4],[3,4,6,8],[6,3,4,1],[-10,-9,2,10],[2,2,3,10],[5,1,-7,-3],[10,-8,10,10],[-4,10,-1,-5]],[[-8,-3,-1,6],[-8,9,8,10],[-8,2,2,7],[3,3,8,8],[-5,7,-5,3],[-2,1,-4,7],[3,-9,-3,10],[-4,9,1,9],[8,1,1,-9],[6,-4,-2,2]],[[2,8,-8,9],[-1,5,6,5],[2,-7,10,5],[-5,4,-1,1],[-8,9,9,-9],[6,10,1,-6],[-3,-5,1,7],[-10,3,9,-5],[5,4,-1,4],[-10,1,-2,-4]],[[4,-8,-1,10],[7,-3,1,7],[1,10,6,-1],[-8,10,9,-7],[-3,-7,9,6],[-3,4,8,-10],[5,-10,3,9],[-4,-3,5,8],[-4,-10,4,-1],[-4,3,-8,-10]]], dtype = "uint8")#candidate|10629|(10, 10, 4)|const|uint8
bop_10630 = relay.less_equal(call_10623.astype('bool'), relay.reshape(const_10629.astype('bool'), relay.shape_of(call_10623))) # shape=(10, 10, 4)
bop_10633 = relay.less_equal(call_10625.astype('bool'), relay.reshape(const_10629.astype('bool'), relay.shape_of(call_10625))) # shape=(10, 10, 4)
func_575_call = mod.get_global_var('func_575')
func_579_call = mutated_mod.get_global_var('func_579')
var_10635 = relay.var("var_10635", dtype = "float32", shape = (8, 12))#candidate|10635|(8, 12)|var|float32
call_10634 = relay.TupleGetItem(func_575_call(relay.reshape(var_10635.astype('float32'), [6, 1, 16]), relay.reshape(const_10624.astype('int8'), [40,]), ), 1)
call_10636 = relay.TupleGetItem(func_579_call(relay.reshape(var_10635.astype('float32'), [6, 1, 16]), relay.reshape(const_10624.astype('int8'), [40,]), ), 1)
output = relay.Tuple([call_10607,const_10624,bop_10630,call_10634,var_10635,])
output2 = relay.Tuple([call_10608,const_10624,bop_10633,call_10636,var_10635,])
func_10645 = relay.Function([var_10635,], output)
mod['func_10645'] = func_10645
mod = relay.transform.InferType()(mod)
mutated_mod['func_10645'] = func_10645
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10646 = relay.var("var_10646", dtype = "float32", shape = (8, 12))#candidate|10646|(8, 12)|var|float32
func_10645_call = mutated_mod.get_global_var('func_10645')
call_10647 = func_10645_call(var_10646)
output = call_10647
func_10648 = relay.Function([var_10646], output)
mutated_mod['func_10648'] = func_10648
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7451_call = mod.get_global_var('func_7451')
func_7453_call = mutated_mod.get_global_var('func_7453')
call_10661 = relay.TupleGetItem(func_7451_call(), 0)
call_10662 = relay.TupleGetItem(func_7453_call(), 0)
func_3920_call = mod.get_global_var('func_3920')
func_3922_call = mutated_mod.get_global_var('func_3922')
call_10667 = relay.TupleGetItem(func_3920_call(), 0)
call_10668 = relay.TupleGetItem(func_3922_call(), 0)
uop_10682 = relay.cosh(call_10661.astype('float32')) # shape=(9, 2, 2)
uop_10684 = relay.cosh(call_10662.astype('float32')) # shape=(9, 2, 2)
output = relay.Tuple([call_10667,uop_10682,])
output2 = relay.Tuple([call_10668,uop_10684,])
func_10685 = relay.Function([], output)
mod['func_10685'] = func_10685
mod = relay.transform.InferType()(mod)
output = func_10685()
func_10686 = relay.Function([], output)
mutated_mod['func_10686'] = func_10686
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7819_call = mod.get_global_var('func_7819')
func_7820_call = mutated_mod.get_global_var('func_7820')
call_10759 = relay.TupleGetItem(func_7819_call(), 0)
call_10760 = relay.TupleGetItem(func_7820_call(), 0)
func_3920_call = mod.get_global_var('func_3920')
func_3922_call = mutated_mod.get_global_var('func_3922')
call_10763 = relay.TupleGetItem(func_3920_call(), 0)
call_10764 = relay.TupleGetItem(func_3922_call(), 0)
func_5408_call = mod.get_global_var('func_5408')
func_5410_call = mutated_mod.get_global_var('func_5410')
call_10776 = relay.TupleGetItem(func_5408_call(), 0)
call_10777 = relay.TupleGetItem(func_5410_call(), 0)
output = relay.Tuple([call_10759,call_10763,call_10776,])
output2 = relay.Tuple([call_10760,call_10764,call_10777,])
func_10791 = relay.Function([], output)
mod['func_10791'] = func_10791
mod = relay.transform.InferType()(mod)
output = func_10791()
func_10792 = relay.Function([], output)
mutated_mod['func_10792'] = func_10792
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7169_call = mod.get_global_var('func_7169')
func_7171_call = mutated_mod.get_global_var('func_7171')
call_10793 = relay.TupleGetItem(func_7169_call(), 0)
call_10794 = relay.TupleGetItem(func_7171_call(), 0)
output = relay.Tuple([call_10793,])
output2 = relay.Tuple([call_10794,])
func_10798 = relay.Function([], output)
mod['func_10798'] = func_10798
mod = relay.transform.InferType()(mod)
mutated_mod['func_10798'] = func_10798
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10798_call = mutated_mod.get_global_var('func_10798')
call_10799 = func_10798_call()
output = call_10799
func_10800 = relay.Function([], output)
mutated_mod['func_10800'] = func_10800
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9371_call = mod.get_global_var('func_9371')
func_9372_call = mutated_mod.get_global_var('func_9372')
call_10828 = func_9371_call()
call_10829 = func_9371_call()
func_3908_call = mod.get_global_var('func_3908')
func_3910_call = mutated_mod.get_global_var('func_3910')
call_10841 = relay.TupleGetItem(func_3908_call(), 0)
call_10842 = relay.TupleGetItem(func_3910_call(), 0)
output = relay.Tuple([call_10828,call_10841,])
output2 = relay.Tuple([call_10829,call_10842,])
func_10844 = relay.Function([], output)
mod['func_10844'] = func_10844
mod = relay.transform.InferType()(mod)
mutated_mod['func_10844'] = func_10844
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10844_call = mutated_mod.get_global_var('func_10844')
call_10845 = func_10844_call()
output = call_10845
func_10846 = relay.Function([], output)
mutated_mod['func_10846'] = func_10846
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8698_call = mod.get_global_var('func_8698')
func_8699_call = mutated_mod.get_global_var('func_8699')
call_10885 = func_8698_call()
call_10886 = func_8698_call()
output = relay.Tuple([call_10885,])
output2 = relay.Tuple([call_10886,])
func_10906 = relay.Function([], output)
mod['func_10906'] = func_10906
mod = relay.transform.InferType()(mod)
mutated_mod['func_10906'] = func_10906
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10906_call = mutated_mod.get_global_var('func_10906')
call_10907 = func_10906_call()
output = call_10907
func_10908 = relay.Function([], output)
mutated_mod['func_10908'] = func_10908
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10286_call = mod.get_global_var('func_10286')
func_10287_call = mutated_mod.get_global_var('func_10287')
call_10909 = relay.TupleGetItem(func_10286_call(), 0)
call_10910 = relay.TupleGetItem(func_10287_call(), 0)
func_3258_call = mod.get_global_var('func_3258')
func_3259_call = mutated_mod.get_global_var('func_3259')
call_10922 = relay.TupleGetItem(func_3258_call(), 0)
call_10923 = relay.TupleGetItem(func_3259_call(), 0)
func_9761_call = mod.get_global_var('func_9761')
func_9763_call = mutated_mod.get_global_var('func_9763')
call_10933 = relay.TupleGetItem(func_9761_call(), 1)
call_10934 = relay.TupleGetItem(func_9763_call(), 1)
func_6934_call = mod.get_global_var('func_6934')
func_6936_call = mutated_mod.get_global_var('func_6936')
call_10938 = func_6934_call()
call_10939 = func_6934_call()
func_4593_call = mod.get_global_var('func_4593')
func_4594_call = mutated_mod.get_global_var('func_4594')
call_10949 = relay.TupleGetItem(func_4593_call(), 2)
call_10950 = relay.TupleGetItem(func_4594_call(), 2)
func_8052_call = mod.get_global_var('func_8052')
func_8054_call = mutated_mod.get_global_var('func_8054')
call_10963 = func_8052_call()
call_10964 = func_8052_call()
func_3961_call = mod.get_global_var('func_3961')
func_3963_call = mutated_mod.get_global_var('func_3963')
call_10965 = func_3961_call()
call_10966 = func_3961_call()
func_7819_call = mod.get_global_var('func_7819')
func_7820_call = mutated_mod.get_global_var('func_7820')
call_10967 = relay.TupleGetItem(func_7819_call(), 0)
call_10968 = relay.TupleGetItem(func_7820_call(), 0)
func_6412_call = mod.get_global_var('func_6412')
func_6414_call = mutated_mod.get_global_var('func_6414')
call_10973 = relay.TupleGetItem(func_6412_call(), 0)
call_10974 = relay.TupleGetItem(func_6414_call(), 0)
func_2909_call = mod.get_global_var('func_2909')
func_2912_call = mutated_mod.get_global_var('func_2912')
const_10980 = relay.const([2.591721,-4.481301,-3.281191,4.381550,3.557100,0.277221,9.900527,-3.590554,2.580788,7.038384,5.294501,-3.776724,-2.296695,-9.809559,1.473941,-9.439660,6.480968,0.818686,3.456418,4.815222,-8.910641,-5.735106,8.176070,1.163891,-8.888176,2.027728,3.156593,3.017344,2.427672,4.776990,-6.421170,0.452284,8.758309,1.716523,2.117986,3.910929,9.899831,1.126121,-9.342905,7.593404,8.920932,7.139214,-5.264441,0.685738,-9.921901,-7.176165,-8.895926,-2.463509,-6.754442,-3.016316,4.031368,-4.844271,8.314644,6.267189,-2.736197,-5.639011,6.818627,8.737519,4.398636,0.862846,1.601634,-8.344397,1.199484,7.909197,-8.570445,-5.382972,-1.124331,8.919514,-0.593114,3.005998,1.650083,4.201979,7.065777,5.901760,6.930532,4.945660,-1.823444,-0.184153,-8.400938,-5.293516,1.073331,-3.522201,9.202888,-1.838694,-2.315810,-4.609448,3.083477,-8.689997,-9.694511,1.771814,-6.866449,4.203993,-9.000413,5.721424,8.991447,-3.090846,-2.399867,-4.315348,-3.380304,8.242765,7.809189,-9.040873,9.183852,5.061166,-5.857711,5.755743,9.385352,-5.286479,-3.225547,1.509220,0.970670,5.190731,-5.580164,9.235800,-7.212945,-4.302331,-2.751970,-7.879974,4.229146,-4.933392,0.250773,8.934766,-0.953356,-4.935734,4.473033,-4.321794,1.609467,-6.651050,-1.683586,-6.974301,-9.091880,-2.794775,-6.288653,6.748504,-2.451774,7.589163,1.323679,8.124959,-5.217543,6.876660,3.386065,-0.444117,0.824843,-4.798390,-3.014612,-9.664330,9.436563,-1.820083,7.283687,-0.829839,4.229365,7.864909,-3.649556,-0.780639,6.111663,-4.425413,9.677763,5.213802,2.117099,-2.466691,6.384967,-0.197378,3.432851,-5.723069,-9.113564,9.721732,-7.747953,9.955569,5.329468,-8.805077,8.754841,1.201877,2.627103,2.296161,-0.920128,3.969087,-4.115839,2.369389,-2.878372,-5.984666,-0.834780,-0.240670,3.111102,8.707981,3.109087,1.624500,-4.142055,5.145099,6.036935,-4.797702,0.758914,7.247888,1.133435,5.529583,-2.064456,4.237530,7.116161,-6.615453,9.803702,1.102213,0.839339,9.758003,3.024136,6.365393,1.486552,0.773598,8.470976,-2.667780,4.968478,-4.701812,2.315306,-6.592416,1.528793,0.399088,-1.447691,0.358214,7.620277,3.954603,-3.391465,-0.182337,-2.112878,-7.086521,-4.547289,-9.543595,-1.968432,-8.489641,-2.325053,7.213113,6.402263,-6.958497,5.166019,2.799638,-4.203090,-0.596194,4.554186,-7.231523,-1.671625,-6.518517,9.550320,-9.097308,5.920722,-1.457549,3.191660,-0.325603,-8.073624,-9.492016,-2.495204,1.369506,-7.653117,9.606585,-5.024491,3.882276], dtype = "float64")#candidate|10980|(252,)|const|float64
var_10981 = relay.var("var_10981", dtype = "int64", shape = (250,))#candidate|10981|(250,)|var|int64
call_10979 = relay.TupleGetItem(func_2909_call(relay.reshape(const_10980.astype('float64'), [6, 42]), relay.reshape(var_10981.astype('int64'), [25, 10]), ), 0)
call_10982 = relay.TupleGetItem(func_2912_call(relay.reshape(const_10980.astype('float64'), [6, 42]), relay.reshape(var_10981.astype('int64'), [25, 10]), ), 0)
uop_10983 = relay.tan(call_10979.astype('float32')) # shape=(5, 13, 2)
uop_10985 = relay.tan(call_10982.astype('float32')) # shape=(5, 13, 2)
func_10645_call = mod.get_global_var('func_10645')
func_10648_call = mutated_mod.get_global_var('func_10648')
var_10995 = relay.var("var_10995", dtype = "float32", shape = (96,))#candidate|10995|(96,)|var|float32
call_10994 = relay.TupleGetItem(func_10645_call(relay.reshape(var_10995.astype('float32'), [8, 12])), 3)
call_10996 = relay.TupleGetItem(func_10648_call(relay.reshape(var_10995.astype('float32'), [8, 12])), 3)
output = relay.Tuple([call_10909,call_10922,call_10933,call_10938,call_10949,call_10963,call_10965,call_10967,call_10973,const_10980,var_10981,uop_10983,call_10994,var_10995,])
output2 = relay.Tuple([call_10910,call_10923,call_10934,call_10939,call_10950,call_10964,call_10966,call_10968,call_10974,const_10980,var_10981,uop_10985,call_10996,var_10995,])
func_11000 = relay.Function([var_10981,var_10995,], output)
mod['func_11000'] = func_11000
mod = relay.transform.InferType()(mod)
mutated_mod['func_11000'] = func_11000
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11000_call = mutated_mod.get_global_var('func_11000')
var_11002 = relay.var("var_11002", dtype = "int64", shape = (250,))#candidate|11002|(250,)|var|int64
var_11003 = relay.var("var_11003", dtype = "float32", shape = (96,))#candidate|11003|(96,)|var|float32
call_11001 = func_11000_call(var_11002,var_11003,)
output = call_11001
func_11004 = relay.Function([var_11002,var_11003,], output)
mutated_mod['func_11004'] = func_11004
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11006 = relay.var("var_11006", dtype = "uint32", shape = (7, 5, 10))#candidate|11006|(7, 5, 10)|var|uint32
var_11007 = relay.var("var_11007", dtype = "uint32", shape = (7, 5, 10))#candidate|11007|(7, 5, 10)|var|uint32
bop_11008 = relay.right_shift(var_11006.astype('uint32'), relay.reshape(var_11007.astype('uint32'), relay.shape_of(var_11006))) # shape=(7, 5, 10)
uop_11016 = relay.asin(var_11007.astype('float32')) # shape=(7, 5, 10)
func_2304_call = mod.get_global_var('func_2304')
func_2306_call = mutated_mod.get_global_var('func_2306')
call_11019 = relay.TupleGetItem(func_2304_call(), 0)
call_11020 = relay.TupleGetItem(func_2306_call(), 0)
func_2201_call = mod.get_global_var('func_2201')
func_2203_call = mutated_mod.get_global_var('func_2203')
call_11025 = relay.TupleGetItem(func_2201_call(), 0)
call_11026 = relay.TupleGetItem(func_2203_call(), 0)
uop_11033 = relay.erf(bop_11008.astype('float32')) # shape=(7, 5, 10)
uop_11042 = relay.atan(uop_11016.astype('float64')) # shape=(7, 5, 10)
func_10375_call = mod.get_global_var('func_10375')
func_10376_call = mutated_mod.get_global_var('func_10376')
call_11045 = relay.TupleGetItem(func_10375_call(), 0)
call_11046 = relay.TupleGetItem(func_10376_call(), 0)
func_2909_call = mod.get_global_var('func_2909')
func_2912_call = mutated_mod.get_global_var('func_2912')
var_11064 = relay.var("var_11064", dtype = "float64", shape = (252, 1))#candidate|11064|(252, 1)|var|float64
var_11065 = relay.var("var_11065", dtype = "int64", shape = (250,))#candidate|11065|(250,)|var|int64
call_11063 = relay.TupleGetItem(func_2909_call(relay.reshape(var_11064.astype('float64'), [6, 42]), relay.reshape(var_11065.astype('int64'), [25, 10]), ), 2)
call_11066 = relay.TupleGetItem(func_2912_call(relay.reshape(var_11064.astype('float64'), [6, 42]), relay.reshape(var_11065.astype('int64'), [25, 10]), ), 2)
output = relay.Tuple([call_11019,call_11025,uop_11033,uop_11042,call_11045,call_11063,var_11064,var_11065,])
output2 = relay.Tuple([call_11020,call_11026,uop_11033,uop_11042,call_11046,call_11066,var_11064,var_11065,])
func_11083 = relay.Function([var_11006,var_11007,var_11064,var_11065,], output)
mod['func_11083'] = func_11083
mod = relay.transform.InferType()(mod)
mutated_mod['func_11083'] = func_11083
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11083_call = mutated_mod.get_global_var('func_11083')
var_11085 = relay.var("var_11085", dtype = "uint32", shape = (7, 5, 10))#candidate|11085|(7, 5, 10)|var|uint32
var_11086 = relay.var("var_11086", dtype = "uint32", shape = (7, 5, 10))#candidate|11086|(7, 5, 10)|var|uint32
var_11087 = relay.var("var_11087", dtype = "float64", shape = (252, 1))#candidate|11087|(252, 1)|var|float64
var_11088 = relay.var("var_11088", dtype = "int64", shape = (250,))#candidate|11088|(250,)|var|int64
call_11084 = func_11083_call(var_11085,var_11086,var_11087,var_11088,)
output = call_11084
func_11089 = relay.Function([var_11085,var_11086,var_11087,var_11088,], output)
mutated_mod['func_11089'] = func_11089
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3694_call = mod.get_global_var('func_3694')
func_3695_call = mutated_mod.get_global_var('func_3695')
call_11091 = relay.TupleGetItem(func_3694_call(), 0)
call_11092 = relay.TupleGetItem(func_3695_call(), 0)
func_541_call = mod.get_global_var('func_541')
func_544_call = mutated_mod.get_global_var('func_544')
const_11138 = relay.const([5,1,-9,-7,-8,6,-6,-10,-5,-3,5,-6,-2,8,-4,-3,2,-5,1,-3,10,-4,6,5,-8,4,6,4,2,7,2,-4,-3,7,-8,-2,10,9,1,9], dtype = "int8")#candidate|11138|(40,)|const|int8
var_11139 = relay.var("var_11139", dtype = "int8", shape = (400,))#candidate|11139|(400,)|var|int8
call_11137 = func_541_call(relay.reshape(const_11138.astype('int8'), [10, 1, 4]), relay.reshape(var_11139.astype('int8'), [10, 10, 4]), )
call_11140 = func_541_call(relay.reshape(const_11138.astype('int8'), [10, 1, 4]), relay.reshape(var_11139.astype('int8'), [10, 10, 4]), )
bop_11143 = relay.equal(var_11139.astype('bool'), relay.reshape(call_11137.astype('bool'), relay.shape_of(var_11139))) # shape=(400,)
bop_11146 = relay.equal(var_11139.astype('bool'), relay.reshape(call_11140.astype('bool'), relay.shape_of(var_11139))) # shape=(400,)
output = relay.Tuple([call_11091,const_11138,bop_11143,])
output2 = relay.Tuple([call_11092,const_11138,bop_11146,])
func_11156 = relay.Function([var_11139,], output)
mod['func_11156'] = func_11156
mod = relay.transform.InferType()(mod)
var_11157 = relay.var("var_11157", dtype = "int8", shape = (400,))#candidate|11157|(400,)|var|int8
output = func_11156(var_11157)
func_11158 = relay.Function([var_11157], output)
mutated_mod['func_11158'] = func_11158
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10906_call = mod.get_global_var('func_10906')
func_10908_call = mutated_mod.get_global_var('func_10908')
call_11175 = relay.TupleGetItem(func_10906_call(), 0)
call_11176 = relay.TupleGetItem(func_10908_call(), 0)
output = call_11175
output2 = call_11176
func_11180 = relay.Function([], output)
mod['func_11180'] = func_11180
mod = relay.transform.InferType()(mod)
mutated_mod['func_11180'] = func_11180
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11180_call = mutated_mod.get_global_var('func_11180')
call_11181 = func_11180_call()
output = call_11181
func_11182 = relay.Function([], output)
mutated_mod['func_11182'] = func_11182
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3995_call = mod.get_global_var('func_3995')
func_3996_call = mutated_mod.get_global_var('func_3996')
call_11190 = func_3995_call()
call_11191 = func_3995_call()
output = call_11190
output2 = call_11191
func_11194 = relay.Function([], output)
mod['func_11194'] = func_11194
mod = relay.transform.InferType()(mod)
mutated_mod['func_11194'] = func_11194
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11194_call = mutated_mod.get_global_var('func_11194')
call_11195 = func_11194_call()
output = call_11195
func_11196 = relay.Function([], output)
mutated_mod['func_11196'] = func_11196
mutated_mod = relay.transform.InferType()(mutated_mod)
const_11224 = relay.const([[[2.476364,-7.098249,-4.992185],[-2.488992,-6.302764,2.974532],[6.873248,5.280898,5.395063]],[[-4.094153,3.461819,2.425868],[1.360541,6.492644,2.446375],[-1.416674,-8.783356,1.192462]],[[-8.537333,3.718810,9.594200],[-8.945457,8.883754,-4.714750],[-3.248162,-9.105697,3.883872]],[[2.860400,-6.504807,5.748412],[3.953669,-8.122555,-3.542391],[1.454577,3.045249,-2.852770]],[[6.973626,4.666158,-5.625248],[2.555343,-4.327200,-5.050382],[3.968176,-9.597742,4.390455]],[[7.714970,4.866046,-2.770142],[6.385532,6.750629,-5.118022],[8.639880,-2.195026,-1.073812]],[[-9.270491,1.182971,-6.177828],[-0.687947,2.379038,6.507473],[6.003583,-5.648172,6.730139]],[[-7.227750,-4.762516,3.438171],[1.801004,-6.949484,-9.393267],[2.750218,-5.327771,8.348888]],[[-6.209355,5.764264,0.745916],[-6.520709,4.781608,6.913205],[0.526790,-7.261753,2.874305]],[[-2.124319,-3.054675,-8.626911],[-7.666851,-4.960314,0.666621],[6.804080,3.527903,5.035462]],[[2.947990,2.384353,-4.905817],[7.833430,5.376492,9.260745],[-6.102302,4.123217,-0.862606]],[[4.589001,0.469116,-6.526296],[0.650824,4.219153,-1.399842],[8.269233,-7.739795,-3.030710]],[[-4.223510,1.252466,5.345701],[-8.185777,-8.332004,6.265724],[-3.390816,7.702710,-0.809857]]], dtype = "float32")#candidate|11224|(13, 3, 3)|const|float32
var_11225 = relay.var("var_11225", dtype = "float32", shape = (13, 3, 3))#candidate|11225|(13, 3, 3)|var|float32
bop_11226 = relay.power(const_11224.astype('float32'), relay.reshape(var_11225.astype('float32'), relay.shape_of(const_11224))) # shape=(13, 3, 3)
uop_11233 = relay.log(const_11224.astype('float64')) # shape=(13, 3, 3)
func_3650_call = mod.get_global_var('func_3650')
func_3652_call = mutated_mod.get_global_var('func_3652')
call_11235 = func_3650_call()
call_11236 = func_3650_call()
output = relay.Tuple([bop_11226,uop_11233,call_11235,])
output2 = relay.Tuple([bop_11226,uop_11233,call_11236,])
func_11255 = relay.Function([var_11225,], output)
mod['func_11255'] = func_11255
mod = relay.transform.InferType()(mod)
mutated_mod['func_11255'] = func_11255
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11256 = relay.var("var_11256", dtype = "float32", shape = (13, 3, 3))#candidate|11256|(13, 3, 3)|var|float32
func_11255_call = mutated_mod.get_global_var('func_11255')
call_11257 = func_11255_call(var_11256)
output = call_11257
func_11258 = relay.Function([var_11256], output)
mutated_mod['func_11258'] = func_11258
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10097_call = mod.get_global_var('func_10097')
func_10098_call = mutated_mod.get_global_var('func_10098')
call_11287 = relay.TupleGetItem(func_10097_call(), 0)
call_11288 = relay.TupleGetItem(func_10098_call(), 0)
output = call_11287
output2 = call_11288
func_11303 = relay.Function([], output)
mod['func_11303'] = func_11303
mod = relay.transform.InferType()(mod)
output = func_11303()
func_11304 = relay.Function([], output)
mutated_mod['func_11304'] = func_11304
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11335 = relay.var("var_11335", dtype = "float32", shape = (11, 9, 6))#candidate|11335|(11, 9, 6)|var|float32
uop_11336 = relay.atanh(var_11335.astype('float32')) # shape=(11, 9, 6)
uop_11341 = relay.asin(uop_11336.astype('float32')) # shape=(11, 9, 6)
output = uop_11341
output2 = uop_11341
F = relay.Function([var_11335,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_11335,], output2)
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
