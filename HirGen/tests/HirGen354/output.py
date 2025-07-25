import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
const_22 = relay.const([[[-2.520230,9.386211,-7.051316,6.032635,1.556128,-6.614641,-7.745796,-7.864395],[-7.709051,1.542532,3.508102,7.316768,-1.921133,3.857318,5.053182,-2.591657],[-2.837633,5.239308,-5.894247,4.698003,-1.583820,-5.653088,9.629354,6.831168],[0.150473,2.339302,-6.364592,6.809188,-2.707187,-3.574263,2.772395,-2.722482]],[[-8.752419,-9.824777,-7.679892,7.035642,9.649043,4.324622,-6.180990,7.413398],[2.258839,6.057970,8.568463,-9.879832,1.518628,-3.322216,7.637715,-5.682549],[-0.064848,-7.708718,-6.702953,6.406616,-5.894438,-1.108728,-8.833824,-8.533567],[9.899446,4.199834,-7.701595,-0.059711,-5.540733,2.362360,8.735439,-6.197045]],[[-6.565248,-8.712055,-4.772181,8.155247,-1.891646,3.085855,9.287430,-1.201292],[6.463511,1.898265,7.210535,6.223823,-9.157929,6.739320,0.248556,-2.085006],[9.573804,-5.319960,-5.379564,-8.835515,-6.030604,5.074382,8.018751,-6.463267],[-2.112988,-7.941227,0.966484,4.471025,-9.380584,-2.365125,-4.542551,-6.544350]]], dtype = "float64")#candidate|22|(3, 4, 8)|const|float64
uop_23 = relay.sin(const_22.astype('float64')) # shape=(3, 4, 8)
uop_30 = relay.tan(uop_23.astype('float64')) # shape=(3, 4, 8)
output = uop_30
output2 = uop_30
func_40 = relay.Function([], output)
mod['func_40'] = func_40
mod = relay.transform.InferType()(mod)
output = func_40()
func_41 = relay.Function([], output)
mutated_mod['func_41'] = func_41
mutated_mod = relay.transform.InferType()(mutated_mod)
func_40_call = mod.get_global_var('func_40')
func_41_call = mutated_mod.get_global_var('func_41')
call_47 = func_40_call()
call_48 = func_40_call()
uop_81 = relay.acosh(call_47.astype('float32')) # shape=(3, 4, 8)
uop_83 = relay.acosh(call_48.astype('float32')) # shape=(3, 4, 8)
const_84 = relay.const([[[0.675191,-7.852862,-5.389768,4.304139,-4.454549,6.932120,9.156280,9.956578],[-8.633573,-6.176160,-5.877958,-9.439850,5.354194,-3.487894,-3.144465,0.160007],[-0.468264,-8.601686,-2.015063,-2.300276,-7.482450,2.088061,-0.624440,-8.777766],[3.129223,-4.129447,8.047111,1.981202,-2.650416,6.359805,5.836364,8.375090]],[[-3.044364,2.633556,5.346181,2.462723,6.377506,8.521753,5.635981,6.353523],[-8.280949,-6.741665,-3.349773,-2.891815,8.244028,8.434383,3.281749,-8.023352],[-9.134509,-1.607393,1.469309,0.159514,9.086169,5.760882,-7.277272,4.704926],[-6.531697,0.513057,-7.410980,2.325950,3.385997,-5.153558,6.606071,-5.302348]],[[-2.088201,1.201468,-1.317814,2.013287,-3.501695,-2.002556,5.628114,1.808482],[7.024647,-5.970812,8.457779,4.152264,-3.401454,6.653018,4.463262,-6.760176],[-0.749224,0.036943,-5.781725,-3.987934,6.071062,-0.098994,8.865738,-3.276219],[-1.401472,-7.797789,9.170031,-1.664955,2.604183,6.377738,8.863657,4.649813]]], dtype = "float32")#candidate|84|(3, 4, 8)|const|float32
bop_85 = relay.floor_mod(uop_81.astype('float32'), relay.reshape(const_84.astype('float32'), relay.shape_of(uop_81))) # shape=(3, 4, 8)
bop_88 = relay.floor_mod(uop_83.astype('float32'), relay.reshape(const_84.astype('float32'), relay.shape_of(uop_83))) # shape=(3, 4, 8)
func_40_call = mod.get_global_var('func_40')
func_41_call = mutated_mod.get_global_var('func_41')
call_105 = func_40_call()
call_106 = func_40_call()
uop_110 = relay.log(bop_85.astype('float32')) # shape=(3, 4, 8)
uop_112 = relay.log(bop_88.astype('float32')) # shape=(3, 4, 8)
bop_117 = relay.floor_divide(call_47.astype('float32'), relay.reshape(call_105.astype('float32'), relay.shape_of(call_47))) # shape=(3, 4, 8)
bop_120 = relay.floor_divide(call_48.astype('float32'), relay.reshape(call_106.astype('float32'), relay.shape_of(call_48))) # shape=(3, 4, 8)
func_40_call = mod.get_global_var('func_40')
func_41_call = mutated_mod.get_global_var('func_41')
call_126 = func_40_call()
call_127 = func_40_call()
bop_128 = relay.equal(uop_110.astype('bool'), relay.reshape(call_126.astype('bool'), relay.shape_of(uop_110))) # shape=(3, 4, 8)
bop_131 = relay.equal(uop_112.astype('bool'), relay.reshape(call_127.astype('bool'), relay.shape_of(uop_112))) # shape=(3, 4, 8)
uop_138 = relay.sigmoid(bop_117.astype('float64')) # shape=(3, 4, 8)
uop_140 = relay.sigmoid(bop_120.astype('float64')) # shape=(3, 4, 8)
func_40_call = mod.get_global_var('func_40')
func_41_call = mutated_mod.get_global_var('func_41')
call_144 = func_40_call()
call_145 = func_40_call()
output = relay.Tuple([bop_128,uop_138,call_144,])
output2 = relay.Tuple([bop_131,uop_140,call_145,])
func_148 = relay.Function([], output)
mod['func_148'] = func_148
mod = relay.transform.InferType()(mod)
mutated_mod['func_148'] = func_148
mutated_mod = relay.transform.InferType()(mutated_mod)
func_148_call = mutated_mod.get_global_var('func_148')
call_149 = func_148_call()
output = call_149
func_150 = relay.Function([], output)
mutated_mod['func_150'] = func_150
mutated_mod = relay.transform.InferType()(mutated_mod)
func_148_call = mod.get_global_var('func_148')
func_150_call = mutated_mod.get_global_var('func_150')
call_246 = relay.TupleGetItem(func_148_call(), 2)
call_247 = relay.TupleGetItem(func_150_call(), 2)
func_148_call = mod.get_global_var('func_148')
func_150_call = mutated_mod.get_global_var('func_150')
call_251 = relay.TupleGetItem(func_148_call(), 1)
call_252 = relay.TupleGetItem(func_150_call(), 1)
output = relay.Tuple([call_246,call_251,])
output2 = relay.Tuple([call_247,call_252,])
func_257 = relay.Function([], output)
mod['func_257'] = func_257
mod = relay.transform.InferType()(mod)
mutated_mod['func_257'] = func_257
mutated_mod = relay.transform.InferType()(mutated_mod)
func_257_call = mutated_mod.get_global_var('func_257')
call_258 = func_257_call()
output = call_258
func_259 = relay.Function([], output)
mutated_mod['func_259'] = func_259
mutated_mod = relay.transform.InferType()(mutated_mod)
func_40_call = mod.get_global_var('func_40')
func_41_call = mutated_mod.get_global_var('func_41')
call_283 = func_40_call()
call_284 = func_40_call()
uop_287 = relay.atanh(call_283.astype('float64')) # shape=(3, 4, 8)
uop_289 = relay.atanh(call_284.astype('float64')) # shape=(3, 4, 8)
uop_304 = relay.log10(uop_287.astype('float64')) # shape=(3, 4, 8)
uop_306 = relay.log10(uop_289.astype('float64')) # shape=(3, 4, 8)
output = uop_304
output2 = uop_306
func_307 = relay.Function([], output)
mod['func_307'] = func_307
mod = relay.transform.InferType()(mod)
mutated_mod['func_307'] = func_307
mutated_mod = relay.transform.InferType()(mutated_mod)
func_307_call = mutated_mod.get_global_var('func_307')
call_308 = func_307_call()
output = call_308
func_309 = relay.Function([], output)
mutated_mod['func_309'] = func_309
mutated_mod = relay.transform.InferType()(mutated_mod)
func_307_call = mod.get_global_var('func_307')
func_309_call = mutated_mod.get_global_var('func_309')
call_320 = func_307_call()
call_321 = func_307_call()
output = relay.Tuple([call_320,])
output2 = relay.Tuple([call_321,])
func_322 = relay.Function([], output)
mod['func_322'] = func_322
mod = relay.transform.InferType()(mod)
output = func_322()
func_323 = relay.Function([], output)
mutated_mod['func_323'] = func_323
mutated_mod = relay.transform.InferType()(mutated_mod)
var_368 = relay.var("var_368", dtype = "float32", shape = (12, 8, 2))#candidate|368|(12, 8, 2)|var|float32
uop_369 = relay.rsqrt(var_368.astype('float32')) # shape=(12, 8, 2)
output = uop_369
output2 = uop_369
func_375 = relay.Function([var_368,], output)
mod['func_375'] = func_375
mod = relay.transform.InferType()(mod)
mutated_mod['func_375'] = func_375
mutated_mod = relay.transform.InferType()(mutated_mod)
var_376 = relay.var("var_376", dtype = "float32", shape = (12, 8, 2))#candidate|376|(12, 8, 2)|var|float32
func_375_call = mutated_mod.get_global_var('func_375')
call_377 = func_375_call(var_376)
output = call_377
func_378 = relay.Function([var_376], output)
mutated_mod['func_378'] = func_378
mutated_mod = relay.transform.InferType()(mutated_mod)
var_397 = relay.var("var_397", dtype = "bool", shape = ())#candidate|397|()|var|bool
var_398 = relay.var("var_398", dtype = "bool", shape = (6, 6, 13))#candidate|398|(6, 6, 13)|var|bool
bop_399 = relay.logical_or(var_397.astype('bool'), var_398.astype('bool')) # shape=(6, 6, 13)
var_408 = relay.var("var_408", dtype = "bool", shape = (6, 6, 13))#candidate|408|(6, 6, 13)|var|bool
bop_409 = relay.mod(var_398.astype('float64'), relay.reshape(var_408.astype('float64'), relay.shape_of(var_398))) # shape=(6, 6, 13)
const_414 = relay.const([[[False,False,True,False,True,True,False,True,False,True,False,False,True],[True,True,True,True,True,False,True,False,False,False,False,True,False],[True,False,False,True,False,False,True,True,False,True,True,True,False],[True,False,False,True,True,True,False,False,False,False,False,False,False],[False,False,False,True,False,False,True,False,True,False,False,True,True],[True,False,False,False,False,True,False,False,True,True,False,True,True]],[[False,True,True,False,True,False,False,False,True,True,False,True,True],[True,True,False,False,False,True,False,True,True,False,False,True,True],[True,False,True,True,True,True,False,False,False,False,False,False,False],[False,True,False,True,True,True,False,True,False,False,False,False,True],[True,True,False,False,False,True,False,True,False,True,False,True,True],[False,True,False,True,True,False,False,True,True,True,False,True,False]],[[False,True,False,True,True,True,False,True,True,False,False,True,True],[True,False,True,False,False,False,True,False,True,False,False,True,True],[True,True,True,False,True,False,True,False,True,False,True,True,True],[True,True,False,False,False,True,True,True,True,True,True,False,True],[False,False,True,False,True,False,True,False,False,False,False,True,False],[True,False,False,False,True,True,True,True,True,True,False,False,True]],[[True,True,False,True,False,True,True,True,True,False,True,False,True],[True,False,True,True,True,True,True,True,True,False,False,True,False],[True,False,False,False,True,False,True,False,True,False,True,True,True],[False,True,True,False,False,False,False,False,True,True,True,False,False],[False,True,False,True,True,False,False,True,False,True,True,True,True],[True,True,False,False,True,False,True,False,False,False,False,True,False]],[[False,False,True,False,True,True,True,True,True,False,True,True,False],[True,False,True,True,False,False,False,False,False,True,True,False,True],[True,False,False,False,False,False,True,True,False,False,False,False,True],[True,False,True,False,False,False,True,False,True,True,False,False,True],[True,True,False,True,True,False,True,True,False,True,True,True,False],[True,True,False,True,True,False,False,False,False,False,False,True,False]],[[False,False,True,False,False,False,True,False,True,False,False,False,True],[True,True,False,False,True,False,False,True,True,True,True,True,True],[False,False,True,True,False,True,False,True,True,False,True,True,False],[False,True,True,False,True,False,True,True,False,False,True,False,False],[True,True,True,False,False,True,False,False,True,True,True,True,False],[True,True,False,False,True,False,True,False,True,False,False,False,False]]], dtype = "bool")#candidate|414|(6, 6, 13)|const|bool
bop_415 = relay.divide(var_408.astype('float32'), relay.reshape(const_414.astype('float32'), relay.shape_of(var_408))) # shape=(6, 6, 13)
uop_438 = relay.asin(const_414.astype('float64')) # shape=(6, 6, 13)
var_468 = relay.var("var_468", dtype = "bool", shape = (6, 6, 13))#candidate|468|(6, 6, 13)|var|bool
bop_469 = relay.bitwise_or(const_414.astype('int16'), relay.reshape(var_468.astype('int16'), relay.shape_of(const_414))) # shape=(6, 6, 13)
func_257_call = mod.get_global_var('func_257')
func_259_call = mutated_mod.get_global_var('func_259')
call_491 = relay.TupleGetItem(func_257_call(), 1)
call_492 = relay.TupleGetItem(func_259_call(), 1)
func_307_call = mod.get_global_var('func_307')
func_309_call = mutated_mod.get_global_var('func_309')
call_504 = func_307_call()
call_505 = func_307_call()
bop_510 = relay.add(uop_438.astype('float64'), relay.reshape(const_414.astype('float64'), relay.shape_of(uop_438))) # shape=(6, 6, 13)
output = relay.Tuple([bop_399,bop_409,bop_415,bop_469,call_491,call_504,bop_510,])
output2 = relay.Tuple([bop_399,bop_409,bop_415,bop_469,call_492,call_505,bop_510,])
func_514 = relay.Function([var_397,var_398,var_408,var_468,], output)
mod['func_514'] = func_514
mod = relay.transform.InferType()(mod)
mutated_mod['func_514'] = func_514
mutated_mod = relay.transform.InferType()(mutated_mod)
func_514_call = mutated_mod.get_global_var('func_514')
var_516 = relay.var("var_516", dtype = "bool", shape = ())#candidate|516|()|var|bool
var_517 = relay.var("var_517", dtype = "bool", shape = (6, 6, 13))#candidate|517|(6, 6, 13)|var|bool
var_518 = relay.var("var_518", dtype = "bool", shape = (6, 6, 13))#candidate|518|(6, 6, 13)|var|bool
var_519 = relay.var("var_519", dtype = "bool", shape = (6, 6, 13))#candidate|519|(6, 6, 13)|var|bool
call_515 = func_514_call(var_516,var_517,var_518,var_519,)
output = call_515
func_520 = relay.Function([var_516,var_517,var_518,var_519,], output)
mutated_mod['func_520'] = func_520
mutated_mod = relay.transform.InferType()(mutated_mod)
func_40_call = mod.get_global_var('func_40')
func_41_call = mutated_mod.get_global_var('func_41')
call_541 = func_40_call()
call_542 = func_40_call()
func_40_call = mod.get_global_var('func_40')
func_41_call = mutated_mod.get_global_var('func_41')
call_543 = func_40_call()
call_544 = func_40_call()
output = relay.Tuple([call_541,call_543,])
output2 = relay.Tuple([call_542,call_544,])
func_557 = relay.Function([], output)
mod['func_557'] = func_557
mod = relay.transform.InferType()(mod)
output = func_557()
func_558 = relay.Function([], output)
mutated_mod['func_558'] = func_558
mutated_mod = relay.transform.InferType()(mutated_mod)
func_40_call = mod.get_global_var('func_40')
func_41_call = mutated_mod.get_global_var('func_41')
call_586 = func_40_call()
call_587 = func_40_call()
func_257_call = mod.get_global_var('func_257')
func_259_call = mutated_mod.get_global_var('func_259')
call_594 = relay.TupleGetItem(func_257_call(), 0)
call_595 = relay.TupleGetItem(func_259_call(), 0)
func_257_call = mod.get_global_var('func_257')
func_259_call = mutated_mod.get_global_var('func_259')
call_596 = relay.TupleGetItem(func_257_call(), 0)
call_597 = relay.TupleGetItem(func_259_call(), 0)
func_557_call = mod.get_global_var('func_557')
func_558_call = mutated_mod.get_global_var('func_558')
call_612 = relay.TupleGetItem(func_557_call(), 0)
call_613 = relay.TupleGetItem(func_558_call(), 0)
func_148_call = mod.get_global_var('func_148')
func_150_call = mutated_mod.get_global_var('func_150')
call_623 = relay.TupleGetItem(func_148_call(), 2)
call_624 = relay.TupleGetItem(func_150_call(), 2)
bop_626 = relay.left_shift(call_623.astype('uint64'), relay.reshape(call_612.astype('uint64'), relay.shape_of(call_623))) # shape=(3, 4, 8)
bop_629 = relay.left_shift(call_624.astype('uint64'), relay.reshape(call_613.astype('uint64'), relay.shape_of(call_624))) # shape=(3, 4, 8)
uop_639 = relay.asin(bop_626.astype('float32')) # shape=(3, 4, 8)
uop_641 = relay.asin(bop_629.astype('float32')) # shape=(3, 4, 8)
uop_642 = relay.sinh(uop_639.astype('float64')) # shape=(3, 4, 8)
uop_644 = relay.sinh(uop_641.astype('float64')) # shape=(3, 4, 8)
func_514_call = mod.get_global_var('func_514')
func_520_call = mutated_mod.get_global_var('func_520')
var_650 = relay.var("var_650", dtype = "bool", shape = ())#candidate|650|()|var|bool
const_651 = relay.const([True,True,True,True,True,False,True,True,False,False,True,True,True,False,False,False,True,True,True,True,True,True,False,False,True,True,False,True,True,False,True,False,True,False,True,False,True,True,False,True,True,True,False,False,True,True,True,False,False,False,True,False,False,True,False,True,True,True,True,False,True,False,False,True,False,True,True,True,False,True,False,False,False,True,False,True,False,True,False,False,False,True,False,False,True,True,True,False,False,False,False,True,False,False,False,True,True,False,False,False,True,True,False,False,False,False,True,False,False,True,False,False,True,True,False,False,False,True,False,False,False,False,True,False,False,False,True,True,False,False,True,True,True,True,True,True,False,True,True,False,False,True,False,True,False,False,True,False,True,True,False,True,True,False,False,True,False,True,True,False,True,False,True,False,False,True,True,False,False,False,False,False,False,False,False,False,False,True,True,True,True,True,True,False,True,True,False,True,False,True,True,False,True,True,False,True,False,False,True,False,False,True,False,False,True,False,True,True,False,False,True,True,True,False,True,True,True,True,False,True,False,False,True,False,True,False,True,True,False,True,True,False,False,True,True,False,False,False,True,False,False,False,True,True,False,False,False,True,False,True,True,False,True,False,False,False,False,False,True,False,True,False,True,True,True,False,True,True,False,True,True,False,True,False,True,False,True,False,True,True,True,False,True,False,True,False,False,True,False,True,False,True,True,True,False,False,True,False,False,True,True,True,True,False,False,False,False,True,False,False,False,True,False,True,True,True,True,True,True,True,False,True,False,True,False,True,False,True,True,False,False,False,True,True,False,True,True,True,False,False,True,False,True,True,False,True,True,True,False,False,True,True,True,True,False,True,False,False,False,True,False,False,True,False,True,False,True,False,True,False,False,False,False,False,True,False,True,False,False,True,False,True,False,True,False,True,False,True,True,False,False,False,False,False,False,True,False,True,False,True,True,False,True,False,False,False,False,True,True,False,True,True,True,True,True,False,False,True,True,False,False,True,False,False,True,False,False,True,True,False,False,True,False,True,True,True,False,True,False,True,False,True,False,True,True,True,True,True,True,False,True,True,False,True,True,True,True,True,True,True,True,True,False,False,True,True,True,True], dtype = "bool")#candidate|651|(468,)|const|bool
call_649 = relay.TupleGetItem(func_514_call(relay.reshape(var_650.astype('bool'), []), relay.reshape(const_651.astype('bool'), [6, 6, 13]), relay.reshape(const_651.astype('bool'), [6, 6, 13]), relay.reshape(const_651.astype('bool'), [6, 6, 13]), ), 6)
call_652 = relay.TupleGetItem(func_520_call(relay.reshape(var_650.astype('bool'), []), relay.reshape(const_651.astype('bool'), [6, 6, 13]), relay.reshape(const_651.astype('bool'), [6, 6, 13]), relay.reshape(const_651.astype('bool'), [6, 6, 13]), ), 6)
func_40_call = mod.get_global_var('func_40')
func_41_call = mutated_mod.get_global_var('func_41')
call_653 = func_40_call()
call_654 = func_40_call()
bop_659 = relay.less_equal(uop_639.astype('bool'), relay.reshape(call_653.astype('bool'), relay.shape_of(uop_639))) # shape=(3, 4, 8)
bop_662 = relay.less_equal(uop_641.astype('bool'), relay.reshape(call_654.astype('bool'), relay.shape_of(uop_641))) # shape=(3, 4, 8)
uop_677 = relay.sqrt(uop_642.astype('float32')) # shape=(3, 4, 8)
uop_679 = relay.sqrt(uop_644.astype('float32')) # shape=(3, 4, 8)
bop_685 = relay.bitwise_and(uop_677.astype('uint32'), relay.reshape(call_612.astype('uint32'), relay.shape_of(uop_677))) # shape=(3, 4, 8)
bop_688 = relay.bitwise_and(uop_679.astype('uint32'), relay.reshape(call_613.astype('uint32'), relay.shape_of(uop_679))) # shape=(3, 4, 8)
bop_689 = relay.subtract(uop_677.astype('float64'), relay.reshape(call_612.astype('float64'), relay.shape_of(uop_677))) # shape=(3, 4, 8)
bop_692 = relay.subtract(uop_679.astype('float64'), relay.reshape(call_613.astype('float64'), relay.shape_of(uop_679))) # shape=(3, 4, 8)
output = relay.Tuple([call_586,call_594,call_596,call_649,var_650,const_651,bop_659,bop_685,bop_689,])
output2 = relay.Tuple([call_587,call_595,call_597,call_652,var_650,const_651,bop_662,bop_688,bop_692,])
func_695 = relay.Function([var_650,], output)
mod['func_695'] = func_695
mod = relay.transform.InferType()(mod)
mutated_mod['func_695'] = func_695
mutated_mod = relay.transform.InferType()(mutated_mod)
var_696 = relay.var("var_696", dtype = "bool", shape = ())#candidate|696|()|var|bool
func_695_call = mutated_mod.get_global_var('func_695')
call_697 = func_695_call(var_696)
output = call_697
func_698 = relay.Function([var_696], output)
mutated_mod['func_698'] = func_698
mutated_mod = relay.transform.InferType()(mutated_mod)
var_756 = relay.var("var_756", dtype = "float64", shape = (3, 2))#candidate|756|(3, 2)|var|float64
uop_757 = relay.asinh(var_756.astype('float64')) # shape=(3, 2)
output = uop_757
output2 = uop_757
func_767 = relay.Function([var_756,], output)
mod['func_767'] = func_767
mod = relay.transform.InferType()(mod)
mutated_mod['func_767'] = func_767
mutated_mod = relay.transform.InferType()(mutated_mod)
var_768 = relay.var("var_768", dtype = "float64", shape = (3, 2))#candidate|768|(3, 2)|var|float64
func_767_call = mutated_mod.get_global_var('func_767')
call_769 = func_767_call(var_768)
output = call_769
func_770 = relay.Function([var_768], output)
mutated_mod['func_770'] = func_770
mutated_mod = relay.transform.InferType()(mutated_mod)
func_322_call = mod.get_global_var('func_322')
func_323_call = mutated_mod.get_global_var('func_323')
call_776 = relay.TupleGetItem(func_322_call(), 0)
call_777 = relay.TupleGetItem(func_323_call(), 0)
func_375_call = mod.get_global_var('func_375')
func_378_call = mutated_mod.get_global_var('func_378')
var_783 = relay.var("var_783", dtype = "float32", shape = (192,))#candidate|783|(192,)|var|float32
call_782 = func_375_call(relay.reshape(var_783.astype('float32'), [12, 8, 2]))
call_784 = func_375_call(relay.reshape(var_783.astype('float32'), [12, 8, 2]))
output = relay.Tuple([call_776,call_782,var_783,])
output2 = relay.Tuple([call_777,call_784,var_783,])
func_799 = relay.Function([var_783,], output)
mod['func_799'] = func_799
mod = relay.transform.InferType()(mod)
var_800 = relay.var("var_800", dtype = "float32", shape = (192,))#candidate|800|(192,)|var|float32
output = func_799(var_800)
func_801 = relay.Function([var_800], output)
mutated_mod['func_801'] = func_801
mutated_mod = relay.transform.InferType()(mutated_mod)
var_812 = relay.var("var_812", dtype = "int16", shape = (14, 6, 4))#candidate|812|(14, 6, 4)|var|int16
const_813 = relay.const([[[-10,-6,10,-6],[7,-1,10,-7],[-5,-9,-6,-10],[9,-3,-3,-4],[1,-8,4,-5],[1,-1,-6,-9]],[[-9,-3,9,3],[5,6,-8,-1],[-10,2,-4,-5],[5,-8,-4,1],[-3,-10,2,-2],[-1,5,9,-10]],[[6,5,3,4],[5,8,-9,5],[-7,-6,-10,4],[-9,3,-6,8],[-7,9,-2,7],[-5,9,7,-5]],[[8,-3,-2,-10],[-7,-8,7,2],[-1,-3,4,-4],[-6,2,-6,-8],[-8,5,-8,-10],[9,8,6,-10]],[[-1,-1,5,-5],[-8,-4,1,1],[3,-9,10,-5],[-7,-4,5,9],[-7,2,-6,2],[-3,10,-8,-3]],[[-8,3,-10,-8],[-3,10,-6,-3],[-1,-4,-3,5],[-3,-10,-8,4],[-5,-4,7,-4],[4,-8,4,3]],[[8,4,-6,-7],[-6,1,-10,-9],[-4,-10,7,-9],[7,-1,-9,-8],[-6,10,3,-10],[-4,10,6,9]],[[-4,-10,4,-2],[-7,3,1,-4],[-4,-8,2,4],[7,-2,-5,4],[1,-2,3,7],[9,5,1,-7]],[[-6,2,1,3],[-1,-4,5,8],[1,-2,-4,-2],[9,4,-1,-5],[-4,-4,-4,-6],[4,-3,-5,7]],[[-3,-10,-8,-1],[-4,-6,-6,9],[-9,-6,1,-8],[-1,4,-4,-3],[9,-5,6,3],[10,4,-2,5]],[[-7,6,4,-1],[-5,-2,3,5],[9,-9,5,-4],[3,1,2,-9],[-1,-4,-9,10],[9,2,-7,6]],[[-8,-10,6,7],[3,-7,8,-3],[10,-3,-2,4],[7,5,-4,10],[5,4,6,-3],[1,-4,-3,-7]],[[-4,-4,7,8],[-4,10,6,-10],[9,-4,-5,-4],[4,-5,-4,-4],[5,5,-3,-6],[7,-5,-3,4]],[[8,9,-3,-2],[-10,8,1,2],[-7,8,9,-9],[9,9,-10,5],[1,3,-8,4],[6,-4,1,5]]], dtype = "int16")#candidate|813|(14, 6, 4)|const|int16
bop_814 = relay.add(var_812.astype('int16'), relay.reshape(const_813.astype('int16'), relay.shape_of(var_812))) # shape=(14, 6, 4)
output = bop_814
output2 = bop_814
func_828 = relay.Function([var_812,], output)
mod['func_828'] = func_828
mod = relay.transform.InferType()(mod)
var_829 = relay.var("var_829", dtype = "int16", shape = (14, 6, 4))#candidate|829|(14, 6, 4)|var|int16
output = func_828(var_829)
func_830 = relay.Function([var_829], output)
mutated_mod['func_830'] = func_830
mutated_mod = relay.transform.InferType()(mutated_mod)
func_257_call = mod.get_global_var('func_257')
func_259_call = mutated_mod.get_global_var('func_259')
call_835 = relay.TupleGetItem(func_257_call(), 0)
call_836 = relay.TupleGetItem(func_259_call(), 0)
func_40_call = mod.get_global_var('func_40')
func_41_call = mutated_mod.get_global_var('func_41')
call_852 = func_40_call()
call_853 = func_40_call()
output = relay.Tuple([call_835,call_852,])
output2 = relay.Tuple([call_836,call_853,])
func_858 = relay.Function([], output)
mod['func_858'] = func_858
mod = relay.transform.InferType()(mod)
output = func_858()
func_859 = relay.Function([], output)
mutated_mod['func_859'] = func_859
mutated_mod = relay.transform.InferType()(mutated_mod)
func_858_call = mod.get_global_var('func_858')
func_859_call = mutated_mod.get_global_var('func_859')
call_886 = relay.TupleGetItem(func_858_call(), 1)
call_887 = relay.TupleGetItem(func_859_call(), 1)
func_514_call = mod.get_global_var('func_514')
func_520_call = mutated_mod.get_global_var('func_520')
var_899 = relay.var("var_899", dtype = "bool", shape = ())#candidate|899|()|var|bool
const_900 = relay.const([False,True,False,True,False,False,False,True,False,True,False,True,True,False,False,False,True,True,True,False,True,True,True,False,True,False,True,True,True,True,True,True,True,True,True,True,False,True,True,False,False,True,False,True,True,False,False,False,True,True,False,False,False,True,False,True,True,False,True,False,True,False,False,False,False,True,False,False,False,True,False,True,False,False,False,True,True,False,True,False,True,True,True,True,False,True,True,True,True,False,True,True,False,True,True,False,False,True,False,True,False,True,False,False,True,False,True,False,True,False,True,False,True,False,False,True,True,True,False,True,True,False,False,True,True,True,False,False,True,False,True,True,True,True,False,True,True,True,True,False,False,False,True,True,False,True,True,False,False,True,True,True,True,True,False,True,False,False,True,True,True,False,True,False,True,True,True,False,False,True,True,False,True,False,False,False,True,True,False,True,False,True,False,False,False,False,True,False,True,False,False,False,False,True,False,True,False,False,True,False,True,False,True,False,False,True,False,True,False,False,False,False,True,False,False,True,True,True,False,False,True,False,False,True,True,False,False,True,False,False,True,True,False,False,False,True,True,False,False,True,True,True,False,False,True,False,False,False,False,False,False,True,False,False,True,True,True,True,False,True,True,True,True,False,False,True,True,True,True,True,True,False,False,True,True,False,True,True,False,True,True,True,True,True,True,False,False,False,True,False,False,True,True,True,True,True,False,False,True,True,True,False,False,False,True,True,False,False,False,False,False,True,True,True,False,True,True,False,True,False,False,True,True,True,False,False,True,False,False,False,False,False,False,False,False,True,True,False,True,True,False,True,False,False,False,False,True,True,False,False,False,False,False,True,True,False,False,False,True,False,False,True,False,False,True,False,True,False,False,True,True,True,False,True,True,True,True,False,False,True,False,False,True,False,False,False,True,False,True,False,False,True,True,True,False,False,True,True,False,False,False,True,True,True,False,False,False,True,False,False,False,False,True,True,True,True,True,False,True,False,False,True,False,True,False,False,True,False,True,True,False,False,False,True,True,False,True,True,True,True,True,True,True,False,False,False,True,True,False,False,False,False,False,False,True,False,False,False,False,True,True,False,True,True,True,False,True,False], dtype = "bool")#candidate|900|(468,)|const|bool
call_898 = relay.TupleGetItem(func_514_call(relay.reshape(var_899.astype('bool'), []), relay.reshape(const_900.astype('bool'), [6, 6, 13]), relay.reshape(const_900.astype('bool'), [6, 6, 13]), relay.reshape(const_900.astype('bool'), [6, 6, 13]), ), 1)
call_901 = relay.TupleGetItem(func_520_call(relay.reshape(var_899.astype('bool'), []), relay.reshape(const_900.astype('bool'), [6, 6, 13]), relay.reshape(const_900.astype('bool'), [6, 6, 13]), relay.reshape(const_900.astype('bool'), [6, 6, 13]), ), 1)
bop_908 = relay.greater_equal(call_898.astype('bool'), var_899.astype('bool')) # shape=(6, 6, 13)
bop_911 = relay.greater_equal(call_901.astype('bool'), var_899.astype('bool')) # shape=(6, 6, 13)
output = relay.Tuple([call_886,const_900,bop_908,])
output2 = relay.Tuple([call_887,const_900,bop_911,])
func_916 = relay.Function([var_899,], output)
mod['func_916'] = func_916
mod = relay.transform.InferType()(mod)
var_917 = relay.var("var_917", dtype = "bool", shape = ())#candidate|917|()|var|bool
output = func_916(var_917)
func_918 = relay.Function([var_917], output)
mutated_mod['func_918'] = func_918
mutated_mod = relay.transform.InferType()(mutated_mod)
func_858_call = mod.get_global_var('func_858')
func_859_call = mutated_mod.get_global_var('func_859')
call_947 = relay.TupleGetItem(func_858_call(), 1)
call_948 = relay.TupleGetItem(func_859_call(), 1)
func_695_call = mod.get_global_var('func_695')
func_698_call = mutated_mod.get_global_var('func_698')
const_964 = relay.const(False, dtype = "bool")#candidate|964|()|const|bool
call_963 = relay.TupleGetItem(func_695_call(relay.reshape(const_964.astype('bool'), [])), 0)
call_965 = relay.TupleGetItem(func_698_call(relay.reshape(const_964.astype('bool'), [])), 0)
func_828_call = mod.get_global_var('func_828')
func_830_call = mutated_mod.get_global_var('func_830')
const_968 = relay.const([-2,10,-6,-1,4,7,-3,9,2,-10,-6,-6,-1,-10,-7,9,-6,3,5,-4,-4,-10,9,-2,7,-4,1,7,-7,9,4,5,-6,-9,2,1,8,2,1,8,8,-10,2,-10,-6,4,6,7,-10,4,4,8,7,9,8,5,-1,-6,4,-1,5,-10,7,-7,-8,8,6,-5,-10,10,-2,-3,-10,6,-4,-4,-4,-2,-4,7,9,3,3,-8,-2,10,-3,-7,-3,7,-1,8,5,-6,10,8,-9,5,-9,-7,-5,-7,2,-1,8,-2,-9,2,-10,-1,-2,-10,-2,-4,-1,-3,10,5,3,-6,-6,-8,7,-8,-8,9,-10,10,-5,-2,-9,-1,5,10,-3,-7,-5,3,4,-10,10,10,-8,1,-9,8,-8,-7,-8,-10,-3,10,-9,9,2,-6,9,-2,10,-10,6,7,8,8,-10,5,-5,-1,-7,8,2,-4,1,7,1,10,-5,5,8,-7,2,-4,-10,1,-5,-9,-4,7,-10,9,-2,-3,6,10,1,-4,1,10,-3,9,2,5,2,5,6,5,5,-3,-6,-6,-10,10,10,-7,2,1,5,-4,-7,10,3,1,5,-10,7,-8,8,-2,-1,-3,4,-1,-1,-7,3,4,-3,5,-9,1,-1,-4,-8,-9,-5,3,8,10,8,10,5,7,-8,-7,7,2,-6,7,5,4,10,-3,3,10,1,3,3,-3,2,8,6,7,8,-8,2,7,1,-2,3,8,-3,9,10,-9,-2,10,-6,-1,-3,-9,3,8,-6,-10,4,5,8,-3,8,1,-8,-9,7,1,1,6,-6,7,5,-2,-5,6,3,-2,-9,10,-3,2,-10,-2,2,4,2,-1,9,6,2,-1,-1,-3,-5,10,3,2,4,2], dtype = "int16")#candidate|968|(336,)|const|int16
call_967 = func_828_call(relay.reshape(const_968.astype('int16'), [14, 6, 4]))
call_969 = func_828_call(relay.reshape(const_968.astype('int16'), [14, 6, 4]))
func_557_call = mod.get_global_var('func_557')
func_558_call = mutated_mod.get_global_var('func_558')
call_978 = relay.TupleGetItem(func_557_call(), 0)
call_979 = relay.TupleGetItem(func_558_call(), 0)
output = relay.Tuple([call_947,call_963,const_964,call_967,const_968,call_978,])
output2 = relay.Tuple([call_948,call_965,const_964,call_969,const_968,call_979,])
func_984 = relay.Function([], output)
mod['func_984'] = func_984
mod = relay.transform.InferType()(mod)
mutated_mod['func_984'] = func_984
mutated_mod = relay.transform.InferType()(mutated_mod)
func_984_call = mutated_mod.get_global_var('func_984')
call_985 = func_984_call()
output = call_985
func_986 = relay.Function([], output)
mutated_mod['func_986'] = func_986
mutated_mod = relay.transform.InferType()(mutated_mod)
func_257_call = mod.get_global_var('func_257')
func_259_call = mutated_mod.get_global_var('func_259')
call_1034 = relay.TupleGetItem(func_257_call(), 0)
call_1035 = relay.TupleGetItem(func_259_call(), 0)
func_767_call = mod.get_global_var('func_767')
func_770_call = mutated_mod.get_global_var('func_770')
var_1037 = relay.var("var_1037", dtype = "float64", shape = (6,))#candidate|1037|(6,)|var|float64
call_1036 = func_767_call(relay.reshape(var_1037.astype('float64'), [3, 2]))
call_1038 = func_767_call(relay.reshape(var_1037.astype('float64'), [3, 2]))
output = relay.Tuple([call_1034,call_1036,var_1037,])
output2 = relay.Tuple([call_1035,call_1038,var_1037,])
func_1058 = relay.Function([var_1037,], output)
mod['func_1058'] = func_1058
mod = relay.transform.InferType()(mod)
var_1059 = relay.var("var_1059", dtype = "float64", shape = (6,))#candidate|1059|(6,)|var|float64
output = func_1058(var_1059)
func_1060 = relay.Function([var_1059], output)
mutated_mod['func_1060'] = func_1060
mutated_mod = relay.transform.InferType()(mutated_mod)
func_858_call = mod.get_global_var('func_858')
func_859_call = mutated_mod.get_global_var('func_859')
call_1094 = relay.TupleGetItem(func_858_call(), 0)
call_1095 = relay.TupleGetItem(func_859_call(), 0)
uop_1107 = relay.atan(call_1094.astype('float64')) # shape=(3, 4, 8)
uop_1109 = relay.atan(call_1095.astype('float64')) # shape=(3, 4, 8)
func_767_call = mod.get_global_var('func_767')
func_770_call = mutated_mod.get_global_var('func_770')
var_1112 = relay.var("var_1112", dtype = "float64", shape = (6,))#candidate|1112|(6,)|var|float64
call_1111 = func_767_call(relay.reshape(var_1112.astype('float64'), [3, 2]))
call_1113 = func_767_call(relay.reshape(var_1112.astype('float64'), [3, 2]))
func_984_call = mod.get_global_var('func_984')
func_986_call = mutated_mod.get_global_var('func_986')
call_1131 = relay.TupleGetItem(func_984_call(), 1)
call_1132 = relay.TupleGetItem(func_986_call(), 1)
func_767_call = mod.get_global_var('func_767')
func_770_call = mutated_mod.get_global_var('func_770')
call_1148 = func_767_call(relay.reshape(var_1112.astype('float64'), [3, 2]))
call_1149 = func_767_call(relay.reshape(var_1112.astype('float64'), [3, 2]))
func_514_call = mod.get_global_var('func_514')
func_520_call = mutated_mod.get_global_var('func_520')
const_1160 = relay.const(False, dtype = "bool")#candidate|1160|()|const|bool
const_1161 = relay.const([[False],[True],[False],[False],[False],[True],[False],[True],[False],[True],[False],[False],[False],[True],[True],[True],[False],[False],[False],[False],[True],[False],[True],[False],[False],[True],[False],[True],[True],[True],[False],[True],[False],[False],[False],[False],[False],[False],[False],[False],[True],[False],[False],[True],[True],[True],[False],[True],[False],[False],[True],[True],[False],[False],[True],[True],[True],[True],[False],[False],[False],[False],[False],[False],[True],[False],[True],[True],[False],[True],[True],[True],[True],[False],[False],[False],[True],[False],[False],[True],[False],[True],[True],[False],[False],[False],[True],[True],[False],[True],[False],[False],[False],[False],[True],[True],[False],[False],[False],[False],[True],[True],[True],[False],[True],[True],[False],[True],[True],[False],[False],[True],[False],[True],[True],[False],[False],[True],[True],[False],[False],[True],[False],[False],[True],[True],[True],[True],[True],[True],[True],[False],[True],[False],[False],[False],[True],[True],[True],[False],[True],[False],[True],[True],[True],[True],[True],[True],[False],[True],[True],[False],[False],[False],[True],[False],[True],[False],[True],[True],[False],[True],[True],[True],[True],[False],[True],[True],[True],[True],[True],[False],[True],[True],[False],[False],[False],[True],[False],[False],[False],[True],[False],[True],[True],[True],[True],[True],[False],[False],[False],[False],[True],[True],[True],[True],[True],[False],[False],[False],[True],[True],[True],[False],[False],[True],[True],[False],[False],[True],[False],[True],[False],[True],[False],[False],[False],[True],[True],[False],[True],[True],[False],[True],[False],[True],[False],[False],[False],[False],[False],[True],[True],[True],[False],[False],[False],[True],[False],[True],[False],[True],[False],[False],[False],[False],[False],[False],[True],[True],[True],[False],[False],[True],[True],[True],[True],[True],[True],[True],[True],[True],[False],[True],[True],[False],[True],[True],[True],[True],[False],[True],[False],[False],[False],[False],[False],[False],[True],[True],[False],[False],[False],[False],[True],[True],[True],[False],[True],[False],[True],[False],[False],[False],[True],[True],[False],[False],[False],[False],[False],[True],[True],[False],[True],[True],[True],[False],[False],[False],[True],[False],[False],[True],[False],[True],[True],[False],[False],[False],[False],[True],[False],[False],[True],[False],[True],[False],[False],[False],[False],[False],[True],[True],[True],[False],[True],[False],[False],[True],[False],[False],[True],[False],[True],[True],[True],[False],[True],[True],[False],[False],[True],[True],[False],[False],[True],[False],[False],[True],[False],[False],[False],[True],[False],[True],[True],[True],[True],[False],[False],[True],[False],[True],[True],[True],[False],[False],[False],[False],[False],[False],[False],[True],[True],[False],[True],[False],[False],[False],[False],[False],[False],[False],[True],[False],[True],[True],[True],[False],[True],[True],[True],[True],[False],[False],[False],[True],[False],[False],[True],[False],[True],[True],[True],[False],[True],[True],[True],[False],[True],[True],[False],[True],[True],[False],[False],[False],[True],[True],[False],[False],[True],[True],[True],[True],[True],[True],[False],[True],[False],[True],[False],[True],[False],[True],[True],[False],[False],[False],[False],[True],[True],[False],[True],[False],[False],[True],[False],[True],[False],[False],[True],[True],[True],[False],[True],[False]], dtype = "bool")#candidate|1161|(468, 1)|const|bool
call_1159 = relay.TupleGetItem(func_514_call(relay.reshape(const_1160.astype('bool'), []), relay.reshape(const_1161.astype('bool'), [6, 6, 13]), relay.reshape(const_1161.astype('bool'), [6, 6, 13]), relay.reshape(const_1161.astype('bool'), [6, 6, 13]), ), 0)
call_1162 = relay.TupleGetItem(func_520_call(relay.reshape(const_1160.astype('bool'), []), relay.reshape(const_1161.astype('bool'), [6, 6, 13]), relay.reshape(const_1161.astype('bool'), [6, 6, 13]), relay.reshape(const_1161.astype('bool'), [6, 6, 13]), ), 0)
func_375_call = mod.get_global_var('func_375')
func_378_call = mutated_mod.get_global_var('func_378')
var_1165 = relay.var("var_1165", dtype = "float32", shape = (192,))#candidate|1165|(192,)|var|float32
call_1164 = func_375_call(relay.reshape(var_1165.astype('float32'), [12, 8, 2]))
call_1166 = func_375_call(relay.reshape(var_1165.astype('float32'), [12, 8, 2]))
func_858_call = mod.get_global_var('func_858')
func_859_call = mutated_mod.get_global_var('func_859')
call_1188 = relay.TupleGetItem(func_858_call(), 0)
call_1189 = relay.TupleGetItem(func_859_call(), 0)
func_322_call = mod.get_global_var('func_322')
func_323_call = mutated_mod.get_global_var('func_323')
call_1194 = relay.TupleGetItem(func_322_call(), 0)
call_1195 = relay.TupleGetItem(func_323_call(), 0)
func_148_call = mod.get_global_var('func_148')
func_150_call = mutated_mod.get_global_var('func_150')
call_1224 = relay.TupleGetItem(func_148_call(), 2)
call_1225 = relay.TupleGetItem(func_150_call(), 2)
func_375_call = mod.get_global_var('func_375')
func_378_call = mutated_mod.get_global_var('func_378')
call_1235 = func_375_call(relay.reshape(var_1165.astype('float32'), [12, 8, 2]))
call_1236 = func_375_call(relay.reshape(var_1165.astype('float32'), [12, 8, 2]))
func_695_call = mod.get_global_var('func_695')
func_698_call = mutated_mod.get_global_var('func_698')
call_1237 = relay.TupleGetItem(func_695_call(relay.reshape(const_1160.astype('bool'), [])), 6)
call_1238 = relay.TupleGetItem(func_698_call(relay.reshape(const_1160.astype('bool'), [])), 6)
output = relay.Tuple([uop_1107,call_1111,var_1112,call_1131,call_1148,call_1159,const_1160,const_1161,call_1164,var_1165,call_1188,call_1194,call_1224,call_1235,call_1237,])
output2 = relay.Tuple([uop_1109,call_1113,var_1112,call_1132,call_1149,call_1162,const_1160,const_1161,call_1166,var_1165,call_1189,call_1195,call_1225,call_1236,call_1238,])
func_1246 = relay.Function([var_1112,var_1165,], output)
mod['func_1246'] = func_1246
mod = relay.transform.InferType()(mod)
mutated_mod['func_1246'] = func_1246
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1246_call = mutated_mod.get_global_var('func_1246')
var_1248 = relay.var("var_1248", dtype = "float64", shape = (6,))#candidate|1248|(6,)|var|float64
var_1249 = relay.var("var_1249", dtype = "float32", shape = (192,))#candidate|1249|(192,)|var|float32
call_1247 = func_1246_call(var_1248,var_1249,)
output = call_1247
func_1250 = relay.Function([var_1248,var_1249,], output)
mutated_mod['func_1250'] = func_1250
mutated_mod = relay.transform.InferType()(mutated_mod)
func_257_call = mod.get_global_var('func_257')
func_259_call = mutated_mod.get_global_var('func_259')
call_1306 = relay.TupleGetItem(func_257_call(), 0)
call_1307 = relay.TupleGetItem(func_259_call(), 0)
output = call_1306
output2 = call_1307
func_1316 = relay.Function([], output)
mod['func_1316'] = func_1316
mod = relay.transform.InferType()(mod)
output = func_1316()
func_1317 = relay.Function([], output)
mutated_mod['func_1317'] = func_1317
mutated_mod = relay.transform.InferType()(mutated_mod)
func_40_call = mod.get_global_var('func_40')
func_41_call = mutated_mod.get_global_var('func_41')
call_1332 = func_40_call()
call_1333 = func_40_call()
func_916_call = mod.get_global_var('func_916')
func_918_call = mutated_mod.get_global_var('func_918')
const_1340 = relay.const(False, dtype = "bool")#candidate|1340|()|const|bool
call_1339 = relay.TupleGetItem(func_916_call(relay.reshape(const_1340.astype('bool'), [])), 2)
call_1341 = relay.TupleGetItem(func_918_call(relay.reshape(const_1340.astype('bool'), [])), 2)
var_1350 = relay.var("var_1350", dtype = "bool", shape = (14, 1, 4))#candidate|1350|(14, 1, 4)|var|bool
bop_1351 = relay.floor_divide(const_1340.astype('float32'), var_1350.astype('float32')) # shape=(14, 1, 4)
func_307_call = mod.get_global_var('func_307')
func_309_call = mutated_mod.get_global_var('func_309')
call_1357 = func_307_call()
call_1358 = func_307_call()
func_257_call = mod.get_global_var('func_257')
func_259_call = mutated_mod.get_global_var('func_259')
call_1362 = relay.TupleGetItem(func_257_call(), 0)
call_1363 = relay.TupleGetItem(func_259_call(), 0)
func_695_call = mod.get_global_var('func_695')
func_698_call = mutated_mod.get_global_var('func_698')
call_1374 = relay.TupleGetItem(func_695_call(relay.reshape(const_1340.astype('bool'), [])), 5)
call_1375 = relay.TupleGetItem(func_698_call(relay.reshape(const_1340.astype('bool'), [])), 5)
func_695_call = mod.get_global_var('func_695')
func_698_call = mutated_mod.get_global_var('func_698')
call_1396 = relay.TupleGetItem(func_695_call(relay.reshape(const_1340.astype('bool'), [])), 2)
call_1397 = relay.TupleGetItem(func_698_call(relay.reshape(const_1340.astype('bool'), [])), 2)
output = relay.Tuple([call_1332,call_1339,bop_1351,call_1357,call_1362,call_1374,call_1396,])
output2 = relay.Tuple([call_1333,call_1341,bop_1351,call_1358,call_1363,call_1375,call_1397,])
func_1404 = relay.Function([var_1350,], output)
mod['func_1404'] = func_1404
mod = relay.transform.InferType()(mod)
mutated_mod['func_1404'] = func_1404
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1405 = relay.var("var_1405", dtype = "bool", shape = (14, 1, 4))#candidate|1405|(14, 1, 4)|var|bool
func_1404_call = mutated_mod.get_global_var('func_1404')
call_1406 = func_1404_call(var_1405)
output = call_1406
func_1407 = relay.Function([var_1405], output)
mutated_mod['func_1407'] = func_1407
mutated_mod = relay.transform.InferType()(mutated_mod)
func_858_call = mod.get_global_var('func_858')
func_859_call = mutated_mod.get_global_var('func_859')
call_1445 = relay.TupleGetItem(func_858_call(), 0)
call_1446 = relay.TupleGetItem(func_859_call(), 0)
output = call_1445
output2 = call_1446
func_1452 = relay.Function([], output)
mod['func_1452'] = func_1452
mod = relay.transform.InferType()(mod)
output = func_1452()
func_1453 = relay.Function([], output)
mutated_mod['func_1453'] = func_1453
mutated_mod = relay.transform.InferType()(mutated_mod)
func_148_call = mod.get_global_var('func_148')
func_150_call = mutated_mod.get_global_var('func_150')
call_1468 = relay.TupleGetItem(func_148_call(), 1)
call_1469 = relay.TupleGetItem(func_150_call(), 1)
func_322_call = mod.get_global_var('func_322')
func_323_call = mutated_mod.get_global_var('func_323')
call_1481 = relay.TupleGetItem(func_322_call(), 0)
call_1482 = relay.TupleGetItem(func_323_call(), 0)
output = relay.Tuple([call_1468,call_1481,])
output2 = relay.Tuple([call_1469,call_1482,])
func_1498 = relay.Function([], output)
mod['func_1498'] = func_1498
mod = relay.transform.InferType()(mod)
output = func_1498()
func_1499 = relay.Function([], output)
mutated_mod['func_1499'] = func_1499
mutated_mod = relay.transform.InferType()(mutated_mod)
func_557_call = mod.get_global_var('func_557')
func_558_call = mutated_mod.get_global_var('func_558')
call_1512 = relay.TupleGetItem(func_557_call(), 1)
call_1513 = relay.TupleGetItem(func_558_call(), 1)
output = relay.Tuple([call_1512,])
output2 = relay.Tuple([call_1513,])
func_1531 = relay.Function([], output)
mod['func_1531'] = func_1531
mod = relay.transform.InferType()(mod)
mutated_mod['func_1531'] = func_1531
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1531_call = mutated_mod.get_global_var('func_1531')
call_1532 = func_1531_call()
output = call_1532
func_1533 = relay.Function([], output)
mutated_mod['func_1533'] = func_1533
mutated_mod = relay.transform.InferType()(mutated_mod)
func_322_call = mod.get_global_var('func_322')
func_323_call = mutated_mod.get_global_var('func_323')
call_1536 = relay.TupleGetItem(func_322_call(), 0)
call_1537 = relay.TupleGetItem(func_323_call(), 0)
func_307_call = mod.get_global_var('func_307')
func_309_call = mutated_mod.get_global_var('func_309')
call_1544 = func_307_call()
call_1545 = func_307_call()
func_858_call = mod.get_global_var('func_858')
func_859_call = mutated_mod.get_global_var('func_859')
call_1547 = relay.TupleGetItem(func_858_call(), 0)
call_1548 = relay.TupleGetItem(func_859_call(), 0)
output = relay.Tuple([call_1536,call_1544,call_1547,])
output2 = relay.Tuple([call_1537,call_1545,call_1548,])
func_1550 = relay.Function([], output)
mod['func_1550'] = func_1550
mod = relay.transform.InferType()(mod)
mutated_mod['func_1550'] = func_1550
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1550_call = mutated_mod.get_global_var('func_1550')
call_1551 = func_1550_call()
output = call_1551
func_1552 = relay.Function([], output)
mutated_mod['func_1552'] = func_1552
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1498_call = mod.get_global_var('func_1498')
func_1499_call = mutated_mod.get_global_var('func_1499')
call_1611 = relay.TupleGetItem(func_1498_call(), 1)
call_1612 = relay.TupleGetItem(func_1499_call(), 1)
output = call_1611
output2 = call_1612
func_1615 = relay.Function([], output)
mod['func_1615'] = func_1615
mod = relay.transform.InferType()(mod)
output = func_1615()
func_1616 = relay.Function([], output)
mutated_mod['func_1616'] = func_1616
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1498_call = mod.get_global_var('func_1498')
func_1499_call = mutated_mod.get_global_var('func_1499')
call_1636 = relay.TupleGetItem(func_1498_call(), 0)
call_1637 = relay.TupleGetItem(func_1499_call(), 0)
func_40_call = mod.get_global_var('func_40')
func_41_call = mutated_mod.get_global_var('func_41')
call_1662 = func_40_call()
call_1663 = func_40_call()
output = relay.Tuple([call_1636,call_1662,])
output2 = relay.Tuple([call_1637,call_1663,])
func_1674 = relay.Function([], output)
mod['func_1674'] = func_1674
mod = relay.transform.InferType()(mod)
mutated_mod['func_1674'] = func_1674
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1674_call = mutated_mod.get_global_var('func_1674')
call_1675 = func_1674_call()
output = call_1675
func_1676 = relay.Function([], output)
mutated_mod['func_1676'] = func_1676
mutated_mod = relay.transform.InferType()(mutated_mod)
func_40_call = mod.get_global_var('func_40')
func_41_call = mutated_mod.get_global_var('func_41')
call_1791 = func_40_call()
call_1792 = func_40_call()
func_148_call = mod.get_global_var('func_148')
func_150_call = mutated_mod.get_global_var('func_150')
call_1815 = relay.TupleGetItem(func_148_call(), 0)
call_1816 = relay.TupleGetItem(func_150_call(), 0)
func_375_call = mod.get_global_var('func_375')
func_378_call = mutated_mod.get_global_var('func_378')
const_1821 = relay.const([5.300701,-6.998876,-0.372979,7.275465,9.624428,-1.421894,5.614081,-6.790936,-1.611705,-9.633732,9.515065,-8.129073,-4.458863,-7.860886,9.617129,0.230254,-1.681946,1.859090,7.597293,-0.609399,5.776314,-9.071010,-1.512159,7.508432,4.922083,-1.743257,-2.059913,-3.948427,7.615114,-1.489687,6.211564,2.897277,9.071557,-8.343333,7.443442,-5.173507,2.975579,2.258569,2.480762,8.904393,2.320656,-9.387610,-3.593075,-4.923289,7.783054,1.526493,-2.315900,-0.845459,0.494088,0.207796,8.125887,3.015355,-3.721693,-7.577108,8.183781,-6.415393,6.081170,-8.333096,-7.125189,6.558833,2.325866,-0.464024,9.418960,-0.595590,8.603096,-5.950818,4.646126,-5.175033,-0.993888,9.589302,-5.939443,-5.736742,-9.897322,6.158876,-9.395457,-3.892474,6.249133,4.697591,3.176130,-6.968909,6.421792,9.308666,-1.321009,-6.081037,-1.321411,7.398592,-0.173711,5.846014,-8.658340,1.861597,0.823896,8.890481,-4.540149,-7.736708,-5.885701,-0.539983,0.641567,-0.881128,7.798013,-8.331742,-5.983903,-4.731630,-6.200523,-6.826802,6.999796,6.152434,1.268361,5.973712,1.822546,-4.418984,-9.554304,-6.206654,-8.236538,-7.753892,7.832038,-3.234427,-2.162190,-6.051480,-0.053658,1.839390,-5.504362,-1.232139,9.585317,0.715081,7.249631,-3.895355,9.530583,8.330360,4.585048,0.821938,5.690678,5.453038,3.896601,-3.519842,-8.813767,3.710598,-5.806049,-4.119310,7.818320,-9.802906,9.492874,5.132576,5.630232,2.047915,-2.479429,-4.746601,-8.206998,4.657820,5.189259,9.270180,7.891033,8.446827,-9.057578,-4.351349,2.971570,1.682105,2.890083,3.073174,9.920205,-2.502363,-9.728685,9.408667,-2.858985,-3.660147,-4.758109,7.843848,-7.098768,6.774903,-1.410064,-9.100169,9.372532,9.783515,-0.164913,7.459840,3.420835,0.554079,-7.858337,-7.266962,4.937125,7.524340,-1.712377,-2.028397,4.114463,6.377945,8.673388,8.994945,3.660353,9.953449,-2.858925,-0.493934,-6.810870,7.109333], dtype = "float32")#candidate|1821|(192,)|const|float32
call_1820 = func_375_call(relay.reshape(const_1821.astype('float32'), [12, 8, 2]))
call_1822 = func_375_call(relay.reshape(const_1821.astype('float32'), [12, 8, 2]))
output = relay.Tuple([call_1791,call_1815,call_1820,const_1821,])
output2 = relay.Tuple([call_1792,call_1816,call_1822,const_1821,])
func_1823 = relay.Function([], output)
mod['func_1823'] = func_1823
mod = relay.transform.InferType()(mod)
mutated_mod['func_1823'] = func_1823
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1823_call = mutated_mod.get_global_var('func_1823')
call_1824 = func_1823_call()
output = call_1824
func_1825 = relay.Function([], output)
mutated_mod['func_1825'] = func_1825
mutated_mod = relay.transform.InferType()(mutated_mod)
func_40_call = mod.get_global_var('func_40')
func_41_call = mutated_mod.get_global_var('func_41')
call_1831 = func_40_call()
call_1832 = func_40_call()
func_1452_call = mod.get_global_var('func_1452')
func_1453_call = mutated_mod.get_global_var('func_1453')
call_1841 = func_1452_call()
call_1842 = func_1452_call()
func_799_call = mod.get_global_var('func_799')
func_801_call = mutated_mod.get_global_var('func_801')
var_1844 = relay.var("var_1844", dtype = "float32", shape = (192, 1))#candidate|1844|(192, 1)|var|float32
call_1843 = relay.TupleGetItem(func_799_call(relay.reshape(var_1844.astype('float32'), [192,])), 2)
call_1845 = relay.TupleGetItem(func_801_call(relay.reshape(var_1844.astype('float32'), [192,])), 2)
func_1531_call = mod.get_global_var('func_1531')
func_1533_call = mutated_mod.get_global_var('func_1533')
call_1848 = relay.TupleGetItem(func_1531_call(), 0)
call_1849 = relay.TupleGetItem(func_1533_call(), 0)
const_1850 = relay.const([[6.901285,-0.785326,4.004046,-8.768074,-3.522632,-9.217921,-7.425650,0.680871,3.924101,-3.315821,-6.468656],[1.313232,5.776789,-0.688462,-0.404205,-8.270504,4.247362,-7.118348,1.257123,-6.818539,1.977278,-6.793728],[8.343430,3.961560,-8.559696,7.313913,-0.918984,4.610731,3.042278,-8.061294,-4.704899,3.511625,0.641672],[-1.806104,-0.001895,-7.787088,2.420219,8.415775,5.393312,-0.856320,-2.152159,-5.047625,-4.007418,-0.923460],[-9.303031,7.441451,6.948083,-6.446794,-0.431018,-5.701667,0.757802,5.576272,9.782198,-2.023774,0.787643],[-7.096338,-9.662795,-7.188672,-4.160608,-6.115071,3.773771,8.440656,-6.568144,-2.308678,9.213014,3.136823],[0.362177,2.030928,2.541626,0.429158,-0.577554,2.398839,6.639113,-4.073659,-0.827351,-8.464444,-9.295130],[6.730693,7.780326,-4.162367,-7.439102,-3.668072,-9.833201,-7.508597,2.951701,-2.432458,2.089128,-3.511295],[-7.992685,-7.001818,3.651524,-6.868497,1.884411,-4.986829,5.972252,7.723678,-7.074038,-6.928444,3.675056],[-2.703081,-8.571234,5.377098,-5.018443,-3.958270,-3.924388,-7.027242,7.257999,5.497513,-2.282481,-2.153344],[-3.371109,7.903040,0.212315,6.806039,-5.639501,2.018284,2.065103,-4.602419,-7.067257,-3.394439,9.910276],[-3.697818,2.496166,3.313999,3.036896,-5.867067,0.952013,-9.719101,8.528698,-8.590489,8.460098,-6.852550],[-8.558867,6.248001,-3.350268,1.459360,-3.590289,-5.816463,5.313118,7.282510,8.100761,7.381603,4.797568],[3.825578,5.618640,-9.353798,1.146154,2.233939,9.542597,-7.714650,-9.452070,9.395204,4.004297,4.886579],[-2.071157,8.386428,-0.786948,-6.487065,-6.468365,-1.635234,7.181588,4.462504,8.536799,-8.949674,5.673236],[-6.915008,-1.311665,-6.826452,-0.879445,7.101406,-1.233197,-5.804826,5.629512,-7.497662,2.088687,0.080808],[4.767129,8.590599,-8.591326,7.792580,3.505539,9.585972,3.062089,3.043650,7.362685,-9.754413,-9.969070],[-2.363912,-8.361048,6.498056,7.532751,-1.521693,8.120668,-8.697264,-9.836960,3.282957,3.134928,4.382920],[-8.076369,-9.170922,4.794293,0.242546,-2.183865,3.003726,-1.950250,-1.541023,-9.208553,-4.522643,-2.912684],[5.521368,-5.507535,-7.008571,8.548049,2.507838,0.864531,-2.079066,-1.691553,-8.263239,6.636976,9.071823],[-9.400400,-0.813654,8.521529,3.865867,9.648701,-4.273851,9.322573,4.772184,-1.990563,6.881316,1.432253],[9.247219,7.234459,-7.313676,6.484290,9.526831,1.907675,-8.664090,-3.354772,-8.059351,-5.199101,-9.501587],[-4.774752,2.512910,-4.968584,-4.601481,-1.643153,0.964310,9.487670,-8.832103,-6.957810,-0.410025,4.156758],[-8.350598,-4.190905,8.048939,8.551670,5.178473,-0.996933,-6.270044,2.288162,-2.753597,-9.295962,6.148498],[4.844561,2.273305,5.737772,0.365961,-7.134456,6.193555,-0.934236,-1.543269,-9.334807,5.242136,-8.797343],[7.758017,-8.195638,5.417261,5.181110,-1.717921,-3.491024,-0.076261,-9.651091,7.455562,0.396095,1.941545],[7.841194,4.457622,4.946390,-8.590329,8.121467,1.967526,6.494996,-4.049622,-9.263115,8.436969,-7.067786],[-7.393569,7.718835,-9.571513,-7.120161,3.298770,5.334237,7.491679,4.224861,-1.438631,3.959346,6.555494],[-3.665542,-4.508257,-6.133455,7.940378,3.319578,4.748344,1.979376,-8.477657,-0.837736,-2.889991,-1.755037],[-9.116419,3.189965,-4.042970,3.964427,-2.417898,-1.359490,-3.156552,-5.923078,0.739420,5.000457,6.260062],[-9.436226,9.777802,9.950152,-1.490655,6.251080,2.985854,0.394631,-8.661915,8.815081,-6.150003,6.735911],[4.732737,3.087024,3.370313,8.946300,0.181036,-5.077919,-4.726640,-7.497839,-8.174431,-6.317757,8.430742],[3.849316,-3.419238,-8.002891,-4.656990,9.626827,4.361306,7.296611,8.723453,3.776469,-7.346665,8.636703],[7.350003,-3.934947,-0.776716,-6.357421,-8.773366,3.210252,-5.871785,-5.449586,7.663938,-7.402024,-4.523200],[2.124804,1.000122,-1.292704,0.674580,-2.424918,-1.689513,-6.648591,2.323604,-5.534646,-6.108576,-8.040524],[4.158008,-5.913437,-9.900811,0.804883,-9.892095,6.708722,-6.976075,4.140833,2.681049,-6.272164,-9.335172],[-4.325666,1.768816,-6.759839,-8.592655,2.321260,8.400856,-7.142893,-8.869141,-7.414372,9.543291,-2.092657],[8.153893,4.240507,-9.354774,-3.176723,-2.657688,-8.488778,2.662863,7.190961,-1.050674,7.472368,-0.749476],[9.312094,-5.415699,8.601162,3.707902,7.033465,-6.921540,-0.206945,-7.184129,0.890031,6.087184,7.843286],[-9.700006,5.239445,9.623616,-5.885255,-5.496536,-0.575850,9.680053,-1.964267,-4.976281,-1.488490,-3.389667],[1.362523,6.273101,8.446877,-6.862115,-3.391407,-4.832872,1.188739,-9.087390,1.241339,-1.214707,0.449667],[-5.689778,-9.721038,4.423219,4.170862,5.295485,5.312708,7.146144,-9.337552,4.843761,6.880595,-4.092468],[4.376281,-5.877368,8.270080,-8.210645,3.668346,8.949334,2.079032,-1.652941,-8.201507,6.771165,-0.128931],[4.113474,1.099117,3.517173,-4.044469,1.898109,7.002813,-8.310377,-0.334354,0.295417,5.129818,-8.555050],[-5.340642,3.103405,-8.347767,-8.058400,-1.629079,8.483394,-3.421058,-6.519382,-5.433201,-3.222866,9.721000],[0.721216,5.120934,1.118810,5.780945,-8.165414,-8.830652,-8.412520,-9.237306,-6.530387,-1.490688,-0.512429],[-6.253040,3.944494,2.844200,-6.818042,3.379375,-9.075887,2.343256,2.513379,1.963950,-2.230733,-8.896161],[5.553490,8.662946,2.595487,5.863456,-4.909567,-7.572615,7.128061,9.430130,-1.802227,6.755635,4.455854],[9.341868,5.157829,-7.400673,-8.235248,-5.462615,-7.974650,6.730899,-8.990486,4.328873,1.219686,-8.403845],[2.172956,-3.402476,-8.996501,5.944827,-2.772923,8.715371,3.962746,3.595778,-4.321099,6.811427,6.286225],[-2.753040,-8.956928,-1.480254,8.845957,-2.737894,-4.384137,-9.387000,-7.254739,8.082347,-5.865808,-6.410264],[-4.877244,-7.619756,7.310055,9.781121,-9.591757,-2.905497,-7.067765,-5.538220,-4.457599,-9.355453,-6.829574],[9.986605,-0.782864,6.251779,5.805606,2.795997,-3.304984,-3.407479,9.635274,-8.334566,5.087847,-8.409123],[-7.520157,7.579434,8.074363,3.679350,4.892882,-5.073358,5.699234,-7.430386,3.099736,9.465916,0.487054],[-8.643081,8.754175,3.377679,1.956862,-5.381091,-7.184495,-8.229999,-1.211614,3.009454,6.466436,7.504272],[-4.035993,7.727614,7.657532,0.727265,0.136152,-9.615651,-6.623848,1.420948,1.935829,8.681839,-4.604858],[-6.341266,-8.381678,-3.837835,5.580221,-3.828705,4.367768,-1.427568,-8.166892,-4.179615,3.650694,6.542573],[-1.049355,0.105451,-5.808532,1.598449,4.252319,5.579488,-9.653501,1.036500,-2.161367,3.648729,3.310387],[-2.145782,9.559264,0.223239,8.859157,-5.502607,-5.659689,-6.631775,4.984785,7.294269,7.157013,-7.115392],[-2.484551,5.060552,7.696418,-7.329554,-1.323049,2.273210,4.808188,-9.476152,3.695968,-5.002016,5.562595],[-4.954742,4.831439,1.686115,9.233024,-7.433442,0.824668,-6.650084,-1.126142,3.742826,2.851112,-2.908245],[-9.940913,-2.748598,4.302392,7.622395,0.051646,6.683975,6.673984,7.599273,-5.565627,-9.223491,8.766857],[7.642939,7.221139,9.781209,0.695119,-4.801050,-3.028962,9.027966,6.911562,-3.265964,-2.879746,2.840528],[-5.886419,-9.679175,-8.608669,-0.890836,8.426500,3.496483,4.946052,-3.796330,-6.381805,-4.220341,3.857228],[1.588537,-0.482476,8.872942,9.075934,-1.606220,8.559794,4.527684,5.126149,0.629447,4.243775,2.598206],[3.695431,3.335428,-6.555745,2.159182,2.341456,8.624495,-3.263592,-7.741070,4.789479,-0.726085,-3.341318],[5.419123,7.215202,-2.738689,7.550536,1.594055,6.803884,3.095747,-4.739301,9.342746,7.781006,9.226076],[3.471476,6.645524,-8.667968,4.334077,2.660501,-0.379136,-8.760985,7.499319,8.593898,-3.319734,1.040485],[-4.953461,-2.706091,6.106276,-0.070865,-4.746296,0.988762,2.928952,3.041427,-1.093206,8.691121,1.197209],[8.926718,9.042500,-5.245631,-9.862276,9.687713,0.745403,-6.783492,7.947662,-4.578043,2.796167,-7.165317],[3.946406,8.164376,-8.337407,7.456042,-6.300663,2.395590,4.791205,-1.506143,8.844221,-4.677505,1.377861],[-2.253787,-8.617867,-1.740950,-3.891802,-3.151395,-0.205933,5.918304,-9.352172,9.749132,1.797213,-8.653269],[-5.150265,-8.702533,7.328596,-8.062086,-5.622436,9.617531,9.154395,-3.687228,-9.661594,-5.973896,-0.018782],[-8.809384,-4.015414,-2.219200,-1.646067,-8.743869,8.357642,-2.180067,1.153563,3.204595,9.559908,-7.900395],[9.166305,-8.425434,7.953698,-0.762720,-6.314909,-8.794816,-2.709862,9.288111,-2.048236,3.940315,-3.282720],[-6.637823,7.783133,9.206251,-9.536135,7.516810,-0.119592,-4.567605,-4.668947,-9.834087,0.716762,6.369413],[6.009939,-0.034183,-4.994817,7.868559,9.931458,4.168235,9.126175,-6.040118,-8.859436,9.740109,5.508891],[0.621887,3.058595,6.927889,-2.196953,-4.901074,2.690379,3.184246,6.344607,-3.163129,-9.255106,9.935369],[9.968895,-1.455043,2.714178,-3.880473,4.182630,0.973872,8.427581,6.489771,8.407758,3.275045,-8.591070],[4.899623,4.513129,-7.124167,7.974185,-8.483404,6.805562,-6.378163,-2.084968,-1.500001,-8.916925,-0.774577],[-2.727652,-8.408042,-0.354792,-5.816116,-0.367094,-4.132552,3.389265,-7.239428,-1.748807,4.065409,8.787616],[-3.031579,6.025006,3.584987,-0.591859,6.125011,6.380730,0.513147,-7.204912,-5.351228,0.678137,-6.876151],[5.371331,5.835738,6.800918,-8.475744,-9.341285,1.253435,1.176075,-3.369823,-6.688327,-1.389591,2.897511],[3.120924,1.180215,-3.622031,-3.281828,6.371500,5.191821,7.646891,-7.430605,4.455784,2.420596,-2.507360],[5.137879,-5.608823,-2.487134,3.936917,-0.481600,0.416026,-5.383033,-1.036488,1.961201,7.994077,-2.375803],[9.273648,-1.109787,-2.307786,7.757271,-5.626772,9.369796,5.166041,7.839658,3.148430,8.952516,9.498479],[-5.727288,3.587300,1.424005,7.619736,8.904425,-4.899183,9.506287,4.587781,9.948328,-8.001954,5.369355],[0.529847,-4.527839,-4.958140,1.386184,-3.821545,-6.727699,8.798081,-4.501750,8.714497,-1.020475,3.780297],[-5.476166,-0.220541,-4.764915,-6.412686,-3.210758,-9.615331,-8.671193,6.003655,-4.084609,-0.442158,4.067240],[-5.604242,-2.624695,3.182459,-3.106385,-8.725015,-8.515269,-7.457180,4.705494,-5.024442,-3.488624,4.284997],[9.562787,4.473554,-0.552672,-9.004935,1.004234,2.064036,1.765984,-4.266041,7.228445,-7.351007,-1.303174],[-4.002276,-0.087482,4.921363,4.876346,5.595599,9.531412,-3.253677,-0.753844,2.910823,1.763517,5.960103],[-1.994530,-6.760830,1.965269,3.510784,-7.450156,5.003860,-3.941998,5.003382,4.169080,-1.962961,8.885807],[-4.194728,-5.489120,-5.629323,-3.029037,-2.211622,5.263211,-0.486369,3.585031,-6.505977,3.913545,-0.777401],[1.254952,4.004935,9.818683,5.670827,-9.641756,-2.072320,-7.705893,2.714607,1.834336,0.457323,-3.311146],[3.256162,4.896537,4.747752,9.982899,-1.350607,-0.558402,-8.592193,1.762228,-4.903426,1.036727,-5.776969],[8.017857,9.384839,8.897879,-5.272206,-0.548595,-7.301819,8.009646,9.098454,6.503833,8.806768,2.150176],[8.281728,-6.755464,2.436950,7.709143,9.305314,4.597288,0.847581,4.012443,-7.460081,9.240660,1.325074],[8.282863,8.107087,-7.302532,-2.995447,-5.739959,-2.352210,0.812049,8.149531,-6.665509,-9.211398,9.771300],[-6.783853,3.751071,-4.270649,9.953181,5.406319,-2.602587,-0.214649,-8.428736,3.910116,-0.186253,9.858430],[1.061373,-0.485900,5.414083,2.738720,-0.023218,3.982402,-0.900258,-2.675241,4.511786,-5.499636,4.008331],[-3.260667,2.281948,-6.841225,8.545042,-0.741354,-0.976692,-2.861292,2.863116,-0.072555,-5.332145,8.895452],[-8.781133,-8.894377,9.172227,0.225746,1.988275,-8.490786,2.920199,8.198136,-1.960046,6.136256,-7.053116],[-3.773109,5.929329,-9.220941,-8.482713,4.101226,1.786891,-1.721300,-4.708508,4.654836,7.968029,8.470922],[0.916672,-5.858209,-2.724609,-2.877953,7.396689,-5.041302,-4.753163,-7.323139,-7.177456,0.483161,-9.075178],[-0.664803,5.522575,-4.891187,-4.414320,-9.496414,-4.681584,7.123386,-0.477218,-2.175422,0.383255,7.947903],[5.517210,-1.811327,2.568955,4.819256,-1.244940,-0.407730,-3.596947,-4.941670,-9.246553,-2.084045,4.833636],[0.071374,7.808183,-3.714495,-6.148274,-0.916633,3.025520,3.222596,-8.533696,-2.438362,7.540799,4.049109],[-6.015439,-3.605243,-0.488242,7.357051,-9.958055,0.952849,-2.521664,-0.499015,1.362071,-3.848787,-5.080133],[6.231138,1.913372,8.661315,6.616629,-9.703337,-1.766090,-2.448909,2.094267,3.992286,4.657632,4.740511],[-1.257009,-9.865098,0.517521,-1.385033,7.755351,-6.802296,-0.348761,2.026359,-3.005503,3.912920,-8.576831],[6.394727,0.848477,8.062041,-4.272218,7.481336,4.588894,-5.999256,-3.078291,-1.610304,3.262352,-2.252793],[-9.539086,3.775753,8.372658,2.260693,-7.528308,5.647035,5.649830,-2.084034,-8.775085,-4.402052,-6.561312],[-4.640195,-3.198535,-7.874549,7.965935,0.343412,-4.888678,4.730428,2.448402,9.072374,3.502002,4.460284],[1.753617,-1.414078,4.763007,1.874601,-2.721782,6.395358,-4.035038,-6.674535,-3.437898,8.467234,-1.515218],[1.399451,-3.355189,2.555007,5.985046,-4.073889,2.171371,-4.632397,-4.829900,-4.833353,1.217179,0.140602],[8.017781,-3.843908,2.017941,-5.894522,-8.042711,5.903212,-0.348788,-2.517340,6.053132,-9.750313,-9.734847],[-5.392855,9.403998,9.749543,-6.058673,-1.155331,-4.538349,6.379527,7.794662,5.490784,6.412139,-7.914093],[6.280896,-6.341505,5.605669,9.857770,9.598115,-2.333026,-4.813641,-2.939343,-2.177900,-6.739371,5.944754],[-6.900112,3.840959,-0.785125,-3.478039,-5.928063,0.118246,8.893990,-8.997351,-0.684295,-9.548178,-8.079394],[-3.406900,5.740554,4.204333,9.803852,5.483058,3.735142,5.625866,-5.141287,-9.381313,-4.036699,7.608002],[6.317251,-4.661765,7.274157,-5.450238,-7.036389,-6.673745,-1.780136,5.134044,-0.061811,8.832519,-5.957579],[7.369737,8.043668,0.747819,-4.337091,7.495752,-5.563276,1.408611,-6.187160,7.842603,9.472444,-2.309641],[-7.704222,8.446541,-4.792145,-8.757740,-8.463363,2.320296,-3.983103,1.488842,4.372649,-5.438079,-2.012154],[-2.621095,6.408143,4.272562,1.951101,-5.331137,-7.606738,9.907433,3.076047,1.148875,7.642181,8.298149],[3.246643,-3.958259,5.178004,9.266961,1.608131,-7.779651,6.551663,3.669086,0.015844,-5.751483,3.824067],[-9.455819,-2.351784,-4.991668,7.067421,3.108494,-1.231276,1.926037,-8.949213,-3.039976,-9.123886,-2.198617],[-4.063375,6.959621,-8.759589,3.064129,3.567359,-2.557318,5.651822,3.258593,-7.593543,-0.870180,2.593206],[-1.662375,-4.257094,6.336497,5.254935,-2.609409,4.001893,9.451468,-8.242335,9.703556,-7.904900,9.324336],[7.747027,-9.222599,5.085238,-7.896214,8.561960,-7.139031,2.453504,-8.454337,1.954706,3.160261,-9.397932],[-6.577904,4.448126,-7.290840,4.335809,-4.000139,8.466371,-7.094848,8.186087,2.380418,0.252238,-4.732860],[1.042183,2.197272,9.718318,5.068958,2.804421,-8.975097,8.176680,5.476636,-5.085059,1.947363,-2.935937],[-9.611309,4.992539,-3.609027,9.641514,7.455451,-4.536380,-2.132730,5.073343,2.211472,2.270694,-7.613166],[4.190470,-0.542878,2.755020,7.382581,3.409688,5.930106,2.878829,-5.504912,-3.080161,4.725103,-8.484893],[-8.565995,5.547034,8.758528,-2.901603,1.266220,2.330767,5.804139,-3.065251,-8.897537,6.467683,-8.772681],[-6.715001,3.972262,-5.206189,1.733509,-4.185656,8.989082,3.121378,2.023281,-6.547244,1.505640,-0.247074],[-9.416980,6.674448,-5.248954,-9.566221,8.406898,2.377291,2.966083,5.520242,6.656379,-7.970229,3.227984],[0.226187,4.487964,-1.794610,9.381467,-3.349572,2.886783,-6.134991,-8.022672,-3.388599,2.578807,-4.675365],[2.120950,4.376339,-8.021757,3.538468,-0.940727,-4.302068,-9.234122,-4.649285,5.678230,2.885568,1.203942],[-1.942833,-6.077812,6.263224,5.602333,-4.997572,-3.596480,7.728860,-6.478644,-7.704805,5.775212,-4.951856],[5.753460,6.172188,5.514303,4.823810,-9.231742,-5.317961,-3.945052,1.163414,-4.627148,1.623277,9.548816],[0.097487,4.446749,-6.988265,-2.438724,2.292057,-4.925197,-4.799095,6.988255,-1.421529,9.202789,7.405683],[-5.918138,3.660725,-2.430183,9.867896,1.108094,2.792536,5.359272,1.966522,6.136084,3.160911,2.420745],[3.890445,-3.591426,9.083837,8.435403,9.567709,9.992127,-6.786800,2.347154,3.496560,-8.443862,-5.613963],[3.388458,8.668454,-3.345820,-1.280837,-1.418395,-2.422938,8.249239,-5.758697,-9.399757,-1.401943,7.525748],[-5.791819,2.890399,8.935314,-0.301876,6.355752,-4.206952,-7.105845,6.819727,-0.748457,7.578233,-8.374691],[-1.361784,3.770568,8.688047,-5.857031,-2.687485,4.777017,9.757778,7.592971,-6.066167,3.546765,4.470987],[3.053885,-3.080934,-4.065398,3.098903,-7.274267,8.558223,-3.081044,7.956388,3.633555,2.519680,3.461614],[-3.753261,8.129496,4.444407,5.992362,-2.789076,-3.047932,-3.852678,-9.368360,5.366431,-5.424446,-7.972857],[7.894686,0.940672,0.009053,-0.738853,0.472256,4.994872,3.339429,7.285450,7.479895,-8.916045,-6.817867],[-5.312913,-9.268729,3.249682,1.461614,4.372214,-6.123075,1.752666,-0.422829,-1.002255,-5.923649,-5.102394],[3.457405,-4.223025,6.963049,-6.443882,-7.334951,0.867957,-7.492653,2.239695,-8.901474,3.148506,2.792581],[8.246373,-8.254980,-3.204695,8.709872,-4.911898,-9.992072,-7.244302,0.183783,-7.876446,5.657279,-0.947216],[-5.322639,0.990176,6.384352,5.532050,-8.659968,-8.813536,9.321969,9.566581,5.612969,2.664026,9.957273],[8.268522,-7.428871,-7.869523,6.685573,2.242740,-6.287668,3.134868,2.240436,-8.965237,8.479704,-5.231501],[0.187499,4.030022,-6.163106,2.987151,-6.463641,-6.977400,-4.088957,3.356079,-2.468092,2.572890,4.436159],[-3.376690,-0.983495,-4.283222,4.012912,-6.967693,3.663833,4.322266,-7.711520,2.534897,8.712538,8.243875],[-6.118032,-4.249977,8.209263,2.984352,-8.249247,-7.242329,-6.564137,-3.462583,9.242823,9.014694,-9.713616],[-5.441262,4.846000,-0.240127,-8.202359,-5.832156,-3.985139,5.598880,-7.740929,-6.894658,-7.024874,8.769937],[-5.621745,-8.843324,-0.642826,-3.179357,-3.369213,2.913119,-5.388664,-3.005222,6.378872,3.621784,6.240855],[-8.325822,1.096136,-1.033125,6.552119,-8.090182,0.512005,1.870257,-6.344194,8.884800,1.941790,-3.347410],[-6.343708,-5.665326,0.057291,8.565902,-0.144550,8.760644,-4.209881,0.886641,5.986750,9.554154,-0.851346],[0.172914,-6.943462,6.934272,0.750721,1.059163,-7.029862,-5.939889,8.946948,0.118564,5.200430,2.727250],[-2.190008,4.924013,0.374974,8.711694,8.568788,-9.147256,1.697508,5.238875,-2.526470,-9.841564,-6.945549],[-5.220975,-3.120610,0.626222,-9.420262,9.652945,9.139500,4.333161,-0.197104,-5.406906,6.453762,4.381316],[-9.599978,5.346549,-3.012112,-7.368173,-2.462918,-8.847190,-7.296770,-2.047456,2.835301,6.370986,-8.314893],[6.409758,6.735404,7.381174,-5.139800,3.126453,9.421178,8.676330,-2.231525,9.394399,4.504395,0.309993],[7.052660,-9.541865,-8.837084,-6.384690,-5.037372,7.131338,4.486900,-1.507808,0.771581,5.144391,6.234588],[-7.206366,-5.869223,-4.940767,-6.818935,1.953188,-6.160050,-8.585277,4.032574,5.943771,-2.157580,-3.059033],[8.857116,3.556266,-7.045998,-2.557284,-3.111833,-1.886985,-4.203351,-9.457658,-0.518456,-6.598801,6.803197],[5.317589,4.003233,2.863742,3.342428,-0.210824,-7.417694,-8.355288,-1.467732,-0.290005,9.664006,4.385550],[-4.111530,-3.905167,1.662606,9.609307,9.854205,3.398874,3.768024,-3.843834,-0.079352,-5.303873,3.615608],[-3.207589,1.224677,-7.989247,4.391433,-4.838168,4.016984,-3.244834,6.776009,4.828173,4.554304,-3.543891],[3.027118,2.688726,4.557072,5.040808,-4.063352,-6.681333,-1.534501,1.971875,-1.471425,6.357775,-3.021725],[-9.536909,9.284815,2.783322,-3.233047,-4.410935,-5.618717,-5.347034,1.880496,-9.456843,5.940670,1.746543],[7.299242,9.433421,-2.477004,8.368274,-1.187051,-0.052861,-6.432773,-9.800527,6.099349,-5.811515,0.502083],[8.689799,-4.842029,-8.691433,-5.989131,-3.968521,-9.667089,1.124695,-5.787964,-2.369587,-4.910651,2.075484],[-8.023644,-4.213244,-1.514738,0.991912,3.987843,-9.070280,3.637998,7.469896,-6.988371,9.209883,4.942957],[9.182427,-5.615078,-8.641442,-1.030006,6.732656,-7.248345,3.841586,-6.703122,-1.787951,7.978817,-8.417164],[2.820898,5.755782,6.244588,0.029927,8.367165,-4.704719,-4.022846,4.025465,-8.742690,9.934427,-1.782114],[0.494506,5.120018,-6.434268,-0.754525,8.360558,-3.244660,8.792129,-4.385976,-4.866225,9.489888,5.790361],[0.073608,5.165011,4.952366,-3.707782,9.916534,-0.865376,8.736157,7.498891,0.494567,-1.181938,5.584939],[1.598002,-6.384224,-3.086356,2.457255,8.458671,-6.866034,-4.471647,6.142746,8.060881,7.827293,3.702564],[-2.058624,-9.135196,-5.721817,6.650084,1.713009,7.001841,-1.677343,0.637997,1.627972,-9.043364,9.808257],[9.234943,-3.531416,3.544524,-1.694545,-0.681299,-2.790376,0.485002,6.019293,-1.678938,1.410644,-0.417827],[0.112365,0.193972,-8.696287,-2.809682,4.953292,-4.592664,-0.397400,7.208902,9.874945,1.646032,-7.953630],[-6.958045,9.480269,-3.481843,-6.661784,-2.025194,1.608980,-1.637049,-5.629773,4.421263,-6.319447,6.599068],[-5.539190,0.187735,-0.767844,3.491699,2.640580,6.690317,-1.652944,-4.436046,-3.956693,9.414446,-5.140617],[-4.746859,-3.862330,-0.829159,1.596559,-3.302180,-6.863209,5.279057,-4.249538,-7.811490,-0.077306,3.592527],[8.400650,4.632155,-5.867495,0.584356,-6.715801,4.552980,-3.024162,0.035637,7.721646,2.358347,-4.871639],[1.680015,5.662487,-0.774421,2.749141,-3.587453,9.161275,-5.453193,-6.847970,8.203559,8.219387,-2.258586],[-8.339138,-7.455616,3.220550,-5.505145,-4.323207,-9.639325,6.117464,-1.044288,-2.606735,4.352560,-1.109068]], dtype = "float32")#candidate|1850|(192, 11)|const|float32
bop_1851 = relay.subtract(var_1844.astype('uint8'), const_1850.astype('uint8')) # shape=(192, 11)
func_375_call = mod.get_global_var('func_375')
func_378_call = mutated_mod.get_global_var('func_378')
call_1857 = func_375_call(relay.reshape(call_1843.astype('float32'), [12, 8, 2]))
call_1858 = func_375_call(relay.reshape(call_1843.astype('float32'), [12, 8, 2]))
uop_1863 = relay.erf(const_1850.astype('float64')) # shape=(192, 11)
output = relay.Tuple([call_1831,call_1841,call_1843,call_1848,bop_1851,call_1857,uop_1863,])
output2 = relay.Tuple([call_1832,call_1842,call_1845,call_1849,bop_1851,call_1858,uop_1863,])
func_1865 = relay.Function([var_1844,], output)
mod['func_1865'] = func_1865
mod = relay.transform.InferType()(mod)
var_1866 = relay.var("var_1866", dtype = "float32", shape = (192, 1))#candidate|1866|(192, 1)|var|float32
output = func_1865(var_1866)
func_1867 = relay.Function([var_1866], output)
mutated_mod['func_1867'] = func_1867
mutated_mod = relay.transform.InferType()(mutated_mod)
func_984_call = mod.get_global_var('func_984')
func_986_call = mutated_mod.get_global_var('func_986')
call_1894 = relay.TupleGetItem(func_984_call(), 1)
call_1895 = relay.TupleGetItem(func_986_call(), 1)
output = relay.Tuple([call_1894,])
output2 = relay.Tuple([call_1895,])
func_1896 = relay.Function([], output)
mod['func_1896'] = func_1896
mod = relay.transform.InferType()(mod)
mutated_mod['func_1896'] = func_1896
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1896_call = mutated_mod.get_global_var('func_1896')
call_1897 = func_1896_call()
output = call_1897
func_1898 = relay.Function([], output)
mutated_mod['func_1898'] = func_1898
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1930 = relay.var("var_1930", dtype = "uint32", shape = (13, 1, 1))#candidate|1930|(13, 1, 1)|var|uint32
var_1931 = relay.var("var_1931", dtype = "uint32", shape = (13, 1, 9))#candidate|1931|(13, 1, 9)|var|uint32
bop_1932 = relay.greater_equal(var_1930.astype('bool'), var_1931.astype('bool')) # shape=(13, 1, 9)
func_40_call = mod.get_global_var('func_40')
func_41_call = mutated_mod.get_global_var('func_41')
call_1945 = func_40_call()
call_1946 = func_40_call()
output = relay.Tuple([bop_1932,call_1945,])
output2 = relay.Tuple([bop_1932,call_1946,])
func_1967 = relay.Function([var_1930,var_1931,], output)
mod['func_1967'] = func_1967
mod = relay.transform.InferType()(mod)
mutated_mod['func_1967'] = func_1967
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1967_call = mutated_mod.get_global_var('func_1967')
var_1969 = relay.var("var_1969", dtype = "uint32", shape = (13, 1, 1))#candidate|1969|(13, 1, 1)|var|uint32
var_1970 = relay.var("var_1970", dtype = "uint32", shape = (13, 1, 9))#candidate|1970|(13, 1, 9)|var|uint32
call_1968 = func_1967_call(var_1969,var_1970,)
output = call_1968
func_1971 = relay.Function([var_1969,var_1970,], output)
mutated_mod['func_1971'] = func_1971
mutated_mod = relay.transform.InferType()(mutated_mod)
func_307_call = mod.get_global_var('func_307')
func_309_call = mutated_mod.get_global_var('func_309')
call_1983 = func_307_call()
call_1984 = func_307_call()
func_148_call = mod.get_global_var('func_148')
func_150_call = mutated_mod.get_global_var('func_150')
call_1985 = relay.TupleGetItem(func_148_call(), 0)
call_1986 = relay.TupleGetItem(func_150_call(), 0)
output = relay.Tuple([call_1983,call_1985,])
output2 = relay.Tuple([call_1984,call_1986,])
func_1993 = relay.Function([], output)
mod['func_1993'] = func_1993
mod = relay.transform.InferType()(mod)
output = func_1993()
func_1994 = relay.Function([], output)
mutated_mod['func_1994'] = func_1994
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1498_call = mod.get_global_var('func_1498')
func_1499_call = mutated_mod.get_global_var('func_1499')
call_2022 = relay.TupleGetItem(func_1498_call(), 1)
call_2023 = relay.TupleGetItem(func_1499_call(), 1)
func_1404_call = mod.get_global_var('func_1404')
func_1407_call = mutated_mod.get_global_var('func_1407')
var_2026 = relay.var("var_2026", dtype = "bool", shape = (56,))#candidate|2026|(56,)|var|bool
call_2025 = relay.TupleGetItem(func_1404_call(relay.reshape(var_2026.astype('bool'), [14, 1, 4])), 0)
call_2027 = relay.TupleGetItem(func_1407_call(relay.reshape(var_2026.astype('bool'), [14, 1, 4])), 0)
func_767_call = mod.get_global_var('func_767')
func_770_call = mutated_mod.get_global_var('func_770')
var_2029 = relay.var("var_2029", dtype = "float64", shape = (6,))#candidate|2029|(6,)|var|float64
call_2028 = func_767_call(relay.reshape(var_2029.astype('float64'), [3, 2]))
call_2030 = func_767_call(relay.reshape(var_2029.astype('float64'), [3, 2]))
func_767_call = mod.get_global_var('func_767')
func_770_call = mutated_mod.get_global_var('func_770')
call_2034 = func_767_call(relay.reshape(var_2029.astype('float64'), [3, 2]))
call_2035 = func_767_call(relay.reshape(var_2029.astype('float64'), [3, 2]))
output = relay.Tuple([call_2022,call_2025,var_2026,call_2028,var_2029,call_2034,])
output2 = relay.Tuple([call_2023,call_2027,var_2026,call_2030,var_2029,call_2035,])
func_2038 = relay.Function([var_2026,var_2029,], output)
mod['func_2038'] = func_2038
mod = relay.transform.InferType()(mod)
var_2039 = relay.var("var_2039", dtype = "bool", shape = (56,))#candidate|2039|(56,)|var|bool
var_2040 = relay.var("var_2040", dtype = "float64", shape = (6,))#candidate|2040|(6,)|var|float64
output = func_2038(var_2039,var_2040,)
func_2041 = relay.Function([var_2039,var_2040,], output)
mutated_mod['func_2041'] = func_2041
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1316_call = mod.get_global_var('func_1316')
func_1317_call = mutated_mod.get_global_var('func_1317')
call_2046 = func_1316_call()
call_2047 = func_1316_call()
output = relay.Tuple([call_2046,])
output2 = relay.Tuple([call_2047,])
func_2054 = relay.Function([], output)
mod['func_2054'] = func_2054
mod = relay.transform.InferType()(mod)
mutated_mod['func_2054'] = func_2054
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2054_call = mutated_mod.get_global_var('func_2054')
call_2055 = func_2054_call()
output = call_2055
func_2056 = relay.Function([], output)
mutated_mod['func_2056'] = func_2056
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2093 = relay.var("var_2093", dtype = "float32", shape = (14, 7, 13))#candidate|2093|(14, 7, 13)|var|float32
uop_2094 = relay.rsqrt(var_2093.astype('float32')) # shape=(14, 7, 13)
func_828_call = mod.get_global_var('func_828')
func_830_call = mutated_mod.get_global_var('func_830')
const_2098 = relay.const([[-5,-7,10,-9,-2,-7,-5,5,10,7,2,-3,-5,-9],[-10,1,2,4,-10,10,-3,-7,9,2,-3,-7,8,-9],[-9,-5,-3,-4,-6,4,3,-8,-4,7,-6,1,8,4],[5,1,4,-3,-4,-2,5,-6,2,5,8,-7,10,4],[5,-4,-3,-6,-2,-6,6,-7,-3,-9,7,-1,7,1],[-8,-5,-5,5,7,5,-2,6,-6,-1,5,6,-8,-7],[4,2,5,5,8,7,3,5,-2,7,3,9,-2,10],[-1,-4,-6,-7,8,2,3,-1,3,4,-8,-5,1,-9],[-8,-2,5,-4,-6,6,2,-10,-9,-3,-9,-8,-10,-8],[-9,-1,-5,6,8,-2,10,8,8,-8,9,9,-8,4],[4,-8,-8,-9,-1,2,-6,6,4,9,2,-9,9,-10],[9,-7,-6,5,4,-7,-9,-4,5,1,4,1,7,6],[2,-5,9,-3,6,9,1,3,-6,5,9,-1,7,-8],[6,2,-7,8,-10,-1,10,-4,-5,-3,8,-2,-5,1],[-7,-4,-10,-10,5,4,-2,10,6,-4,-5,-2,4,-9],[9,9,-8,10,3,-6,1,-2,7,-4,7,4,7,-4],[-3,10,-2,9,-5,-9,-10,-5,-7,1,-10,-8,5,9],[-1,-2,6,6,4,10,-4,-8,-4,-3,-1,-6,1,7],[8,-7,9,-3,5,2,3,-7,-3,-9,-9,9,-7,10],[-10,4,-3,7,4,6,9,7,2,-1,10,-1,4,-10],[4,9,-6,-4,-7,2,2,9,6,5,1,-2,-6,1],[-2,1,10,1,-6,-7,-5,4,-5,-1,8,-10,2,9],[4,7,8,5,1,-4,-3,10,9,7,5,-6,2,2],[-5,-1,1,-8,-10,-9,-1,8,3,1,-1,8,4,1]], dtype = "int16")#candidate|2098|(24, 14)|const|int16
call_2097 = func_828_call(relay.reshape(const_2098.astype('int16'), [14, 6, 4]))
call_2099 = func_828_call(relay.reshape(const_2098.astype('int16'), [14, 6, 4]))
func_1316_call = mod.get_global_var('func_1316')
func_1317_call = mutated_mod.get_global_var('func_1317')
call_2104 = func_1316_call()
call_2105 = func_1316_call()
func_1498_call = mod.get_global_var('func_1498')
func_1499_call = mutated_mod.get_global_var('func_1499')
call_2108 = relay.TupleGetItem(func_1498_call(), 0)
call_2109 = relay.TupleGetItem(func_1499_call(), 0)
func_1246_call = mod.get_global_var('func_1246')
func_1250_call = mutated_mod.get_global_var('func_1250')
var_2120 = relay.var("var_2120", dtype = "float64", shape = (1, 6))#candidate|2120|(1, 6)|var|float64
var_2121 = relay.var("var_2121", dtype = "float32", shape = (192,))#candidate|2121|(192,)|var|float32
call_2119 = relay.TupleGetItem(func_1246_call(relay.reshape(var_2120.astype('float64'), [6,]), relay.reshape(var_2121.astype('float32'), [192,]), ), 13)
call_2122 = relay.TupleGetItem(func_1250_call(relay.reshape(var_2120.astype('float64'), [6,]), relay.reshape(var_2121.astype('float32'), [192,]), ), 13)
output = relay.Tuple([uop_2094,call_2097,const_2098,call_2104,call_2108,call_2119,var_2120,var_2121,])
output2 = relay.Tuple([uop_2094,call_2099,const_2098,call_2105,call_2109,call_2122,var_2120,var_2121,])
func_2130 = relay.Function([var_2093,var_2120,var_2121,], output)
mod['func_2130'] = func_2130
mod = relay.transform.InferType()(mod)
mutated_mod['func_2130'] = func_2130
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2130_call = mutated_mod.get_global_var('func_2130')
var_2132 = relay.var("var_2132", dtype = "float32", shape = (14, 7, 13))#candidate|2132|(14, 7, 13)|var|float32
var_2133 = relay.var("var_2133", dtype = "float64", shape = (1, 6))#candidate|2133|(1, 6)|var|float64
var_2134 = relay.var("var_2134", dtype = "float32", shape = (192,))#candidate|2134|(192,)|var|float32
call_2131 = func_2130_call(var_2132,var_2133,var_2134,)
output = call_2131
func_2135 = relay.Function([var_2132,var_2133,var_2134,], output)
mutated_mod['func_2135'] = func_2135
mutated_mod = relay.transform.InferType()(mutated_mod)
func_858_call = mod.get_global_var('func_858')
func_859_call = mutated_mod.get_global_var('func_859')
call_2161 = relay.TupleGetItem(func_858_call(), 0)
call_2162 = relay.TupleGetItem(func_859_call(), 0)
func_148_call = mod.get_global_var('func_148')
func_150_call = mutated_mod.get_global_var('func_150')
call_2182 = relay.TupleGetItem(func_148_call(), 0)
call_2183 = relay.TupleGetItem(func_150_call(), 0)
func_1531_call = mod.get_global_var('func_1531')
func_1533_call = mutated_mod.get_global_var('func_1533')
call_2201 = relay.TupleGetItem(func_1531_call(), 0)
call_2202 = relay.TupleGetItem(func_1533_call(), 0)
func_40_call = mod.get_global_var('func_40')
func_41_call = mutated_mod.get_global_var('func_41')
call_2215 = func_40_call()
call_2216 = func_40_call()
output = relay.Tuple([call_2161,call_2182,call_2201,call_2215,])
output2 = relay.Tuple([call_2162,call_2183,call_2202,call_2216,])
func_2218 = relay.Function([], output)
mod['func_2218'] = func_2218
mod = relay.transform.InferType()(mod)
output = func_2218()
func_2219 = relay.Function([], output)
mutated_mod['func_2219'] = func_2219
mutated_mod = relay.transform.InferType()(mutated_mod)
func_557_call = mod.get_global_var('func_557')
func_558_call = mutated_mod.get_global_var('func_558')
call_2267 = relay.TupleGetItem(func_557_call(), 1)
call_2268 = relay.TupleGetItem(func_558_call(), 1)
output = relay.Tuple([call_2267,])
output2 = relay.Tuple([call_2268,])
func_2294 = relay.Function([], output)
mod['func_2294'] = func_2294
mod = relay.transform.InferType()(mod)
output = func_2294()
func_2295 = relay.Function([], output)
mutated_mod['func_2295'] = func_2295
mutated_mod = relay.transform.InferType()(mutated_mod)
func_148_call = mod.get_global_var('func_148')
func_150_call = mutated_mod.get_global_var('func_150')
call_2341 = relay.TupleGetItem(func_148_call(), 0)
call_2342 = relay.TupleGetItem(func_150_call(), 0)
func_2054_call = mod.get_global_var('func_2054')
func_2056_call = mutated_mod.get_global_var('func_2056')
call_2376 = relay.TupleGetItem(func_2054_call(), 0)
call_2377 = relay.TupleGetItem(func_2056_call(), 0)
output = relay.Tuple([call_2341,call_2376,])
output2 = relay.Tuple([call_2342,call_2377,])
func_2380 = relay.Function([], output)
mod['func_2380'] = func_2380
mod = relay.transform.InferType()(mod)
mutated_mod['func_2380'] = func_2380
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2380_call = mutated_mod.get_global_var('func_2380')
call_2381 = func_2380_call()
output = call_2381
func_2382 = relay.Function([], output)
mutated_mod['func_2382'] = func_2382
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1896_call = mod.get_global_var('func_1896')
func_1898_call = mutated_mod.get_global_var('func_1898')
call_2388 = relay.TupleGetItem(func_1896_call(), 0)
call_2389 = relay.TupleGetItem(func_1898_call(), 0)
func_1823_call = mod.get_global_var('func_1823')
func_1825_call = mutated_mod.get_global_var('func_1825')
call_2395 = relay.TupleGetItem(func_1823_call(), 2)
call_2396 = relay.TupleGetItem(func_1825_call(), 2)
output = relay.Tuple([call_2388,call_2395,])
output2 = relay.Tuple([call_2389,call_2396,])
func_2457 = relay.Function([], output)
mod['func_2457'] = func_2457
mod = relay.transform.InferType()(mod)
output = func_2457()
func_2458 = relay.Function([], output)
mutated_mod['func_2458'] = func_2458
mutated_mod = relay.transform.InferType()(mutated_mod)
func_40_call = mod.get_global_var('func_40')
func_41_call = mutated_mod.get_global_var('func_41')
call_2461 = func_40_call()
call_2462 = func_40_call()
output = relay.Tuple([call_2461,])
output2 = relay.Tuple([call_2462,])
func_2466 = relay.Function([], output)
mod['func_2466'] = func_2466
mod = relay.transform.InferType()(mod)
mutated_mod['func_2466'] = func_2466
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2466_call = mutated_mod.get_global_var('func_2466')
call_2467 = func_2466_call()
output = call_2467
func_2468 = relay.Function([], output)
mutated_mod['func_2468'] = func_2468
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2294_call = mod.get_global_var('func_2294')
func_2295_call = mutated_mod.get_global_var('func_2295')
call_2529 = relay.TupleGetItem(func_2294_call(), 0)
call_2530 = relay.TupleGetItem(func_2295_call(), 0)
func_767_call = mod.get_global_var('func_767')
func_770_call = mutated_mod.get_global_var('func_770')
var_2536 = relay.var("var_2536", dtype = "float64", shape = (6,))#candidate|2536|(6,)|var|float64
call_2535 = func_767_call(relay.reshape(var_2536.astype('float64'), [3, 2]))
call_2537 = func_767_call(relay.reshape(var_2536.astype('float64'), [3, 2]))
output = relay.Tuple([call_2529,call_2535,var_2536,])
output2 = relay.Tuple([call_2530,call_2537,var_2536,])
func_2552 = relay.Function([var_2536,], output)
mod['func_2552'] = func_2552
mod = relay.transform.InferType()(mod)
var_2553 = relay.var("var_2553", dtype = "float64", shape = (6,))#candidate|2553|(6,)|var|float64
output = func_2552(var_2553)
func_2554 = relay.Function([var_2553], output)
mutated_mod['func_2554'] = func_2554
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1452_call = mod.get_global_var('func_1452')
func_1453_call = mutated_mod.get_global_var('func_1453')
call_2568 = func_1452_call()
call_2569 = func_1452_call()
output = relay.Tuple([call_2568,])
output2 = relay.Tuple([call_2569,])
func_2584 = relay.Function([], output)
mod['func_2584'] = func_2584
mod = relay.transform.InferType()(mod)
output = func_2584()
func_2585 = relay.Function([], output)
mutated_mod['func_2585'] = func_2585
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1674_call = mod.get_global_var('func_1674')
func_1676_call = mutated_mod.get_global_var('func_1676')
call_2604 = relay.TupleGetItem(func_1674_call(), 0)
call_2605 = relay.TupleGetItem(func_1676_call(), 0)
output = relay.Tuple([call_2604,])
output2 = relay.Tuple([call_2605,])
func_2606 = relay.Function([], output)
mod['func_2606'] = func_2606
mod = relay.transform.InferType()(mod)
mutated_mod['func_2606'] = func_2606
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2606_call = mutated_mod.get_global_var('func_2606')
call_2607 = func_2606_call()
output = call_2607
func_2608 = relay.Function([], output)
mutated_mod['func_2608'] = func_2608
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2054_call = mod.get_global_var('func_2054')
func_2056_call = mutated_mod.get_global_var('func_2056')
call_2628 = relay.TupleGetItem(func_2054_call(), 0)
call_2629 = relay.TupleGetItem(func_2056_call(), 0)
var_2632 = relay.var("var_2632", dtype = "float64", shape = (3, 4, 8))#candidate|2632|(3, 4, 8)|var|float64
bop_2633 = relay.right_shift(call_2628.astype('int8'), relay.reshape(var_2632.astype('int8'), relay.shape_of(call_2628))) # shape=(3, 4, 8)
bop_2636 = relay.right_shift(call_2629.astype('int8'), relay.reshape(var_2632.astype('int8'), relay.shape_of(call_2629))) # shape=(3, 4, 8)
func_2552_call = mod.get_global_var('func_2552')
func_2554_call = mutated_mod.get_global_var('func_2554')
var_2646 = relay.var("var_2646", dtype = "float64", shape = (3, 2))#candidate|2646|(3, 2)|var|float64
call_2645 = relay.TupleGetItem(func_2552_call(relay.reshape(var_2646.astype('float64'), [6,])), 0)
call_2647 = relay.TupleGetItem(func_2554_call(relay.reshape(var_2646.astype('float64'), [6,])), 0)
func_984_call = mod.get_global_var('func_984')
func_986_call = mutated_mod.get_global_var('func_986')
call_2653 = relay.TupleGetItem(func_984_call(), 5)
call_2654 = relay.TupleGetItem(func_986_call(), 5)
output = relay.Tuple([bop_2633,call_2645,var_2646,call_2653,])
output2 = relay.Tuple([bop_2636,call_2647,var_2646,call_2654,])
func_2655 = relay.Function([var_2632,var_2646,], output)
mod['func_2655'] = func_2655
mod = relay.transform.InferType()(mod)
var_2656 = relay.var("var_2656", dtype = "float64", shape = (3, 4, 8))#candidate|2656|(3, 4, 8)|var|float64
var_2657 = relay.var("var_2657", dtype = "float64", shape = (3, 2))#candidate|2657|(3, 2)|var|float64
output = func_2655(var_2656,var_2657,)
func_2658 = relay.Function([var_2656,var_2657,], output)
mutated_mod['func_2658'] = func_2658
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1498_call = mod.get_global_var('func_1498')
func_1499_call = mutated_mod.get_global_var('func_1499')
call_2703 = relay.TupleGetItem(func_1498_call(), 1)
call_2704 = relay.TupleGetItem(func_1499_call(), 1)
func_1823_call = mod.get_global_var('func_1823')
func_1825_call = mutated_mod.get_global_var('func_1825')
call_2713 = relay.TupleGetItem(func_1823_call(), 1)
call_2714 = relay.TupleGetItem(func_1825_call(), 1)
output = relay.Tuple([call_2703,call_2713,])
output2 = relay.Tuple([call_2704,call_2714,])
func_2716 = relay.Function([], output)
mod['func_2716'] = func_2716
mod = relay.transform.InferType()(mod)
output = func_2716()
func_2717 = relay.Function([], output)
mutated_mod['func_2717'] = func_2717
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2584_call = mod.get_global_var('func_2584')
func_2585_call = mutated_mod.get_global_var('func_2585')
call_2739 = relay.TupleGetItem(func_2584_call(), 0)
call_2740 = relay.TupleGetItem(func_2585_call(), 0)
func_2380_call = mod.get_global_var('func_2380')
func_2382_call = mutated_mod.get_global_var('func_2382')
call_2755 = relay.TupleGetItem(func_2380_call(), 1)
call_2756 = relay.TupleGetItem(func_2382_call(), 1)
output = relay.Tuple([call_2739,call_2755,])
output2 = relay.Tuple([call_2740,call_2756,])
func_2757 = relay.Function([], output)
mod['func_2757'] = func_2757
mod = relay.transform.InferType()(mod)
mutated_mod['func_2757'] = func_2757
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2757_call = mutated_mod.get_global_var('func_2757')
call_2758 = func_2757_call()
output = call_2758
func_2759 = relay.Function([], output)
mutated_mod['func_2759'] = func_2759
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1823_call = mod.get_global_var('func_1823')
func_1825_call = mutated_mod.get_global_var('func_1825')
call_2791 = relay.TupleGetItem(func_1823_call(), 1)
call_2792 = relay.TupleGetItem(func_1825_call(), 1)
output = call_2791
output2 = call_2792
func_2793 = relay.Function([], output)
mod['func_2793'] = func_2793
mod = relay.transform.InferType()(mod)
output = func_2793()
func_2794 = relay.Function([], output)
mutated_mod['func_2794'] = func_2794
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1896_call = mod.get_global_var('func_1896')
func_1898_call = mutated_mod.get_global_var('func_1898')
call_2813 = relay.TupleGetItem(func_1896_call(), 0)
call_2814 = relay.TupleGetItem(func_1898_call(), 0)
output = call_2813
output2 = call_2814
func_2827 = relay.Function([], output)
mod['func_2827'] = func_2827
mod = relay.transform.InferType()(mod)
output = func_2827()
func_2828 = relay.Function([], output)
mutated_mod['func_2828'] = func_2828
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2294_call = mod.get_global_var('func_2294')
func_2295_call = mutated_mod.get_global_var('func_2295')
call_2855 = relay.TupleGetItem(func_2294_call(), 0)
call_2856 = relay.TupleGetItem(func_2295_call(), 0)
func_916_call = mod.get_global_var('func_916')
func_918_call = mutated_mod.get_global_var('func_918')
const_2863 = relay.const(True, dtype = "bool")#candidate|2863|()|const|bool
call_2862 = relay.TupleGetItem(func_916_call(relay.reshape(const_2863.astype('bool'), [])), 2)
call_2864 = relay.TupleGetItem(func_918_call(relay.reshape(const_2863.astype('bool'), [])), 2)
bop_2877 = relay.less(call_2862.astype('bool'), const_2863.astype('bool')) # shape=(6, 6, 13)
bop_2880 = relay.less(call_2864.astype('bool'), const_2863.astype('bool')) # shape=(6, 6, 13)
func_1896_call = mod.get_global_var('func_1896')
func_1898_call = mutated_mod.get_global_var('func_1898')
call_2884 = relay.TupleGetItem(func_1896_call(), 0)
call_2885 = relay.TupleGetItem(func_1898_call(), 0)
func_1674_call = mod.get_global_var('func_1674')
func_1676_call = mutated_mod.get_global_var('func_1676')
call_2887 = relay.TupleGetItem(func_1674_call(), 0)
call_2888 = relay.TupleGetItem(func_1676_call(), 0)
output = relay.Tuple([call_2855,bop_2877,call_2884,call_2887,])
output2 = relay.Tuple([call_2856,bop_2880,call_2885,call_2888,])
func_2891 = relay.Function([], output)
mod['func_2891'] = func_2891
mod = relay.transform.InferType()(mod)
output = func_2891()
func_2892 = relay.Function([], output)
mutated_mod['func_2892'] = func_2892
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1896_call = mod.get_global_var('func_1896')
func_1898_call = mutated_mod.get_global_var('func_1898')
call_2999 = relay.TupleGetItem(func_1896_call(), 0)
call_3000 = relay.TupleGetItem(func_1898_call(), 0)
output = call_2999
output2 = call_3000
func_3008 = relay.Function([], output)
mod['func_3008'] = func_3008
mod = relay.transform.InferType()(mod)
output = func_3008()
func_3009 = relay.Function([], output)
mutated_mod['func_3009'] = func_3009
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2757_call = mod.get_global_var('func_2757')
func_2759_call = mutated_mod.get_global_var('func_2759')
call_3039 = relay.TupleGetItem(func_2757_call(), 1)
call_3040 = relay.TupleGetItem(func_2759_call(), 1)
output = relay.Tuple([call_3039,])
output2 = relay.Tuple([call_3040,])
func_3043 = relay.Function([], output)
mod['func_3043'] = func_3043
mod = relay.transform.InferType()(mod)
mutated_mod['func_3043'] = func_3043
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3043_call = mutated_mod.get_global_var('func_3043')
call_3044 = func_3043_call()
output = call_3044
func_3045 = relay.Function([], output)
mutated_mod['func_3045'] = func_3045
mutated_mod = relay.transform.InferType()(mutated_mod)
func_858_call = mod.get_global_var('func_858')
func_859_call = mutated_mod.get_global_var('func_859')
call_3100 = relay.TupleGetItem(func_858_call(), 1)
call_3101 = relay.TupleGetItem(func_859_call(), 1)
output = relay.Tuple([call_3100,])
output2 = relay.Tuple([call_3101,])
func_3111 = relay.Function([], output)
mod['func_3111'] = func_3111
mod = relay.transform.InferType()(mod)
output = func_3111()
func_3112 = relay.Function([], output)
mutated_mod['func_3112'] = func_3112
mutated_mod = relay.transform.InferType()(mutated_mod)
func_148_call = mod.get_global_var('func_148')
func_150_call = mutated_mod.get_global_var('func_150')
call_3129 = relay.TupleGetItem(func_148_call(), 1)
call_3130 = relay.TupleGetItem(func_150_call(), 1)
output = call_3129
output2 = call_3130
func_3134 = relay.Function([], output)
mod['func_3134'] = func_3134
mod = relay.transform.InferType()(mod)
mutated_mod['func_3134'] = func_3134
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3134_call = mutated_mod.get_global_var('func_3134')
call_3135 = func_3134_call()
output = call_3135
func_3136 = relay.Function([], output)
mutated_mod['func_3136'] = func_3136
mutated_mod = relay.transform.InferType()(mutated_mod)
func_40_call = mod.get_global_var('func_40')
func_41_call = mutated_mod.get_global_var('func_41')
call_3187 = func_40_call()
call_3188 = func_40_call()
func_2827_call = mod.get_global_var('func_2827')
func_2828_call = mutated_mod.get_global_var('func_2828')
call_3216 = func_2827_call()
call_3217 = func_2827_call()
func_1531_call = mod.get_global_var('func_1531')
func_1533_call = mutated_mod.get_global_var('func_1533')
call_3218 = relay.TupleGetItem(func_1531_call(), 0)
call_3219 = relay.TupleGetItem(func_1533_call(), 0)
output = relay.Tuple([call_3187,call_3216,call_3218,])
output2 = relay.Tuple([call_3188,call_3217,call_3219,])
func_3234 = relay.Function([], output)
mod['func_3234'] = func_3234
mod = relay.transform.InferType()(mod)
output = func_3234()
func_3235 = relay.Function([], output)
mutated_mod['func_3235'] = func_3235
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2054_call = mod.get_global_var('func_2054')
func_2056_call = mutated_mod.get_global_var('func_2056')
call_3292 = relay.TupleGetItem(func_2054_call(), 0)
call_3293 = relay.TupleGetItem(func_2056_call(), 0)
func_1865_call = mod.get_global_var('func_1865')
func_1867_call = mutated_mod.get_global_var('func_1867')
const_3295 = relay.const([9.399524,-4.033941,-6.029519,6.227550,-6.706421,5.694515,1.974781,-5.893944,8.139671,-0.550986,-9.517966,-7.336002,-4.579186,1.681460,-5.818999,-1.577410,7.816699,-1.568502,-7.137735,2.165340,-7.360573,-8.310516,-0.169350,-3.253827,-2.489953,-7.652611,-9.540379,3.742030,7.405303,-4.733058,6.491596,3.574461,-9.999096,-3.854001,-8.397042,2.290085,-5.291321,-6.559676,-5.459503,3.167389,-8.082202,-2.192653,-2.224112,4.186516,-7.053565,4.239841,-1.657630,-8.632544,6.141030,-1.173484,-2.705707,-8.712268,9.224896,9.805315,5.635110,-4.597184,-2.090914,7.985882,-8.274297,2.244025,-8.373178,-2.435223,5.331912,2.199858,2.989628,-4.299366,0.759914,6.016533,-3.775982,6.526594,6.817549,2.629542,-1.315450,-6.987182,2.274038,9.319447,-5.506924,3.597195,-8.653333,-1.503596,-2.770743,-1.768479,4.111884,-3.064921,-4.363039,-8.846718,4.017879,-3.164371,-0.385039,3.562136,-6.469272,2.639938,-6.031936,-3.889582,-5.914601,4.116343,-6.018794,-3.430316,0.990141,5.111581,-2.741859,8.134303,6.597055,1.768183,-1.230775,9.750003,8.443291,4.237102,8.956801,6.908221,2.027573,-4.399749,-6.774898,9.929534,7.152146,9.816980,-4.876987,-0.987357,-4.237062,7.642016,-0.671639,8.105692,-8.551891,1.072052,7.977312,2.492193,3.440729,-5.152863,-4.228566,4.688169,-9.218711,-7.683922,0.411154,-5.760198,-8.605304,-5.639352,-6.328268,2.510850,8.427797,1.796003,7.575725,2.459315,-4.474768,-8.031742,5.432606,2.072079,-8.924465,3.636380,-2.558270,-3.109103,9.043773,0.455620,-5.943457,-0.763745,9.217651,-4.384152,-4.710864,-0.320259,2.171574,-2.839324,-3.166631,-5.261216,7.858940,3.569339,7.384621,-8.310619,-6.836293,4.612121,-7.253416,-8.229142,2.718287,-2.058716,-8.491883,-1.525933,8.792508,0.429490,-2.106551,7.626976,8.033292,2.104076,-8.645453,8.499305,2.313101,0.959260,7.562424,-0.347120,1.472825,-0.570354,3.811367,4.119840,8.203273,-6.870123], dtype = "float32")#candidate|3295|(192,)|const|float32
call_3294 = relay.TupleGetItem(func_1865_call(relay.reshape(const_3295.astype('float32'), [192, 1])), 5)
call_3296 = relay.TupleGetItem(func_1867_call(relay.reshape(const_3295.astype('float32'), [192, 1])), 5)
func_322_call = mod.get_global_var('func_322')
func_323_call = mutated_mod.get_global_var('func_323')
call_3300 = relay.TupleGetItem(func_322_call(), 0)
call_3301 = relay.TupleGetItem(func_323_call(), 0)
output = relay.Tuple([call_3292,call_3294,const_3295,call_3300,])
output2 = relay.Tuple([call_3293,call_3296,const_3295,call_3301,])
func_3302 = relay.Function([], output)
mod['func_3302'] = func_3302
mod = relay.transform.InferType()(mod)
mutated_mod['func_3302'] = func_3302
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3302_call = mutated_mod.get_global_var('func_3302')
call_3303 = func_3302_call()
output = call_3303
func_3304 = relay.Function([], output)
mutated_mod['func_3304'] = func_3304
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3308 = relay.var("var_3308", dtype = "float32", shape = (6, 6, 9))#candidate|3308|(6, 6, 9)|var|float32
uop_3309 = relay.tan(var_3308.astype('float32')) # shape=(6, 6, 9)
bop_3315 = relay.power(uop_3309.astype('float64'), relay.reshape(var_3308.astype('float64'), relay.shape_of(uop_3309))) # shape=(6, 6, 9)
bop_3318 = relay.bitwise_xor(bop_3315.astype('uint8'), relay.reshape(var_3308.astype('uint8'), relay.shape_of(bop_3315))) # shape=(6, 6, 9)
func_2457_call = mod.get_global_var('func_2457')
func_2458_call = mutated_mod.get_global_var('func_2458')
call_3336 = relay.TupleGetItem(func_2457_call(), 0)
call_3337 = relay.TupleGetItem(func_2458_call(), 0)
output = relay.Tuple([bop_3318,call_3336,])
output2 = relay.Tuple([bop_3318,call_3337,])
func_3345 = relay.Function([var_3308,], output)
mod['func_3345'] = func_3345
mod = relay.transform.InferType()(mod)
mutated_mod['func_3345'] = func_3345
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3346 = relay.var("var_3346", dtype = "float32", shape = (6, 6, 9))#candidate|3346|(6, 6, 9)|var|float32
func_3345_call = mutated_mod.get_global_var('func_3345')
call_3347 = func_3345_call(var_3346)
output = call_3347
func_3348 = relay.Function([var_3346], output)
mutated_mod['func_3348'] = func_3348
mutated_mod = relay.transform.InferType()(mutated_mod)
func_257_call = mod.get_global_var('func_257')
func_259_call = mutated_mod.get_global_var('func_259')
call_3359 = relay.TupleGetItem(func_257_call(), 1)
call_3360 = relay.TupleGetItem(func_259_call(), 1)
func_1498_call = mod.get_global_var('func_1498')
func_1499_call = mutated_mod.get_global_var('func_1499')
call_3382 = relay.TupleGetItem(func_1498_call(), 1)
call_3383 = relay.TupleGetItem(func_1499_call(), 1)
func_3302_call = mod.get_global_var('func_3302')
func_3304_call = mutated_mod.get_global_var('func_3304')
call_3390 = relay.TupleGetItem(func_3302_call(), 1)
call_3391 = relay.TupleGetItem(func_3304_call(), 1)
func_858_call = mod.get_global_var('func_858')
func_859_call = mutated_mod.get_global_var('func_859')
call_3395 = relay.TupleGetItem(func_858_call(), 0)
call_3396 = relay.TupleGetItem(func_859_call(), 0)
func_322_call = mod.get_global_var('func_322')
func_323_call = mutated_mod.get_global_var('func_323')
call_3397 = relay.TupleGetItem(func_322_call(), 0)
call_3398 = relay.TupleGetItem(func_323_call(), 0)
output = relay.Tuple([call_3359,call_3382,call_3390,call_3395,call_3397,])
output2 = relay.Tuple([call_3360,call_3383,call_3391,call_3396,call_3398,])
func_3403 = relay.Function([], output)
mod['func_3403'] = func_3403
mod = relay.transform.InferType()(mod)
output = func_3403()
func_3404 = relay.Function([], output)
mutated_mod['func_3404'] = func_3404
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3416 = relay.var("var_3416", dtype = "float32", shape = (5, 15, 2))#candidate|3416|(5, 15, 2)|var|float32
var_3417 = relay.var("var_3417", dtype = "float32", shape = (5, 15, 2))#candidate|3417|(5, 15, 2)|var|float32
bop_3418 = relay.minimum(var_3416.astype('float32'), relay.reshape(var_3417.astype('float32'), relay.shape_of(var_3416))) # shape=(5, 15, 2)
uop_3424 = relay.log2(bop_3418.astype('float32')) # shape=(5, 15, 2)
output = uop_3424
output2 = uop_3424
func_3430 = relay.Function([var_3416,var_3417,], output)
mod['func_3430'] = func_3430
mod = relay.transform.InferType()(mod)
mutated_mod['func_3430'] = func_3430
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3430_call = mutated_mod.get_global_var('func_3430')
var_3432 = relay.var("var_3432", dtype = "float32", shape = (5, 15, 2))#candidate|3432|(5, 15, 2)|var|float32
var_3433 = relay.var("var_3433", dtype = "float32", shape = (5, 15, 2))#candidate|3433|(5, 15, 2)|var|float32
call_3431 = func_3430_call(var_3432,var_3433,)
output = call_3431
func_3434 = relay.Function([var_3432,var_3433,], output)
mutated_mod['func_3434'] = func_3434
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2294_call = mod.get_global_var('func_2294')
func_2295_call = mutated_mod.get_global_var('func_2295')
call_3495 = relay.TupleGetItem(func_2294_call(), 0)
call_3496 = relay.TupleGetItem(func_2295_call(), 0)
output = call_3495
output2 = call_3496
func_3546 = relay.Function([], output)
mod['func_3546'] = func_3546
mod = relay.transform.InferType()(mod)
output = func_3546()
func_3547 = relay.Function([], output)
mutated_mod['func_3547'] = func_3547
mutated_mod = relay.transform.InferType()(mutated_mod)
func_858_call = mod.get_global_var('func_858')
func_859_call = mutated_mod.get_global_var('func_859')
call_3567 = relay.TupleGetItem(func_858_call(), 0)
call_3568 = relay.TupleGetItem(func_859_call(), 0)
output = call_3567
output2 = call_3568
func_3588 = relay.Function([], output)
mod['func_3588'] = func_3588
mod = relay.transform.InferType()(mod)
mutated_mod['func_3588'] = func_3588
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3588_call = mutated_mod.get_global_var('func_3588')
call_3589 = func_3588_call()
output = call_3589
func_3590 = relay.Function([], output)
mutated_mod['func_3590'] = func_3590
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3134_call = mod.get_global_var('func_3134')
func_3136_call = mutated_mod.get_global_var('func_3136')
call_3672 = func_3134_call()
call_3673 = func_3134_call()
output = call_3672
output2 = call_3673
func_3709 = relay.Function([], output)
mod['func_3709'] = func_3709
mod = relay.transform.InferType()(mod)
mutated_mod['func_3709'] = func_3709
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3709_call = mutated_mod.get_global_var('func_3709')
call_3710 = func_3709_call()
output = call_3710
func_3711 = relay.Function([], output)
mutated_mod['func_3711'] = func_3711
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3709_call = mod.get_global_var('func_3709')
func_3711_call = mutated_mod.get_global_var('func_3711')
call_3747 = func_3709_call()
call_3748 = func_3709_call()
output = relay.Tuple([call_3747,])
output2 = relay.Tuple([call_3748,])
func_3765 = relay.Function([], output)
mod['func_3765'] = func_3765
mod = relay.transform.InferType()(mod)
mutated_mod['func_3765'] = func_3765
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3765_call = mutated_mod.get_global_var('func_3765')
call_3766 = func_3765_call()
output = call_3766
func_3767 = relay.Function([], output)
mutated_mod['func_3767'] = func_3767
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3043_call = mod.get_global_var('func_3043')
func_3045_call = mutated_mod.get_global_var('func_3045')
call_3836 = relay.TupleGetItem(func_3043_call(), 0)
call_3837 = relay.TupleGetItem(func_3045_call(), 0)
func_3134_call = mod.get_global_var('func_3134')
func_3136_call = mutated_mod.get_global_var('func_3136')
call_3840 = func_3134_call()
call_3841 = func_3134_call()
func_257_call = mod.get_global_var('func_257')
func_259_call = mutated_mod.get_global_var('func_259')
call_3850 = relay.TupleGetItem(func_257_call(), 1)
call_3851 = relay.TupleGetItem(func_259_call(), 1)
func_2552_call = mod.get_global_var('func_2552')
func_2554_call = mutated_mod.get_global_var('func_2554')
var_3860 = relay.var("var_3860", dtype = "float64", shape = (6,))#candidate|3860|(6,)|var|float64
call_3859 = relay.TupleGetItem(func_2552_call(relay.reshape(var_3860.astype('float64'), [6,])), 2)
call_3861 = relay.TupleGetItem(func_2554_call(relay.reshape(var_3860.astype('float64'), [6,])), 2)
output = relay.Tuple([call_3836,call_3840,call_3850,call_3859,var_3860,])
output2 = relay.Tuple([call_3837,call_3841,call_3851,call_3861,var_3860,])
func_3865 = relay.Function([var_3860,], output)
mod['func_3865'] = func_3865
mod = relay.transform.InferType()(mod)
var_3866 = relay.var("var_3866", dtype = "float64", shape = (6,))#candidate|3866|(6,)|var|float64
output = func_3865(var_3866)
func_3867 = relay.Function([var_3866], output)
mutated_mod['func_3867'] = func_3867
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3872 = relay.const([[[-1.516616,-0.116344,-1.628133,9.216371,-7.916520,8.689442],[-7.598463,9.276088,-0.563197,-7.408962,9.867242,-9.037223],[4.580585,8.197268,-9.253138,0.177941,1.561916,-2.475798]],[[-0.565662,2.319686,9.344218,5.678853,9.880315,0.607898],[1.834145,-0.523830,-2.475155,9.294136,-9.328053,8.049421],[-7.640134,5.186557,0.041794,7.745694,4.759306,-4.359568]],[[2.862668,-1.861908,7.599387,-0.748778,2.288601,8.941145],[0.599738,-2.544780,4.326888,9.244865,-6.713811,2.478807],[-5.094391,6.980131,9.765885,-5.232228,0.560451,-6.776678]],[[-6.102513,4.952615,1.959484,1.116472,-0.386520,-9.111088],[-7.711199,0.272601,-4.723146,-9.080458,8.875807,-1.249897],[1.624944,2.661094,8.272259,9.302597,-4.279538,-8.778151]],[[8.927741,7.006018,8.912681,0.742858,1.967506,-1.671242],[8.863438,-9.134180,-6.994783,-8.239479,9.360013,-9.986900],[5.164022,-5.068054,6.113376,2.083018,-5.666599,-2.198196]],[[-3.068555,6.926140,-5.981479,7.498803,-5.537931,-3.744497],[-0.408865,0.778416,-4.504209,-1.446975,7.220640,5.676225],[2.145822,-9.828985,4.350464,4.770248,-5.521340,5.672623]],[[-3.672226,5.427465,-9.465024,3.710001,-6.373537,-0.484465],[5.435351,-0.130196,4.838772,0.740200,-7.667472,6.202637],[-8.043851,3.296479,0.892742,7.182229,3.045446,2.880934]],[[-8.873525,-8.206143,4.011254,4.228146,1.572528,5.702880],[2.619024,-3.413888,-2.323822,-7.061332,-9.479871,-5.333240],[-1.613066,-6.087385,-4.008812,-4.703136,-1.486380,8.060895]],[[6.259162,-4.821446,-5.632622,-4.100830,-4.973449,8.290962],[-9.783343,6.043459,4.276421,-5.118999,6.306944,1.267014],[-9.806173,-3.409359,-6.473777,-7.199447,-5.372721,-0.803488]],[[1.453659,0.884978,4.273016,-3.477250,-1.599255,4.475935],[9.924938,1.512957,-6.589253,-2.741777,-2.167700,4.596611],[-8.185246,0.570845,0.383184,6.054260,-9.735274,-8.778079]],[[8.224050,7.068835,6.976156,5.695861,-2.024492,8.488623],[6.288139,-8.347754,3.344457,-5.574044,1.162898,-2.518833],[-2.760280,5.692348,-2.237314,-4.785042,1.522172,5.544512]]], dtype = "float64")#candidate|3872|(11, 3, 6)|const|float64
uop_3873 = relay.sin(const_3872.astype('float64')) # shape=(11, 3, 6)
uop_3875 = relay.rsqrt(const_3872.astype('float32')) # shape=(11, 3, 6)
output = relay.Tuple([uop_3873,uop_3875,])
output2 = relay.Tuple([uop_3873,uop_3875,])
func_3878 = relay.Function([], output)
mod['func_3878'] = func_3878
mod = relay.transform.InferType()(mod)
mutated_mod['func_3878'] = func_3878
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3878_call = mutated_mod.get_global_var('func_3878')
call_3879 = func_3878_call()
output = call_3879
func_3880 = relay.Function([], output)
mutated_mod['func_3880'] = func_3880
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3008_call = mod.get_global_var('func_3008')
func_3009_call = mutated_mod.get_global_var('func_3009')
call_3913 = func_3008_call()
call_3914 = func_3008_call()
output = call_3913
output2 = call_3914
func_3932 = relay.Function([], output)
mod['func_3932'] = func_3932
mod = relay.transform.InferType()(mod)
mutated_mod['func_3932'] = func_3932
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3932_call = mutated_mod.get_global_var('func_3932')
call_3933 = func_3932_call()
output = call_3933
func_3934 = relay.Function([], output)
mutated_mod['func_3934'] = func_3934
mutated_mod = relay.transform.InferType()(mutated_mod)
func_557_call = mod.get_global_var('func_557')
func_558_call = mutated_mod.get_global_var('func_558')
call_3994 = relay.TupleGetItem(func_557_call(), 1)
call_3995 = relay.TupleGetItem(func_558_call(), 1)
func_2584_call = mod.get_global_var('func_2584')
func_2585_call = mutated_mod.get_global_var('func_2585')
call_3998 = relay.TupleGetItem(func_2584_call(), 0)
call_3999 = relay.TupleGetItem(func_2585_call(), 0)
output = relay.Tuple([call_3994,call_3998,])
output2 = relay.Tuple([call_3995,call_3999,])
func_4003 = relay.Function([], output)
mod['func_4003'] = func_4003
mod = relay.transform.InferType()(mod)
output = func_4003()
func_4004 = relay.Function([], output)
mutated_mod['func_4004'] = func_4004
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1498_call = mod.get_global_var('func_1498')
func_1499_call = mutated_mod.get_global_var('func_1499')
call_4018 = relay.TupleGetItem(func_1498_call(), 0)
call_4019 = relay.TupleGetItem(func_1499_call(), 0)
output = call_4018
output2 = call_4019
func_4051 = relay.Function([], output)
mod['func_4051'] = func_4051
mod = relay.transform.InferType()(mod)
output = func_4051()
func_4052 = relay.Function([], output)
mutated_mod['func_4052'] = func_4052
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1452_call = mod.get_global_var('func_1452')
func_1453_call = mutated_mod.get_global_var('func_1453')
call_4107 = func_1452_call()
call_4108 = func_1452_call()
func_2655_call = mod.get_global_var('func_2655')
func_2658_call = mutated_mod.get_global_var('func_2658')
const_4127 = relay.const([[3.441705],[8.568996],[0.015799],[-8.575937],[1.271279],[-0.644657]], dtype = "float64")#candidate|4127|(6, 1)|const|float64
call_4126 = relay.TupleGetItem(func_2655_call(relay.reshape(call_4107.astype('float64'), [3, 4, 8]), relay.reshape(const_4127.astype('float64'), [3, 2]), ), 1)
call_4128 = relay.TupleGetItem(func_2658_call(relay.reshape(call_4107.astype('float64'), [3, 4, 8]), relay.reshape(const_4127.astype('float64'), [3, 2]), ), 1)
output = relay.Tuple([call_4107,call_4126,const_4127,])
output2 = relay.Tuple([call_4108,call_4128,const_4127,])
func_4138 = relay.Function([], output)
mod['func_4138'] = func_4138
mod = relay.transform.InferType()(mod)
mutated_mod['func_4138'] = func_4138
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4138_call = mutated_mod.get_global_var('func_4138')
call_4139 = func_4138_call()
output = call_4139
func_4140 = relay.Function([], output)
mutated_mod['func_4140'] = func_4140
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4146 = relay.var("var_4146", dtype = "int64", shape = (13, 13, 1))#candidate|4146|(13, 13, 1)|var|int64
var_4147 = relay.var("var_4147", dtype = "int64", shape = (13, 13, 14))#candidate|4147|(13, 13, 14)|var|int64
bop_4148 = relay.equal(var_4146.astype('bool'), var_4147.astype('bool')) # shape=(13, 13, 14)
output = relay.Tuple([bop_4148,])
output2 = relay.Tuple([bop_4148,])
func_4156 = relay.Function([var_4146,var_4147,], output)
mod['func_4156'] = func_4156
mod = relay.transform.InferType()(mod)
mutated_mod['func_4156'] = func_4156
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4156_call = mutated_mod.get_global_var('func_4156')
var_4158 = relay.var("var_4158", dtype = "int64", shape = (13, 13, 1))#candidate|4158|(13, 13, 1)|var|int64
var_4159 = relay.var("var_4159", dtype = "int64", shape = (13, 13, 14))#candidate|4159|(13, 13, 14)|var|int64
call_4157 = func_4156_call(var_4158,var_4159,)
output = call_4157
func_4160 = relay.Function([var_4158,var_4159,], output)
mutated_mod['func_4160'] = func_4160
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4165 = relay.var("var_4165", dtype = "uint32", shape = (16, 7, 13))#candidate|4165|(16, 7, 13)|var|uint32
const_4166 = relay.const([[[4,-10,-1,2,2,-7,-8,-2,4,-6,-4,1,3],[2,1,-4,10,-4,8,1,3,-3,-2,3,-1,-8],[1,2,3,10,3,-9,-9,-4,-10,-6,-4,-3,-6],[-4,-5,-3,-4,-10,8,-10,-7,4,3,-4,-2,7],[-9,-4,-7,3,1,-10,-10,9,-4,9,-8,-7,10],[6,-2,-7,3,8,-10,-4,9,-7,4,-9,6,10],[-10,7,-8,1,5,-3,-1,-10,3,3,8,5,5]],[[10,1,-5,9,-10,-4,7,10,10,2,-2,4,9],[5,-3,5,4,-5,6,1,-1,8,8,9,-9,10],[5,7,5,5,4,1,-7,-7,8,-10,4,-8,-8],[-2,7,-8,-5,4,7,-6,-1,-9,3,5,3,-2],[-5,-3,7,-10,7,-7,-3,2,4,2,-5,6,-8],[-3,6,10,-8,-4,8,3,2,-10,3,-6,8,-2],[1,-4,1,-10,5,-8,-2,-1,-8,10,4,-6,9]],[[-4,2,-1,6,-9,-5,3,8,-6,-8,5,-1,8],[2,-2,10,8,-4,2,-8,-6,-2,4,2,2,-9],[6,1,-5,1,-4,3,-10,4,-6,7,-5,1,-8],[-1,1,-9,-10,-2,-3,-2,2,2,-2,-6,-9,10],[-1,-5,-2,-9,-8,1,-9,3,-3,-3,-2,-9,-1],[3,-9,4,-4,8,7,10,-8,-3,1,10,-3,-1],[8,-1,8,-9,-7,-8,1,-6,5,-4,-6,-1,5]],[[2,-4,6,4,3,9,10,2,-8,6,-1,-1,-6],[-4,-3,8,-10,8,-6,-1,-4,-10,8,-4,7,2],[3,-5,-10,7,7,-9,-10,2,9,7,-4,2,9],[10,-6,-3,6,9,6,-9,3,-1,5,9,7,-1],[-10,-4,-9,-6,7,-5,9,8,1,-10,7,7,7],[10,-1,6,2,-2,-6,-7,8,-7,7,4,-7,2],[8,-6,5,-8,6,10,3,8,-10,4,6,-7,-1]],[[1,-5,-9,-10,5,-10,-2,6,6,-3,1,-9,3],[8,-8,-3,4,2,1,8,-9,-1,-7,-2,6,-7],[-9,2,6,4,-7,-5,-4,-2,-8,1,3,8,-8],[-4,6,-1,-2,8,1,1,8,-8,-2,-7,5,10],[1,7,-8,6,-4,8,-10,-1,-10,-10,8,-3,10],[-3,-10,-2,-10,-10,2,10,-3,-10,-7,-3,-5,7],[2,-8,-10,7,3,-10,-8,9,6,-6,10,-1,8]],[[5,-8,-1,-2,3,9,9,9,2,2,9,-3,-7],[2,-3,4,6,-10,-2,-5,4,7,5,-5,-5,-8],[-4,-9,5,1,-4,6,6,-8,-10,-5,6,-2,-10],[-7,3,-1,-8,10,-4,1,-5,-7,-7,-9,-7,-5],[-8,3,3,5,5,5,-8,7,7,9,9,10,10],[-4,6,1,4,2,-4,-5,2,-4,-6,-2,3,2],[-7,7,-4,6,2,-1,-3,-6,-9,10,3,-4,7]],[[4,7,-9,10,4,8,-1,-1,-7,-7,-3,-5,10],[7,7,-1,-1,6,-5,-7,-10,2,7,4,-8,-8],[7,-6,-1,2,6,-8,-2,-8,-3,-5,-1,-2,10],[4,-7,1,-6,-3,-9,-5,-8,1,-9,6,-5,5],[-10,6,-5,10,-5,-7,7,7,9,-10,-9,7,-1],[10,-8,3,1,7,-10,-9,-9,5,8,-9,-6,-4],[-1,2,7,-7,-8,2,10,7,-8,4,-3,-1,-2]],[[10,3,-2,-6,-4,8,-8,2,8,-9,9,-9,5],[5,-5,-10,5,-8,6,5,10,3,-2,8,-4,-4],[8,-9,7,1,-9,6,6,4,1,4,-5,-9,-2],[8,6,1,7,-9,2,-8,-2,-6,2,2,9,5],[5,-2,1,-2,-2,-2,-1,-5,10,-3,-2,3,-10],[7,3,5,4,-4,7,-1,-9,6,-4,2,-6,8],[-7,-2,-8,-8,9,-8,1,9,7,7,-4,5,-5]],[[4,3,9,-5,-7,-10,-3,-8,-3,4,-9,3,-7],[8,-5,-1,2,10,-6,-2,9,7,2,-4,4,-8],[-9,8,6,-9,7,-1,-6,2,-8,-2,-10,-9,-4],[-7,1,3,6,5,5,4,-4,3,-8,9,-3,4],[-9,4,-6,-2,-8,-4,-4,6,-2,3,7,-5,3],[10,-4,7,-7,-7,-4,9,-3,6,-3,1,3,3],[-10,-3,-10,-8,9,-8,-8,9,-5,4,3,-9,2]],[[-4,-4,5,3,6,2,10,1,8,-4,-3,-5,-8],[7,-9,-5,-6,-9,-2,10,10,6,-3,-9,-6,8],[-3,-6,-5,6,4,4,4,-10,8,6,1,-7,9],[-7,-10,-4,-8,-1,5,-7,-3,-10,6,3,1,-3],[3,9,7,-7,-1,-7,-1,-3,10,-5,1,-9,-7],[-3,4,-1,8,-9,5,4,-6,4,1,-4,-5,5],[-6,3,9,-10,-3,-1,10,-10,7,1,-4,1,-10]],[[10,5,1,10,-3,-1,-5,5,-9,-8,-1,2,-8],[-7,-6,7,-4,9,-2,-1,-1,9,1,2,10,-9],[-4,-5,9,-3,-10,-1,3,-10,-1,1,5,8,7],[-8,-9,-9,9,-7,-7,5,1,10,4,-10,-10,8],[4,-3,-7,7,7,-1,2,-7,10,-4,6,6,3],[6,8,1,2,-10,-5,9,5,-8,-9,3,5,-10],[-3,-10,4,-2,-1,-2,-6,-6,-9,3,-4,-10,8]],[[-10,-3,3,-9,-2,10,-3,6,-8,8,-5,8,3],[-3,-4,-6,-1,7,7,-8,10,3,-2,1,-3,-3],[-9,8,-2,-3,-9,1,2,-7,-5,-5,4,-10,-9],[6,1,-10,-2,-10,-9,-1,6,10,1,4,-2,-2],[-9,5,-3,-9,10,-5,-10,-7,2,9,9,5,-9],[-7,-9,9,9,-7,-5,-9,10,9,10,8,5,7],[9,3,2,8,9,1,-3,2,-7,-7,6,-6,4]],[[-6,3,1,7,9,6,-1,9,4,-10,-2,-9,3],[-4,2,5,5,3,-2,-3,-2,-2,-5,6,-5,-6],[-5,-5,-2,1,7,2,-6,9,7,-10,-3,3,3],[7,-10,-4,-10,7,-10,-4,2,8,-10,5,8,-6],[6,-9,3,-7,-9,-7,-2,10,1,-6,9,3,2],[7,-1,-1,4,-8,-3,7,-7,-10,-1,10,4,6],[-1,-3,5,3,2,-7,-1,3,-1,8,7,9,-8]],[[-9,-5,6,-4,-9,6,8,-3,4,9,1,-10,-10],[-9,-6,-7,9,-1,-8,-1,-5,8,-5,-8,6,-6],[9,-8,-2,7,-3,-4,6,5,-10,10,3,9,-10],[7,-6,5,-9,-8,9,9,-10,2,8,-2,6,-4],[-2,7,1,8,-8,-7,-3,8,-10,3,1,8,5],[-8,1,-9,4,-5,-3,2,-3,6,2,9,4,2],[5,5,-9,10,2,3,9,-10,-10,-2,9,-8,-6]],[[5,-6,3,8,-3,10,8,-7,7,10,8,10,-10],[10,2,-4,-3,-5,-6,-6,-9,-4,-8,8,7,-5],[-6,5,-3,-6,10,-3,2,1,2,-7,-2,8,4],[-7,3,-5,4,9,-4,6,4,-9,9,4,-7,-10],[2,1,5,-6,-10,1,1,-5,4,-3,9,5,-1],[-9,10,9,9,-9,-8,5,5,3,-6,5,10,-8],[-7,8,4,8,7,7,5,-10,-10,-2,1,-3,6]],[[4,-5,6,5,-1,9,2,-5,2,6,7,-7,1],[6,4,3,7,-10,9,5,6,-1,2,1,8,-7],[1,3,3,-7,1,-5,-7,1,4,-8,-2,3,5],[-9,9,-9,2,-6,1,-10,-3,-1,1,6,8,6],[-3,5,2,2,-3,-4,4,10,3,-8,-6,-9,-8],[2,1,7,8,-3,-9,-2,7,-7,-5,-6,8,7],[10,-1,-2,-8,3,-8,-9,-1,-7,3,8,5,-9]]], dtype = "uint32")#candidate|4166|(16, 7, 13)|const|uint32
bop_4167 = relay.logical_xor(var_4165.astype('uint32'), relay.reshape(const_4166.astype('uint32'), relay.shape_of(var_4165))) # shape=(16, 7, 13)
bop_4177 = relay.right_shift(var_4165.astype('int32'), relay.reshape(bop_4167.astype('int32'), relay.shape_of(var_4165))) # shape=(16, 7, 13)
output = relay.Tuple([bop_4177,])
output2 = relay.Tuple([bop_4177,])
func_4189 = relay.Function([var_4165,], output)
mod['func_4189'] = func_4189
mod = relay.transform.InferType()(mod)
var_4190 = relay.var("var_4190", dtype = "uint32", shape = (16, 7, 13))#candidate|4190|(16, 7, 13)|var|uint32
output = func_4189(var_4190)
func_4191 = relay.Function([var_4190], output)
mutated_mod['func_4191'] = func_4191
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2793_call = mod.get_global_var('func_2793')
func_2794_call = mutated_mod.get_global_var('func_2794')
call_4229 = func_2793_call()
call_4230 = func_2793_call()
func_1246_call = mod.get_global_var('func_1246')
func_1250_call = mutated_mod.get_global_var('func_1250')
var_4234 = relay.var("var_4234", dtype = "float64", shape = (6,))#candidate|4234|(6,)|var|float64
const_4235 = relay.const([-4.189106,-4.327339,-0.548413,7.328893,-4.682055,0.479939,-7.014402,-2.364360,4.517201,-3.549733,-0.524299,-8.960912,4.027179,-5.163740,2.180427,-0.800582,-0.830741,-8.443352,3.987056,1.853017,8.252540,-2.553624,6.588662,8.801513,6.373425,-6.342822,5.358082,-0.463887,1.739516,5.938718,4.352005,-3.694127,8.698528,-2.451688,-5.166361,-9.888230,-4.988432,-4.123953,1.602736,-4.745349,1.463103,8.923230,4.695112,-9.684111,-5.200459,2.714314,0.238597,-7.799228,9.727158,7.334371,-6.007113,0.869325,0.161848,3.542571,1.577323,8.960795,-8.744294,-3.115745,-8.192223,-9.158535,-1.811368,-4.778101,-8.858997,-5.175595,6.482287,9.543880,2.982032,-8.434475,-5.416798,-3.433330,-8.401066,6.349157,-1.869602,-3.474945,-4.408998,0.578888,0.912869,-9.667160,-6.250947,3.746708,-0.137778,-4.444667,9.794031,-5.590481,-2.932156,3.256328,-4.019795,7.380163,-6.083506,-4.342709,-1.614566,-4.801025,9.434084,2.193395,8.196383,-4.693330,-0.423806,-6.832335,4.697889,3.045177,2.319868,-4.170085,6.776550,-1.822862,-4.410301,-0.947204,-6.423113,-7.761838,5.473372,-2.378298,-3.096757,6.175992,2.575646,-9.877269,-8.447068,-4.993396,-2.177662,-4.025601,-9.261872,-9.175194,4.768111,8.431522,5.820483,3.287627,-0.931974,5.974523,-7.269265,3.837733,-3.383280,1.060598,7.836547,-3.324222,-7.040426,-4.604501,1.774242,6.875770,1.446731,5.782427,-1.715954,-5.998065,-4.472179,6.949356,-1.287959,-4.881973,-5.648265,8.605211,5.593412,-6.486482,-1.643099,-0.066849,8.444907,-7.168819,-9.164158,9.084025,2.970064,5.883649,6.458565,-9.878238,7.485968,7.193295,-6.738170,-7.836213,-4.848705,-5.168946,5.846896,2.287566,-8.953861,5.769197,2.943216,-6.559422,-6.489269,-7.696949,-8.763450,2.058458,2.979154,-1.717881,-6.741631,4.291377,7.099192,4.585360,-5.386651,1.524319,0.565828,0.979254,9.395318,7.778283,-2.900151,1.144090,-8.154540,-5.294274,1.443433,-7.497578], dtype = "float32")#candidate|4235|(192,)|const|float32
call_4233 = relay.TupleGetItem(func_1246_call(relay.reshape(var_4234.astype('float64'), [6,]), relay.reshape(const_4235.astype('float32'), [192,]), ), 3)
call_4236 = relay.TupleGetItem(func_1250_call(relay.reshape(var_4234.astype('float64'), [6,]), relay.reshape(const_4235.astype('float32'), [192,]), ), 3)
output = relay.Tuple([call_4229,call_4233,var_4234,const_4235,])
output2 = relay.Tuple([call_4230,call_4236,var_4234,const_4235,])
func_4252 = relay.Function([var_4234,], output)
mod['func_4252'] = func_4252
mod = relay.transform.InferType()(mod)
var_4253 = relay.var("var_4253", dtype = "float64", shape = (6,))#candidate|4253|(6,)|var|float64
output = func_4252(var_4253)
func_4254 = relay.Function([var_4253], output)
mutated_mod['func_4254'] = func_4254
mutated_mod = relay.transform.InferType()(mutated_mod)
func_148_call = mod.get_global_var('func_148')
func_150_call = mutated_mod.get_global_var('func_150')
call_4347 = relay.TupleGetItem(func_148_call(), 2)
call_4348 = relay.TupleGetItem(func_150_call(), 2)
output = call_4347
output2 = call_4348
func_4354 = relay.Function([], output)
mod['func_4354'] = func_4354
mod = relay.transform.InferType()(mod)
mutated_mod['func_4354'] = func_4354
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4354_call = mutated_mod.get_global_var('func_4354')
call_4355 = func_4354_call()
output = call_4355
func_4356 = relay.Function([], output)
mutated_mod['func_4356'] = func_4356
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4361 = relay.const([[[-2.725111,-4.885822,1.074578,-0.018383,2.355865,9.105069,-9.980205,6.298427,9.454528,-6.557672,5.946939,2.260501,6.054736,6.357993],[-6.419870,-8.838281,-0.992420,-2.776193,3.812077,5.605070,-3.573864,5.628112,-0.253861,-1.320633,-7.131729,0.239237,-2.673438,1.014812],[8.824116,6.392004,7.435639,-6.746373,-8.156151,1.107130,4.627678,9.659219,4.736596,-8.248957,3.404080,5.139048,7.700851,6.101179]],[[6.621413,-6.380256,-2.319015,-4.266821,8.069394,6.018323,-8.989865,8.776985,-2.453493,4.541480,-2.086239,4.258094,-0.152263,6.528925],[4.267031,1.158378,2.269080,1.561867,-0.993398,9.856403,-9.018615,1.459540,7.242116,-0.192526,4.565763,5.367674,1.840514,5.926278],[4.733074,0.676488,-5.414242,1.861200,-4.521676,2.252816,-5.219913,-0.434017,9.315663,2.583888,1.703959,-3.975269,2.606704,-1.487345]],[[-6.555063,0.878228,-2.323120,-1.245534,2.511828,-4.331419,-8.712594,-6.126992,-1.798068,3.443659,7.662672,-5.549323,-6.251665,3.061173],[-5.464670,-6.428692,-1.776816,-3.757026,3.022776,6.122233,-9.795791,-7.831615,7.954355,5.557707,-2.990457,7.668170,-2.216727,-3.497466],[7.813110,-3.305092,3.308363,-5.727135,-7.748800,-0.934181,-8.613389,6.107236,9.153772,9.410242,-5.076856,-1.492404,-0.173924,-3.623614]],[[8.257651,0.027992,0.728217,-3.752097,4.868947,-0.069874,4.661813,9.916013,-2.395396,-4.305799,-0.210906,-7.373263,-2.520075,0.183057],[-7.077352,7.406865,-2.826911,-8.084143,3.809592,-9.751970,-4.474603,-9.983939,5.708684,9.276431,-5.527761,9.960999,5.776098,-5.548137],[-3.257361,-8.448566,8.124726,-0.252429,4.873197,0.471553,3.604994,7.414483,-9.688493,7.895092,5.510912,0.393609,-5.079112,-7.119339]],[[-4.101576,-8.699197,6.638513,-9.891656,-2.304944,-9.344918,7.286213,-2.783870,-0.702881,-9.786487,-2.375490,-0.138709,-0.938441,5.171095],[2.691110,4.927644,-5.238067,-5.657571,-5.026145,1.576663,-6.611857,-2.750278,6.358963,-1.545438,-4.214269,6.393310,5.387712,-0.396419],[6.412253,-0.765972,-7.380291,6.120682,9.156474,-7.512417,-9.679028,4.157866,8.445021,-2.102430,-5.595841,-1.208015,-0.334388,0.992051]],[[-0.979154,9.420922,-5.928835,-1.864485,4.525046,1.656921,4.794344,4.491955,5.061792,-4.714979,-2.378321,-3.170490,-3.701458,-8.347439],[-1.600109,-0.377493,8.301736,-9.080936,1.412692,-1.984745,-2.553843,-5.059159,4.587094,1.497301,-1.424591,-4.566508,9.138235,8.768355],[5.390662,-1.790373,-0.252847,-8.536596,-2.013931,6.225142,6.338089,8.276832,3.750996,-3.847009,3.231582,-5.876549,5.965201,-1.556886]]], dtype = "float32")#candidate|4361|(6, 3, 14)|const|float32
uop_4362 = relay.asinh(const_4361.astype('float32')) # shape=(6, 3, 14)
bop_4366 = relay.greater_equal(uop_4362.astype('bool'), relay.reshape(const_4361.astype('bool'), relay.shape_of(uop_4362))) # shape=(6, 3, 14)
func_4354_call = mod.get_global_var('func_4354')
func_4356_call = mutated_mod.get_global_var('func_4356')
call_4370 = func_4354_call()
call_4371 = func_4354_call()
output = relay.Tuple([bop_4366,call_4370,])
output2 = relay.Tuple([bop_4366,call_4371,])
func_4374 = relay.Function([], output)
mod['func_4374'] = func_4374
mod = relay.transform.InferType()(mod)
mutated_mod['func_4374'] = func_4374
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4374_call = mutated_mod.get_global_var('func_4374')
call_4375 = func_4374_call()
output = call_4375
func_4376 = relay.Function([], output)
mutated_mod['func_4376'] = func_4376
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4383 = relay.var("var_4383", dtype = "float32", shape = ())#candidate|4383|()|var|float32
var_4384 = relay.var("var_4384", dtype = "float32", shape = (15, 7, 12))#candidate|4384|(15, 7, 12)|var|float32
bop_4385 = relay.floor_divide(var_4383.astype('float32'), var_4384.astype('float32')) # shape=(15, 7, 12)
output = relay.Tuple([bop_4385,])
output2 = relay.Tuple([bop_4385,])
func_4390 = relay.Function([var_4383,var_4384,], output)
mod['func_4390'] = func_4390
mod = relay.transform.InferType()(mod)
mutated_mod['func_4390'] = func_4390
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4390_call = mutated_mod.get_global_var('func_4390')
var_4392 = relay.var("var_4392", dtype = "float32", shape = ())#candidate|4392|()|var|float32
var_4393 = relay.var("var_4393", dtype = "float32", shape = (15, 7, 12))#candidate|4393|(15, 7, 12)|var|float32
call_4391 = func_4390_call(var_4392,var_4393,)
output = call_4391
func_4394 = relay.Function([var_4392,var_4393,], output)
mutated_mod['func_4394'] = func_4394
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2716_call = mod.get_global_var('func_2716')
func_2717_call = mutated_mod.get_global_var('func_2717')
call_4434 = relay.TupleGetItem(func_2716_call(), 1)
call_4435 = relay.TupleGetItem(func_2717_call(), 1)
output = call_4434
output2 = call_4435
func_4436 = relay.Function([], output)
mod['func_4436'] = func_4436
mod = relay.transform.InferType()(mod)
mutated_mod['func_4436'] = func_4436
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4436_call = mutated_mod.get_global_var('func_4436')
call_4437 = func_4436_call()
output = call_4437
func_4438 = relay.Function([], output)
mutated_mod['func_4438'] = func_4438
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4051_call = mod.get_global_var('func_4051')
func_4052_call = mutated_mod.get_global_var('func_4052')
call_4456 = func_4051_call()
call_4457 = func_4051_call()
func_4390_call = mod.get_global_var('func_4390')
func_4394_call = mutated_mod.get_global_var('func_4394')
var_4479 = relay.var("var_4479", dtype = "float32", shape = ())#candidate|4479|()|var|float32
var_4480 = relay.var("var_4480", dtype = "float32", shape = (3, 420))#candidate|4480|(3, 420)|var|float32
call_4478 = relay.TupleGetItem(func_4390_call(relay.reshape(var_4479.astype('float32'), []), relay.reshape(var_4480.astype('float32'), [15, 7, 12]), ), 0)
call_4481 = relay.TupleGetItem(func_4394_call(relay.reshape(var_4479.astype('float32'), []), relay.reshape(var_4480.astype('float32'), [15, 7, 12]), ), 0)
output = relay.Tuple([call_4456,call_4478,var_4479,var_4480,])
output2 = relay.Tuple([call_4457,call_4481,var_4479,var_4480,])
func_4483 = relay.Function([var_4479,var_4480,], output)
mod['func_4483'] = func_4483
mod = relay.transform.InferType()(mod)
mutated_mod['func_4483'] = func_4483
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4483_call = mutated_mod.get_global_var('func_4483')
var_4485 = relay.var("var_4485", dtype = "float32", shape = ())#candidate|4485|()|var|float32
var_4486 = relay.var("var_4486", dtype = "float32", shape = (3, 420))#candidate|4486|(3, 420)|var|float32
call_4484 = func_4483_call(var_4485,var_4486,)
output = call_4484
func_4487 = relay.Function([var_4485,var_4486,], output)
mutated_mod['func_4487'] = func_4487
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4515 = relay.const([[[-1.374465,7.363957,1.673268,9.129548,-3.100705],[7.662836,-9.092480,2.605799,-2.423820,5.009856],[-2.837291,5.998992,1.240556,-1.077794,3.151159],[-6.549575,-7.038245,2.282737,6.958964,7.802222],[8.643655,3.238594,-2.534186,-9.419191,-8.836891],[4.062886,3.673455,3.466957,-9.134876,7.921688],[5.568810,9.059748,7.722491,0.418252,7.164329],[0.616723,-5.624387,-2.230045,6.160912,3.369137],[-1.101659,-2.536474,-9.580812,3.522706,-6.655074]],[[-1.054023,-1.722223,7.960468,-0.830382,-6.320606],[0.739142,-4.513392,-0.215765,9.343415,-1.151313],[9.733024,3.677172,-0.472586,8.581716,-6.456846],[0.259489,4.830117,-7.090775,2.123048,-2.424346],[-7.102744,5.852685,6.334597,8.479724,-7.125639],[4.731484,7.332107,9.781223,-0.927898,8.286867],[-3.649759,-4.270158,-7.034560,8.604649,3.785586],[-6.589405,2.125205,5.252019,1.743613,3.053675],[-4.801253,-6.842548,-6.508036,9.720038,-2.553596]],[[4.615532,2.325080,8.198843,8.131540,-1.794537],[-6.338233,-0.399902,-4.039989,-7.097194,5.514696],[5.848005,-3.562032,1.244017,-8.622676,-3.549840],[9.442524,9.562212,2.663267,-9.406075,5.993187],[3.310112,3.342881,-7.003923,7.414112,-2.088647],[-0.114153,-4.843678,0.472001,2.835774,1.261997],[-9.831572,-4.200136,7.954673,-5.784668,-1.912397],[-9.007003,0.062767,6.049497,-0.717856,-4.267608],[1.489153,-4.289264,-5.255759,5.396270,5.828728]],[[8.974508,9.372902,-1.823454,9.837345,9.865720],[-5.721064,0.952925,7.923607,2.416724,-5.653322],[-4.841112,1.081421,9.444511,-8.834040,5.559302],[7.749684,-0.753557,-9.899052,-7.570227,3.502157],[9.632485,6.308658,-3.344479,-0.156814,-5.765278],[2.622389,-7.025327,-4.869614,-1.882286,9.957938],[-5.500283,-5.709569,6.650743,3.579791,-1.669462],[1.846261,9.102343,9.406925,-6.750966,1.549529],[-5.666378,7.183763,2.690019,-8.883256,7.088081]],[[-1.285679,6.022911,-2.206704,4.298092,-7.791348],[-8.511082,-6.253131,-0.176226,8.663987,8.996406],[-9.714446,-8.694360,-3.100624,2.058613,1.646018],[-9.989150,-6.245683,2.955557,8.173304,7.182892],[-3.072425,6.861915,9.679593,-4.914347,-9.038056],[9.931159,5.220758,1.498261,-8.697693,3.043385],[9.521550,1.483936,9.860573,-3.261667,9.309848],[-0.307374,7.258006,-9.638160,6.349649,-8.194172],[-9.218171,-9.306828,5.561892,-4.419221,-7.390204]],[[9.863617,6.955473,-5.194231,1.799004,7.604288],[-8.101576,1.635360,-1.401456,-8.205722,-6.983247],[4.784962,-5.882788,3.857079,2.451822,9.624545],[6.802276,1.130145,2.034274,4.427005,-3.093207],[-0.735070,-0.889077,1.693916,1.914530,-7.677892],[-0.918632,3.161406,-9.724510,-4.193661,-0.734949],[8.246415,-5.219713,-9.913587,-9.839760,7.162388],[9.645338,5.305617,3.637421,-1.265653,-4.586474],[-8.198125,-2.084802,-8.496244,-3.326051,9.156775]],[[-0.477446,-1.547660,1.627634,4.733292,-5.653107],[3.014379,-0.486200,7.228497,6.498226,-1.126257],[1.099949,-5.636291,-2.103435,-4.730584,1.040181],[3.992592,-5.873167,-9.204870,4.813292,-2.983964],[-1.890948,7.827140,-7.050558,-9.858004,-2.273306],[-2.914494,-0.072017,9.117387,9.678080,7.702301],[4.876946,-1.743519,0.192777,-6.665701,-2.560028],[-4.927565,-3.577141,9.779508,4.978200,-7.486171],[3.322472,5.543463,0.219068,-9.729941,-3.397680]],[[5.956689,7.715725,9.610960,-4.162388,4.164838],[-4.519801,-3.737412,4.180566,-6.301721,7.852886],[-9.512074,6.371869,-9.290786,-3.408933,6.841085],[4.105214,2.077371,-0.835799,4.651438,-7.161995],[-6.014311,-8.987056,6.272572,-7.887525,-8.011042],[-7.147636,-9.895353,-8.300841,-6.891026,-2.423083],[4.661792,-0.786901,-1.976274,-3.359678,7.217600],[-4.279232,2.356444,-1.190884,-3.117997,-4.765644],[9.688529,0.688452,-1.011847,-3.045805,-1.461285]]], dtype = "float32")#candidate|4515|(8, 9, 5)|const|float32
var_4516 = relay.var("var_4516", dtype = "float32", shape = (8, 9, 5))#candidate|4516|(8, 9, 5)|var|float32
bop_4517 = relay.floor_divide(const_4515.astype('float32'), relay.reshape(var_4516.astype('float32'), relay.shape_of(const_4515))) # shape=(8, 9, 5)
output = relay.Tuple([bop_4517,])
output2 = relay.Tuple([bop_4517,])
func_4523 = relay.Function([var_4516,], output)
mod['func_4523'] = func_4523
mod = relay.transform.InferType()(mod)
var_4524 = relay.var("var_4524", dtype = "float32", shape = (8, 9, 5))#candidate|4524|(8, 9, 5)|var|float32
output = func_4523(var_4524)
func_4525 = relay.Function([var_4524], output)
mutated_mod['func_4525'] = func_4525
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3765_call = mod.get_global_var('func_3765')
func_3767_call = mutated_mod.get_global_var('func_3767')
call_4530 = relay.TupleGetItem(func_3765_call(), 0)
call_4531 = relay.TupleGetItem(func_3767_call(), 0)
output = relay.Tuple([call_4530,])
output2 = relay.Tuple([call_4531,])
func_4536 = relay.Function([], output)
mod['func_4536'] = func_4536
mod = relay.transform.InferType()(mod)
output = func_4536()
func_4537 = relay.Function([], output)
mutated_mod['func_4537'] = func_4537
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4557 = relay.var("var_4557", dtype = "float32", shape = (3, 5, 8))#candidate|4557|(3, 5, 8)|var|float32
uop_4558 = relay.rsqrt(var_4557.astype('float32')) # shape=(3, 5, 8)
bop_4561 = relay.not_equal(uop_4558.astype('bool'), relay.reshape(var_4557.astype('bool'), relay.shape_of(uop_4558))) # shape=(3, 5, 8)
uop_4593 = relay.atan(var_4557.astype('float32')) # shape=(3, 5, 8)
func_1498_call = mod.get_global_var('func_1498')
func_1499_call = mutated_mod.get_global_var('func_1499')
call_4605 = relay.TupleGetItem(func_1498_call(), 1)
call_4606 = relay.TupleGetItem(func_1499_call(), 1)
output = relay.Tuple([bop_4561,uop_4593,call_4605,])
output2 = relay.Tuple([bop_4561,uop_4593,call_4606,])
func_4613 = relay.Function([var_4557,], output)
mod['func_4613'] = func_4613
mod = relay.transform.InferType()(mod)
mutated_mod['func_4613'] = func_4613
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4614 = relay.var("var_4614", dtype = "float32", shape = (3, 5, 8))#candidate|4614|(3, 5, 8)|var|float32
func_4613_call = mutated_mod.get_global_var('func_4613')
call_4615 = func_4613_call(var_4614)
output = call_4615
func_4616 = relay.Function([var_4614], output)
mutated_mod['func_4616'] = func_4616
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2606_call = mod.get_global_var('func_2606')
func_2608_call = mutated_mod.get_global_var('func_2608')
call_4626 = relay.TupleGetItem(func_2606_call(), 0)
call_4627 = relay.TupleGetItem(func_2608_call(), 0)
output = call_4626
output2 = call_4627
func_4638 = relay.Function([], output)
mod['func_4638'] = func_4638
mod = relay.transform.InferType()(mod)
mutated_mod['func_4638'] = func_4638
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4638_call = mutated_mod.get_global_var('func_4638')
call_4639 = func_4638_call()
output = call_4639
func_4640 = relay.Function([], output)
mutated_mod['func_4640'] = func_4640
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3546_call = mod.get_global_var('func_3546')
func_3547_call = mutated_mod.get_global_var('func_3547')
call_4729 = func_3546_call()
call_4730 = func_3546_call()
output = relay.Tuple([call_4729,])
output2 = relay.Tuple([call_4730,])
func_4736 = relay.Function([], output)
mod['func_4736'] = func_4736
mod = relay.transform.InferType()(mod)
output = func_4736()
func_4737 = relay.Function([], output)
mutated_mod['func_4737'] = func_4737
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4736_call = mod.get_global_var('func_4736')
func_4737_call = mutated_mod.get_global_var('func_4737')
call_4794 = relay.TupleGetItem(func_4736_call(), 0)
call_4795 = relay.TupleGetItem(func_4737_call(), 0)
func_2827_call = mod.get_global_var('func_2827')
func_2828_call = mutated_mod.get_global_var('func_2828')
call_4808 = func_2827_call()
call_4809 = func_2827_call()
func_3932_call = mod.get_global_var('func_3932')
func_3934_call = mutated_mod.get_global_var('func_3934')
call_4812 = func_3932_call()
call_4813 = func_3932_call()
func_695_call = mod.get_global_var('func_695')
func_698_call = mutated_mod.get_global_var('func_698')
const_4816 = relay.const(True, dtype = "bool")#candidate|4816|()|const|bool
call_4815 = relay.TupleGetItem(func_695_call(relay.reshape(const_4816.astype('bool'), [])), 3)
call_4817 = relay.TupleGetItem(func_698_call(relay.reshape(const_4816.astype('bool'), [])), 3)
func_1865_call = mod.get_global_var('func_1865')
func_1867_call = mutated_mod.get_global_var('func_1867')
const_4850 = relay.const([-7.138727,-4.060550,-0.092547,-1.590823,7.742547,-9.977004,5.788265,-6.245562,6.265816,4.510693,0.275199,9.448627,5.419689,6.828725,-0.224760,-3.507491,0.214332,1.651818,9.877092,3.344700,4.359428,7.853957,0.516323,1.921401,-4.629799,9.124739,-0.468813,3.783123,3.970730,-8.214933,-8.323853,-3.803911,7.587755,-5.012073,5.046252,6.669638,0.524489,5.384982,5.593223,4.553540,-8.399387,6.758508,2.266491,-7.047010,3.194003,5.468247,8.012501,-6.503630,0.278809,8.927360,-0.913575,3.831259,6.940632,8.370442,3.145120,5.342162,1.979001,-3.589469,6.884074,2.280523,1.583328,-8.301651,-9.798653,1.801418,0.569544,8.667461,-3.608997,-5.555098,0.747819,-6.029917,-4.287089,-9.712691,-5.350956,5.127692,2.208050,9.757076,6.689235,4.159769,-4.034062,1.177930,-7.573975,5.774790,1.093603,-2.441651,7.122275,6.101471,-5.336274,-9.502673,0.038344,-3.077450,-0.211029,3.594597,-5.795389,-9.702888,-9.053318,-1.480855,-3.449930,1.399895,3.679636,-5.924980,-9.792975,9.661542,-7.316502,3.401470,0.602195,-3.920219,8.187087,5.330687,0.411650,-1.699591,5.795214,-3.670899,8.591563,6.252873,6.669287,9.022322,5.206984,8.401168,-0.047993,7.521211,-1.866122,-6.456445,-2.784009,7.901684,5.205444,0.342239,8.661202,-0.144659,0.441968,0.760345,0.983559,-1.108767,9.913661,-1.070808,-7.083217,9.479306,-7.036348,5.347120,3.619980,-4.508110,-3.478647,8.010775,6.059416,-3.700031,4.997868,2.350896,9.052418,-0.466057,6.910744,-4.665655,-6.175750,5.164164,4.478500,4.461807,1.812023,0.041572,1.950201,5.432954,-6.056525,3.413211,-4.036871,4.102260,-9.641846,-4.914710,-9.713027,-5.584892,2.734641,3.690398,-9.633129,0.680067,-7.923103,2.311082,-4.346004,-1.200775,2.026396,-8.658739,0.839618,1.835136,1.433800,3.235254,-4.418263,1.722500,5.887445,6.368184,6.910303,-3.202233,2.003627,-7.626747,-3.111457,4.574031,-0.587696,0.393312], dtype = "float32")#candidate|4850|(192,)|const|float32
call_4849 = relay.TupleGetItem(func_1865_call(relay.reshape(const_4850.astype('float32'), [192, 1])), 5)
call_4851 = relay.TupleGetItem(func_1867_call(relay.reshape(const_4850.astype('float32'), [192, 1])), 5)
output = relay.Tuple([call_4794,call_4808,call_4812,call_4815,const_4816,call_4849,const_4850,])
output2 = relay.Tuple([call_4795,call_4809,call_4813,call_4817,const_4816,call_4851,const_4850,])
func_4853 = relay.Function([], output)
mod['func_4853'] = func_4853
mod = relay.transform.InferType()(mod)
output = func_4853()
func_4854 = relay.Function([], output)
mutated_mod['func_4854'] = func_4854
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2757_call = mod.get_global_var('func_2757')
func_2759_call = mutated_mod.get_global_var('func_2759')
call_5019 = relay.TupleGetItem(func_2757_call(), 0)
call_5020 = relay.TupleGetItem(func_2759_call(), 0)
output = relay.Tuple([call_5019,])
output2 = relay.Tuple([call_5020,])
func_5035 = relay.Function([], output)
mod['func_5035'] = func_5035
mod = relay.transform.InferType()(mod)
output = func_5035()
func_5036 = relay.Function([], output)
mutated_mod['func_5036'] = func_5036
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5059 = relay.var("var_5059", dtype = "float64", shape = (1, 13, 7))#candidate|5059|(1, 13, 7)|var|float64
const_5060 = relay.const([[[0.065809,-8.679222,-9.025963,-7.404694,-5.833989,-3.919511,-9.557195],[9.650198,6.316702,8.319143,-5.508542,8.113354,8.766252,9.560460],[5.912331,-8.436704,2.493099,-9.669596,8.128113,8.451885,1.187616],[3.740736,8.751718,3.327981,9.729045,4.350474,0.250339,1.935954],[0.044058,-2.826555,0.391234,8.410996,4.145313,-8.094287,8.206389],[-3.351314,9.464924,-0.993363,8.161409,0.953383,-0.981611,-2.167990],[2.128583,-4.419771,-8.300465,3.636067,-0.812834,-4.096774,3.802119],[-6.236923,-3.048779,0.837390,0.952875,-3.323851,8.238617,3.241222],[-6.096940,4.424959,9.464303,-4.537052,-2.603364,2.736217,9.766456],[-2.135002,4.791693,8.762182,-3.428996,3.743899,-1.824241,-5.981293],[-0.773005,0.953186,1.216629,-5.396342,6.527541,1.292314,6.831324],[-5.402351,-4.852270,5.274078,6.830113,-9.816456,9.527741,5.942278],[4.546244,7.031372,2.704329,3.655710,8.958046,5.162869,-9.637876]],[[0.267395,-6.977424,-7.249077,-2.588143,-2.666191,-4.095209,7.329627],[-6.867040,6.979154,-1.288491,8.131569,-0.052730,9.300119,8.372742],[-7.864407,3.718593,7.216196,1.059014,-2.935762,7.485303,9.086756],[3.202581,5.495204,-5.411348,-8.527194,9.745064,-6.221265,-5.254418],[3.405036,7.305702,0.634153,6.870129,-6.378422,6.390081,0.898997],[5.930941,-0.916365,7.683218,-8.158998,1.904928,1.441762,6.013102],[-0.468512,6.162882,7.380720,3.558109,4.486342,3.399905,0.483285],[-2.012418,3.778537,8.620279,8.148217,9.106231,-9.163053,-6.717469],[9.988047,-4.755832,7.229697,7.537538,-7.201998,0.084392,-2.438438],[8.078829,5.954025,-2.442733,0.538161,6.497783,-4.240702,-7.341740],[7.258836,-8.736988,-6.104694,-5.443338,-2.233086,-7.782520,-2.806148],[-1.250819,-5.148486,-1.950571,-0.391538,-3.849575,-6.411712,-1.857369],[-6.673832,-9.562992,7.928979,-1.838524,6.516643,9.687808,7.421462]],[[-5.338705,2.636068,-9.056855,-4.980346,-5.024597,6.084921,-0.368036],[-5.883604,-7.705659,7.763789,-3.365864,-3.281935,0.529627,6.057805],[3.466318,-5.829204,-6.098415,2.787065,-7.081428,9.287727,-0.199669],[2.893016,-0.665602,4.120534,8.052761,6.596253,4.352154,-3.607804],[0.212945,9.534694,-7.890813,-8.734393,4.363735,4.794035,5.771637],[-2.066390,5.938498,-4.521908,7.730164,6.216713,3.821058,-3.366437],[-9.905166,0.135414,-6.034526,-3.111845,-5.907543,1.808862,-4.913334],[1.442812,7.965493,5.459438,-0.173707,9.265458,8.427291,-2.662466],[7.717184,4.186148,5.890684,-2.764572,8.934579,9.917166,0.444355],[-7.668723,7.930017,-5.878592,9.661426,-1.055644,5.534298,-9.593661],[-4.027320,9.922567,5.614393,3.434104,9.641299,1.169330,-9.352507],[7.663565,5.568250,-9.960074,8.035090,-3.932041,-9.695379,-4.536504],[-6.015723,1.415625,0.226332,-5.715220,6.610562,-3.532324,0.958467]],[[-3.633279,-5.194283,-6.075125,4.324649,-3.604709,5.149874,6.129084],[0.457803,0.835184,-3.022522,-5.835844,-5.850682,2.966375,-1.617329],[-3.607803,6.690877,-1.058069,-9.937654,9.042015,7.765472,6.608325],[-0.402655,-5.313188,-6.799212,8.695184,-5.413381,6.212799,3.756622],[7.667636,-8.808288,3.071737,-9.956851,1.355530,-3.918930,-5.813897],[-2.955073,-4.725900,-7.546484,9.632889,4.305215,-5.305041,-1.882404],[-1.820489,-9.450308,-9.022342,2.324043,-3.506830,1.765439,7.163206],[-8.038231,3.716082,5.828459,-9.558079,-0.799754,-1.072574,-4.829891],[-9.452760,-0.501508,-7.898719,-4.942090,3.675965,9.325293,2.293625],[9.237391,-9.075605,-4.411938,5.035431,-8.506653,3.775446,2.758340],[-9.135984,-5.895842,-7.884493,4.582945,5.998831,1.624605,5.079532],[-0.701051,3.840799,7.170815,-4.484295,9.876744,2.217865,1.854494],[5.316872,2.882735,-6.936884,-4.878412,-1.828211,-3.275395,2.004713]],[[8.601049,-1.731529,6.056892,3.575014,1.907048,-5.336798,9.127669],[-0.218039,-8.626973,9.326105,9.469628,-6.982441,7.368210,6.220864],[-4.462479,7.022722,-9.550230,-4.984296,-0.282576,-0.048105,4.678448],[-0.650334,7.743308,4.006194,-9.998213,1.703805,-6.744075,2.808620],[-6.043761,3.005975,7.659845,-7.915073,-0.750722,6.381558,9.238828],[0.251368,-7.308233,2.178449,-3.928823,-1.638918,-4.236612,8.172639],[1.673414,-9.871800,5.237500,-9.115910,-8.516919,-4.735193,1.192906],[5.493310,-7.958088,3.060610,4.879093,-5.963890,6.787665,-9.955460],[-0.899006,9.040387,0.843637,7.321439,5.708811,1.718981,8.846266],[7.037116,-3.681631,4.327209,9.459917,0.220864,2.378590,-5.533310],[-3.211435,-4.229738,-7.669346,-6.143630,0.326030,6.827642,-5.562962],[4.261752,-9.306432,-3.736619,0.573812,3.660443,1.535465,0.081893],[-1.662038,6.705097,5.247120,0.828571,8.554996,3.759384,-2.004783]],[[-8.055504,9.288786,-9.545054,-4.964692,-2.487206,-2.920927,-3.560883],[5.698884,-5.231596,7.185934,-0.425542,-1.874486,4.881511,-8.694579],[-0.674918,0.731810,2.025977,-1.326810,-0.908187,-2.861367,3.268376],[5.435515,-7.059086,6.875588,-8.597794,6.709984,3.783804,4.906368],[1.080228,9.121680,-5.379994,-1.081282,-2.904653,5.678389,3.595073],[6.949944,-5.835664,-9.478521,7.058490,2.519479,1.752011,8.037471],[-6.357048,0.194318,-5.154901,-4.346984,9.907476,-1.189521,6.995659],[-3.847106,4.984863,0.911273,-4.950221,6.513380,-0.019775,-1.130337],[2.559398,-8.309825,-9.808111,3.834547,8.192776,7.124353,4.732826],[-4.971657,8.694803,0.561782,-1.726347,-1.954976,1.043956,7.672976],[-3.304246,7.733647,3.599835,-2.381983,7.161120,-3.218464,3.435015],[2.520982,2.124389,7.192345,-9.810045,4.112661,-6.334605,-0.336688],[5.763369,7.890038,8.177215,4.224332,-2.562808,-1.914767,-9.065116]],[[-9.731293,-9.618984,-8.127756,1.398113,-0.653871,-7.332547,9.804268],[3.027007,-9.287844,1.165700,-9.063052,-5.242721,8.089398,4.005138],[-2.344785,-5.569020,9.852770,-1.186995,-7.289234,-2.077471,-3.904419],[-3.812625,1.437009,0.127938,7.278067,0.654073,4.087073,8.847467],[-0.397681,-1.981858,-5.032087,-0.292271,9.365508,2.788766,-8.728900],[-3.553723,5.002651,-0.092099,-9.697269,-4.665414,-7.480575,2.311304],[-9.154028,-8.531822,-2.720626,9.956773,1.592778,-1.491823,3.999317],[-1.062110,3.500383,-2.891781,-1.147916,7.515563,-3.764797,-5.326878],[1.189013,-2.241143,-6.891399,5.726148,4.293827,-0.397266,-8.417851],[6.108161,-9.925812,3.741594,-2.510211,-5.814241,7.825644,5.312435],[-6.634257,-0.199765,9.599266,6.342513,-1.305298,-0.739097,1.706900],[-1.953859,-1.034152,2.771574,-1.139781,-2.479640,-2.415189,6.582755],[5.137444,0.784681,-9.754881,8.868133,-8.622825,9.099546,5.644341]],[[-9.999998,-2.152953,-6.486091,-3.027329,-7.852460,9.451783,4.473379],[6.951958,5.399604,2.545359,-3.556569,-6.539194,-6.666094,-2.246217],[5.057132,0.331918,6.223294,9.617404,-8.217045,8.633161,-5.994002],[-5.982721,5.938465,-8.118696,-7.322541,3.218691,3.921248,-4.151034],[3.885206,2.851814,4.445345,-8.850811,1.856431,-6.682603,-6.891838],[-5.786657,-9.563780,-2.915617,-7.719364,-0.274390,6.288999,-1.511632],[-6.907314,-5.033340,2.541940,-2.996857,-7.487187,6.267078,-4.546537],[-1.791663,-4.757643,8.753908,8.480614,-0.500330,-0.296373,-6.882008],[-0.764364,-4.311307,1.525360,-2.639480,8.590917,6.888189,-3.015846],[7.129005,2.503255,1.357005,-4.073048,-7.161184,-4.400334,2.363767],[-6.702465,-4.713415,-8.552883,5.742133,6.587695,8.529332,-1.365734],[0.366820,4.196915,-3.658300,-9.839378,-1.216319,-3.651908,-6.219171],[8.054966,-2.142531,4.274215,2.503446,3.583674,5.836195,-6.862969]],[[3.456610,-9.199639,4.848032,3.560613,-5.965063,3.127631,-8.242951],[9.440831,9.796862,1.101214,-0.126105,-1.234087,-4.626846,-5.863604],[9.794756,-8.168181,-5.291067,3.567558,0.960764,5.234089,-0.610009],[-0.458858,-6.725954,8.234801,6.705292,4.098307,4.142084,0.401907],[-8.693499,9.337537,-5.595422,-1.734389,-4.979237,6.349055,9.391620],[1.844635,0.787357,-9.756867,-4.436081,5.639889,-4.314834,3.871072],[2.762771,-9.004754,8.512736,3.334067,2.100739,-8.062342,8.556579],[6.278338,-5.309755,-4.679620,7.074234,8.371757,-1.771347,6.332556],[-8.562487,-0.663453,9.090489,8.821235,-4.759075,-0.953581,-4.920983],[-6.510224,-8.735180,-1.839456,-8.407847,9.442306,-5.573546,3.525950],[4.812668,1.905851,-4.245506,3.225118,-8.729071,-9.436026,0.661735],[9.480142,8.150468,2.245747,3.185893,-5.419656,-7.102569,2.159610],[-1.992089,0.543854,7.943134,4.360026,-3.631268,2.891458,7.798911]]], dtype = "float64")#candidate|5060|(9, 13, 7)|const|float64
bop_5061 = relay.floor_divide(var_5059.astype('float64'), const_5060.astype('float64')) # shape=(9, 13, 7)
func_4536_call = mod.get_global_var('func_4536')
func_4537_call = mutated_mod.get_global_var('func_4537')
call_5068 = relay.TupleGetItem(func_4536_call(), 0)
call_5069 = relay.TupleGetItem(func_4537_call(), 0)
uop_5090 = relay.sin(var_5059.astype('float64')) # shape=(1, 13, 7)
func_3546_call = mod.get_global_var('func_3546')
func_3547_call = mutated_mod.get_global_var('func_3547')
call_5100 = func_3546_call()
call_5101 = func_3546_call()
bop_5113 = relay.right_shift(bop_5061.astype('int64'), relay.reshape(const_5060.astype('int64'), relay.shape_of(bop_5061))) # shape=(9, 13, 7)
output = relay.Tuple([call_5068,uop_5090,call_5100,bop_5113,])
output2 = relay.Tuple([call_5069,uop_5090,call_5101,bop_5113,])
func_5134 = relay.Function([var_5059,], output)
mod['func_5134'] = func_5134
mod = relay.transform.InferType()(mod)
var_5135 = relay.var("var_5135", dtype = "float64", shape = (1, 13, 7))#candidate|5135|(1, 13, 7)|var|float64
output = func_5134(var_5135)
func_5136 = relay.Function([var_5135], output)
mutated_mod['func_5136'] = func_5136
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4003_call = mod.get_global_var('func_4003')
func_4004_call = mutated_mod.get_global_var('func_4004')
call_5141 = relay.TupleGetItem(func_4003_call(), 0)
call_5142 = relay.TupleGetItem(func_4004_call(), 0)
output = relay.Tuple([call_5141,])
output2 = relay.Tuple([call_5142,])
func_5168 = relay.Function([], output)
mod['func_5168'] = func_5168
mod = relay.transform.InferType()(mod)
mutated_mod['func_5168'] = func_5168
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5168_call = mutated_mod.get_global_var('func_5168')
call_5169 = func_5168_call()
output = call_5169
func_5170 = relay.Function([], output)
mutated_mod['func_5170'] = func_5170
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2793_call = mod.get_global_var('func_2793')
func_2794_call = mutated_mod.get_global_var('func_2794')
call_5213 = func_2793_call()
call_5214 = func_2793_call()
output = relay.Tuple([call_5213,])
output2 = relay.Tuple([call_5214,])
func_5215 = relay.Function([], output)
mod['func_5215'] = func_5215
mod = relay.transform.InferType()(mod)
output = func_5215()
func_5216 = relay.Function([], output)
mutated_mod['func_5216'] = func_5216
mutated_mod = relay.transform.InferType()(mutated_mod)
func_858_call = mod.get_global_var('func_858')
func_859_call = mutated_mod.get_global_var('func_859')
call_5237 = relay.TupleGetItem(func_858_call(), 0)
call_5238 = relay.TupleGetItem(func_859_call(), 0)
func_3588_call = mod.get_global_var('func_3588')
func_3590_call = mutated_mod.get_global_var('func_3590')
call_5242 = func_3588_call()
call_5243 = func_3588_call()
func_2380_call = mod.get_global_var('func_2380')
func_2382_call = mutated_mod.get_global_var('func_2382')
call_5271 = relay.TupleGetItem(func_2380_call(), 0)
call_5272 = relay.TupleGetItem(func_2382_call(), 0)
func_4853_call = mod.get_global_var('func_4853')
func_4854_call = mutated_mod.get_global_var('func_4854')
call_5283 = relay.TupleGetItem(func_4853_call(), 5)
call_5284 = relay.TupleGetItem(func_4854_call(), 5)
output = relay.Tuple([call_5237,call_5242,call_5271,call_5283,])
output2 = relay.Tuple([call_5238,call_5243,call_5272,call_5284,])
func_5293 = relay.Function([], output)
mod['func_5293'] = func_5293
mod = relay.transform.InferType()(mod)
output = func_5293()
func_5294 = relay.Function([], output)
mutated_mod['func_5294'] = func_5294
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3403_call = mod.get_global_var('func_3403')
func_3404_call = mutated_mod.get_global_var('func_3404')
call_5320 = relay.TupleGetItem(func_3403_call(), 1)
call_5321 = relay.TupleGetItem(func_3404_call(), 1)
output = call_5320
output2 = call_5321
func_5336 = relay.Function([], output)
mod['func_5336'] = func_5336
mod = relay.transform.InferType()(mod)
output = func_5336()
func_5337 = relay.Function([], output)
mutated_mod['func_5337'] = func_5337
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5343 = relay.var("var_5343", dtype = "float64", shape = (14, 8, 1))#candidate|5343|(14, 8, 1)|var|float64
var_5344 = relay.var("var_5344", dtype = "float64", shape = (14, 8, 11))#candidate|5344|(14, 8, 11)|var|float64
bop_5345 = relay.floor_divide(var_5343.astype('float64'), var_5344.astype('float64')) # shape=(14, 8, 11)
output = relay.Tuple([bop_5345,])
output2 = relay.Tuple([bop_5345,])
func_5358 = relay.Function([var_5343,var_5344,], output)
mod['func_5358'] = func_5358
mod = relay.transform.InferType()(mod)
var_5359 = relay.var("var_5359", dtype = "float64", shape = (14, 8, 1))#candidate|5359|(14, 8, 1)|var|float64
var_5360 = relay.var("var_5360", dtype = "float64", shape = (14, 8, 11))#candidate|5360|(14, 8, 11)|var|float64
output = func_5358(var_5359,var_5360,)
func_5361 = relay.Function([var_5359,var_5360,], output)
mutated_mod['func_5361'] = func_5361
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3008_call = mod.get_global_var('func_3008')
func_3009_call = mutated_mod.get_global_var('func_3009')
call_5376 = func_3008_call()
call_5377 = func_3008_call()
func_1452_call = mod.get_global_var('func_1452')
func_1453_call = mutated_mod.get_global_var('func_1453')
call_5392 = func_1452_call()
call_5393 = func_1452_call()
func_1498_call = mod.get_global_var('func_1498')
func_1499_call = mutated_mod.get_global_var('func_1499')
call_5403 = relay.TupleGetItem(func_1498_call(), 0)
call_5404 = relay.TupleGetItem(func_1499_call(), 0)
func_5134_call = mod.get_global_var('func_5134')
func_5136_call = mutated_mod.get_global_var('func_5136')
const_5416 = relay.const([-2.956406,-9.393907,-6.013259,-1.494953,-1.292419,7.360446,2.265135,-1.103747,-6.507224,-8.324005,2.624643,-5.031959,1.262664,6.866330,-1.721158,5.557913,9.762178,6.592681,7.339986,-1.940472,-7.606140,-2.102918,-6.306649,-8.770172,-1.121805,-3.699610,3.477585,-2.212689,-7.327293,1.719423,-4.506925,1.399321,5.349598,1.919284,-9.712969,-9.241324,4.251581,-0.937058,7.170084,3.105835,0.915305,-0.850752,-8.044607,5.946104,-5.342259,0.180087,-4.789131,2.298812,6.340667,-4.878335,-4.290922,7.346720,-8.367044,-7.454611,-1.476187,1.982272,0.181598,-8.259507,-8.604310,-0.523312,-5.261152,2.852366,-1.801117,-7.981208,1.320338,5.717396,1.772696,8.080932,5.751862,-7.825376,3.652409,9.482127,2.552544,-7.626705,-6.269996,-2.357716,-1.986474,8.242365,-2.057416,7.326983,-6.880231,-5.810513,9.246157,0.833975,6.595485,-7.560466,4.690339,4.194528,7.782623,-1.698099,3.782745], dtype = "float64")#candidate|5416|(91,)|const|float64
call_5415 = relay.TupleGetItem(func_5134_call(relay.reshape(const_5416.astype('float64'), [1, 13, 7])), 3)
call_5417 = relay.TupleGetItem(func_5136_call(relay.reshape(const_5416.astype('float64'), [1, 13, 7])), 3)
output = relay.Tuple([call_5376,call_5392,call_5403,call_5415,const_5416,])
output2 = relay.Tuple([call_5377,call_5393,call_5404,call_5417,const_5416,])
func_5433 = relay.Function([], output)
mod['func_5433'] = func_5433
mod = relay.transform.InferType()(mod)
output = func_5433()
func_5434 = relay.Function([], output)
mutated_mod['func_5434'] = func_5434
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3878_call = mod.get_global_var('func_3878')
func_3880_call = mutated_mod.get_global_var('func_3880')
call_5469 = relay.TupleGetItem(func_3878_call(), 1)
call_5470 = relay.TupleGetItem(func_3880_call(), 1)
var_5474 = relay.var("var_5474", dtype = "float32", shape = (11, 3, 6))#candidate|5474|(11, 3, 6)|var|float32
bop_5475 = relay.greater(call_5469.astype('bool'), relay.reshape(var_5474.astype('bool'), relay.shape_of(call_5469))) # shape=(11, 3, 6)
bop_5478 = relay.greater(call_5470.astype('bool'), relay.reshape(var_5474.astype('bool'), relay.shape_of(call_5470))) # shape=(11, 3, 6)
func_3709_call = mod.get_global_var('func_3709')
func_3711_call = mutated_mod.get_global_var('func_3711')
call_5479 = func_3709_call()
call_5480 = func_3709_call()
const_5496 = relay.const([[[6.200966,-1.193920,-4.743665,-3.098606,7.377843,-1.603655],[5.005731,7.588115,-0.021519,6.894322,1.215749,9.026414],[-9.748652,8.372717,-8.245454,2.091530,-0.371462,0.080820]],[[3.850648,1.980682,-2.704962,-2.963890,-3.419936,5.656467],[7.480859,4.165897,7.256600,3.862558,-4.398988,6.506000],[3.679008,-3.088000,-8.423416,-4.739359,5.034683,4.753168]],[[-1.170320,5.961900,1.964055,4.655289,-2.581898,-0.827822],[1.529890,6.110970,-8.147229,-6.585535,9.151363,5.636763],[-6.676106,-0.958811,6.193027,-3.919482,3.033554,-6.298403]],[[-5.380842,-5.494085,-6.369714,5.951358,-0.863906,4.619039],[7.739450,3.381216,3.089253,-1.948952,-3.566306,1.553356],[-7.308319,8.965931,-1.616767,6.424946,0.421698,9.482354]],[[-1.712449,5.174676,8.395428,7.890034,-1.572930,5.632670],[0.525484,-6.213885,-0.342647,3.715312,6.782542,5.087002],[8.738420,-8.710103,-0.820614,-9.896662,-5.531981,8.251389]],[[8.082070,-0.148226,5.843586,1.467630,-3.502408,4.906283],[0.447401,7.106316,0.940280,-2.564881,0.911459,-1.742890],[-6.423618,-7.396789,-1.311422,-4.478424,-7.997175,-2.714130]],[[3.319286,-5.537353,3.869613,-9.683195,4.396523,8.349169],[-0.563820,9.215464,-2.437336,2.036075,-3.129422,-8.355304],[-6.852805,-7.632351,3.882050,-4.632717,-6.444051,-8.020294]],[[-3.402894,5.725078,8.451972,1.532006,-6.674456,9.120971],[-2.588664,-9.196660,1.579281,0.409180,8.136147,-1.273247],[-3.236607,6.750013,-4.089617,-5.988714,6.021844,-8.092921]],[[-9.521329,-5.316108,-3.303454,-8.700817,0.282597,4.018226],[2.052140,-3.073036,6.126829,6.103478,9.124452,-3.003943],[8.393906,3.960332,-5.215161,7.366761,3.628736,-4.686932]],[[3.280159,-6.198706,0.020585,4.451121,-5.374021,0.227361],[4.195081,-8.446981,-0.425210,-5.028015,6.610888,-6.005330],[4.587814,1.861926,4.691403,-3.948981,-2.738946,6.418951]],[[-9.991643,-4.893004,-2.723356,-4.055339,-3.836336,2.530302],[-0.888876,-9.547856,5.003983,6.499558,-7.963612,7.626346],[-9.235956,8.169536,-9.180068,-1.568062,1.849626,3.913240]]], dtype = "float32")#candidate|5496|(11, 3, 6)|const|float32
bop_5497 = relay.maximum(var_5474.astype('int16'), relay.reshape(const_5496.astype('int16'), relay.shape_of(var_5474))) # shape=(11, 3, 6)
output = relay.Tuple([bop_5475,call_5479,bop_5497,])
output2 = relay.Tuple([bop_5478,call_5480,bop_5497,])
func_5508 = relay.Function([var_5474,], output)
mod['func_5508'] = func_5508
mod = relay.transform.InferType()(mod)
mutated_mod['func_5508'] = func_5508
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5509 = relay.var("var_5509", dtype = "float32", shape = (11, 3, 6))#candidate|5509|(11, 3, 6)|var|float32
func_5508_call = mutated_mod.get_global_var('func_5508')
call_5510 = func_5508_call(var_5509)
output = call_5510
func_5511 = relay.Function([var_5509], output)
mutated_mod['func_5511'] = func_5511
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5513 = relay.const([[[4,-9,-10,5,4,5,9,2]],[[3,-4,-4,3,9,-4,7,-8]],[[-5,-2,-1,4,8,-3,-5,-2]],[[-4,-9,-1,8,8,-6,-7,6]],[[3,-7,-4,10,-10,1,-7,-4]],[[-1,9,-7,-6,6,-8,8,7]],[[9,-4,6,-4,-6,-4,10,-3]],[[-2,5,-9,2,4,-10,-5,2]],[[2,-8,-1,-5,-9,-9,8,2]]], dtype = "uint8")#candidate|5513|(9, 1, 8)|const|uint8
var_5514 = relay.var("var_5514", dtype = "uint8", shape = (9, 8, 8))#candidate|5514|(9, 8, 8)|var|uint8
bop_5515 = relay.not_equal(const_5513.astype('bool'), var_5514.astype('bool')) # shape=(9, 8, 8)
output = relay.Tuple([bop_5515,])
output2 = relay.Tuple([bop_5515,])
func_5521 = relay.Function([var_5514,], output)
mod['func_5521'] = func_5521
mod = relay.transform.InferType()(mod)
mutated_mod['func_5521'] = func_5521
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5522 = relay.var("var_5522", dtype = "uint8", shape = (9, 8, 8))#candidate|5522|(9, 8, 8)|var|uint8
func_5521_call = mutated_mod.get_global_var('func_5521')
call_5523 = func_5521_call(var_5522)
output = call_5523
func_5524 = relay.Function([var_5522], output)
mutated_mod['func_5524'] = func_5524
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5555 = relay.var("var_5555", dtype = "bool", shape = (6, 5, 16))#candidate|5555|(6, 5, 16)|var|bool
const_5556 = relay.const([[[True,False,True,True,False,True,False,False,True,False,False,True,False,True,True,True],[True,True,True,False,False,True,False,False,False,False,True,False,True,False,False,False],[False,True,True,True,False,True,True,True,True,True,False,True,True,True,False,False],[False,False,False,True,True,True,True,True,True,False,True,False,False,True,False,True],[False,True,False,True,False,True,False,True,False,True,False,True,False,True,False,True]],[[True,False,False,False,True,True,True,False,True,False,False,False,True,False,True,True],[True,True,False,True,False,True,False,False,False,True,False,False,False,False,True,True],[False,True,True,False,False,False,False,False,False,True,False,True,True,True,False,True],[False,True,False,False,False,True,False,False,False,False,False,False,False,False,True,True],[True,False,True,False,False,True,False,False,False,False,True,False,True,True,True,True]],[[False,True,True,False,False,True,False,False,False,True,False,False,True,True,True,False],[True,False,False,True,False,False,True,False,False,False,False,True,False,True,False,False],[True,True,True,True,True,True,False,True,False,False,True,True,False,True,False,True],[True,False,True,True,True,False,False,True,True,False,True,True,False,True,True,True],[True,False,False,False,False,False,True,False,True,False,False,True,True,False,False,True]],[[False,True,False,True,False,False,True,True,True,False,False,True,True,True,False,False],[False,False,False,False,True,True,False,False,False,False,True,True,False,True,False,True],[True,True,False,True,True,True,False,False,True,False,True,True,True,True,True,True],[False,False,True,True,True,False,True,True,False,False,True,True,True,True,False,False],[False,False,True,False,False,True,False,True,True,False,False,True,True,False,False,True]],[[False,False,False,True,False,True,True,False,True,False,True,True,True,True,True,False],[False,True,False,False,False,False,True,False,False,False,True,False,False,True,True,False],[True,False,True,True,True,False,False,True,False,True,False,False,True,True,False,True],[False,False,True,True,False,False,True,True,False,False,True,False,True,False,False,True],[False,False,False,False,False,False,True,True,False,True,True,True,False,True,False,True]],[[True,True,False,True,True,True,False,False,True,True,False,False,False,True,True,False],[True,False,False,True,False,True,False,False,False,True,True,True,False,True,False,True],[False,False,True,False,True,True,False,False,True,False,False,True,True,False,True,False],[False,False,False,False,True,False,True,False,False,False,True,False,False,True,False,False],[True,True,False,False,False,False,False,True,True,False,False,False,False,False,True,False]]], dtype = "bool")#candidate|5556|(6, 5, 16)|const|bool
bop_5557 = relay.logical_or(var_5555.astype('bool'), relay.reshape(const_5556.astype('bool'), relay.shape_of(var_5555))) # shape=(6, 5, 16)
func_2606_call = mod.get_global_var('func_2606')
func_2608_call = mutated_mod.get_global_var('func_2608')
call_5587 = relay.TupleGetItem(func_2606_call(), 0)
call_5588 = relay.TupleGetItem(func_2608_call(), 0)
func_3134_call = mod.get_global_var('func_3134')
func_3136_call = mutated_mod.get_global_var('func_3136')
call_5599 = func_3134_call()
call_5600 = func_3134_call()
uop_5605 = relay.sinh(const_5556.astype('float32')) # shape=(6, 5, 16)
output = relay.Tuple([bop_5557,call_5587,call_5599,uop_5605,])
output2 = relay.Tuple([bop_5557,call_5588,call_5600,uop_5605,])
func_5627 = relay.Function([var_5555,], output)
mod['func_5627'] = func_5627
mod = relay.transform.InferType()(mod)
var_5628 = relay.var("var_5628", dtype = "bool", shape = (6, 5, 16))#candidate|5628|(6, 5, 16)|var|bool
output = func_5627(var_5628)
func_5629 = relay.Function([var_5628], output)
mutated_mod['func_5629'] = func_5629
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5168_call = mod.get_global_var('func_5168')
func_5170_call = mutated_mod.get_global_var('func_5170')
call_5643 = relay.TupleGetItem(func_5168_call(), 0)
call_5644 = relay.TupleGetItem(func_5170_call(), 0)
output = call_5643
output2 = call_5644
func_5649 = relay.Function([], output)
mod['func_5649'] = func_5649
mod = relay.transform.InferType()(mod)
mutated_mod['func_5649'] = func_5649
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5649_call = mutated_mod.get_global_var('func_5649')
call_5650 = func_5649_call()
output = call_5650
func_5651 = relay.Function([], output)
mutated_mod['func_5651'] = func_5651
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1615_call = mod.get_global_var('func_1615')
func_1616_call = mutated_mod.get_global_var('func_1616')
call_5695 = func_1615_call()
call_5696 = func_1615_call()
func_2584_call = mod.get_global_var('func_2584')
func_2585_call = mutated_mod.get_global_var('func_2585')
call_5697 = relay.TupleGetItem(func_2584_call(), 0)
call_5698 = relay.TupleGetItem(func_2585_call(), 0)
output = relay.Tuple([call_5695,call_5697,])
output2 = relay.Tuple([call_5696,call_5698,])
func_5707 = relay.Function([], output)
mod['func_5707'] = func_5707
mod = relay.transform.InferType()(mod)
output = func_5707()
func_5708 = relay.Function([], output)
mutated_mod['func_5708'] = func_5708
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2716_call = mod.get_global_var('func_2716')
func_2717_call = mutated_mod.get_global_var('func_2717')
call_5716 = relay.TupleGetItem(func_2716_call(), 1)
call_5717 = relay.TupleGetItem(func_2717_call(), 1)
output = relay.Tuple([call_5716,])
output2 = relay.Tuple([call_5717,])
func_5719 = relay.Function([], output)
mod['func_5719'] = func_5719
mod = relay.transform.InferType()(mod)
output = func_5719()
func_5720 = relay.Function([], output)
mutated_mod['func_5720'] = func_5720
mutated_mod = relay.transform.InferType()(mutated_mod)
func_322_call = mod.get_global_var('func_322')
func_323_call = mutated_mod.get_global_var('func_323')
call_5745 = relay.TupleGetItem(func_322_call(), 0)
call_5746 = relay.TupleGetItem(func_323_call(), 0)
output = relay.Tuple([call_5745,])
output2 = relay.Tuple([call_5746,])
func_5751 = relay.Function([], output)
mod['func_5751'] = func_5751
mod = relay.transform.InferType()(mod)
mutated_mod['func_5751'] = func_5751
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5751_call = mutated_mod.get_global_var('func_5751')
call_5752 = func_5751_call()
output = call_5752
func_5753 = relay.Function([], output)
mutated_mod['func_5753'] = func_5753
mutated_mod = relay.transform.InferType()(mutated_mod)
func_257_call = mod.get_global_var('func_257')
func_259_call = mutated_mod.get_global_var('func_259')
call_5760 = relay.TupleGetItem(func_257_call(), 0)
call_5761 = relay.TupleGetItem(func_259_call(), 0)
func_1404_call = mod.get_global_var('func_1404')
func_1407_call = mutated_mod.get_global_var('func_1407')
const_5792 = relay.const([False,False,True,False,True,False,True,False,True,True,False,True,False,True,False,False,True,False,True,True,True,False,True,True,True,True,True,False,True,True,False,True,True,True,True,True,True,False,True,False,True,True,True,False,False,True,False,False,True,True,True,False,True,False,False,False], dtype = "bool")#candidate|5792|(56,)|const|bool
call_5791 = relay.TupleGetItem(func_1404_call(relay.reshape(const_5792.astype('bool'), [14, 1, 4])), 3)
call_5793 = relay.TupleGetItem(func_1407_call(relay.reshape(const_5792.astype('bool'), [14, 1, 4])), 3)
func_1550_call = mod.get_global_var('func_1550')
func_1552_call = mutated_mod.get_global_var('func_1552')
call_5809 = relay.TupleGetItem(func_1550_call(), 0)
call_5810 = relay.TupleGetItem(func_1552_call(), 0)
func_5168_call = mod.get_global_var('func_5168')
func_5170_call = mutated_mod.get_global_var('func_5170')
call_5814 = relay.TupleGetItem(func_5168_call(), 0)
call_5815 = relay.TupleGetItem(func_5170_call(), 0)
func_4536_call = mod.get_global_var('func_4536')
func_4537_call = mutated_mod.get_global_var('func_4537')
call_5817 = relay.TupleGetItem(func_4536_call(), 0)
call_5818 = relay.TupleGetItem(func_4537_call(), 0)
output = relay.Tuple([call_5760,call_5791,const_5792,call_5809,call_5814,call_5817,])
output2 = relay.Tuple([call_5761,call_5793,const_5792,call_5810,call_5815,call_5818,])
func_5820 = relay.Function([], output)
mod['func_5820'] = func_5820
mod = relay.transform.InferType()(mod)
output = func_5820()
func_5821 = relay.Function([], output)
mutated_mod['func_5821'] = func_5821
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5827 = relay.var("var_5827", dtype = "bool", shape = (10, 6, 12))#candidate|5827|(10, 6, 12)|var|bool
const_5828 = relay.const([[[False,False,True,True,True,True,False,True,False,True,False,True],[True,False,True,True,False,False,True,True,False,True,True,True],[True,False,True,False,True,False,False,True,False,True,False,True],[False,True,True,False,False,True,True,False,True,False,True,False],[True,True,True,True,False,False,True,True,False,False,True,True],[False,True,False,False,True,False,False,True,True,True,False,False]],[[False,True,False,False,False,True,False,True,False,True,False,True],[True,True,False,True,True,False,False,True,True,False,False,False],[False,False,False,False,True,False,False,True,True,False,True,True],[True,True,False,False,False,True,True,True,False,True,False,False],[True,False,True,True,False,True,True,True,True,True,True,False],[True,True,False,True,True,True,False,False,True,True,False,True]],[[False,True,True,False,True,True,False,False,False,False,True,False],[True,True,True,True,False,False,True,False,True,True,True,False],[True,True,True,False,False,True,True,False,True,False,True,False],[False,True,False,False,True,False,False,True,True,False,False,True],[False,True,True,False,True,False,False,False,False,True,False,False],[True,True,True,False,False,False,False,False,True,False,False,True]],[[False,False,False,True,False,False,True,True,True,False,True,False],[True,True,False,True,True,False,True,False,False,False,False,False],[False,False,False,False,False,False,True,True,False,True,False,True],[True,True,False,False,False,True,True,True,False,True,False,True],[False,True,True,False,False,True,False,False,True,False,False,False],[False,True,True,False,False,True,True,True,True,True,False,True]],[[False,True,False,True,False,False,False,False,True,False,False,True],[True,False,False,True,False,False,True,False,False,False,True,False],[True,False,False,False,False,False,True,False,True,True,True,True],[True,False,False,True,False,False,False,True,True,False,False,True],[True,True,False,True,True,True,True,True,True,True,True,True],[True,True,False,False,False,True,False,False,True,False,True,True]],[[False,True,True,True,False,True,True,True,True,True,False,False],[False,True,True,True,True,True,True,False,False,True,True,False],[False,True,False,False,True,True,True,True,True,False,True,True],[False,False,False,True,True,False,True,True,True,True,False,False],[False,True,True,False,False,False,False,True,True,True,True,False],[False,False,True,True,True,False,False,True,False,False,False,True]],[[False,True,False,False,False,True,False,False,False,True,False,True],[True,True,False,False,False,True,False,False,True,False,False,False],[False,False,True,True,True,True,False,True,True,True,True,True],[False,False,False,False,True,False,True,True,True,True,True,True],[False,False,False,False,False,False,False,False,False,False,True,True],[True,False,True,False,True,False,False,True,False,False,True,False]],[[False,True,True,False,False,False,True,True,False,True,True,False],[True,True,True,False,True,False,True,True,False,False,True,True],[True,True,False,True,True,False,True,False,True,False,False,True],[True,True,False,True,True,True,False,False,True,True,False,False],[True,False,True,False,False,True,True,True,False,False,True,False],[False,False,False,True,True,False,False,False,True,True,True,False]],[[False,True,True,True,False,True,False,False,True,True,False,False],[False,True,True,True,True,False,True,True,True,True,False,False],[True,True,False,False,False,True,True,False,True,False,False,True],[True,False,True,True,True,True,True,False,True,False,True,False],[True,False,False,False,True,False,False,False,True,False,False,True],[True,True,False,False,True,False,False,True,False,True,False,True]],[[True,True,True,False,True,False,False,False,False,False,False,True],[True,False,True,False,False,False,False,False,True,False,False,True],[False,False,False,False,False,False,True,True,True,True,True,False],[True,True,True,False,False,True,True,True,False,True,True,False],[True,True,False,False,True,True,True,True,True,True,True,True],[True,True,False,False,False,True,True,True,True,False,True,True]]], dtype = "bool")#candidate|5828|(10, 6, 12)|const|bool
bop_5829 = relay.logical_or(var_5827.astype('bool'), relay.reshape(const_5828.astype('bool'), relay.shape_of(var_5827))) # shape=(10, 6, 12)
output = bop_5829
output2 = bop_5829
func_5832 = relay.Function([var_5827,], output)
mod['func_5832'] = func_5832
mod = relay.transform.InferType()(mod)
var_5833 = relay.var("var_5833", dtype = "bool", shape = (10, 6, 12))#candidate|5833|(10, 6, 12)|var|bool
output = func_5832(var_5833)
func_5834 = relay.Function([var_5833], output)
mutated_mod['func_5834'] = func_5834
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5035_call = mod.get_global_var('func_5035')
func_5036_call = mutated_mod.get_global_var('func_5036')
call_5844 = relay.TupleGetItem(func_5035_call(), 0)
call_5845 = relay.TupleGetItem(func_5036_call(), 0)
func_1896_call = mod.get_global_var('func_1896')
func_1898_call = mutated_mod.get_global_var('func_1898')
call_5853 = relay.TupleGetItem(func_1896_call(), 0)
call_5854 = relay.TupleGetItem(func_1898_call(), 0)
bop_5856 = relay.maximum(call_5844.astype('uint8'), relay.reshape(call_5853.astype('uint8'), relay.shape_of(call_5844))) # shape=(3, 4, 8)
bop_5859 = relay.maximum(call_5845.astype('uint8'), relay.reshape(call_5854.astype('uint8'), relay.shape_of(call_5845))) # shape=(3, 4, 8)
output = relay.Tuple([bop_5856,])
output2 = relay.Tuple([bop_5859,])
func_5864 = relay.Function([], output)
mod['func_5864'] = func_5864
mod = relay.transform.InferType()(mod)
output = func_5864()
func_5865 = relay.Function([], output)
mutated_mod['func_5865'] = func_5865
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2827_call = mod.get_global_var('func_2827')
func_2828_call = mutated_mod.get_global_var('func_2828')
call_5872 = func_2827_call()
call_5873 = func_2827_call()
output = call_5872
output2 = call_5873
func_5883 = relay.Function([], output)
mod['func_5883'] = func_5883
mod = relay.transform.InferType()(mod)
mutated_mod['func_5883'] = func_5883
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5883_call = mutated_mod.get_global_var('func_5883')
call_5884 = func_5883_call()
output = call_5884
func_5885 = relay.Function([], output)
mutated_mod['func_5885'] = func_5885
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5886 = relay.var("var_5886", dtype = "float64", shape = (6, 10, 8))#candidate|5886|(6, 10, 8)|var|float64
const_5887 = relay.const([[[9.876160,-3.195299,-9.338407,-1.180282,-2.899256,6.803415,-9.054939,-7.779391],[-1.688847,-7.357972,-7.383934,-7.703284,-0.190346,9.000123,-9.767401,-2.328968],[7.549368,2.108325,4.441948,7.005587,-3.738873,-3.339112,2.673575,4.500340],[-7.766676,-3.739223,-0.788609,-0.744156,1.257991,2.244273,-9.915227,5.412571],[-6.295393,0.224069,5.216780,-6.443250,6.983289,-7.752204,8.053848,-4.303822],[9.196525,-5.526324,5.024041,6.261857,-4.635488,-9.269274,-7.742682,-9.796611],[8.873108,2.682345,-5.953505,-2.572532,-2.659114,5.003501,-5.277830,1.069795],[-3.116260,3.839318,-8.524340,9.431722,-7.522597,3.819208,4.107028,4.355548],[1.868511,6.146814,-4.880560,2.400796,9.285667,-5.966489,-3.083785,4.354725],[-4.633002,8.393123,2.408598,5.599493,-9.774624,8.386682,5.138869,-5.516468]],[[5.987361,-8.869573,3.921744,-4.911763,-5.402326,-6.296225,-5.472004,-7.607757],[0.669187,-8.606589,-2.700693,-1.107649,-4.302271,-0.630822,-6.819779,4.080462],[1.864634,-5.364833,3.003742,2.675985,3.856511,8.816512,4.927329,-5.294003],[7.243031,-2.670437,2.093490,-2.113087,-8.258779,8.835257,-2.814871,-3.566865],[-8.539516,-1.859175,8.429638,-9.883201,-8.355788,-5.274981,3.990238,-1.820023],[6.795318,-7.216057,7.566031,6.529725,3.082699,-0.353711,0.171462,6.551967],[6.868089,5.943904,2.470544,-6.966369,6.332057,-6.996220,3.067568,1.736578],[6.012018,5.023767,0.698837,-7.206923,7.034507,-3.898239,4.777669,5.303926],[9.610129,5.782132,-9.131430,-4.205408,-2.855645,-9.776566,5.539533,5.190875],[5.769938,4.413626,7.536291,3.744519,8.956321,5.465619,-6.358813,7.970947]],[[2.144289,-3.393688,-7.471463,-5.128598,1.033599,3.392343,-7.984851,0.701881],[6.535101,-6.922509,-5.071281,-2.838355,7.692630,-7.492881,-2.848357,-1.079011],[-4.625911,2.433145,0.822665,-9.254066,-1.772416,-8.343413,-5.256440,-6.488459],[-8.873657,-2.264168,-6.228973,-5.145113,-1.754735,4.196666,3.266147,-4.419481],[1.352665,-9.746341,4.220703,8.686562,-5.502936,4.255802,-8.224905,5.868365],[-2.186418,6.081895,-2.837758,4.585190,8.408353,4.684535,-0.278214,-2.742217],[9.235114,-5.634820,8.818571,-7.764659,4.921729,-4.252187,6.938370,2.909570],[4.939928,-3.116838,-3.829084,-8.610460,1.676262,-4.013858,-3.240297,4.655490],[-0.904914,-5.015327,2.847884,9.081886,-1.646334,-8.944972,3.541204,-6.159326],[9.254561,-9.425188,-3.558956,5.702050,-8.661421,6.428785,-2.541202,-6.664503]],[[-9.253777,3.200277,3.093440,2.622219,-7.630096,4.123453,2.967648,8.229018],[1.487628,-9.951079,-2.312804,3.208429,-9.078878,2.812881,5.772865,5.511732],[4.304007,2.438534,4.260907,-3.112986,9.023514,-5.756038,5.023619,3.910854],[4.305129,-0.630930,9.267519,7.198182,-0.756710,-1.243408,-3.618346,-6.678861],[-1.128563,7.310993,-7.388405,-9.785703,0.623414,-4.858671,-1.071540,4.124295],[9.495641,0.082809,8.700300,-9.492617,-9.036889,3.088212,-1.003169,-0.290756],[-7.150123,0.665437,5.185771,-5.290739,-7.448676,-2.496741,-2.491844,-8.634177],[5.082502,-4.104116,-2.262855,1.090473,4.716748,-9.132905,-2.921961,7.992486],[-4.484320,4.330770,-9.504531,-7.818259,-8.545045,4.908893,4.251782,-4.004594],[8.271600,6.844923,-4.081584,-1.904965,-3.302889,0.300485,1.255798,7.364447]],[[3.727862,-1.817578,-1.624387,-5.973949,1.399148,9.513685,-1.193474,7.900457],[-8.240302,4.678626,9.133626,-5.659367,-1.912311,-6.352080,-5.541730,7.794598],[-6.006288,3.662216,7.975498,5.841617,2.341665,7.679422,0.244320,-0.909016],[8.854138,-3.361385,0.322395,-3.855052,-7.095360,-2.266941,-4.566031,2.281615],[1.216095,0.172022,-0.460040,8.617258,5.191294,6.068390,3.155898,-6.984201],[-3.975856,-0.735133,-4.957964,9.732040,3.921155,3.548897,-1.639938,5.397282],[-6.395886,-7.115452,0.422908,-3.324437,-7.262236,5.885272,3.374847,-2.448570],[-3.075094,-3.897154,-8.606328,-9.291055,1.907113,6.118833,-3.858503,5.394552],[-1.942440,1.575700,0.990953,-5.612144,-1.811258,7.982541,-4.318191,1.759621],[-4.668575,0.656064,0.669083,3.832239,2.635944,-7.905408,9.885185,-4.654601]],[[1.226524,2.418300,-3.098052,-1.046930,-5.047240,-3.626461,-8.094400,1.945816],[6.960769,8.813697,-8.511248,1.642358,1.894579,3.352552,1.819429,-4.041289],[-7.096287,2.635678,-5.310623,4.272043,-8.660410,5.655730,7.141278,9.932165],[1.938112,4.266941,3.385629,2.646043,6.134002,3.877312,7.832031,9.489796],[-1.066496,-0.247612,6.992765,0.169510,8.235473,-6.925896,7.553561,-6.830578],[-5.912851,3.869001,-6.595178,-5.457859,0.367992,6.518205,-4.667288,-0.442683],[5.047572,0.489161,-4.217989,-9.143168,1.828644,-9.211042,8.537068,0.011620],[4.667268,5.199626,9.996420,1.782967,-1.219168,6.515910,3.724418,4.747264],[-9.895001,6.121671,2.782368,0.257413,-4.633591,4.318008,-3.272084,2.382749],[0.524037,5.349062,4.701607,-6.398733,2.651495,-1.900272,6.893616,-4.665915]]], dtype = "float64")#candidate|5887|(6, 10, 8)|const|float64
bop_5888 = relay.not_equal(var_5886.astype('bool'), relay.reshape(const_5887.astype('bool'), relay.shape_of(var_5886))) # shape=(6, 10, 8)
func_4051_call = mod.get_global_var('func_4051')
func_4052_call = mutated_mod.get_global_var('func_4052')
call_5891 = func_4051_call()
call_5892 = func_4051_call()
uop_5899 = relay.sinh(bop_5888.astype('float32')) # shape=(6, 10, 8)
output = relay.Tuple([call_5891,uop_5899,])
output2 = relay.Tuple([call_5892,uop_5899,])
func_5903 = relay.Function([var_5886,], output)
mod['func_5903'] = func_5903
mod = relay.transform.InferType()(mod)
var_5904 = relay.var("var_5904", dtype = "float64", shape = (6, 10, 8))#candidate|5904|(6, 10, 8)|var|float64
output = func_5903(var_5904)
func_5905 = relay.Function([var_5904], output)
mutated_mod['func_5905'] = func_5905
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5336_call = mod.get_global_var('func_5336')
func_5337_call = mutated_mod.get_global_var('func_5337')
call_5907 = func_5336_call()
call_5908 = func_5336_call()
output = call_5907
output2 = call_5908
func_5924 = relay.Function([], output)
mod['func_5924'] = func_5924
mod = relay.transform.InferType()(mod)
mutated_mod['func_5924'] = func_5924
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5924_call = mutated_mod.get_global_var('func_5924')
call_5925 = func_5924_call()
output = call_5925
func_5926 = relay.Function([], output)
mutated_mod['func_5926'] = func_5926
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4536_call = mod.get_global_var('func_4536')
func_4537_call = mutated_mod.get_global_var('func_4537')
call_5997 = relay.TupleGetItem(func_4536_call(), 0)
call_5998 = relay.TupleGetItem(func_4537_call(), 0)
func_2584_call = mod.get_global_var('func_2584')
func_2585_call = mutated_mod.get_global_var('func_2585')
call_6003 = relay.TupleGetItem(func_2584_call(), 0)
call_6004 = relay.TupleGetItem(func_2585_call(), 0)
func_5134_call = mod.get_global_var('func_5134')
func_5136_call = mutated_mod.get_global_var('func_5136')
const_6016 = relay.const([6.250253,5.057318,2.776930,-2.906657,9.933161,7.711930,-2.026389,3.286679,6.907653,3.435798,-9.862180,5.689822,-5.009368,0.613057,-8.858182,-5.524463,6.876912,5.573990,-6.523372,-1.137049,-8.977410,-6.736836,-6.994735,-6.208303,-4.901998,-9.408963,-0.705308,-6.644999,-2.371819,-7.723537,-6.532410,-8.127360,-2.000549,-8.148777,8.699881,-2.416164,1.454676,-6.531872,0.989951,3.672161,-1.251396,-6.946701,1.059090,6.292369,-3.585181,-3.215744,1.214243,-6.197440,-5.968531,-7.703914,-3.893843,1.590829,4.338218,9.206853,2.436851,7.886127,-2.936244,-5.530817,-8.149083,3.605059,4.047486,8.384842,-3.500680,9.219661,-3.405384,3.484811,-7.138719,-7.021555,-9.065789,-7.276851,-4.043414,-9.979795,6.966013,3.971155,-5.848496,0.767040,-0.332600,-1.457637,-3.974358,-9.961003,-9.689289,3.418402,-7.612990,-8.409479,-7.069474,-3.709781,-2.556892,1.061810,1.799174,3.175104,-0.473187], dtype = "float64")#candidate|6016|(91,)|const|float64
call_6015 = relay.TupleGetItem(func_5134_call(relay.reshape(const_6016.astype('float64'), [1, 13, 7])), 0)
call_6017 = relay.TupleGetItem(func_5136_call(relay.reshape(const_6016.astype('float64'), [1, 13, 7])), 0)
var_6024 = relay.var("var_6024", dtype = "float64", shape = (91,))#candidate|6024|(91,)|var|float64
bop_6025 = relay.left_shift(const_6016.astype('int16'), relay.reshape(var_6024.astype('int16'), relay.shape_of(const_6016))) # shape=(91,)
uop_6028 = relay.asinh(var_6024.astype('float64')) # shape=(91,)
output = relay.Tuple([call_5997,call_6003,call_6015,bop_6025,uop_6028,])
output2 = relay.Tuple([call_5998,call_6004,call_6017,bop_6025,uop_6028,])
func_6039 = relay.Function([var_6024,], output)
mod['func_6039'] = func_6039
mod = relay.transform.InferType()(mod)
var_6040 = relay.var("var_6040", dtype = "float64", shape = (91,))#candidate|6040|(91,)|var|float64
output = func_6039(var_6040)
func_6041 = relay.Function([var_6040], output)
mutated_mod['func_6041'] = func_6041
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6065 = relay.var("var_6065", dtype = "float32", shape = (1, 13, 3))#candidate|6065|(1, 13, 3)|var|float32
uop_6066 = relay.sigmoid(var_6065.astype('float32')) # shape=(1, 13, 3)
var_6086 = relay.var("var_6086", dtype = "float32", shape = (2, 13, 3))#candidate|6086|(2, 13, 3)|var|float32
bop_6087 = relay.minimum(uop_6066.astype('int32'), var_6086.astype('int32')) # shape=(2, 13, 3)
output = relay.Tuple([bop_6087,])
output2 = relay.Tuple([bop_6087,])
func_6103 = relay.Function([var_6065,var_6086,], output)
mod['func_6103'] = func_6103
mod = relay.transform.InferType()(mod)
mutated_mod['func_6103'] = func_6103
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6103_call = mutated_mod.get_global_var('func_6103')
var_6105 = relay.var("var_6105", dtype = "float32", shape = (1, 13, 3))#candidate|6105|(1, 13, 3)|var|float32
var_6106 = relay.var("var_6106", dtype = "float32", shape = (2, 13, 3))#candidate|6106|(2, 13, 3)|var|float32
call_6104 = func_6103_call(var_6105,var_6106,)
output = call_6104
func_6107 = relay.Function([var_6105,var_6106,], output)
mutated_mod['func_6107'] = func_6107
mutated_mod = relay.transform.InferType()(mutated_mod)
func_858_call = mod.get_global_var('func_858')
func_859_call = mutated_mod.get_global_var('func_859')
call_6175 = relay.TupleGetItem(func_858_call(), 1)
call_6176 = relay.TupleGetItem(func_859_call(), 1)
func_5820_call = mod.get_global_var('func_5820')
func_5821_call = mutated_mod.get_global_var('func_5821')
call_6192 = relay.TupleGetItem(func_5820_call(), 2)
call_6193 = relay.TupleGetItem(func_5821_call(), 2)
output = relay.Tuple([call_6175,call_6192,])
output2 = relay.Tuple([call_6176,call_6193,])
func_6207 = relay.Function([], output)
mod['func_6207'] = func_6207
mod = relay.transform.InferType()(mod)
output = func_6207()
func_6208 = relay.Function([], output)
mutated_mod['func_6208'] = func_6208
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5883_call = mod.get_global_var('func_5883')
func_5885_call = mutated_mod.get_global_var('func_5885')
call_6220 = func_5883_call()
call_6221 = func_5883_call()
func_5134_call = mod.get_global_var('func_5134')
func_5136_call = mutated_mod.get_global_var('func_5136')
const_6223 = relay.const([7.451684,-9.303036,-1.963371,-9.036599,-6.586891,-0.886037,5.670651,6.176226,-5.289231,-3.368748,-5.635089,7.320953,2.549244,-2.246428,-9.176335,-7.558056,-5.957254,-1.513843,-7.758939,9.141398,-4.318578,-0.690992,-2.441505,-2.348134,7.766170,4.176243,9.668906,-4.996593,-4.974437,1.919854,-4.790466,-1.425092,-6.075533,9.214531,-3.745235,2.084951,-1.368076,-0.420738,5.420173,7.839392,2.670239,2.096698,3.721398,6.324137,-6.666570,2.424891,-0.953327,2.055276,-9.969236,5.863274,-0.346164,5.014713,-4.429076,1.240415,-4.765767,-8.056073,6.069806,-4.988155,3.222900,6.840895,-2.382254,-8.244878,-7.650805,-7.453740,5.987533,8.760132,-1.185823,-7.855262,-3.947187,6.627931,2.772726,-9.339110,3.675911,3.769388,8.727734,-0.527687,1.833897,-4.076506,3.832979,1.179222,1.375679,-4.725368,1.414704,-9.267013,-9.751718,0.866922,-8.803451,-1.828265,-1.968262,-6.485264,-9.593944], dtype = "float64")#candidate|6223|(91,)|const|float64
call_6222 = relay.TupleGetItem(func_5134_call(relay.reshape(const_6223.astype('float64'), [1, 13, 7])), 1)
call_6224 = relay.TupleGetItem(func_5136_call(relay.reshape(const_6223.astype('float64'), [1, 13, 7])), 1)
output = relay.Tuple([call_6220,call_6222,const_6223,])
output2 = relay.Tuple([call_6221,call_6224,const_6223,])
func_6238 = relay.Function([], output)
mod['func_6238'] = func_6238
mod = relay.transform.InferType()(mod)
mutated_mod['func_6238'] = func_6238
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6238_call = mutated_mod.get_global_var('func_6238')
call_6239 = func_6238_call()
output = call_6239
func_6240 = relay.Function([], output)
mutated_mod['func_6240'] = func_6240
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3932_call = mod.get_global_var('func_3932')
func_3934_call = mutated_mod.get_global_var('func_3934')
call_6243 = func_3932_call()
call_6244 = func_3932_call()
func_1531_call = mod.get_global_var('func_1531')
func_1533_call = mutated_mod.get_global_var('func_1533')
call_6247 = relay.TupleGetItem(func_1531_call(), 0)
call_6248 = relay.TupleGetItem(func_1533_call(), 0)
func_557_call = mod.get_global_var('func_557')
func_558_call = mutated_mod.get_global_var('func_558')
call_6251 = relay.TupleGetItem(func_557_call(), 0)
call_6252 = relay.TupleGetItem(func_558_call(), 0)
func_4638_call = mod.get_global_var('func_4638')
func_4640_call = mutated_mod.get_global_var('func_4640')
call_6272 = func_4638_call()
call_6273 = func_4638_call()
func_148_call = mod.get_global_var('func_148')
func_150_call = mutated_mod.get_global_var('func_150')
call_6276 = relay.TupleGetItem(func_148_call(), 0)
call_6277 = relay.TupleGetItem(func_150_call(), 0)
output = relay.Tuple([call_6243,call_6247,call_6251,call_6272,call_6276,])
output2 = relay.Tuple([call_6244,call_6248,call_6252,call_6273,call_6277,])
func_6279 = relay.Function([], output)
mod['func_6279'] = func_6279
mod = relay.transform.InferType()(mod)
mutated_mod['func_6279'] = func_6279
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6279_call = mutated_mod.get_global_var('func_6279')
call_6280 = func_6279_call()
output = call_6280
func_6281 = relay.Function([], output)
mutated_mod['func_6281'] = func_6281
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6329 = relay.var("var_6329", dtype = "int8", shape = (12, 14, 12))#candidate|6329|(12, 14, 12)|var|int8
var_6330 = relay.var("var_6330", dtype = "int8", shape = (12, 14, 12))#candidate|6330|(12, 14, 12)|var|int8
bop_6331 = relay.add(var_6329.astype('int8'), relay.reshape(var_6330.astype('int8'), relay.shape_of(var_6329))) # shape=(12, 14, 12)
output = relay.Tuple([bop_6331,])
output2 = relay.Tuple([bop_6331,])
func_6361 = relay.Function([var_6329,var_6330,], output)
mod['func_6361'] = func_6361
mod = relay.transform.InferType()(mod)
var_6362 = relay.var("var_6362", dtype = "int8", shape = (12, 14, 12))#candidate|6362|(12, 14, 12)|var|int8
var_6363 = relay.var("var_6363", dtype = "int8", shape = (12, 14, 12))#candidate|6363|(12, 14, 12)|var|int8
output = func_6361(var_6362,var_6363,)
func_6364 = relay.Function([var_6362,var_6363,], output)
mutated_mod['func_6364'] = func_6364
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6407 = relay.var("var_6407", dtype = "uint64", shape = (1, 10, 9))#candidate|6407|(1, 10, 9)|var|uint64
var_6408 = relay.var("var_6408", dtype = "uint64", shape = (13, 10, 9))#candidate|6408|(13, 10, 9)|var|uint64
bop_6409 = relay.right_shift(var_6407.astype('uint64'), var_6408.astype('uint64')) # shape=(13, 10, 9)
output = bop_6409
output2 = bop_6409
func_6416 = relay.Function([var_6407,var_6408,], output)
mod['func_6416'] = func_6416
mod = relay.transform.InferType()(mod)
mutated_mod['func_6416'] = func_6416
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6416_call = mutated_mod.get_global_var('func_6416')
var_6418 = relay.var("var_6418", dtype = "uint64", shape = (1, 10, 9))#candidate|6418|(1, 10, 9)|var|uint64
var_6419 = relay.var("var_6419", dtype = "uint64", shape = (13, 10, 9))#candidate|6419|(13, 10, 9)|var|uint64
call_6417 = func_6416_call(var_6418,var_6419,)
output = call_6417
func_6420 = relay.Function([var_6418,var_6419,], output)
mutated_mod['func_6420'] = func_6420
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2054_call = mod.get_global_var('func_2054')
func_2056_call = mutated_mod.get_global_var('func_2056')
call_6475 = relay.TupleGetItem(func_2054_call(), 0)
call_6476 = relay.TupleGetItem(func_2056_call(), 0)
output = call_6475
output2 = call_6476
func_6505 = relay.Function([], output)
mod['func_6505'] = func_6505
mod = relay.transform.InferType()(mod)
output = func_6505()
func_6506 = relay.Function([], output)
mutated_mod['func_6506'] = func_6506
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2606_call = mod.get_global_var('func_2606')
func_2608_call = mutated_mod.get_global_var('func_2608')
call_6538 = relay.TupleGetItem(func_2606_call(), 0)
call_6539 = relay.TupleGetItem(func_2608_call(), 0)
func_1404_call = mod.get_global_var('func_1404')
func_1407_call = mutated_mod.get_global_var('func_1407')
const_6552 = relay.const([True,True,False,True,True,False,True,True,True,False,True,False,False,True,True,True,False,False,False,False,True,False,False,True,False,True,False,False,False,True,False,True,False,False,True,True,False,False,False,False,False,True,False,True,True,True,False,True,True,False,True,True,False,True,False,False], dtype = "bool")#candidate|6552|(56,)|const|bool
call_6551 = relay.TupleGetItem(func_1404_call(relay.reshape(const_6552.astype('bool'), [14, 1, 4])), 2)
call_6553 = relay.TupleGetItem(func_1407_call(relay.reshape(const_6552.astype('bool'), [14, 1, 4])), 2)
output = relay.Tuple([call_6538,call_6551,const_6552,])
output2 = relay.Tuple([call_6539,call_6553,const_6552,])
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
func_1498_call = mod.get_global_var('func_1498')
func_1499_call = mutated_mod.get_global_var('func_1499')
call_6584 = relay.TupleGetItem(func_1498_call(), 1)
call_6585 = relay.TupleGetItem(func_1499_call(), 1)
output = relay.Tuple([call_6584,])
output2 = relay.Tuple([call_6585,])
func_6609 = relay.Function([], output)
mod['func_6609'] = func_6609
mod = relay.transform.InferType()(mod)
output = func_6609()
func_6610 = relay.Function([], output)
mutated_mod['func_6610'] = func_6610
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4003_call = mod.get_global_var('func_4003')
func_4004_call = mutated_mod.get_global_var('func_4004')
call_6649 = relay.TupleGetItem(func_4003_call(), 0)
call_6650 = relay.TupleGetItem(func_4004_call(), 0)
func_5627_call = mod.get_global_var('func_5627')
func_5629_call = mutated_mod.get_global_var('func_5629')
var_6652 = relay.var("var_6652", dtype = "bool", shape = (120, 4))#candidate|6652|(120, 4)|var|bool
call_6651 = relay.TupleGetItem(func_5627_call(relay.reshape(var_6652.astype('bool'), [6, 5, 16])), 1)
call_6653 = relay.TupleGetItem(func_5629_call(relay.reshape(var_6652.astype('bool'), [6, 5, 16])), 1)
output = relay.Tuple([call_6649,call_6651,var_6652,])
output2 = relay.Tuple([call_6650,call_6653,var_6652,])
func_6656 = relay.Function([var_6652,], output)
mod['func_6656'] = func_6656
mod = relay.transform.InferType()(mod)
mutated_mod['func_6656'] = func_6656
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6657 = relay.var("var_6657", dtype = "bool", shape = (120, 4))#candidate|6657|(120, 4)|var|bool
func_6656_call = mutated_mod.get_global_var('func_6656')
call_6658 = func_6656_call(var_6657)
output = call_6658
func_6659 = relay.Function([var_6657], output)
mutated_mod['func_6659'] = func_6659
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4003_call = mod.get_global_var('func_4003')
func_4004_call = mutated_mod.get_global_var('func_4004')
call_6672 = relay.TupleGetItem(func_4003_call(), 0)
call_6673 = relay.TupleGetItem(func_4004_call(), 0)
output = call_6672
output2 = call_6673
func_6699 = relay.Function([], output)
mod['func_6699'] = func_6699
mod = relay.transform.InferType()(mod)
mutated_mod['func_6699'] = func_6699
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6699_call = mutated_mod.get_global_var('func_6699')
call_6700 = func_6699_call()
output = call_6700
func_6701 = relay.Function([], output)
mutated_mod['func_6701'] = func_6701
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6732 = relay.var("var_6732", dtype = "uint16", shape = ())#candidate|6732|()|var|uint16
var_6733 = relay.var("var_6733", dtype = "uint16", shape = (16, 9, 6))#candidate|6733|(16, 9, 6)|var|uint16
bop_6734 = relay.add(var_6732.astype('uint16'), var_6733.astype('uint16')) # shape=(16, 9, 6)
func_557_call = mod.get_global_var('func_557')
func_558_call = mutated_mod.get_global_var('func_558')
call_6747 = relay.TupleGetItem(func_557_call(), 1)
call_6748 = relay.TupleGetItem(func_558_call(), 1)
func_5719_call = mod.get_global_var('func_5719')
func_5720_call = mutated_mod.get_global_var('func_5720')
call_6752 = relay.TupleGetItem(func_5719_call(), 0)
call_6753 = relay.TupleGetItem(func_5720_call(), 0)
func_6609_call = mod.get_global_var('func_6609')
func_6610_call = mutated_mod.get_global_var('func_6610')
call_6757 = relay.TupleGetItem(func_6609_call(), 0)
call_6758 = relay.TupleGetItem(func_6610_call(), 0)
func_5358_call = mod.get_global_var('func_5358')
func_5361_call = mutated_mod.get_global_var('func_5361')
const_6765 = relay.const([[3.645335,-6.923467,-4.070062,6.888194,-7.212126,2.852925,-1.869748,8.904618,-1.380511,-8.307090,-3.078796,4.567179,8.649706,-8.672612,8.129771,-4.818193,3.286023,-5.645809,6.746697,6.809430,9.167296,-0.226749,3.270120,-8.614884,3.077923,-8.831580,-5.378156,9.185687,0.811184,0.529409,-9.457430,2.911938,-8.763041,7.750598,8.528437,-4.017185,7.638953,-9.169507,-6.575605,-8.024737,2.862849,-1.987873,-2.790124,7.647467,6.500023,-6.026091,-0.116780,6.410885,3.213964,4.394343,1.141537,-6.634292,-5.471400,0.066716,6.438412,2.717557,2.201980,-2.720427,9.320316,2.871008,-2.421800,-6.160165,0.091411,-8.614710,-6.743541,3.197802,3.273762,-7.896539,-8.854605,-2.470710,2.253955,-0.530364,2.763201,-1.056991,-6.475570,7.978241,-3.690259,2.959949,-3.243508,-1.504588,7.398780,-6.007423,5.061934,5.868870,2.976866,-2.611425,5.535434,7.518892,3.520457,1.104451,2.455670,8.961759,0.853924,6.968264,-9.421296,-7.823822,8.027805,-7.031688,-2.056349,-5.214959,7.333853,-9.978414,9.646375,-8.356110,-9.248021,-6.236841,-5.672031,7.213492,-7.102767,9.627512,-7.304311,8.413050]], dtype = "float64")#candidate|6765|(1, 112)|const|float64
const_6766 = relay.const([6.446409,0.396738,-5.567039,5.041904,4.191126,-6.345318,9.535073,5.127657,-2.180663,2.681582,8.787601,8.524204,5.624689,8.119879,-2.913412,-1.405458,-3.618466,4.381667,6.649219,-6.850582,-9.702959,-4.004869,6.713238,2.158447,-0.864931,-3.334956,-7.178249,-4.093018,-2.670543,-6.840103,-5.006314,-5.582916,-9.488100,5.331972,-3.142456,-7.321218,-1.497780,6.211648,-6.969464,-0.372161,3.862694,-5.247692,-0.860002,9.723608,-9.668049,-1.997414,-6.799842,9.326863,-0.137898,3.176071,-5.857850,0.304744,-6.277673,-9.723988,6.585776,-8.549801,6.389957,-1.088851,4.145440,8.186098,5.634919,-7.862870,-9.886085,-5.832762,-2.485141,-8.068970,8.233080,5.753614,-7.645052,-2.809659,-5.629754,-5.536493,4.239733,-1.131345,6.950703,-7.154471,3.995293,-1.865000,-9.408339,-8.048165,-6.418778,1.246750,-5.865495,-3.552367,-3.533748,-9.513292,2.497322,9.946974,-4.945520,0.023924,6.355152,-9.418426,-7.046848,-2.868240,-4.937715,2.701553,2.042943,-2.685107,3.917754,-3.338106,-8.303825,7.724080,-3.139674,-2.527364,-9.260342,-4.064060,-9.547206,-0.688546,3.366203,2.914239,0.507350,1.369413,-7.509300,-8.903745,-1.938199,0.984495,8.220961,-9.782650,3.887095,-1.936808,-6.249678,8.534899,-8.833991,9.254604,7.998973,6.794315,6.353629,1.701092,-1.560180,6.921166,6.798296,3.232313,6.263557,-7.591591,3.617466,-3.339275,3.275617,-1.430179,6.497957,0.156235,-4.846726,2.128512,4.174086,5.881148,-7.960957,-6.796027,-7.298681,7.498912,7.086150,-6.419355,-0.514195,-5.220467,1.806816,0.423980,-4.556915,2.383865,4.843705,-8.163060,3.183762,9.688859,8.649262,8.616575,6.055721,0.069716,-2.133075,5.316198,8.756772,-3.487952,-2.568308,6.109420,9.429567,-3.490739,-9.630801,1.104663,-3.065707,0.449288,2.988046,4.043414,0.253802,2.793767,3.543471,5.396481,6.551452,8.857626,1.548936,-1.045862,6.694158,-4.711140,-3.054959,9.033081,-5.491103,-2.145537,-1.460689,-3.310303,-4.586644,6.976277,4.723925,-5.247540,3.205462,-4.525287,2.553075,5.285851,4.973473,-5.789941,3.968406,9.352970,-1.512397,6.978952,1.484162,6.781705,-0.532282,2.495344,4.535910,-0.507683,1.864506,8.242602,5.114026,6.597985,-1.107585,-2.368393,-9.463649,6.543760,7.955697,6.219793,2.656244,1.635508,1.025786,4.786016,-1.068329,9.863560,-9.849122,-0.193659,7.663000,1.794292,2.367030,-6.341555,4.023718,7.850863,-8.909446,8.912029,7.089865,0.143650,-6.179046,3.313533,-1.505037,-8.190248,0.732871,8.850319,8.136341,5.349732,-6.371883,-9.208871,3.225240,8.299295,-1.354062,7.176863,5.072319,-0.652262,6.742783,-8.596992,9.801869,6.147984,-9.904019,4.779409,3.684506,-9.460366,-3.281828,9.454801,-5.894714,-8.103504,8.764829,-9.746630,-7.463540,-4.048577,-5.181410,-3.444863,-7.536318,7.103570,-4.382577,-2.352054,8.318104,5.681817,1.796379,6.505714,9.500013,-3.388014,-3.543250,6.054329,3.884453,-2.556253,5.644913,7.930784,-0.576377,-1.987770,-4.825537,-5.162971,3.008116,3.358755,-1.964667,8.917126,-3.096387,3.461042,-1.866344,-8.574589,-5.033810,-4.245179,0.684647,2.106491,-5.700666,-5.202334,-8.780255,-6.932113,-8.513853,-5.071223,-0.976142,9.603050,8.141281,6.478732,2.945198,-4.724503,9.055767,3.721084,-7.576666,-4.468788,-3.788348,1.331356,-2.155038,2.522788,-0.715182,4.929568,5.190461,9.460385,3.458846,-5.731308,-0.455662,8.099047,3.500424,-4.326421,9.619966,-4.729712,5.268215,7.485303,0.377791,5.207870,-8.435626,0.911305,9.280745,5.388598,4.279842,6.181167,-5.006385,6.561052,-0.102348,6.928958,6.962529,9.999883,-8.332236,-1.717342,9.514064,0.424205,-4.875978,8.540025,5.878243,8.791497,4.307858,1.828717,3.190037,7.056859,-6.634324,2.093389,8.930991,3.217801,0.670308,2.789256,3.593852,4.544802,1.296520,4.876528,5.115512,-0.602309,5.463715,-9.233765,-0.430739,-9.308403,-7.636403,-0.215965,6.100268,3.379108,1.092814,4.966017,6.901297,9.130901,-1.605132,-4.179483,6.134786,-4.531170,-9.869858,6.158457,-5.511682,9.219716,2.326440,-4.944110,2.584114,-8.075629,3.740078,6.902895,-7.857129,4.854159,3.243644,-3.143933,-7.936676,-5.743192,0.339782,-6.645885,8.762192,-4.473468,2.027029,9.479344,1.228421,-8.076325,-3.195564,7.672149,-7.580143,8.879620,-4.425697,-8.915535,-7.237971,7.016591,-2.691266,6.979098,-7.315787,-1.359455,5.585304,-6.753516,1.101739,8.131156,1.970687,-3.017839,1.367774,7.770500,2.836971,3.554015,-9.527451,3.041821,-2.336529,9.395737,4.936626,-8.882910,6.244481,4.650463,6.212623,-3.407268,3.084779,-1.572105,-8.613410,8.015386,4.963637,2.024273,1.679849,-9.195164,-8.906072,-1.454318,-9.940591,-0.864520,-5.215902,-7.589716,-2.153423,-6.336683,-0.430749,-1.082414,-5.501325,-6.237367,-0.100289,-3.152993,8.551166,7.131275,-4.173979,4.830451,9.486145,-0.609717,3.268219,3.132487,-3.955061,3.745682,1.658883,9.604941,8.640012,7.134468,-0.753666,-1.368164,7.151170,8.889856,6.655609,-2.316665,-6.010227,-3.077342,4.069173,2.267434,7.569876,-8.131242,-7.727038,8.596029,-1.398108,-1.810644,-8.630529,-1.642741,-4.206459,2.669926,-4.530093,-8.993601,-4.429289,-6.901087,3.949951,9.720421,-1.907549,5.539541,-9.338107,6.161751,3.924147,4.504379,-0.175413,7.905804,6.040071,-2.226292,-6.449597,-8.355097,-7.920518,2.418882,-3.269860,-5.508617,-9.334558,4.265938,-1.308177,5.619156,-5.415291,2.516662,-1.354739,-4.266363,3.231401,4.632001,6.904645,6.841733,-4.181287,5.605829,5.336322,-1.444601,1.576901,-6.844750,-3.262200,-1.192061,-8.440501,7.217415,-2.198301,-3.298270,-4.890732,-1.809125,0.334505,2.311135,-2.650378,-7.648471,6.590782,5.124334,8.953174,-5.484522,-0.035709,-2.086567,8.653742,7.478526,4.032808,9.652662,-9.550701,-7.316298,7.487791,3.649967,-0.092780,-8.875887,-7.426675,1.632974,7.832508,8.563442,-3.778378,3.124830,0.708932,5.058397,-4.503773,0.730330,-2.637084,5.435415,4.562883,3.191502,-5.545778,9.484982,-2.436528,-7.848018,9.564890,0.795395,-8.348329,9.657863,8.501001,-5.154358,0.588730,-4.989136,3.731519,-1.648632,3.068791,9.369162,3.969530,-3.513935,6.883522,0.620764,1.410217,-0.567438,8.195237,3.295836,-9.531577,0.370595,8.097549,-1.790561,1.637249,-4.516360,-5.567464,-9.156534,-9.552665,9.003977,-5.552915,-5.565459,6.499658,3.115733,-4.246525,-9.695266,-7.042824,1.114636,1.025511,8.148241,-4.450712,2.403383,3.281277,-2.106300,3.461974,5.267848,-4.746867,9.000819,-6.407883,7.490557,6.599559,3.005847,8.213073,-6.145526,-8.889048,9.115699,4.380260,-6.741656,-5.542715,-6.101656,-6.027356,7.289959,-2.295499,5.185164,9.369153,0.139367,-8.591133,7.953042,4.191617,-0.143515,5.314560,-3.141396,3.595672,2.361808,9.981890,9.931935,7.158500,2.813417,5.241643,-3.371789,2.820206,5.127257,-8.206213,8.804274,-6.024924,-1.433008,3.779459,-4.195712,4.400768,-1.112546,-1.127225,-6.954995,8.414043,9.383423,-3.644688,5.312404,5.301113,3.013922,2.473611,-4.549583,6.882414,3.089801,7.485717,3.453352,6.740305,-9.478307,6.259132,2.754940,-2.386031,8.890355,-8.141918,-8.950935,7.535756,-7.675763,-2.361910,1.326395,3.082056,-5.192197,-9.675190,0.980967,6.923054,1.450567,-6.872804,7.956502,4.372203,-0.114293,-8.876598,-4.146499,-4.966774,-2.721344,8.660284,-5.091896,8.931984,9.635375,-6.030692,8.997587,-9.306711,-0.329948,-2.739694,8.438362,-5.822915,4.531207,-3.421076,1.892248,-3.720709,8.940201,2.051082,-0.821362,-4.816161,-0.004549,-4.278579,6.991865,0.700733,-3.816447,6.737481,0.013724,8.258989,-2.582300,-9.338808,-0.086513,-0.918467,-5.761678,-6.202790,-9.209657,0.876621,8.573479,-0.536931,-3.661406,9.880517,2.695832,3.532799,-4.572749,-0.461575,-1.009680,-7.166142,1.160376,3.850716,-7.385279,9.663680,-2.434370,-0.349421,-9.177196,-9.193115,-7.064994,4.819877,4.636290,-0.700850,7.849679,-2.449797,-8.596997,7.724786,5.517633,6.683991,-7.108687,-9.519249,1.759938,-6.231242,-3.130935,9.860396,-6.966453,-0.871816,5.680726,-7.252021,3.393757,-0.172576,1.314583,-6.158540,-4.554717,9.546234,-9.955235,-7.382056,-3.621714,8.210314,7.595532,5.797476,-8.056574,7.082765,-8.638334,-4.610600,9.346426,8.942688,-8.908709,2.604420,-6.561857,5.562022,0.946774,-7.590455,8.773376,-4.250314,-1.377663,-0.694567,2.902441,-5.144344,3.742620,-7.445812,-6.852810,-3.057593,1.605350,3.572730,-7.854033,-0.428519,-4.076855,5.750169,-4.783575,7.032888,5.037011,6.152389,6.125042,-1.603559,2.838050,5.054415,1.850531,-9.352423,-3.479797,-0.079281,4.232672,-2.190950,1.614885,8.354530,3.282609,3.473821,-4.219425,3.476494,-6.942252,2.844512,-4.869948,4.208698,-5.540830,-6.805523,-7.119518,9.315771,4.443962,8.222746,5.218987,5.752129,3.638904,3.555895,3.565578,-5.991859,-2.204197,9.123286,-3.510740,-4.382199,1.663353,4.927151,9.705185,8.073345,-6.983301,-0.326121,4.675232,-2.636435,-2.386665,-4.385891,9.772592,4.313300,-5.075390,-1.949593,-0.062930,8.584633,-9.226111,6.131620,3.832498,-6.921102,6.021330,0.474732,-0.120079,-4.702152,8.713135,2.069882,5.894601,1.983235,3.709209,-2.956326,-3.389156,0.970311,2.095742,6.672651,8.127457,-5.281867,-5.673493,9.230380,-1.522285,9.290627,9.260841,-4.674640,3.334338,-4.270423,6.399386,-6.930189,6.908528,-3.305350,-7.097404,3.181457,-1.608410,4.613215,-0.619346,5.063669,-3.420201,-8.315684,4.038282,-2.021634,-9.547561,-5.738898,6.256455,-1.363931,-5.550704,2.476913,-5.156128,2.422732,8.701540,3.202148,2.085479,-4.859762,7.342696,0.340962,4.248520,0.509413,8.551158,2.754585,6.660901,0.741670,5.553946,-5.811087,5.013593,-0.453627,-6.621462,-5.622390,-6.369841,8.362637,-2.019078,5.471497,-5.452936,6.212907,-9.023592,7.213097,-1.275474,9.200373,6.199178,3.208541,3.565007,5.483109,8.969198,-1.200220,-9.264353,4.151409,-1.514291,-1.497952,-8.175631,-1.495784,7.480648,-5.693667,-6.276140,9.972504,7.041816,0.786316,-0.875742,9.082186,-8.666670,8.136971,9.634027,8.397459,0.121469,7.840249,-4.578919,-9.448619,5.978633,0.110355,9.620876,7.258725,-4.745037,7.032988,-7.633305,-5.431176,-8.700674,6.119423,5.672415,-6.829090,4.712737,-4.509250,2.185849,2.470157,0.006436,6.247734,4.940771,6.177915,2.039338,-8.955726,4.050791,-1.347036,-4.267214,-8.204487,2.921702,6.241501,-6.459847,-6.456490,-1.908810,-7.480327,-3.559816,-1.563742,-7.599395,8.977971,0.346019,8.575944,8.915331,-4.480054,-4.624504,0.512020,5.904935,-3.869931,-3.528311,-7.124082,-9.162570,-1.210574,-6.605298,-4.256471,-0.570989,-2.825792,4.407832,2.785349,9.594016,-4.000772,-4.068779,0.472650,-5.949628,9.985494,-5.517333,-3.042435,-1.935323,-1.573513,4.059561,6.208941,-0.707363,7.141568,-1.808018,-9.913223,3.647265,4.951300,-6.472607,6.391539,-8.115103,2.119467,-1.685959,9.439901,-5.975313,2.953638,-6.924498,-5.068476,-4.074855,-3.879901,-2.435333,2.229029,9.857779,2.951240,3.277251,8.854607,5.700099,2.594490,-8.482653,-1.258221,-7.938025,-5.456386,-3.088344,0.967020,9.634800,0.580917,5.279933,1.620764,1.347193,-8.009604,1.541727,-5.110123,4.049730,0.442861,-2.623002,-5.841337,5.468183,9.039844,1.787792,5.332337,-2.075954,-2.426045,8.585592,7.046115,-6.757360,3.801736,4.076232,-8.640605,2.307330,-5.951404,0.634359,-4.455775,2.409700,0.240480,4.598460,0.289145,2.967144,4.021591,3.998015,-3.352204,-0.855597,-5.195564,6.025459,-6.836725,-2.310707,1.429119,-1.383714,-6.695592,8.933363,-0.881324,-5.205799,0.313840,-1.800296,-1.454272,2.212678,7.896680,3.326022,8.595124,6.244365,0.321015,-7.380285,4.195131,7.858882,-8.712513,1.693611,2.885116,7.070011,-0.470011,8.113244,3.428676,4.809797,-5.935748,-0.905353,8.236456,-8.686341,3.936640,0.674891,1.326901,0.297860,-6.031339,-0.303806,-9.972228,-1.750353,0.834504,-0.158063,-8.038010,-8.629319,-9.626473,-1.355504,-0.159163,-7.715851,1.100283,-0.884057,-3.574241,-5.529591,1.180984,-5.556063,-0.399999,-8.036028,-0.434301,1.221336,-8.013083,-8.136899,-7.141191,-9.922791,6.338626,5.006586,6.653925,0.584094,4.176785,-0.133763,-5.242265,-5.256812,3.672949,1.572857,7.962408,-8.620060,-8.649760,-3.723269,1.101649,1.740450,-8.454442,4.936728,-8.736750,8.594980,-8.478774,-4.359090,0.445421,-1.408618,7.984015,-6.862774,-8.560215,-4.735451,0.492099,8.109956,-9.877073,1.244574,5.602077,-6.749240], dtype = "float64")#candidate|6766|(1232,)|const|float64
call_6764 = relay.TupleGetItem(func_5358_call(relay.reshape(const_6765.astype('float64'), [14, 8, 1]), relay.reshape(const_6766.astype('float64'), [14, 8, 11]), ), 0)
call_6767 = relay.TupleGetItem(func_5361_call(relay.reshape(const_6765.astype('float64'), [14, 8, 1]), relay.reshape(const_6766.astype('float64'), [14, 8, 11]), ), 0)
func_148_call = mod.get_global_var('func_148')
func_150_call = mutated_mod.get_global_var('func_150')
call_6785 = relay.TupleGetItem(func_148_call(), 0)
call_6786 = relay.TupleGetItem(func_150_call(), 0)
func_1404_call = mod.get_global_var('func_1404')
func_1407_call = mutated_mod.get_global_var('func_1407')
var_6788 = relay.var("var_6788", dtype = "bool", shape = (56,))#candidate|6788|(56,)|var|bool
call_6787 = relay.TupleGetItem(func_1404_call(relay.reshape(var_6788.astype('bool'), [14, 1, 4])), 3)
call_6789 = relay.TupleGetItem(func_1407_call(relay.reshape(var_6788.astype('bool'), [14, 1, 4])), 3)
func_2584_call = mod.get_global_var('func_2584')
func_2585_call = mutated_mod.get_global_var('func_2585')
call_6793 = relay.TupleGetItem(func_2584_call(), 0)
call_6794 = relay.TupleGetItem(func_2585_call(), 0)
func_3111_call = mod.get_global_var('func_3111')
func_3112_call = mutated_mod.get_global_var('func_3112')
call_6795 = relay.TupleGetItem(func_3111_call(), 0)
call_6796 = relay.TupleGetItem(func_3112_call(), 0)
output = relay.Tuple([bop_6734,call_6747,call_6752,call_6757,call_6764,const_6765,const_6766,call_6785,call_6787,var_6788,call_6793,call_6795,])
output2 = relay.Tuple([bop_6734,call_6748,call_6753,call_6758,call_6767,const_6765,const_6766,call_6786,call_6789,var_6788,call_6794,call_6796,])
func_6803 = relay.Function([var_6732,var_6733,var_6788,], output)
mod['func_6803'] = func_6803
mod = relay.transform.InferType()(mod)
var_6804 = relay.var("var_6804", dtype = "uint16", shape = ())#candidate|6804|()|var|uint16
var_6805 = relay.var("var_6805", dtype = "uint16", shape = (16, 9, 6))#candidate|6805|(16, 9, 6)|var|uint16
var_6806 = relay.var("var_6806", dtype = "bool", shape = (56,))#candidate|6806|(56,)|var|bool
output = func_6803(var_6804,var_6805,var_6806,)
func_6807 = relay.Function([var_6804,var_6805,var_6806,], output)
mutated_mod['func_6807'] = func_6807
mutated_mod = relay.transform.InferType()(mutated_mod)
func_322_call = mod.get_global_var('func_322')
func_323_call = mutated_mod.get_global_var('func_323')
call_6842 = relay.TupleGetItem(func_322_call(), 0)
call_6843 = relay.TupleGetItem(func_323_call(), 0)
func_2466_call = mod.get_global_var('func_2466')
func_2468_call = mutated_mod.get_global_var('func_2468')
call_6846 = relay.TupleGetItem(func_2466_call(), 0)
call_6847 = relay.TupleGetItem(func_2468_call(), 0)
output = relay.Tuple([call_6842,call_6846,])
output2 = relay.Tuple([call_6843,call_6847,])
func_6859 = relay.Function([], output)
mod['func_6859'] = func_6859
mod = relay.transform.InferType()(mod)
mutated_mod['func_6859'] = func_6859
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6859_call = mutated_mod.get_global_var('func_6859')
call_6860 = func_6859_call()
output = call_6860
func_6861 = relay.Function([], output)
mutated_mod['func_6861'] = func_6861
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1550_call = mod.get_global_var('func_1550')
func_1552_call = mutated_mod.get_global_var('func_1552')
call_6907 = relay.TupleGetItem(func_1550_call(), 1)
call_6908 = relay.TupleGetItem(func_1552_call(), 1)
func_3765_call = mod.get_global_var('func_3765')
func_3767_call = mutated_mod.get_global_var('func_3767')
call_6925 = relay.TupleGetItem(func_3765_call(), 0)
call_6926 = relay.TupleGetItem(func_3767_call(), 0)
output = relay.Tuple([call_6907,call_6925,])
output2 = relay.Tuple([call_6908,call_6926,])
func_6932 = relay.Function([], output)
mod['func_6932'] = func_6932
mod = relay.transform.InferType()(mod)
output = func_6932()
func_6933 = relay.Function([], output)
mutated_mod['func_6933'] = func_6933
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3765_call = mod.get_global_var('func_3765')
func_3767_call = mutated_mod.get_global_var('func_3767')
call_6981 = relay.TupleGetItem(func_3765_call(), 0)
call_6982 = relay.TupleGetItem(func_3767_call(), 0)
func_557_call = mod.get_global_var('func_557')
func_558_call = mutated_mod.get_global_var('func_558')
call_6991 = relay.TupleGetItem(func_557_call(), 1)
call_6992 = relay.TupleGetItem(func_558_call(), 1)
func_2038_call = mod.get_global_var('func_2038')
func_2041_call = mutated_mod.get_global_var('func_2041')
const_7016 = relay.const([True,True,False,False,True,True,False,False,False,False,True,False,True,False,True,True,False,False,False,False,False,True,True,True,True,True,False,False,False,False,False,True,False,False,False,True,True,False,True,False,True,False,False,False,False,True,False,True,True,False,True,False,True,False,True,False], dtype = "bool")#candidate|7016|(56,)|const|bool
var_7017 = relay.var("var_7017", dtype = "float64", shape = (3, 2))#candidate|7017|(3, 2)|var|float64
call_7015 = relay.TupleGetItem(func_2038_call(relay.reshape(const_7016.astype('bool'), [56,]), relay.reshape(var_7017.astype('float64'), [6,]), ), 5)
call_7018 = relay.TupleGetItem(func_2041_call(relay.reshape(const_7016.astype('bool'), [56,]), relay.reshape(var_7017.astype('float64'), [6,]), ), 5)
output = relay.Tuple([call_6981,call_6991,call_7015,const_7016,var_7017,])
output2 = relay.Tuple([call_6982,call_6992,call_7018,const_7016,var_7017,])
func_7026 = relay.Function([var_7017,], output)
mod['func_7026'] = func_7026
mod = relay.transform.InferType()(mod)
mutated_mod['func_7026'] = func_7026
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7027 = relay.var("var_7027", dtype = "float64", shape = (3, 2))#candidate|7027|(3, 2)|var|float64
func_7026_call = mutated_mod.get_global_var('func_7026')
call_7028 = func_7026_call(var_7027)
output = call_7028
func_7029 = relay.Function([var_7027], output)
mutated_mod['func_7029'] = func_7029
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4736_call = mod.get_global_var('func_4736')
func_4737_call = mutated_mod.get_global_var('func_4737')
call_7066 = relay.TupleGetItem(func_4736_call(), 0)
call_7067 = relay.TupleGetItem(func_4737_call(), 0)
output = call_7066
output2 = call_7067
func_7084 = relay.Function([], output)
mod['func_7084'] = func_7084
mod = relay.transform.InferType()(mod)
mutated_mod['func_7084'] = func_7084
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7084_call = mutated_mod.get_global_var('func_7084')
call_7085 = func_7084_call()
output = call_7085
func_7086 = relay.Function([], output)
mutated_mod['func_7086'] = func_7086
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2294_call = mod.get_global_var('func_2294')
func_2295_call = mutated_mod.get_global_var('func_2295')
call_7127 = relay.TupleGetItem(func_2294_call(), 0)
call_7128 = relay.TupleGetItem(func_2295_call(), 0)
func_2218_call = mod.get_global_var('func_2218')
func_2219_call = mutated_mod.get_global_var('func_2219')
call_7138 = relay.TupleGetItem(func_2218_call(), 3)
call_7139 = relay.TupleGetItem(func_2219_call(), 3)
output = relay.Tuple([call_7127,call_7138,])
output2 = relay.Tuple([call_7128,call_7139,])
func_7144 = relay.Function([], output)
mod['func_7144'] = func_7144
mod = relay.transform.InferType()(mod)
mutated_mod['func_7144'] = func_7144
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7144_call = mutated_mod.get_global_var('func_7144')
call_7145 = func_7144_call()
output = call_7145
func_7146 = relay.Function([], output)
mutated_mod['func_7146'] = func_7146
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6932_call = mod.get_global_var('func_6932')
func_6933_call = mutated_mod.get_global_var('func_6933')
call_7307 = relay.TupleGetItem(func_6932_call(), 1)
call_7308 = relay.TupleGetItem(func_6933_call(), 1)
output = relay.Tuple([call_7307,])
output2 = relay.Tuple([call_7308,])
func_7309 = relay.Function([], output)
mod['func_7309'] = func_7309
mod = relay.transform.InferType()(mod)
output = func_7309()
func_7310 = relay.Function([], output)
mutated_mod['func_7310'] = func_7310
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3878_call = mod.get_global_var('func_3878')
func_3880_call = mutated_mod.get_global_var('func_3880')
call_7350 = relay.TupleGetItem(func_3878_call(), 1)
call_7351 = relay.TupleGetItem(func_3880_call(), 1)
output = call_7350
output2 = call_7351
func_7355 = relay.Function([], output)
mod['func_7355'] = func_7355
mod = relay.transform.InferType()(mod)
output = func_7355()
func_7356 = relay.Function([], output)
mutated_mod['func_7356'] = func_7356
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4051_call = mod.get_global_var('func_4051')
func_4052_call = mutated_mod.get_global_var('func_4052')
call_7357 = func_4051_call()
call_7358 = func_4051_call()
output = call_7357
output2 = call_7358
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
func_5820_call = mod.get_global_var('func_5820')
func_5821_call = mutated_mod.get_global_var('func_5821')
call_7409 = relay.TupleGetItem(func_5820_call(), 5)
call_7410 = relay.TupleGetItem(func_5821_call(), 5)
output = call_7409
output2 = call_7410
func_7415 = relay.Function([], output)
mod['func_7415'] = func_7415
mod = relay.transform.InferType()(mod)
output = func_7415()
func_7416 = relay.Function([], output)
mutated_mod['func_7416'] = func_7416
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7084_call = mod.get_global_var('func_7084')
func_7086_call = mutated_mod.get_global_var('func_7086')
call_7427 = func_7084_call()
call_7428 = func_7084_call()
func_2457_call = mod.get_global_var('func_2457')
func_2458_call = mutated_mod.get_global_var('func_2458')
call_7429 = relay.TupleGetItem(func_2457_call(), 0)
call_7430 = relay.TupleGetItem(func_2458_call(), 0)
func_5521_call = mod.get_global_var('func_5521')
func_5524_call = mutated_mod.get_global_var('func_5524')
const_7433 = relay.const([9,-3,-1,-9,-7,4,-6,10,2,-10,-2,7,8,-2,-1,8,-8,4,-3,6,7,-8,1,-9,-1,4,-9,5,-8,-10,1,8,6,-1,-8,-1,-5,8,-8,2,7,3,8,-7,3,7,5,7,1,2,-5,4,1,9,-10,-9,7,-7,9,3,-1,-10,-8,-10,3,8,-5,9,6,-7,6,-5,7,-2,-4,-10,7,-1,-5,6,3,7,8,-5,-1,-1,8,4,8,2,2,8,10,-4,10,-4,-4,10,6,-8,-10,7,-7,-1,-8,-8,5,-8,5,9,-2,8,-5,-9,6,9,6,-3,-7,-7,-7,5,-1,6,-7,-1,1,6,-10,6,-10,-3,9,1,-10,2,3,1,10,-2,-4,5,-2,1,6,7,10,-4,4,8,-4,-3,-8,3,-2,7,5,1,-3,-9,-10,6,-6,3,-6,6,-3,-6,-3,-1,3,-3,1,8,-8,4,-5,2,-1,-5,-7,-6,2,-1,3,2,-1,-6,8,-6,-3,4,1,3,-10,8,9,-10,-5,6,5,4,10,10,-4,-4,-9,6,4,-9,-8,-4,10,-8,4,-3,-3,-7,-6,2,-5,8,-7,-1,6,7,-8,2,6,-3,7,1,2,4,-7,2,5,6,-6,2,9,-9,10,-5,3,-9,5,-10,-10,-8,3,10,10,9,-3,2,-10,-8,-2,9,10,-6,7,-3,2,-5,9,-4,-9,7,-4,3,9,4,-2,-7,-10,1,-10,-4,6,-7,5,6,-4,8,-1,10,10,-1,7,-9,10,-4,-2,3,8,-5,-3,8,5,5,-5,-5,-1,9,4,-6,-6,5,1,-10,-9,-3,-7,10,-7,7,2,-8,6,-10,5,-5,8,-1,-9,9,5,2,3,3,7,-3,-1,1,-8,10,-8,-6,-6,-5,-7,4,-6,-5,8,-10,-9,-3,2,2,4,-5,6,9,8,6,10,-1,-6,-5,6,9,-8,10,6,-2,-1,-3,10,-8,9,6,-3,6,-3,4,-8,-9,-3,6,8,-10,-9,-7,-6,-7,-10,-4,2,-2,3,-6,-9,7,1,-1,-3,1,3,-1,4,4,3,-7,-8,-9,7,1,-8,7,-4,-2,1,-1,1,5,-9,7,7,-6,5,7,9,-5,8,10,-2,1,6,-8,-3,10,10,-6,1,3,5,7,9,5,-6,1,7,-9,-3,8,8,10,7,-6,-5,-6,2,-8,-5,-10,10,-7,5,-10,5,-6,7,-2,9,-3,-8,9,-2,2,-2,8,-6,-6,3,3,5,-10,5,-5,9,-1,8,-6,6,8,2,7,1,1,1,-3,-3,-9,4,-3,3,-9,-5,-3,-4,-9,7,6,-3,-3,1,3,8,4,-5,4,-2,-2,9,-8,-6,-1,6,2,-4,-8,-2,1,-2,-3,-2,6,1,1,-1,5,9,-10,-5,8,7,8,-4,1,-4,2,1,-1,6,-4,-4,-6,-7,10,9,3,4,5,-10,6,1,3,-6,6,-8,-10,-1,7,-3,2,-7,-7,-8,-10,1,4,4,5], dtype = "uint8")#candidate|7433|(576,)|const|uint8
call_7432 = relay.TupleGetItem(func_5521_call(relay.reshape(const_7433.astype('uint8'), [9, 8, 8])), 0)
call_7434 = relay.TupleGetItem(func_5524_call(relay.reshape(const_7433.astype('uint8'), [9, 8, 8])), 0)
output = relay.Tuple([call_7427,call_7429,call_7432,const_7433,])
output2 = relay.Tuple([call_7428,call_7430,call_7434,const_7433,])
func_7452 = relay.Function([], output)
mod['func_7452'] = func_7452
mod = relay.transform.InferType()(mod)
output = func_7452()
func_7453 = relay.Function([], output)
mutated_mod['func_7453'] = func_7453
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3111_call = mod.get_global_var('func_3111')
func_3112_call = mutated_mod.get_global_var('func_3112')
call_7490 = relay.TupleGetItem(func_3111_call(), 0)
call_7491 = relay.TupleGetItem(func_3112_call(), 0)
func_4613_call = mod.get_global_var('func_4613')
func_4616_call = mutated_mod.get_global_var('func_4616')
const_7493 = relay.const([-5.267711,-2.891300,0.369099,-2.920850,-2.005041,-5.892477,2.657000,-6.066171,0.008990,4.690769,-0.915070,-8.300074,-0.626911,-0.292900,4.989248,-7.687644,4.285323,-2.915317,-2.157407,3.096622,-2.855833,-5.154483,3.595134,5.476379,6.872368,-7.068119,-8.726715,6.543540,-6.356211,-6.578342,-4.027003,0.422419,3.282761,4.439628,-1.707756,-5.073918,-8.310590,-1.191769,-6.754525,-8.129487,-5.399844,8.794986,1.840496,-2.550454,-4.739219,7.129403,1.044439,1.081353,1.771689,2.305168,7.036570,-8.314383,-5.160652,5.769966,-6.053907,-9.056422,-7.655028,9.813984,0.370655,-7.725793,-4.828345,-4.071240,-4.129707,5.299361,-4.248088,-3.594679,-1.151723,3.649269,0.307344,7.818747,-9.289114,1.447835,-7.953036,-3.148087,-1.497142,8.470553,9.846319,-9.488808,2.824845,2.759655,-6.908108,9.666145,-1.088698,3.908104,8.182716,-2.340735,3.045793,2.497695,-1.672019,7.084862,-1.233088,-9.921056,-7.626853,1.351432,-2.429270,-4.798200,-9.256665,1.298482,-9.930724,6.662872,-2.963400,-9.041015,6.997243,3.676743,5.772232,-2.977547,4.112516,3.761022,2.538659,-4.306792,8.141679,9.483858,-8.463096,1.247786,2.653962,6.078794,-1.491111,2.195460,2.863551,1.883451], dtype = "float32")#candidate|7493|(120,)|const|float32
call_7492 = relay.TupleGetItem(func_4613_call(relay.reshape(const_7493.astype('float32'), [3, 5, 8])), 1)
call_7494 = relay.TupleGetItem(func_4616_call(relay.reshape(const_7493.astype('float32'), [3, 5, 8])), 1)
output = relay.Tuple([call_7490,call_7492,const_7493,])
output2 = relay.Tuple([call_7491,call_7494,const_7493,])
func_7497 = relay.Function([], output)
mod['func_7497'] = func_7497
mod = relay.transform.InferType()(mod)
output = func_7497()
func_7498 = relay.Function([], output)
mutated_mod['func_7498'] = func_7498
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7084_call = mod.get_global_var('func_7084')
func_7086_call = mutated_mod.get_global_var('func_7086')
call_7551 = func_7084_call()
call_7552 = func_7084_call()
func_7497_call = mod.get_global_var('func_7497')
func_7498_call = mutated_mod.get_global_var('func_7498')
call_7558 = relay.TupleGetItem(func_7497_call(), 1)
call_7559 = relay.TupleGetItem(func_7498_call(), 1)
output = relay.Tuple([call_7551,call_7558,])
output2 = relay.Tuple([call_7552,call_7559,])
func_7578 = relay.Function([], output)
mod['func_7578'] = func_7578
mod = relay.transform.InferType()(mod)
mutated_mod['func_7578'] = func_7578
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7578_call = mutated_mod.get_global_var('func_7578')
call_7579 = func_7578_call()
output = call_7579
func_7580 = relay.Function([], output)
mutated_mod['func_7580'] = func_7580
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4354_call = mod.get_global_var('func_4354')
func_4356_call = mutated_mod.get_global_var('func_4356')
call_7598 = func_4354_call()
call_7599 = func_4354_call()
output = call_7598
output2 = call_7599
func_7600 = relay.Function([], output)
mod['func_7600'] = func_7600
mod = relay.transform.InferType()(mod)
output = func_7600()
func_7601 = relay.Function([], output)
mutated_mod['func_7601'] = func_7601
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2827_call = mod.get_global_var('func_2827')
func_2828_call = mutated_mod.get_global_var('func_2828')
call_7619 = func_2827_call()
call_7620 = func_2827_call()
func_1246_call = mod.get_global_var('func_1246')
func_1250_call = mutated_mod.get_global_var('func_1250')
const_7634 = relay.const([1.678176,-7.544735,2.927311,-2.742766,9.046840,3.439434], dtype = "float64")#candidate|7634|(6,)|const|float64
var_7635 = relay.var("var_7635", dtype = "float32", shape = (192,))#candidate|7635|(192,)|var|float32
call_7633 = relay.TupleGetItem(func_1246_call(relay.reshape(const_7634.astype('float64'), [6,]), relay.reshape(var_7635.astype('float32'), [192,]), ), 9)
call_7636 = relay.TupleGetItem(func_1250_call(relay.reshape(const_7634.astype('float64'), [6,]), relay.reshape(var_7635.astype('float32'), [192,]), ), 9)
func_3546_call = mod.get_global_var('func_3546')
func_3547_call = mutated_mod.get_global_var('func_3547')
call_7640 = func_3546_call()
call_7641 = func_3546_call()
output = relay.Tuple([call_7619,call_7633,const_7634,var_7635,call_7640,])
output2 = relay.Tuple([call_7620,call_7636,const_7634,var_7635,call_7641,])
func_7647 = relay.Function([var_7635,], output)
mod['func_7647'] = func_7647
mod = relay.transform.InferType()(mod)
mutated_mod['func_7647'] = func_7647
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7648 = relay.var("var_7648", dtype = "float32", shape = (192,))#candidate|7648|(192,)|var|float32
func_7647_call = mutated_mod.get_global_var('func_7647')
call_7649 = func_7647_call(var_7648)
output = call_7649
func_7650 = relay.Function([var_7648], output)
mutated_mod['func_7650'] = func_7650
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2891_call = mod.get_global_var('func_2891')
func_2892_call = mutated_mod.get_global_var('func_2892')
call_7668 = relay.TupleGetItem(func_2891_call(), 3)
call_7669 = relay.TupleGetItem(func_2892_call(), 3)
output = relay.Tuple([call_7668,])
output2 = relay.Tuple([call_7669,])
func_7676 = relay.Function([], output)
mod['func_7676'] = func_7676
mod = relay.transform.InferType()(mod)
mutated_mod['func_7676'] = func_7676
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7676_call = mutated_mod.get_global_var('func_7676')
call_7677 = func_7676_call()
output = call_7677
func_7678 = relay.Function([], output)
mutated_mod['func_7678'] = func_7678
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3709_call = mod.get_global_var('func_3709')
func_3711_call = mutated_mod.get_global_var('func_3711')
call_7686 = func_3709_call()
call_7687 = func_3709_call()
output = call_7686
output2 = call_7687
func_7700 = relay.Function([], output)
mod['func_7700'] = func_7700
mod = relay.transform.InferType()(mod)
output = func_7700()
func_7701 = relay.Function([], output)
mutated_mod['func_7701'] = func_7701
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3111_call = mod.get_global_var('func_3111')
func_3112_call = mutated_mod.get_global_var('func_3112')
call_7743 = relay.TupleGetItem(func_3111_call(), 0)
call_7744 = relay.TupleGetItem(func_3112_call(), 0)
func_375_call = mod.get_global_var('func_375')
func_378_call = mutated_mod.get_global_var('func_378')
const_7755 = relay.const([-7.287905,-5.202698,-7.647912,4.902599,-4.631148,-0.173738,7.362184,-3.544565,8.942651,5.797012,-7.606901,-0.852956,3.218399,-3.365353,1.123880,9.318790,6.957331,5.993698,-2.544180,-6.147156,-7.581284,2.739525,5.104037,-0.366134,9.975473,2.620550,-3.855569,-7.754126,-0.338693,-0.519847,3.045186,-2.253340,4.305846,5.555115,-6.477057,-4.479086,-2.853594,-2.249505,4.121687,-3.899563,-0.715386,9.381349,8.918379,-3.547482,-5.839787,-1.105581,-5.698693,-7.304406,-8.422731,-6.158957,5.918521,4.020333,-2.469963,-5.482888,7.150810,-1.580110,-4.213906,-6.402472,5.213114,-5.854939,4.791705,-5.096664,4.939706,0.881403,-3.906574,-3.041795,-8.777449,0.316613,8.354413,9.901049,-1.322286,-3.275375,2.457382,6.572670,-3.431261,-4.791325,-7.019165,9.585391,3.034253,5.340180,-8.185934,-1.181395,-1.645307,9.854320,9.157085,-2.704175,5.608108,-1.894935,2.121671,7.423122,1.293656,6.893231,-9.190860,4.830379,2.089626,7.426596,-3.218343,-6.500851,6.550083,-0.168820,-5.848598,6.217876,-3.258109,-5.093317,0.567002,3.993015,6.749567,-4.517325,5.412928,-3.067663,-9.402138,0.237213,6.187511,1.364527,4.904428,3.268440,-9.406497,4.178771,-7.067935,-9.413980,-6.195002,8.944499,-0.430507,1.756970,6.514143,-0.239600,-4.813461,1.114326,-7.374904,-5.996331,-1.468499,0.089172,-3.703093,6.666742,9.969196,-2.937668,7.030793,0.005146,5.738455,-4.769845,-6.188967,1.791815,-6.463396,-7.927296,6.321210,-5.522089,-6.726027,8.759105,2.029787,-1.590075,-3.863972,-3.835640,-7.375510,-3.137939,-2.934912,-8.172083,6.060796,1.065127,-8.235535,-7.056943,0.202663,-4.915652,7.726476,-6.039982,-2.510224,4.007453,-0.267667,1.382548,8.776644,-8.422913,-0.640669,9.989612,-7.825696,9.526480,-1.759703,0.803238,-2.598482,-3.935250,7.280346,-4.732880,2.557037,-3.870508,0.287906,-2.625577,5.521091,5.454347,4.165785,-7.111405,8.188290,2.553480,3.037790,8.611148], dtype = "float32")#candidate|7755|(192,)|const|float32
call_7754 = func_375_call(relay.reshape(const_7755.astype('float32'), [12, 8, 2]))
call_7756 = func_375_call(relay.reshape(const_7755.astype('float32'), [12, 8, 2]))
output = relay.Tuple([call_7743,call_7754,const_7755,])
output2 = relay.Tuple([call_7744,call_7756,const_7755,])
func_7768 = relay.Function([], output)
mod['func_7768'] = func_7768
mod = relay.transform.InferType()(mod)
output = func_7768()
func_7769 = relay.Function([], output)
mutated_mod['func_7769'] = func_7769
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7781 = relay.var("var_7781", dtype = "int16", shape = (5, 4, 1))#candidate|7781|(5, 4, 1)|var|int16
const_7782 = relay.const([[[-3,-7,1,10,5,-5,-7],[-5,8,4,-5,5,3,-3],[1,4,3,9,-3,1,2],[-3,2,-7,8,-4,-6,-7]],[[8,-1,5,3,1,1,-10],[-3,10,-1,-4,5,-2,8],[-7,-8,8,3,7,1,-5],[1,7,-8,-2,3,9,-1]],[[-8,-10,-6,9,-8,-7,-8],[4,-1,1,-2,8,9,-1],[1,1,1,-4,10,10,8],[4,6,-9,4,8,10,10]],[[-9,-10,-3,10,4,2,9],[-3,-9,-3,6,3,-4,8],[7,5,-10,-6,8,8,2],[-8,-2,-6,-8,8,-2,6]],[[2,-10,-1,-4,-2,4,8],[3,-2,9,-2,6,5,-5],[-5,-3,-4,-5,-1,-6,1],[4,3,-7,8,10,-2,-1]]], dtype = "int16")#candidate|7782|(5, 4, 7)|const|int16
bop_7783 = relay.multiply(var_7781.astype('int16'), const_7782.astype('int16')) # shape=(5, 4, 7)
func_6238_call = mod.get_global_var('func_6238')
func_6240_call = mutated_mod.get_global_var('func_6240')
call_7794 = relay.TupleGetItem(func_6238_call(), 0)
call_7795 = relay.TupleGetItem(func_6240_call(), 0)
func_2130_call = mod.get_global_var('func_2130')
func_2135_call = mutated_mod.get_global_var('func_2135')
var_7801 = relay.var("var_7801", dtype = "float32", shape = (1274,))#candidate|7801|(1274,)|var|float32
var_7802 = relay.var("var_7802", dtype = "float64", shape = (6,))#candidate|7802|(6,)|var|float64
const_7803 = relay.const([-2.121803,-0.410431,-2.500045,-1.529007,-9.733447,4.921588,-8.718528,5.395680,8.076348,1.301080,-6.157928,-4.911597,-5.260013,-4.964499,9.231978,-4.750203,-7.504928,-3.467883,-1.306571,7.348208,-9.970877,2.090898,-9.325109,1.914829,7.452329,-4.036885,4.216569,6.279620,-6.282640,-3.388427,8.583567,7.640106,7.801748,-0.329091,-2.373324,-9.114862,-5.816321,-8.751800,5.898194,4.959522,-4.615247,-4.695261,-0.516904,-0.432554,0.127902,7.579340,5.599485,-9.820205,-6.540938,-7.517175,-0.653172,6.658570,-3.432314,-0.743295,4.198723,-4.074949,2.381037,1.934932,-2.991250,-6.049721,-2.132233,-3.007817,4.300022,5.138721,-0.569928,-4.228809,-4.872582,7.962111,8.578351,-7.144442,2.114604,9.150917,-7.523602,3.554548,-5.005589,-6.738391,1.052442,-4.560990,-0.816670,-9.548465,3.669929,0.349198,-8.477369,-0.282369,-8.741368,-8.494128,4.968368,-0.385566,-8.958774,7.337629,-3.545649,-3.660231,-4.216934,-8.441343,-7.400814,8.242346,5.228155,3.461391,-6.164416,-4.363439,9.940352,-7.427826,-1.305370,-1.169731,-6.805968,9.353176,7.960947,-4.181615,-8.011609,-8.901032,3.915288,-0.237914,2.874899,-0.295240,4.462673,-7.635271,1.395199,2.163409,-1.934223,8.728267,3.875466,6.599212,-0.936108,2.121769,-0.224219,8.844311,9.091823,-9.139019,8.870568,-6.838419,1.357898,2.133677,-9.084317,-7.563304,-8.864222,3.436686,-5.785700,3.267121,0.539372,0.996507,-5.198282,2.094921,-2.508495,-1.052241,9.951180,-0.549432,-2.528239,2.485488,6.723011,0.117255,6.895239,9.653620,7.175213,-8.633347,5.369131,-0.577593,-2.602161,-4.507683,0.761966,9.908915,6.128895,-4.246420,7.295986,-4.113378,3.633031,8.928003,3.845720,9.533487,0.487474,0.320330,8.039086,-7.874935,8.899011,9.973357,-0.497514,2.983257,-3.599636,5.192418,-9.353722,-7.560951,5.081181,-2.755432,1.724687,6.177844,-0.617136,9.268014,-5.869043,5.169315,-2.264031,-2.822025,2.066374,7.423476], dtype = "float32")#candidate|7803|(192,)|const|float32
call_7800 = relay.TupleGetItem(func_2130_call(relay.reshape(var_7801.astype('float32'), [14, 7, 13]), relay.reshape(var_7802.astype('float64'), [1, 6]), relay.reshape(const_7803.astype('float32'), [192,]), ), 0)
call_7804 = relay.TupleGetItem(func_2135_call(relay.reshape(var_7801.astype('float32'), [14, 7, 13]), relay.reshape(var_7802.astype('float64'), [1, 6]), relay.reshape(const_7803.astype('float32'), [192,]), ), 0)
func_858_call = mod.get_global_var('func_858')
func_859_call = mutated_mod.get_global_var('func_859')
call_7807 = relay.TupleGetItem(func_858_call(), 0)
call_7808 = relay.TupleGetItem(func_859_call(), 0)
bop_7810 = relay.bitwise_or(var_7802.astype('uint8'), var_7781.astype('uint8')) # shape=(5, 4, 6)
output = relay.Tuple([bop_7783,call_7794,call_7800,var_7801,const_7803,call_7807,bop_7810,])
output2 = relay.Tuple([bop_7783,call_7795,call_7804,var_7801,const_7803,call_7808,bop_7810,])
func_7816 = relay.Function([var_7781,var_7801,var_7802,], output)
mod['func_7816'] = func_7816
mod = relay.transform.InferType()(mod)
var_7817 = relay.var("var_7817", dtype = "int16", shape = (5, 4, 1))#candidate|7817|(5, 4, 1)|var|int16
var_7818 = relay.var("var_7818", dtype = "float32", shape = (1274,))#candidate|7818|(1274,)|var|float32
var_7819 = relay.var("var_7819", dtype = "float64", shape = (6,))#candidate|7819|(6,)|var|float64
output = func_7816(var_7817,var_7818,var_7819,)
func_7820 = relay.Function([var_7817,var_7818,var_7819,], output)
mutated_mod['func_7820'] = func_7820
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6932_call = mod.get_global_var('func_6932')
func_6933_call = mutated_mod.get_global_var('func_6933')
call_7833 = relay.TupleGetItem(func_6932_call(), 1)
call_7834 = relay.TupleGetItem(func_6933_call(), 1)
func_7578_call = mod.get_global_var('func_7578')
func_7580_call = mutated_mod.get_global_var('func_7580')
call_7838 = relay.TupleGetItem(func_7578_call(), 1)
call_7839 = relay.TupleGetItem(func_7580_call(), 1)
var_7842 = relay.var("var_7842", dtype = "float32", shape = (3, 5, 8))#candidate|7842|(3, 5, 8)|var|float32
bop_7843 = relay.equal(call_7838.astype('bool'), relay.reshape(var_7842.astype('bool'), relay.shape_of(call_7838))) # shape=(3, 5, 8)
bop_7846 = relay.equal(call_7839.astype('bool'), relay.reshape(var_7842.astype('bool'), relay.shape_of(call_7839))) # shape=(3, 5, 8)
bop_7865 = relay.left_shift(var_7842.astype('int64'), relay.reshape(bop_7843.astype('int64'), relay.shape_of(var_7842))) # shape=(3, 5, 8)
bop_7868 = relay.left_shift(var_7842.astype('int64'), relay.reshape(bop_7846.astype('int64'), relay.shape_of(var_7842))) # shape=(3, 5, 8)
uop_7871 = relay.acosh(bop_7843.astype('float32')) # shape=(3, 5, 8)
uop_7873 = relay.acosh(bop_7846.astype('float32')) # shape=(3, 5, 8)
var_7881 = relay.var("var_7881", dtype = "float32", shape = (3, 5, 8))#candidate|7881|(3, 5, 8)|var|float32
bop_7882 = relay.logical_and(var_7842.astype('bool'), relay.reshape(var_7881.astype('bool'), relay.shape_of(var_7842))) # shape=(3, 5, 8)
uop_7897 = relay.sinh(var_7842.astype('float32')) # shape=(3, 5, 8)
func_5035_call = mod.get_global_var('func_5035')
func_5036_call = mutated_mod.get_global_var('func_5036')
call_7911 = relay.TupleGetItem(func_5035_call(), 0)
call_7912 = relay.TupleGetItem(func_5036_call(), 0)
output = relay.Tuple([call_7833,bop_7865,uop_7871,bop_7882,uop_7897,call_7911,])
output2 = relay.Tuple([call_7834,bop_7868,uop_7873,bop_7882,uop_7897,call_7912,])
func_7924 = relay.Function([var_7842,var_7881,], output)
mod['func_7924'] = func_7924
mod = relay.transform.InferType()(mod)
mutated_mod['func_7924'] = func_7924
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7924_call = mutated_mod.get_global_var('func_7924')
var_7926 = relay.var("var_7926", dtype = "float32", shape = (3, 5, 8))#candidate|7926|(3, 5, 8)|var|float32
var_7927 = relay.var("var_7927", dtype = "float32", shape = (3, 5, 8))#candidate|7927|(3, 5, 8)|var|float32
call_7925 = func_7924_call(var_7926,var_7927,)
output = call_7925
func_7928 = relay.Function([var_7926,var_7927,], output)
mutated_mod['func_7928'] = func_7928
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1896_call = mod.get_global_var('func_1896')
func_1898_call = mutated_mod.get_global_var('func_1898')
call_7972 = relay.TupleGetItem(func_1896_call(), 0)
call_7973 = relay.TupleGetItem(func_1898_call(), 0)
output = relay.Tuple([call_7972,])
output2 = relay.Tuple([call_7973,])
func_7976 = relay.Function([], output)
mod['func_7976'] = func_7976
mod = relay.transform.InferType()(mod)
mutated_mod['func_7976'] = func_7976
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7976_call = mutated_mod.get_global_var('func_7976')
call_7977 = func_7976_call()
output = call_7977
func_7978 = relay.Function([], output)
mutated_mod['func_7978'] = func_7978
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7983 = relay.var("var_7983", dtype = "uint16", shape = (9, 3, 3))#candidate|7983|(9, 3, 3)|var|uint16
const_7984 = relay.const([[[-6,-1,2],[-4,-9,-10],[-3,6,9]],[[8,7,-6],[2,-8,2],[8,10,-6]],[[1,5,-9],[10,1,3],[-8,-3,6]],[[-1,-1,-9],[10,-4,-9],[3,2,-9]],[[-4,-2,-6],[4,8,8],[-1,10,2]],[[7,-7,2],[-1,5,4],[4,-4,4]],[[-1,-4,8],[-3,-5,-10],[-4,-8,-10]],[[-8,-7,4],[-8,9,3],[2,4,5]],[[9,10,2],[-10,-9,-9],[1,9,2]]], dtype = "uint16")#candidate|7984|(9, 3, 3)|const|uint16
bop_7985 = relay.equal(var_7983.astype('bool'), relay.reshape(const_7984.astype('bool'), relay.shape_of(var_7983))) # shape=(9, 3, 3)
bop_7998 = relay.left_shift(var_7983.astype('uint8'), relay.reshape(bop_7985.astype('uint8'), relay.shape_of(var_7983))) # shape=(9, 3, 3)
func_2218_call = mod.get_global_var('func_2218')
func_2219_call = mutated_mod.get_global_var('func_2219')
call_8001 = relay.TupleGetItem(func_2218_call(), 3)
call_8002 = relay.TupleGetItem(func_2219_call(), 3)
output = relay.Tuple([bop_7998,call_8001,])
output2 = relay.Tuple([bop_7998,call_8002,])
func_8024 = relay.Function([var_7983,], output)
mod['func_8024'] = func_8024
mod = relay.transform.InferType()(mod)
mutated_mod['func_8024'] = func_8024
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8025 = relay.var("var_8025", dtype = "uint16", shape = (9, 3, 3))#candidate|8025|(9, 3, 3)|var|uint16
func_8024_call = mutated_mod.get_global_var('func_8024')
call_8026 = func_8024_call(var_8025)
output = call_8026
func_8027 = relay.Function([var_8025], output)
mutated_mod['func_8027'] = func_8027
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7976_call = mod.get_global_var('func_7976')
func_7978_call = mutated_mod.get_global_var('func_7978')
call_8092 = relay.TupleGetItem(func_7976_call(), 0)
call_8093 = relay.TupleGetItem(func_7978_call(), 0)
func_4252_call = mod.get_global_var('func_4252')
func_4254_call = mutated_mod.get_global_var('func_4254')
const_8110 = relay.const([1.709586,-6.464073,7.573232,-7.275050,-9.772633,-7.785097], dtype = "float64")#candidate|8110|(6,)|const|float64
call_8109 = relay.TupleGetItem(func_4252_call(relay.reshape(const_8110.astype('float64'), [6,])), 0)
call_8111 = relay.TupleGetItem(func_4254_call(relay.reshape(const_8110.astype('float64'), [6,])), 0)
output = relay.Tuple([call_8092,call_8109,const_8110,])
output2 = relay.Tuple([call_8093,call_8111,const_8110,])
func_8115 = relay.Function([], output)
mod['func_8115'] = func_8115
mod = relay.transform.InferType()(mod)
mutated_mod['func_8115'] = func_8115
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8115_call = mutated_mod.get_global_var('func_8115')
call_8116 = func_8115_call()
output = call_8116
func_8117 = relay.Function([], output)
mutated_mod['func_8117'] = func_8117
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3008_call = mod.get_global_var('func_3008')
func_3009_call = mutated_mod.get_global_var('func_3009')
call_8172 = func_3008_call()
call_8173 = func_3008_call()
output = relay.Tuple([call_8172,])
output2 = relay.Tuple([call_8173,])
func_8201 = relay.Function([], output)
mod['func_8201'] = func_8201
mod = relay.transform.InferType()(mod)
mutated_mod['func_8201'] = func_8201
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8201_call = mutated_mod.get_global_var('func_8201')
call_8202 = func_8201_call()
output = call_8202
func_8203 = relay.Function([], output)
mutated_mod['func_8203'] = func_8203
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1674_call = mod.get_global_var('func_1674')
func_1676_call = mutated_mod.get_global_var('func_1676')
call_8248 = relay.TupleGetItem(func_1674_call(), 0)
call_8249 = relay.TupleGetItem(func_1676_call(), 0)
output = call_8248
output2 = call_8249
func_8252 = relay.Function([], output)
mod['func_8252'] = func_8252
mod = relay.transform.InferType()(mod)
mutated_mod['func_8252'] = func_8252
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8252_call = mutated_mod.get_global_var('func_8252')
call_8253 = func_8252_call()
output = call_8253
func_8254 = relay.Function([], output)
mutated_mod['func_8254'] = func_8254
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1452_call = mod.get_global_var('func_1452')
func_1453_call = mutated_mod.get_global_var('func_1453')
call_8374 = func_1452_call()
call_8375 = func_1452_call()
func_7600_call = mod.get_global_var('func_7600')
func_7601_call = mutated_mod.get_global_var('func_7601')
call_8381 = func_7600_call()
call_8382 = func_7600_call()
output = relay.Tuple([call_8374,call_8381,])
output2 = relay.Tuple([call_8375,call_8382,])
func_8397 = relay.Function([], output)
mod['func_8397'] = func_8397
mod = relay.transform.InferType()(mod)
output = func_8397()
func_8398 = relay.Function([], output)
mutated_mod['func_8398'] = func_8398
mutated_mod = relay.transform.InferType()(mutated_mod)
const_8413 = relay.const([[0.497027,7.662182,1.873558,-7.756377,5.524175,-4.241298,-6.483081,5.164994,-2.080805,-2.391008,-7.409362],[7.640860,-3.338681,1.121153,9.070084,-1.322683,7.332227,-0.340050,-2.055431,3.520036,5.533990,6.744410],[6.730916,2.306618,-4.234208,4.603689,6.189157,-5.340475,5.245542,-7.719075,-9.673740,2.177172,-9.057755],[3.829922,3.773340,-1.441096,-2.119047,-1.300710,-3.813748,-3.672686,4.636897,2.544192,-4.401884,-5.086863],[5.893683,-7.921834,-6.157522,6.325465,4.485983,9.763551,5.162092,9.961480,9.136317,-8.133081,1.611343],[-6.477942,-5.433076,-7.722695,0.161458,-5.227581,3.358900,-6.696768,-6.657292,-3.869054,-7.595030,-8.048244],[9.794532,-7.700495,2.403931,-5.425994,0.092842,6.579721,-2.022002,-8.764678,4.858139,-6.767648,7.233391]], dtype = "float64")#candidate|8413|(7, 11)|const|float64
uop_8414 = relay.cosh(const_8413.astype('float64')) # shape=(7, 11)
func_7647_call = mod.get_global_var('func_7647')
func_7650_call = mutated_mod.get_global_var('func_7650')
var_8420 = relay.var("var_8420", dtype = "float32", shape = (192,))#candidate|8420|(192,)|var|float32
call_8419 = relay.TupleGetItem(func_7647_call(relay.reshape(var_8420.astype('float32'), [192,])), 3)
call_8421 = relay.TupleGetItem(func_7650_call(relay.reshape(var_8420.astype('float32'), [192,])), 3)
func_3709_call = mod.get_global_var('func_3709')
func_3711_call = mutated_mod.get_global_var('func_3711')
call_8422 = func_3709_call()
call_8423 = func_3709_call()
func_6859_call = mod.get_global_var('func_6859')
func_6861_call = mutated_mod.get_global_var('func_6861')
call_8425 = relay.TupleGetItem(func_6859_call(), 1)
call_8426 = relay.TupleGetItem(func_6861_call(), 1)
output = relay.Tuple([uop_8414,call_8419,var_8420,call_8422,call_8425,])
output2 = relay.Tuple([uop_8414,call_8421,var_8420,call_8423,call_8426,])
func_8433 = relay.Function([var_8420,], output)
mod['func_8433'] = func_8433
mod = relay.transform.InferType()(mod)
mutated_mod['func_8433'] = func_8433
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8434 = relay.var("var_8434", dtype = "float32", shape = (192,))#candidate|8434|(192,)|var|float32
func_8433_call = mutated_mod.get_global_var('func_8433')
call_8435 = func_8433_call(var_8434)
output = call_8435
func_8436 = relay.Function([var_8434], output)
mutated_mod['func_8436'] = func_8436
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7084_call = mod.get_global_var('func_7084')
func_7086_call = mutated_mod.get_global_var('func_7086')
call_8449 = func_7084_call()
call_8450 = func_7084_call()
func_7924_call = mod.get_global_var('func_7924')
func_7928_call = mutated_mod.get_global_var('func_7928')
const_8453 = relay.const([5.616262,-7.174245,7.880705,5.131186,-6.670361,-6.828511,8.876308,6.762483,7.099990,-3.330050,8.976883,0.485274,-3.092420,6.722866,9.772962,2.099150,6.947471,-2.428593,-1.674341,-1.485932,-8.348898,-3.048925,6.016251,-7.755452,0.003750,3.547054,-4.187137,7.466975,-8.298994,-1.814274,-7.994608,-3.979240,2.764581,-5.945445,-7.519355,-2.319293,-0.121681,-6.510796,-7.036463,-4.735431,0.038086,-0.220685,-4.811249,-2.491741,5.817063,4.807436,7.295627,2.501110,-8.911314,-4.416482,-4.371038,-8.857405,-5.672989,-6.579636,3.497247,-9.653933,-4.886385,4.210829,-9.704532,8.616523,-0.292321,6.008993,-2.896696,0.056319,4.124396,5.689496,-6.364501,-1.036766,-5.383720,-8.247556,3.264024,-0.344235,1.389655,-0.342325,-4.544421,3.276813,-2.410039,-7.748700,1.951285,-5.104600,8.389200,-1.983437,0.917521,-2.770606,1.822231,1.420184,7.797403,9.322337,1.538492,-7.056022,3.392467,1.886840,4.682629,1.840895,0.107386,6.267822,9.639864,-0.923438,-0.190121,3.401056,9.061133,-2.931903,-1.242690,-5.728471,0.947400,5.040596,-7.529456,7.658652,-0.291851,1.250099,-7.188584,4.674566,-8.627461,-0.439921,-3.740408,5.329674,-9.564009,0.691990,4.289635,7.527239], dtype = "float32")#candidate|8453|(120,)|const|float32
call_8452 = relay.TupleGetItem(func_7924_call(relay.reshape(const_8453.astype('float32'), [3, 5, 8]), relay.reshape(const_8453.astype('float32'), [3, 5, 8]), ), 4)
call_8454 = relay.TupleGetItem(func_7928_call(relay.reshape(const_8453.astype('float32'), [3, 5, 8]), relay.reshape(const_8453.astype('float32'), [3, 5, 8]), ), 4)
output = relay.Tuple([call_8449,call_8452,const_8453,])
output2 = relay.Tuple([call_8450,call_8454,const_8453,])
func_8457 = relay.Function([], output)
mod['func_8457'] = func_8457
mod = relay.transform.InferType()(mod)
output = func_8457()
func_8458 = relay.Function([], output)
mutated_mod['func_8458'] = func_8458
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5215_call = mod.get_global_var('func_5215')
func_5216_call = mutated_mod.get_global_var('func_5216')
call_8472 = relay.TupleGetItem(func_5215_call(), 0)
call_8473 = relay.TupleGetItem(func_5216_call(), 0)
func_4189_call = mod.get_global_var('func_4189')
func_4191_call = mutated_mod.get_global_var('func_4191')
const_8479 = relay.const([10,3,-10,6,-8,-5,-9,-5,5,3,-2,-8,-7,-7,6,-5,3,6,-1,-9,9,9,-10,8,-6,3,-9,4,-7,3,2,10,5,1,8,2,5,5,10,1,6,5,8,-1,10,-8,9,-10,-6,10,-2,-1,-6,2,-10,3,8,9,-7,1,-4,2,9,-10,4,8,4,4,-6,7,9,9,-10,-5,1,-6,7,2,1,-2,4,4,-9,-10,-3,10,7,-9,-10,-5,10,-9,1,-4,5,-9,8,-9,-10,-2,3,4,3,-10,10,5,-7,7,-6,-2,9,-10,-5,-3,-7,9,-9,4,10,5,7,10,-2,4,1,1,-9,4,1,10,-6,-7,-6,7,5,6,1,8,6,-5,9,-5,-6,-4,-8,-4,5,-9,4,-9,-9,-1,-2,8,-2,-2,-7,-1,8,10,10,-2,5,6,-1,-8,-1,-3,-9,-10,3,4,-1,-3,-10,6,-4,5,-2,-9,-7,5,6,-10,8,8,1,1,6,-10,-4,-6,-7,-10,-3,3,-7,-7,-6,-8,4,6,-7,-7,9,-1,6,-3,-8,1,3,-1,-2,-3,-5,3,-8,-5,3,10,-1,-7,10,-9,5,10,-6,8,1,-6,-4,-6,-7,-7,-4,4,-10,2,1,8,1,-3,1,7,-5,-8,4,-9,-8,-3,5,-10,8,-5,-3,-6,1,5,3,5,5,-4,1,1,-4,-2,4,4,-3,-5,-9,5,10,-3,-10,-10,-6,-7,2,4,4,4,7,-4,-6,9,7,7,-3,-2,-1,-1,9,-1,6,6,3,-10,8,3,10,-9,-5,8,-7,3,3,4,-2,2,2,7,-7,-8,-10,9,4,-9,-4,-8,-7,10,5,-3,-1,-4,-4,10,8,6,-2,10,-5,-4,-7,-4,3,6,8,-4,4,-3,1,-10,5,6,3,1,6,10,6,-8,10,7,-3,8,-1,4,4,10,9,5,6,1,1,-5,-7,-6,-9,4,5,9,-3,-9,-6,6,-7,-9,-9,4,4,-7,-4,-8,7,5,4,-10,-7,-3,10,-8,4,-1,-10,3,6,-4,6,-5,4,4,6,-6,-5,-5,10,-3,3,-7,8,-4,1,-5,2,9,2,5,-9,10,-9,10,-10,-4,-6,-3,-1,1,9,-9,5,-6,-9,-4,9,4,-9,-7,-7,10,-10,-10,-4,-2,-6,-1,-7,10,7,6,-8,-3,-7,3,-9,-9,-8,1,9,-4,-2,-8,3,7,-3,-7,5,7,-10,8,-7,-2,6,-6,5,-2,6,-8,-9,10,-7,-3,7,-6,4,8,-3,-4,-2,-5,-4,-5,-8,-9,7,-9,6,-9,-3,10,3,7,-8,6,-5,8,10,2,-6,5,2,-10,-7,1,-7,9,9,-3,-1,9,-10,7,-2,-7,10,4,7,10,2,-8,-2,-9,5,10,-3,-1,-7,4,-7,-10,5,9,-7,-10,10,-9,2,-5,-10,-2,5,-5,-2,-4,1,8,-5,2,5,10,-7,-10,-5,-6,10,-7,1,-9,-4,-4,4,-3,-10,-10,4,-2,9,9,-7,-2,-3,3,-2,9,-5,10,-6,10,-7,-2,-2,-1,-4,-8,7,7,-8,6,-3,7,1,-7,2,2,8,10,8,-1,-6,-3,-7,-5,-3,7,9,3,-1,6,6,3,-1,1,8,2,-1,7,9,4,-6,-9,-5,2,1,-1,5,2,-1,-7,-7,3,8,-7,-3,-1,2,-1,-2,-4,10,-1,-1,2,6,-1,10,10,-3,5,7,-4,-5,7,9,-2,9,3,-6,2,-6,-4,6,-4,-8,6,4,4,4,-9,-3,1,4,-1,-10,-4,-9,-1,-10,-5,-4,4,8,1,9,4,-3,-3,-8,-9,1,-3,2,5,-10,10,1,4,-4,-1,7,7,10,-8,6,5,3,-10,-5,-6,-7,-9,-2,8,-9,1,4,-7,7,3,7,3,-9,6,9,-8,-10,-5,-1,-10,-1,10,8,2,-5,9,2,-3,-8,-4,10,-3,9,3,-2,2,-4,9,-2,-7,5,-8,-9,-7,-9,-4,-2,-9,7,-1,-5,-2,-7,-10,1,5,-3,-2,-5,9,-1,3,2,-4,-4,-9,10,-7,-2,8,-2,1,10,-10,-4,1,4,9,-7,-6,-8,1,6,-6,3,-4,-1,-4,8,-5,3,-8,-3,-2,9,-1,-2,-6,-10,-7,-8,-2,7,9,-8,-8,2,7,-4,-6,-8,2,1,10,-10,-4,9,-7,-2,2,3,-10,-7,-10,7,-5,-7,6,-3,-7,5,-1,-9,-1,-5,10,4,-2,-8,-3,2,-1,5,5,6,-2,7,-5,4,-9,10,8,9,6,-6,-4,7,5,5,-3,-6,-3,-10,9,-8,-4,8,-2,-4,6,-7,8,6,-9,5,-5,9,-4,-10,-5,-3,-7,-3,-10,9,-6,-6,2,10,-6,-5,6,1,-3,4,9,8,-10,7,9,8,4,-2,8,10,-6,5,9,1,8,1,-7,-5,2,-9,-10,6,8,2,9,10,-7,7,-2,9,6,-9,-8,1,10,1,-4,-6,7,10,10,-3,-6,4,-9,-10,-2,9,5,2,-8,7,-3,6,-3,-8,-8,-1,-9,4,7,-4,-3,10,1,-5,-4,2,-9,7,-9,-6,-6,-3,1,5,-9,6,-2,-2,-6,-5,-3,-10,-7,4,-4,5,7,-8,-3,-4,-4,6,7,-2,-7,5,-3,-2,-4,10,-7,1,-1,2,-2,10,-9,3,-6,-8,1,3,-10,8,-1,5,1,2,5,-10,10,-4,-4,-4,-3,3,8,9,1,4,-4,-2,5,1,-9,6,8,-8,-8,-5,5,-4,-6,-10,8,10,5,1,7,-9,-10,6,6,2,-8,-4,7,-7,8,-9,-3,10,-1,7,2,4,10,10,8,9,-1,1,10,-10,-7,-7,-5,8,8,6,3,2,2,9,-7,7,5,5,-6,-4,-1,-3,9,-4,9,7,-2,5,-2,-5,7,7,2,7,-7,10,1,-6,-9,7,2,1,-4,9,3,5,8,1,-3,7,-9,-8,2,-3,4,-8,6,10,6,-6,-5,-10,-10,-2,-9,-3,-6,1,2,-9,-5,-3,-8,9,-4,2,5,-2,-3,9,3,-10,-2,-9,4,3,6,-10,-10,-8,-5,6,4,-6,4,9,-7,8,-10,4,-6,-5,2,9,-4,8,9,9,4,10,-1,5,8,7,-10,-3,-7,-9,4,5,-4,7,-9,-9,-2,-10,8,2,9,-5,2,3,6,10,-9,8,-8,-9,3,-9,-6,9,4,-1,1,-10,-4,4,-7,2,9,-1,4,3,9,4,3,-9,-5,8,6,8,-4,-2,7,1,3,-5,4,-6,-2,-8,4,-9,-8,4,8,-8,6,-5,5,1,8,6,-3,-4,-5,-9,-10,7,-7,3,-6,-10,-10,-5,9,-2,-1,-10,3,9,-6,6,-7,3,-7,-1,-9,3,-6,-4,-6,3,-5,2,-8,-7,-9,10,7,2,-4,-4,4,2,-10,4,-1,3,-1,-5,6,-3,6,-1,-1,-6,5,-7,9,-10,4,-5,2,-2,-3,-2,-10,3,8,-8,6,3,-5,-2,-8,3,10,-8,8,-5,-10,9,10,5,-4,7,6,-3,10,5,-10,9,-8,2,8,8,-2,7,9,-2,-4,4,8,-3,3,-6,8,-2,-2,-4,-2,8,9,8,7,10,-10,3,10,-6,-4,5,-10,10,-1,-4,-7,7,-8,-4,6,6,6,5,3,-8,-6,9,-2,-9,3,6,-6,8,1,-8,-5,4,-2,-7,2,4,-2,5,-3,-7,-6,8,7,5,-7,-6,7,-4,-8,-6,10,-10,4,-6,-10,3,5,9,9,-9,-8,9,-4,-6,7,7,-1,-10,2,2,-9,9,6], dtype = "uint32")#candidate|8479|(1456,)|const|uint32
call_8478 = relay.TupleGetItem(func_4189_call(relay.reshape(const_8479.astype('uint32'), [16, 7, 13])), 0)
call_8480 = relay.TupleGetItem(func_4191_call(relay.reshape(const_8479.astype('uint32'), [16, 7, 13])), 0)
uop_8503 = relay.log2(call_8478.astype('float64')) # shape=(16, 7, 13)
uop_8505 = relay.log2(call_8480.astype('float64')) # shape=(16, 7, 13)
func_4138_call = mod.get_global_var('func_4138')
func_4140_call = mutated_mod.get_global_var('func_4140')
call_8521 = relay.TupleGetItem(func_4138_call(), 0)
call_8522 = relay.TupleGetItem(func_4140_call(), 0)
func_1615_call = mod.get_global_var('func_1615')
func_1616_call = mutated_mod.get_global_var('func_1616')
call_8523 = func_1615_call()
call_8524 = func_1615_call()
output = relay.Tuple([call_8472,const_8479,uop_8503,call_8521,call_8523,])
output2 = relay.Tuple([call_8473,const_8479,uop_8505,call_8522,call_8524,])
func_8530 = relay.Function([], output)
mod['func_8530'] = func_8530
mod = relay.transform.InferType()(mod)
mutated_mod['func_8530'] = func_8530
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8530_call = mutated_mod.get_global_var('func_8530')
call_8531 = func_8530_call()
output = call_8531
func_8532 = relay.Function([], output)
mutated_mod['func_8532'] = func_8532
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8587 = relay.var("var_8587", dtype = "float64", shape = (1, 16, 13))#candidate|8587|(1, 16, 13)|var|float64
uop_8588 = relay.atanh(var_8587.astype('float64')) # shape=(1, 16, 13)
func_3865_call = mod.get_global_var('func_3865')
func_3867_call = mutated_mod.get_global_var('func_3867')
const_8621 = relay.const([5.593033,-9.446979,8.960967,6.507242,-7.836297,-9.393202], dtype = "float64")#candidate|8621|(6,)|const|float64
call_8620 = relay.TupleGetItem(func_3865_call(relay.reshape(const_8621.astype('float64'), [6,])), 1)
call_8622 = relay.TupleGetItem(func_3867_call(relay.reshape(const_8621.astype('float64'), [6,])), 1)
uop_8634 = relay.exp(uop_8588.astype('float64')) # shape=(1, 16, 13)
bop_8636 = relay.floor_mod(uop_8588.astype('float32'), relay.reshape(var_8587.astype('float32'), relay.shape_of(uop_8588))) # shape=(1, 16, 13)
func_1865_call = mod.get_global_var('func_1865')
func_1867_call = mutated_mod.get_global_var('func_1867')
var_8653 = relay.var("var_8653", dtype = "float32", shape = (4, 48))#candidate|8653|(4, 48)|var|float32
call_8652 = relay.TupleGetItem(func_1865_call(relay.reshape(var_8653.astype('float32'), [192, 1])), 0)
call_8654 = relay.TupleGetItem(func_1867_call(relay.reshape(var_8653.astype('float32'), [192, 1])), 0)
uop_8659 = relay.asinh(uop_8634.astype('float32')) # shape=(1, 16, 13)
output = relay.Tuple([call_8620,const_8621,bop_8636,call_8652,var_8653,uop_8659,])
output2 = relay.Tuple([call_8622,const_8621,bop_8636,call_8654,var_8653,uop_8659,])
func_8661 = relay.Function([var_8587,var_8653,], output)
mod['func_8661'] = func_8661
mod = relay.transform.InferType()(mod)
var_8662 = relay.var("var_8662", dtype = "float64", shape = (1, 16, 13))#candidate|8662|(1, 16, 13)|var|float64
var_8663 = relay.var("var_8663", dtype = "float32", shape = (4, 48))#candidate|8663|(4, 48)|var|float32
output = func_8661(var_8662,var_8663,)
func_8664 = relay.Function([var_8662,var_8663,], output)
mutated_mod['func_8664'] = func_8664
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7084_call = mod.get_global_var('func_7084')
func_7086_call = mutated_mod.get_global_var('func_7086')
call_8668 = func_7084_call()
call_8669 = func_7084_call()
output = call_8668
output2 = call_8669
func_8699 = relay.Function([], output)
mod['func_8699'] = func_8699
mod = relay.transform.InferType()(mod)
mutated_mod['func_8699'] = func_8699
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8699_call = mutated_mod.get_global_var('func_8699')
call_8700 = func_8699_call()
output = call_8700
func_8701 = relay.Function([], output)
mutated_mod['func_8701'] = func_8701
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5215_call = mod.get_global_var('func_5215')
func_5216_call = mutated_mod.get_global_var('func_5216')
call_8709 = relay.TupleGetItem(func_5215_call(), 0)
call_8710 = relay.TupleGetItem(func_5216_call(), 0)
func_4374_call = mod.get_global_var('func_4374')
func_4376_call = mutated_mod.get_global_var('func_4376')
call_8722 = relay.TupleGetItem(func_4374_call(), 0)
call_8723 = relay.TupleGetItem(func_4376_call(), 0)
output = relay.Tuple([call_8709,call_8722,])
output2 = relay.Tuple([call_8710,call_8723,])
func_8734 = relay.Function([], output)
mod['func_8734'] = func_8734
mod = relay.transform.InferType()(mod)
mutated_mod['func_8734'] = func_8734
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8734_call = mutated_mod.get_global_var('func_8734')
call_8735 = func_8734_call()
output = call_8735
func_8736 = relay.Function([], output)
mutated_mod['func_8736'] = func_8736
mutated_mod = relay.transform.InferType()(mutated_mod)
const_8770 = relay.const([[[-3.899742,-5.677474,4.456370,-2.794780,7.828362],[9.714797,0.194890,-8.396155,0.964239,3.539001],[-5.502150,4.048022,3.608031,3.705777,-5.241683],[-1.450842,-9.599652,3.300613,5.039281,3.953480],[-8.273347,-2.341537,-2.552615,0.688510,4.490821],[4.127953,4.530116,-3.812368,-6.249863,0.291078],[-0.094108,-8.917538,0.742714,-5.970183,0.491119],[4.102511,5.227711,7.608264,-1.914214,5.329199],[1.993898,5.508003,3.275676,6.808951,-5.974426],[-8.886045,1.034018,6.816286,5.019761,3.671397],[5.403254,-9.532836,-5.575368,-1.940509,-1.478929],[-5.987892,-8.058693,-1.509063,9.316876,-5.889838]],[[1.356473,-3.764775,2.803798,3.684031,-1.264420],[2.435253,4.904327,-1.809431,7.798485,-2.836661],[-6.553391,5.193304,-5.173782,6.938875,7.105884],[0.234232,-0.365599,7.857647,-3.975750,-5.090762],[2.118423,-8.626616,1.560705,5.807014,-8.612752],[5.263174,-7.557113,4.153612,-2.317216,1.731974],[-7.354023,-3.123846,-4.715615,-1.461804,-2.496874],[8.018777,-8.271530,-5.758217,-8.993379,-4.150139],[0.907180,-0.347674,-0.200428,8.831517,-8.464108],[7.743766,1.857926,5.090373,5.977202,-0.694265],[4.556206,-4.876956,-9.416094,8.290186,-7.020967],[4.405329,4.256932,2.942600,7.337205,0.688855]],[[9.959789,9.057536,-2.446643,8.643632,-6.296423],[-1.312347,4.174299,-3.961539,2.311541,5.272111],[0.647966,-7.324826,-5.362836,2.118755,-4.518245],[9.804174,1.548191,-0.992897,3.849025,7.626026],[-7.789716,4.199901,-4.961191,3.046131,-9.581262],[7.270574,0.765983,-1.075812,-7.054300,2.020016],[-6.376627,-2.010985,6.975064,-1.883311,-7.801302],[2.806523,0.239874,3.770952,-6.357302,1.575597],[6.866101,-0.030093,-5.481147,-0.364423,-2.120075],[0.120394,-6.462924,-0.673566,4.709755,-7.667182],[1.859005,-9.423223,3.666914,-8.661365,-2.220505],[-7.326737,5.098851,-4.886233,0.106622,-5.571368]],[[-7.746503,4.319716,9.118237,9.266423,-7.128230],[6.309108,4.439408,-2.382383,8.629872,-2.913427],[-7.627491,2.810085,9.924791,-1.001563,-3.736229],[3.563212,-1.204264,1.775134,-2.524351,-9.453530],[-0.856019,-4.545354,2.722250,-6.543235,-7.689702],[-6.687872,5.573922,-1.182669,9.269226,-8.923506],[5.804050,9.177743,-0.727954,9.469379,5.955281],[3.060024,2.520749,7.508301,-8.589303,6.995294],[-5.485290,1.476115,0.815397,-5.641677,-3.317557],[-6.922639,-2.996780,-5.104357,-0.470964,-7.452511],[8.585869,-6.556208,1.471036,-8.058410,0.682497],[-7.076386,5.770064,-7.618472,7.809282,-1.086692]],[[2.782939,5.160850,-5.745537,-9.434414,-9.388786],[-6.038312,-8.611951,-9.571024,-7.218507,3.621762],[4.945120,8.911177,2.650586,1.220577,-2.214214],[6.869627,0.984953,-7.260136,-0.135975,-2.737491],[9.834558,-5.004634,5.282058,1.549492,6.067346],[-0.224297,1.104362,-6.296255,9.326193,2.405318],[8.762510,6.394443,-9.856078,-3.515919,-4.321872],[5.720614,1.522555,6.310902,-4.299529,-4.070223],[6.286715,-4.840814,-4.277533,2.132248,5.901667],[3.657956,2.084354,7.738447,-2.511210,-2.428458],[-0.811322,-3.818108,-9.596074,4.510525,0.376706],[-9.721547,-0.278121,1.959122,3.496604,-6.585963]],[[9.530550,9.437182,-1.536258,-5.804095,-4.863491],[0.786736,-8.152970,-0.412878,6.290893,-2.481132],[1.503786,5.483571,0.292272,-8.695046,3.325542],[6.247937,2.766154,-5.470096,8.856858,-5.557589],[2.818508,8.449436,-9.911304,-1.682044,2.967631],[-0.180997,-3.213668,-6.616836,-9.950309,-9.718259],[6.148777,-7.473124,9.240099,-7.212300,-7.980784],[-6.289634,-1.396639,6.438682,-5.715475,-1.932213],[-7.878620,-6.663501,-2.956409,1.137765,-3.711884],[-8.253873,0.017826,-9.168306,1.896104,-6.428534],[1.328124,-8.817445,-0.728743,-1.621825,7.230132],[-4.199185,7.871035,-8.677616,8.589958,-0.984341]],[[-3.399108,1.149264,-5.200575,-5.028284,-4.984778],[9.375516,8.789998,9.199779,8.883437,-5.474491],[-9.331940,1.842906,-1.022445,0.751413,6.102287],[5.250351,-7.282912,7.772738,-9.338976,9.877043],[-6.333966,-9.298565,-7.916576,6.871523,-1.761408],[-3.199313,-3.498764,-5.771410,-5.242237,-7.371625],[-5.911343,0.497530,-3.617860,3.473669,-6.199624],[7.505357,7.330617,-0.493247,5.415657,9.863837],[-1.731481,-1.683248,2.141304,9.841729,-6.954177],[3.400066,6.689137,-7.860535,-8.182193,-2.508620],[-4.932484,9.591888,7.500744,2.722350,-4.562422],[-2.633226,-5.407588,3.525374,-8.115484,3.981243]],[[3.638655,9.658738,9.473329,-9.565732,6.577920],[-2.281989,8.061259,5.841623,-8.437424,2.752724],[5.748140,6.207156,9.643187,-1.740432,2.635959],[-6.837408,-0.024528,7.532755,5.283964,9.957357],[-0.059903,-8.042399,-8.201155,-5.644366,-1.154746],[3.045688,-9.364990,-1.708766,3.490968,4.345067],[-9.562951,5.252205,0.871111,7.546383,5.405243],[9.084103,-5.056547,4.785419,4.085875,5.593174],[8.665612,9.570599,8.275278,2.205664,-5.912105],[0.206334,0.700894,-1.163460,1.000176,4.822091],[-2.025200,-8.085700,4.346158,0.626398,-0.356074],[-1.274813,5.597856,0.428451,4.892939,-4.097782]]], dtype = "float32")#candidate|8770|(8, 12, 5)|const|float32
uop_8771 = relay.cosh(const_8770.astype('float32')) # shape=(8, 12, 5)
func_1316_call = mod.get_global_var('func_1316')
func_1317_call = mutated_mod.get_global_var('func_1317')
call_8778 = func_1316_call()
call_8779 = func_1316_call()
output = relay.Tuple([uop_8771,call_8778,])
output2 = relay.Tuple([uop_8771,call_8779,])
func_8786 = relay.Function([], output)
mod['func_8786'] = func_8786
mod = relay.transform.InferType()(mod)
output = func_8786()
func_8787 = relay.Function([], output)
mutated_mod['func_8787'] = func_8787
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8788 = relay.var("var_8788", dtype = "int8", shape = ())#candidate|8788|()|var|int8
var_8789 = relay.var("var_8789", dtype = "int8", shape = (8, 1, 1))#candidate|8789|(8, 1, 1)|var|int8
bop_8790 = relay.greater(var_8788.astype('bool'), var_8789.astype('bool')) # shape=(8, 1, 1)
bop_8795 = relay.add(var_8789.astype('int32'), relay.reshape(bop_8790.astype('int32'), relay.shape_of(var_8789))) # shape=(8, 1, 1)
func_5883_call = mod.get_global_var('func_5883')
func_5885_call = mutated_mod.get_global_var('func_5885')
call_8800 = func_5883_call()
call_8801 = func_5883_call()
output = relay.Tuple([bop_8795,call_8800,])
output2 = relay.Tuple([bop_8795,call_8801,])
func_8806 = relay.Function([var_8788,var_8789,], output)
mod['func_8806'] = func_8806
mod = relay.transform.InferType()(mod)
var_8807 = relay.var("var_8807", dtype = "int8", shape = ())#candidate|8807|()|var|int8
var_8808 = relay.var("var_8808", dtype = "int8", shape = (8, 1, 1))#candidate|8808|(8, 1, 1)|var|int8
output = func_8806(var_8807,var_8808,)
func_8809 = relay.Function([var_8807,var_8808,], output)
mutated_mod['func_8809'] = func_8809
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3588_call = mod.get_global_var('func_3588')
func_3590_call = mutated_mod.get_global_var('func_3590')
call_8821 = func_3588_call()
call_8822 = func_3588_call()
output = call_8821
output2 = call_8822
func_8823 = relay.Function([], output)
mod['func_8823'] = func_8823
mod = relay.transform.InferType()(mod)
output = func_8823()
func_8824 = relay.Function([], output)
mutated_mod['func_8824'] = func_8824
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6505_call = mod.get_global_var('func_6505')
func_6506_call = mutated_mod.get_global_var('func_6506')
call_8827 = func_6505_call()
call_8828 = func_6505_call()
output = call_8827
output2 = call_8828
func_8831 = relay.Function([], output)
mod['func_8831'] = func_8831
mod = relay.transform.InferType()(mod)
output = func_8831()
func_8832 = relay.Function([], output)
mutated_mod['func_8832'] = func_8832
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8841 = relay.var("var_8841", dtype = "int16", shape = (16, 2, 13))#candidate|8841|(16, 2, 13)|var|int16
const_8842 = relay.const([[[-4,-1,-3,8,2,-7,-6,-8,-9,-6,7,8,-2],[8,10,8,-6,2,-7,-1,-6,8,9,10,8,7]],[[-2,3,1,9,-9,-7,5,-6,2,3,-4,-9,6],[-3,9,-10,-4,2,2,-7,8,8,3,-6,-3,-4]],[[10,2,-5,10,4,5,-1,-5,8,-6,8,-10,1],[-8,6,1,-7,4,7,-6,-6,-3,7,1,-10,2]],[[4,8,9,-8,-8,-3,-2,-7,-2,4,-5,4,2],[5,-4,-9,8,-2,5,-4,-10,8,-5,-3,-9,7]],[[-3,-3,-8,-9,7,3,-7,-4,6,5,-4,-8,-7],[8,-9,9,-7,8,-3,10,-5,5,7,-4,7,8]],[[2,2,10,-5,-6,2,-7,1,-7,9,-3,4,4],[-2,5,6,-10,7,8,-1,-10,-8,-3,-6,9,2]],[[2,1,-2,-8,-6,6,-3,-6,-7,-7,-9,-4,5],[3,-9,-5,9,-6,-2,-9,1,2,8,-6,2,4]],[[2,4,-1,-3,-1,9,6,-2,2,-7,-7,-6,5],[-2,9,10,5,1,10,6,2,-1,1,-9,3,3]],[[-2,-6,2,8,5,3,10,8,7,9,-9,10,-4],[-4,-4,8,7,7,-2,-3,10,7,-9,10,-10,5]],[[-1,-1,3,-3,-2,5,5,-9,6,3,9,6,8],[-3,-8,6,-5,-6,10,-7,2,-2,-5,-5,-6,-5]],[[-10,-2,-10,7,-5,-9,9,1,7,-6,2,-8,-10],[6,-1,10,5,-2,-6,2,1,4,-7,3,-4,4]],[[6,3,-3,1,-1,7,-2,-8,5,2,1,8,-4],[3,8,4,-7,10,-7,6,-4,3,-10,-4,2,3]],[[-5,-3,-1,-7,-2,-3,-9,1,-5,-5,9,-5,-10],[6,-7,7,-9,3,5,-1,10,-7,8,-6,-6,4]],[[-8,4,7,1,-10,-8,-9,1,10,10,-7,-10,7],[-1,-6,8,-1,-3,4,-4,2,-3,4,2,7,3]],[[-3,10,8,4,-4,9,7,-6,4,7,-2,7,-6],[10,-3,7,6,7,-9,-8,-5,10,9,-7,6,10]],[[-4,-5,-6,-2,-8,6,-8,-7,-5,-2,4,-6,-8],[7,-5,-3,2,9,-3,-6,10,4,-6,-5,-8,3]]], dtype = "int16")#candidate|8842|(16, 2, 13)|const|int16
bop_8843 = relay.bitwise_xor(var_8841.astype('int16'), relay.reshape(const_8842.astype('int16'), relay.shape_of(var_8841))) # shape=(16, 2, 13)
var_8850 = relay.var("var_8850", dtype = "int16", shape = (16, 2, 13))#candidate|8850|(16, 2, 13)|var|int16
bop_8851 = relay.mod(bop_8843.astype('float32'), relay.reshape(var_8850.astype('float32'), relay.shape_of(bop_8843))) # shape=(16, 2, 13)
func_4736_call = mod.get_global_var('func_4736')
func_4737_call = mutated_mod.get_global_var('func_4737')
call_8866 = relay.TupleGetItem(func_4736_call(), 0)
call_8867 = relay.TupleGetItem(func_4737_call(), 0)
func_2294_call = mod.get_global_var('func_2294')
func_2295_call = mutated_mod.get_global_var('func_2295')
call_8875 = relay.TupleGetItem(func_2294_call(), 0)
call_8876 = relay.TupleGetItem(func_2295_call(), 0)
func_1674_call = mod.get_global_var('func_1674')
func_1676_call = mutated_mod.get_global_var('func_1676')
call_8879 = relay.TupleGetItem(func_1674_call(), 1)
call_8880 = relay.TupleGetItem(func_1676_call(), 1)
func_4613_call = mod.get_global_var('func_4613')
func_4616_call = mutated_mod.get_global_var('func_4616')
const_8889 = relay.const([-7.296360,-7.486665,1.465455,4.789466,-2.049808,-4.673151,9.252959,-9.097002,-4.620943,3.552554,1.069450,-7.393463,1.687884,8.441141,-3.791428,-4.160746,0.354885,4.154827,2.879432,2.481574,-2.178458,3.190488,-9.252671,6.662645,-8.352182,2.039661,0.400882,6.287018,-2.810715,-5.041652,-7.318724,2.798420,5.244829,-4.099730,-1.911809,-2.449168,-2.241239,-3.995926,-0.332374,8.018244,1.125280,-6.666983,-0.437438,7.181031,-8.490163,8.230065,-4.499738,-8.636824,-4.561501,-0.190431,0.635981,3.914418,-9.069211,-1.399011,-0.892794,9.376127,-5.269519,-3.482148,3.705586,2.762779,9.209170,9.850549,1.361730,2.431990,-4.955199,-7.301251,8.539938,1.331243,-3.169498,-8.880286,0.172421,-1.505284,7.296515,-6.648889,-7.025958,-1.315636,3.744657,9.042513,5.816145,-0.967943,-3.402115,8.362665,-8.020417,7.704549,-8.765260,1.790292,1.856177,7.270359,8.134909,-7.886120,8.274398,5.943860,-2.306231,-0.670348,-5.664213,8.613034,0.281846,-6.439256,-6.475390,-5.546388,0.565050,-0.604265,7.888046,3.324753,-1.748056,-1.898329,-1.524020,-4.938898,-4.919562,-0.542439,5.968205,8.875102,9.530380,-0.681045,2.452438,-2.834956,6.467725,-8.460175,1.543617,8.461833], dtype = "float32")#candidate|8889|(120,)|const|float32
call_8888 = relay.TupleGetItem(func_4613_call(relay.reshape(const_8889.astype('float32'), [3, 5, 8])), 2)
call_8890 = relay.TupleGetItem(func_4616_call(relay.reshape(const_8889.astype('float32'), [3, 5, 8])), 2)
output = relay.Tuple([bop_8851,call_8866,call_8875,call_8879,call_8888,const_8889,])
output2 = relay.Tuple([bop_8851,call_8867,call_8876,call_8880,call_8890,const_8889,])
func_8893 = relay.Function([var_8841,var_8850,], output)
mod['func_8893'] = func_8893
mod = relay.transform.InferType()(mod)
mutated_mod['func_8893'] = func_8893
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8893_call = mutated_mod.get_global_var('func_8893')
var_8895 = relay.var("var_8895", dtype = "int16", shape = (16, 2, 13))#candidate|8895|(16, 2, 13)|var|int16
var_8896 = relay.var("var_8896", dtype = "int16", shape = (16, 2, 13))#candidate|8896|(16, 2, 13)|var|int16
call_8894 = func_8893_call(var_8895,var_8896,)
output = call_8894
func_8897 = relay.Function([var_8895,var_8896,], output)
mutated_mod['func_8897'] = func_8897
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2827_call = mod.get_global_var('func_2827')
func_2828_call = mutated_mod.get_global_var('func_2828')
call_8901 = func_2827_call()
call_8902 = func_2827_call()
output = relay.Tuple([call_8901,])
output2 = relay.Tuple([call_8902,])
func_8903 = relay.Function([], output)
mod['func_8903'] = func_8903
mod = relay.transform.InferType()(mod)
output = func_8903()
func_8904 = relay.Function([], output)
mutated_mod['func_8904'] = func_8904
mutated_mod = relay.transform.InferType()(mutated_mod)
const_8916 = relay.const(5, dtype = "uint32")#candidate|8916|()|const|uint32
var_8917 = relay.var("var_8917", dtype = "uint32", shape = (9, 1, 1))#candidate|8917|(9, 1, 1)|var|uint32
bop_8918 = relay.add(const_8916.astype('uint32'), var_8917.astype('uint32')) # shape=(9, 1, 1)
output = bop_8918
output2 = bop_8918
func_8922 = relay.Function([var_8917,], output)
mod['func_8922'] = func_8922
mod = relay.transform.InferType()(mod)
mutated_mod['func_8922'] = func_8922
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8923 = relay.var("var_8923", dtype = "uint32", shape = (9, 1, 1))#candidate|8923|(9, 1, 1)|var|uint32
func_8922_call = mutated_mod.get_global_var('func_8922')
call_8924 = func_8922_call(var_8923)
output = call_8924
func_8925 = relay.Function([var_8923], output)
mutated_mod['func_8925'] = func_8925
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8946 = relay.var("var_8946", dtype = "uint8", shape = (3, 1, 11))#candidate|8946|(3, 1, 11)|var|uint8
var_8947 = relay.var("var_8947", dtype = "uint8", shape = (3, 1, 11))#candidate|8947|(3, 1, 11)|var|uint8
bop_8948 = relay.bitwise_or(var_8946.astype('uint8'), relay.reshape(var_8947.astype('uint8'), relay.shape_of(var_8946))) # shape=(3, 1, 11)
output = bop_8948
output2 = bop_8948
func_8957 = relay.Function([var_8946,var_8947,], output)
mod['func_8957'] = func_8957
mod = relay.transform.InferType()(mod)
var_8958 = relay.var("var_8958", dtype = "uint8", shape = (3, 1, 11))#candidate|8958|(3, 1, 11)|var|uint8
var_8959 = relay.var("var_8959", dtype = "uint8", shape = (3, 1, 11))#candidate|8959|(3, 1, 11)|var|uint8
output = func_8957(var_8958,var_8959,)
func_8960 = relay.Function([var_8958,var_8959,], output)
mutated_mod['func_8960'] = func_8960
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8903_call = mod.get_global_var('func_8903')
func_8904_call = mutated_mod.get_global_var('func_8904')
call_8971 = relay.TupleGetItem(func_8903_call(), 0)
call_8972 = relay.TupleGetItem(func_8904_call(), 0)
output = relay.Tuple([call_8971,])
output2 = relay.Tuple([call_8972,])
func_8995 = relay.Function([], output)
mod['func_8995'] = func_8995
mod = relay.transform.InferType()(mod)
mutated_mod['func_8995'] = func_8995
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8995_call = mutated_mod.get_global_var('func_8995')
call_8996 = func_8995_call()
output = call_8996
func_8997 = relay.Function([], output)
mutated_mod['func_8997'] = func_8997
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8397_call = mod.get_global_var('func_8397')
func_8398_call = mutated_mod.get_global_var('func_8398')
call_9052 = relay.TupleGetItem(func_8397_call(), 1)
call_9053 = relay.TupleGetItem(func_8398_call(), 1)
output = call_9052
output2 = call_9053
func_9070 = relay.Function([], output)
mod['func_9070'] = func_9070
mod = relay.transform.InferType()(mod)
mutated_mod['func_9070'] = func_9070
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9070_call = mutated_mod.get_global_var('func_9070')
call_9071 = func_9070_call()
output = call_9071
func_9072 = relay.Function([], output)
mutated_mod['func_9072'] = func_9072
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4736_call = mod.get_global_var('func_4736')
func_4737_call = mutated_mod.get_global_var('func_4737')
call_9162 = relay.TupleGetItem(func_4736_call(), 0)
call_9163 = relay.TupleGetItem(func_4737_call(), 0)
func_8661_call = mod.get_global_var('func_8661')
func_8664_call = mutated_mod.get_global_var('func_8664')
const_9172 = relay.const([-5.758052,-8.543929,-0.806095,7.980748,1.346274,-9.461769,-9.258056,2.959458,5.829598,-5.015347,-7.137837,0.228384,-7.487658,-3.402622,-4.399538,2.667475,0.178230,6.591139,5.427063,-8.084995,6.163922,-1.904676,-5.566067,-6.548963,-4.784416,7.069325,-9.375363,2.296447,-3.053989,-7.663839,4.942144,4.486334,-5.107024,-3.381989,-5.994739,-4.737766,6.409462,0.600310,-1.230590,3.172151,4.942683,9.449049,-5.656701,-1.785040,7.314477,0.297599,-9.456363,8.057237,9.098830,-9.516606,-9.788299,-5.624916,-9.089573,-7.055639,0.701478,4.775428,-0.418227,-9.332285,2.673142,6.992021,6.155063,1.589346,8.833849,-0.659020,-2.464318,-9.986745,9.225706,2.067315,5.981069,-1.819600,2.772772,2.211118,5.743985,-8.075411,-1.731432,9.954740,-8.290998,5.204412,1.121494,4.841913,8.955970,5.878503,-9.474150,-9.811108,-1.532797,-3.033507,-4.666649,4.138811,9.913047,-2.143965,8.853262,0.627557,5.666386,2.156526,4.461761,-9.552364,2.197131,3.196615,-4.897515,0.432039,6.319888,3.914260,1.159679,1.376222,-0.408488,-7.117189,7.193646,-6.415593,-0.746592,5.481682,-9.846071,-6.560330,4.230239,2.836010,2.546513,-9.474260,-4.754254,-6.972719,-3.596470,-4.409458,-8.271690,-9.412095,-0.527566,-9.121521,6.068431,-8.151310,9.798962,4.319610,9.539389,1.771043,9.936259,6.627493,4.623696,5.171792,2.339254,-5.692726,-8.834693,7.201335,4.562575,6.461874,8.323459,-2.628829,4.388990,-1.174706,-1.688324,4.010962,5.751866,3.584427,7.979883,4.909806,-3.777078,-7.325732,-5.411892,-3.392309,6.109199,-2.818893,9.605771,5.660405,-0.212827,5.377481,0.057125,-3.242436,3.004758,5.576099,-4.001883,4.746437,2.661531,1.918090,6.334168,8.985113,-9.305630,-3.313531,7.258413,-1.441403,9.659932,-7.152378,-9.111559,9.374968,0.401179,-9.990340,3.990992,-2.738548,3.627580,1.271651,6.759953,8.353492,-0.559755,-9.439196,-8.219076,-1.932451,-4.472342,-2.709894,3.970785,9.620322,4.386972,3.005897,3.257778,6.398671,3.111948,-7.929939,7.114670,-7.970722,7.805451,5.747077,3.247184,9.975014,0.772806,6.084199], dtype = "float64")#candidate|9172|(208,)|const|float64
const_9173 = relay.const([-3.746973,-5.706694,-2.018977,1.974808,-6.223538,8.434625,8.407200,1.112298,-8.753634,-8.102307,-6.820295,8.071699,-9.968655,5.076074,2.740655,-8.698414,7.363682,-1.861601,-3.211216,3.782134,0.396561,-2.120923,9.228008,1.638628,7.618930,5.032016,8.366652,7.217666,4.287119,8.670557,7.063698,1.162637,-6.267718,-6.683282,5.353426,2.709916,-4.015676,0.445380,-6.290104,0.753791,8.743536,6.334570,-9.485670,-6.933725,8.921949,-4.913716,5.048863,0.514189,0.064252,-8.061456,-8.429993,8.921893,7.053701,-7.846317,6.063205,0.368254,-3.646464,5.792770,3.331313,3.891017,-7.364726,2.097671,1.762989,0.612034,5.945465,5.758091,-0.943492,-1.069212,5.382164,1.000841,6.956772,7.488514,7.842026,-4.269095,-7.007536,-7.429583,8.347414,-3.156926,-3.961466,-6.711862,7.592050,8.579735,-2.987640,-4.126654,-6.764294,7.128043,-4.862872,-3.297123,1.528969,1.061873,-6.593361,-9.627493,3.974377,-6.206556,1.868976,1.378619,-7.057181,-0.681763,6.005378,-7.581600,-2.019289,9.560881,7.547745,-1.856869,-7.732886,-8.856152,7.195147,-5.468818,-5.830702,0.122522,9.210814,-5.477541,4.556642,5.916010,5.990977,3.575587,6.507083,4.275080,-9.129419,5.783419,4.548309,5.965796,0.469400,2.647092,-1.170260,6.748075,-1.011327,6.505445,-4.622098,-5.548080,-1.240991,1.125896,-4.142965,-2.546818,-9.822472,1.692639,-0.641751,9.444296,-6.601098,9.864022,9.108242,1.222767,-9.457450,4.169858,3.519548,3.703368,7.628472,4.616390,6.335355,-8.584926,3.710612,7.962347,-6.239190,2.778357,1.404682,5.144104,7.871749,-0.563934,9.212823,-3.765778,8.993112,8.869838,-6.434991,-9.030504,-0.928163,-0.873701,-6.158139,4.630417,-0.671850,-4.769519,7.701640,-6.526775,-9.858365,3.134044,-5.677185,-8.453203,1.155805,5.188277,-2.574427,7.813394,-8.600991,-3.877953,5.945905,-5.328437,1.942921,3.287381,-0.937779,1.782646,4.888777,3.187173,5.144532,0.664729], dtype = "float32")#candidate|9173|(192,)|const|float32
call_9171 = relay.TupleGetItem(func_8661_call(relay.reshape(const_9172.astype('float64'), [1, 16, 13]), relay.reshape(const_9173.astype('float32'), [4, 48]), ), 5)
call_9174 = relay.TupleGetItem(func_8664_call(relay.reshape(const_9172.astype('float64'), [1, 16, 13]), relay.reshape(const_9173.astype('float32'), [4, 48]), ), 5)
bop_9178 = relay.multiply(call_9171.astype('int64'), relay.reshape(const_9172.astype('int64'), relay.shape_of(call_9171))) # shape=(1, 16, 13)
bop_9181 = relay.multiply(call_9174.astype('int64'), relay.reshape(const_9172.astype('int64'), relay.shape_of(call_9174))) # shape=(1, 16, 13)
uop_9182 = relay.log(call_9171.astype('float32')) # shape=(1, 16, 13)
uop_9184 = relay.log(call_9174.astype('float32')) # shape=(1, 16, 13)
func_5215_call = mod.get_global_var('func_5215')
func_5216_call = mutated_mod.get_global_var('func_5216')
call_9185 = relay.TupleGetItem(func_5215_call(), 0)
call_9186 = relay.TupleGetItem(func_5216_call(), 0)
func_257_call = mod.get_global_var('func_257')
func_259_call = mutated_mod.get_global_var('func_259')
call_9192 = relay.TupleGetItem(func_257_call(), 1)
call_9193 = relay.TupleGetItem(func_259_call(), 1)
bop_9194 = relay.logical_xor(uop_9182.astype('uint8'), relay.reshape(bop_9178.astype('uint8'), relay.shape_of(uop_9182))) # shape=(1, 16, 13)
bop_9197 = relay.logical_xor(uop_9184.astype('uint8'), relay.reshape(bop_9181.astype('uint8'), relay.shape_of(uop_9184))) # shape=(1, 16, 13)
bop_9209 = relay.logical_or(uop_9182.astype('bool'), relay.reshape(call_9171.astype('bool'), relay.shape_of(uop_9182))) # shape=(1, 16, 13)
bop_9212 = relay.logical_or(uop_9184.astype('bool'), relay.reshape(call_9174.astype('bool'), relay.shape_of(uop_9184))) # shape=(1, 16, 13)
bop_9213 = relay.minimum(bop_9209.astype('float32'), relay.reshape(call_9171.astype('float32'), relay.shape_of(bop_9209))) # shape=(1, 16, 13)
bop_9216 = relay.minimum(bop_9212.astype('float32'), relay.reshape(call_9174.astype('float32'), relay.shape_of(bop_9212))) # shape=(1, 16, 13)
bop_9218 = relay.divide(bop_9209.astype('float64'), relay.reshape(bop_9194.astype('float64'), relay.shape_of(bop_9209))) # shape=(1, 16, 13)
bop_9221 = relay.divide(bop_9212.astype('float64'), relay.reshape(bop_9197.astype('float64'), relay.shape_of(bop_9212))) # shape=(1, 16, 13)
output = relay.Tuple([call_9162,const_9173,call_9185,call_9192,bop_9213,bop_9218,])
output2 = relay.Tuple([call_9163,const_9173,call_9186,call_9193,bop_9216,bop_9221,])
F = relay.Function([], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([], output2)
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
