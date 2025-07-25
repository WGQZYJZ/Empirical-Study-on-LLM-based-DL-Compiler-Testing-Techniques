import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_10 = relay.var("var_10", dtype = "float32", shape = (9, 13, 15))#candidate|10|(9, 13, 15)|var|float32
uop_11 = relay.tan(var_10.astype('float32')) # shape=(9, 13, 15)
output = relay.Tuple([uop_11,])
output2 = relay.Tuple([uop_11,])
func_22 = relay.Function([var_10,], output)
mod['func_22'] = func_22
mod = relay.transform.InferType()(mod)
mutated_mod['func_22'] = func_22
mutated_mod = relay.transform.InferType()(mutated_mod)
var_23 = relay.var("var_23", dtype = "float32", shape = (9, 13, 15))#candidate|23|(9, 13, 15)|var|float32
func_22_call = mutated_mod.get_global_var('func_22')
call_24 = func_22_call(var_23)
output = call_24
func_25 = relay.Function([var_23], output)
mutated_mod['func_25'] = func_25
mutated_mod = relay.transform.InferType()(mutated_mod)
const_277 = relay.const([[[-3,-6,4,-8,-1,-10,2,-4,8],[6,3,-4,-1,-3,-4,4,5,-8],[-10,-8,3,8,4,8,-7,-3,8],[-9,-6,9,1,7,3,-5,-2,-4],[10,2,-3,8,-5,-2,6,4,-6],[-2,-6,2,-6,2,1,3,-7,7],[-5,10,6,3,-3,-6,9,5,8]],[[-7,-4,10,-7,9,8,-4,1,-3],[7,-10,4,-9,-3,2,-2,8,10],[-1,3,-2,6,-3,1,-5,-3,-1],[1,2,4,7,-3,-2,-3,9,-3],[-6,-7,7,3,10,-4,-3,-3,-1],[8,-3,-3,3,9,1,-1,2,-3],[9,10,-4,-10,-1,3,-10,-8,-2]],[[-1,6,-7,2,3,7,5,-4,7],[9,-6,-10,10,9,-4,-10,6,-5],[-4,-2,-2,-5,-6,2,-8,1,-1],[10,-3,-1,2,2,-9,2,5,-2],[-2,6,7,-9,10,6,3,3,9],[-2,5,-10,2,-10,5,-6,9,2],[1,-1,-5,10,-5,1,5,4,7]],[[4,5,6,6,-4,3,4,-1,-3],[-2,-2,4,-2,7,10,-7,3,10],[1,-9,-4,-2,6,-1,-8,2,1],[-5,6,8,-8,-2,-6,-10,10,-1],[2,1,7,-7,-7,6,6,3,-3],[-7,6,2,4,9,1,-8,-3,3],[3,4,-10,9,2,-5,1,-8,5]]], dtype = "int32")#candidate|277|(4, 7, 9)|const|int32
var_278 = relay.var("var_278", dtype = "int32", shape = (4, 7, 9))#candidate|278|(4, 7, 9)|var|int32
bop_279 = relay.multiply(const_277.astype('int32'), relay.reshape(var_278.astype('int32'), relay.shape_of(const_277))) # shape=(4, 7, 9)
func_22_call = mod.get_global_var('func_22')
func_25_call = mutated_mod.get_global_var('func_25')
var_284 = relay.var("var_284", dtype = "float32", shape = (1755,))#candidate|284|(1755,)|var|float32
call_283 = relay.TupleGetItem(func_22_call(relay.reshape(var_284.astype('float32'), [9, 13, 15])), 0)
call_285 = relay.TupleGetItem(func_25_call(relay.reshape(var_284.astype('float32'), [9, 13, 15])), 0)
func_22_call = mod.get_global_var('func_22')
func_25_call = mutated_mod.get_global_var('func_25')
call_291 = relay.TupleGetItem(func_22_call(relay.reshape(var_284.astype('float32'), [9, 13, 15])), 0)
call_292 = relay.TupleGetItem(func_25_call(relay.reshape(var_284.astype('float32'), [9, 13, 15])), 0)
func_22_call = mod.get_global_var('func_22')
func_25_call = mutated_mod.get_global_var('func_25')
call_299 = relay.TupleGetItem(func_22_call(relay.reshape(var_284.astype('float32'), [9, 13, 15])), 0)
call_300 = relay.TupleGetItem(func_25_call(relay.reshape(var_284.astype('float32'), [9, 13, 15])), 0)
bop_304 = relay.bitwise_xor(const_277.astype('uint16'), relay.reshape(bop_279.astype('uint16'), relay.shape_of(const_277))) # shape=(4, 7, 9)
func_22_call = mod.get_global_var('func_22')
func_25_call = mutated_mod.get_global_var('func_25')
call_309 = relay.TupleGetItem(func_22_call(relay.reshape(call_291.astype('float32'), [9, 13, 15])), 0)
call_310 = relay.TupleGetItem(func_25_call(relay.reshape(call_291.astype('float32'), [9, 13, 15])), 0)
func_22_call = mod.get_global_var('func_22')
func_25_call = mutated_mod.get_global_var('func_25')
call_322 = relay.TupleGetItem(func_22_call(relay.reshape(call_283.astype('float32'), [9, 13, 15])), 0)
call_323 = relay.TupleGetItem(func_25_call(relay.reshape(call_283.astype('float32'), [9, 13, 15])), 0)
func_22_call = mod.get_global_var('func_22')
func_25_call = mutated_mod.get_global_var('func_25')
call_324 = relay.TupleGetItem(func_22_call(relay.reshape(call_291.astype('float32'), [9, 13, 15])), 0)
call_325 = relay.TupleGetItem(func_25_call(relay.reshape(call_291.astype('float32'), [9, 13, 15])), 0)
bop_326 = relay.equal(var_284.astype('bool'), relay.reshape(call_283.astype('bool'), relay.shape_of(var_284))) # shape=(1755,)
bop_329 = relay.equal(var_284.astype('bool'), relay.reshape(call_285.astype('bool'), relay.shape_of(var_284))) # shape=(1755,)
bop_338 = relay.bitwise_or(bop_279.astype('int8'), relay.reshape(const_277.astype('int8'), relay.shape_of(bop_279))) # shape=(4, 7, 9)
const_372 = relay.const([True,False,False,True,True,False,False,False,False,True,True,False,True,True,True,False,True,False,True,True,False,False,False,False,True,False,False,True,True,False,True,False,True,False,True,False,False,True,False,False,True,True,False,False,True,True,True,False,True,False,True,False,False,True,False,False,False,False,True,True,False,False,False,True,False,True,True,False,True,False,False,False,True,True,False,False,False,True,True,False,True,False,False,False,False,False,False,False,False,True,True,False,True,True,False,False,True,True,False,False,True,True,False,True,False,False,True,False,False,False,False,True,True,False,True,True,False,True,True,False,False,False,True,False,False,True,False,True,False,False,True,False,True,True,True,True,True,False,False,True,True,False,True,False,True,False,True,True,False,False,False,False,False,True,False,False,False,False,True,False,True,False,False,False,True,True,False,True,False,False,False,True,False,True,True,True,False,False,True,False,False,True,False,False,False,True,True,False,True,False,False,False,True,True,True,False,False,True,True,False,True,False,True,True,True,False,True,True,False,False,True,False,True,False,True,True,True,False,True,False,False,True,True,True,False,False,False,True,True,True,True,False,True,True,True,True,True,False,False,False,False,False,False,True,False,True,False,True,True,True,True,False,True,False,True,True,False,True,False,True,True,False,True,False,True,True,True,False,True,False,False,False,False,True,True,False,False,False,True,False,True,False,False,False,True,True,False,True,True,False,True,False,False,False,False,True,True,False,False,True,False,False,True,False,True,False,False,False,False,True,False,False,True,False,False,False,True,False,False,False,True,True,False,True,True,True,True,True,True,True,False,True,True,True,True,True,True,True,True,False,False,True,False,True,True,False,False,False,True,False,True,False,True,True,True,False,False,False,True,True,True,True,False,True,False,True,False,False,False,True,False,False,False,False,False,True,False,False,True,True,False,False,True,True,False,True,True,False,True,True,False,True,False,False,False,True,False,False,True,False,True,True,True,True,True,True,False,True,True,True,True,True,False,False,False,False,True,True,False,True,False,False,False,True,True,False,False,True,False,True,True,True,False,False,False,True,True,False,False,False,True,True,True,True,False,True,True,True,True,False,False,True,False,False,False,True,False,False,False,False,True,False,True,True,False,True,False,False,True,True,False,True,False,False,False,False,True,False,False,False,False,False,False,False,True,False,False,True,True,False,False,False,False,True,False,True,True,False,True,False,True,True,True,False,True,False,False,True,False,False,True,False,True,True,False,False,False,False,True,True,True,True,True,True,True,True,False,False,False,True,False,True,True,False,True,False,False,False,True,False,False,True,False,True,False,False,True,False,True,True,True,False,False,True,True,True,False,False,True,False,True,False,False,False,False,True,True,False,True,False,False,False,True,False,True,False,False,True,False,True,False,False,True,False,True,True,False,True,True,True,False,False,True,False,True,True,True,False,True,True,False,True,True,False,True,False,False,False,True,False,True,True,False,True,False,True,False,False,True,True,True,True,True,True,True,False,False,False,False,False,True,True,True,False,True,True,True,True,True,False,True,False,False,False,True,False,True,True,False,False,False,True,True,False,False,False,False,True,True,True,True,False,False,False,True,True,True,False,False,False,False,True,True,False,True,False,False,True,False,False,True,False,False,True,False,False,True,True,True,False,False,False,True,False,True,False,True,False,False,True,True,False,False,False,True,False,False,True,True,False,False,False,True,False,True,True,False,True,False,False,True,False,False,False,False,True,False,True,False,False,False,True,True,True,True,False,True,True,True,False,False,True,False,True,True,False,False,False,True,True,False,False,True,False,True,False,False,True,True,False,False,False,True,True,True,False,True,False,True,False,False,True,False,False,False,True,False,True,True,True,False,True,False,True,False,True,True,False,False,True,False,False,True,True,True,False,True,False,False,False,True,False,False,True,False,False,False,True,True,False,False,True,True,False,True,True,True,False,True,False,True,True,False,False,False,False,False,True,False,False,False,True,False,False,False,True,False,True,False,False,True,False,True,False,True,False,False,False,True,True,False,False,True,True,True,True,True,True,True,True,False,True,True,False,True,True,True,True,False,True,True,True,False,True,False,True,True,False,True,False,True,False,True,False,True,False,False,False,True,True,True,True,False,False,False,True,False,True,False,False,True,False,False,True,True,False,False,False,False,True,True,True,True,False,False,False,False,False,False,True,True,False,True,True,False,True,False,False,False,False,True,True,False,True,False,True,True,False,False,True,False,True,False,True,True,False,False,True,False,False,False,True,False,True,False,True,False,False,True,True,True,False,False,True,True,True,True,False,True,True,True,True,False,False,True,True,False,True,False,True,True,False,False,False,False,True,True,False,True,False,True,False,True,False,False,False,True,True,True,False,False,False,False,False,False,True,True,True,False,True,False,True,True,False,True,True,True,False,False,True,True,True,True,False,True,True,False,False,False,True,True,False,False,True,False,False,False,True,True,False,False,True,True,False,False,True,True,True,True,True,False,False,True,False,False,False,True,True,True,False,False,False,False,False,True,True,True,True,False,False,True,True,False,False,True,False,True,False,True,True,False,False,True,True,False,False,True,True,True,False,True,True,False,False,False,True,True,True,False,True,True,True,False,True,False,True,True,True,False,True,False,False,True,False,True,True,False,False,False,True,True,False,False,True,False,False,True,True,True,True,False,True,True,True,False,True,False,False,False,False,True,True,False,False,True,True,True,True,False,True,False,True,True,False,False,True,True,True,False,False,True,True,True,False,False,False,True,False,False,True,True,True,False,True,True,True,True,False,False,True,True,False,False,True,True,False,False,False,False,True,False,True,False,False,True,False,False,False,False,False,True,True,True,False,True,False,True,False,False,False,True,True,False,True,False,True,True,True,True,True,False,False,False,False,False,True,False,False,True,False,False,True,False,True,True,True,True,False,True,True,False,False,False,True,True,True,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,True,True,True,False,False,False,True,False,False,True,True,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,True,True,False,True,True,False,True,False,False,False,True,False,True,False,False,True,False,False,True,True,False,False,True,False,False,False,False,False,True,False,True,False,True,True,True,False,True,True,False,True,True,True,True,False,True,True,False,False,True,True,True,True,True,False,True,False,False,True,False,True,True,True,False,False,False,True,False,True,False,False,True,True,False,False,False,True,False,False,True,True,True,False,True,True,True,False,True,True,False,True,True,True,True,True,False,True,False,False,True,True,True,False,False,True,False,False,False,False,False,False,False,False,False,True,True,True,True,False,True,True,True,False,True,False,True,True,False,True,True,True,False,False,True,True,True,True,True,False,False,False,False,False,False,False,True,True,False,False,True,True,False,False,True,True,True,False,False,True,True,True,False,False,False,True,True,True,False,False,True,False,False,True,False,False,False,True,True,False,False,False,True,False,True,False,True,False,False,True,True,True,False,True,True,False,False,False,False,False,True,True,True,True,True,True,False,True,True,True,True,True,False,False,True,True,False,False,True,False,True,False,True,True,True,True,False,True,True,False,True,False,True,False,False,False,False,False,True,True,True,False,False,True,False,True,False,False,True,True,False,False,True,False,True,False,True,True,True,False,True,True,True,True,True,True,True,True,True,True,False,False,True,False,False,False,True,False,False,False,False,True,False,True,True,False,False,False,True,True,False,True,False,True,False,False,False,True,True,True,False,False,False,False,False,False,False,False,False,False,False,False,True,True,False,False,True,False,False,False,True,True,True,False,False,True,False,True,True,True,False,True,True,False,True,False,False,True,False,True,False,False,True,True,True,True,False,False,True,False,True,True,True,False,True,False,False,True,True,True,False,True,False,False,False,False,False,False,True,False,True,True,False,True,True,False,False,True,False,False,True,True,True,True,False,False,True,False,True,False,True,True,True,True,True,True,True,True,False,True,True,True,False,False,False,True,False,True,False,False,True,False,False,False,True,False,False,False,False,True,False,True,False,True,False,False,True,False,True,True,True,True,False,True,True,True,True,True,False,True,True,True,True,True,True,False,True,True,False,True,False,False,False,False,False,True,False,True,True,False,False,False,True], dtype = "bool")#candidate|372|(1755,)|const|bool
bop_373 = relay.floor_divide(bop_326.astype('float64'), relay.reshape(const_372.astype('float64'), relay.shape_of(bop_326))) # shape=(1755,)
bop_376 = relay.floor_divide(bop_329.astype('float64'), relay.reshape(const_372.astype('float64'), relay.shape_of(bop_329))) # shape=(1755,)
output = relay.Tuple([call_291,call_299,bop_304,call_309,call_322,call_324,bop_338,bop_373,])
output2 = relay.Tuple([call_292,call_300,bop_304,call_310,call_323,call_325,bop_338,bop_376,])
func_385 = relay.Function([var_278,var_284,], output)
mod['func_385'] = func_385
mod = relay.transform.InferType()(mod)
var_386 = relay.var("var_386", dtype = "int32", shape = (4, 7, 9))#candidate|386|(4, 7, 9)|var|int32
var_387 = relay.var("var_387", dtype = "float32", shape = (1755,))#candidate|387|(1755,)|var|float32
output = func_385(var_386,var_387,)
func_388 = relay.Function([var_386,var_387,], output)
mutated_mod['func_388'] = func_388
mutated_mod = relay.transform.InferType()(mutated_mod)
var_640 = relay.var("var_640", dtype = "uint8", shape = (11, 5, 5))#candidate|640|(11, 5, 5)|var|uint8
var_641 = relay.var("var_641", dtype = "uint8", shape = (11, 5, 5))#candidate|641|(11, 5, 5)|var|uint8
bop_642 = relay.not_equal(var_640.astype('bool'), relay.reshape(var_641.astype('bool'), relay.shape_of(var_640))) # shape=(11, 5, 5)
bop_652 = relay.divide(var_640.astype('float32'), relay.reshape(bop_642.astype('float32'), relay.shape_of(var_640))) # shape=(11, 5, 5)
var_658 = relay.var("var_658", dtype = "uint8", shape = (11, 5, 5))#candidate|658|(11, 5, 5)|var|uint8
bop_659 = relay.bitwise_and(var_640.astype('int8'), relay.reshape(var_658.astype('int8'), relay.shape_of(var_640))) # shape=(11, 5, 5)
const_664 = relay.const([[[7,-3,1,8,-9],[-9,-10,9,-9,9],[-3,-3,4,9,-1],[-9,9,5,-10,-6],[-5,-5,3,6,-3]],[[10,-9,8,-8,-9],[2,-9,9,-2,8],[-7,5,9,-6,-8],[1,-4,-2,2,-9],[-8,8,-3,1,8]],[[-3,4,9,-4,10],[3,-1,-10,9,-2],[4,1,-9,-10,8],[-2,7,9,-1,10],[-8,-3,-9,-3,-6]],[[7,6,3,-10,6],[3,1,3,-5,-4],[6,-9,2,-1,-4],[-9,-6,-7,-8,1],[9,1,-5,1,-1]],[[-6,-6,5,3,-10],[-4,8,-3,10,-3],[7,-9,1,5,4],[6,2,-5,9,-4],[4,9,-9,-6,6]],[[-1,1,-3,2,2],[-1,-7,10,9,-1],[10,10,-5,4,9],[-3,2,10,4,-3],[-9,-5,-7,-10,4]],[[-1,5,6,2,3],[9,-2,10,6,6],[-10,-6,-1,2,1],[-3,2,8,9,-7],[3,-10,7,-9,-4]],[[4,1,-1,-5,6],[-10,-10,4,-2,8],[-7,7,8,-7,-1],[-1,5,7,4,10],[5,6,4,-3,-5]],[[8,-4,9,-1,8],[-7,6,-8,-7,-4],[2,-7,-7,2,-9],[-5,-1,4,-10,6],[8,4,5,-7,-8]],[[-9,10,-1,-9,9],[10,-7,-2,10,-7],[-7,-2,-10,-6,-9],[-8,5,6,-9,10],[3,1,-2,-2,-4]],[[-1,-5,-3,-9,-4],[5,9,-1,7,8],[-7,9,2,10,4],[-6,-4,-7,7,-10],[-4,-2,7,8,3]]], dtype = "uint8")#candidate|664|(11, 5, 5)|const|uint8
bop_665 = relay.floor_mod(var_640.astype('float32'), relay.reshape(const_664.astype('float32'), relay.shape_of(var_640))) # shape=(11, 5, 5)
output = relay.Tuple([bop_652,bop_659,bop_665,])
output2 = relay.Tuple([bop_652,bop_659,bop_665,])
func_668 = relay.Function([var_640,var_641,var_658,], output)
mod['func_668'] = func_668
mod = relay.transform.InferType()(mod)
var_669 = relay.var("var_669", dtype = "uint8", shape = (11, 5, 5))#candidate|669|(11, 5, 5)|var|uint8
var_670 = relay.var("var_670", dtype = "uint8", shape = (11, 5, 5))#candidate|670|(11, 5, 5)|var|uint8
var_671 = relay.var("var_671", dtype = "uint8", shape = (11, 5, 5))#candidate|671|(11, 5, 5)|var|uint8
output = func_668(var_669,var_670,var_671,)
func_672 = relay.Function([var_669,var_670,var_671,], output)
mutated_mod['func_672'] = func_672
mutated_mod = relay.transform.InferType()(mutated_mod)
const_695 = relay.const([[[6,3,-3,-1,-3,7,-8,9,9,2,-3,-5,-7],[-7,-2,-7,10,-2,-9,10,-10,3,6,-5,-3,-4],[-7,-1,-5,9,1,-6,6,-4,10,8,-8,8,-5],[9,-4,-6,4,-7,-4,-8,4,5,-3,6,10,-5],[-5,4,-10,7,6,4,1,-8,-8,9,2,2,3],[-1,2,-5,9,-8,-2,2,10,-5,7,-5,2,7],[-10,-9,8,9,-6,-10,4,5,-5,-2,-4,6,-2],[8,-7,-8,-7,1,9,-7,4,1,5,4,4,3],[-4,-1,1,2,6,6,-1,9,9,-4,-3,-1,-2],[8,-2,3,-1,-4,-4,10,-8,-5,5,8,2,-9],[6,5,6,3,-6,5,3,-10,8,10,8,7,-9],[-9,7,-6,-9,-1,4,-2,2,-8,9,-3,9,4],[-9,3,6,-9,-2,-5,7,6,2,2,7,1,9],[2,-1,7,9,-8,-6,7,-1,6,8,9,-10,-6],[-2,-3,-4,1,3,-3,-10,7,-7,1,-5,-6,-1]],[[-5,-6,9,9,-1,7,8,9,-2,4,4,-4,-9],[-6,-1,10,9,6,-5,10,-10,7,-8,-1,5,2],[7,6,2,-3,-10,-1,-8,-7,-4,9,5,-1,-4],[5,-8,-1,-10,2,-1,-9,9,-10,-8,2,-3,5],[-8,-10,1,-2,-2,-5,-1,6,-4,-3,-4,-2,9],[6,4,1,-10,-6,8,-9,2,3,-2,5,6,1],[-2,-4,-6,2,-2,5,6,2,-9,6,-8,5,10],[8,-10,5,3,-3,-8,2,-10,1,-6,1,5,-5],[8,2,9,-1,-2,-1,4,5,-10,3,2,7,-8],[-3,8,5,-9,-2,-1,-9,1,-8,-5,8,-8,7],[-4,9,-5,-4,-4,10,10,-4,-7,1,-7,3,-2],[9,-2,1,3,10,2,-2,7,-10,4,-5,8,-6],[-7,-7,2,10,-4,-1,-8,-4,7,7,-8,8,-2],[4,2,-5,1,-9,-9,6,-7,2,-8,-8,-4,8],[5,-5,-10,6,-1,3,4,2,1,1,-4,5,-1]],[[6,1,9,-9,-2,-5,3,1,7,-7,3,6,-8],[-6,4,-10,-5,6,7,-10,8,-7,-3,-6,4,-1],[3,-10,10,8,5,8,-8,-4,2,4,-3,-1,-9],[-9,2,1,-7,-10,9,3,-7,2,5,-2,1,-9],[9,1,8,-1,7,-8,5,1,8,-7,-5,4,-6],[9,6,-4,-7,-1,4,-5,-7,7,-3,-5,-4,-9],[3,1,2,9,-7,3,7,-6,7,3,-6,-8,-3],[-9,-7,-8,-4,2,-8,-3,3,8,9,10,-5,2],[5,10,2,7,-10,2,3,-9,4,-7,-6,-6,8],[3,-10,7,-6,5,8,7,-6,-1,2,3,2,2],[4,-4,-3,10,-3,-9,5,7,8,3,-5,-5,4],[3,-10,5,3,8,10,9,6,2,-4,5,7,5],[2,-10,-10,6,10,-3,3,-8,3,6,-5,-1,1],[2,3,9,9,-6,2,10,3,4,-9,1,-10,-9],[7,-6,5,-8,7,-6,7,-7,3,-3,-1,4,-1]],[[-9,-2,-6,8,9,1,-4,5,5,1,4,-9,4],[-4,-1,-5,-6,1,-8,-5,4,6,-4,-7,6,-3],[6,7,-6,-8,8,9,2,5,1,-9,-5,5,10],[10,-2,6,7,-7,6,7,-1,-7,8,-5,3,-6],[-10,10,6,6,3,7,-5,2,-4,-5,-5,7,4],[2,5,8,2,-7,-7,8,5,1,-2,1,-2,-10],[-9,-2,-1,10,6,-3,-5,-9,-3,4,2,8,-10],[7,-7,1,-6,-7,-1,2,5,8,-8,-2,-3,9],[-4,9,-7,-6,-5,-10,-3,-5,6,-4,5,-2,-8],[-3,3,-4,10,2,2,-2,8,6,-1,-6,10,-9],[-1,-7,-7,7,2,-8,-7,-10,10,-3,-3,10,2],[2,-7,7,10,-6,-4,-9,-8,-7,-7,3,-8,-6],[9,-7,-1,1,10,5,-3,8,-7,2,-4,-10,7],[-8,4,-7,9,2,-5,-9,4,-6,6,2,1,-9],[-4,-5,4,5,-7,-9,-10,-8,7,-1,-3,5,1]],[[3,3,6,-10,-8,4,2,-10,10,3,7,7,-10],[7,10,-5,9,-6,5,5,10,-1,-1,-3,-2,-2],[6,-9,8,2,-1,2,2,4,-1,3,8,-4,-4],[3,3,5,3,-6,9,10,2,1,-7,3,3,1],[-9,-2,4,-9,1,6,9,4,9,-7,5,5,4],[-1,-4,-10,-9,-6,-8,-2,10,-2,2,-8,-1,10],[-4,7,4,4,-2,1,-7,-8,1,-3,-8,1,-2],[-10,3,-8,-6,-4,4,-6,-10,-10,3,1,8,8],[-2,7,-7,6,5,-8,10,-1,10,1,-6,9,8],[7,6,1,4,2,3,3,4,10,5,-8,-9,-7],[9,6,5,-3,-9,-1,-10,-4,4,2,-9,4,4],[-9,3,1,1,9,-3,9,7,-4,-4,2,6,-8],[8,10,-5,8,6,-10,-7,5,3,1,-3,-7,-3],[-6,4,-5,5,-8,-6,-8,6,-1,7,4,-9,10],[-7,-10,-7,-9,-2,5,2,10,10,2,6,-8,9]],[[-4,6,-10,-2,-3,-1,-2,-9,-2,10,8,-10,3],[-4,-8,4,1,6,3,4,-9,-10,-7,5,1,1],[-5,-10,6,1,8,6,5,1,-3,6,1,10,9],[7,-3,9,-1,8,4,-1,-7,2,-2,2,9,5],[5,7,-3,4,-7,5,2,3,-3,6,3,1,-2],[-9,10,10,9,1,-6,-1,-6,8,10,-1,8,-2],[-7,4,-6,2,-5,5,-4,10,-9,-2,9,-2,3],[-3,-3,10,10,1,5,3,-8,7,-5,9,-10,-9],[-10,8,-6,-4,4,1,6,-9,7,-4,-2,-4,-8],[1,5,6,10,-1,-3,-5,9,-2,-10,-7,-4,-2],[1,-3,1,8,-3,5,8,-10,-3,9,-1,-8,-3],[7,-7,6,-5,9,-3,3,-1,9,-6,-10,6,-10],[2,7,4,-3,-3,9,9,3,4,10,-6,-3,-10],[1,4,-2,-1,10,-4,-6,-5,2,-2,-8,3,-2],[-8,1,-9,3,-4,-10,5,2,-6,-6,-5,6,7]],[[6,3,9,2,-9,-10,6,9,-3,-7,-6,5,-5],[4,8,5,-9,9,-10,-8,5,1,-4,-9,-9,-1],[-1,-8,-7,-10,-4,-8,-3,-3,-9,2,-8,7,-7],[10,3,10,-10,-4,3,-1,-9,1,5,5,-4,-9],[-1,-4,-1,4,-8,1,5,4,-7,4,-1,8,-1],[-1,9,7,6,-10,-6,4,9,1,-1,1,-9,6],[1,7,6,-5,7,8,-3,-2,-1,4,-2,-3,1],[2,8,-9,1,-1,3,-5,9,-6,2,-3,6,2],[-6,10,-6,7,-10,2,-2,2,8,8,3,-10,-3],[7,-4,-7,3,-8,-10,2,1,5,9,-9,-7,4],[2,-4,-1,-4,7,5,-9,-8,10,-2,7,4,-7],[3,-1,-5,-5,8,7,2,5,5,-2,4,-6,-3],[-6,-9,2,-8,-2,-6,1,2,-9,-5,4,8,-4],[8,-3,-4,-9,-3,-6,-6,5,5,9,5,4,2],[-9,-3,-5,4,3,-6,-3,-5,-1,7,-4,-1,10]],[[1,-3,9,3,6,3,7,-9,10,3,1,8,-7],[10,7,3,3,9,9,-6,-10,-8,6,-2,-9,6],[9,8,8,4,-8,-3,5,7,-4,1,-1,-2,6],[7,-1,5,-7,-5,-1,-2,8,-3,7,-6,-10,-4],[-8,2,-2,-9,-10,-10,9,5,8,10,3,8,-3],[1,-5,-6,3,5,7,-8,-8,5,6,9,7,10],[5,10,-6,1,5,-2,-5,4,1,-8,-2,8,5],[4,9,2,5,1,-2,-1,-8,-7,-10,-5,-5,-1],[8,-9,-9,4,10,-1,7,-4,-2,10,-8,5,10],[-8,-4,5,10,-4,-8,6,-4,1,-7,-2,2,1],[9,-9,-9,-3,7,5,-2,8,-9,8,-9,5,-5],[-7,9,8,-7,4,-5,-8,-4,2,4,-6,4,6],[-2,-3,6,-6,9,2,3,9,2,4,10,4,8],[7,-3,-7,-4,1,-8,4,3,3,-1,-7,10,2],[7,-4,-5,7,5,-2,2,-10,4,-10,-1,4,5]],[[-6,-3,5,-4,5,3,9,5,9,-9,-10,3,10],[4,6,9,6,-10,-2,-1,6,-8,-4,-10,-10,1],[2,1,6,9,-7,-3,10,6,-10,10,3,-4,-3],[-1,1,-5,6,6,3,5,2,3,-5,-6,5,2],[-4,-6,-1,1,9,-5,-4,-8,-6,9,4,2,2],[-4,-3,-7,-5,5,-2,-7,4,7,-5,-7,1,-1],[-9,-2,-2,-7,5,2,-9,-3,5,3,4,-7,6],[-1,7,1,4,6,10,-1,-7,2,-1,-8,-8,6],[-10,2,5,4,5,10,9,-7,7,-3,-2,4,-3],[-10,3,3,-6,-3,8,5,-3,7,8,2,-2,4],[1,7,-10,6,-4,-9,6,3,9,9,2,-5,-10],[8,3,5,-9,9,1,3,6,6,-3,-6,-7,-4],[1,-9,-8,2,-10,5,-1,-1,2,10,7,10,6],[-10,-2,-2,-4,5,-2,3,-6,-1,7,-9,-7,8],[4,-4,5,3,-8,10,10,6,-2,3,-9,5,8]],[[6,-5,-9,-2,1,-7,-5,-1,-1,-10,-2,7,-2],[-2,2,-3,5,-3,-8,7,4,-6,-1,4,10,8],[-10,-9,-1,1,9,4,-3,8,3,3,-1,6,7],[-3,-8,1,6,-10,9,10,5,-3,4,2,-1,7],[-3,4,-5,-7,8,8,-7,10,-2,-5,-8,-7,-2],[-10,-1,4,9,4,-7,-6,-8,-10,5,-1,4,-3],[-6,3,-7,-10,-7,2,6,-10,6,9,-2,-7,3],[-3,-5,7,9,7,2,-6,-4,5,-6,-3,2,-6],[-5,3,-2,4,7,7,1,1,3,-2,-8,9,5],[6,-5,4,-7,9,5,7,5,5,-9,-1,6,1],[4,7,3,-7,-8,-10,7,-6,-3,4,6,7,-8],[10,-6,9,3,7,1,-6,-4,8,8,-6,7,-10],[-9,-10,7,-4,-1,3,1,9,4,3,-2,1,-4],[-10,7,4,8,7,-4,-10,-4,-8,-3,-6,-2,6],[1,5,-6,-6,8,-9,6,4,6,4,7,4,-8]],[[-6,3,-8,1,10,8,-10,-8,3,-4,-3,-10,-10],[-8,6,7,10,-6,-4,10,6,-2,6,-5,3,9],[8,2,8,-2,-7,6,9,-4,1,-7,-5,3,-10],[-4,8,8,3,-3,9,5,2,-3,-5,4,-2,5],[1,-1,-8,5,-8,-1,-4,-4,-8,10,10,1,-10],[-3,7,2,-8,10,-7,4,-7,-10,7,-5,-3,-7],[6,-10,4,-1,-1,-10,5,7,-2,-9,5,-1,3],[9,10,-1,-5,-5,4,1,-8,-6,-8,4,5,-2],[-5,3,8,-6,-8,-5,5,4,-5,-7,-6,5,-8],[-8,6,-3,3,-9,-8,7,1,10,1,7,1,-10],[-9,-4,8,1,-2,-5,10,5,-10,-3,6,8,9],[7,1,6,-4,10,2,6,-6,8,6,4,-8,6],[10,3,-1,-9,8,6,-6,4,6,4,2,7,-5],[-3,-8,9,6,9,-10,2,4,10,4,9,-5,-3],[-5,2,-3,-5,7,-1,5,10,8,3,-2,3,-6]],[[-8,-5,5,-5,-2,-5,9,2,-3,-10,2,5,-2],[-8,-4,9,-5,-5,6,9,-8,6,4,-9,-7,-10],[-9,-4,-3,-5,-7,9,9,-4,5,3,-8,3,9],[1,-3,4,-5,2,-1,4,-9,3,6,3,1,-5],[6,-2,-1,10,-3,7,-3,7,6,-5,4,-3,3],[2,-1,-2,-6,-10,7,-5,4,-8,1,-4,-9,-1],[5,1,-1,4,9,-7,-2,4,-10,-8,10,-3,5],[9,-4,-5,6,1,-1,9,2,-7,-4,-4,9,-9],[1,-2,-9,10,-1,6,-3,7,3,3,2,4,10],[-10,-1,10,5,8,-10,9,5,1,4,1,-1,-7],[-4,-1,-8,-5,-4,-10,-6,-2,7,8,-9,-10,-6],[-2,-5,2,-9,-8,-5,-5,10,7,2,-10,1,2],[8,10,-3,1,-3,-1,-7,9,-2,1,8,7,5],[2,7,5,6,-7,10,-8,2,-3,-8,1,9,-3],[-9,-8,10,-2,5,-10,3,-1,9,5,-9,-2,-3]],[[9,6,8,4,4,7,9,-3,5,10,8,5,3],[-2,-3,10,6,5,3,-1,1,3,1,1,-2,4],[-10,-3,-5,8,9,-1,5,-10,-3,-5,10,6,-6],[1,-8,7,-4,-3,-7,-8,-8,-3,2,3,-6,-4],[8,10,-7,-1,-4,6,-1,6,9,-4,2,2,-3],[-3,-3,7,-7,5,-8,2,7,1,-5,5,2,3],[-1,7,-9,-4,7,6,-8,9,-7,7,9,3,-4],[9,10,-7,-6,4,7,10,9,8,-6,3,-10,-7],[-8,-2,-9,-8,3,-9,-2,-6,2,4,1,1,1],[-1,4,-9,-10,-5,-1,7,8,5,-2,-2,-9,8],[-8,-5,2,-1,6,7,10,5,4,-7,10,4,-3],[6,3,-1,-4,-2,-4,1,3,-6,-9,-4,2,5],[3,6,8,-1,-10,3,-1,-8,-10,-7,-6,-5,3],[-10,-3,1,-8,6,-10,8,9,4,10,7,1,-2],[6,-6,1,5,10,-3,-2,-6,-6,-4,8,7,10]],[[-8,5,-1,-1,9,2,-5,-8,3,-7,-4,-3,-10],[-6,9,-8,-8,10,3,6,-3,-3,-1,7,3,-10],[1,-3,4,-7,-7,3,9,7,-3,5,1,4,-1],[5,9,8,1,-2,-3,10,-5,9,6,-7,1,7],[-9,8,-4,-1,10,-4,3,8,4,-7,-10,-2,-4],[-7,10,-9,-7,-7,9,5,-9,2,6,7,-7,6],[1,-6,-8,2,-9,4,-9,8,-1,9,3,-10,-1],[-6,1,6,3,-9,-6,-6,1,2,3,7,-2,-3],[-8,-3,-10,-7,-4,-5,6,-7,-4,-7,3,4,-9],[9,9,-6,5,-6,-2,-9,8,3,-9,-6,3,7],[-5,1,4,-5,2,-10,3,-3,10,1,-8,-2,5],[8,-1,6,-8,8,-9,-4,6,-9,1,6,-3,-7],[-3,8,7,8,2,2,10,-5,4,-9,5,-1,-9],[-6,-4,-5,-4,-5,-8,-8,6,4,3,5,9,10],[-10,-8,8,3,-9,-8,-1,3,-7,-2,3,1,3]],[[3,-9,-6,2,10,-10,-1,-1,-1,2,-2,6,-4],[-9,-3,2,-6,7,-10,6,10,-4,4,-9,-8,10],[2,5,5,2,6,-3,4,2,10,7,3,-10,7],[-3,-2,6,-9,1,-4,-1,8,-1,-4,8,3,6],[5,5,7,8,9,5,-4,1,1,8,-3,-2,2],[-3,-3,2,-6,1,-5,7,2,3,8,6,3,7],[-3,-5,8,1,-8,1,-2,-9,1,2,-8,1,-6],[-5,1,6,-2,-8,-8,2,-3,-10,-5,-1,-7,-2],[-7,-8,2,-3,7,8,10,-10,6,-6,6,4,-7],[10,8,-8,8,8,-1,-4,10,-8,7,-1,-9,-2],[3,6,8,5,-9,1,-10,7,1,10,3,-4,-3],[5,-1,4,-10,-7,6,8,-4,-3,9,-6,1,-2],[3,7,8,-9,-9,-7,5,9,4,7,6,2,9],[-6,3,7,1,-3,7,1,7,5,10,3,3,1],[9,-7,-3,-1,10,-4,3,1,1,4,-8,10,-4]],[[1,3,9,7,-2,-10,9,-10,-10,-2,3,-2,3],[-7,-7,6,-2,-2,-10,-8,9,5,7,-1,-10,-7],[10,3,9,-6,3,-6,10,-8,9,3,4,-8,-5],[8,-3,10,4,7,-3,4,9,-5,-10,-9,8,8],[2,-5,-4,2,-7,3,8,-7,-4,-1,10,2,-6],[10,-5,-8,-2,-3,5,6,-10,5,8,10,-4,-7],[-4,6,-1,8,5,-4,10,-5,-3,-8,1,-4,7],[3,5,-8,10,-1,-2,-9,-6,6,-10,-10,4,-7],[-9,-4,-5,8,8,10,-9,10,-1,-8,2,10,7],[-7,6,-5,-7,3,-7,-1,-8,2,-4,-1,-3,-10],[5,9,2,4,-9,4,8,-7,2,-10,1,-2,-8],[7,-3,6,-9,-1,-10,10,4,5,-3,8,2,-8],[4,7,-4,-1,5,9,4,-6,5,-4,-10,-2,1],[10,10,8,9,-5,-4,-2,-6,3,-10,-2,3,-7],[-5,5,1,-1,5,-4,-7,-9,-7,-7,3,3,-9]]], dtype = "uint8")#candidate|695|(16, 15, 13)|const|uint8
var_696 = relay.var("var_696", dtype = "uint8", shape = (16, 15, 13))#candidate|696|(16, 15, 13)|var|uint8
bop_697 = relay.left_shift(const_695.astype('uint8'), relay.reshape(var_696.astype('uint8'), relay.shape_of(const_695))) # shape=(16, 15, 13)
func_668_call = mod.get_global_var('func_668')
func_672_call = mutated_mod.get_global_var('func_672')
const_701 = relay.const([[-3],[-6],[9],[-4],[-8],[-4],[-1],[2],[-2],[-8],[-8],[-9],[8],[8],[7],[-10],[-3],[5],[-10],[5],[-1],[8],[9],[-9],[-3],[-5],[-3],[-1],[-6],[10],[-3],[6],[-9],[-7],[1],[10],[2],[3],[8],[-2],[9],[3],[-2],[1],[-1],[5],[-3],[9],[-3],[4],[10],[-7],[2],[2],[4],[-10],[-1],[-4],[-7],[-3],[10],[-2],[1],[7],[-10],[10],[-5],[-2],[9],[-6],[8],[-5],[-8],[2],[-8],[4],[4],[-2],[-9],[-9],[-10],[-1],[-5],[1],[-9],[-6],[-2],[3],[-4],[5],[-3],[1],[-5],[2],[-2],[7],[9],[-8],[-2],[-8],[-5],[-7],[-7],[-6],[7],[-4],[-10],[-8],[8],[1],[1],[1],[-7],[-4],[-7],[2],[-9],[8],[9],[-9],[-5],[7],[-8],[10],[-6],[-5],[10],[-9],[-6],[-8],[7],[6],[8],[4],[-7],[-4],[-5],[-6],[9],[-8],[-9],[-4],[-10],[6],[7],[-10],[5],[-10],[9],[-10],[6],[9],[-6],[-4],[-4],[-2],[5],[10],[8],[-3],[1],[1],[9],[-6],[-5],[7],[10],[-3],[-2],[3],[-9],[-9],[-8],[2],[-4],[-3],[8],[8],[5],[-8],[-2],[-4],[-10],[9],[5],[-9],[5],[-9],[-6],[1],[7],[4],[9],[-5],[-8],[7],[-7],[-2],[-9],[8],[-3],[6],[-5],[-2],[-9],[-1],[-8],[4],[-9],[-2],[-1],[8],[-9],[4],[1],[9],[10],[-1],[2],[6],[-6],[-10],[3],[10],[2],[-10],[-10],[-10],[9],[4],[-5],[-2],[-10],[-2],[6],[-6],[6],[-5],[-9],[-3],[-6],[5],[-3],[4],[10],[-2],[2],[-1],[-8],[-7],[-10],[5],[10],[-9],[6],[1],[6],[7],[-10],[1],[-10],[4],[-6],[-8],[-8],[9],[9],[-8],[-3],[-9],[8],[10],[-5],[-5],[-1]], dtype = "uint8")#candidate|701|(275, 1)|const|uint8
call_700 = relay.TupleGetItem(func_668_call(relay.reshape(const_701.astype('uint8'), [11, 5, 5]), relay.reshape(const_701.astype('uint8'), [11, 5, 5]), relay.reshape(const_701.astype('uint8'), [11, 5, 5]), ), 2)
call_702 = relay.TupleGetItem(func_672_call(relay.reshape(const_701.astype('uint8'), [11, 5, 5]), relay.reshape(const_701.astype('uint8'), [11, 5, 5]), relay.reshape(const_701.astype('uint8'), [11, 5, 5]), ), 2)
output = relay.Tuple([bop_697,call_700,const_701,])
output2 = relay.Tuple([bop_697,call_702,const_701,])
func_709 = relay.Function([var_696,], output)
mod['func_709'] = func_709
mod = relay.transform.InferType()(mod)
var_710 = relay.var("var_710", dtype = "uint8", shape = (16, 15, 13))#candidate|710|(16, 15, 13)|var|uint8
output = func_709(var_710)
func_711 = relay.Function([var_710], output)
mutated_mod['func_711'] = func_711
mutated_mod = relay.transform.InferType()(mutated_mod)
const_750 = relay.const([[[-9.079668,-5.534357,0.447432,2.001731,-3.488443,-1.543145,-9.549497,6.259381,-5.338719,8.401844,6.342811,-0.080175,-0.309401,-6.041574]],[[7.953881,-2.215542,-9.814988,8.164817,2.466345,9.001830,7.000270,-6.509320,-7.051106,6.441793,-2.044660,5.866227,-3.200941,-3.792936]],[[4.204152,3.134385,8.239266,2.871199,-5.794447,4.149266,7.607872,-5.919034,4.076835,-1.107405,-0.535417,-5.236832,-0.824518,-7.466085]]], dtype = "float64")#candidate|750|(3, 1, 14)|const|float64
uop_751 = relay.sqrt(const_750.astype('float64')) # shape=(3, 1, 14)
func_22_call = mod.get_global_var('func_22')
func_25_call = mutated_mod.get_global_var('func_25')
const_754 = relay.const([9.617288,1.425418,7.848989,-4.177010,7.473856,-0.567498,-2.036036,-2.270043,-1.499089,8.218985,-2.025466,8.539683,-0.687666,-1.430721,7.051632,2.453113,-4.050085,1.165560,-7.168231,-1.627757,8.432202,6.026459,-6.487959,-4.309291,8.291887,-3.997915,5.835356,0.709421,5.198370,2.959965,5.170526,6.785492,-8.963830,0.898758,-4.698822,-5.663806,0.812945,0.938109,6.596586,-1.007348,-0.730142,-4.761218,-7.292374,1.598290,6.080147,-1.666740,2.242626,4.703351,5.655025,6.783020,-2.094142,0.006094,7.373123,7.014526,-6.089676,3.278501,0.857820,4.333404,-5.965412,3.386726,1.142400,-5.613770,0.670646,-3.584179,4.250789,4.904007,3.317759,7.637457,3.616128,-8.112412,-6.556959,-5.775858,3.370778,-0.334616,-6.925775,-4.722184,8.747081,2.264111,-4.285852,7.852774,2.313971,1.659841,5.370754,5.723293,-3.407645,7.375868,-7.944860,-1.491512,5.624217,8.840841,-3.859311,9.036291,-7.342125,-4.370390,6.130009,-4.165528,-5.008844,1.684524,-0.687244,7.090126,-9.483900,-4.816996,-1.827969,8.362606,5.678547,-4.326473,-5.699250,0.596331,-0.898204,9.420944,-5.366917,-3.834215,7.976437,-4.983741,-7.443870,-5.201919,-2.196077,1.044682,5.720535,-9.049919,2.851301,-4.417999,0.378305,6.576286,-1.868729,8.482159,-8.311122,8.823779,8.162032,-7.677347,5.802399,2.943204,8.999279,3.423755,3.119661,9.107808,-7.680606,-5.847384,3.923270,2.478110,-2.181696,-1.523960,-3.014736,-3.815535,-0.317752,6.185145,-9.114831,4.002765,-4.875101,-0.739827,5.592430,-5.125425,-2.592448,9.167762,-9.322900,8.709217,2.806486,-4.352597,1.031469,7.430624,8.602038,-9.929018,2.067440,2.224407,-6.915420,7.533260,9.675972,0.934595,-5.954035,3.006547,0.750688,8.231300,0.397838,-5.229344,1.358586,-4.184712,-7.838273,-0.813212,-5.161940,8.093577,8.019851,-9.598690,2.186391,-8.141836,-4.021379,-6.184266,-4.661911,-5.703553,5.194306,7.703101,7.914914,9.536282,-6.548193,5.072592,8.519072,7.163687,-0.395522,0.726762,1.833277,4.644032,-2.590918,6.550876,-4.604626,-1.493042,-0.139850,-0.007932,5.443528,3.099531,2.273976,-9.911524,-8.033639,0.917383,-8.769712,-8.379791,4.755395,4.746726,4.614899,-0.383464,6.172748,-9.904606,-9.487245,8.257342,-4.269601,6.919408,3.323504,8.047015,9.818118,-8.578047,7.789972,4.435936,4.904459,-8.552967,5.382836,-0.835914,0.586735,-4.021326,3.068387,6.687828,2.628872,0.128730,9.379460,-2.071105,3.301377,-5.379372,4.683597,5.022239,-3.862082,5.199292,1.840856,-5.995765,-3.035413,-2.068642,-0.229111,-4.583984,9.803160,6.145233,-2.368332,3.542921,-6.346073,-3.581179,-8.535546,-2.579778,-9.964918,-0.595703,0.031020,-2.237408,-2.403206,8.079826,0.161381,-3.857083,1.997532,6.474609,2.846594,-2.343298,-6.004067,0.566469,-7.739265,5.646987,3.771114,-4.357731,0.413735,9.698208,-7.084297,-5.446540,-4.255082,-1.670594,-9.946636,9.013087,-3.331162,-2.486119,-5.066177,8.146885,8.096990,1.112565,7.289580,-8.879508,5.148183,-3.473807,-4.544555,8.728437,8.198796,8.867209,2.331118,5.817747,-9.192851,-9.094425,0.993625,5.026909,-3.257658,3.372957,4.580504,-9.585946,4.585324,-5.690254,-9.102952,-1.775516,9.428640,4.231781,-1.096843,-3.230327,-1.057525,-6.657341,1.815374,4.341373,-3.216651,9.619506,-2.614388,-3.741747,-4.953136,2.861669,-4.104029,-4.651151,3.180758,-3.199154,-6.181817,-1.534943,4.901405,-2.452268,9.612273,5.542209,-3.377809,3.440555,-8.529499,2.305697,-6.392592,1.920202,-1.213974,-0.041698,-7.781480,-4.847381,2.995398,0.510940,8.087998,0.663937,7.282276,-4.437084,2.131946,-2.323430,-5.585148,-8.668385,6.432917,2.394698,2.051779,3.605802,3.352282,-0.866046,5.714201,4.770732,3.085641,2.129973,6.623430,1.918392,5.587850,1.387758,4.133610,-9.113728,5.165904,-0.639859,1.961074,-5.759078,9.554714,2.234917,8.997990,8.453936,-3.975311,9.642544,9.474782,-9.113028,5.826542,-5.879717,-1.143408,4.515753,-9.476823,-7.881063,1.013906,-9.971055,-5.438835,4.955846,9.644583,-9.679266,3.605146,7.948424,-6.246936,6.411717,1.359525,-8.217748,-3.088667,-5.186822,-8.359325,-1.129244,5.762751,-7.071812,1.434867,8.111203,1.963448,-8.829990,-8.097410,4.517332,8.662550,-9.257169,-4.804177,-8.043180,-0.051942,2.288508,-3.612829,-5.244726,5.120349,9.370874,4.011646,7.936855,-4.130664,9.616958,3.660923,-2.089347,-6.164468,-4.304326,2.574637,9.065552,3.429254,-4.870972,4.250842,6.350651,-9.053835,6.192090,-0.536710,-1.147713,-4.456258,2.866896,-6.582145,-5.906146,-9.595289,8.166999,-5.207152,0.139917,7.595924,7.053486,-2.579719,2.717168,6.593096,-6.473464,6.683970,-1.426614,1.772280,-7.924177,6.938941,-3.673639,4.675573,-4.885270,-3.434483,7.407827,5.745242,-3.540609,8.768733,-6.543379,-4.340758,-2.661060,3.596808,1.756042,-3.591325,-6.313650,8.748593,3.087379,-2.734900,-8.549179,4.348519,7.056564,-5.804255,1.396242,0.137496,-6.899664,-3.527196,-4.195982,9.677209,-6.434688,9.841472,-1.826146,5.784693,5.191048,8.303705,7.994462,4.511566,2.849898,-9.181119,7.168360,6.933702,-6.501747,5.457671,9.019173,-9.591762,-1.885850,4.808912,-0.727122,2.576766,-0.675467,2.064043,3.207338,-0.121538,-3.673808,7.558423,9.892688,9.274226,7.084606,-2.943733,-1.235627,-4.692384,-5.591905,7.291418,3.574959,-0.249607,3.529224,3.047739,-0.456126,6.360528,-2.898113,-0.874118,2.751351,3.986736,-8.267623,-7.144971,8.560847,-4.697079,-4.089490,-1.561616,-0.194760,1.407934,9.961804,-5.290890,9.283624,-5.879865,1.844892,8.692347,3.814164,3.433017,-8.609317,-1.077089,-3.173204,1.814131,-2.653705,-6.944929,-2.143499,-1.680684,-2.503724,5.572262,-6.810543,-3.357289,-4.020197,2.608192,-3.921036,-1.178425,-4.870949,-5.082400,7.862211,5.295832,-8.683305,-8.495781,7.464502,-3.241307,8.329498,4.426133,2.339168,3.398697,8.870152,6.243766,2.478901,-2.543821,-0.366721,0.347046,-2.699627,3.633454,-7.953024,2.868007,-1.224135,-4.310757,0.630894,-6.318120,4.432974,0.183439,-0.586341,-0.842686,-2.255025,3.690916,-7.359331,-4.525489,6.888711,9.741042,4.147940,3.953966,-0.876325,4.132196,-8.836870,-7.872800,-3.224195,-0.669496,1.987339,-8.090392,-2.445526,-7.792113,-2.106983,4.234227,0.116335,-2.753664,-8.678960,-7.851972,7.798162,-0.266819,7.215481,5.381242,-4.316130,-7.937562,-6.924724,3.428473,-2.233064,1.275014,-5.273083,-6.047119,7.118231,-8.101740,2.493951,-6.041905,2.649759,-9.654037,-9.722733,-3.276632,9.816929,-9.288789,2.064324,-5.898448,5.125087,9.878137,4.661637,9.372220,-3.816900,-6.958409,3.956455,-1.157589,7.941212,8.760563,-3.338122,9.852825,1.752400,3.997632,4.398789,-0.846511,-3.348350,1.759218,-6.980668,-6.263740,-4.475040,-6.633529,-8.743010,-9.688970,5.222622,2.065296,9.801176,1.881345,-9.338654,-5.949674,2.961039,-5.799882,-1.460449,7.840561,9.703875,7.973978,-3.175577,5.302575,-9.899172,-4.214734,4.404869,2.898524,-4.422733,4.712267,4.364574,1.911649,1.768954,-9.719164,1.460364,-5.130562,-4.529595,-9.736281,4.883072,4.947193,-3.488697,7.827275,1.802155,-6.708014,4.325113,-8.323912,3.081025,6.363482,3.596760,-7.847627,8.464690,0.394944,-2.303754,-9.647167,3.005364,4.311746,-6.073322,-2.011951,9.323527,4.033084,-6.356988,-9.887685,4.482968,-5.849090,3.824408,4.102188,0.059962,-3.458857,4.114286,0.002866,-0.737587,-1.557128,2.532762,-0.191749,2.531024,-7.191256,5.551599,-8.682003,-0.235152,-9.156899,0.336724,1.815360,-6.782802,8.617885,-2.680788,4.278278,7.589130,4.273936,-2.950235,-1.357051,-8.184418,5.409647,5.447237,-8.042379,6.192727,6.717346,5.919580,8.971127,8.877951,5.909736,-6.618442,-1.955448,-2.742864,-3.914534,-2.526766,-7.750266,1.130818,-2.515063,7.102230,7.168093,2.130220,-3.382684,9.315326,2.516209,-2.936991,-4.921296,4.633025,-1.166644,9.791652,-7.369135,1.941984,-1.430211,-9.010013,8.685260,2.625796,-8.775815,-1.816607,8.803360,3.860135,-6.556416,2.654981,-1.332539,1.503219,-3.469783,9.359947,-4.831707,-5.713426,-0.014739,-4.360549,-8.058527,-2.711146,-3.708367,5.698208,-0.035235,-7.744395,-0.927799,6.038212,-3.297966,-9.592973,3.302414,7.308940,-3.043449,-4.483069,1.740753,0.835654,9.740882,-4.024699,-7.652220,7.394195,-4.209471,1.329569,-1.487793,7.348020,4.028811,9.676854,-5.951773,2.330029,-5.334986,5.135758,-5.721307,-8.608714,-5.392146,2.449165,-3.570448,5.317950,7.064367,-1.427757,7.743649,-1.431588,9.067907,-0.889951,3.381065,-5.810449,7.238155,2.496393,-5.376183,4.871283,-0.871746,7.638967,-6.333516,-6.196716,3.784910,9.750624,-2.857354,-6.472164,6.182915,1.412642,-5.290242,8.181706,5.599895,0.589442,-0.571026,-8.997508,1.606317,5.668423,-6.505762,7.320862,-0.068862,1.699334,1.830388,-1.456376,-7.616105,7.108357,-3.229005,-3.971389,9.232895,5.145681,5.163935,-1.779363,-6.747743,-0.548014,1.490244,-8.537349,-0.932023,4.044377,8.823412,-1.944634,3.626012,-2.372618,-2.904616,-4.141057,-0.762804,2.598510,6.792335,6.268422,-5.486598,6.706892,1.103914,4.788117,3.979863,6.501802,0.600040,-8.350200,4.578416,-2.642444,6.857421,0.374691,-0.334514,5.435919,8.810544,3.756321,-3.573529,4.442856,6.286242,2.577545,6.069676,3.659212,8.611831,-1.104282,7.329148,-5.182114,2.663575,-2.249314,1.225979,1.760048,-9.523186,-8.402160,0.799192,8.052507,-4.278726,7.348629,6.844921,-9.727381,-2.470315,-4.904611,0.322083,0.371092,-8.031129,3.727784,7.274027,-1.689784,8.839074,2.082546,4.912157,9.489785,0.890000,5.316283,-5.370813,7.020512,-6.549370,-5.288706,2.041171,-6.729495,2.441561,2.218940,5.525855,9.998455,-6.822636,5.527296,7.755487,9.136096,-3.862825,9.628493,4.089516,8.228639,-5.556274,9.792409,3.882704,-9.342303,1.640941,-3.726359,1.823419,-8.328551,-8.900133,4.076836,-2.124661,-9.037077,-0.949431,6.323980,0.795363,2.044979,-2.972893,8.717108,3.464540,2.127325,0.657584,2.743881,4.645375,-3.137892,5.760152,1.279520,-8.573327,-9.195568,8.065926,-8.009553,4.203793,2.584098,9.726748,3.680374,-4.715386,6.278718,-7.712616,-4.064475,-3.549772,9.489895,6.323589,-7.754200,0.272874,-6.702395,-2.398056,2.110429,-9.567714,-9.150147,3.555506,-9.668122,-7.220901,7.792673,-0.322239,-8.949770,-7.540217,1.228181,-9.861471,5.231695,-6.014488,-6.280958,8.936085,-5.618084,-0.198874,2.477050,8.604111,3.889907,8.560440,-5.400298,0.562909,6.871021,3.509619,3.648608,-0.341587,3.234705,-8.558735,9.706562,5.074005,8.553437,-5.296956,4.139891,1.763490,3.440004,3.178083,-3.488890,-2.130588,-6.636007,-8.074433,0.434560,-3.188947,-6.282255,8.615865,-6.143162,7.457361,-1.561937,-2.062956,8.432931,4.778013,3.480301,4.584873,8.383774,3.237108,1.281278,4.806093,-6.060754,7.089072,-6.398878,-5.832477,3.039470,-2.239233,-8.275443,8.977123,-6.936859,-5.694827,8.593361,-7.492942,-0.795855,-3.282831,8.870372,-0.080157,5.191845,-5.895644,-7.870638,0.292012,4.666697,-4.852680,-9.282235,2.461425,-7.618069,-7.871636,9.119523,-0.945554,-8.542524,8.803116,-5.566807,7.301359,5.451850,5.063165,1.294802,0.943995,-3.078733,-0.632280,4.345028,-9.049907,2.424112,4.650594,6.568489,-8.679366,-5.961833,0.422083,-9.027844,1.611703,5.248591,8.101300,7.047761,9.722020,-5.389329,-8.083413,7.028261,1.455725,-1.598575,-8.109906,-8.496587,4.090351,-0.187700,4.694988,-2.181261,4.559761,4.102701,-6.761255,7.059356,9.171464,5.913472,-2.246361,-4.714863,3.640987,-9.680020,-4.381005,7.628533,-1.557567,-2.607847,-6.152499,-3.225539,-0.023934,-0.276363,-0.849661,-7.049520,-0.899910,7.076219,2.184589,-9.659120,-3.435199,-4.241616,-5.902109,8.701366,9.781771,-1.267722,-4.800448,2.527463,6.433869,8.466657,-5.913602,3.358625,7.038486,8.198557,-9.747042,7.919351,-3.121760,5.950965,0.592966,0.374009,-3.921467,-1.703041,-2.127469,-3.191317,-8.884682,8.697684,6.482011,7.892149,-7.304905,5.738416,-6.371731,1.515009,-7.338946,5.161147,6.534118,5.964259,6.653246,-0.361392,8.022982,3.003694,-2.916894,-9.732604,1.715197,-5.811072,-6.135448,-2.303421,2.521794,-9.116687,-6.083340,9.968189,-0.480002,3.077615,7.694803,-0.685799,-2.750265,-0.299279,-4.246015,6.443308,-0.390235,9.997453,3.550206,9.888035,-0.655311,8.915540,-4.971005,-8.007145,9.051495,-4.243225,-9.946506,9.899647,-2.916262,9.248205,0.444580,-9.594931,7.524333,-1.708108,9.558107,3.328231,4.645197,-0.399342,5.051905,3.476042,-3.945690,0.771938,-4.985726,-6.025534,-1.485470,3.749464,-2.836661,8.747695,-2.129808,-7.992552,-4.129016,9.739334,-3.998791,2.284750,-4.714507,-8.858392,-4.214850,8.619268,1.631557,7.916668,-5.332904,8.845132,-9.356816,-1.955223,-1.113037,-1.784412,-1.938605,5.547878,2.090433,-1.124234,1.579888,-9.671451,2.546165,-9.692171,5.392591,-9.574709,-6.754491,-8.199592,6.719850,5.415086,-7.324699,-1.933981,6.553804,4.816014,-9.480377,9.808808,7.833679,6.126864,9.783738,3.186325,3.032437,-7.327362,2.991430,-4.885544,1.450918,-7.642585,1.358191,-2.070415,-8.017057,6.532659,-8.829046,-3.787087,-4.581797,-7.220634,1.864089,0.261741,5.491935,5.935123,-8.968502,9.601797,3.755242,8.524090,-5.866220,-8.407882,-6.724687,3.826122,-7.610731,-4.009087,9.184684,-0.727127,-3.404400,8.368119,-4.903301,-6.384084,-0.273992,-7.721948,2.898206,-1.929684,-3.507844,9.647560,-9.693126,4.600160,-5.082570,-0.707494,-2.027522,6.953630,-3.957881,-3.116954,9.316660,7.910545,0.543306,5.214017,-9.518843,-3.170508,-1.330424,8.985048,7.373842,0.057311,-1.545917,6.775912,0.300720,0.858063,-2.624984,-1.983523,-8.151269,3.115317,3.458322,-2.574285,5.940953,-2.627004,-5.002169,-9.426283,-1.727909,-8.299290,9.248890,8.398726,-5.535420,-9.144776,3.060695,-1.638650,5.778357,2.077221,-2.863397,-7.113683,-6.808951,-0.263307,-0.200796,-0.917644,-0.083092,3.575597,4.572841,-7.175054,9.366221,-4.045248,9.963283,-2.208668,-9.283334,-9.179125,2.580185,-7.639312,9.452579,5.419584,-8.069709,9.370027,-7.467713,-6.415509,0.629398,6.663984,-9.468646,9.946011,-5.274345,-9.565413,5.421853,2.936604,4.711754,9.154831,-2.805284,-1.964144,-9.798815,-0.397996,-5.364087,-9.129625,8.972587,-5.117072,9.288922,-5.428345,7.248426,7.951212,3.759717,2.726101,-8.338335,0.206258,4.313916,2.918087,5.764225,-3.570330,8.065134,-9.951479,-0.944497,-1.710179,-1.592500,0.420432,7.426213,4.476652,-9.916407,7.593012,9.327480,6.208589,-4.904588,-9.023180,-3.020984,5.735740,-9.080059,8.422272,-7.411221,-0.477163,-2.279859,-6.464038,-1.309730,-6.217523,-7.142858,-1.557935,-3.351121,3.242441,-4.819080,6.003225,-5.220076,-2.203751,-4.539876,-5.452277,2.345102,9.003322,-9.000293,5.966368,8.060831,3.380417,1.380142,1.413517,-8.949434,-5.704398,9.259723,4.252222,-6.794732,-5.906012,4.314436,8.697344,6.389202,-0.128374,-7.993324,9.735520,4.243156,-7.903836,-5.209242,1.452708,-6.049085,5.441407,5.216462,5.241392,4.024690,-0.001985,-9.834491,2.869568,-5.703553,-0.262949,-9.074319,9.783225,-3.638282,-8.368045,0.630527,5.223574,-4.710293,7.404029,-4.210025,7.839832,-3.824392,-1.406163,-5.818383,0.871411,-2.012863,6.350905,2.006490,-9.437421,-1.693065,-4.996909,-1.944382,0.171957,-0.571841,-0.778731,-6.133020,-5.520844,3.845631,3.753702,6.495259,5.052044,-5.087888,-0.848557,9.923731,-4.027802,7.934859,4.133642,-8.491607,-4.273059,-7.798982,5.185280,5.964654,3.008492,2.913601,-4.310513,7.644002,-9.522266,-6.183498,6.683187,2.773413,-5.740419,-1.686080,9.696401,-7.994049,-7.686773,-5.533980,2.792354,4.979298,2.693241,-4.427085,3.360629,3.728556,1.876532,-1.715832,5.706038,-1.560054,0.351973,9.262445,-1.100830,-4.828207,-7.203368,-3.722650,-7.724447,8.760524,-8.982446,3.328418,0.665349,4.824561,6.434988,-8.263845,-3.104232,-1.294949,2.811133,-9.528186,5.503975,-1.509695,9.322576,-0.150201,6.169274,0.304963,8.957216,5.441102,2.696768,9.153452,6.638676,8.527109,6.806011,7.631190,-4.999213,-5.959456,-7.039847,4.474414,3.160029,-9.880933,1.123610,0.380099,-6.521838,-0.521686,5.868844,-2.634612,0.416035,-5.692852,2.365355,1.125377,4.286525,-0.724962,9.742435,-5.133965,1.608459,7.666479,-0.403459,1.132689,7.778127,7.632939,9.724564,3.689071,0.816305,3.704378,8.535891,-8.275033,-9.132586,8.899624,9.965661,7.016420,-6.959342,5.830623,6.561999,0.306482,-9.497422,4.749109,7.489246,-2.611267,4.761777,1.822375,7.756265,7.763232,-9.549684,7.556490,-5.591319,-2.768163,1.414485,-1.095054,-6.732723,9.031708,-1.043917,2.347992,-4.369120,-1.435010,7.534614,-0.628158,-8.273527,2.048125,-4.233610,-4.668127,6.733261,1.748281,-7.948579,2.085666,-4.756314,-7.085876,4.756968,-7.089622,3.933221,8.754475,-1.365504,5.186247,-2.203816,-2.275290,6.873617,6.957379,1.980860,5.617259,-3.079116,5.031950,-0.329534,3.513894,0.943421,0.801784,0.968900,4.370633,-9.758535,-8.191891,8.199922,-1.080639,9.770297,8.942424,-9.161901,-4.957768,4.796271,5.495915,6.928269,-4.952527,-4.162595,-7.065428,-0.231180,-5.303478,-0.075932,3.593453,2.615664,6.105863,-2.308944,6.797914,1.211742,4.066729,9.201624,-4.816347,-6.738251,5.881016,-8.426061,-3.799714,-3.880646,-5.984601,0.189791,-2.903345,9.706067,6.584746,6.001672,-7.259924,-9.303820,4.393120,6.299951,6.146066,-7.451398,-5.945396,-3.000771,-2.296763,9.375833,1.157269,-0.387791,2.850569,6.527053,7.861830,-1.233300,-5.502537,-3.805442,-7.852489,3.658851,2.658182,7.711891,6.248943,-4.864084,-8.478690,-6.419314,-4.734237,7.677660,-0.411744,-4.481830,9.295940,5.000815,4.671912,-5.558564,1.675859,1.925262,9.743891], dtype = "float32")#candidate|754|(1755,)|const|float32
call_753 = relay.TupleGetItem(func_22_call(relay.reshape(const_754.astype('float32'), [9, 13, 15])), 0)
call_755 = relay.TupleGetItem(func_25_call(relay.reshape(const_754.astype('float32'), [9, 13, 15])), 0)
func_709_call = mod.get_global_var('func_709')
func_711_call = mutated_mod.get_global_var('func_711')
var_761 = relay.var("var_761", dtype = "uint8", shape = (156, 20))#candidate|761|(156, 20)|var|uint8
call_760 = relay.TupleGetItem(func_709_call(relay.reshape(var_761.astype('uint8'), [16, 15, 13])), 0)
call_762 = relay.TupleGetItem(func_711_call(relay.reshape(var_761.astype('uint8'), [16, 15, 13])), 0)
bop_764 = relay.right_shift(uop_751.astype('uint16'), relay.reshape(const_750.astype('uint16'), relay.shape_of(uop_751))) # shape=(3, 1, 14)
uop_770 = relay.erf(uop_751.astype('float32')) # shape=(3, 1, 14)
uop_774 = relay.tan(uop_770.astype('float64')) # shape=(3, 1, 14)
uop_784 = relay.cosh(uop_770.astype('float64')) # shape=(3, 1, 14)
func_385_call = mod.get_global_var('func_385')
func_388_call = mutated_mod.get_global_var('func_388')
const_789 = relay.const([-3,-10,-2,4,5,-7,-7,-2,10,4,2,-10,1,-1,-9,8,3,-10,-5,8,-6,-8,4,9,-6,10,10,-10,6,-1,-4,-8,5,3,2,3,-8,3,10,8,5,-4,7,-6,-5,-9,-6,-7,-7,-2,-4,9,5,-6,1,1,-1,3,-8,1,5,-2,9,1,-2,4,-9,7,-2,9,6,-3,6,7,6,5,7,2,9,-1,8,6,-10,-3,8,8,-3,-3,9,-3,7,6,-7,4,-4,6,2,-1,-7,-7,-8,10,-7,10,-4,-9,-3,9,-5,-8,7,3,8,-4,-10,-9,-5,10,4,8,-3,1,3,-7,-2,-7,9,-2,4,1,6,-2,10,5,-2,-2,-1,2,-4,2,4,-6,-7,-1,2,-7,-3,-1,1,-7,-10,-9,-3,-5,-9,-2,4,9,4,-6,-3,7,4,-9,4,7,4,-5,6,-5,-6,-2,-4,-4,1,5,5,-8,-1,-3,2,9,7,-6,-5,-9,-7,-3,-10,-7,9,4,5,-2,-10,1,4,-9,-7,3,5,5,3,-1,7,5,-4,-1,-3,-7,-7,-7,10,3,3,9,9,10,-2,-6,-2,6,-10,-5,9,7,10,-8,-10,-10,-8,-2,3,-9,-4,-5,-4,2,-9,8,-1,-5,-1,-3,-5,-5,-2,-9,9,-1,3,-1], dtype = "int32")#candidate|789|(252,)|const|int32
call_788 = relay.TupleGetItem(func_385_call(relay.reshape(const_789.astype('int32'), [4, 7, 9]), relay.reshape(call_753.astype('float32'), [1755,]), ), 5)
call_790 = relay.TupleGetItem(func_388_call(relay.reshape(const_789.astype('int32'), [4, 7, 9]), relay.reshape(call_753.astype('float32'), [1755,]), ), 5)
output = relay.Tuple([call_753,const_754,call_760,var_761,bop_764,uop_774,uop_784,call_788,const_789,])
output2 = relay.Tuple([call_755,const_754,call_762,var_761,bop_764,uop_774,uop_784,call_790,const_789,])
func_796 = relay.Function([var_761,], output)
mod['func_796'] = func_796
mod = relay.transform.InferType()(mod)
var_797 = relay.var("var_797", dtype = "uint8", shape = (156, 20))#candidate|797|(156, 20)|var|uint8
output = func_796(var_797)
func_798 = relay.Function([var_797], output)
mutated_mod['func_798'] = func_798
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1313 = relay.const([[[1.666199,-4.605210,-9.526358,-2.167637,3.219893,-1.023628,-1.173498,-9.837040,-7.836256,2.631549,9.035527,-4.962892,-2.670022,9.536334,-2.369043],[-2.108240,0.377714,4.112493,-9.973887,-7.436197,-3.768436,-9.805387,9.151859,2.217865,-7.499664,5.471210,1.447845,-7.533379,1.753707,9.595466],[-8.410338,-9.914106,-9.065490,-6.485356,0.106484,-0.269275,1.641983,-6.089638,6.306101,-6.790294,-3.098667,5.168804,8.820291,-2.137557,3.398240],[-8.767264,0.621241,-0.623752,-6.704098,-3.388200,6.062763,-7.321707,2.949732,6.237172,-8.877857,-3.658592,-7.615223,-1.972809,-0.061480,-3.383372],[-1.396390,1.957452,0.706678,8.042630,-5.745307,-4.009545,-1.920406,-2.740683,5.263093,6.137765,-7.860404,5.547460,2.907441,-5.013994,-4.083233],[-0.435276,-7.220839,-4.953255,2.167946,5.004046,5.864308,2.961476,-9.091984,-3.288239,-4.494879,-3.531931,4.126455,8.984397,7.002645,-3.448105],[-5.726241,7.014794,7.377671,1.112760,6.583443,-1.316712,-2.786899,7.813298,-0.206121,-4.485583,3.957988,5.840389,-3.096161,5.525082,-5.556473],[5.472210,-2.228049,2.887368,-7.900914,-1.430280,-2.598540,2.099763,2.787181,4.526522,-5.397237,-1.646685,-4.553617,-4.396245,-9.508559,8.235635],[-0.334541,5.619898,2.495243,-1.902209,3.234025,6.296270,3.725288,-2.967041,4.711277,-8.603507,-4.966888,9.669440,-1.025564,2.405606,-9.724713],[-9.016710,-3.319621,6.660153,-5.974766,0.136076,9.301574,7.211166,8.727992,0.053833,-7.442727,-4.850900,-9.309226,7.972241,-3.708511,7.226364],[0.202887,5.649263,6.628098,0.121145,-9.234857,-4.709256,-4.901823,-2.234617,6.836417,-3.167455,-6.120784,-6.803491,9.904883,0.122166,1.468674],[-1.774057,-5.405495,-8.039269,-3.436506,-0.251147,-2.736934,-0.173020,-4.518758,2.604047,-3.145641,0.981017,-1.483189,0.672387,-4.047575,8.627656],[8.025888,-3.512800,4.744786,-5.500223,5.353195,-6.110504,2.037081,-8.277282,-5.652429,5.998661,9.679770,9.814412,5.103326,4.784379,4.507235],[3.927377,-4.018243,0.339560,-2.899752,-9.436680,-7.180982,3.575334,8.564715,8.166390,9.376260,0.750034,-6.692868,2.267539,2.941833,4.636018],[5.266477,-0.781144,-0.140629,-7.333510,6.848329,-7.646415,9.209034,2.393605,0.488714,-5.721359,7.399974,-5.330290,-0.969140,4.638583,-8.413888]],[[6.117501,3.954078,-7.809018,9.621373,-7.629339,0.566862,-0.340518,0.256227,6.739219,-5.385922,1.429063,2.867719,6.578404,4.882411,-9.714902],[7.014497,-7.059469,4.893994,2.662075,3.061499,5.006780,-9.302137,0.462834,4.169585,7.195864,1.566898,8.637396,-6.220415,-7.719351,-8.106250],[0.940938,-7.725949,-8.114266,-5.177367,-8.444380,-9.178657,-8.747086,2.375419,-5.195739,0.961642,6.967277,-7.321791,0.524405,3.676950,5.386965],[-9.990177,-4.411646,-6.892234,-2.248681,-2.634519,-1.590763,-0.748990,3.845118,-9.910956,-9.440170,8.463175,-0.414122,1.082416,-2.204649,-5.376295],[-9.436985,7.760899,7.534913,2.902351,-4.703439,8.333110,-2.947479,-0.176743,3.509723,6.251289,-5.827984,8.011202,3.499097,-6.452311,-2.952362],[4.146747,-3.207811,9.754189,-7.392403,9.571260,-1.860578,7.470615,3.792614,-0.310190,-2.432898,-8.356883,2.653876,-1.244557,-9.983125,-1.025496],[4.752159,6.858275,-6.574337,7.628891,-8.296926,-7.490598,2.815121,4.951903,3.624418,-6.545609,-3.541711,-3.407379,-9.627797,-7.728074,9.829698],[2.619762,-7.826512,-4.697505,0.921445,8.988135,6.635772,-3.456939,3.277485,8.935966,-5.441013,-2.624460,-7.516500,-1.676927,4.032611,-1.051337],[0.751091,5.631706,-6.103723,6.557099,-9.617253,7.593556,-1.896008,-7.752932,-8.103732,-4.069667,3.653698,3.179646,1.565874,6.656620,-0.776329],[6.905658,3.872953,3.499880,1.046272,-9.236975,1.597788,4.352335,6.630515,6.043746,4.236608,-2.118277,-7.177936,-8.688372,8.784787,2.095963],[5.162917,-9.839426,1.076888,2.531174,-5.322025,-0.425083,6.643340,3.387711,-9.602642,-5.842703,-9.041421,-3.188010,-0.147061,-8.789003,-5.069398],[9.047510,-0.306838,9.865947,9.779610,-5.831937,-3.531920,1.873794,-1.005393,-7.878416,2.907820,-6.664348,-6.437362,1.896262,-9.653974,-5.086158],[1.174878,-9.705354,2.249326,9.637678,-5.514330,-2.349834,8.317237,5.983027,-5.175384,-7.993535,-1.931714,3.124090,0.974902,-5.542273,-3.139415],[8.410584,-9.545759,-2.547904,3.096030,8.567910,8.937238,-5.092081,6.275109,0.591354,6.823090,-6.019449,-0.304166,-3.173754,-2.425488,5.228824],[-5.973349,-4.481847,1.092008,-3.155074,-0.828458,-6.550991,-2.669679,-6.796748,-8.569014,2.397137,4.299206,-2.907030,-9.252902,-6.955710,6.338994]],[[7.686786,-7.586613,-9.847596,-1.097728,-9.585736,-2.934212,6.159392,7.587246,3.771971,3.682576,3.746189,-8.000859,-8.010293,8.970234,7.455122],[9.861718,-6.949888,-9.963979,0.601073,5.627549,2.744368,-2.428540,-7.189322,4.786803,-9.454473,8.634079,1.886849,9.293755,-9.419425,-0.229138],[8.590786,-6.600727,9.546787,-4.189773,-4.708021,-2.571627,-0.958481,-7.093060,-9.590636,-5.421977,-6.364455,0.555931,5.553941,5.692992,4.055408],[6.733992,7.210110,-4.155868,-4.781520,3.284853,-9.249742,-7.057113,5.299722,-3.212011,-6.183517,-8.758773,-7.139879,6.336639,-8.705065,9.941927],[-0.957569,-5.440535,-2.678819,8.997659,3.750212,0.470252,-6.099395,-5.525810,-2.077580,-8.904316,0.063961,9.707165,-9.833082,7.563882,-8.417099],[-9.363418,5.232084,-6.679908,4.236291,-1.533377,5.609160,-4.481259,-1.191395,9.259342,0.548977,8.178965,-2.258710,-0.980505,7.572259,6.599330],[-4.671028,2.078097,-7.180415,-2.106551,1.925749,-5.366559,-1.901652,-9.362764,-6.303067,-1.099355,4.493002,-7.723523,-8.039171,-4.511271,9.785953],[4.994305,6.593854,4.365288,0.378282,8.807860,1.014386,3.639355,7.523277,-0.699271,4.156641,6.646994,-0.639149,-4.666307,3.277543,7.785060],[-6.200305,-5.156744,4.939993,5.458088,9.485459,9.658967,-1.522991,4.142097,-4.065296,7.899318,-3.455881,2.661623,2.295719,9.081464,-6.421683],[4.888608,-4.966007,4.626564,7.433434,-5.497418,1.782398,2.008888,-8.748668,7.704290,-5.472621,-2.783625,-0.459711,-6.283062,1.981530,-9.411940],[-5.124031,-3.732447,5.717073,-2.161826,-5.202648,-6.135285,-8.878655,7.876987,-8.121443,9.979307,-9.753877,1.164850,5.808825,-4.486948,6.744615],[3.243530,-2.293393,-0.530772,3.483007,-2.189301,9.626637,2.926178,7.000223,-8.356565,-9.098632,-9.589921,8.514521,3.089678,8.251431,4.744190],[-3.914403,-3.470432,-5.895112,-1.206797,6.189522,0.452623,8.389071,-3.880180,-0.271458,-8.342926,7.841221,1.484931,-3.770803,1.236990,-7.402994],[9.400948,2.686050,0.050863,-1.294996,1.961319,-4.051043,2.681884,-1.169819,-3.304359,-1.872630,9.734433,-2.842078,0.601714,7.612992,-4.441516],[6.210677,-6.646635,-9.891705,4.393274,8.863755,-5.631502,9.501000,-9.084275,-5.317965,-0.386462,2.611211,-4.229826,-9.414894,1.900493,-0.973976]],[[7.195372,3.073626,1.903429,4.949601,-8.042521,8.113856,5.276109,-7.689827,-5.152265,-5.645425,-4.021437,-0.628005,0.411178,-2.485294,-8.001295],[2.341675,-3.618894,0.210855,-4.037645,-0.255394,-1.356915,0.983338,1.275208,5.075817,-4.372021,-7.189834,6.073082,9.743065,-3.994172,0.877656],[4.196550,-7.130255,9.331568,1.279838,3.604996,1.931336,2.341526,7.658526,-9.090146,5.002243,-4.935051,3.138091,-2.256182,6.301650,-6.306910],[-2.639959,1.777288,-2.297397,-9.127755,-2.364324,5.931910,8.847312,-1.259221,2.457943,1.284636,-5.282599,1.663642,-6.081688,-2.726428,-7.999813],[-9.953744,-6.427392,5.574217,8.744815,-2.630277,6.154045,5.112343,7.899961,8.513360,-0.417987,4.616495,4.317080,6.133322,-6.699955,4.931477],[-8.190725,4.208239,8.648117,5.551914,7.157714,-2.245227,-4.347323,2.402378,4.539961,-7.364028,-0.962498,-4.846115,-3.525670,2.334190,-4.747916],[0.113169,-6.141783,8.440472,-0.750339,-2.573913,8.822994,-8.590695,-2.327050,6.337988,8.280628,-9.328877,2.343422,7.257855,-6.651694,-7.621451],[0.136680,1.050260,2.708596,3.470675,-2.788509,4.627073,-2.357112,2.256445,7.645530,-6.669327,-4.508967,-0.451820,-9.182845,-7.325430,-2.786255],[6.412303,-5.724136,-5.314655,7.092339,8.805637,8.086889,4.647871,0.584883,2.471285,4.119820,6.085019,-3.715535,6.066828,0.242402,8.339187],[6.673698,4.567642,7.321342,6.929679,9.604914,-6.450268,9.220469,-0.754891,-0.730060,5.962525,8.344808,-4.305791,5.756038,-3.031389,9.667627],[-8.504002,-2.412597,-6.789918,4.661508,7.232027,8.554652,-6.600348,3.058652,0.859621,-2.661595,-1.716043,0.281098,4.849956,-2.226106,4.441503],[9.162296,-7.998015,6.801701,1.399833,-4.224104,9.373796,2.734828,-3.251711,-7.410807,-2.453190,0.865557,-6.770847,8.569512,3.283413,-8.184308],[4.017682,-1.605976,1.244959,1.400142,7.581653,7.562874,1.303525,-4.531121,-9.808925,9.234194,1.629048,9.821953,2.044060,4.179363,-5.994169],[0.945135,0.729966,-1.453283,4.892948,8.069633,1.468318,7.635756,5.297656,1.868684,-4.228476,1.184036,2.223824,7.254424,3.330835,3.941289],[-9.774679,-4.421563,-7.144499,7.977320,-4.451789,-9.587935,0.970851,-1.482636,2.524013,-8.940030,-8.056370,6.459570,-4.925313,-9.748568,5.987677]],[[-1.351351,-2.413534,5.253888,2.258852,-5.038520,-7.461928,6.952096,-2.272237,-5.927831,4.672100,3.327937,-8.491328,3.369904,1.853798,6.968188],[8.685361,4.016502,-1.593509,2.645559,9.362989,3.180863,-7.019355,2.029762,-1.656079,2.160436,2.999009,1.151411,4.106996,-4.532794,-0.920660],[-2.198607,5.739804,0.162219,-0.135509,0.112962,-5.477954,7.233182,-9.765627,9.890084,4.753895,-5.795576,3.965323,-2.325403,2.767479,9.571238],[-5.062631,8.826514,4.524073,9.538097,2.462312,3.056053,0.210196,2.633005,-1.581259,-0.422782,9.013302,-6.160401,-3.205434,9.433189,5.680617],[2.755359,-5.824135,-6.227175,0.001017,-1.803601,-5.349715,-6.379630,-4.218615,6.020016,-1.038344,-4.522408,2.143598,-9.129076,-8.981873,2.249944],[5.002886,0.379577,1.413474,0.929466,-2.396503,-2.971539,-2.622623,-4.228655,-8.994889,5.294606,-5.042163,-5.237601,-6.672408,3.452561,-6.512154],[-6.268322,-7.067270,-8.705580,2.866626,-9.938942,6.723560,7.366197,-8.930364,-3.464879,4.014315,8.090803,-2.638361,4.545184,7.494166,8.688286],[7.144212,0.870764,5.582209,-2.084483,9.762138,-7.423717,9.616911,-5.769833,-9.517644,-0.414051,-0.290768,1.229208,6.857261,9.262559,1.465649],[-7.332867,6.191735,-8.696243,6.467383,0.476932,-1.814227,7.741387,8.478746,3.428470,5.562184,-3.304190,8.294866,-6.784289,-2.222662,0.807635],[-6.208042,3.982310,5.842519,-6.519053,-7.067097,-6.503013,-9.984453,-0.674146,0.640238,8.091407,4.530932,3.835652,0.765357,4.256805,6.803902],[9.309080,-8.893624,2.574991,2.448247,3.432913,-8.155234,-5.758304,6.156981,-4.420502,-2.083271,7.779111,0.203693,-6.479504,-2.233883,9.164230],[2.148844,6.803385,5.844672,9.998458,0.677905,-4.928042,-6.138021,-7.838926,4.327439,1.004451,-2.856491,9.140901,3.091898,-3.967728,2.132970],[6.507986,-1.437033,-9.804363,-2.699918,-8.392754,-0.823754,1.850550,9.149962,4.946401,-7.732720,-2.107012,1.185851,7.840813,-4.823986,4.194437],[3.612526,-4.409429,9.398542,5.860331,-6.335723,1.136667,-0.475917,-2.761300,-2.081163,-2.515966,-5.812012,6.265321,-8.499530,-5.104922,-6.643479],[-5.940498,-3.101728,-5.595139,0.884989,6.747239,8.307003,1.078624,4.841384,-3.005997,1.757091,6.937868,2.366978,4.939889,5.370451,-9.966209]],[[1.861890,2.746410,1.702736,-5.505373,1.202233,9.804289,-2.386908,-6.344045,-0.430376,-7.685383,3.404731,1.340721,-2.396747,-8.153858,-8.327711],[-6.233416,1.952674,0.336884,6.119952,2.478353,-9.527980,3.661025,0.773386,-7.684006,-3.307959,9.257373,-6.775898,3.621158,-7.360166,-5.197324],[-9.636251,-2.316531,-3.849074,8.840055,7.377079,-5.872048,2.669145,6.760008,5.170673,-2.676451,-0.347981,3.994218,-6.987115,6.629940,-4.316320],[9.041577,-5.567892,-8.349628,2.563292,-4.318730,5.534452,-3.647243,8.108733,4.006421,-0.620993,-3.120037,-8.493682,6.520675,-8.417317,9.340077],[5.390190,-8.472131,-4.005968,-3.989223,-6.203506,1.390377,-5.381502,-0.939888,1.909111,-8.950662,4.731438,-9.407867,5.054732,-9.377901,-4.702168],[-2.577419,-5.204427,-7.421965,-7.972890,-0.438937,9.441826,-8.884089,-8.135166,7.251595,-7.482709,7.271748,4.928815,8.352513,5.143620,-1.880459],[5.503152,6.609932,7.396795,8.961136,6.000250,-6.151717,0.983644,-6.119212,8.943058,2.973823,5.975788,2.912465,-7.699680,5.350803,-9.618089],[7.269979,4.277877,9.434887,-2.163368,-2.923630,8.948472,7.861138,5.763103,-6.496546,5.639306,-3.625595,-6.561869,3.245401,6.311319,-0.453411],[0.401981,5.164420,4.022129,6.576874,3.174307,1.245302,4.404995,7.384020,-7.811562,3.992519,3.439141,-7.259872,-6.917533,-3.008449,0.840605],[2.452163,9.042623,9.735145,-5.217354,-5.122349,-2.673086,-0.799113,-1.260422,-8.485521,3.234163,0.524121,1.279743,-2.941820,6.648358,3.175778],[6.342220,2.789609,-4.125951,9.272735,-3.212809,-8.278471,9.486806,-7.883112,2.348599,-9.387729,-1.744681,4.236744,-3.850662,5.675344,9.476672],[-6.058051,-2.262177,1.126040,-3.697656,6.770764,-0.025146,9.593837,-9.908379,-5.750079,-1.287393,-6.445609,-6.300512,-3.114144,5.941068,-2.485662],[1.977280,7.124138,8.675712,-5.445307,-1.717997,-7.499247,8.366089,-5.874570,4.587055,5.476452,-5.228000,-7.272043,-1.647276,9.380553,4.705525],[-7.905551,-7.076554,-2.770484,-2.944543,9.848629,-1.293582,1.447954,9.408944,2.461303,-5.876000,-5.404799,-5.435633,7.194311,9.605696,-2.092507],[5.754938,0.698920,-8.852515,2.174577,-8.104021,3.516955,-6.454998,1.751554,4.750466,-7.717175,8.118271,-5.770133,9.659683,-6.252570,-8.602053]],[[3.535689,5.692230,0.018410,-1.798221,-4.885460,4.809447,4.656589,6.004367,5.635790,5.446402,-0.020719,-1.769039,-3.444431,3.461850,-0.141080],[0.457747,4.637816,6.004493,4.137593,1.653303,-2.258510,9.724604,-9.989836,-0.876373,1.745209,2.780348,9.745664,-4.554276,0.125703,-2.777862],[4.416311,-8.713785,1.929734,6.097515,2.389098,-4.614915,9.670879,-4.879719,-7.287370,1.509674,-8.538091,-6.099103,-1.036687,-5.109852,-6.252567],[-1.794061,-5.626676,-9.085541,-6.959272,-5.429390,-4.565124,4.321231,7.582052,8.073563,8.553524,5.668295,3.515990,7.549207,8.499141,0.120621],[-0.253888,2.681671,-4.107659,-5.669988,-4.587094,1.300571,-3.468507,-6.945478,-2.265134,3.123264,3.462664,4.344053,-3.159847,-7.578905,-7.605034],[5.450111,4.406189,-7.942861,-2.306910,-1.672736,1.886029,1.874978,1.842936,8.050622,1.784745,4.459377,-7.257119,4.964429,0.381098,-1.171910],[-5.518207,-1.614688,-8.847528,9.427346,-5.882276,0.390843,1.392566,8.526506,8.632126,-7.476542,0.366159,9.841588,5.217049,8.079085,-8.680251],[-9.565370,7.251265,9.976851,0.844009,3.785435,-4.178716,-3.161067,0.541495,-3.325983,-2.881381,-9.505016,-6.756885,7.075120,-4.882035,-7.259924],[-7.221646,7.340215,-4.320961,-0.131362,-4.361647,5.038959,-6.225689,-3.225952,2.130781,-1.542694,-4.397122,3.774854,-7.535388,-7.295984,8.106669],[-9.774623,5.288971,-6.742739,-5.000427,-3.355128,-5.262014,9.965732,2.002172,-1.514172,5.676409,-4.976172,8.511113,-7.309918,9.532415,2.523251],[-5.012344,-3.431378,5.703456,6.962470,5.975267,-9.443239,3.381500,9.444905,-3.559215,4.029675,-2.005388,5.985590,6.236571,-4.001899,-0.249006],[-7.777894,3.978688,-5.990719,6.888324,-8.353268,7.190422,-8.033030,-9.129083,1.962045,6.496533,-2.494798,5.906655,-7.767142,-2.815297,0.846762],[-5.719375,7.871097,-7.594435,-7.645398,7.740453,8.031797,-3.025558,1.546441,0.332469,4.911280,6.376442,-9.872546,4.474098,4.395010,6.247248],[-0.844057,-2.664828,2.838523,6.222684,-8.501236,-8.094888,-8.807408,2.520582,-1.989285,-8.753200,-5.548583,7.289607,-7.980741,1.882341,-2.427992],[-2.952930,-8.194904,-7.413462,-2.374555,9.388837,-0.935615,-8.326145,-4.962220,-7.696725,-0.499185,-7.600235,-7.722877,3.173440,-0.293675,6.451909]],[[-7.676839,0.982576,-5.404204,-3.001998,-8.798745,-3.963883,-7.088580,0.683940,-0.305914,4.123237,-4.387473,0.960049,9.505530,-0.495676,6.969352],[5.992221,7.673713,-9.323462,-7.040087,-0.096638,3.147096,-4.410005,1.898072,-0.061948,4.480505,-4.087133,-0.197501,0.247089,1.236885,9.904643],[8.351314,-1.969572,-5.097051,-4.319953,1.464100,3.222682,1.762268,-3.763238,3.235262,7.093281,-9.093396,-7.115660,2.575001,4.268062,7.757063],[-2.330292,5.961394,-0.017270,5.561137,-6.147308,0.896554,9.124420,0.931241,-1.887177,3.532875,-9.869985,9.425833,-3.953044,-1.780487,9.628215],[-1.742134,-2.265734,-6.277690,3.137726,8.349876,8.740684,8.378970,-1.362643,-2.225869,6.444862,-6.831701,-0.043565,3.869723,-6.967813,-7.456843],[7.242900,0.916595,-8.656869,-7.280311,-7.131177,5.277243,6.259443,-7.036415,-5.918112,-3.798885,-9.430665,8.097861,-3.680236,4.744851,-7.891997],[6.553656,5.703280,5.741704,-2.527812,9.283479,8.596011,-9.174939,-5.030881,-8.940755,-7.457087,-4.428250,1.083796,9.021079,-6.419686,2.857999],[-9.472402,0.818385,2.640338,0.888115,-8.197697,-9.994845,0.490802,-2.521517,-3.868106,-8.324553,1.547888,3.959307,-2.764742,0.591313,-2.315735],[2.331342,6.980770,-6.213183,3.570605,-8.160249,-6.649311,-2.073586,-2.259148,8.753056,7.048494,3.642165,8.473775,-9.024620,7.362155,-2.837271],[-7.448928,-0.041226,-8.634541,-0.760934,-7.737473,-4.940978,-0.111599,-7.134796,4.606663,6.984025,-0.624364,-1.032050,1.132063,0.463072,-2.900531],[-6.075221,-6.371844,-2.759558,2.442641,-0.789947,9.108436,8.047951,4.782348,-9.071297,3.945455,-0.017334,-9.965453,9.948118,8.151630,-1.210516],[4.153213,-5.575809,1.560818,-9.396402,4.219771,-9.958542,8.296402,-8.844703,-7.940765,-9.763649,-3.013001,4.347447,9.090969,9.302449,7.943749],[-8.260907,-8.209118,-6.661814,4.347213,0.905674,-5.116371,1.369012,2.811410,-3.704875,5.497965,0.417979,0.722413,-2.734452,-5.549898,8.984183],[-9.852532,-0.478679,-0.307154,-4.295429,8.385339,1.364967,-2.106247,-2.771129,-4.838724,0.707666,0.201341,-8.175805,0.714745,2.285087,-1.988442],[4.237180,-8.206640,9.371519,8.189761,-8.827855,3.898738,-0.066730,-2.866526,8.424469,4.808483,-4.309230,-8.087418,-3.615882,-6.976558,7.851833]],[[-4.171762,7.247529,-9.974614,-7.134102,-7.924349,-8.121939,-3.710180,7.128875,5.835110,5.310838,4.012825,1.320792,-4.081505,1.897939,6.642507],[3.546023,-3.862569,-4.893040,-0.424991,-3.720642,0.120082,-4.316051,5.315649,2.604652,9.040369,1.341472,-8.956627,-0.408952,-9.126251,6.122197],[-7.978175,-4.039333,8.667221,1.757500,2.848792,5.986736,-0.092226,-3.730338,5.670944,3.849568,-4.579871,-0.942199,8.734908,-7.291680,-8.173056],[-8.197998,-3.464871,1.614982,8.126937,3.860436,-7.968888,-1.381724,0.694153,-0.615037,-5.187711,4.561568,3.161592,5.555945,-3.876099,-4.797791],[-7.170247,5.731016,2.531413,-4.363687,4.581458,6.065285,-7.783886,-5.454439,-5.258427,2.350225,-3.055068,-4.293007,-0.572730,4.665422,2.302473],[3.148389,-1.193924,-1.102982,-9.182183,-0.661256,8.241302,3.652362,4.185908,3.909116,5.675291,-7.587945,6.529657,7.837701,5.612941,-6.965373],[-8.892964,-1.355648,-5.385908,1.483144,5.848478,-1.710410,6.962264,6.795682,0.814126,2.058753,0.987764,4.886537,-0.172971,-6.602424,6.038989],[-7.799162,-9.282942,-4.381389,6.049966,1.147732,2.709584,6.290330,-4.493567,-3.336081,8.054512,-4.412401,8.967775,8.094215,-5.049605,7.329021],[-2.350799,7.352131,-8.731057,3.259522,4.920324,4.458087,-4.158971,-0.644895,6.113293,8.168342,-8.664771,3.245633,2.804411,1.082889,-9.528145],[9.945876,-8.948642,4.905506,-9.028203,-9.650013,-3.849636,-5.419384,8.484119,1.983149,9.767335,1.548426,-3.495068,-4.072497,-2.895668,3.292214],[-8.597958,3.084875,5.184452,-0.755237,-5.719788,-2.162312,-3.022019,4.567839,0.020081,-3.264156,4.233342,-5.422787,-8.346626,6.846048,-5.608124],[9.380317,1.867399,0.842786,5.748568,-3.199874,-5.451042,-0.021263,-5.178190,-4.193250,-7.544613,-7.377866,5.176363,0.984197,5.632127,-6.965081],[7.185541,8.625334,-8.540059,-4.624226,-8.617459,5.767315,0.075365,0.920215,-3.988790,2.133942,-3.024198,-1.590171,-6.558090,2.624837,1.169778],[9.737115,0.342962,6.573316,4.675381,5.606201,6.389703,-0.581663,3.848907,-0.362235,-2.829119,-1.444146,7.787991,-8.781917,2.568344,-1.998950],[6.623705,3.599251,-4.192258,-0.584566,-9.316815,6.979647,4.054273,-0.047370,0.596230,-5.795890,-1.103828,-3.327410,2.154241,6.433706,-0.328135]]], dtype = "float64")#candidate|1313|(9, 15, 15)|const|float64
uop_1314 = relay.sinh(const_1313.astype('float64')) # shape=(9, 15, 15)
func_385_call = mod.get_global_var('func_385')
func_388_call = mutated_mod.get_global_var('func_388')
var_1319 = relay.var("var_1319", dtype = "int32", shape = (252,))#candidate|1319|(252,)|var|int32
var_1320 = relay.var("var_1320", dtype = "float32", shape = (1755,))#candidate|1320|(1755,)|var|float32
call_1318 = relay.TupleGetItem(func_385_call(relay.reshape(var_1319.astype('int32'), [4, 7, 9]), relay.reshape(var_1320.astype('float32'), [1755,]), ), 5)
call_1321 = relay.TupleGetItem(func_388_call(relay.reshape(var_1319.astype('int32'), [4, 7, 9]), relay.reshape(var_1320.astype('float32'), [1755,]), ), 5)
func_22_call = mod.get_global_var('func_22')
func_25_call = mutated_mod.get_global_var('func_25')
call_1327 = relay.TupleGetItem(func_22_call(relay.reshape(var_1320.astype('float32'), [9, 13, 15])), 0)
call_1328 = relay.TupleGetItem(func_25_call(relay.reshape(var_1320.astype('float32'), [9, 13, 15])), 0)
output = relay.Tuple([uop_1314,call_1318,var_1319,var_1320,call_1327,])
output2 = relay.Tuple([uop_1314,call_1321,var_1319,var_1320,call_1328,])
func_1341 = relay.Function([var_1319,var_1320,], output)
mod['func_1341'] = func_1341
mod = relay.transform.InferType()(mod)
var_1342 = relay.var("var_1342", dtype = "int32", shape = (252,))#candidate|1342|(252,)|var|int32
var_1343 = relay.var("var_1343", dtype = "float32", shape = (1755,))#candidate|1343|(1755,)|var|float32
output = func_1341(var_1342,var_1343,)
func_1344 = relay.Function([var_1342,var_1343,], output)
mutated_mod['func_1344'] = func_1344
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1409 = relay.var("var_1409", dtype = "float64", shape = (16, 5, 2))#candidate|1409|(16, 5, 2)|var|float64
uop_1410 = relay.acosh(var_1409.astype('float64')) # shape=(16, 5, 2)
output = uop_1410
output2 = uop_1410
func_1423 = relay.Function([var_1409,], output)
mod['func_1423'] = func_1423
mod = relay.transform.InferType()(mod)
mutated_mod['func_1423'] = func_1423
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1424 = relay.var("var_1424", dtype = "float64", shape = (16, 5, 2))#candidate|1424|(16, 5, 2)|var|float64
func_1423_call = mutated_mod.get_global_var('func_1423')
call_1425 = func_1423_call(var_1424)
output = call_1425
func_1426 = relay.Function([var_1424], output)
mutated_mod['func_1426'] = func_1426
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1593 = relay.var("var_1593", dtype = "int64", shape = (4, 10, 3))#candidate|1593|(4, 10, 3)|var|int64
var_1594 = relay.var("var_1594", dtype = "int64", shape = (4, 10, 3))#candidate|1594|(4, 10, 3)|var|int64
bop_1595 = relay.maximum(var_1593.astype('int64'), relay.reshape(var_1594.astype('int64'), relay.shape_of(var_1593))) # shape=(4, 10, 3)
output = bop_1595
output2 = bop_1595
func_1598 = relay.Function([var_1593,var_1594,], output)
mod['func_1598'] = func_1598
mod = relay.transform.InferType()(mod)
var_1599 = relay.var("var_1599", dtype = "int64", shape = (4, 10, 3))#candidate|1599|(4, 10, 3)|var|int64
var_1600 = relay.var("var_1600", dtype = "int64", shape = (4, 10, 3))#candidate|1600|(4, 10, 3)|var|int64
output = func_1598(var_1599,var_1600,)
func_1601 = relay.Function([var_1599,var_1600,], output)
mutated_mod['func_1601'] = func_1601
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1620 = relay.const([[[-1,-10,-10,7,-2,2,5,3,-10,6,-10],[4,9,4,6,8,10,-6,1,-2,4,10],[7,-9,-4,6,-5,9,10,4,7,-5,9],[7,-5,-3,-2,-8,-6,8,6,-6,-4,7]],[[-10,-4,-2,-4,-2,-1,2,8,6,-5,-5],[-4,6,-5,7,-8,4,4,1,-9,10,2],[3,-6,-5,3,5,-4,9,3,3,3,-3],[3,6,9,-1,6,10,-5,4,-7,-7,-1]],[[-10,4,-6,-1,3,-5,6,-3,-6,3,4],[2,-9,-6,-2,5,-1,-7,4,-8,-4,6],[-10,8,-9,-3,-2,10,6,8,-4,1,-1],[-4,8,4,6,1,8,-1,2,-1,-1,-4]]], dtype = "uint32")#candidate|1620|(3, 4, 11)|const|uint32
var_1621 = relay.var("var_1621", dtype = "uint32", shape = (3, 4, 11))#candidate|1621|(3, 4, 11)|var|uint32
bop_1622 = relay.multiply(const_1620.astype('uint32'), relay.reshape(var_1621.astype('uint32'), relay.shape_of(const_1620))) # shape=(3, 4, 11)
func_796_call = mod.get_global_var('func_796')
func_798_call = mutated_mod.get_global_var('func_798')
const_1628 = relay.const([-5,-3,-10,3,10,-6,6,7,-3,-9,-10,-6,6,-10,5,2,6,4,-10,7,2,3,5,-3,3,-9,-4,7,4,-7,-3,-8,4,6,-10,6,-8,9,8,-4,-4,3,-8,10,-6,-1,-5,9,-1,-5,-9,3,1,9,-4,10,5,-7,-2,5,3,-8,-2,-10,-3,6,-6,-7,10,6,-10,3,-10,8,-7,-1,-8,-1,-7,7,-5,-3,-3,6,10,-9,-8,6,3,1,9,-4,-10,-9,-5,-8,9,-9,-4,6,-9,-4,7,7,6,-2,10,1,-1,9,-7,4,10,6,2,-8,9,2,-2,6,8,4,-1,10,-7,8,7,10,9,1,-10,-6,1,-2,8,-10,5,-6,8,10,4,9,-2,-9,5,-4,-1,3,-8,-4,3,3,-7,-8,-3,-2,6,10,-10,-1,-9,9,3,1,-9,8,-8,-1,9,3,8,1,-9,-4,-10,-6,-9,-10,-9,4,5,-9,2,-9,1,-3,9,3,-6,9,-3,4,9,2,4,-5,9,-1,8,-2,-4,-6,-2,3,9,2,6,-1,2,7,1,-7,8,3,-10,4,3,-10,-2,-1,-6,10,10,1,7,10,-9,-10,4,4,-10,9,10,-6,-2,-1,1,10,-5,5,-8,9,3,6,-5,-1,-9,-8,-10,1,-5,-10,-4,-10,-3,8,-4,-9,-10,-4,7,2,8,5,6,9,8,10,4,-10,8,8,-9,-9,-2,-2,8,5,3,3,-9,5,-4,9,6,4,-9,4,-9,-5,-5,2,-10,-7,-10,-6,-3,-4,5,-6,3,5,-10,10,-3,10,1,-9,-10,7,9,7,-4,2,4,-2,-5,1,-5,7,-5,6,-1,-10,-5,9,2,-9,-6,-8,6,1,7,9,4,-2,2,-6,2,4,-5,-1,-8,3,-1,4,3,1,7,3,-7,-2,-2,-4,6,-2,-8,6,-5,-9,2,-4,-9,4,-6,-9,2,1,-10,6,2,5,-3,5,-1,-4,10,-7,-4,6,8,2,9,-3,10,-4,-9,2,1,-2,4,7,-6,2,7,-8,5,6,3,10,-1,6,5,-6,5,-1,3,-10,4,7,-10,-6,-6,9,-4,-3,-5,-4,6,9,7,-10,-7,1,4,3,-6,-1,3,-2,-10,1,5,-8,-7,-2,-6,-9,5,-6,-10,3,2,-8,3,-2,-6,-10,2,2,4,4,-8,-5,-2,10,-4,8,6,-8,6,3,7,-3,-1,8,10,-9,4,-1,-7,-10,3,-4,6,9,-6,-5,6,-1,4,-4,1,5,7,4,7,4,6,1,4,5,2,2,-10,5,-2,2,-2,1,-3,5,10,1,1,-7,2,4,4,2,-9,-9,7,6,-8,-3,1,2,9,-7,-7,-5,8,5,-5,5,-5,7,-6,3,10,-5,-4,-4,2,3,-6,8,-6,-6,-1,5,5,-8,-6,7,7,-9,-10,-3,-6,2,5,-8,5,1,4,2,9,2,-2,-3,10,-1,-7,-5,-3,5,-8,-8,-6,3,-5,9,6,1,-10,-1,6,-3,8,-6,-6,6,5,-1,3,10,8,3,-3,-3,9,-5,6,8,7,-3,-6,-9,5,1,-3,-7,2,-4,-6,-10,-1,-10,5,10,-1,-7,4,-9,7,8,-10,-10,6,-9,-2,-9,-2,-1,6,-8,-6,5,2,-10,3,10,4,-8,-5,5,4,4,3,-4,9,-8,-9,-7,-9,2,5,-7,-4,-9,2,8,-10,-3,-10,-1,-10,-3,4,-10,7,6,3,-10,10,6,5,-9,8,7,-10,-6,9,-7,-9,7,10,7,1,-10,7,5,2,5,8,10,10,8,5,-4,4,-8,7,10,1,8,-8,9,9,-1,-8,4,-7,9,10,4,-7,10,8,-3,-10,8,-6,-9,3,-1,-1,8,7,-7,1,3,-6,1,5,-4,4,4,-10,-4,-10,-1,10,-8,7,6,-1,-5,5,10,9,-4,7,-3,-10,-8,-2,3,8,-8,9,4,-6,6,6,-1,1,10,-5,2,1,-6,-9,-4,-10,-6,8,-10,1,-6,-1,6,4,7,10,-3,-1,4,9,9,-10,-10,-6,-5,-8,6,9,1,-9,-3,10,-7,-8,-3,9,-6,-8,1,9,-1,-10,6,2,-3,8,7,5,-10,-7,7,6,6,2,-8,-5,7,9,-5,3,-9,5,10,1,2,-7,-3,2,7,-9,6,3,9,9,10,-1,4,4,-5,-5,3,6,5,7,4,4,-10,-5,10,1,7,-8,8,-6,8,-10,3,7,5,-9,-10,1,1,-8,-2,-10,3,-2,3,5,-9,-10,-2,2,3,-8,-6,4,5,-10,-3,7,-10,10,-7,5,-2,8,-4,-3,4,9,-10,-9,4,-3,-2,6,1,7,1,-4,9,-8,6,1,3,-10,-2,8,-2,7,-3,-8,-9,4,9,2,4,2,-3,10,2,9,-10,-1,7,-6,1,7,-1,9,-1,-9,-2,4,3,-1,3,10,-4,8,1,4,-2,-1,3,2,-2,8,-3,9,-6,2,8,-7,-2,-6,2,4,-2,-6,6,9,-10,-2,-9,8,1,7,9,4,10,6,-9,-4,9,5,10,3,-3,3,-8,-9,9,2,1,-1,5,3,-10,-6,8,4,7,8,-4,2,-9,5,-9,8,-1,3,8,2,4,7,-1,-2,10,-10,10,-10,-5,9,-10,-5,5,10,3,-1,10,-1,-1,-1,2,7,5,2,-2,3,-7,-4,-6,6,-6,6,-7,1,9,-10,5,-2,-5,-8,5,-9,-2,5,-9,5,7,3,10,1,6,-8,-1,1,5,2,-3,-2,-6,-2,5,-10,3,-6,9,-10,-1,8,-1,7,-8,-5,8,9,2,8,-1,2,4,-4,-7,10,5,9,4,-1,5,-7,-5,6,8,-7,-4,4,6,3,-4,-3,-8,4,-8,-6,5,7,-2,9,9,-10,4,-1,1,8,-4,4,-3,3,5,6,5,-10,-6,-8,5,-8,-9,3,-4,7,10,-9,2,-6,-5,9,-6,8,7,7,-1,5,5,-4,-7,-6,-2,1,10,3,10,5,10,-7,9,-1,10,-2,3,3,-9,-10,3,7,9,-9,1,-6,-9,-1,9,-1,-7,-4,-1,2,-6,-10,-4,-4,-6,-5,-9,1,-3,8,-4,1,-4,-4,5,-4,10,4,1,-10,-3,8,-3,-3,9,10,-10,7,-9,-6,8,-5,-4,-4,-7,3,-9,-5,8,-1,-7,2,-4,-1,1,7,-9,-8,1,7,-6,1,1,-8,-2,-8,1,-8,1,6,-9,1,-5,-1,3,-8,10,6,3,-2,4,6,2,-8,3,4,9,10,-4,-4,-8,-6,10,-2,6,10,4,5,9,-8,9,6,7,6,6,-6,10,5,-2,5,-10,7,-10,-7,-8,-3,7,7,-3,5,2,-6,-3,-2,-7,-4,1,-9,6,2,-3,10,-2,3,-1,7,-10,-4,3,10,5,6,-5,-7,-3,6,-3,7,3,-5,10,8,6,-3,-9,10,6,10,-3,4,-7,1,7,7,9,6,3,-9,5,-7,-6,-10,5,4,8,-3,8,-7,3,5,-6,-3,-3,8,-6,-2,-4,-3,-2,-8,-4,-7,4,-5,10,10,9,4,6,1,9,-4,-6,5,-3,10,1,-2,-5,-5,-7,10,-8,9,8,-8,3,-1,1,1,-8,-3,-2,5,2,-10,-7,-6,-7,-1,-6,2,-2,-2,-1,-7,4,10,-7,-1,7,9,-6,-8,-1,-7,-7,8,-4,-2,-3,-3,-1,3,8,-8,-7,-8,1,5,-3,10,-1,-1,1,9,-4,-1,5,-4,7,-9,-6,-9,-1,10,-9,5,-9,3,2,3,4,3,-7,-4,7,-3,8,-2,8,-4,2,-7,8,10,1,5,9,-5,-5,3,2,-8,9,1,2,6,-7,-5,-2,4,-10,1,9,8,-6,-7,-8,-1,5,-8,-1,8,-9,2,10,7,7,9,-5,-1,7,-9,2,-4,6,-1,8,5,-4,9,3,2,-5,7,8,-10,5,-2,3,-2,-7,6,-4,-1,5,2,9,1,7,-3,-7,9,-6,1,-6,8,7,9,2,10,1,7,-6,-5,8,7,2,-9,9,-10,2,8,-10,3,-8,-9,-6,10,-9,-6,-2,-2,1,5,-1,4,-10,5,9,4,-2,6,-1,2,1,7,-3,8,-2,3,-7,-1,1,-9,-5,-10,7,-6,4,8,-8,-9,-8,2,-1,7,3,-8,-5,7,-1,-8,-4,-7,-4,4,-4,2,1,1,-2,3,-6,10,-10,-3,5,-9,8,9,-3,-6,7,6,-4,3,7,1,-7,-7,1,9,-1,-5,6,-3,-7,5,-8,4,-2,-10,-5,4,-6,-10,-1,1,9,1,1,4,6,4,2,8,8,-3,-2,4,8,-3,3,10,-3,7,6,4,3,-8,9,-1,5,-8,2,5,6,-10,-3,2,3,7,-3,3,-10,-4,-6,-4,10,-10,-3,-4,-2,-7,7,8,-9,9,-8,9,-3,7,-10,2,4,-4,-4,6,-5,10,2,-1,-3,-4,-5,10,-8,9,7,-7,3,10,2,-5,10,-10,-3,5,1,8,-4,6,-5,-9,-6,5,-10,9,10,-10,1,-3,10,10,-9,9,-7,5,-2,6,5,-9,6,-8,4,-9,9,-9,9,-10,8,-2,-6,6,-3,6,-4,4,5,-8,-9,5,-8,7,-4,6,8,-6,4,2,4,7,3,8,1,-8,-3,-10,-7,-8,6,2,1,8,-10,5,8,-10,1,-10,5,7,-1,1,-6,1,-3,5,1,-1,4,2,10,-5,-1,-5,1,6,-1,-1,6,-10,-7,6,2,8,5,-10,-6,-6,-7,5,5,1,-6,4,8,-2,-2,-2,6,-10,2,6,2,4,4,-9,-9,-4,5,-1,-3,8,1,-10,10,10,8,9,-9,-9,-2,-2,1,8,-6,-10,3,-6,8,3,-4,9,10,-3,-10,-2,3,3,-9,-1,-1,-8,9,-9,2,2,-7,-9,8,4,4,-10,9,2,-8,5,-4,-6,-8,7,-8,-5,1,-10,6,8,-3,1,-6,1,6,3,-10,-2,-3,8,9,6,9,-10,3,7,8,5,-10,8,-2,-5,-10,-3,-7,6,-6,7,-10,10,-7,-7,-2,-9,-1,-8,9,-9,2,6,3,-7,-6,-2,-1,10,-9,3,3,4,10,-9,7,10,10,-9,7,1,10,2,8,-9,10,8,5,-7,6,-6,6,4,-1,10,-1,-5,-6,2,6,-1,-5,-10,-3,-5,-7,-3,8,-10,2,-1,2,-4,1,-2,-9,-5,-10,-5,6,-3,3,-7,-5,10,-8,2,6,-8,-4,-4,-1,-7,6,5,4,-4,-4,-7,-7,-6,-9,6,-4,2,3,1,5,-9,2,2,4,2,-6,-8,-8,-9,-3,-2,-9,7,10,-8,-7,-5,-2,6,2,5,7,-2,-8,-1,8,-9,6,1,-5,-1,7,-3,5,-7,7,7,-7,-8,4,7,-1,-10,-4,4,-1,4,-3,9,6,6,-1,-7,6,3,-3,3,-9,-2,6,-2,1,7,5,-9,-3,4,10,2,9,5,8,-7,-2,9,4,-7,7,6,-1,3,-2,9,2,-7,9,-2,-1,-3,7,3,3,-4,-3,2,-7,-7,6,2,-9,7,-2,-4,-8,-6,-1,4,-8,-6,-9,4,-5,-7,-10,7,10,5,4,3,-8,-5,-7,-5,-7,5,-9,-6,-3,-5,1,-10,9,3,7,-3,4,-6,-9,5,1,-4,10,-5,2,-5,6,-6,-3,6,2,6,9,8,-4,6,4,6,-1,-6,-4,7,-8,-7,-9,-10,-4,8,2,-3,-10,4,8,-7,-2,1,-4,8,-1,-3,-7,1,1,7,7,2,7,-1,-5,-4,-9,-4,5,-7,8,5,4,1,7,-1,-5,2,-8,-9,-1,-1,-9,-5,1,-1,3,6,-3,-5,4,7,-8,3,1,-10,-6,3,7,2,-4,-7,-10,-4,-10,3,4,3,-8,7,-10,-4,-7,-4,8,2,-10,9,-4,2,2,7,-7,10,-9,-9,-6,-7,-1,-9,8,1,2,9,10,9,-1,10,9,5,6,8,4,-5,6,-6,-7,4,4,3,-7,8,1,5,-7,-9,-2,-5,4,-5,-3,-7,-5,-10,-6,-3,-7,10,6,-7,8,5,5,-8,9,-1,2,5,-9,-6,-7,-10,7,-2,7,-7,-9,5,-2,5,6,-8,-4,-8,7,9,-3,10,-9,5,6,-9,6,-9,8,-4,7,-5,-4,-3,-8,-6,-9,3,3,-2,-1,3,6,8,3,-8,-3,-1,-7,7,-7,6,-1,6,6,4,10,7,-7,-1,6,-3,6,5,10,-1,-4,7,-6,3,10,3,3,9,4,4,-3,10,-3,-3,6,-2,-10,8,-3,-2,-8,-4,-3,-3,-6,7,-4,-7,2,9,-1,-10,3,9,-9,-8,3,8,-6,-3,9,-10,-8,9,-6,-10,1,-1,8,-10,-10,3,-10,-9,3,-9,-5,5,-7,-5,-3,3,7,-10,-2,3,7,-5,-1,3,10,8,10,-9,6,-9,3,4,-6,8,-5,1,-8,-8,3,-5,-1,8,-4,8,3,2,-9,-7,-3,4,5,-9,-2,-4,-8,9,1,3,-4,-9,10,4,-8,-6,-3,8,-4,1,-3,2,-3,3,8,-1,-6,-1,2,6,4,2,2,7,6,-3,-2,-2,-4,1,10,-6,4,3,-3,-5,-2,-8,6,2,3,3,-8,2,-10,8,7,-6,-3,7,9,5,-9,-8,8,9,3,7,-8,5,-4,-10,7,9,7,6,-8,-7,-5,5,5,7,7,9,-2,5,-9,6,3,6,3,-5,-4,-9,-9,4,-8,10,-4,-3,5,-2,-5,2,4,-7,9,-10,-6,2,3,7,-7,-1,8,-7,1,1,8,5,9,-10,4,3,-9,5,-3,7,1,-10,9,-6,-7,-10,8,8,5,-10,-8,-3,10,-10,2,2,5,-6,9,9,-9,-10,2,6,8,10,-9,-4,1,-1,-3,-8,-4,3,4,-9,8,-10,9,-10,4,-4,1,3,2,-4,-6,3,7,-5,-7,6,4,-10,3,-2,7,9,2,1,5,-10,10,-3,1,-7,-10,6,8,9,-5,8,6,2,-1,-3,8,7,9,4,8,8,6,-4,-9,8,5,-6,5,-9,10,-3,9,8,-2,6,6,7,-8,-8,5,3,-4,-1,6,7,3,-6,-2,10,9,-3,10,8,-1,6,-2,6,-7,-7,6,-1,-6,3,3,3,9,-6,-7,8,-1,-6,3,-3,6,7,3,-2,7,8,-9,4,10,9,-6,-7,-1,-2,-4,9,4,-3,4,-8,3,10,1,-9,6,10,7,9,-2,-4,-7,-6,9,-9,-5,5,-7,9,9,-10,-8,-6,-8,2,-7,6,-1,4,2,-4,-2,-6,-4,-6,-2,9,-7,-4,-2,-4,-5,1,-5,-10,8,-5,-5,-9,3,-3,2,-9,-10,3,-1,9,9,4,6,-10,-9,5,3,2,-9,-5,10,-7,6,10,-9,3,-10,-4,4,1,9,5,1,-10,-6,-1,-6,5,-10,-9,-6,9,-3,2,-6,-9,10,7,-5,4,-1,-6,-5,8,7,-6,-2,-1,-9,10,-8,10,-7,1,-5,1,-2,-2,-7,-2,-10,9,7,-8,-3,-2,9,2,1,6,-10,2,4,-7,-8,7,-1,-1,6,-5,-8,-3,10,-3,-9,-7,-5,-1,4,-2,-8,2,7,8,-3,-4,9,-7,3,10,-8,2,-7,-4,10,-5,5,10,3,5,10,-6,-9,7,-3,-5,-5,6,-10,5,6,-2,9,3,9,-7,-9,9,-4,-1,5,-9,5,-4,-6,8,-1,3,4,2,-3,-4,2,4,2,-4,-3,9,8,4,-4,-4,-3,-7,-2,-10,-9,-1,10,4,1,8,1,-2,3,-3,-8,-2,-5,-8,7,3,-4,5,-8,-5,1,2,3,2,-8,2,3,9,-4,-4,6,-7,2,8,4,-8,9,8,-2,9,-5,-7,7,-6,-4,-2,-8,3,-4,9,-4,-5,-6,6,-1,-1,-8,-7,-4,-5,-5,-9,7,-2,-4,-1,9,3,8,5,-6,8,-5,-10,7,-7,4,5,9,4,-2,4,-10,-7,10,-10,8,-2,-2,-2,-6,3,-5,1,10,7,-2,-1,10,3,-10,6,-10,1,-9,-4,9,6,8,8,-5,-7,-8,1,8,7,8,6,-4,-1,9,1,-5,-4,6,-10,-8,10,-5,3,-5], dtype = "uint8")#candidate|1628|(3120,)|const|uint8
call_1627 = relay.TupleGetItem(func_796_call(relay.reshape(const_1628.astype('uint8'), [156, 20])), 1)
call_1629 = relay.TupleGetItem(func_798_call(relay.reshape(const_1628.astype('uint8'), [156, 20])), 1)
output = relay.Tuple([bop_1622,call_1627,const_1628,])
output2 = relay.Tuple([bop_1622,call_1629,const_1628,])
func_1632 = relay.Function([var_1621,], output)
mod['func_1632'] = func_1632
mod = relay.transform.InferType()(mod)
mutated_mod['func_1632'] = func_1632
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1633 = relay.var("var_1633", dtype = "uint32", shape = (3, 4, 11))#candidate|1633|(3, 4, 11)|var|uint32
func_1632_call = mutated_mod.get_global_var('func_1632')
call_1634 = func_1632_call(var_1633)
output = call_1634
func_1635 = relay.Function([var_1633], output)
mutated_mod['func_1635'] = func_1635
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1738 = relay.var("var_1738", dtype = "float32", shape = ())#candidate|1738|()|var|float32
const_1739 = relay.const([[[6.565707,-7.211670,5.770112,-1.748677,5.976277,7.951808,9.558663,-9.953662],[-5.063742,1.828790,1.982352,-6.201003,7.107014,-4.035849,-0.562072,-8.693630],[-6.951501,-1.614750,-4.423844,7.415760,2.295108,8.884823,-4.837100,8.773395],[-8.964100,1.926697,-7.774090,0.794520,2.622944,0.898732,4.138602,2.163394],[0.333721,5.767402,1.243681,8.430802,-3.010540,1.520820,-7.994686,8.201905],[4.654716,2.609994,-3.024574,0.561184,-0.686763,6.229591,-5.697123,2.564020],[1.568359,8.763549,6.629349,4.342947,-0.804606,2.683195,9.510752,4.435469],[0.423909,2.069055,7.617794,0.834328,7.672896,-1.174066,-7.728693,8.125171],[-1.703343,-4.548172,-9.521867,2.464611,-4.057633,0.811962,2.088526,-4.740338],[0.673091,0.449614,4.841521,-1.034392,5.658299,-7.629770,-3.970083,0.824879],[7.120332,9.822294,-9.954630,-9.550655,6.121925,-7.443655,-1.490948,7.986422],[-3.108057,-2.477507,-0.002393,8.369229,8.982381,0.881618,5.771300,1.174275]],[[-2.362287,-2.212566,1.075736,2.341453,4.826440,-8.691973,-4.274530,1.858704],[-2.357424,-7.902867,2.085841,-8.700528,-5.991036,-6.602059,8.695624,-9.494440],[-0.695494,-0.184134,3.196273,-6.484802,3.086861,-6.421925,2.924364,8.369921],[7.623553,-3.240404,4.639558,-7.290594,-9.720739,1.131802,-3.448184,6.129758],[6.616391,-9.284553,8.897182,2.781473,5.273985,-7.806060,3.688066,-8.523067],[-0.742612,6.150055,-9.377189,0.830433,0.387634,-8.869254,-7.308184,-0.627299],[9.322710,-9.040763,-2.734494,1.065141,4.119378,-8.126766,6.772311,3.003681],[5.095431,5.587847,-7.278135,-1.452643,-5.919595,8.093321,-4.922082,-0.329498],[1.025745,-5.914363,-3.307072,8.553175,3.226772,-7.831819,6.762676,-0.821559],[9.157768,-6.810203,-2.534246,4.046364,3.745068,4.505543,-5.440465,2.493113],[-1.595734,5.169594,8.857824,-6.463953,-3.184469,-5.530065,5.282133,-1.428903],[-1.710282,-5.054421,3.423478,6.196618,2.161457,-5.022598,-5.387629,3.055238]],[[5.822829,6.910287,2.862141,-4.710013,1.769865,7.172733,1.995147,3.278703],[-7.644606,9.520117,9.479767,-4.656889,9.633363,-1.954602,-4.357660,9.960062],[9.936813,7.585082,-1.899203,-1.752929,-4.420253,-9.219191,-9.692213,7.445509],[-4.615223,-0.141830,-7.687412,-0.986132,-5.541924,3.260034,-8.979469,-8.421627],[-6.714509,-3.980700,7.029281,-8.274988,0.735400,-0.965075,-2.596748,-0.314156],[-8.064559,-4.249838,-1.545712,-8.828472,0.620179,7.777766,-9.783639,5.093367],[7.941412,-7.778533,0.384142,-1.157693,8.947837,-4.140823,9.606709,-1.169049],[7.145180,-4.537716,5.314169,-7.495928,-4.448758,-0.017395,-3.437955,4.757793],[-6.131958,-8.925752,-5.291171,-6.502204,0.433130,8.195360,7.945977,-3.129806],[-4.659403,-9.641936,-7.402934,9.421205,4.605377,6.692779,0.799925,2.214862],[-9.256542,8.323397,1.400997,5.384106,-8.893830,0.689777,-2.454213,6.921342],[-3.138634,3.482058,-0.560924,1.200151,-8.760354,9.958608,-3.390722,7.631881]],[[9.551523,2.024253,-5.211774,7.874666,-4.963909,0.350726,1.978572,5.313301],[-0.691901,-7.576473,1.808480,-2.433235,-6.253342,-1.836955,4.461439,-4.541666],[-9.495455,9.684947,-7.143993,-5.467535,7.246725,6.969566,-7.789084,-1.353938],[7.757401,3.524863,-5.450082,1.251253,-4.910206,2.447350,2.781398,-7.961483],[-5.216522,0.984205,-2.339836,3.528508,8.282258,-7.630991,5.485415,-0.097177],[5.392032,-1.534273,-2.628420,5.745377,5.093628,-2.307881,-4.490823,-3.152534],[-4.973874,9.486340,4.685115,-8.955182,2.878399,-1.715520,5.536470,-6.519962],[0.818438,-4.668713,-4.045481,-4.267054,0.188593,-3.544732,4.742538,-3.392685],[-3.985776,-5.770804,-7.809114,-8.978002,-6.054653,-2.735602,-5.167753,-1.081599],[0.995932,3.097734,-6.093660,7.135616,-1.048248,1.635292,5.969654,0.353647],[3.497199,4.621019,-5.066249,-9.300283,1.351193,-9.173353,8.073764,1.991206],[7.567196,-7.101921,-9.528718,8.318776,7.070465,-3.674024,-3.884055,4.038222]],[[1.886325,0.861455,-3.355894,-0.052969,4.787590,5.249845,-2.845765,7.508035],[1.910002,1.319375,-5.954118,-3.657172,-4.164649,-0.049526,-1.725262,-5.522314],[-3.315390,5.699055,4.429104,-1.880605,-1.411830,5.420877,-0.980869,5.194071],[-5.859528,7.977246,2.951938,0.197404,-0.100095,9.117442,4.752041,1.543755],[3.199888,-6.280579,-4.050443,0.955057,2.972955,2.006037,-0.527826,0.704310],[-0.508811,2.091867,3.162594,2.122276,-6.566399,-2.025692,-3.416294,1.627270],[0.740462,4.813325,8.977010,-0.144430,7.238337,-9.596942,-8.118004,5.331507],[1.107711,9.624069,9.250510,-5.252653,8.704099,6.658058,-7.385840,6.470502],[-3.142781,-1.818509,-9.766951,-4.108765,-7.351798,1.562727,2.747081,7.481710],[3.574924,2.121653,9.151185,-8.661557,-3.772316,0.183828,-6.288967,-9.877014],[2.985590,-6.166284,-5.937020,4.838875,-9.323486,2.444468,9.006562,-2.578685],[9.346239,9.807428,3.084621,6.435380,5.626849,7.464018,-2.914220,4.294210]],[[-4.053718,4.816848,-8.080698,0.637689,6.732524,-1.076230,-5.172399,9.075102],[-9.902499,-6.230920,-2.982332,-9.894179,-6.172496,5.827805,0.467554,-6.798835],[9.712609,-6.274542,7.746401,-9.532815,2.994811,3.408982,7.064528,3.067570],[-7.333117,1.910858,-1.002032,-6.120247,4.200096,0.200027,-7.017932,-9.052942],[3.757807,-4.051692,3.323065,2.777731,9.941897,-5.633280,2.973282,9.279490],[0.250748,-7.481802,-7.612302,8.200804,-9.210158,-3.305849,-6.886617,-6.978067],[-8.798411,-7.966195,5.819121,-0.753570,5.082019,8.062735,-6.540177,-7.025475],[-0.517417,7.623344,3.661702,-5.855789,7.912944,8.338363,-4.392475,3.063910],[-0.934281,-4.681796,1.290605,-4.778913,8.864838,0.265023,-2.230108,5.886901],[-4.649650,3.729748,3.927980,-4.207671,3.732288,0.353000,0.245153,-1.431070],[-3.025958,-1.938540,7.128073,-0.066503,-3.157087,-0.385000,0.570986,1.787012],[8.748561,-1.324240,3.643028,8.523783,-5.268433,-6.658070,-8.784607,9.878176]]], dtype = "float32")#candidate|1739|(6, 12, 8)|const|float32
bop_1740 = relay.multiply(var_1738.astype('float32'), const_1739.astype('float32')) # shape=(6, 12, 8)
output = relay.Tuple([bop_1740,])
output2 = relay.Tuple([bop_1740,])
func_1748 = relay.Function([var_1738,], output)
mod['func_1748'] = func_1748
mod = relay.transform.InferType()(mod)
var_1749 = relay.var("var_1749", dtype = "float32", shape = ())#candidate|1749|()|var|float32
output = func_1748(var_1749)
func_1750 = relay.Function([var_1749], output)
mutated_mod['func_1750'] = func_1750
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1771 = relay.var("var_1771", dtype = "float32", shape = (10, 5, 10))#candidate|1771|(10, 5, 10)|var|float32
uop_1772 = relay.sinh(var_1771.astype('float32')) # shape=(10, 5, 10)
const_1786 = relay.const([[[4.283879,3.055159,3.789035,3.947521,-8.440730,7.008525,3.750401,-1.955591,3.224944,8.230608],[7.418203,2.016111,-5.519017,-1.051919,1.453172,-1.070132,-8.026182,-5.484359,3.013748,-2.071420],[0.112142,1.513737,-6.083971,-0.094754,7.905602,6.793949,0.636162,-0.138900,4.773505,4.478916],[0.632142,3.917346,8.360171,0.513022,-2.376285,-4.858276,-0.810574,-3.893816,9.671845,-9.674173],[-9.260880,6.412164,-0.413780,1.428435,-9.435823,4.584820,-0.328392,-9.795039,-8.209775,-0.421334]],[[5.221666,9.067574,6.137769,6.680727,-6.150622,5.134600,6.152293,-7.365445,-4.140714,6.635331],[-9.204228,-8.070975,-5.431267,-1.309577,9.823362,1.299483,-2.908903,-7.775552,-6.887429,-1.209658],[3.499831,0.776352,0.743498,4.981936,6.610696,-6.385226,3.390614,-8.799304,5.310915,-4.213143],[9.957644,-9.460539,-4.111741,3.397903,-7.516948,6.578747,9.383721,-2.894726,7.637725,7.351815],[6.875881,-3.448954,-7.390759,-6.339607,-6.410764,-8.363223,-1.080380,7.931204,8.574723,1.244853]],[[-0.283841,-4.168899,1.612085,-9.499261,-2.919718,6.538117,-6.690354,-8.214580,-4.305557,-5.687899],[4.641087,-3.371705,8.096402,9.755154,5.989501,-6.338985,1.100535,1.915531,-4.635851,0.742989],[2.401173,-5.085827,6.940264,3.895133,5.787832,-4.497093,-9.434907,-1.743727,-8.809613,8.611337],[-1.768654,6.400430,-3.576665,-3.793759,1.524377,6.477968,-0.576823,-5.630602,-1.081810,7.910483],[3.046684,-5.026273,-9.444721,-1.144023,-1.531504,-4.014754,1.054895,6.136326,1.700220,-2.074079]],[[2.411558,4.333244,5.135430,0.242092,5.873239,7.338044,-7.249727,2.995575,-5.216709,4.127122],[8.567533,0.927899,-9.190876,-0.556061,-9.090407,-1.922962,-6.585614,9.403105,8.544251,2.060687],[1.841308,3.857010,-1.722168,8.026940,-4.979417,-7.426316,-3.172818,5.147489,-8.449099,-6.148218],[-9.907500,-9.073824,6.512769,2.993353,9.038138,3.760826,9.277067,-0.692575,6.428808,4.816357],[4.908716,0.367284,7.568847,-5.034490,-4.371736,6.461032,3.056984,2.148009,8.288977,4.384901]],[[3.070162,-3.979245,9.259663,9.621386,-8.356667,8.372432,-0.388793,9.384717,2.078629,5.670254],[4.266879,-7.137009,-2.706192,8.971857,-3.066069,-8.461517,8.879208,9.581519,-5.930791,-6.209577],[5.473287,-6.152471,-1.017908,3.183035,2.447909,-1.945716,5.311909,6.549780,-2.695619,-3.365541],[3.937723,6.406326,1.644143,9.946061,8.425231,-9.251760,8.902523,-7.072211,-8.761874,0.085135],[-5.884381,-3.828680,1.797154,8.165372,-1.372082,-1.944479,7.835677,5.696802,-8.139795,-1.021422]],[[-5.734990,-2.321655,6.511646,7.516320,8.995797,8.264098,-5.166232,3.617023,2.831210,-4.184330],[-1.579203,0.960859,-0.086681,-7.741065,2.666737,-8.273839,4.699156,-4.281021,6.466841,5.012548],[-7.464557,-3.570663,-3.002455,-8.762302,-3.317590,-6.082344,-0.115493,-0.335743,-5.551950,1.050335],[9.178423,3.702234,7.624571,4.029922,3.910650,8.556803,7.882231,1.623471,8.943796,6.926780],[-3.651677,9.395089,3.582758,5.780442,-7.237435,-6.341463,-9.871660,8.563239,0.319545,-9.300199]],[[8.322820,-3.006216,4.491321,-2.555212,-8.149873,-8.413278,2.881127,6.839648,-4.003647,-8.476387],[3.317643,-1.977561,-3.312086,7.444507,0.963109,7.764694,2.467204,1.158531,9.222213,-7.227625],[-8.409433,-8.615757,-4.168920,-8.870167,-4.546120,3.297548,9.427735,3.800318,5.144048,0.532364],[-9.470696,7.416422,5.014071,-2.149766,4.673613,-0.368585,3.688388,0.160247,-5.392731,-6.525196],[1.323160,-3.993411,-3.209910,-8.831517,3.364917,-3.903069,-3.570557,2.536115,-3.626888,-1.814278]],[[-6.631716,5.413841,9.983863,5.273344,4.531465,-5.147216,-4.908699,2.899171,-6.812411,-0.397047],[-6.355917,6.833655,1.234046,-1.757251,-0.103553,6.393555,6.623046,0.381537,1.014030,-1.424198],[-0.559892,7.702443,7.474945,5.021544,9.236235,0.273034,-0.121481,-6.695452,-5.245321,-5.426430],[-0.578748,6.062424,-4.478256,-1.680784,-9.323025,-4.271034,-5.587443,6.296172,4.773799,4.177222],[-3.291443,-2.491675,-4.534682,-2.420255,0.759940,6.533809,-3.827529,9.591685,3.108017,3.823534]],[[-4.339447,9.415206,2.491280,-3.651168,9.102376,4.367945,2.758491,7.536845,9.443950,-5.486825],[-3.285377,-7.322606,-5.047732,4.486509,6.335649,3.267778,3.690242,-8.399136,5.048658,3.738321],[0.669253,5.336906,-0.778079,-3.815228,-5.933388,-1.607055,-5.660609,-2.596792,-3.108136,4.076776],[-4.913774,8.500917,7.146734,-3.569180,-3.179354,6.314165,9.793480,-1.167378,6.100754,3.880902],[4.068274,-7.023640,-6.416394,8.405333,4.727667,-6.675268,7.563493,6.762123,-7.567048,-5.765236]],[[3.785262,-4.431499,-0.510132,-5.842093,5.922786,9.139485,2.320838,-5.328670,-1.026095,-0.867396],[-9.590787,5.659563,-1.205208,-0.713947,9.509473,5.689069,3.110177,4.919196,5.619156,3.984721],[7.234980,7.305632,5.733341,-2.669011,8.396212,0.930532,2.536990,-1.156915,3.845162,-0.474242],[5.639046,9.731019,8.850545,-6.036857,-8.497391,0.247997,-4.211175,-0.398228,2.242931,-6.785873],[6.133755,-4.176424,-6.138840,-3.933916,-2.077664,-5.169155,-9.507221,-7.389976,-9.790322,-9.728773]]], dtype = "float32")#candidate|1786|(10, 5, 10)|const|float32
bop_1787 = relay.bitwise_and(uop_1772.astype('uint16'), relay.reshape(const_1786.astype('uint16'), relay.shape_of(uop_1772))) # shape=(10, 5, 10)
output = relay.Tuple([bop_1787,])
output2 = relay.Tuple([bop_1787,])
func_1791 = relay.Function([var_1771,], output)
mod['func_1791'] = func_1791
mod = relay.transform.InferType()(mod)
var_1792 = relay.var("var_1792", dtype = "float32", shape = (10, 5, 10))#candidate|1792|(10, 5, 10)|var|float32
output = func_1791(var_1792)
func_1793 = relay.Function([var_1792], output)
mutated_mod['func_1793'] = func_1793
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1859 = relay.var("var_1859", dtype = "float64", shape = (2, 2, 11))#candidate|1859|(2, 2, 11)|var|float64
var_1860 = relay.var("var_1860", dtype = "float64", shape = (2, 2, 11))#candidate|1860|(2, 2, 11)|var|float64
bop_1861 = relay.maximum(var_1859.astype('float64'), relay.reshape(var_1860.astype('float64'), relay.shape_of(var_1859))) # shape=(2, 2, 11)
output = relay.Tuple([bop_1861,])
output2 = relay.Tuple([bop_1861,])
func_1866 = relay.Function([var_1859,var_1860,], output)
mod['func_1866'] = func_1866
mod = relay.transform.InferType()(mod)
mutated_mod['func_1866'] = func_1866
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1866_call = mutated_mod.get_global_var('func_1866')
var_1868 = relay.var("var_1868", dtype = "float64", shape = (2, 2, 11))#candidate|1868|(2, 2, 11)|var|float64
var_1869 = relay.var("var_1869", dtype = "float64", shape = (2, 2, 11))#candidate|1869|(2, 2, 11)|var|float64
call_1867 = func_1866_call(var_1868,var_1869,)
output = call_1867
func_1870 = relay.Function([var_1868,var_1869,], output)
mutated_mod['func_1870'] = func_1870
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2003 = relay.const(3, dtype = "int16")#candidate|2003|()|const|int16
var_2004 = relay.var("var_2004", dtype = "int16", shape = (3, 12, 1))#candidate|2004|(3, 12, 1)|var|int16
bop_2005 = relay.greater(const_2003.astype('bool'), var_2004.astype('bool')) # shape=(3, 12, 1)
func_668_call = mod.get_global_var('func_668')
func_672_call = mutated_mod.get_global_var('func_672')
var_2013 = relay.var("var_2013", dtype = "uint8", shape = (275,))#candidate|2013|(275,)|var|uint8
call_2012 = relay.TupleGetItem(func_668_call(relay.reshape(var_2013.astype('uint8'), [11, 5, 5]), relay.reshape(var_2013.astype('uint8'), [11, 5, 5]), relay.reshape(var_2013.astype('uint8'), [11, 5, 5]), ), 1)
call_2014 = relay.TupleGetItem(func_672_call(relay.reshape(var_2013.astype('uint8'), [11, 5, 5]), relay.reshape(var_2013.astype('uint8'), [11, 5, 5]), relay.reshape(var_2013.astype('uint8'), [11, 5, 5]), ), 1)
bop_2015 = relay.floor_divide(bop_2005.astype('float64'), relay.reshape(var_2004.astype('float64'), relay.shape_of(bop_2005))) # shape=(3, 12, 1)
func_1598_call = mod.get_global_var('func_1598')
func_1601_call = mutated_mod.get_global_var('func_1601')
var_2020 = relay.var("var_2020", dtype = "int64", shape = (120,))#candidate|2020|(120,)|var|int64
call_2019 = func_1598_call(relay.reshape(var_2020.astype('int64'), [4, 10, 3]), relay.reshape(var_2020.astype('int64'), [4, 10, 3]), )
call_2021 = func_1598_call(relay.reshape(var_2020.astype('int64'), [4, 10, 3]), relay.reshape(var_2020.astype('int64'), [4, 10, 3]), )
func_1632_call = mod.get_global_var('func_1632')
func_1635_call = mutated_mod.get_global_var('func_1635')
const_2024 = relay.const([[-3,8,-4,7,8,7,-10,9,-4,-10,8,3,-8,7,2,-3,4,2,-4,-3,5,-8,-6,3,-5,7,6,3,-2,3,-8,6,10,3,9,8,-6,8,-3,-2,-5,-2,-8,4,5,-1,-8,4,-8,-1,3,-10,-8,-2,1,-9,-2,9,4,-9,3,-10,8,-8,-3,1,10,4,2,-9,10,1,-9,-2,-4,-1,-1,-9,-7,5,-5,5,-2,5,4,8,4,-6,10,5,10,-2,-9,2,-7,5,7,-9,-8,2,-10,8,10,8,-3,-3,-1,4,5,5,4,5,-1,-10,-1,-4,3,-9,-5,10,-2,-3,-7,2,-4,5,8,-9,6,-9,-2,-10]], dtype = "uint32")#candidate|2024|(1, 132)|const|uint32
call_2023 = relay.TupleGetItem(func_1632_call(relay.reshape(const_2024.astype('uint32'), [3, 4, 11])), 2)
call_2025 = relay.TupleGetItem(func_1635_call(relay.reshape(const_2024.astype('uint32'), [3, 4, 11])), 2)
func_709_call = mod.get_global_var('func_709')
func_711_call = mutated_mod.get_global_var('func_711')
call_2034 = relay.TupleGetItem(func_709_call(relay.reshape(call_2023.astype('uint8'), [16, 15, 13])), 2)
call_2035 = relay.TupleGetItem(func_711_call(relay.reshape(call_2023.astype('uint8'), [16, 15, 13])), 2)
func_668_call = mod.get_global_var('func_668')
func_672_call = mutated_mod.get_global_var('func_672')
call_2044 = relay.TupleGetItem(func_668_call(relay.reshape(var_2013.astype('uint8'), [11, 5, 5]), relay.reshape(var_2013.astype('uint8'), [11, 5, 5]), relay.reshape(call_2012.astype('uint8'), [11, 5, 5]), ), 1)
call_2045 = relay.TupleGetItem(func_672_call(relay.reshape(var_2013.astype('uint8'), [11, 5, 5]), relay.reshape(var_2013.astype('uint8'), [11, 5, 5]), relay.reshape(call_2012.astype('uint8'), [11, 5, 5]), ), 1)
output = relay.Tuple([call_2012,var_2013,bop_2015,call_2019,var_2020,call_2023,const_2024,call_2034,call_2044,])
output2 = relay.Tuple([call_2014,var_2013,bop_2015,call_2021,var_2020,call_2025,const_2024,call_2035,call_2045,])
func_2050 = relay.Function([var_2004,var_2013,var_2020,], output)
mod['func_2050'] = func_2050
mod = relay.transform.InferType()(mod)
var_2051 = relay.var("var_2051", dtype = "int16", shape = (3, 12, 1))#candidate|2051|(3, 12, 1)|var|int16
var_2052 = relay.var("var_2052", dtype = "uint8", shape = (275,))#candidate|2052|(275,)|var|uint8
var_2053 = relay.var("var_2053", dtype = "int64", shape = (120,))#candidate|2053|(120,)|var|int64
output = func_2050(var_2051,var_2052,var_2053,)
func_2054 = relay.Function([var_2051,var_2052,var_2053,], output)
mutated_mod['func_2054'] = func_2054
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2156 = relay.const([[[-10,4,10,-5,6,7,2,-3,8,3,3,-4,8,1,-7,-3],[-4,9,3,-4,-9,4,-6,-8,5,10,3,-4,-3,1,10,7],[1,7,-9,6,1,1,6,-4,9,8,7,2,-9,-2,-9,4],[-6,-5,-9,4,2,7,-5,9,-6,-5,-3,5,-4,-4,7,-2],[-8,-9,-9,-8,8,-8,-8,-6,-6,-1,10,10,4,-6,1,-5],[4,-7,-7,-3,-10,-10,8,7,7,-2,4,2,7,9,5,-6],[-8,-3,7,1,-6,8,-7,7,-2,4,10,-4,-5,4,6,8],[-2,2,6,7,-6,-6,-1,-8,10,1,-9,7,-7,-3,-1,-1]],[[-1,-2,-6,-1,-7,5,7,-3,5,-9,6,-6,6,-7,10,10],[9,-10,-3,5,-7,-8,-4,-1,2,1,7,2,-9,-10,5,2],[-4,-8,5,-4,6,5,10,8,8,-1,-9,8,-10,-8,-10,10],[3,10,-5,-10,-6,-10,-3,-10,10,-7,4,8,8,10,6,-2],[2,-9,-6,-8,4,-9,-8,1,10,-6,5,-8,-10,1,-10,5],[6,-9,-2,5,6,-4,-4,-10,-3,9,-2,1,7,8,-6,1],[6,2,-8,-2,2,-9,-1,1,7,1,10,1,-5,-7,1,-3],[-10,3,-4,4,-2,-2,-4,-6,4,-2,1,-4,-4,7,10,10]],[[-7,-2,9,6,-9,-4,-3,5,10,-4,3,-7,-8,10,-4,-2],[7,-1,7,10,6,-8,6,8,1,5,9,-10,-6,-9,-5,3],[-2,-8,2,7,-4,8,-10,-6,-10,6,-4,-8,-9,3,5,-5],[2,10,-3,-3,3,7,-10,6,-3,-9,1,9,4,5,10,8],[3,-6,-4,3,10,3,-2,-8,-3,4,-6,-7,7,-8,10,-8],[4,9,-3,-7,2,-1,-1,1,-7,10,-10,-2,7,-3,-7,-1],[-7,1,3,-10,-8,-9,-3,-2,7,-4,9,1,9,4,-9,9],[5,5,-9,-3,10,-5,2,3,-1,4,6,-7,-3,3,8,-7]],[[3,1,9,-1,5,9,-5,-5,-1,8,8,2,-8,3,-6,-1],[2,-3,5,7,-9,-7,1,3,-3,-7,6,-2,4,-2,-6,1],[6,-7,7,-1,2,-3,2,-5,6,-5,1,9,-3,-6,-6,6],[-9,3,1,-6,-3,-6,-4,-1,-2,5,6,-9,-4,9,-9,10],[-8,-8,8,-1,-3,-8,-9,9,5,-7,5,1,8,-7,-5,-9],[-1,-1,8,-2,3,10,-8,5,3,6,7,-9,-7,4,-5,-4],[-9,-5,-1,10,6,-7,-8,-8,6,1,3,-8,6,2,-4,-8],[-3,4,2,9,-5,-2,1,-6,-6,-8,-6,-9,6,-4,10,-7]],[[-8,7,4,-8,2,-4,10,10,6,6,2,-6,9,-3,5,3],[9,-1,-8,4,9,-3,-9,-6,10,-8,-9,3,6,8,3,3],[1,-7,-5,9,10,-4,6,5,-3,-8,-7,10,-6,3,10,-1],[1,10,-10,9,-2,8,-2,5,6,-6,4,-4,-6,10,-4,9],[-9,-9,-9,-9,-1,10,-10,9,-10,-8,-2,-5,-1,6,-7,1],[3,7,10,4,4,5,1,-1,10,5,2,-2,-6,10,-3,-1],[3,-10,-3,4,-10,-3,-4,10,-2,8,7,-8,-10,8,1,2],[9,-7,-8,-2,-2,7,-9,-2,4,-6,-9,5,5,3,-5,10]],[[-8,-6,7,-5,3,9,-1,-5,-2,-7,9,2,-7,2,1,6],[8,-8,-2,-6,-6,-8,-7,-1,6,-9,10,-1,-6,1,-4,9],[-2,8,1,-10,-10,-4,-3,-5,-5,-6,-6,3,9,-9,2,-4],[6,-8,-6,4,9,3,2,-3,-2,1,-7,10,-10,-10,9,-9],[-7,-2,7,1,3,-8,-1,2,-3,1,-9,7,-10,-4,-2,-3],[-1,-2,-10,-2,6,-10,4,-10,6,6,-2,7,-1,-10,5,2],[8,-4,-6,3,-8,-8,-4,-9,2,8,-10,6,7,4,1,9],[9,-10,-10,6,-6,10,5,-10,7,-10,2,-10,-6,-2,10,8]],[[3,-4,-3,-10,-7,8,-2,-8,6,-7,6,7,2,10,-1,1],[6,-6,8,-9,8,6,6,10,1,-10,7,-2,-7,2,9,-1],[-1,-6,-4,-1,-2,4,-10,-10,6,-2,5,3,-4,-9,8,-2],[10,-5,2,-9,-4,2,1,-7,-2,-9,10,-1,7,-9,-2,2],[-8,-6,-5,-5,-10,-3,9,-8,-8,9,1,4,10,2,4,-5],[3,5,8,8,-8,-9,-2,9,-3,8,6,1,7,9,-7,6],[-8,9,2,4,-2,-7,1,4,4,-10,-6,-10,4,6,4,3],[-4,7,-4,6,-5,8,-10,-2,6,9,-10,-7,-8,6,-7,-3]],[[-3,-7,-3,-1,-7,-6,3,3,7,3,1,-4,5,1,10,4],[-6,10,-5,10,2,-1,6,-8,8,-2,3,9,5,9,4,9],[-6,1,-2,5,9,-10,-2,7,10,-2,-5,-1,9,-8,-5,4],[7,-5,8,-4,-8,1,-5,-1,-10,-9,1,9,-4,-4,-5,-2],[-4,5,7,-9,6,-4,-10,9,7,7,10,2,5,2,-6,4],[1,2,-9,-2,2,-7,2,-4,-3,-1,-9,6,-10,-3,1,4],[9,10,8,-4,-10,1,-6,-5,8,-4,8,10,-6,-2,-2,-1],[-4,-10,4,1,4,10,-8,1,-8,2,4,-3,7,-9,2,2]]], dtype = "uint8")#candidate|2156|(8, 8, 16)|const|uint8
var_2157 = relay.var("var_2157", dtype = "uint8", shape = (8, 8, 16))#candidate|2157|(8, 8, 16)|var|uint8
bop_2158 = relay.left_shift(const_2156.astype('uint8'), relay.reshape(var_2157.astype('uint8'), relay.shape_of(const_2156))) # shape=(8, 8, 16)
func_796_call = mod.get_global_var('func_796')
func_798_call = mutated_mod.get_global_var('func_798')
var_2174 = relay.var("var_2174", dtype = "uint8", shape = (780, 4))#candidate|2174|(780, 4)|var|uint8
call_2173 = relay.TupleGetItem(func_796_call(relay.reshape(var_2174.astype('uint8'), [156, 20])), 2)
call_2175 = relay.TupleGetItem(func_798_call(relay.reshape(var_2174.astype('uint8'), [156, 20])), 2)
func_668_call = mod.get_global_var('func_668')
func_672_call = mutated_mod.get_global_var('func_672')
var_2179 = relay.var("var_2179", dtype = "uint8", shape = (275,))#candidate|2179|(275,)|var|uint8
call_2178 = relay.TupleGetItem(func_668_call(relay.reshape(var_2179.astype('uint8'), [11, 5, 5]), relay.reshape(var_2179.astype('uint8'), [11, 5, 5]), relay.reshape(var_2179.astype('uint8'), [11, 5, 5]), ), 0)
call_2180 = relay.TupleGetItem(func_672_call(relay.reshape(var_2179.astype('uint8'), [11, 5, 5]), relay.reshape(var_2179.astype('uint8'), [11, 5, 5]), relay.reshape(var_2179.astype('uint8'), [11, 5, 5]), ), 0)
output = relay.Tuple([bop_2158,call_2173,var_2174,call_2178,var_2179,])
output2 = relay.Tuple([bop_2158,call_2175,var_2174,call_2180,var_2179,])
func_2181 = relay.Function([var_2157,var_2174,var_2179,], output)
mod['func_2181'] = func_2181
mod = relay.transform.InferType()(mod)
var_2182 = relay.var("var_2182", dtype = "uint8", shape = (8, 8, 16))#candidate|2182|(8, 8, 16)|var|uint8
var_2183 = relay.var("var_2183", dtype = "uint8", shape = (780, 4))#candidate|2183|(780, 4)|var|uint8
var_2184 = relay.var("var_2184", dtype = "uint8", shape = (275,))#candidate|2184|(275,)|var|uint8
output = func_2181(var_2182,var_2183,var_2184,)
func_2185 = relay.Function([var_2182,var_2183,var_2184,], output)
mutated_mod['func_2185'] = func_2185
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2196 = relay.const([[[-6.057510,-2.805236,-3.477200,-6.537204,3.707521,-9.846051,-7.209108,-7.734905]],[[9.777558,9.242806,-7.392383,4.029991,-0.240496,0.810652,4.084320,-3.637087]]], dtype = "float32")#candidate|2196|(2, 1, 8)|const|float32
uop_2197 = relay.atan(const_2196.astype('float32')) # shape=(2, 1, 8)
output = uop_2197
output2 = uop_2197
func_2200 = relay.Function([], output)
mod['func_2200'] = func_2200
mod = relay.transform.InferType()(mod)
output = func_2200()
func_2201 = relay.Function([], output)
mutated_mod['func_2201'] = func_2201
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2200_call = mod.get_global_var('func_2200')
func_2201_call = mutated_mod.get_global_var('func_2201')
call_2230 = func_2200_call()
call_2231 = func_2200_call()
output = relay.Tuple([call_2230,])
output2 = relay.Tuple([call_2231,])
func_2252 = relay.Function([], output)
mod['func_2252'] = func_2252
mod = relay.transform.InferType()(mod)
mutated_mod['func_2252'] = func_2252
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2252_call = mutated_mod.get_global_var('func_2252')
call_2253 = func_2252_call()
output = call_2253
func_2254 = relay.Function([], output)
mutated_mod['func_2254'] = func_2254
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2252_call = mod.get_global_var('func_2252')
func_2254_call = mutated_mod.get_global_var('func_2254')
call_2264 = relay.TupleGetItem(func_2252_call(), 0)
call_2265 = relay.TupleGetItem(func_2254_call(), 0)
uop_2273 = relay.asin(call_2264.astype('float64')) # shape=(2, 1, 8)
uop_2275 = relay.asin(call_2265.astype('float64')) # shape=(2, 1, 8)
output = uop_2273
output2 = uop_2275
func_2278 = relay.Function([], output)
mod['func_2278'] = func_2278
mod = relay.transform.InferType()(mod)
mutated_mod['func_2278'] = func_2278
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2278_call = mutated_mod.get_global_var('func_2278')
call_2279 = func_2278_call()
output = call_2279
func_2280 = relay.Function([], output)
mutated_mod['func_2280'] = func_2280
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2278_call = mod.get_global_var('func_2278')
func_2280_call = mutated_mod.get_global_var('func_2280')
call_2299 = func_2278_call()
call_2300 = func_2278_call()
output = relay.Tuple([call_2299,])
output2 = relay.Tuple([call_2300,])
func_2307 = relay.Function([], output)
mod['func_2307'] = func_2307
mod = relay.transform.InferType()(mod)
mutated_mod['func_2307'] = func_2307
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2307_call = mutated_mod.get_global_var('func_2307')
call_2308 = func_2307_call()
output = call_2308
func_2309 = relay.Function([], output)
mutated_mod['func_2309'] = func_2309
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2366 = relay.var("var_2366", dtype = "float32", shape = (2, 16, 15))#candidate|2366|(2, 16, 15)|var|float32
var_2367 = relay.var("var_2367", dtype = "float32", shape = (2, 16, 15))#candidate|2367|(2, 16, 15)|var|float32
bop_2368 = relay.floor_divide(var_2366.astype('float32'), relay.reshape(var_2367.astype('float32'), relay.shape_of(var_2366))) # shape=(2, 16, 15)
uop_2394 = relay.sinh(var_2367.astype('float32')) # shape=(2, 16, 15)
uop_2406 = relay.log(uop_2394.astype('float64')) # shape=(2, 16, 15)
output = relay.Tuple([bop_2368,uop_2406,])
output2 = relay.Tuple([bop_2368,uop_2406,])
func_2412 = relay.Function([var_2366,var_2367,], output)
mod['func_2412'] = func_2412
mod = relay.transform.InferType()(mod)
mutated_mod['func_2412'] = func_2412
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2412_call = mutated_mod.get_global_var('func_2412')
var_2414 = relay.var("var_2414", dtype = "float32", shape = (2, 16, 15))#candidate|2414|(2, 16, 15)|var|float32
var_2415 = relay.var("var_2415", dtype = "float32", shape = (2, 16, 15))#candidate|2415|(2, 16, 15)|var|float32
call_2413 = func_2412_call(var_2414,var_2415,)
output = call_2413
func_2416 = relay.Function([var_2414,var_2415,], output)
mutated_mod['func_2416'] = func_2416
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2278_call = mod.get_global_var('func_2278')
func_2280_call = mutated_mod.get_global_var('func_2280')
call_2420 = func_2278_call()
call_2421 = func_2278_call()
func_2252_call = mod.get_global_var('func_2252')
func_2254_call = mutated_mod.get_global_var('func_2254')
call_2427 = relay.TupleGetItem(func_2252_call(), 0)
call_2428 = relay.TupleGetItem(func_2254_call(), 0)
func_2278_call = mod.get_global_var('func_2278')
func_2280_call = mutated_mod.get_global_var('func_2280')
call_2442 = func_2278_call()
call_2443 = func_2278_call()
output = relay.Tuple([call_2420,call_2427,call_2442,])
output2 = relay.Tuple([call_2421,call_2428,call_2443,])
func_2445 = relay.Function([], output)
mod['func_2445'] = func_2445
mod = relay.transform.InferType()(mod)
output = func_2445()
func_2446 = relay.Function([], output)
mutated_mod['func_2446'] = func_2446
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2252_call = mod.get_global_var('func_2252')
func_2254_call = mutated_mod.get_global_var('func_2254')
call_2492 = relay.TupleGetItem(func_2252_call(), 0)
call_2493 = relay.TupleGetItem(func_2254_call(), 0)
var_2495 = relay.var("var_2495", dtype = "float32", shape = (2, 5, 8))#candidate|2495|(2, 5, 8)|var|float32
bop_2496 = relay.subtract(call_2492.astype('int32'), var_2495.astype('int32')) # shape=(2, 5, 8)
bop_2499 = relay.subtract(call_2493.astype('int32'), var_2495.astype('int32')) # shape=(2, 5, 8)
func_2252_call = mod.get_global_var('func_2252')
func_2254_call = mutated_mod.get_global_var('func_2254')
call_2500 = relay.TupleGetItem(func_2252_call(), 0)
call_2501 = relay.TupleGetItem(func_2254_call(), 0)
func_1748_call = mod.get_global_var('func_1748')
func_1750_call = mutated_mod.get_global_var('func_1750')
var_2507 = relay.var("var_2507", dtype = "float32", shape = ())#candidate|2507|()|var|float32
call_2506 = relay.TupleGetItem(func_1748_call(relay.reshape(var_2507.astype('float32'), [])), 0)
call_2508 = relay.TupleGetItem(func_1750_call(relay.reshape(var_2507.astype('float32'), [])), 0)
bop_2509 = relay.logical_and(call_2500.astype('bool'), bop_2496.astype('bool')) # shape=(2, 5, 8)
bop_2512 = relay.logical_and(call_2501.astype('bool'), bop_2499.astype('bool')) # shape=(2, 5, 8)
func_2252_call = mod.get_global_var('func_2252')
func_2254_call = mutated_mod.get_global_var('func_2254')
call_2517 = relay.TupleGetItem(func_2252_call(), 0)
call_2518 = relay.TupleGetItem(func_2254_call(), 0)
func_2200_call = mod.get_global_var('func_2200')
func_2201_call = mutated_mod.get_global_var('func_2201')
call_2521 = func_2200_call()
call_2522 = func_2200_call()
func_2278_call = mod.get_global_var('func_2278')
func_2280_call = mutated_mod.get_global_var('func_2280')
call_2523 = func_2278_call()
call_2524 = func_2278_call()
output = relay.Tuple([call_2506,var_2507,bop_2509,call_2517,call_2521,call_2523,])
output2 = relay.Tuple([call_2508,var_2507,bop_2512,call_2518,call_2522,call_2524,])
func_2539 = relay.Function([var_2495,var_2507,], output)
mod['func_2539'] = func_2539
mod = relay.transform.InferType()(mod)
var_2540 = relay.var("var_2540", dtype = "float32", shape = (2, 5, 8))#candidate|2540|(2, 5, 8)|var|float32
var_2541 = relay.var("var_2541", dtype = "float32", shape = ())#candidate|2541|()|var|float32
output = func_2539(var_2540,var_2541,)
func_2542 = relay.Function([var_2540,var_2541,], output)
mutated_mod['func_2542'] = func_2542
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2307_call = mod.get_global_var('func_2307')
func_2309_call = mutated_mod.get_global_var('func_2309')
call_2569 = relay.TupleGetItem(func_2307_call(), 0)
call_2570 = relay.TupleGetItem(func_2309_call(), 0)
func_1748_call = mod.get_global_var('func_1748')
func_1750_call = mutated_mod.get_global_var('func_1750')
const_2576 = relay.const(-0.497572, dtype = "float32")#candidate|2576|()|const|float32
call_2575 = relay.TupleGetItem(func_1748_call(relay.reshape(const_2576.astype('float32'), [])), 0)
call_2577 = relay.TupleGetItem(func_1750_call(relay.reshape(const_2576.astype('float32'), [])), 0)
func_2445_call = mod.get_global_var('func_2445')
func_2446_call = mutated_mod.get_global_var('func_2446')
call_2579 = relay.TupleGetItem(func_2445_call(), 1)
call_2580 = relay.TupleGetItem(func_2446_call(), 1)
func_2181_call = mod.get_global_var('func_2181')
func_2185_call = mutated_mod.get_global_var('func_2185')
var_2591 = relay.var("var_2591", dtype = "uint8", shape = (1024,))#candidate|2591|(1024,)|var|uint8
var_2592 = relay.var("var_2592", dtype = "uint8", shape = (3120,))#candidate|2592|(3120,)|var|uint8
var_2593 = relay.var("var_2593", dtype = "uint8", shape = (275,))#candidate|2593|(275,)|var|uint8
call_2590 = relay.TupleGetItem(func_2181_call(relay.reshape(var_2591.astype('uint8'), [8, 8, 16]), relay.reshape(var_2592.astype('uint8'), [780, 4]), relay.reshape(var_2593.astype('uint8'), [275,]), ), 1)
call_2594 = relay.TupleGetItem(func_2185_call(relay.reshape(var_2591.astype('uint8'), [8, 8, 16]), relay.reshape(var_2592.astype('uint8'), [780, 4]), relay.reshape(var_2593.astype('uint8'), [275,]), ), 1)
func_2200_call = mod.get_global_var('func_2200')
func_2201_call = mutated_mod.get_global_var('func_2201')
call_2601 = func_2200_call()
call_2602 = func_2200_call()
func_1791_call = mod.get_global_var('func_1791')
func_1793_call = mutated_mod.get_global_var('func_1793')
var_2605 = relay.var("var_2605", dtype = "float32", shape = (10, 50))#candidate|2605|(10, 50)|var|float32
call_2604 = relay.TupleGetItem(func_1791_call(relay.reshape(var_2605.astype('float32'), [10, 5, 10])), 0)
call_2606 = relay.TupleGetItem(func_1793_call(relay.reshape(var_2605.astype('float32'), [10, 5, 10])), 0)
uop_2607 = relay.exp(call_2575.astype('float32')) # shape=(6, 12, 8)
uop_2609 = relay.exp(call_2577.astype('float32')) # shape=(6, 12, 8)
output = relay.Tuple([call_2569,const_2576,call_2579,call_2590,var_2591,var_2592,var_2593,call_2601,call_2604,var_2605,uop_2607,])
output2 = relay.Tuple([call_2570,const_2576,call_2580,call_2594,var_2591,var_2592,var_2593,call_2602,call_2606,var_2605,uop_2609,])
func_2626 = relay.Function([var_2591,var_2592,var_2593,var_2605,], output)
mod['func_2626'] = func_2626
mod = relay.transform.InferType()(mod)
mutated_mod['func_2626'] = func_2626
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2626_call = mutated_mod.get_global_var('func_2626')
var_2628 = relay.var("var_2628", dtype = "uint8", shape = (1024,))#candidate|2628|(1024,)|var|uint8
var_2629 = relay.var("var_2629", dtype = "uint8", shape = (3120,))#candidate|2629|(3120,)|var|uint8
var_2630 = relay.var("var_2630", dtype = "uint8", shape = (275,))#candidate|2630|(275,)|var|uint8
var_2631 = relay.var("var_2631", dtype = "float32", shape = (10, 50))#candidate|2631|(10, 50)|var|float32
call_2627 = func_2626_call(var_2628,var_2629,var_2630,var_2631,)
output = call_2627
func_2632 = relay.Function([var_2628,var_2629,var_2630,var_2631,], output)
mutated_mod['func_2632'] = func_2632
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2445_call = mod.get_global_var('func_2445')
func_2446_call = mutated_mod.get_global_var('func_2446')
call_2642 = relay.TupleGetItem(func_2445_call(), 1)
call_2643 = relay.TupleGetItem(func_2446_call(), 1)
output = relay.Tuple([call_2642,])
output2 = relay.Tuple([call_2643,])
func_2644 = relay.Function([], output)
mod['func_2644'] = func_2644
mod = relay.transform.InferType()(mod)
mutated_mod['func_2644'] = func_2644
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2644_call = mutated_mod.get_global_var('func_2644')
call_2645 = func_2644_call()
output = call_2645
func_2646 = relay.Function([], output)
mutated_mod['func_2646'] = func_2646
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2307_call = mod.get_global_var('func_2307')
func_2309_call = mutated_mod.get_global_var('func_2309')
call_2652 = relay.TupleGetItem(func_2307_call(), 0)
call_2653 = relay.TupleGetItem(func_2309_call(), 0)
func_2252_call = mod.get_global_var('func_2252')
func_2254_call = mutated_mod.get_global_var('func_2254')
call_2657 = relay.TupleGetItem(func_2252_call(), 0)
call_2658 = relay.TupleGetItem(func_2254_call(), 0)
var_2659 = relay.var("var_2659", dtype = "float32", shape = (2, 15, 8))#candidate|2659|(2, 15, 8)|var|float32
bop_2660 = relay.not_equal(call_2657.astype('bool'), var_2659.astype('bool')) # shape=(2, 15, 8)
bop_2663 = relay.not_equal(call_2658.astype('bool'), var_2659.astype('bool')) # shape=(2, 15, 8)
bop_2667 = relay.add(call_2652.astype('uint64'), relay.reshape(call_2657.astype('uint64'), relay.shape_of(call_2652))) # shape=(2, 1, 8)
bop_2670 = relay.add(call_2653.astype('uint64'), relay.reshape(call_2658.astype('uint64'), relay.shape_of(call_2653))) # shape=(2, 1, 8)
output = relay.Tuple([bop_2660,bop_2667,])
output2 = relay.Tuple([bop_2663,bop_2670,])
func_2675 = relay.Function([var_2659,], output)
mod['func_2675'] = func_2675
mod = relay.transform.InferType()(mod)
var_2676 = relay.var("var_2676", dtype = "float32", shape = (2, 15, 8))#candidate|2676|(2, 15, 8)|var|float32
output = func_2675(var_2676)
func_2677 = relay.Function([var_2676], output)
mutated_mod['func_2677'] = func_2677
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2694 = relay.var("var_2694", dtype = "float64", shape = (14, 11, 3))#candidate|2694|(14, 11, 3)|var|float64
var_2695 = relay.var("var_2695", dtype = "float64", shape = (14, 11, 3))#candidate|2695|(14, 11, 3)|var|float64
bop_2696 = relay.subtract(var_2694.astype('float64'), relay.reshape(var_2695.astype('float64'), relay.shape_of(var_2694))) # shape=(14, 11, 3)
output = bop_2696
output2 = bop_2696
func_2699 = relay.Function([var_2694,var_2695,], output)
mod['func_2699'] = func_2699
mod = relay.transform.InferType()(mod)
mutated_mod['func_2699'] = func_2699
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2699_call = mutated_mod.get_global_var('func_2699')
var_2701 = relay.var("var_2701", dtype = "float64", shape = (14, 11, 3))#candidate|2701|(14, 11, 3)|var|float64
var_2702 = relay.var("var_2702", dtype = "float64", shape = (14, 11, 3))#candidate|2702|(14, 11, 3)|var|float64
call_2700 = func_2699_call(var_2701,var_2702,)
output = call_2700
func_2703 = relay.Function([var_2701,var_2702,], output)
mutated_mod['func_2703'] = func_2703
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2644_call = mod.get_global_var('func_2644')
func_2646_call = mutated_mod.get_global_var('func_2646')
call_2717 = relay.TupleGetItem(func_2644_call(), 0)
call_2718 = relay.TupleGetItem(func_2646_call(), 0)
func_2050_call = mod.get_global_var('func_2050')
func_2054_call = mutated_mod.get_global_var('func_2054')
const_2722 = relay.const([-9,2,-1,7,-3,-5,1,-4,-9,5,-4,-5,8,-4,9,5,-6,9,-3,-3,-3,5,8,-1,2,1,3,-9,-4,-1,4,-3,4,10,-10,-6], dtype = "int16")#candidate|2722|(36,)|const|int16
const_2723 = relay.const([9,2,-6,-5,2,-7,-10,6,5,9,2,10,1,-7,5,1,9,3,8,4,-8,5,-1,-9,-2,-2,2,-8,-2,-3,5,2,-7,-9,2,9,4,10,-4,2,7,-10,-6,3,5,6,2,-6,-2,4,-8,-8,6,8,6,3,3,-4,4,-8,7,-1,-3,-6,1,3,-4,4,8,9,3,9,9,-5,-3,4,-1,7,-1,1,4,5,-6,9,10,-9,-3,-9,2,-3,-8,-4,-1,3,5,-8,-9,-10,-2,10,-8,7,7,-2,-1,-5,4,-8,-2,1,-6,-8,-3,-1,-7,7,1,-7,-9,9,-7,-8,6,10,-8,7,1,10,-6,-9,3,-2,-1,5,9,-1,-10,9,-7,-6,-9,9,-10,4,-10,-3,-10,-7,2,-10,-6,9,-9,2,9,-1,10,-10,6,8,-8,9,4,8,6,8,10,7,-8,-5,4,-7,5,5,-1,9,2,9,2,1,-5,1,8,5,5,-5,8,-5,7,-6,3,-2,-1,-2,-6,2,-1,7,9,7,1,-6,4,-2,3,3,-1,-2,4,5,6,1,10,-9,9,-6,-10,1,-6,-4,1,7,-10,6,5,-6,-1,-10,-7,2,7,-8,10,8,2,-5,1,9,-2,-7,-6,-8,10,-10,7,2,-7,8,10,5,1,-7,3,4,-8,-2,4,5,-8,-10,4,8,10,1,3,2,-8,-6,4,6,-1,-8,8,8,8], dtype = "uint8")#candidate|2723|(275,)|const|uint8
var_2724 = relay.var("var_2724", dtype = "int64", shape = (120,))#candidate|2724|(120,)|var|int64
call_2721 = relay.TupleGetItem(func_2050_call(relay.reshape(const_2722.astype('int16'), [3, 12, 1]), relay.reshape(const_2723.astype('uint8'), [275,]), relay.reshape(var_2724.astype('int64'), [120,]), ), 6)
call_2725 = relay.TupleGetItem(func_2054_call(relay.reshape(const_2722.astype('int16'), [3, 12, 1]), relay.reshape(const_2723.astype('uint8'), [275,]), relay.reshape(var_2724.astype('int64'), [120,]), ), 6)
uop_2732 = relay.sin(const_2722.astype('float64')) # shape=(36,)
output = relay.Tuple([call_2717,call_2721,const_2723,var_2724,uop_2732,])
output2 = relay.Tuple([call_2718,call_2725,const_2723,var_2724,uop_2732,])
func_2734 = relay.Function([var_2724,], output)
mod['func_2734'] = func_2734
mod = relay.transform.InferType()(mod)
var_2735 = relay.var("var_2735", dtype = "int64", shape = (120,))#candidate|2735|(120,)|var|int64
output = func_2734(var_2735)
func_2736 = relay.Function([var_2735], output)
mutated_mod['func_2736'] = func_2736
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2200_call = mod.get_global_var('func_2200')
func_2201_call = mutated_mod.get_global_var('func_2201')
call_2800 = func_2200_call()
call_2801 = func_2200_call()
output = call_2800
output2 = call_2801
func_2802 = relay.Function([], output)
mod['func_2802'] = func_2802
mod = relay.transform.InferType()(mod)
mutated_mod['func_2802'] = func_2802
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2802_call = mutated_mod.get_global_var('func_2802')
call_2803 = func_2802_call()
output = call_2803
func_2804 = relay.Function([], output)
mutated_mod['func_2804'] = func_2804
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2819 = relay.var("var_2819", dtype = "int16", shape = (8, 4, 11))#candidate|2819|(8, 4, 11)|var|int16
var_2820 = relay.var("var_2820", dtype = "int16", shape = (8, 4, 11))#candidate|2820|(8, 4, 11)|var|int16
bop_2821 = relay.right_shift(var_2819.astype('int16'), relay.reshape(var_2820.astype('int16'), relay.shape_of(var_2819))) # shape=(8, 4, 11)
bop_2828 = relay.greater(var_2820.astype('bool'), relay.reshape(bop_2821.astype('bool'), relay.shape_of(var_2820))) # shape=(8, 4, 11)
output = bop_2828
output2 = bop_2828
func_2831 = relay.Function([var_2819,var_2820,], output)
mod['func_2831'] = func_2831
mod = relay.transform.InferType()(mod)
var_2832 = relay.var("var_2832", dtype = "int16", shape = (8, 4, 11))#candidate|2832|(8, 4, 11)|var|int16
var_2833 = relay.var("var_2833", dtype = "int16", shape = (8, 4, 11))#candidate|2833|(8, 4, 11)|var|int16
output = func_2831(var_2832,var_2833,)
func_2834 = relay.Function([var_2832,var_2833,], output)
mutated_mod['func_2834'] = func_2834
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2644_call = mod.get_global_var('func_2644')
func_2646_call = mutated_mod.get_global_var('func_2646')
call_2852 = relay.TupleGetItem(func_2644_call(), 0)
call_2853 = relay.TupleGetItem(func_2646_call(), 0)
func_2675_call = mod.get_global_var('func_2675')
func_2677_call = mutated_mod.get_global_var('func_2677')
const_2863 = relay.const([-4.219174,-1.431221,-5.083581,3.998739,-8.364720,-3.888630,6.215692,-3.569996,4.849650,4.832068,8.610585,5.520406,9.406701,-1.295204,-2.186655,4.596022,-8.638416,-6.251028,-2.406761,5.559635,-8.554733,-6.923118,-1.027265,3.839052,-9.668106,-9.047889,9.228141,7.791677,-0.152630,2.834105,1.101700,9.770785,7.061212,-6.824848,3.826439,-8.920274,4.049211,-6.309919,1.708877,7.244275,-6.024640,1.093594,7.853465,0.067159,-6.267467,-9.579652,5.960803,-0.368613,3.036321,-1.797153,-9.232726,-9.018801,-4.554029,-2.710262,-0.510575,4.617518,4.880636,9.801334,-3.957488,-7.532308,7.352819,-9.165706,7.986427,9.763804,-9.376383,0.968536,-9.361962,-4.210780,-8.169949,-9.985564,4.097114,-9.092374,-8.472422,3.525910,-5.370265,-6.608125,9.199300,-3.233902,7.702589,5.521692,4.776886,-8.800202,3.823954,-5.250759,2.533483,-9.719802,8.701803,-7.713636,-3.804941,-9.626819,6.340408,6.299122,9.699332,8.232572,6.962945,-8.619200,-4.257809,6.089486,-4.645989,1.070097,-6.826387,-4.340720,-6.377322,-6.444489,-0.822265,9.276575,7.378683,-7.341080,-6.066894,0.013376,2.312172,3.754135,-9.608821,3.322722,-0.893797,5.072279,-5.051679,-8.702838,-9.023710,-2.122135,3.110565,-6.192058,-7.246312,-6.461103,7.835695,-8.817911,8.585574,-6.637023,-8.154971,-6.064491,-3.565792,-7.714096,9.502005,-5.369606,9.366400,6.301898,-2.486297,7.190605,-6.756581,-7.452490,1.174102,-1.427182,-3.630536,-1.062517,-2.739612,4.001247,-8.026323,-6.984897,8.897274,2.646871,5.723064,1.834054,4.366698,-0.175866,-3.917221,7.847026,5.428702,4.333519,-5.462901,5.703680,-9.628018,0.385799,-2.741554,0.490316,-1.670905,-5.558024,7.982122,-6.089206,-1.610480,-9.220323,7.452852,-8.336528,-2.452569,-0.913902,4.881070,4.859054,-1.451550,3.663700,-9.502442,-5.106551,1.597660,-4.198031,0.449636,4.180325,9.519029,-4.419388,1.255557,-3.334618,-7.783822,-8.846777,-3.316388,-8.462879,3.410064,9.207250,-0.522381,-6.061835,-8.036405,-3.376221,3.544787,0.104152,8.706800,2.071134,-3.382994,-5.009452,-0.167208,-1.083252,9.249824,-7.532219,-6.682325,-5.639830,1.299486,2.936278,-7.708758,6.080010,9.839016,-3.371477,3.203705,-1.108252,7.792209,-3.589775,2.936573,-9.559011,8.709405,4.307069,-5.107087,-6.141639,2.593519,6.063609,7.157379,1.739223,5.263574,-4.251943,-5.567553,-1.388869,2.985098,5.670516,-1.366730,7.830199,-3.104129,2.737098], dtype = "float32")#candidate|2863|(240,)|const|float32
call_2862 = relay.TupleGetItem(func_2675_call(relay.reshape(const_2863.astype('float32'), [2, 15, 8])), 1)
call_2864 = relay.TupleGetItem(func_2677_call(relay.reshape(const_2863.astype('float32'), [2, 15, 8])), 1)
bop_2870 = relay.subtract(call_2852.astype('int16'), relay.reshape(call_2862.astype('int16'), relay.shape_of(call_2852))) # shape=(2, 1, 8)
bop_2873 = relay.subtract(call_2853.astype('int16'), relay.reshape(call_2864.astype('int16'), relay.shape_of(call_2853))) # shape=(2, 1, 8)
func_1423_call = mod.get_global_var('func_1423')
func_1426_call = mutated_mod.get_global_var('func_1426')
const_2876 = relay.const([6.347252,6.838543,8.164924,-8.363620,0.351492,9.464688,7.612767,-9.827384,4.687702,0.682377,8.622850,-7.476687,8.227340,3.082186,-3.576561,0.636867,6.865967,0.544054,-4.974560,-1.210307,-1.925805,1.657143,-5.007098,-4.487552,7.826929,4.634000,2.433024,3.328916,8.330507,7.641865,1.992768,0.622515,9.838345,4.445574,-8.797152,-6.032293,3.476358,-6.696834,4.062843,9.096492,-7.916193,9.656806,-0.990792,-9.088332,2.232762,6.268017,7.991277,-7.054677,9.372032,-6.388256,5.707125,8.562919,-0.397518,0.128652,-2.490805,-2.209666,2.949028,-9.131088,-2.220115,8.096405,6.717612,-5.111913,7.592736,2.567256,-1.185545,-8.617560,-7.113774,-6.627177,-0.662064,-7.088013,1.190210,1.783037,5.205001,-5.938100,6.863847,6.495657,0.489336,8.525423,-9.254677,7.904598,-2.294775,9.272901,8.629278,2.810204,6.558340,5.116273,-6.041053,8.512121,-4.204372,1.290674,2.971918,-9.568779,-1.935577,2.961269,6.030643,7.292559,-9.457741,-6.487756,-6.414351,1.336603,-1.553244,-8.003892,-8.598292,-6.247294,-8.420988,-1.434395,-5.733721,-8.940385,-8.028254,-1.162098,-7.834512,6.106179,-4.239066,8.439213,4.023324,-7.755610,5.810769,-3.806388,-9.863361,-3.781900,-7.099582,-9.605605,-4.239720,8.925280,-3.206839,-9.169359,8.868978,8.629224,0.995923,-0.496962,-8.095738,-8.538711,-4.251166,4.223525,1.376944,3.251997,-0.113375,5.848319,-3.128659,9.498137,-0.622478,1.783670,7.266393,2.246221,0.694970,6.825846,-7.213635,7.658575,-4.384764,2.095896,9.324791,4.547828,-0.259125,-6.072627,6.917272,6.739274,2.127390,1.745115,3.563628,5.731246], dtype = "float64")#candidate|2876|(160,)|const|float64
call_2875 = func_1423_call(relay.reshape(const_2876.astype('float64'), [16, 5, 2]))
call_2877 = func_1423_call(relay.reshape(const_2876.astype('float64'), [16, 5, 2]))
output = relay.Tuple([const_2863,bop_2870,call_2875,const_2876,])
output2 = relay.Tuple([const_2863,bop_2873,call_2877,const_2876,])
func_2900 = relay.Function([], output)
mod['func_2900'] = func_2900
mod = relay.transform.InferType()(mod)
output = func_2900()
func_2901 = relay.Function([], output)
mutated_mod['func_2901'] = func_2901
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2445_call = mod.get_global_var('func_2445')
func_2446_call = mutated_mod.get_global_var('func_2446')
call_2912 = relay.TupleGetItem(func_2445_call(), 1)
call_2913 = relay.TupleGetItem(func_2446_call(), 1)
var_2914 = relay.var("var_2914", dtype = "float32", shape = (2, 11, 8))#candidate|2914|(2, 11, 8)|var|float32
bop_2915 = relay.bitwise_and(call_2912.astype('uint8'), var_2914.astype('uint8')) # shape=(2, 11, 8)
bop_2918 = relay.bitwise_and(call_2913.astype('uint8'), var_2914.astype('uint8')) # shape=(2, 11, 8)
func_1423_call = mod.get_global_var('func_1423')
func_1426_call = mutated_mod.get_global_var('func_1426')
const_2925 = relay.const([3.023243,9.946054,-4.927794,5.631587,-4.127135,-7.770205,2.266288,1.604536,-1.683144,4.096755,-1.221393,5.852222,-6.658543,-5.223709,6.385605,-3.652584,-3.416538,8.625908,-6.365557,-2.563577,0.748432,-2.801698,4.567518,-2.171947,2.841372,-4.431581,-3.969588,2.435779,-1.720496,-3.248524,9.085932,8.795420,-5.044348,6.088268,2.625426,-7.334937,-7.763616,2.314192,-3.684390,-3.593831,-4.897095,1.487210,-8.368058,6.621845,-6.269095,-3.227348,-7.829236,5.256788,-6.525504,7.438562,1.002569,2.315395,-1.113090,9.415330,-6.598559,2.527153,3.303230,9.732571,3.673530,-1.453519,-4.061578,-4.314604,-3.064115,-1.301242,-8.426174,-4.627956,4.680097,0.867427,6.597056,-2.223625,-8.946382,-7.465166,-2.845572,2.132848,-0.116379,6.743537,-9.293339,0.418263,2.961044,-4.588947,6.256526,8.292129,-3.454290,7.294010,-0.502641,8.501770,7.842768,-2.864139,-6.572568,1.829947,4.091993,1.759137,-9.956596,0.865627,-8.981987,9.778171,-1.729417,-1.135193,-6.117705,-0.701190,2.413076,7.719070,9.278017,-0.476447,-4.064631,-9.041789,-4.460995,1.881893,-7.189586,6.780021,-6.827590,7.428075,2.115924,0.048671,4.789968,-6.235303,-2.504282,1.011074,3.506393,7.163586,6.188254,-7.975635,4.707534,9.750856,-9.411371,1.456088,4.442695,5.651580,-2.307997,-5.589126,1.255379,3.678910,4.553461,0.934136,-4.602645,-5.802209,0.472239,-8.963116,-8.910227,-5.099693,-8.170865,-4.922172,-3.431949,-1.861037,-8.538583,-0.634295,-8.778803,2.724428,-9.919733,-4.906828,5.013810,8.505622,2.719650,-5.223050,2.872938,-8.062089,-2.137112,5.089519,7.487216,3.077788], dtype = "float64")#candidate|2925|(160,)|const|float64
call_2924 = func_1423_call(relay.reshape(const_2925.astype('float64'), [16, 5, 2]))
call_2926 = func_1423_call(relay.reshape(const_2925.astype('float64'), [16, 5, 2]))
func_2626_call = mod.get_global_var('func_2626')
func_2632_call = mutated_mod.get_global_var('func_2632')
const_2937 = relay.const([-9,-1,-1,4,4,-8,-4,4,-10,-4,9,3,-5,9,-10,-3,7,7,-10,-10,2,-7,-7,-10,6,-1,5,10,6,9,-10,-4,8,-4,4,-5,2,-3,-2,7,6,4,-3,-3,-6,5,-5,-2,4,-1,10,7,7,2,-2,9,8,-1,-8,9,7,9,-5,-6,6,7,5,-9,-3,-4,-1,-3,6,1,-10,-7,6,-10,-8,-8,-6,-2,9,5,-2,7,2,2,7,2,-6,4,-9,-3,-3,-3,7,1,-7,-8,-5,-2,-8,-5,-10,10,-9,7,1,5,10,6,-5,3,-3,-1,-7,-5,7,-8,8,4,4,-5,1,2,10,-9,5,7,3,6,10,5,-3,6,-2,-1,2,-3,6,4,-1,2,-5,6,6,-9,3,-6,6,-10,-10,7,6,5,-3,-9,2,-4,10,-4,-10,-5,-7,-1,-2,-3,1,6,-10,-9,-2,9,10,10,1,-8,-8,-8,-5,10,-10,-2,5,-6,1,-7,-4,6,2,-3,1,-8,6,4,2,1,-8,-3,-2,-7,-6,7,-3,-5,-8,-9,-2,8,10,-1,5,-4,-4,-8,-8,1,-9,6,-9,6,9,-8,10,-9,7,1,-2,7,-4,4,7,-7,-2,-8,-4,-10,-8,4,-2,8,-4,1,6,4,2,3,1,-8,3,-4,10,9,-10,-6,7,2,-5,-9,-3,-10,-1,6,10,-5,-8,9,-2,-8,3,-5,-9,6,-1,2,10,-9,-4,-2,-9,-9,-5,6,9,2,-7,-6,5,8,-7,-2,-2,-5,-7,3,6,-2,-10,-10,10,1,-8,-4,9,3,-2,-10,-5,3,5,-8,7,2,6,-6,-4,6,6,-9,9,10,6,-8,-6,-2,10,-2,10,4,-5,-4,1,-5,9,-1,-5,-2,10,1,-4,9,-3,-10,-6,-10,-7,2,-4,5,2,-4,7,-5,9,-5,8,-6,6,5,10,-2,10,7,4,9,-7,10,-10,-3,2,-9,-5,-3,-1,-2,4,10,-2,7,-6,-10,9,9,7,-8,1,1,-4,-6,3,-6,3,-10,-10,1,-3,-10,-2,-4,2,-10,-1,6,5,8,9,-4,1,-9,3,8,-4,-10,9,7,-8,-2,-8,-4,-2,1,-8,6,-9,10,-9,-7,9,1,-5,-9,5,-2,2,6,-10,-5,-1,8,10,-1,-8,-3,-10,-5,5,10,5,-3,-7,1,7,6,1,-8,-3,3,9,-10,-10,-6,9,5,7,3,10,-3,-3,2,4,6,-1,1,-5,-1,-6,-2,-2,-10,-8,4,8,4,6,-5,6,-2,-10,-6,-5,-2,5,-5,2,5,10,-7,-7,-10,-6,7,-8,-8,-1,-5,-5,-7,-10,7,-2,1,4,-10,6,-5,-9,-4,-3,-7,-1,1,9,4,4,5,-4,8,4,-10,-10,-3,-9,-5,-3,7,5,8,9,7,-3,-7,-7,-6,3,-3,3,1,5,4,-8,-10,10,7,9,-1,6,-1,5,6,-5,10,-5,8,6,-9,-3,-7,6,2,-10,10,-3,9,-10,5,-5,3,-7,-1,-5,9,-9,10,-10,3,-7,6,-5,7,1,1,8,-6,-5,2,-7,-7,-7,2,-1,-9,-9,8,1,9,7,8,6,-4,2,2,-7,6,7,-3,-2,-7,-7,-6,2,8,7,-7,-3,7,-9,5,-9,-1,-8,7,7,2,10,-10,-3,-2,-6,7,-1,5,3,-7,-10,9,3,7,-1,-3,6,5,-4,2,-7,-1,3,-10,5,-9,6,-2,-5,10,-7,8,8,3,-10,2,-3,-8,1,3,5,-3,-1,3,-4,-3,-8,6,-6,-8,5,-6,4,-5,9,-1,9,7,-8,7,5,-5,-2,-9,-10,-7,-6,3,4,-5,7,9,-9,-7,9,9,5,7,4,6,-2,1,3,-1,6,-1,-3,1,9,1,4,-3,5,-6,5,-5,4,-8,3,-3,-5,-2,-5,10,-4,3,10,-9,-8,-4,-7,-2,8,-8,-9,-10,5,5,-6,5,6,10,-6,3,-3,6,7,-1,-10,-5,-9,-7,6,4,7,-4,9,-10,-10,-8,-9,3,4,4,4,-5,4,-7,4,-4,5,3,-1,-9,-6,-6,-3,3,-4,3,6,-10,2,5,-3,4,-9,9,9,-3,-9,10,-7,-1,-9,8,4,10,-7,9,-3,5,-9,-2,-6,-1,-1,9,3,-8,6,-2,5,-6,4,-4,10,9,-8,10,-5,1,4,-3,-1,1,-8,-8,4,9,1,7,3,-3,-6,-6,-3,-6,-6,6,-1,-3,-2,3,-6,8,-6,-1,10,1,-8,-8,4,10,2,-5,2,3,10,-4,8,6,-4,6,-2,3,-4,2,4,7,-7,10,-10,-7,-8,-7,-10,2,-1,-1,5,-6,2,6,10,-3,-4,10,5,4,-8,-10,5,4,8,2,7,2,-6,7,-4,4,-3,-3,2,2,10,8,-1,5,6,-5,-3,-4,9,-6,-6,-2,5,-7,-3,-8,-10,2,9,-3,3,1,8,7,-9,-2,-3,3,-8,-8,-1,5,5,3,5,10,-7,-5,6,-4,-7,1,-9,-10,7,9,4,-9,3,4,9,7,-5,-3,-6,-8,-3,5,-3,10,-4,-8,-5,9,9,8,-7,8,-7,3,-9,-8,-7,-6,-9,10,7,4,-3,2,6,3,-2,5,9,-5,-8,1,-6,-6,3,-8,2,-2,7,-10,-3,6,2,-5,9,1,2,3], dtype = "uint8")#candidate|2937|(1024,)|const|uint8
const_2938 = relay.const([[-5,-2,7,-8,-1,-3,5,10,-6,7,2,-10,-8,2,2,1,-5,2,8,-5],[3,4,3,-9,8,9,-3,-9,-1,8,-1,3,-2,7,5,9,-2,-7,8,8],[-1,5,7,6,-7,3,3,-5,1,7,6,5,10,4,9,5,8,-3,-6,-3],[3,-2,-4,-5,8,2,-7,-3,10,-6,-7,8,-3,-10,-1,-3,-1,-5,1,-1],[-10,-5,3,-8,3,-1,-7,8,3,8,-1,8,-5,10,-3,-4,-5,1,-7,10],[-3,2,3,9,-6,-9,7,2,2,-9,-2,-7,-4,-4,7,10,-8,-9,10,6],[-4,-4,2,-6,-7,-7,-8,7,-3,4,6,4,-4,-4,3,-2,-3,-10,4,9],[-1,-2,1,2,10,-7,-9,2,-4,-10,4,-3,-10,-4,-1,8,9,2,9,7],[-1,8,5,-5,-4,-7,-9,-7,-7,7,-6,-1,-5,7,8,-3,-10,1,9,-6],[3,3,-6,-4,3,-1,6,-6,-5,-3,8,-6,-5,6,4,-8,7,-10,-2,-6],[-6,6,8,-3,4,10,1,2,2,1,2,-3,-9,-2,9,-7,-4,7,6,7],[-5,4,2,4,-6,9,4,-6,7,5,-5,-9,9,3,7,5,-6,7,-7,-9],[8,8,2,-7,2,-2,-8,6,-8,-1,8,6,5,1,6,4,9,-8,-7,-7],[6,-6,2,-2,-2,7,8,-3,7,-6,5,9,-3,-5,1,-1,-3,3,-10,10],[-5,1,10,-8,-9,2,-6,10,-7,4,-6,6,4,7,-2,6,-3,3,-5,10],[7,10,4,-5,-2,10,-3,-1,4,1,-6,5,5,1,-9,6,3,-1,3,-8],[4,6,4,4,-5,4,-1,-1,7,8,2,-3,-9,4,10,-10,-1,2,2,-3],[-1,10,-8,-10,-2,-2,-4,1,-9,7,10,4,4,9,1,4,-1,-4,3,5],[-6,-2,-1,-6,-10,10,2,3,9,1,4,-10,10,-5,9,10,8,-6,5,-1],[-6,-6,4,-4,1,-3,-3,-1,8,-7,7,-2,7,4,-1,8,-8,6,4,-7],[5,2,-4,10,9,10,-3,3,-2,4,3,-1,-6,3,8,5,-1,-1,9,8],[9,6,-2,-3,-5,10,-1,-9,1,-7,3,2,10,-10,7,9,-7,9,3,6],[3,7,10,-10,-9,7,2,9,-5,1,6,7,4,-3,-9,4,-8,5,9,6],[-4,-4,-2,-8,-10,8,-8,9,2,8,4,3,-5,7,-4,3,-8,4,-10,9],[-1,5,-4,3,10,-7,-7,6,9,-7,-10,10,-7,-8,-9,6,5,-1,-10,3],[10,-6,-10,-9,10,1,6,6,10,-2,-2,-8,10,4,-8,1,6,-6,-10,5],[-3,-9,-2,4,-10,8,5,-1,-9,-6,-1,-4,-4,5,-5,5,-1,-9,-1,2],[1,5,9,-10,10,-3,5,-10,-10,-3,9,5,4,10,8,7,5,-3,8,1],[3,9,-5,-7,5,-2,-9,4,-10,7,8,5,-5,-6,-6,-9,2,5,6,-10],[3,7,8,5,6,6,-5,-7,-3,-3,1,6,-1,-9,-4,-10,-3,-8,10,1],[-5,-2,-1,-3,2,-1,-10,-6,-9,-10,6,-9,8,-1,3,4,10,8,-5,-6],[-9,-1,4,-9,-4,8,-10,-10,6,-7,-5,7,-9,1,-8,-4,-3,-7,4,-2],[7,-8,-6,-5,2,-3,5,6,-7,-9,-1,-3,9,3,-7,10,4,-1,6,7],[10,-7,-10,-8,-10,-3,1,7,-7,1,-5,10,-9,-2,-8,5,8,2,4,6],[-8,-5,6,-7,10,9,-1,7,-1,-6,-7,-9,-10,-5,-1,-6,-4,8,-3,-5],[4,-8,-4,-4,-3,5,9,7,5,6,6,4,5,10,-6,-10,-8,5,5,-6],[-10,-10,-7,2,2,-9,-2,-8,5,-2,4,5,-2,5,-2,6,4,-4,-7,-2],[-4,7,3,2,5,3,8,1,-8,7,-7,-3,3,1,-4,6,3,-4,9,6],[-2,3,-7,-1,-1,5,3,1,5,-3,7,5,-5,8,-6,7,-5,9,-5,7],[9,5,1,-10,-2,-3,4,-10,-8,-10,5,4,8,-10,-6,-8,-10,-8,9,-5],[-1,-1,-8,-2,9,3,-1,-2,4,9,-10,4,-10,-8,10,-1,4,6,2,10],[-3,-5,-2,3,-2,6,1,-1,2,-1,5,-5,-3,10,-10,7,3,-8,-1,-1],[-5,-5,6,-7,-7,5,2,2,-1,-1,3,4,1,1,3,7,10,2,9,-8],[-10,10,-3,7,5,6,-7,-3,2,-4,-7,-1,-4,7,-6,2,8,-6,-4,-4],[3,4,10,-10,-3,-7,5,9,5,-3,-1,-5,-6,-9,-5,7,2,-10,3,5],[2,6,2,-7,1,7,4,2,-6,10,3,1,-3,8,-9,-9,6,2,-3,6],[8,8,7,4,9,5,3,7,-7,1,-1,8,-8,-7,9,2,9,1,-10,-9],[1,10,10,-10,-4,2,1,-3,10,7,5,9,1,-10,-7,9,3,-1,-9,-7],[-10,-10,-8,-8,-5,10,-4,6,2,-6,4,-6,7,9,8,10,-4,-7,-5,3],[-9,2,5,-1,-3,-6,4,-6,-9,6,-1,-5,9,1,8,6,8,-3,3,8],[10,-4,5,-5,5,4,-10,-4,1,-2,9,8,-5,10,4,-5,3,-9,1,5],[-3,-3,9,1,3,1,-3,-9,8,8,9,-6,-3,1,7,10,-6,-5,10,-5],[3,-5,4,7,-3,-6,6,-5,7,5,-1,-5,9,3,10,-4,-5,9,3,3],[-1,-8,-9,8,-8,-1,7,7,-8,7,8,10,8,-3,5,9,-3,3,-2,9],[3,9,5,-7,-6,-10,-4,8,-10,-5,4,-3,2,10,-8,-2,-10,2,-6,-10],[-1,-7,-1,-9,3,-9,9,-6,9,-3,-7,-7,-7,-2,-6,-5,3,4,-6,-6],[-8,-8,7,7,1,3,4,-5,-7,-4,-1,1,-3,-9,-1,-10,2,-5,-3,6],[-2,-4,-7,7,-7,-8,-10,-4,8,-3,-10,8,-10,-2,-7,9,-7,6,-3,1],[-4,8,-2,8,-6,8,4,10,1,9,2,7,-2,-5,-6,4,-7,-5,-7,-6],[-3,-10,2,-1,2,1,7,-3,-3,-3,-7,10,-9,1,-7,10,-3,7,2,8],[-9,8,-9,6,-1,2,5,-2,-8,-2,-1,-6,-5,-10,4,-1,-9,8,3,-1],[-10,2,8,10,6,10,6,-4,3,-8,-3,8,9,3,10,6,-8,7,-4,-1],[-1,-10,9,10,9,6,8,-6,-2,10,-3,-3,-7,-9,9,1,-1,9,-6,-3],[-6,9,-5,-2,3,10,-8,-1,5,-6,-1,6,-2,3,3,-5,5,4,8,-8],[8,1,4,3,-3,6,7,-6,-7,7,5,9,-5,-1,-9,-5,10,2,-7,5],[-5,-2,3,3,8,-9,1,4,-1,10,7,-6,9,-1,5,6,7,4,9,9],[7,-2,-8,-4,-5,-8,10,-9,1,7,6,-8,5,-2,-7,-2,10,3,-4,6],[3,-2,-5,-2,-3,-4,4,1,-2,-4,5,-5,3,3,-7,5,-1,3,-9,4],[-5,10,-8,9,-5,3,10,-7,6,-10,-10,-4,-3,-9,-1,-4,-1,6,-5,-3],[7,-2,-4,1,10,-4,8,3,5,4,5,10,2,5,-10,-10,4,5,-5,-9],[-10,5,-3,9,-10,-3,1,-1,1,4,6,-10,8,-10,6,7,-6,-3,-3,-8],[5,8,-7,1,-4,-1,9,-3,-9,-9,4,-10,-10,-1,3,-4,1,4,-10,7],[-8,-6,-10,-3,2,3,-9,8,5,-10,9,7,-5,-1,4,9,-6,10,-4,6],[-8,-3,3,-6,-3,7,2,5,2,4,-3,1,-10,7,7,-1,6,2,7,8],[-4,-5,8,6,5,-8,-3,-8,-2,-6,-10,-4,2,6,3,3,-10,6,8,7],[-9,10,8,4,2,-10,8,-9,-1,-2,-10,4,3,5,1,3,-1,-2,2,10],[8,6,-6,-8,9,-1,-7,8,-4,-1,9,5,-8,10,4,4,1,-10,7,2],[-10,-5,-8,6,6,-7,3,4,8,1,-5,6,5,3,-5,-9,7,-1,7,-9],[7,9,-5,-9,-8,-4,5,10,-5,-3,-7,-3,-6,-1,4,-9,3,8,2,10],[-10,-4,-4,7,7,-8,-4,-1,7,-5,-2,-1,2,-5,-7,-6,-9,3,7,1],[-2,8,-1,-6,9,-9,-8,7,10,-4,-7,5,1,9,6,1,10,5,6,-10],[-5,-7,-9,-10,-8,-5,5,3,6,5,4,1,3,5,-7,6,4,-4,-2,10],[-1,5,5,-3,9,-4,-3,-7,2,8,7,-3,1,-1,-2,-1,8,-8,-5,5],[-8,-9,7,-7,-7,8,9,4,9,-3,8,3,-1,2,-1,-1,7,7,-5,-3],[-9,6,-4,-10,-6,3,6,-2,4,-6,-3,3,-7,4,-5,4,-1,4,1,-10],[6,2,9,10,10,-10,10,-10,4,-1,-4,4,5,1,-9,-2,-4,6,8,9],[-1,8,-10,10,-6,-4,-6,-6,-4,7,-9,10,-3,7,4,9,4,-7,-8,10],[-8,4,3,-4,-6,4,-10,-9,3,-4,3,-10,-1,-5,4,2,-2,-7,-6,-3],[4,8,-2,-6,-6,-9,2,-7,-6,1,-8,5,9,4,-3,-8,6,10,6,2],[6,2,-3,-2,-3,-1,10,-2,8,-6,5,-9,-1,-9,-6,-8,2,-4,-1,4],[-1,-5,-10,10,3,10,-2,-8,-7,10,6,8,10,-3,-10,2,-1,-2,2,-1],[-10,2,10,-4,5,-2,6,10,-4,6,7,5,5,-9,3,-3,-10,4,-4,-7],[-6,1,1,-5,-2,8,9,7,3,10,-7,9,-7,-7,3,10,-5,9,-2,-2],[7,8,-3,9,-3,2,-3,7,-3,-1,-10,-6,-3,2,1,-4,4,-2,6,-5],[-2,1,9,5,4,-10,8,1,1,9,-5,-10,-2,8,-6,9,1,3,-7,3],[4,-6,-7,4,-10,2,5,-6,4,6,-8,-8,-4,8,1,3,-5,10,5,2],[6,-3,-5,9,-5,-1,-2,2,2,-7,3,10,8,2,3,-3,9,9,6,-3],[-5,-4,5,-2,9,-2,9,2,10,-5,9,2,-3,-2,-1,8,1,-2,9,3],[-1,-10,-5,-10,-8,9,-10,-3,-4,-1,-2,-2,10,-7,-7,-7,-3,1,-1,4],[5,-5,6,9,5,-6,9,-9,-3,-10,-7,1,5,-10,4,-6,-9,5,2,-5],[3,5,-9,-1,-1,5,9,9,-9,-10,5,3,8,-7,-3,7,-4,-8,-7,7],[1,5,7,3,5,2,-1,1,-4,-8,-1,-3,-7,9,-1,1,10,1,2,-5],[9,-4,-2,-8,3,5,2,2,10,-3,-10,4,-10,7,-9,8,2,6,7,2],[1,8,7,3,1,-8,-10,-9,7,4,-10,6,4,-6,8,-5,-5,-2,-2,10],[1,-2,-10,5,9,-5,-4,3,-3,-3,8,9,10,6,6,-3,5,2,-8,-5],[8,10,-1,4,-1,-6,-4,2,6,-3,-5,-1,-4,6,-10,3,-2,-2,3,8],[10,2,-9,-7,2,9,-8,8,5,-6,-4,3,-1,1,-10,9,-3,5,5,10],[1,5,-2,-3,-6,4,-9,7,3,-5,5,2,-5,3,-8,-7,2,10,6,3],[-6,1,-5,7,-6,-10,6,-10,-8,1,8,6,-2,6,-2,10,-7,3,-1,9],[-5,-8,-10,4,-3,-3,-6,1,-5,-8,7,3,10,7,10,-9,-2,8,9,-9],[8,3,10,2,2,-10,-9,-4,-3,-2,-6,8,10,-9,7,-1,-9,8,10,-5],[-1,3,10,-9,-10,-5,-2,4,6,-10,1,-7,6,10,-5,-10,9,-6,-5,-3],[-4,1,3,7,-9,4,8,2,7,2,8,10,-9,8,1,-9,4,-2,-5,6],[-6,8,4,-10,4,4,-7,-1,3,2,-5,-1,-1,5,4,4,4,5,-3,-8],[10,1,10,-6,5,9,9,8,4,7,-7,-9,-4,10,3,4,-1,1,-9,4],[-4,-4,4,-2,7,6,10,-6,2,-2,3,-6,-1,8,5,3,-7,-10,-3,7],[2,4,1,-8,6,-7,6,-3,-2,6,-5,9,-8,-10,1,-10,3,9,-6,8],[-7,-8,10,-9,-4,-2,-3,-10,-9,-3,8,-7,9,-8,3,4,-10,-2,-8,5],[-5,3,-9,1,3,-10,9,-5,-3,3,8,-7,-4,1,1,5,4,-4,-1,10],[-2,7,8,-2,-5,-9,4,3,7,9,-9,-2,2,-3,4,1,6,7,-1,6],[-4,9,1,8,-6,-3,-3,8,-4,2,-6,4,-10,5,10,7,4,-3,-10,2],[10,-10,4,-2,-9,-6,5,7,9,-7,1,2,-2,4,-8,7,-4,4,-5,6],[-9,10,-2,-1,7,1,-2,7,10,5,8,9,-10,-1,7,8,-10,4,-5,5],[3,-2,-1,-10,-10,10,-6,9,-9,-1,-8,6,9,-1,3,8,2,-2,9,-5],[-6,7,3,9,4,2,-1,9,-6,-6,-8,6,4,-4,-1,-2,-3,10,4,-10],[3,2,8,-6,4,5,6,-2,9,-3,-5,9,3,2,1,8,3,8,3,-6],[-7,9,-2,4,-8,-4,-2,-9,-2,-4,4,-9,-2,-8,2,-4,-7,-2,5,-2],[3,-4,-7,-7,5,-4,-3,-7,1,-2,1,3,8,-7,-1,5,-5,6,3,10],[7,8,8,-9,-1,1,-6,2,-10,-8,-7,7,-2,-3,10,-3,-1,9,6,-8],[8,9,-4,9,-9,6,-7,-10,-6,4,-8,3,7,9,-1,-8,-4,2,-7,1],[7,4,8,3,-6,-2,-3,4,-8,-3,7,7,-10,1,-9,5,-8,9,2,-2],[10,-5,-10,5,1,6,-9,1,-3,1,5,-7,7,-10,10,9,7,-3,2,-4],[5,-1,4,-8,-4,-8,-2,-9,3,-10,-3,-2,-1,-7,4,6,-3,6,6,-4],[-10,9,-9,3,-10,-4,-9,3,-3,5,-4,-7,-7,-6,-4,5,-3,7,3,-4],[2,5,-6,3,3,-9,10,-3,8,10,-10,-7,7,6,4,2,2,7,-8,-9],[10,-7,3,-5,-1,-2,-10,-5,3,-9,-3,-2,10,3,10,8,-10,-8,7,6],[10,9,7,1,5,-6,2,-3,7,-10,-8,5,-5,2,10,-10,-6,-2,-10,4],[4,-4,-9,-1,-3,-1,1,-10,3,-8,2,3,6,-2,10,-2,7,3,4,-2],[4,7,-1,2,9,-7,10,10,9,2,9,6,-1,3,2,2,1,1,-6,-6],[-7,-7,-6,2,-10,-5,-10,6,9,-7,-7,8,8,-9,-6,-3,-1,9,7,3],[6,8,-10,-7,6,-1,-5,-2,-10,-9,-10,-7,-3,10,-10,9,2,1,-2,10],[-6,-2,10,6,-6,4,9,9,-10,4,-2,5,10,6,8,-9,-7,-5,-4,-6],[-8,-8,-4,9,-6,5,5,3,-9,5,-5,2,-5,8,10,4,4,2,-1,-5],[1,-6,-1,-2,-10,-10,3,-6,10,10,7,5,7,1,-8,6,6,8,3,-10],[8,5,-1,-10,4,-1,5,4,5,2,2,5,-10,-7,-4,5,6,-1,-10,10],[-10,-6,-8,9,-6,7,8,7,-6,2,-3,1,-6,6,3,1,6,-10,-8,8],[-1,3,10,1,6,7,10,-9,-2,4,3,-1,-5,-5,-4,-6,-9,-6,8,-6],[-1,-2,-1,-9,7,10,-1,1,6,8,1,4,-4,1,-6,-4,10,-7,-8,5],[4,-7,10,2,4,-5,5,-4,-8,10,-2,10,-2,-4,-7,-8,-6,-5,-3,-2],[8,-9,-7,-3,8,8,8,3,-6,2,5,4,5,2,6,-4,-1,9,-7,-4],[6,6,-1,5,3,-3,-9,4,6,-1,-9,-9,9,-10,-10,1,6,1,-4,7],[4,-10,4,-7,9,5,5,10,-1,10,7,-1,-7,-2,-9,-2,6,-5,5,3],[2,-4,3,10,-6,-7,-2,-8,1,3,1,-2,-7,-9,9,-8,1,7,-8,8],[-9,-9,-7,3,-8,-7,-2,-6,-8,-1,1,9,1,-6,4,5,2,8,2,7],[-8,1,-5,-8,3,1,1,6,5,1,7,-5,-9,-6,4,10,-10,-3,9,-10],[-5,6,1,7,5,5,5,1,-3,-6,-2,9,9,-7,-5,1,-7,5,-1,4]], dtype = "uint8")#candidate|2938|(156, 20)|const|uint8
var_2939 = relay.var("var_2939", dtype = "uint8", shape = (275,))#candidate|2939|(275,)|var|uint8
var_2940 = relay.var("var_2940", dtype = "float32", shape = (500,))#candidate|2940|(500,)|var|float32
call_2936 = relay.TupleGetItem(func_2626_call(relay.reshape(const_2937.astype('uint8'), [1024,]), relay.reshape(const_2938.astype('uint8'), [3120,]), relay.reshape(var_2939.astype('uint8'), [275,]), relay.reshape(var_2940.astype('float32'), [10, 50]), ), 8)
call_2941 = relay.TupleGetItem(func_2632_call(relay.reshape(const_2937.astype('uint8'), [1024,]), relay.reshape(const_2938.astype('uint8'), [3120,]), relay.reshape(var_2939.astype('uint8'), [275,]), relay.reshape(var_2940.astype('float32'), [10, 50]), ), 8)
output = relay.Tuple([bop_2915,call_2924,const_2925,call_2936,const_2937,const_2938,var_2939,var_2940,])
output2 = relay.Tuple([bop_2918,call_2926,const_2925,call_2941,const_2937,const_2938,var_2939,var_2940,])
func_2945 = relay.Function([var_2914,var_2939,var_2940,], output)
mod['func_2945'] = func_2945
mod = relay.transform.InferType()(mod)
var_2946 = relay.var("var_2946", dtype = "float32", shape = (2, 11, 8))#candidate|2946|(2, 11, 8)|var|float32
var_2947 = relay.var("var_2947", dtype = "uint8", shape = (275,))#candidate|2947|(275,)|var|uint8
var_2948 = relay.var("var_2948", dtype = "float32", shape = (500,))#candidate|2948|(500,)|var|float32
output = func_2945(var_2946,var_2947,var_2948,)
func_2949 = relay.Function([var_2946,var_2947,var_2948,], output)
mutated_mod['func_2949'] = func_2949
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2252_call = mod.get_global_var('func_2252')
func_2254_call = mutated_mod.get_global_var('func_2254')
call_2962 = relay.TupleGetItem(func_2252_call(), 0)
call_2963 = relay.TupleGetItem(func_2254_call(), 0)
var_2965 = relay.var("var_2965", dtype = "float32", shape = (2, 7, 8))#candidate|2965|(2, 7, 8)|var|float32
bop_2966 = relay.greater_equal(call_2962.astype('bool'), var_2965.astype('bool')) # shape=(2, 7, 8)
bop_2969 = relay.greater_equal(call_2963.astype('bool'), var_2965.astype('bool')) # shape=(2, 7, 8)
output = bop_2966
output2 = bop_2969
func_2971 = relay.Function([var_2965,], output)
mod['func_2971'] = func_2971
mod = relay.transform.InferType()(mod)
mutated_mod['func_2971'] = func_2971
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2972 = relay.var("var_2972", dtype = "float32", shape = (2, 7, 8))#candidate|2972|(2, 7, 8)|var|float32
func_2971_call = mutated_mod.get_global_var('func_2971')
call_2973 = func_2971_call(var_2972)
output = call_2973
func_2974 = relay.Function([var_2972], output)
mutated_mod['func_2974'] = func_2974
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2998 = relay.var("var_2998", dtype = "uint32", shape = (9, 8, 11))#candidate|2998|(9, 8, 11)|var|uint32
const_2999 = relay.const([[[-4,-7,-4,-7,8,4,-2,-5,7,7,-2],[-6,6,9,-4,6,-5,-4,7,7,-1,3],[1,4,-3,8,1,10,-1,-3,-3,3,-3],[-8,-2,8,-7,-9,-8,6,3,9,-1,-5],[-8,-7,9,-9,-1,-3,-4,-6,-1,-1,7],[2,-3,-8,-10,7,3,-8,-6,-3,8,9],[8,-4,2,9,1,1,-2,8,-4,-1,1],[-7,8,3,9,-7,9,7,-7,1,10,3]],[[5,-6,-8,-5,-6,-5,6,10,2,-2,1],[4,-10,5,1,3,-1,4,-4,8,3,4],[-3,-5,-6,-8,10,6,-9,9,-10,5,-3],[-9,-9,-7,-10,4,-9,-8,7,3,-10,-7],[-1,8,-1,1,1,1,8,-4,2,4,8],[8,10,3,2,6,6,-3,6,-3,5,-8],[-3,-3,-4,-8,-9,-6,-10,6,8,-7,5],[-3,5,9,-9,5,3,7,-5,8,1,-10]],[[4,7,7,6,6,-4,-7,-5,1,-8,-7],[2,10,-3,-5,-6,-8,-10,-6,8,10,-7],[4,3,1,10,6,8,-3,9,-4,8,7],[-9,-6,7,9,-3,5,10,7,1,-3,9],[2,3,-2,-9,1,-2,-5,5,4,-8,-3],[-4,-10,6,-6,9,-3,-5,5,4,4,-3],[4,4,5,6,2,-10,4,6,-1,7,9],[-8,8,2,-7,-10,4,-10,7,9,-7,2]],[[5,3,-2,1,-4,10,3,3,-9,-5,-8],[2,-3,5,-9,3,-4,1,9,-9,-1,5],[1,5,1,-2,5,4,-4,1,-5,-7,-3],[5,8,-6,-5,4,9,7,-9,6,-3,-5],[-9,-2,3,1,8,9,-2,-7,-6,-2,-10],[2,9,5,-8,1,-7,10,-2,5,1,-8],[-8,1,-7,6,3,9,6,4,-4,-1,-7],[10,-6,-9,-10,-1,3,-10,-4,-8,-6,8]],[[10,-8,-6,7,4,5,4,-6,-3,3,-8],[6,1,8,10,-1,-8,9,2,9,5,5],[-8,-6,-9,-6,-1,-8,6,-4,-3,-1,8],[5,7,-5,6,2,2,-4,6,-9,-2,-3],[-6,-9,4,8,-9,1,6,8,5,-5,-9],[-1,1,-4,-8,3,6,2,1,1,2,-6],[7,2,4,-10,-8,-8,2,4,-10,5,-9],[5,7,-2,5,9,1,-3,-1,-10,5,-10]],[[3,-8,-10,-1,10,-1,-2,-5,-10,-1,8],[-10,9,7,-1,3,-10,-6,-6,1,3,-10],[-4,1,1,-9,-6,-9,-8,-2,-3,2,8],[6,-7,7,-9,-4,-3,-9,9,-5,-6,1],[-1,4,8,9,-5,9,2,-3,-4,-5,6],[-3,-1,-7,3,10,10,9,-9,-5,5,-10],[1,-9,-2,4,-8,10,-5,6,-8,-5,-2],[8,5,8,9,-1,3,7,-4,-3,8,-4]],[[4,-5,10,-1,-6,-6,4,3,1,-6,-3],[10,-6,4,10,-10,-9,7,5,-2,8,-4],[-1,6,2,-8,6,6,5,-5,7,-7,10],[-8,3,8,7,4,10,3,5,-8,-3,1],[4,1,1,8,6,-8,7,10,9,-3,5],[2,-9,-1,5,-8,-9,-10,1,-4,3,3],[10,-3,9,-8,4,-6,-10,-5,10,4,6],[-10,2,-1,-7,-7,10,-4,8,5,1,6]],[[8,-6,9,-8,4,2,-3,10,-9,-5,-7],[-10,-4,-10,6,-8,-9,5,-4,3,-2,-1],[7,-2,-10,-5,-9,-3,-10,10,9,4,-2],[-8,-1,-4,7,7,9,-10,10,6,-2,4],[2,-10,2,8,5,2,-8,-1,2,-9,-9],[1,-6,-1,-6,2,9,-8,8,-8,-4,10],[-5,-7,7,1,4,-5,9,-9,-1,4,5],[-4,1,-5,-10,-9,6,-3,9,-10,6,-3]],[[3,1,-3,5,-8,-10,-9,-4,-1,-6,-6],[-9,5,-9,-7,5,4,-4,-10,6,6,-4],[2,5,-10,2,2,-2,3,7,4,9,-9],[-7,-2,6,9,-4,-8,8,-2,6,4,-2],[-9,-8,-4,-3,10,9,-2,-9,-4,4,3],[-2,2,2,5,-4,4,7,7,-10,-1,8],[-5,6,9,3,-4,9,-2,4,5,-2,-8],[-9,-3,3,-10,-7,7,4,5,-1,4,-5]]], dtype = "uint32")#candidate|2999|(9, 8, 11)|const|uint32
bop_3000 = relay.greater(var_2998.astype('bool'), relay.reshape(const_2999.astype('bool'), relay.shape_of(var_2998))) # shape=(9, 8, 11)
output = relay.Tuple([bop_3000,])
output2 = relay.Tuple([bop_3000,])
func_3034 = relay.Function([var_2998,], output)
mod['func_3034'] = func_3034
mod = relay.transform.InferType()(mod)
mutated_mod['func_3034'] = func_3034
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3035 = relay.var("var_3035", dtype = "uint32", shape = (9, 8, 11))#candidate|3035|(9, 8, 11)|var|uint32
func_3034_call = mutated_mod.get_global_var('func_3034')
call_3036 = func_3034_call(var_3035)
output = call_3036
func_3037 = relay.Function([var_3035], output)
mutated_mod['func_3037'] = func_3037
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2802_call = mod.get_global_var('func_2802')
func_2804_call = mutated_mod.get_global_var('func_2804')
call_3121 = func_2802_call()
call_3122 = func_2802_call()
output = relay.Tuple([call_3121,])
output2 = relay.Tuple([call_3122,])
func_3123 = relay.Function([], output)
mod['func_3123'] = func_3123
mod = relay.transform.InferType()(mod)
output = func_3123()
func_3124 = relay.Function([], output)
mutated_mod['func_3124'] = func_3124
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2900_call = mod.get_global_var('func_2900')
func_2901_call = mutated_mod.get_global_var('func_2901')
call_3148 = relay.TupleGetItem(func_2900_call(), 3)
call_3149 = relay.TupleGetItem(func_2901_call(), 3)
func_1598_call = mod.get_global_var('func_1598')
func_1601_call = mutated_mod.get_global_var('func_1601')
const_3154 = relay.const([-5,4,-6,-6,-8,1,9,-8,-2,4,9,8,-6,4,9,4,4,-2,2,7,-2,-3,-8,9,-5,3,-6,4,3,-10,5,4,9,-2,-1,2,-7,-8,6,-6,-10,-9,-9,-8,10,5,-1,5,-5,10,7,-1,7,-9,7,-7,4,3,8,-6,-1,-6,-9,10,-7,10,-4,-8,10,-5,-5,-4,-8,-2,8,7,-10,2,3,3,-4,-5,4,9,-3,9,-9,-6,-9,5,8,-9,-6,-8,-2,-8,4,5,9,9,2,-9,-2,2,-5,3,1,-4,2,6,4,4,-9,3,-5,-7,4,-2,3,10], dtype = "int64")#candidate|3154|(120,)|const|int64
call_3153 = func_1598_call(relay.reshape(const_3154.astype('int64'), [4, 10, 3]), relay.reshape(const_3154.astype('int64'), [4, 10, 3]), )
call_3155 = func_1598_call(relay.reshape(const_3154.astype('int64'), [4, 10, 3]), relay.reshape(const_3154.astype('int64'), [4, 10, 3]), )
output = relay.Tuple([call_3148,call_3153,const_3154,])
output2 = relay.Tuple([call_3149,call_3155,const_3154,])
func_3175 = relay.Function([], output)
mod['func_3175'] = func_3175
mod = relay.transform.InferType()(mod)
mutated_mod['func_3175'] = func_3175
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3175_call = mutated_mod.get_global_var('func_3175')
call_3176 = func_3175_call()
output = call_3176
func_3177 = relay.Function([], output)
mutated_mod['func_3177'] = func_3177
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2278_call = mod.get_global_var('func_2278')
func_2280_call = mutated_mod.get_global_var('func_2280')
call_3255 = func_2278_call()
call_3256 = func_2278_call()
output = call_3255
output2 = call_3256
func_3267 = relay.Function([], output)
mod['func_3267'] = func_3267
mod = relay.transform.InferType()(mod)
output = func_3267()
func_3268 = relay.Function([], output)
mutated_mod['func_3268'] = func_3268
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2900_call = mod.get_global_var('func_2900')
func_2901_call = mutated_mod.get_global_var('func_2901')
call_3298 = relay.TupleGetItem(func_2900_call(), 0)
call_3299 = relay.TupleGetItem(func_2901_call(), 0)
output = call_3298
output2 = call_3299
func_3302 = relay.Function([], output)
mod['func_3302'] = func_3302
mod = relay.transform.InferType()(mod)
output = func_3302()
func_3303 = relay.Function([], output)
mutated_mod['func_3303'] = func_3303
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2900_call = mod.get_global_var('func_2900')
func_2901_call = mutated_mod.get_global_var('func_2901')
call_3307 = relay.TupleGetItem(func_2900_call(), 0)
call_3308 = relay.TupleGetItem(func_2901_call(), 0)
func_2181_call = mod.get_global_var('func_2181')
func_2185_call = mutated_mod.get_global_var('func_2185')
const_3325 = relay.const([-6,5,7,-4,-2,-6,-6,1,-10,-5,-1,-1,-5,-2,-8,-8,9,10,9,-10,-6,-3,-1,-2,-9,10,-7,-7,-7,3,1,2,7,3,6,6,10,-6,6,-6,6,4,-6,-6,-1,10,10,-9,-4,2,-6,3,8,10,9,10,1,-9,-7,10,3,10,-2,10,-1,-7,1,-6,-3,-6,2,8,-1,10,3,6,2,9,4,1,4,-4,-1,-7,-5,-7,-8,-2,-3,9,-6,1,-10,1,4,9,3,-4,-4,-9,3,-7,10,-9,4,10,-2,8,-3,-6,-3,6,8,10,-10,-2,4,3,-9,-10,10,-2,1,4,9,3,-7,-9,9,-9,-8,-2,-10,-10,-7,3,10,-10,7,5,4,-9,-6,-7,10,2,7,-2,-8,8,-3,-3,-8,4,-6,1,-8,2,1,-7,-7,8,-4,3,-5,9,1,10,6,-5,4,4,-8,-6,-8,-9,3,-1,10,-2,6,-2,5,8,-8,4,1,-6,4,8,-6,-9,4,7,-7,-10,10,9,6,7,-2,-7,-6,-10,6,4,-4,-10,-6,-4,-6,5,-6,3,4,7,-10,-9,-9,9,-6,7,10,10,-4,1,1,-8,-2,3,3,-4,-6,1,9,-3,7,-6,-7,4,-3,1,-3,-4,-4,-1,-7,-3,-7,10,-6,-2,3,9,4,-1,-10,-4,-3,-8,-3,5,-5,3,-3,-7,-6,-4,-6,-6,8,-9,10,-1,-2,-2,-9,5,7,5,10,1,-2,-2,-7,9,8,6,-3,-2,10,-10,-1,5,4,8,-4,10,3,4,-4,7,-3,9,2,1,-5,10,-7,-6,5,-4,4,-6,-8,8,3,4,-10,4,-4,5,7,7,-10,-4,6,7,4,6,-2,-3,-2,3,-10,4,-3,3,-6,-3,-1,5,-6,7,4,1,-8,2,-1,-1,-1,3,6,1,6,10,2,-5,6,8,7,-7,-4,-6,2,-6,-4,5,6,-2,2,10,-7,-2,-8,2,-10,10,-8,8,4,2,-2,-10,7,-1,-5,-4,-7,-5,9,-2,-8,2,1,-7,4,4,8,-4,-7,-3,7,5,6,-1,-9,5,-5,7,-8,10,-2,8,8,7,1,6,-9,-2,-2,1,3,-3,4,-4,-2,4,9,-6,-6,-2,2,4,10,-8,8,6,-7,2,6,-2,2,-4,8,8,4,-2,10,10,4,2,9,-5,-6,-8,7,-5,-5,-8,1,-8,7,-3,-8,7,-3,3,-9,-8,9,9,5,-3,-3,5,10,-10,5,-4,-8,-4,1,3,-8,-5,7,1,8,-2,6,6,1,2,9,1,-8,8,-2,9,10,-5,2,8,-1,-2,10,-2,3,-8,-10,2,4,7,-9,-6,-4,7,-8,-5,-7,-5,-4,7,10,2,4,10,-3,2,7,2,-8,7,-6,-4,-1,8,-5,-5,-2,-7,-4,-2,5,-1,-3,-4,-4,6,5,-10,10,-4,-5,-10,-9,-3,3,9,1,-10,3,-7,5,4,5,8,4,-8,2,-7,-6,-3,-6,-9,-2,-3,-3,1,-6,-9,3,-4,-9,7,4,-2,4,1,8,1,7,7,6,7,7,1,-3,-8,-1,6,10,-6,-5,-6,-5,7,3,-3,3,9,7,-9,-6,5,-1,3,-10,6,7,2,-1,5,2,10,-7,-5,-10,-5,3,-4,-2,6,9,9,7,8,-8,-1,3,6,-2,-6,-7,-7,-2,5,-9,6,-4,-3,-6,-9,6,-7,-1,10,-5,-4,-7,1,3,1,-8,1,4,4,-7,-6,-3,1,-7,-7,-7,-5,3,2,-3,-1,2,2,6,-7,9,7,8,5,-10,10,-5,-2,10,-6,8,3,-7,-7,-2,-7,8,2,3,3,-2,-9,-7,-5,6,9,7,6,-8,-1,7,-9,4,-3,1,-8,-1,7,-9,-5,4,-9,-8,6,-5,-4,5,-7,7,5,8,-10,-2,6,-9,-6,-7,-3,7,-8,-6,-7,8,-9,-6,4,8,4,10,1,1,4,10,2,9,-2,-4,6,-4,8,9,-7,-3,7,1,5,-5,9,-10,-5,-10,-4,7,-6,-4,3,4,2,-1,3,7,3,8,-7,2,7,-8,-6,-10,-8,-5,-10,2,-8,-1,4,-8,-1,-10,7,10,-4,5,-5,-2,-9,-3,6,1,8,-5,-9,1,3,10,-3,-4,-3,7,-3,-1,6,3,9,7,3,4,-9,6,8,2,8,-10,-4,-9,8,3,-5,-7,8,4,10,-7,-2,-10,9,-4,7,-8,-3,-2,-8,-4,-1,9,-8,3,10,-6,-3,3,-10,8,10,-10,4,3,-7,7,9,9,9,-7,2,-1,2,6,2,-9,10,5,-9,6,-5,-6,-8,-6,-7,-8,-8,5,-7,-4,-2,1,-2,6,5,9,-4,8,10,-3,-9,-7,1,9,-2,5,5,6,4,-9,3,-3,-5,-2,-7,3,5,-2,-1,-2,-3,-6,7,-6,-5,2,-4,-6,-5,3,3,-7,5,5,-2,8,-6,-6,10,3,-8,5,7,-3,10,-4,2,-3,3,-3,-3,-10,9,1,1,-5,7,3,1,-8,-1,-8,-4,-8,-7,1,3,-10,-1,-2,-6,-1,8,9,-9,-4,1,-1,-3,1,-3,-1,-8,-9,-3,-9,-9,-2,-4,8,-9,-4,-4,-5,-6,-6,-3,-7,9,7,-8,-1,-9,-8,5,6,8,-6,7,-1,10,-3,-4,3,6,-5,8], dtype = "uint8")#candidate|3325|(1024,)|const|uint8
const_3326 = relay.const([-10,-10,9,-3,-8,-3,-10,7,2,2,-2,-1,-5,-5,4,-8,5,3,5,-2,3,-7,10,3,-8,9,-10,-8,-9,-5,-5,9,-2,5,-6,-2,2,4,-5,-3,-3,-3,-3,7,-6,-4,9,2,-4,1,-3,1,-4,7,-3,4,-3,1,8,5,-2,4,2,3,2,-6,-10,-10,3,4,10,-1,5,-8,-10,6,3,3,7,-1,-3,3,7,6,3,-5,-1,7,-8,10,9,10,-5,7,-1,10,7,-7,-9,4,6,4,-6,1,5,4,7,-5,-8,-6,-3,5,2,-6,-5,-10,10,6,6,-1,-1,4,-10,-4,-1,7,9,-6,4,-1,-4,9,6,1,-7,2,9,7,2,8,-2,-1,-9,-3,1,-3,4,9,9,1,-4,3,-6,3,-2,5,-7,6,-3,10,-2,9,5,5,9,8,-8,9,1,-5,-4,-8,9,9,-4,6,-10,-3,2,-6,5,-6,-7,10,6,1,-8,-1,3,-10,6,5,10,10,-6,-5,-4,-6,6,9,3,-2,-10,-9,4,2,-5,8,2,9,8,-1,-7,-3,2,4,3,6,2,8,5,8,4,-5,-7,6,-8,-8,-3,7,7,9,-9,5,10,-9,-3,5,4,6,2,-7,-1,5,-7,9,4,-6,-5,-6,4,2,-2,-7,-6,-8,-6,-9,9,3,6,2,2,-5,-10,-5,-8,-4,-3,7,-3,-8,-9,8,-2,-7,-2,10,-8,-2,10,5,-4,8,-9,7,-1,2,1,-9,-10,-3,7,8,-2,6,-8,8,9,9,3,1,-2,-6,-1,-8,-3,-5,6,-8,4,10,4,-5,-6,-4,-2,-4,7,7,-7,1,8,4,7,-4,-5,-4,4,5,-6,8,-1,-2,2,-6,-6,3,-3,10,9,3,-8,-5,8,2,-7,2,3,-8,-5,8,-3,7,-7,8,-9,-2,-7,9,6,-1,-2,-5,-9,1,-9,-7,-9,-8,9,4,6,7,4,-1,9,-7,7,7,-7,1,-5,-8,-3,1,-4,-4,-3,-6,-10,1,-10,-2,2,-2,6,-5,-4,-5,3,10,3,10,4,-4,6,6,6,3,-7,-9,10,4,-6,10,-7,7,-4,-5,-4,5,-8,5,8,4,-5,-6,4,9,-1,1,1,9,6,4,-4,-7,-9,-6,10,-10,-10,2,-10,-6,-1,-10,-7,-8,2,-1,2,-9,-10,-7,5,-7,-8,1,-9,-1,-5,3,-10,5,2,10,-3,6,-6,-6,-4,7,4,-2,-6,5,3,-5,10,7,-5,-7,-8,6,6,6,-6,4,3,-3,6,-2,8,6,-7,-10,-1,-5,-10,2,2,7,-3,8,-6,4,-10,3,-6,-4,1,7,2,1,-2,9,-3,4,9,1,-2,7,3,-8,8,-4,-9,-1,5,-3,4,-3,-2,2,-8,5,10,-1,-4,2,4,-3,8,-2,-5,-10,-10,-8,9,-2,-3,-6,-10,5,-6,6,-2,-3,-2,-3,-1,-7,-7,5,-5,2,5,2,-5,-9,-4,2,-3,-8,9,9,-8,3,1,3,5,3,-5,7,-2,10,-1,-3,7,-7,-7,-6,-5,10,5,2,-1,1,-2,4,5,1,8,10,7,10,8,-7,-5,10,10,-1,9,-7,-8,-4,-6,-9,-8,2,8,9,7,8,-3,-3,10,-6,-6,9,-3,-7,9,5,-6,-5,10,10,-8,-1,-5,-7,-8,4,-5,8,-8,-9,2,4,-3,-4,-1,-10,1,1,6,2,1,6,9,-6,-10,1,2,-1,4,-10,8,-7,3,-6,8,-5,-4,-6,6,7,10,-7,5,1,-3,-6,3,1,-3,-7,7,-9,2,1,1,3,5,-6,-9,-2,8,-5,-3,-8,-7,7,-8,2,-4,-9,10,6,3,-6,9,-7,5,-1,-2,5,6,1,8,8,-6,-7,-9,10,7,6,-5,6,-7,-8,-5,-8,7,-9,-3,-9,3,3,-10,-6,10,-4,5,5,-6,2,-10,-4,-8,-1,9,-9,-5,4,7,4,-2,-4,-10,-10,6,10,10,2,-7,2,3,8,-6,-5,2,2,-10,2,9,-8,4,2,2,-6,7,6,-7,-9,-7,-6,4,3,-6,5,7,-2,-3,-6,8,-5,8,-6,6,-8,8,1,3,7,9,9,-7,-8,5,5,-4,10,-2,6,2,10,-1,-1,5,6,-1,-3,-5,-9,4,6,4,9,2,3,-1,-3,4,-7,-3,-4,-9,5,5,-6,7,7,10,9,-3,-8,-5,-7,7,7,-10,-6,-7,4,-4,3,4,5,7,-8,8,5,6,-4,9,-3,-4,7,-8,3,3,3,7,-3,-2,3,4,-5,1,3,1,-8,-5,-4,5,-6,5,-6,-9,-7,10,1,7,6,5,9,-5,9,-1,2,-2,4,8,-2,-1,-8,-8,-6,-4,6,-2,-5,9,7,-9,-5,5,-2,3,10,2,6,-6,6,7,-1,-6,-7,2,-4,3,2,1,1,-8,8,8,2,6,-7,-2,3,-7,-5,-4,-8,8,-5,5,-1,-8,7,-2,-3,8,5,-8,-2,-1,-4,3,2,-3,10,-4,5,1,1,10,4,-3,10,7,6,8,-3,-1,2,-3,-4,-5,-10,-10,8,4,-7,-10,8,-10,5,2,7,-2,-9,-3,-3,-3,-5,-3,-2,6,4,8,-3,-4,-6,-8,-4,-4,-7,-8,-7,3,-6,4,3,-9,6,-9,-6,9,3,-7,-8,-10,9,-5,-10,6,-5,6,-10,7,4,5,10,4,-1,-10,1,6,-7,4,-7,5,-3,-10,-8,7,4,2,7,-9,6,-9,-9,-6,-6,-4,-3,7,-10,6,-5,-9,-6,2,6,4,-1,8,-8,6,5,8,-9,-1,-3,8,-2,6,-8,1,-10,-8,8,10,-2,-1,-6,-4,-6,-7,-4,7,-2,3,-1,-5,-9,-3,1,-4,-10,10,4,5,3,-8,-7,-2,-6,-8,-1,-10,-6,-7,6,9,-6,6,-7,1,2,-6,2,9,-4,7,-2,6,-9,6,-6,-5,-6,-4,3,2,3,-6,5,-7,2,2,10,-3,-5,-8,4,3,6,4,1,5,-1,2,-6,-2,-2,2,6,-3,-4,2,-4,-9,-2,-8,-8,-8,-3,4,-9,10,5,-3,7,2,7,-1,-8,-1,-3,3,3,-8,-4,-8,1,4,9,-6,7,2,-1,7,1,-10,-9,4,4,8,8,-1,-3,-4,-4,3,-8,5,5,-1,-10,-1,-1,10,-10,-3,4,7,1,-4,-2,6,1,3,5,-2,-2,3,1,1,2,2,-10,-7,-10,5,7,6,-5,2,1,-7,1,10,-5,-7,-7,-5,8,9,3,2,7,6,6,-4,-5,2,2,10,-3,4,-6,8,-3,3,-8,5,-4,-9,-2,7,-3,5,-9,1,-4,1,-8,-5,5,-6,-5,-10,4,9,-10,5,-5,9,7,-7,6,2,-8,-4,5,6,3,-10,5,4,8,-9,2,-9,9,-10,8,1,-9,9,-5,5,-2,6,6,3,1,-7,1,2,3,-4,-5,7,10,-1,4,4,3,-5,9,-3,1,3,-7,1,10,1,2,1,-5,-8,10,-6,9,-2,-9,-1,6,-4,1,-2,-5,-6,10,-9,-2,5,9,5,-1,8,-5,-4,-3,3,-6,-4,-10,7,10,7,3,3,1,1,6,-6,8,-1,8,6,-1,-4,3,-10,-7,4,-9,5,-7,-6,6,6,-1,7,-3,3,5,4,9,8,3,10,-1,3,-9,-2,10,1,5,1,4,3,-3,5,4,-10,9,8,4,7,2,-10,-7,4,-2,-3,8,6,-6,-3,-6,7,4,-5,-9,-4,4,-3,-7,-5,1,7,-6,1,4,10,9,-7,-5,3,-9,-6,1,5,8,8,10,9,8,7,5,6,-7,9,9,9,-9,2,6,-7,-9,-2,-2,-4,10,-4,9,1,5,9,3,2,2,-9,1,-3,-5,-1,7,-7,7,3,5,3,3,-6,9,-8,3,-1,5,7,10,-7,3,3,-9,-7,10,4,3,2,7,-5,7,-5,10,4,-9,-7,7,4,6,-10,-3,-4,6,10,-5,-6,-3,-9,-4,-2,-6,-5,9,-8,-3,3,-7,-4,-4,6,1,4,-2,8,-5,-9,7,3,5,3,2,-4,5,-1,4,8,9,1,4,7,10,-10,2,-5,7,-7,-3,9,8,-5,-7,-10,-5,-8,-10,8,-3,-9,4,-3,1,3,8,-2,-1,-1,-1,5,-3,5,-9,5,3,-6,5,9,7,10,3,-6,-10,-5,9,5,4,-7,-4,5,-4,6,10,5,-9,-7,-6,7,9,5,1,-1,-1,-7,9,-4,-3,-2,6,-2,-4,-7,1,6,-5,9,-2,-2,1,10,3,2,-4,1,-4,3,2,-8,-6,-3,5,9,-4,-4,4,4,-8,3,5,-2,-7,-8,-6,1,1,3,8,7,6,-9,-5,-8,-3,5,-5,6,-3,-2,-3,1,9,-1,-9,-2,-10,-5,-6,-8,-4,-5,-1,2,9,4,-6,-5,-10,-3,5,-4,-8,9,-10,1,1,2,10,7,7,-9,-6,-2,-1,3,-2,-2,-4,2,-10,-9,-2,-5,6,-2,-3,7,-5,4,-4,5,-6,6,-10,5,5,10,-6,10,7,4,-2,9,-2,7,-2,3,1,-7,2,-10,-7,-4,5,4,5,4,-2,9,8,1,-8,7,6,10,-7,4,-1,6,4,10,1,-9,6,7,3,3,2,9,-3,5,9,3,-10,6,10,-5,1,-4,-1,-3,6,-4,-6,-6,3,-1,3,-10,5,-6,3,8,5,-1,2,1,-9,-8,-1,6,-8,-6,-2,-5,-4,4,2,9,5,-6,-1,-6,-3,5,-1,-7,9,1,10,8,6,-1,-7,8,10,10,-2,-4,-3,10,-2,-2,-8,2,-8,4,-6,2,3,3,5,-7,-10,-3,-1,-6,10,4,2,8,8,-3,6,8,-9,-5,4,3,-4,-8,9,-8,3,-9,-1,4,8,6,5,3,4,-10,9,-4,-10,-10,6,10,-1,4,-5,-3,-10,-6,2,-10,-7,-5,-4,1,-9,6,8,-5,-4,-3,1,-1,5,-7,7,1,8,2,5,5,-4,-9,7,-3,5,2,-2,-7,2,-3,-1,-5,-2,-10,-10,-1,8,-7,4,-7,-6,6,-4,6,-9,7,7,1,-6,-6,-8,1,5,-2,-5,-1,-2,10,2,-3,7,2,-1,3,4,4,-4,-9,-10,-1,1,-8,7,-10,6,-9,-3,-6,4,2,7,-1,10,2,-2,-6,3,8,6,10,-9,-4,9,-7,-9,10,-4,7,-2,5,-1,9,-9,-5,-4,6,3,-8,-9,-5,5,-4,-10,-4,-1,-8,-9,8,7,2,10,7,-7,-6,-3,7,-10,-8,4,-5,-10,-9,2,-9,-3,-2,-9,6,5,4,-5,-7,-4,7,4,4,5,-5,1,7,4,-6,-10,9,-6,-5,-4,8,-7,5,-7,7,4,-2,-5,10,-10,-2,-1,-6,-4,8,3,-7,2,-2,-2,-4,3,1,7,-7,10,-7,-2,5,-6,-5,10,-1,-5,3,4,-4,-3,4,8,7,1,-6,9,-1,6,-5,-10,-1,9,-4,1,-1,5,-4,-5,1,-7,10,-2,-10,-9,-5,1,-5,9,-7,-7,7,-2,-5,4,-6,6,-6,7,7,2,6,-9,8,-8,10,-1,-7,6,1,-9,10,3,4,-1,-7,-2,-8,3,8,-9,7,3,-5,6,-10,3,2,5,7,4,1,-8,-6,-3,2,-3,1,3,-7,-4,-5,9,4,-1,2,-6,3,9,4,-4,-3,-5,4,-4,6,10,-4,9,2,8,7,-6,7,10,9,-8,-2,9,-1,-7,-1,-2,-7,-3,-3,5,-5,2,6,3,-5,-8,-4,-5,1,3,10,-9,6,-5,2,-1,-1,-9,5,4,5,-9,10,5,7,-5,5,3,7,2,-10,-6,-8,-7,1,4,-3,4,-8,-9,8,1,10,-7,-4,6,-4,4,-9,6,2,3,-5,-1,7,8,-5,-9,5,-2,4,2,10,1,-6,-9,-7,6,-1,-4,6,-4,-3,6,8,8,5,10,-7,-5,8,-3,-6,4,5,-6,10,-2,2,2,7,1,-1,5,2,10,4,2,2,9,-5,-8,6,9,-9,7,-2,-8,-9,-8,-3,-10,4,8,1,-5,4,-3,-5,-10,5,2,6,-10,-3,6,9,-6,10,-10,3,7,-1,10,5,4,-7,-7,6,-10,6,-8,1,-7,-8,-10,-4,-10,7,3,-10,-2,-3,2,6,2,-7,8,-4,9,-4,5,-7,-5,3,-6,4,1,-7,-9,-6,-7,-1,1,10,9,10,-3,7,1,7,6,-5,1,2,9,2,3,10,1,5,-7,-6,-1,-10,6,2,-1,8,1,1,-2,-5,-8,-10,-9,1,-1,6,-9,-6,6,-6,5,8,-6,5,3,2,6,-10,-6,-1,-7,10,-7,-10,4,-1,-10,6,-1,-1,-2,-6,4,5,7,8,7,8,6,-9,6,1,3,1,10,-8,6,1,10,-1,-2,-8,8,-4,-8,5,5,9,5,1,3,-8,-3,-8,-4,9,7,-6,-7,-7,3,8,-2,-3,-8,-4,4,-9,-10,-10,-5,2,-10,7,9,4,-10,10,-1,10,-7,-10,6,-8,8,3,-10,-5,5,10,8,6,6,9,-8,9,-3,6,10,-8,-5,2,-5,-6,1,-4,9,8,-5,5,5,-1,-4,-8,3,5,-6,-3,-5,3,6,8,9,-3,2,10,-3,-6,7,3,3,-10,-6,1,-4,9,4,-7,1,7,-9,3,-7,-9,4,-6,2,7,1,-9,-2,6,6,-9,5,-4,-5,6,-5,-8,-9,-7,2,-8,10,7,8,10,-9,4,-4,-8,-3,-1,-3,7,-5,4,-6,2,2,2,5,3,-10,7,3,-5,4,-5,6,1,-6,-3,-7,-10,4,-8,-3,-2,10,-9,9,-1,1,-9,10,2,-5,10,-8,3,-2,3,-4,8,-8,-8,2,-9,-7,-2,8,-5,-9,-5,5,10,-8,3,-2,7,2,7,5,7,-6,-1,4,-7,8,1,9,1,6,1,-6,10,-4,-2,-4,-2,-9,-3,6,-6,-2,-8,-10,-2,4,6,2,8,2,-6,10,-7,1,-3,-9,-1,-8,6,9,-4,-1,-3,-4,-10,2,5,6,-2,-1,5,-6,3,-7,-1,6,7,4,10,-10,8,-8,5,-2,-10,4,3,2,-3,6,5,-9,-1,2,-3,-2,6,4,6,10,9,3,-3,1,-4,-8,-10,1,2,-3,-6,5,-6,5,5,10,-9,-7,8,6,4,2,3,-5,7,-9,4,-6,5,6,7,5,9,-6,-9,-2,8,-8,7,5,3,10,-10,-2,10,-4,-4,-4,-10,-1,-5,-1,-6,4,-4,1,5,-9,-10,7,-8,8,9,-6,-2,-7,9,8,8,-3,4,-4,-5,-1,3,-4,8,-5,-2,5,10,-1,-1,8,-2,4,3,5,10,-3,-4,5,9,-9,5,-4,-8,-5,3,-10,4,-3,1,-5,1,-5,-4,-7,4,-5,1,-3,-4,10,4,6,-4,-7,6,8,-1,-4,-5,8,-8,8,2,-2,2,8,2,5,5,-4,3,10,-7,9,-7,3,1,7,-5,-4,3,-4,-7,2,1,3,-10,-8,-9,-2,5,4,-9,1,-1,10,6,8,4,-5,10,1,-3,8,9,2,7,9,-10,9,-5,7,2,-5,7,-3,10,-6,6,-8,-6,-10,6,-9,10,-8,-7,-6,-2,7,-1,-6,-8,-5,-8,1,1,7,1,-6,3,7,10,-9,6,-2,8,-9,10,-3,5,4,-5,5,-6,8,6,-1,9,-9,-8,4,-8,-4,-7,9,-3,9,-4,6,7,3,-9,2,-4,5,-1,-8,3,9,1,3,-3,-5,-9,8,7,1,-6,6,-5,2,1,7,1,4,-6,-7,-9,5,-3,6,-8,6,2,-4,2,-3,3,6,5,-8,-7,9,7,-6,1,-10,8,3,-5,-9,2,-1,1,10,9,9,5,4,4,-2,-1,-3,8,1,2,2,1,8,-3,7,8,-10,4,5,-5,4,-1,4,-5,-3,-4,-1,-10,-6,9,7,-1,-2,-4,-4,6,-2,7,6,-1,-6,-6,10,8,-9,9,-6,-4,7,5,-6,9,10,5,5,5,-1,-2,6,-6,7,-4,8,-1,-7,-6,9,-10,1,-5,1,2,2,2,-4,-5,-6,5,-7,8,-5], dtype = "uint8")#candidate|3326|(3120,)|const|uint8
const_3327 = relay.const([-10,-3,10,9,-9,-3,5,-8,-6,9,2,-7,-2,-2,-9,-1,4,2,-3,5,-4,-2,6,7,3,-3,3,1,-4,10,-10,6,6,-9,-1,-10,3,-3,2,-10,-9,7,4,5,2,5,8,-9,-9,1,1,4,-3,-4,10,-9,8,1,7,9,-3,5,-6,-6,-1,5,-8,7,-8,8,6,7,7,-5,5,-4,-10,2,3,1,6,-7,6,8,6,2,-7,-5,8,-7,-4,5,-1,-10,-6,-10,8,7,-1,10,2,9,-2,4,-4,6,3,4,8,-10,-4,7,8,-7,-10,6,10,3,-8,3,7,10,9,-8,7,-3,10,6,-5,-7,-10,9,6,2,-9,8,2,-8,3,2,-3,2,9,1,8,9,1,-8,1,3,-4,-6,8,-1,-9,10,10,-7,-9,-2,-8,-7,-10,4,-6,9,-7,-8,10,-7,-2,5,8,-10,-2,-5,5,9,-8,5,1,4,3,-4,-1,6,-7,-5,4,-3,-10,-7,10,-8,-1,10,1,10,6,-6,3,10,2,-7,3,-3,8,-7,7,7,-2,-10,3,-6,-3,5,4,-8,-1,3,4,-8,-9,3,4,-6,8,-9,7,3,-8,6,4,-8,-8,10,8,-6,-6,-3,-8,-5,4,-1,-9,-10,3,-9,-9,-3,-8,3,-4,3,8,8,-4,6,9,8,2,-5,6,-3,10,4,-10,4,-5,-1,2,1,-2,-5,-6], dtype = "uint8")#candidate|3327|(275,)|const|uint8
call_3324 = relay.TupleGetItem(func_2181_call(relay.reshape(const_3325.astype('uint8'), [8, 8, 16]), relay.reshape(const_3326.astype('uint8'), [780, 4]), relay.reshape(const_3327.astype('uint8'), [275,]), ), 0)
call_3328 = relay.TupleGetItem(func_2185_call(relay.reshape(const_3325.astype('uint8'), [8, 8, 16]), relay.reshape(const_3326.astype('uint8'), [780, 4]), relay.reshape(const_3327.astype('uint8'), [275,]), ), 0)
func_1791_call = mod.get_global_var('func_1791')
func_1793_call = mutated_mod.get_global_var('func_1793')
const_3333 = relay.const([[4.606010,4.094181],[-3.132675,9.625119],[-8.341364,-8.379507],[2.743144,-5.751967],[2.724030,-4.281253],[-9.662141,1.894005],[-8.656421,5.934392],[5.747720,-0.992457],[-1.036875,3.410792],[-3.800421,3.694279],[6.984972,9.908333],[6.006063,-2.485937],[7.366107,-9.601646],[-9.762103,2.550717],[-7.972428,9.762479],[-7.438385,-4.121350],[9.568384,2.769481],[-8.202483,-0.517251],[-9.587634,-6.385628],[8.955349,-6.847979],[-8.590745,-1.898638],[-4.805778,5.244765],[-0.145507,-9.847599],[-0.617753,-7.935752],[-7.287593,0.862254],[-9.070852,-3.705185],[-4.024380,-2.590833],[-1.987722,-6.644459],[6.608881,1.549484],[-0.979319,-6.881082],[-4.869599,3.860399],[2.110458,-2.807887],[7.475846,5.602555],[-5.445354,-4.429082],[-9.731952,-9.209761],[-0.623272,3.173760],[-2.749691,7.013816],[8.848255,1.968807],[2.525020,1.782077],[-9.793203,-1.529650],[0.142739,8.338959],[-4.745687,-6.440594],[-0.734685,4.347958],[2.761935,-4.998861],[0.286341,7.920443],[3.971106,-5.120703],[5.704823,-9.138921],[-6.573931,-2.368375],[-2.653503,7.575091],[5.520203,7.599521],[-6.965227,-0.459277],[-2.886661,8.283340],[0.920676,-4.909847],[-6.654116,0.075149],[-0.240398,7.011277],[-1.509325,0.557264],[-2.208160,5.852187],[-8.762013,5.198700],[4.052778,4.538073],[6.085704,-9.381660],[5.361871,4.365210],[7.602927,3.355886],[-8.452109,-2.454835],[-1.523324,0.676018],[-0.118962,3.243944],[-2.555726,-9.897735],[-3.413889,4.550929],[-9.435367,-3.247527],[-5.752923,1.294382],[-2.418381,-7.651094],[-9.718622,-4.870102],[-3.133484,1.034680],[-5.480902,9.560054],[8.642339,8.674038],[9.733864,5.135418],[-3.966082,6.920714],[-7.418347,-4.429660],[-4.739637,6.690461],[-7.561973,5.974595],[-3.546034,4.402128],[0.146355,0.952873],[-1.313303,7.910942],[4.945326,-3.464092],[-8.847048,-7.341517],[-2.065312,-7.813395],[4.345685,6.262083],[9.288444,-1.768004],[8.192109,-6.642075],[5.001514,-8.379988],[-4.264748,1.864934],[-0.482457,1.355063],[-0.811021,4.585386],[6.843075,1.401131],[-5.805461,-7.619510],[6.505372,6.571530],[-3.347726,-6.313637],[2.079341,-1.108016],[-1.303807,4.473703],[5.865980,2.578029],[-7.283951,-7.837641],[-1.253273,8.941486],[2.686936,-8.507970],[-7.597898,8.081809],[-9.995516,-3.316608],[-1.237759,5.293692],[8.153384,-6.063196],[-7.876492,-7.128827],[-1.451163,-6.331750],[-1.976407,1.038571],[8.355367,-2.457204],[1.116320,-5.977086],[6.643259,6.498310],[7.002744,-9.709005],[6.693339,4.337699],[9.660158,6.395051],[2.665844,-2.278796],[2.534516,5.910765],[-3.283314,-6.031298],[2.921333,5.091498],[-9.449665,5.491359],[5.120847,-3.034223],[-3.067363,-0.961938],[3.463421,6.614441],[1.663418,-7.972010],[-7.100378,2.843472],[6.784361,-0.095140],[3.969771,-3.146917],[0.682660,1.405804],[8.677499,5.453534],[-4.048032,0.380845],[7.484503,-3.747611],[9.804527,5.947372],[-7.418535,-2.169874],[2.729309,-5.077060],[-1.609153,-6.115270],[-9.791640,-1.831088],[7.060450,4.574881],[-6.409964,9.883279],[-0.443368,-3.398406],[-7.312088,5.866850],[2.143886,-9.848097],[-2.655723,1.130092],[5.719577,-1.115282],[5.562860,-1.409315],[2.190720,-9.282777],[-2.181913,0.968220],[1.405450,-9.892307],[-4.781417,-9.550469],[9.578788,-9.926182],[-0.550849,-5.618742],[6.536674,1.703128],[-5.972680,8.943613],[-5.512989,2.302241],[7.699911,2.929784],[-8.578098,-4.926671],[1.481378,-7.520492],[1.907114,-7.806661],[-5.165502,-6.239207],[-5.266312,8.465575],[1.384189,-9.513696],[-7.568180,-4.996064],[-4.778460,0.363803],[-1.131770,5.403226],[-1.066717,-6.605631],[-5.867855,5.009568],[-7.791387,-4.679804],[-0.696348,9.163559],[-6.674065,2.492139],[0.130930,-9.601960],[7.505688,-6.938448],[2.570083,8.925932],[-0.110613,-7.564363],[-2.370595,7.153691],[2.378289,5.595634],[1.171589,6.724664],[-4.121423,9.452797],[-9.909084,-6.586559],[4.465903,4.934950],[-0.975050,-8.711723],[9.354827,-0.111224],[3.572266,-6.561059],[5.970980,-3.728697],[-8.106184,9.636706],[-1.730374,-8.375712],[-0.441750,-0.661180],[6.621293,3.208603],[-4.622057,-3.021473],[-4.743928,1.527716],[5.123527,-8.707178],[-6.821232,5.018204],[-4.103281,7.295787],[7.455582,0.575458],[-8.036893,4.687931],[-8.315115,-7.174475],[2.104843,-1.718903],[9.879827,1.242530],[1.758577,1.579405],[-0.403597,-8.482247],[2.885692,6.516600],[3.833923,2.162758],[-7.613538,8.389400],[4.157203,0.888882],[8.502190,-2.164367],[7.918363,6.555888],[0.907436,-9.531202],[4.671640,-2.132796],[3.219980,-7.840747],[-9.166069,-9.838206],[-3.516131,7.736046],[9.902072,-1.864917],[-2.990232,4.716148],[-7.543428,-9.174233],[-7.046625,5.167892],[3.077829,-2.417006],[1.219001,2.000022],[-7.193358,-0.272425],[-2.720622,-1.236365],[-1.612327,-5.179466],[2.438325,0.322627],[-1.364867,7.880488],[-7.165965,-9.719267],[-6.692384,-5.623582],[4.556398,-2.135245],[-9.812416,6.341397],[-6.267702,-1.884010],[-9.053543,-3.221689],[8.153753,-0.941251],[0.331204,-1.282900],[-8.434723,-1.594882],[7.303954,5.676165],[-2.505561,4.310316],[-0.154875,7.955086],[-3.163540,-1.811719],[-0.988232,8.522908],[-5.704149,4.850909],[2.160261,1.533004],[1.336381,0.319508],[1.394996,0.854082],[-2.657003,-7.117503],[9.760914,8.387177],[5.465509,9.165608],[-2.817285,3.322833],[-9.634504,6.251519],[-3.540058,8.704693],[-9.666035,1.760147],[4.172971,4.259707],[2.379724,1.478725],[-4.341078,-8.686804],[-4.598928,7.492604],[-1.128311,2.072181]], dtype = "float32")#candidate|3333|(250, 2)|const|float32
call_3332 = relay.TupleGetItem(func_1791_call(relay.reshape(const_3333.astype('float32'), [10, 5, 10])), 0)
call_3334 = relay.TupleGetItem(func_1793_call(relay.reshape(const_3333.astype('float32'), [10, 5, 10])), 0)
output = relay.Tuple([call_3307,call_3324,const_3325,const_3326,const_3327,call_3332,const_3333,])
output2 = relay.Tuple([call_3308,call_3328,const_3325,const_3326,const_3327,call_3334,const_3333,])
func_3341 = relay.Function([], output)
mod['func_3341'] = func_3341
mod = relay.transform.InferType()(mod)
output = func_3341()
func_3342 = relay.Function([], output)
mutated_mod['func_3342'] = func_3342
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3343 = relay.const([[[3.856504],[-0.271893],[-1.475952],[0.093589],[-8.503215],[-0.150985],[-5.413294],[-7.384308],[4.894488],[-5.284191],[-8.085351],[4.979297],[-7.960281],[-1.617202],[5.123791]],[[6.331108],[-1.699888],[-7.822015],[3.543037],[4.676380],[-2.796566],[7.116495],[-0.087645],[-9.363115],[-2.725749],[8.420381],[3.577106],[2.235152],[4.799212],[2.304031]],[[5.464354],[8.579741],[-0.401725],[-4.213645],[-4.608760],[6.478229],[3.684769],[8.902276],[4.839619],[6.738002],[-0.693564],[-6.861284],[3.501247],[5.008862],[-8.647128]],[[3.138128],[4.281375],[8.143903],[-9.559666],[5.344180],[1.546806],[-7.738031],[2.976981],[-4.083685],[2.618435],[3.749903],[-3.151339],[8.751958],[4.878272],[-6.074767]],[[3.178312],[9.943435],[-0.328172],[-5.312142],[-8.871232],[7.725236],[7.276792],[-3.321616],[3.430560],[4.198519],[-2.999863],[8.279113],[-2.216405],[-0.896761],[8.943502]],[[0.230090],[-7.998457],[-6.343880],[4.809230],[-5.972734],[-4.054329],[2.223884],[6.483844],[1.545770],[-8.658366],[5.654804],[1.450221],[0.799697],[2.387866],[8.913038]],[[-0.897458],[0.535373],[9.748455],[-6.312453],[-1.599454],[-2.146252],[-9.757166],[-8.504829],[5.163722],[7.795610],[-7.396925],[-2.753710],[6.829613],[-5.971400],[7.355913]],[[9.587332],[-6.491317],[-5.775512],[-6.829767],[3.098132],[3.629051],[-4.290746],[5.130367],[6.863162],[-3.259693],[1.813927],[6.296845],[-2.349244],[5.930711],[2.659737]],[[-5.869660],[5.386222],[9.893203],[-6.377770],[-0.359298],[6.987174],[6.202751],[0.187118],[-4.489405],[2.353644],[4.317120],[-1.743067],[-5.675574],[8.787160],[3.173709]],[[-1.293839],[-8.737892],[-2.428140],[5.957393],[9.071877],[-3.756725],[-2.600266],[-8.525781],[8.406576],[-0.798976],[4.626293],[0.095884],[2.949635],[-3.170013],[4.127117]],[[1.889273],[2.354594],[6.612122],[-2.920406],[-2.126908],[-4.987806],[-1.793599],[-2.096510],[4.265108],[7.218077],[-2.683656],[6.896121],[-1.243878],[1.000672],[-4.717965]],[[-0.960105],[-8.858911],[4.194304],[-3.738277],[5.528758],[1.254651],[3.050615],[-4.679237],[1.441785],[2.850995],[1.840563],[9.177665],[8.004175],[7.485391],[7.808112]],[[-8.727074],[-6.610324],[4.680468],[-7.594559],[4.370740],[8.341459],[-0.650492],[-9.599281],[-3.429523],[-0.315617],[-7.187841],[-9.851166],[-8.094830],[-0.377421],[-3.461553]],[[2.143335],[7.104966],[-8.464101],[9.760071],[-4.643995],[-9.880323],[-8.316465],[2.262657],[9.965590],[-8.035277],[2.680392],[8.067626],[-4.055561],[-9.350535],[-7.624677]],[[-7.407591],[5.983323],[6.642171],[9.829364],[-5.374392],[5.350444],[5.268342],[6.064377],[-5.570479],[-6.604083],[-5.579317],[2.085910],[6.136674],[-2.395833],[-9.324080]]], dtype = "float32")#candidate|3343|(15, 15, 1)|const|float32
uop_3344 = relay.rsqrt(const_3343.astype('float32')) # shape=(15, 15, 1)
func_2200_call = mod.get_global_var('func_2200')
func_2201_call = mutated_mod.get_global_var('func_2201')
call_3351 = func_2200_call()
call_3352 = func_2200_call()
bop_3356 = relay.subtract(const_3343.astype('int8'), relay.reshape(uop_3344.astype('int8'), relay.shape_of(const_3343))) # shape=(15, 15, 1)
output = relay.Tuple([call_3351,bop_3356,])
output2 = relay.Tuple([call_3352,bop_3356,])
func_3363 = relay.Function([], output)
mod['func_3363'] = func_3363
mod = relay.transform.InferType()(mod)
output = func_3363()
func_3364 = relay.Function([], output)
mutated_mod['func_3364'] = func_3364
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2252_call = mod.get_global_var('func_2252')
func_2254_call = mutated_mod.get_global_var('func_2254')
call_3403 = relay.TupleGetItem(func_2252_call(), 0)
call_3404 = relay.TupleGetItem(func_2254_call(), 0)
output = relay.Tuple([call_3403,])
output2 = relay.Tuple([call_3404,])
func_3427 = relay.Function([], output)
mod['func_3427'] = func_3427
mod = relay.transform.InferType()(mod)
output = func_3427()
func_3428 = relay.Function([], output)
mutated_mod['func_3428'] = func_3428
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2900_call = mod.get_global_var('func_2900')
func_2901_call = mutated_mod.get_global_var('func_2901')
call_3481 = relay.TupleGetItem(func_2900_call(), 3)
call_3482 = relay.TupleGetItem(func_2901_call(), 3)
output = call_3481
output2 = call_3482
func_3493 = relay.Function([], output)
mod['func_3493'] = func_3493
mod = relay.transform.InferType()(mod)
output = func_3493()
func_3494 = relay.Function([], output)
mutated_mod['func_3494'] = func_3494
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3341_call = mod.get_global_var('func_3341')
func_3342_call = mutated_mod.get_global_var('func_3342')
call_3524 = relay.TupleGetItem(func_3341_call(), 4)
call_3525 = relay.TupleGetItem(func_3342_call(), 4)
var_3532 = relay.var("var_3532", dtype = "uint8", shape = (275,))#candidate|3532|(275,)|var|uint8
bop_3533 = relay.bitwise_or(call_3524.astype('int16'), relay.reshape(var_3532.astype('int16'), relay.shape_of(call_3524))) # shape=(275,)
bop_3536 = relay.bitwise_or(call_3525.astype('int16'), relay.reshape(var_3532.astype('int16'), relay.shape_of(call_3525))) # shape=(275,)
output = relay.Tuple([bop_3533,])
output2 = relay.Tuple([bop_3536,])
func_3543 = relay.Function([var_3532,], output)
mod['func_3543'] = func_3543
mod = relay.transform.InferType()(mod)
var_3544 = relay.var("var_3544", dtype = "uint8", shape = (275,))#candidate|3544|(275,)|var|uint8
output = func_3543(var_3544)
func_3545 = relay.Function([var_3544], output)
mutated_mod['func_3545'] = func_3545
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2802_call = mod.get_global_var('func_2802')
func_2804_call = mutated_mod.get_global_var('func_2804')
call_3549 = func_2802_call()
call_3550 = func_2802_call()
func_385_call = mod.get_global_var('func_385')
func_388_call = mutated_mod.get_global_var('func_388')
var_3555 = relay.var("var_3555", dtype = "int32", shape = (252,))#candidate|3555|(252,)|var|int32
var_3556 = relay.var("var_3556", dtype = "float32", shape = (1755,))#candidate|3556|(1755,)|var|float32
call_3554 = relay.TupleGetItem(func_385_call(relay.reshape(var_3555.astype('int32'), [4, 7, 9]), relay.reshape(var_3556.astype('float32'), [1755,]), ), 1)
call_3557 = relay.TupleGetItem(func_388_call(relay.reshape(var_3555.astype('int32'), [4, 7, 9]), relay.reshape(var_3556.astype('float32'), [1755,]), ), 1)
output = relay.Tuple([call_3549,call_3554,var_3555,var_3556,])
output2 = relay.Tuple([call_3550,call_3557,var_3555,var_3556,])
func_3569 = relay.Function([var_3555,var_3556,], output)
mod['func_3569'] = func_3569
mod = relay.transform.InferType()(mod)
var_3570 = relay.var("var_3570", dtype = "int32", shape = (252,))#candidate|3570|(252,)|var|int32
var_3571 = relay.var("var_3571", dtype = "float32", shape = (1755,))#candidate|3571|(1755,)|var|float32
output = func_3569(var_3570,var_3571,)
func_3572 = relay.Function([var_3570,var_3571,], output)
mutated_mod['func_3572'] = func_3572
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2445_call = mod.get_global_var('func_2445')
func_2446_call = mutated_mod.get_global_var('func_2446')
call_3613 = relay.TupleGetItem(func_2445_call(), 1)
call_3614 = relay.TupleGetItem(func_2446_call(), 1)
uop_3641 = relay.acosh(call_3613.astype('float64')) # shape=(2, 1, 8)
uop_3643 = relay.acosh(call_3614.astype('float64')) # shape=(2, 1, 8)
bop_3646 = relay.not_equal(uop_3641.astype('bool'), relay.reshape(call_3613.astype('bool'), relay.shape_of(uop_3641))) # shape=(2, 1, 8)
bop_3649 = relay.not_equal(uop_3643.astype('bool'), relay.reshape(call_3614.astype('bool'), relay.shape_of(uop_3643))) # shape=(2, 1, 8)
func_1632_call = mod.get_global_var('func_1632')
func_1635_call = mutated_mod.get_global_var('func_1635')
var_3655 = relay.var("var_3655", dtype = "uint32", shape = (132,))#candidate|3655|(132,)|var|uint32
call_3654 = relay.TupleGetItem(func_1632_call(relay.reshape(var_3655.astype('uint32'), [3, 4, 11])), 0)
call_3656 = relay.TupleGetItem(func_1635_call(relay.reshape(var_3655.astype('uint32'), [3, 4, 11])), 0)
func_1598_call = mod.get_global_var('func_1598')
func_1601_call = mutated_mod.get_global_var('func_1601')
const_3661 = relay.const([-6,1,4,2,-4,5,7,5,-3,10,1,-3,-9,7,4,4,-7,-2,4,10,8,-5,-7,3,-5,9,8,1,9,-1,-2,-4,1,-9,2,4,7,3,2,-5,10,-3,6,-10,-5,-9,-7,5,-9,-4,4,-8,-7,-8,-8,-6,-8,1,-6,-10,-1,6,-10,-7,-5,-7,-10,3,-6,6,3,6,-4,5,5,1,-2,5,7,-2,-4,-3,-4,2,5,-7,2,10,-8,6,-10,-1,-5,6,-8,-6,7,-7,-6,-2,8,1,-1,-8,6,4,2,-10,-2,10,-3,4,-6,3,-1,2,2,-3,-4,4], dtype = "int64")#candidate|3661|(120,)|const|int64
call_3660 = func_1598_call(relay.reshape(const_3661.astype('int64'), [4, 10, 3]), relay.reshape(const_3661.astype('int64'), [4, 10, 3]), )
call_3662 = func_1598_call(relay.reshape(const_3661.astype('int64'), [4, 10, 3]), relay.reshape(const_3661.astype('int64'), [4, 10, 3]), )
func_3363_call = mod.get_global_var('func_3363')
func_3364_call = mutated_mod.get_global_var('func_3364')
call_3663 = relay.TupleGetItem(func_3363_call(), 0)
call_3664 = relay.TupleGetItem(func_3364_call(), 0)
output = relay.Tuple([bop_3646,call_3654,var_3655,call_3660,const_3661,call_3663,])
output2 = relay.Tuple([bop_3649,call_3656,var_3655,call_3662,const_3661,call_3664,])
func_3676 = relay.Function([var_3655,], output)
mod['func_3676'] = func_3676
mod = relay.transform.InferType()(mod)
mutated_mod['func_3676'] = func_3676
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3677 = relay.var("var_3677", dtype = "uint32", shape = (132,))#candidate|3677|(132,)|var|uint32
func_3676_call = mutated_mod.get_global_var('func_3676')
call_3678 = func_3676_call(var_3677)
output = call_3678
func_3679 = relay.Function([var_3677], output)
mutated_mod['func_3679'] = func_3679
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2900_call = mod.get_global_var('func_2900')
func_2901_call = mutated_mod.get_global_var('func_2901')
call_3720 = relay.TupleGetItem(func_2900_call(), 0)
call_3721 = relay.TupleGetItem(func_2901_call(), 0)
func_3569_call = mod.get_global_var('func_3569')
func_3572_call = mutated_mod.get_global_var('func_3572')
const_3739 = relay.const([-2,4,4,3,-7,8,8,5,-2,-2,-10,1,-3,-8,-6,7,9,-8,-5,2,-8,1,2,5,4,4,-8,-4,9,9,-7,5,-10,-9,-4,10,-5,-7,9,-10,9,7,-8,10,2,-3,8,5,1,-4,6,6,-6,-6,-6,8,-10,-7,-7,-6,-6,6,-8,-1,-6,3,-10,-3,3,3,-8,7,7,8,10,-3,-4,-10,1,-1,-8,-6,3,-9,1,-8,-3,8,-10,4,-10,-6,-7,7,8,2,10,8,-1,2,7,10,-6,9,-7,-5,1,1,8,5,-4,3,9,9,-8,-2,10,6,4,-1,-2,6,-8,3,-5,-3,7,4,9,8,6,-6,-3,4,2,8,4,7,-3,9,1,8,7,-8,7,6,5,2,4,7,3,-10,-1,10,-9,1,-10,10,3,6,3,3,-1,7,-1,3,-2,-3,-10,-7,2,1,-7,1,-10,-9,-6,2,-7,7,7,-2,-1,-2,-7,-1,6,-3,4,4,1,-8,4,-6,-1,9,-1,7,-7,4,-5,-5,9,-6,1,9,-1,-9,-9,8,-10,-7,9,4,10,-9,4,-8,1,-8,-3,-6,-5,1,-2,3,-5,2,2,-9,-5,-9,-2,6,10,8,2,-8,-9,-1,8,-2,2,-7,1,9,4,-8,5,-10,7,-10], dtype = "int32")#candidate|3739|(252,)|const|int32
const_3740 = relay.const([-9.923188,9.011531,6.239214,-7.875769,-1.016673,-7.380755,-2.413905,2.492895,2.375912,-6.704567,7.797487,8.339219,9.584907,6.108972,-3.577158,0.962373,5.543970,9.319409,8.498521,0.430827,-7.773717,9.237444,2.261882,8.752821,5.821505,-1.961181,2.370837,-0.040027,3.932698,-6.107301,7.701091,-8.501744,-3.640623,6.320720,7.572704,-8.518771,-1.729020,4.244592,-7.766136,-2.030171,-5.682208,6.623060,7.465163,-4.142438,4.406041,-4.010188,-0.345075,-6.667063,-7.426788,-2.655523,-3.880978,-5.163464,0.103154,-9.604116,-5.662950,7.546681,7.677444,2.414539,-8.678536,-5.866256,-5.048524,-3.493791,5.846111,7.762224,-4.018211,-2.666253,-8.098491,8.777962,-1.356954,-4.487092,9.094777,4.673410,-1.404392,9.733403,-3.797443,-7.307317,-2.516764,3.837005,7.583122,4.591206,-7.065247,-3.289963,-2.365266,-1.418028,-6.613264,-9.943275,-0.927891,-2.031414,-0.380805,-9.913814,0.338452,7.145100,9.663181,-6.861486,1.709612,7.266154,7.934573,3.215133,4.513188,-5.721385,-9.698801,3.008159,-9.557392,8.225567,6.624366,4.799079,-4.336636,-4.633819,5.760781,7.689116,2.959901,-0.319879,-3.894701,-4.539306,-7.043673,9.085951,2.219901,1.173766,3.691889,-0.504084,-3.968021,7.026015,-0.529662,7.250385,-6.783703,3.994823,3.448103,-8.123125,8.156928,0.405378,6.584306,-3.024875,-5.925543,-3.868839,-3.333619,-9.165232,-6.818691,0.363507,-2.647012,-5.013744,9.500458,-9.914742,-2.785448,9.417934,2.173687,7.013149,0.608327,-3.030729,7.835403,7.662129,7.613288,1.074259,-5.165462,2.139250,7.005927,1.506827,9.860696,3.178423,9.095361,2.632971,1.262281,5.863619,-1.001829,-2.633194,8.420346,1.894980,-3.981325,-9.524202,2.043518,5.038589,-1.690073,-9.900298,-8.415164,4.794439,-5.493614,-9.127963,3.435634,-6.768581,6.938578,4.737478,6.705666,-0.327679,7.847996,-4.660913,-6.671639,4.913419,-1.253029,-6.026522,0.166302,-7.431689,-0.316670,-4.177956,6.485585,9.240168,0.889344,4.836285,4.482714,-7.171436,-3.941535,3.514036,-0.284018,6.867887,-9.667017,9.701581,1.044591,1.966812,0.829126,0.433080,2.621381,6.600586,-7.607238,4.734971,-8.142161,-0.009331,-6.986171,3.189418,9.564847,4.477316,-9.324149,0.808746,9.405260,6.290357,-8.539792,2.662012,5.957955,7.460401,6.359590,4.276968,-2.314663,-2.270122,-1.030999,-4.016609,7.964876,7.901066,-8.926151,7.476666,-0.029026,-4.293643,-5.049545,-7.558455,5.842047,5.629163,-2.693259,-1.576535,-2.564855,3.162714,7.852386,-5.195796,0.579107,-3.534694,6.851096,8.820979,7.356102,-1.478059,4.854646,8.114728,-6.204903,9.190091,-4.832001,-2.122213,5.480708,9.019471,1.974449,6.229616,0.969051,-3.016808,6.797012,-8.923731,-9.923743,-4.795021,5.208131,-7.755576,-1.189063,-6.181649,9.707674,-5.518096,-7.624865,5.281966,8.348781,8.655575,2.038394,8.905026,1.133936,0.234888,6.178668,-8.038474,5.925115,-0.711899,-3.450415,-8.557792,1.971584,-6.731748,-3.185653,0.533435,-0.420346,1.312591,6.749880,7.258373,-3.554755,-6.641146,-5.209515,4.980250,6.780405,-5.204360,-6.250706,5.130056,8.354115,-7.678663,-7.170785,0.698346,-4.945990,-3.083762,-9.614802,-9.130192,-9.792165,-6.081670,9.472234,-8.646449,5.169872,8.818506,-7.147545,-3.955952,-6.843987,2.063361,-4.493493,-2.117097,9.196376,-9.629374,-4.607295,3.950486,3.527863,3.241071,6.370007,0.363428,-2.900251,-2.661794,-0.146133,-2.727002,0.478311,3.752975,7.184210,-8.160436,-6.719556,-7.092999,-1.323107,5.106428,1.627611,-1.835483,-0.504554,4.135549,-6.432931,3.922333,-0.902923,-8.112389,-9.138984,-9.779226,8.983203,-0.569966,6.256398,-7.131583,-4.731922,-5.016277,-7.636535,-8.872220,-9.432729,-1.399359,-8.477081,5.594362,4.471151,-1.540914,7.983729,0.944450,-4.249453,-0.082146,-6.609304,9.213479,-8.891158,-0.943308,-3.503773,-2.501836,3.989635,-4.681815,-5.826616,-8.231493,6.590444,2.295610,9.089955,3.614203,5.771482,-2.537180,-1.338779,-3.266405,6.424790,2.721109,-9.617069,-3.957042,-0.675922,5.322719,7.539525,5.361198,-5.030146,3.423800,8.711426,0.937804,6.076950,0.927591,8.740317,-4.683420,-5.703304,1.609171,0.945993,-6.636384,-2.400157,2.866318,-6.895212,-1.072673,5.169931,-1.326452,-5.867681,0.656517,6.668241,1.323522,9.516544,2.962547,5.412917,-6.831512,1.851295,5.619984,-7.065390,8.408958,8.862420,2.630208,9.483719,0.216214,-1.996574,9.102297,3.358551,-2.759636,0.093376,4.791757,-4.372248,2.389430,-0.469842,3.052787,6.008953,8.388446,-6.513465,-9.368019,6.416386,5.625648,-2.155264,5.184665,6.365063,-0.200440,-2.457333,-9.835277,8.294493,-6.502459,-5.352302,-9.182551,-2.965922,-6.919280,3.143789,-7.764524,-6.461231,-8.119245,3.058654,3.386406,1.218358,7.196536,6.468459,9.585369,2.831480,-5.364843,5.724672,-5.676221,2.482249,2.601344,7.049742,1.181120,2.580138,-1.187577,9.619074,-7.020626,-4.390142,-8.089056,6.337266,-8.808993,0.319832,-8.287149,-3.446343,-2.343629,3.758305,-9.639590,-2.835105,-8.702572,5.704049,-8.615085,-6.000234,2.694632,-8.309191,-8.094353,8.319605,-1.872225,-6.604754,-9.391424,7.589926,-8.248627,-8.231056,9.745965,-1.929452,-0.812609,6.695677,-8.063438,8.033463,-1.137251,-0.293373,6.074832,9.668590,-3.409659,-3.398007,-4.251289,-0.674305,-3.317307,4.658938,5.536027,-8.955139,8.425049,-7.745070,1.867220,-5.052209,2.037156,6.975531,-9.363266,-2.747134,-7.303902,2.850389,0.732314,2.890822,-9.540854,9.680614,-1.052554,-0.676787,2.224446,9.506212,-6.852937,-6.506927,-7.935707,6.088744,5.447345,-1.791158,-6.553639,-7.889866,4.493551,-1.890228,2.833179,8.595984,6.229270,9.168571,-2.012549,5.049011,-7.407931,-6.307271,2.235940,-9.081585,3.536528,-2.711420,-8.285409,8.966850,-3.557102,-8.500238,-0.110227,3.573473,9.402378,-7.057987,-8.800995,-0.309544,-5.817405,4.382875,-7.871588,-3.271236,-2.201306,-9.475223,8.855686,-1.818607,3.796691,3.243553,-9.926688,8.319496,-8.227104,9.388640,5.516269,3.465840,-8.216867,-8.217952,-6.211310,6.054807,8.889971,-7.727876,9.361205,3.257289,1.957322,-1.058109,8.652246,3.359940,-8.695094,-3.458879,-3.374206,9.682708,4.045388,-5.743600,-8.798842,-0.590227,0.658504,-0.942826,-3.596450,4.784282,0.018509,5.091638,6.135450,-9.706548,-1.433246,6.476523,-7.117925,5.983861,-1.482064,-1.048196,5.506549,3.314954,6.799626,-2.357957,4.885770,1.760201,1.447495,7.833492,3.196514,-4.762135,0.604964,-6.605403,-1.551327,5.756901,6.443164,4.819143,-8.276680,2.185590,8.037604,0.122848,5.828572,6.958244,-8.352384,4.635279,-4.133824,5.254796,-5.827240,4.720563,2.668444,7.886933,-7.732760,-1.348570,2.657809,-9.019164,7.014806,8.470152,-1.005383,8.561897,-1.789951,-5.140018,9.385036,-6.575717,-1.887914,-1.367791,-0.611680,-7.555525,2.904185,4.528365,4.252722,9.706749,-7.026702,0.479881,1.567031,5.927319,-0.780349,-2.631576,9.472271,6.486560,-3.815032,5.359192,4.487529,-5.781758,-9.933384,-0.995248,5.745280,-5.585733,-2.724950,6.353292,3.344893,6.647845,-3.674152,3.565808,-8.372331,5.259880,-6.010798,8.319690,3.640211,-1.612676,-6.766254,0.832377,-8.390630,3.052210,8.306665,-3.572649,8.430402,-9.432477,7.854308,1.885451,-3.687614,0.262833,5.345504,3.412004,-5.592789,5.779220,-5.699675,-7.938921,-4.848727,1.103622,-2.452245,-7.843112,-5.588926,-4.029682,-2.200553,2.801328,-3.168427,-0.197798,-6.887431,-8.703884,2.659526,5.470486,-1.556151,7.727390,3.683953,5.583604,-5.180750,7.241980,-8.419169,6.417454,8.418488,-5.834714,7.848733,6.919946,-3.281624,-5.409218,9.057797,4.087948,0.961654,2.958085,2.730158,8.643300,-7.159111,-8.837758,-6.168475,-9.782549,6.592141,6.445010,5.753216,-7.546428,9.071628,1.209885,-4.015870,-8.945111,5.567576,-2.860193,-7.024934,5.616638,-9.719005,-7.714185,8.163720,-3.951875,4.939660,7.201645,-5.916915,-1.900168,-4.844433,6.948245,-6.054923,-9.157443,0.829236,-5.595672,-9.348983,-5.929517,-1.643636,9.958374,6.790851,-8.924241,-0.682730,9.384672,1.727042,-6.110591,-8.208724,-6.007437,3.825577,-6.135523,2.607258,1.850563,-7.705806,-7.761572,-8.073397,-8.809803,3.245589,-6.453258,-0.138038,-0.507971,3.979080,2.971494,-1.435042,-4.869382,6.204796,-2.730399,4.782076,-4.024169,-5.310407,-8.535756,6.988346,-8.949362,1.802575,-4.955910,8.419913,4.428480,4.431315,-5.794978,-9.110816,3.982261,1.824460,-4.682047,5.353278,6.652555,7.430772,-4.737431,-1.412848,9.744031,2.430886,-1.854588,1.484163,1.328328,-3.236454,-3.149813,-2.709517,-1.906187,-0.489676,7.676412,-2.893610,0.546319,-3.666006,-0.036185,-3.492675,2.163756,3.752489,-2.178727,4.345089,0.062130,7.217277,0.819276,1.799389,-2.261834,-6.363790,-8.677644,-8.002478,4.002800,5.780616,4.115496,3.858590,-8.845590,-6.668735,3.353425,-0.453483,-8.492826,6.296192,-2.424748,6.634759,-6.986536,-8.265898,-5.816667,-9.579596,2.513172,9.061325,2.137377,6.256978,2.338286,6.054613,-3.867197,2.798613,9.701684,-6.121424,-4.553840,-8.289353,7.043360,5.311940,8.341510,9.911887,9.220040,-0.901330,-5.472352,-6.614919,5.157534,-5.724874,-8.045185,-3.853862,-4.040290,6.710696,5.704754,2.627780,-6.661246,-4.431292,-2.074383,-8.683137,3.929146,6.382847,3.815729,9.584332,8.710827,-8.258977,-2.818244,0.413197,7.310552,7.375733,2.703281,3.466281,2.015087,7.051065,-7.523047,3.755445,-0.005387,2.221897,7.089438,3.365903,-2.638430,-6.740909,-6.956715,-6.992627,-6.740051,-7.517667,-4.847155,0.839401,-2.814552,-1.567343,-1.604411,-5.923327,-5.827115,-8.593688,-5.164582,-7.449246,4.632430,6.877907,-9.432039,2.263901,3.328435,-5.997809,-8.868194,2.768192,4.179344,7.079885,-5.088497,-1.205426,4.518013,-5.202254,-4.508452,-0.152977,1.830097,-4.815607,8.670438,-5.950367,5.892775,1.639286,-6.183257,-5.959233,-3.013272,8.122366,0.472147,7.793279,6.704926,4.684501,-6.225695,8.377728,2.549595,7.212328,-6.223020,-5.078928,7.748365,5.605120,-2.343724,4.992503,0.811505,7.908033,-1.405480,7.773703,-3.063668,-3.391711,-6.216429,-7.115488,6.100792,8.121510,2.044222,3.621250,5.785610,-9.407567,8.187705,-4.157846,4.741991,3.224584,-0.370744,0.429398,2.321898,1.235595,8.313139,-5.664230,0.975741,-3.227820,7.591597,3.785951,-6.629845,-4.381919,1.795274,-4.501865,6.238142,5.733652,-5.580654,-3.433374,-7.254627,-2.120640,-8.335623,-5.975485,-2.337271,-3.858908,-4.675997,-4.194358,-5.179725,-2.072006,8.351984,-8.273537,4.360771,-2.959685,-0.241746,3.927827,-6.563758,-7.442705,-6.181008,-6.036259,-3.275616,-8.969411,6.153654,3.996508,-5.703355,3.171887,0.802792,-5.131585,0.972591,-6.132652,5.456160,-2.121115,2.126702,-7.599777,3.060229,-1.920393,-4.493235,8.961514,5.822356,2.124124,-0.772165,8.592766,-9.166715,-4.567472,-7.460870,6.032329,5.445742,1.795052,-6.195252,-8.174133,4.725962,2.056949,-4.961099,4.782411,-2.379276,0.362662,2.966935,-4.592013,-6.823639,-8.489479,6.151835,-2.586939,8.766125,-2.007080,-1.119408,-5.337698,5.733931,9.049681,-5.046549,-0.310529,0.154542,7.446787,-6.747092,-7.276001,6.187764,-9.539385,-7.277019,3.046791,-0.576713,4.399075,-3.309901,-8.559895,-7.760426,1.368199,-0.707460,9.716896,1.712416,3.888050,-2.342382,-5.442855,-8.274822,-1.917636,-8.273567,-8.552074,9.162154,7.488825,7.707506,-2.509611,7.360997,-8.759390,2.786283,7.753720,1.167744,-8.592803,-1.607903,7.548271,4.098120,8.766742,3.634262,5.879056,4.141098,-4.126412,-3.569798,-5.727005,3.322580,-3.940499,-8.121366,9.168228,-1.693371,7.119460,5.061895,5.706478,7.088710,-2.300753,-1.413417,7.375769,-0.942063,3.638157,-3.423982,-6.205455,-9.370900,-0.775481,-9.755346,-7.777453,-6.047639,4.722183,-1.091308,-6.854768,4.838713,-9.624714,-3.151972,8.835170,-8.111703,-9.296080,4.585512,-9.940023,0.022389,-8.349057,-5.296110,-8.566333,3.123971,-6.564173,-3.867419,2.399844,4.284781,4.114184,6.214694,-6.368568,4.740836,1.293172,0.105085,2.507678,-9.243928,-9.660218,-1.995945,9.521781,-7.541634,-7.741882,1.338148,-5.010419,7.457253,-2.291408,0.559519,-3.784461,4.581167,7.566650,6.593697,8.745329,-3.455153,8.310917,-1.300134,-1.267585,-0.280522,1.428148,-2.372368,0.955271,-4.584151,6.355847,-0.449691,-0.659199,0.405018,9.295957,-9.339728,-8.272540,-0.062279,-9.034791,3.983730,-1.992468,1.066312,5.041641,2.078027,0.243246,-5.503724,9.884270,2.083837,3.397353,2.037737,6.785840,7.240996,7.774616,1.616561,5.109830,-2.672101,7.935892,3.102058,-1.419167,9.131217,-6.944053,-8.745562,-4.577835,-2.261813,-0.910733,-5.762738,6.224480,2.455955,-0.537843,-0.061607,0.850537,1.939823,-2.107435,0.736097,2.430715,6.928168,2.811753,-5.162810,9.713937,3.813522,-2.559523,5.908230,1.358897,-8.046721,-0.413430,9.724391,-8.549949,-1.992494,-8.400483,5.637783,-9.281253,8.724155,-8.413886,3.661975,-0.632574,0.443196,9.965170,7.600758,6.937378,-8.192750,-1.819679,-6.600089,-1.775163,-1.075023,-2.330702,-3.792044,-5.109627,-9.724572,6.062204,-9.828148,-7.326646,4.430639,-4.737451,0.999305,-0.876235,2.230644,9.085826,8.498442,-7.634203,-7.557893,4.387390,4.736859,3.337961,-4.100754,-6.421829,-1.494163,-6.882427,-8.587929,-0.686850,4.137819,6.823460,-2.957868,-0.535258,-5.457450,8.723693,2.590999,9.466497,-3.337541,3.741074,-8.918014,8.503757,-1.967111,-1.973596,-9.315354,-2.176665,4.206834,9.982009,3.884104,-5.802752,-3.799392,-7.656867,-4.717080,9.748065,-6.891838,-4.777323,-9.593034,-0.969690,5.072487,1.514423,3.958725,9.567205,5.930031,-5.005273,-0.854905,-3.901403,-7.161792,3.844550,-4.994287,2.043045,3.976275,3.235671,0.379095,-1.896285,-0.612977,6.086032,-6.541441,5.781265,7.243359,-0.145714,-1.397824,-7.552877,5.019540,5.900865,-2.260711,2.202582,-4.701972,4.504463,-1.908141,0.186460,9.055360,-9.733465,1.350649,4.864147,-0.507544,0.497037,-4.934075,0.362515,5.326577,-9.182643,-8.666227,9.181903,-1.455082,-6.695614,-0.501652,-0.887613,-0.160774,4.773583,-2.225093,-2.494437,-5.090640,8.293103,-6.029257,1.014408,5.421196,9.871751,9.827086,1.689923,-1.716336,-1.834546,0.648627,-8.252079,3.955313,3.236999,7.565948,-1.054508,5.001462,-9.278699,6.095144,4.612018,1.075509,-6.456195,6.660832,3.066187,9.298393,0.351947,-5.223874,2.852596,0.668789,2.482776,-7.677563,6.025744,1.900440,3.189627,3.844513,2.445109,-7.418552,2.550281,4.363215,1.091125,-2.373997,8.487580,-5.455104,-2.053832,-9.440477,-4.842586,-8.378331,-1.864295,-1.278975,-5.912981,8.583188,-5.913746,5.199376,1.385916,-8.774077,0.837885,1.803916,8.857540,9.624466,-0.347502,0.396229,8.922230,-5.755316,2.081514,5.793873,-0.960323,-8.571766,-5.418761,-8.301597,-9.015494,-8.901205,9.928300,6.919551,-8.472841,-3.872330,-0.357755,3.664523,9.619899,4.036799,-4.512115,-2.093452,8.920490,-6.303198,-2.344623,-8.037486,5.506993,5.356984,-4.905956,-2.805289,8.233572,8.242437,-5.278473,8.486511,-3.564046,0.109127,-8.737329,5.004451,-8.583317,6.077602,-1.393485,7.071862,6.676212,-2.082695,8.364585,-0.204512,-3.217011,-9.954490,-2.833092,-5.142485,0.600980,-3.868450,-7.534399,1.372650,5.344495,5.002888,-0.997269,1.997143,3.981813,-3.679571,-9.747635,-5.910786,-4.434024,-0.105151,-8.515024,-4.637017,-8.428329,3.453338,-2.399825,4.471840,-1.284238,-9.412390,0.280324,-7.725477,7.085651,-8.587606,2.710596,-3.584274,4.879713,-1.135216,-6.106590,2.136304,0.816035,7.900411,-8.677026,7.909917,3.191319,1.801034,-8.911225,-0.583078,-5.236160,7.765309,2.701167,-4.537328,-1.134680,-7.835639,1.946412,9.798309,1.005374,-8.753617,4.689914,-8.900861,2.284003,-0.191625,5.065210,-7.717363,5.556142,5.210997,7.667502,1.446500,-6.422699,-2.037880,-8.456061,8.296882,-8.284169,3.672581,5.648514,0.648414,6.255046,-0.023939,-4.806294,0.427622,7.924125,-6.940169,-0.418110,-5.184000,6.873461,-1.077064,8.036580,4.975098,8.987655,9.107219,-7.682117,-2.401104,-6.190521,-3.816461,3.991968,-1.576737,-6.635028,9.541669,5.099148,-6.277776,7.324405,-7.444742,-3.433546,-6.344534,-5.682287,-0.707992,-4.906265,-4.646606,-7.691584,2.208356,-5.899007,-1.590435,-2.605317,3.887388,4.966675,3.806282,-2.426334,9.658110,0.302033,4.528627,-9.106531,9.621207,-9.648725,4.478373,-1.441156,-1.212378,3.194833,-8.524301,-6.957797,2.366990,6.210275,-0.826383,-5.783453,-3.702121,-4.703540,4.149096,2.747578,8.636273,-0.849506,-2.408996,-4.713322,-1.009629,0.782885,2.859826,-6.064979,-8.818888,9.881407,-9.645670,-5.404495,-6.371593,-6.083485,8.277875,-1.148235,6.882955,-1.583842,5.374164,-9.983688,-0.582178,-2.144575,5.335211,-0.754146,-2.506750,9.960734,6.173303,7.702294,-9.118636,4.541266,-4.496759,-0.252179,-9.650137,8.296516,1.994465,4.483075,-2.712343,-8.520618,3.454512,8.029066,-7.329592,-8.137265,-9.020748,2.847818,1.772261,3.979135,-2.754601,3.948005,-6.277808,6.730131,-5.748851,8.183843,-1.016184,-1.370378,-7.175983,-2.047283,-6.645392,-0.510525,-5.235404,3.133589,-6.308183,0.926355,8.390953,0.052900,-5.148910,9.962751,-7.354643,3.254089,-9.054254,-5.498010,1.490644,-8.116229,9.082234,-2.099837,-2.331375,4.168097,-4.494539,-3.383895,8.406822,7.852163,-7.079439,-8.984274,9.516442,5.022273,1.409753,-6.983786,-9.618198,2.551036,5.537771,-1.868382,3.283084,-4.897865,-4.933780,7.312351,2.441456,2.312528,-6.191492,-8.557058,1.457825,2.867236,4.541534,0.375060,-1.330512,5.223780,3.151429,-8.745922,5.575318,-2.755511,4.425191,7.600233,7.571821,-2.291431,-4.699472,6.392729,-0.871366,-1.416307,3.624005,-5.395658,-0.788733,2.499847,8.519859,8.821053,2.867508,-1.835448,2.705792], dtype = "float32")#candidate|3740|(1755,)|const|float32
call_3738 = relay.TupleGetItem(func_3569_call(relay.reshape(const_3739.astype('int32'), [252,]), relay.reshape(const_3740.astype('float32'), [1755,]), ), 2)
call_3741 = relay.TupleGetItem(func_3572_call(relay.reshape(const_3739.astype('int32'), [252,]), relay.reshape(const_3740.astype('float32'), [1755,]), ), 2)
output = relay.Tuple([call_3720,call_3738,const_3739,const_3740,])
output2 = relay.Tuple([call_3721,call_3741,const_3739,const_3740,])
func_3742 = relay.Function([], output)
mod['func_3742'] = func_3742
mod = relay.transform.InferType()(mod)
mutated_mod['func_3742'] = func_3742
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3742_call = mutated_mod.get_global_var('func_3742')
call_3743 = func_3742_call()
output = call_3743
func_3744 = relay.Function([], output)
mutated_mod['func_3744'] = func_3744
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3363_call = mod.get_global_var('func_3363')
func_3364_call = mutated_mod.get_global_var('func_3364')
call_3763 = relay.TupleGetItem(func_3363_call(), 1)
call_3764 = relay.TupleGetItem(func_3364_call(), 1)
output = relay.Tuple([call_3763,])
output2 = relay.Tuple([call_3764,])
func_3772 = relay.Function([], output)
mod['func_3772'] = func_3772
mod = relay.transform.InferType()(mod)
output = func_3772()
func_3773 = relay.Function([], output)
mutated_mod['func_3773'] = func_3773
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3427_call = mod.get_global_var('func_3427')
func_3428_call = mutated_mod.get_global_var('func_3428')
call_3789 = relay.TupleGetItem(func_3427_call(), 0)
call_3790 = relay.TupleGetItem(func_3428_call(), 0)
uop_3791 = relay.cos(call_3789.astype('float64')) # shape=(2, 1, 8)
uop_3793 = relay.cos(call_3790.astype('float64')) # shape=(2, 1, 8)
func_2971_call = mod.get_global_var('func_2971')
func_2974_call = mutated_mod.get_global_var('func_2974')
const_3802 = relay.const([[-1.354411,-0.558899,-0.919570,4.780409],[-4.937851,0.784103,4.290479,-8.998432],[5.025342,6.044362,-2.115784,-0.491661],[7.767858,-7.707919,-7.641537,-8.902494],[-2.460769,-4.878627,-5.884010,-4.374920],[6.158841,4.609945,-8.173389,8.848004],[8.151557,2.105539,-2.537248,-3.474283],[4.035054,2.406729,7.878723,-3.035719],[-7.038458,-2.629702,9.549458,9.423759],[-7.112429,4.854192,-9.082867,-0.349560],[3.945466,-4.855819,-3.273326,1.913585],[9.141951,0.784328,0.123674,-8.994405],[-2.497093,-7.099498,-1.785985,6.024119],[-7.564487,3.578072,7.011335,-0.808642],[6.642989,-5.323981,9.665007,1.072466],[-5.382510,1.159292,-6.878573,1.870493],[-8.055835,-6.978697,0.561547,-6.880512],[-7.282787,-7.378538,6.561962,5.373054],[8.108027,-2.536279,2.765713,-2.701912],[-8.287753,0.010461,1.617667,-9.425911],[9.581201,-6.304952,-9.728036,-5.356132],[-7.683294,-0.716731,-7.772422,-9.466045],[9.105170,-3.831900,-6.366643,-2.758036],[6.545158,-2.002285,-5.696098,-9.407871],[4.997364,-7.828321,3.206232,3.778371],[9.516067,-0.692260,2.296470,-0.226874],[8.019458,3.464847,5.270137,8.015706],[-9.282527,8.168212,-5.646656,-2.680340]], dtype = "float32")#candidate|3802|(28, 4)|const|float32
call_3801 = func_2971_call(relay.reshape(const_3802.astype('float32'), [2, 7, 8]))
call_3803 = func_2971_call(relay.reshape(const_3802.astype('float32'), [2, 7, 8]))
const_3816 = relay.const([[[2.092908,8.546352,-6.345577,4.585459,-4.288447,-1.658442,-0.288371,-0.473483],[-0.373222,-1.306042,-6.955075,6.318397,5.471561,-9.083996,-6.319264,-3.599211],[-6.120213,-7.690145,-2.928572,-6.591297,-2.677913,-6.434416,9.302722,-1.351150],[-8.241557,-9.474258,8.842145,-4.956110,-6.229781,5.245945,-4.045938,-9.535592]],[[8.570893,-6.891425,-6.693761,-5.656992,5.006989,-6.569824,-3.643494,-5.059608],[7.406299,9.615062,-4.268741,6.942207,1.144828,3.647023,5.128931,-9.975545],[-0.717384,-5.234832,2.365064,1.573776,9.206224,-3.565983,-1.688385,-8.395362],[2.767297,1.737439,2.433466,-1.278547,1.836683,0.626824,3.068359,2.026154]]], dtype = "float64")#candidate|3816|(2, 4, 8)|const|float64
bop_3817 = relay.floor_divide(uop_3791.astype('float64'), const_3816.astype('float64')) # shape=(2, 4, 8)
bop_3820 = relay.floor_divide(uop_3793.astype('float64'), const_3816.astype('float64')) # shape=(2, 4, 8)
func_1341_call = mod.get_global_var('func_1341')
func_1344_call = mutated_mod.get_global_var('func_1344')
var_3839 = relay.var("var_3839", dtype = "int32", shape = (252,))#candidate|3839|(252,)|var|int32
var_3840 = relay.var("var_3840", dtype = "float32", shape = (1, 1755))#candidate|3840|(1, 1755)|var|float32
call_3838 = relay.TupleGetItem(func_1341_call(relay.reshape(var_3839.astype('int32'), [252,]), relay.reshape(var_3840.astype('float32'), [1755,]), ), 1)
call_3841 = relay.TupleGetItem(func_1344_call(relay.reshape(var_3839.astype('int32'), [252,]), relay.reshape(var_3840.astype('float32'), [1755,]), ), 1)
func_3341_call = mod.get_global_var('func_3341')
func_3342_call = mutated_mod.get_global_var('func_3342')
call_3848 = relay.TupleGetItem(func_3341_call(), 3)
call_3849 = relay.TupleGetItem(func_3342_call(), 3)
output = relay.Tuple([call_3801,const_3802,bop_3817,call_3838,var_3839,var_3840,call_3848,])
output2 = relay.Tuple([call_3803,const_3802,bop_3820,call_3841,var_3839,var_3840,call_3849,])
func_3851 = relay.Function([var_3839,var_3840,], output)
mod['func_3851'] = func_3851
mod = relay.transform.InferType()(mod)
mutated_mod['func_3851'] = func_3851
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3851_call = mutated_mod.get_global_var('func_3851')
var_3853 = relay.var("var_3853", dtype = "int32", shape = (252,))#candidate|3853|(252,)|var|int32
var_3854 = relay.var("var_3854", dtype = "float32", shape = (1, 1755))#candidate|3854|(1, 1755)|var|float32
call_3852 = func_3851_call(var_3853,var_3854,)
output = call_3852
func_3855 = relay.Function([var_3853,var_3854,], output)
mutated_mod['func_3855'] = func_3855
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2307_call = mod.get_global_var('func_2307')
func_2309_call = mutated_mod.get_global_var('func_2309')
call_3871 = relay.TupleGetItem(func_2307_call(), 0)
call_3872 = relay.TupleGetItem(func_2309_call(), 0)
output = relay.Tuple([call_3871,])
output2 = relay.Tuple([call_3872,])
func_3896 = relay.Function([], output)
mod['func_3896'] = func_3896
mod = relay.transform.InferType()(mod)
mutated_mod['func_3896'] = func_3896
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3896_call = mutated_mod.get_global_var('func_3896')
call_3897 = func_3896_call()
output = call_3897
func_3898 = relay.Function([], output)
mutated_mod['func_3898'] = func_3898
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3123_call = mod.get_global_var('func_3123')
func_3124_call = mutated_mod.get_global_var('func_3124')
call_3904 = relay.TupleGetItem(func_3123_call(), 0)
call_3905 = relay.TupleGetItem(func_3124_call(), 0)
output = call_3904
output2 = call_3905
func_3918 = relay.Function([], output)
mod['func_3918'] = func_3918
mod = relay.transform.InferType()(mod)
mutated_mod['func_3918'] = func_3918
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3918_call = mutated_mod.get_global_var('func_3918')
call_3919 = func_3918_call()
output = call_3919
func_3920 = relay.Function([], output)
mutated_mod['func_3920'] = func_3920
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3918_call = mod.get_global_var('func_3918')
func_3920_call = mutated_mod.get_global_var('func_3920')
call_3928 = func_3918_call()
call_3929 = func_3918_call()
output = relay.Tuple([call_3928,])
output2 = relay.Tuple([call_3929,])
func_3930 = relay.Function([], output)
mod['func_3930'] = func_3930
mod = relay.transform.InferType()(mod)
output = func_3930()
func_3931 = relay.Function([], output)
mutated_mod['func_3931'] = func_3931
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2445_call = mod.get_global_var('func_2445')
func_2446_call = mutated_mod.get_global_var('func_2446')
call_4014 = relay.TupleGetItem(func_2445_call(), 0)
call_4015 = relay.TupleGetItem(func_2446_call(), 0)
func_3302_call = mod.get_global_var('func_3302')
func_3303_call = mutated_mod.get_global_var('func_3303')
call_4018 = func_3302_call()
call_4019 = func_3302_call()
func_2539_call = mod.get_global_var('func_2539')
func_2542_call = mutated_mod.get_global_var('func_2542')
var_4032 = relay.var("var_4032", dtype = "float32", shape = (80,))#candidate|4032|(80,)|var|float32
var_4033 = relay.var("var_4033", dtype = "float32", shape = ())#candidate|4033|()|var|float32
call_4031 = relay.TupleGetItem(func_2539_call(relay.reshape(var_4032.astype('float32'), [2, 5, 8]), relay.reshape(var_4033.astype('float32'), []), ), 0)
call_4034 = relay.TupleGetItem(func_2542_call(relay.reshape(var_4032.astype('float32'), [2, 5, 8]), relay.reshape(var_4033.astype('float32'), []), ), 0)
output = relay.Tuple([call_4014,call_4018,call_4031,var_4032,var_4033,])
output2 = relay.Tuple([call_4015,call_4019,call_4034,var_4032,var_4033,])
func_4068 = relay.Function([var_4032,var_4033,], output)
mod['func_4068'] = func_4068
mod = relay.transform.InferType()(mod)
mutated_mod['func_4068'] = func_4068
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4068_call = mutated_mod.get_global_var('func_4068')
var_4070 = relay.var("var_4070", dtype = "float32", shape = (80,))#candidate|4070|(80,)|var|float32
var_4071 = relay.var("var_4071", dtype = "float32", shape = ())#candidate|4071|()|var|float32
call_4069 = func_4068_call(var_4070,var_4071,)
output = call_4069
func_4072 = relay.Function([var_4070,var_4071,], output)
mutated_mod['func_4072'] = func_4072
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3341_call = mod.get_global_var('func_3341')
func_3342_call = mutated_mod.get_global_var('func_3342')
call_4125 = relay.TupleGetItem(func_3341_call(), 6)
call_4126 = relay.TupleGetItem(func_3342_call(), 6)
uop_4135 = relay.tan(call_4125.astype('float32')) # shape=(250, 2)
uop_4137 = relay.tan(call_4126.astype('float32')) # shape=(250, 2)
output = uop_4135
output2 = uop_4137
func_4141 = relay.Function([], output)
mod['func_4141'] = func_4141
mod = relay.transform.InferType()(mod)
output = func_4141()
func_4142 = relay.Function([], output)
mutated_mod['func_4142'] = func_4142
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3427_call = mod.get_global_var('func_3427')
func_3428_call = mutated_mod.get_global_var('func_3428')
call_4152 = relay.TupleGetItem(func_3427_call(), 0)
call_4153 = relay.TupleGetItem(func_3428_call(), 0)
output = call_4152
output2 = call_4153
func_4165 = relay.Function([], output)
mod['func_4165'] = func_4165
mod = relay.transform.InferType()(mod)
output = func_4165()
func_4166 = relay.Function([], output)
mutated_mod['func_4166'] = func_4166
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2278_call = mod.get_global_var('func_2278')
func_2280_call = mutated_mod.get_global_var('func_2280')
call_4197 = func_2278_call()
call_4198 = func_2278_call()
uop_4204 = relay.sqrt(call_4197.astype('float64')) # shape=(2, 1, 8)
uop_4206 = relay.sqrt(call_4198.astype('float64')) # shape=(2, 1, 8)
func_2699_call = mod.get_global_var('func_2699')
func_2703_call = mutated_mod.get_global_var('func_2703')
const_4213 = relay.const([1.534689,2.921653,7.513665,1.536913,8.441316,-1.626684,4.394371,-7.426257,5.609499,4.047141,8.333244,-5.229352,4.275061,9.138348,-0.810336,-4.118456,-2.547582,-0.481464,0.787887,3.031061,-1.842604,-6.564357,-5.749543,2.179402,4.732316,-0.008093,-8.735909,-0.566569,-4.966722,-4.074920,-7.835734,-9.837363,6.228272,-1.628070,-5.666719,3.104919,4.517192,-6.198974,-8.682946,6.099347,9.351628,-3.793888,-5.499748,5.765861,-6.526758,-6.005624,2.788130,2.652169,8.236071,8.768681,7.393030,-2.638660,-3.276926,-5.695994,-1.432580,-0.103912,6.121423,1.628099,0.367861,6.407967,6.131372,-1.182054,-6.127941,6.281804,8.347854,-6.088053,4.261896,-3.667715,7.548179,-9.575948,-3.951844,4.035804,6.964646,-5.466917,-3.944137,-3.109959,0.756441,-6.232093,-1.201816,8.350557,-9.413625,-1.219760,-0.216438,-7.899619,7.667964,6.820987,6.970542,1.030301,2.278885,-6.775997,9.085092,2.791977,9.941132,7.173749,0.115374,-3.579693,-2.100270,9.826065,1.619954,-2.818708,-8.117660,-4.287303,6.243861,-4.608104,3.367912,-9.848557,9.910308,9.136945,6.231556,-3.940530,3.735235,-7.327238,7.184835,-6.681246,0.071430,8.633413,-3.996275,-3.119951,-9.459910,6.476745,7.463787,-5.473343,5.048829,8.042995,-2.254110,-3.092580,-6.374178,6.970790,-3.576966,-1.626806,4.893552,-4.130398,-1.191591,0.758020,7.013042,-9.479732,-3.249230,-2.863258,5.347892,-1.185035,4.250509,8.848367,8.132605,-3.503674,3.161985,-7.944625,-4.521995,-4.932215,2.822682,3.560399,-6.396623,3.344805,4.306790,0.575276,6.275304,-3.212499,-8.265660,8.332749,8.142216,2.683724,-6.432902,3.733666,-7.562844,9.797867,8.791533,5.189485,9.797501,-5.175360,-0.092503,9.720248,8.947439,-7.027342,8.999553,6.135590,3.328000,6.435732,-8.572771,3.611950,0.811452,-3.826005,0.063860,-8.752883,-7.918737,6.766775,-7.165062,8.149393,2.896180,0.617159,3.829417,2.788542,-7.896486,-1.871701,6.498337,1.535232,9.377775,5.807976,1.901253,7.790691,-5.845280,-0.551779,7.582055,-3.625856,-0.715767,9.766196,-4.069958,-1.349691,-9.774062,-7.797515,-5.930506,-2.509050,9.483340,1.486078,1.538023,0.365732,8.006721,3.836207,3.442249,0.882154,8.553748,8.268160,1.223695,-4.001413,-5.459942,6.470971,8.180742,-5.545744,7.129993,1.326945,-3.096749,-2.638089,3.925267,-2.501773,0.630669,-8.193919,0.071294,1.882438,4.376381,-1.217967,-3.308981,5.286847,8.641941,-0.878789,4.536848,5.110842,-5.714111,4.911730,9.911037,-0.341966,-2.151478,-0.383038,-1.739194,-0.018344,2.003207,-9.949909,6.615131,4.986379,9.614496,1.493679,-3.879031,5.668853,8.214397,-3.924160,-8.781731,6.972202,7.761225,-9.914262,1.344664,7.726594,0.587964,-0.358773,0.539754,8.408089,-0.333964,3.709325,-8.735274,5.629004,-9.070785,-4.368336,3.760178,2.516017,5.435767,-6.679574,-9.843702,-7.148387,5.505133,-6.636699,-3.520295,-1.942844,3.152273,5.485028,-8.558965,9.920329,-9.425993,9.829532,0.729800,-3.089173,6.594821,-0.936513,2.841319,5.837211,1.631323,4.769111,-4.088117,-8.489093,-0.711839,9.849895,5.174936,5.359069,-6.667583,0.508571,5.419736,7.404087,-2.117753,-6.061025,-7.369364,1.806886,-7.700746,0.039529,-3.401082,-9.018290,-4.733127,9.117614,-7.201886,5.320015,0.824979,-6.634557,7.241271,7.030151,4.273711,8.520692,-3.310965,-4.932446,8.918490,7.795155,2.312578,-7.062951,8.987305,0.152029,-5.802762,-5.814700,2.538344,-9.671617,-9.502733,8.424986,-9.323767,1.614079,5.830027,3.454063,-5.285795,-2.385050,-1.201090,9.757293,-6.499615,7.242185,0.733651,-8.838365,-5.825216,2.667386,2.238507,0.197245,2.184704,-7.908025,-6.657493,-1.581466,-4.716650,-7.662429,8.880192,-7.213542,5.339688,2.865159,5.421945,9.192268,-5.186752,7.984335,4.800003,1.423448,7.524699,3.257433,0.057105,-5.741163,-1.676469,-3.245916,-9.378422,7.856365,-4.052277,9.582858,2.707799,-2.352376,2.661706,0.499320,-8.488808,-7.531712,-8.052496,5.777635,2.305185,9.667921,-4.854295,1.861630,-7.868320,-6.804409,7.287951,-2.848564,1.549243,5.780855,-9.107981,2.852135,7.782396,1.778383,-0.391451,-3.318084,-4.611990,0.063643,1.890436,-0.026720,-1.252821,8.439211,-7.575211,-3.295738,-5.651446,-8.743440,-1.029486,7.652724,7.353501,9.170858,2.742005,9.417524,0.525479,-3.886781,-0.162124,-6.142903,-8.170843,-7.580352,8.259497,-9.549292,-9.946786,4.797575,-9.756455,1.872345,8.485911,4.494793,-7.337862,-6.071345,-1.666991,-6.461563,5.365511,9.102647,-6.471239,-5.508159,-1.204030,0.044457,-9.676881,7.723820,7.419040,-0.046558,7.687075,1.237504,8.252212,0.805710,4.761784,-6.574108,-0.881702,-4.649205], dtype = "float64")#candidate|4213|(462,)|const|float64
call_4212 = func_2699_call(relay.reshape(const_4213.astype('float64'), [14, 11, 3]), relay.reshape(const_4213.astype('float64'), [14, 11, 3]), )
call_4214 = func_2699_call(relay.reshape(const_4213.astype('float64'), [14, 11, 3]), relay.reshape(const_4213.astype('float64'), [14, 11, 3]), )
func_1423_call = mod.get_global_var('func_1423')
func_1426_call = mutated_mod.get_global_var('func_1426')
const_4218 = relay.const([-2.430137,5.144591,0.225045,9.138835,-8.066196,-6.093559,-4.887624,-9.969853,0.213936,4.875651,-2.876838,0.049777,-5.848328,7.933775,7.184610,-7.037735,-9.658227,-7.654929,-4.826559,-7.507814,-9.278710,-1.193499,-6.095934,-7.156682,3.287463,-8.051570,-7.128993,-9.292523,5.750112,-2.889265,5.386820,-2.774882,-3.091012,2.219011,-4.754998,7.579730,-2.415507,5.692521,-8.568719,-6.909521,4.944481,0.720098,-3.457279,3.673734,8.600721,-6.669338,-2.695132,-6.120199,-1.872245,7.947731,2.018729,5.760790,-5.210774,-6.183529,-5.922369,-3.358971,-7.709212,4.664030,-8.767930,-4.654459,-8.590994,-0.164376,8.588196,8.953142,-1.198501,-2.879008,0.281880,9.784162,-3.733026,-8.355528,4.349718,8.963992,-4.830391,-4.140128,3.404703,-9.837132,-8.543719,-9.862382,8.658076,1.705716,9.724602,0.228770,8.076258,-8.655479,0.870699,-6.745311,-3.051503,-3.468868,-8.253436,5.045433,5.135518,5.688246,-0.408775,1.333392,4.123597,0.750576,-3.058975,9.469983,5.128816,1.223083,-8.561868,0.185110,1.162091,4.148635,4.143489,2.007055,-4.914357,-2.592897,4.024578,-3.527768,-9.702399,5.088260,-4.408213,-9.676525,-4.765986,-6.401747,6.405845,9.462547,5.323090,-0.300036,9.785669,9.214010,-5.235541,-3.590100,3.762614,-7.046580,-9.441644,-8.370984,-9.672075,7.983452,6.829607,9.525145,1.289214,6.856369,4.111724,9.394165,-0.039145,-9.051103,-8.169834,-5.487647,5.221522,0.168202,-5.758410,-0.034557,-4.633998,1.141401,-0.714966,-6.353781,-5.322930,-5.734075,5.044252,-3.201701,7.108528,-3.819238,-1.304480,5.495612,7.787574,8.938684,9.537428,-5.143831], dtype = "float64")#candidate|4218|(160,)|const|float64
call_4217 = func_1423_call(relay.reshape(const_4218.astype('float64'), [16, 5, 2]))
call_4219 = func_1423_call(relay.reshape(const_4218.astype('float64'), [16, 5, 2]))
output = relay.Tuple([uop_4204,call_4212,const_4213,call_4217,const_4218,])
output2 = relay.Tuple([uop_4206,call_4214,const_4213,call_4219,const_4218,])
func_4222 = relay.Function([], output)
mod['func_4222'] = func_4222
mod = relay.transform.InferType()(mod)
output = func_4222()
func_4223 = relay.Function([], output)
mutated_mod['func_4223'] = func_4223
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3267_call = mod.get_global_var('func_3267')
func_3268_call = mutated_mod.get_global_var('func_3268')
call_4227 = func_3267_call()
call_4228 = func_3267_call()
output = call_4227
output2 = call_4228
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
func_4222_call = mod.get_global_var('func_4222')
func_4223_call = mutated_mod.get_global_var('func_4223')
call_4241 = relay.TupleGetItem(func_4222_call(), 1)
call_4242 = relay.TupleGetItem(func_4223_call(), 1)
output = relay.Tuple([call_4241,])
output2 = relay.Tuple([call_4242,])
func_4246 = relay.Function([], output)
mod['func_4246'] = func_4246
mod = relay.transform.InferType()(mod)
output = func_4246()
func_4247 = relay.Function([], output)
mutated_mod['func_4247'] = func_4247
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4305 = relay.const(-4, dtype = "uint64")#candidate|4305|()|const|uint64
var_4306 = relay.var("var_4306", dtype = "uint64", shape = (1, 2, 11))#candidate|4306|(1, 2, 11)|var|uint64
bop_4307 = relay.logical_xor(const_4305.astype('uint64'), var_4306.astype('uint64')) # shape=(1, 2, 11)
func_2734_call = mod.get_global_var('func_2734')
func_2736_call = mutated_mod.get_global_var('func_2736')
const_4315 = relay.const([-5,9,-5,-8,-9,-7,-1,-8,-8,7,-8,-6,8,10,-3,4,-9,10,3,6,-4,-3,-5,2,-7,-3,-7,-7,-7,1,-4,-10,9,-7,-7,-8,-6,-5,-1,6,-7,-4,-8,-1,10,8,8,8,-9,2,10,8,3,8,-2,6,3,-4,-3,-9,7,-8,7,-2,3,-4,-8,-10,10,6,2,1,-4,-6,10,-1,-3,1,6,-6,-7,-3,-7,-5,1,-8,5,-8,-6,5,10,-4,4,-10,-9,1,-1,1,7,4,9,-3,-5,5,-5,-7,4,-5,7,9,6,-1,4,4,10,-1,3,-7,-5,8], dtype = "int64")#candidate|4315|(120,)|const|int64
call_4314 = relay.TupleGetItem(func_2734_call(relay.reshape(const_4315.astype('int64'), [120,])), 4)
call_4316 = relay.TupleGetItem(func_2736_call(relay.reshape(const_4315.astype('int64'), [120,])), 4)
output = relay.Tuple([bop_4307,call_4314,const_4315,])
output2 = relay.Tuple([bop_4307,call_4316,const_4315,])
func_4323 = relay.Function([var_4306,], output)
mod['func_4323'] = func_4323
mod = relay.transform.InferType()(mod)
mutated_mod['func_4323'] = func_4323
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4324 = relay.var("var_4324", dtype = "uint64", shape = (1, 2, 11))#candidate|4324|(1, 2, 11)|var|uint64
func_4323_call = mutated_mod.get_global_var('func_4323')
call_4325 = func_4323_call(var_4324)
output = call_4325
func_4326 = relay.Function([var_4324], output)
mutated_mod['func_4326'] = func_4326
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3493_call = mod.get_global_var('func_3493')
func_3494_call = mutated_mod.get_global_var('func_3494')
call_4348 = func_3493_call()
call_4349 = func_3493_call()
func_1423_call = mod.get_global_var('func_1423')
func_1426_call = mutated_mod.get_global_var('func_1426')
call_4350 = func_1423_call(relay.reshape(call_4348.astype('float64'), [16, 5, 2]))
call_4351 = func_1423_call(relay.reshape(call_4348.astype('float64'), [16, 5, 2]))
var_4352 = relay.var("var_4352", dtype = "float64", shape = (16, 5, 2))#candidate|4352|(16, 5, 2)|var|float64
bop_4353 = relay.floor_divide(call_4350.astype('float32'), relay.reshape(var_4352.astype('float32'), relay.shape_of(call_4350))) # shape=(16, 5, 2)
bop_4356 = relay.floor_divide(call_4351.astype('float32'), relay.reshape(var_4352.astype('float32'), relay.shape_of(call_4351))) # shape=(16, 5, 2)
uop_4360 = relay.erf(bop_4353.astype('float32')) # shape=(16, 5, 2)
uop_4362 = relay.erf(bop_4356.astype('float32')) # shape=(16, 5, 2)
func_2699_call = mod.get_global_var('func_2699')
func_2703_call = mutated_mod.get_global_var('func_2703')
var_4375 = relay.var("var_4375", dtype = "float64", shape = (462,))#candidate|4375|(462,)|var|float64
call_4374 = func_2699_call(relay.reshape(var_4375.astype('float64'), [14, 11, 3]), relay.reshape(var_4375.astype('float64'), [14, 11, 3]), )
call_4376 = func_2699_call(relay.reshape(var_4375.astype('float64'), [14, 11, 3]), relay.reshape(var_4375.astype('float64'), [14, 11, 3]), )
func_3742_call = mod.get_global_var('func_3742')
func_3744_call = mutated_mod.get_global_var('func_3744')
call_4387 = relay.TupleGetItem(func_3742_call(), 3)
call_4388 = relay.TupleGetItem(func_3744_call(), 3)
output = relay.Tuple([call_4348,uop_4360,call_4374,var_4375,call_4387,])
output2 = relay.Tuple([call_4349,uop_4362,call_4376,var_4375,call_4388,])
func_4389 = relay.Function([var_4352,var_4375,], output)
mod['func_4389'] = func_4389
mod = relay.transform.InferType()(mod)
mutated_mod['func_4389'] = func_4389
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4389_call = mutated_mod.get_global_var('func_4389')
var_4391 = relay.var("var_4391", dtype = "float64", shape = (16, 5, 2))#candidate|4391|(16, 5, 2)|var|float64
var_4392 = relay.var("var_4392", dtype = "float64", shape = (462,))#candidate|4392|(462,)|var|float64
call_4390 = func_4389_call(var_4391,var_4392,)
output = call_4390
func_4393 = relay.Function([var_4391,var_4392,], output)
mutated_mod['func_4393'] = func_4393
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4165_call = mod.get_global_var('func_4165')
func_4166_call = mutated_mod.get_global_var('func_4166')
call_4462 = func_4165_call()
call_4463 = func_4165_call()
func_4141_call = mod.get_global_var('func_4141')
func_4142_call = mutated_mod.get_global_var('func_4142')
call_4464 = func_4141_call()
call_4465 = func_4141_call()
var_4470 = relay.var("var_4470", dtype = "float32", shape = (250, 2))#candidate|4470|(250, 2)|var|float32
bop_4471 = relay.bitwise_and(call_4464.astype('uint64'), relay.reshape(var_4470.astype('uint64'), relay.shape_of(call_4464))) # shape=(250, 2)
bop_4474 = relay.bitwise_and(call_4465.astype('uint64'), relay.reshape(var_4470.astype('uint64'), relay.shape_of(call_4465))) # shape=(250, 2)
uop_4477 = relay.asinh(var_4470.astype('float64')) # shape=(250, 2)
output = relay.Tuple([call_4462,bop_4471,uop_4477,])
output2 = relay.Tuple([call_4463,bop_4474,uop_4477,])
func_4479 = relay.Function([var_4470,], output)
mod['func_4479'] = func_4479
mod = relay.transform.InferType()(mod)
mutated_mod['func_4479'] = func_4479
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4480 = relay.var("var_4480", dtype = "float32", shape = (250, 2))#candidate|4480|(250, 2)|var|float32
func_4479_call = mutated_mod.get_global_var('func_4479')
call_4481 = func_4479_call(var_4480)
output = call_4481
func_4482 = relay.Function([var_4480], output)
mutated_mod['func_4482'] = func_4482
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4507 = relay.var("var_4507", dtype = "int8", shape = ())#candidate|4507|()|var|int8
var_4508 = relay.var("var_4508", dtype = "int8", shape = (10, 5, 12))#candidate|4508|(10, 5, 12)|var|int8
bop_4509 = relay.logical_xor(var_4507.astype('int8'), var_4508.astype('int8')) # shape=(10, 5, 12)
bop_4542 = relay.divide(var_4507.astype('float32'), bop_4509.astype('float32')) # shape=(10, 5, 12)
output = bop_4542
output2 = bop_4542
func_4578 = relay.Function([var_4507,var_4508,], output)
mod['func_4578'] = func_4578
mod = relay.transform.InferType()(mod)
mutated_mod['func_4578'] = func_4578
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4578_call = mutated_mod.get_global_var('func_4578')
var_4580 = relay.var("var_4580", dtype = "int8", shape = ())#candidate|4580|()|var|int8
var_4581 = relay.var("var_4581", dtype = "int8", shape = (10, 5, 12))#candidate|4581|(10, 5, 12)|var|int8
call_4579 = func_4578_call(var_4580,var_4581,)
output = call_4579
func_4582 = relay.Function([var_4580,var_4581,], output)
mutated_mod['func_4582'] = func_4582
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2278_call = mod.get_global_var('func_2278')
func_2280_call = mutated_mod.get_global_var('func_2280')
call_4616 = func_2278_call()
call_4617 = func_2278_call()
func_3918_call = mod.get_global_var('func_3918')
func_3920_call = mutated_mod.get_global_var('func_3920')
call_4618 = func_3918_call()
call_4619 = func_3918_call()
bop_4626 = relay.floor_mod(call_4616.astype('float32'), relay.reshape(call_4618.astype('float32'), relay.shape_of(call_4616))) # shape=(2, 1, 8)
bop_4629 = relay.floor_mod(call_4617.astype('float32'), relay.reshape(call_4619.astype('float32'), relay.shape_of(call_4617))) # shape=(2, 1, 8)
output = relay.Tuple([bop_4626,])
output2 = relay.Tuple([bop_4629,])
func_4630 = relay.Function([], output)
mod['func_4630'] = func_4630
mod = relay.transform.InferType()(mod)
output = func_4630()
func_4631 = relay.Function([], output)
mutated_mod['func_4631'] = func_4631
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4165_call = mod.get_global_var('func_4165')
func_4166_call = mutated_mod.get_global_var('func_4166')
call_4676 = func_4165_call()
call_4677 = func_4165_call()
output = call_4676
output2 = call_4677
func_4689 = relay.Function([], output)
mod['func_4689'] = func_4689
mod = relay.transform.InferType()(mod)
mutated_mod['func_4689'] = func_4689
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4689_call = mutated_mod.get_global_var('func_4689')
call_4690 = func_4689_call()
output = call_4690
func_4691 = relay.Function([], output)
mutated_mod['func_4691'] = func_4691
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2900_call = mod.get_global_var('func_2900')
func_2901_call = mutated_mod.get_global_var('func_2901')
call_4759 = relay.TupleGetItem(func_2900_call(), 3)
call_4760 = relay.TupleGetItem(func_2901_call(), 3)
output = relay.Tuple([call_4759,])
output2 = relay.Tuple([call_4760,])
func_4807 = relay.Function([], output)
mod['func_4807'] = func_4807
mod = relay.transform.InferType()(mod)
mutated_mod['func_4807'] = func_4807
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4807_call = mutated_mod.get_global_var('func_4807')
call_4808 = func_4807_call()
output = call_4808
func_4809 = relay.Function([], output)
mutated_mod['func_4809'] = func_4809
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4830 = relay.var("var_4830", dtype = "float64", shape = (4, 16, 7))#candidate|4830|(4, 16, 7)|var|float64
uop_4831 = relay.acos(var_4830.astype('float64')) # shape=(4, 16, 7)
bop_4848 = relay.minimum(var_4830.astype('int32'), relay.reshape(uop_4831.astype('int32'), relay.shape_of(var_4830))) # shape=(4, 16, 7)
bop_4860 = relay.logical_and(uop_4831.astype('bool'), relay.reshape(var_4830.astype('bool'), relay.shape_of(uop_4831))) # shape=(4, 16, 7)
uop_4863 = relay.sin(var_4830.astype('float32')) # shape=(4, 16, 7)
output = relay.Tuple([bop_4848,bop_4860,uop_4863,])
output2 = relay.Tuple([bop_4848,bop_4860,uop_4863,])
func_4865 = relay.Function([var_4830,], output)
mod['func_4865'] = func_4865
mod = relay.transform.InferType()(mod)
mutated_mod['func_4865'] = func_4865
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4866 = relay.var("var_4866", dtype = "float64", shape = (4, 16, 7))#candidate|4866|(4, 16, 7)|var|float64
func_4865_call = mutated_mod.get_global_var('func_4865')
call_4867 = func_4865_call(var_4866)
output = call_4867
func_4868 = relay.Function([var_4866], output)
mutated_mod['func_4868'] = func_4868
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3896_call = mod.get_global_var('func_3896')
func_3898_call = mutated_mod.get_global_var('func_3898')
call_4914 = relay.TupleGetItem(func_3896_call(), 0)
call_4915 = relay.TupleGetItem(func_3898_call(), 0)
uop_4919 = relay.tan(call_4914.astype('float32')) # shape=(2, 1, 8)
uop_4921 = relay.tan(call_4915.astype('float32')) # shape=(2, 1, 8)
func_2644_call = mod.get_global_var('func_2644')
func_2646_call = mutated_mod.get_global_var('func_2646')
call_4925 = relay.TupleGetItem(func_2644_call(), 0)
call_4926 = relay.TupleGetItem(func_2646_call(), 0)
output = relay.Tuple([uop_4919,call_4925,])
output2 = relay.Tuple([uop_4921,call_4926,])
func_4927 = relay.Function([], output)
mod['func_4927'] = func_4927
mod = relay.transform.InferType()(mod)
mutated_mod['func_4927'] = func_4927
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4927_call = mutated_mod.get_global_var('func_4927')
call_4928 = func_4927_call()
output = call_4928
func_4929 = relay.Function([], output)
mutated_mod['func_4929'] = func_4929
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3267_call = mod.get_global_var('func_3267')
func_3268_call = mutated_mod.get_global_var('func_3268')
call_4954 = func_3267_call()
call_4955 = func_3267_call()
func_2307_call = mod.get_global_var('func_2307')
func_2309_call = mutated_mod.get_global_var('func_2309')
call_4956 = relay.TupleGetItem(func_2307_call(), 0)
call_4957 = relay.TupleGetItem(func_2309_call(), 0)
var_4960 = relay.var("var_4960", dtype = "float64", shape = (2, 9, 8))#candidate|4960|(2, 9, 8)|var|float64
bop_4961 = relay.right_shift(call_4954.astype('uint16'), var_4960.astype('uint16')) # shape=(2, 9, 8)
bop_4964 = relay.right_shift(call_4955.astype('uint16'), var_4960.astype('uint16')) # shape=(2, 9, 8)
func_1866_call = mod.get_global_var('func_1866')
func_1870_call = mutated_mod.get_global_var('func_1870')
var_4985 = relay.var("var_4985", dtype = "float64", shape = (44,))#candidate|4985|(44,)|var|float64
call_4984 = relay.TupleGetItem(func_1866_call(relay.reshape(var_4985.astype('float64'), [2, 2, 11]), relay.reshape(var_4985.astype('float64'), [2, 2, 11]), ), 0)
call_4986 = relay.TupleGetItem(func_1870_call(relay.reshape(var_4985.astype('float64'), [2, 2, 11]), relay.reshape(var_4985.astype('float64'), [2, 2, 11]), ), 0)
output = relay.Tuple([call_4956,bop_4961,call_4984,var_4985,])
output2 = relay.Tuple([call_4957,bop_4964,call_4986,var_4985,])
func_4989 = relay.Function([var_4960,var_4985,], output)
mod['func_4989'] = func_4989
mod = relay.transform.InferType()(mod)
mutated_mod['func_4989'] = func_4989
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4989_call = mutated_mod.get_global_var('func_4989')
var_4991 = relay.var("var_4991", dtype = "float64", shape = (2, 9, 8))#candidate|4991|(2, 9, 8)|var|float64
var_4992 = relay.var("var_4992", dtype = "float64", shape = (44,))#candidate|4992|(44,)|var|float64
call_4990 = func_4989_call(var_4991,var_4992,)
output = call_4990
func_4993 = relay.Function([var_4991,var_4992,], output)
mutated_mod['func_4993'] = func_4993
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3896_call = mod.get_global_var('func_3896')
func_3898_call = mutated_mod.get_global_var('func_3898')
call_5071 = relay.TupleGetItem(func_3896_call(), 0)
call_5072 = relay.TupleGetItem(func_3898_call(), 0)
var_5075 = relay.var("var_5075", dtype = "float64", shape = (2, 13, 8))#candidate|5075|(2, 13, 8)|var|float64
bop_5076 = relay.equal(call_5071.astype('bool'), var_5075.astype('bool')) # shape=(2, 13, 8)
bop_5079 = relay.equal(call_5072.astype('bool'), var_5075.astype('bool')) # shape=(2, 13, 8)
bop_5083 = relay.bitwise_and(bop_5076.astype('int64'), relay.reshape(var_5075.astype('int64'), relay.shape_of(bop_5076))) # shape=(2, 13, 8)
bop_5086 = relay.bitwise_and(bop_5079.astype('int64'), relay.reshape(var_5075.astype('int64'), relay.shape_of(bop_5079))) # shape=(2, 13, 8)
func_4927_call = mod.get_global_var('func_4927')
func_4929_call = mutated_mod.get_global_var('func_4929')
call_5087 = relay.TupleGetItem(func_4927_call(), 0)
call_5088 = relay.TupleGetItem(func_4929_call(), 0)
func_4865_call = mod.get_global_var('func_4865')
func_4868_call = mutated_mod.get_global_var('func_4868')
var_5095 = relay.var("var_5095", dtype = "float64", shape = (448,))#candidate|5095|(448,)|var|float64
call_5094 = relay.TupleGetItem(func_4865_call(relay.reshape(var_5095.astype('float64'), [4, 16, 7])), 1)
call_5096 = relay.TupleGetItem(func_4868_call(relay.reshape(var_5095.astype('float64'), [4, 16, 7])), 1)
func_2412_call = mod.get_global_var('func_2412')
func_2416_call = mutated_mod.get_global_var('func_2416')
var_5098 = relay.var("var_5098", dtype = "float32", shape = (480,))#candidate|5098|(480,)|var|float32
call_5097 = relay.TupleGetItem(func_2412_call(relay.reshape(var_5098.astype('float32'), [2, 16, 15]), relay.reshape(var_5098.astype('float32'), [2, 16, 15]), ), 0)
call_5099 = relay.TupleGetItem(func_2416_call(relay.reshape(var_5098.astype('float32'), [2, 16, 15]), relay.reshape(var_5098.astype('float32'), [2, 16, 15]), ), 0)
func_2945_call = mod.get_global_var('func_2945')
func_2949_call = mutated_mod.get_global_var('func_2949')
var_5110 = relay.var("var_5110", dtype = "float32", shape = (176,))#candidate|5110|(176,)|var|float32
var_5111 = relay.var("var_5111", dtype = "uint8", shape = (11, 25))#candidate|5111|(11, 25)|var|uint8
const_5112 = relay.const([1.852518,1.635206,-6.247913,-4.803147,-2.801068,0.242705,-5.146762,9.118342,0.995343,-7.862712,-4.368983,-9.298005,2.857022,5.405505,4.454242,0.712109,-7.540364,-7.103475,3.369853,2.250429,1.056454,-6.692949,3.071911,-3.195811,5.784318,3.811464,1.491302,-3.021964,-5.636080,6.894982,-4.401719,-3.267804,9.080935,6.887174,9.377671,-4.880467,9.749165,-7.851299,-4.115280,8.212390,9.349303,4.604347,0.847447,-5.866880,-9.005433,4.353137,-1.785712,5.546029,-1.302938,-9.171408,8.179850,-9.104706,7.851075,7.452077,5.147418,0.651546,-1.866150,0.064168,0.733013,1.751860,5.470836,-6.226616,7.013191,3.064549,-9.198811,4.149880,-8.953038,-9.570802,9.328955,-9.565243,-1.410103,7.982083,-2.054094,-4.542825,-9.843048,9.751752,-0.827413,-1.618857,1.078333,9.844313,9.438258,-1.426930,4.746208,-5.205078,-6.055011,2.416601,-1.126390,7.395121,-6.541476,-8.704400,-0.345103,-9.346471,8.745932,-2.656856,5.423755,-1.047326,-3.386071,-7.014154,9.244592,-3.276384,8.396893,7.298983,3.941329,3.078898,-7.227938,-0.798405,2.173143,-3.578820,8.681612,-8.783956,-0.173048,-3.132352,9.296883,-1.589523,3.837090,-2.920572,4.550562,-7.573104,6.538107,-5.888359,-2.439710,-7.556362,6.124394,-0.089311,9.138183,9.798467,-6.295093,-4.695840,3.197682,-1.958499,-4.984804,8.600366,-2.341564,-4.897248,1.018750,-2.864003,2.545510,-1.660064,0.427815,-6.861303,4.648567,-2.288380,4.638221,3.992813,-1.732398,7.787186,-5.992784,-1.774450,-6.339027,-1.099072,9.468234,3.161536,1.460892,7.259367,1.744879,6.870098,-8.039976,-8.424650,1.169659,-9.801623,1.564422,-8.493972,-9.996754,8.868701,7.088521,2.535277,-2.929251,9.492658,-8.227033,-6.872182,-7.208309,-4.818547,7.761564,-3.071954,-2.823855,-3.150018,-1.994578,4.505515,5.242410,-0.558876,2.622662,6.178962,-2.028433,6.513651,-9.618179,-6.618342,-8.271912,9.621584,6.611628,-5.515497,-2.342477,-6.843385,7.969821,3.089277,-3.204470,2.672506,1.970849,2.820384,6.669918,-6.313781,-9.279207,1.855122,3.289381,-2.308455,-7.402614,-5.152301,-8.424977,-8.769711,2.814893,-0.325867,0.340063,1.181677,4.697670,-4.812366,0.756547,-6.848053,-5.184806,-8.350508,-8.592672,-9.466699,0.999244,5.623814,2.534602,3.205601,7.315121,-8.881278,7.159650,-9.067464,-6.431685,-4.703958,0.776920,7.667803,-2.537602,-3.768438,6.117824,7.054550,3.711073,-3.955752,-5.659659,8.719091,7.036509,-1.556924,3.354851,3.799384,-3.955885,-7.888305,-1.952844,7.724643,4.617910,6.472250,-9.817387,-5.259177,8.811684,4.590625,-0.842775,-0.076697,-5.221249,6.046442,1.032676,-9.711822,-2.340789,1.610011,-6.046782,6.125015,-6.511284,-7.890413,1.243707,7.454224,6.723478,4.600455,5.979744,-2.897800,-4.135852,-1.319424,-0.276158,4.116344,2.477489,-8.490974,1.584227,0.032541,-0.875695,0.182279,-6.899305,1.424269,0.726148,-8.286402,-9.592753,-6.046865,-9.336567,-6.144489,5.840677,9.870113,-5.597891,6.909722,3.574459,-5.254189,-9.305412,6.941091,-0.107146,6.886674,4.257002,-1.553782,-8.312593,3.573557,7.224736,4.672490,2.937572,4.776240,-9.988130,-6.849171,-3.567552,-2.217185,-7.173616,8.448538,-4.157179,-9.649359,-8.960057,8.037333,0.667833,6.081033,-1.407746,-3.228274,4.235275,4.713735,-9.778922,0.711682,-4.455395,7.976685,-2.944733,8.455462,2.221426,-2.112125,8.848559,-6.364133,-9.228438,3.481368,7.392033,1.712906,-8.932491,-6.017553,-9.881922,9.548755,8.707946,8.860931,2.077276,-9.342246,-9.817205,2.762911,-9.260854,-4.299256,9.569575,4.890279,8.341394,-1.156578,-2.978337,-2.210875,-4.823169,3.540011,1.611052,4.067943,-0.502344,3.307392,3.799774,-4.474845,4.609070,-3.184755,-8.096417,9.445675,-2.498558,0.893333,-8.478550,3.862921,2.719166,0.265690,4.538514,-1.564619,-6.230671,-2.340960,-0.461585,-6.110573,-5.001182,-4.757225,-2.905755,-8.883638,8.122532,3.423596,-7.749469,9.557087,-9.925898,-5.363245,9.709969,7.993399,-7.500025,5.760412,-5.701143,-7.476851,0.974645,1.541494,-9.415499,-2.534193,-9.976864,-7.129197,8.334739,-9.953568,-7.313831,9.637993,4.583082,7.041220,7.303961,-1.428765,-5.553882,-7.067088,-4.773242,-3.431888,7.064093,-3.988213,-0.886620,-8.143106,-2.933161,3.157558,5.359846,9.637548,3.552014,8.716816,9.139137,-9.132595,-2.469598,1.632486,7.682107,-3.451515,6.188665,-9.470141,2.532020,3.133939,0.988946,-3.091456,4.953457,-1.425612,-3.329841,4.323422,6.039316,-6.611515,-5.011477,-3.085440,8.502568,1.765480,-5.384385,-5.137964,-5.183548,1.841136,2.743798,9.157192,8.136255,5.558731,9.894481,-3.168098,8.460926,-2.963994,-7.532938,8.440850,0.665377,-3.273474,-1.731541,9.497372,-7.120466,-2.390228,-5.583479,2.044129,0.035641,-4.480372,1.851647,-8.494805,4.635419,0.431382,7.561149,4.041742,0.114457,-1.126770,-3.873174,-2.426771,9.007837,-3.198730,-4.470869,7.789440,9.337676,-0.810294,-2.346366,8.576378,-1.377905,-9.668070,8.117134,-0.169946,8.339568,-3.009617,0.503090,5.409190,9.992428,-7.674355,0.581283,-4.566745], dtype = "float32")#candidate|5112|(500,)|const|float32
call_5109 = relay.TupleGetItem(func_2945_call(relay.reshape(var_5110.astype('float32'), [2, 11, 8]), relay.reshape(var_5111.astype('uint8'), [275,]), relay.reshape(const_5112.astype('float32'), [500,]), ), 4)
call_5113 = relay.TupleGetItem(func_2949_call(relay.reshape(var_5110.astype('float32'), [2, 11, 8]), relay.reshape(var_5111.astype('uint8'), [275,]), relay.reshape(const_5112.astype('float32'), [500,]), ), 4)
output = relay.Tuple([bop_5083,call_5087,call_5094,var_5095,call_5097,var_5098,call_5109,var_5110,var_5111,const_5112,])
output2 = relay.Tuple([bop_5086,call_5088,call_5096,var_5095,call_5099,var_5098,call_5113,var_5110,var_5111,const_5112,])
func_5121 = relay.Function([var_5075,var_5095,var_5098,var_5110,var_5111,], output)
mod['func_5121'] = func_5121
mod = relay.transform.InferType()(mod)
var_5122 = relay.var("var_5122", dtype = "float64", shape = (2, 13, 8))#candidate|5122|(2, 13, 8)|var|float64
var_5123 = relay.var("var_5123", dtype = "float64", shape = (448,))#candidate|5123|(448,)|var|float64
var_5124 = relay.var("var_5124", dtype = "float32", shape = (480,))#candidate|5124|(480,)|var|float32
var_5125 = relay.var("var_5125", dtype = "float32", shape = (176,))#candidate|5125|(176,)|var|float32
var_5126 = relay.var("var_5126", dtype = "uint8", shape = (11, 25))#candidate|5126|(11, 25)|var|uint8
output = func_5121(var_5122,var_5123,var_5124,var_5125,var_5126,)
func_5127 = relay.Function([var_5122,var_5123,var_5124,var_5125,var_5126,], output)
mutated_mod['func_5127'] = func_5127
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4246_call = mod.get_global_var('func_4246')
func_4247_call = mutated_mod.get_global_var('func_4247')
call_5150 = relay.TupleGetItem(func_4246_call(), 0)
call_5151 = relay.TupleGetItem(func_4247_call(), 0)
func_4479_call = mod.get_global_var('func_4479')
func_4482_call = mutated_mod.get_global_var('func_4482')
var_5157 = relay.var("var_5157", dtype = "float32", shape = (500,))#candidate|5157|(500,)|var|float32
call_5156 = relay.TupleGetItem(func_4479_call(relay.reshape(var_5157.astype('float32'), [250, 2])), 1)
call_5158 = relay.TupleGetItem(func_4482_call(relay.reshape(var_5157.astype('float32'), [250, 2])), 1)
func_4246_call = mod.get_global_var('func_4246')
func_4247_call = mutated_mod.get_global_var('func_4247')
call_5162 = relay.TupleGetItem(func_4246_call(), 0)
call_5163 = relay.TupleGetItem(func_4247_call(), 0)
output = relay.Tuple([call_5150,call_5156,var_5157,call_5162,])
output2 = relay.Tuple([call_5151,call_5158,var_5157,call_5163,])
func_5166 = relay.Function([var_5157,], output)
mod['func_5166'] = func_5166
mod = relay.transform.InferType()(mod)
mutated_mod['func_5166'] = func_5166
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5167 = relay.var("var_5167", dtype = "float32", shape = (500,))#candidate|5167|(500,)|var|float32
func_5166_call = mutated_mod.get_global_var('func_5166')
call_5168 = func_5166_call(var_5167)
output = call_5168
func_5169 = relay.Function([var_5167], output)
mutated_mod['func_5169'] = func_5169
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4689_call = mod.get_global_var('func_4689')
func_4691_call = mutated_mod.get_global_var('func_4691')
call_5190 = func_4689_call()
call_5191 = func_4689_call()
output = call_5190
output2 = call_5191
func_5213 = relay.Function([], output)
mod['func_5213'] = func_5213
mod = relay.transform.InferType()(mod)
output = func_5213()
func_5214 = relay.Function([], output)
mutated_mod['func_5214'] = func_5214
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3175_call = mod.get_global_var('func_3175')
func_3177_call = mutated_mod.get_global_var('func_3177')
call_5217 = relay.TupleGetItem(func_3175_call(), 1)
call_5218 = relay.TupleGetItem(func_3177_call(), 1)
func_3896_call = mod.get_global_var('func_3896')
func_3898_call = mutated_mod.get_global_var('func_3898')
call_5221 = relay.TupleGetItem(func_3896_call(), 0)
call_5222 = relay.TupleGetItem(func_3898_call(), 0)
output = relay.Tuple([call_5217,call_5221,])
output2 = relay.Tuple([call_5218,call_5222,])
func_5227 = relay.Function([], output)
mod['func_5227'] = func_5227
mod = relay.transform.InferType()(mod)
output = func_5227()
func_5228 = relay.Function([], output)
mutated_mod['func_5228'] = func_5228
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4689_call = mod.get_global_var('func_4689')
func_4691_call = mutated_mod.get_global_var('func_4691')
call_5255 = func_4689_call()
call_5256 = func_4689_call()
var_5268 = relay.var("var_5268", dtype = "float32", shape = (2, 11, 8))#candidate|5268|(2, 11, 8)|var|float32
bop_5269 = relay.maximum(call_5255.astype('int64'), var_5268.astype('int64')) # shape=(2, 11, 8)
bop_5272 = relay.maximum(call_5256.astype('int64'), var_5268.astype('int64')) # shape=(2, 11, 8)
output = relay.Tuple([bop_5269,])
output2 = relay.Tuple([bop_5272,])
func_5279 = relay.Function([var_5268,], output)
mod['func_5279'] = func_5279
mod = relay.transform.InferType()(mod)
mutated_mod['func_5279'] = func_5279
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5280 = relay.var("var_5280", dtype = "float32", shape = (2, 11, 8))#candidate|5280|(2, 11, 8)|var|float32
func_5279_call = mutated_mod.get_global_var('func_5279')
call_5281 = func_5279_call(var_5280)
output = call_5281
func_5282 = relay.Function([var_5280], output)
mutated_mod['func_5282'] = func_5282
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5301 = relay.var("var_5301", dtype = "int8", shape = (13, 13, 16))#candidate|5301|(13, 13, 16)|var|int8
var_5302 = relay.var("var_5302", dtype = "int8", shape = (13, 13, 16))#candidate|5302|(13, 13, 16)|var|int8
bop_5303 = relay.not_equal(var_5301.astype('bool'), relay.reshape(var_5302.astype('bool'), relay.shape_of(var_5301))) # shape=(13, 13, 16)
output = bop_5303
output2 = bop_5303
func_5309 = relay.Function([var_5301,var_5302,], output)
mod['func_5309'] = func_5309
mod = relay.transform.InferType()(mod)
mutated_mod['func_5309'] = func_5309
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5309_call = mutated_mod.get_global_var('func_5309')
var_5311 = relay.var("var_5311", dtype = "int8", shape = (13, 13, 16))#candidate|5311|(13, 13, 16)|var|int8
var_5312 = relay.var("var_5312", dtype = "int8", shape = (13, 13, 16))#candidate|5312|(13, 13, 16)|var|int8
call_5310 = func_5309_call(var_5311,var_5312,)
output = call_5310
func_5313 = relay.Function([var_5311,var_5312,], output)
mutated_mod['func_5313'] = func_5313
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5213_call = mod.get_global_var('func_5213')
func_5214_call = mutated_mod.get_global_var('func_5214')
call_5317 = func_5213_call()
call_5318 = func_5213_call()
var_5344 = relay.var("var_5344", dtype = "float32", shape = (2, 1, 8))#candidate|5344|(2, 1, 8)|var|float32
bop_5345 = relay.right_shift(call_5317.astype('uint16'), relay.reshape(var_5344.astype('uint16'), relay.shape_of(call_5317))) # shape=(2, 1, 8)
bop_5348 = relay.right_shift(call_5318.astype('uint16'), relay.reshape(var_5344.astype('uint16'), relay.shape_of(call_5318))) # shape=(2, 1, 8)
func_1341_call = mod.get_global_var('func_1341')
func_1344_call = mutated_mod.get_global_var('func_1344')
var_5359 = relay.var("var_5359", dtype = "int32", shape = (252,))#candidate|5359|(252,)|var|int32
const_5360 = relay.const([[-0.924576],[6.156464],[-5.567115],[-1.360367],[-0.749128],[8.503960],[-1.706963],[-8.698367],[0.923635],[-4.967192],[-7.428037],[0.130022],[-9.774647],[1.534397],[1.931602],[8.035957],[5.510727],[-1.026260],[-4.817502],[1.437036],[9.450927],[-7.735893],[5.395523],[-9.283095],[1.087781],[4.792613],[1.176574],[1.294747],[3.475770],[9.320478],[-8.426450],[-8.348854],[3.598323],[2.626718],[-8.875039],[-4.406397],[-0.151570],[1.749723],[8.245574],[-2.795655],[7.500727],[-4.625086],[-6.217166],[-9.723237],[-8.006639],[-1.069314],[7.086708],[3.275601],[1.114330],[-0.409178],[8.941663],[-8.617254],[-4.521926],[-1.112232],[1.509516],[-3.298588],[-9.231188],[-1.079643],[-5.827514],[3.746939],[-2.184362],[-2.292268],[-2.050748],[-6.392542],[-0.275772],[6.703669],[0.009612],[7.006050],[-0.313033],[4.116276],[-5.770510],[-4.624355],[-2.183799],[-2.471400],[0.025593],[1.986271],[4.242538],[5.858263],[9.556796],[-7.931748],[8.282987],[-6.175565],[9.998275],[-1.026545],[9.283835],[3.119217],[9.989815],[-3.746521],[-1.691835],[-8.281597],[-8.104117],[0.270528],[2.382384],[-4.750487],[-8.200411],[0.122959],[-4.307089],[-7.024016],[5.328131],[8.632047],[-4.512620],[6.891775],[-3.119084],[9.510068],[-5.838659],[3.324679],[-7.067663],[-8.602870],[4.819710],[-6.245454],[4.168323],[4.295901],[4.299870],[9.610455],[-6.392820],[6.845612],[-8.134801],[-0.123637],[1.037836],[3.258592],[-5.372223],[-0.406741],[-7.423755],[-6.053607],[3.238906],[9.332896],[-4.308993],[5.163284],[2.934769],[6.163716],[3.462107],[-5.821377],[0.912531],[9.820687],[8.628469],[-7.268939],[7.608220],[-7.133678],[3.005329],[1.260171],[7.957586],[-8.068116],[-0.642395],[-2.670280],[-5.860624],[1.979602],[-0.215587],[3.463796],[5.770847],[-6.241338],[-1.897631],[-6.677582],[-0.276980],[5.070169],[3.573577],[-8.145378],[3.707921],[1.373472],[-5.016393],[9.449004],[5.513889],[6.453757],[4.904084],[9.925585],[4.083640],[5.537921],[-8.348147],[9.764845],[-8.548236],[-6.566814],[1.235311],[-7.268873],[7.813057],[-5.996563],[7.436640],[7.596441],[7.323370],[5.145996],[9.161418],[8.217810],[-5.783178],[-3.531288],[-1.050623],[2.269634],[-5.025647],[-3.888245],[3.465893],[6.028091],[-2.281061],[-7.507787],[4.171513],[-7.902982],[-8.400767],[0.609684],[-2.781265],[-9.406964],[4.642719],[5.931661],[-1.470902],[-8.740344],[5.266541],[0.118677],[-3.016092],[0.311268],[-9.270220],[-2.539055],[9.985800],[-5.392648],[-5.883595],[-5.708167],[-9.037243],[-9.727450],[8.360365],[0.035176],[-5.897690],[2.204712],[5.627050],[-3.829712],[9.610872],[-5.024454],[-1.234955],[3.370225],[-5.781072],[8.562031],[-9.124030],[4.295899],[7.527814],[-8.366351],[-1.411302],[-5.715575],[-6.696213],[-7.781274],[-1.968387],[6.883819],[-2.262934],[-7.203156],[-1.191224],[9.329701],[1.270693],[-1.231942],[-3.327614],[0.466614],[1.657075],[-5.073384],[5.707766],[-9.933118],[-3.517321],[8.492478],[-6.003912],[-2.904200],[6.534269],[0.929903],[1.385112],[-6.165672],[1.845714],[-2.762382],[-0.940485],[0.439676],[4.039021],[1.705313],[0.765368],[-3.900164],[-7.645513],[-9.709158],[-9.730599],[-8.759141],[5.368896],[-7.521380],[-5.154172],[-1.265613],[0.658042],[9.714520],[-5.363617],[6.797318],[-1.944742],[-2.383660],[-5.603342],[-5.931409],[4.029740],[9.630087],[0.327463],[5.648982],[0.961371],[0.017044],[-7.564086],[-0.205115],[-4.132226],[7.252260],[-2.274722],[7.559211],[-7.477104],[-0.729438],[-8.096932],[3.435058],[-0.139296],[-2.556139],[-4.582673],[-0.427737],[2.021393],[9.633248],[5.933433],[3.493658],[5.559505],[-4.370599],[0.797119],[0.793857],[-1.160428],[-9.546781],[-5.728350],[-8.701440],[2.487460],[-5.717645],[-0.679020],[1.380535],[3.627702],[6.393381],[-0.319810],[-9.266832],[6.853600],[-7.298470],[-2.538536],[-3.464147],[6.246219],[-0.092282],[2.648338],[-1.119280],[4.980999],[-1.623135],[-1.240137],[4.152906],[1.107342],[-9.422402],[2.921305],[5.783504],[-3.191800],[8.160283],[4.465157],[2.249581],[-8.406457],[-6.079877],[-9.465068],[-3.094033],[-8.621740],[5.997919],[9.977000],[-5.292050],[7.063001],[-2.673701],[7.424878],[1.559377],[7.777354],[3.822370],[4.658431],[-2.705149],[-3.616442],[8.865223],[4.342068],[-6.929323],[-4.608606],[-2.490375],[-4.799769],[-3.815784],[-9.953615],[-5.669243],[1.852773],[5.000538],[-8.171163],[8.372485],[8.682092],[2.091061],[1.007321],[-2.460452],[0.430929],[-4.795323],[-0.903643],[1.840930],[9.618550],[-3.862633],[-3.127817],[0.790894],[-8.699709],[4.531786],[1.122852],[-0.383095],[-5.029484],[-0.659343],[-1.623258],[-4.701107],[9.123873],[-2.512857],[-5.571328],[-2.729304],[9.645488],[4.491415],[8.825412],[7.430215],[7.273659],[-7.328241],[-9.567166],[8.179978],[9.529846],[-3.522441],[-4.629490],[1.415240],[6.872021],[7.568489],[5.432123],[2.668208],[-0.522872],[-6.607274],[8.566587],[7.462669],[-9.126303],[-6.055498],[9.473567],[0.377952],[1.914470],[-1.034749],[4.527449],[-0.584488],[5.380845],[-3.524480],[5.964557],[-6.110557],[-7.971544],[-8.452105],[-7.326560],[-5.504827],[2.741447],[8.252047],[-9.513099],[8.010701],[-2.544827],[7.807409],[5.156735],[-8.123512],[6.662855],[9.293210],[-4.580489],[-6.914654],[4.533008],[0.971345],[-3.087095],[-4.053820],[-6.689782],[-5.544365],[6.891517],[-0.922986],[-5.140074],[2.349973],[4.151858],[-7.055819],[-0.388537],[-1.206265],[0.410370],[0.696112],[3.871663],[8.720131],[-4.381967],[9.698334],[2.393208],[1.643633],[-7.737849],[6.560143],[9.161357],[-0.097454],[-3.400014],[4.902539],[3.778187],[-8.134067],[-5.603546],[2.615515],[-4.126633],[3.423618],[-5.456779],[5.574379],[6.281644],[-8.647130],[-6.520315],[-2.914377],[-9.635651],[8.536088],[5.795948],[6.859264],[-8.315123],[-9.619389],[0.401466],[-3.259122],[-6.383293],[-3.871130],[-8.610940],[-2.099929],[-6.177550],[2.979791],[-6.811591],[-0.158870],[2.745506],[-8.747269],[-2.729556],[3.859114],[9.982412],[6.570111],[5.699934],[-4.553547],[-4.851808],[-8.089898],[-6.426001],[-4.228389],[-7.533586],[3.425872],[1.508293],[5.599456],[5.175061],[1.721801],[-0.131087],[-6.907622],[-6.252229],[-3.587769],[5.433060],[3.852817],[-1.452019],[0.273081],[9.169844],[4.580879],[1.083461],[-2.896037],[4.296173],[5.235032],[1.572890],[-6.911625],[2.389417],[0.795109],[0.240884],[0.464374],[-9.433059],[-6.944036],[2.266129],[7.337717],[9.047285],[-1.514818],[-4.226230],[6.855692],[-1.632318],[-1.909012],[8.310960],[6.857073],[-6.907929],[4.292534],[1.710833],[-2.400632],[4.544970],[-7.526231],[-8.453167],[0.202872],[-8.678298],[3.719684],[6.052532],[-6.463341],[9.709615],[8.664460],[-7.851732],[-2.350042],[-7.676343],[-2.309338],[-4.088737],[2.293915],[3.695620],[-3.952832],[-4.835977],[6.141273],[8.193977],[1.606164],[5.367628],[4.771756],[-4.116648],[6.629105],[2.676834],[6.696030],[9.441489],[8.168539],[7.657085],[-6.107791],[-8.394348],[-9.312382],[-8.191164],[-0.156613],[-9.651167],[-6.328336],[0.795537],[1.351885],[7.773489],[-6.825067],[-1.042120],[-0.649339],[1.326448],[1.333226],[-3.269189],[8.787621],[3.450981],[9.353662],[4.287270],[9.167175],[5.558986],[1.537212],[9.762936],[0.981839],[-2.859898],[-2.073154],[3.186200],[-9.986213],[-1.060813],[5.806871],[6.991220],[-7.836562],[5.319640],[8.008334],[4.814954],[-4.523345],[-8.567411],[7.085131],[-0.409697],[-6.505304],[0.786766],[9.852926],[6.504197],[4.488285],[-6.129811],[0.836941],[-0.899991],[-7.296101],[7.844531],[-1.872769],[-4.902710],[-2.160004],[2.114073],[7.620629],[-6.957557],[-1.327408],[-1.752103],[-2.987513],[4.129986],[7.208713],[7.251701],[-0.024169],[-3.479421],[3.930190],[-7.223446],[-7.738305],[-6.430287],[4.939825],[6.956963],[-6.076000],[3.284852],[9.280957],[-6.478086],[6.950609],[9.444698],[7.008857],[7.862552],[-4.594680],[-0.886530],[-2.249808],[-6.378582],[-8.832248],[6.720696],[-8.556530],[-0.113698],[-8.161971],[7.790172],[9.525750],[1.465127],[0.310060],[0.243865],[2.801194],[-6.533540],[5.573276],[8.917866],[3.135028],[-7.302094],[5.296181],[-0.899412],[-8.719205],[-5.374619],[-4.254302],[-9.182546],[2.432248],[-6.719403],[3.428107],[-2.173978],[0.549995],[-8.084228],[0.262620],[-5.673482],[3.408315],[-4.258025],[-5.147916],[-5.233521],[4.777088],[8.807881],[-7.088983],[9.782036],[8.850147],[8.457916],[-6.309269],[-2.179373],[-5.838296],[-8.190118],[-2.100216],[5.787957],[8.670147],[-6.584592],[-0.660383],[8.480170],[1.156782],[8.528152],[-3.811395],[-8.749330],[-4.630000],[-7.894759],[1.051884],[-6.923777],[-6.296878],[1.125430],[5.391833],[-1.901211],[7.243893],[-6.989136],[-7.715275],[3.426560],[-2.402498],[1.299914],[-2.149065],[7.336928],[4.923269],[0.183079],[-0.238435],[0.350193],[-2.400300],[0.367381],[1.424568],[-4.859571],[1.315439],[-4.337935],[-6.547056],[4.763687],[-1.185716],[-3.650132],[-5.023843],[2.261189],[7.180760],[-5.910213],[4.502769],[-8.602017],[5.426954],[3.896968],[-7.584360],[6.285702],[1.080851],[6.603228],[5.902817],[-8.033710],[7.044991],[-0.136514],[-7.329900],[-2.606341],[-7.685681],[1.025266],[-8.321527],[0.077856],[-3.667732],[-7.975284],[2.384915],[-1.670232],[6.972286],[-0.685122],[-0.060018],[-0.956394],[0.181921],[-7.830657],[-6.916110],[-2.480877],[4.941251],[-7.662214],[5.046504],[6.690110],[3.180988],[-7.446147],[5.135722],[3.313672],[-9.522216],[-3.739372],[-3.188829],[6.107271],[8.951669],[-2.726604],[-6.936154],[6.226403],[-9.308551],[4.408576],[8.870417],[7.258774],[-7.845922],[9.616165],[-3.922146],[-7.094121],[2.584524],[-9.385412],[5.255224],[4.351041],[4.304499],[-3.477893],[-0.682832],[3.740246],[-3.807436],[2.171313],[-6.937266],[-8.239771],[-0.813524],[-2.837928],[-7.823590],[-8.729043],[7.631006],[6.719573],[-0.565721],[-8.346948],[-3.586403],[3.793680],[-4.275838],[-9.198716],[3.000637],[-8.645958],[-8.690629],[-0.532498],[2.759564],[-7.488199],[6.523083],[1.163486],[1.830121],[9.303182],[3.884219],[6.240738],[-1.359510],[3.813545],[2.094547],[8.443926],[3.153850],[-7.152251],[-2.085586],[-7.099919],[-2.705615],[8.941039],[8.321841],[-5.220963],[-8.438388],[-8.122933],[8.852387],[8.674494],[-1.239404],[-9.848239],[-7.072964],[-9.912933],[-7.734817],[-5.901342],[1.617005],[-1.223950],[9.349278],[6.287129],[-3.881179],[7.305189],[3.140495],[-9.002865],[3.586389],[0.467465],[-3.093121],[5.982996],[2.938572],[-2.325166],[6.196131],[4.770226],[-5.798540],[-5.667570],[0.226375],[-2.013310],[8.490780],[-4.328475],[-7.984338],[-7.647857],[0.005288],[2.624109],[5.392410],[-9.480782],[4.808254],[-1.293688],[2.512327],[2.251182],[5.770372],[8.895778],[-3.560415],[-5.594169],[5.595105],[-9.789075],[-6.706321],[7.770395],[-1.693140],[3.177381],[-7.605527],[8.221369],[1.417555],[-0.552917],[1.399119],[-6.831427],[9.870865],[9.699409],[8.984792],[4.056062],[0.309669],[-5.473009],[-8.755687],[1.862396],[3.838181],[2.809171],[-1.383307],[1.473190],[-1.229413],[1.266458],[0.535401],[8.115777],[3.818771],[-1.506539],[-4.534146],[-7.182362],[-8.076061],[5.826372],[-3.639974],[6.567106],[-7.592953],[4.726777],[9.945168],[-8.577023],[-7.662142],[8.236335],[4.224188],[-5.610461],[-6.208683],[5.092639],[5.352883],[-5.021516],[2.052832],[-4.000086],[-7.555259],[0.200507],[-3.193942],[6.323328],[8.742643],[-8.646660],[9.739547],[5.180526],[-7.500932],[-9.033914],[7.314151],[3.435912],[3.558499],[-3.412785],[-0.931657],[-2.419186],[-1.107546],[2.901131],[0.894611],[3.728463],[-7.263610],[-3.282534],[5.634791],[-0.464418],[-7.420281],[-0.334009],[-8.849382],[-0.242528],[8.346926],[-7.309882],[7.644451],[-8.140842],[-6.895661],[9.414981],[4.280216],[-4.642935],[-9.496565],[5.111679],[1.477880],[2.979211],[-9.557256],[5.220302],[3.535192],[-5.398584],[-0.758896],[-9.687816],[-0.107096],[0.893796],[-0.341981],[-5.848271],[6.264695],[0.384543],[3.645016],[-2.488495],[-8.461213],[-2.444566],[7.243402],[-7.171915],[4.872110],[-7.813571],[0.736983],[-6.803222],[3.920031],[6.095889],[-4.775575],[8.973227],[-8.409688],[1.396642],[-7.247390],[-0.558371],[9.864229],[8.159017],[-0.777301],[1.134466],[7.518965],[8.164026],[5.667442],[-8.744522],[-1.517358],[-6.919652],[5.930771],[-5.419374],[3.525666],[8.957054],[8.980848],[-2.369329],[4.409397],[-2.085451],[7.731906],[0.480526],[3.212128],[-8.970474],[-5.950570],[4.551575],[-9.654492],[6.553397],[-5.588171],[3.817434],[6.555386],[8.576198],[8.356254],[1.107791],[0.154906],[-6.006799],[-3.418730],[4.081002],[8.797983],[-8.632071],[-2.058194],[-3.307030],[9.284048],[-3.560975],[4.099716],[8.691608],[6.193797],[-9.023204],[2.566080],[7.770025],[3.542204],[9.444045],[1.579658],[5.634635],[-0.661875],[3.137716],[7.160437],[0.343903],[9.965721],[-7.767069],[-6.182999],[-1.575590],[-8.879529],[-5.446366],[-0.433856],[2.060645],[8.034280],[1.297244],[5.264833],[0.012376],[-6.769048],[2.588337],[-0.886239],[1.385509],[-6.556237],[8.714123],[9.404602],[-5.791927],[-7.244186],[4.940981],[-9.215349],[-8.407854],[-6.419503],[3.652081],[-8.047520],[0.646299],[0.662725],[-6.777526],[-3.437045],[1.271509],[-2.821640],[9.611536],[-7.041149],[7.021291],[-4.702186],[-8.267075],[2.018456],[-2.528884],[-4.991178],[-4.360123],[9.983227],[-3.203784],[-0.981561],[-2.161369],[-2.926430],[2.915210],[-3.785773],[-2.626245],[7.512574],[0.443702],[2.497988],[-2.354319],[-2.945911],[-0.072592],[-9.128775],[7.958786],[-1.006459],[-5.220290],[8.036914],[9.380494],[2.153482],[-4.267732],[3.861371],[-5.973730],[-5.416676],[-1.266667],[2.286980],[8.405027],[-5.256649],[0.318285],[-0.532178],[-4.948941],[-9.123140],[8.132884],[5.803168],[4.463109],[4.217570],[4.407807],[-4.833390],[0.254559],[5.536482],[-1.820966],[2.524240],[5.589775],[0.872467],[-0.730173],[1.655948],[4.312316],[-4.708857],[7.759135],[6.100970],[-0.746535],[-9.411400],[-7.791866],[7.650915],[-4.035008],[2.091623],[-2.270873],[-6.228560],[-5.640144],[-9.625138],[1.552469],[7.345310],[3.154343],[4.949379],[-0.255933],[1.600241],[4.304587],[-9.463096],[-2.567010],[-5.519216],[-4.308733],[-3.457677],[-1.076905],[-0.866572],[-8.991078],[5.663431],[3.526617],[-1.043345],[-1.149717],[3.534524],[2.319209],[0.170930],[7.358839],[-7.118835],[-1.998933],[-7.864773],[-9.109511],[4.121926],[3.392883],[-0.016334],[-5.324841],[2.483982],[-8.182349],[-4.545059],[3.550255],[1.596560],[-7.068860],[3.332815],[-7.579764],[8.312113],[-6.226077],[-6.793377],[-3.413823],[0.456930],[8.550296],[-8.264423],[-9.167231],[4.425179],[8.346361],[3.610038],[-6.856083],[7.375600],[-1.274854],[-6.329783],[-5.543511],[8.694938],[9.363737],[-9.097612],[7.459174],[8.516012],[8.291774],[-8.878941],[6.832076],[-9.229319],[6.453298],[3.315849],[1.333071],[-7.598422],[8.213161],[-3.568967],[-9.950447],[4.705070],[1.353061],[-3.920299],[1.372268],[-2.900932],[6.018246],[-4.802701],[-6.276910],[1.403559],[3.788247],[5.780502],[-1.624341],[-6.529603],[-6.895564],[1.140765],[-5.396309],[-3.944567],[-0.066916],[-7.194967],[-4.837035],[-8.211988],[4.669056],[-6.378995],[-3.316169],[0.303261],[-7.758777],[-7.156531],[-1.825184],[9.288176],[6.143246],[1.820719],[9.778217],[-3.688016],[-0.128653],[1.232772],[0.810461],[-4.840584],[7.423167],[-7.632991],[1.914315],[6.473766],[7.606081],[-0.502040],[-0.384702],[-1.225135],[-4.243295],[6.394994],[-1.516770],[-6.527297],[-3.888535],[9.196451],[7.317838],[-0.770965],[7.108250],[-3.278855],[-7.137300],[-4.919959],[0.972650],[5.492428],[-1.056884],[-8.434615],[1.320878],[-3.341346],[0.214384],[4.426173],[4.997838],[9.277747],[-9.104556],[7.660394],[-7.233689],[-3.041715],[5.603664],[-2.185457],[6.551112],[-0.185746],[-3.522057],[0.399283],[-1.085582],[3.618749],[-4.621641],[6.699907],[5.620744],[-9.927806],[-4.975795],[6.124994],[-3.929583],[1.917963],[4.272073],[-8.206159],[8.427237],[-2.669438],[5.524678],[6.858990],[-8.495530],[4.543495],[0.216913],[-7.629299],[9.964163],[0.389435],[-1.648867],[2.428827],[-0.371813],[-2.686320],[-6.463991],[0.945003],[1.251714],[5.822701],[4.268673],[-2.335488],[7.861570],[-1.804261],[-9.517438],[-1.214652],[9.555445],[2.209578],[-6.798511],[-8.452417],[1.355705],[-0.718307],[-8.669558],[3.494798],[-9.170777],[-4.122600],[3.665907],[1.178119],[4.598526],[-3.901193],[-6.290460],[4.089605],[-8.643284],[2.401343],[5.245899],[5.908589],[-0.335776],[0.130477],[0.985488],[-7.869208],[3.555642],[5.408519],[3.165012],[-1.807319],[-3.108104],[-7.480481],[2.934528],[3.117643],[-4.533748],[-1.632890],[-0.434069],[-9.323222],[-1.065133],[8.067810],[-7.886230],[3.112086],[8.876519],[-9.731883],[7.172000],[6.252163],[3.102164],[-3.986421],[0.759156],[-8.006763],[-2.301835],[-1.572521],[9.252701],[9.021794],[-7.973473],[3.905415],[-4.217847],[-8.307624],[-7.219121],[-3.826398],[5.452712],[5.215659],[5.087563],[9.100409],[6.681699],[-1.060094],[4.599189],[3.106575],[1.950744],[-5.608113],[6.499653],[-1.917873],[-4.607225],[1.121369],[0.889765],[-3.176155],[0.204033],[-3.363940],[2.115783],[-5.158606],[3.877490],[-1.118613],[4.471153],[0.713480],[-9.562246],[-0.419393],[-1.508261],[6.937565],[5.807933],[4.736274],[-3.104714],[-3.645775],[4.170544],[-9.205977],[-2.782025],[-4.175154],[3.193094],[-2.528075],[-3.966016],[2.441551],[0.924987],[-4.567582],[-5.256973],[-4.621868],[5.953478],[-1.655568],[8.098702],[5.404103],[4.547569],[2.347289],[-2.497062],[-6.990612],[-6.488316],[-8.142252],[-6.392681],[5.467103],[2.335682],[3.996034],[7.491682],[-5.482603],[4.497902],[-1.450225],[9.712395],[-2.098274],[9.474735],[-2.035206],[5.362876],[4.498743],[-7.604490],[-3.194717],[4.982585],[-1.326268],[4.528368],[-0.855523],[-3.587996],[8.145182],[-0.325267],[-2.662036],[-2.658083],[-5.136481],[1.571301],[2.095640],[4.558723],[-1.716305],[2.356854],[0.111647],[7.829339],[5.075176],[9.125252],[6.673004],[-5.689493],[-1.818690],[3.929893],[-9.542508],[5.924886],[3.820833],[-9.233968],[6.341800],[-1.325892],[1.705922],[-2.769448],[-9.017045],[-9.081818],[-8.110662],[-2.336018],[9.870970],[1.053704],[0.287838],[6.629999],[-6.147373],[-1.836045],[9.769973],[-8.442548],[4.979476],[-7.180967],[-4.622046],[3.151231],[-5.764965],[3.611191],[3.478445],[2.572549],[-8.157256],[-4.789947],[7.759573],[-8.186296],[-8.533509],[0.172499],[9.379975],[-0.755045],[-9.247681],[3.456993],[5.722583],[-6.086290],[-5.809119],[0.451750],[3.907929],[3.878809],[9.490024],[8.644990],[7.163736],[-0.386745],[-5.181083],[3.188722],[8.786306],[-1.370824],[-2.082706],[6.655400],[-3.078773],[-1.312598],[7.536506],[7.274381],[-6.569987],[-9.255025],[-0.453545],[-7.269639],[8.545962],[-1.649977],[-4.150597],[1.925377],[7.557904],[-8.920326],[2.118098],[-3.602734],[2.896550],[8.313193],[-2.881449],[7.785538],[4.267370],[-8.545956],[2.971341],[3.129440],[7.140472],[-1.160661],[1.499550],[2.321849],[-7.851787],[-0.490460],[3.645835],[1.247758],[4.082006],[8.679171],[8.914146],[-1.622436],[7.904499],[2.893720],[9.842572],[8.540221],[-4.093940],[0.968623],[-9.703696],[-9.790182],[-2.189350],[-4.480856],[1.960510],[-8.888642],[-4.607128],[-4.220671],[-7.776689],[-4.917282],[0.624314],[-4.213136],[-6.429164],[0.036665],[7.690787],[-1.392376],[-1.769643],[-2.798953],[-9.130196],[-4.291524],[6.770950],[-2.595934],[6.891086],[1.938661],[-1.679708],[1.918026],[1.867246],[-9.438545],[4.609364],[-5.014266],[-2.029552],[-2.135018],[-7.007719],[2.998061],[-6.375443],[-6.094493],[-4.552311],[2.696837],[-9.633607],[5.569039],[7.132100],[-3.723946],[-8.301527],[-7.290131],[1.652179],[2.380600],[-7.761186],[-9.860815],[-3.720693],[3.350349],[5.450212],[-0.182573],[-1.040473],[2.118825],[5.795917],[0.623384],[9.193679],[5.876454],[9.146184],[-9.438891],[9.484677],[-3.470681],[8.944291],[-3.681228],[1.867030],[-0.352990],[2.392047],[-4.088356],[6.225448],[-3.722070],[7.451614],[1.555585],[-4.124923],[-2.021249],[-2.283281],[-6.477652],[-8.038911],[5.549547],[9.338019],[-0.870525],[6.336790],[5.676932],[0.301493],[9.658303],[-3.250646],[6.545588],[9.843584],[-6.433761],[-8.596956],[5.724669],[3.987302],[-8.041823],[6.932256],[-4.327271],[3.991343],[8.194389],[8.292995],[6.908498],[-1.589369],[8.148156],[5.576634],[-4.115956],[2.655283],[-0.351230],[-9.228192],[0.913483],[8.324144],[3.102936],[0.881943],[5.521450],[-1.587149],[-9.728366],[5.831588],[7.885256],[-3.057922],[-8.712156],[0.320131],[-0.506026],[-4.348833],[-1.410561],[3.032453],[-0.974947],[6.579678],[0.483764],[1.093314],[4.192146],[6.863607],[-8.080362],[-8.836906],[-0.071294],[-8.473933],[-8.713288],[-1.311983],[8.383530],[1.822232],[1.135349],[8.752574],[4.730017],[8.740381],[1.134437],[6.223716],[3.211842],[-7.201952],[9.063879],[4.954981],[0.877627]], dtype = "float32")#candidate|5360|(1755, 1)|const|float32
call_5358 = relay.TupleGetItem(func_1341_call(relay.reshape(var_5359.astype('int32'), [252,]), relay.reshape(const_5360.astype('float32'), [1755,]), ), 0)
call_5361 = relay.TupleGetItem(func_1344_call(relay.reshape(var_5359.astype('int32'), [252,]), relay.reshape(const_5360.astype('float32'), [1755,]), ), 0)
func_3302_call = mod.get_global_var('func_3302')
func_3303_call = mutated_mod.get_global_var('func_3303')
call_5363 = func_3302_call()
call_5364 = func_3302_call()
output = relay.Tuple([bop_5345,call_5358,var_5359,const_5360,call_5363,])
output2 = relay.Tuple([bop_5348,call_5361,var_5359,const_5360,call_5364,])
func_5366 = relay.Function([var_5344,var_5359,], output)
mod['func_5366'] = func_5366
mod = relay.transform.InferType()(mod)
mutated_mod['func_5366'] = func_5366
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5366_call = mutated_mod.get_global_var('func_5366')
var_5368 = relay.var("var_5368", dtype = "float32", shape = (2, 1, 8))#candidate|5368|(2, 1, 8)|var|float32
var_5369 = relay.var("var_5369", dtype = "int32", shape = (252,))#candidate|5369|(252,)|var|int32
call_5367 = func_5366_call(var_5368,var_5369,)
output = call_5367
func_5370 = relay.Function([var_5368,var_5369,], output)
mutated_mod['func_5370'] = func_5370
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3918_call = mod.get_global_var('func_3918')
func_3920_call = mutated_mod.get_global_var('func_3920')
call_5375 = func_3918_call()
call_5376 = func_3918_call()
func_2945_call = mod.get_global_var('func_2945')
func_2949_call = mutated_mod.get_global_var('func_2949')
var_5378 = relay.var("var_5378", dtype = "float32", shape = (176,))#candidate|5378|(176,)|var|float32
var_5379 = relay.var("var_5379", dtype = "uint8", shape = (275,))#candidate|5379|(275,)|var|uint8
var_5380 = relay.var("var_5380", dtype = "float32", shape = (500,))#candidate|5380|(500,)|var|float32
call_5377 = relay.TupleGetItem(func_2945_call(relay.reshape(var_5378.astype('float32'), [2, 11, 8]), relay.reshape(var_5379.astype('uint8'), [275,]), relay.reshape(var_5380.astype('float32'), [500,]), ), 4)
call_5381 = relay.TupleGetItem(func_2949_call(relay.reshape(var_5378.astype('float32'), [2, 11, 8]), relay.reshape(var_5379.astype('uint8'), [275,]), relay.reshape(var_5380.astype('float32'), [500,]), ), 4)
uop_5399 = relay.log(var_5379.astype('float32')) # shape=(275,)
func_3493_call = mod.get_global_var('func_3493')
func_3494_call = mutated_mod.get_global_var('func_3494')
call_5401 = func_3493_call()
call_5402 = func_3493_call()
bop_5407 = relay.bitwise_xor(uop_5399.astype('int16'), relay.reshape(var_5379.astype('int16'), relay.shape_of(uop_5399))) # shape=(275,)
func_5166_call = mod.get_global_var('func_5166')
func_5169_call = mutated_mod.get_global_var('func_5169')
call_5410 = relay.TupleGetItem(func_5166_call(relay.reshape(var_5380.astype('float32'), [500,])), 1)
call_5411 = relay.TupleGetItem(func_5169_call(relay.reshape(var_5380.astype('float32'), [500,])), 1)
uop_5425 = relay.asin(bop_5407.astype('float64')) # shape=(275,)
func_1632_call = mod.get_global_var('func_1632')
func_1635_call = mutated_mod.get_global_var('func_1635')
var_5431 = relay.var("var_5431", dtype = "uint32", shape = (1, 132))#candidate|5431|(1, 132)|var|uint32
call_5430 = relay.TupleGetItem(func_1632_call(relay.reshape(var_5431.astype('uint32'), [3, 4, 11])), 1)
call_5432 = relay.TupleGetItem(func_1635_call(relay.reshape(var_5431.astype('uint32'), [3, 4, 11])), 1)
func_4238_call = mod.get_global_var('func_4238')
func_4240_call = mutated_mod.get_global_var('func_4240')
call_5434 = func_4238_call()
call_5435 = func_4238_call()
bop_5437 = relay.add(uop_5425.astype('int32'), relay.reshape(uop_5399.astype('int32'), relay.shape_of(uop_5425))) # shape=(275,)
func_3363_call = mod.get_global_var('func_3363')
func_3364_call = mutated_mod.get_global_var('func_3364')
call_5445 = relay.TupleGetItem(func_3363_call(), 1)
call_5446 = relay.TupleGetItem(func_3364_call(), 1)
uop_5450 = relay.asinh(bop_5437.astype('float32')) # shape=(275,)
bop_5454 = relay.multiply(uop_5450.astype('uint32'), relay.reshape(var_5379.astype('uint32'), relay.shape_of(uop_5450))) # shape=(275,)
func_1748_call = mod.get_global_var('func_1748')
func_1750_call = mutated_mod.get_global_var('func_1750')
const_5458 = relay.const(-6.817445, dtype = "float32")#candidate|5458|()|const|float32
call_5457 = relay.TupleGetItem(func_1748_call(relay.reshape(const_5458.astype('float32'), [])), 0)
call_5459 = relay.TupleGetItem(func_1750_call(relay.reshape(const_5458.astype('float32'), [])), 0)
func_2945_call = mod.get_global_var('func_2945')
func_2949_call = mutated_mod.get_global_var('func_2949')
call_5462 = relay.TupleGetItem(func_2945_call(relay.reshape(var_5378.astype('float32'), [2, 11, 8]), relay.reshape(uop_5450.astype('uint8'), [275,]), relay.reshape(var_5380.astype('float32'), [500,]), ), 5)
call_5463 = relay.TupleGetItem(func_2949_call(relay.reshape(var_5378.astype('float32'), [2, 11, 8]), relay.reshape(uop_5450.astype('uint8'), [275,]), relay.reshape(var_5380.astype('float32'), [500,]), ), 5)
func_4141_call = mod.get_global_var('func_4141')
func_4142_call = mutated_mod.get_global_var('func_4142')
call_5466 = func_4141_call()
call_5467 = func_4141_call()
const_5468 = relay.const([9.897515,1.271008,6.521243,-9.476598,0.268241,9.369716,-0.257612,-1.280338,-8.603481,-3.928994,5.767022,2.549687,-3.285940,7.611869,3.799643,5.221217,-6.575453,7.082393,0.222020,9.423548,-3.423594,-9.369531,-2.452982,2.013589,3.513812,-9.548248,-2.530213,2.052695,-8.251403,5.529816,9.956084,-3.354334,9.906119,-8.531690,7.512440,9.398131,-4.428557,-7.492418,-3.495650,7.722542,2.358145,-4.126977,7.287470,-2.536234,-1.132072,8.297761,-3.441610,9.351715,7.945772,2.056831,1.153607,1.870806,-4.191636,-8.716119,2.289928,-5.917231,2.936634,-9.816822,-8.949737,-9.116211,-5.892158,8.735932,-2.092037,-9.328904,-3.842508,-4.582185,-3.632262,7.596521,-7.562196,8.703061,0.503242,-9.272757,-7.641632,-3.826725,-3.795123,5.047746,-4.416519,0.291227,5.348153,9.700569,1.010257,-8.613673,3.413152,8.054853,5.983284,9.364034,-1.109586,-6.370532,-5.329145,-5.384771,2.113567,6.810767,-0.672130,-6.696941,-2.378687,1.737483,-8.736329,4.721250,7.541526,3.145378,6.300896,1.274307,-5.073993,-0.516634,-5.427661,7.854392,-9.115178,-9.297120,-6.005284,-8.545642,-8.964119,-1.769868,6.720760,-3.178818,-6.204830,-5.275647,-2.683433,-1.307595,8.131448,4.772205,9.859923,9.424083,6.373508,-0.934478,8.698440,-1.475902,-5.308356,-2.237135,-8.482018,-3.364315,-0.201998,-8.759142,-2.177044,3.318054,5.490484,-1.268021,-2.936161,-4.926545,0.949155,1.296607,8.307779,-1.699229,-2.159456,-2.147651,5.033597,-1.665980,2.857183,-7.588960,7.696183,6.677681,-5.361461,8.061914,7.691790,-6.996114,-5.744277,3.085346,2.721870,4.767181,-2.981574,-9.004930,-0.850625,6.179930,5.581385,6.245555,-5.735602,7.404734,-6.090563,5.490903,-7.311844,-3.910517,5.611646,-2.825917,2.107895,-1.757804,7.189066,8.607406,1.357473,9.657051,-9.983125,3.669376,3.684753,9.339788,6.290938,-5.759467,-2.675923,-4.058437,-2.320492,-2.777317,-5.509584,-9.831522,4.983005,4.829793,-7.074199,0.104711,-4.068774,7.455222,0.434422,6.815022,9.774266,-4.143083,0.145645,4.818692,-5.399504,1.491086,9.086235,-7.729977,-8.387587,7.090689,2.243936,7.832675,-2.891785,2.306198,-6.618515,-6.193836,-2.729540,2.080826,-5.874344,-0.630161,2.651579,2.440860,3.296491,5.947102,-8.092683,-2.528898,-4.521211,0.664897,6.513180,-2.579899,2.086560,8.527875,-7.326229,1.404576,-4.371422,0.383225,-6.649659,-8.617355,-0.464027,6.122434,-0.382221,-5.626280,0.374505,3.027289,4.263636,-1.716382,6.746645,-9.501128,9.850323,-0.017862,6.207810,3.658823,-3.719486,4.533877,9.845390,7.925717,6.279957,-8.869830,5.955585,6.203253,-6.905003,-2.003692,0.447978,4.892273,-1.631886,-2.784497,6.335142,9.037002,0.632100,-2.911915,3.840339,6.635700,-0.908727,-1.015248,5.138115,-0.581265,6.073114], dtype = "float32")#candidate|5468|(275,)|const|float32
bop_5469 = relay.floor_mod(uop_5450.astype('float32'), relay.reshape(const_5468.astype('float32'), relay.shape_of(uop_5450))) # shape=(275,)
output = relay.Tuple([call_5375,call_5377,var_5378,var_5380,call_5401,call_5410,call_5430,var_5431,call_5434,call_5445,bop_5454,call_5457,const_5458,call_5462,call_5466,bop_5469,])
output2 = relay.Tuple([call_5376,call_5381,var_5378,var_5380,call_5402,call_5411,call_5432,var_5431,call_5435,call_5446,bop_5454,call_5459,const_5458,call_5463,call_5467,bop_5469,])
func_5472 = relay.Function([var_5378,var_5379,var_5380,var_5431,], output)
mod['func_5472'] = func_5472
mod = relay.transform.InferType()(mod)
mutated_mod['func_5472'] = func_5472
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5472_call = mutated_mod.get_global_var('func_5472')
var_5474 = relay.var("var_5474", dtype = "float32", shape = (176,))#candidate|5474|(176,)|var|float32
var_5475 = relay.var("var_5475", dtype = "uint8", shape = (275,))#candidate|5475|(275,)|var|uint8
var_5476 = relay.var("var_5476", dtype = "float32", shape = (500,))#candidate|5476|(500,)|var|float32
var_5477 = relay.var("var_5477", dtype = "uint32", shape = (1, 132))#candidate|5477|(1, 132)|var|uint32
call_5473 = func_5472_call(var_5474,var_5475,var_5476,var_5477,)
output = call_5473
func_5478 = relay.Function([var_5474,var_5475,var_5476,var_5477,], output)
mutated_mod['func_5478'] = func_5478
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3427_call = mod.get_global_var('func_3427')
func_3428_call = mutated_mod.get_global_var('func_3428')
call_5487 = relay.TupleGetItem(func_3427_call(), 0)
call_5488 = relay.TupleGetItem(func_3428_call(), 0)
output = relay.Tuple([call_5487,])
output2 = relay.Tuple([call_5488,])
func_5492 = relay.Function([], output)
mod['func_5492'] = func_5492
mod = relay.transform.InferType()(mod)
mutated_mod['func_5492'] = func_5492
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5492_call = mutated_mod.get_global_var('func_5492')
call_5493 = func_5492_call()
output = call_5493
func_5494 = relay.Function([], output)
mutated_mod['func_5494'] = func_5494
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5227_call = mod.get_global_var('func_5227')
func_5228_call = mutated_mod.get_global_var('func_5228')
call_5564 = relay.TupleGetItem(func_5227_call(), 1)
call_5565 = relay.TupleGetItem(func_5228_call(), 1)
output = relay.Tuple([call_5564,])
output2 = relay.Tuple([call_5565,])
func_5582 = relay.Function([], output)
mod['func_5582'] = func_5582
mod = relay.transform.InferType()(mod)
output = func_5582()
func_5583 = relay.Function([], output)
mutated_mod['func_5583'] = func_5583
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2278_call = mod.get_global_var('func_2278')
func_2280_call = mutated_mod.get_global_var('func_2280')
call_5591 = func_2278_call()
call_5592 = func_2278_call()
func_2307_call = mod.get_global_var('func_2307')
func_2309_call = mutated_mod.get_global_var('func_2309')
call_5598 = relay.TupleGetItem(func_2307_call(), 0)
call_5599 = relay.TupleGetItem(func_2309_call(), 0)
output = relay.Tuple([call_5591,call_5598,])
output2 = relay.Tuple([call_5592,call_5599,])
func_5601 = relay.Function([], output)
mod['func_5601'] = func_5601
mod = relay.transform.InferType()(mod)
mutated_mod['func_5601'] = func_5601
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5601_call = mutated_mod.get_global_var('func_5601')
call_5602 = func_5601_call()
output = call_5602
func_5603 = relay.Function([], output)
mutated_mod['func_5603'] = func_5603
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4141_call = mod.get_global_var('func_4141')
func_4142_call = mutated_mod.get_global_var('func_4142')
call_5628 = func_4141_call()
call_5629 = func_4141_call()
output = relay.Tuple([call_5628,])
output2 = relay.Tuple([call_5629,])
func_5630 = relay.Function([], output)
mod['func_5630'] = func_5630
mod = relay.transform.InferType()(mod)
mutated_mod['func_5630'] = func_5630
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5630_call = mutated_mod.get_global_var('func_5630')
call_5631 = func_5630_call()
output = call_5631
func_5632 = relay.Function([], output)
mutated_mod['func_5632'] = func_5632
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3427_call = mod.get_global_var('func_3427')
func_3428_call = mutated_mod.get_global_var('func_3428')
call_5651 = relay.TupleGetItem(func_3427_call(), 0)
call_5652 = relay.TupleGetItem(func_3428_call(), 0)
func_1423_call = mod.get_global_var('func_1423')
func_1426_call = mutated_mod.get_global_var('func_1426')
const_5659 = relay.const([7.821481,-2.766492,0.102194,7.397860,4.151801,6.302296,-1.754858,-1.029181,-9.728311,8.653795,-3.901505,-7.489988,8.186553,8.904657,-3.050640,-8.466950,1.123488,-4.215203,1.393482,6.334507,-2.454007,-9.557380,-9.247792,-8.028295,8.478289,3.006892,-1.869265,-3.064884,0.324400,-8.069197,-8.554672,7.591480,8.027586,-3.627237,7.682184,2.813292,-8.974478,5.442198,-3.527118,-9.821047,2.930856,-0.111327,1.866853,-1.921298,-4.884855,4.461847,4.450987,-9.170267,-7.743399,2.456374,-6.679533,1.899977,-0.689077,8.619899,-9.478905,-8.059010,-1.589514,9.661405,1.257925,-0.030839,-7.015111,-1.203175,-9.158705,-4.505463,3.312940,3.616514,-7.311276,3.674620,9.013053,-8.802631,-3.647240,2.793258,8.186198,-6.331970,-6.420429,-2.218487,-3.174908,2.349689,3.468702,7.513964,3.032127,-5.131007,-0.542929,2.847705,3.985979,0.916920,-1.092385,-7.897107,-6.568408,1.909556,4.174905,6.935957,-1.111380,-0.948236,7.405755,7.875144,-3.138310,-1.735284,8.541389,-7.504004,4.665852,-4.664641,9.640754,0.084820,1.509199,-6.142554,-8.298140,1.556091,-4.499834,-8.472272,3.756379,2.442052,-7.487682,-4.492448,3.212302,-9.346999,3.230520,-4.190244,0.953777,-8.223920,-0.054293,3.542741,-4.725936,-1.512960,-3.738144,-1.547419,-8.642484,-4.519912,-4.609502,-4.897322,7.006188,-0.014802,7.965009,7.551952,2.419079,6.718710,0.989721,-9.756957,9.502581,-7.743700,-2.810886,-5.352289,-1.976170,4.893854,8.042682,-6.000769,-3.885706,0.829100,-2.652374,-9.629501,-9.744179,3.087346,-2.446780,-3.014304,-0.974011,7.339707,2.519233,8.878843,-4.851753,-9.412721], dtype = "float64")#candidate|5659|(160,)|const|float64
call_5658 = func_1423_call(relay.reshape(const_5659.astype('float64'), [16, 5, 2]))
call_5660 = func_1423_call(relay.reshape(const_5659.astype('float64'), [16, 5, 2]))
func_4479_call = mod.get_global_var('func_4479')
func_4482_call = mutated_mod.get_global_var('func_4482')
const_5672 = relay.const([4.430857,-5.764568,-3.284096,8.661669,4.803806,5.829721,-0.452588,7.414266,-9.524348,-2.576565,-2.374469,-6.356747,1.653153,1.946461,8.742400,8.808977,-7.777852,5.334782,1.150707,-8.094851,-9.685235,-9.986253,4.217821,-5.959745,-9.167103,8.743489,2.209687,-1.612550,0.039590,-5.635712,-8.125060,3.200792,8.010839,4.066441,-6.190809,5.830082,5.000907,2.165892,5.453210,7.005081,-8.783611,-0.195928,-0.956561,-7.118389,-0.209908,9.203823,-1.321638,-9.529694,6.630820,-8.518581,0.277222,-7.249929,-6.332017,6.578948,5.593368,2.281739,0.034749,-5.115085,-1.576144,1.550120,4.523767,1.944775,9.569530,0.482254,7.828819,-7.746678,0.412220,0.420560,-7.590991,8.200649,7.559704,5.302835,1.402579,8.076823,1.869423,-8.838594,6.947794,-8.174181,5.049968,9.657142,-0.163542,0.074311,-4.237638,3.988893,6.366360,-0.477219,9.053444,1.324233,9.696883,-1.227403,2.366394,7.361777,-5.631195,-6.925063,2.959202,-5.389725,8.363340,3.285010,-7.420691,9.370147,-2.327611,4.920372,6.143361,-3.183481,2.013448,4.209303,8.812351,6.287016,7.147243,-9.185160,2.318239,-0.793075,-1.717512,-7.976617,-1.333608,4.657549,5.256316,-3.606830,7.342689,-0.546987,5.611369,-6.235967,-6.462044,-2.040983,0.567923,2.852198,1.430191,6.925016,2.245186,-1.898965,1.462026,-6.848071,-1.918920,-4.384887,5.917318,-1.535027,-2.956604,-2.491145,-0.214431,-6.384598,5.864147,-4.935720,8.291468,-7.517785,9.646830,-0.899814,-0.890759,-6.539592,6.293524,6.011786,1.526057,6.322252,-1.371503,-7.003721,-6.469711,-8.315728,-0.035497,-4.622974,-0.511841,6.292267,-9.518506,4.141385,-3.439420,6.142757,-9.937078,7.984531,7.918905,4.053906,-8.293626,-2.562771,8.206518,-5.846947,-2.785977,1.086947,4.062741,-6.985855,6.839658,1.775665,0.983666,4.333407,3.423940,4.893751,-7.623460,-5.555281,2.734428,8.609847,5.216183,-8.087486,5.055349,-5.906836,-4.852063,-9.530260,-6.009286,-0.417321,-4.134111,3.048752,-3.782358,-5.975297,-5.047037,6.043815,-8.310999,-6.602454,-7.926679,9.670119,-8.055092,-7.980123,-1.714618,-6.215881,-9.712023,6.326562,4.601515,-8.876269,0.030236,-2.465150,8.163007,0.541484,-4.980551,9.567106,9.269834,-4.080624,8.360134,-4.325571,5.012486,-6.625847,8.913378,4.250748,2.943256,-3.797739,-5.803305,-1.636782,-9.234395,1.243717,1.351917,1.755957,3.684901,-5.523718,6.356539,5.488784,-2.288239,-9.583239,9.327518,-2.258167,-3.527721,8.527547,1.216959,-4.742968,-8.930035,-8.133452,9.486754,-3.095686,-6.899720,8.774225,3.050159,-1.536019,-2.609829,-9.745269,-6.791612,-1.817555,4.335139,-0.721051,3.957048,1.971804,-2.821416,6.184675,5.621334,1.528160,6.381617,9.721383,8.186380,-4.045590,4.445011,7.713882,0.136117,-6.579309,4.533010,0.932493,3.835901,-9.311309,-6.345523,6.899634,3.551451,0.056975,3.817185,-3.667147,3.539910,0.034915,6.985271,-0.818382,-4.677107,0.806722,7.754771,1.679776,7.842886,9.773441,7.861124,-1.903421,3.786270,3.953377,-3.876053,2.794185,-1.434150,-0.986421,8.667363,-5.573260,4.846713,5.934964,-4.676539,-7.705507,5.551189,-7.441883,-1.564405,6.723627,-4.582485,1.278223,-2.742285,-8.632994,4.757443,-7.290923,-0.308652,-6.658610,8.171400,-7.346079,-6.005084,9.766138,-9.978985,6.002428,-0.241361,-0.538734,0.707349,-9.901092,-7.888950,3.150725,5.029940,-4.638898,-7.920146,-5.459276,7.754436,-9.453420,1.250746,7.610048,2.165925,-9.365746,3.880548,-1.283051,-7.575382,8.983830,-5.379935,-5.950604,-3.209923,3.966424,-3.761744,-9.442915,-7.632383,5.358427,6.512774,-6.160455,1.087507,-7.793391,5.664240,-1.551216,5.959934,3.416783,-5.405087,-2.686604,-7.672040,6.322520,9.922154,-2.511268,-6.145773,0.004478,-0.290655,-4.534088,-7.847238,1.071640,-1.091079,-6.944303,9.964126,8.789401,1.002771,-0.027876,2.795835,-6.820742,-0.252828,-0.187763,1.518215,-7.773959,6.695960,3.806374,5.237789,-7.348982,-4.876637,-9.595521,-5.845425,2.014317,8.855969,5.334432,-8.180028,8.889933,9.875182,0.564653,3.787720,-2.864295,1.830322,-7.465738,-3.173301,-8.677260,5.322362,-7.932608,-1.736253,-1.382540,-4.205788,-9.756925,1.516734,2.553414,0.686687,2.153236,-0.837235,-2.766640,-7.690607,-8.914506,6.006367,5.767199,0.955512,-6.381085,-2.244488,9.788560,-1.859717,7.874535,7.321642,-8.120726,5.258574,5.646634,-8.995435,0.579747,0.991450,7.976038,-1.330072,9.771182,4.627439,3.883663,-0.597116,-0.005225,-2.509459,1.905930,-0.289472,9.428488,9.814789,8.394807,-9.567019,-4.613810,-4.705024,-3.301592,5.215592,9.671973,0.419956,-4.545465,7.263144,-7.523111,-4.157712,-4.333970,-5.424689,-5.915349,-8.723809,7.654039,4.271886,-8.222581,6.985961,-1.576044,5.656631,9.173650,0.527285,-2.997068,-9.654150,-9.730123,-2.367744,7.103980,-8.890726,9.600184,6.806627,9.818591,-4.899910,7.221436,-7.206466,-9.657111,6.074028,-0.681375,6.541376,7.995098,-7.695511,-5.772878,-6.523053,8.854287,-2.507828,-5.167018,9.456447,-2.105411,8.596593,4.260368,3.844411,5.956835], dtype = "float32")#candidate|5672|(500,)|const|float32
call_5671 = relay.TupleGetItem(func_4479_call(relay.reshape(const_5672.astype('float32'), [250, 2])), 2)
call_5673 = relay.TupleGetItem(func_4482_call(relay.reshape(const_5672.astype('float32'), [250, 2])), 2)
func_2307_call = mod.get_global_var('func_2307')
func_2309_call = mutated_mod.get_global_var('func_2309')
call_5679 = relay.TupleGetItem(func_2307_call(), 0)
call_5680 = relay.TupleGetItem(func_2309_call(), 0)
func_3267_call = mod.get_global_var('func_3267')
func_3268_call = mutated_mod.get_global_var('func_3268')
call_5682 = func_3267_call()
call_5683 = func_3267_call()
output = relay.Tuple([call_5651,call_5658,const_5659,call_5671,const_5672,call_5679,call_5682,])
output2 = relay.Tuple([call_5652,call_5660,const_5659,call_5673,const_5672,call_5680,call_5683,])
func_5688 = relay.Function([], output)
mod['func_5688'] = func_5688
mod = relay.transform.InferType()(mod)
output = func_5688()
func_5689 = relay.Function([], output)
mutated_mod['func_5689'] = func_5689
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5492_call = mod.get_global_var('func_5492')
func_5494_call = mutated_mod.get_global_var('func_5494')
call_5708 = relay.TupleGetItem(func_5492_call(), 0)
call_5709 = relay.TupleGetItem(func_5494_call(), 0)
func_4323_call = mod.get_global_var('func_4323')
func_4326_call = mutated_mod.get_global_var('func_4326')
const_5719 = relay.const([4,-8,-2,-7,-5,9,-5,-4,6,9,5,-4,9,-6,-7,-4,4,5,7,4,6,-9], dtype = "uint64")#candidate|5719|(22,)|const|uint64
call_5718 = relay.TupleGetItem(func_4323_call(relay.reshape(const_5719.astype('uint64'), [1, 2, 11])), 0)
call_5720 = relay.TupleGetItem(func_4326_call(relay.reshape(const_5719.astype('uint64'), [1, 2, 11])), 0)
func_5279_call = mod.get_global_var('func_5279')
func_5282_call = mutated_mod.get_global_var('func_5282')
const_5730 = relay.const([-1.178427,-3.337897,-9.929151,7.416687,4.149248,9.943181,9.859154,2.264443,-5.219407,-2.182281,0.400228,7.277548,6.858548,6.547157,-5.701329,0.026841,-4.741054,-6.986455,7.903709,-6.253553,-3.525259,-5.673411,-7.834047,-7.599467,-4.288690,-4.172102,-4.127394,-7.141809,-8.591782,-3.220675,-8.576207,0.067276,9.399167,8.660526,-0.889006,2.391205,5.090596,-7.605822,-9.990721,-0.386441,8.623481,-9.200969,-3.400139,5.690061,2.396187,4.962911,2.207152,-7.281527,8.853766,-4.227905,8.696235,-9.897980,7.455838,-6.430032,-3.473865,6.705870,7.651132,3.841876,-9.142114,2.327368,-7.206835,6.815143,8.715395,-5.020077,-4.471480,-2.866490,7.636173,-6.595389,3.882605,-7.375053,-0.504834,-8.382030,4.538805,5.122506,-1.065341,0.576839,-6.565355,6.148143,0.232239,-8.990400,-3.160651,6.930386,9.755681,-7.112500,6.682203,-3.841591,-6.319512,3.093602,-0.447394,6.163748,0.586193,1.286338,-7.022351,-8.547429,0.824677,1.397112,9.906767,2.639697,-6.424293,-1.508659,-2.969692,1.414350,6.839929,-8.267163,-7.512092,-5.897344,6.832795,3.104982,-9.268469,6.792742,-8.440922,6.057949,9.789627,-8.045235,1.592275,0.217280,-2.432941,-2.682300,-2.279934,9.064674,8.693754,-6.052263,-2.971363,-2.863461,6.820029,-0.618347,-9.075859,-3.692169,-0.988801,8.521101,6.385489,6.465213,-7.161038,2.677619,-2.079295,1.176464,-1.517453,-8.725529,6.532313,-0.346558,-2.337496,-2.534466,-1.592980,7.291273,4.934511,-6.403756,2.358759,-5.710165,-2.925946,-4.091194,7.201878,-8.706536,-1.927723,-7.223284,9.051048,-0.971052,5.416001,-9.221761,8.921694,-9.134454,-4.141216,7.563357,-2.283055,8.232756,2.627400,0.259739,3.787446,1.387310,1.448822,1.699351,-6.162152,-1.268216,-4.689623,8.392016,-3.172017,8.400749], dtype = "float32")#candidate|5730|(176,)|const|float32
call_5729 = relay.TupleGetItem(func_5279_call(relay.reshape(const_5730.astype('float32'), [2, 11, 8])), 0)
call_5731 = relay.TupleGetItem(func_5282_call(relay.reshape(const_5730.astype('float32'), [2, 11, 8])), 0)
uop_5739 = relay.acos(call_5729.astype('float64')) # shape=(2, 11, 8)
uop_5741 = relay.acos(call_5731.astype('float64')) # shape=(2, 11, 8)
func_5309_call = mod.get_global_var('func_5309')
func_5313_call = mutated_mod.get_global_var('func_5313')
const_5752 = relay.const([-4,5,-8,-5,-9,8,-9,-4,5,3,4,-5,-8,-6,-9,-6,-5,8,-4,-4,-9,7,-1,8,-2,-9,6,3,-3,1,-9,-6,10,8,4,-6,-8,-10,5,5,10,4,-10,-9,4,-6,9,-9,-3,-2,9,-9,-5,6,-10,5,-4,7,6,6,8,-4,1,5,-8,-10,-8,-6,9,-1,2,2,-5,-10,5,-10,8,-9,7,3,-10,4,4,-1,5,-4,7,5,-5,4,2,4,-8,-1,6,2,-8,3,8,5,-5,-10,-4,-6,-1,10,4,5,4,9,-1,5,-7,1,4,9,-4,-2,6,-9,8,-10,3,6,-3,-9,-6,-2,-5,-10,-9,-8,10,1,-10,4,-10,-2,-2,-2,3,-7,-4,-4,4,-9,3,-5,-1,-10,9,-9,-10,3,1,-7,5,-5,-5,-1,5,1,9,-2,4,-1,5,3,-3,7,4,-8,8,-9,4,-1,9,-8,9,9,1,-8,10,-4,-10,6,-5,-2,-10,7,10,-5,-1,5,1,3,4,10,5,-6,7,8,8,6,-10,4,-2,-6,9,2,7,-4,9,4,2,-8,4,10,5,-10,10,2,2,-4,1,-3,-3,9,4,5,-5,-2,8,-1,-1,-7,-6,2,9,8,-4,-10,9,9,3,7,7,-7,3,-8,-10,5,4,-3,-5,-2,-4,-8,-2,-6,2,-4,-7,4,10,4,4,5,9,10,-9,-5,-7,-7,9,-5,-9,10,10,5,5,-10,-3,9,-3,7,3,8,-6,-8,-8,-6,4,4,9,5,-1,2,-2,-7,10,-8,10,3,-10,-1,-8,7,4,-7,1,6,9,-7,1,-7,-9,-5,10,5,1,-10,4,2,-7,10,2,-1,7,3,1,8,4,1,3,6,3,-2,3,2,2,-9,1,7,-7,4,10,-2,-7,-10,8,-4,-4,-7,-2,-7,2,-9,6,-8,6,-3,-8,-3,-7,-5,1,-7,8,9,2,4,-4,8,1,-4,-10,3,3,4,9,6,-1,-4,-6,8,-1,-3,-7,6,7,-5,7,6,4,-2,1,4,1,-10,-10,-7,3,7,-3,6,-1,10,8,9,-5,-8,9,8,-7,8,-1,10,9,3,-8,-3,-1,10,8,-3,10,-9,3,-8,-8,-10,5,2,-5,5,4,-6,-10,6,6,1,3,3,-9,-8,1,-7,-6,-10,4,8,-5,4,-9,-3,2,-10,-6,-10,-8,-4,-4,5,2,3,-3,5,-5,1,-1,-10,-8,5,3,-9,-4,10,-5,-10,-10,-2,-3,-9,8,-4,-6,-10,-3,8,-2,9,-1,-4,3,5,6,-6,-6,9,7,-3,-6,-7,9,6,-4,5,-3,-6,-2,10,10,-7,3,2,-7,-4,1,-3,7,-2,-4,8,8,2,5,-8,-9,3,10,1,4,2,7,6,5,-6,-8,6,10,-6,1,-2,-8,2,2,-5,1,2,3,5,-7,-6,-7,9,-10,4,10,4,1,-5,-1,7,-10,-1,8,-8,7,8,-6,-3,3,-10,1,2,-9,-5,9,-4,3,-1,-1,4,3,-4,-10,-5,-4,7,-10,9,7,-2,8,-7,-3,-1,-7,4,8,9,9,-2,-1,-10,9,-10,5,-5,8,-5,-8,7,1,5,1,7,8,-3,-8,9,6,6,-1,-6,2,-2,-6,-6,-2,6,3,-3,1,-1,3,-10,7,-2,-6,-9,-10,9,-10,2,-3,5,-2,-8,-8,-3,9,2,9,6,2,6,-6,7,9,8,-8,8,3,2,-7,4,10,5,8,7,-7,-2,-9,9,-8,7,-1,-7,-5,8,6,1,6,7,7,3,-8,-9,4,2,6,-2,-8,-1,-10,8,-1,-3,-5,10,-6,-6,-10,1,4,9,-7,-6,10,10,8,-7,7,5,-2,-1,-10,3,3,-7,9,6,-5,-3,-4,6,-10,-3,4,-8,3,-7,8,4,-5,-8,-4,-2,-1,-7,-7,8,-5,4,-9,8,-2,4,6,-1,8,9,8,-5,6,5,-5,3,-4,-1,-9,-4,3,-1,7,-2,-5,-8,-2,-3,5,4,-3,-1,-3,-1,-1,-3,2,-5,-10,-5,-8,10,-6,-8,1,2,-6,10,-5,-2,-5,-1,1,-7,1,-7,-4,8,-8,-4,6,-4,1,4,6,-10,-10,-1,7,3,-9,-6,5,-7,-10,-5,-7,1,-2,3,10,10,-4,-1,8,-8,6,2,-10,6,9,6,-10,-3,-1,-2,-10,1,1,5,-9,8,9,-7,-8,8,-6,-3,-1,-1,-3,-5,3,-6,-9,-6,4,-4,-4,3,-3,1,-5,-8,-1,1,1,-6,2,-1,-3,-1,-2,3,5,-8,-4,8,3,6,-4,-1,-4,1,1,9,10,-2,-7,6,10,8,5,5,-3,-6,-1,4,-4,-1,7,-8,2,-9,6,8,-3,1,-6,6,1,-8,8,6,-9,6,9,-2,5,-9,-9,6,7,10,8,-5,-9,-9,-9,9,-2,-3,-1,1,8,-7,-10,9,-2,3,6,-9,2,-1,1,-8,-7,3,6,3,5,-3,3,-4,-2,7,6,-2,-3,1,5,8,-2,9,6,-4,-10,-10,10,9,3,-1,-3,-9,-5,10,-2,3,1,2,4,10,4,8,-4,-7,5,5,-10,-4,-5,-9,3,10,2,1,9,-1,-3,-8,-7,5,-2,10,7,1,8,-10,9,-3,4,-8,-7,-8,7,-9,-3,-6,5,9,2,3,-9,1,2,1,-9,-1,-10,-9,4,-1,10,-4,-7,-6,-2,-7,1,10,-1,1,2,8,-10,-8,3,-3,-9,10,9,-5,3,3,1,7,-6,3,10,-7,10,-7,5,8,9,1,1,1,9,8,-1,1,-5,3,-8,8,-6,-3,-6,-6,-6,-5,3,3,-1,-2,-7,-8,-9,-8,1,-7,10,7,-10,3,10,-4,-3,6,7,-8,3,5,-9,1,8,9,9,-5,9,-4,5,5,-3,6,1,4,-2,-7,1,-2,-7,8,7,4,3,-8,-6,-8,5,8,-10,9,-1,-4,4,5,7,9,9,1,-3,-2,-1,9,6,2,-2,-9,-7,7,-9,7,8,-3,1,-10,-4,-3,-5,-10,10,9,5,6,1,5,8,9,8,-2,7,-3,-6,-5,-9,-4,-9,2,10,-5,-1,-2,-10,4,4,-7,10,9,6,-7,-1,7,-3,-3,7,6,6,-7,-3,-6,-7,-6,-5,-2,-1,10,-1,1,6,-9,-9,2,-6,-6,10,-6,9,5,-8,-6,10,-10,-1,-5,2,9,-2,1,-10,9,-10,-8,-6,2,-3,-3,-2,-4,-4,1,4,9,1,-7,8,-2,10,7,4,-2,-8,10,1,-7,2,1,6,-5,2,9,-8,8,10,6,5,-10,6,-6,-1,-10,-9,-10,-2,3,7,-4,10,2,7,3,-7,-6,-1,8,3,9,-2,8,-4,-10,10,5,-7,-1,3,8,-5,3,-7,1,2,4,9,-9,-1,-3,6,5,2,-10,8,-7,2,-10,-2,3,-1,9,6,-10,-9,-2,-10,8,10,9,4,2,7,-9,3,4,-6,1,-10,-3,-5,-4,1,-8,-8,9,-2,-1,3,7,-9,-9,5,1,2,-4,8,-3,-10,7,8,1,9,9,2,-7,9,8,-5,-9,2,3,3,-6,-6,2,-3,4,-5,-3,8,-9,-7,9,5,-6,-1,-6,6,7,7,8,2,-1,4,5,-7,7,9,-3,-3,-3,1,-9,1,10,5,7,9,-6,3,3,6,-1,7,1,-4,-4,-4,-1,9,3,1,-5,8,-3,5,-1,9,5,-6,6,3,-7,3,1,1,-9,-4,5,8,-2,-8,-1,5,-3,-4,-4,-8,-1,-1,4,8,6,-8,3,3,-8,-10,-9,4,-9,2,-3,-6,-3,1,-9,-3,-1,8,-6,3,1,2,10,4,4,5,-6,4,-6,-7,3,9,-10,10,-7,1,-6,-10,10,-8,-7,2,3,-3,2,-5,-9,-9,-1,-6,-1,8,9,-4,9,-3,-6,-10,-4,2,-2,-1,3,-9,-8,-5,-9,6,9,8,3,-4,8,-2,6,8,-2,6,-10,10,-9,7,-5,7,5,2,9,-9,-10,1,8,4,2,-5,-5,10,-9,-2,-10,-10,8,-2,-10,6,-5,-7,-10,-3,3,3,-3,1,-10,6,-6,4,10,1,-9,3,-5,7,3,8,-7,3,-5,-2,1,-6,6,-9,6,-10,6,-8,-4,-8,4,3,8,1,-2,10,-1,-8,-6,5,8,6,-9,-7,-1,1,3,-7,2,6,-1,7,3,-8,4,-3,-9,8,-5,-2,-2,-4,-7,-7,10,-10,10,-2,-5,-5,6,-3,7,4,10,2,6,-8,8,-1,9,-1,1,5,6,4,8,-6,3,-8,-3,-5,-6,-2,-8,-5,4,-9,9,-10,-4,6,4,-6,9,9,4,-1,-7,-7,7,4,-7,-8,-7,-1,3,-2,9,-5,1,10,-8,-6,-7,-9,-4,-8,6,-9,-4,-5,-8,-5,4,-5,6,2,8,6,-2,2,8,9,3,6,-8,6,7,-5,3,-7,7,2,9,5,-3,-9,4,-4,6,6,-10,-4,-6,-9,10,10,9,-7,2,-2,-6,5,-9,-10,-8,10,1,-6,-2,-5,-4,4,-7,-2,2,3,4,-9,-8,7,7,7,-1,2,9,-10,4,-6,4,9,1,3,3,-10,2,8,-7,7,9,5,-9,-3,-6,4,-9,5,7,7,1,3,-5,5,8,-1,-3,7,9,7,-8,-7,-5,7,2,4,-1,9,7,-7,-5,-4,-7,2,-8,3,-1,-5,3,-10,5,-8,-2,2,10,4,10,-6,8,2,9,4,-6,-10,-10,-5,6,-9,2,-8,3,-8,2,9,-3,8,6,4,10,4,6,-4,5,-1,-7,7,-2,2,-8,6,1,5,-5,-3,5,-6,7,3,5,6,4,-1,-8,-2,5,-2,-9,8,-6,-8,6,-1,-4,-4,-8,-1,4,1,-7,2,9,10,9,-2,7,-7,4,8,2,-6,-2,5,9,10,6,-7,6,-7,-3,3,10,5,-7,3,4,-2,-6,-4,10,10,8,5,5,10,-10,10,-2,-6,-9,-10,8,-3,6,1,3,-6,-1,6,2,5,-10,1,-3,3,-6,5,5,-8,5,-1,-3,1,7,-1,7,10,-5,1,8,8,-9,7,2,8,-7,8,-5,3,8,2,1,5,3,-2,2,-2,-4,8,4,-5,-5,8,-4,2,6,9,6,-1,-2,7,-4,6,7,6,-9,2,-8,4,3,5,-1,-5,10,3,1,-7,-10,7,-8,9,-5,-3,-1,-4,4,4,-6,2,8,-8,-7,6,-8,5,5,5,-2,3,-5,10,6,5,-6,8,2,3,-2,7,1,8,-5,-7,1,-2,9,-8,-9,-9,-7,7,4,1,10,-6,9,8,-8,2,-5,10,8,10,-8,-2,-5,-6,-8,5,-6,-10,8,8,-3,9,-5,-3,-4,10,-2,-9,-1,6,-4,9,5,-7,-7,8,5,9,4,-5,-7,-2,-9,-5,-10,4,-5,5,4,10,-7,3,-6,4,-6,-2,-7,-1,-7,-9,-9,-10,5,4,-5,3,5,-6,8,-4,-8,-5,-1,1,3,7,-2,8,-2,9,7,3,-7,4,6,10,-4,-1,3,5,4,10,8,-5,10,-2,-7,-10,2,2,2,4,-8,1,8,7,-7,-10,-5,-7,-1,4,4,4,10,3,-9,9,5,1,5,7,-7,7,2,-8,3,-4,-6,2,-6,7,4,-5,6,-2,5,5,4,5,5,2,-5,-4,7,-6,-1,-10,-9,-3,4,7,5,-3,-3,-9,-4,-8,-9,2,8,-9,-1,3,-8,6,-2,-1,-5,7,5,-8,-7,9,-9,-10,-9,6,-1,-9,-7,-9,9,7,-4,-4,8,-7,-10,-1,-7,8,3,3,4,3,10,10,3,5,-2,8,3,-7,2,-4,10,-5,5,-4,-4,8,-8,3,-8,1,-7,1,4,5,-7,-7,10,-1,9,-1,2,-7,2,6,-8,9,3,9,2,-5,2,8,-1,-4,4,-5,9,-1,-2,10,-1,9,-10,3,-2,-1,-8,6,-7,2,-10,-10,-9,-9,-7,4,7,-3,-2,9,3,-10,-10,-10,9,-10,1,7,10,-2,2,-6,1,-7,4,-1,-9,-9,7,8,3,2,-8,3,-2,7,-5,6,2,1,1,-6,2,9,-5,3,5,-2,-4,-2,-2,-4,-4,4,-4,-6,8,-5,-5,10,-3,10,8,-2,-6,1,-5,-6,-3,-7,-7,4,-4,6,5,-1,-10,-8,-2,-1,3,8,-6,9,7,8,10,9,-3,5,-4,-8,-9,3,5,10,7,-9,4,-4,-3,-7,6,-9,5,-9,-10,1,5,1,-7,1,-2,-7,-8,9,5,6,-2,-2,-9,-3,-2,-8,-8,7,3,9,8,-4,-9,8,7,-7,9,5,4,6,-4,-3,5,-8,-7,6,5,2,2,-9,-3,9,10,7,6,10,-8,-2,2,-5,-1,4,2,-9,5,-3,-6,8,8,10,9,-4,2,3,-10,-2,-9,6,-2,6,-4,-6,3,6,1,7,-7,-8,9,-2,-10,-9,-3,-10,9,-2,7,3,4,-1,-7,-5,-9,5,6,8,-4,-7,-3,1,5,7,1,-9,-1,-10,-1,5,1,2,9,-3,9,9,-7,6,-4,-3,2,2,4,-4,-8,-7,-10,6,8,-4,9,1,-6,9,9,-6,4,6,1,-5,8,-8,2,10,3,-9,9,-2,6,-4,-3,-7,10,5,3,2,3,-10,6,-4,-5,-5,2,9,9,4,6,9,7,1,5,9,-5,-2,10,2,-9,-10,-4,-1,-4,5,8,-8,-5,3,4,7,-3,-4,4,-8,5,-6,-7,-2,-3,3,-8,-6,-1,4,-5,9,-9,-2,-9,6,10,-10,8,-10,-8,2,-3,10,1,1,4,-3,3,6,8,3,-3,-5,-5,-9,7,9,-2,-5,-5,-7,8,-2,9,-10,-1,3,6,-2,-2,-5,2,8,-5,7,1,8,5,-10,-1,1,3,-3,-3,-1,-6,5,-10,-4,-8,-6,-4,-10,-6,5,-3,9,-2,5,9,-2,2,-7,-2,9,1,-1,-10,5,-3,5,-7,-2,-7,4,-4,-3,6,9,10,-2,-3,-5,5], dtype = "int8")#candidate|5752|(2704,)|const|int8
call_5751 = func_5309_call(relay.reshape(const_5752.astype('int8'), [13, 13, 16]), relay.reshape(const_5752.astype('int8'), [13, 13, 16]), )
call_5753 = func_5309_call(relay.reshape(const_5752.astype('int8'), [13, 13, 16]), relay.reshape(const_5752.astype('int8'), [13, 13, 16]), )
bop_5758 = relay.less_equal(const_5719.astype('bool'), relay.reshape(call_5718.astype('bool'), relay.shape_of(const_5719))) # shape=(22,)
bop_5761 = relay.less_equal(const_5719.astype('bool'), relay.reshape(call_5720.astype('bool'), relay.shape_of(const_5719))) # shape=(22,)
func_4578_call = mod.get_global_var('func_4578')
func_4582_call = mutated_mod.get_global_var('func_4582')
const_5766 = relay.const(-5, dtype = "int8")#candidate|5766|()|const|int8
const_5767 = relay.const([[-7,2,6,-8,-3,-7,-2,-7,-8,8,-8,-10,-10,4,2,-6,10,4,5,1,2,10,-2,-4,-7,-6,5,-4,8,3,-4,10,6,-10,-5,-10,8,-2,-6,3,-9,6,5,-6,-8,5,-9,-5,-9,5,-5,1,-4,-4,-9,4,5,9,10,5,8,1,4,-10,1,7,2,-9,-10,9,-1,-7,-4,8,-6,3,2,-9,10,-9,9,-8,5,9,4,9,2,-2,4,2,5,-4,-9,-3,-4,-3,2,4,-1,-7,5,-10,1,5,4,-7,-3,5,-4,5,5,-3,-9,6,-3,5,-8,5,7,-5,5,9,3,-4,-6,-6,-6,8,9,-7,7,-8,-7,4,-1,6,-1,6,2,-2,8,9,-9,9,-3,10,-8,-6,-9,2,1,8,6,-7,-5,-5,7,6,3,5,2,5,-2,-9,-3,-3,-1,-6,8,-5,10,-5,-6,-4,8,4,-5,-2,-1,-9,3,9,-4,3,6,-4,-8,7,2,4,1,10,8,-2,-4,-3,3,-3,7,-1,-3,-3,-6,8,2,-9,-9,-8,2,8,-10,-5,3,2,-5,4,7,-1,-8,4,1,10,2,-1,-7,-10,-9,10,2,-3,4,-7,5,-6,8,-10,3,3,1,2,10,-4,7,-1,7,-8,-3,2,4,10,9,-1,3,8,5,-1,1,3,3,-1,-10,-9,-3,-1,-10,8,-5,10,2,-4,-9,3,-2,2,-4,6,-9,7,6,10,2,-5,-9,-7,-6,-10,-5,7,-3,3,-9,1,3,-3,-7,7,10,-8,-7,-10,5,-10,-4,8,-5,3,9,3,2,-3,8,10,-1,9,-5,-3,-10,9,-9,1,7,7,10,7,7,-2,-9,-4,-3,10,-3,-8,-5,7,3,5,4,7,-3,5,-4,6,-3,6,5,-4,9,3,1,6,-10,6,-5,7,9,2,2,9,-10,1,-10,-4,-1,1,-9,-5,-9,2,-6,-6,4,10,-5,1,-5,9,-1,4,-1,3,-1,-8,9,-6,2,10,9,-2,-9,8,-9,-1,3,4,10,6,4,-4,6,6,6,-4,5,9,-10,10,-7,10,6,-6,1,-10,7,-6,5,-3,-9,6,-2,8,4,-1,-10,-3,-7,3,-2,-3,-6,-4,-2,-2,3,-2,4,6,9,1,10,-4,-4,7,9,-4,6,5,-4,-8,8,-1,10,-4,-7,-8,10,8,-8,-9,2,1,-9,7,-7,10,4,10,1,5,-9,-6,3,-3,8,10,-5,-9,1,-10,10,-8,3,10,-1,1,8,-1,3,3,-7,-1,-8,-7,-6,-9,-6,3,-4,1,-8,7,2,-6,-3,-8,4,1,10,10,4,2,-4,-9,-8,6,-7,-1,-1,5,5,-4,-1,-10,-4,6,-10,10,-1,-6,1,4,-3,6,1,-1,3,7,2,-6,10,6,8,7,7,10,-3,6,1,-3,-3,1,10,1,-7,-10,-7,-8,6,-6,-9,1,-3,10,-8,6,-7,-9,-5,1,-5,9,-1,1,-4,-8,-5,5,-5,2,9,-7,7,3,6,3,7,5,1,-3,3,10,-2,8,1,3,9,6,5,9,-5,5]], dtype = "int8")#candidate|5767|(1, 600)|const|int8
call_5765 = func_4578_call(relay.reshape(const_5766.astype('int8'), []), relay.reshape(const_5767.astype('int8'), [10, 5, 12]), )
call_5768 = func_4578_call(relay.reshape(const_5766.astype('int8'), []), relay.reshape(const_5767.astype('int8'), [10, 5, 12]), )
bop_5774 = relay.less_equal(uop_5739.astype('bool'), relay.reshape(call_5729.astype('bool'), relay.shape_of(uop_5739))) # shape=(2, 11, 8)
bop_5777 = relay.less_equal(uop_5741.astype('bool'), relay.reshape(call_5731.astype('bool'), relay.shape_of(uop_5741))) # shape=(2, 11, 8)
output = relay.Tuple([call_5708,const_5730,call_5751,const_5752,bop_5758,call_5765,const_5766,const_5767,bop_5774,])
output2 = relay.Tuple([call_5709,const_5730,call_5753,const_5752,bop_5761,call_5768,const_5766,const_5767,bop_5777,])
func_5789 = relay.Function([], output)
mod['func_5789'] = func_5789
mod = relay.transform.InferType()(mod)
mutated_mod['func_5789'] = func_5789
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5789_call = mutated_mod.get_global_var('func_5789')
call_5790 = func_5789_call()
output = call_5790
func_5791 = relay.Function([], output)
mutated_mod['func_5791'] = func_5791
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5803 = relay.const([[[-3,-6,2,-5,-10,6,9,3,-9,-8,-10],[7,8,7,4,-5,-4,1,5,-4,-8,-6],[-4,-8,4,1,1,-3,9,-2,7,1,-10],[-9,10,-1,6,5,6,4,1,5,-5,-1]],[[-2,9,-2,-3,5,-9,-9,-5,-8,2,-4],[-6,-4,-7,1,5,-2,-3,9,1,1,-10],[10,3,6,4,4,6,-10,8,2,-7,2],[-1,7,2,1,8,7,-1,-7,-2,-2,-10]],[[1,8,-3,-8,-6,-3,-10,-2,-9,2,10],[-1,-6,-7,-3,-5,-4,10,9,-2,8,9],[-2,-6,-1,-9,4,1,4,10,-4,-4,9],[8,1,-4,-7,6,6,-10,-2,2,-8,-8]],[[1,-10,5,7,-7,6,7,8,5,-3,5],[9,-4,-7,-4,-7,-3,1,-10,-5,-5,6],[1,6,-5,6,-4,-1,-8,3,1,8,-6],[3,-9,-4,9,6,3,5,-3,-9,-6,5]],[[9,7,-7,-6,-3,-10,9,-7,-5,8,7],[5,-4,8,7,7,1,-5,-6,3,2,-2],[-9,-1,3,4,5,-1,4,-1,3,6,-2],[4,4,7,-1,8,1,-8,-1,6,10,4]],[[-7,6,5,-3,2,4,5,3,4,9,3],[2,8,9,-7,5,-8,-3,-10,9,-6,-10],[-6,-8,-8,-8,4,4,-7,-3,6,6,6],[8,-10,2,3,8,6,-2,4,-5,7,4]],[[4,6,-3,7,-6,9,-3,-1,-2,-6,4],[3,5,8,-1,5,10,-9,-6,4,1,-7],[2,-9,-6,3,2,-9,7,-10,-10,6,-8],[2,-1,-7,8,7,1,-6,-2,8,6,2]]], dtype = "int64")#candidate|5803|(7, 4, 11)|const|int64
var_5804 = relay.var("var_5804", dtype = "int64", shape = (7, 4, 11))#candidate|5804|(7, 4, 11)|var|int64
bop_5805 = relay.greater(const_5803.astype('bool'), relay.reshape(var_5804.astype('bool'), relay.shape_of(const_5803))) # shape=(7, 4, 11)
func_1748_call = mod.get_global_var('func_1748')
func_1750_call = mutated_mod.get_global_var('func_1750')
const_5809 = relay.const(-3.048504, dtype = "float32")#candidate|5809|()|const|float32
call_5808 = relay.TupleGetItem(func_1748_call(relay.reshape(const_5809.astype('float32'), [])), 0)
call_5810 = relay.TupleGetItem(func_1750_call(relay.reshape(const_5809.astype('float32'), [])), 0)
bop_5818 = relay.minimum(bop_5805.astype('uint8'), relay.reshape(var_5804.astype('uint8'), relay.shape_of(bop_5805))) # shape=(7, 4, 11)
output = relay.Tuple([call_5808,const_5809,bop_5818,])
output2 = relay.Tuple([call_5810,const_5809,bop_5818,])
func_5823 = relay.Function([var_5804,], output)
mod['func_5823'] = func_5823
mod = relay.transform.InferType()(mod)
var_5824 = relay.var("var_5824", dtype = "int64", shape = (7, 4, 11))#candidate|5824|(7, 4, 11)|var|int64
output = func_5823(var_5824)
func_5825 = relay.Function([var_5824], output)
mutated_mod['func_5825'] = func_5825
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5838 = relay.var("var_5838", dtype = "int8", shape = (8, 5, 6))#candidate|5838|(8, 5, 6)|var|int8
var_5839 = relay.var("var_5839", dtype = "int8", shape = (8, 5, 6))#candidate|5839|(8, 5, 6)|var|int8
bop_5840 = relay.bitwise_xor(var_5838.astype('int8'), relay.reshape(var_5839.astype('int8'), relay.shape_of(var_5838))) # shape=(8, 5, 6)
func_1341_call = mod.get_global_var('func_1341')
func_1344_call = mutated_mod.get_global_var('func_1344')
const_5849 = relay.const([[10],[-2],[4],[9],[8],[6],[4],[5],[4],[-7],[-3],[3],[-6],[4],[7],[-10],[9],[1],[-9],[-5],[6],[5],[1],[-10],[-1],[10],[-9],[-3],[3],[4],[9],[-9],[7],[6],[-10],[5],[4],[-6],[9],[10],[4],[-8],[-2],[-10],[8],[7],[8],[-10],[3],[3],[6],[-9],[-9],[5],[-4],[9],[-4],[3],[-8],[3],[4],[7],[-5],[9],[10],[-3],[-3],[7],[1],[1],[7],[-3],[9],[-9],[6],[-6],[3],[6],[-8],[-5],[-8],[-7],[3],[2],[-5],[7],[-5],[5],[8],[-2],[9],[7],[-9],[9],[10],[10],[-2],[-9],[-10],[-9],[6],[-9],[8],[-6],[9],[1],[5],[-9],[2],[6],[1],[10],[-2],[10],[-1],[-8],[-7],[-9],[-10],[-3],[4],[8],[-3],[6],[2],[9],[-9],[-9],[-9],[-2],[10],[-9],[-7],[-5],[-5],[8],[2],[1],[-1],[-5],[10],[-8],[-5],[9],[-8],[8],[2],[-8],[-8],[-6],[9],[2],[-9],[1],[9],[-7],[-1],[7],[4],[4],[10],[-3],[-9],[-9],[-1],[-10],[10],[6],[-5],[1],[4],[-5],[5],[-3],[-10],[4],[-10],[2],[7],[8],[8],[-10],[2],[-8],[-4],[2],[-9],[5],[9],[-4],[6],[10],[-4],[-5],[4],[10],[-3],[-8],[8],[-1],[7],[2],[-10],[-1],[-6],[9],[4],[8],[-2],[8],[8],[5],[8],[-4],[1],[3],[-1],[-5],[2],[10],[-2],[10],[10],[3],[-2],[-7],[-1],[-2],[6],[-7],[5],[7],[5],[-7],[-10],[6],[7],[8],[-7],[1],[-4],[-2],[9],[-3],[-1],[-3],[10],[-10],[-4],[5],[3],[-5]], dtype = "int32")#candidate|5849|(252, 1)|const|int32
const_5850 = relay.const([-3.144518,-7.318723,-3.595002,-3.203788,-6.665237,2.345267,8.488878,1.958508,-3.167874,4.701161,2.192494,-7.701309,-4.937156,8.563206,6.143266,4.051055,-5.887175,7.771316,4.884739,-1.101327,-2.894436,-0.187896,4.548659,7.041070,-1.124960,-4.613940,6.242977,0.180611,0.521351,6.032608,-6.182920,-7.993107,-4.958991,2.784500,2.151597,8.858906,0.684018,-7.640884,4.693458,-8.185096,-7.356599,2.350321,-8.294939,-7.093575,-4.636432,-9.645648,-8.184680,9.900714,-0.265341,-4.199637,-5.466492,-8.992528,-2.413495,2.541491,-3.057224,1.954115,-9.375664,-3.457805,0.509464,-8.862582,-8.654906,0.439117,0.707151,-0.933157,1.643246,0.802473,-3.706557,-0.487835,-3.189912,7.991668,3.182072,-5.937258,6.337164,-2.965508,0.546147,-2.003718,-2.329613,-1.199959,2.609920,0.714157,7.522964,-5.639322,-0.014698,-4.549747,-2.405038,4.072188,7.802159,7.648530,-1.833480,7.933026,-8.325481,-9.054343,6.542600,-7.413423,3.242464,-8.617946,0.526288,-4.489822,8.511872,-1.036181,-4.102228,1.091924,7.618141,2.036789,3.329764,6.751783,-8.603986,-2.567810,-2.794424,-8.829839,-0.665130,3.087677,-6.315014,-3.554262,-2.353580,1.364146,-9.359211,-5.687254,-6.283488,-1.079335,9.718890,8.008877,3.856257,0.627901,9.362235,9.297163,-1.962229,0.731294,-5.637784,-1.576682,-7.317796,-7.752898,7.633889,1.954341,-7.263639,2.160577,5.146365,9.955514,-6.045638,0.100873,7.324129,8.515024,6.093391,-2.292095,-9.747802,-9.659509,-7.230344,-0.875023,-6.568272,2.261066,8.511064,-9.215430,-7.886998,7.568552,-1.492449,-4.242823,7.700754,-1.572457,-9.749064,-6.841751,3.737534,1.470502,8.311676,7.354637,4.576897,-7.843309,7.395662,-6.718099,8.980345,-0.478255,-4.886439,2.195197,9.557642,-0.832311,-1.992520,-9.863784,5.341225,8.514857,4.697392,-0.513145,-0.940127,7.676745,8.850256,1.390386,3.258784,6.104719,-1.885731,3.345862,-8.002934,2.954120,5.937307,-2.547517,1.600396,0.483182,3.100977,-7.259060,3.663928,0.699979,9.503995,0.790679,4.306615,-8.999984,3.379817,0.231058,5.572760,-8.120320,-5.037846,2.315598,-9.088630,0.054837,3.935498,7.657900,0.029651,1.992255,2.683739,-7.387909,0.152913,-4.842326,-3.975990,-3.939913,-0.929392,-3.638745,-7.956559,0.031334,1.083075,-5.352891,-4.024320,8.912136,-6.014497,-1.485066,4.407835,-3.691481,7.300803,2.176861,-2.380514,2.218180,-6.770172,-0.401472,9.258501,3.056926,-4.311924,7.715321,-0.432550,-4.123413,-3.131845,-5.959925,5.227308,-0.483638,-0.064179,8.701761,-7.832814,9.388383,-5.649893,1.181494,2.533525,-7.775493,-7.200625,-4.265620,-0.887812,9.363170,5.706805,-1.369226,5.977636,4.063543,-5.558763,-7.836067,1.387388,1.154865,1.818270,-5.010174,-0.737943,-3.914380,-5.255515,9.276562,-1.454787,9.570059,-9.641779,-4.949920,9.438067,5.383668,-9.381495,-1.609903,-1.642283,-8.789840,-9.333488,-5.335547,0.689644,1.208025,-3.024030,1.446438,7.589190,-7.621711,-6.120987,1.628093,1.681489,-5.457881,3.817923,6.327240,-6.208342,4.207304,-1.617282,2.898831,5.927539,-0.616092,6.020125,-1.266825,-1.548801,4.185863,3.034479,-4.151407,4.721856,4.026967,7.482228,-7.631349,-9.933717,-6.252803,-7.222186,-0.818400,-7.239891,3.298476,-3.110917,7.281632,-0.730200,-6.930800,1.003554,-1.665034,0.476837,5.286981,3.711181,-2.733007,-4.978007,-0.923413,6.686218,-0.470364,0.628781,8.838163,6.433633,1.538655,3.490401,1.454682,-9.379141,-2.864213,3.611540,6.362564,9.205535,-2.903998,-3.193093,-7.906731,-9.451556,-4.726922,-4.808795,2.617596,-2.462735,-5.030496,-5.723845,-2.565488,8.854866,-0.176129,4.837081,4.432596,-3.488381,-8.448933,0.355635,-9.338254,5.061246,5.601031,-2.155668,4.632346,0.201609,3.793871,9.384061,8.291103,-1.653911,-6.675170,7.712973,-1.076317,6.119626,-8.799099,-4.016997,-4.446324,4.604004,5.689230,7.894554,-6.551140,-9.720779,-5.872310,-1.940701,3.092902,-0.281899,-3.875546,4.976737,2.094003,2.262284,6.591645,-4.249769,7.614557,-4.407319,5.528624,3.645140,-2.701516,9.811904,4.045366,-2.830935,-8.199417,-1.532036,-3.320455,-4.168267,8.832498,-1.671067,0.629593,-1.738469,-4.441547,1.089464,-9.193454,-0.012702,4.505784,-5.145906,2.498808,7.177873,2.378571,-3.319080,1.802556,4.020570,-8.433404,-9.557231,-8.563799,-1.001358,5.796117,-4.722835,-7.427201,-4.226752,2.967767,-4.855847,-9.310069,-4.646425,-3.814997,5.160048,6.053644,-7.764587,-2.587855,5.810158,9.728538,-7.085510,-4.174911,6.450588,9.196398,-9.454769,-3.780298,4.756524,-1.017651,-2.564821,-5.465089,-5.553992,-3.511719,1.780165,4.246997,3.038149,-8.639212,4.561320,-0.674981,4.355356,3.230673,-0.816855,-2.852842,-5.272058,-0.144313,3.932657,-4.157611,-4.774228,-4.310315,-5.042314,1.611255,8.352933,9.136068,-1.158856,0.522286,3.499267,8.631117,-6.640541,9.143755,-6.084753,0.154912,-7.515002,2.779897,-5.609705,-5.923091,-9.096497,-7.193995,4.127940,-3.127164,2.607036,6.708937,-4.851046,8.112823,-6.289561,9.519262,-6.842406,4.519156,8.157457,2.476669,-8.895923,-7.941695,1.340838,-9.631854,-3.244793,-9.163985,-9.253633,-4.697034,-7.840859,6.425793,-1.714103,5.362007,3.555990,1.905466,-9.027080,-3.748353,-9.752802,9.803212,1.887685,-0.889218,-9.146179,-9.217446,-9.371469,-4.395938,-6.838079,4.685625,-9.154235,5.230116,0.307788,-1.438836,4.803741,0.848186,4.904747,-2.873151,-3.267529,-7.596827,2.437009,-3.373742,7.828297,2.809434,-7.870398,-8.859585,7.075096,1.346639,-0.361371,-3.153626,-6.884286,9.205107,-4.587271,1.683800,-7.765418,-3.925624,-0.461327,4.479526,5.989750,8.534709,-6.392443,-6.007970,6.223987,-0.731669,-9.657480,3.082983,-9.212460,-0.199980,-0.493342,-7.986492,-8.294649,9.279845,3.934962,-0.340383,5.957282,-4.962844,-5.773037,7.362583,-1.102343,0.296980,3.658174,-5.702309,-4.466083,-9.299429,-5.790191,7.337293,8.448519,6.218737,-0.553479,7.430671,7.722365,0.595746,3.764002,1.962132,-0.576448,-3.494272,9.336719,-7.070980,8.016678,5.505000,1.617809,-6.296409,4.139651,5.935705,-4.402377,0.134174,-2.669606,4.687667,6.546708,-0.728641,2.946479,1.976250,6.132144,-3.844744,1.615178,-1.973120,7.435255,2.647447,-7.636865,-4.153779,-2.839731,-6.888681,-5.059967,-9.708108,-9.599224,6.879866,7.643375,-8.031098,-7.051116,5.851363,-4.290801,-2.677424,8.920864,-5.852538,-7.749271,-7.005261,-5.681973,-3.166215,-7.681713,7.345485,4.835082,-1.552827,1.776675,3.129803,-8.987546,2.679797,-5.129701,-7.456641,-7.754751,9.238923,5.739134,2.986474,-2.431483,-2.302023,-0.856736,8.340034,-6.136627,-2.419152,-3.067892,-5.071274,-8.131855,-1.426145,6.647990,-7.616246,5.234230,2.725820,7.932139,7.592908,-1.057888,-2.515245,7.629352,-2.917846,-8.410621,6.715422,-9.496734,6.742709,-1.318982,8.537815,-2.289935,4.534223,4.728564,-0.585591,1.875124,-3.670191,6.696966,-7.261190,-6.575223,-1.095959,5.010255,7.109214,1.238818,-1.401395,-5.046253,-5.348704,-3.904853,0.779151,-5.563095,-5.846773,4.736330,4.808330,-9.007077,7.371122,-3.552201,3.005613,5.440955,1.328795,3.997762,-6.334357,3.422458,-2.014673,-3.720799,9.646584,0.835255,-1.770886,-7.016777,6.714614,7.010650,1.517908,-9.424683,1.457942,5.814390,4.209054,9.369139,2.779497,-4.052994,-4.198770,8.837864,3.517860,0.262932,4.430552,3.178853,-0.254296,4.435913,-5.451893,-1.577073,7.583236,-5.996571,-6.516918,9.028021,-4.677117,6.234319,-4.648869,-7.044082,2.089382,-2.979511,8.979803,2.940995,-9.008917,9.265020,1.785708,0.107497,4.175489,4.075152,8.374009,9.479464,-7.708706,-3.181865,8.149055,-0.260237,-6.616862,5.596867,-6.115725,-0.150046,5.464322,6.148766,7.752287,-3.915559,-6.549959,1.674321,-9.165883,4.462539,2.213443,4.758299,-9.154764,-7.441560,-0.981124,-5.903015,-9.970312,-2.423573,-5.169117,-3.576005,-1.336048,-4.736398,-4.280837,-8.220818,4.115213,3.278716,9.698663,9.898563,-9.155224,-6.306924,-9.793254,8.550358,0.480833,-4.276513,3.246926,-6.593947,3.608189,-2.900712,-0.770645,-3.832400,-4.931399,-1.975880,1.257795,3.967712,6.268794,-5.700873,-6.389606,2.792933,7.750345,7.045341,-9.781077,-2.009460,8.031945,-1.565829,3.261333,3.542696,-0.537024,0.729064,7.983294,-8.825580,0.871965,-0.510629,-6.566610,6.721333,-9.480206,2.400391,-3.292604,-2.372092,-1.807303,5.218206,-4.700924,-6.256178,4.873047,-9.037620,-6.250823,9.071564,4.096363,-7.333301,9.958873,-8.782785,-4.899822,1.834734,2.923557,-6.408603,-3.553359,-7.664573,-9.003411,1.225966,-4.412635,7.240054,-6.260804,-4.351219,-4.984043,-3.591304,1.539230,1.666563,-9.374404,-4.609727,4.347219,1.388543,3.898944,-2.497934,-7.099471,5.575641,9.550625,-1.640712,0.760521,5.691051,3.132750,-9.322365,-8.402985,-9.895522,-0.641133,8.559518,-0.289450,9.909216,-5.207830,4.897646,5.524848,0.857953,6.048071,3.993425,0.410818,1.021178,-1.813789,7.526821,7.362354,7.133101,-4.493316,7.833992,7.317025,-5.108183,-2.503636,7.539780,-4.100041,-0.853597,-2.783921,3.865612,0.440110,-3.835170,-8.165778,-3.929585,4.479547,5.058536,-4.333690,-4.007088,4.647576,3.411595,2.781151,7.542307,-1.926939,4.847220,4.450692,-1.384163,5.597583,-4.336039,-5.868582,-2.321919,-0.585156,2.411840,-7.708845,4.828381,2.662969,-9.170917,0.305091,-0.471283,0.182401,-7.282708,-6.678203,8.736752,5.797616,1.949268,0.624663,5.946125,5.693538,-9.234776,5.937588,5.681873,6.290685,2.296914,-7.661388,-5.436921,4.835205,-5.609559,0.715623,-9.810176,-4.452871,-3.926902,4.135236,2.751745,-2.946593,-1.761723,9.599461,-1.547158,1.276880,7.719534,-3.867823,-5.324797,-9.651139,8.966155,-1.770420,-4.079392,-9.485526,-9.245371,7.328941,-1.037267,-5.757220,0.451794,6.926365,-2.018335,1.160084,-1.113802,1.558383,2.732294,8.321918,2.241176,-2.295229,-0.588184,-1.129980,-2.799923,1.958431,4.530366,-3.998620,4.325464,2.957266,-4.266732,-7.993500,-7.436864,1.250062,3.984171,-4.102970,2.772759,3.309677,0.654045,-6.376729,0.306035,7.065996,9.208636,0.414654,8.577633,-8.919400,3.500770,-9.052610,-5.929522,1.805633,-8.576139,-7.578113,5.705157,-0.153191,8.984295,-4.757254,-2.616709,-4.965764,3.418397,-5.872818,-2.315975,2.324263,3.635233,7.063083,2.290486,-8.430102,-1.513388,1.583185,-7.103001,3.969487,5.935747,-6.842189,1.566440,8.504408,-3.805316,1.755544,8.998655,-7.328999,-9.128037,-5.082528,-0.623852,8.250536,-2.551719,-1.582444,-0.290969,-2.521507,-1.129418,9.004613,9.160843,-2.555031,0.208411,-8.975557,-3.993788,6.956384,-1.010123,4.887397,-3.215953,-7.078075,6.439089,4.071696,-0.334521,0.956536,-1.747399,-7.241196,-3.292015,1.852436,-1.149698,-2.350213,-6.064735,6.551628,9.147590,-2.234505,5.238094,-2.065649,4.750220,1.736859,-5.220681,-1.220698,5.347013,-8.724085,-2.300732,1.380829,-6.582813,5.437495,-5.024455,0.384129,9.394830,9.932557,-5.242213,-3.371454,-7.223069,1.897052,-6.238791,8.694258,-1.285668,0.374373,-8.655750,2.196462,-9.195193,6.214283,3.771046,6.057382,-3.698726,-0.786951,-0.003539,9.362826,-8.563628,2.933119,-1.545512,-5.155668,2.201060,7.090799,7.632528,-4.163103,-1.012878,-2.324142,-3.234830,-4.825881,-5.972483,-7.843096,9.218280,1.880732,-2.157689,1.906741,-0.596355,-8.628479,8.298608,8.659470,-8.353180,4.058021,9.530876,4.717387,9.467367,0.238279,-3.756472,-9.229092,0.818547,4.848038,0.193576,-9.127907,-7.440454,8.879609,6.393169,-7.637621,-0.791520,-8.765868,8.322641,1.800939,3.129601,0.917299,-9.122017,-8.005090,1.458232,-1.338998,-7.824237,-1.677591,8.154220,-5.280955,-8.770020,-4.613555,-9.257614,9.372806,-4.247323,-0.194934,1.712411,8.599776,-7.480267,6.964404,8.132492,-9.352581,-5.032216,0.302265,-2.070546,-5.687561,-1.522361,5.962186,9.845563,6.666724,6.895895,-8.368722,6.931859,9.154304,5.179849,8.123650,-4.671134,-6.485466,1.498389,-5.067417,5.395218,-2.741698,8.746903,2.915486,-9.611460,3.233028,-1.685775,-5.448557,2.037741,5.778418,-6.115346,-2.810816,-0.590561,-9.694807,-9.213244,2.127224,7.919746,4.338687,3.468455,-7.895075,0.268724,-6.040635,4.163864,7.596539,-4.323106,3.987086,-3.316458,6.746842,-9.589316,-5.341869,-2.820510,-0.266683,8.352863,-5.591275,-8.578539,3.105455,-6.095417,-8.601230,-4.395761,7.169900,-5.013234,-7.167488,-0.066208,-4.799372,0.269973,8.464074,-5.798426,1.162638,1.795293,5.542067,-7.836004,-4.994917,-2.393490,-1.784394,-8.453614,4.729322,-1.103680,7.339685,3.633419,5.018318,-5.029608,-2.661039,3.419832,9.609674,2.722021,-0.557086,1.497441,6.364448,2.477574,-8.573668,9.978816,0.890843,9.088305,-5.603550,-8.848197,7.788181,-6.349495,1.415667,-2.274474,-3.649222,6.771469,8.394385,1.191862,-1.617180,0.778108,1.184211,-4.116311,-3.480517,4.358315,-8.185507,8.772072,9.358860,0.535099,9.893294,8.895290,-7.238883,-1.891205,4.505060,-0.227700,5.901323,-2.219239,-5.512743,6.074789,1.022095,4.101044,-7.170120,2.616209,-9.172354,-9.000226,-1.784762,4.901506,0.781419,9.076447,-3.596851,-6.506087,2.654410,-1.714632,-4.232387,-6.432727,-4.372864,1.617354,-5.508500,-7.710782,-9.824385,-9.539450,-4.317949,1.872679,-1.108057,-8.193723,-0.087594,-1.240678,-2.760116,9.249269,-0.441541,-3.634704,8.477944,9.897394,-2.809792,-4.639195,-2.776253,-3.323220,-6.786466,-9.161595,-4.158856,3.527540,-6.791922,-2.302928,-7.303170,5.923364,4.147333,-4.180426,1.510492,3.276020,6.366655,-6.250010,-4.151131,4.439164,-0.274494,5.592035,-8.699753,7.732142,-1.514792,6.900374,1.889153,0.412604,-0.973941,0.567788,9.660726,-5.593917,-8.817935,3.327682,8.550683,-1.885060,-0.953379,-2.993706,-7.551003,2.738148,3.523458,-8.534360,9.317558,1.712203,1.285301,-1.793747,8.216322,5.610399,6.953245,7.625733,7.343776,6.773993,6.434504,7.283647,8.978108,7.679875,4.010981,-0.361902,4.902158,3.242566,-2.668789,-1.098796,-4.494218,-4.759390,-4.983541,-3.301974,4.378783,7.987123,4.037262,-5.337678,-9.363055,8.189694,4.916814,-2.843946,0.556867,4.571814,0.596080,-7.463504,-6.532443,-2.927236,-1.917562,-4.594645,-9.217931,-2.717075,-8.001799,-7.914296,-7.730009,3.139465,3.914295,8.831059,3.344333,3.223247,-6.373118,-2.188878,-1.823446,1.694811,6.943178,-8.784477,8.869955,7.177192,8.560617,-6.506370,4.193358,-2.633361,-2.719631,3.421882,-4.502784,-0.122682,-9.299407,0.190406,1.978431,7.060137,1.101310,-4.129798,1.215243,-3.334289,-4.911305,-9.921180,-4.327481,-9.761758,-7.004592,-1.381267,-3.658011,8.577506,7.970525,9.110262,3.667394,7.587886,-2.446935,-6.095043,7.213143,5.689521,8.023824,7.652204,-1.528512,-3.794808,-8.329230,2.981705,-3.272416,4.684108,-2.510361,-5.732076,-5.733874,-9.043569,-9.856377,-1.241142,0.700028,5.173747,3.621271,7.375319,-4.452292,9.870985,-0.455134,-4.887083,8.617424,6.390096,-2.650565,-8.641028,0.267360,-9.717627,6.308350,-4.767497,-8.950195,2.518768,-0.292709,8.384464,8.309237,6.966623,4.668202,-1.126035,-1.643099,-3.842917,1.004525,9.654665,9.885973,-8.382640,-2.916590,-3.332341,-4.367029,-6.577170,-6.735446,-5.292875,-4.695314,6.988054,0.093432,6.837638,9.041763,-5.560931,-5.366490,-0.711250,0.404082,-2.625824,8.348690,-5.743372,-7.085985,-3.190179,-4.976474,-2.375978,1.261073,2.344350,6.667818,-4.847869,-0.938937,-6.210348,-1.746202,0.280232,1.158934,8.090840,-3.412596,1.180028,-9.950476,0.144251,-3.399561,-8.401324,3.335104,-0.287320,-5.531997,-2.851686,2.858015,8.931967,7.187885,-6.850242,-1.136224,0.001051,6.843258,9.708328,-0.010967,8.127629,2.504103,-4.698588,9.742684,3.527112,8.654190,-0.985565,-7.931351,-6.329985,-5.392917,4.798164,-2.123645,9.564942,4.639683,-4.863335,0.235441,-2.053811,3.871891,-6.289474,3.119833,-2.699160,9.548456,4.605435,-5.912426,5.578519,-4.639374,8.889608,3.500250,3.304626,9.102078,-0.200324,0.971656,2.841033,-9.799199,3.590399,-2.892767,-0.350975,-7.045031,9.051048,-4.028896,-8.653481,9.218246,6.531216,-2.535079,3.580344,-9.277304,8.180854,-9.978586,-0.672892,-7.812277,-9.227925,5.725934,-2.305547,3.063405,-6.788938,-5.300791,-9.703000,-6.760173,-9.627814,-4.851508,2.782825,2.934092,-7.900760,0.574359,-7.642503,-2.735385,-8.532111,-1.879779,-7.022090,8.709039,0.341195,0.372944,6.301767,6.543164,-9.931081,-7.042771,3.661479,-9.876027,6.847766,-6.486184,4.236506,4.600643,8.905838,-8.261623,9.688931,-0.701778,0.532952,-2.675778,-9.669337,-1.682070,-6.784963,-9.372107,4.308885,6.420363,-6.467422,-5.748766,2.806557,-2.590743,1.961335,-1.224931,-0.059332,3.229556,-8.233574,-7.783825,-1.893906,7.881501,0.442663,-7.068025,5.899784,-4.472835,9.592477,3.522989,-7.335445,3.392291,4.219188,-9.456201,0.235797,0.568935,7.151329,-5.386787,3.672234,-9.919506,2.008497,7.376596,0.391367,-7.480693,-2.841722,5.276629,5.373207,9.570885,-3.785971,-4.774394,3.125892,6.722902,-8.274117,-1.913488,9.808254,-8.795613,6.117499,2.251938,6.493614,-7.135329,-7.254684,-9.617985,-5.935451,-9.734124,6.955878,-0.736950,-3.013307,-5.889478,4.532547,-5.159308,0.314979,8.669957,-7.287658,0.799723,1.702453,-4.523703,2.933651,0.597623,-7.531624,-8.442031,2.702550,-3.513484,-7.186382,-1.714986,-8.791671,5.159711,9.415172,-0.421617,8.812928,-9.173681,6.219352,-2.506395,7.695140,9.512065,8.884374,-0.494445,-1.124866,1.462390,4.418227,6.165772,-1.131753,2.662460,5.168139,-3.165687,-6.073253,3.491508,3.357069,-5.760636,-6.916356,-5.680863,-4.881722,-2.922531,6.434275,9.912702,6.597097,-7.782840,4.783130,7.120096,-3.760967,-8.305997,-8.247261,-9.981827,1.211937,0.282037,-7.218179,-4.550024,-3.345651,-5.668303,-0.188547], dtype = "float32")#candidate|5850|(1755,)|const|float32
call_5848 = relay.TupleGetItem(func_1341_call(relay.reshape(const_5849.astype('int32'), [252,]), relay.reshape(const_5850.astype('float32'), [1755,]), ), 1)
call_5851 = relay.TupleGetItem(func_1344_call(relay.reshape(const_5849.astype('int32'), [252,]), relay.reshape(const_5850.astype('float32'), [1755,]), ), 1)
bop_5868 = relay.less(const_5850.astype('bool'), const_5849.astype('bool')) # shape=(252, 1755)
func_1423_call = mod.get_global_var('func_1423')
func_1426_call = mutated_mod.get_global_var('func_1426')
const_5873 = relay.const([-0.772721,-3.474489,8.378523,7.757956,1.766545,-9.313045,-7.582482,-1.557001,4.254295,0.220377,9.776114,4.945539,3.099172,2.491679,-9.812085,8.191919,-8.493288,3.549369,2.799522,-5.098734,-8.537874,-4.262581,-3.162728,9.692810,2.381062,7.739403,8.409038,5.186092,4.909160,1.931319,3.342094,1.844215,8.238462,4.158798,9.250983,8.881221,-0.004058,9.044579,-5.790425,-9.083824,2.201338,6.331455,-2.477222,1.105204,1.754505,8.277276,-2.963686,-8.695409,6.501294,-9.106357,8.026342,-1.424930,-8.760599,-5.244986,-6.922272,-3.181538,8.996352,2.743988,0.051421,1.985365,9.902992,2.390265,8.688144,2.887603,5.578704,-8.351038,-6.867759,-0.500988,-8.765078,6.491635,8.580805,-2.547053,6.048283,-1.130990,-3.646576,4.391072,-0.665881,9.122597,-6.603224,-8.632009,6.248379,-2.905388,-7.690827,-0.978605,-6.525332,9.635862,2.632861,-2.814814,5.703736,0.892868,-5.646560,-3.927263,7.386505,1.941783,-3.658892,9.188022,-4.658284,4.180474,-1.797610,7.364891,-2.051272,-3.629782,-6.052133,-5.867481,4.129847,8.040407,7.601877,-9.772394,-9.712913,-5.247094,-2.736125,-4.759022,-7.252921,8.251061,1.913778,7.204735,9.751862,9.516164,-0.389964,-5.375239,-4.936937,5.990556,6.022942,-2.722899,2.972125,-1.649740,9.384852,-2.870936,9.468744,-7.741957,-6.088373,-6.735979,-1.058709,1.075102,5.171776,-7.466913,-4.163607,9.655245,-9.317744,5.592308,0.295623,9.638639,-9.171091,-5.001655,8.907552,-9.448124,-7.466551,3.824124,-1.744756,3.558675,-9.797971,2.714732,7.846209,-3.528474,9.144527,-4.001219,-4.249288,3.927809,5.290918,-5.197798], dtype = "float64")#candidate|5873|(160,)|const|float64
call_5872 = func_1423_call(relay.reshape(const_5873.astype('float64'), [16, 5, 2]))
call_5874 = func_1423_call(relay.reshape(const_5873.astype('float64'), [16, 5, 2]))
uop_5885 = relay.log2(const_5850.astype('float64')) # shape=(1755,)
bop_5888 = relay.greater(bop_5868.astype('bool'), const_5850.astype('bool')) # shape=(252, 1755)
bop_5902 = relay.bitwise_xor(uop_5885.astype('uint32'), relay.reshape(call_5848.astype('uint32'), relay.shape_of(uop_5885))) # shape=(1755,)
bop_5905 = relay.bitwise_xor(uop_5885.astype('uint32'), relay.reshape(call_5851.astype('uint32'), relay.shape_of(uop_5885))) # shape=(1755,)
uop_5924 = relay.acosh(bop_5902.astype('float64')) # shape=(1755,)
uop_5926 = relay.acosh(bop_5905.astype('float64')) # shape=(1755,)
func_2626_call = mod.get_global_var('func_2626')
func_2632_call = mutated_mod.get_global_var('func_2632')
var_5933 = relay.var("var_5933", dtype = "uint8", shape = (1024,))#candidate|5933|(1024,)|var|uint8
var_5934 = relay.var("var_5934", dtype = "uint8", shape = (3120,))#candidate|5934|(3120,)|var|uint8
const_5935 = relay.const([5,-4,-7,-4,2,-6,5,8,-8,7,-10,8,7,-7,-7,1,-10,-10,-8,1,2,2,-1,-7,3,-7,-6,-4,8,-7,-10,6,3,-8,-4,-2,-8,4,-7,8,-5,-2,1,-2,-9,-3,-9,-10,9,-5,9,-9,-4,-6,-4,-10,1,-9,-7,-3,-4,-7,7,7,-7,9,2,5,-1,-6,5,-5,7,1,7,-2,10,5,-1,3,7,-6,-8,-4,9,-5,7,3,3,9,7,2,5,7,10,-3,-4,7,-7,-2,-2,-5,6,-4,-1,1,-6,-9,10,6,8,8,-8,5,-5,-6,-3,-5,-6,-7,2,8,1,-1,-5,-3,-8,-6,-6,-2,7,6,-8,8,2,2,3,3,7,-7,3,-5,2,7,-2,9,-8,9,7,-9,-5,2,1,2,-1,2,10,5,1,-10,-3,-2,5,7,1,1,-7,3,-8,9,5,-3,9,9,-2,-2,-9,5,10,-3,8,-6,-9,-4,-6,-8,2,-6,-1,-2,-3,9,-1,-3,6,1,-2,-10,7,-7,5,-2,7,10,4,-3,6,-10,-6,-7,10,8,-4,4,2,-2,7,6,5,-5,9,5,-10,4,7,10,-9,3,9,-5,-9,10,3,3,5,9,6,1,1,1,9,7,-4,-9,8,-5,-1,4,-2,-5,4,1,8,-3,-9,8,8,4,-8,4,-9,4,4,7,4,3,4,8,-5,-4,5,-2,7,-4,1], dtype = "uint8")#candidate|5935|(275,)|const|uint8
var_5936 = relay.var("var_5936", dtype = "float32", shape = (500,))#candidate|5936|(500,)|var|float32
call_5932 = relay.TupleGetItem(func_2626_call(relay.reshape(var_5933.astype('uint8'), [1024,]), relay.reshape(var_5934.astype('uint8'), [3120,]), relay.reshape(const_5935.astype('uint8'), [275,]), relay.reshape(var_5936.astype('float32'), [10, 50]), ), 3)
call_5937 = relay.TupleGetItem(func_2632_call(relay.reshape(var_5933.astype('uint8'), [1024,]), relay.reshape(var_5934.astype('uint8'), [3120,]), relay.reshape(const_5935.astype('uint8'), [275,]), relay.reshape(var_5936.astype('float32'), [10, 50]), ), 3)
func_385_call = mod.get_global_var('func_385')
func_388_call = mutated_mod.get_global_var('func_388')
call_5942 = relay.TupleGetItem(func_385_call(relay.reshape(const_5849.astype('int32'), [4, 7, 9]), relay.reshape(call_5848.astype('float32'), [1755,]), ), 4)
call_5943 = relay.TupleGetItem(func_388_call(relay.reshape(const_5849.astype('int32'), [4, 7, 9]), relay.reshape(call_5848.astype('float32'), [1755,]), ), 4)
func_3918_call = mod.get_global_var('func_3918')
func_3920_call = mutated_mod.get_global_var('func_3920')
call_5945 = func_3918_call()
call_5946 = func_3918_call()
output = relay.Tuple([bop_5840,call_5872,const_5873,bop_5888,uop_5924,call_5932,var_5933,var_5934,const_5935,var_5936,call_5942,call_5945,])
output2 = relay.Tuple([bop_5840,call_5874,const_5873,bop_5888,uop_5926,call_5937,var_5933,var_5934,const_5935,var_5936,call_5943,call_5946,])
func_5947 = relay.Function([var_5838,var_5839,var_5933,var_5934,var_5936,], output)
mod['func_5947'] = func_5947
mod = relay.transform.InferType()(mod)
var_5948 = relay.var("var_5948", dtype = "int8", shape = (8, 5, 6))#candidate|5948|(8, 5, 6)|var|int8
var_5949 = relay.var("var_5949", dtype = "int8", shape = (8, 5, 6))#candidate|5949|(8, 5, 6)|var|int8
var_5950 = relay.var("var_5950", dtype = "uint8", shape = (1024,))#candidate|5950|(1024,)|var|uint8
var_5951 = relay.var("var_5951", dtype = "uint8", shape = (3120,))#candidate|5951|(3120,)|var|uint8
var_5952 = relay.var("var_5952", dtype = "float32", shape = (500,))#candidate|5952|(500,)|var|float32
output = func_5947(var_5948,var_5949,var_5950,var_5951,var_5952,)
func_5953 = relay.Function([var_5948,var_5949,var_5950,var_5951,var_5952,], output)
mutated_mod['func_5953'] = func_5953
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3896_call = mod.get_global_var('func_3896')
func_3898_call = mutated_mod.get_global_var('func_3898')
call_6000 = relay.TupleGetItem(func_3896_call(), 0)
call_6001 = relay.TupleGetItem(func_3898_call(), 0)
output = relay.Tuple([call_6000,])
output2 = relay.Tuple([call_6001,])
func_6003 = relay.Function([], output)
mod['func_6003'] = func_6003
mod = relay.transform.InferType()(mod)
output = func_6003()
func_6004 = relay.Function([], output)
mutated_mod['func_6004'] = func_6004
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2278_call = mod.get_global_var('func_2278')
func_2280_call = mutated_mod.get_global_var('func_2280')
call_6060 = func_2278_call()
call_6061 = func_2278_call()
var_6065 = relay.var("var_6065", dtype = "float64", shape = (2, 9, 8))#candidate|6065|(2, 9, 8)|var|float64
bop_6066 = relay.minimum(call_6060.astype('uint16'), var_6065.astype('uint16')) # shape=(2, 9, 8)
bop_6069 = relay.minimum(call_6061.astype('uint16'), var_6065.astype('uint16')) # shape=(2, 9, 8)
output = relay.Tuple([bop_6066,])
output2 = relay.Tuple([bop_6069,])
func_6076 = relay.Function([var_6065,], output)
mod['func_6076'] = func_6076
mod = relay.transform.InferType()(mod)
mutated_mod['func_6076'] = func_6076
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6077 = relay.var("var_6077", dtype = "float64", shape = (2, 9, 8))#candidate|6077|(2, 9, 8)|var|float64
func_6076_call = mutated_mod.get_global_var('func_6076')
call_6078 = func_6076_call(var_6077)
output = call_6078
func_6079 = relay.Function([var_6077], output)
mutated_mod['func_6079'] = func_6079
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2307_call = mod.get_global_var('func_2307')
func_2309_call = mutated_mod.get_global_var('func_2309')
call_6084 = relay.TupleGetItem(func_2307_call(), 0)
call_6085 = relay.TupleGetItem(func_2309_call(), 0)
func_5582_call = mod.get_global_var('func_5582')
func_5583_call = mutated_mod.get_global_var('func_5583')
call_6093 = relay.TupleGetItem(func_5582_call(), 0)
call_6094 = relay.TupleGetItem(func_5583_call(), 0)
bop_6098 = relay.logical_xor(call_6093.astype('int8'), relay.reshape(call_6084.astype('int8'), relay.shape_of(call_6093))) # shape=(2, 1, 8)
bop_6101 = relay.logical_xor(call_6094.astype('int8'), relay.reshape(call_6085.astype('int8'), relay.shape_of(call_6094))) # shape=(2, 1, 8)
output = relay.Tuple([bop_6098,])
output2 = relay.Tuple([bop_6101,])
func_6108 = relay.Function([], output)
mod['func_6108'] = func_6108
mod = relay.transform.InferType()(mod)
mutated_mod['func_6108'] = func_6108
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6108_call = mutated_mod.get_global_var('func_6108')
call_6109 = func_6108_call()
output = call_6109
func_6110 = relay.Function([], output)
mutated_mod['func_6110'] = func_6110
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4165_call = mod.get_global_var('func_4165')
func_4166_call = mutated_mod.get_global_var('func_4166')
call_6192 = func_4165_call()
call_6193 = func_4165_call()
output = relay.Tuple([call_6192,])
output2 = relay.Tuple([call_6193,])
func_6194 = relay.Function([], output)
mod['func_6194'] = func_6194
mod = relay.transform.InferType()(mod)
mutated_mod['func_6194'] = func_6194
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6194_call = mutated_mod.get_global_var('func_6194')
call_6195 = func_6194_call()
output = call_6195
func_6196 = relay.Function([], output)
mutated_mod['func_6196'] = func_6196
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4165_call = mod.get_global_var('func_4165')
func_4166_call = mutated_mod.get_global_var('func_4166')
call_6227 = func_4165_call()
call_6228 = func_4165_call()
var_6234 = relay.var("var_6234", dtype = "float32", shape = (2, 8, 8))#candidate|6234|(2, 8, 8)|var|float32
bop_6235 = relay.add(call_6227.astype('uint64'), var_6234.astype('uint64')) # shape=(2, 8, 8)
bop_6238 = relay.add(call_6228.astype('uint64'), var_6234.astype('uint64')) # shape=(2, 8, 8)
func_4323_call = mod.get_global_var('func_4323')
func_4326_call = mutated_mod.get_global_var('func_4326')
var_6240 = relay.var("var_6240", dtype = "uint64", shape = (11, 2))#candidate|6240|(11, 2)|var|uint64
call_6239 = relay.TupleGetItem(func_4323_call(relay.reshape(var_6240.astype('uint64'), [1, 2, 11])), 2)
call_6241 = relay.TupleGetItem(func_4326_call(relay.reshape(var_6240.astype('uint64'), [1, 2, 11])), 2)
bop_6245 = relay.equal(call_6227.astype('bool'), var_6234.astype('bool')) # shape=(2, 8, 8)
bop_6248 = relay.equal(call_6228.astype('bool'), var_6234.astype('bool')) # shape=(2, 8, 8)
func_4323_call = mod.get_global_var('func_4323')
func_4326_call = mutated_mod.get_global_var('func_4326')
call_6256 = relay.TupleGetItem(func_4323_call(relay.reshape(var_6240.astype('uint64'), [1, 2, 11])), 0)
call_6257 = relay.TupleGetItem(func_4326_call(relay.reshape(var_6240.astype('uint64'), [1, 2, 11])), 0)
output = relay.Tuple([bop_6235,call_6239,var_6240,bop_6245,call_6256,])
output2 = relay.Tuple([bop_6238,call_6241,var_6240,bop_6248,call_6257,])
func_6259 = relay.Function([var_6234,var_6240,], output)
mod['func_6259'] = func_6259
mod = relay.transform.InferType()(mod)
var_6260 = relay.var("var_6260", dtype = "float32", shape = (2, 8, 8))#candidate|6260|(2, 8, 8)|var|float32
var_6261 = relay.var("var_6261", dtype = "uint64", shape = (11, 2))#candidate|6261|(11, 2)|var|uint64
output = func_6259(var_6260,var_6261,)
func_6262 = relay.Function([var_6260,var_6261,], output)
mutated_mod['func_6262'] = func_6262
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3772_call = mod.get_global_var('func_3772')
func_3773_call = mutated_mod.get_global_var('func_3773')
call_6264 = relay.TupleGetItem(func_3772_call(), 0)
call_6265 = relay.TupleGetItem(func_3773_call(), 0)
output = relay.Tuple([call_6264,])
output2 = relay.Tuple([call_6265,])
func_6274 = relay.Function([], output)
mod['func_6274'] = func_6274
mod = relay.transform.InferType()(mod)
mutated_mod['func_6274'] = func_6274
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6274_call = mutated_mod.get_global_var('func_6274')
call_6275 = func_6274_call()
output = call_6275
func_6276 = relay.Function([], output)
mutated_mod['func_6276'] = func_6276
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3772_call = mod.get_global_var('func_3772')
func_3773_call = mutated_mod.get_global_var('func_3773')
call_6290 = relay.TupleGetItem(func_3772_call(), 0)
call_6291 = relay.TupleGetItem(func_3773_call(), 0)
func_6108_call = mod.get_global_var('func_6108')
func_6110_call = mutated_mod.get_global_var('func_6110')
call_6296 = relay.TupleGetItem(func_6108_call(), 0)
call_6297 = relay.TupleGetItem(func_6110_call(), 0)
func_4479_call = mod.get_global_var('func_4479')
func_4482_call = mutated_mod.get_global_var('func_4482')
const_6303 = relay.const([-2.072579,-7.544706,-4.555037,9.488452,-1.621140,0.811804,-3.467261,-6.097059,-6.825540,-1.959020,4.732048,5.114204,4.057568,-1.604074,-2.448827,4.116914,-8.819393,8.318514,-2.448235,8.282912,3.669221,5.093520,-2.774663,7.272549,8.719182,-0.888681,-4.551227,-2.060108,9.059671,1.549204,-8.087898,1.890171,-9.338792,-4.622051,4.522438,7.477890,-2.610358,-2.180805,-4.160462,-8.961409,-9.122209,-6.282450,-0.689380,-7.175896,5.716364,2.680938,-2.786732,-3.581404,7.065927,-2.531321,-8.502990,-1.394557,-8.656083,5.286581,-8.690402,-6.993950,-7.829813,2.646053,-4.654859,4.552457,4.221137,0.498717,0.087602,-6.744356,-9.082600,1.119008,-3.086463,-7.980333,8.983826,3.389929,4.500551,-0.140942,-5.285768,-4.738967,2.734089,-2.600246,-7.801017,0.440671,1.228858,-8.459136,-5.876452,-3.083111,9.808780,5.117876,8.783896,-8.518937,-4.139100,-7.036196,2.634490,8.894123,-3.424260,4.249559,-9.731753,-0.077293,2.562620,7.258264,6.282710,-0.747906,-6.270383,4.471919,0.683473,-5.121951,-6.035052,-7.722495,9.686529,-8.602619,-7.718451,-5.786453,-6.507970,-5.827164,-7.851894,0.028915,-6.707370,-5.663123,7.562741,-7.658881,-7.576803,8.559204,8.406049,-9.690789,1.773100,1.221210,-3.904151,-7.417899,-5.367391,-8.877635,5.185946,-7.395496,-8.800738,-7.394080,-5.232605,-8.012498,-4.572871,1.679014,6.549670,-4.768316,5.338523,-3.605813,-6.419116,-0.295043,-7.218283,1.407684,7.741429,9.750004,-4.072964,1.803677,-5.436608,5.539418,1.756860,-6.420157,-3.212316,-4.467489,-8.422621,-1.899086,0.946056,-5.764704,5.528580,1.431254,6.429082,-7.698696,2.532953,5.461086,7.406203,-8.513649,5.432904,-3.206040,1.621996,3.840781,9.118842,-1.664690,9.909699,-9.714354,-8.745157,8.497631,-6.494655,-3.258325,9.764685,4.835490,-0.075712,-4.366318,1.887810,-6.564402,1.152413,-7.671116,7.900736,4.274616,7.916947,3.409979,-5.018352,-3.931042,4.562848,-9.724644,-3.193067,1.087955,3.204601,-4.885050,-4.085848,4.024554,1.918675,6.722005,8.727066,4.562608,-9.297763,-0.464248,6.742320,-0.290529,7.373146,2.689709,-1.271150,1.339186,-0.876946,-1.711296,-3.768227,-5.337728,-4.037676,-9.839494,7.926680,-0.891146,-8.862788,-7.153714,3.735192,-0.090952,5.355167,-8.772040,5.965283,9.809628,-6.319904,-1.968350,2.165142,-4.741935,-0.874631,0.853309,-6.600084,-5.681485,9.265740,-0.145510,4.011507,0.997156,-1.262043,-9.712475,6.365526,-7.555569,-7.169761,-2.507968,2.917463,9.156399,8.330675,5.955400,-1.442888,9.711779,-7.470019,9.053836,-8.827979,-8.821439,-6.562396,-3.659430,-9.510572,5.735202,-5.223248,8.890577,-8.151255,2.115190,0.450682,5.250383,-4.634067,2.099602,-4.477095,-4.542837,-2.410523,-4.705543,-4.778038,-7.737047,9.517341,8.761410,-4.606063,2.807110,7.775823,-9.007813,-7.938018,-4.992843,-5.328849,1.978569,-7.680180,-8.858622,0.531553,-5.488111,3.802008,-4.468609,-4.770389,-7.668187,-9.196652,-1.682036,0.456372,9.793985,-2.324124,-1.589711,9.967166,-0.439154,-7.614807,-2.750330,9.424756,9.198016,-4.912212,7.123238,7.286493,2.136266,8.430506,2.014003,-9.575723,-1.694559,-6.656600,-9.413705,6.569523,-5.231070,5.695033,9.269942,3.470897,5.390841,-0.309508,-5.259713,9.829793,-9.696824,9.469283,6.510628,-0.313196,7.557831,-6.115282,-1.985991,-1.654036,6.308813,-6.336337,-1.387530,7.280735,5.289508,-9.460206,1.776840,0.057523,-4.213686,9.024836,-5.432282,-1.652724,5.228850,7.609464,-7.081210,-1.585083,0.028661,-5.093878,-0.481498,-8.891323,3.179190,9.750768,-5.198356,-5.267058,-7.014117,-8.067505,0.129613,-3.395518,7.565313,1.415507,7.622406,-9.755827,-5.427939,-6.534461,-0.694835,-1.294860,1.827825,2.133494,-2.258449,-4.122780,3.736344,7.312101,7.507818,6.922429,-8.455732,-1.364161,-9.550851,-2.152634,3.535598,2.858260,6.624661,-9.620702,-8.650535,-9.598003,6.575909,5.003598,4.654988,-8.228361,-5.500236,-9.744810,-6.170632,-3.837643,8.439325,0.515326,4.965057,-8.672971,-9.731524,3.216368,-1.780073,9.645945,-6.648014,3.699424,8.160459,2.007745,3.562295,-3.072178,-0.698258,3.855540,-3.678280,6.993740,7.740169,-3.559251,-3.638204,-7.245463,-9.011875,-7.303215,-6.139379,-9.024436,7.182711,6.551098,9.312621,-5.535698,-1.985016,1.718299,-2.475106,-5.996220,7.692038,6.103809,-1.116435,-6.327072,1.596873,-2.080507,-0.483647,-7.606293,-3.966351,6.203222,1.664311,0.782728,8.051160,-1.846142,1.559064,3.649814,-9.597152,-2.646035,6.793193,8.493277,-9.492698,-9.450781,-9.687391,-3.110916,9.062411,8.083316,-7.019209,-0.413746,4.925923,0.068917,-8.192996,2.272367,-2.702241,8.002549,3.446644,-8.938261,-8.908003,-4.882963,4.708675,4.155677,-6.552375,-9.804068,-4.876422,-1.084128,0.814025,-9.987210,1.593633,-9.518678,-2.569753,1.993228,-7.010470,3.962269,-8.987483,-8.240347,-1.239808,-7.105302,-0.411600,1.467793,-4.184726,-1.745556,-4.331780,1.475631,1.746967,7.210202,5.386884,8.235841,-4.853019,1.645103,-0.744456,0.057852,3.852022,-6.544719,-0.901849,-7.890019,6.875611], dtype = "float32")#candidate|6303|(500,)|const|float32
call_6302 = relay.TupleGetItem(func_4479_call(relay.reshape(const_6303.astype('float32'), [250, 2])), 2)
call_6304 = relay.TupleGetItem(func_4482_call(relay.reshape(const_6303.astype('float32'), [250, 2])), 2)
uop_6305 = relay.log(call_6302.astype('float32')) # shape=(250, 2)
uop_6307 = relay.log(call_6304.astype('float32')) # shape=(250, 2)
uop_6317 = relay.sigmoid(const_6303.astype('float64')) # shape=(500,)
var_6326 = relay.var("var_6326", dtype = "float32", shape = (250, 2))#candidate|6326|(250, 2)|var|float32
bop_6327 = relay.greater(uop_6305.astype('bool'), relay.reshape(var_6326.astype('bool'), relay.shape_of(uop_6305))) # shape=(250, 2)
bop_6330 = relay.greater(uop_6307.astype('bool'), relay.reshape(var_6326.astype('bool'), relay.shape_of(uop_6307))) # shape=(250, 2)
func_5582_call = mod.get_global_var('func_5582')
func_5583_call = mutated_mod.get_global_var('func_5583')
call_6334 = relay.TupleGetItem(func_5582_call(), 0)
call_6335 = relay.TupleGetItem(func_5583_call(), 0)
func_5166_call = mod.get_global_var('func_5166')
func_5169_call = mutated_mod.get_global_var('func_5169')
call_6343 = relay.TupleGetItem(func_5166_call(relay.reshape(call_6302.astype('float32'), [500,])), 0)
call_6344 = relay.TupleGetItem(func_5169_call(relay.reshape(call_6302.astype('float32'), [500,])), 0)
func_6003_call = mod.get_global_var('func_6003')
func_6004_call = mutated_mod.get_global_var('func_6004')
call_6357 = relay.TupleGetItem(func_6003_call(), 0)
call_6358 = relay.TupleGetItem(func_6004_call(), 0)
func_2734_call = mod.get_global_var('func_2734')
func_2736_call = mutated_mod.get_global_var('func_2736')
var_6360 = relay.var("var_6360", dtype = "int64", shape = (30, 4))#candidate|6360|(30, 4)|var|int64
call_6359 = relay.TupleGetItem(func_2734_call(relay.reshape(var_6360.astype('int64'), [120,])), 0)
call_6361 = relay.TupleGetItem(func_2736_call(relay.reshape(var_6360.astype('int64'), [120,])), 0)
uop_6365 = relay.erf(uop_6317.astype('float32')) # shape=(500,)
output = relay.Tuple([call_6290,call_6296,bop_6327,call_6334,call_6343,call_6357,call_6359,var_6360,uop_6365,])
output2 = relay.Tuple([call_6291,call_6297,bop_6330,call_6335,call_6344,call_6358,call_6361,var_6360,uop_6365,])
func_6382 = relay.Function([var_6326,var_6360,], output)
mod['func_6382'] = func_6382
mod = relay.transform.InferType()(mod)
var_6383 = relay.var("var_6383", dtype = "float32", shape = (250, 2))#candidate|6383|(250, 2)|var|float32
var_6384 = relay.var("var_6384", dtype = "int64", shape = (30, 4))#candidate|6384|(30, 4)|var|int64
output = func_6382(var_6383,var_6384,)
func_6385 = relay.Function([var_6383,var_6384,], output)
mutated_mod['func_6385'] = func_6385
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6455 = relay.var("var_6455", dtype = "bool", shape = (14, 4, 6))#candidate|6455|(14, 4, 6)|var|bool
var_6456 = relay.var("var_6456", dtype = "bool", shape = (14, 4, 6))#candidate|6456|(14, 4, 6)|var|bool
bop_6457 = relay.logical_or(var_6455.astype('bool'), relay.reshape(var_6456.astype('bool'), relay.shape_of(var_6455))) # shape=(14, 4, 6)
output = relay.Tuple([bop_6457,])
output2 = relay.Tuple([bop_6457,])
F = relay.Function([var_6455,var_6456,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_6455,var_6456,], output2)
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
