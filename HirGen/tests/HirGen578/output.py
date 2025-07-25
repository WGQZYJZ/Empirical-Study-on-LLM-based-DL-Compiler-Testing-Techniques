import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
const_63 = relay.const(False, dtype = "bool")#candidate|63|()|const|bool
var_64 = relay.var("var_64", dtype = "bool", shape = (16, 1, 4))#candidate|64|(16, 1, 4)|var|bool
bop_65 = relay.logical_and(const_63.astype('bool'), var_64.astype('bool')) # shape=(16, 1, 4)
output = bop_65
output2 = bop_65
func_105 = relay.Function([var_64,], output)
mod['func_105'] = func_105
mod = relay.transform.InferType()(mod)
var_106 = relay.var("var_106", dtype = "bool", shape = (16, 1, 4))#candidate|106|(16, 1, 4)|var|bool
output = func_105(var_106)
func_107 = relay.Function([var_106], output)
mutated_mod['func_107'] = func_107
mutated_mod = relay.transform.InferType()(mutated_mod)
const_274 = relay.const([[[4,-1,-6,-2,1,1,-9],[3,9,-4,1,7,-7,-4],[5,-5,3,-10,2,-4,-2],[-8,-9,-10,5,3,7,-9],[5,7,9,8,7,-10,10],[3,10,2,2,-6,-7,-4],[10,-1,7,4,-10,-9,-10],[8,-5,-3,-2,-4,8,1],[10,-10,-9,5,8,1,4],[5,-2,-6,-3,4,4,8],[-8,7,-4,-10,7,8,-7]],[[-3,2,-8,10,1,-5,-7],[-1,-10,5,10,-6,4,-8],[-1,3,7,-10,8,-9,3],[2,-2,6,5,-1,1,-5],[-3,7,-7,7,-6,1,9],[2,5,-2,10,-10,9,10],[-9,9,8,-5,6,1,9],[5,3,9,-3,4,1,6],[5,4,-3,-5,6,-7,2],[-4,1,10,-9,1,-10,-5],[9,10,9,8,-4,-2,7]],[[-5,-9,-1,-2,-6,9,-3],[4,-9,1,-9,-3,2,-3],[2,-8,-6,-9,9,7,-2],[-7,-5,-5,6,-4,-6,-1],[8,5,-2,6,9,-9,7],[-8,-2,6,-3,-2,4,-3],[4,-9,10,2,-6,-1,6],[-7,-6,3,-9,-7,-7,3],[-6,-4,-10,5,-6,1,-7],[-10,2,5,-2,8,-7,-6],[-6,10,5,4,-6,5,-8]],[[-5,-3,-8,-2,-5,-3,-8],[9,-9,-2,7,-2,3,4],[9,6,-6,8,-6,-9,7],[-3,4,-10,7,1,-7,6],[10,-10,1,10,-7,-3,1],[1,4,4,5,1,3,-5],[5,-2,3,-4,10,-4,-2],[-7,7,-10,3,8,-7,-2],[-3,3,-10,2,9,-10,10],[3,8,-7,-1,7,1,3],[-6,-10,-4,6,-10,-9,-6]]], dtype = "uint16")#candidate|274|(4, 11, 7)|const|uint16
const_275 = relay.const([[[-5,-1,2,6,3,6,-5],[-1,1,5,2,-6,8,7],[-3,1,10,8,3,9,-10],[-3,1,-1,-1,-2,6,10],[-6,-9,5,-6,-1,6,10],[1,4,9,7,-6,8,9],[-7,-5,9,-9,3,1,2],[9,5,-6,-3,-2,4,-7],[7,-6,7,5,-5,-2,2],[2,1,7,-3,-2,-9,7],[4,8,1,4,-5,-6,5]],[[-9,-1,2,6,5,6,6],[-2,9,-8,-7,-8,9,-2],[-4,-4,6,7,7,-9,3],[-10,9,3,-9,-4,1,9],[-5,-6,-8,5,-6,-3,-6],[-5,-8,-9,10,6,2,-8],[-1,-3,-6,7,-1,-9,5],[-10,-4,1,4,2,1,-3],[-9,-7,6,9,1,7,10],[-9,-7,7,5,-5,7,1],[9,-10,5,-1,9,4,-9]],[[2,-8,-6,1,8,3,-5],[5,8,-1,2,-8,-8,4],[9,-4,3,-3,9,-6,1],[2,-10,3,-9,-8,4,-6],[5,6,-1,8,-4,-7,-6],[-2,2,3,1,10,4,-2],[6,-1,-6,-8,9,5,6],[8,2,-8,-2,-6,1,-2],[6,1,2,4,9,4,-5],[-3,10,-4,9,-7,-5,5],[-1,-10,3,-8,3,10,3]],[[2,-5,-10,4,7,7,8],[1,9,2,-10,1,9,-1],[8,7,3,-4,-6,8,-4],[1,7,5,3,-5,4,2],[-8,2,-8,-5,-10,-3,-9],[-2,-6,-7,5,8,1,3],[-9,-7,-10,4,-8,9,10],[-6,5,-2,-1,3,-10,3],[6,5,1,-4,-2,8,-9],[-10,9,8,2,-4,-8,8],[-9,9,7,3,-7,8,5]]], dtype = "uint16")#candidate|275|(4, 11, 7)|const|uint16
bop_276 = relay.bitwise_xor(const_274.astype('uint16'), relay.reshape(const_275.astype('uint16'), relay.shape_of(const_274))) # shape=(4, 11, 7)
func_105_call = mod.get_global_var('func_105')
func_107_call = mutated_mod.get_global_var('func_107')
const_281 = relay.const([[True],[False],[False],[False],[True],[True],[False],[False],[True],[False],[False],[False],[False],[False],[False],[False],[True],[False],[False],[False],[True],[True],[False],[False],[False],[False],[False],[True],[False],[True],[True],[True],[True],[True],[True],[False],[False],[True],[True],[False],[False],[True],[False],[False],[False],[False],[False],[True],[True],[True],[True],[False],[False],[True],[False],[False],[True],[True],[False],[True],[False],[True],[False],[False]], dtype = "bool")#candidate|281|(64, 1)|const|bool
call_280 = func_105_call(relay.reshape(const_281.astype('bool'), [16, 1, 4]))
call_282 = func_105_call(relay.reshape(const_281.astype('bool'), [16, 1, 4]))
output = relay.Tuple([bop_276,call_280,const_281,])
output2 = relay.Tuple([bop_276,call_282,const_281,])
func_295 = relay.Function([], output)
mod['func_295'] = func_295
mod = relay.transform.InferType()(mod)
mutated_mod['func_295'] = func_295
mutated_mod = relay.transform.InferType()(mutated_mod)
func_295_call = mutated_mod.get_global_var('func_295')
call_296 = func_295_call()
output = call_296
func_297 = relay.Function([], output)
mutated_mod['func_297'] = func_297
mutated_mod = relay.transform.InferType()(mutated_mod)
const_328 = relay.const([[[True,False],[True,False]]], dtype = "bool")#candidate|328|(1, 2, 2)|const|bool
var_329 = relay.var("var_329", dtype = "bool", shape = (12, 2, 2))#candidate|329|(12, 2, 2)|var|bool
bop_330 = relay.logical_and(const_328.astype('bool'), var_329.astype('bool')) # shape=(12, 2, 2)
output = bop_330
output2 = bop_330
func_348 = relay.Function([var_329,], output)
mod['func_348'] = func_348
mod = relay.transform.InferType()(mod)
mutated_mod['func_348'] = func_348
mutated_mod = relay.transform.InferType()(mutated_mod)
var_349 = relay.var("var_349", dtype = "bool", shape = (12, 2, 2))#candidate|349|(12, 2, 2)|var|bool
func_348_call = mutated_mod.get_global_var('func_348')
call_350 = func_348_call(var_349)
output = call_350
func_351 = relay.Function([var_349], output)
mutated_mod['func_351'] = func_351
mutated_mod = relay.transform.InferType()(mutated_mod)
func_295_call = mod.get_global_var('func_295')
func_297_call = mutated_mod.get_global_var('func_297')
call_379 = relay.TupleGetItem(func_295_call(), 2)
call_380 = relay.TupleGetItem(func_297_call(), 2)
const_381 = relay.const([[True,True,True,False,False,True],[True,False,False,False,True,False],[True,False,True,True,True,True],[False,False,False,False,False,True],[True,True,False,True,True,True],[True,True,True,False,True,True],[True,False,False,False,False,True],[False,True,True,True,False,False],[False,True,False,False,True,True],[False,False,False,False,True,False],[True,False,True,False,False,False],[False,False,False,False,False,False],[True,False,False,False,True,False],[True,True,True,True,True,False],[False,True,True,True,True,False],[True,True,True,False,True,True],[False,True,True,False,True,True],[False,False,True,False,True,False],[True,False,True,False,True,True],[True,False,False,False,True,False],[False,False,True,True,False,False],[True,False,False,False,False,True],[False,False,False,True,True,True],[False,False,True,True,False,False],[False,True,False,True,True,True],[True,False,True,False,True,True],[False,False,True,False,True,True],[False,True,False,False,False,True],[True,False,True,False,False,True],[False,False,True,True,True,False],[False,False,False,False,False,False],[True,True,False,True,True,True],[False,True,False,False,True,True],[True,False,True,False,False,True],[False,True,False,True,False,True],[True,False,False,False,False,False],[False,False,True,False,True,True],[False,True,False,False,False,False],[True,True,False,True,False,True],[False,False,False,False,True,False],[False,False,False,False,False,True],[False,False,True,False,True,False],[True,True,True,True,True,True],[True,True,True,False,False,True],[True,False,True,True,True,False],[True,True,False,True,True,True],[False,True,True,True,True,False],[True,False,True,True,False,True],[False,True,False,True,True,False],[False,False,False,True,True,True],[True,False,False,False,False,True],[True,False,True,False,False,False],[True,True,True,False,False,True],[True,True,False,True,False,False],[True,True,False,False,False,False],[True,False,False,False,False,False],[True,True,True,False,True,True],[True,False,False,False,True,True],[True,False,False,True,False,False],[True,True,True,False,True,False],[False,True,False,False,True,False],[True,False,True,False,True,False],[True,False,True,True,False,False],[False,True,False,False,False,False]], dtype = "bool")#candidate|381|(64, 6)|const|bool
bop_382 = relay.floor_mod(call_379.astype('float32'), const_381.astype('float32')) # shape=(64, 6)
bop_385 = relay.floor_mod(call_380.astype('float32'), const_381.astype('float32')) # shape=(64, 6)
output = bop_382
output2 = bop_385
func_391 = relay.Function([], output)
mod['func_391'] = func_391
mod = relay.transform.InferType()(mod)
output = func_391()
func_392 = relay.Function([], output)
mutated_mod['func_392'] = func_392
mutated_mod = relay.transform.InferType()(mutated_mod)
func_295_call = mod.get_global_var('func_295')
func_297_call = mutated_mod.get_global_var('func_297')
call_430 = relay.TupleGetItem(func_295_call(), 1)
call_431 = relay.TupleGetItem(func_297_call(), 1)
const_432 = relay.const([[[False,False,True,False],[True,True,False,True],[True,False,True,True],[True,False,False,True],[True,True,False,True],[False,True,True,True],[False,True,True,True],[True,False,False,True],[False,True,False,True],[False,False,False,True]],[[True,True,True,False],[False,True,True,True],[False,True,False,False],[False,True,True,True],[False,False,False,True],[False,False,True,False],[False,True,True,False],[True,False,False,False],[True,True,True,True],[False,False,False,False]],[[False,False,False,False],[True,False,True,True],[False,False,True,True],[False,False,True,False],[True,True,True,False],[True,True,True,False],[False,False,False,False],[False,False,False,False],[True,False,True,False],[False,False,False,True]],[[False,True,False,True],[True,True,True,False],[False,False,False,True],[True,True,False,True],[True,False,True,False],[False,True,False,True],[False,True,False,False],[False,False,True,False],[True,True,True,False],[True,True,False,True]],[[True,False,True,True],[False,True,False,True],[True,False,True,True],[True,False,True,True],[True,True,False,True],[True,True,False,False],[True,True,False,False],[False,False,True,False],[False,False,True,False],[True,True,False,False]],[[True,True,False,True],[True,True,False,True],[False,False,False,True],[False,False,True,True],[False,True,True,False],[True,False,False,True],[True,True,False,False],[True,False,True,False],[True,True,True,True],[False,False,False,False]],[[False,False,True,False],[True,False,True,True],[True,False,True,False],[True,False,True,False],[True,True,False,False],[True,True,True,True],[False,False,False,False],[False,False,False,True],[False,True,True,True],[True,True,False,False]],[[True,False,False,False],[False,False,False,True],[True,True,False,True],[False,True,False,True],[True,False,True,False],[False,False,True,False],[True,False,False,True],[True,False,True,True],[False,False,True,False],[False,False,False,True]],[[True,False,False,True],[True,False,False,False],[False,False,False,False],[False,True,True,True],[False,True,False,True],[True,False,False,False],[False,False,False,False],[False,False,True,True],[False,False,False,True],[False,True,False,True]],[[True,False,True,True],[False,False,False,False],[True,True,True,True],[True,False,True,True],[False,True,True,False],[False,False,True,False],[False,True,False,True],[False,False,False,True],[False,True,False,False],[False,True,False,True]],[[False,False,False,True],[False,True,False,False],[True,True,False,True],[True,True,True,False],[False,True,True,True],[True,True,False,False],[False,True,False,False],[False,True,False,False],[True,False,True,True],[False,True,True,True]],[[False,True,False,True],[False,True,True,False],[True,False,True,False],[True,False,False,False],[True,True,False,True],[False,False,True,True],[True,False,False,True],[True,True,False,True],[False,False,False,False],[True,False,False,False]],[[False,False,True,False],[False,True,False,True],[False,False,False,False],[True,True,True,False],[True,True,True,False],[False,True,True,False],[True,True,False,False],[True,True,True,False],[True,False,False,True],[True,False,False,False]],[[False,False,False,True],[True,False,True,False],[True,False,False,False],[True,True,False,False],[False,True,True,False],[False,False,False,True],[False,False,False,True],[False,False,True,False],[False,False,False,True],[False,True,True,True]],[[False,True,True,True],[False,False,False,False],[True,True,False,True],[True,False,False,True],[False,False,False,False],[False,False,True,False],[False,True,True,False],[False,False,True,False],[True,True,False,True],[True,False,True,False]],[[True,False,True,False],[False,True,True,True],[True,True,True,True],[True,False,True,True],[True,False,True,False],[False,True,False,True],[False,False,False,True],[False,True,True,True],[True,False,True,False],[True,False,True,False]]], dtype = "bool")#candidate|432|(16, 10, 4)|const|bool
bop_433 = relay.divide(call_430.astype('float64'), const_432.astype('float64')) # shape=(16, 10, 4)
bop_436 = relay.divide(call_431.astype('float64'), const_432.astype('float64')) # shape=(16, 10, 4)
output = bop_433
output2 = bop_436
func_439 = relay.Function([], output)
mod['func_439'] = func_439
mod = relay.transform.InferType()(mod)
output = func_439()
func_440 = relay.Function([], output)
mutated_mod['func_440'] = func_440
mutated_mod = relay.transform.InferType()(mutated_mod)
var_453 = relay.var("var_453", dtype = "float64", shape = (11, 11, 1))#candidate|453|(11, 11, 1)|var|float64
uop_454 = relay.log2(var_453.astype('float64')) # shape=(11, 11, 1)
output = relay.Tuple([uop_454,])
output2 = relay.Tuple([uop_454,])
func_467 = relay.Function([var_453,], output)
mod['func_467'] = func_467
mod = relay.transform.InferType()(mod)
mutated_mod['func_467'] = func_467
mutated_mod = relay.transform.InferType()(mutated_mod)
var_468 = relay.var("var_468", dtype = "float64", shape = (11, 11, 1))#candidate|468|(11, 11, 1)|var|float64
func_467_call = mutated_mod.get_global_var('func_467')
call_469 = func_467_call(var_468)
output = call_469
func_470 = relay.Function([var_468], output)
mutated_mod['func_470'] = func_470
mutated_mod = relay.transform.InferType()(mutated_mod)
func_439_call = mod.get_global_var('func_439')
func_440_call = mutated_mod.get_global_var('func_440')
call_497 = func_439_call()
call_498 = func_439_call()
func_348_call = mod.get_global_var('func_348')
func_351_call = mutated_mod.get_global_var('func_351')
const_551 = relay.const([False,True,True,True,True,False,True,True,True,False,True,False,True,True,False,False,False,False,False,False,False,False,False,True,True,True,True,False,True,True,True,False,False,False,True,False,False,False,True,True,False,False,True,True,True,True,True,False], dtype = "bool")#candidate|551|(48,)|const|bool
call_550 = func_348_call(relay.reshape(const_551.astype('bool'), [12, 2, 2]))
call_552 = func_348_call(relay.reshape(const_551.astype('bool'), [12, 2, 2]))
func_391_call = mod.get_global_var('func_391')
func_392_call = mutated_mod.get_global_var('func_392')
call_558 = func_391_call()
call_559 = func_391_call()
var_571 = relay.var("var_571", dtype = "float32", shape = (64, 6))#candidate|571|(64, 6)|var|float32
bop_572 = relay.multiply(call_558.astype('uint64'), relay.reshape(var_571.astype('uint64'), relay.shape_of(call_558))) # shape=(64, 6)
bop_575 = relay.multiply(call_559.astype('uint64'), relay.reshape(var_571.astype('uint64'), relay.shape_of(call_559))) # shape=(64, 6)
output = relay.Tuple([call_497,call_550,const_551,bop_572,])
output2 = relay.Tuple([call_498,call_552,const_551,bop_575,])
func_578 = relay.Function([var_571,], output)
mod['func_578'] = func_578
mod = relay.transform.InferType()(mod)
mutated_mod['func_578'] = func_578
mutated_mod = relay.transform.InferType()(mutated_mod)
var_579 = relay.var("var_579", dtype = "float32", shape = (64, 6))#candidate|579|(64, 6)|var|float32
func_578_call = mutated_mod.get_global_var('func_578')
call_580 = func_578_call(var_579)
output = call_580
func_581 = relay.Function([var_579], output)
mutated_mod['func_581'] = func_581
mutated_mod = relay.transform.InferType()(mutated_mod)
func_439_call = mod.get_global_var('func_439')
func_440_call = mutated_mod.get_global_var('func_440')
call_621 = func_439_call()
call_622 = func_439_call()
var_627 = relay.var("var_627", dtype = "float64", shape = (16, 10, 4))#candidate|627|(16, 10, 4)|var|float64
bop_628 = relay.minimum(call_621.astype('uint64'), relay.reshape(var_627.astype('uint64'), relay.shape_of(call_621))) # shape=(16, 10, 4)
bop_631 = relay.minimum(call_622.astype('uint64'), relay.reshape(var_627.astype('uint64'), relay.shape_of(call_622))) # shape=(16, 10, 4)
func_467_call = mod.get_global_var('func_467')
func_470_call = mutated_mod.get_global_var('func_470')
var_633 = relay.var("var_633", dtype = "float64", shape = (11, 11))#candidate|633|(11, 11)|var|float64
call_632 = relay.TupleGetItem(func_467_call(relay.reshape(var_633.astype('float64'), [11, 11, 1])), 0)
call_634 = relay.TupleGetItem(func_470_call(relay.reshape(var_633.astype('float64'), [11, 11, 1])), 0)
uop_641 = relay.erf(bop_628.astype('float64')) # shape=(16, 10, 4)
uop_643 = relay.erf(bop_631.astype('float64')) # shape=(16, 10, 4)
func_467_call = mod.get_global_var('func_467')
func_470_call = mutated_mod.get_global_var('func_470')
call_646 = relay.TupleGetItem(func_467_call(relay.reshape(call_632.astype('float64'), [11, 11, 1])), 0)
call_647 = relay.TupleGetItem(func_470_call(relay.reshape(call_632.astype('float64'), [11, 11, 1])), 0)
func_295_call = mod.get_global_var('func_295')
func_297_call = mutated_mod.get_global_var('func_297')
call_648 = relay.TupleGetItem(func_295_call(), 1)
call_649 = relay.TupleGetItem(func_297_call(), 1)
output = relay.Tuple([call_632,var_633,uop_641,call_646,call_648,])
output2 = relay.Tuple([call_634,var_633,uop_643,call_647,call_649,])
func_655 = relay.Function([var_627,var_633,], output)
mod['func_655'] = func_655
mod = relay.transform.InferType()(mod)
var_656 = relay.var("var_656", dtype = "float64", shape = (16, 10, 4))#candidate|656|(16, 10, 4)|var|float64
var_657 = relay.var("var_657", dtype = "float64", shape = (11, 11))#candidate|657|(11, 11)|var|float64
output = func_655(var_656,var_657,)
func_658 = relay.Function([var_656,var_657,], output)
mutated_mod['func_658'] = func_658
mutated_mod = relay.transform.InferType()(mutated_mod)
var_687 = relay.var("var_687", dtype = "float64", shape = (11, 10, 6))#candidate|687|(11, 10, 6)|var|float64
const_688 = relay.const([[[-4.906503,1.004129,2.442353,9.396285,7.236846,-3.462452],[-6.101543,-0.833996,5.914315,-7.061030,-2.912824,-3.822979],[9.527608,-3.726449,8.980019,-1.787765,-9.220442,-8.620194],[-2.421049,9.067414,-9.322794,-2.744671,-2.565213,2.229388],[-5.054641,-6.044394,5.730639,0.849396,7.234547,-0.660163],[-7.473412,-4.463018,-7.580264,-4.748833,-2.643133,-4.739772],[3.481120,6.296257,-6.158908,2.962266,6.661993,2.107368],[2.714183,8.594317,9.768298,8.523179,-6.959228,-8.639624],[-5.578000,6.756445,-4.734124,-7.263461,-2.927498,3.104064],[-7.902110,7.625136,-8.429243,6.467321,-0.844687,-3.498334]],[[-9.817709,5.507464,1.017118,5.632780,-5.590254,7.661062],[8.999847,-9.576798,1.276934,-8.163360,-8.370408,0.714721],[-1.483198,-7.117207,2.621568,-7.162183,4.677224,1.948895],[8.603942,-5.206085,6.473726,-9.889051,0.235332,2.689869],[8.289342,0.429649,6.909768,-4.707545,9.985635,-1.115800],[-6.856017,-2.902879,-8.765948,-5.665446,-0.257445,0.385129],[-8.282278,-5.876446,-3.296394,0.389519,4.930365,-3.602193],[4.912675,0.153804,5.842147,-0.670398,-2.227745,8.568862],[-2.273213,4.943821,1.939262,-5.900802,-6.940661,3.550893],[-3.806984,-5.007371,2.118702,4.217423,-7.228290,9.545242]],[[-7.903290,9.771672,-9.513162,-9.486746,-7.876427,-0.859245],[-5.997916,-4.153720,1.718795,-5.672983,-5.048540,-5.774594],[0.379389,-1.464124,-5.151290,3.834971,1.534380,5.541618],[-6.012835,-5.202336,7.961351,-3.868435,-2.046086,2.823341],[-6.547882,8.512332,-4.081913,3.142855,2.971890,0.407600],[5.080888,1.836987,2.851357,8.519112,-5.893834,5.280741],[-6.899706,1.086632,-6.013397,-7.375002,-5.977384,0.308085],[0.267863,-7.104340,-7.977754,-2.316902,6.322983,3.466851],[0.143418,-8.239520,-3.052609,7.307977,9.694478,3.265313],[6.832810,-2.408858,-2.535671,5.226411,-1.221562,-9.305472]],[[1.531644,6.358886,-4.642851,-2.979068,2.630305,9.118853],[-0.869460,-3.280743,-4.253594,3.077014,2.201097,7.820583],[7.606370,-8.696916,0.541006,-8.759943,4.951678,2.356951],[-8.770913,4.887138,-4.101648,-5.063329,-9.228559,-0.718428],[-9.095810,-9.317607,4.520753,1.684421,-2.768818,3.910719],[7.174790,6.622654,9.034778,-6.861135,-8.384822,1.299722],[2.282905,6.455249,-0.114241,-3.957016,6.192203,-3.245874],[-1.972429,0.933167,2.096110,-9.820579,-2.181004,-2.884528],[-7.566008,-2.572645,-4.326329,3.778931,5.320960,5.944686],[-7.186388,-4.084109,7.836418,2.172471,8.846459,-3.058501]],[[1.412468,8.726803,-2.769107,3.585820,-2.292765,4.621735],[9.574236,-9.872146,8.986248,-7.257835,1.957700,3.467991],[0.600807,0.982226,1.735175,-9.884830,-6.583603,8.170686],[4.732157,-2.128494,-0.745505,-3.148330,-7.652855,-1.456926],[6.183440,-4.610850,1.586973,2.234882,-2.377102,8.432823],[-4.484736,-4.529825,4.398226,-1.833396,-1.348588,3.278542],[-1.285418,-2.833873,-0.086119,9.197141,9.053440,6.649219],[8.075125,8.035646,2.061989,-5.264295,-1.929388,-7.631356],[-1.607259,-0.996994,8.413075,6.595279,-7.474471,4.756546],[-5.045779,-7.243517,-9.355166,-8.735300,-1.053676,3.935809]],[[8.499938,5.599200,-7.229419,9.133610,-4.606519,3.427044],[2.985148,-7.645263,-9.321463,3.732117,-3.506843,-0.931928],[4.716453,-7.355942,-7.108367,0.068319,5.320259,-1.124025],[-1.108414,-5.548583,6.003015,0.847430,-0.064210,-9.492778],[0.331150,5.292309,3.737320,-6.297863,7.202829,-0.828653],[-5.474286,9.815461,6.783523,3.441415,8.256631,-1.009349],[3.320897,-1.960474,7.921332,-6.076488,-4.306674,-1.510543],[2.474174,-0.744114,-0.155466,-9.510859,-7.064702,-6.546602],[2.984101,7.730377,-3.909224,-0.471117,7.979333,3.896067],[7.882135,2.547346,-7.247861,-9.749265,-2.050028,-6.521525]],[[8.132852,1.411139,-8.134677,1.939624,4.148947,-3.442427],[3.902040,7.910600,7.192574,7.320077,-6.438689,-8.809561],[3.286314,-8.455405,3.228399,-8.161320,-3.975065,-4.733144],[9.741497,-7.355904,0.629937,-3.151574,3.430453,9.421768],[7.526986,-3.556207,-0.623567,-0.842032,9.364753,5.737152],[0.034744,0.548880,-8.480455,-3.883008,-5.090527,-0.793306],[8.457927,-3.735013,8.239936,-0.378045,-7.951004,-2.626753],[3.534988,-2.858615,-3.165287,-2.011151,2.923233,2.622433],[3.068740,-6.709123,-5.875407,4.962174,0.171023,8.821672],[-7.075289,2.725486,-4.638375,8.150742,-2.737623,-9.029756]],[[5.699371,-5.428297,-1.438096,-5.632536,9.384926,1.958059],[-0.080951,-9.361302,-9.410269,-0.548489,7.975756,-1.640386],[1.129840,5.385925,8.388680,-1.997725,-2.895349,-2.954133],[-8.339488,0.413557,8.820835,-2.361118,1.183093,0.845284],[-9.573519,-4.558740,-1.686211,9.760336,-6.635294,8.187496],[-1.829126,1.332023,1.233153,4.804198,-1.228584,5.240315],[-6.445477,9.470571,-6.202313,0.876839,-4.426437,-8.955303],[-0.726462,6.848402,2.123040,5.818314,-1.151697,-8.928367],[-0.621148,-7.691393,-2.564687,-2.486081,6.563338,1.406520],[-1.287369,-2.816575,-6.436193,1.229897,-7.574754,-8.140903]],[[-6.645387,6.505622,-1.271270,-4.567480,8.758276,2.780135],[-2.196970,-0.085020,-8.124662,-8.625452,1.130228,5.982512],[1.811416,-3.207793,1.719753,2.699838,-9.397782,7.748105],[9.068338,1.325033,-3.593830,-8.183617,-9.949990,-6.433395],[-7.532389,-1.024652,1.773715,-3.850379,-4.204493,-2.910132],[1.683657,7.569645,-7.950722,-3.675435,-4.307460,-7.363471],[-3.037631,-7.808701,-5.999682,6.994843,1.901884,-6.485275],[-1.265185,7.702006,1.399082,-3.734200,-4.777604,3.364596],[-0.879114,-3.797619,6.877347,2.385775,2.580389,4.381424],[-6.626974,6.631685,-9.908379,-7.234796,-7.846952,4.431452]],[[9.149200,-2.934333,-6.702040,-9.133125,8.093787,2.322852],[-0.339174,-8.534352,-1.248245,5.316874,5.993377,-2.305743],[-7.023209,-8.758365,3.540507,-8.862806,8.233256,-9.757780],[-3.494403,3.378933,2.114148,4.581101,3.039633,9.890916],[8.973506,7.993154,4.472679,-8.342139,-5.285394,-4.369230],[-5.365521,6.973445,5.711360,8.366559,-1.249946,0.463173],[-6.149088,7.863054,2.037468,2.794537,4.156676,3.179213],[9.462227,-4.107350,-0.720484,1.594430,-9.427477,-7.041027],[-2.221542,0.524910,-5.401769,-6.888879,1.892469,7.017576],[-1.685678,5.897903,6.039671,2.567935,-6.022175,-7.769789]],[[-4.117074,-8.221732,-5.443920,0.899097,-0.312274,-6.617298],[4.530374,0.939030,-6.057692,5.838294,-8.157522,3.778565],[4.200399,-5.427418,-3.421634,-5.792047,-2.944410,8.872435],[-7.398891,3.622995,-6.701403,8.249498,-3.704785,-5.054259],[9.201474,4.457647,5.393492,5.337197,4.977833,-4.161631],[5.133724,6.621163,6.558195,-2.522617,9.081571,4.570380],[6.016708,1.261747,1.018506,8.371476,-8.277884,-6.764054],[3.938053,-4.042651,3.575256,-8.220035,-2.443253,-1.564881],[1.337255,2.831908,-6.964804,-5.923686,8.476182,7.085800],[3.580689,-9.783233,-2.072969,8.224733,-9.214245,-0.649679]]], dtype = "float64")#candidate|688|(11, 10, 6)|const|float64
bop_689 = relay.floor_divide(var_687.astype('float64'), relay.reshape(const_688.astype('float64'), relay.shape_of(var_687))) # shape=(11, 10, 6)
func_655_call = mod.get_global_var('func_655')
func_658_call = mutated_mod.get_global_var('func_658')
const_702 = relay.const([7.886337,-3.951548,0.206266,-8.866799,-4.171336,3.248701,-2.929666,-6.748993,-3.975136,7.366831,-9.180050,-8.058215,-7.536233,9.033910,4.865001,-9.221430,2.676392,-0.769190,4.202676,-3.337039,8.721325,-5.869048,-1.689663,1.924508,6.046039,-0.330584,1.554471,-0.793087,9.101565,-3.482655,9.473602,6.884706,5.807076,5.287247,6.692186,9.136233,9.062830,-5.626381,-2.836193,-6.839244,-2.890654,-9.366398,9.272344,4.385382,-6.430929,-2.902236,-3.841215,-1.815134,8.356891,-1.224689,9.177015,7.357021,3.574582,-9.554400,-9.435164,9.424599,6.596170,-8.690345,4.348747,9.751231,2.468628,3.614670,-7.570057,-3.962350,1.631531,-7.456423,-8.266950,2.517514,9.856608,4.686733,4.588046,6.033044,-7.500634,1.280262,8.191804,8.206249,-1.261458,2.335477,-9.779667,-1.418879,-5.676473,-3.635323,6.361137,4.289859,1.526097,-8.064845,3.928178,3.767097,7.402164,9.231567,-7.690463,-2.599459,5.091327,0.686208,1.074573,4.882102,-6.918468,-7.746910,-3.433821,-3.310444,-8.668045,-4.443636,-0.707820,-3.294345,-9.911141,6.851039,-2.922738,-8.227421,7.321381,-9.938590,5.399952,-4.177664,4.629921,4.242502,-5.587671,-5.730994,-6.213517,3.548991,-3.571905,4.839894,4.981978,6.674622,-3.305195,-2.963534,6.374030,-5.089733,-7.271330,-5.420898,7.207228,7.082834,-1.168988,-7.717190,-1.317773,3.326684,0.120736,-0.275435,0.015645,5.080225,8.867603,3.197667,-7.535796,0.058757,9.603274,-8.868466,-2.368455,-0.907979,6.324816,9.004111,-8.807730,9.237463,0.693912,0.929158,8.095585,-9.942010,-5.837216,-4.806096,5.125809,0.426690,8.121766,3.829865,-2.153507,-8.440002,2.944916,3.380712,5.526437,1.765891,-5.154636,9.632945,0.744115,-1.586858,-4.240805,-9.694803,6.240969,-2.317021,-5.706438,-2.272860,3.583840,-7.186082,-3.366887,3.948146,-2.333678,9.811672,0.829989,0.516466,-9.367433,-8.643797,-6.427561,1.964932,-4.519278,-8.199892,3.302630,0.699429,-3.891105,1.860201,-0.853331,-7.846068,-4.831965,9.969061,-3.225994,-6.909704,1.872174,5.388351,-2.520659,0.864775,-1.968875,1.140227,-7.931743,9.419480,-7.539278,8.949749,4.915109,-7.294766,9.152544,4.791092,-0.777318,3.768599,-4.279077,6.180494,8.916516,0.388713,-6.651990,5.908468,-2.644303,6.071876,-8.099479,5.782716,-4.025978,6.048604,9.659175,-0.184138,-6.571915,3.109856,-3.166351,6.808503,8.012600,-9.715330,6.307513,-6.102186,-6.639646,9.240458,8.566157,-8.465240,-4.632906,5.185905,-5.360391,8.821907,9.296471,2.225136,3.934673,7.242713,3.492469,-0.725055,-3.873222,-5.837229,1.763487,6.546452,-2.978294,-0.128595,0.439060,4.318786,2.546488,-2.973370,2.192551,0.062716,7.037472,-1.393279,-0.834103,0.052265,7.739917,4.713261,1.551693,3.141538,-8.794049,-6.605160,-6.908318,2.451085,-8.081057,-0.174079,8.547344,-9.464114,2.023822,4.533182,-5.487690,-6.478293,4.714998,-8.898498,-6.758933,-8.866478,1.470317,-2.265419,-5.010429,-4.697996,5.473020,6.889613,-4.043543,5.755846,-1.318703,3.556871,-2.340879,-9.009122,2.673210,-0.281836,1.895096,-5.636540,-9.738489,-3.905457,-0.256224,0.406323,2.942017,-3.262979,2.506505,0.124581,-4.194315,-7.982422,-6.391316,-4.456410,7.590261,9.498193,-4.677008,8.856763,-2.771215,1.391484,-0.275587,6.456025,8.494014,9.729229,7.676412,-5.022565,2.120896,-1.175888,-7.804918,3.489830,-0.128820,-6.454702,-4.636850,4.061617,3.685648,6.768708,2.143229,8.732459,-2.322215,8.876146,-0.328467,-1.759614,-9.470352,6.892588,8.989901,-3.205932,-0.664616,-5.882042,3.021669,0.139280,4.334711,-7.708526,6.312881,8.808961,9.462771,-2.295961,0.272561,9.978208,6.253443,-2.501589,-6.283765,-5.132207,6.792948,9.126996,-2.971221,5.098750,-7.352342,2.154299,5.342251,6.485952,2.616556,-1.739164,-2.566649,9.540586,4.712285,1.595532,-1.375366,-8.946851,-0.524272,-5.417389,-5.832627,-8.544119,-8.186548,4.418841,5.056046,-5.226057,-8.038820,5.123621,-1.496037,-6.603882,-4.024793,5.719494,-6.164503,-2.743286,-0.884398,5.551732,-8.046274,1.221826,2.003822,-3.334483,6.666640,-0.947192,-3.378331,0.515609,-3.722902,-1.518608,5.720038,7.449177,1.485810,-1.328375,2.667789,-3.722876,-9.949973,-5.516899,-4.981643,-8.454243,4.018303,6.919406,-1.834876,-7.086904,7.066098,5.681259,9.853975,-9.449375,-1.693594,-3.380214,-7.045432,5.704391,-5.927898,3.516305,-6.413620,-9.644127,-3.211368,6.575408,-9.961727,9.631777,-2.759650,-1.875907,1.759220,-5.268155,-8.094070,4.727236,-1.864933,1.988864,-9.166213,9.076992,-3.913792,-3.861543,-8.206695,9.087329,-4.261904,-8.254922,8.933183,-6.013989,8.022305,-0.549999,7.961568,-5.188490,-5.631484,-8.273832,-7.009430,6.920197,7.636820,6.458945,-6.464641,8.566138,9.295935,2.509756,-0.199789,-0.236649,7.965815,8.752299,-5.088369,-0.381915,6.766721,-8.312253,-8.564938,-5.970615,2.925451,0.940261,-2.316023,-5.957335,-7.552537,-8.407798,9.680444,-0.465035,8.710223,0.168784,-9.501230,-7.430634,-9.784220,8.234389,0.086865,3.076940,-0.273096,-8.884230,5.560735,-5.820151,-9.556215,-1.173543,7.420131,-3.349309,0.540559,4.191392,8.771195,4.909505,-4.062547,3.885170,8.399041,-4.044238,7.173764,-5.574103,-7.899847,4.744143,-5.011668,-6.566380,-3.126522,-3.886837,6.837585,2.850631,-0.201865,-5.539817,-9.459609,-2.385064,-7.297381,3.904001,3.585725,-1.346960,-9.450967,-8.195382,-7.795182,2.168509,-8.223668,-5.678057,1.097550,-1.219672,-3.668358,-2.593943,-2.195810,-0.122353,6.104542,4.886301,-6.059304,-0.898114,1.076872,4.494620,-1.967173,-2.776458,-2.034855,-5.982380,8.078625,8.332775,3.744561,-6.119686,-2.377530,6.108553,-7.089557,-2.677111,-7.288097,7.647325,-5.258699,7.705889,5.321029,1.311190,-7.705641,9.063116,-1.669349,-6.219471,-7.786541,-3.485670,6.591693,0.851819,-0.883864,-0.070387,-5.634042,-0.463764,-7.662510,2.636030,5.520502,-2.014091,-8.627311,6.814221,-9.060994,9.791052,-9.481008,-8.656219,5.204698,0.489802,2.547427,-2.071793,-7.292704,-1.061838,1.495639,-7.727565,-1.246670,-6.154848,1.527502,-3.474862,3.303962,-0.626197,4.291109,-3.832331,-5.222570,-5.841397,6.044296,-8.301380,1.368744,7.708421,-3.331921,5.928613,-4.515719,-3.400857,-9.769996,6.205500,-8.709476,1.264805,-3.859815,-9.776570,-1.150499,4.630210,6.555869,8.399217,-5.821178,0.511131,-4.219800,-6.182561,7.874907,-0.275091,2.944971,6.753103,-7.631837,9.387676,-2.733201,7.332767,-8.299379,8.950808,-7.043298,-7.271512], dtype = "float64")#candidate|702|(640,)|const|float64
const_703 = relay.const([[-6.636804,2.278450,7.513552,-5.317758,-3.068941,-1.251981,-9.160490,4.738848,4.180520,-3.638302,4.128878,5.585904,7.293968,-3.523467,-2.856093,-6.274047,-7.907241,-3.504975,-3.891936,-3.414946,4.175838,-5.241851,-3.036714,9.198055,3.267976,-3.060159,0.982456,-0.349645,-3.593099,-5.443604,-6.477916,3.060949,-6.879536,-3.561177,-6.489001,2.613519,7.382919,7.426070,3.976450,7.527071,-7.283049,7.038490,4.084821,5.946315,-7.921322,5.466811,-3.980364,1.039438,-6.067027,-3.431592,1.176970,-7.608891,3.289492,-9.101124,-9.143034,-3.334468,7.880231,-7.476104,4.098884,-5.421985,4.709471,-8.837077,-8.490772,-8.943558,-2.534155,1.812495,-1.047830,-7.920963,-0.966883,-3.243435,4.968474,9.546110,6.875811,1.491769,0.157893,-8.905897,0.252618,0.965182,0.046708,-9.410600,-8.451702,4.608095,2.982153,-2.761028,-1.486556,7.083171,5.836746,-7.987040,-1.702144,-0.419430,0.842148,4.758826,2.572104,-8.971842,-4.004645,-0.904769,-7.164992,-6.477312,-1.016098,3.473531,7.673595,-4.002350,-4.257471,2.203638,-7.444676,-9.877705,6.271934,2.026061,-6.032875,9.793935,-3.970158,3.292803,6.663671,3.553639,2.433644,-3.978907,7.860302,9.887585,2.823201,-0.040322,-6.717461]], dtype = "float64")#candidate|703|(1, 121)|const|float64
call_701 = relay.TupleGetItem(func_655_call(relay.reshape(const_702.astype('float64'), [16, 10, 4]), relay.reshape(const_703.astype('float64'), [11, 11]), ), 2)
call_704 = relay.TupleGetItem(func_658_call(relay.reshape(const_702.astype('float64'), [16, 10, 4]), relay.reshape(const_703.astype('float64'), [11, 11]), ), 2)
output = relay.Tuple([bop_689,call_701,const_702,const_703,])
output2 = relay.Tuple([bop_689,call_704,const_702,const_703,])
func_706 = relay.Function([var_687,], output)
mod['func_706'] = func_706
mod = relay.transform.InferType()(mod)
var_707 = relay.var("var_707", dtype = "float64", shape = (11, 10, 6))#candidate|707|(11, 10, 6)|var|float64
output = func_706(var_707)
func_708 = relay.Function([var_707], output)
mutated_mod['func_708'] = func_708
mutated_mod = relay.transform.InferType()(mutated_mod)
var_803 = relay.var("var_803", dtype = "float64", shape = (6, 4, 1))#candidate|803|(6, 4, 1)|var|float64
uop_804 = relay.atanh(var_803.astype('float64')) # shape=(6, 4, 1)
const_853 = relay.const([[[0.605195,2.269799,8.557070,4.041179,-5.852776,-7.953566,-3.988192,-8.076220,0.439970,9.782154,6.569835,-7.801438,8.215755,9.472042,4.255718],[-8.115370,1.414332,4.078208,9.054551,4.229682,-1.526289,4.372226,-9.166090,2.291759,-8.110059,-1.954768,0.976467,6.745315,-8.774892,1.883515],[1.254953,-2.046775,-4.294945,-1.286536,-7.749293,0.602861,6.257853,9.997837,-3.448443,1.825262,-7.972750,1.993974,4.451171,-6.542522,0.609676],[7.674602,1.931342,3.694618,2.967734,-5.941053,-8.437164,2.528363,-4.190288,1.715896,3.080780,0.053246,0.392123,6.074869,-8.981135,-8.651517]],[[3.800136,-7.055586,9.030736,-5.949842,7.081251,-1.376825,-8.719233,-7.638710,5.035845,-7.994120,-2.238193,-6.969222,-1.350715,-4.396332,5.803126],[-3.127603,-0.456238,4.851726,3.527915,9.665692,-9.880357,-4.751571,7.525484,0.621346,-5.932251,1.401332,-2.232343,-2.686366,9.866071,6.750487],[1.616008,8.915629,-4.868484,3.571029,8.460764,1.772491,1.756427,-3.603676,-7.500066,4.093608,2.991300,2.621028,-2.308056,-8.070079,7.596572],[-2.113400,-1.584989,-2.514287,-1.351183,-7.673638,-9.961888,-8.903577,0.568869,-3.390122,-2.569525,-6.098280,-9.460589,2.131511,-8.441547,-3.364198]],[[5.521758,-1.739780,8.735397,3.709310,6.284254,6.452543,1.912646,4.542665,-6.451521,-9.639402,4.413188,9.319723,-9.829196,-2.506416,-5.369792],[-4.701480,8.194747,6.941862,-3.069253,-6.194681,-0.089597,4.062932,1.148272,-6.927577,9.381208,5.708301,-8.207423,-1.615554,5.662626,0.655985],[-4.717677,-9.544967,-6.142168,-6.578034,-3.736005,-1.471307,-8.734338,-6.517460,-1.087179,1.337627,5.746987,-4.111278,2.041490,-0.905395,8.774037],[0.038206,-9.588959,8.185523,5.507178,6.830649,9.305054,5.265940,9.381135,3.899000,-4.460142,9.410467,0.144933,7.429755,1.988744,-7.001256]],[[0.282753,-0.551742,7.282019,1.196335,5.695523,-5.997917,-7.406587,-5.565569,2.121827,-5.037433,-2.423122,6.824020,6.957291,1.530869,-6.585323],[-0.797798,8.910977,4.161354,-5.594052,8.616805,5.286250,-1.972865,4.968469,-2.989916,2.942530,9.919537,-1.488686,4.592661,3.101588,-6.592414],[-9.493469,-2.366871,4.871869,-2.545065,-3.943100,6.459436,5.264355,1.032761,-5.919531,6.508117,-4.413919,-7.384270,5.903396,7.411405,-9.745092],[9.490165,-4.979917,-2.409809,8.260433,0.793376,-0.133916,-1.628663,6.971194,8.717767,8.545566,6.884082,9.974830,-7.833024,4.030212,5.588382]],[[-6.820862,9.317168,-6.168902,-8.464465,-2.203358,9.255277,1.192223,3.192606,-3.753684,-2.760412,3.403078,3.008591,6.090418,-8.657982,0.448023],[-9.722252,-7.365331,-0.887448,4.721275,-2.137059,6.312310,3.347916,8.834145,7.479830,9.565156,4.864686,8.906216,1.721741,8.134403,9.373883],[6.454031,-7.542492,5.890900,9.234007,4.039853,1.376281,7.238264,9.896043,9.342747,-5.747442,9.955599,9.484978,0.639940,4.828390,-2.572017],[7.468922,7.672914,7.980866,9.187431,5.066819,3.239239,9.286704,3.881353,8.159852,1.403302,9.218387,-1.796827,1.272024,7.786861,-6.482341]],[[0.753896,-9.102610,1.026460,-7.713317,-4.330840,8.431016,-7.852354,-4.224205,-9.372358,-6.235973,-6.016244,-6.266953,-9.431734,-9.758522,-9.630536],[-8.464151,-8.268991,-7.792470,-4.983827,-7.721111,3.373039,-1.839793,-1.525752,9.736877,1.780650,-4.172875,-7.521469,-8.070668,-7.285299,-0.994737],[8.213791,4.091366,0.830403,0.623835,-1.332495,-4.804413,6.777027,7.170195,-2.110943,-0.808486,-4.409012,5.147306,2.295478,7.946678,-8.777622],[9.525483,-5.666105,8.068438,-8.325777,-1.632906,4.357005,-8.040662,7.094700,-1.524296,4.735823,9.876970,-1.676612,-8.214985,-1.907481,5.737551]]], dtype = "float64")#candidate|853|(6, 4, 15)|const|float64
bop_854 = relay.equal(uop_804.astype('bool'), const_853.astype('bool')) # shape=(6, 4, 15)
func_391_call = mod.get_global_var('func_391')
func_392_call = mutated_mod.get_global_var('func_392')
call_865 = func_391_call()
call_866 = func_391_call()
output = relay.Tuple([bop_854,call_865,])
output2 = relay.Tuple([bop_854,call_866,])
func_874 = relay.Function([var_803,], output)
mod['func_874'] = func_874
mod = relay.transform.InferType()(mod)
mutated_mod['func_874'] = func_874
mutated_mod = relay.transform.InferType()(mutated_mod)
var_875 = relay.var("var_875", dtype = "float64", shape = (6, 4, 1))#candidate|875|(6, 4, 1)|var|float64
func_874_call = mutated_mod.get_global_var('func_874')
call_876 = func_874_call(var_875)
output = call_876
func_877 = relay.Function([var_875], output)
mutated_mod['func_877'] = func_877
mutated_mod = relay.transform.InferType()(mutated_mod)
func_295_call = mod.get_global_var('func_295')
func_297_call = mutated_mod.get_global_var('func_297')
call_887 = relay.TupleGetItem(func_295_call(), 2)
call_888 = relay.TupleGetItem(func_297_call(), 2)
var_895 = relay.var("var_895", dtype = "bool", shape = (64, 8))#candidate|895|(64, 8)|var|bool
bop_896 = relay.maximum(call_887.astype('float32'), var_895.astype('float32')) # shape=(64, 8)
bop_899 = relay.maximum(call_888.astype('float32'), var_895.astype('float32')) # shape=(64, 8)
output = relay.Tuple([bop_896,])
output2 = relay.Tuple([bop_899,])
func_900 = relay.Function([var_895,], output)
mod['func_900'] = func_900
mod = relay.transform.InferType()(mod)
var_901 = relay.var("var_901", dtype = "bool", shape = (64, 8))#candidate|901|(64, 8)|var|bool
output = func_900(var_901)
func_902 = relay.Function([var_901], output)
mutated_mod['func_902'] = func_902
mutated_mod = relay.transform.InferType()(mutated_mod)
func_295_call = mod.get_global_var('func_295')
func_297_call = mutated_mod.get_global_var('func_297')
call_931 = relay.TupleGetItem(func_295_call(), 2)
call_932 = relay.TupleGetItem(func_297_call(), 2)
var_938 = relay.var("var_938", dtype = "bool", shape = (64, 4))#candidate|938|(64, 4)|var|bool
bop_939 = relay.floor_divide(call_931.astype('float32'), var_938.astype('float32')) # shape=(64, 4)
bop_942 = relay.floor_divide(call_932.astype('float32'), var_938.astype('float32')) # shape=(64, 4)
uop_945 = relay.atan(var_938.astype('float64')) # shape=(64, 4)
func_655_call = mod.get_global_var('func_655')
func_658_call = mutated_mod.get_global_var('func_658')
const_950 = relay.const([6.898049,5.207123,-7.921388,-4.927191,8.532405,7.155037,8.288613,7.605524,3.166788,3.140501,-5.240082,2.642520,4.467880,-8.561986,-9.468596,-6.075358,-5.549961,-7.916300,-4.477837,-7.165001,6.059336,4.313838,8.032707,-3.753639,2.277548,-2.038676,-3.222484,3.807294,5.643287,-3.975578,-8.683182,1.860541,3.630103,0.876277,3.714820,5.968740,-1.453040,7.344031,-1.474291,-6.403802,1.373508,8.702215,-7.687206,9.696873,-2.987193,-5.566024,-9.419704,-0.089148,9.758761,4.650968,2.388799,2.227288,6.242090,0.723669,-2.780706,-8.311519,8.945985,-4.597013,-2.821856,2.130079,6.000849,7.857196,8.818259,6.352772,-4.524083,4.926448,-5.585830,0.674731,0.061144,0.052194,-9.643432,4.522220,2.883748,-9.312552,0.935198,1.706175,5.184735,-3.131152,-2.670654,1.377480,-3.128773,-5.009527,-2.966488,6.437176,6.325267,4.372726,-7.842986,7.042389,-7.184118,5.485429,6.031037,4.282868,-6.173666,3.266491,4.705554,7.167954,-6.320413,-6.192418,4.841055,-0.866193,-2.688453,-7.248819,1.434143,6.510744,0.201198,3.092633,6.374627,1.677191,9.627874,-0.233688,-3.568255,-3.137034,6.630287,9.504769,-1.399610,9.963791,6.208988,6.702754,4.511882,4.601682,-7.496035,8.395586,4.223245,1.329448,-6.413781,4.952438,3.788856,1.968653,5.362994,2.317345,-9.768813,-8.790522,-4.352553,-0.105595,-0.493282,3.987134,7.687053,-5.853380,5.298515,5.347367,8.983183,-5.288352,-6.710490,-1.142291,-3.390267,-6.051072,-2.550640,3.394508,-4.289939,1.088710,2.790470,9.748508,4.004958,3.761344,4.783892,-5.245874,4.227976,7.872405,-2.319710,3.609808,6.211490,-7.907093,8.617316,1.775233,5.698014,-1.413408,3.696801,0.711175,-8.548672,8.524619,5.637058,-2.674820,5.043114,8.404580,1.667196,-1.451742,-8.823249,8.408993,-5.375201,0.802671,6.037326,-5.995560,-9.005749,7.910001,-2.567176,-0.952898,1.800859,7.444810,8.930979,-4.149522,4.595168,4.574649,3.405179,6.733394,5.216128,-9.591765,4.960817,9.299125,-5.973365,-8.524943,-7.077839,0.963799,2.498549,-6.727940,7.878725,-9.729281,4.535847,-6.167095,-4.034362,4.416755,-2.867240,-7.201255,-0.669947,2.347771,-2.736795,-8.762998,3.440192,-7.753969,-1.362016,4.018826,-0.803892,-3.001371,3.461251,-0.061312,0.978097,-0.388002,2.646693,7.412489,-3.390666,3.064643,-0.635919,3.996666,6.484001,-6.020753,-6.788537,9.546434,6.444652,2.292788,-2.815769,-0.143830,1.719364,3.008773,1.382285,-6.567215,-6.005616,4.496930,2.889352,-4.961104,-1.812048,-5.874551,-2.621444,4.760174,-4.355911,-4.197582,9.149475,-6.366635,1.645117,9.578641,-1.970105,9.267770,9.372289,2.057526,1.465231,5.590891,-4.515623,8.729570,9.354937,7.601571,1.003115,-9.953176,-2.064467,6.218283,1.205109,6.586177,-5.382738,-1.761467,2.367332,6.402897,0.568628,-7.656277,-4.812567,-7.156188,5.479943,9.421447,0.483978,2.304627,-8.880682,-8.193781,3.617251,4.039659,-2.472239,-0.714881,0.415454,-9.970747,-7.616694,2.989281,-9.775250,7.972528,8.158379,-5.307597,-6.553416,-6.030747,-6.763456,-0.994781,-7.235195,-7.829863,0.674791,-0.910825,-9.043549,5.859543,-9.602672,6.432717,-7.572225,-6.516877,-3.701810,2.770247,-6.974426,7.863796,-1.181811,-8.915790,-2.482529,3.631881,5.983910,-9.973230,-0.010088,0.940139,-9.043647,-2.328270,8.887899,-1.969043,2.816305,-6.495126,-0.608774,2.244188,-0.880309,2.845944,-1.958313,-5.382856,4.345392,1.362070,7.839775,-2.284217,9.097741,-5.648384,9.630970,-2.178051,-5.664198,-1.540772,4.224918,5.903424,1.493565,-1.105859,2.044792,-2.409812,0.284423,0.050934,-6.727710,6.924971,-5.033963,-9.333015,-1.244352,-9.843944,4.635185,9.549734,-0.556991,-0.037025,-6.286541,8.807344,-7.234292,-0.739592,0.671206,-8.247981,0.855877,-3.950058,0.127774,7.369136,8.616383,5.830978,-1.722541,9.018281,3.457373,-6.626618,-6.637530,-9.422592,0.402976,3.879579,-2.432191,-9.062043,6.125223,6.782621,3.085021,-4.626956,-5.907698,-3.420601,1.356883,-0.286670,0.456089,-9.323141,-0.826175,-5.384845,5.257614,6.105034,2.027685,5.817582,-9.549356,-3.147449,9.421225,-1.845736,-9.161263,-8.580812,5.477274,-8.755699,5.297123,-7.076337,0.448186,-8.870035,-4.642979,-9.901783,3.414407,-8.991082,-7.684859,-6.140818,-1.051587,-5.945604,8.775838,-3.946767,8.220103,2.833827,9.234005,-5.269597,4.233835,9.660573,-8.025224,1.977679,9.217980,4.172391,-0.713824,4.517503,5.895404,4.837882,-0.619832,8.392734,4.698598,-5.936511,-3.495331,7.710977,2.040703,-2.036417,5.554595,-1.422089,1.015523,-9.784625,4.481616,-5.249716,5.096338,6.556058,2.809145,8.673040,5.343437,5.418066,5.498814,2.087101,5.696817,-3.086454,-9.965671,8.625259,8.798091,1.572627,5.392188,4.562035,-7.597939,-5.250489,5.502623,-0.952069,-1.407447,-0.042606,-7.515124,-4.767563,1.692297,-9.025652,7.239004,-7.598310,-2.565718,5.969547,9.616698,-1.273095,9.184929,-4.651076,7.806409,-0.035740,-6.252667,6.600522,-3.435694,3.250718,-6.608340,4.523615,8.980469,-1.019676,-3.677295,-4.502104,-1.729453,9.071151,0.283362,-4.792240,-9.407327,-0.854412,-3.806127,9.220430,-8.182162,-2.470578,8.759139,-8.831201,3.161189,-2.982472,4.093748,-9.219250,3.673767,5.615615,1.503799,1.385104,-0.657381,-0.332850,4.628003,-5.046058,-3.820250,3.969205,-7.613612,8.133879,-0.135398,1.385667,-4.281602,-0.398432,8.064115,-6.222310,2.172619,-4.474723,-7.068203,-1.667740,2.443192,5.101469,-6.617258,7.659440,-8.105024,-8.020663,-2.365062,-8.385874,7.629642,-0.986204,2.335988,2.821799,7.686793,-6.667607,2.141565,4.601394,2.068501,-5.491610,8.495394,8.782755,-9.119838,4.485352,0.802056,7.372404,-5.930589,-8.215349,5.192313,-0.048745,9.502932,-8.428227,-1.408843,5.239156,-4.347554,1.861217,4.398817,1.758764,-3.207045,-5.077255,1.750541,7.638376,-3.182419,4.195896,5.898139,-1.639598,-4.255106,1.587740,-4.769696,7.235677,8.113867,0.842880,6.924184,-5.709633,4.577819,8.201979,9.400850,-1.593603,-0.469076,5.659008,4.180939,5.035541,-8.974453,-2.087630,1.792476,5.245396,-9.233086,-2.156585,1.909756,-7.918400,4.642203,7.262259,-8.868240,-2.630069,8.358744,-5.631646,9.190763,5.162720,9.651165,2.968908,1.217020,2.153150,8.435471,0.259084,-8.292718,0.397360,9.784934,-9.369847,-3.980715,1.819197,-5.302512,-9.656620,7.622844,5.170533,-8.865114,7.483280,4.392285,7.036546,-2.533375,-2.171923,-2.617830,4.538347,-8.042087,5.218773], dtype = "float64")#candidate|950|(640,)|const|float64
var_951 = relay.var("var_951", dtype = "float64", shape = (121,))#candidate|951|(121,)|var|float64
call_949 = relay.TupleGetItem(func_655_call(relay.reshape(const_950.astype('float64'), [16, 10, 4]), relay.reshape(var_951.astype('float64'), [11, 11]), ), 3)
call_952 = relay.TupleGetItem(func_658_call(relay.reshape(const_950.astype('float64'), [16, 10, 4]), relay.reshape(var_951.astype('float64'), [11, 11]), ), 3)
output = relay.Tuple([bop_939,uop_945,call_949,const_950,var_951,])
output2 = relay.Tuple([bop_942,uop_945,call_952,const_950,var_951,])
func_959 = relay.Function([var_938,var_951,], output)
mod['func_959'] = func_959
mod = relay.transform.InferType()(mod)
mutated_mod['func_959'] = func_959
mutated_mod = relay.transform.InferType()(mutated_mod)
func_959_call = mutated_mod.get_global_var('func_959')
var_961 = relay.var("var_961", dtype = "bool", shape = (64, 4))#candidate|961|(64, 4)|var|bool
var_962 = relay.var("var_962", dtype = "float64", shape = (121,))#candidate|962|(121,)|var|float64
call_960 = func_959_call(var_961,var_962,)
output = call_960
func_963 = relay.Function([var_961,var_962,], output)
mutated_mod['func_963'] = func_963
mutated_mod = relay.transform.InferType()(mutated_mod)
func_439_call = mod.get_global_var('func_439')
func_440_call = mutated_mod.get_global_var('func_440')
call_983 = func_439_call()
call_984 = func_439_call()
func_105_call = mod.get_global_var('func_105')
func_107_call = mutated_mod.get_global_var('func_107')
const_1007 = relay.const([True,True,False,False,False,True,False,False,True,False,False,False,False,True,True,False,False,True,False,False,True,True,False,True,True,False,False,True,False,False,True,True,True,False,True,True,True,True,True,False,False,False,False,False,True,True,False,True,True,False,True,False,True,False,True,False,False,True,False,False,False,True,True,True], dtype = "bool")#candidate|1007|(64,)|const|bool
call_1006 = func_105_call(relay.reshape(const_1007.astype('bool'), [16, 1, 4]))
call_1008 = func_105_call(relay.reshape(const_1007.astype('bool'), [16, 1, 4]))
func_391_call = mod.get_global_var('func_391')
func_392_call = mutated_mod.get_global_var('func_392')
call_1009 = func_391_call()
call_1010 = func_391_call()
output = relay.Tuple([call_983,call_1006,const_1007,call_1009,])
output2 = relay.Tuple([call_984,call_1008,const_1007,call_1010,])
func_1017 = relay.Function([], output)
mod['func_1017'] = func_1017
mod = relay.transform.InferType()(mod)
output = func_1017()
func_1018 = relay.Function([], output)
mutated_mod['func_1018'] = func_1018
mutated_mod = relay.transform.InferType()(mutated_mod)
func_391_call = mod.get_global_var('func_391')
func_392_call = mutated_mod.get_global_var('func_392')
call_1037 = func_391_call()
call_1038 = func_391_call()
uop_1044 = relay.asinh(call_1037.astype('float64')) # shape=(64, 6)
uop_1046 = relay.asinh(call_1038.astype('float64')) # shape=(64, 6)
uop_1054 = relay.erf(call_1037.astype('float64')) # shape=(64, 6)
uop_1056 = relay.erf(call_1038.astype('float64')) # shape=(64, 6)
uop_1057 = relay.atanh(call_1037.astype('float32')) # shape=(64, 6)
uop_1059 = relay.atanh(call_1038.astype('float32')) # shape=(64, 6)
func_348_call = mod.get_global_var('func_348')
func_351_call = mutated_mod.get_global_var('func_351')
var_1065 = relay.var("var_1065", dtype = "bool", shape = (48,))#candidate|1065|(48,)|var|bool
call_1064 = func_348_call(relay.reshape(var_1065.astype('bool'), [12, 2, 2]))
call_1066 = func_348_call(relay.reshape(var_1065.astype('bool'), [12, 2, 2]))
bop_1072 = relay.less_equal(uop_1054.astype('bool'), relay.reshape(uop_1044.astype('bool'), relay.shape_of(uop_1054))) # shape=(64, 6)
bop_1075 = relay.less_equal(uop_1056.astype('bool'), relay.reshape(uop_1046.astype('bool'), relay.shape_of(uop_1056))) # shape=(64, 6)
bop_1085 = relay.equal(call_1037.astype('bool'), relay.reshape(uop_1054.astype('bool'), relay.shape_of(call_1037))) # shape=(64, 6)
bop_1088 = relay.equal(call_1038.astype('bool'), relay.reshape(uop_1056.astype('bool'), relay.shape_of(call_1038))) # shape=(64, 6)
output = relay.Tuple([uop_1057,call_1064,var_1065,bop_1072,bop_1085,])
output2 = relay.Tuple([uop_1059,call_1066,var_1065,bop_1075,bop_1088,])
func_1095 = relay.Function([var_1065,], output)
mod['func_1095'] = func_1095
mod = relay.transform.InferType()(mod)
mutated_mod['func_1095'] = func_1095
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1096 = relay.var("var_1096", dtype = "bool", shape = (48,))#candidate|1096|(48,)|var|bool
func_1095_call = mutated_mod.get_global_var('func_1095')
call_1097 = func_1095_call(var_1096)
output = call_1097
func_1098 = relay.Function([var_1096], output)
mutated_mod['func_1098'] = func_1098
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1017_call = mod.get_global_var('func_1017')
func_1018_call = mutated_mod.get_global_var('func_1018')
call_1105 = relay.TupleGetItem(func_1017_call(), 1)
call_1106 = relay.TupleGetItem(func_1018_call(), 1)
output = relay.Tuple([call_1105,])
output2 = relay.Tuple([call_1106,])
func_1107 = relay.Function([], output)
mod['func_1107'] = func_1107
mod = relay.transform.InferType()(mod)
output = func_1107()
func_1108 = relay.Function([], output)
mutated_mod['func_1108'] = func_1108
mutated_mod = relay.transform.InferType()(mutated_mod)
func_295_call = mod.get_global_var('func_295')
func_297_call = mutated_mod.get_global_var('func_297')
call_1123 = relay.TupleGetItem(func_295_call(), 2)
call_1124 = relay.TupleGetItem(func_297_call(), 2)
var_1126 = relay.var("var_1126", dtype = "bool", shape = (64, 4))#candidate|1126|(64, 4)|var|bool
bop_1127 = relay.bitwise_xor(call_1123.astype('uint64'), var_1126.astype('uint64')) # shape=(64, 4)
bop_1130 = relay.bitwise_xor(call_1124.astype('uint64'), var_1126.astype('uint64')) # shape=(64, 4)
bop_1131 = relay.power(call_1123.astype('float32'), var_1126.astype('float32')) # shape=(64, 4)
bop_1134 = relay.power(call_1124.astype('float32'), var_1126.astype('float32')) # shape=(64, 4)
func_1095_call = mod.get_global_var('func_1095')
func_1098_call = mutated_mod.get_global_var('func_1098')
const_1141 = relay.const([True,True,True,False,False,True,False,False,False,True,False,True,True,False,True,True,False,False,True,False,False,False,False,False,False,True,True,False,True,True,False,False,False,True,False,False,True,False,False,True,False,True,False,True,True,True,True,True], dtype = "bool")#candidate|1141|(48,)|const|bool
call_1140 = relay.TupleGetItem(func_1095_call(relay.reshape(const_1141.astype('bool'), [48,])), 2)
call_1142 = relay.TupleGetItem(func_1098_call(relay.reshape(const_1141.astype('bool'), [48,])), 2)
func_900_call = mod.get_global_var('func_900')
func_902_call = mutated_mod.get_global_var('func_902')
const_1149 = relay.const([[False,True,False,False,True,True,False,True,False,True,True,True,False,True,True,False,False,False,True,False,False,False,True,True,True,False,False,False,False,True,True,False,False,True,False,False,False,True,True,True,False,False,False,False,False,True,False,False,False,False,False,False,False,True,True,True,True,True,True,True,True,True,True,True],[False,False,True,True,True,True,False,True,True,False,True,True,False,True,True,False,True,False,False,True,True,True,False,True,True,False,False,False,True,False,True,True,False,True,False,True,False,False,False,True,True,True,True,True,False,False,True,False,False,True,True,False,False,False,True,True,False,True,True,True,True,True,False,True],[False,True,False,False,True,False,True,False,True,False,True,False,True,False,False,True,True,True,True,False,True,False,True,True,False,True,False,True,False,True,True,False,False,True,False,True,False,True,False,True,False,True,True,True,False,True,False,True,True,False,True,False,False,True,False,False,False,False,False,False,True,True,False,True],[False,False,True,False,True,True,False,True,False,True,False,False,True,True,False,False,True,True,False,True,False,False,False,False,True,False,False,False,True,False,False,True,False,True,False,False,False,False,True,False,True,False,True,False,True,True,False,False,False,True,True,True,True,True,True,False,True,False,True,False,False,True,False,True],[False,False,True,False,False,False,False,True,False,True,False,True,False,False,True,True,True,True,False,True,False,True,True,False,True,False,False,False,True,False,True,True,False,False,True,False,False,False,False,True,True,False,False,False,False,False,True,False,True,True,True,True,False,False,True,False,True,False,False,False,False,True,False,True],[True,True,True,True,True,True,False,True,True,True,True,False,True,False,False,False,True,True,True,True,True,True,True,False,True,True,True,True,False,True,False,True,False,False,True,False,True,True,True,True,False,False,True,True,False,True,True,True,False,True,False,True,False,False,False,True,True,True,False,False,False,True,True,False],[True,False,False,False,False,True,True,False,True,False,False,True,True,True,False,True,False,True,True,False,True,True,True,False,False,False,False,False,True,False,False,False,False,True,False,False,False,False,True,False,False,True,True,False,False,False,True,True,True,False,True,False,True,True,False,True,True,True,True,False,True,False,False,True],[True,False,False,True,False,True,True,True,False,True,True,False,True,False,True,False,True,True,False,False,False,False,False,True,True,True,True,False,True,True,False,False,True,False,False,False,True,True,True,True,False,False,True,True,False,True,True,True,False,True,False,False,False,False,True,True,True,False,False,True,True,False,True,False]], dtype = "bool")#candidate|1149|(8, 64)|const|bool
call_1148 = relay.TupleGetItem(func_900_call(relay.reshape(const_1149.astype('bool'), [64, 8])), 0)
call_1150 = relay.TupleGetItem(func_902_call(relay.reshape(const_1149.astype('bool'), [64, 8])), 0)
func_1107_call = mod.get_global_var('func_1107')
func_1108_call = mutated_mod.get_global_var('func_1108')
call_1151 = relay.TupleGetItem(func_1107_call(), 0)
call_1152 = relay.TupleGetItem(func_1108_call(), 0)
uop_1160 = relay.rsqrt(const_1149.astype('float64')) # shape=(8, 64)
uop_1165 = relay.tan(uop_1160.astype('float64')) # shape=(8, 64)
bop_1174 = relay.power(uop_1160.astype('float64'), relay.reshape(uop_1165.astype('float64'), relay.shape_of(uop_1160))) # shape=(8, 64)
output = relay.Tuple([bop_1127,bop_1131,call_1140,const_1141,call_1148,call_1151,bop_1174,])
output2 = relay.Tuple([bop_1130,bop_1134,call_1142,const_1141,call_1150,call_1152,bop_1174,])
func_1178 = relay.Function([var_1126,], output)
mod['func_1178'] = func_1178
mod = relay.transform.InferType()(mod)
var_1179 = relay.var("var_1179", dtype = "bool", shape = (64, 4))#candidate|1179|(64, 4)|var|bool
output = func_1178(var_1179)
func_1180 = relay.Function([var_1179], output)
mutated_mod['func_1180'] = func_1180
mutated_mod = relay.transform.InferType()(mutated_mod)
func_295_call = mod.get_global_var('func_295')
func_297_call = mutated_mod.get_global_var('func_297')
call_1182 = relay.TupleGetItem(func_295_call(), 0)
call_1183 = relay.TupleGetItem(func_297_call(), 0)
func_439_call = mod.get_global_var('func_439')
func_440_call = mutated_mod.get_global_var('func_440')
call_1220 = func_439_call()
call_1221 = func_439_call()
const_1222 = relay.const([[[-8,7,10,-6,1,4,3],[6,-4,7,-6,-4,9,-5],[2,10,4,3,7,9,-3],[-7,6,-10,-6,8,-8,-3],[10,1,-1,-3,-10,8,-6],[-7,-1,7,10,10,4,9],[2,-10,-9,4,4,4,-4],[3,-1,-2,9,-2,7,-6],[-9,7,-7,4,10,6,5],[-7,-2,8,-3,8,10,-10],[1,1,10,-3,-5,-3,-5]],[[8,-6,-9,-9,4,7,-3],[-1,7,-8,-3,-4,-5,3],[5,-6,-8,-2,-3,-5,-1],[8,-1,-7,-4,-5,-5,-3],[-10,-8,-8,10,7,4,2],[-6,10,-7,6,9,2,6],[5,-8,8,1,-2,-2,4],[-8,5,-9,7,-6,-3,2],[-1,3,-8,2,-8,-1,-6],[9,1,6,9,-1,-3,-1],[3,10,-10,9,-3,-3,4]],[[1,-1,9,8,-9,1,5],[-8,10,8,7,-4,-7,7],[-10,-5,2,1,-9,-7,6],[-8,-1,7,-10,-1,4,-3],[-4,10,3,5,3,-7,5],[-3,-3,3,-9,-5,-7,4],[-4,4,-9,-2,-4,-8,-2],[-1,10,-9,-5,8,5,3],[-4,7,5,-5,-10,7,-3],[10,1,-2,5,5,-6,-6],[-6,6,7,9,-5,-8,-1]],[[-6,1,8,7,-2,-5,-4],[10,3,10,-8,-1,1,-1],[-2,6,-7,-5,-9,-6,7],[-10,2,3,-9,-5,10,-4],[-5,-9,-9,6,-10,-2,-5],[1,-2,3,2,1,8,8],[3,8,9,4,10,6,1],[2,6,8,-6,-2,-8,10],[1,4,10,-4,9,8,10],[-1,2,6,7,-6,6,1],[-2,-10,9,-9,-7,-9,-10]]], dtype = "uint16")#candidate|1222|(4, 11, 7)|const|uint16
bop_1223 = relay.left_shift(call_1182.astype('int16'), relay.reshape(const_1222.astype('int16'), relay.shape_of(call_1182))) # shape=(4, 11, 7)
bop_1226 = relay.left_shift(call_1183.astype('int16'), relay.reshape(const_1222.astype('int16'), relay.shape_of(call_1183))) # shape=(4, 11, 7)
output = relay.Tuple([call_1220,bop_1223,])
output2 = relay.Tuple([call_1221,bop_1226,])
func_1227 = relay.Function([], output)
mod['func_1227'] = func_1227
mod = relay.transform.InferType()(mod)
mutated_mod['func_1227'] = func_1227
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1227_call = mutated_mod.get_global_var('func_1227')
call_1228 = func_1227_call()
output = call_1228
func_1229 = relay.Function([], output)
mutated_mod['func_1229'] = func_1229
mutated_mod = relay.transform.InferType()(mutated_mod)
func_391_call = mod.get_global_var('func_391')
func_392_call = mutated_mod.get_global_var('func_392')
call_1233 = func_391_call()
call_1234 = func_391_call()
func_1017_call = mod.get_global_var('func_1017')
func_1018_call = mutated_mod.get_global_var('func_1018')
call_1245 = relay.TupleGetItem(func_1017_call(), 1)
call_1246 = relay.TupleGetItem(func_1018_call(), 1)
func_1107_call = mod.get_global_var('func_1107')
func_1108_call = mutated_mod.get_global_var('func_1108')
call_1253 = relay.TupleGetItem(func_1107_call(), 0)
call_1254 = relay.TupleGetItem(func_1108_call(), 0)
output = relay.Tuple([call_1233,call_1245,call_1253,])
output2 = relay.Tuple([call_1234,call_1246,call_1254,])
func_1260 = relay.Function([], output)
mod['func_1260'] = func_1260
mod = relay.transform.InferType()(mod)
output = func_1260()
func_1261 = relay.Function([], output)
mutated_mod['func_1261'] = func_1261
mutated_mod = relay.transform.InferType()(mutated_mod)
func_439_call = mod.get_global_var('func_439')
func_440_call = mutated_mod.get_global_var('func_440')
call_1286 = func_439_call()
call_1287 = func_439_call()
func_900_call = mod.get_global_var('func_900')
func_902_call = mutated_mod.get_global_var('func_902')
const_1295 = relay.const([False,False,False,True,True,False,True,True,False,False,False,False,True,True,False,False,False,True,False,True,True,False,True,True,False,True,True,False,True,False,False,True,False,True,False,False,True,True,True,True,False,False,False,True,True,False,True,False,True,True,True,True,True,False,False,True,True,False,False,False,False,False,True,False,True,True,False,True,True,False,False,True,False,False,False,True,True,True,True,False,True,False,True,False,True,False,False,False,False,False,True,False,False,False,False,False,False,True,True,True,True,True,False,True,False,False,False,True,True,False,True,False,False,True,True,True,True,True,False,True,True,True,True,True,True,True,True,True,False,False,False,True,False,False,False,False,False,True,True,False,True,False,False,True,True,True,True,False,False,True,True,True,False,False,True,True,False,False,True,False,True,True,False,True,False,False,True,False,True,False,False,False,False,True,False,False,False,True,False,True,False,False,False,False,False,True,True,False,False,False,True,True,False,True,False,False,True,True,False,True,True,True,True,True,False,True,True,False,False,False,True,False,False,False,False,False,True,False,True,True,False,False,False,False,True,False,False,False,True,True,True,False,False,True,False,False,False,True,False,True,True,False,True,True,False,False,False,True,False,True,True,False,True,True,True,False,False,True,False,True,False,False,False,False,True,False,False,True,True,True,False,True,True,False,False,True,False,False,False,False,True,True,False,False,True,True,False,True,True,True,False,True,True,False,False,False,False,False,True,False,True,False,True,False,False,True,True,False,False,False,False,True,True,False,False,False,False,False,True,True,True,False,False,False,False,False,False,True,True,False,True,False,False,False,True,False,True,False,False,True,False,False,True,False,False,True,False,False,True,False,True,True,False,False,True,False,False,False,True,True,False,False,False,False,False,True,False,False,True,False,True,False,False,False,False,False,True,False,True,True,False,False,False,False,False,True,True,True,True,False,False,True,True,False,True,True,True,True,True,True,True,True,True,True,True,True,False,True,True,True,False,False,True,False,False,False,True,True,True,True,False,True,False,True,False,False,False,True,True,False,False,True,True,True,False,False,False,False,True,False,True,True,False,True,True,False,True,True,False,False,False,False,True,False,True,True,False,True,True,False,True,True,True,False,True,True,True,True,False,False,True,True,False,True,False,True,False,True,False,False,True,False,False,True,True,True,False,True,False,True,True,False,True,False,False,False,False,True,True,False,False,True,True,False,False,False,True,False,True,False,False,True], dtype = "bool")#candidate|1295|(512,)|const|bool
call_1294 = relay.TupleGetItem(func_900_call(relay.reshape(const_1295.astype('bool'), [64, 8])), 0)
call_1296 = relay.TupleGetItem(func_902_call(relay.reshape(const_1295.astype('bool'), [64, 8])), 0)
output = relay.Tuple([call_1286,call_1294,const_1295,])
output2 = relay.Tuple([call_1287,call_1296,const_1295,])
func_1305 = relay.Function([], output)
mod['func_1305'] = func_1305
mod = relay.transform.InferType()(mod)
mutated_mod['func_1305'] = func_1305
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1305_call = mutated_mod.get_global_var('func_1305')
call_1306 = func_1305_call()
output = call_1306
func_1307 = relay.Function([], output)
mutated_mod['func_1307'] = func_1307
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1354 = relay.const([[[5.526103,-2.017101,9.786189,3.971623,-7.932876,-5.691117,3.237766,-7.060329]],[[-9.923264,7.093037,0.134196,-1.792386,-1.208516,6.635435,3.994887,-5.114761]],[[-0.722803,-7.959649,-7.931552,2.804966,-2.149076,9.445466,7.120820,-9.697374]],[[0.253487,-7.623546,5.910869,-6.536264,-7.333807,-0.375564,1.400188,-3.264597]],[[1.438811,9.421063,6.232395,-1.251681,-4.927992,4.529412,2.275658,6.116664]],[[9.857188,-2.414653,-6.942578,-6.980008,-6.672541,6.613437,-2.541238,3.917914]]], dtype = "float64")#candidate|1354|(6, 1, 8)|const|float64
uop_1355 = relay.sin(const_1354.astype('float64')) # shape=(6, 1, 8)
output = relay.Tuple([uop_1355,])
output2 = relay.Tuple([uop_1355,])
func_1362 = relay.Function([], output)
mod['func_1362'] = func_1362
mod = relay.transform.InferType()(mod)
mutated_mod['func_1362'] = func_1362
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1362_call = mutated_mod.get_global_var('func_1362')
call_1363 = func_1362_call()
output = call_1363
func_1364 = relay.Function([], output)
mutated_mod['func_1364'] = func_1364
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1305_call = mod.get_global_var('func_1305')
func_1307_call = mutated_mod.get_global_var('func_1307')
call_1367 = relay.TupleGetItem(func_1305_call(), 2)
call_1368 = relay.TupleGetItem(func_1307_call(), 2)
var_1383 = relay.var("var_1383", dtype = "bool", shape = (512,))#candidate|1383|(512,)|var|bool
bop_1384 = relay.floor_mod(call_1367.astype('float32'), relay.reshape(var_1383.astype('float32'), relay.shape_of(call_1367))) # shape=(512,)
bop_1387 = relay.floor_mod(call_1368.astype('float32'), relay.reshape(var_1383.astype('float32'), relay.shape_of(call_1368))) # shape=(512,)
func_578_call = mod.get_global_var('func_578')
func_581_call = mutated_mod.get_global_var('func_581')
const_1391 = relay.const([-0.356013,-4.325920,-3.795090,-4.448441,-2.085453,-4.104028,8.383559,-7.848385,0.257679,-8.974683,1.086334,9.989313,-4.947707,6.060728,-2.642429,7.068966,-5.650681,3.013026,-6.564852,-6.658731,9.774930,-5.984284,-4.241570,4.271064,-0.100007,9.936673,4.081928,-9.618860,-4.711111,3.910389,-6.944946,6.420519,9.712808,-9.651330,0.240408,-1.297734,9.659121,6.928332,8.064492,8.006967,-7.978875,-6.480829,0.671929,9.384626,-2.597237,2.398591,5.847814,-1.471596,4.872686,4.220987,8.928116,5.048327,-9.751460,8.447179,2.316179,-9.210707,2.260940,-4.815875,4.411657,-3.831751,-5.466527,7.791511,6.623768,-1.347658,-7.940899,2.768228,-2.326141,-8.877042,3.047536,-2.293958,-3.316196,-3.227012,6.631910,6.858833,-4.392532,8.823700,9.330695,2.067440,-9.580426,0.076300,3.081090,-8.315790,4.294392,-3.746793,-7.711701,3.995838,8.643924,-6.591328,-0.749376,-8.693025,-7.693903,-5.670031,-3.062110,-5.096675,4.302016,7.857856,-3.152099,-6.525594,-7.044087,-1.300990,-8.534389,6.824451,6.817011,-5.005068,3.266506,-3.518595,-5.858411,9.971489,-9.536404,7.825036,8.494626,-1.099026,2.517489,6.743818,-0.779303,-0.089022,-2.552664,-1.278492,-7.222480,1.778110,8.821466,2.652057,-6.702597,-4.391206,-7.444630,1.096677,-8.501146,6.318023,-6.763549,8.877405,-0.916105,3.342160,-8.724117,-6.880921,7.660897,-8.988396,9.251507,-0.228544,8.009668,2.979626,9.379618,7.565255,-5.568167,0.370210,-4.373915,8.508817,-6.233067,3.371344,6.660125,8.565940,4.154442,5.166952,1.311451,1.811695,6.103463,-3.557215,5.906666,-1.196665,-1.027225,-8.012509,8.016366,5.262796,7.173334,-2.409926,-4.815577,1.636863,3.351542,2.119760,-2.097564,7.856643,1.992361,-9.005897,-5.515757,-4.658678,-0.621899,9.304880,6.850157,-9.108789,6.323081,7.542004,-7.349400,7.407664,2.752572,3.772337,2.920632,5.153374,-5.934232,1.940310,3.052780,-9.689297,6.528113,6.039043,-7.565098,2.575520,-5.544335,-8.877618,7.868564,-2.935617,-3.921555,-2.918695,3.508466,-3.176456,-3.988209,-5.710063,1.224016,8.816398,-3.947460,4.273065,-4.498423,-6.743950,5.943611,-8.530612,-4.695834,-0.294191,-1.573382,3.292724,-4.335788,4.711023,4.455138,-6.744810,-5.153312,8.301232,-2.126361,-9.131250,7.326374,9.853029,1.835912,0.347958,9.247435,-3.723397,4.960768,4.533212,6.814108,-5.463543,-3.825313,0.510007,-3.381249,0.320718,-2.312849,-7.948462,-3.248596,-4.038397,3.373803,3.742149,2.956529,-0.550357,8.358846,3.200875,-7.957575,-4.472658,-8.554626,-0.805156,-9.397353,-5.304495,3.875603,8.563118,-0.057358,0.765993,0.668534,-2.727823,-1.098186,9.866282,-4.809991,-6.749625,-2.640332,8.561053,-5.872351,-6.228733,9.126067,9.593837,5.570552,-7.086069,6.844122,7.512865,4.285888,9.477588,-0.917666,5.772734,6.308155,9.368634,-3.328042,7.871282,-5.908798,-8.894375,-4.994955,-0.455652,-5.356099,1.767366,-1.477040,-5.732926,3.272311,6.073342,6.970404,-4.402545,-1.554506,-5.884303,9.335657,-1.105490,4.862007,4.611588,-5.179365,7.722794,9.023427,-5.847389,2.424635,2.796498,4.945325,-4.632113,3.150517,8.784798,4.320025,5.235574,6.073031,-1.366503,-1.649207,-6.250730,-8.325523,4.024296,9.719068,6.474038,-7.933645,9.683624,-9.197507,-9.283043,-3.322342,8.295030,-1.125851,-9.784406,-2.138764,-1.341574,1.366863,-2.175457,0.216605,7.845748,5.782101,1.525441,8.397735,3.118560,5.858378,2.965262,-3.802155,9.739543,1.062306,-7.930860,-2.500201,-6.767602,-0.121087,4.112045,-3.245160,-3.267976,-1.638036,-0.171094,-7.571055,8.330973,1.352973,1.456120,5.414763,-3.151137,0.836997,0.473363,-9.010363,1.162597,-9.771361,-2.850311,8.379506,-9.858771,-5.197014,4.952629,4.910835,-5.093065,1.625114,-6.749398,-8.170968,-1.543530,8.534311,-3.753907,7.478258,-3.982815,-2.485177,5.837911,2.111391,5.828767,-8.836389,-3.645662], dtype = "float32")#candidate|1391|(384,)|const|float32
call_1390 = relay.TupleGetItem(func_578_call(relay.reshape(const_1391.astype('float32'), [64, 6])), 3)
call_1392 = relay.TupleGetItem(func_581_call(relay.reshape(const_1391.astype('float32'), [64, 6])), 3)
func_959_call = mod.get_global_var('func_959')
func_963_call = mutated_mod.get_global_var('func_963')
var_1403 = relay.var("var_1403", dtype = "bool", shape = (256,))#candidate|1403|(256,)|var|bool
const_1404 = relay.const([-8.658972,6.893334,5.910135,-0.484809,-0.356095,5.446160,2.722547,4.373504,-0.714086,-7.021844,6.586824,8.886651,-4.675709,2.151371,-6.804405,-0.605136,-8.031929,-9.221754,6.844948,2.024034,4.919095,2.324792,-6.672331,5.599577,-7.571729,-4.737202,-8.114604,9.581356,-2.611382,-5.067514,-7.214294,0.763815,4.037385,-8.398002,-3.547857,-2.813075,-1.821301,9.181386,-1.331964,-4.438867,-5.654096,8.028856,-2.228180,4.406765,3.302731,7.432953,-0.021289,4.112555,-5.617217,4.887852,3.353826,-1.120942,0.972577,-7.940034,6.246477,6.352319,4.350936,-0.698122,1.445521,6.365368,6.810860,-1.808850,0.861212,3.433709,0.268553,0.653740,-4.905229,2.591618,4.716009,-7.885285,-8.075748,-1.394904,-5.411585,2.105705,-4.510704,-8.252098,5.770582,9.113518,-0.916642,-1.093883,5.823231,-5.092703,-7.024770,-1.629754,-1.650784,-1.142956,-2.577262,-4.120172,0.524082,-2.162500,-4.046188,3.560038,-0.876980,2.571278,-4.123942,-4.734473,3.663067,3.265966,-1.647424,2.170633,-2.265534,1.074248,-7.916561,4.948176,6.950757,5.909677,4.012387,2.279542,1.798878,-1.740990,6.671898,-9.929478,-0.552684,-2.452517,2.999841,9.459707,7.965702,-2.999826,-7.433718,2.040483,6.254162], dtype = "float64")#candidate|1404|(121,)|const|float64
call_1402 = relay.TupleGetItem(func_959_call(relay.reshape(var_1403.astype('bool'), [64, 4]), relay.reshape(const_1404.astype('float64'), [121,]), ), 4)
call_1405 = relay.TupleGetItem(func_963_call(relay.reshape(var_1403.astype('bool'), [64, 4]), relay.reshape(const_1404.astype('float64'), [121,]), ), 4)
func_1095_call = mod.get_global_var('func_1095')
func_1098_call = mutated_mod.get_global_var('func_1098')
const_1422 = relay.const([False,False,True,False,True,True,False,True,True,True,True,True,False,True,True,True,True,False,True,False,True,True,False,False,False,True,True,True,False,True,False,False,False,True,True,True,False,True,False,False,False,True,True,False,True,False,True,False], dtype = "bool")#candidate|1422|(48,)|const|bool
call_1421 = relay.TupleGetItem(func_1095_call(relay.reshape(const_1422.astype('bool'), [48,])), 3)
call_1423 = relay.TupleGetItem(func_1098_call(relay.reshape(const_1422.astype('bool'), [48,])), 3)
output = relay.Tuple([bop_1384,call_1390,const_1391,call_1402,var_1403,const_1404,call_1421,const_1422,])
output2 = relay.Tuple([bop_1387,call_1392,const_1391,call_1405,var_1403,const_1404,call_1423,const_1422,])
func_1433 = relay.Function([var_1383,var_1403,], output)
mod['func_1433'] = func_1433
mod = relay.transform.InferType()(mod)
mutated_mod['func_1433'] = func_1433
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1433_call = mutated_mod.get_global_var('func_1433')
var_1435 = relay.var("var_1435", dtype = "bool", shape = (512,))#candidate|1435|(512,)|var|bool
var_1436 = relay.var("var_1436", dtype = "bool", shape = (256,))#candidate|1436|(256,)|var|bool
call_1434 = func_1433_call(var_1435,var_1436,)
output = call_1434
func_1437 = relay.Function([var_1435,var_1436,], output)
mutated_mod['func_1437'] = func_1437
mutated_mod = relay.transform.InferType()(mutated_mod)
func_295_call = mod.get_global_var('func_295')
func_297_call = mutated_mod.get_global_var('func_297')
call_1510 = relay.TupleGetItem(func_295_call(), 0)
call_1511 = relay.TupleGetItem(func_297_call(), 0)
func_1095_call = mod.get_global_var('func_1095')
func_1098_call = mutated_mod.get_global_var('func_1098')
var_1522 = relay.var("var_1522", dtype = "bool", shape = (1, 48))#candidate|1522|(1, 48)|var|bool
call_1521 = relay.TupleGetItem(func_1095_call(relay.reshape(var_1522.astype('bool'), [48,])), 0)
call_1523 = relay.TupleGetItem(func_1098_call(relay.reshape(var_1522.astype('bool'), [48,])), 0)
output = relay.Tuple([call_1510,call_1521,var_1522,])
output2 = relay.Tuple([call_1511,call_1523,var_1522,])
func_1530 = relay.Function([var_1522,], output)
mod['func_1530'] = func_1530
mod = relay.transform.InferType()(mod)
mutated_mod['func_1530'] = func_1530
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1531 = relay.var("var_1531", dtype = "bool", shape = (1, 48))#candidate|1531|(1, 48)|var|bool
func_1530_call = mutated_mod.get_global_var('func_1530')
call_1532 = func_1530_call(var_1531)
output = call_1532
func_1533 = relay.Function([var_1531], output)
mutated_mod['func_1533'] = func_1533
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1305_call = mod.get_global_var('func_1305')
func_1307_call = mutated_mod.get_global_var('func_1307')
call_1537 = relay.TupleGetItem(func_1305_call(), 1)
call_1538 = relay.TupleGetItem(func_1307_call(), 1)
uop_1540 = relay.atanh(call_1537.astype('float64')) # shape=(64, 8)
uop_1542 = relay.atanh(call_1538.astype('float64')) # shape=(64, 8)
output = relay.Tuple([uop_1540,])
output2 = relay.Tuple([uop_1542,])
func_1547 = relay.Function([], output)
mod['func_1547'] = func_1547
mod = relay.transform.InferType()(mod)
output = func_1547()
func_1548 = relay.Function([], output)
mutated_mod['func_1548'] = func_1548
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1547_call = mod.get_global_var('func_1547')
func_1548_call = mutated_mod.get_global_var('func_1548')
call_1559 = relay.TupleGetItem(func_1547_call(), 0)
call_1560 = relay.TupleGetItem(func_1548_call(), 0)
var_1568 = relay.var("var_1568", dtype = "float64", shape = (64, 8))#candidate|1568|(64, 8)|var|float64
bop_1569 = relay.floor_divide(call_1559.astype('float32'), relay.reshape(var_1568.astype('float32'), relay.shape_of(call_1559))) # shape=(64, 8)
bop_1572 = relay.floor_divide(call_1560.astype('float32'), relay.reshape(var_1568.astype('float32'), relay.shape_of(call_1560))) # shape=(64, 8)
output = relay.Tuple([bop_1569,])
output2 = relay.Tuple([bop_1572,])
func_1580 = relay.Function([var_1568,], output)
mod['func_1580'] = func_1580
mod = relay.transform.InferType()(mod)
mutated_mod['func_1580'] = func_1580
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1581 = relay.var("var_1581", dtype = "float64", shape = (64, 8))#candidate|1581|(64, 8)|var|float64
func_1580_call = mutated_mod.get_global_var('func_1580')
call_1582 = func_1580_call(var_1581)
output = call_1582
func_1583 = relay.Function([var_1581], output)
mutated_mod['func_1583'] = func_1583
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1260_call = mod.get_global_var('func_1260')
func_1261_call = mutated_mod.get_global_var('func_1261')
call_1600 = relay.TupleGetItem(func_1260_call(), 0)
call_1601 = relay.TupleGetItem(func_1261_call(), 0)
func_348_call = mod.get_global_var('func_348')
func_351_call = mutated_mod.get_global_var('func_351')
const_1608 = relay.const([False,True,True,False,True,True,True,False,False,True,False,False,True,False,False,False,True,True,True,False,True,False,False,True,False,True,False,False,False,False,False,False,True,True,True,False,False,False,True,True,True,True,True,True,False,True,True,True], dtype = "bool")#candidate|1608|(48,)|const|bool
call_1607 = func_348_call(relay.reshape(const_1608.astype('bool'), [12, 2, 2]))
call_1609 = func_348_call(relay.reshape(const_1608.astype('bool'), [12, 2, 2]))
func_900_call = mod.get_global_var('func_900')
func_902_call = mutated_mod.get_global_var('func_902')
var_1611 = relay.var("var_1611", dtype = "bool", shape = (512, 1))#candidate|1611|(512, 1)|var|bool
call_1610 = relay.TupleGetItem(func_900_call(relay.reshape(var_1611.astype('bool'), [64, 8])), 0)
call_1612 = relay.TupleGetItem(func_902_call(relay.reshape(var_1611.astype('bool'), [64, 8])), 0)
bop_1624 = relay.left_shift(call_1610.astype('uint16'), relay.reshape(var_1611.astype('uint16'), relay.shape_of(call_1610))) # shape=(64, 8)
bop_1627 = relay.left_shift(call_1612.astype('uint16'), relay.reshape(var_1611.astype('uint16'), relay.shape_of(call_1612))) # shape=(64, 8)
output = relay.Tuple([call_1600,call_1607,const_1608,bop_1624,])
output2 = relay.Tuple([call_1601,call_1609,const_1608,bop_1627,])
func_1634 = relay.Function([var_1611,], output)
mod['func_1634'] = func_1634
mod = relay.transform.InferType()(mod)
mutated_mod['func_1634'] = func_1634
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1635 = relay.var("var_1635", dtype = "bool", shape = (512, 1))#candidate|1635|(512, 1)|var|bool
func_1634_call = mutated_mod.get_global_var('func_1634')
call_1636 = func_1634_call(var_1635)
output = call_1636
func_1637 = relay.Function([var_1635], output)
mutated_mod['func_1637'] = func_1637
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1547_call = mod.get_global_var('func_1547')
func_1548_call = mutated_mod.get_global_var('func_1548')
call_1639 = relay.TupleGetItem(func_1547_call(), 0)
call_1640 = relay.TupleGetItem(func_1548_call(), 0)
func_295_call = mod.get_global_var('func_295')
func_297_call = mutated_mod.get_global_var('func_297')
call_1641 = relay.TupleGetItem(func_295_call(), 0)
call_1642 = relay.TupleGetItem(func_297_call(), 0)
uop_1653 = relay.atan(call_1641.astype('float32')) # shape=(4, 11, 7)
uop_1655 = relay.atan(call_1642.astype('float32')) # shape=(4, 11, 7)
output = relay.Tuple([call_1639,uop_1653,])
output2 = relay.Tuple([call_1640,uop_1655,])
func_1684 = relay.Function([], output)
mod['func_1684'] = func_1684
mod = relay.transform.InferType()(mod)
mutated_mod['func_1684'] = func_1684
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1684_call = mutated_mod.get_global_var('func_1684')
call_1685 = func_1684_call()
output = call_1685
func_1686 = relay.Function([], output)
mutated_mod['func_1686'] = func_1686
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1107_call = mod.get_global_var('func_1107')
func_1108_call = mutated_mod.get_global_var('func_1108')
call_1716 = relay.TupleGetItem(func_1107_call(), 0)
call_1717 = relay.TupleGetItem(func_1108_call(), 0)
output = relay.Tuple([call_1716,])
output2 = relay.Tuple([call_1717,])
func_1718 = relay.Function([], output)
mod['func_1718'] = func_1718
mod = relay.transform.InferType()(mod)
output = func_1718()
func_1719 = relay.Function([], output)
mutated_mod['func_1719'] = func_1719
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1740 = relay.const([[[4.290833,0.089471,-0.691734,-9.396174,3.524360,0.152430,-1.226153,6.952101],[-9.741283,-6.433762,1.376759,4.064306,-2.880060,-9.958926,2.029578,-5.539472],[-6.837551,6.217149,5.450658,2.506484,6.907337,6.852257,-4.403367,3.480739],[6.774321,1.391050,-2.569337,2.915780,-5.887680,-0.473467,8.684962,-6.810707],[-0.310278,9.844347,2.906666,-4.024196,6.614402,-2.340026,-7.724802,7.802009],[-4.439433,6.504989,7.117405,4.959438,-1.437460,3.254272,-0.280311,-2.019579],[4.755644,-8.186151,-6.125480,-5.580965,-0.930516,-6.076932,-4.993463,-7.863343],[-9.210953,-1.279229,1.833619,0.811518,5.180965,1.896649,-7.453275,-9.470368],[5.839674,9.575023,-5.203419,-8.460968,-6.574859,9.661904,-4.041068,0.863940],[1.183633,-7.567901,-4.090405,3.097603,-7.955490,5.959281,-9.254257,-6.845020],[7.237210,4.510407,5.216144,-2.804633,-4.761240,2.473344,-7.345797,3.715438],[-5.939398,-0.708202,5.914226,-6.728970,-1.551703,2.172434,8.402574,9.497014],[7.569083,-1.439544,-5.757236,-9.286665,9.778997,7.220894,9.219375,9.954979],[-2.109510,-9.360039,0.130874,4.585393,-9.296290,-3.164662,-4.001906,-8.444517],[4.348636,3.601021,-4.170676,-7.369387,6.296608,0.221134,5.846352,-7.161486],[-9.474215,4.199246,8.949083,3.500349,9.043146,6.222506,7.984001,0.467706]],[[8.140648,-0.265119,0.836490,9.174138,-3.422739,3.524888,5.724425,0.021979],[-0.153717,-3.268351,8.150374,5.387787,3.890527,6.976162,6.787892,2.107800],[7.480625,-7.328315,0.152085,3.464686,-3.265564,4.527077,-4.356576,4.225072],[5.474916,-9.802059,3.406783,-6.657758,-3.926654,-6.169421,-8.475864,-7.987179],[3.315904,-7.673016,-4.528160,6.104327,-6.797070,1.492307,2.452998,6.810966],[-2.561567,-2.586242,-9.543574,-9.960254,-1.787251,-2.825914,7.101153,-4.467568],[3.024372,4.792997,-4.317314,-6.214877,0.143711,4.131336,-4.400684,9.172752],[-4.271689,-3.409915,-7.141429,1.612001,6.163627,-9.391236,1.206761,-8.999437],[4.609764,-8.083089,-8.330511,1.186715,-3.461007,-2.522324,6.562587,5.853070],[9.773118,-6.669198,6.967716,-2.611334,2.268592,7.210270,1.709878,2.381329],[6.178287,-8.196478,-8.182100,5.434006,-4.836341,7.938686,2.733674,0.272873],[5.081171,1.995961,-8.150601,3.898356,-7.853468,-4.837427,-4.005152,-1.642572],[8.728735,9.731073,-1.977227,7.451764,9.607605,4.487246,3.767424,0.389683],[-4.889713,8.463291,7.202979,0.512946,2.395823,0.931106,6.222651,7.591533],[1.810689,6.142273,6.495403,-0.292609,4.130964,-7.990695,2.359841,3.503370],[-9.798762,-4.808807,-3.364117,2.976013,1.657611,9.811517,-9.351277,5.416054]],[[-7.862037,-2.365507,7.857132,-7.993787,-9.698024,-2.420458,-8.041551,3.911617],[-0.185761,-6.206899,1.033792,8.889341,5.440470,-2.776063,1.947556,1.861332],[-5.539869,-1.590758,-1.407919,-4.454815,6.698488,-1.662493,2.707158,-1.868538],[7.264284,-8.845959,-8.943502,8.009418,-8.513377,7.982434,-1.356417,0.031475],[-4.612264,-5.035852,-2.168322,6.675934,9.846231,-4.937946,-8.917960,5.876701],[3.573968,-9.236345,5.668507,9.791279,0.146394,4.366596,2.801892,-0.399136],[-0.847492,8.825557,-8.327680,-9.321329,-2.164274,-7.595413,9.803499,7.013749],[1.804506,-5.259090,7.865282,-0.144560,6.608408,-2.898169,2.139220,-9.339591],[-0.336972,-7.358305,3.964742,-5.467334,3.625062,-3.169284,-2.107219,-9.908376],[3.197927,-2.279261,-2.028845,-1.782887,8.309723,5.158773,5.553675,-7.333683],[8.433121,-0.612712,-1.256722,-8.645227,3.432167,-6.193503,-6.121197,1.069660],[-1.119452,6.555309,2.083773,-7.219406,-0.328571,9.830703,8.410866,5.487173],[-7.106051,4.430787,6.169623,3.800622,-1.778766,-9.800522,-9.623681,3.826005],[-0.190650,2.731746,-2.552906,-8.821103,2.091852,-3.395087,5.053734,8.620080],[-4.094122,-4.631415,2.490082,-6.571384,-1.867997,-5.211995,4.942421,3.092866],[-5.375150,3.077572,-6.531177,-9.007199,9.880002,-7.733272,-7.245387,-2.319815]],[[3.357352,-2.895351,-7.119740,-4.002207,-2.521996,3.720792,-8.918727,0.154423],[-4.909216,7.539021,-3.882376,-6.378417,1.205318,-8.429244,1.290656,-1.978048],[-4.366563,1.179978,1.217418,1.592029,-5.833557,9.527590,4.694982,-6.298543],[6.742899,-1.261314,7.611194,6.535973,3.545593,-3.139471,6.739018,7.312269],[-3.380539,-8.566621,5.214130,1.389442,6.499503,-2.778399,1.439293,-5.934101],[7.628412,-2.079229,4.192784,0.469105,7.269915,6.793846,-8.717022,-4.776721],[0.219691,-8.431694,-5.188200,8.940912,0.951891,-1.435712,-8.215388,7.416114],[3.290193,-5.709686,-6.215967,-0.284854,5.006371,-9.846829,-5.968657,-3.015700],[8.065020,-1.976420,-7.159254,7.352812,-9.315876,-3.082808,-9.148905,-5.598933],[1.979437,2.068784,-1.718435,-1.519698,2.441792,9.622521,9.512770,-5.014703],[-9.464067,2.775402,-5.497653,-1.982015,-8.007893,5.406564,4.636256,0.090809],[-9.408288,-9.256028,-9.062971,-8.517426,6.826604,9.032662,-9.546658,2.549897],[6.398354,6.988867,-5.030390,-2.451162,6.210248,3.493490,6.972437,3.143982],[1.264402,-6.228527,-2.455663,-0.777479,-0.082110,5.344969,3.269574,8.189631],[1.830129,-7.325727,7.408711,-2.808336,-2.827994,5.974431,-3.591386,5.852003],[-5.120917,6.744445,-9.849438,-0.685935,-1.009813,3.785129,-9.309814,-5.869131]],[[-6.865522,5.144812,2.590437,-4.850811,-4.178024,9.840180,-5.953639,-2.515332],[-9.226127,-6.943759,8.280024,3.200440,-2.182379,0.792423,0.919527,-7.855262],[-4.590133,2.626239,6.580077,2.373888,2.712244,9.389606,4.779806,-2.540781],[3.128491,7.369758,7.615582,-6.449847,1.200556,8.705477,6.110596,-4.769885],[6.021431,0.392599,8.124606,-9.816564,6.401431,5.859024,-8.326213,-5.246774],[-8.197055,-5.659998,-1.995344,1.187972,8.488558,1.189989,-0.140452,-1.576917],[5.682598,-3.327911,9.382649,-6.161252,-3.138716,9.635660,3.890016,0.557041],[9.518983,-4.357173,-6.615206,-9.284530,-3.392748,9.748488,9.155494,-2.386021],[8.099142,-8.004346,-7.333308,-2.388773,-9.594349,2.688709,0.582884,1.565213],[-5.164288,8.914575,8.035915,-0.923376,1.787570,-0.775513,-2.713848,0.216823],[8.895768,-2.009219,-0.182925,4.730538,-1.472625,7.455638,3.896612,0.449849],[-9.261780,-6.221675,-7.904282,9.223810,-9.757024,-5.145406,-1.746932,0.006597],[7.135497,4.408543,-8.654806,-4.499953,9.899122,-0.475543,-2.941249,8.287950],[-6.597867,-0.466877,-1.067423,-2.293626,6.335528,7.951649,5.397403,-9.623603],[-9.890090,-1.198775,-7.748889,-1.933541,-2.957339,-6.524257,-7.445688,7.695448],[5.191635,9.024243,7.927815,4.559558,-5.686351,6.914112,3.735766,7.147115]],[[2.469603,-1.851263,-6.517159,-6.484347,8.427935,-9.246507,-3.615291,1.585186],[1.822304,9.951833,-9.084837,-8.496009,-2.936085,-7.495289,1.666021,5.588555],[-1.400809,-4.254877,-2.988465,2.710477,9.673757,2.700803,-7.304218,1.848936],[2.706303,-9.236732,4.071632,9.453031,-6.018812,3.297877,3.002600,3.468477],[-3.474719,-8.546092,-6.768307,7.569688,1.552248,6.036251,6.953957,-1.507524],[5.044668,-0.237639,2.189363,-9.948670,-2.754109,9.240128,5.571744,2.691267],[-0.202866,-6.548409,7.890064,-1.989086,3.664982,-9.603467,-1.921297,0.528824],[-0.781700,7.702950,6.827540,3.188798,6.126822,4.139067,4.157737,7.292970],[4.858468,-9.586153,6.767021,8.832144,-2.875161,5.507602,-5.558490,5.051509],[-0.946878,-6.237409,-3.945610,7.730565,-1.193109,-5.927668,5.450936,3.242650],[-1.299806,-6.496058,-3.128938,-8.841398,5.376929,-6.209142,-0.547258,-1.135122],[-2.635314,4.276779,3.764400,-0.966568,1.935991,3.296189,-1.852937,7.566078],[6.724795,-4.731467,-4.528936,-8.667064,-0.788253,2.786011,-4.647337,-4.185181],[4.638466,-9.110788,-6.190187,-3.956822,9.394535,0.369336,3.071014,-6.133306],[-1.783905,-7.428397,0.100427,-7.656350,5.488180,4.926608,-7.151983,-8.076221],[2.134562,-3.756774,-7.972384,8.419638,-9.773816,0.496247,-6.801318,-9.610254]],[[8.171551,4.948063,-3.335531,-3.704216,3.526403,1.451647,6.033242,6.668888],[-7.021304,2.910998,4.112818,5.559380,5.597506,0.105981,-5.401058,-3.875810],[-5.890497,8.136941,7.312296,7.143284,0.451255,-3.888700,-2.473607,8.454976],[8.028989,8.234764,3.566730,3.386022,-9.766442,-3.050959,-3.630604,-4.983301],[-4.849076,3.009705,0.074892,5.915862,-1.847957,-1.534449,9.261250,5.856581],[-0.553323,8.003640,6.884608,-0.741724,6.112879,6.323819,9.790892,6.499895],[8.456201,7.274899,4.614250,2.965514,5.461379,-8.668675,1.451874,2.564784],[4.106156,0.620222,5.754896,-1.900224,9.844914,7.976502,5.314638,-6.081326],[5.175311,2.750278,-2.098431,-3.821451,-9.095645,2.393967,2.278297,2.746973],[4.822649,0.160983,-8.612539,-8.511425,1.601995,-0.179934,-7.006973,8.663868],[9.373477,-0.217055,3.411386,5.915969,2.149824,6.659580,6.150739,1.800847],[-3.521937,-0.930207,-1.141657,-2.278160,-6.548967,-3.332597,0.346618,-0.506026],[9.068939,5.030223,-0.667938,-3.652643,6.372460,-1.029783,6.761545,5.145664],[-4.803399,-9.783005,-5.071284,8.147276,-0.659662,4.032329,4.398357,-3.100860],[-2.303708,-5.001058,-1.083421,9.966877,-2.078775,-3.186403,0.518471,1.796038],[5.287980,5.312610,-5.797450,-9.634326,-0.845487,2.411486,-1.384727,-3.612994]],[[8.950736,7.935569,-4.025833,8.136390,-6.185683,-1.920102,6.040815,4.297069],[1.168151,9.495596,8.863256,-8.830381,3.096653,-4.578118,9.356055,6.398900],[2.194487,-0.777173,9.691891,-6.693227,-5.456193,4.162219,9.521477,-8.480705],[2.830988,-3.758094,-0.732156,9.611618,-4.225106,6.844744,-3.837871,-7.036821],[0.154275,6.437183,-4.269800,-2.371489,-2.951829,8.377461,-4.293559,2.460579],[2.315367,2.212037,-0.918493,6.751477,-8.004871,6.406567,8.645219,-2.141423],[-1.864468,9.218373,4.906408,4.869607,-2.423797,8.488031,6.258516,-7.385014],[2.126479,-2.102148,-4.179313,-9.455440,-7.033430,-2.052350,-7.601237,-8.300497],[-2.782365,7.427798,0.051604,-8.563883,4.998714,-1.739146,-4.322479,6.355958],[-8.604346,8.986503,-8.617558,7.988995,1.676268,-7.356668,-4.950328,4.077822],[6.726628,4.581770,9.051090,-9.441016,1.199759,9.344686,0.936495,9.908217],[-6.465892,4.843984,7.711535,8.024354,-1.584773,-6.464531,-0.536464,2.315208],[-3.616474,-8.939233,-5.078832,5.855177,-4.953403,6.220683,0.949191,4.061451],[-6.192969,-1.645541,-8.244424,-9.652701,-2.767521,8.098447,-2.254189,-3.866411],[7.593531,8.944115,8.462633,-4.735849,2.101789,0.118275,-7.094378,7.525752],[8.333245,-0.205015,7.204129,-4.046707,4.378380,1.578528,2.200141,4.379689]],[[-1.302009,-7.577606,8.732418,2.640403,6.558847,8.197756,-2.466801,-5.077668],[0.708507,9.710698,5.049243,-7.646769,6.310860,7.092736,8.980459,-8.503533],[6.089106,9.496625,6.100697,3.771205,5.600233,-7.240038,5.334670,-5.097605],[-5.943292,-9.417850,8.917062,-9.035257,-1.647283,2.273572,-9.175832,0.880348],[5.542049,-9.697984,-2.090815,6.967314,3.398150,3.988803,-1.105933,9.487395],[3.577719,-6.567406,-5.369892,6.067278,-6.776440,-3.543239,-0.172869,-2.177266],[-2.880109,-2.529708,3.036370,-8.548423,-1.862507,4.968163,5.659087,5.632988],[-3.950973,-5.991840,-9.917687,7.854638,-3.774122,-1.557162,-9.895782,-4.570794],[5.312550,1.243250,-4.693306,0.107605,4.577631,6.487472,3.856920,6.992118],[1.103422,-5.446074,2.195099,-6.752238,1.934052,3.715215,-5.640893,-4.707938],[-8.137266,-6.353197,-4.455373,7.593414,-7.981616,-0.448575,2.421518,-4.974662],[5.987719,8.843216,-8.241821,8.939267,-0.790317,0.111098,-1.256008,-9.740752],[6.443640,-7.844030,8.322612,7.954925,-8.688488,8.986601,7.149431,-9.079275],[8.926411,-3.270520,-6.172549,1.524424,-8.082248,8.000303,6.535199,1.479744],[-7.714869,-2.020378,-3.588434,0.326120,1.362876,-1.567383,-3.074439,-0.174772],[-6.764871,-6.665024,-1.456420,0.353622,-9.089226,5.846674,1.402983,4.855951]],[[-0.557790,2.081300,0.989230,-0.698725,2.439829,-0.668032,1.094089,6.121690],[7.720144,-8.213686,-5.902495,-0.754068,-6.889141,-8.884040,-1.439533,1.429579],[0.675395,4.338782,-0.157065,3.737138,1.949972,2.256384,-3.461541,-7.268275],[-9.616691,7.201207,7.870577,-0.882065,-9.914269,3.939758,-6.659577,0.016135],[6.973657,-2.153818,-6.977894,4.538877,9.767828,6.687687,-1.674891,1.339996],[-9.204240,3.827392,-9.398917,-3.528664,-8.776443,-0.615638,-8.602936,-3.011649],[-0.768080,6.385924,-0.053956,-4.714157,-9.984638,-0.607266,-5.523178,9.422399],[-7.537465,-2.143901,-8.399361,7.762768,-0.416294,9.441471,-4.295272,-7.695123],[6.806841,6.565173,-0.755496,4.290170,5.705122,8.685872,-9.835948,3.893688],[7.956067,7.657766,-8.872456,-8.405036,-5.866660,8.088598,1.615258,-5.647705],[-2.392258,8.661823,6.103139,9.822832,-7.720036,-8.921829,5.364541,8.356939],[9.226730,6.450191,-6.828454,-6.754956,0.524309,3.684112,9.770406,3.973026],[2.394296,3.014878,-8.296339,-6.441754,8.029754,7.716663,-4.274250,-0.221949],[9.380890,3.436148,2.263059,1.774379,4.932489,-9.075742,-2.684017,-2.863717],[-3.285101,-6.667321,-3.572784,6.131607,-8.842499,7.712780,1.417582,-3.057659],[4.115421,-8.123315,-4.987761,2.353247,-6.244606,-5.685106,-6.028036,4.271409]],[[-5.410480,1.455493,-2.364667,5.270694,8.458583,0.682340,-6.707756,4.478311],[2.946199,-2.931666,0.506191,3.484348,1.029359,-3.069994,4.902966,-8.460478],[-3.319123,-1.966436,-8.805591,4.248038,-6.798809,5.125583,-1.117689,-0.575436],[-2.033913,7.926298,3.424136,-8.504104,2.364723,-7.938652,-9.329977,-4.017543],[-3.796223,3.590631,-7.566523,-6.314125,1.130912,9.857981,-8.463269,8.934010],[5.147548,8.363516,5.966942,2.817377,-0.925331,2.704335,0.579931,0.700551],[8.622969,-6.581615,2.083373,-1.618359,-3.882538,0.524878,-2.209711,-8.019233],[7.417351,-6.394677,1.973757,1.059043,8.579603,-7.518235,7.792891,-4.645324],[-5.734484,-8.915852,3.372133,-3.025263,5.145690,-5.467002,-8.756390,6.517260],[-4.879434,-7.186620,3.646950,-8.957982,4.596093,7.465917,-8.413882,7.828019],[6.536469,9.469298,-7.472527,-1.926524,3.003978,5.563311,3.128938,1.584044],[-6.081428,3.708380,-7.220877,-9.639403,-9.344494,-9.008052,3.129150,3.325267],[0.062107,4.710985,-6.855635,0.363283,1.469648,1.906447,5.160446,-4.867470],[3.551829,-1.563227,9.711403,0.892429,-5.989593,9.503356,0.549680,-0.846681],[9.534186,-7.521922,-8.089098,7.139370,4.487919,-8.116254,8.445972,-8.344863],[3.156245,-1.742510,-9.228590,-9.759896,8.785329,-3.076578,2.784011,-4.219021]],[[3.669795,-9.956875,-1.537398,1.746634,5.334736,5.405362,-0.421356,1.526566],[-9.283694,0.964142,2.552785,7.055151,0.673897,6.412192,6.234275,3.586625],[-9.071040,-8.832301,9.477083,-0.117272,1.001725,2.122462,-2.131626,7.398376],[8.943428,5.258365,2.398521,0.220923,-5.036188,9.854218,-8.172077,-1.203210],[-9.446033,-2.542306,-0.021086,-4.531485,-6.037261,-5.147747,-5.103201,7.055531],[-8.776220,-4.037752,3.696554,-2.838831,-8.946828,2.557617,-6.264917,-5.818604],[-0.002604,-9.030971,4.243479,3.594365,-4.900201,-0.106786,6.216901,-5.579042],[-0.175088,9.070569,0.073761,-2.059756,5.259072,-5.810980,9.129022,9.021277],[0.911906,0.911629,-2.296795,-4.868717,-2.708063,-1.595408,-3.004409,7.068419],[8.456603,9.211329,-5.241478,2.111525,3.680483,6.839109,-9.239615,9.970499],[-0.371908,-7.431769,7.589001,7.194319,-2.646881,4.339439,3.714968,6.850602],[-1.217779,9.494761,-0.456736,-2.805292,-4.706564,8.229983,-0.130577,6.187599],[0.536962,-8.237086,-8.218519,-0.042183,1.956120,-6.132958,-0.491750,2.773234],[-1.867989,9.036649,7.555007,-9.174673,7.710479,-4.761176,-2.038900,-7.984279],[-8.073927,-2.040252,-3.705154,8.930598,5.858337,-8.685749,3.711482,-1.402749],[-2.689145,8.585791,3.205526,-2.930770,5.461168,6.099048,-5.794643,6.155771]],[[-9.893069,9.210832,-0.529882,-6.488900,-5.410157,9.002512,-0.460506,6.384320],[4.453441,0.648493,8.758418,1.403947,-0.034174,-0.790540,-6.327858,0.601637],[-9.951498,9.911423,1.989174,-5.156717,1.756815,-0.800741,3.355546,-4.283001],[-6.556129,6.251686,1.738306,-9.536107,8.698548,-5.173162,-2.801176,-4.423336],[9.076594,6.131391,1.486484,-5.973017,7.599635,3.394932,3.966273,2.495420],[8.794057,2.261938,2.693183,-8.702062,-4.725567,-5.423442,3.198314,0.725006],[-6.473258,7.922268,-7.102157,-7.832966,-1.399838,-1.964326,-8.335738,8.922316],[9.571782,-2.986329,-2.991518,8.275924,-6.506786,6.211493,9.700601,-1.068123],[4.126654,5.324558,9.504157,4.721890,4.139734,8.927270,6.925588,1.331589],[2.135279,4.639190,1.323862,3.999795,-3.196947,2.100321,2.699950,-4.861090],[7.914868,7.470112,3.417586,8.480317,-3.258110,-2.628372,4.972277,-1.689937],[-1.826111,1.364423,9.200144,7.781466,2.326686,1.541105,-9.235900,-5.628126],[4.576711,-8.006865,-2.558706,-9.325481,8.683375,1.252986,-9.953469,1.019700],[5.541855,-5.674502,7.250509,1.967054,-3.983362,-1.325277,-9.767731,9.617772],[-6.103434,-2.588606,5.739486,6.207189,-0.195022,2.444945,4.044498,4.085200],[0.040324,7.934170,5.372767,-0.096321,5.958822,-7.282727,4.066846,1.099934]],[[4.987128,-4.792000,-7.919087,7.581924,-6.886035,-1.949965,-3.097767,3.653626],[1.547176,-3.723498,3.050343,6.124908,6.983485,-4.955046,7.520877,-4.635277],[6.518527,1.684103,7.164660,-3.589983,4.525290,4.791876,-4.353581,-5.035297],[2.748735,-4.616128,1.909298,6.175533,9.798352,4.475628,0.204582,-3.635191],[-3.922865,1.387990,-8.451058,-2.648401,-7.689712,2.010327,-4.626134,-1.985142],[5.752491,-1.529122,-2.782376,5.591596,6.925735,-8.209805,9.483530,7.116224],[-7.559426,2.675863,5.653362,7.905442,9.673805,-8.912886,-0.489423,5.742724],[-9.980875,-5.841193,1.173516,-4.731697,-7.787470,9.947187,2.021102,6.492632],[3.617754,4.701080,-8.934891,-7.990422,2.344095,3.855289,-6.227002,4.891408],[-7.830292,7.724757,-8.897650,-9.155896,7.848998,-6.499637,3.343658,-3.655324],[-1.778002,4.584746,-5.760280,-0.834768,-9.019660,9.307390,-5.695382,4.438906],[-0.918181,-0.070416,8.155765,5.059158,-9.623692,2.366347,-7.115736,2.863626],[1.010333,4.873408,-4.040496,-4.096099,-8.632976,7.937556,-5.375628,4.240811],[-2.399942,1.506085,2.011405,-8.349068,-2.131336,1.355309,7.879837,0.898492],[4.138507,8.734875,-5.835424,-4.090230,8.130183,8.812618,8.866876,8.134125],[-4.318618,4.647601,3.302546,-3.441910,4.203188,-3.594052,-0.061339,-7.865873]],[[8.290062,6.428769,7.083220,-8.026075,-3.845827,-4.970168,-9.832396,7.790183],[9.099831,-1.463565,-7.572528,-8.703113,-3.110822,-5.350546,1.079784,-9.301350],[-7.024713,-1.738854,-9.749715,0.766379,5.539734,-7.117982,9.141539,-0.492007],[-6.123085,5.369240,7.846955,-6.404721,1.141739,-6.015364,1.685557,1.748292],[4.998299,7.278434,-3.795891,-8.848856,5.305224,0.678006,-6.580858,3.122937],[6.948092,2.629426,-7.905778,-1.232061,-3.547662,-3.708290,-6.124992,-8.529231],[-8.881040,0.536418,-2.237582,-3.025590,-7.899228,-8.893203,3.107808,6.451948],[-1.658667,-1.427336,-4.905042,-4.120060,8.254824,4.591170,-4.468849,1.228945],[8.751955,2.566830,-3.228693,0.538353,-7.344943,2.426542,4.620277,-0.185337],[9.049852,3.462722,5.715553,3.274322,-6.502332,-7.894969,-1.863967,4.240837],[-5.586841,7.288009,-4.672167,9.319874,-7.354250,5.426592,2.331362,6.551776],[-5.293580,6.148057,3.870507,-2.685712,5.541894,-1.128861,3.980203,0.975559],[5.452328,-2.457886,-0.531287,-5.733624,1.835388,-5.297046,9.103486,3.397483],[-2.283367,3.020940,1.026376,-1.668555,3.550002,-4.211609,-9.938347,-7.964650],[-2.308790,-5.819338,1.902240,3.092045,-5.661755,9.323187,-5.549603,1.810928],[2.444557,-1.770732,-4.931906,9.162672,6.519677,-4.442127,-7.365509,9.407265]]], dtype = "float64")#candidate|1740|(15, 16, 8)|const|float64
var_1741 = relay.var("var_1741", dtype = "float64", shape = (15, 16, 8))#candidate|1741|(15, 16, 8)|var|float64
bop_1742 = relay.floor_divide(const_1740.astype('float64'), relay.reshape(var_1741.astype('float64'), relay.shape_of(const_1740))) # shape=(15, 16, 8)
output = relay.Tuple([bop_1742,])
output2 = relay.Tuple([bop_1742,])
func_1755 = relay.Function([var_1741,], output)
mod['func_1755'] = func_1755
mod = relay.transform.InferType()(mod)
mutated_mod['func_1755'] = func_1755
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1756 = relay.var("var_1756", dtype = "float64", shape = (15, 16, 8))#candidate|1756|(15, 16, 8)|var|float64
func_1755_call = mutated_mod.get_global_var('func_1755')
call_1757 = func_1755_call(var_1756)
output = call_1757
func_1758 = relay.Function([var_1756], output)
mutated_mod['func_1758'] = func_1758
mutated_mod = relay.transform.InferType()(mutated_mod)
func_295_call = mod.get_global_var('func_295')
func_297_call = mutated_mod.get_global_var('func_297')
call_1783 = relay.TupleGetItem(func_295_call(), 2)
call_1784 = relay.TupleGetItem(func_297_call(), 2)
var_1802 = relay.var("var_1802", dtype = "bool", shape = (64, 9))#candidate|1802|(64, 9)|var|bool
bop_1803 = relay.subtract(call_1783.astype('float32'), var_1802.astype('float32')) # shape=(64, 9)
bop_1806 = relay.subtract(call_1784.astype('float32'), var_1802.astype('float32')) # shape=(64, 9)
uop_1814 = relay.atan(call_1783.astype('float32')) # shape=(64, 1)
uop_1816 = relay.atan(call_1784.astype('float32')) # shape=(64, 1)
bop_1817 = relay.multiply(uop_1814.astype('float64'), relay.reshape(call_1783.astype('float64'), relay.shape_of(uop_1814))) # shape=(64, 1)
bop_1820 = relay.multiply(uop_1816.astype('float64'), relay.reshape(call_1784.astype('float64'), relay.shape_of(uop_1816))) # shape=(64, 1)
output = relay.Tuple([bop_1803,bop_1817,])
output2 = relay.Tuple([bop_1806,bop_1820,])
func_1823 = relay.Function([var_1802,], output)
mod['func_1823'] = func_1823
mod = relay.transform.InferType()(mod)
var_1824 = relay.var("var_1824", dtype = "bool", shape = (64, 9))#candidate|1824|(64, 9)|var|bool
output = func_1823(var_1824)
func_1825 = relay.Function([var_1824], output)
mutated_mod['func_1825'] = func_1825
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1305_call = mod.get_global_var('func_1305')
func_1307_call = mutated_mod.get_global_var('func_1307')
call_1918 = relay.TupleGetItem(func_1305_call(), 0)
call_1919 = relay.TupleGetItem(func_1307_call(), 0)
func_1634_call = mod.get_global_var('func_1634')
func_1637_call = mutated_mod.get_global_var('func_1637')
var_1942 = relay.var("var_1942", dtype = "bool", shape = (64, 8))#candidate|1942|(64, 8)|var|bool
call_1941 = relay.TupleGetItem(func_1634_call(relay.reshape(var_1942.astype('bool'), [512, 1])), 2)
call_1943 = relay.TupleGetItem(func_1637_call(relay.reshape(var_1942.astype('bool'), [512, 1])), 2)
output = relay.Tuple([call_1918,call_1941,var_1942,])
output2 = relay.Tuple([call_1919,call_1943,var_1942,])
func_1949 = relay.Function([var_1942,], output)
mod['func_1949'] = func_1949
mod = relay.transform.InferType()(mod)
var_1950 = relay.var("var_1950", dtype = "bool", shape = (64, 8))#candidate|1950|(64, 8)|var|bool
output = func_1949(var_1950)
func_1951 = relay.Function([var_1950], output)
mutated_mod['func_1951'] = func_1951
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1227_call = mod.get_global_var('func_1227')
func_1229_call = mutated_mod.get_global_var('func_1229')
call_2040 = relay.TupleGetItem(func_1227_call(), 1)
call_2041 = relay.TupleGetItem(func_1229_call(), 1)
uop_2042 = relay.asinh(call_2040.astype('float64')) # shape=(4, 11, 7)
uop_2044 = relay.asinh(call_2041.astype('float64')) # shape=(4, 11, 7)
func_1823_call = mod.get_global_var('func_1823')
func_1825_call = mutated_mod.get_global_var('func_1825')
var_2054 = relay.var("var_2054", dtype = "bool", shape = (576,))#candidate|2054|(576,)|var|bool
call_2053 = relay.TupleGetItem(func_1823_call(relay.reshape(var_2054.astype('bool'), [64, 9])), 0)
call_2055 = relay.TupleGetItem(func_1825_call(relay.reshape(var_2054.astype('bool'), [64, 9])), 0)
func_1362_call = mod.get_global_var('func_1362')
func_1364_call = mutated_mod.get_global_var('func_1364')
call_2067 = relay.TupleGetItem(func_1362_call(), 0)
call_2068 = relay.TupleGetItem(func_1364_call(), 0)
func_959_call = mod.get_global_var('func_959')
func_963_call = mutated_mod.get_global_var('func_963')
var_2073 = relay.var("var_2073", dtype = "bool", shape = (256,))#candidate|2073|(256,)|var|bool
const_2074 = relay.const([[-2.814004],[6.241986],[-3.812250],[7.496451],[-7.567095],[0.031663],[4.417371],[-4.650494],[8.317109],[-3.279403],[-3.793534],[2.434687],[4.043104],[0.203843],[1.375330],[2.869164],[-5.126986],[0.935891],[0.488148],[6.366846],[0.459253],[3.095938],[3.410374],[-2.199379],[-5.652057],[-8.394960],[3.065180],[-3.150812],[9.568935],[-2.731856],[-0.260880],[-0.875902],[9.957490],[-1.762209],[-1.504383],[-3.981976],[-3.198956],[3.391104],[-5.088764],[-2.525307],[-9.582239],[7.375528],[-2.166010],[-3.373694],[-8.587548],[6.301363],[-3.562279],[8.007363],[4.145148],[-1.170060],[0.836022],[4.284052],[-2.745556],[7.387016],[-3.064257],[-4.327294],[3.750225],[-4.021764],[4.585018],[5.130488],[-9.929894],[3.331438],[-0.111685],[-8.523107],[-5.504447],[-4.263306],[4.122977],[6.490810],[-3.448347],[-7.625786],[9.805862],[3.657214],[2.337749],[-2.951282],[-2.535879],[-4.348290],[-8.464105],[8.309003],[-9.158339],[2.782497],[8.602658],[1.896389],[0.554072],[-6.592394],[7.766982],[5.731395],[1.467099],[3.158238],[-3.581552],[-6.128446],[1.740471],[4.648020],[-3.199749],[4.616346],[-5.871483],[3.782935],[-0.786791],[0.736333],[6.324921],[2.688818],[-7.984326],[3.777273],[8.555087],[-8.056301],[7.497005],[-0.002712],[1.577902],[-2.774476],[-3.174340],[2.576644],[-1.201783],[-9.196894],[0.520657],[1.343281],[-7.575233],[7.668641],[3.333971],[-9.272705],[-8.684487],[-7.813240],[5.091047]], dtype = "float64")#candidate|2074|(121, 1)|const|float64
call_2072 = relay.TupleGetItem(func_959_call(relay.reshape(var_2073.astype('bool'), [64, 4]), relay.reshape(const_2074.astype('float64'), [121,]), ), 3)
call_2075 = relay.TupleGetItem(func_963_call(relay.reshape(var_2073.astype('bool'), [64, 4]), relay.reshape(const_2074.astype('float64'), [121,]), ), 3)
bop_2089 = relay.power(uop_2042.astype('float64'), relay.reshape(call_2040.astype('float64'), relay.shape_of(uop_2042))) # shape=(4, 11, 7)
bop_2092 = relay.power(uop_2044.astype('float64'), relay.reshape(call_2041.astype('float64'), relay.shape_of(uop_2044))) # shape=(4, 11, 7)
output = relay.Tuple([call_2053,var_2054,call_2067,call_2072,var_2073,const_2074,bop_2089,])
output2 = relay.Tuple([call_2055,var_2054,call_2068,call_2075,var_2073,const_2074,bop_2092,])
func_2094 = relay.Function([var_2054,var_2073,], output)
mod['func_2094'] = func_2094
mod = relay.transform.InferType()(mod)
var_2095 = relay.var("var_2095", dtype = "bool", shape = (576,))#candidate|2095|(576,)|var|bool
var_2096 = relay.var("var_2096", dtype = "bool", shape = (256,))#candidate|2096|(256,)|var|bool
output = func_2094(var_2095,var_2096,)
func_2097 = relay.Function([var_2095,var_2096,], output)
mutated_mod['func_2097'] = func_2097
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1227_call = mod.get_global_var('func_1227')
func_1229_call = mutated_mod.get_global_var('func_1229')
call_2105 = relay.TupleGetItem(func_1227_call(), 0)
call_2106 = relay.TupleGetItem(func_1229_call(), 0)
func_391_call = mod.get_global_var('func_391')
func_392_call = mutated_mod.get_global_var('func_392')
call_2137 = func_391_call()
call_2138 = func_391_call()
output = relay.Tuple([call_2105,call_2137,])
output2 = relay.Tuple([call_2106,call_2138,])
func_2146 = relay.Function([], output)
mod['func_2146'] = func_2146
mod = relay.transform.InferType()(mod)
mutated_mod['func_2146'] = func_2146
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2146_call = mutated_mod.get_global_var('func_2146')
call_2147 = func_2146_call()
output = call_2147
func_2148 = relay.Function([], output)
mutated_mod['func_2148'] = func_2148
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1362_call = mod.get_global_var('func_1362')
func_1364_call = mutated_mod.get_global_var('func_1364')
call_2310 = relay.TupleGetItem(func_1362_call(), 0)
call_2311 = relay.TupleGetItem(func_1364_call(), 0)
var_2313 = relay.var("var_2313", dtype = "float64", shape = (6, 7, 8))#candidate|2313|(6, 7, 8)|var|float64
bop_2314 = relay.maximum(call_2310.astype('int16'), var_2313.astype('int16')) # shape=(6, 7, 8)
bop_2317 = relay.maximum(call_2311.astype('int16'), var_2313.astype('int16')) # shape=(6, 7, 8)
output = bop_2314
output2 = bop_2317
func_2331 = relay.Function([var_2313,], output)
mod['func_2331'] = func_2331
mod = relay.transform.InferType()(mod)
var_2332 = relay.var("var_2332", dtype = "float64", shape = (6, 7, 8))#candidate|2332|(6, 7, 8)|var|float64
output = func_2331(var_2332)
func_2333 = relay.Function([var_2332], output)
mutated_mod['func_2333'] = func_2333
mutated_mod = relay.transform.InferType()(mutated_mod)
func_439_call = mod.get_global_var('func_439')
func_440_call = mutated_mod.get_global_var('func_440')
call_2408 = func_439_call()
call_2409 = func_439_call()
output = relay.Tuple([call_2408,])
output2 = relay.Tuple([call_2409,])
func_2414 = relay.Function([], output)
mod['func_2414'] = func_2414
mod = relay.transform.InferType()(mod)
mutated_mod['func_2414'] = func_2414
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2414_call = mutated_mod.get_global_var('func_2414')
call_2415 = func_2414_call()
output = call_2415
func_2416 = relay.Function([], output)
mutated_mod['func_2416'] = func_2416
mutated_mod = relay.transform.InferType()(mutated_mod)
func_391_call = mod.get_global_var('func_391')
func_392_call = mutated_mod.get_global_var('func_392')
call_2425 = func_391_call()
call_2426 = func_391_call()
func_439_call = mod.get_global_var('func_439')
func_440_call = mutated_mod.get_global_var('func_440')
call_2428 = func_439_call()
call_2429 = func_439_call()
output = relay.Tuple([call_2425,call_2428,])
output2 = relay.Tuple([call_2426,call_2429,])
func_2430 = relay.Function([], output)
mod['func_2430'] = func_2430
mod = relay.transform.InferType()(mod)
output = func_2430()
func_2431 = relay.Function([], output)
mutated_mod['func_2431'] = func_2431
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2457 = relay.const([[[4.092589,-8.305855,7.515006,6.480287,-8.093218,-6.506263,-9.752027,0.506992,-4.130477,-2.338713,8.905278],[-5.265597,1.986743,8.994276,-1.597922,-7.518267,3.394738,-8.754347,7.232476,3.175188,7.075052,5.625277],[-9.480009,6.325303,8.412537,-8.417134,-9.893652,-4.490511,-5.719455,5.739534,-0.458201,-8.806280,-5.825685],[5.835566,4.000661,-2.507480,-2.839343,-0.476876,-9.654528,-0.775311,4.230797,-9.664349,5.268435,-9.656501],[-9.035662,-1.936059,5.238084,5.311343,7.712766,2.823505,6.205918,-5.513067,1.262652,-5.800600,-6.934938],[5.591059,-9.158237,-8.221469,2.812020,9.294206,-0.117661,-6.116221,-6.515204,4.125409,-3.409716,-2.477225],[-1.536142,-7.797160,6.192239,-7.883257,0.952312,-6.138578,6.551124,8.735464,3.264777,7.876355,3.006830],[7.705011,6.444566,2.325823,6.559622,9.264529,-4.846007,-8.401962,9.773998,-7.711389,-4.215303,-3.466734]],[[4.779937,-9.830744,-8.686474,-4.349959,-2.920546,8.317013,-0.667003,6.687396,7.426741,-8.614002,-9.574180],[1.893036,6.364532,-3.455150,-0.540588,0.663045,3.619407,-8.248942,2.488463,0.231116,-7.657858,3.487947],[2.037969,7.544323,-0.714944,4.283719,-7.456520,-2.007675,-8.771051,3.197024,8.121326,-8.084397,1.345017],[-1.423245,0.087563,-8.768143,-2.249753,-8.241164,-5.176946,-4.417763,1.432211,-1.901145,6.154226,1.875741],[6.036084,-4.257496,-8.958295,6.464461,-1.696212,-5.594764,6.784930,1.138594,2.513078,-6.685362,5.694923],[-9.360241,-8.932648,-5.971314,8.975959,3.713230,8.710149,7.609198,-6.248472,8.775618,-6.657494,-7.993006],[-0.330137,9.147754,4.382342,5.424887,5.869808,-2.186020,-4.357129,2.363668,-3.243145,7.402945,-1.826623],[9.382956,6.020922,3.787107,5.362778,-4.401090,-0.632374,5.744579,1.265565,-2.441249,-0.839786,-1.134887]],[[-8.338032,-4.603314,-5.578000,-1.927528,-3.022617,2.047485,-0.190495,0.791624,-3.019998,6.543688,5.359945],[-0.911379,4.497915,1.959430,2.038680,6.003893,1.895470,2.726698,4.040577,8.118834,1.168769,8.721430],[5.778974,0.269805,-7.939062,-3.358122,6.002916,-8.309600,-2.387344,-3.758996,7.202101,6.689736,6.850592],[-2.009928,-4.128115,-3.213703,-0.965480,3.638367,-2.344792,1.776227,8.250126,5.802619,3.083455,1.070295],[6.512372,6.243729,1.537775,-5.879760,4.185043,1.269307,-3.614266,-7.749632,-4.351570,-2.131331,-4.298922],[1.893502,-9.372212,9.141654,4.249307,6.398405,-2.055739,0.486563,7.398239,1.934227,8.938008,-8.958521],[-3.171436,-2.921279,-8.653738,-7.380773,3.760483,-8.628308,-3.865637,0.795479,-4.959556,-7.335601,6.332809],[6.749389,2.192713,-0.827486,8.520304,-0.027240,2.908161,-0.911142,-0.720243,-0.792421,1.181219,2.738953]],[[-8.938588,0.828086,0.162746,-6.226170,6.166241,3.868130,-2.588606,6.323192,-9.523713,7.120730,1.630777],[6.893642,-0.586381,0.212267,-5.356056,4.779539,2.184198,4.192545,7.217730,3.974426,7.161138,3.965188],[-2.515536,-4.197346,1.213901,-9.909923,2.620974,-2.825952,-4.492441,9.241242,-6.737960,6.714626,0.977965],[-0.882247,-9.719711,-4.898878,-1.500331,5.248381,-3.373192,8.478509,-6.212245,-4.327864,8.623105,1.547672],[-1.973727,-8.833231,-5.189910,-9.788267,-5.210409,-3.230624,3.164544,8.857642,-0.086811,-2.691747,-5.911293],[-9.142060,-9.245715,-1.884045,0.406472,7.919300,3.181773,-5.667016,8.867561,4.556297,7.325406,9.794324],[-4.071491,-7.508213,0.876260,-2.896957,-0.984288,-1.926992,7.849121,-6.123088,4.102815,1.575033,1.128014],[-1.425387,-8.259630,4.747135,0.323980,-7.079611,0.614482,-4.082331,-2.456125,-4.501964,-3.351276,1.100734]]], dtype = "float64")#candidate|2457|(4, 8, 11)|const|float64
uop_2458 = relay.log(const_2457.astype('float64')) # shape=(4, 8, 11)
func_1718_call = mod.get_global_var('func_1718')
func_1719_call = mutated_mod.get_global_var('func_1719')
call_2461 = relay.TupleGetItem(func_1718_call(), 0)
call_2462 = relay.TupleGetItem(func_1719_call(), 0)
uop_2476 = relay.exp(uop_2458.astype('float64')) # shape=(4, 8, 11)
output = relay.Tuple([call_2461,uop_2476,])
output2 = relay.Tuple([call_2462,uop_2476,])
func_2482 = relay.Function([], output)
mod['func_2482'] = func_2482
mod = relay.transform.InferType()(mod)
mutated_mod['func_2482'] = func_2482
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2482_call = mutated_mod.get_global_var('func_2482')
call_2483 = func_2482_call()
output = call_2483
func_2484 = relay.Function([], output)
mutated_mod['func_2484'] = func_2484
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2579 = relay.var("var_2579", dtype = "float64", shape = (1, 8, 15))#candidate|2579|(1, 8, 15)|var|float64
var_2580 = relay.var("var_2580", dtype = "float64", shape = (13, 8, 15))#candidate|2580|(13, 8, 15)|var|float64
bop_2581 = relay.floor_divide(var_2579.astype('float64'), var_2580.astype('float64')) # shape=(13, 8, 15)
func_1755_call = mod.get_global_var('func_1755')
func_1758_call = mutated_mod.get_global_var('func_1758')
var_2594 = relay.var("var_2594", dtype = "float64", shape = (96, 20))#candidate|2594|(96, 20)|var|float64
call_2593 = relay.TupleGetItem(func_1755_call(relay.reshape(var_2594.astype('float64'), [15, 16, 8])), 0)
call_2595 = relay.TupleGetItem(func_1758_call(relay.reshape(var_2594.astype('float64'), [15, 16, 8])), 0)
output = relay.Tuple([bop_2581,call_2593,var_2594,])
output2 = relay.Tuple([bop_2581,call_2595,var_2594,])
func_2596 = relay.Function([var_2579,var_2580,var_2594,], output)
mod['func_2596'] = func_2596
mod = relay.transform.InferType()(mod)
var_2597 = relay.var("var_2597", dtype = "float64", shape = (1, 8, 15))#candidate|2597|(1, 8, 15)|var|float64
var_2598 = relay.var("var_2598", dtype = "float64", shape = (13, 8, 15))#candidate|2598|(13, 8, 15)|var|float64
var_2599 = relay.var("var_2599", dtype = "float64", shape = (96, 20))#candidate|2599|(96, 20)|var|float64
output = func_2596(var_2597,var_2598,var_2599,)
func_2600 = relay.Function([var_2597,var_2598,var_2599,], output)
mutated_mod['func_2600'] = func_2600
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2482_call = mod.get_global_var('func_2482')
func_2484_call = mutated_mod.get_global_var('func_2484')
call_2627 = relay.TupleGetItem(func_2482_call(), 0)
call_2628 = relay.TupleGetItem(func_2484_call(), 0)
func_2482_call = mod.get_global_var('func_2482')
func_2484_call = mutated_mod.get_global_var('func_2484')
call_2666 = relay.TupleGetItem(func_2482_call(), 0)
call_2667 = relay.TupleGetItem(func_2484_call(), 0)
bop_2673 = relay.logical_or(call_2666.astype('bool'), relay.reshape(call_2627.astype('bool'), relay.shape_of(call_2666))) # shape=(16, 1, 4)
bop_2676 = relay.logical_or(call_2667.astype('bool'), relay.reshape(call_2628.astype('bool'), relay.shape_of(call_2667))) # shape=(16, 1, 4)
output = relay.Tuple([bop_2673,])
output2 = relay.Tuple([bop_2676,])
func_2677 = relay.Function([], output)
mod['func_2677'] = func_2677
mod = relay.transform.InferType()(mod)
mutated_mod['func_2677'] = func_2677
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2677_call = mutated_mod.get_global_var('func_2677')
call_2678 = func_2677_call()
output = call_2678
func_2679 = relay.Function([], output)
mutated_mod['func_2679'] = func_2679
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1017_call = mod.get_global_var('func_1017')
func_1018_call = mutated_mod.get_global_var('func_1018')
call_2770 = relay.TupleGetItem(func_1017_call(), 1)
call_2771 = relay.TupleGetItem(func_1018_call(), 1)
output = relay.Tuple([call_2770,])
output2 = relay.Tuple([call_2771,])
func_2782 = relay.Function([], output)
mod['func_2782'] = func_2782
mod = relay.transform.InferType()(mod)
output = func_2782()
func_2783 = relay.Function([], output)
mutated_mod['func_2783'] = func_2783
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1017_call = mod.get_global_var('func_1017')
func_1018_call = mutated_mod.get_global_var('func_1018')
call_2807 = relay.TupleGetItem(func_1017_call(), 1)
call_2808 = relay.TupleGetItem(func_1018_call(), 1)
func_2782_call = mod.get_global_var('func_2782')
func_2783_call = mutated_mod.get_global_var('func_2783')
call_2809 = relay.TupleGetItem(func_2782_call(), 0)
call_2810 = relay.TupleGetItem(func_2783_call(), 0)
output = relay.Tuple([call_2807,call_2809,])
output2 = relay.Tuple([call_2808,call_2810,])
func_2814 = relay.Function([], output)
mod['func_2814'] = func_2814
mod = relay.transform.InferType()(mod)
mutated_mod['func_2814'] = func_2814
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2814_call = mutated_mod.get_global_var('func_2814')
call_2815 = func_2814_call()
output = call_2815
func_2816 = relay.Function([], output)
mutated_mod['func_2816'] = func_2816
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1305_call = mod.get_global_var('func_1305')
func_1307_call = mutated_mod.get_global_var('func_1307')
call_2845 = relay.TupleGetItem(func_1305_call(), 1)
call_2846 = relay.TupleGetItem(func_1307_call(), 1)
func_1684_call = mod.get_global_var('func_1684')
func_1686_call = mutated_mod.get_global_var('func_1686')
call_2847 = relay.TupleGetItem(func_1684_call(), 1)
call_2848 = relay.TupleGetItem(func_1686_call(), 1)
var_2849 = relay.var("var_2849", dtype = "float32", shape = (64, 8))#candidate|2849|(64, 8)|var|float32
bop_2850 = relay.mod(call_2845.astype('float64'), relay.reshape(var_2849.astype('float64'), relay.shape_of(call_2845))) # shape=(64, 8)
bop_2853 = relay.mod(call_2846.astype('float64'), relay.reshape(var_2849.astype('float64'), relay.shape_of(call_2846))) # shape=(64, 8)
func_295_call = mod.get_global_var('func_295')
func_297_call = mutated_mod.get_global_var('func_297')
call_2864 = relay.TupleGetItem(func_295_call(), 1)
call_2865 = relay.TupleGetItem(func_297_call(), 1)
output = relay.Tuple([call_2847,bop_2850,call_2864,])
output2 = relay.Tuple([call_2848,bop_2853,call_2865,])
func_2866 = relay.Function([var_2849,], output)
mod['func_2866'] = func_2866
mod = relay.transform.InferType()(mod)
var_2867 = relay.var("var_2867", dtype = "float32", shape = (64, 8))#candidate|2867|(64, 8)|var|float32
output = func_2866(var_2867)
func_2868 = relay.Function([var_2867], output)
mutated_mod['func_2868'] = func_2868
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2146_call = mod.get_global_var('func_2146')
func_2148_call = mutated_mod.get_global_var('func_2148')
call_2870 = relay.TupleGetItem(func_2146_call(), 0)
call_2871 = relay.TupleGetItem(func_2148_call(), 0)
func_1823_call = mod.get_global_var('func_1823')
func_1825_call = mutated_mod.get_global_var('func_1825')
var_2883 = relay.var("var_2883", dtype = "bool", shape = (12, 48))#candidate|2883|(12, 48)|var|bool
call_2882 = relay.TupleGetItem(func_1823_call(relay.reshape(var_2883.astype('bool'), [64, 9])), 0)
call_2884 = relay.TupleGetItem(func_1825_call(relay.reshape(var_2883.astype('bool'), [64, 9])), 0)
output = relay.Tuple([call_2870,call_2882,var_2883,])
output2 = relay.Tuple([call_2871,call_2884,var_2883,])
func_2891 = relay.Function([var_2883,], output)
mod['func_2891'] = func_2891
mod = relay.transform.InferType()(mod)
var_2892 = relay.var("var_2892", dtype = "bool", shape = (12, 48))#candidate|2892|(12, 48)|var|bool
output = func_2891(var_2892)
func_2893 = relay.Function([var_2892], output)
mutated_mod['func_2893'] = func_2893
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1260_call = mod.get_global_var('func_1260')
func_1261_call = mutated_mod.get_global_var('func_1261')
call_2898 = relay.TupleGetItem(func_1260_call(), 1)
call_2899 = relay.TupleGetItem(func_1261_call(), 1)
func_1718_call = mod.get_global_var('func_1718')
func_1719_call = mutated_mod.get_global_var('func_1719')
call_2909 = relay.TupleGetItem(func_1718_call(), 0)
call_2910 = relay.TupleGetItem(func_1719_call(), 0)
func_2331_call = mod.get_global_var('func_2331')
func_2333_call = mutated_mod.get_global_var('func_2333')
const_2924 = relay.const([-9.642363,-4.471747,2.757449,-5.188774,0.709464,3.286787,5.639727,0.805434,6.680953,8.743877,9.005456,5.247988,-7.639370,6.741781,-8.769058,8.912928,5.326111,0.317881,-3.247180,4.332586,-5.819147,6.874558,-4.860874,2.876767,7.177500,8.031891,0.897648,5.695816,4.294008,2.740332,2.707369,0.308896,2.760853,9.319214,-4.587824,3.495564,-1.050799,-0.180094,3.644203,-1.734826,-6.629292,-6.304222,6.447901,-5.382740,-8.183270,-1.059348,-2.183002,2.960188,-0.276694,-8.716071,0.952052,2.049913,-4.732126,-8.932364,5.255515,-2.608769,-1.453215,7.417440,-9.184459,-3.665439,-8.476558,-0.511647,-5.487233,-8.620119,-1.474919,-5.425972,-3.766109,8.571294,5.262024,-2.808487,8.127961,7.319808,0.459477,5.191004,-3.449615,9.709979,-6.399568,8.886672,9.168597,9.723457,-9.876776,1.873192,-8.412166,3.603513,-4.516408,-5.503279,-7.784009,5.239451,2.528295,1.917388,-2.582951,-8.976439,-7.712658,-9.171844,8.869197,-3.770935,4.493530,-8.457778,-8.306864,4.595972,0.701179,-6.994382,3.833295,-4.074160,-4.771045,-0.312382,-7.513425,1.747234,2.765815,-7.984648,-9.736581,-5.453576,-5.122669,9.725158,5.484083,8.467329,-8.519177,-1.703599,2.674581,-0.622363,3.918305,-6.365614,3.475483,-1.108586,9.219084,7.751329,8.116403,2.578323,-6.048666,2.914840,-3.848520,4.967438,-0.651417,-5.090624,-6.743048,-3.076636,-3.296282,4.727891,-5.893165,-1.757002,-3.481772,2.345674,5.633102,8.785575,5.490705,0.111628,7.225078,7.007909,7.868342,8.431063,-5.130869,5.088810,-8.478983,2.820862,-5.364228,2.142605,8.007850,3.921478,0.988645,3.968146,2.375575,-1.276036,7.299327,-5.242879,-5.694665,-7.148085,0.579094,3.642929,-9.629526,5.253457,-8.713035,1.245482,7.762782,-5.164993,3.975634,-7.233377,8.756546,4.420757,-2.739752,6.615724,2.482461,2.180357,2.925296,-9.742286,3.835029,-3.732611,-8.961690,-9.408916,-3.117186,5.528372,-2.537292,-6.024147,-5.817046,-4.940028,-0.028382,7.950982,9.762299,-3.718055,0.350560,-3.003209,-6.779298,-5.174239,-5.150234,9.215175,-5.310021,-3.627245,-3.846923,-5.343166,-5.828019,9.921050,-9.831035,-2.521834,8.443462,-2.614953,0.711829,-6.761810,1.852151,2.568685,7.724084,8.534612,9.660265,-9.944567,-8.533163,-7.487307,2.355211,2.238416,9.574885,3.617648,2.875898,8.122792,-0.830299,-2.628284,3.432143,2.430342,-8.567924,-7.051952,-2.775388,2.828116,7.405001,2.909304,5.529158,-9.393166,-3.463398,-3.814011,9.858735,-9.864475,2.423879,8.994133,-7.584998,9.711050,5.933008,-3.632057,-2.335118,0.451860,-8.347964,-6.618718,0.668965,-5.435811,-0.894138,1.268255,-4.993866,1.166641,4.977302,-6.507558,8.967738,-6.128063,2.560873,-9.444627,1.551459,9.489088,-4.644633,7.631326,-0.505868,7.089889,-9.848710,-6.879465,-4.815312,-1.118663,8.146002,-0.200224,-5.728863,7.063603,2.681017,8.780009,5.757672,-0.554804,-8.843300,-2.520222,1.693603,8.637413,-2.625830,9.495816,5.563866,-9.692126,-1.148319,2.243081,-3.177592,8.862054,-4.930007,-2.405985,4.647438,2.495936,-9.221480,7.254942,1.353798,-1.877206,-5.796476,5.429783,3.809582,-4.887899,-3.181971,3.453848,3.360190,-8.477302,7.705465,3.628495,-7.637457,8.688019,-2.723221,-3.251899,2.822525,-2.937298,-8.384747,-7.320708,3.326600,-5.887413,-5.643023,-7.903556,-2.260172,-1.808022,0.704170,-7.590449,-4.476058,1.608617,-6.259567,0.314509], dtype = "float64")#candidate|2924|(336,)|const|float64
call_2923 = func_2331_call(relay.reshape(const_2924.astype('float64'), [6, 7, 8]))
call_2925 = func_2331_call(relay.reshape(const_2924.astype('float64'), [6, 7, 8]))
func_2596_call = mod.get_global_var('func_2596')
func_2600_call = mutated_mod.get_global_var('func_2600')
const_2931 = relay.const([[-7.359360,8.714668,9.126060,8.650253],[7.342043,-2.582341,6.475301,-2.152396],[-6.413973,-0.352823,7.042776,-7.139533],[4.627074,-7.995902,3.252105,7.107007],[-7.419019,-7.084165,7.376527,7.529921],[5.320551,4.635661,-5.772806,-2.330396],[5.696427,9.880358,1.157600,5.195613],[0.584845,-9.649145,-6.145975,4.580816],[4.534284,-1.085844,5.885152,2.649375],[4.865758,6.064217,-7.763353,4.882881],[-7.644822,2.019882,-5.693226,-7.419151],[-3.134759,6.428494,-2.070116,5.070154],[-5.863498,-5.059216,-9.797253,-6.774528],[-1.890376,6.162649,-7.744764,5.786407],[4.698382,-4.355023,9.682626,-0.375404],[9.243914,-5.141349,-5.147728,1.529177],[2.113101,-9.430751,4.432704,8.597891],[-4.824679,4.183525,8.083873,1.397894],[8.471336,4.909936,-0.550608,-0.019903],[8.100637,-8.990103,-5.221020,-5.294895],[0.245133,8.885495,4.118975,5.513556],[7.641207,-6.968479,3.205873,-3.354404],[1.914126,8.878055,4.394418,-5.435802],[-3.376738,-6.731756,-5.187007,-8.032571],[3.327348,0.830260,-0.283022,-7.839237],[7.919563,0.133473,-1.804748,1.727331],[9.589828,9.827963,-7.745423,3.505858],[-8.353857,3.151366,-5.461930,1.154048],[-7.904458,-8.422307,4.491271,-6.569372],[-8.161751,4.023944,0.324567,-1.459788]], dtype = "float64")#candidate|2931|(30, 4)|const|float64
const_2932 = relay.const([6.019987,-4.233068,-8.259813,9.804341,4.512301,-1.606313,1.441857,-9.662320,7.925242,3.917053,-9.675253,-8.929583,0.008744,-6.006575,8.060464,-1.362171,-6.964844,-8.229798,-4.313075,5.464104,-4.598527,5.970997,4.430779,-1.740871,6.632555,-0.742007,-4.022391,5.757970,3.990364,-9.712592,-5.960587,-8.319041,8.203027,3.335280,-8.117275,9.303335,4.126695,-1.593683,6.643680,7.835027,-4.180105,-7.414095,4.488161,-4.354213,-8.653761,1.368876,5.940347,0.140862,-0.399103,-6.774510,-0.025483,-2.696199,9.292424,-0.100420,0.599518,5.422213,9.601223,3.918668,7.030962,6.703450,-3.682009,-2.168477,-7.562435,7.696503,4.059850,0.879586,1.924906,4.136882,-8.190508,7.770492,4.794243,4.077355,0.084952,5.128050,-5.164038,-8.711301,9.613759,-9.826392,-0.587209,3.635813,-4.918227,8.765866,-8.961073,-9.621966,-5.071557,-8.405074,-0.768797,-4.626380,-7.384571,-8.654521,4.738289,-3.305385,-5.910046,-3.541928,-0.943595,-0.380727,4.081564,-9.967354,-1.610950,-9.400838,8.415285,-3.979675,3.096073,5.997478,4.670332,-1.659885,-2.900076,8.609908,-0.158812,8.031084,7.031418,3.701290,-0.767407,-7.588931,-6.361020,5.500716,-2.318704,3.585071,1.597784,3.352316,-9.664050,1.330630,-7.549364,4.723617,-5.829969,1.234294,-9.167610,-6.051158,6.603613,1.568933,-1.029331,2.076450,1.835578,-5.160003,4.673370,3.546302,8.397251,-7.052138,3.663319,-5.597948,-5.128163,-7.738248,-9.804446,3.307251,5.889235,1.945959,-1.493638,-9.490599,3.592494,-4.556236,9.404576,7.052525,-5.035521,-4.457490,1.303237,0.104557,4.589725,2.420706,9.247659,4.784607,7.966985,-8.351836,7.379838,2.124970,0.463910,8.127018,2.091364,5.303393,-5.005207,-2.879107,0.635584,8.562462,7.996215,-5.330203,-0.137373,9.495136,4.147441,9.840782,9.415062,7.028025,-9.891504,9.296934,3.977526,3.317033,-7.489955,-3.603791,0.489473,-4.652026,-0.273701,1.436685,-8.902822,-9.762379,-0.796421,-6.177375,4.037894,-9.795327,-4.855283,1.228322,3.680386,0.123663,-0.914437,8.163901,-0.671589,-8.678998,-9.179013,0.317666,2.590499,-1.188897,3.729292,3.800947,8.340169,-6.636220,5.771054,6.089111,-3.447993,-5.730437,-4.339539,-6.676019,-4.737663,5.785772,8.940171,0.069629,8.328412,-0.232934,4.261275,4.642381,-4.372435,-8.582830,6.454721,-6.238114,1.824830,1.286211,-3.833475,-5.099858,-7.270731,2.416275,-9.229660,-6.191268,6.263519,-3.377350,-5.588280,0.190536,9.399649,-8.945208,5.345974,-7.235872,-5.764079,5.624916,9.758264,3.619169,9.217089,6.511457,0.611816,0.490962,5.879417,1.444467,8.026801,-5.573699,1.659037,-2.245994,6.800356,1.183146,-6.614119,-8.610212,-4.418310,7.946257,-1.618143,9.122248,0.130554,-8.306943,-9.120625,-6.252944,-2.718703,-3.677286,-7.008557,5.206521,5.749484,2.103200,8.329411,6.861258,8.811424,1.956515,-0.685860,9.300574,-0.134688,-9.094114,-0.479440,-7.136441,2.804015,-1.849834,0.992428,8.774208,-6.338541,-9.048805,-0.150853,3.723422,9.285100,0.820109,5.482744,0.466865,8.316040,-7.832695,-1.427419,-1.288007,1.688583,4.410963,-7.354988,7.982741,1.857976,-7.118752,4.402956,7.352637,4.082414,-8.900392,-1.346155,-0.689434,6.499232,2.152515,6.028311,7.613383,-8.059241,-0.842609,2.601358,9.061110,7.607784,-6.838857,8.157460,7.943057,5.879775,9.902439,6.576600,0.900602,-7.654952,0.729341,-3.939084,-4.753862,8.997494,-5.948882,-1.507770,-3.787551,3.305585,-9.777046,-4.540574,0.972684,-7.583334,3.306723,-5.512189,-9.828536,8.862256,2.372142,8.976853,-8.903337,-4.514280,8.614908,-2.586493,-4.499587,6.923388,-0.517896,2.812211,9.666672,-8.220676,7.498090,1.926050,7.505671,2.432932,-2.652532,-1.060786,-4.477274,9.568520,2.428718,7.289266,-3.719929,9.614199,-5.319041,-9.229937,-5.073940,8.728507,-7.438913,2.640688,7.798910,-2.741681,7.832882,5.540117,3.792269,-3.790613,-9.672553,-1.999246,-6.222976,-6.376003,-5.622750,-9.383231,4.647496,4.585928,-1.743875,-6.490580,3.193711,6.191840,5.837982,-0.962656,-2.251400,-5.732903,-3.283176,3.514462,-8.939973,-7.607364,-9.790251,8.306702,-3.526298,8.218734,1.606196,-4.291962,-2.850704,-5.620858,-0.274706,-3.948577,9.733426,-7.087998,-4.449727,-2.394118,9.702559,3.505433,6.747158,7.056480,2.617068,-0.517626,-0.506788,-4.209683,-8.093119,6.324008,1.598815,1.593314,-3.007124,4.238347,7.365089,6.888370,-8.047015,0.131632,5.353221,4.752162,1.288051,5.809657,-2.486120,2.826271,-5.646418,-6.852779,-2.446688,-8.906251,8.438075,7.981333,5.986234,4.950569,-9.074507,6.083833,3.886280,-9.061334,-0.696415,1.092997,2.196975,-5.896052,6.550374,-3.166664,-3.529958,-3.998690,-3.238584,9.102377,-5.080335,5.385543,8.766209,-6.585449,0.751679,1.094851,-1.774811,-9.693985,0.454276,-7.456080,7.566713,4.765948,8.738471,4.901975,9.851297,-4.897826,8.225231,-5.051339,-9.303809,-5.099950,-8.641881,-2.564839,-8.510456,-2.249262,8.018489,-9.790331,1.950230,-8.070691,2.755632,-0.970005,-2.454852,-5.799445,-0.145615,-8.053510,9.136978,-3.850400,5.142091,-5.882351,-1.353910,2.033401,0.087830,-5.300811,5.066345,-5.254069,8.733056,-0.369877,3.279270,7.393687,6.094441,-0.518915,-9.393802,-8.558026,5.992040,8.686040,-5.125754,6.576176,-0.148906,-4.424314,7.484287,-0.646443,-4.866160,-4.763569,9.975649,0.974572,-2.569910,4.728668,1.479991,-8.878222,4.117755,-6.160445,-5.718409,2.418459,9.375922,9.070432,-2.285072,5.958247,-8.404222,-4.291979,-2.591605,-6.759540,-7.077321,6.502208,-9.463212,-9.224635,-4.732141,1.849341,2.259045,6.201997,-1.231032,8.458976,7.161906,8.727003,-3.169724,5.213598,-9.446001,2.621720,-3.847767,-8.354347,-1.634557,-5.513733,7.465451,-9.275838,-7.962464,8.283036,-3.820950,-0.747377,-7.315900,5.506474,5.605652,1.459482,-6.794748,-8.877414,5.283844,2.821419,-6.484480,-3.760416,3.437114,-8.906425,2.053283,9.966116,-5.029691,9.182910,6.147302,0.041337,2.412019,-3.589768,-0.908703,-0.958410,7.554427,8.795635,9.033988,1.136202,-5.800476,8.631326,-6.481258,6.086259,-9.904455,7.344009,4.461516,-1.234606,7.902173,8.550255,-9.184379,0.536035,5.665499,9.005972,2.020608,-2.190805,-9.344750,9.742879,-7.690341,0.336582,6.944588,-4.617552,1.148118,8.446309,-4.975247,-4.553456,6.603390,-2.628950,8.505768,5.434658,6.032955,-3.647005,9.228293,-9.212869,8.972852,-5.940272,-1.560915,7.161209,-6.997380,-9.238359,0.538399,9.613480,-3.072035,-7.534838,3.948322,-7.502642,6.610387,-2.672572,-6.002981,-3.508167,-3.616370,-2.500495,9.833263,-3.751725,4.946481,-4.251247,-3.310480,4.215270,-9.385969,-5.559063,1.365152,-8.339154,0.232965,-3.870353,2.438138,0.496277,0.649981,-1.134599,-0.340377,-2.834806,4.491407,-0.483982,-3.515348,-3.757415,3.839562,-5.693951,-8.287421,0.522297,7.621681,5.856769,-1.059651,-9.746174,4.055864,2.355936,-2.048420,7.435829,-7.651259,0.811383,0.610352,2.065029,-0.806026,1.338609,-8.631765,-1.086322,-9.269695,-6.070972,5.709681,4.133401,1.101825,-3.457289,-8.721158,1.157026,4.289214,-3.903497,5.799355,-9.886158,9.879055,-0.336921,-8.881009,-6.692672,-9.706716,-2.924739,2.439576,-6.473445,-5.673379,-5.528172,-0.734542,6.134003,-9.277464,-6.098713,-8.842786,4.211009,4.791177,8.835657,8.904705,-4.595103,9.398614,4.233255,-0.297936,9.944152,-9.700717,-7.008642,-6.857773,-3.332239,1.362685,-3.061861,7.735109,7.387855,3.826130,4.399579,-9.024278,-1.593417,-6.048110,2.874641,-7.496934,6.019077,-4.954037,2.945052,7.005845,-5.803917,0.480082,-1.422953,-0.141097,8.687271,9.652258,-0.859637,-8.555576,4.542465,-9.842942,-0.395474,6.898527,1.958614,3.629310,-8.670084,3.586052,8.675747,6.797526,6.538139,4.485623,9.380946,1.372197,1.591304,7.820599,-1.131695,2.384019,-7.299817,-9.758530,-5.315664,-7.923982,6.279110,7.528592,-5.327602,-5.460136,4.693855,-2.198064,-3.905422,-0.156289,-2.498464,-3.700934,-6.936948,9.067189,5.407715,-6.728663,7.160349,-0.642211,-2.909353,7.677613,7.744664,2.390211,5.101372,7.952713,4.645138,7.974505,6.947080,0.367281,1.276377,-3.240908,-8.676114,2.662172,-2.515487,-7.677924,8.073612,3.361965,-3.367129,9.359867,1.765090,9.071132,2.363075,-7.371858,4.780656,-8.291151,-7.833179,2.413623,9.237503,-8.270875,-5.827497,4.811707,-5.447405,-3.514269,3.351208,-4.472803,3.386822,0.462653,4.491884,5.215917,5.297150,7.773705,5.929853,1.679919,6.491348,-1.053190,-2.195870,-5.129849,-0.798594,3.922452,-3.429267,-3.119841,-4.242611,-9.833197,9.982346,-1.055386,1.817200,-3.760768,-2.291364,-6.266447,0.830235,3.190707,-5.030278,-5.332977,0.204243,-7.400116,-9.478064,3.733793,-7.774542,-1.074974,9.596380,4.718560,-9.540677,9.687795,8.944115,9.020542,-6.969391,-5.902644,-4.209070,-6.430628,3.858550,1.497134,7.221218,-4.725970,0.807466,-1.671893,5.414189,7.175784,7.143337,-6.878315,-3.209751,-5.341791,-0.266473,9.073240,9.251171,-8.144819,-6.996801,-4.586405,-2.374323,-3.940231,5.397417,2.752990,-3.646201,1.872485,8.099054,-8.682347,0.880419,5.576492,0.220564,-9.021677,-6.170420,1.945169,-5.279494,-8.351606,-2.490482,-2.188434,7.882516,-0.263296,0.886668,-6.600606,0.716954,-6.211255,6.744027,0.858721,6.948221,5.975116,-1.930322,-8.773832,7.480990,-6.434013,0.943363,7.437231,-8.148010,-0.225813,5.685954,-4.752017,7.518344,3.759471,-0.444491,-5.506224,-1.572891,0.401696,-4.627301,-6.623787,6.527242,-4.491352,3.348564,1.610772,2.100744,2.874180,-4.616459,-6.980607,9.542865,-3.265126,-7.334126,4.955900,7.441554,8.843349,-6.557810,8.952620,-3.873254,8.096663,1.925527,1.361392,-9.467890,-5.100559,0.623313,4.229922,-9.907572,-3.743408,-6.063634,-5.594068,8.086114,3.187854,1.402789,0.536747,-4.307364,8.229408,6.579086,9.880955,-4.066603,7.967723,-5.400814,-8.334539,-1.173737,1.515492,-2.065814,-0.411484,7.612808,0.515221,-4.673509,6.596106,6.364415,5.085839,7.942193,6.718518,-3.309312,4.852273,1.492419,4.706809,5.337271,-1.956336,-0.379730,7.608089,-4.422742,-0.280343,1.914769,-7.240217,6.006852,7.169709,-7.629159,-3.403178,0.656641,8.340857,3.270077,6.621459,1.711746,-3.938495,-4.179274,0.210167,-7.906448,-3.546799,9.617709,2.780735,-3.051860,-8.603512,6.309347,1.691496,-1.737771,5.383283,8.525981,-5.943263,-2.354947,8.412257,-2.116547,2.502145,-4.436362,-1.132732,-2.478837,-5.360059,0.195263,5.847302,9.390458,4.217802,7.738758,9.432129,4.265120,0.385421,-7.050261,9.511457,-4.360662,-8.556926,-0.873416,-3.481241,-1.357744,3.027800,9.234444,-0.093237,6.101482,2.630396,-9.408540,2.464893,-7.394574,0.370775,5.567829,-7.501013,0.592283,5.602456,1.406013,3.318275,-3.193574,8.402635,3.434316,9.932609,-0.486416,-5.983718,1.926266,-4.175464,-2.010845,7.397655,-4.161607,9.400884,-1.135220,9.163207,5.426661,5.971184,4.260657,3.136159,-5.225173,0.968883,6.242002,7.639391,-1.112973,3.392686,9.834123,-3.133831,-2.595573,9.118001,-6.263436,-3.095988,9.923748,-8.225534,5.825682,-5.201124,-8.948326,-3.752221,1.236696,-3.935718,8.631917,-4.176877,-8.861742,2.722967,9.001043,6.720261,0.442348,8.691819,8.265403,-9.069010,1.063970,-8.573751,-4.112652,-6.092613,-0.444188,2.946347,-8.453476,-3.630024,4.594267,8.714824,5.840317,-3.884579,-8.337290,9.635839,8.810019,-3.934652,-6.309828,-1.898965,4.388764,-2.761871,-9.350397,-3.148045,-9.735124,2.040514,-2.842440,-6.087634,-8.994063,-8.557805,-3.358657,-0.888866,3.307204,-3.037336,-9.853777,3.746047,8.468113,6.578324,2.305002,-4.023209,4.902579,9.748378,-9.200255,9.924374,7.089153,-7.307665,6.270891,6.117651,6.171497,0.036951,7.277424,-8.048122,-3.659207,-5.285467,1.833701,3.696585,-9.546404,-0.877887,-6.662881,5.630918,9.248676,9.534920,3.305920,-5.421119,3.045754,-2.408475,-7.037318,1.612722,-3.083012,-3.841697,5.147450,-9.013239,1.163491,-0.509243,-0.606318,0.579860,1.792196,0.103142,3.672808,-4.821355,1.613114,5.417932,7.395351,-6.419362,-6.282655,1.949085,9.454247,-6.743025,-2.694669,-0.532705,-5.395309,-7.471623,4.901427,-5.966865,6.605318,7.144667,8.788340,-9.607019,3.230081,3.583860,-5.187091,2.897118,-6.646096,-8.281666,3.871592,-3.387629,-4.615354,1.519138,-5.147310,-3.792017,-5.317793,-5.176963,0.397525,-9.076844,5.374834,-6.629306,-7.940089,0.786914,9.754365,4.718783,4.072596,5.993799,7.168851,3.829884,-0.200076,3.116706,2.744802,0.140364,3.674586,5.231326,6.909688,-9.009583,-7.716078,-9.871721,7.650149,-1.469133,9.850595,-1.440167,-0.438737,-6.784630,9.877800,-3.103641,9.238670,0.595174,5.243156,-9.683523,3.397024,7.035725,-3.193495,9.629464,1.650923,-5.589056,8.797448,5.412806,-6.592131,3.335964,-3.268179,-9.430299,6.015078,-4.300147,9.635718,9.963067,0.192415,-3.985587,-8.583087,6.455938,9.176224,7.302717,-9.062736,-3.141275,-0.033686,-7.359113,2.869897,2.951745,8.576958,-5.592221,-7.857646,7.190740,-9.299699,7.288147,1.267709,-2.297928,2.247199,-1.676435,2.430538,-5.733942,-2.378922,-7.166031,-7.949372,-2.582550,6.532792,-6.033039,-1.235396,6.150294,1.668849,5.193185,5.442245,2.256870,8.120555,-9.571446,-8.544548,6.938290,1.718960,1.507905,7.952435,5.063254,-3.521595,-8.528172,6.835430,7.130335,-7.944697,-0.802599,-3.135059,-3.718465,0.761195,-4.485277,-2.683157,-1.106177,3.967601,2.908126,4.494653,4.953509,-6.331062,-1.640254,5.672072,-3.579530,-3.365365,7.364224,-3.867893,4.219503,-7.996799,4.605672,5.763190,0.480919,0.268404,7.245808,2.427052,-7.134271,-9.437601,-4.207912,-7.172371,3.589775,2.684631,-4.416922,9.539040,5.631608,0.955329,-7.219951,-5.857294,-1.846475,-7.955867,-7.487852,-7.517028,1.283279,6.558201,4.403690,-8.110777,-5.626064,0.704461,2.459233,-3.595949,2.169660,6.132032,-8.908575,0.857895,-7.625535,-1.808114,4.197244,3.979633,5.116362,-0.778452,7.145261,-1.448866,-0.113204,-5.188308,-9.822357,-5.127433,-5.185238,7.326800,4.449601,5.945082,-8.171389,-4.059631,9.680438,-9.604347,-0.069073,7.240341,4.915364,-2.626267,6.871018,8.157226,4.386588,8.117705,5.837194,9.940658,3.877707,-0.372179,-6.316306,-2.342969,9.865771,6.051287,9.151381,7.955054,-4.368052,3.368957,-0.877736,5.600182,-9.774444,2.426226,6.333388,2.783405,-6.464270,-5.481339,-4.461463,-4.469314,1.722714,-6.421869,-9.024412,0.529510,7.428618,-2.407756,9.680132,1.898154,7.427133,5.748994,0.733152,0.166232,3.589469,8.050363,-8.422450,1.225101,5.797444,5.818483,5.725045,-9.273238,2.839347,-0.600018,-4.402530,-0.119180,-3.684805,-9.580616,-5.852444,8.295352,0.396453,-4.185240,-2.889075,5.941361,3.774682,1.795548,3.689168,5.429795,4.380416,9.960178,7.724836,7.087231,6.945124,-7.650765,8.446477,0.192269,-1.735777,4.562587,2.107816,-9.617911,8.174921,4.068143,4.557700,7.958661,-3.867316,-0.207181,-5.182822,-4.720980,5.468359,-3.089357,-2.589297,0.080380,2.628168,-1.099374,6.017558,7.721601,-3.357298,3.346801,8.144858,-3.175957,4.133488,7.673439,-3.878205,7.492804,-0.970124,3.057706,-9.960177,0.335254,7.450019,-8.746387,-7.950518,8.004339,1.714300,-3.943437,0.826263,-2.059539,8.651652,-6.015861,4.444611,6.005893,4.089225,0.792787,7.789624,1.583674,-6.217779,3.180186,1.184622,3.932117,5.073374,6.862318,1.632316,9.418600,-2.835370,-4.486330,-7.984292,4.197514,-6.178925,3.434833,-7.078222,-4.549291,-7.018898,0.051986,-6.965900,-9.004210,2.174001,-7.289613,-8.699303,0.039668,-8.522823,-8.525273,-1.442433,-8.454448,-2.139040,-1.259266,4.027594,3.091762,6.353475,7.883756,-0.228871,8.654557,-7.014095,-7.298803,-7.160785,1.117706,8.772129,9.972560,3.068813,3.747858,7.527388], dtype = "float64")#candidate|2932|(1560,)|const|float64
var_2933 = relay.var("var_2933", dtype = "float64", shape = (480, 4))#candidate|2933|(480, 4)|var|float64
call_2930 = relay.TupleGetItem(func_2596_call(relay.reshape(const_2931.astype('float64'), [1, 8, 15]), relay.reshape(const_2932.astype('float64'), [13, 8, 15]), relay.reshape(var_2933.astype('float64'), [96, 20]), ), 1)
call_2934 = relay.TupleGetItem(func_2600_call(relay.reshape(const_2931.astype('float64'), [1, 8, 15]), relay.reshape(const_2932.astype('float64'), [13, 8, 15]), relay.reshape(var_2933.astype('float64'), [96, 20]), ), 1)
var_2936 = relay.var("var_2936", dtype = "bool", shape = (16, 8, 4))#candidate|2936|(16, 8, 4)|var|bool
bop_2937 = relay.less(call_2909.astype('bool'), var_2936.astype('bool')) # shape=(16, 8, 4)
bop_2940 = relay.less(call_2910.astype('bool'), var_2936.astype('bool')) # shape=(16, 8, 4)
func_2891_call = mod.get_global_var('func_2891')
func_2893_call = mutated_mod.get_global_var('func_2893')
const_2949 = relay.const([[False,True,False,True,True,True,False,True,True,False,False,True,True,True,False,True,False,True,False,False,False,True,False,True,False,False,False,True,False,False,True,True,True,True,False,False,False,False,True,False,False,True,True,True,False,False,True,False],[True,True,True,True,False,True,True,True,True,True,False,False,True,True,True,False,False,True,False,True,True,True,True,True,True,False,True,True,False,False,False,False,True,True,True,False,False,False,True,True,False,True,True,True,False,False,False,False],[True,False,True,False,False,False,False,True,True,True,False,True,True,False,True,False,True,True,False,True,True,True,True,True,False,False,True,False,True,True,True,False,True,False,True,True,True,True,False,False,False,True,True,True,True,True,True,True],[False,False,False,True,True,True,True,False,False,False,False,True,True,True,True,False,False,False,False,True,True,False,True,True,True,False,False,True,True,False,False,True,False,False,True,True,False,False,True,False,False,False,True,True,True,False,True,True],[True,True,False,False,False,True,False,True,False,False,False,True,False,False,True,False,True,False,False,True,False,True,True,False,True,False,True,True,False,False,False,True,False,True,False,False,False,False,True,False,False,False,False,True,False,True,True,True],[True,True,False,True,True,True,True,False,True,False,True,False,False,False,True,False,True,True,False,True,True,False,False,False,False,False,True,False,True,False,False,False,False,False,True,True,False,False,True,True,False,True,True,False,True,True,True,False],[False,True,True,False,True,True,False,True,True,True,False,False,True,False,False,True,False,True,False,False,True,False,False,True,True,True,False,False,False,True,False,True,False,True,True,False,True,True,True,False,False,True,True,True,True,True,True,False],[True,True,False,False,True,False,False,False,False,False,False,False,True,False,True,True,False,False,True,True,True,True,True,True,False,False,True,False,False,False,False,True,True,False,True,True,True,True,True,True,True,False,True,False,False,True,False,False],[True,True,True,True,False,True,False,True,True,True,True,True,True,True,False,True,True,False,False,False,True,True,True,True,True,True,True,False,False,True,False,True,True,False,False,True,True,True,False,False,False,True,False,False,False,False,True,False],[False,True,False,False,False,False,True,False,True,False,False,True,False,False,False,True,False,True,False,True,False,True,False,False,False,False,False,True,False,True,True,True,False,True,True,True,True,False,True,False,False,True,True,False,True,False,True,False],[True,False,True,True,True,True,True,True,True,False,False,False,True,True,True,False,True,False,True,False,False,False,True,False,True,False,True,False,False,False,False,True,False,False,False,True,True,False,True,True,False,True,True,True,True,False,True,False],[False,False,False,False,False,True,False,True,False,True,False,False,False,False,False,False,False,False,False,False,False,True,True,False,False,False,False,True,False,True,True,False,False,False,False,False,True,False,False,True,False,False,False,False,False,False,False,True]], dtype = "bool")#candidate|2949|(12, 48)|const|bool
call_2948 = relay.TupleGetItem(func_2891_call(relay.reshape(const_2949.astype('bool'), [12, 48])), 2)
call_2950 = relay.TupleGetItem(func_2893_call(relay.reshape(const_2949.astype('bool'), [12, 48])), 2)
output = relay.Tuple([call_2898,call_2923,const_2924,call_2930,const_2931,const_2932,var_2933,bop_2937,call_2948,const_2949,])
output2 = relay.Tuple([call_2899,call_2925,const_2924,call_2934,const_2931,const_2932,var_2933,bop_2940,call_2950,const_2949,])
func_2958 = relay.Function([var_2933,var_2936,], output)
mod['func_2958'] = func_2958
mod = relay.transform.InferType()(mod)
mutated_mod['func_2958'] = func_2958
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2958_call = mutated_mod.get_global_var('func_2958')
var_2960 = relay.var("var_2960", dtype = "float64", shape = (480, 4))#candidate|2960|(480, 4)|var|float64
var_2961 = relay.var("var_2961", dtype = "bool", shape = (16, 8, 4))#candidate|2961|(16, 8, 4)|var|bool
call_2959 = func_2958_call(var_2960,var_2961,)
output = call_2959
func_2962 = relay.Function([var_2960,var_2961,], output)
mutated_mod['func_2962'] = func_2962
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1547_call = mod.get_global_var('func_1547')
func_1548_call = mutated_mod.get_global_var('func_1548')
call_2973 = relay.TupleGetItem(func_1547_call(), 0)
call_2974 = relay.TupleGetItem(func_1548_call(), 0)
uop_2975 = relay.erf(call_2973.astype('float64')) # shape=(64, 8)
uop_2977 = relay.erf(call_2974.astype('float64')) # shape=(64, 8)
output = relay.Tuple([uop_2975,])
output2 = relay.Tuple([uop_2977,])
func_2982 = relay.Function([], output)
mod['func_2982'] = func_2982
mod = relay.transform.InferType()(mod)
mutated_mod['func_2982'] = func_2982
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2982_call = mutated_mod.get_global_var('func_2982')
call_2983 = func_2982_call()
output = call_2983
func_2984 = relay.Function([], output)
mutated_mod['func_2984'] = func_2984
mutated_mod = relay.transform.InferType()(mutated_mod)
func_391_call = mod.get_global_var('func_391')
func_392_call = mutated_mod.get_global_var('func_392')
call_3004 = func_391_call()
call_3005 = func_391_call()
const_3008 = relay.const([[7.785947,-0.523342,-6.068539,5.004048,-8.643057,-3.507174],[7.261286,5.804631,-4.772141,-4.264656,4.375026,-5.847913],[6.246258,-6.926539,6.379986,-0.862578,0.935541,-4.157890],[6.826940,1.892112,-1.641393,6.063009,-4.509625,-9.097655],[-2.146758,-2.990865,3.261240,9.198129,-5.118602,-0.264187],[5.974161,-5.174778,5.032525,-9.306685,7.952523,-1.813337],[4.320450,4.167242,-0.167289,-8.525922,-8.416245,-1.372217],[4.443255,5.220229,7.284075,5.575174,-6.774176,3.022307],[-1.354219,-9.246808,-8.706483,-6.870352,-2.815024,8.780511],[5.545333,0.077710,-4.863081,8.449279,6.912314,8.988221],[9.936830,3.508404,-1.865510,9.002486,-7.741496,-3.522475],[3.486095,-4.430585,-1.308427,-2.239579,5.532169,-4.376957],[-5.003964,6.120256,-5.102162,-5.731994,-4.552006,6.345230],[7.149258,5.845857,-6.579100,-7.132858,-0.017840,9.297879],[-0.179921,-6.652038,9.465041,9.099556,6.348974,8.140455],[3.599463,6.099354,8.936714,-9.431918,3.815412,-5.012036],[-2.398018,7.123324,5.389778,8.682861,3.543662,6.225543],[-4.584669,-5.646046,0.096022,3.438851,1.763645,-9.448132],[5.660707,6.576037,8.080340,-0.537285,-2.916978,-4.532067],[-2.242803,6.856947,-7.663476,-7.868786,4.676591,-8.095881],[-2.901510,9.666623,-4.842036,-2.062437,3.719392,-7.437008],[9.058970,-0.937416,6.940204,1.688039,-2.257072,8.729869],[3.491672,-5.087379,-3.587682,-2.212800,-9.042054,-4.082243],[7.344621,7.898017,2.039210,9.698572,-7.336548,-2.512858],[0.148954,-1.590971,9.531777,-4.971580,9.499141,2.837121],[6.270343,6.975051,-8.592709,-4.539621,-4.477022,-5.006912],[9.246408,4.932108,7.343091,3.331037,7.021858,-9.021226],[5.478665,-8.988644,6.959201,-0.597469,6.800708,7.582127],[-8.042603,2.722908,1.848249,-0.050702,-3.873984,-7.891222],[0.113014,-9.256330,9.711664,5.573504,7.000076,-4.769682],[-0.790434,3.073085,-0.330386,4.323924,-6.284147,8.844796],[-3.335335,-7.489406,1.178195,-4.778974,3.240725,-6.963819],[7.858594,3.954002,4.667690,-8.497888,7.803849,3.467112],[-6.730177,-2.557289,7.597234,-2.982311,6.466398,-8.946913],[4.274263,1.661349,0.378423,-9.593791,-3.608496,7.908817],[5.560257,2.990466,5.758203,-3.274482,2.286548,-2.295333],[-6.539236,-1.370532,-8.219907,6.504486,2.462861,-6.527835],[-3.502637,9.086091,-7.528099,-9.511537,-0.285128,-6.352141],[-1.779139,4.097244,3.822611,-8.340072,-3.919447,3.335895],[-8.100503,7.734745,-6.777202,-5.592805,-3.664190,8.501368],[8.604889,-1.273089,2.420441,9.814031,6.335201,8.372225],[6.900948,-7.300602,-5.638224,-1.523822,-4.153837,-0.424504],[8.774623,0.357340,-7.204076,-0.170405,-8.966283,-4.021883],[-2.556081,8.288326,-9.873030,-9.875606,5.375559,-4.978549],[0.967015,-5.075857,-0.820734,-6.358731,3.725518,7.381339],[-5.173259,8.518289,-2.067392,-9.066309,-2.811647,-4.809009],[-1.817171,-7.784003,3.655962,8.383501,6.030513,0.683963],[-3.133185,3.202188,0.016799,9.603817,-7.365524,6.498981],[-7.675698,8.903298,3.644156,-5.120616,6.178549,3.293788],[9.754105,1.667801,-4.630898,-9.098085,-9.452060,2.285225],[-7.818756,6.138140,4.968222,9.541156,-5.743670,-1.510739],[-8.014042,7.838368,7.044034,-5.307921,2.517511,2.682960],[-7.955964,-9.383973,6.529541,3.715839,-8.847068,8.729773],[0.776715,-9.611241,4.365582,5.450766,8.824447,6.434522],[-2.796996,9.468969,9.425309,6.693041,-5.549897,-3.280927],[8.146799,6.628662,-5.316796,-5.912429,3.295220,8.708659],[5.851048,-0.970230,7.659659,-1.522594,4.448694,5.774158],[-4.174511,7.172211,-3.353041,7.884579,9.627522,-6.666905],[6.491371,3.615358,0.698904,4.958088,0.089059,7.370991],[-5.460770,-6.541691,7.549027,-5.452316,8.068243,-5.128802],[-4.646113,8.701584,-2.106915,7.335273,-2.670466,-7.208052],[-9.468641,1.940903,3.856644,-8.605779,-9.575813,6.286619],[9.892537,3.306469,6.855449,-9.509741,3.652107,3.244557],[6.854279,8.431043,2.284846,3.334871,-6.520435,-0.620564]], dtype = "float32")#candidate|3008|(64, 6)|const|float32
bop_3009 = relay.greater(call_3004.astype('bool'), relay.reshape(const_3008.astype('bool'), relay.shape_of(call_3004))) # shape=(64, 6)
bop_3012 = relay.greater(call_3005.astype('bool'), relay.reshape(const_3008.astype('bool'), relay.shape_of(call_3005))) # shape=(64, 6)
output = bop_3009
output2 = bop_3012
func_3013 = relay.Function([], output)
mod['func_3013'] = func_3013
mod = relay.transform.InferType()(mod)
mutated_mod['func_3013'] = func_3013
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3013_call = mutated_mod.get_global_var('func_3013')
call_3014 = func_3013_call()
output = call_3014
func_3015 = relay.Function([], output)
mutated_mod['func_3015'] = func_3015
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1227_call = mod.get_global_var('func_1227')
func_1229_call = mutated_mod.get_global_var('func_1229')
call_3077 = relay.TupleGetItem(func_1227_call(), 1)
call_3078 = relay.TupleGetItem(func_1229_call(), 1)
output = relay.Tuple([call_3077,])
output2 = relay.Tuple([call_3078,])
func_3079 = relay.Function([], output)
mod['func_3079'] = func_3079
mod = relay.transform.InferType()(mod)
output = func_3079()
func_3080 = relay.Function([], output)
mutated_mod['func_3080'] = func_3080
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3086 = relay.const(-9, dtype = "uint64")#candidate|3086|()|const|uint64
var_3087 = relay.var("var_3087", dtype = "uint64", shape = (5, 1, 7))#candidate|3087|(5, 1, 7)|var|uint64
bop_3088 = relay.bitwise_xor(const_3086.astype('uint64'), var_3087.astype('uint64')) # shape=(5, 1, 7)
func_105_call = mod.get_global_var('func_105')
func_107_call = mutated_mod.get_global_var('func_107')
var_3096 = relay.var("var_3096", dtype = "bool", shape = (8, 8))#candidate|3096|(8, 8)|var|bool
call_3095 = func_105_call(relay.reshape(var_3096.astype('bool'), [16, 1, 4]))
call_3097 = func_105_call(relay.reshape(var_3096.astype('bool'), [16, 1, 4]))
func_3079_call = mod.get_global_var('func_3079')
func_3080_call = mutated_mod.get_global_var('func_3080')
call_3105 = relay.TupleGetItem(func_3079_call(), 0)
call_3106 = relay.TupleGetItem(func_3080_call(), 0)
output = relay.Tuple([bop_3088,call_3095,var_3096,call_3105,])
output2 = relay.Tuple([bop_3088,call_3097,var_3096,call_3106,])
func_3109 = relay.Function([var_3087,var_3096,], output)
mod['func_3109'] = func_3109
mod = relay.transform.InferType()(mod)
mutated_mod['func_3109'] = func_3109
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3109_call = mutated_mod.get_global_var('func_3109')
var_3111 = relay.var("var_3111", dtype = "uint64", shape = (5, 1, 7))#candidate|3111|(5, 1, 7)|var|uint64
var_3112 = relay.var("var_3112", dtype = "bool", shape = (8, 8))#candidate|3112|(8, 8)|var|bool
call_3110 = func_3109_call(var_3111,var_3112,)
output = call_3110
func_3113 = relay.Function([var_3111,var_3112,], output)
mutated_mod['func_3113'] = func_3113
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1017_call = mod.get_global_var('func_1017')
func_1018_call = mutated_mod.get_global_var('func_1018')
call_3243 = relay.TupleGetItem(func_1017_call(), 1)
call_3244 = relay.TupleGetItem(func_1018_call(), 1)
func_295_call = mod.get_global_var('func_295')
func_297_call = mutated_mod.get_global_var('func_297')
call_3257 = relay.TupleGetItem(func_295_call(), 2)
call_3258 = relay.TupleGetItem(func_297_call(), 2)
func_1580_call = mod.get_global_var('func_1580')
func_1583_call = mutated_mod.get_global_var('func_1583')
const_3260 = relay.const([6.783339,4.627070,0.764667,5.905247,6.399205,1.822180,7.190459,7.258491,-2.579284,-8.128022,7.493450,-0.448962,2.456127,4.975142,-4.548767,-3.535314,-4.238700,-9.569696,5.546463,-4.612920,7.518077,3.151191,-9.529012,1.741753,-0.067089,0.972437,-3.770423,-5.203150,-5.510692,-2.554826,-2.727905,-2.712987,1.078959,-3.799920,-4.548377,2.435096,-1.631476,-2.837392,7.088868,9.243155,2.663890,-8.358677,9.685623,6.974345,-7.844167,-7.715128,3.334795,-4.821729,6.606774,5.539156,2.481783,4.590598,5.139193,-8.564120,-2.176397,-5.948721,-2.735118,6.514582,7.419796,6.604537,-2.473170,7.941944,-0.116084,-9.108206,-4.661183,-9.970375,0.513101,-2.527441,6.795371,4.140622,-8.138374,-6.130856,-0.485500,-8.735850,-5.092738,-6.562631,0.557283,-4.218218,2.393487,5.111799,3.757710,1.239910,-7.423416,3.904598,-1.776162,7.694043,5.542754,-4.079022,0.707157,7.848759,-2.016948,-8.767665,8.341273,-4.659917,-1.442740,6.546640,9.733145,-6.212252,-1.092390,0.865876,-1.410264,4.475007,-4.470158,-2.393211,5.917265,-3.749559,2.605806,4.690754,2.056776,5.296026,-6.626349,7.695890,4.136552,7.091478,-7.875524,-3.659942,9.473636,-6.906566,8.494602,8.481823,-8.686233,0.040088,-6.481174,3.870192,-3.476993,2.578679,3.281674,-2.715840,-9.631511,-3.009108,-0.527523,-9.206251,-3.680768,-8.149242,7.762669,-0.545381,4.573618,2.434630,2.551862,7.246320,3.653766,-7.616336,-6.303166,7.129368,-2.382715,6.429194,-4.167664,-2.116722,-5.165213,0.488490,-6.061897,1.751426,4.315671,2.260709,7.513296,-3.595673,-6.043080,9.486327,3.258994,6.810587,-6.883555,-9.968834,-8.993025,-5.859352,4.573043,-4.867496,1.271774,4.502242,-6.162338,0.316543,-5.947873,-2.452817,-2.615319,0.064659,-1.095618,7.743502,2.813138,-4.849008,-0.859267,-3.755533,-7.321285,3.398933,-7.729536,-8.305447,-4.961360,6.184665,8.940242,8.455701,2.798013,2.900045,7.225219,1.673313,-4.337820,6.266331,-2.329238,5.021715,-0.852444,-6.754742,1.866874,-5.634755,2.148175,-2.705610,3.028675,-6.335658,-6.652463,9.233711,3.632262,-9.650813,-9.066475,-0.177026,6.313439,9.815973,6.279903,6.421986,-8.588534,-3.362301,0.097792,-2.636554,-2.822431,2.021283,-5.177613,-0.259831,3.804310,8.153480,-0.505008,-3.528013,6.190182,-8.402415,-4.603512,-5.129272,4.478661,-7.317070,5.727694,8.655789,2.091659,0.981609,8.944633,3.992181,-4.785040,-0.127545,6.315481,6.644691,-5.794964,4.565727,2.281199,7.810805,-6.760907,7.085250,-2.434445,9.069768,9.016859,7.292178,-4.635923,-3.602939,-1.024220,-0.759744,5.901804,-0.301419,3.789213,-6.495760,6.964699,3.612710,2.841106,-2.226428,5.162333,-3.817808,-0.427195,-9.104557,-8.438105,9.762126,1.782326,-3.250203,0.280249,0.114170,-8.400682,9.672629,1.682758,8.554776,2.205720,8.955046,6.566884,-2.283423,9.157236,4.298204,9.590604,-4.041142,-0.378008,6.515372,-2.664403,-1.015560,7.568376,-9.263914,-0.493978,1.551333,2.393602,-8.696020,-3.084550,-5.396050,4.088591,-2.127275,2.880167,-9.484655,5.750612,3.265367,-5.883776,8.901744,-2.312515,-6.475832,7.764834,-6.699142,-8.432143,-1.284916,7.607430,8.751774,-8.437272,0.344703,-9.947401,3.966887,-3.364781,1.099937,-1.520013,-6.425126,2.614046,1.135737,-7.570051,8.756561,-7.961500,-8.853973,9.488833,2.951770,3.499029,7.348227,-4.828396,7.143567,0.133007,1.263647,0.299714,-6.141543,-1.280307,-7.443839,-8.481193,-2.126341,0.251381,-2.046515,-0.394442,-9.873949,4.744308,8.596034,-6.894031,-2.276223,-6.356217,4.626795,8.033840,-8.269223,3.962769,-1.282880,-3.940349,-5.193261,4.155571,-7.703297,-6.977743,4.566027,-0.189862,8.488776,-1.591868,3.351185,3.656089,-1.481778,-8.351230,0.444325,5.080231,9.776710,-2.997145,0.251659,6.553229,5.950799,-4.340693,0.748837,1.280658,4.397910,-8.693387,-3.809944,5.786860,-4.147607,9.816804,2.423193,4.967930,5.583734,0.883583,-9.044977,-4.513812,-6.975998,-3.005940,-1.374472,5.885036,8.798554,-0.642617,9.542719,0.704286,1.198413,1.238714,1.685804,-3.718609,-7.708867,-4.494065,-1.363030,-1.112443,8.620653,-6.040096,0.917866,-5.553227,8.270306,-3.425895,-9.635442,-6.984574,9.576920,9.318734,-7.413595,2.004081,9.390716,9.544746,-2.106051,-2.681551,4.726566,8.394377,-5.937985,0.966240,-2.954935,6.157813,3.810431,0.047376,0.777301,-6.641503,-0.809599,1.095036,6.003606,6.175338,-5.949008,8.536131,-4.481740,-5.754407,-9.858800,-4.643454,-0.960313,-2.563498,2.154814,-3.121709,-6.340615,-3.192983,-7.422382,-8.694362,5.012047,8.602948,4.942896,1.668581,-9.174617,1.158538,9.554786,6.697347,7.492135,-0.058437,4.936483,8.838929,0.098688,-5.732902,9.789550,3.969866,-1.590874,0.520200,4.066582,1.624559,-0.206558,1.842846,-4.966695,3.151086,-9.578078,-7.108744,-1.350133,8.574280,-2.873933,6.329465,-1.905958,-8.277874,-4.969140,-9.893694,-9.790000,9.522025,-5.227757,-5.255176,8.117717,-4.029075,2.935869,-7.796322,9.550350,8.717236,9.898658,1.472378,3.685944,1.460121,1.205656,-4.105690,7.603656,3.969136,-8.984498,6.078273,0.206306,4.803436,-1.706316,0.591476,7.038251,7.490535,4.290177], dtype = "float64")#candidate|3260|(512,)|const|float64
call_3259 = relay.TupleGetItem(func_1580_call(relay.reshape(const_3260.astype('float64'), [64, 8])), 0)
call_3261 = relay.TupleGetItem(func_1583_call(relay.reshape(const_3260.astype('float64'), [64, 8])), 0)
func_2094_call = mod.get_global_var('func_2094')
func_2097_call = mutated_mod.get_global_var('func_2097')
const_3264 = relay.const([False,True,True,True,True,False,True,True,False,False,False,False,True,False,True,True,True,True,True,False,True,False,True,True,True,False,False,True,False,False,False,False,True,False,True,True,False,True,False,False,True,False,True,True,False,False,False,False,True,False,False,False,False,True,True,True,True,False,False,True,False,True,False,False,True,True,True,True,False,True,True,False,False,False,True,False,False,True,False,True,True,False,False,False,False,True,True,True,True,False,True,False,True,True,False,False,False,True,True,True,False,False,True,False,True,False,True,True,True,True,True,True,False,True,True,False,False,False,True,False,False,False,False,True,True,False,True,False,True,False,True,True,True,False,False,False,False,True,True,True,False,False,False,False,True,True,False,False,False,False,False,False,False,False,False,False,False,True,False,True,False,True,False,True,True,False,True,True,True,False,False,False,True,True,False,False,False,True,False,False,True,False,True,True,False,True,True,False,False,True,True,False,False,False,True,True,False,False,False,False,True,True,False,False,False,False,False,False,True,True,True,False,True,False,False,False,True,True,False,True,True,False,False,True,False,True,True,False,False,True,False,True,False,False,True,False,True,True,True,False,False,False,True,False,False,True,False,True,False,False,False,True,False,False,True,False,False,False,True,False,True,True,True,False,False,False,False,True,True,True,True,False,True,False,False,True,True,False,False,False,False,True,True,True,True,False,True,True,False,False,True,False,False,False,False,False,False,False,True,False,False,False,False,True,True,False,True,False,False,True,False,False,False,False,True,False,False,True,True,True,True,True,True,True,True,True,True,False,True,False,False,True,True,False,True,False,False,False,False,False,True,True,False,False,True,False,False,True,True,True,False,False,False,True,False,False,False,True,False,False,False,False,True,True,False,False,True,False,False,True,False,False,False,False,False,True,False,False,True,True,True,True,False,False,True,False,False,True,True,False,True,True,False,True,False,False,True,True,False,False,True,False,False,True,False,False,True,True,False,False,False,True,True,False,True,False,False,True,False,False,True,True,True,True,False,False,True,False,True,True,False,False,True,False,False,False,False,True,True,False,True,True,True,False,False,True,True,False,False,True,False,False,False,False,True,True,False,True,True,True,False,True,False,False,True,False,False,True,True,True,True,False,False,False,False,False,True,True,True,False,False,True,False,True,True,True,False,True,False,True,True,True,False,True,True,True,True,True,False,False,False,True,False,False,True,False,True,True,False,False,True,False,True,True,True,True,False,True,False,True,False,True,False,False,False,True,True,True,False,True,True,False,False,True,False,False,False,True,True,False,True,False,False,True,True,False,False,True,True,False,False,False,False,False,False,False,True,False,False,True,True,True,True,False,True,False,False,True,True,True,True,True,True,True,False,False], dtype = "bool")#candidate|3264|(576,)|const|bool
var_3265 = relay.var("var_3265", dtype = "bool", shape = (256,))#candidate|3265|(256,)|var|bool
call_3263 = relay.TupleGetItem(func_2094_call(relay.reshape(const_3264.astype('bool'), [576,]), relay.reshape(var_3265.astype('bool'), [256,]), ), 4)
call_3266 = relay.TupleGetItem(func_2097_call(relay.reshape(const_3264.astype('bool'), [576,]), relay.reshape(var_3265.astype('bool'), [256,]), ), 4)
bop_3283 = relay.logical_xor(const_3260.astype('int8'), relay.reshape(call_3259.astype('int8'), relay.shape_of(const_3260))) # shape=(512,)
bop_3286 = relay.logical_xor(const_3260.astype('int8'), relay.reshape(call_3261.astype('int8'), relay.shape_of(const_3260))) # shape=(512,)
func_1433_call = mod.get_global_var('func_1433')
func_1437_call = mutated_mod.get_global_var('func_1437')
call_3296 = relay.TupleGetItem(func_1433_call(relay.reshape(const_3260.astype('bool'), [512,]), relay.reshape(var_3265.astype('bool'), [256,]), ), 4)
call_3297 = relay.TupleGetItem(func_1437_call(relay.reshape(const_3260.astype('bool'), [512,]), relay.reshape(var_3265.astype('bool'), [256,]), ), 4)
func_874_call = mod.get_global_var('func_874')
func_877_call = mutated_mod.get_global_var('func_877')
const_3311 = relay.const([-0.777343,5.951394,0.509862,-5.233504,0.921227,-9.403634,3.226570,5.992844,5.688607,5.694414,9.487991,5.292702,-9.437867,-9.325544,-1.877296,-8.681849,-4.469674,-1.378219,3.091218,7.929197,9.830392,-3.006098,3.928434,-1.710883], dtype = "float64")#candidate|3311|(24,)|const|float64
call_3310 = relay.TupleGetItem(func_874_call(relay.reshape(const_3311.astype('float64'), [6, 4, 1])), 1)
call_3312 = relay.TupleGetItem(func_877_call(relay.reshape(const_3311.astype('float64'), [6, 4, 1])), 1)
func_2814_call = mod.get_global_var('func_2814')
func_2816_call = mutated_mod.get_global_var('func_2816')
call_3319 = relay.TupleGetItem(func_2814_call(), 0)
call_3320 = relay.TupleGetItem(func_2816_call(), 0)
output = relay.Tuple([call_3243,call_3257,call_3263,const_3264,var_3265,bop_3283,call_3296,call_3310,const_3311,call_3319,])
output2 = relay.Tuple([call_3244,call_3258,call_3266,const_3264,var_3265,bop_3286,call_3297,call_3312,const_3311,call_3320,])
func_3326 = relay.Function([var_3265,], output)
mod['func_3326'] = func_3326
mod = relay.transform.InferType()(mod)
mutated_mod['func_3326'] = func_3326
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3327 = relay.var("var_3327", dtype = "bool", shape = (256,))#candidate|3327|(256,)|var|bool
func_3326_call = mutated_mod.get_global_var('func_3326')
call_3328 = func_3326_call(var_3327)
output = call_3328
func_3329 = relay.Function([var_3327], output)
mutated_mod['func_3329'] = func_3329
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2482_call = mod.get_global_var('func_2482')
func_2484_call = mutated_mod.get_global_var('func_2484')
call_3351 = relay.TupleGetItem(func_2482_call(), 0)
call_3352 = relay.TupleGetItem(func_2484_call(), 0)
output = call_3351
output2 = call_3352
func_3368 = relay.Function([], output)
mod['func_3368'] = func_3368
mod = relay.transform.InferType()(mod)
mutated_mod['func_3368'] = func_3368
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3368_call = mutated_mod.get_global_var('func_3368')
call_3369 = func_3368_call()
output = call_3369
func_3370 = relay.Function([], output)
mutated_mod['func_3370'] = func_3370
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3013_call = mod.get_global_var('func_3013')
func_3015_call = mutated_mod.get_global_var('func_3015')
call_3382 = func_3013_call()
call_3383 = func_3013_call()
var_3386 = relay.var("var_3386", dtype = "bool", shape = (64, 6))#candidate|3386|(64, 6)|var|bool
bop_3387 = relay.power(call_3382.astype('float32'), relay.reshape(var_3386.astype('float32'), relay.shape_of(call_3382))) # shape=(64, 6)
bop_3390 = relay.power(call_3383.astype('float32'), relay.reshape(var_3386.astype('float32'), relay.shape_of(call_3383))) # shape=(64, 6)
func_1095_call = mod.get_global_var('func_1095')
func_1098_call = mutated_mod.get_global_var('func_1098')
var_3392 = relay.var("var_3392", dtype = "bool", shape = (48,))#candidate|3392|(48,)|var|bool
call_3391 = relay.TupleGetItem(func_1095_call(relay.reshape(var_3392.astype('bool'), [48,])), 1)
call_3393 = relay.TupleGetItem(func_1098_call(relay.reshape(var_3392.astype('bool'), [48,])), 1)
output = relay.Tuple([bop_3387,call_3391,var_3392,])
output2 = relay.Tuple([bop_3390,call_3393,var_3392,])
func_3396 = relay.Function([var_3386,var_3392,], output)
mod['func_3396'] = func_3396
mod = relay.transform.InferType()(mod)
var_3397 = relay.var("var_3397", dtype = "bool", shape = (64, 6))#candidate|3397|(64, 6)|var|bool
var_3398 = relay.var("var_3398", dtype = "bool", shape = (48,))#candidate|3398|(48,)|var|bool
output = func_3396(var_3397,var_3398,)
func_3399 = relay.Function([var_3397,var_3398,], output)
mutated_mod['func_3399'] = func_3399
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1547_call = mod.get_global_var('func_1547')
func_1548_call = mutated_mod.get_global_var('func_1548')
call_3414 = relay.TupleGetItem(func_1547_call(), 0)
call_3415 = relay.TupleGetItem(func_1548_call(), 0)
output = call_3414
output2 = call_3415
func_3425 = relay.Function([], output)
mod['func_3425'] = func_3425
mod = relay.transform.InferType()(mod)
mutated_mod['func_3425'] = func_3425
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3425_call = mutated_mod.get_global_var('func_3425')
call_3426 = func_3425_call()
output = call_3426
func_3427 = relay.Function([], output)
mutated_mod['func_3427'] = func_3427
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1227_call = mod.get_global_var('func_1227')
func_1229_call = mutated_mod.get_global_var('func_1229')
call_3436 = relay.TupleGetItem(func_1227_call(), 1)
call_3437 = relay.TupleGetItem(func_1229_call(), 1)
func_3326_call = mod.get_global_var('func_3326')
func_3329_call = mutated_mod.get_global_var('func_3329')
var_3445 = relay.var("var_3445", dtype = "bool", shape = (256,))#candidate|3445|(256,)|var|bool
call_3444 = relay.TupleGetItem(func_3326_call(relay.reshape(var_3445.astype('bool'), [256,])), 2)
call_3446 = relay.TupleGetItem(func_3329_call(relay.reshape(var_3445.astype('bool'), [256,])), 2)
output = relay.Tuple([call_3436,call_3444,var_3445,])
output2 = relay.Tuple([call_3437,call_3446,var_3445,])
func_3464 = relay.Function([var_3445,], output)
mod['func_3464'] = func_3464
mod = relay.transform.InferType()(mod)
var_3465 = relay.var("var_3465", dtype = "bool", shape = (256,))#candidate|3465|(256,)|var|bool
output = func_3464(var_3465)
func_3466 = relay.Function([var_3465], output)
mutated_mod['func_3466'] = func_3466
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1547_call = mod.get_global_var('func_1547')
func_1548_call = mutated_mod.get_global_var('func_1548')
call_3483 = relay.TupleGetItem(func_1547_call(), 0)
call_3484 = relay.TupleGetItem(func_1548_call(), 0)
func_3396_call = mod.get_global_var('func_3396')
func_3399_call = mutated_mod.get_global_var('func_3399')
var_3493 = relay.var("var_3493", dtype = "bool", shape = (384,))#candidate|3493|(384,)|var|bool
const_3494 = relay.const([False,True,False,False,False,True,False,True,False,True,True,False,False,False,False,True,False,True,True,False,True,False,True,True,True,False,False,False,False,False,True,False,True,True,True,True,True,True,False,True,False,True,True,True,True,False,False,False], dtype = "bool")#candidate|3494|(48,)|const|bool
call_3492 = relay.TupleGetItem(func_3396_call(relay.reshape(var_3493.astype('bool'), [64, 6]), relay.reshape(const_3494.astype('bool'), [48,]), ), 2)
call_3495 = relay.TupleGetItem(func_3399_call(relay.reshape(var_3493.astype('bool'), [64, 6]), relay.reshape(const_3494.astype('bool'), [48,]), ), 2)
output = relay.Tuple([call_3483,call_3492,var_3493,const_3494,])
output2 = relay.Tuple([call_3484,call_3495,var_3493,const_3494,])
func_3503 = relay.Function([var_3493,], output)
mod['func_3503'] = func_3503
mod = relay.transform.InferType()(mod)
mutated_mod['func_3503'] = func_3503
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3504 = relay.var("var_3504", dtype = "bool", shape = (384,))#candidate|3504|(384,)|var|bool
func_3503_call = mutated_mod.get_global_var('func_3503')
call_3505 = func_3503_call(var_3504)
output = call_3505
func_3506 = relay.Function([var_3504], output)
mutated_mod['func_3506'] = func_3506
mutated_mod = relay.transform.InferType()(mutated_mod)
func_295_call = mod.get_global_var('func_295')
func_297_call = mutated_mod.get_global_var('func_297')
call_3536 = relay.TupleGetItem(func_295_call(), 2)
call_3537 = relay.TupleGetItem(func_297_call(), 2)
uop_3538 = relay.tan(call_3536.astype('float32')) # shape=(64, 1)
uop_3540 = relay.tan(call_3537.astype('float32')) # shape=(64, 1)
bop_3541 = relay.greater(uop_3538.astype('bool'), relay.reshape(call_3536.astype('bool'), relay.shape_of(uop_3538))) # shape=(64, 1)
bop_3544 = relay.greater(uop_3540.astype('bool'), relay.reshape(call_3537.astype('bool'), relay.shape_of(uop_3540))) # shape=(64, 1)
bop_3547 = relay.greater_equal(bop_3541.astype('bool'), relay.reshape(uop_3538.astype('bool'), relay.shape_of(bop_3541))) # shape=(64, 1)
bop_3550 = relay.greater_equal(bop_3544.astype('bool'), relay.reshape(uop_3540.astype('bool'), relay.shape_of(bop_3544))) # shape=(64, 1)
output = relay.Tuple([bop_3547,])
output2 = relay.Tuple([bop_3550,])
func_3555 = relay.Function([], output)
mod['func_3555'] = func_3555
mod = relay.transform.InferType()(mod)
mutated_mod['func_3555'] = func_3555
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3555_call = mutated_mod.get_global_var('func_3555')
call_3556 = func_3555_call()
output = call_3556
func_3557 = relay.Function([], output)
mutated_mod['func_3557'] = func_3557
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3582 = relay.const([[[-7.003045],[-7.782191],[-8.969568],[8.543933],[-3.239863],[-7.460574],[-5.634530],[-5.035705],[8.769732],[3.961422]],[[3.781326],[4.921954],[-4.323214],[3.258676],[1.660454],[-1.219302],[0.157862],[-9.583534],[-5.690152],[-7.918598]],[[-2.973517],[7.053764],[2.775767],[4.803607],[-9.257885],[4.385821],[3.653784],[-5.383817],[-3.572578],[3.905362]],[[-0.268369],[6.492712],[-5.558189],[-0.193659],[9.610189],[0.105472],[3.557409],[-1.016619],[7.070291],[5.514443]],[[-6.919645],[2.293698],[5.271419],[-7.781697],[-8.568876],[9.793043],[0.524364],[-5.985190],[-6.073953],[-0.547223]],[[9.747215],[-3.130367],[-3.411891],[2.591673],[-9.388480],[0.529151],[5.664699],[-6.067329],[5.567077],[7.781893]],[[-1.892626],[-0.001589],[3.666514],[-0.309147],[9.854174],[-3.328730],[-4.432971],[7.472601],[3.253332],[-2.838192]],[[3.317327],[1.260076],[8.375289],[6.415531],[-4.064244],[-0.065988],[-6.095436],[-4.851624],[1.316918],[5.203423]],[[5.804686],[-0.797971],[-4.649486],[1.031023],[-5.101167],[-3.796834],[4.669521],[5.981941],[1.831609],[9.199035]],[[6.429457],[7.638290],[6.570910],[7.919234],[-3.900948],[0.693009],[-5.763174],[0.247101],[-3.467980],[0.881307]],[[9.651183],[-1.058865],[6.744162],[7.565246],[3.264133],[-1.119787],[-8.960729],[-4.131201],[8.957719],[-9.297864]],[[-0.016628],[5.195276],[0.722445],[-6.073688],[0.261635],[2.770669],[9.060746],[-6.505246],[1.558900],[1.873078]],[[-8.113794],[8.490511],[1.079045],[-5.971634],[3.015676],[-2.882089],[1.808719],[5.096943],[8.433326],[-8.855064]],[[3.184939],[1.930038],[3.643911],[2.429625],[8.837963],[3.358540],[-9.044845],[-6.154847],[-3.364177],[-4.592332]],[[7.930150],[-9.642130],[-7.335215],[-2.309847],[2.234050],[9.402462],[-5.419059],[9.648935],[-4.349371],[-3.405053]]], dtype = "float64")#candidate|3582|(15, 10, 1)|const|float64
uop_3583 = relay.sigmoid(const_3582.astype('float64')) # shape=(15, 10, 1)
uop_3587 = relay.cos(uop_3583.astype('float64')) # shape=(15, 10, 1)
output = relay.Tuple([uop_3587,])
output2 = relay.Tuple([uop_3587,])
func_3590 = relay.Function([], output)
mod['func_3590'] = func_3590
mod = relay.transform.InferType()(mod)
mutated_mod['func_3590'] = func_3590
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3590_call = mutated_mod.get_global_var('func_3590')
call_3591 = func_3590_call()
output = call_3591
func_3592 = relay.Function([], output)
mutated_mod['func_3592'] = func_3592
mutated_mod = relay.transform.InferType()(mutated_mod)
func_439_call = mod.get_global_var('func_439')
func_440_call = mutated_mod.get_global_var('func_440')
call_3622 = func_439_call()
call_3623 = func_439_call()
output = call_3622
output2 = call_3623
func_3626 = relay.Function([], output)
mod['func_3626'] = func_3626
mod = relay.transform.InferType()(mod)
mutated_mod['func_3626'] = func_3626
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3626_call = mutated_mod.get_global_var('func_3626')
call_3627 = func_3626_call()
output = call_3627
func_3628 = relay.Function([], output)
mutated_mod['func_3628'] = func_3628
mutated_mod = relay.transform.InferType()(mutated_mod)
func_391_call = mod.get_global_var('func_391')
func_392_call = mutated_mod.get_global_var('func_392')
call_3664 = func_391_call()
call_3665 = func_391_call()
func_391_call = mod.get_global_var('func_391')
func_392_call = mutated_mod.get_global_var('func_392')
call_3666 = func_391_call()
call_3667 = func_391_call()
uop_3671 = relay.sin(call_3666.astype('float64')) # shape=(64, 6)
uop_3673 = relay.sin(call_3667.astype('float64')) # shape=(64, 6)
func_2677_call = mod.get_global_var('func_2677')
func_2679_call = mutated_mod.get_global_var('func_2679')
call_3674 = relay.TupleGetItem(func_2677_call(), 0)
call_3675 = relay.TupleGetItem(func_2679_call(), 0)
output = relay.Tuple([call_3664,uop_3671,call_3674,])
output2 = relay.Tuple([call_3665,uop_3673,call_3675,])
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
func_1227_call = mod.get_global_var('func_1227')
func_1229_call = mutated_mod.get_global_var('func_1229')
call_3723 = relay.TupleGetItem(func_1227_call(), 0)
call_3724 = relay.TupleGetItem(func_1229_call(), 0)
uop_3726 = relay.sigmoid(call_3723.astype('float32')) # shape=(16, 10, 4)
uop_3728 = relay.sigmoid(call_3724.astype('float32')) # shape=(16, 10, 4)
output = relay.Tuple([uop_3726,])
output2 = relay.Tuple([uop_3728,])
func_3729 = relay.Function([], output)
mod['func_3729'] = func_3729
mod = relay.transform.InferType()(mod)
output = func_3729()
func_3730 = relay.Function([], output)
mutated_mod['func_3730'] = func_3730
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3425_call = mod.get_global_var('func_3425')
func_3427_call = mutated_mod.get_global_var('func_3427')
call_3814 = func_3425_call()
call_3815 = func_3425_call()
func_3503_call = mod.get_global_var('func_3503')
func_3506_call = mutated_mod.get_global_var('func_3506')
var_3819 = relay.var("var_3819", dtype = "bool", shape = (384,))#candidate|3819|(384,)|var|bool
call_3818 = relay.TupleGetItem(func_3503_call(relay.reshape(var_3819.astype('bool'), [384,])), 1)
call_3820 = relay.TupleGetItem(func_3506_call(relay.reshape(var_3819.astype('bool'), [384,])), 1)
output = relay.Tuple([call_3814,call_3818,var_3819,])
output2 = relay.Tuple([call_3815,call_3820,var_3819,])
func_3854 = relay.Function([var_3819,], output)
mod['func_3854'] = func_3854
mod = relay.transform.InferType()(mod)
mutated_mod['func_3854'] = func_3854
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3855 = relay.var("var_3855", dtype = "bool", shape = (384,))#candidate|3855|(384,)|var|bool
func_3854_call = mutated_mod.get_global_var('func_3854')
call_3856 = func_3854_call(var_3855)
output = call_3856
func_3857 = relay.Function([var_3855], output)
mutated_mod['func_3857'] = func_3857
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3884 = relay.var("var_3884", dtype = "float32", shape = (3, 10, 11))#candidate|3884|(3, 10, 11)|var|float32
uop_3885 = relay.log(var_3884.astype('float32')) # shape=(3, 10, 11)
bop_3890 = relay.right_shift(uop_3885.astype('int32'), relay.reshape(var_3884.astype('int32'), relay.shape_of(uop_3885))) # shape=(3, 10, 11)
func_1178_call = mod.get_global_var('func_1178')
func_1180_call = mutated_mod.get_global_var('func_1180')
const_3904 = relay.const([[False,False,False,False,True,False,False,True,False,False,True,True,True,True,False,True,False,False,True,True,True,True,False,True,False,True,False,True,True,True,False,True,False,False,True,True,False,True,True,False,True,False,False,False,False,False,True,False,True,False,True,False,False,False,True,False,True,False,True,False,True,True,True,True,False,False,True,False,True,False,True,False,False,True,False,False,True,True,False,False,False,False,True,False,False,False,False,True,False,True,True,False,True,False,True,True,False,False,True,True,False,False,True,True,True,True,True,True,False,False,True,False,False,False,False,False,True,False,True,True,False,False,True,True,False,True,False,False,True,True,True,False,False,False,True,True,True,False,False,True,False,False,False,False,False,False,False,True,True,True,True,True,True,False,False,True,True,False,True,True,True,False,True,True,False,False,True,True,False,True,True,True,True,True,True,False,True,False,True,False,True,False,True,True,True,True,False,False,True,False,True,True,False,False,False,True,False,True,False,True,True,True,False,False,False,True,False,False,True,False,False,True,False,False,False,True,True,False,False,True,False,True,False,True,False,False,False,False,False,False,True,True,False,True,True,False,True,False,False,False,False,True,True,False,True,True,False,False,False,False,True,False,True,True,True,True]], dtype = "bool")#candidate|3904|(1, 256)|const|bool
call_3903 = relay.TupleGetItem(func_1178_call(relay.reshape(const_3904.astype('bool'), [64, 4])), 5)
call_3905 = relay.TupleGetItem(func_1180_call(relay.reshape(const_3904.astype('bool'), [64, 4])), 5)
func_2146_call = mod.get_global_var('func_2146')
func_2148_call = mutated_mod.get_global_var('func_2148')
call_3915 = relay.TupleGetItem(func_2146_call(), 0)
call_3916 = relay.TupleGetItem(func_2148_call(), 0)
uop_3920 = relay.log(const_3904.astype('float64')) # shape=(1, 256)
func_1227_call = mod.get_global_var('func_1227')
func_1229_call = mutated_mod.get_global_var('func_1229')
call_3929 = relay.TupleGetItem(func_1227_call(), 0)
call_3930 = relay.TupleGetItem(func_1229_call(), 0)
bop_3936 = relay.divide(uop_3920.astype('float64'), relay.reshape(const_3904.astype('float64'), relay.shape_of(uop_3920))) # shape=(1, 256)
func_3109_call = mod.get_global_var('func_3109')
func_3113_call = mutated_mod.get_global_var('func_3113')
const_3955 = relay.const([-5,-7,8,-10,1,-4,8,5,5,-5,-4,-4,7,1,10,5,8,6,8,-7,-6,9,8,5,-2,2,5,8,-8,9,3,-5,-6,7,7], dtype = "uint64")#candidate|3955|(35,)|const|uint64
call_3954 = relay.TupleGetItem(func_3109_call(relay.reshape(const_3955.astype('uint64'), [5, 1, 7]), relay.reshape(call_3903.astype('bool'), [8, 8]), ), 1)
call_3956 = relay.TupleGetItem(func_3113_call(relay.reshape(const_3955.astype('uint64'), [5, 1, 7]), relay.reshape(call_3903.astype('bool'), [8, 8]), ), 1)
bop_3969 = relay.less(const_3904.astype('bool'), relay.reshape(uop_3920.astype('bool'), relay.shape_of(const_3904))) # shape=(1, 256)
func_2677_call = mod.get_global_var('func_2677')
func_2679_call = mutated_mod.get_global_var('func_2679')
call_3972 = relay.TupleGetItem(func_2677_call(), 0)
call_3973 = relay.TupleGetItem(func_2679_call(), 0)
bop_3975 = relay.less_equal(uop_3885.astype('bool'), relay.reshape(var_3884.astype('bool'), relay.shape_of(uop_3885))) # shape=(3, 10, 11)
output = relay.Tuple([bop_3890,call_3903,call_3915,call_3929,bop_3936,call_3954,const_3955,bop_3969,call_3972,bop_3975,])
output2 = relay.Tuple([bop_3890,call_3905,call_3916,call_3930,bop_3936,call_3956,const_3955,bop_3969,call_3973,bop_3975,])
func_3979 = relay.Function([var_3884,], output)
mod['func_3979'] = func_3979
mod = relay.transform.InferType()(mod)
mutated_mod['func_3979'] = func_3979
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3980 = relay.var("var_3980", dtype = "float32", shape = (3, 10, 11))#candidate|3980|(3, 10, 11)|var|float32
func_3979_call = mutated_mod.get_global_var('func_3979')
call_3981 = func_3979_call(var_3980)
output = call_3981
func_3982 = relay.Function([var_3980], output)
mutated_mod['func_3982'] = func_3982
mutated_mod = relay.transform.InferType()(mutated_mod)
func_391_call = mod.get_global_var('func_391')
func_392_call = mutated_mod.get_global_var('func_392')
call_4003 = func_391_call()
call_4004 = func_391_call()
uop_4005 = relay.cos(call_4003.astype('float32')) # shape=(64, 6)
uop_4007 = relay.cos(call_4004.astype('float32')) # shape=(64, 6)
bop_4011 = relay.less(uop_4005.astype('bool'), relay.reshape(call_4003.astype('bool'), relay.shape_of(uop_4005))) # shape=(64, 6)
bop_4014 = relay.less(uop_4007.astype('bool'), relay.reshape(call_4004.astype('bool'), relay.shape_of(uop_4007))) # shape=(64, 6)
func_3626_call = mod.get_global_var('func_3626')
func_3628_call = mutated_mod.get_global_var('func_3628')
call_4021 = func_3626_call()
call_4022 = func_3626_call()
output = relay.Tuple([bop_4011,call_4021,])
output2 = relay.Tuple([bop_4014,call_4022,])
func_4033 = relay.Function([], output)
mod['func_4033'] = func_4033
mod = relay.transform.InferType()(mod)
output = func_4033()
func_4034 = relay.Function([], output)
mutated_mod['func_4034'] = func_4034
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3013_call = mod.get_global_var('func_3013')
func_3015_call = mutated_mod.get_global_var('func_3015')
call_4052 = func_3013_call()
call_4053 = func_3013_call()
func_900_call = mod.get_global_var('func_900')
func_902_call = mutated_mod.get_global_var('func_902')
const_4060 = relay.const([False,True,False,False,True,False,False,False,False,True,False,False,False,False,True,False,False,False,True,False,True,True,False,True,False,False,False,True,False,False,False,True,True,False,True,True,False,True,True,True,False,True,True,False,False,True,True,False,True,False,True,False,True,True,True,True,True,True,True,False,True,True,True,True,True,False,False,False,True,True,True,False,False,False,False,False,True,True,True,False,False,False,False,True,True,False,True,False,True,False,False,True,True,True,False,False,True,False,False,True,True,True,True,True,False,True,False,True,True,True,False,True,True,False,False,False,False,True,False,False,True,True,True,False,False,True,True,False,True,True,True,False,True,False,True,True,True,True,False,False,False,False,True,True,True,False,True,True,True,False,True,True,True,False,True,True,True,False,True,False,False,False,False,True,False,False,False,False,True,False,False,False,True,False,True,False,False,True,True,True,True,True,False,False,True,False,True,True,False,True,True,False,True,False,True,False,False,True,False,True,False,False,True,True,False,True,True,False,False,False,False,True,True,False,True,True,False,False,False,True,True,True,True,True,True,True,True,True,False,True,True,False,True,False,True,False,True,False,False,True,True,False,False,False,True,True,True,True,False,True,False,True,True,False,False,False,True,True,False,True,False,True,False,False,True,True,False,True,False,False,False,True,True,True,True,False,False,True,True,False,False,False,False,True,False,False,False,True,False,False,False,False,True,False,False,False,False,False,True,False,True,False,True,False,True,False,False,True,True,True,False,False,True,False,True,True,False,True,False,False,True,True,True,False,True,True,True,True,False,False,True,True,False,False,True,True,True,True,True,False,False,True,False,False,True,False,True,True,True,False,False,True,True,True,True,False,False,False,False,False,True,True,True,True,False,False,True,True,True,False,True,False,True,False,False,False,False,True,True,True,True,True,False,False,False,False,True,True,False,True,True,True,False,True,True,False,True,False,True,True,False,True,True,True,True,True,True,True,False,False,False,False,False,True,False,False,True,True,True,True,False,True,True,True,False,False,True,True,False,True,False,False,False,True,True,True,False,False,False,True,False,False,True,False,True,True,True,False,True,False,False,True,True,True,False,True,True,False,True,True,True,True,True,True,True,False,False,True,False,False,False,False,False,True,True,False,True,False,False,False,False,False,True,False,True,False,True,False,False,False,True,True,False,False,False,True,False,False,False,False,False,True,True,False,False,False,False,True,False,True,True,False], dtype = "bool")#candidate|4060|(512,)|const|bool
call_4059 = relay.TupleGetItem(func_900_call(relay.reshape(const_4060.astype('bool'), [64, 8])), 0)
call_4061 = relay.TupleGetItem(func_902_call(relay.reshape(const_4060.astype('bool'), [64, 8])), 0)
var_4067 = relay.var("var_4067", dtype = "bool", shape = (64, 6))#candidate|4067|(64, 6)|var|bool
bop_4068 = relay.bitwise_and(call_4052.astype('int8'), relay.reshape(var_4067.astype('int8'), relay.shape_of(call_4052))) # shape=(64, 6)
bop_4071 = relay.bitwise_and(call_4053.astype('int8'), relay.reshape(var_4067.astype('int8'), relay.shape_of(call_4053))) # shape=(64, 6)
bop_4076 = relay.bitwise_xor(call_4059.astype('uint32'), relay.reshape(const_4060.astype('uint32'), relay.shape_of(call_4059))) # shape=(64, 8)
bop_4079 = relay.bitwise_xor(call_4061.astype('uint32'), relay.reshape(const_4060.astype('uint32'), relay.shape_of(call_4061))) # shape=(64, 8)
output = relay.Tuple([bop_4068,bop_4076,])
output2 = relay.Tuple([bop_4071,bop_4079,])
func_4087 = relay.Function([var_4067,], output)
mod['func_4087'] = func_4087
mod = relay.transform.InferType()(mod)
var_4088 = relay.var("var_4088", dtype = "bool", shape = (64, 6))#candidate|4088|(64, 6)|var|bool
output = func_4087(var_4088)
func_4089 = relay.Function([var_4088], output)
mutated_mod['func_4089'] = func_4089
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2982_call = mod.get_global_var('func_2982')
func_2984_call = mutated_mod.get_global_var('func_2984')
call_4109 = relay.TupleGetItem(func_2982_call(), 0)
call_4110 = relay.TupleGetItem(func_2984_call(), 0)
uop_4125 = relay.tan(call_4109.astype('float64')) # shape=(64, 8)
uop_4127 = relay.tan(call_4110.astype('float64')) # shape=(64, 8)
func_1547_call = mod.get_global_var('func_1547')
func_1548_call = mutated_mod.get_global_var('func_1548')
call_4129 = relay.TupleGetItem(func_1547_call(), 0)
call_4130 = relay.TupleGetItem(func_1548_call(), 0)
func_2414_call = mod.get_global_var('func_2414')
func_2416_call = mutated_mod.get_global_var('func_2416')
call_4148 = relay.TupleGetItem(func_2414_call(), 0)
call_4149 = relay.TupleGetItem(func_2416_call(), 0)
output = relay.Tuple([uop_4125,call_4129,call_4148,])
output2 = relay.Tuple([uop_4127,call_4130,call_4149,])
func_4159 = relay.Function([], output)
mod['func_4159'] = func_4159
mod = relay.transform.InferType()(mod)
output = func_4159()
func_4160 = relay.Function([], output)
mutated_mod['func_4160'] = func_4160
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1684_call = mod.get_global_var('func_1684')
func_1686_call = mutated_mod.get_global_var('func_1686')
call_4189 = relay.TupleGetItem(func_1684_call(), 1)
call_4190 = relay.TupleGetItem(func_1686_call(), 1)
func_1718_call = mod.get_global_var('func_1718')
func_1719_call = mutated_mod.get_global_var('func_1719')
call_4198 = relay.TupleGetItem(func_1718_call(), 0)
call_4199 = relay.TupleGetItem(func_1719_call(), 0)
output = relay.Tuple([call_4189,call_4198,])
output2 = relay.Tuple([call_4190,call_4199,])
func_4214 = relay.Function([], output)
mod['func_4214'] = func_4214
mod = relay.transform.InferType()(mod)
output = func_4214()
func_4215 = relay.Function([], output)
mutated_mod['func_4215'] = func_4215
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3013_call = mod.get_global_var('func_3013')
func_3015_call = mutated_mod.get_global_var('func_3015')
call_4238 = func_3013_call()
call_4239 = func_3013_call()
output = relay.Tuple([call_4238,])
output2 = relay.Tuple([call_4239,])
func_4246 = relay.Function([], output)
mod['func_4246'] = func_4246
mod = relay.transform.InferType()(mod)
output = func_4246()
func_4247 = relay.Function([], output)
mutated_mod['func_4247'] = func_4247
mutated_mod = relay.transform.InferType()(mutated_mod)
func_439_call = mod.get_global_var('func_439')
func_440_call = mutated_mod.get_global_var('func_440')
call_4298 = func_439_call()
call_4299 = func_439_call()
output = relay.Tuple([call_4298,])
output2 = relay.Tuple([call_4299,])
func_4319 = relay.Function([], output)
mod['func_4319'] = func_4319
mod = relay.transform.InferType()(mod)
output = func_4319()
func_4320 = relay.Function([], output)
mutated_mod['func_4320'] = func_4320
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4319_call = mod.get_global_var('func_4319')
func_4320_call = mutated_mod.get_global_var('func_4320')
call_4352 = relay.TupleGetItem(func_4319_call(), 0)
call_4353 = relay.TupleGetItem(func_4320_call(), 0)
var_4389 = relay.var("var_4389", dtype = "float64", shape = (16, 10, 4))#candidate|4389|(16, 10, 4)|var|float64
bop_4390 = relay.left_shift(call_4352.astype('int8'), relay.reshape(var_4389.astype('int8'), relay.shape_of(call_4352))) # shape=(16, 10, 4)
bop_4393 = relay.left_shift(call_4353.astype('int8'), relay.reshape(var_4389.astype('int8'), relay.shape_of(call_4353))) # shape=(16, 10, 4)
func_2982_call = mod.get_global_var('func_2982')
func_2984_call = mutated_mod.get_global_var('func_2984')
call_4413 = relay.TupleGetItem(func_2982_call(), 0)
call_4414 = relay.TupleGetItem(func_2984_call(), 0)
output = relay.Tuple([bop_4390,call_4413,])
output2 = relay.Tuple([bop_4393,call_4414,])
func_4417 = relay.Function([var_4389,], output)
mod['func_4417'] = func_4417
mod = relay.transform.InferType()(mod)
var_4418 = relay.var("var_4418", dtype = "float64", shape = (16, 10, 4))#candidate|4418|(16, 10, 4)|var|float64
output = func_4417(var_4418)
func_4419 = relay.Function([var_4418], output)
mutated_mod['func_4419'] = func_4419
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4475 = relay.var("var_4475", dtype = "float32", shape = (7, 8, 15))#candidate|4475|(7, 8, 15)|var|float32
uop_4476 = relay.rsqrt(var_4475.astype('float32')) # shape=(7, 8, 15)
func_1634_call = mod.get_global_var('func_1634')
func_1637_call = mutated_mod.get_global_var('func_1637')
var_4505 = relay.var("var_4505", dtype = "bool", shape = (512,))#candidate|4505|(512,)|var|bool
call_4504 = relay.TupleGetItem(func_1634_call(relay.reshape(var_4505.astype('bool'), [512, 1])), 0)
call_4506 = relay.TupleGetItem(func_1637_call(relay.reshape(var_4505.astype('bool'), [512, 1])), 0)
output = relay.Tuple([uop_4476,call_4504,var_4505,])
output2 = relay.Tuple([uop_4476,call_4506,var_4505,])
func_4509 = relay.Function([var_4475,var_4505,], output)
mod['func_4509'] = func_4509
mod = relay.transform.InferType()(mod)
mutated_mod['func_4509'] = func_4509
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4509_call = mutated_mod.get_global_var('func_4509')
var_4511 = relay.var("var_4511", dtype = "float32", shape = (7, 8, 15))#candidate|4511|(7, 8, 15)|var|float32
var_4512 = relay.var("var_4512", dtype = "bool", shape = (512,))#candidate|4512|(512,)|var|bool
call_4510 = func_4509_call(var_4511,var_4512,)
output = call_4510
func_4513 = relay.Function([var_4511,var_4512,], output)
mutated_mod['func_4513'] = func_4513
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2814_call = mod.get_global_var('func_2814')
func_2816_call = mutated_mod.get_global_var('func_2816')
call_4548 = relay.TupleGetItem(func_2814_call(), 0)
call_4549 = relay.TupleGetItem(func_2816_call(), 0)
func_1178_call = mod.get_global_var('func_1178')
func_1180_call = mutated_mod.get_global_var('func_1180')
const_4556 = relay.const([True,True,False,True,False,True,True,False,True,True,True,True,False,False,True,False,False,False,True,True,False,True,True,True,False,True,True,True,False,True,True,True,False,True,False,False,False,True,True,True,True,False,True,True,False,False,True,True,True,True,False,True,False,True,False,False,False,True,False,False,True,True,True,True,False,False,False,True,True,True,False,False,True,True,False,True,False,True,False,True,False,False,False,False,True,False,True,True,True,True,True,False,False,True,False,False,True,False,True,False,True,False,True,False,True,True,True,True,False,False,False,True,False,False,True,False,False,False,True,False,True,True,False,True,False,False,False,True,False,True,True,True,True,False,True,True,True,True,False,False,True,True,True,True,True,False,True,False,True,True,False,False,False,False,False,False,True,False,True,True,True,False,True,True,True,False,False,False,True,False,False,False,True,True,False,True,False,True,True,True,False,True,True,False,True,True,False,False,True,True,False,True,False,True,False,True,True,False,True,True,False,False,True,False,True,True,True,True,True,False,False,True,True,False,False,False,True,False,True,True,False,True,False,False,False,False,True,True,False,False,False,False,False,False,False,False,True,True,True,False,True,False,False,False,False,False,True,True,False,False,False,False,True,False,False,True], dtype = "bool")#candidate|4556|(256,)|const|bool
call_4555 = relay.TupleGetItem(func_1178_call(relay.reshape(const_4556.astype('bool'), [64, 4])), 1)
call_4557 = relay.TupleGetItem(func_1180_call(relay.reshape(const_4556.astype('bool'), [64, 4])), 1)
output = relay.Tuple([call_4548,call_4555,const_4556,])
output2 = relay.Tuple([call_4549,call_4557,const_4556,])
func_4559 = relay.Function([], output)
mod['func_4559'] = func_4559
mod = relay.transform.InferType()(mod)
output = func_4559()
func_4560 = relay.Function([], output)
mutated_mod['func_4560'] = func_4560
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1107_call = mod.get_global_var('func_1107')
func_1108_call = mutated_mod.get_global_var('func_1108')
call_4568 = relay.TupleGetItem(func_1107_call(), 0)
call_4569 = relay.TupleGetItem(func_1108_call(), 0)
output = relay.Tuple([call_4568,])
output2 = relay.Tuple([call_4569,])
func_4596 = relay.Function([], output)
mod['func_4596'] = func_4596
mod = relay.transform.InferType()(mod)
output = func_4596()
func_4597 = relay.Function([], output)
mutated_mod['func_4597'] = func_4597
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4319_call = mod.get_global_var('func_4319')
func_4320_call = mutated_mod.get_global_var('func_4320')
call_4629 = relay.TupleGetItem(func_4319_call(), 0)
call_4630 = relay.TupleGetItem(func_4320_call(), 0)
output = call_4629
output2 = call_4630
func_4637 = relay.Function([], output)
mod['func_4637'] = func_4637
mod = relay.transform.InferType()(mod)
output = func_4637()
func_4638 = relay.Function([], output)
mutated_mod['func_4638'] = func_4638
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4681 = relay.var("var_4681", dtype = "uint8", shape = (10, 13, 6))#candidate|4681|(10, 13, 6)|var|uint8
var_4682 = relay.var("var_4682", dtype = "uint8", shape = (10, 13, 6))#candidate|4682|(10, 13, 6)|var|uint8
bop_4683 = relay.less(var_4681.astype('bool'), relay.reshape(var_4682.astype('bool'), relay.shape_of(var_4681))) # shape=(10, 13, 6)
func_391_call = mod.get_global_var('func_391')
func_392_call = mutated_mod.get_global_var('func_392')
call_4698 = func_391_call()
call_4699 = func_391_call()
func_3079_call = mod.get_global_var('func_3079')
func_3080_call = mutated_mod.get_global_var('func_3080')
call_4702 = relay.TupleGetItem(func_3079_call(), 0)
call_4703 = relay.TupleGetItem(func_3080_call(), 0)
func_3729_call = mod.get_global_var('func_3729')
func_3730_call = mutated_mod.get_global_var('func_3730')
call_4704 = relay.TupleGetItem(func_3729_call(), 0)
call_4705 = relay.TupleGetItem(func_3730_call(), 0)
output = relay.Tuple([bop_4683,call_4698,call_4702,call_4704,])
output2 = relay.Tuple([bop_4683,call_4699,call_4703,call_4705,])
func_4706 = relay.Function([var_4681,var_4682,], output)
mod['func_4706'] = func_4706
mod = relay.transform.InferType()(mod)
var_4707 = relay.var("var_4707", dtype = "uint8", shape = (10, 13, 6))#candidate|4707|(10, 13, 6)|var|uint8
var_4708 = relay.var("var_4708", dtype = "uint8", shape = (10, 13, 6))#candidate|4708|(10, 13, 6)|var|uint8
output = func_4706(var_4707,var_4708,)
func_4709 = relay.Function([var_4707,var_4708,], output)
mutated_mod['func_4709'] = func_4709
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4246_call = mod.get_global_var('func_4246')
func_4247_call = mutated_mod.get_global_var('func_4247')
call_4746 = relay.TupleGetItem(func_4246_call(), 0)
call_4747 = relay.TupleGetItem(func_4247_call(), 0)
func_105_call = mod.get_global_var('func_105')
func_107_call = mutated_mod.get_global_var('func_107')
var_4749 = relay.var("var_4749", dtype = "bool", shape = (64,))#candidate|4749|(64,)|var|bool
call_4748 = func_105_call(relay.reshape(var_4749.astype('bool'), [16, 1, 4]))
call_4750 = func_105_call(relay.reshape(var_4749.astype('bool'), [16, 1, 4]))
uop_4755 = relay.cosh(call_4746.astype('float64')) # shape=(64, 6)
uop_4757 = relay.cosh(call_4747.astype('float64')) # shape=(64, 6)
func_2414_call = mod.get_global_var('func_2414')
func_2416_call = mutated_mod.get_global_var('func_2416')
call_4760 = relay.TupleGetItem(func_2414_call(), 0)
call_4761 = relay.TupleGetItem(func_2416_call(), 0)
uop_4768 = relay.exp(uop_4755.astype('float32')) # shape=(64, 6)
uop_4770 = relay.exp(uop_4757.astype('float32')) # shape=(64, 6)
output = relay.Tuple([call_4748,var_4749,call_4760,uop_4768,])
output2 = relay.Tuple([call_4750,var_4749,call_4761,uop_4770,])
func_4771 = relay.Function([var_4749,], output)
mod['func_4771'] = func_4771
mod = relay.transform.InferType()(mod)
mutated_mod['func_4771'] = func_4771
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4772 = relay.var("var_4772", dtype = "bool", shape = (64,))#candidate|4772|(64,)|var|bool
func_4771_call = mutated_mod.get_global_var('func_4771')
call_4773 = func_4771_call(var_4772)
output = call_4773
func_4774 = relay.Function([var_4772], output)
mutated_mod['func_4774'] = func_4774
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4033_call = mod.get_global_var('func_4033')
func_4034_call = mutated_mod.get_global_var('func_4034')
call_4778 = relay.TupleGetItem(func_4033_call(), 1)
call_4779 = relay.TupleGetItem(func_4034_call(), 1)
func_1260_call = mod.get_global_var('func_1260')
func_1261_call = mutated_mod.get_global_var('func_1261')
call_4795 = relay.TupleGetItem(func_1260_call(), 0)
call_4796 = relay.TupleGetItem(func_1261_call(), 0)
output = relay.Tuple([call_4778,call_4795,])
output2 = relay.Tuple([call_4779,call_4796,])
func_4797 = relay.Function([], output)
mod['func_4797'] = func_4797
mod = relay.transform.InferType()(mod)
output = func_4797()
func_4798 = relay.Function([], output)
mutated_mod['func_4798'] = func_4798
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1227_call = mod.get_global_var('func_1227')
func_1229_call = mutated_mod.get_global_var('func_1229')
call_5025 = relay.TupleGetItem(func_1227_call(), 0)
call_5026 = relay.TupleGetItem(func_1229_call(), 0)
func_2430_call = mod.get_global_var('func_2430')
func_2431_call = mutated_mod.get_global_var('func_2431')
call_5037 = relay.TupleGetItem(func_2430_call(), 1)
call_5038 = relay.TupleGetItem(func_2431_call(), 1)
func_3626_call = mod.get_global_var('func_3626')
func_3628_call = mutated_mod.get_global_var('func_3628')
call_5055 = func_3626_call()
call_5056 = func_3626_call()
output = relay.Tuple([call_5025,call_5037,call_5055,])
output2 = relay.Tuple([call_5026,call_5038,call_5056,])
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
func_4559_call = mod.get_global_var('func_4559')
func_4560_call = mutated_mod.get_global_var('func_4560')
call_5090 = relay.TupleGetItem(func_4559_call(), 2)
call_5091 = relay.TupleGetItem(func_4560_call(), 2)
func_3979_call = mod.get_global_var('func_3979')
func_3982_call = mutated_mod.get_global_var('func_3982')
var_5111 = relay.var("var_5111", dtype = "float32", shape = (1, 330))#candidate|5111|(1, 330)|var|float32
call_5110 = relay.TupleGetItem(func_3979_call(relay.reshape(var_5111.astype('float32'), [3, 10, 11])), 3)
call_5112 = relay.TupleGetItem(func_3982_call(relay.reshape(var_5111.astype('float32'), [3, 10, 11])), 3)
output = relay.Tuple([call_5090,call_5110,var_5111,])
output2 = relay.Tuple([call_5091,call_5112,var_5111,])
func_5148 = relay.Function([var_5111,], output)
mod['func_5148'] = func_5148
mod = relay.transform.InferType()(mod)
mutated_mod['func_5148'] = func_5148
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5149 = relay.var("var_5149", dtype = "float32", shape = (1, 330))#candidate|5149|(1, 330)|var|float32
func_5148_call = mutated_mod.get_global_var('func_5148')
call_5150 = func_5148_call(var_5149)
output = call_5150
func_5151 = relay.Function([var_5149], output)
mutated_mod['func_5151'] = func_5151
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5201 = relay.var("var_5201", dtype = "int32", shape = ())#candidate|5201|()|var|int32
var_5202 = relay.var("var_5202", dtype = "int32", shape = (5, 10, 10))#candidate|5202|(5, 10, 10)|var|int32
bop_5203 = relay.greater_equal(var_5201.astype('bool'), var_5202.astype('bool')) # shape=(5, 10, 10)
func_4319_call = mod.get_global_var('func_4319')
func_4320_call = mutated_mod.get_global_var('func_4320')
call_5214 = relay.TupleGetItem(func_4319_call(), 0)
call_5215 = relay.TupleGetItem(func_4320_call(), 0)
var_5221 = relay.var("var_5221", dtype = "int32", shape = (5, 10, 10))#candidate|5221|(5, 10, 10)|var|int32
bop_5222 = relay.not_equal(var_5202.astype('bool'), relay.reshape(var_5221.astype('bool'), relay.shape_of(var_5202))) # shape=(5, 10, 10)
func_1433_call = mod.get_global_var('func_1433')
func_1437_call = mutated_mod.get_global_var('func_1437')
var_5237 = relay.var("var_5237", dtype = "bool", shape = (512,))#candidate|5237|(512,)|var|bool
var_5238 = relay.var("var_5238", dtype = "bool", shape = (256,))#candidate|5238|(256,)|var|bool
call_5236 = relay.TupleGetItem(func_1433_call(relay.reshape(var_5237.astype('bool'), [512,]), relay.reshape(var_5238.astype('bool'), [256,]), ), 2)
call_5239 = relay.TupleGetItem(func_1437_call(relay.reshape(var_5237.astype('bool'), [512,]), relay.reshape(var_5238.astype('bool'), [256,]), ), 2)
output = relay.Tuple([bop_5203,call_5214,bop_5222,call_5236,var_5237,var_5238,])
output2 = relay.Tuple([bop_5203,call_5215,bop_5222,call_5239,var_5237,var_5238,])
func_5248 = relay.Function([var_5201,var_5202,var_5221,var_5237,var_5238,], output)
mod['func_5248'] = func_5248
mod = relay.transform.InferType()(mod)
var_5249 = relay.var("var_5249", dtype = "int32", shape = ())#candidate|5249|()|var|int32
var_5250 = relay.var("var_5250", dtype = "int32", shape = (5, 10, 10))#candidate|5250|(5, 10, 10)|var|int32
var_5251 = relay.var("var_5251", dtype = "int32", shape = (5, 10, 10))#candidate|5251|(5, 10, 10)|var|int32
var_5252 = relay.var("var_5252", dtype = "bool", shape = (512,))#candidate|5252|(512,)|var|bool
var_5253 = relay.var("var_5253", dtype = "bool", shape = (256,))#candidate|5253|(256,)|var|bool
output = func_5248(var_5249,var_5250,var_5251,var_5252,var_5253,)
func_5254 = relay.Function([var_5249,var_5250,var_5251,var_5252,var_5253,], output)
mutated_mod['func_5254'] = func_5254
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3676_call = mod.get_global_var('func_3676')
func_3678_call = mutated_mod.get_global_var('func_3678')
call_5272 = relay.TupleGetItem(func_3676_call(), 0)
call_5273 = relay.TupleGetItem(func_3678_call(), 0)
output = relay.Tuple([call_5272,])
output2 = relay.Tuple([call_5273,])
func_5281 = relay.Function([], output)
mod['func_5281'] = func_5281
mod = relay.transform.InferType()(mod)
mutated_mod['func_5281'] = func_5281
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5281_call = mutated_mod.get_global_var('func_5281')
call_5282 = func_5281_call()
output = call_5282
func_5283 = relay.Function([], output)
mutated_mod['func_5283'] = func_5283
mutated_mod = relay.transform.InferType()(mutated_mod)
func_295_call = mod.get_global_var('func_295')
func_297_call = mutated_mod.get_global_var('func_297')
call_5294 = relay.TupleGetItem(func_295_call(), 1)
call_5295 = relay.TupleGetItem(func_297_call(), 1)
func_1684_call = mod.get_global_var('func_1684')
func_1686_call = mutated_mod.get_global_var('func_1686')
call_5304 = relay.TupleGetItem(func_1684_call(), 0)
call_5305 = relay.TupleGetItem(func_1686_call(), 0)
output = relay.Tuple([call_5294,call_5304,])
output2 = relay.Tuple([call_5295,call_5305,])
func_5308 = relay.Function([], output)
mod['func_5308'] = func_5308
mod = relay.transform.InferType()(mod)
output = func_5308()
func_5309 = relay.Function([], output)
mutated_mod['func_5309'] = func_5309
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5396 = relay.const([[[-3,3,-7,-9,-2,5,6,6,1,-7],[-4,4,3,8,4,7,6,3,4,8],[-8,4,4,-4,-8,1,-7,-5,-6,-8],[4,-6,-7,4,2,7,-4,5,-9,-7],[1,-8,-3,-1,-5,-7,-6,9,-5,-5],[2,8,3,6,-4,8,10,-4,-10,-2],[-3,5,-6,-3,5,8,1,5,-9,5],[-5,9,-10,8,7,6,3,-1,6,-7],[-3,-10,1,8,10,3,6,-1,-4,-10],[-3,3,10,2,-10,-8,-4,-7,6,4],[9,-1,9,5,3,4,-4,1,-9,-1],[-1,-1,-9,-9,4,-3,1,1,-6,-3]],[[2,6,-4,-1,9,1,-10,5,3,-6],[-7,1,3,-10,-8,9,-10,-7,3,7],[-9,1,3,1,-10,-4,-6,-7,-8,-7],[1,6,4,-8,-1,-8,-5,10,-3,-3],[-7,-9,3,1,4,8,7,-7,-7,-5],[-9,-1,-2,-2,3,7,4,5,6,9],[-6,-5,10,2,-6,8,-2,10,9,8],[-1,1,2,3,4,8,-8,2,5,-5],[-5,-8,1,8,2,-3,-10,8,-2,2],[2,7,4,-8,-5,10,8,-6,6,1],[1,-10,-10,-7,-9,10,8,3,-7,1],[-6,4,8,4,-6,-3,1,-8,-2,-5]],[[3,-4,1,4,-8,1,-7,9,5,-1],[-8,-7,-10,2,-1,2,-2,-6,-2,4],[7,-6,-10,-2,-10,-7,-9,-9,-1,-10],[-10,8,-7,-9,-7,10,8,-10,3,-3],[-7,1,-5,5,-3,-8,-7,9,1,2],[-10,-3,10,-7,7,8,-2,-10,-1,-3],[-1,-9,9,2,-5,9,-9,-4,-8,-4],[2,-7,-2,3,3,8,-9,4,-7,8],[-3,7,-1,-2,3,2,-9,2,-7,5],[-9,5,1,7,-8,-8,-4,-4,8,-4],[6,-6,6,-6,-1,4,-5,-1,10,2],[3,-10,7,-1,-4,5,2,4,-9,10]],[[5,-3,3,-5,-2,-1,-9,1,7,-10],[-9,-2,6,9,-8,9,-3,4,-6,8],[-7,2,-2,-1,-7,1,-6,6,-8,-1],[-4,-4,5,-2,6,-9,-9,-9,4,-1],[3,-6,4,2,7,-2,6,-9,-3,-9],[2,-4,-1,-3,4,-5,-5,-7,2,-5],[-5,-3,3,9,4,-7,-8,-7,-5,-3],[4,8,-10,10,-4,-3,2,-7,8,4],[-4,8,1,10,-4,5,-2,7,7,5],[4,10,6,2,-3,-5,7,-8,7,-4],[-2,2,3,-5,-9,-2,10,9,-7,-9],[-7,-7,8,-3,-3,9,-8,-9,-10,-1]],[[-5,-10,-5,1,1,-4,4,5,7,6],[-6,7,-6,7,1,3,-1,2,-3,9],[3,-2,-5,9,-4,-5,-2,6,-7,1],[9,5,-8,-7,2,-5,-1,1,4,9],[-7,-8,-5,4,-7,3,1,-7,6,2],[-2,-2,5,-9,5,9,-2,-8,3,-10],[-9,6,10,-8,7,-6,-10,2,-4,-6],[-8,-1,-4,-7,3,5,10,-1,-5,9],[-1,-3,-1,-8,-5,-6,-9,-3,-5,10],[-8,9,6,-8,-9,3,10,-2,-10,-8],[3,7,-10,-7,-1,-5,9,4,-4,-6],[-9,-4,4,4,6,-8,7,-5,6,-3]],[[6,-5,-4,10,-3,-4,7,3,-5,5],[8,-2,-9,-1,-8,1,6,9,-4,9],[-7,-2,-10,8,-2,9,-6,-7,10,1],[4,-2,-9,10,1,-3,-2,-7,-9,-10],[-5,1,1,-8,5,1,-3,-10,3,6],[-9,6,-1,6,5,-1,4,-4,1,8],[-3,-9,-1,9,-1,9,3,3,-8,5],[4,6,1,5,-1,-2,-1,1,10,-5],[6,-2,1,4,-4,-5,-7,8,-8,-2],[5,5,4,7,7,-6,-8,-1,-6,2],[-6,-10,-5,-2,1,-6,-9,2,1,7],[1,-1,4,2,9,-9,1,9,-8,-1]],[[-5,5,9,7,-7,8,-10,1,-2,-1],[8,-7,9,-5,7,6,-4,-5,-10,-3],[-9,-9,9,-2,-4,4,-4,1,7,2],[1,-3,3,-7,4,-2,-8,-3,-10,8],[9,5,2,-9,-1,10,-1,6,5,-6],[1,2,-8,8,2,-3,-9,6,-4,2],[-8,-7,9,4,7,3,-8,9,1,-6],[-3,-6,7,4,7,-7,10,5,-7,3],[6,4,-2,4,10,8,6,6,4,-5],[7,7,5,-7,8,8,6,2,7,-3],[3,-10,5,-4,-5,-1,2,10,-9,-2],[6,1,-4,-10,-8,-7,4,3,3,-10]],[[8,-1,-1,-8,9,-5,9,-7,-10,3],[-1,10,6,-7,-1,-7,10,1,-10,-10],[-6,6,-5,-8,9,5,-10,7,8,-6],[3,-10,-3,2,10,4,9,3,2,-8],[-5,-3,8,2,6,-7,-3,-1,9,-10],[7,7,4,1,5,7,4,4,1,-10],[-6,-5,-5,3,-2,-7,9,-7,5,-6],[-1,10,-4,9,-2,2,5,9,6,8],[-7,6,-8,-6,3,5,9,-7,-4,10],[-5,-6,-2,4,6,-3,-8,8,2,-1],[8,-6,5,-9,2,-5,-2,9,5,-1],[7,6,4,1,10,10,-2,-6,-2,6]],[[-6,2,1,3,7,8,9,9,-10,1],[4,1,-8,3,-3,5,-9,9,-10,-5],[-8,3,9,-3,6,-2,-5,-8,-9,4],[-9,3,-8,5,7,-7,5,2,-3,4],[1,10,8,-9,-9,10,2,4,-8,-5],[1,9,1,-1,-10,-4,10,5,3,6],[6,8,3,-5,-2,-5,-4,8,-8,2],[3,-9,3,2,7,-8,6,-9,9,-10],[-6,-4,1,-6,1,7,7,9,-9,5],[-9,-8,-8,-3,-1,-8,8,-7,-5,8],[-4,-2,-10,-10,1,4,6,-6,9,9],[-2,8,10,9,-2,-1,-1,-7,3,-1]],[[-1,-4,-8,-1,-10,10,-9,2,-6,5],[7,6,9,10,-1,6,-7,-10,3,-2],[6,-4,2,4,-6,-8,5,10,7,7],[2,-1,6,-4,7,-1,-9,7,1,-9],[-2,-10,1,2,4,8,-3,-5,-4,-7],[8,-3,-4,-10,4,4,6,-5,-7,-7],[-8,-7,5,1,4,10,7,8,-6,6],[8,7,7,-3,3,-5,6,-4,-3,-10],[-1,8,-8,9,7,-3,9,-10,-4,-9],[4,7,-6,-1,-4,-6,5,-4,2,-6],[-3,3,9,-6,-8,-1,1,-4,-9,-5],[-10,-1,-7,-8,2,-10,-3,5,-8,-6]],[[-8,-3,-6,-5,4,9,3,6,9,-10],[8,-6,-3,-10,1,-9,4,9,9,-5],[4,-4,6,-8,4,7,-8,-10,1,-3],[-9,-3,-4,-2,-6,3,-3,-10,9,-5],[8,6,3,8,-9,8,1,10,6,8],[9,6,10,-10,-6,1,-6,-9,-2,-5],[-7,-8,6,4,10,-8,5,2,9,-2],[8,8,-10,-3,5,-5,2,-1,-1,-10],[8,3,-1,-7,-8,5,4,-10,-2,1],[2,10,-9,-2,-5,-5,-2,6,-3,6],[-6,7,-6,-6,-3,-8,3,1,-8,-4],[7,7,8,-3,-8,2,1,4,10,8]]], dtype = "uint16")#candidate|5396|(11, 12, 10)|const|uint16
const_5397 = relay.const([[[-5,9,10,-10,5,10,-9,10,4,3],[3,4,-2,4,-9,9,6,7,-9,10],[-10,-5,-3,5,7,3,-5,5,-9,1],[4,3,9,7,6,2,-2,-7,4,-4],[1,2,-4,5,3,-3,-9,10,6,-6],[7,-2,-4,3,10,-10,5,-9,6,4],[10,-8,-4,7,-6,-6,-2,3,7,8],[5,8,-8,9,-1,-5,10,1,2,6],[4,2,-8,4,10,3,-7,-5,10,-1],[9,-3,1,-3,-4,2,8,-4,10,-4],[-9,8,-1,-3,9,3,1,-6,-2,5],[7,5,-5,4,6,-8,6,-3,10,-8]],[[-1,8,-9,-4,5,-8,-9,8,2,9],[-1,-5,4,-3,-5,5,2,-9,8,-1],[-1,5,-1,-3,-6,-1,9,1,-7,6],[-5,-9,4,7,9,7,8,1,-7,-2],[-5,8,-2,-5,-5,-10,-4,7,-5,2],[-6,-6,-10,-4,9,10,1,-8,-8,10],[4,2,-9,5,-7,9,-5,6,2,-4],[7,7,-9,1,-9,-1,-2,-10,3,-4],[4,2,10,7,-9,7,3,6,-10,-1],[1,-2,4,4,9,10,3,3,1,7],[8,-7,-9,-5,3,6,8,7,-1,-1],[-8,2,-2,-7,4,4,10,-3,8,6]],[[3,-3,1,5,10,-2,7,-2,-10,2],[4,6,-9,1,-6,-9,2,-2,-4,4],[-2,-4,10,-8,6,-4,7,-2,-8,6],[-1,-5,-8,5,5,-6,6,4,8,4],[-1,2,-8,-4,9,-10,-4,-5,-5,4],[10,5,-2,1,2,-3,6,10,-10,-10],[-4,-3,-9,-1,-9,-2,-5,-6,-9,-6],[-6,3,4,6,8,7,6,2,-8,-10],[10,-7,-3,3,-4,1,9,10,7,-9],[1,9,-6,5,-6,1,8,-10,-3,-1],[1,4,7,-3,-1,-9,8,4,-9,-8],[-5,-10,6,-4,-2,-7,8,-4,7,-9]],[[-2,5,-8,-6,7,1,-2,4,8,9],[2,4,-9,-7,6,7,6,-7,-10,-1],[-6,10,3,8,-2,3,4,6,-6,10],[-8,-9,10,1,9,-6,4,5,-9,-9],[1,-7,-1,-8,7,-8,-8,1,5,5],[-4,10,-6,3,7,8,-6,-5,-9,4],[5,-3,9,9,8,7,-7,-9,-2,-10],[-6,9,5,-7,-8,-4,-2,-4,-3,-6],[-8,-4,-10,8,5,2,-8,3,4,-2],[10,-3,-3,7,1,8,6,4,4,9],[4,1,2,-7,-4,9,3,8,1,1],[-9,-3,2,3,3,-5,3,9,8,4]],[[-3,7,6,-1,3,1,2,6,-3,-9],[-3,3,10,3,-6,-1,-9,4,-6,-2],[-6,2,9,1,9,10,6,-7,-5,-6],[9,-9,-8,4,7,-4,1,2,-5,3],[5,-5,-7,7,3,5,1,-10,9,4],[2,-1,-3,4,-8,-2,-2,-5,-9,3],[6,-4,1,5,-10,8,-6,-6,1,-8],[8,-5,-7,9,1,-10,9,-3,7,-2],[6,10,6,2,7,10,10,-4,-4,-4],[5,5,7,-4,-7,-5,4,-6,1,-2],[7,-4,7,-7,10,-9,5,-9,-1,1],[9,2,1,-8,7,-1,-3,-3,-2,3]],[[-2,-7,6,3,8,5,10,-5,-7,-5],[2,-9,10,5,-2,6,-1,-3,6,6],[2,5,1,2,10,2,-5,9,5,-9],[-2,-3,7,-4,3,-9,1,6,-2,2],[8,-6,-9,8,8,-2,-4,5,-4,4],[-9,4,-7,-6,1,-2,3,3,2,-7],[1,-1,8,-4,-7,2,1,7,-6,-8],[-2,9,-8,-9,-4,-1,8,1,9,8],[6,-3,-6,7,-5,3,3,5,4,2],[-10,4,4,-2,1,-1,2,5,6,3],[5,1,8,9,-9,10,3,-5,-7,2],[-9,-6,8,-10,-1,8,-9,-4,-4,-6]],[[4,-2,8,-2,6,-7,-6,7,-2,8],[10,-1,-6,5,-6,3,-7,-4,2,-3],[1,-3,-3,-1,-9,-10,7,-9,4,3],[5,1,2,-10,-3,-3,3,3,8,10],[-5,8,2,2,-1,8,-2,-9,-6,9],[4,-8,-7,2,5,5,-4,1,-8,4],[8,5,-2,-6,-5,-2,6,5,-8,-1],[1,-2,-8,-3,-6,6,-10,7,9,-2],[8,-5,-1,10,-7,4,-8,5,1,-2],[4,2,1,7,3,-6,3,-5,-2,-6],[7,-9,8,1,-1,-6,-1,10,-10,-3],[4,3,-1,-2,5,-1,7,7,3,5]],[[-1,10,3,-7,5,-5,-9,6,9,2],[7,-6,3,-10,-3,2,-7,-7,2,-5],[-4,-6,1,5,-2,-5,2,1,-7,4],[7,-4,-10,-7,5,-7,-4,-1,7,-6],[3,-7,-3,10,1,-9,-10,7,4,-2],[7,7,4,-4,-2,-1,-2,-7,7,4],[-1,-10,-8,3,-10,2,-4,-9,-6,3],[-3,-2,3,9,-9,9,10,3,6,-9],[-10,-6,-9,-5,5,-3,-10,-5,-8,-2],[1,-7,3,-8,-5,-7,-9,9,5,-5],[2,1,4,-7,-4,9,2,-6,-5,6],[-1,-5,4,-8,-8,9,2,-3,10,9]],[[9,-9,4,-8,2,-9,4,3,9,-7],[6,-8,10,5,1,3,-1,-5,-10,4],[-6,4,10,-10,-9,-6,6,1,5,-3],[-9,-10,-9,-7,-7,-10,5,-5,-1,4],[3,-5,3,-5,4,-9,-4,-5,-4,-3],[-5,-4,-7,7,-3,8,-10,6,-10,6],[-9,-9,1,-8,-6,6,6,-2,-8,-10],[10,10,10,-5,-5,6,-5,-8,9,-1],[-9,-6,6,7,-9,-8,7,-2,2,-9],[10,2,10,-2,-8,-4,2,3,2,-4],[8,-1,-8,4,-10,-8,10,-6,1,-7],[-10,7,3,-10,1,7,5,-6,2,-2]],[[5,-5,-9,-5,-8,9,-5,2,8,2],[-5,9,-8,-5,-7,3,7,8,6,8],[6,-1,-6,1,-4,-3,2,1,7,8],[-2,-7,-6,9,-8,7,-6,7,3,8],[-10,8,-3,4,6,-3,3,-1,4,-5],[7,-8,-10,7,-4,-1,-5,8,10,7],[4,-6,1,9,7,10,4,9,7,-7],[10,-5,9,-3,7,-6,-2,-9,-10,-10],[10,3,10,-10,-7,-5,-9,1,8,-6],[6,6,-4,2,-3,3,2,9,-9,8],[8,-10,-8,6,5,-10,3,8,1,3],[4,-7,-3,10,-5,-7,-4,3,-6,-5]],[[-10,1,-1,3,2,-5,-4,-5,-9,1],[3,-1,3,-6,-1,-3,8,-4,-4,10],[-3,-2,-5,5,2,-10,-2,-10,2,-7],[9,-6,3,-3,-9,4,-7,-8,-5,-8],[9,-10,6,-7,5,3,-1,10,-9,10],[7,-9,-10,9,-9,2,3,-8,-1,-7],[-8,-2,-9,2,7,-7,6,9,4,1],[4,-3,5,-8,-8,-7,-7,-5,3,-6],[9,-5,3,3,3,-3,9,-6,9,3],[8,4,-8,2,6,10,-3,-2,-10,-4],[-9,1,-2,2,-10,-9,-4,-4,1,2],[3,-7,-10,5,-4,-4,-5,-4,-4,8]]], dtype = "uint16")#candidate|5397|(11, 12, 10)|const|uint16
bop_5398 = relay.equal(const_5396.astype('bool'), relay.reshape(const_5397.astype('bool'), relay.shape_of(const_5396))) # shape=(11, 12, 10)
func_2146_call = mod.get_global_var('func_2146')
func_2148_call = mutated_mod.get_global_var('func_2148')
call_5405 = relay.TupleGetItem(func_2146_call(), 0)
call_5406 = relay.TupleGetItem(func_2148_call(), 0)
uop_5423 = relay.asinh(const_5397.astype('float64')) # shape=(11, 12, 10)
uop_5428 = relay.rsqrt(const_5397.astype('float32')) # shape=(11, 12, 10)
func_3326_call = mod.get_global_var('func_3326')
func_3329_call = mutated_mod.get_global_var('func_3329')
const_5435 = relay.const([False,False,False,False,False,True,True,True,False,True,True,False,False,False,False,False,False,False,True,True,True,False,False,True,True,False,True,False,True,True,False,True,False,False,True,False,False,False,False,False,True,True,False,True,False,False,True,False,False,False,True,True,False,True,False,False,True,False,False,False,True,False,True,True,False,False,False,False,False,False,False,False,True,False,True,True,True,True,True,True,True,False,True,False,False,True,False,True,True,False,False,True,False,True,False,False,False,False,True,False,False,True,False,False,False,False,True,True,True,True,False,False,True,True,False,True,True,False,True,False,False,True,True,False,False,False,True,False,False,False,True,True,True,True,True,True,True,False,False,False,True,True,True,True,False,True,False,True,False,True,False,False,False,True,True,True,True,False,True,False,False,False,True,True,False,False,True,True,False,True,False,False,False,True,True,True,False,True,False,False,True,False,True,True,False,False,False,True,False,False,True,False,False,False,True,False,False,False,False,True,False,False,True,False,True,False,True,True,True,False,False,False,False,True,False,False,True,False,False,True,False,True,True,True,False,False,True,False,True,True,True,True,True,False,True,False,False,True,False,False,True,False,False,True,True,False,False,False,True,False,True,True,True,False,False,True], dtype = "bool")#candidate|5435|(256,)|const|bool
call_5434 = relay.TupleGetItem(func_3326_call(relay.reshape(const_5435.astype('bool'), [256,])), 1)
call_5436 = relay.TupleGetItem(func_3329_call(relay.reshape(const_5435.astype('bool'), [256,])), 1)
output = relay.Tuple([bop_5398,call_5405,uop_5423,uop_5428,call_5434,const_5435,])
output2 = relay.Tuple([bop_5398,call_5406,uop_5423,uop_5428,call_5436,const_5435,])
func_5438 = relay.Function([], output)
mod['func_5438'] = func_5438
mod = relay.transform.InferType()(mod)
mutated_mod['func_5438'] = func_5438
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5438_call = mutated_mod.get_global_var('func_5438')
call_5439 = func_5438_call()
output = call_5439
func_5440 = relay.Function([], output)
mutated_mod['func_5440'] = func_5440
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3013_call = mod.get_global_var('func_3013')
func_3015_call = mutated_mod.get_global_var('func_3015')
call_5450 = func_3013_call()
call_5451 = func_3013_call()
var_5457 = relay.var("var_5457", dtype = "bool", shape = (64, 6))#candidate|5457|(64, 6)|var|bool
bop_5458 = relay.bitwise_or(call_5450.astype('uint8'), relay.reshape(var_5457.astype('uint8'), relay.shape_of(call_5450))) # shape=(64, 6)
bop_5461 = relay.bitwise_or(call_5451.astype('uint8'), relay.reshape(var_5457.astype('uint8'), relay.shape_of(call_5451))) # shape=(64, 6)
bop_5464 = relay.logical_xor(var_5457.astype('int64'), relay.reshape(call_5450.astype('int64'), relay.shape_of(var_5457))) # shape=(64, 6)
bop_5467 = relay.logical_xor(var_5457.astype('int64'), relay.reshape(call_5451.astype('int64'), relay.shape_of(var_5457))) # shape=(64, 6)
bop_5497 = relay.bitwise_xor(bop_5458.astype('int8'), relay.reshape(var_5457.astype('int8'), relay.shape_of(bop_5458))) # shape=(64, 6)
bop_5500 = relay.bitwise_xor(bop_5461.astype('int8'), relay.reshape(var_5457.astype('int8'), relay.shape_of(bop_5461))) # shape=(64, 6)
output = relay.Tuple([bop_5464,bop_5497,])
output2 = relay.Tuple([bop_5467,bop_5500,])
func_5501 = relay.Function([var_5457,], output)
mod['func_5501'] = func_5501
mod = relay.transform.InferType()(mod)
var_5502 = relay.var("var_5502", dtype = "bool", shape = (64, 6))#candidate|5502|(64, 6)|var|bool
output = func_5501(var_5502)
func_5503 = relay.Function([var_5502], output)
mutated_mod['func_5503'] = func_5503
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5566 = relay.var("var_5566", dtype = "float32", shape = (15, 16, 3))#candidate|5566|(15, 16, 3)|var|float32
var_5567 = relay.var("var_5567", dtype = "float32", shape = (15, 16, 3))#candidate|5567|(15, 16, 3)|var|float32
bop_5568 = relay.mod(var_5566.astype('float32'), relay.reshape(var_5567.astype('float32'), relay.shape_of(var_5566))) # shape=(15, 16, 3)
func_2596_call = mod.get_global_var('func_2596')
func_2600_call = mutated_mod.get_global_var('func_2600')
var_5575 = relay.var("var_5575", dtype = "float64", shape = (120,))#candidate|5575|(120,)|var|float64
var_5576 = relay.var("var_5576", dtype = "float64", shape = (1560,))#candidate|5576|(1560,)|var|float64
var_5577 = relay.var("var_5577", dtype = "float64", shape = (1920,))#candidate|5577|(1920,)|var|float64
call_5574 = relay.TupleGetItem(func_2596_call(relay.reshape(var_5575.astype('float64'), [1, 8, 15]), relay.reshape(var_5576.astype('float64'), [13, 8, 15]), relay.reshape(var_5577.astype('float64'), [96, 20]), ), 2)
call_5578 = relay.TupleGetItem(func_2600_call(relay.reshape(var_5575.astype('float64'), [1, 8, 15]), relay.reshape(var_5576.astype('float64'), [13, 8, 15]), relay.reshape(var_5577.astype('float64'), [96, 20]), ), 2)
func_2814_call = mod.get_global_var('func_2814')
func_2816_call = mutated_mod.get_global_var('func_2816')
call_5582 = relay.TupleGetItem(func_2814_call(), 1)
call_5583 = relay.TupleGetItem(func_2816_call(), 1)
output = relay.Tuple([bop_5568,call_5574,var_5575,var_5576,var_5577,call_5582,])
output2 = relay.Tuple([bop_5568,call_5578,var_5575,var_5576,var_5577,call_5583,])
func_5594 = relay.Function([var_5566,var_5567,var_5575,var_5576,var_5577,], output)
mod['func_5594'] = func_5594
mod = relay.transform.InferType()(mod)
mutated_mod['func_5594'] = func_5594
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5594_call = mutated_mod.get_global_var('func_5594')
var_5596 = relay.var("var_5596", dtype = "float32", shape = (15, 16, 3))#candidate|5596|(15, 16, 3)|var|float32
var_5597 = relay.var("var_5597", dtype = "float32", shape = (15, 16, 3))#candidate|5597|(15, 16, 3)|var|float32
var_5598 = relay.var("var_5598", dtype = "float64", shape = (120,))#candidate|5598|(120,)|var|float64
var_5599 = relay.var("var_5599", dtype = "float64", shape = (1560,))#candidate|5599|(1560,)|var|float64
var_5600 = relay.var("var_5600", dtype = "float64", shape = (1920,))#candidate|5600|(1920,)|var|float64
call_5595 = func_5594_call(var_5596,var_5597,var_5598,var_5599,var_5600,)
output = call_5595
func_5601 = relay.Function([var_5596,var_5597,var_5598,var_5599,var_5600,], output)
mutated_mod['func_5601'] = func_5601
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1017_call = mod.get_global_var('func_1017')
func_1018_call = mutated_mod.get_global_var('func_1018')
call_5607 = relay.TupleGetItem(func_1017_call(), 1)
call_5608 = relay.TupleGetItem(func_1018_call(), 1)
func_4637_call = mod.get_global_var('func_4637')
func_4638_call = mutated_mod.get_global_var('func_4638')
call_5624 = func_4637_call()
call_5625 = func_4637_call()
func_3013_call = mod.get_global_var('func_3013')
func_3015_call = mutated_mod.get_global_var('func_3015')
call_5632 = func_3013_call()
call_5633 = func_3013_call()
var_5643 = relay.var("var_5643", dtype = "bool", shape = (64, 6))#candidate|5643|(64, 6)|var|bool
bop_5644 = relay.add(call_5632.astype('float32'), relay.reshape(var_5643.astype('float32'), relay.shape_of(call_5632))) # shape=(64, 6)
bop_5647 = relay.add(call_5633.astype('float32'), relay.reshape(var_5643.astype('float32'), relay.shape_of(call_5633))) # shape=(64, 6)
output = relay.Tuple([call_5607,call_5624,bop_5644,])
output2 = relay.Tuple([call_5608,call_5625,bop_5647,])
func_5650 = relay.Function([var_5643,], output)
mod['func_5650'] = func_5650
mod = relay.transform.InferType()(mod)
var_5651 = relay.var("var_5651", dtype = "bool", shape = (64, 6))#candidate|5651|(64, 6)|var|bool
output = func_5650(var_5651)
func_5652 = relay.Function([var_5651], output)
mutated_mod['func_5652'] = func_5652
mutated_mod = relay.transform.InferType()(mutated_mod)
func_295_call = mod.get_global_var('func_295')
func_297_call = mutated_mod.get_global_var('func_297')
call_5693 = relay.TupleGetItem(func_295_call(), 0)
call_5694 = relay.TupleGetItem(func_297_call(), 0)
output = relay.Tuple([call_5693,])
output2 = relay.Tuple([call_5694,])
func_5724 = relay.Function([], output)
mod['func_5724'] = func_5724
mod = relay.transform.InferType()(mod)
mutated_mod['func_5724'] = func_5724
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5724_call = mutated_mod.get_global_var('func_5724')
call_5725 = func_5724_call()
output = call_5725
func_5726 = relay.Function([], output)
mutated_mod['func_5726'] = func_5726
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5738 = relay.const([[[-4.756782,-5.564986,-4.512224,7.437043,-1.552595,1.332872,-9.723499,-6.131756,-4.501900,4.307830,3.395553,3.626831,-2.022878,-3.031495],[-3.567593,-4.128753,4.980858,6.802345,5.673123,3.270827,1.142050,-9.539873,2.216133,-9.967122,-5.366854,3.184772,2.121919,9.701782],[-9.650385,-8.345167,5.137415,-6.288744,6.019499,-2.117056,-2.742143,0.545378,9.065972,7.368437,-0.057849,-9.464147,0.618110,-9.439671],[-4.670648,6.619262,7.141227,0.722052,-4.154557,0.986089,-3.004764,-2.170552,-1.024629,-1.149200,-2.813474,-0.712341,-9.059297,4.052904],[-8.083626,-3.493978,-7.632064,-4.773801,-1.052573,-1.604831,5.059140,-7.639154,-0.462830,-3.870786,-0.560139,-8.103014,0.826271,-8.079138],[0.255143,9.966432,4.246065,-3.892264,2.770020,-2.971730,9.657619,2.397695,-8.524745,-7.210498,-5.105813,8.718110,4.780726,3.438318],[-4.624672,-1.992309,-7.888659,-6.447390,-5.011339,5.339109,8.747745,8.023941,-4.904402,4.647882,-5.383965,3.825188,-3.308977,-4.612478],[-8.373769,-5.013678,8.246756,-2.691683,6.119186,2.331092,-9.531463,1.277074,-8.282506,-7.185794,1.723689,-9.829867,9.718829,5.639831],[-8.128994,3.027903,1.337705,-7.105915,8.569841,-6.110793,2.277162,-3.580222,-5.280305,7.293875,-9.963788,-6.286185,1.178330,0.543765],[-1.021610,-2.441189,-5.803525,-3.340320,-5.152964,-7.487797,5.174892,-5.653971,6.417257,-0.555445,-3.227981,-6.675859,9.408059,8.508826],[9.744163,1.479599,1.554209,7.180026,-1.539193,8.286271,-6.987772,-8.910278,9.305475,-1.743664,9.242435,-4.657100,-7.024309,-0.436383],[8.263753,-4.957083,-1.838330,0.458740,4.307947,-9.152404,-2.704831,-0.495338,7.898931,-1.204918,6.191002,4.872214,-6.563564,1.133489],[8.628371,-2.669042,5.786938,8.203457,8.595480,4.568929,9.538917,-9.183270,7.399807,-8.066381,5.160716,1.473816,3.427510,0.764310],[1.660328,-0.280433,-6.883129,2.038255,5.220035,6.693263,5.434594,-4.791668,-2.004469,-4.931732,6.600695,2.488439,-8.996597,-2.815324],[7.779926,7.466442,-3.094647,5.345777,-2.770110,-9.817798,-3.108760,-7.140102,-1.870778,-4.187512,5.629715,-6.477086,-9.261435,5.983992],[6.646142,-9.885208,5.141960,1.297844,-2.299520,-2.489139,8.844852,-0.038296,5.462799,-7.287600,6.502464,-0.163946,4.926105,-6.622650]],[[-9.801804,-7.916845,5.572391,3.779136,-4.113017,-5.384319,1.927246,-0.003363,4.055272,-1.034943,4.312668,-0.726519,-2.846114,-2.395838],[3.580713,1.762592,-5.572634,8.469375,-9.793588,5.843415,5.676984,6.211854,-0.650138,-0.706449,5.780283,-0.407605,8.552899,2.452049],[-4.144969,8.464231,-6.521690,1.386487,5.640616,-7.215117,9.583327,-9.337237,0.621387,-2.103854,5.890984,4.456075,3.342240,-8.853107],[-5.377666,-9.036343,7.069901,5.697064,-9.815730,-3.718240,5.995449,-2.927230,-6.652504,-8.980304,-8.252334,-0.962995,5.817811,-0.109681],[7.898988,0.331785,1.967900,-4.995715,4.671448,-8.785306,5.641163,7.214496,-2.606991,0.662708,6.011610,-0.287546,-7.997855,5.067904],[9.273924,0.378042,-1.927801,-5.550477,-3.124198,-5.139219,-0.434146,-9.478602,-5.145753,2.806043,0.884988,6.289445,-9.769216,-6.253982],[-9.115049,-1.244930,-9.836889,6.582962,-9.236538,-8.234995,-6.189147,-8.443503,5.228997,-5.764359,9.369390,-5.785687,3.337247,2.164712],[-0.652773,-1.902264,5.912314,-8.942928,-8.830566,4.433831,0.527287,-0.603424,-8.466222,1.647981,4.444143,0.154631,5.542191,6.075051],[-7.404652,-6.767088,-6.318322,2.920245,4.258640,5.762730,6.757629,-2.177114,-8.551186,4.514883,4.364633,3.353604,-7.034467,7.241330],[-3.304632,-5.524325,0.780782,3.228938,-1.873157,-5.258507,-4.572012,4.833215,-6.229509,8.312597,-4.846940,6.662052,4.569077,-6.338442],[-6.613479,5.917134,-4.742084,1.904694,-3.941951,-8.224390,8.727807,-6.706893,-2.994797,-7.786443,8.519572,-4.230577,-2.473225,1.223460],[-7.555795,2.231117,-7.780645,2.714018,8.471449,-2.687744,-3.717395,-8.141974,2.835342,6.585106,-3.052628,-4.988005,7.009494,-2.734247],[9.199863,8.570632,8.265415,-8.399186,4.552334,3.647833,-9.676174,-3.216520,-2.651399,-3.462851,6.977718,7.140254,5.890273,8.948846],[-2.548596,-5.473317,-6.151054,4.176689,0.232471,9.350443,-6.844422,5.884111,-7.385891,1.088613,-9.136090,4.659531,4.265076,2.786083],[-3.535796,-5.879988,-9.721298,-9.932099,-3.824948,9.507125,2.289388,6.809939,6.809182,-8.383594,-8.127081,-7.853588,-3.118235,0.850743],[-3.165368,-6.159821,8.893662,-6.688253,-6.163888,-6.890474,-8.622778,-1.262424,-5.527578,1.959260,-9.319988,-6.954610,0.255941,1.881152]],[[-2.538371,-2.703204,1.394206,0.652555,5.416172,0.366487,1.671657,-9.975221,1.903674,2.451477,-1.327083,2.682874,2.640783,-8.125206],[-3.356741,-1.810787,-1.318150,5.072739,0.802164,-1.241888,-6.544703,-4.804997,-3.540814,-2.925649,1.475076,2.549125,-6.856325,-0.984708],[-4.955341,9.859896,-7.310224,4.811329,-9.974170,6.026908,-5.791707,-2.890753,9.142220,-4.215072,2.861070,5.095372,-7.941330,8.313744],[5.226407,-5.904344,-4.175670,-4.567314,7.305294,3.967436,-9.483646,-2.847144,-6.745598,-7.167316,8.153887,9.156843,5.255748,-2.830883],[-0.639668,-4.860991,5.893916,5.819486,-6.515320,7.939340,-9.418416,2.400166,7.609534,1.003211,-9.755794,6.235632,-9.986951,0.445075],[9.053035,4.226238,0.679224,1.979792,9.860961,-8.394397,-2.376881,8.023394,-8.442555,4.139147,-5.157396,1.658498,-1.397938,3.874876],[-4.668587,-4.259524,-5.594587,2.734447,-5.243607,-9.832226,1.720178,2.451906,-6.955508,-7.130430,-0.852387,-2.804693,-0.867069,5.953321],[-5.452744,4.989726,7.429120,-1.122239,-2.783040,9.167675,-5.053398,-2.207124,-5.797309,8.850623,-3.797332,4.249319,-7.622724,-5.190201],[-4.273564,5.764815,-7.841002,8.819608,7.197260,6.458625,1.868763,-1.304156,-5.670853,0.876771,-9.308835,-7.488907,5.565102,1.658313],[4.743161,-1.943473,-9.343885,1.564589,8.526604,-5.628370,-2.676463,-7.599826,6.123108,-7.488351,5.251663,-1.420342,-4.881202,-2.942994],[6.981691,1.473832,1.428605,-6.879644,-9.366213,-7.160979,-2.070252,-0.830983,-6.621872,-3.622003,4.303658,-3.408022,-0.619369,-7.372408],[8.510390,-1.585668,4.453918,6.686178,-9.188706,-8.597306,0.828454,-0.372698,0.630904,9.916137,9.174834,2.759071,-2.888632,9.250501],[3.529145,3.987922,-1.559683,1.042998,-5.549321,2.812197,-9.663683,5.223859,-1.200990,9.368887,-5.223581,-5.683184,-4.775612,-4.177142],[8.923834,4.116936,8.234670,8.925911,6.301696,6.236464,9.455411,-1.137170,-0.071427,-5.841557,4.392331,4.464839,-0.316693,1.955089],[8.359420,4.678973,7.121927,2.593765,5.529622,-0.850098,3.900873,-9.469227,-8.225444,-5.027697,-2.894507,-8.375062,-6.072133,2.483271],[1.809061,9.214099,-2.307908,0.570385,-5.399708,2.431745,2.049140,-3.028220,8.961275,2.942535,3.057268,1.554863,-3.772049,4.352724]],[[2.223255,5.771122,0.409706,2.101141,0.211731,1.716573,-7.714485,-5.645252,-5.319484,-8.703203,1.187343,-4.445156,-5.526112,4.290086],[2.791901,8.796136,7.504003,0.627094,-4.016838,6.450465,1.540252,8.700074,3.031614,6.031367,-4.214668,9.152019,4.575999,-4.497020],[4.585193,1.775189,-6.816741,6.391294,8.745158,-8.472495,-5.803003,-8.859022,-5.425164,5.443333,0.731979,8.311893,-6.020609,3.454527],[-8.066930,8.864994,0.278037,-9.959325,-0.177256,-4.011442,-4.073800,5.377216,-8.419729,-0.480662,0.614442,-2.406178,-6.673762,-2.941096],[-9.649488,1.440142,2.536547,0.807270,6.632159,-0.233548,7.506704,0.123745,8.027846,-7.394066,-1.501003,-0.526876,-4.926957,-0.330771],[-4.409313,-1.117069,8.422346,-8.214073,-4.175644,9.185494,8.694233,0.388258,-2.009066,2.798321,1.130338,3.766555,-7.986869,7.085649],[-2.544329,-4.295764,-3.571654,-2.870838,-6.538001,-8.439359,-9.466416,-6.164637,0.319328,-6.781528,-5.224184,7.657324,-6.385827,-5.222938],[-4.526420,7.959135,1.585590,-2.491895,-9.059282,3.235009,8.574666,-1.154729,-0.543899,4.265329,-2.289099,8.298074,0.298722,8.374578],[-9.615990,4.653306,9.640225,9.948147,-6.245095,0.254747,-9.196187,0.274884,-5.606221,6.396214,-0.540066,2.555234,5.185471,5.646549],[4.684453,-9.931321,-3.104028,2.432936,-0.733026,1.090415,-5.503316,-7.187741,0.777259,-0.446219,3.895251,-6.241147,-9.915011,-3.662622],[5.009528,6.353476,-1.384042,-8.367754,6.985139,2.429528,-3.387198,-0.349531,7.550504,-5.213176,-7.478932,-4.930872,-2.036210,2.786233],[-8.107988,-9.138687,9.388471,8.524250,8.574064,8.141956,7.250610,3.763521,1.541708,-4.267283,-2.910295,8.926535,4.246779,-0.634005],[5.165650,-8.490009,7.803350,9.557627,-6.325622,1.068307,-7.293266,-9.137928,5.466556,2.034772,4.502112,2.932505,-0.531503,-9.028225],[-0.571526,-8.221678,-1.752996,-7.159688,3.133091,8.708715,-4.029673,-6.912286,3.159169,-4.162014,-5.119718,2.084285,6.918294,0.876860],[8.902810,2.072602,-5.496631,0.232071,-0.473550,-6.399089,3.241825,-7.921447,-0.362067,-6.586818,5.972555,-6.111016,3.739465,-4.940645],[-8.446726,-5.122431,1.540215,-2.426768,8.103212,5.164844,1.691790,-7.592355,3.083256,-2.470584,1.276910,6.009846,6.567899,-3.413649]]], dtype = "float64")#candidate|5738|(4, 16, 14)|const|float64
uop_5739 = relay.rsqrt(const_5738.astype('float64')) # shape=(4, 16, 14)
func_2430_call = mod.get_global_var('func_2430')
func_2431_call = mutated_mod.get_global_var('func_2431')
call_5752 = relay.TupleGetItem(func_2430_call(), 1)
call_5753 = relay.TupleGetItem(func_2431_call(), 1)
output = relay.Tuple([uop_5739,call_5752,])
output2 = relay.Tuple([uop_5739,call_5753,])
func_5767 = relay.Function([], output)
mod['func_5767'] = func_5767
mod = relay.transform.InferType()(mod)
output = func_5767()
func_5768 = relay.Function([], output)
mutated_mod['func_5768'] = func_5768
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2814_call = mod.get_global_var('func_2814')
func_2816_call = mutated_mod.get_global_var('func_2816')
call_5772 = relay.TupleGetItem(func_2814_call(), 0)
call_5773 = relay.TupleGetItem(func_2816_call(), 0)
output = call_5772
output2 = call_5773
func_5783 = relay.Function([], output)
mod['func_5783'] = func_5783
mod = relay.transform.InferType()(mod)
output = func_5783()
func_5784 = relay.Function([], output)
mutated_mod['func_5784'] = func_5784
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4033_call = mod.get_global_var('func_4033')
func_4034_call = mutated_mod.get_global_var('func_4034')
call_5853 = relay.TupleGetItem(func_4033_call(), 0)
call_5854 = relay.TupleGetItem(func_4034_call(), 0)
func_2891_call = mod.get_global_var('func_2891')
func_2893_call = mutated_mod.get_global_var('func_2893')
var_5857 = relay.var("var_5857", dtype = "bool", shape = (144, 4))#candidate|5857|(144, 4)|var|bool
call_5856 = relay.TupleGetItem(func_2891_call(relay.reshape(var_5857.astype('bool'), [12, 48])), 1)
call_5858 = relay.TupleGetItem(func_2893_call(relay.reshape(var_5857.astype('bool'), [12, 48])), 1)
var_5860 = relay.var("var_5860", dtype = "bool", shape = (64, 6))#candidate|5860|(64, 6)|var|bool
bop_5861 = relay.floor_divide(call_5853.astype('float64'), relay.reshape(var_5860.astype('float64'), relay.shape_of(call_5853))) # shape=(64, 6)
bop_5864 = relay.floor_divide(call_5854.astype('float64'), relay.reshape(var_5860.astype('float64'), relay.shape_of(call_5854))) # shape=(64, 6)
bop_5868 = relay.mod(var_5860.astype('float32'), relay.reshape(bop_5861.astype('float32'), relay.shape_of(var_5860))) # shape=(64, 6)
bop_5871 = relay.mod(var_5860.astype('float32'), relay.reshape(bop_5864.astype('float32'), relay.shape_of(var_5860))) # shape=(64, 6)
uop_5873 = relay.asin(var_5860.astype('float64')) # shape=(64, 6)
var_5881 = relay.var("var_5881", dtype = "float64", shape = (64, 6))#candidate|5881|(64, 6)|var|float64
bop_5882 = relay.right_shift(uop_5873.astype('uint8'), relay.reshape(var_5881.astype('uint8'), relay.shape_of(uop_5873))) # shape=(64, 6)
bop_5887 = relay.logical_and(bop_5882.astype('bool'), relay.reshape(call_5853.astype('bool'), relay.shape_of(bop_5882))) # shape=(64, 6)
bop_5890 = relay.logical_and(bop_5882.astype('bool'), relay.reshape(call_5854.astype('bool'), relay.shape_of(bop_5882))) # shape=(64, 6)
func_2866_call = mod.get_global_var('func_2866')
func_2868_call = mutated_mod.get_global_var('func_2868')
const_5899 = relay.const([[3.923878],[3.395715],[8.265294],[-4.835355],[-7.054139],[-7.872618],[-8.955859],[8.356479],[-4.440239],[-3.744293],[-1.649905],[-2.484689],[0.164732],[9.096094],[-0.806496],[2.415861],[7.392030],[7.042702],[-3.510967],[5.009899],[1.792981],[-7.366632],[-1.453324],[-8.341446],[-5.942187],[-5.176595],[-9.706103],[5.797262],[-1.502053],[5.563977],[3.630228],[-6.290912],[1.065723],[0.874994],[-9.423487],[3.505415],[-5.764164],[1.702206],[0.531337],[7.084061],[-9.592989],[-5.404897],[2.284771],[1.013904],[-2.311180],[-6.614218],[1.463493],[3.262031],[-7.190141],[-9.599774],[8.112149],[-6.817256],[-6.764929],[3.221411],[-3.433396],[2.314985],[-6.463243],[8.891242],[-0.845153],[4.610727],[-5.025183],[-0.838924],[-0.294615],[-4.019742],[-8.237840],[7.813735],[-8.171702],[-1.126289],[-4.446979],[-0.248026],[-7.503594],[4.476391],[6.830691],[-6.583693],[4.607206],[7.965170],[2.465979],[8.898459],[1.007829],[9.899379],[8.310306],[4.361106],[-7.937363],[-1.679805],[7.624628],[9.578730],[-9.622119],[-6.021779],[-5.636730],[1.259413],[-5.604316],[6.115071],[-0.726810],[-9.507958],[-6.048014],[-0.613269],[-7.965370],[-6.391924],[6.232304],[7.322216],[1.454464],[-3.741975],[-1.802322],[-9.498579],[-7.736312],[-8.873662],[-2.216449],[-5.719450],[5.854402],[-9.826957],[-4.184912],[9.928592],[-9.487848],[-7.138099],[-8.918161],[5.839877],[-6.576934],[2.630659],[-3.916329],[3.843186],[-6.387752],[-5.973143],[3.177247],[5.674575],[4.309794],[1.714552],[-0.747842],[-5.882843],[-4.556779],[-4.113047],[6.902684],[-8.061409],[-9.344198],[-9.530801],[6.746406],[1.313248],[9.852413],[-2.701248],[-9.959775],[2.234154],[7.454592],[-9.499694],[4.154957],[3.778607],[9.119350],[-0.030313],[8.524398],[-1.716612],[3.526176],[-7.385337],[6.747529],[-4.187768],[7.427406],[6.013935],[-7.242464],[1.028126],[3.938487],[-6.044002],[3.504943],[-7.079446],[1.751027],[5.330558],[-0.721800],[-6.827413],[-7.314857],[-7.288736],[-0.778208],[-0.906953],[-8.277218],[-4.597796],[9.167011],[-5.190939],[8.508474],[5.988365],[-7.083631],[5.678129],[3.870241],[-7.423166],[-2.097194],[2.616079],[-2.335394],[-5.587581],[-7.662154],[-4.045546],[2.952304],[1.359972],[9.769574],[3.346808],[-7.195775],[7.319479],[4.475817],[1.224021],[0.738379],[-1.295047],[-8.027760],[-1.717398],[0.786717],[-6.667167],[2.449751],[-8.356654],[3.099604],[1.117535],[-0.398754],[6.894792],[-1.361387],[2.418830],[6.173094],[-5.757909],[6.964451],[-4.418084],[-5.354446],[-7.887305],[-0.053648],[2.970794],[2.797210],[-5.988438],[2.604912],[7.308391],[-1.150284],[5.447328],[1.586213],[-8.772339],[1.300520],[2.812645],[6.114062],[-5.821407],[-5.794442],[-8.023816],[5.571621],[3.066622],[3.723653],[3.836001],[4.114893],[-7.255456],[4.128933],[-7.661507],[8.829894],[0.397203],[3.067067],[6.457670],[9.705291],[-1.274128],[-2.000993],[-2.631318],[-9.202698],[-0.947651],[6.099054],[3.202174],[7.406983],[-6.505345],[7.412399],[7.801739],[-1.617120],[9.254500],[-4.099819],[-8.010490],[-0.821917],[9.125242],[6.376690],[8.830848],[0.030087],[-9.283687],[4.021144],[-7.143925],[9.646051],[-6.714424],[0.996825],[5.055377],[-9.239987],[-8.921794],[1.032809],[-9.424501],[9.441302],[-4.902001],[8.770667],[0.850440],[-9.779105],[3.845693],[8.064924],[-1.626573],[6.444068],[9.514364],[-0.147951],[-2.395620],[5.228693],[3.754208],[4.924637],[-2.126831],[-3.050265],[-6.108287],[-3.900145],[-9.819116],[7.610839],[1.983935],[3.299062],[0.439195],[-0.255256],[-0.561479],[-4.206912],[5.302732],[9.061880],[-6.238796],[9.211837],[4.616217],[-8.023467],[0.234590],[8.260545],[0.623799],[-5.511777],[2.482474],[-8.649139],[-5.629039],[2.424495],[4.080729],[9.657624],[7.256367],[-1.297829],[3.856254],[0.359473],[6.380220],[-3.783955],[-0.983768],[-8.757774],[-5.248267],[-8.665281],[2.861798],[5.640378],[0.043467],[-1.772020],[-7.666182],[-5.750260],[-3.863682],[1.850209],[-7.108544],[-5.097369],[-9.563787],[-8.933340],[9.887534],[-1.606265],[5.841330],[5.190404],[4.653619],[-0.545329],[-0.963792],[-8.713153],[-2.625695],[-2.382582],[4.338035],[9.847375],[-7.030817],[7.792986],[-0.670899],[-4.236823],[-6.289464],[-1.570416],[9.155337],[-3.913166],[-4.930275],[-2.912489],[7.332136],[7.129269],[0.804828],[-0.839560],[3.480951],[-4.886974],[-6.197967],[4.896387],[9.089023],[-8.273091],[-8.845870],[-4.127205],[-7.344675],[1.459874],[3.891257],[9.889115],[-1.996011],[0.998679],[5.252430],[-4.264172],[2.213709],[-9.047232],[-3.799339],[-6.436546],[4.639806],[0.474992],[2.461058],[-2.459204],[0.801007],[-8.663005],[4.806287],[5.148531],[-7.884326],[1.780509],[9.040720],[7.940405],[-0.726711],[-0.129447],[8.231905],[-7.887937],[2.316814],[-2.585559],[8.575660],[-8.328016],[-8.361559],[-5.360807],[1.749725],[0.472930],[-5.055029],[6.120379],[-3.451654],[-5.461002],[-6.716037],[5.732380],[1.550236],[9.703555],[-1.509801],[-3.233172],[-8.257841],[-0.361129],[6.839294],[-0.143606],[-1.338610],[3.499762],[-7.553300],[-7.671310],[5.114682],[6.686320],[0.940444],[3.708752],[-4.097945],[5.079321],[-9.710805],[7.990416],[1.064230],[-2.294209],[-1.494896],[8.498740],[-1.038834],[3.746361],[1.917948],[-7.504201],[-4.157159],[-9.499086],[-5.769822],[-3.793724],[-3.980999],[7.508010],[9.869457],[0.295212],[-7.728657],[-4.987817],[-3.544491],[-5.997538],[-9.885720],[6.556837],[7.379128],[-4.449066],[8.055343],[-0.815810],[-5.672070],[0.332933],[-9.956104],[9.777914],[8.037308],[-3.900873],[-0.386009],[-1.439010],[-5.483842],[-1.077837],[-5.988346],[-6.496860],[3.112272],[1.791148],[-0.940974],[-4.328196],[-0.338186],[1.880612],[9.625600],[0.871856],[-0.611663],[-9.017640],[-0.793073],[9.908720],[3.473376],[0.470445],[-6.459511],[-3.681011],[-2.530495],[-6.280352],[0.303057],[4.474408],[-0.801814],[-4.282475],[6.140911],[-6.609197],[-7.848282],[2.612899],[3.558890],[7.689638],[-4.002708],[-5.963222],[1.797698],[-7.272712],[-9.604306],[-4.666638],[9.316861],[-0.703571],[-5.495568],[3.709241],[-8.075214],[7.950728],[4.360452]], dtype = "float32")#candidate|5899|(512, 1)|const|float32
call_5898 = relay.TupleGetItem(func_2866_call(relay.reshape(const_5899.astype('float32'), [64, 8])), 1)
call_5900 = relay.TupleGetItem(func_2868_call(relay.reshape(const_5899.astype('float32'), [64, 8])), 1)
func_2146_call = mod.get_global_var('func_2146')
func_2148_call = mutated_mod.get_global_var('func_2148')
call_5906 = relay.TupleGetItem(func_2146_call(), 0)
call_5907 = relay.TupleGetItem(func_2148_call(), 0)
func_5724_call = mod.get_global_var('func_5724')
func_5726_call = mutated_mod.get_global_var('func_5726')
call_5911 = relay.TupleGetItem(func_5724_call(), 0)
call_5912 = relay.TupleGetItem(func_5726_call(), 0)
uop_5916 = relay.tan(bop_5882.astype('float32')) # shape=(64, 6)
func_706_call = mod.get_global_var('func_706')
func_708_call = mutated_mod.get_global_var('func_708')
var_5921 = relay.var("var_5921", dtype = "float64", shape = (660,))#candidate|5921|(660,)|var|float64
call_5920 = relay.TupleGetItem(func_706_call(relay.reshape(var_5921.astype('float64'), [11, 10, 6])), 2)
call_5922 = relay.TupleGetItem(func_708_call(relay.reshape(var_5921.astype('float64'), [11, 10, 6])), 2)
uop_5933 = relay.atan(uop_5873.astype('float32')) # shape=(64, 6)
output = relay.Tuple([call_5856,var_5857,bop_5868,bop_5887,call_5898,const_5899,call_5906,call_5911,uop_5916,call_5920,var_5921,uop_5933,])
output2 = relay.Tuple([call_5858,var_5857,bop_5871,bop_5890,call_5900,const_5899,call_5907,call_5912,uop_5916,call_5922,var_5921,uop_5933,])
func_5941 = relay.Function([var_5857,var_5860,var_5881,var_5921,], output)
mod['func_5941'] = func_5941
mod = relay.transform.InferType()(mod)
var_5942 = relay.var("var_5942", dtype = "bool", shape = (144, 4))#candidate|5942|(144, 4)|var|bool
var_5943 = relay.var("var_5943", dtype = "bool", shape = (64, 6))#candidate|5943|(64, 6)|var|bool
var_5944 = relay.var("var_5944", dtype = "float64", shape = (64, 6))#candidate|5944|(64, 6)|var|float64
var_5945 = relay.var("var_5945", dtype = "float64", shape = (660,))#candidate|5945|(660,)|var|float64
output = func_5941(var_5942,var_5943,var_5944,var_5945,)
func_5946 = relay.Function([var_5942,var_5943,var_5944,var_5945,], output)
mutated_mod['func_5946'] = func_5946
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2814_call = mod.get_global_var('func_2814')
func_2816_call = mutated_mod.get_global_var('func_2816')
call_5965 = relay.TupleGetItem(func_2814_call(), 0)
call_5966 = relay.TupleGetItem(func_2816_call(), 0)
func_5308_call = mod.get_global_var('func_5308')
func_5309_call = mutated_mod.get_global_var('func_5309')
call_5973 = relay.TupleGetItem(func_5308_call(), 0)
call_5974 = relay.TupleGetItem(func_5309_call(), 0)
output = relay.Tuple([call_5965,call_5973,])
output2 = relay.Tuple([call_5966,call_5974,])
func_5981 = relay.Function([], output)
mod['func_5981'] = func_5981
mod = relay.transform.InferType()(mod)
output = func_5981()
func_5982 = relay.Function([], output)
mutated_mod['func_5982'] = func_5982
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4797_call = mod.get_global_var('func_4797')
func_4798_call = mutated_mod.get_global_var('func_4798')
call_6036 = relay.TupleGetItem(func_4797_call(), 0)
call_6037 = relay.TupleGetItem(func_4798_call(), 0)
output = relay.Tuple([call_6036,])
output2 = relay.Tuple([call_6037,])
func_6045 = relay.Function([], output)
mod['func_6045'] = func_6045
mod = relay.transform.InferType()(mod)
mutated_mod['func_6045'] = func_6045
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6045_call = mutated_mod.get_global_var('func_6045')
call_6046 = func_6045_call()
output = call_6046
func_6047 = relay.Function([], output)
mutated_mod['func_6047'] = func_6047
mutated_mod = relay.transform.InferType()(mutated_mod)
func_391_call = mod.get_global_var('func_391')
func_392_call = mutated_mod.get_global_var('func_392')
call_6150 = func_391_call()
call_6151 = func_391_call()
uop_6152 = relay.log2(call_6150.astype('float64')) # shape=(64, 6)
uop_6154 = relay.log2(call_6151.astype('float64')) # shape=(64, 6)
const_6158 = relay.const([[5.412865,-4.732610,-6.574479,-4.644982,-5.593135,1.117028],[-4.419186,-0.194340,7.273226,0.513650,-7.889355,8.261095],[-2.134447,7.101791,-7.056245,-8.514976,-5.435224,2.914274],[-0.696033,9.183270,-9.705386,6.212981,7.804501,7.683529],[-0.508185,2.566468,9.710131,-3.683125,-1.494895,7.595853],[-5.776016,-8.144963,-0.871334,5.053103,4.015461,2.260427],[8.214992,4.900558,-6.953531,5.601889,6.884579,7.583065],[-1.940454,7.935075,-5.185162,1.524799,-8.696316,4.518492],[2.107890,4.691257,4.832722,-7.394019,6.094326,3.040621],[-3.108857,-5.349414,-5.071544,7.761533,-0.207427,9.866306],[6.870800,5.332522,-3.613227,-2.992112,-9.680554,-3.885601],[-7.895820,-5.535867,-7.469182,-6.347810,7.923745,2.851108],[-9.110850,-0.479907,7.708273,4.132582,-9.609835,-7.094141],[-3.967635,-3.641753,-6.127673,-1.058742,-5.636654,-5.575263],[6.307019,6.046873,9.520788,-0.444958,9.636265,-5.127297],[-8.907004,2.477750,8.792368,0.211435,-3.009858,-1.758714],[-4.333989,-6.566316,0.323227,-5.509468,6.738003,8.133108],[-8.766077,-6.029982,-0.121080,-4.196891,7.882864,6.073100],[1.931629,-4.708153,2.208011,-8.496053,8.726170,-2.010618],[7.878562,3.790709,-5.906478,5.961665,-7.119319,4.847744],[9.376299,0.169132,0.628946,8.715675,4.686660,2.875852],[-3.508905,3.375060,-1.583419,-1.680695,-8.374802,-8.563186],[1.926994,7.484068,4.322231,-9.016664,-6.652717,0.157615],[0.599006,-2.871301,-8.866618,6.168016,0.495152,5.466916],[-4.272185,0.564208,8.615320,8.665773,5.024009,8.583041],[7.610485,6.408859,4.348533,-2.985423,7.436753,-4.987813],[-6.638837,-7.458182,-0.159876,1.939300,-3.934168,5.972835],[-1.160633,-4.232677,4.592416,-3.915485,8.000052,-3.786404],[0.138909,2.917988,9.071171,-8.488470,7.483760,1.102109],[-4.879022,-2.785317,3.824604,5.148320,9.424766,4.258303],[6.736012,6.316779,-7.412688,4.921474,-0.551728,-5.049500],[-9.225971,7.153447,-5.624775,5.476181,3.902483,3.582566],[4.453890,-2.659303,-3.968910,2.285886,-1.864049,-9.821875],[-8.505639,-6.849092,4.535414,-0.008175,2.784056,3.876286],[-1.053155,8.875155,2.221199,-9.301748,2.773742,1.869834],[4.553324,3.054686,0.563113,-6.434368,6.328797,1.760859],[6.792025,0.668779,4.152664,-1.233017,5.874321,-4.276253],[-8.871457,-3.421281,5.307413,1.208917,-7.565284,-5.676683],[9.490104,-7.543337,6.199981,9.179851,3.091903,-9.231880],[0.326083,9.134389,-9.004323,8.913152,-9.737376,-7.517806],[0.708310,-2.773462,-4.640264,-0.521237,9.394349,-2.413765],[-9.827878,-2.147752,-5.343579,-6.561079,9.777559,2.236430],[8.395727,2.525009,-3.385333,-2.185073,4.593032,4.283546],[6.503616,6.260470,-3.803359,-5.946810,2.641625,3.590939],[1.152610,-1.546439,1.101739,-7.266348,-1.968697,-9.057061],[9.573322,3.543076,-5.112330,-0.066170,-1.379641,-8.530921],[7.160619,9.892791,1.655042,2.199462,-5.845350,-2.192680],[8.568748,6.998036,-6.471701,-0.606160,-6.297081,-3.470216],[-4.801917,-7.605414,3.147224,-6.724658,0.480955,1.624283],[-3.033297,7.875131,-2.387022,-9.884923,-2.247440,-9.186482],[8.627943,-9.085499,-2.918075,-0.930889,1.902180,1.845021],[-5.095208,-7.393650,0.361577,-3.539724,-7.278457,-8.115739],[8.180603,-4.280496,-0.613327,-9.989710,3.701841,7.230292],[-3.910115,-8.283384,3.432088,-3.893608,5.799840,4.287596],[-0.766524,-0.269189,-5.724414,-3.630782,9.580610,9.443659],[4.249511,-5.081117,4.942794,-3.141270,4.820727,9.388142],[-7.433177,-1.276688,-7.888057,-0.382613,-5.987416,9.138792],[2.449745,-3.661749,-2.390682,0.954528,-6.250590,-2.796069],[1.452240,0.482886,-8.341691,1.914650,-6.049590,-5.995551],[-7.064618,0.676652,-3.537810,8.096518,-4.583790,-0.307545],[1.044473,-7.875774,6.956257,0.470192,8.397063,-4.161865],[-1.916878,-4.271220,2.069946,6.118506,2.312555,-2.898942],[-3.114353,-1.467101,-0.739568,8.936987,-0.273874,0.803877],[0.912174,-1.536690,7.655934,-6.379109,2.996932,-5.399906]], dtype = "float64")#candidate|6158|(64, 6)|const|float64
bop_6159 = relay.minimum(uop_6152.astype('uint32'), relay.reshape(const_6158.astype('uint32'), relay.shape_of(uop_6152))) # shape=(64, 6)
bop_6162 = relay.minimum(uop_6154.astype('uint32'), relay.reshape(const_6158.astype('uint32'), relay.shape_of(uop_6154))) # shape=(64, 6)
output = relay.Tuple([bop_6159,])
output2 = relay.Tuple([bop_6162,])
func_6164 = relay.Function([], output)
mod['func_6164'] = func_6164
mod = relay.transform.InferType()(mod)
mutated_mod['func_6164'] = func_6164
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6164_call = mutated_mod.get_global_var('func_6164')
call_6165 = func_6164_call()
output = call_6165
func_6166 = relay.Function([], output)
mutated_mod['func_6166'] = func_6166
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5724_call = mod.get_global_var('func_5724')
func_5726_call = mutated_mod.get_global_var('func_5726')
call_6175 = relay.TupleGetItem(func_5724_call(), 0)
call_6176 = relay.TupleGetItem(func_5726_call(), 0)
output = call_6175
output2 = call_6176
func_6208 = relay.Function([], output)
mod['func_6208'] = func_6208
mod = relay.transform.InferType()(mod)
output = func_6208()
func_6209 = relay.Function([], output)
mutated_mod['func_6209'] = func_6209
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6208_call = mod.get_global_var('func_6208')
func_6209_call = mutated_mod.get_global_var('func_6209')
call_6212 = func_6208_call()
call_6213 = func_6208_call()
func_5767_call = mod.get_global_var('func_5767')
func_5768_call = mutated_mod.get_global_var('func_5768')
call_6221 = relay.TupleGetItem(func_5767_call(), 1)
call_6222 = relay.TupleGetItem(func_5768_call(), 1)
uop_6223 = relay.log2(call_6212.astype('float32')) # shape=(4, 11, 7)
uop_6225 = relay.log2(call_6213.astype('float32')) # shape=(4, 11, 7)
func_1547_call = mod.get_global_var('func_1547')
func_1548_call = mutated_mod.get_global_var('func_1548')
call_6235 = relay.TupleGetItem(func_1547_call(), 0)
call_6236 = relay.TupleGetItem(func_1548_call(), 0)
output = relay.Tuple([call_6221,uop_6223,call_6235,])
output2 = relay.Tuple([call_6222,uop_6225,call_6236,])
func_6240 = relay.Function([], output)
mod['func_6240'] = func_6240
mod = relay.transform.InferType()(mod)
mutated_mod['func_6240'] = func_6240
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6240_call = mutated_mod.get_global_var('func_6240')
call_6241 = func_6240_call()
output = call_6241
func_6242 = relay.Function([], output)
mutated_mod['func_6242'] = func_6242
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6285 = relay.var("var_6285", dtype = "float32", shape = (9, 8, 7))#candidate|6285|(9, 8, 7)|var|float32
var_6286 = relay.var("var_6286", dtype = "float32", shape = (9, 8, 7))#candidate|6286|(9, 8, 7)|var|float32
bop_6287 = relay.floor_divide(var_6285.astype('float32'), relay.reshape(var_6286.astype('float32'), relay.shape_of(var_6285))) # shape=(9, 8, 7)
output = relay.Tuple([bop_6287,])
output2 = relay.Tuple([bop_6287,])
func_6291 = relay.Function([var_6285,var_6286,], output)
mod['func_6291'] = func_6291
mod = relay.transform.InferType()(mod)
mutated_mod['func_6291'] = func_6291
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6291_call = mutated_mod.get_global_var('func_6291')
var_6293 = relay.var("var_6293", dtype = "float32", shape = (9, 8, 7))#candidate|6293|(9, 8, 7)|var|float32
var_6294 = relay.var("var_6294", dtype = "float32", shape = (9, 8, 7))#candidate|6294|(9, 8, 7)|var|float32
call_6292 = func_6291_call(var_6293,var_6294,)
output = call_6292
func_6295 = relay.Function([var_6293,var_6294,], output)
mutated_mod['func_6295'] = func_6295
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6299 = relay.var("var_6299", dtype = "float32", shape = (1, 3, 1))#candidate|6299|(1, 3, 1)|var|float32
uop_6300 = relay.rsqrt(var_6299.astype('float32')) # shape=(1, 3, 1)
func_959_call = mod.get_global_var('func_959')
func_963_call = mutated_mod.get_global_var('func_963')
var_6314 = relay.var("var_6314", dtype = "bool", shape = (32, 8))#candidate|6314|(32, 8)|var|bool
var_6315 = relay.var("var_6315", dtype = "float64", shape = (121,))#candidate|6315|(121,)|var|float64
call_6313 = relay.TupleGetItem(func_959_call(relay.reshape(var_6314.astype('bool'), [64, 4]), relay.reshape(var_6315.astype('float64'), [121,]), ), 3)
call_6316 = relay.TupleGetItem(func_963_call(relay.reshape(var_6314.astype('bool'), [64, 4]), relay.reshape(var_6315.astype('float64'), [121,]), ), 3)
output = relay.Tuple([uop_6300,call_6313,var_6314,var_6315,])
output2 = relay.Tuple([uop_6300,call_6316,var_6314,var_6315,])
func_6320 = relay.Function([var_6299,var_6314,var_6315,], output)
mod['func_6320'] = func_6320
mod = relay.transform.InferType()(mod)
mutated_mod['func_6320'] = func_6320
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6320_call = mutated_mod.get_global_var('func_6320')
var_6322 = relay.var("var_6322", dtype = "float32", shape = (1, 3, 1))#candidate|6322|(1, 3, 1)|var|float32
var_6323 = relay.var("var_6323", dtype = "bool", shape = (32, 8))#candidate|6323|(32, 8)|var|bool
var_6324 = relay.var("var_6324", dtype = "float64", shape = (121,))#candidate|6324|(121,)|var|float64
call_6321 = func_6320_call(var_6322,var_6323,var_6324,)
output = call_6321
func_6325 = relay.Function([var_6322,var_6323,var_6324,], output)
mutated_mod['func_6325'] = func_6325
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5281_call = mod.get_global_var('func_5281')
func_5283_call = mutated_mod.get_global_var('func_5283')
call_6359 = relay.TupleGetItem(func_5281_call(), 0)
call_6360 = relay.TupleGetItem(func_5283_call(), 0)
func_1260_call = mod.get_global_var('func_1260')
func_1261_call = mutated_mod.get_global_var('func_1261')
call_6368 = relay.TupleGetItem(func_1260_call(), 0)
call_6369 = relay.TupleGetItem(func_1261_call(), 0)
output = relay.Tuple([call_6359,call_6368,])
output2 = relay.Tuple([call_6360,call_6369,])
func_6370 = relay.Function([], output)
mod['func_6370'] = func_6370
mod = relay.transform.InferType()(mod)
output = func_6370()
func_6371 = relay.Function([], output)
mutated_mod['func_6371'] = func_6371
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4159_call = mod.get_global_var('func_4159')
func_4160_call = mutated_mod.get_global_var('func_4160')
call_6375 = relay.TupleGetItem(func_4159_call(), 0)
call_6376 = relay.TupleGetItem(func_4160_call(), 0)
const_6380 = relay.const([[-6.795404,4.492039,-5.470570,8.904028,3.663504,1.447581,6.774689,-4.581057],[5.379352,0.230382,7.313392,5.696638,-2.293847,7.295351,7.988145,7.964235],[-6.532008,9.001073,-1.817169,-2.413165,8.310306,9.998577,-4.200416,-8.137627],[5.453708,-0.478440,7.406652,2.096623,-1.338987,8.834739,7.534848,3.848055],[-1.145317,5.845741,5.393157,-9.715047,3.738656,-1.199179,7.010017,9.851133],[-5.651214,7.072535,4.251442,9.888420,8.155348,-7.486928,-1.633344,4.569878],[-7.451495,8.938403,-1.594869,2.092982,7.359380,5.410696,-2.876301,-8.977861],[-1.872678,5.649486,-2.626839,4.388285,0.940426,4.830720,-0.221651,-6.280877],[3.313101,-4.068836,7.358243,4.365027,9.381652,6.813746,3.835053,-0.842467],[-6.524833,-2.870414,0.784008,-3.627258,3.621378,-1.521129,-8.431523,-8.883752],[-1.648788,3.826668,-1.624300,8.565915,7.362599,-9.379818,-4.716637,-4.231816],[-3.333391,2.283928,9.112241,-6.419421,3.469204,-8.114111,-6.742327,1.155836],[9.046338,-2.672809,0.480369,-5.809381,3.204364,-9.900387,3.160835,-1.277416],[8.779002,2.662461,9.822493,9.881494,-6.974093,0.119126,-9.014926,-8.751149],[8.611865,-7.957803,-6.649791,-6.948644,2.058643,1.672987,8.901522,-1.341601],[9.000012,6.281088,4.944895,-8.347396,-0.713600,-3.244310,-6.761784,3.334040],[-7.583681,9.683631,-1.943611,-4.118604,-3.730087,-9.587749,4.960990,-0.800686],[7.312309,6.305897,-9.118374,-5.461301,8.677464,0.861555,5.346461,-7.829871],[-7.034996,-6.975045,8.411832,-3.207715,-6.702079,3.349349,2.272032,5.398314],[-4.125056,-5.860348,-7.081739,2.052925,4.109713,7.080181,1.870870,-0.884992],[5.309977,-6.833482,5.172438,-8.325168,-6.313409,9.455266,3.551911,-5.815546],[-7.074112,-0.241133,4.549351,-8.366693,6.672777,-3.499129,4.836187,-1.418787],[7.413576,8.357301,-6.241162,0.319987,-4.040287,-4.206935,1.194594,2.050252],[8.261844,-9.125247,4.937111,-9.232218,-0.781220,-1.437119,4.371243,9.463441],[5.405385,-3.397944,-3.994768,-9.977708,-8.198157,5.468938,9.595303,6.011066],[-2.303255,-3.276196,3.642170,-1.819511,1.105120,7.988129,-0.949799,3.358804],[-7.682695,1.488229,3.261665,3.692362,-2.746630,7.069026,1.564489,7.461422],[-4.285458,1.785053,-5.145271,-6.678707,-7.865774,-3.613261,-0.326679,5.266708],[0.617720,2.925048,-5.135407,6.633579,4.508515,8.941807,4.945723,7.280996],[-9.577833,4.216223,-3.008143,-2.259384,-9.110656,2.263662,-7.865430,8.823069],[2.603601,1.977880,0.980494,2.037852,2.876054,1.237920,8.897941,6.005527],[6.969876,-6.801350,-9.298058,6.798302,1.667687,7.820121,1.126325,-1.171638],[1.340357,-9.139304,-7.891842,-9.149316,-8.358218,-8.610974,-0.308212,3.865275],[8.085701,1.383280,-8.542082,-1.842347,-7.451414,-5.045033,-2.674847,-7.329028],[-8.909167,-5.305116,-2.189457,-4.707774,-4.367246,-6.675558,-9.826002,-3.358872],[1.626531,4.269347,-0.643142,-9.217479,4.887696,-3.258148,4.138881,-5.470890],[-3.185391,-3.473867,5.504069,1.876532,5.236396,-3.024251,-4.746911,6.437070],[-8.088053,2.867298,-4.524804,4.804932,-6.647448,7.311170,2.654779,3.713868],[-0.331725,-0.471946,7.339676,1.016306,-0.982113,-6.558063,4.971405,-0.970110],[6.291969,-0.818565,4.498664,5.884042,-6.890717,9.001076,-1.905170,7.261681],[-2.757306,-8.051182,1.648602,6.067513,6.468996,-2.438145,7.818132,1.225381],[2.722393,6.428568,4.859466,-7.796147,3.421809,2.488984,9.552059,3.828957],[0.183692,2.820265,5.218052,-3.251821,-1.942262,0.718057,5.631114,-1.152213],[7.697628,-6.382747,5.987711,-0.680592,-1.450153,-1.730044,-4.133985,-2.120037],[-3.945049,-3.461823,-9.628180,-5.126732,-2.709574,-3.303308,-3.521118,-5.626519],[-2.627396,1.585237,4.936352,1.290732,9.667987,0.046807,1.253038,6.238256],[4.449559,7.755634,-3.296846,0.049929,-7.158536,6.983001,-7.774746,-3.165981],[-3.062033,-1.122535,5.772461,2.351805,-5.983560,-8.055372,-1.171192,0.578928],[1.999946,6.968640,-1.192683,-3.080399,2.144947,-8.068791,7.107000,-6.380426],[-9.559723,-2.111682,-7.386089,-7.301340,-7.698791,-2.547733,9.826133,1.601028],[3.417533,-4.356362,2.392898,-9.423455,-0.865477,-2.719727,2.506812,5.582949],[-6.436538,5.888993,-0.878038,4.782133,-8.470088,4.841504,7.869616,-8.561191],[-3.627973,-1.495730,-5.143441,-9.454689,1.306965,-9.844547,1.131886,-2.287325],[5.031344,7.025695,-4.744627,6.136372,-9.137854,-6.984165,2.010269,-2.744372],[5.738754,6.286083,6.804939,6.889385,-3.388551,8.618833,6.834909,3.910023],[2.519877,-9.278499,2.099255,-5.908622,8.316377,2.132993,-7.698460,-6.846436],[3.195079,8.261083,9.956309,1.246158,-5.089822,0.220481,8.782895,7.389490],[7.170020,-4.251947,1.349413,1.595237,9.728233,2.257522,-3.439147,0.409524],[3.884288,9.097545,6.038171,-9.546712,7.393626,-0.034894,2.754179,-2.919492],[9.787197,7.881425,3.520517,7.055899,-9.522236,-0.001293,-9.587668,-2.709893],[-0.390572,-9.708199,-1.878675,-6.593013,7.342769,-6.519222,-7.910980,5.489383],[7.639370,-8.916462,9.806951,5.039960,-5.962341,9.618581,-5.130162,-4.797269],[3.033047,-8.399331,4.597634,8.133411,6.143181,4.790660,-7.044843,-6.195945],[-4.165591,1.537527,-0.030065,1.130409,-1.921900,-0.385580,-2.320771,-2.074284]], dtype = "float64")#candidate|6380|(64, 8)|const|float64
bop_6381 = relay.subtract(call_6375.astype('uint16'), relay.reshape(const_6380.astype('uint16'), relay.shape_of(call_6375))) # shape=(64, 8)
bop_6384 = relay.subtract(call_6376.astype('uint16'), relay.reshape(const_6380.astype('uint16'), relay.shape_of(call_6376))) # shape=(64, 8)
output = bop_6381
output2 = bop_6384
func_6386 = relay.Function([], output)
mod['func_6386'] = func_6386
mod = relay.transform.InferType()(mod)
output = func_6386()
func_6387 = relay.Function([], output)
mutated_mod['func_6387'] = func_6387
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1547_call = mod.get_global_var('func_1547')
func_1548_call = mutated_mod.get_global_var('func_1548')
call_6388 = relay.TupleGetItem(func_1547_call(), 0)
call_6389 = relay.TupleGetItem(func_1548_call(), 0)
output = relay.Tuple([call_6388,])
output2 = relay.Tuple([call_6389,])
func_6400 = relay.Function([], output)
mod['func_6400'] = func_6400
mod = relay.transform.InferType()(mod)
output = func_6400()
func_6401 = relay.Function([], output)
mutated_mod['func_6401'] = func_6401
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2982_call = mod.get_global_var('func_2982')
func_2984_call = mutated_mod.get_global_var('func_2984')
call_6415 = relay.TupleGetItem(func_2982_call(), 0)
call_6416 = relay.TupleGetItem(func_2984_call(), 0)
var_6432 = relay.var("var_6432", dtype = "float64", shape = (64, 8))#candidate|6432|(64, 8)|var|float64
bop_6433 = relay.multiply(call_6415.astype('uint16'), relay.reshape(var_6432.astype('uint16'), relay.shape_of(call_6415))) # shape=(64, 8)
bop_6436 = relay.multiply(call_6416.astype('uint16'), relay.reshape(var_6432.astype('uint16'), relay.shape_of(call_6416))) # shape=(64, 8)
bop_6437 = relay.power(bop_6433.astype('float32'), relay.reshape(var_6432.astype('float32'), relay.shape_of(bop_6433))) # shape=(64, 8)
bop_6440 = relay.power(bop_6436.astype('float32'), relay.reshape(var_6432.astype('float32'), relay.shape_of(bop_6436))) # shape=(64, 8)
bop_6443 = relay.logical_xor(call_6415.astype('uint8'), relay.reshape(bop_6433.astype('uint8'), relay.shape_of(call_6415))) # shape=(64, 8)
bop_6446 = relay.logical_xor(call_6416.astype('uint8'), relay.reshape(bop_6436.astype('uint8'), relay.shape_of(call_6416))) # shape=(64, 8)
output = relay.Tuple([bop_6437,bop_6443,])
output2 = relay.Tuple([bop_6440,bop_6446,])
F = relay.Function([var_6432,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_6432,], output2)
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
