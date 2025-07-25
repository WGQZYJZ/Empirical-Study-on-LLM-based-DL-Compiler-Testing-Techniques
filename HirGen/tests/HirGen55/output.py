import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_138 = relay.var("var_138", dtype = "uint32", shape = (8, 5, 14))#candidate|138|(8, 5, 14)|var|uint32
var_139 = relay.var("var_139", dtype = "uint32", shape = (8, 5, 14))#candidate|139|(8, 5, 14)|var|uint32
bop_140 = relay.logical_xor(var_138.astype('uint32'), relay.reshape(var_139.astype('uint32'), relay.shape_of(var_138))) # shape=(8, 5, 14)
output = bop_140
output2 = bop_140
func_147 = relay.Function([var_138,var_139,], output)
mod['func_147'] = func_147
mod = relay.transform.InferType()(mod)
mutated_mod['func_147'] = func_147
mutated_mod = relay.transform.InferType()(mutated_mod)
func_147_call = mutated_mod.get_global_var('func_147')
var_149 = relay.var("var_149", dtype = "uint32", shape = (8, 5, 14))#candidate|149|(8, 5, 14)|var|uint32
var_150 = relay.var("var_150", dtype = "uint32", shape = (8, 5, 14))#candidate|150|(8, 5, 14)|var|uint32
call_148 = func_147_call(var_149,var_150,)
output = call_148
func_151 = relay.Function([var_149,var_150,], output)
mutated_mod['func_151'] = func_151
mutated_mod = relay.transform.InferType()(mutated_mod)
const_290 = relay.const(-3.652693, dtype = "float32")#candidate|290|()|const|float32
var_291 = relay.var("var_291", dtype = "float32", shape = (16, 1, 4))#candidate|291|(16, 1, 4)|var|float32
bop_292 = relay.less_equal(const_290.astype('bool'), var_291.astype('bool')) # shape=(16, 1, 4)
output = relay.Tuple([bop_292,])
output2 = relay.Tuple([bop_292,])
func_312 = relay.Function([var_291,], output)
mod['func_312'] = func_312
mod = relay.transform.InferType()(mod)
var_313 = relay.var("var_313", dtype = "float32", shape = (16, 1, 4))#candidate|313|(16, 1, 4)|var|float32
output = func_312(var_313)
func_314 = relay.Function([var_313], output)
mutated_mod['func_314'] = func_314
mutated_mod = relay.transform.InferType()(mutated_mod)
var_423 = relay.var("var_423", dtype = "float64", shape = (6, 12, 4))#candidate|423|(6, 12, 4)|var|float64
uop_424 = relay.acos(var_423.astype('float64')) # shape=(6, 12, 4)
output = uop_424
output2 = uop_424
func_426 = relay.Function([var_423,], output)
mod['func_426'] = func_426
mod = relay.transform.InferType()(mod)
mutated_mod['func_426'] = func_426
mutated_mod = relay.transform.InferType()(mutated_mod)
var_427 = relay.var("var_427", dtype = "float64", shape = (6, 12, 4))#candidate|427|(6, 12, 4)|var|float64
func_426_call = mutated_mod.get_global_var('func_426')
call_428 = func_426_call(var_427)
output = call_428
func_429 = relay.Function([var_427], output)
mutated_mod['func_429'] = func_429
mutated_mod = relay.transform.InferType()(mutated_mod)
const_434 = relay.const([[[6,2],[2,-10],[7,3],[4,9],[3,4],[7,-8],[10,7],[-10,6],[4,1],[8,-1],[5,-8],[7,-9]],[[-5,8],[3,-6],[-10,1],[-3,-8],[-4,3],[10,-6],[-7,6],[-10,-6],[9,10],[2,5],[10,-1],[-2,1]]], dtype = "uint16")#candidate|434|(2, 12, 2)|const|uint16
var_435 = relay.var("var_435", dtype = "uint16", shape = (2, 12, 2))#candidate|435|(2, 12, 2)|var|uint16
bop_436 = relay.right_shift(const_434.astype('uint16'), relay.reshape(var_435.astype('uint16'), relay.shape_of(const_434))) # shape=(2, 12, 2)
output = relay.Tuple([bop_436,])
output2 = relay.Tuple([bop_436,])
func_441 = relay.Function([var_435,], output)
mod['func_441'] = func_441
mod = relay.transform.InferType()(mod)
mutated_mod['func_441'] = func_441
mutated_mod = relay.transform.InferType()(mutated_mod)
var_442 = relay.var("var_442", dtype = "uint16", shape = (2, 12, 2))#candidate|442|(2, 12, 2)|var|uint16
func_441_call = mutated_mod.get_global_var('func_441')
call_443 = func_441_call(var_442)
output = call_443
func_444 = relay.Function([var_442], output)
mutated_mod['func_444'] = func_444
mutated_mod = relay.transform.InferType()(mutated_mod)
var_537 = relay.var("var_537", dtype = "bool", shape = (6, 2, 1))#candidate|537|(6, 2, 1)|var|bool
const_538 = relay.const([[[False,False,False,True,False,True,True,False,True],[True,False,False,True,False,False,False,True,True]],[[False,True,False,True,True,False,False,False,True],[False,True,True,False,True,False,False,True,False]],[[True,False,False,True,True,True,True,True,True],[True,True,True,False,True,False,True,True,True]],[[True,True,False,False,False,True,True,False,False],[True,True,True,False,False,False,False,True,True]],[[True,False,False,True,True,False,False,False,True],[False,True,False,False,False,False,False,False,False]],[[True,True,False,True,True,True,True,True,False],[True,True,True,False,True,False,True,False,True]]], dtype = "bool")#candidate|538|(6, 2, 9)|const|bool
bop_539 = relay.logical_or(var_537.astype('bool'), const_538.astype('bool')) # shape=(6, 2, 9)
uop_556 = relay.sigmoid(var_537.astype('float64')) # shape=(6, 2, 1)
uop_558 = relay.rsqrt(uop_556.astype('float32')) # shape=(6, 2, 1)
uop_560 = relay.erf(uop_558.astype('float32')) # shape=(6, 2, 1)
func_147_call = mod.get_global_var('func_147')
func_151_call = mutated_mod.get_global_var('func_151')
var_564 = relay.var("var_564", dtype = "uint32", shape = (560,))#candidate|564|(560,)|var|uint32
call_563 = func_147_call(relay.reshape(var_564.astype('uint32'), [8, 5, 14]), relay.reshape(var_564.astype('uint32'), [8, 5, 14]), )
call_565 = func_147_call(relay.reshape(var_564.astype('uint32'), [8, 5, 14]), relay.reshape(var_564.astype('uint32'), [8, 5, 14]), )
bop_570 = relay.logical_xor(uop_560.astype('int32'), bop_539.astype('int32')) # shape=(6, 2, 9)
uop_574 = relay.acos(uop_560.astype('float32')) # shape=(6, 2, 1)
func_147_call = mod.get_global_var('func_147')
func_151_call = mutated_mod.get_global_var('func_151')
call_603 = func_147_call(relay.reshape(var_564.astype('uint32'), [8, 5, 14]), relay.reshape(var_564.astype('uint32'), [8, 5, 14]), )
call_604 = func_147_call(relay.reshape(var_564.astype('uint32'), [8, 5, 14]), relay.reshape(var_564.astype('uint32'), [8, 5, 14]), )
output = relay.Tuple([call_563,var_564,bop_570,uop_574,call_603,])
output2 = relay.Tuple([call_565,var_564,bop_570,uop_574,call_604,])
func_607 = relay.Function([var_537,var_564,], output)
mod['func_607'] = func_607
mod = relay.transform.InferType()(mod)
mutated_mod['func_607'] = func_607
mutated_mod = relay.transform.InferType()(mutated_mod)
func_607_call = mutated_mod.get_global_var('func_607')
var_609 = relay.var("var_609", dtype = "bool", shape = (6, 2, 1))#candidate|609|(6, 2, 1)|var|bool
var_610 = relay.var("var_610", dtype = "uint32", shape = (560,))#candidate|610|(560,)|var|uint32
call_608 = func_607_call(var_609,var_610,)
output = call_608
func_611 = relay.Function([var_609,var_610,], output)
mutated_mod['func_611'] = func_611
mutated_mod = relay.transform.InferType()(mutated_mod)
const_774 = relay.const([[[10,4,3,-6,4,-9,-9,-6,3,5,4,4,-6,2,3,-10],[9,10,-7,1,6,10,7,6,-7,-8,5,-10,3,6,3,-10],[-1,-6,-9,-2,9,2,9,7,-7,8,9,4,3,7,-6,-2],[-9,7,-7,3,-2,-3,-3,8,7,3,-7,7,6,8,3,1],[8,10,-7,-1,-9,10,5,3,8,-8,-4,-7,-9,6,-4,-3],[-7,6,-5,-2,1,8,4,10,9,8,-2,-6,9,2,9,4],[8,9,-8,10,5,-9,-7,-2,6,-10,5,1,5,5,-7,-9]],[[10,-8,9,10,-4,-4,8,9,-5,4,4,2,-7,3,-6,10],[-10,-4,6,2,5,-5,1,-8,-3,-6,6,-6,7,-10,4,8],[-6,-1,-10,-4,-9,7,3,10,-8,2,-6,-10,10,3,7,5],[8,8,1,1,3,3,5,-1,-10,8,1,-7,5,-6,3,-8],[9,7,9,9,-9,-5,6,9,9,9,5,-3,-6,-5,-10,2],[-8,-9,-8,-7,3,-3,-8,-2,-10,-8,-7,-5,8,5,-4,7],[-5,-9,7,2,-9,-6,7,-5,10,-2,-4,3,-9,-2,-3,-5]],[[7,1,-1,1,-10,-1,6,-4,9,7,-4,-5,-7,6,-8,-8],[6,-9,4,8,-9,-3,-5,5,-2,7,-1,9,-1,-7,7,-4],[-7,-3,-4,-7,2,-10,-4,2,5,3,4,-3,-8,-6,8,-9],[4,7,3,-3,-1,-1,-7,-4,2,8,1,3,-6,6,2,8],[-9,5,9,8,-8,9,-2,8,2,4,-1,-3,-7,-8,4,4],[-3,7,5,-5,2,10,9,-2,6,-2,-2,-4,4,7,-10,-3],[-1,6,-4,1,-7,2,1,-4,-9,-5,-3,-9,1,-7,8,-5]],[[-10,3,3,2,6,-5,9,7,-8,-6,-1,10,-10,2,-6,-4],[-7,-10,4,-10,7,1,-7,-1,-1,5,-3,-6,3,10,-7,8],[5,6,-2,-2,-4,-3,9,5,3,4,7,1,-7,9,-7,-8],[5,-4,10,3,6,6,-2,-5,-1,2,-6,9,-6,-7,-5,7],[-9,-6,4,-5,-7,-6,-10,-5,10,2,-2,1,-7,-3,3,2],[-1,-1,10,-7,-6,8,-6,8,2,-5,-9,2,-7,10,-5,2],[-3,-2,8,1,-4,10,2,7,-8,-8,-1,4,-5,7,-9,5]],[[1,-8,-7,-5,-8,1,2,1,2,-8,-10,-10,7,5,8,1],[-7,2,-7,-3,1,4,3,7,7,-10,-6,-3,2,2,-8,-1],[3,7,10,5,-5,7,4,-7,7,-7,-10,9,-6,1,-5,9],[6,8,-7,7,1,1,-8,-6,6,2,-4,9,2,-6,-4,3],[-10,-4,-3,8,-5,-9,9,-9,-9,-2,-4,2,3,-2,-2,5],[-7,8,9,4,-5,8,8,-1,-2,9,6,-1,9,5,8,3],[10,5,-7,7,2,8,-5,-9,3,-3,9,-7,-5,2,-6,-9]],[[6,8,-5,-5,-10,-8,-1,-2,-5,3,-8,4,5,-9,1,-7],[-3,10,10,4,-8,5,-1,4,-3,-2,9,6,-4,-7,4,3],[1,-7,9,-2,-6,-8,5,5,-1,1,-6,8,-4,6,2,-7],[-3,5,6,10,-4,10,-2,-9,3,7,-9,-9,1,-10,7,8],[-10,3,-10,-9,-3,8,-6,-10,-7,10,1,8,5,7,-5,-1],[7,2,-8,6,2,7,-10,-8,-6,-4,8,-1,10,-6,-2,-10],[4,10,5,-3,7,6,9,-6,-2,1,2,6,9,-7,-2,2]],[[10,-6,-8,-1,-9,4,-1,-2,-1,-7,-5,5,7,-7,-2,3],[-2,7,7,7,-5,5,-3,10,-10,-7,2,-2,-5,-5,9,8],[-6,3,5,1,-3,7,-3,-10,-6,1,8,-6,-2,1,-9,-5],[4,-8,2,-10,-6,-10,5,-4,-8,10,8,-10,-5,4,-10,8],[-8,4,6,4,-10,-10,6,-8,1,-2,-4,-9,-3,-4,1,8],[8,9,5,-3,10,10,9,2,-7,-9,7,9,-1,3,-5,-3],[-3,7,6,3,-3,-3,4,-2,-10,-2,-9,6,-4,-3,-2,-3]],[[9,-4,-10,-10,-3,-7,8,8,10,-4,-10,8,9,-4,8,-7],[5,-1,-8,8,-3,6,4,-9,3,3,4,-7,5,-6,-7,9],[4,-7,-8,-4,9,4,6,-8,-9,-10,4,-7,-9,9,8,7],[7,-4,8,8,8,3,-7,2,-5,10,2,-6,4,6,-5,-4],[9,-9,-6,6,-1,9,-3,-6,5,-6,5,7,-1,-1,-8,-1],[3,-3,7,4,-2,7,-5,-4,9,7,-5,-3,-9,-3,9,5],[-3,2,10,7,-8,9,-7,4,-4,10,-5,-6,-7,-3,-2,-10]],[[-9,-5,8,-2,6,2,4,-9,-6,10,2,-8,-6,5,1,4],[-6,8,-3,-2,4,4,9,8,2,9,-7,-3,9,-2,-3,-2],[-7,5,-5,-1,-1,6,-8,-5,4,2,-10,4,-3,4,5,5],[10,-4,-8,-1,1,1,4,10,10,9,9,3,-10,-7,5,-8],[3,10,-8,2,-10,1,-9,-2,-4,-10,2,4,10,-6,-5,-2],[6,-2,6,-6,-7,2,7,-4,5,-2,5,1,-7,-2,3,1],[-9,8,8,-4,8,-10,10,-5,-8,-3,3,10,-5,2,-8,1]],[[-9,3,-10,2,-2,4,8,8,8,-9,-7,1,-3,2,-10,-1],[2,6,-10,2,3,-4,7,7,3,-4,-4,6,2,9,1,-10],[-5,-6,5,6,4,-10,-4,-4,-10,-9,7,-4,-3,10,-4,-8],[-7,3,-2,1,-1,-7,-6,3,-3,-2,10,-1,8,1,-2,-10],[-5,8,-4,-3,9,-1,3,3,-8,8,1,-3,1,-3,-2,9],[-8,3,7,8,-8,-1,4,-8,-8,-10,-6,-2,-6,-7,9,-6],[-4,-2,6,4,-10,-4,-8,-9,-1,-7,-4,3,5,-8,7,-5]],[[4,-1,-7,4,-2,6,-1,8,3,-8,-6,9,-2,-8,-3,-9],[8,5,6,7,-8,-8,5,2,3,7,4,1,-2,-6,-9,2],[-4,5,8,8,2,-6,1,-6,-1,-2,-10,-10,1,7,-10,7],[6,6,5,-10,9,5,8,-2,8,-4,6,-9,2,9,7,-8],[10,-8,7,4,-6,3,4,-2,1,9,2,6,-5,5,-1,-4],[-6,-5,-10,8,10,1,7,4,-9,-7,2,4,6,-1,2,-9],[-10,3,5,-8,-3,9,-2,9,-8,6,-8,9,-10,3,6,2]],[[8,7,-5,8,-4,9,2,1,4,9,-8,8,-9,-1,6,-2],[-7,8,4,1,5,-7,-9,6,-8,5,-3,3,5,10,7,6],[3,-7,9,8,-1,-10,5,-2,-9,8,-10,-8,5,8,2,-6],[-7,-1,-3,2,-5,-2,6,-1,1,-1,-10,-9,8,5,-3,-4],[-3,1,-5,-10,5,1,8,-10,-1,1,1,6,-1,-1,1,-9],[2,10,2,10,-2,3,-2,10,-6,-7,-2,10,4,-10,-7,-1],[8,8,1,-1,6,-4,9,-2,-4,-5,1,-4,5,2,-2,4]],[[-4,3,-2,-2,-10,-7,-10,-5,-1,5,-4,-9,-2,4,5,7],[10,-7,-6,-1,5,5,-10,-4,-1,-2,-7,-5,-1,-4,-6,-6],[-10,-9,1,-3,9,-4,8,-1,-8,-3,4,-5,-6,-3,-9,-7],[3,-7,7,3,-8,6,-6,7,9,-8,-8,10,-1,4,-2,-2],[8,-9,7,-4,8,3,8,7,-7,-10,7,9,-1,-9,6,7],[-1,1,-8,-5,5,-2,5,10,-4,9,10,-1,-10,5,-4,-2],[-1,-2,-9,7,4,-9,-9,-5,1,4,1,-4,6,1,-4,-2]],[[5,5,-1,-8,-4,-6,-5,-5,4,-8,3,-9,3,-8,10,-3],[-5,1,-1,-3,-5,7,9,-8,9,9,10,-2,6,2,-9,-5],[3,10,-2,-10,-1,8,-9,2,-4,2,9,-9,-4,-4,-5,-7],[2,2,-2,2,-9,5,1,-6,8,-9,1,-5,10,-10,-6,-3],[6,-4,-8,-4,-9,3,-6,-4,-6,-3,-2,4,8,7,2,-2],[-5,-9,-3,10,-1,3,-1,-4,-10,5,-7,-6,-4,-7,-4,7],[5,2,2,-1,2,-2,1,-1,-5,6,9,5,6,-2,-2,10]],[[8,7,-2,2,-4,-9,2,-9,10,7,7,3,-5,-4,7,-6],[3,-4,6,1,2,-9,1,9,1,-1,9,2,2,-3,-7,3],[-6,5,2,-4,-5,7,10,9,4,-10,7,-9,7,7,4,-3],[6,-2,3,3,10,-8,-7,-2,9,8,-5,7,10,5,4,4],[-8,-8,-4,-3,-2,5,-7,4,10,-4,-8,4,-4,2,8,8],[4,-7,9,-5,10,-10,-6,5,-6,-10,1,-2,2,5,-10,6],[-10,-4,-4,10,8,2,-6,-1,-5,5,-4,3,1,-6,10,6]],[[-6,1,-1,3,-10,-5,-10,-9,9,3,10,-9,-3,-3,6,4],[-4,-9,5,4,7,-4,-8,-5,8,10,5,1,4,-2,-7,-2],[3,-4,5,6,9,-10,4,6,3,-1,5,6,-10,-10,7,6],[5,-6,1,-2,-3,-9,-8,-8,5,1,3,-1,-6,-10,5,2],[-7,10,-2,8,5,-10,-6,-5,-10,-1,4,6,3,4,1,9],[4,-7,2,-2,5,-1,2,2,-2,7,-4,-7,-10,-6,5,-10],[-5,-5,-2,-5,9,-8,3,5,2,3,-4,7,-1,6,10,-7]]], dtype = "int64")#candidate|774|(16, 7, 16)|const|int64
var_775 = relay.var("var_775", dtype = "int64", shape = (16, 7, 16))#candidate|775|(16, 7, 16)|var|int64
bop_776 = relay.bitwise_and(const_774.astype('int64'), relay.reshape(var_775.astype('int64'), relay.shape_of(const_774))) # shape=(16, 7, 16)
uop_779 = relay.exp(var_775.astype('float32')) # shape=(16, 7, 16)
func_607_call = mod.get_global_var('func_607')
func_611_call = mutated_mod.get_global_var('func_611')
var_801 = relay.var("var_801", dtype = "bool", shape = (12,))#candidate|801|(12,)|var|bool
const_802 = relay.const([-5,6,2,9,-1,8,9,-7,9,2,3,4,5,5,6,-4,6,-10,10,-10,6,-5,2,-5,-9,4,5,6,-1,-1,-2,8,5,-6,-9,-5,4,9,-3,-9,-1,4,1,4,-4,9,-2,-4,4,3,6,-10,10,-6,-2,-5,8,-9,-1,10,-9,-1,-5,1,5,-5,-6,1,2,8,4,9,5,10,-2,-3,-9,-4,-1,4,-1,-7,3,2,5,1,5,1,9,-6,-4,-2,5,-7,-4,-4,-9,-3,-9,8,-7,3,-1,4,8,1,-10,6,2,4,2,1,7,2,9,1,-8,-9,-1,-1,4,-4,8,10,1,5,1,7,-10,-5,-10,8,-3,9,2,6,1,-10,7,-8,-5,-4,-1,-6,9,-1,-2,-6,-7,-10,4,-3,-5,3,-3,2,4,-6,-8,-7,6,7,8,-4,10,-4,-9,9,-9,7,3,-2,9,3,2,6,7,-7,-7,-10,4,-1,-10,-6,3,3,-7,7,6,-3,8,-6,1,10,4,-6,1,-1,10,-1,5,10,-10,-5,-7,-5,-8,-1,-6,-8,10,-1,1,-3,-1,3,8,-7,-2,-7,3,-3,-2,-7,-3,1,8,6,3,-10,4,2,1,-2,-2,-2,-10,-3,7,-1,6,8,1,5,3,-10,-3,1,-2,6,4,8,-1,4,-2,2,6,-3,-4,-5,-6,-8,-7,-10,3,-2,4,-1,-10,6,-2,1,-8,7,3,-1,-6,5,-7,4,-2,9,6,-2,-4,10,7,-4,-6,-7,2,7,6,-3,8,6,-4,6,2,-10,-6,-4,2,8,-8,4,-4,10,-2,4,8,1,-5,-4,7,-5,4,6,7,1,-10,9,-7,-3,-10,2,8,-2,10,-10,-9,10,6,9,-9,-1,9,-2,-9,-7,1,-8,3,-2,7,-8,8,-2,-3,6,-3,-2,8,-9,8,-5,7,9,-5,-3,-2,-1,-8,-3,-3,-4,7,-9,9,-2,-5,-7,2,2,-7,-2,-3,-7,3,3,-10,-2,-2,-4,8,7,6,-4,2,-8,1,7,-2,-7,6,-2,-5,-7,-5,8,-8,-5,-3,-5,-6,-3,4,1,6,-2,7,3,8,1,-1,-7,5,5,2,10,-6,7,5,-9,-7,7,3,-8,-10,-4,-5,1,-4,8,10,-6,-3,8,10,-10,8,-10,7,-4,6,-7,-9,-3,-7,-9,-8,-3,7,-10,-9,-5,-10,-10,5,-4,-1,4,-3,5,9,-7,10,-8,3,7,10,1,-10,-5,-4,-8,3,-7,10,-6,-7,-7,-5,5,5,-10,-5,-3,1,-10,10,-9,1,-9,7,1,10,-10,-3,3,-6,-10,-5,4,2,2,-1,5,7,2,-3,8,10,-8,-5,-8,-5,2,3,5,-1,5,8,-3,-6,-10,9,-2,-8,-2,3,-1,-8,8,10,-7,2,10,-4,6,-1,10,-4,9,-5,4,10,-6,-10,-2,-10,9,10,4,4,5,4,-5,8,-10], dtype = "uint32")#candidate|802|(560,)|const|uint32
call_800 = relay.TupleGetItem(func_607_call(relay.reshape(var_801.astype('bool'), [6, 2, 1]), relay.reshape(const_802.astype('uint32'), [560,]), ), 1)
call_803 = relay.TupleGetItem(func_611_call(relay.reshape(var_801.astype('bool'), [6, 2, 1]), relay.reshape(const_802.astype('uint32'), [560,]), ), 1)
output = relay.Tuple([bop_776,uop_779,call_800,var_801,const_802,])
output2 = relay.Tuple([bop_776,uop_779,call_803,var_801,const_802,])
func_812 = relay.Function([var_775,var_801,], output)
mod['func_812'] = func_812
mod = relay.transform.InferType()(mod)
var_813 = relay.var("var_813", dtype = "int64", shape = (16, 7, 16))#candidate|813|(16, 7, 16)|var|int64
var_814 = relay.var("var_814", dtype = "bool", shape = (12,))#candidate|814|(12,)|var|bool
output = func_812(var_813,var_814,)
func_815 = relay.Function([var_813,var_814,], output)
mutated_mod['func_815'] = func_815
mutated_mod = relay.transform.InferType()(mutated_mod)
var_822 = relay.var("var_822", dtype = "float32", shape = (9, 14, 16))#candidate|822|(9, 14, 16)|var|float32
uop_823 = relay.acos(var_822.astype('float32')) # shape=(9, 14, 16)
output = uop_823
output2 = uop_823
func_825 = relay.Function([var_822,], output)
mod['func_825'] = func_825
mod = relay.transform.InferType()(mod)
var_826 = relay.var("var_826", dtype = "float32", shape = (9, 14, 16))#candidate|826|(9, 14, 16)|var|float32
output = func_825(var_826)
func_827 = relay.Function([var_826], output)
mutated_mod['func_827'] = func_827
mutated_mod = relay.transform.InferType()(mutated_mod)
var_986 = relay.var("var_986", dtype = "uint64", shape = (7, 11, 3))#candidate|986|(7, 11, 3)|var|uint64
const_987 = relay.const([[[5,-10,1],[-7,3,6],[6,-4,-9],[-9,-6,2],[-7,9,10],[5,-2,-10],[-1,4,1],[-3,-6,-2],[-6,2,7],[7,-4,-3],[8,8,2]],[[-5,-9,8],[10,8,6],[1,-4,-6],[-6,-2,-9],[5,-2,-1],[2,-9,4],[-2,-9,-10],[-2,-1,-3],[5,1,-4],[-4,-10,-1],[-3,7,-6]],[[1,5,8],[-7,6,7],[6,-1,-3],[7,-3,6],[-10,-8,2],[7,-4,5],[8,4,-1],[-5,7,2],[-10,-7,-8],[8,-1,2],[-2,9,3]],[[-10,8,-7],[9,6,8],[7,-8,3],[-5,-1,-7],[2,-6,-7],[-4,2,-5],[1,-10,1],[8,8,-2],[2,-1,-6],[10,2,-6],[6,10,-2]],[[-8,-10,-1],[-8,8,-4],[6,10,1],[-10,3,-8],[2,10,2],[4,6,-10],[-4,-7,4],[-5,-9,10],[10,-2,1],[-3,-4,5],[-5,-7,3]],[[-8,-6,1],[8,2,10],[9,3,4],[-3,-9,10],[-4,2,-5],[-7,-4,-10],[4,-3,-7],[-8,3,-2],[-9,4,4],[1,8,-7],[8,8,6]],[[-9,9,-7],[-4,-3,-8],[4,9,-5],[-1,-9,10],[1,-10,2],[-10,8,-4],[4,-2,5],[-3,7,-8],[-7,9,-9],[3,-8,1],[-3,-2,8]]], dtype = "uint64")#candidate|987|(7, 11, 3)|const|uint64
bop_988 = relay.less(var_986.astype('bool'), relay.reshape(const_987.astype('bool'), relay.shape_of(var_986))) # shape=(7, 11, 3)
func_147_call = mod.get_global_var('func_147')
func_151_call = mutated_mod.get_global_var('func_151')
const_992 = relay.const([[-9,-1,-9,9,1,1,8,9,9,8,9,-4,6,1,-9,-2,-8,-5,5,10,-3,-3,6,-8,2,-8,-6,9,2,5,-3,-10,-1,5,-10,-1,5,-5,-7,-10,9,-9,-10,-6,-6,-6,7,9,2,3,6,-6,-9,6,3,5,3,4,10,-8,10,-7,-1,-4,-10,-6,10,-9,-2,-5,10,7,-1,7,-3,-2,-8,-8,5,5,-9,-4,-2,8,-10,8,-2,-1,8,-8,2,1,-9,10,-3,1,-5,-10,8,10,-2,7,-5,-9,-6,-1,-7,8,-3,9,-3,-7,5,-7,7,2,8,-7,8,6,-3,4,-1,-5,1,10,4,4,9,4,-9,-7,-6,9,-10,-9,4,-4,-6,-9],[3,-2,-1,6,-10,-5,-7,-5,9,-8,-1,-4,10,9,-7,2,-8,-6,-3,-8,-5,9,5,6,1,3,-8,-6,6,-4,-4,2,-3,2,1,6,-2,7,-2,-3,6,5,-4,-4,-8,3,7,5,-4,-3,-8,-10,-5,-10,-1,-7,1,-10,-5,-7,-3,5,6,7,9,-6,8,-7,-4,-7,10,-1,-8,-7,-7,5,5,-9,10,-10,9,-5,-3,-9,9,-1,4,9,-4,4,-1,1,-9,-6,10,1,3,6,8,2,-3,-6,6,8,6,-3,-1,2,7,-2,-5,6,-8,-5,-8,-4,1,-8,9,-8,8,-1,-6,-10,2,-9,4,8,-8,10,9,8,6,-8,-4,2,-10,10,8,8],[-5,-1,-6,2,-2,-1,6,3,-7,-9,-9,-2,7,-4,5,7,3,-8,-8,3,1,-3,5,-1,8,5,2,-8,-1,-4,-6,-6,-10,8,-5,8,-4,2,-6,4,-2,3,6,3,-6,4,9,-3,-4,-6,3,-4,-2,8,1,4,-9,-9,10,2,10,-2,-8,7,7,1,-5,6,-5,-5,-6,-2,-8,2,3,-4,10,2,-10,-9,10,6,9,5,6,-2,1,-9,-5,4,5,-10,5,-2,-1,-3,-5,8,-3,-9,3,1,-5,2,9,9,8,-8,3,10,-3,9,-4,-1,10,-5,-1,-8,7,8,7,-10,9,8,10,-8,-2,10,-3,-2,10,7,-4,-10,6,6,5,6,6,6],[1,10,10,-1,2,6,-1,-5,-10,5,-3,7,9,-2,7,-4,3,-2,-5,-5,-6,-2,4,3,4,-9,-9,7,-10,-6,6,-5,-3,1,2,8,7,-7,9,6,-6,-2,-1,-6,7,-8,-9,3,2,1,-10,-3,10,9,-10,3,-9,-4,6,-1,-9,10,-4,3,7,-1,4,3,6,1,6,-1,-3,-7,-4,-3,-7,-2,-6,-8,-10,1,3,-5,-7,-4,-4,-9,-1,-5,-3,9,-3,-3,-7,-1,10,-10,-7,3,-3,6,3,6,10,-10,-2,-4,-1,4,-8,4,9,2,-8,8,1,9,-7,-9,-8,9,9,5,-2,7,-3,9,-2,8,5,1,9,-1,7,-5,-10,-3,10,8]], dtype = "uint32")#candidate|992|(4, 140)|const|uint32
call_991 = func_147_call(relay.reshape(const_992.astype('uint32'), [8, 5, 14]), relay.reshape(const_992.astype('uint32'), [8, 5, 14]), )
call_993 = func_147_call(relay.reshape(const_992.astype('uint32'), [8, 5, 14]), relay.reshape(const_992.astype('uint32'), [8, 5, 14]), )
output = relay.Tuple([bop_988,call_991,const_992,])
output2 = relay.Tuple([bop_988,call_993,const_992,])
func_1023 = relay.Function([var_986,], output)
mod['func_1023'] = func_1023
mod = relay.transform.InferType()(mod)
mutated_mod['func_1023'] = func_1023
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1024 = relay.var("var_1024", dtype = "uint64", shape = (7, 11, 3))#candidate|1024|(7, 11, 3)|var|uint64
func_1023_call = mutated_mod.get_global_var('func_1023')
call_1025 = func_1023_call(var_1024)
output = call_1025
func_1026 = relay.Function([var_1024], output)
mutated_mod['func_1026'] = func_1026
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1196 = relay.var("var_1196", dtype = "float64", shape = (2, 3, 14))#candidate|1196|(2, 3, 14)|var|float64
uop_1197 = relay.erf(var_1196.astype('float64')) # shape=(2, 3, 14)
output = uop_1197
output2 = uop_1197
func_1205 = relay.Function([var_1196,], output)
mod['func_1205'] = func_1205
mod = relay.transform.InferType()(mod)
var_1206 = relay.var("var_1206", dtype = "float64", shape = (2, 3, 14))#candidate|1206|(2, 3, 14)|var|float64
output = func_1205(var_1206)
func_1207 = relay.Function([var_1206], output)
mutated_mod['func_1207'] = func_1207
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1371 = relay.var("var_1371", dtype = "float32", shape = ())#candidate|1371|()|var|float32
var_1372 = relay.var("var_1372", dtype = "float32", shape = (11, 8, 8))#candidate|1372|(11, 8, 8)|var|float32
bop_1373 = relay.floor_mod(var_1371.astype('float32'), var_1372.astype('float32')) # shape=(11, 8, 8)
uop_1384 = relay.sin(bop_1373.astype('float32')) # shape=(11, 8, 8)
output = uop_1384
output2 = uop_1384
func_1386 = relay.Function([var_1371,var_1372,], output)
mod['func_1386'] = func_1386
mod = relay.transform.InferType()(mod)
mutated_mod['func_1386'] = func_1386
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1386_call = mutated_mod.get_global_var('func_1386')
var_1388 = relay.var("var_1388", dtype = "float32", shape = ())#candidate|1388|()|var|float32
var_1389 = relay.var("var_1389", dtype = "float32", shape = (11, 8, 8))#candidate|1389|(11, 8, 8)|var|float32
call_1387 = func_1386_call(var_1388,var_1389,)
output = call_1387
func_1390 = relay.Function([var_1388,var_1389,], output)
mutated_mod['func_1390'] = func_1390
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1768 = relay.var("var_1768", dtype = "int32", shape = (4, 5, 13))#candidate|1768|(4, 5, 13)|var|int32
var_1769 = relay.var("var_1769", dtype = "int32", shape = (4, 5, 13))#candidate|1769|(4, 5, 13)|var|int32
bop_1770 = relay.not_equal(var_1768.astype('bool'), relay.reshape(var_1769.astype('bool'), relay.shape_of(var_1768))) # shape=(4, 5, 13)
output = relay.Tuple([bop_1770,])
output2 = relay.Tuple([bop_1770,])
func_1774 = relay.Function([var_1768,var_1769,], output)
mod['func_1774'] = func_1774
mod = relay.transform.InferType()(mod)
var_1775 = relay.var("var_1775", dtype = "int32", shape = (4, 5, 13))#candidate|1775|(4, 5, 13)|var|int32
var_1776 = relay.var("var_1776", dtype = "int32", shape = (4, 5, 13))#candidate|1776|(4, 5, 13)|var|int32
output = func_1774(var_1775,var_1776,)
func_1777 = relay.Function([var_1775,var_1776,], output)
mutated_mod['func_1777'] = func_1777
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1965 = relay.const([[[-4,-2,-3,-4,9,9,-4,1,-2,-2,7,-2,2,-6,5,10]],[[4,-6,-10,6,-10,5,1,-2,9,9,-6,2,2,8,7,7]],[[-1,-10,7,10,-10,3,-3,6,3,-9,-6,-6,1,8,-3,1]],[[9,-4,-7,6,-9,1,-8,-7,4,-9,-9,1,-10,-7,-3,4]],[[8,-10,2,4,-9,-5,-2,7,8,-8,-2,6,5,2,2,2]],[[3,4,-10,-9,3,-5,6,-3,-9,-3,8,-2,3,-3,-1,4]],[[6,1,8,6,-4,6,-2,-4,10,3,-7,10,-10,-6,9,7]],[[9,3,8,9,-10,-9,6,5,-3,3,-3,1,-8,-6,-10,-4]],[[1,-8,-7,-10,-4,1,-4,-5,7,8,-2,5,7,-7,-4,-8]],[[8,-1,-3,-2,-2,6,-1,5,-10,10,-2,-10,-6,-6,7,3]],[[-9,10,7,-8,7,7,6,8,2,6,2,-5,-6,-7,6,-10]],[[-6,7,-4,-4,-1,-3,-4,-3,-6,2,-6,6,-7,-6,-5,-8]],[[-7,-6,-9,6,-5,7,7,-6,8,2,-5,7,-1,5,-9,7]]], dtype = "uint8")#candidate|1965|(13, 1, 16)|const|uint8
var_1966 = relay.var("var_1966", dtype = "uint8", shape = (13, 13, 16))#candidate|1966|(13, 13, 16)|var|uint8
bop_1967 = relay.bitwise_xor(const_1965.astype('uint8'), var_1966.astype('uint8')) # shape=(13, 13, 16)
uop_1974 = relay.atanh(const_1965.astype('float64')) # shape=(13, 1, 16)
output = relay.Tuple([bop_1967,uop_1974,])
output2 = relay.Tuple([bop_1967,uop_1974,])
func_1977 = relay.Function([var_1966,], output)
mod['func_1977'] = func_1977
mod = relay.transform.InferType()(mod)
mutated_mod['func_1977'] = func_1977
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1978 = relay.var("var_1978", dtype = "uint8", shape = (13, 13, 16))#candidate|1978|(13, 13, 16)|var|uint8
func_1977_call = mutated_mod.get_global_var('func_1977')
call_1979 = func_1977_call(var_1978)
output = call_1979
func_1980 = relay.Function([var_1978], output)
mutated_mod['func_1980'] = func_1980
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2078 = relay.var("var_2078", dtype = "float32", shape = (6, 9, 8))#candidate|2078|(6, 9, 8)|var|float32
uop_2079 = relay.asin(var_2078.astype('float32')) # shape=(6, 9, 8)
uop_2082 = relay.log10(uop_2079.astype('float32')) # shape=(6, 9, 8)
uop_2111 = relay.log2(uop_2082.astype('float32')) # shape=(6, 9, 8)
output = uop_2111
output2 = uop_2111
func_2124 = relay.Function([var_2078,], output)
mod['func_2124'] = func_2124
mod = relay.transform.InferType()(mod)
mutated_mod['func_2124'] = func_2124
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2125 = relay.var("var_2125", dtype = "float32", shape = (6, 9, 8))#candidate|2125|(6, 9, 8)|var|float32
func_2124_call = mutated_mod.get_global_var('func_2124')
call_2126 = func_2124_call(var_2125)
output = call_2126
func_2127 = relay.Function([var_2125], output)
mutated_mod['func_2127'] = func_2127
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2270 = relay.var("var_2270", dtype = "int8", shape = (9, 3, 7))#candidate|2270|(9, 3, 7)|var|int8
var_2271 = relay.var("var_2271", dtype = "int8", shape = (9, 3, 7))#candidate|2271|(9, 3, 7)|var|int8
bop_2272 = relay.add(var_2270.astype('int8'), relay.reshape(var_2271.astype('int8'), relay.shape_of(var_2270))) # shape=(9, 3, 7)
uop_2280 = relay.log10(var_2270.astype('float64')) # shape=(9, 3, 7)
func_825_call = mod.get_global_var('func_825')
func_827_call = mutated_mod.get_global_var('func_827')
var_2291 = relay.var("var_2291", dtype = "float32", shape = (2016,))#candidate|2291|(2016,)|var|float32
call_2290 = func_825_call(relay.reshape(var_2291.astype('float32'), [9, 14, 16]))
call_2292 = func_825_call(relay.reshape(var_2291.astype('float32'), [9, 14, 16]))
bop_2295 = relay.bitwise_and(uop_2280.astype('int8'), relay.reshape(var_2270.astype('int8'), relay.shape_of(uop_2280))) # shape=(9, 3, 7)
func_441_call = mod.get_global_var('func_441')
func_444_call = mutated_mod.get_global_var('func_444')
const_2304 = relay.const([-1,9,5,7,-3,-7,1,9,5,8,-4,2,-1,5,4,-2,-10,8,-5,3,5,4,10,-3,3,8,-10,-7,3,-10,7,5,-3,5,7,3,10,7,-3,6,4,3,-4,2,6,8,4,-3], dtype = "uint16")#candidate|2304|(48,)|const|uint16
call_2303 = relay.TupleGetItem(func_441_call(relay.reshape(const_2304.astype('uint16'), [2, 12, 2])), 0)
call_2305 = relay.TupleGetItem(func_444_call(relay.reshape(const_2304.astype('uint16'), [2, 12, 2])), 0)
func_607_call = mod.get_global_var('func_607')
func_611_call = mutated_mod.get_global_var('func_611')
const_2319 = relay.const([True,True,True,False,False,True,False,True,False,False,False,False], dtype = "bool")#candidate|2319|(12,)|const|bool
var_2320 = relay.var("var_2320", dtype = "uint32", shape = (560,))#candidate|2320|(560,)|var|uint32
call_2318 = relay.TupleGetItem(func_607_call(relay.reshape(const_2319.astype('bool'), [6, 2, 1]), relay.reshape(var_2320.astype('uint32'), [560,]), ), 3)
call_2321 = relay.TupleGetItem(func_611_call(relay.reshape(const_2319.astype('bool'), [6, 2, 1]), relay.reshape(var_2320.astype('uint32'), [560,]), ), 3)
func_607_call = mod.get_global_var('func_607')
func_611_call = mutated_mod.get_global_var('func_611')
call_2326 = relay.TupleGetItem(func_607_call(relay.reshape(const_2319.astype('bool'), [6, 2, 1]), relay.reshape(var_2320.astype('uint32'), [560,]), ), 1)
call_2327 = relay.TupleGetItem(func_611_call(relay.reshape(const_2319.astype('bool'), [6, 2, 1]), relay.reshape(var_2320.astype('uint32'), [560,]), ), 1)
output = relay.Tuple([bop_2272,call_2290,var_2291,bop_2295,call_2303,const_2304,call_2318,const_2319,var_2320,call_2326,])
output2 = relay.Tuple([bop_2272,call_2292,var_2291,bop_2295,call_2305,const_2304,call_2321,const_2319,var_2320,call_2327,])
func_2329 = relay.Function([var_2270,var_2271,var_2291,var_2320,], output)
mod['func_2329'] = func_2329
mod = relay.transform.InferType()(mod)
mutated_mod['func_2329'] = func_2329
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2329_call = mutated_mod.get_global_var('func_2329')
var_2331 = relay.var("var_2331", dtype = "int8", shape = (9, 3, 7))#candidate|2331|(9, 3, 7)|var|int8
var_2332 = relay.var("var_2332", dtype = "int8", shape = (9, 3, 7))#candidate|2332|(9, 3, 7)|var|int8
var_2333 = relay.var("var_2333", dtype = "float32", shape = (2016,))#candidate|2333|(2016,)|var|float32
var_2334 = relay.var("var_2334", dtype = "uint32", shape = (560,))#candidate|2334|(560,)|var|uint32
call_2330 = func_2329_call(var_2331,var_2332,var_2333,var_2334,)
output = call_2330
func_2335 = relay.Function([var_2331,var_2332,var_2333,var_2334,], output)
mutated_mod['func_2335'] = func_2335
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2447 = relay.var("var_2447", dtype = "int32", shape = (9, 13, 10))#candidate|2447|(9, 13, 10)|var|int32
var_2448 = relay.var("var_2448", dtype = "int32", shape = (9, 13, 10))#candidate|2448|(9, 13, 10)|var|int32
bop_2449 = relay.equal(var_2447.astype('bool'), relay.reshape(var_2448.astype('bool'), relay.shape_of(var_2447))) # shape=(9, 13, 10)
output = relay.Tuple([bop_2449,])
output2 = relay.Tuple([bop_2449,])
func_2458 = relay.Function([var_2447,var_2448,], output)
mod['func_2458'] = func_2458
mod = relay.transform.InferType()(mod)
var_2459 = relay.var("var_2459", dtype = "int32", shape = (9, 13, 10))#candidate|2459|(9, 13, 10)|var|int32
var_2460 = relay.var("var_2460", dtype = "int32", shape = (9, 13, 10))#candidate|2460|(9, 13, 10)|var|int32
output = func_2458(var_2459,var_2460,)
func_2461 = relay.Function([var_2459,var_2460,], output)
mutated_mod['func_2461'] = func_2461
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2591 = relay.var("var_2591", dtype = "float64", shape = ())#candidate|2591|()|var|float64
var_2592 = relay.var("var_2592", dtype = "float64", shape = (7, 15, 14))#candidate|2592|(7, 15, 14)|var|float64
bop_2593 = relay.power(var_2591.astype('float64'), var_2592.astype('float64')) # shape=(7, 15, 14)
func_1205_call = mod.get_global_var('func_1205')
func_1207_call = mutated_mod.get_global_var('func_1207')
var_2600 = relay.var("var_2600", dtype = "float64", shape = (84,))#candidate|2600|(84,)|var|float64
call_2599 = func_1205_call(relay.reshape(var_2600.astype('float64'), [2, 3, 14]))
call_2601 = func_1205_call(relay.reshape(var_2600.astype('float64'), [2, 3, 14]))
func_2329_call = mod.get_global_var('func_2329')
func_2335_call = mutated_mod.get_global_var('func_2335')
const_2614 = relay.const([5,7,3,3,-7,-6,-9,-3,8,-1,-2,-8,3,2,9,5,7,-9,-3,-8,3,5,2,5,1,8,4,-10,1,-8,1,-4,5,-9,-8,-3,2,2,-5,3,-2,-1,-7,5,3,6,-9,4,-4,4,-1,-2,4,-6,-1,-7,2,-1,-1,6,-2,-9,3,-4,-6,10,5,10,-7,10,-9,-3,5,1,2,9,10,-4,-1,1,-7,7,-6,-3,7,-3,10,-9,-9,10,-8,5,7,2,-8,-9,5,-10,3,3,9,-6,1,-6,6,2,-5,1,-8,1,-5,2,-6,-10,-8,-9,-1,7,-2,4,7,9,5,-5,10,-1,-6,-4,7,-3,1,1,-9,-3,1,9,3,1,8,3,2,5,-6,2,5,8,7,7,10,-7,9,-9,3,-4,-4,1,10,-3,6,-2,9,8,-9,-4,-9,8,-8,-2,-4,4,-3,3,-2,2,2,-3,-3,-8,8,-1,-2,6,-7,1,-5,1,-9,-3,-3], dtype = "int8")#candidate|2614|(189,)|const|int8
var_2615 = relay.var("var_2615", dtype = "float32", shape = (2016,))#candidate|2615|(2016,)|var|float32
var_2616 = relay.var("var_2616", dtype = "uint32", shape = (560,))#candidate|2616|(560,)|var|uint32
call_2613 = relay.TupleGetItem(func_2329_call(relay.reshape(const_2614.astype('int8'), [9, 3, 7]), relay.reshape(const_2614.astype('int8'), [9, 3, 7]), relay.reshape(var_2615.astype('float32'), [2016,]), relay.reshape(var_2616.astype('uint32'), [560,]), ), 2)
call_2617 = relay.TupleGetItem(func_2335_call(relay.reshape(const_2614.astype('int8'), [9, 3, 7]), relay.reshape(const_2614.astype('int8'), [9, 3, 7]), relay.reshape(var_2615.astype('float32'), [2016,]), relay.reshape(var_2616.astype('uint32'), [560,]), ), 2)
func_2329_call = mod.get_global_var('func_2329')
func_2335_call = mutated_mod.get_global_var('func_2335')
call_2622 = relay.TupleGetItem(func_2329_call(relay.reshape(const_2614.astype('int8'), [9, 3, 7]), relay.reshape(const_2614.astype('int8'), [9, 3, 7]), relay.reshape(var_2615.astype('float32'), [2016,]), relay.reshape(var_2616.astype('uint32'), [560,]), ), 3)
call_2623 = relay.TupleGetItem(func_2335_call(relay.reshape(const_2614.astype('int8'), [9, 3, 7]), relay.reshape(const_2614.astype('int8'), [9, 3, 7]), relay.reshape(var_2615.astype('float32'), [2016,]), relay.reshape(var_2616.astype('uint32'), [560,]), ), 3)
uop_2625 = relay.log2(var_2616.astype('float64')) # shape=(560,)
func_312_call = mod.get_global_var('func_312')
func_314_call = mutated_mod.get_global_var('func_314')
const_2637 = relay.const([1.689747,-6.235409,-6.117302,-6.186880,0.345530,-5.804524,3.477242,8.126653,-1.364381,5.403388,8.935703,-6.025146,1.092482,-2.651684,2.827436,-7.377514,-8.322617,-2.006681,-2.126480,-2.782426,-2.837723,-1.753364,-3.526004,3.078878,-8.803846,9.650136,1.090628,-2.012833,2.149735,1.712219,-3.970901,8.191184,-3.395513,0.170054,-1.056730,-9.940660,-9.727955,-6.563336,9.802594,4.390905,-7.298827,2.346356,-7.851783,3.415803,-0.564846,-9.718192,-7.052031,9.370896,-7.555696,7.627346,6.486606,5.028322,-2.563243,-2.820954,-3.211344,3.969152,6.522241,-0.296100,-5.049586,1.284722,9.016452,0.872219,5.643521,-2.392954], dtype = "float32")#candidate|2637|(64,)|const|float32
call_2636 = relay.TupleGetItem(func_312_call(relay.reshape(const_2637.astype('float32'), [16, 1, 4])), 0)
call_2638 = relay.TupleGetItem(func_314_call(relay.reshape(const_2637.astype('float32'), [16, 1, 4])), 0)
func_2329_call = mod.get_global_var('func_2329')
func_2335_call = mutated_mod.get_global_var('func_2335')
call_2647 = relay.TupleGetItem(func_2329_call(relay.reshape(call_2622.astype('int8'), [9, 3, 7]), relay.reshape(const_2614.astype('int8'), [9, 3, 7]), relay.reshape(call_2613.astype('float32'), [2016,]), relay.reshape(var_2616.astype('uint32'), [560,]), ), 2)
call_2648 = relay.TupleGetItem(func_2335_call(relay.reshape(call_2622.astype('int8'), [9, 3, 7]), relay.reshape(const_2614.astype('int8'), [9, 3, 7]), relay.reshape(call_2613.astype('float32'), [2016,]), relay.reshape(var_2616.astype('uint32'), [560,]), ), 2)
func_2124_call = mod.get_global_var('func_2124')
func_2127_call = mutated_mod.get_global_var('func_2127')
var_2650 = relay.var("var_2650", dtype = "float32", shape = (432,))#candidate|2650|(432,)|var|float32
call_2649 = func_2124_call(relay.reshape(var_2650.astype('float32'), [6, 9, 8]))
call_2651 = func_2124_call(relay.reshape(var_2650.astype('float32'), [6, 9, 8]))
const_2659 = relay.const([-1.689314,0.104932,0.206496,5.205252,4.166324,-4.005252,1.790471,-5.297572,-0.603995,-0.210092,9.289608,-0.116906,1.711467,-6.279029,-6.759599,-1.980668,1.108015,-7.036787,8.068007,3.097020,1.923683,-3.508648,-3.049986,0.995324,5.895991,3.048108,9.126746,7.300054,5.209573,7.728884,-1.198570,0.998129,3.809826,-4.939008,5.956445,-7.143793,7.617638,2.716230,1.255844,-0.407395,8.836530,3.369729,2.901106,5.992992,-1.541257,-8.570914,-4.694315,-9.605452,-5.897629,5.329306,-0.572026,-7.736158,-2.823397,5.797384,-7.380414,1.943825,-7.709774,-0.078462,7.452450,-2.864549,8.613393,-8.616136,-5.063723,8.207248,-6.988148,8.317606,-3.149226,-5.532631,6.534504,3.706828,-3.194627,1.364147,1.609607,-5.052811,-1.114315,0.345377,-8.667057,2.742881,-3.390353,4.673136,2.648770,-9.095574,-1.323358,1.206189,-2.167083,8.698179,9.776342,8.677819,5.130608,1.937224,1.513459,2.063180,8.070675,-0.238876,0.277775,-0.961683,-7.330699,5.313162,5.051826,2.385171,2.495791,-2.829265,5.401038,3.723543,-9.784189,-4.674457,5.020110,1.659334,3.180548,1.403713,1.290039,8.435925,-8.621535,-1.680646,2.969147,8.546966,-3.442957,6.780768,-8.445345,-2.496053,-3.981825,-8.999359,-6.024919,-1.166290,7.690260,4.337990,5.426770,1.511661,8.379613,6.434834,6.668679,3.464434,3.494286,9.066361,4.542869,-3.699908,8.537424,-5.449359,-3.733008,9.163025,-0.769176,-9.895425,5.842090,4.690813,4.765470,-7.633951,5.705585,-2.752676,-9.979618,-7.480509,-1.683691,1.334074,4.556682,3.444691,-5.773791,-2.075849,5.185874,-5.239778,-3.036214,4.534421,2.629857,-7.697831,9.916350,9.113684,-1.106612,-5.974698,-9.421890,-5.907056,0.719679,8.419696,-3.061145,-0.040547,-9.531156,9.089365,-1.715197,-2.954243,-0.828778,-3.406617,8.508063,5.038360,-5.064748,-3.621209,-2.385490,-8.515563,7.740462,6.029525,4.502726,3.394010,9.348277,-9.641154,-2.087778,3.569897,4.496061,-7.343017,1.572399,2.417245,7.632139,-8.052096,-1.592777,2.272459,-2.914195,-5.037415,-0.701219,7.825113,-2.038207,9.363609,-7.358323,7.268331,7.898073,-4.545408,4.299218,-8.125144,-1.007102,-2.933127,2.209937,-8.439828,7.949604,-8.704840,-0.075693,9.866038,3.543359,3.329211,8.618119,-2.187420,3.005668,6.299868,-0.215882,8.558599,-3.185236,7.783683,-3.389809,6.960898,-5.542838,4.431754,5.250626,3.398107,-4.068179,-7.974542,0.196448,-1.720839,3.206442,-0.147059,0.210675,-2.809611,2.797191,3.408189,2.092039,3.244930,-5.289293,2.635071,5.174594,5.805986,9.085930,9.885319,-0.032178,1.167097,3.346054,9.463151,-1.343681,-1.635698,7.785809,4.669827,-3.359324,3.706279,2.204796,-9.321935,5.732703,-2.758700,7.993370,-1.685911,2.730212,-8.934806,2.753692,3.920956,7.770123,4.308800,-8.865340,-7.648570,-9.469177,3.609067,-4.842696,-7.008002,8.015714,-4.832467,1.882306,-5.257506,0.597751,0.646678,-8.931673,-8.287498,0.538327,1.216038,-9.581342,-7.534150,9.661621,-7.899782,-1.444592,4.079560,-6.662840,-8.381828,-0.441991,-4.562820,8.306732,-4.569796,7.464725,-1.900978,4.189392,-7.533950,1.599051,-4.467434,-7.088410,-7.633084,5.629483,7.934083,9.391541,6.918315,-4.134981,8.190052,-1.816823,-6.171836,-6.688946,-8.677526,-0.044991,9.465033,5.018719,-4.414832,4.315556,-8.455532,-0.416711,-8.944398,-6.868981,-9.466259,6.141155,-4.286365,3.209610,5.563550,4.633951,5.985234,-4.914472,9.400944,-4.354186,-7.859727,-0.538412,2.434586,-2.320509,5.368624,1.097552,2.934615,9.217090,-1.470836,-4.235918,2.106671,0.276521,5.848199,2.766328,-4.705114,-3.732995,3.329413,5.717707,-1.948608,-4.988273,-8.497604,1.193721,4.464094,-0.282383,7.578858,8.880214,-1.816762,-1.440486,8.472767,9.337035,5.387482,-0.357287,-3.071559,3.909621,4.923467,-9.728162,-4.466760,2.900449,2.186386,7.549147,0.906110,1.915617,-3.026127,4.375516,2.587949,9.743072,7.714359,-0.203698,0.241874,-5.445861,4.825954,2.172059,-5.234241,3.370524,-0.511124,-3.809386,-2.861164,6.030832,3.538836,-1.509568,1.194313,-2.255096,5.938975,6.317590,-5.517440,3.392328,-0.642194,6.523253,7.268812,-4.904610,-2.523548,9.038411,-3.552609,9.828395,-8.569901,2.460400,9.943077,-7.219986,-5.649014,7.371061,4.955911,-3.195113,5.706910,-2.817958,1.423798,-2.220030,9.861264,-1.024834,3.969952,-2.415451,4.911368,5.961811,3.354437,2.351258,9.312299,-5.147969,5.035356,0.914866,7.197609,7.755066,-2.083446,-5.229688,-2.313873,-9.865137,-5.838269,8.659887,-7.034244,-2.515802,-9.291739,8.926038,-5.321480,-5.697818,-2.058621,6.786259,0.028572,-2.236672,-0.430211,6.176633,4.717036,-4.665013,-1.904607,8.175400,3.798127,-9.904620,8.670140,8.506516,-2.980541,9.980694,8.364157,-6.460315,-1.525786,4.631580,3.789848,7.653037,-9.173858,-4.186727,5.276121,9.341447,2.874301,-1.861867,7.020024,-1.020350,0.878287,-1.999666,-3.754688,2.126339,-3.747168,-6.027697,3.480269,-1.741907,4.861886,7.225322,2.574887,6.656398,-0.342374,3.192355,-7.417117,4.848623,-2.001156,-6.056516,-1.299337,8.060461,-8.263534,-0.245175,7.648859,6.731549,2.493930,3.799463,0.702673,5.152017,-4.833158,6.917253,3.821339,-3.060549,4.601291,-3.895307,-6.106154,-8.293940,9.555043,-3.823310,4.728957,-6.596827,-5.404356,4.395165,-6.387184,-5.334166,-6.079958,9.340377,-6.778142,1.745801,9.166540,-7.384038,3.050583,-0.368233,5.647645,1.937647,8.503265,-9.654837,9.382147,1.240099,-0.772341,-7.149119,-6.035808,-1.303653,7.535040,-6.527074,-6.846541,-7.189790,1.140376,-7.419293,0.709977,1.686373,8.157000,6.163024,-3.875880,4.888973,-7.159479,0.747242,4.526670], dtype = "float64")#candidate|2659|(560,)|const|float64
bop_2660 = relay.logical_xor(uop_2625.astype('uint16'), relay.reshape(const_2659.astype('uint16'), relay.shape_of(uop_2625))) # shape=(560,)
output = relay.Tuple([bop_2593,call_2599,var_2600,call_2613,const_2614,var_2615,call_2622,call_2636,const_2637,call_2647,call_2649,var_2650,bop_2660,])
output2 = relay.Tuple([bop_2593,call_2601,var_2600,call_2617,const_2614,var_2615,call_2623,call_2638,const_2637,call_2648,call_2651,var_2650,bop_2660,])
func_2664 = relay.Function([var_2591,var_2592,var_2600,var_2615,var_2616,var_2650,], output)
mod['func_2664'] = func_2664
mod = relay.transform.InferType()(mod)
mutated_mod['func_2664'] = func_2664
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2664_call = mutated_mod.get_global_var('func_2664')
var_2666 = relay.var("var_2666", dtype = "float64", shape = ())#candidate|2666|()|var|float64
var_2667 = relay.var("var_2667", dtype = "float64", shape = (7, 15, 14))#candidate|2667|(7, 15, 14)|var|float64
var_2668 = relay.var("var_2668", dtype = "float64", shape = (84,))#candidate|2668|(84,)|var|float64
var_2669 = relay.var("var_2669", dtype = "float32", shape = (2016,))#candidate|2669|(2016,)|var|float32
var_2670 = relay.var("var_2670", dtype = "uint32", shape = (560,))#candidate|2670|(560,)|var|uint32
var_2671 = relay.var("var_2671", dtype = "float32", shape = (432,))#candidate|2671|(432,)|var|float32
call_2665 = func_2664_call(var_2666,var_2667,var_2668,var_2669,var_2670,var_2671,)
output = call_2665
func_2672 = relay.Function([var_2666,var_2667,var_2668,var_2669,var_2670,var_2671,], output)
mutated_mod['func_2672'] = func_2672
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2775 = relay.const([[[8.449644,4.319187,-8.485620,-6.345944,2.510414,7.215735,-1.653211,-4.242926,2.314594,-3.531726,4.907909,-2.896446,6.969760,-6.206474,-5.942840,-1.478850],[-8.484806,9.986705,-2.640659,-1.878768,-6.323326,-0.172156,-4.085344,-1.515874,1.844129,-0.722516,-5.577602,-8.214694,-0.881520,6.410996,-5.515493,-8.000360],[4.855338,2.544057,-7.221455,2.929877,3.985412,7.626984,5.040380,3.600525,-9.709457,4.125745,-3.682145,-9.662784,4.995731,5.610993,-3.752160,-5.027490]],[[2.379717,5.788418,3.426362,1.580211,-5.457165,5.736905,-4.030573,-7.431428,-7.683173,4.012801,6.798093,1.139343,7.286128,4.359197,4.713426,6.217446],[4.376731,-8.799240,-1.272031,-9.416576,-9.875849,-0.823416,-7.797257,6.526709,-7.380995,-9.663808,-0.434494,-2.108564,-8.999481,3.240782,-0.913201,3.239896],[-7.380420,-7.466551,6.200810,3.430366,-3.567514,-9.324396,5.264203,8.402710,5.662809,1.498071,-4.599194,9.867675,9.953408,-4.756541,-7.356079,-7.022622]],[[2.725121,3.257149,5.600677,-8.284870,-2.087780,-5.843168,-8.215009,3.421147,8.826521,3.318538,6.894580,2.492445,-3.885128,-7.299071,8.618652,2.066561],[8.960421,9.795572,8.299291,8.650519,-7.473140,7.928080,6.146558,-4.982616,-3.776454,-9.943212,6.506186,-5.766556,5.105456,-5.363970,4.007950,0.803288],[-5.972240,1.699613,-5.907561,9.986971,0.860383,5.085587,8.900615,1.570653,-6.055107,8.252167,1.268116,1.650046,-3.982657,0.257791,8.919513,0.537394]],[[4.296640,6.033646,0.119852,6.458974,-3.651108,8.606105,-7.468698,0.753646,9.995858,-7.823704,-9.158580,7.212818,5.100507,6.664724,-3.193742,-9.156821],[5.868257,4.565629,-5.678420,3.035596,-1.886018,5.771519,-1.195393,0.153488,4.348750,-3.818504,3.474563,7.021607,7.380115,0.859690,3.401579,1.470975],[2.114879,2.126143,4.608274,-1.100835,3.628065,8.262702,-8.321944,0.909566,-9.856156,-1.026170,-2.161432,8.717395,-6.509589,6.518013,-0.093976,-4.623278]],[[7.890923,-8.919902,5.022066,-4.461220,-7.278006,-2.078259,-2.370387,-5.433427,8.112965,-5.817601,-9.319707,2.179580,-5.235654,-7.071808,-5.539872,0.213846],[-5.316509,-6.466093,-7.272827,0.539839,-9.606998,-9.674064,7.268644,-9.973543,4.918627,-9.366390,-9.165817,-4.062242,-6.624070,1.311353,9.717472,6.206675],[-6.048901,3.045637,-1.996653,7.729894,-5.747383,-8.019933,1.187731,7.054010,7.005599,-4.671736,2.458621,2.230899,-1.884397,-1.158354,4.071463,3.711868]],[[-1.433389,-3.970374,4.566148,2.961574,9.095345,-4.980460,-0.528066,2.268881,5.205474,2.524839,-4.683377,8.267914,-6.522985,1.596764,8.317440,7.497399],[9.959107,-9.529473,-0.775126,6.109369,2.236160,-9.391872,2.157432,-8.733908,1.121916,3.069505,-1.597265,-1.569713,7.568985,-3.157973,0.078985,-5.261377],[4.620182,5.193774,-8.878065,-9.321503,-4.134805,-4.843604,-1.718976,2.990418,-6.466009,-1.204914,1.448138,1.953168,-1.786139,5.951875,-7.581129,-7.837089]],[[-2.028685,4.949637,-6.106929,0.935550,-4.507109,-2.322174,-0.501470,-4.335363,6.162279,2.103557,-4.469612,2.007854,-0.944140,-4.742131,-0.484084,-3.797041],[-6.165844,1.004470,3.116394,-5.794483,-0.202414,5.019625,-3.637120,-3.864908,-5.575089,-8.994598,-1.557818,9.092878,-0.896635,9.111018,-3.975922,4.959301],[3.200360,-8.091356,6.584262,-8.526889,0.744930,-1.861737,-6.594692,9.083831,-8.647066,8.595459,1.403050,6.418621,-7.556124,-8.243365,1.479128,7.828557]],[[5.751263,0.827399,-4.539577,-0.875252,1.321094,7.017056,4.555238,-5.802601,-5.572906,6.587947,-9.119340,2.436226,7.431155,-5.290452,-3.820833,-6.495235],[7.589763,-4.067954,9.004362,5.329360,-1.945196,-8.569656,-0.813359,6.729332,-1.128904,-2.229628,-8.799877,1.120025,-7.561330,-4.997641,-0.492466,-7.420342],[-7.706163,6.147284,2.806836,6.007548,-8.249686,-2.522900,-6.443030,0.110652,-1.978321,-9.064362,-4.538803,-5.040015,5.632463,9.808181,7.416518,5.979579]],[[-9.202002,-4.601019,7.777101,8.699177,7.835466,-4.802619,-9.231630,9.500876,-6.599404,9.410067,7.515431,0.465092,-8.553258,-3.570569,-2.877289,8.919323],[0.496562,-1.881373,0.720798,-5.793707,1.126439,7.998563,-0.510324,-9.121955,-6.908809,5.370724,-6.969770,-0.568767,3.291010,-5.375622,-9.296064,4.456808],[1.092683,-2.890898,2.832606,-8.445120,-1.667225,-0.604889,-0.696599,8.495800,-8.320414,-8.337134,3.255121,8.862232,-3.683471,-8.375708,-9.875520,-4.153998]],[[9.245273,-9.464089,9.287258,-1.660611,-6.487878,-8.947266,7.659276,8.535667,4.684024,-7.144489,-2.837267,1.756577,-1.410782,7.241198,3.950639,-7.438809],[1.357543,-6.013767,8.774823,-8.639539,1.635657,-5.828752,-3.131963,0.543643,-6.406979,-6.210821,2.091682,6.069908,2.924869,-3.922235,-3.085733,6.358888],[-7.588829,-7.784249,-1.347787,6.532557,4.237577,8.526970,-7.084981,6.555752,-1.184180,6.058511,-9.970963,5.742754,-4.613293,-7.569813,2.613720,-2.292213]],[[1.283568,3.019152,7.885812,-1.226795,0.207893,-2.049505,-3.791539,-3.797079,8.255853,-2.931462,-6.252252,2.710407,-0.563910,6.754077,7.965866,5.750783],[-4.045521,0.995458,1.542424,-4.611382,7.000423,-8.449883,0.587902,-1.922008,5.196902,-7.431502,8.064432,-7.883350,6.856502,3.151126,3.255851,-7.384388],[0.730905,5.912325,5.001057,0.426117,-3.855593,-7.368754,-3.956051,-5.149168,2.109117,0.642677,-4.913859,-1.003188,4.937287,-9.018739,-8.684165,-3.926420]],[[-4.051003,8.175684,-5.404887,-5.265901,-7.129737,-7.244094,-5.922695,-3.205160,9.970334,-9.834586,3.906543,0.468155,-6.213712,1.853557,-0.976795,-6.162541],[2.680291,-8.315524,5.906992,-5.551817,2.040583,-2.685312,0.064895,-8.655995,3.672134,-2.245365,9.509342,3.078820,-9.729287,2.794749,5.093070,8.534623],[6.252462,-5.928004,6.226319,-6.015814,9.688971,-1.351356,-5.053980,0.548622,6.748742,-8.898542,5.039744,-9.252003,6.151650,5.883001,7.412207,7.859568]],[[-2.739249,1.184594,0.364716,3.561115,7.354367,3.749174,-5.975082,6.745953,9.166719,-5.226554,3.543066,-1.276073,-3.034400,5.365206,-1.422066,-5.248093],[-8.049045,-9.770120,-4.815731,-4.393477,3.336761,7.247829,-3.959961,7.892669,-6.299840,6.592273,-5.440568,-3.550221,7.030169,5.581490,2.008918,-8.031588],[2.716345,8.616384,-9.994532,0.324840,5.878518,7.062299,3.465233,9.030720,0.201901,-7.074454,-1.634870,-6.978652,-9.236169,-1.149638,-7.750032,-1.991265]],[[9.623810,3.318316,2.657194,-1.997705,8.889942,2.344371,-1.509063,-5.429266,4.635232,-2.871253,-6.845736,6.780187,-4.650138,-2.917352,-2.300568,-1.687089],[-2.489139,-0.331185,2.341847,-3.098559,-4.478373,3.883429,5.447186,-3.426353,-9.360286,-2.859960,-3.414656,-0.809427,2.060291,8.872212,4.970911,-1.256271],[9.869666,3.311031,9.799107,8.124236,2.899701,-2.728381,-1.122775,4.487490,1.261298,7.916209,9.586870,-4.748052,-0.630925,7.489014,-6.084031,8.164318]],[[-3.252678,-3.182755,8.021953,0.843683,-2.563464,6.980627,6.778078,-2.213598,-3.271338,-3.334679,3.056938,4.043616,-7.669438,1.830850,-6.055962,-3.580524],[4.192549,-6.824165,-6.235910,-4.124540,1.382732,2.211501,-0.238387,-6.094411,-1.103224,1.067772,5.635999,3.371666,5.191301,-6.189937,-7.040084,-7.862086],[5.471291,-9.139575,-0.112146,0.291966,-8.430968,-1.832872,-2.035670,2.311050,1.077682,-5.654325,9.312669,-7.392762,-6.217221,-9.376380,7.573705,-3.357729]],[[6.175610,-4.429758,7.112772,-0.476162,4.957506,1.834140,4.081151,-2.308386,8.659929,4.145356,-6.634084,5.513635,8.688064,0.284331,-8.471344,6.676123],[-7.407055,4.820942,9.684542,1.394901,2.404779,-8.383652,-9.040835,7.996420,5.703389,-9.490958,7.673922,-5.959248,-8.744980,2.710938,-8.255317,-6.893186],[4.960254,-1.737147,3.560243,1.352730,-3.452875,5.547390,-7.243244,-8.475409,-9.060140,8.123415,-8.400988,-1.965715,-8.246479,3.670868,-8.210091,8.087824]]], dtype = "float32")#candidate|2775|(16, 3, 16)|const|float32
uop_2776 = relay.tan(const_2775.astype('float32')) # shape=(16, 3, 16)
func_1205_call = mod.get_global_var('func_1205')
func_1207_call = mutated_mod.get_global_var('func_1207')
var_2792 = relay.var("var_2792", dtype = "float64", shape = (84,))#candidate|2792|(84,)|var|float64
call_2791 = func_1205_call(relay.reshape(var_2792.astype('float64'), [2, 3, 14]))
call_2793 = func_1205_call(relay.reshape(var_2792.astype('float64'), [2, 3, 14]))
func_2458_call = mod.get_global_var('func_2458')
func_2461_call = mutated_mod.get_global_var('func_2461')
var_2815 = relay.var("var_2815", dtype = "int32", shape = (1170,))#candidate|2815|(1170,)|var|int32
call_2814 = relay.TupleGetItem(func_2458_call(relay.reshape(var_2815.astype('int32'), [9, 13, 10]), relay.reshape(var_2815.astype('int32'), [9, 13, 10]), ), 0)
call_2816 = relay.TupleGetItem(func_2461_call(relay.reshape(var_2815.astype('int32'), [9, 13, 10]), relay.reshape(var_2815.astype('int32'), [9, 13, 10]), ), 0)
func_825_call = mod.get_global_var('func_825')
func_827_call = mutated_mod.get_global_var('func_827')
const_2820 = relay.const([-6.684969,4.216867,3.524509,3.232967,-2.257104,-8.583208,7.102641,-1.919301,-3.355815,3.717684,8.617154,-0.709322,6.590577,0.392964,-1.921067,9.672126,7.799750,6.245395,8.241022,-1.717934,9.939084,9.427341,-2.222941,-3.701096,9.574703,-0.481474,-9.520066,5.135783,-3.600088,-6.072840,1.942579,4.824805,9.501428,-9.772935,-4.548076,-6.154446,4.070416,-9.301736,-3.931280,4.020191,-4.789067,-7.979804,-6.938825,-1.412584,-6.474934,3.547087,-3.717002,0.132267,-2.570878,8.281930,-8.610723,-9.503986,7.125068,3.327467,5.006067,2.048220,-8.946870,-1.941769,-8.848519,5.900591,-9.856972,-3.266281,3.120591,-8.622997,3.545422,-2.338381,6.187369,-3.775218,3.077624,-8.816622,-5.257728,9.630579,-2.351931,9.773199,-5.565050,2.563737,4.368689,-0.219178,9.678433,-3.305066,-9.925636,-4.800742,0.534399,-1.385020,-2.828894,-4.217266,-8.853050,4.126823,9.719669,3.149587,3.870156,-4.284960,7.786195,-0.311110,1.130609,9.567681,1.006902,-5.953817,-7.418108,-4.696044,9.674622,8.830405,-1.306353,-4.654379,2.650925,1.620059,1.401192,-5.959237,-2.518136,7.259122,5.823789,9.281475,8.033895,-5.269502,-6.223380,-1.833614,1.807429,-8.690159,6.121660,8.825992,-2.572465,9.056755,9.575281,-1.419679,-6.148199,8.610549,0.457756,5.084974,-3.786255,-2.130541,-0.276827,4.835743,9.295800,9.490648,-0.499028,8.207237,0.901160,-1.558205,-2.315319,4.041590,8.190467,8.248456,9.884782,5.433461,-1.651397,8.780246,-9.955903,-6.187785,-3.597634,-7.372202,-2.300802,2.920540,0.311837,-0.861593,3.817775,-0.739163,7.771087,2.412803,-2.357143,-7.822225,-8.374882,3.914504,-1.404807,-3.691548,5.768718,-2.150054,8.824323,-9.485867,9.475960,-6.761806,-5.590791,2.206625,-9.921626,-8.372138,6.519915,3.867235,-9.416535,7.294843,-5.090444,4.486776,-6.272163,-0.023610,-8.005594,-0.879189,2.644958,-1.387578,-8.634732,7.653880,-4.684478,7.329997,4.159869,0.103853,-7.689091,-2.782049,5.450481,-0.235700,9.496123,5.110687,8.637809,-1.121675,-7.899182,-8.343900,-6.441469,-6.443948,-1.285788,0.566370,-6.401292,0.780115,4.008360,-6.523914,-9.080358,-2.030550,0.820242,2.378997,-5.290951,9.333357,-2.031527,3.559577,-8.297973,9.630535,1.458894,-0.530559,2.938922,-9.356123,4.152995,0.086239,-9.942676,-9.822751,9.564486,-5.116301,1.729491,1.633155,-2.812143,-4.809780,-5.340882,9.057310,-0.648179,6.723998,6.180372,-6.254853,-1.610827,-1.172811,-1.160635,-2.301142,-9.438681,2.323628,5.714845,3.394457,7.186181,-8.165343,3.159623,2.529232,8.032460,-5.274553,4.880249,8.075188,-8.743933,-2.419619,-3.911188,4.742622,4.706184,-6.871195,7.088841,-3.635461,-5.137641,-3.965383,-2.651809,0.174375,-1.961038,9.807828,6.593767,-4.889208,-2.936992,-8.959386,4.527901,-6.136105,-9.796264,0.550411,-3.784134,-9.367310,-5.323494,6.694730,-5.436381,-9.876163,-7.347732,-4.500265,8.195299,2.630510,7.053043,-0.541230,7.283024,-7.953676,-5.874890,5.551667,8.327468,0.840038,-9.251479,2.990375,8.059985,-9.959670,8.710507,1.631564,4.733613,-7.625862,-1.946338,6.317191,3.719973,7.167826,-4.197328,0.249877,-2.832149,6.055104,7.764751,-0.359701,3.795946,-8.571172,6.280832,1.980309,-4.140419,-5.990434,-2.093085,7.938327,9.447651,8.308065,1.372251,7.401619,5.372204,2.093822,1.736635,-0.899575,-8.016035,4.397824,-9.211098,-9.354435,6.009912,-7.018329,-7.169756,2.707886,-4.206390,5.579627,6.511955,-8.703631,-1.756818,6.716869,5.345887,-6.922097,-5.378463,1.263805,-2.448071,-4.029090,-8.086464,5.914988,-7.965419,-3.536059,-4.539155,-9.400520,4.733320,-3.956042,-7.030360,0.706805,4.456684,9.958652,-8.087232,4.006252,-3.663315,-4.522809,-7.591428,-9.364791,-1.606977,7.283901,-2.743042,5.819502,-1.720643,9.535903,1.341002,-1.071700,-3.772581,7.406638,0.727920,6.187396,-5.094269,-7.830326,-5.784816,3.236242,-2.781961,1.385653,-8.486660,-1.139469,-3.220560,-7.581155,-5.465692,2.412431,-6.061981,4.311516,5.560174,-9.553921,-7.913485,-2.176102,9.997394,-5.389105,-8.801114,-1.681302,-5.079642,-3.692329,5.568899,-5.293537,2.073599,-6.084850,-2.031814,0.266015,1.942634,7.630780,2.965444,-6.418186,1.895567,-7.721668,-8.191579,8.480361,7.382506,4.300302,-2.630205,-3.298171,2.774435,1.082721,2.887325,8.314141,-2.197742,-9.407035,-3.606952,-0.621614,9.378873,-6.377035,-1.513182,-1.012855,9.731251,-4.082213,-6.349245,6.754575,9.858931,0.384769,-4.388685,5.244681,-2.469953,-6.003191,-0.887752,-6.539231,7.946090,8.962544,-2.970473,4.033931,-5.614716,6.754841,-1.554326,-1.198300,-2.779778,-4.157081,1.610654,1.886815,-3.216239,-6.826600,1.093341,-0.537550,5.259593,-1.983633,-8.093341,4.415961,3.028224,8.588144,-0.736143,4.891406,9.606372,6.131114,-2.838939,-3.336987,-2.354609,5.727745,-5.637265,-3.889537,-4.512045,2.651747,-7.387896,8.949923,-3.342983,6.872709,-9.540307,1.972653,3.181889,-7.216330,6.812523,-2.598724,-3.008130,9.348786,2.249306,-8.526337,-9.249562,-2.317286,6.720149,-6.542820,-5.616132,-8.912201,8.878079,8.546343,-8.260920,-5.324852,-1.333363,8.335838,-9.108426,1.896041,-1.440205,1.101581,-1.479303,7.829874,3.145646,9.990244,4.724795,0.192590,6.975304,6.527454,-5.877309,9.161833,-1.582469,2.937490,-5.381242,5.255520,0.467971,6.274511,-2.281738,9.434879,1.452087,-8.841147,-0.040681,8.915943,-3.399548,4.758021,-4.970587,3.351186,5.123579,2.157337,-0.097000,-0.264839,-4.520337,5.229315,-9.472739,-3.622287,3.429708,-7.138651,-9.801069,9.160895,4.608174,-0.990912,6.598862,-8.152869,-4.082105,-7.849914,-9.312141,-8.202008,8.658144,-2.978876,-6.441154,0.008247,2.603213,9.322369,7.653838,-5.662755,4.967530,-3.423210,-3.058838,8.783559,-4.157789,0.160227,-3.323771,5.447718,7.883127,1.142753,5.253633,7.867983,9.583926,-6.434429,6.678422,4.553981,0.715783,-4.010062,-1.540815,6.518615,4.587759,-7.973660,-7.584236,2.326655,6.018955,-4.456415,0.260479,2.560266,-8.425544,5.343539,-8.154368,1.589439,-6.665592,2.687397,9.723161,-9.519197,-6.023905,1.197411,-5.720018,-1.527659,2.595480,-2.208591,0.193987,4.484141,-0.480711,8.004287,5.502925,-0.859935,-9.100704,4.705160,-7.691417,2.692727,-3.525634,-7.293717,6.955580,-0.065834,1.558975,-5.593114,-3.786758,-0.474665,-6.881126,4.679474,-6.250416,-2.963379,0.583976,4.778337,7.212590,-0.855020,6.071850,-7.239178,-3.145731,5.439077,-7.138376,-1.603192,-4.685520,8.561896,-4.729570,-0.717530,-5.511677,-2.229503,-4.022007,-8.596417,-3.470792,4.843652,9.589141,-6.651471,-3.618334,4.562503,9.035830,4.990866,-1.856942,3.642557,0.257781,-3.548717,-7.952231,-2.187676,-6.037534,-7.512869,1.251453,-7.665085,6.404317,-5.793112,-6.547413,-5.824307,1.533692,2.663487,-4.715779,0.434401,5.460177,-8.598360,-0.056011,-6.908068,0.514508,9.166202,7.636957,9.267809,-2.054910,-4.377780,3.620535,2.658274,9.044579,-7.622647,8.674925,8.936240,9.889443,-8.751789,-9.526538,-9.202166,6.824271,6.489471,9.464038,1.753503,-1.057638,5.493534,0.768821,8.560572,3.369377,-9.178960,5.180512,7.380384,1.608362,-1.867727,6.404538,7.673092,-9.273953,3.303939,7.971109,3.475438,-1.076818,4.217411,6.262366,-7.284583,9.883567,5.631516,8.494099,2.796409,-2.163737,-9.944002,0.072358,-4.202910,-7.037063,5.151320,0.855646,-2.190486,4.717454,9.105605,-0.672839,-1.264619,-2.222592,-7.798964,-4.466934,0.306998,5.489450,-3.157222,7.499383,-4.396663,-5.028359,-6.865387,-2.491366,-2.847210,-0.450657,1.787517,4.133408,-9.839064,3.496760,7.003184,5.303927,1.374689,5.105860,0.282480,-1.893529,-9.946997,1.990706,-4.699493,8.457229,-1.970831,-2.230891,-3.586274,5.740970,-4.180559,5.225494,-7.293802,-4.003422,5.574681,-4.808676,-4.165696,-5.800629,8.959435,2.063414,-3.424368,-9.020427,5.349053,-0.268156,3.657801,-4.455945,-7.374725,6.310153,-6.126164,-2.189187,4.625809,-2.294296,-8.234865,8.435725,6.710300,7.788873,3.835928,-6.725716,1.170232,0.018202,-1.964827,-8.279155,5.552504,8.820797,8.894089,-3.272009,-9.270591,-9.146312,6.786598,8.501830,4.151224,-1.219901,-3.694150,2.314009,2.891628,-0.392416,-5.873286,0.475429,0.061775,-7.962357,-1.362073,6.544500,2.524968,4.284126,3.232787,4.536222,-7.293453,-7.157335,-7.594227,-0.035951,-7.619887,3.651425,3.814423,-3.669402,-1.393148,8.458065,4.641316,1.973009,-1.988034,-2.077064,1.620376,-7.552542,0.764962,3.820480,-5.673013,-6.732952,-2.186360,-8.978238,-8.219416,-6.425818,1.206065,1.528398,2.117304,4.752772,-9.046037,6.399742,-3.475739,2.888771,-9.893417,9.577051,-7.114377,3.899890,-3.865719,-1.970781,9.997248,2.195398,-2.426202,1.473390,6.142671,3.303041,-5.933146,-4.647630,1.802736,9.969642,-9.881091,-6.608778,-7.574431,5.536506,0.164431,5.728976,6.328350,8.862609,7.955704,9.345249,-7.721499,-2.341691,0.293035,6.965122,-5.861607,5.085380,8.819177,3.888340,7.150487,-1.506855,-9.865053,1.209634,-3.514147,9.694703,-8.387621,0.559050,-1.868864,3.213193,-1.930587,-4.328186,5.871452,0.338212,6.709842,-5.422547,4.153739,-6.428207,-5.600020,4.252774,-5.295210,1.272919,0.584337,7.696339,-1.163243,-8.100732,6.802681,-9.907421,-3.850539,-3.950377,-0.126649,-8.859016,5.790701,-8.626471,6.419848,6.340934,-0.725700,-6.756436,0.230816,5.932887,-2.031953,-8.518740,-8.867406,1.982535,-6.830134,9.834700,-7.412496,-7.800392,-7.852381,-9.102042,2.578029,4.879588,-4.785475,7.586431,-9.248851,2.743481,-8.373810,-4.844740,-2.531721,5.773509,9.978346,-0.428704,9.148550,-3.272621,9.087235,3.621822,-9.199287,-1.306898,-8.887638,-7.086078,2.671408,7.333266,3.103412,-1.592865,0.949567,-2.502981,-6.315475,5.380155,8.074093,4.816579,-7.586744,3.058018,-0.505153,7.057905,-3.270566,5.018145,2.774144,3.848224,-9.528055,8.131170,-3.404621,9.727094,-7.361813,-9.378988,-3.188063,-6.025954,-3.759463,2.004663,1.387188,5.663484,-6.924146,9.713417,3.976308,-7.630961,1.769083,-3.990602,0.846906,-2.464900,-4.606020,7.114738,8.821375,0.890181,-9.112598,-4.578331,4.595510,9.101186,-2.287074,9.408981,8.581419,3.722404,8.519813,-5.558188,7.842378,-4.353239,6.957275,-8.773759,3.282485,-2.127250,-3.771316,-3.210040,-9.021692,0.469140,-4.584632,8.952630,-0.818541,-8.197765,-2.244668,-1.814415,-2.218445,5.458308,9.275093,-9.649019,1.798057,-7.702773,2.338212,4.803965,-7.774598,-1.454855,5.277570,-1.274246,-6.658445,-5.837175,-4.403396,1.536723,3.653797,-0.373071,-5.744563,-1.990654,-4.570570,-9.558683,7.755210,9.954561,-3.409192,-0.594661,2.617196,-0.598607,-3.472443,-1.969946,8.361427,5.112858,-5.424931,7.443426,-3.442262,-4.926814,-1.965226,-2.735015,-8.368763,0.786182,0.694806,5.727416,4.764227,-6.529763,-9.280657,-7.786242,-7.266974,-0.544643,3.930241,-8.833580,5.369064,-9.546652,1.355959,3.555192,9.014572,-0.375837,1.831706,1.510687,1.288898,-0.301432,1.762913,-7.985664,-4.388403,-6.730110,-7.037588,1.791193,-0.751951,-2.781025,-8.452577,0.989538,-0.453126,-8.226445,9.104919,-4.502756,8.416359,-9.058702,1.282933,3.069253,-8.862387,-2.819679,-0.387817,-0.022998,8.483234,-8.898517,9.362164,1.867014,4.376981,3.607377,-6.554218,-3.757725,-6.874162,-8.902951,9.188828,2.269575,7.198529,-0.753875,7.977915,-3.744551,3.510214,-5.852987,2.214942,7.083345,1.573625,4.971745,-9.667683,1.754693,3.669166,7.419696,6.105340,-8.974646,-0.384025,-9.690518,8.408026,-0.133800,9.345808,6.901907,5.683455,-7.410169,6.396928,-7.510868,0.400415,-1.017871,8.872758,6.815115,-3.217551,4.131133,-5.667965,-0.641180,5.115982,8.464895,6.716227,9.594454,5.364211,5.293973,5.064081,-7.271671,-1.747295,7.681839,-3.508926,-9.284336,-3.153904,3.189556,-0.536187,9.129426,9.018983,-3.387647,7.835838,4.166531,1.217448,-7.309436,-9.107790,5.138287,5.749393,-8.561524,2.452629,6.264631,-3.935575,2.733114,-7.852376,-0.593087,7.002613,7.000220,-4.141198,2.723807,4.116495,8.437510,-9.993479,-4.448882,9.860034,-1.939500,-0.750997,2.779508,-2.218155,2.623672,3.715319,-4.808013,-8.398353,5.443251,-2.447621,7.331449,-9.995126,9.363587,3.461907,4.414915,-6.256240,-3.285929,3.343129,-0.586447,-7.027974,-1.101373,9.660257,-1.896438,-2.941802,7.735502,-1.126221,7.996605,0.462284,5.589799,-8.219461,2.163874,-7.164200,4.938086,9.638950,-6.375386,0.088987,3.713276,9.673567,7.112840,-1.254836,2.830800,8.176012,6.579146,6.783797,2.102004,8.120411,0.395153,-3.303023,8.040575,-2.611314,5.897808,1.986890,-0.776289,-7.817819,-5.244505,-2.916583,3.101941,-9.458879,-8.430557,-3.116057,-5.336265,9.996008,5.852735,-3.536648,6.766437,-6.831440,6.550412,-0.903628,6.455343,7.489036,5.548059,1.207458,7.758779,2.686066,9.750825,3.894135,-8.326572,6.631562,8.657176,-8.642243,-5.795111,4.916940,-2.522956,-1.453198,4.389577,-3.107833,1.166254,8.183000,1.892093,7.149820,-2.721379,-5.309193,1.009089,2.430730,-2.764749,6.345055,-2.645350,-8.898470,-9.081445,-8.045157,-1.702967,-4.428453,-0.128840,-6.475410,9.038859,4.139752,-5.337547,-4.594933,7.571742,-3.228945,2.478772,6.890770,0.988669,5.122347,-0.215368,9.558775,-1.653877,-7.446319,1.157292,-7.462490,-1.820880,1.551879,-4.259835,-3.649545,9.842485,0.587697,0.440535,-4.475075,-7.314038,-0.166657,-0.342604,4.049480,-5.654529,9.173274,-5.130839,-0.892903,0.789938,4.644723,0.537321,-2.123429,9.645365,8.176293,-0.998962,4.191577,3.337353,1.043105,3.464129,-6.392621,-0.447635,9.515635,-7.244563,-5.309752,0.932343,4.618772,3.874503,2.514980,6.530419,6.278834,0.691089,-7.914226,0.767232,-5.903152,-6.776401,-0.507222,-8.950879,1.579590,5.913308,0.605498,2.646229,6.146882,-8.294495,5.901361,1.652408,0.221257,4.459399,-3.076759,5.708141,7.535498,0.123151,-2.009343,-8.299601,-3.971811,0.547400,-2.358152,-2.372958,-1.442112,9.260168,-7.290889,-4.062829,7.687577,1.274029,-1.082362,-4.427582,-2.642019,1.146083,2.296609,-9.089655,2.147073,7.155744,7.234451,2.260722,-4.762732,1.976132,-5.306386,-8.477674,-9.571612,3.442104,-3.203879,-4.685453,8.691367,-3.913849,0.313452,3.929891,-8.338755,1.903105,-8.966342,5.360661,0.608008,-1.687037,3.719593,3.010563,-5.316906,-7.776041,-0.230857,-0.657484,3.121383,-2.070939,2.663616,9.807031,8.135837,8.456659,-4.132953,-5.677156,-3.447428,1.606407,-9.184644,2.086942,4.769279,5.011826,-5.336472,4.942542,-7.024555,9.863890,4.864516,-8.563348,1.735267,2.500996,-2.358339,3.689468,-9.065686,-2.193682,8.603005,1.040660,-4.261638,-2.548821,-7.510420,-6.420505,4.283673,5.515042,-6.644520,2.454227,2.883031,0.627136,0.679309,-6.161155,6.339370,-6.942365,-6.950203,9.185965,-4.940819,-7.284660,-6.797366,-8.243659,-7.508090,-0.083060,5.142915,-4.652785,-3.113182,-6.708840,-2.987281,9.437547,-7.031966,-8.044753,-8.059395,8.387798,9.204101,7.800461,-4.637083,8.002404,4.486080,5.058104,-0.528134,-3.446506,-6.479282,-4.177544,3.587728,-5.066814,7.755980,7.361218,1.773141,-4.431478,-6.139313,-2.440993,5.379945,7.708621,7.780400,9.294888,-4.742610,8.739512,9.568953,4.004415,4.659976,-0.052862,-5.868046,-2.704462,-8.961107,-3.484045,0.264138,1.426200,-7.432320,4.355973,8.210070,9.686710,-8.703382,-7.245845,-0.393771,3.953561,-1.131841,-6.361137,2.809944,-0.046856,-9.753901,-6.824145,3.367988,-3.009550,-1.109130,4.659047,7.377530,0.831389,7.631813,1.407239,6.887088,-7.730455,-8.339563,-0.870910,1.627838,1.720292,2.691393,2.678023,0.606423,-9.961178,-9.067213,4.654938,7.230943,4.650704,5.525331,-6.820560,1.700629,-6.490746,-2.913580,0.673721,6.599190,4.509683,-0.456101,5.843140,-8.904710,7.766780,7.757256,-2.985076,1.876941,-5.506171,-5.076457,4.707501,9.072932,3.291086,-2.788679,4.096823,4.471525,-9.196973,-6.849148,5.666429,-6.829151,2.383739,-8.200434,-8.498326,4.259706,-0.350927,3.648853,-2.857526,8.086144,-7.991057,-0.887139,4.039418,-6.799884,-3.987948,0.535248,-5.652852,-4.154127,9.159352,1.581596,7.085229,-8.725901,5.422829,6.804390,-5.392757,0.650386,3.634400,5.369220,-9.510449,-5.288322,-7.752674,-3.851228,2.411115,-4.990631,2.591480,-8.145117,-4.490281,-9.976033,1.374304,1.948659,-5.767428,-3.458135,6.764015,-9.601678,-1.855178,-4.692641,-7.152326,3.226092,4.298925,2.320783,8.716203,2.393482,-4.395740,6.501697,-8.532162,-6.734635,-6.143159,-9.234131,-8.273121,1.341252,2.160651,0.405752,-3.837869,-2.773096,-5.780111,9.245992,6.880505,6.531667,-3.327847,3.680702,-4.911559,-0.579159,9.617996,-3.901970,2.007827,-4.255606,0.833761,5.397022,-7.357250,5.879146,5.149390,-6.923552,-8.678982,-1.392682,6.128845,5.034518,7.056708,-1.417943,-6.039424,-3.559731,-2.886085,-1.715647,-8.508333,8.526131,2.256664,0.516521,0.399989,-3.066635,-4.637959,6.459476,-5.052764,0.685650,-0.057132,-7.263735,-3.572146,-0.832965,8.188385,-5.624691,-3.719226,-0.456906,-6.609969,-3.112375,-3.228182,5.155807,-6.218922,-5.070461,4.062151,-7.715240,6.238643,-2.990080,-8.106906,-6.847976,-2.389858,7.823638,-3.108430,-2.744032,-4.085319,5.749674,6.929318,0.054286,6.098073,0.340486,1.150370,-6.179510,-4.191517,-7.501481,5.671997,0.267293,0.136660,2.260196,-6.277175,-8.479893,-6.551013,0.580951,0.284285,5.336444,-5.047666,2.832809,6.748471,-5.698332,6.408670,-8.365943,3.078175,-1.313239,-0.926350,5.875880,6.573629,2.446062,0.363448,-1.341156,0.351988,5.419547,-2.292730,6.941811,-2.225760,4.347377,-5.960586,-0.677564,4.890369,-5.388036,-0.005920,5.268613,-2.185707,-3.611357,0.584758,-3.714538,-4.525900,9.304960,-7.523379,-0.094303,-6.459604,-7.799082,9.231235,0.018609,1.036307,4.790694,1.215684,-5.219611,7.331413,8.191474,9.579869,-0.635323,6.088371,-7.272754,-9.857966,-0.702304,-6.083411,-8.955877,5.178304,6.455398,8.269090,3.215040,7.035956,-7.058484,-5.572201,6.940506,3.066683,3.052136,4.599939,4.092556,4.378281,8.681095,-8.163807,5.513445,9.956973,3.032543,1.688605,7.878327,-0.394108,-7.948454,6.570354,-1.795176,0.536680,1.281714,6.787553,-2.152286,-5.416457,-2.472365,5.334617,-7.444912,-2.199358,-7.873739,-7.475436,-1.382133,6.157285,3.211733,0.194261,-3.060795,-2.801167,7.899122,-8.360137,-7.026304,3.331037,1.608283,-8.595364,8.424285,3.229821,6.595587,0.912944,-3.204496,-4.796499,9.011248,0.597187,-3.655180,0.333269,1.601996,3.245647,-6.181269,7.220711,-7.825046,-7.501083,-6.948102,8.895397,2.064212,-3.915000,5.005709,-8.066583,-0.856590,-5.792039,6.593326,-8.142014,2.367771,-1.744095,4.066527,-9.797345,9.039424,0.052696,-5.920159,4.695496,-5.775532,-5.316723,-1.500378,-2.662447,-7.382241,9.110340,8.586696,6.971792,-9.637489,-0.346786,7.737317,4.890881,6.700323,-2.423568,5.621725,-3.703235,0.447122,7.595352,1.551120,-8.046071,4.105593,6.642380,-8.110551,8.766615,-2.505878,-7.563671,-1.198955,-0.130787,-6.956782,-9.483335,2.410045,7.084963,3.971546,-0.014546,6.611507,-5.053174,5.873811,8.711384,-9.762319,-4.469050,-7.423124,-6.377736,-8.493409,5.846790,-2.837729,-8.991483,-9.211254,-9.064948,-0.559037,-0.897996,-6.461337,-3.950096,-6.085630,7.365265,8.253799,6.220354,-7.058366,-2.813895,-7.914078,6.927831,4.824947,-0.088803,-0.456404,9.430592,-6.738238,-2.574822,0.691592,-0.108625,-8.732308,-1.956117,4.648812,3.221441,-5.970143,-6.004871,7.732663,7.765612,3.607314,-3.127937,-3.356055,-6.863721,4.605751,2.725835,-0.376575,-3.201197,2.353223,-3.806455,-3.061248,-1.704570,7.008226,-8.089205,6.189888,-5.784777,5.377019,-6.952287,-2.251324,-7.362449,0.498150,-1.716445,8.147015,-5.313490,-6.911852,3.838205,-7.246227,8.676208,-1.890312,7.232911,1.046598,-2.352979,-5.737387,-2.234621,-7.252002,5.885528,6.753546,8.255477,-5.276985,7.709009,-7.185528,-2.314432,5.651892,-0.920581,4.236444,2.100557,6.475735,3.155791,-8.754922,6.789125,1.516776,-6.762095,-0.870895,2.353747,3.633523,8.864403,-9.676376,-1.328225,8.965672,1.897948,-2.096839,1.705536,1.186562,-9.546208,3.600062,-9.169079,-6.936998,9.833985,-3.307969,6.196539,5.938903,0.250810,-7.623484,3.609528,-2.722636,-5.294085,0.232424,6.026935,3.667925,-0.396020,1.583742,2.778029,9.060078,-5.695160,8.316541,0.946665,7.084924,-6.747020,6.306190], dtype = "float32")#candidate|2820|(2016,)|const|float32
call_2819 = func_825_call(relay.reshape(const_2820.astype('float32'), [9, 14, 16]))
call_2821 = func_825_call(relay.reshape(const_2820.astype('float32'), [9, 14, 16]))
output = relay.Tuple([uop_2776,call_2791,var_2792,call_2814,var_2815,call_2819,const_2820,])
output2 = relay.Tuple([uop_2776,call_2793,var_2792,call_2816,var_2815,call_2821,const_2820,])
func_2822 = relay.Function([var_2792,var_2815,], output)
mod['func_2822'] = func_2822
mod = relay.transform.InferType()(mod)
mutated_mod['func_2822'] = func_2822
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2822_call = mutated_mod.get_global_var('func_2822')
var_2824 = relay.var("var_2824", dtype = "float64", shape = (84,))#candidate|2824|(84,)|var|float64
var_2825 = relay.var("var_2825", dtype = "int32", shape = (1170,))#candidate|2825|(1170,)|var|int32
call_2823 = func_2822_call(var_2824,var_2825,)
output = call_2823
func_2826 = relay.Function([var_2824,var_2825,], output)
mutated_mod['func_2826'] = func_2826
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2895 = relay.var("var_2895", dtype = "float32", shape = (7, 8, 2))#candidate|2895|(7, 8, 2)|var|float32
uop_2896 = relay.cos(var_2895.astype('float32')) # shape=(7, 8, 2)
uop_2899 = relay.exp(uop_2896.astype('float32')) # shape=(7, 8, 2)
uop_2904 = relay.sinh(uop_2899.astype('float64')) # shape=(7, 8, 2)
output = uop_2904
output2 = uop_2904
func_2910 = relay.Function([var_2895,], output)
mod['func_2910'] = func_2910
mod = relay.transform.InferType()(mod)
mutated_mod['func_2910'] = func_2910
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2911 = relay.var("var_2911", dtype = "float32", shape = (7, 8, 2))#candidate|2911|(7, 8, 2)|var|float32
func_2910_call = mutated_mod.get_global_var('func_2910')
call_2912 = func_2910_call(var_2911)
output = call_2912
func_2913 = relay.Function([var_2911], output)
mutated_mod['func_2913'] = func_2913
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3002 = relay.const([[[3,-2,-6,2,1,9,-10],[6,3,-7,8,-1,6,-7],[3,6,1,-5,-3,4,-6],[-3,-10,-10,10,3,9,-8],[-1,3,-5,2,-8,-7,-5]],[[6,-4,8,5,-6,-5,7],[-2,2,-10,-9,-5,2,-9],[-6,-2,4,1,-9,-1,-3],[3,-4,-5,-10,3,-9,-2],[2,2,6,8,9,3,6]],[[-2,-2,-1,1,5,10,-5],[-4,1,-10,4,6,-5,3],[-4,4,10,-2,4,-8,9],[7,-6,-10,-9,-10,4,4],[3,-7,-6,5,-7,-8,2]],[[-2,-3,-4,-9,8,5,-8],[-5,8,10,7,8,-2,8],[-8,8,-1,6,-4,10,-5],[-9,3,5,-4,-9,-3,-4],[2,6,2,9,-7,-9,-3]],[[10,-3,1,6,7,3,2],[1,-2,8,4,-2,-5,9],[9,-2,-8,-1,-1,6,-7],[-2,-4,5,-9,-4,4,5],[6,-3,7,-5,10,-5,10]],[[-9,-8,-8,-5,8,7,-6],[-7,-10,8,-7,9,-10,-7],[10,-6,-6,9,9,-8,-9],[-1,6,7,-1,9,9,-10],[-9,-6,4,-9,8,-6,-3]],[[6,-9,-8,-4,-3,1,5],[-2,-1,-3,1,10,-10,7],[7,-10,3,-1,6,-5,10],[-1,-5,1,-3,2,-4,3],[1,9,9,3,1,-2,-9]]], dtype = "uint64")#candidate|3002|(7, 5, 7)|const|uint64
var_3003 = relay.var("var_3003", dtype = "uint64", shape = (7, 5, 7))#candidate|3003|(7, 5, 7)|var|uint64
bop_3004 = relay.logical_xor(const_3002.astype('uint64'), relay.reshape(var_3003.astype('uint64'), relay.shape_of(const_3002))) # shape=(7, 5, 7)
output = bop_3004
output2 = bop_3004
func_3008 = relay.Function([var_3003,], output)
mod['func_3008'] = func_3008
mod = relay.transform.InferType()(mod)
var_3009 = relay.var("var_3009", dtype = "uint64", shape = (7, 5, 7))#candidate|3009|(7, 5, 7)|var|uint64
output = func_3008(var_3009)
func_3010 = relay.Function([var_3009], output)
mutated_mod['func_3010'] = func_3010
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3139 = relay.const([[[-4,-3,-5,-10,-3,-6,5,-3,-8,2,-8,7,7],[-8,2,1,6,1,-10,-4,7,3,1,-5,-1,-1],[7,-1,-5,-3,4,-3,7,-4,4,-9,-8,-5,10],[-8,-10,-2,-8,-1,-1,9,8,8,9,-2,1,-6],[-6,8,10,9,-8,6,3,10,-10,1,-3,3,4],[5,-9,-2,1,-10,-5,-2,9,8,3,-6,-7,1],[10,3,1,7,8,-4,-9,-1,-5,-7,9,6,5],[5,1,-3,-1,-4,6,-2,-9,3,-3,2,7,2],[-7,8,-2,-6,-10,-5,7,5,9,8,-8,-5,7],[-8,-9,10,9,-1,-10,6,-8,-3,8,-8,7,-4]],[[1,5,1,4,-4,-7,2,-3,-7,-2,-10,9,3],[5,-5,5,2,-6,3,-2,-4,-9,-9,9,-1,-10],[-6,-9,6,10,-4,-1,-5,9,9,-5,4,-9,6],[8,9,-8,-7,-5,-10,-8,10,-3,6,-4,-5,8],[-3,-2,-7,6,-10,-2,-1,2,1,-6,-9,9,10],[2,2,-3,-1,4,5,3,-4,2,1,7,-6,-5],[3,-4,-7,8,-8,-6,8,-6,-2,8,-3,1,6],[8,-2,-9,-8,8,9,7,-9,-8,-5,-9,5,-2],[10,4,3,8,-4,-10,9,-8,-6,-6,9,1,10],[8,-9,-6,6,-5,-2,4,-9,8,4,6,2,8]]], dtype = "int64")#candidate|3139|(2, 10, 13)|const|int64
var_3140 = relay.var("var_3140", dtype = "int64", shape = (2, 10, 13))#candidate|3140|(2, 10, 13)|var|int64
bop_3141 = relay.multiply(const_3139.astype('int64'), relay.reshape(var_3140.astype('int64'), relay.shape_of(const_3139))) # shape=(2, 10, 13)
func_812_call = mod.get_global_var('func_812')
func_815_call = mutated_mod.get_global_var('func_815')
var_3149 = relay.var("var_3149", dtype = "int64", shape = (1, 1792))#candidate|3149|(1, 1792)|var|int64
var_3150 = relay.var("var_3150", dtype = "bool", shape = (12, 1))#candidate|3150|(12, 1)|var|bool
call_3148 = relay.TupleGetItem(func_812_call(relay.reshape(var_3149.astype('int64'), [16, 7, 16]), relay.reshape(var_3150.astype('bool'), [12,]), ), 3)
call_3151 = relay.TupleGetItem(func_815_call(relay.reshape(var_3149.astype('int64'), [16, 7, 16]), relay.reshape(var_3150.astype('bool'), [12,]), ), 3)
uop_3153 = relay.erf(bop_3141.astype('float32')) # shape=(2, 10, 13)
output = relay.Tuple([call_3148,var_3149,var_3150,uop_3153,])
output2 = relay.Tuple([call_3151,var_3149,var_3150,uop_3153,])
func_3156 = relay.Function([var_3140,var_3149,var_3150,], output)
mod['func_3156'] = func_3156
mod = relay.transform.InferType()(mod)
mutated_mod['func_3156'] = func_3156
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3156_call = mutated_mod.get_global_var('func_3156')
var_3158 = relay.var("var_3158", dtype = "int64", shape = (2, 10, 13))#candidate|3158|(2, 10, 13)|var|int64
var_3159 = relay.var("var_3159", dtype = "int64", shape = (1, 1792))#candidate|3159|(1, 1792)|var|int64
var_3160 = relay.var("var_3160", dtype = "bool", shape = (12, 1))#candidate|3160|(12, 1)|var|bool
call_3157 = func_3156_call(var_3158,var_3159,var_3160,)
output = call_3157
func_3161 = relay.Function([var_3158,var_3159,var_3160,], output)
mutated_mod['func_3161'] = func_3161
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3192 = relay.const([[[-2,6,8,-3],[6,5,-5,6],[6,-4,-4,2],[-1,-5,-5,-1],[-3,-10,-1,-1],[6,3,-8,-9],[-4,5,-4,-6],[-2,-4,-5,5],[-9,10,-10,9],[6,-7,4,9],[7,-5,-1,-5],[-1,1,1,-5],[-10,2,-5,8],[-4,4,-9,7],[-6,-6,-3,-9]],[[10,-4,5,3],[4,9,-6,-1],[-10,-10,9,-6],[10,-4,-4,9],[5,7,3,-7],[-3,6,-3,-10],[3,3,-5,-9],[-2,-8,-5,2],[-2,-2,-9,2],[7,-1,-7,3],[-9,4,-7,9],[-7,10,5,4],[3,4,6,3],[-6,-2,-5,4],[3,-10,-4,-4]],[[7,3,-7,1],[4,9,-1,-3],[-7,1,2,-6],[5,9,-4,-10],[-8,6,1,-3],[-3,7,7,3],[5,-7,-9,-5],[-8,4,9,6],[-7,1,10,-5],[10,-8,-1,4],[3,6,4,-6],[8,-8,-4,-2],[-7,-2,-1,-9],[-10,10,8,-1],[3,4,-1,-4]],[[2,3,8,-10],[-10,-1,9,2],[7,-5,3,-7],[-3,8,1,10],[3,1,1,-6],[2,-2,7,4],[-5,10,-5,8],[8,-2,7,-4],[7,4,5,-9],[-9,-1,4,-2],[-4,-8,-9,-7],[-10,8,2,2],[7,7,5,-10],[8,3,-9,-10],[-7,-4,-5,-7]],[[-9,-4,7,10],[1,-6,5,3],[1,3,10,5],[-4,-8,-9,5],[10,-10,-7,-8],[8,-9,2,-6],[7,-1,5,-8],[4,-9,1,-2],[5,-5,-2,1],[7,-3,-1,9],[8,-8,-7,-5],[10,-5,-8,-1],[1,-5,7,1],[7,2,-4,-9],[3,9,-4,5]],[[8,5,9,1],[2,-10,-4,-4],[8,-1,8,-7],[7,-3,10,-5],[7,6,-7,-5],[3,-7,-8,-9],[6,-1,2,-5],[3,2,-5,-2],[8,-8,5,4],[-1,-6,-10,7],[9,-2,5,-1],[-5,-2,1,-3],[-3,4,6,-9],[-8,6,-2,-6],[1,1,3,-2]],[[5,1,9,-5],[-4,-4,6,5],[-8,2,4,-2],[-5,-10,-5,9],[8,5,3,-2],[8,7,-9,10],[5,-9,9,5],[4,-4,-8,8],[4,-5,-5,4],[-3,9,-5,-1],[-10,-1,-10,5],[-4,3,-6,9],[-4,7,-1,3],[3,-8,-3,-1],[7,-4,-10,3]],[[1,-7,-6,-5],[1,2,-4,-8],[8,-5,4,6],[8,10,-10,-4],[-10,-6,-7,9],[-2,10,7,-2],[3,-8,3,-10],[-3,-3,-5,1],[-7,-4,-9,-4],[7,6,-3,10],[6,-5,-3,4],[-5,-8,1,8],[8,4,-6,-8],[-4,6,5,-3],[6,-1,-1,5]],[[-1,6,4,-2],[5,-2,6,-3],[-6,-6,-5,-3],[-7,9,9,-5],[7,-4,5,-3],[-4,1,-5,-10],[3,4,-7,10],[3,-5,1,5],[-9,-9,5,-5],[9,8,-2,8],[6,-5,9,8],[-5,4,-3,6],[-8,-8,-10,-1],[-1,-4,-9,10],[4,-10,-3,7]],[[-3,5,-2,8],[9,2,-9,8],[-3,-4,-7,-8],[2,-6,-8,4],[-3,-7,-2,-2],[3,10,-8,3],[-1,4,3,-8],[1,9,-4,3],[4,2,-9,6],[-10,-3,5,10],[4,3,-7,2],[5,-9,8,8],[-4,-7,7,-4],[-10,-7,-4,10],[-2,-7,5,7]]], dtype = "int32")#candidate|3192|(10, 15, 4)|const|int32
var_3193 = relay.var("var_3193", dtype = "int32", shape = (10, 15, 4))#candidate|3193|(10, 15, 4)|var|int32
bop_3194 = relay.bitwise_or(const_3192.astype('int32'), relay.reshape(var_3193.astype('int32'), relay.shape_of(const_3192))) # shape=(10, 15, 4)
func_3008_call = mod.get_global_var('func_3008')
func_3010_call = mutated_mod.get_global_var('func_3010')
const_3200 = relay.const([6,7,-7,-1,-9,-6,-2,-6,-8,9,10,-9,-6,-5,4,4,-3,3,-10,-7,-5,-3,7,-3,8,3,6,1,9,-2,1,5,9,-4,-10,-7,-5,1,2,6,-8,8,-3,7,-6,-4,-7,4,5,-6,-10,-2,-5,-8,-9,-7,-5,10,-5,-7,5,9,-10,-9,-1,-2,10,-8,6,-2,-2,1,-5,3,-7,-10,-4,4,1,1,-2,5,-4,7,-10,-7,7,10,-9,1,-7,-6,-9,7,8,4,-10,2,-3,-5,5,7,-10,-5,2,-4,-6,-2,-3,-4,6,2,6,-1,10,-2,-10,8,-6,10,10,6,4,-8,-8,1,8,-1,5,3,-8,2,-6,9,-5,1,-4,-9,7,-7,-10,9,10,-4,2,10,-4,1,5,1,10,3,-1,2,2,2,-8,1,1,-4,-3,-4,-9,9,4,1,-4,-7,1,-10,9,-4,-3,4,8,-8,2,-2,-6,2,10,5,10,-8,1,3,-2,-6,9,10,6,2,9,-9,-4,-8,-6,8,-4,8,-4,7,7,-10,3,-6,9,9,4,4,2,-2,-4,-8,-9,-8,-7,-9,-8,3,-1,10,-10,8,10,-2,6,1,-6,-2,5,-8,-5,-1,7,4,-4,10,5,8,3,-8,-3,1,-7], dtype = "uint64")#candidate|3200|(245,)|const|uint64
call_3199 = func_3008_call(relay.reshape(const_3200.astype('uint64'), [7, 5, 7]))
call_3201 = func_3008_call(relay.reshape(const_3200.astype('uint64'), [7, 5, 7]))
output = relay.Tuple([bop_3194,call_3199,const_3200,])
output2 = relay.Tuple([bop_3194,call_3201,const_3200,])
func_3214 = relay.Function([var_3193,], output)
mod['func_3214'] = func_3214
mod = relay.transform.InferType()(mod)
mutated_mod['func_3214'] = func_3214
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3215 = relay.var("var_3215", dtype = "int32", shape = (10, 15, 4))#candidate|3215|(10, 15, 4)|var|int32
func_3214_call = mutated_mod.get_global_var('func_3214')
call_3216 = func_3214_call(var_3215)
output = call_3216
func_3217 = relay.Function([var_3215], output)
mutated_mod['func_3217'] = func_3217
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3634 = relay.const([[[9,-2,7,3,5,-7,2,-4,6,-8,-4,-3],[-1,-7,-7,10,6,-7,2,-1,1,-9,-3,-3],[-3,-6,-1,-5,3,-9,-6,-6,-1,-7,4,-9],[5,10,-2,-9,-4,-1,1,1,5,4,-9,4],[-5,2,-9,4,8,2,-7,-5,5,7,-10,-1],[6,-8,8,-6,5,2,-8,7,-10,-8,-9,5],[-8,3,-9,-5,-2,4,7,10,-8,5,9,-6],[9,4,-6,4,-3,6,-3,-9,-5,2,-2,3],[7,10,8,-4,7,-6,1,10,9,4,-8,5],[-7,-5,-1,3,-6,5,6,-10,-1,7,-8,-4],[5,-7,2,-6,10,1,2,1,-4,2,8,-4],[-10,-9,-10,-5,10,7,5,4,-7,-7,7,-8],[6,3,-4,3,8,10,6,2,-7,-9,-4,-8],[-5,1,6,-5,9,-6,-4,7,-2,9,-4,3],[10,6,4,7,2,5,7,-8,-7,1,5,1],[-7,-5,-3,-2,10,-7,3,-8,-1,-3,-3,9]]], dtype = "uint64")#candidate|3634|(1, 16, 12)|const|uint64
const_3635 = relay.const([[[-1,-8,-10,-5,7,3,1,9,-2,3,7,4],[-6,-3,7,5,-2,10,-9,9,5,5,-9,-3],[9,10,-1,6,-1,2,-8,-6,1,4,-5,8],[-7,3,7,7,-5,2,3,-5,8,2,6,8],[-8,-9,-9,2,-10,-2,-4,-3,-7,-6,6,5],[-9,-1,9,-4,4,-1,-10,9,-9,-7,1,1],[-8,10,-8,-7,4,-4,9,-1,3,8,-4,-3],[9,5,1,-1,4,-10,-6,9,-7,4,-3,1],[-6,9,-5,4,-10,5,6,-10,-7,1,9,5],[7,4,-4,-5,-3,2,-5,-3,3,8,-5,-10],[-1,6,-2,-8,10,-8,8,-5,-8,-10,-1,-9],[2,-6,8,-9,-8,10,6,1,-1,-8,-4,1],[-2,-4,5,-9,-5,-6,-2,3,-10,4,-1,1],[5,1,4,9,3,9,1,7,-5,-8,-7,-1],[-3,4,9,6,-7,-3,-6,-7,8,-7,5,4],[6,-1,2,-2,6,-9,-1,8,1,-9,4,6]],[[-3,2,8,2,-7,-6,4,5,4,-6,10,-1],[5,-8,7,2,8,1,-9,7,-7,-6,3,-10],[7,1,10,-8,3,6,9,-1,-4,-2,-7,-1],[-4,-5,10,3,1,-5,-6,-8,9,9,1,-5],[-6,10,-6,10,-9,6,-2,9,2,6,6,-7],[7,-3,9,5,-4,9,-7,-1,-3,6,-7,9],[-8,7,1,9,9,-8,1,-4,-10,5,3,2],[5,1,4,1,-9,9,10,7,1,10,9,-5],[6,-4,7,4,7,-4,-9,6,3,5,-3,-5],[-8,-6,-8,5,2,2,7,-3,-5,-5,4,-2],[7,2,-2,4,-3,-6,-1,4,10,5,6,-2],[-5,-5,8,-3,9,-5,-2,10,7,-6,-8,-2],[-10,8,4,-7,6,-5,-3,9,6,2,1,3],[1,8,2,10,8,-8,-5,-9,-10,5,-5,-3],[8,-8,9,-9,-5,-10,9,-10,5,9,-4,-10],[5,8,-2,2,8,9,5,8,8,-6,-7,6]],[[-4,-3,-5,3,-10,1,-1,2,-5,7,-2,10],[4,-9,-2,-6,-9,-5,3,4,8,-7,-10,-8],[-1,-9,-1,-3,4,-9,-4,-3,3,-7,5,-4],[-9,-1,2,-8,-4,6,-5,-4,8,7,8,6],[7,10,7,4,6,8,5,-9,-4,-8,-3,-10],[-6,6,7,5,-7,10,10,-3,1,6,-9,5],[-1,2,5,-6,9,5,2,-3,-9,-5,7,7],[9,-4,-8,2,3,-3,6,-1,9,-2,-8,-2],[-10,-7,-4,6,8,2,10,7,-5,-4,-10,-7],[-1,-2,8,7,2,4,8,9,-10,4,-4,3],[-1,-2,2,-10,10,3,5,-5,-3,2,9,-9],[-4,-10,4,-10,10,6,1,4,-5,9,-8,8],[3,5,3,4,-1,-8,8,9,-9,-2,10,-4],[-3,-4,9,-4,-4,-8,-7,6,5,-2,-1,-2],[8,3,-10,-3,-1,-5,1,-5,-10,-9,3,4],[9,-2,-7,-3,10,2,-2,-4,4,-3,1,-7]],[[9,8,3,-2,8,-5,10,-1,-3,-2,-8,9],[-8,-4,-10,-1,-8,3,-1,-6,-10,-5,10,-3],[-8,9,3,-7,-10,-9,-3,1,1,5,-10,-2],[-1,-3,10,-3,2,4,1,6,4,4,-8,-1],[1,-1,-4,-3,8,5,3,8,-1,9,-6,3],[-10,9,2,-7,5,-5,-8,5,6,6,7,3],[10,10,-6,-8,-8,8,-1,2,-2,-7,7,8],[2,-5,10,9,-1,-6,9,-7,4,-6,8,-9],[7,1,-7,-1,5,-8,-3,4,5,1,5,1],[-1,4,-7,2,-10,1,-3,6,6,2,-10,-3],[8,9,2,-5,-6,-4,4,8,8,9,10,9],[9,9,-10,6,-6,3,4,-1,-9,-3,1,-6],[9,-10,3,8,1,-3,10,8,4,-4,-3,9],[1,4,-1,3,-8,-10,-4,-2,6,7,7,-1],[-9,1,1,-4,10,-6,-10,3,-6,6,-3,-7],[6,-4,9,5,-8,10,6,2,1,9,1,-9]],[[6,6,-6,8,-7,6,-6,4,9,5,-9,1],[7,1,-3,4,8,9,-3,7,-9,-5,-7,-1],[4,-2,-3,3,7,7,-6,9,10,-9,5,2],[10,9,8,-4,5,5,2,-7,4,7,6,-8],[-6,-1,3,-6,-1,-10,4,1,-1,7,-6,10],[-8,-2,7,-3,6,-3,-7,2,4,9,6,-7],[-8,-10,-9,-4,1,3,5,8,-2,-2,10,9],[6,1,-9,10,-5,10,5,2,2,-2,3,-10],[-3,-6,-6,4,-4,-5,5,10,8,-3,6,8],[1,6,-4,-9,-9,-9,-9,-7,9,-7,7,-2],[9,-9,9,4,-9,-5,7,9,10,-10,-10,3],[-9,2,10,-3,9,6,1,-9,-2,-3,-10,-6],[-8,-1,-5,8,7,-2,-5,-5,-8,4,5,-10],[-10,8,5,2,10,2,2,-9,-1,5,7,10],[-3,7,-8,4,9,-1,6,8,1,-1,-1,9],[3,-7,3,10,-2,5,3,9,3,-8,5,3]],[[5,6,-6,7,-10,4,2,1,-2,-3,8,-8],[-3,-8,-10,4,-6,-3,-7,6,5,-1,3,-8],[-10,9,-4,-9,-3,5,9,-1,10,-1,-6,-2],[-6,-7,-5,-5,7,-3,3,6,-8,-1,8,1],[-10,5,-9,5,10,-6,7,9,5,3,-1,-6],[-9,5,-3,-7,1,6,-9,-5,5,3,3,5],[4,-8,10,4,-2,-9,7,7,8,-10,-4,-5],[8,-10,9,-1,-7,8,2,5,2,1,9,-9],[-9,3,6,2,-5,-7,10,-7,-6,2,-6,-3],[2,8,-10,-10,8,4,-1,-7,9,-3,1,-5],[5,-6,6,-1,-3,-2,6,2,5,-7,2,-5],[10,-1,-9,10,8,7,5,-2,7,-1,-6,-8],[-9,-9,10,4,-3,-5,-5,-8,-10,7,-3,4],[-5,-4,8,-3,-8,9,-6,10,-10,-2,9,-10],[-5,4,7,9,-3,-4,4,7,10,9,-9,-5],[-3,5,-5,1,-1,-9,5,2,-10,6,-8,7]],[[8,-3,-7,5,-3,4,-5,-9,1,7,-5,-3],[-7,-10,-3,2,5,6,4,-3,-10,-9,3,-3],[6,-2,9,8,6,3,-5,9,-2,1,4,7],[1,1,5,-10,-4,-4,8,2,-9,3,2,5],[5,-2,-10,-7,6,-4,-3,-2,7,-1,9,10],[8,2,-3,4,5,-1,6,5,-7,2,5,7],[1,8,-3,6,2,-1,-8,-5,2,5,3,7],[3,9,3,-4,6,-4,2,10,1,1,8,-10],[1,8,9,5,7,2,10,6,-9,4,-2,7],[8,1,-3,8,-8,9,2,-1,-6,10,-10,1],[-7,-3,1,-2,-6,-9,-6,3,3,-3,-6,5],[9,9,2,-1,6,9,3,-8,-6,8,-4,-6],[-4,2,-5,-3,4,4,-1,6,8,-7,-9,-10],[4,5,-10,4,1,-4,-5,-1,-9,5,-3,-7],[8,-3,-1,-2,-2,2,9,4,4,-8,-4,-5],[7,3,3,-10,6,-8,6,-9,-6,-8,8,6]]], dtype = "uint64")#candidate|3635|(7, 16, 12)|const|uint64
bop_3636 = relay.greater_equal(const_3634.astype('bool'), const_3635.astype('bool')) # shape=(7, 16, 12)
bop_3639 = relay.less(bop_3636.astype('bool'), relay.reshape(const_3635.astype('bool'), relay.shape_of(bop_3636))) # shape=(7, 16, 12)
output = relay.Tuple([bop_3639,])
output2 = relay.Tuple([bop_3639,])
func_3642 = relay.Function([], output)
mod['func_3642'] = func_3642
mod = relay.transform.InferType()(mod)
output = func_3642()
func_3643 = relay.Function([], output)
mutated_mod['func_3643'] = func_3643
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3642_call = mod.get_global_var('func_3642')
func_3643_call = mutated_mod.get_global_var('func_3643')
call_3656 = relay.TupleGetItem(func_3642_call(), 0)
call_3657 = relay.TupleGetItem(func_3643_call(), 0)
func_2458_call = mod.get_global_var('func_2458')
func_2461_call = mutated_mod.get_global_var('func_2461')
var_3659 = relay.var("var_3659", dtype = "int32", shape = (10, 117))#candidate|3659|(10, 117)|var|int32
call_3658 = relay.TupleGetItem(func_2458_call(relay.reshape(var_3659.astype('int32'), [9, 13, 10]), relay.reshape(var_3659.astype('int32'), [9, 13, 10]), ), 0)
call_3660 = relay.TupleGetItem(func_2461_call(relay.reshape(var_3659.astype('int32'), [9, 13, 10]), relay.reshape(var_3659.astype('int32'), [9, 13, 10]), ), 0)
var_3665 = relay.var("var_3665", dtype = "int32", shape = (10, 117))#candidate|3665|(10, 117)|var|int32
bop_3666 = relay.right_shift(var_3659.astype('uint64'), relay.reshape(var_3665.astype('uint64'), relay.shape_of(var_3659))) # shape=(10, 117)
output = relay.Tuple([call_3656,call_3658,bop_3666,])
output2 = relay.Tuple([call_3657,call_3660,bop_3666,])
func_3679 = relay.Function([var_3659,var_3665,], output)
mod['func_3679'] = func_3679
mod = relay.transform.InferType()(mod)
var_3680 = relay.var("var_3680", dtype = "int32", shape = (10, 117))#candidate|3680|(10, 117)|var|int32
var_3681 = relay.var("var_3681", dtype = "int32", shape = (10, 117))#candidate|3681|(10, 117)|var|int32
output = func_3679(var_3680,var_3681,)
func_3682 = relay.Function([var_3680,var_3681,], output)
mutated_mod['func_3682'] = func_3682
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3689 = relay.var("var_3689", dtype = "int16", shape = (6, 15, 2))#candidate|3689|(6, 15, 2)|var|int16
var_3690 = relay.var("var_3690", dtype = "int16", shape = (6, 15, 2))#candidate|3690|(6, 15, 2)|var|int16
bop_3691 = relay.right_shift(var_3689.astype('int16'), relay.reshape(var_3690.astype('int16'), relay.shape_of(var_3689))) # shape=(6, 15, 2)
uop_3694 = relay.acos(bop_3691.astype('float32')) # shape=(6, 15, 2)
func_2822_call = mod.get_global_var('func_2822')
func_2826_call = mutated_mod.get_global_var('func_2826')
var_3697 = relay.var("var_3697", dtype = "float64", shape = (84, 1))#candidate|3697|(84, 1)|var|float64
const_3698 = relay.const([6,8,2,-2,-5,-10,-8,2,-2,8,-1,7,-7,8,-3,-9,-7,-5,-4,-1,7,-4,4,2,6,1,3,3,-9,7,4,-1,3,-1,-4,-10,2,10,1,-2,-4,-6,-9,8,4,1,1,10,-9,-3,-1,-8,6,-1,-9,-5,5,9,2,3,-3,5,-6,8,-6,-8,1,-2,-3,-3,7,3,-1,6,-10,-1,-1,6,1,-3,-6,-4,9,5,8,-2,6,-6,8,10,3,2,8,-3,4,6,7,9,3,-7,10,7,-5,-4,-7,2,10,3,-1,-6,10,-7,9,4,7,-6,-1,6,-8,-8,9,-2,-1,6,1,9,4,-2,-1,7,-8,-7,-6,2,5,8,9,2,6,1,10,9,-7,6,-7,-6,-6,3,-7,-7,-6,-6,-6,4,6,9,9,-7,1,2,8,5,2,9,5,-10,2,10,4,-8,-1,-6,5,7,-9,-3,9,-3,6,-10,8,5,-8,6,9,4,-2,-2,-4,-2,10,-1,5,-9,6,3,-1,-3,-5,1,-6,-6,5,-5,9,-5,-5,7,10,1,7,-1,-6,7,5,5,-5,10,-3,1,2,-10,-2,-9,6,2,5,4,-10,-3,3,6,3,9,1,-7,-8,4,-5,-6,-2,-6,2,10,-1,6,-5,1,10,-5,10,8,10,-9,4,7,2,4,-3,5,-1,7,7,5,8,10,1,-5,1,-7,-9,-2,-8,-6,-5,5,4,-2,-8,8,-7,3,8,1,1,-4,-2,1,5,3,8,3,-9,-5,-4,-4,-1,10,-4,9,-9,-8,-9,3,8,-1,-3,10,-1,-9,-8,-7,8,10,-10,-1,-2,-10,-2,5,8,-6,-2,10,-3,-2,2,10,9,-5,-9,-8,7,-1,10,7,-2,8,1,-9,9,-5,-1,2,-7,10,3,-6,-5,-9,5,-4,1,2,2,-8,3,3,-10,-5,-1,-4,3,7,9,3,-4,-2,9,-10,-5,5,4,3,4,-3,-5,1,9,5,6,3,-5,6,8,8,-4,3,-10,4,-6,-8,5,10,1,-3,3,6,10,-1,-10,10,-1,-2,1,4,-2,-10,-6,-3,4,-4,2,5,4,8,7,7,-3,7,-4,1,5,-5,10,8,3,-2,-1,-7,-3,8,3,7,4,-9,-7,6,-2,3,-10,9,-2,-8,-8,-8,10,-2,-1,8,-3,2,9,-3,9,-4,-8,4,-4,3,-7,-2,6,9,-2,-3,-6,-4,2,-8,5,2,5,-3,8,8,6,-4,5,-10,-2,2,7,-5,-5,-2,4,-4,-1,5,-3,-7,-4,-9,-4,-6,1,6,-3,-7,-3,9,-4,-4,9,6,-4,-9,2,9,-9,2,-2,6,-9,-2,-3,-10,3,3,5,4,-2,10,-10,-2,6,9,-4,1,-9,8,5,2,-3,-10,6,-8,6,4,8,5,4,10,-10,-3,-8,-2,10,1,-8,-2,6,3,-7,-9,7,-9,-9,-8,1,-7,-6,-10,-2,-10,5,-5,1,4,-6,-2,-9,1,9,-7,5,-7,-3,-7,-9,5,8,-6,7,6,-5,6,9,-3,9,7,8,-4,3,7,-10,-8,2,9,6,-3,-6,-8,-8,-3,3,-2,-6,-1,2,2,10,-4,6,2,-1,-6,5,3,-4,-2,-8,7,5,-4,-8,10,-8,10,8,-7,-6,5,4,-7,-4,-5,-5,6,-4,6,-7,-2,1,-9,4,7,7,-3,1,9,-9,8,9,-6,6,-5,-10,-8,-8,7,2,-4,-7,-10,-7,4,1,9,-7,3,7,-6,4,8,-2,-4,1,1,-2,-6,10,-4,3,-3,10,-4,3,-6,8,8,10,-2,7,9,-6,10,-7,7,2,2,5,1,-10,2,10,5,2,-3,3,-10,-8,-5,9,-7,-1,4,-7,-1,-3,-2,-4,5,6,-7,-9,-8,-1,4,-4,-10,-1,10,-1,-4,7,-7,3,-7,7,10,2,5,-2,3,1,2,10,-10,4,-3,-10,-1,10,3,-3,5,10,9,10,-7,-5,-5,-10,4,-10,2,7,4,3,-7,2,-2,-6,4,10,9,10,-10,2,4,-1,2,10,-5,5,9,-6,10,1,7,7,7,-1,-8,1,5,-8,9,-6,3,8,1,-3,5,-4,5,2,9,-1,6,-8,-5,9,6,-8,-7,3,10,8,1,-10,3,10,-5,10,-4,-2,5,-3,-7,4,-9,1,-4,-5,-10,1,8,7,4,-7,-4,-9,2,-3,-5,2,-3,-3,1,10,-4,-3,4,-10,-7,-1,7,1,-2,-8,-1,-2,5,-9,-3,6,-2,4,10,8,-10,-8,9,-4,-4,-1,-5,9,-6,6,9,-1,-10,-1,-6,8,8,-10,-3,-1,9,4,-4,-5,3,-2,-3,7,7,-6,7,-10,7,-5,6,-9,-7,-2,8,-1,-1,7,-7,1,-2,-8,10,7,8,10,-7,3,-4,7,4,-4,3,3,6,6,9,-1,2,8,10,-5,9,-3,7,-6,7,8,-3,-2,4,-9,1,-4,5,-2,10,-4,-9,1,-4,-9,-6,3,-9,-10,-4,-6,8,6,3,-10,7,-3,8,2,-10,-7,7,8,6,9,-7,-4,4,-8,-10,-10,-2,-5,7,-4,-10,7,-10,5,3,7,8,4,-3,-9,-1,-4,-3,3,8,-9,8,-10,-1,8,9,-5,-9,1,1,7,-2,-7,9,5,9,10,9,10,4,-5,3,2,-9,4,-4,6,-1,10,-4,9,-10,3,-6,-1,-10,3,-8,-7,-9,-9,-1,10,-9,-2,-7,6,-8,9,3,6,8,-1,6,5,9,10,-10,-10,5,2,2,1,9,6,10,9,1,4,8,-3,-3,6,7,2,9,6,-4,-3,-7,-6,1,6,-7,-9,10,-1,7,10,-5,-8,6,8,-8,-2,-10,-3,6,-2,10,8,-3,6,-8,8,9,-10,7,-7,-8,2,-9,-8,-4,8,2,-5,4,-7,-10,-6,8,-3,3,-3,-9,9,-10,5,-9,-2,-8,6,-10,6,9,-6,9,3,1,3,1,-10,-2,8,7,-2,7,-10,-2,-7,-10,7,4,3,6,-7,-1,9,-1,5,-5,6,-5,-8,-5], dtype = "int32")#candidate|3698|(1170,)|const|int32
call_3696 = relay.TupleGetItem(func_2822_call(relay.reshape(var_3697.astype('float64'), [84,]), relay.reshape(const_3698.astype('int32'), [1170,]), ), 0)
call_3699 = relay.TupleGetItem(func_2826_call(relay.reshape(var_3697.astype('float64'), [84,]), relay.reshape(const_3698.astype('int32'), [1170,]), ), 0)
output = relay.Tuple([uop_3694,call_3696,var_3697,const_3698,])
output2 = relay.Tuple([uop_3694,call_3699,var_3697,const_3698,])
func_3702 = relay.Function([var_3689,var_3690,var_3697,], output)
mod['func_3702'] = func_3702
mod = relay.transform.InferType()(mod)
mutated_mod['func_3702'] = func_3702
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3702_call = mutated_mod.get_global_var('func_3702')
var_3704 = relay.var("var_3704", dtype = "int16", shape = (6, 15, 2))#candidate|3704|(6, 15, 2)|var|int16
var_3705 = relay.var("var_3705", dtype = "int16", shape = (6, 15, 2))#candidate|3705|(6, 15, 2)|var|int16
var_3706 = relay.var("var_3706", dtype = "float64", shape = (84, 1))#candidate|3706|(84, 1)|var|float64
call_3703 = func_3702_call(var_3704,var_3705,var_3706,)
output = call_3703
func_3707 = relay.Function([var_3704,var_3705,var_3706,], output)
mutated_mod['func_3707'] = func_3707
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3642_call = mod.get_global_var('func_3642')
func_3643_call = mutated_mod.get_global_var('func_3643')
call_3719 = relay.TupleGetItem(func_3642_call(), 0)
call_3720 = relay.TupleGetItem(func_3643_call(), 0)
func_812_call = mod.get_global_var('func_812')
func_815_call = mutated_mod.get_global_var('func_815')
const_3726 = relay.const([[-4,5,-9,9,-6,5,9,9,2,7,-6,-10,-2,-1,-6,4,-9,-4,-9,-8,4,-4,-7,-9,10,6,-2,10,-7,8,-6,-3,-3,-5,10,7,7,6,-6,-4,1,-2,-6,7,-3,-9,7,-4,-7,-1,4,-10,1,4,1,6,8,4,-10,9,6,-2,10,-3,7,-1,-4,-2,6,-4,4,10,-8,7,-5,-3,6,6,-1,2,-5,-9,-3,3,6,10,-7,-3,-5,5,1,-3,-3,-3,-7,2,-8,-10,1,4,-5,7,-7,9,3,3,9,-2,-8,7,-10,9,2,-10,-5,10,1,1,2,-1,3,-10,4,7,7,-7,-4,4,6,-1,-2,-2,-10,2,-5,8,7,-2,-10,-2,4,-1,-6,6,-2,-4,8,7,10,-4,2,-5,-10,1,8,6,-1,-2,-5,-8,5,-1,-7,-5,-10,10,-10,3,3,-9,-7,3,-3,6,5,-5,5,5,4,7,-6,-8,-3,6,4,7,2,1,6,5,9,-2,-4,6,-5,-4,9,9,2,8,-5,-9,-4,4,8,-9,-9,-3,8,-5,-10,5,-10,3,-4,-9,-7,-7,1,-1,3,5,-1,-9,6,3,2,9,-6,7,5,-8,6,-5,7,3,-6,-3,7,-7,5,-10,7,10,-4,-3,5,-3,-7,8,-2,3,9,6,-8,-10,-2,10,10,5,9,4,1,2,4,1,3,8,8,10,7,-8,10,2,-10,-7,9,2,7,-8,-6,-10,1,-10,2,-6,10,1,4,4,-2,-2,2,-1,-9,-1,7,1,1,-8,3,-3,-2,5,-10,9,-1,3,4,-2,4,-8,-9,9,-2,3,3,-8,-2,10,-3,-6,-9,-8,4,5,-5,8,-2,4,-4,-7,4,-3,-10,10,9,10,6,10,-7,-7,8,6,2,1,-6,-2,-6,1,-7,1,-9,-5,-8,5,2,8,9,9,4,7,2,4,-4,4,-8,-9,-6,3,1,-9,-2,-2,-3,-2,5,-8,-9,-3,-9,-8,3,-3,-4,-5,6,10,1,1,-5,10,4,-4,-2,10,7,-8,7,-3,10,8,2,-4,-9,6,9,5,7,8,10,1,-6,-10,-2,4,1,-6,9,5,-6,-4,-10,-8,-8,-6,-6,6,6,5,-10,-10,10,-3,9,-6,10,9,9,-7,-6,7,-10,4,-10,-5,-9,-9,-2,-9,-2,-5,-5,4,-4,2,4,1,-4,-1,5,3,3,-2,-8,-6,-6,-3,-5,-6,8,8,9,7,6,8,-3,5,6,-3,-6,5,9,-4,6,5,10,-7,7,-4,3,-4,6,-4,-7,-9,5,-7,-3,-1,1,-7,3,9,10,-5,-9,9,10,-8,-8,10,-2,-10,-7,5,8,6,8,3,3,8,7,-7,-1,-4,3,-4,10,-9,-4,-5,-8,6,-8,-3,7,1,9,2,3,10,-9,-1,6,-8,-6,-3,-1,2,9,10,-7,9,1,7,-7,-9,1,5,-2,10,-3,-4,-3,6,10,-8,-9,6,-8,3,1,-2,-4,2,2,-3,4,-1,-4,8,3,2,3,-1,2,-8,5,-5,-1,-6,10,7,-9,-2,-5,6,6,-9,7,-2,3,-1,-4,-9,5,5,7,9,10,8,2,3,-3,7,-2,10,-2,2,-7,-8,-8,-8,-7,-10,8,10,9,10,-6,3,-7,-1,-4,-5,-8,1,-8,-1,-6,1,7,6,7,-10,-4,-10,8,1,6,10,9,-10,-10,1,9,2,5,2,3,-4,-6,7,6,5,2,-6,9,-9,4,-7,-3,-7,-6,-8,-2,5,7,-4,-9,-2,6,-3,3,-6,-3,-10,-1,-5,-7,-7,5,8,1,4,-1,-3,6,2,8,-8,10,-7,4,-9,5,3,7,4,3,9,4,-3,-8,2,4,6,8,6,-5,7,2,-2,9,-6,-3,8,-7,-2,7,-10,3,-4,1,-3,6,8,7,-8,5,-3,-1,8,2,-2,3,10,9,-7,4,9,-9,2,9,6,-4,-4,10,2,3,10,7,2,-4,8,-10,-9,-6,-6,-1,-10,-1,-9,-6,4,-4,-5,-6,8,-5,-9,-7,-3,1,9,4,-6,-4,6,5,-9,-6,-1,1,-2,10,-1,-10,-10,-6,3,-8,4,4,-2,-2,8,-5,-10,-10,5,6,7,-4,6,-7,9,8,9,-5,-10,4,-7,-1,-7,3,-3,10,4,-8,-4,-1,-2,8,2,-2,4,-2,-5,10,-4,-4,2,6,7,-6,6,-6,8,-10,1,3,-8,-6,8,6,1,-8,5,-8,-5,-5,-4,1,-7,2,-5,-3,2,9,-7,1,-3,8,-2,-10,3,-1,-8,-8,-5,5,9,-6,-9,-10,-8,-4,-3,-10,-9,3,-8,8,7,5,10,4,9,-8,-3,-7,-3,-3,-3,1,-3,-5,-9,9,1,-9,-5,8,-5,4,-9,8,-2,-8,1,-9,4,-7,9,10,-9,10,-4,-8,9,6,5,-1,4,-1,7,-3,-6,-5,-4,6,5,-7,-6,-9,-9,4,8,8,-5,1,3,-4,-2,-5,-5,2,-6,-1,6,-1,3,-8,1,7,6,-7,-1,9,1,4,4,-5,6,5,4,-6,1,1,9,9,5,-6,8,-4,9,6,3,-4,-7,-1,-4,1,-3,9,-10,9,6,-4,3,5,5,7,-3,8,-1,5,10,-5,8,-4,4,-4,1,7,7,7,-3,1,-7,-8,-2,6,-8,-2,4,-5,-1,1,6,-7,-9,-4,-1,10,7,-6,2,-8,2,-9,10,-9,2,3,7,10,4,-8,-2,-3,-8,-6,3,-3,8,5,3,-8,-3,2,1,-6,9,-2,-2,-9,-5,3,3,-3,7,8,2,-6,9,3,-1,6,2,-10,-6,9,4,-9,7,7,-2,3,-2,-6,-6,-10,-9,6,6,-8,-4,4,-8,-6,-7,-8,-9,2,9,-10,-1,3,-7,-1,-6,7,-7,-2,6,-1,-1,3,-9,1,4,-4,-10,-5,7,-1,-9,5,-1,-5,4,-9,5,5,8,-4,5,-9,5,5,-4,-5,7,10,-4,5,1,3,8,1,-3,-10,3,7,-5,-9,1,1,1,-5,8,-5,6,6,7,1,4,-10,1,6,10,-5,9,-10,-7,9,7,-4,-1,8,-10,8,10,-1,-5,-9,4,9,-1,-6,-4,-6,9,3,-2,10,9,6,-7,-2,-5,9,-6,3,-7,-8,3,1,3,4,4,7,-1,3,-9,-10,8,4,-10,-3,-5,10,-4,10,7,-5,7,4,-5,5,4,10,5,-7,-10,-3,-1,5,-6,-5,10,-5,3,4,-8,4,4,-5,-8,5,-3,5,5,-1,6,5,-7,-4,2,8,6,-6,-6,1,-3,3,7,8,-1,-5,5,4,10,2,-5,6,4,4,-10,5,-1,7,-8,2,-6,-6,-6,-6,-10,10,1,-9,-5,5,7,-1,10,-6,5,-10,4,-5,-8,-7,-9,4,-3,5,3,5,3,8,-6,-2,4,-3,9,1,8,6,4,-7,2,-7,5,-6,-8,2,1,-6,-7,5,6,5,-3,1,-2,6,-4,10,-7,-8,3,10,5,10,4,7,-5,-3,-5,8,5,-1,9,8,10,-2,7,8,7,-3,-7,-10,-5,1,-9,7,-6,-5,-2,2,3,4,7,2,-1,-6,7,1,1,4,-2,6,-1,-3,-7,4,1,8,1,-4,6,3,6,-7,-7,-4,2,-8,-2,6,8,-7,-10,-6,8,-5,10,8,-5,10,6,2,-6,2,1,-9,-10,9,5,2,7,-6,9,-2,10,6,-8,5,9,5,-7,-1,1,8,-7,-7,-2,-1,10,-5,5,-8,8,-8,3,8,-6,-7,-1,2,9,-2,4,-2,-5,7,-6,3,-8,-2,-4,1,1,6,-4,8,8,4,3,10,-1,-8,-2,3,-3,1,5,-7,9,-8,2,6,-6,-5,6,-7,-2,8,-9,4,-5,-1,-4,-1,-2,5,5,-5,4,1,7,1,-4,-3,-9,7,9,-8,-4,5,-6,-1,2,3,10,-5,2,6,4,-1,4,7,-3,8,4,5,-6,2,-6,3,8,3,-6,8,-6,-3,4,-8,6,6,1,-1,-2,4,-7,6,-7,-9,-7,4,-5,-8,8,-8,3,-6,7,-1,10,9,-4,-7,1,5,1,3,-8,-7,-6,1,-8,4,-4,-6,-2,-6,-9,1,-6,-10,-6,5,4,10,-8,7,-10,3,8,10,4,8,6,-3,-6,1,6,7,1,-9,-8,5,7,-2,9,7,-8,7,6,10,5,-5,-9,-10,-10,9,5,-8,2,-9,3,-4,-3,-7,-3,1,8,8,8,10,-6,6,3,-4,-3,5,9,7,2,-10,-2,-10,7,-10,5,3,-10,-1,-4,-9,-7,2,-6,9,6,-1,-2,-9,-9,4,-8,3,7,-3,8,7,-6,3,-2,8,-4,4,-1,7,-1,-2,-9,9,1,-8,-1,6,5,-9,-4,5,-7,-7,2,-6,6,-2,-7,2,10,-8,-4,8,4,6,-4,9,10,8,8,2,6,-1,-4,10,1,-7,-10,4,-2,-5,1,-8,8,2,-3,-1,8,-1,-3,8,-7,-10,-10,5,7,8,2,1,-5,-7,7,7,-8,-10,9,8,1,-5,6,-2,-9,-3,10,4,-6,4,-9,-9,-1,-9,-6,-8,-6,-7,4,5,2,8,-3,7,-1,3,4,-6,-2,7,5,5,8,-4,-3,-8,9,7,6,3,5,-7,1,-5,-2]], dtype = "int64")#candidate|3726|(1, 1792)|const|int64
const_3727 = relay.const([True,False,False,False,False,True,True,True,False,False,False,False], dtype = "bool")#candidate|3727|(12,)|const|bool
call_3725 = relay.TupleGetItem(func_812_call(relay.reshape(const_3726.astype('int64'), [16, 7, 16]), relay.reshape(const_3727.astype('bool'), [12,]), ), 0)
call_3728 = relay.TupleGetItem(func_815_call(relay.reshape(const_3726.astype('int64'), [16, 7, 16]), relay.reshape(const_3727.astype('bool'), [12,]), ), 0)
func_3214_call = mod.get_global_var('func_3214')
func_3217_call = mutated_mod.get_global_var('func_3217')
var_3740 = relay.var("var_3740", dtype = "int32", shape = (600,))#candidate|3740|(600,)|var|int32
call_3739 = relay.TupleGetItem(func_3214_call(relay.reshape(var_3740.astype('int32'), [10, 15, 4])), 1)
call_3741 = relay.TupleGetItem(func_3217_call(relay.reshape(var_3740.astype('int32'), [10, 15, 4])), 1)
bop_3747 = relay.maximum(const_3726.astype('int8'), relay.reshape(call_3725.astype('int8'), relay.shape_of(const_3726))) # shape=(1, 1792)
bop_3750 = relay.maximum(const_3726.astype('int8'), relay.reshape(call_3728.astype('int8'), relay.shape_of(const_3726))) # shape=(1, 1792)
output = relay.Tuple([call_3719,const_3727,call_3739,var_3740,bop_3747,])
output2 = relay.Tuple([call_3720,const_3727,call_3741,var_3740,bop_3750,])
func_3753 = relay.Function([var_3740,], output)
mod['func_3753'] = func_3753
mod = relay.transform.InferType()(mod)
var_3754 = relay.var("var_3754", dtype = "int32", shape = (600,))#candidate|3754|(600,)|var|int32
output = func_3753(var_3754)
func_3755 = relay.Function([var_3754], output)
mutated_mod['func_3755'] = func_3755
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3642_call = mod.get_global_var('func_3642')
func_3643_call = mutated_mod.get_global_var('func_3643')
call_3802 = relay.TupleGetItem(func_3642_call(), 0)
call_3803 = relay.TupleGetItem(func_3643_call(), 0)
output = relay.Tuple([call_3802,])
output2 = relay.Tuple([call_3803,])
func_3809 = relay.Function([], output)
mod['func_3809'] = func_3809
mod = relay.transform.InferType()(mod)
output = func_3809()
func_3810 = relay.Function([], output)
mutated_mod['func_3810'] = func_3810
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3809_call = mod.get_global_var('func_3809')
func_3810_call = mutated_mod.get_global_var('func_3810')
call_3811 = relay.TupleGetItem(func_3809_call(), 0)
call_3812 = relay.TupleGetItem(func_3810_call(), 0)
output = relay.Tuple([call_3811,])
output2 = relay.Tuple([call_3812,])
func_3827 = relay.Function([], output)
mod['func_3827'] = func_3827
mod = relay.transform.InferType()(mod)
mutated_mod['func_3827'] = func_3827
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3827_call = mutated_mod.get_global_var('func_3827')
call_3828 = func_3827_call()
output = call_3828
func_3829 = relay.Function([], output)
mutated_mod['func_3829'] = func_3829
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3865 = relay.var("var_3865", dtype = "float64", shape = (15, 10, 1))#candidate|3865|(15, 10, 1)|var|float64
uop_3866 = relay.sin(var_3865.astype('float64')) # shape=(15, 10, 1)
uop_3869 = relay.atanh(var_3865.astype('float32')) # shape=(15, 10, 1)
uop_3898 = relay.rsqrt(var_3865.astype('float32')) # shape=(15, 10, 1)
bop_3900 = relay.add(uop_3898.astype('float64'), relay.reshape(uop_3866.astype('float64'), relay.shape_of(uop_3898))) # shape=(15, 10, 1)
output = relay.Tuple([uop_3869,bop_3900,])
output2 = relay.Tuple([uop_3869,bop_3900,])
func_3904 = relay.Function([var_3865,], output)
mod['func_3904'] = func_3904
mod = relay.transform.InferType()(mod)
mutated_mod['func_3904'] = func_3904
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3905 = relay.var("var_3905", dtype = "float64", shape = (15, 10, 1))#candidate|3905|(15, 10, 1)|var|float64
func_3904_call = mutated_mod.get_global_var('func_3904')
call_3906 = func_3904_call(var_3905)
output = call_3906
func_3907 = relay.Function([var_3905], output)
mutated_mod['func_3907'] = func_3907
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3809_call = mod.get_global_var('func_3809')
func_3810_call = mutated_mod.get_global_var('func_3810')
call_3918 = relay.TupleGetItem(func_3809_call(), 0)
call_3919 = relay.TupleGetItem(func_3810_call(), 0)
output = relay.Tuple([call_3918,])
output2 = relay.Tuple([call_3919,])
func_3922 = relay.Function([], output)
mod['func_3922'] = func_3922
mod = relay.transform.InferType()(mod)
output = func_3922()
func_3923 = relay.Function([], output)
mutated_mod['func_3923'] = func_3923
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3938 = relay.var("var_3938", dtype = "int64", shape = (13, 12, 4))#candidate|3938|(13, 12, 4)|var|int64
const_3939 = relay.const([[[10,-6,3,7],[-2,-7,1,8],[-8,-4,1,-5],[-5,-10,3,-10],[3,-1,10,6],[10,-8,-7,-9],[-7,-9,8,-5],[8,-1,-5,-4],[-7,-9,-3,-10],[-10,-4,-5,1],[7,-10,5,-7],[9,6,8,-6]],[[-4,-3,10,10],[2,-7,8,-6],[-8,-9,4,-8],[3,-10,-3,-8],[-3,-4,4,5],[7,-2,-7,-9],[7,-10,5,5],[-3,10,1,-2],[1,-7,7,1],[-3,-8,-3,7],[-4,-2,-8,-10],[-10,-6,-8,-5]],[[-4,4,-4,7],[9,-8,-2,-4],[-6,7,3,-3],[-8,6,-7,7],[-3,5,9,5],[-7,2,-1,-6],[-5,9,2,3],[-2,8,-9,-3],[7,2,-9,-3],[1,4,4,-9],[4,-6,-3,-6],[9,-4,-8,-1]],[[-4,10,9,8],[3,-3,5,-5],[-1,7,2,-9],[-7,9,10,2],[-4,-7,-10,-4],[8,-7,1,-2],[-4,6,-4,1],[8,9,-2,1],[-5,-1,-3,7],[2,4,7,6],[7,-9,9,-2],[-10,6,-4,-9]],[[7,-6,-5,-2],[5,10,4,-5],[-8,-1,6,5],[-4,9,-7,-9],[-8,-5,-5,10],[4,4,-4,10],[3,2,-7,-5],[-7,1,5,-10],[-4,-6,3,9],[-3,-7,1,-2],[1,6,-8,-10],[-7,1,-2,7]],[[-4,-5,10,-4],[8,-2,1,5],[-8,1,-4,-3],[4,5,2,2],[-6,5,-10,8],[10,-8,6,4],[-6,9,8,1],[5,7,-7,-5],[5,-8,9,-4],[-6,2,8,3],[1,-2,-6,-10],[-8,-10,8,-9]],[[-5,10,10,3],[-6,7,10,-8],[6,9,-4,4],[-8,8,-10,-8],[1,-9,4,9],[6,6,8,7],[3,-5,-7,-8],[3,-2,10,-10],[-10,3,2,3],[-10,3,2,-1],[8,-1,-4,1],[-2,2,4,4]],[[2,7,-1,-3],[-9,8,-8,6],[4,-2,-6,-6],[7,2,-10,5],[-6,-8,-5,8],[9,7,5,-5],[1,-7,-2,7],[1,-3,8,4],[2,-2,3,3],[6,-9,-3,9],[-4,3,9,9],[1,-10,-10,4]],[[-6,-1,4,3],[3,-2,10,2],[-8,-2,-7,5],[-3,-9,-1,6],[-7,8,-10,3],[7,-8,7,-3],[-7,3,5,3],[5,2,-3,3],[5,3,-6,-7],[-4,-10,-6,-7],[7,8,10,-2],[1,8,2,6]],[[-5,-3,7,-4],[6,1,8,-9],[-10,8,6,2],[4,3,-3,5],[8,-9,-7,-4],[-8,9,5,-10],[2,-2,8,8],[-5,-7,-10,8],[-8,2,9,-2],[-3,2,8,-2],[10,1,-7,7],[1,-2,-6,-10]],[[-9,-2,10,-5],[7,-10,1,-7],[5,10,-10,6],[3,-2,-10,3],[-5,-8,-1,8],[2,4,2,-6],[-3,9,-3,5],[-4,-5,9,2],[5,9,-2,-5],[-8,10,4,7],[2,1,2,1],[4,8,4,-9]],[[9,4,-8,-6],[9,6,-1,1],[8,1,9,-6],[10,6,4,-2],[5,4,6,-8],[7,-10,-7,-4],[-2,-7,-6,4],[6,9,-7,-5],[-8,6,1,1],[-9,8,2,3],[6,-5,-4,8],[10,2,-10,-2]],[[5,4,-1,4],[8,8,-4,5],[2,2,-10,-5],[-10,10,3,-10],[-9,4,3,-1],[-4,10,1,-7],[5,8,4,8],[2,5,1,4],[2,-1,10,6],[1,1,3,-5],[-1,-6,8,-8],[3,8,1,-3]]], dtype = "int64")#candidate|3939|(13, 12, 4)|const|int64
bop_3940 = relay.add(var_3938.astype('int64'), relay.reshape(const_3939.astype('int64'), relay.shape_of(var_3938))) # shape=(13, 12, 4)
var_3957 = relay.var("var_3957", dtype = "int64", shape = (13, 12, 4))#candidate|3957|(13, 12, 4)|var|int64
bop_3958 = relay.multiply(bop_3940.astype('uint64'), relay.reshape(var_3957.astype('uint64'), relay.shape_of(bop_3940))) # shape=(13, 12, 4)
func_3904_call = mod.get_global_var('func_3904')
func_3907_call = mutated_mod.get_global_var('func_3907')
var_3974 = relay.var("var_3974", dtype = "float64", shape = (150,))#candidate|3974|(150,)|var|float64
call_3973 = relay.TupleGetItem(func_3904_call(relay.reshape(var_3974.astype('float64'), [15, 10, 1])), 0)
call_3975 = relay.TupleGetItem(func_3907_call(relay.reshape(var_3974.astype('float64'), [15, 10, 1])), 0)
output = relay.Tuple([bop_3958,call_3973,var_3974,])
output2 = relay.Tuple([bop_3958,call_3975,var_3974,])
func_3986 = relay.Function([var_3938,var_3957,var_3974,], output)
mod['func_3986'] = func_3986
mod = relay.transform.InferType()(mod)
mutated_mod['func_3986'] = func_3986
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3986_call = mutated_mod.get_global_var('func_3986')
var_3988 = relay.var("var_3988", dtype = "int64", shape = (13, 12, 4))#candidate|3988|(13, 12, 4)|var|int64
var_3989 = relay.var("var_3989", dtype = "int64", shape = (13, 12, 4))#candidate|3989|(13, 12, 4)|var|int64
var_3990 = relay.var("var_3990", dtype = "float64", shape = (150,))#candidate|3990|(150,)|var|float64
call_3987 = func_3986_call(var_3988,var_3989,var_3990,)
output = call_3987
func_3991 = relay.Function([var_3988,var_3989,var_3990,], output)
mutated_mod['func_3991'] = func_3991
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3809_call = mod.get_global_var('func_3809')
func_3810_call = mutated_mod.get_global_var('func_3810')
call_4029 = relay.TupleGetItem(func_3809_call(), 0)
call_4030 = relay.TupleGetItem(func_3810_call(), 0)
output = call_4029
output2 = call_4030
func_4059 = relay.Function([], output)
mod['func_4059'] = func_4059
mod = relay.transform.InferType()(mod)
mutated_mod['func_4059'] = func_4059
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4059_call = mutated_mod.get_global_var('func_4059')
call_4060 = func_4059_call()
output = call_4060
func_4061 = relay.Function([], output)
mutated_mod['func_4061'] = func_4061
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3922_call = mod.get_global_var('func_3922')
func_3923_call = mutated_mod.get_global_var('func_3923')
call_4090 = relay.TupleGetItem(func_3922_call(), 0)
call_4091 = relay.TupleGetItem(func_3923_call(), 0)
output = call_4090
output2 = call_4091
func_4108 = relay.Function([], output)
mod['func_4108'] = func_4108
mod = relay.transform.InferType()(mod)
mutated_mod['func_4108'] = func_4108
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4108_call = mutated_mod.get_global_var('func_4108')
call_4109 = func_4108_call()
output = call_4109
func_4110 = relay.Function([], output)
mutated_mod['func_4110'] = func_4110
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4108_call = mod.get_global_var('func_4108')
func_4110_call = mutated_mod.get_global_var('func_4110')
call_4223 = func_4108_call()
call_4224 = func_4108_call()
output = call_4223
output2 = call_4224
func_4238 = relay.Function([], output)
mod['func_4238'] = func_4238
mod = relay.transform.InferType()(mod)
mutated_mod['func_4238'] = func_4238
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4238_call = mutated_mod.get_global_var('func_4238')
call_4239 = func_4238_call()
output = call_4239
func_4240 = relay.Function([], output)
mutated_mod['func_4240'] = func_4240
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4238_call = mod.get_global_var('func_4238')
func_4240_call = mutated_mod.get_global_var('func_4240')
call_4259 = func_4238_call()
call_4260 = func_4238_call()
func_1205_call = mod.get_global_var('func_1205')
func_1207_call = mutated_mod.get_global_var('func_1207')
var_4274 = relay.var("var_4274", dtype = "float64", shape = (84,))#candidate|4274|(84,)|var|float64
call_4273 = func_1205_call(relay.reshape(var_4274.astype('float64'), [2, 3, 14]))
call_4275 = func_1205_call(relay.reshape(var_4274.astype('float64'), [2, 3, 14]))
output = relay.Tuple([call_4259,call_4273,var_4274,])
output2 = relay.Tuple([call_4260,call_4275,var_4274,])
func_4279 = relay.Function([var_4274,], output)
mod['func_4279'] = func_4279
mod = relay.transform.InferType()(mod)
var_4280 = relay.var("var_4280", dtype = "float64", shape = (84,))#candidate|4280|(84,)|var|float64
output = func_4279(var_4280)
func_4281 = relay.Function([var_4280], output)
mutated_mod['func_4281'] = func_4281
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4059_call = mod.get_global_var('func_4059')
func_4061_call = mutated_mod.get_global_var('func_4061')
call_4286 = func_4059_call()
call_4287 = func_4059_call()
func_607_call = mod.get_global_var('func_607')
func_611_call = mutated_mod.get_global_var('func_611')
const_4291 = relay.const([False,False,True,False,True,True,True,True,False,False,False,True], dtype = "bool")#candidate|4291|(12,)|const|bool
var_4292 = relay.var("var_4292", dtype = "uint32", shape = (280, 2))#candidate|4292|(280, 2)|var|uint32
call_4290 = relay.TupleGetItem(func_607_call(relay.reshape(const_4291.astype('bool'), [6, 2, 1]), relay.reshape(var_4292.astype('uint32'), [560,]), ), 1)
call_4293 = relay.TupleGetItem(func_611_call(relay.reshape(const_4291.astype('bool'), [6, 2, 1]), relay.reshape(var_4292.astype('uint32'), [560,]), ), 1)
output = relay.Tuple([call_4286,call_4290,const_4291,var_4292,])
output2 = relay.Tuple([call_4287,call_4293,const_4291,var_4292,])
func_4308 = relay.Function([var_4292,], output)
mod['func_4308'] = func_4308
mod = relay.transform.InferType()(mod)
var_4309 = relay.var("var_4309", dtype = "uint32", shape = (280, 2))#candidate|4309|(280, 2)|var|uint32
output = func_4308(var_4309)
func_4310 = relay.Function([var_4309], output)
mutated_mod['func_4310'] = func_4310
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4059_call = mod.get_global_var('func_4059')
func_4061_call = mutated_mod.get_global_var('func_4061')
call_4312 = func_4059_call()
call_4313 = func_4059_call()
func_1977_call = mod.get_global_var('func_1977')
func_1980_call = mutated_mod.get_global_var('func_1980')
var_4334 = relay.var("var_4334", dtype = "uint8", shape = (1, 2704))#candidate|4334|(1, 2704)|var|uint8
call_4333 = relay.TupleGetItem(func_1977_call(relay.reshape(var_4334.astype('uint8'), [13, 13, 16])), 0)
call_4335 = relay.TupleGetItem(func_1980_call(relay.reshape(var_4334.astype('uint8'), [13, 13, 16])), 0)
func_2910_call = mod.get_global_var('func_2910')
func_2913_call = mutated_mod.get_global_var('func_2913')
var_4358 = relay.var("var_4358", dtype = "float32", shape = (4, 28))#candidate|4358|(4, 28)|var|float32
call_4357 = func_2910_call(relay.reshape(var_4358.astype('float32'), [7, 8, 2]))
call_4359 = func_2910_call(relay.reshape(var_4358.astype('float32'), [7, 8, 2]))
func_1023_call = mod.get_global_var('func_1023')
func_1026_call = mutated_mod.get_global_var('func_1026')
const_4362 = relay.const([-4,-10,-6,2,5,-7,-8,-1,8,-7,7,-5,5,-7,10,7,8,-8,6,-8,-10,3,4,9,3,-2,-3,9,4,3,10,8,7,-2,-10,3,7,-9,10,-3,-4,-5,-4,5,2,2,7,-8,9,-7,-10,8,6,8,-5,-9,10,8,-2,-1,-10,-6,4,1,-4,2,-9,-3,10,-1,6,6,7,7,-6,2,3,4,2,3,-6,-3,-7,-7,10,2,9,-10,-1,-4,9,-4,5,-2,-5,-6,9,-5,-6,1,-2,9,-4,-8,10,-3,-1,1,-7,5,-7,-3,8,3,2,-9,-9,-6,1,-8,-7,8,-10,-3,10,-8,-9,-3,1,-3,2,-9,-4,5,-8,-4,6,2,1,-4,3,9,-5,3,10,10,9,4,4,-7,-2,9,5,5,-7,6,-1,4,-9,3,-2,-1,4,-4,-5,-3,4,-7,3,4,1,10,6,1,8,5,8,-10,-3,3,5,-7,7,-7,-7,10,10,-3,1,-2,-7,10,-6,8,-3,9,8,-7,1,-5,5,-8,5,-3,-3,-7,3,6,6,-1,8,8,-8,-10,1,9,1,2,9,4,10,4,7,-3,7,-3,-3,-8,-6,-10,-6], dtype = "uint64")#candidate|4362|(231,)|const|uint64
call_4361 = relay.TupleGetItem(func_1023_call(relay.reshape(const_4362.astype('uint64'), [7, 11, 3])), 2)
call_4363 = relay.TupleGetItem(func_1026_call(relay.reshape(const_4362.astype('uint64'), [7, 11, 3])), 2)
uop_4368 = relay.erf(const_4362.astype('float64')) # shape=(231,)
uop_4385 = relay.log10(uop_4368.astype('float64')) # shape=(231,)
output = relay.Tuple([call_4312,call_4333,var_4334,call_4357,var_4358,call_4361,uop_4385,])
output2 = relay.Tuple([call_4313,call_4335,var_4334,call_4359,var_4358,call_4363,uop_4385,])
func_4388 = relay.Function([var_4334,var_4358,], output)
mod['func_4388'] = func_4388
mod = relay.transform.InferType()(mod)
mutated_mod['func_4388'] = func_4388
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4388_call = mutated_mod.get_global_var('func_4388')
var_4390 = relay.var("var_4390", dtype = "uint8", shape = (1, 2704))#candidate|4390|(1, 2704)|var|uint8
var_4391 = relay.var("var_4391", dtype = "float32", shape = (4, 28))#candidate|4391|(4, 28)|var|float32
call_4389 = func_4388_call(var_4390,var_4391,)
output = call_4389
func_4392 = relay.Function([var_4390,var_4391,], output)
mutated_mod['func_4392'] = func_4392
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4238_call = mod.get_global_var('func_4238')
func_4240_call = mutated_mod.get_global_var('func_4240')
call_4452 = func_4238_call()
call_4453 = func_4238_call()
func_2329_call = mod.get_global_var('func_2329')
func_2335_call = mutated_mod.get_global_var('func_2335')
const_4463 = relay.const([10,-10,6,5,7,-5,-6,-10,5,-5,-3,9,-7,-5,7,-2,7,-3,-3,7,4,8,-10,2,-2,6,-10,-5,10,-1,1,-3,-7,-3,5,-10,-3,10,9,-9,-1,-6,10,9,5,-8,-5,-5,5,1,-8,-10,1,6,-6,-9,-2,9,10,5,-9,-10,-1,-7,4,6,-10,7,-10,1,10,10,-7,-7,8,10,2,-2,-8,-9,10,6,-4,3,-6,8,4,-9,1,-10,5,-6,4,9,-8,4,-6,2,-5,-3,-9,6,-3,8,2,-2,-10,5,-6,-5,3,-6,2,-8,-3,8,4,-9,1,-2,5,-2,-2,-8,9,5,-3,-10,1,3,-1,-7,-5,3,-6,-2,8,-8,9,1,9,2,8,-8,2,-2,10,-7,8,4,-4,6,8,-4,-10,-7,-10,-3,-10,5,10,-2,-7,-7,8,8,8,6,8,5,3,-8,-10,1,-2,2,4,-2,3,-5,-5,-5,-6,10,-8,-3,6,6,-2], dtype = "int8")#candidate|4463|(189,)|const|int8
const_4464 = relay.const([7.107964,-5.600312,-7.299288,0.260879,5.704261,9.503616,0.137826,1.151839,6.994039,9.637852,8.611210,-5.516989,0.752032,-6.857938,-1.400786,-8.513830,-1.035835,-2.775653,5.720013,6.541467,2.687237,8.262777,4.141100,9.191487,-8.996299,6.512499,-8.015617,2.105277,-3.059286,1.962594,-6.333772,-9.166966,-4.423670,8.946164,7.048393,-5.273149,-9.141181,6.583339,1.071315,-6.989699,6.694965,9.225339,-9.870271,6.016729,2.983625,7.113486,-2.681027,-9.520370,-2.515637,3.483606,-9.918027,-7.159210,0.568600,-2.936797,-7.483387,-1.022762,0.699141,-0.254965,-0.308285,-3.479053,-0.276475,6.412418,-4.195794,0.333544,-6.910972,-7.483363,-2.973355,9.036340,-9.078543,-0.208124,-4.195395,4.794746,4.940892,5.280780,6.066955,0.793845,0.658219,8.282095,-1.995259,5.754821,0.686778,1.799561,-7.763440,2.632439,9.489253,-3.629028,-8.641006,8.326908,5.121992,9.451375,-4.161572,-2.092536,-6.304121,0.417653,-6.192888,7.382309,-7.235772,6.312424,1.662274,-1.985543,7.060946,-4.381477,-1.848885,9.856277,5.023985,-6.306749,8.651487,2.327956,-8.427299,-7.703161,7.853627,-8.354827,-1.590523,4.654026,-4.810065,-4.927383,-4.318344,8.801654,-2.741831,-0.934493,-3.788455,-0.227869,6.738219,7.541547,-7.370874,-3.960221,0.389640,-2.678013,-0.617099,5.451425,1.957649,-5.209411,-3.208394,-4.613228,-1.559013,-2.477956,1.425345,-1.169851,7.539682,3.189007,0.726968,0.335249,-7.423346,4.062572,4.920203,-3.772842,-5.850197,-4.019705,-1.788217,-3.423091,7.375067,6.211856,9.373924,0.762247,4.044840,-3.523037,-3.728092,1.682416,5.844657,-3.230288,5.029304,7.924887,1.119711,3.901949,-7.005084,5.268615,-1.156454,9.980331,-3.471405,-2.094153,9.940475,0.960359,2.547609,-3.024004,7.442062,0.318422,3.574159,-7.587367,2.044716,3.115803,2.291000,4.989938,6.878727,6.878671,-1.187454,-3.520724,0.667913,7.273201,-0.728488,6.269771,-3.354883,2.657913,-7.089209,2.244594,1.230701,8.309135,2.651143,-3.871736,1.454480,-0.244174,-2.288579,0.948390,-7.093598,-5.261666,3.939053,-0.435232,-8.886694,1.927123,-1.019648,-8.061339,6.665115,-4.812935,9.479533,-7.685858,5.729471,-1.608270,1.123099,8.554152,-2.562039,-1.414504,3.486604,-2.525239,-1.170333,-2.286811,-6.206534,-3.739224,6.382145,-8.135533,-7.111839,6.178815,6.840799,8.355728,-9.500044,0.726199,-4.278191,-5.481918,-6.213385,5.827308,-3.511279,8.217290,1.848973,6.915551,4.230542,6.607508,-1.467306,9.566151,-9.190613,-3.505576,6.465426,9.665546,3.256090,8.780519,-0.401220,4.678838,8.104615,7.392405,-7.504315,0.943303,-1.160657,5.856801,3.555608,7.670907,4.173579,-4.752910,8.691696,-1.224657,4.993570,-7.264459,9.487777,1.599160,8.998734,1.664512,2.134479,5.833082,2.497639,-1.416773,5.388512,-3.965038,7.785735,4.788931,-7.230146,8.233544,5.919863,-2.106444,4.582940,9.019890,-9.728139,7.013113,3.142785,-7.665099,2.742658,-6.873962,-8.686846,-0.949481,7.770201,-3.362884,9.911324,-3.527313,4.986272,1.925411,-9.489600,3.869095,4.917601,-9.791618,9.729807,1.745163,2.213383,2.456004,-9.966088,9.515058,3.039013,-6.625099,2.458094,-0.259571,1.156410,-6.415988,-9.897087,-1.792873,-3.291223,7.492074,9.272870,-7.251715,-5.120824,-0.246314,2.761384,-3.879214,8.282785,-8.536285,0.840992,-7.258866,-4.930902,-6.031228,-0.411904,8.045251,6.452851,8.436333,7.586536,9.647180,2.838104,6.907727,6.996478,-1.062653,-1.190762,-5.953903,3.620413,-0.869614,2.411334,-9.078838,8.966109,-1.573755,-0.566056,-0.012123,2.698096,0.366619,0.161570,-3.992330,9.510031,-6.559819,0.230745,6.021744,7.460572,-4.020318,1.677414,-6.928558,-4.034632,6.790751,-3.939135,7.116868,-5.660672,5.813468,7.140517,-5.399551,-8.722535,-7.053766,3.041156,-8.506233,6.899023,1.168439,0.973755,7.508994,-7.073434,5.456480,-6.522584,6.186095,1.842658,1.376265,-0.906296,2.982663,-8.566196,-6.751051,-5.684255,-7.421716,7.278252,-1.848716,4.944567,3.168402,-5.678304,7.208552,6.560128,2.723194,8.797148,4.694545,7.907067,-9.035856,-1.741624,7.505020,7.548216,-3.856702,-8.621448,2.985451,-6.353609,5.524766,0.063273,-3.192035,0.832291,-2.072811,-4.940691,-9.624558,-8.119432,1.315737,8.827549,6.707849,-7.132935,-3.973456,-4.392808,-0.743842,-1.516276,-1.752542,-7.868359,-4.457512,-6.112885,-2.052844,-8.240654,-7.054403,1.025734,2.362792,6.825094,6.305442,-2.825206,-2.767643,-2.763270,3.489076,-6.159340,-7.639980,-6.116832,7.849048,8.489706,3.192259,-8.339699,6.258095,1.147880,6.039733,0.717846,-5.193763,-1.459992,9.321235,-4.973901,0.330981,-6.099473,1.111798,-5.351270,4.695968,0.697966,4.055912,6.705967,2.685067,6.600232,6.298801,-5.013597,-2.040679,-1.964993,2.965720,-7.435468,5.150155,-7.444527,-9.976031,8.884823,8.757862,-4.284120,5.546341,7.836060,8.228428,3.602782,1.994884,-2.393072,-8.374195,6.467690,0.804626,-6.826321,-6.558690,-6.408112,4.990322,8.638096,-9.759466,8.080185,0.145994,-8.184586,1.545504,2.122299,3.749587,-3.052849,-9.767599,8.151747,2.513688,-2.588602,8.541214,-6.417052,2.347048,3.905684,-0.337099,9.903665,9.025476,-3.504664,1.844763,4.459065,1.171017,-7.380385,-5.770508,-0.004741,7.939644,8.801054,2.747474,2.334198,0.682798,-7.561627,0.649803,8.043908,6.186263,2.425753,5.914781,-8.460810,-8.000756,-6.794233,-7.856971,-1.839601,-9.362616,-4.219131,-1.297290,-6.466784,-9.143157,7.415363,-5.878118,-2.027673,-6.511653,-0.067772,7.274983,-4.283182,3.671461,-4.594336,8.099146,9.046512,-4.378912,1.938683,2.000062,4.014775,-4.504867,6.707829,3.861476,4.730394,9.780437,-7.921028,-1.163398,-0.856170,3.190654,5.326861,2.938429,-1.962382,8.538589,-0.662149,9.476143,-3.319515,-7.793481,-6.486324,-0.872241,6.252864,0.638407,-2.496739,1.829899,8.015647,3.294430,8.068203,9.445246,-3.593547,-3.962390,7.246427,-7.240777,6.159368,0.133960,8.709474,3.334974,0.805514,-0.210215,-3.855089,-3.060199,-4.710115,9.368928,6.096953,-2.956270,5.074874,-2.118688,-0.790264,-0.578499,-2.580037,-0.105129,2.046674,-4.248634,-8.279455,-7.341361,-4.472690,8.460654,-9.715270,1.822525,2.413788,-0.409411,-8.366282,-3.947339,8.415690,-0.252073,-2.431519,7.330804,8.896844,8.104558,-4.806608,-4.447295,-4.316076,-2.006076,-5.168190,-3.408600,8.911367,-1.545238,-7.480333,-9.682667,-0.788511,2.730491,2.301187,-0.024550,-9.379060,0.495543,-4.435588,-3.808352,5.619795,9.702150,-1.308358,7.673746,-3.401567,3.140163,-1.713255,3.623258,-1.099758,-6.586596,1.340546,-2.118039,-7.200679,1.072702,-8.657539,9.735972,-3.262216,3.909833,4.107441,-4.272072,9.685094,-0.050829,2.382146,-4.606422,-8.594181,-7.494606,1.047050,0.349851,-4.877197,-7.972563,-1.758206,-1.488973,2.239933,9.244239,-7.024379,-7.378772,3.007452,-8.811051,-0.964686,8.922179,4.207577,4.226723,-7.393187,-1.010471,4.505202,2.194247,-2.809119,-2.831257,-2.358197,-4.723349,7.951120,-9.383445,9.540251,8.233962,1.346272,-7.598110,-5.834967,7.762623,0.446941,4.107154,7.604996,-0.350771,-7.158636,8.757907,4.004509,-9.271541,-2.667039,4.638176,2.744353,-4.251802,9.537604,3.182965,-6.163166,0.422020,-9.993489,-7.769408,2.101011,0.308527,7.091084,-6.492368,2.264905,4.437211,5.945137,0.060605,2.272804,4.829427,1.069431,1.721925,-7.465983,7.013534,7.788611,-3.651744,-1.422121,3.428406,-6.451516,-8.075309,-4.406233,4.644144,6.067766,-5.143343,-2.513717,1.106440,-1.080753,9.638103,9.541495,7.496776,-3.914494,-9.357380,7.995037,-5.542319,7.548847,6.483543,-7.225290,-8.164467,-5.222130,7.681141,-1.301876,-5.284946,8.728104,5.063099,-4.872749,3.168681,-7.177940,2.995873,6.600001,0.241597,2.658928,-8.774322,-5.975418,7.288669,0.916243,1.393814,7.594631,-7.235114,-6.309507,-3.035218,-8.546114,9.519256,7.472077,9.812052,1.201142,6.886926,1.570066,-8.089794,-9.021066,-3.520147,-6.469386,-9.749323,5.632156,-3.351675,-5.682172,-8.501747,7.007795,-2.165841,0.042086,0.181235,-0.660350,2.536080,8.914247,2.620321,8.058820,1.123115,-4.846636,6.158974,5.642662,1.969356,-2.065230,-7.075747,9.581455,-0.735438,-8.385703,3.720343,6.067590,7.603864,0.901351,-8.502966,-8.993143,-2.687088,1.415673,2.780687,-7.060834,4.056567,-8.696266,-2.075115,-2.970685,-7.671834,-2.633448,1.712128,-8.707458,-6.692214,-7.339795,-8.549987,3.667004,4.492846,5.270286,0.917392,1.083094,-6.068405,-2.757575,3.195309,-0.339797,-3.139553,-9.103260,-6.410783,-8.134417,-7.769576,1.711860,8.053398,7.707929,-8.394414,1.799770,-8.279472,-9.378040,4.771342,2.409452,8.395857,-4.408969,6.970266,3.641033,-6.501422,-6.059101,-8.524565,0.318774,-1.336249,-2.648310,7.584714,-7.965598,-5.928514,2.792335,-8.887809,8.427859,-9.240114,3.064796,-3.296128,2.265723,-6.809478,0.216697,1.069112,-2.622387,5.421110,-5.646439,0.241743,0.582925,8.129140,7.389943,1.210291,3.743672,-9.721796,1.377713,-1.804634,7.252690,4.426317,5.261867,-5.370026,-9.266185,8.610426,-0.966775,-8.599453,-7.035310,-2.096438,3.408279,-6.226592,1.465149,1.946707,0.623180,4.687143,-1.849041,8.391047,-3.719934,2.401456,-7.886736,8.491951,3.476553,-5.852625,-0.698821,0.530798,-0.777288,-6.502828,8.759617,6.829378,4.757641,6.739769,0.705310,-1.357691,-6.997941,-1.493217,-4.073141,-4.168046,7.816239,8.521605,7.077113,5.224622,9.004088,-1.189435,0.802565,7.215704,-7.515250,-3.896974,-2.796246,4.982884,6.154105,9.548238,-5.557150,8.061144,-6.950231,0.319073,-9.950646,2.670643,-1.750202,-3.611358,2.058608,3.157980,-0.687142,2.964826,-8.066631,-7.924363,3.902932,7.076862,4.466879,7.921155,9.256501,7.936855,-8.407274,0.931648,-5.930951,-0.767638,-5.952677,-6.209373,-0.776695,0.865356,-7.696191,-1.260547,3.255829,3.120139,-8.166060,-3.524058,9.120451,1.203020,-7.252015,1.320464,-8.905197,2.323280,4.636388,-2.699911,2.189715,-0.723396,2.379703,1.397648,-3.804846,0.718074,-6.724179,-4.933114,2.631942,7.010092,8.089610,8.382262,-5.811754,-6.863843,-2.655525,2.284724,-8.729013,1.442954,-4.884475,-5.060499,-4.866535,-0.613493,8.950755,-1.273470,-8.619285,-4.631637,-8.682115,-4.765240,-9.129625,-6.730386,3.849032,2.901308,6.617764,1.902821,6.118300,-1.738071,3.599487,-1.200312,-7.223953,5.447020,-8.358937,-5.747801,0.153266,-5.649324,7.031165,-8.917118,-7.871887,-9.346506,2.171802,-2.442792,3.143043,-0.120860,3.525419,2.949368,4.130908,-9.051703,-7.465592,4.621229,1.899194,-6.486811,-5.496825,3.515314,-2.581408,1.632177,6.248399,-3.601394,-2.871507,7.359503,-7.308034,3.722308,-1.226660,0.324019,-9.896473,-4.687103,-3.819356,-3.669320,-8.295256,-8.730759,4.488029,-5.811331,6.698577,7.293218,8.664975,6.764712,4.546977,2.376087,-8.588185,0.617281,4.781372,0.224939,-6.794667,6.042560,0.391433,4.032224,0.725341,-0.132005,-8.621605,-3.834886,-8.635315,8.580828,4.590821,2.806494,-4.774542,-1.483204,2.007271,4.825339,-6.991155,-7.108251,-2.215254,-9.302306,1.321456,-1.514470,4.378121,8.155656,-5.975080,4.139598,3.708232,-5.813229,8.417178,-2.002070,-6.873552,-7.488382,-1.017946,-5.179700,-0.878332,-4.981449,8.032523,-5.145294,0.164912,9.933044,-1.739599,1.211486,8.885803,3.364832,1.461871,1.480347,-1.651024,-6.971899,-1.976043,6.793171,4.062160,-0.869791,0.583713,2.605171,-7.617023,-4.329116,-4.856954,0.374034,5.901755,-4.854299,-1.490497,-1.568860,-3.928922,8.851574,-4.418799,4.920163,-7.472209,-2.976936,-8.918056,-0.063874,-1.152600,-0.873367,9.787641,5.689323,-6.604155,0.508905,9.586539,5.595853,-4.682872,5.392460,-4.164402,-1.233123,-0.442541,-2.496807,4.822068,-1.946443,9.780664,-2.165135,-8.373306,-2.922402,5.259960,0.371479,4.833898,-5.382089,2.619483,-0.359872,7.915179,-2.961546,-5.346272,-1.413974,2.634688,4.600465,3.595642,9.269673,9.669500,7.860713,7.069495,-8.672926,7.773854,-6.324289,-1.156731,-7.161311,-3.160846,5.386652,3.056263,-6.209830,-1.918754,-2.674416,5.431087,5.469236,5.218537,0.724591,6.720586,6.021873,9.197473,7.053738,8.379762,0.043114,-1.920306,-8.617357,-7.609085,2.267923,-5.681381,2.128343,2.355634,1.430017,3.659234,-2.048512,-4.071399,8.801465,2.602757,3.337654,3.281150,-2.998655,3.279778,4.650234,9.872389,7.938831,-9.178585,3.459349,6.443275,-7.863377,-0.833055,-8.015953,9.357766,-7.361457,-8.748888,5.068698,-0.706185,-3.810240,-6.037986,5.461560,-0.751126,9.816300,2.801866,-1.590510,9.660372,6.516722,7.896626,-2.339918,-3.980797,-4.695404,-5.744643,-8.753704,6.020941,1.653765,-8.130187,-6.547168,5.016175,-6.587091,-1.816650,8.398587,2.000337,7.321052,-2.077820,9.405121,-0.891870,-5.627045,6.062513,5.392042,7.205711,-7.167893,-2.225022,-0.583784,4.962124,-3.321411,2.346022,8.068770,3.666197,-8.272235,5.971259,-6.982675,2.425282,-9.025354,1.357062,7.031052,-8.660770,-9.713878,-0.347521,-8.344212,9.889342,-1.241427,9.359058,-6.303950,-9.013872,-9.372550,-6.388400,-1.469936,2.243298,1.587874,-9.573839,9.681685,-8.371449,3.546406,-8.632448,-9.779113,6.580149,3.549988,5.032437,7.918017,-0.500607,5.920293,-2.904342,-2.643134,-6.459036,-8.472357,-7.339022,-3.226002,0.754820,-1.519958,3.080068,-2.042252,8.092524,4.870851,0.473068,-1.847931,0.158481,-3.761050,8.206330,2.621831,-5.221260,2.126643,-2.761425,-3.822998,5.101380,8.313401,6.259064,0.539765,5.288664,8.128226,9.736959,-7.463300,6.286867,-7.445567,7.360844,8.883491,0.634298,5.547674,-0.140530,-2.376954,-5.523251,-3.947424,7.185601,-1.909788,7.499603,2.493065,7.820644,0.002092,-0.575610,-6.327958,4.156829,-0.938936,-6.105165,-2.977803,3.793825,-3.574156,8.362984,6.673441,8.494604,0.444022,-6.878578,7.326777,6.332642,-3.115806,6.940133,7.114553,-7.205151,8.931870,2.974365,1.741321,-5.599011,-2.889781,4.114294,-4.403506,4.539817,1.061502,-1.696973,-1.458922,8.746614,-2.707214,2.861888,5.733236,4.427304,-2.643063,9.536978,3.619351,4.274884,5.343574,8.013200,0.470094,8.822882,-7.093992,-2.984332,9.389731,-2.817588,-1.113171,-5.223847,9.063220,-0.123893,-0.781806,-3.200521,-6.659234,-5.183771,-0.284507,4.769886,-3.420936,-7.501477,8.786452,3.277200,-3.315447,-1.258522,2.773344,-8.428487,-3.781533,-7.988483,-5.417406,-5.156515,9.501542,-5.237477,-2.682734,2.538074,1.017612,-5.968571,-8.350838,0.813980,2.242682,5.384689,-6.026654,9.935647,9.005057,-8.414781,-0.430550,-5.273710,9.661040,7.763373,-6.943983,-7.871515,-9.472723,-0.463022,5.382267,8.018473,3.187553,7.869175,1.277346,-9.600048,6.761435,-3.413655,5.803741,4.513672,-0.258496,6.889009,4.115073,-6.207023,-5.678182,1.533232,-3.515576,-7.328602,4.123461,-0.585738,-7.763711,5.883269,0.822294,-5.447250,-3.969340,6.604625,-8.367267,-8.961089,-5.449471,-5.802527,2.054973,-4.459251,-0.295030,-7.330598,2.423173,-8.843927,8.718119,9.680012,-5.185416,-6.711069,4.662758,5.508371,-2.103966,8.388033,-8.821361,0.018053,3.751153,8.887367,-3.925195,-4.500430,-9.125528,3.095576,-4.953308,-7.185084,-3.657069,-5.573949,-3.841378,-1.796728,6.344792,-4.574284,7.689542,6.669427,3.241692,-5.468229,-7.534541,0.344154,-1.965005,8.396763,1.492955,5.577523,-5.198054,5.476189,4.504052,4.651407,-9.638960,-6.914986,4.174251,-8.739192,-7.219986,-8.807252,1.004958,-6.962772,-3.831930,4.234981,0.246254,-3.041677,-3.634249,0.633977,4.292132,-5.547900,-7.342790,1.056503,-8.531238,-9.157335,-0.803034,-7.914163,4.343287,3.339615,-1.141416,2.758788,1.747310,7.377461,-0.433610,3.353753,8.634490,1.564817,-7.764595,6.071393,-2.309259,-8.184003,-1.853953,6.733837,4.098011,4.512231,1.160490,0.050683,-2.765901,-3.404102,3.154533,-6.593261,9.296443,-4.405002,-5.154804,-3.193519,-1.670325,-1.381637,1.761534,-3.397221,-6.390133,-6.079565,-1.144587,2.812500,-2.593943,1.414826,4.676616,-4.451714,7.928777,5.161123,-0.992022,2.646660,-1.193410,1.378975,8.951874,-0.361498,-8.784765,4.857661,-4.715470,6.921597,-2.895869,6.922223,5.490789,-5.928676,-4.984969,-0.581192,5.759028,0.318954,4.672958,-8.636863,-1.625667,9.587639,0.519264,-7.015626,3.323825,1.578896,-1.466359,3.231131,-3.102749,4.937577,6.203812,-2.466491,7.460509,-9.523450,-8.971725,5.902505,7.196560,9.932524,7.774234,1.483462,-4.434207,-2.249973,9.139755,-8.912254,4.396935,-1.938682,4.409795,6.863768,4.999074,-5.519341,-0.810461,-5.011449,-1.100097,3.400494,4.886860,-0.385005,9.017530,7.005495,-1.435289,-5.827373,4.288887,7.282532,8.957972,5.137257,-3.020977,4.595327,2.560682,0.842882,0.908777,4.455779,8.910854,-1.588702,-4.390058,2.473796,1.075347,-1.927190,-5.865965,-7.567840,-6.539283,-5.724664,0.284349,-2.213445,-3.609393,-2.702193,-3.517502,-8.739775,1.704306,-6.241105,-6.786119,-5.495700,2.190119,-3.657444,-3.832424,-9.355049,-5.950609,-6.092572,-4.161007,-4.595128,-8.425772,-5.908822,-2.487090,-0.524140,-0.892902,2.542700,-0.667989,-2.987081,-5.781326,2.853824,6.144205,-8.832382,8.068864,9.083710,9.248211,-2.020938,-0.479817,-8.319733,4.178767,-9.114346,4.718859,1.360511,-3.404179,3.966651,-1.485501,4.906247,-8.222161,-6.496237,-4.640914,0.237527,4.620591,0.574641,6.505456,5.960215,-3.788221,-9.616019,0.840787,1.738072,0.254510,4.656350,-2.649558,-9.102837,-1.056178,-8.884901,-4.692087,-3.165935,1.896844,-5.609754,7.354969,5.676355,2.639835,3.621352,8.889948,-6.600892,9.881180,8.330185,9.349191,9.264716,-9.612517,-7.317208,6.837367,-6.672693,0.785407,9.443091,-0.607219,-8.225906,-5.297796,3.172021,4.367705,9.950907,0.635588,-7.774334,-5.219436,-2.899674,2.568545,1.320017,5.506782,5.303027,-5.897446,9.546381,7.179134,7.491784,2.923457,-9.553844,-1.490262,1.578436,-1.586204,-3.113986,5.948079,9.466841,-2.365313,-8.947995,-1.205409,-2.061853,-4.333433,-6.055140,5.364436,-9.554735,-9.728398,4.889143,-4.005997,-7.518520,-2.535121,1.106220,9.506401,-0.861600,8.803038,5.264144,-8.365396,5.169022,5.062474,3.996701,8.497001,1.876336,-5.627606,-1.626301,9.563306,1.645825,-9.450991,-8.595485,1.277758,3.964105,3.459878,-3.833941,-9.704485,-3.343029,9.615671,-0.636197,4.106335,-3.922430,9.180167,-7.587306,8.683184,-1.662680,-1.558868,7.639849,-2.623155,1.329102,3.519655,8.873235,0.576336,8.239002,6.401860,9.185097,8.279363,-9.857469,-1.959191,-2.451836,-1.452606,0.949674,5.764436,-3.579870,4.140104,7.775011,-6.051777,-8.400205,-6.454629,-9.145612,-6.389950,5.882241,-2.704240,-9.401203,-7.000819,-1.878558,4.850321,-9.775769,8.418004,-6.946676,-6.453510,0.905826,2.017264,-3.501171,-3.658132,3.765135,-5.927112,-4.661563,6.182829,3.476002,9.825228,-6.254679,-2.422633,1.005633,-6.709701,-3.834560,8.263206,4.821041,-7.278604,0.720140,-5.183929,9.012089,4.651089,3.671796,-1.424083,-5.772026,6.241785,-9.200211,6.562669,0.019581,-3.763216,-0.020825,3.225009,-9.138836,6.151403,-1.638521,-0.607104,-5.493647,-0.324593,-3.043915,1.336622,-5.418997,-2.170791,-9.128999,8.490278,6.163191,1.016567,9.269601,4.141622,-7.885116,9.456088,-0.722121,-2.647370,1.533184,7.102891,0.807838,3.418248,0.033791,3.376378,4.108410,3.926673,-0.456376,3.030592,7.480997,0.656983,1.817870,7.653979,-4.397477,0.534523,-0.039977,-7.469309,3.674763,7.154711,2.727860,-3.882491,0.276293,1.887946,-1.442131,-8.259809,7.821152,-3.549004,-3.634826,-7.802850,1.857272,3.115646,-4.342650,-3.398010,9.204789,-3.590834,-8.659830,4.957059,-8.695997,7.829543,9.046202,5.151749,0.194268,-5.805153,9.068786,-4.150712,-7.797094,-9.744731,0.854754,-5.339455,-0.981108,1.652290,9.163539,3.302136,8.105825,-1.925564,-2.340745,4.827667,2.828819,4.326030,9.186897,-7.046953,3.410587,-4.200382,4.424993,5.465753,-9.641826,-0.061673,-9.728706,9.993986,-2.157485,-8.915567,7.417316,-0.290099,8.202789,1.271611,3.521008,-8.509771,-4.047995,-5.701340,7.043969,-7.801543,-2.487376,2.229219,-8.142980,4.385924,3.435135,9.227995,8.153070,5.939642,6.320249,4.638839,-6.902882,-9.848899,3.673298,-7.628340,-1.970513,-6.655156,8.543440,8.198924,-5.142135,-0.638090,0.239349,8.637646,6.387715,7.125926,2.549602,-0.947418,1.237797,3.018590,1.497095,9.127190,-7.622369,-8.586438,-8.430827,6.879274], dtype = "float32")#candidate|4464|(2016,)|const|float32
var_4465 = relay.var("var_4465", dtype = "uint32", shape = (560,))#candidate|4465|(560,)|var|uint32
call_4462 = relay.TupleGetItem(func_2329_call(relay.reshape(const_4463.astype('int8'), [9, 3, 7]), relay.reshape(const_4463.astype('int8'), [9, 3, 7]), relay.reshape(const_4464.astype('float32'), [2016,]), relay.reshape(var_4465.astype('uint32'), [560,]), ), 0)
call_4466 = relay.TupleGetItem(func_2335_call(relay.reshape(const_4463.astype('int8'), [9, 3, 7]), relay.reshape(const_4463.astype('int8'), [9, 3, 7]), relay.reshape(const_4464.astype('float32'), [2016,]), relay.reshape(var_4465.astype('uint32'), [560,]), ), 0)
output = relay.Tuple([call_4452,call_4462,const_4463,const_4464,var_4465,])
output2 = relay.Tuple([call_4453,call_4466,const_4463,const_4464,var_4465,])
func_4469 = relay.Function([var_4465,], output)
mod['func_4469'] = func_4469
mod = relay.transform.InferType()(mod)
mutated_mod['func_4469'] = func_4469
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4470 = relay.var("var_4470", dtype = "uint32", shape = (560,))#candidate|4470|(560,)|var|uint32
func_4469_call = mutated_mod.get_global_var('func_4469')
call_4471 = func_4469_call(var_4470)
output = call_4471
func_4472 = relay.Function([var_4470], output)
mutated_mod['func_4472'] = func_4472
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3922_call = mod.get_global_var('func_3922')
func_3923_call = mutated_mod.get_global_var('func_3923')
call_4503 = relay.TupleGetItem(func_3922_call(), 0)
call_4504 = relay.TupleGetItem(func_3923_call(), 0)
func_3642_call = mod.get_global_var('func_3642')
func_3643_call = mutated_mod.get_global_var('func_3643')
call_4505 = relay.TupleGetItem(func_3642_call(), 0)
call_4506 = relay.TupleGetItem(func_3643_call(), 0)
func_812_call = mod.get_global_var('func_812')
func_815_call = mutated_mod.get_global_var('func_815')
const_4541 = relay.const([-9,7,6,-2,-2,-10,-4,-1,6,6,-1,8,3,7,5,5,-5,-3,-4,2,7,-6,-9,-7,4,4,6,-7,-9,2,10,-7,-4,8,5,-3,3,3,-8,-6,-4,8,-4,1,-9,7,-4,6,3,3,-5,-10,8,10,-6,10,9,-9,1,6,5,-1,8,-5,1,-8,-6,5,-4,2,1,9,10,-3,-8,-2,2,1,3,10,-6,10,-9,-8,2,-4,-1,-1,10,3,2,-10,1,4,-7,-7,3,7,-4,4,4,-9,10,6,-5,-8,6,-1,9,-10,10,-1,7,-4,10,9,7,-9,-9,6,7,10,10,-2,-7,-7,-2,-9,-4,-1,2,-10,-9,5,-7,-1,5,-8,1,5,-2,4,-9,-2,7,-1,3,-9,2,10,6,-6,1,5,-3,9,-1,1,9,4,7,6,-9,-2,-10,2,2,-5,1,-4,-10,-2,-9,2,-6,-5,-2,-3,-5,-1,5,-10,-1,-9,-5,-7,-7,6,1,3,4,10,-8,-6,8,-9,5,2,-4,-8,-6,-4,5,-1,7,6,2,7,1,-5,5,3,-3,5,8,8,10,8,-1,-4,3,-10,-7,6,-2,-6,7,6,4,9,7,-5,1,-4,4,-1,-1,-3,9,4,-2,-8,-10,1,6,-6,-9,-1,6,-3,7,-7,-6,-5,-2,6,-1,-5,7,-5,-7,-5,1,9,3,-8,-9,-7,7,-9,2,3,10,-4,-3,1,7,-10,-3,-8,10,-5,10,3,-5,-6,-10,8,-6,-6,-1,-1,-4,-9,-10,1,2,1,9,1,8,1,-6,-9,-1,-1,3,-1,5,-4,-6,6,-3,3,-1,-8,-2,1,7,-8,5,3,5,7,-5,-4,-5,10,-5,2,7,-9,10,-7,-7,9,6,4,-5,1,9,10,6,-2,5,1,5,-1,7,3,-2,-10,4,2,-2,-9,10,4,9,9,1,6,-9,2,6,1,-10,10,4,3,-7,-8,-2,-5,8,5,-5,5,1,-9,3,-6,-3,-6,8,-3,-2,4,-3,4,-6,-1,3,4,-3,10,-4,-10,-3,-4,-8,6,9,-3,-2,4,-6,-6,8,3,-4,9,9,5,-6,3,-7,1,10,6,10,7,-4,-7,6,6,-2,7,2,3,4,-9,6,7,-5,5,5,-1,8,3,-7,1,-2,3,4,-2,-4,9,5,6,-9,3,-5,-2,2,7,4,1,8,-2,9,-3,8,-3,-8,-1,9,4,10,-7,3,6,-1,3,-8,-6,-10,-8,-2,1,9,8,8,2,-10,-4,4,-8,4,6,8,-9,-2,-9,9,4,-4,5,-6,3,7,-7,-7,6,10,-5,6,9,2,-10,-1,-10,9,-8,2,1,9,8,4,-1,-6,3,2,-9,3,9,6,-1,-3,-9,10,-4,-7,9,6,8,-8,-5,-4,-7,6,2,-3,6,-2,3,-5,5,1,5,-5,1,-3,-4,-3,-5,4,10,2,7,10,-10,-9,9,8,-7,-5,6,7,7,8,-8,1,4,-5,-9,-1,2,-3,-1,-2,-4,9,7,10,5,-7,-2,2,-2,-7,3,-10,-9,3,4,10,-4,-9,-4,-6,7,-3,-2,5,3,-6,9,1,-7,-7,4,10,-8,-1,-8,-1,-10,3,3,-5,9,5,7,5,-4,6,4,6,-7,-2,5,9,2,-7,-2,-1,6,-9,4,9,-10,4,5,4,8,-4,-1,-8,4,8,-8,7,7,-8,-1,8,6,-3,-3,-10,5,4,8,1,-7,-8,-9,10,-10,-6,-7,-2,6,3,-4,-2,8,7,8,-6,6,-10,10,1,-10,2,-3,10,2,1,-6,-5,1,-8,9,-3,-9,-1,5,-8,-1,2,-5,-3,6,2,-9,4,-10,-8,-8,5,-6,-6,-8,-7,7,3,4,10,2,-9,3,-10,6,4,-10,1,5,10,6,-4,-9,-6,5,-2,-9,9,-4,5,-8,6,-7,-6,6,8,5,6,9,6,9,-10,-9,-10,-7,-5,-3,-2,9,5,-6,-9,4,-5,-9,-6,1,9,-4,-4,-4,-7,9,-7,9,-6,-6,-8,-2,5,5,4,-9,5,9,-6,8,10,-5,8,9,-3,-10,-5,-3,6,4,-4,-2,-8,-6,-6,10,-2,2,-10,-5,-8,-3,7,-5,-4,4,2,6,-9,-4,7,-2,8,-10,-5,-1,-9,-7,-10,3,9,-1,5,1,-10,-10,7,-7,-6,-3,-3,3,9,-10,2,3,1,2,-3,-2,8,-3,4,7,-8,-10,-5,5,-4,-2,-8,-8,1,7,-5,-9,2,5,2,5,-4,-3,7,2,-4,-8,9,3,9,6,-2,-6,-8,10,5,-2,-10,10,4,1,-8,10,8,-1,-5,9,-3,2,8,-1,-7,3,-9,-5,9,-1,-8,6,6,10,-4,9,-6,9,2,6,-7,7,6,-1,1,-1,4,-2,7,-2,-1,-10,-3,-10,3,4,-6,5,6,-6,9,3,-7,4,7,4,-8,-6,5,5,1,-7,-2,-9,-10,5,-2,-3,-5,2,-2,1,-3,10,-2,-8,-6,-2,-7,9,7,7,6,10,-8,5,-1,1,-3,5,-5,10,6,-2,-4,2,-6,-1,-10,4,-3,9,5,-1,-2,6,7,-1,-8,8,3,-3,9,-1,-5,9,2,-4,-10,5,-3,-9,7,-3,-2,-6,1,4,-3,10,-8,6,7,-6,6,8,2,-10,-9,3,4,-8,1,6,9,-10,3,8,5,-8,7,10,7,-8,1,-10,3,1,-2,-5,-10,-9,-10,-6,10,6,2,-7,-4,-7,-6,-1,7,-2,10,1,2,-5,-6,7,-7,-5,7,-9,-9,-7,5,6,1,-2,-3,2,-2,8,-10,-4,-8,-5,1,5,2,6,1,1,8,-2,8,-8,1,-8,1,-7,1,3,7,1,-3,7,7,-3,-3,7,10,-2,1,3,2,-2,-1,-4,-6,-8,-3,10,-4,6,1,9,-9,2,10,6,5,-4,5,-7,-4,10,9,-9,5,10,-9,7,9,1,-7,5,5,10,-9,10,1,3,10,-5,-7,2,4,-7,-3,6,3,3,1,7,10,5,5,-3,2,-3,1,-9,7,9,2,9,7,3,-3,7,-6,-7,4,10,-8,-7,8,-3,1,2,-9,9,3,1,-2,1,3,-3,-8,3,3,4,-7,6,-2,1,9,5,-4,8,-7,6,-9,-6,-9,2,8,-5,6,3,10,-7,-4,3,-9,3,-1,5,-7,8,10,10,-7,-3,6,1,7,-9,10,-8,4,-6,-2,7,-2,5,-7,1,2,7,9,-8,-5,9,8,6,-3,-8,-5,-4,2,-10,8,10,-5,-10,6,3,2,7,-1,3,-5,-9,-8,9,4,-6,1,2,7,-10,-9,-2,-5,2,-2,-10,-6,9,-1,3,-10,-8,8,-6,-10,-6,9,10,9,-4,7,-9,-4,-8,-1,-10,1,-9,-6,4,3,-4,9,8,8,-8,7,-9,-10,-6,9,9,4,10,4,7,-5,-10,9,-2,-2,-3,10,8,10,-10,-9,-10,8,4,-4,-9,-6,-5,9,-1,10,1,-5,-1,-4,3,-1,-8,-2,10,5,-7,8,-3,9,-1,-7,10,-1,4,-3,9,-9,10,-9,-7,10,5,-6,-7,4,4,10,1,7,7,2,2,2,3,4,10,-4,2,-5,6,8,-9,6,-8,-7,2,2,1,6,9,-3,-4,2,-8,-6,6,-6,10,7,6,-4,1,2,2,-5,-8,8,7,7,-8,-2,6,-9,4,6,-10,-6,-8,5,6,9,-10,5,6,5,-2,-8,8,7,-3,-10,5,4,-6,-1,10,-6,6,8,-1,8,3,-4,-3,-1,-3,-1,-10,-2,-5,9,-3,-6,6,5,-8,-5,-8,1,1,8,-6,-4,6,-1,9,6,4,-2,-5,-2,-9,5,-7,9,-10,-1,7,-1,1,2,1,-1,10,-9,-10,8,-7,7,1,1,-2,-8,-10,-10,10,-9,1,-9,-3,6,1,-3,8,2,5,-1,-8,3,-7,-8,-6,1,9,6,10,7,7,10,3,5,7,-2,2,-4,-8,-7,3,10,7,6,-10,-9,-7,2,-2,6,10,8,-3,2,-9,6,6,4,5,-1,6,-4,10,3,-3,-3,8,7,-6,-5,-8,6,10,-9,1,10,9,-10,-9,1,3,5,7,-5,2,7,2,6,-3,-6,5,2,9,-3,3,2,-9,-9,10,-1,-3,-4,2,-6,-5,1,-8,3,3,10,1,-3,-1,-9,6,3,8,6,-7,9,5,-1,-3,2,4,3,4,-8,-10,-5,-6,-8,8,-6,-6,-7,5,4,6,-5,8,6,5,8,-10,4,5,-2,-5,8,-5,2,6,-9,2,1,-1,-5,-10,4,7,-7,1,5,-10,-7,9,7,3,-8,-2,-8,-5,-3,-5,-6,-6,-5,2,3,5,9,9,-1,-3,-1,7,10,-10,8,2,8,-9,-5,2,-5,9,-3,1,3,1,1,-1,4,5,-9,-8,-5,9,-9,9,8,-7,6,-2,-6,-3,5,-9,9,2,3,2,-6,9,2,9,-7,2,6,4,-9,8,-5,4,5,10,6,7,5,-7,-5,10,3,-5,5,3,-8,-1,-2,-7,-9,-4,-2,-6,8,-7,-10,-4,8,3,1,-9,-1,-6,-3,9,-1,-8,-5,-2,-10,7,-8,4,-2,-9,-5,6,9,8,-4,-8,1,9,-4,8,-2,3,-5,5,-4,-2,5,6], dtype = "int64")#candidate|4541|(1792,)|const|int64
const_4542 = relay.const([False,True,True,True,False,True,False,True,True,True,False,False], dtype = "bool")#candidate|4542|(12,)|const|bool
call_4540 = relay.TupleGetItem(func_812_call(relay.reshape(const_4541.astype('int64'), [16, 7, 16]), relay.reshape(const_4542.astype('bool'), [12,]), ), 3)
call_4543 = relay.TupleGetItem(func_815_call(relay.reshape(const_4541.astype('int64'), [16, 7, 16]), relay.reshape(const_4542.astype('bool'), [12,]), ), 3)
func_825_call = mod.get_global_var('func_825')
func_827_call = mutated_mod.get_global_var('func_827')
const_4566 = relay.const([[-7.545642,-1.989795,-7.230423,-7.078874,9.323215,3.732331,-2.834907,4.132970,-7.323698,0.050874,-7.221146,-2.387611,-6.589800,4.226299,3.075664,-1.614453,-8.891061,2.315900,-2.509642,-0.447075,7.833003,3.430995,-0.666508,8.013181,3.128295,-9.548812,-0.468500,-1.490920,-5.544396,7.834007,7.422985,0.387581,-4.226317,-5.024597,-2.743686,-4.587192,-5.821422,5.148795,-0.363281,8.445361,-9.044957,2.722331,-5.923672,5.613082,-1.759933,-7.181710,-0.480040,2.458188,-9.176263,8.429214,-5.275626,-5.513509,-3.163956,0.208521,-6.831540,-4.072920,-5.529723,6.656344,-7.790976,0.109581,8.098008,-7.706746,5.379529,-2.874369,7.662938,-5.803683,3.452306,-3.592224,1.695897,-5.472886,6.107330,-4.547534,0.769099,-0.314533,-1.462360,-3.937600,-2.298886,-4.441896,-2.674314,5.805928,-6.770462,9.653689,7.438904,7.151872,9.555732,-2.584389,8.021771,3.818549,8.708063,-3.599003,1.181564,5.386348,0.711409,-3.231555,2.370275,1.576039,3.594881,3.898766,-2.639137,1.236102,4.050148,-6.571029,-6.364881,1.543948,-9.593032,-1.212554,-2.498876,3.869285,9.309262,3.548637,6.283846,-8.128373,7.447168,1.338398,2.948925,5.690499,3.820113,3.658908,1.424251,4.146984,-5.529476,-8.524356,1.852874,-0.968350,7.232935,8.973826,-1.833226,6.907914,-0.690045,4.084655,-8.036687,-3.276192,3.888908,7.168087,-8.325124,-5.348793,-0.411665,0.809855,-9.275786,-9.680653,9.974556,-8.754513,-5.077285,9.818292],[4.127069,-3.170651,6.761328,8.218300,-0.880126,-0.069200,6.151105,0.886277,3.763585,6.506211,-7.499212,7.587672,-2.636327,7.758806,8.648614,3.467519,8.764440,-1.929505,-1.384217,4.630591,6.619996,7.837684,-4.735929,-0.050444,7.151650,4.700199,-1.338858,4.104309,2.442749,8.315871,2.553909,5.795876,-2.862077,8.136896,6.212323,6.716801,-9.462842,4.601051,2.817921,-4.937937,4.656994,-7.093077,-6.514567,-7.885042,-6.079411,0.288777,-3.610681,-3.347838,-3.316382,5.428052,0.760319,-0.909179,4.753259,-0.964844,-2.780924,4.693148,0.607362,6.832714,7.306687,4.563499,5.967786,7.325443,0.430889,-0.019688,-6.344845,5.880876,-8.269685,4.324115,5.615065,-1.742548,9.720539,9.955029,8.442270,-8.871667,0.474083,-0.796520,-7.699247,-3.928303,6.693059,-9.708920,6.435420,5.206852,1.132399,2.929767,1.823869,-0.718923,-2.367537,2.896195,-0.149053,-4.638002,2.602700,-1.038111,9.196057,2.538066,4.420828,-5.049123,1.631682,-2.676174,-8.922411,0.486420,0.311850,-5.660812,9.835473,4.018965,-5.608106,8.797334,-6.753121,9.473165,8.407828,5.922204,-9.534888,7.794022,0.124852,3.866843,0.308950,2.246992,-6.158358,-4.026135,9.768100,-3.448010,-0.060913,1.294450,2.679424,-4.378266,5.050120,-9.621077,7.195189,6.433421,3.257648,-0.099215,6.867056,-4.654114,-8.929986,-7.824565,-3.674684,3.628739,-1.019252,-6.206298,9.617435,-4.688394,-6.560155,6.869320,-8.573004,-7.492591],[1.408501,6.271757,6.977749,-6.787383,-7.678671,6.171978,2.615752,7.984830,-3.474342,-0.719109,-6.950862,-6.075888,2.193445,-0.067113,9.710903,3.186796,-0.059233,6.220792,-1.318553,8.348046,-1.496785,-1.021665,3.400051,-6.369448,4.350934,0.277693,8.321754,-5.476651,0.282354,8.594285,1.128073,7.890013,8.906031,1.688572,7.137418,-6.074838,-6.564084,0.734066,0.248386,8.572109,-8.580707,-8.492429,-6.836583,-1.712702,-6.320200,-2.243226,0.036281,4.292868,8.832434,-5.448191,1.370286,-4.287125,7.003135,8.313197,4.940450,7.858746,3.528039,-9.074579,-3.407677,-3.065153,-7.468444,4.311598,-1.501848,-9.745790,8.881980,-8.260668,2.810734,-7.963594,9.306584,0.271179,-1.723781,-1.499835,7.180556,-7.942140,-4.235567,-1.212024,4.875599,-2.791320,-9.835513,4.431066,3.175270,-7.083821,1.465138,-7.664415,-6.903449,6.380982,-3.590810,-7.890643,-3.261638,-5.425151,2.692272,3.122158,-0.391242,6.322276,-6.671501,-9.566123,-9.607040,3.264210,-5.898849,-8.863268,8.292413,8.473614,-9.659095,0.276475,-5.404553,6.352466,-5.055562,1.225961,-5.243190,4.931197,8.235446,-0.471241,-7.961971,5.970194,6.480371,2.772611,-5.467316,3.225208,3.857859,2.582720,-7.954229,1.277055,-0.105416,4.329945,3.352316,8.044332,-1.345613,4.762713,2.320570,3.353265,-8.108598,-1.740773,-8.923185,9.251769,-9.117521,7.870593,9.408000,-4.377254,2.756194,-3.649022,-1.539755,-7.457022,-4.087822,-1.263435],[-5.081103,-1.569650,-8.884414,0.802475,-4.067736,-3.169529,-7.983578,4.447819,8.718862,9.310389,0.304084,2.728656,1.101353,4.503045,0.577946,-9.555523,5.519109,8.770900,5.332596,-1.992689,6.247225,-9.528275,6.313650,-8.489262,1.599146,9.766793,7.200914,8.600443,-3.630734,-9.281003,-2.280129,-0.014887,-8.017874,8.480704,-4.610350,4.901959,7.835692,1.804967,-3.917051,0.833438,6.340075,-4.945021,4.867275,-0.887655,-2.735387,-7.964331,6.127828,3.725062,-0.765390,5.984660,-4.846561,-3.821772,-8.498055,-1.847763,0.753084,7.734688,0.844857,-5.116958,0.660296,-0.134232,9.703712,-5.433937,0.215226,-6.442778,-2.291250,3.109852,8.223399,-9.913100,1.250067,-9.409551,-5.074472,-2.067666,6.914860,7.348415,3.411472,6.704625,-4.411131,7.165887,6.037344,5.081623,7.364710,-1.535004,-9.466993,-7.082244,-7.525225,0.431271,-1.314667,-5.401995,-8.046625,-0.122604,3.986197,-5.938445,2.965038,-6.819399,-7.083502,3.337788,-3.990740,-6.867999,-9.199331,-4.851497,0.936370,-4.550772,2.065252,8.193641,-5.918501,1.979389,6.857061,4.041982,8.690524,7.545346,3.974296,2.485395,0.860938,-8.518033,1.782247,-4.636642,-3.668457,-6.170646,5.332579,5.344124,-2.924066,8.114629,3.313124,-9.351807,-3.640145,-4.954241,-8.809989,5.184244,5.039441,-2.234822,7.978083,2.707062,2.474404,5.639303,3.993864,-7.122531,-1.630733,-0.877956,-6.626703,-9.419837,-8.154066,-0.154148,8.676617,-6.935145],[0.119007,0.243878,6.529358,6.113410,-4.919441,2.165713,6.378869,7.005330,-2.357176,8.691821,5.098988,4.718434,-5.682006,-5.915459,-6.769971,-6.078667,1.427836,-0.770394,-8.223067,9.938692,-8.341002,3.275412,-7.938289,3.316631,-7.666670,1.991031,4.297317,3.351831,-5.779107,2.275696,0.893763,4.495773,7.787208,8.642928,6.090014,-3.672875,-4.239828,4.460458,0.783582,4.295290,-1.374712,5.817033,1.256896,2.067405,-2.867009,-5.163753,7.711238,6.448978,7.195277,-1.472280,2.051869,7.259046,-1.642227,7.248409,6.246819,3.391521,1.299572,6.018553,-9.378617,7.907241,1.574572,-2.131447,5.279103,8.271326,-2.949940,6.152414,5.944209,2.836898,7.153557,7.816998,7.059054,-9.601518,5.498238,-2.385879,9.439331,-9.999516,0.691539,5.000383,-8.277257,-8.555507,-0.474967,0.575595,-0.759276,-3.565139,5.961431,-3.678427,-7.901376,3.885616,3.226947,0.996973,9.526470,4.644746,-1.041247,5.482321,-5.053953,-8.155957,1.738971,-0.050773,-5.173427,-1.640985,-0.365790,5.580130,4.573623,-0.158169,-5.639250,3.271532,1.733875,-2.309640,3.000181,5.443575,6.728001,4.117645,9.340946,-9.342205,-3.328916,6.517567,-9.705184,1.282310,4.461470,-6.276151,-7.349078,-8.054697,-6.986242,5.564095,-3.337724,8.758807,-6.020996,0.763938,-9.227006,-1.563969,-4.832184,5.480380,-3.690933,-5.879968,-4.274264,3.698485,8.366742,8.198094,-3.082171,8.189544,3.126872,4.032292,8.032974,3.810684],[-3.436120,-7.876621,4.761061,3.825399,7.463711,9.150021,-8.077869,-4.549538,-6.607814,-2.837493,-6.463228,-6.854642,-2.307702,-7.576562,-6.569209,-1.097148,6.155749,5.544703,-5.556513,-7.249256,-0.978250,-6.984242,-6.202379,-1.608844,-4.300718,2.066505,5.337732,-2.658284,5.344012,4.258072,-0.831432,7.919331,5.148954,-1.086395,4.806613,9.397308,-2.329606,7.870996,-0.655338,-0.151656,-5.743569,1.199636,4.930101,3.343235,-4.390068,-9.909235,-2.499917,-0.683318,-4.310541,-2.498963,9.852888,2.717527,5.228251,-0.513215,5.644799,-9.507316,0.226118,3.538163,3.648004,2.912451,4.390652,-4.531604,0.947099,9.590497,3.510415,-0.435189,8.795501,-9.055774,-9.344874,-9.253664,6.351774,2.104656,4.966780,7.406750,2.296161,-7.333483,-1.017325,8.558788,-1.669320,9.758952,-1.203200,-2.304395,-6.486631,-4.966247,-5.883001,-4.456171,4.338678,-2.263726,-3.534571,8.163276,-6.081245,-7.553666,-6.531211,8.967281,7.378731,-2.773680,-1.989975,1.318381,0.445532,8.006941,9.702155,-0.072403,0.969554,4.356393,-9.158736,7.284606,-3.886953,-2.986793,7.652961,8.976658,-2.595146,-3.806496,8.937568,2.943786,2.105248,-2.519579,-0.673791,3.898025,5.787953,6.347221,4.224009,-6.553469,8.043857,-4.975959,-5.836701,8.279804,5.259688,7.999654,2.018548,-0.509977,8.365370,9.839767,4.146950,9.462162,4.557986,-2.523082,-3.912937,2.782206,8.798669,-8.051927,2.041653,1.212682,-4.986117,6.702385],[5.251741,-2.304900,-4.571082,3.197605,0.284659,-2.859275,2.296116,5.621729,-0.497659,0.204326,4.598820,5.802302,4.798026,8.025782,-6.333661,-2.482353,-8.998289,-8.963349,-2.177366,-8.220057,3.237450,5.355122,-9.951510,-9.992639,5.285994,-0.055184,1.299233,5.095017,-6.396156,-9.940674,-9.943062,4.059247,-3.203260,5.398908,7.286621,-5.552062,4.786345,1.448051,-3.409863,-4.684188,-1.283864,-2.557629,-3.245102,-5.651747,9.101844,8.405927,7.193033,-6.184977,9.068841,8.082160,-7.623143,3.876775,5.438844,5.479073,-1.684218,4.588049,-6.256407,-7.144337,7.648584,-3.077142,-9.574018,-9.676756,-1.199912,9.759792,2.741752,-6.672096,-6.433677,6.860919,-7.951265,5.520416,-2.313554,1.867779,6.374930,6.646936,7.345048,3.189709,-4.949934,7.612374,-5.678283,-7.446291,8.881828,6.983587,-8.894292,7.016517,6.327169,2.322782,8.958769,6.011548,-6.352122,-7.731777,-8.729936,2.427345,7.988506,8.671122,6.136792,2.869817,-5.029811,-3.126879,6.596309,2.324802,4.262776,-7.458932,-2.532866,4.548808,9.306280,-4.537945,9.313654,-7.886520,-8.185034,-9.572742,8.407751,8.276907,9.256201,-8.450055,5.050466,1.619885,-4.131486,-6.129845,6.382204,4.275008,4.719732,-8.311533,-9.757826,9.066199,-0.098797,-6.019904,-3.768547,5.713296,-6.586748,-4.520414,-0.648509,-3.993290,-1.553892,5.356120,-3.910808,-4.063506,-5.443470,-2.811722,6.398054,4.041395,1.717443,6.261235,3.460374,1.813876],[-4.705565,-9.822156,-5.024751,9.669594,1.848490,-0.006217,7.102809,3.420925,-4.793207,-4.968850,8.284740,3.631691,-8.904902,-5.064564,-3.397943,9.830838,-2.772328,9.923185,-7.957411,6.544391,5.329183,8.887863,-0.307788,-6.933572,-8.689577,-4.194823,-6.304272,-9.862521,-9.399730,4.879025,0.588906,5.790340,-4.997808,-5.342128,7.976297,-1.271586,6.517910,7.043434,-0.635539,-8.418017,7.524526,-7.169912,0.945617,-9.145192,-5.128642,-6.783833,-5.292279,9.287327,-0.629250,7.204825,6.785520,-3.563838,8.691141,-4.203585,6.935828,-9.577014,8.215472,-0.385577,5.627899,-5.159829,-4.421699,2.368249,-9.104535,1.921166,-0.619094,-9.164035,-8.546369,9.040970,-9.667507,5.027864,-9.736262,-5.890574,0.982679,-0.644390,2.295780,-1.899394,4.950022,-8.164488,-1.675583,-7.252249,-8.756354,-7.397836,0.033335,-5.979115,1.370766,1.074012,8.145048,0.395208,5.449259,-4.832346,-8.138280,-2.650471,-1.380419,3.019076,4.776344,-2.362626,-1.238132,-6.178966,-6.495267,5.981225,9.694440,2.430289,1.770804,8.727938,8.420404,6.934136,-8.679667,3.064015,9.696659,5.286805,0.254877,-4.425630,-5.651180,8.941295,-2.315445,-6.051902,-5.269186,-8.886923,-8.855739,-4.412033,5.673981,8.809524,8.195672,8.343636,0.600334,7.107160,-6.619285,-6.162601,8.589695,2.160473,-4.082372,1.557934,3.105733,-4.492010,7.747416,4.579095,1.946293,-0.776639,-6.726466,1.732532,-6.598413,-1.122440,-9.368162,8.921247],[-0.051761,9.755692,-1.086035,3.828825,5.629883,0.648364,-6.309266,3.330968,5.017805,2.470636,9.924972,4.180945,4.401191,-6.318208,-4.180948,3.880846,-1.250687,7.850000,8.090391,6.847556,7.759907,2.552583,4.983746,7.351286,-3.869616,-2.031167,3.989985,6.157903,7.171500,-3.597899,2.608210,9.659494,1.652675,-6.202803,3.712110,9.229937,-1.247594,5.628477,2.858778,-7.966973,2.842306,-4.835671,-1.125460,7.799399,4.440221,9.043552,-1.182404,4.128729,-0.134083,-3.132743,1.509817,-7.397008,5.337584,3.505609,-5.741549,-0.302703,3.373836,-3.686400,7.071076,6.662958,3.498136,7.648077,6.103571,6.847472,4.985380,-7.339430,4.261916,-3.333236,-5.080402,-4.546595,-5.134879,-3.823488,6.728350,3.907965,-1.459508,1.238058,-4.206818,4.837840,8.513449,1.303195,9.763443,6.373647,-2.964400,1.725722,-6.176456,8.719838,-7.004893,-7.621111,-3.194073,-9.208280,-1.185728,-8.411285,0.808983,3.130442,6.612031,3.594145,-5.463897,2.554858,-9.850028,1.910180,-9.212574,0.165464,-1.216944,-7.323159,-5.122147,4.031509,8.981151,3.646585,-5.976476,5.135745,1.301483,-8.920150,-4.933398,-4.409305,-3.036237,3.570040,-4.774646,9.396273,-7.107372,7.686763,4.443142,4.823729,-9.604127,6.138262,0.615924,-4.001106,6.585648,-0.399724,1.367497,-3.594688,-8.630459,-3.619461,4.130593,4.123026,-4.922176,-8.291896,-9.388055,-1.669034,-3.274286,4.418323,-0.498220,-2.138806,-7.322901,5.584662],[9.593256,4.872194,5.237502,-2.970695,4.119054,-8.195107,-9.809381,3.778813,5.284771,5.963871,4.621420,1.571340,5.275891,4.571338,3.502889,2.340137,7.621812,-7.927750,-4.847896,8.353716,6.734276,2.298488,-8.054051,-6.638844,-2.092961,7.440706,-3.230476,-2.478821,-9.776419,0.678052,-7.290881,-7.693111,7.589809,3.386969,7.243810,8.798091,-0.760049,-1.900000,-6.285130,-8.498625,-6.254929,-7.424061,8.796397,-9.677625,2.944137,1.939865,-9.569907,9.457425,-3.215099,-3.337115,8.118498,-2.429008,-1.443526,-8.360049,0.306178,-2.035414,-7.211160,-0.454396,8.880789,4.194675,-3.556331,-1.694936,-3.415883,-0.779969,-3.531429,-1.134559,7.540749,-8.835206,1.512937,-4.153718,5.528672,-7.635965,0.075579,7.903493,-9.712900,3.258761,1.619824,5.459577,5.271066,0.796115,-7.402809,0.905183,-8.380783,-6.950957,-3.128631,8.819397,4.142245,6.865811,-4.465566,0.639096,4.697925,-9.610667,-6.968512,-4.575663,4.695732,-9.892509,2.252574,5.297211,0.621579,5.429572,-9.934641,0.642052,0.299999,6.762618,-1.154785,-2.994169,9.334757,-4.511025,-4.546002,-9.340966,-3.711093,-1.893438,-4.846346,-2.023880,8.786775,-4.805270,-4.036932,0.794830,-8.571449,3.482328,4.233250,9.130358,-5.194735,-3.165262,-7.837492,5.446883,5.954637,1.895787,4.449040,5.179430,5.765421,7.272394,-5.094440,6.426202,8.282570,0.670756,-5.306534,5.565243,-1.759954,-6.009508,-0.436764,-6.707801,8.257852,-7.881617],[5.500220,3.888296,4.310414,-0.598242,7.580919,-9.338709,-1.096799,3.852869,-6.121010,-0.490582,-4.237664,-9.343468,-5.074491,9.084177,-9.270174,-4.379793,5.867997,-2.374470,-5.678473,-2.532044,9.268616,-1.082517,-4.610538,-9.761937,0.412854,-3.450137,8.167869,-7.632586,0.653650,2.298720,5.022521,5.999575,2.203921,2.187222,-8.539220,7.293601,7.913530,6.348053,4.513270,-4.883519,-9.950287,4.247853,5.543346,3.012049,9.842294,-8.609676,6.528757,5.854150,-9.145225,-7.291947,7.466478,-7.553980,-1.535996,-2.697799,4.875590,-5.758912,5.309664,-5.287781,3.650060,6.523252,-0.431760,-1.421756,5.186654,5.223599,-4.937718,-4.848158,1.556893,-6.008049,4.345354,-4.743564,-8.702358,-0.080099,-0.067490,-6.668225,4.836070,-5.155056,-6.267382,8.427773,-6.955000,3.221124,-6.595082,-4.758424,-1.426356,8.210364,-5.366194,-1.929576,-7.553103,-1.881916,1.128863,9.898532,4.368174,9.998900,-7.912108,1.433602,6.995058,8.876693,6.946036,2.852695,8.029146,5.008344,-3.858218,-1.663615,-2.742739,6.356349,5.908334,-2.230553,-8.549042,-7.844921,-5.091113,-7.172651,-9.883019,-4.533609,6.110884,3.372828,-8.099102,-1.978038,8.186239,-1.264376,-3.982897,0.466009,-6.057467,-2.207519,1.818494,3.497045,-6.495026,4.157971,9.470541,-2.950754,-3.981662,7.019514,-6.151031,4.745755,-9.496689,-2.633026,-3.392981,0.931738,1.819736,5.725223,-8.295321,7.730574,-5.070171,-3.062423,-4.158943,4.210750],[-7.626096,0.752547,-3.297653,-5.216024,-1.745985,8.502697,8.266492,1.911329,-7.564417,6.214508,2.531656,-5.840118,-5.323304,-1.445044,6.118787,4.333900,-2.871176,6.637476,1.340297,-3.164694,-8.893951,-0.258182,-0.486971,-0.211647,5.954477,6.582358,-2.666647,-9.395600,-1.704835,5.601928,-8.150168,-8.040178,-0.518547,-4.779699,9.630701,7.570368,-2.578336,3.082806,-5.411629,-1.803348,-3.642551,-0.064203,6.300811,5.745639,9.952756,3.512137,3.252274,2.252371,7.142474,4.936715,-0.956330,-4.499737,3.723622,4.854729,-7.550657,5.913193,5.486895,5.641524,-2.215168,2.094178,-3.588509,-4.511494,-5.322352,8.105499,4.381216,-9.908928,5.706458,-9.073174,4.815511,-1.767579,7.303812,-1.253232,-7.915188,2.875717,-3.581175,-0.755440,-6.907524,-4.784740,-0.639809,-2.145753,-2.622167,2.181707,-7.658715,-0.464641,4.541610,9.564023,-7.475021,-0.161886,3.740113,-9.505712,-3.647178,-3.471322,4.577111,2.182951,-5.256826,7.168923,-3.371387,6.409027,-7.904942,-0.275946,-3.666807,6.388209,8.969735,4.091761,6.944335,-1.182581,3.621598,-6.698396,0.440316,-7.116787,-3.569939,8.510757,7.327711,0.493577,-4.178063,5.659351,1.203825,-6.691996,-3.414216,0.414738,9.574677,3.866914,6.324093,8.759906,5.200049,-3.212108,3.158168,4.712714,-6.224049,-2.365709,-5.782847,-8.659026,-1.886179,7.256857,-8.263992,8.470921,-1.016158,-7.531616,-2.213811,0.552323,-8.232678,6.659568,2.513385,-7.145752],[6.537605,-2.697784,-3.112855,5.000082,4.827701,-3.245448,-4.815667,2.190306,-6.741261,-7.701373,7.391336,6.105514,0.898430,2.041473,2.043192,2.989214,2.776488,-0.685725,-5.215911,-1.344949,-2.520353,5.984172,-6.523996,-9.837904,4.818397,-3.088371,-3.302999,-0.896669,-0.332254,-6.656410,8.654804,1.782307,7.479583,-3.905788,6.660134,-7.899174,1.750383,-7.930640,-9.075351,3.775056,5.517646,6.302793,6.613691,-0.162388,5.229481,0.517716,-0.196666,3.313718,-5.861538,1.497856,4.780495,-5.790213,2.558078,-9.174167,6.062746,0.208119,8.475606,-3.342185,-8.061249,2.590554,8.205883,-4.761350,1.540153,8.003144,-2.222780,5.993844,-8.422049,-8.998729,5.640612,-7.090865,-9.719410,9.526937,-4.651991,-6.644742,-7.779776,-1.502842,-9.094041,3.345661,3.644376,-4.938856,7.791202,0.935200,8.200299,-2.167104,-4.531858,5.108300,-3.839684,5.058491,-8.514710,-8.461782,6.875953,-1.216969,0.276307,0.676412,-1.248757,-4.215627,4.890685,-2.864528,-9.509441,5.428038,4.946229,9.103173,-7.804296,-0.149392,1.416790,5.235908,3.840895,-3.297897,-5.762641,0.558117,4.330535,-5.060285,3.550277,0.776022,9.394478,1.132478,5.160440,0.296292,9.045353,-6.318875,-2.388887,0.238746,3.593463,-6.505466,0.124969,6.108137,-1.094315,4.272538,-2.657271,7.575169,-2.561811,-3.466255,4.198589,2.949401,7.375507,1.514011,1.931865,5.717464,5.017854,-0.416750,-2.150899,4.672052,-4.902973,-1.422251],[-1.982370,-9.906182,-5.119672,-9.340409,-7.182869,-9.731231,-9.481463,2.331202,-3.287210,-1.332471,1.189512,-9.158108,-4.160957,-7.943109,9.229200,5.549466,-8.087789,-9.804294,-4.256102,-2.213783,-6.146726,-4.860536,3.040691,-4.414570,7.338721,6.387113,-9.033349,-5.568450,2.577195,7.709806,7.366928,-0.670311,-3.837779,2.745055,-3.339864,-5.499676,-8.350432,0.171171,-4.263094,-0.649474,-8.830078,-5.414360,9.745579,-8.209020,2.489148,4.449991,-9.180149,-9.397071,-6.061541,-6.010707,-4.445987,5.355399,3.119472,-5.429547,4.204999,6.492246,-1.562943,-4.455577,-1.199348,-5.935818,-0.695857,8.549592,-2.991576,3.738038,7.516262,6.545781,-5.024155,-9.054138,2.078564,-6.815603,4.888815,-0.212135,6.699824,-5.523904,6.021386,-2.293043,-4.644372,2.200350,3.797863,-0.425048,-9.928439,-0.203481,-7.636089,-0.529851,1.499833,-1.608079,6.851648,-8.612680,1.513692,-1.603566,-1.685133,-7.237321,-6.975588,2.596855,2.149890,-8.181850,0.004817,-4.868702,-3.704599,2.527967,0.687513,-0.074729,-6.626134,-1.116918,0.377635,7.253977,9.631435,6.058710,5.618107,9.637757,-1.746799,-9.738974,1.579301,7.115982,2.317433,5.083981,8.952209,0.151670,0.611897,6.375369,9.575113,-4.217880,5.351360,-8.650125,-8.706941,0.216467,-0.536277,-6.047917,-4.513702,4.000071,-1.430492,8.782880,-7.341274,5.584047,-1.165856,3.358682,0.894134,-5.281327,9.396264,7.381266,-7.749635,-3.837126,-3.498207,-1.453026]], dtype = "float32")#candidate|4566|(14, 144)|const|float32
call_4565 = func_825_call(relay.reshape(const_4566.astype('float32'), [9, 14, 16]))
call_4567 = func_825_call(relay.reshape(const_4566.astype('float32'), [9, 14, 16]))
output = relay.Tuple([call_4503,call_4505,call_4540,const_4541,const_4542,call_4565,const_4566,])
output2 = relay.Tuple([call_4504,call_4506,call_4543,const_4541,const_4542,call_4567,const_4566,])
func_4571 = relay.Function([], output)
mod['func_4571'] = func_4571
mod = relay.transform.InferType()(mod)
mutated_mod['func_4571'] = func_4571
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4571_call = mutated_mod.get_global_var('func_4571')
call_4572 = func_4571_call()
output = call_4572
func_4573 = relay.Function([], output)
mutated_mod['func_4573'] = func_4573
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3922_call = mod.get_global_var('func_3922')
func_3923_call = mutated_mod.get_global_var('func_3923')
call_4580 = relay.TupleGetItem(func_3922_call(), 0)
call_4581 = relay.TupleGetItem(func_3923_call(), 0)
output = relay.Tuple([call_4580,])
output2 = relay.Tuple([call_4581,])
func_4584 = relay.Function([], output)
mod['func_4584'] = func_4584
mod = relay.transform.InferType()(mod)
output = func_4584()
func_4585 = relay.Function([], output)
mutated_mod['func_4585'] = func_4585
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3809_call = mod.get_global_var('func_3809')
func_3810_call = mutated_mod.get_global_var('func_3810')
call_4597 = relay.TupleGetItem(func_3809_call(), 0)
call_4598 = relay.TupleGetItem(func_3810_call(), 0)
func_4108_call = mod.get_global_var('func_4108')
func_4110_call = mutated_mod.get_global_var('func_4110')
call_4606 = func_4108_call()
call_4607 = func_4108_call()
func_426_call = mod.get_global_var('func_426')
func_429_call = mutated_mod.get_global_var('func_429')
const_4618 = relay.const([-6.655106,-9.248802,6.816223,-3.269144,-7.436778,1.152689,-6.280754,0.222320,-4.327402,-4.615867,5.027094,-9.103701,-4.516752,2.777325,-6.244279,-3.188721,4.694092,-2.667383,7.928757,-0.076171,6.648777,-5.344428,0.429463,2.038160,-4.036248,-2.919127,-5.031036,2.802951,-3.516718,-4.481542,0.936393,4.357708,-0.803250,2.144959,5.101646,0.027458,-1.084770,-4.676541,6.002380,9.771574,8.598121,8.150745,3.018028,3.851034,7.042161,-1.560696,-4.736269,4.432958,9.242505,4.686429,-9.432886,0.727090,-1.762585,7.146538,9.338920,8.251815,-6.827236,7.869756,-1.824066,6.407229,-5.338290,-0.688284,-2.675117,8.780828,0.279418,-9.662605,9.544773,-8.370046,0.327312,-1.817016,-6.368162,-1.493642,-2.273592,-5.046631,-1.814425,5.447180,9.168953,5.248926,8.704789,9.086344,1.299177,8.381447,-9.593625,5.564501,6.827672,-9.282355,8.702869,-5.728253,-5.086016,-7.722715,-0.890572,-1.357779,-5.068230,9.640800,-9.077933,-2.509299,-8.731092,7.046830,0.291915,0.299966,-5.164437,-3.570657,-7.931039,4.294558,-1.763614,0.574909,7.428415,-3.987594,6.481894,-6.322583,6.195022,-5.394596,-2.263324,-6.368510,-3.904119,-5.601750,3.834431,-9.374499,9.175848,6.459413,-2.809402,-7.759595,-7.920978,2.459657,2.342199,6.579778,-7.330633,-4.913058,1.570784,-0.667952,-0.592267,-1.708593,1.397162,9.331035,2.454400,-0.620403,4.114367,7.471738,-6.646245,-1.016423,-3.656222,-0.036509,3.762854,5.577024,7.415003,-7.375555,-9.967738,6.141960,9.145132,-9.350653,7.856172,-2.994066,-7.065765,-6.021072,-5.799412,-4.628279,5.771704,9.665270,7.958918,0.683738,-6.083708,3.121558,9.885746,4.265141,7.937689,9.275629,-9.818919,-3.815037,6.313473,7.214129,6.985386,0.995272,-6.397213,4.251680,7.986989,-7.369406,-3.210609,8.096546,0.224037,-2.554867,-3.717854,3.279650,-8.607360,2.722221,7.765005,9.068264,-6.706799,7.376530,-7.457213,1.670155,1.862552,0.022541,9.092612,9.196001,5.068246,4.492614,3.497511,4.809823,-7.277475,-0.417244,6.674725,-3.967695,-8.706595,8.036432,-8.320094,-1.642761,-9.372357,0.684413,-4.051670,-6.103686,6.886988,-2.211380,7.448659,-9.786730,-9.438365,3.948540,-7.208244,-3.730367,8.833340,9.221903,-7.311099,8.465823,-9.178537,-2.479267,-8.984471,-1.861976,-9.632881,-1.682418,-5.132944,-1.721618,2.849856,7.441575,1.352409,-1.043945,5.600701,4.859381,-4.391059,-3.788760,1.995416,8.907355,-8.392059,9.562597,-4.863239,-5.352014,-1.409750,-2.054253,-7.911107,-4.791229,9.000931,-3.821067,-1.653964,-1.913140,-7.598227,0.286366,8.046312,3.892240,1.252611,-7.792531,6.339332,-1.996514,8.895429,3.129323,-7.806174,-8.402600,8.271499,-5.979910,-0.558187,-6.681047,-5.141268,-0.513540,-1.704656,7.012127,7.958471,-7.185991,-9.620281,-3.259468,4.677182,1.109923,6.847225,2.937035,-6.127794,3.338165,-4.498135,4.820293,3.543173,-1.593423,-3.964866,1.693386], dtype = "float64")#candidate|4618|(288,)|const|float64
call_4617 = func_426_call(relay.reshape(const_4618.astype('float64'), [6, 12, 4]))
call_4619 = func_426_call(relay.reshape(const_4618.astype('float64'), [6, 12, 4]))
output = relay.Tuple([call_4597,call_4606,call_4617,const_4618,])
output2 = relay.Tuple([call_4598,call_4607,call_4619,const_4618,])
func_4620 = relay.Function([], output)
mod['func_4620'] = func_4620
mod = relay.transform.InferType()(mod)
output = func_4620()
func_4621 = relay.Function([], output)
mutated_mod['func_4621'] = func_4621
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3642_call = mod.get_global_var('func_3642')
func_3643_call = mutated_mod.get_global_var('func_3643')
call_4625 = relay.TupleGetItem(func_3642_call(), 0)
call_4626 = relay.TupleGetItem(func_3643_call(), 0)
func_1977_call = mod.get_global_var('func_1977')
func_1980_call = mutated_mod.get_global_var('func_1980')
var_4642 = relay.var("var_4642", dtype = "uint8", shape = (2704,))#candidate|4642|(2704,)|var|uint8
call_4641 = relay.TupleGetItem(func_1977_call(relay.reshape(var_4642.astype('uint8'), [13, 13, 16])), 0)
call_4643 = relay.TupleGetItem(func_1980_call(relay.reshape(var_4642.astype('uint8'), [13, 13, 16])), 0)
func_3642_call = mod.get_global_var('func_3642')
func_3643_call = mutated_mod.get_global_var('func_3643')
call_4651 = relay.TupleGetItem(func_3642_call(), 0)
call_4652 = relay.TupleGetItem(func_3643_call(), 0)
output = relay.Tuple([call_4625,call_4641,var_4642,call_4651,])
output2 = relay.Tuple([call_4626,call_4643,var_4642,call_4652,])
func_4654 = relay.Function([var_4642,], output)
mod['func_4654'] = func_4654
mod = relay.transform.InferType()(mod)
var_4655 = relay.var("var_4655", dtype = "uint8", shape = (2704,))#candidate|4655|(2704,)|var|uint8
output = func_4654(var_4655)
func_4656 = relay.Function([var_4655], output)
mutated_mod['func_4656'] = func_4656
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4571_call = mod.get_global_var('func_4571')
func_4573_call = mutated_mod.get_global_var('func_4573')
call_4742 = relay.TupleGetItem(func_4571_call(), 3)
call_4743 = relay.TupleGetItem(func_4573_call(), 3)
uop_4749 = relay.exp(call_4742.astype('float64')) # shape=(1792,)
uop_4751 = relay.exp(call_4743.astype('float64')) # shape=(1792,)
func_3679_call = mod.get_global_var('func_3679')
func_3682_call = mutated_mod.get_global_var('func_3682')
const_4757 = relay.const([-9,4,10,-7,5,-1,-5,-3,-5,1,-3,-7,1,-8,-2,-6,1,2,3,10,-5,5,3,7,3,4,-10,-8,8,-8,7,1,5,-9,3,6,-10,10,-9,1,-4,7,-4,9,-1,2,10,-5,-7,3,6,7,-10,-1,-5,-10,-7,-5,2,-5,-10,10,-10,-4,9,-4,7,-1,10,8,4,2,-7,-4,-10,3,-6,9,7,-3,-3,9,10,-6,4,4,4,-1,5,-9,4,5,6,-8,-7,7,-1,9,8,2,1,-2,-5,5,6,-5,7,-2,3,-6,-10,2,1,3,-9,3,-2,-5,6,7,6,-4,-1,8,6,-4,-6,10,-8,-9,9,-6,-7,-9,5,-8,-7,5,-9,-10,6,-3,-2,2,-7,8,-2,-8,7,3,3,-2,4,-8,2,-7,-4,3,-5,-8,5,-8,-10,6,-6,-1,10,9,3,-6,5,-3,6,-7,-10,-3,10,-4,2,10,-10,-4,4,-4,-1,2,-4,5,1,-2,8,8,1,-8,1,-8,9,-1,7,2,4,2,-6,-1,-10,10,10,-5,7,1,-3,10,3,9,-5,-6,2,10,-6,7,-3,3,4,-2,3,-10,4,-2,-9,5,-1,-6,8,3,8,1,6,3,-3,-10,10,-7,-9,-1,10,-4,-4,4,-8,-7,6,6,-3,-3,-7,5,2,-2,-8,9,9,-9,-6,7,1,-10,6,-10,-6,5,7,-3,-1,9,-9,9,2,1,2,-1,5,-1,-9,10,-5,1,5,8,8,-5,-6,3,4,-7,3,1,-1,-1,-3,-6,-5,8,-10,6,-6,6,-7,1,4,-10,-9,-9,1,-1,-8,-3,-7,-3,-7,-6,1,-4,-1,-10,6,6,-2,6,-2,8,-5,2,-1,-8,3,-1,5,3,-2,-5,-4,2,5,-9,-6,-6,9,-4,5,1,5,2,-7,10,-7,-10,5,9,1,-4,7,7,-9,8,-2,-2,1,10,9,9,-2,-9,10,-6,5,7,1,-8,6,6,5,6,-4,-3,-4,-8,-3,5,6,4,3,-5,-7,9,-1,1,3,-1,4,9,-8,8,8,5,-7,7,-4,6,-7,7,10,-3,7,-1,10,1,-8,1,6,-2,-7,-5,-5,-4,-6,2,9,10,-1,-9,2,1,10,-8,8,-9,2,7,7,-2,2,-10,9,-7,2,3,5,-5,-6,3,-6,-2,-8,-6,10,-9,-9,-3,10,1,5,5,-10,7,5,3,-4,-8,3,9,-3,6,-7,2,-9,9,-1,-6,-5,8,-6,-1,-3,3,4,-1,-10,1,-8,-7,8,-2,10,-9,-4,-7,7,9,7,-7,-5,10,-5,-7,5,-9,9,1,1,6,-8,-4,-1,4,8,-10,10,-10,-10,6,-2,8,8,3,-1,5,-2,-4,-3,-10,10,3,2,4,2,-7,7,-8,-9,4,-9,-1,7,3,-6,10,5,-7,-1,-10,3,9,-5,6,-7,-5,-1,-5,-2,10,-5,5,6,-6,-2,-9,-4,-6,-5,-4,-7,7,5,-6,-4,4,-9,-9,10,-3,4,7,2,8,10,-10,-2,4,-2,-4,-9,6,-7,4,-2,10,-10,-3,-4,10,6,-10,-8,6,5,4,8,1,-7,-5,-3,-5,3,5,-1,-1,4,5,-4,-10,1,-2,-6,-4,-9,1,3,-6,4,-4,-6,-3,-4,10,1,6,6,9,-10,-6,-2,-4,-5,-1,-4,5,8,10,-10,10,2,1,4,3,-3,-7,-6,-1,-3,-1,7,-9,-5,7,-9,7,4,3,-8,-6,-3,-7,5,-1,10,7,9,-10,-3,10,-7,7,-4,1,-5,2,-9,-9,7,-3,4,-4,-4,-7,-5,-10,3,4,-8,-9,10,-10,-2,-3,3,-8,6,9,-8,8,3,-4,7,-4,-10,7,4,-1,10,-5,-2,9,-5,-9,-5,6,4,4,5,8,1,-7,5,-3,-6,10,-3,5,7,3,-10,10,9,9,2,-1,-3,1,-8,4,5,1,1,8,-3,-10,1,9,3,-4,-3,9,-3,5,7,7,-1,9,-8,2,1,-4,-3,2,1,3,1,2,-4,-9,-6,2,7,-1,-10,6,-8,-6,1,9,6,-8,5,2,6,-10,-10,-2,-6,1,8,9,-6,-9,5,-3,-7,7,-10,1,2,10,8,10,5,-9,-9,-10,-5,5,6,-10,-8,7,8,6,1,-4,6,-2,5,5,-2,-2,4,9,-7,3,6,3,-7,-5,-5,-9,3,1,3,-6,10,5,7,-6,-5,-10,-8,-6,-2,-7,-10,-7,8,-2,5,-9,6,-1,-8,-7,-5,-5,-10,1,-1,-8,-5,-3,4,-5,3,-3,5,-4,-2,-9,10,3,-2,1,-3,4,5,-10,-3,7,8,-7,-8,10,-5,-9,1,-4,-4,-8,-5,4,8,-10,-10,8,-9,-3,-9,-6,-9,9,5,-5,-10,8,5,-7,8,5,4,-8,-2,9,1,6,-10,-2,-10,-4,1,-6,-3,-9,-10,-1,-2,9,-7,5,-6,9,-8,9,-9,-8,6,-7,9,-10,-4,5,-7,8,-5,-3,4,6,-5,9,9,-6,-1,4,1,-9,4,-1,-2,-6,-1,-7,2,-6,10,3,-3,4,2,-4,-1,-7,8,-7,-6,9,-3,4,-2,6,-8,-1,8,4,3,-4,-10,-7,-9,-3,9,-4,-8,10,1,-2,-5,-9,-10,6,1,-6,-2,-3,9,-8,6,1,-10,-6,6,-9,2,-3,-1,4,8,-4,4,1,-3,-2,-3,-5,-3,-6,-8,10,-5,4,2,9,-9,2,10,9,-4,-2,-3,2,7,-2,4,-9,-7,-6,-1,10,-6,5,8,9,2,-9,-10,10,-10,6,-6,-3,-8,-1,2,10,4,7,-7,3,10,6,-4,9,9,-8,-2,8,-9,-10,-10,10,4,-7,-6,4,-6,-7,-7,6,4,2,4,8,9,-6,-6,7,6,5,-8,-7,7,7,-2,9,9,-4,1,8,-7,3,3,-5,5,2,-9,10,-2,-10,-1,10,2,5,-3,-5,9,6,-9,-2,3,2,2,-7,-8,-9,-8,1,5,5,-10,10,10,1,9,8,7,5,9,-6,-1,-9,5,8,5,8,4,3], dtype = "int32")#candidate|4757|(1170,)|const|int32
call_4756 = relay.TupleGetItem(func_3679_call(relay.reshape(const_4757.astype('int32'), [10, 117]), relay.reshape(const_4757.astype('int32'), [10, 117]), ), 1)
call_4758 = relay.TupleGetItem(func_3682_call(relay.reshape(const_4757.astype('int32'), [10, 117]), relay.reshape(const_4757.astype('int32'), [10, 117]), ), 1)
output = relay.Tuple([uop_4749,call_4756,const_4757,])
output2 = relay.Tuple([uop_4751,call_4758,const_4757,])
func_4765 = relay.Function([], output)
mod['func_4765'] = func_4765
mod = relay.transform.InferType()(mod)
mutated_mod['func_4765'] = func_4765
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4765_call = mutated_mod.get_global_var('func_4765')
call_4766 = func_4765_call()
output = call_4766
func_4767 = relay.Function([], output)
mutated_mod['func_4767'] = func_4767
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3809_call = mod.get_global_var('func_3809')
func_3810_call = mutated_mod.get_global_var('func_3810')
call_4873 = relay.TupleGetItem(func_3809_call(), 0)
call_4874 = relay.TupleGetItem(func_3810_call(), 0)
func_3214_call = mod.get_global_var('func_3214')
func_3217_call = mutated_mod.get_global_var('func_3217')
const_4877 = relay.const([[2,9,-1,-8,1,-2,6,1,1,10,4,1,-2,5,-2,3,8,-3,2,-5,7,-5,-9,5,-4,1,-10,-10,-9,-8,-6,6,-4,-5,8,1,-7,-8,-3,-8,8,6,6,-10,1,-7,-2,-10,-1,5,5,5,-2,-2,-8,5,2,5,7,2,-5,6,-1,6,-1,3,6,-10,3,-7,-2,8,-4,-9,-8,1,-1,3,-3,-6,-9,-2,7,3,-6,2,3,-2,-2,-7,4,-6,-5,9,-9,4,-1,2,10,9,-8,-4,8,-5,6,3,-10,-7,9,2,-10,-3,-3,-1,10,9,-9,-8,-6,9,7,-6,-10,-1,-8,4,-9,10,-2,5,9,2,4,6,3,5,-7,8,-3,-4,-3,-10,-7,-6,-9,3,-2,7,4,-9,-9,8,5,-3,6,1,8,-4,10,-4,-1,-7,9,-1,9,10,4,4,-6,10,-4,3,-10,5,-7,9,5,2,-1,-6,5,-10,6,10,1,-5,-9,-7,5,9,2,-1,7,2,8,-10,-6,2,2,-5,2,-10,-6,1,10,5,-9,10,8,4,9,-9,-4,-8,-4,1,-3,-8,7,-2,1,-2,4,6,3,-9,4,9,10,-6,10,-2,-8,6,2,-4,-5,-1,8,10,7,-8,-7,1,-4,-2,4,-9,-4,8,3,9,10,-9,-9,-2,8,9,6,-3,-9,-7,8,-3,-3,10,-5,-5,9,5,-5,-4,8,-10,-5,7,9,5,9,2,3,9,-1,4,10,-5,8,-8,3,1,1,2,-1,9,-6,-2,-7,6,-7,7,8,2,1,2,-8,-4,2,-2,2,1,-6,-5,-7,-8,-9,-4,7,5,-8,6,2,8,3,-5,1,2,-2,-8,-8,-5,-3,6,-7,-10,9,-2,5,5,7,-4,9,-6,3,-9,-2,7,-3,7,-5,-4,4,-7,5,-8,3,3,-6,-2,4,-9,6,-4,-1,1,-8,2,1,3,-3,-10,-1,-10,-1,5,4,10,9,10,-4,6,6,-6,-7,-4,-7,9,-5,-6,-1,-2,4,6,-7,-3,-5,-5,-7,9,1,6,-8,-8,6,-1,-7,-2,4,-6,2,4,-10,-10,1,5,-3,-9,-8,5,-3,8,9,2,-8,6,10,9,8,-9,9,8,4,4,-8,-3,5,-2,-1,-10,3,-9,6,10,-5,3,-2,-7,-2,-6,2,-3,1,3,-8,-1,3,-1,-7,-4,-2,8,10,10,-8,2,8,-9,9,-2,-7,9,2,8,2,4,9,-10,1,8,-8,1,6,-4,-2,-3,9,8,1,-3,-9,9,-10,6,-8,-3,7,-2,-4,9,3,4,3,5,1,6,-8,-10,5,2,-2,-2,6,3,10,-5,-3,7,4,-9,4,5,-2,2,10,-1,-6,-5,-6,-4,2,1,2,-3,-4,1,10,9,10,-9,5,5,2,-8,8,-7,3,8,-8,2,-3,-9,9,-7,9,-9,8,8,6,10,-7,-6,5,-6,5,2,-10,-5,8,8,-7,-4,3,-7,-7,4,-4,-6,6,-1,-9,1,5,-8,7,2,3,1,9,6,6,10,2,-10,-8,-9,5,8,-5,3,-2,-8]], dtype = "int32")#candidate|4877|(1, 600)|const|int32
call_4876 = relay.TupleGetItem(func_3214_call(relay.reshape(const_4877.astype('int32'), [10, 15, 4])), 2)
call_4878 = relay.TupleGetItem(func_3217_call(relay.reshape(const_4877.astype('int32'), [10, 15, 4])), 2)
output = relay.Tuple([call_4873,call_4876,const_4877,])
output2 = relay.Tuple([call_4874,call_4878,const_4877,])
func_4883 = relay.Function([], output)
mod['func_4883'] = func_4883
mod = relay.transform.InferType()(mod)
mutated_mod['func_4883'] = func_4883
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4883_call = mutated_mod.get_global_var('func_4883')
call_4884 = func_4883_call()
output = call_4884
func_4885 = relay.Function([], output)
mutated_mod['func_4885'] = func_4885
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4895 = relay.var("var_4895", dtype = "int16", shape = ())#candidate|4895|()|var|int16
var_4896 = relay.var("var_4896", dtype = "int16", shape = (1, 7, 12))#candidate|4896|(1, 7, 12)|var|int16
bop_4897 = relay.less(var_4895.astype('bool'), var_4896.astype('bool')) # shape=(1, 7, 12)
bop_4913 = relay.subtract(bop_4897.astype('uint16'), relay.reshape(var_4896.astype('uint16'), relay.shape_of(bop_4897))) # shape=(1, 7, 12)
output = relay.Tuple([bop_4913,])
output2 = relay.Tuple([bop_4913,])
func_4928 = relay.Function([var_4895,var_4896,], output)
mod['func_4928'] = func_4928
mod = relay.transform.InferType()(mod)
var_4929 = relay.var("var_4929", dtype = "int16", shape = ())#candidate|4929|()|var|int16
var_4930 = relay.var("var_4930", dtype = "int16", shape = (1, 7, 12))#candidate|4930|(1, 7, 12)|var|int16
output = func_4928(var_4929,var_4930,)
func_4931 = relay.Function([var_4929,var_4930,], output)
mutated_mod['func_4931'] = func_4931
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4765_call = mod.get_global_var('func_4765')
func_4767_call = mutated_mod.get_global_var('func_4767')
call_4945 = relay.TupleGetItem(func_4765_call(), 2)
call_4946 = relay.TupleGetItem(func_4767_call(), 2)
func_3753_call = mod.get_global_var('func_3753')
func_3755_call = mutated_mod.get_global_var('func_3755')
const_4952 = relay.const([-2,8,-4,3,-2,-6,-3,-1,4,4,8,2,-1,5,8,9,2,-8,-2,6,5,4,-8,-9,-4,-4,4,-10,-5,-1,1,-2,9,1,-2,-7,9,-7,10,-1,10,-7,-3,1,3,10,-4,-9,4,-4,9,5,5,-6,7,7,3,4,-2,6,7,-1,10,-3,2,-5,1,10,10,-8,1,8,9,2,7,7,5,4,-8,2,-6,-10,6,10,-5,-5,-6,-2,5,6,-3,-5,-3,-4,7,2,2,10,-1,4,-9,-4,-1,9,2,5,2,-4,10,5,-3,-1,-8,-2,9,7,-6,4,9,1,-1,-7,-8,-8,-6,-6,-2,5,-7,-1,5,-6,-10,6,6,-3,8,9,-10,6,2,6,-10,5,7,4,7,1,-4,9,6,6,9,-2,6,6,4,3,-10,-1,-6,9,7,-1,8,-1,-9,10,6,-8,2,10,3,-9,-4,3,5,1,1,5,1,4,4,-9,-6,3,-10,-3,6,9,-10,10,-2,9,5,5,-1,8,-2,6,-6,5,1,1,10,7,-10,-9,-10,-8,-2,2,1,-9,-1,-1,3,2,-4,1,-3,-5,-7,-7,-3,-3,9,10,-7,3,5,4,-7,-4,-1,6,5,-7,8,-1,-1,7,10,-10,-8,5,-6,-3,-9,-6,4,-6,-5,-3,-9,5,-7,-9,-2,5,1,-5,-1,10,7,-2,-7,-10,-1,7,-7,1,-5,-2,1,-8,7,1,-4,-2,6,2,2,10,-8,5,-9,1,7,4,-3,10,6,10,4,-10,5,6,7,3,2,1,4,-7,7,1,-4,10,4,-1,-3,9,-5,5,10,7,4,7,-10,-1,6,7,-2,-1,8,-3,2,-6,6,1,9,-1,-8,3,3,-6,-5,-2,-9,-3,4,5,9,-5,5,4,5,-7,4,-10,-5,7,-7,-8,1,-3,-9,-2,-2,-7,4,8,-9,-10,-8,-1,7,2,-8,-2,2,-5,-4,3,-4,2,2,-7,7,-5,10,-8,5,-2,-10,1,10,5,4,1,-8,8,-2,-2,-2,6,4,-8,-3,1,5,-5,9,10,-10,1,-3,-10,4,6,1,-10,3,2,-10,-9,-7,1,-8,9,-3,6,1,-3,-9,1,-8,-3,-8,-8,9,5,-4,4,-9,-10,7,-10,-3,1,9,-10,-4,-9,1,3,5,-8,4,8,8,8,3,4,-1,6,9,-7,2,-5,3,4,6,4,-5,5,-10,1,-1,1,-1,3,4,3,8,-8,-8,7,-4,5,-5,7,3,3,2,-7,-9,-3,10,1,-3,-9,3,6,8,1,2,-1,5,-1,5,9,10,-1,7,-10,-2,5,4,-3,1,-6,-1,7,10,-4,-8,1,7,10,-3,-6,1,10,-3,10,8,-8,-4,4,5,-10,-1,2,-4,-1,7,2,1,3,-5,-9,-8,2,1,5,4,-10,-10,-2,-9,1,-2,-1,-5,6,-7,4,3,-5,-2,2,-10,2,7,2,6,-1,8,-9,6,4,-4,9,4,2,6,3,-6,-4,6,-6,-9,1,9,-2,-7,10,-5,-9,-3,-7,2,-3,-7,-1,4,5,6,-3], dtype = "int32")#candidate|4952|(600,)|const|int32
call_4951 = relay.TupleGetItem(func_3753_call(relay.reshape(const_4952.astype('int32'), [600,])), 2)
call_4953 = relay.TupleGetItem(func_3755_call(relay.reshape(const_4952.astype('int32'), [600,])), 2)
output = relay.Tuple([call_4945,call_4951,const_4952,])
output2 = relay.Tuple([call_4946,call_4953,const_4952,])
func_4954 = relay.Function([], output)
mod['func_4954'] = func_4954
mod = relay.transform.InferType()(mod)
output = func_4954()
func_4955 = relay.Function([], output)
mutated_mod['func_4955'] = func_4955
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4765_call = mod.get_global_var('func_4765')
func_4767_call = mutated_mod.get_global_var('func_4767')
call_5017 = relay.TupleGetItem(func_4765_call(), 1)
call_5018 = relay.TupleGetItem(func_4767_call(), 1)
func_2124_call = mod.get_global_var('func_2124')
func_2127_call = mutated_mod.get_global_var('func_2127')
const_5030 = relay.const([-4.904519,-6.917239,-9.325621,4.078591,2.618238,-9.452903,6.307782,9.458562,5.476620,0.894482,3.994811,3.222573,-9.872569,7.903440,-3.353496,9.761014,4.829984,-9.292335,-5.811326,6.904373,8.374131,4.072490,6.271123,0.224095,0.583243,-8.313525,8.785458,7.906567,1.641217,2.061310,-2.200233,-9.587435,8.409646,3.241208,-0.557183,4.775557,-4.825772,-8.031271,7.670992,-5.374557,-0.993388,9.171107,8.018453,4.759888,-9.745334,-6.557047,9.433217,-7.719078,6.575900,-3.213162,-8.554274,4.567747,-6.560465,6.528105,5.921324,-4.720691,-8.654504,2.722076,-9.041415,-4.885894,1.882011,1.266358,0.621353,2.855615,0.001284,-5.666948,0.880568,4.186390,9.065860,-5.461342,-5.732250,7.797510,-1.013779,-8.584824,1.326557,7.348258,6.904511,-2.540534,5.191320,7.270066,3.931525,-2.102645,7.220930,8.945453,-2.980697,2.415524,-2.289713,-7.824990,3.447276,-1.099107,5.693420,-5.058345,-6.975648,-7.141997,-5.766560,4.874846,2.174119,0.409295,2.519673,-9.836011,-0.965743,-5.930742,-8.455999,2.452212,-4.878704,-7.667388,-0.257662,-2.763234,5.934243,-0.760704,0.402329,-8.655107,5.962113,0.386069,-9.063020,0.851553,-0.615716,6.068470,-1.198714,-6.263199,-2.359357,-2.347451,0.310449,-0.863909,6.906258,6.677162,-1.794478,-2.235723,2.034690,-4.150134,3.299035,-5.709713,0.143778,-8.122589,-2.642889,-0.121344,7.644987,6.618323,-0.065256,-0.140584,-6.277215,-5.418722,8.517873,3.245640,-2.071713,-5.585259,1.645504,7.489771,-6.925034,-5.533097,5.075282,-4.395557,7.704464,7.708543,1.077772,-3.477530,6.270076,-6.782005,2.821590,2.125074,5.361400,3.403322,-9.187462,4.657958,-3.938359,-3.941502,4.740631,-5.052310,-4.684725,-0.970704,4.296842,-5.290802,5.787144,0.080701,-3.284578,-3.307693,-0.338804,-6.329934,0.673686,-6.180781,8.710779,2.131213,1.398971,4.861804,2.597770,1.224294,-2.563839,-9.689282,-8.868766,-4.471475,-9.894129,-5.226683,-9.472856,-3.376692,-7.765291,6.659906,1.434510,-4.067309,0.979331,-8.267529,9.852691,5.445735,2.145064,5.641744,-8.750117,-6.456049,0.976348,9.004848,4.851422,6.993973,-3.285549,7.732946,8.309749,-6.935473,-5.813700,0.438446,-6.273687,9.175031,-8.203046,8.403173,8.743924,-2.369071,-9.911089,-1.944513,9.345226,-6.628588,3.677920,0.135172,9.776673,7.461508,-3.972217,-5.389270,0.614938,3.286162,-1.387513,-7.880432,-4.125546,-6.989621,4.981862,5.253847,-0.564529,-3.704522,7.264252,-3.350045,-0.073217,-3.111464,3.529234,6.155950,0.518411,-9.005915,-3.962341,8.601677,7.823469,2.599685,-9.372130,6.777124,-6.849531,-2.303255,1.279921,2.510917,-3.724894,4.133140,-6.480444,7.887049,6.810355,2.441039,-7.757630,-6.514617,6.938110,-3.447237,-1.186520,-8.243530,-4.846290,6.423165,-0.748911,5.699841,-5.010571,-6.390215,3.700801,-4.366441,7.249391,-9.876538,-2.110657,-5.645266,1.899504,-7.859989,-1.203551,-1.920529,8.622070,0.711774,-4.491694,9.095610,9.369798,3.251732,2.750748,2.286472,-9.425949,-0.463540,-0.865128,-1.364910,-5.374729,-1.004559,4.300300,5.035073,-0.809555,-0.052302,5.311387,4.869142,7.154474,0.464908,7.418763,-7.056408,9.514181,-2.542861,8.572020,8.488585,0.753024,-3.653424,-5.881187,-1.222969,-3.349699,-2.987444,-2.371419,-0.913626,-8.487010,-1.953312,-7.292732,2.566291,0.324981,-5.676779,-8.287086,-1.513031,6.339401,7.293359,-3.637533,-2.403751,-7.897273,-4.821337,-2.919196,9.531496,5.647612,-5.089120,-8.116498,1.885969,-3.435843,-5.966541,0.755281,-4.704212,7.586931,-2.570860,2.511938,4.276634,0.414242,-9.869418,-3.135055,7.590406,9.346670,-3.261393,8.106082,-0.739830,9.103825,1.300585,9.002572,6.309079,1.498500,2.909584,-7.860633,-5.970787,-9.921412,8.586827,-8.296466,-2.636939,1.595100,5.093723,-6.372745,-3.936518,-1.126918,-5.534019,6.311598,0.445743,-3.721610,-9.662925,4.974370,-6.137727,1.325202,-0.776992,-1.495634,-5.404791,6.259615,4.220120,7.859759,8.704912,2.789289,1.284518,6.830411,5.032689,2.083862,-1.575037,-2.947422,3.370135,0.051157,-7.429642,-5.180369,8.724700,-2.094382,-6.530137,-4.846873,-2.589454,0.197988,-2.592142,-9.061893,-0.768716,6.317604,-5.836950,-0.149499,-2.749732,3.249707,6.886833,1.657539,-4.584716,5.572665,7.702166,-1.880296,5.215463,0.551136,8.649143,8.929357,-7.380668,-6.280002,7.127789,-2.854025,-9.575163], dtype = "float32")#candidate|5030|(432,)|const|float32
call_5029 = func_2124_call(relay.reshape(const_5030.astype('float32'), [6, 9, 8]))
call_5031 = func_2124_call(relay.reshape(const_5030.astype('float32'), [6, 9, 8]))
output = relay.Tuple([call_5017,call_5029,const_5030,])
output2 = relay.Tuple([call_5018,call_5031,const_5030,])
func_5036 = relay.Function([], output)
mod['func_5036'] = func_5036
mod = relay.transform.InferType()(mod)
mutated_mod['func_5036'] = func_5036
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5036_call = mutated_mod.get_global_var('func_5036')
call_5037 = func_5036_call()
output = call_5037
func_5038 = relay.Function([], output)
mutated_mod['func_5038'] = func_5038
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4584_call = mod.get_global_var('func_4584')
func_4585_call = mutated_mod.get_global_var('func_4585')
call_5039 = relay.TupleGetItem(func_4584_call(), 0)
call_5040 = relay.TupleGetItem(func_4585_call(), 0)
func_4571_call = mod.get_global_var('func_4571')
func_4573_call = mutated_mod.get_global_var('func_4573')
call_5053 = relay.TupleGetItem(func_4571_call(), 2)
call_5054 = relay.TupleGetItem(func_4573_call(), 2)
output = relay.Tuple([call_5039,call_5053,])
output2 = relay.Tuple([call_5040,call_5054,])
func_5059 = relay.Function([], output)
mod['func_5059'] = func_5059
mod = relay.transform.InferType()(mod)
mutated_mod['func_5059'] = func_5059
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5059_call = mutated_mod.get_global_var('func_5059')
call_5060 = func_5059_call()
output = call_5060
func_5061 = relay.Function([], output)
mutated_mod['func_5061'] = func_5061
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4059_call = mod.get_global_var('func_4059')
func_4061_call = mutated_mod.get_global_var('func_4061')
call_5082 = func_4059_call()
call_5083 = func_4059_call()
func_441_call = mod.get_global_var('func_441')
func_444_call = mutated_mod.get_global_var('func_444')
var_5095 = relay.var("var_5095", dtype = "uint16", shape = (48,))#candidate|5095|(48,)|var|uint16
call_5094 = relay.TupleGetItem(func_441_call(relay.reshape(var_5095.astype('uint16'), [2, 12, 2])), 0)
call_5096 = relay.TupleGetItem(func_444_call(relay.reshape(var_5095.astype('uint16'), [2, 12, 2])), 0)
var_5107 = relay.var("var_5107", dtype = "bool", shape = (7, 16, 12))#candidate|5107|(7, 16, 12)|var|bool
bop_5108 = relay.maximum(call_5082.astype('uint8'), relay.reshape(var_5107.astype('uint8'), relay.shape_of(call_5082))) # shape=(7, 16, 12)
bop_5111 = relay.maximum(call_5083.astype('uint8'), relay.reshape(var_5107.astype('uint8'), relay.shape_of(call_5083))) # shape=(7, 16, 12)
func_426_call = mod.get_global_var('func_426')
func_429_call = mutated_mod.get_global_var('func_429')
var_5122 = relay.var("var_5122", dtype = "float64", shape = (288,))#candidate|5122|(288,)|var|float64
call_5121 = func_426_call(relay.reshape(var_5122.astype('float64'), [6, 12, 4]))
call_5123 = func_426_call(relay.reshape(var_5122.astype('float64'), [6, 12, 4]))
bop_5127 = relay.divide(call_5082.astype('float32'), relay.reshape(bop_5108.astype('float32'), relay.shape_of(call_5082))) # shape=(7, 16, 12)
bop_5130 = relay.divide(call_5083.astype('float32'), relay.reshape(bop_5111.astype('float32'), relay.shape_of(call_5083))) # shape=(7, 16, 12)
output = relay.Tuple([call_5094,var_5095,call_5121,var_5122,bop_5127,])
output2 = relay.Tuple([call_5096,var_5095,call_5123,var_5122,bop_5130,])
func_5136 = relay.Function([var_5095,var_5107,var_5122,], output)
mod['func_5136'] = func_5136
mod = relay.transform.InferType()(mod)
var_5137 = relay.var("var_5137", dtype = "uint16", shape = (48,))#candidate|5137|(48,)|var|uint16
var_5138 = relay.var("var_5138", dtype = "bool", shape = (7, 16, 12))#candidate|5138|(7, 16, 12)|var|bool
var_5139 = relay.var("var_5139", dtype = "float64", shape = (288,))#candidate|5139|(288,)|var|float64
output = func_5136(var_5137,var_5138,var_5139,)
func_5140 = relay.Function([var_5137,var_5138,var_5139,], output)
mutated_mod['func_5140'] = func_5140
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4883_call = mod.get_global_var('func_4883')
func_4885_call = mutated_mod.get_global_var('func_4885')
call_5152 = relay.TupleGetItem(func_4883_call(), 0)
call_5153 = relay.TupleGetItem(func_4885_call(), 0)
func_812_call = mod.get_global_var('func_812')
func_815_call = mutated_mod.get_global_var('func_815')
var_5172 = relay.var("var_5172", dtype = "int64", shape = (1792,))#candidate|5172|(1792,)|var|int64
var_5173 = relay.var("var_5173", dtype = "bool", shape = (12,))#candidate|5173|(12,)|var|bool
call_5171 = relay.TupleGetItem(func_812_call(relay.reshape(var_5172.astype('int64'), [16, 7, 16]), relay.reshape(var_5173.astype('bool'), [12,]), ), 2)
call_5174 = relay.TupleGetItem(func_815_call(relay.reshape(var_5172.astype('int64'), [16, 7, 16]), relay.reshape(var_5173.astype('bool'), [12,]), ), 2)
func_3214_call = mod.get_global_var('func_3214')
func_3217_call = mutated_mod.get_global_var('func_3217')
const_5182 = relay.const([6,-8,-8,1,4,-3,10,-3,6,1,-6,-7,10,-6,3,-6,-3,4,-7,-3,8,-5,1,-7,5,8,-8,-2,-2,-7,4,-8,10,-10,6,-8,-9,-3,1,9,9,-7,2,-9,-10,1,-2,2,-10,-10,6,-3,1,7,-5,9,-6,2,8,2,10,5,-10,-5,-9,-9,5,2,-5,7,9,-5,-4,1,-8,1,6,-9,5,9,1,1,-7,1,3,-3,5,7,4,-1,-3,-2,10,-7,7,9,5,3,4,-5,1,-1,-7,4,-6,-6,1,8,-9,-6,-3,4,6,10,-1,-9,5,7,-6,-5,-7,-9,-3,10,4,-8,-3,-4,2,-1,1,3,7,9,-2,8,-9,8,6,4,5,6,6,7,4,-1,7,2,-6,9,-7,-7,-4,8,4,9,-6,7,2,2,-3,2,8,6,-5,2,-2,8,-8,7,2,3,-10,2,6,10,8,3,-4,-10,4,10,-2,1,7,-2,-3,-7,-5,4,4,5,6,5,-5,-6,8,-6,-6,-8,6,-4,-5,1,-9,-5,9,-4,-8,-4,6,3,-7,2,-5,-8,2,-9,10,-9,6,-3,-4,1,-6,4,-6,3,7,9,-8,4,-7,-9,4,10,-1,-7,10,8,3,-7,10,-4,-7,-8,10,-7,6,7,-5,10,-2,3,-4,-7,3,-10,5,-2,9,-9,4,9,3,8,5,-4,-6,8,-7,9,-10,-7,-4,-1,-8,5,8,2,10,-9,-9,-1,-9,-4,-5,-10,-3,3,-5,2,5,-7,-1,-4,8,-7,4,9,8,-2,6,9,-1,1,-7,1,-10,4,-7,4,10,10,9,9,-3,-2,5,2,-6,-3,-6,4,3,9,6,3,5,10,-5,3,2,-8,-7,-4,-1,-3,-1,5,4,-2,-9,6,10,-2,-7,-2,-8,-5,-1,7,5,-1,8,-10,1,-3,-9,-8,7,2,3,-10,-4,-8,-5,7,7,-8,-5,7,10,-6,-1,6,4,-1,-5,10,7,4,-4,-5,8,-6,-2,9,-5,1,-1,5,8,-4,6,-10,-3,6,-5,10,4,8,-1,8,-4,-3,5,-2,-3,-5,10,1,-2,-3,-7,2,-1,7,-9,-1,3,2,1,2,8,-2,-3,-2,-9,3,9,7,-8,-3,1,-4,7,4,-7,3,-6,-4,9,5,2,-4,-1,-3,7,-10,10,-5,-7,9,7,-1,-9,3,4,6,4,-7,10,6,7,-8,-9,6,-3,-1,-6,-7,-9,3,-6,9,8,7,-7,-7,-8,-1,-1,-4,-1,9,9,-6,-4,-2,-9,-10,-1,5,9,-4,1,7,-4,6,-6,-7,-9,-5,-2,-5,10,-8,-4,10,-6,-4,2,9,-2,1,2,-5,1,-5,-7,-3,-6,9,-5,5,3,-10,-9,-1,6,1,2,-10,-7,7,5,-2,-3,3,10,-9,7,10,-10,9,4,5,-5,10,-10,-6,7,8,-9,-7,-10,3,-6,3,3,4,-9,5,6,8,2,-2,3,8,2,-2,2,8,-8,3,-1,9,8,8,9,9,-3,10,-1,-8,4,5,-5,3,4,-5,5,-8,9,-6,-3,10,5,2], dtype = "int32")#candidate|5182|(600,)|const|int32
call_5181 = relay.TupleGetItem(func_3214_call(relay.reshape(const_5182.astype('int32'), [10, 15, 4])), 0)
call_5183 = relay.TupleGetItem(func_3217_call(relay.reshape(const_5182.astype('int32'), [10, 15, 4])), 0)
output = relay.Tuple([call_5152,call_5171,var_5172,var_5173,call_5181,const_5182,])
output2 = relay.Tuple([call_5153,call_5174,var_5172,var_5173,call_5183,const_5182,])
func_5185 = relay.Function([var_5172,var_5173,], output)
mod['func_5185'] = func_5185
mod = relay.transform.InferType()(mod)
mutated_mod['func_5185'] = func_5185
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5185_call = mutated_mod.get_global_var('func_5185')
var_5187 = relay.var("var_5187", dtype = "int64", shape = (1792,))#candidate|5187|(1792,)|var|int64
var_5188 = relay.var("var_5188", dtype = "bool", shape = (12,))#candidate|5188|(12,)|var|bool
call_5186 = func_5185_call(var_5187,var_5188,)
output = call_5186
func_5189 = relay.Function([var_5187,var_5188,], output)
mutated_mod['func_5189'] = func_5189
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4059_call = mod.get_global_var('func_4059')
func_4061_call = mutated_mod.get_global_var('func_4061')
call_5203 = func_4059_call()
call_5204 = func_4059_call()
func_1205_call = mod.get_global_var('func_1205')
func_1207_call = mutated_mod.get_global_var('func_1207')
const_5231 = relay.const([-9.331096,-0.040872,2.532245,8.804658,2.511365,2.761104,-8.090309,-0.139382,0.243542,0.825038,7.680084,-0.046645,2.097816,-8.733589,-7.836803,-8.927700,-7.557712,-5.556278,-1.359614,9.275003,-3.916677,0.615897,-8.559589,-3.804041,7.646781,-2.713919,0.511802,1.562778,-0.590185,-3.215819,9.273211,2.924906,4.251146,-7.992645,8.383901,-4.645342,-9.510895,-4.838554,7.803671,-9.591595,2.244844,3.621727,6.959582,3.647016,-7.468120,-2.431316,-3.647052,-8.052533,-6.810748,7.219221,-8.567010,4.955431,-8.758195,0.860712,4.609814,-0.834864,3.856805,9.683278,-4.101612,-1.579654,-4.793615,8.106978,-9.922518,6.277890,-0.236833,-4.081655,-1.984654,7.219910,5.389190,-2.904464,-5.350917,2.262441,-5.879009,-1.857999,-7.425687,-6.097452,-0.613773,4.999112,6.720749,6.124359,-3.528803,-0.337329,3.333893,8.971141], dtype = "float64")#candidate|5231|(84,)|const|float64
call_5230 = func_1205_call(relay.reshape(const_5231.astype('float64'), [2, 3, 14]))
call_5232 = func_1205_call(relay.reshape(const_5231.astype('float64'), [2, 3, 14]))
uop_5237 = relay.sigmoid(const_5231.astype('float64')) # shape=(84,)
output = relay.Tuple([call_5203,call_5230,uop_5237,])
output2 = relay.Tuple([call_5204,call_5232,uop_5237,])
func_5259 = relay.Function([], output)
mod['func_5259'] = func_5259
mod = relay.transform.InferType()(mod)
output = func_5259()
func_5260 = relay.Function([], output)
mutated_mod['func_5260'] = func_5260
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5059_call = mod.get_global_var('func_5059')
func_5061_call = mutated_mod.get_global_var('func_5061')
call_5269 = relay.TupleGetItem(func_5059_call(), 0)
call_5270 = relay.TupleGetItem(func_5061_call(), 0)
func_2664_call = mod.get_global_var('func_2664')
func_2672_call = mutated_mod.get_global_var('func_2672')
const_5276 = relay.const(-4.320642, dtype = "float64")#candidate|5276|()|const|float64
const_5277 = relay.const([0.009912,1.130169,-7.637332,-0.798251,2.204889,3.876330,0.130606,-9.597597,9.274430,-0.746029,-8.075443,7.233131,-7.307577,-4.532626,0.876671,-9.115318,-2.839293,9.711991,-8.660839,8.607313,-7.612979,3.673317,6.418411,5.210482,-9.610502,-2.849694,-5.459879,-8.897850,7.754572,1.962367,7.662421,-5.527725,9.079957,3.636820,3.053553,4.593406,6.361096,-7.804488,-6.015191,4.583413,4.038788,6.104131,7.229982,7.493850,6.944219,9.574079,-4.452709,-9.890499,-7.201489,0.180358,-0.570315,1.906525,6.737522,-2.436596,-0.855828,-5.652336,-3.439151,7.839474,-5.425632,-2.726650,2.579095,-5.036907,3.075847,-7.324493,-8.818044,-4.790804,-5.876038,8.255183,4.022840,-8.547273,7.800205,0.280843,-2.905183,-7.723877,8.399105,-6.377187,-0.207140,-8.261788,-9.568235,0.855433,-6.652498,1.711080,-8.787223,2.964751,2.949595,1.707744,-1.901703,-5.614771,4.962668,7.684835,6.813256,-8.779119,1.543488,-1.970586,9.920933,-1.117874,3.077942,-9.122714,-3.765229,8.434721,1.712719,0.308921,3.081952,7.310979,-0.729971,-2.940296,-4.603390,8.879335,3.148780,7.599635,-6.957710,2.923820,-9.728873,6.297189,7.973389,-2.506071,4.464834,-2.708458,7.786222,4.100077,1.916965,2.328666,-5.213206,2.938307,-3.046545,-2.872287,-0.208286,-8.636691,-9.895244,-2.856011,-2.390757,-9.306962,-5.431180,6.791171,-3.397286,3.753109,-0.097946,-0.652669,2.858599,-3.883391,-7.085381,-6.039251,-7.139510,2.730105,-3.942340,-7.276174,-4.619565,-5.193167,-8.529834,-1.688736,3.424775,-3.257326,6.296606,-1.546791,-8.910807,-4.725596,-5.275631,9.102765,-8.619716,0.859604,-5.693737,8.210436,-2.419181,2.287756,7.014323,-8.340209,9.785257,-1.102518,3.944487,-8.830184,-6.404983,-1.043220,7.968029,3.303423,2.387114,1.295639,6.721935,-8.392512,-0.437356,-1.801581,-0.637220,-0.423155,8.575507,-8.186528,-2.522342,-8.436311,7.960268,6.104722,-8.454821,-2.240080,8.961991,-6.204447,4.711892,-4.736872,-1.416524,7.789659,8.893768,9.694817,9.186765,6.473361,-2.715209,-4.160760,7.027459,-1.304793,-5.463873,8.064951,-0.639300,-2.155221,-1.619414,-9.775147,9.235702,1.613606,6.869718,5.145209,-9.814240,-8.146799,-0.438266,7.604395,-4.343556,-5.870262,-1.274524,-0.887836,2.301270,-4.387033,-6.139837,-8.288188,0.060434,-6.534557,-3.916021,3.869216,2.664631,5.817386,-5.606940,6.779700,0.806870,5.731536,1.259674,-1.987541,8.189548,-8.981979,2.559138,1.892057,4.319553,-2.223683,-2.671276,-0.028624,0.187051,7.352239,-1.422466,5.791296,-8.186017,-2.031389,-1.918625,-6.436969,0.870446,0.297809,-7.610464,7.208097,9.205999,1.027173,1.268587,4.881394,-1.186576,-5.230175,2.881328,-2.845402,6.778610,6.167778,0.936381,1.741019,-6.120804,-4.586816,0.936755,-1.183706,1.259836,-6.452930,-6.815205,5.135203,9.580845,0.826048,8.784971,-3.549066,-4.684735,6.309648,-6.906407,0.820039,8.735006,7.709987,2.278517,5.300451,9.421894,-2.151182,5.601889,-5.584820,3.969444,8.882493,5.934884,1.269790,7.583032,-4.559568,3.365366,6.978591,7.059152,-7.687765,-9.995338,0.218674,4.850487,5.301428,6.650549,7.277349,-0.266975,-1.452229,7.197984,7.285425,-2.913725,-6.937035,1.157882,-3.442211,-5.668596,-4.846617,0.822742,-4.456629,1.266241,3.046751,-1.542747,3.320508,-9.240939,-3.594851,-8.328029,-3.336406,4.179350,-4.410339,-7.970898,4.326369,2.202523,-5.984477,3.606940,-6.639008,-9.774457,-3.995826,-4.241504,0.292664,6.520173,-4.875241,-8.623570,-5.287290,7.814341,-5.089274,2.812168,-2.439129,9.045950,3.689923,-4.793089,7.533800,-5.960959,5.267425,-9.678492,2.160683,-2.893824,5.150351,-9.898708,2.097316,-0.881202,-1.234438,1.170000,3.364342,3.194842,-4.574154,-2.070867,-1.487941,7.508588,1.362547,6.936114,1.960700,5.887839,-8.620435,-3.136015,8.792150,2.992836,-5.512481,8.981693,-5.397283,2.628169,-7.106305,-5.596701,-9.437734,-5.379229,5.809301,-4.321516,9.919478,9.872338,7.045499,1.909966,0.145238,-9.369567,-1.059019,3.986430,-5.982223,5.664933,-2.333034,-0.599858,1.245763,-0.911935,-1.135909,6.280653,-0.695842,3.610048,-3.823953,5.403838,5.150123,4.165044,1.217222,-9.389173,2.847921,-5.803846,-6.328060,-4.341006,3.834678,-3.509090,3.907260,4.431936,9.073827,-7.462337,-7.029961,1.641262,0.767359,7.562125,1.241415,8.791875,1.741077,-7.273854,-0.521952,0.069386,9.306665,1.542591,7.022227,6.218886,1.460500,-1.333369,5.414946,3.460407,-1.354233,4.691163,6.846735,1.726660,-0.487287,-4.739995,-2.560231,-8.380891,7.906065,0.652138,-8.086883,4.746625,-5.247438,9.006851,9.791674,-9.639451,4.474396,5.711022,-2.537867,0.034338,-7.535033,2.207093,3.744185,3.751475,6.893781,8.656031,4.416000,8.413877,-8.998300,1.983177,-3.214963,-2.796500,7.138550,-0.593181,-9.536206,-4.895427,3.968427,8.544621,6.376517,5.584054,1.406525,-1.581288,-0.045215,-7.151735,1.484331,-2.398051,-9.722571,5.757124,6.738640,4.867824,-2.657087,-9.040194,-1.113922,-7.816593,-9.237839,-6.504122,2.209597,-6.473626,6.510771,-5.298773,-2.324504,-0.604538,6.366032,-1.421904,7.625769,-0.680844,2.735753,5.662183,5.039786,1.692076,0.888202,2.344877,8.964669,-3.569293,5.979068,6.333978,-8.691734,-1.683059,9.902681,-1.891371,-5.063351,-8.892639,2.558043,5.901551,-4.273727,5.539640,4.536167,-6.018885,-2.208684,1.883659,8.780780,-5.396136,-8.011549,-6.559642,5.272710,-1.110189,2.173934,-7.467518,-2.956656,2.736843,-4.766334,-2.915562,-8.754445,-9.211256,-2.405603,-3.125554,-6.832197,6.040938,1.305159,2.084821,-0.379656,-0.303310,-1.441193,-6.480693,0.913519,0.769016,-2.583696,9.600370,-8.791476,-7.002907,4.622107,9.544701,7.718255,-2.275138,-5.615004,2.309897,9.720309,-6.265064,-6.964166,-3.035754,9.374848,-5.184015,7.194784,-9.548378,1.131478,-6.251000,5.039816,0.564111,-3.365638,1.142676,8.346488,2.480711,-2.470240,-4.727682,7.048574,-4.879115,5.201591,-4.047774,-4.075667,-2.540822,0.833886,-3.431667,-8.783108,1.672240,5.025078,2.385907,-2.558718,8.222672,7.234288,2.486127,-9.781754,9.670945,-0.939226,5.496582,-1.044709,3.011928,-8.480939,-6.843203,8.676316,-6.714894,-3.668879,0.535289,-5.051116,1.435065,-4.269194,-3.091249,4.023738,-4.158511,-8.684376,-2.736554,-6.734644,-7.986854,-8.501511,8.986823,4.816474,-6.528493,-6.956346,-1.241052,4.975614,-1.714105,-8.991501,-1.490000,-3.407881,-6.793702,-7.320419,5.162009,-6.209535,-8.364218,-0.865004,-1.142931,2.354612,2.070523,-7.945700,-6.968586,1.439403,8.280341,-5.320612,0.298975,9.741710,2.225380,7.826791,-8.769270,-5.899598,-5.284518,-3.752544,-0.446700,3.906999,6.863552,5.691108,3.109762,-2.536357,6.846578,4.255259,8.249081,-3.667567,-3.128813,8.896889,3.537546,9.137678,-8.176242,-7.599367,8.422594,-0.087015,8.434349,4.319976,1.850682,5.363156,-3.346866,0.856922,0.401015,-8.425302,5.204983,-8.414963,9.571012,-9.608014,-4.389183,1.976688,1.953000,-3.787801,3.118716,5.045848,-9.285703,3.116438,0.604858,-2.188017,-3.180119,2.286066,8.122556,-7.026021,3.024062,-8.353217,1.036844,-5.407433,-0.269830,9.961238,-3.225359,-8.360233,-1.779688,1.530280,-8.038786,-2.049924,-9.164429,4.494053,-8.107661,-8.587701,-7.955878,9.653710,-5.249566,-0.749923,-4.410380,5.365451,0.749096,9.322155,2.689194,6.516720,6.395616,2.965277,3.054769,9.988567,-0.958499,-5.393371,-6.026067,9.115980,5.034804,5.776801,2.061773,-1.500286,-6.959110,-6.065512,-9.509207,-7.230102,-1.174091,7.714159,-2.176948,6.702544,-2.855985,4.764936,3.649121,-1.356574,2.891219,-3.174311,-1.381253,4.819469,2.949816,-5.574366,9.062588,8.572162,-9.826391,-3.718736,9.016512,-5.549168,4.240819,-4.400580,-8.467983,8.248200,4.693096,-0.099870,-3.139107,-1.707016,-0.870624,9.600081,9.741968,4.998993,6.623001,-8.792803,5.401766,-2.905940,4.317735,8.104787,6.241981,8.714268,-3.814454,-3.987207,9.466930,-2.310394,-1.814094,1.568288,-5.491224,6.794179,-1.144166,-4.899713,-5.477170,-0.279646,-9.876220,8.265292,-0.337371,-5.043030,0.145754,2.761419,8.487493,-0.243627,6.748537,-0.600167,-0.263025,0.280550,1.635187,-0.552622,6.764485,1.941244,-4.155669,8.298778,3.255990,5.433399,7.080206,7.826021,1.106875,-5.532471,-5.496819,-7.235780,-6.188644,8.157034,-5.077853,-8.501959,8.412216,8.198740,-6.058562,-3.960633,-5.585128,-4.630242,3.166943,-4.432048,9.861011,1.116403,4.454007,-8.908664,-4.092735,-2.822817,0.645601,-4.654757,-3.245684,-3.805407,-5.875451,6.453673,9.625715,-9.896003,7.050343,1.027122,2.117644,-8.124873,-1.537604,3.841364,6.122312,2.416004,-0.963774,8.857319,4.057270,3.861685,-7.151236,-9.520574,8.127303,-2.444931,-4.087278,4.529511,6.933838,-8.172501,9.128253,-8.011366,1.416868,0.693644,6.057761,0.317289,5.790658,-0.995229,4.818712,9.716192,-1.443057,9.091488,4.527686,-6.691273,5.475055,-1.584046,-5.816605,2.881480,1.047143,3.130870,1.145981,2.304174,-8.677139,-9.626317,4.840861,-8.758930,-4.581244,-8.339979,-9.639145,-5.270148,3.234423,-3.958674,6.350142,-9.636499,7.511283,2.374429,-2.189741,5.055709,-1.839418,-7.445947,1.999494,9.481466,-8.713642,8.022863,2.231660,-7.683070,-5.525561,-2.135412,-3.291096,-3.354408,4.448265,-8.469906,2.675583,-7.973048,-3.487153,5.667252,2.147560,3.523811,-8.954118,-4.479603,-9.775317,-3.653454,-1.800716,-9.602923,2.952681,-9.734173,-3.575216,-2.129537,-6.917022,0.415219,6.587296,-6.388285,-0.145979,1.841612,-5.678170,-1.626870,-6.092958,7.072358,3.208495,-7.829991,4.971668,9.799772,2.247241,2.994173,-1.603188,-8.189522,5.053053,-5.230815,-1.174146,-7.417217,-7.775622,6.681677,8.302424,2.241641,-3.664480,-6.643843,-6.070600,9.256470,5.487765,5.307309,-9.935163,-7.102226,-3.388772,3.665238,-4.903247,6.554571,-3.125431,7.738904,6.036174,-5.093248,-2.371550,1.610716,5.359092,8.925284,7.924660,-1.885573,-6.075483,1.998354,-3.593609,-3.492817,-4.579571,1.897387,-9.904058,7.200414,4.014683,-9.133180,-7.339960,-5.359422,-1.204628,-3.698455,-2.398208,6.904512,5.750193,6.697023,2.188916,-4.684499,3.508120,-8.002841,4.057188,8.112548,-4.539882,-3.448652,-0.684197,-3.132352,-5.335884,-0.517467,1.216461,-9.500853,4.604246,-0.676177,8.472158,-3.347640,-9.720025,-0.526444,-3.540851,-6.256155,8.215236,9.220767,8.577394,4.354232,9.607478,-9.258379,6.999419,6.445172,-5.317698,-2.977869,8.749076,-7.450697,0.589955,3.140942,9.825864,-6.953875,-3.559554,-0.603966,8.300628,-2.866243,0.464980,-9.009429,0.407099,5.976887,2.541151,6.541512,0.414028,2.722718,-1.377526,-4.522365,-9.602097,2.181994,6.743002,1.756813,6.355349,3.658545,-0.663077,5.719950,4.532637,-2.261662,-3.883824,4.104658,7.239951,9.752919,5.314638,5.419748,-0.918484,3.030822,-8.270317,9.909065,-8.530322,3.955199,-3.352108,-4.167594,3.976756,-5.375921,-1.045866,5.886779,-2.007811,6.442163,5.782851,-9.852824,4.784177,4.279954,-8.539160,3.258021,3.800952,8.059442,-3.515569,2.258936,-2.196285,8.173387,-1.828838,1.188048,2.744608,-6.392910,4.713386,5.450968,-6.677771,2.775093,4.992378,5.059415,1.790505,-3.048143,-1.367475,5.262203,8.677793,8.635100,-9.607569,4.491791,-4.196194,-8.053707,-8.556031,-0.323359,-7.412110,3.995266,1.343493,-8.728376,7.238701,-2.904528,-5.408106,8.946141,-2.664532,6.033250,8.005117,7.239014,8.562944,3.242879,1.673331,-6.950650,0.708438,2.142548,4.030130,0.235677,-6.748655,-6.536518,-3.354862,-9.481353,4.715472,1.773342,-0.320648,-6.537124,-3.967253,3.144015,8.497549,2.815436,0.094820,9.900692,-9.759105,-9.812973,-6.307196,9.684107,-3.107138,-9.812889,-7.578990,-2.666718,-7.302402,-9.650685,-3.154065,-0.688440,7.092651,5.577432,-5.813744,3.840445,1.694988,6.366821,5.215272,-4.509650,-1.658417,1.907960,-3.603272,-9.770989,-0.909521,2.778689,-4.504273,-4.481349,5.043696,0.750300,8.230663,-0.593750,-0.354543,-6.374453,0.047239,9.102297,5.049824,-3.115563,-7.682256,-8.436629,8.500250,8.927711,3.800944,0.846803,8.632465,-4.079480,-4.355187,-1.608510,-0.583823,-4.140494,8.723120,-6.874024,-4.694000,8.120818,6.622146,3.785813,3.066317,-2.921249,-5.150413,-1.234652,-0.619035,-0.646056,1.343707,6.144418,-6.627334,6.700025,3.113286,-5.770287,-9.308155,-7.709549,-3.458536,-4.614143,3.802490,-0.506378,6.054116,7.549838,-6.299150,-3.287241,-1.324324,1.011852,1.308422,9.794796,-1.231212,-7.138816,1.515418,-9.718480,-6.188116,2.336372,-9.187161,3.533833,-9.743716,9.880388,2.909659,7.931684,-4.126958,-9.067908,5.002673,-8.687851,0.769723,0.690818,-7.494239,-2.454319,-0.653101,-9.959460,-4.803868,-2.720899,-6.935843,2.742110,8.110153,-3.560655,1.580024,6.369651,-5.828243,8.703296,-6.782658,-0.435727,-2.067646,5.524613,-7.027730,2.471228,-4.143856,-3.695800,-5.627316,-9.549179,-3.419500,1.792479,3.434579,-8.089549,-1.020194,2.712802,-3.848112,8.505002,9.184810,-4.052136,-3.804066,-2.142436,5.592852,-1.779911,-9.174225,-4.260071,9.779137,-4.067664,-7.956973,-5.381820,-5.494220,-5.145318,6.652802,-7.285294,-5.045879,-4.283661,-3.412374,3.819780,8.125215,9.725952,-8.354446,-5.773820,7.082562,-7.570790,-1.993255,4.493919,1.827074,3.337190,9.989984,7.890712,-7.664961,0.829616,-0.955182,4.037974,-1.082838,9.892070,-4.679307,-0.901607,-3.255841,1.194638,3.269894,-1.154008,-3.998156,0.274027,1.240508,-0.277948,-2.246495,-4.496460,-6.915901,2.266365,5.300156,-3.421539,-5.999229,1.967134,8.097282,1.929987,1.465977,4.965039,-5.644193,-5.662198,9.707790,6.282912,-7.125084,-6.577231,1.297788,0.219252,-2.397341,-1.418097,-6.882760,-3.653220,9.434044,-7.739264,9.723402,-9.760429,-2.937878,8.468075,9.660548,9.109636,-3.117336,0.860762,5.065158,-8.612315,-0.786007,1.491533,8.958860,-7.513353,6.797409,5.845602,3.993391,-9.053462,-5.866150,2.766518,3.667444,2.412584,3.712217,6.955056,4.831974,-3.457708,6.753552,-7.269290,1.841366,9.105631,6.640778,7.312037,-9.989555,-8.935174,2.049130,0.148663,2.620943,6.498910,5.277754,5.112870,-5.635716,-8.268824,7.460498,-4.522881,5.233277,-8.434789,2.910596,8.520748,3.699683,-5.153890,-7.128852,5.799935,8.009607,-0.766341,-9.704773,2.689082,5.095331,-6.637248,7.197693,-9.417565,-3.568550,1.129718,-0.006519,4.173377,7.921366,4.120107,0.191785,8.504635,5.074327,4.031801,4.304609,-3.239195,-2.086223,-3.635458,-3.733805,0.637403,2.506214,-0.448786,9.986128,3.856689,0.953565,-4.248096,-5.603600,3.226315,1.157871,6.032783,-8.325047,-2.731182,-9.546676,-1.066350,0.612129,5.695505,-1.120420,-6.391283,3.092386,-7.267136,-6.204307,-2.519772,-3.984264,-8.394026,-0.651468,2.735263,-1.332569,-9.447541,-8.542237,0.987874,-8.116779,-4.712017,-4.464705,-0.270040,-4.640775,-6.347201,-9.910149,0.040645], dtype = "float64")#candidate|5277|(1470,)|const|float64
const_5278 = relay.const([1.905585,-0.913396,4.236468,-2.793933,6.769671,1.090381,-8.771484,-5.621286,6.581379,8.474737,-9.392876,-7.574607,-3.232391,9.280324,-6.560497,8.261902,1.392157,1.399856,-9.941298,-4.704652,8.828080,7.432704,5.626647,-6.587326,2.373066,9.253388,4.327615,-0.534307,8.267098,8.931808,9.429652,-5.435527,-9.645891,-5.401909,8.277179,-6.426422,-4.149083,0.465186,-1.784355,-3.076948,4.363978,7.319908,-3.867122,-5.473935,0.317557,8.076847,-5.747658,-5.026918,6.336303,-3.326327,6.568242,7.319096,-8.181452,-5.148441,-0.355765,-1.865142,-4.506783,-8.361893,1.909887,-2.224874,8.958133,-2.249093,5.013194,-1.516967,2.063643,-8.304890,-3.258663,-1.130967,-0.143352,2.936133,-7.751445,-8.887978,8.128644,3.756581,1.254969,3.953728,6.882837,-4.175883,-0.552147,3.634034,3.216379,7.644751,9.704032,3.157020], dtype = "float64")#candidate|5278|(84,)|const|float64
var_5279 = relay.var("var_5279", dtype = "float32", shape = (2016, 1))#candidate|5279|(2016, 1)|var|float32
const_5280 = relay.const([-1,-3,9,-6,10,-1,-8,-10,-8,2,-2,-10,-10,7,1,6,-4,-6,6,7,6,2,2,7,-7,-4,4,7,2,-4,1,-5,-8,-8,-5,-10,-5,-2,-8,-7,-8,1,4,5,-5,8,-10,-9,-6,-5,-1,9,-9,3,2,2,10,3,5,-9,-9,-4,-2,9,1,-6,-9,10,-9,-7,2,10,-5,7,3,10,-7,-10,9,-6,1,5,-8,-10,-8,8,8,-6,-3,3,-3,7,-9,-6,4,1,3,-7,-2,9,-6,2,9,7,2,-9,4,2,10,-2,-1,4,-8,6,10,10,4,-1,1,-6,-9,10,10,-7,-2,-7,-1,-9,-3,-10,2,-10,3,1,1,-1,-10,-6,-4,1,1,1,10,-4,4,-6,4,-3,7,-5,1,1,-8,4,-9,8,-4,3,-8,8,10,10,-10,-5,9,5,7,-1,-2,-4,1,-10,-2,10,-9,6,2,5,1,9,9,7,-2,8,-7,-5,-8,-3,10,-2,4,10,6,-10,-5,-4,-2,2,-3,-8,-5,-7,9,-5,7,-10,7,-9,-7,-7,-7,-1,-4,-3,-3,7,7,3,8,-7,-5,-6,-8,5,-3,2,-7,-8,-5,-10,-5,6,-3,-8,-7,5,-1,-6,7,6,8,-1,10,6,4,2,2,-9,-9,3,-1,9,1,-1,-9,-8,5,-1,-1,-8,2,-2,10,-7,-2,6,-1,5,10,-10,-3,7,-10,-10,-5,5,10,2,-1,-10,1,6,1,-6,9,4,-4,9,1,-4,10,6,7,4,6,2,-2,-1,-2,-5,-3,-3,2,-3,-1,-9,-8,-5,-10,-4,-2,4,-7,-6,4,-7,10,5,2,-5,9,-6,-9,-2,1,-7,-4,-7,-10,7,-6,-10,-4,10,-5,1,-9,8,9,8,8,2,-8,1,4,1,-4,-6,-6,-4,-9,6,3,7,6,1,1,-3,2,9,4,6,3,-6,-8,1,-7,-7,-10,2,10,-9,-9,-1,10,9,-4,-2,6,-5,10,2,-2,8,1,-10,-7,1,-5,7,6,9,-10,4,-9,-8,6,6,7,2,8,-1,4,9,6,-7,3,-2,-7,6,-7,6,-4,-3,-10,3,8,-3,5,4,-9,6,6,-4,6,10,-4,-9,3,-1,7,-3,7,-9,-9,4,3,1,-7,4,-4,-7,3,9,7,10,-4,-1,8,-3,-3,6,-6,7,1,9,8,-6,-1,8,4,2,-1,-1,2,-6,1,-5,7,2,-3,-3,-6,-3,-3,7,-9,7,3,-8,2,-2,-6,-3,8,10,6,-4,4,3,8,-5,2,-4,-2,10,6,10,-8,4,-8,-9,2,1,3,-3,6,6,4,3,-4,-1,-8,2,-1,3,-3,-4,-8,-10,8,1,-3,-4,-9,-2,-3,-5,3,-6,-6,-4,3,-3,-4,1,-8,8,1,8,-10,-5,3,-1,-7,-1,-7,-1,4,1,-9,-9,-7,8,-10,10,-9,4,-6,8], dtype = "uint32")#candidate|5280|(560,)|const|uint32
const_5281 = relay.const([[-8.271014,9.601918,1.950846,3.398811,-5.355130,2.020811,4.522478,-3.681264,0.865641,-6.624302,6.633124,8.768519,-8.359927,-6.323722,-6.746063,1.408495,-5.351061,6.840799,-4.961423,-6.955053,3.877674,4.688630,-8.573858,-6.891694,-6.883264,1.708515,3.903639,-4.606752,-9.512356,3.458809,-3.710794,4.738286,3.869631,-5.729745,9.090674,3.808320],[-0.556751,3.371866,-5.822756,7.340599,3.842360,-7.667923,2.229526,-9.227389,-8.215082,-6.013388,-1.406021,4.105663,6.539277,2.401273,-1.441280,1.103989,3.141920,6.965216,-4.568923,7.892301,-3.682636,3.211985,-1.793374,9.020253,4.788902,5.752567,7.480734,8.897243,-2.161638,5.375741,8.634611,-2.388862,8.979007,1.711838,-2.951874,2.576201],[-2.734829,-5.207054,5.991941,0.316445,7.967289,-3.140233,6.421283,9.419490,1.920193,9.332941,-0.183350,5.761018,5.224140,6.100290,7.141999,-7.024020,8.870382,6.338785,-7.863556,8.173559,6.882348,-8.217126,-1.028203,3.603903,-4.991310,-4.341427,-7.543519,0.161086,-6.959756,1.629143,7.797549,-8.860283,-5.492577,2.184081,-9.874723,-1.476148],[0.438818,6.682017,8.994351,7.306980,1.468570,-5.552240,5.714446,0.244827,-5.678957,-5.769126,7.072484,9.140331,-2.642129,-8.210827,8.385257,-1.181956,-8.687351,-4.589078,-8.049154,7.259112,-8.480959,5.243084,7.504062,6.452796,9.685680,-4.159016,-4.474283,-2.061887,-7.526323,-8.534896,-8.382837,-8.590467,-7.444740,-9.959950,-1.687443,-8.582021],[7.696146,1.739895,-3.731944,-7.601377,-1.902773,-0.250639,-0.312586,9.095243,-9.125470,7.208028,-3.105754,0.188626,-1.939081,-7.666365,1.044375,5.008405,-2.535460,-3.474227,-8.788374,2.166782,2.483404,3.790403,-9.443789,-3.802547,-5.181661,5.222115,-5.170830,7.110568,-8.299260,2.222483,-5.784351,-0.313907,2.545800,-1.060922,-1.204454,-8.299623],[0.678350,0.796502,-2.219798,-5.181278,6.814384,-2.458715,-3.508657,8.130070,7.256393,9.323118,0.449305,-6.484964,-0.442232,-3.968602,-1.159398,-0.875442,3.723974,-2.781004,9.627623,-7.685677,-9.223230,-9.891614,0.044947,-8.913416,3.988275,-2.282356,3.027471,4.719431,1.859120,-0.012229,4.263579,-1.574043,0.427406,-1.897461,9.151156,1.807635],[0.812096,6.393443,2.288691,3.656149,6.768678,-7.554055,7.920703,-8.281156,1.534958,-2.278330,4.098600,7.176215,2.282879,9.361413,4.586208,2.806425,1.173508,5.567433,-6.838357,6.377036,-7.314235,-1.630978,2.418833,3.023606,-4.025600,7.044270,-7.890782,-3.371255,7.172428,-9.660886,-3.657319,0.995110,-0.954113,6.588525,-1.054563,-5.917598],[-7.820812,-5.621313,9.498726,-0.302166,0.439862,4.669749,6.021343,-9.193987,-4.179581,8.366126,-6.989479,-6.585496,4.749416,1.146000,-2.002298,-1.407035,-8.697550,-2.425264,-5.783374,1.507429,7.573415,0.313376,-4.094547,4.045330,4.354790,-0.738897,4.414771,-2.224070,-0.940251,-5.368504,-1.841793,5.689871,3.053747,-3.419111,-3.627823,-2.828709],[8.396655,-9.998264,2.881159,-0.587030,-8.692005,-2.488545,8.752970,-1.667384,-8.525845,-8.607137,-9.312207,4.952180,0.304209,0.074768,-2.983733,1.103238,-6.513192,8.114718,1.660708,-1.778201,-4.615902,-7.776834,3.893904,2.995094,0.653481,-3.691298,5.851490,-9.489217,-0.024852,7.761528,7.272635,-9.248146,-4.173621,9.337182,4.830054,-2.120082],[-7.333819,1.823324,7.041041,7.494880,-3.777608,-3.876289,2.778840,-8.370285,2.218629,-9.691782,1.894866,-6.912087,1.069358,7.035897,8.548116,-3.880016,-3.065893,8.447922,9.800981,3.601498,7.785312,2.834473,-8.965796,-3.073740,4.434020,-3.084183,0.832115,1.526752,-3.099324,5.558699,-8.454689,7.325179,2.547276,-1.976821,5.684209,-5.117413],[-0.351016,3.211896,4.646663,-4.010768,1.511914,0.141547,2.857692,7.794721,-3.051388,0.501394,-0.565536,3.317902,1.068773,-0.045235,5.806914,4.891366,6.539516,-5.195120,-9.610729,6.600570,4.872600,-2.735447,8.014544,-5.969856,-9.908882,-1.967488,-6.581928,-0.466823,-2.495532,-5.603695,8.881105,0.555320,2.955334,-7.288166,-9.679039,7.856459],[-4.103725,-5.689725,5.850958,9.296081,-3.675591,-9.653808,-1.472796,-0.944482,-2.105807,-4.228506,5.868006,-5.240435,-4.909383,-9.389375,-2.862006,-6.770635,-4.739748,1.981459,-4.393180,8.396749,-2.000596,8.970288,9.300373,5.214098,5.449812,5.338552,5.209451,6.231561,-2.030459,-5.416046,8.327996,-5.255541,5.864779,2.326754,-9.424868,-5.810850]], dtype = "float32")#candidate|5281|(12, 36)|const|float32
call_5275 = relay.TupleGetItem(func_2664_call(relay.reshape(const_5276.astype('float64'), []), relay.reshape(const_5277.astype('float64'), [7, 15, 14]), relay.reshape(const_5278.astype('float64'), [84,]), relay.reshape(var_5279.astype('float32'), [2016,]), relay.reshape(const_5280.astype('uint32'), [560,]), relay.reshape(const_5281.astype('float32'), [432,]), ), 3)
call_5282 = relay.TupleGetItem(func_2672_call(relay.reshape(const_5276.astype('float64'), []), relay.reshape(const_5277.astype('float64'), [7, 15, 14]), relay.reshape(const_5278.astype('float64'), [84,]), relay.reshape(var_5279.astype('float32'), [2016,]), relay.reshape(const_5280.astype('uint32'), [560,]), relay.reshape(const_5281.astype('float32'), [432,]), ), 3)
output = relay.Tuple([call_5269,call_5275,const_5276,const_5277,const_5278,var_5279,const_5280,const_5281,])
output2 = relay.Tuple([call_5270,call_5282,const_5276,const_5277,const_5278,var_5279,const_5280,const_5281,])
func_5293 = relay.Function([var_5279,], output)
mod['func_5293'] = func_5293
mod = relay.transform.InferType()(mod)
mutated_mod['func_5293'] = func_5293
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5294 = relay.var("var_5294", dtype = "float32", shape = (2016, 1))#candidate|5294|(2016, 1)|var|float32
func_5293_call = mutated_mod.get_global_var('func_5293')
call_5295 = func_5293_call(var_5294)
output = call_5295
func_5296 = relay.Function([var_5294], output)
mutated_mod['func_5296'] = func_5296
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4571_call = mod.get_global_var('func_4571')
func_4573_call = mutated_mod.get_global_var('func_4573')
call_5302 = relay.TupleGetItem(func_4571_call(), 0)
call_5303 = relay.TupleGetItem(func_4573_call(), 0)
output = call_5302
output2 = call_5303
func_5323 = relay.Function([], output)
mod['func_5323'] = func_5323
mod = relay.transform.InferType()(mod)
mutated_mod['func_5323'] = func_5323
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5323_call = mutated_mod.get_global_var('func_5323')
call_5324 = func_5323_call()
output = call_5324
func_5325 = relay.Function([], output)
mutated_mod['func_5325'] = func_5325
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4620_call = mod.get_global_var('func_4620')
func_4621_call = mutated_mod.get_global_var('func_4621')
call_5341 = relay.TupleGetItem(func_4620_call(), 1)
call_5342 = relay.TupleGetItem(func_4621_call(), 1)
func_5259_call = mod.get_global_var('func_5259')
func_5260_call = mutated_mod.get_global_var('func_5260')
call_5347 = relay.TupleGetItem(func_5259_call(), 0)
call_5348 = relay.TupleGetItem(func_5260_call(), 0)
output = relay.Tuple([call_5341,call_5347,])
output2 = relay.Tuple([call_5342,call_5348,])
func_5372 = relay.Function([], output)
mod['func_5372'] = func_5372
mod = relay.transform.InferType()(mod)
mutated_mod['func_5372'] = func_5372
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5372_call = mutated_mod.get_global_var('func_5372')
call_5373 = func_5372_call()
output = call_5373
func_5374 = relay.Function([], output)
mutated_mod['func_5374'] = func_5374
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4584_call = mod.get_global_var('func_4584')
func_4585_call = mutated_mod.get_global_var('func_4585')
call_5402 = relay.TupleGetItem(func_4584_call(), 0)
call_5403 = relay.TupleGetItem(func_4585_call(), 0)
output = call_5402
output2 = call_5403
func_5404 = relay.Function([], output)
mod['func_5404'] = func_5404
mod = relay.transform.InferType()(mod)
mutated_mod['func_5404'] = func_5404
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5404_call = mutated_mod.get_global_var('func_5404')
call_5405 = func_5404_call()
output = call_5405
func_5406 = relay.Function([], output)
mutated_mod['func_5406'] = func_5406
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5431 = relay.var("var_5431", dtype = "float32", shape = (8, 3, 16))#candidate|5431|(8, 3, 16)|var|float32
uop_5432 = relay.asin(var_5431.astype('float32')) # shape=(8, 3, 16)
output = uop_5432
output2 = uop_5432
func_5435 = relay.Function([var_5431,], output)
mod['func_5435'] = func_5435
mod = relay.transform.InferType()(mod)
mutated_mod['func_5435'] = func_5435
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5436 = relay.var("var_5436", dtype = "float32", shape = (8, 3, 16))#candidate|5436|(8, 3, 16)|var|float32
func_5435_call = mutated_mod.get_global_var('func_5435')
call_5437 = func_5435_call(var_5436)
output = call_5437
func_5438 = relay.Function([var_5436], output)
mutated_mod['func_5438'] = func_5438
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5323_call = mod.get_global_var('func_5323')
func_5325_call = mutated_mod.get_global_var('func_5325')
call_5452 = func_5323_call()
call_5453 = func_5323_call()
output = relay.Tuple([call_5452,])
output2 = relay.Tuple([call_5453,])
func_5461 = relay.Function([], output)
mod['func_5461'] = func_5461
mod = relay.transform.InferType()(mod)
output = func_5461()
func_5462 = relay.Function([], output)
mutated_mod['func_5462'] = func_5462
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5467 = relay.var("var_5467", dtype = "float64", shape = (7, 8, 12))#candidate|5467|(7, 8, 12)|var|float64
uop_5468 = relay.cosh(var_5467.astype('float64')) # shape=(7, 8, 12)
bop_5485 = relay.logical_xor(var_5467.astype('uint32'), relay.reshape(uop_5468.astype('uint32'), relay.shape_of(var_5467))) # shape=(7, 8, 12)
func_3922_call = mod.get_global_var('func_3922')
func_3923_call = mutated_mod.get_global_var('func_3923')
call_5488 = relay.TupleGetItem(func_3922_call(), 0)
call_5489 = relay.TupleGetItem(func_3923_call(), 0)
output = relay.Tuple([bop_5485,call_5488,])
output2 = relay.Tuple([bop_5485,call_5489,])
func_5504 = relay.Function([var_5467,], output)
mod['func_5504'] = func_5504
mod = relay.transform.InferType()(mod)
mutated_mod['func_5504'] = func_5504
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5505 = relay.var("var_5505", dtype = "float64", shape = (7, 8, 12))#candidate|5505|(7, 8, 12)|var|float64
func_5504_call = mutated_mod.get_global_var('func_5504')
call_5506 = func_5504_call(var_5505)
output = call_5506
func_5507 = relay.Function([var_5505], output)
mutated_mod['func_5507'] = func_5507
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5259_call = mod.get_global_var('func_5259')
func_5260_call = mutated_mod.get_global_var('func_5260')
call_5578 = relay.TupleGetItem(func_5259_call(), 2)
call_5579 = relay.TupleGetItem(func_5260_call(), 2)
func_147_call = mod.get_global_var('func_147')
func_151_call = mutated_mod.get_global_var('func_151')
const_5603 = relay.const([9,-2,4,-7,1,-6,-7,-5,-6,-1,2,-5,3,-1,-2,-10,6,4,-8,-5,-8,10,-1,8,1,6,5,-4,-9,-1,-9,-4,5,-5,8,-1,-10,2,5,-3,-3,-10,2,-7,10,4,9,4,-5,-6,-10,-9,-10,-6,-5,1,-7,4,-6,-10,1,6,1,5,-1,-9,9,-1,-3,4,-5,-3,8,10,2,-10,4,-2,-6,-1,7,-5,-9,3,-5,-9,-4,3,-2,3,4,7,-9,-1,6,-9,-1,9,-3,2,-1,-6,-3,-4,1,1,3,3,8,7,3,9,10,-4,2,9,-8,8,-6,-8,-4,-4,8,-8,-1,-2,-1,-10,1,-4,-1,10,-9,-3,-3,-6,4,3,-7,-10,-8,-3,-7,9,-7,3,-5,-9,3,3,-5,-2,-9,10,-10,4,-3,4,-10,-8,-4,-6,7,-5,-7,6,-7,8,-5,-2,9,10,5,-3,-9,-3,-3,-3,-4,1,-7,3,5,-10,10,-7,9,2,-3,10,-6,-6,2,1,8,-9,-7,10,6,4,3,-6,9,8,-2,6,9,-7,9,-9,8,-3,2,8,-3,-5,-4,-1,-10,-8,5,-8,-4,-5,3,-2,-2,9,-10,2,-9,-2,-10,9,9,-2,-9,-9,7,10,10,2,-8,-7,-8,-2,8,4,-4,-7,10,7,10,-4,2,7,-7,3,2,4,1,-8,9,-4,-5,-7,-10,4,-10,7,4,3,6,5,-8,-7,4,-5,-9,7,1,7,-10,-3,9,2,5,5,3,-1,-10,9,6,-8,-4,7,10,-9,4,3,-4,-9,2,2,5,-6,2,8,9,2,-2,9,4,-4,-1,-6,-4,4,10,-1,1,-1,-5,2,-6,7,5,3,5,-2,6,1,-4,6,-5,10,-6,-9,-9,-5,7,-4,-10,-6,4,-1,-5,-10,9,2,3,-10,-2,-2,-9,-7,-8,3,-9,3,6,-4,6,9,-10,-1,-4,1,-9,-8,-9,7,7,5,8,9,-2,4,-7,-5,-3,-9,7,-4,3,5,8,-9,-1,-2,2,4,6,-4,-8,-9,5,-9,-8,-7,6,4,5,2,10,6,7,8,5,-6,10,7,3,-8,-10,3,6,-9,-3,-6,4,6,1,5,-3,2,-6,9,-6,2,1,-9,1,9,-8,6,8,-5,6,-8,1,-4,-10,8,-9,9,6,-8,-5,-2,3,-8,9,-3,-3,8,2,5,-7,5,5,-8,1,7,-5,2,-6,1,4,-2,7,-5,2,-9,2,4,10,-8,10,-1,-4,-4,-3,-8,1,6,-2,4,-10,4,9,-1,2,1,7,-6,5,3,-5,7,-3,-1,-5,-10,10,-8,1,-7,3,4,10,-4,8,-2,-10,-8,-1,9,-3,-10,-10,1,10,-4,-6,4,6,10,5,8,9,10,4,6,6,-10,4,8,9,-8,8,-4,2,-10,-6,-4,-6,-6,2,10,8,4,1,-10,4,9,4,8,-7,-2], dtype = "uint32")#candidate|5603|(560,)|const|uint32
call_5602 = func_147_call(relay.reshape(const_5603.astype('uint32'), [8, 5, 14]), relay.reshape(const_5603.astype('uint32'), [8, 5, 14]), )
call_5604 = func_147_call(relay.reshape(const_5603.astype('uint32'), [8, 5, 14]), relay.reshape(const_5603.astype('uint32'), [8, 5, 14]), )
func_4654_call = mod.get_global_var('func_4654')
func_4656_call = mutated_mod.get_global_var('func_4656')
const_5606 = relay.const([-7,-9,-10,-7,3,-8,10,2,4,3,1,4,-1,2,-10,-7,-5,-4,-3,1,8,-8,-1,-8,-6,1,-8,-1,-8,3,5,4,4,4,8,-3,5,5,-2,3,3,-5,8,4,-8,-3,4,-2,-5,8,-2,-10,-2,4,-9,2,-2,-4,5,-4,4,-8,5,7,-6,3,-5,6,-9,1,-9,9,2,-10,3,9,-3,6,-5,-10,-7,9,-10,-1,-5,-7,9,-6,1,-5,-1,-2,1,6,10,-7,1,-10,4,9,6,-4,4,-6,-7,9,-5,-6,-8,2,-8,-4,-8,-1,-6,2,6,8,7,5,7,3,7,-8,-2,1,-3,9,9,-4,10,-8,-5,8,-2,-7,9,1,-1,-10,-3,-1,6,-8,1,10,9,10,6,-7,3,9,3,-7,-1,7,10,10,9,-10,1,6,8,5,3,4,5,-7,3,5,5,-8,10,-10,6,-1,-10,9,2,3,6,-3,-9,1,8,-6,8,7,-9,-8,9,-4,-8,-6,-8,8,-6,-5,3,7,-4,4,6,-9,-10,-2,8,-9,-10,7,-6,2,-7,-7,4,4,8,9,1,8,9,-4,7,-3,8,5,-6,4,-5,-6,8,9,7,-9,-10,-4,1,5,-9,7,8,-1,-10,-10,7,-7,5,10,-6,4,8,-4,-4,-4,-7,2,4,4,8,10,1,10,-5,-9,9,-8,1,-3,3,10,10,-7,-5,8,-4,-9,-8,-10,9,-4,5,3,-6,-3,-4,8,4,8,-4,-3,7,-3,8,5,-5,6,-3,-7,5,-7,-2,-3,-8,-8,-9,1,2,10,9,9,-6,-5,-4,-7,2,-10,-9,-5,-5,-1,5,-10,-8,-10,6,1,4,1,8,-9,-4,-7,1,9,-6,-10,-2,7,-9,-7,6,-6,-3,2,-7,-4,-9,1,2,8,10,-8,-8,-2,-3,3,6,4,6,-3,-7,3,7,-10,4,8,7,8,-2,-4,9,6,7,-7,4,-8,-8,-10,5,-7,-7,-4,-2,10,5,10,-1,1,6,3,-1,-4,-1,5,2,8,-8,4,7,3,7,-5,-2,6,-6,2,1,-8,8,-10,-5,2,1,3,-9,9,2,2,-2,-3,-7,-8,9,-3,-9,-9,-1,8,-8,-1,7,-1,-4,4,3,-4,2,-1,6,-10,-6,9,-4,9,-8,-7,10,8,2,8,9,6,-4,4,8,4,7,-1,-2,10,-3,-9,-4,-7,-8,2,6,9,-2,1,1,5,-1,-6,9,5,5,-4,-10,7,-7,5,4,3,-1,9,-10,-7,-3,5,10,-7,-5,-4,-4,-5,8,4,6,-10,-4,8,-5,6,-9,-3,3,2,3,-5,6,7,1,-8,9,-5,-10,6,9,5,-2,-5,-10,-3,6,9,-9,8,6,-7,7,-9,-7,2,8,2,-8,5,5,-3,7,4,8,5,9,10,-6,-3,-5,-6,4,3,6,-2,-9,3,6,-1,9,-8,-10,4,-9,-8,2,5,2,10,7,9,6,1,9,-8,-10,7,-7,7,-10,10,8,9,-5,-8,-2,8,8,2,5,-6,-8,-6,-7,-3,-7,2,8,5,-2,-8,1,2,7,-9,-8,7,1,3,8,5,-8,-1,10,-2,1,7,-7,-3,7,-7,8,-10,-1,7,8,-5,2,-3,-3,5,4,-10,-10,-5,7,-1,10,-6,-6,-10,-8,1,2,10,-10,1,-6,-4,6,-5,-3,-9,-2,4,1,-2,-7,-9,-10,6,6,3,10,10,9,10,4,7,-6,3,4,-6,-10,-2,6,10,5,3,3,1,9,-7,1,-6,-4,-4,-4,-9,-5,-7,-7,2,2,-7,-9,10,2,-8,9,1,4,-10,-6,-7,10,-4,2,-8,3,1,6,7,-7,10,-10,-9,-6,5,2,5,-5,-8,8,1,-1,-3,-2,-4,7,6,5,-4,-6,3,10,-9,-10,1,-3,9,-3,-1,-5,5,-1,9,-6,-4,-1,-2,6,7,-8,-4,-3,5,7,2,-2,-2,-7,8,-6,-10,9,2,-5,1,-9,4,-10,-7,-8,-9,-7,-3,5,-2,4,-10,5,-8,10,4,6,1,-1,-5,9,-9,-8,-3,-6,4,6,-2,-5,-1,-2,4,7,8,-4,-6,10,9,10,2,8,3,-1,5,7,-3,-5,1,-2,9,-3,-1,2,2,6,5,10,-8,-7,9,10,-5,8,-6,-6,-10,-2,3,-5,-4,-8,4,1,3,2,-1,3,-7,1,-5,8,7,10,-4,4,-5,8,-2,-9,4,6,-8,-1,-4,-10,-1,-6,-10,8,-3,-1,7,-8,-8,-4,2,10,-1,-7,-5,-3,5,7,-8,-9,-7,9,-10,3,-6,2,6,-10,-5,1,-1,-8,-8,4,-8,-8,1,-9,6,1,-8,2,7,1,8,-1,8,9,-4,3,4,-9,9,-8,-1,-9,-1,2,-4,7,-5,-4,10,3,4,8,-7,5,-8,-3,9,7,-2,8,-2,-7,-5,-3,4,-1,-2,-6,-9,-7,3,7,1,-4,4,8,-6,6,7,8,-5,-10,7,8,-9,4,-6,-4,6,-9,-7,-6,-3,6,-2,-1,-1,-8,7,8,-2,7,-3,6,-8,-8,1,10,8,3,-10,1,-5,2,4,7,-2,5,-5,5,-5,8,10,-9,4,10,-6,5,-7,-3,-7,-6,-7,6,-1,5,5,1,9,-2,2,7,3,1,-9,1,-7,6,-10,-5,-3,-7,2,-2,8,8,-7,9,-6,-8,-5,2,-5,-5,1,8,-10,10,4,7,-5,-3,-9,-2,5,10,8,3,10,-10,1,3,-4,-5,5,10,6,-6,-10,-8,8,-6,-1,4,8,-2,-2,10,10,-4,-9,6,-10,8,1,-6,5,-7,-10,8,5,-8,-5,-4,-6,-1,-5,-10,-1,6,6,3,3,-10,3,4,7,6,2,6,-8,-5,-4,-9,-3,7,6,-3,-1,5,-10,-9,-1,-9,-5,-3,4,8,-2,2,-4,7,10,1,4,3,-3,10,-9,8,-6,1,-6,-7,-7,-4,-2,1,2,3,-7,9,-1,5,2,4,-4,-7,3,1,-6,3,5,-8,-5,4,-7,6,-3,-8,6,-4,-6,-1,6,-2,-6,-8,6,-9,-9,7,-7,6,3,7,-5,-10,-2,1,-2,2,-6,2,-10,-7,5,7,-6,-1,4,-8,9,-9,8,10,-2,9,-5,-2,-1,4,-2,7,-1,-8,-6,-3,4,-7,1,-2,2,-1,-2,1,-3,-9,-3,4,5,-8,-8,-8,-2,-5,-4,4,-8,-4,9,6,-8,6,3,7,3,9,-6,-4,-3,1,-5,3,1,6,1,-1,-8,2,6,9,5,-1,-6,9,-5,7,5,-5,-7,6,2,-1,-4,-2,-2,-2,-3,-8,-1,8,-9,-5,-7,1,-1,4,-6,-6,7,1,-10,-6,7,4,3,3,9,6,-10,9,-6,7,-7,-2,-2,4,7,7,-4,-3,2,-8,-8,6,1,-1,8,9,-2,10,6,-6,-5,-1,5,-5,4,8,8,-9,-9,6,-10,-3,-9,-4,6,-2,-6,-10,-8,8,10,5,-9,-7,-7,-6,-1,7,1,-5,-5,7,-9,-10,6,1,3,-4,-2,-3,-5,6,-7,3,6,4,-4,-1,-2,4,-9,3,-2,-6,-7,3,-9,7,-10,1,-10,-7,10,1,-9,7,9,1,7,4,-8,8,-4,1,-9,1,-1,-6,-6,-10,-10,-2,9,8,1,-1,-9,-6,8,-10,-4,-4,9,4,7,-8,-3,5,4,-7,9,5,9,-2,3,-1,3,1,-7,5,1,2,6,5,5,6,-1,2,6,-8,6,-5,-9,10,3,2,1,-7,5,8,3,-4,8,-6,-9,-5,-6,-3,9,10,1,4,-8,-10,3,3,-5,-4,-10,-1,-7,-6,-9,7,-4,-9,-9,-8,6,-9,9,6,-8,1,1,9,-8,-10,-5,4,3,6,-8,10,4,2,-3,9,9,9,2,9,-4,7,-7,1,-4,-4,3,6,-5,-5,5,10,-6,5,5,-5,2,-8,-3,-10,8,-9,10,-2,-2,-3,-3,-2,-2,-4,-10,7,1,2,6,10,4,9,-5,-10,10,-5,-8,1,-5,-6,5,8,1,-1,1,-3,3,10,-2,6,-4,4,-9,2,9,-2,3,2,9,1,5,5,-5,-5,-5,-1,-1,3,-2,-7,-4,7,8,-3,3,6,-9,5,8,-1,2,-4,-8,6,-3,-5,9,-8,1,3,-7,-3,4,8,-9,-6,2,-7,-10,-4,-3,2,9,10,-1,-6,-4,3,-9,1,-2,1,9,-8,-1,2,9,6,5,-2,9,-5,8,-2,-2,5,1,10,5,9,-8,10,6,-7,-1,7,6,-4,3,1,2,9,-3,-3,9,-6,6,6,1,-3,2,-2,-4,-3,4,-2,10,-10,-2,-5,9,-8,7,-7,7,9,-1,-10,-9,4,6,2,9,3,6,-2,9,-8,-4,-3,6,-2,4,6,4,-1,-7,-8,-4,10,9,3,-4,4,-9,-10,-10,-3,-4,-2,-10,1,-3,-8,4,-6,-1,-10,-1,2,-3,4,7,-10,8,-1,4,-10,5,-5,-5,9,-10,-1,-5,-1,-7,4,4,-5,7,-5,-8,-9,2,-1,2,2,-10,3,8,-6,10,-9,3,1,9,-2,-8,1,2,6,1,8,-3,-9,-8,5,4,-4,-7,-8,10,3,-10,9,-4,7,-5,7,9,-10,-8,3,-9,10,4,10,9,-2,-8,2,-6,-7,6,-8,7,-10,-2,-8,3,-9,-9,9,-4,6,1,-4,-9,-7,-5,9,-4,-1,-3,-9,9,3,9,-8,2,7,-4,-8,3,7,2,-2,-5,3,1,4,2,-2,9,5,3,-3,-2,9,8,-5,-2,-7,1,-4,-3,-6,8,-7,-5,-8,-6,-7,-4,6,-6,4,-10,-4,-10,3,1,-10,7,-5,4,3,6,8,10,-4,5,-4,-7,-5,-9,2,-10,-10,-4,9,10,-7,6,6,7,2,-8,-8,5,3,4,5,-10,10,1,1,3,-8,1,-5,-4,4,-5,6,-6,5,4,3,-6,7,2,9,-6,-6,-2,9,10,-7,-6,7,4,1,4,4,-4,-9,1,-6,6,-5,-3,-4,10,9,6,9,8,8,3,-5,-4,-7,-4,-1,-5,9,-5,-2,-6,-2,-9,-2,2,-10,-3,5,-9,10,5,6,-10,-9,-9,9,-4,-8,5,-9,-2,-3,5,-10,-2,10,4,1,-10,-10,-1,-4,1,9,2,2,-10,6,-4,-10,1,-8,-5,-10,9,-5,6,-7,-1,-2,8,-6,-8,2,1,2,1,6,9,2,-5,-8,4,9,-6,10,-4,2,9,5,7,3,-7,5,-6,-4,2,1,9,-3,10,9,-10,-3,5,2,-5,-2,-5,-8,4,3,2,-3,-5,-6,-2,6,-5,2,8,2,8,-8,10,7,6,9,-5,10,9,-2,2,2,10,5,-5,-3,-10,-7,7,-2,3,2,4,-5,-10,3,-6,9,-8,-5,-3,5,1,4,5,2,7,-5,6,3,6,7,-2,1,1,2,-6,7,-10,-7,5,4,-1,-5,6,4,6,7,8,-8,4,2,7,-7,-8,-4,2,-9,5,-2,1,-5,7,-5,-10,3,2,-3,-7,-10,5,-10,-1,9,-2,-9,9,10,-7,-3,7,-2,3,2,8,-5,-5,9,3,-2,-1,7,-6,-5,1,2,4,-9,-3,-7,2,-3,8,-2,10,-7,4,10,-1,3,-3,-10,-2,5,9,-4,7,-7,-7,-7,3,-7,-8,-9,2,-2,10,3,2,-5,2,-3,7,4,-9,3,5,-10,-5,-5,-2,1,9,-2,-3,-2,-8,-6,3,9,10,-5,-1,9,6,4,-1,10,10,10,10,-10,7,1,5,3,3,-10,4,2,-7,6,1,7,7,-5,-9,5,-9,5,8,9,7,8,3,9,-6,8,-2,-9,2,8,-8,-7,-9,3,2,9,-3,1,8,-6,7,-2,-8,-10,6,4,-10,1,5,7,7,-7,4,8,9,6,9,5,-10,10,2,8,-4,1,6,-7,5,-5,3,1,-9,-8,-7,-8,7,-1,-1,-2,9,-4,-1,-7,-6,-5,6,-1,-3,5,-3,6,-2,-2,7,10,7,-2,5,-5,4,10,-6,-6,1,10,6,-7,-3,3,-10,8,7,6,-1,-2,10,4,-4,-6,2,2,-2,-8,5,6,2,-3,-6,-10,-1,-10,6,-9,-2,9,1,-4,8,1,-1,9,3,-4,-4,-5,-9,-7,9,-7,-3,9,-6,8,-4,7,7,1,-1,-10,1,1,-10,-5,6,-4,-6,4,5,-6,-2,4,-3,9,4,-9,5,-5,10,-8,3,5,4,-1,-1,7,4,-3,10,10,-3,9,1,-5,-5,7,-6,7,-10,-10,-9,-4,-10,-7,1,4,-8,-4,-8,-2,-3,-1,9,-10,8,2,6,-10,5,9,-7,-1,-8,6,5,9,6,6,9,6,3,5,-6,-8,-4,-10,-1,-8,8,-5,3,-9,-3,6,-1,9,2,5,-1,-2,1,-6,5,-1,7,5,9,8,-1,4,-7,-5,-9,9,-5,-6,3,1,5,10,-2,-1,9,3,-4,-1,1,9,8,1,9,2,-9,-1,-8,6,5,1,9,-3,10,-5,10,3,4,-3,-9,-8,-9,3,-9,7,8,-10,-1,-1,9,-4,-10,8,8,8,8,6,-4,-5,5,8,10,-2,1,2,7,-10,2,2,1,5,-7,-7,9,-3,3,-10,9,6,3,-1,-3,-9,3,2,3,-3,10,1,-3,-6,6,-1,-5,-5,4,-1,9,1,3,-5,-5,-9,10,6,4,2,-5,-7,10,3,9,3,5,-1,-9,7,7,-1,-3,2,9,1,7,-8,-1,-2,-4,2,9,8,-2,-4,-8,-7,1,10,5,8,9,-8,-7,-3,-5,10,8,2,2,8,10,-3,-7,3,-6,4,8,-8,-4,8,5,1,-6,1,8,10,-7,9,5,9,-4,7,-7,-9,-5,10,4,1,-4,-10,6,-8,-2,-8,-10,8,-2,-6,-7,9,1,-2,-1,-7,-7,-9,8,5,-6,-6,-2,10,9,-2,-10,-8,10,-8,-3,8,-3,-3,4,-2,3,-7,-2,8,3,-8,8,-8,6,-9,-2,-10,-4], dtype = "uint8")#candidate|5606|(2704,)|const|uint8
call_5605 = relay.TupleGetItem(func_4654_call(relay.reshape(const_5606.astype('uint8'), [2704,])), 3)
call_5607 = relay.TupleGetItem(func_4656_call(relay.reshape(const_5606.astype('uint8'), [2704,])), 3)
output = relay.Tuple([call_5578,call_5602,const_5603,call_5605,const_5606,])
output2 = relay.Tuple([call_5579,call_5604,const_5603,call_5607,const_5606,])
func_5613 = relay.Function([], output)
mod['func_5613'] = func_5613
mod = relay.transform.InferType()(mod)
mutated_mod['func_5613'] = func_5613
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5613_call = mutated_mod.get_global_var('func_5613')
call_5614 = func_5613_call()
output = call_5614
func_5615 = relay.Function([], output)
mutated_mod['func_5615'] = func_5615
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4571_call = mod.get_global_var('func_4571')
func_4573_call = mutated_mod.get_global_var('func_4573')
call_5616 = relay.TupleGetItem(func_4571_call(), 0)
call_5617 = relay.TupleGetItem(func_4573_call(), 0)
output = call_5616
output2 = call_5617
func_5618 = relay.Function([], output)
mod['func_5618'] = func_5618
mod = relay.transform.InferType()(mod)
output = func_5618()
func_5619 = relay.Function([], output)
mutated_mod['func_5619'] = func_5619
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5404_call = mod.get_global_var('func_5404')
func_5406_call = mutated_mod.get_global_var('func_5406')
call_5674 = func_5404_call()
call_5675 = func_5404_call()
func_5323_call = mod.get_global_var('func_5323')
func_5325_call = mutated_mod.get_global_var('func_5325')
call_5682 = func_5323_call()
call_5683 = func_5323_call()
output = relay.Tuple([call_5674,call_5682,])
output2 = relay.Tuple([call_5675,call_5683,])
func_5698 = relay.Function([], output)
mod['func_5698'] = func_5698
mod = relay.transform.InferType()(mod)
mutated_mod['func_5698'] = func_5698
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5698_call = mutated_mod.get_global_var('func_5698')
call_5699 = func_5698_call()
output = call_5699
func_5700 = relay.Function([], output)
mutated_mod['func_5700'] = func_5700
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4571_call = mod.get_global_var('func_4571')
func_4573_call = mutated_mod.get_global_var('func_4573')
call_5784 = relay.TupleGetItem(func_4571_call(), 6)
call_5785 = relay.TupleGetItem(func_4573_call(), 6)
var_5788 = relay.var("var_5788", dtype = "float32", shape = (14, 144))#candidate|5788|(14, 144)|var|float32
bop_5789 = relay.bitwise_xor(call_5784.astype('int32'), relay.reshape(var_5788.astype('int32'), relay.shape_of(call_5784))) # shape=(14, 144)
bop_5792 = relay.bitwise_xor(call_5785.astype('int32'), relay.reshape(var_5788.astype('int32'), relay.shape_of(call_5785))) # shape=(14, 144)
uop_5806 = relay.acosh(var_5788.astype('float32')) # shape=(14, 144)
output = relay.Tuple([bop_5789,uop_5806,])
output2 = relay.Tuple([bop_5792,uop_5806,])
func_5812 = relay.Function([var_5788,], output)
mod['func_5812'] = func_5812
mod = relay.transform.InferType()(mod)
mutated_mod['func_5812'] = func_5812
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5813 = relay.var("var_5813", dtype = "float32", shape = (14, 144))#candidate|5813|(14, 144)|var|float32
func_5812_call = mutated_mod.get_global_var('func_5812')
call_5814 = func_5812_call(var_5813)
output = call_5814
func_5815 = relay.Function([var_5813], output)
mutated_mod['func_5815'] = func_5815
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5461_call = mod.get_global_var('func_5461')
func_5462_call = mutated_mod.get_global_var('func_5462')
call_5823 = relay.TupleGetItem(func_5461_call(), 0)
call_5824 = relay.TupleGetItem(func_5462_call(), 0)
output = call_5823
output2 = call_5824
func_5832 = relay.Function([], output)
mod['func_5832'] = func_5832
mod = relay.transform.InferType()(mod)
mutated_mod['func_5832'] = func_5832
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5832_call = mutated_mod.get_global_var('func_5832')
call_5833 = func_5832_call()
output = call_5833
func_5834 = relay.Function([], output)
mutated_mod['func_5834'] = func_5834
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5835 = relay.var("var_5835", dtype = "uint16", shape = ())#candidate|5835|()|var|uint16
var_5836 = relay.var("var_5836", dtype = "uint16", shape = (3, 5, 1))#candidate|5836|(3, 5, 1)|var|uint16
bop_5837 = relay.bitwise_and(var_5835.astype('uint16'), var_5836.astype('uint16')) # shape=(3, 5, 1)
output = relay.Tuple([bop_5837,])
output2 = relay.Tuple([bop_5837,])
func_5842 = relay.Function([var_5835,var_5836,], output)
mod['func_5842'] = func_5842
mod = relay.transform.InferType()(mod)
var_5843 = relay.var("var_5843", dtype = "uint16", shape = ())#candidate|5843|()|var|uint16
var_5844 = relay.var("var_5844", dtype = "uint16", shape = (3, 5, 1))#candidate|5844|(3, 5, 1)|var|uint16
output = func_5842(var_5843,var_5844,)
func_5845 = relay.Function([var_5843,var_5844,], output)
mutated_mod['func_5845'] = func_5845
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5461_call = mod.get_global_var('func_5461')
func_5462_call = mutated_mod.get_global_var('func_5462')
call_5847 = relay.TupleGetItem(func_5461_call(), 0)
call_5848 = relay.TupleGetItem(func_5462_call(), 0)
func_4059_call = mod.get_global_var('func_4059')
func_4061_call = mutated_mod.get_global_var('func_4061')
call_5849 = func_4059_call()
call_5850 = func_4059_call()
output = relay.Tuple([call_5847,call_5849,])
output2 = relay.Tuple([call_5848,call_5850,])
func_5856 = relay.Function([], output)
mod['func_5856'] = func_5856
mod = relay.transform.InferType()(mod)
mutated_mod['func_5856'] = func_5856
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5856_call = mutated_mod.get_global_var('func_5856')
call_5857 = func_5856_call()
output = call_5857
func_5858 = relay.Function([], output)
mutated_mod['func_5858'] = func_5858
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5832_call = mod.get_global_var('func_5832')
func_5834_call = mutated_mod.get_global_var('func_5834')
call_5902 = func_5832_call()
call_5903 = func_5832_call()
output = call_5902
output2 = call_5903
func_5904 = relay.Function([], output)
mod['func_5904'] = func_5904
mod = relay.transform.InferType()(mod)
mutated_mod['func_5904'] = func_5904
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5904_call = mutated_mod.get_global_var('func_5904')
call_5905 = func_5904_call()
output = call_5905
func_5906 = relay.Function([], output)
mutated_mod['func_5906'] = func_5906
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5856_call = mod.get_global_var('func_5856')
func_5858_call = mutated_mod.get_global_var('func_5858')
call_5917 = relay.TupleGetItem(func_5856_call(), 0)
call_5918 = relay.TupleGetItem(func_5858_call(), 0)
output = call_5917
output2 = call_5918
func_5921 = relay.Function([], output)
mod['func_5921'] = func_5921
mod = relay.transform.InferType()(mod)
mutated_mod['func_5921'] = func_5921
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5921_call = mutated_mod.get_global_var('func_5921')
call_5922 = func_5921_call()
output = call_5922
func_5923 = relay.Function([], output)
mutated_mod['func_5923'] = func_5923
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5927 = relay.const([[[4,1,-7,9,-6,-6],[6,-10,1,3,8,4],[-8,-5,-6,2,-9,4],[-2,7,-1,5,-2,-10],[10,7,-3,-6,-1,3],[-3,7,-7,-7,-6,-7],[7,4,-8,-2,-6,-6]],[[10,-3,2,8,10,-7],[-8,6,-9,3,-6,5],[1,-2,-6,7,2,-9],[-5,-2,-4,-4,5,10],[-4,10,-2,-5,2,-10],[-10,6,-7,8,4,7],[-1,4,-10,10,9,-5]],[[6,-2,7,-7,-8,-9],[-2,9,9,5,6,7],[-6,-1,8,-6,5,-3],[1,-1,4,8,-9,1],[-2,1,10,5,7,-10],[3,9,5,4,3,9],[-5,3,-1,-5,5,-10]],[[-4,-10,4,-7,-6,-6],[-8,1,6,-9,4,-9],[10,-9,-10,9,-5,-6],[-9,-5,-9,7,3,-1],[7,-2,-5,7,6,2],[4,-1,-10,-9,2,-5],[-7,2,-2,1,-4,10]],[[7,-5,-3,9,10,-10],[9,-1,-3,3,3,-4],[-10,-6,-9,4,-6,-8],[-7,10,-7,8,-8,-8],[-7,3,-8,-7,-1,3],[-9,-7,-5,6,10,-9],[-4,4,8,-3,4,-9]]], dtype = "uint8")#candidate|5927|(5, 7, 6)|const|uint8
var_5928 = relay.var("var_5928", dtype = "uint8", shape = (5, 7, 6))#candidate|5928|(5, 7, 6)|var|uint8
bop_5929 = relay.bitwise_or(const_5927.astype('uint8'), relay.reshape(var_5928.astype('uint8'), relay.shape_of(const_5927))) # shape=(5, 7, 6)
output = relay.Tuple([bop_5929,])
output2 = relay.Tuple([bop_5929,])
func_5940 = relay.Function([var_5928,], output)
mod['func_5940'] = func_5940
mod = relay.transform.InferType()(mod)
var_5941 = relay.var("var_5941", dtype = "uint8", shape = (5, 7, 6))#candidate|5941|(5, 7, 6)|var|uint8
output = func_5940(var_5941)
func_5942 = relay.Function([var_5941], output)
mutated_mod['func_5942'] = func_5942
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5613_call = mod.get_global_var('func_5613')
func_5615_call = mutated_mod.get_global_var('func_5615')
call_5952 = relay.TupleGetItem(func_5613_call(), 0)
call_5953 = relay.TupleGetItem(func_5615_call(), 0)
output = call_5952
output2 = call_5953
func_5972 = relay.Function([], output)
mod['func_5972'] = func_5972
mod = relay.transform.InferType()(mod)
output = func_5972()
func_5973 = relay.Function([], output)
mutated_mod['func_5973'] = func_5973
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5698_call = mod.get_global_var('func_5698')
func_5700_call = mutated_mod.get_global_var('func_5700')
call_6017 = relay.TupleGetItem(func_5698_call(), 0)
call_6018 = relay.TupleGetItem(func_5700_call(), 0)
output = relay.Tuple([call_6017,])
output2 = relay.Tuple([call_6018,])
func_6020 = relay.Function([], output)
mod['func_6020'] = func_6020
mod = relay.transform.InferType()(mod)
output = func_6020()
func_6021 = relay.Function([], output)
mutated_mod['func_6021'] = func_6021
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3922_call = mod.get_global_var('func_3922')
func_3923_call = mutated_mod.get_global_var('func_3923')
call_6031 = relay.TupleGetItem(func_3922_call(), 0)
call_6032 = relay.TupleGetItem(func_3923_call(), 0)
func_5832_call = mod.get_global_var('func_5832')
func_5834_call = mutated_mod.get_global_var('func_5834')
call_6033 = func_5832_call()
call_6034 = func_5832_call()
func_3827_call = mod.get_global_var('func_3827')
func_3829_call = mutated_mod.get_global_var('func_3829')
call_6044 = relay.TupleGetItem(func_3827_call(), 0)
call_6045 = relay.TupleGetItem(func_3829_call(), 0)
output = relay.Tuple([call_6031,call_6033,call_6044,])
output2 = relay.Tuple([call_6032,call_6034,call_6045,])
func_6052 = relay.Function([], output)
mod['func_6052'] = func_6052
mod = relay.transform.InferType()(mod)
output = func_6052()
func_6053 = relay.Function([], output)
mutated_mod['func_6053'] = func_6053
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5323_call = mod.get_global_var('func_5323')
func_5325_call = mutated_mod.get_global_var('func_5325')
call_6057 = func_5323_call()
call_6058 = func_5323_call()
output = call_6057
output2 = call_6058
func_6059 = relay.Function([], output)
mod['func_6059'] = func_6059
mod = relay.transform.InferType()(mod)
mutated_mod['func_6059'] = func_6059
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6059_call = mutated_mod.get_global_var('func_6059')
call_6060 = func_6059_call()
output = call_6060
func_6061 = relay.Function([], output)
mutated_mod['func_6061'] = func_6061
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4584_call = mod.get_global_var('func_4584')
func_4585_call = mutated_mod.get_global_var('func_4585')
call_6091 = relay.TupleGetItem(func_4584_call(), 0)
call_6092 = relay.TupleGetItem(func_4585_call(), 0)
func_3753_call = mod.get_global_var('func_3753')
func_3755_call = mutated_mod.get_global_var('func_3755')
var_6107 = relay.var("var_6107", dtype = "int32", shape = (12, 50))#candidate|6107|(12, 50)|var|int32
call_6106 = relay.TupleGetItem(func_3753_call(relay.reshape(var_6107.astype('int32'), [600,])), 2)
call_6108 = relay.TupleGetItem(func_3755_call(relay.reshape(var_6107.astype('int32'), [600,])), 2)
uop_6116 = relay.exp(var_6107.astype('float64')) # shape=(12, 50)
output = relay.Tuple([call_6091,call_6106,uop_6116,])
output2 = relay.Tuple([call_6092,call_6108,uop_6116,])
func_6126 = relay.Function([var_6107,], output)
mod['func_6126'] = func_6126
mod = relay.transform.InferType()(mod)
var_6127 = relay.var("var_6127", dtype = "int32", shape = (12, 50))#candidate|6127|(12, 50)|var|int32
output = func_6126(var_6127)
func_6128 = relay.Function([var_6127], output)
mutated_mod['func_6128'] = func_6128
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3827_call = mod.get_global_var('func_3827')
func_3829_call = mutated_mod.get_global_var('func_3829')
call_6156 = relay.TupleGetItem(func_3827_call(), 0)
call_6157 = relay.TupleGetItem(func_3829_call(), 0)
func_5618_call = mod.get_global_var('func_5618')
func_5619_call = mutated_mod.get_global_var('func_5619')
call_6158 = func_5618_call()
call_6159 = func_5618_call()
func_4279_call = mod.get_global_var('func_4279')
func_4281_call = mutated_mod.get_global_var('func_4281')
const_6163 = relay.const([[7.873674,-8.663206],[-9.169575,-0.699525],[-5.895971,-2.640879],[-6.162579,-3.213258],[-2.932432,-3.679664],[2.212973,-6.962970],[5.094792,4.095070],[1.813385,2.118620],[7.319337,6.406960],[5.524499,-7.276789],[3.936722,5.665705],[-9.330415,-8.823576],[-2.717090,9.924841],[9.886426,-1.874307],[5.134956,-9.329341],[-7.361121,0.092972],[7.247483,-5.323136],[-9.498033,3.000837],[7.484415,-3.736395],[-9.629983,6.543975],[6.676736,-4.898211],[-4.037954,4.904316],[-1.625200,-0.724807],[-9.105266,-4.546910],[0.776408,-2.723274],[-3.133555,2.933413],[-0.727245,4.960835],[-2.807943,-4.678983],[4.617641,-9.837959],[8.429650,7.748975],[5.489529,1.286876],[-0.023558,5.807656],[-7.365909,8.614037],[2.273173,-8.765424],[-4.187484,-7.664645],[-8.926346,-9.039928],[7.871909,-5.657205],[5.522379,4.553328],[6.787733,-6.780922],[-8.396253,2.789109],[3.072563,4.394663],[4.236172,8.839849]], dtype = "float64")#candidate|6163|(42, 2)|const|float64
call_6162 = relay.TupleGetItem(func_4279_call(relay.reshape(const_6163.astype('float64'), [84,])), 2)
call_6164 = relay.TupleGetItem(func_4281_call(relay.reshape(const_6163.astype('float64'), [84,])), 2)
output = relay.Tuple([call_6156,call_6158,call_6162,const_6163,])
output2 = relay.Tuple([call_6157,call_6159,call_6164,const_6163,])
func_6180 = relay.Function([], output)
mod['func_6180'] = func_6180
mod = relay.transform.InferType()(mod)
output = func_6180()
func_6181 = relay.Function([], output)
mutated_mod['func_6181'] = func_6181
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6180_call = mod.get_global_var('func_6180')
func_6181_call = mutated_mod.get_global_var('func_6181')
call_6215 = relay.TupleGetItem(func_6180_call(), 2)
call_6216 = relay.TupleGetItem(func_6181_call(), 2)
output = call_6215
output2 = call_6216
func_6220 = relay.Function([], output)
mod['func_6220'] = func_6220
mod = relay.transform.InferType()(mod)
output = func_6220()
func_6221 = relay.Function([], output)
mutated_mod['func_6221'] = func_6221
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4571_call = mod.get_global_var('func_4571')
func_4573_call = mutated_mod.get_global_var('func_4573')
call_6227 = relay.TupleGetItem(func_4571_call(), 6)
call_6228 = relay.TupleGetItem(func_4573_call(), 6)
uop_6241 = relay.acos(call_6227.astype('float32')) # shape=(14, 144)
uop_6243 = relay.acos(call_6228.astype('float32')) # shape=(14, 144)
var_6263 = relay.var("var_6263", dtype = "float32", shape = (14, 144))#candidate|6263|(14, 144)|var|float32
bop_6264 = relay.bitwise_or(uop_6241.astype('uint16'), relay.reshape(var_6263.astype('uint16'), relay.shape_of(uop_6241))) # shape=(14, 144)
bop_6267 = relay.bitwise_or(uop_6243.astype('uint16'), relay.reshape(var_6263.astype('uint16'), relay.shape_of(uop_6243))) # shape=(14, 144)
uop_6272 = relay.exp(bop_6264.astype('float32')) # shape=(14, 144)
uop_6274 = relay.exp(bop_6267.astype('float32')) # shape=(14, 144)
func_5293_call = mod.get_global_var('func_5293')
func_5296_call = mutated_mod.get_global_var('func_5296')
call_6277 = relay.TupleGetItem(func_5293_call(relay.reshape(uop_6272.astype('float32'), [2016, 1])), 0)
call_6278 = relay.TupleGetItem(func_5296_call(relay.reshape(uop_6272.astype('float32'), [2016, 1])), 0)
output = relay.Tuple([uop_6272,call_6277,])
output2 = relay.Tuple([uop_6274,call_6278,])
func_6290 = relay.Function([var_6263,], output)
mod['func_6290'] = func_6290
mod = relay.transform.InferType()(mod)
mutated_mod['func_6290'] = func_6290
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6291 = relay.var("var_6291", dtype = "float32", shape = (14, 144))#candidate|6291|(14, 144)|var|float32
func_6290_call = mutated_mod.get_global_var('func_6290')
call_6292 = func_6290_call(var_6291)
output = call_6292
func_6293 = relay.Function([var_6291], output)
mutated_mod['func_6293'] = func_6293
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6359 = relay.var("var_6359", dtype = "float64", shape = (2, 8, 10))#candidate|6359|(2, 8, 10)|var|float64
uop_6360 = relay.sigmoid(var_6359.astype('float64')) # shape=(2, 8, 10)
output = relay.Tuple([uop_6360,])
output2 = relay.Tuple([uop_6360,])
func_6365 = relay.Function([var_6359,], output)
mod['func_6365'] = func_6365
mod = relay.transform.InferType()(mod)
var_6366 = relay.var("var_6366", dtype = "float64", shape = (2, 8, 10))#candidate|6366|(2, 8, 10)|var|float64
output = func_6365(var_6366)
func_6367 = relay.Function([var_6366], output)
mutated_mod['func_6367'] = func_6367
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6380 = relay.var("var_6380", dtype = "float32", shape = (11, 4, 4))#candidate|6380|(11, 4, 4)|var|float32
uop_6381 = relay.tan(var_6380.astype('float32')) # shape=(11, 4, 4)
output = uop_6381
output2 = uop_6381
func_6383 = relay.Function([var_6380,], output)
mod['func_6383'] = func_6383
mod = relay.transform.InferType()(mod)
mutated_mod['func_6383'] = func_6383
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6384 = relay.var("var_6384", dtype = "float32", shape = (11, 4, 4))#candidate|6384|(11, 4, 4)|var|float32
func_6383_call = mutated_mod.get_global_var('func_6383')
call_6385 = func_6383_call(var_6384)
output = call_6385
func_6386 = relay.Function([var_6384], output)
mutated_mod['func_6386'] = func_6386
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3922_call = mod.get_global_var('func_3922')
func_3923_call = mutated_mod.get_global_var('func_3923')
call_6426 = relay.TupleGetItem(func_3922_call(), 0)
call_6427 = relay.TupleGetItem(func_3923_call(), 0)
output = relay.Tuple([call_6426,])
output2 = relay.Tuple([call_6427,])
func_6444 = relay.Function([], output)
mod['func_6444'] = func_6444
mod = relay.transform.InferType()(mod)
mutated_mod['func_6444'] = func_6444
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6444_call = mutated_mod.get_global_var('func_6444')
call_6445 = func_6444_call()
output = call_6445
func_6446 = relay.Function([], output)
mutated_mod['func_6446'] = func_6446
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3642_call = mod.get_global_var('func_3642')
func_3643_call = mutated_mod.get_global_var('func_3643')
call_6473 = relay.TupleGetItem(func_3642_call(), 0)
call_6474 = relay.TupleGetItem(func_3643_call(), 0)
output = call_6473
output2 = call_6474
func_6492 = relay.Function([], output)
mod['func_6492'] = func_6492
mod = relay.transform.InferType()(mod)
mutated_mod['func_6492'] = func_6492
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6492_call = mutated_mod.get_global_var('func_6492')
call_6493 = func_6492_call()
output = call_6493
func_6494 = relay.Function([], output)
mutated_mod['func_6494'] = func_6494
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6522 = relay.const([[[-6,-1,-6,5,8],[1,1,-7,5,8],[5,3,5,8,-6],[5,-9,-3,5,-10],[-4,-6,9,8,9],[-2,-10,-4,9,-6],[-8,-8,-7,-3,-1],[-7,5,9,-7,10],[3,-8,6,-9,-3],[-1,7,-9,2,-9],[6,9,-9,7,-7],[10,6,-4,-2,-9],[-9,-8,-10,3,9]],[[-7,9,-6,4,4],[10,-3,4,9,2],[2,10,2,-7,4],[-8,-2,-6,-5,4],[6,-3,-8,-8,-2],[-9,-4,4,-9,-2],[8,-3,-6,1,-3],[-1,6,-8,3,-5],[6,1,1,7,-8],[-2,-8,-9,5,-6],[-2,7,-4,-4,9],[-4,-3,5,2,-5],[-1,-9,1,-3,-5]],[[-7,9,4,-7,10],[10,-10,-1,-7,9],[5,9,8,1,8],[-4,2,-9,7,-7],[-1,-3,7,6,-8],[6,-6,9,-6,-7],[4,-1,5,5,5],[8,-10,-7,-6,-3],[-1,-10,-5,-10,7],[5,-9,10,-6,7],[-8,9,8,4,-2],[-8,7,7,7,3],[5,7,-6,-1,1]],[[-6,-4,8,-1,-6],[1,-6,-4,-10,-8],[-4,3,-8,-8,3],[-6,-10,-6,-2,1],[9,-2,10,-8,6],[5,1,-1,9,8],[1,-3,-4,-1,5],[4,6,9,-3,-8],[4,-9,3,4,9],[4,-7,5,3,10],[8,1,2,-1,10],[-4,-5,9,-2,2],[6,3,2,-9,-4]],[[4,-4,7,7,-1],[-9,1,-7,-6,3],[10,3,-7,1,-9],[-6,6,-9,4,-3],[3,1,10,4,4],[-1,1,8,-8,-5],[-6,1,8,7,4],[-8,-3,-2,-6,-8],[-4,-7,-4,2,-5],[-8,-7,-3,9,-9],[-1,1,-8,7,-7],[-4,-6,7,-7,-10],[5,3,9,7,7]],[[2,-2,2,-5,-2],[5,-5,-9,1,-1],[-10,2,-8,-1,-8],[8,-6,2,8,10],[10,-10,-8,-9,-6],[-3,9,-10,-6,-2],[1,6,-10,-9,6],[2,5,-4,2,-4],[-4,-7,-2,-9,-9],[-7,-1,-10,-1,-3],[8,-4,-7,6,2],[10,-6,-8,-5,9],[8,-6,8,1,-7]],[[-6,-10,-6,9,-10],[1,-8,8,-7,4],[9,-1,2,3,9],[-8,2,7,8,-1],[8,10,-9,3,1],[2,-7,5,2,-3],[-7,-8,-2,7,5],[-8,-10,-1,5,6],[9,-8,-3,-8,-2],[-8,3,-7,2,-4],[-4,10,-9,4,2],[3,-10,-10,3,-5],[-8,-3,-10,-5,-6]],[[7,-9,3,-7,3],[-9,-3,-9,-9,10],[7,-9,-8,-3,-1],[-9,-7,7,-6,9],[6,-10,-4,-1,-1],[-8,-8,1,6,-8],[-10,-7,-5,9,9],[-3,-5,-3,1,-1],[-6,1,6,1,-5],[-10,5,-4,-10,-2],[-2,-5,9,3,3],[-10,-4,4,-2,-3],[3,2,1,-8,2]],[[1,6,-8,-3,5],[-6,4,6,10,-4],[-5,-8,-4,-6,9],[2,-9,-7,3,9],[-5,-3,-4,8,8],[-9,-8,-3,-6,-5],[-4,-7,7,-1,4],[-8,-4,-10,1,4],[-2,6,2,4,-8],[-4,-8,-7,-7,-5],[8,-1,-6,3,-1],[-1,-2,4,-4,-3],[-9,-5,10,-2,-2]],[[-9,2,-3,1,8],[-2,4,5,7,6],[4,-7,-2,2,-3],[5,-5,1,7,-1],[-1,-3,-7,5,-10],[4,-8,-4,7,8],[-10,-3,10,-10,-4],[-4,-6,-4,-7,-8],[1,2,4,-2,2],[2,-3,-5,-9,-1],[-10,9,-4,-10,1],[-8,4,2,6,9],[-5,7,8,-2,9]],[[-1,8,4,3,3],[-5,-6,2,7,3],[-3,-10,6,-4,-6],[-2,1,-9,4,-2],[5,7,-6,-9,-7],[10,-3,-10,-10,-7],[-9,-3,9,-7,3],[-9,9,-10,-6,-10],[3,3,-10,-3,9],[-7,9,9,4,-10],[-7,5,-6,1,-4],[-5,8,-3,10,1],[5,8,-9,-3,-2]],[[10,-1,-5,10,1],[4,-10,-1,-5,10],[2,3,1,-6,-5],[-7,-10,-9,-9,9],[-2,-3,9,9,7],[-9,5,9,-4,-2],[3,-3,2,-8,-1],[-9,3,-9,-6,-6],[8,-3,9,-10,-7],[9,4,5,-4,-4],[-1,9,-5,-6,-9],[-5,2,-9,-8,-2],[-3,-6,-3,-2,-3]],[[3,9,8,4,-4],[-10,7,5,-1,-7],[9,-5,7,-6,-6],[-3,-5,-3,-6,-10],[-8,-9,2,-3,10],[-7,-9,6,8,-3],[2,-5,10,-3,5],[-7,4,1,4,9],[3,-3,-6,-8,-2],[3,1,-3,6,-7],[7,-5,4,7,8],[-1,3,5,4,8],[-8,-10,-6,10,-6]]], dtype = "int8")#candidate|6522|(13, 13, 5)|const|int8
var_6523 = relay.var("var_6523", dtype = "int8", shape = (13, 13, 5))#candidate|6523|(13, 13, 5)|var|int8
bop_6524 = relay.multiply(const_6522.astype('int8'), relay.reshape(var_6523.astype('int8'), relay.shape_of(const_6522))) # shape=(13, 13, 5)
func_3214_call = mod.get_global_var('func_3214')
func_3217_call = mutated_mod.get_global_var('func_3217')
var_6533 = relay.var("var_6533", dtype = "int32", shape = (2, 300))#candidate|6533|(2, 300)|var|int32
call_6532 = relay.TupleGetItem(func_3214_call(relay.reshape(var_6533.astype('int32'), [10, 15, 4])), 1)
call_6534 = relay.TupleGetItem(func_3217_call(relay.reshape(var_6533.astype('int32'), [10, 15, 4])), 1)
output = relay.Tuple([bop_6524,call_6532,var_6533,])
output2 = relay.Tuple([bop_6524,call_6534,var_6533,])
func_6543 = relay.Function([var_6523,var_6533,], output)
mod['func_6543'] = func_6543
mod = relay.transform.InferType()(mod)
var_6544 = relay.var("var_6544", dtype = "int8", shape = (13, 13, 5))#candidate|6544|(13, 13, 5)|var|int8
var_6545 = relay.var("var_6545", dtype = "int32", shape = (2, 300))#candidate|6545|(2, 300)|var|int32
output = func_6543(var_6544,var_6545,)
func_6546 = relay.Function([var_6544,var_6545,], output)
mutated_mod['func_6546'] = func_6546
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4883_call = mod.get_global_var('func_4883')
func_4885_call = mutated_mod.get_global_var('func_4885')
call_6572 = relay.TupleGetItem(func_4883_call(), 2)
call_6573 = relay.TupleGetItem(func_4885_call(), 2)
uop_6574 = relay.sinh(call_6572.astype('float64')) # shape=(1, 600)
uop_6576 = relay.sinh(call_6573.astype('float64')) # shape=(1, 600)
uop_6583 = relay.acos(uop_6574.astype('float64')) # shape=(1, 600)
uop_6585 = relay.acos(uop_6576.astype('float64')) # shape=(1, 600)
uop_6591 = relay.sin(uop_6583.astype('float64')) # shape=(1, 600)
uop_6593 = relay.sin(uop_6585.astype('float64')) # shape=(1, 600)
uop_6595 = relay.erf(uop_6583.astype('float64')) # shape=(1, 600)
uop_6597 = relay.erf(uop_6585.astype('float64')) # shape=(1, 600)
func_2910_call = mod.get_global_var('func_2910')
func_2913_call = mutated_mod.get_global_var('func_2913')
const_6608 = relay.const([-8.752551,-4.776083,-9.676757,9.236120,-8.908483,-0.307711,8.216886,-0.703440,7.407638,-2.361384,-5.079733,-0.088712,8.627678,-5.873803,-0.976589,-5.717133,-0.877656,6.749906,3.717812,-5.808601,-8.242730,3.944995,-3.901067,9.744369,5.220259,8.786866,-4.683258,-4.121062,6.899669,-0.186958,-0.033183,-5.190789,-6.915208,6.729465,-6.373322,4.233242,-9.652145,3.391045,-2.784943,-7.029160,-6.980193,0.886777,0.926462,-3.035297,-5.989234,-4.906000,6.339276,-8.526023,-8.282400,2.587871,5.691131,-2.230978,-4.001271,-5.119316,-4.070727,-4.872235,3.353835,8.078670,4.289414,3.292446,2.115182,-7.867233,-4.971182,-4.120094,-9.245865,5.247431,-6.025476,-3.480417,0.325227,9.446931,1.618338,-6.342786,9.102442,-3.083465,5.851924,-9.194177,1.374155,-9.257506,0.732991,2.951181,-4.979478,-1.719004,-8.803429,7.158568,0.643575,5.769209,9.448020,2.979811,-9.127071,6.149250,6.567965,-8.588454,4.652075,-0.633891,0.324520,-7.326050,2.712153,-2.280790,7.512801,9.620174,-8.981158,-7.853183,9.855493,-2.639884,7.020878,6.653948,9.430754,7.143911,-1.767652,-0.737447,2.514589,-0.619068], dtype = "float32")#candidate|6608|(112,)|const|float32
call_6607 = func_2910_call(relay.reshape(const_6608.astype('float32'), [7, 8, 2]))
call_6609 = func_2910_call(relay.reshape(const_6608.astype('float32'), [7, 8, 2]))
uop_6611 = relay.exp(uop_6595.astype('float32')) # shape=(1, 600)
uop_6613 = relay.exp(uop_6597.astype('float32')) # shape=(1, 600)
output = relay.Tuple([uop_6591,call_6607,const_6608,uop_6611,])
output2 = relay.Tuple([uop_6593,call_6609,const_6608,uop_6613,])
func_6640 = relay.Function([], output)
mod['func_6640'] = func_6640
mod = relay.transform.InferType()(mod)
mutated_mod['func_6640'] = func_6640
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6640_call = mutated_mod.get_global_var('func_6640')
call_6641 = func_6640_call()
output = call_6641
func_6642 = relay.Function([], output)
mutated_mod['func_6642'] = func_6642
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6680 = relay.const(-2.729082, dtype = "float32")#candidate|6680|()|const|float32
var_6681 = relay.var("var_6681", dtype = "float32", shape = (16, 1, 15))#candidate|6681|(16, 1, 15)|var|float32
bop_6682 = relay.power(const_6680.astype('float32'), var_6681.astype('float32')) # shape=(16, 1, 15)
bop_6689 = relay.logical_or(var_6681.astype('bool'), relay.reshape(bop_6682.astype('bool'), relay.shape_of(var_6681))) # shape=(16, 1, 15)
uop_6693 = relay.sigmoid(bop_6682.astype('float64')) # shape=(16, 1, 15)
output = relay.Tuple([bop_6689,uop_6693,])
output2 = relay.Tuple([bop_6689,uop_6693,])
func_6696 = relay.Function([var_6681,], output)
mod['func_6696'] = func_6696
mod = relay.transform.InferType()(mod)
var_6697 = relay.var("var_6697", dtype = "float32", shape = (16, 1, 15))#candidate|6697|(16, 1, 15)|var|float32
output = func_6696(var_6697)
func_6698 = relay.Function([var_6697], output)
mutated_mod['func_6698'] = func_6698
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6492_call = mod.get_global_var('func_6492')
func_6494_call = mutated_mod.get_global_var('func_6494')
call_6711 = func_6492_call()
call_6712 = func_6492_call()
func_4308_call = mod.get_global_var('func_4308')
func_4310_call = mutated_mod.get_global_var('func_4310')
var_6726 = relay.var("var_6726", dtype = "uint32", shape = (4, 140))#candidate|6726|(4, 140)|var|uint32
call_6725 = relay.TupleGetItem(func_4308_call(relay.reshape(var_6726.astype('uint32'), [280, 2])), 1)
call_6727 = relay.TupleGetItem(func_4310_call(relay.reshape(var_6726.astype('uint32'), [280, 2])), 1)
func_3809_call = mod.get_global_var('func_3809')
func_3810_call = mutated_mod.get_global_var('func_3810')
call_6744 = relay.TupleGetItem(func_3809_call(), 0)
call_6745 = relay.TupleGetItem(func_3810_call(), 0)
func_4388_call = mod.get_global_var('func_4388')
func_4392_call = mutated_mod.get_global_var('func_4392')
var_6760 = relay.var("var_6760", dtype = "uint8", shape = (2704,))#candidate|6760|(2704,)|var|uint8
var_6761 = relay.var("var_6761", dtype = "float32", shape = (112,))#candidate|6761|(112,)|var|float32
call_6759 = relay.TupleGetItem(func_4388_call(relay.reshape(var_6760.astype('uint8'), [1, 2704]), relay.reshape(var_6761.astype('float32'), [4, 28]), ), 2)
call_6762 = relay.TupleGetItem(func_4392_call(relay.reshape(var_6760.astype('uint8'), [1, 2704]), relay.reshape(var_6761.astype('float32'), [4, 28]), ), 2)
func_3156_call = mod.get_global_var('func_3156')
func_3161_call = mutated_mod.get_global_var('func_3161')
var_6764 = relay.var("var_6764", dtype = "int64", shape = (260,))#candidate|6764|(260,)|var|int64
var_6765 = relay.var("var_6765", dtype = "int64", shape = (2, 896))#candidate|6765|(2, 896)|var|int64
var_6766 = relay.var("var_6766", dtype = "bool", shape = (12,))#candidate|6766|(12,)|var|bool
call_6763 = relay.TupleGetItem(func_3156_call(relay.reshape(var_6764.astype('int64'), [2, 10, 13]), relay.reshape(var_6765.astype('int64'), [1, 1792]), relay.reshape(var_6766.astype('bool'), [12, 1]), ), 3)
call_6767 = relay.TupleGetItem(func_3161_call(relay.reshape(var_6764.astype('int64'), [2, 10, 13]), relay.reshape(var_6765.astype('int64'), [1, 1792]), relay.reshape(var_6766.astype('bool'), [12, 1]), ), 3)
func_6180_call = mod.get_global_var('func_6180')
func_6181_call = mutated_mod.get_global_var('func_6181')
call_6768 = relay.TupleGetItem(func_6180_call(), 2)
call_6769 = relay.TupleGetItem(func_6181_call(), 2)
uop_6799 = relay.sqrt(var_6760.astype('float32')) # shape=(2704,)
output = relay.Tuple([call_6711,call_6725,var_6726,call_6744,call_6759,var_6761,call_6763,var_6764,var_6765,var_6766,call_6768,uop_6799,])
output2 = relay.Tuple([call_6712,call_6727,var_6726,call_6745,call_6762,var_6761,call_6767,var_6764,var_6765,var_6766,call_6769,uop_6799,])
func_6814 = relay.Function([var_6726,var_6760,var_6761,var_6764,var_6765,var_6766,], output)
mod['func_6814'] = func_6814
mod = relay.transform.InferType()(mod)
mutated_mod['func_6814'] = func_6814
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6814_call = mutated_mod.get_global_var('func_6814')
var_6816 = relay.var("var_6816", dtype = "uint32", shape = (4, 140))#candidate|6816|(4, 140)|var|uint32
var_6817 = relay.var("var_6817", dtype = "uint8", shape = (2704,))#candidate|6817|(2704,)|var|uint8
var_6818 = relay.var("var_6818", dtype = "float32", shape = (112,))#candidate|6818|(112,)|var|float32
var_6819 = relay.var("var_6819", dtype = "int64", shape = (260,))#candidate|6819|(260,)|var|int64
var_6820 = relay.var("var_6820", dtype = "int64", shape = (2, 896))#candidate|6820|(2, 896)|var|int64
var_6821 = relay.var("var_6821", dtype = "bool", shape = (12,))#candidate|6821|(12,)|var|bool
call_6815 = func_6814_call(var_6816,var_6817,var_6818,var_6819,var_6820,var_6821,)
output = call_6815
func_6822 = relay.Function([var_6816,var_6817,var_6818,var_6819,var_6820,var_6821,], output)
mutated_mod['func_6822'] = func_6822
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3809_call = mod.get_global_var('func_3809')
func_3810_call = mutated_mod.get_global_var('func_3810')
call_6824 = relay.TupleGetItem(func_3809_call(), 0)
call_6825 = relay.TupleGetItem(func_3810_call(), 0)
output = call_6824
output2 = call_6825
func_6851 = relay.Function([], output)
mod['func_6851'] = func_6851
mod = relay.transform.InferType()(mod)
output = func_6851()
func_6852 = relay.Function([], output)
mutated_mod['func_6852'] = func_6852
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5618_call = mod.get_global_var('func_5618')
func_5619_call = mutated_mod.get_global_var('func_5619')
call_6853 = func_5618_call()
call_6854 = func_5618_call()
func_6640_call = mod.get_global_var('func_6640')
func_6642_call = mutated_mod.get_global_var('func_6642')
call_6905 = relay.TupleGetItem(func_6640_call(), 2)
call_6906 = relay.TupleGetItem(func_6642_call(), 2)
func_3008_call = mod.get_global_var('func_3008')
func_3010_call = mutated_mod.get_global_var('func_3010')
const_6934 = relay.const([8,-1,-7,9,-6,-8,1,-7,-2,-4,8,5,-3,-1,8,-6,-1,-9,3,-2,-3,7,8,-8,9,-9,4,-8,-6,-1,-8,3,5,-8,3,7,-10,-9,-8,-3,9,-5,5,9,4,-8,-1,10,4,-4,9,1,10,10,-9,7,2,-10,-5,2,2,-2,10,1,-1,1,10,9,-3,8,-1,-1,-8,2,3,5,-4,8,-10,-8,-6,2,2,-6,10,9,10,4,3,5,2,9,8,9,-10,2,-7,-2,6,4,-1,-9,4,-10,1,-1,7,8,1,5,4,5,-10,2,4,-3,-10,-7,6,-9,5,10,2,-9,-5,4,2,3,-8,-9,1,-7,-4,3,-2,-7,-4,8,6,1,-2,1,6,-5,8,-7,5,10,-8,9,9,6,-4,-1,4,2,-9,-7,6,9,7,5,-10,1,-9,-8,8,-2,-10,5,-5,7,9,-8,7,10,-3,-6,-7,-1,-9,5,-2,-4,-9,4,7,9,5,-10,5,8,3,9,3,8,-8,3,-9,-10,-7,4,6,-7,-1,5,7,1,9,3,1,-6,-6,7,-6,-6,1,-5,5,8,-1,9,-8,9,2,7,-3,2,-2,5,-6,-10,-2,4,9,3,-4,-9,5,-10,-7,-2,-2,10,-5], dtype = "uint64")#candidate|6934|(245,)|const|uint64
call_6933 = func_3008_call(relay.reshape(const_6934.astype('uint64'), [7, 5, 7]))
call_6935 = func_3008_call(relay.reshape(const_6934.astype('uint64'), [7, 5, 7]))
output = relay.Tuple([call_6853,call_6905,call_6933,const_6934,])
output2 = relay.Tuple([call_6854,call_6906,call_6935,const_6934,])
func_6938 = relay.Function([], output)
mod['func_6938'] = func_6938
mod = relay.transform.InferType()(mod)
output = func_6938()
func_6939 = relay.Function([], output)
mutated_mod['func_6939'] = func_6939
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4238_call = mod.get_global_var('func_4238')
func_4240_call = mutated_mod.get_global_var('func_4240')
call_6940 = func_4238_call()
call_6941 = func_4238_call()
output = relay.Tuple([call_6940,])
output2 = relay.Tuple([call_6941,])
func_6943 = relay.Function([], output)
mod['func_6943'] = func_6943
mod = relay.transform.InferType()(mod)
output = func_6943()
func_6944 = relay.Function([], output)
mutated_mod['func_6944'] = func_6944
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6938_call = mod.get_global_var('func_6938')
func_6939_call = mutated_mod.get_global_var('func_6939')
call_6950 = relay.TupleGetItem(func_6938_call(), 0)
call_6951 = relay.TupleGetItem(func_6939_call(), 0)
func_5259_call = mod.get_global_var('func_5259')
func_5260_call = mutated_mod.get_global_var('func_5260')
call_6959 = relay.TupleGetItem(func_5259_call(), 1)
call_6960 = relay.TupleGetItem(func_5260_call(), 1)
var_6963 = relay.var("var_6963", dtype = "float64", shape = (2, 3, 14))#candidate|6963|(2, 3, 14)|var|float64
bop_6964 = relay.logical_or(call_6959.astype('bool'), relay.reshape(var_6963.astype('bool'), relay.shape_of(call_6959))) # shape=(2, 3, 14)
bop_6967 = relay.logical_or(call_6960.astype('bool'), relay.reshape(var_6963.astype('bool'), relay.shape_of(call_6960))) # shape=(2, 3, 14)
output = relay.Tuple([call_6950,bop_6964,])
output2 = relay.Tuple([call_6951,bop_6967,])
func_6976 = relay.Function([var_6963,], output)
mod['func_6976'] = func_6976
mod = relay.transform.InferType()(mod)
mutated_mod['func_6976'] = func_6976
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6977 = relay.var("var_6977", dtype = "float64", shape = (2, 3, 14))#candidate|6977|(2, 3, 14)|var|float64
func_6976_call = mutated_mod.get_global_var('func_6976')
call_6978 = func_6976_call(var_6977)
output = call_6978
func_6979 = relay.Function([var_6977], output)
mutated_mod['func_6979'] = func_6979
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3809_call = mod.get_global_var('func_3809')
func_3810_call = mutated_mod.get_global_var('func_3810')
call_7029 = relay.TupleGetItem(func_3809_call(), 0)
call_7030 = relay.TupleGetItem(func_3810_call(), 0)
uop_7033 = relay.rsqrt(call_7029.astype('float64')) # shape=(7, 16, 12)
uop_7035 = relay.rsqrt(call_7030.astype('float64')) # shape=(7, 16, 12)
output = uop_7033
output2 = uop_7035
func_7060 = relay.Function([], output)
mod['func_7060'] = func_7060
mod = relay.transform.InferType()(mod)
output = func_7060()
func_7061 = relay.Function([], output)
mutated_mod['func_7061'] = func_7061
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7163 = relay.var("var_7163", dtype = "float32", shape = (7, 13, 4))#candidate|7163|(7, 13, 4)|var|float32
uop_7164 = relay.sqrt(var_7163.astype('float32')) # shape=(7, 13, 4)
output = uop_7164
output2 = uop_7164
func_7167 = relay.Function([var_7163,], output)
mod['func_7167'] = func_7167
mod = relay.transform.InferType()(mod)
var_7168 = relay.var("var_7168", dtype = "float32", shape = (7, 13, 4))#candidate|7168|(7, 13, 4)|var|float32
output = func_7167(var_7168)
func_7169 = relay.Function([var_7168], output)
mutated_mod['func_7169'] = func_7169
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6059_call = mod.get_global_var('func_6059')
func_6061_call = mutated_mod.get_global_var('func_6061')
call_7215 = func_6059_call()
call_7216 = func_6059_call()
output = relay.Tuple([call_7215,])
output2 = relay.Tuple([call_7216,])
func_7231 = relay.Function([], output)
mod['func_7231'] = func_7231
mod = relay.transform.InferType()(mod)
output = func_7231()
func_7232 = relay.Function([], output)
mutated_mod['func_7232'] = func_7232
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4238_call = mod.get_global_var('func_4238')
func_4240_call = mutated_mod.get_global_var('func_4240')
call_7251 = func_4238_call()
call_7252 = func_4238_call()
output = relay.Tuple([call_7251,])
output2 = relay.Tuple([call_7252,])
func_7257 = relay.Function([], output)
mod['func_7257'] = func_7257
mod = relay.transform.InferType()(mod)
mutated_mod['func_7257'] = func_7257
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7257_call = mutated_mod.get_global_var('func_7257')
call_7258 = func_7257_call()
output = call_7258
func_7259 = relay.Function([], output)
mutated_mod['func_7259'] = func_7259
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7260 = relay.var("var_7260", dtype = "float64", shape = ())#candidate|7260|()|var|float64
var_7261 = relay.var("var_7261", dtype = "float64", shape = (11, 14, 8))#candidate|7261|(11, 14, 8)|var|float64
bop_7262 = relay.divide(var_7260.astype('float64'), var_7261.astype('float64')) # shape=(11, 14, 8)
func_4059_call = mod.get_global_var('func_4059')
func_4061_call = mutated_mod.get_global_var('func_4061')
call_7288 = func_4059_call()
call_7289 = func_4059_call()
output = relay.Tuple([bop_7262,call_7288,])
output2 = relay.Tuple([bop_7262,call_7289,])
func_7305 = relay.Function([var_7260,var_7261,], output)
mod['func_7305'] = func_7305
mod = relay.transform.InferType()(mod)
mutated_mod['func_7305'] = func_7305
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7305_call = mutated_mod.get_global_var('func_7305')
var_7307 = relay.var("var_7307", dtype = "float64", shape = ())#candidate|7307|()|var|float64
var_7308 = relay.var("var_7308", dtype = "float64", shape = (11, 14, 8))#candidate|7308|(11, 14, 8)|var|float64
call_7306 = func_7305_call(var_7307,var_7308,)
output = call_7306
func_7309 = relay.Function([var_7307,var_7308,], output)
mutated_mod['func_7309'] = func_7309
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6492_call = mod.get_global_var('func_6492')
func_6494_call = mutated_mod.get_global_var('func_6494')
call_7374 = func_6492_call()
call_7375 = func_6492_call()
output = call_7374
output2 = call_7375
func_7385 = relay.Function([], output)
mod['func_7385'] = func_7385
mod = relay.transform.InferType()(mod)
output = func_7385()
func_7386 = relay.Function([], output)
mutated_mod['func_7386'] = func_7386
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7257_call = mod.get_global_var('func_7257')
func_7259_call = mutated_mod.get_global_var('func_7259')
call_7469 = relay.TupleGetItem(func_7257_call(), 0)
call_7470 = relay.TupleGetItem(func_7259_call(), 0)
func_4883_call = mod.get_global_var('func_4883')
func_4885_call = mutated_mod.get_global_var('func_4885')
call_7478 = relay.TupleGetItem(func_4883_call(), 1)
call_7479 = relay.TupleGetItem(func_4885_call(), 1)
output = relay.Tuple([call_7469,call_7478,])
output2 = relay.Tuple([call_7470,call_7479,])
func_7480 = relay.Function([], output)
mod['func_7480'] = func_7480
mod = relay.transform.InferType()(mod)
mutated_mod['func_7480'] = func_7480
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7480_call = mutated_mod.get_global_var('func_7480')
call_7481 = func_7480_call()
output = call_7481
func_7482 = relay.Function([], output)
mutated_mod['func_7482'] = func_7482
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6943_call = mod.get_global_var('func_6943')
func_6944_call = mutated_mod.get_global_var('func_6944')
call_7528 = relay.TupleGetItem(func_6943_call(), 0)
call_7529 = relay.TupleGetItem(func_6944_call(), 0)
output = relay.Tuple([call_7528,])
output2 = relay.Tuple([call_7529,])
func_7542 = relay.Function([], output)
mod['func_7542'] = func_7542
mod = relay.transform.InferType()(mod)
output = func_7542()
func_7543 = relay.Function([], output)
mutated_mod['func_7543'] = func_7543
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6851_call = mod.get_global_var('func_6851')
func_6852_call = mutated_mod.get_global_var('func_6852')
call_7563 = func_6851_call()
call_7564 = func_6851_call()
func_1977_call = mod.get_global_var('func_1977')
func_1980_call = mutated_mod.get_global_var('func_1980')
const_7590 = relay.const([-1,-7,-7,-9,9,6,2,1,7,2,6,-7,5,-3,10,-10,8,4,-8,-10,-6,3,8,-9,1,6,7,6,-9,-8,2,-9,-9,-6,8,4,-4,10,-2,-9,-2,-8,10,-2,2,-7,-10,-7,-9,-6,10,-9,-6,8,-9,10,-2,2,-2,-1,4,3,4,5,-4,10,-8,10,-9,-5,-7,-2,3,3,8,-4,-3,8,-8,3,-1,-7,2,-6,-8,-9,-6,-4,-5,-8,4,-7,10,6,-10,9,-10,2,-4,2,1,-6,4,-8,8,4,-8,9,-8,-6,-2,10,1,-5,-2,6,-10,-2,4,-5,-8,4,-2,5,-6,8,8,-1,2,6,2,-9,6,-9,5,-1,-3,-2,8,4,-10,3,2,7,-9,-8,-6,-3,2,1,4,-10,-8,3,-10,1,1,8,-7,5,-9,-5,2,9,10,9,3,2,-4,9,-1,-3,-2,4,-9,5,2,5,8,7,-4,-1,-8,10,9,3,10,2,1,3,-7,-8,-8,4,-6,3,7,-9,-8,-4,-10,9,-7,6,-9,5,-7,6,7,9,-10,5,8,-2,-5,-5,7,7,-5,9,-9,-9,-9,-2,-4,2,-5,3,1,2,-4,-10,-9,3,7,-7,8,5,-10,6,7,-9,-4,-6,8,10,-4,-10,-7,-8,-7,-3,2,4,2,-9,-7,3,-3,-8,-8,-2,9,7,9,2,-4,-10,-2,10,4,5,10,-5,-9,-3,-1,9,-8,-6,6,2,-3,-4,-9,-9,6,6,-1,6,-4,-9,3,-5,-6,10,10,-10,8,-8,-2,10,10,-1,-9,-3,7,9,9,5,-8,-7,-8,-1,-3,-3,-3,-3,1,6,-3,4,-10,-10,-9,-6,1,-5,-10,-7,-3,-10,-3,9,-6,-5,-5,-9,-4,-6,5,1,-5,6,3,2,2,-2,4,-1,10,1,7,-10,10,-5,8,-2,-4,-10,-10,3,-2,-8,-10,-7,5,6,8,4,-2,5,-6,-2,-3,-9,3,-4,-9,-3,9,9,-10,7,-1,-5,1,10,5,10,-4,-1,-1,2,-5,-10,7,-2,6,-2,-2,7,-9,1,-1,-3,1,10,9,1,8,-10,-3,-9,-2,6,-10,-7,2,-4,-10,5,-1,3,-8,-5,8,-9,-10,1,-1,-5,-10,9,-2,-2,-10,-6,-2,2,-5,-4,4,5,-4,-7,-1,-6,-7,-10,10,3,-9,-2,8,-2,-2,-8,-2,4,9,-2,4,-1,5,-1,-5,4,3,-8,-1,-8,7,-3,8,6,9,-10,-6,-3,6,5,-8,7,6,-6,6,-1,-9,1,-2,-7,-6,1,9,2,-9,7,7,-3,-1,-9,-5,1,3,-3,10,-5,10,8,-1,5,7,-1,9,-7,-5,1,-5,3,-4,-4,-8,-3,-6,-8,-1,-8,8,-5,3,1,-8,-7,-3,-4,9,-3,8,5,-7,10,-9,-8,-8,-8,-5,-3,9,8,2,-3,2,8,-4,-2,10,-8,-10,8,9,3,2,9,-5,7,10,8,8,10,1,-2,3,9,-6,5,2,-1,5,-10,-8,-8,7,-8,4,-4,9,-5,5,8,-3,-9,3,3,-2,8,8,-6,-4,9,-4,2,-8,-6,4,-6,-10,-4,-7,-1,-10,6,-9,-4,-1,-2,5,-6,4,7,9,5,-10,-2,-7,-3,6,-4,6,-9,-8,-1,6,7,-1,-5,10,10,10,5,7,-2,-1,-7,4,-3,-6,7,-2,-9,9,-5,-6,8,-9,1,3,8,-2,1,10,10,8,5,2,-5,9,-9,-5,9,10,-9,-5,-8,-1,-3,-3,-6,-8,1,6,-2,-5,8,-8,1,8,4,6,-8,-9,9,-4,4,-9,-4,2,10,7,-7,-6,6,10,-7,9,5,-8,1,1,-8,10,-5,-9,8,-4,2,5,6,-7,-10,-10,-4,1,-4,1,-5,5,-3,-7,-10,-8,-3,-2,6,3,4,3,6,7,8,-10,-9,1,9,5,-8,-2,3,3,-3,-5,2,7,4,5,-2,-3,2,-4,-1,-10,9,-4,-8,-2,-3,-8,-5,-2,10,10,-4,4,-4,-7,-5,-8,1,-7,-6,7,-5,2,-1,10,-4,5,1,4,-8,-4,7,9,1,6,6,5,-2,3,5,-7,6,-5,-1,-4,-1,4,-10,8,1,-9,9,10,4,5,1,-6,-3,-3,1,5,-8,2,2,-9,5,-1,3,6,-7,5,-4,-2,-4,-3,-4,9,-5,-10,-10,-3,-9,1,-6,-9,9,-2,5,-2,-10,-5,1,-6,4,7,-7,1,5,-5,-9,5,-8,-3,-10,3,-9,-4,-2,-1,8,-8,-8,-8,1,3,8,9,6,1,8,8,2,-10,-4,-9,-8,-7,8,-7,-1,-8,-10,-4,-1,-2,9,-6,4,5,6,-2,3,-9,5,9,-8,-6,5,5,-7,7,-9,-6,1,-2,-5,1,2,-8,-8,6,5,-6,-1,8,-10,-1,8,-3,-1,5,-7,-6,8,9,-3,4,4,2,-1,-3,-7,-1,4,-3,-8,2,7,-6,4,-5,-10,-8,-8,-2,-3,9,9,-5,3,9,8,-7,-1,-2,-10,-3,7,-7,-4,-4,-3,-6,-5,5,-9,-9,8,-4,9,-4,-4,-9,10,3,-4,2,-2,-10,-9,6,1,-5,-9,6,4,9,8,-8,-4,4,-10,5,-5,10,10,-2,-1,-10,5,-10,-7,-8,7,-5,8,8,6,-1,-8,4,9,1,-4,-10,-8,-9,-1,1,-2,-8,-6,8,10,4,2,-6,-6,1,-7,-9,1,-3,5,-10,-10,9,7,-9,-9,-6,3,-4,-10,-10,-5,-3,7,1,-10,8,1,8,-7,6,-2,-8,6,-5,-6,5,-2,-8,-6,10,9,-8,7,8,-4,7,9,-2,-7,3,-2,3,-9,-4,9,3,-1,-8,-10,2,3,2,5,10,1,-5,4,-6,10,-9,3,5,-6,4,-9,2,6,-5,9,4,9,-2,9,7,9,8,-10,8,6,-2,10,9,7,10,-9,6,6,-2,-8,-6,-5,-1,-9,-8,2,-2,-3,2,-6,4,7,-5,7,-1,6,-2,-4,-3,3,-8,3,-9,4,4,2,-7,-7,-3,10,9,-1,-7,5,8,3,-3,7,-1,-1,-8,3,3,8,6,2,-3,8,8,10,-9,1,9,4,-6,5,2,-1,-1,3,-8,3,-9,-3,-4,4,-6,-7,-2,5,8,6,-9,6,-8,7,5,-9,-3,-1,7,-4,2,-8,-4,6,4,-1,1,-4,6,6,5,6,-8,-7,-4,-10,2,-3,-2,8,1,2,7,-10,9,-6,9,-4,-9,-4,2,1,3,-2,-3,2,2,-3,-9,-3,6,5,-1,6,10,5,5,7,2,-2,2,6,-5,-4,-3,-5,8,8,-6,9,6,7,-2,7,4,8,3,-9,-4,-3,1,7,7,-9,10,9,6,5,-10,1,-4,-9,4,5,10,6,-5,3,8,5,9,-4,-9,2,-3,-3,-3,-6,-2,-4,1,6,-3,-8,-8,-9,-8,-4,1,-8,3,3,-4,1,-10,-8,3,6,2,8,-10,1,-9,-7,-2,-9,4,1,3,-6,4,-5,-8,6,-9,-2,-1,-7,9,-3,6,-8,-5,10,10,2,-10,3,-10,-1,-3,-7,7,5,7,9,-1,8,5,-6,4,8,-5,-5,2,-5,9,9,8,-4,-1,2,9,10,8,10,3,7,1,-4,-9,9,-1,-6,4,5,2,-9,-5,-6,4,6,-3,5,6,10,8,-1,-10,9,-6,9,-2,-10,9,2,1,-1,1,-10,-5,10,10,4,10,-5,-8,6,-3,8,2,5,8,-8,10,-5,10,8,-9,-1,-6,7,1,3,-10,5,-3,-5,-6,1,5,-3,-1,5,5,-1,4,-4,-3,-8,8,-5,6,3,7,10,-9,-6,-3,-2,-1,-9,3,10,10,9,3,-10,-5,3,-6,5,5,8,6,-6,5,2,1,-5,9,-1,-7,-3,6,6,8,-9,-5,-3,-9,8,6,-3,9,6,-2,-2,9,-1,1,9,1,4,-5,8,6,9,5,9,-9,-4,3,10,-9,-9,8,-4,5,6,-7,-3,10,6,-3,-9,-9,5,-7,6,-6,8,10,-3,-2,-5,5,1,-2,-1,10,-9,-3,3,-1,-7,3,-1,7,-7,4,7,2,5,5,-8,5,5,4,-7,-8,-10,-10,-3,-6,6,-2,9,1,5,9,-10,-3,-10,5,-1,-2,4,-3,-8,5,9,7,1,-4,-3,-2,-7,9,1,7,-9,-3,8,7,-3,10,-2,-1,-6,-1,-8,-3,9,2,-8,-4,-7,-9,2,-3,-8,8,1,-3,4,7,1,7,-3,-2,8,-9,2,2,-4,1,-7,10,-8,-6,-8,-4,-2,-1,-10,8,-10,4,5,-5,2,-10,5,-8,4,-5,4,3,10,3,-6,9,7,7,-1,10,-8,-4,-10,-8,-8,-9,4,-10,-6,6,3,-6,-9,2,-5,7,5,-10,6,1,3,-6,-2,3,9,-7,-5,3,-8,-5,-1,10,-4,1,8,-3,2,8,-8,-9,10,-1,3,-10,3,5,8,8,-6,3,10,7,-9,-3,7,6,-2,-4,-5,5,2,1,-7,-3,9,9,3,-1,-2,-1,-8,8,-8,-2,-7,-2,-7,8,-4,-9,8,-2,5,-5,-8,5,3,-4,6,-5,-3,1,-10,5,1,-6,-3,1,-4,2,1,7,-1,-7,7,1,9,-1,2,-2,2,-3,8,3,-10,-3,-4,-7,9,3,7,7,7,-4,8,3,4,6,-10,4,-4,1,5,-7,3,4,6,-6,3,-10,-6,10,-9,-9,-5,-8,-10,-9,8,-1,5,-3,-9,4,10,3,-8,-3,-1,-7,7,-5,6,-4,-1,-7,2,-9,-8,-3,8,-4,8,3,-2,-4,-8,8,7,10,6,-6,5,9,10,-2,5,3,3,-1,-8,6,7,2,5,-2,7,-1,-5,8,2,2,-5,-1,2,-5,-10,-6,6,-1,-10,-2,-4,1,-3,5,-8,3,3,-4,-7,-7,2,3,3,-9,-8,-2,-3,-2,-4,2,-5,5,-10,-6,10,3,7,1,2,5,-10,10,1,-10,10,-7,8,6,-3,-6,-6,-8,-6,4,-7,-6,5,-10,2,3,3,-9,-4,-10,7,-1,-4,-5,7,8,6,1,-2,2,-1,5,5,-7,-9,5,5,-7,4,-1,1,5,3,-3,-6,-8,9,1,7,4,-6,-2,-4,2,-2,1,10,3,1,-8,-8,-4,-10,-3,-4,3,-6,3,-5,-10,-5,10,-8,-9,-6,5,-1,-3,3,-10,-4,9,7,2,4,-8,-4,6,-3,10,-10,-5,2,-4,5,4,-6,-9,-4,6,2,10,-4,7,-9,-7,10,2,10,-10,1,-4,8,9,-4,-1,8,-4,8,-10,-8,6,8,3,5,3,-7,10,-10,-7,-5,-3,-2,5,-10,-6,3,10,1,9,7,1,-1,-1,-1,5,9,-9,7,-2,1,7,2,-5,-1,9,8,-5,-1,10,-5,8,-5,8,2,-10,9,-7,7,2,-8,-7,10,-7,-8,-5,-4,-10,1,-4,9,-6,-3,7,-4,-7,1,3,8,4,-7,-1,-5,1,-1,9,-8,6,7,-1,-4,7,2,9,-10,-6,-6,-9,9,9,6,10,2,-7,-1,1,-7,-3,8,9,-8,4,-5,7,4,4,3,-4,-9,-5,9,6,-4,-5,2,8,-10,-6,-7,8,6,-9,-3,-3,6,-5,-3,9,1,-10,7,-4,2,1,-2,1,1,6,-5,-8,-6,3,3,7,-5,8,-4,-10,-4,-8,-2,-2,-8,-6,-7,5,-9,-1,2,6,-4,1,9,-6,4,7,4,-8,-10,-7,-1,10,-1,-2,-10,2,5,2,5,-6,6,5,-7,-2,7,3,2,-8,6,-7,8,-10,3,6,-2,8,-8,-7,6,-1,9,-3,-9,5,10,-2,1,1,6,1,2,5,2,4,-9,1,10,2,-4,7,-9,2,2,4,-3,-5,4,-6,2,-4,-6,3,-10,7,10,-8,2,-10,5,4,1,-2,9,-3,9,-4,-2,-1,1,-6,10,3,6,-8,-9,9,-4,-5,1,6,5,5,8,-2,1,-2,-4,5,-6,10,-7,-5,4,-4,8,-4,-1,-2,4,9,-4,6,-4,7,-6,-7,-10,6,4,8,1,7,-1,-2,-3,-10,-10,6,-7,-5,-1,-8,5,-2,3,3,2,-5,-8,-9,9,-9,-6,-4,7,-6,2,-1,7,7,5,-3,9,1,-8,-10,10,6,4,8,1,-2,-9,3,-8,7,10,2,9,-7,-6,4,6,-1,-9,-2,5,5,-8,-2,-9,-2,9,10,-7,-7,-4,10,-10,-10,2,-1,-9,10,5,6,3,2,-1,-1,9,-3,6,5,-4,7,1,2,-4,-7,-6,-4,-2,10,9,4,-9,5,2,-3,6,-4,-8,7,1,-3,-9,-8,3,4,1,-2,-7,-8,-8,7,1,-1,10,-2,-1,9,-2,-1,-7,9,-3,8,9,-10,5,10,-9,-6,8,9,3,-1,5,1,9,9,2,-3,-1,7,10,-3,-8,-9,7,6,-8,-6,-1,6,-7,-3,2,10,-10,-1,-4,-1,-5,7,-10,1,-3,2,4,-5,3,-9,-5,8,6,8,-6,-2,-9,3,3,-9,3,-10,9,9,5,-7,-7,-8,4,4,-2,1,5,-5,1,5,-7,-2,-2,8,-7,10,2,10,1,-6,-2,8,-2,-6,-7,9,-7,10,-10,-9,-7,-2,6,-3,-7,3,7,-7,-4,-3,5,7,-1,-3,7,-7,-2,3,2,-8,6,-8,-3,-3,-9,10,-8,-6,-5,-9,1,-9,6,3,-8,1,-10,-9,6,-2,10,-7,-2,-7,-1,9,2,-5,10,10,-8,-5,10,3,-6,10,-10,4,9,-7,8,2,-6,2,-6,-5,3,-3,4,10,-3,-7,9,-3,3,-1,-7,-2,-4,8,-7,4,-3,-7,-5,6,-9,-10,-6,-1,2,9,6,2,-6,-10,5,4,-3,4,8,-5,-5,-7,8,10,-9,1,10,7,-6,-10,-3,9,-3,-3,5,10,-10,2,3,8,-3,-7,-4,1,-1,1,5,-9,4,-9,-7,2,-6,-7,-8,-10,6,4,-4,-8,-5,-1,10,9,2,-3,-9,-10,9,3,-2,6,2], dtype = "uint8")#candidate|7590|(2704,)|const|uint8
call_7589 = relay.TupleGetItem(func_1977_call(relay.reshape(const_7590.astype('uint8'), [13, 13, 16])), 1)
call_7591 = relay.TupleGetItem(func_1980_call(relay.reshape(const_7590.astype('uint8'), [13, 13, 16])), 1)
func_426_call = mod.get_global_var('func_426')
func_429_call = mutated_mod.get_global_var('func_429')
var_7616 = relay.var("var_7616", dtype = "float64", shape = (288,))#candidate|7616|(288,)|var|float64
call_7615 = func_426_call(relay.reshape(var_7616.astype('float64'), [6, 12, 4]))
call_7617 = func_426_call(relay.reshape(var_7616.astype('float64'), [6, 12, 4]))
func_607_call = mod.get_global_var('func_607')
func_611_call = mutated_mod.get_global_var('func_611')
var_7633 = relay.var("var_7633", dtype = "bool", shape = (12,))#candidate|7633|(12,)|var|bool
var_7634 = relay.var("var_7634", dtype = "uint32", shape = (560,))#candidate|7634|(560,)|var|uint32
call_7632 = relay.TupleGetItem(func_607_call(relay.reshape(var_7633.astype('bool'), [6, 2, 1]), relay.reshape(var_7634.astype('uint32'), [560,]), ), 4)
call_7635 = relay.TupleGetItem(func_611_call(relay.reshape(var_7633.astype('bool'), [6, 2, 1]), relay.reshape(var_7634.astype('uint32'), [560,]), ), 4)
func_6444_call = mod.get_global_var('func_6444')
func_6446_call = mutated_mod.get_global_var('func_6446')
call_7640 = relay.TupleGetItem(func_6444_call(), 0)
call_7641 = relay.TupleGetItem(func_6446_call(), 0)
output = relay.Tuple([call_7563,call_7589,const_7590,call_7615,var_7616,call_7632,var_7633,var_7634,call_7640,])
output2 = relay.Tuple([call_7564,call_7591,const_7590,call_7617,var_7616,call_7635,var_7633,var_7634,call_7641,])
func_7648 = relay.Function([var_7616,var_7633,var_7634,], output)
mod['func_7648'] = func_7648
mod = relay.transform.InferType()(mod)
mutated_mod['func_7648'] = func_7648
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7648_call = mutated_mod.get_global_var('func_7648')
var_7650 = relay.var("var_7650", dtype = "float64", shape = (288,))#candidate|7650|(288,)|var|float64
var_7651 = relay.var("var_7651", dtype = "bool", shape = (12,))#candidate|7651|(12,)|var|bool
var_7652 = relay.var("var_7652", dtype = "uint32", shape = (560,))#candidate|7652|(560,)|var|uint32
call_7649 = func_7648_call(var_7650,var_7651,var_7652,)
output = call_7649
func_7653 = relay.Function([var_7650,var_7651,var_7652,], output)
mutated_mod['func_7653'] = func_7653
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3827_call = mod.get_global_var('func_3827')
func_3829_call = mutated_mod.get_global_var('func_3829')
call_7662 = relay.TupleGetItem(func_3827_call(), 0)
call_7663 = relay.TupleGetItem(func_3829_call(), 0)
func_3214_call = mod.get_global_var('func_3214')
func_3217_call = mutated_mod.get_global_var('func_3217')
const_7667 = relay.const([10,-8,7,-5,2,9,2,-7,5,-4,-3,-1,-2,-6,4,5,1,2,9,-10,1,-9,1,5,2,-2,-4,-5,6,5,-1,5,4,-2,7,6,-1,-2,-4,10,-4,-10,7,-7,9,4,2,3,-7,1,-7,1,-3,-2,-9,3,-5,4,-10,-9,-2,-8,2,-10,-6,-4,-7,3,-9,-9,7,2,6,-6,-6,5,9,2,-7,-2,-3,-8,-1,-10,-5,-1,-2,-6,10,5,8,5,5,9,-10,-5,-7,-3,3,1,4,-2,-4,5,4,-9,3,-10,-1,-10,-9,-6,-9,5,4,-2,7,-7,6,-6,-5,1,-10,6,-1,4,3,-4,-9,-6,4,-3,4,3,-3,8,-5,6,1,7,-10,2,1,8,7,-4,2,6,-1,-5,8,-4,4,8,-2,7,-8,-7,-7,10,9,-8,5,-6,-3,-1,-4,-5,5,-4,-10,8,2,-6,10,-4,2,-1,-4,-3,10,9,1,2,7,2,9,-3,7,9,-7,-8,6,10,-6,8,-9,2,9,3,-2,-1,-4,1,6,-9,-4,4,6,-10,8,-2,3,6,-8,7,-5,2,-3,-3,4,3,-10,-7,-2,-1,-7,7,7,-3,4,8,8,-9,10,3,-3,-3,5,1,9,10,-7,7,2,-10,9,8,-5,-10,8,-10,-10,-5,-4,-4,8,-8,-5,-8,4,3,-7,1,-7,-8,4,9,-2,-1,-3,-9,1,8,2,-2,6,-2,-8,5,-5,4,5,-5,10,-3,-3,3,-2,1,-7,-2,10,-7,8,6,7,3,5,-8,6,-7,-8,4,-1,5,9,4,3,10,3,5,7,-1,7,-5,-5,-3,-5,2,-3,-6,6,2,9,-1,7,2,5,6,5,5,6,-2,5,8,2,-10,4,-8,-3,7,8,-6,5,2,-7,-9,-5,5,4,9,5,-4,9,-6,-4,4,4,-2,-6,-8,-3,6,-7,-9,-2,7,-8,-8,5,-1,7,-9,-9,-10,7,-6,5,10,2,-5,10,2,4,-4,6,-8,-3,7,-1,-7,-5,1,-4,5,2,10,3,9,6,8,3,6,-6,9,10,-6,-10,8,-7,10,3,3,-6,3,8,-3,-9,8,-3,-1,-5,-9,-3,9,-2,-9,-10,10,5,-7,7,5,-10,1,1,6,8,-9,6,1,6,4,-10,-4,-10,-7,1,-4,6,4,-7,3,10,6,-9,-6,7,-5,-4,2,-1,10,-3,-3,-10,-6,1,-2,-1,-9,-7,7,2,-1,-2,10,-1,5,5,-3,-7,9,6,9,2,-10,-2,3,1,-10,-6,-6,1,3,9,2,-4,-6,-4,10,4,7,6,-1,3,-10,4,-7,7,-2,7,6,4,-4,6,6,-3,-7,-10,-8,10,3,-5,-8,10,1,-3,-9,-9,-7,8,-7,4,-3,-4,9,-8,7,-3,-6,-6,-10,-3,10,-3,-7,10,-3,-9,1,7,7,-2,-1,-3,6,3,10,9,10,-9,-5,2,-5,6,6,6,9,10,-1,-6,-2,-6,-6,6,-7,4,4,-9,9,-7,-9,10,10,-9,-3,-9,5,-9,10,-7,-10,8,7,5,5,2,-4], dtype = "int32")#candidate|7667|(600,)|const|int32
call_7666 = relay.TupleGetItem(func_3214_call(relay.reshape(const_7667.astype('int32'), [10, 15, 4])), 2)
call_7668 = relay.TupleGetItem(func_3217_call(relay.reshape(const_7667.astype('int32'), [10, 15, 4])), 2)
output = relay.Tuple([call_7662,call_7666,const_7667,])
output2 = relay.Tuple([call_7663,call_7668,const_7667,])
func_7692 = relay.Function([], output)
mod['func_7692'] = func_7692
mod = relay.transform.InferType()(mod)
mutated_mod['func_7692'] = func_7692
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7692_call = mutated_mod.get_global_var('func_7692')
call_7693 = func_7692_call()
output = call_7693
func_7694 = relay.Function([], output)
mutated_mod['func_7694'] = func_7694
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5259_call = mod.get_global_var('func_5259')
func_5260_call = mutated_mod.get_global_var('func_5260')
call_7784 = relay.TupleGetItem(func_5259_call(), 1)
call_7785 = relay.TupleGetItem(func_5260_call(), 1)
func_5372_call = mod.get_global_var('func_5372')
func_5374_call = mutated_mod.get_global_var('func_5374')
call_7796 = relay.TupleGetItem(func_5372_call(), 0)
call_7797 = relay.TupleGetItem(func_5374_call(), 0)
uop_7798 = relay.log2(call_7784.astype('float32')) # shape=(2, 3, 14)
uop_7800 = relay.log2(call_7785.astype('float32')) # shape=(2, 3, 14)
bop_7812 = relay.logical_and(uop_7798.astype('bool'), relay.reshape(call_7784.astype('bool'), relay.shape_of(uop_7798))) # shape=(2, 3, 14)
bop_7815 = relay.logical_and(uop_7800.astype('bool'), relay.reshape(call_7785.astype('bool'), relay.shape_of(uop_7800))) # shape=(2, 3, 14)
func_6180_call = mod.get_global_var('func_6180')
func_6181_call = mutated_mod.get_global_var('func_6181')
call_7823 = relay.TupleGetItem(func_6180_call(), 0)
call_7824 = relay.TupleGetItem(func_6181_call(), 0)
func_4584_call = mod.get_global_var('func_4584')
func_4585_call = mutated_mod.get_global_var('func_4585')
call_7825 = relay.TupleGetItem(func_4584_call(), 0)
call_7826 = relay.TupleGetItem(func_4585_call(), 0)
uop_7827 = relay.atanh(uop_7798.astype('float32')) # shape=(2, 3, 14)
uop_7829 = relay.atanh(uop_7800.astype('float32')) # shape=(2, 3, 14)
var_7835 = relay.var("var_7835", dtype = "float32", shape = (2, 3, 14))#candidate|7835|(2, 3, 14)|var|float32
bop_7836 = relay.greater_equal(uop_7798.astype('bool'), relay.reshape(var_7835.astype('bool'), relay.shape_of(uop_7798))) # shape=(2, 3, 14)
bop_7839 = relay.greater_equal(uop_7800.astype('bool'), relay.reshape(var_7835.astype('bool'), relay.shape_of(uop_7800))) # shape=(2, 3, 14)
output = relay.Tuple([call_7796,bop_7812,call_7823,call_7825,uop_7827,bop_7836,])
output2 = relay.Tuple([call_7797,bop_7815,call_7824,call_7826,uop_7829,bop_7839,])
func_7849 = relay.Function([var_7835,], output)
mod['func_7849'] = func_7849
mod = relay.transform.InferType()(mod)
mutated_mod['func_7849'] = func_7849
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7850 = relay.var("var_7850", dtype = "float32", shape = (2, 3, 14))#candidate|7850|(2, 3, 14)|var|float32
func_7849_call = mutated_mod.get_global_var('func_7849')
call_7851 = func_7849_call(var_7850)
output = call_7851
func_7852 = relay.Function([var_7850], output)
mutated_mod['func_7852'] = func_7852
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4883_call = mod.get_global_var('func_4883')
func_4885_call = mutated_mod.get_global_var('func_4885')
call_7863 = relay.TupleGetItem(func_4883_call(), 2)
call_7864 = relay.TupleGetItem(func_4885_call(), 2)
uop_7869 = relay.asinh(call_7863.astype('float64')) # shape=(1, 600)
uop_7871 = relay.asinh(call_7864.astype('float64')) # shape=(1, 600)
func_6052_call = mod.get_global_var('func_6052')
func_6053_call = mutated_mod.get_global_var('func_6053')
call_7878 = relay.TupleGetItem(func_6052_call(), 2)
call_7879 = relay.TupleGetItem(func_6053_call(), 2)
func_825_call = mod.get_global_var('func_825')
func_827_call = mutated_mod.get_global_var('func_827')
var_7892 = relay.var("var_7892", dtype = "float32", shape = (2016,))#candidate|7892|(2016,)|var|float32
call_7891 = func_825_call(relay.reshape(var_7892.astype('float32'), [9, 14, 16]))
call_7893 = func_825_call(relay.reshape(var_7892.astype('float32'), [9, 14, 16]))
var_7895 = relay.var("var_7895", dtype = "float64", shape = (4, 600))#candidate|7895|(4, 600)|var|float64
bop_7896 = relay.minimum(uop_7869.astype('float64'), var_7895.astype('float64')) # shape=(4, 600)
bop_7899 = relay.minimum(uop_7871.astype('float64'), var_7895.astype('float64')) # shape=(4, 600)
output = relay.Tuple([call_7878,call_7891,var_7892,bop_7896,])
output2 = relay.Tuple([call_7879,call_7893,var_7892,bop_7899,])
func_7900 = relay.Function([var_7892,var_7895,], output)
mod['func_7900'] = func_7900
mod = relay.transform.InferType()(mod)
var_7901 = relay.var("var_7901", dtype = "float32", shape = (2016,))#candidate|7901|(2016,)|var|float32
var_7902 = relay.var("var_7902", dtype = "float64", shape = (4, 600))#candidate|7902|(4, 600)|var|float64
output = func_7900(var_7901,var_7902,)
func_7903 = relay.Function([var_7901,var_7902,], output)
mutated_mod['func_7903'] = func_7903
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3809_call = mod.get_global_var('func_3809')
func_3810_call = mutated_mod.get_global_var('func_3810')
call_7962 = relay.TupleGetItem(func_3809_call(), 0)
call_7963 = relay.TupleGetItem(func_3810_call(), 0)
output = call_7962
output2 = call_7963
func_7977 = relay.Function([], output)
mod['func_7977'] = func_7977
mod = relay.transform.InferType()(mod)
mutated_mod['func_7977'] = func_7977
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7977_call = mutated_mod.get_global_var('func_7977')
call_7978 = func_7977_call()
output = call_7978
func_7979 = relay.Function([], output)
mutated_mod['func_7979'] = func_7979
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8000 = relay.var("var_8000", dtype = "int32", shape = (1, 7, 8))#candidate|8000|(1, 7, 8)|var|int32
var_8001 = relay.var("var_8001", dtype = "int32", shape = (7, 7, 8))#candidate|8001|(7, 7, 8)|var|int32
bop_8002 = relay.add(var_8000.astype('int32'), var_8001.astype('int32')) # shape=(7, 7, 8)
func_4308_call = mod.get_global_var('func_4308')
func_4310_call = mutated_mod.get_global_var('func_4310')
var_8037 = relay.var("var_8037", dtype = "uint32", shape = (560,))#candidate|8037|(560,)|var|uint32
call_8036 = relay.TupleGetItem(func_4308_call(relay.reshape(var_8037.astype('uint32'), [280, 2])), 2)
call_8038 = relay.TupleGetItem(func_4310_call(relay.reshape(var_8037.astype('uint32'), [280, 2])), 2)
func_7167_call = mod.get_global_var('func_7167')
func_7169_call = mutated_mod.get_global_var('func_7169')
const_8055 = relay.const([5.673114,5.445507,-7.227359,-9.147087,-4.184482,1.320925,-9.205965,-0.614008,4.666837,-3.235398,1.768102,-0.961267,1.540724,2.428584,-6.798162,-7.339885,5.113103,9.109430,-8.157587,-2.635394,-5.082452,0.912147,-4.099702,-4.157629,-6.387344,7.952689,-6.542358,-6.767048,2.994555,2.823878,-9.259884,9.082505,1.187851,5.290804,-0.326120,-8.603411,9.546473,-6.991232,-6.540602,-8.754254,7.222820,-7.068096,8.393549,9.291599,-9.151556,-0.566685,8.542385,6.748490,2.436504,-4.547840,-4.695620,-8.007694,-6.504104,-7.444207,0.286685,0.672413,-6.842418,4.880177,-4.305837,-8.971534,6.905130,1.022753,0.001907,2.580704,6.964492,-9.258614,-5.634338,-5.163570,7.426211,1.894632,0.497830,6.351700,7.613316,9.923913,-8.805375,-6.516893,-6.707433,-6.275634,-7.546830,-4.969820,1.830600,-2.040846,6.492332,-3.299195,6.835912,-3.122505,5.071305,-7.154319,-9.480376,-8.270017,9.661943,-0.420276,3.694504,2.619628,-0.968770,6.492090,1.738820,4.509961,-9.738249,3.511393,-1.989887,-0.584422,-5.644120,-6.804191,-0.289859,6.734691,8.386500,-7.220996,-3.522045,8.249401,0.593426,-9.014327,-5.156671,-2.869963,4.375180,-4.701070,1.181341,9.864674,8.359651,-7.092796,7.993168,4.266137,7.935017,2.767797,-6.575152,-8.777996,7.178290,-1.617119,-4.705162,0.264281,-2.655064,3.094599,-6.839049,0.634951,-8.524242,-0.872470,7.422412,0.751018,4.412192,-5.281710,5.255943,5.386546,9.159405,-6.342583,-5.694226,-0.873604,3.505321,-8.043842,-0.951418,5.564855,1.426139,-7.103819,1.954585,1.930270,-2.065020,-9.278934,-0.800980,4.200411,2.266677,-5.885960,7.033697,7.119141,-3.486253,-9.333587,6.680822,-6.194645,4.590175,-9.125047,-7.473826,2.463327,0.285057,-3.841828,-3.737430,-9.617289,0.666439,3.644394,5.529789,0.724782,2.378809,-8.118444,7.961198,4.815634,-3.306873,6.817263,-9.470250,3.664766,3.657144,9.018978,9.430946,4.431564,-3.381422,1.043204,1.264248,-7.777171,9.126268,-4.711621,9.135532,1.331121,0.200664,-6.285210,-8.244223,2.297618,0.815806,5.564312,-8.453176,0.767509,5.053514,-5.804335,6.562447,2.253220,-4.361919,2.128951,-9.031999,3.446019,4.202291,5.306628,9.200464,7.124497,0.395659,-1.964589,-7.224256,8.569927,-3.030307,-6.499419,-6.562878,-7.519763,0.489834,-8.461915,8.325696,7.685757,2.881085,-1.210093,-7.756958,2.619775,-3.732643,9.652832,4.947691,-8.334399,5.016766,8.266097,1.302787,-2.440609,0.194615,-8.271111,-6.734206,8.306899,-2.711683,-8.297404,-4.405088,-1.898379,7.371414,3.060325,-7.508008,1.142809,-7.046817,7.507553,-7.338390,7.569521,-3.689523,-3.249610,1.726278,-7.850867,7.786678,-4.986088,-8.908116,-3.637365,6.266270,-8.117355,-3.851226,4.595276,-0.776231,-6.152061,-7.943592,-9.558039,4.089121,8.381741,6.875668,-5.238255,-5.996629,-6.429210,1.439299,6.473513,-2.771503,8.593678,0.636676,5.341656,4.137944,-4.977656,8.433249,9.549223,-7.972028,-2.197430,-5.620110,-9.015224,3.692682,-0.267477,-0.516017,4.518452,8.131941,8.054928,0.076336,5.197293,-0.512257,-5.776834,-0.188888,-4.668615,-1.038209,-7.359461,2.260519,-9.758274,9.728906,9.400333,-5.278134,-4.239945,6.776862,-4.898796,8.193638,-0.390774,0.632560,8.296586,-5.131138,-9.011291,-4.614629,6.940469,-6.850186,2.292500,-1.497344,4.867788,8.988226,3.363834,3.211262,-3.733776,9.836613,-6.431534,8.940435,-6.854853,3.104683,3.310220,-0.393847,7.716101,-2.162868,-5.075582,5.810545,3.463162,-0.479266,-3.212376,-2.902874,-7.420964,1.135977,-1.317985,-8.715194,-3.537705,-5.868133,-2.887394,-4.145671,4.043090,-2.150936,-5.550929,8.710097,-0.754136,-0.109142,8.766611,6.810735,-2.346498], dtype = "float32")#candidate|8055|(364,)|const|float32
call_8054 = func_7167_call(relay.reshape(const_8055.astype('float32'), [7, 13, 4]))
call_8056 = func_7167_call(relay.reshape(const_8055.astype('float32'), [7, 13, 4]))
func_147_call = mod.get_global_var('func_147')
func_151_call = mutated_mod.get_global_var('func_151')
call_8062 = func_147_call(relay.reshape(var_8037.astype('uint32'), [8, 5, 14]), relay.reshape(var_8037.astype('uint32'), [8, 5, 14]), )
call_8063 = func_147_call(relay.reshape(var_8037.astype('uint32'), [8, 5, 14]), relay.reshape(var_8037.astype('uint32'), [8, 5, 14]), )
func_6543_call = mod.get_global_var('func_6543')
func_6546_call = mutated_mod.get_global_var('func_6546')
const_8068 = relay.const([[4,8,9,2,-6,-5,1,7,6,7,8,-10,-1],[9,-9,-8,10,-8,-3,8,5,8,9,-3,-9,-9],[-10,-5,7,3,-10,9,-4,-9,-7,8,-2,8,-2],[-4,-3,-10,-3,-8,-1,-8,-9,-9,4,-3,8,-5],[-8,10,5,-4,9,3,-1,2,-1,10,-7,-4,8],[-4,-9,-9,-1,8,4,-4,6,-5,-10,6,9,-1],[7,-9,-3,3,3,8,10,-2,9,-9,5,1,-3],[7,5,10,1,8,4,5,-3,1,-10,10,-9,4],[5,9,4,-9,4,-2,-9,-9,2,-10,7,-10,6],[-6,-1,1,6,3,8,1,-3,6,-1,-7,-1,8],[10,-6,-10,-1,3,-6,-4,8,-10,3,-10,-7,6],[-6,1,-8,3,-7,-6,-5,-2,7,9,7,6,7],[1,-9,-8,-5,-8,-9,-8,-6,-7,-3,-2,-7,10],[4,-4,-2,-3,-1,7,-9,10,7,-8,-2,4,6],[-10,8,-6,3,-3,4,-9,8,-2,10,9,-10,10],[4,1,-1,4,10,2,-2,10,3,-3,-3,8,-9],[-3,-3,-2,9,6,4,-9,-10,8,8,-9,7,-1],[-7,6,-7,-4,3,7,1,2,-3,-10,6,8,5],[-6,-7,5,-8,-9,-3,5,-9,8,6,-5,-2,6],[2,3,-9,-4,-8,10,1,10,2,-9,-8,1,8],[-4,1,-10,2,-2,2,7,4,-7,7,-8,5,-2],[-4,-8,8,-3,-10,2,6,-2,10,10,7,9,-7],[4,4,-8,8,-1,5,-7,-6,-8,-5,-5,-8,-10],[-4,-8,8,6,10,10,-7,-6,6,-1,4,-7,8],[5,8,-10,4,5,1,-4,5,-9,-7,-7,2,-5],[7,-7,-3,10,8,6,-9,-6,2,1,5,10,-9],[-3,6,9,-10,-8,-9,-6,10,2,3,-2,-7,-2],[7,2,-2,-8,5,-2,2,-9,10,-9,-7,2,1],[3,-8,-10,-1,-2,-9,1,-6,8,3,-2,-3,5],[-3,8,-2,-2,9,5,6,3,8,1,7,5,-9],[4,7,1,-6,-4,1,-9,7,10,-3,-9,7,6],[-1,3,-7,1,-6,-4,1,-3,3,5,-7,-3,8],[-1,6,-6,-10,7,5,3,-10,8,-6,-6,-2,-1],[5,-9,-8,7,-2,10,-3,-1,-7,-4,1,10,2],[6,-8,2,1,-8,4,4,10,9,-1,6,3,6],[-1,-9,4,-6,4,-6,9,-5,-1,10,3,9,-8],[-3,-4,-4,5,7,-1,-2,8,10,-1,-4,-4,-4],[-4,2,-7,-2,3,-7,9,8,4,5,-7,3,1],[-10,2,3,-8,-5,-9,-5,4,1,-5,-5,8,-5],[6,2,-5,-6,6,-10,-6,1,-3,8,-10,1,7],[-6,-8,9,-9,5,1,9,-3,-4,-6,-4,3,8],[-2,-9,-5,-5,6,-8,5,8,-3,5,-8,4,-6],[-4,-4,-2,-9,9,-8,8,-8,-8,10,-9,5,-10],[5,-8,4,-1,2,7,6,9,2,-7,-6,3,3],[8,8,-10,3,3,9,8,-7,5,2,-7,-1,-5],[9,10,2,9,-7,-2,-6,8,10,7,2,1,3],[-8,-2,1,3,-3,-9,-6,1,7,-4,3,10,1],[1,5,10,10,8,-3,-3,7,-9,10,-10,5,1],[-6,-1,2,9,-8,1,-2,1,2,-2,-10,2,10],[7,6,5,-9,-8,-10,6,-7,8,-8,5,-7,-10],[9,-4,-4,6,1,3,-10,8,-2,-8,3,-8,-8],[-2,-3,9,4,3,-6,-1,10,4,-7,-10,9,7],[7,-5,-10,8,-1,7,2,-5,-9,-5,10,-1,-4],[-5,-10,-4,-10,1,-6,-3,-10,2,8,-10,6,8],[-9,-5,9,-5,-6,7,8,6,-1,-10,-9,2,-4],[6,10,-7,10,-1,6,9,4,8,6,-5,10,5],[-2,9,-9,-5,7,-7,6,8,-3,1,-5,-7,-2],[-7,2,4,-10,9,5,10,7,-3,-7,-2,9,8],[-4,-6,-9,-9,-6,-6,-5,10,10,4,-9,-10,-7],[9,-8,10,1,-10,-1,-3,3,5,-8,-6,7,8],[6,-4,-10,8,7,-4,6,-1,3,5,-5,4,5],[2,1,-8,7,1,-5,7,-9,-10,-5,3,5,5],[-8,3,-8,-5,-4,5,7,9,5,5,9,10,-8],[-3,10,-3,7,-2,-1,-4,-4,-4,-5,4,-1,5],[-4,-5,7,-5,7,5,-6,-9,-8,1,1,2,10]], dtype = "int8")#candidate|8068|(65, 13)|const|int8
const_8069 = relay.const([6,-2,-6,-3,4,2,-10,5,6,2,-6,5,-8,-5,-4,9,6,-10,-8,-7,-5,-6,-8,10,5,-5,4,-10,8,1,10,1,3,10,4,-4,8,3,-10,-9,6,-4,5,-3,9,-2,5,-9,-5,-8,8,-8,-3,-4,6,8,9,-2,-7,-5,8,7,1,2,7,-4,3,3,7,-10,3,4,-9,-6,9,5,9,3,-8,-7,-4,-9,-5,4,4,-4,2,-10,-4,7,8,-3,4,8,-10,8,-5,10,3,-1,-7,-5,3,-2,-4,2,-1,-10,10,10,2,-3,-6,7,6,8,5,6,1,-6,-7,6,1,4,3,-1,-1,-1,7,6,-8,-1,-10,-2,3,3,-6,7,-6,-1,4,-3,8,1,2,1,4,4,10,-4,-7,2,-7,-3,1,-1,7,9,-5,-3,10,10,9,-9,-1,-2,9,2,-5,10,-10,-9,2,-4,-10,6,4,-5,10,-10,6,-1,-5,2,9,-4,-2,6,2,-1,-9,-2,2,4,3,5,7,6,-1,2,10,-9,-2,6,-4,-8,-3,6,10,-9,5,2,-4,-5,-7,-4,-6,1,7,4,4,4,2,7,1,3,-2,9,-3,10,5,9,7,9,-7,5,5,-3,1,-9,5,-10,8,2,8,-1,6,-4,10,-6,8,-2,-5,10,-2,10,-2,4,-2,1,-8,2,-2,8,-10,1,-8,-1,-8,8,-1,-7,9,-4,8,10,10,10,8,6,-4,8,-1,-4,-1,7,1,8,5,-10,9,-9,-3,1,-8,-1,-5,2,-9,5,1,3,-7,-9,-5,5,10,-3,4,-4,4,-3,-8,4,-3,7,-10,5,3,10,-4,4,-1,-7,-4,5,10,-4,5,6,-7,-4,-5,-6,3,-8,3,3,10,6,2,-9,-1,1,-3,4,9,-8,-6,-5,-10,-8,-5,-4,-10,7,4,-6,-1,1,-5,-5,-4,9,5,9,-6,-8,-5,-4,-7,-10,-8,-7,5,-4,-4,3,10,-6,-5,-4,-1,2,7,2,8,6,-8,9,-1,-2,-10,1,-8,-8,-1,3,-5,7,-10,7,-2,-8,-5,4,7,-1,2,10,-10,-4,-1,4,-4,7,1,-6,8,-3,-10,-1,2,8,5,-7,-6,-5,-2,2,-9,1,-2,2,2,3,10,-1,-5,10,6,-2,-8,9,7,5,-10,-9,-5,2,-6,-9,8,-1,-6,-10,8,-5,2,-6,5,8,-10,-8,6,4,5,-10,-3,6,4,4,-10,8,-2,3,-10,3,-8,6,-10,-7,4,-6,10,8,7,-6,10,-1,10,2,-8,9,5,-1,-6,8,8,8,-7,2,8,-3,1,1,-1,-1,-7,3,8,6,4,5,-9,10,1,2,-9,8,-10,-9,-1,9,1,-7,-8,2,-9,6,1,-6,7,2,4,5,-6,-6,-5,4,-7,-6,5,6,8,-4,7,1,-9,-1,-2,8,1,6,8,-5,-2,9,10,1,-7,-6,4,-2,2,-7,-2,-6,-8,-2,-2,-9,-7,-2,-6,-6,8,9,1,7,7,-10,9,-3,-6,-3,-1,5,-3,-6,9,-1,-3,-1,4,-8,1,9,1,9], dtype = "int32")#candidate|8069|(600,)|const|int32
call_8067 = relay.TupleGetItem(func_6543_call(relay.reshape(const_8068.astype('int8'), [13, 13, 5]), relay.reshape(const_8069.astype('int32'), [2, 300]), ), 0)
call_8070 = relay.TupleGetItem(func_6546_call(relay.reshape(const_8068.astype('int8'), [13, 13, 5]), relay.reshape(const_8069.astype('int32'), [2, 300]), ), 0)
output = relay.Tuple([bop_8002,call_8036,var_8037,call_8054,const_8055,call_8062,call_8067,const_8068,const_8069,])
output2 = relay.Tuple([bop_8002,call_8038,var_8037,call_8056,const_8055,call_8063,call_8070,const_8068,const_8069,])
func_8075 = relay.Function([var_8000,var_8001,var_8037,], output)
mod['func_8075'] = func_8075
mod = relay.transform.InferType()(mod)
mutated_mod['func_8075'] = func_8075
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8075_call = mutated_mod.get_global_var('func_8075')
var_8077 = relay.var("var_8077", dtype = "int32", shape = (1, 7, 8))#candidate|8077|(1, 7, 8)|var|int32
var_8078 = relay.var("var_8078", dtype = "int32", shape = (7, 7, 8))#candidate|8078|(7, 7, 8)|var|int32
var_8079 = relay.var("var_8079", dtype = "uint32", shape = (560,))#candidate|8079|(560,)|var|uint32
call_8076 = func_8075_call(var_8077,var_8078,var_8079,)
output = call_8076
func_8080 = relay.Function([var_8077,var_8078,var_8079,], output)
mutated_mod['func_8080'] = func_8080
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5323_call = mod.get_global_var('func_5323')
func_5325_call = mutated_mod.get_global_var('func_5325')
call_8085 = func_5323_call()
call_8086 = func_5323_call()
func_4238_call = mod.get_global_var('func_4238')
func_4240_call = mutated_mod.get_global_var('func_4240')
call_8087 = func_4238_call()
call_8088 = func_4238_call()
output = relay.Tuple([call_8085,call_8087,])
output2 = relay.Tuple([call_8086,call_8088,])
func_8090 = relay.Function([], output)
mod['func_8090'] = func_8090
mod = relay.transform.InferType()(mod)
mutated_mod['func_8090'] = func_8090
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8090_call = mutated_mod.get_global_var('func_8090')
call_8091 = func_8090_call()
output = call_8091
func_8092 = relay.Function([], output)
mutated_mod['func_8092'] = func_8092
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5904_call = mod.get_global_var('func_5904')
func_5906_call = mutated_mod.get_global_var('func_5906')
call_8119 = func_5904_call()
call_8120 = func_5904_call()
func_5293_call = mod.get_global_var('func_5293')
func_5296_call = mutated_mod.get_global_var('func_5296')
const_8127 = relay.const([8.390484,-7.747837,8.124968,8.986091,-5.146178,0.037623,-5.380517,-2.241296,-4.279413,9.494456,-2.054548,-6.443911,0.674616,1.569415,4.612129,-6.978167,-8.382550,-7.495408,5.154596,1.719197,2.085061,4.185253,-4.388369,-9.089108,0.446811,1.033721,4.676341,5.879604,6.170670,-3.674181,4.720153,-2.586583,3.494927,5.833009,-5.036684,-1.430196,3.178716,-2.279658,9.984268,9.756944,-6.255597,4.762141,-6.627136,-3.117793,3.376425,-3.279046,3.621900,-8.529538,9.122858,1.330170,-4.044598,1.793566,7.447872,1.128000,0.590403,-9.435864,7.474820,0.190567,-5.291173,9.087811,-2.066672,-7.909247,-9.132541,-0.201192,-0.909466,-4.432079,-2.066655,8.111883,4.960156,-7.292702,6.246267,-8.933594,-6.330693,-9.359256,9.339896,-4.127039,4.821393,6.185943,8.817488,-0.184420,2.615741,-3.406638,-5.159140,7.413355,-9.053018,-7.732700,-3.885646,-7.099486,2.572408,-0.463736,4.679923,-6.957892,3.733371,-8.182206,-7.200950,8.664533,8.025505,1.498959,0.933784,4.171432,-8.118301,5.109979,-2.844681,-7.551405,-2.269733,-1.524189,1.933265,-0.496373,-3.206894,-6.981367,4.218656,-3.057497,6.469986,7.293953,2.816826,9.030514,-1.868781,-4.090135,-4.380444,-5.694344,8.574873,-5.036490,-9.866442,-3.047244,-0.814870,9.255452,-2.114262,-4.050150,4.100195,-1.905565,7.413764,-0.482747,-9.866679,-3.053563,3.862725,1.949370,-8.829879,-4.385629,-8.209143,5.333630,5.141762,7.622739,7.237734,6.809489,8.118372,9.604020,0.809072,-4.449197,-8.433618,7.375547,-8.688203,0.939467,-7.731610,9.749681,-7.039957,3.894587,0.768493,4.572735,5.165727,8.841426,-8.755381,1.892387,-4.128492,3.086005,-7.401980,7.554574,4.051137,7.626513,-4.510973,-5.455066,-9.713857,-5.080621,-3.199863,-3.777967,-8.937368,-2.226263,-0.859449,7.723557,-0.951790,8.226313,6.988100,2.102534,2.155784,-8.154611,3.886422,-3.469964,0.588032,2.216423,-9.018486,3.688154,0.305456,7.406943,2.288298,-8.585036,2.430327,-5.383824,-4.466412,8.167490,7.455211,3.344182,9.472220,-3.355912,-9.163722,-8.805262,2.330665,-9.683492,-0.524972,-9.808483,-2.030027,9.494021,-6.725116,-0.657613,4.322532,3.649539,4.692906,4.091206,-9.530702,0.684968,6.967032,-1.036594,5.462103,0.815030,-8.429993,5.026195,-1.408085,3.727803,3.422722,-3.806041,2.015117,9.344911,-6.116116,5.022221,-1.699200,-2.854692,9.906592,-0.026277,1.972210,-5.397009,7.526659,-6.285703,-8.186744,-4.784462,5.744032,-5.990560,-2.004920,5.531002,-8.154046,-6.800021,-5.051787,-6.585896,0.544426,-3.666029,-9.759733,-8.166933,7.230591,5.761098,-7.388853,8.699550,-7.364207,5.865586,4.839591,-7.330377,7.566466,-2.666509,0.263982,8.078896,6.568407,4.671167,-7.639570,8.742360,-1.528637,0.579141,-1.645098,-8.350527,-4.040724,-1.548606,-9.542826,4.257514,2.375075,4.076684,-5.198978,3.399123,9.398517,9.406167,-2.756924,6.185755,-3.772821,-9.148629,7.405753,1.057408,-2.509909,3.929398,-7.409223,-2.750315,-9.888547,-4.746313,0.505942,-9.614016,-1.944521,-2.771749,-0.885849,6.748638,4.756666,4.704521,-3.638212,-5.197872,-1.007775,-5.726307,3.400336,-3.637671,-3.872760,-3.219915,-8.814490,-5.855187,7.884035,-9.474586,-5.703124,-8.629324,1.391257,-9.771748,-9.334676,-3.389811,-6.756242,-3.540937,7.119696,3.845633,0.675907,3.561271,-2.653720,8.163023,2.192082,2.052251,8.016810,5.100721,-2.143366,1.296576,-9.552111,2.321175,-6.827256,-6.770939,1.780467,7.787602,-9.005627,-5.008072,6.400339,-7.157594,1.442290,-3.906964,3.214811,8.390763,-2.819663,-9.798884,-4.359981,5.873267,2.394568,1.546389,-0.740720,-0.331100,7.102465,0.718048,-4.081147,0.731165,-0.394697,-5.239476,9.261188,8.922177,-0.040325,9.947586,2.120614,0.630557,-8.188744,4.832322,-5.417222,4.324304,8.154201,-7.764693,-2.491572,1.460850,6.435169,-2.154523,-1.555087,-8.500374,-1.384633,1.997316,9.057291,-0.204260,8.390625,-0.621759,6.038857,-6.444752,-3.626935,-5.723396,-1.137984,9.365548,-5.693158,9.997501,9.421066,2.240450,7.917978,-0.534225,-6.314944,-3.073360,-5.481999,4.215087,8.754389,-0.290652,-6.861374,-9.346918,0.714842,-0.385121,-5.105573,-1.357279,-1.485448,2.887568,-3.346993,-8.935604,-6.776428,2.049647,0.920764,9.950445,-5.549286,-1.342892,-8.907201,1.143355,2.185526,3.925098,2.203794,0.286759,-0.128640,7.605949,-5.312297,6.883023,0.722879,-4.336667,2.555694,3.511143,7.557083,-2.956913,-7.470753,5.617000,7.565719,1.495515,-2.597481,-6.657913,6.827688,-2.697722,8.910226,2.596833,-4.942342,3.421668,1.847515,2.593723,7.914989,-4.565151,4.437976,7.120794,0.608788,-5.481001,6.456261,-1.429374,-9.930793,4.987933,-9.671001,-8.852329,-9.196071,-1.439723,-7.877609,-6.260219,3.723018,-4.844795,3.745949,1.853148,-2.072942,-6.065062,3.052206,9.313802,3.905544,8.680320,3.558635,-2.978506,-5.503863,5.152605,-5.309273,-1.165096,-0.928267,4.137797,-8.405493,-4.098458,-3.699164,-4.881069,5.976097,1.180327,-5.438060,-7.165476,6.454101,7.686472,2.986567,-0.033504,4.686985,2.888613,5.792554,5.115158,-5.291066,4.207818,-3.201408,-4.621741,3.146295,7.875233,-1.024873,2.871092,-4.180569,0.467830,6.125204,-1.899860,-7.293687,-8.706794,-8.235597,1.082512,-6.058816,5.368247,3.391808,-6.315405,0.922160,-5.605883,-4.436186,1.512898,5.830284,-4.926472,3.245058,1.286457,5.944498,4.590449,5.791951,-8.461564,7.954288,-7.512026,5.664318,9.228636,-1.827506,-7.152454,3.749091,-5.434960,2.883465,7.942484,3.842796,-5.358675,2.111305,-8.381229,7.330063,-9.898273,-0.847357,7.524680,7.764098,-3.515701,-7.051765,-8.568496,2.268119,-2.030819,-5.695939,0.820097,-7.038088,-4.081780,0.909256,-5.978134,0.992716,-7.448952,-0.670252,6.793751,-5.847592,6.370211,-9.869344,5.521331,-0.566516,-9.749886,5.043939,-5.539765,-5.925969,9.097737,8.361478,-0.356292,-3.726535,-8.968183,-8.228011,7.290617,-7.960340,8.663162,-5.268169,-9.280728,6.975004,0.113482,-3.462170,-4.980675,-8.254653,-9.293511,-0.447461,-8.749797,9.991595,0.244395,-5.898321,6.179206,8.899845,-8.408510,4.601103,6.694970,8.219149,9.007598,-0.749756,-5.433396,-2.867563,2.177467,4.576395,2.234688,-9.780174,-0.781741,0.889330,8.107051,1.865226,3.417140,-1.548745,1.480236,0.071041,5.748038,-7.578851,1.277391,4.277501,4.038622,-1.703269,2.925539,3.388775,-8.549601,9.686069,-7.291937,1.893174,0.744911,-7.151966,5.717306,-5.543459,7.084279,5.334009,5.859250,0.157864,9.791447,5.139388,0.409244,1.430510,-0.018914,9.549856,5.337573,-0.302450,5.858669,6.447229,-4.530144,5.810861,-7.004348,-1.576042,7.734845,5.419065,-8.103635,-1.750502,6.248147,3.766354,-7.711728,-4.103286,5.493789,6.417636,3.179205,9.958791,-9.808526,-4.409929,3.947663,-3.368328,-4.690976,-0.188899,-9.280672,-7.834260,-1.008573,1.665657,1.141272,-8.906040,-6.221541,6.607661,-4.419146,-4.165083,2.377926,3.515961,1.715405,-7.303307,0.369403,-3.567739,4.614678,-5.745677,-2.533673,-2.185407,1.692413,-8.092108,-8.681556,-2.632960,3.197737,3.874460,0.757493,6.881627,-6.055119,-1.765365,-0.986259,-0.640864,-1.645107,8.125367,-5.194618,-1.595363,-8.383702,-6.759761,-8.969733,3.968204,5.575447,-1.037803,-0.888462,4.871341,8.220625,-8.422232,0.236284,5.619269,0.171140,-7.180144,7.447247,-9.184032,-9.907179,-2.618558,3.446501,-9.635952,3.186922,0.494503,-0.100416,-1.996232,-0.894165,-3.797789,6.454882,3.790684,-9.498311,2.673626,-9.330446,-8.163034,-0.695147,5.208232,-2.588548,-9.135837,7.344938,3.815178,-8.996500,7.137015,4.989815,-9.232890,-1.414360,5.713249,-9.848267,-2.758390,-4.010791,9.325185,9.391032,-4.899407,-4.437451,8.864313,-0.200009,5.645402,2.961142,-2.360820,-8.880860,7.300151,-8.406769,-3.801003,1.254686,-1.361777,1.882782,-6.719595,-7.875772,-6.444226,6.566843,-1.217343,9.236920,4.265624,6.059687,1.318282,-1.303556,-1.286733,1.525239,0.274279,3.458326,8.348475,9.083143,0.081305,-7.684392,-5.464413,-5.122170,-1.253426,9.745961,-2.157961,2.407245,-5.794810,-1.068853,-8.514220,4.806069,4.016920,5.580206,0.195890,-1.325917,7.730519,0.992468,3.883199,-5.489299,6.949506,9.235383,-6.222811,5.072546,-0.886576,9.921555,7.763984,6.249331,0.918703,0.977053,5.965228,-7.639325,5.435132,5.605296,4.851745,-3.788388,9.968780,-1.931651,-4.484704,-2.494281,7.264463,6.190596,8.601835,8.128793,-2.376935,3.320352,5.632346,-9.134120,6.117514,2.468812,9.232199,0.245166,0.636784,9.818620,1.271352,-8.861988,1.271776,-1.155970,-8.126209,-4.868438,-5.685818,1.813364,7.836458,-1.521171,2.055613,4.039515,5.249523,1.235820,-3.199921,-9.198020,-8.870786,-9.871287,8.452580,-7.774097,2.773722,-9.886364,7.001105,2.311571,8.424448,9.644575,3.758273,9.599834,-8.090482,3.596885,7.141982,-0.473117,-3.419986,-0.327222,6.054236,-0.952604,3.494979,5.233093,-6.031291,6.438562,-3.348002,-4.431124,0.530319,3.742970,-5.543155,-2.130734,-7.221975,7.449441,2.998787,-0.625281,8.325899,5.786098,5.367409,2.756645,6.307339,3.599338,7.308595,4.757934,-1.226935,-6.488385,4.138427,-9.135513,-0.044516,9.287402,0.829546,-0.279982,-8.135850,5.472218,-5.899116,2.493292,6.177425,-5.163959,-7.871934,4.079426,-3.467100,9.357543,-1.577132,2.316911,9.721660,3.013315,2.650113,4.254357,2.629354,3.912958,8.335611,-4.541345,-7.993884,-0.663814,-3.162774,1.999765,9.023160,9.555832,-4.344871,-9.499929,1.091596,1.694459,-3.263371,-9.581262,4.029037,9.419944,-2.636243,-4.691932,-4.201302,5.795628,-2.610006,9.880775,6.172820,-6.883617,-9.121429,0.378250,-0.517378,-8.694877,-7.485241,-3.899947,-1.355631,-2.487741,6.390275,3.305690,3.959182,0.415255,3.407543,-7.945157,8.017922,6.053209,9.378165,7.455600,4.865089,-9.097283,-0.024456,8.108745,1.795365,6.809191,-0.941983,-4.567382,2.715410,-1.213194,3.377745,4.311779,8.783608,-9.025554,4.790379,-6.864273,7.239112,-2.635465,9.716203,-0.343994,-3.030129,-7.303904,6.090732,-4.278054,-8.440974,8.401396,6.500051,-2.677736,0.917337,-6.369407,-3.183782,6.528071,6.044324,4.836716,-6.843577,1.848055,5.899518,4.475604,6.604955,4.207540,-5.032356,6.300350,6.603376,-6.568419,-6.912625,7.020355,3.388910,-5.704669,9.147924,-0.279932,7.716815,-7.871854,1.947393,3.412182,0.638006,-2.661877,-7.672982,-1.652903,6.064858,-6.899226,5.224791,-3.508060,8.799668,2.091451,-5.092021,-3.182811,-2.557395,-7.727132,-1.316728,-6.517500,-6.856929,-7.298008,-8.524474,-1.648358,0.931184,4.720323,-4.825292,-8.640667,-5.105420,-8.413098,0.790984,-5.179407,1.404549,2.389646,6.307633,-8.549601,-4.153523,-4.028831,6.186779,-2.551002,2.724167,6.372171,6.577418,1.006192,3.381036,-8.960190,-9.644416,-0.294714,2.111262,-5.150763,8.785917,-3.028264,8.224157,-0.228809,1.748464,1.543057,-2.623919,-8.209005,-6.206759,5.133538,-5.223901,-4.436150,3.389481,-4.218112,-0.910675,4.207018,9.186545,2.420894,-7.697438,9.834176,-0.426908,-8.211121,7.433994,-3.291906,6.593127,-2.270599,0.601557,-6.190936,3.543226,8.880435,7.897011,-7.441740,-0.141960,6.816757,7.720803,-2.112922,-8.335587,7.174862,-4.913705,7.700561,0.568290,3.543235,5.401585,7.652772,-4.051692,-3.910861,0.423593,6.718704,2.155223,-9.191843,5.395705,-8.942203,-6.411806,-5.068320,-3.262958,-2.833112,9.887172,-1.748903,0.406949,7.780461,6.270139,-5.621168,-0.792401,-2.417692,-6.929514,8.371730,-6.270427,6.061648,1.929292,5.173928,-8.561640,4.186407,7.704526,-3.525389,-6.434811,-6.249326,5.066508,-4.229001,-0.616380,6.159540,-0.438340,6.123728,3.685986,7.705126,-5.775241,-1.128006,-1.649223,-7.339823,6.167719,-4.853711,-6.815595,0.749162,2.538060,-2.598339,6.756304,0.298740,-4.177331,-1.226189,5.500809,-8.871021,-5.791774,-9.827486,-4.189801,-3.649248,8.372338,9.974382,2.610003,-1.858013,6.428825,2.754119,-9.549395,-6.167401,9.019623,-4.394809,-1.314405,-8.527598,5.063839,3.150249,9.219651,-5.811101,-2.236787,-6.994121,-5.338621,1.261851,6.419239,-7.540925,4.609210,-8.895786,3.284073,4.876773,2.678352,-2.798749,2.805023,0.364949,1.642975,7.367948,8.289138,-9.519070,-2.078314,3.408883,-4.469169,-4.500873,-7.481747,-6.564354,8.368573,9.195718,6.863952,-6.075688,2.849652,2.305384,5.506369,1.930058,-4.183224,-4.655550,6.564929,3.928176,-9.398029,3.973968,-3.697290,-6.352576,6.237455,6.687335,-8.624760,8.530679,3.504200,-8.015499,-5.605169,5.269043,5.872185,0.144181,-1.064283,-1.092756,-0.018073,2.128791,1.469062,1.341472,-4.623041,2.016226,-2.565982,-0.351545,6.165149,-2.725179,-5.810631,3.417700,9.116234,-8.011422,5.497913,-8.429380,-2.643884,-6.958008,-0.723068,2.171163,-5.487566,0.592385,4.091597,-4.099637,-3.175332,-6.596919,6.841970,2.428287,4.161516,-7.027461,-6.600248,-1.056520,-9.295856,2.720973,-9.201404,8.791311,0.036641,5.584367,0.032482,-6.733832,-1.785164,-1.687801,-0.789580,1.358176,-0.944858,-5.044753,-6.391775,3.864398,3.717624,4.272879,3.564336,7.033064,7.351104,-5.001210,-9.501304,5.255823,0.731928,-0.751657,9.620957,4.469056,7.746506,-2.536711,6.115518,7.117989,-3.930587,-2.698921,4.978737,5.189232,9.151880,3.941077,-5.209535,-8.655517,0.701586,3.961595,-5.411899,-9.618072,-8.304498,-2.890803,-6.863369,-4.047825,-5.861775,8.721487,-9.790319,6.240893,-6.833677,-2.152223,3.773525,-4.229290,8.439830,9.210317,9.944337,-2.254158,-1.808107,7.956980,-0.710719,-4.928766,-0.459636,-0.185200,-7.758618,-3.298239,3.987224,0.910198,-8.297588,6.375869,7.244991,6.827142,-4.737729,-2.687717,-1.071374,4.888042,3.833300,-6.342113,3.968091,4.173172,-8.265968,-7.761517,-8.377977,-9.331620,-0.151686,-0.457765,-6.362166,-8.089671,0.067116,6.163100,-8.312558,-9.607397,-2.816730,3.776332,-6.253456,3.118943,2.293443,-8.385473,4.209695,-5.766351,-0.705631,6.089204,-2.219653,2.384412,-1.237216,-8.101560,7.275637,1.983406,4.948489,-4.264975,2.953141,-3.405968,2.010349,-6.441535,3.126481,-4.171435,0.718670,-6.065974,4.063597,-0.326042,-8.750192,-3.848478,3.274486,-9.211737,4.571214,-9.075706,-6.081035,9.374013,2.071284,3.125421,-6.864116,-2.630341,2.961206,9.784994,-2.753271,7.811858,-5.706258,4.245381,2.598643,-7.269383,-4.960396,2.293879,6.175249,-0.793697,-2.469308,5.253859,-1.368547,-7.955512,-7.389400,-0.358411,9.502926,-4.028129,-8.353457,-1.237943,0.728158,-7.730799,6.283357,-5.464038,-4.447725,-5.043313,-9.100126,9.572784,4.995896,9.043520,6.448451,5.615341,5.310302,4.366889,9.985579,2.954216,-2.862408,-5.555755,8.533904,9.223114,8.599622,-1.689993,0.298589,-3.204986,2.451992,4.615068,-1.721055,-7.131414,-3.013245,5.355045,5.913191,-7.949188,-2.960992,1.958097,4.197318,6.675836,-5.698485,8.727523,5.290381,1.182077,9.882632,5.425458,3.826571,2.190382,9.912086,2.190366,1.809949,6.330276,-5.102847,1.360746,9.134864,-2.304925,-1.295387,3.008179,-1.017611,-4.482866,5.666481,0.608220,3.574769,-9.180184,5.932947,4.079847,2.347802,-0.056189,-9.024348,-3.018454,-3.077769,9.777033,-9.162196,-2.770715,0.929353,-9.674251,-2.074717,6.096445,-5.953124,5.185706,2.239451,-7.341423,4.458654,-8.314604,-5.138297,2.804431,-8.274797,6.634969,1.890248,6.613720,-8.651197,-6.286201,9.837001,2.972522,8.580017,6.372782,6.750113,-0.978002,-9.612574,-4.456104,8.614723,9.503149,5.420759,-7.129997,-0.110609,2.393167,7.679721,8.813559,-1.980336,-9.141004,0.421202,-3.278512,2.479359,5.694021,-7.497867,-9.226231,0.183689,3.758351,-3.479142,-6.036537,5.380353,5.285717,9.981155,4.544329,0.888139,7.110463,8.970409,-5.452132,-4.395009,-1.766570,3.785148,-3.595004,-4.841763,7.053822,2.234315,3.459290,-6.750132,9.582958,1.735309,7.861579,-8.501844,-8.574509,-0.691611,-6.528267,-1.634795,5.516087,2.123083,2.719540,5.045281,-7.672008,-7.779956,9.570289,8.521553,-8.291868,8.871746,6.150593,-2.965954,9.591808,-4.401454,-8.392510,-3.179684,1.279099,3.688771,8.746981,8.763827,-7.120122,4.793526,-5.346197,-3.191358,-5.798942,-7.708773,-9.682471,6.836076,-4.277761,6.017306,-6.759199,-0.369045,-3.853749,-5.106465,6.699989,7.670291,5.650567,9.471483,6.946927,-0.432363,-9.626259,-3.889756,-5.905936,-9.230411,3.060615,6.751853,-2.116279,5.275627,8.645961,-5.381684,-8.552525,-3.067403,9.505439,1.822474,-8.732632,-0.850620,9.555771,4.600347,-2.499911,-1.619703,0.233828,3.992854,4.804170,-8.275227,6.559764,3.180939,9.347050,3.823697,-6.287587,0.485026,9.967361,2.975928,-1.746844,-7.953383,-4.934175,1.545009,-0.386614,9.709035,7.410346,-8.554262,5.816149,-2.713367,-7.011552,9.029143,9.627247,8.052417,-0.332655,9.510424,2.259306,5.977055,-9.861159,6.465624,5.990460,-4.659103,5.933488,5.596254,3.449449,8.047812,-1.298094,-7.165062,1.574930,-6.574483,-6.557403,2.880431,8.758720,4.673233,0.058959,-1.019332,-7.090862,9.096843,2.384040,-7.643243,8.915762,-5.239843,-8.179538,9.222352,-9.632077,3.709895,5.572732,-4.990873,0.966580,-8.725781,9.615488,6.095433,6.963244,4.136444,-4.565194,2.373170,7.691184,5.547372,-6.196702,7.716406,-1.312715,6.113317,6.172286,-0.748738,-7.111856,1.662100,5.366306,9.921682,-1.081514,0.709527,-7.717484,-9.502810,9.036747,7.339502,-2.807258,-7.554541,6.089846,-1.233675,-6.006206,6.815879,4.625254,-7.003990,6.992352,5.446238,-3.627960,-2.235621,-6.057743,-8.128781,-5.998560,8.673000,-3.026593,1.882527,-8.897812,8.227718,-0.631240,9.769835,5.599692,-9.490142,5.781762,-6.471132,7.374638,-7.501336,0.526303,6.106049,-8.874770,-4.994994,-0.333266,-7.539995,7.504037,9.092752,-7.646322,6.755610,-8.255526,-3.942096,-8.289279,2.450020,-0.032412,1.597024,-5.236191,7.247137,9.448834,-3.620108,-9.607030,-9.737367,-3.618725,1.278831,-4.937798,-5.664348,0.231138,-3.229287,-3.603894,1.378295,4.570915,-0.407944,2.768385,-5.256691,-5.858573,-2.905951,0.647638,-6.789843,2.243874,-3.940348,4.017918,-1.202304,-4.363141,-5.202012,8.960710,6.027384,-2.897161,-8.644990,0.450838,-5.366242,8.636102,-9.098195,-4.001171,-2.027713,3.405753,1.780758,-0.922351,2.077417,8.926048,2.882366,1.166778,7.618745,-5.987312,2.672854,7.091214,0.978485,-2.703316,9.351830,1.712702,-7.698595,1.748428,2.937673,-7.557665,-3.975345,-2.072774,-6.277129,-5.762113,4.164979,0.585360,-6.192398,-5.283939,-2.487661,-7.545867,0.618338,7.341918,-5.754654,-4.720953,-2.503126,-6.953759,-6.567175,-9.668401,-1.650648,-6.019896,-0.899406,-8.404624,-0.214486,-4.491566,8.360697,1.964896,-0.111557,7.150037,3.906545,-3.309671,-7.644225,-3.368030,8.600757,0.963977,7.472437,9.415382,9.420766,-1.692566,0.069387,-7.594977,5.888276,8.232929,9.520706,-8.044622,-9.153397,-0.818502,4.204591,3.574186,-2.101979,-2.162731,9.944791,1.555373,8.544084,-7.859431,-2.902650,-7.714659,-5.847334,-3.293806,-6.348100,-9.020742,6.503330,6.815135,0.620955,-0.044863,6.175307,9.042963,-8.383761,6.385704,3.672754,-0.387753,9.431870,7.514617,8.156422,4.992215,3.654983,-9.792471,-1.268269,7.926362,5.282403,3.411043,1.280603,4.433104,2.800643,5.019678,-9.473608,3.730170,-7.185017,-3.123189,-5.263979,0.598505,4.299818,-4.846240,9.080938,-7.319046,9.571206,5.432827,-4.493533,2.807677,-7.478753,-1.490475,-7.513711,-1.822837,2.842070,-7.288798,-5.311339,0.450629,-6.027238,9.953758,8.993462,-6.222477,-6.610988,9.666026,-5.632821,-2.724360,-7.460403,2.575567,-3.968591,7.320077,-7.604892,7.385163,-8.080462,2.606822,7.634723,-3.886132,-5.715771,0.775999,3.699831,9.042236,7.695610,-8.086960,7.477670,8.822954,7.716074,4.939533,-2.266704,-6.474651,6.249468,1.974127,-1.598130,4.988294,-0.817669,7.937523,-6.319443,7.643869,7.143558,3.841298,-7.148031,-8.676324,5.611885,9.090081,5.233765,-4.581332,9.667012,7.416471,-5.542149,-9.508371,2.354517,-7.166793,9.527823,-6.959947,3.296674,9.042597,-0.181585,2.050011,1.984225,0.103076,-9.366217,7.512984,-0.934892,6.500178,4.821796,8.200791,-0.897747,-9.827720,-5.097969,-6.833481,-6.407758,7.627804,6.107793,1.043960,4.647903,9.823670,-8.514853,-1.421209,3.830801,9.908179,3.533148,-1.842092,-5.561567,6.461531,0.011458,-3.532896,4.863196,-8.878880,-5.597032,0.599698,-2.023533,6.828532,7.315914,0.506720], dtype = "float32")#candidate|8127|(2016,)|const|float32
call_8126 = relay.TupleGetItem(func_5293_call(relay.reshape(const_8127.astype('float32'), [2016, 1])), 4)
call_8128 = relay.TupleGetItem(func_5296_call(relay.reshape(const_8127.astype('float32'), [2016, 1])), 4)
func_5136_call = mod.get_global_var('func_5136')
func_5140_call = mutated_mod.get_global_var('func_5140')
var_8144 = relay.var("var_8144", dtype = "uint16", shape = (12, 4))#candidate|8144|(12, 4)|var|uint16
const_8145 = relay.const([-1.031340,-2.543413,2.045434,8.111137,-2.843986,-0.997652,4.745973,-5.564201,-7.720514,-7.243949,9.698668,-7.108839,-4.910675,-8.799314,3.509867,2.110153,-4.238260,-4.782406,-8.080784,3.981257,1.403683,-4.500031,-1.800803,-1.251725,-5.486936,1.361236,7.532436,2.541966,-7.321513,-9.781319,-0.604182,5.518694,7.220324,6.200508,5.709395,-0.202613,-0.683236,7.557322,0.777249,5.336264,-6.048996,9.963386,-5.721195,0.866174,-3.072618,6.769554,-7.279473,4.644505,-2.347493,3.431649,-7.994032,-3.878451,-1.597840,3.662945,-7.690446,8.410500,9.693008,-7.553491,-4.149002,-9.314418,2.620119,5.001849,-1.833946,4.452623,4.866966,4.256889,-5.267717,-4.958951,5.661687,-3.590571,1.308190,2.636793,-3.764022,-5.059579,2.989465,-3.213896,-4.417620,-6.046233,-1.517685,-2.962929,-0.528013,1.822973,9.820935,9.580422,8.972546,-5.961550,-5.903255,6.179400,-0.348267,3.311283,-2.076262,-9.473024,8.103130,-3.163924,8.174350,-5.228868,-9.088998,-0.699376,8.973040,-5.078499,-1.867284,3.129819,-5.841108,7.586000,7.942692,1.077285,-8.911453,-2.883348,-1.585938,-9.499714,6.096930,-6.583494,-0.856244,-7.316659,-7.969689,7.044195,1.960182,8.433628,7.542801,-6.437702,2.735151,0.414622,-8.515703,-4.942451,-4.588362,-8.197106,1.411733,3.242969,3.528891,4.319478,-8.224059,-8.089529,-5.167438,-4.472189,0.568588,-2.470783,-3.353393,-8.743148,4.707298,1.948268,2.672875,-1.680942,-0.516813,1.573240,0.142627,-8.398916,4.659566,0.971481,-2.122671,6.146142,2.457890,7.991962,0.254414,-0.301015,-4.536202,-1.278664,6.505837,-8.287504,-2.211101,2.719189,-4.188060,-9.806785,5.402935,9.775677,9.022751,7.819561,-0.842161,-7.805245,-1.266052,6.714258,-7.869393,6.734029,-8.211763,-2.758368,7.096767,-1.108137,1.806235,1.945939,-8.170954,-6.455952,5.578639,-7.202498,-3.821480,-0.816660,8.895808,2.754040,9.221671,7.247337,-8.853772,5.652555,-0.119519,-4.271133,-3.707755,-0.935400,-5.456680,-6.746249,-5.334873,-6.363821,8.514903,5.223415,-6.582156,-1.658761,0.564667,1.051580,4.612241,9.919033,-0.692771,5.664211,7.925221,5.360867,8.081349,-6.052944,9.651856,-1.954232,9.108150,9.523159,8.338554,8.617025,-7.470460,-8.656009,8.503507,5.029032,4.476493,-4.723705,-9.537863,4.718776,1.708614,3.214706,-5.617133,6.080953,4.391600,8.143914,6.677478,-4.488213,4.360859,7.131170,-5.331477,-1.684639,-3.583808,7.518961,-2.365806,-1.119849,-2.895947,-3.563866,3.038389,-7.141668,3.149873,4.841603,-8.297548,-3.592930,1.679567,5.452641,-5.184738,0.358660,-4.718157,8.532184,2.823177,8.817720,9.188949,-1.368263,0.016249,4.230719,-0.830014,6.567272,-7.954577,-5.860064,-3.555588,-0.766277,0.834513,4.051035,-8.308124,9.553795,-1.211723,3.349411,-3.177364,-9.138044,-6.341927,-8.199639,1.706595,5.647041,5.439227,0.002978,8.549435,-8.969692,5.496652,3.963660,-9.888609,-0.070569], dtype = "float64")#candidate|8145|(288,)|const|float64
call_8143 = relay.TupleGetItem(func_5136_call(relay.reshape(var_8144.astype('uint16'), [48,]), relay.reshape(call_8119.astype('bool'), [7, 16, 12]), relay.reshape(const_8145.astype('float64'), [288,]), ), 4)
call_8146 = relay.TupleGetItem(func_5140_call(relay.reshape(var_8144.astype('uint16'), [48,]), relay.reshape(call_8119.astype('bool'), [7, 16, 12]), relay.reshape(const_8145.astype('float64'), [288,]), ), 4)
var_8164 = relay.var("var_8164", dtype = "float32", shape = (2016,))#candidate|8164|(2016,)|var|float32
bop_8165 = relay.right_shift(const_8127.astype('uint32'), relay.reshape(var_8164.astype('uint32'), relay.shape_of(const_8127))) # shape=(2016,)
bop_8179 = relay.logical_or(bop_8165.astype('bool'), relay.reshape(const_8127.astype('bool'), relay.shape_of(bop_8165))) # shape=(2016,)
func_3922_call = mod.get_global_var('func_3922')
func_3923_call = mutated_mod.get_global_var('func_3923')
call_8182 = relay.TupleGetItem(func_3922_call(), 0)
call_8183 = relay.TupleGetItem(func_3923_call(), 0)
func_147_call = mod.get_global_var('func_147')
func_151_call = mutated_mod.get_global_var('func_151')
var_8195 = relay.var("var_8195", dtype = "uint32", shape = (560,))#candidate|8195|(560,)|var|uint32
call_8194 = func_147_call(relay.reshape(var_8195.astype('uint32'), [8, 5, 14]), relay.reshape(var_8195.astype('uint32'), [8, 5, 14]), )
call_8196 = func_147_call(relay.reshape(var_8195.astype('uint32'), [8, 5, 14]), relay.reshape(var_8195.astype('uint32'), [8, 5, 14]), )
func_5698_call = mod.get_global_var('func_5698')
func_5700_call = mutated_mod.get_global_var('func_5700')
call_8198 = relay.TupleGetItem(func_5698_call(), 0)
call_8199 = relay.TupleGetItem(func_5700_call(), 0)
output = relay.Tuple([call_8119,call_8126,call_8143,var_8144,const_8145,bop_8179,call_8182,call_8194,var_8195,call_8198,])
output2 = relay.Tuple([call_8120,call_8128,call_8146,var_8144,const_8145,bop_8179,call_8183,call_8196,var_8195,call_8199,])
func_8201 = relay.Function([var_8144,var_8164,var_8195,], output)
mod['func_8201'] = func_8201
mod = relay.transform.InferType()(mod)
mutated_mod['func_8201'] = func_8201
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8201_call = mutated_mod.get_global_var('func_8201')
var_8203 = relay.var("var_8203", dtype = "uint16", shape = (12, 4))#candidate|8203|(12, 4)|var|uint16
var_8204 = relay.var("var_8204", dtype = "float32", shape = (2016,))#candidate|8204|(2016,)|var|float32
var_8205 = relay.var("var_8205", dtype = "uint32", shape = (560,))#candidate|8205|(560,)|var|uint32
call_8202 = func_8201_call(var_8203,var_8204,var_8205,)
output = call_8202
func_8206 = relay.Function([var_8203,var_8204,var_8205,], output)
mutated_mod['func_8206'] = func_8206
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6180_call = mod.get_global_var('func_6180')
func_6181_call = mutated_mod.get_global_var('func_6181')
call_8231 = relay.TupleGetItem(func_6180_call(), 0)
call_8232 = relay.TupleGetItem(func_6181_call(), 0)
output = call_8231
output2 = call_8232
func_8240 = relay.Function([], output)
mod['func_8240'] = func_8240
mod = relay.transform.InferType()(mod)
output = func_8240()
func_8241 = relay.Function([], output)
mutated_mod['func_8241'] = func_8241
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8295 = relay.var("var_8295", dtype = "float64", shape = (11, 1, 8))#candidate|8295|(11, 1, 8)|var|float64
uop_8296 = relay.atan(var_8295.astype('float64')) # shape=(11, 1, 8)
uop_8306 = relay.asinh(uop_8296.astype('float64')) # shape=(11, 1, 8)
output = uop_8306
output2 = uop_8306
func_8319 = relay.Function([var_8295,], output)
mod['func_8319'] = func_8319
mod = relay.transform.InferType()(mod)
mutated_mod['func_8319'] = func_8319
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8320 = relay.var("var_8320", dtype = "float64", shape = (11, 1, 8))#candidate|8320|(11, 1, 8)|var|float64
func_8319_call = mutated_mod.get_global_var('func_8319')
call_8321 = func_8319_call(var_8320)
output = call_8321
func_8322 = relay.Function([var_8320], output)
mutated_mod['func_8322'] = func_8322
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7542_call = mod.get_global_var('func_7542')
func_7543_call = mutated_mod.get_global_var('func_7543')
call_8358 = relay.TupleGetItem(func_7542_call(), 0)
call_8359 = relay.TupleGetItem(func_7543_call(), 0)
output = call_8358
output2 = call_8359
func_8360 = relay.Function([], output)
mod['func_8360'] = func_8360
mod = relay.transform.InferType()(mod)
output = func_8360()
func_8361 = relay.Function([], output)
mutated_mod['func_8361'] = func_8361
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3642_call = mod.get_global_var('func_3642')
func_3643_call = mutated_mod.get_global_var('func_3643')
call_8403 = relay.TupleGetItem(func_3642_call(), 0)
call_8404 = relay.TupleGetItem(func_3643_call(), 0)
func_3986_call = mod.get_global_var('func_3986')
func_3991_call = mutated_mod.get_global_var('func_3991')
var_8414 = relay.var("var_8414", dtype = "int64", shape = (624,))#candidate|8414|(624,)|var|int64
const_8415 = relay.const([6.041624,4.475319,-4.203334,-5.074518,-6.293028,8.889402,-8.387625,-4.631592,-6.955402,-3.983491,5.935845,0.230863,5.379784,-0.918624,-8.643653,5.184818,3.337099,-4.681211,6.326242,-3.407589,9.582177,-1.397992,-8.480964,0.833743,1.872226,-9.967049,3.793790,-1.757422,1.976931,8.588678,4.295623,3.528976,-8.952696,-1.913683,-2.070636,6.696852,-2.168340,-9.586110,-5.439450,-4.301608,7.540165,-8.643059,-0.936641,8.302138,-5.634011,2.834723,9.270644,-1.166724,-8.909676,0.213350,-4.338039,7.228534,-4.898646,2.180152,3.530726,7.808097,-1.045240,1.633330,-6.490979,-9.344937,-7.760880,-1.389024,3.470536,4.870895,7.841468,-3.389594,2.227567,-6.798592,3.143990,-1.732333,6.697039,-3.436352,2.886766,-1.753460,-2.270020,-4.844633,1.233940,6.829465,-9.448141,-0.927986,3.613475,8.821451,-9.170076,1.587052,3.709455,1.970255,1.520503,3.764971,5.040193,-0.768784,-2.607796,-1.417342,3.834389,-7.249394,-5.306190,4.872286,-6.100574,-2.937967,-9.232916,-5.323907,7.898838,4.100721,4.263745,-0.604678,-6.902946,3.423546,4.530620,-1.415882,4.628802,-9.153768,-1.677889,6.981661,-6.022691,2.247169,7.793783,4.216542,4.406426,6.035737,0.770310,-6.326944,-7.205654,-5.817450,0.698993,-2.486119,-9.645880,8.968123,-1.178598,7.522053,-0.440387,-0.917452,-8.766458,6.855755,-3.796058,3.787956,-8.253863,3.866781,0.405193,-8.107710,3.048193,8.806309,-7.591084,-4.601234,2.521946,0.348466,-7.839747,-9.056531,1.578885,2.054318,-2.552830,9.764622], dtype = "float64")#candidate|8415|(150,)|const|float64
call_8413 = relay.TupleGetItem(func_3986_call(relay.reshape(var_8414.astype('int64'), [13, 12, 4]), relay.reshape(var_8414.astype('int64'), [13, 12, 4]), relay.reshape(const_8415.astype('float64'), [150,]), ), 1)
call_8416 = relay.TupleGetItem(func_3991_call(relay.reshape(var_8414.astype('int64'), [13, 12, 4]), relay.reshape(var_8414.astype('int64'), [13, 12, 4]), relay.reshape(const_8415.astype('float64'), [150,]), ), 1)
bop_8418 = relay.logical_and(var_8414.astype('bool'), call_8413.astype('bool')) # shape=(15, 10, 624)
bop_8421 = relay.logical_and(var_8414.astype('bool'), call_8416.astype('bool')) # shape=(15, 10, 624)
output = relay.Tuple([call_8403,const_8415,bop_8418,])
output2 = relay.Tuple([call_8404,const_8415,bop_8421,])
func_8432 = relay.Function([var_8414,], output)
mod['func_8432'] = func_8432
mod = relay.transform.InferType()(mod)
mutated_mod['func_8432'] = func_8432
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8433 = relay.var("var_8433", dtype = "int64", shape = (624,))#candidate|8433|(624,)|var|int64
func_8432_call = mutated_mod.get_global_var('func_8432')
call_8434 = func_8432_call(var_8433)
output = call_8434
func_8435 = relay.Function([var_8433], output)
mutated_mod['func_8435'] = func_8435
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6180_call = mod.get_global_var('func_6180')
func_6181_call = mutated_mod.get_global_var('func_6181')
call_8458 = relay.TupleGetItem(func_6180_call(), 2)
call_8459 = relay.TupleGetItem(func_6181_call(), 2)
func_6976_call = mod.get_global_var('func_6976')
func_6979_call = mutated_mod.get_global_var('func_6979')
call_8472 = relay.TupleGetItem(func_6976_call(relay.reshape(call_8458.astype('float64'), [2, 3, 14])), 0)
call_8473 = relay.TupleGetItem(func_6979_call(relay.reshape(call_8458.astype('float64'), [2, 3, 14])), 0)
func_7385_call = mod.get_global_var('func_7385')
func_7386_call = mutated_mod.get_global_var('func_7386')
call_8474 = func_7385_call()
call_8475 = func_7385_call()
func_6383_call = mod.get_global_var('func_6383')
func_6386_call = mutated_mod.get_global_var('func_6386')
var_8482 = relay.var("var_8482", dtype = "float32", shape = (176,))#candidate|8482|(176,)|var|float32
call_8481 = func_6383_call(relay.reshape(var_8482.astype('float32'), [11, 4, 4]))
call_8483 = func_6383_call(relay.reshape(var_8482.astype('float32'), [11, 4, 4]))
func_1386_call = mod.get_global_var('func_1386')
func_1390_call = mutated_mod.get_global_var('func_1390')
const_8486 = relay.const(-9.589565, dtype = "float32")#candidate|8486|()|const|float32
var_8487 = relay.var("var_8487", dtype = "float32", shape = (704,))#candidate|8487|(704,)|var|float32
call_8485 = func_1386_call(relay.reshape(const_8486.astype('float32'), []), relay.reshape(var_8487.astype('float32'), [11, 8, 8]), )
call_8488 = func_1386_call(relay.reshape(const_8486.astype('float32'), []), relay.reshape(var_8487.astype('float32'), [11, 8, 8]), )
output = relay.Tuple([call_8458,call_8472,call_8474,call_8481,var_8482,call_8485,const_8486,var_8487,])
output2 = relay.Tuple([call_8459,call_8473,call_8475,call_8483,var_8482,call_8488,const_8486,var_8487,])
func_8503 = relay.Function([var_8482,var_8487,], output)
mod['func_8503'] = func_8503
mod = relay.transform.InferType()(mod)
var_8504 = relay.var("var_8504", dtype = "float32", shape = (176,))#candidate|8504|(176,)|var|float32
var_8505 = relay.var("var_8505", dtype = "float32", shape = (704,))#candidate|8505|(704,)|var|float32
output = func_8503(var_8504,var_8505,)
func_8506 = relay.Function([var_8504,var_8505,], output)
mutated_mod['func_8506'] = func_8506
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7385_call = mod.get_global_var('func_7385')
func_7386_call = mutated_mod.get_global_var('func_7386')
call_8510 = func_7385_call()
call_8511 = func_7385_call()
func_6814_call = mod.get_global_var('func_6814')
func_6822_call = mutated_mod.get_global_var('func_6822')
const_8518 = relay.const([-2,-6,-2,7,9,-2,-10,-3,2,-2,-2,-8,1,-10,-9,-2,5,1,6,-1,-8,5,-1,7,-10,-2,1,3,-5,2,2,-8,10,6,7,-1,2,1,4,-9,-8,-1,10,8,-8,1,4,9,-9,10,-2,-1,8,-10,-1,-9,9,-5,-3,-6,3,1,9,1,-4,-3,3,3,-7,6,-1,6,-6,-10,-4,-1,4,-6,1,10,-10,4,-7,7,-9,2,9,-9,-9,-3,5,-1,6,-3,-7,-6,6,-10,-8,-6,1,6,-6,-4,-4,-9,1,-8,-7,5,4,1,-1,2,10,-6,-8,3,-7,-8,-4,-8,8,1,6,1,7,-9,-5,-8,1,-7,4,2,5,-10,8,3,5,1,-1,-5,-4,-7,-7,3,-8,-6,10,-4,9,-7,6,-3,5,-6,8,-7,6,-1,-10,9,-7,-2,5,6,-2,3,3,8,-1,6,-6,2,-8,2,-9,8,8,-3,-6,8,-1,5,-6,4,9,-9,-7,-6,-3,-5,-1,-6,-2,5,1,-3,4,-8,3,10,-4,-7,-7,5,3,-2,-2,-7,-1,-10,6,5,-3,2,5,-10,-10,-1,1,-9,-6,3,1,-4,-2,3,10,-10,10,-1,-4,5,7,1,2,4,-10,7,7,-4,-6,1,-4,10,-2,9,1,2,-10,8,4,1,1,5,-1,-8,-5,-4,-9,3,5,-9,-5,-6,5,-6,-8,-3,7,6,7,5,-3,9,3,-5,-3,7,-9,-5,-9,-1,8,-7,-2,-2,-8,-8,-6,-7,2,-9,8,5,1,2,-10,8,-9,-6,-9,-9,-5,-10,-8,10,-10,-5,5,6,9,-5,-2,-1,-7,1,3,-2,9,-9,-10,-6,-6,-9,-10,-4,-4,10,-1,7,9,-3,-10,-3,9,-7,-9,-9,4,7,-4,3,-1,6,-7,9,4,8,-6,-4,-1,6,-2,8,-5,-9,5,1,-8,-5,3,-9,-5,-1,-8,-8,4,10,10,-1,10,-6,-4,10,-5,5,10,-4,-2,7,-8,8,10,-9,5,-5,-1,-1,-7,7,7,-9,9,-3,-8,1,-7,1,1,6,-1,-3,2,-7,7,3,7,3,7,7,8,3,-8,-1,-4,5,9,-8,-3,10,-9,6,-8,2,-6,-1,6,8,-10,-5,9,10,9,7,-2,-4,3,-7,-10,4,-5,-10,3,-6,-8,-9,-2,-5,6,-3,-10,-9,8,1,4,-3,4,-1,3,2,-2,-10,-10,5,6,6,6,8,3,3,-7,-8,2,-10,1,-6,-2,5,-1,10,8,-3,1,-10,1,2,2,2,9,6,-5,1,1,9,-6,-9,-5,1,-4,-10,6,4,2,-9,10,-9,2,-2,7,4,2,-10,-4,5,-5,2,7,-9,-3,-7,8,8,9,-10,3,2,7,-4,-6,-10,4,-2,9,-7,4,5,-4,-9,-3,9,-4,3,2,4,-4,9,-8,8,-4,2,-3,-9,2,-9,-8,-2,9,6], dtype = "uint32")#candidate|8518|(560,)|const|uint32
const_8519 = relay.const([-1,6,-3,-3,-4,8,-5,4,7,2,10,-4,6,6,-9,4,1,2,-6,7,-3,7,5,2,7,7,7,10,7,5,-2,-7,-1,-1,5,-9,4,-6,9,-2,-5,-4,10,-6,-9,-6,10,-5,2,1,5,-6,8,-9,-4,-3,-10,9,-8,-9,-6,7,-8,-10,-2,2,3,-8,1,-7,-10,2,-7,2,-8,2,7,1,-6,10,1,5,9,4,5,-5,-2,-9,-9,-4,-3,2,-8,9,-5,-1,-8,-2,-2,-7,10,3,8,-2,-4,-8,3,-9,7,6,-7,-10,-3,-4,-1,-3,-2,4,10,-10,2,-1,10,-7,-10,-8,-10,-1,-5,10,-5,-8,3,8,-7,8,-6,6,1,-10,-8,7,9,3,-5,9,-7,-7,-8,-4,3,6,-2,-3,8,3,4,-4,-10,-4,-9,4,-1,-8,6,-3,5,8,4,2,7,-5,-5,-1,-5,9,1,2,6,8,-2,-3,-4,6,-4,-7,-4,-9,3,-4,-8,-2,8,-8,4,8,-1,-4,-4,1,9,-9,2,1,-2,4,2,9,-2,6,-5,3,-7,-10,-7,1,1,-8,1,-10,6,3,2,10,10,-9,2,10,-8,2,-3,3,6,7,-5,-10,-3,-1,-6,-8,-6,-3,10,10,4,-5,-7,-1,2,-10,-8,-7,5,3,-8,-10,-7,-5,-6,5,6,-9,8,6,1,-6,8,10,-3,9,-4,-8,-1,10,-5,-1,4,-4,3,4,-7,5,-8,-1,5,-4,10,-2,6,-10,6,4,3,-6,-9,10,-3,-3,7,-1,3,-5,-9,6,8,8,7,-8,9,7,-4,-4,-4,-7,-1,7,-6,-9,-7,2,-10,3,-10,10,-3,-7,-5,-4,-8,-2,-9,-6,-9,-2,9,6,-4,-9,-8,-6,-5,9,-6,1,-4,-4,1,-10,7,9,-7,7,3,-8,4,-3,-6,1,5,-7,-4,-4,5,7,7,7,-10,5,-10,-4,6,-3,10,-6,5,-4,8,-6,-3,2,9,-3,-4,10,-1,6,2,10,3,-6,1,7,-9,2,-6,-3,-6,3,7,3,8,5,-1,1,-3,2,7,5,4,8,-2,4,7,7,1,-2,-3,10,-4,-8,7,2,3,2,5,-7,10,4,-1,3,-2,2,4,9,-6,-6,1,9,-5,1,-10,6,2,-7,-2,-6,7,-8,-3,-8,6,-1,2,-8,10,9,-8,10,-7,-4,9,-1,-1,7,8,10,-9,-10,3,-8,-7,-1,-3,8,9,-7,3,5,9,-7,-5,-10,10,-5,-9,-5,1,-3,8,4,-3,-4,-9,10,10,4,4,10,-3,6,2,-8,9,9,3,5,-4,-4,-9,-2,10,4,1,10,1,-8,9,-7,-9,8,-10,10,3,9,-6,8,-9,4,6,-4,1,-9,-9,-1,-3,-10,3,6,-4,5,-6,-10,5,2,7,10,9,-10,-6,-7,-1,1,-9,-9,10,4,7,10,5,3,2,-2,3,-9,3,9,3,10,-6,4,1,5,-10,-9,-9,-9,-8,-9,-2,-1,4,-1,-1,-8,9,7,8,7,-5,4,-1,-4,-5,9,3,2,-1,4,-3,-10,-4,2,7,1,10,-7,-2,1,5,-3,-1,6,8,-3,-2,-3,8,-10,9,-8,-9,-9,7,6,-1,8,6,1,4,6,4,4,-9,8,6,-4,-2,-3,4,-9,-10,6,-3,-9,10,4,-7,8,5,-1,-4,5,1,-3,7,1,-10,-3,-3,-1,8,-8,6,-10,-4,3,7,1,5,-2,-7,10,-1,2,5,-6,1,-9,-2,9,7,1,9,1,-8,-6,7,4,-1,1,-2,-3,3,-9,9,8,-9,2,-2,1,8,-7,-5,5,9,-6,-5,1,8,-10,9,5,-8,5,-1,-2,-4,-8,-9,-9,-10,-9,-3,-10,2,10,-9,-9,-5,7,-1,-7,-7,7,9,-4,10,-2,6,6,4,-9,-2,-10,-5,2,-5,2,-7,9,5,-5,-9,-10,10,4,1,-5,-4,-9,-3,2,2,-1,4,-5,3,6,6,8,-1,8,-6,4,-9,6,5,-9,5,-6,-9,-8,10,6,-1,9,-5,-5,-3,10,3,3,5,3,-1,-8,9,-5,-1,4,-3,5,2,-10,10,-7,7,9,2,-3,2,-5,9,-1,-9,4,7,-4,1,4,-6,-4,-8,9,6,3,3,-10,-8,-3,-3,-2,8,9,-10,1,-3,10,-8,1,1,2,4,8,-3,10,10,6,6,7,10,3,-3,-5,2,-4,4,6,-10,-1,-5,-8,-2,3,4,5,10,-7,9,-5,-2,3,-7,-3,3,-9,-4,3,3,-6,-10,1,7,2,-4,8,-5,1,9,-8,-9,-1,6,-10,2,8,-7,1,-10,1,-1,9,9,10,5,10,-7,-6,-5,-5,-4,-10,-3,4,-7,9,-3,3,-8,10,3,5,1,4,-10,4,4,-3,-8,-2,2,-10,-10,9,-8,-9,-10,-2,8,8,6,1,9,-9,-3,-1,-4,3,6,2,-2,-6,5,-5,5,-10,9,-3,9,5,-6,-8,7,-6,3,10,7,10,-5,7,-2,3,10,8,-9,-3,1,-7,3,3,9,3,-1,-10,-10,4,-3,3,-2,-5,6,-8,-9,5,-8,8,-4,-5,-4,9,1,-5,-2,-10,-1,-7,-2,4,-2,1,-9,-7,-10,10,-9,-9,4,-7,-6,3,1,-2,7,-4,7,6,6,1,-8,-1,9,7,8,2,-10,-9,4,-4,9,7,5,4,-9,-7,-5,3,-2,9,-4,-4,-3,5,-8,8,9,5,-1,5,-5,8,-3,-4,-3,5,-2,-10,-5,4,-6,-3,2,-8,9,4,6,-4,6,3,10,5,-10,9,-3,-9,9,-3,1,3,-5,-4,2,-1,5,-6,-4,9,9,9,2,1,1,-2,5,4,4,-2,-5,3,-7,-7,1,6,3,-3,7,-6,-8,-3,-6,5,-5,4,-10,-2,-5,1,-2,-9,-4,9,4,10,-6,5,7,1,6,4,2,4,-2,7,-2,8,-7,-5,-4,5,7,-1,-7,-8,10,9,-5,-1,-8,2,7,3,-5,-6,-5,-9,8,-9,-6,10,-1,8,-3,-5,-1,8,7,1,4,-2,-8,-3,3,-3,-3,5,-1,-9,5,-5,3,4,7,-1,-1,-1,-4,-5,-8,-7,1,-2,8,7,9,10,7,1,9,6,5,-1,10,7,4,9,-8,10,-4,9,-10,5,-3,1,8,-4,-5,-3,8,-4,-4,10,4,5,-8,1,-3,7,-5,-8,6,-8,-6,5,-1,-8,2,4,-1,-3,-5,-9,3,4,4,2,5,-10,-3,5,-6,8,5,3,2,7,2,-6,1,4,-4,-7,6,-10,-4,2,1,7,3,4,-6,5,-8,-3,-10,6,3,3,-3,-10,-1,9,4,10,6,5,6,1,10,2,-1,6,-2,-3,5,3,8,7,-8,1,2,9,7,-1,4,-9,-4,8,5,2,-7,-5,7,-4,1,-10,-3,-3,8,7,1,-6,-2,-10,8,-6,-9,7,-3,2,8,10,-10,2,-1,10,7,-5,-2,8,1,4,-5,5,-4,5,-8,5,-8,-5,-8,-10,-5,-7,-2,-9,-9,2,-6,5,3,-3,-2,8,-7,-10,-2,-3,-7,-3,5,3,-5,-1,1,10,-3,4,5,-7,7,-9,-10,-5,5,6,-2,-6,-2,-7,-1,9,-3,-1,-5,1,8,10,-6,-2,4,1,-5,-2,-3,1,7,-10,-5,9,1,-3,-1,4,-9,-8,-4,-7,-7,-9,-10,-6,2,-7,9,6,-5,-7,-3,4,9,5,1,6,10,8,-6,7,2,-5,-10,-1,2,-1,-10,7,5,7,-3,-3,8,5,6,4,-5,-9,1,-10,-9,-8,-6,-10,-6,-6,-2,3,2,4,7,-6,-6,-7,-6,-10,8,3,4,4,2,8,-10,-4,7,10,7,-8,4,1,-4,6,10,5,-3,-3,-8,-9,-4,-3,-10,-6,-1,-9,2,5,-3,-6,-10,-9,10,10,-5,-8,-1,-9,-2,-7,1,-7,7,7,-3,-5,5,-8,5,5,-8,-8,-4,9,4,-10,-3,8,-9,2,-9,6,8,-1,1,-3,-8,7,10,7,-1,6,4,-4,8,-4,2,5,4,-4,-1,-4,-10,3,7,1,-7,-2,3,-3,-1,-2,-8,4,2,-7,-5,-3,3,4,-6,-8,3,3,5,1,-4,10,7,-4,-3,1,3,2,2,6,10,10,-3,1,10,5,-2,-5,-2,-9,9,1,-6,8,1,-3,-7,4,7,-9,9,10,-2,2,4,-8,-1,-5,-4,-4,-6,-5,1,4,-7,6,8,7,3,-5,-3,9,2,3,-6,10,-4,-6,4,-7,-4,7,1,3,5,2,-1,-4,-7,-8,1,-5,-2,-4,-1,-7,3,9,10,-9,-10,-5,-4,-3,-5,3,8,5,-1,8,1,10,-1,-10,-9,-10,-10,9,5,6,-2,7,9,1,10,-5,-5,5,-2,-9,-5,-1,3,10,1,-7,5,4,-6,5,4,-9,6,7,10,-10,-6,-10,2,-8,-6,-5,-8,6,-4,2,-2,7,6,6,1,-10,9,-5,-2,4,-7,-10,8,1,-6,9,3,-5,-9,6,9,6,-8,10,5,9,-3,-9,2,4,-2,-5,9,5,-1,10,6,9,-1,5,3,8,-2,10,6,1,8,-4,-4,-7,-9,-6,-4,-1,5,9,-10,5,-5,-6,-10,-8,1,-5,8,-1,-8,-3,3,7,10,6,-4,-1,-8,9,-4,-6,8,3,3,4,2,-4,-9,-4,9,-10,3,-4,-8,8,-10,8,-4,-4,6,8,5,-4,-5,5,8,-8,7,-1,5,-1,-4,2,2,6,-6,-6,8,-5,-8,-8,-8,-7,-6,-1,10,5,3,-3,-7,-10,5,4,-6,10,-1,-10,3,-3,-8,2,-8,-1,6,5,2,6,3,-3,-9,5,-1,7,2,5,-8,-5,5,7,-9,5,-8,-9,1,10,-6,7,9,1,6,1,-4,10,4,1,8,5,6,-6,7,-4,2,10,7,-3,9,9,-10,-3,6,8,-9,-1,8,-2,5,9,1,-7,5,3,3,9,9,-10,5,9,10,1,-9,-2,-2,10,-2,-10,-6,-1,5,4,2,-8,-9,-1,1,6,6,2,1,-9,-10,10,-4,-7,-10,2,3,9,1,3,-3,-1,9,4,5,2,4,3,4,-6,1,8,-10,-7,8,-4,-1,9,6,1,-9,-1,7,-1,-4,-7,7,-10,-2,-9,-1,1,-5,3,6,-7,10,-7,1,-10,-7,1,-2,-2,-2,-7,3,6,-10,1,4,2,5,-1,-9,1,-7,1,-5,-6,-3,9,-2,-4,-3,-10,-7,1,2,-10,4,-9,6,-2,1,8,-2,-10,10,-9,-2,-10,-1,-3,-4,6,-4,8,-4,-1,-2,-1,-3,-1,8,8,10,9,2,8,4,-3,-10,-8,-3,1,7,-2,-4,5,-4,2,-2,9,4,9,3,8,-3,8,-5,-3,-1,-3,7,-7,-1,-9,1,-7,7,-4,-6,-4,9,6,8,-4,-6,4,-3,6,-9,6,-5,4,9,-2,10,-3,-7,3,-10,-6,4,-10,10,-2,3,8,3,9,2,6,-7,-3,9,2,2,8,6,4,7,7,-6,-7,-9,-10,10,-4,-4,-3,-2,-6,1,-8,-3,-6,-8,2,8,-2,8,7,-5,-6,8,4,4,-2,-4,-3,5,-9,2,9,-1,-6,-1,8,6,5,-3,3,6,2,10,-7,7,-9,7,7,-7,8,8,5,10,-5,8,-10,-5,-6,-10,-9,-9,3,6,-6,5,-2,10,6,-7,2,-10,10,7,-10,9,3,10,5,-8,-9,-5,-7,-8,4,3,-9,-10,-10,-6,-5,2,6,6,7,4,-8,-9,-1,-9,2,-1,-4,-3,10,-5,-6,-3,-10,-6,2,7,9,8,-4,-7,8,9,-10,8,-2,5,1,-2,6,10,-10,-1,-2,8,-5,-2,4,-6,-2,4,-7,-3,8,1,-5,-3,5,-3,2,-5,-6,-1,6,5,-10,-5,-10,7,-6,-10,-7,-6,-9,-1,10,-10,-3,-7,6,1,2,5,4,10,8,3,-4,-10,-9,4,7,8,-2,-10,-8,6,-5,-4,1,-1,3,-4,4,-2,5,2,7,-3,-4,9,4,-2,6,-9,9,6,5,-10,4,-2,7,2,-2,7,7,-10,3,1,-9,6,4,1,-4,8,5,6,2,6,-2,-3,-8,2,-4,-3,-7,10,-3,-9,-2,-4,7,-8,9,-6,-6,-1,-10,8,-10,-7,-9,6,-8,10,4,-8,5,9,-10,6,3,-2,4,7,10,9,-2,3,2,1,-7,-6,-3,-8,-1,10,-4,5,2,-2,-9,-4,-7,-1,10,6,1,2,8,-8,6,1,10,-10,1,9,-2,-8,-1,8,3,9,-6,9,-10,-1,6,-6,9,1,7,-9,-4,-8,8,-4,-1,-4,-3,1,9,-2,7,1,6,-7,3,-2,2,2,7,10,1,7,6,-9,-3,10,-1,-5,3,9,-7,-5,-2,-9,-2,-7,5,-9,3,6,1,3,4,-8,-1,7,10,6,-8,1,6,-5,3,1,-3,9,10,-5,-1,3,4,9,-1,-5,2,9,5,10,-9,1,8,6,-1,2,8,5,7,-5,9,-7,8,-10,1,9,10,2,10,-6,2,5,5,-1,6,-1,6,7,-6,-4,-8,9,-3,-8,10,5,1,-2,-2,9,9,-2,-9,-8,7,-4,-7,4,3,-4,-3,-6,9,-1,1,8,1,4,8,-7,-5,9,-1,5,-5,8,8,-2,-2,-9,-6,-2,6,9,7,10,-6,-8,-3,2,10,6,7,-4,-5,-3,-9,-8,-10,-8,4,1,-8,-8,9,-9,-1,6,4,-7,4,-10,5,-5,-8,10,-2,1,-9,9,8,-9,-2,8,-7,-7,-5,2,-8,4,4,9,6,-6,-8,5,2,8,8,-3,3,8,8,9,-8,3,7,-8,1,-10,-8,8,8,7,2,-3,-10,2,-2,6,-3,4,1,3,-7,-3,-7,-6,-7,-2,-4,5,-5,-4,7,7,-10,-10,-4,-5,7,5,-8,-8,5,-5,5,3,-4,-9,6,3,-8,7,9,10,-9,-9,-5,2,-6,-8,-5], dtype = "uint8")#candidate|8519|(2704,)|const|uint8
const_8520 = relay.const([[2.115288,-5.899843,-5.792732,9.789132,-8.891399,6.882429,-8.849893,9.396699,4.479790,-3.271658,7.523910,8.002486,3.483081,9.917197,0.311071,-4.646857,2.668358,-8.234730,-6.256041,-2.880360,2.339865,-6.116294,4.504102,1.841702,4.594092,8.198900,9.986073,7.721185],[6.568765,-5.042180,9.793520,1.766830,8.585815,7.767161,7.089331,-1.624351,2.741267,-0.561415,-9.313380,2.853984,7.465686,-0.882528,5.656464,2.500379,-1.512364,6.277673,-7.745913,-6.649715,-5.829632,2.301419,7.050463,1.586750,-4.350484,-3.294293,4.624555,-7.853982],[-9.094869,4.123217,-9.247418,-3.152833,-8.385987,5.534163,-2.551021,6.877765,1.686009,-2.174046,-3.928143,4.861681,7.241460,-5.866898,5.059828,0.578645,2.653047,4.256984,9.807767,3.037960,6.270532,-1.631449,-7.315342,-1.995169,-7.995556,7.244809,-1.572146,2.871810],[-0.175460,-0.005504,-4.755442,1.986648,-4.538100,-3.794515,-0.730961,-6.398296,-9.676033,1.562643,-0.312185,-2.879462,-5.986080,1.158106,-2.124325,-2.134941,-8.388545,-7.814908,-7.372949,2.164904,-8.809516,-2.662971,3.756702,-1.002967,5.644049,-8.616282,4.316418,-6.827948]], dtype = "float32")#candidate|8520|(4, 28)|const|float32
var_8521 = relay.var("var_8521", dtype = "int64", shape = (260,))#candidate|8521|(260,)|var|int64
var_8522 = relay.var("var_8522", dtype = "int64", shape = (1792,))#candidate|8522|(1792,)|var|int64
var_8523 = relay.var("var_8523", dtype = "bool", shape = (12,))#candidate|8523|(12,)|var|bool
call_8517 = relay.TupleGetItem(func_6814_call(relay.reshape(const_8518.astype('uint32'), [4, 140]), relay.reshape(const_8519.astype('uint8'), [2704,]), relay.reshape(const_8520.astype('float32'), [112,]), relay.reshape(var_8521.astype('int64'), [260,]), relay.reshape(var_8522.astype('int64'), [2, 896]), relay.reshape(var_8523.astype('bool'), [12,]), ), 0)
call_8524 = relay.TupleGetItem(func_6822_call(relay.reshape(const_8518.astype('uint32'), [4, 140]), relay.reshape(const_8519.astype('uint8'), [2704,]), relay.reshape(const_8520.astype('float32'), [112,]), relay.reshape(var_8521.astype('int64'), [260,]), relay.reshape(var_8522.astype('int64'), [2, 896]), relay.reshape(var_8523.astype('bool'), [12,]), ), 0)
output = relay.Tuple([call_8510,call_8517,const_8518,const_8519,const_8520,var_8521,var_8522,var_8523,])
output2 = relay.Tuple([call_8511,call_8524,const_8518,const_8519,const_8520,var_8521,var_8522,var_8523,])
func_8526 = relay.Function([var_8521,var_8522,var_8523,], output)
mod['func_8526'] = func_8526
mod = relay.transform.InferType()(mod)
mutated_mod['func_8526'] = func_8526
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8526_call = mutated_mod.get_global_var('func_8526')
var_8528 = relay.var("var_8528", dtype = "int64", shape = (260,))#candidate|8528|(260,)|var|int64
var_8529 = relay.var("var_8529", dtype = "int64", shape = (1792,))#candidate|8529|(1792,)|var|int64
var_8530 = relay.var("var_8530", dtype = "bool", shape = (12,))#candidate|8530|(12,)|var|bool
call_8527 = func_8526_call(var_8528,var_8529,var_8530,)
output = call_8527
func_8531 = relay.Function([var_8528,var_8529,var_8530,], output)
mutated_mod['func_8531'] = func_8531
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8598 = relay.var("var_8598", dtype = "float32", shape = (12, 16, 14))#candidate|8598|(12, 16, 14)|var|float32
var_8599 = relay.var("var_8599", dtype = "float32", shape = (12, 16, 14))#candidate|8599|(12, 16, 14)|var|float32
bop_8600 = relay.floor_mod(var_8598.astype('float32'), relay.reshape(var_8599.astype('float32'), relay.shape_of(var_8598))) # shape=(12, 16, 14)
uop_8624 = relay.asinh(var_8599.astype('float32')) # shape=(12, 16, 14)
uop_8626 = relay.asin(uop_8624.astype('float32')) # shape=(12, 16, 14)
output = relay.Tuple([bop_8600,uop_8626,])
output2 = relay.Tuple([bop_8600,uop_8626,])
F = relay.Function([var_8598,var_8599,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_8598,var_8599,], output2)
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
