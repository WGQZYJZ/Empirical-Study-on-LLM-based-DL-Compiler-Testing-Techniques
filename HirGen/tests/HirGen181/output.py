import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_116 = relay.var("var_116", dtype = "uint64", shape = ())#candidate|116|()|var|uint64
var_117 = relay.var("var_117", dtype = "uint64", shape = (3, 12, 7))#candidate|117|(3, 12, 7)|var|uint64
bop_118 = relay.multiply(var_116.astype('uint64'), var_117.astype('uint64')) # shape=(3, 12, 7)
uop_129 = relay.sin(var_117.astype('float32')) # shape=(3, 12, 7)
output = relay.Tuple([bop_118,uop_129,])
output2 = relay.Tuple([bop_118,uop_129,])
func_137 = relay.Function([var_116,var_117,], output)
mod['func_137'] = func_137
mod = relay.transform.InferType()(mod)
mutated_mod['func_137'] = func_137
mutated_mod = relay.transform.InferType()(mutated_mod)
func_137_call = mutated_mod.get_global_var('func_137')
var_139 = relay.var("var_139", dtype = "uint64", shape = ())#candidate|139|()|var|uint64
var_140 = relay.var("var_140", dtype = "uint64", shape = (3, 12, 7))#candidate|140|(3, 12, 7)|var|uint64
call_138 = func_137_call(var_139,var_140,)
output = call_138
func_141 = relay.Function([var_139,var_140,], output)
mutated_mod['func_141'] = func_141
mutated_mod = relay.transform.InferType()(mutated_mod)
const_293 = relay.const([[[3.994498,-4.207818]],[[-1.722991,-6.651808]],[[0.066366,-1.467353]]], dtype = "float64")#candidate|293|(3, 1, 2)|const|float64
uop_294 = relay.atan(const_293.astype('float64')) # shape=(3, 1, 2)
func_137_call = mod.get_global_var('func_137')
func_141_call = mutated_mod.get_global_var('func_141')
var_301 = relay.var("var_301", dtype = "uint64", shape = ())#candidate|301|()|var|uint64
var_302 = relay.var("var_302", dtype = "uint64", shape = (1, 252))#candidate|302|(1, 252)|var|uint64
call_300 = relay.TupleGetItem(func_137_call(relay.reshape(var_301.astype('uint64'), []), relay.reshape(var_302.astype('uint64'), [3, 12, 7]), ), 0)
call_303 = relay.TupleGetItem(func_141_call(relay.reshape(var_301.astype('uint64'), []), relay.reshape(var_302.astype('uint64'), [3, 12, 7]), ), 0)
output = relay.Tuple([uop_294,call_300,var_301,var_302,])
output2 = relay.Tuple([uop_294,call_303,var_301,var_302,])
func_311 = relay.Function([var_301,var_302,], output)
mod['func_311'] = func_311
mod = relay.transform.InferType()(mod)
var_312 = relay.var("var_312", dtype = "uint64", shape = ())#candidate|312|()|var|uint64
var_313 = relay.var("var_313", dtype = "uint64", shape = (1, 252))#candidate|313|(1, 252)|var|uint64
output = func_311(var_312,var_313,)
func_314 = relay.Function([var_312,var_313,], output)
mutated_mod['func_314'] = func_314
mutated_mod = relay.transform.InferType()(mutated_mod)
var_335 = relay.var("var_335", dtype = "uint16", shape = ())#candidate|335|()|var|uint16
const_336 = relay.const([[[9,5,-2,9,-8,2,-1,-1,1],[1,-4,-10,5,5,4,-6,-5,9],[8,3,-6,-2,-3,6,-7,-3,-1],[3,-8,-2,8,5,10,3,4,6]],[[10,-9,-10,-9,1,8,-3,-8,7],[3,-7,-1,6,5,-7,-2,-8,1],[5,5,-2,-5,-1,-7,-2,-6,-1],[-6,-10,-7,-3,-5,1,8,-8,1]],[[5,-8,-1,-7,-5,2,1,-5,2],[-9,4,-5,-1,-10,-8,-10,6,-1],[3,10,2,-8,-3,-5,6,1,7],[-4,10,7,2,3,5,7,-4,8]],[[2,-1,8,9,8,-3,-7,-3,-8],[7,8,-1,3,-3,-6,3,4,4],[-7,-5,2,-10,-4,6,-3,-5,2],[-6,-6,2,-9,-2,6,-4,-9,-10]],[[8,2,2,5,10,8,7,-8,2],[-5,-2,5,-2,-3,-9,-4,4,10],[-3,-3,6,6,5,6,-4,10,1],[6,-6,4,3,-2,-3,4,7,8]],[[7,9,-10,1,8,-9,-9,-2,-5],[10,-6,6,-5,5,6,-7,9,-8],[3,-2,3,1,8,4,-2,3,7],[9,-10,5,-8,-2,8,-6,9,3]],[[-1,1,8,3,2,-9,-7,-10,-3],[-6,7,5,-8,-6,1,9,4,1],[7,-3,2,-7,-10,-8,10,-3,-2],[2,-1,8,-10,4,-9,7,9,-5]]], dtype = "uint16")#candidate|336|(7, 4, 9)|const|uint16
bop_337 = relay.not_equal(var_335.astype('bool'), const_336.astype('bool')) # shape=(7, 4, 9)
uop_355 = relay.sqrt(const_336.astype('float32')) # shape=(7, 4, 9)
output = relay.Tuple([bop_337,uop_355,])
output2 = relay.Tuple([bop_337,uop_355,])
func_357 = relay.Function([var_335,], output)
mod['func_357'] = func_357
mod = relay.transform.InferType()(mod)
var_358 = relay.var("var_358", dtype = "uint16", shape = ())#candidate|358|()|var|uint16
output = func_357(var_358)
func_359 = relay.Function([var_358], output)
mutated_mod['func_359'] = func_359
mutated_mod = relay.transform.InferType()(mutated_mod)
const_413 = relay.const([[[10,7,-10,-6,7,7,10,3],[6,-8,10,-3,-10,-4,5,-7],[2,2,2,5,4,1,8,9],[7,8,9,-2,2,-8,-8,10],[8,1,2,1,8,9,-8,-1],[-6,-6,-10,6,4,1,-8,3],[-4,7,-2,3,-2,7,1,-7],[-7,-3,-1,1,10,9,-2,3],[-7,-4,-1,-9,9,5,4,-10],[6,9,2,-5,1,-2,6,-1],[-8,-4,-3,-3,10,6,-1,6],[8,7,5,-4,-7,9,2,8],[6,10,-6,-4,1,10,-4,1],[2,-4,1,-3,-6,2,4,-7]],[[-2,10,10,-4,-3,6,3,-1],[-5,-3,-5,-5,-9,-9,4,3],[-3,-6,6,5,-6,-7,8,5],[-3,2,-3,8,-1,-4,3,3],[-2,-8,-10,-10,-5,7,-4,-7],[-1,6,-5,7,-1,10,-10,-1],[-5,1,-3,-4,-7,-2,-3,10],[9,9,2,7,-9,-9,-2,-9],[9,-4,10,-1,-9,8,3,8],[-3,3,3,9,8,8,8,9],[-9,10,-1,8,5,1,-5,-9],[6,-6,-5,-10,4,-5,7,-2],[8,-8,4,-8,4,-10,-2,1],[-2,-6,3,9,2,-2,9,7]],[[-5,-6,-1,-1,-8,7,-9,-6],[5,-9,8,6,4,-10,3,8],[-2,-8,-1,-9,-9,8,3,2],[-6,6,10,5,-1,7,-2,-1],[-1,7,-7,2,-3,7,-4,5],[1,5,5,-7,5,-2,3,1],[-4,8,7,9,-10,-7,7,-4],[5,-2,-9,1,-7,3,6,-5],[-4,-4,-3,-10,-1,-7,1,7],[-1,10,-1,8,-4,7,-4,-2],[5,9,9,3,8,-8,-1,7],[-5,-4,10,4,2,7,4,-4],[7,1,3,-8,3,-10,-3,8],[7,-6,-3,-2,4,1,-1,10]],[[-10,-4,4,6,9,2,6,-4],[2,-10,2,2,-1,5,9,8],[4,-6,5,6,9,-10,9,-8],[3,8,9,-3,-2,-10,4,2],[-1,8,2,2,5,-6,5,5],[-3,-5,-2,1,-9,-7,-9,2],[-9,8,6,3,-3,6,-5,5],[-6,8,-1,4,-10,-4,1,-10],[6,-2,-9,6,5,9,-4,10],[7,2,9,-9,-8,-9,-8,-1],[-9,9,-5,-10,-8,2,3,4],[10,-7,5,-7,8,-3,-6,-1],[5,-3,-6,3,-9,-5,-7,-4],[8,-5,9,5,-9,-6,-1,8]],[[-8,8,-3,7,8,-6,-3,-1],[2,-2,-9,8,5,2,10,4],[10,-3,5,-5,-4,-7,1,-7],[-7,4,8,-3,-6,9,-7,-6],[-4,-2,-9,-1,7,-1,9,1],[-9,-3,7,-1,3,10,4,-6],[5,9,-4,8,-2,4,-6,-9],[-10,-3,-10,-1,-8,-2,-7,3],[8,-7,-4,-6,3,-10,-4,4],[-1,2,-5,4,-2,-8,-7,-10],[-2,-7,-1,5,-4,-10,5,-4],[-5,8,9,-5,-10,-9,-1,4],[-5,4,-8,7,5,10,-3,6],[3,10,-8,3,6,-7,-1,4]],[[3,-10,-8,-3,-4,3,-9,7],[-3,-4,-2,10,-8,-6,-9,-3],[-8,-5,9,9,3,3,1,6],[7,-4,6,4,3,3,10,-6],[8,-5,9,10,-8,-4,1,2],[9,-6,1,10,-9,6,6,10],[-1,-1,-10,2,4,-8,5,2],[5,-10,-7,10,1,7,-8,-3],[3,1,5,-3,9,-3,-9,-8],[-4,-1,-7,8,7,-7,-4,3],[-4,-1,8,-7,3,-9,6,9],[8,-10,-10,-2,6,3,-10,5],[3,-3,10,-7,-10,5,6,6],[3,8,6,4,1,-4,-4,-5]],[[7,-7,7,-9,-10,3,-8,9],[-6,-7,-9,8,8,1,1,8],[-3,4,-9,-7,7,7,10,9],[5,10,-6,-5,10,-6,-3,10],[9,8,-7,7,4,9,9,9],[5,9,-8,8,10,1,-10,9],[-3,7,1,-3,-9,-8,4,2],[9,-1,-4,6,-2,-7,-6,-2],[-5,-10,-5,3,7,2,-1,1],[8,8,10,7,-1,-6,5,5],[-9,8,7,-7,3,10,-6,3],[-2,7,4,-7,8,-9,3,5],[-10,7,-2,-6,6,8,-4,7],[1,9,7,10,1,-10,-7,6]],[[6,7,-8,5,-6,7,6,-9],[7,4,-3,-1,6,-9,-6,10],[-6,2,-9,-7,1,-6,-7,6],[2,8,-4,2,-2,-5,-3,2],[4,-3,-2,6,4,2,7,-3],[-6,6,2,4,-6,2,-7,-1],[10,-2,6,-8,1,10,-8,9],[-8,5,-1,-3,1,-10,-2,7],[-7,-6,6,3,-6,5,10,7],[9,7,5,8,-7,-4,1,3],[-10,-9,5,-4,-7,-4,-5,4],[-4,-3,-10,5,-1,-6,-10,-10],[-10,-7,-3,5,-1,6,1,-7],[10,6,-5,9,1,10,-6,2]],[[-9,8,-9,3,-3,4,-8,9],[-5,10,-5,7,4,-5,-6,-4],[-7,9,7,-6,1,-4,-4,-9],[-5,8,5,6,-3,-10,10,-7],[8,3,-8,-10,2,7,7,5],[-4,4,10,-9,-10,5,-4,-7],[6,2,10,4,3,7,7,4],[7,-3,5,-4,-2,5,9,10],[5,-1,1,-8,-7,6,9,7],[5,4,1,-7,5,9,-5,1],[-9,6,8,-6,-6,-8,4,10],[-5,-1,2,-9,9,3,5,5],[-6,5,4,-8,-6,7,4,-9],[-4,5,-8,5,10,-5,-3,10]],[[3,3,7,-8,-10,2,2,2],[4,4,-2,3,-8,-9,-1,8],[4,-1,-5,-5,4,6,3,-4],[5,-2,6,1,4,-2,-10,-8],[4,-9,-10,1,-4,-2,4,5],[-3,-8,-2,2,10,-10,-6,7],[8,8,-10,4,7,2,-3,3],[-6,6,10,2,1,2,-10,9],[7,-8,6,3,-9,7,6,7],[-10,7,-10,-2,1,-8,5,1],[-5,-10,-2,-6,-10,2,-2,-5],[9,-4,1,9,2,-4,-7,10],[7,-2,-3,-9,-1,8,-9,6],[6,-8,6,2,-7,6,3,-7]],[[-5,1,-9,-8,3,-4,10,-2],[-7,-5,10,-4,4,-2,-5,-9],[-7,-8,-3,7,-4,-8,-8,-3],[1,-2,7,-7,-6,-10,-7,3],[1,10,-8,10,5,-6,-8,-10],[9,1,5,-7,-8,-4,-7,-7],[-6,2,4,-6,10,4,3,9],[5,7,10,3,-10,1,3,4],[6,3,-6,1,-5,5,8,-1],[4,4,-10,9,5,-7,-1,8],[-7,-9,2,-10,-4,6,-9,-6],[-2,6,-1,-4,-7,5,-2,-5],[-5,-1,-6,-5,-5,4,-7,6],[3,5,-9,10,-8,3,-7,-8]]], dtype = "int32")#candidate|413|(11, 14, 8)|const|int32
const_414 = relay.const([[[10,2,4,7,-7,-4,-7,-10],[-10,-8,-4,7,8,6,4,5],[7,-5,9,9,-2,4,7,-10],[9,-5,2,2,9,-8,-7,-8],[-8,7,7,-5,8,-10,3,4],[-9,-6,-1,1,-8,5,-1,2],[-8,-9,5,-5,3,-2,7,-10],[-4,-7,7,-7,8,2,8,9],[3,2,1,-2,1,1,-7,4],[9,8,-1,3,-10,-9,9,4],[-5,9,-2,-10,-5,2,-2,-5],[10,-9,2,-2,-6,-1,-10,-8],[-1,-1,-8,-9,2,6,10,6],[-7,-2,-4,-1,7,7,9,2]],[[-4,7,4,4,-7,-1,-2,-6],[-10,9,-7,6,2,-1,1,-3],[8,7,-3,-9,3,-7,7,-5],[-6,-10,-5,-6,4,-8,-5,-9],[10,-5,9,5,-4,-9,8,7],[-8,-8,5,-10,3,3,-10,1],[10,-2,9,-1,2,5,3,5],[-9,4,6,3,3,-7,8,-2],[-3,-7,4,9,-9,-5,8,-6],[2,3,6,-9,-1,10,6,8],[-8,6,-5,7,1,8,1,-6],[-6,3,4,10,8,-7,-4,6],[9,4,-6,8,3,5,-2,9],[2,9,-3,3,1,-8,4,6]],[[3,-7,-3,6,-3,-1,4,4],[-3,-3,-3,2,4,-8,-3,2],[-6,-6,-8,-4,3,-7,-7,-2],[5,9,-2,2,10,-6,8,-8],[9,-5,6,9,7,6,-8,-6],[-6,10,5,-3,4,5,-7,6],[9,-4,-3,4,-8,5,1,-8],[-6,4,-10,6,6,8,6,-1],[7,10,8,-1,-4,-2,-6,1],[-9,-3,4,7,-1,-5,-10,2],[4,9,-7,8,-7,-6,3,4],[4,2,-7,10,-3,6,3,-3],[1,-9,-2,-10,9,1,5,3],[5,9,-4,1,-4,-3,7,2]],[[-9,8,7,-2,6,-8,1,2],[9,-1,10,2,-10,-1,-10,9],[-5,1,-5,-10,-6,-1,2,-6],[-7,-3,8,-3,10,-7,8,-10],[-3,6,-5,8,-9,-2,-4,-1],[3,10,-7,4,-8,8,9,10],[2,-9,-6,-10,-5,5,1,2],[10,-9,-4,6,4,-9,-3,-4],[-9,-2,9,10,-6,-5,1,-3],[9,9,3,-7,-1,-9,-7,9],[-7,3,-7,-1,-7,10,-6,-10],[4,-10,5,3,8,-10,8,-3],[4,-10,8,-6,8,5,-10,8],[-4,-1,10,5,-10,2,-8,-1]],[[-2,5,-2,5,8,1,2,-2],[-2,7,8,7,-9,-6,-8,3],[-9,8,-1,9,-2,9,-4,2],[5,5,3,3,-4,1,7,-10],[2,8,-2,5,9,-9,5,6],[-3,5,-4,-8,-7,-10,4,-1],[-9,-2,-5,-4,8,-9,5,3],[8,-3,-6,3,-1,6,-3,4],[5,1,-2,6,8,-3,1,-10],[5,3,4,3,-7,3,-7,1],[4,3,9,-5,5,10,5,-6],[5,2,-3,9,7,3,-10,7],[6,-9,9,2,2,-1,5,-9],[-5,2,-7,2,-2,7,9,5]],[[4,-2,7,-7,9,-8,-3,5],[-8,-10,7,-1,8,4,-2,5],[-4,-8,-3,10,3,4,-4,8],[7,7,1,-6,5,-6,-8,4],[-8,-3,-9,2,-10,10,7,-6],[-9,10,-2,-8,-4,-6,7,-6],[-2,7,1,-3,-8,-7,-4,-9],[9,-2,-6,7,-7,4,-3,-3],[9,-6,9,-5,6,-2,-6,-3],[2,5,-6,-10,5,10,-4,3],[-3,6,-10,-9,-3,-7,3,6],[-5,-5,-1,-5,1,-4,-8,-10],[6,3,7,2,-4,-10,9,2],[5,5,4,-4,-7,10,3,-8]],[[-6,-5,-4,4,8,-5,-10,-2],[-6,-4,-9,5,-5,5,3,-9],[6,-1,-2,8,-8,8,-2,4],[-7,10,5,4,-8,-9,2,-1],[3,9,-6,-7,2,2,-6,-3],[5,1,-9,-1,5,10,-10,-8],[-3,-10,5,-5,5,-10,6,-7],[7,10,-4,2,2,7,-3,5],[-1,8,4,-3,-3,-1,-6,-9],[-6,-6,-1,-10,-10,-5,1,2],[-4,-9,4,-7,-5,-5,9,-4],[6,-7,-10,-1,5,5,7,7],[-10,10,-8,-10,-7,4,2,3],[7,6,-7,10,-5,8,-4,1]],[[-3,7,-10,-4,3,-5,5,-2],[7,2,5,8,6,-1,-2,4],[5,-9,-8,4,-5,8,-6,-6],[8,-9,-9,4,4,8,8,-5],[5,8,1,7,-2,7,5,2],[-9,-8,-9,-6,8,3,9,-8],[4,-10,-9,-2,-1,-8,-10,2],[3,-2,4,7,3,7,10,6],[1,-2,4,1,10,-4,10,-4],[9,7,-3,5,-6,9,6,-3],[-1,7,-6,-3,-8,1,-4,-2],[2,-4,6,2,-2,10,-6,4],[8,5,10,4,-4,7,-1,-10],[-10,7,-6,8,10,5,-2,7]],[[2,8,1,-1,7,4,-9,-9],[1,-3,-5,-6,-10,4,3,6],[3,-7,-3,9,6,-8,-10,-2],[-4,-9,-7,-5,7,2,1,3],[-9,-8,9,-2,3,-8,6,-1],[4,-9,-4,-9,-6,-10,7,10],[-4,-8,-6,-7,-2,-9,4,9],[1,-8,-4,7,-8,-6,-10,2],[-5,-6,3,-9,8,-3,1,10],[-10,6,-7,-6,7,3,8,-1],[6,-3,5,-3,-3,5,8,3],[-8,-6,1,-2,-3,8,-10,4],[10,-6,3,-8,-8,8,2,6],[2,5,-3,6,1,7,6,-7]],[[3,1,-3,-10,-4,6,2,6],[-5,1,-9,4,-2,-1,-4,-3],[2,-1,-5,-5,-1,-6,5,1],[4,-6,9,-5,10,-7,4,9],[6,-10,-3,9,-6,-9,9,-8],[1,8,-3,1,6,-8,-10,8],[-7,4,-5,-3,9,1,5,-1],[-7,-8,-1,-6,9,-9,8,-2],[6,-4,10,-4,-3,-7,8,5],[-8,-6,4,-5,-5,-9,-2,10],[6,10,3,-4,-1,-5,10,4],[4,6,3,8,-8,3,-7,-9],[-6,10,-5,8,-7,4,-2,5],[8,4,5,-9,9,2,-4,-3]],[[-9,10,9,-1,10,4,-4,9],[-2,-5,-5,9,-6,-3,9,-1],[-9,4,10,4,1,-3,9,-6],[7,10,-6,7,10,-4,-4,-9],[7,-2,-9,8,-6,-4,5,10],[1,-3,10,3,-9,-9,4,-9],[3,10,8,1,-1,3,-5,9],[4,5,3,2,-6,7,10,1],[-7,-3,-8,-1,9,4,-8,2],[-6,-3,-6,1,7,10,-1,-9],[1,-3,8,8,9,-3,-9,-8],[1,-2,-8,9,-10,-3,1,1],[-5,2,10,5,6,-8,-3,7],[-10,1,3,-1,8,-6,-7,-10]]], dtype = "int32")#candidate|414|(11, 14, 8)|const|int32
bop_415 = relay.logical_xor(const_413.astype('int32'), relay.reshape(const_414.astype('int32'), relay.shape_of(const_413))) # shape=(11, 14, 8)
output = relay.Tuple([bop_415,])
output2 = relay.Tuple([bop_415,])
func_426 = relay.Function([], output)
mod['func_426'] = func_426
mod = relay.transform.InferType()(mod)
output = func_426()
func_427 = relay.Function([], output)
mutated_mod['func_427'] = func_427
mutated_mod = relay.transform.InferType()(mutated_mod)
func_426_call = mod.get_global_var('func_426')
func_427_call = mutated_mod.get_global_var('func_427')
call_433 = relay.TupleGetItem(func_426_call(), 0)
call_434 = relay.TupleGetItem(func_427_call(), 0)
var_441 = relay.var("var_441", dtype = "int32", shape = (11, 14, 8))#candidate|441|(11, 14, 8)|var|int32
bop_442 = relay.left_shift(call_433.astype('uint64'), relay.reshape(var_441.astype('uint64'), relay.shape_of(call_433))) # shape=(11, 14, 8)
bop_445 = relay.left_shift(call_434.astype('uint64'), relay.reshape(var_441.astype('uint64'), relay.shape_of(call_434))) # shape=(11, 14, 8)
func_357_call = mod.get_global_var('func_357')
func_359_call = mutated_mod.get_global_var('func_359')
var_449 = relay.var("var_449", dtype = "uint16", shape = ())#candidate|449|()|var|uint16
call_448 = relay.TupleGetItem(func_357_call(relay.reshape(var_449.astype('uint16'), [])), 0)
call_450 = relay.TupleGetItem(func_359_call(relay.reshape(var_449.astype('uint16'), [])), 0)
output = relay.Tuple([bop_442,call_448,var_449,])
output2 = relay.Tuple([bop_445,call_450,var_449,])
func_463 = relay.Function([var_441,var_449,], output)
mod['func_463'] = func_463
mod = relay.transform.InferType()(mod)
var_464 = relay.var("var_464", dtype = "int32", shape = (11, 14, 8))#candidate|464|(11, 14, 8)|var|int32
var_465 = relay.var("var_465", dtype = "uint16", shape = ())#candidate|465|()|var|uint16
output = func_463(var_464,var_465,)
func_466 = relay.Function([var_464,var_465,], output)
mutated_mod['func_466'] = func_466
mutated_mod = relay.transform.InferType()(mutated_mod)
var_473 = relay.var("var_473", dtype = "int64", shape = ())#candidate|473|()|var|int64
const_474 = relay.const([[[-4,6,5,2,8,8,-10,6],[-9,-2,-10,8,2,2,5,-1]],[[-4,2,6,7,-5,6,5,7],[-10,1,-9,1,-10,-1,1,-1]],[[-10,-6,-8,10,7,-1,7,-4],[-8,9,3,1,3,6,5,-2]],[[-2,-1,1,-6,-7,-1,-6,1],[2,-3,10,-8,-7,8,4,7]],[[8,10,9,-10,-4,9,7,-6],[-8,4,7,10,8,8,-7,8]],[[2,5,-4,6,-7,10,4,5],[-6,-9,-2,-9,-6,10,1,-9]],[[8,2,10,-1,-2,-4,-6,-8],[9,7,8,-2,10,-8,-2,2]]], dtype = "int64")#candidate|474|(7, 2, 8)|const|int64
bop_475 = relay.less_equal(var_473.astype('bool'), const_474.astype('bool')) # shape=(7, 2, 8)
uop_485 = relay.sqrt(const_474.astype('float32')) # shape=(7, 2, 8)
output = relay.Tuple([bop_475,uop_485,])
output2 = relay.Tuple([bop_475,uop_485,])
func_487 = relay.Function([var_473,], output)
mod['func_487'] = func_487
mod = relay.transform.InferType()(mod)
var_488 = relay.var("var_488", dtype = "int64", shape = ())#candidate|488|()|var|int64
output = func_487(var_488)
func_489 = relay.Function([var_488], output)
mutated_mod['func_489'] = func_489
mutated_mod = relay.transform.InferType()(mutated_mod)
func_426_call = mod.get_global_var('func_426')
func_427_call = mutated_mod.get_global_var('func_427')
call_554 = relay.TupleGetItem(func_426_call(), 0)
call_555 = relay.TupleGetItem(func_427_call(), 0)
func_137_call = mod.get_global_var('func_137')
func_141_call = mutated_mod.get_global_var('func_141')
var_583 = relay.var("var_583", dtype = "uint64", shape = ())#candidate|583|()|var|uint64
var_584 = relay.var("var_584", dtype = "uint64", shape = (252,))#candidate|584|(252,)|var|uint64
call_582 = relay.TupleGetItem(func_137_call(relay.reshape(var_583.astype('uint64'), []), relay.reshape(var_584.astype('uint64'), [3, 12, 7]), ), 1)
call_585 = relay.TupleGetItem(func_141_call(relay.reshape(var_583.astype('uint64'), []), relay.reshape(var_584.astype('uint64'), [3, 12, 7]), ), 1)
output = relay.Tuple([call_554,call_582,var_583,var_584,])
output2 = relay.Tuple([call_555,call_585,var_583,var_584,])
func_589 = relay.Function([var_583,var_584,], output)
mod['func_589'] = func_589
mod = relay.transform.InferType()(mod)
var_590 = relay.var("var_590", dtype = "uint64", shape = ())#candidate|590|()|var|uint64
var_591 = relay.var("var_591", dtype = "uint64", shape = (252,))#candidate|591|(252,)|var|uint64
output = func_589(var_590,var_591,)
func_592 = relay.Function([var_590,var_591,], output)
mutated_mod['func_592'] = func_592
mutated_mod = relay.transform.InferType()(mutated_mod)
func_426_call = mod.get_global_var('func_426')
func_427_call = mutated_mod.get_global_var('func_427')
call_594 = relay.TupleGetItem(func_426_call(), 0)
call_595 = relay.TupleGetItem(func_427_call(), 0)
output = relay.Tuple([call_594,])
output2 = relay.Tuple([call_595,])
func_608 = relay.Function([], output)
mod['func_608'] = func_608
mod = relay.transform.InferType()(mod)
mutated_mod['func_608'] = func_608
mutated_mod = relay.transform.InferType()(mutated_mod)
func_608_call = mutated_mod.get_global_var('func_608')
call_609 = func_608_call()
output = call_609
func_610 = relay.Function([], output)
mutated_mod['func_610'] = func_610
mutated_mod = relay.transform.InferType()(mutated_mod)
func_608_call = mod.get_global_var('func_608')
func_610_call = mutated_mod.get_global_var('func_610')
call_628 = relay.TupleGetItem(func_608_call(), 0)
call_629 = relay.TupleGetItem(func_610_call(), 0)
func_608_call = mod.get_global_var('func_608')
func_610_call = mutated_mod.get_global_var('func_610')
call_630 = relay.TupleGetItem(func_608_call(), 0)
call_631 = relay.TupleGetItem(func_610_call(), 0)
bop_633 = relay.mod(call_628.astype('float64'), relay.reshape(call_630.astype('float64'), relay.shape_of(call_628))) # shape=(11, 14, 8)
bop_636 = relay.mod(call_629.astype('float64'), relay.reshape(call_631.astype('float64'), relay.shape_of(call_629))) # shape=(11, 14, 8)
uop_643 = relay.acosh(bop_633.astype('float64')) # shape=(11, 14, 8)
uop_645 = relay.acosh(bop_636.astype('float64')) # shape=(11, 14, 8)
uop_662 = relay.tan(uop_643.astype('float64')) # shape=(11, 14, 8)
uop_664 = relay.tan(uop_645.astype('float64')) # shape=(11, 14, 8)
uop_678 = relay.acos(uop_662.astype('float32')) # shape=(11, 14, 8)
uop_680 = relay.acos(uop_664.astype('float32')) # shape=(11, 14, 8)
func_463_call = mod.get_global_var('func_463')
func_466_call = mutated_mod.get_global_var('func_466')
const_682 = relay.const(-6, dtype = "uint16")#candidate|682|()|const|uint16
call_681 = relay.TupleGetItem(func_463_call(relay.reshape(call_630.astype('int32'), [11, 14, 8]), relay.reshape(const_682.astype('uint16'), []), ), 0)
call_683 = relay.TupleGetItem(func_466_call(relay.reshape(call_630.astype('int32'), [11, 14, 8]), relay.reshape(const_682.astype('uint16'), []), ), 0)
uop_692 = relay.sqrt(uop_678.astype('float64')) # shape=(11, 14, 8)
uop_694 = relay.sqrt(uop_680.astype('float64')) # shape=(11, 14, 8)
output = relay.Tuple([call_681,const_682,uop_692,])
output2 = relay.Tuple([call_683,const_682,uop_694,])
func_695 = relay.Function([], output)
mod['func_695'] = func_695
mod = relay.transform.InferType()(mod)
output = func_695()
func_696 = relay.Function([], output)
mutated_mod['func_696'] = func_696
mutated_mod = relay.transform.InferType()(mutated_mod)
func_695_call = mod.get_global_var('func_695')
func_696_call = mutated_mod.get_global_var('func_696')
call_769 = relay.TupleGetItem(func_695_call(), 2)
call_770 = relay.TupleGetItem(func_696_call(), 2)
func_589_call = mod.get_global_var('func_589')
func_592_call = mutated_mod.get_global_var('func_592')
var_775 = relay.var("var_775", dtype = "uint64", shape = ())#candidate|775|()|var|uint64
var_776 = relay.var("var_776", dtype = "uint64", shape = (252,))#candidate|776|(252,)|var|uint64
call_774 = relay.TupleGetItem(func_589_call(relay.reshape(var_775.astype('uint64'), []), relay.reshape(var_776.astype('uint64'), [252,]), ), 2)
call_777 = relay.TupleGetItem(func_592_call(relay.reshape(var_775.astype('uint64'), []), relay.reshape(var_776.astype('uint64'), [252,]), ), 2)
var_783 = relay.var("var_783", dtype = "float64", shape = (11, 14, 8))#candidate|783|(11, 14, 8)|var|float64
bop_784 = relay.logical_and(call_769.astype('bool'), relay.reshape(var_783.astype('bool'), relay.shape_of(call_769))) # shape=(11, 14, 8)
bop_787 = relay.logical_and(call_770.astype('bool'), relay.reshape(var_783.astype('bool'), relay.shape_of(call_770))) # shape=(11, 14, 8)
func_463_call = mod.get_global_var('func_463')
func_466_call = mutated_mod.get_global_var('func_466')
call_789 = relay.TupleGetItem(func_463_call(relay.reshape(call_769.astype('int32'), [11, 14, 8]), relay.reshape(call_774.astype('uint16'), []), ), 2)
call_790 = relay.TupleGetItem(func_466_call(relay.reshape(call_769.astype('int32'), [11, 14, 8]), relay.reshape(call_774.astype('uint16'), []), ), 2)
func_695_call = mod.get_global_var('func_695')
func_696_call = mutated_mod.get_global_var('func_696')
call_794 = relay.TupleGetItem(func_695_call(), 1)
call_795 = relay.TupleGetItem(func_696_call(), 1)
var_796 = relay.var("var_796", dtype = "uint64", shape = (7, 8, 15))#candidate|796|(7, 8, 15)|var|uint64
bop_797 = relay.divide(call_774.astype('float64'), var_796.astype('float64')) # shape=(7, 8, 15)
bop_800 = relay.divide(call_777.astype('float64'), var_796.astype('float64')) # shape=(7, 8, 15)
func_357_call = mod.get_global_var('func_357')
func_359_call = mutated_mod.get_global_var('func_359')
call_801 = relay.TupleGetItem(func_357_call(relay.reshape(call_774.astype('uint16'), [])), 1)
call_802 = relay.TupleGetItem(func_359_call(relay.reshape(call_774.astype('uint16'), [])), 1)
uop_805 = relay.atan(bop_797.astype('float64')) # shape=(7, 8, 15)
uop_807 = relay.atan(bop_800.astype('float64')) # shape=(7, 8, 15)
bop_816 = relay.floor_divide(uop_805.astype('float64'), call_789.astype('float64')) # shape=(7, 8, 15)
bop_819 = relay.floor_divide(uop_807.astype('float64'), call_790.astype('float64')) # shape=(7, 8, 15)
output = relay.Tuple([var_775,var_776,bop_784,call_794,call_801,bop_816,])
output2 = relay.Tuple([var_775,var_776,bop_787,call_795,call_802,bop_819,])
func_829 = relay.Function([var_775,var_776,var_783,var_796,], output)
mod['func_829'] = func_829
mod = relay.transform.InferType()(mod)
mutated_mod['func_829'] = func_829
mutated_mod = relay.transform.InferType()(mutated_mod)
func_829_call = mutated_mod.get_global_var('func_829')
var_831 = relay.var("var_831", dtype = "uint64", shape = ())#candidate|831|()|var|uint64
var_832 = relay.var("var_832", dtype = "uint64", shape = (252,))#candidate|832|(252,)|var|uint64
var_833 = relay.var("var_833", dtype = "float64", shape = (11, 14, 8))#candidate|833|(11, 14, 8)|var|float64
var_834 = relay.var("var_834", dtype = "uint64", shape = (7, 8, 15))#candidate|834|(7, 8, 15)|var|uint64
call_830 = func_829_call(var_831,var_832,var_833,var_834,)
output = call_830
func_835 = relay.Function([var_831,var_832,var_833,var_834,], output)
mutated_mod['func_835'] = func_835
mutated_mod = relay.transform.InferType()(mutated_mod)
var_860 = relay.var("var_860", dtype = "uint32", shape = (8, 12, 7))#candidate|860|(8, 12, 7)|var|uint32
var_861 = relay.var("var_861", dtype = "uint32", shape = (8, 12, 7))#candidate|861|(8, 12, 7)|var|uint32
bop_862 = relay.add(var_860.astype('uint32'), relay.reshape(var_861.astype('uint32'), relay.shape_of(var_860))) # shape=(8, 12, 7)
func_487_call = mod.get_global_var('func_487')
func_489_call = mutated_mod.get_global_var('func_489')
const_870 = relay.const(3, dtype = "int64")#candidate|870|()|const|int64
call_869 = relay.TupleGetItem(func_487_call(relay.reshape(const_870.astype('int64'), [])), 1)
call_871 = relay.TupleGetItem(func_489_call(relay.reshape(const_870.astype('int64'), [])), 1)
uop_891 = relay.acos(bop_862.astype('float64')) # shape=(8, 12, 7)
uop_908 = relay.asin(uop_891.astype('float32')) # shape=(8, 12, 7)
output = relay.Tuple([call_869,const_870,uop_908,])
output2 = relay.Tuple([call_871,const_870,uop_908,])
func_910 = relay.Function([var_860,var_861,], output)
mod['func_910'] = func_910
mod = relay.transform.InferType()(mod)
var_911 = relay.var("var_911", dtype = "uint32", shape = (8, 12, 7))#candidate|911|(8, 12, 7)|var|uint32
var_912 = relay.var("var_912", dtype = "uint32", shape = (8, 12, 7))#candidate|912|(8, 12, 7)|var|uint32
output = func_910(var_911,var_912,)
func_913 = relay.Function([var_911,var_912,], output)
mutated_mod['func_913'] = func_913
mutated_mod = relay.transform.InferType()(mutated_mod)
const_953 = relay.const([[[-8.045479],[8.144134],[-9.348013]],[[1.368753],[-8.327804],[9.887274]]], dtype = "float64")#candidate|953|(2, 3, 1)|const|float64
uop_954 = relay.acosh(const_953.astype('float64')) # shape=(2, 3, 1)
output = relay.Tuple([uop_954,])
output2 = relay.Tuple([uop_954,])
func_960 = relay.Function([], output)
mod['func_960'] = func_960
mod = relay.transform.InferType()(mod)
mutated_mod['func_960'] = func_960
mutated_mod = relay.transform.InferType()(mutated_mod)
func_960_call = mutated_mod.get_global_var('func_960')
call_961 = func_960_call()
output = call_961
func_962 = relay.Function([], output)
mutated_mod['func_962'] = func_962
mutated_mod = relay.transform.InferType()(mutated_mod)
func_960_call = mod.get_global_var('func_960')
func_962_call = mutated_mod.get_global_var('func_962')
call_966 = relay.TupleGetItem(func_960_call(), 0)
call_967 = relay.TupleGetItem(func_962_call(), 0)
output = call_966
output2 = call_967
func_968 = relay.Function([], output)
mod['func_968'] = func_968
mod = relay.transform.InferType()(mod)
mutated_mod['func_968'] = func_968
mutated_mod = relay.transform.InferType()(mutated_mod)
func_968_call = mutated_mod.get_global_var('func_968')
call_969 = func_968_call()
output = call_969
func_970 = relay.Function([], output)
mutated_mod['func_970'] = func_970
mutated_mod = relay.transform.InferType()(mutated_mod)
const_976 = relay.const([[[-1,-4,-3,9,2,-1,-5],[2,5,-1,-6,-1,-3,-7],[3,1,-1,2,3,-8,-9],[10,1,-2,-5,-7,9,-2],[-6,-5,1,5,-3,7,-10],[-3,-3,-5,-4,3,9,2],[8,10,5,5,3,9,8],[-4,-9,7,9,-8,-8,-4],[-1,-5,-2,-4,-4,2,-10],[-5,-7,5,5,7,6,7],[-6,-1,9,5,2,-8,-10],[-4,-1,7,8,-3,-7,-9],[8,7,8,1,5,-7,-5],[3,-7,-6,-8,6,8,-10],[-2,8,-4,-5,4,-10,-2],[-7,-5,-4,9,-1,-4,4]],[[-6,7,-3,9,-3,-2,10],[7,2,-3,-4,7,7,-2],[-5,-5,1,1,8,-3,-6],[-7,8,10,-7,7,10,-5],[-2,-1,3,9,5,-8,-4],[1,8,6,-1,-6,-1,-10],[-8,9,-1,-8,4,10,9],[-4,9,-1,-5,-2,7,-5],[-2,-9,-1,2,-9,-8,-8],[-4,-6,-8,-4,-1,9,-5],[1,3,6,-6,10,-9,-8],[2,5,3,-4,6,1,7],[1,6,-4,9,-1,-7,3],[-10,4,7,1,3,-10,-5],[8,-10,-6,5,5,9,7],[9,-1,10,-4,-7,6,10]],[[10,-6,-7,-9,3,2,6],[-6,-7,-2,5,-6,-3,-3],[10,5,-9,8,7,9,-9],[-2,2,9,-4,-8,5,9],[4,6,-5,5,4,-2,-3],[3,-1,9,2,3,-9,6],[-6,3,-6,5,2,7,-7],[6,-1,-2,-5,-8,-8,-6],[3,-2,-6,-10,-4,6,-6],[1,-4,-3,-8,-7,-7,4],[7,6,-2,10,3,-8,4],[-4,-7,-6,-2,5,-6,-6],[9,-2,-10,6,-7,7,8],[-9,-1,3,-8,10,7,-1],[-8,-8,7,-1,8,-10,-8],[5,4,6,-6,5,9,-3]],[[9,-1,-1,3,-9,-8,4],[2,-4,-7,10,6,-6,8],[-6,-4,-5,1,-6,-5,-9],[-3,-10,6,-1,-2,6,-5],[-9,-8,5,10,-8,5,5],[2,4,8,10,8,5,-2],[-10,-5,-1,-5,-6,-4,6],[-10,-1,7,-8,9,-7,9],[7,-4,8,7,4,-4,5],[-5,-9,-3,7,-8,-5,1],[2,-5,-1,7,10,-9,-3],[5,2,2,4,4,7,4],[-6,5,7,8,-1,-1,8],[5,2,-1,9,8,1,5],[-3,-10,-6,-9,-5,4,2],[8,5,3,-5,-4,2,-8]],[[-3,10,1,-4,-7,1,10],[7,-1,3,-8,3,-5,-8],[8,-9,-8,-8,-9,8,-5],[-7,6,-8,10,-3,2,-4],[5,-3,9,-6,8,-7,-4],[4,-6,6,-6,-9,6,7],[-9,4,-4,-7,-6,1,4],[-3,-5,-10,10,2,-8,4],[-4,3,-5,-7,3,-1,4],[-5,10,-7,-6,7,-2,-4],[2,8,3,1,-8,7,2],[-10,-2,5,4,-8,-10,8],[3,-4,-4,-5,4,4,-4],[-3,3,-3,8,-8,9,-3],[-2,-2,-5,-4,-1,-5,-2],[-6,4,-3,3,-3,-3,3]],[[10,2,9,8,2,-4,-8],[-7,1,-9,3,3,9,4],[8,5,-5,9,2,-9,-9],[7,-3,-10,-10,-9,-2,-6],[6,-4,-9,-2,7,-10,1],[1,-2,7,-5,-8,-3,-7],[-7,7,-4,2,1,10,7],[5,7,8,-6,-5,-10,-5],[9,-10,-4,-4,2,-2,9],[-9,1,-6,1,8,-7,-2],[5,1,-9,2,10,4,3],[-4,-9,1,-10,8,9,1],[-8,-4,-10,9,-6,7,-9],[9,-8,-4,-8,6,-2,-9],[10,-8,5,-3,6,6,-3],[9,3,-5,1,-5,6,6]],[[6,2,7,4,3,7,-9],[1,-6,-5,-8,-10,-2,9],[8,8,3,10,2,-2,-1],[-2,9,-2,4,4,10,5],[10,-9,-1,10,9,-6,4],[-5,4,-5,3,-10,9,-10],[-9,-10,-1,5,8,-8,7],[-9,1,-6,-1,7,-2,-2],[-2,-7,-9,10,-6,4,2],[2,-7,10,6,4,-9,-3],[10,10,-8,-5,-4,9,-1],[3,-6,-5,-7,-4,1,10],[8,10,7,-10,-7,-3,1],[2,-4,7,1,6,5,10],[-5,7,-4,-1,-7,9,7],[6,2,10,-2,-8,7,2]],[[4,-9,4,2,2,-2,-6],[4,1,-1,-7,-10,6,-3],[-4,6,-7,-6,-2,1,-6],[3,-4,-5,-7,9,-9,-3],[1,-9,-1,2,9,-10,-8],[5,4,6,-4,-4,-9,-5],[3,3,-3,8,5,-1,8],[7,2,8,1,7,-6,8],[-3,-4,-10,2,-7,-5,-10],[1,8,4,2,-10,-7,-10],[-6,-8,1,9,7,3,4],[10,-6,4,9,-6,1,5],[10,10,-6,-9,8,-8,-1],[-1,-1,-1,-2,-1,-4,-3],[2,2,7,-2,-8,-10,10],[3,9,8,-7,-8,-7,-1]],[[7,-3,-3,-5,-5,-3,-9],[-1,-9,2,-10,-1,-1,-7],[10,-9,-1,-8,-7,7,1],[7,1,8,-4,-1,1,3],[-10,10,6,7,-2,-4,-9],[3,8,-7,-9,10,-5,10],[-2,-8,1,10,-9,-7,-3],[2,-3,-9,4,-2,3,6],[5,-6,9,9,3,-9,8],[7,-10,-1,-3,-4,10,-10],[9,3,-4,-1,4,-2,1],[1,-9,9,7,-2,2,-5],[-3,-5,3,-6,-8,9,-9],[9,2,9,8,3,-10,6],[-3,4,8,-8,-9,7,5],[7,6,-6,-8,4,-3,-3]],[[-3,4,-10,2,8,-10,-6],[4,4,5,-9,-2,6,-3],[4,1,-5,-5,-1,-4,7],[-6,10,4,1,-5,10,7],[3,2,-8,-7,8,-9,-9],[2,6,10,-9,-1,4,3],[1,-8,2,2,-5,-2,-10],[-5,-5,-6,-4,6,-1,-4],[-2,8,6,10,8,-7,-2],[9,1,1,-1,-8,1,8],[2,-6,-10,-10,2,4,3],[-4,-2,6,-7,1,2,-4],[-3,9,-6,-10,1,3,-9],[1,10,-6,8,-6,-7,-4],[-6,3,1,-5,-7,5,4],[-1,-7,-4,8,9,-9,3]]], dtype = "uint16")#candidate|976|(10, 16, 7)|const|uint16
var_977 = relay.var("var_977", dtype = "uint16", shape = (10, 16, 7))#candidate|977|(10, 16, 7)|var|uint16
bop_978 = relay.equal(const_976.astype('bool'), relay.reshape(var_977.astype('bool'), relay.shape_of(const_976))) # shape=(10, 16, 7)
output = relay.Tuple([bop_978,])
output2 = relay.Tuple([bop_978,])
func_983 = relay.Function([var_977,], output)
mod['func_983'] = func_983
mod = relay.transform.InferType()(mod)
var_984 = relay.var("var_984", dtype = "uint16", shape = (10, 16, 7))#candidate|984|(10, 16, 7)|var|uint16
output = func_983(var_984)
func_985 = relay.Function([var_984], output)
mutated_mod['func_985'] = func_985
mutated_mod = relay.transform.InferType()(mutated_mod)
func_426_call = mod.get_global_var('func_426')
func_427_call = mutated_mod.get_global_var('func_427')
call_991 = relay.TupleGetItem(func_426_call(), 0)
call_992 = relay.TupleGetItem(func_427_call(), 0)
func_829_call = mod.get_global_var('func_829')
func_835_call = mutated_mod.get_global_var('func_835')
var_995 = relay.var("var_995", dtype = "uint64", shape = ())#candidate|995|()|var|uint64
const_996 = relay.const([6,7,4,8,8,2,5,-10,8,-8,-5,-3,2,1,4,-8,-9,10,8,3,-3,-1,-2,3,-4,10,-2,10,-6,-9,-6,-3,-3,-8,-1,6,7,4,-2,-3,8,8,8,-5,-8,5,1,-8,-10,-5,1,-7,-1,-2,-10,9,-8,-9,4,9,6,5,1,-2,-2,-4,-10,-5,-1,-6,-2,8,-2,6,-1,-8,-10,-6,8,2,5,-7,6,-8,9,-10,8,10,-7,8,3,4,-10,-2,10,-10,-1,-2,7,4,3,-6,3,3,-2,7,8,9,-4,8,-7,9,-5,5,-10,-7,-4,-3,9,-9,6,8,-9,-4,8,-7,10,2,-8,7,-7,-8,-9,10,-7,-1,-4,9,-8,6,-6,-10,10,2,-1,3,-5,-1,-4,-2,-9,-5,6,4,-6,-9,-5,9,-2,-1,-1,-1,7,-1,-10,-3,-10,1,10,-7,8,-9,6,6,8,-1,2,-5,3,-2,-1,-1,3,4,-9,-2,-10,8,8,3,1,-2,5,4,3,10,-2,2,5,9,-10,9,-1,-5,-10,2,10,6,3,-3,7,10,-4,-5,2,-1,4,-2,8,3,-6,1,2,3,-9,-4,10,6,-10,-3,4,7,-5,-2,-6,10,3,-8,-9,10,9,-4,2,3,8,4,-1,9,-10,8,7,10], dtype = "uint64")#candidate|996|(252,)|const|uint64
const_997 = relay.const([-7,-6,9,-9,-2,-10,-7,-8,6,-8,-10,9,-8,6,-6,3,-3,10,-10,1,-7,-7,-6,3,-6,-5,9,2,10,-7,2,-2,8,-9,2,2,-10,4,-5,8,-7,-6,6,-6,-7,-5,-2,5,2,8,-5,3,-9,-1,-5,-6,3,1,-1,8,-9,-6,-3,-2,-9,8,1,1,-10,6,5,-10,-3,8,9,1,-10,-2,2,-7,-4,-6,8,-7,-4,-6,7,7,-8,-6,-2,8,6,6,-1,8,10,10,-5,-6,4,-6,-7,-10,8,1,-3,-2,8,6,3,-7,-1,-10,-8,5,-6,10,6,8,6,-3,-10,-9,-5,10,-2,-2,5,-9,-6,-2,7,-4,2,6,1,10,-8,-2,5,-2,8,-1,-4,6,7,2,10,7,-10,-3,-2,-4,1,5,7,-4,-1,-8,5,5,-1,-6,-5,-4,-5,7,9,10,-9,-9,-10,1,-10,-6,-2,9,-2,-4,-5,3,5,-7,-3,-4,2,9,8,3,9,-3,4,4,-4,-2,-5,10,7,4,-6,2,-4,10,-1,8,-6,-10,-10,6,-3,6,7,7,5,4,2,9,-9,5,-4,1,-3,-10,-7,8,9,7,-2,-10,8,8,9,3,6,9,1,2,3,9,-2,-10,-3,-7,-3,-1,10,-10,-7,-7,1,5,-8,-7,8,-2,3,1,1,10,-6,7,-10,-5,10,-10,-9,-4,-1,-9,7,9,-3,7,-2,-2,-9,4,-7,-6,2,9,-10,-10,4,-2,-1,2,-5,2,9,4,2,-9,7,-6,-1,10,-8,4,10,-2,9,6,6,-1,-1,-4,3,2,7,8,-10,1,9,-9,-1,1,-8,6,-5,10,-4,-9,-8,-8,6,4,4,-6,-1,5,10,4,3,2,6,3,8,6,10,10,-10,6,10,-9,8,2,10,-6,5,10,-1,3,5,-3,5,-3,-10,1,10,2,5,-6,10,-7,-9,10,2,-9,-5,1,8,7,2,1,-7,10,6,5,7,3,-1,-7,-8,-9,9,-5,4,6,-7,8,9,-3,3,1,2,-7,8,-7,8,-9,5,-3,-5,9,-7,5,-4,-3,8,8,-9,-4,-6,-3,-6,1,-8,4,-7,-7,-9,-2,-1,-9,-8,-1,-1,2,-8,4,-7,7,1,-1,4,5,-10,-4,2,2,-2,5,-1,-3,-1,-3,1,-8,-1,1,4,-7,-2,7,-8,-2,-3,-6,-5,3,3,6,6,-6,-2,-10,-4,-3,8,10,9,8,10,-8,10,-1,-7,-9,-3,-8,4,3,5,-6,-6,-10,-10,-6,-10,-5,6,-5,7,6,9,-6,1,2,-5,-8,-5,-5,5,-7,-8,5,-10,-8,4,-8,-7,-9,6,-4,-10,-2,-9,1,-8,8,1,-1,6,2,3,-7,4,9,-7,-1,-3,3,-7,7,5,3,-3,-8,4,-10,-10,7,1,6,-9,5,9,8,-4,-5,-2,-4,-3,-3,4,5,-10,-2,10,-9,6,-3,-1,2,5,4,-6,-4,5,-9,3,-7,-6,-4,-6,5,6,-8,6,4,-7,-1,-9,5,2,-4,-8,8,7,-2,4,6,3,8,-4,-5,3,8,-8,-7,-9,-5,-10,-4,-4,4,2,-7,6,8,-2,-2,6,-6,-5,7,3,-4,5,-4,2,7,9,-3,-1,-4,-4,7,-8,-6,-7,-8,7,5,-10,2,-6,6,-3,10,-9,-9,1,-5,-3,2,8,-10,2,8,6,-3,-9,10,9,-7,4,-3,4,-2,1,-6,-3,-3,-2,8,10,-2,2,10,2,2,-3,-9,-3,3,6,-10,-6,6,5,-7,7,4,1,-3,-1,-1,7,5,-2,3,-10,6,9,3,10,-7,-1,-6,-6,7,3,-4,-7,-2,9,-8,-2,2,-10,3,9,5,-2,-2,2,-6,9,-5,10,7,5,-8,-2,6,9,10,-1,6,7,-2,9,-4,-9,-7,6,-10,-9,-6,1,1,-3,-6,7,10,3,-3,-9,3,5,8,-3,-2,9,5,2,-9,-8,-1,-10,9,2,-6,-10,-10,-10,-6,-9,7,-6,9,8,-5,7,-3,1,-2,5,-4,8,10,4,-1,4,-2,-8,-10,-1,7,3,6,-4,-6,6,-4,6,2,-1,5,-9,-6,10,-7,1,10,4,9,-4,-6,7,-5,-5,-4,-8,-2,6,5,-3,6,4,9,1,5,3,6,-1,-2,5,-3,-5,-1,-4,-6,9,-1,9,3], dtype = "uint64")#candidate|997|(840,)|const|uint64
call_994 = relay.TupleGetItem(func_829_call(relay.reshape(var_995.astype('uint64'), []), relay.reshape(const_996.astype('uint64'), [252,]), relay.reshape(call_991.astype('float64'), [11, 14, 8]), relay.reshape(const_997.astype('uint64'), [7, 8, 15]), ), 0)
call_998 = relay.TupleGetItem(func_835_call(relay.reshape(var_995.astype('uint64'), []), relay.reshape(const_996.astype('uint64'), [252,]), relay.reshape(call_991.astype('float64'), [11, 14, 8]), relay.reshape(const_997.astype('uint64'), [7, 8, 15]), ), 0)
func_426_call = mod.get_global_var('func_426')
func_427_call = mutated_mod.get_global_var('func_427')
call_1006 = relay.TupleGetItem(func_426_call(), 0)
call_1007 = relay.TupleGetItem(func_427_call(), 0)
output = relay.Tuple([call_991,call_994,var_995,const_996,const_997,call_1006,])
output2 = relay.Tuple([call_992,call_998,var_995,const_996,const_997,call_1007,])
func_1010 = relay.Function([var_995,], output)
mod['func_1010'] = func_1010
mod = relay.transform.InferType()(mod)
mutated_mod['func_1010'] = func_1010
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1011 = relay.var("var_1011", dtype = "uint64", shape = ())#candidate|1011|()|var|uint64
func_1010_call = mutated_mod.get_global_var('func_1010')
call_1012 = func_1010_call(var_1011)
output = call_1012
func_1013 = relay.Function([var_1011], output)
mutated_mod['func_1013'] = func_1013
mutated_mod = relay.transform.InferType()(mutated_mod)
func_608_call = mod.get_global_var('func_608')
func_610_call = mutated_mod.get_global_var('func_610')
call_1018 = relay.TupleGetItem(func_608_call(), 0)
call_1019 = relay.TupleGetItem(func_610_call(), 0)
func_608_call = mod.get_global_var('func_608')
func_610_call = mutated_mod.get_global_var('func_610')
call_1023 = relay.TupleGetItem(func_608_call(), 0)
call_1024 = relay.TupleGetItem(func_610_call(), 0)
func_487_call = mod.get_global_var('func_487')
func_489_call = mutated_mod.get_global_var('func_489')
const_1026 = relay.const(-6, dtype = "int64")#candidate|1026|()|const|int64
call_1025 = relay.TupleGetItem(func_487_call(relay.reshape(const_1026.astype('int64'), [])), 0)
call_1027 = relay.TupleGetItem(func_489_call(relay.reshape(const_1026.astype('int64'), [])), 0)
output = relay.Tuple([call_1018,call_1023,call_1025,const_1026,])
output2 = relay.Tuple([call_1019,call_1024,call_1027,const_1026,])
func_1028 = relay.Function([], output)
mod['func_1028'] = func_1028
mod = relay.transform.InferType()(mod)
output = func_1028()
func_1029 = relay.Function([], output)
mutated_mod['func_1029'] = func_1029
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1028_call = mod.get_global_var('func_1028')
func_1029_call = mutated_mod.get_global_var('func_1029')
call_1084 = relay.TupleGetItem(func_1028_call(), 3)
call_1085 = relay.TupleGetItem(func_1029_call(), 3)
func_829_call = mod.get_global_var('func_829')
func_835_call = mutated_mod.get_global_var('func_835')
var_1088 = relay.var("var_1088", dtype = "uint64", shape = (252,))#candidate|1088|(252,)|var|uint64
var_1089 = relay.var("var_1089", dtype = "float64", shape = (1232,))#candidate|1089|(1232,)|var|float64
const_1090 = relay.const([-8,-9,-6,1,-7,8,10,10,2,-9,-8,3,4,5,7,-9,-6,6,-3,3,-3,-2,8,1,6,8,4,-5,-3,10,2,-7,-8,-2,9,-4,4,-9,8,4,-1,1,-8,-4,9,-10,-3,-9,9,-3,5,-5,3,-5,4,-6,4,2,6,-2,8,-5,-9,2,-6,-8,-2,1,-7,-8,-8,7,4,5,-3,-4,-8,-4,3,-5,-10,-1,-8,-10,1,-5,4,2,-1,-9,-3,-7,-4,-6,-6,-8,-5,-1,-3,5,10,-4,4,-4,2,-9,-8,8,5,9,-6,-8,-7,-2,-3,-4,-9,-9,6,-7,-9,-5,-1,9,6,9,-6,-1,-7,3,1,3,8,2,7,2,4,-3,10,-4,1,-8,-2,9,-3,-1,2,4,-8,-3,6,3,5,-6,9,3,5,6,-2,9,7,-2,6,8,4,10,-7,9,-10,-6,9,10,1,-1,1,10,2,7,-8,3,-4,-10,-8,2,-8,-9,-6,-10,3,9,3,-3,1,-2,-5,-9,-8,10,1,-3,10,3,9,4,5,7,5,3,-10,-3,10,3,-4,-5,7,-2,-8,-5,-10,-2,-4,-5,8,3,4,4,9,-3,2,-7,-6,10,-6,4,5,5,4,8,-9,-2,8,-9,5,1,-2,8,9,-5,-2,5,2,7,-1,9,-8,2,-9,7,5,-9,8,6,-5,4,-7,-5,8,-6,-10,8,-8,-6,-3,8,4,-6,7,2,2,-1,5,-9,-9,2,2,7,-10,6,9,1,3,6,9,6,-5,2,3,5,-8,1,-6,-1,-3,-10,-3,6,8,10,1,1,-10,-6,-4,-7,9,-4,6,1,-6,-2,4,7,-9,1,2,5,-3,-7,3,9,1,7,3,-9,-1,-8,-8,-6,3,-6,-9,8,-4,-1,8,9,5,9,3,9,-8,8,-3,10,4,-8,6,7,1,-7,7,-2,-3,4,-8,2,9,1,-6,5,-6,-5,1,4,-9,2,-8,-2,-7,7,-9,-1,-6,-8,3,4,-6,-4,10,-10,-1,-9,-9,8,-7,-1,-3,-5,-3,3,6,-7,-4,-1,1,7,4,-10,9,8,4,-4,-2,-6,-2,2,6,-2,2,-9,5,-6,-2,-3,-8,-6,-10,9,-9,-8,-6,9,-10,4,-4,-7,-9,-9,1,1,-3,-2,-9,-7,-10,9,5,-9,9,-7,8,-2,-6,9,3,7,-9,2,-1,-8,6,-6,7,4,-1,-1,-4,6,-3,9,5,5,4,3,8,6,-9,3,-2,-4,-9,-1,-7,4,4,-8,-1,6,-10,-3,-10,-2,-3,-5,-1,7,-3,4,-9,-9,-4,-3,-2,10,-8,2,-2,-7,9,-10,-2,-10,-7,-4,-3,-9,-10,1,1,-5,2,5,2,-9,-5,-1,7,-9,-8,-1,5,-9,10,8,1,10,-3,-9,6,-7,-8,5,10,10,-8,8,-10,-10,-8,4,6,-5,9,-5,4,6,-8,7,-7,-7,-9,10,-3,10,3,-9,5,7,9,-9,-1,3,5,9,-1,9,-1,-7,-3,6,-8,4,-10,-7,2,10,-10,5,6,-5,10,5,5,8,9,-4,10,2,9,-8,7,4,-4,-1,3,-7,2,-6,4,-4,7,-9,8,-6,-3,7,4,-5,10,-9,4,6,8,4,8,-6,-8,4,8,-10,-6,-9,10,-1,10,3,-5,-9,-5,-6,10,7,-7,-3,-3,-6,-2,1,10,2,3,-5,8,-3,8,-5,-3,8,5,7,-6,7,9,-2,4,-3,3,7,-4,4,2,-4,-4,-5,6,5,6,-2,3,-7,7,-2,-8,2,9,-5,7,-6,-2,8,-4,9,-8,-8,-4,6,3,-2,6,2,-1,-8,6,9,-6,5,-3,-3,-5,10,4,-1,-3,-7,-6,-4,-5,5,-6,-9,-3,-4,9,7,-8,3,10,-8,-8,2,3,-3,8,-10,-4,9,-3,6,-2,-8,-10,2,-7,-3,-3,-1,10,-7,-1,7,7,-7,-2,-4,5,-5,-5,5,7,-8,-4,9,2,6,-4,-3,8,-1,2,-5,9,4,-8,5,8,6,-4,-7,2,4,-6,-6,6,7,5,6,3,-8,-8,6,8,-9,-8,1,-2,7,9,-2,-1,2,2,-1,-8,4,4,4,-2,6,-1,-2,-9,1,-2,-4,4,10,6,9,-10,1,-4,8,8,-8,9,2,-8,-10,5,-3,4,5,5,-5,8,1,-9,-8,2,-7], dtype = "uint64")#candidate|1090|(840,)|const|uint64
call_1087 = relay.TupleGetItem(func_829_call(relay.reshape(call_1084.astype('uint64'), []), relay.reshape(var_1088.astype('uint64'), [252,]), relay.reshape(var_1089.astype('float64'), [11, 14, 8]), relay.reshape(const_1090.astype('uint64'), [7, 8, 15]), ), 2)
call_1091 = relay.TupleGetItem(func_835_call(relay.reshape(call_1084.astype('uint64'), []), relay.reshape(var_1088.astype('uint64'), [252,]), relay.reshape(var_1089.astype('float64'), [11, 14, 8]), relay.reshape(const_1090.astype('uint64'), [7, 8, 15]), ), 2)
func_960_call = mod.get_global_var('func_960')
func_962_call = mutated_mod.get_global_var('func_962')
call_1102 = relay.TupleGetItem(func_960_call(), 0)
call_1103 = relay.TupleGetItem(func_962_call(), 0)
output = relay.Tuple([call_1084,call_1087,var_1088,var_1089,const_1090,call_1102,])
output2 = relay.Tuple([call_1085,call_1091,var_1088,var_1089,const_1090,call_1103,])
func_1107 = relay.Function([var_1088,var_1089,], output)
mod['func_1107'] = func_1107
mod = relay.transform.InferType()(mod)
var_1108 = relay.var("var_1108", dtype = "uint64", shape = (252,))#candidate|1108|(252,)|var|uint64
var_1109 = relay.var("var_1109", dtype = "float64", shape = (1232,))#candidate|1109|(1232,)|var|float64
output = func_1107(var_1108,var_1109,)
func_1110 = relay.Function([var_1108,var_1109,], output)
mutated_mod['func_1110'] = func_1110
mutated_mod = relay.transform.InferType()(mutated_mod)
func_695_call = mod.get_global_var('func_695')
func_696_call = mutated_mod.get_global_var('func_696')
call_1134 = relay.TupleGetItem(func_695_call(), 2)
call_1135 = relay.TupleGetItem(func_696_call(), 2)
func_829_call = mod.get_global_var('func_829')
func_835_call = mutated_mod.get_global_var('func_835')
const_1142 = relay.const(3, dtype = "uint64")#candidate|1142|()|const|uint64
var_1143 = relay.var("var_1143", dtype = "uint64", shape = (126, 2))#candidate|1143|(126, 2)|var|uint64
var_1144 = relay.var("var_1144", dtype = "uint64", shape = (840,))#candidate|1144|(840,)|var|uint64
call_1141 = relay.TupleGetItem(func_829_call(relay.reshape(const_1142.astype('uint64'), []), relay.reshape(var_1143.astype('uint64'), [252,]), relay.reshape(call_1134.astype('float64'), [11, 14, 8]), relay.reshape(var_1144.astype('uint64'), [7, 8, 15]), ), 2)
call_1145 = relay.TupleGetItem(func_835_call(relay.reshape(const_1142.astype('uint64'), []), relay.reshape(var_1143.astype('uint64'), [252,]), relay.reshape(call_1134.astype('float64'), [11, 14, 8]), relay.reshape(var_1144.astype('uint64'), [7, 8, 15]), ), 2)
uop_1148 = relay.erf(call_1141.astype('float64')) # shape=(11, 14, 8)
uop_1150 = relay.erf(call_1145.astype('float64')) # shape=(11, 14, 8)
func_983_call = mod.get_global_var('func_983')
func_985_call = mutated_mod.get_global_var('func_985')
var_1152 = relay.var("var_1152", dtype = "uint16", shape = (2, 560))#candidate|1152|(2, 560)|var|uint16
call_1151 = relay.TupleGetItem(func_983_call(relay.reshape(var_1152.astype('uint16'), [10, 16, 7])), 0)
call_1153 = relay.TupleGetItem(func_985_call(relay.reshape(var_1152.astype('uint16'), [10, 16, 7])), 0)
func_968_call = mod.get_global_var('func_968')
func_970_call = mutated_mod.get_global_var('func_970')
call_1161 = func_968_call()
call_1162 = func_968_call()
func_463_call = mod.get_global_var('func_463')
func_466_call = mutated_mod.get_global_var('func_466')
call_1177 = relay.TupleGetItem(func_463_call(relay.reshape(uop_1148.astype('int32'), [11, 14, 8]), relay.reshape(const_1142.astype('uint16'), []), ), 2)
call_1178 = relay.TupleGetItem(func_466_call(relay.reshape(uop_1148.astype('int32'), [11, 14, 8]), relay.reshape(const_1142.astype('uint16'), []), ), 2)
bop_1187 = relay.power(var_1143.astype('float64'), const_1142.astype('float64')) # shape=(126, 2)
uop_1191 = relay.rsqrt(call_1134.astype('float32')) # shape=(11, 14, 8)
uop_1193 = relay.rsqrt(call_1135.astype('float32')) # shape=(11, 14, 8)
func_968_call = mod.get_global_var('func_968')
func_970_call = mutated_mod.get_global_var('func_970')
call_1194 = func_968_call()
call_1195 = func_968_call()
func_1028_call = mod.get_global_var('func_1028')
func_1029_call = mutated_mod.get_global_var('func_1029')
call_1218 = relay.TupleGetItem(func_1028_call(), 1)
call_1219 = relay.TupleGetItem(func_1029_call(), 1)
func_983_call = mod.get_global_var('func_983')
func_985_call = mutated_mod.get_global_var('func_985')
call_1228 = relay.TupleGetItem(func_983_call(relay.reshape(call_1151.astype('uint16'), [10, 16, 7])), 0)
call_1229 = relay.TupleGetItem(func_985_call(relay.reshape(call_1151.astype('uint16'), [10, 16, 7])), 0)
uop_1236 = relay.log(var_1143.astype('float64')) # shape=(126, 2)
uop_1238 = relay.exp(var_1152.astype('float32')) # shape=(2, 560)
func_968_call = mod.get_global_var('func_968')
func_970_call = mutated_mod.get_global_var('func_970')
call_1247 = func_968_call()
call_1248 = func_968_call()
output = relay.Tuple([var_1144,uop_1148,call_1151,call_1161,call_1177,bop_1187,uop_1191,call_1194,call_1218,call_1228,uop_1236,uop_1238,call_1247,])
output2 = relay.Tuple([var_1144,uop_1150,call_1153,call_1162,call_1178,bop_1187,uop_1193,call_1195,call_1219,call_1229,uop_1236,uop_1238,call_1248,])
func_1257 = relay.Function([var_1143,var_1144,var_1152,], output)
mod['func_1257'] = func_1257
mod = relay.transform.InferType()(mod)
mutated_mod['func_1257'] = func_1257
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1257_call = mutated_mod.get_global_var('func_1257')
var_1259 = relay.var("var_1259", dtype = "uint64", shape = (126, 2))#candidate|1259|(126, 2)|var|uint64
var_1260 = relay.var("var_1260", dtype = "uint64", shape = (840,))#candidate|1260|(840,)|var|uint64
var_1261 = relay.var("var_1261", dtype = "uint16", shape = (2, 560))#candidate|1261|(2, 560)|var|uint16
call_1258 = func_1257_call(var_1259,var_1260,var_1261,)
output = call_1258
func_1262 = relay.Function([var_1259,var_1260,var_1261,], output)
mutated_mod['func_1262'] = func_1262
mutated_mod = relay.transform.InferType()(mutated_mod)
func_608_call = mod.get_global_var('func_608')
func_610_call = mutated_mod.get_global_var('func_610')
call_1282 = relay.TupleGetItem(func_608_call(), 0)
call_1283 = relay.TupleGetItem(func_610_call(), 0)
uop_1295 = relay.asinh(call_1282.astype('float64')) # shape=(11, 14, 8)
uop_1297 = relay.asinh(call_1283.astype('float64')) # shape=(11, 14, 8)
func_608_call = mod.get_global_var('func_608')
func_610_call = mutated_mod.get_global_var('func_610')
call_1298 = relay.TupleGetItem(func_608_call(), 0)
call_1299 = relay.TupleGetItem(func_610_call(), 0)
output = relay.Tuple([uop_1295,call_1298,])
output2 = relay.Tuple([uop_1297,call_1299,])
func_1302 = relay.Function([], output)
mod['func_1302'] = func_1302
mod = relay.transform.InferType()(mod)
mutated_mod['func_1302'] = func_1302
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1302_call = mutated_mod.get_global_var('func_1302')
call_1303 = func_1302_call()
output = call_1303
func_1304 = relay.Function([], output)
mutated_mod['func_1304'] = func_1304
mutated_mod = relay.transform.InferType()(mutated_mod)
func_608_call = mod.get_global_var('func_608')
func_610_call = mutated_mod.get_global_var('func_610')
call_1328 = relay.TupleGetItem(func_608_call(), 0)
call_1329 = relay.TupleGetItem(func_610_call(), 0)
output = call_1328
output2 = call_1329
func_1330 = relay.Function([], output)
mod['func_1330'] = func_1330
mod = relay.transform.InferType()(mod)
mutated_mod['func_1330'] = func_1330
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1330_call = mutated_mod.get_global_var('func_1330')
call_1331 = func_1330_call()
output = call_1331
func_1332 = relay.Function([], output)
mutated_mod['func_1332'] = func_1332
mutated_mod = relay.transform.InferType()(mutated_mod)
func_960_call = mod.get_global_var('func_960')
func_962_call = mutated_mod.get_global_var('func_962')
call_1352 = relay.TupleGetItem(func_960_call(), 0)
call_1353 = relay.TupleGetItem(func_962_call(), 0)
uop_1365 = relay.sinh(call_1352.astype('float32')) # shape=(2, 3, 1)
uop_1367 = relay.sinh(call_1353.astype('float32')) # shape=(2, 3, 1)
func_357_call = mod.get_global_var('func_357')
func_359_call = mutated_mod.get_global_var('func_359')
var_1373 = relay.var("var_1373", dtype = "uint16", shape = ())#candidate|1373|()|var|uint16
call_1372 = relay.TupleGetItem(func_357_call(relay.reshape(var_1373.astype('uint16'), [])), 1)
call_1374 = relay.TupleGetItem(func_359_call(relay.reshape(var_1373.astype('uint16'), [])), 1)
bop_1375 = relay.maximum(uop_1365.astype('int16'), var_1373.astype('int16')) # shape=(2, 3, 1)
bop_1378 = relay.maximum(uop_1367.astype('int16'), var_1373.astype('int16')) # shape=(2, 3, 1)
uop_1390 = relay.cosh(uop_1365.astype('float64')) # shape=(2, 3, 1)
uop_1392 = relay.cosh(uop_1367.astype('float64')) # shape=(2, 3, 1)
uop_1403 = relay.asinh(uop_1390.astype('float64')) # shape=(2, 3, 1)
uop_1405 = relay.asinh(uop_1392.astype('float64')) # shape=(2, 3, 1)
const_1407 = relay.const([[[6.382698,-0.653100,3.704008,-6.574954,-0.015621,-7.859977,9.573675,-3.308643,-2.693412,-4.998432,3.776316],[9.658152,9.447894,1.915521,9.030583,-0.341591,-9.099014,5.080627,8.880557,-6.795270,2.933097,-3.205595],[8.299452,-5.801934,-8.412885,-5.901426,-9.962556,-5.691773,7.952603,7.098546,-7.685874,-2.196174,-4.183381]],[[-6.168657,8.347334,-6.270809,7.733460,-7.526236,4.953899,2.060399,3.650752,4.524361,1.110448,-8.415814],[-1.188958,4.980654,5.925188,1.879450,1.841801,1.489318,-8.504678,-0.916083,-4.931944,-4.970898,8.499526],[2.440721,7.646201,7.534019,-4.963662,-1.522650,6.790663,9.158527,1.560931,-6.437203,-6.822661,6.926592]]], dtype = "float64")#candidate|1407|(2, 3, 11)|const|float64
bop_1408 = relay.logical_and(uop_1390.astype('bool'), const_1407.astype('bool')) # shape=(2, 3, 11)
bop_1411 = relay.logical_and(uop_1392.astype('bool'), const_1407.astype('bool')) # shape=(2, 3, 11)
func_487_call = mod.get_global_var('func_487')
func_489_call = mutated_mod.get_global_var('func_489')
call_1412 = relay.TupleGetItem(func_487_call(relay.reshape(var_1373.astype('int64'), [])), 1)
call_1413 = relay.TupleGetItem(func_489_call(relay.reshape(var_1373.astype('int64'), [])), 1)
func_695_call = mod.get_global_var('func_695')
func_696_call = mutated_mod.get_global_var('func_696')
call_1422 = relay.TupleGetItem(func_695_call(), 1)
call_1423 = relay.TupleGetItem(func_696_call(), 1)
bop_1424 = relay.mod(uop_1403.astype('float64'), relay.reshape(uop_1390.astype('float64'), relay.shape_of(uop_1403))) # shape=(2, 3, 1)
bop_1427 = relay.mod(uop_1405.astype('float64'), relay.reshape(uop_1392.astype('float64'), relay.shape_of(uop_1405))) # shape=(2, 3, 1)
uop_1428 = relay.asin(uop_1403.astype('float64')) # shape=(2, 3, 1)
uop_1430 = relay.asin(uop_1405.astype('float64')) # shape=(2, 3, 1)
func_137_call = mod.get_global_var('func_137')
func_141_call = mutated_mod.get_global_var('func_141')
call_1434 = relay.TupleGetItem(func_137_call(relay.reshape(call_1422.astype('uint64'), []), relay.reshape(call_1372.astype('uint64'), [3, 12, 7]), ), 0)
call_1435 = relay.TupleGetItem(func_141_call(relay.reshape(call_1422.astype('uint64'), []), relay.reshape(call_1372.astype('uint64'), [3, 12, 7]), ), 0)
output = relay.Tuple([call_1372,bop_1375,bop_1408,call_1412,call_1422,bop_1424,uop_1428,call_1434,])
output2 = relay.Tuple([call_1374,bop_1378,bop_1411,call_1413,call_1423,bop_1427,uop_1430,call_1435,])
func_1440 = relay.Function([var_1373,], output)
mod['func_1440'] = func_1440
mod = relay.transform.InferType()(mod)
var_1441 = relay.var("var_1441", dtype = "uint16", shape = ())#candidate|1441|()|var|uint16
output = func_1440(var_1441)
func_1442 = relay.Function([var_1441], output)
mutated_mod['func_1442'] = func_1442
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1470 = relay.const([[[4.601096,2.726449,1.488105,-6.500718,-6.281579,-9.123640,2.608671,-3.497753,0.595957,-3.406878,1.104050,8.979440],[-8.942316,3.540141,-7.391871,8.771353,7.994561,7.550135,-0.176780,-3.304997,-7.490155,8.850718,-0.553537,1.987567],[2.785888,9.494748,-7.740798,-7.180741,9.336923,2.483311,6.046720,2.262374,-1.043809,8.225650,-6.531736,5.392451]],[[-6.592082,-0.806303,2.298407,-0.002559,-5.548687,3.070625,-9.402435,0.870882,9.493194,1.813120,9.714970,-1.204777],[-9.000576,-5.191037,3.799962,7.539383,-8.143604,-9.291896,4.802102,-5.029584,-1.343839,-6.919654,-6.402450,-6.255264],[7.752593,-6.136996,-1.840033,-6.593528,-9.535449,-5.631597,-1.700014,-9.328403,8.659051,-9.585894,2.110876,-7.341428]],[[-6.351660,0.727703,-1.893480,5.980530,7.762921,-5.778577,-5.254038,-0.276619,3.333494,-2.787013,-9.774485,-9.451688],[6.345526,-8.103048,-4.404950,9.997495,-5.995427,4.166214,-0.202773,-1.632292,-7.585700,-3.174514,8.256006,3.504713],[2.398324,-1.345664,-9.052463,7.037130,-7.864434,8.439298,0.511067,5.327265,4.052485,-9.843990,8.580604,7.910698]],[[-3.024374,-8.619515,9.435542,-5.739649,9.034039,-0.118253,-5.052132,-5.960965,-2.744243,5.518685,-3.089995,1.513335],[3.214221,4.227791,-4.068635,-0.190459,-0.998381,-5.294165,-9.199407,-3.415589,2.464440,-8.833102,1.358933,-9.357670],[-1.569185,7.659371,5.057122,-7.295762,-7.456445,7.268540,-5.578268,3.163491,6.668283,-4.448869,6.658538,9.645707]],[[-4.054700,-3.244334,-2.820300,8.646473,-6.504491,6.533636,7.444366,-0.430112,-9.204791,-8.592694,9.904667,9.903752],[1.066708,-9.907611,6.003900,1.964536,0.962563,3.688414,8.494862,-9.376184,4.927876,4.104864,3.354903,-4.440778],[5.987819,2.127330,6.324323,3.865220,-9.734791,8.765754,-2.269438,8.024203,-3.420309,3.414078,7.796669,2.643949]],[[-1.642376,9.598304,-5.162142,8.385998,-4.946120,-6.977041,3.655639,-9.263483,4.236814,8.028915,9.071229,-4.777326],[2.815352,3.903885,0.103267,0.175308,7.283638,-2.407433,3.247848,1.310554,-8.568816,8.460450,-4.935120,8.458535],[3.241583,8.870544,-0.698966,-2.404761,2.752458,-4.525665,-2.690023,-8.850701,3.954409,3.573934,-3.077202,-8.980313]],[[-8.597880,0.670418,-0.625627,-1.199820,8.850202,-5.361533,5.188256,-4.978078,-0.092045,-5.397547,-9.889376,-0.470800],[2.256209,-5.561594,-3.794139,-6.573177,-6.231722,7.476427,-4.618973,-4.886318,7.414538,1.634170,0.136009,-4.554750],[0.790182,-1.551945,3.968801,4.234014,-3.648004,6.445368,-5.013077,4.110327,1.879795,6.364902,0.140673,5.427615]],[[-0.691682,3.293525,-8.941949,2.944351,-1.385003,-7.902384,-6.381426,-8.590978,1.904036,-1.488389,4.600218,2.220063],[-0.473458,9.999172,-5.487371,8.524641,8.870234,5.059358,-7.141876,9.140164,-2.399246,-9.306885,2.727188,-9.194268],[-8.626519,0.841577,-5.120405,-2.603617,7.011850,-7.906438,7.354232,9.330658,9.539044,-0.702943,4.069436,-3.075638]],[[1.350289,4.636047,-8.733786,-3.441907,-4.204315,-0.188183,-2.682677,7.084928,-6.431943,8.233190,4.276714,9.041670],[1.032094,-6.083266,0.223002,5.522441,-6.727794,-9.506475,-4.402762,9.824673,-9.541616,0.108930,9.632463,-4.633029],[4.212971,3.799683,-6.989366,4.670622,-2.625517,9.656376,-2.212628,1.666409,1.880540,2.397056,-7.044472,-1.735262]],[[1.105932,6.689428,-2.319279,-3.655419,2.608064,4.340284,-4.544635,-4.723788,-6.761344,5.928632,-4.384069,3.672278],[-9.826750,0.818959,-2.814266,4.984341,5.649043,-9.805095,-6.055163,6.122024,-9.393765,-8.801345,6.441154,4.789139],[-0.322854,2.892088,2.551224,-6.794692,5.995663,-5.439505,1.812000,6.559028,-4.362298,-2.115782,0.247140,0.640751]],[[-0.977797,-5.432982,-6.315073,-6.257635,-8.037674,3.976528,-8.884134,7.793027,4.343658,5.227965,1.797441,6.985901],[-1.860894,1.649366,-0.885282,8.837822,-6.533997,-7.225982,-1.008183,7.806650,-1.117751,-5.221357,-5.500071,9.891758],[-5.511342,-4.403048,2.525697,2.328748,9.860746,3.149935,4.145027,1.595225,2.875515,-7.163990,-2.430975,-3.127777]],[[-8.803527,5.965191,1.037956,-3.198779,-0.363264,7.302708,2.421609,4.254799,4.954129,-7.230052,-9.445691,-8.794533],[0.905884,0.144982,-7.789817,3.821948,-1.721834,5.423018,8.256523,1.065741,-4.718290,1.105083,-0.267430,3.157151],[-9.203140,-9.621760,6.287179,-8.619907,-8.764741,-8.820697,6.617743,7.840324,-9.290289,6.072482,8.802480,6.489119]],[[-8.966375,9.969883,-2.442777,-0.783914,-0.065565,5.688591,-0.852383,-2.458574,9.317064,0.982209,-7.434754,-1.872986],[-2.636812,-9.305941,2.602102,6.657046,1.995053,-3.758228,4.642181,-3.853589,8.077213,7.752288,6.598974,-0.264350],[-4.683466,3.966105,3.003147,-6.790205,-1.364005,5.394905,-9.650740,0.186150,4.712819,0.322444,-1.097497,-2.768862]],[[5.515167,3.868947,7.087577,7.094009,-0.341211,8.929910,5.549679,7.326759,-6.923271,8.907992,5.609190,-6.119166],[-2.324829,-9.912454,7.488892,-2.197440,-0.567513,4.805887,-0.542219,-2.647804,-0.423865,-0.870793,6.350758,5.636538],[-9.441892,-9.293946,1.602475,-7.939387,3.630882,-8.911485,7.936278,4.128283,4.915406,1.239202,-6.466695,-3.902112]]], dtype = "float64")#candidate|1470|(14, 3, 12)|const|float64
uop_1471 = relay.asinh(const_1470.astype('float64')) # shape=(14, 3, 12)
bop_1477 = relay.power(uop_1471.astype('float32'), relay.reshape(const_1470.astype('float32'), relay.shape_of(uop_1471))) # shape=(14, 3, 12)
var_1481 = relay.var("var_1481", dtype = "float64", shape = (14, 3, 12))#candidate|1481|(14, 3, 12)|var|float64
bop_1482 = relay.logical_and(const_1470.astype('bool'), relay.reshape(var_1481.astype('bool'), relay.shape_of(const_1470))) # shape=(14, 3, 12)
bop_1490 = relay.greater_equal(uop_1471.astype('bool'), relay.reshape(const_1470.astype('bool'), relay.shape_of(uop_1471))) # shape=(14, 3, 12)
output = relay.Tuple([bop_1477,bop_1482,bop_1490,])
output2 = relay.Tuple([bop_1477,bop_1482,bop_1490,])
func_1500 = relay.Function([var_1481,], output)
mod['func_1500'] = func_1500
mod = relay.transform.InferType()(mod)
mutated_mod['func_1500'] = func_1500
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1501 = relay.var("var_1501", dtype = "float64", shape = (14, 3, 12))#candidate|1501|(14, 3, 12)|var|float64
func_1500_call = mutated_mod.get_global_var('func_1500')
call_1502 = func_1500_call(var_1501)
output = call_1502
func_1503 = relay.Function([var_1501], output)
mutated_mod['func_1503'] = func_1503
mutated_mod = relay.transform.InferType()(mutated_mod)
func_960_call = mod.get_global_var('func_960')
func_962_call = mutated_mod.get_global_var('func_962')
call_1528 = relay.TupleGetItem(func_960_call(), 0)
call_1529 = relay.TupleGetItem(func_962_call(), 0)
func_1028_call = mod.get_global_var('func_1028')
func_1029_call = mutated_mod.get_global_var('func_1029')
call_1532 = relay.TupleGetItem(func_1028_call(), 3)
call_1533 = relay.TupleGetItem(func_1029_call(), 3)
output = relay.Tuple([call_1528,call_1532,])
output2 = relay.Tuple([call_1529,call_1533,])
func_1560 = relay.Function([], output)
mod['func_1560'] = func_1560
mod = relay.transform.InferType()(mod)
mutated_mod['func_1560'] = func_1560
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1560_call = mutated_mod.get_global_var('func_1560')
call_1561 = func_1560_call()
output = call_1561
func_1562 = relay.Function([], output)
mutated_mod['func_1562'] = func_1562
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1330_call = mod.get_global_var('func_1330')
func_1332_call = mutated_mod.get_global_var('func_1332')
call_1579 = func_1330_call()
call_1580 = func_1330_call()
output = relay.Tuple([call_1579,])
output2 = relay.Tuple([call_1580,])
func_1581 = relay.Function([], output)
mod['func_1581'] = func_1581
mod = relay.transform.InferType()(mod)
mutated_mod['func_1581'] = func_1581
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1581_call = mutated_mod.get_global_var('func_1581')
call_1582 = func_1581_call()
output = call_1582
func_1583 = relay.Function([], output)
mutated_mod['func_1583'] = func_1583
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1330_call = mod.get_global_var('func_1330')
func_1332_call = mutated_mod.get_global_var('func_1332')
call_1604 = func_1330_call()
call_1605 = func_1330_call()
func_463_call = mod.get_global_var('func_463')
func_466_call = mutated_mod.get_global_var('func_466')
var_1613 = relay.var("var_1613", dtype = "uint16", shape = ())#candidate|1613|()|var|uint16
call_1612 = relay.TupleGetItem(func_463_call(relay.reshape(call_1604.astype('int32'), [11, 14, 8]), relay.reshape(var_1613.astype('uint16'), []), ), 1)
call_1614 = relay.TupleGetItem(func_466_call(relay.reshape(call_1604.astype('int32'), [11, 14, 8]), relay.reshape(var_1613.astype('uint16'), []), ), 1)
output = relay.Tuple([call_1604,call_1612,var_1613,])
output2 = relay.Tuple([call_1605,call_1614,var_1613,])
func_1617 = relay.Function([var_1613,], output)
mod['func_1617'] = func_1617
mod = relay.transform.InferType()(mod)
mutated_mod['func_1617'] = func_1617
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1618 = relay.var("var_1618", dtype = "uint16", shape = ())#candidate|1618|()|var|uint16
func_1617_call = mutated_mod.get_global_var('func_1617')
call_1619 = func_1617_call(var_1618)
output = call_1619
func_1620 = relay.Function([var_1618], output)
mutated_mod['func_1620'] = func_1620
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1330_call = mod.get_global_var('func_1330')
func_1332_call = mutated_mod.get_global_var('func_1332')
call_1685 = func_1330_call()
call_1686 = func_1330_call()
func_695_call = mod.get_global_var('func_695')
func_696_call = mutated_mod.get_global_var('func_696')
call_1687 = relay.TupleGetItem(func_695_call(), 1)
call_1688 = relay.TupleGetItem(func_696_call(), 1)
bop_1692 = relay.right_shift(call_1687.astype('int8'), call_1685.astype('int8')) # shape=(11, 14, 8)
bop_1695 = relay.right_shift(call_1688.astype('int8'), call_1686.astype('int8')) # shape=(11, 14, 8)
func_1560_call = mod.get_global_var('func_1560')
func_1562_call = mutated_mod.get_global_var('func_1562')
call_1706 = relay.TupleGetItem(func_1560_call(), 0)
call_1707 = relay.TupleGetItem(func_1562_call(), 0)
func_960_call = mod.get_global_var('func_960')
func_962_call = mutated_mod.get_global_var('func_962')
call_1713 = relay.TupleGetItem(func_960_call(), 0)
call_1714 = relay.TupleGetItem(func_962_call(), 0)
func_426_call = mod.get_global_var('func_426')
func_427_call = mutated_mod.get_global_var('func_427')
call_1718 = relay.TupleGetItem(func_426_call(), 0)
call_1719 = relay.TupleGetItem(func_427_call(), 0)
output = relay.Tuple([bop_1692,call_1706,call_1713,call_1718,])
output2 = relay.Tuple([bop_1695,call_1707,call_1714,call_1719,])
func_1724 = relay.Function([], output)
mod['func_1724'] = func_1724
mod = relay.transform.InferType()(mod)
output = func_1724()
func_1725 = relay.Function([], output)
mutated_mod['func_1725'] = func_1725
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1581_call = mod.get_global_var('func_1581')
func_1583_call = mutated_mod.get_global_var('func_1583')
call_1726 = relay.TupleGetItem(func_1581_call(), 0)
call_1727 = relay.TupleGetItem(func_1583_call(), 0)
output = call_1726
output2 = call_1727
func_1731 = relay.Function([], output)
mod['func_1731'] = func_1731
mod = relay.transform.InferType()(mod)
mutated_mod['func_1731'] = func_1731
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1731_call = mutated_mod.get_global_var('func_1731')
call_1732 = func_1731_call()
output = call_1732
func_1733 = relay.Function([], output)
mutated_mod['func_1733'] = func_1733
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1753 = relay.var("var_1753", dtype = "float64", shape = (16, 5, 8))#candidate|1753|(16, 5, 8)|var|float64
uop_1754 = relay.sinh(var_1753.astype('float64')) # shape=(16, 5, 8)
output = relay.Tuple([uop_1754,])
output2 = relay.Tuple([uop_1754,])
func_1763 = relay.Function([var_1753,], output)
mod['func_1763'] = func_1763
mod = relay.transform.InferType()(mod)
mutated_mod['func_1763'] = func_1763
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1764 = relay.var("var_1764", dtype = "float64", shape = (16, 5, 8))#candidate|1764|(16, 5, 8)|var|float64
func_1763_call = mutated_mod.get_global_var('func_1763')
call_1765 = func_1763_call(var_1764)
output = call_1765
func_1766 = relay.Function([var_1764], output)
mutated_mod['func_1766'] = func_1766
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1794 = relay.var("var_1794", dtype = "int16", shape = (2, 15, 15))#candidate|1794|(2, 15, 15)|var|int16
var_1795 = relay.var("var_1795", dtype = "int16", shape = (2, 15, 15))#candidate|1795|(2, 15, 15)|var|int16
bop_1796 = relay.less(var_1794.astype('bool'), relay.reshape(var_1795.astype('bool'), relay.shape_of(var_1794))) # shape=(2, 15, 15)
output = bop_1796
output2 = bop_1796
func_1809 = relay.Function([var_1794,var_1795,], output)
mod['func_1809'] = func_1809
mod = relay.transform.InferType()(mod)
mutated_mod['func_1809'] = func_1809
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1809_call = mutated_mod.get_global_var('func_1809')
var_1811 = relay.var("var_1811", dtype = "int16", shape = (2, 15, 15))#candidate|1811|(2, 15, 15)|var|int16
var_1812 = relay.var("var_1812", dtype = "int16", shape = (2, 15, 15))#candidate|1812|(2, 15, 15)|var|int16
call_1810 = func_1809_call(var_1811,var_1812,)
output = call_1810
func_1813 = relay.Function([var_1811,var_1812,], output)
mutated_mod['func_1813'] = func_1813
mutated_mod = relay.transform.InferType()(mutated_mod)
func_960_call = mod.get_global_var('func_960')
func_962_call = mutated_mod.get_global_var('func_962')
call_1822 = relay.TupleGetItem(func_960_call(), 0)
call_1823 = relay.TupleGetItem(func_962_call(), 0)
func_1302_call = mod.get_global_var('func_1302')
func_1304_call = mutated_mod.get_global_var('func_1304')
call_1824 = relay.TupleGetItem(func_1302_call(), 1)
call_1825 = relay.TupleGetItem(func_1304_call(), 1)
uop_1834 = relay.exp(call_1822.astype('float64')) # shape=(2, 3, 1)
uop_1836 = relay.exp(call_1823.astype('float64')) # shape=(2, 3, 1)
func_910_call = mod.get_global_var('func_910')
func_913_call = mutated_mod.get_global_var('func_913')
var_1841 = relay.var("var_1841", dtype = "uint32", shape = (672,))#candidate|1841|(672,)|var|uint32
call_1840 = relay.TupleGetItem(func_910_call(relay.reshape(var_1841.astype('uint32'), [8, 12, 7]), relay.reshape(var_1841.astype('uint32'), [8, 12, 7]), ), 1)
call_1842 = relay.TupleGetItem(func_913_call(relay.reshape(var_1841.astype('uint32'), [8, 12, 7]), relay.reshape(var_1841.astype('uint32'), [8, 12, 7]), ), 1)
output = relay.Tuple([call_1824,uop_1834,call_1840,var_1841,])
output2 = relay.Tuple([call_1825,uop_1836,call_1842,var_1841,])
func_1856 = relay.Function([var_1841,], output)
mod['func_1856'] = func_1856
mod = relay.transform.InferType()(mod)
mutated_mod['func_1856'] = func_1856
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1857 = relay.var("var_1857", dtype = "uint32", shape = (672,))#candidate|1857|(672,)|var|uint32
func_1856_call = mutated_mod.get_global_var('func_1856')
call_1858 = func_1856_call(var_1857)
output = call_1858
func_1859 = relay.Function([var_1857], output)
mutated_mod['func_1859'] = func_1859
mutated_mod = relay.transform.InferType()(mutated_mod)
func_960_call = mod.get_global_var('func_960')
func_962_call = mutated_mod.get_global_var('func_962')
call_1942 = relay.TupleGetItem(func_960_call(), 0)
call_1943 = relay.TupleGetItem(func_962_call(), 0)
func_1330_call = mod.get_global_var('func_1330')
func_1332_call = mutated_mod.get_global_var('func_1332')
call_1955 = func_1330_call()
call_1956 = func_1330_call()
output = relay.Tuple([call_1942,call_1955,])
output2 = relay.Tuple([call_1943,call_1956,])
func_1965 = relay.Function([], output)
mod['func_1965'] = func_1965
mod = relay.transform.InferType()(mod)
output = func_1965()
func_1966 = relay.Function([], output)
mutated_mod['func_1966'] = func_1966
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1581_call = mod.get_global_var('func_1581')
func_1583_call = mutated_mod.get_global_var('func_1583')
call_2160 = relay.TupleGetItem(func_1581_call(), 0)
call_2161 = relay.TupleGetItem(func_1583_call(), 0)
var_2165 = relay.var("var_2165", dtype = "int32", shape = (11, 14, 8))#candidate|2165|(11, 14, 8)|var|int32
bop_2166 = relay.equal(call_2160.astype('bool'), relay.reshape(var_2165.astype('bool'), relay.shape_of(call_2160))) # shape=(11, 14, 8)
bop_2169 = relay.equal(call_2161.astype('bool'), relay.reshape(var_2165.astype('bool'), relay.shape_of(call_2161))) # shape=(11, 14, 8)
func_1010_call = mod.get_global_var('func_1010')
func_1013_call = mutated_mod.get_global_var('func_1013')
var_2182 = relay.var("var_2182", dtype = "uint64", shape = ())#candidate|2182|()|var|uint64
call_2181 = relay.TupleGetItem(func_1010_call(relay.reshape(var_2182.astype('uint64'), [])), 0)
call_2183 = relay.TupleGetItem(func_1013_call(relay.reshape(var_2182.astype('uint64'), [])), 0)
output = relay.Tuple([bop_2166,call_2181,var_2182,])
output2 = relay.Tuple([bop_2169,call_2183,var_2182,])
func_2187 = relay.Function([var_2165,var_2182,], output)
mod['func_2187'] = func_2187
mod = relay.transform.InferType()(mod)
mutated_mod['func_2187'] = func_2187
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2187_call = mutated_mod.get_global_var('func_2187')
var_2189 = relay.var("var_2189", dtype = "int32", shape = (11, 14, 8))#candidate|2189|(11, 14, 8)|var|int32
var_2190 = relay.var("var_2190", dtype = "uint64", shape = ())#candidate|2190|()|var|uint64
call_2188 = func_2187_call(var_2189,var_2190,)
output = call_2188
func_2191 = relay.Function([var_2189,var_2190,], output)
mutated_mod['func_2191'] = func_2191
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1724_call = mod.get_global_var('func_1724')
func_1725_call = mutated_mod.get_global_var('func_1725')
call_2227 = relay.TupleGetItem(func_1724_call(), 1)
call_2228 = relay.TupleGetItem(func_1725_call(), 1)
output = relay.Tuple([call_2227,])
output2 = relay.Tuple([call_2228,])
func_2249 = relay.Function([], output)
mod['func_2249'] = func_2249
mod = relay.transform.InferType()(mod)
mutated_mod['func_2249'] = func_2249
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2249_call = mutated_mod.get_global_var('func_2249')
call_2250 = func_2249_call()
output = call_2250
func_2251 = relay.Function([], output)
mutated_mod['func_2251'] = func_2251
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1581_call = mod.get_global_var('func_1581')
func_1583_call = mutated_mod.get_global_var('func_1583')
call_2268 = relay.TupleGetItem(func_1581_call(), 0)
call_2269 = relay.TupleGetItem(func_1583_call(), 0)
output = call_2268
output2 = call_2269
func_2289 = relay.Function([], output)
mod['func_2289'] = func_2289
mod = relay.transform.InferType()(mod)
mutated_mod['func_2289'] = func_2289
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2289_call = mutated_mod.get_global_var('func_2289')
call_2290 = func_2289_call()
output = call_2290
func_2291 = relay.Function([], output)
mutated_mod['func_2291'] = func_2291
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2411 = relay.const(-9.091876, dtype = "float64")#candidate|2411|()|const|float64
var_2412 = relay.var("var_2412", dtype = "float64", shape = (16, 6, 15))#candidate|2412|(16, 6, 15)|var|float64
bop_2413 = relay.floor_divide(const_2411.astype('float64'), var_2412.astype('float64')) # shape=(16, 6, 15)
output = bop_2413
output2 = bop_2413
func_2430 = relay.Function([var_2412,], output)
mod['func_2430'] = func_2430
mod = relay.transform.InferType()(mod)
var_2431 = relay.var("var_2431", dtype = "float64", shape = (16, 6, 15))#candidate|2431|(16, 6, 15)|var|float64
output = func_2430(var_2431)
func_2432 = relay.Function([var_2431], output)
mutated_mod['func_2432'] = func_2432
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1330_call = mod.get_global_var('func_1330')
func_1332_call = mutated_mod.get_global_var('func_1332')
call_2464 = func_1330_call()
call_2465 = func_1330_call()
uop_2471 = relay.log2(call_2464.astype('float32')) # shape=(11, 14, 8)
uop_2473 = relay.log2(call_2465.astype('float32')) # shape=(11, 14, 8)
output = relay.Tuple([uop_2471,])
output2 = relay.Tuple([uop_2473,])
func_2475 = relay.Function([], output)
mod['func_2475'] = func_2475
mod = relay.transform.InferType()(mod)
mutated_mod['func_2475'] = func_2475
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2475_call = mutated_mod.get_global_var('func_2475')
call_2476 = func_2475_call()
output = call_2476
func_2477 = relay.Function([], output)
mutated_mod['func_2477'] = func_2477
mutated_mod = relay.transform.InferType()(mutated_mod)
func_960_call = mod.get_global_var('func_960')
func_962_call = mutated_mod.get_global_var('func_962')
call_2488 = relay.TupleGetItem(func_960_call(), 0)
call_2489 = relay.TupleGetItem(func_962_call(), 0)
output = call_2488
output2 = call_2489
func_2490 = relay.Function([], output)
mod['func_2490'] = func_2490
mod = relay.transform.InferType()(mod)
output = func_2490()
func_2491 = relay.Function([], output)
mutated_mod['func_2491'] = func_2491
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1302_call = mod.get_global_var('func_1302')
func_1304_call = mutated_mod.get_global_var('func_1304')
call_2502 = relay.TupleGetItem(func_1302_call(), 0)
call_2503 = relay.TupleGetItem(func_1304_call(), 0)
func_695_call = mod.get_global_var('func_695')
func_696_call = mutated_mod.get_global_var('func_696')
call_2504 = relay.TupleGetItem(func_695_call(), 0)
call_2505 = relay.TupleGetItem(func_696_call(), 0)
func_1856_call = mod.get_global_var('func_1856')
func_1859_call = mutated_mod.get_global_var('func_1859')
const_2508 = relay.const([-8,3,-8,-3,-7,10,8,6,-5,8,7,-8,4,-3,4,-5,8,-4,-4,3,-8,7,-4,3,-3,-5,2,3,3,-5,6,1,-7,-10,10,4,-8,-3,5,-4,-8,9,4,-4,-7,-4,-8,-7,-10,9,2,-9,6,3,-7,-10,-5,6,10,-6,10,10,-9,-4,5,10,-9,-10,-10,-6,1,3,-6,7,9,-3,-5,9,-1,2,8,-5,-10,2,9,6,-6,6,-8,-6,-8,7,3,9,9,-9,-3,4,1,-3,5,-8,8,3,-9,-6,9,2,1,5,3,9,-10,1,-10,-2,4,6,-8,-10,9,5,9,-9,9,2,-7,1,-3,-1,-7,-8,4,4,4,-8,10,-2,-1,1,4,-5,2,2,-8,-8,5,9,1,-1,7,-9,-5,8,-1,-7,2,-10,7,2,3,4,8,-9,-5,4,-10,-9,-2,-10,-5,10,10,-4,1,4,-7,-2,-2,-2,1,-8,-8,7,-5,-5,-5,-10,6,-2,1,1,-6,1,-5,-4,-10,9,-1,-10,-3,-7,-3,-5,-2,-5,5,-10,-2,7,-5,-4,-5,-5,-7,-3,9,3,8,10,-5,2,5,-2,-3,4,2,-7,9,3,6,-10,-7,-6,1,6,2,-7,-10,-4,10,4,-6,-8,2,4,-7,-2,7,3,3,3,7,-4,1,-1,6,10,6,-8,9,-6,-4,5,4,9,-5,-7,-4,-1,-9,-3,-8,8,1,4,-7,8,-7,-5,9,10,-6,-8,8,-3,-4,5,-1,7,8,-4,2,-8,-3,1,5,-7,10,1,-7,-6,-1,2,-5,-6,2,8,9,4,7,5,-9,-4,10,-9,-10,-7,-10,-2,1,6,5,-7,1,8,9,1,4,8,-1,-2,-6,1,-9,8,3,3,-9,-4,-4,-10,4,2,9,3,-9,-10,-5,10,5,3,-2,-6,9,-3,2,9,-7,5,10,-5,-4,-5,-7,2,1,-10,4,-5,-5,7,2,-3,-6,4,-8,-7,5,1,5,3,-1,-10,-8,5,3,-3,9,-1,-4,-10,-5,9,9,1,-5,3,-9,8,-7,-3,6,-3,-1,9,1,-2,-6,-6,10,2,-6,-9,7,-4,-2,-5,4,3,-6,3,-2,4,5,-7,-1,-10,4,-2,9,-7,7,-9,-2,8,-5,-7,-7,6,-3,7,-2,1,-8,-10,10,-8,-1,-10,9,3,9,2,-1,8,-9,-9,5,8,-2,-10,8,-1,-3,4,-9,8,6,-3,-8,2,9,-10,-9,8,9,-8,-4,-5,-2,-2,5,10,-2,8,-6,-7,2,-1,-10,-4,7,-7,5,-1,-3,9,-3,-1,1,-2,10,4,-1,-4,-6,-9,2,-3,9,5,6,-10,-10,3,10,10,9,3,3,-10,-8,1,6,-9,9,-7,-8,4,-9,1,4,-1,-9,10,4,8,-8,3,4,-9,6,6,4,-1,-6,-4,6,-3,2,5,-5,9,4,9,4,1,-5,-3,6,2,6,4,1,-5,3,2,-4,3,-5,-6,-2,8,-3,-6,4,-4,-6,-10,-10,-4,4,-2,7,8,10,10,10,-9,10,5,7,-4,-10,2,9,2,9,4,9,-7,-8,1,6,3,7,-10,9,-7,-8,8,4,5,-6,-1,-2,6,-7,6,-8,1,-8,2,-7,-8,-10,4,-8,7,-7,1,-7,7,-3,-7,-5,8,9,3,-9,-1,-7,10,6,-1,8,-2,10,-10,6,6,6,-7,4,-3,10,1,-2,7,10,1,-2,4,-4,-5,-4,4,-4,6,-10,10], dtype = "uint32")#candidate|2508|(672,)|const|uint32
call_2507 = relay.TupleGetItem(func_1856_call(relay.reshape(const_2508.astype('uint32'), [672,])), 1)
call_2509 = relay.TupleGetItem(func_1859_call(relay.reshape(const_2508.astype('uint32'), [672,])), 1)
output = relay.Tuple([call_2502,call_2504,call_2507,const_2508,])
output2 = relay.Tuple([call_2503,call_2505,call_2509,const_2508,])
func_2516 = relay.Function([], output)
mod['func_2516'] = func_2516
mod = relay.transform.InferType()(mod)
mutated_mod['func_2516'] = func_2516
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2516_call = mutated_mod.get_global_var('func_2516')
call_2517 = func_2516_call()
output = call_2517
func_2518 = relay.Function([], output)
mutated_mod['func_2518'] = func_2518
mutated_mod = relay.transform.InferType()(mutated_mod)
func_695_call = mod.get_global_var('func_695')
func_696_call = mutated_mod.get_global_var('func_696')
call_2524 = relay.TupleGetItem(func_695_call(), 1)
call_2525 = relay.TupleGetItem(func_696_call(), 1)
output = relay.Tuple([call_2524,])
output2 = relay.Tuple([call_2525,])
func_2544 = relay.Function([], output)
mod['func_2544'] = func_2544
mod = relay.transform.InferType()(mod)
mutated_mod['func_2544'] = func_2544
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2544_call = mutated_mod.get_global_var('func_2544')
call_2545 = func_2544_call()
output = call_2545
func_2546 = relay.Function([], output)
mutated_mod['func_2546'] = func_2546
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1731_call = mod.get_global_var('func_1731')
func_1733_call = mutated_mod.get_global_var('func_1733')
call_2570 = func_1731_call()
call_2571 = func_1731_call()
func_910_call = mod.get_global_var('func_910')
func_913_call = mutated_mod.get_global_var('func_913')
var_2582 = relay.var("var_2582", dtype = "uint32", shape = (672,))#candidate|2582|(672,)|var|uint32
call_2581 = relay.TupleGetItem(func_910_call(relay.reshape(var_2582.astype('uint32'), [8, 12, 7]), relay.reshape(var_2582.astype('uint32'), [8, 12, 7]), ), 2)
call_2583 = relay.TupleGetItem(func_913_call(relay.reshape(var_2582.astype('uint32'), [8, 12, 7]), relay.reshape(var_2582.astype('uint32'), [8, 12, 7]), ), 2)
output = relay.Tuple([call_2570,call_2581,var_2582,])
output2 = relay.Tuple([call_2571,call_2583,var_2582,])
func_2591 = relay.Function([var_2582,], output)
mod['func_2591'] = func_2591
mod = relay.transform.InferType()(mod)
var_2592 = relay.var("var_2592", dtype = "uint32", shape = (672,))#candidate|2592|(672,)|var|uint32
output = func_2591(var_2592)
func_2593 = relay.Function([var_2592], output)
mutated_mod['func_2593'] = func_2593
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2595 = relay.const([[[8,6,9,-6,-4,2,-6,2],[3,1,-6,2,-8,-8,5,2],[9,-9,-3,-1,-1,-10,-6,-7],[6,2,4,-3,-4,-3,6,2],[-3,-2,-9,3,3,-7,8,7],[-1,-9,4,9,-2,7,-8,-1],[-4,-9,-5,-1,10,9,-3,5],[7,2,3,-9,4,10,5,-4],[6,1,8,10,-1,7,7,-9],[5,6,-3,-2,9,10,5,4],[-9,-1,-7,6,-1,-2,-6,-1],[-4,-6,1,5,-2,-7,-9,8]],[[-6,-5,-1,-10,6,9,5,-3],[-8,-10,-9,-1,8,-7,9,-6],[-4,5,-4,8,-9,3,10,4],[7,8,-9,-8,-7,5,-10,-8],[-2,4,9,7,2,3,8,-9],[-3,2,8,-10,-6,-10,6,5],[-2,-5,10,3,3,-3,3,-7],[-10,10,-10,-2,5,-3,1,-2],[-6,6,-10,7,4,6,3,-6],[2,-3,-6,9,7,4,-1,-1],[-3,2,-7,-9,-10,-10,8,-7],[2,5,5,9,7,9,2,-4]],[[8,-10,-8,8,6,2,-4,6],[-9,3,-6,-5,10,2,4,6],[-5,-1,-9,-10,6,9,-1,5],[-8,1,5,-9,-9,-4,7,7],[10,5,-6,4,-7,2,-10,5],[7,1,3,4,1,5,2,1],[9,-1,1,6,8,5,5,5],[-7,2,6,-1,6,6,9,9],[-3,4,-6,1,8,-4,-5,5],[-5,3,-2,10,-2,5,-4,-3],[5,-1,8,6,8,-1,9,9],[2,7,6,-4,-6,4,-5,6]],[[-2,2,-1,-10,-10,-5,8,3],[6,5,-9,-4,10,-2,-3,-5],[-9,7,-7,10,7,-4,-9,-4],[-9,9,-10,1,-9,6,-5,-6],[-10,-4,-9,4,-10,-10,7,6],[-5,-4,-7,8,1,-7,5,-1],[-6,3,9,-1,6,-10,7,1],[-10,-8,3,3,10,-10,-1,3],[8,-3,1,-8,5,-4,-5,-6],[-1,1,2,9,4,-10,-2,2],[-7,7,-9,9,-2,-10,-7,1],[3,-3,8,1,-3,8,-2,-5]],[[7,10,-6,4,3,4,-10,-9],[9,-10,-6,-10,1,-4,8,5],[1,3,-6,3,1,-9,-4,-6],[4,1,-8,-9,-9,-4,-2,2],[4,-9,2,-10,-3,4,9,10],[7,-5,2,-3,-9,-8,6,6],[-7,10,1,4,9,1,7,5],[-5,-8,4,-10,8,8,9,-4],[9,8,4,-3,-10,-4,6,-3],[-8,9,-2,-9,-6,2,10,-6],[10,10,7,-8,10,6,-1,-8],[-7,3,6,8,10,1,-8,9]]], dtype = "int64")#candidate|2595|(5, 12, 8)|const|int64
var_2596 = relay.var("var_2596", dtype = "int64", shape = (5, 12, 8))#candidate|2596|(5, 12, 8)|var|int64
bop_2597 = relay.bitwise_xor(const_2595.astype('int64'), relay.reshape(var_2596.astype('int64'), relay.shape_of(const_2595))) # shape=(5, 12, 8)
func_311_call = mod.get_global_var('func_311')
func_314_call = mutated_mod.get_global_var('func_314')
const_2602 = relay.const(-3, dtype = "uint64")#candidate|2602|()|const|uint64
var_2603 = relay.var("var_2603", dtype = "uint64", shape = (1, 252))#candidate|2603|(1, 252)|var|uint64
call_2601 = relay.TupleGetItem(func_311_call(relay.reshape(const_2602.astype('uint64'), []), relay.reshape(var_2603.astype('uint64'), [1, 252]), ), 0)
call_2604 = relay.TupleGetItem(func_314_call(relay.reshape(const_2602.astype('uint64'), []), relay.reshape(var_2603.astype('uint64'), [1, 252]), ), 0)
const_2606 = relay.const([[[9,1,-1,10,6,-2,4,-1,10,-10,6,9],[-5,2,8,-4,-5,2,-10,8,2,4,-7,5],[-2,-4,-9,4,3,7,-5,8,-8,6,3,-3],[-3,10,-3,7,4,-6,6,4,-7,3,-4,3],[-3,9,2,-10,-10,-7,7,-8,9,1,-5,9],[8,7,-4,3,1,3,5,-10,-4,-5,5,2],[-7,-9,10,6,9,1,4,-3,7,8,-1,-4],[-9,8,4,6,-4,6,5,5,3,-9,9,2],[8,-5,-10,4,10,1,-1,-5,-4,-1,1,2],[10,-3,-1,-5,4,-8,1,-4,-3,4,4,8],[-10,-8,5,-7,1,-5,4,3,-10,-2,2,-1],[-1,-6,-4,-4,5,5,1,-6,3,-5,1,-3],[-9,-3,1,6,9,-6,8,7,-1,5,6,2]],[[-3,6,-7,7,6,-6,6,-8,6,7,-5,9],[-7,-7,6,-6,-10,-4,-3,-2,-3,-5,-2,3],[8,-2,-4,-10,5,-8,1,-1,8,8,6,-2],[10,-9,2,-10,2,5,3,1,-7,9,4,-6],[5,4,4,4,3,8,-3,-10,-10,-5,2,-1],[4,4,-1,-10,6,2,8,-8,7,-8,4,-9],[3,-7,9,-6,1,-1,-2,-1,-3,-10,6,5],[4,6,-3,2,9,3,-1,-1,8,-5,2,-1],[-8,9,-1,-9,-8,-4,-2,-9,8,-8,-10,1],[10,-2,-1,-1,-8,-5,5,-5,-9,-5,5,-1],[-5,-4,-6,7,-1,2,4,3,4,-10,-9,3],[3,-10,-4,-3,-10,6,-10,-3,3,-4,-9,-8],[4,1,2,5,1,-6,-6,4,4,1,-6,-6]],[[10,-6,1,-1,2,10,5,1,-9,-3,-4,9],[8,3,-4,2,2,-4,-10,8,6,-7,-1,7],[5,-5,8,8,-5,9,-1,5,9,-6,4,-2],[-2,-9,7,-5,7,-3,7,10,-4,3,-2,-1],[-8,9,-3,-2,9,-9,9,-1,5,1,5,6],[-2,5,7,-4,-2,-7,-5,-1,-10,3,4,8],[-9,-3,-2,-4,-8,-10,-6,10,-9,-7,5,1],[6,-7,-9,2,-5,2,4,6,8,8,2,6],[-6,8,-8,-9,2,-5,-4,-10,-1,-8,10,-10],[-2,4,6,-5,-2,-6,-1,-5,4,5,8,-6],[-8,8,10,8,-6,-4,-2,-7,-4,-5,9,-8],[-1,-2,8,7,-2,-4,3,-2,6,-1,9,-3],[2,-5,-9,5,-6,8,-5,-2,2,-9,9,3]],[[-1,4,-4,-10,6,-7,-10,6,9,2,10,1],[1,8,3,-3,-8,6,-5,-8,4,7,-8,-2],[8,-3,9,2,-5,-7,-2,5,-1,-1,7,-9],[-5,-7,-1,1,4,-8,7,-2,-8,1,3,-1],[-8,1,4,-8,-6,3,5,-7,-6,-3,-4,-5],[6,-4,5,3,10,9,-2,4,-4,-5,8,10],[-6,-9,10,5,-4,-6,8,2,-5,-3,-10,7],[3,4,4,9,9,-2,-4,4,8,4,-1,-6],[-7,-3,6,-2,-2,2,10,-7,9,-7,-8,10],[-3,4,3,10,8,9,-5,-5,-7,6,10,6],[5,-4,-6,-1,-3,3,-6,7,8,10,-7,4],[-3,1,4,-5,-3,-3,5,8,-8,5,-3,8],[6,-9,-2,-5,3,-8,-7,7,-2,-9,-4,-7]],[[9,8,2,-5,3,-1,9,10,6,-1,9,-1],[10,-9,8,-9,-8,8,3,10,1,3,-1,-2],[-8,-8,-4,-9,-2,1,6,8,8,-8,1,-1],[1,-2,4,9,-10,-1,9,-1,2,-2,3,-4],[6,-6,-2,-1,8,7,-9,3,7,-6,-6,7],[8,-6,-9,-3,-4,4,-3,-1,8,4,6,1],[-3,-10,-3,-9,-6,3,7,10,5,9,9,-1],[-8,6,-2,7,-3,6,-6,6,-2,-9,3,2],[5,7,9,-1,-5,-3,4,-4,-9,-3,-7,-8],[6,-8,1,8,-1,-8,-5,9,5,-8,-2,-8],[-3,7,-7,-9,-6,-1,-8,1,-6,-2,-9,2],[5,-5,-10,-9,1,3,2,-1,10,5,3,-7],[-6,-1,-2,-9,2,-5,6,-7,9,-6,-3,-1]],[[-1,9,2,-6,-7,-1,1,-5,3,-7,-3,5],[6,4,8,-2,-10,4,9,10,6,-6,-3,-2],[-10,-5,-3,6,2,9,-3,-1,-2,-5,-7,-8],[8,2,6,8,-10,10,5,-3,3,-9,2,9],[4,-6,9,-4,9,-8,9,-10,9,4,-5,-1],[8,-5,9,-6,-10,-6,10,7,7,4,-1,4],[-6,4,-5,10,-4,-6,10,7,-4,-8,4,-4],[1,6,-6,-2,9,4,2,9,-8,10,-5,-8],[2,5,-3,5,-9,-8,1,7,-7,-6,-4,4],[8,-2,2,3,-7,-8,-9,6,5,-5,7,8],[5,-2,9,-3,-1,1,2,-7,-4,1,1,-3],[3,-3,-2,-4,-7,5,6,2,-10,3,6,-5],[7,4,-3,-4,-5,-9,-10,-5,1,2,8,5]],[[4,4,-9,10,2,6,1,4,-7,-6,-3,-3],[-8,4,-8,6,8,-3,6,5,-9,3,-8,-7],[-9,-3,3,9,-10,9,-1,-9,-4,5,8,-8],[-10,-7,10,-7,-9,3,6,-3,-4,-6,7,3],[-10,9,-2,-4,-2,3,7,2,10,-7,-7,5],[-5,6,8,1,-10,7,1,-4,-2,-4,-7,-6],[2,-5,6,-10,-3,-2,6,1,4,-7,7,8],[10,-10,-10,4,-10,3,-9,8,7,-4,-3,-10],[1,2,1,-9,3,8,6,7,2,-3,-3,4],[-2,7,-3,2,4,-4,-5,-6,2,4,-5,-3],[3,8,8,-7,10,6,1,-7,-4,-10,4,9],[-7,4,-4,-8,5,-4,-10,7,-5,3,-1,-10],[1,-3,-5,1,-5,-3,3,7,-9,-5,2,-7]],[[3,4,10,10,-6,-6,-7,-1,3,-1,-7,-6],[-9,-5,1,7,-4,1,-7,-7,3,-1,4,3],[10,-4,2,5,-9,2,4,7,2,-4,-8,-1],[-8,-1,8,10,10,5,3,5,2,-5,9,-2],[7,-10,-9,-6,-5,9,-3,-1,4,4,8,1],[-7,4,-6,6,4,-10,9,4,-5,7,-4,10],[4,5,-5,2,3,-7,4,-6,-9,5,-4,-2],[-2,6,9,3,-2,-7,-7,9,5,-2,-9,-9],[-7,-8,3,-10,1,10,2,3,-4,-10,-9,2],[5,3,4,-2,-8,2,10,-6,-7,-9,10,4],[-2,4,3,5,1,2,2,6,2,-3,1,-3],[8,1,6,1,-2,-9,-10,-5,-4,6,-8,-8],[-4,7,2,6,-4,7,2,9,-2,1,5,-5]],[[-2,7,-7,4,-9,7,-1,-1,-9,6,-8,-7],[5,4,-5,-1,2,-9,-4,-8,-2,-4,7,-7],[-6,10,-7,-4,-7,2,-7,-9,10,8,10,7],[-1,6,-6,8,7,-6,5,7,-8,5,4,4],[3,8,-8,-7,5,8,-8,3,-4,-10,-9,-4],[7,-2,-5,-3,-6,2,-5,2,-2,-1,-1,-4],[3,6,2,-9,-1,-8,-7,5,-5,9,5,9],[-6,-8,5,1,-7,-2,-9,7,-3,-6,-9,6],[-7,-3,-8,10,5,10,9,9,-8,-4,-3,-7],[-8,-7,-2,-9,9,1,-4,-1,6,-8,1,-8],[8,8,-3,-8,-5,-7,9,6,-8,5,-8,9],[-8,-7,-6,-9,-9,8,1,-4,-2,-3,-7,-8],[8,4,-10,9,2,8,-3,2,6,-7,-7,-1]]], dtype = "uint64")#candidate|2606|(9, 13, 12)|const|uint64
bop_2607 = relay.less_equal(const_2602.astype('bool'), const_2606.astype('bool')) # shape=(9, 13, 12)
func_2544_call = mod.get_global_var('func_2544')
func_2546_call = mutated_mod.get_global_var('func_2546')
call_2614 = relay.TupleGetItem(func_2544_call(), 0)
call_2615 = relay.TupleGetItem(func_2546_call(), 0)
func_1257_call = mod.get_global_var('func_1257')
func_1262_call = mutated_mod.get_global_var('func_1262')
const_2622 = relay.const([1,8,6,-2,1,-10,3,4,3,10,6,5,-10,-2,4,-1,-9,-9,-6,9,10,10,7,3,-3,-3,-10,3,-5,-5,2,7,6,6,4,-1,-7,8,-2,-3,-3,-4,-7,4,-5,2,-8,9,-3,-8,-10,-3,-8,10,9,5,-2,-6,-9,10,1,1,10,-3,-3,-2,-10,2,4,-7,5,-7,-4,-5,-5,-5,6,-10,-6,-9,-6,3,-4,1,7,2,-2,1,4,-9,3,-9,-9,-5,-2,5,-7,-1,3,10,-1,-6,-1,-1,2,-6,-3,4,-4,9,7,-3,2,7,7,9,-10,-5,9,10,5,6,2,3,1,3,6,2,1,7,-5,-8,-9,-9,-10,-2,4,-6,-10,-2,1,-8,-1,-8,8,-2,10,-1,4,9,-9,-8,1,-1,3,1,-1,4,9,-6,-5,-3,8,-4,-4,-6,-6,-7,-10,-5,4,-8,6,8,-2,-4,3,-4,1,-5,2,9,-6,2,-7,-1,-6,-7,-9,-10,1,9,-1,-9,10,-7,-3,-8,-3,7,9,2,-6,-8,5,-7,-1,-4,-9,7,5,2,2,-1,10,6,5,-7,-8,8,-2,-10,1,-7,7,10,10,1,9,1,-9,3,7,-7,-2,8,9,-8,4,-1,-1,-2,-10,-5,3,10,-4,-6,-2,8,5,9,4,4,-3,8,3,-7,10,-4,9,-5,-7,-8,3,5,1,-3,1,4,2,10,-1,10,10,-6,-8,-3,-1,5,6,3,-4,-2,-6,1,-8,5,9,-1,-9,-7,8,-3,-3,-5,10,6,-6,1,5,-10,-4,-2,-2,1,10,10,1,6,-4,3,-1,-10,-9,9,-2,7,-5,8,-4,1,-8,-1,-8,1,10,-8,6,5,8,1,2,7,-9,-7,3,-4,-2,-7,3,-4,5,3,-9,-9,4,-8,-8,-6,-9,7,-4,4,7,6,-1,-5,2,10,-10,-8,-6,3,-1,-10,-3,-4,-7,2,-10,-6,-9,-1,-10,-2,-9,5,9,1,6,-2,-8,5,-5,-9,-5,9,-5,5,-1,-4,-9,10,-6,10,2,-10,-8,-6,-3,-1,-10,-4,-1,10,8,-4,2,5,-5,-9,-4,-7,-5,-9,-8,7,-1,2,-10,5,6,-4,-3,8,1,7,6,2,-7,-10,-1,2,7,-7,-6,-6,-2,-3,-9,-5,8,-10,5,8,2,8,2,-9,-6,6,9,-4,-2,5,8,6,1,-2,7,-8,-5,-6,8,6,2,-6,5,1,9,-3,-6,-4,-4,-1,6,1,10,10,5,-2,9,-7,9,6,-3,-6,-7,-4,-7,-3,8,6,-3,4,4,4,-5,10,10,2,4,-10,6,-1,1,-8,7,-7,-2,-8,-8,-2,5,4,7,-9,-4,1,5,5,-5,6,-10,-4,-5,-1,-7,5,4,-9,7,-1,7,1,5,1,-10,3,10,-2,-10,-10,-5,-8,6,9,5,4,-3,5,2,7,-3,-4,8,1,-1,4,6,3,1,-5,4,-8,6,-3,1,2,2,8,2,-1,-10,8,-9,8,-5,-6,-2,-3,10,-9,-8,5,-7,-4,-4,-1,-10,-10,10,-10,-1,-3,3,-1,2,3,1,3,-5,-6,-2,3,5,-4,1,1,2,-5,8,7,-8,-3,2,-6,3,-6,-8,-10,4,8,-7,7,3,-2,8,2,-4,4,10,-3,-1,-9,-9,3,-2,9,2,-9,-8,5,-2,3,-1,-2,-8,-6,-5,9,6,9,3,-7,6,7,7,-3,8,-7,-2,1,-3,8,-4,3,-8,-9,-2,5,2,-3,5,-2,-1,-5,-5,4,3,-9,10,-6,6,-9,-2,8,10,7,-9,-10,5,5,10,-1,1,2,1,10,-3,-6,5,1,7,-1,-6,-7,4,10,-9,-1,-8,-2,10,6,10,10,-4,-1,10,7,10,-4,6,-2,-6,7,-5,3,-8,-1,-1,-2,-2,7,-4,8,8,2,-8,1,7,-8,-5,-10,-1,1,-9,-8,7,-5,-10,7,-4,6,-1,-4,4,-3,-4,-6,-3,7,-2,-5,10,10,-2,2,5,-8,4,7,3,-1,-4,-1,3,-10,-5,-4,4,7,-2,-4,6,3,3,9,1,-2,-6,1,3,2,6,-2,-1,-8,7,-8,-1,2,1,9,-3,7,6,-9,-1,8,9,8,1,3,-8,-1,-3,5,8,6,-7,-1,4,5,-10,-1,-4,-1,8,3,6,-7,8,-3,-7,8,-3,-8], dtype = "uint64")#candidate|2622|(840,)|const|uint64
var_2623 = relay.var("var_2623", dtype = "uint16", shape = (1120,))#candidate|2623|(1120,)|var|uint16
call_2621 = relay.TupleGetItem(func_1257_call(relay.reshape(var_2603.astype('uint64'), [126, 2]), relay.reshape(const_2622.astype('uint64'), [840,]), relay.reshape(var_2623.astype('uint16'), [2, 560]), ), 8)
call_2624 = relay.TupleGetItem(func_1262_call(relay.reshape(var_2603.astype('uint64'), [126, 2]), relay.reshape(const_2622.astype('uint64'), [840,]), relay.reshape(var_2623.astype('uint16'), [2, 560]), ), 8)
func_1440_call = mod.get_global_var('func_1440')
func_1442_call = mutated_mod.get_global_var('func_1442')
call_2629 = relay.TupleGetItem(func_1440_call(relay.reshape(call_2614.astype('uint16'), [])), 2)
call_2630 = relay.TupleGetItem(func_1442_call(relay.reshape(call_2614.astype('uint16'), [])), 2)
output = relay.Tuple([bop_2597,call_2601,var_2603,bop_2607,call_2614,call_2621,const_2622,var_2623,call_2629,])
output2 = relay.Tuple([bop_2597,call_2604,var_2603,bop_2607,call_2615,call_2624,const_2622,var_2623,call_2630,])
func_2633 = relay.Function([var_2596,var_2603,var_2623,], output)
mod['func_2633'] = func_2633
mod = relay.transform.InferType()(mod)
mutated_mod['func_2633'] = func_2633
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2633_call = mutated_mod.get_global_var('func_2633')
var_2635 = relay.var("var_2635", dtype = "int64", shape = (5, 12, 8))#candidate|2635|(5, 12, 8)|var|int64
var_2636 = relay.var("var_2636", dtype = "uint64", shape = (1, 252))#candidate|2636|(1, 252)|var|uint64
var_2637 = relay.var("var_2637", dtype = "uint16", shape = (1120,))#candidate|2637|(1120,)|var|uint16
call_2634 = func_2633_call(var_2635,var_2636,var_2637,)
output = call_2634
func_2638 = relay.Function([var_2635,var_2636,var_2637,], output)
mutated_mod['func_2638'] = func_2638
mutated_mod = relay.transform.InferType()(mutated_mod)
func_608_call = mod.get_global_var('func_608')
func_610_call = mutated_mod.get_global_var('func_610')
call_2668 = relay.TupleGetItem(func_608_call(), 0)
call_2669 = relay.TupleGetItem(func_610_call(), 0)
output = relay.Tuple([call_2668,])
output2 = relay.Tuple([call_2669,])
func_2673 = relay.Function([], output)
mod['func_2673'] = func_2673
mod = relay.transform.InferType()(mod)
output = func_2673()
func_2674 = relay.Function([], output)
mutated_mod['func_2674'] = func_2674
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1302_call = mod.get_global_var('func_1302')
func_1304_call = mutated_mod.get_global_var('func_1304')
call_2675 = relay.TupleGetItem(func_1302_call(), 0)
call_2676 = relay.TupleGetItem(func_1304_call(), 0)
output = call_2675
output2 = call_2676
func_2683 = relay.Function([], output)
mod['func_2683'] = func_2683
mod = relay.transform.InferType()(mod)
output = func_2683()
func_2684 = relay.Function([], output)
mutated_mod['func_2684'] = func_2684
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2490_call = mod.get_global_var('func_2490')
func_2491_call = mutated_mod.get_global_var('func_2491')
call_2694 = func_2490_call()
call_2695 = func_2490_call()
output = relay.Tuple([call_2694,])
output2 = relay.Tuple([call_2695,])
func_2698 = relay.Function([], output)
mod['func_2698'] = func_2698
mod = relay.transform.InferType()(mod)
mutated_mod['func_2698'] = func_2698
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2698_call = mutated_mod.get_global_var('func_2698')
call_2699 = func_2698_call()
output = call_2699
func_2700 = relay.Function([], output)
mutated_mod['func_2700'] = func_2700
mutated_mod = relay.transform.InferType()(mutated_mod)
func_426_call = mod.get_global_var('func_426')
func_427_call = mutated_mod.get_global_var('func_427')
call_2718 = relay.TupleGetItem(func_426_call(), 0)
call_2719 = relay.TupleGetItem(func_427_call(), 0)
uop_2720 = relay.exp(call_2718.astype('float64')) # shape=(11, 14, 8)
uop_2722 = relay.exp(call_2719.astype('float64')) # shape=(11, 14, 8)
func_1809_call = mod.get_global_var('func_1809')
func_1813_call = mutated_mod.get_global_var('func_1813')
const_2732 = relay.const([9,7,2,4,7,-4,5,10,-2,-8,4,6,-3,3,8,2,-1,-5,-10,2,4,-2,5,-3,-10,1,-1,5,7,-8,9,2,-8,-6,7,-6,3,4,-1,-2,-9,6,-9,4,8,-2,-1,-10,3,-9,-3,3,-4,-3,-3,-7,-7,2,3,-3,-7,1,-1,-7,8,-7,1,-6,-7,2,-5,4,-2,-9,2,8,-1,7,2,6,-10,-9,-3,5,-6,-3,6,3,6,4,8,-9,-1,-8,-10,2,-7,2,8,1,-4,6,-2,9,3,-5,-5,7,-3,-10,-1,-3,-3,-10,2,-6,-4,8,1,5,1,4,-6,-4,8,-2,-6,9,1,10,-9,-2,1,10,-7,8,4,-4,5,-9,-1,3,-5,-7,-10,-2,5,3,-3,-10,7,-10,1,3,-3,-2,3,-2,-8,7,-5,-6,-2,-6,1,7,5,-10,3,-6,-6,-1,-2,1,1,7,-6,6,-3,3,10,3,-9,-6,8,9,8,5,4,-9,4,10,-10,-10,-9,-6,-4,6,4,6,-2,6,-8,2,-6,6,9,-2,10,-2,6,10,9,-5,-8,4,7,-1,-10,-4,4,-8,8,1,-3,-9,-5,9,4,8,5,1,-4,7,-3,-2,-3,-9,-2,8,-5,4,-5,3,-9,1,-3,-5,5,10,-3,7,3,-4,6,2,-9,1,-9,3,-3,1,-7,2,-8,-3,5,6,6,6,-4,-5,-3,8,1,2,-6,-2,9,8,-6,-6,-9,-2,-4,10,5,10,-4,-1,-2,8,6,-2,6,2,-10,-7,-3,-7,5,5,-3,-7,-5,-1,-1,-4,1,-4,9,10,-6,-10,4,-6,-3,9,7,-2,-4,9,1,6,1,-10,-6,10,7,-3,-5,2,-1,5,-6,-10,9,-10,3,4,-6,6,7,5,6,-9,-8,-1,1,-7,-5,1,-6,-6,-9,-7,-7,8,-1,-9,1,-9,8,-8,-10,-10,-3,8,-4,-10,-7,7,-2,-9,7,1,6,9,-4,3,-5,8,3,-7,10,-9,8,2,-2,4,-7,-9,9,-6,-6,-6,3,-9,9,5,-7,8,-2,-5,1,4,-6,-2,-3,-7,-9,-10,-6,3,8,7,-4,-1,5,-3,-7,4,-1,8,5,3,-8,-10,-3,-2,-1,-6,-3,-5,3,5,-4,3,5,9,5,-6,6,-9,-9,2,7,-6,7,9], dtype = "int16")#candidate|2732|(450,)|const|int16
call_2731 = func_1809_call(relay.reshape(const_2732.astype('int16'), [2, 15, 15]), relay.reshape(const_2732.astype('int16'), [2, 15, 15]), )
call_2733 = func_1809_call(relay.reshape(const_2732.astype('int16'), [2, 15, 15]), relay.reshape(const_2732.astype('int16'), [2, 15, 15]), )
func_608_call = mod.get_global_var('func_608')
func_610_call = mutated_mod.get_global_var('func_610')
call_2745 = relay.TupleGetItem(func_608_call(), 0)
call_2746 = relay.TupleGetItem(func_610_call(), 0)
uop_2755 = relay.sin(call_2718.astype('float64')) # shape=(11, 14, 8)
uop_2757 = relay.sin(call_2719.astype('float64')) # shape=(11, 14, 8)
func_2475_call = mod.get_global_var('func_2475')
func_2477_call = mutated_mod.get_global_var('func_2477')
call_2760 = relay.TupleGetItem(func_2475_call(), 0)
call_2761 = relay.TupleGetItem(func_2477_call(), 0)
uop_2765 = relay.atan(uop_2755.astype('float32')) # shape=(11, 14, 8)
uop_2767 = relay.atan(uop_2757.astype('float32')) # shape=(11, 14, 8)
var_2775 = relay.var("var_2775", dtype = "bool", shape = (2, 15, 15))#candidate|2775|(2, 15, 15)|var|bool
bop_2776 = relay.logical_and(call_2731.astype('bool'), relay.reshape(var_2775.astype('bool'), relay.shape_of(call_2731))) # shape=(2, 15, 15)
bop_2779 = relay.logical_and(call_2733.astype('bool'), relay.reshape(var_2775.astype('bool'), relay.shape_of(call_2733))) # shape=(2, 15, 15)
uop_2780 = relay.sinh(uop_2755.astype('float64')) # shape=(11, 14, 8)
uop_2782 = relay.sinh(uop_2757.astype('float64')) # shape=(11, 14, 8)
func_2633_call = mod.get_global_var('func_2633')
func_2638_call = mutated_mod.get_global_var('func_2638')
var_2790 = relay.var("var_2790", dtype = "int64", shape = (1, 480))#candidate|2790|(1, 480)|var|int64
var_2791 = relay.var("var_2791", dtype = "uint64", shape = (1, 252))#candidate|2791|(1, 252)|var|uint64
var_2792 = relay.var("var_2792", dtype = "uint16", shape = (280, 4))#candidate|2792|(280, 4)|var|uint16
call_2789 = relay.TupleGetItem(func_2633_call(relay.reshape(var_2790.astype('int64'), [5, 12, 8]), relay.reshape(var_2791.astype('uint64'), [1, 252]), relay.reshape(var_2792.astype('uint16'), [1120,]), ), 6)
call_2793 = relay.TupleGetItem(func_2638_call(relay.reshape(var_2790.astype('int64'), [5, 12, 8]), relay.reshape(var_2791.astype('uint64'), [1, 252]), relay.reshape(var_2792.astype('uint16'), [1120,]), ), 6)
bop_2796 = relay.minimum(uop_2765.astype('uint64'), relay.reshape(call_2718.astype('uint64'), relay.shape_of(uop_2765))) # shape=(11, 14, 8)
bop_2799 = relay.minimum(uop_2767.astype('uint64'), relay.reshape(call_2719.astype('uint64'), relay.shape_of(uop_2767))) # shape=(11, 14, 8)
output = relay.Tuple([uop_2720,const_2732,call_2745,call_2760,bop_2776,uop_2780,call_2789,var_2790,var_2791,var_2792,bop_2796,])
output2 = relay.Tuple([uop_2722,const_2732,call_2746,call_2761,bop_2779,uop_2782,call_2793,var_2790,var_2791,var_2792,bop_2799,])
func_2802 = relay.Function([var_2775,var_2790,var_2791,var_2792,], output)
mod['func_2802'] = func_2802
mod = relay.transform.InferType()(mod)
var_2803 = relay.var("var_2803", dtype = "bool", shape = (2, 15, 15))#candidate|2803|(2, 15, 15)|var|bool
var_2804 = relay.var("var_2804", dtype = "int64", shape = (1, 480))#candidate|2804|(1, 480)|var|int64
var_2805 = relay.var("var_2805", dtype = "uint64", shape = (1, 252))#candidate|2805|(1, 252)|var|uint64
var_2806 = relay.var("var_2806", dtype = "uint16", shape = (280, 4))#candidate|2806|(280, 4)|var|uint16
output = func_2802(var_2803,var_2804,var_2805,var_2806,)
func_2807 = relay.Function([var_2803,var_2804,var_2805,var_2806,], output)
mutated_mod['func_2807'] = func_2807
mutated_mod = relay.transform.InferType()(mutated_mod)
func_960_call = mod.get_global_var('func_960')
func_962_call = mutated_mod.get_global_var('func_962')
call_2827 = relay.TupleGetItem(func_960_call(), 0)
call_2828 = relay.TupleGetItem(func_962_call(), 0)
const_2832 = relay.const([[[4.436984,7.333337,6.680560,-5.119336,7.126872,-9.992935,-9.307846,-3.170323,-0.626903,1.786091,2.803174,-5.059899,-4.353125],[9.993485,-4.466000,3.497420,1.297251,-8.424497,2.185407,-4.553035,-3.236560,2.251914,-1.344834,2.613079,0.622014,6.209275],[3.588145,3.910473,-9.102125,3.319328,6.549705,8.022362,5.523610,3.411880,-2.310301,9.783732,-4.454300,4.251207,4.111005]],[[-8.114674,6.987865,7.382693,1.144135,-1.328216,1.447700,-1.624975,-9.420974,1.258938,-2.283773,3.749127,-4.471802,3.719442],[2.270129,6.245901,0.769449,8.928561,-5.792159,5.088816,-4.632936,7.306157,4.530225,-5.482018,4.282758,1.479738,9.770913],[-5.103000,-5.582666,-5.236526,-0.172704,-6.859947,0.014009,-6.705098,-3.226881,5.315997,-6.225417,-7.817780,5.425306,2.205936]]], dtype = "float64")#candidate|2832|(2, 3, 13)|const|float64
bop_2833 = relay.less(call_2827.astype('bool'), const_2832.astype('bool')) # shape=(2, 3, 13)
bop_2836 = relay.less(call_2828.astype('bool'), const_2832.astype('bool')) # shape=(2, 3, 13)
var_2839 = relay.var("var_2839", dtype = "float64", shape = (2, 3, 12))#candidate|2839|(2, 3, 12)|var|float64
bop_2840 = relay.multiply(call_2827.astype('float32'), var_2839.astype('float32')) # shape=(2, 3, 12)
bop_2843 = relay.multiply(call_2828.astype('float32'), var_2839.astype('float32')) # shape=(2, 3, 12)
func_1724_call = mod.get_global_var('func_1724')
func_1725_call = mutated_mod.get_global_var('func_1725')
call_2850 = relay.TupleGetItem(func_1724_call(), 2)
call_2851 = relay.TupleGetItem(func_1725_call(), 2)
uop_2855 = relay.atan(call_2827.astype('float64')) # shape=(2, 3, 1)
uop_2857 = relay.atan(call_2828.astype('float64')) # shape=(2, 3, 1)
func_1302_call = mod.get_global_var('func_1302')
func_1304_call = mutated_mod.get_global_var('func_1304')
call_2869 = relay.TupleGetItem(func_1302_call(), 0)
call_2870 = relay.TupleGetItem(func_1304_call(), 0)
func_1440_call = mod.get_global_var('func_1440')
func_1442_call = mutated_mod.get_global_var('func_1442')
var_2876 = relay.var("var_2876", dtype = "uint16", shape = ())#candidate|2876|()|var|uint16
call_2875 = relay.TupleGetItem(func_1440_call(relay.reshape(var_2876.astype('uint16'), [])), 1)
call_2877 = relay.TupleGetItem(func_1442_call(relay.reshape(var_2876.astype('uint16'), [])), 1)
uop_2886 = relay.rsqrt(uop_2855.astype('float32')) # shape=(2, 3, 1)
uop_2888 = relay.rsqrt(uop_2857.astype('float32')) # shape=(2, 3, 1)
output = relay.Tuple([bop_2833,bop_2840,call_2850,call_2869,call_2875,var_2876,uop_2886,])
output2 = relay.Tuple([bop_2836,bop_2843,call_2851,call_2870,call_2877,var_2876,uop_2888,])
func_2892 = relay.Function([var_2839,var_2876,], output)
mod['func_2892'] = func_2892
mod = relay.transform.InferType()(mod)
var_2893 = relay.var("var_2893", dtype = "float64", shape = (2, 3, 12))#candidate|2893|(2, 3, 12)|var|float64
var_2894 = relay.var("var_2894", dtype = "uint16", shape = ())#candidate|2894|()|var|uint16
output = func_2892(var_2893,var_2894,)
func_2895 = relay.Function([var_2893,var_2894,], output)
mutated_mod['func_2895'] = func_2895
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2917 = relay.var("var_2917", dtype = "float32", shape = (10, 8, 9))#candidate|2917|(10, 8, 9)|var|float32
uop_2918 = relay.sinh(var_2917.astype('float32')) # shape=(10, 8, 9)
func_960_call = mod.get_global_var('func_960')
func_962_call = mutated_mod.get_global_var('func_962')
call_2940 = relay.TupleGetItem(func_960_call(), 0)
call_2941 = relay.TupleGetItem(func_962_call(), 0)
func_1965_call = mod.get_global_var('func_1965')
func_1966_call = mutated_mod.get_global_var('func_1966')
call_2942 = relay.TupleGetItem(func_1965_call(), 1)
call_2943 = relay.TupleGetItem(func_1966_call(), 1)
uop_2946 = relay.sin(uop_2918.astype('float64')) # shape=(10, 8, 9)
output = relay.Tuple([call_2940,call_2942,uop_2946,])
output2 = relay.Tuple([call_2941,call_2943,uop_2946,])
func_2952 = relay.Function([var_2917,], output)
mod['func_2952'] = func_2952
mod = relay.transform.InferType()(mod)
mutated_mod['func_2952'] = func_2952
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2953 = relay.var("var_2953", dtype = "float32", shape = (10, 8, 9))#candidate|2953|(10, 8, 9)|var|float32
func_2952_call = mutated_mod.get_global_var('func_2952')
call_2954 = func_2952_call(var_2953)
output = call_2954
func_2955 = relay.Function([var_2953], output)
mutated_mod['func_2955'] = func_2955
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2516_call = mod.get_global_var('func_2516')
func_2518_call = mutated_mod.get_global_var('func_2518')
call_2968 = relay.TupleGetItem(func_2516_call(), 3)
call_2969 = relay.TupleGetItem(func_2518_call(), 3)
func_1107_call = mod.get_global_var('func_1107')
func_1110_call = mutated_mod.get_global_var('func_1110')
const_2976 = relay.const([[2,1,10,7,-8,7,-7,-9,-6,-5,-1,6,-2,-10,8,-5,6,4,-3,-3,9,-3,5,-3,-8,5,5,-1,4,8,-9,-2,10,10,-9,6,-3,6,1,-6,10,-8,7,-1,-3,2,-1,7,-2,-5,-10,-1,-10,-10,8,9,9,2,7,8,-4,3,7,-7,7,-2,-4,9,-9,4,4,7,1,1,7,-7,10,-6,-2,-7,-4,-5,1,-2,-10,2,-10,-9,-2,-6,-10,8,6,8,-7,-4,-6,-1,2,1,-8,8,-4,8,7,-3,-10,8,6,-2,3,-6,-7,-7,-10,3,-1,-7,-9,-1,8,3,6,4,7,7,-1,8,1,9,4,-9,-4,-2,-1,9,-4,9,-2,-3,6,1,-4,7,6,7,7,-7,-4,4,-1,-5,3,-6,-7,-8,-1,-10,7,2,-1,-3,9,-9,-10,-8,-6,-5,-9,8,2,-6,-2,-9,4,-2,2,-5,-7,4,9,-8,7,8,4,9,-1,-8,3,-1,9,-6,-1,4,7,-5,9,5,-7,-1,6,-7,-5,1,-4,-9,-8,-6,5,-6,9,3,5,6,-9,-2,-7,4,-6,1,9,-3,-4,3,10,-6,-3,6,6,-9,-9,4,10,7,4,3,8,8,4,3,-3,2,-9,3,2,-2,10,6,-3,5,-3,-1]], dtype = "uint64")#candidate|2976|(1, 252)|const|uint64
var_2977 = relay.var("var_2977", dtype = "float64", shape = (1232,))#candidate|2977|(1232,)|var|float64
call_2975 = relay.TupleGetItem(func_1107_call(relay.reshape(const_2976.astype('uint64'), [252,]), relay.reshape(var_2977.astype('float64'), [1232,]), ), 4)
call_2978 = relay.TupleGetItem(func_1110_call(relay.reshape(const_2976.astype('uint64'), [252,]), relay.reshape(var_2977.astype('float64'), [1232,]), ), 4)
output = relay.Tuple([call_2968,call_2975,const_2976,var_2977,])
output2 = relay.Tuple([call_2969,call_2978,const_2976,var_2977,])
func_2984 = relay.Function([var_2977,], output)
mod['func_2984'] = func_2984
mod = relay.transform.InferType()(mod)
var_2985 = relay.var("var_2985", dtype = "float64", shape = (1232,))#candidate|2985|(1232,)|var|float64
output = func_2984(var_2985)
func_2986 = relay.Function([var_2985], output)
mutated_mod['func_2986'] = func_2986
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1302_call = mod.get_global_var('func_1302')
func_1304_call = mutated_mod.get_global_var('func_1304')
call_3089 = relay.TupleGetItem(func_1302_call(), 1)
call_3090 = relay.TupleGetItem(func_1304_call(), 1)
func_608_call = mod.get_global_var('func_608')
func_610_call = mutated_mod.get_global_var('func_610')
call_3104 = relay.TupleGetItem(func_608_call(), 0)
call_3105 = relay.TupleGetItem(func_610_call(), 0)
output = relay.Tuple([call_3089,call_3104,])
output2 = relay.Tuple([call_3090,call_3105,])
func_3107 = relay.Function([], output)
mod['func_3107'] = func_3107
mod = relay.transform.InferType()(mod)
mutated_mod['func_3107'] = func_3107
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3107_call = mutated_mod.get_global_var('func_3107')
call_3108 = func_3107_call()
output = call_3108
func_3109 = relay.Function([], output)
mutated_mod['func_3109'] = func_3109
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1965_call = mod.get_global_var('func_1965')
func_1966_call = mutated_mod.get_global_var('func_1966')
call_3123 = relay.TupleGetItem(func_1965_call(), 0)
call_3124 = relay.TupleGetItem(func_1966_call(), 0)
output = call_3123
output2 = call_3124
func_3127 = relay.Function([], output)
mod['func_3127'] = func_3127
mod = relay.transform.InferType()(mod)
output = func_3127()
func_3128 = relay.Function([], output)
mutated_mod['func_3128'] = func_3128
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2673_call = mod.get_global_var('func_2673')
func_2674_call = mutated_mod.get_global_var('func_2674')
call_3153 = relay.TupleGetItem(func_2673_call(), 0)
call_3154 = relay.TupleGetItem(func_2674_call(), 0)
func_2952_call = mod.get_global_var('func_2952')
func_2955_call = mutated_mod.get_global_var('func_2955')
var_3156 = relay.var("var_3156", dtype = "float32", shape = (4, 180))#candidate|3156|(4, 180)|var|float32
call_3155 = relay.TupleGetItem(func_2952_call(relay.reshape(var_3156.astype('float32'), [10, 8, 9])), 0)
call_3157 = relay.TupleGetItem(func_2955_call(relay.reshape(var_3156.astype('float32'), [10, 8, 9])), 0)
uop_3158 = relay.sin(call_3155.astype('float32')) # shape=(2, 3, 1)
uop_3160 = relay.sin(call_3157.astype('float32')) # shape=(2, 3, 1)
uop_3171 = relay.acosh(var_3156.astype('float32')) # shape=(4, 180)
func_1763_call = mod.get_global_var('func_1763')
func_1766_call = mutated_mod.get_global_var('func_1766')
const_3205 = relay.const([-2.851001,7.532977,-5.101317,-7.353161,1.575666,-5.085655,3.826118,8.756159,-2.653341,-6.056370,6.986355,-6.578839,1.747735,9.127781,9.942154,-9.660112,9.129058,8.454514,8.121653,9.760322,6.124635,2.741522,-2.114654,-5.136710,6.652125,3.270688,-1.042421,-1.411565,5.927022,-0.436723,5.948193,4.213863,-5.058464,-5.300154,-5.605628,-3.178620,-5.397975,-1.634525,-4.817242,4.613590,8.654863,-3.524265,-9.419666,1.266009,-8.433543,-4.622671,-8.660848,7.510170,-8.330028,-2.404718,1.281628,1.995079,8.776117,-7.301786,-2.202701,6.017717,-8.307884,2.940652,-6.160134,-4.199794,-4.853787,-2.432173,-0.508606,8.673399,2.763714,6.043034,-2.672498,-8.839022,-5.363425,6.704042,-2.133822,-0.441595,0.007110,-9.332139,-5.555476,-2.252074,5.431978,-4.051769,-6.975370,8.869568,6.839235,-5.912779,7.795246,2.260167,1.026948,-4.985313,6.329144,-3.812948,0.573514,-6.630634,-6.683757,-2.796176,6.021106,0.816048,8.778820,-8.299691,-1.989635,-9.041244,9.011570,9.206218,9.425326,5.895944,2.097274,5.555756,-0.610188,-3.426254,-9.458055,-9.370782,9.311309,-1.496106,-3.367226,-8.541570,8.406368,-1.009286,-7.795206,-5.468010,-6.767753,5.299542,4.116035,-8.986138,-5.940787,-9.013337,4.846412,5.726123,7.913861,0.331811,-3.138698,-3.197740,3.379065,-3.482955,-6.674927,5.174810,-8.065752,-5.802597,0.563516,9.110283,-1.686032,-8.376669,1.872035,-7.448401,6.474715,-6.719820,6.928192,-2.080421,-6.601705,7.007102,5.615165,1.153307,0.966568,4.251337,-5.197213,-5.665464,1.501121,-2.269812,-4.775578,7.291820,9.573377,5.044121,-5.889698,8.684203,7.598708,9.828714,4.337589,-4.255307,7.039655,4.457368,2.216607,-4.873237,-4.501730,3.436208,2.221519,3.917272,-1.298876,-6.255545,-6.490085,3.819571,-9.078556,-3.163778,4.891373,-6.589448,-2.312726,-6.165192,3.029519,-9.016614,-0.781241,1.510416,-5.076229,-1.019032,8.500621,6.688807,-6.348409,0.491608,-3.777503,-1.969655,2.499302,-3.235097,-9.546711,8.398071,3.033410,6.547006,7.773143,8.934871,8.516503,-3.069813,-8.096245,-8.741026,4.762345,8.208172,8.443101,0.196837,-1.443535,5.453076,5.241557,0.799043,-0.385986,-6.518049,3.712856,-4.263081,4.898531,7.963436,-8.638259,-3.682021,-8.068346,2.388019,4.099109,-0.374867,-9.337304,-9.009049,-2.545547,-2.140750,-6.487112,-6.310762,1.129589,9.529654,0.594028,-3.557041,-4.413336,2.944919,1.341515,0.967470,-0.079314,-3.256675,7.804128,-1.769995,-6.584632,-0.998377,9.259293,-1.296053,9.504831,7.579318,8.311088,5.294766,-5.040239,-1.294020,8.515163,-8.239314,7.953016,6.609538,8.535093,-2.991545,-0.757165,-1.623814,9.422874,-1.076263,-3.571753,5.551242,-6.856389,-3.944239,-6.331038,-6.089220,-2.473671,4.695567,3.695042,-0.286080,-2.120366,2.279621,3.579296,-6.242429,-9.957362,-1.127837,-0.889822,-7.298650,-5.973900,1.403804,0.537660,-4.045478,-2.105204,1.178574,-8.967113,-0.706077,-6.919615,-6.085579,2.034993,-9.241452,6.025413,8.493526,3.403847,-9.773003,-5.930603,-0.855847,4.059032,0.041307,-7.867958,-8.515701,-3.926515,0.384792,-8.980058,-2.362906,-2.131355,7.967578,9.537296,6.131081,0.220952,-5.490668,3.276751,6.771343,-0.336462,-1.558207,-4.279197,0.649728,7.199534,5.977331,-8.144760,2.178698,1.027026,2.994083,8.698769,2.896290,-3.593344,-1.836006,-8.129818,4.773781,-1.940726,5.052599,-0.279316,0.598547,6.814071,6.089453,4.237612,-5.230082,6.972953,6.876590,-2.913092,8.675432,9.424503,-4.208586,-9.499286,-0.273080,8.481206,3.658419,-1.161083,8.676124,0.255287,-0.043557,9.969706,0.330819,-5.752948,-3.599502,0.386166,2.538054,3.422508,-1.947978,7.402340,9.614038,-1.363181,-1.131164,3.906128,-9.312999,-2.255674,0.854365,9.121986,1.510482,-0.333887,-5.914909,1.172963,-0.786436,6.049689,-9.566215,2.956423,2.520115,-2.618057,-3.881789,6.871722,3.433918,2.152432,-6.826891,2.413245,-3.301611,5.868700,-1.579997,1.862918,3.579296,1.015925,0.871167,5.222562,3.930405,6.439560,-9.810448,-9.204835,-1.077161,-1.925022,5.640016,-9.902047,8.179517,-6.945302,0.351579,-1.236893,1.012506,-6.821868,-9.423493,8.778355,-9.869551,-6.467753,-7.896514,-6.491290,-3.652837,3.458593,-8.322428,-1.590277,5.042098,9.836684,-9.176231,8.667187,-6.958600,-4.160079,-1.958278,-4.879292,-6.091349,1.756221,2.956858,-1.415469,-5.352956,4.633852,9.795505,2.650583,4.111195,4.773542,-3.219426,7.149554,0.799211,-5.657105,8.720817,-6.272273,8.620348,-7.351300,7.489585,-8.691889,-4.410902,-1.087016,0.780628,-4.567024,5.518814,-2.186094,7.617317,-6.778707,-6.328464,-1.611865,5.176416,1.042571,-8.374562,0.747213,-3.530943,9.593158,-0.706134,0.395123,2.237698,-2.512618,9.172599,5.881932,-6.441506,4.588779,-4.275547,-8.322876,-4.667426,-1.386330,-6.321884,-1.823865,9.460414,6.988784,-6.371028,-8.868785,7.664521,-5.196844,3.968315,5.028055,4.932081,-9.074196,-8.595328,1.490230,3.784101,8.206242,5.672192,-6.952143,6.348341,-0.700408,-6.672854,-8.895901,9.195710,2.029383,-3.153323,-2.320673,9.162295,1.070836,-4.416819,9.689283,-4.475993,1.061641,-7.040926,-8.645792,1.413725,1.645289,1.098586,2.455685,-1.051372,-5.628690,1.419888,-5.091097,6.902313,-8.222887,-5.467331,0.692415,-4.624901,2.572640,4.500863,7.341126,-9.746566,-1.608068,-7.642516,0.889161,-2.312915,5.879129,-8.832091,1.938889,8.074297,8.668071,1.845211,-7.524841,2.320452,-4.681912,2.026810,-5.191725,1.510146,-2.730629,-1.347383,-8.723452,0.127840,9.961353,-2.557973,1.861172,-9.862345,1.493749,-6.780382,-5.232179,3.944031,-3.886454,-2.652870,4.504357,6.732355,1.940981,7.076860,1.544480,2.451106,-9.789844,9.021709,1.842505,4.694754,1.860889,-1.471553,1.392274,-2.453391,-7.022173,-9.600382,-6.776223,1.798652,-0.843152,-5.360402,4.764855,-5.722202,0.308451,-0.978092,6.294059,2.677904,7.014334,-2.146094,-6.896354,-0.676879,5.595520,-4.444100,-4.896414,2.948330,-8.619760,-5.549365,5.876248,0.781746,-5.508450,9.603790,6.936782,-5.692666,-6.714624,-6.249288,-4.815808,-5.490403,5.426744,6.398720,-0.574870,-5.617925,-0.877452,1.715229,4.860447,-4.236036,-5.915327,-6.626119,5.255638,-8.091085,0.326349,-3.831731,3.655638,-7.401627,8.498877,-5.440935,-3.040594,-8.293675,-5.010725,8.834125,-0.388933,1.429509,4.908406,5.589628,7.895341,5.577189,-9.388404,-5.972708,-4.460773,-7.315441,-3.548877,8.234034,-8.777703,-7.591218,1.945595,-8.631965], dtype = "float64")#candidate|3205|(640,)|const|float64
call_3204 = relay.TupleGetItem(func_1763_call(relay.reshape(const_3205.astype('float64'), [16, 5, 8])), 0)
call_3206 = relay.TupleGetItem(func_1766_call(relay.reshape(const_3205.astype('float64'), [16, 5, 8])), 0)
bop_3209 = relay.logical_or(uop_3158.astype('bool'), relay.reshape(call_3155.astype('bool'), relay.shape_of(uop_3158))) # shape=(2, 3, 1)
bop_3212 = relay.logical_or(uop_3160.astype('bool'), relay.reshape(call_3157.astype('bool'), relay.shape_of(uop_3160))) # shape=(2, 3, 1)
output = relay.Tuple([call_3153,uop_3171,call_3204,const_3205,bop_3209,])
output2 = relay.Tuple([call_3154,uop_3171,call_3206,const_3205,bop_3212,])
func_3240 = relay.Function([var_3156,], output)
mod['func_3240'] = func_3240
mod = relay.transform.InferType()(mod)
mutated_mod['func_3240'] = func_3240
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3241 = relay.var("var_3241", dtype = "float32", shape = (4, 180))#candidate|3241|(4, 180)|var|float32
func_3240_call = mutated_mod.get_global_var('func_3240')
call_3242 = func_3240_call(var_3241)
output = call_3242
func_3243 = relay.Function([var_3241], output)
mutated_mod['func_3243'] = func_3243
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2544_call = mod.get_global_var('func_2544')
func_2546_call = mutated_mod.get_global_var('func_2546')
call_3248 = relay.TupleGetItem(func_2544_call(), 0)
call_3249 = relay.TupleGetItem(func_2546_call(), 0)
func_2984_call = mod.get_global_var('func_2984')
func_2986_call = mutated_mod.get_global_var('func_2986')
var_3261 = relay.var("var_3261", dtype = "float64", shape = (1232,))#candidate|3261|(1232,)|var|float64
call_3260 = relay.TupleGetItem(func_2984_call(relay.reshape(var_3261.astype('float64'), [1232,])), 2)
call_3262 = relay.TupleGetItem(func_2986_call(relay.reshape(var_3261.astype('float64'), [1232,])), 2)
func_960_call = mod.get_global_var('func_960')
func_962_call = mutated_mod.get_global_var('func_962')
call_3263 = relay.TupleGetItem(func_960_call(), 0)
call_3264 = relay.TupleGetItem(func_962_call(), 0)
const_3267 = relay.const([[2,-6,4,-3,2,9,-8,5,1,-10,9,-10,-10,-4,1,-4,5,-5,-1,7,-10,-3,5,-10,3,7,3,8,8,-2,-3,3,-8,8,5,-1,4,-3,-1,-7,-4,8,-6,5,-10,2,-3,3,3,1,7,-3,5,3,-9,-2,-7,-2,-7,-6,4,-2,2,8,-7,3,2,-8,-10,-5,-3,1,7,2,2,3,-7,3,-10,-7,2,4,4,1,5,4,-2,8,10,-3,10,-8,-1,-6,-2,10,3,-7,8,-2,3,8,10,-5,8,5,-4,-2,-4,5,-3,7,1,-2,2,-1,-7,2,-7,-2,-7,-2,9,-5,4,6,-7,3,9,-8,-7,-5,1,6,6,-4,2,-3,10,4,10,-3,-5,6,2,-4,-4,-5,-8,-3,-8,7,-3,-3,-10,10,6,-8,10,4,9,-10,7,-10,-8,-9,-1,6,-7,-8,-5,5,-10,4,-9,3,-6,-1,-10,-8,-5,5,-1,10,2,-3,4,10,-2,-7,3,-9,1,-2,2,-9,6,2,5,-7,10,3,9,2,-8,-4,-7,1,-4,10,4,-2,-5,10,-6,6,9,2,3,-1,2,-3,10,-8,-9,-8,-10,-5,-5,-7,-4,-7,-2,-10,2,7,9,-1,-4,-1,1,-5,-2,-8,-7,-7,5,1,2,6,3,6],[-3,-10,9,-1,-1,-1,-9,1,1,-7,2,8,9,8,5,-5,2,-9,-7,1,-9,2,-9,-5,8,9,-2,-6,10,5,7,-6,-7,1,-5,1,-3,3,-5,6,-2,5,-3,5,4,-9,-3,-9,-9,-2,3,8,8,1,10,9,4,6,-5,-9,2,-2,-2,-5,3,5,1,-3,-3,-2,-2,4,5,1,8,10,9,-7,3,4,-9,2,-10,-1,-9,-5,4,-5,7,10,8,-9,4,-8,8,-4,10,-9,3,3,-4,1,8,-8,1,-2,10,6,7,-4,7,-4,-6,-7,-6,10,-9,-6,6,1,2,6,5,9,-7,9,-10,1,9,-6,-8,-4,7,3,-6,1,-10,-1,1,8,-2,2,-1,2,10,-6,-4,5,-10,3,3,-3,2,-9,-5,-1,-4,-3,-3,-9,-2,-1,-5,8,-5,3,-6,2,-2,3,5,-8,-4,-6,-7,1,-9,-8,9,10,-8,3,-9,3,5,3,-9,-1,-4,-1,-1,2,7,6,7,-1,1,8,8,-3,9,-4,-9,-1,-1,3,7,4,7,-9,8,-9,1,-8,3,3,-9,10,10,-10,4,-5,-1,4,-10,4,10,-6,-3,3,8,-7,2,7,-7,-5,2,-1,-2,3,-7,-10,10,-1,2,8,9,-9,1,3,10,-8],[-9,-7,5,2,7,-10,-10,10,4,-2,-1,3,4,9,-3,8,9,10,-5,5,-4,9,-5,-6,8,1,-8,3,-10,9,1,-5,3,6,10,2,-6,8,1,-10,3,-8,6,4,-4,-7,-10,-7,8,3,-5,-1,-7,4,-4,-6,-6,1,-6,5,-8,6,5,-5,9,2,-2,-6,-4,8,5,-9,10,10,-5,-7,7,2,-9,8,4,3,-3,-6,9,8,-10,2,5,6,-9,2,6,-10,3,-4,-8,-5,-8,-9,-7,-1,-2,-6,7,6,5,-3,-5,10,1,-3,1,-1,10,-5,6,3,1,6,3,5,1,-1,-1,2,-4,-2,-4,-5,-2,1,-8,-6,4,-6,-4,-5,9,3,8,5,-2,-1,9,-1,8,-8,6,5,6,7,4,-6,1,-4,-5,-4,-5,5,1,-6,-10,5,-8,6,-4,3,8,-1,-7,9,-2,-10,6,-3,-1,-7,-3,7,-5,-3,-7,-4,-6,-5,10,8,6,10,-1,-10,2,-3,8,-4,4,-1,-6,5,2,8,3,3,-3,-1,8,9,7,-2,-4,9,6,7,4,5,-4,-7,8,-4,5,-5,5,10,8,6,-8,7,4,5,10,4,-4,8,-3,5,6,-10,4,2,5,3,4,9,-6,7,-6,-7,-4,-4,-5,-6],[7,-3,-7,4,-6,7,-6,9,-1,-7,9,-7,7,9,-8,-7,10,-9,-9,-1,9,7,2,-7,-4,10,-8,-6,8,-1,2,-3,-7,1,5,-1,10,2,-5,7,-5,3,-5,8,-6,-10,-6,1,7,-1,6,9,-9,-9,1,-4,-4,8,7,3,-7,-4,-5,-6,6,5,1,-9,-4,-5,-6,-1,-5,2,-7,7,-5,4,-5,4,-2,-5,-2,1,5,-1,4,-5,-1,3,9,9,-1,8,7,-9,-9,-10,-1,9,9,-10,1,4,-10,9,8,-7,-5,7,7,1,-2,-8,-3,10,-6,7,-4,1,-9,-7,-2,-8,-1,9,10,-5,2,-7,10,-9,6,8,-6,-5,-1,3,-9,8,-7,8,-8,2,-8,-3,4,7,-7,-1,-5,-1,1,10,7,9,-7,-1,-2,5,2,8,-9,6,-1,-10,-3,5,-6,-3,-4,-7,9,-8,-3,-1,-10,-10,6,-6,5,5,8,4,-4,-9,9,-1,-5,1,9,-2,-1,-9,-10,-3,-4,3,-6,-8,-1,-1,2,-3,9,7,-6,-1,3,3,7,-6,-4,-3,-3,-3,5,-9,3,5,5,-4,-1,7,4,-5,6,10,-2,10,-1,2,-4,4,-2,-3,-1,8,-1,5,-5,-4,4,10,-6,-1,-5,6,5,-9,1,6],[9,5,10,-3,2,9,3,4,-2,-10,-10,-6,-8,-6,7,4,-9,-3,-1,-6,-8,-1,-6,2,-1,-5,-1,-8,6,-2,7,8,-5,6,9,-8,-9,-8,3,-1,6,-5,-6,8,8,-6,5,2,-5,5,10,-3,-2,4,-2,-10,-2,7,-10,10,6,5,-10,-3,-5,2,-4,6,5,1,-4,8,-6,4,10,3,1,-9,-5,7,5,-9,4,4,5,7,-4,5,-9,-5,-4,9,4,-8,2,-1,7,-5,5,-10,-5,-10,-3,-1,8,3,4,-9,10,7,5,3,10,-2,-9,7,-1,-5,6,7,1,5,-4,4,-2,-9,3,-10,10,-9,-4,3,5,-10,-3,4,8,1,-4,7,-8,-2,8,3,3,7,10,3,-7,8,-9,-5,-10,3,1,-9,-8,-9,4,-4,-6,6,-10,-3,3,6,2,3,8,-7,5,8,-8,8,9,-8,-5,-2,5,-2,7,-2,-1,-2,-8,6,4,7,-10,-1,-8,-7,7,-10,7,3,-1,-4,2,1,-4,5,2,-7,6,-5,-10,9,-2,-10,-2,2,9,-8,-1,-1,8,2,-8,4,8,10,2,3,-8,-2,7,-6,9,7,4,4,6,4,4,7,9,-7,-7,-4,3,-7,-9,9,10,-7,-4,8,6,5,2,-9],[-9,4,7,3,4,-2,-5,-1,7,-9,1,-2,-1,-5,8,6,10,-5,7,-7,-10,-6,-10,-1,-6,-7,-10,-2,-5,-4,10,-10,9,7,3,-7,-5,-7,-9,-1,9,-2,8,-9,-2,3,2,-4,9,7,7,5,6,-6,-10,-1,-4,9,-10,4,3,8,3,6,-5,-5,6,2,-2,10,7,5,8,-5,4,10,7,3,-10,-5,2,7,10,4,10,-7,7,8,6,2,3,7,2,3,9,-8,5,-10,7,-10,8,-3,7,-10,7,3,4,9,2,-9,-9,3,-10,-1,-9,-3,-6,1,10,-8,-3,-6,-3,-4,-6,-5,8,10,-10,-5,10,5,-6,1,10,-2,10,-10,4,9,7,-6,-3,2,-5,-2,7,-5,8,9,-5,10,1,-2,6,-5,-5,-5,-5,-2,4,-9,5,-3,10,-10,-5,2,-2,10,-6,-10,-6,-9,-2,5,-5,8,-6,3,-5,3,-5,5,-1,-5,10,8,-10,10,8,-9,-8,4,-8,-2,-2,-2,-1,-4,1,-9,-3,-10,-4,5,4,4,1,-9,-5,-1,-7,-3,9,9,5,3,-7,-10,-3,-10,9,2,1,10,-2,2,3,6,-1,3,6,-5,-1,1,-2,-3,-6,2,6,-5,2,-8,5,6,-2,3,5,9,4,1],[3,-10,1,-10,3,-5,-5,9,-8,7,6,-8,-9,-8,-8,-1,-5,2,1,10,7,1,10,-3,9,-10,9,7,-4,-1,3,3,-10,-1,7,7,9,-8,-1,9,1,4,-7,8,-5,-2,-10,6,10,-3,1,8,9,10,9,2,1,9,-7,7,-7,-10,-4,9,6,-8,1,8,4,-1,-1,2,-9,8,-2,-5,6,8,-2,3,-6,-4,8,6,-1,-6,10,-2,3,-2,-7,-5,-2,10,-9,-1,-5,-1,-6,7,-6,8,5,4,2,-2,-4,-1,-10,-2,5,4,-8,-4,-4,2,6,-5,-3,-10,4,5,10,8,-6,-9,-6,2,-7,-10,7,-10,-3,-7,-1,-3,-10,-7,-4,-10,-5,-5,1,-5,-4,-1,7,6,-4,8,10,4,-2,8,-4,-8,7,-10,-3,-7,7,7,-9,6,6,1,-7,-5,6,7,-4,-10,10,-1,2,7,-8,-5,-7,-10,-5,10,6,3,1,-3,-4,-7,-1,-7,-6,4,1,9,-2,-3,-2,1,8,-1,3,-5,-6,-3,-9,-2,9,7,7,1,6,6,-7,-7,10,-6,-1,2,-3,6,9,5,6,-9,-9,-2,-4,-5,5,10,10,-10,6,10,-9,1,6,6,-9,5,-7,7,5,-4,3,-8,1,6,2,-7,2,-8],[6,-10,-1,5,2,-9,1,9,-9,-7,-7,-8,-8,-7,-4,1,-1,5,6,9,-1,4,6,-7,10,-5,-8,-3,9,9,7,3,2,9,9,3,8,5,-1,-9,8,-8,-7,3,5,9,-5,-9,2,3,5,5,-7,7,1,-1,-10,-5,3,10,3,7,2,5,1,-7,-7,-2,-3,2,-5,-2,3,-9,-9,-2,8,10,-5,-6,-4,7,-7,6,7,3,3,6,-7,2,-6,8,-6,-6,3,1,8,9,-4,5,-4,-5,6,-3,-10,8,-1,-2,5,10,-3,-7,7,-4,2,-4,10,1,5,-10,9,1,-6,-7,-4,-1,5,5,6,5,-1,-4,10,-10,1,10,-9,2,-5,-6,-3,3,5,-2,-7,10,-9,2,4,-6,1,-7,-6,-6,7,9,9,9,-10,-4,9,-9,-10,10,1,1,10,2,6,-9,10,-2,-10,2,4,-10,-1,3,-10,-7,9,-4,-7,-6,-4,5,-3,-2,2,4,9,-2,3,-4,-8,-5,-1,5,5,1,6,-7,7,-1,-3,-4,9,7,-1,6,-3,10,9,-4,-9,-8,-2,-2,-4,7,-8,-2,-7,10,1,1,4,-10,7,9,-8,10,2,1,7,-5,-9,3,-5,7,-8,10,10,-6,5,-4,4,4,-6,-2,-3,9]], dtype = "uint64")#candidate|3267|(8, 252)|const|uint64
bop_3268 = relay.bitwise_xor(call_3260.astype('uint64'), const_3267.astype('uint64')) # shape=(8, 252)
bop_3271 = relay.bitwise_xor(call_3262.astype('uint64'), const_3267.astype('uint64')) # shape=(8, 252)
uop_3274 = relay.tan(const_3267.astype('float32')) # shape=(8, 252)
output = relay.Tuple([call_3248,var_3261,call_3263,bop_3268,uop_3274,])
output2 = relay.Tuple([call_3249,var_3261,call_3264,bop_3271,uop_3274,])
func_3277 = relay.Function([var_3261,], output)
mod['func_3277'] = func_3277
mod = relay.transform.InferType()(mod)
mutated_mod['func_3277'] = func_3277
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3278 = relay.var("var_3278", dtype = "float64", shape = (1232,))#candidate|3278|(1232,)|var|float64
func_3277_call = mutated_mod.get_global_var('func_3277')
call_3279 = func_3277_call(var_3278)
output = call_3279
func_3280 = relay.Function([var_3278], output)
mutated_mod['func_3280'] = func_3280
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1731_call = mod.get_global_var('func_1731')
func_1733_call = mutated_mod.get_global_var('func_1733')
call_3331 = func_1731_call()
call_3332 = func_1731_call()
output = relay.Tuple([call_3331,])
output2 = relay.Tuple([call_3332,])
func_3334 = relay.Function([], output)
mod['func_3334'] = func_3334
mod = relay.transform.InferType()(mod)
output = func_3334()
func_3335 = relay.Function([], output)
mutated_mod['func_3335'] = func_3335
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3363 = relay.var("var_3363", dtype = "float32", shape = (15, 8, 8))#candidate|3363|(15, 8, 8)|var|float32
uop_3364 = relay.cos(var_3363.astype('float32')) # shape=(15, 8, 8)
var_3366 = relay.var("var_3366", dtype = "float32", shape = (15, 8, 8))#candidate|3366|(15, 8, 8)|var|float32
bop_3367 = relay.logical_xor(uop_3364.astype('uint64'), relay.reshape(var_3366.astype('uint64'), relay.shape_of(uop_3364))) # shape=(15, 8, 8)
func_2490_call = mod.get_global_var('func_2490')
func_2491_call = mutated_mod.get_global_var('func_2491')
call_3379 = func_2490_call()
call_3380 = func_2490_call()
func_2698_call = mod.get_global_var('func_2698')
func_2700_call = mutated_mod.get_global_var('func_2700')
call_3384 = relay.TupleGetItem(func_2698_call(), 0)
call_3385 = relay.TupleGetItem(func_2700_call(), 0)
func_1330_call = mod.get_global_var('func_1330')
func_1332_call = mutated_mod.get_global_var('func_1332')
call_3387 = func_1330_call()
call_3388 = func_1330_call()
uop_3404 = relay.sinh(uop_3364.astype('float64')) # shape=(15, 8, 8)
uop_3408 = relay.atanh(uop_3364.astype('float32')) # shape=(15, 8, 8)
output = relay.Tuple([bop_3367,call_3379,call_3384,call_3387,uop_3404,uop_3408,])
output2 = relay.Tuple([bop_3367,call_3380,call_3385,call_3388,uop_3404,uop_3408,])
func_3411 = relay.Function([var_3363,var_3366,], output)
mod['func_3411'] = func_3411
mod = relay.transform.InferType()(mod)
var_3412 = relay.var("var_3412", dtype = "float32", shape = (15, 8, 8))#candidate|3412|(15, 8, 8)|var|float32
var_3413 = relay.var("var_3413", dtype = "float32", shape = (15, 8, 8))#candidate|3413|(15, 8, 8)|var|float32
output = func_3411(var_3412,var_3413,)
func_3414 = relay.Function([var_3412,var_3413,], output)
mutated_mod['func_3414'] = func_3414
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2289_call = mod.get_global_var('func_2289')
func_2291_call = mutated_mod.get_global_var('func_2291')
call_3418 = func_2289_call()
call_3419 = func_2289_call()
func_1581_call = mod.get_global_var('func_1581')
func_1583_call = mutated_mod.get_global_var('func_1583')
call_3420 = relay.TupleGetItem(func_1581_call(), 0)
call_3421 = relay.TupleGetItem(func_1583_call(), 0)
func_2683_call = mod.get_global_var('func_2683')
func_2684_call = mutated_mod.get_global_var('func_2684')
call_3424 = func_2683_call()
call_3425 = func_2683_call()
bop_3456 = relay.less(call_3420.astype('bool'), relay.reshape(call_3424.astype('bool'), relay.shape_of(call_3420))) # shape=(11, 14, 8)
bop_3459 = relay.less(call_3421.astype('bool'), relay.reshape(call_3425.astype('bool'), relay.shape_of(call_3421))) # shape=(11, 14, 8)
uop_3466 = relay.log10(call_3424.astype('float64')) # shape=(11, 14, 8)
uop_3468 = relay.log10(call_3425.astype('float64')) # shape=(11, 14, 8)
output = relay.Tuple([call_3418,bop_3456,uop_3466,])
output2 = relay.Tuple([call_3419,bop_3459,uop_3468,])
func_3469 = relay.Function([], output)
mod['func_3469'] = func_3469
mod = relay.transform.InferType()(mod)
mutated_mod['func_3469'] = func_3469
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3469_call = mutated_mod.get_global_var('func_3469')
call_3470 = func_3469_call()
output = call_3470
func_3471 = relay.Function([], output)
mutated_mod['func_3471'] = func_3471
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3469_call = mod.get_global_var('func_3469')
func_3471_call = mutated_mod.get_global_var('func_3471')
call_3581 = relay.TupleGetItem(func_3469_call(), 0)
call_3582 = relay.TupleGetItem(func_3471_call(), 0)
func_1560_call = mod.get_global_var('func_1560')
func_1562_call = mutated_mod.get_global_var('func_1562')
call_3583 = relay.TupleGetItem(func_1560_call(), 0)
call_3584 = relay.TupleGetItem(func_1562_call(), 0)
output = relay.Tuple([call_3581,call_3583,])
output2 = relay.Tuple([call_3582,call_3584,])
func_3595 = relay.Function([], output)
mod['func_3595'] = func_3595
mod = relay.transform.InferType()(mod)
output = func_3595()
func_3596 = relay.Function([], output)
mutated_mod['func_3596'] = func_3596
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3127_call = mod.get_global_var('func_3127')
func_3128_call = mutated_mod.get_global_var('func_3128')
call_3611 = func_3127_call()
call_3612 = func_3127_call()
func_1724_call = mod.get_global_var('func_1724')
func_1725_call = mutated_mod.get_global_var('func_1725')
call_3613 = relay.TupleGetItem(func_1724_call(), 2)
call_3614 = relay.TupleGetItem(func_1725_call(), 2)
func_2187_call = mod.get_global_var('func_2187')
func_2191_call = mutated_mod.get_global_var('func_2191')
var_3628 = relay.var("var_3628", dtype = "int32", shape = (1232,))#candidate|3628|(1232,)|var|int32
var_3629 = relay.var("var_3629", dtype = "uint64", shape = ())#candidate|3629|()|var|uint64
call_3627 = relay.TupleGetItem(func_2187_call(relay.reshape(var_3628.astype('int32'), [11, 14, 8]), relay.reshape(var_3629.astype('uint64'), []), ), 1)
call_3630 = relay.TupleGetItem(func_2191_call(relay.reshape(var_3628.astype('int32'), [11, 14, 8]), relay.reshape(var_3629.astype('uint64'), []), ), 1)
func_2698_call = mod.get_global_var('func_2698')
func_2700_call = mutated_mod.get_global_var('func_2700')
call_3638 = relay.TupleGetItem(func_2698_call(), 0)
call_3639 = relay.TupleGetItem(func_2700_call(), 0)
func_2952_call = mod.get_global_var('func_2952')
func_2955_call = mutated_mod.get_global_var('func_2955')
var_3643 = relay.var("var_3643", dtype = "float32", shape = (720,))#candidate|3643|(720,)|var|float32
call_3642 = relay.TupleGetItem(func_2952_call(relay.reshape(var_3643.astype('float32'), [10, 8, 9])), 2)
call_3644 = relay.TupleGetItem(func_2955_call(relay.reshape(var_3643.astype('float32'), [10, 8, 9])), 2)
output = relay.Tuple([call_3611,call_3613,call_3627,var_3628,var_3629,call_3638,call_3642,var_3643,])
output2 = relay.Tuple([call_3612,call_3614,call_3630,var_3628,var_3629,call_3639,call_3644,var_3643,])
func_3648 = relay.Function([var_3628,var_3629,var_3643,], output)
mod['func_3648'] = func_3648
mod = relay.transform.InferType()(mod)
mutated_mod['func_3648'] = func_3648
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3648_call = mutated_mod.get_global_var('func_3648')
var_3650 = relay.var("var_3650", dtype = "int32", shape = (1232,))#candidate|3650|(1232,)|var|int32
var_3651 = relay.var("var_3651", dtype = "uint64", shape = ())#candidate|3651|()|var|uint64
var_3652 = relay.var("var_3652", dtype = "float32", shape = (720,))#candidate|3652|(720,)|var|float32
call_3649 = func_3648_call(var_3650,var_3651,var_3652,)
output = call_3649
func_3653 = relay.Function([var_3650,var_3651,var_3652,], output)
mutated_mod['func_3653'] = func_3653
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3658 = relay.const([[[False,True,False,False,False,True,False,False,False,False,False,True,False,True],[False,True,True,True,False,False,False,False,False,True,True,True,False,False],[False,False,True,False,True,True,False,False,False,True,False,False,True,False],[False,True,True,False,False,False,True,False,True,False,True,True,True,False],[True,False,True,True,False,False,True,True,True,True,True,False,False,False],[False,False,False,False,True,False,False,False,False,False,False,True,False,True],[True,True,False,False,True,True,True,True,True,False,True,False,True,False],[False,False,False,True,False,True,True,True,True,False,True,True,False,False],[True,False,True,False,True,True,False,True,False,True,False,True,True,True]],[[False,False,False,False,False,False,True,False,True,True,False,False,True,True],[False,True,True,True,True,True,True,False,False,True,True,True,False,False],[False,True,True,False,True,True,True,False,False,False,False,True,True,False],[False,False,False,False,True,True,True,False,False,False,True,True,True,False],[False,True,False,False,False,False,True,True,True,False,True,True,False,False],[True,False,False,True,False,False,True,False,False,False,False,False,False,True],[True,True,False,True,False,False,False,False,False,True,True,False,True,True],[True,True,True,False,True,True,True,False,False,False,False,False,False,False],[False,False,False,False,True,False,True,True,False,True,True,True,False,True]],[[True,True,False,False,True,True,True,False,False,False,False,False,True,False],[False,True,True,True,False,True,True,True,True,False,True,True,False,False],[False,False,True,True,False,True,False,True,False,True,True,True,True,False],[True,False,False,False,False,True,True,False,False,False,True,True,False,False],[True,False,True,True,True,False,True,True,False,True,False,False,False,True],[True,True,True,True,False,False,True,False,True,False,False,False,False,True],[True,False,False,False,True,True,False,False,True,True,True,True,False,True],[False,False,False,True,True,False,False,True,False,True,True,True,True,True],[True,True,True,True,False,True,True,True,False,True,True,True,False,False]],[[True,False,True,True,False,True,False,False,True,True,True,True,False,True],[True,False,False,False,True,True,True,True,False,True,False,False,False,True],[False,True,True,True,True,False,False,False,False,False,False,True,True,True],[True,False,False,False,False,True,False,True,False,False,True,True,True,True],[True,True,True,True,False,False,False,False,True,False,False,True,True,False],[False,False,True,True,False,False,True,False,True,False,False,True,False,True],[False,True,False,False,False,True,True,True,False,False,True,True,False,True],[False,True,True,False,False,False,False,False,False,True,True,True,True,True],[True,True,False,True,False,False,True,True,False,True,False,False,True,True]],[[True,True,False,True,True,True,True,True,True,True,True,False,True,False],[True,False,True,False,False,True,False,False,False,True,True,False,False,True],[False,True,False,True,True,False,False,False,True,True,True,True,True,False],[True,False,True,False,False,False,True,False,False,True,True,False,False,False],[False,True,False,False,False,False,True,True,True,True,True,False,False,False],[True,True,True,False,True,False,True,False,False,False,False,False,True,True],[False,True,False,False,False,False,False,True,False,True,False,True,False,False],[False,True,False,True,False,True,False,False,True,True,False,False,True,False],[False,False,False,True,True,False,True,False,False,False,True,False,True,True]],[[False,False,True,False,True,False,True,True,True,True,True,True,False,True],[True,True,False,True,True,False,False,True,False,False,True,False,False,False],[False,True,True,False,True,True,False,False,True,False,False,False,True,True],[True,False,True,False,True,True,False,True,True,False,False,True,False,True],[True,False,True,True,False,False,False,True,True,False,False,False,False,False],[True,False,True,False,False,False,True,True,True,True,False,False,True,False],[True,False,True,False,False,False,False,False,True,False,False,False,False,False],[True,True,False,False,True,True,False,True,False,True,False,True,False,True],[False,False,True,True,False,True,False,False,True,False,True,False,False,True]],[[True,False,True,False,True,True,False,False,False,False,True,False,False,False],[False,False,True,False,False,False,True,False,True,True,True,True,True,False],[True,True,True,False,False,False,False,True,True,False,False,True,True,True],[False,True,True,False,True,False,False,False,True,True,False,False,True,True],[True,False,True,True,False,False,True,False,False,False,True,True,False,True],[True,True,True,True,False,False,True,False,True,True,False,False,False,False],[False,True,False,False,False,True,True,False,False,False,False,False,False,True],[False,True,True,True,False,False,False,True,False,True,True,True,False,True],[True,False,True,False,False,True,False,False,True,True,False,True,True,False]],[[True,False,True,True,True,False,False,True,False,False,False,True,True,True],[False,True,False,False,False,False,False,False,True,False,False,False,True,False],[True,False,False,True,False,True,False,True,False,True,True,False,True,True],[True,True,True,False,False,True,False,False,True,False,False,True,False,False],[True,True,False,True,True,False,False,False,False,False,True,False,True,False],[False,True,False,False,False,True,False,False,False,False,True,False,False,True],[True,False,False,False,True,False,True,False,True,True,False,True,False,False],[True,True,False,True,False,False,True,False,True,True,True,False,True,False],[False,True,True,True,True,True,True,False,False,True,True,True,False,True]],[[False,False,True,True,False,False,False,False,False,False,True,False,True,False],[False,True,False,False,False,True,True,False,True,False,False,True,True,True],[False,False,True,False,False,False,True,False,False,True,True,True,True,False],[True,True,False,True,False,False,True,False,True,False,False,False,False,True],[True,False,False,True,False,True,True,False,False,False,True,False,False,False],[True,True,False,False,False,False,True,False,False,False,True,True,False,True],[False,True,False,True,True,True,True,True,False,False,True,False,True,False],[True,True,False,False,False,False,True,True,False,False,True,False,True,False],[False,True,False,False,False,False,True,True,True,False,False,False,True,False]],[[False,False,False,True,True,True,False,True,True,True,False,False,True,False],[False,False,False,False,False,False,False,False,True,False,False,False,False,False],[False,True,False,True,True,True,False,False,False,False,False,True,True,False],[True,True,False,False,True,True,False,True,True,True,False,False,True,False],[True,True,False,True,True,True,False,False,False,True,True,False,True,True],[True,True,True,True,False,False,True,True,True,True,True,False,False,True],[True,True,True,False,True,True,True,False,False,False,False,False,True,True],[False,False,False,False,True,False,True,True,False,False,True,True,True,False],[True,False,True,False,True,False,False,False,True,False,False,False,False,True]],[[False,True,False,True,True,True,True,True,True,False,False,True,False,True],[False,True,True,True,True,False,False,True,False,False,True,False,False,False],[False,False,True,False,True,True,True,True,False,False,False,True,False,False],[False,False,False,False,False,True,False,True,False,False,False,False,False,False],[False,True,False,False,True,True,True,True,False,False,False,True,True,False],[False,True,False,True,False,False,True,False,False,True,True,False,True,False],[False,False,False,True,True,False,True,False,True,False,True,True,True,True],[False,False,True,True,True,False,False,True,False,True,True,False,True,True],[False,False,True,True,False,True,False,True,True,True,False,False,False,True]],[[True,True,True,False,True,False,True,False,False,True,False,True,False,True],[True,True,False,False,False,True,True,False,False,True,False,True,False,False],[True,False,True,True,True,False,True,False,True,False,True,True,True,True],[False,True,False,False,True,True,False,True,False,True,True,True,False,True],[False,False,True,False,True,True,True,False,True,False,True,False,False,False],[False,True,True,False,False,True,False,True,False,False,False,True,True,False],[False,True,True,False,False,True,False,True,False,True,True,True,True,False],[False,True,False,False,False,True,False,True,True,True,False,True,True,True],[False,True,True,False,False,False,True,False,True,True,True,True,True,True]],[[True,False,True,True,False,False,True,False,True,True,True,False,False,False],[False,False,True,False,True,False,True,True,False,False,False,False,True,True],[True,False,False,False,True,False,True,True,False,False,True,True,False,True],[False,False,True,False,False,False,False,True,False,True,True,False,True,True],[False,True,False,False,True,True,False,False,True,False,True,True,False,True],[False,False,False,False,True,True,False,True,True,True,True,True,False,False],[True,False,True,False,True,True,False,False,False,False,True,True,False,False],[False,True,True,True,True,True,True,False,False,False,False,True,True,True],[False,True,True,False,True,False,False,False,True,False,True,False,False,False]],[[True,True,False,False,False,False,True,True,True,False,False,False,False,False],[True,True,True,False,True,False,False,False,False,False,True,True,False,False],[True,False,False,True,True,False,True,True,False,False,True,False,False,True],[False,True,True,True,False,False,True,True,False,True,False,False,True,True],[True,True,True,True,False,True,False,True,True,True,True,False,True,False],[False,True,True,False,False,False,True,True,False,True,False,False,False,False],[False,False,True,True,True,False,False,True,True,False,True,True,True,False],[True,False,False,True,False,True,True,False,True,False,True,True,True,False],[True,False,False,True,False,False,False,True,False,True,True,False,True,False]]], dtype = "bool")#candidate|3658|(14, 9, 14)|const|bool
var_3659 = relay.var("var_3659", dtype = "bool", shape = (14, 9, 14))#candidate|3659|(14, 9, 14)|var|bool
bop_3660 = relay.logical_and(const_3658.astype('bool'), relay.reshape(var_3659.astype('bool'), relay.shape_of(const_3658))) # shape=(14, 9, 14)
func_1809_call = mod.get_global_var('func_1809')
func_1813_call = mutated_mod.get_global_var('func_1813')
const_3683 = relay.const([9,3,8,-1,-6,-10,-3,7,7,1,3,-1,10,-9,7,4,-9,-9,-5,-1,-9,7,-9,-4,-2,2,6,8,-5,2,6,-9,-2,-3,9,10,-6,1,-3,2,1,-3,-9,-10,9,-10,7,9,8,-6,5,-4,-5,6,10,-3,4,-8,8,-9,2,-9,9,-10,-7,1,-2,-3,-9,-7,7,-2,8,3,-1,-1,4,-4,8,-9,10,-9,4,-1,10,-4,8,9,-7,1,7,-1,-6,5,8,-10,-3,-1,2,-1,-10,1,-10,-7,3,5,2,2,-2,1,-8,-8,-4,9,3,-8,5,-2,-10,-2,-6,2,2,7,10,3,3,-10,-2,-10,-8,-7,-8,6,9,10,4,5,-5,-3,2,-2,9,9,10,6,8,1,-4,5,-6,1,4,-9,8,-3,-7,-5,-8,8,4,5,9,9,6,9,8,3,5,2,-3,-6,-1,-9,-7,-6,-2,4,-9,-9,8,7,9,9,-4,-9,-7,7,10,-4,4,-8,3,10,-9,-8,-6,-5,7,-8,5,5,-6,8,10,-3,-4,-1,-4,-10,9,-10,-3,9,-8,-8,-6,-5,-9,8,-6,6,-3,8,9,10,4,-2,-6,-6,9,9,10,8,8,-1,-9,6,-5,9,2,1,-1,4,7,4,-5,1,-9,-5,9,1,4,-7,-4,2,-6,-4,7,6,10,-9,-3,10,-1,8,4,7,-9,-6,1,-8,8,-3,10,8,7,4,-10,-3,3,1,1,5,2,-2,7,9,-2,2,-10,-3,-10,1,3,-10,-5,6,-9,-7,-10,4,-9,-7,-5,-4,-1,-4,-5,-2,-10,7,-3,3,-3,5,-1,3,1,-2,8,1,-4,2,-1,8,-7,7,7,2,-10,3,5,1,7,2,9,7,-10,3,-3,1,5,10,7,3,-10,-1,4,10,-5,-9,8,2,-6,9,5,1,-9,-3,4,6,-2,-8,-8,10,-3,-2,6,10,8,-3,-1,-4,-5,7,-4,-3,9,-5,-10,-4,5,-5,-9,-2,6,9,-10,-10,-1,8,1,2,-5,-8,-3,9,6,8,10,-4,7,-8,8,6,4,-3,-5,4,1,4,-2,-1,-8,-8,10,9,-5,4,4,1,4,-4,10,-1,-9,6,-10,4,7,-10,-3,-2,-5,-2,-8,6,8,5,9,-10,2,2,4,-4,9,5,1,10], dtype = "int16")#candidate|3683|(450,)|const|int16
call_3682 = func_1809_call(relay.reshape(const_3683.astype('int16'), [2, 15, 15]), relay.reshape(const_3683.astype('int16'), [2, 15, 15]), )
call_3684 = func_1809_call(relay.reshape(const_3683.astype('int16'), [2, 15, 15]), relay.reshape(const_3683.astype('int16'), [2, 15, 15]), )
output = relay.Tuple([bop_3660,call_3682,const_3683,])
output2 = relay.Tuple([bop_3660,call_3684,const_3683,])
func_3694 = relay.Function([var_3659,], output)
mod['func_3694'] = func_3694
mod = relay.transform.InferType()(mod)
mutated_mod['func_3694'] = func_3694
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3695 = relay.var("var_3695", dtype = "bool", shape = (14, 9, 14))#candidate|3695|(14, 9, 14)|var|bool
func_3694_call = mutated_mod.get_global_var('func_3694')
call_3696 = func_3694_call(var_3695)
output = call_3696
func_3697 = relay.Function([var_3695], output)
mutated_mod['func_3697'] = func_3697
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3334_call = mod.get_global_var('func_3334')
func_3335_call = mutated_mod.get_global_var('func_3335')
call_3704 = relay.TupleGetItem(func_3334_call(), 0)
call_3705 = relay.TupleGetItem(func_3335_call(), 0)
func_2516_call = mod.get_global_var('func_2516')
func_2518_call = mutated_mod.get_global_var('func_2518')
call_3718 = relay.TupleGetItem(func_2516_call(), 3)
call_3719 = relay.TupleGetItem(func_2518_call(), 3)
func_1330_call = mod.get_global_var('func_1330')
func_1332_call = mutated_mod.get_global_var('func_1332')
call_3736 = func_1330_call()
call_3737 = func_1330_call()
func_1731_call = mod.get_global_var('func_1731')
func_1733_call = mutated_mod.get_global_var('func_1733')
call_3762 = func_1731_call()
call_3763 = func_1731_call()
func_2683_call = mod.get_global_var('func_2683')
func_2684_call = mutated_mod.get_global_var('func_2684')
call_3766 = func_2683_call()
call_3767 = func_2683_call()
func_463_call = mod.get_global_var('func_463')
func_466_call = mutated_mod.get_global_var('func_466')
const_3772 = relay.const(3, dtype = "uint16")#candidate|3772|()|const|uint16
call_3771 = relay.TupleGetItem(func_463_call(relay.reshape(call_3704.astype('int32'), [11, 14, 8]), relay.reshape(const_3772.astype('uint16'), []), ), 0)
call_3773 = relay.TupleGetItem(func_466_call(relay.reshape(call_3704.astype('int32'), [11, 14, 8]), relay.reshape(const_3772.astype('uint16'), []), ), 0)
func_2698_call = mod.get_global_var('func_2698')
func_2700_call = mutated_mod.get_global_var('func_2700')
call_3777 = relay.TupleGetItem(func_2698_call(), 0)
call_3778 = relay.TupleGetItem(func_2700_call(), 0)
func_589_call = mod.get_global_var('func_589')
func_592_call = mutated_mod.get_global_var('func_592')
var_3782 = relay.var("var_3782", dtype = "uint64", shape = (252,))#candidate|3782|(252,)|var|uint64
call_3781 = relay.TupleGetItem(func_589_call(relay.reshape(const_3772.astype('uint64'), []), relay.reshape(var_3782.astype('uint64'), [252,]), ), 1)
call_3783 = relay.TupleGetItem(func_592_call(relay.reshape(const_3772.astype('uint64'), []), relay.reshape(var_3782.astype('uint64'), [252,]), ), 1)
uop_3801 = relay.log(call_3777.astype('float32')) # shape=(2, 3, 1)
uop_3803 = relay.log(call_3778.astype('float32')) # shape=(2, 3, 1)
bop_3806 = relay.floor_divide(uop_3801.astype('float64'), call_3718.astype('float64')) # shape=(2, 3, 672)
bop_3809 = relay.floor_divide(uop_3803.astype('float64'), call_3719.astype('float64')) # shape=(2, 3, 672)
uop_3822 = relay.sqrt(uop_3801.astype('float64')) # shape=(2, 3, 1)
uop_3824 = relay.sqrt(uop_3803.astype('float64')) # shape=(2, 3, 1)
bop_3825 = relay.logical_and(uop_3822.astype('bool'), relay.reshape(uop_3801.astype('bool'), relay.shape_of(uop_3822))) # shape=(2, 3, 1)
bop_3828 = relay.logical_and(uop_3824.astype('bool'), relay.reshape(uop_3803.astype('bool'), relay.shape_of(uop_3824))) # shape=(2, 3, 1)
func_2892_call = mod.get_global_var('func_2892')
func_2895_call = mutated_mod.get_global_var('func_2895')
const_3832 = relay.const([-6.164448,3.102322,-8.360517,5.959619,9.829293,-1.125850,-8.096638,-2.423598,2.211577,5.078377,0.372943,1.145058,-1.520347,2.074874,7.758628,-3.066237,2.999861,-0.465765,-0.966811,-5.903654,9.793075,-2.368636,-0.070618,9.453198,9.720537,-1.783689,1.781995,-6.704677,-3.255448,-0.776410,8.111690,8.976556,-4.078892,-5.524955,-6.344613,5.229216,2.974883,6.123410,-5.026195,1.331169,1.143592,-9.194532,-4.063640,-9.269943,-9.905778,-2.173099,9.366923,5.231300,6.215645,-2.968460,-5.227206,5.074206,2.942931,1.480534,9.920478,7.576866,-3.772822,-7.151952,-0.054763,5.829930,7.363993,-3.391083,-0.690597,-9.506328,-2.968758,7.541797,-4.185836,-4.086070,9.831596,4.004566,1.570614,-4.749863], dtype = "float64")#candidate|3832|(72,)|const|float64
call_3831 = relay.TupleGetItem(func_2892_call(relay.reshape(const_3832.astype('float64'), [2, 3, 12]), relay.reshape(const_3772.astype('uint16'), []), ), 4)
call_3833 = relay.TupleGetItem(func_2895_call(relay.reshape(const_3832.astype('float64'), [2, 3, 12]), relay.reshape(const_3772.astype('uint16'), []), ), 4)
bop_3838 = relay.bitwise_and(call_3766.astype('uint64'), relay.reshape(call_3771.astype('uint64'), relay.shape_of(call_3766))) # shape=(11, 14, 8)
bop_3841 = relay.bitwise_and(call_3767.astype('uint64'), relay.reshape(call_3773.astype('uint64'), relay.shape_of(call_3767))) # shape=(11, 14, 8)
bop_3850 = relay.less_equal(bop_3825.astype('bool'), const_3772.astype('bool')) # shape=(2, 3, 1)
bop_3853 = relay.less_equal(bop_3828.astype('bool'), const_3772.astype('bool')) # shape=(2, 3, 1)
func_1965_call = mod.get_global_var('func_1965')
func_1966_call = mutated_mod.get_global_var('func_1966')
call_3857 = relay.TupleGetItem(func_1965_call(), 0)
call_3858 = relay.TupleGetItem(func_1966_call(), 0)
func_2249_call = mod.get_global_var('func_2249')
func_2251_call = mutated_mod.get_global_var('func_2251')
call_3866 = relay.TupleGetItem(func_2249_call(), 0)
call_3867 = relay.TupleGetItem(func_2251_call(), 0)
output = relay.Tuple([call_3704,call_3736,call_3762,call_3781,var_3782,bop_3806,call_3831,const_3832,bop_3838,bop_3850,call_3857,call_3866,])
output2 = relay.Tuple([call_3705,call_3737,call_3763,call_3783,var_3782,bop_3809,call_3833,const_3832,bop_3841,bop_3853,call_3858,call_3867,])
func_3870 = relay.Function([var_3782,], output)
mod['func_3870'] = func_3870
mod = relay.transform.InferType()(mod)
mutated_mod['func_3870'] = func_3870
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3871 = relay.var("var_3871", dtype = "uint64", shape = (252,))#candidate|3871|(252,)|var|uint64
func_3870_call = mutated_mod.get_global_var('func_3870')
call_3872 = func_3870_call(var_3871)
output = call_3872
func_3873 = relay.Function([var_3871], output)
mutated_mod['func_3873'] = func_3873
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2289_call = mod.get_global_var('func_2289')
func_2291_call = mutated_mod.get_global_var('func_2291')
call_3894 = func_2289_call()
call_3895 = func_2289_call()
func_3277_call = mod.get_global_var('func_3277')
func_3280_call = mutated_mod.get_global_var('func_3280')
call_3916 = relay.TupleGetItem(func_3277_call(relay.reshape(call_3894.astype('float64'), [1232,])), 0)
call_3917 = relay.TupleGetItem(func_3280_call(relay.reshape(call_3894.astype('float64'), [1232,])), 0)
func_1581_call = mod.get_global_var('func_1581')
func_1583_call = mutated_mod.get_global_var('func_1583')
call_3918 = relay.TupleGetItem(func_1581_call(), 0)
call_3919 = relay.TupleGetItem(func_1583_call(), 0)
func_1560_call = mod.get_global_var('func_1560')
func_1562_call = mutated_mod.get_global_var('func_1562')
call_3923 = relay.TupleGetItem(func_1560_call(), 0)
call_3924 = relay.TupleGetItem(func_1562_call(), 0)
func_3469_call = mod.get_global_var('func_3469')
func_3471_call = mutated_mod.get_global_var('func_3471')
call_3928 = relay.TupleGetItem(func_3469_call(), 0)
call_3929 = relay.TupleGetItem(func_3471_call(), 0)
output = relay.Tuple([call_3894,call_3916,call_3918,call_3923,call_3928,])
output2 = relay.Tuple([call_3895,call_3917,call_3919,call_3924,call_3929,])
func_3933 = relay.Function([], output)
mod['func_3933'] = func_3933
mod = relay.transform.InferType()(mod)
output = func_3933()
func_3934 = relay.Function([], output)
mutated_mod['func_3934'] = func_3934
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3334_call = mod.get_global_var('func_3334')
func_3335_call = mutated_mod.get_global_var('func_3335')
call_3947 = relay.TupleGetItem(func_3334_call(), 0)
call_3948 = relay.TupleGetItem(func_3335_call(), 0)
func_1500_call = mod.get_global_var('func_1500')
func_1503_call = mutated_mod.get_global_var('func_1503')
var_3973 = relay.var("var_3973", dtype = "float64", shape = (504,))#candidate|3973|(504,)|var|float64
call_3972 = relay.TupleGetItem(func_1500_call(relay.reshape(var_3973.astype('float64'), [14, 3, 12])), 0)
call_3974 = relay.TupleGetItem(func_1503_call(relay.reshape(var_3973.astype('float64'), [14, 3, 12])), 0)
output = relay.Tuple([call_3947,call_3972,var_3973,])
output2 = relay.Tuple([call_3948,call_3974,var_3973,])
func_3993 = relay.Function([var_3973,], output)
mod['func_3993'] = func_3993
mod = relay.transform.InferType()(mod)
mutated_mod['func_3993'] = func_3993
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3994 = relay.var("var_3994", dtype = "float64", shape = (504,))#candidate|3994|(504,)|var|float64
func_3993_call = mutated_mod.get_global_var('func_3993')
call_3995 = func_3993_call(var_3994)
output = call_3995
func_3996 = relay.Function([var_3994], output)
mutated_mod['func_3996'] = func_3996
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2490_call = mod.get_global_var('func_2490')
func_2491_call = mutated_mod.get_global_var('func_2491')
call_4006 = func_2490_call()
call_4007 = func_2490_call()
output = call_4006
output2 = call_4007
func_4010 = relay.Function([], output)
mod['func_4010'] = func_4010
mod = relay.transform.InferType()(mod)
output = func_4010()
func_4011 = relay.Function([], output)
mutated_mod['func_4011'] = func_4011
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4024 = relay.const([[[-5.016762,5.758871,-0.067983,-9.658458,-3.799112,-0.211753,6.637046,6.726061,2.935596,4.373757,-8.720928,4.779963,-5.856046,9.686833],[1.417543,-3.325109,-4.340290,-5.780810,7.154077,1.761384,-9.613553,-8.012101,2.666069,-4.962920,-1.600332,1.262297,4.610537,-9.705219],[-3.856749,9.152674,-9.828223,4.113014,4.680729,2.384134,-4.543361,-0.438740,-4.566817,6.999066,-5.129712,9.944417,1.782440,-1.369543],[7.653328,-5.644285,-5.588087,-0.372942,5.863567,-3.205791,3.114713,1.617283,-1.940870,-0.287483,-0.643255,2.489646,-7.724258,-1.784060],[5.313073,-2.931695,2.073031,6.610909,-9.853167,-8.468272,4.202238,-4.674251,-0.301442,5.549472,-5.897853,-1.161314,0.522149,6.540175],[-8.806012,6.060720,-5.683150,-5.821051,8.174547,-9.570374,8.174554,6.500301,1.296724,2.848240,-9.669288,-1.083205,1.300815,3.087728]],[[-7.538618,-0.958479,-3.859725,1.541293,1.201750,-0.418760,0.522084,8.885066,0.455344,2.211371,-5.311747,0.240045,1.544569,3.467859],[-5.983196,4.655699,-0.487661,4.040825,-6.574431,0.774207,-2.179747,-7.652880,-6.952465,1.819674,-6.045872,-0.758208,8.437442,7.809231],[-9.729362,7.045623,-2.329363,9.022697,-1.323883,8.690298,7.110769,4.658419,7.446768,7.413606,3.819697,7.995750,-0.431417,-8.724273],[8.226785,-1.961312,2.215610,-1.662623,3.851776,-2.904680,-5.209627,-7.536308,-6.730254,-6.095958,1.874286,-4.148800,-6.876909,-6.426839],[9.788302,-0.942888,0.589855,-0.559290,3.088977,-2.685363,9.372584,-3.342419,-8.387067,4.595244,-2.897698,-5.004880,-9.840164,-7.692564],[7.264192,9.790692,-6.244867,5.325117,-3.203396,-2.380819,3.029745,-1.908829,2.023407,-0.485402,2.015571,-2.269822,3.618501,9.495079]]], dtype = "float64")#candidate|4024|(2, 6, 14)|const|float64
const_4025 = relay.const([[[-0.407545,9.190457,-2.410761,-0.164963,6.177191,2.572776,-6.436590,-9.050212,7.149214,9.366571,1.998015,-5.784976,4.195007,6.461008],[9.134956,-4.852113,4.284781,2.537190,7.409652,4.554713,-3.781029,-2.943270,4.016158,-2.313422,-0.207754,5.300484,-8.574281,-5.821914],[1.041002,5.658556,-6.275175,0.929957,8.980096,3.680917,-4.488354,5.625930,-0.833876,5.901905,-5.154919,-8.775195,9.267748,-3.498493],[6.669445,0.247402,-4.711139,8.686225,3.071546,-0.072270,3.377367,4.844917,6.782931,3.260211,1.708911,1.242365,-9.647333,-9.190502],[8.866616,9.490358,4.131684,-8.724038,2.038479,5.561483,-7.991326,3.095027,3.226548,0.048885,9.826634,-5.583305,1.283447,-0.694768],[-5.156199,1.235527,-7.517248,-3.411137,-9.298877,0.067911,8.464776,-1.465389,2.792604,1.948178,-5.961476,0.261681,5.337920,-5.451065]],[[7.104356,-5.228935,-9.474158,-7.718601,3.815493,-0.852538,9.901278,3.704159,-4.242345,-7.468183,-6.163222,6.540499,-7.491279,-4.436341],[-5.986548,-1.040930,-5.251206,1.557978,-9.536302,3.900105,4.152544,1.546129,6.595127,9.861734,-4.495865,5.494828,7.993568,-9.837750],[2.549741,-5.179564,9.529867,-9.733648,8.619356,-1.359659,7.830339,7.640687,-3.611181,4.602718,-0.761714,6.622322,-0.397391,4.932255],[3.117873,6.155508,-4.831534,2.128834,-4.893500,5.244071,9.785354,2.511532,5.982480,2.024910,-5.095883,-5.799308,4.703814,8.687607],[-7.787369,-8.213221,-9.146461,0.262713,7.069971,9.843271,-4.249702,4.220742,-7.003735,-8.186075,-1.739391,7.063040,-1.860830,2.997961],[-6.051653,1.659923,9.372457,-6.786504,5.726524,-3.168909,-0.070834,-6.515961,8.599361,5.460262,-2.303242,6.028018,4.394557,1.266634]]], dtype = "float64")#candidate|4025|(2, 6, 14)|const|float64
bop_4026 = relay.floor_divide(const_4024.astype('float64'), relay.reshape(const_4025.astype('float64'), relay.shape_of(const_4024))) # shape=(2, 6, 14)
func_695_call = mod.get_global_var('func_695')
func_696_call = mutated_mod.get_global_var('func_696')
call_4030 = relay.TupleGetItem(func_695_call(), 1)
call_4031 = relay.TupleGetItem(func_696_call(), 1)
func_2892_call = mod.get_global_var('func_2892')
func_2895_call = mutated_mod.get_global_var('func_2895')
const_4037 = relay.const([1.298365,6.649714,1.145014,-0.784929,7.263847,-6.515174,-7.870930,6.726251,-8.585128,0.354569,7.381594,-7.652058,4.159612,-2.966896,-7.317411,1.949061,-4.384145,5.059602,6.285322,4.970807,2.140199,-9.449090,-3.164866,-2.357765,-3.030824,4.686856,3.599629,9.005159,-2.141835,7.470477,0.388267,-5.327202,2.256228,-8.469779,9.801492,6.226138,1.006206,-0.653106,9.693660,-6.529640,-7.175892,2.481295,6.368841,-4.476502,6.796483,-8.255570,-3.512991,-1.984877,-7.891969,-8.694266,-0.011751,4.649362,3.327687,1.546443,-8.121030,7.217113,3.473074,-3.731027,4.309413,1.042972,-7.426020,-0.878694,-9.344999,-1.525194,1.681358,7.086237,-8.984794,5.046081,-0.499869,-5.263879,-8.142913,-6.926579], dtype = "float64")#candidate|4037|(72,)|const|float64
call_4036 = relay.TupleGetItem(func_2892_call(relay.reshape(const_4037.astype('float64'), [2, 3, 12]), relay.reshape(call_4030.astype('uint16'), []), ), 3)
call_4038 = relay.TupleGetItem(func_2895_call(relay.reshape(const_4037.astype('float64'), [2, 3, 12]), relay.reshape(call_4030.astype('uint16'), []), ), 3)
var_4040 = relay.var("var_4040", dtype = "float64", shape = (2, 6, 14))#candidate|4040|(2, 6, 14)|var|float64
bop_4041 = relay.multiply(bop_4026.astype('uint32'), relay.reshape(var_4040.astype('uint32'), relay.shape_of(bop_4026))) # shape=(2, 6, 14)
output = relay.Tuple([call_4030,call_4036,const_4037,bop_4041,])
output2 = relay.Tuple([call_4031,call_4038,const_4037,bop_4041,])
func_4048 = relay.Function([var_4040,], output)
mod['func_4048'] = func_4048
mod = relay.transform.InferType()(mod)
mutated_mod['func_4048'] = func_4048
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4049 = relay.var("var_4049", dtype = "float64", shape = (2, 6, 14))#candidate|4049|(2, 6, 14)|var|float64
func_4048_call = mutated_mod.get_global_var('func_4048')
call_4050 = func_4048_call(var_4049)
output = call_4050
func_4051 = relay.Function([var_4049], output)
mutated_mod['func_4051'] = func_4051
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3127_call = mod.get_global_var('func_3127')
func_3128_call = mutated_mod.get_global_var('func_3128')
call_4191 = func_3127_call()
call_4192 = func_3127_call()
uop_4197 = relay.atanh(call_4191.astype('float32')) # shape=(2, 3, 1)
uop_4199 = relay.atanh(call_4192.astype('float32')) # shape=(2, 3, 1)
func_1500_call = mod.get_global_var('func_1500')
func_1503_call = mutated_mod.get_global_var('func_1503')
var_4203 = relay.var("var_4203", dtype = "float64", shape = (504,))#candidate|4203|(504,)|var|float64
call_4202 = relay.TupleGetItem(func_1500_call(relay.reshape(var_4203.astype('float64'), [14, 3, 12])), 0)
call_4204 = relay.TupleGetItem(func_1503_call(relay.reshape(var_4203.astype('float64'), [14, 3, 12])), 0)
func_1763_call = mod.get_global_var('func_1763')
func_1766_call = mutated_mod.get_global_var('func_1766')
var_4208 = relay.var("var_4208", dtype = "float64", shape = (640,))#candidate|4208|(640,)|var|float64
call_4207 = relay.TupleGetItem(func_1763_call(relay.reshape(var_4208.astype('float64'), [16, 5, 8])), 0)
call_4209 = relay.TupleGetItem(func_1766_call(relay.reshape(var_4208.astype('float64'), [16, 5, 8])), 0)
output = relay.Tuple([uop_4197,call_4202,var_4203,call_4207,var_4208,])
output2 = relay.Tuple([uop_4199,call_4204,var_4203,call_4209,var_4208,])
func_4226 = relay.Function([var_4203,var_4208,], output)
mod['func_4226'] = func_4226
mod = relay.transform.InferType()(mod)
mutated_mod['func_4226'] = func_4226
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4226_call = mutated_mod.get_global_var('func_4226')
var_4228 = relay.var("var_4228", dtype = "float64", shape = (504,))#candidate|4228|(504,)|var|float64
var_4229 = relay.var("var_4229", dtype = "float64", shape = (640,))#candidate|4229|(640,)|var|float64
call_4227 = func_4226_call(var_4228,var_4229,)
output = call_4227
func_4230 = relay.Function([var_4228,var_4229,], output)
mutated_mod['func_4230'] = func_4230
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4232 = relay.var("var_4232", dtype = "int16", shape = (2, 4, 11))#candidate|4232|(2, 4, 11)|var|int16
var_4233 = relay.var("var_4233", dtype = "int16", shape = (2, 4, 11))#candidate|4233|(2, 4, 11)|var|int16
bop_4234 = relay.right_shift(var_4232.astype('int16'), relay.reshape(var_4233.astype('int16'), relay.shape_of(var_4232))) # shape=(2, 4, 11)
func_3694_call = mod.get_global_var('func_3694')
func_3697_call = mutated_mod.get_global_var('func_3697')
var_4241 = relay.var("var_4241", dtype = "bool", shape = (1764,))#candidate|4241|(1764,)|var|bool
call_4240 = relay.TupleGetItem(func_3694_call(relay.reshape(var_4241.astype('bool'), [14, 9, 14])), 2)
call_4242 = relay.TupleGetItem(func_3697_call(relay.reshape(var_4241.astype('bool'), [14, 9, 14])), 2)
func_960_call = mod.get_global_var('func_960')
func_962_call = mutated_mod.get_global_var('func_962')
call_4246 = relay.TupleGetItem(func_960_call(), 0)
call_4247 = relay.TupleGetItem(func_962_call(), 0)
output = relay.Tuple([bop_4234,call_4240,var_4241,call_4246,])
output2 = relay.Tuple([bop_4234,call_4242,var_4241,call_4247,])
func_4254 = relay.Function([var_4232,var_4233,var_4241,], output)
mod['func_4254'] = func_4254
mod = relay.transform.InferType()(mod)
var_4255 = relay.var("var_4255", dtype = "int16", shape = (2, 4, 11))#candidate|4255|(2, 4, 11)|var|int16
var_4256 = relay.var("var_4256", dtype = "int16", shape = (2, 4, 11))#candidate|4256|(2, 4, 11)|var|int16
var_4257 = relay.var("var_4257", dtype = "bool", shape = (1764,))#candidate|4257|(1764,)|var|bool
output = func_4254(var_4255,var_4256,var_4257,)
func_4258 = relay.Function([var_4255,var_4256,var_4257,], output)
mutated_mod['func_4258'] = func_4258
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2475_call = mod.get_global_var('func_2475')
func_2477_call = mutated_mod.get_global_var('func_2477')
call_4269 = relay.TupleGetItem(func_2475_call(), 0)
call_4270 = relay.TupleGetItem(func_2477_call(), 0)
var_4288 = relay.var("var_4288", dtype = "float32", shape = (11, 14, 8))#candidate|4288|(11, 14, 8)|var|float32
bop_4289 = relay.add(call_4269.astype('uint8'), relay.reshape(var_4288.astype('uint8'), relay.shape_of(call_4269))) # shape=(11, 14, 8)
bop_4292 = relay.add(call_4270.astype('uint8'), relay.reshape(var_4288.astype('uint8'), relay.shape_of(call_4270))) # shape=(11, 14, 8)
func_1440_call = mod.get_global_var('func_1440')
func_1442_call = mutated_mod.get_global_var('func_1442')
var_4312 = relay.var("var_4312", dtype = "uint16", shape = ())#candidate|4312|()|var|uint16
call_4311 = relay.TupleGetItem(func_1440_call(relay.reshape(var_4312.astype('uint16'), [])), 0)
call_4313 = relay.TupleGetItem(func_1442_call(relay.reshape(var_4312.astype('uint16'), [])), 0)
output = relay.Tuple([bop_4289,call_4311,var_4312,])
output2 = relay.Tuple([bop_4292,call_4313,var_4312,])
func_4321 = relay.Function([var_4288,var_4312,], output)
mod['func_4321'] = func_4321
mod = relay.transform.InferType()(mod)
mutated_mod['func_4321'] = func_4321
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4321_call = mutated_mod.get_global_var('func_4321')
var_4323 = relay.var("var_4323", dtype = "float32", shape = (11, 14, 8))#candidate|4323|(11, 14, 8)|var|float32
var_4324 = relay.var("var_4324", dtype = "uint16", shape = ())#candidate|4324|()|var|uint16
call_4322 = func_4321_call(var_4323,var_4324,)
output = call_4322
func_4325 = relay.Function([var_4323,var_4324,], output)
mutated_mod['func_4325'] = func_4325
mutated_mod = relay.transform.InferType()(mutated_mod)
func_426_call = mod.get_global_var('func_426')
func_427_call = mutated_mod.get_global_var('func_427')
call_4327 = relay.TupleGetItem(func_426_call(), 0)
call_4328 = relay.TupleGetItem(func_427_call(), 0)
func_1724_call = mod.get_global_var('func_1724')
func_1725_call = mutated_mod.get_global_var('func_1725')
call_4363 = relay.TupleGetItem(func_1724_call(), 3)
call_4364 = relay.TupleGetItem(func_1725_call(), 3)
output = relay.Tuple([call_4327,call_4363,])
output2 = relay.Tuple([call_4328,call_4364,])
func_4365 = relay.Function([], output)
mod['func_4365'] = func_4365
mod = relay.transform.InferType()(mod)
mutated_mod['func_4365'] = func_4365
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4365_call = mutated_mod.get_global_var('func_4365')
call_4366 = func_4365_call()
output = call_4366
func_4367 = relay.Function([], output)
mutated_mod['func_4367'] = func_4367
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3334_call = mod.get_global_var('func_3334')
func_3335_call = mutated_mod.get_global_var('func_3335')
call_4378 = relay.TupleGetItem(func_3334_call(), 0)
call_4379 = relay.TupleGetItem(func_3335_call(), 0)
func_3993_call = mod.get_global_var('func_3993')
func_3996_call = mutated_mod.get_global_var('func_3996')
var_4392 = relay.var("var_4392", dtype = "float64", shape = (2, 252))#candidate|4392|(2, 252)|var|float64
call_4391 = relay.TupleGetItem(func_3993_call(relay.reshape(var_4392.astype('float64'), [504,])), 0)
call_4393 = relay.TupleGetItem(func_3996_call(relay.reshape(var_4392.astype('float64'), [504,])), 0)
func_1809_call = mod.get_global_var('func_1809')
func_1813_call = mutated_mod.get_global_var('func_1813')
const_4402 = relay.const([10,-3,-4,-10,4,7,-7,5,6,-2,10,8,2,-4,-6,9,7,-7,-5,-9,-7,4,7,-5,1,10,7,7,-8,4,-2,-1,4,-1,7,1,6,7,7,10,1,-3,8,8,3,-1,6,5,2,-3,5,4,-9,9,-2,8,-9,-2,1,2,-3,-10,-8,10,-10,-10,5,8,-4,-2,4,-10,10,-9,-1,4,5,-4,10,3,-7,7,-7,-7,-10,7,-10,-6,-8,-9,7,6,9,6,-4,-9,4,-2,-9,-9,-10,4,3,10,6,-2,-5,6,8,1,-1,-2,6,-3,5,-3,-10,4,-6,5,-4,-6,7,2,2,-9,6,7,7,5,5,8,-7,-9,7,-7,-2,1,-5,-5,8,1,7,-4,-1,6,-10,-1,7,2,-3,8,-3,5,3,6,-5,-5,-8,-7,-9,5,9,8,6,-1,-10,4,-7,-5,2,2,-10,-10,-6,-9,3,-6,-10,8,6,-6,-8,2,-1,6,8,-1,-4,9,1,7,-2,6,-7,9,-6,2,7,-1,-10,-4,-6,-1,7,10,-7,-1,10,-2,-2,4,10,-3,-9,7,-1,2,-7,8,2,-3,-7,-10,2,7,7,-5,7,-3,-10,8,5,-1,-2,8,10,-6,6,7,-10,-5,8,-3,5,3,-10,1,2,8,4,9,5,-3,1,-10,-6,7,2,9,8,5,3,-3,-7,-9,5,4,-3,-1,-7,-5,-6,9,4,5,1,2,-5,1,4,-2,-9,-8,-5,7,2,7,8,-5,-5,6,8,10,-3,-5,2,-5,-6,-3,4,3,6,5,5,8,-8,-5,-4,-2,-7,-1,4,10,-9,-1,5,-2,-3,4,-6,-7,9,-5,-9,8,-3,7,-7,9,1,10,3,8,-10,3,7,2,-6,-8,3,-2,-5,6,-9,-7,-7,8,-2,8,-1,7,3,-5,-6,5,-9,8,8,-5,10,-7,2,7,-4,-3,5,6,-1,8,-3,9,-10,5,10,4,5,-7,7,-10,-8,-7,-5,5,-3,3,6,8,-8,5,-7,8,-10,-9,-10,9,4,-2,-10,-6,10,9,-3,3,1,9,-8,-10,-3,-7,-7,-10,-4,-1,9,-9,7,4,-6,1,-6,-7,-9,-3,7,-3,6,-7,-6,-7,6,-4,4,4,7,-9,-8,-9,5,-9,-2,7,8,10,-2,8,1,-2,-10,-4], dtype = "int16")#candidate|4402|(450,)|const|int16
call_4401 = func_1809_call(relay.reshape(const_4402.astype('int16'), [2, 15, 15]), relay.reshape(const_4402.astype('int16'), [2, 15, 15]), )
call_4403 = func_1809_call(relay.reshape(const_4402.astype('int16'), [2, 15, 15]), relay.reshape(const_4402.astype('int16'), [2, 15, 15]), )
output = relay.Tuple([call_4378,call_4391,var_4392,call_4401,const_4402,])
output2 = relay.Tuple([call_4379,call_4393,var_4392,call_4403,const_4402,])
func_4404 = relay.Function([var_4392,], output)
mod['func_4404'] = func_4404
mod = relay.transform.InferType()(mod)
mutated_mod['func_4404'] = func_4404
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4405 = relay.var("var_4405", dtype = "float64", shape = (2, 252))#candidate|4405|(2, 252)|var|float64
func_4404_call = mutated_mod.get_global_var('func_4404')
call_4406 = func_4404_call(var_4405)
output = call_4406
func_4407 = relay.Function([var_4405], output)
mutated_mod['func_4407'] = func_4407
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4417 = relay.var("var_4417", dtype = "int64", shape = (8, 7, 1))#candidate|4417|(8, 7, 1)|var|int64
var_4418 = relay.var("var_4418", dtype = "int64", shape = (8, 7, 6))#candidate|4418|(8, 7, 6)|var|int64
bop_4419 = relay.bitwise_or(var_4417.astype('int64'), var_4418.astype('int64')) # shape=(8, 7, 6)
uop_4423 = relay.log10(var_4417.astype('float32')) # shape=(8, 7, 1)
output = relay.Tuple([bop_4419,uop_4423,])
output2 = relay.Tuple([bop_4419,uop_4423,])
func_4426 = relay.Function([var_4417,var_4418,], output)
mod['func_4426'] = func_4426
mod = relay.transform.InferType()(mod)
var_4427 = relay.var("var_4427", dtype = "int64", shape = (8, 7, 1))#candidate|4427|(8, 7, 1)|var|int64
var_4428 = relay.var("var_4428", dtype = "int64", shape = (8, 7, 6))#candidate|4428|(8, 7, 6)|var|int64
output = func_4426(var_4427,var_4428,)
func_4429 = relay.Function([var_4427,var_4428,], output)
mutated_mod['func_4429'] = func_4429
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2544_call = mod.get_global_var('func_2544')
func_2546_call = mutated_mod.get_global_var('func_2546')
call_4446 = relay.TupleGetItem(func_2544_call(), 0)
call_4447 = relay.TupleGetItem(func_2546_call(), 0)
output = relay.Tuple([call_4446,])
output2 = relay.Tuple([call_4447,])
func_4457 = relay.Function([], output)
mod['func_4457'] = func_4457
mod = relay.transform.InferType()(mod)
mutated_mod['func_4457'] = func_4457
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4457_call = mutated_mod.get_global_var('func_4457')
call_4458 = func_4457_call()
output = call_4458
func_4459 = relay.Function([], output)
mutated_mod['func_4459'] = func_4459
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4010_call = mod.get_global_var('func_4010')
func_4011_call = mutated_mod.get_global_var('func_4011')
call_4521 = func_4010_call()
call_4522 = func_4010_call()
func_2984_call = mod.get_global_var('func_2984')
func_2986_call = mutated_mod.get_global_var('func_2986')
const_4525 = relay.const([[9.022375,6.850317],[1.614464,3.684825],[-9.239646,8.824296],[-5.098428,-0.003940],[-3.207931,7.354633],[-0.537176,6.493736],[4.969666,-1.715881],[9.714342,-3.251495],[3.803029,-7.246185],[-3.149657,0.586316],[-9.992328,2.203681],[-4.303073,-9.868689],[3.385786,-8.623112],[-0.100614,0.591305],[5.002905,6.383791],[-2.260780,3.091536],[-5.697537,-4.195933],[-7.936384,6.652972],[-5.855882,5.429877],[-4.502838,-9.654976],[-4.487658,4.300977],[-1.016633,-5.290877],[-2.732960,-2.035052],[4.147024,8.293883],[4.676960,-1.123725],[2.935905,-1.614593],[6.228900,5.114426],[-5.523303,4.248981],[-6.317822,8.418373],[7.670137,-9.974912],[4.362917,-6.900405],[4.518284,-2.394203],[-3.700654,-3.605886],[-0.802889,4.952718],[-1.455834,6.030858],[-3.335056,3.125646],[9.928685,1.859315],[-1.627145,5.605173],[-9.977599,-7.940461],[9.688213,-5.150925],[-1.489209,7.251193],[-7.242146,-0.248999],[3.515364,7.559235],[-8.916096,8.744316],[6.751949,-2.470899],[-9.850720,3.586621],[7.885202,-4.103710],[8.320801,-5.896631],[5.109258,-8.180002],[8.407722,5.389199],[2.933486,-2.624053],[5.696484,2.530916],[9.027306,3.012000],[1.081847,-0.655650],[-8.776069,8.952226],[-5.627302,2.195590],[-0.385647,9.962655],[-3.268609,-8.114830],[5.889402,7.876271],[-4.623988,1.808517],[-6.460624,-9.870343],[2.845179,3.958068],[7.371044,2.484534],[-1.485708,-4.166347],[0.940633,-4.359275],[-3.272271,3.470577],[-0.548660,-9.731647],[8.678536,-6.723606],[-3.964985,-1.798451],[7.323513,-1.684782],[-8.954674,-2.780250],[-6.515713,6.764607],[-9.221161,-5.544458],[7.387513,-1.569818],[-7.308230,-0.221339],[-7.887964,-6.534812],[1.817948,6.111323],[-3.109257,-0.939316],[3.742214,8.373817],[6.971237,9.998647],[5.850516,-1.589611],[1.869560,-4.066431],[0.763694,-4.104482],[4.409461,5.533434],[4.260129,6.540679],[-1.270957,-9.932578],[2.031432,6.024745],[9.835864,-4.392367],[-5.732017,6.082962],[-0.456293,-7.786456],[-0.029872,0.988466],[5.467846,4.906746],[2.676447,-7.246896],[-3.979880,-4.461638],[-9.346360,-8.155987],[-4.532479,-8.266478],[9.910996,5.808935],[8.130519,6.417186],[-0.433722,5.700778],[8.587996,-5.246599],[-4.117914,-6.837410],[2.488918,-7.908342],[1.887735,9.243453],[9.320717,-7.023653],[0.660327,-8.550077],[8.007702,9.720033],[7.485821,4.963140],[1.553458,2.827135],[-1.098612,-9.571805],[-9.710407,-7.219031],[6.463146,-7.102281],[9.392469,1.057195],[-8.706117,-1.492614],[1.928301,6.366926],[-3.483634,-6.880090],[-3.482093,0.816062],[5.762904,-9.700990],[-2.122820,2.432606],[4.840247,5.182051],[4.206591,3.555133],[-3.489414,3.327611],[5.602983,-7.664771],[-7.632774,7.320109],[1.195460,1.906109],[-9.151637,-5.534823],[-3.216210,-9.029108],[3.153327,6.273119],[-6.130749,-8.851578],[-8.748648,2.844237],[-4.550251,4.470769],[-8.591520,6.816259],[-2.502421,-4.824456],[6.214012,1.297041],[1.644556,1.503056],[7.770912,0.174343],[2.738402,7.868387],[7.851400,-3.497827],[-2.943125,-3.512950],[-7.195583,-0.454084],[0.134626,-1.721851],[-6.887903,-1.912980],[4.127398,-6.840975],[-2.281623,2.801015],[-3.806775,6.122377],[7.836742,9.597671],[-7.124579,-1.602936],[-3.859065,6.287814],[0.319715,-8.259784],[0.412351,6.302296],[-4.256761,-8.443435],[0.085369,-9.226554],[-3.123147,-3.872664],[5.445348,6.561461],[8.647098,2.518411],[5.234245,5.081392],[-9.815072,-4.351861],[7.134745,-4.752892],[1.531451,-1.766425],[-7.899283,-7.706261],[5.494126,-9.766002],[8.244578,-2.693126],[8.383194,-8.522110],[-8.769580,-4.108557],[6.148765,-6.980816],[-1.062479,-6.010380],[2.128068,4.713266],[4.535668,-0.365362],[-5.409762,-7.486931],[8.168340,-5.752667],[-7.428701,4.755966],[3.068315,6.693313],[-6.772862,0.380695],[-7.099107,-8.920701],[-8.513835,-0.328994],[-4.887730,-0.625075],[3.047440,-0.200483],[8.026460,-9.325992],[1.156513,-0.088225],[7.236482,1.424293],[-5.592120,-5.144664],[-3.273785,-0.389348],[-2.926018,-2.216612],[-6.139621,9.850832],[3.562049,-0.146365],[0.766960,-1.960177],[-8.710730,0.230306],[-1.796832,7.794095],[7.548619,-2.198803],[-5.745040,-7.546541],[1.953776,8.677554],[-3.886943,1.247850],[-7.025910,-9.484238],[-5.503300,-9.994272],[-9.098680,-4.382857],[-0.553279,0.092961],[-7.005735,8.352183],[-1.752138,7.662408],[0.096457,5.302912],[-6.403829,9.388211],[-7.466149,-6.375565],[2.620846,8.322487],[-3.632851,-1.914102],[8.187700,-4.858480],[3.434186,9.752109],[6.252761,4.633155],[6.727266,-6.741578],[-8.268206,0.187323],[-9.702233,1.956964],[-3.002621,9.612452],[2.898101,-3.119897],[7.793967,-8.915025],[-5.554583,-2.132652],[-2.080260,-6.137247],[5.197032,6.739575],[4.866057,-1.913006],[-1.347108,5.810421],[2.951562,9.056571],[-3.563116,9.342686],[-9.687663,6.954079],[6.466260,2.066389],[4.733613,-9.249444],[-2.560580,-3.609467],[-6.562685,1.821679],[6.557003,9.893539],[7.370448,5.449387],[-1.817225,7.386075],[-3.049680,-0.490978],[4.589911,9.808489],[7.691914,0.096347],[-5.470661,4.173390],[-4.728779,7.298333],[2.338511,-3.885121],[-5.616072,3.281888],[8.767990,7.549973],[4.860303,3.677760],[1.046545,5.479889],[-0.363370,8.044979],[4.521017,8.839145],[2.744369,6.655092],[-7.943152,-1.522372],[7.789099,5.667225],[-6.314087,-8.474053],[-7.508366,-6.405648],[-9.770232,3.760900],[-1.238674,4.318040],[7.788981,-9.244290],[-9.139822,-6.122442],[9.189981,0.821620],[-5.291503,6.154047],[6.063746,-0.951814],[-6.385989,-6.569143],[-5.424984,7.046564],[-7.927788,-3.380964],[-9.661832,-1.065485],[-3.642756,2.052432],[3.219390,-9.333321],[8.128165,5.013648],[1.433153,8.441118],[-2.649145,8.643491],[6.155075,-9.527050],[4.668488,6.202252],[6.182391,-2.192835],[-5.913937,8.904936],[-0.554971,2.175452],[-7.925298,5.865634],[-9.891041,9.709665],[-1.281538,-4.153794],[6.265867,9.080686],[7.122583,-8.681817],[-7.953354,4.189321],[-8.182875,3.971434],[-2.373843,3.647382],[5.806963,9.266797],[8.539294,-4.437197],[6.272980,9.638725],[7.552800,8.886921],[5.188867,7.050641],[1.318346,8.481644],[-0.289881,-2.108161],[1.263930,9.143729],[-1.866169,5.246065],[3.497581,5.626825],[-2.211371,6.780915],[8.604048,-2.270333],[9.219307,3.528931],[-2.493143,-1.406851],[1.305813,-3.517029],[-2.134217,7.963423],[-7.286221,-4.253940],[-0.837112,-8.985652],[-3.066145,0.515746],[-3.360738,5.478467],[2.279594,-4.951157],[3.734374,-2.021346],[-9.802883,3.323155],[-9.350344,1.110687],[9.121690,-4.294546],[-5.007217,-9.009519],[4.009130,-1.548446],[-9.462246,6.022565],[-8.525972,5.556586],[-4.540238,-7.835071],[-5.068739,-9.112595],[-4.044830,1.568367],[4.310426,-4.390601],[-3.061045,2.266658],[-8.664956,-1.204544],[6.197354,-2.876798],[3.200896,6.232237],[-0.180927,-5.692407],[8.439291,1.155777],[0.985026,-8.587543],[5.089267,-9.281937],[5.849136,9.332297],[8.127623,-5.086144],[4.332001,0.421202],[8.690641,-6.340256],[-7.574350,-6.822327],[6.253987,-8.949568],[0.381193,-6.818898],[6.639747,-1.830579],[-4.081801,-3.382929],[3.308905,-5.370394],[9.369617,-8.318757],[-5.823752,-0.826121],[0.059181,-7.115893],[6.000862,2.571312],[2.675729,8.665782],[-6.310428,-3.391142],[7.060409,8.520269],[8.254073,9.436802],[2.619165,9.234160],[-4.373748,-3.364817],[7.899379,5.475841],[9.301657,7.526690],[-0.957720,5.265212],[-7.949438,1.677632],[-2.854443,9.370085],[-1.868856,2.143033],[-7.158127,8.708004],[-0.530082,-4.226564],[-3.539668,-0.395500],[3.593819,4.459887],[-6.514810,-0.370781],[-6.967346,-9.569133],[-0.982805,-0.686016],[-9.776174,-2.509137],[6.381194,-0.166342],[-3.114538,9.316291],[-4.603472,-1.713674],[1.172885,7.218670],[0.471906,-2.272764],[6.262253,-0.252713],[-6.469564,-2.998435],[-0.250159,2.284480],[-6.347627,-5.121183],[9.251687,0.519063],[4.018063,8.995827],[6.043227,6.495588],[-1.968536,-6.809717],[-9.242339,-3.244662],[-3.787160,-3.620538],[4.935161,-0.404221],[8.371300,-2.524411],[-8.372680,-8.395412],[-6.655047,-4.905570],[-2.085559,-2.234937],[7.844475,-0.292665],[2.499106,5.989347],[4.393809,2.176179],[1.596684,-6.767229],[-3.246445,8.039758],[-5.584934,-9.960519],[3.140983,2.725102],[-5.757602,4.777965],[-5.685852,-3.034016],[-4.027938,9.130618],[3.399571,-0.609567],[-8.264063,5.298583],[-6.042201,6.209621],[-5.672004,5.561380],[-2.772697,5.268896],[-1.686038,3.282885],[-8.999198,-1.151290],[5.331222,-8.655531],[-6.642879,5.615859],[4.117656,8.120364],[-1.296967,-7.495894],[7.834058,-4.078923],[-5.461841,-0.428150],[-4.195341,-1.316270],[5.685470,7.167666],[-2.521644,5.323938],[9.743930,-0.835575],[1.381612,-5.978009],[-9.220478,-3.043369],[-9.968747,-5.682552],[-5.728703,9.193691],[-6.649794,7.608212],[-6.925672,-7.070982],[-0.607212,-7.218900],[-9.452320,-8.430872],[-1.180893,7.340551],[-4.705087,-1.738945],[5.509950,1.743121],[-5.798662,-8.738564],[-6.856179,-7.390379],[1.442065,-1.921879],[2.328235,8.237389],[3.087818,9.504600],[-3.170798,-8.341561],[6.767029,7.418188],[0.823832,-7.646805],[7.274438,-9.457794],[0.035588,-9.344005],[1.137460,-7.221295],[4.035821,1.181453],[-8.515596,2.494544],[3.977358,4.415678],[-4.931713,8.596372],[6.505649,6.404841],[9.204211,8.849901],[8.903043,2.701682],[-6.157173,8.769179],[0.832761,-3.058166],[6.994057,-9.429176],[7.547610,1.518363],[-6.727957,-2.668741],[4.598561,-8.337296],[2.540110,1.298736],[2.188640,-3.199113],[-4.258308,-2.511660],[-8.324092,6.570003],[-3.713430,-1.830493],[6.643456,3.113946],[6.117176,-6.323239],[-5.323835,0.341187],[-9.140979,-0.072860],[9.533272,2.477203],[-4.535798,9.052822],[-8.614473,-1.828852],[-5.141218,-9.814057],[2.469825,9.629866],[9.861000,0.594313],[-6.598490,-1.745095],[8.239858,-3.105694],[2.424456,-9.512079],[0.225408,-3.247229],[4.889180,-6.202723],[2.016381,7.256404],[7.710302,7.911634],[-4.293396,-5.119845],[2.322387,8.059396],[5.443955,6.137500],[5.374019,-1.259250],[0.362443,-6.532433],[9.654387,-0.871821],[-6.152868,6.699149],[-0.648550,-6.113008],[6.786328,4.260309],[3.694086,5.279412],[2.287314,9.619050],[5.826528,5.805703],[-1.737888,5.907613],[3.660289,4.951786],[5.766629,4.584851],[0.623723,2.096606],[-6.995722,-5.982641],[7.419934,-9.441027],[-5.624342,-9.632338],[6.386361,4.870985],[3.414640,5.069816],[-8.647575,-7.624230],[-4.540562,-7.370963],[-4.160291,-0.677235],[-6.195136,-2.164334],[3.605946,-8.584675],[8.215552,0.274620],[1.230732,-8.606824],[5.682215,2.651752],[-0.883172,0.925874],[7.574825,7.759792],[3.460143,-0.533146],[-7.512552,-3.119269],[1.262470,5.370783],[1.527812,5.186056],[0.036167,7.977037],[8.705830,4.248629],[1.360162,-9.877636],[-3.995051,-8.398502],[-1.190846,6.990198],[1.496472,-2.062503],[8.725424,4.058430],[-7.810190,5.878896],[4.931838,-5.817205],[9.534394,-5.585818],[-8.643085,3.761694],[-0.010228,8.291044],[-5.617104,8.000975],[-6.098629,-8.155298],[-8.125259,-8.961446],[-2.781311,-4.383659],[-9.924447,-6.444700],[-7.576354,-3.171601],[-1.879700,2.770329],[4.079956,3.153179],[-6.946515,-3.514451],[-4.122935,-4.250739],[-3.421608,5.910636],[-1.627468,-0.558516],[-8.038706,-6.014984],[-9.174061,5.691450],[-4.793620,5.538582],[6.927999,8.704357],[-7.377363,-7.138985],[-9.221555,4.234833],[8.124797,4.795352],[-1.364790,9.890002],[-9.112311,-1.447514],[-1.181264,4.262690],[-1.048422,6.985126],[7.787157,0.042197],[-2.641441,-4.214258],[-3.122420,7.629607],[-3.667898,0.760205],[8.456124,0.975649],[-3.247383,-1.674501],[-1.016534,5.965451],[-3.567596,-5.592273],[7.189083,2.311257],[-8.670345,-7.824159],[3.268815,-0.745679],[-7.450430,7.666832],[-5.213438,-5.129803],[-6.222794,-5.185379],[-6.095531,5.092546],[-7.562187,7.458694],[-3.393267,0.614620],[-2.073574,7.755285],[2.165086,-6.542847],[-7.152312,9.855623],[-7.043728,5.987391],[-9.736835,4.082462],[-8.416927,-4.138912],[1.391808,-1.929841],[-2.789720,-0.550178],[-2.157616,1.102806],[7.190572,0.171114],[6.700226,9.567136],[-2.959072,-1.311130],[-5.138932,-1.957110],[-5.632799,9.611152],[-1.036221,7.720936],[8.629028,0.137828],[-3.395873,6.236173],[-4.668215,9.914040],[-1.596925,-9.378919],[5.290078,2.486846],[-4.579583,-6.705538],[-3.342770,-8.964490],[-0.905735,-8.713102],[2.228934,5.690349],[-7.806893,-6.726056],[6.294190,-6.857715],[-1.095046,3.119685],[6.970065,0.186020],[-6.149940,-4.072647],[6.689210,4.647842],[7.920491,0.880194],[3.450537,-1.218732],[9.433947,6.453060],[-5.466662,-0.451034],[-9.023898,-9.908303],[1.008589,8.767770],[-2.246981,-3.277733],[8.759704,6.948915],[5.952225,0.476826],[6.424714,-9.360822],[-5.768846,0.769691],[0.607907,4.052901],[5.449980,4.172922],[3.983158,-5.196046],[9.463067,3.658184],[-2.449656,8.224439],[5.877581,7.727177],[-1.987477,-5.398822],[8.255377,8.102153],[3.990837,-8.370699],[-7.993455,0.951965],[-2.768383,2.185315],[0.576097,-2.539232],[9.268090,9.241067],[5.510709,4.681554],[0.677110,-7.756147],[-6.040985,1.427413],[8.831961,-7.835479],[-6.250261,9.868266],[-7.109822,-0.680501],[-1.569261,3.508533],[-7.360778,-6.914791],[6.368893,0.193977],[2.364223,6.815035],[6.179134,-2.716112],[-4.794568,-9.595268],[-7.488284,-7.062014],[8.055648,-7.532880],[8.393690,0.211065],[3.240943,2.165483],[-6.350635,8.718388],[6.723464,8.293414],[2.293177,5.501868],[-8.143372,-0.609083],[5.634815,6.546666],[3.774551,-8.989430],[-4.938677,-8.004739],[-0.991335,-7.060556]], dtype = "float64")#candidate|4525|(616, 2)|const|float64
call_4524 = relay.TupleGetItem(func_2984_call(relay.reshape(const_4525.astype('float64'), [1232,])), 0)
call_4526 = relay.TupleGetItem(func_2986_call(relay.reshape(const_4525.astype('float64'), [1232,])), 0)
func_3648_call = mod.get_global_var('func_3648')
func_3653_call = mutated_mod.get_global_var('func_3653')
var_4537 = relay.var("var_4537", dtype = "uint64", shape = ())#candidate|4537|()|var|uint64
const_4538 = relay.const([7.961883,-2.830148,1.215008,1.895228,9.072342,-6.126397,-7.469104,-1.044171,5.440384,-9.597535,1.288061,-8.088522,-5.669123,-4.282611,9.297649,-0.772483,0.648408,-0.229031,2.309146,-5.941457,-4.889116,4.262066,-0.773845,-0.588393,7.049518,-4.330484,-9.747582,0.615452,6.804058,-6.657433,-6.931433,-4.475629,6.722372,-4.835328,-1.477575,8.608874,-7.910577,2.809197,-0.495710,-0.225148,-6.622896,-5.362292,9.139289,6.293592,-0.078574,6.868749,-2.010126,-0.317908,-9.733408,1.969865,1.392944,-3.574964,5.222384,-5.009759,0.133276,3.923954,3.668330,-5.763731,-9.034492,-5.505559,2.554051,8.991530,8.299776,6.068717,-9.842727,-5.235199,-5.151798,6.846144,-9.303286,4.657581,-7.085859,4.698379,3.197151,-8.132181,6.150089,-5.007350,-8.443817,0.777642,3.005114,-4.967220,4.879774,2.648405,5.155736,9.993948,6.855984,5.570651,-7.995748,1.286769,4.367988,4.354792,-5.447807,8.076729,1.910532,-9.448141,-4.717213,-5.091489,5.090996,2.124007,3.621330,-1.209565,2.499171,-9.066920,-9.786726,1.981494,-3.587328,7.686562,-2.750608,2.180134,5.384311,-2.349857,-8.570718,6.500967,5.061013,-2.991325,9.833767,2.043524,0.304959,-6.547044,4.718558,6.141180,-0.689659,2.222747,7.786732,-6.196506,-8.820496,-5.003154,-7.633564,4.478147,-2.008548,-3.431183,-5.761960,4.166067,3.537759,-9.833622,0.063589,-8.956661,-3.119225,4.764517,6.368122,-4.015991,-5.658838,-2.254830,-3.208149,-6.360623,-1.532868,-5.028137,-2.886958,-8.270846,-7.982820,6.566969,-8.969222,3.995913,7.130289,-3.893188,3.861872,-9.110244,-3.076946,-6.875929,-7.040114,2.561119,4.586401,-2.919133,2.036244,4.232791,5.679121,-4.647007,5.792191,-6.923740,-3.788372,8.366389,6.529182,5.030386,-7.416146,-5.022703,6.336979,2.907652,4.275909,-1.284107,-1.311994,-6.357172,-0.546130,9.232345,7.935590,-2.132724,5.623239,6.825459,-9.279945,-3.792399,-4.630067,2.513959,-7.171024,-3.293589,-9.187475,3.273965,-9.460851,-5.161566,-2.650304,-8.996553,4.952634,0.460465,-8.434594,9.722676,4.540960,-6.561077,-8.620449,3.438424,-7.963439,9.503845,7.095832,-6.815109,-5.162517,-1.108948,-7.933811,-2.040279,-9.390019,-7.713266,-8.026610,1.508810,2.114022,5.130636,9.294355,3.180432,-6.537406,2.007868,3.227636,-2.147428,-6.859769,-6.768526,0.191405,7.285541,-7.602509,2.765168,8.285022,-9.838831,-6.896080,2.301407,5.609206,1.290892,1.824131,8.955127,-1.310352,-4.458722,-8.927887,-3.048743,-7.016210,6.821846,6.978111,4.513477,9.106488,-0.002133,-9.009593,-1.714582,-0.812068,6.070751,-8.883846,-9.078464,-0.066675,0.114620,3.286036,7.874631,4.823088,-0.597720,6.933159,-6.036148,5.823904,-0.311373,-0.769267,0.560021,-5.280657,-8.316258,2.391555,-3.616928,5.282048,9.974523,2.703336,-5.926692,7.857412,8.900512,6.851700,-7.130023,-7.207356,-2.424327,1.388520,4.890827,-7.902958,-8.875838,-5.590472,-4.139115,-9.269967,-7.505739,-2.033056,6.299122,5.454801,-3.343441,-4.989189,-1.469293,9.476695,6.702514,-1.919843,-3.355227,-3.163296,9.948429,2.325491,-6.928296,2.469729,8.617330,-4.750013,8.677382,-6.186541,-0.928785,-0.762575,6.358178,5.846404,-8.477732,-1.787179,-7.448736,5.887205,0.767039,7.466564,5.825504,8.913523,-5.257375,0.300845,4.575246,7.135529,-8.518216,-2.255285,0.572968,-3.901749,-4.402740,8.488035,8.816242,-0.793873,7.993552,-9.687572,-6.159409,-9.904027,6.481346,-8.026970,1.821117,-1.459009,-8.850422,1.869780,-4.533106,0.387104,-8.458711,-2.450056,-0.497869,5.990278,-1.021442,-7.426160,2.374252,-4.339021,-3.477806,6.093616,-2.672067,0.918765,3.570830,0.024295,-8.077537,-4.792239,1.894578,-1.534504,6.632735,8.157566,8.199557,-7.607469,-5.236111,-0.079759,1.206350,-9.451514,1.115402,-4.105118,1.070800,1.278260,7.772338,-8.626972,-7.581586,-5.859852,-6.452722,9.796527,9.598630,-4.275768,-8.450655,-6.830924,3.527559,-2.600108,-9.503349,3.384747,-5.825303,8.663355,-4.189046,-9.424416,-1.460279,-2.622621,-2.847031,-6.653694,4.819548,-4.906289,2.157974,9.405490,6.292282,-2.047821,1.482015,4.488354,-8.740779,3.365395,9.244490,7.610231,-4.728004,-9.212854,5.554472,-9.411710,-1.906969,7.467482,1.755644,-3.288079,-9.821352,-6.019551,-1.875379,0.776959,-9.108491,0.157781,-2.794568,8.340833,-4.808805,8.055088,-0.750062,-8.427280,-4.611063,9.269791,-8.248706,1.354811,-7.354986,-8.704222,1.800172,3.505254,-6.495061,3.723239,8.324727,5.817405,1.908332,3.672184,-2.194100,-3.854436,8.288820,-8.981283,3.239125,-7.102023,3.184357,-5.088910,-1.925626,-5.921306,-2.821193,9.129099,-6.099495,8.489084,-1.588441,-1.493743,-5.688374,1.411655,-9.232803,0.487622,8.945439,5.421177,9.503615,-8.807805,1.527371,-1.883857,-9.697757,7.692925,5.695059,-8.352004,7.910582,-0.095569,4.268563,-7.538284,-0.360304,2.285871,5.385870,-4.411775,-9.578605,8.362329,-2.746623,8.377323,8.536088,7.423912,8.313119,-7.962692,-4.953785,-0.928630,7.908632,9.175568,6.848921,4.529096,2.389772,9.035094,-6.786475,9.546442,-5.431707,-4.310790,5.453832,-3.842700,9.008197,-3.934760,-6.680936,-6.020351,9.968388,2.804323,-4.095650,3.358275,-6.534219,-6.221211,3.387991,2.942498,-4.939556,-4.446211,-4.034351,7.684412,6.021813,7.087737,-2.549728,5.755544,-7.100161,-7.537526,-5.254105,-2.006950,-3.009725,8.326578,0.844735,-9.978916,-1.793413,0.902292,0.349746,6.283058,-2.207654,-4.441654,-7.810822,-6.822920,-6.986045,0.629000,0.983694,-3.059528,-6.505666,0.090385,-0.670190,-1.911314,-1.453896,1.267365,-2.652558,8.456496,-2.651366,6.034272,4.579937,8.115248,2.346501,-1.599521,-3.044381,-3.079224,5.234062,-3.781042,9.113847,-6.043388,0.028322,-3.383240,-8.045969,-1.238486,7.973097,0.105469,-8.991061,5.851233,-5.230191,-3.631061,-1.677111,6.445702,-6.757603,9.485991,-1.077844,-3.500644,-0.039322,4.061903,-2.085236,1.701428,-7.833095,-9.359135,0.356369,-0.707383,-7.035506,-1.454846,6.817148,-0.200898,-0.312301,-1.082268,1.124529,-2.782980,6.404036,9.085537,5.587299,3.381682,2.430310,-9.444801,3.433603,-0.988024,5.161698,-6.437387,1.894113,2.307544,3.953641,-8.290305,-3.887298,-1.849603,1.371252,2.506567,-1.352909,-9.729267,-3.089019,-9.581325,7.364553,9.333252,1.267000,4.547731,-5.531221,-5.722438,-1.617330,2.315586,1.691775,-7.794805,3.799725,-2.198406,7.979845,5.961394,6.412949,5.121968,4.024515,-2.071965,1.760593,5.533223,-1.963225,6.609616,-1.323957,8.495727,-3.044280,-0.409891,5.406569,6.261911,7.308210,-6.944862,-0.429216,1.920170,5.164071,-3.657774,-1.977632,-4.853300,-8.887324,0.367718,-0.685210,-2.670749,4.159691,-0.670393,2.842871,5.139297,1.926609,-7.236893,1.745366,3.462003,4.614066,7.224793,2.121956,-5.705359,8.298377,-0.293038,-0.506758,-0.612597,-5.608897,-6.593209,-4.860221,-7.257968,3.055916,4.843197,4.586824,4.016038,2.413915,-6.994155,4.326204,-8.868058,-8.535855,-2.952849,1.604117,-4.245300,-3.674386,-6.272651,-5.864599,-2.578112,0.209324,1.338499,-9.793116,3.144749,5.284061,-7.577182,-9.208367,-0.484839,6.794170,8.721040,8.977346,-5.617188,-4.232977,0.311073,-5.197704,-6.219903,4.959615,-9.404061,3.639748,8.681037,2.818143,6.240680,-3.999410,-1.772048,-2.763371,6.442121,-6.283189], dtype = "float32")#candidate|4538|(720,)|const|float32
call_4536 = relay.TupleGetItem(func_3648_call(relay.reshape(const_4525.astype('int32'), [1232,]), relay.reshape(var_4537.astype('uint64'), []), relay.reshape(const_4538.astype('float32'), [720,]), ), 1)
call_4539 = relay.TupleGetItem(func_3653_call(relay.reshape(const_4525.astype('int32'), [1232,]), relay.reshape(var_4537.astype('uint64'), []), relay.reshape(const_4538.astype('float32'), [720,]), ), 1)
output = relay.Tuple([call_4521,call_4524,const_4525,call_4536,var_4537,const_4538,])
output2 = relay.Tuple([call_4522,call_4526,const_4525,call_4539,var_4537,const_4538,])
func_4559 = relay.Function([var_4537,], output)
mod['func_4559'] = func_4559
mod = relay.transform.InferType()(mod)
var_4560 = relay.var("var_4560", dtype = "uint64", shape = ())#candidate|4560|()|var|uint64
output = func_4559(var_4560)
func_4561 = relay.Function([var_4560], output)
mutated_mod['func_4561'] = func_4561
mutated_mod = relay.transform.InferType()(mutated_mod)
func_426_call = mod.get_global_var('func_426')
func_427_call = mutated_mod.get_global_var('func_427')
call_4603 = relay.TupleGetItem(func_426_call(), 0)
call_4604 = relay.TupleGetItem(func_427_call(), 0)
output = relay.Tuple([call_4603,])
output2 = relay.Tuple([call_4604,])
func_4622 = relay.Function([], output)
mod['func_4622'] = func_4622
mod = relay.transform.InferType()(mod)
output = func_4622()
func_4623 = relay.Function([], output)
mutated_mod['func_4623'] = func_4623
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2249_call = mod.get_global_var('func_2249')
func_2251_call = mutated_mod.get_global_var('func_2251')
call_4654 = relay.TupleGetItem(func_2249_call(), 0)
call_4655 = relay.TupleGetItem(func_2251_call(), 0)
func_2516_call = mod.get_global_var('func_2516')
func_2518_call = mutated_mod.get_global_var('func_2518')
call_4673 = relay.TupleGetItem(func_2516_call(), 1)
call_4674 = relay.TupleGetItem(func_2518_call(), 1)
output = relay.Tuple([call_4654,call_4673,])
output2 = relay.Tuple([call_4655,call_4674,])
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
func_426_call = mod.get_global_var('func_426')
func_427_call = mutated_mod.get_global_var('func_427')
call_4689 = relay.TupleGetItem(func_426_call(), 0)
call_4690 = relay.TupleGetItem(func_427_call(), 0)
uop_4704 = relay.cosh(call_4689.astype('float32')) # shape=(11, 14, 8)
uop_4706 = relay.cosh(call_4690.astype('float32')) # shape=(11, 14, 8)
func_910_call = mod.get_global_var('func_910')
func_913_call = mutated_mod.get_global_var('func_913')
const_4717 = relay.const([[-6,3,1,2],[10,1,10,8],[-7,1,-5,7],[-6,-3,-6,-5],[1,-4,-5,-10],[2,7,-7,10],[-9,-4,-7,-4],[-1,7,2,-10],[3,7,8,-3],[1,4,4,6],[5,8,2,-7],[9,-10,8,-5],[-4,9,2,-2],[-3,-4,2,-2],[9,-3,4,-6],[5,-5,8,6],[-4,3,8,-2],[-4,7,4,5],[9,-6,7,7],[10,5,-4,1],[7,-6,9,-5],[4,-1,1,-4],[3,5,-4,3],[2,3,10,-6],[7,-3,9,9],[2,-4,5,7],[-9,-9,-3,-8],[-2,-3,-4,1],[-2,-10,-4,6],[1,3,9,-6],[-10,-1,7,8],[-2,-2,-1,-10],[9,5,8,-9],[1,-5,-2,9],[5,-5,-1,4],[5,2,10,10],[-1,-1,4,8],[-4,8,-5,7],[8,2,4,-5],[-1,6,6,-9],[9,-7,-1,-2],[9,2,8,-4],[1,8,-2,-4],[-9,-6,-6,-3],[6,10,7,4],[-4,2,6,-8],[1,-2,-10,-8],[9,-5,1,-2],[8,-4,-5,-2],[9,-1,-9,-3],[7,-5,-4,-6],[-9,7,-9,-6],[-2,3,-3,6],[-1,6,-4,-2],[4,7,-2,-10],[2,-2,-8,-9],[3,8,6,-7],[-9,-7,-1,5],[8,-3,5,-3],[3,-9,8,-1],[-7,-4,-3,2],[-5,6,-9,1],[-2,-10,-10,-3],[2,5,-9,8],[7,3,-4,-3],[-5,5,7,3],[-2,6,8,6],[1,-8,10,-8],[-2,9,5,5],[1,6,-7,7],[4,1,5,1],[-9,-6,-7,-7],[5,-6,-10,-8],[2,8,5,-9],[1,10,-7,9],[2,-6,2,-7],[-1,-5,6,9],[9,7,3,2],[8,-9,5,-1],[-5,-5,10,4],[-6,2,6,10],[-9,1,5,-5],[7,7,3,-8],[-5,-5,-4,-8],[-2,2,2,-3],[-9,2,-10,-6],[-2,-1,-1,3],[-2,2,-9,-6],[-3,-9,10,-3],[-10,4,3,-9],[1,9,-10,7],[-1,10,1,3],[6,-8,-7,9],[7,9,1,4],[9,3,8,-3],[-1,10,-9,-8],[8,3,-9,3],[4,-6,10,-1],[5,-10,6,-1],[6,-2,6,-2],[-8,-10,-7,-2],[4,8,-8,-3],[-2,6,-8,-6],[-8,-1,-8,9],[-6,-2,-9,-6],[2,7,4,5],[-6,-6,5,9],[10,-8,-1,-6],[-5,3,-5,-8],[-2,9,6,-4],[4,-7,3,4],[7,4,10,-6],[10,-10,-8,-4],[-3,8,8,2],[-3,-10,-6,-10],[6,-1,-3,9],[8,-8,8,-9],[-6,10,1,3],[2,2,6,3],[5,-6,2,-10],[7,-7,10,5],[4,-8,-9,1],[-4,1,5,2],[7,6,7,8],[-6,10,2,1],[-1,3,2,1],[-8,-10,6,3],[-1,-3,-9,-4],[-7,-10,-8,-6],[-2,10,4,-3],[-6,7,4,7],[3,6,10,-6],[4,7,6,2],[-4,-3,-4,3],[9,3,-2,-1],[-8,-6,6,-7],[-7,-2,-8,3],[7,-2,-4,2],[-7,-9,5,7],[-6,4,-6,-2],[-3,-7,1,5],[-8,8,4,-7],[4,3,5,-5],[-4,3,-7,-2],[-1,3,1,-1],[-7,-2,10,-3],[5,-6,-7,-9],[7,8,1,4],[10,-6,-5,1],[6,10,-3,10],[10,-8,4,-7],[-3,5,-4,-6],[4,7,-8,1],[2,-10,6,-2],[-6,5,-10,-3],[7,7,-6,-8],[-2,2,-1,-4],[6,-7,5,-1],[2,3,8,6],[-5,-7,-3,-5],[-7,-7,-2,1],[-6,-10,-10,2],[-7,-3,-2,-8],[-10,-9,-7,-10],[-3,-5,9,-3],[-4,7,-6,-5],[5,-7,7,-5],[-10,3,-1,4]], dtype = "uint32")#candidate|4717|(168, 4)|const|uint32
call_4716 = relay.TupleGetItem(func_910_call(relay.reshape(const_4717.astype('uint32'), [8, 12, 7]), relay.reshape(const_4717.astype('uint32'), [8, 12, 7]), ), 0)
call_4718 = relay.TupleGetItem(func_913_call(relay.reshape(const_4717.astype('uint32'), [8, 12, 7]), relay.reshape(const_4717.astype('uint32'), [8, 12, 7]), ), 0)
output = relay.Tuple([uop_4704,call_4716,const_4717,])
output2 = relay.Tuple([uop_4706,call_4718,const_4717,])
func_4721 = relay.Function([], output)
mod['func_4721'] = func_4721
mod = relay.transform.InferType()(mod)
mutated_mod['func_4721'] = func_4721
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4721_call = mutated_mod.get_global_var('func_4721')
call_4722 = func_4721_call()
output = call_4722
func_4723 = relay.Function([], output)
mutated_mod['func_4723'] = func_4723
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3469_call = mod.get_global_var('func_3469')
func_3471_call = mutated_mod.get_global_var('func_3471')
call_4728 = relay.TupleGetItem(func_3469_call(), 1)
call_4729 = relay.TupleGetItem(func_3471_call(), 1)
output = relay.Tuple([call_4728,])
output2 = relay.Tuple([call_4729,])
func_4732 = relay.Function([], output)
mod['func_4732'] = func_4732
mod = relay.transform.InferType()(mod)
mutated_mod['func_4732'] = func_4732
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4732_call = mutated_mod.get_global_var('func_4732')
call_4733 = func_4732_call()
output = call_4733
func_4734 = relay.Function([], output)
mutated_mod['func_4734'] = func_4734
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4683_call = mod.get_global_var('func_4683')
func_4685_call = mutated_mod.get_global_var('func_4685')
call_4780 = relay.TupleGetItem(func_4683_call(), 1)
call_4781 = relay.TupleGetItem(func_4685_call(), 1)
output = call_4780
output2 = call_4781
func_4785 = relay.Function([], output)
mod['func_4785'] = func_4785
mod = relay.transform.InferType()(mod)
output = func_4785()
func_4786 = relay.Function([], output)
mutated_mod['func_4786'] = func_4786
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4836 = relay.var("var_4836", dtype = "float64", shape = (4, 15, 9))#candidate|4836|(4, 15, 9)|var|float64
var_4837 = relay.var("var_4837", dtype = "float64", shape = (4, 15, 9))#candidate|4837|(4, 15, 9)|var|float64
bop_4838 = relay.mod(var_4836.astype('float64'), relay.reshape(var_4837.astype('float64'), relay.shape_of(var_4836))) # shape=(4, 15, 9)
output = bop_4838
output2 = bop_4838
func_4845 = relay.Function([var_4836,var_4837,], output)
mod['func_4845'] = func_4845
mod = relay.transform.InferType()(mod)
mutated_mod['func_4845'] = func_4845
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4845_call = mutated_mod.get_global_var('func_4845')
var_4847 = relay.var("var_4847", dtype = "float64", shape = (4, 15, 9))#candidate|4847|(4, 15, 9)|var|float64
var_4848 = relay.var("var_4848", dtype = "float64", shape = (4, 15, 9))#candidate|4848|(4, 15, 9)|var|float64
call_4846 = func_4845_call(var_4847,var_4848,)
output = call_4846
func_4849 = relay.Function([var_4847,var_4848,], output)
mutated_mod['func_4849'] = func_4849
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4457_call = mod.get_global_var('func_4457')
func_4459_call = mutated_mod.get_global_var('func_4459')
call_4858 = relay.TupleGetItem(func_4457_call(), 0)
call_4859 = relay.TupleGetItem(func_4459_call(), 0)
func_1560_call = mod.get_global_var('func_1560')
func_1562_call = mutated_mod.get_global_var('func_1562')
call_4872 = relay.TupleGetItem(func_1560_call(), 0)
call_4873 = relay.TupleGetItem(func_1562_call(), 0)
func_1330_call = mod.get_global_var('func_1330')
func_1332_call = mutated_mod.get_global_var('func_1332')
call_4889 = func_1330_call()
call_4890 = func_1330_call()
output = relay.Tuple([call_4858,call_4872,call_4889,])
output2 = relay.Tuple([call_4859,call_4873,call_4890,])
func_4899 = relay.Function([], output)
mod['func_4899'] = func_4899
mod = relay.transform.InferType()(mod)
output = func_4899()
func_4900 = relay.Function([], output)
mutated_mod['func_4900'] = func_4900
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1302_call = mod.get_global_var('func_1302')
func_1304_call = mutated_mod.get_global_var('func_1304')
call_4943 = relay.TupleGetItem(func_1302_call(), 0)
call_4944 = relay.TupleGetItem(func_1304_call(), 0)
func_2516_call = mod.get_global_var('func_2516')
func_2518_call = mutated_mod.get_global_var('func_2518')
call_4945 = relay.TupleGetItem(func_2516_call(), 3)
call_4946 = relay.TupleGetItem(func_2518_call(), 3)
var_4962 = relay.var("var_4962", dtype = "uint32", shape = (672,))#candidate|4962|(672,)|var|uint32
bop_4963 = relay.logical_or(call_4945.astype('bool'), relay.reshape(var_4962.astype('bool'), relay.shape_of(call_4945))) # shape=(672,)
bop_4966 = relay.logical_or(call_4946.astype('bool'), relay.reshape(var_4962.astype('bool'), relay.shape_of(call_4946))) # shape=(672,)
output = relay.Tuple([call_4943,bop_4963,])
output2 = relay.Tuple([call_4944,bop_4966,])
func_4969 = relay.Function([var_4962,], output)
mod['func_4969'] = func_4969
mod = relay.transform.InferType()(mod)
mutated_mod['func_4969'] = func_4969
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4970 = relay.var("var_4970", dtype = "uint32", shape = (672,))#candidate|4970|(672,)|var|uint32
func_4969_call = mutated_mod.get_global_var('func_4969')
call_4971 = func_4969_call(var_4970)
output = call_4971
func_4972 = relay.Function([var_4970], output)
mutated_mod['func_4972'] = func_4972
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2516_call = mod.get_global_var('func_2516')
func_2518_call = mutated_mod.get_global_var('func_2518')
call_4996 = relay.TupleGetItem(func_2516_call(), 3)
call_4997 = relay.TupleGetItem(func_2518_call(), 3)
output = call_4996
output2 = call_4997
func_5006 = relay.Function([], output)
mod['func_5006'] = func_5006
mod = relay.transform.InferType()(mod)
output = func_5006()
func_5007 = relay.Function([], output)
mutated_mod['func_5007'] = func_5007
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1302_call = mod.get_global_var('func_1302')
func_1304_call = mutated_mod.get_global_var('func_1304')
call_5022 = relay.TupleGetItem(func_1302_call(), 0)
call_5023 = relay.TupleGetItem(func_1304_call(), 0)
output = call_5022
output2 = call_5023
func_5034 = relay.Function([], output)
mod['func_5034'] = func_5034
mod = relay.transform.InferType()(mod)
mutated_mod['func_5034'] = func_5034
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5034_call = mutated_mod.get_global_var('func_5034')
call_5035 = func_5034_call()
output = call_5035
func_5036 = relay.Function([], output)
mutated_mod['func_5036'] = func_5036
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4457_call = mod.get_global_var('func_4457')
func_4459_call = mutated_mod.get_global_var('func_4459')
call_5090 = relay.TupleGetItem(func_4457_call(), 0)
call_5091 = relay.TupleGetItem(func_4459_call(), 0)
output = relay.Tuple([call_5090,])
output2 = relay.Tuple([call_5091,])
func_5110 = relay.Function([], output)
mod['func_5110'] = func_5110
mod = relay.transform.InferType()(mod)
output = func_5110()
func_5111 = relay.Function([], output)
mutated_mod['func_5111'] = func_5111
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2673_call = mod.get_global_var('func_2673')
func_2674_call = mutated_mod.get_global_var('func_2674')
call_5121 = relay.TupleGetItem(func_2673_call(), 0)
call_5122 = relay.TupleGetItem(func_2674_call(), 0)
var_5123 = relay.var("var_5123", dtype = "int32", shape = (11, 14, 8))#candidate|5123|(11, 14, 8)|var|int32
bop_5124 = relay.subtract(call_5121.astype('int16'), relay.reshape(var_5123.astype('int16'), relay.shape_of(call_5121))) # shape=(11, 14, 8)
bop_5127 = relay.subtract(call_5122.astype('int16'), relay.reshape(var_5123.astype('int16'), relay.shape_of(call_5122))) # shape=(11, 14, 8)
uop_5132 = relay.atanh(bop_5124.astype('float64')) # shape=(11, 14, 8)
uop_5134 = relay.atanh(bop_5127.astype('float64')) # shape=(11, 14, 8)
func_4010_call = mod.get_global_var('func_4010')
func_4011_call = mutated_mod.get_global_var('func_4011')
call_5137 = func_4010_call()
call_5138 = func_4010_call()
func_1809_call = mod.get_global_var('func_1809')
func_1813_call = mutated_mod.get_global_var('func_1813')
const_5165 = relay.const([9,-3,3,-6,5,8,-3,-10,-6,-4,3,-2,5,-6,-1,6,-2,6,-2,2,8,-1,-8,5,1,5,-7,6,-10,-8,-9,4,3,7,-2,5,10,10,9,1,7,6,4,7,6,8,2,-7,10,2,-4,2,3,1,7,1,-10,7,-1,-8,10,6,-8,6,-6,1,-5,3,3,9,-6,4,-1,7,-5,-1,-3,-6,-10,8,-3,8,-2,-6,-3,-6,9,-2,-3,2,-6,-5,-10,9,-5,7,-5,-6,6,-1,10,7,-7,10,9,-10,-5,-5,7,-6,-2,2,8,6,3,2,-5,1,-9,4,2,-5,10,-3,-6,1,4,7,3,-7,-1,8,-9,9,-1,-5,8,2,-2,5,8,7,-7,-5,8,-5,-10,-6,-3,6,-2,8,3,-8,-9,-4,-6,10,-7,-4,-6,5,-3,6,10,1,-2,-1,-3,1,-9,10,6,-9,-4,10,-3,7,-8,3,4,9,4,-3,7,8,9,-1,7,-9,-4,-10,-6,2,-9,-3,8,-9,1,9,5,6,-7,-10,7,-5,8,8,2,9,5,-4,-3,-7,-4,2,8,-5,5,9,-5,-2,2,9,2,-7,10,-3,-4,-7,9,-10,-7,1,-8,-3,9,-6,-9,-6,2,9,-7,-5,3,1,-9,-10,-6,8,3,7,-1,4,-9,-1,6,-5,10,-3,-9,-6,7,-7,-7,7,10,-4,8,-9,8,9,7,8,1,-2,-8,-1,2,-6,-6,-9,-8,5,10,-4,-3,-4,-7,2,4,10,-2,-6,2,-5,6,3,8,-1,-4,-7,-8,-1,-3,-4,-7,-8,-7,5,-8,-6,-6,-2,8,3,6,1,10,10,-5,10,-9,10,7,-3,-8,1,7,6,-7,-7,8,-9,-2,-4,3,8,4,-6,-5,-6,-8,-5,-2,-2,10,4,-9,-8,1,-5,-6,8,3,3,-5,-1,7,9,10,10,1,10,6,9,10,4,9,5,8,-9,8,7,9,7,-7,1,-1,-6,-9,-4,10,-4,-10,10,9,-10,-3,-2,-10,4,-6,-5,-4,-1,9,1,-3,-8,-5,10,10,-9,-6,-7,-2,6,-4,4,-4,-10,-10,10,-7,6,-9,-4,-6,-1,-7,-1,-7,-4,5,-8,3,-2,10,-8,-2,-7,-3,-9,-7,3,9,1,-8,9,-5,4,7,-10,-10,4,-5,3,5,6], dtype = "int16")#candidate|5165|(450,)|const|int16
call_5164 = func_1809_call(relay.reshape(const_5165.astype('int16'), [2, 15, 15]), relay.reshape(const_5165.astype('int16'), [2, 15, 15]), )
call_5166 = func_1809_call(relay.reshape(const_5165.astype('int16'), [2, 15, 15]), relay.reshape(const_5165.astype('int16'), [2, 15, 15]), )
func_4457_call = mod.get_global_var('func_4457')
func_4459_call = mutated_mod.get_global_var('func_4459')
call_5189 = relay.TupleGetItem(func_4457_call(), 0)
call_5190 = relay.TupleGetItem(func_4459_call(), 0)
output = relay.Tuple([uop_5132,call_5137,call_5164,const_5165,call_5189,])
output2 = relay.Tuple([uop_5134,call_5138,call_5166,const_5165,call_5190,])
func_5192 = relay.Function([var_5123,], output)
mod['func_5192'] = func_5192
mod = relay.transform.InferType()(mod)
var_5193 = relay.var("var_5193", dtype = "int32", shape = (11, 14, 8))#candidate|5193|(11, 14, 8)|var|int32
output = func_5192(var_5193)
func_5194 = relay.Function([var_5193], output)
mutated_mod['func_5194'] = func_5194
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3107_call = mod.get_global_var('func_3107')
func_3109_call = mutated_mod.get_global_var('func_3109')
call_5219 = relay.TupleGetItem(func_3107_call(), 1)
call_5220 = relay.TupleGetItem(func_3109_call(), 1)
output = relay.Tuple([call_5219,])
output2 = relay.Tuple([call_5220,])
func_5223 = relay.Function([], output)
mod['func_5223'] = func_5223
mod = relay.transform.InferType()(mod)
output = func_5223()
func_5224 = relay.Function([], output)
mutated_mod['func_5224'] = func_5224
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4785_call = mod.get_global_var('func_4785')
func_4786_call = mutated_mod.get_global_var('func_4786')
call_5231 = func_4785_call()
call_5232 = func_4785_call()
output = relay.Tuple([call_5231,])
output2 = relay.Tuple([call_5232,])
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
func_1965_call = mod.get_global_var('func_1965')
func_1966_call = mutated_mod.get_global_var('func_1966')
call_5252 = relay.TupleGetItem(func_1965_call(), 0)
call_5253 = relay.TupleGetItem(func_1966_call(), 0)
output = call_5252
output2 = call_5253
func_5261 = relay.Function([], output)
mod['func_5261'] = func_5261
mod = relay.transform.InferType()(mod)
mutated_mod['func_5261'] = func_5261
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5261_call = mutated_mod.get_global_var('func_5261')
call_5262 = func_5261_call()
output = call_5262
func_5263 = relay.Function([], output)
mutated_mod['func_5263'] = func_5263
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2475_call = mod.get_global_var('func_2475')
func_2477_call = mutated_mod.get_global_var('func_2477')
call_5305 = relay.TupleGetItem(func_2475_call(), 0)
call_5306 = relay.TupleGetItem(func_2477_call(), 0)
func_2591_call = mod.get_global_var('func_2591')
func_2593_call = mutated_mod.get_global_var('func_2593')
var_5320 = relay.var("var_5320", dtype = "uint32", shape = (672,))#candidate|5320|(672,)|var|uint32
call_5319 = relay.TupleGetItem(func_2591_call(relay.reshape(var_5320.astype('uint32'), [672,])), 0)
call_5321 = relay.TupleGetItem(func_2593_call(relay.reshape(var_5320.astype('uint32'), [672,])), 0)
output = relay.Tuple([call_5305,call_5319,var_5320,])
output2 = relay.Tuple([call_5306,call_5321,var_5320,])
func_5332 = relay.Function([var_5320,], output)
mod['func_5332'] = func_5332
mod = relay.transform.InferType()(mod)
mutated_mod['func_5332'] = func_5332
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5333 = relay.var("var_5333", dtype = "uint32", shape = (672,))#candidate|5333|(672,)|var|uint32
func_5332_call = mutated_mod.get_global_var('func_5332')
call_5334 = func_5332_call(var_5333)
output = call_5334
func_5335 = relay.Function([var_5333], output)
mutated_mod['func_5335'] = func_5335
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2289_call = mod.get_global_var('func_2289')
func_2291_call = mutated_mod.get_global_var('func_2291')
call_5390 = func_2289_call()
call_5391 = func_2289_call()
func_1965_call = mod.get_global_var('func_1965')
func_1966_call = mutated_mod.get_global_var('func_1966')
call_5407 = relay.TupleGetItem(func_1965_call(), 0)
call_5408 = relay.TupleGetItem(func_1966_call(), 0)
output = relay.Tuple([call_5390,call_5407,])
output2 = relay.Tuple([call_5391,call_5408,])
func_5421 = relay.Function([], output)
mod['func_5421'] = func_5421
mod = relay.transform.InferType()(mod)
output = func_5421()
func_5422 = relay.Function([], output)
mutated_mod['func_5422'] = func_5422
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4721_call = mod.get_global_var('func_4721')
func_4723_call = mutated_mod.get_global_var('func_4723')
call_5423 = relay.TupleGetItem(func_4721_call(), 2)
call_5424 = relay.TupleGetItem(func_4723_call(), 2)
func_2673_call = mod.get_global_var('func_2673')
func_2674_call = mutated_mod.get_global_var('func_2674')
call_5441 = relay.TupleGetItem(func_2673_call(), 0)
call_5442 = relay.TupleGetItem(func_2674_call(), 0)
func_3870_call = mod.get_global_var('func_3870')
func_3873_call = mutated_mod.get_global_var('func_3873')
var_5453 = relay.var("var_5453", dtype = "uint64", shape = (252,))#candidate|5453|(252,)|var|uint64
call_5452 = relay.TupleGetItem(func_3870_call(relay.reshape(var_5453.astype('uint64'), [252,])), 11)
call_5454 = relay.TupleGetItem(func_3873_call(relay.reshape(var_5453.astype('uint64'), [252,])), 11)
func_983_call = mod.get_global_var('func_983')
func_985_call = mutated_mod.get_global_var('func_985')
var_5472 = relay.var("var_5472", dtype = "uint16", shape = (1120,))#candidate|5472|(1120,)|var|uint16
call_5471 = relay.TupleGetItem(func_983_call(relay.reshape(var_5472.astype('uint16'), [10, 16, 7])), 0)
call_5473 = relay.TupleGetItem(func_985_call(relay.reshape(var_5472.astype('uint16'), [10, 16, 7])), 0)
output = relay.Tuple([call_5423,call_5441,call_5452,var_5453,call_5471,var_5472,])
output2 = relay.Tuple([call_5424,call_5442,call_5454,var_5453,call_5473,var_5472,])
func_5474 = relay.Function([var_5453,var_5472,], output)
mod['func_5474'] = func_5474
mod = relay.transform.InferType()(mod)
var_5475 = relay.var("var_5475", dtype = "uint64", shape = (252,))#candidate|5475|(252,)|var|uint64
var_5476 = relay.var("var_5476", dtype = "uint16", shape = (1120,))#candidate|5476|(1120,)|var|uint16
output = func_5474(var_5475,var_5476,)
func_5477 = relay.Function([var_5475,var_5476,], output)
mutated_mod['func_5477'] = func_5477
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2516_call = mod.get_global_var('func_2516')
func_2518_call = mutated_mod.get_global_var('func_2518')
call_5516 = relay.TupleGetItem(func_2516_call(), 0)
call_5517 = relay.TupleGetItem(func_2518_call(), 0)
var_5520 = relay.var("var_5520", dtype = "float64", shape = (11, 14, 8))#candidate|5520|(11, 14, 8)|var|float64
bop_5521 = relay.bitwise_or(call_5516.astype('uint8'), relay.reshape(var_5520.astype('uint8'), relay.shape_of(call_5516))) # shape=(11, 14, 8)
bop_5524 = relay.bitwise_or(call_5517.astype('uint8'), relay.reshape(var_5520.astype('uint8'), relay.shape_of(call_5517))) # shape=(11, 14, 8)
output = bop_5521
output2 = bop_5524
func_5526 = relay.Function([var_5520,], output)
mod['func_5526'] = func_5526
mod = relay.transform.InferType()(mod)
var_5527 = relay.var("var_5527", dtype = "float64", shape = (11, 14, 8))#candidate|5527|(11, 14, 8)|var|float64
output = func_5526(var_5527)
func_5528 = relay.Function([var_5527], output)
mutated_mod['func_5528'] = func_5528
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2516_call = mod.get_global_var('func_2516')
func_2518_call = mutated_mod.get_global_var('func_2518')
call_5554 = relay.TupleGetItem(func_2516_call(), 3)
call_5555 = relay.TupleGetItem(func_2518_call(), 3)
output = relay.Tuple([call_5554,])
output2 = relay.Tuple([call_5555,])
func_5561 = relay.Function([], output)
mod['func_5561'] = func_5561
mod = relay.transform.InferType()(mod)
mutated_mod['func_5561'] = func_5561
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5561_call = mutated_mod.get_global_var('func_5561')
call_5562 = func_5561_call()
output = call_5562
func_5563 = relay.Function([], output)
mutated_mod['func_5563'] = func_5563
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2249_call = mod.get_global_var('func_2249')
func_2251_call = mutated_mod.get_global_var('func_2251')
call_5605 = relay.TupleGetItem(func_2249_call(), 0)
call_5606 = relay.TupleGetItem(func_2251_call(), 0)
func_589_call = mod.get_global_var('func_589')
func_592_call = mutated_mod.get_global_var('func_592')
var_5616 = relay.var("var_5616", dtype = "uint64", shape = ())#candidate|5616|()|var|uint64
const_5617 = relay.const([-7,-3,8,10,8,-2,10,4,-8,7,10,7,10,5,6,8,-3,-6,-6,10,6,5,-4,7,3,-1,-7,-8,-2,-10,1,2,10,2,6,10,-7,-7,3,4,7,8,-8,1,-9,8,1,-3,-8,7,-8,6,-1,6,-9,9,-10,10,-3,-7,3,4,5,-7,2,-7,-2,-6,7,8,-6,2,5,-3,-4,-3,-8,-5,2,-6,-7,-7,-7,5,-8,-2,1,10,7,-4,-6,9,2,4,5,2,-4,-4,-3,9,-1,4,4,-10,7,-1,1,-6,-4,-8,-2,-3,-9,-9,6,-4,6,1,-1,-2,-4,-3,3,-7,10,5,6,-8,5,-7,-5,7,8,3,10,-10,-8,-9,-10,7,-2,2,8,-4,9,-3,-4,-6,-10,-4,6,-5,8,-5,-10,10,3,-9,4,-6,-7,-5,-1,5,-2,2,-4,-10,10,-1,-8,-2,3,-3,-7,9,-8,-6,5,-10,2,-5,-8,-7,2,9,-8,-10,4,-9,-2,6,-3,9,-4,7,3,-2,-8,-1,8,-10,-3,-9,-4,8,9,6,-6,1,5,6,9,1,9,-10,4,-5,-10,3,-5,8,5,-5,10,-3,-4,-3,8,-2,5,-4,-2,7,-3,4,3,3,7,-1,4,1,10,2,-7,-5,-6,3,-7,-10,1,10], dtype = "uint64")#candidate|5617|(252,)|const|uint64
call_5615 = relay.TupleGetItem(func_589_call(relay.reshape(var_5616.astype('uint64'), []), relay.reshape(const_5617.astype('uint64'), [252,]), ), 2)
call_5618 = relay.TupleGetItem(func_592_call(relay.reshape(var_5616.astype('uint64'), []), relay.reshape(const_5617.astype('uint64'), [252,]), ), 2)
func_3933_call = mod.get_global_var('func_3933')
func_3934_call = mutated_mod.get_global_var('func_3934')
call_5620 = relay.TupleGetItem(func_3933_call(), 0)
call_5621 = relay.TupleGetItem(func_3934_call(), 0)
output = relay.Tuple([call_5605,call_5615,var_5616,const_5617,call_5620,])
output2 = relay.Tuple([call_5606,call_5618,var_5616,const_5617,call_5621,])
func_5623 = relay.Function([var_5616,], output)
mod['func_5623'] = func_5623
mod = relay.transform.InferType()(mod)
var_5624 = relay.var("var_5624", dtype = "uint64", shape = ())#candidate|5624|()|var|uint64
output = func_5623(var_5624)
func_5625 = relay.Function([var_5624], output)
mutated_mod['func_5625'] = func_5625
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5561_call = mod.get_global_var('func_5561')
func_5563_call = mutated_mod.get_global_var('func_5563')
call_5671 = relay.TupleGetItem(func_5561_call(), 0)
call_5672 = relay.TupleGetItem(func_5563_call(), 0)
output = relay.Tuple([call_5671,])
output2 = relay.Tuple([call_5672,])
func_5693 = relay.Function([], output)
mod['func_5693'] = func_5693
mod = relay.transform.InferType()(mod)
mutated_mod['func_5693'] = func_5693
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5693_call = mutated_mod.get_global_var('func_5693')
call_5694 = func_5693_call()
output = call_5694
func_5695 = relay.Function([], output)
mutated_mod['func_5695'] = func_5695
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5421_call = mod.get_global_var('func_5421')
func_5422_call = mutated_mod.get_global_var('func_5422')
call_5712 = relay.TupleGetItem(func_5421_call(), 0)
call_5713 = relay.TupleGetItem(func_5422_call(), 0)
const_5718 = relay.const([[[8,-6,-10,6,6,-6,-4,5],[3,9,-6,1,2,-3,-3,-2],[4,2,10,2,10,10,-2,-5],[10,10,4,-1,3,5,-2,7],[-6,10,6,1,1,9,8,-8],[-9,4,10,-10,-9,9,1,-7],[-4,2,-10,8,-4,-7,-9,1],[-5,-1,-10,8,-5,1,2,4],[5,-7,-7,-8,-10,-3,10,-8],[9,-10,2,8,-6,5,7,5],[3,8,-7,-3,1,-7,-10,-6],[6,-5,7,-6,-2,-10,-10,10],[-8,-5,7,3,2,9,-7,-10],[-2,-1,-10,-9,-8,1,5,-1]],[[-2,-10,-4,6,-3,9,-7,-2],[6,7,8,10,6,-6,-5,-8],[5,5,-10,-7,-4,-2,-7,-2],[-6,9,-7,-2,10,-8,6,1],[3,-3,7,-4,8,5,-10,8],[-8,-2,8,1,-1,-3,4,-8],[-2,-10,1,-1,1,4,-3,-7],[-9,-7,2,-5,7,-2,3,-10],[1,3,7,2,-8,-9,-7,1],[7,5,5,4,9,5,-6,-9],[8,-2,4,2,8,-2,-10,-5],[2,-8,-1,9,10,3,2,6],[4,2,2,9,-5,-7,5,-4],[1,3,6,-3,9,-4,-8,10]],[[8,9,6,-10,-10,-8,10,-1],[5,4,-8,-10,4,8,4,-3],[8,10,9,-6,10,3,7,-2],[10,6,4,-2,1,10,8,8],[5,-1,-10,5,-5,10,4,6],[10,9,9,-10,-3,-6,4,-6],[-3,-5,-6,-3,-1,-4,-4,7],[2,8,1,-4,8,5,5,5],[2,1,2,-10,-8,6,-3,-6],[2,10,1,10,-7,5,8,-10],[-10,10,-6,3,-3,5,-5,-4],[-4,10,10,7,7,-9,-10,5],[3,-1,6,-2,4,-6,10,-6],[6,-4,-8,-4,-2,9,-6,-3]],[[-2,8,8,-8,1,1,-5,8],[5,-8,2,9,6,10,-4,3],[-9,5,-2,2,-8,5,-2,-3],[-6,1,2,5,-7,2,-10,-1],[-5,-10,1,10,-7,-1,9,-7],[4,2,7,3,-2,9,-7,3],[-7,9,-7,7,4,-4,-3,-8],[10,-2,5,4,10,9,4,-9],[7,10,9,-9,-7,-5,-3,-9],[3,1,-7,-5,-6,6,10,-2],[-5,10,-10,-6,1,1,-6,-8],[-2,-7,2,5,10,-8,7,7],[2,6,8,1,3,5,2,8],[-2,2,9,-2,1,9,-1,9]],[[-4,7,7,3,-2,1,2,8],[4,-6,7,4,-9,5,-7,-5],[-1,5,10,10,-6,4,2,-10],[1,-1,-5,6,8,-3,-8,-8],[-1,-7,-2,-1,-9,4,8,-8],[-9,7,6,7,-5,-8,1,1],[10,-2,-6,9,-9,-7,-7,4],[-5,-10,-6,-4,-1,3,-8,-3],[4,-1,8,4,-2,-2,7,5],[-9,-5,-5,-6,-1,6,5,10],[-5,-10,8,10,-6,-9,10,-6],[-2,-6,10,-1,2,2,1,9],[-2,10,-2,2,-3,-10,6,6],[7,-2,5,-7,5,8,-3,1]],[[-5,-7,-9,4,1,-9,-10,-2],[-8,-3,10,-1,3,-10,-6,6],[-9,-8,-4,-4,-6,10,7,-6],[-8,7,-1,4,8,4,2,3],[3,-4,4,1,-1,10,5,-3],[5,1,-2,1,9,-4,-3,4],[10,2,4,-8,4,-2,-3,2],[-9,-3,-7,3,-10,-7,-5,1],[-9,-3,-8,-9,-6,1,-10,-7],[-5,-1,5,-10,-10,9,10,-5],[5,-5,7,-3,-8,2,9,-8],[10,-9,-3,1,6,1,2,-6],[-3,7,-6,3,-7,2,4,2],[-1,-10,-10,10,-3,-3,-8,-1]],[[1,-9,8,-10,6,-3,-2,-8],[-6,7,-1,1,1,-10,-6,-10],[-7,-3,-10,2,-5,-10,-9,-1],[-7,8,-7,-4,6,7,-5,6],[-5,-8,2,-5,-6,5,3,10],[-6,2,1,4,-1,7,8,-9],[4,10,-9,6,-9,-1,-9,-4],[9,-2,3,-8,-9,-10,10,-9],[-7,4,-3,-1,3,5,-3,7],[-9,2,5,6,-5,-10,-8,-1],[10,-2,8,-5,5,1,3,10],[8,-3,2,-8,6,3,-9,-10],[2,1,-5,-10,-10,-10,10,-4],[4,3,7,-6,-1,8,5,-10]],[[9,-8,-10,7,-9,5,-9,-10],[-8,-2,6,9,-8,9,8,10],[-1,-4,-5,2,-9,3,-6,4],[6,1,5,1,-1,-7,-2,-6],[3,5,-2,4,-4,3,10,5],[5,-1,-8,-4,-5,-5,7,-1],[1,10,2,7,3,-9,-7,-10],[-10,3,-5,6,9,8,-3,6],[-4,-1,10,-4,8,-5,-8,7],[8,-8,8,-5,-5,1,-2,6],[-3,2,-3,-8,10,5,-2,7],[-4,-5,9,1,4,4,1,2],[6,-9,2,1,-3,-9,-1,-5],[1,1,-9,-4,4,-7,-9,-9]],[[6,-4,-5,10,3,3,4,-3],[7,5,-4,-6,-6,-3,5,9],[-10,-8,10,-5,5,-9,5,6],[-5,5,-9,-10,-6,-1,7,-10],[3,-1,6,-7,1,4,9,-7],[10,-6,5,-7,10,-1,7,3],[-9,-4,10,8,7,-7,-1,-3],[-8,-1,6,3,-5,5,6,-2],[2,-4,7,-4,-3,3,7,4],[-4,10,4,-7,10,8,10,4],[6,-6,7,7,3,3,-5,-7],[5,-8,1,-5,9,-8,3,-3],[-8,-10,-9,7,7,1,-1,1],[-6,-3,6,9,-1,-6,-8,3]],[[-10,-3,10,-10,-1,10,-1,-6],[-4,5,6,7,2,-2,-4,6],[-10,2,6,8,5,9,-1,-3],[3,4,4,9,-7,-6,-7,-5],[-9,6,3,3,4,-3,7,1],[-6,1,8,-7,10,6,-4,-4],[-1,10,-6,1,-7,6,-2,3],[-4,9,-4,-9,-10,2,9,6],[-4,-2,-1,10,-7,1,-5,-9],[-9,-3,5,-7,-10,-8,5,-8],[2,1,3,9,-10,-1,-5,4],[-1,8,2,10,6,-10,3,10],[-8,-9,4,2,8,-7,-6,-10],[-9,-2,6,2,3,3,-9,-1]],[[5,7,10,1,5,-3,-2,-7],[-1,-1,-2,-9,4,10,8,-8],[3,-2,7,1,3,2,-6,6],[7,-6,-2,-3,-8,10,6,9],[-5,2,-6,3,-8,-7,-3,6],[2,-8,-7,-1,-6,1,10,1],[2,-9,-10,-8,-7,-7,-7,10],[-2,-2,-1,-4,-5,-1,6,10],[7,6,4,-8,-6,3,7,-1],[-4,-8,9,4,-10,8,-6,3],[10,3,-3,4,5,3,1,-2],[8,-9,-3,-10,5,10,6,7],[3,9,10,-5,9,8,1,-4],[-10,-7,-6,-8,5,-4,-1,9]]], dtype = "int32")#candidate|5718|(11, 14, 8)|const|int32
bop_5719 = relay.floor_divide(call_5712.astype('float64'), relay.reshape(const_5718.astype('float64'), relay.shape_of(call_5712))) # shape=(11, 14, 8)
bop_5722 = relay.floor_divide(call_5713.astype('float64'), relay.reshape(const_5718.astype('float64'), relay.shape_of(call_5713))) # shape=(11, 14, 8)
output = bop_5719
output2 = bop_5722
func_5733 = relay.Function([], output)
mod['func_5733'] = func_5733
mod = relay.transform.InferType()(mod)
output = func_5733()
func_5734 = relay.Function([], output)
mutated_mod['func_5734'] = func_5734
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3469_call = mod.get_global_var('func_3469')
func_3471_call = mutated_mod.get_global_var('func_3471')
call_5818 = relay.TupleGetItem(func_3469_call(), 2)
call_5819 = relay.TupleGetItem(func_3471_call(), 2)
func_4365_call = mod.get_global_var('func_4365')
func_4367_call = mutated_mod.get_global_var('func_4367')
call_5829 = relay.TupleGetItem(func_4365_call(), 1)
call_5830 = relay.TupleGetItem(func_4367_call(), 1)
bop_5835 = relay.greater(call_5818.astype('bool'), relay.reshape(call_5829.astype('bool'), relay.shape_of(call_5818))) # shape=(11, 14, 8)
bop_5838 = relay.greater(call_5819.astype('bool'), relay.reshape(call_5830.astype('bool'), relay.shape_of(call_5819))) # shape=(11, 14, 8)
uop_5843 = relay.sigmoid(bop_5835.astype('float32')) # shape=(11, 14, 8)
uop_5845 = relay.sigmoid(bop_5838.astype('float32')) # shape=(11, 14, 8)
func_3694_call = mod.get_global_var('func_3694')
func_3697_call = mutated_mod.get_global_var('func_3697')
const_5863 = relay.const([True,True,True,True,True,True,True,True,True,False,True,False,True,True,False,True,False,True,False,False,False,False,True,False,True,True,False,True,False,False,True,True,False,False,True,True,False,False,False,True,False,True,False,False,True,False,True,True,True,True,True,False,True,False,False,False,True,False,True,False,True,False,True,True,True,False,False,True,False,True,False,True,False,False,True,True,True,False,False,False,True,False,False,False,False,True,False,False,True,False,False,False,False,True,True,True,False,False,False,False,True,True,True,True,True,False,True,False,False,True,True,True,True,True,True,False,False,False,False,False,False,False,False,False,True,False,False,True,False,False,False,True,True,True,False,True,False,True,True,False,True,False,False,False,False,True,False,False,True,False,False,True,False,True,False,False,True,False,True,True,False,True,False,False,True,False,True,True,False,False,True,True,True,True,True,True,True,False,True,False,False,False,False,True,True,False,True,False,False,False,True,False,False,True,False,True,True,True,False,True,False,True,False,True,True,False,False,False,False,True,False,False,True,False,True,False,False,False,False,False,True,True,True,True,False,True,False,False,True,False,True,True,True,False,False,False,False,False,False,False,True,True,False,True,True,False,True,False,False,False,False,True,True,True,False,False,True,False,False,False,False,True,True,False,True,True,False,True,True,True,True,False,False,False,True,True,False,True,True,False,True,False,False,False,True,False,False,False,True,False,False,True,False,True,True,True,False,False,True,True,True,False,False,True,False,True,False,False,False,False,True,True,False,True,False,True,True,False,False,False,True,False,False,True,False,True,False,False,True,True,False,False,False,False,True,False,True,False,True,False,False,False,True,False,True,True,True,False,False,True,True,True,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,True,True,False,False,True,True,True,True,True,False,False,True,True,False,True,True,False,True,True,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,True,True,True,False,False,True,False,True,False,False,False,False,False,False,True,True,False,True,True,False,True,False,True,True,True,True,True,True,True,True,True,False,True,True,False,True,False,False,True,True,False,True,True,True,True,False,False,True,False,True,False,True,False,True,True,True,False,False,False,False,False,True,False,True,False,True,False,True,True,True,False,False,True,True,True,False,True,True,False,True,False,False,True,False,True,False,True,True,False,True,True,False,True,False,True,True,True,False,False,False,True,False,False,False,True,True,True,True,False,True,False,True,True,True,True,False,True,True,True,False,False,True,False,True,True,False,True,False,False,True,False,True,False,True,False,True,False,True,False,True,False,True,False,True,False,True,True,False,False,False,False,True,True,False,False,False,False,True,False,False,True,True,False,True,False,False,False,False,True,True,True,True,False,True,False,False,True,True,False,True,True,False,False,True,True,True,True,True,False,False,False,True,True,False,False,True,False,True,True,True,False,True,False,False,False,False,False,True,True,True,True,False,True,True,True,False,False,True,False,True,True,False,False,False,False,True,True,False,False,False,True,False,True,True,False,False,True,False,True,False,True,False,False,True,False,False,True,False,True,True,True,False,True,False,False,True,True,True,True,True,True,False,True,True,True,True,True,False,True,False,False,True,True,True,False,True,True,True,True,False,True,True,False,False,True,False,False,False,True,True,True,False,False,False,True,True,True,False,False,False,True,False,True,False,True,True,True,False,True,False,False,False,True,False,False,False,False,False,False,True,False,True,False,False,True,True,True,False,False,True,True,True,False,False,True,True,False,False,False,True,False,False,True,False,True,True,False,True,False,True,True,False,False,True,False,False,False,True,False,False,True,True,True,True,False,False,False,False,False,False,True,True,True,False,True,False,True,True,True,True,False,False,True,True,True,True,True,False,True,True,False,False,True,False,True,True,False,True,True,True,False,False,False,True,False,True,True,True,False,False,True,True,True,False,False,False,False,True,False,True,False,True,True,True,True,False,False,True,True,True,False,True,True,False,False,True,True,True,True,False,False,False,True,True,False,True,True,False,False,False,True,False,True,False,False,False,False,False,True,False,False,False,True,True,False,False,True,False,True,False,False,True,False,True,False,False,False,False,True,False,False,False,False,True,True,False,True,True,True,False,True,True,False,True,False,True,True,True,True,False,True,True,False,True,False,False,False,False,False,True,False,False,True,False,True,False,True,False,False,False,True,True,True,True,False,True,False,True,True,True,False,False,False,False,False,False,False,False,False,True,True,False,True,False,True,True,True,False,True,True,False,False,False,True,False,True,False,False,False,True,False,False,False,False,False,False,True,True,False,True,False,True,False,True,True,True,False,False,True,False,True,True,False,False,False,False,True,False,True,True,False,True,False,False,True,False,False,False,True,False,False,True,True,False,True,False,True,True,True,False,True,False,True,False,False,True,False,True,True,True,True,True,False,True,True,False,True,True,False,True,True,False,False,False,False,True,True,True,True,False,True,False,False,False,False,True,True,True,False,True,False,True,False,True,False,False,True,False,True,True,True,True,False,True,True,False,True,False,False,False,False,True,False,True,False,True,False,True,False,False,False,False,False,True,True,False,True,False,False,False,False,True,True,False,True,True,False,False,True,False,False,False,False,False,True,False,True,True,True,True,True,False,False,True,True,True,False,False,False,False,False,False,False,False,False,True,True,False,True,False,True,True,False,True,True,True,True,True,False,False,False,False,False,False,True,True,False,True,True,False,False,False,False,False,False,False,True,True,False,False,True,True,True,False,False,False,True,True,True,False,False,False,False,False,False,True,False,False,True,True,False,True,True,False,True,True,False,False,False,True,False,False,False,True,False,True,True,True,False,True,True,False,True,True,True,True,True,True,False,False,False,False,True,False,True,False,True,True,False,False,False,False,False,True,True,False,False,False,True,False,True,True,True,False,False,False,False,True,True,False,True,True,False,False,True,True,False,True,True,False,True,True,False,True,False,True,True,False,False,False,True,True,True,False,False,False,False,False,True,True,False,True,False,False,True,False,False,False,True,True,False,False,False,True,True,True,False,False,True,False,False,False,False,False,False,False,False,False,False,True,True,False,False,False,False,False,False,False,False,True,True,False,True,False,True,False,True,False,False,False,False,False,True,False,False,True,False,False,False,False,False,True,False,False,True,True,False,True,True,False,False,True,True,True,True,False,True,False,False,True,False,True,False,True,True,False,True,False,True,True,False,True,False,True,True,False,False,False,True,True,False,False,False,True,True,True,False,True,True,False,False,False,True,False,True,True,True,False,True,False,True,True,True,False,False,False,False,False,False,True,False,True,True,False,False,True,False,False,False,True,True,False,True,False,True,True,True,False,True,False,False,True,False,True,True,False,True,True,True,False,False,True,True,False,True,True,True,True,False,True,True,True,True,False,True,False,True,True,False,True,True,False,False,True,True,True,False,True,False,True,True,False,False,False,False,True,True,True,True,True,False,False,False,False,False,False,False,False,True,True,True,False,True,True,False,True,False,False,False,False,True,True,False,True,True,True,False,False,False,True,False,True,True,False,True,False,False,True,False,True,False,True,False,False,False,False,True,False,False,True,False,True,False,False,False,True,True,False,True,False,False,True,True,True,False,False,True,False,True,True,False,False,False,False,False,False,False,True,False,False,False,False,True,False,True,True,True,False,True,False,False,True,False,True,True,False,True,False,False,True,False,False,True,False,False,True,True,False,False,True,False,False,False,True,False,True,False,True,True,False,True,False,True,True,True,False,True,True,True,False,False,True,False,True,True,True,False,False,True,False,False,False,False,False,True,False,True,False,True,False,False,False,False,True,False,False,False,True,True,True,True,True,False,False,False,True,True,False,False,False,False,False,False,False,False,False,False,True,False,True,True,False,True,False,True,True,False,True,True,True,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,True,False,True,False,False,False,False,False,False,False,True,True,True,False,True,True,False,False,True,False,True,True,False,True,True,False,False,True,False,False,True,True,True,False,False,True,True,False,True,True,True,True,False,False,True,True,False,True,True,True,False,True,True,False,False,False,True,False,False,True,True,True,True,False,False,True,True,True,True,True,False,False,False,False,True,True,True,True,False], dtype = "bool")#candidate|5863|(1764,)|const|bool
call_5862 = relay.TupleGetItem(func_3694_call(relay.reshape(const_5863.astype('bool'), [14, 9, 14])), 2)
call_5864 = relay.TupleGetItem(func_3697_call(relay.reshape(const_5863.astype('bool'), [14, 9, 14])), 2)
bop_5869 = relay.floor_mod(bop_5835.astype('float64'), relay.reshape(uop_5843.astype('float64'), relay.shape_of(bop_5835))) # shape=(11, 14, 8)
bop_5872 = relay.floor_mod(bop_5838.astype('float64'), relay.reshape(uop_5845.astype('float64'), relay.shape_of(bop_5838))) # shape=(11, 14, 8)
output = relay.Tuple([call_5862,const_5863,bop_5869,])
output2 = relay.Tuple([call_5864,const_5863,bop_5872,])
func_5879 = relay.Function([], output)
mod['func_5879'] = func_5879
mod = relay.transform.InferType()(mod)
mutated_mod['func_5879'] = func_5879
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5879_call = mutated_mod.get_global_var('func_5879')
call_5880 = func_5879_call()
output = call_5880
func_5881 = relay.Function([], output)
mutated_mod['func_5881'] = func_5881
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5110_call = mod.get_global_var('func_5110')
func_5111_call = mutated_mod.get_global_var('func_5111')
call_5902 = relay.TupleGetItem(func_5110_call(), 0)
call_5903 = relay.TupleGetItem(func_5111_call(), 0)
func_3334_call = mod.get_global_var('func_3334')
func_3335_call = mutated_mod.get_global_var('func_3335')
call_5907 = relay.TupleGetItem(func_3334_call(), 0)
call_5908 = relay.TupleGetItem(func_3335_call(), 0)
func_2187_call = mod.get_global_var('func_2187')
func_2191_call = mutated_mod.get_global_var('func_2191')
call_5932 = relay.TupleGetItem(func_2187_call(relay.reshape(call_5907.astype('int32'), [11, 14, 8]), relay.reshape(call_5902.astype('uint64'), []), ), 0)
call_5933 = relay.TupleGetItem(func_2191_call(relay.reshape(call_5907.astype('int32'), [11, 14, 8]), relay.reshape(call_5902.astype('uint64'), []), ), 0)
output = relay.Tuple([call_5902,call_5907,call_5932,])
output2 = relay.Tuple([call_5903,call_5908,call_5933,])
func_5941 = relay.Function([], output)
mod['func_5941'] = func_5941
mod = relay.transform.InferType()(mod)
mutated_mod['func_5941'] = func_5941
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5941_call = mutated_mod.get_global_var('func_5941')
call_5942 = func_5941_call()
output = call_5942
func_5943 = relay.Function([], output)
mutated_mod['func_5943'] = func_5943
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5959 = relay.const([[[5.281537,2.943276,-9.820153,-8.469424,5.342269,-5.641259,-0.569121,2.906168,-1.835323,-3.038611,-6.844079,-4.193698,3.300655,2.063229,-4.604488,-9.660399]],[[7.398014,-1.598813,2.432803,9.793188,0.232864,3.249584,7.318038,-3.838665,-9.092849,-4.567466,7.442665,-9.307171,-9.892144,0.202954,-6.771422,-4.909616]],[[8.598935,-9.647871,2.686665,1.571473,9.852162,-1.614500,5.792358,-6.567636,0.447588,0.780463,7.432816,3.768145,7.420671,3.336231,-8.348693,7.143303]],[[-1.390552,-8.893926,-4.719792,-6.294133,-2.128612,-3.818266,-6.703243,-8.956765,6.779368,-8.982194,0.677206,-7.890050,-3.559822,-8.221936,9.706102,-9.303921]],[[1.037069,9.987290,-5.226885,-6.936581,-2.676189,2.969127,7.209585,-2.009454,0.673283,-5.629902,-0.753969,5.813553,-9.690253,4.955706,0.517085,2.278060]],[[-5.559315,-5.996666,6.292297,-0.745729,4.242704,-8.118615,3.697236,1.124343,8.356120,8.469886,-8.277159,9.405770,-8.263767,-3.711356,-6.946484,5.791047]],[[-7.565192,-5.842570,-0.790691,6.173753,-4.714162,-6.373623,-8.018818,-8.895895,3.726066,4.760254,-4.422906,-8.748937,9.369033,-7.002212,1.723399,0.781110]],[[-9.122459,6.064728,-3.870605,-2.101242,-3.767834,-3.704307,8.229668,-8.462013,-9.035933,-4.803190,-7.546985,9.078993,-0.402466,-5.022048,3.721123,5.094275]],[[6.095102,-7.371509,-6.056237,-2.878685,-9.268168,4.407466,4.903262,-1.589894,-5.124083,-9.976454,-7.989901,-8.341274,1.733445,-9.200389,-3.072430,-8.929804]],[[-1.119329,9.342986,-4.494800,8.024039,-7.942627,-4.737490,-1.344121,2.473557,0.356806,-8.853597,-8.239997,-2.872584,4.209473,-6.993795,7.698834,0.443834]],[[-2.207787,-3.455865,-7.524531,3.661085,-6.983032,-7.027441,-9.451740,8.569463,2.001899,5.738319,0.827474,4.525489,-8.553062,-1.726451,0.651419,5.069370]],[[4.435290,-2.174407,3.957853,-3.495259,2.927938,5.244632,0.052043,6.929151,-7.605727,-5.831575,1.767648,-8.045169,0.201563,9.089201,-9.064284,-3.855494]],[[-0.548763,0.092967,-2.863734,0.206724,-4.282221,-9.096302,-8.701710,-1.385164,-5.762895,-3.070540,-2.921449,-9.076227,8.784692,-3.447705,-7.465699,0.450608]],[[6.848132,1.902269,5.553509,7.327550,0.358230,8.303553,-7.688071,-5.699710,-3.428721,-2.688126,3.494398,-6.247581,-8.041416,-2.420711,-7.002186,5.140164]]], dtype = "float32")#candidate|5959|(14, 1, 16)|const|float32
const_5960 = relay.const([[[5.961873,2.717919,-3.002540,-3.941646,-4.701742,-3.219961,6.401279,4.400959,9.994596,-0.865149,5.264544,-8.531803,-6.147095,1.742320,-9.475353,-9.801961],[-4.455559,-5.018154,-1.072753,0.846541,4.803533,7.151854,-5.011942,4.416960,0.079867,4.121210,-1.917610,-9.795101,2.955186,9.420112,-1.929250,1.118359],[9.732538,-1.873806,5.751765,-6.999293,3.096576,2.620524,8.411055,1.802660,-9.698401,7.326804,-4.978519,-9.494043,7.605891,-5.556961,9.302863,-1.101672],[2.630650,7.368848,-3.168597,-5.926758,0.453461,5.565419,-9.488520,4.452197,1.188333,-7.661924,-6.415039,9.025808,-3.302092,-9.890163,-4.084248,9.870982]],[[1.211908,-9.747470,-4.066949,2.829140,-7.753750,-7.059337,8.236840,-0.235172,-4.098858,-7.295751,0.908042,4.478873,3.824687,4.423578,-9.207419,-9.636003],[2.380095,-7.919707,0.927933,-3.556406,-3.500136,-6.100071,-4.389951,0.444094,8.297666,-8.004890,1.980394,3.057424,4.533398,-7.563427,3.301115,8.213188],[7.869118,-4.456621,6.092862,4.819607,-2.189249,3.860252,-1.091786,1.750894,-6.660865,-2.190433,4.726483,5.359893,-2.254056,0.690369,-6.214080,4.505831],[-2.715074,-1.539358,-6.172639,2.316591,7.317448,9.308525,7.333013,-2.139682,-7.039508,-7.415065,-7.608274,-2.083467,9.223131,-6.852900,-1.602172,-1.157941]],[[8.154442,-4.334396,-4.554866,-8.230043,-4.566961,2.102017,1.216089,-6.553527,-2.046287,5.618566,-4.184311,8.458223,2.644245,7.991863,9.206686,-0.946221],[-1.271924,-0.965062,6.166681,-6.249317,6.353905,9.545582,4.509358,-9.795651,-2.343445,-4.586678,-8.915836,7.624185,4.504300,7.752363,-2.848137,-4.612431],[9.403333,6.381195,6.589873,-6.686557,9.544173,6.532080,0.432756,-6.537520,-9.249043,-1.053002,-5.095525,-8.019096,-5.685527,1.222209,-7.223602,6.714815],[-0.363374,-9.888933,1.614297,-9.318461,-7.790548,1.074100,-7.323416,-0.818531,2.672608,0.945544,-3.759451,1.084418,0.590540,8.180943,-3.397787,4.394543]],[[2.268783,7.480121,5.458453,1.927004,7.540718,1.555928,-0.237341,-4.132102,9.584098,5.059962,-0.797896,-2.443499,5.144882,3.774894,2.749507,0.093800],[-0.095595,7.821854,-9.811469,3.672569,0.014398,1.991181,-1.922661,9.305092,1.468876,7.887634,-0.450133,-1.444372,7.083969,6.805979,-5.490212,7.391464],[3.337989,-4.254587,8.618636,-6.729193,2.246259,-9.038210,8.377129,4.868341,0.989808,-4.989437,-5.851428,9.387696,-2.651675,-9.566147,8.545351,6.486948],[-0.083423,2.020075,-9.456234,5.991228,1.637513,0.846045,0.581075,-7.419346,-7.623137,-5.191962,2.083414,-6.092368,9.673306,-8.578870,7.577781,2.676067]],[[-6.408828,5.044115,-6.841710,-1.445263,0.503085,2.507267,-4.811661,4.025707,-4.267874,6.139412,8.284100,-3.724767,9.418303,-4.563252,-4.528540,-4.432577],[-8.738857,3.486841,-7.242970,-3.136678,-9.578315,4.066059,6.923302,9.800473,-1.733651,6.997342,-8.245245,-4.676639,9.236565,-9.276351,5.078978,-4.654690],[2.432559,-4.727529,8.780895,7.078713,-0.523511,-9.309830,6.158483,-7.254302,-8.833695,5.537832,4.302485,-1.623217,-2.798859,-4.087243,-2.610602,2.707034],[6.999643,8.657846,2.631095,-7.525355,4.798348,8.258447,-4.773257,4.164955,-0.558507,0.936583,-6.421058,-0.704229,9.062351,-8.850072,9.355912,9.001032]],[[-4.057415,5.766262,7.161187,5.813615,-5.245225,7.161222,-5.645342,6.729671,7.308510,-8.760202,5.713415,5.054041,-7.413245,-9.464972,9.395543,-1.082077],[-6.337854,9.442845,8.495769,6.224690,-4.350138,-5.527868,2.711368,6.278025,-5.707727,-6.999924,-4.050375,-0.903262,-2.069483,-6.364957,-2.988857,3.005382],[-7.941111,-9.573271,8.472398,9.374437,-2.778247,2.360466,6.103501,9.170077,-7.311647,2.454192,6.295609,0.700825,-7.118339,6.889106,-7.212897,-3.765504],[-1.162018,-1.719438,-2.617035,3.386380,6.491749,-4.970320,7.914896,5.885204,3.276283,-2.210589,-8.475217,-5.365479,1.883936,-7.559840,-9.776451,-4.460555]],[[0.150011,4.644339,-6.004341,8.613045,5.905244,-8.061468,8.562080,-9.552793,0.448037,6.847548,9.961031,-7.637897,8.052929,-3.737297,7.112069,-7.631503],[-2.607669,-4.075600,-4.672500,-3.777159,3.713347,-3.332737,-1.657837,-9.074019,3.409982,-9.978332,4.615482,9.192680,9.869144,2.466796,-8.783735,4.762147],[0.360773,5.027960,1.110131,4.724645,6.363769,4.213036,-1.889631,5.041679,5.310431,-9.872547,-7.425480,-5.421175,-0.604968,8.858091,7.003500,2.430587],[-4.604432,7.553644,-7.480105,6.330630,-1.852548,-6.625027,-8.408575,3.961011,7.303497,-9.967066,6.212957,0.004284,-1.879873,2.291349,6.440325,-5.332138]],[[7.088653,-3.960754,-4.543893,1.674518,-0.451434,-9.532376,1.476068,0.342393,9.525362,7.328440,-3.136411,-7.282738,3.982159,-1.233891,-9.635762,-9.676682],[-3.132816,-3.502005,-5.165621,-8.231542,7.496004,5.385922,-3.790857,4.017048,2.253319,-8.971359,4.430733,-2.760624,-8.764216,4.452606,-1.292739,8.424980],[-3.904985,2.654420,4.029104,-7.214412,-1.522112,-4.510061,-2.433004,8.648933,-1.040252,5.722413,-6.410148,-8.249142,-4.148918,-6.509200,1.089682,-0.552821],[7.348053,5.036060,5.492986,8.612169,7.531267,-9.104968,1.883671,7.971582,8.139074,4.072216,0.851684,3.105538,9.750327,-0.596924,7.635513,3.138636]],[[-3.358629,0.196746,-0.372483,-0.321728,-9.246883,7.384872,-5.370301,6.149000,4.360391,7.424483,-5.113549,-6.417643,-5.648646,4.878928,9.066566,-6.394558],[1.113109,2.312507,-9.209464,2.953088,-8.904904,-5.958533,-1.114433,9.868475,-3.133295,-6.714327,5.155624,9.769078,2.031024,9.436833,8.231324,-5.932432],[5.423111,-5.211219,7.740853,7.394606,-5.416411,-2.970115,2.743628,-9.550084,2.434583,6.591564,6.184002,-0.628387,3.543028,-4.802758,-6.292805,5.778942],[-4.422672,6.313036,6.510197,-4.531764,5.002376,-2.192869,-3.742329,-1.776740,3.000223,-1.445526,-2.203055,7.459695,-7.907380,-7.208460,8.797007,-2.419447]],[[1.966394,0.471403,-6.692224,-7.811360,1.321416,5.343972,3.540513,3.688315,3.250173,-1.235164,-9.830949,9.573939,4.420528,6.562986,8.160005,-8.363502],[-8.622440,8.464455,8.710374,-8.730188,7.209142,-1.218110,0.936006,1.705526,5.440129,4.062938,-2.890650,-1.592526,-8.156350,-1.780814,-3.385966,4.837961],[-8.715098,1.348335,-0.642513,-2.611514,2.342636,6.260404,-7.501704,1.949846,-0.953507,-9.921577,3.918794,-3.403695,-7.174641,0.859175,2.900038,9.738566],[-8.202014,-2.699899,-9.921383,-7.624494,3.991542,3.363696,-4.104056,-8.431243,8.352757,9.711066,4.271338,-7.550821,-6.583776,-2.093837,-2.900828,-9.479821]],[[7.509835,-8.189432,4.216789,0.661757,-8.014397,9.935469,-3.668069,7.512181,-1.195253,-1.139618,-6.640754,1.159336,7.362079,-2.757958,-8.313879,-6.885776],[8.577240,5.898412,5.176994,-0.127717,8.950537,-3.031450,0.812554,3.721144,2.602473,0.034380,0.629831,-0.729975,6.930406,-3.672405,6.004738,9.858898],[4.371299,-9.785727,5.997462,-8.735535,-1.548997,-7.516425,-6.874076,1.100809,-9.160324,9.371739,3.714555,-9.583561,2.658324,-3.658703,0.201111,9.892266],[9.473880,7.254670,-4.785831,5.842168,-3.321975,-4.973720,-4.873612,-0.223253,2.142350,-1.360222,-6.556143,8.222422,1.846888,-6.754488,3.567931,-0.295701]],[[4.198269,4.161700,9.993732,-4.250418,7.486952,7.451456,-5.490844,-7.895388,3.088822,1.862829,5.304074,5.289164,-6.748984,2.091875,-9.942071,-1.927900],[5.379682,0.600635,2.056394,-3.744668,6.281966,-7.991535,-9.201209,4.468792,7.057865,2.806806,9.365184,0.731279,-2.868191,9.331575,-6.082515,1.105278],[9.040563,5.406880,-9.009768,4.438381,1.413846,-2.776389,-1.896064,1.511757,-9.680432,-4.430088,-2.276699,7.036505,-8.944529,3.503913,6.476729,-4.058155],[1.373900,7.838448,-0.926507,0.195425,-3.520186,9.043304,1.336129,-1.656912,4.419914,4.282620,-0.915858,-4.399876,8.513432,-4.630507,-2.935168,-1.811864]],[[-2.269939,-0.613399,-7.004765,-0.747717,4.064761,-9.296131,-4.637674,-5.159577,1.206302,9.689645,-6.801715,0.215607,4.468459,-5.343546,-2.999274,-9.827944],[-2.416594,8.334023,-8.871292,5.721456,3.041326,2.022818,-0.017561,1.903609,1.472280,-3.450565,2.399807,-5.702749,1.122638,-2.842165,0.778493,-9.725014],[5.150388,-6.253484,1.201273,0.389362,2.097868,-4.393446,-6.517659,-3.106390,0.931635,-9.245123,-5.961955,3.964223,6.461338,4.348380,-5.076157,2.961578],[-4.345623,-7.046470,8.293197,-8.947194,-5.263564,5.771336,2.442421,-1.513460,-2.875603,8.995311,1.327954,-3.980734,-8.390198,9.031290,7.306629,7.125764]],[[6.384198,8.570971,0.451153,5.513029,-9.166782,1.490959,-9.274546,-3.188595,-4.064481,9.869026,6.163716,-4.171613,-5.213732,-1.187955,-4.041445,2.359173],[2.078582,0.337457,-2.302498,-6.917610,9.194620,-7.604626,-7.352543,-8.163853,-8.846114,-2.998155,0.766787,-2.100797,0.664281,8.495218,-0.590541,6.205771],[5.377457,-9.891253,7.271719,-4.745526,-4.279591,1.609980,-9.665044,2.673270,1.338446,-1.188855,3.727981,-1.435719,8.432574,-2.872691,-1.126143,-8.949358],[-8.147647,-9.453599,3.020219,-5.035937,9.368176,-2.288388,0.038149,0.011839,-1.969091,5.441401,-6.833412,-6.009217,0.024797,9.363109,-1.308162,8.153101]]], dtype = "float32")#candidate|5960|(14, 4, 16)|const|float32
bop_5961 = relay.power(const_5959.astype('float32'), const_5960.astype('float32')) # shape=(14, 4, 16)
output = bop_5961
output2 = bop_5961
func_5964 = relay.Function([], output)
mod['func_5964'] = func_5964
mod = relay.transform.InferType()(mod)
output = func_5964()
func_5965 = relay.Function([], output)
mutated_mod['func_5965'] = func_5965
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4683_call = mod.get_global_var('func_4683')
func_4685_call = mutated_mod.get_global_var('func_4685')
call_6022 = relay.TupleGetItem(func_4683_call(), 1)
call_6023 = relay.TupleGetItem(func_4685_call(), 1)
func_3107_call = mod.get_global_var('func_3107')
func_3109_call = mutated_mod.get_global_var('func_3109')
call_6031 = relay.TupleGetItem(func_3107_call(), 1)
call_6032 = relay.TupleGetItem(func_3109_call(), 1)
func_2984_call = mod.get_global_var('func_2984')
func_2986_call = mutated_mod.get_global_var('func_2986')
call_6041 = relay.TupleGetItem(func_2984_call(relay.reshape(call_6022.astype('float64'), [1232,])), 2)
call_6042 = relay.TupleGetItem(func_2986_call(relay.reshape(call_6022.astype('float64'), [1232,])), 2)
func_4732_call = mod.get_global_var('func_4732')
func_4734_call = mutated_mod.get_global_var('func_4734')
call_6048 = relay.TupleGetItem(func_4732_call(), 0)
call_6049 = relay.TupleGetItem(func_4734_call(), 0)
var_6065 = relay.var("var_6065", dtype = "uint64", shape = (7, 252))#candidate|6065|(7, 252)|var|uint64
bop_6066 = relay.greater(call_6041.astype('bool'), var_6065.astype('bool')) # shape=(7, 252)
bop_6069 = relay.greater(call_6042.astype('bool'), var_6065.astype('bool')) # shape=(7, 252)
output = relay.Tuple([call_6022,call_6031,call_6048,bop_6066,])
output2 = relay.Tuple([call_6023,call_6032,call_6049,bop_6069,])
func_6101 = relay.Function([var_6065,], output)
mod['func_6101'] = func_6101
mod = relay.transform.InferType()(mod)
var_6102 = relay.var("var_6102", dtype = "uint64", shape = (7, 252))#candidate|6102|(7, 252)|var|uint64
output = func_6101(var_6102)
func_6103 = relay.Function([var_6102], output)
mutated_mod['func_6103'] = func_6103
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6129 = relay.var("var_6129", dtype = "uint64", shape = ())#candidate|6129|()|var|uint64
var_6130 = relay.var("var_6130", dtype = "uint64", shape = (12, 1, 10))#candidate|6130|(12, 1, 10)|var|uint64
bop_6131 = relay.maximum(var_6129.astype('uint64'), var_6130.astype('uint64')) # shape=(12, 1, 10)
bop_6136 = relay.not_equal(var_6130.astype('bool'), var_6129.astype('bool')) # shape=(12, 1, 10)
output = relay.Tuple([bop_6131,bop_6136,])
output2 = relay.Tuple([bop_6131,bop_6136,])
F = relay.Function([var_6129,var_6130,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_6129,var_6130,], output2)
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
