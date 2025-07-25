import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_272 = relay.var("var_272", dtype = "float64", shape = (2, 7, 3))#candidate|272|(2, 7, 3)|var|float64
uop_273 = relay.cosh(var_272.astype('float64')) # shape=(2, 7, 3)
output = relay.Tuple([uop_273,])
output2 = relay.Tuple([uop_273,])
func_292 = relay.Function([var_272,], output)
mod['func_292'] = func_292
mod = relay.transform.InferType()(mod)
var_293 = relay.var("var_293", dtype = "float64", shape = (2, 7, 3))#candidate|293|(2, 7, 3)|var|float64
output = func_292(var_293)
func_294 = relay.Function([var_293], output)
mutated_mod['func_294'] = func_294
mutated_mod = relay.transform.InferType()(mutated_mod)
var_361 = relay.var("var_361", dtype = "int16", shape = ())#candidate|361|()|var|int16
var_362 = relay.var("var_362", dtype = "int16", shape = (12, 3, 1))#candidate|362|(12, 3, 1)|var|int16
bop_363 = relay.bitwise_or(var_361.astype('int16'), var_362.astype('int16')) # shape=(12, 3, 1)
output = relay.Tuple([bop_363,])
output2 = relay.Tuple([bop_363,])
func_377 = relay.Function([var_361,var_362,], output)
mod['func_377'] = func_377
mod = relay.transform.InferType()(mod)
mutated_mod['func_377'] = func_377
mutated_mod = relay.transform.InferType()(mutated_mod)
func_377_call = mutated_mod.get_global_var('func_377')
var_379 = relay.var("var_379", dtype = "int16", shape = ())#candidate|379|()|var|int16
var_380 = relay.var("var_380", dtype = "int16", shape = (12, 3, 1))#candidate|380|(12, 3, 1)|var|int16
call_378 = func_377_call(var_379,var_380,)
output = call_378
func_381 = relay.Function([var_379,var_380,], output)
mutated_mod['func_381'] = func_381
mutated_mod = relay.transform.InferType()(mutated_mod)
const_434 = relay.const([[[2,1,9,9,10,10,6],[5,-9,-1,-4,-4,9,9],[5,-3,1,-4,-7,8,-6],[-1,2,-8,10,-3,-8,-1],[10,-8,-7,-3,-4,9,-1],[9,5,8,7,8,7,-4],[-8,-3,-8,-3,-3,5,5],[-1,1,4,9,5,9,-5],[-5,-3,-5,-3,-1,-10,-5],[2,-9,8,2,-7,-3,-8],[8,-1,2,7,-2,4,9],[8,9,5,4,7,7,-8],[8,3,9,8,7,3,-8]],[[-3,-9,2,-2,5,2,9],[-7,10,-4,1,8,-7,9],[-8,-4,-5,-1,-2,-5,8],[-10,9,-5,3,3,-3,5],[9,9,-10,-8,10,1,-4],[-1,-6,-1,-8,-3,6,-5],[8,-8,-4,6,-1,-9,6],[3,8,2,4,-8,-10,1],[6,4,6,5,-10,-3,5],[-2,-6,1,-8,10,6,4],[9,-1,-3,-3,8,10,6],[9,-7,-2,-5,-9,-8,6],[-8,-2,-8,-4,-10,2,4]],[[4,-5,-3,3,7,8,2],[6,-10,10,3,-6,9,-7],[-2,2,1,2,-2,-9,4],[9,-5,-5,1,-6,-5,5],[-8,6,-3,9,-8,10,-5],[-10,-8,6,4,-8,-7,3],[-9,-6,1,9,2,8,7],[9,6,-3,-10,10,10,-1],[4,-9,-2,-10,-10,-5,-4],[-10,10,5,1,-2,4,-5],[10,3,9,7,-10,-4,-5],[-1,-1,-2,-10,-9,-4,2],[-3,-4,2,-8,-9,4,-1]],[[8,-9,-7,-9,3,5,-2],[3,10,-2,10,2,-7,-3],[10,3,-2,-8,5,9,9],[-10,-4,7,-10,8,5,5],[9,-6,2,9,-2,-4,-4],[-4,6,6,-8,3,3,5],[-9,9,8,9,3,-5,-4],[-1,-9,-1,-9,-4,9,-5],[9,8,2,-8,-5,2,6],[4,-4,10,9,8,-6,7],[2,-8,3,8,7,8,6],[1,-7,4,9,-7,-5,8],[-9,-9,-8,1,6,9,-7]],[[5,-8,7,-1,-9,5,9],[-2,1,4,4,8,-3,7],[8,-10,-7,-9,-4,-5,1],[10,10,-8,5,3,-4,-5],[7,-1,-5,-8,-9,-7,9],[7,-2,3,9,4,-5,-3],[10,-6,-1,-2,7,-9,8],[3,-7,-1,-9,10,-6,-4],[-1,-10,7,8,2,-2,-9],[-7,-8,8,3,4,-2,10],[9,10,10,-1,-5,-5,-8],[-10,-2,5,9,5,3,-2],[6,-4,7,-6,-4,-6,-7]],[[-10,1,-3,-6,3,4,-7],[-7,-1,-2,-7,10,6,2],[5,-6,-4,4,10,-8,7],[-10,8,-3,2,5,-4,3],[-7,5,-4,-8,6,8,5],[-10,7,-7,9,5,7,1],[2,-3,-10,-2,9,-3,-5],[-2,6,-1,2,-9,9,-2],[-1,-10,-8,-4,3,-3,8],[-9,6,3,3,-4,-3,-10],[6,-9,-7,-9,-3,-3,1],[-9,1,-3,-9,-8,10,1],[-4,6,-3,6,5,4,10]],[[-2,-3,-9,-1,1,9,-4],[3,4,6,-9,4,-10,-3],[-7,-2,-4,-2,-1,-9,2],[-2,-9,-2,4,3,-9,-9],[8,-3,-6,3,-2,-5,9],[5,-2,-10,4,3,1,1],[3,-9,5,5,7,-1,7],[1,-2,7,-5,-4,-10,9],[5,1,4,-10,-4,-8,4],[-9,7,-9,8,2,5,-4],[-5,6,7,-7,-9,-7,3],[-3,7,10,-4,3,-4,-7],[3,4,6,-7,7,-1,-10]],[[-9,-6,-9,-4,4,-9,10],[-2,-2,8,-2,-8,-7,-2],[1,-9,-6,-3,-7,-6,-3],[-10,8,-9,6,8,4,-6],[1,1,1,-4,-8,-3,-4],[-6,4,1,7,-4,-9,-2],[10,-4,-7,5,-9,-6,-10],[10,8,2,-3,5,2,4],[2,4,3,3,5,9,-10],[10,5,-3,-7,6,7,9],[-1,-3,-8,-4,-5,2,-8],[-5,-9,-8,5,9,8,4],[-9,7,8,2,8,-9,-7]],[[-6,-4,-5,4,-9,-7,-10],[4,-2,-7,-2,2,-10,-3],[7,10,7,2,8,7,4],[-6,1,-10,-2,4,3,1],[8,4,6,-7,-9,6,5],[-7,-9,7,2,3,-6,1],[4,-5,-7,-6,-5,7,1],[3,5,9,4,4,-5,1],[5,-3,5,-1,-8,-7,-1],[-7,6,-2,-2,6,9,2],[-8,-7,9,4,-9,8,4],[-10,-10,9,9,-8,2,-6],[4,5,5,7,-2,-9,7]],[[-8,-3,-8,-3,10,8,-4],[-3,-3,2,-1,2,10,8],[-4,-7,8,9,4,4,-6],[1,7,2,-1,10,9,9],[-5,-1,3,-1,1,-8,-6],[8,-7,3,2,-3,-8,-6],[-6,-8,-3,-2,-10,-9,5],[-3,-4,-4,-9,6,-10,6],[-4,5,-9,-1,-4,1,5],[5,1,-10,9,5,-1,-1],[10,7,2,-3,6,5,4],[6,-8,-9,8,-4,-5,9],[2,5,9,-7,5,-4,-2]],[[3,-7,-5,-9,-3,-6,-6],[-6,7,4,1,7,6,5],[-4,-1,5,7,2,-6,3],[-2,5,3,-7,7,2,-3],[7,-10,-5,10,-10,9,3],[7,-9,6,-6,-7,7,8],[-9,8,8,-1,-3,-2,9],[5,7,7,-10,2,-1,-6],[5,8,4,4,-5,5,-5],[1,10,-8,-9,-3,-8,-6],[3,7,-7,-4,10,4,-2],[-5,8,2,3,5,5,-4],[4,-1,-1,7,-3,10,-8]]], dtype = "uint16")#candidate|434|(11, 13, 7)|const|uint16
const_435 = relay.const([[[9,-3,-4,9,-4,9,2],[2,2,5,-3,-5,-9,3],[-3,1,5,-8,6,-4,-6],[2,10,1,7,-10,-1,5],[10,-3,7,5,-9,10,-2],[10,7,3,7,-1,-2,-7],[8,4,-9,2,-10,-5,2],[6,2,-10,-7,-8,9,-9],[10,7,-7,7,9,-10,-6],[9,2,2,3,-5,-6,-5],[2,-9,9,10,8,-9,-7],[-5,-4,1,-2,-2,-6,7],[7,1,5,2,8,9,-1]],[[3,9,-3,4,1,-8,3],[9,9,2,-5,-2,3,3],[3,2,4,-6,6,-2,10],[-9,5,2,4,-6,3,8],[-7,7,4,8,1,-6,5],[-2,-7,7,9,-8,5,1],[-3,1,-9,9,-8,-3,2],[5,-5,-2,10,-6,1,1],[1,4,-3,3,-5,-5,-1],[1,-8,-1,-5,-5,4,-3],[7,-3,-8,-2,5,-10,10],[-3,-4,6,-3,4,4,1],[3,5,8,6,-8,-6,4]],[[3,-1,-8,-3,8,-3,-3],[4,-5,8,6,-1,-3,-3],[-1,-4,4,1,4,-4,9],[7,-6,-6,9,-4,-1,9],[3,-2,10,9,3,4,3],[10,-9,3,-9,6,-2,-10],[5,-8,3,1,10,-7,-9],[10,1,5,8,-5,9,-2],[-2,-6,6,-5,6,10,7],[8,-8,-9,2,-1,2,-7],[7,-1,-6,8,-3,-8,-1],[4,8,4,-2,-7,5,-5],[3,-7,5,-9,-7,2,-10]],[[-8,1,-8,3,6,-3,2],[-2,6,-2,6,-2,-8,-4],[8,3,4,7,-4,2,-8],[5,-6,10,4,6,9,5],[-9,-8,-2,3,6,7,-2],[1,5,-1,-5,-2,3,9],[8,-9,-2,5,9,-9,10],[4,7,2,-1,5,-4,-5],[7,-8,7,-3,4,2,-6],[6,-8,-7,-4,-9,2,3],[10,-2,3,9,5,10,10],[3,-4,3,7,-9,7,-10],[-1,-6,4,-6,-9,-8,9]],[[-6,-3,-6,-5,-10,-6,-7],[-6,-3,-1,-8,8,1,-10],[-2,10,-9,-6,-1,3,3],[-2,-4,9,-7,-8,-5,-10],[-6,9,1,-7,-4,7,-1],[-7,-10,7,7,-3,8,9],[10,2,-10,-3,2,-3,-10],[-10,-9,-7,5,-2,4,7],[7,-7,-5,-2,-2,8,-4],[10,1,8,8,8,-3,-8],[-6,-9,2,9,-5,-6,5],[-2,-5,6,4,-6,9,-6],[6,9,10,2,-4,-1,1]],[[5,-1,8,9,4,8,-6],[5,1,-7,-1,8,8,6],[8,-7,5,2,-6,7,-6],[9,4,-5,3,-5,8,-10],[3,8,-5,-8,4,6,-3],[-9,10,1,2,-10,8,9],[-9,4,7,5,8,-2,5],[6,3,-7,3,-10,1,-2],[-5,5,-2,-8,-1,-8,-6],[5,10,-9,7,7,-3,-7],[-7,3,9,-8,9,7,8],[-2,8,6,-9,3,1,7],[7,8,10,7,-3,10,10]],[[-3,5,-3,-3,2,-5,7],[5,10,8,7,3,-9,9],[-8,9,7,7,6,10,1],[5,3,-3,-3,3,9,5],[2,-9,5,4,-1,-4,10],[-7,1,-10,-1,7,4,-7],[6,2,8,-2,9,-6,8],[7,6,-10,5,1,-5,-3],[10,3,-2,8,8,2,6],[8,-8,4,1,2,6,-4],[-4,1,7,-10,8,-6,7],[-6,5,-9,-10,-8,-8,7],[-2,6,-7,9,-10,-2,6]],[[7,-7,-8,-8,7,9,9],[4,3,8,-3,6,-1,-1],[-7,1,10,-6,2,5,-1],[3,-2,-7,-2,-2,-2,-6],[-5,5,4,5,-6,2,6],[-5,10,9,4,6,-3,-2],[-1,5,5,-7,6,1,-4],[9,-10,10,-4,-3,7,8],[-2,-2,-9,8,-6,3,10],[5,-8,-5,-1,-10,4,-5],[7,-10,6,-3,-10,10,-7],[-10,-8,-10,-9,5,-9,-5],[10,-5,-5,-5,8,7,8]],[[-4,2,-3,-8,7,7,-5],[8,-3,-2,-5,-5,10,-8],[-1,-6,-3,-8,-9,9,-4],[-9,-5,1,-5,-8,9,-3],[-7,8,7,-3,-4,-7,9],[-10,-4,-4,-8,-9,-5,5],[10,-7,-9,7,10,-8,-2],[9,3,-6,2,6,-4,-3],[1,5,6,-2,-8,2,-8],[-4,7,6,5,-7,-2,7],[9,5,7,-3,3,-9,4],[-6,-2,-5,-6,-1,10,9],[2,-8,-5,-10,2,-7,-9]],[[-5,-8,5,3,-2,-10,-9],[-10,4,2,2,-4,2,-8],[-2,-7,-9,-10,-8,-6,-10],[-1,9,-7,7,5,-1,-4],[9,-5,-8,-10,9,5,2],[8,-8,-3,2,9,1,1],[-5,6,6,6,2,-2,5],[10,9,-9,7,-5,2,-10],[-10,-5,-7,-10,10,8,-10],[-7,-10,-2,5,7,1,-2],[-5,-6,-5,-9,-3,3,5],[-7,4,9,3,2,-3,9],[-10,-7,-3,-10,-3,9,10]],[[-9,-7,-9,4,-4,9,2],[-6,6,-4,-3,-3,5,3],[-3,-10,-5,3,-8,2,-2],[8,5,-7,-10,-3,7,-7],[3,8,3,2,-5,-2,10],[4,6,-9,6,1,6,10],[-9,8,6,-2,6,-7,-7],[-5,-4,2,-3,-1,7,-6],[8,-6,4,3,-10,7,8],[-6,-4,3,-9,7,6,-10],[2,5,3,-10,-5,-7,7],[2,9,-10,8,10,-10,1],[5,-10,9,-10,9,1,3]]], dtype = "uint16")#candidate|435|(11, 13, 7)|const|uint16
bop_436 = relay.greater_equal(const_434.astype('bool'), relay.reshape(const_435.astype('bool'), relay.shape_of(const_434))) # shape=(11, 13, 7)
output = relay.Tuple([bop_436,])
output2 = relay.Tuple([bop_436,])
func_442 = relay.Function([], output)
mod['func_442'] = func_442
mod = relay.transform.InferType()(mod)
output = func_442()
func_443 = relay.Function([], output)
mutated_mod['func_443'] = func_443
mutated_mod = relay.transform.InferType()(mutated_mod)
func_442_call = mod.get_global_var('func_442')
func_443_call = mutated_mod.get_global_var('func_443')
call_446 = relay.TupleGetItem(func_442_call(), 0)
call_447 = relay.TupleGetItem(func_443_call(), 0)
uop_468 = relay.acosh(call_446.astype('float64')) # shape=(11, 13, 7)
uop_470 = relay.acosh(call_447.astype('float64')) # shape=(11, 13, 7)
func_377_call = mod.get_global_var('func_377')
func_381_call = mutated_mod.get_global_var('func_381')
const_480 = relay.const(4, dtype = "int16")#candidate|480|()|const|int16
const_481 = relay.const([6,-5,-1,4,-5,3,1,5,-1,9,8,8,6,7,7,-8,-6,-4,9,-10,-10,-2,-10,-6,-6,4,6,7,10,-2,4,2,4,-8,3,-1], dtype = "int16")#candidate|481|(36,)|const|int16
call_479 = relay.TupleGetItem(func_377_call(relay.reshape(const_480.astype('int16'), []), relay.reshape(const_481.astype('int16'), [12, 3, 1]), ), 0)
call_482 = relay.TupleGetItem(func_381_call(relay.reshape(const_480.astype('int16'), []), relay.reshape(const_481.astype('int16'), [12, 3, 1]), ), 0)
func_442_call = mod.get_global_var('func_442')
func_443_call = mutated_mod.get_global_var('func_443')
call_491 = relay.TupleGetItem(func_442_call(), 0)
call_492 = relay.TupleGetItem(func_443_call(), 0)
var_509 = relay.var("var_509", dtype = "float64", shape = (11, 13, 7))#candidate|509|(11, 13, 7)|var|float64
bop_510 = relay.minimum(uop_468.astype('int16'), relay.reshape(var_509.astype('int16'), relay.shape_of(uop_468))) # shape=(11, 13, 7)
bop_513 = relay.minimum(uop_470.astype('int16'), relay.reshape(var_509.astype('int16'), relay.shape_of(uop_470))) # shape=(11, 13, 7)
func_377_call = mod.get_global_var('func_377')
func_381_call = mutated_mod.get_global_var('func_381')
call_551 = relay.TupleGetItem(func_377_call(relay.reshape(const_480.astype('int16'), []), relay.reshape(call_479.astype('int16'), [12, 3, 1]), ), 0)
call_552 = relay.TupleGetItem(func_381_call(relay.reshape(const_480.astype('int16'), []), relay.reshape(call_479.astype('int16'), [12, 3, 1]), ), 0)
func_292_call = mod.get_global_var('func_292')
func_294_call = mutated_mod.get_global_var('func_294')
var_554 = relay.var("var_554", dtype = "float64", shape = (42,))#candidate|554|(42,)|var|float64
call_553 = relay.TupleGetItem(func_292_call(relay.reshape(var_554.astype('float64'), [2, 7, 3])), 0)
call_555 = relay.TupleGetItem(func_294_call(relay.reshape(var_554.astype('float64'), [2, 7, 3])), 0)
uop_560 = relay.log10(call_551.astype('float32')) # shape=(12, 3, 1)
uop_562 = relay.log10(call_552.astype('float32')) # shape=(12, 3, 1)
output = relay.Tuple([call_479,const_480,const_481,call_491,bop_510,call_553,var_554,uop_560,])
output2 = relay.Tuple([call_482,const_480,const_481,call_492,bop_513,call_555,var_554,uop_562,])
func_564 = relay.Function([var_509,var_554,], output)
mod['func_564'] = func_564
mod = relay.transform.InferType()(mod)
var_565 = relay.var("var_565", dtype = "float64", shape = (11, 13, 7))#candidate|565|(11, 13, 7)|var|float64
var_566 = relay.var("var_566", dtype = "float64", shape = (42,))#candidate|566|(42,)|var|float64
output = func_564(var_565,var_566,)
func_567 = relay.Function([var_565,var_566,], output)
mutated_mod['func_567'] = func_567
mutated_mod = relay.transform.InferType()(mutated_mod)
const_582 = relay.const([[[5,-1,-8,-4,-6,2,7,-3,7,-5,-10],[-8,3,-5,10,3,5,-10,2,6,8,-1]],[[9,10,-4,9,-7,4,2,-4,-1,-10,10],[-1,-6,2,4,9,-9,-1,3,9,-6,-1]],[[-4,5,-4,2,-6,6,-2,6,-4,-9,-3],[8,-10,-5,1,7,2,9,-6,10,5,-6]],[[6,3,6,-5,-10,-2,-1,7,4,7,3],[-2,8,2,7,10,-7,-3,5,-1,-2,-5]],[[9,-7,3,1,-10,6,-4,-5,6,4,8],[-8,7,8,-10,4,-5,6,-3,-6,9,-4]],[[2,-6,5,-2,7,-8,9,6,8,-1,-1],[1,-4,-8,10,-8,3,1,-3,-3,-4,7]],[[-6,5,4,-7,4,10,6,3,-2,-10,-2],[-3,7,5,6,7,8,-5,7,-9,9,-9]],[[7,-5,-10,6,-8,-8,6,6,-9,3,4],[-10,-10,-2,-8,6,-10,8,5,-3,-4,8]],[[6,3,9,-1,-4,4,1,2,4,5,-8],[5,7,-6,10,-3,10,-2,-2,1,-5,7]],[[-10,3,7,-1,3,10,-5,10,-10,2,1],[-8,8,-8,-6,-6,3,2,9,9,-9,-1]],[[3,10,6,-5,7,-9,-5,-7,-1,-7,4],[8,-3,5,-4,-6,10,2,1,5,3,2]],[[-1,8,2,6,-5,9,-1,-9,3,-4,3],[-8,-5,4,-7,7,7,-9,9,7,2,-3]]], dtype = "uint16")#candidate|582|(12, 2, 11)|const|uint16
var_583 = relay.var("var_583", dtype = "uint16", shape = (12, 2, 11))#candidate|583|(12, 2, 11)|var|uint16
bop_584 = relay.maximum(const_582.astype('uint16'), relay.reshape(var_583.astype('uint16'), relay.shape_of(const_582))) # shape=(12, 2, 11)
uop_588 = relay.acos(var_583.astype('float64')) # shape=(12, 2, 11)
output = relay.Tuple([bop_584,uop_588,])
output2 = relay.Tuple([bop_584,uop_588,])
func_594 = relay.Function([var_583,], output)
mod['func_594'] = func_594
mod = relay.transform.InferType()(mod)
mutated_mod['func_594'] = func_594
mutated_mod = relay.transform.InferType()(mutated_mod)
var_595 = relay.var("var_595", dtype = "uint16", shape = (12, 2, 11))#candidate|595|(12, 2, 11)|var|uint16
func_594_call = mutated_mod.get_global_var('func_594')
call_596 = func_594_call(var_595)
output = call_596
func_597 = relay.Function([var_595], output)
mutated_mod['func_597'] = func_597
mutated_mod = relay.transform.InferType()(mutated_mod)
func_442_call = mod.get_global_var('func_442')
func_443_call = mutated_mod.get_global_var('func_443')
call_625 = relay.TupleGetItem(func_442_call(), 0)
call_626 = relay.TupleGetItem(func_443_call(), 0)
func_594_call = mod.get_global_var('func_594')
func_597_call = mutated_mod.get_global_var('func_597')
var_633 = relay.var("var_633", dtype = "uint16", shape = (264,))#candidate|633|(264,)|var|uint16
call_632 = relay.TupleGetItem(func_594_call(relay.reshape(var_633.astype('uint16'), [12, 2, 11])), 1)
call_634 = relay.TupleGetItem(func_597_call(relay.reshape(var_633.astype('uint16'), [12, 2, 11])), 1)
func_377_call = mod.get_global_var('func_377')
func_381_call = mutated_mod.get_global_var('func_381')
var_637 = relay.var("var_637", dtype = "int16", shape = ())#candidate|637|()|var|int16
const_638 = relay.const([[-7,1],[-4,-8],[1,7],[-4,10],[10,3],[3,-3],[10,6],[2,-3],[-3,-9],[-7,6],[-5,-6],[5,-8],[-3,-1],[10,-5],[-3,-2],[7,2],[-10,-8],[9,4]], dtype = "int16")#candidate|638|(18, 2)|const|int16
call_636 = relay.TupleGetItem(func_377_call(relay.reshape(var_637.astype('int16'), []), relay.reshape(const_638.astype('int16'), [12, 3, 1]), ), 0)
call_639 = relay.TupleGetItem(func_381_call(relay.reshape(var_637.astype('int16'), []), relay.reshape(const_638.astype('int16'), [12, 3, 1]), ), 0)
bop_641 = relay.minimum(call_632.astype('uint16'), relay.reshape(var_633.astype('uint16'), relay.shape_of(call_632))) # shape=(12, 2, 11)
bop_644 = relay.minimum(call_634.astype('uint16'), relay.reshape(var_633.astype('uint16'), relay.shape_of(call_634))) # shape=(12, 2, 11)
uop_655 = relay.log10(call_625.astype('float64')) # shape=(11, 13, 7)
uop_657 = relay.log10(call_626.astype('float64')) # shape=(11, 13, 7)
func_292_call = mod.get_global_var('func_292')
func_294_call = mutated_mod.get_global_var('func_294')
const_662 = relay.const([-1.618780,-7.501186,-2.894971,4.798634,2.673554,9.179575,-5.968605,9.424491,-5.539776,-9.334462,8.641018,-5.166008,5.217295,-0.958989,0.320354,8.511933,5.485398,-7.976550,-8.965745,-8.366496,5.522233,5.679014,7.970788,2.948672,2.293754,9.977901,-4.892800,-2.716137,7.351898,9.497260,-3.358645,2.210408,-7.684616,-2.923200,0.236277,3.386316,-6.885214,-7.509808,4.327017,5.603808,9.248009,0.348469], dtype = "float64")#candidate|662|(42,)|const|float64
call_661 = relay.TupleGetItem(func_292_call(relay.reshape(const_662.astype('float64'), [2, 7, 3])), 0)
call_663 = relay.TupleGetItem(func_294_call(relay.reshape(const_662.astype('float64'), [2, 7, 3])), 0)
output = relay.Tuple([call_636,var_637,const_638,bop_641,uop_655,call_661,const_662,])
output2 = relay.Tuple([call_639,var_637,const_638,bop_644,uop_657,call_663,const_662,])
func_671 = relay.Function([var_633,var_637,], output)
mod['func_671'] = func_671
mod = relay.transform.InferType()(mod)
mutated_mod['func_671'] = func_671
mutated_mod = relay.transform.InferType()(mutated_mod)
func_671_call = mutated_mod.get_global_var('func_671')
var_673 = relay.var("var_673", dtype = "uint16", shape = (264,))#candidate|673|(264,)|var|uint16
var_674 = relay.var("var_674", dtype = "int16", shape = ())#candidate|674|()|var|int16
call_672 = func_671_call(var_673,var_674,)
output = call_672
func_675 = relay.Function([var_673,var_674,], output)
mutated_mod['func_675'] = func_675
mutated_mod = relay.transform.InferType()(mutated_mod)
func_442_call = mod.get_global_var('func_442')
func_443_call = mutated_mod.get_global_var('func_443')
call_677 = relay.TupleGetItem(func_442_call(), 0)
call_678 = relay.TupleGetItem(func_443_call(), 0)
var_692 = relay.var("var_692", dtype = "bool", shape = (11, 13, 7))#candidate|692|(11, 13, 7)|var|bool
bop_693 = relay.floor_divide(call_677.astype('float32'), relay.reshape(var_692.astype('float32'), relay.shape_of(call_677))) # shape=(11, 13, 7)
bop_696 = relay.floor_divide(call_678.astype('float32'), relay.reshape(var_692.astype('float32'), relay.shape_of(call_678))) # shape=(11, 13, 7)
output = relay.Tuple([bop_693,])
output2 = relay.Tuple([bop_696,])
func_708 = relay.Function([var_692,], output)
mod['func_708'] = func_708
mod = relay.transform.InferType()(mod)
mutated_mod['func_708'] = func_708
mutated_mod = relay.transform.InferType()(mutated_mod)
var_709 = relay.var("var_709", dtype = "bool", shape = (11, 13, 7))#candidate|709|(11, 13, 7)|var|bool
func_708_call = mutated_mod.get_global_var('func_708')
call_710 = func_708_call(var_709)
output = call_710
func_711 = relay.Function([var_709], output)
mutated_mod['func_711'] = func_711
mutated_mod = relay.transform.InferType()(mutated_mod)
var_756 = relay.var("var_756", dtype = "float32", shape = (7, 9, 7))#candidate|756|(7, 9, 7)|var|float32
var_757 = relay.var("var_757", dtype = "float32", shape = (7, 9, 7))#candidate|757|(7, 9, 7)|var|float32
bop_758 = relay.greater(var_756.astype('bool'), relay.reshape(var_757.astype('bool'), relay.shape_of(var_756))) # shape=(7, 9, 7)
uop_771 = relay.tan(var_756.astype('float64')) # shape=(7, 9, 7)
output = relay.Tuple([bop_758,uop_771,])
output2 = relay.Tuple([bop_758,uop_771,])
func_777 = relay.Function([var_756,var_757,], output)
mod['func_777'] = func_777
mod = relay.transform.InferType()(mod)
var_778 = relay.var("var_778", dtype = "float32", shape = (7, 9, 7))#candidate|778|(7, 9, 7)|var|float32
var_779 = relay.var("var_779", dtype = "float32", shape = (7, 9, 7))#candidate|779|(7, 9, 7)|var|float32
output = func_777(var_778,var_779,)
func_780 = relay.Function([var_778,var_779,], output)
mutated_mod['func_780'] = func_780
mutated_mod = relay.transform.InferType()(mutated_mod)
var_879 = relay.var("var_879", dtype = "bool", shape = (2, 15))#candidate|879|(2, 15)|var|bool
var_880 = relay.var("var_880", dtype = "bool", shape = (2, 15))#candidate|880|(2, 15)|var|bool
bop_881 = relay.logical_and(var_879.astype('bool'), relay.reshape(var_880.astype('bool'), relay.shape_of(var_879))) # shape=(2, 15)
func_442_call = mod.get_global_var('func_442')
func_443_call = mutated_mod.get_global_var('func_443')
call_907 = relay.TupleGetItem(func_442_call(), 0)
call_908 = relay.TupleGetItem(func_443_call(), 0)
uop_909 = relay.atan(call_907.astype('float64')) # shape=(11, 13, 7)
uop_911 = relay.atan(call_908.astype('float64')) # shape=(11, 13, 7)
output = relay.Tuple([bop_881,uop_909,])
output2 = relay.Tuple([bop_881,uop_911,])
func_918 = relay.Function([var_879,var_880,], output)
mod['func_918'] = func_918
mod = relay.transform.InferType()(mod)
mutated_mod['func_918'] = func_918
mutated_mod = relay.transform.InferType()(mutated_mod)
func_918_call = mutated_mod.get_global_var('func_918')
var_920 = relay.var("var_920", dtype = "bool", shape = (2, 15))#candidate|920|(2, 15)|var|bool
var_921 = relay.var("var_921", dtype = "bool", shape = (2, 15))#candidate|921|(2, 15)|var|bool
call_919 = func_918_call(var_920,var_921,)
output = call_919
func_922 = relay.Function([var_920,var_921,], output)
mutated_mod['func_922'] = func_922
mutated_mod = relay.transform.InferType()(mutated_mod)
var_926 = relay.var("var_926", dtype = "float64", shape = (15, 2, 11))#candidate|926|(15, 2, 11)|var|float64
uop_927 = relay.atan(var_926.astype('float64')) # shape=(15, 2, 11)
func_777_call = mod.get_global_var('func_777')
func_780_call = mutated_mod.get_global_var('func_780')
var_939 = relay.var("var_939", dtype = "float32", shape = (441,))#candidate|939|(441,)|var|float32
call_938 = relay.TupleGetItem(func_777_call(relay.reshape(var_939.astype('float32'), [7, 9, 7]), relay.reshape(var_939.astype('float32'), [7, 9, 7]), ), 1)
call_940 = relay.TupleGetItem(func_780_call(relay.reshape(var_939.astype('float32'), [7, 9, 7]), relay.reshape(var_939.astype('float32'), [7, 9, 7]), ), 1)
func_777_call = mod.get_global_var('func_777')
func_780_call = mutated_mod.get_global_var('func_780')
call_942 = relay.TupleGetItem(func_777_call(relay.reshape(var_939.astype('float32'), [7, 9, 7]), relay.reshape(call_938.astype('float32'), [7, 9, 7]), ), 0)
call_943 = relay.TupleGetItem(func_780_call(relay.reshape(var_939.astype('float32'), [7, 9, 7]), relay.reshape(call_938.astype('float32'), [7, 9, 7]), ), 0)
func_918_call = mod.get_global_var('func_918')
func_922_call = mutated_mod.get_global_var('func_922')
const_945 = relay.const([False,True,True,True,True,False,True,True,True,True,True,False,True,True,False,True,True,False,False,True,True,False,False,True,False,True,True,True,True,True], dtype = "bool")#candidate|945|(30,)|const|bool
call_944 = relay.TupleGetItem(func_918_call(relay.reshape(const_945.astype('bool'), [2, 15]), relay.reshape(const_945.astype('bool'), [2, 15]), ), 0)
call_946 = relay.TupleGetItem(func_922_call(relay.reshape(const_945.astype('bool'), [2, 15]), relay.reshape(const_945.astype('bool'), [2, 15]), ), 0)
output = relay.Tuple([uop_927,call_938,var_939,call_942,call_944,const_945,])
output2 = relay.Tuple([uop_927,call_940,var_939,call_943,call_946,const_945,])
func_961 = relay.Function([var_926,var_939,], output)
mod['func_961'] = func_961
mod = relay.transform.InferType()(mod)
var_962 = relay.var("var_962", dtype = "float64", shape = (15, 2, 11))#candidate|962|(15, 2, 11)|var|float64
var_963 = relay.var("var_963", dtype = "float32", shape = (441,))#candidate|963|(441,)|var|float32
output = func_961(var_962,var_963,)
func_964 = relay.Function([var_962,var_963,], output)
mutated_mod['func_964'] = func_964
mutated_mod = relay.transform.InferType()(mutated_mod)
func_442_call = mod.get_global_var('func_442')
func_443_call = mutated_mod.get_global_var('func_443')
call_1002 = relay.TupleGetItem(func_442_call(), 0)
call_1003 = relay.TupleGetItem(func_443_call(), 0)
uop_1019 = relay.sqrt(call_1002.astype('float64')) # shape=(11, 13, 7)
uop_1021 = relay.sqrt(call_1003.astype('float64')) # shape=(11, 13, 7)
output = relay.Tuple([uop_1019,])
output2 = relay.Tuple([uop_1021,])
func_1034 = relay.Function([], output)
mod['func_1034'] = func_1034
mod = relay.transform.InferType()(mod)
output = func_1034()
func_1035 = relay.Function([], output)
mutated_mod['func_1035'] = func_1035
mutated_mod = relay.transform.InferType()(mutated_mod)
func_442_call = mod.get_global_var('func_442')
func_443_call = mutated_mod.get_global_var('func_443')
call_1061 = relay.TupleGetItem(func_442_call(), 0)
call_1062 = relay.TupleGetItem(func_443_call(), 0)
func_594_call = mod.get_global_var('func_594')
func_597_call = mutated_mod.get_global_var('func_597')
var_1075 = relay.var("var_1075", dtype = "uint16", shape = (264,))#candidate|1075|(264,)|var|uint16
call_1074 = relay.TupleGetItem(func_594_call(relay.reshape(var_1075.astype('uint16'), [12, 2, 11])), 1)
call_1076 = relay.TupleGetItem(func_597_call(relay.reshape(var_1075.astype('uint16'), [12, 2, 11])), 1)
func_1034_call = mod.get_global_var('func_1034')
func_1035_call = mutated_mod.get_global_var('func_1035')
call_1100 = relay.TupleGetItem(func_1034_call(), 0)
call_1101 = relay.TupleGetItem(func_1035_call(), 0)
output = relay.Tuple([call_1061,call_1074,var_1075,call_1100,])
output2 = relay.Tuple([call_1062,call_1076,var_1075,call_1101,])
func_1112 = relay.Function([var_1075,], output)
mod['func_1112'] = func_1112
mod = relay.transform.InferType()(mod)
var_1113 = relay.var("var_1113", dtype = "uint16", shape = (264,))#candidate|1113|(264,)|var|uint16
output = func_1112(var_1113)
func_1114 = relay.Function([var_1113], output)
mutated_mod['func_1114'] = func_1114
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1121 = relay.const([[[10,-1,8,7,4,5,-3,-2,-1,-7,-1,10,8,8],[2,2,-5,4,-10,3,-8,7,7,4,-10,6,-3,-9]],[[-2,-5,-5,8,-3,-3,-5,8,5,5,-5,-9,10,-10],[-4,6,-6,-2,-9,10,5,4,10,-3,9,10,-7,-3]],[[-6,1,-10,8,9,6,2,-1,-9,-7,9,7,-10,-4],[-6,7,7,-4,7,4,1,6,-6,-10,-4,-8,-1,-4]],[[2,9,4,1,-5,2,-6,8,6,1,-4,1,-2,-2],[-3,-5,4,-4,1,2,2,-8,10,-6,-3,-10,-1,-5]],[[-9,-5,3,1,3,8,3,-10,5,3,-5,4,7,-2],[-5,1,-4,-8,6,4,7,5,-1,-4,2,-2,8,2]],[[-9,6,-1,-10,5,2,9,3,8,-5,3,-5,-7,-10],[2,2,8,5,-5,6,3,3,6,8,-4,-2,2,-9]],[[-4,-6,5,-6,-6,-4,-6,-10,10,10,9,-9,1,-9],[-7,-2,9,7,-3,-9,-6,9,5,2,5,3,-2,-7]],[[4,-5,-2,3,-4,7,5,-6,9,4,7,1,-10,3],[9,-6,-6,7,6,1,-2,7,4,-10,-1,7,4,7]],[[4,-7,-2,9,2,5,-6,9,-7,-5,2,-4,-4,10],[-10,-2,-10,9,-10,9,-4,1,5,8,-6,2,10,2]],[[6,-2,10,-1,2,2,10,-3,10,-2,2,6,3,-8],[4,9,-2,6,-4,2,-9,-8,-8,1,5,-4,5,8]]], dtype = "uint16")#candidate|1121|(10, 2, 14)|const|uint16
const_1122 = relay.const([[[5,-2,3,-7,10,-9,1,-6,4,-7,8,-2,8,-8],[8,8,-3,8,-4,2,-4,-10,8,-3,2,9,-5,-2]],[[2,3,9,5,-2,9,-9,9,3,10,9,-4,-5,-10],[7,-7,-2,-10,2,5,8,9,7,3,-1,-1,-10,9]],[[9,8,-1,-6,-3,-6,-2,10,-4,-9,9,1,7,-10],[9,2,1,6,3,7,-10,5,-1,-4,-4,-8,-7,4]],[[-2,-10,-4,-1,-2,-8,-2,-5,5,4,4,3,-5,10],[-9,-7,-9,-2,-1,9,-3,-2,-10,-5,6,-1,1,8]],[[-4,-7,5,3,-3,6,-9,9,1,-7,10,-6,-5,-9],[-2,2,7,10,-5,5,-10,-4,-7,-3,6,-9,-3,-5]],[[3,-3,-2,4,6,3,-7,-9,-1,-7,6,5,9,-10],[-9,9,8,-9,-10,-2,-7,8,-3,-2,-10,3,9,9]],[[1,8,-4,-4,-2,-5,-9,7,-1,-1,-1,-1,2,-8],[1,6,-7,-6,3,3,6,-8,-2,1,1,8,-5,-5]],[[-2,-5,-10,-8,5,-6,-5,-6,5,-6,-10,-2,6,-4],[-10,7,10,6,-1,7,-10,8,9,8,9,-3,-8,-9]],[[7,-7,-10,9,-6,-2,-1,7,-1,9,-9,6,-9,-5],[5,5,-7,9,9,-9,-6,2,-1,1,3,2,6,-10]],[[-6,-6,-10,5,5,5,5,-7,-7,8,-7,8,8,-2],[7,-1,-6,7,8,-3,7,5,4,-5,-2,-10,4,10]]], dtype = "uint16")#candidate|1122|(10, 2, 14)|const|uint16
bop_1123 = relay.add(const_1121.astype('uint16'), relay.reshape(const_1122.astype('uint16'), relay.shape_of(const_1121))) # shape=(10, 2, 14)
bop_1130 = relay.greater(bop_1123.astype('bool'), relay.reshape(const_1122.astype('bool'), relay.shape_of(bop_1123))) # shape=(10, 2, 14)
output = relay.Tuple([bop_1130,])
output2 = relay.Tuple([bop_1130,])
func_1140 = relay.Function([], output)
mod['func_1140'] = func_1140
mod = relay.transform.InferType()(mod)
mutated_mod['func_1140'] = func_1140
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1140_call = mutated_mod.get_global_var('func_1140')
call_1141 = func_1140_call()
output = call_1141
func_1142 = relay.Function([], output)
mutated_mod['func_1142'] = func_1142
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1140_call = mod.get_global_var('func_1140')
func_1142_call = mutated_mod.get_global_var('func_1142')
call_1163 = relay.TupleGetItem(func_1140_call(), 0)
call_1164 = relay.TupleGetItem(func_1142_call(), 0)
output = relay.Tuple([call_1163,])
output2 = relay.Tuple([call_1164,])
func_1167 = relay.Function([], output)
mod['func_1167'] = func_1167
mod = relay.transform.InferType()(mod)
mutated_mod['func_1167'] = func_1167
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1167_call = mutated_mod.get_global_var('func_1167')
call_1168 = func_1167_call()
output = call_1168
func_1169 = relay.Function([], output)
mutated_mod['func_1169'] = func_1169
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1167_call = mod.get_global_var('func_1167')
func_1169_call = mutated_mod.get_global_var('func_1169')
call_1239 = relay.TupleGetItem(func_1167_call(), 0)
call_1240 = relay.TupleGetItem(func_1169_call(), 0)
output = relay.Tuple([call_1239,])
output2 = relay.Tuple([call_1240,])
func_1249 = relay.Function([], output)
mod['func_1249'] = func_1249
mod = relay.transform.InferType()(mod)
mutated_mod['func_1249'] = func_1249
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1249_call = mutated_mod.get_global_var('func_1249')
call_1250 = func_1249_call()
output = call_1250
func_1251 = relay.Function([], output)
mutated_mod['func_1251'] = func_1251
mutated_mod = relay.transform.InferType()(mutated_mod)
func_442_call = mod.get_global_var('func_442')
func_443_call = mutated_mod.get_global_var('func_443')
call_1259 = relay.TupleGetItem(func_442_call(), 0)
call_1260 = relay.TupleGetItem(func_443_call(), 0)
var_1275 = relay.var("var_1275", dtype = "bool", shape = (11, 13, 7))#candidate|1275|(11, 13, 7)|var|bool
bop_1276 = relay.bitwise_and(call_1259.astype('int64'), relay.reshape(var_1275.astype('int64'), relay.shape_of(call_1259))) # shape=(11, 13, 7)
bop_1279 = relay.bitwise_and(call_1260.astype('int64'), relay.reshape(var_1275.astype('int64'), relay.shape_of(call_1260))) # shape=(11, 13, 7)
var_1281 = relay.var("var_1281", dtype = "bool", shape = (11, 13, 7))#candidate|1281|(11, 13, 7)|var|bool
bop_1282 = relay.less(var_1275.astype('bool'), relay.reshape(var_1281.astype('bool'), relay.shape_of(var_1275))) # shape=(11, 13, 7)
output = relay.Tuple([bop_1276,bop_1282,])
output2 = relay.Tuple([bop_1279,bop_1282,])
func_1285 = relay.Function([var_1275,var_1281,], output)
mod['func_1285'] = func_1285
mod = relay.transform.InferType()(mod)
var_1286 = relay.var("var_1286", dtype = "bool", shape = (11, 13, 7))#candidate|1286|(11, 13, 7)|var|bool
var_1287 = relay.var("var_1287", dtype = "bool", shape = (11, 13, 7))#candidate|1287|(11, 13, 7)|var|bool
output = func_1285(var_1286,var_1287,)
func_1288 = relay.Function([var_1286,var_1287,], output)
mutated_mod['func_1288'] = func_1288
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1350 = relay.var("var_1350", dtype = "float32", shape = (11, 13, 11))#candidate|1350|(11, 13, 11)|var|float32
var_1351 = relay.var("var_1351", dtype = "float32", shape = (11, 13, 11))#candidate|1351|(11, 13, 11)|var|float32
bop_1352 = relay.divide(var_1350.astype('float32'), relay.reshape(var_1351.astype('float32'), relay.shape_of(var_1350))) # shape=(11, 13, 11)
func_961_call = mod.get_global_var('func_961')
func_964_call = mutated_mod.get_global_var('func_964')
const_1366 = relay.const([6.886649,1.510375,-3.387942,-8.966515,2.368105,-8.855801,-2.139713,2.926450,6.378151,4.657043,-7.053998,-7.482795,7.051466,8.277047,8.473959,3.800477,4.692763,-2.588722,-0.767280,-7.982692,-7.686945,-5.887626,2.062455,-1.106149,7.943994,-9.693953,-5.899707,-9.863870,9.105398,-4.960071,5.584423,9.419535,2.298977,-8.231784,-8.022411,8.877280,-2.462472,3.636141,3.760460,-0.083305,-1.987024,-7.707412,4.156779,-7.881675,-8.499186,7.742694,-4.092158,-4.172590,-9.108525,1.578308,-3.057668,9.367324,-5.322641,-1.717304,-8.295257,7.229888,0.701061,9.603897,-3.668520,0.475769,5.617462,-9.377942,9.912277,9.636779,-6.015229,7.916673,8.048401,2.694611,9.423087,6.856628,-9.124720,-2.493081,-9.089638,-6.203576,0.586584,1.325623,-9.688114,7.103494,4.610730,-3.426953,9.254514,-1.614491,-7.591885,3.852998,8.290057,-0.890276,4.626545,-5.720057,-3.625888,-3.065126,-2.787346,-6.140127,-2.817777,6.195896,-0.950584,3.160002,5.392533,-6.704818,8.567632,0.987564,-3.996221,-9.015020,1.234893,6.670674,3.913136,6.460696,-5.769271,-4.835151,1.225080,-6.769927,5.075453,-5.559063,9.940663,2.414525,-5.141721,6.994524,-1.229705,-7.938629,-0.115624,1.972694,5.353877,-1.572342,9.973976,-5.299780,-7.110078,-3.069112,-7.489892,-9.109314,-8.585134,-4.107398,-0.887972,3.547268,8.255001,-7.606470,-7.499749,5.082424,8.936025,6.126024,2.568872,3.746139,-9.022387,1.483260,-5.010322,-4.779962,5.736071,5.435966,-0.952217,-9.648269,-3.663642,-8.989460,1.360776,6.228130,4.318332,5.314567,-5.289999,-8.611017,-9.835000,-3.403578,4.911637,9.231016,8.123803,-8.556134,-2.641248,-4.325202,-2.769741,8.395938,-1.113690,-7.254976,9.980236,-8.121749,-4.241227,-8.573399,6.026012,-7.393346,4.217174,2.525997,-0.042137,-5.486952,0.577253,-2.972938,9.206566,9.547629,-2.717927,3.087838,3.025275,2.233627,-1.040649,-9.296387,-9.550736,-4.793373,0.201456,5.431586,-7.061908,-5.462401,-9.637152,6.642435,-6.725750,5.264278,-3.628464,-6.623621,0.502608,6.220198,1.827396,5.197520,-7.582495,6.180388,5.448381,-8.705654,-6.927480,0.509212,9.786263,2.438174,7.119895,-3.015951,5.171759,4.858564,-1.712563,7.857980,8.324850,-3.434361,-6.891007,1.525966,-5.466346,7.647594,-5.297671,1.551419,0.569250,9.027430,6.714953,-6.732048,-2.867709,4.383230,0.170291,-0.055935,2.287671,-4.782430,-1.282087,-8.854045,3.854353,7.623835,-6.536972,9.828132,7.796482,4.862844,-6.600358,-1.068677,1.725858,-9.226533,-0.964359,1.470045,1.795605,6.610133,7.754476,-0.988571,-2.576998,-6.412150,-2.255634,-7.403277,-8.454649,-3.844769,-9.921912,7.038835,7.622517,-3.094037,-6.279842,5.105474,3.077758,0.916885,-3.280789,-1.318034,-5.136106,-0.748588,-9.130771,-3.633735,-0.047553,-0.627822,6.512616,-7.489181,7.841796,-3.933040,9.909812,5.212128,1.051591,6.309579,-1.219153,-0.674014,9.795839,2.552151,9.492303,-8.520936,-6.079476,-8.238754,7.213294,-8.219463,0.375357,-0.951993,7.840771,-7.793161,5.870822,-0.649032,7.328043,-7.216040,5.877362,-7.467047,0.539854,-1.815331,7.386071,-4.024308,-8.240870,0.934679,4.453189,-6.645954,3.608312,4.762935,-1.085010,-2.029894,-1.102988,-8.897784,-8.828649,1.925635,-0.352582,-8.424220,-5.523635,-9.122732,7.073468,3.267954,1.241162,2.526167,-1.547759,0.440848], dtype = "float64")#candidate|1366|(330,)|const|float64
const_1367 = relay.const([-1.336662,4.739466,2.860986,7.093552,1.555430,-2.841573,-6.057291,-3.583719,-8.278978,-8.177796,6.892637,2.803450,2.212877,-8.180937,-9.997114,-0.296358,-1.020334,-4.570967,-4.128100,4.899016,2.865443,-3.607639,-8.612057,5.732440,-2.590328,-6.483033,-3.214067,3.109096,8.178352,-9.861754,-0.978268,-0.264527,-1.620634,-7.587174,-4.921970,-3.257515,9.792526,3.423055,1.691026,7.048660,2.666258,5.872911,1.377340,7.160459,2.017203,-7.694881,-1.761661,-7.613789,3.982124,-9.654618,-5.869869,0.733235,3.465715,9.042223,-6.824560,-5.629330,-0.159097,2.784659,-5.203335,-3.302809,-3.116969,9.026388,-5.446976,4.655869,-7.312251,3.541894,4.312784,8.386405,-7.591881,7.160888,8.523606,-7.163335,-4.246779,5.919274,-9.346773,-7.124222,-8.379678,7.288319,9.090118,9.510012,-7.213158,-8.592666,9.807657,-3.921043,-2.390038,-4.532150,8.813982,2.956361,-2.456465,-2.004566,8.555014,3.704876,-8.702894,-7.187552,-7.211437,-7.971751,-7.175866,-5.264183,-0.822971,7.015515,-3.428025,-1.212523,-6.321874,5.025855,-0.246226,1.156142,-6.001356,7.207456,-7.092822,-7.439017,7.267317,5.665155,2.912970,-7.472832,9.780409,-4.958666,9.099676,8.118514,5.296353,4.942538,4.384384,7.864809,9.689936,-3.368577,-2.551975,-9.399828,2.224356,8.261784,4.947758,-3.847286,-0.908134,5.051803,9.203858,1.717516,1.541748,-1.748737,-7.213472,2.049900,3.804118,1.065459,-8.565073,0.198529,6.412444,9.791063,-9.948470,6.110595,-2.968621,4.250202,-7.147640,-1.691633,1.557923,-3.624629,-3.750854,4.860667,3.014708,4.490659,9.601006,-9.677992,-6.682164,2.842338,7.343804,4.089343,4.009154,-2.805240,5.631921,-5.589871,7.337955,-7.512600,-9.690785,6.216763,-2.258156,5.184945,-4.047177,3.718669,8.996066,6.523919,2.897148,5.296745,7.769002,-9.014469,-7.383191,8.763576,7.827644,-2.980978,-2.057705,-1.615563,-8.038239,-6.795992,0.885048,6.829490,-0.505697,8.134333,6.647698,2.460566,-2.860281,-3.767467,-7.990447,1.483459,1.446963,4.008768,1.346314,5.548222,9.154633,-3.717327,3.668360,-3.028258,0.067703,6.105564,-5.629261,3.325674,6.530846,5.410978,-6.140083,2.980503,-0.041258,4.174676,-1.183952,-7.690789,-0.710829,-3.184425,-7.485175,8.718879,3.828757,9.580439,1.473879,-2.610599,-3.122150,-8.078225,-9.891640,-1.280143,-7.540135,7.104622,-3.773209,6.651847,-5.817623,-8.743317,-2.954023,-6.242697,1.182304,8.242088,9.261957,4.930905,0.956689,-1.426531,3.455415,3.575349,-7.769888,2.762014,-0.249283,3.555547,-6.559436,3.536664,0.715171,-0.195867,7.612631,-3.961496,-7.482559,-8.919319,6.184786,8.363247,-1.021063,8.091509,3.151948,6.993724,5.308670,7.529951,9.012070,-4.911322,-5.955774,3.633537,-9.048740,-0.559084,4.951844,-1.172581,8.743395,8.332238,-2.243546,-1.280106,8.615739,2.585237,-2.174616,1.785741,-8.298151,5.425916,-3.274097,-2.198519,-3.122794,2.946876,-2.635856,-6.908649,-3.050623,7.771698,-5.143977,-3.273410,3.589185,-6.207382,-1.669852,2.768519,7.344638,-5.122420,5.624451,-8.036715,0.609378,6.901757,-4.913777,-3.053732,-7.404389,2.846967,0.060275,-6.123010,-4.030611,5.983914,-8.657913,4.248118,4.036867,-9.668965,-8.952779,-6.524108,-6.106505,8.369585,8.949883,3.760287,5.792032,2.765538,5.808794,-4.475273,-4.913427,-0.849551,-7.873258,1.258535,6.292485,4.416382,-7.962674,-1.852391,0.158922,4.789676,7.351800,-7.994041,-2.921225,3.695455,-0.449520,8.570120,6.128100,5.521002,0.471663,6.260669,-8.405479,-7.224359,-8.536181,-3.279323,8.586543,1.777662,-5.128920,2.374255,8.911580,-7.782824,-2.471912,-5.674721,-3.145616,-2.652921,-9.878006,-4.410339,-9.097855,-6.390288,8.153592,-1.148949,-0.393045,5.442287,-1.317313,7.767550,-2.806476,8.173980,4.957881,-7.121732,1.052998,1.137424,5.407918,4.822788,6.386611,-2.616581,-5.032721,4.531045,-7.456048,5.023841,7.096559,-1.303960,9.636268,8.490997,-4.735320,-4.978202,-9.272430,0.995474,8.426021,5.809527,-6.063521,-8.945873,-1.384707,-6.669329,-7.568607,4.847410,-6.853548,9.033201,6.064523,1.952812,5.808751,-7.735345,2.745084,0.004793,-4.247641,5.732933,-2.855744,0.530526,2.958616,-9.330902,4.694390,-2.411484,5.198463,3.569736,-5.122521,-4.670494,-8.375857,7.758447,0.015773,8.278690,2.526423,-4.234401,-3.793906,-5.775336,0.521275,6.547221,3.412523,5.007053,-1.626547,6.801065,3.926157,-4.193934,-8.735769,2.286528,-9.326732,1.984098,-9.164518], dtype = "float32")#candidate|1367|(441,)|const|float32
call_1365 = relay.TupleGetItem(func_961_call(relay.reshape(const_1366.astype('float64'), [15, 2, 11]), relay.reshape(const_1367.astype('float32'), [441,]), ), 5)
call_1368 = relay.TupleGetItem(func_964_call(relay.reshape(const_1366.astype('float64'), [15, 2, 11]), relay.reshape(const_1367.astype('float32'), [441,]), ), 5)
func_564_call = mod.get_global_var('func_564')
func_567_call = mutated_mod.get_global_var('func_567')
const_1372 = relay.const([[4.035358],[2.270009],[5.619740],[-5.908440],[-0.965680],[2.661576],[7.574920],[-1.546197],[-6.999481],[-5.702453],[5.042725],[7.563428],[-1.748634],[3.963066],[-7.614857],[2.870432],[9.013654],[5.557223],[-3.623318],[-5.597331],[7.706223],[-6.405265],[-4.475914],[6.226940],[3.765047],[4.949130],[-1.911823],[-0.178445],[-7.680943],[7.006247],[0.863331],[-9.432187],[-2.396697],[-7.788273],[8.562874],[3.585245],[-0.222680],[-2.939521],[-5.757687],[1.936928],[5.600240],[7.013818],[-9.663964],[-5.975388],[5.814578],[1.128043],[-8.610749],[3.529096],[8.902861],[-3.555632],[-0.889486],[-5.795851],[8.516217],[5.121348],[-9.446395],[-3.329999],[-9.879133],[8.936930],[9.146937],[2.829538],[-8.875583],[1.951677],[-2.195123],[7.896548],[-2.856530],[-9.944586],[5.843326],[-3.033259],[9.603614],[5.631372],[-0.499590],[-6.693255],[9.181582],[7.528033],[6.981538],[0.692258],[5.752817],[1.400148],[6.266513],[-7.591224],[-3.954840],[-2.270644],[0.428176],[-5.838432],[-8.238510],[-2.076739],[1.446451],[1.297891],[-6.582662],[8.681053],[2.623802],[0.173371],[-1.604258],[-3.761808],[9.983433],[9.333326],[-6.012008],[-6.165348],[-3.369233],[-3.717457],[-0.603500],[-7.135110],[4.315162],[-6.638205],[-3.325681],[-9.423367],[-2.640924],[6.995599],[-9.462418],[-8.981010],[-7.839410],[8.296987],[0.756911],[-0.731420],[-7.152857],[-1.384482],[6.833371],[0.533553],[5.839361],[-5.464295],[6.566008],[7.506677],[8.696938],[-8.047854],[4.305525],[4.136897],[3.675902],[-9.931230],[-0.626621],[-5.389110],[9.317521],[7.635515],[9.513237],[-5.765278],[-3.268823],[7.647461],[0.015956],[0.412867],[3.966467],[-2.061424],[-6.855034],[-6.813957],[-6.440894],[-6.586682],[0.695516],[3.002615],[-3.220373],[2.148388],[7.097429],[-4.368463],[-8.019411],[-1.862034],[-3.449705],[-0.440828],[0.369582],[-7.666287],[0.383240],[7.273565],[0.552077],[-5.598586],[7.481343],[-6.593994],[9.412588],[0.698706],[8.023199],[-6.491664],[2.407040],[8.330040],[9.197442],[9.192293],[-1.211832],[-3.053206],[-9.285204],[0.019205],[-3.981226],[-7.949354],[8.300732],[7.143156],[-1.499555],[-6.316580],[-6.548438],[-7.289044],[2.456715],[4.290808],[1.287169],[8.300677],[7.734181],[2.793811],[-0.482685],[5.421381],[5.558619],[-0.382481],[-0.846399],[3.304729],[-7.871806],[-0.667076],[-3.600241],[8.322383],[-2.496590],[-6.725912],[5.390456],[9.337906],[-6.434549],[4.173611],[4.699684],[2.943705],[-9.968877],[-4.757376],[7.115549],[-8.471781],[3.922432],[-2.579243],[5.429917],[8.079122],[-2.736053],[1.404629],[9.715999],[-1.597219],[-6.842811],[-0.265383],[9.867846],[-7.724477],[5.992515],[-1.303089],[-5.955550],[1.994048],[-7.177966],[4.892699],[4.743539],[6.367631],[7.214435],[9.585881],[-4.786481],[-9.719497],[9.564362],[-4.079392],[-8.216632],[1.110954],[3.917673],[-2.104870],[-5.109966],[0.311942],[3.247153],[-2.409107],[0.173445],[-0.710541],[-2.104142],[-6.975525],[-3.013569],[4.854362],[1.901401],[-8.931121],[-9.327686],[-4.876661],[5.848144],[1.557189],[-7.670199],[-2.941142],[-5.651351],[-6.069858],[3.851987],[-4.145147],[-0.799181],[-1.547730],[8.762596],[5.333275],[1.200469],[-6.768951],[1.864341],[-1.641378],[2.571843],[-6.332026],[-4.787166],[1.846098],[5.719859],[7.679600],[-2.714656],[-3.034596],[-9.080886],[7.100137],[3.859907],[-5.622271],[-3.809282],[-3.253900],[6.704461],[7.169481],[6.341490],[-4.696678],[-3.995420],[-0.199756],[1.241138],[-2.561843],[6.222525],[0.896126],[2.089136],[0.885316],[0.994450],[-2.371661],[-7.175902],[5.604173],[7.279340],[-2.127735],[-3.595515],[-3.803672],[-2.870233],[-2.141176],[-7.113354],[1.006164],[7.460067],[6.237907],[-9.104910],[5.615723],[3.102991],[1.276189],[0.532460],[4.939404],[3.440906],[5.367109],[1.955150],[7.834854],[-2.246002],[1.302334],[-5.766797],[-0.932027],[9.421728],[5.312155],[-1.610865],[9.991664],[-7.498013],[1.592833],[2.449107],[-7.412229],[-1.429343],[-3.200354],[1.558380],[2.093348],[6.750352],[3.492390],[1.249893],[-0.276777],[4.280234],[-7.247811],[-0.513151],[3.694079],[7.039620],[-8.978995],[-9.724421],[1.959240],[-5.085502],[-3.129171],[3.425971],[9.673027],[-1.760569],[7.629134],[-5.046604],[2.539273],[6.738987],[2.636621],[0.936755],[-5.904729],[1.169712],[-0.434036],[3.731129],[-4.916246],[0.897571],[5.148030],[-7.400169],[-8.841848],[2.176288],[7.780482],[8.679818],[-0.122587],[-0.082734],[-2.149516],[-7.047995],[-2.269733],[-7.213369],[4.113604],[0.006513],[3.983486],[-5.183257],[7.759499],[-9.021771],[-8.855897],[1.896762],[3.042591],[-4.036061],[7.896681],[-3.735923],[-8.238547],[-8.889805],[-6.155215],[8.452780],[-7.108939],[-8.227187],[-1.779598],[0.446179],[8.158666],[4.366541],[6.943760],[2.800995],[9.244590],[-6.707808],[0.045288],[-3.740207],[-6.037439],[-3.475847],[3.946331],[-8.114157],[-7.380175],[-9.852677],[-2.455960],[5.661048],[2.247158],[6.074894],[4.295687],[4.709162],[-2.016717],[-4.282759],[-0.812448],[1.219034],[2.920730],[-5.131397],[-6.866590],[9.042865],[8.030477],[9.505988],[1.164860],[3.267852],[3.615704],[8.318889],[-6.492646],[7.366777],[6.658062],[-7.246500],[-4.456830],[-1.670064],[5.953913],[7.392356],[0.332212],[8.350302],[-9.950014],[-7.850814],[4.603419],[-0.457431],[-7.731028],[4.728456],[-0.043416],[8.791915],[-5.101900],[-6.309871],[-9.875314],[6.008850],[2.357933],[1.634324],[5.813884],[4.731227],[8.976728],[6.842285],[1.294182],[7.450738],[9.205025],[-5.791273],[9.046248],[6.556689],[6.982392],[-2.205360],[-8.048916],[-3.143132],[-2.793593],[2.956463],[-3.901657],[6.851572],[-7.489023],[-3.884258],[-3.841990],[-6.458941],[-9.893152],[-2.975107],[-2.370488],[-3.776566],[3.512383],[7.802543],[-2.916967],[5.277862],[3.421674],[-0.166034],[4.285131],[4.062011],[-3.716318],[8.838334],[2.609021],[-4.724244],[5.480449],[1.730452],[5.604743],[7.343590],[1.665274],[-6.173596],[-1.623277],[-0.760462],[-6.910157],[4.581499],[9.069539],[-4.796198],[-1.475521],[-2.796558],[8.580144],[-6.896513],[0.925204],[-0.162558],[8.100444],[3.222543],[9.326354],[-2.438407],[9.954496],[1.214130],[5.435913],[6.135347],[-3.208474],[-1.951864],[-0.887775],[-9.186195],[7.893481],[-8.038082],[8.080245],[8.253935],[-4.447548],[5.206718],[2.462022],[-2.884117],[-0.186837],[-5.811161],[-4.533054],[-7.518444],[9.317235],[-9.635920],[-4.281541],[4.955730],[5.939932],[-0.298964],[7.374705],[8.591204],[1.238517],[0.030611],[-6.060475],[5.723010],[5.253324],[-4.933220],[-6.877294],[-3.131714],[4.552276],[1.210578],[-5.732115],[1.089986],[-7.821606],[-5.743626],[-9.947293],[5.851438],[-6.745433],[-5.100047],[-8.803289],[5.322853],[3.057935],[-4.769469],[8.455555],[-0.131341],[5.652305],[-0.265710],[-9.708270],[4.635482],[4.057588],[-6.225695],[8.168942],[2.078327],[-4.694967],[-7.681580],[-1.862829],[1.378128],[6.717813],[0.023676],[-2.506940],[6.764271],[7.909588],[1.548283],[9.970180],[-8.021183],[-5.118278],[-4.529113],[-4.838317],[3.767754],[3.406917],[-2.533677],[-8.537467],[-8.763449],[6.289970],[-5.266743],[9.932644],[1.111971],[0.304512],[-1.865279],[2.142057],[4.785650],[-6.746998],[3.929542],[-0.569657],[8.082316],[-0.071760],[2.366594],[1.312133],[-1.919080],[0.151136],[4.210233],[-0.740511],[8.957232],[0.269857],[-8.940117],[-3.335267],[8.053602],[-3.750172],[0.249931],[3.728872],[-2.720152],[-3.659550],[-6.101698],[4.348692],[-2.157152],[3.537501],[4.549025],[-0.557723],[4.265334],[9.109280],[-5.919203],[-9.591134],[-1.023777],[-8.757094],[8.467496],[-3.889918],[6.507220],[4.660402],[6.354061],[-0.992669],[1.319978],[6.670299],[5.615189],[6.087505],[1.591280],[3.083051],[-8.990855],[4.834403],[-1.432495],[-7.094046],[-4.714138],[3.515054],[-3.121547],[1.499419],[-1.181283],[9.129737],[-5.654049],[-5.964692],[5.752179],[-0.608141],[-6.467241],[-7.329585],[6.149709],[4.573474],[-9.238404],[0.835422],[5.026102],[-3.372513],[0.683577],[1.157293],[-5.751071],[4.882240],[1.678500],[-4.159136],[0.645116],[9.382373],[-7.837698],[-1.384875],[-9.781783],[8.765687],[-1.338709],[4.585609],[-2.163890],[5.540524],[7.556700],[7.147837],[4.590637],[-7.956662],[-8.085810],[0.929122],[-9.820664],[-0.234163],[9.654308],[-5.390866],[-6.511659],[-3.563770],[9.878281],[-6.074911],[1.395381],[3.842173],[-7.989788],[-8.300077],[-9.063848],[-7.068156],[-4.696410],[-9.307348],[1.165436],[3.550599],[-9.699030],[-8.338459],[-8.096233],[6.449122],[-2.569917],[6.054445],[8.837745],[-6.099153],[1.336856],[5.038734],[-0.679999],[-1.104117],[-0.647174],[0.844011],[5.553514],[-3.960563],[-7.147579],[7.615525],[2.634454],[-2.467270],[-4.317081],[8.028835],[6.808375],[-1.948385],[4.714402],[-4.749089],[5.922852],[-5.914023],[4.763693],[3.453112],[-3.237806],[-4.833175],[-5.066556],[4.824613],[-1.563188],[7.937424],[3.430508],[-3.578611],[1.173530],[5.342927],[3.965266],[-0.627752],[1.577960],[-3.201417],[-1.552388],[1.621015],[0.402096],[4.870431],[2.982379],[1.711825],[0.765262],[0.869736],[6.549241],[0.007375],[-3.175974],[2.619899],[-4.100518],[-2.714124],[-0.541634],[-2.203032],[0.607427],[-7.665705],[-8.998576],[-5.216873],[-4.386502],[8.159024],[0.385400],[6.815191],[4.022910],[1.132772],[6.328649],[9.166679],[-6.739070],[2.267248],[-8.222926],[2.141670],[-1.905362],[-0.839203],[8.873928],[-7.846555],[-1.387141],[3.698205],[-1.975842],[-4.485807],[6.407979],[8.116817],[7.571509],[-8.825921],[5.492056],[-3.611422],[-8.552001],[5.189892],[4.921518],[8.397711],[-8.667467],[1.517700],[0.007409],[-7.696226],[5.517777],[6.329333],[-6.535731],[8.668456],[3.196858],[8.388513],[-8.795429],[-1.274156],[8.039372],[1.531238],[0.194805],[-1.334833],[-2.209080],[-0.443679],[-7.456225],[-0.719099],[-1.467792],[2.575445],[-5.773598],[-7.065273],[-4.772029],[-6.015627],[1.309478],[1.062078],[-5.270452],[-6.647676],[0.645180],[-5.394915],[-0.849757],[-6.991892],[1.789128],[-5.077727],[-3.471621],[6.524497],[-8.641508],[4.571245],[1.738324],[5.638736],[-2.438082],[-6.372339],[1.820577],[9.755558],[4.030854],[6.598652],[-0.490737],[-7.750906],[-2.575923],[0.248218],[-1.447436],[5.032642],[-5.203524],[-2.263695],[3.501115],[6.244183],[-7.732890],[-2.325640],[-9.997165],[8.697541],[3.846279],[0.721373],[-8.265967],[-8.538450],[-6.969299],[2.933234],[-0.138930],[1.945540],[1.043316],[-6.473979],[-8.683861],[6.933783],[2.022381],[-6.495522],[7.863100],[0.933608],[-7.947052],[-6.376767],[2.654567],[7.023610],[4.526458],[-2.769232],[-8.646519],[-5.558107],[1.175341],[-1.409051],[-2.347105],[4.425605],[3.228995],[9.797777],[8.478349],[-9.563420],[3.463050],[-4.874949],[1.760353],[-3.865963],[-2.202354],[-8.199810],[4.145816],[3.361308],[4.981656],[-0.876466],[9.671423],[-0.483548],[8.466621],[7.070332],[-9.051654],[7.847864],[-6.291778],[-6.605906],[1.457146],[-1.983289],[-9.874106],[-3.115540],[-0.886169],[-7.790832],[9.102607],[7.133864],[-9.387180],[-7.090098],[-5.719200],[-0.391159],[6.353672],[-8.719859],[3.174192],[0.233821],[-8.264681],[6.780938],[-2.934600],[-4.802242],[5.992078],[-7.179788],[8.855101],[0.869512],[8.698552],[9.248157],[2.277556],[5.595122],[0.685306],[-4.275178],[-2.811697],[-9.383116],[-1.524828],[1.669925],[6.517978],[0.975629],[1.428350],[-9.513482],[7.620846],[-4.005371],[6.928969],[-7.269541],[-7.423200],[0.039325],[-4.811452],[-7.722834],[6.140004],[5.014669],[-0.888758],[-1.928076],[-0.013248],[-1.007392],[1.737544],[-0.655006],[-5.413722],[-6.941900],[-4.437073],[-7.308122],[-7.217866],[8.840570],[-5.903672],[3.213134],[-8.677396],[0.311838],[-6.403039],[-5.886500],[3.792595],[-3.981461],[2.470197],[1.700735],[7.978726],[1.570599],[9.333559],[-0.317842],[8.345677],[-3.980656],[-7.444676],[8.194131],[-1.985982],[6.465301],[-2.912926],[8.928599],[4.682157],[9.726680],[-1.623549]], dtype = "float64")#candidate|1372|(1001, 1)|const|float64
var_1373 = relay.var("var_1373", dtype = "float64", shape = (14, 3))#candidate|1373|(14, 3)|var|float64
call_1371 = relay.TupleGetItem(func_564_call(relay.reshape(const_1372.astype('float64'), [11, 13, 7]), relay.reshape(var_1373.astype('float64'), [42,]), ), 4)
call_1374 = relay.TupleGetItem(func_567_call(relay.reshape(const_1372.astype('float64'), [11, 13, 7]), relay.reshape(var_1373.astype('float64'), [42,]), ), 4)
uop_1377 = relay.sinh(var_1351.astype('float64')) # shape=(11, 13, 11)
output = relay.Tuple([bop_1352,call_1365,const_1366,const_1367,call_1371,const_1372,var_1373,uop_1377,])
output2 = relay.Tuple([bop_1352,call_1368,const_1366,const_1367,call_1374,const_1372,var_1373,uop_1377,])
func_1380 = relay.Function([var_1350,var_1351,var_1373,], output)
mod['func_1380'] = func_1380
mod = relay.transform.InferType()(mod)
mutated_mod['func_1380'] = func_1380
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1380_call = mutated_mod.get_global_var('func_1380')
var_1382 = relay.var("var_1382", dtype = "float32", shape = (11, 13, 11))#candidate|1382|(11, 13, 11)|var|float32
var_1383 = relay.var("var_1383", dtype = "float32", shape = (11, 13, 11))#candidate|1383|(11, 13, 11)|var|float32
var_1384 = relay.var("var_1384", dtype = "float64", shape = (14, 3))#candidate|1384|(14, 3)|var|float64
call_1381 = func_1380_call(var_1382,var_1383,var_1384,)
output = call_1381
func_1385 = relay.Function([var_1382,var_1383,var_1384,], output)
mutated_mod['func_1385'] = func_1385
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1167_call = mod.get_global_var('func_1167')
func_1169_call = mutated_mod.get_global_var('func_1169')
call_1407 = relay.TupleGetItem(func_1167_call(), 0)
call_1408 = relay.TupleGetItem(func_1169_call(), 0)
output = relay.Tuple([call_1407,])
output2 = relay.Tuple([call_1408,])
func_1412 = relay.Function([], output)
mod['func_1412'] = func_1412
mod = relay.transform.InferType()(mod)
mutated_mod['func_1412'] = func_1412
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1412_call = mutated_mod.get_global_var('func_1412')
call_1413 = func_1412_call()
output = call_1413
func_1414 = relay.Function([], output)
mutated_mod['func_1414'] = func_1414
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1412_call = mod.get_global_var('func_1412')
func_1414_call = mutated_mod.get_global_var('func_1414')
call_1425 = relay.TupleGetItem(func_1412_call(), 0)
call_1426 = relay.TupleGetItem(func_1414_call(), 0)
output = call_1425
output2 = call_1426
func_1435 = relay.Function([], output)
mod['func_1435'] = func_1435
mod = relay.transform.InferType()(mod)
output = func_1435()
func_1436 = relay.Function([], output)
mutated_mod['func_1436'] = func_1436
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1140_call = mod.get_global_var('func_1140')
func_1142_call = mutated_mod.get_global_var('func_1142')
call_1437 = relay.TupleGetItem(func_1140_call(), 0)
call_1438 = relay.TupleGetItem(func_1142_call(), 0)
uop_1451 = relay.log(call_1437.astype('float64')) # shape=(10, 2, 14)
uop_1453 = relay.log(call_1438.astype('float64')) # shape=(10, 2, 14)
uop_1457 = relay.cosh(uop_1451.astype('float32')) # shape=(10, 2, 14)
uop_1459 = relay.cosh(uop_1453.astype('float32')) # shape=(10, 2, 14)
output = uop_1457
output2 = uop_1459
func_1461 = relay.Function([], output)
mod['func_1461'] = func_1461
mod = relay.transform.InferType()(mod)
mutated_mod['func_1461'] = func_1461
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1461_call = mutated_mod.get_global_var('func_1461')
call_1462 = func_1461_call()
output = call_1462
func_1463 = relay.Function([], output)
mutated_mod['func_1463'] = func_1463
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1034_call = mod.get_global_var('func_1034')
func_1035_call = mutated_mod.get_global_var('func_1035')
call_1485 = relay.TupleGetItem(func_1034_call(), 0)
call_1486 = relay.TupleGetItem(func_1035_call(), 0)
output = relay.Tuple([call_1485,])
output2 = relay.Tuple([call_1486,])
func_1497 = relay.Function([], output)
mod['func_1497'] = func_1497
mod = relay.transform.InferType()(mod)
output = func_1497()
func_1498 = relay.Function([], output)
mutated_mod['func_1498'] = func_1498
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1540 = relay.const([[[-8.757801,4.958681,-3.140309,4.303841,7.057671,9.007991,-3.980102,3.684779,8.305969,-3.575806,9.454901,-6.950050,1.551789,-7.187016,-2.136409,1.645438],[0.386590,2.390016,4.612053,3.156535,9.553910,-2.998168,5.848554,3.135046,-2.180125,-0.022766,5.782678,-8.634059,0.726723,-7.539765,-4.674869,-5.538670],[9.139138,6.896238,-4.569754,4.582058,-8.354587,-2.158437,0.124361,-5.399577,5.798662,3.626667,9.427274,-9.471987,4.209247,-0.383871,-9.350469,5.708884],[-0.976623,-9.687946,5.242348,-5.473603,-6.828669,0.639001,-6.716172,4.439357,-7.513074,-2.819691,0.536572,5.772794,-1.468240,-9.898665,-1.869754,-4.473490]],[[6.565623,-2.392602,-7.237202,-6.791828,3.056878,-4.119364,9.634784,4.551350,-8.255034,0.658794,-9.248939,-2.678152,-5.030846,-8.802998,-0.801501,8.636768],[3.726981,-2.477108,-6.944703,-9.628540,3.783000,5.649844,4.523541,-0.813540,4.185138,3.969024,-3.435004,-7.654923,-6.733611,-8.620348,0.282759,-0.278267],[7.345406,-1.448835,1.710516,2.046527,8.648955,8.450316,4.461700,-1.134104,4.558890,7.563219,-9.952900,-9.691817,-4.208907,5.820270,-2.936447,-4.874617],[0.009187,1.807103,-2.159365,3.500970,-6.092245,-6.596976,-3.625680,-8.999234,-2.128151,-7.356108,8.493658,0.097251,8.667647,1.019259,2.959884,4.457560]],[[-9.524767,6.683685,9.702882,-2.905697,-5.514696,4.490424,4.541628,-2.819394,8.516657,-0.175821,-2.730393,-5.280368,7.926934,7.014666,-1.158353,4.204526],[-3.057534,3.604451,2.378451,5.701696,-7.471852,-9.665739,-5.636894,9.201385,5.836080,-8.235064,0.863397,4.773044,-6.408605,1.808825,5.687545,2.275231],[-7.284885,3.406089,-6.823501,2.045717,-9.189126,-0.644405,-6.695484,-9.092672,-1.052612,3.384228,-9.851598,-3.344609,-3.278906,7.893346,-2.548311,5.152043],[6.321991,-1.159119,2.979887,-4.219722,1.220379,-1.243476,-8.984998,-7.213518,3.706232,-7.701104,-0.818943,-7.889978,4.784171,6.782173,-5.090859,-3.051903]],[[3.728341,6.621816,-4.326350,-5.628725,-5.704074,1.350362,-9.483936,3.692408,-0.469794,9.235942,-3.355782,3.605713,7.601643,2.092916,9.201854,8.200753],[-6.987766,4.966258,-9.619874,2.400179,-5.942299,6.312706,-3.837598,-1.556179,-8.733406,4.969873,6.126742,-8.623342,0.881340,-3.418630,2.993226,-8.159043],[-9.799483,-8.409126,2.633658,1.974079,0.421020,-6.320295,-8.157239,-6.778350,-3.322356,2.400027,-2.365875,-0.417326,-2.963192,-6.620505,-2.138031,9.560807],[-2.858383,8.428673,0.660872,4.554094,2.844850,-1.333395,-9.155579,1.159499,1.758154,-2.234488,-2.539977,2.548927,1.646109,9.204801,-0.455379,-1.595678]],[[-9.286947,4.921127,-7.779654,-5.626564,-2.497515,7.493793,8.579083,-4.815092,-9.930978,-1.652847,0.635633,7.768847,4.822812,4.506908,6.394478,-1.981635],[8.328040,-2.463154,-3.149576,-4.226178,6.308966,9.312731,-4.273561,8.645745,-8.552460,3.982223,-1.277585,-2.701885,1.390197,5.137341,8.071128,1.508970],[8.268266,6.912819,-8.762292,2.307428,2.505456,3.139297,-7.215615,-2.600881,-9.279921,-2.650147,-6.792865,1.972291,-4.918209,6.731147,-3.869760,5.269745],[-2.738342,-1.640605,-4.436651,-1.186693,-4.330045,5.603674,1.602256,-1.566118,8.123035,-1.217513,4.834451,-4.167771,-2.757021,-8.781851,-7.865957,8.953208]],[[-0.567344,4.100970,7.670018,-6.522393,4.001940,-5.067204,-1.583940,5.956848,4.306623,2.221968,7.649703,6.700235,5.724682,-6.969043,5.576199,-7.169052],[0.413326,-5.619243,-9.815077,4.584350,-7.543324,-1.093981,-8.225454,-7.997502,2.098955,-9.994087,0.008203,-4.873438,7.090290,-0.169589,-7.320925,-7.259017],[9.263513,-5.181590,-7.065160,2.304904,1.442277,5.783785,0.399935,-1.165950,7.319251,2.106436,-5.435850,-4.823185,8.226258,-7.112374,9.759002,7.218540],[2.316940,-0.070677,1.847761,-9.310317,7.401255,-0.979419,9.227656,2.401461,-6.513405,-9.554406,3.715140,-8.530854,5.935083,-9.168447,-4.338759,6.585444]],[[-6.334079,4.290285,-1.246719,-6.090655,2.230419,-3.852362,1.609157,5.296807,6.403448,-9.303879,-5.676508,4.870192,5.555843,1.055460,8.485721,7.928684],[-4.268993,-9.703269,-2.910640,5.868747,9.170053,5.486338,9.381764,-4.601090,-2.229632,0.829911,-1.086649,-2.590537,4.667564,5.218025,1.489638,-2.458653],[0.260868,-9.320611,1.787415,3.777829,3.497805,-4.520966,7.358952,6.160594,0.724437,2.005947,9.389158,-5.434216,9.522698,-7.382768,-6.976081,-2.812662],[9.595670,-6.748446,-3.736433,6.203360,-6.746211,1.108885,4.233060,2.085965,9.473498,-5.893271,-6.563483,7.324785,-3.569275,-9.753071,-5.696089,-4.719059]],[[8.715218,2.894102,-4.307868,-9.787972,-6.543510,-3.113105,-1.671270,-8.088176,-6.467485,1.974664,6.964316,-3.939641,-0.788368,2.898720,-0.273993,-3.795562],[-1.519554,9.678487,-7.581245,7.140551,0.850738,-0.616459,9.596623,-2.097028,3.782202,-6.940284,-8.455869,-0.091870,-4.101355,-2.893687,9.717900,-0.321051],[-6.225435,-6.257309,4.441787,1.494608,-1.799590,0.891816,-9.985050,8.000511,3.741275,5.820524,1.273048,-9.044527,3.467605,-9.674235,1.169455,-2.230687],[-4.798810,-8.341086,-8.825793,3.950553,-6.350163,-2.385780,-3.949368,-6.739191,1.084388,2.119422,-0.216073,-4.912131,-2.847339,-9.402089,-4.151719,5.865417]],[[-6.167460,-6.353948,8.543372,4.058663,-4.225798,1.250647,0.601119,-7.962295,0.582035,2.381714,4.583014,8.477452,-3.189353,7.310440,-7.954046,-0.336177],[3.659592,2.344328,-3.730554,-5.424145,-4.219936,7.421968,3.287011,-3.853071,5.076823,-9.472816,-4.761787,0.712197,-8.252123,1.186714,4.237392,7.746591],[-8.637451,-6.162599,9.036674,-4.089185,-0.088590,2.914510,9.468649,-3.646635,-8.733416,-4.073333,-2.565905,3.232076,-2.673251,7.123259,-3.617051,-2.130006],[0.372878,4.844528,4.938051,-2.220057,2.242059,-5.955892,8.459771,-8.718575,5.816651,-7.603116,-8.009002,-8.561341,-4.951222,-7.682675,-8.213191,-6.817729]],[[3.699099,-6.286833,2.048232,-8.710168,9.187740,0.212389,3.896819,-9.877079,-6.311154,-6.044661,-9.145069,-7.532292,-5.928822,-5.906331,5.750651,-7.007415],[-4.434815,-9.856283,4.300530,5.361040,6.502780,-2.787576,-8.914421,5.380688,7.774735,4.693195,7.708702,2.194131,-7.679899,-4.347532,-5.089820,8.955892],[-7.217108,-6.224711,-2.414676,-8.741410,-6.959925,6.489368,7.171197,-4.801219,-7.875286,-6.817976,3.845924,-7.595778,4.891873,7.324494,8.316214,9.039954],[-2.223989,-3.244884,8.134385,-5.786489,7.474161,-2.611531,1.815913,7.171882,-5.628233,1.167107,9.712469,7.971977,-1.759565,-0.984795,8.310883,6.150298]],[[2.493231,0.905129,-6.335173,1.265173,0.161232,-2.411949,-7.505249,-7.298335,-8.612781,-1.712055,0.832303,-2.350322,-1.736527,-9.842468,-8.803227,-6.767794],[0.406615,-8.939736,8.714643,5.211755,1.551785,2.212928,2.274389,-9.784030,4.330180,-2.056666,8.053245,3.980422,1.856888,3.077218,2.266609,-3.774230],[9.744403,8.536248,-8.848522,8.468452,-7.312550,3.952033,0.481142,0.210312,-3.667072,1.139957,5.361295,5.153123,-2.812065,-6.797204,-1.742375,-6.758899],[-5.238095,1.221952,-1.410269,-6.428679,4.577873,5.265476,-7.240812,-1.315376,-9.680510,-8.290167,-9.252466,-6.367430,-0.050091,-6.570877,1.751271,6.099735]],[[-8.569872,-0.077802,9.131889,-7.580503,-3.779438,9.898300,-0.279389,7.492943,-7.762020,-4.461875,-2.967936,6.632467,-3.277095,0.295727,2.847098,6.084190],[9.755010,-3.336602,-9.065052,-8.434874,-3.775387,4.916814,3.013500,8.633292,-5.783355,-5.574359,7.412135,-5.217846,1.082530,6.693179,-7.638781,1.890297],[0.042340,-7.834283,-3.702910,-6.754869,0.300048,7.182086,9.037586,-1.133864,1.099980,-3.543656,-2.033925,-9.038621,-9.404834,-2.885854,-6.048923,5.713865],[-3.925870,5.045603,-7.650041,1.762991,-4.484802,-8.974541,-0.308957,7.348224,6.668106,-8.648011,-9.461832,8.208943,-6.339082,4.453601,7.916175,-7.068318]],[[8.094974,-9.399440,-3.211599,0.550634,4.381870,-3.950953,-6.383578,1.071177,6.498499,7.205361,-0.675197,-2.494285,3.618150,1.951476,-1.059965,-2.792836],[1.639814,8.054208,-3.875652,-5.826710,-4.270986,5.198882,7.762141,-9.064950,-7.437669,-5.902231,3.661280,-6.013969,9.114371,4.890916,9.466245,9.195252],[1.378800,-3.703935,9.230554,6.915558,6.076821,-6.250995,1.865908,0.781140,-3.487180,-3.420692,8.838607,-9.585451,-1.979608,-6.648233,8.895542,-7.163926],[1.613195,7.872297,-9.340190,-4.214158,9.046120,-0.524914,-3.985405,2.277700,8.162542,-1.919895,-4.793732,9.744824,-9.557437,-1.943420,8.244929,-3.716207]],[[-4.718391,2.721373,-3.499446,-4.945830,-9.322705,-1.363224,5.377224,-5.024675,6.048756,1.712232,5.878525,-6.412540,-2.480255,-8.001720,-4.609752,-3.855207],[-7.716557,5.020291,-5.333173,-1.467505,-5.387886,6.178018,-4.098743,-2.521259,-9.798034,8.735239,6.481951,9.050677,3.523806,7.033037,1.536515,-7.228725],[-0.280979,-0.517006,6.031790,6.338216,-5.649016,1.679418,-1.172532,-0.230421,7.281073,8.986890,-3.495444,3.520467,-6.778064,1.147329,-0.773882,5.726062],[2.643303,6.000878,-2.512894,-0.511776,1.332989,-7.925036,4.603701,-8.773274,-0.678929,6.874284,4.137348,-7.946355,-6.664949,9.756814,1.151301,5.201723]],[[-9.710418,-0.819768,9.985988,9.104114,-8.698672,7.992506,7.004311,4.219255,0.830309,-9.528447,0.161592,-0.586029,-1.907784,-2.005978,-2.632169,-4.882674],[4.860335,5.402168,1.987405,6.322544,-6.447766,4.661684,5.981055,-9.524140,-8.073489,6.191576,3.518225,5.827304,2.011132,-1.850355,8.566610,-0.456473],[8.445520,0.099422,2.889497,-2.375530,9.089474,9.454223,-2.325717,4.538257,-2.545908,-4.348877,-1.357281,3.081423,-1.450659,5.202987,-0.232868,-0.120607],[-9.060324,-8.891741,-7.120959,1.770340,-9.401834,-7.429593,-0.143872,2.383788,-0.179974,5.694361,9.827515,-3.690638,-9.894903,1.569893,-5.447508,-7.958205]]], dtype = "float64")#candidate|1540|(15, 4, 16)|const|float64
uop_1541 = relay.cosh(const_1540.astype('float64')) # shape=(15, 4, 16)
uop_1557 = relay.asinh(uop_1541.astype('float32')) # shape=(15, 4, 16)
output = relay.Tuple([uop_1557,])
output2 = relay.Tuple([uop_1557,])
func_1580 = relay.Function([], output)
mod['func_1580'] = func_1580
mod = relay.transform.InferType()(mod)
mutated_mod['func_1580'] = func_1580
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1580_call = mutated_mod.get_global_var('func_1580')
call_1581 = func_1580_call()
output = call_1581
func_1582 = relay.Function([], output)
mutated_mod['func_1582'] = func_1582
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1580_call = mod.get_global_var('func_1580')
func_1582_call = mutated_mod.get_global_var('func_1582')
call_1594 = relay.TupleGetItem(func_1580_call(), 0)
call_1595 = relay.TupleGetItem(func_1582_call(), 0)
output = relay.Tuple([call_1594,])
output2 = relay.Tuple([call_1595,])
func_1598 = relay.Function([], output)
mod['func_1598'] = func_1598
mod = relay.transform.InferType()(mod)
output = func_1598()
func_1599 = relay.Function([], output)
mutated_mod['func_1599'] = func_1599
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1249_call = mod.get_global_var('func_1249')
func_1251_call = mutated_mod.get_global_var('func_1251')
call_1628 = relay.TupleGetItem(func_1249_call(), 0)
call_1629 = relay.TupleGetItem(func_1251_call(), 0)
output = call_1628
output2 = call_1629
func_1654 = relay.Function([], output)
mod['func_1654'] = func_1654
mod = relay.transform.InferType()(mod)
mutated_mod['func_1654'] = func_1654
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1654_call = mutated_mod.get_global_var('func_1654')
call_1655 = func_1654_call()
output = call_1655
func_1656 = relay.Function([], output)
mutated_mod['func_1656'] = func_1656
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1598_call = mod.get_global_var('func_1598')
func_1599_call = mutated_mod.get_global_var('func_1599')
call_1738 = relay.TupleGetItem(func_1598_call(), 0)
call_1739 = relay.TupleGetItem(func_1599_call(), 0)
output = call_1738
output2 = call_1739
func_1747 = relay.Function([], output)
mod['func_1747'] = func_1747
mod = relay.transform.InferType()(mod)
output = func_1747()
func_1748 = relay.Function([], output)
mutated_mod['func_1748'] = func_1748
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1654_call = mod.get_global_var('func_1654')
func_1656_call = mutated_mod.get_global_var('func_1656')
call_1780 = func_1654_call()
call_1781 = func_1654_call()
uop_1813 = relay.asin(call_1780.astype('float32')) # shape=(10, 2, 14)
uop_1815 = relay.asin(call_1781.astype('float32')) # shape=(10, 2, 14)
uop_1817 = relay.rsqrt(uop_1813.astype('float32')) # shape=(10, 2, 14)
uop_1819 = relay.rsqrt(uop_1815.astype('float32')) # shape=(10, 2, 14)
func_292_call = mod.get_global_var('func_292')
func_294_call = mutated_mod.get_global_var('func_294')
const_1823 = relay.const([2.875771,3.281611,1.382246,6.516654,1.770433,-7.457371,-2.817761,-6.881914,9.313425,1.406264,9.058873,-5.642841,-7.531233,4.824657,8.901788,-6.886062,1.555221,9.202693,7.894781,-1.262230,-6.691065,-0.305149,4.155724,-6.673565,-6.887285,4.885135,9.935348,8.479452,4.684249,-1.861313,6.735625,-7.125730,-6.224711,4.599518,-1.606835,-0.329023,3.078147,1.914013,-9.034111,9.664799,1.397477,-5.733669], dtype = "float64")#candidate|1823|(42,)|const|float64
call_1822 = relay.TupleGetItem(func_292_call(relay.reshape(const_1823.astype('float64'), [2, 7, 3])), 0)
call_1824 = relay.TupleGetItem(func_294_call(relay.reshape(const_1823.astype('float64'), [2, 7, 3])), 0)
func_961_call = mod.get_global_var('func_961')
func_964_call = mutated_mod.get_global_var('func_964')
var_1832 = relay.var("var_1832", dtype = "float64", shape = (330,))#candidate|1832|(330,)|var|float64
const_1833 = relay.const([-1.088313,-1.512934,1.984522,-5.210906,-5.882016,6.069262,2.254653,9.630969,-8.691884,6.333915,2.490679,7.078426,0.311349,-4.019337,9.746574,4.175011,-9.358442,-0.474629,-6.920701,-8.264785,0.160038,-5.697134,8.667384,-5.862195,8.829644,4.005143,-2.880893,2.435059,-6.711164,-0.499014,4.778829,-7.214669,-8.203649,9.734738,6.006159,1.800483,8.209703,-8.124982,-8.219220,-9.660647,-4.304308,-8.542871,-5.188974,-2.116812,2.720750,-7.965118,-0.111285,6.066065,4.461735,7.973380,-7.895502,4.545307,-5.905116,-5.710094,5.429091,5.625127,4.784617,-2.097871,2.089864,-9.312215,9.137313,7.239267,2.256805,-8.234324,0.538428,-2.761778,8.590895,8.540620,2.155970,-3.714295,9.035222,-3.464963,0.133795,-7.764698,9.386631,8.610802,-1.400347,6.521558,7.759594,-0.766691,6.932748,8.187884,0.512903,7.622426,-5.428975,0.309199,0.588729,-0.383833,-0.063185,8.788497,-4.118271,-5.734301,4.530786,-4.690472,-3.690373,3.487905,2.315077,-1.727949,9.481542,4.831141,2.166426,5.496699,-0.014791,1.475922,1.794759,1.804297,5.388203,-4.089605,3.152520,-7.689356,6.078440,3.642344,-6.823134,5.955524,1.515134,1.199429,0.851023,4.619394,3.236318,-4.261857,0.791021,-9.446619,-6.201021,0.994108,7.073322,0.852229,9.764368,-0.112915,-3.503902,-7.784411,-3.839877,-2.321818,-6.408822,-7.215441,-4.348441,-0.547474,-0.345552,-1.530761,9.428875,-5.000096,3.452276,-2.127681,-2.850193,-9.386939,-7.559281,6.573775,9.132672,1.950068,4.668302,9.298883,-0.355313,-3.792715,-5.480757,8.575178,-6.079203,-8.358326,6.094470,7.745992,7.052974,-4.419718,-5.730744,8.826879,9.666083,0.335783,-7.270132,-0.678998,2.565673,3.547154,-9.314788,0.614969,-4.088725,-6.382861,-1.360129,7.768081,-3.165563,-8.874103,0.406802,-3.021920,-5.761353,-8.477401,-3.917474,4.586169,5.427248,2.899226,-7.722189,-4.689257,-2.783312,-7.738658,-9.998709,4.357564,-3.994925,6.747198,3.940938,-2.762422,-1.176864,-0.077584,-5.559571,-6.934836,-2.884045,9.820087,-2.061590,0.381143,-6.844978,-3.920479,2.194038,9.554923,2.792436,-8.470952,-8.695730,-9.924035,0.506475,7.698449,-5.998954,4.866774,7.429548,4.445966,-9.089980,7.194056,7.497476,-9.730349,1.068426,-7.035460,-5.348130,2.433847,6.488607,9.960725,-1.469814,-6.894520,-8.510976,4.333526,-8.540268,-7.319801,8.892552,-3.500455,1.276808,2.370549,-0.255264,3.334405,-3.519197,-0.299402,-7.162403,-5.103185,-7.093978,3.940380,-5.911009,8.624654,-4.880204,-0.559781,3.577633,-5.860032,6.051720,5.204843,3.626664,-3.669198,2.997805,6.305662,9.740876,-0.292677,1.415540,-0.477960,-7.038332,-0.054189,1.803269,-9.531128,5.031731,8.689458,-0.024734,9.920538,1.801417,-8.992653,-4.823137,-5.573034,1.482281,0.345047,3.261584,3.275879,0.014861,-3.439833,-0.541337,1.658428,4.862519,-9.279217,6.462706,9.873035,6.286968,5.107588,7.685750,1.750791,-8.320674,2.581703,1.657934,2.256467,9.975699,7.355535,-0.062542,2.575627,-0.258108,-6.253585,6.325029,-7.402018,4.013482,-1.433178,-1.570232,6.962724,6.528152,-2.177082,7.952380,8.473097,5.453406,-8.173726,-1.337631,2.454308,4.557725,-6.468791,4.831884,-6.751852,2.247931,5.461078,-4.977289,-4.229083,-1.702014,-3.597767,6.609054,-8.206117,9.541155,-0.420177,-5.408027,-8.488963,1.156709,6.913183,0.692415,3.889114,-9.157925,-5.519451,-7.313190,-0.151103,5.759393,-2.321053,1.442837,7.478397,-0.590718,-2.996216,7.745101,-7.849463,8.923530,0.585467,1.891767,4.973234,-2.994645,4.586916,4.352400,2.838951,-1.739564,3.208141,-9.682342,-4.156290,-5.301509,3.635897,1.520745,0.930417,6.687878,-5.356217,4.178515,8.871494,5.654549,-9.037647,-1.111259,-3.766098,-8.905126,-8.430272,-2.706845,8.309618,5.532910,6.967293,-2.147792,-1.457344,4.592484,0.796128,-7.236334,-1.318655,2.215175,-5.326662,-2.399318,-6.294177,-7.864504,1.784663,-2.033275,-9.477145,-9.325214,-4.226129,-7.360735,-2.979368,5.641550,-7.181932,-1.881388,-2.974895,-2.193885,-5.156779,7.478762,2.770589,3.337958,-6.631334,2.433799,-9.383207,-1.833889,-7.709002,2.237773,8.517964,-0.212680,-4.770414,-6.797732,-4.033663,-4.102631,-7.604853,-0.856387,4.395879,-1.688560,8.430806,-2.118532,6.960107,-6.018833,8.959451,8.020769,4.785942,3.632991,-7.261241,-2.711090,-3.572382,6.378045,-2.220941,-4.829886,-8.051692,8.078032,-3.682683,5.902660,8.785547,2.112915,7.040382,5.077328,9.414031,-6.260844], dtype = "float32")#candidate|1833|(441,)|const|float32
call_1831 = relay.TupleGetItem(func_961_call(relay.reshape(var_1832.astype('float64'), [15, 2, 11]), relay.reshape(const_1833.astype('float32'), [441,]), ), 3)
call_1834 = relay.TupleGetItem(func_964_call(relay.reshape(var_1832.astype('float64'), [15, 2, 11]), relay.reshape(const_1833.astype('float32'), [441,]), ), 3)
bop_1837 = relay.power(uop_1817.astype('float64'), relay.reshape(uop_1813.astype('float64'), relay.shape_of(uop_1817))) # shape=(10, 2, 14)
bop_1840 = relay.power(uop_1819.astype('float64'), relay.reshape(uop_1815.astype('float64'), relay.shape_of(uop_1819))) # shape=(10, 2, 14)
output = relay.Tuple([call_1822,const_1823,call_1831,var_1832,const_1833,bop_1837,])
output2 = relay.Tuple([call_1824,const_1823,call_1834,var_1832,const_1833,bop_1840,])
func_1848 = relay.Function([var_1832,], output)
mod['func_1848'] = func_1848
mod = relay.transform.InferType()(mod)
var_1849 = relay.var("var_1849", dtype = "float64", shape = (330,))#candidate|1849|(330,)|var|float64
output = func_1848(var_1849)
func_1850 = relay.Function([var_1849], output)
mutated_mod['func_1850'] = func_1850
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1747_call = mod.get_global_var('func_1747')
func_1748_call = mutated_mod.get_global_var('func_1748')
call_1878 = func_1747_call()
call_1879 = func_1747_call()
func_564_call = mod.get_global_var('func_564')
func_567_call = mutated_mod.get_global_var('func_567')
const_1881 = relay.const([4.221655,-7.776263,1.066459,-6.848447,9.997000,2.784806,1.664241,9.572605,7.241850,-1.972772,-6.997583,-7.436655,-6.211668,-2.339650,4.312265,-8.624543,-1.942884,2.732323,-7.782849,0.979087,0.581109,2.647133,-5.319459,4.055456,5.884752,9.269778,-1.279438,6.787497,-8.662774,8.727928,0.873111,3.184959,-3.073963,6.132325,-0.721926,3.369482,4.426039,-7.898802,1.464005,9.078275,-6.054717,3.970967,0.103170,6.245708,-3.926501,5.723190,-0.996553,4.463174,3.288585,2.927493,3.298149,-5.159251,-5.048511,-8.266565,-8.324676,-2.651204,3.121283,3.050714,-1.455959,-3.192804,7.258286,1.785979,-5.382547,1.142156,7.999740,5.303057,2.928545,-9.582238,5.138346,2.431424,-2.237748,-4.352172,3.448744,-7.497868,-6.982561,-5.264110,3.273648,-6.243457,-2.691990,9.458438,-8.210369,-3.844273,-7.141164,3.361721,-5.115308,2.047265,7.562160,-5.127374,-8.649997,-5.947205,2.781858,-8.557970,-5.841274,3.565573,-5.623753,5.718167,9.457174,-9.078638,-0.931524,9.874465,5.421111,6.934261,-6.357875,5.362224,7.762053,-3.136331,7.407948,9.938030,9.352269,-8.992659,2.854646,-6.045906,-1.945239,8.377636,6.742073,5.910933,9.955717,0.398276,-3.335609,-7.383534,-1.932338,-8.561099,-1.383540,-9.272265,-8.956093,5.639660,-6.783071,7.329787,7.755525,0.812685,1.858255,2.364865,9.135997,0.420987,4.395744,6.152920,-3.247063,2.013357,0.282696,-2.336359,3.369471,-5.182015,3.735736,-5.729613,-0.948401,0.948800,-4.086071,-5.020625,0.019969,0.971253,-7.680582,0.589302,-5.564017,8.018157,-6.066720,-5.338738,6.301775,9.220611,-4.996596,4.325481,0.678909,-2.010226,8.125601,3.830699,-6.803903,-6.442494,-3.675589,2.328891,-3.096595,-0.161919,-0.693784,-8.951321,3.636655,1.618862,7.977985,-4.407781,6.025764,-2.768022,-2.861390,-1.826463,-1.490960,5.603086,-0.636820,-9.498757,5.572901,0.716554,8.831523,2.062763,4.122446,-1.446728,-7.649388,9.617866,8.850649,-6.045099,7.922345,8.482471,0.576427,-5.548520,2.029965,3.570741,-3.904935,9.327333,-0.057519,-7.101716,1.050314,6.529438,-3.477415,7.639200,-3.167758,0.274016,-9.436408,-9.002375,3.393499,8.535908,6.122681,4.261311,5.766841,1.020667,3.212387,7.780971,-4.558861,-0.941713,0.862061,-2.882050,-7.602788,-2.222597,-9.871418,-3.456927,0.494420,3.372241,-4.342377,-3.570536,5.141330,-2.135387,-2.580279,7.889764,-1.876641,3.838020,0.619643,7.781415,8.240691,2.933615,-6.613352,2.163491,4.849739,-5.317636,2.581824,-6.754799,-6.027645,1.304416,-9.888030,3.186568,4.311370,2.302391,7.781088,-5.336854,-2.307372,-7.536883,0.227010,-7.395728,-8.538820,2.196255,-9.481184,-7.236189,-4.489613,5.776340,-1.900743,6.988592,7.020162,5.117609,2.944348,8.239429,3.565066,5.933812,9.270933,6.820802,-2.663554,0.707156,-6.127687,-3.371683,6.115665,-0.543036,-8.184723,2.554104,-6.331818,-4.114227,-4.198271,0.121622,-2.495642,4.491098,-1.103357,7.562326,0.051657,8.109027,4.924569,-2.794064,7.738846,-1.053324,-3.720066,6.345222,-5.774186,-3.002727,2.189668,-4.940754,-7.940366,6.821370,5.696605,-2.395139,6.162052,-9.305964,1.004510,-4.323394,6.399357,-6.283451,-2.868424,-7.176160,-6.153569,-1.973073,-9.643026,6.717869,-8.946279,-8.866866,1.034710,-1.856840,-9.524565,7.077980,2.586729,2.059144,7.432935,-9.283399,9.404033,-6.333997,9.258359,-3.820312,-5.631058,7.026299,-7.771747,-1.073337,-2.217941,1.035109,1.876901,-1.038055,-5.913143,-6.813721,1.670791,3.412131,2.212514,-0.950901,-9.248149,2.735536,-1.176592,1.722270,-7.998685,2.965049,-6.145038,5.653838,3.409735,-1.525299,7.555632,6.755349,8.008989,-3.616139,4.395160,-2.593593,6.093852,-6.567937,-4.165266,-0.217153,1.915665,9.874244,-0.362841,3.476641,-0.285322,3.296505,-8.941761,-6.434571,-9.756951,6.089603,-8.271449,9.109354,6.204902,6.451450,-5.046792,-2.632279,7.529749,1.720600,-7.510794,-3.772821,8.498623,1.717406,-2.747906,3.498705,-3.880431,-3.592605,-7.745069,-6.336714,9.098306,9.039435,3.867027,1.618246,9.143003,6.214322,-4.951161,-6.597646,1.550053,9.075812,-3.438199,-0.240154,0.362394,6.320198,2.967696,5.618258,9.031400,-8.223000,-7.134132,-8.587044,-2.358140,-2.914874,3.634636,-0.870263,-2.032378,-7.122796,9.037511,4.869367,-0.621681,-7.752211,-2.819121,-5.255281,3.598806,-4.064420,3.787288,6.287681,-5.703244,-3.419026,6.416883,0.645007,-1.440387,-6.051634,-9.721226,0.721622,-2.624787,-4.645825,7.469016,-4.388185,0.607391,7.481179,3.826694,2.509596,-4.954604,9.020532,-3.150510,1.770113,9.346167,-7.562889,3.175279,-6.020875,-5.703015,-0.131611,7.749180,-3.225643,1.687648,8.145420,-9.331018,5.991774,-3.081419,-1.545398,2.326532,-7.005378,4.168439,-7.015714,-2.888199,-8.361398,-5.806721,-9.133613,-6.572755,-8.733524,-3.496843,-8.392493,-3.874461,6.498722,6.369390,-4.354981,3.280606,6.517586,2.714816,2.417013,-4.304322,-4.908819,-4.859534,-8.933538,3.617040,9.712563,7.002138,9.472026,8.902031,-6.452552,-7.078724,8.917113,8.794602,0.715993,-3.288585,-7.768961,-6.583498,2.625157,-1.154904,4.279124,2.088271,1.467124,3.190117,-3.139099,-9.098891,8.086252,2.236899,-1.703638,0.207340,-3.103742,5.174533,-3.090639,3.732302,-7.406660,5.996194,-7.572665,-3.559344,0.876234,-4.011901,-5.966870,2.886009,1.446563,-3.243077,7.264924,0.904098,-4.830934,8.897252,4.895781,-6.788926,-3.407931,9.270829,-7.871762,-8.809761,1.932437,-8.642964,5.718923,2.920600,-8.559450,5.395812,8.546275,4.297445,9.578199,-9.525552,-6.104665,-0.398581,1.332399,5.916915,-2.557899,0.531177,-0.530785,0.427213,9.814443,-8.441750,6.709224,-5.707640,6.058415,-6.563043,-4.696725,1.726192,8.328025,7.135380,4.646189,9.382156,-4.645273,-9.659352,-0.258327,0.509819,-5.936769,4.341360,9.870359,6.690455,-1.791924,8.278920,-2.246855,7.892496,-3.500581,-6.446766,5.659932,9.321219,0.528282,-8.553415,-5.310244,9.187057,1.939041,-9.596488,-5.029962,2.989408,8.823127,9.325469,2.087761,6.696937,7.126839,-7.009978,2.939025,2.146091,9.551672,-8.206562,6.596374,-9.886641,4.656115,9.806710,-8.826995,-9.204017,4.697800,-2.428345,-9.281782,-0.370464,8.385028,-5.362447,3.657052,4.041441,1.326847,-2.261364,-4.283771,4.520708,7.906067,4.964915,-6.268992,1.711525,-8.926478,-3.700767,4.191184,-8.533308,0.221304,-2.025332,-8.378764,6.649997,9.527430,-9.852260,6.740447,7.178168,-3.686986,-4.127420,-7.322432,-8.155391,4.546804,3.840930,-9.813893,-0.312817,-6.623911,-3.020151,-2.124322,-1.028514,0.019896,9.408474,3.604993,8.868606,-1.798530,-5.751136,6.301648,1.818535,9.217447,0.862966,-9.024904,-4.704555,-8.775545,-3.052067,-7.439381,1.962829,3.858062,-2.731815,1.533215,7.248554,-0.594652,0.905301,-1.110576,-3.419323,9.029738,1.727244,9.183637,3.221822,-9.816141,5.387440,-2.387560,-3.988668,0.539645,-2.617249,-8.653045,-9.116982,5.973735,-7.971869,-0.866903,-9.769178,0.903576,-1.122886,6.098135,-8.545456,5.025379,-2.793503,-9.505242,7.438298,-1.152867,8.665128,1.256820,2.716226,4.359634,7.312560,-8.168691,4.101124,5.060070,5.555216,8.160067,2.906117,2.545537,7.226966,-7.885499,2.775437,-9.828744,-1.092917,2.101781,5.158300,9.988870,-4.591785,-8.479628,8.648196,4.518983,-3.245239,6.846687,6.215365,1.727902,-4.467056,-9.175503,-4.832804,-5.565803,-0.279363,-5.324868,-1.723058,-3.739615,-5.990519,6.508923,7.206367,-1.274554,6.816869,4.711653,-7.690469,9.302901,-5.247780,-2.027891,1.079633,1.090928,-5.263200,0.894343,-6.358121,-8.736134,-3.647102,-7.184887,-4.142867,0.358941,-9.242899,3.151154,8.562641,-8.523769,-9.352819,8.158474,6.270752,7.992823,-3.671807,9.058831,5.605914,7.921593,8.856901,3.373366,-8.226275,4.254897,0.912753,6.098218,-6.808874,-0.759082,5.354662,-3.616841,1.789821,-1.181947,-8.524867,-9.494000,5.426174,8.296384,6.151812,9.300144,9.144844,7.761683,2.718476,6.531266,-4.875409,-1.421818,3.467667,-7.503260,-5.377796,9.385036,-7.809047,-9.953112,1.709757,-4.631137,-2.648423,0.434614,0.755225,-5.597104,2.794233,-2.148691,-2.077639,8.457785,3.071696,-6.835193,6.357310,-3.901968,3.867076,0.295729,-5.488167,9.367336,2.613863,-9.160876,5.951040,6.861863,-0.827034,-9.742234,-4.538485,3.001131,-5.259459,-0.426235,8.660384,5.711142,7.843609,2.810305,6.289477,9.141717,3.621245,1.725010,-7.548968,-8.476204,-6.226984,6.253589,-2.682209,-9.315078,-8.915942,-9.663952,7.716494,-0.535787,3.732898,-3.703118,1.615134,3.874092,4.675288,1.766719,-1.550647,-0.675300,8.436110,2.747938,-4.119950,-8.841524,-2.495796,-5.982562,-0.606855,8.781450,1.562510,-9.963591,1.482492,3.343392,-4.709771,-2.608310,-4.431731,3.459851,7.657534,-2.275451,-5.389183,-1.617737,0.349914,-5.422969,-9.369055,3.176415,1.678783,-9.353831,-6.843663,4.363909,-2.802628,3.042057,9.707587,-0.659889,0.500855,-2.746795,6.272988,1.581893,-9.661026,2.081431,3.380132,-2.489036,-5.010029,3.024588,-9.248188,-0.619005,-2.178224,-7.487954,-5.986766,-0.164356,5.327821,-0.365065,-7.223876,9.790948,3.699962,9.873154,-4.100624,-4.535471,-3.188202,8.098364,-9.432216,1.271297,5.727519,-5.356182,2.719584,5.529790,-2.500793,9.472291,6.824663,8.123115,5.534004,6.547943,-8.903468,3.662787,3.902637,1.330626,-2.410621,3.187515,-7.298267,2.956766,-4.238981,-5.822431,-8.426199,1.931803,1.576683,2.920803,5.137722,-4.947007,-1.353222,-7.321990,-6.608500,8.832344,7.796066,-9.103677,7.373484,6.516492,-2.165224,-8.125365,7.483591,8.202178,-3.916393,-8.980987,7.794245,8.352991,-7.290367,-9.335754,3.011057,8.466833,-4.119339,7.595089,7.329864,0.177304,-7.786384,5.573935,-5.633980,-1.103742,0.167015,-8.536280,2.675594,-4.724907,-9.879225,-5.248264,-6.618628,-3.141071,4.519221,-4.919033,-9.717198,7.185018,2.240764,-4.552621,1.074874,-9.442484,9.904249,2.107572,-2.793124,-0.319909,-1.655307,5.500467,-3.365936,8.732660,3.059284,3.441721,-2.039463,-3.677340,8.055821,8.054235,-3.317230,6.764995,-8.052963,-6.173791,-1.891286,3.995112,-2.022297], dtype = "float64")#candidate|1881|(1001,)|const|float64
const_1882 = relay.const([[2.043221,3.638446,-2.762908,2.791208,9.244261,-0.132364],[7.835954,7.275909,5.044234,-9.973411,4.620020,-6.258395],[-9.036248,-9.608394,9.799645,-5.827335,-0.339978,-4.175680],[-7.406211,-0.266228,-4.253366,8.548615,-5.465907,6.308843],[-5.051510,1.054256,-9.240024,2.605907,-3.762898,5.210661],[2.678540,-1.074712,-1.968115,-3.485573,-4.581418,-2.973181],[-9.925221,-0.667974,-1.637912,-3.372390,-0.838245,-1.098347]], dtype = "float64")#candidate|1882|(7, 6)|const|float64
call_1880 = relay.TupleGetItem(func_564_call(relay.reshape(const_1881.astype('float64'), [11, 13, 7]), relay.reshape(const_1882.astype('float64'), [42,]), ), 1)
call_1883 = relay.TupleGetItem(func_567_call(relay.reshape(const_1881.astype('float64'), [11, 13, 7]), relay.reshape(const_1882.astype('float64'), [42,]), ), 1)
output = relay.Tuple([call_1878,call_1880,const_1881,const_1882,])
output2 = relay.Tuple([call_1879,call_1883,const_1881,const_1882,])
func_1905 = relay.Function([], output)
mod['func_1905'] = func_1905
mod = relay.transform.InferType()(mod)
output = func_1905()
func_1906 = relay.Function([], output)
mutated_mod['func_1906'] = func_1906
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1167_call = mod.get_global_var('func_1167')
func_1169_call = mutated_mod.get_global_var('func_1169')
call_1995 = relay.TupleGetItem(func_1167_call(), 0)
call_1996 = relay.TupleGetItem(func_1169_call(), 0)
output = call_1995
output2 = call_1996
func_2014 = relay.Function([], output)
mod['func_2014'] = func_2014
mod = relay.transform.InferType()(mod)
output = func_2014()
func_2015 = relay.Function([], output)
mutated_mod['func_2015'] = func_2015
mutated_mod = relay.transform.InferType()(mutated_mod)
func_442_call = mod.get_global_var('func_442')
func_443_call = mutated_mod.get_global_var('func_443')
call_2101 = relay.TupleGetItem(func_442_call(), 0)
call_2102 = relay.TupleGetItem(func_443_call(), 0)
func_1654_call = mod.get_global_var('func_1654')
func_1656_call = mutated_mod.get_global_var('func_1656')
call_2105 = func_1654_call()
call_2106 = func_1654_call()
output = relay.Tuple([call_2101,call_2105,])
output2 = relay.Tuple([call_2102,call_2106,])
func_2109 = relay.Function([], output)
mod['func_2109'] = func_2109
mod = relay.transform.InferType()(mod)
mutated_mod['func_2109'] = func_2109
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2109_call = mutated_mod.get_global_var('func_2109')
call_2110 = func_2109_call()
output = call_2110
func_2111 = relay.Function([], output)
mutated_mod['func_2111'] = func_2111
mutated_mod = relay.transform.InferType()(mutated_mod)
func_442_call = mod.get_global_var('func_442')
func_443_call = mutated_mod.get_global_var('func_443')
call_2130 = relay.TupleGetItem(func_442_call(), 0)
call_2131 = relay.TupleGetItem(func_443_call(), 0)
func_1461_call = mod.get_global_var('func_1461')
func_1463_call = mutated_mod.get_global_var('func_1463')
call_2170 = func_1461_call()
call_2171 = func_1461_call()
func_1747_call = mod.get_global_var('func_1747')
func_1748_call = mutated_mod.get_global_var('func_1748')
call_2183 = func_1747_call()
call_2184 = func_1747_call()
func_594_call = mod.get_global_var('func_594')
func_597_call = mutated_mod.get_global_var('func_597')
const_2198 = relay.const([1,-6,-4,-9,-6,5,-3,4,-9,1,2,-8,-10,10,-7,-5,-2,5,5,4,-8,1,-6,-5,3,-6,10,9,-2,5,-1,-8,-3,-2,-9,-2,-7,-8,-7,7,-1,-8,-6,-8,8,-8,4,-6,8,-7,-4,4,3,2,5,1,-4,-4,6,9,-7,-2,10,10,-6,5,-8,-9,10,-1,3,-10,9,-7,10,-10,10,10,2,10,-8,7,-5,-7,10,-2,9,9,-10,4,2,-6,8,4,7,7,8,-3,8,10,9,-10,7,-8,-6,6,-8,10,-10,5,8,-5,4,1,-10,-2,4,9,3,-8,-4,9,-7,-8,-3,4,-7,-8,-1,-4,2,1,-10,-7,10,4,-8,-5,-1,-1,10,-8,6,-7,-4,9,-9,-2,-1,-3,-4,6,-9,-6,8,7,-5,-4,-10,10,-1,2,9,8,2,-2,8,8,-3,-10,-4,-8,1,-9,-2,-6,8,-3,-1,7,-2,-10,1,10,4,4,6,-4,3,-9,-6,7,5,1,1,-1,-10,-5,-1,-4,4,3,-9,6,-2,-4,10,-4,-1,2,4,-9,6,-5,1,-2,-7,-5,-1,6,-6,4,4,-2,3,-9,7,3,-3,10,10,-9,8,3,2,5,-2,5,-8,-2,-1,10,-10,1,5,-7,5,2,-7,3,4,9,-8,3,9,7,-10,-8,-1,-6,-2,1,-9,3], dtype = "uint16")#candidate|2198|(264,)|const|uint16
call_2197 = relay.TupleGetItem(func_594_call(relay.reshape(const_2198.astype('uint16'), [12, 2, 11])), 1)
call_2199 = relay.TupleGetItem(func_597_call(relay.reshape(const_2198.astype('uint16'), [12, 2, 11])), 1)
func_2109_call = mod.get_global_var('func_2109')
func_2111_call = mutated_mod.get_global_var('func_2111')
call_2203 = relay.TupleGetItem(func_2109_call(), 0)
call_2204 = relay.TupleGetItem(func_2111_call(), 0)
output = relay.Tuple([call_2130,call_2170,call_2183,call_2197,const_2198,call_2203,])
output2 = relay.Tuple([call_2131,call_2171,call_2184,call_2199,const_2198,call_2204,])
func_2207 = relay.Function([], output)
mod['func_2207'] = func_2207
mod = relay.transform.InferType()(mod)
mutated_mod['func_2207'] = func_2207
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2207_call = mutated_mod.get_global_var('func_2207')
call_2208 = func_2207_call()
output = call_2208
func_2209 = relay.Function([], output)
mutated_mod['func_2209'] = func_2209
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1747_call = mod.get_global_var('func_1747')
func_1748_call = mutated_mod.get_global_var('func_1748')
call_2213 = func_1747_call()
call_2214 = func_1747_call()
var_2227 = relay.var("var_2227", dtype = "float32", shape = (15, 4, 16))#candidate|2227|(15, 4, 16)|var|float32
bop_2228 = relay.logical_or(call_2213.astype('bool'), relay.reshape(var_2227.astype('bool'), relay.shape_of(call_2213))) # shape=(15, 4, 16)
bop_2231 = relay.logical_or(call_2214.astype('bool'), relay.reshape(var_2227.astype('bool'), relay.shape_of(call_2214))) # shape=(15, 4, 16)
output = bop_2228
output2 = bop_2231
func_2236 = relay.Function([var_2227,], output)
mod['func_2236'] = func_2236
mod = relay.transform.InferType()(mod)
mutated_mod['func_2236'] = func_2236
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2237 = relay.var("var_2237", dtype = "float32", shape = (15, 4, 16))#candidate|2237|(15, 4, 16)|var|float32
func_2236_call = mutated_mod.get_global_var('func_2236')
call_2238 = func_2236_call(var_2237)
output = call_2238
func_2239 = relay.Function([var_2237], output)
mutated_mod['func_2239'] = func_2239
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1598_call = mod.get_global_var('func_1598')
func_1599_call = mutated_mod.get_global_var('func_1599')
call_2266 = relay.TupleGetItem(func_1598_call(), 0)
call_2267 = relay.TupleGetItem(func_1599_call(), 0)
func_1580_call = mod.get_global_var('func_1580')
func_1582_call = mutated_mod.get_global_var('func_1582')
call_2297 = relay.TupleGetItem(func_1580_call(), 0)
call_2298 = relay.TupleGetItem(func_1582_call(), 0)
var_2329 = relay.var("var_2329", dtype = "float32", shape = (15, 4, 16))#candidate|2329|(15, 4, 16)|var|float32
bop_2330 = relay.greater(call_2266.astype('bool'), relay.reshape(var_2329.astype('bool'), relay.shape_of(call_2266))) # shape=(15, 4, 16)
bop_2333 = relay.greater(call_2267.astype('bool'), relay.reshape(var_2329.astype('bool'), relay.shape_of(call_2267))) # shape=(15, 4, 16)
uop_2341 = relay.asin(call_2266.astype('float32')) # shape=(15, 4, 16)
uop_2343 = relay.asin(call_2267.astype('float32')) # shape=(15, 4, 16)
output = relay.Tuple([call_2297,bop_2330,uop_2341,])
output2 = relay.Tuple([call_2298,bop_2333,uop_2343,])
func_2344 = relay.Function([var_2329,], output)
mod['func_2344'] = func_2344
mod = relay.transform.InferType()(mod)
mutated_mod['func_2344'] = func_2344
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2345 = relay.var("var_2345", dtype = "float32", shape = (15, 4, 16))#candidate|2345|(15, 4, 16)|var|float32
func_2344_call = mutated_mod.get_global_var('func_2344')
call_2346 = func_2344_call(var_2345)
output = call_2346
func_2347 = relay.Function([var_2345], output)
mutated_mod['func_2347'] = func_2347
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1598_call = mod.get_global_var('func_1598')
func_1599_call = mutated_mod.get_global_var('func_1599')
call_2349 = relay.TupleGetItem(func_1598_call(), 0)
call_2350 = relay.TupleGetItem(func_1599_call(), 0)
func_1285_call = mod.get_global_var('func_1285')
func_1288_call = mutated_mod.get_global_var('func_1288')
var_2352 = relay.var("var_2352", dtype = "bool", shape = (91, 11))#candidate|2352|(91, 11)|var|bool
call_2351 = relay.TupleGetItem(func_1285_call(relay.reshape(var_2352.astype('bool'), [11, 13, 7]), relay.reshape(var_2352.astype('bool'), [11, 13, 7]), ), 1)
call_2353 = relay.TupleGetItem(func_1288_call(relay.reshape(var_2352.astype('bool'), [11, 13, 7]), relay.reshape(var_2352.astype('bool'), [11, 13, 7]), ), 1)
output = relay.Tuple([call_2349,call_2351,var_2352,])
output2 = relay.Tuple([call_2350,call_2353,var_2352,])
func_2357 = relay.Function([var_2352,], output)
mod['func_2357'] = func_2357
mod = relay.transform.InferType()(mod)
mutated_mod['func_2357'] = func_2357
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2358 = relay.var("var_2358", dtype = "bool", shape = (91, 11))#candidate|2358|(91, 11)|var|bool
func_2357_call = mutated_mod.get_global_var('func_2357')
call_2359 = func_2357_call(var_2358)
output = call_2359
func_2360 = relay.Function([var_2358], output)
mutated_mod['func_2360'] = func_2360
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2207_call = mod.get_global_var('func_2207')
func_2209_call = mutated_mod.get_global_var('func_2209')
call_2375 = relay.TupleGetItem(func_2207_call(), 2)
call_2376 = relay.TupleGetItem(func_2209_call(), 2)
output = relay.Tuple([call_2375,])
output2 = relay.Tuple([call_2376,])
func_2378 = relay.Function([], output)
mod['func_2378'] = func_2378
mod = relay.transform.InferType()(mod)
mutated_mod['func_2378'] = func_2378
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2378_call = mutated_mod.get_global_var('func_2378')
call_2379 = func_2378_call()
output = call_2379
func_2380 = relay.Function([], output)
mutated_mod['func_2380'] = func_2380
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2378_call = mod.get_global_var('func_2378')
func_2380_call = mutated_mod.get_global_var('func_2380')
call_2388 = relay.TupleGetItem(func_2378_call(), 0)
call_2389 = relay.TupleGetItem(func_2380_call(), 0)
output = call_2388
output2 = call_2389
func_2395 = relay.Function([], output)
mod['func_2395'] = func_2395
mod = relay.transform.InferType()(mod)
mutated_mod['func_2395'] = func_2395
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2395_call = mutated_mod.get_global_var('func_2395')
call_2396 = func_2395_call()
output = call_2396
func_2397 = relay.Function([], output)
mutated_mod['func_2397'] = func_2397
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1580_call = mod.get_global_var('func_1580')
func_1582_call = mutated_mod.get_global_var('func_1582')
call_2401 = relay.TupleGetItem(func_1580_call(), 0)
call_2402 = relay.TupleGetItem(func_1582_call(), 0)
output = relay.Tuple([call_2401,])
output2 = relay.Tuple([call_2402,])
func_2412 = relay.Function([], output)
mod['func_2412'] = func_2412
mod = relay.transform.InferType()(mod)
mutated_mod['func_2412'] = func_2412
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2412_call = mutated_mod.get_global_var('func_2412')
call_2413 = func_2412_call()
output = call_2413
func_2414 = relay.Function([], output)
mutated_mod['func_2414'] = func_2414
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2428 = relay.var("var_2428", dtype = "uint8", shape = (8, 14, 2))#candidate|2428|(8, 14, 2)|var|uint8
var_2429 = relay.var("var_2429", dtype = "uint8", shape = (8, 14, 2))#candidate|2429|(8, 14, 2)|var|uint8
bop_2430 = relay.bitwise_xor(var_2428.astype('uint8'), relay.reshape(var_2429.astype('uint8'), relay.shape_of(var_2428))) # shape=(8, 14, 2)
func_1285_call = mod.get_global_var('func_1285')
func_1288_call = mutated_mod.get_global_var('func_1288')
var_2455 = relay.var("var_2455", dtype = "bool", shape = (13, 77))#candidate|2455|(13, 77)|var|bool
call_2454 = relay.TupleGetItem(func_1285_call(relay.reshape(var_2455.astype('bool'), [11, 13, 7]), relay.reshape(var_2455.astype('bool'), [11, 13, 7]), ), 1)
call_2456 = relay.TupleGetItem(func_1288_call(relay.reshape(var_2455.astype('bool'), [11, 13, 7]), relay.reshape(var_2455.astype('bool'), [11, 13, 7]), ), 1)
uop_2484 = relay.acosh(var_2429.astype('float32')) # shape=(8, 14, 2)
func_2207_call = mod.get_global_var('func_2207')
func_2209_call = mutated_mod.get_global_var('func_2209')
call_2513 = relay.TupleGetItem(func_2207_call(), 3)
call_2514 = relay.TupleGetItem(func_2209_call(), 3)
output = relay.Tuple([bop_2430,call_2454,var_2455,uop_2484,call_2513,])
output2 = relay.Tuple([bop_2430,call_2456,var_2455,uop_2484,call_2514,])
func_2519 = relay.Function([var_2428,var_2429,var_2455,], output)
mod['func_2519'] = func_2519
mod = relay.transform.InferType()(mod)
var_2520 = relay.var("var_2520", dtype = "uint8", shape = (8, 14, 2))#candidate|2520|(8, 14, 2)|var|uint8
var_2521 = relay.var("var_2521", dtype = "uint8", shape = (8, 14, 2))#candidate|2521|(8, 14, 2)|var|uint8
var_2522 = relay.var("var_2522", dtype = "bool", shape = (13, 77))#candidate|2522|(13, 77)|var|bool
output = func_2519(var_2520,var_2521,var_2522,)
func_2523 = relay.Function([var_2520,var_2521,var_2522,], output)
mutated_mod['func_2523'] = func_2523
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1249_call = mod.get_global_var('func_1249')
func_1251_call = mutated_mod.get_global_var('func_1251')
call_2606 = relay.TupleGetItem(func_1249_call(), 0)
call_2607 = relay.TupleGetItem(func_1251_call(), 0)
uop_2615 = relay.tan(call_2606.astype('float64')) # shape=(10, 2, 14)
uop_2617 = relay.tan(call_2607.astype('float64')) # shape=(10, 2, 14)
func_1249_call = mod.get_global_var('func_1249')
func_1251_call = mutated_mod.get_global_var('func_1251')
call_2625 = relay.TupleGetItem(func_1249_call(), 0)
call_2626 = relay.TupleGetItem(func_1251_call(), 0)
func_708_call = mod.get_global_var('func_708')
func_711_call = mutated_mod.get_global_var('func_711')
const_2634 = relay.const([True,True,True,True,True,False,False,False,False,True,False,False,False,True,True,False,False,False,True,False,True,False,False,False,True,True,True,True,False,False,True,False,True,True,True,True,True,True,True,True,True,False,True,True,True,False,False,True,False,True,True,True,False,True,True,True,False,True,False,True,True,True,True,False,False,False,True,True,False,True,True,True,True,False,False,False,True,False,True,True,False,True,True,False,False,False,True,True,True,True,False,False,False,True,True,True,True,False,False,True,True,True,False,False,False,True,False,True,True,False,False,True,True,True,True,True,False,False,False,True,True,False,False,False,True,True,True,True,True,True,False,True,True,True,True,True,False,False,False,True,False,False,True,True,False,False,False,False,True,True,True,False,True,True,False,True,False,True,False,False,True,False,True,False,True,False,True,True,False,True,True,False,True,False,True,True,False,False,True,True,True,True,False,False,False,False,True,True,False,True,True,True,False,False,True,True,False,False,True,True,True,False,True,False,False,True,False,False,True,True,False,False,False,False,False,True,False,False,False,False,True,True,True,True,True,False,True,True,False,False,False,True,False,False,False,False,True,False,False,False,True,False,False,False,False,False,True,True,False,True,True,False,False,True,True,True,True,False,False,False,False,True,True,False,True,True,False,False,True,True,False,True,True,False,True,False,False,False,True,True,True,False,True,True,True,False,False,True,True,False,True,True,True,False,False,False,False,False,False,True,True,False,False,True,False,True,True,True,True,False,False,False,False,True,True,False,True,True,True,False,False,False,False,True,False,False,False,False,False,False,False,False,True,False,True,True,False,False,False,True,False,False,False,False,True,True,False,True,True,True,True,True,True,True,False,False,True,False,False,False,True,False,False,False,True,True,True,True,True,False,False,True,False,False,True,False,False,False,True,True,True,False,False,True,False,False,True,True,True,True,True,False,False,True,False,True,False,True,False,True,True,False,False,False,True,False,False,True,False,True,False,True,True,False,False,True,False,True,True,True,True,False,True,True,False,True,False,False,True,False,False,False,False,False,False,True,False,False,False,False,True,False,False,True,False,False,False,True,False,True,False,True,False,False,False,False,True,False,False,False,False,False,True,False,True,True,False,True,False,False,False,True,True,False,False,True,False,True,False,False,False,True,True,False,True,True,False,False,True,True,True,True,True,False,False,False,True,False,False,True,False,False,True,True,False,True,True,False,False,True,True,True,False,False,True,True,False,False,False,True,True,True,True,False,True,True,True,False,True,True,False,True,True,True,True,True,False,False,True,True,True,False,False,False,True,True,True,True,True,True,False,False,False,True,True,True,False,False,False,True,True,False,True,False,True,False,True,True,False,False,False,True,True,False,True,False,False,True,True,True,False,True,False,True,True,True,False,True,True,False,True,False,False,False,False,True,False,True,True,False,True,True,True,False,False,True,False,False,False,True,True,False,True,True,True,False,False,False,True,True,False,False,True,True,False,True,False,False,False,True,False,False,True,False,False,True,True,True,True,True,False,False,True,True,False,True,True,False,True,True,False,True,True,True,False,False,True,True,False,True,False,True,True,True,True,False,False,False,True,True,True,True,False,False,True,False,True,False,False,False,True,False,False,True,False,False,True,True,True,True,False,False,False,False,True,True,False,False,True,True,True,False,False,True,True,True,True,False,False,False,True,True,False,True,False,False,True,True,True,True,True,False,True,True,False,False,True,False,False,False,True,False,True,True,True,False,True,True,False,True,True,True,False,True,False,True,False,False,False,True,True,True,True,False,True,True,False,False,True,True,False,False,True,True,False,False,True,True,True,False,False,False,True,False,False,False,True,False,False,False,True,True,True,True,True,False,False,True,False,False,False,True,False,True,False,False,False,False,True,True,False,True,False,True,False,False,True,True,False,True,True,True,False,True,False,True,True,True,True,False,True,True,True,True,True,True,False,True,True,True,False,True,True,False,True,True,False,False,False,False,False,False,False,False,True,False,False,False,True,True,False,False,False,True,False,True,True,False,False,False,True,True,False,False,True,True,True,False,True,False,False,True,False,False,False,True,True,False,True,False,True,False,True,True,True,True,True,False,True,True,True,False,False,True,True,False,False,False,False,True,False,False,True,False,True,True,True,False,True,True,False,False,True,True,True,False,False,False,True,True,False,False,False,False,True,True,False,True,True,False,False,False,True,True,False,False,False,False,False,True,True,False,True,False,False,True,False,False,True,True,False,True,True,False,False,False,True,False,True,False,True,False,False,False,True,True,False,False,True,False,True,False,False,True,False,False,False,False,True,True,False,True,True,True,True,True,False,False,True,True,False,False,True,True,False,True,False,False,True,True,False], dtype = "bool")#candidate|2634|(1001,)|const|bool
call_2633 = relay.TupleGetItem(func_708_call(relay.reshape(const_2634.astype('bool'), [11, 13, 7])), 0)
call_2635 = relay.TupleGetItem(func_711_call(relay.reshape(const_2634.astype('bool'), [11, 13, 7])), 0)
func_2378_call = mod.get_global_var('func_2378')
func_2380_call = mutated_mod.get_global_var('func_2380')
call_2641 = relay.TupleGetItem(func_2378_call(), 0)
call_2642 = relay.TupleGetItem(func_2380_call(), 0)
uop_2645 = relay.asinh(call_2625.astype('float64')) # shape=(10, 2, 14)
uop_2647 = relay.asinh(call_2626.astype('float64')) # shape=(10, 2, 14)
output = relay.Tuple([uop_2615,call_2633,const_2634,call_2641,uop_2645,])
output2 = relay.Tuple([uop_2617,call_2635,const_2634,call_2642,uop_2647,])
func_2648 = relay.Function([], output)
mod['func_2648'] = func_2648
mod = relay.transform.InferType()(mod)
output = func_2648()
func_2649 = relay.Function([], output)
mutated_mod['func_2649'] = func_2649
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1412_call = mod.get_global_var('func_1412')
func_1414_call = mutated_mod.get_global_var('func_1414')
call_2656 = relay.TupleGetItem(func_1412_call(), 0)
call_2657 = relay.TupleGetItem(func_1414_call(), 0)
func_1654_call = mod.get_global_var('func_1654')
func_1656_call = mutated_mod.get_global_var('func_1656')
call_2663 = func_1654_call()
call_2664 = func_1654_call()
output = relay.Tuple([call_2656,call_2663,])
output2 = relay.Tuple([call_2657,call_2664,])
func_2680 = relay.Function([], output)
mod['func_2680'] = func_2680
mod = relay.transform.InferType()(mod)
output = func_2680()
func_2681 = relay.Function([], output)
mutated_mod['func_2681'] = func_2681
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1598_call = mod.get_global_var('func_1598')
func_1599_call = mutated_mod.get_global_var('func_1599')
call_2682 = relay.TupleGetItem(func_1598_call(), 0)
call_2683 = relay.TupleGetItem(func_1599_call(), 0)
func_1435_call = mod.get_global_var('func_1435')
func_1436_call = mutated_mod.get_global_var('func_1436')
call_2721 = func_1435_call()
call_2722 = func_1435_call()
func_1034_call = mod.get_global_var('func_1034')
func_1035_call = mutated_mod.get_global_var('func_1035')
call_2736 = relay.TupleGetItem(func_1034_call(), 0)
call_2737 = relay.TupleGetItem(func_1035_call(), 0)
output = relay.Tuple([call_2682,call_2721,call_2736,])
output2 = relay.Tuple([call_2683,call_2722,call_2737,])
func_2759 = relay.Function([], output)
mod['func_2759'] = func_2759
mod = relay.transform.InferType()(mod)
mutated_mod['func_2759'] = func_2759
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2759_call = mutated_mod.get_global_var('func_2759')
call_2760 = func_2759_call()
output = call_2760
func_2761 = relay.Function([], output)
mutated_mod['func_2761'] = func_2761
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2378_call = mod.get_global_var('func_2378')
func_2380_call = mutated_mod.get_global_var('func_2380')
call_2791 = relay.TupleGetItem(func_2378_call(), 0)
call_2792 = relay.TupleGetItem(func_2380_call(), 0)
output = relay.Tuple([call_2791,])
output2 = relay.Tuple([call_2792,])
func_2798 = relay.Function([], output)
mod['func_2798'] = func_2798
mod = relay.transform.InferType()(mod)
mutated_mod['func_2798'] = func_2798
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2798_call = mutated_mod.get_global_var('func_2798')
call_2799 = func_2798_call()
output = call_2799
func_2800 = relay.Function([], output)
mutated_mod['func_2800'] = func_2800
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2759_call = mod.get_global_var('func_2759')
func_2761_call = mutated_mod.get_global_var('func_2761')
call_2813 = relay.TupleGetItem(func_2759_call(), 1)
call_2814 = relay.TupleGetItem(func_2761_call(), 1)
func_1249_call = mod.get_global_var('func_1249')
func_1251_call = mutated_mod.get_global_var('func_1251')
call_2821 = relay.TupleGetItem(func_1249_call(), 0)
call_2822 = relay.TupleGetItem(func_1251_call(), 0)
func_671_call = mod.get_global_var('func_671')
func_675_call = mutated_mod.get_global_var('func_675')
var_2824 = relay.var("var_2824", dtype = "uint16", shape = (132, 2))#candidate|2824|(132, 2)|var|uint16
var_2825 = relay.var("var_2825", dtype = "int16", shape = ())#candidate|2825|()|var|int16
call_2823 = relay.TupleGetItem(func_671_call(relay.reshape(var_2824.astype('uint16'), [264,]), relay.reshape(var_2825.astype('int16'), []), ), 4)
call_2826 = relay.TupleGetItem(func_675_call(relay.reshape(var_2824.astype('uint16'), [264,]), relay.reshape(var_2825.astype('int16'), []), ), 4)
output = relay.Tuple([call_2813,call_2821,call_2823,var_2824,var_2825,])
output2 = relay.Tuple([call_2814,call_2822,call_2826,var_2824,var_2825,])
func_2830 = relay.Function([var_2824,var_2825,], output)
mod['func_2830'] = func_2830
mod = relay.transform.InferType()(mod)
var_2831 = relay.var("var_2831", dtype = "uint16", shape = (132, 2))#candidate|2831|(132, 2)|var|uint16
var_2832 = relay.var("var_2832", dtype = "int16", shape = ())#candidate|2832|()|var|int16
output = func_2830(var_2831,var_2832,)
func_2833 = relay.Function([var_2831,var_2832,], output)
mutated_mod['func_2833'] = func_2833
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2759_call = mod.get_global_var('func_2759')
func_2761_call = mutated_mod.get_global_var('func_2761')
call_2835 = relay.TupleGetItem(func_2759_call(), 0)
call_2836 = relay.TupleGetItem(func_2761_call(), 0)
func_292_call = mod.get_global_var('func_292')
func_294_call = mutated_mod.get_global_var('func_294')
const_2845 = relay.const([0.232704,-1.346328,-5.120611,9.860264,3.884746,-4.491421,-6.273062,6.592315,-8.024683,-8.003748,-1.353483,-2.696034,4.206555,-1.501991,-5.757748,4.584651,5.701170,8.853922,7.708411,2.810957,2.349754,3.755073,-4.997257,-1.341028,1.187485,-3.954427,5.556693,7.888532,9.518586,9.068969,9.631845,-6.564555,4.725823,-5.378904,-6.278065,0.778535,-5.592060,6.141914,0.607096,6.564711,5.250337,-1.345178], dtype = "float64")#candidate|2845|(42,)|const|float64
call_2844 = relay.TupleGetItem(func_292_call(relay.reshape(const_2845.astype('float64'), [2, 7, 3])), 0)
call_2846 = relay.TupleGetItem(func_294_call(relay.reshape(const_2845.astype('float64'), [2, 7, 3])), 0)
func_1140_call = mod.get_global_var('func_1140')
func_1142_call = mutated_mod.get_global_var('func_1142')
call_2853 = relay.TupleGetItem(func_1140_call(), 0)
call_2854 = relay.TupleGetItem(func_1142_call(), 0)
uop_2867 = relay.atan(call_2853.astype('float32')) # shape=(10, 2, 14)
uop_2869 = relay.atan(call_2854.astype('float32')) # shape=(10, 2, 14)
output = relay.Tuple([call_2835,call_2844,const_2845,uop_2867,])
output2 = relay.Tuple([call_2836,call_2846,const_2845,uop_2869,])
func_2870 = relay.Function([], output)
mod['func_2870'] = func_2870
mod = relay.transform.InferType()(mod)
output = func_2870()
func_2871 = relay.Function([], output)
mutated_mod['func_2871'] = func_2871
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2877 = relay.var("var_2877", dtype = "uint8", shape = (7, 10, 5))#candidate|2877|(7, 10, 5)|var|uint8
var_2878 = relay.var("var_2878", dtype = "uint8", shape = (7, 10, 5))#candidate|2878|(7, 10, 5)|var|uint8
bop_2879 = relay.not_equal(var_2877.astype('bool'), relay.reshape(var_2878.astype('bool'), relay.shape_of(var_2877))) # shape=(7, 10, 5)
bop_2884 = relay.floor_divide(var_2878.astype('float64'), relay.reshape(var_2877.astype('float64'), relay.shape_of(var_2878))) # shape=(7, 10, 5)
func_2344_call = mod.get_global_var('func_2344')
func_2347_call = mutated_mod.get_global_var('func_2347')
var_2890 = relay.var("var_2890", dtype = "float32", shape = (960,))#candidate|2890|(960,)|var|float32
call_2889 = relay.TupleGetItem(func_2344_call(relay.reshape(var_2890.astype('float32'), [15, 4, 16])), 0)
call_2891 = relay.TupleGetItem(func_2347_call(relay.reshape(var_2890.astype('float32'), [15, 4, 16])), 0)
bop_2901 = relay.multiply(bop_2884.astype('float32'), relay.reshape(bop_2879.astype('float32'), relay.shape_of(bop_2884))) # shape=(7, 10, 5)
func_2344_call = mod.get_global_var('func_2344')
func_2347_call = mutated_mod.get_global_var('func_2347')
call_2922 = relay.TupleGetItem(func_2344_call(relay.reshape(call_2889.astype('float32'), [15, 4, 16])), 1)
call_2923 = relay.TupleGetItem(func_2347_call(relay.reshape(call_2889.astype('float32'), [15, 4, 16])), 1)
func_564_call = mod.get_global_var('func_564')
func_567_call = mutated_mod.get_global_var('func_567')
const_2925 = relay.const([[-9.027957,1.944333,-2.860427,5.745037,-8.281956,-1.618733,3.271468,9.313601,8.732142,1.161277,-5.239821,0.012755,-2.495325,5.676048,4.262984,8.334452,-3.422995,7.028159,-8.287616,2.725231,-1.078215,3.147301,0.464398,-4.828157,-6.945894,-8.738534,2.476958,-3.591619,-4.981442,-8.925895,-7.183606,9.453058,0.271260,-6.132614,-1.540236,-1.734781,7.715007,-9.413904,4.852733,4.537553,-0.662983,-8.713398,2.608974,1.253012,-8.387188,-7.307254,1.494803,-2.341194,-3.208556,-6.200895,-1.387691,6.023236,-0.975309,-8.998201,3.865733,0.826947,6.929993,8.159077,9.073517,-6.703654,-0.308617,-4.747909,9.752488,-0.783255,0.952736,-1.008834,-0.862603,1.611476,1.756455,-1.945254,2.523805,9.728316,8.839874,-1.629867,5.178411,-7.653152,1.797635,-5.058924,1.832249,-1.069073,0.148315,-9.992290,3.603540,0.080541,-8.156175,1.780861,0.313933,-0.479927,8.971169,9.458514,-5.701329,-3.907691,7.371212,-5.581447,-7.637267,1.113333,6.285020,3.891632,-7.303354,4.666060,-3.628096,-9.139920,7.144954,-8.706034,1.671633,-6.072762,8.617706,5.231770,9.611100,-6.892144,1.035950,2.016736,4.633326,4.060441,1.774877,-1.688342,9.410884,-9.271674,-1.829898,7.127631,-1.061640,2.148272,-5.403060,-2.311656,-0.685491,9.476156,1.910994,-2.086993,2.889450,-7.802940,-9.340994,-2.040566,0.394018,6.116148,4.998216,-1.560634,-6.740845,-3.045276,-6.227269,-9.956235,0.844662,-3.804085,-5.378291,6.350874,-4.436960,1.213615,0.132684,-7.767937,-7.509818,-9.351696,-0.700886,2.068228,-3.688030,-4.060945,8.867087,3.562745,-2.916187,4.754656,-6.717869,8.237658,-8.558340,6.034772,-1.753914,-6.357737,2.217448,1.444342,4.468984,-5.327065,-7.523228,8.246816,2.627022,-0.329203,-8.773536,3.623326,-5.581317,-7.245512,1.709223,-0.984034,3.289070,-7.607038,9.763857,9.219618,-6.470110,-4.213269,-3.942146,-0.302096,-3.886860,6.095052,-4.126701,7.718878,6.480147,6.239222,-9.971758,2.170510,0.501254,-8.259596,8.543346,7.451260,-9.237470,-9.004233,1.028769,-2.206585,4.983263,8.536540,-0.291601,-0.430702,-6.844332,-9.822103,-8.438386,-4.251070,2.733935,-6.818489,-7.544496,0.812998,-3.553941,9.625663,-6.926752,5.206883,-3.100342,-3.525815,-8.670471,-7.439284,-0.459976,6.424405,-7.698523,-9.834410,-0.042745,-6.554899,2.405168,9.162866,9.824807,7.516003,6.294841,6.858668,6.835212,-6.751253,2.226436,-1.404171,-0.326824,-8.474714,-6.183479,-6.815879,8.944822,2.360861,-8.169718,-1.879918,-4.226619,-4.745804,7.418918,0.799043,1.889711,-8.710137,-7.324194,-5.428426,-6.440475,-4.717003,-0.883238,5.836680,3.121663,-8.370209,-0.366663,-3.038426,-3.570650,-7.008128,-1.869093,6.784674,1.823148,-8.237525,-0.250529,-3.982669,8.101980,7.896058,-0.345208,-0.697068,-2.266281,4.762989,5.711615,3.843896,-2.077014,5.318938,7.927625,-9.354622,-0.842143,-2.261469,-7.521375,3.688068,0.101791,1.788008,-8.081212,-6.554751,-8.127220,6.190517,0.747185,5.085006,-3.300589,-8.333910,5.997989,-2.073056,-5.778633,0.545692,-1.487994,-9.355007,0.972503,0.325014,0.669127,-0.441785,7.287811,-2.822951,-8.635776,6.861362,-2.768714,-5.978943,-2.463682,-6.054595,-0.796581,9.966137,-1.319520,-8.551391,8.657661,9.752405,4.955861,-7.093146,6.352159,5.364933,2.735900,-9.315085,4.626600,1.194291,-2.513872,-7.880111,8.301833,9.534205,1.665504,-5.600315,3.683349,-1.319092,1.064189,2.744222,0.142009,7.229022,5.977843,-3.217596,-6.640933,6.160557,2.373213,0.393498,0.317816,2.574868,7.716656,-2.600992,0.788245,0.733847,9.966784,-3.523523,-8.599782,4.357348,1.104759,-2.617608,-7.402337,-9.136131,8.234230,-8.506474,-7.779552,6.666282,5.948338,-6.282127,-6.064536,-2.240125,9.499616,-8.545885,-0.355260,5.275464,-8.559039,0.846485,6.274720,-5.438120,-5.844793,-1.082292,-3.383918,-0.612837,5.233326,7.731859,-7.536812,4.781504,-4.053977,4.896685,-0.981997,-3.579008,-9.272506,8.126666,-3.289220,-3.824967,-3.936628,7.985940,5.227683,8.457697,5.842434,-7.476993,-0.713706,8.880984,-0.504986,1.805019,9.619043,3.380987,5.460789,-1.205350,-6.441656,-0.108436,7.219483,-2.922125,7.964921,8.276344,-6.034187,9.916509,9.265590,5.283858,8.685573,-7.026793,-7.244327,0.575702,-8.616610,4.908743,-7.128979,-5.035040,-9.838635,-2.835788,-5.786432,-8.584916,-7.327983,4.177601,-5.186294,7.435880,2.322756,-2.967258,1.694528,9.203429,7.501971,-6.179921,6.073889,8.169860,8.664090,1.903928,5.880399,-0.198687,2.048189,-9.830431,-4.945329,-2.883840,9.351615,-9.578537,-8.644765,1.542043,-9.450928,5.885844,-2.613985,0.632389,1.620870,1.708234,-5.120851,-3.104769,0.229117,1.339786,-0.842555,5.643831,7.641085,-8.050040,8.991947,3.943816,5.290634,5.353942,-9.784871,-5.842080,-9.628542,-0.436776,3.307327,-7.084764,9.781741,3.618172,8.089406,-6.260768,-7.271665,-1.510010,-8.906655,0.696964,4.790699,5.665691,-4.438647,2.145756,6.515621,8.255924,-8.105796,7.508491,-2.344530,8.786503,3.529086,-8.956977,-1.405774,8.789323,-3.735425,-9.013477,-4.436855,6.701229,9.388848,8.664966,2.205685,-0.386370,-8.553059,9.523298,-4.006287,8.895355,-5.161723,0.649950,-6.426159,2.585167,6.773527,-3.115498,0.055047,-4.398573,-9.627604,2.774221,5.910798,7.960499,8.108976,-4.997359,1.780314,3.270693,0.989093,-0.347116,-5.092191,-0.103637,-8.375985,8.773545,3.058748,-4.782956,3.550247,6.890741,8.464443,-0.784770,3.845178,-1.698666,-2.345521,0.035109,-3.407334,-6.695581,6.167312,0.728433,5.569831,-0.990678,-4.667465,3.649634,-7.177465,-0.322380,7.933930,8.768379,1.616614,-8.897610,0.621953,1.266193,7.333871,-2.276623,3.247109,-4.937168,-0.745568,3.230566,-8.398681,-4.431438,5.462761,-3.226356,-3.441627,7.785048,-6.150696,6.089326,2.187461,2.957971,-5.737730,-1.319521,5.161437,7.474253,0.625250,4.569820,3.586557,-0.907041,-7.695967,9.716254,-8.448815,8.461907,-4.022306,1.531311,8.389625,7.501101,-6.800106,9.201221,-0.503565,-2.089372,8.923856,5.803972,6.766983,9.753868,7.626530,-9.502684,-2.329078,-1.173348,0.589418,-4.154912,-7.883448,-1.678232,3.142374,3.101642,-0.048919,0.821459,2.957562,-8.355058,1.093952,-8.383832,7.212026,-7.016038,-5.435498,-5.146598,-7.609347,5.921043,-6.898255,-9.312334,2.919071,-7.235030,4.188054,-3.170136,-5.539893,2.267294,-9.307265,-5.117763,9.353600,8.910200,2.180219,8.347673,3.587490,0.154127,-3.418498,3.782474,0.459138,-0.287738,-9.122578,6.933624,5.769479,-1.922005,-0.396729,3.396889,5.631082,-7.932551,6.513644,5.038549,-5.547779,-5.451695,-1.052851,-6.632884,2.625068,-1.568768,9.451385,5.125546,-7.998563,7.032619,-1.503720,-2.332145,2.672829,6.274116,-0.795938,7.636516,7.254900,-4.513856,-7.545675,6.121021,3.553712,0.061430,6.357843,5.340031,-2.885506,-5.663062,-5.793271,-2.523841,8.013511,-3.350244,-1.661564,-3.478431,4.547944,9.932432,-0.824322,-4.411885,-9.248045,-2.236870,-1.843447,-7.512634,-4.635942,0.763878,4.568142,9.067271,7.937624,4.773711,9.589628,1.848088,-0.155786,-5.301859,1.790406,-5.285832,-6.203374,9.073414,-0.983642,1.587854,0.359190,7.080737,1.742068,9.689261,-0.798907,-1.146097,1.008474,9.048591,9.365985,-9.848904,-3.428853,-4.070581,7.334310,6.958377,1.450766,8.701794,5.559116,-4.399325,8.277297,-4.510417,-2.531850,7.822758,-5.681164,6.189009,2.137937,6.796807,-7.094980,-8.664655,1.030023,8.597132,7.616583,1.755731,-4.076032,9.717542,-6.318701,9.259792,-2.899525,-9.340035,0.088910,-5.145368,7.484420,-8.574868,-0.117196,9.056190,-4.024586,-2.294972,0.875858,6.202187,6.955925,9.468702,-3.207230,-6.068421,-7.708442,1.037166,-3.991346,-7.179299,4.589318,1.206157,0.694119,-6.087700,-2.577474,3.575939,-1.327368,8.584310,8.210178,2.330305,9.493660,7.802258,-6.215402,-9.907767,-6.754421,-7.293638,0.627771,4.303350,0.642822,5.847993,6.342368,7.826928,9.037621,1.535604,-5.200782,-2.045277,8.085781,1.983747,-9.914994,-8.447448,-0.800098,7.889649,3.498466,-9.492286,-1.293403,-8.967631,5.265696,1.775514,-0.972571,7.506874,-7.561261,-0.757281,6.620900,2.927056,8.954737,1.346550,7.911700,-7.183862,0.831149,6.778569,-6.612830,0.669924,4.220147,-5.573782,-0.625559,-1.554982,3.582312,-7.723570,-1.729988,-7.475506,9.570873,8.686324,-9.077976,8.283523,4.941705,3.217600,-5.847593,0.657523,-9.437134,4.986195,9.122235,0.941329,3.781697,-5.911479,8.331978,1.108721,-8.366342,4.376135,-3.698586,-0.060383,8.207523,1.672457,9.793987,-8.298422,-5.100870,-4.437015,2.928966,-0.345980,1.568941,8.004806,-0.766726,7.439283,2.555428,9.393739,-1.910665,1.861861,-1.557651,3.870537,8.622856,7.691663,-9.584285,-9.355602,5.017957,-5.195555,1.719105,8.992738,-2.260631,-2.525752,-2.361986,-3.862302,3.783564,-7.006282,-4.274485,2.949227,2.812631,-1.870206,-6.753450,-0.413494,8.179326,-0.622200,-4.336804,-5.967999,3.313536,-2.738392,1.860935,-7.342953,6.555445,-6.640566,-0.287252,9.478528,-9.793011,0.908630,-1.542455,-7.623093,-9.159963,-7.924843,-8.632318,-7.247323,1.582795,0.971489,7.243896,-9.748710,2.290205,-8.822717,-5.577794,0.127676,7.100204,-9.554039,-5.515029,-1.852562,4.212610,1.094105,0.818138,5.116161,4.135417,9.460666,-0.713589,0.410562,-8.446391,-7.120942,8.908141,6.332331,-1.322869,5.908816,-2.475248,-3.710083,-8.867399,-5.950774,3.453891,2.337801,-8.547099,4.529747,-9.501212,-5.566925,-0.914795,0.070677,0.687796,9.691758,-9.894590,-6.898635,-9.605559,3.170665,1.608200,-1.724951,7.318701,1.591476,0.887500,6.576406,0.340207,-0.230298,-2.842089,6.767676,3.438472,0.543198,7.037955,-9.758436,-1.012598,6.730545,4.135972,-3.926389,2.387921,4.975826,-4.575086,-5.678990,-7.564696,-4.071310,-7.177316,-9.719697,-2.332052,-7.288039,-1.486939,8.423642,-9.224654,-5.910158,-7.905369,-1.585718,-1.704966,-9.834447,-1.769313,-0.906097,-6.669695,2.291137,-5.655165,-5.829252,-9.250435,8.698370,9.486756,0.278891,6.803877,-7.482255,8.058175,6.225539,-9.965858,-0.233426,-0.497834,8.107452,2.776832,3.801828,2.643348]], dtype = "float64")#candidate|2925|(1, 1001)|const|float64
var_2926 = relay.var("var_2926", dtype = "float64", shape = (42, 1))#candidate|2926|(42, 1)|var|float64
call_2924 = relay.TupleGetItem(func_564_call(relay.reshape(const_2925.astype('float64'), [11, 13, 7]), relay.reshape(var_2926.astype('float64'), [42,]), ), 6)
call_2927 = relay.TupleGetItem(func_567_call(relay.reshape(const_2925.astype('float64'), [11, 13, 7]), relay.reshape(var_2926.astype('float64'), [42,]), ), 6)
output = relay.Tuple([call_2889,var_2890,bop_2901,call_2922,call_2924,const_2925,var_2926,])
output2 = relay.Tuple([call_2891,var_2890,bop_2901,call_2923,call_2927,const_2925,var_2926,])
func_2928 = relay.Function([var_2877,var_2878,var_2890,var_2926,], output)
mod['func_2928'] = func_2928
mod = relay.transform.InferType()(mod)
mutated_mod['func_2928'] = func_2928
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2928_call = mutated_mod.get_global_var('func_2928')
var_2930 = relay.var("var_2930", dtype = "uint8", shape = (7, 10, 5))#candidate|2930|(7, 10, 5)|var|uint8
var_2931 = relay.var("var_2931", dtype = "uint8", shape = (7, 10, 5))#candidate|2931|(7, 10, 5)|var|uint8
var_2932 = relay.var("var_2932", dtype = "float32", shape = (960,))#candidate|2932|(960,)|var|float32
var_2933 = relay.var("var_2933", dtype = "float64", shape = (42, 1))#candidate|2933|(42, 1)|var|float64
call_2929 = func_2928_call(var_2930,var_2931,var_2932,var_2933,)
output = call_2929
func_2934 = relay.Function([var_2930,var_2931,var_2932,var_2933,], output)
mutated_mod['func_2934'] = func_2934
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1167_call = mod.get_global_var('func_1167')
func_1169_call = mutated_mod.get_global_var('func_1169')
call_2936 = relay.TupleGetItem(func_1167_call(), 0)
call_2937 = relay.TupleGetItem(func_1169_call(), 0)
var_2942 = relay.var("var_2942", dtype = "bool", shape = (10, 2, 14))#candidate|2942|(10, 2, 14)|var|bool
bop_2943 = relay.mod(call_2936.astype('float64'), relay.reshape(var_2942.astype('float64'), relay.shape_of(call_2936))) # shape=(10, 2, 14)
bop_2946 = relay.mod(call_2937.astype('float64'), relay.reshape(var_2942.astype('float64'), relay.shape_of(call_2937))) # shape=(10, 2, 14)
const_2951 = relay.const([[[True,False,True,True,True,True,False,True,True,False,False,False,False,True],[True,False,False,True,True,False,False,True,False,False,False,True,False,True]],[[True,False,True,True,False,True,False,True,False,False,False,True,False,True],[True,False,False,True,False,False,False,False,True,False,True,True,False,False]],[[False,True,True,True,True,True,False,True,False,False,False,False,False,False],[True,True,True,True,True,False,False,False,False,False,False,True,False,True]],[[False,False,True,False,True,True,False,False,False,False,True,False,True,True],[False,True,False,True,False,True,False,False,True,False,False,False,False,False]],[[True,False,True,False,True,True,False,False,False,False,True,False,True,False],[False,False,False,False,True,False,True,False,True,False,False,True,False,False]],[[True,True,False,False,True,True,False,False,False,True,True,False,True,False],[False,False,False,False,False,False,False,False,False,False,False,False,False,False]],[[True,False,False,False,True,False,False,True,True,True,True,False,False,False],[False,True,False,True,False,True,True,False,True,False,False,False,False,False]],[[False,False,False,True,False,False,True,False,False,True,True,False,False,False],[False,False,True,False,False,True,True,False,False,True,False,False,True,True]],[[False,True,True,False,True,False,True,True,False,False,True,True,True,False],[True,False,True,True,False,False,True,False,True,True,False,False,False,True]],[[False,True,False,False,False,True,False,True,True,True,False,False,True,False],[True,False,False,False,False,True,True,True,True,False,True,True,True,False]]], dtype = "bool")#candidate|2951|(10, 2, 14)|const|bool
bop_2952 = relay.greater_equal(call_2936.astype('bool'), relay.reshape(const_2951.astype('bool'), relay.shape_of(call_2936))) # shape=(10, 2, 14)
bop_2955 = relay.greater_equal(call_2937.astype('bool'), relay.reshape(const_2951.astype('bool'), relay.shape_of(call_2937))) # shape=(10, 2, 14)
func_1140_call = mod.get_global_var('func_1140')
func_1142_call = mutated_mod.get_global_var('func_1142')
call_2979 = relay.TupleGetItem(func_1140_call(), 0)
call_2980 = relay.TupleGetItem(func_1142_call(), 0)
output = relay.Tuple([bop_2943,bop_2952,call_2979,])
output2 = relay.Tuple([bop_2946,bop_2955,call_2980,])
func_2991 = relay.Function([var_2942,], output)
mod['func_2991'] = func_2991
mod = relay.transform.InferType()(mod)
mutated_mod['func_2991'] = func_2991
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2992 = relay.var("var_2992", dtype = "bool", shape = (10, 2, 14))#candidate|2992|(10, 2, 14)|var|bool
func_2991_call = mutated_mod.get_global_var('func_2991')
call_2993 = func_2991_call(var_2992)
output = call_2993
func_2994 = relay.Function([var_2992], output)
mutated_mod['func_2994'] = func_2994
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1654_call = mod.get_global_var('func_1654')
func_1656_call = mutated_mod.get_global_var('func_1656')
call_3047 = func_1654_call()
call_3048 = func_1654_call()
func_564_call = mod.get_global_var('func_564')
func_567_call = mutated_mod.get_global_var('func_567')
const_3051 = relay.const([-4.845345,-4.075560,-4.462689,2.566342,5.934958,9.550160,-1.851854,-3.033507,8.936499,5.520456,-4.015344,-0.716676,-8.539075,-5.585157,9.806708,-6.118340,8.812344,5.455270,7.454044,7.521573,7.219839,-2.382190,5.015019,-1.773506,-5.443384,4.545388,-1.766416,7.859378,-5.542234,-0.103773,3.553919,5.864570,-5.955693,-7.111703,-6.857143,-0.152603,8.140265,4.966655,-8.080316,9.389792,8.390188,0.955390,2.771053,1.650010,-4.248348,7.009372,-7.276068,0.485469,-8.614986,0.982664,7.402634,-8.851142,-2.776063,0.903033,-6.854326,2.672115,1.791246,4.160913,-6.979914,-2.995772,-2.545323,-9.219472,8.392074,4.421056,-9.903603,-3.466364,8.565271,-7.381412,-8.209283,-9.555152,-6.837237,2.440009,-0.498749,-3.955214,8.012407,1.212185,7.758291,-2.877394,7.723266,-7.278206,-4.258701,1.162690,3.043718,4.479175,2.914254,-0.067492,-9.966063,4.988272,-9.503723,3.909411,3.765370,-6.605233,-4.748142,2.034202,-2.544216,3.758408,-4.529783,-2.242397,-6.889487,2.739198,1.322515,-9.116760,9.259968,-2.183808,5.920880,4.947077,9.150632,1.369713,7.432527,7.264587,-0.878290,-5.180077,-3.621771,3.189029,3.145664,-1.390570,-3.099836,-3.749209,5.347771,-1.097935,-1.593166,2.501664,0.019802,3.266595,8.899918,-2.059600,-9.074649,-2.479470,-6.823700,3.971615,-7.465005,-7.407048,-1.517205,2.538049,-7.113042,8.265355,2.751733,-8.717150,3.887897,5.326091,-4.271429,5.906947,3.403192,3.840732,1.274523,0.507629,7.110740,-3.478926,-4.548644,5.520497,1.146914,6.753477,3.480319,1.885132,9.700200,6.191742,4.975607,-5.313417,-0.510196,-2.109630,9.096826,1.049009,1.228567,-4.223025,6.128789,-0.839517,-2.341665,-1.390679,8.943267,4.193806,-0.815326,0.784392,1.442890,-5.456829,3.738038,8.092394,-9.076229,7.767569,-2.026331,2.785395,8.393336,8.929011,3.664993,0.689663,8.065105,-9.128853,3.254483,7.565373,8.984066,-1.584647,-3.010236,4.355199,7.011156,5.670127,8.218909,2.206856,-0.893921,-3.713107,-0.320055,2.481666,-9.460996,-2.227543,9.076206,-9.717735,3.017178,9.802023,-7.337205,6.467650,-3.432150,-1.052664,2.425622,-7.930671,-4.647738,-2.666628,4.743146,-1.034568,0.602799,3.848431,8.395685,6.046881,7.018988,-6.897343,-3.627107,9.246720,-0.496340,-4.628334,3.516951,-2.553343,4.286183,0.098554,-3.571392,8.965947,-6.543525,-2.260216,-3.737223,-3.400413,-0.720195,-8.053750,-5.045691,6.467345,7.461350,4.478819,3.733927,-9.929134,-2.419010,3.021323,1.026540,-3.469417,1.500965,9.920674,-1.327256,8.535232,7.485691,7.206629,0.665764,-2.614216,-4.519959,-6.487778,4.422368,7.361552,-0.504027,-7.083513,5.994325,4.599184,2.472065,-9.040561,-2.708320,9.377678,8.364250,-4.727511,4.773675,1.593657,-3.968405,6.915379,-7.367829,0.437333,2.057759,2.306193,-2.016839,-9.755074,9.280040,5.130079,-7.215104,7.411450,-9.057837,1.523307,5.594961,4.060608,-8.523083,2.831169,4.594032,0.657392,9.608343,4.926019,8.431902,3.919948,1.443813,-8.144165,3.642830,5.306838,2.535480,-4.761433,-7.807530,-6.110811,-8.033084,7.586407,-0.313678,8.997960,5.815198,4.310929,-6.824962,-6.940693,-1.809472,4.959803,-3.482707,0.039151,1.099684,-3.679933,1.117337,-2.482559,2.084599,-6.316477,-8.117029,3.717036,-5.873040,-6.354515,9.646597,-4.728830,-9.045058,-8.554778,5.704414,-4.071595,1.829053,-8.885750,-1.243410,-7.936487,-4.829516,4.377604,-5.256354,1.702631,-9.937142,1.487772,-2.155151,6.789715,-7.537293,1.376295,8.554412,-9.620376,5.577186,8.885553,-0.841654,9.004477,-5.377593,9.931880,3.394955,-3.946586,4.527285,6.920937,5.295079,-6.109794,-3.244032,7.532815,0.010075,-8.011077,-3.798143,-1.851759,-5.437296,-6.253987,3.875100,2.980575,-2.689473,-4.680132,-1.042135,6.681373,-0.969603,5.744685,9.425562,-8.151832,-3.104393,3.581664,-3.855545,8.555204,0.959408,-0.200973,-1.004923,5.087578,4.109366,-0.316894,-6.760633,1.989187,9.161582,1.275192,-7.884712,4.009541,0.940189,4.522222,5.417686,-7.815172,-7.991007,6.898016,-0.688296,6.872638,-9.401282,7.390023,8.312555,9.068367,7.486854,-4.052195,-4.019988,4.549562,-7.963939,4.059229,4.942193,7.496245,-4.183898,-4.011527,7.812939,-3.166829,5.461316,-7.501036,6.757661,3.906570,2.938233,-6.499197,-9.738341,2.142937,-6.267357,-2.265200,-1.520118,-7.891281,-1.448919,7.583362,-2.616053,7.983396,-4.993559,8.634047,6.105528,-4.459514,-7.441560,-4.353230,-5.481329,9.678867,-7.229290,3.465892,4.580042,-4.235466,-4.188094,-1.803650,0.036815,7.646522,1.421281,9.830564,9.295585,6.169131,-6.393084,-9.432413,2.525777,-5.216930,1.988651,-8.978713,3.474464,-2.052329,0.892068,-7.646313,-9.300545,-0.209969,-8.433730,-7.137504,4.943534,7.079555,2.396461,7.958423,-0.476133,2.703381,3.026957,-5.742905,-2.081069,-7.236485,4.132176,-4.503131,-7.672023,-3.422735,3.108621,6.534497,-4.807294,-5.675374,-7.670604,0.070174,7.153131,3.018657,-0.745955,2.105168,-2.024550,-7.168995,1.981566,-1.543086,2.126443,-3.803679,3.965306,-6.042200,6.771377,-9.919750,-5.926873,-1.783717,-3.298877,-6.199794,5.958968,0.629845,3.962694,-2.950311,-1.780887,0.133077,1.992163,-3.733883,0.438937,-0.794784,-4.959844,-4.204766,-6.723262,-3.878642,-8.340753,-1.145664,6.540262,-8.162725,5.144670,0.604321,7.173927,-1.288694,-4.780075,2.588796,3.659598,-0.759937,-4.052199,-4.941659,0.869862,4.486191,0.435133,-2.046351,5.904074,7.035290,3.274005,8.303656,7.364096,0.386898,-1.672773,5.967752,-7.979477,4.925977,4.863205,-9.674937,5.026693,-0.073099,5.237454,8.332641,5.127135,9.761171,9.526918,4.559741,-9.296780,-3.164345,-1.784373,-4.809392,-5.659289,8.602817,7.564218,-5.008649,-2.243351,7.712848,6.514631,-0.631554,-2.739874,9.838180,-6.446687,-0.034447,4.571922,-1.329451,8.699816,1.368194,-1.058071,0.710632,-3.226797,-0.763639,-1.497765,-2.864224,-6.392852,2.241207,-4.003499,-6.828915,6.793716,-6.915099,-7.798493,-0.470453,0.475288,5.208255,4.986144,-9.512016,-7.805771,-0.632548,-7.228238,6.103814,8.269460,3.126655,9.356588,1.811793,4.314890,-2.934964,-3.763698,7.088109,-4.966659,3.055841,2.248411,7.084700,0.141869,-5.677399,-5.722733,-7.756792,-0.671238,5.495366,-3.225180,1.415066,-8.270545,6.587571,-8.104221,2.448170,7.190357,-7.838138,-7.113469,-5.149466,6.124487,0.586570,-3.546020,-9.108786,-4.542329,7.715334,-9.511247,-1.657090,-3.353588,2.054710,-8.052942,8.426201,1.484680,-1.423787,1.183000,4.503374,2.563889,-2.138791,8.150690,4.318040,-9.524592,-9.338841,2.019520,-2.213920,-9.511416,-9.122448,-6.186726,-7.167733,-1.714191,4.068219,2.878699,-7.414099,9.609329,6.661743,0.570767,-0.927095,2.196040,-9.210585,2.446007,-8.205461,-4.438912,-0.959113,-2.595334,4.170634,4.175678,-8.854007,7.048474,-4.846625,4.094157,5.385420,-5.801765,-2.000638,-9.229013,-4.994235,0.611937,7.674207,6.999232,-5.065320,-9.375069,-9.462734,-2.283251,8.681357,-9.358363,3.240162,8.424760,-9.357358,-7.389159,9.525411,-8.281995,2.876890,-3.300063,2.408283,-1.596209,9.067614,3.017183,6.631452,-6.306391,-4.786330,-3.592359,-3.380789,-9.337104,4.483036,7.103676,-9.640338,-8.164292,-2.575251,-8.227759,-0.261668,6.292919,-1.019777,-4.600676,1.558353,-2.112686,8.073177,8.627560,-1.431745,-2.521827,-0.788875,-5.614255,4.151572,-6.948158,6.739924,-2.374711,-6.248618,6.320330,-9.241606,-4.393010,-1.669706,9.063537,0.691509,0.504965,9.698973,3.349015,0.654604,-2.408631,-7.508272,-2.829957,2.801347,4.460510,3.088367,-0.104861,-2.614709,9.613822,8.146884,-9.700046,1.264558,-4.938871,-3.962284,-7.704114,8.588231,-9.027537,-9.942526,3.886905,2.334541,8.631366,9.123169,2.844299,-1.154216,-3.648629,2.988601,-2.523955,-9.389980,4.413266,-4.640268,9.547132,-8.674902,2.436036,-4.176645,9.093876,1.930812,-9.352325,-1.644387,0.884257,-2.302371,8.997139,-1.461955,-0.023593,-4.623835,3.612363,-6.059875,3.114102,3.034226,3.631647,8.244347,9.766211,3.742371,-5.641756,0.425294,-1.351471,7.303916,-2.471641,6.279984,6.612831,-0.869601,-5.136908,2.012278,-1.596628,-8.893567,-0.698461,-9.785850,-2.792561,-5.280457,2.224024,-6.001649,4.318468,7.210231,-3.647981,4.575950,4.425583,-6.056095,-5.629605,6.258885,-2.653165,-9.654862,3.405249,0.106419,-0.410192,-3.393812,3.318179,5.806959,1.166827,-5.611235,4.271554,9.362300,-1.689687,-6.156187,7.149453,6.938483,6.965501,-3.242201,-5.347679,-0.395244,2.994372,-8.616693,-0.439615,-8.856279,9.878113,9.257523,-7.076844,4.848627,-7.092268,3.532817,9.670001,-0.249877,-5.746545,9.747009,-1.564750,4.057531,1.840039,-2.787063,2.301683,3.612240,-9.054258,4.522673,5.076237,8.338051,-9.818604,1.375630,2.665863,-4.160510,-9.393328,-5.030711,8.901865,7.341747,6.545501,-5.702352,-6.073844,1.978645,-6.393689,6.960298,6.310724,-4.186617,6.502704,5.178129,5.779612,-6.013212,-4.364533,-7.971967,-0.345327,-4.222529,8.827962,-7.316280,-0.863246,-6.566098,-1.363643,-3.048293,-3.157360,4.534171,-6.597035,-5.768526,-6.551444,8.743868,1.300866,-4.680375,0.693293,-3.453026,-5.134235,-3.755204,-3.885803,6.257438,-5.667367,0.157579,-8.702793,-9.810072,4.603854,-5.910033,9.044829,-4.137715,9.656417,-6.192897,4.094460,-4.144794,7.379540,-4.639573,0.997566,-2.350466,5.470459,5.897934,-5.949627,-6.465861,-6.223765,4.642320,9.254757,2.863314,1.799511,8.870391,-4.016506,-4.721888,3.581959,9.524330,-3.474841,-1.652807,4.631810,-7.390561,-9.232063,-8.657093,0.200253,-3.480797,3.799233,-5.624814,-7.288586,-5.889651,7.588752,-3.165061,7.553209,2.361324,-9.861770,-6.374811,4.073724,1.936140,1.063947,7.673578,-9.284473,0.678807,6.498132,-9.457972,-3.415723,-1.113742,2.511297,-8.452169,-4.287040,-8.209340,8.402859,7.268236,2.003717,-7.856078,-8.674097,-9.998750,-6.780406,-0.221644,6.666381,1.497371,9.290807,1.428346,-4.130764,-4.475957,5.224953,0.115174,2.076661,-8.590158,-6.335907,7.083732,-0.234698,5.275132,-0.744559,-6.716696,-8.500672,6.821643,3.394241,-9.199967,-1.865034,-8.518513,2.920625], dtype = "float64")#candidate|3051|(1001,)|const|float64
var_3052 = relay.var("var_3052", dtype = "float64", shape = (42,))#candidate|3052|(42,)|var|float64
call_3050 = relay.TupleGetItem(func_564_call(relay.reshape(const_3051.astype('float64'), [11, 13, 7]), relay.reshape(var_3052.astype('float64'), [42,]), ), 7)
call_3053 = relay.TupleGetItem(func_567_call(relay.reshape(const_3051.astype('float64'), [11, 13, 7]), relay.reshape(var_3052.astype('float64'), [42,]), ), 7)
bop_3059 = relay.not_equal(call_3050.astype('bool'), const_3051.astype('bool')) # shape=(12, 3, 1001)
bop_3062 = relay.not_equal(call_3053.astype('bool'), const_3051.astype('bool')) # shape=(12, 3, 1001)
bop_3075 = relay.less_equal(bop_3059.astype('bool'), call_3050.astype('bool')) # shape=(12, 3, 1001)
bop_3078 = relay.less_equal(bop_3062.astype('bool'), call_3053.astype('bool')) # shape=(12, 3, 1001)
bop_3083 = relay.greater(bop_3059.astype('bool'), relay.reshape(bop_3075.astype('bool'), relay.shape_of(bop_3059))) # shape=(12, 3, 1001)
bop_3086 = relay.greater(bop_3062.astype('bool'), relay.reshape(bop_3078.astype('bool'), relay.shape_of(bop_3062))) # shape=(12, 3, 1001)
func_2759_call = mod.get_global_var('func_2759')
func_2761_call = mutated_mod.get_global_var('func_2761')
call_3088 = relay.TupleGetItem(func_2759_call(), 2)
call_3089 = relay.TupleGetItem(func_2761_call(), 2)
uop_3091 = relay.acosh(const_3051.astype('float32')) # shape=(1001,)
var_3099 = relay.var("var_3099", dtype = "float32", shape = (1001,))#candidate|3099|(1001,)|var|float32
bop_3100 = relay.logical_xor(uop_3091.astype('uint64'), relay.reshape(var_3099.astype('uint64'), relay.shape_of(uop_3091))) # shape=(1001,)
uop_3106 = relay.atanh(bop_3100.astype('float64')) # shape=(1001,)
func_708_call = mod.get_global_var('func_708')
func_711_call = mutated_mod.get_global_var('func_711')
call_3114 = relay.TupleGetItem(func_708_call(relay.reshape(var_3099.astype('bool'), [11, 13, 7])), 0)
call_3115 = relay.TupleGetItem(func_711_call(relay.reshape(var_3099.astype('bool'), [11, 13, 7])), 0)
uop_3121 = relay.sin(uop_3106.astype('float32')) # shape=(1001,)
func_1580_call = mod.get_global_var('func_1580')
func_1582_call = mutated_mod.get_global_var('func_1582')
call_3126 = relay.TupleGetItem(func_1580_call(), 0)
call_3127 = relay.TupleGetItem(func_1582_call(), 0)
func_2759_call = mod.get_global_var('func_2759')
func_2761_call = mutated_mod.get_global_var('func_2761')
call_3128 = relay.TupleGetItem(func_2759_call(), 0)
call_3129 = relay.TupleGetItem(func_2761_call(), 0)
func_2928_call = mod.get_global_var('func_2928')
func_2934_call = mutated_mod.get_global_var('func_2934')
var_3133 = relay.var("var_3133", dtype = "uint8", shape = (350, 1))#candidate|3133|(350, 1)|var|uint8
call_3132 = relay.TupleGetItem(func_2928_call(relay.reshape(var_3133.astype('uint8'), [7, 10, 5]), relay.reshape(var_3133.astype('uint8'), [7, 10, 5]), relay.reshape(call_3126.astype('float32'), [960,]), relay.reshape(var_3052.astype('float64'), [42, 1]), ), 1)
call_3134 = relay.TupleGetItem(func_2934_call(relay.reshape(var_3133.astype('uint8'), [7, 10, 5]), relay.reshape(var_3133.astype('uint8'), [7, 10, 5]), relay.reshape(call_3126.astype('float32'), [960,]), relay.reshape(var_3052.astype('float64'), [42, 1]), ), 1)
output = relay.Tuple([call_3047,var_3052,bop_3083,call_3088,call_3114,uop_3121,call_3126,call_3128,call_3132,var_3133,])
output2 = relay.Tuple([call_3048,var_3052,bop_3086,call_3089,call_3115,uop_3121,call_3127,call_3129,call_3134,var_3133,])
func_3153 = relay.Function([var_3052,var_3099,var_3133,], output)
mod['func_3153'] = func_3153
mod = relay.transform.InferType()(mod)
var_3154 = relay.var("var_3154", dtype = "float64", shape = (42,))#candidate|3154|(42,)|var|float64
var_3155 = relay.var("var_3155", dtype = "float32", shape = (1001,))#candidate|3155|(1001,)|var|float32
var_3156 = relay.var("var_3156", dtype = "uint8", shape = (350, 1))#candidate|3156|(350, 1)|var|uint8
output = func_3153(var_3154,var_3155,var_3156,)
func_3157 = relay.Function([var_3154,var_3155,var_3156,], output)
mutated_mod['func_3157'] = func_3157
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1598_call = mod.get_global_var('func_1598')
func_1599_call = mutated_mod.get_global_var('func_1599')
call_3159 = relay.TupleGetItem(func_1598_call(), 0)
call_3160 = relay.TupleGetItem(func_1599_call(), 0)
output = call_3159
output2 = call_3160
func_3166 = relay.Function([], output)
mod['func_3166'] = func_3166
mod = relay.transform.InferType()(mod)
output = func_3166()
func_3167 = relay.Function([], output)
mutated_mod['func_3167'] = func_3167
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2412_call = mod.get_global_var('func_2412')
func_2414_call = mutated_mod.get_global_var('func_2414')
call_3168 = relay.TupleGetItem(func_2412_call(), 0)
call_3169 = relay.TupleGetItem(func_2414_call(), 0)
output = relay.Tuple([call_3168,])
output2 = relay.Tuple([call_3169,])
func_3172 = relay.Function([], output)
mod['func_3172'] = func_3172
mod = relay.transform.InferType()(mod)
output = func_3172()
func_3173 = relay.Function([], output)
mutated_mod['func_3173'] = func_3173
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3208 = relay.var("var_3208", dtype = "float64", shape = ())#candidate|3208|()|var|float64
var_3209 = relay.var("var_3209", dtype = "float64", shape = (16, 15, 14))#candidate|3209|(16, 15, 14)|var|float64
bop_3210 = relay.power(var_3208.astype('float64'), var_3209.astype('float64')) # shape=(16, 15, 14)
uop_3216 = relay.atan(var_3209.astype('float32')) # shape=(16, 15, 14)
uop_3219 = relay.tan(uop_3216.astype('float32')) # shape=(16, 15, 14)
uop_3243 = relay.sigmoid(uop_3219.astype('float64')) # shape=(16, 15, 14)
bop_3247 = relay.bitwise_or(uop_3219.astype('int32'), relay.reshape(bop_3210.astype('int32'), relay.shape_of(uop_3219))) # shape=(16, 15, 14)
output = relay.Tuple([uop_3243,bop_3247,])
output2 = relay.Tuple([uop_3243,bop_3247,])
func_3252 = relay.Function([var_3208,var_3209,], output)
mod['func_3252'] = func_3252
mod = relay.transform.InferType()(mod)
var_3253 = relay.var("var_3253", dtype = "float64", shape = ())#candidate|3253|()|var|float64
var_3254 = relay.var("var_3254", dtype = "float64", shape = (16, 15, 14))#candidate|3254|(16, 15, 14)|var|float64
output = func_3252(var_3253,var_3254,)
func_3255 = relay.Function([var_3253,var_3254,], output)
mutated_mod['func_3255'] = func_3255
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2109_call = mod.get_global_var('func_2109')
func_2111_call = mutated_mod.get_global_var('func_2111')
call_3260 = relay.TupleGetItem(func_2109_call(), 1)
call_3261 = relay.TupleGetItem(func_2111_call(), 1)
func_377_call = mod.get_global_var('func_377')
func_381_call = mutated_mod.get_global_var('func_381')
var_3268 = relay.var("var_3268", dtype = "int16", shape = ())#candidate|3268|()|var|int16
var_3269 = relay.var("var_3269", dtype = "int16", shape = (36,))#candidate|3269|(36,)|var|int16
call_3267 = relay.TupleGetItem(func_377_call(relay.reshape(var_3268.astype('int16'), []), relay.reshape(var_3269.astype('int16'), [12, 3, 1]), ), 0)
call_3270 = relay.TupleGetItem(func_381_call(relay.reshape(var_3268.astype('int16'), []), relay.reshape(var_3269.astype('int16'), [12, 3, 1]), ), 0)
func_377_call = mod.get_global_var('func_377')
func_381_call = mutated_mod.get_global_var('func_381')
call_3287 = relay.TupleGetItem(func_377_call(relay.reshape(var_3268.astype('int16'), []), relay.reshape(call_3267.astype('int16'), [12, 3, 1]), ), 0)
call_3288 = relay.TupleGetItem(func_381_call(relay.reshape(var_3268.astype('int16'), []), relay.reshape(call_3267.astype('int16'), [12, 3, 1]), ), 0)
func_2412_call = mod.get_global_var('func_2412')
func_2414_call = mutated_mod.get_global_var('func_2414')
call_3297 = relay.TupleGetItem(func_2412_call(), 0)
call_3298 = relay.TupleGetItem(func_2414_call(), 0)
uop_3301 = relay.asin(call_3267.astype('float64')) # shape=(12, 3, 1)
uop_3303 = relay.asin(call_3270.astype('float64')) # shape=(12, 3, 1)
output = relay.Tuple([call_3260,var_3268,var_3269,call_3287,call_3297,uop_3301,])
output2 = relay.Tuple([call_3261,var_3268,var_3269,call_3288,call_3298,uop_3303,])
func_3308 = relay.Function([var_3268,var_3269,], output)
mod['func_3308'] = func_3308
mod = relay.transform.InferType()(mod)
var_3309 = relay.var("var_3309", dtype = "int16", shape = ())#candidate|3309|()|var|int16
var_3310 = relay.var("var_3310", dtype = "int16", shape = (36,))#candidate|3310|(36,)|var|int16
output = func_3308(var_3309,var_3310,)
func_3311 = relay.Function([var_3309,var_3310,], output)
mutated_mod['func_3311'] = func_3311
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3358 = relay.var("var_3358", dtype = "uint64", shape = (1, 11, 3))#candidate|3358|(1, 11, 3)|var|uint64
var_3359 = relay.var("var_3359", dtype = "uint64", shape = (3, 11, 3))#candidate|3359|(3, 11, 3)|var|uint64
bop_3360 = relay.minimum(var_3358.astype('uint64'), var_3359.astype('uint64')) # shape=(3, 11, 3)
output = bop_3360
output2 = bop_3360
func_3368 = relay.Function([var_3358,var_3359,], output)
mod['func_3368'] = func_3368
mod = relay.transform.InferType()(mod)
var_3369 = relay.var("var_3369", dtype = "uint64", shape = (1, 11, 3))#candidate|3369|(1, 11, 3)|var|uint64
var_3370 = relay.var("var_3370", dtype = "uint64", shape = (3, 11, 3))#candidate|3370|(3, 11, 3)|var|uint64
output = func_3368(var_3369,var_3370,)
func_3371 = relay.Function([var_3369,var_3370,], output)
mutated_mod['func_3371'] = func_3371
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2395_call = mod.get_global_var('func_2395')
func_2397_call = mutated_mod.get_global_var('func_2397')
call_3415 = func_2395_call()
call_3416 = func_2395_call()
var_3440 = relay.var("var_3440", dtype = "float32", shape = (15, 4, 16))#candidate|3440|(15, 4, 16)|var|float32
bop_3441 = relay.less(call_3415.astype('bool'), relay.reshape(var_3440.astype('bool'), relay.shape_of(call_3415))) # shape=(15, 4, 16)
bop_3444 = relay.less(call_3416.astype('bool'), relay.reshape(var_3440.astype('bool'), relay.shape_of(call_3416))) # shape=(15, 4, 16)
output = relay.Tuple([bop_3441,])
output2 = relay.Tuple([bop_3444,])
func_3448 = relay.Function([var_3440,], output)
mod['func_3448'] = func_3448
mod = relay.transform.InferType()(mod)
mutated_mod['func_3448'] = func_3448
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3449 = relay.var("var_3449", dtype = "float32", shape = (15, 4, 16))#candidate|3449|(15, 4, 16)|var|float32
func_3448_call = mutated_mod.get_global_var('func_3448')
call_3450 = func_3448_call(var_3449)
output = call_3450
func_3451 = relay.Function([var_3449], output)
mutated_mod['func_3451'] = func_3451
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1435_call = mod.get_global_var('func_1435')
func_1436_call = mutated_mod.get_global_var('func_1436')
call_3462 = func_1435_call()
call_3463 = func_1435_call()
func_1140_call = mod.get_global_var('func_1140')
func_1142_call = mutated_mod.get_global_var('func_1142')
call_3468 = relay.TupleGetItem(func_1140_call(), 0)
call_3469 = relay.TupleGetItem(func_1142_call(), 0)
func_2236_call = mod.get_global_var('func_2236')
func_2239_call = mutated_mod.get_global_var('func_2239')
var_3473 = relay.var("var_3473", dtype = "float32", shape = (960,))#candidate|3473|(960,)|var|float32
call_3472 = func_2236_call(relay.reshape(var_3473.astype('float32'), [15, 4, 16]))
call_3474 = func_2236_call(relay.reshape(var_3473.astype('float32'), [15, 4, 16]))
const_3477 = relay.const([[[False,True,False,False,True,False,True,False,False,False,True,True,True,True,True,True],[False,False,True,False,False,False,True,False,False,True,False,True,False,False,True,True],[False,True,True,True,True,False,False,True,True,True,True,False,False,False,True,False],[True,False,True,True,False,False,True,False,True,True,True,False,True,True,True,True]],[[False,False,True,False,False,True,True,True,False,False,False,False,True,True,True,False],[False,False,True,False,False,False,True,False,True,False,False,False,True,True,False,False],[True,True,False,True,False,True,True,False,False,True,False,True,False,True,True,False],[True,False,True,False,False,False,False,True,False,False,True,False,True,True,False,False]],[[False,False,True,False,True,False,False,True,True,True,False,False,False,True,False,False],[True,True,False,True,True,False,False,False,False,False,False,True,True,False,True,False],[False,False,False,True,True,True,True,False,False,True,False,False,True,True,False,False],[False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False]],[[True,False,True,False,True,False,False,True,False,True,False,True,False,False,True,False],[True,True,False,True,False,False,False,False,False,True,False,False,False,False,False,True],[True,False,True,False,False,True,False,False,False,False,True,False,False,True,True,True],[False,True,True,False,False,True,True,False,False,True,True,False,False,True,True,True]],[[True,False,True,False,False,True,False,False,True,False,True,False,True,False,True,True],[True,False,False,True,True,True,False,False,False,True,False,False,False,False,True,False],[False,True,False,False,False,False,True,False,False,False,False,True,False,True,True,True],[False,True,True,True,False,True,True,False,False,False,True,False,False,False,False,False]],[[True,False,True,False,True,False,False,True,False,False,True,False,True,False,True,True],[True,False,True,True,True,False,True,True,False,False,False,False,True,False,True,False],[True,False,False,False,False,False,True,False,False,False,False,False,False,True,True,True],[False,False,False,True,True,False,True,True,False,True,False,True,True,True,False,False]],[[True,False,False,True,True,False,True,True,False,True,True,True,False,True,False,False],[True,True,False,False,True,True,False,True,False,False,True,True,True,True,False,False],[True,False,True,False,False,False,False,True,True,True,False,True,False,False,False,False],[True,False,False,False,True,False,False,True,False,True,False,True,False,False,True,True]],[[True,False,False,True,False,False,False,True,True,False,True,False,True,True,False,False],[True,False,True,False,True,True,True,True,False,True,True,False,False,False,True,True],[True,True,False,True,True,True,True,True,True,False,True,False,True,True,True,False],[True,False,False,False,True,True,False,True,False,True,True,False,True,False,True,False]],[[False,False,False,True,True,True,False,False,True,True,True,False,False,False,False,False],[False,False,False,True,True,False,False,True,True,True,False,True,True,True,True,True],[True,True,True,False,False,True,True,True,True,False,True,True,False,True,True,False],[True,False,True,False,False,True,False,False,False,False,True,True,True,False,True,True]],[[False,False,True,False,True,False,False,False,False,True,False,False,True,True,False,False],[True,True,True,False,False,True,False,False,True,True,False,False,True,True,True,True],[True,True,False,False,True,False,True,False,True,True,False,False,False,True,True,False],[False,False,False,True,True,False,True,False,True,True,False,False,False,False,False,True]],[[True,False,False,False,False,True,False,True,False,True,False,False,False,True,False,False],[True,False,True,False,False,True,False,True,False,False,False,True,False,False,False,True],[False,False,False,False,True,False,True,True,True,True,False,True,False,False,False,True],[True,True,True,True,False,True,True,True,False,True,False,False,True,False,False,True]],[[True,False,True,False,False,False,False,False,False,False,True,False,False,True,False,True],[True,True,True,True,True,False,False,True,True,False,True,False,True,True,True,False],[True,False,False,False,False,False,False,False,False,True,True,True,True,True,False,False],[False,True,True,True,True,False,False,False,False,False,False,True,True,True,True,True]],[[True,False,True,False,False,True,False,True,False,True,False,True,False,False,True,True],[False,True,False,True,True,True,False,True,True,False,True,False,False,False,True,True],[False,False,True,True,True,False,False,False,True,False,True,False,False,True,True,False],[False,True,False,True,False,False,False,True,False,True,False,False,False,True,False,False]],[[False,True,True,True,True,True,True,True,True,True,True,False,False,False,False,False],[True,False,True,False,False,True,True,True,True,True,True,True,True,True,True,True],[True,True,False,False,False,False,True,False,True,False,False,True,False,False,True,False],[True,False,False,True,True,True,False,False,True,False,True,False,True,True,True,False]],[[False,True,True,False,True,False,False,False,True,False,True,True,True,False,True,False],[False,True,True,False,True,False,False,False,False,False,False,True,True,True,False,True],[False,True,True,False,True,False,False,False,False,False,False,True,False,True,True,True],[True,True,True,False,True,True,False,True,True,False,False,False,True,False,True,True]]], dtype = "bool")#candidate|3477|(15, 4, 16)|const|bool
bop_3478 = relay.bitwise_or(call_3472.astype('int64'), relay.reshape(const_3477.astype('int64'), relay.shape_of(call_3472))) # shape=(15, 4, 16)
bop_3481 = relay.bitwise_or(call_3474.astype('int64'), relay.reshape(const_3477.astype('int64'), relay.shape_of(call_3474))) # shape=(15, 4, 16)
var_3485 = relay.var("var_3485", dtype = "bool", shape = (15, 4, 16))#candidate|3485|(15, 4, 16)|var|bool
bop_3486 = relay.right_shift(call_3472.astype('uint32'), relay.reshape(var_3485.astype('uint32'), relay.shape_of(call_3472))) # shape=(15, 4, 16)
bop_3489 = relay.right_shift(call_3474.astype('uint32'), relay.reshape(var_3485.astype('uint32'), relay.shape_of(call_3474))) # shape=(15, 4, 16)
output = relay.Tuple([call_3462,call_3468,var_3473,bop_3478,bop_3486,])
output2 = relay.Tuple([call_3463,call_3469,var_3473,bop_3481,bop_3489,])
func_3508 = relay.Function([var_3473,var_3485,], output)
mod['func_3508'] = func_3508
mod = relay.transform.InferType()(mod)
mutated_mod['func_3508'] = func_3508
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3508_call = mutated_mod.get_global_var('func_3508')
var_3510 = relay.var("var_3510", dtype = "float32", shape = (960,))#candidate|3510|(960,)|var|float32
var_3511 = relay.var("var_3511", dtype = "bool", shape = (15, 4, 16))#candidate|3511|(15, 4, 16)|var|bool
call_3509 = func_3508_call(var_3510,var_3511,)
output = call_3509
func_3512 = relay.Function([var_3510,var_3511,], output)
mutated_mod['func_3512'] = func_3512
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2798_call = mod.get_global_var('func_2798')
func_2800_call = mutated_mod.get_global_var('func_2800')
call_3524 = relay.TupleGetItem(func_2798_call(), 0)
call_3525 = relay.TupleGetItem(func_2800_call(), 0)
func_1497_call = mod.get_global_var('func_1497')
func_1498_call = mutated_mod.get_global_var('func_1498')
call_3538 = relay.TupleGetItem(func_1497_call(), 0)
call_3539 = relay.TupleGetItem(func_1498_call(), 0)
uop_3541 = relay.cos(call_3538.astype('float64')) # shape=(11, 13, 7)
uop_3543 = relay.cos(call_3539.astype('float64')) # shape=(11, 13, 7)
output = relay.Tuple([call_3524,uop_3541,])
output2 = relay.Tuple([call_3525,uop_3543,])
func_3544 = relay.Function([], output)
mod['func_3544'] = func_3544
mod = relay.transform.InferType()(mod)
output = func_3544()
func_3545 = relay.Function([], output)
mutated_mod['func_3545'] = func_3545
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2870_call = mod.get_global_var('func_2870')
func_2871_call = mutated_mod.get_global_var('func_2871')
call_3577 = relay.TupleGetItem(func_2870_call(), 2)
call_3578 = relay.TupleGetItem(func_2871_call(), 2)
func_2412_call = mod.get_global_var('func_2412')
func_2414_call = mutated_mod.get_global_var('func_2414')
call_3584 = relay.TupleGetItem(func_2412_call(), 0)
call_3585 = relay.TupleGetItem(func_2414_call(), 0)
func_1380_call = mod.get_global_var('func_1380')
func_1385_call = mutated_mod.get_global_var('func_1385')
const_3594 = relay.const([[2.286128,2.949092,2.037799,6.495379,-2.398927,-9.696317,4.201871,-9.656989,7.672666,-5.293749,-0.698516,7.760380,-7.838581,-4.575608,-4.016091,-3.313515,4.081549,-3.328736,6.248325,1.096635,5.205672,-0.673808,3.482008,-8.194834,-8.565846,3.252631,-9.450203,-2.642553,-6.132995,8.725353,0.392565,-0.521420,4.368243,2.226908,-3.861733,-7.738726,-5.505507,-3.098924,0.436853,-8.759891,2.887264,-1.451327,-4.140683,5.279645,-6.001881,3.964369,-4.028536,-6.524375,-7.844560,-5.829673,-5.547472,-4.005484,-0.571352,-7.641279,1.031744,8.954475,3.260021,-8.319904,3.341575,-5.753030,-3.418024,8.718458,8.332416,-0.439587,2.355495,9.308161,7.708019,-1.055474,-8.956378,-4.950076,2.119666,3.866713,1.069672,-4.617019,3.914610,-9.104963,-6.480930,-4.557542,-1.886079,3.270750,6.749549,2.775928,-0.735178,-9.210237,2.866743,1.782165,8.395083,9.125824,-3.957611,5.988348,-2.071371,-6.414014,4.927046,-4.551428,9.762701,5.064316,-5.847025,-2.201209,-4.474736,-7.907753,6.437380,-2.018045,-7.889669,0.069739,1.529758,-1.785906,5.728102,-1.645654,9.507835,-5.881725,-2.608022,8.981775,-5.196546,4.058543,1.344627,-2.101168,3.274771,9.613091,-0.609138,6.891824,2.864637,5.930012,-0.214548,0.336629,4.231809,-8.600399,4.135713,-9.656867,5.076931,-4.245359,0.281691,7.263770,8.190969,-5.554710,-1.085094,8.403475,7.274687,-1.058159,-0.759257,5.971234,9.512803,9.848394,-0.739557,-4.496170,3.469037,-4.086061,-0.176961,-0.073323,-8.347168,1.555408,-3.416207,-6.897359,-8.035238,8.400927,-9.192837,-8.111510,-8.717572,-5.788336,0.541538,3.805528,0.922606,-6.831795,5.996581,5.679499,7.524702,-1.953821,4.737789,-8.022669,6.440223,-2.680438,-6.127722,2.436866,-8.465776,1.857490,0.808208,-4.450651,-2.667723,-2.199271,7.088604,9.031557,-5.962124,-0.752983,-9.877546,6.184051,-8.669917,3.903873,-3.989462,-9.251413,-3.764676,7.938790,-6.943488,-6.852608,-6.161093,-3.543705,-9.534344,-7.235844,-7.949568,-9.361659,7.241360,-2.368834,1.191092,3.124821,0.551707,-3.498258,6.627487,4.425565,-2.738037,2.150417,-2.693068,-1.992286,4.237212,3.222799,-3.770512,4.813445,-3.562822,6.606955,0.410996,5.294609,-0.428763,1.901752,8.410885,4.346305,-9.495805,-4.986243,3.464529,-5.168754,-7.398062,-5.142520,3.123132,-7.757708,6.101456,-0.134318,-8.249301,9.366449,0.969271,2.460585,9.218783,-0.631822,4.350598,-5.426385,-5.178333,9.042025,7.173746,0.011800,4.327772,-3.783816,9.526850,-0.140534,-2.508770,2.945711,-4.565772,2.415154,0.041296,9.942746,-5.704980,3.601080,-3.451988,3.929121,-9.825408,7.375977,1.444474,0.510562,-9.367419,-6.026744,2.749715,-0.528570,-8.292128,-5.467274,-0.916959,-7.416663,4.488623,3.439496,3.382996,2.338752,6.622150,7.407780,-9.062757,5.479312,-4.302921,-3.778700,8.103756,6.035462,-2.022988,-6.297044,-9.657270,2.614884,-7.317464,4.780202,-2.755593,-2.097656,1.732026,-1.127864,-5.427855,-9.769160,4.773590,-1.564836,-2.028149,7.386690,1.175490,1.554175,-0.589370,-1.923761,6.527693,-3.367443,-6.062778,7.029904,7.345735,-4.060644,5.602836,-6.264877,4.620931,-9.169913,0.473915,-1.270595,4.793485,-5.160538,-5.757420,-9.804977,-8.869754,7.177964,9.764078,3.140794,-1.853087,-3.552676,-6.262450,3.013934,-3.481525,8.888833,7.231915,-7.076473,2.950685,-1.082287,0.982480,3.689729,-5.571996,1.152581,4.339186,-3.733032,-0.018909,-3.314771,5.617504,-3.498394,9.342839,4.244093,0.201913,1.073225,-1.588389,-5.037937,-2.149345,-7.589810,3.196451,8.939367,-7.302139,-8.861918,-0.718209,7.960481,-6.918090,1.415542,-0.534646,-3.823719,8.071425,-9.723734,-6.636303,8.626226,8.116421,4.171829,9.031258,7.779766,-5.586966,-8.090795,-2.336864,-5.102704,5.271095,-2.485906,9.646699,2.309228,-0.835088,-4.012417,8.127597,-5.392056,1.450066,5.364310,-1.867631,-2.866819,-2.877561,0.894789,9.731949,-1.156990,-8.771480,-2.490273,5.455280,-0.853001,9.098278,-9.801989,-7.774158,7.480113,-5.973448,5.890487,-2.160239,1.049237,-4.484821,4.600853,1.016155,1.140302,1.352629,5.856008,0.110190,-4.898004,-7.480060,9.276049,6.974317,5.651766,6.894344,-2.017384,-0.275209,5.298126,3.054044,-0.770180,-7.301281,-5.168437,8.871447,-2.504751,9.555732,-7.542187,-5.838076,-7.447801,-1.678090,6.866167,-7.242628,9.387389,-9.792701,-1.804654,-7.212917,-1.504776,-6.863448,-3.324363,-8.771973,-9.432684,6.463843,5.142061,1.144255,-8.641455,8.989461,4.978022,2.072786,6.316912,2.270150,9.989787,-0.649900,-5.155144,-3.791084,5.817600,-9.448360,-3.079887,-7.062333,3.377474,-8.607190,6.157375,0.299144,7.450804,-0.519676,-8.413594,-9.866097,3.330641,3.954620,1.543296,-4.802468,-0.238279,3.012931,-8.031296,6.142854,3.758251,2.855423,5.792775,1.876264,-4.297671,4.896972,-9.617612,-0.608389,3.885207,2.105581,-1.275831,5.938863,-5.257819,0.746538,-8.096288,-4.952534,-8.192874,-2.800485,9.223171,3.677337,6.728934,-9.300321,-7.027245,5.644110,8.548551,0.677476,-1.021090,-0.956619,5.699868,-6.139237,-1.327014,9.022566,-1.493880,1.104414,7.080950,8.735503,4.618625,-7.558546,6.936734,4.908120,9.357715,-1.517439,5.787741,-1.794613,-5.395615,-0.306609,-6.033472,-0.301130,-8.313714,-9.730093,-3.500334,-0.694329,1.815243,5.614524,8.075672,6.716554,9.383013,-4.769131,8.154930,3.262456,9.998948,-6.152699,5.158181,5.431247,-0.380507,-9.622478,4.610070,3.160924,2.097545,2.356969,3.019163,9.573767,-5.482302,-4.467428,8.333074,-9.873861,0.810751,-8.094114,1.496450,-1.679506,4.827886,-3.332588,-9.804993,5.623097,-1.856725,-6.350210,-3.878168,1.508612,6.614789,-6.979138,1.391540,-1.454230,3.564634,-6.547639,-4.366745,3.183101,2.234274,-5.090972,9.293876,5.049255,9.049622,7.655105,-4.166301,-2.975833,-7.874949,-5.619511,7.580547,3.853457,8.947086,5.849520,-3.953082,8.222877,-5.500405,9.088892,7.371730,-8.573677,-4.159015,-2.890597,-6.285084,9.361776,1.850123,-9.550363,-2.012631,-7.299768,8.341886,9.626549,-5.042416,5.871462,-8.427614,-9.052682,-2.359569,-8.148049,-0.157646,2.063104,-0.724088,-9.465945,-6.055375,-6.779186,-9.440942,-4.675088,3.854867,0.738236,-4.628584,-3.908589,-0.863235,-0.707250,0.689934,5.728039,-9.054349,-7.123627,6.763962,-2.857552,-6.503544,-0.435352,9.954644,-8.843109,-3.127307,-1.898145,1.676486,-2.845936,8.787985,-9.148416,1.939265,2.431168,-7.300001,-8.384685,-3.781535,5.051942,-2.225410,1.648285,-4.429938,-2.787867,3.475536,1.088122,9.666941,-8.044678,-0.660633,-2.989356,3.229524,4.197941,9.832053,7.175637,7.803605,-1.015163,8.044697,0.460553,-8.726109,-7.590820,1.916191,-4.347320,4.950210,9.327115,8.347936,-0.281784,4.661792,-2.935353,2.137429,-8.913144,-8.246911,-3.227400,-0.459665,0.745837,9.935621,3.541018,5.573366,-0.522157,-3.488087,-5.640666,7.893036,-2.123504,9.147257,8.498216,0.115573,5.405368,8.726186,9.026936,8.454937,-6.079109,-8.092134,0.520692,6.791430,5.488362,-4.996160,8.043613,-8.127976,-7.103219,-8.703400,-5.656827,-3.274696,3.241650,-9.990602,0.565229,6.025998,-5.610742,2.959187,3.266411,6.849095,6.519017,-6.707367,0.345503,-6.050942,-7.819913,-9.081272,-1.621308,-4.833371,-7.175662,-7.836670,9.671835,4.333428,-2.755921,3.796296,4.115984,-4.264550,-9.429552,1.951125,3.491010,-8.485899,-8.032835,-4.564132,2.867073,-7.067643,9.586735,9.069487,-6.777370,4.764345,-7.984274,-7.239831,7.189887,-8.199854,3.866018,-6.549600,1.080135,8.633148,8.142404,1.234875,-6.583765,-9.048849,-8.165441,-7.624523,-0.330507,9.096438,9.081842,-4.296003,-8.503607,-3.604322,-2.812062,-2.502586,3.172092,7.237661,-3.668502,3.918475,-0.206178,-0.973032,-5.222663,5.500742,-6.520009,2.279125,-9.993003,7.466933,-7.678370,-2.863268,-0.059129,-7.740087,-3.839454,-9.875289,-0.417152,-5.893504,7.296229,-5.136206,1.105070,-0.632982,-9.083721,9.331026,5.625706,-0.014816,7.925018,-9.655998,2.764320,2.666246,-7.963422,-0.376092,-2.776392,6.680408,-2.815181,7.712520,4.722332,0.138168,5.161419,-2.104992,2.353423,-1.314975,4.313594,-5.864425,4.019035,1.650491,4.216689,4.917351,-6.158211,9.511707,-2.400318,-9.884471,-9.489464,6.037465,0.041579,-5.687750,-7.280412,4.370514,6.107997,6.669375,5.856755,-4.192623,-2.143194,-8.729740,-4.246259,3.367219,-4.932572,-4.305336,-1.646652,-8.825570,2.093958,-8.629979,1.711795,-9.946683,-4.833245,-5.980824,-3.845008,-1.089267,-6.307297,7.871355,1.546828,9.078474,-5.812092,-7.405852,3.257232,-4.235866,-6.774526,7.875087,-3.959015,-3.205257,6.850193,5.562632,-2.176202,-8.635445,-4.528989,1.087441,6.335293,-7.192276,9.173457,-3.914479,7.705188,4.359871,3.009175,-2.902718,-7.328907,-8.006026,8.015039,2.495185,-8.453639,-5.049029,4.552515,-7.539828,-0.578483,3.004133,8.479686,-6.469570,-7.952983,-1.352438,-8.731647,-0.115178,-7.025767,-4.091963,-1.703788,6.942720,-8.173614,2.083320,7.126711,-6.171779,-4.794456,7.100051,9.377003,5.545108,-2.636775,3.371916,-2.631976,3.794899,5.316012,-6.259329,-3.631108,-7.037497,6.009001,-7.978054,2.994966,-1.999238,-7.153298,4.934313,9.787720,-6.349459,4.629055,2.277673,5.502028,-5.837091,-0.319705,-9.466991,-7.308748,9.128777,-8.634795,-2.229906,-7.363750,-8.218922,9.410403,-3.277924,-8.094487,-3.060140,8.173352,5.153481,-2.005124,4.869756,-2.222925,2.319903,-2.336360,-1.207734,5.726593,-8.457174,0.750357,-0.485378,-3.622533,7.566433,0.468118,-4.027822,2.137867,8.318129,5.964847,3.852524,-3.240941,-0.467728,7.914446,-5.209547,-6.165696,0.838645,8.026254,-0.359182,-3.055485,-8.827545,2.605253,-0.243084,-4.398626,-4.415009,-3.346238,3.048645,7.549506,6.366768,-9.109824,4.171238,-7.612757,-1.835649,-3.907358,-3.822925,-5.342464,8.402878,6.836641,3.126632,3.551278,-3.137418,2.453073,7.795858,8.158546,7.290128,-1.094281,-1.242691,0.345525,-7.542066,4.407757,1.252886,9.713050,4.777722,-5.567778,-2.014005,3.142558,-4.760224,-6.609150,9.799099,-6.205530,4.584752,4.962328,-5.990164,-8.227652,-9.556399,7.161882,6.387422,-7.126705,4.229546,7.365634,9.770109,-0.608059,1.658978,0.466649,3.789054,-4.525003,-0.624594,-0.021282,-2.563546,3.135450,9.178042,-7.297315,4.343987,6.087066,-4.720554,-8.205863,8.801263,9.509483,4.577987,9.047912,-0.422690,6.259476,8.679328,9.789197,-5.442184,5.290420,3.490582,-5.238402,-1.338353,-2.529253,0.550105,-3.068490,3.366238,1.530072,-9.034114,0.096818,-1.382320,6.045869,9.725900,-7.424084,9.230345,2.395357,9.952500,2.158900,3.790867,-6.612914,-2.698977,-9.401475,-2.603405,-7.882613,-7.850078,-0.046359,-9.556519,3.772558,-4.361807,9.127988,2.379254,9.359712,5.717922,-6.607528,-7.694275,3.322478,-5.799154,-5.318639,3.306374,8.196495,9.058508,6.364669,-0.220146,1.653780,-4.567628,-1.306597,8.686638,-4.931018,0.688237,0.489442,-3.071335,-7.328708,-2.549882,6.294880,-7.219911,-0.059336,-9.931283,3.763511,-1.052639,-0.753103,-8.837565,-2.195721,-5.514857,-6.621706,8.719855,6.696832,-9.262693,-6.492833,-5.245698,-5.590237,5.382283,-5.900615,-7.119846,-2.453302,-9.585390,5.092186,5.361639,-8.475624,2.551860,3.199249,4.705155,-8.372676,6.973906,-0.092569,-5.442355,-2.606541,1.984111,-6.966938,-1.412632,-8.986494,7.087161,8.753334,3.331296,-3.819868,-4.175339,-2.883678,-8.580970,7.744003,4.849028,2.999486,8.940260,3.282797,6.980214,-9.565790,-7.402286,-9.477402,5.720915,8.674261,-1.459125,4.801269,4.232114,-7.057623,-1.269804,4.585198,8.780179,2.374836,-2.506481,-1.818991,-8.100025,-1.619538,0.636437,-6.336646,-9.905972,-0.592437,4.902991,-4.529159,5.582371,-3.278930,-4.619307,0.556039,4.556103,-2.244191,-4.059004,6.141576,-8.421167,5.248615,-0.413392,-1.702127,7.196767,9.836237,-4.389618,-7.534960,-2.991922,1.072729,-3.559517,9.039029,4.141776,-8.045384,-1.482255,4.163181,8.965509,-6.053689,-9.406109,-5.516659,3.228027,1.296647,0.105183,4.761456,-8.801848,4.402128,-5.732834,-6.406607,-8.819743,6.801409,-7.246919,9.377091,9.760145,-6.124469,-0.783580,-4.191305,-6.227095,0.901301,9.950963,-2.113288,5.611576,-0.038628,-3.368027,-0.233957,0.183614,7.020736,-8.941500,6.915002,-2.250223,0.162793,5.282501,4.441100,3.314439,5.315381,4.244930,7.957605,3.715412,-9.278862,-4.772824,5.500103,-9.404909,-2.536001,1.649308,7.340148,4.383874,9.082092,-1.463523,-6.637471,0.446289,-5.404868,3.594394,-0.088992,1.523914,-1.923273,3.538657,-2.567000,-6.728613,-4.006259,-3.643711,-9.130414,-0.764701,-2.877136,-9.901793,7.783830,8.105568,-4.774238,6.681763,9.229641,-1.180373,-5.183571,0.427973,0.814350,6.855636,-8.609704,1.179792,3.960980,-7.303090,-1.134198,7.324392,-8.372368,1.307230,8.989537,7.853119,-6.569506,8.689626,5.474638,3.398382,-4.015906,-1.944431,-5.813018,8.779714,-5.082918,-8.477812,-7.884681,-8.818619,-8.236108,-4.478503,-4.246748,-7.902684,3.686982,6.867197,2.435722,1.014902,-0.066769,-7.379097,-3.637652,-5.641156,6.308518,5.393444,-0.224662,-8.188653,-6.587549,8.557216,9.922926,2.843876,1.820639,4.219102,6.252421,-6.611443,8.644966,-6.212221,4.172758,-3.757314,8.491405,-5.902409,0.318555,-6.374420,6.930495,-6.648431,-4.144863,5.127601,-1.276623,-4.508025,-3.711265,5.694918,2.225418,4.312256,7.143740,5.774529,5.396407,-5.955835,-4.999823,-1.832020,-0.381498,-3.214272,-8.502056,-1.846862,3.722353,-2.034504,-8.228734,7.294575,-1.206736,-6.902728,-0.467765,-3.764635,1.251383,-8.336408,-3.379935,-8.390314,3.857721,8.434237,-3.260955,-2.420338,-7.798643,2.805379,8.944027,-3.408410,1.420874,7.449187,-8.666098,-2.308625,-4.081487,9.435981,6.133265,-4.248756,4.454290,2.279059,2.926744,1.591397,-4.091339,-5.753578,4.439009,6.954886,8.893212,-5.586539,6.747627,-3.007088,2.787871,-1.565793,8.299971,7.939913,-4.543559,-9.737229,-0.805974,4.765700,5.824041,-7.883833,-9.891876,4.909043,-5.506747,9.387680,-6.621154,-5.567344,9.046491,4.265753,1.563089,0.666139,1.156489,6.796388,6.811516,-7.116975,2.662986,1.277265,4.718061,9.523313,-9.393619,1.613276,-9.837068,-2.729207,-2.211250,-0.571900,-1.251112,2.505640,-9.854826,-3.378557,3.928916,-6.524521,2.904967,-5.805450,-1.925215,9.920071,-7.417139,-5.980892,-8.481282,-9.428933,-9.092709,-5.887384,8.509346,-9.560434,-8.005061,6.712200,4.833795,-7.488795,-1.601413,5.817309,4.196133,1.294120,9.275490,-0.277385,1.496419,-2.908128,-5.955078,-9.733782,-0.868656,0.959752,6.865179,-7.733535,-4.261922,-9.537357,4.575102,2.406331,-5.302705,-0.819960,-1.936805,6.143923,-9.307373,7.063579,-8.682682,-4.625727,-6.902732,8.636313,-1.035440,6.906243,2.496720,6.759859,8.852995,3.378720,-2.517594,-1.870240,-1.463330,-7.490704,1.499492,4.507895,9.605865,7.756759,1.772692,-1.014793,-7.271324,-3.752273,1.175263,1.372567,2.386149,-9.004649,-2.905994,-1.264657,-3.881808,5.248724,0.371915,7.234036,-1.810254,-4.073072,4.372772,-6.168120,-0.628499,3.945261,-9.404716,9.628364,8.378682,3.395627,-3.619556,6.020061,-5.279925,-4.981329,3.588562,2.442568,-0.539196,-1.338558,-5.748021,-9.141316,9.950516,-7.943387,-4.414799,7.572685,8.006364,9.423321,4.175545,-5.397197,-3.578618,1.239200,-9.590875,7.594422,-7.577409,-3.475212,-5.500737,-5.109515,8.222371,-1.103298,-7.087697,1.432280,-1.498215,8.905719,4.967303,-6.774431,-8.828275,-2.148543,-5.998789,-4.755415,8.554713,1.510301,1.185346,7.262476,-4.233750,-2.230093,-4.147766,-6.604303,-4.263292,-2.003983,3.547652,6.759153,-7.153382,-2.429291,-8.887567,0.213773,9.852058,1.481541,-0.306216,3.821041,-5.694102,6.834063,-2.764368,-6.015632,0.346654,-1.831659,4.996856,9.545923,3.600250,-6.132249,-9.340101,2.572548,-3.863523,-8.828188,-5.224893,5.841506,0.267842,0.088024,-5.731677,-1.541552,-7.302163,-2.389145,7.416194]], dtype = "float32")#candidate|3594|(1, 1573)|const|float32
call_3593 = relay.TupleGetItem(func_1380_call(relay.reshape(const_3594.astype('float32'), [11, 13, 11]), relay.reshape(const_3594.astype('float32'), [11, 13, 11]), relay.reshape(call_3577.astype('float64'), [14, 3]), ), 0)
call_3595 = relay.TupleGetItem(func_1385_call(relay.reshape(const_3594.astype('float32'), [11, 13, 11]), relay.reshape(const_3594.astype('float32'), [11, 13, 11]), relay.reshape(call_3577.astype('float64'), [14, 3]), ), 0)
bop_3598 = relay.minimum(call_3593.astype('uint8'), relay.reshape(const_3594.astype('uint8'), relay.shape_of(call_3593))) # shape=(11, 13, 11)
bop_3601 = relay.minimum(call_3595.astype('uint8'), relay.reshape(const_3594.astype('uint8'), relay.shape_of(call_3595))) # shape=(11, 13, 11)
output = relay.Tuple([call_3577,call_3584,bop_3598,])
output2 = relay.Tuple([call_3578,call_3585,bop_3601,])
func_3602 = relay.Function([], output)
mod['func_3602'] = func_3602
mod = relay.transform.InferType()(mod)
mutated_mod['func_3602'] = func_3602
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3602_call = mutated_mod.get_global_var('func_3602')
call_3603 = func_3602_call()
output = call_3603
func_3604 = relay.Function([], output)
mutated_mod['func_3604'] = func_3604
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2109_call = mod.get_global_var('func_2109')
func_2111_call = mutated_mod.get_global_var('func_2111')
call_3645 = relay.TupleGetItem(func_2109_call(), 1)
call_3646 = relay.TupleGetItem(func_2111_call(), 1)
func_3368_call = mod.get_global_var('func_3368')
func_3371_call = mutated_mod.get_global_var('func_3371')
var_3684 = relay.var("var_3684", dtype = "uint64", shape = (33,))#candidate|3684|(33,)|var|uint64
const_3685 = relay.const([7,3,-4,2,-5,4,-2,5,6,-9,-6,-7,1,-8,-1,10,1,-1,-2,2,8,7,4,-8,-5,1,5,10,2,-5,-8,-8,-10,-5,-3,-8,-4,-1,-6,-7,7,2,8,8,-1,10,7,10,6,-8,2,-2,-2,5,3,8,-1,-1,-4,8,1,-5,-5,-6,10,-2,1,-1,8,-10,1,2,-8,-3,-4,-6,-7,5,-7,5,-6,-2,-10,1,-8,-10,9,-10,-8,7,-4,-9,7,-4,-7,-4,5,-2,-6], dtype = "uint64")#candidate|3685|(99,)|const|uint64
call_3683 = func_3368_call(relay.reshape(var_3684.astype('uint64'), [1, 11, 3]), relay.reshape(const_3685.astype('uint64'), [3, 11, 3]), )
call_3686 = func_3368_call(relay.reshape(var_3684.astype('uint64'), [1, 11, 3]), relay.reshape(const_3685.astype('uint64'), [3, 11, 3]), )
func_2798_call = mod.get_global_var('func_2798')
func_2800_call = mutated_mod.get_global_var('func_2800')
call_3705 = relay.TupleGetItem(func_2798_call(), 0)
call_3706 = relay.TupleGetItem(func_2800_call(), 0)
uop_3707 = relay.log2(call_3645.astype('float64')) # shape=(10, 2, 14)
uop_3709 = relay.log2(call_3646.astype('float64')) # shape=(10, 2, 14)
uop_3711 = relay.sigmoid(uop_3707.astype('float32')) # shape=(10, 2, 14)
uop_3713 = relay.sigmoid(uop_3709.astype('float32')) # shape=(10, 2, 14)
output = relay.Tuple([call_3683,var_3684,const_3685,call_3705,uop_3711,])
output2 = relay.Tuple([call_3686,var_3684,const_3685,call_3706,uop_3713,])
func_3714 = relay.Function([var_3684,], output)
mod['func_3714'] = func_3714
mod = relay.transform.InferType()(mod)
mutated_mod['func_3714'] = func_3714
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3715 = relay.var("var_3715", dtype = "uint64", shape = (33,))#candidate|3715|(33,)|var|uint64
func_3714_call = mutated_mod.get_global_var('func_3714')
call_3716 = func_3714_call(var_3715)
output = call_3716
func_3717 = relay.Function([var_3715], output)
mutated_mod['func_3717'] = func_3717
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2680_call = mod.get_global_var('func_2680')
func_2681_call = mutated_mod.get_global_var('func_2681')
call_3724 = relay.TupleGetItem(func_2680_call(), 0)
call_3725 = relay.TupleGetItem(func_2681_call(), 0)
output = relay.Tuple([call_3724,])
output2 = relay.Tuple([call_3725,])
func_3733 = relay.Function([], output)
mod['func_3733'] = func_3733
mod = relay.transform.InferType()(mod)
output = func_3733()
func_3734 = relay.Function([], output)
mutated_mod['func_3734'] = func_3734
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3771 = relay.var("var_3771", dtype = "float32", shape = (3, 1, 15))#candidate|3771|(3, 1, 15)|var|float32
uop_3772 = relay.tan(var_3771.astype('float32')) # shape=(3, 1, 15)
output = uop_3772
output2 = uop_3772
func_3776 = relay.Function([var_3771,], output)
mod['func_3776'] = func_3776
mod = relay.transform.InferType()(mod)
var_3777 = relay.var("var_3777", dtype = "float32", shape = (3, 1, 15))#candidate|3777|(3, 1, 15)|var|float32
output = func_3776(var_3777)
func_3778 = relay.Function([var_3777], output)
mutated_mod['func_3778'] = func_3778
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3800 = relay.var("var_3800", dtype = "bool", shape = (12, 12, 14))#candidate|3800|(12, 12, 14)|var|bool
var_3801 = relay.var("var_3801", dtype = "bool", shape = (12, 12, 14))#candidate|3801|(12, 12, 14)|var|bool
bop_3802 = relay.logical_and(var_3800.astype('bool'), relay.reshape(var_3801.astype('bool'), relay.shape_of(var_3800))) # shape=(12, 12, 14)
uop_3808 = relay.asinh(bop_3802.astype('float32')) # shape=(12, 12, 14)
func_3368_call = mod.get_global_var('func_3368')
func_3371_call = mutated_mod.get_global_var('func_3371')
const_3827 = relay.const([10,-6,8,-1,-4,7,10,10,-9,5,-8,-5,-1,6,4,1,1,-10,-7,-5,3,-2,8,-8,-3,-7,8,-9,-10,6,8,-7,-5], dtype = "uint64")#candidate|3827|(33,)|const|uint64
const_3828 = relay.const([10,-2,2,8,3,8,-1,-8,-7,-9,6,3,3,1,9,-9,-10,5,-2,-5,-9,3,-10,-10,-10,5,4,-7,8,-2,-8,9,1,-3,7,10,-10,7,-3,-6,5,8,7,-6,-5,-5,1,-4,-8,-5,-2,-2,-7,-4,-7,5,10,-1,1,6,-8,-1,-5,-9,-10,9,-1,-6,-7,1,1,-5,-1,1,-6,8,-10,-10,3,-9,6,-7,-6,-5,5,8,-6,-8,3,-1,-6,4,-7,2,-6,3,8,10,2], dtype = "uint64")#candidate|3828|(99,)|const|uint64
call_3826 = func_3368_call(relay.reshape(const_3827.astype('uint64'), [1, 11, 3]), relay.reshape(const_3828.astype('uint64'), [3, 11, 3]), )
call_3829 = func_3368_call(relay.reshape(const_3827.astype('uint64'), [1, 11, 3]), relay.reshape(const_3828.astype('uint64'), [3, 11, 3]), )
output = relay.Tuple([uop_3808,call_3826,const_3827,const_3828,])
output2 = relay.Tuple([uop_3808,call_3829,const_3827,const_3828,])
func_3832 = relay.Function([var_3800,var_3801,], output)
mod['func_3832'] = func_3832
mod = relay.transform.InferType()(mod)
mutated_mod['func_3832'] = func_3832
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3832_call = mutated_mod.get_global_var('func_3832')
var_3834 = relay.var("var_3834", dtype = "bool", shape = (12, 12, 14))#candidate|3834|(12, 12, 14)|var|bool
var_3835 = relay.var("var_3835", dtype = "bool", shape = (12, 12, 14))#candidate|3835|(12, 12, 14)|var|bool
call_3833 = func_3832_call(var_3834,var_3835,)
output = call_3833
func_3836 = relay.Function([var_3834,var_3835,], output)
mutated_mod['func_3836'] = func_3836
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3544_call = mod.get_global_var('func_3544')
func_3545_call = mutated_mod.get_global_var('func_3545')
call_3838 = relay.TupleGetItem(func_3544_call(), 0)
call_3839 = relay.TupleGetItem(func_3545_call(), 0)
func_3308_call = mod.get_global_var('func_3308')
func_3311_call = mutated_mod.get_global_var('func_3311')
const_3853 = relay.const(7, dtype = "int16")#candidate|3853|()|const|int16
const_3854 = relay.const([-2,-1,10,9,8,4,9,-9,-6,-5,-2,-1,2,-8,-6,4,-5,-2,-8,-4,2,-8,-1,2,-1,2,-1,-6,9,-3,-9,2,4,1,-5,-8], dtype = "int16")#candidate|3854|(36,)|const|int16
call_3852 = relay.TupleGetItem(func_3308_call(relay.reshape(const_3853.astype('int16'), []), relay.reshape(const_3854.astype('int16'), [36,]), ), 2)
call_3855 = relay.TupleGetItem(func_3311_call(relay.reshape(const_3853.astype('int16'), []), relay.reshape(const_3854.astype('int16'), [36,]), ), 2)
bop_3856 = relay.floor_mod(const_3854.astype('float32'), const_3853.astype('float32')) # shape=(36,)
func_1848_call = mod.get_global_var('func_1848')
func_1850_call = mutated_mod.get_global_var('func_1850')
var_3860 = relay.var("var_3860", dtype = "float64", shape = (330,))#candidate|3860|(330,)|var|float64
call_3859 = relay.TupleGetItem(func_1848_call(relay.reshape(var_3860.astype('float64'), [330,])), 2)
call_3861 = relay.TupleGetItem(func_1850_call(relay.reshape(var_3860.astype('float64'), [330,])), 2)
const_3865 = relay.const([[[True,False,False,True,True,True,True],[False,False,True,False,False,False,True],[True,True,True,True,False,False,False],[False,True,True,False,False,False,False],[False,False,False,True,True,True,True],[False,False,False,True,True,True,True],[True,False,False,False,True,False,True],[True,False,True,False,False,True,False],[False,True,False,False,False,True,False]],[[True,False,True,True,False,True,False],[True,True,False,True,True,False,True],[False,False,True,True,True,False,True],[True,True,False,True,True,False,True],[True,True,True,False,True,False,True],[False,False,False,True,True,False,False],[False,False,False,False,True,True,True],[False,True,True,True,True,True,False],[False,True,True,True,True,True,True]],[[False,True,False,False,True,False,False],[False,False,False,False,True,False,False],[False,True,False,False,True,True,True],[False,False,True,False,True,False,True],[False,True,False,True,True,False,True],[False,True,True,True,True,False,True],[False,False,False,False,False,False,False],[True,True,True,True,True,False,True],[False,True,False,True,False,False,False]],[[True,False,True,False,True,True,True],[True,True,False,True,True,False,False],[True,False,False,False,True,False,True],[False,False,False,True,True,False,False],[False,False,False,True,True,True,True],[False,False,False,True,True,True,True],[True,True,True,False,False,True,True],[True,True,False,False,False,True,True],[True,True,True,True,False,True,True]],[[True,False,False,True,True,True,True],[False,False,False,True,True,True,False],[True,False,True,True,False,True,True],[False,False,False,True,False,True,True],[False,False,False,True,False,False,False],[True,True,True,False,True,True,True],[True,False,True,False,True,False,True],[True,False,False,True,False,False,False],[False,True,True,False,True,True,True]],[[False,False,False,True,True,True,True],[True,True,True,False,True,False,False],[False,True,False,True,True,False,False],[True,True,True,False,False,False,False],[False,False,False,False,False,False,True],[True,True,True,False,False,False,False],[False,False,True,False,True,True,False],[False,True,False,False,False,True,False],[True,False,False,True,False,False,True]],[[False,False,False,True,False,True,False],[False,True,False,False,False,True,True],[True,False,True,False,False,True,False],[False,True,False,True,True,False,False],[True,True,True,True,True,False,False],[True,True,False,False,True,True,False],[True,False,True,False,True,False,False],[True,False,False,True,True,False,True],[False,True,True,True,False,True,False]]], dtype = "bool")#candidate|3865|(7, 9, 7)|const|bool
bop_3866 = relay.floor_mod(call_3859.astype('float32'), relay.reshape(const_3865.astype('float32'), relay.shape_of(call_3859))) # shape=(7, 9, 7)
bop_3869 = relay.floor_mod(call_3861.astype('float32'), relay.reshape(const_3865.astype('float32'), relay.shape_of(call_3861))) # shape=(7, 9, 7)
uop_3897 = relay.sinh(bop_3856.astype('float64')) # shape=(36,)
bop_3904 = relay.add(const_3854.astype('int16'), relay.reshape(uop_3897.astype('int16'), relay.shape_of(const_3854))) # shape=(36,)
output = relay.Tuple([call_3838,call_3852,var_3860,bop_3866,bop_3904,])
output2 = relay.Tuple([call_3839,call_3855,var_3860,bop_3869,bop_3904,])
func_3914 = relay.Function([var_3860,], output)
mod['func_3914'] = func_3914
mod = relay.transform.InferType()(mod)
var_3915 = relay.var("var_3915", dtype = "float64", shape = (330,))#candidate|3915|(330,)|var|float64
output = func_3914(var_3915)
func_3916 = relay.Function([var_3915], output)
mutated_mod['func_3916'] = func_3916
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3934 = relay.var("var_3934", dtype = "int8", shape = (8, 13, 1))#candidate|3934|(8, 13, 1)|var|int8
var_3935 = relay.var("var_3935", dtype = "int8", shape = (8, 13, 2))#candidate|3935|(8, 13, 2)|var|int8
bop_3936 = relay.left_shift(var_3934.astype('int8'), var_3935.astype('int8')) # shape=(8, 13, 2)
var_3939 = relay.var("var_3939", dtype = "int8", shape = (8, 13, 2))#candidate|3939|(8, 13, 2)|var|int8
bop_3940 = relay.divide(bop_3936.astype('float32'), relay.reshape(var_3939.astype('float32'), relay.shape_of(bop_3936))) # shape=(8, 13, 2)
uop_3944 = relay.tan(var_3934.astype('float32')) # shape=(8, 13, 1)
func_2870_call = mod.get_global_var('func_2870')
func_2871_call = mutated_mod.get_global_var('func_2871')
call_3947 = relay.TupleGetItem(func_2870_call(), 0)
call_3948 = relay.TupleGetItem(func_2871_call(), 0)
func_1580_call = mod.get_global_var('func_1580')
func_1582_call = mutated_mod.get_global_var('func_1582')
call_3958 = relay.TupleGetItem(func_1580_call(), 0)
call_3959 = relay.TupleGetItem(func_1582_call(), 0)
bop_3966 = relay.logical_xor(uop_3944.astype('int64'), bop_3940.astype('int64')) # shape=(8, 13, 2)
uop_3972 = relay.sin(bop_3966.astype('float64')) # shape=(8, 13, 2)
output = relay.Tuple([call_3947,call_3958,uop_3972,])
output2 = relay.Tuple([call_3948,call_3959,uop_3972,])
func_3974 = relay.Function([var_3934,var_3935,var_3939,], output)
mod['func_3974'] = func_3974
mod = relay.transform.InferType()(mod)
mutated_mod['func_3974'] = func_3974
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3974_call = mutated_mod.get_global_var('func_3974')
var_3976 = relay.var("var_3976", dtype = "int8", shape = (8, 13, 1))#candidate|3976|(8, 13, 1)|var|int8
var_3977 = relay.var("var_3977", dtype = "int8", shape = (8, 13, 2))#candidate|3977|(8, 13, 2)|var|int8
var_3978 = relay.var("var_3978", dtype = "int8", shape = (8, 13, 2))#candidate|3978|(8, 13, 2)|var|int8
call_3975 = func_3974_call(var_3976,var_3977,var_3978,)
output = call_3975
func_3979 = relay.Function([var_3976,var_3977,var_3978,], output)
mutated_mod['func_3979'] = func_3979
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2798_call = mod.get_global_var('func_2798')
func_2800_call = mutated_mod.get_global_var('func_2800')
call_4003 = relay.TupleGetItem(func_2798_call(), 0)
call_4004 = relay.TupleGetItem(func_2800_call(), 0)
func_1167_call = mod.get_global_var('func_1167')
func_1169_call = mutated_mod.get_global_var('func_1169')
call_4005 = relay.TupleGetItem(func_1167_call(), 0)
call_4006 = relay.TupleGetItem(func_1169_call(), 0)
output = relay.Tuple([call_4003,call_4005,])
output2 = relay.Tuple([call_4004,call_4006,])
func_4010 = relay.Function([], output)
mod['func_4010'] = func_4010
mod = relay.transform.InferType()(mod)
output = func_4010()
func_4011 = relay.Function([], output)
mutated_mod['func_4011'] = func_4011
mutated_mod = relay.transform.InferType()(mutated_mod)
func_442_call = mod.get_global_var('func_442')
func_443_call = mutated_mod.get_global_var('func_443')
call_4028 = relay.TupleGetItem(func_442_call(), 0)
call_4029 = relay.TupleGetItem(func_443_call(), 0)
output = relay.Tuple([call_4028,])
output2 = relay.Tuple([call_4029,])
func_4030 = relay.Function([], output)
mod['func_4030'] = func_4030
mod = relay.transform.InferType()(mod)
output = func_4030()
func_4031 = relay.Function([], output)
mutated_mod['func_4031'] = func_4031
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1435_call = mod.get_global_var('func_1435')
func_1436_call = mutated_mod.get_global_var('func_1436')
call_4064 = func_1435_call()
call_4065 = func_1435_call()
func_2519_call = mod.get_global_var('func_2519')
func_2523_call = mutated_mod.get_global_var('func_2523')
var_4075 = relay.var("var_4075", dtype = "uint8", shape = (224,))#candidate|4075|(224,)|var|uint8
var_4076 = relay.var("var_4076", dtype = "bool", shape = (1001,))#candidate|4076|(1001,)|var|bool
call_4074 = relay.TupleGetItem(func_2519_call(relay.reshape(var_4075.astype('uint8'), [8, 14, 2]), relay.reshape(var_4075.astype('uint8'), [8, 14, 2]), relay.reshape(var_4076.astype('bool'), [13, 77]), ), 3)
call_4077 = relay.TupleGetItem(func_2523_call(relay.reshape(var_4075.astype('uint8'), [8, 14, 2]), relay.reshape(var_4075.astype('uint8'), [8, 14, 2]), relay.reshape(var_4076.astype('bool'), [13, 77]), ), 3)
const_4083 = relay.const([[[True,True,True,False,False,True,False,True,True,True,False,False,True,True],[True,True,True,False,False,False,False,True,False,False,False,False,True,True]],[[False,False,False,True,True,True,True,True,False,False,False,False,True,True],[False,False,False,True,True,False,True,False,False,True,True,False,True,False]],[[True,True,True,True,True,True,True,False,True,False,False,True,False,False],[True,False,True,True,False,False,False,False,False,True,False,False,False,True]],[[True,False,True,False,True,True,True,False,False,False,False,True,True,False],[True,True,True,False,True,False,False,False,False,False,False,False,False,False]],[[True,False,True,False,False,True,False,True,False,True,True,False,False,False],[False,True,False,True,False,True,True,False,False,True,False,False,False,False]],[[True,False,False,False,False,True,False,True,False,False,False,False,True,False],[True,True,False,True,False,False,False,True,False,True,True,False,True,True]],[[False,True,True,True,True,True,True,True,False,True,False,True,True,True],[True,True,True,False,False,True,True,True,True,True,False,True,True,True]],[[True,False,False,False,True,True,True,False,False,True,True,False,False,False],[True,False,True,True,True,False,True,True,True,True,False,False,False,False]],[[False,True,True,True,True,True,True,False,False,True,False,False,False,False],[True,False,False,False,False,True,True,True,True,True,True,False,False,True]],[[False,False,False,False,False,True,False,True,True,True,False,True,False,False],[False,False,False,True,True,False,True,True,True,True,True,False,False,False]]], dtype = "bool")#candidate|4083|(10, 2, 14)|const|bool
bop_4084 = relay.less(call_4064.astype('bool'), relay.reshape(const_4083.astype('bool'), relay.shape_of(call_4064))) # shape=(10, 2, 14)
bop_4087 = relay.less(call_4065.astype('bool'), relay.reshape(const_4083.astype('bool'), relay.shape_of(call_4065))) # shape=(10, 2, 14)
func_2928_call = mod.get_global_var('func_2928')
func_2934_call = mutated_mod.get_global_var('func_2934')
const_4090 = relay.const([[-8,-5],[-9,-3],[10,-1],[-8,-6],[6,-10],[-8,7],[-3,7],[-8,-7],[3,5],[-6,-2],[2,1],[-6,-8],[10,9],[8,-10],[-9,-10],[-7,5],[-3,-4],[1,-7],[7,4],[5,-4],[-9,-5],[-8,-2],[1,4],[-1,9],[-3,2],[7,8],[9,7],[-3,1],[5,9],[-10,-10],[4,-8],[-5,8],[-10,-4],[2,-10],[4,-7],[8,7],[3,-7],[-8,5],[-3,7],[-1,-7],[-5,-7],[1,-8],[-5,-1],[2,-8],[-5,-1],[4,-7],[10,-4],[-6,2],[-2,-8],[6,-9],[2,4],[10,-10],[-7,-10],[-6,7],[-8,7],[-3,-7],[7,1],[3,4],[2,9],[10,-6],[10,-9],[10,4],[-8,-6],[-9,-8],[-10,2],[9,-9],[2,2],[9,10],[-2,8],[2,4],[3,2],[2,-10],[9,8],[-6,8],[6,1],[-7,-7],[-7,-3],[-8,-2],[8,3],[-2,-2],[5,-8],[8,-10],[-7,4],[-1,5],[7,-10],[6,4],[-3,-3],[1,7],[-7,6],[2,-2],[8,-5],[6,-8],[7,-7],[-9,-4],[-9,-1],[-2,4],[-3,7],[-6,-6],[-4,3],[10,-2],[-1,-9],[-10,-7],[2,9],[4,5],[4,5],[-2,8],[4,7],[-5,3],[8,10],[-7,-8],[3,-2],[1,-6],[-1,8],[-4,9],[-8,-3],[5,-10],[-10,-4],[-5,5],[-8,-7],[-6,5],[-4,1],[9,-7],[6,9],[8,6],[-10,-4],[-3,-3],[5,1],[2,9],[10,3],[1,8],[2,1],[-9,-7],[-9,3],[7,4],[-7,3],[2,-5],[-3,-6],[10,2],[-3,1],[3,-2],[8,-4],[-3,-7],[3,10],[-4,-10],[3,9],[-9,-5],[-7,-4],[-4,-3],[-2,-9],[5,-5],[-8,6],[10,-6],[1,6],[8,4],[-8,6],[-5,-6],[5,-3],[-1,-9],[-3,-8],[-2,-6],[2,4],[-3,-7],[-7,5],[-3,-10],[-6,9],[1,-4],[-4,7],[-1,-8],[7,4],[10,-3],[8,10],[8,-8],[-5,2],[6,10],[10,-3]], dtype = "uint8")#candidate|4090|(175, 2)|const|uint8
var_4091 = relay.var("var_4091", dtype = "float32", shape = (960,))#candidate|4091|(960,)|var|float32
var_4092 = relay.var("var_4092", dtype = "float64", shape = (42,))#candidate|4092|(42,)|var|float64
call_4089 = relay.TupleGetItem(func_2928_call(relay.reshape(const_4090.astype('uint8'), [7, 10, 5]), relay.reshape(const_4090.astype('uint8'), [7, 10, 5]), relay.reshape(var_4091.astype('float32'), [960,]), relay.reshape(var_4092.astype('float64'), [42, 1]), ), 1)
call_4093 = relay.TupleGetItem(func_2934_call(relay.reshape(const_4090.astype('uint8'), [7, 10, 5]), relay.reshape(const_4090.astype('uint8'), [7, 10, 5]), relay.reshape(var_4091.astype('float32'), [960,]), relay.reshape(var_4092.astype('float64'), [42, 1]), ), 1)
output = relay.Tuple([call_4074,var_4075,var_4076,bop_4084,call_4089,const_4090,var_4091,var_4092,])
output2 = relay.Tuple([call_4077,var_4075,var_4076,bop_4087,call_4093,const_4090,var_4091,var_4092,])
func_4094 = relay.Function([var_4075,var_4076,var_4091,var_4092,], output)
mod['func_4094'] = func_4094
mod = relay.transform.InferType()(mod)
mutated_mod['func_4094'] = func_4094
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4094_call = mutated_mod.get_global_var('func_4094')
var_4096 = relay.var("var_4096", dtype = "uint8", shape = (224,))#candidate|4096|(224,)|var|uint8
var_4097 = relay.var("var_4097", dtype = "bool", shape = (1001,))#candidate|4097|(1001,)|var|bool
var_4098 = relay.var("var_4098", dtype = "float32", shape = (960,))#candidate|4098|(960,)|var|float32
var_4099 = relay.var("var_4099", dtype = "float64", shape = (42,))#candidate|4099|(42,)|var|float64
call_4095 = func_4094_call(var_4096,var_4097,var_4098,var_4099,)
output = call_4095
func_4100 = relay.Function([var_4096,var_4097,var_4098,var_4099,], output)
mutated_mod['func_4100'] = func_4100
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4102 = relay.var("var_4102", dtype = "float64", shape = ())#candidate|4102|()|var|float64
var_4103 = relay.var("var_4103", dtype = "float64", shape = (9, 13, 6))#candidate|4103|(9, 13, 6)|var|float64
bop_4104 = relay.greater(var_4102.astype('bool'), var_4103.astype('bool')) # shape=(9, 13, 6)
uop_4117 = relay.tan(bop_4104.astype('float64')) # shape=(9, 13, 6)
bop_4128 = relay.not_equal(uop_4117.astype('bool'), relay.reshape(bop_4104.astype('bool'), relay.shape_of(uop_4117))) # shape=(9, 13, 6)
func_1497_call = mod.get_global_var('func_1497')
func_1498_call = mutated_mod.get_global_var('func_1498')
call_4135 = relay.TupleGetItem(func_1497_call(), 0)
call_4136 = relay.TupleGetItem(func_1498_call(), 0)
bop_4147 = relay.bitwise_and(var_4103.astype('int32'), var_4102.astype('int32')) # shape=(9, 13, 6)
uop_4153 = relay.atan(bop_4128.astype('float64')) # shape=(9, 13, 6)
output = relay.Tuple([call_4135,bop_4147,uop_4153,])
output2 = relay.Tuple([call_4136,bop_4147,uop_4153,])
func_4157 = relay.Function([var_4102,var_4103,], output)
mod['func_4157'] = func_4157
mod = relay.transform.InferType()(mod)
var_4158 = relay.var("var_4158", dtype = "float64", shape = ())#candidate|4158|()|var|float64
var_4159 = relay.var("var_4159", dtype = "float64", shape = (9, 13, 6))#candidate|4159|(9, 13, 6)|var|float64
output = func_4157(var_4158,var_4159,)
func_4160 = relay.Function([var_4158,var_4159,], output)
mutated_mod['func_4160'] = func_4160
mutated_mod = relay.transform.InferType()(mutated_mod)
func_442_call = mod.get_global_var('func_442')
func_443_call = mutated_mod.get_global_var('func_443')
call_4204 = relay.TupleGetItem(func_442_call(), 0)
call_4205 = relay.TupleGetItem(func_443_call(), 0)
const_4208 = relay.const([[[False,True,True,True,False,True,True],[True,True,True,True,True,True,True],[False,True,True,False,False,False,True],[False,False,True,False,False,True,True],[False,False,False,False,True,True,False],[True,False,True,True,True,False,False],[False,False,True,False,True,False,True],[True,True,False,True,True,True,False],[True,False,True,True,True,True,False],[False,False,False,False,False,True,True],[False,False,True,False,False,True,True],[True,True,False,False,False,False,True],[False,False,True,True,False,True,True]],[[True,False,True,False,True,True,False],[True,False,True,True,False,False,False],[False,True,True,True,True,True,True],[True,True,True,True,True,False,True],[False,True,False,True,False,True,True],[True,False,True,False,False,False,False],[True,True,False,True,False,True,True],[True,False,False,True,True,True,False],[True,False,True,True,True,True,False],[True,False,False,False,False,True,True],[True,False,True,False,True,True,True],[True,False,False,True,False,True,False],[True,False,False,False,False,False,True]],[[False,True,False,True,False,False,False],[False,True,True,True,True,False,True],[False,True,True,False,True,True,True],[True,False,True,False,True,True,True],[True,True,False,True,True,False,True],[True,False,True,True,False,False,True],[True,False,False,False,True,True,False],[False,True,True,True,True,False,True],[False,True,False,False,True,True,True],[False,True,False,True,False,True,False],[False,True,True,True,True,False,True],[False,True,True,False,False,False,True],[False,False,True,False,False,True,False]],[[True,False,False,True,False,False,False],[False,False,False,False,True,False,True],[True,False,True,True,True,False,False],[False,True,True,False,True,False,False],[True,False,True,False,False,True,True],[False,True,True,False,True,False,False],[True,False,False,False,False,True,True],[True,True,True,True,False,True,True],[False,True,False,True,True,True,False],[False,False,True,False,True,True,True],[True,True,True,False,True,True,False],[True,False,True,False,False,True,False],[False,False,True,False,True,True,False]],[[True,False,False,True,False,True,True],[False,False,False,True,True,False,True],[False,True,True,True,False,False,False],[False,True,False,False,True,True,True],[True,True,True,False,True,True,True],[False,False,False,False,True,True,True],[False,True,False,True,False,True,False],[False,True,False,False,True,False,True],[False,False,False,True,True,True,True],[False,False,False,False,False,True,False],[True,False,True,False,True,True,True],[True,False,True,False,False,False,False],[True,False,True,True,False,True,True]],[[True,False,False,False,False,True,False],[True,False,True,False,False,False,False],[True,False,True,False,False,True,False],[False,True,True,True,True,False,True],[False,False,False,True,False,False,True],[True,True,False,False,True,True,False],[True,True,True,False,True,False,True],[False,True,True,False,False,False,False],[False,True,True,False,True,True,True],[True,True,True,False,True,True,False],[False,False,True,False,True,False,False],[True,False,True,True,False,True,True],[False,True,True,False,False,False,False]],[[True,True,False,True,True,True,True],[False,False,False,False,False,True,False],[True,True,True,False,True,False,True],[True,True,True,False,True,False,False],[True,True,True,True,False,True,False],[True,False,True,True,False,True,False],[False,False,False,True,True,True,False],[True,False,True,False,True,False,False],[False,True,True,False,False,False,True],[False,True,True,False,True,False,True],[True,False,True,True,False,False,False],[False,True,False,True,True,False,True],[True,False,False,True,True,True,True]],[[True,True,False,False,False,True,False],[True,False,True,False,False,True,True],[False,True,True,False,False,False,True],[False,False,True,True,False,True,False],[False,False,False,True,True,False,True],[True,False,True,False,False,True,False],[False,False,True,False,True,False,True],[True,False,False,True,False,True,False],[True,False,True,True,False,True,False],[True,True,False,False,True,True,False],[True,False,False,True,False,True,False],[True,False,True,True,False,True,False],[True,True,True,False,True,False,True]],[[False,True,True,True,False,True,False],[False,True,False,True,True,True,True],[False,False,True,True,False,False,False],[True,True,True,False,False,False,False],[False,False,True,False,True,False,True],[True,False,True,True,True,False,True],[False,True,False,False,True,True,False],[False,True,False,True,False,True,True],[True,True,True,True,True,False,True],[False,False,False,False,False,False,True],[True,False,False,False,True,False,False],[False,True,False,False,False,True,True],[True,False,False,False,False,True,True]],[[True,True,False,False,False,False,False],[False,False,True,False,False,False,False],[True,False,False,False,False,True,False],[False,False,False,True,False,False,True],[False,False,False,False,True,False,False],[True,True,False,False,True,True,False],[False,True,False,True,False,False,True],[False,True,False,False,True,False,False],[False,False,True,False,False,False,False],[False,False,False,True,True,False,True],[True,False,True,True,True,True,False],[True,False,False,True,True,False,False],[True,False,False,True,False,True,True]],[[True,True,False,True,False,False,False],[True,True,False,False,True,True,True],[False,True,False,False,True,False,True],[False,False,True,True,False,True,False],[False,True,False,True,False,False,False],[False,False,True,False,True,True,False],[False,False,False,True,True,False,True],[False,False,False,True,False,False,False],[False,True,True,False,False,True,False],[True,True,False,True,True,True,True],[True,False,False,True,True,False,False],[False,False,True,True,False,False,False],[False,False,False,False,True,True,False]]], dtype = "bool")#candidate|4208|(11, 13, 7)|const|bool
bop_4209 = relay.logical_or(call_4204.astype('bool'), relay.reshape(const_4208.astype('bool'), relay.shape_of(call_4204))) # shape=(11, 13, 7)
bop_4212 = relay.logical_or(call_4205.astype('bool'), relay.reshape(const_4208.astype('bool'), relay.shape_of(call_4205))) # shape=(11, 13, 7)
func_1034_call = mod.get_global_var('func_1034')
func_1035_call = mutated_mod.get_global_var('func_1035')
call_4223 = relay.TupleGetItem(func_1034_call(), 0)
call_4224 = relay.TupleGetItem(func_1035_call(), 0)
output = relay.Tuple([bop_4209,call_4223,])
output2 = relay.Tuple([bop_4212,call_4224,])
func_4228 = relay.Function([], output)
mod['func_4228'] = func_4228
mod = relay.transform.InferType()(mod)
mutated_mod['func_4228'] = func_4228
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4228_call = mutated_mod.get_global_var('func_4228')
call_4229 = func_4228_call()
output = call_4229
func_4230 = relay.Function([], output)
mutated_mod['func_4230'] = func_4230
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1140_call = mod.get_global_var('func_1140')
func_1142_call = mutated_mod.get_global_var('func_1142')
call_4250 = relay.TupleGetItem(func_1140_call(), 0)
call_4251 = relay.TupleGetItem(func_1142_call(), 0)
output = relay.Tuple([call_4250,])
output2 = relay.Tuple([call_4251,])
func_4275 = relay.Function([], output)
mod['func_4275'] = func_4275
mod = relay.transform.InferType()(mod)
output = func_4275()
func_4276 = relay.Function([], output)
mutated_mod['func_4276'] = func_4276
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2207_call = mod.get_global_var('func_2207')
func_2209_call = mutated_mod.get_global_var('func_2209')
call_4280 = relay.TupleGetItem(func_2207_call(), 4)
call_4281 = relay.TupleGetItem(func_2209_call(), 4)
func_3508_call = mod.get_global_var('func_3508')
func_3512_call = mutated_mod.get_global_var('func_3512')
var_4283 = relay.var("var_4283", dtype = "float32", shape = (960,))#candidate|4283|(960,)|var|float32
call_4282 = relay.TupleGetItem(func_3508_call(relay.reshape(var_4283.astype('float32'), [960,]), relay.reshape(var_4283.astype('bool'), [15, 4, 16]), ), 2)
call_4284 = relay.TupleGetItem(func_3512_call(relay.reshape(var_4283.astype('float32'), [960,]), relay.reshape(var_4283.astype('bool'), [15, 4, 16]), ), 2)
func_671_call = mod.get_global_var('func_671')
func_675_call = mutated_mod.get_global_var('func_675')
const_4291 = relay.const(-3, dtype = "int16")#candidate|4291|()|const|int16
call_4290 = relay.TupleGetItem(func_671_call(relay.reshape(call_4280.astype('uint16'), [264,]), relay.reshape(const_4291.astype('int16'), []), ), 2)
call_4292 = relay.TupleGetItem(func_675_call(relay.reshape(call_4280.astype('uint16'), [264,]), relay.reshape(const_4291.astype('int16'), []), ), 2)
func_918_call = mod.get_global_var('func_918')
func_922_call = mutated_mod.get_global_var('func_922')
const_4305 = relay.const([True,False,True,False,False,True,False,False,False,True,True,False,False,False,False,False,False,True,True,False,False,False,True,False,False,False,False,True,True,True], dtype = "bool")#candidate|4305|(30,)|const|bool
call_4304 = relay.TupleGetItem(func_918_call(relay.reshape(const_4305.astype('bool'), [2, 15]), relay.reshape(const_4305.astype('bool'), [2, 15]), ), 0)
call_4306 = relay.TupleGetItem(func_922_call(relay.reshape(const_4305.astype('bool'), [2, 15]), relay.reshape(const_4305.astype('bool'), [2, 15]), ), 0)
func_2207_call = mod.get_global_var('func_2207')
func_2209_call = mutated_mod.get_global_var('func_2209')
call_4307 = relay.TupleGetItem(func_2207_call(), 3)
call_4308 = relay.TupleGetItem(func_2209_call(), 3)
output = relay.Tuple([call_4280,call_4282,var_4283,call_4290,const_4291,call_4304,const_4305,call_4307,])
output2 = relay.Tuple([call_4281,call_4284,var_4283,call_4292,const_4291,call_4306,const_4305,call_4308,])
func_4311 = relay.Function([var_4283,], output)
mod['func_4311'] = func_4311
mod = relay.transform.InferType()(mod)
mutated_mod['func_4311'] = func_4311
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4312 = relay.var("var_4312", dtype = "float32", shape = (960,))#candidate|4312|(960,)|var|float32
func_4311_call = mutated_mod.get_global_var('func_4311')
call_4313 = func_4311_call(var_4312)
output = call_4313
func_4314 = relay.Function([var_4312], output)
mutated_mod['func_4314'] = func_4314
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3733_call = mod.get_global_var('func_3733')
func_3734_call = mutated_mod.get_global_var('func_3734')
call_4318 = relay.TupleGetItem(func_3733_call(), 0)
call_4319 = relay.TupleGetItem(func_3734_call(), 0)
output = relay.Tuple([call_4318,])
output2 = relay.Tuple([call_4319,])
func_4324 = relay.Function([], output)
mod['func_4324'] = func_4324
mod = relay.transform.InferType()(mod)
output = func_4324()
func_4325 = relay.Function([], output)
mutated_mod['func_4325'] = func_4325
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1140_call = mod.get_global_var('func_1140')
func_1142_call = mutated_mod.get_global_var('func_1142')
call_4337 = relay.TupleGetItem(func_1140_call(), 0)
call_4338 = relay.TupleGetItem(func_1142_call(), 0)
uop_4343 = relay.sin(call_4337.astype('float64')) # shape=(10, 2, 14)
uop_4345 = relay.sin(call_4338.astype('float64')) # shape=(10, 2, 14)
func_1380_call = mod.get_global_var('func_1380')
func_1385_call = mutated_mod.get_global_var('func_1385')
const_4348 = relay.const([-6.414708,-2.078480,3.122446,7.575681,-8.703186,-1.374489,9.431777,-6.063263,-3.023846,-4.025528,-3.583243,0.524059,3.517409,-0.310079,4.800729,6.099170,-2.524629,-5.011078,-6.569910,-3.769346,3.963547,2.937735,-3.285225,9.840607,1.646597,8.508033,5.225169,-0.147168,4.102725,-8.522544,-9.013997,8.824345,9.747414,5.442246,0.754934,-8.455990,-3.084795,-2.597319,6.720187,0.460086,6.318896,-6.251803,0.043717,-9.032674,1.583637,-9.787691,-9.596584,-4.139749,8.327239,-3.597260,2.980881,3.181920,-7.191939,6.226679,2.576889,0.301974,7.617829,4.471471,-5.530003,4.685841,-4.637324,3.607463,2.636089,-9.268439,9.796510,-4.559240,5.281683,1.790450,8.833586,7.109114,2.499933,5.558299,0.601776,-0.522058,-4.356123,6.238421,3.159331,-0.626491,9.526726,7.107088,7.920030,4.959764,0.723634,-6.605479,1.657510,0.941623,-2.166578,0.471756,9.150726,4.132667,-1.660328,4.210063,-9.137700,-1.416234,-7.765292,-3.653200,7.669043,0.653267,-5.244649,7.733892,9.980918,0.510291,-8.973163,0.158909,-0.817734,2.177169,-1.928903,-4.277313,-9.858005,-0.757074,-6.109382,-1.331772,-2.201844,-2.239017,-6.167708,6.194967,-4.782885,1.111926,7.086723,-8.018502,-2.494506,-6.790397,-0.266548,9.209874,-7.231076,-4.507762,-4.616529,-1.180068,-7.638889,-2.309795,0.703580,-7.758200,-2.527703,-9.738230,9.397421,7.956348,-1.982323,-7.301583,-5.963028,-9.967092,7.876678,8.910157,3.032288,-6.592487,-3.365626,-9.367482,-2.745418,0.947597,6.437064,1.499680,-8.078621,-2.738819,-1.709428,-4.094642,-4.570765,2.696471,4.491588,1.029696,5.392859,-6.316142,-4.750749,6.544066,3.678787,0.504732,-4.341617,4.348352,6.572797,9.155598,-1.022696,-4.802036,-9.593675,-5.084912,-3.567988,9.652493,-4.206058,9.276950,-4.842613,5.822787,1.785301,-1.432633,8.471618,1.427369,0.359378,6.761303,-8.989290,-1.100098,0.278487,-2.802890,5.153666,6.968891,7.196395,-5.148761,0.285888,5.163005,7.679141,-6.849125,-0.973167,9.867673,1.461247,3.413205,8.215840,-7.299234,0.953232,-5.166423,-2.417156,-4.029408,4.530304,-8.681983,-4.539881,6.650499,4.121433,5.422506,1.037336,-2.215016,7.102888,-3.657615,6.176794,0.304419,8.746854,2.545550,-8.577093,8.581431,1.528055,-9.519073,-3.646405,2.413902,-0.800922,4.248396,3.409984,-6.462104,3.198935,1.317296,0.063610,6.538871,3.168407,3.222449,-9.015392,3.835110,-0.851913,-0.009369,6.484053,-0.403025,-0.932400,-0.027086,6.617028,-3.780444,6.301677,-7.577016,-2.294471,-9.421847,-3.612177,0.934823,-2.136136,-4.090463,2.077901,5.906540,-7.587073,-8.001740,8.607794,4.738536,5.005769,-9.512959,9.742683,6.107873,-2.756494,6.773996,6.850583,-5.397411,7.396613,-9.537825,5.527289,-9.496758,-3.188730,-4.280628,5.779773,-4.492101,4.004066,8.300961,2.250948,-4.219037,-8.815269,3.930758,9.683194,-2.920149,-0.798843,2.903893,-8.584912,-5.199928,-8.914883,0.249496,-4.369205,-0.547026,-3.755336,-3.131199,-3.406607,2.622799,2.063782,6.209675,-2.097245,8.102887,-9.839909,-0.466811,-2.170839,5.109837,6.600988,-2.908989,1.029998,1.434833,2.061416,4.254222,3.476841,-6.155229,6.723941,0.251464,0.630856,1.544007,0.335103,1.534268,-5.430542,-5.259827,1.049716,5.619425,0.548528,-6.420425,-3.993831,-8.282775,-0.478164,-2.082893,-2.261835,-9.000380,7.726155,-4.047925,6.770353,-0.609015,-3.540607,-7.120530,-6.324937,-7.376967,-6.355007,-0.308821,1.806242,-9.340593,7.713557,0.310858,-8.181599,-9.635815,9.618456,-3.032983,-7.319707,-7.579712,5.354120,-1.511459,-4.722649,9.744759,2.166518,-9.426160,8.645362,-3.882272,5.449355,-6.372869,8.279899,2.362053,2.791462,-3.382877,2.739467,7.622812,2.449171,-4.368265,-9.334296,-4.971873,6.987520,-5.199625,-2.752496,5.717682,1.043681,7.739450,-5.124695,5.895430,7.243261,0.074568,9.170823,2.802603,-8.568847,-1.420564,-5.627087,-4.792470,1.739328,-0.293003,-7.529458,-6.838265,7.160061,-1.413995,-7.534990,-9.735384,2.438144,-7.567342,-1.432386,0.210088,2.728500,4.150387,8.130147,1.753165,5.062217,-2.816398,-9.763242,1.110984,-5.078770,2.117027,3.302897,-3.983829,-8.685531,7.807647,3.495655,1.984905,1.382326,-4.460068,9.287770,9.648462,4.095901,-1.840983,-2.271809,5.939704,1.946908,-1.773897,-1.089967,-0.482086,1.474348,2.145756,-2.743720,-0.769084,-1.002138,-4.956790,-5.608458,-6.717308,3.193487,7.329531,-4.246048,0.194548,-3.747133,-5.164280,-3.109894,5.269150,4.256946,-6.255677,7.516964,3.960166,0.577868,8.279923,6.768357,6.019858,-0.653886,2.763520,-0.156792,8.789582,-1.280125,6.223849,-8.297494,-1.813897,-3.106805,2.250120,3.992153,5.583824,2.251422,8.606034,-2.168489,4.136535,9.763096,2.517631,6.560375,-1.897137,-8.506280,4.691597,-0.873875,-4.619199,-3.452428,7.468438,-8.640951,1.699635,8.105893,9.749103,3.680148,7.982849,0.060343,-1.983452,3.219132,-9.607658,2.212055,-6.216830,4.530179,-6.338218,-8.464880,-4.966630,-3.267577,-4.557757,-4.457393,7.835903,4.633248,-7.834049,0.853927,2.039206,-9.732825,-9.536783,1.854644,6.899602,-8.406243,9.186325,9.988417,8.075371,5.509204,-3.751359,0.830556,6.431538,-8.017976,2.291125,8.552551,-5.367605,-1.795882,3.132719,5.763275,1.132759,-2.924247,-7.381964,-3.526166,9.958634,-8.074695,2.947506,2.949991,-2.231417,-6.133545,5.232495,-6.098056,6.331341,-6.302864,0.009485,-1.737117,0.424276,0.895947,-1.273007,-2.896431,7.466829,7.973730,-6.248708,0.679102,-5.203495,2.025609,4.926047,8.835670,-1.105766,3.873396,3.309938,-3.528764,-1.939552,0.955290,7.221099,-9.343883,-1.762327,9.733179,-0.944548,3.929885,0.095838,-7.502681,-6.049481,2.700011,-8.974919,-1.299365,-5.476113,-9.119525,-8.517502,-2.419614,4.553531,-5.239521,-5.359324,0.690528,6.748828,-3.548022,2.888553,3.766166,-3.907742,-1.240477,-2.063708,5.448685,-6.984768,5.398579,7.365924,-9.087013,5.643062,-6.498734,7.264743,-2.453261,-6.556134,9.415544,-1.038903,0.225006,3.552548,2.562983,7.773884,2.565856,-9.606876,-9.952960,-0.635353,1.537469,-3.738122,7.800355,1.392676,-9.652722,-4.420918,9.077864,-5.982813,-3.574554,-7.113817,7.213824,-2.981652,6.018379,-7.790292,-1.665878,3.744962,-6.699441,2.320702,8.000808,4.233783,-7.315161,0.171830,-3.704390,-2.064834,9.026600,-5.304635,-7.853970,4.882990,-8.364878,-7.567625,-5.121739,-4.765962,5.326333,7.307175,-4.764412,-4.702816,-7.285131,-7.766245,8.322176,0.697543,9.194566,-6.863394,-9.693566,-9.336310,4.398012,3.661107,-3.494980,-3.994187,5.883121,-5.537825,-8.032878,-0.846097,-8.695620,-8.315119,-0.438345,-0.616634,0.497588,5.099429,5.371783,-0.294563,-8.608666,-9.329594,0.938474,-9.792227,-3.092050,-7.345041,2.575175,-2.235295,4.173870,-2.684163,-7.062538,-7.572955,8.948181,-1.235572,2.759189,3.415358,-9.932569,-1.688703,-2.413843,1.938862,1.838295,2.423818,-3.722387,-4.214053,-1.760444,6.988273,8.803117,0.895288,-8.974211,8.422422,-0.501878,3.591672,7.101559,8.339346,8.596050,-8.728384,-4.395901,5.709726,6.730600,8.765131,-8.786946,0.867060,-2.220417,-8.579579,-4.930536,-0.401612,-4.098928,7.173945,0.646786,9.321794,2.673841,9.023992,-7.532102,4.162652,-3.907931,4.037767,1.806888,-6.589066,8.507229,-7.575180,1.147823,8.135794,6.613337,9.184817,1.339409,8.304238,-1.967834,-7.699812,5.221163,2.693086,-9.830423,0.095292,0.705275,7.721886,-4.225121,-5.709811,-2.038809,-7.394492,-9.880225,-0.346542,-1.193999,2.234469,-7.778442,6.602073,7.532194,3.973191,-4.701971,1.491982,9.038001,-1.726709,8.216232,1.531707,-6.313256,3.474315,2.671534,-6.879542,9.274886,-6.550430,-9.553485,0.506339,-2.667048,4.202118,3.058340,-7.374314,-0.053842,8.141137,0.145582,1.178575,-5.149986,5.638733,7.182599,4.685271,3.550080,-2.531110,-6.184280,2.544666,9.005084,7.034307,9.246819,5.944184,-2.181469,8.977519,5.381613,-5.709319,2.079878,7.324438,7.152122,9.709288,-9.242354,-1.485415,-3.809008,-0.322343,0.552242,-1.577750,8.608774,-3.559209,-4.833282,-2.796659,-4.763998,6.120030,-5.258249,-6.558793,-7.432617,-0.483668,-1.467276,8.301439,-3.814708,-0.690974,3.217259,-1.251637,-3.169145,-2.897135,2.809524,-0.384810,1.161182,7.807851,-1.620290,-6.893350,-2.753872,1.771402,1.121819,5.925947,-0.587993,2.301801,-9.307542,1.953431,-7.053695,-5.616440,-8.020572,-4.972760,-9.912196,7.158027,1.638967,3.933187,-3.121038,-7.541320,8.095108,8.489871,6.793050,1.006209,-9.571103,-4.139171,4.969439,-8.867874,6.750765,1.870042,4.070239,-1.711757,-0.704985,-9.820866,1.744539,1.400215,-4.849190,-8.161686,8.758972,3.235014,-6.559195,5.173011,-1.402899,2.703629,-4.853545,-2.993709,9.317073,-2.511286,-9.069231,-7.935640,-8.323729,8.186330,-9.461420,-7.709147,6.174563,-5.393799,-0.595137,0.868614,4.494486,-7.964695,-9.348842,0.208335,-9.872194,9.118090,-0.515024,-9.313911,4.167406,1.599868,2.209864,-3.484490,-2.786590,0.109456,-7.258215,4.823836,6.314599,2.086854,-4.951184,-6.051296,-1.464630,-2.797615,6.041008,0.710102,-7.269557,9.763606,7.763333,-5.982082,-2.218832,-6.878460,8.262559,-9.471780,8.968410,-9.131087,9.144030,-0.004294,-2.410097,-0.389127,4.860603,0.505201,3.928544,-3.368772,-9.971654,-5.061549,-3.065859,1.509756,-9.358118,-3.777305,0.973199,-4.712877,8.770439,-7.356692,2.477649,-5.574995,6.001644,-7.989647,-7.612113,5.541170,5.256594,8.967506,-6.087220,7.397661,-8.414957,-0.513031,-6.354741,-0.530999,-7.888271,-6.292189,-8.750329,-3.843659,-2.650482,-4.640526,1.476373,4.389148,0.297091,-6.751259,5.133386,-6.385625,-2.015138,8.159307,2.745766,-3.171823,-8.168035,1.694541,7.056427,-5.034528,-8.845736,-4.144026,-7.253302,3.744935,-2.835188,1.822510,2.812998,-2.889416,9.342026,4.888048,6.541574,-2.361342,-2.895898,-7.376611,7.623104,5.574039,2.996785,-3.908714,7.492453,3.984170,8.046088,3.692467,1.248074,-8.283427,7.679894,2.444923,-9.227992,-5.841594,-9.164337,-3.270995,-1.302393,2.272928,-1.426954,4.542557,4.474744,8.598768,-0.353558,-4.708393,-0.683923,-3.511767,-9.962947,7.001994,7.961088,6.333721,-1.546187,7.227702,4.583728,7.698952,-1.207185,8.946572,1.404733,3.122098,2.362071,0.400608,-2.925238,2.215395,-4.309804,0.154460,-1.128382,3.767030,8.915868,8.676962,1.166594,-9.466972,-0.384062,-7.395528,-1.417773,4.192797,5.975522,-0.417529,-4.881425,-9.990873,-6.943377,-0.972904,-9.231875,5.869652,-0.379124,-0.762302,3.907207,-7.216263,-5.645262,-5.412880,-8.569757,-5.859057,-3.392717,3.290291,-6.590456,9.835768,-5.652539,3.006718,2.709475,-1.689109,-3.819545,-5.480575,4.382085,3.554638,9.138555,-4.754547,4.465074,7.468875,7.598225,-3.119508,-5.565065,-1.530369,6.300279,2.993704,0.641274,-1.116953,-8.240415,9.566001,9.306643,1.373927,-9.129455,-4.347419,-0.042717,-2.523087,4.186965,3.532431,-6.369725,-9.761257,9.331680,8.260284,9.129609,-1.748579,-0.991637,3.822170,-3.018730,-2.222947,-9.016085,-8.045631,-9.395874,3.440118,7.977069,0.459193,-3.718486,6.474155,9.994464,-8.564874,3.967783,-4.581893,5.354629,8.185180,-8.543185,-5.401005,3.761883,7.214872,7.461928,6.022169,3.823270,3.682055,-5.551815,6.119575,0.127575,-4.737604,9.501661,-2.565610,-4.187994,-6.415686,6.756773,2.369022,-1.834060,-3.505134,8.435350,-7.896596,-3.033611,9.821797,6.084792,-9.672001,-0.825718,4.723239,1.663288,-0.981387,7.480281,-8.364144,-6.594603,5.564254,-0.292023,-3.565928,8.551737,-8.709120,-2.426073,-4.660139,-5.690625,-2.200992,9.564072,-3.840968,4.787135,-0.489762,-8.549058,7.360294,4.955571,5.473234,-6.259376,8.991593,-7.344561,7.006124,5.327066,-5.720840,-4.789881,5.119357,-2.309082,-8.058843,-2.661851,3.813438,2.419657,1.117985,2.563228,-2.256652,5.012337,-9.292923,8.120966,-5.795803,4.770639,7.804593,-3.598154,-8.826876,-0.833026,-8.867583,1.027651,1.703026,7.853125,8.558871,0.461322,-0.428255,-0.827281,0.108677,6.444521,-7.611487,-2.023871,-5.394504,-0.292298,-4.026482,-2.425220,-9.420564,-4.823739,-3.372669,-4.078486,-7.560187,-6.481285,-2.128827,2.561254,-3.918653,-3.885552,-4.207985,-6.819943,0.624004,8.549224,-0.961618,-5.769318,7.492421,-3.591357,-8.119912,-9.836093,1.662454,-6.854692,9.475684,3.527396,-4.553671,-4.653440,-6.395474,7.963431,-8.285570,1.303331,-4.927894,7.501363,-0.300961,-1.902097,-5.962266,-6.914978,2.907200,-1.387871,-8.136675,-8.354505,3.495309,7.784128,-7.006338,6.951083,3.131354,3.909483,-1.493273,-5.994268,-3.424459,-8.038827,8.525687,-3.312453,0.737772,3.689954,-1.233060,-7.349246,-0.059663,-3.347093,-0.962239,9.841477,-8.864340,-4.754221,3.548152,-9.901440,2.606487,3.054116,5.287498,7.824731,-3.432497,-1.238515,-1.579730,-7.704271,2.856035,8.313871,-4.491670,2.718225,1.890537,9.060160,-3.071031,9.165802,-9.166016,-0.854337,-1.904277,-9.978837,-0.578662,-4.657427,5.625062,-5.016205,0.841946,8.854636,-2.977519,-8.144208,-1.438873,5.740890,1.204578,-4.370053,4.556521,3.236681,-5.466287,-3.567314,7.865998,2.728907,7.663108,9.504987,-9.310877,-4.412657,3.977122,-7.344321,-2.164307,9.904517,-8.280089,-4.802319,-2.943572,-9.436438,0.815903,-9.797769,7.122735,-6.960865,4.624303,6.854800,-1.509371,-8.332409,-5.963196,4.916240,-0.850628,3.905065,-7.934329,-3.663466,1.218700,8.097997,1.604696,9.228324,6.478041,1.581411,5.819852,-2.077381,-0.307138,-3.476034,-9.390126,-4.611945,-7.775609,3.180325,4.666915,4.142037,-6.043997,7.861681,-9.603040,-7.325976,-7.590254,-7.152399,-0.446453,5.874339,-2.590364,-0.568573,0.009837,6.463386,-9.429969,-4.311576,1.273883,-8.553469,-0.384005,9.448195,1.061900,6.315856,-4.080068,7.198832,-9.442661,7.500107,-9.657844,4.487202,-8.740063,6.288051,-9.497249,-6.150300,-3.450240,7.805047,5.361371,2.730896,7.647400,-5.686415,2.841796,-7.780385,6.610746,-4.499119,1.856119,1.636406,-8.007193,-4.656124,5.820726,-0.794616,-7.487907,-7.446629,9.403801,-3.358056,-8.344532,-8.893371,-1.480726,-6.685694,-3.800868,-8.565554,-0.657600,-8.639903,-8.641516,1.952700,0.699425,2.029168,-8.434197,4.443126,-1.489379,-4.303841,4.060632,-2.937280,6.474170,1.035671,9.845178,-2.072797,6.826573,-6.607195,3.266871,0.391426,-2.167313,-4.993620,4.488016,-9.419292,3.553027,-5.717069,3.325496,1.488679,2.465399,-7.828827,-6.142403,0.488107,6.858628,9.459429,0.459095,-6.565714,-5.080385,-6.512720,-3.921757,6.280229,3.549122,-2.103114,-0.395179,-5.015889,-2.943720,-8.248463,4.361848,1.423119,8.302650,9.446300,3.567025,-3.741400,3.193663,7.564440,2.891773,6.010664,9.263716,4.093115,2.909186,2.331223,3.757235,-9.839791,8.166266,5.224460,5.901761,-0.781488,-1.268638,-7.986234,3.582882,-7.762135,-5.640673,-8.261697,7.192425,0.290940,0.709803,5.345370,-6.924116,3.022101,6.103041,-7.581594,3.382493,2.031296,-6.670479,8.706509,-9.845586,-3.834730,-4.012367,-9.522534,5.999164,-0.119497,-8.468557,4.291959,-1.384796,1.725478,0.940258,-4.224410,-5.320682,0.994438,6.653862,-8.195725,-2.160288,-6.342598,6.740037,-4.019626,-3.451243,0.254838,-1.974478,8.850383,1.272522,-7.396878,-0.113415,-9.227680,7.323359,1.902089,-8.869876,-2.509187,4.066921,9.395287,7.604038,3.285920,7.870752,-7.485259,3.978393,-6.883375,-0.906880,2.696085,1.319783,1.218580,6.542079,5.915132,0.889306,-2.079383,-8.125504,2.887308,-6.953429,2.485174,-9.728980,2.152726,9.858502,-3.300263,6.695304,-4.235706,5.994165,1.834526,7.049983,8.396146,-4.806977,8.755105,3.164430,-2.904381,8.391926,9.684465,8.856704,7.066097,-0.593637,1.667966,4.287011,-2.165612,8.717595,-0.975812,-2.470194,5.375517,6.046256,6.976143,-0.580947,-0.831194,1.576602,2.605671,6.474485,7.024227,-9.061902,2.476283,9.911128,7.977255,5.427320,3.738064,0.310951,-8.418217,7.267744,1.261890], dtype = "float32")#candidate|4348|(1573,)|const|float32
const_4349 = relay.const([6.684019,3.452323,3.904297,2.247538,4.546485,9.994234,-0.883201,-9.966670,-7.103756,-7.098175,4.249917,1.829581,9.021284,-3.547056,1.045661,2.180771,-5.646622,-1.709864,1.726901,-2.610933,-2.225681,7.780859,-7.030659,-8.371888,3.227653,6.507723,-9.352662,6.765425,4.214894,-2.503018,-3.192040,-2.378617,-1.377626,2.151194,-7.952499,-6.712589,1.915578,3.650807,-1.142111,-9.110829,3.358770,-2.704965], dtype = "float64")#candidate|4349|(42,)|const|float64
call_4347 = relay.TupleGetItem(func_1380_call(relay.reshape(const_4348.astype('float32'), [11, 13, 11]), relay.reshape(const_4348.astype('float32'), [11, 13, 11]), relay.reshape(const_4349.astype('float64'), [14, 3]), ), 4)
call_4350 = relay.TupleGetItem(func_1385_call(relay.reshape(const_4348.astype('float32'), [11, 13, 11]), relay.reshape(const_4348.astype('float32'), [11, 13, 11]), relay.reshape(const_4349.astype('float64'), [14, 3]), ), 4)
output = relay.Tuple([uop_4343,call_4347,const_4348,const_4349,])
output2 = relay.Tuple([uop_4345,call_4350,const_4348,const_4349,])
func_4366 = relay.Function([], output)
mod['func_4366'] = func_4366
mod = relay.transform.InferType()(mod)
output = func_4366()
func_4367 = relay.Function([], output)
mutated_mod['func_4367'] = func_4367
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1167_call = mod.get_global_var('func_1167')
func_1169_call = mutated_mod.get_global_var('func_1169')
call_4385 = relay.TupleGetItem(func_1167_call(), 0)
call_4386 = relay.TupleGetItem(func_1169_call(), 0)
output = relay.Tuple([call_4385,])
output2 = relay.Tuple([call_4386,])
func_4393 = relay.Function([], output)
mod['func_4393'] = func_4393
mod = relay.transform.InferType()(mod)
output = func_4393()
func_4394 = relay.Function([], output)
mutated_mod['func_4394'] = func_4394
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4410 = relay.var("var_4410", dtype = "bool", shape = ())#candidate|4410|()|var|bool
const_4411 = relay.const([[[True,True,False,False,False,True,False,False],[True,False,True,False,True,True,True,False],[False,False,False,False,False,True,True,False],[True,True,True,True,True,False,True,False],[False,True,False,False,False,False,False,True],[True,True,False,False,False,True,False,False],[True,True,True,True,False,False,True,False],[False,False,True,True,True,False,True,True]],[[False,True,True,False,True,False,False,False],[True,False,False,False,True,True,False,False],[False,True,False,False,False,True,False,False],[False,True,True,True,False,False,False,False],[True,True,False,False,True,False,True,True],[False,True,True,True,False,True,False,False],[True,False,True,True,True,True,True,True],[True,False,False,True,False,False,True,True]],[[False,True,True,True,False,False,False,False],[False,True,False,False,True,False,True,False],[False,False,True,True,True,False,True,False],[False,True,True,False,False,False,True,False],[False,False,True,False,True,False,False,True],[True,False,True,False,False,False,False,False],[False,True,False,False,True,True,False,True],[False,False,True,False,False,False,False,False]],[[True,False,False,False,False,True,True,True],[True,False,False,False,True,False,False,True],[False,False,True,True,True,False,True,False],[False,False,False,False,True,True,True,False],[True,True,False,True,False,True,False,False],[True,False,False,False,True,False,False,True],[True,True,False,False,True,True,False,True],[False,True,False,True,False,True,True,True]]], dtype = "bool")#candidate|4411|(4, 8, 8)|const|bool
bop_4412 = relay.logical_and(var_4410.astype('bool'), const_4411.astype('bool')) # shape=(4, 8, 8)
uop_4415 = relay.sin(bop_4412.astype('float64')) # shape=(4, 8, 8)
output = relay.Tuple([uop_4415,])
output2 = relay.Tuple([uop_4415,])
func_4424 = relay.Function([var_4410,], output)
mod['func_4424'] = func_4424
mod = relay.transform.InferType()(mod)
mutated_mod['func_4424'] = func_4424
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4425 = relay.var("var_4425", dtype = "bool", shape = ())#candidate|4425|()|var|bool
func_4424_call = mutated_mod.get_global_var('func_4424')
call_4426 = func_4424_call(var_4425)
output = call_4426
func_4427 = relay.Function([var_4425], output)
mutated_mod['func_4427'] = func_4427
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4393_call = mod.get_global_var('func_4393')
func_4394_call = mutated_mod.get_global_var('func_4394')
call_4447 = relay.TupleGetItem(func_4393_call(), 0)
call_4448 = relay.TupleGetItem(func_4394_call(), 0)
output = relay.Tuple([call_4447,])
output2 = relay.Tuple([call_4448,])
func_4449 = relay.Function([], output)
mod['func_4449'] = func_4449
mod = relay.transform.InferType()(mod)
output = func_4449()
func_4450 = relay.Function([], output)
mutated_mod['func_4450'] = func_4450
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4393_call = mod.get_global_var('func_4393')
func_4394_call = mutated_mod.get_global_var('func_4394')
call_4550 = relay.TupleGetItem(func_4393_call(), 0)
call_4551 = relay.TupleGetItem(func_4394_call(), 0)
var_4579 = relay.var("var_4579", dtype = "bool", shape = (10, 2, 14))#candidate|4579|(10, 2, 14)|var|bool
bop_4580 = relay.right_shift(call_4550.astype('uint32'), relay.reshape(var_4579.astype('uint32'), relay.shape_of(call_4550))) # shape=(10, 2, 14)
bop_4583 = relay.right_shift(call_4551.astype('uint32'), relay.reshape(var_4579.astype('uint32'), relay.shape_of(call_4551))) # shape=(10, 2, 14)
output = bop_4580
output2 = bop_4583
func_4591 = relay.Function([var_4579,], output)
mod['func_4591'] = func_4591
mod = relay.transform.InferType()(mod)
var_4592 = relay.var("var_4592", dtype = "bool", shape = (10, 2, 14))#candidate|4592|(10, 2, 14)|var|bool
output = func_4591(var_4592)
func_4593 = relay.Function([var_4592], output)
mutated_mod['func_4593'] = func_4593
mutated_mod = relay.transform.InferType()(mutated_mod)
func_442_call = mod.get_global_var('func_442')
func_443_call = mutated_mod.get_global_var('func_443')
call_4597 = relay.TupleGetItem(func_442_call(), 0)
call_4598 = relay.TupleGetItem(func_443_call(), 0)
output = relay.Tuple([call_4597,])
output2 = relay.Tuple([call_4598,])
func_4601 = relay.Function([], output)
mod['func_4601'] = func_4601
mod = relay.transform.InferType()(mod)
mutated_mod['func_4601'] = func_4601
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4601_call = mutated_mod.get_global_var('func_4601')
call_4602 = func_4601_call()
output = call_4602
func_4603 = relay.Function([], output)
mutated_mod['func_4603'] = func_4603
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1140_call = mod.get_global_var('func_1140')
func_1142_call = mutated_mod.get_global_var('func_1142')
call_4612 = relay.TupleGetItem(func_1140_call(), 0)
call_4613 = relay.TupleGetItem(func_1142_call(), 0)
output = call_4612
output2 = call_4613
func_4651 = relay.Function([], output)
mod['func_4651'] = func_4651
mod = relay.transform.InferType()(mod)
output = func_4651()
func_4652 = relay.Function([], output)
mutated_mod['func_4652'] = func_4652
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4651_call = mod.get_global_var('func_4651')
func_4652_call = mutated_mod.get_global_var('func_4652')
call_4686 = func_4651_call()
call_4687 = func_4651_call()
func_4393_call = mod.get_global_var('func_4393')
func_4394_call = mutated_mod.get_global_var('func_4394')
call_4724 = relay.TupleGetItem(func_4393_call(), 0)
call_4725 = relay.TupleGetItem(func_4394_call(), 0)
var_4744 = relay.var("var_4744", dtype = "bool", shape = (10, 2, 14))#candidate|4744|(10, 2, 14)|var|bool
bop_4745 = relay.bitwise_and(call_4686.astype('int32'), relay.reshape(var_4744.astype('int32'), relay.shape_of(call_4686))) # shape=(10, 2, 14)
bop_4748 = relay.bitwise_and(call_4687.astype('int32'), relay.reshape(var_4744.astype('int32'), relay.shape_of(call_4687))) # shape=(10, 2, 14)
output = relay.Tuple([call_4724,bop_4745,])
output2 = relay.Tuple([call_4725,bop_4748,])
func_4749 = relay.Function([var_4744,], output)
mod['func_4749'] = func_4749
mod = relay.transform.InferType()(mod)
var_4750 = relay.var("var_4750", dtype = "bool", shape = (10, 2, 14))#candidate|4750|(10, 2, 14)|var|bool
output = func_4749(var_4750)
func_4751 = relay.Function([var_4750], output)
mutated_mod['func_4751'] = func_4751
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4764 = relay.var("var_4764", dtype = "float32", shape = (11, 5, 8))#candidate|4764|(11, 5, 8)|var|float32
uop_4765 = relay.log(var_4764.astype('float32')) # shape=(11, 5, 8)
func_292_call = mod.get_global_var('func_292')
func_294_call = mutated_mod.get_global_var('func_294')
var_4780 = relay.var("var_4780", dtype = "float64", shape = (42,))#candidate|4780|(42,)|var|float64
call_4779 = relay.TupleGetItem(func_292_call(relay.reshape(var_4780.astype('float64'), [2, 7, 3])), 0)
call_4781 = relay.TupleGetItem(func_294_call(relay.reshape(var_4780.astype('float64'), [2, 7, 3])), 0)
bop_4784 = relay.left_shift(uop_4765.astype('uint8'), relay.reshape(var_4764.astype('uint8'), relay.shape_of(uop_4765))) # shape=(11, 5, 8)
uop_4801 = relay.log10(bop_4784.astype('float32')) # shape=(11, 5, 8)
output = relay.Tuple([call_4779,var_4780,uop_4801,])
output2 = relay.Tuple([call_4781,var_4780,uop_4801,])
func_4803 = relay.Function([var_4764,var_4780,], output)
mod['func_4803'] = func_4803
mod = relay.transform.InferType()(mod)
var_4804 = relay.var("var_4804", dtype = "float32", shape = (11, 5, 8))#candidate|4804|(11, 5, 8)|var|float32
var_4805 = relay.var("var_4805", dtype = "float64", shape = (42,))#candidate|4805|(42,)|var|float64
output = func_4803(var_4804,var_4805,)
func_4806 = relay.Function([var_4804,var_4805,], output)
mutated_mod['func_4806'] = func_4806
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1580_call = mod.get_global_var('func_1580')
func_1582_call = mutated_mod.get_global_var('func_1582')
call_4812 = relay.TupleGetItem(func_1580_call(), 0)
call_4813 = relay.TupleGetItem(func_1582_call(), 0)
output = call_4812
output2 = call_4813
func_4821 = relay.Function([], output)
mod['func_4821'] = func_4821
mod = relay.transform.InferType()(mod)
mutated_mod['func_4821'] = func_4821
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4821_call = mutated_mod.get_global_var('func_4821')
call_4822 = func_4821_call()
output = call_4822
func_4823 = relay.Function([], output)
mutated_mod['func_4823'] = func_4823
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2014_call = mod.get_global_var('func_2014')
func_2015_call = mutated_mod.get_global_var('func_2015')
call_4829 = func_2014_call()
call_4830 = func_2014_call()
func_3172_call = mod.get_global_var('func_3172')
func_3173_call = mutated_mod.get_global_var('func_3173')
call_4843 = relay.TupleGetItem(func_3172_call(), 0)
call_4844 = relay.TupleGetItem(func_3173_call(), 0)
func_3153_call = mod.get_global_var('func_3153')
func_3157_call = mutated_mod.get_global_var('func_3157')
var_4848 = relay.var("var_4848", dtype = "float64", shape = (7, 6))#candidate|4848|(7, 6)|var|float64
const_4849 = relay.const([[-4.477939],[-1.315528],[4.299765],[2.586111],[-7.810561],[6.336948],[-8.848655],[-8.802983],[-3.057684],[-4.617371],[8.825103],[7.296055],[3.900913],[6.295376],[-0.256304],[7.473468],[-0.234241],[-0.342630],[1.282196],[7.957678],[-1.600977],[-6.595433],[-2.948329],[4.337810],[-9.275941],[-6.740755],[-1.998380],[9.415079],[-4.577533],[-1.971495],[-7.965257],[4.624211],[8.139114],[6.436972],[0.829906],[-2.492036],[0.388346],[-4.724150],[3.952326],[-5.167909],[5.379293],[4.673456],[5.052143],[8.042808],[2.456139],[-5.394158],[-6.826321],[0.594988],[1.920891],[-4.936968],[7.344167],[-6.726098],[-1.610046],[-0.583514],[3.866254],[0.512588],[6.893822],[-1.747066],[-5.596233],[0.073194],[6.259941],[5.734046],[1.556555],[6.482537],[6.872416],[-0.250811],[-1.390955],[0.411636],[1.442478],[-9.964541],[8.365099],[-9.477811],[-2.663979],[4.915509],[-0.851599],[3.261375],[-2.773912],[6.771631],[8.430212],[-8.449785],[4.052202],[9.295862],[-1.535380],[-5.023720],[-0.311928],[-9.422137],[-0.739986],[0.270005],[0.846593],[2.649086],[4.770016],[-1.586681],[-6.022301],[1.644717],[-6.471596],[-7.684322],[-9.595854],[-8.688514],[0.193033],[2.871680],[8.196347],[1.950759],[-6.786919],[1.310572],[2.636209],[6.507417],[0.794839],[-7.653554],[-3.560212],[8.832286],[6.619381],[-0.359272],[0.095726],[-6.584191],[1.253306],[-0.993440],[6.178568],[-8.956571],[-5.647050],[-8.708485],[8.265054],[-3.117181],[0.431439],[-0.914422],[1.992179],[-8.566216],[7.447913],[-4.398456],[3.186595],[2.951301],[-6.289015],[-6.535868],[9.043695],[9.630521],[-6.357725],[9.895439],[-0.709719],[-4.941520],[-6.558494],[1.267118],[-9.781316],[4.656750],[-7.888148],[-6.506331],[-9.792714],[-0.395223],[9.830012],[6.469452],[6.816403],[8.969646],[-0.112097],[4.212562],[-7.899977],[-1.657673],[-9.664940],[-7.626099],[3.448647],[5.747987],[-1.245547],[-9.257441],[6.972624],[3.951073],[3.525948],[-1.277611],[-3.988835],[-7.376224],[-2.760554],[4.027015],[1.256450],[-8.782285],[5.720220],[-1.533674],[-1.604781],[-0.075872],[7.260753],[6.999732],[4.425119],[8.265920],[7.548541],[7.740881],[2.091330],[-2.570621],[-5.470087],[2.435817],[1.987294],[5.452101],[-7.950415],[-1.933672],[8.651694],[3.806322],[8.802691],[-0.505868],[-7.149463],[5.127109],[9.557898],[4.949600],[-9.543196],[-8.266239],[7.113919],[-9.207537],[6.469803],[6.627427],[6.147113],[-9.953185],[-1.090962],[1.509963],[6.707486],[-5.768136],[8.899426],[9.642996],[-2.415041],[-2.491994],[3.580707],[2.932426],[-3.500982],[2.827613],[-6.565699],[4.214200],[-9.941629],[-1.263282],[-5.778532],[-6.449765],[7.062524],[6.009754],[-3.414688],[5.929436],[8.346221],[5.979279],[2.184901],[8.789244],[-9.810793],[2.069421],[6.958607],[-1.210769],[5.754182],[-0.669482],[-4.466075],[0.511978],[4.030938],[5.204284],[8.413799],[-6.444413],[-2.363825],[8.900079],[5.454486],[2.211675],[-7.422839],[-1.844052],[0.573606],[4.488936],[8.332665],[-9.283336],[8.949141],[-2.857563],[-5.873655],[-4.117526],[-0.863830],[-4.934784],[3.058237],[-3.957204],[-2.464003],[-1.868279],[8.119247],[-3.357801],[-6.478382],[6.270112],[2.521486],[6.501170],[0.788612],[3.628567],[6.971316],[9.152963],[2.978268],[-1.187724],[-8.909263],[5.020427],[-8.588143],[3.754853],[-8.071647],[3.263962],[6.024183],[-3.795420],[-2.416489],[6.369193],[5.459354],[-4.882987],[6.175148],[9.972143],[6.223918],[3.454950],[-0.663794],[6.288239],[-2.708380],[-4.809656],[-0.494627],[7.569091],[-5.269073],[9.427607],[-2.377162],[-4.085173],[1.757032],[-0.757190],[0.494691],[1.805049],[-9.308518],[-8.668587],[0.460880],[0.240639],[-2.816352],[-2.946640],[8.644988],[-3.881604],[-0.239474],[6.584508],[1.802097],[-5.735289],[-6.693509],[5.215326],[-4.462844],[-3.099057],[7.994439],[-9.312596],[-6.401363],[-0.335048],[1.263538],[-6.048632],[3.528283],[5.399952],[-5.645585],[-9.678664],[-9.396218],[-1.861090],[5.762552],[-6.663428],[6.978390],[-8.526275],[9.125506],[7.011183],[6.720330],[-3.032733],[6.688606],[0.358836],[-6.339781],[-0.900257],[5.838983],[-0.068452],[1.218746],[-2.270521],[-8.783962],[1.445993],[-1.768740],[-2.331619],[-7.630299],[0.274891],[0.406862],[-0.968306],[-1.716992],[2.204295],[-4.716871],[6.390955],[-6.817256],[-7.837741],[8.259579],[0.653710],[9.056095],[9.893447],[-3.584064],[-8.565343],[7.333976],[-3.721913],[4.800335],[5.813108],[5.691316],[-6.621075],[-3.259082],[1.266645],[3.771396],[1.480203],[5.868904],[-4.928701],[8.181248],[-0.069314],[6.320364],[-9.169716],[-1.122576],[-9.212143],[7.525915],[-4.875932],[-6.122534],[8.061549],[-4.162858],[-3.402419],[-5.040080],[-7.092878],[-3.929518],[-7.806466],[-1.422077],[9.868746],[3.748808],[4.524597],[0.906386],[-1.320143],[3.785564],[9.837597],[4.022457],[9.754058],[3.832596],[-3.528905],[1.819765],[1.435349],[5.945941],[3.481009],[-2.501737],[-3.207973],[-7.225094],[-3.058525],[3.234419],[-9.789660],[5.950393],[-2.140385],[-5.953663],[-5.693093],[1.616781],[8.817804],[-1.508800],[-3.489508],[9.531569],[6.793946],[2.649281],[7.574110],[0.752340],[2.127736],[-6.238971],[-6.550301],[8.498176],[9.673086],[-7.248347],[9.486909],[-2.084113],[-9.187848],[-7.128290],[-1.515468],[-1.208094],[8.705603],[8.664776],[9.250280],[-6.982282],[6.311267],[-2.175435],[-8.295123],[2.478486],[-8.671372],[-5.098280],[9.772853],[-8.333395],[8.203922],[3.478902],[-7.443800],[4.613713],[4.018178],[5.689560],[-9.576674],[1.661942],[-0.923608],[7.176102],[4.008266],[-1.975653],[-6.044654],[8.280531],[7.885660],[1.301686],[-1.879420],[2.803997],[-6.466572],[1.926530],[8.339672],[-9.687300],[-5.363408],[-5.924281],[0.485856],[-8.264749],[-3.052682],[-1.506354],[8.600440],[-2.915536],[-8.545256],[6.305623],[-4.023690],[3.516806],[3.363315],[-4.435144],[4.327244],[-7.310052],[-7.990328],[4.349570],[-0.329090],[-8.201501],[-5.364792],[8.372825],[8.979124],[3.700991],[7.355640],[-7.455197],[2.921955],[-1.667875],[-1.670150],[5.624204],[6.923528],[-3.323093],[-6.132189],[-1.779631],[7.438550],[1.783054],[8.277326],[3.366814],[9.162677],[-0.976718],[7.202232],[-4.955727],[4.913082],[0.186170],[-5.831085],[4.366036],[8.407803],[6.502027],[2.729112],[-3.473091],[6.808322],[9.660601],[3.542785],[1.297600],[6.350827],[0.789253],[-7.054967],[4.132102],[9.279481],[-8.294168],[3.810443],[4.752124],[5.172773],[6.701960],[-9.268429],[6.154689],[6.814021],[5.152996],[4.179090],[0.871349],[-8.571517],[8.429308],[2.545073],[-6.111413],[6.786982],[-4.071360],[7.735044],[5.779197],[-5.395192],[2.049922],[6.624606],[-5.876307],[6.009284],[8.441223],[-0.115401],[1.599300],[0.361738],[-4.553851],[7.920382],[1.325271],[6.449295],[-0.532934],[-8.587930],[7.672645],[-0.707135],[8.687114],[3.414421],[-2.776108],[1.832916],[6.507225],[5.235670],[8.129304],[2.645304],[9.801567],[-3.161399],[7.681807],[-0.140572],[-5.235458],[-8.495287],[6.424057],[0.759771],[-8.769337],[9.626770],[2.494895],[-6.240572],[-1.371261],[-3.070408],[-1.770378],[2.639327],[-5.039973],[2.422235],[9.835727],[2.071979],[-2.784117],[7.164816],[-6.965653],[-7.391982],[5.144225],[-4.315948],[1.442754],[9.102429],[-5.385388],[7.353569],[8.965941],[-5.152336],[-1.468529],[-3.880981],[8.404094],[-0.682821],[9.774477],[9.867456],[-1.715831],[-9.525428],[9.433622],[-8.021147],[9.888435],[2.451399],[4.865581],[-2.701230],[2.575389],[1.100805],[-1.419831],[-2.900151],[1.985477],[3.501619],[-5.615904],[2.880938],[2.311257],[5.344572],[-9.898905],[9.323911],[3.848437],[4.122512],[6.540886],[-3.231798],[-1.632832],[-0.174569],[6.316994],[-7.110402],[3.373490],[2.474290],[-3.251346],[-8.588833],[-4.823848],[3.761900],[-1.275623],[-0.423433],[1.782638],[-3.843241],[7.536803],[0.177048],[-3.634260],[0.696641],[-2.609114],[4.443539],[9.625091],[-6.988279],[0.756414],[8.059524],[-5.255475],[-8.704338],[2.848197],[-6.401649],[-7.202518],[4.644056],[9.426677],[4.926018],[9.500495],[9.122363],[-3.176176],[9.263542],[7.278256],[8.207062],[8.825232],[-6.040786],[7.640486],[-2.120044],[4.841711],[9.264084],[6.723674],[-8.268847],[-6.098675],[0.949975],[-4.963149],[7.012283],[7.192431],[-5.095316],[-4.080966],[6.744155],[3.525605],[6.460090],[-5.776817],[0.064221],[3.140304],[2.678784],[-7.388499],[2.084270],[8.993093],[-8.880763],[-9.202181],[-8.513643],[-3.620266],[-8.214313],[-9.345865],[-2.240645],[-7.994621],[3.752970],[5.107987],[-0.383777],[6.182476],[-2.910354],[2.498409],[-3.978067],[-4.270857],[-8.008667],[7.370118],[-7.153008],[-6.832911],[-6.227372],[-9.156749],[-8.075355],[8.244567],[7.434366],[-8.350528],[0.984866],[8.521981],[3.615827],[9.019008],[1.419537],[-8.195024],[-6.145545],[-4.975268],[-8.734320],[-9.778380],[7.963335],[1.191840],[7.033704],[4.579125],[-8.313327],[-6.348638],[-4.366739],[2.030506],[3.926897],[1.137036],[-8.108712],[-6.785451],[5.583498],[4.130659],[2.901747],[1.307105],[-8.357613],[-4.439078],[9.287143],[-6.621162],[-8.056081],[3.273771],[-5.950382],[-8.088472],[9.191353],[-0.800369],[-2.715859],[7.056014],[7.330372],[2.788243],[-9.365037],[8.667763],[9.940782],[-1.939779],[-7.954398],[-9.884526],[7.967524],[2.050440],[-4.476951],[1.615004],[5.844093],[0.041879],[7.436371],[-0.680140],[2.563951],[4.391790],[-1.360810],[-6.548871],[5.403472],[-7.358574],[1.351416],[-8.620367],[-3.134324],[-7.614763],[1.801722],[-4.043162],[6.117206],[-7.475501],[-0.343128],[9.993648],[-0.369605],[5.695796],[-0.821485],[5.548866],[-8.189940],[5.219735],[-7.892548],[4.256547],[1.355831],[-1.383438],[0.554454],[5.706141],[-5.431136],[2.648322],[-1.727798],[1.129326],[-5.617910],[5.243962],[-5.973532],[-9.140757],[-0.259434],[5.018884],[9.426116],[0.656426],[-4.364837],[5.417554],[6.546228],[4.155793],[2.318166],[-8.250073],[2.188490],[-1.256820],[7.067846],[-4.814427],[-2.970903],[-7.687305],[-8.336737],[-7.580385],[-6.529838],[-1.760784],[8.454190],[1.378665],[4.183719],[-6.813212],[2.102545],[-7.329055],[-5.048290],[-1.861837],[5.567512],[-0.654470],[1.870254],[-3.682675],[-6.552946],[5.021655],[6.345834],[0.575234],[-0.724439],[0.659847],[1.133227],[-5.667851],[-6.037645],[-8.526087],[2.494272],[-1.548691],[5.979454],[9.811464],[-9.926648],[4.312504],[-4.196339],[4.447237],[-6.707900],[-0.053263],[0.168248],[-7.641265],[2.528432],[-7.372466],[-1.897377],[9.707302],[1.508758],[-4.065661],[-5.063702],[-8.195347],[5.550906],[9.834411],[-2.401466],[5.333595],[2.518750],[2.829303],[4.618098],[-0.460399],[-9.340705],[4.964836],[3.351608],[3.623520],[-4.327345],[0.460681],[8.246764],[8.609883],[2.639668],[-3.650053],[-3.647906],[6.552300],[3.147363],[-1.396790],[-1.819755],[9.781510],[0.203692],[3.292536],[5.687861],[-5.759935],[-3.102441],[-8.520418],[9.149760],[2.762916],[-7.470975],[-1.753156],[2.207970],[6.537518],[9.177447],[-2.054410],[-5.478990],[-5.486466],[-3.585033],[-5.757874],[-2.588810],[2.680913],[-6.813674],[-4.023787],[-0.084059],[5.005843],[8.984181],[6.535623],[5.282739],[1.004049],[-1.025904],[-0.191306],[-7.260468],[5.210994],[7.143338],[-5.846624],[-1.774960],[-7.302720],[-8.346747],[-1.627619],[-6.333973],[6.515189],[4.107426],[2.633233],[1.651225],[1.445848],[-0.597909],[-4.718669],[5.941713],[4.426363],[4.239194],[-5.671856],[4.033586],[1.242887],[-8.766705],[-5.242543],[5.238889],[-6.130573],[-6.509799],[4.992231],[9.881943],[-3.407983],[-3.709286],[-9.533138],[-1.702247],[-6.570048],[0.224801],[8.930687],[-7.466224],[-4.947468],[-4.406364],[3.414056],[2.326125],[-8.398289],[3.718305],[1.055660],[6.060704],[-4.583359],[5.279348],[3.377622],[-5.628555],[2.343084],[-4.418311],[3.823481],[3.279144],[1.790813],[-6.648870],[8.434807],[6.934580],[-4.336022],[7.093469],[8.143909],[3.696654],[5.044147],[-6.479428],[-5.290797]], dtype = "float32")#candidate|4849|(1001, 1)|const|float32
var_4850 = relay.var("var_4850", dtype = "uint8", shape = (1, 350))#candidate|4850|(1, 350)|var|uint8
call_4847 = relay.TupleGetItem(func_3153_call(relay.reshape(var_4848.astype('float64'), [42,]), relay.reshape(const_4849.astype('float32'), [1001,]), relay.reshape(var_4850.astype('uint8'), [350, 1]), ), 4)
call_4851 = relay.TupleGetItem(func_3157_call(relay.reshape(var_4848.astype('float64'), [42,]), relay.reshape(const_4849.astype('float32'), [1001,]), relay.reshape(var_4850.astype('uint8'), [350, 1]), ), 4)
uop_4854 = relay.atan(call_4843.astype('float32')) # shape=(15, 4, 16)
uop_4856 = relay.atan(call_4844.astype('float32')) # shape=(15, 4, 16)
func_442_call = mod.get_global_var('func_442')
func_443_call = mutated_mod.get_global_var('func_443')
call_4864 = relay.TupleGetItem(func_442_call(), 0)
call_4865 = relay.TupleGetItem(func_443_call(), 0)
func_1285_call = mod.get_global_var('func_1285')
func_1288_call = mutated_mod.get_global_var('func_1288')
call_4870 = relay.TupleGetItem(func_1285_call(relay.reshape(call_4847.astype('bool'), [11, 13, 7]), relay.reshape(const_4849.astype('bool'), [11, 13, 7]), ), 1)
call_4871 = relay.TupleGetItem(func_1288_call(relay.reshape(call_4847.astype('bool'), [11, 13, 7]), relay.reshape(const_4849.astype('bool'), [11, 13, 7]), ), 1)
output = relay.Tuple([call_4829,call_4847,var_4848,const_4849,var_4850,uop_4854,call_4864,call_4870,])
output2 = relay.Tuple([call_4830,call_4851,var_4848,const_4849,var_4850,uop_4856,call_4865,call_4871,])
func_4878 = relay.Function([var_4848,var_4850,], output)
mod['func_4878'] = func_4878
mod = relay.transform.InferType()(mod)
mutated_mod['func_4878'] = func_4878
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4878_call = mutated_mod.get_global_var('func_4878')
var_4880 = relay.var("var_4880", dtype = "float64", shape = (7, 6))#candidate|4880|(7, 6)|var|float64
var_4881 = relay.var("var_4881", dtype = "uint8", shape = (1, 350))#candidate|4881|(1, 350)|var|uint8
call_4879 = func_4878_call(var_4880,var_4881,)
output = call_4879
func_4882 = relay.Function([var_4880,var_4881,], output)
mutated_mod['func_4882'] = func_4882
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2798_call = mod.get_global_var('func_2798')
func_2800_call = mutated_mod.get_global_var('func_2800')
call_4888 = relay.TupleGetItem(func_2798_call(), 0)
call_4889 = relay.TupleGetItem(func_2800_call(), 0)
func_2519_call = mod.get_global_var('func_2519')
func_2523_call = mutated_mod.get_global_var('func_2523')
var_4903 = relay.var("var_4903", dtype = "uint8", shape = (224,))#candidate|4903|(224,)|var|uint8
var_4904 = relay.var("var_4904", dtype = "bool", shape = (1001,))#candidate|4904|(1001,)|var|bool
call_4902 = relay.TupleGetItem(func_2519_call(relay.reshape(var_4903.astype('uint8'), [8, 14, 2]), relay.reshape(var_4903.astype('uint8'), [8, 14, 2]), relay.reshape(var_4904.astype('bool'), [13, 77]), ), 0)
call_4905 = relay.TupleGetItem(func_2523_call(relay.reshape(var_4903.astype('uint8'), [8, 14, 2]), relay.reshape(var_4903.astype('uint8'), [8, 14, 2]), relay.reshape(var_4904.astype('bool'), [13, 77]), ), 0)
func_2648_call = mod.get_global_var('func_2648')
func_2649_call = mutated_mod.get_global_var('func_2649')
call_4911 = relay.TupleGetItem(func_2648_call(), 3)
call_4912 = relay.TupleGetItem(func_2649_call(), 3)
output = relay.Tuple([call_4888,call_4902,var_4903,var_4904,call_4911,])
output2 = relay.Tuple([call_4889,call_4905,var_4903,var_4904,call_4912,])
func_4923 = relay.Function([var_4903,var_4904,], output)
mod['func_4923'] = func_4923
mod = relay.transform.InferType()(mod)
var_4924 = relay.var("var_4924", dtype = "uint8", shape = (224,))#candidate|4924|(224,)|var|uint8
var_4925 = relay.var("var_4925", dtype = "bool", shape = (1001,))#candidate|4925|(1001,)|var|bool
output = func_4923(var_4924,var_4925,)
func_4926 = relay.Function([var_4924,var_4925,], output)
mutated_mod['func_4926'] = func_4926
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4030_call = mod.get_global_var('func_4030')
func_4031_call = mutated_mod.get_global_var('func_4031')
call_4932 = relay.TupleGetItem(func_4030_call(), 0)
call_4933 = relay.TupleGetItem(func_4031_call(), 0)
output = call_4932
output2 = call_4933
func_4940 = relay.Function([], output)
mod['func_4940'] = func_4940
mod = relay.transform.InferType()(mod)
mutated_mod['func_4940'] = func_4940
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4940_call = mutated_mod.get_global_var('func_4940')
call_4941 = func_4940_call()
output = call_4941
func_4942 = relay.Function([], output)
mutated_mod['func_4942'] = func_4942
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2207_call = mod.get_global_var('func_2207')
func_2209_call = mutated_mod.get_global_var('func_2209')
call_5009 = relay.TupleGetItem(func_2207_call(), 5)
call_5010 = relay.TupleGetItem(func_2209_call(), 5)
func_4940_call = mod.get_global_var('func_4940')
func_4942_call = mutated_mod.get_global_var('func_4942')
call_5019 = func_4940_call()
call_5020 = func_4940_call()
func_2680_call = mod.get_global_var('func_2680')
func_2681_call = mutated_mod.get_global_var('func_2681')
call_5049 = relay.TupleGetItem(func_2680_call(), 1)
call_5050 = relay.TupleGetItem(func_2681_call(), 1)
output = relay.Tuple([call_5009,call_5019,call_5049,])
output2 = relay.Tuple([call_5010,call_5020,call_5050,])
func_5051 = relay.Function([], output)
mod['func_5051'] = func_5051
mod = relay.transform.InferType()(mod)
mutated_mod['func_5051'] = func_5051
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5051_call = mutated_mod.get_global_var('func_5051')
call_5052 = func_5051_call()
output = call_5052
func_5053 = relay.Function([], output)
mutated_mod['func_5053'] = func_5053
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5101 = relay.var("var_5101", dtype = "float64", shape = (4, 11, 12))#candidate|5101|(4, 11, 12)|var|float64
uop_5102 = relay.tan(var_5101.astype('float64')) # shape=(4, 11, 12)
func_2207_call = mod.get_global_var('func_2207')
func_2209_call = mutated_mod.get_global_var('func_2209')
call_5107 = relay.TupleGetItem(func_2207_call(), 0)
call_5108 = relay.TupleGetItem(func_2209_call(), 0)
output = relay.Tuple([uop_5102,call_5107,])
output2 = relay.Tuple([uop_5102,call_5108,])
func_5110 = relay.Function([var_5101,], output)
mod['func_5110'] = func_5110
mod = relay.transform.InferType()(mod)
mutated_mod['func_5110'] = func_5110
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5111 = relay.var("var_5111", dtype = "float64", shape = (4, 11, 12))#candidate|5111|(4, 11, 12)|var|float64
func_5110_call = mutated_mod.get_global_var('func_5110')
call_5112 = func_5110_call(var_5111)
output = call_5112
func_5113 = relay.Function([var_5111], output)
mutated_mod['func_5113'] = func_5113
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4366_call = mod.get_global_var('func_4366')
func_4367_call = mutated_mod.get_global_var('func_4367')
call_5277 = relay.TupleGetItem(func_4366_call(), 3)
call_5278 = relay.TupleGetItem(func_4367_call(), 3)
var_5279 = relay.var("var_5279", dtype = "float64", shape = (42,))#candidate|5279|(42,)|var|float64
bop_5280 = relay.equal(call_5277.astype('bool'), relay.reshape(var_5279.astype('bool'), relay.shape_of(call_5277))) # shape=(42,)
bop_5283 = relay.equal(call_5278.astype('bool'), relay.reshape(var_5279.astype('bool'), relay.shape_of(call_5278))) # shape=(42,)
output = relay.Tuple([bop_5280,])
output2 = relay.Tuple([bop_5283,])
func_5290 = relay.Function([var_5279,], output)
mod['func_5290'] = func_5290
mod = relay.transform.InferType()(mod)
mutated_mod['func_5290'] = func_5290
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5291 = relay.var("var_5291", dtype = "float64", shape = (42,))#candidate|5291|(42,)|var|float64
func_5290_call = mutated_mod.get_global_var('func_5290')
call_5292 = func_5290_call(var_5291)
output = call_5292
func_5293 = relay.Function([var_5291], output)
mutated_mod['func_5293'] = func_5293
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1412_call = mod.get_global_var('func_1412')
func_1414_call = mutated_mod.get_global_var('func_1414')
call_5301 = relay.TupleGetItem(func_1412_call(), 0)
call_5302 = relay.TupleGetItem(func_1414_call(), 0)
var_5305 = relay.var("var_5305", dtype = "bool", shape = (10, 2, 14))#candidate|5305|(10, 2, 14)|var|bool
bop_5306 = relay.maximum(call_5301.astype('float32'), relay.reshape(var_5305.astype('float32'), relay.shape_of(call_5301))) # shape=(10, 2, 14)
bop_5309 = relay.maximum(call_5302.astype('float32'), relay.reshape(var_5305.astype('float32'), relay.shape_of(call_5302))) # shape=(10, 2, 14)
func_1285_call = mod.get_global_var('func_1285')
func_1288_call = mutated_mod.get_global_var('func_1288')
const_5315 = relay.const([True,True,True,False,False,False,True,True,False,False,True,False,False,False,False,True,True,True,True,True,False,True,False,False,True,False,True,False,False,True,True,False,False,False,False,True,False,True,False,False,True,True,True,False,True,True,True,True,False,True,False,False,False,False,False,True,False,True,True,False,True,False,False,True,False,True,False,False,False,True,True,False,False,False,False,False,True,True,True,True,False,True,True,False,True,True,True,True,False,True,True,True,True,False,True,False,True,True,False,True,False,True,True,True,True,True,True,False,True,False,True,True,True,False,False,False,True,True,True,False,False,False,True,False,False,False,False,True,False,False,True,False,False,False,True,True,False,False,False,True,False,True,False,True,False,False,True,True,False,False,True,False,True,True,False,True,True,False,True,True,True,False,False,True,False,True,False,False,False,False,True,False,False,False,False,False,False,True,True,False,False,True,True,True,False,True,False,True,False,True,True,True,True,True,False,False,False,False,False,False,True,False,True,True,False,True,True,False,False,False,True,False,True,False,True,True,True,False,True,True,True,False,False,True,True,False,True,True,True,True,False,False,True,True,True,True,False,False,False,False,False,True,True,False,True,False,True,False,False,False,False,False,False,False,True,True,True,False,True,False,True,True,False,True,False,True,False,False,True,False,False,True,True,True,True,False,False,True,True,False,True,True,False,False,True,True,True,False,True,False,False,True,True,False,False,True,True,False,True,False,True,False,False,False,True,True,True,True,False,False,False,False,True,False,False,False,False,True,True,True,False,True,False,True,False,False,True,True,True,False,False,False,False,False,False,False,True,True,True,False,True,True,False,False,False,False,True,False,True,False,True,True,True,False,True,True,False,False,True,True,False,True,True,True,True,False,True,False,True,False,False,True,False,False,True,False,False,False,False,False,False,True,True,False,True,False,True,False,False,False,True,True,True,True,False,False,True,True,True,False,True,True,True,True,False,True,True,False,True,True,False,False,True,False,False,False,False,True,False,True,False,False,False,True,True,False,False,False,True,True,False,False,False,False,False,False,True,True,True,False,True,True,False,False,True,False,False,False,False,True,True,False,True,True,True,False,True,True,False,False,False,False,False,True,False,False,True,True,False,False,False,True,False,False,True,True,True,True,True,True,False,False,True,True,True,False,True,False,False,True,False,False,False,True,True,False,True,True,False,True,True,False,False,True,False,True,True,True,True,False,False,True,True,True,True,False,False,False,True,False,False,True,False,False,False,False,False,False,True,False,True,False,False,False,False,True,True,True,False,False,True,True,False,False,False,True,True,False,True,False,False,True,True,True,True,False,True,False,False,False,False,True,False,True,True,False,False,True,True,False,True,True,True,True,True,False,False,False,False,False,False,True,True,False,False,True,False,True,True,False,True,True,True,True,False,True,False,False,False,True,True,True,False,False,True,False,False,True,False,True,True,True,False,True,True,False,False,True,True,True,True,False,False,False,True,True,True,True,True,True,True,False,True,True,True,False,True,True,True,False,False,True,True,False,False,False,False,False,True,True,True,False,True,True,False,True,False,False,False,False,True,True,False,False,True,True,False,False,True,False,False,True,True,True,False,True,True,False,True,False,False,False,False,True,True,True,False,False,True,True,False,False,False,False,True,True,False,True,False,True,True,False,False,False,False,False,True,True,True,False,False,True,False,False,False,False,True,True,False,False,False,False,True,False,False,False,False,False,True,False,True,True,False,False,True,False,False,True,False,True,True,False,False,False,False,True,False,False,False,False,False,False,False,True,False,False,True,False,True,True,False,False,False,True,False,True,True,True,False,True,False,False,True,True,False,False,False,False,False,False,False,False,False,False,False,False,False,True,True,True,False,True,False,False,False,False,False,False,True,False,True,False,False,True,True,False,True,True,False,True,True,False,True,True,False,True,True,True,True,False,False,True,False,False,False,False,True,False,False,False,False,False,False,True,True,True,True,False,False,False,True,True,False,False,False,True,False,False,False,True,False,False,False,False,True,False,True,False,False,True,False,True,True,True,False,False,False,True,False,True,True,True,False,False,False,True,True,False,True,True,True,True,True,True,False,False,False,True,False,False,False,True,True,False,False,True,False,False,True,True,True,False,False,False,False,False,True,True,False,False,False,True,True,False,True,True,False,True,False,True,True,True,False,True,True,False,False,True,False,True,False,False,False,True,False,False,True,True,False,False,True,False,True,False,False,False,False,True,True,False,False,True,True,False,False,False,False,False,False,False,False,False,False,False,True,False,False,True,True,False,True,False,True,False,True,True,True,True,False,False,True,False,True,True,False,True,True,False,False,True,True,False,False,True,False,True,False,False,False,True,True], dtype = "bool")#candidate|5315|(1001,)|const|bool
call_5314 = relay.TupleGetItem(func_1285_call(relay.reshape(const_5315.astype('bool'), [11, 13, 7]), relay.reshape(const_5315.astype('bool'), [11, 13, 7]), ), 0)
call_5316 = relay.TupleGetItem(func_1288_call(relay.reshape(const_5315.astype('bool'), [11, 13, 7]), relay.reshape(const_5315.astype('bool'), [11, 13, 7]), ), 0)
output = relay.Tuple([bop_5306,call_5314,const_5315,])
output2 = relay.Tuple([bop_5309,call_5316,const_5315,])
func_5354 = relay.Function([var_5305,], output)
mod['func_5354'] = func_5354
mod = relay.transform.InferType()(mod)
mutated_mod['func_5354'] = func_5354
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5355 = relay.var("var_5355", dtype = "bool", shape = (10, 2, 14))#candidate|5355|(10, 2, 14)|var|bool
func_5354_call = mutated_mod.get_global_var('func_5354')
call_5356 = func_5354_call(var_5355)
output = call_5356
func_5357 = relay.Function([var_5355], output)
mutated_mod['func_5357'] = func_5357
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3172_call = mod.get_global_var('func_3172')
func_3173_call = mutated_mod.get_global_var('func_3173')
call_5392 = relay.TupleGetItem(func_3172_call(), 0)
call_5393 = relay.TupleGetItem(func_3173_call(), 0)
output = relay.Tuple([call_5392,])
output2 = relay.Tuple([call_5393,])
func_5398 = relay.Function([], output)
mod['func_5398'] = func_5398
mod = relay.transform.InferType()(mod)
mutated_mod['func_5398'] = func_5398
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5398_call = mutated_mod.get_global_var('func_5398')
call_5399 = func_5398_call()
output = call_5399
func_5400 = relay.Function([], output)
mutated_mod['func_5400'] = func_5400
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5428 = relay.var("var_5428", dtype = "float64", shape = ())#candidate|5428|()|var|float64
var_5429 = relay.var("var_5429", dtype = "float64", shape = (6, 10, 11))#candidate|5429|(6, 10, 11)|var|float64
bop_5430 = relay.divide(var_5428.astype('float64'), var_5429.astype('float64')) # shape=(6, 10, 11)
bop_5444 = relay.add(var_5428.astype('uint16'), var_5429.astype('uint16')) # shape=(6, 10, 11)
output = relay.Tuple([bop_5430,bop_5444,])
output2 = relay.Tuple([bop_5430,bop_5444,])
func_5457 = relay.Function([var_5428,var_5429,], output)
mod['func_5457'] = func_5457
mod = relay.transform.InferType()(mod)
mutated_mod['func_5457'] = func_5457
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5457_call = mutated_mod.get_global_var('func_5457')
var_5459 = relay.var("var_5459", dtype = "float64", shape = ())#candidate|5459|()|var|float64
var_5460 = relay.var("var_5460", dtype = "float64", shape = (6, 10, 11))#candidate|5460|(6, 10, 11)|var|float64
call_5458 = func_5457_call(var_5459,var_5460,)
output = call_5458
func_5461 = relay.Function([var_5459,var_5460,], output)
mutated_mod['func_5461'] = func_5461
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1580_call = mod.get_global_var('func_1580')
func_1582_call = mutated_mod.get_global_var('func_1582')
call_5518 = relay.TupleGetItem(func_1580_call(), 0)
call_5519 = relay.TupleGetItem(func_1582_call(), 0)
output = call_5518
output2 = call_5519
func_5528 = relay.Function([], output)
mod['func_5528'] = func_5528
mod = relay.transform.InferType()(mod)
mutated_mod['func_5528'] = func_5528
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5528_call = mutated_mod.get_global_var('func_5528')
call_5529 = func_5528_call()
output = call_5529
func_5530 = relay.Function([], output)
mutated_mod['func_5530'] = func_5530
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4651_call = mod.get_global_var('func_4651')
func_4652_call = mutated_mod.get_global_var('func_4652')
call_5548 = func_4651_call()
call_5549 = func_4651_call()
output = call_5548
output2 = call_5549
func_5557 = relay.Function([], output)
mod['func_5557'] = func_5557
mod = relay.transform.InferType()(mod)
output = func_5557()
func_5558 = relay.Function([], output)
mutated_mod['func_5558'] = func_5558
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3172_call = mod.get_global_var('func_3172')
func_3173_call = mutated_mod.get_global_var('func_3173')
call_5583 = relay.TupleGetItem(func_3172_call(), 0)
call_5584 = relay.TupleGetItem(func_3173_call(), 0)
output = call_5583
output2 = call_5584
func_5603 = relay.Function([], output)
mod['func_5603'] = func_5603
mod = relay.transform.InferType()(mod)
mutated_mod['func_5603'] = func_5603
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5603_call = mutated_mod.get_global_var('func_5603')
call_5604 = func_5603_call()
output = call_5604
func_5605 = relay.Function([], output)
mutated_mod['func_5605'] = func_5605
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4940_call = mod.get_global_var('func_4940')
func_4942_call = mutated_mod.get_global_var('func_4942')
call_5620 = func_4940_call()
call_5621 = func_4940_call()
func_3832_call = mod.get_global_var('func_3832')
func_3836_call = mutated_mod.get_global_var('func_3836')
var_5623 = relay.var("var_5623", dtype = "bool", shape = (2016,))#candidate|5623|(2016,)|var|bool
call_5622 = relay.TupleGetItem(func_3832_call(relay.reshape(var_5623.astype('bool'), [12, 12, 14]), relay.reshape(var_5623.astype('bool'), [12, 12, 14]), ), 0)
call_5624 = relay.TupleGetItem(func_3836_call(relay.reshape(var_5623.astype('bool'), [12, 12, 14]), relay.reshape(var_5623.astype('bool'), [12, 12, 14]), ), 0)
output = relay.Tuple([call_5620,call_5622,var_5623,])
output2 = relay.Tuple([call_5621,call_5624,var_5623,])
func_5626 = relay.Function([var_5623,], output)
mod['func_5626'] = func_5626
mod = relay.transform.InferType()(mod)
var_5627 = relay.var("var_5627", dtype = "bool", shape = (2016,))#candidate|5627|(2016,)|var|bool
output = func_5626(var_5627)
func_5628 = relay.Function([var_5627], output)
mutated_mod['func_5628'] = func_5628
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2870_call = mod.get_global_var('func_2870')
func_2871_call = mutated_mod.get_global_var('func_2871')
call_5688 = relay.TupleGetItem(func_2870_call(), 3)
call_5689 = relay.TupleGetItem(func_2871_call(), 3)
var_5708 = relay.var("var_5708", dtype = "float32", shape = (10, 2, 14))#candidate|5708|(10, 2, 14)|var|float32
bop_5709 = relay.multiply(call_5688.astype('int32'), relay.reshape(var_5708.astype('int32'), relay.shape_of(call_5688))) # shape=(10, 2, 14)
bop_5712 = relay.multiply(call_5689.astype('int32'), relay.reshape(var_5708.astype('int32'), relay.shape_of(call_5689))) # shape=(10, 2, 14)
func_3776_call = mod.get_global_var('func_3776')
func_3778_call = mutated_mod.get_global_var('func_3778')
var_5720 = relay.var("var_5720", dtype = "float32", shape = (45,))#candidate|5720|(45,)|var|float32
call_5719 = func_3776_call(relay.reshape(var_5720.astype('float32'), [3, 1, 15]))
call_5721 = func_3776_call(relay.reshape(var_5720.astype('float32'), [3, 1, 15]))
uop_5730 = relay.cos(call_5719.astype('float64')) # shape=(3, 1, 15)
uop_5732 = relay.cos(call_5721.astype('float64')) # shape=(3, 1, 15)
output = relay.Tuple([bop_5709,var_5720,uop_5730,])
output2 = relay.Tuple([bop_5712,var_5720,uop_5732,])
func_5739 = relay.Function([var_5708,var_5720,], output)
mod['func_5739'] = func_5739
mod = relay.transform.InferType()(mod)
var_5740 = relay.var("var_5740", dtype = "float32", shape = (10, 2, 14))#candidate|5740|(10, 2, 14)|var|float32
var_5741 = relay.var("var_5741", dtype = "float32", shape = (45,))#candidate|5741|(45,)|var|float32
output = func_5739(var_5740,var_5741,)
func_5742 = relay.Function([var_5740,var_5741,], output)
mutated_mod['func_5742'] = func_5742
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4228_call = mod.get_global_var('func_4228')
func_4230_call = mutated_mod.get_global_var('func_4230')
call_5759 = relay.TupleGetItem(func_4228_call(), 0)
call_5760 = relay.TupleGetItem(func_4230_call(), 0)
uop_5773 = relay.atanh(call_5759.astype('float64')) # shape=(11, 13, 7)
uop_5775 = relay.atanh(call_5760.astype('float64')) # shape=(11, 13, 7)
output = uop_5773
output2 = uop_5775
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
