import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_117 = relay.var("var_117", dtype = "uint64", shape = (14, 10, 6))#candidate|117|(14, 10, 6)|var|uint64
const_118 = relay.const([[[4,10,9,2,9,-6],[8,10,-5,-6,-9,-4],[5,7,7,-1,-3,-7],[-2,-4,10,9,-9,-3],[5,3,-4,-4,3,6],[-7,2,-9,-4,7,5],[-9,-9,-3,-3,10,10],[-5,2,-6,-1,-7,-2],[-10,-1,-6,6,1,2],[-6,10,-2,-1,-5,-8]],[[-3,-5,-10,9,5,8],[-8,-5,-10,1,-3,-5],[1,4,8,6,-1,-2],[-8,-2,4,-2,-6,9],[5,5,9,3,-5,6],[10,-7,-3,-1,-3,-3],[3,-7,-4,7,4,-7],[2,-3,-8,-4,-10,-7],[-1,5,-1,9,6,5],[10,-1,-5,-9,8,-6]],[[8,-7,1,1,-4,6],[-5,-9,10,-2,7,-9],[2,9,-8,8,-5,6],[1,-9,-4,-10,1,1],[-5,-6,-8,3,10,2],[9,6,7,1,9,-2],[-9,1,2,-3,-7,-9],[3,5,-4,-3,-8,-6],[-1,4,-10,-3,7,-9],[8,-7,-9,9,6,5]],[[-4,-4,7,9,10,-10],[-10,-7,8,7,8,-10],[8,-8,7,8,-4,-4],[-4,-1,-8,5,3,-6],[-10,7,-9,-4,8,3],[5,-7,-6,2,-7,8],[-3,5,5,-10,-4,-2],[6,10,-7,-1,8,3],[-2,6,7,7,7,9],[1,8,6,10,5,6]],[[-5,-4,7,-9,-2,8],[-8,-1,-5,8,10,5],[7,8,7,2,10,-5],[3,6,8,5,9,5],[-4,3,-1,10,6,-10],[1,-5,7,-10,5,-6],[-1,10,-6,-7,-10,-4],[1,-8,1,7,9,-5],[-1,9,-2,-8,-7,-7],[5,-3,6,-5,1,-1]],[[-3,-6,-10,1,7,-7],[8,-4,-6,-5,-6,-8],[-6,-7,-8,3,7,-6],[-10,10,10,6,3,-10],[-2,-1,-5,-1,2,10],[-8,-3,-2,-6,7,-10],[3,2,8,6,7,10],[-6,5,-1,-10,-7,8],[2,-2,9,-6,7,-8],[-10,-7,-4,10,-8,-10]],[[9,-1,-4,6,2,7],[-1,4,10,3,6,6],[-6,10,1,-4,3,-7],[-6,-5,2,-2,4,10],[-7,4,2,-3,-8,4],[-6,-8,-4,6,-9,-8],[4,5,-5,-3,-10,6],[-9,-2,-6,4,3,-1],[-10,-8,-9,-1,6,10],[-3,-4,2,-4,-2,7]],[[3,10,-7,4,9,6],[8,-10,5,6,4,10],[-1,-8,3,1,-1,1],[-3,3,8,-1,-9,1],[-2,4,6,-4,8,-9],[1,6,-2,-8,-3,8],[-2,-6,-9,-7,-1,-7],[-4,-3,6,3,2,7],[-6,9,-8,9,-6,-1],[1,4,-6,10,-3,-2]],[[4,6,9,-2,-10,4],[-7,-8,-1,8,8,5],[-4,-5,9,5,7,1],[-5,-10,-5,-3,-9,-7],[-3,-2,6,6,-4,6],[8,-7,1,8,-3,10],[-3,10,5,4,-2,-10],[6,10,-5,-1,6,-8],[8,-2,4,-6,-7,1],[-6,2,1,-8,-6,-7]],[[5,-5,-8,7,-9,-6],[10,-10,-10,1,-5,-6],[4,5,4,-2,10,9],[10,-5,-4,-10,2,-3],[2,-10,6,-5,-4,2],[-10,9,4,9,4,1],[-4,-2,4,9,-1,4],[7,-10,8,8,-8,2],[-5,-6,-5,-4,-9,-5],[6,-8,3,2,1,-10]],[[4,9,-5,6,1,8],[10,-7,10,3,-4,-1],[-4,6,7,-4,-3,6],[5,-9,-3,-4,-1,-1],[3,-7,4,-3,-4,-4],[6,-3,3,9,1,-4],[-5,7,-9,6,-4,-8],[-2,-7,-1,-7,-8,-6],[-2,-7,-2,-9,-1,-4],[-9,-2,-5,1,1,-4]],[[-8,-1,-5,-7,3,2],[-7,6,-1,8,-3,1],[9,5,-10,6,2,-4],[6,6,7,9,-8,2],[7,9,8,-6,-4,9],[-10,3,2,-10,1,2],[-1,2,7,-1,3,4],[2,8,-1,-9,2,4],[1,6,8,-10,8,2],[-7,10,5,-1,4,-2]],[[-8,7,-4,6,4,9],[-10,3,-2,-3,-10,-7],[7,-1,-7,3,5,-5],[-10,4,5,-6,-4,-10],[5,-3,6,-1,10,-1],[6,-4,5,-10,4,-9],[-9,1,5,10,-7,-9],[7,-6,-4,5,5,3],[-1,-7,8,2,-4,-3],[-6,-10,-7,6,9,-10]],[[10,-2,-5,7,7,8],[1,-5,5,-3,-2,-4],[2,-1,-1,-3,-6,-8],[-10,-4,-10,-4,-6,-7],[8,4,4,9,7,6],[-10,-10,4,7,2,2],[-8,4,-7,7,-10,-5],[6,-8,-3,10,3,-2],[-8,2,-2,2,3,4],[-5,-5,-1,-7,4,9]]], dtype = "uint64")#candidate|118|(14, 10, 6)|const|uint64
bop_119 = relay.right_shift(var_117.astype('uint64'), relay.reshape(const_118.astype('uint64'), relay.shape_of(var_117))) # shape=(14, 10, 6)
output = bop_119
output2 = bop_119
func_127 = relay.Function([var_117,], output)
mod['func_127'] = func_127
mod = relay.transform.InferType()(mod)
var_128 = relay.var("var_128", dtype = "uint64", shape = (14, 10, 6))#candidate|128|(14, 10, 6)|var|uint64
output = func_127(var_128)
func_129 = relay.Function([var_128], output)
mutated_mod['func_129'] = func_129
mutated_mod = relay.transform.InferType()(mutated_mod)
const_178 = relay.const([[[False,False,True,True,True,False,False,False,False,True,False,True,False,True,True],[True,False,True,True,True,False,False,False,True,False,True,False,True,True,False],[True,False,False,False,True,False,False,True,False,True,False,False,False,False,True],[True,True,False,False,True,True,True,True,False,False,True,True,False,False,False],[False,False,False,True,False,False,True,True,True,True,False,False,True,False,False],[True,False,False,True,False,True,False,True,False,False,True,False,True,True,False],[False,False,False,False,True,True,False,False,False,False,True,False,False,False,False],[False,True,False,False,False,True,True,True,False,False,True,False,False,True,True],[False,True,True,True,True,False,False,False,False,False,False,True,False,False,False],[False,False,True,True,True,False,False,False,True,False,False,False,False,False,True],[False,True,False,True,False,False,False,False,False,False,False,False,False,False,False]],[[False,False,False,True,True,True,True,True,False,False,False,False,True,False,True],[False,False,False,True,False,False,True,False,False,True,False,False,True,False,False],[True,False,False,True,False,False,True,True,True,True,False,True,True,True,False],[False,True,False,False,False,False,False,True,False,False,False,True,False,True,True],[False,False,False,True,False,False,True,True,True,False,False,True,False,True,False],[False,False,False,False,False,False,True,True,False,True,True,False,False,False,False],[False,False,False,False,True,False,False,False,True,True,True,True,True,True,True],[True,True,True,True,True,True,False,False,False,False,False,False,False,False,False],[False,False,False,True,False,False,True,False,False,True,False,True,False,True,False],[True,False,True,False,False,True,False,False,True,False,False,True,False,False,False],[False,True,False,True,False,True,True,True,True,True,False,True,True,True,False]],[[True,False,True,True,True,True,False,True,True,True,True,True,True,False,True],[True,False,False,True,True,False,False,False,False,False,False,False,True,True,True],[False,False,False,True,True,True,False,True,False,True,True,True,False,False,True],[True,True,False,False,False,True,False,True,False,False,True,False,True,False,True],[False,False,True,False,True,True,True,True,False,True,False,True,True,False,True],[False,False,False,False,False,True,False,False,False,False,True,True,False,False,True],[True,False,False,False,True,True,True,False,True,False,False,True,True,True,False],[True,True,False,True,False,False,False,False,False,False,False,True,True,False,True],[True,True,False,True,True,True,False,True,True,True,True,True,True,False,False],[True,True,False,True,True,False,True,True,False,True,False,False,True,True,False],[False,False,True,False,True,False,True,False,True,True,True,False,False,False,True]],[[True,True,False,True,False,True,True,True,True,True,True,True,True,False,False],[True,False,True,False,True,False,False,False,False,False,True,False,False,False,False],[True,True,False,False,False,False,True,True,False,False,False,True,True,True,True],[False,False,True,True,False,False,True,False,True,False,False,False,False,True,False],[False,False,True,False,False,True,True,False,False,True,False,False,False,False,True],[True,False,True,False,True,True,True,False,False,False,False,False,False,False,True],[True,True,False,False,True,False,False,False,False,False,True,True,True,True,True],[False,False,True,False,True,False,True,False,False,True,False,True,False,False,True],[True,True,False,True,False,False,False,False,False,False,False,False,True,True,True],[False,False,False,True,False,True,True,True,True,False,True,True,True,True,True],[False,False,True,True,False,True,True,False,True,True,False,True,True,False,True]],[[True,False,True,True,False,True,False,True,False,True,True,True,False,False,False],[True,True,True,False,False,True,True,True,True,False,False,True,False,False,True],[True,True,False,False,False,False,True,False,True,True,True,True,True,True,True],[True,False,False,False,True,False,True,False,True,False,True,False,False,True,False],[True,False,True,True,False,True,True,True,True,True,False,False,False,True,True],[True,True,True,False,True,False,False,True,True,False,True,False,False,True,True],[False,True,True,True,False,True,False,False,False,True,True,False,True,True,False],[False,False,True,True,False,False,False,True,True,True,True,True,True,True,False],[False,True,True,True,False,False,False,False,False,False,True,True,False,False,False],[False,False,False,True,True,True,False,True,False,True,False,True,False,True,False],[True,True,True,False,False,True,False,False,True,False,False,False,True,True,False]],[[True,True,False,False,True,True,True,True,True,True,False,True,False,True,True],[False,False,False,True,False,True,False,True,True,True,True,False,True,True,True],[True,False,False,True,False,True,False,True,False,True,False,True,True,False,False],[False,False,False,False,True,False,True,True,True,True,False,True,True,True,False],[False,False,False,False,True,True,False,False,False,False,True,True,True,False,True],[True,False,False,True,True,True,False,False,True,True,True,True,False,False,True],[False,False,True,True,True,True,False,True,True,False,True,False,True,True,True],[True,False,True,True,False,False,False,False,True,True,True,False,True,False,True],[False,False,True,True,True,False,False,True,True,True,False,True,False,True,False],[True,False,False,False,True,False,True,False,False,False,True,False,False,False,False],[True,False,False,True,False,False,True,False,True,True,False,True,False,False,True]],[[False,True,True,False,True,True,True,False,True,True,False,False,True,True,True],[True,False,True,False,True,True,False,True,False,True,False,False,True,False,False],[False,False,True,True,False,False,False,True,True,True,True,True,False,False,False],[True,False,True,False,False,False,False,False,True,False,True,True,False,False,True],[False,False,True,True,False,False,True,False,True,False,False,False,False,False,True],[False,True,True,True,True,True,False,True,True,True,True,False,True,True,True],[False,True,True,False,False,True,False,False,False,True,False,False,False,False,False],[True,True,True,False,False,False,True,False,False,False,False,True,False,True,True],[True,True,False,True,True,True,False,True,True,False,True,True,False,True,False],[False,False,True,True,False,True,False,True,False,False,True,False,True,True,True],[False,True,False,True,False,False,False,False,True,True,True,False,False,True,True]],[[False,False,True,True,True,True,True,True,False,True,True,True,True,True,True],[False,True,False,False,False,False,False,False,False,False,True,True,False,False,True],[False,False,True,True,False,False,True,True,False,True,False,True,True,True,False],[False,True,False,False,True,False,False,False,True,False,False,False,False,False,False],[True,False,True,False,False,True,False,True,False,False,False,False,False,True,True],[False,True,False,False,True,True,True,True,True,False,False,True,False,False,False],[True,True,False,False,True,False,True,True,True,True,False,False,True,False,True],[False,False,True,False,True,False,True,False,False,True,False,False,False,False,False],[False,True,True,True,True,False,True,False,True,True,True,True,True,False,True],[False,False,False,True,False,True,False,False,True,False,True,True,False,True,True],[False,False,True,True,True,False,True,False,True,False,True,False,False,False,True]],[[True,True,True,True,False,False,False,False,False,True,False,True,False,False,False],[False,False,False,True,True,True,True,False,False,False,True,True,True,True,False],[False,False,True,True,False,True,True,False,False,True,False,False,False,False,True],[True,False,True,True,True,True,True,True,True,True,True,False,False,False,True],[False,False,False,True,False,False,True,True,False,True,True,False,True,True,True],[False,False,True,False,False,True,True,True,False,False,False,True,True,False,False],[False,True,False,False,False,False,False,True,False,True,False,True,True,False,False],[False,False,True,False,False,True,True,True,False,True,False,False,False,True,False],[False,True,True,True,False,False,True,False,True,True,True,False,False,True,False],[True,True,False,False,True,True,True,False,False,True,True,False,True,False,True],[True,False,True,True,True,True,True,True,True,False,False,True,False,True,False]],[[False,False,True,True,False,True,False,True,True,False,False,True,True,True,True],[False,False,True,True,True,True,False,False,False,False,True,False,True,True,True],[True,False,True,False,True,True,True,True,False,True,True,False,False,False,True],[True,True,False,False,False,True,True,True,False,True,True,True,False,False,False],[True,True,False,True,True,True,False,True,False,True,False,False,True,False,False],[True,True,True,True,True,False,False,True,True,False,False,False,True,False,False],[False,False,True,False,True,False,False,True,True,False,False,True,False,False,True],[True,True,False,False,False,False,False,False,True,True,True,True,True,False,False],[True,False,False,False,True,True,True,True,False,False,True,True,False,False,True],[True,True,False,False,True,False,False,False,False,True,True,True,False,True,False],[False,False,False,False,True,True,True,False,False,False,False,False,True,False,False]],[[False,False,True,False,False,False,False,False,False,False,True,False,False,True,True],[False,False,True,False,False,False,False,False,False,False,False,True,False,True,True],[False,True,True,True,True,True,False,True,True,False,True,False,False,True,False],[True,True,False,True,False,False,True,False,False,False,False,False,True,True,True],[False,True,False,False,True,True,True,True,False,True,True,False,True,False,True],[True,True,True,True,False,True,False,False,True,False,False,True,True,True,False],[False,True,False,True,True,True,False,True,False,True,False,True,True,True,True],[False,True,True,True,False,True,False,False,True,True,True,True,True,False,False],[True,False,False,True,True,True,False,False,False,False,True,False,False,False,False],[True,False,True,False,False,True,False,False,False,True,False,True,True,True,True],[True,False,True,True,False,True,True,False,True,True,True,False,False,True,False]],[[False,False,False,True,True,False,False,True,True,False,False,True,True,True,False],[False,True,False,False,False,False,True,True,True,False,True,False,False,True,True],[False,True,True,False,False,False,True,False,True,False,True,False,True,False,True],[True,True,False,True,True,True,False,False,False,True,False,True,True,False,False],[False,False,True,True,False,True,False,True,False,True,True,True,True,False,True],[True,True,False,True,True,True,False,True,True,True,False,True,False,True,True],[True,True,True,False,False,False,False,False,True,False,False,True,True,True,True],[False,False,True,True,False,False,False,False,True,False,True,True,True,False,False],[True,True,True,False,True,True,False,True,False,False,True,False,True,False,True],[False,True,False,True,False,False,True,False,False,False,False,False,True,False,False],[True,True,True,False,True,False,False,False,False,False,False,True,False,True,False]]], dtype = "bool")#candidate|178|(12, 11, 15)|const|bool
var_179 = relay.var("var_179", dtype = "bool", shape = (12, 11, 15))#candidate|179|(12, 11, 15)|var|bool
bop_180 = relay.logical_or(const_178.astype('bool'), relay.reshape(var_179.astype('bool'), relay.shape_of(const_178))) # shape=(12, 11, 15)
uop_187 = relay.log(var_179.astype('float64')) # shape=(12, 11, 15)
output = relay.Tuple([bop_180,uop_187,])
output2 = relay.Tuple([bop_180,uop_187,])
func_192 = relay.Function([var_179,], output)
mod['func_192'] = func_192
mod = relay.transform.InferType()(mod)
mutated_mod['func_192'] = func_192
mutated_mod = relay.transform.InferType()(mutated_mod)
var_193 = relay.var("var_193", dtype = "bool", shape = (12, 11, 15))#candidate|193|(12, 11, 15)|var|bool
func_192_call = mutated_mod.get_global_var('func_192')
call_194 = func_192_call(var_193)
output = call_194
func_195 = relay.Function([var_193], output)
mutated_mod['func_195'] = func_195
mutated_mod = relay.transform.InferType()(mutated_mod)
var_277 = relay.var("var_277", dtype = "float32", shape = (9, 3, 16))#candidate|277|(9, 3, 16)|var|float32
var_278 = relay.var("var_278", dtype = "float32", shape = (9, 3, 16))#candidate|278|(9, 3, 16)|var|float32
bop_279 = relay.power(var_277.astype('float32'), relay.reshape(var_278.astype('float32'), relay.shape_of(var_277))) # shape=(9, 3, 16)
bop_283 = relay.left_shift(bop_279.astype('int32'), relay.reshape(var_277.astype('int32'), relay.shape_of(bop_279))) # shape=(9, 3, 16)
var_286 = relay.var("var_286", dtype = "int32", shape = (9, 3, 16))#candidate|286|(9, 3, 16)|var|int32
bop_287 = relay.multiply(bop_283.astype('uint64'), relay.reshape(var_286.astype('uint64'), relay.shape_of(bop_283))) # shape=(9, 3, 16)
func_127_call = mod.get_global_var('func_127')
func_129_call = mutated_mod.get_global_var('func_129')
var_294 = relay.var("var_294", dtype = "uint64", shape = (840,))#candidate|294|(840,)|var|uint64
call_293 = func_127_call(relay.reshape(var_294.astype('uint64'), [14, 10, 6]))
call_295 = func_127_call(relay.reshape(var_294.astype('uint64'), [14, 10, 6]))
output = relay.Tuple([bop_287,call_293,var_294,])
output2 = relay.Tuple([bop_287,call_295,var_294,])
func_297 = relay.Function([var_277,var_278,var_286,var_294,], output)
mod['func_297'] = func_297
mod = relay.transform.InferType()(mod)
var_298 = relay.var("var_298", dtype = "float32", shape = (9, 3, 16))#candidate|298|(9, 3, 16)|var|float32
var_299 = relay.var("var_299", dtype = "float32", shape = (9, 3, 16))#candidate|299|(9, 3, 16)|var|float32
var_300 = relay.var("var_300", dtype = "int32", shape = (9, 3, 16))#candidate|300|(9, 3, 16)|var|int32
var_301 = relay.var("var_301", dtype = "uint64", shape = (840,))#candidate|301|(840,)|var|uint64
output = func_297(var_298,var_299,var_300,var_301,)
func_302 = relay.Function([var_298,var_299,var_300,var_301,], output)
mutated_mod['func_302'] = func_302
mutated_mod = relay.transform.InferType()(mutated_mod)
var_343 = relay.var("var_343", dtype = "float32", shape = (8, 14, 7))#candidate|343|(8, 14, 7)|var|float32
uop_344 = relay.rsqrt(var_343.astype('float32')) # shape=(8, 14, 7)
output = relay.Tuple([uop_344,])
output2 = relay.Tuple([uop_344,])
func_348 = relay.Function([var_343,], output)
mod['func_348'] = func_348
mod = relay.transform.InferType()(mod)
mutated_mod['func_348'] = func_348
mutated_mod = relay.transform.InferType()(mutated_mod)
var_349 = relay.var("var_349", dtype = "float32", shape = (8, 14, 7))#candidate|349|(8, 14, 7)|var|float32
func_348_call = mutated_mod.get_global_var('func_348')
call_350 = func_348_call(var_349)
output = call_350
func_351 = relay.Function([var_349], output)
mutated_mod['func_351'] = func_351
mutated_mod = relay.transform.InferType()(mutated_mod)
var_425 = relay.var("var_425", dtype = "float32", shape = (10, 10, 5))#candidate|425|(10, 10, 5)|var|float32
uop_426 = relay.log10(var_425.astype('float32')) # shape=(10, 10, 5)
output = relay.Tuple([uop_426,])
output2 = relay.Tuple([uop_426,])
func_429 = relay.Function([var_425,], output)
mod['func_429'] = func_429
mod = relay.transform.InferType()(mod)
var_430 = relay.var("var_430", dtype = "float32", shape = (10, 10, 5))#candidate|430|(10, 10, 5)|var|float32
output = func_429(var_430)
func_431 = relay.Function([var_430], output)
mutated_mod['func_431'] = func_431
mutated_mod = relay.transform.InferType()(mutated_mod)
const_695 = relay.const([[[4,6,1,-8,6,-3,4,-10,1],[-9,5,-9,-6,-8,-3,-1,-8,-6],[3,-5,-9,2,4,10,-9,10,-2],[-3,-7,1,7,-6,3,7,7,4],[10,-1,10,-10,10,-3,10,-3,8],[-4,8,-1,1,6,7,3,-8,4],[8,6,-3,-10,-6,7,-7,-8,-2],[-7,-6,10,-4,5,-1,-1,10,-7],[-8,-7,2,-6,-8,5,5,2,4],[9,6,10,-10,6,-10,-6,-10,1]],[[-8,2,-5,-5,-8,4,-8,9,-4],[3,4,7,-2,2,-5,-5,-2,-10],[-1,-7,-9,-2,1,-2,2,10,-5],[-10,9,1,5,-8,1,3,-2,-3],[-1,-9,8,-9,9,8,6,10,-10],[-9,7,1,5,3,8,10,3,-4],[-5,1,4,-7,-7,-6,-10,-1,2],[4,-10,9,-5,7,-2,-8,4,8],[-9,8,4,3,1,-8,6,2,-2],[-3,-2,4,-1,-9,-2,-5,-4,6]],[[-9,1,-3,-2,-4,6,-7,-1,-9],[-3,5,-5,2,7,3,5,2,-1],[-4,5,-9,-4,-10,-7,9,-9,-5],[1,-4,-3,-2,2,-4,-1,8,-8],[7,-5,-6,5,-4,10,-9,-7,1],[-4,10,-9,7,-5,-5,3,-7,-8],[1,-6,8,-6,-9,9,-5,-5,9],[1,5,2,-1,2,1,10,-3,-1],[-4,-5,-2,-3,9,3,-1,5,-2],[-3,-10,-2,-5,7,1,-9,4,6]],[[-2,4,4,-9,-4,10,-9,-1,-10],[-2,-7,4,-6,1,-9,-6,5,-2],[7,-5,-6,-7,9,-8,2,7,10],[7,6,-5,-6,-8,1,3,1,-9],[4,6,5,-4,3,-8,3,-8,-5],[6,4,-4,3,-2,-5,3,-8,-3],[-2,-2,8,-9,-7,-2,4,4,3],[4,5,-10,9,-10,-4,-2,9,3],[-5,-10,3,-5,-1,4,8,10,4],[-4,5,1,-6,-6,-8,2,-1,-6]],[[-4,9,1,-1,-1,-2,3,7,-9],[-7,-3,8,2,-5,-2,-7,-1,4],[-2,-10,-8,-8,-8,10,7,-10,10],[2,-8,7,7,6,2,1,-5,-9],[-1,5,-5,-7,-2,-1,-5,-4,-9],[2,-5,-5,10,-5,4,9,2,-7],[9,-1,8,-3,6,-7,10,-10,-10],[4,-8,-5,4,10,-8,-4,8,7],[-7,1,10,8,-7,-5,-3,5,9],[-4,3,-8,10,9,-9,-3,7,-10]],[[2,-6,-6,4,-9,1,-10,-10,2],[6,-2,-9,1,9,-8,6,-9,-6],[3,-6,-10,10,-3,-5,-10,6,-7],[-5,9,-8,-5,4,7,8,-2,2],[-1,-4,-7,-1,1,1,4,-6,-9],[7,-9,7,5,-5,10,-2,2,-9],[-6,-5,8,5,-1,-5,5,6,7],[7,-9,-8,2,1,-6,2,-1,-1],[5,2,-6,8,-9,5,-6,-7,-7],[-3,6,4,4,-6,-4,-3,2,5]],[[-2,-1,-5,-8,-3,7,1,10,6],[9,-9,-3,9,-2,-1,1,1,-6],[-8,-9,-9,-2,8,8,-3,4,-10],[-7,-6,2,-7,3,-4,-4,1,-5],[2,3,-9,-4,5,-6,-8,8,1],[1,4,6,1,2,5,-6,-7,7],[-7,-8,-10,9,-7,-1,-6,10,4],[-10,8,-9,-1,8,-2,-4,7,-1],[-8,6,-7,8,7,5,-4,6,-7],[2,2,6,8,-2,1,3,-6,-7]],[[-6,-10,2,6,-10,-5,1,-7,-9],[6,-2,-2,2,4,-6,2,-7,9],[-8,3,-1,-7,10,-3,6,8,-8],[10,-8,9,-7,-10,-5,-4,-5,-3],[7,-9,5,-6,1,-8,6,2,-4],[10,4,-6,10,-6,-6,1,10,-2],[2,-5,-2,6,2,-2,9,-8,3],[-3,-3,-7,-7,-4,-8,3,4,7],[-2,-6,8,-1,-9,1,-4,-4,-5],[-7,7,1,-6,7,4,-8,4,-1]],[[1,1,-10,3,-1,2,-7,-10,8],[2,-6,8,1,-6,-9,1,-8,3],[7,3,-2,-3,2,3,-5,-8,2],[-2,-9,9,-5,9,5,3,-7,-9],[1,-7,-5,5,-7,-2,-8,-3,-3],[6,-5,1,-8,-1,1,3,1,-7],[4,8,-6,10,5,10,8,-7,-2],[2,-5,4,-10,-9,10,-9,9,-4],[8,-8,7,-4,-7,-7,-1,10,9],[-3,-4,-2,-10,9,-10,6,-8,2]],[[4,10,7,2,-6,4,-8,-4,1],[7,9,-1,-10,9,-1,5,9,9],[-5,-3,-3,6,-6,-4,-10,-8,-6],[8,-8,-7,-9,6,-2,-3,-8,-7],[5,-4,8,10,8,5,-1,-3,-1],[7,3,-8,-2,1,7,-3,-5,-5],[-5,-9,7,9,10,-6,-2,-2,10],[-1,1,2,-4,-2,2,-2,-4,-1],[6,10,4,8,1,-3,2,-1,8],[2,-6,10,2,4,4,1,-7,-7]],[[-7,7,7,-6,7,-3,-1,-8,-7],[-5,-2,-9,6,8,8,-4,-2,-2],[-2,9,6,-6,-5,5,3,-3,1],[-1,9,-2,-5,-4,9,8,-4,3],[-1,10,1,9,5,1,3,7,-1],[1,-7,-5,-2,-10,-3,8,-9,-9],[-4,-8,-10,7,1,5,2,10,-2],[-4,1,1,-6,-6,-9,-9,3,10],[-4,-5,10,7,-8,9,-3,4,-8],[5,-6,-1,8,-6,7,2,-4,4]]], dtype = "uint8")#candidate|695|(11, 10, 9)|const|uint8
var_696 = relay.var("var_696", dtype = "uint8", shape = (11, 10, 9))#candidate|696|(11, 10, 9)|var|uint8
bop_697 = relay.greater(const_695.astype('bool'), relay.reshape(var_696.astype('bool'), relay.shape_of(const_695))) # shape=(11, 10, 9)
bop_705 = relay.right_shift(bop_697.astype('uint16'), relay.reshape(var_696.astype('uint16'), relay.shape_of(bop_697))) # shape=(11, 10, 9)
output = bop_705
output2 = bop_705
func_722 = relay.Function([var_696,], output)
mod['func_722'] = func_722
mod = relay.transform.InferType()(mod)
mutated_mod['func_722'] = func_722
mutated_mod = relay.transform.InferType()(mutated_mod)
var_723 = relay.var("var_723", dtype = "uint8", shape = (11, 10, 9))#candidate|723|(11, 10, 9)|var|uint8
func_722_call = mutated_mod.get_global_var('func_722')
call_724 = func_722_call(var_723)
output = call_724
func_725 = relay.Function([var_723], output)
mutated_mod['func_725'] = func_725
mutated_mod = relay.transform.InferType()(mutated_mod)
const_822 = relay.const(-2, dtype = "int8")#candidate|822|()|const|int8
var_823 = relay.var("var_823", dtype = "int8", shape = (8, 16, 4))#candidate|823|(8, 16, 4)|var|int8
bop_824 = relay.add(const_822.astype('int8'), var_823.astype('int8')) # shape=(8, 16, 4)
output = relay.Tuple([bop_824,])
output2 = relay.Tuple([bop_824,])
func_832 = relay.Function([var_823,], output)
mod['func_832'] = func_832
mod = relay.transform.InferType()(mod)
var_833 = relay.var("var_833", dtype = "int8", shape = (8, 16, 4))#candidate|833|(8, 16, 4)|var|int8
output = func_832(var_833)
func_834 = relay.Function([var_833], output)
mutated_mod['func_834'] = func_834
mutated_mod = relay.transform.InferType()(mutated_mod)
var_909 = relay.var("var_909", dtype = "float32", shape = (11, 15))#candidate|909|(11, 15)|var|float32
uop_910 = relay.log2(var_909.astype('float32')) # shape=(11, 15)
func_348_call = mod.get_global_var('func_348')
func_351_call = mutated_mod.get_global_var('func_351')
const_915 = relay.const([4.186233,-3.287408,-8.839275,-3.263623,-4.201966,-1.740313,-9.855894,0.443090,-4.267164,-1.475401,2.454531,-0.779650,3.029632,4.929021,5.238276,-8.036685,-3.396074,-6.985803,-7.298028,-9.494467,-1.459421,-5.979211,1.845424,-5.033389,-2.882577,6.982866,8.322777,-2.063027,3.816698,-3.477132,6.632264,9.445196,3.314268,1.674912,-1.362546,-7.872442,-5.237271,-1.690292,8.077869,2.058992,6.533012,0.751574,-0.044640,1.950736,9.398840,2.470075,1.477920,-8.583222,-0.557354,-2.601557,-8.650894,-2.401985,7.112647,-0.632943,2.412352,0.881289,-3.702717,1.970492,-9.611372,-0.162270,-7.975165,6.004071,-5.652132,-5.749517,5.961249,7.540492,-0.083011,-5.236119,-3.850550,-6.661821,-9.432945,-5.696319,-7.251958,3.503462,6.809688,-5.086620,7.595881,0.837122,-4.504809,9.730102,-5.660738,6.204832,-0.037518,0.627277,-8.577468,-3.851177,3.244455,1.833420,-6.727869,-9.917888,-2.653770,-4.817290,-3.865578,3.439540,9.050174,-0.779443,1.880535,-1.437016,9.667398,4.821133,8.745861,-6.250783,-4.989152,-3.529905,3.046672,-6.750154,-0.542911,1.777752,-9.598239,2.189606,6.256667,-9.364060,6.811846,-7.488638,-5.745997,-8.975215,8.528131,-5.668073,-6.341936,9.908251,8.947665,4.181062,-7.170968,9.535080,7.356128,-5.120525,-2.681900,6.497761,-2.484497,6.239694,6.207440,-1.279139,-6.922739,5.556089,-2.512062,-2.674188,-9.585121,3.572270,0.093502,-1.159641,8.402684,3.346044,3.610430,0.288899,2.234681,-6.850201,-6.774249,3.812900,4.619300,8.701139,9.522690,9.851108,9.263788,-4.950296,9.556674,9.557546,-6.474212,2.347377,2.309586,2.108276,3.288638,-6.885886,-1.886988,-9.623766,-1.847570,2.634397,-6.214771,5.865306,7.881487,-1.450869,-7.605932,4.164908,-2.935836,-4.105360,7.893624,-8.021812,1.337521,-9.451860,0.526802,0.878560,-7.557321,5.678286,-0.581189,-3.762427,9.805601,-7.968624,-0.117688,-4.570546,-0.939365,9.639979,-5.805879,-2.867312,-4.596701,0.731780,-9.619394,7.048307,-9.129435,0.433220,7.731151,-8.946840,-1.531168,5.054271,7.856944,4.832694,-1.837214,6.966198,8.084958,4.583130,2.593368,8.672159,0.444889,-9.513498,9.567371,-7.812133,-6.256237,9.371871,-2.625796,1.935388,-8.820018,7.351557,4.379178,6.833860,3.470072,-3.714258,-5.350333,-0.278546,-5.236597,7.536135,-3.791717,1.663467,-4.280318,7.987791,1.934734,-3.118857,1.735208,-9.530431,6.984306,7.365426,-7.838695,1.329972,2.109623,1.291719,-1.654665,-4.624364,-5.825436,7.748554,-8.570456,9.265796,-7.260994,-2.635820,-0.973185,-8.549092,-9.556235,-1.809978,-5.709697,9.535384,1.144356,8.325196,1.813117,-9.023287,0.591590,0.801252,-1.473325,1.984027,-6.685539,-0.080211,0.919517,-6.893781,2.213097,-0.388473,-8.877181,2.479644,-2.322948,-9.535085,-1.319712,-4.248469,-7.875449,-7.820353,-8.592728,1.821634,6.422140,5.457051,8.505448,-3.890211,-5.646102,-7.929170,8.453909,-8.802095,-2.984449,5.988948,8.117695,6.326499,4.051598,-9.231766,0.707112,6.680279,-4.464928,3.246235,-6.464650,-8.513556,9.938061,-6.308419,-7.017070,-3.299741,0.294543,-2.407016,8.674007,-1.709984,7.663970,5.830033,5.594864,0.762466,3.976458,6.722094,-3.775652,6.473034,-3.697288,-7.905956,-0.127304,9.815893,9.930731,5.336244,8.465721,0.684876,-1.404541,-9.806902,1.490974,1.051660,-5.805586,4.099031,-0.872762,-5.492787,-0.979968,-9.660905,-1.559111,-9.124073,7.724422,-6.706777,6.749669,8.194074,-0.890458,7.430787,2.147892,3.439659,9.959578,-2.582495,2.749606,-3.797802,-4.069342,-4.425983,8.675539,-6.203167,-1.366456,1.817983,-7.508508,-6.973521,-1.977763,5.024949,-1.971045,-3.923898,7.557325,-9.204059,5.417647,-8.337454,8.761549,-3.083495,7.334763,6.009787,-2.615332,8.606284,4.358255,0.737898,-4.119407,3.372670,5.323312,-9.551746,-3.074457,6.977583,-6.852644,8.361653,8.680979,-6.317247,-1.862142,-3.745277,-1.734080,-0.894103,6.447286,-6.648122,-8.321222,7.448769,3.628640,-2.471512,-6.029719,1.552465,6.554220,-1.363839,2.082231,9.580106,-4.920453,-9.158570,2.439619,-4.232124,-9.475737,-3.384519,-0.678065,5.274859,-0.253866,8.373047,6.429238,4.030178,-5.996757,1.034624,-1.576566,1.460127,2.669965,6.238905,-9.889347,4.535757,-8.849856,6.256070,3.849558,-2.853975,-8.446196,-0.977567,5.314347,-9.810982,8.562144,8.657662,-4.268020,-8.356197,-7.156552,2.382036,4.073895,0.818168,-3.743202,-6.188473,7.580355,3.134742,9.750001,-9.191634,9.865167,-6.170474,-4.572855,-2.240293,-1.797069,-5.372600,1.079704,-6.493295,4.408057,-8.499692,-9.212106,7.618279,-6.338288,-0.829515,6.490064,-5.044341,8.842481,1.932888,-9.517276,2.846987,0.950792,8.740343,0.969793,5.863673,3.464291,-4.542210,1.634618,-2.465307,0.697747,5.641507,2.153266,3.046916,-2.495611,-8.982066,1.416201,0.459343,-5.415719,7.739540,-6.735963,-1.742241,-9.465085,-6.465103,-0.311097,7.236897,0.806295,-0.665872,-0.672599,8.985475,3.794174,3.496193,0.873978,4.683954,0.222984,3.264093,6.210981,-2.172312,0.789708,4.109812,5.436954,2.339897,3.627068,1.615494,5.264122,-0.001501,-6.991406,3.798755,9.188831,8.117102,6.914877,-2.230714,-7.528247,3.423890,3.392857,-1.637161,0.145768,6.161241,8.296225,4.070568,-6.752671,8.693707,1.213603,-9.647816,0.865066,-0.894422,0.873581,-9.016007,9.450932,4.316052,-4.123213,6.419055,6.826905,9.981965,8.788321,5.133716,-4.528988,-7.469487,-3.443403,-0.348963,8.868430,-3.729519,-6.763206,-6.029829,-1.412415,-8.139925,0.648321,9.855970,0.841469,-3.938662,8.748055,-1.273892,-2.494573,3.646073,3.614184,8.643465,-9.020574,8.794141,-1.160670,-7.170215,8.031833,0.143373,-0.436942,8.803463,8.467044,-4.701040,-3.219021,5.377021,-7.490350,3.487401,-2.467239,-0.281557,-4.914649,0.878562,0.013802,-0.200369,4.307790,-3.596240,-6.072438,3.009076,3.556714,-0.164555,-2.785672,-6.761279,-9.651806,-2.971276,-7.909272,-4.806517,1.177484,3.018624,0.401405,7.053669,-4.058784,5.952755,-0.751348,-8.844802,-4.251954,6.580511,-2.757624,9.471419,9.440596,-9.229249,-7.882831,-7.482964,-3.525008,1.450272,1.265790,-6.440071,-8.338838,-9.419547,-9.055940,-2.339198,8.444887,8.828330,2.209378,7.641834,2.374230,9.011734,-5.890670,8.350245,3.403313,-3.707353,1.016155,-1.011198,-5.564799,-2.939247,-2.402271,-8.883126,-0.721536,7.428270,-3.552551,-1.310503,-6.290981,-3.907768,-7.083148,-4.665562,-9.071968,-4.347238,9.038656,6.094394,-3.271144,0.336318,-1.863403,-4.632005,2.690621,-9.591104,-6.096079,3.319989,-3.999725,4.979434,5.595990,6.791976,9.800841,-7.385584,-3.828478,-4.078015,0.595649,7.015788,1.403291,1.479846,-9.224262,4.183062,-3.171528,6.914409,-2.445120,7.116125,-5.662300,3.820579,7.231194,8.348471,7.888069,-2.793028,5.065441,-5.358305,1.228925,5.516409,5.716775,3.260954,-0.974391,3.498004,7.555407,-1.515703,8.517906,8.718491,7.335543,-2.462702,0.988816,-9.936648,8.545004,1.979142,-0.355546,-6.668045,0.103466,4.718944,-5.164234,-2.665582,-4.834038,-7.685962,-3.614960,-9.398054,-8.687479,-5.777599,9.921875,-5.987091,3.797172,1.395750,-1.949381,-2.818480,1.101234,8.816885,-8.085366,-5.826877,2.220044,-4.500624,-0.484961,2.233994,6.000579,-0.067986,-9.385823,5.330921,0.959800,7.420885,-4.045422,7.502899,-7.369471,-8.666342,4.919958,8.097608,5.624053,-8.498189,-6.597770,-9.805863,-6.351286,-3.711501,3.139041,-0.619898,-4.051407,-9.938548,6.847287,2.818464,9.114564,-5.027846,-2.909311,1.595654,0.681993,8.699203,4.455145,-7.789533,0.358550,5.816380,-8.389975,2.607573,2.328638,-5.420279,3.352547,-7.973661,1.289084,5.036915,-2.630017,6.354990,5.512635,8.094877,-8.714893,-0.694418,-2.500898,-4.211106,5.885473,-3.927210,3.773092,-4.327250,-6.060650,9.296746,0.447082,8.881099,4.709908,-7.557516,2.635862,-6.823814,9.977578,7.704674,-4.947381,-0.893476,5.722895,-9.500914,5.143666,-8.642234], dtype = "float32")#candidate|915|(784,)|const|float32
call_914 = relay.TupleGetItem(func_348_call(relay.reshape(const_915.astype('float32'), [8, 14, 7])), 0)
call_916 = relay.TupleGetItem(func_351_call(relay.reshape(const_915.astype('float32'), [8, 14, 7])), 0)
output = relay.Tuple([uop_910,call_914,const_915,])
output2 = relay.Tuple([uop_910,call_916,const_915,])
func_925 = relay.Function([var_909,], output)
mod['func_925'] = func_925
mod = relay.transform.InferType()(mod)
mutated_mod['func_925'] = func_925
mutated_mod = relay.transform.InferType()(mutated_mod)
var_926 = relay.var("var_926", dtype = "float32", shape = (11, 15))#candidate|926|(11, 15)|var|float32
func_925_call = mutated_mod.get_global_var('func_925')
call_927 = func_925_call(var_926)
output = call_927
func_928 = relay.Function([var_926], output)
mutated_mod['func_928'] = func_928
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1051 = relay.var("var_1051", dtype = "uint16", shape = (8, 5, 5))#candidate|1051|(8, 5, 5)|var|uint16
var_1052 = relay.var("var_1052", dtype = "uint16", shape = (8, 5, 5))#candidate|1052|(8, 5, 5)|var|uint16
bop_1053 = relay.multiply(var_1051.astype('uint16'), relay.reshape(var_1052.astype('uint16'), relay.shape_of(var_1051))) # shape=(8, 5, 5)
func_429_call = mod.get_global_var('func_429')
func_431_call = mutated_mod.get_global_var('func_431')
var_1059 = relay.var("var_1059", dtype = "float32", shape = (500,))#candidate|1059|(500,)|var|float32
call_1058 = relay.TupleGetItem(func_429_call(relay.reshape(var_1059.astype('float32'), [10, 10, 5])), 0)
call_1060 = relay.TupleGetItem(func_431_call(relay.reshape(var_1059.astype('float32'), [10, 10, 5])), 0)
output = relay.Tuple([bop_1053,call_1058,var_1059,])
output2 = relay.Tuple([bop_1053,call_1060,var_1059,])
func_1061 = relay.Function([var_1051,var_1052,var_1059,], output)
mod['func_1061'] = func_1061
mod = relay.transform.InferType()(mod)
var_1062 = relay.var("var_1062", dtype = "uint16", shape = (8, 5, 5))#candidate|1062|(8, 5, 5)|var|uint16
var_1063 = relay.var("var_1063", dtype = "uint16", shape = (8, 5, 5))#candidate|1063|(8, 5, 5)|var|uint16
var_1064 = relay.var("var_1064", dtype = "float32", shape = (500,))#candidate|1064|(500,)|var|float32
output = func_1061(var_1062,var_1063,var_1064,)
func_1065 = relay.Function([var_1062,var_1063,var_1064,], output)
mutated_mod['func_1065'] = func_1065
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1177 = relay.var("var_1177", dtype = "float32", shape = (5, 10, 15))#candidate|1177|(5, 10, 15)|var|float32
var_1178 = relay.var("var_1178", dtype = "float32", shape = (5, 10, 15))#candidate|1178|(5, 10, 15)|var|float32
bop_1179 = relay.subtract(var_1177.astype('float32'), relay.reshape(var_1178.astype('float32'), relay.shape_of(var_1177))) # shape=(5, 10, 15)
func_832_call = mod.get_global_var('func_832')
func_834_call = mutated_mod.get_global_var('func_834')
const_1184 = relay.const([8,4,1,-7,2,6,5,9,6,-9,10,10,6,8,-7,-1,-10,4,-6,-4,7,6,-5,1,6,6,5,-8,5,2,-4,8,-10,5,-3,4,-1,5,-5,1,-6,7,-2,-10,-2,10,-9,-2,-1,7,-8,-6,-1,-6,7,6,-4,-3,-10,5,9,-2,4,-1,2,8,9,8,-7,6,4,7,7,-6,5,2,9,-2,7,9,-1,9,5,4,4,5,-2,-7,10,-9,-7,9,-7,2,-4,3,-9,9,-2,5,-3,-5,1,-7,5,6,-6,-1,-5,7,3,-9,4,8,1,1,4,-10,-10,-7,-2,9,7,-1,3,4,-9,10,-10,-9,-4,6,8,2,-2,5,4,-2,-5,5,-2,-4,1,6,2,6,-6,3,-8,-6,-6,4,6,-10,10,9,-4,7,-6,-9,-6,4,7,10,4,10,8,9,2,4,-5,-8,-3,4,-7,8,10,-7,-9,6,4,3,-2,5,10,-9,-10,3,1,-3,-4,2,-2,3,-8,3,5,-6,-8,2,-10,-4,6,-6,-7,-5,-9,-5,6,10,-6,-9,-1,-9,-8,9,-2,10,10,-6,2,-6,-8,2,8,1,-7,5,7,-6,-5,-5,-8,4,1,-3,-1,6,1,-5,-9,2,-7,3,3,1,6,4,10,-2,-7,-6,5,8,-9,6,9,4,-7,2,-10,-7,-8,2,8,-1,-10,-3,-8,-2,6,-6,8,-3,-9,-2,-9,-5,9,-8,-3,1,-7,-8,-9,-3,8,2,-9,10,1,7,2,-8,1,-7,-5,6,5,7,4,-9,-9,-10,-7,4,-2,-7,-5,5,-10,-8,1,5,8,9,1,-4,-10,-7,-5,-4,-4,-1,-5,4,-9,10,-6,5,6,4,4,8,-4,-1,-9,-6,-8,-1,5,10,-8,3,5,6,6,9,-9,3,3,2,1,-5,7,3,3,-6,-2,-5,-1,-8,-4,-6,-7,6,-5,2,-6,-6,-6,5,-10,2,-1,1,-9,-8,8,-8,3,5,-4,-7,-7,-3,1,4,-10,7,3,-5,7,-9,-7,1,1,-9,6,-5,-10,8,6,-5,6,8,-2,-6,-6,5,2,-5,-4,7,-2,-5,-1,-4,-2,-3,-4,2,6,2,-4,5,-5,-6,5,-10,-6,-9,-7,5,-5,10,1,-3,1,-9,4,-9,-4,-9,10,8,-4,4,4,-1,-10,-8,2,-10,-1,-5,4,-6,-1,-9,-4,-9,-8,10,-4,2,-3,-9,-6,-7,9,-1,-8,-3,-4,1,3,-8,3,-4,-10,-5,9,-5,2,-1,6,3,-1,-2,-9,10,-3,3,-6,-6,-5,7,-2,8,-6,4,1,7,-4,-4,4,-6,-4,-4,6,-9], dtype = "int8")#candidate|1184|(512,)|const|int8
call_1183 = relay.TupleGetItem(func_832_call(relay.reshape(const_1184.astype('int8'), [8, 16, 4])), 0)
call_1185 = relay.TupleGetItem(func_834_call(relay.reshape(const_1184.astype('int8'), [8, 16, 4])), 0)
var_1192 = relay.var("var_1192", dtype = "float32", shape = (5, 10, 15))#candidate|1192|(5, 10, 15)|var|float32
bop_1193 = relay.floor_divide(var_1178.astype('float32'), relay.reshape(var_1192.astype('float32'), relay.shape_of(var_1178))) # shape=(5, 10, 15)
func_722_call = mod.get_global_var('func_722')
func_725_call = mutated_mod.get_global_var('func_725')
const_1204 = relay.const([[6,5,2,9,9,10,2,9,-7],[5,-1,-1,-9,-10,-6,9,4,6],[-2,-10,4,-2,-3,4,-4,-9,9],[-7,-8,7,9,8,4,9,-10,-8],[-2,3,-3,-5,-6,-3,6,-5,1],[10,2,1,-1,1,-3,8,-9,-9],[7,-1,-10,-2,-6,-1,-1,-7,9],[10,-10,3,-9,-9,3,-3,3,5],[-10,-2,-6,-3,5,1,-8,4,-1],[3,10,-2,-9,-3,-1,-10,7,-9],[-6,-3,2,5,-4,-2,-7,-9,-5],[10,-8,-8,3,-1,-1,-5,-3,-8],[-2,-9,-3,5,3,7,-5,-6,1],[-5,2,-7,6,-10,2,-6,-2,-3],[3,4,-2,-8,9,-3,7,-7,1],[4,5,8,3,-2,-8,-9,-4,1],[-6,-4,-2,-7,2,10,7,-3,-9],[2,7,-4,-10,8,-7,-8,9,-8],[-7,-1,-1,4,-8,-10,10,-6,5],[-1,-6,7,-9,4,8,-10,1,6],[6,-7,9,-9,9,-3,9,9,5],[9,-2,-4,7,9,-9,9,7,10],[-3,-2,-8,7,8,-3,2,9,-6],[-6,10,10,-10,-5,-5,10,5,10],[-6,-1,3,-7,7,-8,-10,-6,10],[10,-7,7,-9,1,9,-7,8,-9],[-3,5,2,-5,-2,1,-8,-1,5],[6,7,9,-9,-10,6,10,-6,3],[2,10,-8,-5,-1,1,6,-1,-7],[8,-9,-4,6,6,1,-9,7,7],[10,4,-8,-9,-4,-5,3,8,-2],[8,-8,-9,6,-2,-7,10,10,-1],[1,-3,2,-8,1,-6,-10,-10,-9],[-7,-1,9,9,7,5,8,-10,3],[-8,5,-8,-2,-7,5,5,2,1],[4,-3,9,-1,-6,-7,10,-9,-7],[-8,-5,3,-3,-2,-4,6,-4,1],[9,-2,2,3,7,9,-8,2,3],[3,-4,1,-9,6,-6,-9,-8,9],[2,-3,5,-4,-10,8,4,1,6],[3,-9,-9,5,-1,10,-2,1,3],[7,8,-8,3,8,9,6,-1,1],[9,9,9,-9,2,-8,7,-6,5],[3,-5,3,-7,6,-1,10,-2,-1],[6,4,1,3,-7,3,3,1,-9],[10,1,-5,-2,4,4,7,-5,-8],[-2,4,-1,1,-7,2,5,1,7],[-10,-3,-2,-2,-4,9,5,4,9],[8,-1,-2,-10,-4,-5,-9,1,1],[-8,4,2,-6,5,8,-7,-5,1],[1,4,-6,-8,4,-8,5,-8,8],[2,-6,-5,-2,1,3,5,-5,1],[10,8,-1,8,10,8,-7,3,-9],[8,-1,7,2,7,-2,1,-2,-5],[3,10,1,-3,-8,2,5,9,10],[9,9,-9,6,1,9,2,1,-7],[-10,3,-7,7,6,7,1,5,-3],[1,4,-9,9,-5,3,-5,4,-3],[2,2,-6,-3,4,7,2,-7,9],[1,5,-10,-10,1,2,3,-4,3],[4,6,-4,5,2,-4,8,-9,-3],[-3,-4,5,8,2,-6,3,1,-10],[-4,-2,-7,-7,6,-9,-5,-2,-7],[-2,6,9,1,2,1,8,8,-2],[-10,1,-5,3,-3,8,1,-6,-6],[-10,7,8,5,5,-5,8,8,-9],[10,-2,8,-4,9,-7,5,1,-9],[-9,-2,6,3,-3,3,-3,-8,7],[-4,5,3,10,7,-9,10,-1,-4],[2,-2,6,8,10,4,-2,-10,-4],[8,10,-7,4,-7,-2,3,-6,-8],[2,-2,4,2,6,2,5,-4,-7],[-4,-10,7,1,3,-7,-4,1,-3],[-3,2,9,9,-5,-8,6,3,-2],[8,-2,-5,-4,-10,-4,-1,-10,-6],[8,-10,10,5,-10,4,1,-9,2],[4,2,4,-8,5,-9,-4,8,-8],[-4,6,1,7,-1,5,-10,-1,4],[10,-2,8,8,6,8,4,-7,7],[2,10,-2,-9,5,-7,-7,8,4],[9,-10,5,9,1,4,3,-3,1],[7,2,-4,-10,-7,-10,-6,2,6],[-3,9,-10,-1,-10,4,-4,3,-5],[-4,-8,7,4,9,-9,-3,9,-6],[6,-9,-6,8,-8,-5,-10,9,-1],[-5,10,-9,8,-1,4,3,-7,-4],[7,-4,-7,-7,-7,4,-5,-1,3],[-1,-1,-6,-10,-3,-3,-1,-3,5],[-3,6,1,5,8,-8,-7,-2,3],[-1,8,1,5,2,-8,-7,-9,8],[2,5,-1,-1,-4,-7,4,10,-4],[-5,-5,-6,-6,-4,5,-7,9,-6],[-7,-1,1,-9,-7,-9,2,-1,-3],[-1,-9,5,1,10,-6,-2,-3,-5],[10,9,3,-10,2,-3,8,3,1],[1,2,1,8,-2,-6,-7,-10,-6],[6,9,7,2,-6,-3,5,-10,-7],[-6,4,-10,-4,1,-3,9,2,7],[10,5,6,-4,3,-1,-4,-7,-4],[3,4,-4,-10,6,2,3,5,-1],[-7,-6,-8,-3,4,3,7,-6,9],[-9,6,10,1,2,-3,-8,10,1],[1,-2,-3,10,2,-2,7,-9,7],[3,-5,3,-9,-8,-5,7,-10,8],[6,5,6,-7,9,8,-7,3,7],[10,4,-3,5,-4,10,10,2,2],[-3,2,6,5,2,-5,-3,-5,1],[8,9,-2,-6,3,-8,-7,-5,-2],[-3,-6,6,-4,-4,-7,-8,-2,-7],[-5,7,-4,-4,-7,-1,4,7,-9]], dtype = "uint8")#candidate|1204|(110, 9)|const|uint8
call_1203 = func_722_call(relay.reshape(const_1204.astype('uint8'), [11, 10, 9]))
call_1205 = func_722_call(relay.reshape(const_1204.astype('uint8'), [11, 10, 9]))
func_429_call = mod.get_global_var('func_429')
func_431_call = mutated_mod.get_global_var('func_431')
const_1207 = relay.const([1.372604,-3.233782,-1.571203,4.550086,-9.960228,7.217973,1.893278,5.837514,5.254650,-2.786290,0.385183,-8.441362,6.496202,-6.410745,8.286274,-4.885667,-8.164386,4.402226,-1.345914,5.284345,-5.024996,0.077083,1.751257,-3.070056,7.637127,-4.443347,9.731865,-7.443264,-4.902867,7.012066,-1.242074,-6.412848,-3.690501,3.043903,-0.267038,3.620950,5.793398,-5.647388,6.624222,7.531967,8.100193,9.367949,-0.321148,6.404128,-6.145313,7.916404,-3.446029,7.459076,1.561591,-3.489714,4.140545,-0.363670,-2.802094,7.069339,1.960558,-5.390954,-9.237455,3.997421,6.363592,7.071962,2.640610,-4.208047,4.440817,2.249275,-8.783090,-8.718260,0.237516,-4.717366,-2.677751,-8.849030,-7.522601,-2.885878,-6.207168,-5.041556,0.211308,-0.919290,-2.500942,-2.705548,-1.336077,-6.500170,2.261036,0.663464,4.395339,-9.140850,9.319702,7.253346,0.277155,9.605028,-5.193732,6.214356,2.057054,-5.819529,-7.551222,9.616797,-3.938935,6.145427,2.698869,2.037391,-1.776260,-7.162277,-2.873656,-2.169991,3.537555,3.076362,7.485299,8.463463,-9.385828,-0.748278,9.485121,-8.805565,5.058283,2.262471,-5.084297,9.980102,2.649517,-9.554945,7.689175,7.357041,-0.812264,-9.992860,-4.835387,4.936335,-1.475735,5.720602,0.464709,2.449735,-2.925485,4.157527,3.939815,6.054574,-4.575548,-1.684921,-2.453879,6.037791,2.889487,-5.692992,0.522453,-4.205504,1.223904,7.310801,3.683086,5.667813,-9.899522,-6.114478,7.504212,-5.510283,-9.848860,-0.735431,-5.624241,2.374378,1.133158,2.848020,0.190793,-3.897967,-4.156671,-8.744116,6.949338,1.898568,-1.599497,4.054501,4.291727,-5.582733,7.203073,8.240602,-9.137407,5.827072,-2.298916,-0.268700,-5.988092,8.743551,3.789958,9.103671,9.144625,-1.700547,-2.652008,-6.510537,1.123053,2.029170,4.538420,-2.728027,-7.836581,1.861851,4.457249,-3.838423,0.937222,-3.648264,4.480084,2.291676,-1.653015,1.147946,9.381124,-7.010944,-1.411277,4.447714,-2.810444,2.371068,9.479237,-9.023414,-3.517395,7.900584,-2.985369,-4.890339,4.979846,-5.030303,4.234573,-4.659785,7.618918,1.466933,5.085704,1.055647,0.803448,-6.298709,-6.092741,0.751349,1.671892,-9.908649,-2.305568,-2.236246,-7.480872,9.732885,-4.564444,-4.610679,-2.894127,3.850428,9.321961,-5.564509,4.420340,4.223995,9.089561,-4.441265,6.119620,-0.752119,-0.401982,2.498304,1.256483,-7.496838,5.064892,-9.070819,4.452627,8.206473,-0.748423,7.860246,-7.576024,1.958183,9.970250,-8.550682,-1.874083,-5.797985,7.395357,6.030055,-4.535546,-9.716208,6.694361,1.765052,-8.081146,9.984955,-8.016291,-6.422645,5.469751,-6.926526,-3.040191,-3.058732,9.642957,3.670436,-3.351338,-1.488295,-6.725209,-3.498315,0.040202,-3.969026,-7.669521,-0.614450,-3.500248,7.942560,8.799699,-9.809085,1.009711,-6.658068,1.928539,0.002062,4.782036,-3.906347,0.962169,5.143628,4.094131,-4.327123,5.203171,-8.635252,-6.669613,2.879184,-3.190948,3.589749,-0.326255,-6.022188,0.745801,-5.921665,6.869210,-9.371477,6.891314,6.836600,-5.364655,7.460287,9.068894,2.231630,1.177993,1.479273,9.744386,3.433829,-3.341175,5.534124,-6.890970,-5.232286,7.823065,-3.428534,-1.971479,4.886591,1.553917,-3.580720,-0.408784,-8.341889,3.877597,1.330741,-4.996228,-6.233280,5.775753,-1.506063,5.907112,8.531494,-6.040696,-8.151457,-2.351523,6.800636,-2.600148,-8.461738,5.253793,-1.030990,-3.103486,5.603789,1.630677,2.808241,-0.514444,-5.541769,9.181308,-4.932380,0.974821,-9.913427,-0.123103,2.136450,-8.318869,6.110511,0.368555,-6.811939,-8.133178,-1.819377,4.619624,-4.144623,-3.142176,-9.557103,-1.282411,2.297966,6.889117,8.363334,0.118993,-4.309825,-1.621107,4.905203,6.130146,3.812400,-9.671099,2.160669,-9.622512,6.276527,-4.666466,-6.252918,-4.590090,-6.948028,5.120404,5.527736,5.898640,-7.126766,4.472824,9.961197,1.954309,-3.993979,-2.716657,-2.438146,0.660166,4.785973,5.115091,7.780704,7.546206,1.331744,6.431793,4.975765,-7.010936,0.052947,-0.844921,-7.040092,3.220976,0.039175,6.886922,-2.425920,4.173222,-2.734223,3.325983,-2.247712,-7.908021,-2.250959,-7.697872,-9.540089,7.988718,-1.718017,-2.457589,-2.595548,-7.501735,3.216588,7.167878,-2.703219,-8.441755,4.322251,-6.860465,-3.439237,0.502289,1.352697,4.943881,-9.081377,0.671540,-2.048602,6.673364,9.146738,-8.097648,8.590546,8.224899,-2.038876,0.830934,6.506033,1.639424,-9.922782,-8.668472,-9.520102,8.925024,0.924901,9.250021,-8.628015,-4.929748,-0.113245,-3.287659,-6.276370,-4.412971,3.281746,-2.174443,2.189428,6.318666,-5.698444,4.203378,5.737159,6.776253,1.061087,-4.331118,2.026998,-0.524598,7.474851,-8.223312,-4.879349,-2.780770,-6.108707,-3.918120,-7.769302,5.017498,-8.842505,1.422679,9.130354,-4.478223,3.759205,-1.786998,3.104446,8.827151,5.564794,-3.091933,-8.334594,-5.192159,1.816171,-8.142386,-3.564225,-8.213777,4.376820,-5.494015,-2.618210,7.546960,1.517315,-2.373765,-4.368034,0.855366,9.442171,6.159232,-1.864498,-5.121711,5.032031,4.102758,-1.872031], dtype = "float32")#candidate|1207|(500,)|const|float32
call_1206 = relay.TupleGetItem(func_429_call(relay.reshape(const_1207.astype('float32'), [10, 10, 5])), 0)
call_1208 = relay.TupleGetItem(func_431_call(relay.reshape(const_1207.astype('float32'), [10, 10, 5])), 0)
output = relay.Tuple([bop_1179,call_1183,const_1184,bop_1193,call_1203,const_1204,call_1206,const_1207,])
output2 = relay.Tuple([bop_1179,call_1185,const_1184,bop_1193,call_1205,const_1204,call_1208,const_1207,])
func_1209 = relay.Function([var_1177,var_1178,var_1192,], output)
mod['func_1209'] = func_1209
mod = relay.transform.InferType()(mod)
mutated_mod['func_1209'] = func_1209
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1209_call = mutated_mod.get_global_var('func_1209')
var_1211 = relay.var("var_1211", dtype = "float32", shape = (5, 10, 15))#candidate|1211|(5, 10, 15)|var|float32
var_1212 = relay.var("var_1212", dtype = "float32", shape = (5, 10, 15))#candidate|1212|(5, 10, 15)|var|float32
var_1213 = relay.var("var_1213", dtype = "float32", shape = (5, 10, 15))#candidate|1213|(5, 10, 15)|var|float32
call_1210 = func_1209_call(var_1211,var_1212,var_1213,)
output = call_1210
func_1214 = relay.Function([var_1211,var_1212,var_1213,], output)
mutated_mod['func_1214'] = func_1214
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1547 = relay.const([[[-9,2,2,1,-5,4,-5,-7,-4,-7,-4,8,-10,2,-3],[5,1,-3,-7,-7,-3,10,-9,-2,3,1,-4,1,4,-3],[4,10,-3,-2,-7,5,-1,7,1,-5,1,-4,-7,-8,-10],[-7,-6,4,9,-2,-7,6,3,8,-7,8,8,-2,7,-5],[2,5,-10,9,-5,6,9,9,-9,4,7,3,-4,-2,8],[1,-1,10,-5,9,-10,-1,-8,1,-7,-3,-6,10,5,2],[9,-3,-10,-10,-4,5,5,-4,-8,2,9,10,4,-9,3],[-2,5,-3,-10,9,3,7,4,4,-8,7,-4,5,6,6],[-7,10,-8,8,7,2,-5,-1,-4,-9,3,-10,-3,-2,-10],[6,1,-1,10,-6,9,8,-1,-3,6,-5,-7,4,1,7],[-8,-9,1,-5,9,10,1,4,-9,-5,8,-1,-7,5,3],[-7,8,-10,-8,-10,8,9,-7,3,7,-10,10,-1,8,-2],[9,2,9,-6,8,-6,-7,-8,-5,2,-9,-8,-6,5,-5]],[[5,-8,3,10,4,7,-6,2,-1,-5,2,7,-2,-7,7],[3,7,-8,9,-10,-7,3,-1,7,4,5,7,-6,-5,7],[-6,-3,-4,-3,-10,-7,8,-2,7,-1,3,-8,9,3,-8],[5,3,-7,10,3,1,-9,-10,-7,2,7,-3,-8,-9,-6],[1,1,1,4,-7,3,5,-6,5,-3,1,-4,6,-9,-5],[2,-6,2,2,-1,3,7,-6,-4,-8,9,6,8,-5,7],[-1,8,5,-7,5,5,9,-5,-9,-7,-7,-8,8,-5,2],[5,-4,-1,2,-5,5,5,6,-1,3,1,2,3,5,7],[1,-1,4,5,9,2,-1,-9,1,9,-8,3,2,-2,-5],[4,-10,4,-6,-9,-8,10,2,-4,7,-8,-6,7,-9,4],[-9,-4,5,4,-5,-8,-7,-10,-6,-3,-2,10,-4,-5,-7],[8,9,-6,10,-8,4,-7,4,10,-6,5,-2,5,5,8],[10,7,-10,6,2,4,-9,6,10,3,7,-3,6,-6,7]],[[2,-1,-9,-3,-10,10,-10,-5,-2,2,-1,7,9,-2,-6],[-10,10,-9,-2,-3,-9,6,-2,8,6,-3,-9,4,6,3],[-7,-10,4,-6,-4,-1,-4,4,8,3,-2,-4,7,-8,-4],[-4,-6,9,-8,8,-6,6,-6,7,10,1,-6,-2,-4,5],[3,-10,4,9,-6,3,-6,5,9,9,4,3,6,3,6],[-10,5,-8,-1,2,-3,-1,-6,-4,-10,4,4,2,-5,-2],[2,1,-1,-10,-3,-10,-9,-7,7,10,4,-9,-3,10,7],[8,1,-1,-6,3,-3,-8,-3,-7,-4,-10,-1,7,-4,-2],[9,2,-9,2,-4,-7,-9,-9,-7,7,-3,2,-5,-8,7],[10,9,-6,5,-4,-5,3,-3,6,-1,5,-9,-8,7,-3],[-5,8,7,10,2,-10,-2,-10,-7,9,9,-10,9,5,3],[10,-1,9,2,9,-3,2,-1,-4,-9,6,5,8,-3,1],[9,3,-10,9,2,-8,6,-4,-2,-5,9,9,-9,-9,-8]],[[-10,10,10,-6,3,-6,4,-3,-10,7,4,-7,10,-1,-10],[-7,-7,-4,8,7,-9,-4,-6,-1,10,10,-4,10,-4,-2],[10,-5,-10,-6,-8,-2,8,9,-3,-8,10,10,8,-9,8],[9,5,-7,-2,5,-9,-6,-3,9,-9,10,7,-5,-7,-9],[8,-5,3,-9,-8,-6,1,2,-9,1,-9,7,-8,-1,7],[-2,-10,-1,10,8,6,4,6,-3,-6,4,5,1,4,-10],[4,9,10,6,9,9,8,3,7,2,2,9,7,-5,-4],[3,9,-5,-1,-1,7,-6,-1,-10,6,-4,-7,-8,-4,5],[-9,9,10,7,5,2,7,-6,10,1,-9,6,7,-10,8],[1,2,5,4,-5,-1,-8,6,1,1,4,4,-3,6,3],[7,-3,-6,4,10,8,6,-2,-1,10,2,9,4,8,-7],[5,-9,-4,-9,-6,8,2,3,6,-6,5,10,7,-9,-5],[-8,-10,-1,3,-5,-8,-6,-6,-6,-4,-1,-2,4,-7,6]]], dtype = "int8")#candidate|1547|(4, 13, 15)|const|int8
var_1548 = relay.var("var_1548", dtype = "int8", shape = (4, 13, 15))#candidate|1548|(4, 13, 15)|var|int8
bop_1549 = relay.right_shift(const_1547.astype('int8'), relay.reshape(var_1548.astype('int8'), relay.shape_of(const_1547))) # shape=(4, 13, 15)
output = relay.Tuple([bop_1549,])
output2 = relay.Tuple([bop_1549,])
func_1553 = relay.Function([var_1548,], output)
mod['func_1553'] = func_1553
mod = relay.transform.InferType()(mod)
var_1554 = relay.var("var_1554", dtype = "int8", shape = (4, 13, 15))#candidate|1554|(4, 13, 15)|var|int8
output = func_1553(var_1554)
func_1555 = relay.Function([var_1554], output)
mutated_mod['func_1555'] = func_1555
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1925 = relay.var("var_1925", dtype = "uint16", shape = ())#candidate|1925|()|var|uint16
var_1926 = relay.var("var_1926", dtype = "uint16", shape = (8, 5, 11))#candidate|1926|(8, 5, 11)|var|uint16
bop_1927 = relay.minimum(var_1925.astype('uint16'), var_1926.astype('uint16')) # shape=(8, 5, 11)
bop_1936 = relay.add(var_1925.astype('uint8'), bop_1927.astype('uint8')) # shape=(8, 5, 11)
func_832_call = mod.get_global_var('func_832')
func_834_call = mutated_mod.get_global_var('func_834')
var_1940 = relay.var("var_1940", dtype = "int8", shape = (512,))#candidate|1940|(512,)|var|int8
call_1939 = relay.TupleGetItem(func_832_call(relay.reshape(var_1940.astype('int8'), [8, 16, 4])), 0)
call_1941 = relay.TupleGetItem(func_834_call(relay.reshape(var_1940.astype('int8'), [8, 16, 4])), 0)
output = relay.Tuple([bop_1936,call_1939,var_1940,])
output2 = relay.Tuple([bop_1936,call_1941,var_1940,])
func_1954 = relay.Function([var_1925,var_1926,var_1940,], output)
mod['func_1954'] = func_1954
mod = relay.transform.InferType()(mod)
mutated_mod['func_1954'] = func_1954
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1954_call = mutated_mod.get_global_var('func_1954')
var_1956 = relay.var("var_1956", dtype = "uint16", shape = ())#candidate|1956|()|var|uint16
var_1957 = relay.var("var_1957", dtype = "uint16", shape = (8, 5, 11))#candidate|1957|(8, 5, 11)|var|uint16
var_1958 = relay.var("var_1958", dtype = "int8", shape = (512,))#candidate|1958|(512,)|var|int8
call_1955 = func_1954_call(var_1956,var_1957,var_1958,)
output = call_1955
func_1959 = relay.Function([var_1956,var_1957,var_1958,], output)
mutated_mod['func_1959'] = func_1959
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2265 = relay.var("var_2265", dtype = "float32", shape = (15, 8, 9))#candidate|2265|(15, 8, 9)|var|float32
uop_2266 = relay.cosh(var_2265.astype('float32')) # shape=(15, 8, 9)
output = relay.Tuple([uop_2266,])
output2 = relay.Tuple([uop_2266,])
func_2269 = relay.Function([var_2265,], output)
mod['func_2269'] = func_2269
mod = relay.transform.InferType()(mod)
mutated_mod['func_2269'] = func_2269
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2270 = relay.var("var_2270", dtype = "float32", shape = (15, 8, 9))#candidate|2270|(15, 8, 9)|var|float32
func_2269_call = mutated_mod.get_global_var('func_2269')
call_2271 = func_2269_call(var_2270)
output = call_2271
func_2272 = relay.Function([var_2270], output)
mutated_mod['func_2272'] = func_2272
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2346 = relay.var("var_2346", dtype = "float64", shape = (2, 12, 1))#candidate|2346|(2, 12, 1)|var|float64
uop_2347 = relay.cos(var_2346.astype('float64')) # shape=(2, 12, 1)
func_1954_call = mod.get_global_var('func_1954')
func_1959_call = mutated_mod.get_global_var('func_1959')
var_2350 = relay.var("var_2350", dtype = "uint16", shape = ())#candidate|2350|()|var|uint16
const_2351 = relay.const([10,-7,-3,-1,-10,-5,-8,3,-9,-5,-7,10,-5,-4,2,3,-1,-4,9,1,4,2,-8,-7,9,-6,9,4,9,-4,7,-4,10,-3,3,-10,9,9,8,4,2,-2,6,-6,3,-7,-9,-9,6,8,5,8,-10,3,5,-5,-7,-9,-4,9,4,10,-6,-10,10,-4,6,2,1,3,-3,4,-5,7,7,-7,-4,4,-7,-4,2,3,-2,-5,-10,-10,9,5,8,-5,9,-7,10,-3,-6,3,5,-10,-3,-1,-5,10,-6,8,-8,-2,-5,-10,-10,2,-9,8,3,10,-2,2,1,-1,-6,2,4,-1,-3,-5,-3,3,-2,-8,8,2,9,9,-6,1,-3,-8,-9,7,-1,6,-9,-7,-1,-7,-3,1,5,-5,2,4,9,2,10,-9,-2,-6,6,-2,-6,-6,-2,-2,6,-7,-3,6,3,-9,7,-4,5,-10,3,7,-4,10,-9,2,-2,-6,2,-9,1,-7,-6,-9,-1,1,2,-3,1,10,-8,5,-3,-6,-4,7,-5,-6,-5,3,4,2,-3,2,-10,4,-5,9,2,3,2,-1,-6,9,2,9,-7,-1,6,4,6,-4,-7,-2,-10,-4,7,-1,-4,4,2,3,-6,10,10,8,2,-10,6,-7,-7,9,10,-4,-10,-2,6,4,2,4,7,-9,-7,-5,8,-9,5,-8,-10,9,3,-4,7,-8,1,-2,-7,5,-9,-7,4,-4,6,4,-4,-5,6,-3,5,-3,-7,-5,7,10,-2,-5,-5,-7,-10,-6,-6,1,-10,5,10,-4,-5,3,8,-10,-10,-7,3,-7,-5,-9,-6,2,-7,-5,-7,3,-7,5,-8,8,-1,5,8,-9,7,-5,8,-10,6,-1,-4,8,9,-9,-10,8,-9,-5,7,2,-2,4,6,-7,9,5,2,-5,7,-1,8,-8,2,-5,-7,-10,4,1,10,-2,5,2,-1,8,8,6,-9,-2,10,-10,6,8,-6,10,8,-6,-1,10,-3,3,10,-7,6,1,-9,-4,1,-7,-2,6,10,3,-8,3,-5,-3,6,7,-1,9,-9,7,5,-8,10,7,6,1,-6,7,1,-8,4,-10,-4,-7,9,3,-9,-1,9,-8,7,-10,4,-6,-9,-3,-2,10,-1,8,-2,-6,-6,-9,-4,-9,-8,5,8,8], dtype = "uint16")#candidate|2351|(440,)|const|uint16
var_2352 = relay.var("var_2352", dtype = "int8", shape = (512,))#candidate|2352|(512,)|var|int8
call_2349 = relay.TupleGetItem(func_1954_call(relay.reshape(var_2350.astype('uint16'), []), relay.reshape(const_2351.astype('uint16'), [8, 5, 11]), relay.reshape(var_2352.astype('int8'), [512,]), ), 2)
call_2353 = relay.TupleGetItem(func_1959_call(relay.reshape(var_2350.astype('uint16'), []), relay.reshape(const_2351.astype('uint16'), [8, 5, 11]), relay.reshape(var_2352.astype('int8'), [512,]), ), 2)
func_297_call = mod.get_global_var('func_297')
func_302_call = mutated_mod.get_global_var('func_302')
var_2372 = relay.var("var_2372", dtype = "float32", shape = (432,))#candidate|2372|(432,)|var|float32
const_2373 = relay.const([-10,-4,3,2,1,10,-7,7,-7,-7,-9,-9,-1,9,7,-3,-2,-4,10,2,3,9,2,-2,-10,5,-3,-2,-9,-2,-4,5,-4,2,-4,9,4,-9,-4,7,-9,-3,1,7,-8,-8,6,8,-10,-5,-5,-4,-2,5,-4,-2,-9,7,2,-9,5,-5,-9,-2,-5,5,-1,9,2,1,-8,-2,10,4,3,4,-9,8,4,-10,7,1,4,3,-1,5,7,-6,-5,1,-4,-4,6,2,2,-2,-7,8,10,1,-6,-3,-2,-2,-9,-4,1,-5,-2,8,-1,2,3,3,-1,-7,9,-2,8,9,-10,-8,3,-8,2,-8,8,3,1,-7,10,-1,-3,-1,10,6,-3,1,-8,10,4,-5,9,4,-3,4,4,-2,10,-5,3,2,-8,1,-9,7,6,-8,1,-5,-2,10,6,-4,-7,-9,-2,6,2,-5,-6,-6,6,7,7,-6,3,-6,9,-5,9,-5,-5,-9,8,-7,8,-7,9,-6,8,-5,7,1,-9,10,-2,-9,8,3,-3,8,-6,-10,9,-9,-5,1,6,-7,2,-3,4,1,-1,8,5,-7,-3,5,-2,-2,-9,-10,6,-9,7,-5,5,5,-2,-2,-10,-9,-8,6,9,7,-2,-4,-6,-7,9,4,-9,10,3,-10,10,8,4,-8,-4,2,3,2,-2,-2,2,5,-6,-3,-6,2,2,4,3,-8,6,-3,-9,8,-6,2,-6,-1,1,-1,-9,-3,-2,7,-6,4,-9,8,-4,9,7,-7,-8,5,-4,-6,-9,4,-3,-1,-7,8,-4,2,-5,5,4,-4,2,-2,6,-1,-5,8,-5,-7,-6,6,5,5,3,-9,5,9,-3,-6,-7,5,2,-1,2,9,5,5,7,8,-1,-5,2,-6,5,5,-8,5,4,9,4,-2,-3,-8,9,10,-5,-8,9,6,-5,7,1,-5,7,-1,-2,-3,1,5,9,10,2,-3,-2,-4,-9,-2,2,7,9,-4,10,6,-9,9,-8,-2,-9,-1,5,7,6,-6,7,2,1,9,-3,1,7,10,1,8,-6,-10,-4,-4,-8,-3,-6,-3,8,6,-6,-5,-7,10,6,7,-7,-4,-5,5,1,-10,-2,-3,4,4,-6,-3,-4,10,-3,4,3,-2,8,-4,7,7,-7,-10,10,9,2,1,-8,-6,8,-2,-7,1,-4,-4,9,10,2,6,-3,1,8,-1,-3,-9,6,3,-6,9,-1,2,-6,7,2,1,-10,-1,4,-5,9,-9,-5,-10,-9,2,-4,4,-5,-8,-6,-2,-3,5,5,4,3,-10,-6,-1,9,-6,6,-3,-1,-7,9,-3,2,-10,7,-10,-9,-1,1,1,3,-3,7,1,-4,-7,10,7,-6,-7,-3,5,7,9,10,-8,-7,-4,-4,4,-3,-2,1,-5,8,-1,-8,5,4,5,-3,-9,-1,-5,-5,-6,-8,-1,10,5,7,1,4,-5,9,4,-1,2,-3,-1,-4,9,3,-2,-8,-3,4,-2,-9,9,-7,1,6,-1,8,1,7,7,-2,5,7,4,-3,2,-5,1,5,-9,-5,4,-2,-7,-3,-1,3,-4,5,2,8,9,6,-5,-3,-4,7,-2,-10,-8,-5,-9,-4,-7,-5,-6,-4,8,6,-10,10,-9,-9,5,-2,-6,3,-5,10,-7,-2,10,9,-3,1,-6,-5,-5,-8,6,5,-8,7,5,-5,6,7,-1,-4,-1,-8,-6,-6,9,-3,-5,-9,7,6,5,6,9,7,-8,-4,8,10,5,4,1,1,8,-10,-5,-8,-8,-4,-8,8,-4,6,6,-3,-3,7,8,9,7,10,-6,4,3,-2,9,-6,6,-4,-10,-5,5,7,1,9,5,-2,10,-6,4,-5,-10,7,-4,8,9,1,5,-9,-5,-4,10,3,4,4,-7,-2,-9,-1,-1,1,10,5,-9,2,3,-4,4,2,7,7,-2,-9,9,5,8,-1,7,8,10,-10,7,-5,-3,10,-10,2,-7,4,2,7,7,-2,6,2,9,-9,8,-7,1,-3,-6,5,-7,-9,-10,10,-6,4,10,8,-10,4,-2,-10,-2,-6,-7,10,-9,4,-3,9,-5,-1,-10,4,5,7,1,-10,2,9,-6,5,8,-7,2,-2,10,3,2,10,-5,5,-6,-1,1,-8,-1,-2,-10,1,4,10,5,-2,1,4,-8,-6,-6,-3,-8,-1,1,9,-10,-5,2,-8,1,5,1], dtype = "uint64")#candidate|2373|(840,)|const|uint64
call_2371 = relay.TupleGetItem(func_297_call(relay.reshape(var_2372.astype('float32'), [9, 3, 16]), relay.reshape(var_2372.astype('float32'), [9, 3, 16]), relay.reshape(var_2372.astype('int32'), [9, 3, 16]), relay.reshape(const_2373.astype('uint64'), [840,]), ), 0)
call_2374 = relay.TupleGetItem(func_302_call(relay.reshape(var_2372.astype('float32'), [9, 3, 16]), relay.reshape(var_2372.astype('float32'), [9, 3, 16]), relay.reshape(var_2372.astype('int32'), [9, 3, 16]), relay.reshape(const_2373.astype('uint64'), [840,]), ), 0)
uop_2380 = relay.erf(uop_2347.astype('float64')) # shape=(2, 12, 1)
uop_2383 = relay.tan(uop_2347.astype('float32')) # shape=(2, 12, 1)
func_925_call = mod.get_global_var('func_925')
func_928_call = mutated_mod.get_global_var('func_928')
var_2395 = relay.var("var_2395", dtype = "float32", shape = (165,))#candidate|2395|(165,)|var|float32
call_2394 = relay.TupleGetItem(func_925_call(relay.reshape(var_2395.astype('float32'), [11, 15])), 0)
call_2396 = relay.TupleGetItem(func_928_call(relay.reshape(var_2395.astype('float32'), [11, 15])), 0)
uop_2397 = relay.cosh(uop_2383.astype('float64')) # shape=(2, 12, 1)
func_1061_call = mod.get_global_var('func_1061')
func_1065_call = mutated_mod.get_global_var('func_1065')
const_2403 = relay.const([[1],[8],[3],[8],[6],[1],[-10],[-6],[-4],[-7],[-6],[-7],[-3],[8],[4],[10],[-3],[1],[-4],[-9],[-8],[-4],[3],[-3],[-6],[-7],[3],[-5],[-6],[4],[-10],[-7],[5],[-6],[-6],[-9],[-9],[5],[2],[-10],[-10],[1],[8],[10],[10],[4],[-10],[-10],[9],[-4],[-4],[1],[8],[5],[6],[10],[-10],[-7],[-8],[4],[1],[-7],[-9],[8],[6],[-4],[6],[4],[-1],[-6],[6],[-1],[9],[-7],[-5],[7],[9],[10],[3],[-7],[-9],[9],[-4],[9],[-2],[2],[-3],[4],[-3],[2],[-2],[-7],[-5],[10],[-3],[4],[7],[7],[-6],[9],[-5],[8],[6],[-1],[5],[-10],[-2],[-9],[-3],[4],[-7],[10],[-4],[7],[5],[-2],[9],[-8],[3],[7],[-3],[-8],[-3],[4],[7],[2],[8],[8],[-8],[4],[3],[6],[5],[10],[-3],[8],[5],[1],[-3],[3],[-2],[-4],[6],[-4],[8],[-10],[3],[6],[9],[-6],[4],[-8],[-7],[6],[5],[10],[4],[-10],[7],[-9],[-2],[-10],[6],[-5],[-2],[9],[6],[-5],[-6],[5],[-10],[-9],[-10],[-7],[2],[3],[-6],[3],[7],[-6],[10],[4],[-3],[-8],[-10],[10],[-7],[-4],[-9],[3],[-8],[9],[7],[5],[9],[-4],[-9],[2],[-9],[-10]], dtype = "uint16")#candidate|2403|(200, 1)|const|uint16
var_2404 = relay.var("var_2404", dtype = "float32", shape = (500,))#candidate|2404|(500,)|var|float32
call_2402 = relay.TupleGetItem(func_1061_call(relay.reshape(const_2403.astype('uint16'), [8, 5, 5]), relay.reshape(const_2403.astype('uint16'), [8, 5, 5]), relay.reshape(var_2404.astype('float32'), [500,]), ), 0)
call_2405 = relay.TupleGetItem(func_1065_call(relay.reshape(const_2403.astype('uint16'), [8, 5, 5]), relay.reshape(const_2403.astype('uint16'), [8, 5, 5]), relay.reshape(var_2404.astype('float32'), [500,]), ), 0)
output = relay.Tuple([call_2349,var_2350,const_2351,var_2352,call_2371,var_2372,const_2373,uop_2380,call_2394,var_2395,uop_2397,call_2402,const_2403,var_2404,])
output2 = relay.Tuple([call_2353,var_2350,const_2351,var_2352,call_2374,var_2372,const_2373,uop_2380,call_2396,var_2395,uop_2397,call_2405,const_2403,var_2404,])
func_2410 = relay.Function([var_2346,var_2350,var_2352,var_2372,var_2395,var_2404,], output)
mod['func_2410'] = func_2410
mod = relay.transform.InferType()(mod)
mutated_mod['func_2410'] = func_2410
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2410_call = mutated_mod.get_global_var('func_2410')
var_2412 = relay.var("var_2412", dtype = "float64", shape = (2, 12, 1))#candidate|2412|(2, 12, 1)|var|float64
var_2413 = relay.var("var_2413", dtype = "uint16", shape = ())#candidate|2413|()|var|uint16
var_2414 = relay.var("var_2414", dtype = "int8", shape = (512,))#candidate|2414|(512,)|var|int8
var_2415 = relay.var("var_2415", dtype = "float32", shape = (432,))#candidate|2415|(432,)|var|float32
var_2416 = relay.var("var_2416", dtype = "float32", shape = (165,))#candidate|2416|(165,)|var|float32
var_2417 = relay.var("var_2417", dtype = "float32", shape = (500,))#candidate|2417|(500,)|var|float32
call_2411 = func_2410_call(var_2412,var_2413,var_2414,var_2415,var_2416,var_2417,)
output = call_2411
func_2418 = relay.Function([var_2412,var_2413,var_2414,var_2415,var_2416,var_2417,], output)
mutated_mod['func_2418'] = func_2418
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2474 = relay.const([[[-8,-6,6,-8,5,8,-9],[7,5,-4,8,7,6,-10],[-5,8,5,2,2,-4,4],[-2,-8,-4,5,-7,3,-8],[1,-5,-10,2,9,-1,-5],[-5,-6,9,-6,-4,-4,-5],[8,-6,-3,3,-6,-1,10],[5,6,2,8,3,-8,-6],[9,-9,-9,3,-6,7,5]],[[8,-1,-1,-2,8,-6,-6],[9,9,7,4,3,-10,-8],[-2,7,8,-10,7,-4,3],[-6,-4,-3,5,-1,8,10],[4,4,-1,-5,-1,10,8],[-2,3,4,-5,2,-8,10],[-8,1,8,-9,6,-10,8],[4,-3,1,-4,-3,1,-8],[-10,-3,9,-10,1,6,3]],[[6,-7,9,7,-3,-2,-10],[4,2,-6,-2,-10,10,4],[-1,-3,8,9,9,7,7],[-10,4,4,-8,10,-3,-4],[2,-10,-5,-1,-4,-10,4],[-5,-9,-7,1,-7,-2,-10],[-7,-8,2,-3,-5,-8,3],[-10,-9,8,-3,1,8,4],[-6,5,-1,-4,4,-8,10]],[[-6,5,-9,-4,-2,-4,3],[-4,-2,-3,4,1,-7,-5],[-2,10,-9,-5,-1,7,-7],[8,-3,-7,1,-3,6,-6],[8,5,-8,9,1,-6,-4],[6,4,-9,4,-3,8,3],[1,-6,-1,-1,7,4,6],[10,3,-1,-8,5,8,9],[7,1,-9,8,-7,9,-1]],[[-2,5,8,8,6,-2,9],[2,-10,-10,-6,8,-1,5],[1,-2,-2,4,6,1,-9],[-4,5,-6,4,5,-7,6],[-10,-5,-4,1,-4,7,-9],[4,3,6,-4,2,10,-10],[2,6,-6,10,-10,7,10],[-3,-4,8,-5,-5,9,-8],[9,-10,5,-3,-7,-10,-6]],[[10,-1,-4,10,-10,6,-5],[-5,6,5,4,-1,1,-10],[2,6,-3,-5,-9,8,-3],[7,9,-2,-7,-2,7,10],[1,6,7,5,8,6,8],[-1,8,8,-1,4,-9,10],[10,-3,1,4,1,9,-3],[1,9,-2,-7,4,-3,9],[-5,-8,-1,7,2,2,-5]],[[5,8,-9,5,3,6,-3],[8,-10,10,-9,1,-5,-9],[6,-9,-2,-8,-3,-4,6],[-6,10,-10,-8,-10,-3,2],[6,4,3,-7,-10,8,6],[10,4,3,-1,-4,-3,-3],[-7,-4,-6,7,2,8,6],[5,-8,8,-2,-5,1,-9],[4,-3,-1,-6,-5,-10,-6]],[[1,2,8,1,-1,-4,-6],[-8,3,1,4,3,10,-2],[7,7,-2,3,9,3,-9],[-8,5,-3,7,2,-7,1],[3,6,-3,-9,1,4,-8],[-2,5,-5,8,-7,-4,-6],[6,-8,3,10,-8,1,-2],[1,-2,-6,-5,-9,9,-9],[9,-5,5,3,-9,3,5]],[[-9,9,-5,-3,9,-4,-2],[-8,-7,8,-9,5,-2,8],[-4,-9,8,-2,-8,7,-4],[8,5,1,-1,4,-4,6],[7,-3,-7,-3,10,-9,2],[-6,7,6,-9,4,6,4],[10,7,-3,8,3,-4,-9],[-1,-7,1,2,5,-4,3],[-8,-1,-6,6,1,7,7]],[[8,4,-9,8,-6,7,10],[-10,-1,-10,7,-3,5,-8],[1,-4,1,8,-1,-2,-5],[-8,-10,1,-7,4,-7,8],[4,-6,1,-3,10,-4,8],[-7,5,-1,6,-6,3,8],[8,3,9,-4,1,-3,-9],[-1,-5,1,6,2,-3,4],[8,-7,-5,8,-10,-6,-2]],[[-2,-8,-9,3,-2,5,10],[2,-4,-5,9,-3,-8,3],[-6,5,-7,2,7,-9,6],[-4,-2,2,9,10,1,-6],[8,3,6,3,4,-3,-3],[-1,-8,7,1,7,9,9],[3,-9,7,-5,1,-10,3],[7,6,5,4,4,-3,7],[-10,-4,-2,-4,-4,-5,4]],[[3,7,-3,9,-6,10,-8],[5,-7,-2,10,3,-6,-2],[5,4,-5,-7,5,6,8],[-5,1,4,5,-8,-1,-8],[9,7,5,-9,4,9,-1],[-3,1,9,-6,-9,-8,-7],[-9,7,-4,-9,6,9,5],[7,1,8,8,3,10,-6],[-10,-9,-5,-4,-9,-7,-2]]], dtype = "int64")#candidate|2474|(12, 9, 7)|const|int64
var_2475 = relay.var("var_2475", dtype = "int64", shape = (12, 9, 7))#candidate|2475|(12, 9, 7)|var|int64
bop_2476 = relay.bitwise_and(const_2474.astype('int64'), relay.reshape(var_2475.astype('int64'), relay.shape_of(const_2474))) # shape=(12, 9, 7)
bop_2479 = relay.floor_mod(bop_2476.astype('float64'), relay.reshape(const_2474.astype('float64'), relay.shape_of(bop_2476))) # shape=(12, 9, 7)
bop_2494 = relay.not_equal(bop_2476.astype('bool'), relay.reshape(var_2475.astype('bool'), relay.shape_of(bop_2476))) # shape=(12, 9, 7)
func_1209_call = mod.get_global_var('func_1209')
func_1214_call = mutated_mod.get_global_var('func_1214')
var_2500 = relay.var("var_2500", dtype = "float32", shape = (5, 150))#candidate|2500|(5, 150)|var|float32
call_2499 = relay.TupleGetItem(func_1209_call(relay.reshape(var_2500.astype('float32'), [5, 10, 15]), relay.reshape(var_2500.astype('float32'), [5, 10, 15]), relay.reshape(var_2500.astype('float32'), [5, 10, 15]), ), 4)
call_2501 = relay.TupleGetItem(func_1214_call(relay.reshape(var_2500.astype('float32'), [5, 10, 15]), relay.reshape(var_2500.astype('float32'), [5, 10, 15]), relay.reshape(var_2500.astype('float32'), [5, 10, 15]), ), 4)
output = relay.Tuple([bop_2479,bop_2494,call_2499,var_2500,])
output2 = relay.Tuple([bop_2479,bop_2494,call_2501,var_2500,])
func_2506 = relay.Function([var_2475,var_2500,], output)
mod['func_2506'] = func_2506
mod = relay.transform.InferType()(mod)
var_2507 = relay.var("var_2507", dtype = "int64", shape = (12, 9, 7))#candidate|2507|(12, 9, 7)|var|int64
var_2508 = relay.var("var_2508", dtype = "float32", shape = (5, 150))#candidate|2508|(5, 150)|var|float32
output = func_2506(var_2507,var_2508,)
func_2509 = relay.Function([var_2507,var_2508,], output)
mutated_mod['func_2509'] = func_2509
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2728 = relay.var("var_2728", dtype = "float64", shape = (5, 10))#candidate|2728|(5, 10)|var|float64
uop_2729 = relay.cosh(var_2728.astype('float64')) # shape=(5, 10)
func_127_call = mod.get_global_var('func_127')
func_129_call = mutated_mod.get_global_var('func_129')
var_2736 = relay.var("var_2736", dtype = "uint64", shape = (840,))#candidate|2736|(840,)|var|uint64
call_2735 = func_127_call(relay.reshape(var_2736.astype('uint64'), [14, 10, 6]))
call_2737 = func_127_call(relay.reshape(var_2736.astype('uint64'), [14, 10, 6]))
output = relay.Tuple([uop_2729,call_2735,var_2736,])
output2 = relay.Tuple([uop_2729,call_2737,var_2736,])
func_2743 = relay.Function([var_2728,var_2736,], output)
mod['func_2743'] = func_2743
mod = relay.transform.InferType()(mod)
var_2744 = relay.var("var_2744", dtype = "float64", shape = (5, 10))#candidate|2744|(5, 10)|var|float64
var_2745 = relay.var("var_2745", dtype = "uint64", shape = (840,))#candidate|2745|(840,)|var|uint64
output = func_2743(var_2744,var_2745,)
func_2746 = relay.Function([var_2744,var_2745,], output)
mutated_mod['func_2746'] = func_2746
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2854 = relay.var("var_2854", dtype = "float32", shape = (13, 3, 1))#candidate|2854|(13, 3, 1)|var|float32
var_2855 = relay.var("var_2855", dtype = "float32", shape = (13, 3, 5))#candidate|2855|(13, 3, 5)|var|float32
bop_2856 = relay.floor_divide(var_2854.astype('float32'), var_2855.astype('float32')) # shape=(13, 3, 5)
output = bop_2856
output2 = bop_2856
func_2863 = relay.Function([var_2854,var_2855,], output)
mod['func_2863'] = func_2863
mod = relay.transform.InferType()(mod)
var_2864 = relay.var("var_2864", dtype = "float32", shape = (13, 3, 1))#candidate|2864|(13, 3, 1)|var|float32
var_2865 = relay.var("var_2865", dtype = "float32", shape = (13, 3, 5))#candidate|2865|(13, 3, 5)|var|float32
output = func_2863(var_2864,var_2865,)
func_2866 = relay.Function([var_2864,var_2865,], output)
mutated_mod['func_2866'] = func_2866
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3168 = relay.var("var_3168", dtype = "float32", shape = (1, 12, 14))#candidate|3168|(1, 12, 14)|var|float32
uop_3169 = relay.acosh(var_3168.astype('float32')) # shape=(1, 12, 14)
func_127_call = mod.get_global_var('func_127')
func_129_call = mutated_mod.get_global_var('func_129')
const_3173 = relay.const([1,5,-10,-2,-6,4,3,9,-5,-2,1,-7,-1,8,-3,10,-10,9,-7,-4,5,-2,-8,-2,1,-7,2,-3,-8,-1,-3,-6,-5,3,-8,-4,5,-1,7,7,7,-2,7,-4,-6,7,-5,4,-7,-3,-6,-6,-2,-3,10,7,-5,6,4,-8,-6,-2,9,2,-5,-9,-1,1,3,10,-5,9,-6,3,-5,-10,7,2,10,-1,9,7,6,1,3,1,8,9,6,-4,4,-2,8,6,-9,6,-7,-8,-10,-10,-10,-2,-2,-4,2,9,-4,6,6,1,-8,-5,-9,-8,2,3,-9,-4,-7,-9,-6,6,1,1,3,-5,8,-8,5,-5,3,2,-4,-5,5,-9,-4,3,6,-5,8,2,1,3,5,4,-6,2,-1,1,2,-6,-5,-2,-3,-2,6,-6,-5,5,-7,-9,-3,2,-7,1,3,6,6,-10,4,1,9,8,-8,-5,-2,-7,7,-1,4,-4,9,6,-7,-6,10,2,9,-5,-1,-2,-7,7,10,-8,10,-1,3,6,-6,2,4,-7,-4,-9,-3,9,2,5,6,8,7,-4,-9,-2,-5,-2,10,1,2,-8,-3,-6,-3,-8,-6,4,8,-6,10,-3,-6,-1,4,8,-2,-10,1,9,-9,-2,5,-8,4,1,6,7,7,-6,-2,7,-1,10,-5,6,7,-10,-2,5,-4,7,8,-2,4,10,-2,-1,-5,5,-9,5,8,6,6,7,-10,10,10,5,-7,3,3,2,-4,-8,-9,9,-10,1,-8,6,5,-6,-7,3,7,5,10,7,-6,7,2,5,2,-8,4,-8,9,6,-8,-1,-4,4,4,8,-8,5,10,2,8,4,-5,1,-8,-9,5,-1,6,3,-9,-10,-7,-9,-9,-10,-10,-8,-7,-8,-7,1,-8,-3,10,-4,8,-7,3,3,-6,8,7,2,5,1,8,-4,-4,3,-4,4,3,8,-7,9,-3,-1,2,-8,-5,9,-1,-4,-1,-1,-3,8,6,5,6,-9,2,-3,5,-1,10,-8,6,-8,-8,-3,-3,9,8,5,8,5,3,-4,9,3,-9,2,2,4,10,2,-2,-7,5,-4,-5,4,-9,8,-8,-9,1,-4,-3,4,-8,1,5,10,-9,6,-3,1,3,-2,-2,7,2,8,-10,1,7,7,9,6,2,-9,4,-9,-1,5,-1,9,-4,1,7,3,3,8,7,-7,5,6,-5,-4,5,2,-4,9,7,-3,1,8,3,-5,9,-9,-7,-4,9,1,-9,-10,-5,10,-9,6,-6,4,-10,2,-1,4,6,-10,-5,-1,-7,7,9,4,10,-10,4,-8,2,-4,2,1,-7,5,6,-6,4,-5,-9,-3,-6,-7,-6,5,-4,-1,8,-4,-6,4,-2,3,4,-1,6,3,-6,2,-3,9,5,-4,5,5,7,-1,2,9,3,-8,-3,-1,-1,-10,-10,-2,1,8,-3,7,-6,1,4,1,-9,6,-2,-2,2,7,-2,-8,6,1,1,-1,4,-5,1,6,7,-5,-3,-1,-10,-8,5,7,4,-3,4,1,6,-8,2,-1,8,-9,3,-5,-6,5,-10,5,8,8,9,-2,7,-4,-6,9,10,-4,-6,4,-5,-3,1,9,-5,-1,-6,1,-5,-2,1,6,9,-4,10,-7,9,9,10,-9,-5,-1,-5,4,-1,-2,10,-6,7,-4,-10,-3,-4,8,10,-1,10,-6,6,9,-8,10,9,9,-7,-7,5,-7,4,-5,5,-1,-9,1,7,-5,-1,5,10,-7,6,-4,-4,1,6,-4,3,-5,-10,-10,-4,-6,-9,-4,6,7,-5,-4,-4,9,-3,3,6,-8,4,-7,-2,-5,5,-1,-3,2,1,-7,3,5,8,-1,5,3,7,10,-3,8,6,-9,-8,-7,9,4,-9,-7,6,-1,7,-2,4,-2,9,-6,-1,-4,-8,-8,4,-8,-10,9,-2,8,-6,2,4,-8,-5,-10,9,-5,-6,3,-4,2,-5,9,3,7,-8,9,4,-5,-2,-5,-10,10,-5,5,-6,-5,-9,-10,-4,4,-5,-3,2,8,-4,5,-5,-7,9,-10,-10,6,9,-6,3,4,4,-9,-7,10,-9,-5,-1,-5,-6,-5,-9,-6,9,3,3,-9,7,3,4,5,-8,10,-3,-10,-9,5,-8,-6,4,-8,-9,4,-7,-9,-10,-4,5,10,8,-6,6,5,-2,-10,2,-3,-5,6,2,2,-2,-2], dtype = "uint64")#candidate|3173|(840,)|const|uint64
call_3172 = func_127_call(relay.reshape(const_3173.astype('uint64'), [14, 10, 6]))
call_3174 = func_127_call(relay.reshape(const_3173.astype('uint64'), [14, 10, 6]))
output = relay.Tuple([uop_3169,call_3172,const_3173,])
output2 = relay.Tuple([uop_3169,call_3174,const_3173,])
func_3183 = relay.Function([var_3168,], output)
mod['func_3183'] = func_3183
mod = relay.transform.InferType()(mod)
mutated_mod['func_3183'] = func_3183
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3184 = relay.var("var_3184", dtype = "float32", shape = (1, 12, 14))#candidate|3184|(1, 12, 14)|var|float32
func_3183_call = mutated_mod.get_global_var('func_3183')
call_3185 = func_3183_call(var_3184)
output = call_3185
func_3186 = relay.Function([var_3184], output)
mutated_mod['func_3186'] = func_3186
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3204 = relay.const([[[3],[-9],[10],[7],[1],[2],[3],[6],[10],[8],[-5]],[[5],[10],[5],[9],[-9],[-7],[-1],[8],[-1],[-5],[2]]], dtype = "int64")#candidate|3204|(2, 11, 1)|const|int64
var_3205 = relay.var("var_3205", dtype = "int64", shape = (2, 11, 6))#candidate|3205|(2, 11, 6)|var|int64
bop_3206 = relay.less_equal(const_3204.astype('bool'), var_3205.astype('bool')) # shape=(2, 11, 6)
uop_3216 = relay.sin(var_3205.astype('float64')) # shape=(2, 11, 6)
output = relay.Tuple([bop_3206,uop_3216,])
output2 = relay.Tuple([bop_3206,uop_3216,])
func_3220 = relay.Function([var_3205,], output)
mod['func_3220'] = func_3220
mod = relay.transform.InferType()(mod)
mutated_mod['func_3220'] = func_3220
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3221 = relay.var("var_3221", dtype = "int64", shape = (2, 11, 6))#candidate|3221|(2, 11, 6)|var|int64
func_3220_call = mutated_mod.get_global_var('func_3220')
call_3222 = func_3220_call(var_3221)
output = call_3222
func_3223 = relay.Function([var_3221], output)
mutated_mod['func_3223'] = func_3223
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3374 = relay.var("var_3374", dtype = "float64", shape = (12, 2, 5))#candidate|3374|(12, 2, 5)|var|float64
uop_3375 = relay.asin(var_3374.astype('float64')) # shape=(12, 2, 5)
output = uop_3375
output2 = uop_3375
func_3389 = relay.Function([var_3374,], output)
mod['func_3389'] = func_3389
mod = relay.transform.InferType()(mod)
mutated_mod['func_3389'] = func_3389
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3390 = relay.var("var_3390", dtype = "float64", shape = (12, 2, 5))#candidate|3390|(12, 2, 5)|var|float64
func_3389_call = mutated_mod.get_global_var('func_3389')
call_3391 = func_3389_call(var_3390)
output = call_3391
func_3392 = relay.Function([var_3390], output)
mutated_mod['func_3392'] = func_3392
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3648 = relay.const([[[5.673084,-2.525562,4.704625,-7.278657,6.363520,0.485810],[-0.675418,-6.747102,-6.530173,-8.606984,-7.001677,6.575733],[4.697477,7.537757,-6.117869,-7.842284,-7.072715,6.615645],[0.866118,8.810931,-4.535486,-8.862719,-9.245048,7.736002],[5.249767,9.598604,-1.703265,1.111689,-8.419833,7.425479],[0.599768,-5.006071,-3.913016,2.098349,3.104315,-8.912910],[3.727448,-4.651903,0.257247,-2.332023,-4.472057,2.172104],[-6.532845,-4.465304,5.595004,-7.693419,6.102324,-0.600789],[-8.231282,3.165376,-5.050680,5.834127,-5.743928,-5.982006]],[[7.300014,4.875256,-4.587106,-5.421192,7.969259,2.920147],[-1.473754,5.834993,-7.287577,2.479672,0.466155,-8.188973],[4.457479,4.205451,-9.440234,7.395411,6.114725,5.916787],[8.753754,-9.772449,-2.508926,2.418824,8.164508,0.522379],[2.869339,-9.368219,1.423789,-6.479134,-0.723873,5.720065],[7.561642,-3.896804,6.073968,7.608292,3.654192,7.061478],[2.913710,-3.329381,5.371114,9.311460,1.521874,4.774680],[-6.377530,2.847540,5.182874,2.883145,3.148438,4.955689],[9.763632,-5.544056,4.890151,6.489434,-4.026648,5.104157]],[[3.788481,-2.957546,3.250585,7.055435,-6.158795,-6.847865],[6.434225,-5.550210,-5.644367,0.951180,-6.907992,-6.135306],[1.436256,6.000279,-5.013203,9.784280,4.774893,-0.158660],[0.516850,-0.152918,-2.059732,-2.568400,3.222518,-9.250627],[-8.409931,7.544813,5.130359,-2.093244,5.443826,8.959320],[1.247075,9.033197,-8.514773,4.024916,-4.018612,3.618474],[-2.025447,-1.109061,6.099698,8.881662,3.268127,-0.262146],[8.294856,2.051227,-4.651679,-8.550353,-9.139762,-4.444227],[6.658402,-9.100941,-2.592518,-3.107171,5.335184,-7.629999]],[[1.500488,8.663927,-5.104761,-2.573705,-8.721119,8.848625],[-8.785031,-0.513928,4.526850,6.380454,-4.740647,-3.885875],[-8.153353,-8.009167,-6.327247,-3.479380,-9.969601,-0.285919],[3.847738,-2.093806,-8.014180,7.798051,1.557075,4.761281],[-5.617171,7.935770,8.237497,9.236404,-5.819597,5.278343],[-7.520736,2.010017,3.877040,-5.802919,-4.592911,0.621008],[-1.535776,6.505499,-8.868771,-6.197429,1.673939,-1.672097],[-9.067409,-8.737052,9.400021,7.412466,7.496457,-6.807483],[-2.233312,-0.774115,-4.173207,7.526748,-8.355504,-3.098331]],[[-1.676981,9.838955,1.256163,-2.988749,-3.404861,-5.186509],[-8.744797,3.659062,-4.530555,3.931846,-9.368983,0.044275],[8.054706,5.110028,9.456066,-6.604710,4.178696,-0.287407],[6.911824,-8.342855,0.190527,4.042551,-1.390671,-2.926656],[2.847274,7.213303,6.714810,-5.819941,0.901281,-1.347532],[1.831494,-1.774577,-0.881503,3.733000,1.006694,6.140185],[5.996258,6.838733,-8.846131,-9.483236,7.143975,4.958128],[7.129407,6.681947,-7.461213,0.174656,-6.861859,-7.119598],[-7.528706,5.763662,0.074677,5.562243,7.302173,-2.126341]],[[-7.970045,5.187761,-5.141592,-2.523718,-2.005119,-5.580309],[9.717003,6.252313,-6.524491,-4.272906,2.514841,-6.214419],[0.286084,2.497365,-9.435552,-9.918122,1.114950,-2.108094],[-4.528517,0.891553,-6.313986,1.382619,2.322626,-8.276769],[-0.014752,8.073886,-7.868532,-2.399877,4.099635,-7.829626],[2.905623,-7.803110,3.075687,-7.908650,3.064448,-6.513920],[-3.733739,5.701287,-7.966474,9.824151,-0.928758,2.263417],[-1.734022,-8.662303,9.153474,-8.589939,2.180843,0.150793],[0.128148,5.324642,1.402224,3.891721,5.632956,-0.468558]],[[-8.194263,4.221468,-0.460359,2.883330,-2.476473,-8.430786],[-8.435455,2.691701,7.605144,-2.496108,-4.894216,8.110262],[-2.345196,5.599840,5.128599,4.424175,3.655529,-1.525776],[5.614679,9.874902,-2.668898,-1.528709,-0.838058,-6.160292],[-8.881393,-7.721221,-8.372217,2.155949,-9.573222,2.321415],[-1.879608,8.397493,1.170466,3.653812,7.187092,-9.837266],[-8.098856,3.251444,-2.023826,-0.748545,-1.870304,-2.642234],[-6.718576,5.016644,-3.550960,-5.236574,-3.322776,4.238028],[1.979362,-6.835757,7.531359,-8.764769,5.996694,-2.204033]],[[-3.273071,6.194408,4.387695,0.816122,8.757870,7.217223],[7.542692,-8.337515,5.684090,7.841364,-9.783587,-8.156061],[4.343767,1.889399,-4.421635,-6.554343,-4.747447,1.826427],[1.038952,9.198487,-1.043793,5.502206,-8.546230,9.791467],[9.717930,-8.818634,-9.804784,3.215058,-0.337595,3.204555],[-6.315933,3.844716,6.365562,-5.814139,1.325466,9.039930],[-9.791802,-1.417410,-6.655948,6.435395,-1.354190,2.988957],[-4.043322,-9.233522,1.998349,4.273199,-9.234843,-9.265632],[1.060643,-2.251455,-4.191546,-0.472550,-3.551497,5.717744]],[[-9.746531,-0.061445,-9.838850,-3.739360,-5.722437,8.774865],[-8.862587,0.774859,8.004565,-7.738806,1.286364,-5.134881],[-7.282252,-2.035689,6.328051,8.657926,-1.872893,-9.176351],[6.240949,6.604539,-1.104728,4.586449,1.385452,8.448763],[-8.964350,-8.935472,-0.163873,8.506547,4.816847,-3.721068],[8.386660,0.289488,1.053133,-2.319366,-4.577172,7.125606],[3.494344,9.789709,4.231341,2.019383,-1.117877,0.676755],[-5.731350,9.287724,7.443126,-6.988406,7.737905,-4.704525],[-8.238322,4.388928,2.146535,2.414822,7.350650,3.622619]],[[3.627915,-7.859637,-2.508456,-9.969181,-8.198335,7.053882],[5.870751,-2.289119,7.066329,-2.435037,5.711586,-6.008402],[-1.244406,1.986655,-4.002343,-8.925076,-6.986157,9.212023],[4.115970,3.219819,4.698288,8.700893,5.389052,8.545714],[-0.935673,-4.619867,3.127481,-2.465553,-5.037153,4.147275],[0.105536,-7.331920,-6.935292,-1.586818,7.203449,0.162261],[-3.112759,-1.915819,-9.465396,-5.853120,0.807361,-3.756445],[1.790616,-6.245750,9.984572,-1.612300,6.995469,-7.930897],[-9.675860,3.499009,-1.348690,-7.631300,9.897102,-9.526943]],[[-2.431488,2.742821,0.632893,-6.165542,-0.911498,-7.234276],[-5.087930,-2.443039,5.225859,7.396622,-2.130486,-6.195226],[1.525188,1.647340,8.026851,-4.835463,9.011681,5.824797],[-8.081038,4.628698,-7.815667,-6.877829,3.985264,-7.772464],[1.779212,-7.973697,1.895050,-6.073334,-5.361397,9.473045],[-1.948581,5.747021,3.139600,-6.662532,9.738412,3.037252],[-5.854504,-6.529918,-1.079464,-6.100252,7.966898,8.611253],[6.180956,3.986150,-8.029246,5.406195,6.544609,-7.841047],[9.312176,-4.472080,-6.132645,-1.066602,7.022810,-3.910597]],[[-4.967713,5.896523,-7.288715,-4.828876,-8.628053,6.043638],[-1.137428,7.743498,4.527299,6.959254,7.217531,2.369534],[9.452029,-8.607654,8.820721,-1.027866,9.884657,7.350866],[9.280872,-4.326647,0.038457,-0.116749,-5.174012,0.284563],[8.739147,0.403086,-8.784799,-6.523265,-5.683169,-3.260560],[-5.134837,0.201617,-9.268799,3.226133,-7.383722,-2.983451],[6.025957,-3.758410,-8.850599,9.449326,-1.238786,-6.195288],[-8.784859,-1.104411,2.597663,-6.154697,0.236810,-7.245057],[-4.751411,0.964092,8.567258,-3.209978,-3.562659,-7.729585]],[[6.118111,-2.607752,-0.783199,-7.473299,-3.652797,-5.398598],[-3.133801,1.971521,-1.850792,0.720218,6.450106,-3.523066],[-4.943521,0.972397,6.111646,-8.751167,3.828046,-1.105011],[5.812226,-9.450733,1.494172,-4.407298,7.008309,3.364977],[0.772958,-6.988936,-4.668993,0.149735,-6.885416,6.847821],[-5.588500,-3.510734,9.216421,-5.646232,7.982529,-0.343106],[3.104997,-4.585012,-8.331632,-0.646291,5.210162,-9.770642],[8.651150,-2.610459,-7.951453,0.567622,4.767589,-6.245852],[-0.025474,-0.699362,-9.567050,-0.069086,5.871916,-9.753963]],[[4.530749,0.845912,-4.874243,-0.158125,2.415669,9.749790],[-1.566553,-1.879979,-8.571627,-5.886407,7.601690,-8.932290],[4.064542,9.777427,-6.516729,-2.399657,3.928283,-7.395180],[8.650360,9.196643,1.184504,-6.592847,-7.888304,-0.681909],[-4.056174,1.318984,0.924158,8.707104,2.261884,3.183432],[-8.640818,9.660043,7.716110,9.663786,-9.917824,8.077644],[0.407841,1.099119,-8.207536,-6.037582,3.551906,6.599306],[-9.797367,5.223891,2.552474,3.578922,0.108604,5.206326],[-6.685486,3.388585,-8.134946,-0.569965,0.721788,8.689260]]], dtype = "float32")#candidate|3648|(14, 9, 6)|const|float32
const_3649 = relay.const([[[-6.812435,4.975908,8.597057,-9.520555,0.895389,1.221047],[9.779280,2.345588,8.774463,-9.021347,-8.589978,5.415962],[-6.986189,8.226377,9.427452,-8.856721,5.520611,7.010431],[1.932122,9.732398,3.536622,7.008342,0.746654,-4.636068],[-8.952301,-8.149265,7.786997,0.943510,-1.797440,6.496456],[-1.847944,0.580291,4.365876,-9.435025,-7.321943,-4.645378],[1.568625,-2.909276,-4.268532,1.318932,3.435207,-0.566879],[-5.939834,9.570679,-3.504065,-4.303832,-5.616414,-8.410070],[-6.620529,-3.767282,-5.608621,-6.146346,-6.341680,4.958194]],[[3.302795,3.661756,-4.121913,7.822854,3.781536,8.775518],[3.237660,-6.693327,0.707743,-9.547842,-0.144378,-0.923470],[8.064235,-5.194403,0.883174,-3.912834,-2.890228,-2.631551],[0.487001,6.531870,-9.969571,-9.480998,-0.432634,5.193590],[4.668422,2.932030,-0.437167,7.625132,6.862269,8.180864],[1.320635,2.778502,6.262371,-7.042835,-0.901868,5.730137],[-0.383408,-7.108959,0.054394,-7.094281,0.501772,-1.428979],[8.602826,0.868700,4.947754,8.225378,2.494536,-7.692377],[-8.861515,2.009787,1.258955,9.751957,8.552339,-0.694587]],[[4.917708,2.700243,9.302308,-3.724052,6.061121,4.894544],[-9.571327,6.482686,3.473757,-3.560332,-3.886749,-2.186679],[7.953879,9.165158,-9.196315,3.599468,-6.126472,-5.794500],[-1.824931,-4.639149,0.333834,-6.956687,0.479767,5.318342],[0.925560,-9.471464,7.038467,8.889777,4.021264,1.019339],[1.679258,5.942357,-3.533477,6.367192,7.039388,-0.152837],[2.133112,-1.501309,1.092021,5.068507,-3.628714,-7.507256],[0.099413,-9.761446,2.607137,-3.833353,-2.641572,-6.542415],[8.982989,3.032829,-9.483303,6.473713,-0.784095,-8.112964]],[[9.413965,-8.097659,3.648306,-7.024579,8.412374,9.422412],[-7.477773,9.953381,-2.416631,4.728302,7.844975,-5.998807],[7.770507,9.332357,8.248017,5.321634,4.407838,-7.957855],[-0.801423,6.456158,1.118584,-2.433642,-0.095621,-1.230375],[-3.836330,3.266194,-3.229602,8.468985,7.929723,6.172933],[-3.836408,-6.405226,8.811674,-3.785752,0.441437,0.159784],[5.986564,-6.382273,3.541612,-0.424855,9.253406,1.809637],[1.214161,0.898906,7.898704,6.501042,6.530354,8.063093],[5.330584,-8.661098,-2.928127,4.040778,-6.188243,3.540510]],[[5.754258,4.119808,8.622149,-9.311438,7.965559,-5.213891],[4.832238,-8.259765,5.025835,9.039918,7.774924,4.952069],[6.071805,1.916992,-6.230538,0.532441,-5.237127,-8.563791],[2.530007,-4.201908,-6.685855,9.171976,7.159095,-1.495445],[5.956385,1.809834,-2.599590,-4.817503,7.031302,0.750806],[1.822100,5.608559,3.483685,5.103532,8.211822,9.909466],[-5.916957,7.430536,-0.022647,-9.983498,4.941804,-8.715052],[-6.983141,6.249947,3.307098,-0.795021,8.814064,-7.005946],[5.660850,4.305886,-9.495135,4.139122,5.812896,-1.414320]],[[-9.183840,7.668429,-6.099830,6.057518,1.531801,-5.977973],[1.155718,5.358009,5.036651,5.043113,6.386540,3.186068],[1.413076,4.834774,5.318144,-0.807985,-0.418474,6.276524],[-8.193765,-5.075904,1.840427,-6.514713,2.517250,2.749192],[1.966886,6.557031,7.937962,-4.660591,9.702969,8.336129],[2.641759,1.526294,8.022695,-6.586933,6.535684,1.101345],[-1.165000,-5.268330,5.730723,-6.874349,-8.529760,-0.532166],[-6.716584,2.752978,-1.797927,-7.622755,-2.432011,2.201853],[-5.135236,3.882760,-1.365643,-0.744884,-9.494254,-1.796863]],[[-4.491160,7.172488,2.136963,-6.819279,-6.746908,6.775353],[-9.495589,9.428734,6.679253,-5.951401,-7.513506,-8.219302],[1.405566,0.772752,8.048444,9.747864,-7.031077,-8.824064],[-9.821618,9.283774,-6.784064,0.400075,-3.607322,-2.593478],[-2.427338,6.198469,-2.998345,3.518057,-4.376037,-3.046416],[0.371271,7.266616,-2.145440,0.989642,-6.736506,0.961591],[3.698577,1.831776,7.689110,-5.774663,8.520025,3.303131],[3.230424,1.999051,4.123268,2.437817,2.103283,9.869111],[-5.537292,3.754880,5.103034,-4.558425,5.733660,3.157852]],[[9.013554,-8.757247,5.031945,-5.384169,5.376766,3.038768],[5.319712,8.849945,2.830537,-9.570169,8.485330,2.942464],[2.442203,1.960070,7.279997,3.411637,-6.798376,4.024332],[7.356597,-2.277720,2.071823,-3.069749,-8.074350,-1.609701],[-9.531791,-0.439420,-3.791010,-7.009155,7.685677,-7.201684],[-1.282939,3.463533,-7.382072,7.862504,-8.990359,-0.493429],[4.856962,1.051821,-8.110976,0.511711,-1.353878,-3.052381],[0.767612,-3.580836,-0.716214,-3.548015,8.442227,-3.871271],[-4.543464,1.485410,0.171508,7.032640,-8.535370,4.049530]],[[-9.726028,4.531888,-6.984639,6.530790,2.835742,-2.349988],[-8.380053,-1.322484,-4.060772,2.714753,-9.142901,4.802064],[-9.795608,-3.564963,5.288222,8.206698,0.265831,2.457218],[-7.164039,2.819104,-5.922991,-0.549488,-9.861072,-0.687455],[9.361939,-8.675160,1.364379,6.001087,-8.576096,-6.593540],[5.335663,1.782877,0.473553,-5.934241,5.538325,8.174148],[0.607137,-8.316216,-0.753753,-9.910263,4.169173,-5.793495],[2.251104,-9.710649,0.651559,6.156448,5.477190,3.143267],[4.895984,-9.347868,-0.570800,3.707501,4.157334,3.962500]],[[-3.343919,4.564513,-7.246014,-4.738127,-5.910707,9.849296],[-1.788453,-9.524197,9.358188,-9.182705,-4.091648,7.979730],[-4.536419,-0.400449,5.863595,4.267958,-1.577872,6.919870],[-2.292919,-3.086848,-9.695565,4.143998,-6.498008,-3.648167],[7.006090,6.495010,-5.894208,-3.666602,6.533960,-4.929069],[1.036986,-0.018403,4.160055,-7.753379,-5.802256,-6.506020],[1.699671,7.769499,3.118403,6.671326,-3.191767,-1.896749],[-8.294090,9.220586,-2.367580,-3.508536,9.959783,7.661694],[-6.562428,9.491224,-1.688023,1.678896,7.003201,2.134846]],[[7.147451,4.299042,4.618134,-4.796145,0.834807,8.171399],[6.768641,8.893824,7.044092,8.269330,-1.701579,-6.033920],[-3.472783,-0.369451,-8.961293,0.507101,7.504835,6.627721],[-8.959382,-6.167709,6.122974,9.483536,4.771366,6.428111],[1.959751,-3.586207,6.460321,-2.765026,-7.133398,7.824264],[1.601851,-7.457771,-9.013966,9.266532,8.052155,-3.213885],[-0.981341,-6.517654,-9.603228,-6.127747,-2.904214,7.566635],[0.492775,-8.284120,2.079519,-7.061166,-1.430001,3.087609],[-2.826503,3.976864,-2.552030,-6.900184,-3.109148,-9.442739]],[[-8.717958,-3.183090,0.462590,4.794684,-4.328987,-8.325513],[5.069230,-3.936069,-4.921296,-8.138486,-9.309128,-1.764845],[1.355387,9.248708,9.098736,-0.990821,-3.752149,5.921256],[6.365273,-8.092097,-8.971418,4.478770,7.887226,4.780549],[4.911211,-4.933422,3.979087,-8.333176,2.584893,-9.035670],[6.656756,5.776034,-5.358978,8.351853,3.769745,5.300587],[-4.711178,6.718722,-5.793457,0.355807,1.240281,0.423282],[0.343922,1.589198,-6.287826,6.733039,7.813728,0.147133],[5.533046,2.845591,8.980042,-7.037613,4.645341,5.956961]],[[-0.010050,0.890622,9.581053,0.027282,-8.848539,7.163504],[-9.218402,-7.755461,8.489509,4.865181,-5.230436,0.698935],[8.063210,6.872001,-6.620491,-0.456235,-3.723403,-9.049137],[0.313476,-1.622923,-7.387226,-6.985458,-0.308637,-6.308391],[-9.795884,7.991986,-6.643832,-6.391621,-6.274891,-9.113340],[1.220685,-3.551945,-1.089797,2.849519,-2.345130,0.854779],[4.638334,9.623411,-8.643613,-7.645328,-1.722608,2.967803],[-6.635787,-1.193934,-9.787806,4.589880,-4.916775,1.043933],[-3.954203,-1.549879,-5.806456,-6.588287,7.181407,0.150329]],[[5.123271,-6.762488,1.055407,8.505564,-7.766823,4.255646],[-9.633354,-0.180609,-2.132149,-9.669778,-8.250792,4.656650],[-3.465951,-9.066587,1.514632,-8.501643,3.377343,-3.034173],[-1.298545,2.110685,-7.105719,9.494635,5.067417,2.565004],[2.132818,3.493427,-0.980783,-7.829326,-9.446729,-5.450132],[7.098124,-8.539126,1.765981,8.038236,-8.346161,-8.144151],[9.875752,-4.384288,9.265138,-5.585631,3.283705,-5.004207],[-0.739201,-3.597033,-6.015056,5.674501,4.084797,-7.568439],[-6.165003,7.826767,-7.960317,4.688911,7.389657,6.030797]]], dtype = "float32")#candidate|3649|(14, 9, 6)|const|float32
bop_3650 = relay.minimum(const_3648.astype('float32'), relay.reshape(const_3649.astype('float32'), relay.shape_of(const_3648))) # shape=(14, 9, 6)
output = relay.Tuple([bop_3650,])
output2 = relay.Tuple([bop_3650,])
func_3658 = relay.Function([], output)
mod['func_3658'] = func_3658
mod = relay.transform.InferType()(mod)
mutated_mod['func_3658'] = func_3658
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3658_call = mutated_mod.get_global_var('func_3658')
call_3659 = func_3658_call()
output = call_3659
func_3660 = relay.Function([], output)
mutated_mod['func_3660'] = func_3660
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3702 = relay.var("var_3702", dtype = "uint64", shape = ())#candidate|3702|()|var|uint64
const_3703 = relay.const([[[-9,8,-4,2,7,2,-6,-9,3,10,5,-8,6],[9,-7,5,-9,-3,-2,-6,2,-6,-8,3,-6,1],[-1,-8,6,-10,10,-6,-10,2,5,2,8,6,-3],[-9,5,10,-10,2,-8,6,10,6,10,2,6,3],[-4,-1,-1,7,10,-2,8,8,-6,3,-8,-6,9],[-6,-3,-10,-1,5,-1,7,-10,6,3,-3,8,-7],[-8,-5,-2,-3,-1,4,-4,-3,1,-10,9,8,-8],[4,-8,-4,-5,-3,-1,6,9,-3,8,2,6,-10],[-8,8,1,3,5,8,-6,9,-9,-9,-6,3,-8],[5,7,-6,6,-2,-8,-6,4,-2,-7,10,-7,-6],[3,9,4,-3,9,-7,-5,-10,6,5,2,-10,10],[6,-1,2,-2,3,-3,9,8,-7,-7,-8,-2,2],[-10,-4,-4,-2,3,-9,7,8,-8,3,5,9,-4],[-2,9,2,-8,-4,9,7,1,4,8,7,-1,2],[-8,-5,-9,1,-2,-9,-3,5,8,1,-8,7,-7]],[[1,-5,-1,5,7,6,4,-5,10,-6,8,-7,-5],[-4,-2,-7,10,-6,-4,8,7,-1,1,3,-4,6],[-3,4,9,-10,-10,4,8,-10,4,-6,-3,-1,-5],[-8,1,4,9,2,6,1,-9,-6,6,1,-6,-1],[6,-5,-4,1,-9,9,-10,7,7,10,2,4,3],[-10,-2,10,-10,-8,-8,-10,-3,4,-2,-9,-9,-4],[6,1,-3,8,1,-5,1,-3,-2,5,-2,9,9],[4,7,-1,5,-10,-4,-8,-4,-5,-6,-5,3,-4],[-10,2,10,-9,3,-10,5,-9,-8,-5,-7,1,-1],[4,8,-3,-2,8,-9,9,-1,10,-8,-7,5,-3],[4,-8,10,-1,1,-5,-6,-4,-3,9,-1,10,-10],[-10,-10,-9,-8,-9,10,-5,3,3,6,-8,-2,3],[-6,7,-9,-10,1,-1,-8,-5,2,1,-3,-7,-4],[8,-2,9,3,3,-4,-10,2,-2,-4,1,1,3],[6,3,-7,-6,-1,8,-1,-5,-3,10,6,8,-10]],[[-8,-10,-5,1,6,10,-8,7,4,-6,-2,1,8],[5,9,-6,-6,-8,-3,-10,8,9,10,3,-3,-10],[9,1,3,5,1,9,-8,-10,-5,-9,10,-10,-5],[2,-3,7,8,-1,-1,-2,-8,2,7,6,-2,-6],[5,1,-10,-10,-7,-5,2,-5,2,7,-10,7,-1],[-9,10,-3,3,6,9,6,-10,3,7,-5,7,9],[1,5,9,-2,1,-5,-1,8,7,-6,-5,9,8],[10,-7,3,7,7,1,-6,-9,7,-1,2,8,-5],[8,4,-7,9,5,2,-9,-7,-10,-3,3,-9,-2],[4,-10,3,-10,-1,-1,-1,-2,8,1,2,-10,2],[-4,10,3,-5,3,-8,7,10,-2,4,-5,5,-10],[9,3,-3,-2,2,9,8,-7,4,8,2,6,-3],[-10,7,7,-10,-7,7,10,-9,-9,10,5,-2,10],[2,1,9,4,-3,-3,-3,-10,2,-10,-8,7,-6],[5,-5,3,-3,3,-8,-9,9,-4,2,5,-3,-6]],[[5,-2,-8,-1,4,-2,-10,10,-3,-9,-10,-7,8],[-8,-6,-3,-2,5,3,-4,-10,3,-1,-8,-1,7],[9,-6,7,-7,10,5,6,-1,6,8,-2,-7,-6],[-7,1,8,9,8,-8,8,-6,2,-5,-3,-8,6],[-3,-3,8,-6,6,-1,-8,1,-4,7,-6,-4,-4],[9,-7,2,-7,-7,-4,6,-6,5,5,-3,-6,9],[-9,-2,-9,5,-7,-7,1,-1,-8,-7,5,-10,7],[-9,4,-7,-2,-6,-10,-10,9,1,-1,6,-1,-6],[4,-7,9,-6,-6,4,3,-3,-2,-2,-8,10,7],[-1,-9,-7,2,4,9,-2,4,-5,9,-2,10,-9],[-8,10,-5,8,-9,-6,6,-4,-1,-2,-4,6,4],[4,3,-4,4,-8,6,-2,-10,8,10,3,-10,-10],[3,-10,3,2,-9,9,-10,-10,-5,-3,-3,-3,5],[-6,-2,-9,-2,1,-3,3,9,3,1,6,-10,-2],[-10,-5,2,9,-10,8,-9,9,-2,-4,-6,-10,4]],[[4,-3,-6,3,1,5,-7,10,10,4,1,-4,9],[-6,1,-3,4,3,-10,-1,2,-10,-2,-4,-2,-2],[6,-10,7,4,-7,-3,4,1,4,6,10,5,-8],[4,9,3,-3,-2,2,-10,-4,10,-1,-3,-2,1],[5,-4,4,3,6,-9,-10,1,9,-8,8,-3,10],[-4,-7,4,10,4,-6,5,2,2,7,1,7,-2],[-9,4,3,2,4,1,-4,7,-2,5,-8,-4,-2],[-2,-6,4,1,7,-9,-3,6,6,-1,-3,5,4],[5,-10,-5,-6,9,10,-9,4,-7,10,3,3,-10],[6,4,-1,-10,-4,3,7,9,2,4,7,-2,-7],[4,8,6,-9,4,9,-1,8,-2,-6,2,-10,-3],[-2,-5,-10,8,-1,2,7,10,-9,-9,-6,1,4],[1,4,3,9,-4,7,8,6,-9,-5,9,1,10],[10,9,-9,-10,-6,-10,10,-5,5,4,5,-6,-4],[4,-6,-3,10,-2,4,-3,-4,-5,-8,-3,8,-6]],[[-1,-3,1,2,-4,4,9,-4,-8,3,-1,-8,3],[-1,9,1,-2,-6,-4,10,3,3,-10,7,7,9],[2,-6,-9,3,-8,7,-1,-5,-1,-4,-9,-10,-5],[6,-7,-9,-4,-4,-3,8,-3,1,8,-10,1,5],[10,-10,2,-6,-2,-10,9,-7,10,4,-10,1,1],[7,5,1,-7,10,-8,10,1,-4,3,3,-7,-9],[3,5,1,-5,3,-2,8,10,10,4,10,-2,-1],[6,-3,7,5,10,-1,4,3,-4,10,7,-6,3],[-10,8,-9,3,9,8,1,2,4,-8,4,10,-8],[5,-9,-1,-1,-2,3,-4,3,-8,3,6,6,6],[6,5,2,-9,6,10,8,2,7,-6,10,-5,-2],[2,-7,-9,4,-10,-1,7,-10,9,-9,1,-8,6],[-9,-3,-4,-10,-1,5,-2,-2,-5,-4,-6,-4,3],[10,-2,-9,9,-3,-7,5,3,-3,-6,-10,6,7],[7,8,7,-3,-6,2,-4,-10,10,-9,9,10,9]],[[-8,7,8,5,6,-5,10,1,1,-7,-8,-8,1],[-1,3,-4,6,6,-5,-1,2,-10,-1,6,-10,-3],[-1,-7,6,-5,9,-10,9,2,-7,-7,-1,3,9],[4,-4,10,-7,8,-9,4,2,-5,-2,-7,2,-9],[-10,-4,4,2,6,3,-1,9,-6,9,9,-1,3],[-9,3,-5,-10,3,1,-4,-7,2,-8,9,-6,-1],[2,-5,1,9,1,6,5,7,-7,2,-8,4,-7],[-9,3,7,4,-2,5,-1,-5,10,-8,-5,10,9],[-4,-3,7,-4,-3,-6,3,6,-9,-4,3,2,1],[-4,-9,-8,-7,-5,-4,-5,-10,-6,10,10,-6,-2],[6,-10,-5,9,-9,-6,9,-9,10,10,6,6,-7],[-5,-9,-3,3,6,-10,-2,2,-3,9,4,9,-3],[1,3,6,-2,-5,1,-10,9,-2,9,9,6,6],[-1,-3,10,-4,1,-8,-6,-10,4,6,2,-4,-3],[-2,5,7,1,-10,4,-3,-5,-8,8,8,7,-7]],[[3,7,6,-4,-7,7,-1,-10,-1,9,-6,9,-2],[5,-2,-8,6,10,7,3,5,4,6,-2,-7,-5],[6,4,-2,1,3,-8,7,1,1,9,-3,-1,-7],[6,-4,6,6,1,-10,9,-2,-4,-4,-6,-8,-1],[10,-10,7,-10,8,4,-5,-9,7,-2,-6,9,-1],[8,-2,2,3,6,1,-2,1,2,-10,4,-2,6],[3,9,2,5,6,-5,-3,-10,8,-1,7,6,-6],[-7,-5,6,10,-1,-7,-8,4,-2,4,-1,-6,-1],[8,2,-6,-4,-4,10,-10,-8,-7,-9,-10,10,-5],[-6,3,-3,5,-7,-4,5,-3,-2,3,-7,-8,1],[-9,6,10,-2,1,6,-1,-8,-3,-3,-5,-9,-8],[-9,5,6,1,-8,4,-5,-5,1,-3,-3,2,-3],[2,5,10,-6,-4,-9,-6,7,6,7,1,9,6],[10,-7,-5,7,-9,-6,4,-9,6,-9,-7,4,-8],[1,9,-9,-5,6,-5,2,1,-1,9,-7,7,-5]],[[-5,-10,4,-10,9,5,-8,-6,5,-7,5,9,-9],[-8,-6,-3,-3,-2,4,-1,-3,-7,-9,-4,-10,-9],[10,-10,8,-5,10,-3,-3,-10,-9,8,-1,-5,-7],[-3,9,-3,-3,7,-8,6,-2,-10,4,-10,3,8],[-4,-4,-9,9,2,6,2,5,-6,9,-9,-3,-1],[9,2,9,8,8,-2,-7,8,8,-7,-1,5,2],[-10,-9,9,-6,5,8,1,-3,4,7,-3,1,9],[4,-5,10,-3,-6,-10,5,10,-1,1,5,-3,-5],[-7,-10,-2,2,3,3,-4,-10,5,-10,-9,7,-4],[-5,-3,7,9,-6,-2,-10,-4,-2,-4,-3,-8,-4],[-3,-8,1,5,-4,-4,10,7,2,-10,10,5,6],[1,-2,-2,-5,-3,4,2,2,4,-8,5,-8,-8],[-9,-10,-2,9,-7,-10,-3,-1,-3,-6,9,-9,1],[-8,-1,7,9,4,-10,7,6,-2,-2,-6,3,2],[-2,-10,-6,-3,-7,8,-8,9,-7,-7,-4,2,1]],[[-1,-7,-10,-3,-5,-1,8,1,-3,-2,8,9,-2],[6,8,-1,-4,3,1,-4,-7,-7,2,2,-6,10],[-6,1,1,-4,-5,-10,-5,-4,-9,3,5,10,7],[-5,-10,6,3,4,7,6,4,2,9,4,-6,5],[-6,-1,10,-5,-10,-4,10,-8,7,8,10,-9,-8],[8,-1,-5,9,-9,1,-7,4,-5,-1,-1,9,-2],[-9,-1,-5,3,3,4,-6,-8,8,10,-9,8,10],[-2,9,9,4,-7,10,-8,7,-2,6,8,9,6],[2,10,3,2,-6,10,-10,3,-4,-2,3,-4,6],[-5,-9,-5,-4,7,-6,1,-10,4,-7,-10,7,4],[6,1,9,8,-6,2,-7,9,-6,7,-1,-5,-5],[-1,-9,-4,-10,-10,10,8,-3,8,-9,-5,-9,-10],[1,-9,4,-1,-5,-9,-10,6,7,6,6,9,-2],[10,-7,10,-8,8,-8,-5,4,10,3,3,-1,9],[2,-3,-4,-4,5,-1,-4,7,8,7,-5,5,2]],[[-7,7,-2,-6,3,-10,-3,2,10,-4,2,-8,-5],[5,-3,6,-1,6,1,-8,3,3,3,-3,5,-7],[-1,-3,9,4,6,2,4,1,-1,2,-5,2,-2],[10,-2,2,3,10,5,6,6,9,5,7,-8,-1],[-2,10,8,1,8,-1,-9,3,-7,-5,6,-2,3],[10,-6,4,-2,4,-6,-9,-8,-5,3,3,8,10],[-4,-6,2,8,-7,-10,9,-10,-8,-9,-9,-5,4],[-2,-8,8,-9,-6,-2,-10,9,9,-3,4,8,-10],[-10,1,3,-8,-8,-2,5,-7,-4,-6,-9,2,-4],[5,-10,8,2,-5,3,-7,-4,-9,6,-5,-6,-3],[6,9,2,1,-1,-3,8,-7,5,-3,10,7,-9],[6,1,-10,-7,-8,-3,2,-8,6,-4,9,6,8],[6,-3,8,-10,-3,8,1,10,5,-9,-8,8,-7],[-1,9,-10,7,-9,5,3,-4,-7,-7,1,8,4],[5,7,-7,9,-10,-10,-2,-3,2,4,-9,3,5]],[[-9,-3,8,2,-4,-4,6,1,2,-9,-10,-2,-9],[3,-8,-5,3,7,10,5,-10,-6,-2,4,-10,-10],[4,-7,3,-2,-10,8,-6,5,6,-9,-8,3,-2],[7,-8,4,-8,-2,3,-6,2,6,-8,-6,-10,9],[2,9,8,7,10,-5,-4,-3,-2,10,2,-4,7],[-5,4,3,7,-1,-8,9,4,8,5,-5,-2,-3],[-2,-5,6,4,-3,8,-10,2,-9,-6,9,1,9],[2,-2,4,-9,-3,-8,-5,-5,-10,1,-1,-7,3],[2,1,-3,-3,-6,-1,7,-2,-10,-5,-9,9,8],[-2,10,-2,-3,-4,-6,3,5,10,7,-6,-8,-3],[-5,-9,-4,-10,8,7,-7,-8,-9,4,5,5,-6],[1,9,3,6,-10,4,-5,4,-6,6,-3,-6,-8],[-2,3,3,2,-7,7,-8,6,-1,-4,6,5,5],[6,4,2,-8,-4,10,2,-2,5,-7,9,3,-2],[-5,-10,4,4,1,-6,3,-7,-7,-4,-7,8,-9]]], dtype = "uint64")#candidate|3703|(12, 15, 13)|const|uint64
bop_3704 = relay.subtract(var_3702.astype('uint64'), const_3703.astype('uint64')) # shape=(12, 15, 13)
uop_3707 = relay.asin(const_3703.astype('float32')) # shape=(12, 15, 13)
output = relay.Tuple([bop_3704,uop_3707,])
output2 = relay.Tuple([bop_3704,uop_3707,])
func_3715 = relay.Function([var_3702,], output)
mod['func_3715'] = func_3715
mod = relay.transform.InferType()(mod)
mutated_mod['func_3715'] = func_3715
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3716 = relay.var("var_3716", dtype = "uint64", shape = ())#candidate|3716|()|var|uint64
func_3715_call = mutated_mod.get_global_var('func_3715')
call_3717 = func_3715_call(var_3716)
output = call_3717
func_3718 = relay.Function([var_3716], output)
mutated_mod['func_3718'] = func_3718
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3658_call = mod.get_global_var('func_3658')
func_3660_call = mutated_mod.get_global_var('func_3660')
call_3747 = relay.TupleGetItem(func_3658_call(), 0)
call_3748 = relay.TupleGetItem(func_3660_call(), 0)
uop_3749 = relay.log2(call_3747.astype('float32')) # shape=(14, 9, 6)
uop_3751 = relay.log2(call_3748.astype('float32')) # shape=(14, 9, 6)
output = relay.Tuple([uop_3749,])
output2 = relay.Tuple([uop_3751,])
func_3761 = relay.Function([], output)
mod['func_3761'] = func_3761
mod = relay.transform.InferType()(mod)
output = func_3761()
func_3762 = relay.Function([], output)
mutated_mod['func_3762'] = func_3762
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3658_call = mod.get_global_var('func_3658')
func_3660_call = mutated_mod.get_global_var('func_3660')
call_3793 = relay.TupleGetItem(func_3658_call(), 0)
call_3794 = relay.TupleGetItem(func_3660_call(), 0)
output = relay.Tuple([call_3793,])
output2 = relay.Tuple([call_3794,])
func_3802 = relay.Function([], output)
mod['func_3802'] = func_3802
mod = relay.transform.InferType()(mod)
mutated_mod['func_3802'] = func_3802
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3802_call = mutated_mod.get_global_var('func_3802')
call_3803 = func_3802_call()
output = call_3803
func_3804 = relay.Function([], output)
mutated_mod['func_3804'] = func_3804
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3802_call = mod.get_global_var('func_3802')
func_3804_call = mutated_mod.get_global_var('func_3804')
call_3812 = relay.TupleGetItem(func_3802_call(), 0)
call_3813 = relay.TupleGetItem(func_3804_call(), 0)
func_925_call = mod.get_global_var('func_925')
func_928_call = mutated_mod.get_global_var('func_928')
const_3828 = relay.const([5.610392,-3.003983,-7.342833,-4.908127,3.070326,9.292107,-0.775150,0.505656,5.124035,7.601864,3.276053,-3.414379,-8.343485,-3.419869,-0.729224,6.230610,4.960172,-5.787414,-9.222951,-8.507441,9.005041,4.778843,2.243616,-1.004978,8.027596,9.010372,-1.924682,-6.133257,4.815659,-4.167168,8.905388,-7.366333,4.419977,7.518094,5.322754,7.965304,2.100850,-2.850008,7.180822,3.292953,-9.789709,3.384337,-6.121512,2.366344,8.839543,5.187763,-2.051859,9.735694,-7.490892,6.107727,-9.415522,-8.180103,2.122339,-1.395252,0.317445,9.936458,1.167978,-4.128558,7.497370,9.623538,9.431423,0.838651,-3.867964,-1.406892,3.071255,4.783049,-8.561856,4.827932,-4.583587,1.421443,4.895084,-0.962781,8.266101,-0.637668,-5.357327,0.671763,-3.175587,5.999334,8.530277,4.512361,3.036779,8.080545,6.039777,1.409121,-5.823671,9.912336,-8.749520,-8.467567,4.779390,-9.158604,3.978539,7.541655,-5.799883,-3.642655,-4.368436,2.746565,-6.865194,-3.199464,2.390521,-2.908535,-1.049864,-6.191480,5.530143,-6.442429,4.992043,-9.641816,0.589048,5.564608,1.106576,4.015094,0.449871,0.091043,5.183736,0.504540,-4.223857,8.305551,-0.998803,9.528238,-1.575406,-9.911354,-5.386330,-4.177118,-8.133539,7.354606,-3.076839,-8.113882,8.451442,3.266232,3.310187,-9.564839,-7.362352,-9.957627,9.284703,-5.184600,8.034973,7.657493,-5.784309,6.046925,1.672147,-9.792093,-2.659339,-0.933917,-1.365473,-1.515570,-1.952564,5.899551,-0.399008,5.506949,4.237047,-9.202056,-8.915556,-8.029210,4.590477,-8.644563,1.693545,-8.021408,9.267150,2.086301,4.541031,8.124164,-0.948432,-1.986565,-2.857008,-5.045988,-5.355356], dtype = "float32")#candidate|3828|(165,)|const|float32
call_3827 = relay.TupleGetItem(func_925_call(relay.reshape(const_3828.astype('float32'), [11, 15])), 1)
call_3829 = relay.TupleGetItem(func_928_call(relay.reshape(const_3828.astype('float32'), [11, 15])), 1)
func_3715_call = mod.get_global_var('func_3715')
func_3718_call = mutated_mod.get_global_var('func_3718')
var_3842 = relay.var("var_3842", dtype = "uint64", shape = ())#candidate|3842|()|var|uint64
call_3841 = relay.TupleGetItem(func_3715_call(relay.reshape(var_3842.astype('uint64'), [])), 0)
call_3843 = relay.TupleGetItem(func_3718_call(relay.reshape(var_3842.astype('uint64'), [])), 0)
output = relay.Tuple([call_3812,call_3827,const_3828,call_3841,var_3842,])
output2 = relay.Tuple([call_3813,call_3829,const_3828,call_3843,var_3842,])
func_3847 = relay.Function([var_3842,], output)
mod['func_3847'] = func_3847
mod = relay.transform.InferType()(mod)
mutated_mod['func_3847'] = func_3847
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3848 = relay.var("var_3848", dtype = "uint64", shape = ())#candidate|3848|()|var|uint64
func_3847_call = mutated_mod.get_global_var('func_3847')
call_3849 = func_3847_call(var_3848)
output = call_3849
func_3850 = relay.Function([var_3848], output)
mutated_mod['func_3850'] = func_3850
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3658_call = mod.get_global_var('func_3658')
func_3660_call = mutated_mod.get_global_var('func_3660')
call_4026 = relay.TupleGetItem(func_3658_call(), 0)
call_4027 = relay.TupleGetItem(func_3660_call(), 0)
var_4033 = relay.var("var_4033", dtype = "float32", shape = (14, 9, 6))#candidate|4033|(14, 9, 6)|var|float32
bop_4034 = relay.mod(call_4026.astype('float64'), relay.reshape(var_4033.astype('float64'), relay.shape_of(call_4026))) # shape=(14, 9, 6)
bop_4037 = relay.mod(call_4027.astype('float64'), relay.reshape(var_4033.astype('float64'), relay.shape_of(call_4027))) # shape=(14, 9, 6)
func_192_call = mod.get_global_var('func_192')
func_195_call = mutated_mod.get_global_var('func_195')
var_4041 = relay.var("var_4041", dtype = "bool", shape = (1980,))#candidate|4041|(1980,)|var|bool
call_4040 = relay.TupleGetItem(func_192_call(relay.reshape(var_4041.astype('bool'), [12, 11, 15])), 0)
call_4042 = relay.TupleGetItem(func_195_call(relay.reshape(var_4041.astype('bool'), [12, 11, 15])), 0)
uop_4045 = relay.atan(bop_4034.astype('float32')) # shape=(14, 9, 6)
uop_4047 = relay.atan(bop_4037.astype('float32')) # shape=(14, 9, 6)
uop_4053 = relay.sqrt(uop_4045.astype('float32')) # shape=(14, 9, 6)
uop_4055 = relay.sqrt(uop_4047.astype('float32')) # shape=(14, 9, 6)
output = relay.Tuple([call_4040,var_4041,uop_4053,])
output2 = relay.Tuple([call_4042,var_4041,uop_4055,])
func_4061 = relay.Function([var_4033,var_4041,], output)
mod['func_4061'] = func_4061
mod = relay.transform.InferType()(mod)
var_4062 = relay.var("var_4062", dtype = "float32", shape = (14, 9, 6))#candidate|4062|(14, 9, 6)|var|float32
var_4063 = relay.var("var_4063", dtype = "bool", shape = (1980,))#candidate|4063|(1980,)|var|bool
output = func_4061(var_4062,var_4063,)
func_4064 = relay.Function([var_4062,var_4063,], output)
mutated_mod['func_4064'] = func_4064
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3658_call = mod.get_global_var('func_3658')
func_3660_call = mutated_mod.get_global_var('func_3660')
call_4085 = relay.TupleGetItem(func_3658_call(), 0)
call_4086 = relay.TupleGetItem(func_3660_call(), 0)
func_1553_call = mod.get_global_var('func_1553')
func_1555_call = mutated_mod.get_global_var('func_1555')
var_4088 = relay.var("var_4088", dtype = "int8", shape = (780,))#candidate|4088|(780,)|var|int8
call_4087 = relay.TupleGetItem(func_1553_call(relay.reshape(var_4088.astype('int8'), [4, 13, 15])), 0)
call_4089 = relay.TupleGetItem(func_1555_call(relay.reshape(var_4088.astype('int8'), [4, 13, 15])), 0)
output = relay.Tuple([call_4085,call_4087,var_4088,])
output2 = relay.Tuple([call_4086,call_4089,var_4088,])
func_4099 = relay.Function([var_4088,], output)
mod['func_4099'] = func_4099
mod = relay.transform.InferType()(mod)
mutated_mod['func_4099'] = func_4099
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4100 = relay.var("var_4100", dtype = "int8", shape = (780,))#candidate|4100|(780,)|var|int8
func_4099_call = mutated_mod.get_global_var('func_4099')
call_4101 = func_4099_call(var_4100)
output = call_4101
func_4102 = relay.Function([var_4100], output)
mutated_mod['func_4102'] = func_4102
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4104 = relay.var("var_4104", dtype = "float32", shape = (16, 2, 10))#candidate|4104|(16, 2, 10)|var|float32
const_4105 = relay.const([[[4.289493,3.511409,6.822806,4.571084,-6.265439,-5.334278,-7.648271,-3.564855,-0.372820,-8.968491],[1.098836,1.805356,-3.317440,7.010194,-2.327375,-2.616501,-4.915569,-8.630075,-8.251061,-9.411731]],[[8.450173,2.580923,-3.266829,-0.258388,5.313472,-5.183054,9.232652,-4.431641,9.992729,0.442988],[-4.310635,-6.441641,4.046574,-3.342835,-0.938225,-8.176405,-0.178965,2.543681,-3.302698,1.581799]],[[-4.976851,-8.047218,6.031237,0.660686,-3.046215,-3.556249,-4.643593,-3.456722,3.477030,4.947711],[4.649239,4.145118,-4.998499,-3.882351,-4.672226,-0.123688,9.212094,0.219661,8.954714,-8.559398]],[[9.720366,-5.827484,1.038325,6.728828,3.924336,-5.012477,-4.834388,-9.594730,4.211215,3.025839],[-9.916002,-6.550501,8.293474,-6.834409,7.367580,-9.438446,6.197377,-2.445448,8.609096,9.866803]],[[8.868016,8.118663,2.248453,-9.108358,9.186729,4.697227,0.558109,4.551037,4.740503,0.730463],[-8.188304,9.082490,-2.649353,-0.712061,6.890908,-9.806222,-6.081042,-2.826176,-6.331848,-8.496174]],[[5.338477,2.819037,9.288000,4.514311,0.390566,3.567471,-0.104785,7.831913,4.343200,0.196412],[-4.262020,2.144769,1.082103,-5.010699,-0.388863,7.854759,-2.556583,-4.333454,-9.556535,-2.764996]],[[-4.713130,3.985192,-8.772067,7.172714,5.405439,-2.695081,-1.912422,-0.418168,-4.608369,7.634918],[7.476898,-5.114823,-7.045617,6.467782,-6.224010,-0.348078,-2.692681,4.007189,-5.538934,-9.769289]],[[9.137974,5.998716,-4.395893,-7.374093,1.310459,3.097306,-7.948450,-5.612790,-2.276968,5.385405],[-7.169319,8.602385,-3.936364,0.207198,4.636843,-8.407200,0.967248,-2.087674,4.615214,-2.109400]],[[5.493700,1.678485,4.055129,-6.764336,0.961421,-2.319729,2.182683,-6.373188,-4.143791,-1.334883],[5.881853,7.521529,4.247455,-6.762383,-0.569078,8.211360,-9.191678,0.261827,-3.445901,7.123446]],[[-9.807243,0.073979,3.122278,8.002700,-4.982503,6.851236,-8.531608,-7.732036,8.585366,-5.000163],[3.941500,6.342544,-6.314645,7.509123,-4.586560,-5.613755,-1.341471,-9.651847,-8.496340,6.182347]],[[3.534647,-9.593849,0.301719,2.141277,-3.447593,-9.246798,1.354075,1.394903,4.891164,6.089214],[-5.231699,-8.836329,3.274382,-5.915336,-7.543453,-3.288667,6.944990,6.002803,5.447562,2.590283]],[[-2.872432,4.829559,5.693067,3.322519,7.599693,-6.627447,-3.705185,-3.266551,6.917709,4.369205],[9.175922,5.729329,9.213882,5.922799,-7.235834,-3.116160,5.980289,-1.963611,-8.560020,9.390789]],[[-3.145746,3.408043,-0.449724,8.994368,8.414063,1.513800,-6.671463,7.418476,0.311207,6.973716],[7.777844,-6.848720,8.253695,6.308441,-6.424463,-3.533329,-9.019209,8.875868,5.827727,-1.083825]],[[-1.363446,5.170806,-3.982873,-8.257665,-8.189633,0.353182,6.960257,-0.241658,2.841832,-7.790813],[-9.461626,-5.738705,6.198408,9.214911,-6.093319,9.228922,3.712465,-9.892525,7.206290,7.023792]],[[-6.004484,2.093271,-9.071449,-8.333781,9.396023,6.211720,8.712261,-5.116446,2.326943,-5.244812],[5.730421,-0.952070,-3.201246,-6.322311,0.162352,4.103671,2.873101,3.174770,-1.453477,3.074867]],[[5.789368,5.351510,-3.285528,6.882495,3.885095,-5.071306,3.510813,9.878413,9.796730,2.089965],[9.143760,-9.095601,2.399857,-9.199937,6.045956,6.089610,-7.274146,-9.452542,-3.905619,6.051098]]], dtype = "float32")#candidate|4105|(16, 2, 10)|const|float32
bop_4106 = relay.mod(var_4104.astype('float32'), relay.reshape(const_4105.astype('float32'), relay.shape_of(var_4104))) # shape=(16, 2, 10)
output = relay.Tuple([bop_4106,])
output2 = relay.Tuple([bop_4106,])
func_4112 = relay.Function([var_4104,], output)
mod['func_4112'] = func_4112
mod = relay.transform.InferType()(mod)
var_4113 = relay.var("var_4113", dtype = "float32", shape = (16, 2, 10))#candidate|4113|(16, 2, 10)|var|float32
output = func_4112(var_4113)
func_4114 = relay.Function([var_4113], output)
mutated_mod['func_4114'] = func_4114
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3802_call = mod.get_global_var('func_3802')
func_3804_call = mutated_mod.get_global_var('func_3804')
call_4133 = relay.TupleGetItem(func_3802_call(), 0)
call_4134 = relay.TupleGetItem(func_3804_call(), 0)
output = call_4133
output2 = call_4134
func_4135 = relay.Function([], output)
mod['func_4135'] = func_4135
mod = relay.transform.InferType()(mod)
mutated_mod['func_4135'] = func_4135
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4135_call = mutated_mod.get_global_var('func_4135')
call_4136 = func_4135_call()
output = call_4136
func_4137 = relay.Function([], output)
mutated_mod['func_4137'] = func_4137
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3802_call = mod.get_global_var('func_3802')
func_3804_call = mutated_mod.get_global_var('func_3804')
call_4152 = relay.TupleGetItem(func_3802_call(), 0)
call_4153 = relay.TupleGetItem(func_3804_call(), 0)
output = relay.Tuple([call_4152,])
output2 = relay.Tuple([call_4153,])
func_4158 = relay.Function([], output)
mod['func_4158'] = func_4158
mod = relay.transform.InferType()(mod)
output = func_4158()
func_4159 = relay.Function([], output)
mutated_mod['func_4159'] = func_4159
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4158_call = mod.get_global_var('func_4158')
func_4159_call = mutated_mod.get_global_var('func_4159')
call_4175 = relay.TupleGetItem(func_4158_call(), 0)
call_4176 = relay.TupleGetItem(func_4159_call(), 0)
output = relay.Tuple([call_4175,])
output2 = relay.Tuple([call_4176,])
func_4177 = relay.Function([], output)
mod['func_4177'] = func_4177
mod = relay.transform.InferType()(mod)
mutated_mod['func_4177'] = func_4177
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4177_call = mutated_mod.get_global_var('func_4177')
call_4178 = func_4177_call()
output = call_4178
func_4179 = relay.Function([], output)
mutated_mod['func_4179'] = func_4179
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4158_call = mod.get_global_var('func_4158')
func_4159_call = mutated_mod.get_global_var('func_4159')
call_4183 = relay.TupleGetItem(func_4158_call(), 0)
call_4184 = relay.TupleGetItem(func_4159_call(), 0)
output = call_4183
output2 = call_4184
func_4188 = relay.Function([], output)
mod['func_4188'] = func_4188
mod = relay.transform.InferType()(mod)
output = func_4188()
func_4189 = relay.Function([], output)
mutated_mod['func_4189'] = func_4189
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4199 = relay.var("var_4199", dtype = "float32", shape = (14, 11, 8))#candidate|4199|(14, 11, 8)|var|float32
uop_4200 = relay.log(var_4199.astype('float32')) # shape=(14, 11, 8)
output = uop_4200
output2 = uop_4200
func_4203 = relay.Function([var_4199,], output)
mod['func_4203'] = func_4203
mod = relay.transform.InferType()(mod)
mutated_mod['func_4203'] = func_4203
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4204 = relay.var("var_4204", dtype = "float32", shape = (14, 11, 8))#candidate|4204|(14, 11, 8)|var|float32
func_4203_call = mutated_mod.get_global_var('func_4203')
call_4205 = func_4203_call(var_4204)
output = call_4205
func_4206 = relay.Function([var_4204], output)
mutated_mod['func_4206'] = func_4206
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4135_call = mod.get_global_var('func_4135')
func_4137_call = mutated_mod.get_global_var('func_4137')
call_4215 = func_4135_call()
call_4216 = func_4135_call()
const_4222 = relay.const([[[-7.348713,7.126499,9.922022,7.246618,-6.342227,-6.202578],[9.717459,4.124430,-1.459398,3.823578,8.085622,-6.979367],[-9.615091,-6.237633,-8.361511,1.774304,-8.036496,3.366005],[-8.448842,2.860467,-4.404242,-3.152639,4.885061,1.217990],[3.164546,-3.106653,6.701612,0.636214,-1.938302,-1.776499],[0.423927,-3.951923,-3.248975,0.989979,-1.159596,-2.048925],[8.735164,-4.504939,-0.949376,-6.600263,-9.401842,-3.475385],[0.334925,-9.178004,-3.155761,-3.091816,-5.221942,4.013194],[-1.881512,5.056986,-4.090572,-4.276338,-0.034626,-5.366405]],[[-4.915076,-5.321563,9.564097,-8.383401,-3.823782,-3.034835],[-0.757874,6.299109,9.391795,2.146721,4.761276,1.699731],[-1.205500,4.983312,-2.794985,-6.573007,-2.065629,-4.117052],[7.389111,-1.709762,5.694334,-1.592229,-1.110133,-5.076336],[6.396059,3.418973,2.425687,-9.879114,-0.202781,-2.420490],[7.727765,-8.152857,-9.709478,8.610895,5.409340,8.789739],[-3.288254,-9.908865,2.794556,4.374571,0.260171,-7.631370],[8.420258,-3.568789,-2.870121,-6.373312,9.163330,-6.038709],[1.889378,-5.574168,0.376136,8.913933,7.224721,-0.648835]],[[4.377226,2.920747,1.893361,7.275634,-3.228796,-8.707683],[-6.586276,-2.406900,1.503151,6.574722,-7.974229,-8.253566],[-6.633901,-3.227829,7.940525,-1.016303,-7.582275,0.790669],[0.359506,-3.007149,8.688693,0.916826,9.281557,9.866935],[-1.538051,-1.327465,-9.571995,-3.219344,-0.908540,5.429293],[-2.787064,-7.399423,7.927506,-5.967675,-0.260364,2.990524],[5.361691,-8.657059,-2.006088,-0.151444,-1.979772,-8.482591],[4.640540,5.691309,9.989192,9.345223,1.613718,-0.027709],[-5.550201,6.741682,3.049598,-5.514395,7.819148,6.806600]],[[-3.083547,-2.456492,-3.621689,-6.508731,-2.576828,-3.022389],[-3.277732,3.595780,4.464565,-5.587850,-3.218446,3.821865],[-4.672738,-3.155262,-4.239609,-3.123781,7.855236,3.033059],[7.915234,1.888799,-2.858621,1.219949,-9.629373,-0.330136],[-6.282559,8.942958,-1.886920,-5.203018,-8.456210,1.313507],[-9.253453,8.782093,-1.799619,-8.431100,-4.559896,5.744332],[3.372246,9.590717,0.690809,7.435354,3.241958,-4.530717],[4.823872,-0.339204,-0.791786,-7.216699,9.710930,-1.478702],[8.389736,0.905797,0.635919,-9.151409,2.332334,-1.902705]],[[1.828707,-4.488045,-6.698660,-1.837446,1.280516,5.984701],[-0.606849,5.796165,2.284351,-8.671861,-0.040001,6.431804],[-0.949704,-9.280441,7.964027,9.690267,-5.638090,8.789439],[-8.039256,4.090797,0.090504,8.193534,-2.669505,7.883467],[2.540246,-2.005595,-4.127909,5.636510,0.389467,-5.950240],[-6.809596,8.292713,-9.652700,4.641616,7.080852,-7.437203],[0.624781,-9.298333,-7.753730,4.084941,9.112379,4.261554],[1.204476,4.298522,-7.922229,-5.184321,7.907489,-9.954646],[-0.303325,-8.847152,-0.044455,-2.970905,0.342919,4.678039]],[[1.147384,5.539301,9.141858,-2.099100,5.561935,6.662483],[2.784662,-9.596039,-2.984691,-7.135587,-6.266755,-2.298658],[-7.713803,-6.133183,2.079766,1.614064,-7.574678,-4.698874],[-2.383278,5.540526,-6.250082,8.892863,-8.688136,-9.060878],[-1.745276,8.400576,4.493546,9.069797,1.093971,6.024476],[-6.544509,8.223556,8.853114,-7.699262,-9.604687,1.413262],[-2.879134,-6.350500,-7.728644,1.274947,-3.729493,1.264871],[-8.553305,1.619770,-7.761571,2.978284,2.181116,-3.685963],[-6.515746,-2.326741,-7.015416,5.454841,6.249911,5.743273]],[[-0.128551,-8.639526,4.038788,-4.858163,0.298691,2.096026],[0.464629,-9.352884,8.041350,8.926078,7.372868,-5.253185],[-8.265917,-4.802690,-3.818530,5.197950,2.322914,8.740744],[-0.436275,-3.051746,0.645781,6.674378,-9.727714,3.203836],[-6.463254,8.112165,7.715088,1.558211,7.255207,9.209733],[3.768706,-4.923699,-8.203924,-5.714573,-6.818108,-3.924365],[-9.738216,-3.587913,8.803277,4.207311,-6.633690,8.949960],[-6.665829,2.769805,1.608942,2.180576,-8.421123,1.094630],[9.538151,5.600479,-4.453148,7.939224,7.506448,-2.520934]],[[-0.870981,6.709050,-4.313213,-6.406712,7.526781,9.262845],[-8.106681,-6.926719,-2.416508,8.914106,8.215964,9.222837],[7.880006,-4.343707,-4.535783,8.508399,-8.505657,-6.671843],[-1.977081,-8.399116,-8.398826,-1.043297,-9.591656,1.752936],[-8.817641,9.137724,8.930777,4.321693,5.242139,-8.719226],[-6.334790,-6.162440,-2.240044,-8.082578,6.142963,-4.042778],[-2.235569,-3.186252,1.068499,7.348215,8.308015,7.585919],[-7.399458,7.528756,6.561560,5.348668,1.136890,-6.367509],[-6.043834,-5.640611,3.113263,-4.305235,5.953811,1.568966]],[[-4.523592,-6.674753,2.254888,1.905612,8.818178,5.771549],[-5.221744,-2.815839,3.263439,7.937812,5.439734,6.085704],[-8.701837,-2.470892,7.019844,9.552760,3.866437,0.668607],[2.103059,-2.849906,8.808308,8.921677,-1.395357,9.995954],[7.141887,-3.028874,0.892820,2.829581,5.756671,4.145514],[4.372864,-8.371204,6.557773,7.776229,-7.509016,2.659432],[-5.493317,7.171001,-9.490828,-8.613276,1.123704,1.499820],[-4.694455,3.023111,-0.552100,-3.509435,5.677848,-8.274940],[-4.277331,4.825755,2.615426,-9.278066,-3.169826,7.037707]],[[1.002219,-6.392077,-5.992419,4.693867,-1.729133,-2.722552],[9.007386,0.869663,6.919118,9.532154,4.912434,8.314159],[3.512008,-5.264189,3.652037,6.433997,0.074669,-3.936171],[0.377483,2.245279,-1.006870,-4.373138,-3.010000,-8.635514],[-4.295133,-4.681279,-7.719291,-9.811402,4.930915,9.162380],[-4.798829,4.614322,-8.183515,4.918442,8.465694,-9.794586],[-3.634194,-7.510419,-3.232898,2.677720,-9.783423,-4.727852],[0.388449,3.298438,-4.854958,4.751352,7.673616,-5.342860],[-5.437605,6.843805,-2.609769,3.197871,-0.496716,-4.774744]],[[-3.305229,6.956546,1.170125,-1.053206,9.200239,6.078887],[-2.907160,-4.829510,-6.444952,-6.162875,2.807746,-8.693622],[3.538917,-1.572461,7.915166,-7.221656,-4.026688,1.615177],[4.997082,-9.916831,9.695956,-9.705875,0.179747,2.126818],[-3.408375,-2.670436,0.375240,1.017529,5.360567,-0.897735],[-9.606917,-9.850418,6.762366,-8.666070,6.619107,0.080941],[6.722633,6.976972,-7.523438,-9.382176,-7.856440,-5.672025],[9.988694,-2.602960,-5.745921,-2.157249,2.942181,6.783057],[-0.676232,2.649256,8.701227,-8.001841,7.913271,8.446203]],[[-6.372163,-5.951098,-3.588353,-8.392717,-3.979337,-5.521785],[8.371474,-0.667116,-5.271929,2.412825,8.618820,-3.495936],[2.619455,4.810589,-4.583703,7.882738,-0.985925,8.261312],[-1.187076,9.871701,-3.190604,4.988669,-6.699162,-0.022535],[-7.258634,8.784952,3.639112,-0.470913,-7.290626,4.586226],[-2.959830,7.010272,-5.929990,5.545679,-7.796922,4.295650],[6.692502,-2.849422,-5.389666,-4.147445,2.276360,9.899909],[5.585644,4.198306,7.356162,2.784200,6.077949,9.093102],[5.992479,3.095016,8.639413,3.864576,7.792171,-7.257385]],[[-0.904078,-4.064340,-4.380117,-9.544896,3.070505,6.780831],[-5.518617,-1.874544,9.854016,7.057264,9.463931,-7.157914],[-6.627588,9.918278,1.399488,6.365221,-2.835330,7.342716],[4.421756,-8.832822,-9.227588,-8.835923,-1.050075,-1.227521],[-7.892316,4.351354,-4.077131,-8.915314,5.620413,0.089884],[1.640065,-1.519114,-7.839689,-5.229634,-8.474725,3.123006],[-1.319206,1.132646,-2.624412,-2.619691,-3.621679,-7.438065],[7.378273,4.175839,-5.955593,3.005250,6.733899,8.970551],[-8.382303,-1.519168,2.162485,4.036665,4.314492,-6.799427]],[[-5.701573,-5.860854,-2.655936,-8.450156,5.674172,-5.941869],[-8.852835,3.534624,-2.817659,0.876659,-0.533594,7.076957],[3.629708,4.984783,1.428686,6.327559,-7.224747,-6.031098],[-2.135996,-6.325607,-1.820095,-7.461796,-8.346794,3.021501],[-3.403618,5.606824,-8.081987,-4.993180,4.352338,-2.416944],[-5.435034,6.069382,2.222214,6.410791,-1.878304,5.941424],[0.762282,5.418352,4.914372,-7.682627,3.953842,-9.833406],[-2.449781,-3.983343,-6.635743,-5.791437,-6.591422,2.619176],[-7.497161,1.907072,-6.411617,8.117098,-6.293540,0.442852]]], dtype = "float32")#candidate|4222|(14, 9, 6)|const|float32
bop_4223 = relay.floor_divide(call_4215.astype('float32'), relay.reshape(const_4222.astype('float32'), relay.shape_of(call_4215))) # shape=(14, 9, 6)
bop_4226 = relay.floor_divide(call_4216.astype('float32'), relay.reshape(const_4222.astype('float32'), relay.shape_of(call_4216))) # shape=(14, 9, 6)
uop_4227 = relay.asin(bop_4223.astype('float32')) # shape=(14, 9, 6)
uop_4229 = relay.asin(bop_4226.astype('float32')) # shape=(14, 9, 6)
func_3389_call = mod.get_global_var('func_3389')
func_3392_call = mutated_mod.get_global_var('func_3392')
const_4232 = relay.const([-2.962599,-7.855050,-3.984763,2.307060,3.142680,5.332042,-5.850584,-2.268562,5.704217,9.888789,-2.370016,-9.119118,-3.390176,-7.121652,3.085567,-7.013489,8.228256,-4.443999,-5.703465,7.544540,9.551304,-3.749891,6.685850,8.527770,2.583116,4.583747,8.005474,0.838052,1.039236,-7.044260,-0.301227,-0.467330,8.774769,4.354213,-1.394217,8.523504,-8.851218,3.564150,-8.272889,-2.451063,-2.691014,8.062761,-7.131251,2.469436,-2.123614,-1.927216,-8.931587,-0.819411,3.276721,2.512622,7.508402,1.356175,4.702138,2.538657,7.237989,1.569285,6.309242,-8.140048,2.353573,6.041237,8.569058,-9.900297,-6.031430,6.455895,9.264073,4.474787,3.500036,-0.304431,8.482833,-9.056561,1.896785,-8.813670,-4.589681,-9.993134,-5.942364,-9.039774,5.853842,-7.668089,2.848901,7.218442,-0.579401,8.723777,-4.767352,-0.992578,6.660650,-1.500435,-3.628616,6.661332,4.182103,6.155468,0.034834,4.181499,-6.035874,-3.621379,3.500745,-1.212904,-2.678214,0.966326,2.215741,2.697900,-2.215098,-9.775442,-8.376988,-5.577188,8.340090,-1.507847,3.694828,-9.325433,7.760081,0.527295,-1.963165,-8.656805,-9.556321,1.250012,-8.728358,-2.443618,6.387483,8.132990,5.189255,7.253740], dtype = "float64")#candidate|4232|(120,)|const|float64
call_4231 = func_3389_call(relay.reshape(const_4232.astype('float64'), [12, 2, 5]))
call_4233 = func_3389_call(relay.reshape(const_4232.astype('float64'), [12, 2, 5]))
output = relay.Tuple([uop_4227,call_4231,const_4232,])
output2 = relay.Tuple([uop_4229,call_4233,const_4232,])
func_4241 = relay.Function([], output)
mod['func_4241'] = func_4241
mod = relay.transform.InferType()(mod)
output = func_4241()
func_4242 = relay.Function([], output)
mutated_mod['func_4242'] = func_4242
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4158_call = mod.get_global_var('func_4158')
func_4159_call = mutated_mod.get_global_var('func_4159')
call_4281 = relay.TupleGetItem(func_4158_call(), 0)
call_4282 = relay.TupleGetItem(func_4159_call(), 0)
output = relay.Tuple([call_4281,])
output2 = relay.Tuple([call_4282,])
func_4283 = relay.Function([], output)
mod['func_4283'] = func_4283
mod = relay.transform.InferType()(mod)
output = func_4283()
func_4284 = relay.Function([], output)
mutated_mod['func_4284'] = func_4284
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3761_call = mod.get_global_var('func_3761')
func_3762_call = mutated_mod.get_global_var('func_3762')
call_4285 = relay.TupleGetItem(func_3761_call(), 0)
call_4286 = relay.TupleGetItem(func_3762_call(), 0)
var_4287 = relay.var("var_4287", dtype = "float32", shape = (14, 9, 6))#candidate|4287|(14, 9, 6)|var|float32
bop_4288 = relay.power(call_4285.astype('float32'), relay.reshape(var_4287.astype('float32'), relay.shape_of(call_4285))) # shape=(14, 9, 6)
bop_4291 = relay.power(call_4286.astype('float32'), relay.reshape(var_4287.astype('float32'), relay.shape_of(call_4286))) # shape=(14, 9, 6)
func_3802_call = mod.get_global_var('func_3802')
func_3804_call = mutated_mod.get_global_var('func_3804')
call_4294 = relay.TupleGetItem(func_3802_call(), 0)
call_4295 = relay.TupleGetItem(func_3804_call(), 0)
func_4177_call = mod.get_global_var('func_4177')
func_4179_call = mutated_mod.get_global_var('func_4179')
call_4299 = relay.TupleGetItem(func_4177_call(), 0)
call_4300 = relay.TupleGetItem(func_4179_call(), 0)
output = relay.Tuple([bop_4288,call_4294,call_4299,])
output2 = relay.Tuple([bop_4291,call_4295,call_4300,])
func_4343 = relay.Function([var_4287,], output)
mod['func_4343'] = func_4343
mod = relay.transform.InferType()(mod)
var_4344 = relay.var("var_4344", dtype = "float32", shape = (14, 9, 6))#candidate|4344|(14, 9, 6)|var|float32
output = func_4343(var_4344)
func_4345 = relay.Function([var_4344], output)
mutated_mod['func_4345'] = func_4345
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4177_call = mod.get_global_var('func_4177')
func_4179_call = mutated_mod.get_global_var('func_4179')
call_4386 = relay.TupleGetItem(func_4177_call(), 0)
call_4387 = relay.TupleGetItem(func_4179_call(), 0)
output = relay.Tuple([call_4386,])
output2 = relay.Tuple([call_4387,])
func_4398 = relay.Function([], output)
mod['func_4398'] = func_4398
mod = relay.transform.InferType()(mod)
output = func_4398()
func_4399 = relay.Function([], output)
mutated_mod['func_4399'] = func_4399
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4283_call = mod.get_global_var('func_4283')
func_4284_call = mutated_mod.get_global_var('func_4284')
call_4490 = relay.TupleGetItem(func_4283_call(), 0)
call_4491 = relay.TupleGetItem(func_4284_call(), 0)
var_4504 = relay.var("var_4504", dtype = "float32", shape = (14, 9, 6))#candidate|4504|(14, 9, 6)|var|float32
bop_4505 = relay.floor_mod(call_4490.astype('float64'), relay.reshape(var_4504.astype('float64'), relay.shape_of(call_4490))) # shape=(14, 9, 6)
bop_4508 = relay.floor_mod(call_4491.astype('float64'), relay.reshape(var_4504.astype('float64'), relay.shape_of(call_4491))) # shape=(14, 9, 6)
func_2269_call = mod.get_global_var('func_2269')
func_2272_call = mutated_mod.get_global_var('func_2272')
var_4527 = relay.var("var_4527", dtype = "float32", shape = (1080,))#candidate|4527|(1080,)|var|float32
call_4526 = relay.TupleGetItem(func_2269_call(relay.reshape(var_4527.astype('float32'), [15, 8, 9])), 0)
call_4528 = relay.TupleGetItem(func_2272_call(relay.reshape(var_4527.astype('float32'), [15, 8, 9])), 0)
output = relay.Tuple([bop_4505,call_4526,var_4527,])
output2 = relay.Tuple([bop_4508,call_4528,var_4527,])
func_4529 = relay.Function([var_4504,var_4527,], output)
mod['func_4529'] = func_4529
mod = relay.transform.InferType()(mod)
var_4530 = relay.var("var_4530", dtype = "float32", shape = (14, 9, 6))#candidate|4530|(14, 9, 6)|var|float32
var_4531 = relay.var("var_4531", dtype = "float32", shape = (1080,))#candidate|4531|(1080,)|var|float32
output = func_4529(var_4530,var_4531,)
func_4532 = relay.Function([var_4530,var_4531,], output)
mutated_mod['func_4532'] = func_4532
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4135_call = mod.get_global_var('func_4135')
func_4137_call = mutated_mod.get_global_var('func_4137')
call_4536 = func_4135_call()
call_4537 = func_4135_call()
output = relay.Tuple([call_4536,])
output2 = relay.Tuple([call_4537,])
func_4542 = relay.Function([], output)
mod['func_4542'] = func_4542
mod = relay.transform.InferType()(mod)
output = func_4542()
func_4543 = relay.Function([], output)
mutated_mod['func_4543'] = func_4543
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3802_call = mod.get_global_var('func_3802')
func_3804_call = mutated_mod.get_global_var('func_3804')
call_4551 = relay.TupleGetItem(func_3802_call(), 0)
call_4552 = relay.TupleGetItem(func_3804_call(), 0)
func_4112_call = mod.get_global_var('func_4112')
func_4114_call = mutated_mod.get_global_var('func_4114')
var_4563 = relay.var("var_4563", dtype = "float32", shape = (320,))#candidate|4563|(320,)|var|float32
call_4562 = relay.TupleGetItem(func_4112_call(relay.reshape(var_4563.astype('float32'), [16, 2, 10])), 0)
call_4564 = relay.TupleGetItem(func_4114_call(relay.reshape(var_4563.astype('float32'), [16, 2, 10])), 0)
func_3389_call = mod.get_global_var('func_3389')
func_3392_call = mutated_mod.get_global_var('func_3392')
var_4585 = relay.var("var_4585", dtype = "float64", shape = (120, 1))#candidate|4585|(120, 1)|var|float64
call_4584 = func_3389_call(relay.reshape(var_4585.astype('float64'), [12, 2, 5]))
call_4586 = func_3389_call(relay.reshape(var_4585.astype('float64'), [12, 2, 5]))
func_3183_call = mod.get_global_var('func_3183')
func_3186_call = mutated_mod.get_global_var('func_3186')
var_4590 = relay.var("var_4590", dtype = "float32", shape = (168,))#candidate|4590|(168,)|var|float32
call_4589 = relay.TupleGetItem(func_3183_call(relay.reshape(var_4590.astype('float32'), [1, 12, 14])), 2)
call_4591 = relay.TupleGetItem(func_3186_call(relay.reshape(var_4590.astype('float32'), [1, 12, 14])), 2)
output = relay.Tuple([call_4551,call_4562,var_4563,call_4584,var_4585,call_4589,var_4590,])
output2 = relay.Tuple([call_4552,call_4564,var_4563,call_4586,var_4585,call_4591,var_4590,])
func_4601 = relay.Function([var_4563,var_4585,var_4590,], output)
mod['func_4601'] = func_4601
mod = relay.transform.InferType()(mod)
mutated_mod['func_4601'] = func_4601
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4601_call = mutated_mod.get_global_var('func_4601')
var_4603 = relay.var("var_4603", dtype = "float32", shape = (320,))#candidate|4603|(320,)|var|float32
var_4604 = relay.var("var_4604", dtype = "float64", shape = (120, 1))#candidate|4604|(120, 1)|var|float64
var_4605 = relay.var("var_4605", dtype = "float32", shape = (168,))#candidate|4605|(168,)|var|float32
call_4602 = func_4601_call(var_4603,var_4604,var_4605,)
output = call_4602
func_4606 = relay.Function([var_4603,var_4604,var_4605,], output)
mutated_mod['func_4606'] = func_4606
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4158_call = mod.get_global_var('func_4158')
func_4159_call = mutated_mod.get_global_var('func_4159')
call_4630 = relay.TupleGetItem(func_4158_call(), 0)
call_4631 = relay.TupleGetItem(func_4159_call(), 0)
func_3220_call = mod.get_global_var('func_3220')
func_3223_call = mutated_mod.get_global_var('func_3223')
const_4639 = relay.const([9,-6,-1,-6,3,-10,6,-5,-7,8,-2,-3,-3,3,9,1,-6,-3,-7,9,-9,-10,-2,-5,4,5,4,-9,5,8,3,-4,-6,4,-7,5,2,3,2,7,1,2,-9,10,-4,-10,10,4,2,-9,-2,7,2,10,-9,-10,8,-4,6,3,-4,6,6,10,-9,8,-1,-5,-6,9,-3,-6,2,8,-5,7,-3,-5,-3,4,2,-3,-9,-8,-5,-10,5,-9,-5,-4,-7,2,-3,8,10,10,-6,-6,3,-7,10,-7,5,-1,-5,3,-7,-4,1,-8,4,4,-9,2,-4,-10,-10,1,-5,6,-9,-1,-3,9,-7,-5,-3,10,1,5,2,-2], dtype = "int64")#candidate|4639|(132,)|const|int64
call_4638 = relay.TupleGetItem(func_3220_call(relay.reshape(const_4639.astype('int64'), [2, 11, 6])), 1)
call_4640 = relay.TupleGetItem(func_3223_call(relay.reshape(const_4639.astype('int64'), [2, 11, 6])), 1)
uop_4641 = relay.erf(call_4638.astype('float32')) # shape=(2, 11, 6)
uop_4643 = relay.erf(call_4640.astype('float32')) # shape=(2, 11, 6)
func_4061_call = mod.get_global_var('func_4061')
func_4064_call = mutated_mod.get_global_var('func_4064')
const_4648 = relay.const([True,False,False,False,True,False,True,True,False,True,False,True,False,False,True,True,False,True,False,True,True,False,False,False,True,True,False,False,True,False,False,False,False,False,False,True,False,True,False,True,False,True,False,False,True,False,True,True,True,True,True,False,True,True,True,False,False,True,True,True,True,True,True,True,True,True,False,False,False,True,True,False,False,True,False,True,True,True,True,True,True,False,True,False,True,False,True,True,True,False,True,False,True,False,True,False,False,False,False,False,True,True,True,True,True,True,False,False,True,True,True,False,True,True,False,False,True,True,False,True,True,True,True,False,True,True,True,True,True,True,False,False,True,True,True,False,False,True,False,True,True,False,True,False,True,False,True,False,True,True,True,True,False,True,True,True,False,False,True,True,False,True,True,True,False,False,True,False,True,True,False,False,True,True,True,False,True,False,True,True,True,False,False,True,True,True,False,True,False,True,False,False,False,True,True,False,True,False,True,True,True,True,True,True,False,False,True,False,False,False,True,True,True,True,False,False,False,True,False,False,False,False,False,True,False,True,True,True,True,False,False,True,True,False,False,False,False,True,False,True,False,True,False,True,False,True,True,False,False,True,True,False,False,True,True,False,True,True,True,False,True,False,True,True,False,True,True,False,True,True,True,True,False,False,False,False,True,True,False,True,True,True,True,True,True,True,True,False,False,False,False,True,False,False,False,False,True,True,True,False,False,False,True,False,False,True,False,True,True,True,False,False,False,False,True,True,True,False,True,True,False,False,False,True,False,True,True,True,False,False,False,True,True,True,True,True,True,False,True,False,True,True,False,True,True,True,True,False,True,False,True,True,False,False,False,False,True,False,False,True,False,False,False,True,True,False,True,False,False,False,False,True,True,False,False,True,True,True,True,False,False,True,False,False,True,False,True,False,False,True,True,True,True,False,False,False,False,True,True,False,True,True,True,True,False,True,False,True,True,True,False,True,False,False,True,True,False,False,True,True,True,True,False,False,True,False,True,True,False,False,True,True,True,False,False,True,True,False,True,False,False,True,True,False,True,True,False,True,True,True,False,True,False,False,True,True,True,False,False,True,False,True,False,False,True,True,True,True,True,False,True,True,True,True,False,False,False,False,False,True,True,False,False,False,True,False,True,False,False,False,True,True,True,True,True,True,False,False,False,False,True,True,True,False,False,True,True,False,True,True,False,True,True,False,True,False,False,False,False,True,False,True,False,False,True,True,True,True,True,True,True,False,False,True,True,True,False,False,True,False,True,True,True,False,False,False,True,False,False,True,True,True,True,True,True,False,False,False,True,False,True,True,False,True,False,True,False,False,True,False,False,False,True,True,True,True,True,False,False,False,True,True,True,False,True,False,False,True,False,False,True,True,True,False,False,True,True,True,True,True,True,False,True,False,True,False,False,True,False,False,True,False,True,False,False,False,False,True,False,False,True,True,True,False,True,True,True,True,False,False,False,True,False,True,False,False,False,False,True,False,False,False,False,True,False,True,False,False,False,False,False,True,True,True,True,True,False,False,False,True,False,False,False,True,True,False,True,True,False,False,False,False,False,False,False,False,True,False,False,True,False,False,False,True,True,True,False,True,True,False,False,False,False,True,True,False,True,False,True,False,False,True,False,False,False,False,False,True,False,False,True,False,False,True,False,True,True,False,False,False,True,True,False,True,False,True,True,True,True,True,True,True,False,False,True,False,False,True,False,True,True,True,True,True,False,True,False,True,False,True,False,True,False,False,False,False,False,False,True,True,True,True,True,True,True,False,False,True,False,False,False,True,True,False,True,True,True,True,True,True,False,True,False,False,True,True,False,True,True,False,True,False,True,False,True,False,False,True,True,False,True,False,False,False,False,True,False,True,False,True,True,True,False,True,True,True,False,False,True,True,False,False,True,True,False,True,True,False,False,False,True,False,False,True,False,False,False,False,False,False,True,True,True,True,False,True,True,True,True,False,False,True,False,False,False,False,True,True,False,True,True,True,True,False,False,False,False,False,False,False,True,False,True,False,True,False,True,False,True,False,False,True,True,False,True,True,False,False,False,True,False,False,False,True,False,True,True,False,True,False,True,False,False,False,True,True,False,False,False,True,True,False,True,False,True,False,False,True,True,False,False,True,False,True,False,False,False,False,True,True,False,False,False,False,False,True,True,True,True,True,False,False,False,True,True,True,False,True,False,True,True,True,False,False,False,False,False,False,False,True,True,False,True,True,False,False,False,False,True,False,True,True,False,True,True,True,False,True,False,True,False,False,False,False,False,False,False,False,False,True,False,True,True,True,True,False,True,True,False,False,True,True,False,False,True,True,True,True,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,True,False,True,True,True,False,True,False,False,False,False,False,True,True,True,True,True,True,True,True,True,False,True,True,False,True,False,True,True,False,True,False,False,False,True,False,False,False,False,False,False,False,False,False,True,False,True,False,True,False,True,True,False,False,False,True,True,False,False,False,True,True,False,True,True,True,True,True,True,True,False,False,True,False,False,False,False,True,False,False,True,True,True,False,True,True,True,True,False,True,True,True,False,False,False,True,True,False,False,True,True,False,True,True,True,True,True,True,False,False,True,True,True,False,True,True,False,False,False,False,True,True,True,True,True,True,False,True,True,True,False,True,True,True,False,False,False,True,False,False,True,True,True,True,False,True,False,False,True,False,False,True,True,True,False,True,False,True,False,False,False,False,True,True,True,True,False,True,False,False,True,False,True,False,True,True,True,True,True,True,True,True,False,False,False,False,True,True,True,True,True,True,True,False,True,False,True,True,True,True,True,False,True,False,True,False,False,False,True,True,True,False,True,True,True,True,False,False,False,True,False,True,True,True,True,False,False,False,True,True,False,False,False,True,False,True,False,False,True,True,False,True,False,True,False,True,False,False,True,True,False,True,False,True,True,False,True,True,False,False,False,False,False,False,False,False,True,False,True,True,True,True,False,True,False,False,False,False,True,False,True,True,True,False,False,False,False,True,True,False,True,False,True,True,False,True,True,False,True,False,True,False,True,True,False,True,True,False,False,False,False,True,True,False,True,True,False,True,False,False,False,True,False,True,False,False,False,False,False,True,False,True,True,False,False,True,True,False,False,True,False,False,True,False,False,False,True,True,False,False,True,False,True,True,True,False,True,True,False,False,False,False,True,True,False,False,True,False,False,True,True,False,True,False,False,False,True,False,True,True,False,False,True,True,True,False,True,False,True,True,False,True,False,False,False,False,False,True,False,False,False,False,False,False,False,True,False,True,True,True,False,True,True,True,False,False,True,False,False,False,True,True,True,True,True,False,False,True,True,False,True,False,False,True,False,True,False,False,False,True,True,True,False,False,False,True,False,False,True,False,False,False,True,False,False,False,False,False,True,True,False,False,True,True,False,True,False,False,True,False,False,False,True,False,False,False,True,False,False,False,True,False,True,False,False,True,True,False,True,False,False,True,True,True,False,True,True,False,True,False,True,True,True,False,False,True,False,True,False,False,False,True,True,True,True,True,False,False,False,True,True,False,False,False,True,True,True,False,True,False,True,False,False,False,True,False,True,True,True,True,False,True,False,True,False,False,False,False,False,False,True,True,False,False,True,False,True,False,False,False,True,True,True,True,True,False,True,True,True,False,False,True,False,True,False,False,True,True,True,True,True,False,True,False,False,False,False,True,True,False,False,False,False,True,True,True,True,False,False,False,False,True,False,False,False,False,True,True,True,False,False,True,False,True,True,True,False,True,False,True,True,False,True,True,True,False,True,False,False,True,True,False,False,True,True,False,True,False,True,True,False,False,False,False,True,True,True,True,False,False,False,True,False,True,True,False,True,False,False,True,True,True,False,False,False,True,False,False,True,False,True,True,False,True,True,True,False,True,True,False,True,True,True,True,True,False,True,False,False,False,False,False,True,False,False,False,True,False,False,False,False,True,True,False,False,False,False,False,True,True,False,False,False,True,False,True,False,True,False,False,True,False,False,True,False,False,True,True,True,True,True,True,False,False,False,False,False,False,False,False,True,False,False,True,True,False,True,True,False,True,False,True,True,False,False,True,True,True,False,False,False,True,True,False,True,True,False,True,True,False,True,False,False,False,False,False,False,True,True,False,False,True,False,True,False,False,False,True,False,False,True,False,True,False,True,False,False,True,True,True,False,True,False,False,True,False,False,True,True,False,False,True,True,False,False,True,False,False,False,False,False,True,True,True,False,False,True,False,True,False,True,True,True,True,False,False,True,False,False,False,False,False,True,False,False,True,True,False,True,False,True,True,True,False,False,True,False,True,True,True,False,True,True,True,False,True,False,False,True,False,False,False,False,False,False,False,True,True,False,True,True,True,False,True,True,True,False,True,False,False,True,False,True,False,False,True,True,False,True,False,False,False,False,False,False,False,False,True,False,False,False,True,False,True,False,True,False,True,True,False,True,False,True,False,False,True,True,True,True,True,True,True,True,False,True,True,False,True,False,False,True,True,False,True,False,False,True,False,True,False,False,False,False,True,False,False,False], dtype = "bool")#candidate|4648|(1980,)|const|bool
call_4647 = relay.TupleGetItem(func_4061_call(relay.reshape(call_4630.astype('float32'), [14, 9, 6]), relay.reshape(const_4648.astype('bool'), [1980,]), ), 1)
call_4649 = relay.TupleGetItem(func_4064_call(relay.reshape(call_4630.astype('float32'), [14, 9, 6]), relay.reshape(const_4648.astype('bool'), [1980,]), ), 1)
var_4659 = relay.var("var_4659", dtype = "bool", shape = (1980,))#candidate|4659|(1980,)|var|bool
bop_4660 = relay.logical_and(const_4648.astype('bool'), relay.reshape(var_4659.astype('bool'), relay.shape_of(const_4648))) # shape=(1980,)
output = relay.Tuple([call_4630,const_4639,uop_4641,call_4647,bop_4660,])
output2 = relay.Tuple([call_4631,const_4639,uop_4643,call_4649,bop_4660,])
func_4664 = relay.Function([var_4659,], output)
mod['func_4664'] = func_4664
mod = relay.transform.InferType()(mod)
mutated_mod['func_4664'] = func_4664
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4665 = relay.var("var_4665", dtype = "bool", shape = (1980,))#candidate|4665|(1980,)|var|bool
func_4664_call = mutated_mod.get_global_var('func_4664')
call_4666 = func_4664_call(var_4665)
output = call_4666
func_4667 = relay.Function([var_4665], output)
mutated_mod['func_4667'] = func_4667
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4283_call = mod.get_global_var('func_4283')
func_4284_call = mutated_mod.get_global_var('func_4284')
call_4699 = relay.TupleGetItem(func_4283_call(), 0)
call_4700 = relay.TupleGetItem(func_4284_call(), 0)
output = relay.Tuple([call_4699,])
output2 = relay.Tuple([call_4700,])
func_4701 = relay.Function([], output)
mod['func_4701'] = func_4701
mod = relay.transform.InferType()(mod)
mutated_mod['func_4701'] = func_4701
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4701_call = mutated_mod.get_global_var('func_4701')
call_4702 = func_4701_call()
output = call_4702
func_4703 = relay.Function([], output)
mutated_mod['func_4703'] = func_4703
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4542_call = mod.get_global_var('func_4542')
func_4543_call = mutated_mod.get_global_var('func_4543')
call_4754 = relay.TupleGetItem(func_4542_call(), 0)
call_4755 = relay.TupleGetItem(func_4543_call(), 0)
func_4177_call = mod.get_global_var('func_4177')
func_4179_call = mutated_mod.get_global_var('func_4179')
call_4766 = relay.TupleGetItem(func_4177_call(), 0)
call_4767 = relay.TupleGetItem(func_4179_call(), 0)
output = relay.Tuple([call_4754,call_4766,])
output2 = relay.Tuple([call_4755,call_4767,])
func_4770 = relay.Function([], output)
mod['func_4770'] = func_4770
mod = relay.transform.InferType()(mod)
output = func_4770()
func_4771 = relay.Function([], output)
mutated_mod['func_4771'] = func_4771
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4793 = relay.var("var_4793", dtype = "float32", shape = (4, 13, 9))#candidate|4793|(4, 13, 9)|var|float32
uop_4794 = relay.log(var_4793.astype('float32')) # shape=(4, 13, 9)
output = uop_4794
output2 = uop_4794
func_4797 = relay.Function([var_4793,], output)
mod['func_4797'] = func_4797
mod = relay.transform.InferType()(mod)
mutated_mod['func_4797'] = func_4797
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4798 = relay.var("var_4798", dtype = "float32", shape = (4, 13, 9))#candidate|4798|(4, 13, 9)|var|float32
func_4797_call = mutated_mod.get_global_var('func_4797')
call_4799 = func_4797_call(var_4798)
output = call_4799
func_4800 = relay.Function([var_4798], output)
mutated_mod['func_4800'] = func_4800
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4177_call = mod.get_global_var('func_4177')
func_4179_call = mutated_mod.get_global_var('func_4179')
call_4843 = relay.TupleGetItem(func_4177_call(), 0)
call_4844 = relay.TupleGetItem(func_4179_call(), 0)
output = call_4843
output2 = call_4844
func_4858 = relay.Function([], output)
mod['func_4858'] = func_4858
mod = relay.transform.InferType()(mod)
mutated_mod['func_4858'] = func_4858
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4858_call = mutated_mod.get_global_var('func_4858')
call_4859 = func_4858_call()
output = call_4859
func_4860 = relay.Function([], output)
mutated_mod['func_4860'] = func_4860
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4866 = relay.var("var_4866", dtype = "float64", shape = (8, 16, 8))#candidate|4866|(8, 16, 8)|var|float64
const_4867 = relay.const([[[0.786587,-1.247303,-9.069580,-4.010012,7.174481,-4.687477,-2.457021,-0.141753],[9.339681,-2.892064,-9.828113,3.996576,-8.472792,1.102869,-3.418677,-2.471576],[-0.743704,9.229011,2.303662,9.863136,-8.294387,4.202007,-5.641127,-1.061755],[6.187623,5.377066,9.620784,9.585639,-8.727822,5.604788,1.980193,-4.477412],[5.203113,-3.290378,2.976319,7.169409,2.077141,-8.500846,-3.441101,5.634195],[3.639432,9.568030,-3.375978,1.518774,5.018364,7.942615,-8.510498,9.461950],[-5.597870,-8.055557,3.951216,1.717160,-9.767332,-4.489163,-3.756064,8.147316],[-8.319563,-7.902325,0.800515,2.455597,-6.601206,8.949483,-5.679760,-5.477231],[-1.168540,-4.744864,9.122469,-2.238665,1.213988,-7.775926,-7.678975,-0.281738],[9.172487,7.693519,-6.261625,5.879638,-0.320200,9.524011,1.543201,7.458041],[-6.434662,-7.441948,1.476784,0.290123,4.160313,-9.322374,5.036946,4.450820],[0.983329,3.962407,2.966587,-4.887314,8.351120,7.287331,-3.154979,-3.671266],[-3.301298,-8.692028,3.309103,3.522396,4.837801,5.956381,-2.458979,6.415362],[5.500749,6.927747,-3.696414,-5.134006,5.378125,-9.749018,-0.040751,-4.288802],[5.757074,-1.788555,-5.984881,-5.375267,8.923877,1.576561,-4.273218,2.011173],[2.430046,-3.232602,9.968410,-7.275050,-8.742275,-5.935827,6.586114,-0.473414]],[[8.713872,-0.203394,-7.082229,0.039517,-5.778418,2.787936,-2.301819,-6.359740],[9.383634,2.314787,-4.920733,4.369389,-2.974850,0.516265,-1.294714,5.707518],[1.962211,3.217276,-3.341031,0.369280,0.775511,7.829319,-6.996636,-7.540829],[-3.468758,-9.143756,0.488720,-1.319900,5.376520,9.278986,2.538343,0.993969],[-6.210778,-6.425216,3.287394,8.371356,-3.477603,-4.882823,1.568162,-5.080612],[-8.629265,-5.866723,-0.951797,-7.260872,-5.478986,0.256899,-8.394150,-6.616496],[6.095666,7.600524,0.935340,-0.126582,7.118253,-2.488887,2.225829,-4.889892],[9.634214,9.513055,6.784214,8.949466,5.392597,7.071583,8.328213,5.903099],[-9.595695,8.736341,7.252962,0.878939,9.967623,6.906862,-8.606655,-8.367929],[-0.979108,6.845575,9.469949,-5.704573,8.623959,-5.946127,1.610659,-7.127136],[-2.137944,2.023232,0.902804,-7.169782,-6.676083,3.912432,-6.918689,-5.246912],[9.680108,-9.942833,-8.069590,9.907313,6.673378,-6.820509,1.242831,-2.430399],[7.842820,-0.870303,5.891769,9.133585,-0.295768,-1.037301,-4.538983,-2.912383],[2.394914,5.702275,5.496389,9.233602,-1.519338,4.287124,-8.614783,-2.954326],[-1.484834,-5.825278,6.027183,5.124080,-2.897796,-8.373497,2.745668,-4.081134],[-9.366643,-5.142153,9.990679,-8.925816,-2.882680,1.951845,3.594514,-9.923295]],[[-5.485456,2.351673,-8.812584,-8.576693,0.334958,8.410334,4.720385,5.778579],[4.559382,7.623823,2.015128,1.776200,9.651448,6.026171,-6.726351,-2.803840],[-6.726924,-3.187396,1.620455,-3.571201,-1.322924,7.238696,4.382203,6.784884],[-7.851835,8.165116,-0.453480,8.213212,-2.685850,-2.622018,-9.637076,4.940905],[2.945459,3.133070,-1.721781,4.367590,-7.716446,-0.993877,8.396795,-9.201072],[-2.367225,2.251504,-8.735036,7.448376,5.890023,7.291184,-1.510730,9.285988],[2.098971,-4.307675,-5.093903,-1.015235,-8.905883,-4.139470,-9.713053,-3.308796],[0.750206,1.946821,-8.813179,-8.727542,-4.951037,-4.891016,-9.572623,-8.288710],[-1.415788,-6.895371,-2.414695,3.634803,0.027245,-4.780621,4.370697,0.063136],[3.739140,-7.758012,9.603791,5.089166,1.330915,-5.616519,9.425691,1.795434],[-5.825460,-9.563964,-5.075739,0.395975,-1.584649,2.913787,-3.993181,-6.752824],[0.001464,-0.971285,3.303625,-2.985301,3.672349,-1.130979,-3.588699,-3.629647],[7.859489,5.030405,2.399288,-0.728178,4.606093,2.825604,-6.496981,4.724585],[-1.311668,-8.426256,9.843960,-7.327062,4.987097,-1.886408,-9.145426,-6.654962],[3.409366,7.800048,2.421011,-0.523431,0.257550,-2.278731,4.290478,3.290793],[5.892416,1.939992,5.216520,6.054329,4.601197,-9.524707,7.291630,6.354917]],[[-0.980448,7.250604,-6.229042,-5.434188,8.250977,2.055706,-8.966863,-6.366201],[-9.264979,8.568468,-2.829354,9.602986,-5.809244,8.263425,-6.638993,-0.552582],[-7.650274,-8.286223,-2.247654,-1.791668,-2.315806,-6.398889,3.293698,-7.257374],[5.975568,1.490807,9.295057,8.798266,-5.447392,8.905906,5.869973,2.217019],[7.421551,9.560817,7.630900,6.460480,9.010120,-4.213609,-7.983795,6.121446],[-3.412941,8.484254,0.032506,4.383807,-4.503061,-5.855478,1.705154,0.480522],[-1.474110,-3.414723,-7.806082,0.696247,3.861846,-2.353684,-6.074359,5.298195],[-0.201618,-7.114856,0.933328,9.503497,-0.879437,-8.176374,-6.677083,-7.543439],[-5.667675,-6.774175,-2.341978,-0.849178,4.264902,-7.134864,-6.820811,4.591958],[-3.442598,-9.245391,2.955483,6.578179,-9.499031,6.339841,4.249337,4.122600],[-5.704789,2.915458,3.558978,1.911944,-9.789295,-9.728641,1.733944,-3.836730],[-1.221082,-7.191686,-2.450305,4.297136,5.092331,0.308184,2.833334,-3.182888],[-1.351180,-7.800719,5.541479,3.557521,4.059058,8.186151,8.357838,2.939568],[-2.615152,2.005752,7.751700,5.637882,-8.045864,-3.794237,1.570677,3.963293],[-8.307986,8.241168,9.716727,9.018602,2.991342,-6.733642,-9.476409,-3.908240],[4.585429,-2.795353,-4.357883,8.279117,-8.896291,-1.641088,-9.105325,-1.611230]],[[-6.651412,-5.485590,-1.723778,-4.886206,-7.433509,-1.951864,-3.321133,-6.421075],[-3.803467,7.064856,-4.800860,8.754822,-6.003265,5.880618,-6.897025,2.274567],[1.210147,-8.496701,8.783228,6.209819,8.639895,0.121488,-2.925989,6.054715],[-8.276662,-0.353219,1.563397,8.098200,1.710989,-6.886273,-0.515610,-8.640836],[-7.566999,2.031248,-1.766327,0.310257,-5.992615,8.635016,-2.869328,-9.026071],[8.549399,-9.259143,-9.145638,-6.147897,-2.527526,3.612980,-5.070720,-8.781573],[9.791501,4.070034,9.678728,1.545469,5.733764,-2.350406,-8.811922,-0.523751],[9.094594,-3.534806,-2.142504,-0.315160,-5.258963,-7.003123,2.381464,8.417932],[-8.678111,-1.796068,5.405488,-1.736056,8.220857,8.264335,0.099027,7.081336],[-5.654946,-4.824254,1.764994,8.148951,9.552475,-9.057141,-4.729830,0.543771],[-4.708863,-2.092260,4.909124,-8.862963,-8.327412,-8.462124,4.294866,-5.109268],[-0.800644,9.568515,8.469335,5.193682,-0.047024,-0.101825,1.994855,4.676971],[8.848525,3.263641,-2.683886,8.895969,6.905165,-0.207924,-8.745907,-9.220365],[-1.400026,-6.201055,-2.862964,-2.553433,5.003337,-9.316406,-2.319504,4.449914],[1.241020,-2.890699,-2.250376,-3.086202,-6.954286,8.727354,-9.524827,8.508706],[0.338705,-9.288866,3.734222,-6.974326,4.962005,2.137079,-5.782648,-2.114659]],[[4.147625,-3.155118,-7.365649,-0.920591,6.609315,1.100910,8.816487,-6.400504],[-1.937667,5.271168,8.392248,1.404434,-1.161573,-9.207476,7.721423,-0.637930],[-7.596669,-7.068727,-2.629091,6.759642,-7.041278,7.698270,3.148939,-8.073227],[-4.083458,1.194736,7.591619,1.406547,9.139474,2.604863,-6.269344,9.270261],[-7.841743,0.075131,-0.925760,-9.006370,-1.134897,9.141122,-9.999808,7.182179],[6.225172,-8.267282,3.156618,-0.027963,-9.323154,3.653636,9.341799,2.973211],[2.357885,-6.494314,4.227980,-3.701797,-9.898392,6.824144,-8.184886,-3.838821],[3.550746,-7.362546,-1.880159,6.817594,-4.549278,8.612800,3.485656,9.744063],[3.285396,7.735536,0.019756,-3.125213,8.694535,-3.322553,1.002781,0.280179],[7.689447,1.586304,-9.446897,-0.657649,-2.474116,-5.493909,-6.727902,-5.997896],[-6.706514,-3.226954,8.289456,7.789956,-1.865039,-2.362420,-1.770843,-3.465379],[-0.800343,8.108483,-9.958216,9.916758,7.294519,0.143167,-0.847315,-1.031799],[1.534311,-0.851026,7.573292,3.175670,4.138237,6.255158,2.955431,6.389484],[-8.150177,-1.514071,5.863656,7.775369,9.598110,-1.853887,-0.529194,-3.172577],[-6.952065,-7.195041,5.771437,9.611324,-2.819947,-2.543560,2.426253,1.382280],[4.935097,-5.803231,6.971897,8.777461,-5.735252,-8.493004,-0.710843,-5.502403]],[[9.832342,0.960554,-2.858436,7.179939,0.139335,-3.323042,-5.363732,-5.167526],[1.199505,-2.372443,-9.289506,-3.843644,9.163586,6.014562,0.195209,-8.626225],[1.536493,9.466151,3.077096,-3.776123,6.448255,6.456969,-8.793158,9.079751],[-4.853506,-1.312992,6.191181,-7.859347,-9.564854,7.349084,0.680365,-2.052504],[4.977600,7.727133,6.413975,4.741082,-0.231052,-5.677245,3.801805,7.193724],[4.837764,-8.611676,-2.819103,4.298857,5.371544,-7.816877,7.859713,8.110690],[4.576157,6.574492,-9.751020,1.084043,9.973486,5.889044,9.516710,-2.167942],[-7.498854,1.491773,8.337170,0.187764,2.558972,-7.049979,8.009719,8.932600],[-1.059453,1.445066,-6.372568,8.908385,-3.975770,-5.180567,8.718108,-6.262726],[2.023498,-3.584868,-1.225028,6.602070,-1.629562,-1.634129,3.500776,-1.140811],[-0.634545,-0.504823,-6.987913,-9.239866,-8.699189,-4.750449,-2.204338,-2.956331],[-8.428651,-2.380363,-7.111909,2.242303,7.520683,-8.012656,9.175853,-1.751394],[-7.432050,-4.568282,7.883926,4.452828,7.513900,5.816587,-7.326811,-6.280047],[5.103639,-6.877184,-3.455758,-7.277779,3.949944,3.415637,1.897839,3.426423],[-5.709728,-3.636820,-0.260338,-4.404427,0.595808,5.066375,7.552497,-7.023590],[1.637753,-5.013712,-4.568414,4.192700,-6.714390,4.585936,0.629528,0.036388]],[[-8.157330,4.513011,-1.384540,0.022291,9.988374,6.803052,-6.538635,0.754667],[-5.236451,9.741633,-0.688231,8.627453,6.774975,-2.801602,6.341319,6.703387],[2.927252,-5.118486,-7.560265,2.104907,2.165882,-7.992818,2.043054,9.420147],[1.755020,-7.117908,8.407203,-8.393486,-4.292757,8.607159,8.979642,-6.794275],[5.510945,-0.069477,-7.823135,-8.035433,-3.382113,1.785519,-2.399864,-7.889288],[6.127140,-3.519266,-9.791064,-9.158441,1.827238,-5.842602,-2.160274,-8.929772],[6.415689,0.039784,-0.084945,4.901381,-3.808057,-5.120341,0.016647,-1.808095],[-3.826795,-3.490114,-7.926076,6.936315,-7.053015,-8.508235,-0.647540,9.765790],[8.132883,8.569902,-8.652170,-4.895804,3.234681,2.948972,1.651027,-4.973400],[-1.537152,-4.550390,5.147876,7.149883,2.383253,-2.248745,-5.685711,-6.619137],[-6.743567,3.987699,-0.278381,7.017950,4.293852,7.823523,-9.305405,-9.433674],[-0.654305,7.002160,-3.281474,7.740509,-7.151390,-0.372308,5.054744,-9.911829],[-6.137520,-7.243157,-2.418534,6.153790,2.220713,-1.875954,-3.392334,-1.621151],[-0.383099,-8.485211,-7.931193,-0.130563,2.844584,8.617863,3.961528,-2.163462],[-2.428116,3.120659,-4.896992,-5.306634,6.678300,2.264262,0.319904,-4.231376],[-3.176421,-6.476032,-3.711509,2.417293,1.163442,5.782118,8.830102,6.609578]]], dtype = "float64")#candidate|4867|(8, 16, 8)|const|float64
bop_4868 = relay.greater_equal(var_4866.astype('bool'), relay.reshape(const_4867.astype('bool'), relay.shape_of(var_4866))) # shape=(8, 16, 8)
func_4241_call = mod.get_global_var('func_4241')
func_4242_call = mutated_mod.get_global_var('func_4242')
call_4878 = relay.TupleGetItem(func_4241_call(), 1)
call_4879 = relay.TupleGetItem(func_4242_call(), 1)
func_3847_call = mod.get_global_var('func_3847')
func_3850_call = mutated_mod.get_global_var('func_3850')
var_4887 = relay.var("var_4887", dtype = "uint64", shape = ())#candidate|4887|()|var|uint64
call_4886 = relay.TupleGetItem(func_3847_call(relay.reshape(var_4887.astype('uint64'), [])), 3)
call_4888 = relay.TupleGetItem(func_3850_call(relay.reshape(var_4887.astype('uint64'), [])), 3)
func_3715_call = mod.get_global_var('func_3715')
func_3718_call = mutated_mod.get_global_var('func_3718')
call_4889 = relay.TupleGetItem(func_3715_call(relay.reshape(var_4887.astype('uint64'), [])), 1)
call_4890 = relay.TupleGetItem(func_3718_call(relay.reshape(var_4887.astype('uint64'), [])), 1)
var_4896 = relay.var("var_4896", dtype = "float64", shape = (12, 2, 5))#candidate|4896|(12, 2, 5)|var|float64
bop_4897 = relay.minimum(call_4878.astype('int32'), relay.reshape(var_4896.astype('int32'), relay.shape_of(call_4878))) # shape=(12, 2, 5)
bop_4900 = relay.minimum(call_4879.astype('int32'), relay.reshape(var_4896.astype('int32'), relay.shape_of(call_4879))) # shape=(12, 2, 5)
var_4903 = relay.var("var_4903", dtype = "float64", shape = (8, 16, 8))#candidate|4903|(8, 16, 8)|var|float64
bop_4904 = relay.less(const_4867.astype('bool'), relay.reshape(var_4903.astype('bool'), relay.shape_of(const_4867))) # shape=(8, 16, 8)
func_3658_call = mod.get_global_var('func_3658')
func_3660_call = mutated_mod.get_global_var('func_3660')
call_4909 = relay.TupleGetItem(func_3658_call(), 0)
call_4910 = relay.TupleGetItem(func_3660_call(), 0)
bop_4911 = relay.logical_and(call_4886.astype('bool'), relay.reshape(call_4889.astype('bool'), relay.shape_of(call_4886))) # shape=(12, 15, 13)
bop_4914 = relay.logical_and(call_4888.astype('bool'), relay.reshape(call_4890.astype('bool'), relay.shape_of(call_4888))) # shape=(12, 15, 13)
uop_4916 = relay.acos(call_4878.astype('float64')) # shape=(12, 2, 5)
uop_4918 = relay.acos(call_4879.astype('float64')) # shape=(12, 2, 5)
func_832_call = mod.get_global_var('func_832')
func_834_call = mutated_mod.get_global_var('func_834')
var_4923 = relay.var("var_4923", dtype = "int8", shape = (512,))#candidate|4923|(512,)|var|int8
call_4922 = relay.TupleGetItem(func_832_call(relay.reshape(var_4923.astype('int8'), [8, 16, 4])), 0)
call_4924 = relay.TupleGetItem(func_834_call(relay.reshape(var_4923.astype('int8'), [8, 16, 4])), 0)
output = relay.Tuple([bop_4868,var_4887,bop_4897,bop_4904,call_4909,bop_4911,uop_4916,call_4922,var_4923,])
output2 = relay.Tuple([bop_4868,var_4887,bop_4900,bop_4904,call_4910,bop_4914,uop_4918,call_4924,var_4923,])
func_4930 = relay.Function([var_4866,var_4887,var_4896,var_4903,var_4923,], output)
mod['func_4930'] = func_4930
mod = relay.transform.InferType()(mod)
var_4931 = relay.var("var_4931", dtype = "float64", shape = (8, 16, 8))#candidate|4931|(8, 16, 8)|var|float64
var_4932 = relay.var("var_4932", dtype = "uint64", shape = ())#candidate|4932|()|var|uint64
var_4933 = relay.var("var_4933", dtype = "float64", shape = (12, 2, 5))#candidate|4933|(12, 2, 5)|var|float64
var_4934 = relay.var("var_4934", dtype = "float64", shape = (8, 16, 8))#candidate|4934|(8, 16, 8)|var|float64
var_4935 = relay.var("var_4935", dtype = "int8", shape = (512,))#candidate|4935|(512,)|var|int8
output = func_4930(var_4931,var_4932,var_4933,var_4934,var_4935,)
func_4936 = relay.Function([var_4931,var_4932,var_4933,var_4934,var_4935,], output)
mutated_mod['func_4936'] = func_4936
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4188_call = mod.get_global_var('func_4188')
func_4189_call = mutated_mod.get_global_var('func_4189')
call_4964 = func_4188_call()
call_4965 = func_4188_call()
uop_4969 = relay.asinh(call_4964.astype('float64')) # shape=(14, 9, 6)
uop_4971 = relay.asinh(call_4965.astype('float64')) # shape=(14, 9, 6)
func_3220_call = mod.get_global_var('func_3220')
func_3223_call = mutated_mod.get_global_var('func_3223')
const_4986 = relay.const([2,1,3,5,6,4,4,-4,-6,-4,2,-6,10,-1,4,-10,-7,8,-7,-5,10,-3,-1,9,6,8,1,-10,-2,3,-1,4,-6,-2,-7,9,8,4,-9,-5,-8,-2,6,7,2,-6,7,-3,-6,7,3,1,-6,-9,9,3,-8,4,6,6,5,5,3,4,-4,-5,5,-6,-2,-9,10,8,-4,6,6,-1,3,3,-3,-7,6,-2,7,-3,3,-2,1,-5,-2,8,-10,-9,5,8,8,5,-9,-6,-4,-7,-10,-4,-9,-7,-7,-9,4,-9,-1,-4,-4,5,-5,10,-2,8,6,-3,8,-5,5,-1,3,5,-9,-1,8,-6,6,2,-7,-10], dtype = "int64")#candidate|4986|(132,)|const|int64
call_4985 = relay.TupleGetItem(func_3220_call(relay.reshape(const_4986.astype('int64'), [2, 11, 6])), 1)
call_4987 = relay.TupleGetItem(func_3223_call(relay.reshape(const_4986.astype('int64'), [2, 11, 6])), 1)
output = relay.Tuple([uop_4969,call_4985,const_4986,])
output2 = relay.Tuple([uop_4971,call_4987,const_4986,])
func_5003 = relay.Function([], output)
mod['func_5003'] = func_5003
mod = relay.transform.InferType()(mod)
mutated_mod['func_5003'] = func_5003
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5003_call = mutated_mod.get_global_var('func_5003')
call_5004 = func_5003_call()
output = call_5004
func_5005 = relay.Function([], output)
mutated_mod['func_5005'] = func_5005
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4770_call = mod.get_global_var('func_4770')
func_4771_call = mutated_mod.get_global_var('func_4771')
call_5039 = relay.TupleGetItem(func_4770_call(), 1)
call_5040 = relay.TupleGetItem(func_4771_call(), 1)
const_5042 = relay.const([[[7.723656,-2.777307,-7.874981,-9.015709,-9.127333,-8.634564],[6.798365,-6.131477,8.893926,9.163148,-1.011120,-5.999849],[-8.078206,7.170834,-2.704062,1.692056,-8.790464,3.861095],[-0.530605,6.993827,-0.166630,-5.564536,-9.292849,4.747813],[-9.084223,-2.156465,-0.548049,-6.511946,-8.280500,3.217590],[-3.173927,-4.348053,-0.815777,-7.789527,2.333005,4.078614],[7.807749,0.519634,5.114115,0.349731,3.228697,-5.850986],[-5.018622,-0.532897,-3.329311,-2.488098,-2.228782,5.089125],[-6.263410,-5.317581,2.580981,-0.645740,1.549845,9.184213]],[[-6.789762,-0.021128,-8.137900,-3.511192,-6.380909,6.025466],[-2.684759,4.612251,-7.846515,0.214600,-9.069559,-1.553988],[-2.466690,-8.582161,-7.437880,-4.838714,5.215433,-5.330537],[1.853592,-0.788053,-8.291256,-1.533044,9.802825,8.415875],[3.477186,6.237746,-9.229440,3.186466,-5.490464,7.728887],[7.985641,9.138758,-3.286672,-0.310562,-8.245207,7.631742],[-9.374560,9.583161,-8.884353,8.702140,-3.504929,2.519074],[-9.263737,7.946623,9.928196,3.367745,-8.271095,5.166481],[2.984908,-1.011748,-8.858963,-3.715287,1.122504,0.433691]],[[-5.473967,3.352217,7.129202,-1.378340,-2.214347,-8.779265],[-1.577514,-7.063717,-8.891466,3.244996,-7.456937,-0.928120],[-6.692981,9.046436,-5.003948,0.635799,-4.021536,2.795320],[6.782139,3.543079,5.240316,1.306535,-7.580116,-7.218889],[5.440246,-3.610131,7.193105,0.018712,0.256708,-8.165088],[6.461946,-4.631985,-7.959697,6.261772,0.650771,8.887900],[-8.884129,-3.496982,5.729216,8.793079,8.987880,-5.215605],[-5.236554,-4.993541,-6.119910,-7.877969,-8.505382,7.312659],[-6.301900,-5.279872,-2.016914,0.044044,0.870914,4.754680]],[[-2.044960,9.696928,-8.897927,5.248917,1.066388,-0.236411],[-4.976763,8.877613,0.398060,9.450939,1.925612,-2.258604],[-4.325738,-3.956600,8.945028,-3.196143,5.193831,5.618385],[4.507747,-0.621296,-3.856345,-2.920718,5.892477,4.550417],[0.438118,8.298158,5.755229,-9.717113,9.104114,7.663201],[-5.285139,-6.763873,6.712818,4.008953,-0.151544,-2.485214],[-8.350273,3.904642,-1.865660,-0.352709,-2.134761,9.358229],[7.839519,0.839415,-1.535185,-0.905919,-9.238207,-8.835974],[-7.522665,-4.852777,-7.121977,-3.364929,6.294594,-2.818660]],[[-8.621762,0.320171,-2.689032,-0.078746,-8.346889,-5.513029],[-3.258813,4.469817,-4.524392,5.995085,0.250852,1.801939],[-3.110879,-7.899997,-1.612367,7.450625,-8.713365,3.363908],[9.921513,-0.474110,2.897030,7.186712,4.507555,-9.165881],[-7.286481,4.637914,8.791579,2.907664,-4.238247,7.546254],[0.791449,8.380509,-3.253745,-7.336268,3.393815,2.747751],[-0.704833,-2.128610,-9.503151,4.132670,-0.051180,-2.253119],[4.847326,4.844796,-1.226141,-6.716669,-8.913815,6.380855],[-8.142531,-6.713080,-8.823836,-7.617590,-9.673286,3.077223]],[[0.037238,-1.867172,5.491597,5.557318,-4.293520,-9.199895],[-2.942242,-6.557814,-5.235651,4.926136,-3.904744,-8.185051],[7.344346,2.895573,-8.912731,-2.428914,6.876742,3.422422],[-2.797115,8.945017,-4.180101,6.868947,7.402398,0.936356],[9.809681,-9.262828,-7.885759,-6.298799,-4.209450,-1.163467],[-4.127872,-1.454869,0.007017,-1.350966,6.325809,-6.213546],[3.547457,-2.355816,-1.605782,5.915489,-9.566139,4.258970],[-3.730182,-3.019361,5.380221,1.468271,-9.284949,0.487748],[-7.864488,0.710171,3.680201,7.117434,2.298759,5.066663]],[[9.830300,7.883146,5.448791,-5.151983,-4.924442,-4.072644],[0.950119,-9.408298,9.558119,2.450066,9.570029,2.925434],[3.418664,-6.382053,-7.657922,-5.063422,-7.513392,5.356243],[-0.295843,0.862914,2.951896,-0.810802,-0.104295,-4.954105],[-2.783678,3.951079,-4.126047,-7.859106,9.310285,-9.914467],[5.399166,7.038965,-5.102380,2.403426,-8.814253,9.388195],[-5.251819,9.710824,-1.660236,-9.392528,7.683794,9.417567],[2.287748,9.135470,-2.089836,-2.132968,-2.047258,5.317136],[3.028191,4.007822,3.981009,7.341984,-9.869941,-8.329477]],[[-0.628749,0.234771,-0.437830,2.986751,3.302682,-9.065152],[-6.587101,6.590769,-1.126594,5.695460,3.526129,-6.826823],[4.226094,-6.049241,-6.232571,2.635306,8.080675,-4.483039],[1.730764,6.977829,1.848237,-9.782399,5.371069,-4.234050],[-7.447399,3.900112,2.486808,-4.669507,5.063161,-9.194623],[-4.421118,-6.589878,3.218349,6.554678,-7.253267,1.953524],[4.316554,7.316722,4.816857,-7.342879,6.131512,9.321088],[8.084497,2.404169,-3.108784,-7.731363,5.478885,-7.852676],[-1.994122,9.097689,3.309463,-4.445288,-3.353105,2.702187]],[[9.034827,8.042845,4.859029,9.571707,3.893906,0.407302],[4.561523,-8.659326,-0.547197,1.203466,-5.051316,7.984562],[6.586946,-0.187516,7.721591,9.127974,-0.854568,4.188480],[2.381463,-7.453657,2.177215,-4.261591,-4.559266,-1.555357],[8.788266,0.815443,-5.285331,8.996781,-2.306087,-8.142039],[7.822561,-3.129294,-9.435390,6.725622,6.151489,-0.311289],[3.007730,7.157967,2.688702,-6.699446,4.198175,6.725959],[-0.058604,5.910145,-0.499143,-8.794800,6.706897,6.814806],[-8.919140,2.340452,8.697583,4.977741,-5.884853,-5.776789]],[[-7.814078,-5.611489,-7.732168,4.528244,0.912732,4.266955],[-7.247533,8.512600,-6.652840,-9.626172,-7.955342,-0.906624],[2.861704,-2.537761,-1.944623,-1.665909,-6.475875,-3.801164],[-3.418882,6.884777,-9.878723,2.003531,1.544557,-9.010019],[-1.751666,-0.426007,-6.144972,-0.642722,-3.776667,7.472298],[6.832445,4.179823,3.181484,-2.263922,-8.027599,3.975387],[-2.228686,2.567485,3.846689,3.838519,-2.274384,-5.580731],[0.554722,4.719031,-1.195599,-3.875502,-5.114246,6.453425],[-3.202273,1.695516,9.404945,0.818084,9.175531,7.375660]],[[5.035443,-9.139802,6.524098,-5.513131,3.417327,-3.777443],[7.090337,0.354075,5.728201,6.176611,-4.719430,-7.915627],[7.289765,0.937489,-8.699203,2.398398,-9.450787,-1.301651],[1.410553,-6.832196,-2.432667,-0.192163,7.689854,0.383603],[-6.139263,-0.880763,9.787481,-9.027335,3.889972,1.952667],[8.647573,0.817036,8.445442,8.637969,-3.907260,6.438523],[-8.063372,-2.623688,-3.187854,-9.459791,-6.721466,3.064603],[9.919736,-1.085620,-2.368058,2.100671,2.297627,5.513451],[-5.525019,2.447453,-6.472201,3.460780,-6.408455,-3.317006]],[[5.271300,8.666260,-4.053696,0.886818,-5.217135,-4.493152],[1.850025,-6.515899,-2.723544,6.366730,-4.206391,4.746113],[-4.449187,-1.608973,9.383240,8.215481,9.358845,-1.609625],[7.567598,-4.802678,-8.344007,-2.126518,-2.346914,-5.670515],[-5.385100,3.173637,-1.122093,6.315731,5.302598,2.104539],[9.800708,4.595003,6.933297,-1.894489,1.663996,-0.485290],[2.319800,2.233121,-7.719856,-3.326666,-0.155883,3.479325],[-6.952529,5.852454,-4.873054,-5.251014,1.953684,7.162156],[-7.496716,5.469458,-5.335211,4.022213,8.649613,2.597922]],[[-8.390364,-2.927379,8.479883,6.839312,6.870663,9.134700],[4.433540,5.262971,7.440652,3.381224,-7.480793,0.171134],[-4.582191,-4.778530,9.296897,4.098597,8.436415,-1.165916],[-0.135545,-2.315982,-0.559275,2.463530,-4.547607,-8.530863],[6.739786,4.739057,4.003016,-0.872737,4.357818,1.732858],[-0.710566,-7.026723,-7.402752,-7.191989,-5.549461,-2.576720],[-1.960156,-1.285732,-9.738929,-6.058977,-8.170782,1.156278],[-3.432592,5.046444,-6.630687,6.995373,-8.410788,-5.263073],[-6.331049,3.911496,-1.426585,-7.293895,4.252752,1.894350]],[[4.045711,-7.239153,8.336426,9.116413,7.152360,8.584257],[9.458120,3.882094,-1.449528,5.673650,-7.977894,2.033394],[-4.603834,-6.157831,-0.798694,-1.811429,6.304131,8.762363],[-6.459670,7.401038,1.451042,-9.486941,6.392038,-9.645111],[4.000752,-9.230657,-7.633903,-2.757360,0.874569,3.690782],[-0.043542,-8.184619,-1.472741,-9.216339,-9.880574,-5.420111],[-7.122380,9.066352,-9.978777,1.647078,5.809040,-9.533990],[0.101321,-1.243966,1.584215,-8.818276,0.538764,3.202326],[-1.127351,6.897296,8.472053,2.207092,-9.248807,0.402637]]], dtype = "float32")#candidate|5042|(14, 9, 6)|const|float32
bop_5043 = relay.bitwise_or(call_5039.astype('uint8'), relay.reshape(const_5042.astype('uint8'), relay.shape_of(call_5039))) # shape=(14, 9, 6)
bop_5046 = relay.bitwise_or(call_5040.astype('uint8'), relay.reshape(const_5042.astype('uint8'), relay.shape_of(call_5040))) # shape=(14, 9, 6)
output = relay.Tuple([bop_5043,])
output2 = relay.Tuple([bop_5046,])
func_5049 = relay.Function([], output)
mod['func_5049'] = func_5049
mod = relay.transform.InferType()(mod)
output = func_5049()
func_5050 = relay.Function([], output)
mutated_mod['func_5050'] = func_5050
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3761_call = mod.get_global_var('func_3761')
func_3762_call = mutated_mod.get_global_var('func_3762')
call_5070 = relay.TupleGetItem(func_3761_call(), 0)
call_5071 = relay.TupleGetItem(func_3762_call(), 0)
func_4797_call = mod.get_global_var('func_4797')
func_4800_call = mutated_mod.get_global_var('func_4800')
var_5078 = relay.var("var_5078", dtype = "float32", shape = (468,))#candidate|5078|(468,)|var|float32
call_5077 = func_4797_call(relay.reshape(var_5078.astype('float32'), [4, 13, 9]))
call_5079 = func_4797_call(relay.reshape(var_5078.astype('float32'), [4, 13, 9]))
output = relay.Tuple([call_5070,call_5077,var_5078,])
output2 = relay.Tuple([call_5071,call_5079,var_5078,])
func_5093 = relay.Function([var_5078,], output)
mod['func_5093'] = func_5093
mod = relay.transform.InferType()(mod)
mutated_mod['func_5093'] = func_5093
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5094 = relay.var("var_5094", dtype = "float32", shape = (468,))#candidate|5094|(468,)|var|float32
func_5093_call = mutated_mod.get_global_var('func_5093')
call_5095 = func_5093_call(var_5094)
output = call_5095
func_5096 = relay.Function([var_5094], output)
mutated_mod['func_5096'] = func_5096
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5135 = relay.var("var_5135", dtype = "float32", shape = (5, 11, 4))#candidate|5135|(5, 11, 4)|var|float32
uop_5136 = relay.acosh(var_5135.astype('float32')) # shape=(5, 11, 4)
func_4061_call = mod.get_global_var('func_4061')
func_4064_call = mutated_mod.get_global_var('func_4064')
var_5145 = relay.var("var_5145", dtype = "float32", shape = (756,))#candidate|5145|(756,)|var|float32
var_5146 = relay.var("var_5146", dtype = "bool", shape = (1980,))#candidate|5146|(1980,)|var|bool
call_5144 = relay.TupleGetItem(func_4061_call(relay.reshape(var_5145.astype('float32'), [14, 9, 6]), relay.reshape(var_5146.astype('bool'), [1980,]), ), 1)
call_5147 = relay.TupleGetItem(func_4064_call(relay.reshape(var_5145.astype('float32'), [14, 9, 6]), relay.reshape(var_5146.astype('bool'), [1980,]), ), 1)
const_5153 = relay.const([False,True,True,False,True,False,False,False,False,True,False,False,False,False,False,False,True,True,True,False,True,False,True,False,False,False,True,False,False,True,False,False,False,True,False,False,True,True,False,False,False,False,False,False,False,False,False,True,True,False,True,False,False,True,False,False,True,True,False,True,False,False,True,True,False,True,True,True,False,True,True,True,False,True,True,False,True,False,False,True,False,True,True,False,False,False,False,True,True,True,False,False,True,True,True,True,True,False,True,True,True,False,False,True,False,False,False,True,False,False,False,False,True,False,False,False,False,False,True,True,True,False,True,True,True,False,False,False,False,True,False,False,False,False,True,False,False,True,True,False,True,False,False,True,False,False,True,False,True,False,True,False,False,True,True,False,True,False,False,False,True,False,False,True,True,True,True,True,True,True,False,False,True,False,True,True,True,False,True,False,True,False,False,True,True,False,True,True,False,False,True,True,False,True,True,True,False,False,True,True,True,True,False,False,True,True,True,False,False,False,False,True,True,True,False,False,True,False,True,True,False,False,False,False,True,True,False,False,False,True,True,True,False,True,False,True,True,True,False,True,False,False,False,True,True,False,True,False,False,True,True,False,True,False,True,True,True,True,True,True,False,False,True,False,False,True,True,True,False,True,False,False,False,False,True,True,False,True,False,True,False,True,True,True,True,False,False,True,True,True,False,True,False,True,True,False,False,True,True,True,False,True,True,False,True,True,False,True,False,False,False,False,True,False,True,True,False,False,False,False,True,False,True,True,False,True,True,False,False,False,True,False,True,True,True,False,False,True,False,False,True,False,False,False,False,True,True,True,True,True,True,True,False,False,False,False,True,False,False,True,False,False,False,False,True,True,False,True,False,False,True,True,True,True,True,True,False,True,False,False,False,True,True,False,False,True,False,True,True,True,True,False,True,True,False,False,False,False,True,False,True,False,True,False,True,False,True,True,True,False,True,False,True,False,False,True,False,True,True,True,False,False,True,True,True,True,True,True,False,False,True,True,False,False,True,True,False,False,False,False,False,False,False,False,False,False,True,False,True,False,False,True,False,True,False,True,True,True,False,True,True,True,False,True,True,True,False,False,True,True,False,False,True,False,False,True,False,True,False,False,False,False,True,False,True,False,False,False,True,False,True,True,False,True,False,True,False,True,True,False,False,True,False,True,True,False,False,False,True,False,False,True,False,True,False,False,True,False,False,True,False,False,False,False,True,False,False,False,True,True,False,True,True,False,False,False,False,True,False,True,True,False,True,False,False,True,False,True,True,False,False,True,False,False,False,False,True,False,False,False,True,False,False,False,False,False,True,False,True,True,True,True,False,False,True,False,True,True,True,False,True,False,False,False,False,False,False,True,False,False,False,True,False,False,False,False,False,True,False,False,False,True,True,False,False,False,False,True,True,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,True,False,False,False,False,False,True,False,True,True,False,True,False,True,False,False,True,True,False,True,True,False,True,False,False,True,False,False,True,True,False,False,True,True,True,False,True,False,False,True,True,False,False,True,True,True,True,True,False,True,False,True,False,False,True,False,True,False,True,False,True,True,True,False,False,False,False,False,False,False,True,True,False,True,True,False,False,False,True,False,False,True,False,False,True,True,False,True,True,True,True,False,True,False,True,True,False,True,True,False,False,False,False,False,False,True,False,False,True,True,True,True,True,True,True,False,False,False,True,False,True,True,False,False,True,True,False,False,True,True,False,True,False,False,True,False,True,False,False,True,True,True,False,False,False,False,True,True,False,False,True,True,True,True,False,True,True,False,True,False,True,True,True,True,False,False,True,True,False,False,False,False,True,True,False,False,True,True,True,True,False,False,False,True,True,False,False,False,False,True,False,False,True,True,True,True,False,True,False,False,True,True,False,False,False,True,False,True,False,True,False,False,True,False,False,True,True,False,True,True,False,False,True,True,True,True,False,True,False,False,False,True,True,False,True,True,True,False,False,False,True,False,False,True,True,False,False,False,True,True,True,True,True,True,False,True,False,False,False,False,False,False,True,False,True,False,True,False,False,False,False,False,False,True,True,True,True,True,True,False,False,True,True,False,False,True,True,False,True,True,False,False,False,True,False,True,True,True,True,False,True,False,False,False,True,True,True,False,False,True,True,False,False,False,False,False,False,True,False,True,True,False,True,True,True,True,False,False,True,True,False,False,True,False,False,False,True,False,True,True,True,False,False,True,False,False,True,False,False,True,False,True,True,True,False,False,True,False,False,False,True,True,False,True,True,True,True,True,True,False,False,False,False,False,True,True,True,False,True,True,True,True,False,False,True,False,False,False,False,False,False,True,True,False,False,True,True,False,False,False,False,False,False,True,True,True,False,False,True,True,True,False,True,True,False,False,True,False,False,True,True,False,False,False,False,True,True,False,True,True,False,True,False,True,False,True,False,False,True,False,False,False,False,True,True,True,True,False,True,True,True,False,True,True,True,True,False,False,True,True,False,False,True,False,True,True,True,True,False,False,True,False,False,False,True,True,True,False,True,False,True,False,True,False,True,False,True,False,False,True,True,False,True,False,False,False,False,True,True,False,True,True,False,True,True,True,False,False,True,True,False,False,True,True,False,True,True,True,True,False,False,False,False,True,True,True,True,True,False,True,True,False,False,True,True,True,False,False,True,True,True,True,True,True,True,True,False,False,False,True,False,True,True,True,False,False,False,False,True,False,True,False,False,True,True,False,False,True,False,True,False,True,False,True,False,True,False,False,False,True,True,False,False,True,True,False,True,True,False,True,False,True,True,False,False,True,False,False,False,False,True,True,False,False,False,False,True,True,True,True,False,False,False,False,True,True,False,True,True,True,False,True,False,True,True,True,False,False,True,True,False,True,False,False,True,False,True,False,True,False,False,True,False,False,True,False,True,False,True,False,True,True,True,True,False,True,False,True,True,False,False,True,True,False,False,False,False,True,False,False,True,False,True,True,False,True,True,False,True,False,False,False,True,False,True,False,True,False,True,False,False,True,True,True,True,True,True,True,False,True,True,True,False,True,True,False,False,False,False,True,True,True,True,False,True,False,False,False,False,True,False,False,False,True,True,True,True,False,True,True,False,False,True,False,True,False,False,True,False,True,False,True,False,True,False,True,False,False,True,False,False,True,True,False,False,False,False,True,True,True,True,True,True,False,True,True,False,True,False,False,False,True,False,False,False,False,True,False,False,False,True,False,True,False,True,False,False,True,True,True,False,False,False,True,False,True,False,False,True,True,True,True,False,True,False,False,True,True,True,True,False,False,False,True,False,True,True,False,False,True,False,False,True,False,True,False,False,False,False,True,True,True,False,True,False,False,True,True,False,False,True,False,False,True,True,False,False,True,True,False,False,True,False,True,True,True,True,True,True,False,False,False,True,True,True,False,True,True,True,True,True,False,True,False,True,True,False,True,False,True,True,False,False,True,True,False,True,True,True,False,True,False,True,False,True,False,False,False,True,False,False,True,False,True,True,False,False,True,True,False,True,True,False,True,False,False,True,True,True,True,False,False,True,True,False,False,True,True,False,True,True,False,False,True,False,True,True,False,False,True,True,True,False,True,True,False,True,False,False,False,True,False,False,False,True,True,False,False,False,True,True,True,True,True,False,True,False,False,False,True,True,True,False,True,False,True,True,False,False,True,False,True,True,True,False,False,False,False,True,False,True,False,True,True,False,True,False,False,True,False,True,False,True,False,True,False,True,True,False,True,False,False,True,False,True,True,False,True,True,True,True,True,False,False,False,False,False,False,False,True,True,False,False,False,False,True,False,True,False,False,True,True,True,False,True,False,True,True,False,False,True,True,True,True,False,True,True,False,False,True,True,True,True,True,True,True,True,False,True,True,False,False,False,True,False,True,False,True,True,False,True,False,True,True,True,True,False,False,True,False,True,True,True,True,False,True,False,True,True,True,True,True,True,True,True,True,True,True,False,False,True,False,False,False,True,True,False,True,True,True,False,False,False,True,True,True,False,False,False,True,True,True,True,True,True,False,False,False,True,True,False,False,True,False,False,False,True,False,True,False,False,True,False,False,True,False,True,True,False,False,True,True,True,False,False,False,False,True,False,True,False,False,True,True,False,True,True,True,False,False,True,False,False,False,False,True,False,False,False,False,False,True,True,True,True,False,False,True,True,False,False,True,True,True,False,True,True,True,True,True,True,False,True,True,False,True,False,False,True,True,False,True,False,False,True,False,False,True,True,True,True,False,False,False,True,False,False,False,True,True,True,False,True,False,False,False,False,False,False,True,True,True,True,False,True,False,False,True,True,True,False,False,True,False,True,True,False,True,True,True,False,True,True,True,True,True,True,True,False,False,True,True,True,False,True,False,False,True,True,True,True,True,True,False,True,False,True,True,True,True,False,True,False,True,True,True,True,False,True,True,False,False,False,True,False,False,True,False,True,False,True,False,True,False,True,False,True,False,True,False,True,True,False,True,True,True,True,False,True,False,True,False,False,True,True,False,True,True,False,True,True,True,True,True,True], dtype = "bool")#candidate|5153|(1980,)|const|bool
bop_5154 = relay.floor_mod(var_5146.astype('float32'), relay.reshape(const_5153.astype('float32'), relay.shape_of(var_5146))) # shape=(1980,)
uop_5157 = relay.rsqrt(uop_5136.astype('float64')) # shape=(5, 11, 4)
func_4158_call = mod.get_global_var('func_4158')
func_4159_call = mutated_mod.get_global_var('func_4159')
call_5160 = relay.TupleGetItem(func_4158_call(), 0)
call_5161 = relay.TupleGetItem(func_4159_call(), 0)
output = relay.Tuple([call_5144,var_5145,bop_5154,uop_5157,call_5160,])
output2 = relay.Tuple([call_5147,var_5145,bop_5154,uop_5157,call_5161,])
func_5162 = relay.Function([var_5135,var_5145,var_5146,], output)
mod['func_5162'] = func_5162
mod = relay.transform.InferType()(mod)
mutated_mod['func_5162'] = func_5162
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5162_call = mutated_mod.get_global_var('func_5162')
var_5164 = relay.var("var_5164", dtype = "float32", shape = (5, 11, 4))#candidate|5164|(5, 11, 4)|var|float32
var_5165 = relay.var("var_5165", dtype = "float32", shape = (756,))#candidate|5165|(756,)|var|float32
var_5166 = relay.var("var_5166", dtype = "bool", shape = (1980,))#candidate|5166|(1980,)|var|bool
call_5163 = func_5162_call(var_5164,var_5165,var_5166,)
output = call_5163
func_5167 = relay.Function([var_5164,var_5165,var_5166,], output)
mutated_mod['func_5167'] = func_5167
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5181 = relay.var("var_5181", dtype = "uint32", shape = (6, 6, 12))#candidate|5181|(6, 6, 12)|var|uint32
var_5182 = relay.var("var_5182", dtype = "uint32", shape = (6, 6, 12))#candidate|5182|(6, 6, 12)|var|uint32
bop_5183 = relay.add(var_5181.astype('uint32'), relay.reshape(var_5182.astype('uint32'), relay.shape_of(var_5181))) # shape=(6, 6, 12)
bop_5205 = relay.power(var_5182.astype('float32'), relay.reshape(bop_5183.astype('float32'), relay.shape_of(var_5182))) # shape=(6, 6, 12)
func_3847_call = mod.get_global_var('func_3847')
func_3850_call = mutated_mod.get_global_var('func_3850')
const_5209 = relay.const(-7, dtype = "uint64")#candidate|5209|()|const|uint64
call_5208 = relay.TupleGetItem(func_3847_call(relay.reshape(const_5209.astype('uint64'), [])), 0)
call_5210 = relay.TupleGetItem(func_3850_call(relay.reshape(const_5209.astype('uint64'), [])), 0)
output = relay.Tuple([bop_5205,call_5208,const_5209,])
output2 = relay.Tuple([bop_5205,call_5210,const_5209,])
func_5224 = relay.Function([var_5181,var_5182,], output)
mod['func_5224'] = func_5224
mod = relay.transform.InferType()(mod)
var_5225 = relay.var("var_5225", dtype = "uint32", shape = (6, 6, 12))#candidate|5225|(6, 6, 12)|var|uint32
var_5226 = relay.var("var_5226", dtype = "uint32", shape = (6, 6, 12))#candidate|5226|(6, 6, 12)|var|uint32
output = func_5224(var_5225,var_5226,)
func_5227 = relay.Function([var_5225,var_5226,], output)
mutated_mod['func_5227'] = func_5227
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4188_call = mod.get_global_var('func_4188')
func_4189_call = mutated_mod.get_global_var('func_4189')
call_5237 = func_4188_call()
call_5238 = func_4188_call()
output = call_5237
output2 = call_5238
func_5241 = relay.Function([], output)
mod['func_5241'] = func_5241
mod = relay.transform.InferType()(mod)
output = func_5241()
func_5242 = relay.Function([], output)
mutated_mod['func_5242'] = func_5242
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5241_call = mod.get_global_var('func_5241')
func_5242_call = mutated_mod.get_global_var('func_5242')
call_5257 = func_5241_call()
call_5258 = func_5241_call()
output = call_5257
output2 = call_5258
func_5275 = relay.Function([], output)
mod['func_5275'] = func_5275
mod = relay.transform.InferType()(mod)
mutated_mod['func_5275'] = func_5275
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5275_call = mutated_mod.get_global_var('func_5275')
call_5276 = func_5275_call()
output = call_5276
func_5277 = relay.Function([], output)
mutated_mod['func_5277'] = func_5277
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4241_call = mod.get_global_var('func_4241')
func_4242_call = mutated_mod.get_global_var('func_4242')
call_5298 = relay.TupleGetItem(func_4241_call(), 2)
call_5299 = relay.TupleGetItem(func_4242_call(), 2)
output = relay.Tuple([call_5298,])
output2 = relay.Tuple([call_5299,])
func_5301 = relay.Function([], output)
mod['func_5301'] = func_5301
mod = relay.transform.InferType()(mod)
mutated_mod['func_5301'] = func_5301
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5301_call = mutated_mod.get_global_var('func_5301')
call_5302 = func_5301_call()
output = call_5302
func_5303 = relay.Function([], output)
mutated_mod['func_5303'] = func_5303
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5306 = relay.var("var_5306", dtype = "float64", shape = (12, 2, 10))#candidate|5306|(12, 2, 10)|var|float64
const_5307 = relay.const([[[0.159052,0.150577,5.767143,3.113262,9.372927,1.986299,-9.951324,-0.530831,-4.865779,1.333648],[8.638108,5.908265,-1.379062,-0.348008,-9.088111,8.554228,-9.837012,6.686815,-3.677119,6.112470]],[[-0.696507,-2.718874,-2.918312,-7.608202,-6.149145,9.797202,9.961309,-2.948770,1.587578,-3.589440],[-3.440065,4.449154,8.517572,-8.873228,-7.086302,9.069691,-0.728701,5.069931,-0.670525,1.661849]],[[5.309160,2.928447,-9.468126,7.409491,-0.268914,6.017273,8.741451,0.870835,6.897552,-2.093964],[5.812523,-5.835763,6.371933,8.350490,9.040573,9.316108,4.483467,-6.115998,-7.228440,1.138353]],[[3.812335,4.504223,-9.727766,1.341570,5.256369,4.646417,2.568403,-3.833295,1.353244,8.662915],[4.757668,-7.917580,8.095234,-1.794087,-8.960387,-4.187326,-7.947378,-9.917082,9.027903,-7.293660]],[[-3.821533,4.313123,8.069105,-4.485925,3.394675,-5.561620,-4.309690,-9.625897,8.323608,1.675809],[-0.864468,0.128333,-2.375734,5.430621,-0.993395,-4.767689,7.337118,-4.698140,0.529100,-5.832073]],[[-2.216557,6.339403,0.603743,-9.053920,-9.505920,-9.200727,-8.224279,7.171466,3.030754,-7.844165],[-3.861852,-1.594218,-2.669867,3.321493,-0.328150,1.127821,-5.628423,2.063858,-5.617506,-8.212920]],[[-0.411600,9.540974,-3.158155,8.909194,-9.521990,7.621623,-1.336774,-4.575641,2.493921,-5.605667],[3.506261,-5.387195,2.072328,6.764772,-8.994082,-8.398787,-7.974362,3.984442,7.428597,9.951015]],[[-7.964542,-8.138916,-0.733042,3.212135,-0.854266,4.554067,7.565627,7.332323,-1.640477,-9.040549],[-6.435902,1.881718,8.939743,-6.266517,5.985043,-3.431282,-0.231226,-8.068007,9.795616,-7.911865]],[[2.187128,-8.714366,-7.679881,8.786594,-9.120940,6.092691,6.727282,-0.816273,5.632068,9.272961],[-7.153768,-1.319120,-4.805942,7.178766,-9.134790,-8.720514,-4.378095,1.151293,-6.859300,8.505608]],[[-2.713513,-2.395959,8.602479,-4.402281,5.157969,1.624127,5.382726,-0.297923,-5.471906,-7.952154],[-9.433479,-5.220967,6.395273,8.148931,6.903585,-7.694945,9.187975,0.284169,9.713271,9.159665]],[[4.997850,-4.018716,-9.344230,-5.627115,1.540112,8.354237,6.315541,-8.248055,9.064749,6.036939],[-0.227416,4.591447,-7.288824,-2.915359,-6.973098,-7.541436,-2.206558,9.257633,7.245724,5.034361]],[[-1.058878,-9.877686,-1.865325,-3.192489,-6.516994,-7.897750,6.389265,-0.662534,-0.478985,-4.234522],[-8.734643,-1.147368,2.839354,0.053516,-6.569322,8.751766,-9.661037,-4.381797,-3.279260,-8.059938]]], dtype = "float64")#candidate|5307|(12, 2, 10)|const|float64
bop_5308 = relay.power(var_5306.astype('float64'), relay.reshape(const_5307.astype('float64'), relay.shape_of(var_5306))) # shape=(12, 2, 10)
output = relay.Tuple([bop_5308,])
output2 = relay.Tuple([bop_5308,])
func_5311 = relay.Function([var_5306,], output)
mod['func_5311'] = func_5311
mod = relay.transform.InferType()(mod)
mutated_mod['func_5311'] = func_5311
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5312 = relay.var("var_5312", dtype = "float64", shape = (12, 2, 10))#candidate|5312|(12, 2, 10)|var|float64
func_5311_call = mutated_mod.get_global_var('func_5311')
call_5313 = func_5311_call(var_5312)
output = call_5313
func_5314 = relay.Function([var_5312], output)
mutated_mod['func_5314'] = func_5314
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5332 = relay.var("var_5332", dtype = "float32", shape = (14, 8, 13))#candidate|5332|(14, 8, 13)|var|float32
uop_5333 = relay.acos(var_5332.astype('float32')) # shape=(14, 8, 13)
func_4241_call = mod.get_global_var('func_4241')
func_4242_call = mutated_mod.get_global_var('func_4242')
call_5340 = relay.TupleGetItem(func_4241_call(), 0)
call_5341 = relay.TupleGetItem(func_4242_call(), 0)
output = relay.Tuple([uop_5333,call_5340,])
output2 = relay.Tuple([uop_5333,call_5341,])
func_5343 = relay.Function([var_5332,], output)
mod['func_5343'] = func_5343
mod = relay.transform.InferType()(mod)
mutated_mod['func_5343'] = func_5343
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5344 = relay.var("var_5344", dtype = "float32", shape = (14, 8, 13))#candidate|5344|(14, 8, 13)|var|float32
func_5343_call = mutated_mod.get_global_var('func_5343')
call_5345 = func_5343_call(var_5344)
output = call_5345
func_5346 = relay.Function([var_5344], output)
mutated_mod['func_5346'] = func_5346
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5049_call = mod.get_global_var('func_5049')
func_5050_call = mutated_mod.get_global_var('func_5050')
call_5390 = relay.TupleGetItem(func_5049_call(), 0)
call_5391 = relay.TupleGetItem(func_5050_call(), 0)
func_5241_call = mod.get_global_var('func_5241')
func_5242_call = mutated_mod.get_global_var('func_5242')
call_5400 = func_5241_call()
call_5401 = func_5241_call()
output = relay.Tuple([call_5390,call_5400,])
output2 = relay.Tuple([call_5391,call_5401,])
func_5412 = relay.Function([], output)
mod['func_5412'] = func_5412
mod = relay.transform.InferType()(mod)
mutated_mod['func_5412'] = func_5412
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5412_call = mutated_mod.get_global_var('func_5412')
call_5413 = func_5412_call()
output = call_5413
func_5414 = relay.Function([], output)
mutated_mod['func_5414'] = func_5414
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5455 = relay.var("var_5455", dtype = "float32", shape = (5, 3, 16))#candidate|5455|(5, 3, 16)|var|float32
uop_5456 = relay.acosh(var_5455.astype('float32')) # shape=(5, 3, 16)
output = uop_5456
output2 = uop_5456
func_5463 = relay.Function([var_5455,], output)
mod['func_5463'] = func_5463
mod = relay.transform.InferType()(mod)
var_5464 = relay.var("var_5464", dtype = "float32", shape = (5, 3, 16))#candidate|5464|(5, 3, 16)|var|float32
output = func_5463(var_5464)
func_5465 = relay.Function([var_5464], output)
mutated_mod['func_5465'] = func_5465
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3761_call = mod.get_global_var('func_3761')
func_3762_call = mutated_mod.get_global_var('func_3762')
call_5476 = relay.TupleGetItem(func_3761_call(), 0)
call_5477 = relay.TupleGetItem(func_3762_call(), 0)
output = relay.Tuple([call_5476,])
output2 = relay.Tuple([call_5477,])
func_5478 = relay.Function([], output)
mod['func_5478'] = func_5478
mod = relay.transform.InferType()(mod)
output = func_5478()
func_5479 = relay.Function([], output)
mutated_mod['func_5479'] = func_5479
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4241_call = mod.get_global_var('func_4241')
func_4242_call = mutated_mod.get_global_var('func_4242')
call_5480 = relay.TupleGetItem(func_4241_call(), 0)
call_5481 = relay.TupleGetItem(func_4242_call(), 0)
output = relay.Tuple([call_5480,])
output2 = relay.Tuple([call_5481,])
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
func_4398_call = mod.get_global_var('func_4398')
func_4399_call = mutated_mod.get_global_var('func_4399')
call_5534 = relay.TupleGetItem(func_4398_call(), 0)
call_5535 = relay.TupleGetItem(func_4399_call(), 0)
output = relay.Tuple([call_5534,])
output2 = relay.Tuple([call_5535,])
func_5552 = relay.Function([], output)
mod['func_5552'] = func_5552
mod = relay.transform.InferType()(mod)
output = func_5552()
func_5553 = relay.Function([], output)
mutated_mod['func_5553'] = func_5553
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5554 = relay.var("var_5554", dtype = "float32", shape = (6, 11, 8))#candidate|5554|(6, 11, 8)|var|float32
uop_5555 = relay.cos(var_5554.astype('float32')) # shape=(6, 11, 8)
func_1061_call = mod.get_global_var('func_1061')
func_1065_call = mutated_mod.get_global_var('func_1065')
var_5563 = relay.var("var_5563", dtype = "uint16", shape = (1, 200))#candidate|5563|(1, 200)|var|uint16
var_5564 = relay.var("var_5564", dtype = "float32", shape = (500,))#candidate|5564|(500,)|var|float32
call_5562 = relay.TupleGetItem(func_1061_call(relay.reshape(var_5563.astype('uint16'), [8, 5, 5]), relay.reshape(var_5563.astype('uint16'), [8, 5, 5]), relay.reshape(var_5564.astype('float32'), [500,]), ), 0)
call_5565 = relay.TupleGetItem(func_1065_call(relay.reshape(var_5563.astype('uint16'), [8, 5, 5]), relay.reshape(var_5563.astype('uint16'), [8, 5, 5]), relay.reshape(var_5564.astype('float32'), [500,]), ), 0)
output = relay.Tuple([uop_5555,call_5562,var_5563,var_5564,])
output2 = relay.Tuple([uop_5555,call_5565,var_5563,var_5564,])
func_5566 = relay.Function([var_5554,var_5563,var_5564,], output)
mod['func_5566'] = func_5566
mod = relay.transform.InferType()(mod)
var_5567 = relay.var("var_5567", dtype = "float32", shape = (6, 11, 8))#candidate|5567|(6, 11, 8)|var|float32
var_5568 = relay.var("var_5568", dtype = "uint16", shape = (1, 200))#candidate|5568|(1, 200)|var|uint16
var_5569 = relay.var("var_5569", dtype = "float32", shape = (500,))#candidate|5569|(500,)|var|float32
output = func_5566(var_5567,var_5568,var_5569,)
func_5570 = relay.Function([var_5567,var_5568,var_5569,], output)
mutated_mod['func_5570'] = func_5570
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4770_call = mod.get_global_var('func_4770')
func_4771_call = mutated_mod.get_global_var('func_4771')
call_5579 = relay.TupleGetItem(func_4770_call(), 0)
call_5580 = relay.TupleGetItem(func_4771_call(), 0)
output = call_5579
output2 = call_5580
func_5591 = relay.Function([], output)
mod['func_5591'] = func_5591
mod = relay.transform.InferType()(mod)
mutated_mod['func_5591'] = func_5591
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5591_call = mutated_mod.get_global_var('func_5591')
call_5592 = func_5591_call()
output = call_5592
func_5593 = relay.Function([], output)
mutated_mod['func_5593'] = func_5593
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4770_call = mod.get_global_var('func_4770')
func_4771_call = mutated_mod.get_global_var('func_4771')
call_5601 = relay.TupleGetItem(func_4770_call(), 1)
call_5602 = relay.TupleGetItem(func_4771_call(), 1)
output = call_5601
output2 = call_5602
func_5632 = relay.Function([], output)
mod['func_5632'] = func_5632
mod = relay.transform.InferType()(mod)
output = func_5632()
func_5633 = relay.Function([], output)
mutated_mod['func_5633'] = func_5633
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5412_call = mod.get_global_var('func_5412')
func_5414_call = mutated_mod.get_global_var('func_5414')
call_5637 = relay.TupleGetItem(func_5412_call(), 1)
call_5638 = relay.TupleGetItem(func_5414_call(), 1)
func_3183_call = mod.get_global_var('func_3183')
func_3186_call = mutated_mod.get_global_var('func_3186')
const_5642 = relay.const([-3.634398,-3.980683,-2.932123,-2.955997,0.319053,-4.557050,-6.421350,1.095983,0.574849,0.814197,2.828744,3.569954,1.878872,6.938230,7.693589,-4.263651,-2.050362,-9.157722,-3.951472,-5.342604,-9.833779,-5.218639,-1.657203,6.421143,0.473548,-1.976733,0.966067,-3.677533,4.138374,-5.011489,-2.368131,-3.159091,8.252672,2.714964,0.774067,-8.655890,-7.705459,4.117655,-2.642191,4.277728,1.902524,-9.707807,5.491941,9.521067,-6.571746,3.708494,-8.753775,-9.870659,-6.110564,7.361154,4.599774,9.595163,-2.117712,-2.772781,8.786550,-0.551666,1.593371,-3.809796,-7.184869,-8.416499,2.240206,6.657580,6.786615,6.532405,-9.158178,-3.217696,-1.903686,3.011993,-6.788793,4.224580,5.462691,-4.363787,9.862535,8.716012,-8.232215,-5.919731,1.270701,5.107831,5.211800,0.620154,8.458801,9.209339,4.468665,-1.797787,-8.994595,-7.425361,-5.774883,3.873845,6.275336,2.494974,-8.175744,8.607334,8.116461,-6.743808,7.899575,-0.110976,1.914506,1.950771,1.144548,-1.121752,8.036742,2.596727,1.208820,0.413235,-4.948208,-9.423124,3.147329,-5.929221,-7.211351,3.548851,-9.102331,-1.852355,-2.546964,3.547372,-1.672857,4.802708,-9.318297,6.608413,3.507468,-8.883599,5.314067,-1.744114,-7.458611,3.406079,-3.147950,-6.771828,0.078142,-3.504894,-8.363589,3.996297,-8.157210,7.477521,6.830709,-6.703867,0.153687,-6.092339,-3.006255,4.466686,-7.022221,9.718849,-8.752844,9.373961,6.095878,8.061722,2.091510,-2.123237,8.122553,-0.145076,-7.280240,-0.051344,8.346141,-1.095757,7.715070,-4.485021,-4.408852,-7.061099,-3.299451,-0.700089,-9.344086,4.772832,-9.373365,7.149915,1.689453,6.121873,-7.896753,-0.645818,-0.740013,9.277021], dtype = "float32")#candidate|5642|(168,)|const|float32
call_5641 = relay.TupleGetItem(func_3183_call(relay.reshape(const_5642.astype('float32'), [1, 12, 14])), 0)
call_5643 = relay.TupleGetItem(func_3186_call(relay.reshape(const_5642.astype('float32'), [1, 12, 14])), 0)
func_3658_call = mod.get_global_var('func_3658')
func_3660_call = mutated_mod.get_global_var('func_3660')
call_5647 = relay.TupleGetItem(func_3658_call(), 0)
call_5648 = relay.TupleGetItem(func_3660_call(), 0)
bop_5683 = relay.greater(call_5641.astype('bool'), relay.reshape(const_5642.astype('bool'), relay.shape_of(call_5641))) # shape=(1, 12, 14)
bop_5686 = relay.greater(call_5643.astype('bool'), relay.reshape(const_5642.astype('bool'), relay.shape_of(call_5643))) # shape=(1, 12, 14)
bop_5687 = relay.bitwise_and(call_5637.astype('int16'), relay.reshape(call_5647.astype('int16'), relay.shape_of(call_5637))) # shape=(14, 9, 6)
bop_5690 = relay.bitwise_and(call_5638.astype('int16'), relay.reshape(call_5648.astype('int16'), relay.shape_of(call_5638))) # shape=(14, 9, 6)
uop_5708 = relay.atanh(bop_5683.astype('float32')) # shape=(1, 12, 14)
uop_5710 = relay.atanh(bop_5686.astype('float32')) # shape=(1, 12, 14)
output = relay.Tuple([bop_5687,uop_5708,])
output2 = relay.Tuple([bop_5690,uop_5710,])
func_5713 = relay.Function([], output)
mod['func_5713'] = func_5713
mod = relay.transform.InferType()(mod)
mutated_mod['func_5713'] = func_5713
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5713_call = mutated_mod.get_global_var('func_5713')
call_5714 = func_5713_call()
output = call_5714
func_5715 = relay.Function([], output)
mutated_mod['func_5715'] = func_5715
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5275_call = mod.get_global_var('func_5275')
func_5277_call = mutated_mod.get_global_var('func_5277')
call_5806 = func_5275_call()
call_5807 = func_5275_call()
uop_5815 = relay.atanh(call_5806.astype('float64')) # shape=(14, 9, 6)
uop_5817 = relay.atanh(call_5807.astype('float64')) # shape=(14, 9, 6)
func_4858_call = mod.get_global_var('func_4858')
func_4860_call = mutated_mod.get_global_var('func_4860')
call_5830 = func_4858_call()
call_5831 = func_4858_call()
output = relay.Tuple([uop_5815,call_5830,])
output2 = relay.Tuple([uop_5817,call_5831,])
func_5832 = relay.Function([], output)
mod['func_5832'] = func_5832
mod = relay.transform.InferType()(mod)
output = func_5832()
func_5833 = relay.Function([], output)
mutated_mod['func_5833'] = func_5833
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4158_call = mod.get_global_var('func_4158')
func_4159_call = mutated_mod.get_global_var('func_4159')
call_5882 = relay.TupleGetItem(func_4158_call(), 0)
call_5883 = relay.TupleGetItem(func_4159_call(), 0)
output = relay.Tuple([call_5882,])
output2 = relay.Tuple([call_5883,])
func_5885 = relay.Function([], output)
mod['func_5885'] = func_5885
mod = relay.transform.InferType()(mod)
mutated_mod['func_5885'] = func_5885
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5885_call = mutated_mod.get_global_var('func_5885')
call_5886 = func_5885_call()
output = call_5886
func_5887 = relay.Function([], output)
mutated_mod['func_5887'] = func_5887
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5933 = relay.const([[[8,10,9,-4,8,-10,-10,5,-8,6,4,-6,3,6],[2,-9,7,2,-5,-9,-6,2,-5,-7,5,1,-1,10],[4,9,-5,8,-6,-10,-9,-6,9,10,6,8,-5,1],[-3,-9,7,5,-6,6,5,5,-6,-8,-10,10,8,-7]],[[5,8,-9,9,4,-1,-6,2,-4,5,7,-6,2,3],[4,-4,8,-10,-10,4,-2,-6,-4,2,-5,-8,10,1],[10,5,-4,4,2,8,3,-8,10,5,-2,4,4,4],[-5,-8,-9,-10,2,4,2,-8,7,-1,-9,3,-5,-1]],[[-6,-5,-9,10,5,-2,8,1,-9,4,-4,-5,3,-6],[-2,9,3,-2,6,4,-4,8,-2,9,-7,-1,9,-6],[3,-3,3,6,-8,10,-10,5,9,-5,2,6,8,4],[3,-2,-4,-3,10,2,-6,2,-7,2,-2,-8,-1,-6]]], dtype = "uint16")#candidate|5933|(3, 4, 14)|const|uint16
var_5934 = relay.var("var_5934", dtype = "uint16", shape = (3, 4, 14))#candidate|5934|(3, 4, 14)|var|uint16
bop_5935 = relay.right_shift(const_5933.astype('uint16'), relay.reshape(var_5934.astype('uint16'), relay.shape_of(const_5933))) # shape=(3, 4, 14)
func_5343_call = mod.get_global_var('func_5343')
func_5346_call = mutated_mod.get_global_var('func_5346')
const_5950 = relay.const([8.260924,8.331464,9.188734,-9.129612,-9.793479,-1.012226,-0.089210,9.883342,-6.116014,2.160768,9.887851,7.152527,-1.538831,-2.160353,-2.669325,0.519175,-0.786514,-2.421363,-9.099542,3.692927,-6.024934,-7.952381,-1.578823,6.141200,7.828100,-6.378331,3.463418,-7.276619,-4.362777,6.951111,9.740374,-3.960218,-7.663450,8.869968,7.274622,7.393866,-7.748821,-6.456872,-6.476849,6.700142,5.406732,-1.102347,-4.134911,-9.802960,9.541124,7.544753,-9.552514,-0.478736,0.804104,9.953030,-3.622864,-3.035302,0.789873,6.370758,5.071319,9.644260,-4.174622,9.789303,-3.448290,6.087149,5.426505,-3.715080,-4.529602,-7.450561,7.389368,-0.690822,5.144593,-3.053079,-9.633781,-9.450802,6.517989,-1.944218,3.711237,-7.082206,4.461169,5.123630,-3.285949,4.490635,-0.351395,-5.023549,1.050415,4.972957,-5.341945,0.391085,6.364275,-5.337060,1.074395,1.514324,-4.489554,3.660438,5.233867,-4.274350,-9.781622,1.099627,-8.066791,-8.744282,-9.174389,-2.400722,-1.507677,5.333917,8.497878,-5.062633,-8.816019,4.282161,3.456212,6.357018,1.765893,-0.967574,5.813931,-2.774268,-5.845235,0.066830,-8.244947,7.775208,-1.970181,-5.421026,-3.212872,-4.179925,-4.032116,5.969167,-1.488905,8.719113,-7.555825,-4.257344,2.018115,3.059248,5.379975,-4.629539,-5.768833,-4.721181,8.232946,-2.553985,7.333930,-0.714966,-0.199288,3.123629,-5.087063,-2.680261,3.141834,-3.728945,1.272295,-9.087186,5.375438,-2.361140,-6.236620,-6.218504,-6.434446,1.689897,9.660875,9.594866,0.290873,2.861102,8.774101,-6.614357,-7.388210,4.084974,0.984657,-0.345978,5.694905,-3.784455,-5.535953,4.384734,-3.601334,-1.114196,-1.145499,7.478048,0.609710,-7.646723,6.608599,7.484740,3.832098,4.143242,-6.339071,2.528269,3.773137,3.695586,-1.314400,-5.188620,4.400342,8.337484,-6.389566,5.993878,5.442889,5.427678,-4.376580,-9.882017,0.813262,-3.191454,0.609304,9.882673,-0.373701,-1.973870,1.873015,1.103341,-0.140130,1.335139,1.564988,-9.694801,-6.738134,9.404756,-9.936519,-2.165587,-5.874872,5.922834,2.813686,-9.979081,6.817240,-7.521073,4.289818,3.438154,-6.435538,-9.650898,2.042451,-4.641775,-3.164971,-1.518261,1.548566,2.444219,-7.309992,-6.747888,4.690955,7.986451,1.166366,-2.244163,2.115277,-0.384417,-1.716902,9.544961,4.629648,5.633918,-6.719597,-1.919153,-4.059569,4.553788,-8.098127,-8.187331,-3.403079,-5.105226,-3.778117,-0.046709,-6.691064,2.160295,3.797109,-4.906085,2.027411,9.558079,-8.139716,1.178636,3.230765,4.606526,-1.185086,4.393432,9.053720,0.291380,-4.731883,9.361178,-8.437541,9.849678,3.132165,0.178124,1.460682,-7.696290,-1.804042,8.892214,-3.353035,-5.120952,-3.968683,7.770770,4.933569,8.587548,-1.220840,1.775555,-3.265503,6.020334,-6.208615,-5.432947,0.444526,6.357777,-7.041194,8.079676,5.624327,-2.468587,1.537929,7.202796,-3.114804,6.806339,7.963390,1.912800,6.271428,-6.941001,6.942604,-9.702209,0.120734,0.083509,-6.495519,7.980192,-2.818575,7.797135,8.367047,-4.962309,-5.870917,9.105850,-0.953915,6.353809,2.983401,-3.600926,-9.982498,2.474035,-2.519004,6.781696,3.507671,0.733106,-5.550881,3.684551,9.715003,1.085735,3.648863,-9.665352,-2.110150,-1.803298,8.588542,-6.847021,3.360358,0.788187,-7.819514,-0.284996,9.946102,7.121818,-2.251384,-7.372204,6.666631,4.068963,-4.224924,-3.882727,4.800816,-3.601703,4.740066,-5.673413,-2.689130,5.659597,8.856986,-7.807930,9.355536,-5.138378,-5.576083,5.655869,4.946452,1.763525,-8.757078,-7.452582,-1.176715,-1.652378,5.760914,-2.061993,8.823600,9.994814,6.471621,7.630259,1.406999,-3.625311,-0.584922,3.548404,2.656220,1.609951,6.405467,6.993590,-7.274180,7.461691,1.657556,9.973843,0.986435,6.462625,-5.476149,5.220692,-3.344456,-2.375599,-9.268175,-6.493756,-3.745653,5.553496,6.130114,1.748659,6.561920,-4.217763,-6.222275,3.951615,-3.032601,-3.438240,9.389556,-5.870255,9.910707,2.120550,2.349670,8.802561,3.859894,6.976720,-9.497027,3.441966,9.683744,-6.977463,5.913341,-8.180987,-8.929631,1.225771,-2.586232,2.595131,-0.604085,5.807867,5.853536,3.345554,-2.813151,9.416833,7.901488,-6.302238,-1.585447,-3.114230,-7.238852,0.634417,1.855052,-4.120778,0.971731,9.420398,-6.139818,9.555887,-9.585758,1.925296,0.532279,8.920743,6.552920,8.638514,-5.554693,9.346653,-8.890636,3.412077,5.792866,-5.208671,0.895316,-3.360568,-6.068686,3.936389,-1.659819,1.101257,-0.705663,-4.299403,-8.616338,5.898492,9.163513,8.664197,-6.276808,1.091842,1.347518,-8.874572,-0.109484,-1.774990,-9.224818,6.493510,-0.670823,-0.986439,0.096520,-6.749810,-3.652716,-0.886959,0.168431,-2.120640,-1.271348,6.562035,3.302325,-9.217783,8.395464,-4.174972,7.847262,-4.793882,5.723819,-1.442085,-9.644607,-6.001360,-2.957081,-0.451582,3.729133,9.475675,4.583512,9.916526,-4.295200,-8.780282,-9.677828,0.031789,-3.472813,-6.897211,-0.992717,-3.540270,0.244803,-6.292496,4.545661,9.056867,1.125519,-4.947980,-7.322247,1.549381,3.986027,-1.740771,-6.404783,5.904241,2.123016,-8.527079,-5.432350,-3.314397,-2.091346,-6.132880,-1.921558,-4.299144,-1.054686,-4.674746,-9.832686,-8.002479,0.590406,0.303783,-3.511053,-8.881614,-0.721048,-4.239506,3.146800,3.813449,5.806201,2.024325,8.830353,6.225395,-3.682079,-9.751090,1.532871,-1.811609,3.279481,-8.082084,2.117309,-2.477455,-0.965245,-9.340561,2.046557,0.050554,7.512130,-5.331843,-8.536199,8.076165,2.662915,1.229220,-4.769388,9.993696,6.216219,1.603693,-4.718794,1.189422,-3.833400,-5.410230,7.171332,-8.687504,-7.782261,9.378853,-2.607817,7.687287,9.772338,-0.890442,1.258539,2.705757,-5.827159,0.748201,-6.883918,3.180255,-2.436717,4.217727,1.126782,4.057087,-7.386477,-5.024254,9.582742,3.092640,-9.518001,-9.088062,3.445254,-7.074146,-5.818117,1.733950,-7.670599,-1.449998,-4.102331,-3.894830,7.438751,-0.891959,1.564059,6.108866,-2.891876,0.912489,-9.517195,-8.831314,1.868488,2.388810,-3.365867,0.393101,4.929686,-6.883593,2.605989,1.653014,-5.911085,-2.576568,-0.276098,-7.700885,-7.058913,2.053612,2.547759,5.603895,9.518145,-7.479091,3.126437,-4.313532,6.117244,-4.544570,-4.005654,-9.772568,4.801872,-5.409055,-9.995905,0.547045,-0.353377,4.563053,-2.130701,-1.990866,-1.642806,-7.291761,-5.496893,-0.907822,5.151131,-7.595806,6.564755,-4.222936,-0.133855,-1.433834,0.579329,8.388338,0.761981,2.365022,7.462138,3.521801,-5.142966,7.127680,-1.534457,6.260307,2.424806,3.604315,-5.290064,3.019127,-5.852666,2.852538,5.401498,0.916327,8.166428,3.521237,5.991290,-9.329967,-1.754494,-4.275177,-5.085442,-4.328158,-8.555385,-2.210687,6.102096,4.748862,6.516257,4.934081,1.849612,0.457272,0.527031,-5.279853,9.680624,-8.874701,-0.638814,4.955838,-3.421336,-6.642865,8.764689,5.408536,1.043142,9.623481,7.352743,7.248397,9.862949,-8.219345,9.749157,3.779853,8.543359,-0.337817,5.028630,-8.227461,8.989285,-3.973486,9.364574,2.930117,-7.690712,-6.374514,0.351536,-9.980377,-2.230628,8.653337,1.339621,6.837265,0.528379,0.354157,4.134692,-0.721120,-3.720685,3.302993,9.558291,-7.954104,8.614580,1.047715,9.656574,-7.685519,-4.402377,0.354820,-7.123858,1.134765,5.538027,-7.099175,-1.171412,4.432163,7.546269,6.889988,-5.039884,-5.371032,-7.597933,-4.767226,-5.646984,1.682299,5.742252,-1.675518,7.062013,0.973127,-7.877846,1.577159,-6.006405,-0.938528,-9.007718,-0.886447,9.645467,-0.419924,2.975941,2.340651,9.102691,-3.367519,-8.696923,4.406557,-4.939434,-7.706237,-6.946055,-2.608958,-6.301945,4.521033,-6.230023,8.138458,-0.853020,9.531127,4.685400,7.016935,1.270401,1.544549,4.206239,-0.863880,4.336074,-7.918222,-3.056623,-1.323144,7.293948,5.256898,-8.618270,-2.124278,4.356336,-4.754377,-9.883928,7.956901,7.482522,0.175524,8.322790,6.480768,-1.847962,8.935755,-5.499846,-2.514489,7.631709,6.821371,-3.240366,-0.527170,5.852096,-5.979764,4.723158,7.191403,-5.404331,3.895791,-0.350291,-8.680781,-1.435801,-4.374103,-6.560536,5.853437,-4.015697,1.049968,-5.961690,-9.422854,-5.618052,5.268471,6.513624,-3.558661,-7.530304,1.420115,-7.130931,2.007484,0.853849,4.810311,-6.393286,0.449554,4.492601,-0.979659,0.656467,1.469039,6.605736,1.881265,-1.317240,9.719448,3.196494,9.119645,-0.764376,-0.741412,-5.883827,9.126613,-6.404486,-1.676821,6.503641,4.060932,2.691219,-4.273051,-0.938384,2.013420,-1.932042,3.363160,-4.418240,8.054465,7.143176,-1.082324,-6.254897,2.101994,2.268288,-7.144355,-0.503831,9.397247,1.868937,-7.343159,0.677622,-3.941898,-1.936019,1.923367,-6.452044,-2.784797,-1.162054,-8.585584,-1.909381,-3.806036,9.107438,4.370714,-6.353156,3.831841,-4.145401,0.509642,-8.620566,1.845503,8.975310,8.217028,-9.428982,-6.386911,-0.168045,1.944648,-0.489470,-7.283597,-3.466649,3.285916,-0.444374,-8.437347,-3.113198,-2.025381,3.730598,-1.583260,-0.361000,6.112294,0.784308,-2.288219,-9.501863,-6.000511,3.835228,-1.578361,-4.956065,-6.888597,-8.659416,-8.857514,3.281752,4.544172,-2.804741,3.659504,7.124771,5.335539,-9.260188,7.673879,2.741462,1.676037,-5.745739,2.877452,3.536713,-8.076849,-5.239137,8.282116,8.785691,1.047122,-5.835587,3.712013,1.979244,-3.082448,-4.438818,-5.905752,1.239027,-2.260840,1.384737,3.694634,0.772302,-8.800897,-3.163910,0.007842,0.202629,8.007295,-5.636537,5.092592,-8.934489,6.501515,6.911634,-3.015849,-3.979418,1.344749,-7.132695,-3.825155,-6.436617,-3.841786,-8.561747,-4.058718,-1.044065,6.802889,-4.660833,-1.987611,-2.332068,3.643727,0.274475,2.302648,-7.307070,7.443625,5.455882,8.696988,-8.824790,-3.451321,2.018577,-4.199168,-1.893293,-3.502640,9.235590,6.319883,2.537679,7.747234,9.809766,-3.624232,7.950023,-4.130320,8.203769,-0.163264,4.372126,8.251618,-4.144061,-9.248537,2.101117,5.975534,6.648787,6.364692,-4.716618,7.474109,7.348852,8.040462,8.988417,7.051625,9.345926,7.076151,-4.676963,-9.502716,-1.619144,5.783243,5.174887,-0.454556,-9.419555,3.449084,7.678224,-6.351696,-3.225766,8.791345,7.165000,7.752264,7.635090,-6.057574,8.610571,-0.768430,6.734277,0.662511,-5.402111,-3.063810,4.134661,2.786477,-4.006914,0.722748,-3.079083,9.364861,9.600910,-9.862378,2.457644,-0.770977,6.344066,-4.220729,4.839823,-8.206368,-3.388519,-9.490409,-9.922679,-0.040853,2.992896,-4.734688,-8.592820,6.663358,-6.136717,-2.296634,-8.330811,-0.928469,3.545125,8.960677,-5.308770,5.719352,-1.634282,7.541344,5.719687,8.039439,8.382646,-7.290581,4.616298,-8.652798,-1.797657,6.165807,5.871510,-1.300511,5.920020,5.308380,6.915107,-5.456816,-9.415012,9.885434,8.886070,-2.158691,-2.236315,-3.247045,5.500206,6.423281,-2.545242,-5.333060,-0.389607,-0.417753,-7.770176,0.739767,-2.039652,5.932644,6.201150,6.434343,-0.985434,-0.329138,-4.819487,-4.653349,2.992527,2.928931,4.574436,5.893093,4.223265,2.395506,-1.682535,9.057075,-0.829677,4.204022,1.808985,-7.366560,9.569800,-3.725848,2.130282,5.443433,-3.481082,-5.056709,-8.698596,6.844925,-4.311190,-3.201505,-8.934143,1.965760,-2.787756,-3.467796,8.295792,2.668141,3.132087,9.242877,5.684771,5.841505,5.285686,4.000602,-0.358769,6.427081,7.633790,8.914802,-2.099581,-7.663566,7.307087,-5.434455,8.799230,7.195801,-6.547707,3.020354,2.933137,8.612554,0.120138,2.587339,-1.587697,-2.622867,-3.883783,4.029516,-1.808956,8.893659,-0.882446,0.002970,-9.495152,4.719977,5.415358,-0.499747,6.167743,8.588720,-7.065383,-9.875050,-0.366081,-9.066011,-8.824372,8.276832,6.440395,6.456390,-7.759357,0.811034,7.901906,2.463296,0.462554,-2.970344,-3.274309,9.433216,-2.534748,2.551728,-1.310459,4.744096,3.150368,-2.897590,4.812674,-5.089717,-7.603048,-3.596021,-2.047314,-9.847972,0.840720,1.102439,-5.015950,-6.314499,-7.353677,3.075792,7.706085,-3.869943,0.021399,9.003375,-1.358275,1.332251,9.035646,-2.655331,6.612702,-6.909334,8.747935,-9.933993,-8.130861,-6.431133,-1.514271,-9.874532,-3.096148,-0.673710,4.459638,9.413711,-2.967063,-0.429606,-7.334714,9.915497,8.339152,6.961738,6.765354,-5.887390,-6.816956,8.625803,8.506239,2.408854,-3.271607,2.160455,9.260481,1.103152,2.649810,-9.055948,-3.836823,-6.385246,3.045556,2.205886,5.509345,-1.777527,-6.660180,5.607174,6.395018,-4.132024,-0.639223,3.643321,-4.279605,3.333278,-4.133358,2.577627,-9.952371,-6.865939,9.246290,-2.681080,-9.404023,9.886321,-9.965702,-1.916848,8.147777,2.469765,-7.338148,0.262291,9.593920,5.425240,-6.656347,4.461086,-2.638415,-2.524554,4.388311,-5.527525,-9.969463,-0.997562,-9.066757,-2.860536,5.146330,-3.645932,3.257716,-4.216110,-4.424257,-8.795623,3.175107,8.273298,-6.836700,0.367756,6.492061,2.009040,9.576482,-0.605669,-4.828361,4.698267,6.393390,2.964801,-1.501921,1.132967,0.850981,1.876668,6.815754,-7.275038,1.489004,4.130557,-7.046825,-3.356146,1.667022,7.029362,7.271752,9.528526,-7.332879,5.961385,2.086318,-5.412973,7.008961,0.954746,-6.306134,-5.298670,5.901065,-0.359562,-0.762629,-2.516060,-7.163414,4.460419,-5.943886,-4.434366,0.513701,0.340723,-9.174251,-5.831026,-2.726439,8.626709,2.126650,-3.143693,0.301114,-0.841012,3.070114,4.199245,5.013410,8.533006,-3.804876,-5.983085,-6.599047,-7.542383,8.219990,-8.837748,-0.881295,5.655966,0.836549,-4.203980,-8.818839,-5.878202,9.288888,6.450694,-6.121785,3.688417,-4.505055,-2.211749,5.061860,-4.445487,3.641839,-5.795848,-8.270564,-5.269211,0.738851,-7.714160,8.129895,4.418474,8.399593,7.680930,-6.706269,-6.087070,7.908132,4.554638,4.425195,7.383260,-5.840259,-7.001504,7.010678,-4.671434,6.400914,2.810823,5.600577,-4.763105,4.899869,-6.909727,-6.462625,5.146241,4.370906,-0.380417,-2.932760,-2.305755,-1.324127,1.648810,1.747678,-7.197737,-0.968085,5.997818,7.606539,-4.073620,-4.479136,-3.796996,0.484652,-8.008558,-3.592704,4.516841,-8.736619,3.720768,-3.376984,8.609992,-0.148102,1.542501,2.609686,-4.134528,-2.186479,2.623930,5.571787,8.817120,1.008551,4.213421,-7.519206,-7.783978,-9.107767,4.933237,-0.290742,-6.427893,5.722099,-4.177649,6.746188,7.362569,8.063062,-9.033525,-2.870959,-5.087454,9.970993,2.063637,-7.101522,-7.842283,1.881691,-7.106880,-9.721407,-6.113981,-6.002779,-6.055418,1.265349,1.210380,2.704300,4.120532,2.498594,6.990507,9.204472,-0.402981,2.758871,1.955888,6.965225,-9.337925,-1.869513,4.804597,8.890131,-3.880440,3.120947,-7.048734,8.888277,-0.585968,7.448082,6.824086,-8.319764,-5.827100,9.661657,-8.221031,7.778731,-6.670909,5.343727,-8.032799,-7.917791,6.422034,-5.997536,-4.185550], dtype = "float32")#candidate|5950|(1456,)|const|float32
call_5949 = relay.TupleGetItem(func_5343_call(relay.reshape(const_5950.astype('float32'), [14, 8, 13])), 0)
call_5951 = relay.TupleGetItem(func_5346_call(relay.reshape(const_5950.astype('float32'), [14, 8, 13])), 0)
bop_5952 = relay.maximum(const_5950.astype('uint8'), relay.reshape(call_5949.astype('uint8'), relay.shape_of(const_5950))) # shape=(1456,)
bop_5955 = relay.maximum(const_5950.astype('uint8'), relay.reshape(call_5951.astype('uint8'), relay.shape_of(const_5950))) # shape=(1456,)
uop_5972 = relay.log(var_5934.astype('float64')) # shape=(3, 4, 14)
output = relay.Tuple([bop_5935,bop_5952,uop_5972,])
output2 = relay.Tuple([bop_5935,bop_5955,uop_5972,])
func_5974 = relay.Function([var_5934,], output)
mod['func_5974'] = func_5974
mod = relay.transform.InferType()(mod)
mutated_mod['func_5974'] = func_5974
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5975 = relay.var("var_5975", dtype = "uint16", shape = (3, 4, 14))#candidate|5975|(3, 4, 14)|var|uint16
func_5974_call = mutated_mod.get_global_var('func_5974')
call_5976 = func_5974_call(var_5975)
output = call_5976
func_5977 = relay.Function([var_5975], output)
mutated_mod['func_5977'] = func_5977
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4858_call = mod.get_global_var('func_4858')
func_4860_call = mutated_mod.get_global_var('func_4860')
call_6019 = func_4858_call()
call_6020 = func_4858_call()
output = call_6019
output2 = call_6020
func_6066 = relay.Function([], output)
mod['func_6066'] = func_6066
mod = relay.transform.InferType()(mod)
mutated_mod['func_6066'] = func_6066
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6066_call = mutated_mod.get_global_var('func_6066')
call_6067 = func_6066_call()
output = call_6067
func_6068 = relay.Function([], output)
mutated_mod['func_6068'] = func_6068
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5275_call = mod.get_global_var('func_5275')
func_5277_call = mutated_mod.get_global_var('func_5277')
call_6105 = func_5275_call()
call_6106 = func_5275_call()
output = relay.Tuple([call_6105,])
output2 = relay.Tuple([call_6106,])
func_6130 = relay.Function([], output)
mod['func_6130'] = func_6130
mod = relay.transform.InferType()(mod)
mutated_mod['func_6130'] = func_6130
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6130_call = mutated_mod.get_global_var('func_6130')
call_6131 = func_6130_call()
output = call_6131
func_6132 = relay.Function([], output)
mutated_mod['func_6132'] = func_6132
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5885_call = mod.get_global_var('func_5885')
func_5887_call = mutated_mod.get_global_var('func_5887')
call_6151 = relay.TupleGetItem(func_5885_call(), 0)
call_6152 = relay.TupleGetItem(func_5887_call(), 0)
func_4343_call = mod.get_global_var('func_4343')
func_4345_call = mutated_mod.get_global_var('func_4345')
call_6153 = relay.TupleGetItem(func_4343_call(relay.reshape(call_6151.astype('float32'), [14, 9, 6])), 0)
call_6154 = relay.TupleGetItem(func_4345_call(relay.reshape(call_6151.astype('float32'), [14, 9, 6])), 0)
func_5506_call = mod.get_global_var('func_5506')
func_5508_call = mutated_mod.get_global_var('func_5508')
call_6177 = relay.TupleGetItem(func_5506_call(), 0)
call_6178 = relay.TupleGetItem(func_5508_call(), 0)
output = relay.Tuple([call_6151,call_6153,call_6177,])
output2 = relay.Tuple([call_6152,call_6154,call_6178,])
func_6182 = relay.Function([], output)
mod['func_6182'] = func_6182
mod = relay.transform.InferType()(mod)
output = func_6182()
func_6183 = relay.Function([], output)
mutated_mod['func_6183'] = func_6183
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5003_call = mod.get_global_var('func_5003')
func_5005_call = mutated_mod.get_global_var('func_5005')
call_6192 = relay.TupleGetItem(func_5003_call(), 2)
call_6193 = relay.TupleGetItem(func_5005_call(), 2)
func_1061_call = mod.get_global_var('func_1061')
func_1065_call = mutated_mod.get_global_var('func_1065')
var_6203 = relay.var("var_6203", dtype = "uint16", shape = (200,))#candidate|6203|(200,)|var|uint16
var_6204 = relay.var("var_6204", dtype = "float32", shape = (500,))#candidate|6204|(500,)|var|float32
call_6202 = relay.TupleGetItem(func_1061_call(relay.reshape(var_6203.astype('uint16'), [8, 5, 5]), relay.reshape(var_6203.astype('uint16'), [8, 5, 5]), relay.reshape(var_6204.astype('float32'), [500,]), ), 1)
call_6205 = relay.TupleGetItem(func_1065_call(relay.reshape(var_6203.astype('uint16'), [8, 5, 5]), relay.reshape(var_6203.astype('uint16'), [8, 5, 5]), relay.reshape(var_6204.astype('float32'), [500,]), ), 1)
uop_6206 = relay.rsqrt(var_6203.astype('float32')) # shape=(200,)
output = relay.Tuple([call_6192,call_6202,var_6204,uop_6206,])
output2 = relay.Tuple([call_6193,call_6205,var_6204,uop_6206,])
func_6242 = relay.Function([var_6203,var_6204,], output)
mod['func_6242'] = func_6242
mod = relay.transform.InferType()(mod)
var_6243 = relay.var("var_6243", dtype = "uint16", shape = (200,))#candidate|6243|(200,)|var|uint16
var_6244 = relay.var("var_6244", dtype = "float32", shape = (500,))#candidate|6244|(500,)|var|float32
output = func_6242(var_6243,var_6244,)
func_6245 = relay.Function([var_6243,var_6244,], output)
mutated_mod['func_6245'] = func_6245
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5275_call = mod.get_global_var('func_5275')
func_5277_call = mutated_mod.get_global_var('func_5277')
call_6284 = func_5275_call()
call_6285 = func_5275_call()
func_4061_call = mod.get_global_var('func_4061')
func_4064_call = mutated_mod.get_global_var('func_4064')
var_6288 = relay.var("var_6288", dtype = "bool", shape = (1980,))#candidate|6288|(1980,)|var|bool
call_6287 = relay.TupleGetItem(func_4061_call(relay.reshape(call_6284.astype('float32'), [14, 9, 6]), relay.reshape(var_6288.astype('bool'), [1980,]), ), 2)
call_6289 = relay.TupleGetItem(func_4064_call(relay.reshape(call_6284.astype('float32'), [14, 9, 6]), relay.reshape(var_6288.astype('bool'), [1980,]), ), 2)
func_5343_call = mod.get_global_var('func_5343')
func_5346_call = mutated_mod.get_global_var('func_5346')
var_6297 = relay.var("var_6297", dtype = "float32", shape = (1456,))#candidate|6297|(1456,)|var|float32
call_6296 = relay.TupleGetItem(func_5343_call(relay.reshape(var_6297.astype('float32'), [14, 8, 13])), 1)
call_6298 = relay.TupleGetItem(func_5346_call(relay.reshape(var_6297.astype('float32'), [14, 8, 13])), 1)
uop_6302 = relay.tan(var_6288.astype('float32')) # shape=(1980,)
output = relay.Tuple([call_6284,call_6287,call_6296,var_6297,uop_6302,])
output2 = relay.Tuple([call_6285,call_6289,call_6298,var_6297,uop_6302,])
func_6304 = relay.Function([var_6288,var_6297,], output)
mod['func_6304'] = func_6304
mod = relay.transform.InferType()(mod)
var_6305 = relay.var("var_6305", dtype = "bool", shape = (1980,))#candidate|6305|(1980,)|var|bool
var_6306 = relay.var("var_6306", dtype = "float32", shape = (1456,))#candidate|6306|(1456,)|var|float32
output = func_6304(var_6305,var_6306,)
func_6307 = relay.Function([var_6305,var_6306,], output)
mutated_mod['func_6307'] = func_6307
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4241_call = mod.get_global_var('func_4241')
func_4242_call = mutated_mod.get_global_var('func_4242')
call_6309 = relay.TupleGetItem(func_4241_call(), 1)
call_6310 = relay.TupleGetItem(func_4242_call(), 1)
func_4542_call = mod.get_global_var('func_4542')
func_4543_call = mutated_mod.get_global_var('func_4543')
call_6313 = relay.TupleGetItem(func_4542_call(), 0)
call_6314 = relay.TupleGetItem(func_4543_call(), 0)
uop_6342 = relay.sin(call_6313.astype('float64')) # shape=(14, 9, 6)
uop_6344 = relay.sin(call_6314.astype('float64')) # shape=(14, 9, 6)
output = relay.Tuple([call_6309,uop_6342,])
output2 = relay.Tuple([call_6310,uop_6344,])
func_6345 = relay.Function([], output)
mod['func_6345'] = func_6345
mod = relay.transform.InferType()(mod)
output = func_6345()
func_6346 = relay.Function([], output)
mutated_mod['func_6346'] = func_6346
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6182_call = mod.get_global_var('func_6182')
func_6183_call = mutated_mod.get_global_var('func_6183')
call_6419 = relay.TupleGetItem(func_6182_call(), 2)
call_6420 = relay.TupleGetItem(func_6183_call(), 2)
output = relay.Tuple([call_6419,])
output2 = relay.Tuple([call_6420,])
func_6424 = relay.Function([], output)
mod['func_6424'] = func_6424
mod = relay.transform.InferType()(mod)
output = func_6424()
func_6425 = relay.Function([], output)
mutated_mod['func_6425'] = func_6425
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4858_call = mod.get_global_var('func_4858')
func_4860_call = mutated_mod.get_global_var('func_4860')
call_6479 = func_4858_call()
call_6480 = func_4858_call()
output = relay.Tuple([call_6479,])
output2 = relay.Tuple([call_6480,])
func_6515 = relay.Function([], output)
mod['func_6515'] = func_6515
mod = relay.transform.InferType()(mod)
mutated_mod['func_6515'] = func_6515
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6515_call = mutated_mod.get_global_var('func_6515')
call_6516 = func_6515_call()
output = call_6516
func_6517 = relay.Function([], output)
mutated_mod['func_6517'] = func_6517
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5003_call = mod.get_global_var('func_5003')
func_5005_call = mutated_mod.get_global_var('func_5005')
call_6538 = relay.TupleGetItem(func_5003_call(), 2)
call_6539 = relay.TupleGetItem(func_5005_call(), 2)
func_5343_call = mod.get_global_var('func_5343')
func_5346_call = mutated_mod.get_global_var('func_5346')
var_6543 = relay.var("var_6543", dtype = "float32", shape = (1456,))#candidate|6543|(1456,)|var|float32
call_6542 = relay.TupleGetItem(func_5343_call(relay.reshape(var_6543.astype('float32'), [14, 8, 13])), 1)
call_6544 = relay.TupleGetItem(func_5346_call(relay.reshape(var_6543.astype('float32'), [14, 8, 13])), 1)
func_2269_call = mod.get_global_var('func_2269')
func_2272_call = mutated_mod.get_global_var('func_2272')
var_6558 = relay.var("var_6558", dtype = "float32", shape = (1080,))#candidate|6558|(1080,)|var|float32
call_6557 = relay.TupleGetItem(func_2269_call(relay.reshape(var_6558.astype('float32'), [15, 8, 9])), 0)
call_6559 = relay.TupleGetItem(func_2272_call(relay.reshape(var_6558.astype('float32'), [15, 8, 9])), 0)
func_3802_call = mod.get_global_var('func_3802')
func_3804_call = mutated_mod.get_global_var('func_3804')
call_6570 = relay.TupleGetItem(func_3802_call(), 0)
call_6571 = relay.TupleGetItem(func_3804_call(), 0)
output = relay.Tuple([call_6538,call_6542,var_6543,call_6557,var_6558,call_6570,])
output2 = relay.Tuple([call_6539,call_6544,var_6543,call_6559,var_6558,call_6571,])
func_6579 = relay.Function([var_6543,var_6558,], output)
mod['func_6579'] = func_6579
mod = relay.transform.InferType()(mod)
mutated_mod['func_6579'] = func_6579
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6579_call = mutated_mod.get_global_var('func_6579')
var_6581 = relay.var("var_6581", dtype = "float32", shape = (1456,))#candidate|6581|(1456,)|var|float32
var_6582 = relay.var("var_6582", dtype = "float32", shape = (1080,))#candidate|6582|(1080,)|var|float32
call_6580 = func_6579_call(var_6581,var_6582,)
output = call_6580
func_6583 = relay.Function([var_6581,var_6582,], output)
mutated_mod['func_6583'] = func_6583
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6345_call = mod.get_global_var('func_6345')
func_6346_call = mutated_mod.get_global_var('func_6346')
call_6616 = relay.TupleGetItem(func_6345_call(), 1)
call_6617 = relay.TupleGetItem(func_6346_call(), 1)
func_4203_call = mod.get_global_var('func_4203')
func_4206_call = mutated_mod.get_global_var('func_4206')
var_6619 = relay.var("var_6619", dtype = "float32", shape = (2, 616))#candidate|6619|(2, 616)|var|float32
call_6618 = func_4203_call(relay.reshape(var_6619.astype('float32'), [14, 11, 8]))
call_6620 = func_4203_call(relay.reshape(var_6619.astype('float32'), [14, 11, 8]))
output = relay.Tuple([call_6616,call_6618,var_6619,])
output2 = relay.Tuple([call_6617,call_6620,var_6619,])
func_6642 = relay.Function([var_6619,], output)
mod['func_6642'] = func_6642
mod = relay.transform.InferType()(mod)
mutated_mod['func_6642'] = func_6642
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6643 = relay.var("var_6643", dtype = "float32", shape = (2, 616))#candidate|6643|(2, 616)|var|float32
func_6642_call = mutated_mod.get_global_var('func_6642')
call_6644 = func_6642_call(var_6643)
output = call_6644
func_6645 = relay.Function([var_6643], output)
mutated_mod['func_6645'] = func_6645
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5885_call = mod.get_global_var('func_5885')
func_5887_call = mutated_mod.get_global_var('func_5887')
call_6684 = relay.TupleGetItem(func_5885_call(), 0)
call_6685 = relay.TupleGetItem(func_5887_call(), 0)
output = relay.Tuple([call_6684,])
output2 = relay.Tuple([call_6685,])
func_6689 = relay.Function([], output)
mod['func_6689'] = func_6689
mod = relay.transform.InferType()(mod)
mutated_mod['func_6689'] = func_6689
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6689_call = mutated_mod.get_global_var('func_6689')
call_6690 = func_6689_call()
output = call_6690
func_6691 = relay.Function([], output)
mutated_mod['func_6691'] = func_6691
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4701_call = mod.get_global_var('func_4701')
func_4703_call = mutated_mod.get_global_var('func_4703')
call_6740 = relay.TupleGetItem(func_4701_call(), 0)
call_6741 = relay.TupleGetItem(func_4703_call(), 0)
output = call_6740
output2 = call_6741
func_6761 = relay.Function([], output)
mod['func_6761'] = func_6761
mod = relay.transform.InferType()(mod)
output = func_6761()
func_6762 = relay.Function([], output)
mutated_mod['func_6762'] = func_6762
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5049_call = mod.get_global_var('func_5049')
func_5050_call = mutated_mod.get_global_var('func_5050')
call_6797 = relay.TupleGetItem(func_5049_call(), 0)
call_6798 = relay.TupleGetItem(func_5050_call(), 0)
uop_6823 = relay.acos(call_6797.astype('float32')) # shape=(14, 9, 6)
uop_6825 = relay.acos(call_6798.astype('float32')) # shape=(14, 9, 6)
output = relay.Tuple([uop_6823,])
output2 = relay.Tuple([uop_6825,])
func_6841 = relay.Function([], output)
mod['func_6841'] = func_6841
mod = relay.transform.InferType()(mod)
output = func_6841()
func_6842 = relay.Function([], output)
mutated_mod['func_6842'] = func_6842
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6948 = relay.var("var_6948", dtype = "int64", shape = (6, 4, 7))#candidate|6948|(6, 4, 7)|var|int64
var_6949 = relay.var("var_6949", dtype = "int64", shape = (6, 4, 7))#candidate|6949|(6, 4, 7)|var|int64
bop_6950 = relay.subtract(var_6948.astype('int64'), relay.reshape(var_6949.astype('int64'), relay.shape_of(var_6948))) # shape=(6, 4, 7)
output = relay.Tuple([bop_6950,])
output2 = relay.Tuple([bop_6950,])
func_6956 = relay.Function([var_6948,var_6949,], output)
mod['func_6956'] = func_6956
mod = relay.transform.InferType()(mod)
var_6957 = relay.var("var_6957", dtype = "int64", shape = (6, 4, 7))#candidate|6957|(6, 4, 7)|var|int64
var_6958 = relay.var("var_6958", dtype = "int64", shape = (6, 4, 7))#candidate|6958|(6, 4, 7)|var|int64
output = func_6956(var_6957,var_6958,)
func_6959 = relay.Function([var_6957,var_6958,], output)
mutated_mod['func_6959'] = func_6959
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6961 = relay.var("var_6961", dtype = "float64", shape = (7, 5, 7))#candidate|6961|(7, 5, 7)|var|float64
var_6962 = relay.var("var_6962", dtype = "float64", shape = (7, 5, 7))#candidate|6962|(7, 5, 7)|var|float64
bop_6963 = relay.divide(var_6961.astype('float64'), relay.reshape(var_6962.astype('float64'), relay.shape_of(var_6961))) # shape=(7, 5, 7)
output = bop_6963
output2 = bop_6963
func_6968 = relay.Function([var_6961,var_6962,], output)
mod['func_6968'] = func_6968
mod = relay.transform.InferType()(mod)
mutated_mod['func_6968'] = func_6968
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6968_call = mutated_mod.get_global_var('func_6968')
var_6970 = relay.var("var_6970", dtype = "float64", shape = (7, 5, 7))#candidate|6970|(7, 5, 7)|var|float64
var_6971 = relay.var("var_6971", dtype = "float64", shape = (7, 5, 7))#candidate|6971|(7, 5, 7)|var|float64
call_6969 = func_6968_call(var_6970,var_6971,)
output = call_6969
func_6972 = relay.Function([var_6970,var_6971,], output)
mutated_mod['func_6972'] = func_6972
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6980 = relay.var("var_6980", dtype = "float64", shape = (8, 10, 14))#candidate|6980|(8, 10, 14)|var|float64
uop_6981 = relay.rsqrt(var_6980.astype('float64')) # shape=(8, 10, 14)
func_4398_call = mod.get_global_var('func_4398')
func_4399_call = mutated_mod.get_global_var('func_4399')
call_7016 = relay.TupleGetItem(func_4398_call(), 0)
call_7017 = relay.TupleGetItem(func_4399_call(), 0)
var_7019 = relay.var("var_7019", dtype = "float32", shape = (14, 9, 6))#candidate|7019|(14, 9, 6)|var|float32
bop_7020 = relay.multiply(call_7016.astype('int32'), relay.reshape(var_7019.astype('int32'), relay.shape_of(call_7016))) # shape=(14, 9, 6)
bop_7023 = relay.multiply(call_7017.astype('int32'), relay.reshape(var_7019.astype('int32'), relay.shape_of(call_7017))) # shape=(14, 9, 6)
output = relay.Tuple([uop_6981,bop_7020,])
output2 = relay.Tuple([uop_6981,bop_7023,])
func_7024 = relay.Function([var_6980,var_7019,], output)
mod['func_7024'] = func_7024
mod = relay.transform.InferType()(mod)
var_7025 = relay.var("var_7025", dtype = "float64", shape = (8, 10, 14))#candidate|7025|(8, 10, 14)|var|float64
var_7026 = relay.var("var_7026", dtype = "float32", shape = (14, 9, 6))#candidate|7026|(14, 9, 6)|var|float32
output = func_7024(var_7025,var_7026,)
func_7027 = relay.Function([var_7025,var_7026,], output)
mutated_mod['func_7027'] = func_7027
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4241_call = mod.get_global_var('func_4241')
func_4242_call = mutated_mod.get_global_var('func_4242')
call_7090 = relay.TupleGetItem(func_4241_call(), 1)
call_7091 = relay.TupleGetItem(func_4242_call(), 1)
func_6761_call = mod.get_global_var('func_6761')
func_6762_call = mutated_mod.get_global_var('func_6762')
call_7092 = func_6761_call()
call_7093 = func_6761_call()
output = relay.Tuple([call_7090,call_7092,])
output2 = relay.Tuple([call_7091,call_7093,])
func_7095 = relay.Function([], output)
mod['func_7095'] = func_7095
mod = relay.transform.InferType()(mod)
output = func_7095()
func_7096 = relay.Function([], output)
mutated_mod['func_7096'] = func_7096
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5632_call = mod.get_global_var('func_5632')
func_5633_call = mutated_mod.get_global_var('func_5633')
call_7121 = func_5632_call()
call_7122 = func_5632_call()
output = relay.Tuple([call_7121,])
output2 = relay.Tuple([call_7122,])
func_7150 = relay.Function([], output)
mod['func_7150'] = func_7150
mod = relay.transform.InferType()(mod)
output = func_7150()
func_7151 = relay.Function([], output)
mutated_mod['func_7151'] = func_7151
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7179 = relay.var("var_7179", dtype = "float32", shape = (6, 14, 2))#candidate|7179|(6, 14, 2)|var|float32
uop_7180 = relay.erf(var_7179.astype('float32')) # shape=(6, 14, 2)
func_4061_call = mod.get_global_var('func_4061')
func_4064_call = mutated_mod.get_global_var('func_4064')
var_7186 = relay.var("var_7186", dtype = "float32", shape = (756,))#candidate|7186|(756,)|var|float32
const_7187 = relay.const([True,True,True,True,True,False,True,False,True,False,False,False,True,True,True,False,True,False,False,False,False,True,False,True,False,True,True,True,True,True,True,False,True,False,True,False,True,False,False,False,False,True,False,False,False,True,False,True,True,False,True,False,True,True,True,False,False,False,True,True,True,True,True,False,True,True,False,False,True,True,False,False,False,False,False,False,False,False,True,True,False,False,True,False,True,False,False,True,False,True,False,False,False,True,False,False,False,True,False,False,False,True,False,False,True,False,False,True,False,True,True,False,True,False,False,False,True,False,True,True,False,True,True,False,False,False,False,True,True,True,True,True,False,True,True,True,True,True,True,True,False,False,True,True,False,False,True,True,False,False,True,False,True,False,True,True,False,True,False,True,False,True,False,False,False,True,False,True,False,True,False,False,True,False,True,True,False,False,True,False,False,False,True,True,False,False,True,True,True,True,False,False,True,True,False,True,False,False,True,True,True,True,True,False,True,True,False,True,True,True,False,False,True,True,True,True,True,False,False,False,False,True,False,True,False,True,False,False,True,True,True,True,True,True,True,False,False,True,False,True,False,False,True,True,True,True,True,False,True,True,False,True,False,True,False,False,False,True,True,True,False,False,False,True,True,False,False,True,True,False,True,False,False,False,True,True,True,False,True,True,False,True,False,False,False,True,True,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,True,True,True,False,False,False,True,False,True,False,False,False,True,True,False,True,True,False,True,False,True,True,False,True,True,True,True,True,False,True,True,True,True,False,True,True,False,True,True,False,True,True,False,False,True,False,True,False,True,False,False,False,False,False,True,True,False,True,True,False,False,False,True,True,True,False,False,True,True,True,True,False,True,True,False,False,False,True,False,True,False,True,True,False,True,False,True,True,True,False,True,False,True,False,True,False,True,False,True,False,True,True,True,False,False,True,False,False,True,True,True,True,False,False,True,True,True,False,True,False,True,False,False,False,True,False,False,False,False,True,False,True,False,True,False,True,True,False,True,False,True,True,True,True,True,False,True,False,False,False,True,True,False,True,True,True,True,True,True,True,True,False,True,True,True,True,False,False,True,False,False,True,True,True,False,False,True,True,True,False,True,False,True,False,True,True,True,True,False,True,False,True,True,True,True,False,False,True,True,False,True,True,True,False,True,True,True,False,True,False,False,False,False,False,False,True,True,False,False,True,True,True,True,False,False,False,False,True,True,True,True,True,True,False,True,False,True,False,False,False,False,True,True,False,True,True,False,False,True,False,True,False,True,False,False,False,False,True,True,False,False,False,True,True,False,False,True,True,True,False,False,True,True,True,False,False,False,False,False,False,False,True,False,False,False,True,False,False,False,True,False,False,True,True,False,True,False,True,False,True,True,False,False,False,True,False,False,False,False,False,False,True,False,False,True,False,True,True,False,True,False,True,False,True,False,False,False,False,True,False,True,True,True,False,True,False,False,False,False,True,False,False,False,False,True,True,False,False,False,True,False,False,False,False,True,False,False,True,True,True,True,False,False,False,False,False,True,True,False,True,False,False,False,False,True,True,True,True,True,True,False,True,True,False,True,False,True,True,True,False,True,False,False,True,True,True,True,False,False,True,True,False,False,True,False,True,False,True,False,False,False,True,True,True,True,True,True,False,False,False,False,True,False,True,True,True,False,False,True,False,False,True,False,False,False,False,True,True,True,True,True,True,False,False,False,False,True,True,False,False,True,True,True,True,False,False,True,False,True,False,False,True,True,False,True,False,False,False,True,True,True,False,False,False,False,False,False,False,True,False,False,False,True,True,True,True,False,False,True,True,True,True,False,False,True,True,False,True,True,True,False,False,True,False,False,False,False,False,False,True,True,False,True,False,True,True,False,True,True,True,False,False,True,False,True,False,True,True,False,False,True,False,True,False,True,True,False,True,False,False,True,True,False,False,True,False,True,True,True,True,True,False,True,False,False,False,False,False,False,False,False,True,True,True,True,False,True,False,True,True,False,False,False,True,True,True,True,False,True,False,True,False,False,True,False,True,True,False,True,True,True,True,False,False,True,False,False,False,False,True,True,False,False,True,True,True,False,False,True,True,True,True,True,True,False,True,False,True,False,True,True,True,True,True,True,False,True,True,False,True,False,True,False,False,False,True,True,False,False,True,False,True,False,True,False,False,True,True,True,True,False,False,False,True,False,True,True,True,False,True,True,False,False,True,True,False,False,False,True,False,True,True,True,True,False,False,True,True,True,True,False,True,True,False,True,True,True,False,True,True,False,False,False,False,True,True,True,True,True,False,False,True,True,True,False,True,True,False,True,False,True,True,False,False,False,True,False,True,True,True,True,True,True,True,False,False,False,True,True,True,True,True,False,False,True,True,True,False,True,False,True,False,False,True,False,False,False,False,True,True,True,False,True,False,True,True,False,True,False,False,True,True,True,True,True,False,False,False,True,True,True,False,True,True,True,False,True,True,False,False,False,False,True,True,False,False,False,True,False,False,True,True,True,False,False,False,True,True,True,False,False,False,False,False,True,True,False,False,False,False,False,False,False,True,False,True,False,False,False,False,True,True,True,False,True,True,True,False,False,False,False,True,False,False,True,True,True,True,True,True,True,True,False,False,True,False,True,True,False,True,True,True,False,False,False,True,True,True,False,False,True,False,True,True,True,False,False,False,True,True,False,False,False,False,False,True,False,True,False,False,False,True,False,False,True,False,False,True,True,False,True,False,False,False,True,True,False,True,False,True,False,False,True,False,False,False,False,False,True,False,False,False,False,False,False,True,False,False,False,True,False,True,True,True,True,False,False,True,True,False,False,True,False,False,False,False,False,False,False,True,False,True,True,False,True,False,False,False,False,False,True,True,False,True,False,True,True,False,True,True,True,True,False,True,True,False,False,True,False,False,True,True,True,False,True,True,False,True,True,True,False,False,False,False,True,False,True,True,False,False,False,True,False,False,True,True,True,True,True,True,True,False,False,True,False,False,False,True,True,True,False,True,True,False,True,True,False,True,False,False,True,False,False,True,False,True,True,True,False,False,True,True,False,True,False,False,True,False,True,True,True,True,False,True,True,False,False,True,True,False,False,False,False,False,False,False,True,True,False,True,True,True,False,True,False,True,True,False,True,True,True,True,False,True,False,False,True,False,True,False,False,True,True,False,True,True,False,False,False,False,True,True,True,False,False,False,True,True,False,False,False,True,True,True,False,True,True,False,True,False,False,True,False,True,True,True,False,False,False,False,False,True,True,False,True,True,False,False,True,False,True,True,True,False,False,True,False,True,True,True,False,False,True,False,True,False,True,False,False,True,False,True,True,False,True,False,True,True,True,False,True,False,False,False,False,False,True,False,False,True,False,False,True,True,False,False,True,True,False,False,True,True,True,False,True,False,False,False,True,True,True,False,True,True,False,False,True,True,False,True,False,False,True,True,True,True,False,True,True,False,True,False,True,False,False,False,False,False,True,True,False,False,True,True,True,True,True,False,False,False,False,True,False,True,False,False,True,False,True,False,True,False,False,False,False,False,True,False,False,False,True,False,False,False,False,True,True,True,True,True,True,True,False,False,True,True,False,False,True,True,False,False,True,False,True,True,False,False,True,False,False,False,True,False,False,True,True,True,False,False,False,False,False,True,False,True,False,False,True,True,True,True,False,False,True,True,True,True,True,False,True,True,False,False,True,False,True,False,True,False,False,True,False,False,False,False,True,False,False,False,False,True,True,False,True,False,True,False,True,False,False,True,True,False,True,False,False,True,False,True,True,False,False,True,True,True,True,False,True,True,True,True,False,False,True,True,True,False,True,False,False,True,True,True,True,True,True,True,False,True,False,True,False,False,False,True,True,True,True,True,False,False,False,False,True,False,True,False,False,False,False,True,True,False,False,False,True,False,True,True,True,True,False,True,True,False,False,True,True,False,False,True,False,False,True,True,False,False,True,True,False,False,False,True,False,False,True,True,False,False,False,False,True,False,True,False,False,False,True,True,False,True,False,False,False,True,False,False,True,True,True,True,True,True,False,True,False,True,False,False,True,False,False,False,False,False,False,False,False,False,True,False,True,True,False,True,False,False,False,True,False,True,False,True,True,False,True,True,True,True,True,False,False,False,False,False,False,True,True,False,True,False,False,False,False,False,False,False,True,False,False,True,True,False,False,False,True,True,True,False,True,True,True,True,True,True,True,True,False,False,True,True,True,True,False,True,True,False,True,False,False,True,True,True,False,False,False,True,True,True,True,False,False,False,True,True,False,True,False,False,True,True,False,False,False,False,True,False,False,True,False,False,False,False,True,False,False,True,True,True,True,True,False,True,True,True,True,True,False,True,False,False,True,False,False,True,False,False,True,False,True,False,False,True,False,True,False,False,True,True,True,False,False,True,True,False,True,False,True,True,False,True,True,True,True,False,False,True,False,False,True,True,False,True,False,False,True,False,False,False,False,True,False,False,True,True,False,False,False,False,True,False,True,True,True,True,True,True,False,True,True,False,False,True,True,False], dtype = "bool")#candidate|7187|(1980,)|const|bool
call_7185 = relay.TupleGetItem(func_4061_call(relay.reshape(var_7186.astype('float32'), [14, 9, 6]), relay.reshape(const_7187.astype('bool'), [1980,]), ), 1)
call_7188 = relay.TupleGetItem(func_4064_call(relay.reshape(var_7186.astype('float32'), [14, 9, 6]), relay.reshape(const_7187.astype('bool'), [1980,]), ), 1)
bop_7190 = relay.bitwise_or(var_7179.astype('int16'), relay.reshape(uop_7180.astype('int16'), relay.shape_of(var_7179))) # shape=(6, 14, 2)
bop_7200 = relay.less_equal(uop_7180.astype('bool'), relay.reshape(bop_7190.astype('bool'), relay.shape_of(uop_7180))) # shape=(6, 14, 2)
func_5311_call = mod.get_global_var('func_5311')
func_5314_call = mutated_mod.get_global_var('func_5314')
var_7205 = relay.var("var_7205", dtype = "float64", shape = (240,))#candidate|7205|(240,)|var|float64
call_7204 = relay.TupleGetItem(func_5311_call(relay.reshape(var_7205.astype('float64'), [12, 2, 10])), 0)
call_7206 = relay.TupleGetItem(func_5314_call(relay.reshape(var_7205.astype('float64'), [12, 2, 10])), 0)
output = relay.Tuple([call_7185,var_7186,const_7187,bop_7200,call_7204,var_7205,])
output2 = relay.Tuple([call_7188,var_7186,const_7187,bop_7200,call_7206,var_7205,])
func_7207 = relay.Function([var_7179,var_7186,var_7205,], output)
mod['func_7207'] = func_7207
mod = relay.transform.InferType()(mod)
var_7208 = relay.var("var_7208", dtype = "float32", shape = (6, 14, 2))#candidate|7208|(6, 14, 2)|var|float32
var_7209 = relay.var("var_7209", dtype = "float32", shape = (756,))#candidate|7209|(756,)|var|float32
var_7210 = relay.var("var_7210", dtype = "float64", shape = (240,))#candidate|7210|(240,)|var|float64
output = func_7207(var_7208,var_7209,var_7210,)
func_7211 = relay.Function([var_7208,var_7209,var_7210,], output)
mutated_mod['func_7211'] = func_7211
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5478_call = mod.get_global_var('func_5478')
func_5479_call = mutated_mod.get_global_var('func_5479')
call_7227 = relay.TupleGetItem(func_5478_call(), 0)
call_7228 = relay.TupleGetItem(func_5479_call(), 0)
uop_7232 = relay.sigmoid(call_7227.astype('float64')) # shape=(14, 9, 6)
uop_7234 = relay.sigmoid(call_7228.astype('float64')) # shape=(14, 9, 6)
output = relay.Tuple([uop_7232,])
output2 = relay.Tuple([uop_7234,])
func_7240 = relay.Function([], output)
mod['func_7240'] = func_7240
mod = relay.transform.InferType()(mod)
output = func_7240()
func_7241 = relay.Function([], output)
mutated_mod['func_7241'] = func_7241
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3802_call = mod.get_global_var('func_3802')
func_3804_call = mutated_mod.get_global_var('func_3804')
call_7285 = relay.TupleGetItem(func_3802_call(), 0)
call_7286 = relay.TupleGetItem(func_3804_call(), 0)
uop_7291 = relay.exp(call_7285.astype('float64')) # shape=(14, 9, 6)
uop_7293 = relay.exp(call_7286.astype('float64')) # shape=(14, 9, 6)
output = relay.Tuple([uop_7291,])
output2 = relay.Tuple([uop_7293,])
func_7296 = relay.Function([], output)
mod['func_7296'] = func_7296
mod = relay.transform.InferType()(mod)
mutated_mod['func_7296'] = func_7296
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7296_call = mutated_mod.get_global_var('func_7296')
call_7297 = func_7296_call()
output = call_7297
func_7298 = relay.Function([], output)
mutated_mod['func_7298'] = func_7298
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7308 = relay.var("var_7308", dtype = "float32", shape = (3, 7, 7))#candidate|7308|(3, 7, 7)|var|float32
uop_7309 = relay.asinh(var_7308.astype('float32')) # shape=(3, 7, 7)
output = relay.Tuple([uop_7309,])
output2 = relay.Tuple([uop_7309,])
func_7318 = relay.Function([var_7308,], output)
mod['func_7318'] = func_7318
mod = relay.transform.InferType()(mod)
var_7319 = relay.var("var_7319", dtype = "float32", shape = (3, 7, 7))#candidate|7319|(3, 7, 7)|var|float32
output = func_7318(var_7319)
func_7320 = relay.Function([var_7319], output)
mutated_mod['func_7320'] = func_7320
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5885_call = mod.get_global_var('func_5885')
func_5887_call = mutated_mod.get_global_var('func_5887')
call_7325 = relay.TupleGetItem(func_5885_call(), 0)
call_7326 = relay.TupleGetItem(func_5887_call(), 0)
uop_7327 = relay.log10(call_7325.astype('float64')) # shape=(14, 9, 6)
uop_7329 = relay.log10(call_7326.astype('float64')) # shape=(14, 9, 6)
func_1553_call = mod.get_global_var('func_1553')
func_1555_call = mutated_mod.get_global_var('func_1555')
const_7333 = relay.const([[-6,7,8,-5,-1,8,-2,7,2,-7,-7,8,3,-2,5,-3,2,1,5,-6,-2,-6,-5,-4,-10,-7,3,9,-5,-8,4,-1,3,-6,-8,3,-7,4,4,1,10,-3,3,-7,-2,9,10,2,-2,10,-3,7,3,-3,1,3,4,-4,-5,-5,10,2,-2,3,-7,1,7,-9,1,-9,10,6,5,10,5,-8,-9,-6,7,6,-2,3,7,2,-5,-2,5,8,-2,-2,4,-1,-10,-6,6,-10,-9,10,6,5,4,-8,-9,-9,-7,-5,10,-5,-5,-9,1,9,-4,-7,2,-6,3,-7,2,-3,-8,-9,-6,-9,3,2,-7,7,4,4,8,-4,3,3,-7,2,7,-4,-8,-6,10,9,2,9,-10,2,10,-8,7,-8,-10,-2,4,1,-10,4],[-6,-7,7,-6,8,4,4,-3,-3,-9,-1,-1,-8,8,-9,8,-5,6,1,-10,10,9,6,-6,10,4,-6,-10,-7,-2,3,4,5,2,3,-4,-6,6,-2,-10,8,8,9,8,-8,-2,2,-3,-7,-2,-8,1,9,3,2,8,9,5,5,6,6,6,-4,-5,-5,9,-3,-5,-2,6,6,-3,9,5,-3,-9,8,7,6,3,10,3,4,8,10,1,9,1,4,-3,-6,6,-10,6,-8,9,10,-3,-2,2,8,-6,-7,-4,4,8,4,3,-6,1,-5,1,-2,2,9,6,9,-2,-10,9,-8,3,10,5,5,1,-6,-7,-9,2,5,5,1,-2,6,6,-8,-7,5,6,7,1,-10,-4,7,8,6,-10,1,-10,3,2,-7,10,10,-3],[3,-2,2,3,4,3,-3,8,7,10,8,-3,-10,8,-9,8,-4,-5,8,6,-9,3,4,-5,-3,-10,8,5,-8,-7,3,1,8,2,5,-8,-10,6,6,4,-6,-2,10,2,8,5,7,-9,-3,10,10,10,-3,-4,8,10,-6,8,-8,4,-2,-9,6,-5,-10,6,-7,2,5,-8,-5,6,-9,-7,-7,-4,3,-9,3,9,2,-5,-4,-6,-2,1,-3,9,3,10,9,8,-9,-3,2,-6,-9,-1,8,3,4,-7,3,10,4,-4,5,-6,-9,-9,-3,5,-5,-5,6,3,2,-10,8,10,1,6,8,-2,-3,7,-5,-7,1,-3,10,10,6,8,9,5,-4,5,4,-8,-8,2,9,4,-1,-8,3,-4,5,4,-10,3,-9,-3,-8,10],[5,-1,-3,-6,-4,-7,4,7,-3,-5,-9,6,-9,-2,9,-6,6,-3,-4,3,-5,4,-10,-1,3,8,6,-9,3,5,3,-8,-9,-6,-2,-3,-9,-8,-10,-4,9,-3,5,2,-5,-10,6,-7,-1,-10,-4,-1,1,-2,10,-2,-9,4,10,10,10,-4,-9,5,-4,4,9,-10,5,-9,-9,4,9,10,3,-3,-1,3,-7,-2,3,-10,-9,3,2,1,-7,7,-2,-5,8,-9,-6,9,-1,6,-6,8,-5,-9,5,8,4,7,-4,-4,2,-1,6,-4,4,-2,-6,-6,-3,8,7,-1,-3,9,-5,-2,-6,7,-7,-2,-1,-9,-7,8,2,-10,-3,-9,1,6,1,-3,2,-3,-3,8,-9,2,4,8,7,-2,-8,1,-1,5,6,2,-8,-5],[-10,-4,1,-7,-8,-10,2,7,5,9,-4,7,-2,6,-4,2,7,6,-4,5,-9,-6,9,1,1,9,6,-3,-4,10,-3,5,10,10,-4,5,9,4,-5,9,9,-1,-5,5,5,-9,-10,10,6,4,-4,1,10,-9,-2,-3,10,6,-8,5,6,6,10,6,4,4,-8,-1,-4,-5,3,-9,-2,6,-6,5,-7,-10,5,-3,-5,-8,5,1,-2,-6,-4,5,10,6,-4,-9,-2,-8,-2,-9,-7,10,-8,1,-9,2,4,1,-1,-9,10,4,5,-10,-2,-6,5,2,8,3,2,3,5,9,3,-10,6,-6,7,-9,-4,-1,10,-2,7,-6,-1,5,4,-1,-2,1,-7,8,-2,3,4,5,-7,4,4,-7,10,-2,-5,-5,-6,-6,3,6]], dtype = "int8")#candidate|7333|(5, 156)|const|int8
call_7332 = relay.TupleGetItem(func_1553_call(relay.reshape(const_7333.astype('int8'), [4, 13, 15])), 0)
call_7334 = relay.TupleGetItem(func_1555_call(relay.reshape(const_7333.astype('int8'), [4, 13, 15])), 0)
uop_7336 = relay.sin(call_7332.astype('float64')) # shape=(4, 13, 15)
uop_7338 = relay.sin(call_7334.astype('float64')) # shape=(4, 13, 15)
output = relay.Tuple([uop_7327,const_7333,uop_7336,])
output2 = relay.Tuple([uop_7329,const_7333,uop_7338,])
func_7343 = relay.Function([], output)
mod['func_7343'] = func_7343
mod = relay.transform.InferType()(mod)
mutated_mod['func_7343'] = func_7343
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7343_call = mutated_mod.get_global_var('func_7343')
call_7344 = func_7343_call()
output = call_7344
func_7345 = relay.Function([], output)
mutated_mod['func_7345'] = func_7345
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5591_call = mod.get_global_var('func_5591')
func_5593_call = mutated_mod.get_global_var('func_5593')
call_7394 = func_5591_call()
call_7395 = func_5591_call()
func_192_call = mod.get_global_var('func_192')
func_195_call = mutated_mod.get_global_var('func_195')
const_7404 = relay.const([[True,True,True,False,False,False,False,True,True,False,True,True,False,False,True,True,False,False,False,True,False,True,False,False,True,True,True,False,True,False,True,True,True,False,True,False,True,True,True,False,True,False,True,True,False,False,False,False,False,False,False,True,False,False,True,True,False,False,True,True,False,True,False,True,True,True,True,False,False,False,False,True,False,True,True,False,True,True,True,False,False,True,True,False,True,False,True,True,False,True,True,False,False,True,True,True,True,True,False,True,True,False,True,False,False,False,False,True,True,True,True,True,False,False,True,False,False,True,True,False,False,False,False,False,False,False,True,True,True,True,False,False,False,True,False,False,True,True,True,True,False,True,False,True,True,False,True,False,True,False,False,True,True,True,True,True,True,False,False,False,False,False,False,False,False,True,False,True,False,True,False,False,False,True,True,False,True,False,False,False,True,False,True,False,True,False,True,False,False,True,False,False,True,True,False,True,False,False,True,False,False,True,False,False,False,False,False,True,False,False,True,True,True,False,True,False,False,False,True,True],[True,True,True,True,False,False,False,False,False,True,False,False,True,True,True,True,True,True,True,True,False,False,True,True,True,False,True,True,True,False,False,False,False,False,True,False,False,False,True,False,True,True,True,False,False,False,False,True,True,True,True,True,True,False,False,False,False,False,False,True,False,False,False,False,False,True,True,False,True,False,True,True,True,False,True,False,False,True,True,True,False,False,True,False,False,True,False,True,True,False,False,False,True,False,False,True,False,True,False,True,True,True,False,True,True,False,True,True,True,False,False,False,True,True,False,True,True,False,False,False,True,True,False,False,True,True,True,True,False,True,True,False,False,True,True,True,True,False,False,True,False,True,True,True,False,True,True,True,True,True,False,False,False,False,False,False,True,False,True,False,True,False,False,False,False,True,True,True,True,False,False,True,True,True,True,True,False,False,True,False,True,True,False,False,True,True,False,True,True,True,True,False,False,True,False,False,False,False,True,True,False,False,False,True,True,True,False,False,True,True,False,True,False,False,True,False,True,True,True,False],[False,False,True,False,True,True,False,True,True,False,False,True,False,False,False,True,False,True,True,True,False,True,False,True,False,True,True,True,False,False,False,True,False,True,True,True,False,False,False,False,False,False,True,False,False,False,True,False,True,True,False,True,False,False,False,False,False,True,False,False,True,False,True,True,True,True,False,True,True,False,True,True,False,True,True,True,True,False,True,False,True,True,True,False,False,False,False,False,True,False,False,True,False,False,False,True,True,True,True,False,True,False,True,False,True,False,True,False,False,False,False,False,False,False,False,False,False,False,False,True,True,False,False,True,False,True,True,True,False,False,True,True,False,False,True,False,False,False,False,True,True,True,True,True,True,True,True,True,True,True,False,False,True,True,False,False,False,True,True,False,True,True,True,True,True,True,True,False,True,False,True,False,True,False,True,False,True,False,True,False,True,True,True,True,False,True,True,False,False,False,False,True,True,False,False,True,True,False,True,False,False,False,True,True,False,False,True,True,True,False,True,False,True,False,True,False,True,False,False,True],[True,True,False,False,True,True,True,False,True,False,False,True,False,True,False,False,False,True,True,True,True,True,True,False,True,True,False,True,True,True,False,False,False,True,True,True,False,False,True,True,True,True,False,True,True,False,False,True,True,True,False,False,False,True,False,False,False,True,True,False,False,True,False,False,False,True,True,False,False,False,True,True,True,True,False,False,True,False,True,False,False,True,False,False,True,True,False,True,False,True,True,False,True,False,False,True,True,True,False,True,True,True,False,False,True,True,True,False,True,False,True,True,False,True,False,True,False,False,False,False,False,False,False,True,False,False,False,True,True,False,True,False,False,True,True,True,False,False,True,False,False,False,True,False,False,True,True,False,False,False,True,False,False,True,True,False,False,True,True,True,False,False,False,False,False,True,True,False,True,False,False,True,True,False,False,True,True,True,True,True,True,False,True,True,False,False,True,False,False,True,True,False,True,True,False,True,False,True,False,True,True,False,True,False,False,True,True,False,False,True,True,False,True,True,True,True,True,True,True,True],[False,True,True,True,False,True,True,True,False,True,False,False,True,True,False,False,False,False,False,True,True,True,True,False,False,False,False,False,True,True,True,True,False,True,True,True,False,False,False,True,True,False,True,False,False,True,False,False,True,False,True,False,False,False,True,False,True,True,False,False,False,False,False,True,True,True,False,True,True,False,False,False,False,True,False,False,True,True,True,False,True,False,True,True,True,False,False,False,True,False,False,True,False,False,False,True,True,False,True,False,False,True,False,True,True,True,True,False,False,False,False,True,True,True,True,False,True,True,False,False,True,False,False,False,True,False,True,False,True,False,True,True,False,True,False,True,False,False,True,False,False,True,False,True,True,True,True,False,False,True,True,True,False,True,True,True,True,True,True,False,True,False,False,True,False,False,False,False,False,True,True,True,True,True,False,False,False,False,False,False,True,True,True,True,False,True,False,False,False,False,False,True,False,False,True,False,True,True,True,True,True,False,False,False,True,True,False,True,True,False,True,False,False,False,False,False,True,False,False,True],[False,True,True,True,True,False,True,False,True,False,False,False,False,False,False,True,True,False,False,False,True,True,True,True,False,True,True,True,True,False,True,False,True,False,True,False,False,False,True,True,True,True,False,True,True,False,True,True,True,True,True,False,True,False,True,True,True,False,False,True,False,True,True,True,True,False,False,True,False,True,True,True,False,True,True,True,True,False,False,False,True,False,False,False,False,True,True,False,False,False,True,False,True,False,False,True,False,False,False,False,True,True,False,True,False,True,False,False,True,True,False,False,True,True,True,True,False,False,True,False,False,False,True,False,False,True,True,False,True,True,True,False,True,True,True,True,False,True,True,True,False,False,True,True,True,False,True,True,True,False,False,True,True,True,True,True,False,False,False,True,False,True,True,True,False,False,False,False,True,False,True,False,False,False,True,True,True,False,False,False,True,False,True,False,True,True,True,True,True,True,False,True,False,True,False,False,True,True,False,True,True,True,True,True,False,False,False,True,True,False,True,False,True,False,False,False,True,True,False,True],[True,False,False,True,False,True,False,True,False,False,False,True,False,True,False,False,False,False,True,True,False,False,True,True,False,True,False,False,False,False,True,True,False,True,True,False,False,True,False,False,True,False,True,True,False,True,True,False,True,False,True,False,False,False,True,True,True,True,True,True,True,False,True,False,True,False,False,False,True,False,False,False,True,False,False,True,True,True,True,True,False,False,True,False,False,False,True,True,False,False,False,True,False,True,True,False,True,False,False,False,False,False,True,True,False,True,False,False,False,True,True,False,True,False,True,True,False,False,False,False,True,True,False,True,False,True,True,False,True,True,False,False,False,True,True,False,False,False,False,True,True,True,True,True,True,False,False,False,True,True,False,False,False,False,True,False,False,True,False,True,False,True,True,False,False,True,True,True,True,True,False,False,True,True,True,False,False,False,False,True,True,True,True,True,True,False,True,True,True,False,True,False,True,False,False,True,True,True,False,False,True,False,True,False,False,False,False,False,False,True,True,True,False,False,False,True,False,False,True,False],[False,False,False,True,False,False,False,False,False,True,False,True,True,True,True,True,False,True,True,False,False,False,False,False,False,False,False,True,False,True,True,False,True,True,True,True,True,False,True,True,True,False,False,False,True,True,False,True,True,True,False,True,False,False,False,False,False,False,True,True,True,False,True,False,True,True,True,True,True,True,False,False,True,True,False,False,False,False,False,True,False,False,True,False,False,True,False,False,True,False,True,False,False,True,False,False,False,True,True,True,False,True,True,True,False,True,False,True,False,False,False,False,False,True,False,False,False,False,False,True,False,False,True,True,True,True,True,True,True,False,False,True,True,True,True,False,False,True,True,False,True,True,False,True,True,False,True,True,True,True,True,True,True,False,False,False,False,True,True,True,True,True,False,True,False,True,True,True,False,False,True,True,True,False,False,False,False,True,False,True,True,True,True,False,True,True,True,True,True,False,False,False,False,True,True,False,False,False,True,True,False,True,False,False,True,True,False,True,False,False,True,True,True,False,False,True,True,True,False,False],[True,True,True,True,False,False,False,False,True,True,True,True,False,False,True,True,True,False,True,True,False,False,True,False,False,True,True,True,False,True,False,True,False,True,True,False,True,True,True,False,False,False,False,True,False,True,False,True,True,True,True,False,True,False,False,True,True,True,True,True,False,True,False,True,False,True,True,True,False,False,False,True,True,False,False,True,True,False,True,True,False,False,True,True,False,True,True,True,False,False,False,False,True,False,True,True,False,True,False,False,True,False,True,False,False,True,False,False,False,True,True,False,True,False,True,True,True,False,False,True,False,False,True,True,False,True,False,False,False,True,True,True,True,False,False,False,False,False,False,False,True,True,False,False,True,True,True,False,False,True,True,False,True,False,False,True,True,False,False,True,True,True,True,True,True,True,True,True,True,True,True,False,False,True,False,True,True,True,True,True,False,False,True,True,False,True,False,False,False,False,True,True,True,False,False,True,True,True,False,False,False,False,False,False,True,False,True,False,True,False,True,True,False,True,False,True,False,True,True,False]], dtype = "bool")#candidate|7404|(9, 220)|const|bool
call_7403 = relay.TupleGetItem(func_192_call(relay.reshape(const_7404.astype('bool'), [12, 11, 15])), 0)
call_7405 = relay.TupleGetItem(func_195_call(relay.reshape(const_7404.astype('bool'), [12, 11, 15])), 0)
var_7406 = relay.var("var_7406", dtype = "bool", shape = (9, 220))#candidate|7406|(9, 220)|var|bool
bop_7407 = relay.divide(const_7404.astype('float64'), relay.reshape(var_7406.astype('float64'), relay.shape_of(const_7404))) # shape=(9, 220)
output = relay.Tuple([call_7394,call_7403,bop_7407,])
output2 = relay.Tuple([call_7395,call_7405,bop_7407,])
func_7418 = relay.Function([var_7406,], output)
mod['func_7418'] = func_7418
mod = relay.transform.InferType()(mod)
var_7419 = relay.var("var_7419", dtype = "bool", shape = (9, 220))#candidate|7419|(9, 220)|var|bool
output = func_7418(var_7419)
func_7420 = relay.Function([var_7419], output)
mutated_mod['func_7420'] = func_7420
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4188_call = mod.get_global_var('func_4188')
func_4189_call = mutated_mod.get_global_var('func_4189')
call_7450 = func_4188_call()
call_7451 = func_4188_call()
func_5224_call = mod.get_global_var('func_5224')
func_5227_call = mutated_mod.get_global_var('func_5227')
const_7459 = relay.const([3,-6,-6,-4,1,3,-1,5,-6,-8,9,-10,-10,-5,4,-1,-10,3,-1,-2,-2,4,-7,-9,-3,4,6,3,8,9,10,10,-7,9,-1,-2,-7,-6,-7,-7,-1,2,-4,3,5,-3,-2,-6,-5,8,-7,9,-7,10,10,-6,-8,-8,3,6,5,-4,4,7,6,-7,6,-9,-1,-8,-6,-1,3,9,-3,6,8,-7,10,4,-9,-1,9,9,8,-2,-2,-1,2,-2,8,-5,6,9,-3,-1,3,7,-1,1,-4,6,-6,10,10,5,8,2,-9,1,3,-6,6,-10,10,8,6,9,-2,2,-10,10,6,-3,5,10,-6,6,-10,8,-8,3,2,-6,10,6,6,8,-10,-8,5,-4,-4,4,7,-3,8,-10,5,-5,-7,-5,-1,-4,5,7,-2,2,3,10,-8,8,-9,6,-8,1,6,-6,-10,-9,4,5,-8,4,3,-5,6,-6,-4,1,7,-5,9,-9,4,3,5,8,7,7,5,-2,5,-8,-2,9,10,-2,7,-7,1,-3,-10,-2,-10,-8,10,5,-7,2,-1,-9,-7,1,4,7,8,4,8,4,4,4,-1,7,2,-9,4,-6,-1,-5,5,-4,1,-10,3,-8,7,1,10,7,-1,7,-6,-4,-9,4,2,-4,6,-3,-7,8,-2,-3,-8,4,-7,-3,-3,-10,10,4,-1,-5,2,8,9,-7,-4,3,1,9,8,2,1,-2,5,-2,-6,-5,-7,2,-6,6,7,2,-5,-5,5,4,9,-6,4,3,7,8,1,-7,-7,9,-2,-4,-3,10,6,1,-2,2,-7,5,2,-5,5,2,-6,-8,3,5,-10,-2,-1,-2,4,-10,-8,4,-8,5,-2,7,-9,6,6,-7,-10,-3,-6,5,-10,8,10,9,2,3,-2,-3,5,6,3,-8,-4,4,-7,-9,-6,4,-10,3,-9,-5,-7,6,8,-3,-7,5,-5,3,-10,8,1,1,9,3,-10,-10,7,-7,10,-9,3,8,3,-10,4,-10,-4,-6,4,-2,8,-1,10,1,10,-6,-3,2,8,2,2,6,-2,-10,4,3,3,-8,-2,2,-10,-6,7,-1,-10,6,7,-9,-6,7,8,-3,-4,4,1,-7,-8,-6,-8,9,-9,1], dtype = "uint32")#candidate|7459|(432,)|const|uint32
call_7458 = relay.TupleGetItem(func_5224_call(relay.reshape(const_7459.astype('uint32'), [6, 6, 12]), relay.reshape(const_7459.astype('uint32'), [6, 6, 12]), ), 0)
call_7460 = relay.TupleGetItem(func_5227_call(relay.reshape(const_7459.astype('uint32'), [6, 6, 12]), relay.reshape(const_7459.astype('uint32'), [6, 6, 12]), ), 0)
func_6424_call = mod.get_global_var('func_6424')
func_6425_call = mutated_mod.get_global_var('func_6425')
call_7462 = relay.TupleGetItem(func_6424_call(), 0)
call_7463 = relay.TupleGetItem(func_6425_call(), 0)
func_6424_call = mod.get_global_var('func_6424')
func_6425_call = mutated_mod.get_global_var('func_6425')
call_7465 = relay.TupleGetItem(func_6424_call(), 0)
call_7466 = relay.TupleGetItem(func_6425_call(), 0)
uop_7476 = relay.cos(const_7459.astype('float64')) # shape=(432,)
func_4770_call = mod.get_global_var('func_4770')
func_4771_call = mutated_mod.get_global_var('func_4771')
call_7480 = relay.TupleGetItem(func_4770_call(), 0)
call_7481 = relay.TupleGetItem(func_4771_call(), 0)
output = relay.Tuple([call_7450,call_7458,call_7462,call_7465,uop_7476,call_7480,])
output2 = relay.Tuple([call_7451,call_7460,call_7463,call_7466,uop_7476,call_7481,])
func_7482 = relay.Function([], output)
mod['func_7482'] = func_7482
mod = relay.transform.InferType()(mod)
mutated_mod['func_7482'] = func_7482
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7482_call = mutated_mod.get_global_var('func_7482')
call_7483 = func_7482_call()
output = call_7483
func_7484 = relay.Function([], output)
mutated_mod['func_7484'] = func_7484
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5412_call = mod.get_global_var('func_5412')
func_5414_call = mutated_mod.get_global_var('func_5414')
call_7489 = relay.TupleGetItem(func_5412_call(), 1)
call_7490 = relay.TupleGetItem(func_5414_call(), 1)
output = call_7489
output2 = call_7490
func_7496 = relay.Function([], output)
mod['func_7496'] = func_7496
mod = relay.transform.InferType()(mod)
mutated_mod['func_7496'] = func_7496
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7496_call = mutated_mod.get_global_var('func_7496')
call_7497 = func_7496_call()
output = call_7497
func_7498 = relay.Function([], output)
mutated_mod['func_7498'] = func_7498
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7343_call = mod.get_global_var('func_7343')
func_7345_call = mutated_mod.get_global_var('func_7345')
call_7508 = relay.TupleGetItem(func_7343_call(), 0)
call_7509 = relay.TupleGetItem(func_7345_call(), 0)
output = call_7508
output2 = call_7509
func_7520 = relay.Function([], output)
mod['func_7520'] = func_7520
mod = relay.transform.InferType()(mod)
output = func_7520()
func_7521 = relay.Function([], output)
mutated_mod['func_7521'] = func_7521
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7496_call = mod.get_global_var('func_7496')
func_7498_call = mutated_mod.get_global_var('func_7498')
call_7553 = func_7496_call()
call_7554 = func_7496_call()
output = call_7553
output2 = call_7554
func_7564 = relay.Function([], output)
mod['func_7564'] = func_7564
mod = relay.transform.InferType()(mod)
output = func_7564()
func_7565 = relay.Function([], output)
mutated_mod['func_7565'] = func_7565
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7573 = relay.var("var_7573", dtype = "int16", shape = ())#candidate|7573|()|var|int16
const_7574 = relay.const([[[2,-5,10,4,-9,10,-9,-10,1,4,1,6],[7,6,9,-7,-6,1,2,-1,2,-2,8,6],[3,5,-5,2,5,7,-6,6,-1,-7,-4,-3],[-10,7,-9,9,-10,-8,5,9,9,-3,-2,-8],[8,5,4,8,5,3,-6,-9,-7,3,8,2],[-8,4,-6,5,10,5,10,-1,9,-10,-8,-3],[-6,7,-8,3,7,-8,-2,8,4,9,7,8],[1,10,7,-4,-8,10,3,-4,3,-5,6,8],[-7,2,4,-9,-10,-6,-2,3,-5,-8,6,-9],[5,-3,-7,10,7,-9,4,10,9,-10,-8,1],[-3,2,-4,-8,6,9,-2,9,-1,-2,4,-6],[8,4,-8,-1,-7,-2,-5,7,10,7,4,-1],[2,-7,-7,-9,-10,3,9,1,-7,6,-1,-3],[8,-5,4,9,-1,-2,1,3,6,1,8,-3]],[[7,6,2,-1,7,-5,1,-9,-2,1,4,-7],[10,8,-2,-2,10,-6,-7,-3,2,7,3,6],[-7,-9,2,1,-5,-1,-2,5,3,4,-8,-4],[6,4,9,7,8,7,3,4,-9,-5,10,-4],[-1,2,-7,8,10,-5,1,-5,7,10,9,7],[9,-10,-2,-1,-1,10,9,-3,1,8,-9,2],[-2,-7,-6,-1,-4,5,5,9,-1,6,-9,1],[-7,4,1,-2,-6,-5,3,9,-9,3,4,-10],[1,5,2,-9,-4,-5,-9,-9,7,-9,-10,-8],[-7,-2,3,6,-5,5,8,8,-9,8,-1,-4],[10,9,-4,-8,-9,9,-2,7,7,-7,-8,-6],[8,-6,10,-9,3,-10,-4,5,-1,-5,-1,-2],[-6,3,4,2,5,4,6,-8,1,6,-8,-9],[7,-2,8,-1,3,-10,-5,-10,10,10,7,-7]],[[-3,4,-3,-2,8,-3,10,-3,-7,-9,-3,5],[-4,1,10,-10,8,6,-6,4,-4,10,-8,-6],[-6,-5,7,4,4,3,-1,1,-4,1,-7,5],[9,-5,10,1,-8,5,-8,-7,4,8,-2,5],[8,-7,2,-6,9,9,5,-5,6,-8,-1,-9],[-6,10,-8,3,2,10,-4,-6,-10,-4,5,-9],[1,7,4,-7,-3,-8,2,8,3,-10,4,2],[1,10,5,-6,9,-6,-9,5,10,4,5,7],[-10,5,-3,10,10,9,-3,2,8,7,1,-9],[5,4,-3,-10,-8,-9,-1,-4,-10,8,7,5],[8,-1,6,-3,-1,-3,-7,-9,9,5,-6,-4],[-9,-2,-2,10,-1,-2,-10,9,1,-10,-6,-3],[-9,-6,-5,-3,-3,-1,-2,-7,-3,-1,6,-8],[2,5,-7,7,-7,10,3,6,-8,3,1,4]],[[-10,1,-3,-3,7,6,-6,-9,-8,-3,-4,-9],[10,-4,-1,-9,3,7,6,-4,-5,6,-3,-4],[-8,2,-10,6,-2,-2,-9,5,8,-10,9,-9],[4,10,2,10,1,-4,4,10,10,-8,1,-3],[-5,-5,-4,-1,-10,8,4,-4,2,5,-7,10],[7,6,-1,-6,1,1,4,6,4,7,-1,-5],[8,9,-5,3,-8,9,-8,-8,-6,6,4,5],[-5,-7,5,9,2,-1,6,-10,-4,6,5,3],[-4,5,-9,5,5,10,4,5,7,4,9,10],[4,-7,9,-4,9,10,-2,-1,6,8,3,7],[-1,-5,-6,6,-2,-1,-3,5,-4,9,7,4],[-3,5,-8,-8,-3,9,-2,9,6,-5,7,-10],[-5,7,-8,7,-5,-9,-5,10,-2,9,-2,7],[10,-8,4,-8,-6,10,7,-5,-2,-3,-3,-6]],[[2,8,8,3,-9,-7,-8,1,1,7,-9,-10],[9,7,-8,7,-2,3,2,10,-8,4,1,9],[-7,1,9,8,-7,-7,9,5,1,-1,-6,4],[-7,10,-6,-1,-3,10,4,-9,-10,-5,10,-2],[10,6,4,1,-8,1,-10,-6,5,-5,1,-9],[10,-4,6,5,-9,5,9,-7,7,-3,-2,-1],[7,3,2,3,-8,6,10,3,10,-5,3,8],[-3,8,3,2,9,-10,-9,-5,-7,-2,-10,-10],[-2,9,-10,7,9,-9,-7,2,6,9,4,-4],[-4,-10,3,5,7,-3,5,8,-7,6,-8,2],[-10,-3,4,5,-6,-2,-7,8,-3,10,-3,1],[7,-6,8,1,8,4,3,-9,6,-2,10,-8],[-1,10,7,3,-3,-1,6,10,-7,-7,-4,9],[-8,5,-1,1,-1,7,6,-2,-1,-9,6,-3]],[[2,3,-6,7,3,2,-7,7,5,6,4,-8],[2,1,7,-10,4,4,-8,-4,5,7,6,-9],[-8,2,-4,8,-10,-5,5,-3,-1,-8,1,1],[7,-7,-4,6,1,5,-10,3,-3,4,-4,-6],[-5,-5,8,4,6,10,8,-3,4,6,2,-2],[8,3,-5,6,-5,8,-6,9,-4,1,5,-2],[-1,-2,8,8,-2,-5,-1,-8,-3,-10,-9,-3],[9,4,8,-4,-2,4,4,5,4,-4,-2,-1],[-1,6,-1,-2,2,6,-9,1,-9,-3,-8,1],[-10,-4,9,7,-6,9,-1,10,6,5,8,-1],[10,2,-4,-7,1,-7,9,-10,7,6,2,-3],[-4,6,-4,-1,-2,-2,7,1,3,8,-1,10],[-2,8,-2,2,9,10,-6,-8,3,7,9,7],[5,7,6,6,4,1,6,2,5,9,-2,-2]]], dtype = "int16")#candidate|7574|(6, 14, 12)|const|int16
bop_7575 = relay.multiply(var_7573.astype('int16'), const_7574.astype('int16')) # shape=(6, 14, 12)
func_4135_call = mod.get_global_var('func_4135')
func_4137_call = mutated_mod.get_global_var('func_4137')
call_7581 = func_4135_call()
call_7582 = func_4135_call()
func_1209_call = mod.get_global_var('func_1209')
func_1214_call = mutated_mod.get_global_var('func_1214')
const_7591 = relay.const([[-0.663584,-4.572268,1.437114],[5.037160,-3.539793,2.233807],[4.649212,5.253207,7.967916],[-0.914291,-1.926802,-6.737482],[9.295339,9.569991,-9.698716],[-5.011893,-4.985752,9.832650],[4.838222,-3.578820,-5.898250],[-4.611758,5.394643,-5.372586],[1.769551,9.540917,4.258626],[0.746115,-0.636731,-4.564357],[4.047620,8.282247,9.603298],[7.274430,-3.131612,-2.754628],[6.787994,-4.156128,1.564360],[9.366751,9.748229,-2.694126],[-9.412254,5.259333,-2.028624],[8.571048,6.519118,4.907661],[1.920763,3.089865,-7.976718],[-8.152235,-6.774670,1.755589],[1.051367,1.740186,3.449441],[0.215077,8.707140,-2.387739],[-3.405147,5.216133,2.570152],[2.811374,5.791819,-3.183519],[-5.093431,7.572435,1.994659],[-8.962959,4.075229,5.391368],[7.305431,-8.456811,-7.703526],[2.627928,-2.823210,-6.099456],[1.053825,2.845986,-2.027821],[6.736076,-9.220380,4.752749],[4.855175,7.494323,6.598853],[7.418964,8.128695,5.162741],[2.657948,4.319848,3.474915],[2.658672,0.691174,5.487042],[-5.879185,-1.616732,1.981051],[-6.066650,-7.110448,2.459323],[-6.066683,-3.662177,-7.827401],[5.208125,-1.608552,-5.672389],[-0.762960,4.940934,-0.322886],[1.425931,6.864173,4.051054],[-1.066584,6.048451,5.125927],[-1.484027,9.054257,-2.061192],[9.432061,0.750843,-4.432930],[4.295502,8.441375,-3.704092],[-4.675469,-0.278844,2.894362],[-2.097657,7.890928,-0.752347],[1.348630,6.262513,-3.756546],[-3.275397,8.535637,4.235937],[1.828074,7.770346,5.670811],[-5.921168,6.900588,9.329436],[8.744655,-4.917123,7.934423],[5.463954,-0.461286,-5.692174],[-2.054270,-4.060233,-2.102843],[4.321492,-1.708666,9.937330],[-2.464935,8.857168,-4.593010],[4.439573,2.190352,7.307724],[-2.251472,2.228302,7.279726],[6.177114,-9.740922,6.342448],[-1.531569,7.984478,7.636454],[-6.418810,-4.115451,-9.109757],[3.082675,-7.751237,3.436975],[7.656998,9.188803,-8.895814],[-7.535413,-9.163121,5.647366],[-2.142656,4.314796,3.579640],[-6.124118,-4.875052,2.069506],[2.605116,-6.812106,3.135493],[0.555078,-7.627401,7.614142],[5.360650,-0.981675,0.876076],[-5.573757,9.178406,4.355344],[-9.044556,1.313647,-1.616348],[2.417704,0.636170,-3.319201],[-5.843793,6.052268,-5.322921],[1.384677,3.544440,1.256820],[-4.055899,-7.768572,6.756501],[-3.576310,0.114980,1.006579],[-1.121321,0.574027,-7.065383],[2.986080,-0.197326,2.868077],[6.400430,-3.725514,8.906335],[7.718067,2.960694,0.807648],[7.421413,0.279809,5.325153],[3.186111,2.883687,5.508998],[-8.833765,-9.791579,-9.379688],[2.611009,3.497588,-2.439682],[2.395332,-7.324687,8.522939],[-5.205304,9.456324,9.538500],[-5.597743,-1.975800,4.637381],[7.270696,-1.895952,-3.130367],[-7.318823,6.485713,-5.985191],[-0.692942,7.385556,-6.302345],[-0.149946,-1.054025,-7.051746],[7.056611,-0.235418,1.989641],[6.171240,3.160321,-0.431873],[-4.470926,8.020137,-5.631017],[6.977297,2.711100,5.807849],[3.766374,-0.656987,4.124330],[1.578473,8.487392,3.635505],[-9.244566,-7.762598,-5.351696],[0.207960,6.346754,-3.133155],[-4.108531,-5.759492,3.199891],[-8.358191,5.584083,-2.468760],[5.732044,9.328060,3.326338],[2.261978,-9.558550,9.020805],[3.747541,0.682026,6.733463],[-2.540440,-2.094615,6.800841],[7.298574,-7.961270,0.980212],[7.955967,0.529164,7.257561],[8.753184,-2.832552,-7.026975],[4.957589,-9.488563,-3.096780],[-7.536533,-0.752709,3.940147],[-6.965990,4.250023,-3.431492],[7.992796,4.439075,-0.565877],[5.220733,-0.997364,9.194135],[0.435249,-9.194136,-2.697876],[1.869644,9.746738,2.121583],[-7.049947,6.215487,-0.311421],[-3.040048,-1.475418,-8.546340],[-7.761225,-2.313629,5.345106],[-1.466646,-0.527668,2.212281],[1.638558,-2.887589,-9.711829],[-1.837078,6.230285,-8.670660],[5.340652,-4.491634,-9.478545],[-1.454379,-9.797191,7.661123],[5.082903,7.655758,-6.177404],[-4.515845,6.943402,8.739761],[-4.676921,-1.034914,5.399583],[4.125270,9.383451,-5.710694],[2.819630,2.377753,-4.795661],[8.208002,-2.579707,3.451214],[7.198338,-7.565872,-2.453209],[-1.306256,5.636948,9.583657],[1.426382,5.634738,-4.590478],[9.265395,3.750752,9.666004],[7.929029,3.506848,4.454876],[7.734253,-2.465025,-5.359158],[9.048238,7.780530,8.455276],[4.437956,2.198405,-8.220819],[3.567043,0.599451,-5.960811],[-9.274956,-2.184660,2.962420],[-5.366732,-3.277132,-1.908795],[-4.422846,-2.001305,5.834980],[-5.719609,-1.494997,0.484858],[5.071663,-3.551061,7.324040],[8.593011,0.336421,4.872738],[-7.999429,0.960626,-8.656667],[2.558214,9.144883,-2.956362],[9.404389,1.532414,3.813284],[-5.353145,9.969822,0.493174],[2.941436,-4.391837,-0.046214],[1.202838,-3.777192,-6.473891],[7.111380,4.115316,7.228939],[8.490883,-4.135496,-9.275887],[8.592786,-5.511787,-4.305827],[-1.813517,-3.258914,-8.713458],[-0.972372,0.031146,-1.800387],[-9.003721,1.781114,-1.984402],[0.077733,-6.711708,-3.284124],[5.077287,6.184986,8.810456],[-2.367575,-1.344553,-7.965493],[7.926651,-3.638242,6.766322],[-5.276762,-5.551424,0.876519],[-9.383364,-9.099846,-8.729499],[-7.284020,6.087236,7.838602],[4.748677,-5.577928,6.768844],[-6.112108,8.827786,5.942209],[4.506689,-3.959623,-4.201936],[-0.278555,2.904537,4.013029],[4.365989,4.975944,2.790938],[5.530663,-4.734401,-1.353111],[8.218344,4.591902,-1.567125],[6.374472,-7.472468,9.635763],[-9.957617,-7.823188,6.314739],[9.543156,2.197074,7.281898],[-4.083962,3.304602,-0.300316],[-6.155674,-3.999845,-9.990131],[-4.688313,-1.564247,-5.025773],[2.757694,2.094881,-1.793124],[7.482188,5.138643,-0.629554],[-8.734496,-1.562165,-0.584411],[4.978200,-5.203255,-0.813117],[-6.722320,-7.114166,6.440443],[7.934751,4.415653,-6.034759],[3.116840,-8.115152,-1.699655],[8.648761,2.318575,-2.581924],[-9.996864,-2.715980,0.613389],[8.818906,6.817855,-5.790588],[-2.476647,-8.905647,-0.648782],[6.780081,-7.069869,3.896972],[1.585278,5.638260,-4.801194],[-0.896738,-2.894330,2.201245],[3.800025,3.279060,-1.367908],[8.991495,8.072482,7.640059],[5.553590,9.578518,-0.878237],[-3.052543,4.781534,-9.936997],[-2.736749,-7.199540,0.914976],[-0.135679,4.102019,4.797016],[-0.148381,-1.894168,-9.960628],[1.018221,6.321230,-6.637978],[7.719176,8.699696,-9.726109],[-6.114983,-5.525793,6.167123],[-0.856508,-1.906027,-7.521458],[-6.434271,-6.852765,-1.211366],[-2.359665,-3.675010,7.323582],[5.168955,-7.463996,5.706562],[-4.603510,4.189947,6.835184],[-5.818181,-4.484683,9.042439],[-6.867660,5.250084,-5.952126],[-1.001511,-9.515119,-7.761202],[6.840176,-2.558326,-3.025335],[-5.220862,-2.148620,2.881994],[2.627422,6.642287,-4.103080],[-9.414764,-0.696141,-4.723269],[5.808202,6.272944,9.914436],[3.892764,6.449303,-3.861252],[-6.251420,-1.630202,-7.961615],[-7.692023,7.490589,-0.864214],[-9.997241,9.389871,-2.658874],[4.963222,-7.960544,0.443825],[5.754219,-0.776057,8.102633],[-2.468381,6.373747,-2.198133],[5.264797,4.417894,-9.528440],[-0.509938,-5.288565,-2.510258],[0.439738,9.137308,-2.067497],[-0.263685,9.676401,1.026597],[0.784942,-2.790237,-1.772433],[5.985396,4.892976,9.476456],[-3.103687,-3.743222,1.825220],[6.595811,2.016793,-5.932322],[-0.924762,5.169534,9.427978],[-9.639212,-0.361012,4.394347],[5.966074,-2.892018,-0.379790],[-0.260476,-9.368568,8.260745],[3.274450,-5.957974,2.698077],[0.754488,8.416121,-9.017353],[9.279440,-2.842323,8.689926],[-6.912336,-5.437207,-2.629100],[-9.452476,4.515139,1.388968],[-4.527550,7.591101,9.601815],[9.607494,-0.655997,1.336054],[4.241961,0.179312,0.001136],[-8.509979,8.920578,-1.092896],[4.835092,0.612887,3.043558],[9.729474,8.929793,7.781488],[-2.854819,9.713546,5.617720],[2.452205,6.085662,-4.507228],[3.871627,2.961588,9.633852],[-8.114174,-3.171070,9.650965],[5.575470,-0.550054,-8.597327],[5.346496,-9.372113,3.667096],[-3.515367,3.016490,-6.591056],[-4.469335,-9.522330,-0.060092],[8.140734,-2.850014,-5.271088],[-3.960649,-1.911519,2.428297]], dtype = "float32")#candidate|7591|(250, 3)|const|float32
call_7590 = relay.TupleGetItem(func_1209_call(relay.reshape(const_7591.astype('float32'), [5, 10, 15]), relay.reshape(const_7591.astype('float32'), [5, 10, 15]), relay.reshape(const_7591.astype('float32'), [5, 10, 15]), ), 1)
call_7592 = relay.TupleGetItem(func_1214_call(relay.reshape(const_7591.astype('float32'), [5, 10, 15]), relay.reshape(const_7591.astype('float32'), [5, 10, 15]), relay.reshape(const_7591.astype('float32'), [5, 10, 15]), ), 1)
uop_7605 = relay.rsqrt(const_7591.astype('float64')) # shape=(250, 3)
bop_7611 = relay.maximum(uop_7605.astype('int8'), relay.reshape(const_7591.astype('int8'), relay.shape_of(uop_7605))) # shape=(250, 3)
uop_7614 = relay.log2(uop_7605.astype('float32')) # shape=(250, 3)
func_429_call = mod.get_global_var('func_429')
func_431_call = mutated_mod.get_global_var('func_431')
var_7623 = relay.var("var_7623", dtype = "float32", shape = (500,))#candidate|7623|(500,)|var|float32
call_7622 = relay.TupleGetItem(func_429_call(relay.reshape(var_7623.astype('float32'), [10, 10, 5])), 0)
call_7624 = relay.TupleGetItem(func_431_call(relay.reshape(var_7623.astype('float32'), [10, 10, 5])), 0)
uop_7627 = relay.log10(uop_7614.astype('float64')) # shape=(250, 3)
output = relay.Tuple([bop_7575,call_7581,call_7590,bop_7611,call_7622,var_7623,uop_7627,])
output2 = relay.Tuple([bop_7575,call_7582,call_7592,bop_7611,call_7624,var_7623,uop_7627,])
func_7629 = relay.Function([var_7573,var_7623,], output)
mod['func_7629'] = func_7629
mod = relay.transform.InferType()(mod)
var_7630 = relay.var("var_7630", dtype = "int16", shape = ())#candidate|7630|()|var|int16
var_7631 = relay.var("var_7631", dtype = "float32", shape = (500,))#candidate|7631|(500,)|var|float32
output = func_7629(var_7630,var_7631,)
func_7632 = relay.Function([var_7630,var_7631,], output)
mutated_mod['func_7632'] = func_7632
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5049_call = mod.get_global_var('func_5049')
func_5050_call = mutated_mod.get_global_var('func_5050')
call_7640 = relay.TupleGetItem(func_5049_call(), 0)
call_7641 = relay.TupleGetItem(func_5050_call(), 0)
func_5885_call = mod.get_global_var('func_5885')
func_5887_call = mutated_mod.get_global_var('func_5887')
call_7644 = relay.TupleGetItem(func_5885_call(), 0)
call_7645 = relay.TupleGetItem(func_5887_call(), 0)
func_4061_call = mod.get_global_var('func_4061')
func_4064_call = mutated_mod.get_global_var('func_4064')
var_7651 = relay.var("var_7651", dtype = "bool", shape = (1980,))#candidate|7651|(1980,)|var|bool
call_7650 = relay.TupleGetItem(func_4061_call(relay.reshape(call_7644.astype('float32'), [14, 9, 6]), relay.reshape(var_7651.astype('bool'), [1980,]), ), 2)
call_7652 = relay.TupleGetItem(func_4064_call(relay.reshape(call_7644.astype('float32'), [14, 9, 6]), relay.reshape(var_7651.astype('bool'), [1980,]), ), 2)
output = relay.Tuple([call_7640,call_7644,call_7650,var_7651,])
output2 = relay.Tuple([call_7641,call_7645,call_7652,var_7651,])
func_7659 = relay.Function([var_7651,], output)
mod['func_7659'] = func_7659
mod = relay.transform.InferType()(mod)
mutated_mod['func_7659'] = func_7659
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7660 = relay.var("var_7660", dtype = "bool", shape = (1980,))#candidate|7660|(1980,)|var|bool
func_7659_call = mutated_mod.get_global_var('func_7659')
call_7661 = func_7659_call(var_7660)
output = call_7661
func_7662 = relay.Function([var_7660], output)
mutated_mod['func_7662'] = func_7662
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5632_call = mod.get_global_var('func_5632')
func_5633_call = mutated_mod.get_global_var('func_5633')
call_7712 = func_5632_call()
call_7713 = func_5632_call()
output = relay.Tuple([call_7712,])
output2 = relay.Tuple([call_7713,])
func_7728 = relay.Function([], output)
mod['func_7728'] = func_7728
mod = relay.transform.InferType()(mod)
output = func_7728()
func_7729 = relay.Function([], output)
mutated_mod['func_7729'] = func_7729
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6689_call = mod.get_global_var('func_6689')
func_6691_call = mutated_mod.get_global_var('func_6691')
call_7733 = relay.TupleGetItem(func_6689_call(), 0)
call_7734 = relay.TupleGetItem(func_6691_call(), 0)
func_722_call = mod.get_global_var('func_722')
func_725_call = mutated_mod.get_global_var('func_725')
var_7740 = relay.var("var_7740", dtype = "uint8", shape = (990, 1))#candidate|7740|(990, 1)|var|uint8
call_7739 = func_722_call(relay.reshape(var_7740.astype('uint8'), [11, 10, 9]))
call_7741 = func_722_call(relay.reshape(var_7740.astype('uint8'), [11, 10, 9]))
func_722_call = mod.get_global_var('func_722')
func_725_call = mutated_mod.get_global_var('func_725')
call_7746 = func_722_call(relay.reshape(var_7740.astype('uint8'), [11, 10, 9]))
call_7747 = func_722_call(relay.reshape(var_7740.astype('uint8'), [11, 10, 9]))
func_5162_call = mod.get_global_var('func_5162')
func_5167_call = mutated_mod.get_global_var('func_5167')
var_7750 = relay.var("var_7750", dtype = "float32", shape = (220,))#candidate|7750|(220,)|var|float32
const_7751 = relay.const([False,False,True,True,True,False,False,True,False,False,True,True,False,True,True,False,True,True,True,True,False,True,True,False,True,False,False,True,True,False,False,True,True,True,False,False,True,True,True,True,True,False,False,True,True,True,True,False,True,True,True,True,False,True,True,True,True,True,True,False,False,True,False,True,False,False,True,True,True,False,False,True,True,False,False,False,False,False,True,True,True,False,False,True,True,True,True,False,True,False,True,True,True,True,False,True,True,True,False,True,True,False,False,False,False,False,True,False,False,False,True,True,False,True,True,False,True,False,False,False,False,True,True,True,False,True,False,False,False,False,True,True,False,True,False,False,True,True,True,False,True,False,True,True,False,False,True,True,False,False,True,False,True,False,True,False,True,True,False,True,True,True,False,True,False,False,False,True,True,True,True,False,True,True,False,True,True,True,False,False,True,True,False,True,True,False,True,False,True,True,True,True,False,False,False,False,False,False,True,False,True,True,False,True,False,False,False,True,False,True,True,True,False,False,False,False,False,True,False,True,False,False,False,False,False,True,False,False,True,False,False,True,True,True,False,True,True,False,False,True,True,False,True,False,False,True,False,False,True,False,True,True,False,False,False,False,True,False,True,False,False,True,True,True,False,True,False,False,False,True,True,True,True,False,True,True,False,True,True,True,False,False,False,False,False,False,True,True,True,False,False,True,True,True,True,False,True,True,False,True,False,True,False,True,False,False,False,False,True,True,True,True,False,True,False,False,False,True,False,True,True,False,False,False,True,True,False,False,True,False,True,True,False,False,True,False,False,True,False,True,True,True,True,True,False,True,True,False,False,True,True,True,True,False,True,True,True,False,True,False,False,True,False,False,True,True,False,True,False,False,False,True,True,True,False,False,False,False,False,False,True,False,True,True,False,True,False,True,True,True,False,True,False,False,False,True,True,False,False,True,True,True,True,False,False,True,False,True,True,True,True,True,True,True,False,True,False,False,False,True,True,False,False,False,False,False,True,True,True,False,True,False,True,False,False,True,True,True,False,True,False,False,False,True,True,False,False,True,False,False,False,True,True,False,True,True,True,True,True,False,True,False,False,False,False,False,True,True,True,False,False,True,False,False,False,True,False,False,False,False,True,False,False,False,False,True,True,True,False,False,True,True,False,True,True,False,False,True,False,True,True,False,True,True,True,True,False,True,False,False,False,True,False,False,True,False,True,False,False,False,True,True,True,True,True,True,False,True,False,False,False,True,False,True,False,True,True,False,True,True,False,True,False,False,True,True,False,False,True,False,False,False,False,False,False,True,True,False,False,True,False,False,False,False,False,False,False,True,False,True,False,False,False,False,False,True,True,False,True,False,True,False,True,True,False,True,False,True,True,False,False,True,False,False,True,False,False,True,True,False,False,True,False,False,True,False,True,False,False,True,True,True,True,False,False,True,True,False,False,False,False,False,True,True,False,False,True,False,False,True,False,False,False,False,True,False,False,False,False,False,True,True,False,False,True,False,True,False,True,True,False,True,True,True,False,True,False,False,True,False,True,True,False,True,True,True,True,True,False,False,False,True,True,False,False,True,False,True,True,True,True,False,True,False,True,True,False,True,True,True,True,False,True,False,False,False,True,True,False,True,True,False,True,True,False,True,False,False,False,True,False,True,True,True,False,True,False,False,False,False,True,False,False,False,False,False,True,True,False,True,True,True,True,False,False,True,True,False,True,True,False,True,True,True,False,True,False,True,True,True,True,False,True,True,True,True,False,False,False,False,True,True,True,False,True,False,True,False,False,False,False,False,False,True,False,False,False,False,True,True,True,False,True,False,False,False,True,False,False,False,False,True,True,True,True,True,True,False,True,False,True,True,False,True,False,False,True,False,True,True,True,False,True,True,True,True,True,False,True,False,False,True,True,False,True,True,True,False,True,False,False,False,False,True,True,False,True,True,True,False,False,False,True,True,True,False,True,True,False,False,True,True,False,False,True,True,True,False,True,True,False,False,True,False,True,True,True,False,False,False,True,False,False,False,True,False,False,False,True,False,True,False,True,True,False,False,False,False,False,True,True,True,True,False,True,False,True,False,True,True,False,False,True,True,False,True,True,False,True,False,False,False,False,False,True,False,False,True,False,True,True,True,False,False,False,True,True,True,False,False,True,False,False,False,True,False,True,False,False,True,False,False,True,False,False,True,True,True,False,True,False,True,True,False,False,True,True,True,False,True,True,True,False,True,False,True,True,True,False,True,False,False,True,False,True,False,True,False,True,True,True,True,True,False,True,True,True,False,False,False,False,True,True,False,False,True,True,True,True,True,False,True,False,True,True,True,True,False,True,False,False,False,True,True,True,False,False,False,True,False,False,True,True,False,True,True,True,False,False,False,False,False,False,False,True,True,True,True,False,False,True,False,False,True,True,True,True,True,False,False,True,False,True,False,False,False,True,False,True,True,False,True,True,False,True,False,False,False,True,False,False,True,False,False,False,True,False,True,False,False,False,True,False,True,True,True,False,False,True,True,True,True,False,False,False,True,False,False,True,False,False,True,True,False,True,True,True,True,False,True,True,False,False,False,False,True,True,False,True,False,True,False,True,True,False,True,False,False,True,True,False,True,False,True,True,True,False,False,True,True,True,False,True,True,False,True,False,True,True,True,True,False,True,True,True,True,False,True,False,False,False,False,True,False,False,True,False,False,True,True,True,True,True,True,False,False,False,True,True,False,False,True,False,False,False,False,True,False,True,True,False,False,False,False,False,False,True,False,False,False,True,False,True,True,True,False,True,True,True,False,True,True,True,False,True,True,False,True,False,True,False,False,True,False,False,False,False,True,False,True,False,False,True,True,True,False,True,False,True,False,False,True,False,False,True,True,True,True,False,True,False,True,False,False,True,False,False,False,False,False,True,False,False,False,True,True,False,True,True,True,True,False,False,True,False,True,True,True,False,True,True,True,False,True,True,False,True,True,False,True,True,True,True,False,True,True,True,True,False,True,False,True,True,True,True,True,False,False,False,True,True,True,False,False,False,True,False,False,False,False,True,True,True,True,True,False,False,True,True,False,False,True,True,True,False,False,False,True,False,False,False,False,False,False,False,False,True,False,False,True,False,False,False,True,True,False,True,True,True,False,True,True,True,False,False,False,True,False,True,True,False,True,True,False,True,True,True,False,True,True,True,True,True,True,False,False,True,True,True,False,True,False,True,True,True,True,True,False,True,False,True,False,True,True,False,False,False,True,False,False,True,True,True,False,False,False,True,False,True,False,False,True,True,False,False,False,True,True,False,True,True,True,True,False,False,True,False,True,True,False,True,False,True,False,False,True,False,True,True,False,False,False,True,True,False,True,True,True,False,True,False,True,False,True,True,True,True,True,False,False,True,True,False,False,True,False,True,False,False,True,False,False,True,True,True,True,False,False,False,False,True,True,True,True,False,False,False,True,True,False,True,False,True,True,False,True,False,True,True,False,False,True,False,True,False,True,False,False,True,True,False,False,False,True,True,False,True,False,False,False,False,True,False,False,True,False,True,True,True,False,True,False,True,True,True,True,False,False,True,True,True,True,True,True,False,False,True,True,False,True,True,True,True,True,True,False,True,False,True,False,False,False,False,True,True,False,False,True,False,True,False,True,False,True,False,False,True,True,True,False,True,False,True,False,True,False,False,False,False,True,False,False,True,True,True,False,True,True,True,True,False,True,False,False,False,False,False,True,True,True,True,False,True,False,False,False,False,False,False,False,True,False,False,False,True,True,False,False,False,True,True,False,False,True,False,False,True,False,False,True,True,True,True,False,False,False,False,False,False,False,True,False,True,True,False,False,True,True,True,True,False,False,False,True,False,False,True,True,True,True,False,False,True,False,True,True,False,True,True,False,False,False,False,True,False,True,True,True,False,False,False,False,True,False,True,True,True,True,False,False,False,True,False,True,True,True,False,True,True,False,True,True,False,False,False,False,True,True,True,True,False,False,True,True,False,True,False,True,False,False,True,False,True,False,False,False,True,False,True,False,False,True,True,True,True,True,True,False,True,True,True,True,True,False,False,True,True,False,True,True,False,False,False,False,False,False,False,False,False,False,False,True,True,False,False,False,True,True,False,False,False,True,True,True,True,True,True,True,True,False,False,False,False,False,False,True,False,False,True,True,False,True,False,True,True,False,True,True,True,True,True,False,False,True,True,False,False,False,True,False,False,True,False,True,False,False,False,False,False,True,True,True,False,True,False,False,True,False,True,True,True,False,True,False,True,False,False,False,True,True,False,True,False,False,False,False,False,False,True,False,True,False,True,False,False,False,False,True,False,True,False,True,True,True,True,True,False,True,True,True,False,True,False,True,True,True,True,True,True,False,True,True,True,True,True,True,True,True,False,True,False,True,False,True,False,False,False,False,True,True,True,False,False,False,True,True,True,False,False,False,True,False,True,False,True,False,True,False,True,True,True,True,False,True,True,True,True,True,True,True,True,True,True,True,True,False,True,False,False,True,False,True,True,False,True,False,False,False,False,False,False,True,True,False,True,False,True,False,False,True], dtype = "bool")#candidate|7751|(1980,)|const|bool
call_7749 = relay.TupleGetItem(func_5162_call(relay.reshape(var_7750.astype('float32'), [5, 11, 4]), relay.reshape(call_7733.astype('float32'), [756,]), relay.reshape(const_7751.astype('bool'), [1980,]), ), 2)
call_7752 = relay.TupleGetItem(func_5167_call(relay.reshape(var_7750.astype('float32'), [5, 11, 4]), relay.reshape(call_7733.astype('float32'), [756,]), relay.reshape(const_7751.astype('bool'), [1980,]), ), 2)
var_7757 = relay.var("var_7757", dtype = "uint16", shape = (11, 10, 9))#candidate|7757|(11, 10, 9)|var|uint16
bop_7758 = relay.less_equal(call_7746.astype('bool'), relay.reshape(var_7757.astype('bool'), relay.shape_of(call_7746))) # shape=(11, 10, 9)
bop_7761 = relay.less_equal(call_7747.astype('bool'), relay.reshape(var_7757.astype('bool'), relay.shape_of(call_7747))) # shape=(11, 10, 9)
bop_7765 = relay.logical_and(call_7746.astype('bool'), relay.reshape(call_7739.astype('bool'), relay.shape_of(call_7746))) # shape=(11, 10, 9)
bop_7768 = relay.logical_and(call_7747.astype('bool'), relay.reshape(call_7741.astype('bool'), relay.shape_of(call_7747))) # shape=(11, 10, 9)
output = relay.Tuple([call_7733,var_7740,call_7749,var_7750,const_7751,bop_7758,bop_7765,])
output2 = relay.Tuple([call_7734,var_7740,call_7752,var_7750,const_7751,bop_7761,bop_7768,])
func_7769 = relay.Function([var_7740,var_7750,var_7757,], output)
mod['func_7769'] = func_7769
mod = relay.transform.InferType()(mod)
mutated_mod['func_7769'] = func_7769
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7769_call = mutated_mod.get_global_var('func_7769')
var_7771 = relay.var("var_7771", dtype = "uint8", shape = (990, 1))#candidate|7771|(990, 1)|var|uint8
var_7772 = relay.var("var_7772", dtype = "float32", shape = (220,))#candidate|7772|(220,)|var|float32
var_7773 = relay.var("var_7773", dtype = "uint16", shape = (11, 10, 9))#candidate|7773|(11, 10, 9)|var|uint16
call_7770 = func_7769_call(var_7771,var_7772,var_7773,)
output = call_7770
func_7774 = relay.Function([var_7771,var_7772,var_7773,], output)
mutated_mod['func_7774'] = func_7774
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7496_call = mod.get_global_var('func_7496')
func_7498_call = mutated_mod.get_global_var('func_7498')
call_7849 = func_7496_call()
call_7850 = func_7496_call()
func_5974_call = mod.get_global_var('func_5974')
func_5977_call = mutated_mod.get_global_var('func_5977')
const_7852 = relay.const([9,8,-2,1,7,9,-7,-2,-9,-1,10,1,4,6,1,10,5,-10,-4,2,-1,3,9,-10,8,9,5,-2,3,10,9,-6,10,1,6,-7,-6,9,-8,8,-2,-3,-4,-7,5,2,9,-6,5,5,3,-10,-6,6,8,9,-8,9,9,10,-5,-8,2,5,3,9,-4,5,-6,4,-5,-5,7,-7,-10,-10,1,9,-4,-3,4,5,10,8,2,-1,-4,4,-10,10,9,-5,10,6,-8,-2,-10,10,8,-6,-9,1,-3,9,-5,-5,8,5,-6,3,9,-6,-2,-8,4,5,3,1,9,1,-8,6,-6,4,-3,6,2,-10,-8,-7,6,-10,-7,7,2,10,4,-5,-9,2,6,4,2,2,-6,-4,2,9,8,5,-6,9,-1,10,-5,-3,-2,7,-3,-6,10,9,-6,1,-6,6,-1,2], dtype = "uint16")#candidate|7852|(168,)|const|uint16
call_7851 = relay.TupleGetItem(func_5974_call(relay.reshape(const_7852.astype('uint16'), [3, 4, 14])), 1)
call_7853 = relay.TupleGetItem(func_5977_call(relay.reshape(const_7852.astype('uint16'), [3, 4, 14])), 1)
func_3847_call = mod.get_global_var('func_3847')
func_3850_call = mutated_mod.get_global_var('func_3850')
const_7867 = relay.const(10, dtype = "uint64")#candidate|7867|()|const|uint64
call_7866 = relay.TupleGetItem(func_3847_call(relay.reshape(const_7867.astype('uint64'), [])), 3)
call_7868 = relay.TupleGetItem(func_3850_call(relay.reshape(const_7867.astype('uint64'), [])), 3)
output = relay.Tuple([call_7849,call_7851,const_7852,call_7866,const_7867,])
output2 = relay.Tuple([call_7850,call_7853,const_7852,call_7868,const_7867,])
func_7874 = relay.Function([], output)
mod['func_7874'] = func_7874
mod = relay.transform.InferType()(mod)
mutated_mod['func_7874'] = func_7874
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7874_call = mutated_mod.get_global_var('func_7874')
call_7875 = func_7874_call()
output = call_7875
func_7876 = relay.Function([], output)
mutated_mod['func_7876'] = func_7876
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7897 = relay.var("var_7897", dtype = "int8", shape = ())#candidate|7897|()|var|int8
var_7898 = relay.var("var_7898", dtype = "int8", shape = (11, 1))#candidate|7898|(11, 1)|var|int8
bop_7899 = relay.bitwise_xor(var_7897.astype('int8'), var_7898.astype('int8')) # shape=(11, 1)
func_4099_call = mod.get_global_var('func_4099')
func_4102_call = mutated_mod.get_global_var('func_4102')
var_7909 = relay.var("var_7909", dtype = "int8", shape = (780,))#candidate|7909|(780,)|var|int8
call_7908 = relay.TupleGetItem(func_4099_call(relay.reshape(var_7909.astype('int8'), [780,])), 2)
call_7910 = relay.TupleGetItem(func_4102_call(relay.reshape(var_7909.astype('int8'), [780,])), 2)
output = relay.Tuple([bop_7899,call_7908,var_7909,])
output2 = relay.Tuple([bop_7899,call_7910,var_7909,])
func_7912 = relay.Function([var_7897,var_7898,var_7909,], output)
mod['func_7912'] = func_7912
mod = relay.transform.InferType()(mod)
var_7913 = relay.var("var_7913", dtype = "int8", shape = ())#candidate|7913|()|var|int8
var_7914 = relay.var("var_7914", dtype = "int8", shape = (11, 1))#candidate|7914|(11, 1)|var|int8
var_7915 = relay.var("var_7915", dtype = "int8", shape = (780,))#candidate|7915|(780,)|var|int8
output = func_7912(var_7913,var_7914,var_7915,)
func_7916 = relay.Function([var_7913,var_7914,var_7915,], output)
mutated_mod['func_7916'] = func_7916
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6066_call = mod.get_global_var('func_6066')
func_6068_call = mutated_mod.get_global_var('func_6068')
call_7924 = func_6066_call()
call_7925 = func_6066_call()
func_4770_call = mod.get_global_var('func_4770')
func_4771_call = mutated_mod.get_global_var('func_4771')
call_7938 = relay.TupleGetItem(func_4770_call(), 1)
call_7939 = relay.TupleGetItem(func_4771_call(), 1)
output = relay.Tuple([call_7924,call_7938,])
output2 = relay.Tuple([call_7925,call_7939,])
func_7940 = relay.Function([], output)
mod['func_7940'] = func_7940
mod = relay.transform.InferType()(mod)
mutated_mod['func_7940'] = func_7940
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7940_call = mutated_mod.get_global_var('func_7940')
call_7941 = func_7940_call()
output = call_7941
func_7942 = relay.Function([], output)
mutated_mod['func_7942'] = func_7942
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7482_call = mod.get_global_var('func_7482')
func_7484_call = mutated_mod.get_global_var('func_7484')
call_7983 = relay.TupleGetItem(func_7482_call(), 0)
call_7984 = relay.TupleGetItem(func_7484_call(), 0)
output = relay.Tuple([call_7983,])
output2 = relay.Tuple([call_7984,])
func_7989 = relay.Function([], output)
mod['func_7989'] = func_7989
mod = relay.transform.InferType()(mod)
mutated_mod['func_7989'] = func_7989
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7989_call = mutated_mod.get_global_var('func_7989')
call_7990 = func_7989_call()
output = call_7990
func_7991 = relay.Function([], output)
mutated_mod['func_7991'] = func_7991
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7343_call = mod.get_global_var('func_7343')
func_7345_call = mutated_mod.get_global_var('func_7345')
call_8023 = relay.TupleGetItem(func_7343_call(), 1)
call_8024 = relay.TupleGetItem(func_7345_call(), 1)
func_7940_call = mod.get_global_var('func_7940')
func_7942_call = mutated_mod.get_global_var('func_7942')
call_8025 = relay.TupleGetItem(func_7940_call(), 1)
call_8026 = relay.TupleGetItem(func_7942_call(), 1)
var_8031 = relay.var("var_8031", dtype = "int8", shape = (5, 156))#candidate|8031|(5, 156)|var|int8
bop_8032 = relay.not_equal(call_8023.astype('bool'), relay.reshape(var_8031.astype('bool'), relay.shape_of(call_8023))) # shape=(5, 156)
bop_8035 = relay.not_equal(call_8024.astype('bool'), relay.reshape(var_8031.astype('bool'), relay.shape_of(call_8024))) # shape=(5, 156)
var_8048 = relay.var("var_8048", dtype = "int8", shape = (5, 156))#candidate|8048|(5, 156)|var|int8
bop_8049 = relay.right_shift(call_8023.astype('uint8'), relay.reshape(var_8048.astype('uint8'), relay.shape_of(call_8023))) # shape=(5, 156)
bop_8052 = relay.right_shift(call_8024.astype('uint8'), relay.reshape(var_8048.astype('uint8'), relay.shape_of(call_8024))) # shape=(5, 156)
func_5275_call = mod.get_global_var('func_5275')
func_5277_call = mutated_mod.get_global_var('func_5277')
call_8055 = func_5275_call()
call_8056 = func_5275_call()
func_2410_call = mod.get_global_var('func_2410')
func_2418_call = mutated_mod.get_global_var('func_2418')
const_8059 = relay.const([5.497353,-1.813126,-1.354121,-3.257624,-5.571813,-2.105828,7.895549,2.838743,-4.865853,-8.089830,-8.799745,-8.058453,4.844468,2.836251,5.084903,-9.565935,5.481058,-6.956595,-6.494631,-0.751082,0.755807,-5.193640,7.736636,0.066930], dtype = "float64")#candidate|8059|(24,)|const|float64
const_8060 = relay.const(2, dtype = "uint16")#candidate|8060|()|const|uint16
var_8061 = relay.var("var_8061", dtype = "int8", shape = (512,))#candidate|8061|(512,)|var|int8
const_8062 = relay.const([-1.781733,2.238839,9.297656,0.271307,-5.092987,-5.107611,0.421918,-9.784994,0.240416,-6.132416,4.667145,1.762667,1.684933,9.158241,8.396115,-4.027455,-5.163499,-9.263586,2.991228,9.690829,-5.104762,-7.940102,-6.210221,-4.012949,-5.781534,0.836281,6.408482,7.176337,-8.396788,7.912687,-3.095960,-9.821267,9.587832,-3.591626,-6.681786,0.369158,-1.905099,1.948514,-3.057237,-3.203819,-2.002311,7.718969,-5.706851,-0.547998,5.906938,-0.783465,0.648938,-7.580072,3.226411,-1.316741,6.296595,-7.067499,7.395005,-5.107324,-3.661835,6.490681,-2.283663,-2.707310,2.773213,-4.056381,-0.503232,3.218159,7.075329,5.224398,-6.006556,-2.190539,3.339405,0.366975,-9.348688,-2.072742,7.073143,-2.647341,-1.523319,-4.450613,0.926916,6.415565,-9.382519,-2.768708,-7.900986,-3.405785,1.014855,-8.324360,-2.843345,7.878149,6.669731,0.178609,4.955797,0.594036,-0.051645,-9.839649,-8.149124,2.912350,-5.214985,-6.287621,5.324043,4.057725,4.127829,2.619449,-4.174101,5.897032,7.188735,-3.021532,-3.307528,-4.931271,0.311667,-5.238127,-0.802923,-2.258493,8.394978,-5.978943,-6.593065,5.815610,1.352583,6.149205,-3.652987,-8.514833,8.735831,-7.870460,-6.461400,-7.589918,3.899349,4.050629,-7.965903,-7.855790,-2.414438,2.346015,2.390942,-8.049006,1.760835,-6.637422,-3.210805,5.934452,4.367771,1.650542,0.259314,2.919371,5.923642,-6.365860,4.792541,9.159142,8.399596,-6.828785,-0.918715,-0.365858,-2.876798,6.590572,9.054067,-4.575548,-2.220676,-4.787419,7.862405,5.480421,-3.112136,-6.202792,-8.407446,0.768460,-2.417501,-3.512508,-9.141222,2.839146,8.058576,-3.174262,3.578456,2.240448,-5.216221,8.052692,-3.587138,-2.373184,7.261487,-8.489383,3.122874,2.833257,2.289218,-1.102529,-1.956543,-8.702990,-9.933844,-3.146356,3.526505,5.387921,8.426716,9.182550,6.617339,-6.755341,-6.140405,5.257139,-7.583628,-8.724109,-2.433604,-4.439676,-0.654747,8.570022,4.068284,-1.062506,7.516680,-1.439438,6.921376,-7.937246,-3.249157,7.994637,6.172253,-6.404678,2.934543,8.717453,9.536799,8.229117,-6.106467,-5.465946,-9.979845,-5.453229,-1.396884,0.963762,-7.378772,7.542606,-4.496228,-1.437404,5.166930,-9.159451,4.291737,-2.928848,2.912536,-4.080759,-0.994429,9.794863,5.774275,3.685470,-1.116010,5.572813,-6.662481,8.591063,3.582293,4.888180,-7.974837,-6.447219,0.164771,-8.013522,-3.303987,8.550785,6.814845,9.673883,-0.627836,9.066203,3.440905,-1.984886,7.805239,0.432245,8.604038,2.303531,-9.942129,5.591182,-6.565903,-9.967654,-1.899878,-1.594032,-6.656766,-4.163695,-3.550221,7.252842,2.116775,7.342853,-5.883593,1.360675,1.653257,1.679970,-8.103704,-1.845777,6.172934,0.883095,-8.698291,7.619772,-5.526757,0.998326,8.617098,-9.309935,-8.558849,9.113837,-2.219137,-3.656921,8.013520,1.095190,-3.980714,6.970496,-5.228863,2.350633,-0.921248,3.926030,0.035309,1.357066,-0.603597,4.381252,6.097412,4.529973,2.547889,-8.565445,1.388983,8.021791,6.894433,1.655697,9.826803,-0.573063,-1.015086,-0.726034,-4.473364,-5.314149,-4.133044,-9.034839,8.192594,7.719800,5.582220,4.491767,-8.244776,8.935452,4.065646,8.277552,3.865504,-8.073442,-8.442144,2.240136,-1.814994,3.202612,6.152537,3.652680,9.175377,-3.266984,-9.766475,2.488307,-9.410882,-7.126095,-4.716703,-4.590230,5.902494,1.172497,-1.832091,-6.559584,-2.667046,9.870887,9.269560,-0.271944,0.237400,-2.394721,0.239292,-3.657197,-2.111868,5.232547,6.020403,-9.946997,1.474147,-9.134111,5.409878,-3.456377,-7.405690,1.875367,-5.517138,-4.335616,-8.070883,3.855500,-3.552122,9.277923,-7.375602,4.726620,2.002538,-2.536178,2.736950,-6.824421,-9.578420,5.027793,-0.917099,-4.762996,-7.434802,-7.603266,7.447936,-3.936116,-7.750641,-9.878230,7.771939,-0.516362,-1.669168,8.017801,6.216618,-6.198358,-2.290837,-1.366698,-4.186426,-3.568387,2.262226,-1.718445,-7.889711,-9.459708,-8.570964,-9.978140,7.975536,-0.358756,0.980817,1.908663,8.114953,-8.689734,6.504483,-1.198669,-1.920802,4.786524,-0.954774,-1.634549,-9.732109,7.459710,-5.914410,-0.333608,-4.630073,7.610816,-3.470288,-8.587226,-9.969286,-7.691439,5.352936,8.772697,4.297258,8.267399,-9.911469,-5.830198,-9.057401,-0.617022,1.753441,-9.270625,5.176564,-4.478781,1.486394,-8.591135,2.320548,4.566485,9.632174,-0.262339,7.979536,-7.951171], dtype = "float32")#candidate|8062|(432,)|const|float32
var_8063 = relay.var("var_8063", dtype = "float32", shape = (165,))#candidate|8063|(165,)|var|float32
var_8064 = relay.var("var_8064", dtype = "float32", shape = (500,))#candidate|8064|(500,)|var|float32
call_8058 = relay.TupleGetItem(func_2410_call(relay.reshape(const_8059.astype('float64'), [2, 12, 1]), relay.reshape(const_8060.astype('uint16'), []), relay.reshape(var_8061.astype('int8'), [512,]), relay.reshape(const_8062.astype('float32'), [432,]), relay.reshape(var_8063.astype('float32'), [165,]), relay.reshape(var_8064.astype('float32'), [500,]), ), 9)
call_8065 = relay.TupleGetItem(func_2418_call(relay.reshape(const_8059.astype('float64'), [2, 12, 1]), relay.reshape(const_8060.astype('uint16'), []), relay.reshape(var_8061.astype('int8'), [512,]), relay.reshape(const_8062.astype('float32'), [432,]), relay.reshape(var_8063.astype('float32'), [165,]), relay.reshape(var_8064.astype('float32'), [500,]), ), 9)
var_8066 = relay.var("var_8066", dtype = "float32", shape = (165,))#candidate|8066|(165,)|var|float32
bop_8067 = relay.equal(var_8063.astype('bool'), relay.reshape(var_8066.astype('bool'), relay.shape_of(var_8063))) # shape=(165,)
output = relay.Tuple([call_8025,bop_8032,bop_8049,call_8055,call_8058,const_8059,const_8060,var_8061,const_8062,var_8064,bop_8067,])
output2 = relay.Tuple([call_8026,bop_8035,bop_8052,call_8056,call_8065,const_8059,const_8060,var_8061,const_8062,var_8064,bop_8067,])
F = relay.Function([var_8031,var_8048,var_8061,var_8063,var_8064,var_8066,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_8031,var_8048,var_8061,var_8063,var_8064,var_8066,], output2)
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
