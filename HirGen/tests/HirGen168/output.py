import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
const_157 = relay.const([[[-5,-1],[4,8],[2,5],[4,7],[5,1],[7,-4],[-8,-9],[-6,10],[-7,-4],[1,-10],[3,5]],[[3,7],[9,-7],[-5,-7],[5,1],[6,-3],[-4,-2],[10,-6],[-1,2],[6,-2],[-7,-3],[10,-5]],[[-5,-6],[-10,2],[5,-7],[-9,-10],[7,-4],[1,-9],[-5,-1],[2,1],[4,6],[6,8],[-5,-6]],[[1,5],[-8,-10],[-5,9],[1,6],[-6,1],[-6,-2],[7,4],[6,-6],[-8,4],[10,-8],[4,6]],[[7,-1],[2,-1],[-8,-1],[-4,9],[-6,6],[8,3],[3,-4],[9,2],[-5,-7],[4,-5],[2,9]]], dtype = "int8")#candidate|157|(5, 11, 2)|const|int8
var_158 = relay.var("var_158", dtype = "int8", shape = (5, 11, 2))#candidate|158|(5, 11, 2)|var|int8
bop_159 = relay.add(const_157.astype('int8'), relay.reshape(var_158.astype('int8'), relay.shape_of(const_157))) # shape=(5, 11, 2)
uop_166 = relay.cosh(const_157.astype('float64')) # shape=(5, 11, 2)
output = relay.Tuple([bop_159,uop_166,])
output2 = relay.Tuple([bop_159,uop_166,])
func_173 = relay.Function([var_158,], output)
mod['func_173'] = func_173
mod = relay.transform.InferType()(mod)
var_174 = relay.var("var_174", dtype = "int8", shape = (5, 11, 2))#candidate|174|(5, 11, 2)|var|int8
output = func_173(var_174)
func_175 = relay.Function([var_174], output)
mutated_mod['func_175'] = func_175
mutated_mod = relay.transform.InferType()(mutated_mod)
const_177 = relay.const([[[-9.176967,0.312426,5.341578],[-9.475069,6.916300,8.418221],[-2.683443,3.703697,-6.867622],[5.530143,-2.294620,5.940777],[-0.590559,-8.235406,-4.675170]],[[-8.586257,-1.182419,1.336878],[-4.689802,7.821086,-6.680124],[9.451196,-7.631166,5.686267],[-9.176795,-3.220605,-4.747836],[1.270926,2.799612,-4.020506]],[[5.452817,-3.998867,-6.063428],[1.769990,8.507679,4.851749],[4.519521,-3.554098,4.228571],[-7.412472,-8.585214,-9.553851],[-9.878627,-6.861280,9.757065]],[[1.542599,8.439992,-0.307920],[3.191760,-5.640275,-8.510070],[4.109739,1.460090,8.425291],[8.173261,-0.798178,5.913756],[5.214411,-4.740761,5.912854]],[[-6.745026,-7.916127,-4.695284],[-8.207873,-6.535666,-0.447148],[-1.760107,-6.064617,3.908965],[-8.302791,-5.078222,1.347394],[9.759457,5.181497,-3.099588]]], dtype = "float64")#candidate|177|(5, 5, 3)|const|float64
uop_178 = relay.acosh(const_177.astype('float64')) # shape=(5, 5, 3)
func_173_call = mod.get_global_var('func_173')
func_175_call = mutated_mod.get_global_var('func_175')
var_192 = relay.var("var_192", dtype = "int8", shape = (110,))#candidate|192|(110,)|var|int8
call_191 = relay.TupleGetItem(func_173_call(relay.reshape(var_192.astype('int8'), [5, 11, 2])), 1)
call_193 = relay.TupleGetItem(func_175_call(relay.reshape(var_192.astype('int8'), [5, 11, 2])), 1)
func_173_call = mod.get_global_var('func_173')
func_175_call = mutated_mod.get_global_var('func_175')
call_194 = relay.TupleGetItem(func_173_call(relay.reshape(var_192.astype('int8'), [5, 11, 2])), 0)
call_195 = relay.TupleGetItem(func_175_call(relay.reshape(var_192.astype('int8'), [5, 11, 2])), 0)
func_173_call = mod.get_global_var('func_173')
func_175_call = mutated_mod.get_global_var('func_175')
call_204 = relay.TupleGetItem(func_173_call(relay.reshape(call_191.astype('int8'), [5, 11, 2])), 0)
call_205 = relay.TupleGetItem(func_175_call(relay.reshape(call_191.astype('int8'), [5, 11, 2])), 0)
func_173_call = mod.get_global_var('func_173')
func_175_call = mutated_mod.get_global_var('func_175')
call_211 = relay.TupleGetItem(func_173_call(relay.reshape(call_194.astype('int8'), [5, 11, 2])), 0)
call_212 = relay.TupleGetItem(func_175_call(relay.reshape(call_194.astype('int8'), [5, 11, 2])), 0)
output = relay.Tuple([uop_178,call_191,var_192,call_194,call_204,call_211,])
output2 = relay.Tuple([uop_178,call_193,var_192,call_195,call_205,call_212,])
func_217 = relay.Function([var_192,], output)
mod['func_217'] = func_217
mod = relay.transform.InferType()(mod)
mutated_mod['func_217'] = func_217
mutated_mod = relay.transform.InferType()(mutated_mod)
var_218 = relay.var("var_218", dtype = "int8", shape = (110,))#candidate|218|(110,)|var|int8
func_217_call = mutated_mod.get_global_var('func_217')
call_219 = func_217_call(var_218)
output = call_219
func_220 = relay.Function([var_218], output)
mutated_mod['func_220'] = func_220
mutated_mod = relay.transform.InferType()(mutated_mod)
var_244 = relay.var("var_244", dtype = "uint64", shape = (5, 10, 1))#candidate|244|(5, 10, 1)|var|uint64
const_245 = relay.const([[[-1,3,6,-9,-8,-9,9,2,10,2],[7,-6,-4,7,-2,3,2,7,7,-9],[2,3,-7,-3,-6,-10,8,9,7,-9],[3,-2,-9,4,-6,-10,-2,10,-9,-8],[-7,-5,4,-8,2,-10,3,-9,-5,-8],[-8,1,-3,-1,3,7,-8,6,-8,3],[-4,-4,-8,-9,6,4,-6,-3,-6,-1],[-4,1,-1,-1,1,-9,-8,-2,-4,9],[-8,3,10,3,10,6,-10,-5,-2,-10],[-2,-10,1,-9,4,-6,-1,-6,-5,-6]],[[1,-1,9,-4,6,-7,-2,-1,10,-8],[5,5,-3,6,10,-6,-6,-3,-5,-7],[2,9,1,-7,-9,-5,2,-10,-3,-4],[-2,3,9,4,-5,-7,5,3,8,-6],[6,1,3,5,-2,8,-1,-4,9,6],[-1,2,-3,-3,-4,7,-4,10,-10,3],[3,-7,-4,-7,-1,8,-8,-1,5,1],[4,-1,-4,6,-7,-7,-2,-7,7,1],[6,1,2,-6,-7,8,5,-10,2,7],[6,-10,-10,7,10,7,-7,-2,2,6]],[[5,1,-3,10,-6,5,-3,-2,-3,-10],[7,8,8,3,-8,-7,4,6,6,3],[5,6,4,-10,-5,9,-10,7,7,-5],[-10,-1,-10,-10,-2,-10,2,4,-4,-4],[-5,-10,-1,10,-7,-4,-7,1,-9,6],[7,-8,-4,6,7,6,4,6,4,-3],[2,2,-2,1,-6,-5,-4,2,7,7],[-8,7,-2,-7,-10,-9,-8,6,-4,1],[3,-10,3,7,10,6,-9,-9,-6,9],[-7,-2,9,-4,2,-2,-5,4,-6,8]],[[6,-5,-4,6,-3,10,3,-6,10,7],[9,-1,-6,10,5,-10,-1,6,1,9],[-6,3,-3,-4,-1,8,-2,4,-1,10],[4,5,-6,3,2,9,-3,7,-3,8],[2,6,5,2,8,-2,-3,-10,-9,-4],[4,-8,10,-10,8,9,-6,-4,8,-6],[7,9,-4,-8,-9,-3,8,10,9,-10],[-2,5,-7,10,2,-10,-2,8,5,1],[8,8,5,5,2,9,8,3,-2,1],[-8,4,1,8,-9,1,-10,7,-1,-9]],[[8,8,-3,-3,5,-2,4,-1,-9,-2],[-7,-8,-4,-6,5,-9,-5,-3,9,5],[8,4,-3,-9,-7,3,-4,3,-3,-6],[-4,5,3,8,-4,7,-2,5,10,-8],[-7,-1,1,10,4,-4,10,-8,9,-6],[-2,-4,5,-8,7,10,-8,-4,6,2],[-1,-8,8,-5,-3,2,5,-8,7,-3],[-3,-8,-5,-9,-8,9,-7,-2,3,6],[2,3,-3,-8,-8,-7,-6,-3,7,2],[-5,9,-9,9,-2,-2,-10,-2,6,5]]], dtype = "uint64")#candidate|245|(5, 10, 10)|const|uint64
bop_246 = relay.less(var_244.astype('bool'), const_245.astype('bool')) # shape=(5, 10, 10)
func_217_call = mod.get_global_var('func_217')
func_220_call = mutated_mod.get_global_var('func_220')
var_262 = relay.var("var_262", dtype = "int8", shape = (110,))#candidate|262|(110,)|var|int8
call_261 = relay.TupleGetItem(func_217_call(relay.reshape(var_262.astype('int8'), [110,])), 1)
call_263 = relay.TupleGetItem(func_220_call(relay.reshape(var_262.astype('int8'), [110,])), 1)
func_173_call = mod.get_global_var('func_173')
func_175_call = mutated_mod.get_global_var('func_175')
call_269 = relay.TupleGetItem(func_173_call(relay.reshape(var_262.astype('int8'), [5, 11, 2])), 1)
call_270 = relay.TupleGetItem(func_175_call(relay.reshape(var_262.astype('int8'), [5, 11, 2])), 1)
func_173_call = mod.get_global_var('func_173')
func_175_call = mutated_mod.get_global_var('func_175')
call_277 = relay.TupleGetItem(func_173_call(relay.reshape(var_262.astype('int8'), [5, 11, 2])), 0)
call_278 = relay.TupleGetItem(func_175_call(relay.reshape(var_262.astype('int8'), [5, 11, 2])), 0)
output = relay.Tuple([bop_246,call_261,var_262,call_269,call_277,])
output2 = relay.Tuple([bop_246,call_263,var_262,call_270,call_278,])
func_284 = relay.Function([var_244,var_262,], output)
mod['func_284'] = func_284
mod = relay.transform.InferType()(mod)
var_285 = relay.var("var_285", dtype = "uint64", shape = (5, 10, 1))#candidate|285|(5, 10, 1)|var|uint64
var_286 = relay.var("var_286", dtype = "int8", shape = (110,))#candidate|286|(110,)|var|int8
output = func_284(var_285,var_286,)
func_287 = relay.Function([var_285,var_286,], output)
mutated_mod['func_287'] = func_287
mutated_mod = relay.transform.InferType()(mutated_mod)
var_292 = relay.var("var_292", dtype = "int32", shape = (3, 1, 1))#candidate|292|(3, 1, 1)|var|int32
var_293 = relay.var("var_293", dtype = "int32", shape = (3, 7, 8))#candidate|293|(3, 7, 8)|var|int32
bop_294 = relay.bitwise_or(var_292.astype('int32'), var_293.astype('int32')) # shape=(3, 7, 8)
func_217_call = mod.get_global_var('func_217')
func_220_call = mutated_mod.get_global_var('func_220')
var_306 = relay.var("var_306", dtype = "int8", shape = (110,))#candidate|306|(110,)|var|int8
call_305 = relay.TupleGetItem(func_217_call(relay.reshape(var_306.astype('int8'), [110,])), 0)
call_307 = relay.TupleGetItem(func_220_call(relay.reshape(var_306.astype('int8'), [110,])), 0)
uop_310 = relay.sqrt(bop_294.astype('float64')) # shape=(3, 7, 8)
func_217_call = mod.get_global_var('func_217')
func_220_call = mutated_mod.get_global_var('func_220')
call_320 = relay.TupleGetItem(func_217_call(relay.reshape(var_306.astype('int8'), [110,])), 5)
call_321 = relay.TupleGetItem(func_220_call(relay.reshape(var_306.astype('int8'), [110,])), 5)
output = relay.Tuple([call_305,var_306,uop_310,call_320,])
output2 = relay.Tuple([call_307,var_306,uop_310,call_321,])
func_328 = relay.Function([var_292,var_293,var_306,], output)
mod['func_328'] = func_328
mod = relay.transform.InferType()(mod)
var_329 = relay.var("var_329", dtype = "int32", shape = (3, 1, 1))#candidate|329|(3, 1, 1)|var|int32
var_330 = relay.var("var_330", dtype = "int32", shape = (3, 7, 8))#candidate|330|(3, 7, 8)|var|int32
var_331 = relay.var("var_331", dtype = "int8", shape = (110,))#candidate|331|(110,)|var|int8
output = func_328(var_329,var_330,var_331,)
func_332 = relay.Function([var_329,var_330,var_331,], output)
mutated_mod['func_332'] = func_332
mutated_mod = relay.transform.InferType()(mutated_mod)
var_363 = relay.var("var_363", dtype = "float64", shape = ())#candidate|363|()|var|float64
const_364 = relay.const([[[0.629064,7.985718,-6.248506,2.561405,8.729093,-0.323364]],[[1.833448,-2.309245,0.575655,8.776738,-7.315086,-6.219556]],[[8.259337,5.893071,-9.763611,-9.634839,6.329065,-0.950583]],[[0.090273,0.854389,-1.945240,-0.893922,-8.073134,2.662160]],[[-2.620173,2.177739,-9.850446,-1.393469,-6.688944,3.819747]],[[-6.002434,-7.080241,-0.170902,7.439945,-8.518822,-4.359151]]], dtype = "float64")#candidate|364|(6, 1, 6)|const|float64
bop_365 = relay.greater(var_363.astype('bool'), const_364.astype('bool')) # shape=(6, 1, 6)
bop_368 = relay.maximum(const_364.astype('int64'), relay.reshape(bop_365.astype('int64'), relay.shape_of(const_364))) # shape=(6, 1, 6)
func_173_call = mod.get_global_var('func_173')
func_175_call = mutated_mod.get_global_var('func_175')
var_376 = relay.var("var_376", dtype = "int8", shape = (22, 5))#candidate|376|(22, 5)|var|int8
call_375 = relay.TupleGetItem(func_173_call(relay.reshape(var_376.astype('int8'), [5, 11, 2])), 0)
call_377 = relay.TupleGetItem(func_175_call(relay.reshape(var_376.astype('int8'), [5, 11, 2])), 0)
func_173_call = mod.get_global_var('func_173')
func_175_call = mutated_mod.get_global_var('func_175')
call_385 = relay.TupleGetItem(func_173_call(relay.reshape(call_375.astype('int8'), [5, 11, 2])), 0)
call_386 = relay.TupleGetItem(func_175_call(relay.reshape(call_375.astype('int8'), [5, 11, 2])), 0)
bop_393 = relay.logical_or(var_363.astype('bool'), bop_368.astype('bool')) # shape=(6, 1, 6)
func_173_call = mod.get_global_var('func_173')
func_175_call = mutated_mod.get_global_var('func_175')
call_401 = relay.TupleGetItem(func_173_call(relay.reshape(call_385.astype('int8'), [5, 11, 2])), 0)
call_402 = relay.TupleGetItem(func_175_call(relay.reshape(call_385.astype('int8'), [5, 11, 2])), 0)
uop_403 = relay.asin(call_375.astype('float32')) # shape=(5, 11, 2)
uop_405 = relay.asin(call_377.astype('float32')) # shape=(5, 11, 2)
func_328_call = mod.get_global_var('func_328')
func_332_call = mutated_mod.get_global_var('func_332')
const_419 = relay.const([[6,-9,1]], dtype = "int32")#candidate|419|(1, 3)|const|int32
const_420 = relay.const([-6,6,-9,7,2,4,-3,10,10,-10,3,-6,-7,-3,-9,-2,1,-6,-8,-4,6,-10,5,-2,-7,-1,-8,9,-1,4,7,7,-4,8,8,2,4,-5,-1,-3,9,1,10,-5,-2,-3,4,9,-4,10,1,-8,-6,-3,9,-5,1,-10,-6,3,3,-1,7,5,-6,-5,-8,3,5,-9,3,7,-2,4,1,7,3,-2,-7,6,-3,2,6,-3,5,-7,8,10,-10,-7,4,-6,-2,-9,-7,-2,-6,10,-2,-2,5,-5,3,2,-2,6,-2,2,3,3,-4,10,1,-1,3,2,-3,10,4,1,10,3,2,-8,-7,-6,-7,-3,8,-5,-9,10,6,8,-1,-8,-6,3,-8,-2,-3,8,-5,-10,6,4,2,7,-4,-10,4,6,-10,-8,1,3,-6,-1,1,4,7,-5,1,-7,-9,-10,4,2], dtype = "int32")#candidate|420|(168,)|const|int32
call_418 = relay.TupleGetItem(func_328_call(relay.reshape(const_419.astype('int32'), [3, 1, 1]), relay.reshape(const_420.astype('int32'), [3, 7, 8]), relay.reshape(var_376.astype('int8'), [110,]), ), 2)
call_421 = relay.TupleGetItem(func_332_call(relay.reshape(const_419.astype('int32'), [3, 1, 1]), relay.reshape(const_420.astype('int32'), [3, 7, 8]), relay.reshape(var_376.astype('int8'), [110,]), ), 2)
output = relay.Tuple([var_376,call_385,bop_393,call_401,uop_403,call_418,const_419,const_420,])
output2 = relay.Tuple([var_376,call_386,bop_393,call_402,uop_405,call_421,const_419,const_420,])
func_430 = relay.Function([var_363,var_376,], output)
mod['func_430'] = func_430
mod = relay.transform.InferType()(mod)
var_431 = relay.var("var_431", dtype = "float64", shape = ())#candidate|431|()|var|float64
var_432 = relay.var("var_432", dtype = "int8", shape = (22, 5))#candidate|432|(22, 5)|var|int8
output = func_430(var_431,var_432,)
func_433 = relay.Function([var_431,var_432,], output)
mutated_mod['func_433'] = func_433
mutated_mod = relay.transform.InferType()(mutated_mod)
var_469 = relay.var("var_469", dtype = "float32", shape = (2, 3, 4))#candidate|469|(2, 3, 4)|var|float32
uop_470 = relay.erf(var_469.astype('float32')) # shape=(2, 3, 4)
func_430_call = mod.get_global_var('func_430')
func_433_call = mutated_mod.get_global_var('func_433')
var_473 = relay.var("var_473", dtype = "float64", shape = ())#candidate|473|()|var|float64
var_474 = relay.var("var_474", dtype = "int8", shape = (110,))#candidate|474|(110,)|var|int8
call_472 = relay.TupleGetItem(func_430_call(relay.reshape(var_473.astype('float64'), []), relay.reshape(var_474.astype('int8'), [22, 5]), ), 6)
call_475 = relay.TupleGetItem(func_433_call(relay.reshape(var_473.astype('float64'), []), relay.reshape(var_474.astype('int8'), [22, 5]), ), 6)
uop_478 = relay.acos(uop_470.astype('float64')) # shape=(2, 3, 4)
output = relay.Tuple([call_472,var_473,var_474,uop_478,])
output2 = relay.Tuple([call_475,var_473,var_474,uop_478,])
func_485 = relay.Function([var_469,var_473,var_474,], output)
mod['func_485'] = func_485
mod = relay.transform.InferType()(mod)
var_486 = relay.var("var_486", dtype = "float32", shape = (2, 3, 4))#candidate|486|(2, 3, 4)|var|float32
var_487 = relay.var("var_487", dtype = "float64", shape = ())#candidate|487|()|var|float64
var_488 = relay.var("var_488", dtype = "int8", shape = (110,))#candidate|488|(110,)|var|int8
output = func_485(var_486,var_487,var_488,)
func_489 = relay.Function([var_486,var_487,var_488,], output)
mutated_mod['func_489'] = func_489
mutated_mod = relay.transform.InferType()(mutated_mod)
const_621 = relay.const([[[-9,10,5,6,4,5,-3,3,-1,-7,9],[5,6,-2,-4,10,9,5,-6,7,-10,-1],[5,8,-2,-2,-10,2,2,-4,-8,-10,-4],[1,9,-9,10,-1,-3,-3,-3,-6,2,10]],[[-4,2,9,-9,8,-3,9,5,2,-6,-6],[-10,4,3,3,-1,8,-1,7,9,9,4],[4,9,7,2,2,2,7,-3,-9,-9,10],[-1,9,6,-2,8,-2,-3,-10,-4,-7,10]],[[4,-8,8,7,7,-6,-9,-6,3,-10,-9],[-7,10,-1,10,2,-5,-6,-8,-10,2,-3],[10,-4,1,9,-7,-9,10,3,-3,3,-7],[-10,1,-2,-8,3,-4,1,1,7,10,4]],[[-8,-1,3,-9,-4,-5,-1,-9,-2,6,-1],[1,-1,-1,-4,3,3,-5,10,9,6,-9],[1,-5,2,8,2,-5,-8,6,-3,-8,-4],[3,8,8,-5,1,6,-10,-1,10,-10,8]],[[3,-1,-4,-3,3,-2,7,5,8,-10,5],[-1,-10,10,7,-7,-4,9,7,-8,-5,1],[10,-3,-5,-1,5,-7,-4,-3,6,3,10],[2,3,10,-10,-1,-1,1,9,6,-5,-9]],[[9,1,-3,7,-8,3,-9,-1,-3,1,7],[10,3,10,-9,6,2,-5,-6,10,-3,5],[-5,-1,7,2,2,-9,-10,-3,-7,-6,10],[6,4,-10,-9,9,1,2,-1,-3,-8,8]],[[-3,-4,-3,1,-2,7,-3,6,-2,-3,4],[3,2,10,10,8,10,4,-4,5,2,-3],[9,-6,-4,-3,6,6,2,8,4,5,-7],[7,4,7,-6,-2,2,3,8,-6,2,4]],[[8,7,-7,-7,-1,-6,-8,2,5,-6,-3],[5,-7,-8,3,-4,-4,-4,-3,-5,-5,1],[2,-7,7,-4,-2,-4,9,7,-3,-4,2],[-8,-1,1,-2,1,-6,-2,2,5,-6,5]]], dtype = "int64")#candidate|621|(8, 4, 11)|const|int64
var_622 = relay.var("var_622", dtype = "int64", shape = (8, 4, 11))#candidate|622|(8, 4, 11)|var|int64
bop_623 = relay.maximum(const_621.astype('int64'), relay.reshape(var_622.astype('int64'), relay.shape_of(const_621))) # shape=(8, 4, 11)
func_284_call = mod.get_global_var('func_284')
func_287_call = mutated_mod.get_global_var('func_287')
const_627 = relay.const([6,9,5,-4,4,-2,2,1,-4,2,7,3,3,4,-9,-8,2,9,-9,-10,10,1,4,9,-2,7,5,3,-8,-5,-7,4,-10,-7,-7,-3,10,10,-8,4,-2,-1,-3,-4,-3,-9,-3,2,-7,4], dtype = "uint64")#candidate|627|(50,)|const|uint64
const_628 = relay.const([-2,1,-9,-1,-1,3,9,-6,6,1,2,8,7,2,-1,9,1,5,1,4,6,-1,3,7,1,-5,-4,-6,10,4,-6,-5,5,9,-6,7,10,9,9,5,8,2,4,-4,-7,-8,-3,10,-4,5,1,4,-2,-5,10,1,-9,-9,1,9,-2,-1,-1,3,7,5,-10,1,1,2,-7,9,-6,-1,4,6,-7,10,-7,1,-1,-4,-5,-2,1,8,-9,-4,-7,-3,-4,-6,-6,-7,9,9,-6,10,7,8,8,-6,2,1,2,2,-2,7,5,3], dtype = "int8")#candidate|628|(110,)|const|int8
call_626 = relay.TupleGetItem(func_284_call(relay.reshape(const_627.astype('uint64'), [5, 10, 1]), relay.reshape(const_628.astype('int8'), [110,]), ), 2)
call_629 = relay.TupleGetItem(func_287_call(relay.reshape(const_627.astype('uint64'), [5, 10, 1]), relay.reshape(const_628.astype('int8'), [110,]), ), 2)
func_173_call = mod.get_global_var('func_173')
func_175_call = mutated_mod.get_global_var('func_175')
call_630 = relay.TupleGetItem(func_173_call(relay.reshape(const_628.astype('int8'), [5, 11, 2])), 1)
call_631 = relay.TupleGetItem(func_175_call(relay.reshape(const_628.astype('int8'), [5, 11, 2])), 1)
func_173_call = mod.get_global_var('func_173')
func_175_call = mutated_mod.get_global_var('func_175')
call_633 = relay.TupleGetItem(func_173_call(relay.reshape(call_630.astype('int8'), [5, 11, 2])), 1)
call_634 = relay.TupleGetItem(func_175_call(relay.reshape(call_630.astype('int8'), [5, 11, 2])), 1)
bop_638 = relay.logical_or(call_626.astype('bool'), relay.reshape(const_628.astype('bool'), relay.shape_of(call_626))) # shape=(110,)
bop_641 = relay.logical_or(call_629.astype('bool'), relay.reshape(const_628.astype('bool'), relay.shape_of(call_629))) # shape=(110,)
uop_642 = relay.acos(var_622.astype('float64')) # shape=(8, 4, 11)
func_328_call = mod.get_global_var('func_328')
func_332_call = mutated_mod.get_global_var('func_332')
var_645 = relay.var("var_645", dtype = "int32", shape = (3,))#candidate|645|(3,)|var|int32
var_646 = relay.var("var_646", dtype = "int32", shape = (168,))#candidate|646|(168,)|var|int32
call_644 = relay.TupleGetItem(func_328_call(relay.reshape(var_645.astype('int32'), [3, 1, 1]), relay.reshape(var_646.astype('int32'), [3, 7, 8]), relay.reshape(call_633.astype('int8'), [110,]), ), 3)
call_647 = relay.TupleGetItem(func_332_call(relay.reshape(var_645.astype('int32'), [3, 1, 1]), relay.reshape(var_646.astype('int32'), [3, 7, 8]), relay.reshape(call_633.astype('int8'), [110,]), ), 3)
output = relay.Tuple([bop_623,const_627,call_630,call_633,bop_638,uop_642,call_644,var_645,var_646,])
output2 = relay.Tuple([bop_623,const_627,call_631,call_634,bop_641,uop_642,call_647,var_645,var_646,])
func_648 = relay.Function([var_622,var_645,var_646,], output)
mod['func_648'] = func_648
mod = relay.transform.InferType()(mod)
mutated_mod['func_648'] = func_648
mutated_mod = relay.transform.InferType()(mutated_mod)
func_648_call = mutated_mod.get_global_var('func_648')
var_650 = relay.var("var_650", dtype = "int64", shape = (8, 4, 11))#candidate|650|(8, 4, 11)|var|int64
var_651 = relay.var("var_651", dtype = "int32", shape = (3,))#candidate|651|(3,)|var|int32
var_652 = relay.var("var_652", dtype = "int32", shape = (168,))#candidate|652|(168,)|var|int32
call_649 = func_648_call(var_650,var_651,var_652,)
output = call_649
func_653 = relay.Function([var_650,var_651,var_652,], output)
mutated_mod['func_653'] = func_653
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1007 = relay.var("var_1007", dtype = "float32", shape = (5, 5, 4))#candidate|1007|(5, 5, 4)|var|float32
uop_1008 = relay.cos(var_1007.astype('float32')) # shape=(5, 5, 4)
func_430_call = mod.get_global_var('func_430')
func_433_call = mutated_mod.get_global_var('func_433')
const_1028 = relay.const(5.320767, dtype = "float64")#candidate|1028|()|const|float64
var_1029 = relay.var("var_1029", dtype = "int8", shape = (110,))#candidate|1029|(110,)|var|int8
call_1027 = relay.TupleGetItem(func_430_call(relay.reshape(const_1028.astype('float64'), []), relay.reshape(var_1029.astype('int8'), [22, 5]), ), 3)
call_1030 = relay.TupleGetItem(func_433_call(relay.reshape(const_1028.astype('float64'), []), relay.reshape(var_1029.astype('int8'), [22, 5]), ), 3)
output = relay.Tuple([uop_1008,call_1027,const_1028,var_1029,])
output2 = relay.Tuple([uop_1008,call_1030,const_1028,var_1029,])
func_1031 = relay.Function([var_1007,var_1029,], output)
mod['func_1031'] = func_1031
mod = relay.transform.InferType()(mod)
var_1032 = relay.var("var_1032", dtype = "float32", shape = (5, 5, 4))#candidate|1032|(5, 5, 4)|var|float32
var_1033 = relay.var("var_1033", dtype = "int8", shape = (110,))#candidate|1033|(110,)|var|int8
output = func_1031(var_1032,var_1033,)
func_1034 = relay.Function([var_1032,var_1033,], output)
mutated_mod['func_1034'] = func_1034
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1236 = relay.var("var_1236", dtype = "float32", shape = (16, 6, 8))#candidate|1236|(16, 6, 8)|var|float32
uop_1237 = relay.cos(var_1236.astype('float32')) # shape=(16, 6, 8)
bop_1259 = relay.logical_and(uop_1237.astype('bool'), relay.reshape(var_1236.astype('bool'), relay.shape_of(uop_1237))) # shape=(16, 6, 8)
output = relay.Tuple([bop_1259,])
output2 = relay.Tuple([bop_1259,])
func_1263 = relay.Function([var_1236,], output)
mod['func_1263'] = func_1263
mod = relay.transform.InferType()(mod)
mutated_mod['func_1263'] = func_1263
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1264 = relay.var("var_1264", dtype = "float32", shape = (16, 6, 8))#candidate|1264|(16, 6, 8)|var|float32
func_1263_call = mutated_mod.get_global_var('func_1263')
call_1265 = func_1263_call(var_1264)
output = call_1265
func_1266 = relay.Function([var_1264], output)
mutated_mod['func_1266'] = func_1266
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1313 = relay.const(2, dtype = "uint32")#candidate|1313|()|const|uint32
var_1314 = relay.var("var_1314", dtype = "uint32", shape = (4, 11, 5))#candidate|1314|(4, 11, 5)|var|uint32
bop_1315 = relay.multiply(const_1313.astype('uint32'), var_1314.astype('uint32')) # shape=(4, 11, 5)
func_328_call = mod.get_global_var('func_328')
func_332_call = mutated_mod.get_global_var('func_332')
const_1321 = relay.const([7,9,-3], dtype = "int32")#candidate|1321|(3,)|const|int32
const_1322 = relay.const([[10],[-1],[6],[-8],[-7],[8],[-10],[9],[-7],[10],[6],[1],[-4],[7],[10],[-10],[-5],[-1],[-7],[8],[2],[3],[1],[9],[10],[3],[-3],[-9],[-5],[-6],[-2],[-5],[-9],[8],[9],[-9],[3],[4],[5],[-4],[-3],[1],[1],[5],[-8],[3],[9],[-7],[-8],[4],[2],[-8],[-7],[-1],[-6],[-7],[1],[-4],[-8],[2],[-10],[-8],[-5],[-7],[3],[-10],[-7],[1],[1],[-4],[6],[5],[-9],[-2],[10],[5],[-9],[10],[1],[6],[-1],[10],[-5],[9],[1],[-2],[-7],[4],[7],[-3],[2],[-6],[-4],[-4],[6],[-8],[8],[-4],[-6],[-10],[8],[-4],[8],[1],[8],[2],[-5],[-10],[5],[-1],[-5],[7],[-6],[6],[-3],[1],[-6],[-8],[-4],[2],[4],[-1],[-10],[-7],[4],[7],[8],[1],[-2],[6],[-1],[7],[-1],[-6],[4],[7],[1],[9],[9],[-8],[6],[10],[-7],[6],[10],[-5],[8],[-10],[6],[3],[5],[-2],[-10],[-8],[8],[1],[9],[-6],[4],[8],[-3],[-5],[-4],[9],[3],[2],[4],[4]], dtype = "int32")#candidate|1322|(168, 1)|const|int32
var_1323 = relay.var("var_1323", dtype = "int8", shape = (110,))#candidate|1323|(110,)|var|int8
call_1320 = relay.TupleGetItem(func_328_call(relay.reshape(const_1321.astype('int32'), [3, 1, 1]), relay.reshape(const_1322.astype('int32'), [3, 7, 8]), relay.reshape(var_1323.astype('int8'), [110,]), ), 3)
call_1324 = relay.TupleGetItem(func_332_call(relay.reshape(const_1321.astype('int32'), [3, 1, 1]), relay.reshape(const_1322.astype('int32'), [3, 7, 8]), relay.reshape(var_1323.astype('int8'), [110,]), ), 3)
output = relay.Tuple([bop_1315,call_1320,const_1321,const_1322,var_1323,])
output2 = relay.Tuple([bop_1315,call_1324,const_1321,const_1322,var_1323,])
func_1329 = relay.Function([var_1314,var_1323,], output)
mod['func_1329'] = func_1329
mod = relay.transform.InferType()(mod)
mutated_mod['func_1329'] = func_1329
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1329_call = mutated_mod.get_global_var('func_1329')
var_1331 = relay.var("var_1331", dtype = "uint32", shape = (4, 11, 5))#candidate|1331|(4, 11, 5)|var|uint32
var_1332 = relay.var("var_1332", dtype = "int8", shape = (110,))#candidate|1332|(110,)|var|int8
call_1330 = func_1329_call(var_1331,var_1332,)
output = call_1330
func_1333 = relay.Function([var_1331,var_1332,], output)
mutated_mod['func_1333'] = func_1333
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1360 = relay.var("var_1360", dtype = "float64", shape = (14, 14, 7))#candidate|1360|(14, 14, 7)|var|float64
uop_1361 = relay.log10(var_1360.astype('float64')) # shape=(14, 14, 7)
output = uop_1361
output2 = uop_1361
func_1364 = relay.Function([var_1360,], output)
mod['func_1364'] = func_1364
mod = relay.transform.InferType()(mod)
mutated_mod['func_1364'] = func_1364
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1365 = relay.var("var_1365", dtype = "float64", shape = (14, 14, 7))#candidate|1365|(14, 14, 7)|var|float64
func_1364_call = mutated_mod.get_global_var('func_1364')
call_1366 = func_1364_call(var_1365)
output = call_1366
func_1367 = relay.Function([var_1365], output)
mutated_mod['func_1367'] = func_1367
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1513 = relay.var("var_1513", dtype = "float64", shape = (2, 12, 1))#candidate|1513|(2, 12, 1)|var|float64
uop_1514 = relay.acosh(var_1513.astype('float64')) # shape=(2, 12, 1)
func_217_call = mod.get_global_var('func_217')
func_220_call = mutated_mod.get_global_var('func_220')
const_1522 = relay.const([9,-2,-6,5,10,-6,-5,-2,6,-2,-9,2,10,8,7,2,3,-2,-2,9,-9,9,-9,-2,-2,-9,9,10,-5,1,-2,-9,9,-1,10,-7,5,5,-8,1,3,-2,-9,6,-3,-9,-1,7,10,5,10,-1,9,-10,-6,8,1,4,4,-8,-8,-9,3,-1,6,5,7,2,5,-2,5,8,1,7,-3,-2,10,-10,-9,-8,-8,-4,10,-2,10,-3,3,2,-7,-9,4,1,-5,8,5,-3,-2,9,-5,-6,2,-9,-5,1,9,-2,3,8,-8,6], dtype = "int8")#candidate|1522|(110,)|const|int8
call_1521 = relay.TupleGetItem(func_217_call(relay.reshape(const_1522.astype('int8'), [110,])), 4)
call_1523 = relay.TupleGetItem(func_220_call(relay.reshape(const_1522.astype('int8'), [110,])), 4)
bop_1526 = relay.less(uop_1514.astype('bool'), const_1522.astype('bool')) # shape=(2, 12, 110)
output = relay.Tuple([call_1521,bop_1526,])
output2 = relay.Tuple([call_1523,bop_1526,])
func_1533 = relay.Function([var_1513,], output)
mod['func_1533'] = func_1533
mod = relay.transform.InferType()(mod)
var_1534 = relay.var("var_1534", dtype = "float64", shape = (2, 12, 1))#candidate|1534|(2, 12, 1)|var|float64
output = func_1533(var_1534)
func_1535 = relay.Function([var_1534], output)
mutated_mod['func_1535'] = func_1535
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1603 = relay.const([[[6,-5,-6,-5,10,-1,-10,-5,-6,-6,1,1,4,-9],[-5,-8,4,10,-8,2,-6,-3,10,5,-5,10,-2,3]],[[7,2,-3,-4,6,9,-1,-2,-6,5,4,-1,-1,-4],[3,1,-9,3,3,-3,5,3,-2,3,9,-3,8,-4]],[[8,1,7,-1,-5,10,-6,-7,4,-5,4,-4,5,-7],[-3,9,-1,1,2,-4,-10,5,9,5,3,-10,7,9]],[[3,-5,9,8,-4,-7,4,-3,6,-8,-1,8,4,-10],[-6,-5,9,5,-3,7,3,4,-5,-2,5,8,5,-10]],[[8,2,-1,2,4,-7,2,4,7,-5,-7,5,-8,-7],[-1,-2,9,2,10,9,1,2,-9,1,8,-10,2,6]],[[10,-1,-2,-1,-10,10,-5,7,-4,-1,7,9,-5,-10],[-4,-5,10,5,-2,3,-9,3,4,2,-8,1,3,3]],[[-10,-7,7,-9,1,-9,10,4,-6,5,-4,10,-10,-9],[2,2,-3,6,-2,-7,9,-5,-9,-2,5,-7,-4,3]],[[1,-6,-4,-4,-1,6,-5,6,2,-7,-2,8,-6,-8],[-3,4,-5,-8,1,5,-4,5,8,5,3,-1,-3,-2]],[[-5,9,3,3,-4,-6,-2,-6,4,6,-5,1,7,4],[-2,-8,9,4,-3,-2,7,1,-1,-6,10,-6,-4,-4]],[[-1,-8,-7,8,8,-7,-1,5,1,9,-6,-8,6,-3],[2,-9,6,-4,8,8,-7,4,-8,-8,-6,10,2,8]],[[1,-8,1,-6,9,-9,-3,2,3,-8,6,9,-10,3],[4,-2,5,8,9,2,-1,4,9,5,-3,-5,6,-10]],[[1,-10,7,10,2,-7,-9,1,-3,7,3,5,3,-5],[-4,-7,8,-1,-1,-8,-8,-6,-5,8,-5,9,-7,6]],[[-6,10,5,4,7,10,-6,-1,-3,-3,7,8,8,-2],[4,4,-8,-10,2,-8,-1,6,-7,4,-5,10,-10,-4]],[[6,3,3,-9,-4,5,3,6,4,-3,-9,2,-6,8],[1,-4,9,6,-9,-4,-2,-2,6,2,9,2,-4,6]],[[5,6,5,2,9,7,-10,2,3,10,-1,-9,8,2],[4,-2,1,6,7,-1,7,-4,-10,1,-2,3,5,-6]]], dtype = "uint32")#candidate|1603|(15, 2, 14)|const|uint32
const_1604 = relay.const([[[9,-6,8,-8,4,-2,7,-10,-5,-7,10,5,3,-8],[4,8,-7,-10,4,-1,5,-1,3,1,10,10,10,-1]],[[-3,9,9,1,-4,3,10,6,7,-10,-9,-8,-8,6],[-4,-3,6,-4,-9,-10,-9,3,-7,7,-4,-2,-5,-1]],[[-9,-3,6,9,7,-6,2,1,1,1,1,-1,4,-10],[-4,-3,10,5,9,-9,-7,3,4,-9,8,-4,9,-5]],[[-1,-1,8,7,8,-5,5,-5,10,2,-2,1,-4,-10],[-2,-5,10,7,9,-5,7,-8,-5,-5,-9,-10,-9,-2]],[[6,5,6,1,5,3,2,-5,-9,1,3,10,-4,-4],[9,-7,9,3,1,1,-1,-2,-4,4,-7,9,3,-4]],[[8,-2,-6,-2,-1,10,10,-10,8,6,8,-7,-6,-6],[4,10,10,10,10,-2,-8,5,-6,3,-6,7,-10,10]],[[1,-7,-6,8,8,5,-10,1,1,-10,-10,10,9,-9],[-2,-6,-4,9,-7,-7,2,5,9,2,1,-7,-4,-8]],[[-6,3,-3,-2,-10,-9,7,6,-8,-3,-6,-6,-8,1],[-2,6,-3,6,8,4,-1,8,9,-7,-4,5,-7,8]],[[-4,9,7,3,-4,7,9,9,4,-7,-1,1,5,5],[7,-1,-4,8,-6,1,-10,-10,-8,10,-8,7,1,5]],[[4,-10,-5,3,-1,-1,1,-5,-10,1,-7,2,-8,-5],[6,5,-9,-10,-7,-6,-3,-5,10,-5,-6,10,7,-1]],[[10,-4,-5,4,-7,2,7,-2,6,-3,7,9,-4,9],[1,-8,5,7,2,-5,6,-5,-5,3,4,10,-6,7]],[[7,1,5,9,1,9,7,-2,-1,-8,-4,10,9,-1],[10,-4,5,7,5,9,3,-9,2,-5,-10,1,-6,-6]],[[-2,1,-5,3,10,-2,-7,3,9,-2,5,5,-4,3],[-9,6,-6,-5,2,2,7,9,5,8,3,-4,-9,8]],[[-7,-3,10,8,-6,6,9,4,-2,-4,4,-10,1,-9],[-2,4,-8,6,6,-3,-4,-4,8,1,-10,8,6,-5]],[[1,7,-3,-5,-8,10,-4,8,-3,-3,2,-5,-10,8],[-1,2,9,7,10,4,4,4,8,-6,-6,-3,4,1]]], dtype = "uint32")#candidate|1604|(15, 2, 14)|const|uint32
bop_1605 = relay.equal(const_1603.astype('bool'), relay.reshape(const_1604.astype('bool'), relay.shape_of(const_1603))) # shape=(15, 2, 14)
func_173_call = mod.get_global_var('func_173')
func_175_call = mutated_mod.get_global_var('func_175')
var_1612 = relay.var("var_1612", dtype = "int8", shape = (110,))#candidate|1612|(110,)|var|int8
call_1611 = relay.TupleGetItem(func_173_call(relay.reshape(var_1612.astype('int8'), [5, 11, 2])), 1)
call_1613 = relay.TupleGetItem(func_175_call(relay.reshape(var_1612.astype('int8'), [5, 11, 2])), 1)
output = relay.Tuple([bop_1605,call_1611,var_1612,])
output2 = relay.Tuple([bop_1605,call_1613,var_1612,])
func_1627 = relay.Function([var_1612,], output)
mod['func_1627'] = func_1627
mod = relay.transform.InferType()(mod)
mutated_mod['func_1627'] = func_1627
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1628 = relay.var("var_1628", dtype = "int8", shape = (110,))#candidate|1628|(110,)|var|int8
func_1627_call = mutated_mod.get_global_var('func_1627')
call_1629 = func_1627_call(var_1628)
output = call_1629
func_1630 = relay.Function([var_1628], output)
mutated_mod['func_1630'] = func_1630
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1648 = relay.var("var_1648", dtype = "float32", shape = (14, 7, 2))#candidate|1648|(14, 7, 2)|var|float32
uop_1649 = relay.acos(var_1648.astype('float32')) # shape=(14, 7, 2)
func_1533_call = mod.get_global_var('func_1533')
func_1535_call = mutated_mod.get_global_var('func_1535')
var_1652 = relay.var("var_1652", dtype = "float64", shape = (24,))#candidate|1652|(24,)|var|float64
call_1651 = relay.TupleGetItem(func_1533_call(relay.reshape(var_1652.astype('float64'), [2, 12, 1])), 1)
call_1653 = relay.TupleGetItem(func_1535_call(relay.reshape(var_1652.astype('float64'), [2, 12, 1])), 1)
output = relay.Tuple([uop_1649,call_1651,var_1652,])
output2 = relay.Tuple([uop_1649,call_1653,var_1652,])
func_1659 = relay.Function([var_1648,var_1652,], output)
mod['func_1659'] = func_1659
mod = relay.transform.InferType()(mod)
var_1660 = relay.var("var_1660", dtype = "float32", shape = (14, 7, 2))#candidate|1660|(14, 7, 2)|var|float32
var_1661 = relay.var("var_1661", dtype = "float64", shape = (24,))#candidate|1661|(24,)|var|float64
output = func_1659(var_1660,var_1661,)
func_1662 = relay.Function([var_1660,var_1661,], output)
mutated_mod['func_1662'] = func_1662
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1684 = relay.var("var_1684", dtype = "float64", shape = (4, 14, 3))#candidate|1684|(4, 14, 3)|var|float64
uop_1685 = relay.cosh(var_1684.astype('float64')) # shape=(4, 14, 3)
output = uop_1685
output2 = uop_1685
func_1687 = relay.Function([var_1684,], output)
mod['func_1687'] = func_1687
mod = relay.transform.InferType()(mod)
mutated_mod['func_1687'] = func_1687
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1688 = relay.var("var_1688", dtype = "float64", shape = (4, 14, 3))#candidate|1688|(4, 14, 3)|var|float64
func_1687_call = mutated_mod.get_global_var('func_1687')
call_1689 = func_1687_call(var_1688)
output = call_1689
func_1690 = relay.Function([var_1688], output)
mutated_mod['func_1690'] = func_1690
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1729 = relay.var("var_1729", dtype = "uint64", shape = (2, 15, 9))#candidate|1729|(2, 15, 9)|var|uint64
var_1730 = relay.var("var_1730", dtype = "uint64", shape = (2, 15, 9))#candidate|1730|(2, 15, 9)|var|uint64
bop_1731 = relay.multiply(var_1729.astype('uint64'), relay.reshape(var_1730.astype('uint64'), relay.shape_of(var_1729))) # shape=(2, 15, 9)
uop_1739 = relay.exp(bop_1731.astype('float64')) # shape=(2, 15, 9)
uop_1753 = relay.log(uop_1739.astype('float64')) # shape=(2, 15, 9)
func_1659_call = mod.get_global_var('func_1659')
func_1662_call = mutated_mod.get_global_var('func_1662')
var_1768 = relay.var("var_1768", dtype = "float32", shape = (196,))#candidate|1768|(196,)|var|float32
const_1769 = relay.const([-7.071796,9.457670,0.926782,-8.420595,-2.152403,6.877478,-5.110956,1.030506,2.262512,3.980458,-9.435478,9.119681,1.340695,-9.395492,-7.198426,-2.365965,-6.784472,-1.410746,-9.520926,2.201640,6.829945,9.957392,-5.560801,-7.949519], dtype = "float64")#candidate|1769|(24,)|const|float64
call_1767 = relay.TupleGetItem(func_1659_call(relay.reshape(var_1768.astype('float32'), [14, 7, 2]), relay.reshape(const_1769.astype('float64'), [24,]), ), 1)
call_1770 = relay.TupleGetItem(func_1662_call(relay.reshape(var_1768.astype('float32'), [14, 7, 2]), relay.reshape(const_1769.astype('float64'), [24,]), ), 1)
func_430_call = mod.get_global_var('func_430')
func_433_call = mutated_mod.get_global_var('func_433')
const_1776 = relay.const(-0.898348, dtype = "float64")#candidate|1776|()|const|float64
var_1777 = relay.var("var_1777", dtype = "int8", shape = (1, 110))#candidate|1777|(1, 110)|var|int8
call_1775 = relay.TupleGetItem(func_430_call(relay.reshape(const_1776.astype('float64'), []), relay.reshape(var_1777.astype('int8'), [22, 5]), ), 1)
call_1778 = relay.TupleGetItem(func_433_call(relay.reshape(const_1776.astype('float64'), []), relay.reshape(var_1777.astype('int8'), [22, 5]), ), 1)
uop_1786 = relay.rsqrt(uop_1739.astype('float32')) # shape=(2, 15, 9)
func_1659_call = mod.get_global_var('func_1659')
func_1662_call = mutated_mod.get_global_var('func_1662')
call_1792 = relay.TupleGetItem(func_1659_call(relay.reshape(var_1768.astype('float32'), [14, 7, 2]), relay.reshape(const_1769.astype('float64'), [24,]), ), 1)
call_1793 = relay.TupleGetItem(func_1662_call(relay.reshape(var_1768.astype('float32'), [14, 7, 2]), relay.reshape(const_1769.astype('float64'), [24,]), ), 1)
output = relay.Tuple([uop_1753,call_1767,var_1768,const_1769,call_1775,const_1776,var_1777,uop_1786,call_1792,])
output2 = relay.Tuple([uop_1753,call_1770,var_1768,const_1769,call_1778,const_1776,var_1777,uop_1786,call_1793,])
func_1797 = relay.Function([var_1729,var_1730,var_1768,var_1777,], output)
mod['func_1797'] = func_1797
mod = relay.transform.InferType()(mod)
var_1798 = relay.var("var_1798", dtype = "uint64", shape = (2, 15, 9))#candidate|1798|(2, 15, 9)|var|uint64
var_1799 = relay.var("var_1799", dtype = "uint64", shape = (2, 15, 9))#candidate|1799|(2, 15, 9)|var|uint64
var_1800 = relay.var("var_1800", dtype = "float32", shape = (196,))#candidate|1800|(196,)|var|float32
var_1801 = relay.var("var_1801", dtype = "int8", shape = (1, 110))#candidate|1801|(1, 110)|var|int8
output = func_1797(var_1798,var_1799,var_1800,var_1801,)
func_1802 = relay.Function([var_1798,var_1799,var_1800,var_1801,], output)
mutated_mod['func_1802'] = func_1802
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1838 = relay.const([[[5.662441,0.768157,-2.160823,6.223488,5.408269],[7.109490,4.484845,-3.817563,9.955203,-2.426811],[0.995714,-5.644472,-4.333085,8.450425,5.588865],[3.018895,6.178542,0.516951,-4.874190,2.913818]],[[-0.384610,5.720544,-4.734465,7.078705,-0.177831],[3.453560,-3.317442,-5.302781,8.788879,-7.305179],[-4.325503,9.660630,-5.362993,8.237844,-3.835422],[-4.941432,-9.178040,-6.302145,0.962946,-7.677889]],[[2.644970,-4.817704,5.197680,-0.412470,-6.591392],[7.821809,-0.361554,0.578917,-3.592315,-7.038684],[4.809310,5.699112,-0.017154,-0.616388,2.969391],[1.934562,8.440092,-9.867289,-1.943622,3.581016]],[[9.354042,3.339585,9.335958,-1.700512,-6.216999],[-1.495354,-6.541693,4.802100,-6.577095,-7.343698],[-6.743592,-1.627535,0.364890,-4.340978,-7.129166],[8.918346,8.544871,1.907569,0.100866,-2.077452]],[[-2.968975,8.751504,-6.279686,1.089763,0.783443],[-0.310721,9.933054,5.416695,2.138413,-4.062649],[5.641428,9.224998,7.667220,5.033005,-0.287636],[-2.983151,7.441581,0.537885,-7.690441,-9.817409]],[[9.295448,4.583841,7.810122,3.260928,-1.441063],[-6.553519,8.849548,-2.050874,2.733762,4.917655],[4.556670,-9.645579,-1.597066,-4.211043,2.820390],[-2.325641,6.014513,9.556356,-9.915309,8.250923]],[[7.681076,-3.958493,0.777438,6.459137,-4.986845],[0.163596,-4.206103,-5.049125,0.650637,3.678135],[4.152482,7.428940,7.102547,-0.806183,-4.294925],[-5.121532,4.574226,-4.325566,-3.020097,0.341948]],[[3.867696,-8.547270,2.830467,-6.053381,-3.537982],[2.448419,6.052470,-5.412623,0.085174,-8.227649],[5.647191,9.112846,8.537114,7.003567,3.878968],[-9.687243,9.635391,-9.188027,-3.963898,-3.294350]],[[-5.200302,-6.403130,-8.518527,-4.451064,4.463611],[4.184804,-6.208005,-5.839713,4.229250,4.624521],[-0.824249,1.413455,-3.071576,-4.771984,-7.986245],[8.745878,-0.542826,-5.177950,8.164304,1.309941]]], dtype = "float32")#candidate|1838|(9, 4, 5)|const|float32
uop_1839 = relay.tan(const_1838.astype('float32')) # shape=(9, 4, 5)
func_1263_call = mod.get_global_var('func_1263')
func_1266_call = mutated_mod.get_global_var('func_1266')
var_1846 = relay.var("var_1846", dtype = "float32", shape = (768,))#candidate|1846|(768,)|var|float32
call_1845 = relay.TupleGetItem(func_1263_call(relay.reshape(var_1846.astype('float32'), [16, 6, 8])), 0)
call_1847 = relay.TupleGetItem(func_1266_call(relay.reshape(var_1846.astype('float32'), [16, 6, 8])), 0)
output = relay.Tuple([uop_1839,call_1845,var_1846,])
output2 = relay.Tuple([uop_1839,call_1847,var_1846,])
func_1850 = relay.Function([var_1846,], output)
mod['func_1850'] = func_1850
mod = relay.transform.InferType()(mod)
mutated_mod['func_1850'] = func_1850
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1851 = relay.var("var_1851", dtype = "float32", shape = (768,))#candidate|1851|(768,)|var|float32
func_1850_call = mutated_mod.get_global_var('func_1850')
call_1852 = func_1850_call(var_1851)
output = call_1852
func_1853 = relay.Function([var_1851], output)
mutated_mod['func_1853'] = func_1853
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1922 = relay.const(-10, dtype = "uint8")#candidate|1922|()|const|uint8
var_1923 = relay.var("var_1923", dtype = "uint8", shape = (1, 15, 1))#candidate|1923|(1, 15, 1)|var|uint8
bop_1924 = relay.bitwise_xor(const_1922.astype('uint8'), var_1923.astype('uint8')) # shape=(1, 15, 1)
output = bop_1924
output2 = bop_1924
func_1951 = relay.Function([var_1923,], output)
mod['func_1951'] = func_1951
mod = relay.transform.InferType()(mod)
var_1952 = relay.var("var_1952", dtype = "uint8", shape = (1, 15, 1))#candidate|1952|(1, 15, 1)|var|uint8
output = func_1951(var_1952)
func_1953 = relay.Function([var_1952], output)
mutated_mod['func_1953'] = func_1953
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2002 = relay.var("var_2002", dtype = "float32", shape = ())#candidate|2002|()|var|float32
var_2003 = relay.var("var_2003", dtype = "float32", shape = (4, 4))#candidate|2003|(4, 4)|var|float32
bop_2004 = relay.mod(var_2002.astype('float32'), var_2003.astype('float32')) # shape=(4, 4)
output = relay.Tuple([bop_2004,])
output2 = relay.Tuple([bop_2004,])
func_2010 = relay.Function([var_2002,var_2003,], output)
mod['func_2010'] = func_2010
mod = relay.transform.InferType()(mod)
var_2011 = relay.var("var_2011", dtype = "float32", shape = ())#candidate|2011|()|var|float32
var_2012 = relay.var("var_2012", dtype = "float32", shape = (4, 4))#candidate|2012|(4, 4)|var|float32
output = func_2010(var_2011,var_2012,)
func_2013 = relay.Function([var_2011,var_2012,], output)
mutated_mod['func_2013'] = func_2013
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2164 = relay.var("var_2164", dtype = "float32", shape = (12, 3, 5))#candidate|2164|(12, 3, 5)|var|float32
uop_2165 = relay.tan(var_2164.astype('float32')) # shape=(12, 3, 5)
output = uop_2165
output2 = uop_2165
func_2167 = relay.Function([var_2164,], output)
mod['func_2167'] = func_2167
mod = relay.transform.InferType()(mod)
mutated_mod['func_2167'] = func_2167
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2168 = relay.var("var_2168", dtype = "float32", shape = (12, 3, 5))#candidate|2168|(12, 3, 5)|var|float32
func_2167_call = mutated_mod.get_global_var('func_2167')
call_2169 = func_2167_call(var_2168)
output = call_2169
func_2170 = relay.Function([var_2168], output)
mutated_mod['func_2170'] = func_2170
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2223 = relay.var("var_2223", dtype = "float64", shape = (3, 1, 8))#candidate|2223|(3, 1, 8)|var|float64
var_2224 = relay.var("var_2224", dtype = "float64", shape = (3, 2, 8))#candidate|2224|(3, 2, 8)|var|float64
bop_2225 = relay.floor_mod(var_2223.astype('float64'), var_2224.astype('float64')) # shape=(3, 2, 8)
bop_2240 = relay.multiply(var_2224.astype('uint16'), relay.reshape(bop_2225.astype('uint16'), relay.shape_of(var_2224))) # shape=(3, 2, 8)
uop_2244 = relay.log10(var_2223.astype('float64')) # shape=(3, 1, 8)
uop_2247 = relay.cos(uop_2244.astype('float32')) # shape=(3, 1, 8)
var_2250 = relay.var("var_2250", dtype = "float64", shape = (3, 1, 8))#candidate|2250|(3, 1, 8)|var|float64
bop_2251 = relay.maximum(uop_2244.astype('int16'), relay.reshape(var_2250.astype('int16'), relay.shape_of(uop_2244))) # shape=(3, 1, 8)
output = relay.Tuple([bop_2240,uop_2247,bop_2251,])
output2 = relay.Tuple([bop_2240,uop_2247,bop_2251,])
func_2254 = relay.Function([var_2223,var_2224,var_2250,], output)
mod['func_2254'] = func_2254
mod = relay.transform.InferType()(mod)
mutated_mod['func_2254'] = func_2254
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2254_call = mutated_mod.get_global_var('func_2254')
var_2256 = relay.var("var_2256", dtype = "float64", shape = (3, 1, 8))#candidate|2256|(3, 1, 8)|var|float64
var_2257 = relay.var("var_2257", dtype = "float64", shape = (3, 2, 8))#candidate|2257|(3, 2, 8)|var|float64
var_2258 = relay.var("var_2258", dtype = "float64", shape = (3, 1, 8))#candidate|2258|(3, 1, 8)|var|float64
call_2255 = func_2254_call(var_2256,var_2257,var_2258,)
output = call_2255
func_2259 = relay.Function([var_2256,var_2257,var_2258,], output)
mutated_mod['func_2259'] = func_2259
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2342 = relay.var("var_2342", dtype = "uint8", shape = ())#candidate|2342|()|var|uint8
var_2343 = relay.var("var_2343", dtype = "uint8", shape = (12, 11, 4))#candidate|2343|(12, 11, 4)|var|uint8
bop_2344 = relay.less_equal(var_2342.astype('bool'), var_2343.astype('bool')) # shape=(12, 11, 4)
output = relay.Tuple([bop_2344,])
output2 = relay.Tuple([bop_2344,])
func_2385 = relay.Function([var_2342,var_2343,], output)
mod['func_2385'] = func_2385
mod = relay.transform.InferType()(mod)
var_2386 = relay.var("var_2386", dtype = "uint8", shape = ())#candidate|2386|()|var|uint8
var_2387 = relay.var("var_2387", dtype = "uint8", shape = (12, 11, 4))#candidate|2387|(12, 11, 4)|var|uint8
output = func_2385(var_2386,var_2387,)
func_2388 = relay.Function([var_2386,var_2387,], output)
mutated_mod['func_2388'] = func_2388
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2576 = relay.var("var_2576", dtype = "float32", shape = (10, 16, 1))#candidate|2576|(10, 16, 1)|var|float32
uop_2577 = relay.sin(var_2576.astype('float32')) # shape=(10, 16, 1)
func_1687_call = mod.get_global_var('func_1687')
func_1690_call = mutated_mod.get_global_var('func_1690')
var_2582 = relay.var("var_2582", dtype = "float64", shape = (6, 28))#candidate|2582|(6, 28)|var|float64
call_2581 = func_1687_call(relay.reshape(var_2582.astype('float64'), [4, 14, 3]))
call_2583 = func_1687_call(relay.reshape(var_2582.astype('float64'), [4, 14, 3]))
func_284_call = mod.get_global_var('func_284')
func_287_call = mutated_mod.get_global_var('func_287')
var_2585 = relay.var("var_2585", dtype = "uint64", shape = (50,))#candidate|2585|(50,)|var|uint64
const_2586 = relay.const([2,6,9,9,2,-10,4,7,-10,-1,-7,8,-6,5,-4,4,2,-7,-10,3,-10,10,2,10,-2,-1,-1,-1,9,-9,-10,-6,-2,5,1,-3,10,-3,-3,-6,-5,4,-5,6,-4,-4,5,9,3,9,-10,5,8,-4,-4,-5,-7,-6,5,4,-7,4,-8,-9,-6,7,3,-8,1,-3,2,3,-9,10,10,-5,-4,-9,3,5,8,-5,-5,3,7,-2,-6,-8,5,10,4,2,-4,2,9,-7,1,-8,-7,6,-7,-2,-3,-7,-10,4,10,-4,7,2], dtype = "int8")#candidate|2586|(110,)|const|int8
call_2584 = relay.TupleGetItem(func_284_call(relay.reshape(var_2585.astype('uint64'), [5, 10, 1]), relay.reshape(const_2586.astype('int8'), [110,]), ), 2)
call_2587 = relay.TupleGetItem(func_287_call(relay.reshape(var_2585.astype('uint64'), [5, 10, 1]), relay.reshape(const_2586.astype('int8'), [110,]), ), 2)
bop_2594 = relay.greater_equal(uop_2577.astype('bool'), call_2584.astype('bool')) # shape=(10, 16, 110)
bop_2597 = relay.greater_equal(uop_2577.astype('bool'), call_2587.astype('bool')) # shape=(10, 16, 110)
bop_2608 = relay.equal(bop_2594.astype('bool'), call_2584.astype('bool')) # shape=(10, 16, 110)
bop_2611 = relay.equal(bop_2597.astype('bool'), call_2587.astype('bool')) # shape=(10, 16, 110)
output = relay.Tuple([call_2581,var_2582,var_2585,const_2586,bop_2608,])
output2 = relay.Tuple([call_2583,var_2582,var_2585,const_2586,bop_2611,])
func_2615 = relay.Function([var_2576,var_2582,var_2585,], output)
mod['func_2615'] = func_2615
mod = relay.transform.InferType()(mod)
var_2616 = relay.var("var_2616", dtype = "float32", shape = (10, 16, 1))#candidate|2616|(10, 16, 1)|var|float32
var_2617 = relay.var("var_2617", dtype = "float64", shape = (6, 28))#candidate|2617|(6, 28)|var|float64
var_2618 = relay.var("var_2618", dtype = "uint64", shape = (50,))#candidate|2618|(50,)|var|uint64
output = func_2615(var_2616,var_2617,var_2618,)
func_2619 = relay.Function([var_2616,var_2617,var_2618,], output)
mutated_mod['func_2619'] = func_2619
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2888 = relay.var("var_2888", dtype = "uint16", shape = (8, 12, 5))#candidate|2888|(8, 12, 5)|var|uint16
var_2889 = relay.var("var_2889", dtype = "uint16", shape = (8, 12, 5))#candidate|2889|(8, 12, 5)|var|uint16
bop_2890 = relay.bitwise_and(var_2888.astype('uint16'), relay.reshape(var_2889.astype('uint16'), relay.shape_of(var_2888))) # shape=(8, 12, 5)
output = relay.Tuple([bop_2890,])
output2 = relay.Tuple([bop_2890,])
func_2901 = relay.Function([var_2888,var_2889,], output)
mod['func_2901'] = func_2901
mod = relay.transform.InferType()(mod)
mutated_mod['func_2901'] = func_2901
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2901_call = mutated_mod.get_global_var('func_2901')
var_2903 = relay.var("var_2903", dtype = "uint16", shape = (8, 12, 5))#candidate|2903|(8, 12, 5)|var|uint16
var_2904 = relay.var("var_2904", dtype = "uint16", shape = (8, 12, 5))#candidate|2904|(8, 12, 5)|var|uint16
call_2902 = func_2901_call(var_2903,var_2904,)
output = call_2902
func_2905 = relay.Function([var_2903,var_2904,], output)
mutated_mod['func_2905'] = func_2905
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3013 = relay.var("var_3013", dtype = "bool", shape = (12, 5, 3))#candidate|3013|(12, 5, 3)|var|bool
var_3014 = relay.var("var_3014", dtype = "bool", shape = (12, 5, 3))#candidate|3014|(12, 5, 3)|var|bool
bop_3015 = relay.logical_or(var_3013.astype('bool'), relay.reshape(var_3014.astype('bool'), relay.shape_of(var_3013))) # shape=(12, 5, 3)
output = relay.Tuple([bop_3015,])
output2 = relay.Tuple([bop_3015,])
func_3023 = relay.Function([var_3013,var_3014,], output)
mod['func_3023'] = func_3023
mod = relay.transform.InferType()(mod)
var_3024 = relay.var("var_3024", dtype = "bool", shape = (12, 5, 3))#candidate|3024|(12, 5, 3)|var|bool
var_3025 = relay.var("var_3025", dtype = "bool", shape = (12, 5, 3))#candidate|3025|(12, 5, 3)|var|bool
output = func_3023(var_3024,var_3025,)
func_3026 = relay.Function([var_3024,var_3025,], output)
mutated_mod['func_3026'] = func_3026
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3028 = relay.const([[[9.233471,-1.469731],[3.860941,3.608203],[-2.746293,-5.127073],[3.836999,-9.964755],[-0.783035,-0.901123],[-3.572012,7.672021],[-2.672490,-4.891592],[-8.216081,5.347281],[8.811854,-2.104718],[7.489178,1.419148],[8.723277,2.524408],[-1.946599,-2.516746],[7.769313,-4.750541],[-4.260201,-7.026915],[7.697143,3.285310],[-0.324267,3.423731]],[[9.337982,-8.935648],[2.599879,-7.925803],[7.969105,-0.189472],[1.711206,-6.015594],[6.492394,-8.640917],[-9.154047,-5.072480],[2.099837,-5.829243],[-7.493193,5.795923],[1.258380,-6.129756],[9.621652,6.237541],[-2.980455,9.205571],[-0.545963,-3.135714],[-3.547546,3.904273],[9.309206,1.326935],[-0.873506,-5.056234],[1.326058,-0.420460]],[[1.441388,-7.833201],[5.107172,-9.637192],[9.221354,-1.604899],[7.981797,9.401421],[8.613404,0.025050],[-1.070279,-6.711365],[-6.626739,3.955230],[-9.067196,-1.491752],[-4.497391,5.046017],[-0.554329,-0.987599],[0.611541,3.895781],[0.211130,-9.044926],[-9.567955,-4.725455],[-3.112838,7.943985],[6.173905,4.552442],[-0.044718,-5.550102]],[[-8.920891,-6.449058],[8.524778,-4.766804],[0.102101,7.009201],[-8.343359,-5.048101],[4.614095,0.229869],[9.580823,-4.963914],[4.816662,-8.870626],[7.084017,-5.048895],[-0.701681,-0.576558],[8.067418,-7.736176],[6.321888,-1.897717],[-1.422096,-6.266489],[8.210243,4.995373],[-2.060782,7.962894],[6.750326,9.214542],[-8.622336,-7.600802]],[[-2.030476,-5.208806],[4.244176,2.699330],[6.416410,-6.039738],[-0.554545,0.430642],[-8.884125,-6.961078],[0.877104,-6.335017],[3.290144,2.203724],[-4.158810,0.636732],[5.186132,-3.925619],[-0.605288,1.336995],[4.262185,9.154055],[-3.425573,2.239766],[-8.749436,0.166030],[-3.951928,-4.112578],[4.152776,1.984067],[-3.272813,-2.411250]],[[9.567214,-3.148992],[-9.780929,8.371867],[-1.153647,8.562971],[4.302230,0.086474],[-4.946256,7.329948],[3.724318,1.375681],[-7.299042,-3.763048],[6.160412,-9.796664],[8.207764,-9.958217],[-8.945235,-3.165952],[5.081242,2.418458],[-4.362754,-9.587650],[5.323257,8.647502],[1.614259,5.744434],[-0.391238,-6.601647],[-3.554112,-0.600745]]], dtype = "float64")#candidate|3028|(6, 16, 2)|const|float64
var_3029 = relay.var("var_3029", dtype = "float64", shape = (6, 16, 2))#candidate|3029|(6, 16, 2)|var|float64
bop_3030 = relay.greater(const_3028.astype('bool'), relay.reshape(var_3029.astype('bool'), relay.shape_of(const_3028))) # shape=(6, 16, 2)
bop_3034 = relay.greater_equal(bop_3030.astype('bool'), relay.reshape(var_3029.astype('bool'), relay.shape_of(bop_3030))) # shape=(6, 16, 2)
output = bop_3034
output2 = bop_3034
func_3040 = relay.Function([var_3029,], output)
mod['func_3040'] = func_3040
mod = relay.transform.InferType()(mod)
var_3041 = relay.var("var_3041", dtype = "float64", shape = (6, 16, 2))#candidate|3041|(6, 16, 2)|var|float64
output = func_3040(var_3041)
func_3042 = relay.Function([var_3041], output)
mutated_mod['func_3042'] = func_3042
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3075 = relay.var("var_3075", dtype = "float64", shape = (10, 10, 9))#candidate|3075|(10, 10, 9)|var|float64
uop_3076 = relay.asinh(var_3075.astype('float64')) # shape=(10, 10, 9)
func_1797_call = mod.get_global_var('func_1797')
func_1802_call = mutated_mod.get_global_var('func_1802')
var_3080 = relay.var("var_3080", dtype = "uint64", shape = (1, 270))#candidate|3080|(1, 270)|var|uint64
var_3081 = relay.var("var_3081", dtype = "float32", shape = (196, 1))#candidate|3081|(196, 1)|var|float32
var_3082 = relay.var("var_3082", dtype = "int8", shape = (22, 5))#candidate|3082|(22, 5)|var|int8
call_3079 = relay.TupleGetItem(func_1797_call(relay.reshape(var_3080.astype('uint64'), [2, 15, 9]), relay.reshape(var_3080.astype('uint64'), [2, 15, 9]), relay.reshape(var_3081.astype('float32'), [196,]), relay.reshape(var_3082.astype('int8'), [1, 110]), ), 5)
call_3083 = relay.TupleGetItem(func_1802_call(relay.reshape(var_3080.astype('uint64'), [2, 15, 9]), relay.reshape(var_3080.astype('uint64'), [2, 15, 9]), relay.reshape(var_3081.astype('float32'), [196,]), relay.reshape(var_3082.astype('int8'), [1, 110]), ), 5)
func_648_call = mod.get_global_var('func_648')
func_653_call = mutated_mod.get_global_var('func_653')
var_3086 = relay.var("var_3086", dtype = "int64", shape = (352,))#candidate|3086|(352,)|var|int64
const_3087 = relay.const([-5,-8,-5], dtype = "int32")#candidate|3087|(3,)|const|int32
var_3088 = relay.var("var_3088", dtype = "int32", shape = (3, 56))#candidate|3088|(3, 56)|var|int32
call_3085 = relay.TupleGetItem(func_648_call(relay.reshape(var_3086.astype('int64'), [8, 4, 11]), relay.reshape(const_3087.astype('int32'), [3,]), relay.reshape(var_3088.astype('int32'), [168,]), ), 0)
call_3089 = relay.TupleGetItem(func_653_call(relay.reshape(var_3086.astype('int64'), [8, 4, 11]), relay.reshape(const_3087.astype('int32'), [3,]), relay.reshape(var_3088.astype('int32'), [168,]), ), 0)
output = relay.Tuple([uop_3076,call_3079,var_3080,var_3081,var_3082,call_3085,var_3086,const_3087,var_3088,])
output2 = relay.Tuple([uop_3076,call_3083,var_3080,var_3081,var_3082,call_3089,var_3086,const_3087,var_3088,])
func_3093 = relay.Function([var_3075,var_3080,var_3081,var_3082,var_3086,var_3088,], output)
mod['func_3093'] = func_3093
mod = relay.transform.InferType()(mod)
var_3094 = relay.var("var_3094", dtype = "float64", shape = (10, 10, 9))#candidate|3094|(10, 10, 9)|var|float64
var_3095 = relay.var("var_3095", dtype = "uint64", shape = (1, 270))#candidate|3095|(1, 270)|var|uint64
var_3096 = relay.var("var_3096", dtype = "float32", shape = (196, 1))#candidate|3096|(196, 1)|var|float32
var_3097 = relay.var("var_3097", dtype = "int8", shape = (22, 5))#candidate|3097|(22, 5)|var|int8
var_3098 = relay.var("var_3098", dtype = "int64", shape = (352,))#candidate|3098|(352,)|var|int64
var_3099 = relay.var("var_3099", dtype = "int32", shape = (3, 56))#candidate|3099|(3, 56)|var|int32
output = func_3093(var_3094,var_3095,var_3096,var_3097,var_3098,var_3099,)
func_3100 = relay.Function([var_3094,var_3095,var_3096,var_3097,var_3098,var_3099,], output)
mutated_mod['func_3100'] = func_3100
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3722 = relay.var("var_3722", dtype = "float32", shape = (12, 1, 11))#candidate|3722|(12, 1, 11)|var|float32
uop_3723 = relay.log2(var_3722.astype('float32')) # shape=(12, 1, 11)
output = relay.Tuple([uop_3723,])
output2 = relay.Tuple([uop_3723,])
func_3731 = relay.Function([var_3722,], output)
mod['func_3731'] = func_3731
mod = relay.transform.InferType()(mod)
mutated_mod['func_3731'] = func_3731
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3732 = relay.var("var_3732", dtype = "float32", shape = (12, 1, 11))#candidate|3732|(12, 1, 11)|var|float32
func_3731_call = mutated_mod.get_global_var('func_3731')
call_3733 = func_3731_call(var_3732)
output = call_3733
func_3734 = relay.Function([var_3732], output)
mutated_mod['func_3734'] = func_3734
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4041 = relay.var("var_4041", dtype = "float64", shape = (2, 4, 3))#candidate|4041|(2, 4, 3)|var|float64
uop_4042 = relay.erf(var_4041.astype('float64')) # shape=(2, 4, 3)
output = relay.Tuple([uop_4042,])
output2 = relay.Tuple([uop_4042,])
func_4049 = relay.Function([var_4041,], output)
mod['func_4049'] = func_4049
mod = relay.transform.InferType()(mod)
var_4050 = relay.var("var_4050", dtype = "float64", shape = (2, 4, 3))#candidate|4050|(2, 4, 3)|var|float64
output = func_4049(var_4050)
func_4051 = relay.Function([var_4050], output)
mutated_mod['func_4051'] = func_4051
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4104 = relay.const([[[-5,9,2,-10],[-5,-9,6,1],[-6,-3,-9,7],[9,-10,10,-8],[10,-9,-3,1],[2,8,-1,-5],[-9,8,-1,1],[-2,2,-2,7],[10,-6,-4,10],[7,5,-6,-7],[-9,2,-9,-3],[-5,-4,-7,-2],[-8,-1,-3,8],[8,10,-4,-6],[3,4,-2,-6],[3,-7,3,-9]],[[-6,-3,1,1],[-5,-1,9,1],[-7,5,-5,8],[10,-10,3,-6],[-10,-9,10,-8],[2,-3,9,2],[-10,-5,7,5],[-9,2,4,2],[-7,-3,-3,-2],[-10,-8,9,-7],[7,6,-7,1],[5,9,-9,3],[4,-3,-9,-3],[-9,10,-1,9],[-8,1,-7,1],[-6,-3,-1,-1]]], dtype = "int64")#candidate|4104|(2, 16, 4)|const|int64
var_4105 = relay.var("var_4105", dtype = "int64", shape = (2, 16, 4))#candidate|4105|(2, 16, 4)|var|int64
bop_4106 = relay.bitwise_or(const_4104.astype('int64'), relay.reshape(var_4105.astype('int64'), relay.shape_of(const_4104))) # shape=(2, 16, 4)
output = relay.Tuple([bop_4106,])
output2 = relay.Tuple([bop_4106,])
func_4111 = relay.Function([var_4105,], output)
mod['func_4111'] = func_4111
mod = relay.transform.InferType()(mod)
var_4112 = relay.var("var_4112", dtype = "int64", shape = (2, 16, 4))#candidate|4112|(2, 16, 4)|var|int64
output = func_4111(var_4112)
func_4113 = relay.Function([var_4112], output)
mutated_mod['func_4113'] = func_4113
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4130 = relay.const([[[-4.134748,5.857435,8.766014,8.434953,-2.152859,-9.180190,-1.742494,5.835519,-6.837015,-0.130429,5.278531,-7.958437,0.079617],[1.124661,-0.283516,1.086197,-8.105325,-5.436760,6.411010,4.937840,0.811565,7.462096,1.771528,9.662601,-7.717933,7.518801],[-6.275484,-7.119538,-7.970847,-6.632103,3.128496,-1.417483,-5.369215,1.997417,-3.697903,4.355219,-8.203316,8.609440,-3.893287],[4.608325,9.798020,-3.252182,-0.077114,4.023477,1.084415,-0.551507,6.563628,-3.270107,0.592612,0.799936,-5.357569,9.538674],[3.500520,9.573639,5.730438,-9.161425,5.897993,-9.181357,-8.134855,1.240839,-5.225537,-2.222826,-4.115488,0.126205,-9.414849],[9.205220,-6.257228,7.862005,-3.830692,4.381770,6.294309,-5.135648,-0.726756,-7.020510,-9.011221,-9.053363,1.243717,-4.299378],[2.034126,2.754109,-9.613897,3.860196,-4.072360,-7.316525,1.517369,-6.749914,-8.356095,5.334957,-0.356583,3.865447,1.184092],[4.125041,-9.559281,-2.410916,1.210991,5.249199,1.689740,-0.760887,3.139320,-8.176308,-5.759537,2.341787,4.603677,-2.192078],[-4.294504,-6.641159,7.474411,0.989979,9.872671,-1.579935,1.402911,-1.511135,-9.834742,-3.568297,7.339079,-0.201286,-3.806054],[-8.609001,-6.774348,5.564414,-5.850821,9.309234,6.307545,9.311352,-7.361096,5.387044,6.022585,-0.696541,7.317607,6.460063]],[[8.923290,-9.365617,1.824878,5.376883,8.245102,5.905539,-4.261487,-8.031833,6.622955,-3.543071,2.530780,4.808456,8.973566],[-5.343232,7.969629,-0.861042,1.672060,-3.011262,5.366558,-1.374896,-7.128487,4.401446,-1.558779,-7.156640,2.834261,-9.203631],[-6.201734,-8.200698,8.239547,-4.559488,-5.584891,-6.127604,-6.374369,5.703366,-0.970512,-9.654687,6.023570,-3.290090,0.914066],[0.990090,1.643906,2.408657,9.489313,-5.173483,-1.948889,6.421836,9.743789,-4.192992,-9.571267,9.806389,-9.386946,8.015989],[5.162438,0.823419,-5.638073,-6.651632,-0.280987,-2.082045,9.027168,3.704157,8.590944,-8.537981,-7.459651,-0.344721,-1.894836],[8.185682,-4.949333,-1.466937,-7.169553,-2.966769,-2.959041,9.105269,5.390366,7.836065,-3.708756,-1.926335,8.605059,-1.690363],[-8.300511,2.863218,-2.270968,9.027185,7.411597,6.813738,7.513009,4.640494,-7.084745,7.584182,-8.053090,-0.808854,8.986603],[-8.165519,8.327940,-7.231406,-3.423302,9.261953,-3.494725,7.499826,-3.361031,-8.557169,-5.608773,-6.078263,-9.093007,-3.413802],[-0.341302,2.005197,-9.881850,-1.564020,-5.150539,7.833733,-1.824557,4.999369,2.319339,1.423412,3.544549,7.892775,4.353827],[-5.158908,5.560433,-7.912708,3.691561,7.242625,1.941178,-1.816808,-0.399308,-9.978578,-0.957947,-0.721401,-6.428426,0.211106]],[[1.230365,-1.593800,-2.681577,-9.234400,1.731082,7.595377,-3.991183,-0.636361,0.968478,3.105939,-6.258796,-8.961152,7.899589],[-1.726309,-1.802408,-6.192246,2.852447,-2.621118,2.030311,3.572201,3.711673,-6.513657,-3.642343,-9.012246,0.517743,7.058605],[5.370160,-9.736311,-6.620988,9.516100,-1.312228,-5.156420,-2.081416,-7.151967,7.182846,-8.126643,-9.374509,-0.483110,-1.401489],[-6.660270,-8.219171,2.567854,-6.026319,4.003596,9.435809,4.864175,-1.118154,6.191819,7.432785,-4.849857,9.037519,4.475490],[4.507589,-8.692362,-8.432788,5.512885,2.360535,4.444219,-8.922044,-7.322509,6.231817,-4.744335,-4.597439,-0.939988,7.482673],[-4.242383,4.671182,-2.617395,-2.514781,-8.927053,-5.219543,2.445430,5.363955,2.047518,7.074265,8.611978,8.017364,-2.571913],[7.648155,6.476155,-4.402758,5.759785,-8.955331,-6.926329,7.448832,5.050876,8.889943,3.619199,5.970299,-7.304518,-0.387878],[6.817171,2.024404,2.455526,-3.242805,7.392789,4.143166,6.783921,1.167038,-3.133539,-6.806273,-1.346105,-3.052538,-2.434586],[-9.759226,6.008658,-7.204692,-0.671744,-3.670645,-8.513365,3.965291,2.679613,3.340692,-3.235780,0.934967,1.240790,-3.329594],[5.437983,7.779972,5.791558,-6.264153,-5.416986,5.239186,6.255797,7.562702,8.257821,5.247882,7.738429,1.221129,6.799093]],[[-1.613161,-9.570234,-3.499502,5.980930,-0.053257,9.669665,3.888554,6.979120,7.894679,9.616782,2.435474,1.407114,8.073240],[4.494886,-3.442143,1.589874,4.135634,5.459070,2.241805,4.052363,8.338663,5.535591,-0.520234,-6.669804,1.501798,-9.905845],[-3.130851,9.900516,-3.315951,-8.986956,-2.468655,7.932277,0.720283,7.452457,-8.226465,-5.292841,-2.706730,-7.742710,0.884789],[-7.685846,-7.354767,7.098054,-8.975981,6.580880,6.643232,9.818692,8.397259,8.243214,7.018755,-1.233472,1.828644,-3.303122],[-9.207510,-1.200877,5.397109,-0.693771,-7.219723,-7.422442,-2.160225,0.727759,7.762540,9.120018,-8.128991,1.284174,-7.654353],[8.377537,8.806043,2.275669,-0.302998,2.627514,-0.195395,-7.943434,2.407168,6.229931,-9.440738,5.351049,1.017103,-8.418395],[6.560114,8.528486,9.376636,0.415420,-3.633253,-6.926119,-9.864365,-7.002383,1.642136,3.562715,9.681404,3.432154,-8.619367],[8.368544,2.406413,6.180249,-4.276359,-9.075312,9.326246,-1.212774,-7.963745,-2.761364,-7.373239,6.267963,0.470062,-3.795381],[1.990281,-5.992400,-1.501474,0.078594,-5.253962,-0.854343,-8.088325,-1.927346,-7.547070,2.258115,-5.816771,6.841983,0.075276],[-9.940493,-4.899418,7.400637,-4.005751,3.210612,-5.721924,7.088202,7.425819,3.256504,-6.975511,0.673106,-0.656473,-6.706948]],[[-5.371570,9.441379,-1.608606,1.942377,-8.479396,1.771960,-9.124349,8.612234,0.198291,0.900513,-1.623180,-2.996634,3.560820],[6.279189,6.252668,-4.880285,7.878418,8.861334,2.199018,-4.263540,1.641690,9.916291,-7.247532,-5.450456,2.448849,-0.583647],[-5.695610,-4.556226,-1.061402,6.215516,2.838714,-1.455047,4.982117,4.319852,-3.698805,-3.210363,0.146339,9.668176,-3.882574],[4.395030,-9.893277,2.512242,8.905873,-5.879726,8.468883,5.652489,3.431297,-0.874823,3.033522,9.464684,6.964283,1.016248],[8.086418,1.077557,3.419312,2.354104,-3.802099,-4.261422,6.072628,-9.028604,1.882711,0.521594,9.338125,8.621813,8.726722],[-9.577640,5.226721,1.449291,-3.985915,-9.310806,-1.181226,4.718920,2.011134,-1.867512,-5.325842,3.981556,-9.079375,-2.456935],[-3.197162,-8.239979,7.643508,8.621356,-4.012386,7.976345,7.513856,-7.754578,-6.884710,-2.868946,-3.369132,-8.922949,7.995863],[-6.156435,-3.987861,7.176603,-8.454955,6.807810,-6.086051,-4.374744,7.353378,-2.130901,-7.611886,-8.386916,-1.888665,-2.013624],[7.424451,-1.378389,-2.346197,-0.259536,7.270246,-8.442741,9.756568,5.634552,-9.642609,2.626888,-9.996028,-5.212292,-2.271518],[8.175038,0.122799,7.347775,-2.438771,-7.849681,-3.925397,1.973066,-1.577240,-3.061470,3.410471,-5.033695,6.034652,-3.214751]]], dtype = "float64")#candidate|4130|(5, 10, 13)|const|float64
uop_4131 = relay.acos(const_4130.astype('float64')) # shape=(5, 10, 13)
bop_4134 = relay.bitwise_or(uop_4131.astype('int8'), relay.reshape(const_4130.astype('int8'), relay.shape_of(uop_4131))) # shape=(5, 10, 13)
bop_4143 = relay.minimum(uop_4131.astype('uint32'), relay.reshape(bop_4134.astype('uint32'), relay.shape_of(uop_4131))) # shape=(5, 10, 13)
output = bop_4143
output2 = bop_4143
func_4147 = relay.Function([], output)
mod['func_4147'] = func_4147
mod = relay.transform.InferType()(mod)
output = func_4147()
func_4148 = relay.Function([], output)
mutated_mod['func_4148'] = func_4148
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4147_call = mod.get_global_var('func_4147')
func_4148_call = mutated_mod.get_global_var('func_4148')
call_4210 = func_4147_call()
call_4211 = func_4147_call()
func_1951_call = mod.get_global_var('func_1951')
func_1953_call = mutated_mod.get_global_var('func_1953')
var_4218 = relay.var("var_4218", dtype = "uint8", shape = (15,))#candidate|4218|(15,)|var|uint8
call_4217 = func_1951_call(relay.reshape(var_4218.astype('uint8'), [1, 15, 1]))
call_4219 = func_1951_call(relay.reshape(var_4218.astype('uint8'), [1, 15, 1]))
func_1627_call = mod.get_global_var('func_1627')
func_1630_call = mutated_mod.get_global_var('func_1630')
const_4223 = relay.const([[-1],[3],[-1],[1],[9],[-5],[2],[8],[9],[-8],[-2],[4],[-9],[8],[3],[6],[-2],[5],[4],[-9],[9],[-3],[-1],[4],[1],[-4],[6],[-8],[7],[6],[1],[3],[1],[-9],[7],[9],[3],[4],[7],[4],[1],[-10],[6],[-3],[4],[-4],[-1],[10],[-6],[-6],[-8],[-6],[9],[5],[-9],[1],[-6],[8],[-10],[6],[10],[1],[-8],[1],[10],[4],[4],[-1],[1],[6],[-6],[1],[-9],[6],[10],[5],[4],[1],[-5],[-6],[2],[4],[-2],[-7],[-2],[5],[10],[-10],[5],[-8],[9],[-6],[9],[7],[-2],[10],[-4],[7],[1],[9],[7],[-1],[-9],[7],[8],[2],[-1],[10],[-8],[4]], dtype = "int8")#candidate|4223|(110, 1)|const|int8
call_4222 = relay.TupleGetItem(func_1627_call(relay.reshape(const_4223.astype('int8'), [110,])), 1)
call_4224 = relay.TupleGetItem(func_1630_call(relay.reshape(const_4223.astype('int8'), [110,])), 1)
bop_4231 = relay.less(const_4223.astype('bool'), var_4218.astype('bool')) # shape=(110, 15)
output = relay.Tuple([call_4210,call_4217,call_4222,bop_4231,])
output2 = relay.Tuple([call_4211,call_4219,call_4224,bop_4231,])
func_4235 = relay.Function([var_4218,], output)
mod['func_4235'] = func_4235
mod = relay.transform.InferType()(mod)
mutated_mod['func_4235'] = func_4235
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4236 = relay.var("var_4236", dtype = "uint8", shape = (15,))#candidate|4236|(15,)|var|uint8
func_4235_call = mutated_mod.get_global_var('func_4235')
call_4237 = func_4235_call(var_4236)
output = call_4237
func_4238 = relay.Function([var_4236], output)
mutated_mod['func_4238'] = func_4238
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4147_call = mod.get_global_var('func_4147')
func_4148_call = mutated_mod.get_global_var('func_4148')
call_4338 = func_4147_call()
call_4339 = func_4147_call()
func_1659_call = mod.get_global_var('func_1659')
func_1662_call = mutated_mod.get_global_var('func_1662')
var_4341 = relay.var("var_4341", dtype = "float32", shape = (196,))#candidate|4341|(196,)|var|float32
const_4342 = relay.const([[-0.090081,-0.513775],[9.703410,1.126607],[-0.756568,0.946827],[9.808853,7.112829],[0.344399,-0.767125],[6.845139,6.156667],[-1.088318,2.648901],[1.408222,-7.690995],[-5.037854,6.360142],[7.361569,-3.364134],[5.495071,-7.199729],[-0.097940,5.180606]], dtype = "float64")#candidate|4342|(12, 2)|const|float64
call_4340 = relay.TupleGetItem(func_1659_call(relay.reshape(var_4341.astype('float32'), [14, 7, 2]), relay.reshape(const_4342.astype('float64'), [24,]), ), 1)
call_4343 = relay.TupleGetItem(func_1662_call(relay.reshape(var_4341.astype('float32'), [14, 7, 2]), relay.reshape(const_4342.astype('float64'), [24,]), ), 1)
output = relay.Tuple([call_4338,call_4340,var_4341,const_4342,])
output2 = relay.Tuple([call_4339,call_4343,var_4341,const_4342,])
func_4345 = relay.Function([var_4341,], output)
mod['func_4345'] = func_4345
mod = relay.transform.InferType()(mod)
var_4346 = relay.var("var_4346", dtype = "float32", shape = (196,))#candidate|4346|(196,)|var|float32
output = func_4345(var_4346)
func_4347 = relay.Function([var_4346], output)
mutated_mod['func_4347'] = func_4347
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4384 = relay.var("var_4384", dtype = "bool", shape = (8, 8, 8))#candidate|4384|(8, 8, 8)|var|bool
var_4385 = relay.var("var_4385", dtype = "bool", shape = (8, 8, 8))#candidate|4385|(8, 8, 8)|var|bool
bop_4386 = relay.logical_or(var_4384.astype('bool'), relay.reshape(var_4385.astype('bool'), relay.shape_of(var_4384))) # shape=(8, 8, 8)
output = bop_4386
output2 = bop_4386
func_4390 = relay.Function([var_4384,var_4385,], output)
mod['func_4390'] = func_4390
mod = relay.transform.InferType()(mod)
mutated_mod['func_4390'] = func_4390
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4390_call = mutated_mod.get_global_var('func_4390')
var_4392 = relay.var("var_4392", dtype = "bool", shape = (8, 8, 8))#candidate|4392|(8, 8, 8)|var|bool
var_4393 = relay.var("var_4393", dtype = "bool", shape = (8, 8, 8))#candidate|4393|(8, 8, 8)|var|bool
call_4391 = func_4390_call(var_4392,var_4393,)
output = call_4391
func_4394 = relay.Function([var_4392,var_4393,], output)
mutated_mod['func_4394'] = func_4394
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4147_call = mod.get_global_var('func_4147')
func_4148_call = mutated_mod.get_global_var('func_4148')
call_4404 = func_4147_call()
call_4405 = func_4147_call()
output = relay.Tuple([call_4404,])
output2 = relay.Tuple([call_4405,])
func_4416 = relay.Function([], output)
mod['func_4416'] = func_4416
mod = relay.transform.InferType()(mod)
output = func_4416()
func_4417 = relay.Function([], output)
mutated_mod['func_4417'] = func_4417
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4416_call = mod.get_global_var('func_4416')
func_4417_call = mutated_mod.get_global_var('func_4417')
call_4418 = relay.TupleGetItem(func_4416_call(), 0)
call_4419 = relay.TupleGetItem(func_4417_call(), 0)
uop_4427 = relay.atanh(call_4418.astype('float64')) # shape=(5, 10, 13)
uop_4429 = relay.atanh(call_4419.astype('float64')) # shape=(5, 10, 13)
var_4430 = relay.var("var_4430", dtype = "float64", shape = (5, 10, 13))#candidate|4430|(5, 10, 13)|var|float64
bop_4431 = relay.floor_divide(uop_4427.astype('float64'), relay.reshape(var_4430.astype('float64'), relay.shape_of(uop_4427))) # shape=(5, 10, 13)
bop_4434 = relay.floor_divide(uop_4429.astype('float64'), relay.reshape(var_4430.astype('float64'), relay.shape_of(uop_4429))) # shape=(5, 10, 13)
func_4111_call = mod.get_global_var('func_4111')
func_4113_call = mutated_mod.get_global_var('func_4113')
var_4446 = relay.var("var_4446", dtype = "int64", shape = (64, 2))#candidate|4446|(64, 2)|var|int64
call_4445 = relay.TupleGetItem(func_4111_call(relay.reshape(var_4446.astype('int64'), [2, 16, 4])), 0)
call_4447 = relay.TupleGetItem(func_4113_call(relay.reshape(var_4446.astype('int64'), [2, 16, 4])), 0)
func_648_call = mod.get_global_var('func_648')
func_653_call = mutated_mod.get_global_var('func_653')
var_4450 = relay.var("var_4450", dtype = "int64", shape = (176, 2))#candidate|4450|(176, 2)|var|int64
const_4451 = relay.const([4,-7,10], dtype = "int32")#candidate|4451|(3,)|const|int32
var_4452 = relay.var("var_4452", dtype = "int32", shape = (168,))#candidate|4452|(168,)|var|int32
call_4449 = relay.TupleGetItem(func_648_call(relay.reshape(var_4450.astype('int64'), [8, 4, 11]), relay.reshape(const_4451.astype('int32'), [3,]), relay.reshape(var_4452.astype('int32'), [168,]), ), 2)
call_4453 = relay.TupleGetItem(func_653_call(relay.reshape(var_4450.astype('int64'), [8, 4, 11]), relay.reshape(const_4451.astype('int32'), [3,]), relay.reshape(var_4452.astype('int32'), [168,]), ), 2)
bop_4468 = relay.minimum(var_4446.astype('int32'), relay.reshape(call_4445.astype('int32'), relay.shape_of(var_4446))) # shape=(64, 2)
bop_4471 = relay.minimum(var_4446.astype('int32'), relay.reshape(call_4447.astype('int32'), relay.shape_of(var_4446))) # shape=(64, 2)
func_2901_call = mod.get_global_var('func_2901')
func_2905_call = mutated_mod.get_global_var('func_2905')
var_4474 = relay.var("var_4474", dtype = "uint16", shape = (480,))#candidate|4474|(480,)|var|uint16
call_4473 = relay.TupleGetItem(func_2901_call(relay.reshape(var_4474.astype('uint16'), [8, 12, 5]), relay.reshape(var_4474.astype('uint16'), [8, 12, 5]), ), 0)
call_4475 = relay.TupleGetItem(func_2905_call(relay.reshape(var_4474.astype('uint16'), [8, 12, 5]), relay.reshape(var_4474.astype('uint16'), [8, 12, 5]), ), 0)
output = relay.Tuple([bop_4431,call_4449,var_4450,const_4451,var_4452,bop_4468,call_4473,var_4474,])
output2 = relay.Tuple([bop_4434,call_4453,var_4450,const_4451,var_4452,bop_4471,call_4475,var_4474,])
func_4479 = relay.Function([var_4430,var_4446,var_4450,var_4452,var_4474,], output)
mod['func_4479'] = func_4479
mod = relay.transform.InferType()(mod)
mutated_mod['func_4479'] = func_4479
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4479_call = mutated_mod.get_global_var('func_4479')
var_4481 = relay.var("var_4481", dtype = "float64", shape = (5, 10, 13))#candidate|4481|(5, 10, 13)|var|float64
var_4482 = relay.var("var_4482", dtype = "int64", shape = (64, 2))#candidate|4482|(64, 2)|var|int64
var_4483 = relay.var("var_4483", dtype = "int64", shape = (176, 2))#candidate|4483|(176, 2)|var|int64
var_4484 = relay.var("var_4484", dtype = "int32", shape = (168,))#candidate|4484|(168,)|var|int32
var_4485 = relay.var("var_4485", dtype = "uint16", shape = (480,))#candidate|4485|(480,)|var|uint16
call_4480 = func_4479_call(var_4481,var_4482,var_4483,var_4484,var_4485,)
output = call_4480
func_4486 = relay.Function([var_4481,var_4482,var_4483,var_4484,var_4485,], output)
mutated_mod['func_4486'] = func_4486
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4495 = relay.var("var_4495", dtype = "bool", shape = (4, 14, 8))#candidate|4495|(4, 14, 8)|var|bool
var_4496 = relay.var("var_4496", dtype = "bool", shape = (4, 14, 8))#candidate|4496|(4, 14, 8)|var|bool
bop_4497 = relay.logical_and(var_4495.astype('bool'), relay.reshape(var_4496.astype('bool'), relay.shape_of(var_4495))) # shape=(4, 14, 8)
func_3023_call = mod.get_global_var('func_3023')
func_3026_call = mutated_mod.get_global_var('func_3026')
var_4507 = relay.var("var_4507", dtype = "bool", shape = (180,))#candidate|4507|(180,)|var|bool
call_4506 = relay.TupleGetItem(func_3023_call(relay.reshape(var_4507.astype('bool'), [12, 5, 3]), relay.reshape(var_4507.astype('bool'), [12, 5, 3]), ), 0)
call_4508 = relay.TupleGetItem(func_3026_call(relay.reshape(var_4507.astype('bool'), [12, 5, 3]), relay.reshape(var_4507.astype('bool'), [12, 5, 3]), ), 0)
bop_4510 = relay.logical_or(var_4496.astype('bool'), relay.reshape(bop_4497.astype('bool'), relay.shape_of(var_4496))) # shape=(4, 14, 8)
func_4049_call = mod.get_global_var('func_4049')
func_4051_call = mutated_mod.get_global_var('func_4051')
var_4516 = relay.var("var_4516", dtype = "float64", shape = (24,))#candidate|4516|(24,)|var|float64
call_4515 = relay.TupleGetItem(func_4049_call(relay.reshape(var_4516.astype('float64'), [2, 4, 3])), 0)
call_4517 = relay.TupleGetItem(func_4051_call(relay.reshape(var_4516.astype('float64'), [2, 4, 3])), 0)
output = relay.Tuple([call_4506,var_4507,bop_4510,call_4515,var_4516,])
output2 = relay.Tuple([call_4508,var_4507,bop_4510,call_4517,var_4516,])
func_4518 = relay.Function([var_4495,var_4496,var_4507,var_4516,], output)
mod['func_4518'] = func_4518
mod = relay.transform.InferType()(mod)
var_4519 = relay.var("var_4519", dtype = "bool", shape = (4, 14, 8))#candidate|4519|(4, 14, 8)|var|bool
var_4520 = relay.var("var_4520", dtype = "bool", shape = (4, 14, 8))#candidate|4520|(4, 14, 8)|var|bool
var_4521 = relay.var("var_4521", dtype = "bool", shape = (180,))#candidate|4521|(180,)|var|bool
var_4522 = relay.var("var_4522", dtype = "float64", shape = (24,))#candidate|4522|(24,)|var|float64
output = func_4518(var_4519,var_4520,var_4521,var_4522,)
func_4523 = relay.Function([var_4519,var_4520,var_4521,var_4522,], output)
mutated_mod['func_4523'] = func_4523
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4416_call = mod.get_global_var('func_4416')
func_4417_call = mutated_mod.get_global_var('func_4417')
call_4530 = relay.TupleGetItem(func_4416_call(), 0)
call_4531 = relay.TupleGetItem(func_4417_call(), 0)
func_1951_call = mod.get_global_var('func_1951')
func_1953_call = mutated_mod.get_global_var('func_1953')
var_4541 = relay.var("var_4541", dtype = "uint8", shape = (15,))#candidate|4541|(15,)|var|uint8
call_4540 = func_1951_call(relay.reshape(var_4541.astype('uint8'), [1, 15, 1]))
call_4542 = func_1951_call(relay.reshape(var_4541.astype('uint8'), [1, 15, 1]))
func_284_call = mod.get_global_var('func_284')
func_287_call = mutated_mod.get_global_var('func_287')
const_4544 = relay.const([-4,-8,-4,-10,-3,2,-5,2,8,3,1,6,-4,-7,1,-7,-2,4,7,-1,-8,10,7,3,4,-3,-7,-6,-9,4,-2,-6,9,10,-4,8,4,-9,8,8,-10,-8,-1,8,9,3,4,-6,1,-8], dtype = "uint64")#candidate|4544|(50,)|const|uint64
const_4545 = relay.const([-1,2,3,2,3,4,8,8,-7,-1,-8,2,-7,2,-10,-4,1,10,8,-5,3,2,5,9,-7,-6,5,-9,-1,-10,1,1,-1,-5,-1,8,10,-5,-10,-10,-5,1,4,-4,2,-7,9,-2,7,9,-8,1,-7,-6,5,1,2,-1,2,3,-3,-7,-6,-5,8,2,9,5,-2,-10,-9,-8,-4,9,-6,2,-5,-2,-7,6,10,-1,-1,-4,9,1,-8,-1,10,10,4,-5,-8,2,5,9,5,-4,-8,1,-4,-5,3,-5,-8,9,7,-3,-1,8], dtype = "int8")#candidate|4545|(110,)|const|int8
call_4543 = relay.TupleGetItem(func_284_call(relay.reshape(const_4544.astype('uint64'), [5, 10, 1]), relay.reshape(const_4545.astype('int8'), [110,]), ), 1)
call_4546 = relay.TupleGetItem(func_287_call(relay.reshape(const_4544.astype('uint64'), [5, 10, 1]), relay.reshape(const_4545.astype('int8'), [110,]), ), 1)
bop_4547 = relay.bitwise_or(const_4544.astype('uint64'), call_4540.astype('uint64')) # shape=(1, 15, 50)
bop_4550 = relay.bitwise_or(const_4544.astype('uint64'), call_4542.astype('uint64')) # shape=(1, 15, 50)
const_4554 = relay.const([-7,-3,-3,-4,-2,-3,-1,-7,10,-1,2,10,-2,3,3,5,8,-4,-1,-8,-5,-5,-1,-7,4,3,7,-8,-8,-10,7,-1,-5,4,3,-1,6,-7,10,-9,1,-2,7,7,9,4,-5,2,2,-8,-1,-3,6,-5,1,-1,-8,-1,3,10,-7,1,-1,-4,1,8,-2,1,1,2,-2,6,-6,-6,-5,2,-1,4,7,7,-9,-2,-7,8,-10,2,3,-3,7,9,-4,-5,-5,-10,-8,-2,3,-9,8,-8,8,-10,2,-2,-3,-4,-4,-3,-8,3], dtype = "int8")#candidate|4554|(110,)|const|int8
bop_4555 = relay.left_shift(const_4545.astype('int8'), relay.reshape(const_4554.astype('int8'), relay.shape_of(const_4545))) # shape=(110,)
output = relay.Tuple([call_4530,var_4541,call_4543,bop_4547,bop_4555,])
output2 = relay.Tuple([call_4531,var_4541,call_4546,bop_4550,bop_4555,])
func_4567 = relay.Function([var_4541,], output)
mod['func_4567'] = func_4567
mod = relay.transform.InferType()(mod)
var_4568 = relay.var("var_4568", dtype = "uint8", shape = (15,))#candidate|4568|(15,)|var|uint8
output = func_4567(var_4568)
func_4569 = relay.Function([var_4568], output)
mutated_mod['func_4569'] = func_4569
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4147_call = mod.get_global_var('func_4147')
func_4148_call = mutated_mod.get_global_var('func_4148')
call_4621 = func_4147_call()
call_4622 = func_4147_call()
uop_4625 = relay.erf(call_4621.astype('float64')) # shape=(5, 10, 13)
uop_4627 = relay.erf(call_4622.astype('float64')) # shape=(5, 10, 13)
output = relay.Tuple([uop_4625,])
output2 = relay.Tuple([uop_4627,])
func_4640 = relay.Function([], output)
mod['func_4640'] = func_4640
mod = relay.transform.InferType()(mod)
mutated_mod['func_4640'] = func_4640
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4640_call = mutated_mod.get_global_var('func_4640')
call_4641 = func_4640_call()
output = call_4641
func_4642 = relay.Function([], output)
mutated_mod['func_4642'] = func_4642
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4147_call = mod.get_global_var('func_4147')
func_4148_call = mutated_mod.get_global_var('func_4148')
call_4657 = func_4147_call()
call_4658 = func_4147_call()
output = relay.Tuple([call_4657,])
output2 = relay.Tuple([call_4658,])
func_4660 = relay.Function([], output)
mod['func_4660'] = func_4660
mod = relay.transform.InferType()(mod)
mutated_mod['func_4660'] = func_4660
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4660_call = mutated_mod.get_global_var('func_4660')
call_4661 = func_4660_call()
output = call_4661
func_4662 = relay.Function([], output)
mutated_mod['func_4662'] = func_4662
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4660_call = mod.get_global_var('func_4660')
func_4662_call = mutated_mod.get_global_var('func_4662')
call_4687 = relay.TupleGetItem(func_4660_call(), 0)
call_4688 = relay.TupleGetItem(func_4662_call(), 0)
output = call_4687
output2 = call_4688
func_4693 = relay.Function([], output)
mod['func_4693'] = func_4693
mod = relay.transform.InferType()(mod)
output = func_4693()
func_4694 = relay.Function([], output)
mutated_mod['func_4694'] = func_4694
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4693_call = mod.get_global_var('func_4693')
func_4694_call = mutated_mod.get_global_var('func_4694')
call_4716 = func_4693_call()
call_4717 = func_4693_call()
output = relay.Tuple([call_4716,])
output2 = relay.Tuple([call_4717,])
func_4734 = relay.Function([], output)
mod['func_4734'] = func_4734
mod = relay.transform.InferType()(mod)
mutated_mod['func_4734'] = func_4734
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4734_call = mutated_mod.get_global_var('func_4734')
call_4735 = func_4734_call()
output = call_4735
func_4736 = relay.Function([], output)
mutated_mod['func_4736'] = func_4736
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4416_call = mod.get_global_var('func_4416')
func_4417_call = mutated_mod.get_global_var('func_4417')
call_4767 = relay.TupleGetItem(func_4416_call(), 0)
call_4768 = relay.TupleGetItem(func_4417_call(), 0)
var_4779 = relay.var("var_4779", dtype = "uint32", shape = (5, 10, 13))#candidate|4779|(5, 10, 13)|var|uint32
bop_4780 = relay.less(call_4767.astype('bool'), relay.reshape(var_4779.astype('bool'), relay.shape_of(call_4767))) # shape=(5, 10, 13)
bop_4783 = relay.less(call_4768.astype('bool'), relay.reshape(var_4779.astype('bool'), relay.shape_of(call_4768))) # shape=(5, 10, 13)
bop_4784 = relay.multiply(call_4767.astype('uint16'), relay.reshape(bop_4780.astype('uint16'), relay.shape_of(call_4767))) # shape=(5, 10, 13)
bop_4787 = relay.multiply(call_4768.astype('uint16'), relay.reshape(bop_4783.astype('uint16'), relay.shape_of(call_4768))) # shape=(5, 10, 13)
output = bop_4784
output2 = bop_4787
func_4799 = relay.Function([var_4779,], output)
mod['func_4799'] = func_4799
mod = relay.transform.InferType()(mod)
mutated_mod['func_4799'] = func_4799
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4800 = relay.var("var_4800", dtype = "uint32", shape = (5, 10, 13))#candidate|4800|(5, 10, 13)|var|uint32
func_4799_call = mutated_mod.get_global_var('func_4799')
call_4801 = func_4799_call(var_4800)
output = call_4801
func_4802 = relay.Function([var_4800], output)
mutated_mod['func_4802'] = func_4802
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4693_call = mod.get_global_var('func_4693')
func_4694_call = mutated_mod.get_global_var('func_4694')
call_4809 = func_4693_call()
call_4810 = func_4693_call()
func_4799_call = mod.get_global_var('func_4799')
func_4802_call = mutated_mod.get_global_var('func_4802')
call_4813 = func_4799_call(relay.reshape(call_4809.astype('uint32'), [5, 10, 13]))
call_4814 = func_4799_call(relay.reshape(call_4809.astype('uint32'), [5, 10, 13]))
bop_4822 = relay.subtract(call_4813.astype('int16'), relay.reshape(call_4809.astype('int16'), relay.shape_of(call_4813))) # shape=(5, 10, 13)
bop_4825 = relay.subtract(call_4814.astype('int16'), relay.reshape(call_4810.astype('int16'), relay.shape_of(call_4814))) # shape=(5, 10, 13)
func_2615_call = mod.get_global_var('func_2615')
func_2619_call = mutated_mod.get_global_var('func_2619')
var_4831 = relay.var("var_4831", dtype = "float32", shape = (4, 40))#candidate|4831|(4, 40)|var|float32
const_4832 = relay.const([9.568686,-3.670579,-5.400932,-0.997045,-8.816189,8.858461,1.046411,-9.372849,0.491418,4.985816,-6.505763,5.800720,-6.984453,-9.412617,-5.439292,-3.797866,-5.593337,-6.311923,-8.423235,-7.808283,-4.820731,9.119401,0.046578,-7.246868,-5.621162,7.169718,-7.653444,0.370645,4.078528,-1.482044,-0.805692,9.962172,1.437859,-6.392114,-5.134144,-7.596190,-9.040611,-0.589925,0.907034,4.543163,-2.492205,-6.409916,3.305513,-7.310509,-3.195166,1.132836,5.333757,8.623059,-7.244528,7.997522,-9.917550,9.255223,0.656372,-9.708061,6.318588,-9.818614,-9.347290,-9.389345,-0.607651,-4.338185,0.638514,-6.326498,-0.181942,3.752847,3.759859,4.122740,-2.615966,-6.263598,-3.538134,-0.019853,-5.731969,-1.728506,6.848114,1.304231,4.407960,-5.376179,7.368453,2.244383,-6.138556,-3.427647,9.629895,1.021079,-6.965544,4.377537,-2.871312,-5.532342,-3.801909,-8.833926,4.682574,-9.978399,5.905067,6.501501,0.756071,9.247182,4.935223,5.909380,5.633417,-0.053190,-7.265603,9.412638,9.373973,-3.129061,-0.077179,-8.697216,-9.104365,-0.684708,6.081015,-7.472390,-2.441138,8.878909,8.514212,5.200062,1.655765,-2.405368,2.964230,1.879806,-1.908888,3.997212,-3.056647,-5.467899,-6.651863,-1.797167,1.027739,-4.485945,-2.809939,4.636048,-3.109896,8.690864,8.507316,8.943164,8.163542,6.449680,-3.834585,-3.956287,-1.169594,6.606290,9.187795,0.295225,-5.714954,-0.526721,8.335668,-6.567673,-9.227644,6.015883,-7.765526,7.956335,7.009984,0.371505,3.911999,-2.381037,-8.163938,-1.817881,-1.319531,-8.968901,0.947899,4.706152,4.106148,-4.573730,9.993048,7.477830,-5.524924,2.668085,2.346905,-4.651373,-2.761854,5.481215,-9.025201,-0.778152], dtype = "float64")#candidate|4832|(168,)|const|float64
const_4833 = relay.const([[5,9,8,-10,9,-4,8,6,1,5],[-7,-10,-9,5,-8,-2,-1,-8,5,8],[6,1,-5,-9,-5,6,1,10,-4,9],[-2,-6,-6,-3,-4,4,-4,4,-2,-6],[7,8,6,10,-4,6,4,10,6,-10]], dtype = "uint64")#candidate|4833|(5, 10)|const|uint64
call_4830 = relay.TupleGetItem(func_2615_call(relay.reshape(var_4831.astype('float32'), [10, 16, 1]), relay.reshape(const_4832.astype('float64'), [6, 28]), relay.reshape(const_4833.astype('uint64'), [50,]), ), 3)
call_4834 = relay.TupleGetItem(func_2619_call(relay.reshape(var_4831.astype('float32'), [10, 16, 1]), relay.reshape(const_4832.astype('float64'), [6, 28]), relay.reshape(const_4833.astype('uint64'), [50,]), ), 3)
output = relay.Tuple([bop_4822,call_4830,var_4831,const_4832,const_4833,])
output2 = relay.Tuple([bop_4825,call_4834,var_4831,const_4832,const_4833,])
func_4846 = relay.Function([var_4831,], output)
mod['func_4846'] = func_4846
mod = relay.transform.InferType()(mod)
var_4847 = relay.var("var_4847", dtype = "float32", shape = (4, 40))#candidate|4847|(4, 40)|var|float32
output = func_4846(var_4847)
func_4848 = relay.Function([var_4847], output)
mutated_mod['func_4848'] = func_4848
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4416_call = mod.get_global_var('func_4416')
func_4417_call = mutated_mod.get_global_var('func_4417')
call_4918 = relay.TupleGetItem(func_4416_call(), 0)
call_4919 = relay.TupleGetItem(func_4417_call(), 0)
output = call_4918
output2 = call_4919
func_4933 = relay.Function([], output)
mod['func_4933'] = func_4933
mod = relay.transform.InferType()(mod)
mutated_mod['func_4933'] = func_4933
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4933_call = mutated_mod.get_global_var('func_4933')
call_4934 = func_4933_call()
output = call_4934
func_4935 = relay.Function([], output)
mutated_mod['func_4935'] = func_4935
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4998 = relay.const([[[-6.465283,-1.223797]],[[-8.993397,5.371814]],[[2.078177,-4.214507]],[[-3.208697,-9.064031]]], dtype = "float32")#candidate|4998|(4, 1, 2)|const|float32
var_4999 = relay.var("var_4999", dtype = "float32", shape = (4, 5, 2))#candidate|4999|(4, 5, 2)|var|float32
bop_5000 = relay.floor_divide(const_4998.astype('float32'), var_4999.astype('float32')) # shape=(4, 5, 2)
output = bop_5000
output2 = bop_5000
func_5025 = relay.Function([var_4999,], output)
mod['func_5025'] = func_5025
mod = relay.transform.InferType()(mod)
var_5026 = relay.var("var_5026", dtype = "float32", shape = (4, 5, 2))#candidate|5026|(4, 5, 2)|var|float32
output = func_5025(var_5026)
func_5027 = relay.Function([var_5026], output)
mutated_mod['func_5027'] = func_5027
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5109 = relay.const([[[-4,-8,-4,-6,-9],[-3,-2,-8,-3,-4],[-10,10,7,-10,4],[2,-2,2,-7,8],[-3,4,8,-10,9],[-1,4,-10,3,-9],[-9,-5,-1,6,7],[-8,5,-8,4,-5],[-5,-3,-10,-9,10]],[[2,-8,10,-5,-1],[-2,-3,-1,-1,-10],[-7,3,-3,4,7],[-9,-5,3,-6,4],[1,4,-3,4,9],[10,-10,-7,-7,-4],[-5,1,-9,5,-5],[1,-5,9,-2,-1],[10,9,4,4,9]],[[4,-10,-3,-1,4],[-9,1,4,3,-6],[6,-4,7,-3,9],[-8,5,8,-9,-10],[5,10,5,-10,9],[-1,-2,-4,-2,10],[8,-4,10,-2,-3],[5,-4,-5,-8,-7],[1,-4,2,-3,-4]],[[8,5,-6,6,-5],[2,8,-5,-5,8],[-2,10,3,5,-10],[9,2,10,8,-7],[6,2,-5,6,2],[4,2,-1,7,1],[4,5,-5,-3,2],[7,-9,-1,8,8],[1,3,7,-10,-7]],[[-2,-2,-6,-2,9],[8,2,-5,-6,10],[2,-8,-7,-6,-7],[-10,5,-8,9,9],[-5,-4,-8,2,3],[-10,5,1,-2,1],[-1,10,2,-6,-9],[-9,-5,3,-3,1],[-7,2,-10,-2,-1]],[[2,3,-7,-2,-6],[-1,5,-7,1,-3],[5,-3,10,9,6],[6,-1,3,-5,-4],[-6,-5,10,1,-9],[4,-4,10,-2,5],[-10,-7,-1,-10,3],[-5,-6,-4,-2,10],[1,5,2,-9,-8]],[[-2,7,-7,10,-3],[1,6,10,-6,6],[4,-3,-3,6,-1],[6,1,5,-2,-7],[-7,-2,-8,2,-5],[-1,6,-7,8,2],[-8,-3,2,10,2],[-8,8,10,4,-9],[10,7,-5,-6,-8]],[[2,-7,-4,4,2],[3,-3,-1,6,-6],[-2,6,-4,-4,4],[9,7,-3,-6,6],[3,7,8,-10,3],[9,4,-7,-6,1],[2,-8,-7,-9,-7],[2,-2,-7,-8,7],[3,-9,3,7,6]],[[1,-1,4,-9,-2],[7,8,2,-2,-2],[-2,-4,4,-6,7],[1,7,-7,10,5],[4,-4,1,-8,6],[9,5,-8,1,9],[3,5,10,4,-8],[1,-9,4,3,-3],[4,-9,-5,9,1]],[[5,-8,8,2,9],[9,2,7,9,10],[10,-6,-4,-8,-9],[10,4,2,-9,2],[-4,10,-2,-2,10],[5,-7,-1,-1,5],[-7,-4,7,3,-10],[-4,7,-10,4,1],[5,5,8,6,-4]],[[-1,-8,-4,-1,-8],[1,5,9,-8,-9],[-8,9,-8,-9,10],[5,-6,6,-5,6],[-10,-7,-4,2,1],[5,6,3,10,-8],[7,2,6,3,9],[-9,6,-3,4,4],[-7,-5,2,-6,-9]],[[-5,-10,8,-8,-9],[2,-5,-6,9,-6],[-5,4,5,-5,-10],[-5,-1,-3,1,1],[8,2,10,-2,7],[-5,-10,-10,7,-5],[-2,-4,-5,1,8],[-10,5,-10,7,7],[-9,-6,-1,3,4]],[[7,-6,8,-9,9],[-2,6,10,-2,7],[3,-2,-4,-5,-3],[4,-6,4,-4,-4],[-4,4,2,7,1],[5,-1,-10,2,-3],[6,-6,10,6,-4],[-8,5,-8,6,-2],[1,-10,4,7,-9]],[[10,10,6,5,5],[-10,-8,5,-3,3],[-9,-3,-7,2,3],[-6,5,-9,5,4],[-5,-3,1,-3,10],[-10,-2,-1,-1,5],[-2,-9,7,1,3],[-2,-10,-3,4,5],[-4,4,-9,-7,7]]], dtype = "uint16")#candidate|5109|(14, 9, 5)|const|uint16
var_5110 = relay.var("var_5110", dtype = "uint16", shape = (14, 9, 5))#candidate|5110|(14, 9, 5)|var|uint16
bop_5111 = relay.logical_xor(const_5109.astype('uint16'), relay.reshape(var_5110.astype('uint16'), relay.shape_of(const_5109))) # shape=(14, 9, 5)
output = relay.Tuple([bop_5111,])
output2 = relay.Tuple([bop_5111,])
func_5125 = relay.Function([var_5110,], output)
mod['func_5125'] = func_5125
mod = relay.transform.InferType()(mod)
mutated_mod['func_5125'] = func_5125
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5126 = relay.var("var_5126", dtype = "uint16", shape = (14, 9, 5))#candidate|5126|(14, 9, 5)|var|uint16
func_5125_call = mutated_mod.get_global_var('func_5125')
call_5127 = func_5125_call(var_5126)
output = call_5127
func_5128 = relay.Function([var_5126], output)
mutated_mod['func_5128'] = func_5128
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5130 = relay.const([[[-9,3,1,7,-4,4,5,2,-9,-8,2,-7,-10,10,-7],[9,-8,-8,-10,7,-9,3,4,1,-10,2,5,-9,-4,-6],[5,-9,-10,4,-3,3,-1,-5,2,8,-6,-3,10,7,2],[6,-3,-10,3,2,-4,-5,1,-10,5,4,8,4,1,3]],[[9,9,-6,2,5,-3,-8,6,10,2,-5,9,-4,-5,-6],[-6,-10,4,8,-3,-9,3,-5,-7,-6,10,-5,-7,2,4],[2,1,-9,-6,-1,9,3,9,9,-3,-5,8,-2,1,-9],[-1,6,-1,-7,1,3,-9,-10,-6,-6,-5,2,5,10,-7]],[[10,8,-10,-3,7,6,-6,8,-5,6,-1,-6,-4,-6,-4],[3,-3,-2,-1,1,-10,8,3,-1,-8,2,8,4,-9,-6],[7,9,-10,2,-7,-9,-7,-5,1,-1,-5,-2,-10,-4,-9],[2,-2,6,1,3,-9,8,-9,8,-1,1,-1,8,9,10]],[[4,6,4,-8,-9,6,-3,-6,7,4,-3,1,-8,-5,1],[-9,-9,1,-8,-10,-9,-7,-1,7,-6,-4,-6,3,6,-2],[-3,-3,7,-8,2,2,-6,-6,-3,-3,-3,-10,-5,-4,-8],[9,-7,-6,6,-9,-3,10,1,4,-8,-5,-7,-2,5,-5]],[[-2,8,9,-6,-9,-5,-8,-2,10,3,7,1,-2,-8,8],[-1,2,-2,5,-7,-2,7,-7,9,6,-7,9,-7,-10,-7],[10,1,-1,-2,2,1,4,-6,-8,10,6,-7,7,7,8],[-8,-3,-10,-5,-1,4,2,1,-10,-2,2,-10,-4,-10,-4]],[[4,9,-4,-4,-3,-5,8,-6,-5,7,-9,-5,6,5,8],[-8,-5,2,8,-6,2,10,1,8,-4,-3,-3,-3,-6,9],[-10,-6,2,2,-3,-10,2,-4,10,8,8,9,8,2,-10],[9,8,3,-5,-1,-5,-5,3,-1,1,8,-3,-3,-9,-6]],[[-6,9,10,5,8,4,-6,-2,8,3,5,9,6,-10,6],[6,-8,-7,6,4,7,9,6,-4,7,4,-7,-1,-6,2],[6,6,-10,4,5,1,-5,5,4,-6,7,6,-2,10,7],[-9,-7,-6,-10,-4,8,8,8,5,-3,4,8,5,-6,-7]],[[5,7,-1,-1,-5,7,-10,7,8,-9,-2,2,-2,9,2],[-2,-3,10,-4,-6,-6,2,-8,2,-10,7,-4,1,8,4],[7,-8,7,-4,-1,-1,3,-2,2,-7,5,-2,4,2,3],[-3,-6,-1,-1,5,5,-8,1,9,4,-4,1,5,-1,-9]]], dtype = "int16")#candidate|5130|(8, 4, 15)|const|int16
var_5131 = relay.var("var_5131", dtype = "int16", shape = (8, 4, 15))#candidate|5131|(8, 4, 15)|var|int16
bop_5132 = relay.logical_xor(const_5130.astype('int16'), relay.reshape(var_5131.astype('int16'), relay.shape_of(const_5130))) # shape=(8, 4, 15)
func_2010_call = mod.get_global_var('func_2010')
func_2013_call = mutated_mod.get_global_var('func_2013')
const_5137 = relay.const(1.823720, dtype = "float32")#candidate|5137|()|const|float32
const_5138 = relay.const([-5.658331,-9.093305,0.365530,-6.303351,-2.502322,-2.262240,3.318425,7.261451,8.577844,2.354427,4.276676,7.192079,3.363679,-6.036379,-4.630492,-5.175334], dtype = "float32")#candidate|5138|(16,)|const|float32
call_5136 = relay.TupleGetItem(func_2010_call(relay.reshape(const_5137.astype('float32'), []), relay.reshape(const_5138.astype('float32'), [4, 4]), ), 0)
call_5139 = relay.TupleGetItem(func_2013_call(relay.reshape(const_5137.astype('float32'), []), relay.reshape(const_5138.astype('float32'), [4, 4]), ), 0)
output = relay.Tuple([bop_5132,call_5136,const_5137,const_5138,])
output2 = relay.Tuple([bop_5132,call_5139,const_5137,const_5138,])
func_5141 = relay.Function([var_5131,], output)
mod['func_5141'] = func_5141
mod = relay.transform.InferType()(mod)
mutated_mod['func_5141'] = func_5141
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5142 = relay.var("var_5142", dtype = "int16", shape = (8, 4, 15))#candidate|5142|(8, 4, 15)|var|int16
func_5141_call = mutated_mod.get_global_var('func_5141')
call_5143 = func_5141_call(var_5142)
output = call_5143
func_5144 = relay.Function([var_5142], output)
mutated_mod['func_5144'] = func_5144
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4693_call = mod.get_global_var('func_4693')
func_4694_call = mutated_mod.get_global_var('func_4694')
call_5146 = func_4693_call()
call_5147 = func_4693_call()
output = relay.Tuple([call_5146,])
output2 = relay.Tuple([call_5147,])
func_5157 = relay.Function([], output)
mod['func_5157'] = func_5157
mod = relay.transform.InferType()(mod)
output = func_5157()
func_5158 = relay.Function([], output)
mutated_mod['func_5158'] = func_5158
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4734_call = mod.get_global_var('func_4734')
func_4736_call = mutated_mod.get_global_var('func_4736')
call_5235 = relay.TupleGetItem(func_4734_call(), 0)
call_5236 = relay.TupleGetItem(func_4736_call(), 0)
output = call_5235
output2 = call_5236
func_5253 = relay.Function([], output)
mod['func_5253'] = func_5253
mod = relay.transform.InferType()(mod)
output = func_5253()
func_5254 = relay.Function([], output)
mutated_mod['func_5254'] = func_5254
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5253_call = mod.get_global_var('func_5253')
func_5254_call = mutated_mod.get_global_var('func_5254')
call_5282 = func_5253_call()
call_5283 = func_5253_call()
output = call_5282
output2 = call_5283
func_5290 = relay.Function([], output)
mod['func_5290'] = func_5290
mod = relay.transform.InferType()(mod)
mutated_mod['func_5290'] = func_5290
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5290_call = mutated_mod.get_global_var('func_5290')
call_5291 = func_5290_call()
output = call_5291
func_5292 = relay.Function([], output)
mutated_mod['func_5292'] = func_5292
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5330 = relay.var("var_5330", dtype = "bool", shape = (15, 13, 1))#candidate|5330|(15, 13, 1)|var|bool
var_5331 = relay.var("var_5331", dtype = "bool", shape = (15, 13, 5))#candidate|5331|(15, 13, 5)|var|bool
bop_5332 = relay.logical_and(var_5330.astype('bool'), var_5331.astype('bool')) # shape=(15, 13, 5)
output = bop_5332
output2 = bop_5332
func_5345 = relay.Function([var_5330,var_5331,], output)
mod['func_5345'] = func_5345
mod = relay.transform.InferType()(mod)
mutated_mod['func_5345'] = func_5345
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5345_call = mutated_mod.get_global_var('func_5345')
var_5347 = relay.var("var_5347", dtype = "bool", shape = (15, 13, 1))#candidate|5347|(15, 13, 1)|var|bool
var_5348 = relay.var("var_5348", dtype = "bool", shape = (15, 13, 5))#candidate|5348|(15, 13, 5)|var|bool
call_5346 = func_5345_call(var_5347,var_5348,)
output = call_5346
func_5349 = relay.Function([var_5347,var_5348,], output)
mutated_mod['func_5349'] = func_5349
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4416_call = mod.get_global_var('func_4416')
func_4417_call = mutated_mod.get_global_var('func_4417')
call_5370 = relay.TupleGetItem(func_4416_call(), 0)
call_5371 = relay.TupleGetItem(func_4417_call(), 0)
func_4799_call = mod.get_global_var('func_4799')
func_4802_call = mutated_mod.get_global_var('func_4802')
call_5385 = func_4799_call(relay.reshape(call_5370.astype('uint32'), [5, 10, 13]))
call_5386 = func_4799_call(relay.reshape(call_5370.astype('uint32'), [5, 10, 13]))
output = relay.Tuple([call_5370,call_5385,])
output2 = relay.Tuple([call_5371,call_5386,])
func_5396 = relay.Function([], output)
mod['func_5396'] = func_5396
mod = relay.transform.InferType()(mod)
mutated_mod['func_5396'] = func_5396
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5396_call = mutated_mod.get_global_var('func_5396')
call_5397 = func_5396_call()
output = call_5397
func_5398 = relay.Function([], output)
mutated_mod['func_5398'] = func_5398
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5157_call = mod.get_global_var('func_5157')
func_5158_call = mutated_mod.get_global_var('func_5158')
call_5430 = relay.TupleGetItem(func_5157_call(), 0)
call_5431 = relay.TupleGetItem(func_5158_call(), 0)
output = call_5430
output2 = call_5431
func_5448 = relay.Function([], output)
mod['func_5448'] = func_5448
mod = relay.transform.InferType()(mod)
mutated_mod['func_5448'] = func_5448
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5448_call = mutated_mod.get_global_var('func_5448')
call_5449 = func_5448_call()
output = call_5449
func_5450 = relay.Function([], output)
mutated_mod['func_5450'] = func_5450
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5480 = relay.const([[[-8,-3,-7,8,4,3,-8,-8]],[[-1,1,8,-5,5,-7,-4,9]]], dtype = "int8")#candidate|5480|(2, 1, 8)|const|int8
var_5481 = relay.var("var_5481", dtype = "int8", shape = (2, 1, 8))#candidate|5481|(2, 1, 8)|var|int8
bop_5482 = relay.less_equal(const_5480.astype('bool'), relay.reshape(var_5481.astype('bool'), relay.shape_of(const_5480))) # shape=(2, 1, 8)
uop_5490 = relay.asinh(const_5480.astype('float64')) # shape=(2, 1, 8)
bop_5492 = relay.multiply(uop_5490.astype('uint16'), relay.reshape(bop_5482.astype('uint16'), relay.shape_of(uop_5490))) # shape=(2, 1, 8)
output = relay.Tuple([bop_5492,])
output2 = relay.Tuple([bop_5492,])
func_5498 = relay.Function([var_5481,], output)
mod['func_5498'] = func_5498
mod = relay.transform.InferType()(mod)
var_5499 = relay.var("var_5499", dtype = "int8", shape = (2, 1, 8))#candidate|5499|(2, 1, 8)|var|int8
output = func_5498(var_5499)
func_5500 = relay.Function([var_5499], output)
mutated_mod['func_5500'] = func_5500
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4416_call = mod.get_global_var('func_4416')
func_4417_call = mutated_mod.get_global_var('func_4417')
call_5621 = relay.TupleGetItem(func_4416_call(), 0)
call_5622 = relay.TupleGetItem(func_4417_call(), 0)
output = call_5621
output2 = call_5622
func_5645 = relay.Function([], output)
mod['func_5645'] = func_5645
mod = relay.transform.InferType()(mod)
output = func_5645()
func_5646 = relay.Function([], output)
mutated_mod['func_5646'] = func_5646
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5692 = relay.var("var_5692", dtype = "float32", shape = (15, 3, 11))#candidate|5692|(15, 3, 11)|var|float32
uop_5693 = relay.erf(var_5692.astype('float32')) # shape=(15, 3, 11)
func_217_call = mod.get_global_var('func_217')
func_220_call = mutated_mod.get_global_var('func_220')
const_5696 = relay.const([10,2,10,5,1,-4,-2,9,-1,-4,-9,7,1,7,3,-1,-3,-2,-2,8,-10,8,-5,4,9,10,-4,1,8,-7,1,6,3,-6,-7,-10,1,1,-6,-1,-2,2,-8,3,10,-9,-10,-4,-2,-9,9,8,-7,3,5,-10,-4,4,5,8,-7,-8,-1,-9,-5,6,8,-1,4,-2,-1,-3,-5,7,-4,9,3,8,10,-8,8,8,-7,-2,-4,-9,7,9,1,-5,-4,-6,-10,10,-4,4,4,5,-2,4,1,10,-7,1,-9,-3,-1,-8,3,-10], dtype = "int8")#candidate|5696|(110,)|const|int8
call_5695 = relay.TupleGetItem(func_217_call(relay.reshape(const_5696.astype('int8'), [110,])), 0)
call_5697 = relay.TupleGetItem(func_220_call(relay.reshape(const_5696.astype('int8'), [110,])), 0)
bop_5699 = relay.bitwise_and(uop_5693.astype('uint32'), relay.reshape(var_5692.astype('uint32'), relay.shape_of(uop_5693))) # shape=(15, 3, 11)
func_5125_call = mod.get_global_var('func_5125')
func_5128_call = mutated_mod.get_global_var('func_5128')
var_5706 = relay.var("var_5706", dtype = "uint16", shape = (630,))#candidate|5706|(630,)|var|uint16
call_5705 = relay.TupleGetItem(func_5125_call(relay.reshape(var_5706.astype('uint16'), [14, 9, 5])), 0)
call_5707 = relay.TupleGetItem(func_5128_call(relay.reshape(var_5706.astype('uint16'), [14, 9, 5])), 0)
func_648_call = mod.get_global_var('func_648')
func_653_call = mutated_mod.get_global_var('func_653')
const_5729 = relay.const([[6,-8,-5,7,5,-9,1,5,-6,7,-10,-7,-9,10,6,8,7,5,4,4,-7,-6,-8,8,-5,7,1,4,8,6,5,8,-4,4,2,7,-2,10,6,-3,10,-8,1,-9,-5,6,2,4,4,-2,-9,-8,4,2,-3,-10,-6,-5,10,7,-10,-9,-7,-8,2,-9,-1,-3,-6,-2,1,-3,-10,-5,4,-8,-7,9,-10,4,9,7,2,-4,7,7,-9,7,1,-2,4,-9,8,4,5,4,-3,3,-10,-6,-4,-7,5,2,5,-1,7,1,-8,-3,-7,6,-7,7,-7,-4,-6,-1,4,7,9,-2,7,-2,-10,-7,-2,-9,3,6,-9,-8,1,5,5,7,-9,-10,4,-3,-7,-3,5,-9,8,-8,-6,-1,6,-2,-10,-4,-10,7,-6,-10,1,3,-5,-4,-8,9,9,-8,-6,5,-3,-4,5,9,-2,-4,4,10,-2,4,7,3,-3,-2,-3,-4,-7,-1,2,4,1,-10,7,-4,-4,-8,-2,-8,2,-6,6,3,-2,6,4,-9,-7,-2,9,-5,6,4,4,5,-2,1,10,-3,-8,-6,8,7,-6,-2,-5,-8,10,-9,5,-8,-4,7,5,-8,-9,-5,-2,4,3,3,-1,-1,4,-5,3,-6,-4,-2,-2,-2,-5,-8,9,-6,-8,-10,-1,-1,-2,-4,10,3,2,3,-6,-5,-1,-9,-6,3,-8,-4,6,6,2,5,1,-5,3,-6,-4,1,7,6,-9,-7,5,-7,-5,-1,2,-8,-3,-5,3,-9,-4,2,2,-5,10,9,-3,6,-7,4,10,2,7,2,-9,-8,-1,4,-2,-6,1,6,2,-2,7,-8,-2,-4,6,-10,7,9,10,-3,4,-3,-7,-1,-10,-7,2,8,6,2,8,-8,-10,4,2,-10,-1,3,1,6,-8,-2,10,4,-2,7]], dtype = "int64")#candidate|5729|(1, 352)|const|int64
var_5730 = relay.var("var_5730", dtype = "int32", shape = (3,))#candidate|5730|(3,)|var|int32
var_5731 = relay.var("var_5731", dtype = "int32", shape = (168,))#candidate|5731|(168,)|var|int32
call_5728 = relay.TupleGetItem(func_648_call(relay.reshape(const_5729.astype('int64'), [8, 4, 11]), relay.reshape(var_5730.astype('int32'), [3,]), relay.reshape(var_5731.astype('int32'), [168,]), ), 1)
call_5732 = relay.TupleGetItem(func_653_call(relay.reshape(const_5729.astype('int64'), [8, 4, 11]), relay.reshape(var_5730.astype('int32'), [3,]), relay.reshape(var_5731.astype('int32'), [168,]), ), 1)
func_4933_call = mod.get_global_var('func_4933')
func_4935_call = mutated_mod.get_global_var('func_4935')
call_5737 = func_4933_call()
call_5738 = func_4933_call()
func_4567_call = mod.get_global_var('func_4567')
func_4569_call = mutated_mod.get_global_var('func_4569')
var_5740 = relay.var("var_5740", dtype = "uint8", shape = (1, 15))#candidate|5740|(1, 15)|var|uint8
call_5739 = relay.TupleGetItem(func_4567_call(relay.reshape(var_5740.astype('uint8'), [15,])), 4)
call_5741 = relay.TupleGetItem(func_4569_call(relay.reshape(var_5740.astype('uint8'), [15,])), 4)
uop_5744 = relay.acos(uop_5693.astype('float64')) # shape=(15, 3, 11)
bop_5747 = relay.power(bop_5699.astype('float32'), relay.reshape(uop_5744.astype('float32'), relay.shape_of(bop_5699))) # shape=(15, 3, 11)
func_1263_call = mod.get_global_var('func_1263')
func_1266_call = mutated_mod.get_global_var('func_1266')
const_5751 = relay.const([7.612411,5.134674,-9.590984,8.813089,-9.642367,-3.417171,-5.413174,-4.553016,-9.959618,-5.845152,8.345730,-4.870350,2.229969,1.242588,-9.351549,0.329141,-8.338640,9.560738,5.893610,0.767475,-8.414220,-9.277690,-9.283303,-4.528210,3.086448,9.226235,7.041689,1.135215,-0.666944,-4.867256,3.281953,-6.380032,-4.266961,-1.456265,-0.748498,-7.506038,5.480118,4.512855,0.306911,-3.748952,-9.525537,-2.564953,-8.098351,7.545141,-2.831164,6.871282,1.352101,1.384625,6.447010,6.794160,2.040870,0.744823,-4.495780,-0.813052,-1.141419,-3.019011,-2.078417,4.851113,-8.964337,9.925785,-7.445108,-8.018704,-5.720280,9.453994,3.600043,8.081380,-6.223375,0.496708,-7.759221,6.323919,9.760137,4.590486,-9.372158,-2.978866,2.456776,8.497038,-3.645426,6.519455,6.689117,3.762807,0.027066,4.878624,1.441219,4.690539,-7.244169,-6.111328,-4.607660,5.430846,-8.963430,-4.920190,4.303183,1.476325,7.108663,-3.200574,-9.423570,-4.326784,-3.215608,6.965558,-3.208478,6.979232,3.482673,-5.537614,-6.427912,-2.793970,6.533604,-6.033677,-0.624639,9.328795,1.179750,-5.921252,1.799704,5.031859,-1.760083,2.597626,7.791537,6.915875,-7.136805,9.465969,9.740794,-9.637011,-0.534945,1.819250,-9.082288,-1.432788,-2.293223,2.347647,4.153131,-2.556910,-6.093730,9.238332,-5.071436,-8.636420,-0.924868,3.309992,-6.154449,8.229264,4.050041,7.873256,3.871038,1.498950,5.408848,7.185836,9.497138,-9.558972,5.745404,-0.954992,9.003172,-3.054602,-7.574346,5.806894,3.643600,3.365533,-2.168437,0.214634,-1.441268,7.409546,9.321117,4.421502,-3.245126,-7.826971,1.585638,-0.520624,-0.534762,-5.856051,-2.811759,0.285921,-2.192028,-3.430195,8.282888,-9.343582,-0.216780,5.788592,-3.617072,9.218416,3.766473,-8.671423,-3.988734,5.911899,-0.096257,2.741867,7.352186,-7.939363,2.485424,-6.690703,-3.615201,-2.412286,7.117505,6.639184,-0.776497,-2.097616,-5.659914,-0.934009,7.558332,2.542438,-4.158934,3.078328,5.196993,9.465582,-4.910831,-6.378684,5.151652,-1.097910,-0.483251,-3.156810,-8.373450,-4.887620,-1.299688,5.483343,-3.814133,4.590992,6.188747,3.374954,-4.437680,3.624159,-3.651702,-6.540270,-5.391738,-6.523964,-0.206019,-1.115839,-3.016995,5.756784,3.309981,-4.429185,-9.322533,-0.339504,-7.160123,-1.822302,5.140339,-4.176218,2.817915,6.926269,2.415674,3.904591,-6.464257,-5.847017,-3.130817,1.971986,-0.827352,-0.252826,9.134463,-3.320331,-6.016599,1.543370,-9.311685,3.012763,-5.943818,4.694826,7.765811,8.300726,-8.421413,-7.099039,9.157167,7.043394,7.652720,-5.841643,-4.942763,7.133683,-0.402773,-8.618660,-8.604349,-8.380758,-6.627512,-2.665401,-0.554194,-0.539379,0.995921,-5.061511,-6.665566,-2.629703,2.608273,9.659200,8.853604,-7.459862,1.968531,-7.550640,-1.683853,-0.249150,-0.901832,-0.026821,-2.213565,-9.115226,0.347545,-5.055597,-2.623218,-6.528386,-1.319908,8.518597,-0.626841,5.541008,5.472777,7.815611,-7.633808,-4.569423,-9.448510,-3.961876,2.206862,-9.490324,8.718237,3.950888,6.241668,7.112801,2.932080,6.518360,-8.036796,8.197847,-7.436531,4.029968,-7.568688,6.431898,0.881736,2.200701,-1.378343,8.522552,-9.212580,5.839488,-3.652679,0.863274,-4.192184,1.730759,3.470270,-1.107787,8.424139,4.316456,8.442414,-4.933061,-6.987898,-3.897247,3.084036,-4.512060,-3.003401,1.155413,-0.975479,-0.302924,2.713490,7.209321,-5.260477,-2.056649,2.251071,6.211449,3.842490,7.419547,3.869447,-9.124627,-6.119374,-1.554977,4.269580,3.589239,6.125428,-3.245986,-0.984505,9.283917,0.076256,-2.756529,2.785696,2.743108,-3.372576,-4.704293,-1.346595,-2.794607,6.717798,7.227931,7.548748,-2.078680,-8.983600,9.565875,-5.994047,9.209086,3.338817,1.452387,5.457506,0.882674,1.596486,0.275757,-8.193216,-3.472632,3.661297,-3.984730,6.334408,7.269297,4.719710,-5.708024,2.649232,5.124337,4.896113,-5.831466,-4.379704,-0.672838,1.072583,8.649789,-9.889001,-9.138940,-5.317316,-0.712620,7.901263,8.930913,-8.296016,3.805666,-1.234242,-9.547598,8.497890,-1.895951,-6.776791,9.101630,1.571671,-6.705940,8.726210,1.967034,0.393124,4.915076,5.557639,-8.857471,-0.344458,8.680202,-1.526303,-3.379749,-6.135919,2.988166,-1.477193,8.911959,-0.171579,7.276071,-3.513437,9.197192,-0.669076,-0.390357,0.597574,3.669593,-1.032200,-3.663413,4.417562,-6.872524,-8.956367,-3.945694,1.886682,-4.954455,1.960221,1.536142,-0.726463,-5.847050,1.387647,-3.477416,3.727723,-6.226586,-9.120133,-1.054697,8.236776,-5.106351,0.876961,-5.269632,-5.458789,-5.219587,-2.504909,9.163654,-0.081919,2.391470,-2.646715,-3.487268,-2.146002,-9.477411,-9.296133,-0.540397,3.051505,5.769846,2.156526,3.834180,-3.691265,-2.194379,8.798915,9.842872,6.219518,4.971641,-6.610733,5.015633,-3.305089,8.535951,-4.785451,6.194464,-4.256066,-8.171698,-5.892407,5.490986,3.905179,-2.049902,4.946734,-0.819454,-5.223705,6.599527,-8.282450,2.261962,-5.760108,9.534872,-0.569894,-6.336400,3.278090,9.030499,0.924019,-8.120753,-5.955624,7.905539,-5.926356,-3.545941,-1.793349,0.683722,-5.624127,7.175220,2.915132,7.093446,9.972697,0.421476,5.297582,6.020768,7.693012,6.262103,-7.890143,-1.408164,9.639977,4.339016,-6.071221,-3.704328,-3.116452,9.461944,-2.957702,0.918051,-9.057259,-9.380440,5.976566,-0.706696,3.726057,-9.853300,8.525858,-6.436921,7.223439,-4.639894,-2.537588,-0.615134,-1.493098,-1.294193,2.697755,5.721604,-8.990925,3.042436,7.520597,3.235793,6.514660,-0.913004,-0.318412,5.362820,-9.404309,7.955475,-0.079710,4.496652,4.389110,9.045342,-9.945572,-5.075435,-3.863766,-1.437634,-4.614573,-5.138322,-7.856028,-1.038285,1.388308,-7.586539,1.992438,-3.389638,-2.322139,-8.214296,-4.582382,-2.810402,-4.533013,4.503266,-0.625245,-4.117684,9.255605,-1.999275,3.191139,-4.872606,9.853979,2.449542,-5.093295,-3.852154,9.938769,-5.531159,5.253150,-9.694950,-1.618131,-8.730693,-3.309690,5.386685,-8.267813,3.500661,-8.233631,-1.758476,-8.972126,-6.386907,-4.587192,5.784135,1.515592,6.271620,-0.696647,6.092374,3.740748,2.101875,-1.677201,-2.588248,3.029241,9.324264,8.208502,0.364762,2.022357,3.711773,-5.256766,8.254632,-8.309089,-7.598627,0.108011,6.615862,-6.180594,-4.839650,5.089755,7.894075,-9.945642,-4.262119,-9.545384,2.694116,1.676957,0.524332,-2.443305,-0.676608,5.398298,6.088403,-2.258701,-9.159306,-9.601837,8.917850,8.636306,-0.892404,4.193789,7.769835,-5.710443,3.227433,0.529355,2.345498,-4.422394,0.527612,7.332904,-3.344054,6.319047,-1.803188,3.237806,-8.888584,-7.303889,-2.148551,2.266786,6.216460,-7.487748,-0.880530,-9.993964,5.952140,7.933255,-2.991660,-6.612818,-5.954866,5.196891,6.438864,-7.438312,1.961691,-7.112562,0.598526,-8.681103,8.415718,6.056238,-1.372733,3.787929,-5.143795,-0.650300,7.252776,0.983450,9.751683,-2.342361,0.536454,-0.005467,0.916667,-6.303352,-3.410206,-4.444918,-0.472947,2.860816,3.952802,-3.824243,4.961890,-0.880254,4.460625,-5.444608,6.116111,9.189402,-7.127620,8.889017,-7.526557,-5.546200,-0.227211,-0.420670,-3.933315,-1.077834,3.285943,-4.991512,1.117769,5.163994,-3.159747,2.599292,4.874498,9.861099,-8.336830,4.261549,-3.715253,-8.508089,-8.429291,0.756719,-4.753320,-1.787601,4.893062,5.868521,-5.347764,1.209939,-7.057023,-2.213016,-9.961345,1.826416,-0.733539,8.433058,-8.728667,-1.025365,7.402737,-3.093570,9.546797,2.170198,7.199938,2.840362,7.414087,-7.952924,-2.408835,1.189571,-1.496628,5.909644,-2.963001,-5.046999,-7.005071,7.551477,-4.506700,-2.889065,6.621350,-4.361145,-5.282317,-3.732693,0.776269,4.152638,1.934440,-5.674751,-6.991333,-8.277592,-2.717461,0.202734,8.001705,-7.755022,-8.567360,1.808570,-6.921368], dtype = "float32")#candidate|5751|(768,)|const|float32
call_5750 = relay.TupleGetItem(func_1263_call(relay.reshape(const_5751.astype('float32'), [16, 6, 8])), 0)
call_5752 = relay.TupleGetItem(func_1266_call(relay.reshape(const_5751.astype('float32'), [16, 6, 8])), 0)
output = relay.Tuple([call_5695,const_5696,call_5705,var_5706,call_5728,const_5729,var_5730,var_5731,call_5737,call_5739,var_5740,bop_5747,call_5750,const_5751,])
output2 = relay.Tuple([call_5697,const_5696,call_5707,var_5706,call_5732,const_5729,var_5730,var_5731,call_5738,call_5741,var_5740,bop_5747,call_5752,const_5751,])
func_5755 = relay.Function([var_5692,var_5706,var_5730,var_5731,var_5740,], output)
mod['func_5755'] = func_5755
mod = relay.transform.InferType()(mod)
mutated_mod['func_5755'] = func_5755
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5755_call = mutated_mod.get_global_var('func_5755')
var_5757 = relay.var("var_5757", dtype = "float32", shape = (15, 3, 11))#candidate|5757|(15, 3, 11)|var|float32
var_5758 = relay.var("var_5758", dtype = "uint16", shape = (630,))#candidate|5758|(630,)|var|uint16
var_5759 = relay.var("var_5759", dtype = "int32", shape = (3,))#candidate|5759|(3,)|var|int32
var_5760 = relay.var("var_5760", dtype = "int32", shape = (168,))#candidate|5760|(168,)|var|int32
var_5761 = relay.var("var_5761", dtype = "uint8", shape = (1, 15))#candidate|5761|(1, 15)|var|uint8
call_5756 = func_5755_call(var_5757,var_5758,var_5759,var_5760,var_5761,)
output = call_5756
func_5762 = relay.Function([var_5757,var_5758,var_5759,var_5760,var_5761,], output)
mutated_mod['func_5762'] = func_5762
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5645_call = mod.get_global_var('func_5645')
func_5646_call = mutated_mod.get_global_var('func_5646')
call_5791 = func_5645_call()
call_5792 = func_5645_call()
output = relay.Tuple([call_5791,])
output2 = relay.Tuple([call_5792,])
func_5797 = relay.Function([], output)
mod['func_5797'] = func_5797
mod = relay.transform.InferType()(mod)
mutated_mod['func_5797'] = func_5797
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5797_call = mutated_mod.get_global_var('func_5797')
call_5798 = func_5797_call()
output = call_5798
func_5799 = relay.Function([], output)
mutated_mod['func_5799'] = func_5799
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5800 = relay.var("var_5800", dtype = "int8", shape = ())#candidate|5800|()|var|int8
var_5801 = relay.var("var_5801", dtype = "int8", shape = (3, 10, 4))#candidate|5801|(3, 10, 4)|var|int8
bop_5802 = relay.not_equal(var_5800.astype('bool'), var_5801.astype('bool')) # shape=(3, 10, 4)
func_1263_call = mod.get_global_var('func_1263')
func_1266_call = mutated_mod.get_global_var('func_1266')
const_5808 = relay.const([-6.056294,9.036586,9.612495,3.343425,-7.247307,-6.367368,0.842242,5.814294,3.658202,8.726842,-2.789749,-3.749956,2.676629,7.400530,-3.316332,3.934514,6.246278,0.615559,0.371416,9.979534,-4.223560,8.423708,-3.668161,-0.421331,-3.002953,3.955961,1.407718,-8.039174,-7.143352,3.549454,-9.947144,5.027931,0.451943,-5.469929,4.219107,7.043009,6.677400,-2.974156,9.599889,9.513375,-7.028065,4.111042,5.130845,-4.509632,5.700147,-4.168129,-1.709291,-1.352541,-0.326183,-8.255286,-9.181844,7.625154,-1.464446,6.080661,-7.432978,1.910762,-2.499562,-9.655624,5.488394,3.966261,-5.103541,-8.482317,6.293936,2.970691,9.906161,-7.441538,1.109069,-9.730309,5.347159,1.030447,-1.369056,-5.168091,6.614072,-6.819224,-5.388855,-9.491995,4.207969,2.002583,0.796942,-3.192013,7.451323,-4.715902,-3.174090,-3.597252,2.885779,9.751278,0.604412,-3.498128,-3.300370,7.089113,-0.967831,-5.809080,-9.463224,-2.662205,-2.946971,-5.849257,8.729259,-5.397494,5.394028,8.117758,-9.575276,6.973063,4.018015,5.272397,-6.063324,-3.065875,-7.598149,7.598105,-4.357414,-5.046624,-1.901118,-9.311445,6.340610,-2.676098,-6.054358,4.178427,-3.120619,-3.272003,-3.491915,-6.664234,-8.844857,2.489529,0.185930,9.602348,1.751850,-8.222656,-4.336716,2.042808,5.409380,3.252398,-7.455692,-7.117054,0.412706,-6.750981,-5.958207,-3.574312,1.798952,0.548324,-7.486630,-6.272920,-4.453182,-0.374798,-6.728223,0.461236,5.711984,0.237909,4.540309,-0.339577,-2.761960,9.173413,4.964650,1.463389,7.725981,0.767604,5.422704,3.944370,-4.082839,-9.371151,-5.136021,-5.014815,-2.573210,6.489651,-2.444912,-6.576122,-6.540762,5.203253,-2.136893,-7.032459,-0.011411,7.450685,1.172701,7.293561,-5.910716,-7.103052,3.615499,-5.386272,-2.447539,-3.610189,-2.111774,1.658269,-0.406221,-3.493232,4.813141,-6.027066,6.667514,4.651771,1.782145,-5.471078,9.590393,-8.209756,-5.081753,-7.302775,-2.624929,8.883808,-8.704618,2.325487,2.618257,1.161111,-3.311774,-1.214013,4.013932,-9.209338,5.732928,7.615372,-7.266839,2.404113,-1.820494,4.556575,-1.651571,4.057976,-9.003399,1.539517,2.009294,-1.616452,3.669066,6.808112,4.749902,6.911770,-3.658349,7.564256,-6.934524,0.747654,-3.835899,7.189838,5.609219,0.796378,5.305771,-9.524209,9.234704,-1.701844,5.168721,-7.647169,3.521451,0.538733,-0.014036,-7.857434,-4.649617,2.883646,8.571023,1.888869,-3.248807,-5.404577,-1.065725,-1.118789,9.107149,-9.967509,-3.977994,2.746364,-1.256301,0.092799,6.822356,6.663320,-9.870094,2.465859,8.716208,-4.226443,9.509836,8.846803,3.219669,-3.046253,-0.812308,-3.006815,2.173344,-6.644631,-4.897710,-8.888781,-6.673213,8.899375,-5.858339,-3.575711,-5.319619,3.671856,5.106189,3.797332,-6.034397,4.566877,-9.107917,2.916376,-0.361147,6.742529,-0.488515,-0.396879,2.445715,4.917804,-7.953708,8.924656,-3.782681,3.310352,2.328672,1.265882,-4.388650,-8.156319,-0.590506,-7.799202,1.620562,1.702731,9.282198,-7.106709,-1.949552,-1.282788,6.115222,9.547277,6.233863,5.840838,6.479714,-0.674958,-7.983042,-6.086880,6.740780,8.291081,-5.986404,-4.592207,-4.494542,-8.888451,-6.365790,-8.214583,-5.908884,1.686912,-3.432318,-4.827182,3.964247,0.301858,6.180184,-5.011540,-4.801614,1.201636,1.391644,-7.492676,4.409876,-9.339350,6.998681,7.010113,-4.793497,9.847451,-6.649174,-2.637467,7.599697,6.319474,6.724903,8.720489,7.216041,-8.613775,-7.576645,-5.291901,3.396511,9.033978,0.496186,-0.304421,8.353104,-4.029761,3.003585,-6.562874,-3.940563,7.547084,4.230310,8.199186,0.961426,8.798670,-3.475668,4.277836,-7.662670,5.918123,-0.409743,5.328141,6.564749,3.043130,-9.299723,5.774319,2.871817,-4.473029,1.801697,9.027490,2.203870,-1.678198,-3.246037,6.062144,-9.957985,9.146085,-0.799241,9.602836,-6.652024,-3.323666,-5.291601,-9.258522,-1.501626,-2.013847,-3.394424,2.894446,9.744584,-9.824935,1.975910,-9.613201,-3.523207,-0.749468,9.212260,-4.444008,-2.286543,-9.787875,1.684293,-5.194751,-6.539628,7.433598,-3.488660,-1.468583,5.211401,-5.566977,6.654453,-5.061581,-9.842766,-0.406463,-9.669126,3.551045,-3.591655,2.321528,-8.127249,6.710997,2.294651,-1.918532,3.046228,0.431861,0.439495,-5.466606,-8.460199,-9.230963,3.425341,-1.903962,8.916519,3.347233,-1.349371,6.691247,-5.658829,8.114390,-1.512119,-2.365365,-4.960159,-1.857423,5.365668,-2.945844,5.468688,-6.108853,-5.126906,3.661750,-7.183595,8.402961,9.124850,-0.242391,1.827233,5.948344,5.545644,-0.261297,6.445215,6.387823,2.850282,0.759349,-8.208515,7.776846,-5.739735,-0.009770,2.443229,1.906475,7.104727,8.424307,3.856081,-8.915343,-8.744920,7.077333,6.374639,-8.920317,-7.476572,9.231985,4.330413,1.448349,4.897975,-6.652115,3.598864,-9.484977,5.675402,-3.669062,-0.249513,5.583747,2.599144,4.874583,5.574386,8.182408,0.357312,-9.594459,2.207205,-8.013168,-1.258604,-5.778796,0.439162,-8.961055,-0.105906,8.090419,4.679451,2.308540,4.962560,4.902771,-3.164004,7.552477,9.022661,-6.163432,7.905807,-3.985374,1.883395,-8.990664,5.580829,-8.115228,6.366005,-1.952052,-8.242072,9.363479,-8.694850,8.510550,5.489305,-2.281151,-8.895820,3.834351,-8.106190,0.622917,-2.949293,-6.706379,-5.849540,2.919667,-3.297352,-8.366357,3.055802,8.359792,-2.484475,-2.457416,3.484214,4.070041,8.551061,1.970672,-8.842856,-5.290642,-1.653486,-1.348962,4.662286,-8.501613,3.408486,-7.821503,-2.911948,6.630824,-8.604599,-6.371688,-0.732306,-3.623598,0.290635,1.875559,-8.765588,-7.018808,-8.742585,-0.904133,2.736095,-5.733205,0.697608,2.722088,-5.303068,8.606211,1.768426,-8.935867,0.922540,8.544916,-0.774626,-1.381847,-0.531272,-1.475469,4.083576,-1.414063,2.865274,9.654696,-8.133055,1.936562,2.937577,2.394569,-5.184939,6.712149,-9.786023,-0.392273,2.569778,-7.776782,-3.838417,2.720027,5.258495,-5.210047,-8.338338,5.426447,-9.404302,2.045085,6.337439,-2.767459,-9.959318,3.870475,8.964529,9.086954,-1.794031,-4.352215,-7.578339,-6.997451,-5.839744,9.363988,2.996884,5.210142,6.078368,7.353109,1.937726,-9.904380,0.408481,3.738244,-3.967586,-7.958834,-7.279345,7.097700,-7.027143,-8.030084,-7.466997,2.166975,-7.415759,9.270530,2.959954,0.702821,9.007193,-2.981140,8.655147,3.749260,-3.528669,7.117100,-7.296611,-4.331366,-2.061177,5.779624,-4.516157,-7.449629,5.148520,-8.907113,7.399169,-4.039311,7.086378,1.610950,-1.517356,-0.564233,-9.134173,6.480938,-3.711435,0.961265,-6.727693,6.005491,1.255275,7.221967,-2.907879,2.856847,3.836377,-7.343084,-0.444190,-1.274661,-7.943531,-3.724656,-5.834754,6.645516,7.287036,3.501222,-8.146069,-4.575234,3.083176,-6.314950,9.404120,9.362540,2.992378,1.484768,0.300847,-8.544710,2.647925,3.683897,-1.256552,-3.026611,1.659544,8.523963,5.407476,-4.736044,-5.831488,-8.707245,-5.887464,-6.838987,2.518999,-6.307130,1.712006,-5.329709,1.105251,-6.270217,-5.807435,6.363001,7.455951,5.333799,-8.871736,6.176603,7.183707,-6.613491,3.516399,7.862921,-2.086379,6.095893,3.161135,-7.974168,1.846517,-9.011881,-8.983768,-6.166110,2.306557,-2.338161,7.383846,-5.508340,7.674332,-7.227744,2.179712,8.314643,2.964090,-7.630218,-1.737766,4.441337,2.053613,5.949733,9.933675,2.075748,-7.440366,-6.938333,3.234382,-2.189651,0.762377,1.312880,-8.079639,0.481242,-9.492666,-6.452356,-8.231562,-5.051225,-0.786212,0.986608,0.231255,-3.492185,-9.738545,2.379460,4.994798,-2.982414,6.532896,5.382848,-9.422486,9.519442,-1.565060,5.184658,-9.981818,3.989378,-6.977461,-4.450086,5.228597,3.780849,-6.570242,-8.006417,-6.852092,-4.921343,-2.728907,9.092841,-5.911828,6.531823,5.509012,-3.568473,9.592289,-8.987441], dtype = "float32")#candidate|5808|(768,)|const|float32
call_5807 = relay.TupleGetItem(func_1263_call(relay.reshape(const_5808.astype('float32'), [16, 6, 8])), 0)
call_5809 = relay.TupleGetItem(func_1266_call(relay.reshape(const_5808.astype('float32'), [16, 6, 8])), 0)
func_1687_call = mod.get_global_var('func_1687')
func_1690_call = mutated_mod.get_global_var('func_1690')
const_5814 = relay.const([-5.350127,-7.046966,0.424533,3.269221,-5.501133,-9.083179,5.725241,-9.763361,-2.590181,-8.536457,-3.577230,9.872897,3.942278,9.418825,3.466965,-7.200163,-7.137745,6.555344,2.119381,1.684741,6.996677,9.666131,-7.721083,2.499442,2.082806,7.030092,8.479309,0.468714,4.428024,-9.481845,-4.804731,-2.888173,1.617755,6.053333,-4.644894,-7.699415,-0.344522,-1.144783,-0.775017,0.647656,1.404275,0.517241,9.677378,-2.318582,3.160616,4.739410,3.077204,-5.964886,4.613840,0.569542,-7.580334,7.805545,7.971467,-4.868825,-5.652916,-9.726849,-7.523310,-6.862571,-7.054045,-8.709141,8.349762,4.704673,0.907779,-5.761696,7.330319,-5.388448,9.569095,-3.702065,-4.373182,-0.032211,-2.706391,-2.242821,2.032224,-6.828835,8.665323,2.234580,-1.108940,-5.619672,5.701051,-1.949719,-7.210356,-5.373127,6.229468,9.302597,5.513161,-0.142193,-0.927404,-5.743038,0.300902,9.411458,3.733259,-4.631173,2.298269,7.467678,8.982496,-4.223792,5.961822,7.728464,5.738043,-5.613842,3.123456,1.222487,5.729975,8.281125,-8.506238,-8.621749,7.494598,-6.132471,7.257342,3.793544,5.896559,-8.552900,6.664822,1.781669,-6.788748,3.403108,-6.923888,6.391944,9.579018,3.072322,9.307893,4.857319,-2.739845,-5.768011,-3.604958,-5.642752,4.746140,-2.119392,-1.905992,7.218959,1.382801,-0.084932,9.625559,4.380010,-8.215166,9.295739,-8.224145,7.638984,-3.017263,-3.283843,2.068985,-2.831571,-2.498576,5.307835,2.567597,0.226441,-3.481984,-6.661428,-2.728897,-0.487656,-3.588063,-2.381262,-2.240099,1.474147,1.979883,8.852869,-5.261460,3.409605,-3.334616,-8.150472,-8.316538,-0.100959,1.052611,-8.302296,3.038132,2.863164,-0.668623,-1.897485], dtype = "float64")#candidate|5814|(168,)|const|float64
call_5813 = func_1687_call(relay.reshape(const_5814.astype('float64'), [4, 14, 3]))
call_5815 = func_1687_call(relay.reshape(const_5814.astype('float64'), [4, 14, 3]))
func_5157_call = mod.get_global_var('func_5157')
func_5158_call = mutated_mod.get_global_var('func_5158')
call_5816 = relay.TupleGetItem(func_5157_call(), 0)
call_5817 = relay.TupleGetItem(func_5158_call(), 0)
func_4416_call = mod.get_global_var('func_4416')
func_4417_call = mutated_mod.get_global_var('func_4417')
call_5819 = relay.TupleGetItem(func_4416_call(), 0)
call_5820 = relay.TupleGetItem(func_4417_call(), 0)
func_4693_call = mod.get_global_var('func_4693')
func_4694_call = mutated_mod.get_global_var('func_4694')
call_5831 = func_4693_call()
call_5832 = func_4693_call()
uop_5845 = relay.acos(var_5801.astype('float64')) # shape=(3, 10, 4)
func_4147_call = mod.get_global_var('func_4147')
func_4148_call = mutated_mod.get_global_var('func_4148')
call_5851 = func_4147_call()
call_5852 = func_4147_call()
uop_5856 = relay.sqrt(var_5801.astype('float32')) # shape=(3, 10, 4)
bop_5867 = relay.bitwise_or(uop_5856.astype('int64'), relay.reshape(var_5801.astype('int64'), relay.shape_of(uop_5856))) # shape=(3, 10, 4)
output = relay.Tuple([bop_5802,call_5807,const_5808,call_5813,const_5814,call_5816,call_5819,call_5831,uop_5845,call_5851,bop_5867,])
output2 = relay.Tuple([bop_5802,call_5809,const_5808,call_5815,const_5814,call_5817,call_5820,call_5832,uop_5845,call_5852,bop_5867,])
func_5870 = relay.Function([var_5800,var_5801,], output)
mod['func_5870'] = func_5870
mod = relay.transform.InferType()(mod)
mutated_mod['func_5870'] = func_5870
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5870_call = mutated_mod.get_global_var('func_5870')
var_5872 = relay.var("var_5872", dtype = "int8", shape = ())#candidate|5872|()|var|int8
var_5873 = relay.var("var_5873", dtype = "int8", shape = (3, 10, 4))#candidate|5873|(3, 10, 4)|var|int8
call_5871 = func_5870_call(var_5872,var_5873,)
output = call_5871
func_5874 = relay.Function([var_5872,var_5873,], output)
mutated_mod['func_5874'] = func_5874
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5909 = relay.var("var_5909", dtype = "int32", shape = (5, 15, 4))#candidate|5909|(5, 15, 4)|var|int32
const_5910 = relay.const([[[7,-10,-6,2],[-2,5,10,-6],[8,-1,7,3],[-3,-9,9,6],[5,-1,-4,8],[3,-1,7,-9],[7,5,-7,-7],[-5,-9,-8,-2],[-1,-5,3,1],[1,10,-1,3],[10,1,-8,8],[-7,-8,1,1],[1,7,9,10],[1,-10,-1,-2],[2,-8,4,-4]],[[2,9,1,5],[3,-6,1,-4],[7,9,-8,-1],[-8,3,-7,-4],[-10,-2,10,3],[-1,-10,4,-9],[10,3,10,-8],[-2,-10,-9,-8],[7,8,-1,-3],[-9,-7,6,7],[5,-4,3,3],[3,6,8,-3],[-6,-2,-3,1],[7,6,-5,9],[-3,5,5,3]],[[3,-1,3,-8],[4,-10,-7,8],[9,9,-7,2],[-1,3,-6,5],[-6,-10,2,-2],[8,-5,2,-8],[7,3,-6,-1],[-3,-5,3,-8],[-8,-1,-6,7],[6,-8,-5,-9],[6,6,8,-10],[-6,-2,5,-1],[8,-3,7,-8],[-4,-3,-5,-3],[6,-4,1,-7]],[[-9,5,1,-8],[9,5,3,-1],[2,-8,-8,-7],[-2,-9,4,-7],[7,8,-9,-8],[10,-4,-9,-2],[1,-7,10,-1],[6,5,-6,-5],[-8,2,3,-6],[3,8,5,4],[-9,-4,8,5],[-5,-6,-5,-3],[-7,-10,5,3],[-6,-2,10,-6],[9,-10,-5,-3]],[[-5,1,-1,5],[-9,8,3,-2],[2,-9,-1,3],[-6,7,10,-2],[-10,-7,7,-8],[-8,-10,10,9],[7,-6,4,-8],[-4,10,6,9],[4,6,-9,-6],[5,-8,-8,-8],[-5,-3,8,7],[-8,-6,-10,-2],[-2,-6,5,7],[-7,-6,2,-2],[-10,5,-6,-8]]], dtype = "int32")#candidate|5910|(5, 15, 4)|const|int32
bop_5911 = relay.logical_xor(var_5909.astype('int32'), relay.reshape(const_5910.astype('int32'), relay.shape_of(var_5909))) # shape=(5, 15, 4)
func_5755_call = mod.get_global_var('func_5755')
func_5762_call = mutated_mod.get_global_var('func_5762')
var_5928 = relay.var("var_5928", dtype = "float32", shape = (495,))#candidate|5928|(495,)|var|float32
const_5929 = relay.const([[-10,-6,-7,9,-8,4,-9,-7,-1],[-6,-4,-10,8,-5,9,-9,-8,5],[-3,-5,-9,8,-1,2,-10,2,3],[-6,-3,-1,2,-9,-6,6,-1,2],[-1,8,7,-4,8,-8,10,-10,-9],[-3,-3,-1,-1,10,-7,1,-3,10],[9,-7,-9,-6,1,2,-8,-10,9],[10,8,1,-2,-1,-1,7,4,7],[-10,-2,10,10,-9,1,-4,8,-10],[-5,-1,-1,9,4,-3,9,-5,-4],[-7,5,7,-5,-6,2,4,-2,6],[-1,1,-2,-8,6,4,-8,-6,-8],[-10,3,8,4,5,-10,7,-9,7],[-3,-2,8,-10,-6,1,9,-7,-7],[-10,-8,7,5,9,4,-5,1,-5],[3,5,-4,-3,8,-5,-6,8,-9],[4,-8,-10,-9,9,-10,6,2,3],[10,8,6,4,10,8,6,-5,-4],[-7,10,10,-2,3,2,1,4,1],[-3,-3,-7,-4,4,-9,6,9,2],[6,-10,10,-7,-3,10,-2,-8,-8],[8,10,-3,8,5,-5,-9,-2,2],[-8,-5,-9,-6,6,5,-1,-7,-5],[-1,10,-10,-4,-6,7,-10,-6,-7],[-8,7,7,1,7,2,-8,4,-1],[-3,-3,-3,8,5,-8,10,-5,3],[2,-3,-2,10,-10,-8,-7,5,-1],[-10,4,2,8,-2,-10,5,9,-1],[-3,-10,5,3,8,-4,8,7,-7],[-4,10,8,-10,-4,-2,-1,7,-9],[9,4,10,6,2,-10,2,-6,9],[-6,8,10,-6,9,4,6,10,3],[-8,7,-4,-10,10,-1,-9,-8,7],[-9,10,-6,5,-6,-2,4,9,1],[-10,-8,-5,9,-5,3,4,-7,-1],[9,-5,-3,-3,8,-10,-5,-7,1],[1,-10,-7,-2,-6,-7,2,-6,-10],[-5,-6,7,1,8,-5,2,7,4],[-4,6,5,-10,9,5,5,-2,-2],[-8,-1,1,-3,1,6,7,4,-3],[-7,8,-6,-5,3,-3,8,-8,-6],[-2,3,-3,1,-10,-3,5,-5,-6],[-6,-4,-8,-5,-6,5,3,3,3],[6,7,-8,-10,-10,6,6,9,-2],[-4,-3,-2,-4,-8,-3,-6,2,7],[-2,4,2,10,-3,-7,-5,-4,3],[9,-10,-8,-5,-4,-6,10,1,-1],[-6,-10,-9,-6,8,-3,5,-10,-10],[-10,3,-3,-8,-10,-8,2,4,-3],[-7,-7,8,-9,3,-9,-8,-7,6],[1,-4,-3,-1,-8,-6,-8,-1,-1],[-7,3,-10,5,3,10,-4,3,3],[4,-4,-1,-5,-5,-5,7,-7,-6],[-3,4,2,5,-6,-8,8,-4,-2],[3,3,-4,-6,-2,1,9,-8,-2],[-8,8,9,4,-8,2,-3,-7,-4],[-7,-4,-3,-7,-1,-7,7,1,-3],[3,-8,6,-3,6,5,3,-2,1],[3,10,-4,6,4,1,8,5,-7],[7,-9,-9,2,-8,-2,2,8,-9],[8,-6,-3,-10,-2,-8,-5,10,5],[-2,-5,3,-7,3,4,-8,9,5],[-4,4,9,7,-6,-9,6,10,-2],[-9,8,6,3,-8,-9,-4,-9,9],[10,-3,-2,-7,-6,2,-2,6,-2],[-5,8,7,6,2,-2,3,-6,-8],[9,-1,-4,2,3,-9,-2,-9,-8],[10,10,9,-1,-5,9,9,1,-4],[10,-3,5,9,-6,8,7,-6,-7],[10,-9,9,8,-5,-6,4,-6,1]], dtype = "uint16")#candidate|5929|(70, 9)|const|uint16
var_5930 = relay.var("var_5930", dtype = "int32", shape = (3,))#candidate|5930|(3,)|var|int32
const_5931 = relay.const([[-8,-4,3,4],[2,-7,-1,5],[2,-4,6,7],[1,10,7,-7],[-9,9,7,-1],[-7,7,-5,-7],[6,7,-1,5],[-2,1,7,4],[1,9,-9,6],[9,3,6,8],[1,3,10,3],[-10,-3,2,-6],[3,10,-4,-7],[2,4,1,-9],[9,-4,9,-3],[2,10,3,7],[-9,-7,7,-7],[-3,-8,-5,7],[-10,-3,8,10],[1,-4,-5,-2],[1,-1,-3,-9],[1,3,6,-10],[-10,-5,-10,-8],[6,7,4,8],[-9,2,-7,-2],[-8,-4,4,-1],[8,5,-3,-1],[7,-10,7,4],[9,2,9,-6],[-9,-1,4,-9],[8,-2,-9,7],[1,4,-7,6],[6,-4,1,4],[-10,-3,7,-9],[-8,-5,4,-10],[1,-2,4,-8],[7,-7,-2,8],[-6,-6,-7,-7],[6,1,-5,-4],[6,-9,-4,-1],[9,-1,9,-4],[-2,-7,7,-3]], dtype = "int32")#candidate|5931|(42, 4)|const|int32
const_5932 = relay.const([2,4,-2,-2,9,8,-8,9,9,-9,-2,-5,-10,-4,-7], dtype = "uint8")#candidate|5932|(15,)|const|uint8
call_5927 = relay.TupleGetItem(func_5755_call(relay.reshape(var_5928.astype('float32'), [15, 3, 11]), relay.reshape(const_5929.astype('uint16'), [630,]), relay.reshape(var_5930.astype('int32'), [3,]), relay.reshape(const_5931.astype('int32'), [168,]), relay.reshape(const_5932.astype('uint8'), [1, 15]), ), 11)
call_5933 = relay.TupleGetItem(func_5762_call(relay.reshape(var_5928.astype('float32'), [15, 3, 11]), relay.reshape(const_5929.astype('uint16'), [630,]), relay.reshape(var_5930.astype('int32'), [3,]), relay.reshape(const_5931.astype('int32'), [168,]), relay.reshape(const_5932.astype('uint8'), [1, 15]), ), 11)
output = relay.Tuple([bop_5911,call_5927,var_5928,const_5929,var_5930,const_5931,const_5932,])
output2 = relay.Tuple([bop_5911,call_5933,var_5928,const_5929,var_5930,const_5931,const_5932,])
func_5939 = relay.Function([var_5909,var_5928,var_5930,], output)
mod['func_5939'] = func_5939
mod = relay.transform.InferType()(mod)
mutated_mod['func_5939'] = func_5939
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5939_call = mutated_mod.get_global_var('func_5939')
var_5941 = relay.var("var_5941", dtype = "int32", shape = (5, 15, 4))#candidate|5941|(5, 15, 4)|var|int32
var_5942 = relay.var("var_5942", dtype = "float32", shape = (495,))#candidate|5942|(495,)|var|float32
var_5943 = relay.var("var_5943", dtype = "int32", shape = (3,))#candidate|5943|(3,)|var|int32
call_5940 = func_5939_call(var_5941,var_5942,var_5943,)
output = call_5940
func_5944 = relay.Function([var_5941,var_5942,var_5943,], output)
mutated_mod['func_5944'] = func_5944
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5946 = relay.var("var_5946", dtype = "uint32", shape = ())#candidate|5946|()|var|uint32
var_5947 = relay.var("var_5947", dtype = "uint32", shape = (5, 16, 1))#candidate|5947|(5, 16, 1)|var|uint32
bop_5948 = relay.bitwise_and(var_5946.astype('uint32'), var_5947.astype('uint32')) # shape=(5, 16, 1)
uop_5957 = relay.asin(bop_5948.astype('float64')) # shape=(5, 16, 1)
func_1329_call = mod.get_global_var('func_1329')
func_1333_call = mutated_mod.get_global_var('func_1333')
var_5976 = relay.var("var_5976", dtype = "uint32", shape = (220,))#candidate|5976|(220,)|var|uint32
var_5977 = relay.var("var_5977", dtype = "int8", shape = (110, 1))#candidate|5977|(110, 1)|var|int8
call_5975 = relay.TupleGetItem(func_1329_call(relay.reshape(var_5976.astype('uint32'), [4, 11, 5]), relay.reshape(var_5977.astype('int8'), [110,]), ), 1)
call_5978 = relay.TupleGetItem(func_1333_call(relay.reshape(var_5976.astype('uint32'), [4, 11, 5]), relay.reshape(var_5977.astype('int8'), [110,]), ), 1)
func_5396_call = mod.get_global_var('func_5396')
func_5398_call = mutated_mod.get_global_var('func_5398')
call_5980 = relay.TupleGetItem(func_5396_call(), 0)
call_5981 = relay.TupleGetItem(func_5398_call(), 0)
func_4416_call = mod.get_global_var('func_4416')
func_4417_call = mutated_mod.get_global_var('func_4417')
call_5986 = relay.TupleGetItem(func_4416_call(), 0)
call_5987 = relay.TupleGetItem(func_4417_call(), 0)
output = relay.Tuple([uop_5957,call_5975,var_5976,var_5977,call_5980,call_5986,])
output2 = relay.Tuple([uop_5957,call_5978,var_5976,var_5977,call_5981,call_5987,])
func_5991 = relay.Function([var_5946,var_5947,var_5976,var_5977,], output)
mod['func_5991'] = func_5991
mod = relay.transform.InferType()(mod)
var_5992 = relay.var("var_5992", dtype = "uint32", shape = ())#candidate|5992|()|var|uint32
var_5993 = relay.var("var_5993", dtype = "uint32", shape = (5, 16, 1))#candidate|5993|(5, 16, 1)|var|uint32
var_5994 = relay.var("var_5994", dtype = "uint32", shape = (220,))#candidate|5994|(220,)|var|uint32
var_5995 = relay.var("var_5995", dtype = "int8", shape = (110, 1))#candidate|5995|(110, 1)|var|int8
output = func_5991(var_5992,var_5993,var_5994,var_5995,)
func_5996 = relay.Function([var_5992,var_5993,var_5994,var_5995,], output)
mutated_mod['func_5996'] = func_5996
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4640_call = mod.get_global_var('func_4640')
func_4642_call = mutated_mod.get_global_var('func_4642')
call_6004 = relay.TupleGetItem(func_4640_call(), 0)
call_6005 = relay.TupleGetItem(func_4642_call(), 0)
output = relay.Tuple([call_6004,])
output2 = relay.Tuple([call_6005,])
func_6012 = relay.Function([], output)
mod['func_6012'] = func_6012
mod = relay.transform.InferType()(mod)
mutated_mod['func_6012'] = func_6012
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6012_call = mutated_mod.get_global_var('func_6012')
call_6013 = func_6012_call()
output = call_6013
func_6014 = relay.Function([], output)
mutated_mod['func_6014'] = func_6014
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4660_call = mod.get_global_var('func_4660')
func_4662_call = mutated_mod.get_global_var('func_4662')
call_6018 = relay.TupleGetItem(func_4660_call(), 0)
call_6019 = relay.TupleGetItem(func_4662_call(), 0)
func_3731_call = mod.get_global_var('func_3731')
func_3734_call = mutated_mod.get_global_var('func_3734')
var_6040 = relay.var("var_6040", dtype = "float32", shape = (132,))#candidate|6040|(132,)|var|float32
call_6039 = relay.TupleGetItem(func_3731_call(relay.reshape(var_6040.astype('float32'), [12, 1, 11])), 0)
call_6041 = relay.TupleGetItem(func_3734_call(relay.reshape(var_6040.astype('float32'), [12, 1, 11])), 0)
bop_6053 = relay.equal(call_6039.astype('bool'), relay.reshape(var_6040.astype('bool'), relay.shape_of(call_6039))) # shape=(12, 1, 11)
bop_6056 = relay.equal(call_6041.astype('bool'), relay.reshape(var_6040.astype('bool'), relay.shape_of(call_6041))) # shape=(12, 1, 11)
uop_6060 = relay.acosh(call_6039.astype('float32')) # shape=(12, 1, 11)
uop_6062 = relay.acosh(call_6041.astype('float32')) # shape=(12, 1, 11)
uop_6066 = relay.acos(call_6039.astype('float64')) # shape=(12, 1, 11)
uop_6068 = relay.acos(call_6041.astype('float64')) # shape=(12, 1, 11)
func_4567_call = mod.get_global_var('func_4567')
func_4569_call = mutated_mod.get_global_var('func_4569')
const_6070 = relay.const([-7,-1,4,-7,10,3,7,-8,10,4,9,4,9,-7,10], dtype = "uint8")#candidate|6070|(15,)|const|uint8
call_6069 = relay.TupleGetItem(func_4567_call(relay.reshape(const_6070.astype('uint8'), [15,])), 3)
call_6071 = relay.TupleGetItem(func_4569_call(relay.reshape(const_6070.astype('uint8'), [15,])), 3)
uop_6072 = relay.sinh(uop_6060.astype('float32')) # shape=(12, 1, 11)
uop_6074 = relay.sinh(uop_6062.astype('float32')) # shape=(12, 1, 11)
uop_6075 = relay.sin(uop_6072.astype('float32')) # shape=(12, 1, 11)
uop_6077 = relay.sin(uop_6074.astype('float32')) # shape=(12, 1, 11)
func_4640_call = mod.get_global_var('func_4640')
func_4642_call = mutated_mod.get_global_var('func_4642')
call_6078 = relay.TupleGetItem(func_4640_call(), 0)
call_6079 = relay.TupleGetItem(func_4642_call(), 0)
output = relay.Tuple([call_6018,bop_6053,uop_6066,call_6069,const_6070,uop_6075,call_6078,])
output2 = relay.Tuple([call_6019,bop_6056,uop_6068,call_6071,const_6070,uop_6077,call_6079,])
func_6082 = relay.Function([var_6040,], output)
mod['func_6082'] = func_6082
mod = relay.transform.InferType()(mod)
mutated_mod['func_6082'] = func_6082
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6083 = relay.var("var_6083", dtype = "float32", shape = (132,))#candidate|6083|(132,)|var|float32
func_6082_call = mutated_mod.get_global_var('func_6082')
call_6084 = func_6082_call(var_6083)
output = call_6084
func_6085 = relay.Function([var_6083], output)
mutated_mod['func_6085'] = func_6085
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5396_call = mod.get_global_var('func_5396')
func_5398_call = mutated_mod.get_global_var('func_5398')
call_6157 = relay.TupleGetItem(func_5396_call(), 1)
call_6158 = relay.TupleGetItem(func_5398_call(), 1)
func_4416_call = mod.get_global_var('func_4416')
func_4417_call = mutated_mod.get_global_var('func_4417')
call_6166 = relay.TupleGetItem(func_4416_call(), 0)
call_6167 = relay.TupleGetItem(func_4417_call(), 0)
output = relay.Tuple([call_6157,call_6166,])
output2 = relay.Tuple([call_6158,call_6167,])
func_6175 = relay.Function([], output)
mod['func_6175'] = func_6175
mod = relay.transform.InferType()(mod)
mutated_mod['func_6175'] = func_6175
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6175_call = mutated_mod.get_global_var('func_6175')
call_6176 = func_6175_call()
output = call_6176
func_6177 = relay.Function([], output)
mutated_mod['func_6177'] = func_6177
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5645_call = mod.get_global_var('func_5645')
func_5646_call = mutated_mod.get_global_var('func_5646')
call_6212 = func_5645_call()
call_6213 = func_5645_call()
func_2385_call = mod.get_global_var('func_2385')
func_2388_call = mutated_mod.get_global_var('func_2388')
const_6232 = relay.const(8, dtype = "uint8")#candidate|6232|()|const|uint8
const_6233 = relay.const([[6,-6,8,-6,-9,9,-1,2,-9,-6,-1,-8,-10,-2,5,-10,-4,6,2,8,-6,-5,-1,8,-7,7,-5,-1,-8,-8,2,3,-6,-9,5,-2,-6,6,7,-7,8,2,-1,-10,7,3,8,7,-9,2,8,2,4,1,-4,6,4,-7,5,7,5,-1,-6,-9,-9,-8,7,-10,10,2,2,5,-8,-3,8,-2,10,10,-6,-10,9,1,-9,-7,-4,2,9,-2,-10,9,-4,2,8,9,-10,8,-8,5,2,8,-3,2,8,8,-10,7,-9,8,-1,-9,8,10,8,5,5,6,6,9,-1,-3,3,-4,6,-8,-1,-10,4,-4,3,-2,5,-8,5,4,-2,8,-4,6,8,-1,-10,-5,10,1,-1,2,1,6,7,4,6,5,-8,-3,6,3,-4,-4,-8,-8,6,-4,1,-4,7,-8,-2,4,-3,-6,1,-6,-10,7,-5,-6,6,9,9,4,3,-10,4,-7,-2,-7,-4,8,-5,-1,-2,3,-8,-5,-8,-2,10,8,-7,2,-1,10,4,-9,-5,-9,-9,4,7,-2,-6,-5,-6,2,-1,-3,-5,-10,-3,8,-1,-4,1,10,5,10,8,-10,2,8,-8,8,5,2,6,5,-9,10,5,8,1,3,-5,4,7,-3,-4,-8,-6,7,2,-1,-9,1,-10,5,-6,1,-1,1,8,5,-4,10],[-3,3,-9,6,-5,3,7,9,8,7,8,9,3,-7,-7,6,-6,-7,3,-4,-2,8,-6,-3,8,4,-1,1,7,10,8,5,-6,8,6,10,8,-9,4,1,-3,7,7,7,-7,-7,-2,-9,-5,-8,9,-10,7,-3,3,-4,-8,10,10,-9,-2,-3,1,5,-9,6,2,-6,7,-1,-3,7,-7,-9,2,-5,6,-3,10,-2,8,8,8,-10,-3,-5,5,2,-7,-8,-8,-5,2,3,5,-10,7,-4,2,-10,-4,-5,-5,10,5,2,2,-10,-7,-6,-2,5,6,4,3,5,9,8,-7,7,-8,-7,-8,5,-2,8,-7,3,2,1,3,5,-8,-7,1,8,3,-10,-2,8,3,-10,-9,-6,-2,8,-5,-9,-8,-9,-2,-10,2,-8,4,10,2,-10,5,-1,2,-4,6,1,4,5,-9,-3,-5,-7,8,6,9,10,1,3,-5,-2,2,5,5,2,-4,-7,7,-8,5,-7,-10,-10,-2,-4,-2,8,-2,-10,4,3,10,-9,-5,-3,10,5,-9,-3,-10,8,5,-3,-10,6,-8,3,10,-4,8,-5,9,10,-7,-1,-10,-6,-4,4,6,9,8,2,4,2,5,-2,-9,4,-3,-2,1,-10,9,-2,-1,-8,5,-8,6,-2,-9,-5,5,4,-4,3,-6,-4,-4,-1,7,5,-9,-10,-2,6]], dtype = "uint8")#candidate|6233|(2, 264)|const|uint8
call_6231 = relay.TupleGetItem(func_2385_call(relay.reshape(const_6232.astype('uint8'), []), relay.reshape(const_6233.astype('uint8'), [12, 11, 4]), ), 0)
call_6234 = relay.TupleGetItem(func_2388_call(relay.reshape(const_6232.astype('uint8'), []), relay.reshape(const_6233.astype('uint8'), [12, 11, 4]), ), 0)
output = relay.Tuple([call_6212,call_6231,const_6232,const_6233,])
output2 = relay.Tuple([call_6213,call_6234,const_6232,const_6233,])
func_6247 = relay.Function([], output)
mod['func_6247'] = func_6247
mod = relay.transform.InferType()(mod)
mutated_mod['func_6247'] = func_6247
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6247_call = mutated_mod.get_global_var('func_6247')
call_6248 = func_6247_call()
output = call_6248
func_6249 = relay.Function([], output)
mutated_mod['func_6249'] = func_6249
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4660_call = mod.get_global_var('func_4660')
func_4662_call = mutated_mod.get_global_var('func_4662')
call_6253 = relay.TupleGetItem(func_4660_call(), 0)
call_6254 = relay.TupleGetItem(func_4662_call(), 0)
output = call_6253
output2 = call_6254
func_6264 = relay.Function([], output)
mod['func_6264'] = func_6264
mod = relay.transform.InferType()(mod)
output = func_6264()
func_6265 = relay.Function([], output)
mutated_mod['func_6265'] = func_6265
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6288 = relay.var("var_6288", dtype = "int32", shape = (8, 6, 3))#candidate|6288|(8, 6, 3)|var|int32
const_6289 = relay.const([[[-6,-9,3],[5,-6,7],[-7,-8,-1],[7,7,-3],[-2,2,2],[-10,-5,5]],[[-2,-3,-1],[-8,-1,3],[9,-1,-7],[-9,-3,5],[-3,4,-5],[-3,1,-5]],[[8,-3,10],[-8,5,-5],[-6,-5,5],[6,6,-3],[3,8,-4],[6,-8,9]],[[-6,7,10],[6,-6,9],[-3,-7,-7],[10,8,1],[2,-4,-8],[-8,-3,8]],[[5,-1,6],[-2,5,10],[4,1,7],[-6,3,9],[4,-6,10],[-8,7,-8]],[[9,2,3],[-5,1,1],[-2,-8,6],[6,5,-4],[-5,2,2],[-5,-3,-5]],[[8,-3,8],[6,10,4],[-1,3,2],[3,-10,1],[6,-4,-2],[5,-7,-8]],[[4,-6,8],[-10,10,-7],[3,-2,-6],[6,9,-10],[9,1,-6],[2,3,-4]]], dtype = "int32")#candidate|6289|(8, 6, 3)|const|int32
bop_6290 = relay.minimum(var_6288.astype('int32'), relay.reshape(const_6289.astype('int32'), relay.shape_of(var_6288))) # shape=(8, 6, 3)
func_6082_call = mod.get_global_var('func_6082')
func_6085_call = mutated_mod.get_global_var('func_6085')
var_6304 = relay.var("var_6304", dtype = "float32", shape = (132,))#candidate|6304|(132,)|var|float32
call_6303 = relay.TupleGetItem(func_6082_call(relay.reshape(var_6304.astype('float32'), [132,])), 1)
call_6305 = relay.TupleGetItem(func_6085_call(relay.reshape(var_6304.astype('float32'), [132,])), 1)
output = relay.Tuple([bop_6290,call_6303,var_6304,])
output2 = relay.Tuple([bop_6290,call_6305,var_6304,])
func_6313 = relay.Function([var_6288,var_6304,], output)
mod['func_6313'] = func_6313
mod = relay.transform.InferType()(mod)
var_6314 = relay.var("var_6314", dtype = "int32", shape = (8, 6, 3))#candidate|6314|(8, 6, 3)|var|int32
var_6315 = relay.var("var_6315", dtype = "float32", shape = (132,))#candidate|6315|(132,)|var|float32
output = func_6313(var_6314,var_6315,)
func_6316 = relay.Function([var_6314,var_6315,], output)
mutated_mod['func_6316'] = func_6316
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4147_call = mod.get_global_var('func_4147')
func_4148_call = mutated_mod.get_global_var('func_4148')
call_6321 = func_4147_call()
call_6322 = func_4147_call()
output = call_6321
output2 = call_6322
func_6325 = relay.Function([], output)
mod['func_6325'] = func_6325
mod = relay.transform.InferType()(mod)
output = func_6325()
func_6326 = relay.Function([], output)
mutated_mod['func_6326'] = func_6326
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5396_call = mod.get_global_var('func_5396')
func_5398_call = mutated_mod.get_global_var('func_5398')
call_6340 = relay.TupleGetItem(func_5396_call(), 0)
call_6341 = relay.TupleGetItem(func_5398_call(), 0)
output = call_6340
output2 = call_6341
func_6358 = relay.Function([], output)
mod['func_6358'] = func_6358
mod = relay.transform.InferType()(mod)
output = func_6358()
func_6359 = relay.Function([], output)
mutated_mod['func_6359'] = func_6359
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4693_call = mod.get_global_var('func_4693')
func_4694_call = mutated_mod.get_global_var('func_4694')
call_6377 = func_4693_call()
call_6378 = func_4693_call()
func_430_call = mod.get_global_var('func_430')
func_433_call = mutated_mod.get_global_var('func_433')
var_6395 = relay.var("var_6395", dtype = "float64", shape = ())#candidate|6395|()|var|float64
const_6396 = relay.const([[5],[3],[-1],[-7],[4],[-2],[7],[-6],[-10],[8],[-9],[-8],[6],[-5],[-4],[-3],[10],[-8],[-2],[2],[2],[-8],[7],[-2],[1],[10],[4],[-1],[4],[7],[2],[6],[7],[-5],[-8],[4],[2],[-9],[-9],[3],[-10],[10],[-10],[6],[-6],[9],[-4],[-3],[10],[7],[-6],[8],[-4],[4],[-7],[-3],[-9],[2],[-3],[-3],[-3],[10],[9],[6],[1],[7],[-8],[-3],[9],[6],[-6],[4],[-4],[-7],[7],[8],[2],[7],[9],[-1],[1],[-8],[-1],[1],[-10],[-8],[8],[4],[-10],[-8],[8],[-7],[4],[-4],[-9],[3],[-2],[-7],[4],[7],[-7],[-10],[6],[-6],[4],[-3],[10],[5],[-4],[-6]], dtype = "int8")#candidate|6396|(110, 1)|const|int8
call_6394 = relay.TupleGetItem(func_430_call(relay.reshape(var_6395.astype('float64'), []), relay.reshape(const_6396.astype('int8'), [22, 5]), ), 4)
call_6397 = relay.TupleGetItem(func_433_call(relay.reshape(var_6395.astype('float64'), []), relay.reshape(const_6396.astype('int8'), [22, 5]), ), 4)
output = relay.Tuple([call_6377,call_6394,var_6395,const_6396,])
output2 = relay.Tuple([call_6378,call_6397,var_6395,const_6396,])
func_6408 = relay.Function([var_6395,], output)
mod['func_6408'] = func_6408
mod = relay.transform.InferType()(mod)
var_6409 = relay.var("var_6409", dtype = "float64", shape = ())#candidate|6409|()|var|float64
output = func_6408(var_6409)
func_6410 = relay.Function([var_6409], output)
mutated_mod['func_6410'] = func_6410
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5797_call = mod.get_global_var('func_5797')
func_5799_call = mutated_mod.get_global_var('func_5799')
call_6425 = relay.TupleGetItem(func_5797_call(), 0)
call_6426 = relay.TupleGetItem(func_5799_call(), 0)
output = call_6425
output2 = call_6426
func_6434 = relay.Function([], output)
mod['func_6434'] = func_6434
mod = relay.transform.InferType()(mod)
output = func_6434()
func_6435 = relay.Function([], output)
mutated_mod['func_6435'] = func_6435
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6175_call = mod.get_global_var('func_6175')
func_6177_call = mutated_mod.get_global_var('func_6177')
call_6458 = relay.TupleGetItem(func_6175_call(), 1)
call_6459 = relay.TupleGetItem(func_6177_call(), 1)
output = relay.Tuple([call_6458,])
output2 = relay.Tuple([call_6459,])
func_6460 = relay.Function([], output)
mod['func_6460'] = func_6460
mod = relay.transform.InferType()(mod)
mutated_mod['func_6460'] = func_6460
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6460_call = mutated_mod.get_global_var('func_6460')
call_6461 = func_6460_call()
output = call_6461
func_6462 = relay.Function([], output)
mutated_mod['func_6462'] = func_6462
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4734_call = mod.get_global_var('func_4734')
func_4736_call = mutated_mod.get_global_var('func_4736')
call_6528 = relay.TupleGetItem(func_4734_call(), 0)
call_6529 = relay.TupleGetItem(func_4736_call(), 0)
func_3040_call = mod.get_global_var('func_3040')
func_3042_call = mutated_mod.get_global_var('func_3042')
const_6538 = relay.const([[-5.191069,-9.136490,-2.021325,9.835804,-9.867958,1.036484,7.999671,-8.311015,-0.110594,5.647414,-6.280074,-9.148246,-6.696872,7.515748,4.709518,-7.785598,-6.028782,-6.025764,9.428771,9.330504,-8.331427,-8.373386,-1.800864,2.126996],[9.010622,9.840099,2.232600,-2.587765,-7.344287,-3.008377,-4.045146,7.191532,0.927617,1.170454,9.434414,5.548227,8.811515,6.961309,-5.951631,1.021533,-3.815350,8.492266,-0.113272,2.377766,2.855271,-5.950501,-1.675576,-0.916168],[-3.560691,-1.571199,-8.121686,4.299227,-7.517153,0.249239,1.243836,-0.671372,3.307718,9.404986,6.545688,-5.966837,-3.716184,-7.738050,-1.872795,5.384559,-1.412329,-7.479225,2.926283,8.683534,5.180749,-5.941967,0.911346,-0.249283],[-7.376745,-7.043453,-6.004282,-4.776698,-2.705177,-5.274401,0.316612,6.225697,0.654979,-0.281498,3.059150,-4.983187,-1.541831,0.358168,3.218131,-3.136671,-5.642819,-7.831580,-9.348112,1.217499,6.884324,5.479588,8.551115,5.895821],[7.789126,9.523970,1.802887,5.217091,-8.658022,6.953169,-5.674549,0.435351,-6.275988,6.667827,-4.641399,2.823497,-9.974390,-4.858235,1.769295,5.971001,2.796978,4.282537,-0.723825,-4.787349,-9.662039,0.135476,-2.843798,0.262980],[-4.869540,0.542143,0.228470,-1.740200,7.718173,-7.481202,-1.272437,4.821320,-9.552746,-1.114789,5.051582,-6.011716,-4.511316,-1.368884,-2.093795,-5.931807,8.704363,-7.539591,-8.225324,-4.409531,6.071228,7.416397,-9.426282,-6.971017],[9.037398,-4.048132,8.626845,-6.514032,-3.804156,-5.065230,-7.476234,5.868126,-7.306640,8.959873,-2.267087,0.822074,-5.158384,-5.663458,8.834496,8.864721,5.789353,-1.728168,-7.363466,8.218430,4.333582,-3.221773,-2.524679,3.834781],[7.837412,6.229611,5.120627,9.308158,0.640899,-0.308435,-6.319219,-9.908449,3.269740,8.303078,8.590721,-3.148917,-4.642160,6.135774,-7.124206,-8.682772,3.179169,-2.672684,-9.720365,-4.311257,4.893192,-0.864846,-9.335352,5.217268]], dtype = "float64")#candidate|6538|(8, 24)|const|float64
call_6537 = func_3040_call(relay.reshape(const_6538.astype('float64'), [6, 16, 2]))
call_6539 = func_3040_call(relay.reshape(const_6538.astype('float64'), [6, 16, 2]))
output = relay.Tuple([call_6528,call_6537,const_6538,])
output2 = relay.Tuple([call_6529,call_6539,const_6538,])
func_6540 = relay.Function([], output)
mod['func_6540'] = func_6540
mod = relay.transform.InferType()(mod)
output = func_6540()
func_6541 = relay.Function([], output)
mutated_mod['func_6541'] = func_6541
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5448_call = mod.get_global_var('func_5448')
func_5450_call = mutated_mod.get_global_var('func_5450')
call_6545 = func_5448_call()
call_6546 = func_5448_call()
uop_6548 = relay.asin(call_6545.astype('float64')) # shape=(5, 10, 13)
uop_6550 = relay.asin(call_6546.astype('float64')) # shape=(5, 10, 13)
output = relay.Tuple([uop_6548,])
output2 = relay.Tuple([uop_6550,])
func_6554 = relay.Function([], output)
mod['func_6554'] = func_6554
mod = relay.transform.InferType()(mod)
mutated_mod['func_6554'] = func_6554
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6554_call = mutated_mod.get_global_var('func_6554')
call_6555 = func_6554_call()
output = call_6555
func_6556 = relay.Function([], output)
mutated_mod['func_6556'] = func_6556
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6540_call = mod.get_global_var('func_6540')
func_6541_call = mutated_mod.get_global_var('func_6541')
call_6563 = relay.TupleGetItem(func_6540_call(), 0)
call_6564 = relay.TupleGetItem(func_6541_call(), 0)
func_4345_call = mod.get_global_var('func_4345')
func_4347_call = mutated_mod.get_global_var('func_4347')
var_6570 = relay.var("var_6570", dtype = "float32", shape = (196,))#candidate|6570|(196,)|var|float32
call_6569 = relay.TupleGetItem(func_4345_call(relay.reshape(var_6570.astype('float32'), [196,])), 1)
call_6571 = relay.TupleGetItem(func_4347_call(relay.reshape(var_6570.astype('float32'), [196,])), 1)
var_6575 = relay.var("var_6575", dtype = "bool", shape = (2, 12, 110))#candidate|6575|(2, 12, 110)|var|bool
bop_6576 = relay.power(call_6569.astype('float32'), relay.reshape(var_6575.astype('float32'), relay.shape_of(call_6569))) # shape=(2, 12, 110)
bop_6579 = relay.power(call_6571.astype('float32'), relay.reshape(var_6575.astype('float32'), relay.shape_of(call_6571))) # shape=(2, 12, 110)
output = relay.Tuple([call_6563,var_6570,bop_6576,])
output2 = relay.Tuple([call_6564,var_6570,bop_6579,])
func_6583 = relay.Function([var_6570,var_6575,], output)
mod['func_6583'] = func_6583
mod = relay.transform.InferType()(mod)
var_6584 = relay.var("var_6584", dtype = "float32", shape = (196,))#candidate|6584|(196,)|var|float32
var_6585 = relay.var("var_6585", dtype = "bool", shape = (2, 12, 110))#candidate|6585|(2, 12, 110)|var|bool
output = func_6583(var_6584,var_6585,)
func_6586 = relay.Function([var_6584,var_6585,], output)
mutated_mod['func_6586'] = func_6586
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5253_call = mod.get_global_var('func_5253')
func_5254_call = mutated_mod.get_global_var('func_5254')
call_6612 = func_5253_call()
call_6613 = func_5253_call()
output = relay.Tuple([call_6612,])
output2 = relay.Tuple([call_6613,])
func_6616 = relay.Function([], output)
mod['func_6616'] = func_6616
mod = relay.transform.InferType()(mod)
mutated_mod['func_6616'] = func_6616
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6616_call = mutated_mod.get_global_var('func_6616')
call_6617 = func_6616_call()
output = call_6617
func_6618 = relay.Function([], output)
mutated_mod['func_6618'] = func_6618
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5797_call = mod.get_global_var('func_5797')
func_5799_call = mutated_mod.get_global_var('func_5799')
call_6647 = relay.TupleGetItem(func_5797_call(), 0)
call_6648 = relay.TupleGetItem(func_5799_call(), 0)
output = call_6647
output2 = call_6648
func_6651 = relay.Function([], output)
mod['func_6651'] = func_6651
mod = relay.transform.InferType()(mod)
mutated_mod['func_6651'] = func_6651
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6651_call = mutated_mod.get_global_var('func_6651')
call_6652 = func_6651_call()
output = call_6652
func_6653 = relay.Function([], output)
mutated_mod['func_6653'] = func_6653
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4147_call = mod.get_global_var('func_4147')
func_4148_call = mutated_mod.get_global_var('func_4148')
call_6713 = func_4147_call()
call_6714 = func_4147_call()
var_6727 = relay.var("var_6727", dtype = "uint32", shape = (5, 10, 13))#candidate|6727|(5, 10, 13)|var|uint32
bop_6728 = relay.mod(call_6713.astype('float64'), relay.reshape(var_6727.astype('float64'), relay.shape_of(call_6713))) # shape=(5, 10, 13)
bop_6731 = relay.mod(call_6714.astype('float64'), relay.reshape(var_6727.astype('float64'), relay.shape_of(call_6714))) # shape=(5, 10, 13)
output = relay.Tuple([bop_6728,])
output2 = relay.Tuple([bop_6731,])
func_6746 = relay.Function([var_6727,], output)
mod['func_6746'] = func_6746
mod = relay.transform.InferType()(mod)
mutated_mod['func_6746'] = func_6746
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6747 = relay.var("var_6747", dtype = "uint32", shape = (5, 10, 13))#candidate|6747|(5, 10, 13)|var|uint32
func_6746_call = mutated_mod.get_global_var('func_6746')
call_6748 = func_6746_call(var_6747)
output = call_6748
func_6749 = relay.Function([var_6747], output)
mutated_mod['func_6749'] = func_6749
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6781 = relay.const([[[-10,7,-10,4,9,4,1,-7,7],[10,-9,-5,-2,-8,-8,-2,-9,-10],[-9,-1,-2,-2,-6,1,-1,1,9],[9,-2,4,9,6,-6,-8,-3,-3],[-1,10,-4,-1,4,-6,-5,-4,1],[8,-5,-9,3,4,-4,2,2,5],[3,-2,7,7,5,10,1,-8,-4],[-7,-4,-4,-8,8,-8,-5,-8,-5],[-6,-8,6,-9,-7,3,-5,10,-3],[-2,1,-10,-4,10,-3,8,9,-2],[-3,4,-9,-1,9,-8,4,-3,1],[-3,-10,8,10,-5,-9,6,8,-1],[-10,3,-2,4,-10,-2,-2,-7,-10]],[[8,-8,-10,9,-10,7,6,-2,9],[-8,1,-3,1,7,-10,3,-8,-2],[-10,4,10,1,-1,2,8,-4,-10],[-1,-2,10,-7,9,-6,2,2,7],[-7,7,-3,7,-9,-10,8,3,-10],[-4,-6,2,6,1,2,-1,8,7],[4,-3,-7,-5,4,6,9,-3,-5],[-10,-3,-8,-10,-1,6,2,-2,-5],[9,3,-6,-9,1,3,-1,6,5],[-6,-2,5,-7,-7,3,-9,2,6],[-2,-2,-1,8,9,3,-7,-8,9],[6,10,6,-7,-6,6,-4,8,-3],[2,-10,-5,-4,-3,-1,4,10,-3]],[[7,-1,7,-4,-8,-9,-1,2,4],[6,8,-10,4,6,-8,-8,7,8],[7,-4,-2,5,6,7,-5,-7,2],[1,1,-10,6,-6,7,6,-3,8],[5,-3,3,2,2,-2,-9,10,10],[-1,-8,-1,10,-1,-2,-10,-4,-10],[10,-6,3,7,-1,-2,-9,-9,-9],[-3,10,1,3,-8,2,-6,2,-7],[8,-7,-4,-9,-1,1,-1,-10,-10],[-2,2,-4,10,1,9,-6,-3,-7],[-1,2,-7,3,-9,8,2,6,1],[-10,-9,-2,-8,-7,-9,-8,3,2],[4,7,-6,7,-4,-4,3,4,7]],[[-10,4,6,6,-4,7,-6,-1,4],[-7,-9,-4,-3,-9,8,-3,-2,10],[10,5,2,2,-1,-2,-4,6,9],[8,-6,9,4,-4,10,-6,7,-6],[1,8,5,-7,-10,-4,-4,9,1],[3,1,-2,3,-1,9,-1,7,10],[-1,3,-1,-8,-9,-4,6,-6,7],[10,-5,-10,10,5,-3,1,4,-5],[1,2,4,-10,5,9,-3,-4,10],[5,7,9,-6,4,-6,-7,-6,-9],[-6,1,3,3,-9,-6,-3,10,10],[-2,2,8,-6,-5,5,3,2,-1],[5,1,-5,4,-8,9,-4,4,-6]],[[-3,7,-5,3,2,-3,10,-10,-4],[8,4,4,1,2,-5,-8,-3,10],[7,-7,9,-3,9,-8,10,-3,-9],[6,9,7,-8,-4,-10,-8,-8,-6],[-6,3,-4,-8,-6,-9,-10,-7,4],[-2,-1,-5,1,-5,-10,-5,2,2],[9,-10,-3,-2,-3,3,-6,-2,-5],[5,-2,-6,-3,-1,-7,3,-4,-2],[2,-1,6,-6,3,7,-7,-6,7],[3,1,7,6,-7,-2,7,-5,-3],[-4,-3,-9,7,-5,4,4,-1,1],[6,-7,8,-2,-7,3,7,-9,6],[-3,3,-7,9,6,6,-10,-7,-5]],[[-8,9,-3,-5,2,3,9,3,3],[9,-1,3,-4,-2,-2,3,-4,-5],[-5,-9,4,6,-5,5,9,1,-1],[-7,-9,-4,-6,1,1,8,6,-4],[-7,-4,-7,2,7,6,-10,-4,2],[10,-7,9,-8,-6,4,7,-10,8],[3,3,-5,-9,4,6,1,5,8],[6,2,-4,-3,10,3,-1,7,-6],[5,-7,-7,4,-10,6,4,6,5],[2,1,1,9,-10,-8,-1,10,-1],[-1,-6,3,-9,-5,2,-6,-10,-8],[1,-5,-6,-7,-7,4,-5,4,-8],[-3,-5,-3,-10,3,6,-5,1,-7]]], dtype = "int32")#candidate|6781|(6, 13, 9)|const|int32
var_6782 = relay.var("var_6782", dtype = "int32", shape = (6, 13, 9))#candidate|6782|(6, 13, 9)|var|int32
bop_6783 = relay.subtract(const_6781.astype('int32'), relay.reshape(var_6782.astype('int32'), relay.shape_of(const_6781))) # shape=(6, 13, 9)
uop_6786 = relay.tan(var_6782.astype('float32')) # shape=(6, 13, 9)
uop_6791 = relay.sigmoid(uop_6786.astype('float64')) # shape=(6, 13, 9)
func_430_call = mod.get_global_var('func_430')
func_433_call = mutated_mod.get_global_var('func_433')
const_6795 = relay.const(9.173558, dtype = "float64")#candidate|6795|()|const|float64
var_6796 = relay.var("var_6796", dtype = "int8", shape = (110, 1))#candidate|6796|(110, 1)|var|int8
call_6794 = relay.TupleGetItem(func_430_call(relay.reshape(const_6795.astype('float64'), []), relay.reshape(var_6796.astype('int8'), [22, 5]), ), 6)
call_6797 = relay.TupleGetItem(func_433_call(relay.reshape(const_6795.astype('float64'), []), relay.reshape(var_6796.astype('int8'), [22, 5]), ), 6)
bop_6801 = relay.left_shift(uop_6786.astype('uint32'), relay.reshape(var_6782.astype('uint32'), relay.shape_of(uop_6786))) # shape=(6, 13, 9)
uop_6811 = relay.cosh(uop_6791.astype('float32')) # shape=(6, 13, 9)
bop_6813 = relay.bitwise_or(uop_6811.astype('int8'), relay.reshape(uop_6791.astype('int8'), relay.shape_of(uop_6811))) # shape=(6, 13, 9)
func_4933_call = mod.get_global_var('func_4933')
func_4935_call = mutated_mod.get_global_var('func_4935')
call_6816 = func_4933_call()
call_6817 = func_4933_call()
output = relay.Tuple([bop_6783,call_6794,const_6795,var_6796,bop_6801,bop_6813,call_6816,])
output2 = relay.Tuple([bop_6783,call_6797,const_6795,var_6796,bop_6801,bop_6813,call_6817,])
func_6821 = relay.Function([var_6782,var_6796,], output)
mod['func_6821'] = func_6821
mod = relay.transform.InferType()(mod)
mutated_mod['func_6821'] = func_6821
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6821_call = mutated_mod.get_global_var('func_6821')
var_6823 = relay.var("var_6823", dtype = "int32", shape = (6, 13, 9))#candidate|6823|(6, 13, 9)|var|int32
var_6824 = relay.var("var_6824", dtype = "int8", shape = (110, 1))#candidate|6824|(110, 1)|var|int8
call_6822 = func_6821_call(var_6823,var_6824,)
output = call_6822
func_6825 = relay.Function([var_6823,var_6824,], output)
mutated_mod['func_6825'] = func_6825
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6853 = relay.var("var_6853", dtype = "float64", shape = (6, 16, 13))#candidate|6853|(6, 16, 13)|var|float64
uop_6854 = relay.cosh(var_6853.astype('float64')) # shape=(6, 16, 13)
output = relay.Tuple([uop_6854,])
output2 = relay.Tuple([uop_6854,])
F = relay.Function([var_6853,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_6853,], output2)
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
