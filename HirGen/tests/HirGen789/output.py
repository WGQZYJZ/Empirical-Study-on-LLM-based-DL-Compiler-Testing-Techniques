import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_0 = relay.var("var_0", dtype = "int64", shape = ())#candidate|0|()|var|int64
const_1 = relay.const([[[8,1,-6,4,-6,8,10,-8,1,-7,-4,1],[-4,-10,-6,8,-10,9,-2,1,-7,9,3,6],[-7,-2,-6,7,-3,-6,-7,-5,5,-4,-9,8],[6,-3,-5,4,2,1,10,9,6,4,-4,-10],[-3,10,1,-5,-3,5,-9,-10,-8,-10,10,4],[7,-9,7,1,-6,-1,7,6,-6,10,2,8],[-2,10,8,-7,-2,-9,8,10,-1,2,8,-1],[-9,-2,10,4,-8,3,-8,2,-9,-10,3,2],[10,-3,4,-5,-3,-5,-4,-5,3,8,-8,-3],[3,3,-3,9,1,-4,-4,-7,3,-1,2,1],[2,9,2,-7,5,-3,7,6,4,4,-6,-8]],[[-4,9,-3,-3,8,6,-4,-8,-5,9,-3,-3],[-4,8,7,-10,4,-8,10,3,5,-9,-2,-8],[-8,-2,-2,1,-9,6,4,8,-7,-5,2,-4],[-9,4,10,10,-8,10,-7,-6,7,-4,-1,-10],[-3,-5,5,9,-4,5,4,-3,-10,-4,1,5],[3,-2,-6,-3,9,1,9,8,-5,-9,-2,3],[5,-1,9,-6,-7,-7,1,1,9,-4,4,-4],[-6,-9,-5,-2,-2,-7,-9,1,9,9,9,-8],[4,7,-5,-8,-1,-1,1,-7,6,-4,-6,1],[5,5,-3,-10,-6,-6,7,-4,-3,7,10,-9],[-9,-1,7,10,5,-6,10,-5,3,9,-5,10]],[[-2,4,-10,-8,5,4,3,-4,1,7,5,2],[-3,-10,6,6,7,-9,2,-8,9,9,-7,-2],[-2,-2,3,9,-6,4,-8,-9,-10,-2,6,-9],[1,8,-10,6,1,1,3,8,8,1,-2,-9],[-1,-7,8,-3,-4,6,-1,-6,-2,6,8,7],[8,3,10,-4,-2,7,7,-10,-1,2,9,-4],[-8,8,-4,3,-3,-2,8,-4,-7,2,-9,2],[7,1,6,8,-8,2,-1,6,1,9,-5,2],[1,5,-6,-1,-5,-10,-2,4,5,1,-1,2],[-6,1,-1,3,-7,-4,-9,6,9,-4,-4,-8],[2,-3,-8,-5,5,6,-1,7,-9,-10,6,-2]],[[-4,6,3,-5,5,8,-4,-8,8,-2,-2,6],[-10,10,4,10,8,-6,-2,-6,8,2,6,8],[5,5,-10,9,-7,3,2,-1,-1,-1,-7,-10],[2,6,2,-4,-7,4,-7,-5,-5,10,-4,-8],[-10,-8,8,2,9,-8,6,-8,8,-10,7,3],[-6,9,-8,6,8,4,1,-3,-6,3,-2,6],[-5,9,4,5,-9,-1,-3,-2,3,6,2,6],[10,-3,-2,-4,-9,-2,7,2,-4,-2,2,-10],[9,-8,-3,10,-6,10,6,-7,-9,6,6,3],[-5,-9,-8,-1,-2,8,5,-3,-3,-7,6,-3],[-2,-2,-1,8,-9,-2,-5,2,1,-5,9,7]],[[10,2,9,1,-6,-10,10,-2,7,6,6,1],[9,6,-3,-2,7,9,1,7,-4,4,-7,1],[-8,-7,-4,-2,4,10,10,-10,-8,-3,10,-6],[-5,6,-5,-5,3,-9,-10,-9,10,-2,3,-5],[3,-10,8,-5,4,-4,-8,6,-2,-10,8,7],[-9,6,2,-3,-1,-8,-8,-1,-4,-5,-5,6],[6,10,-5,9,5,-8,-9,2,5,-9,2,-5],[-5,1,-9,-5,-4,8,1,5,-3,3,-3,1],[4,1,10,-2,-6,2,1,10,-4,5,6,-3],[3,2,-2,6,-3,-2,2,-7,-7,4,10,-5],[4,2,-10,-10,5,-10,5,3,-10,-2,-8,-9]],[[-1,5,6,-6,10,10,-6,-2,2,-8,-6,6],[7,-8,-8,10,-1,1,-4,10,8,1,-2,-7],[-5,-3,7,6,-9,8,5,-9,2,-6,10,8],[7,3,4,-6,-6,-9,10,8,-2,-7,4,-5],[-7,-3,-6,6,-4,-5,-9,-7,-9,10,4,9],[2,-4,3,3,10,-8,8,-10,-10,-1,5,6],[8,5,1,9,1,2,-3,-3,-2,9,-4,-4],[-5,5,-5,-8,-4,5,7,1,-7,2,-9,-5],[8,10,-7,6,9,4,2,-9,4,-4,-9,-9],[-7,8,-7,-6,9,5,-2,7,-4,-7,4,-5],[-3,-1,5,9,-10,9,-2,-2,-2,-6,-10,8]],[[-6,4,-3,8,9,8,-9,7,6,9,-2,-8],[8,1,-8,3,3,2,6,4,1,-9,-9,-10],[-4,-2,9,-3,5,-4,2,-7,-5,-3,-10,6],[8,-2,6,3,-2,-8,-6,-6,6,6,-7,5],[3,-5,-4,6,8,1,1,-6,9,-2,7,-10],[9,-3,10,-10,-3,-7,6,10,-1,-10,7,5],[-1,2,4,3,9,-10,1,1,-5,-2,2,-4],[7,5,-1,-9,-7,10,-5,7,-6,-1,8,-10],[10,3,8,-5,3,-6,-2,7,-7,5,10,6],[-10,5,-10,-1,9,-2,-1,-9,-7,-1,1,10],[-6,10,4,4,-2,2,-5,2,-8,10,-1,6]],[[-7,7,-6,6,10,10,1,-10,4,-6,-8,3],[-3,5,-6,-2,-9,-9,-5,-9,-10,-1,-2,5],[-6,6,-9,7,-4,6,5,-2,-8,-1,7,-2],[-6,9,5,-5,5,4,-2,6,3,-7,1,-3],[10,5,-4,6,9,10,-9,6,8,-8,1,6],[5,4,-3,-6,-3,-2,-8,-4,6,-3,-1,-1],[-1,9,10,-7,1,10,10,-6,-6,9,7,-1],[9,9,4,-9,6,8,5,10,1,-9,9,4],[-6,-9,6,7,7,5,4,8,-4,-6,6,-7],[10,-7,-3,-4,2,1,7,-5,-4,6,4,7],[-4,9,1,-4,3,-9,2,5,-9,6,-6,10]],[[1,7,-2,5,9,6,1,-2,3,3,5,3],[-8,-1,8,-6,9,-4,10,-9,-5,-1,-6,3],[4,-7,5,4,9,-10,9,3,9,-9,7,10],[-2,8,-1,1,6,4,-10,-7,-6,-3,10,10],[-5,10,6,6,8,10,-7,-5,-9,-6,-7,-7],[9,5,7,-1,-6,-6,1,-4,8,-8,-5,9],[2,-4,-10,2,-2,-9,4,-1,10,-5,-1,-2],[3,3,-3,-1,-10,3,-7,-9,4,7,-7,10],[-8,-10,6,-8,-2,-4,-5,-9,3,5,9,-6],[-2,-4,-1,-8,-1,-8,10,5,-8,6,-5,8],[-1,7,-7,-4,8,-7,4,8,6,4,3,-8]],[[10,4,-1,5,-5,3,-7,-10,6,-4,5,-10],[9,6,5,2,-10,-1,9,4,-8,8,3,-10],[9,3,-7,6,-7,9,8,7,10,-10,4,4],[10,-7,2,-6,-1,-7,-10,-4,5,10,7,-3],[7,-7,-9,5,5,-6,1,-9,1,-1,-9,9],[-10,-1,-8,3,8,-6,-3,8,-5,6,-6,-8],[-3,7,6,7,-9,-5,3,-4,-10,-9,3,10],[4,2,2,-7,9,-6,4,-2,-4,-9,7,-9],[4,-7,-7,-3,-4,3,4,-1,-5,-9,10,1],[-8,-10,-2,9,7,2,-6,5,1,6,-9,10],[1,3,1,-9,4,4,-10,-3,3,-1,10,9]],[[-5,7,-1,7,6,-5,-8,6,6,10,-4,-3],[8,-4,-1,10,-7,1,5,9,-2,8,1,-9],[-7,2,-2,6,6,-8,6,-4,-6,10,5,-5],[-8,-4,-1,7,-4,7,2,7,7,7,-5,6],[-8,-5,8,9,-4,-6,-7,-1,9,-8,3,-9],[1,4,10,9,6,2,-3,1,-3,-2,-7,-3],[3,7,7,6,3,3,-10,1,6,2,-2,1],[-10,-10,-6,-3,-4,-4,-6,10,10,3,8,6],[5,7,10,5,-9,-7,7,5,-2,-4,-9,8],[-8,9,-2,1,-2,-5,4,-4,-4,-9,3,-2],[-5,3,-1,-3,-1,6,-9,1,3,6,7,-2]],[[3,3,7,10,4,-6,-2,3,-1,-9,5,-2],[7,6,9,6,-9,-7,4,8,9,-2,-3,6],[-5,-4,4,-7,-5,-6,10,6,1,-6,1,3],[-6,-2,-2,-2,-5,7,4,2,-6,-6,10,-6],[7,6,-5,-7,5,-1,10,-6,-2,4,-9,-7],[-5,-3,-7,6,10,2,-2,-8,2,8,3,-7],[-8,-2,9,2,-2,-9,-6,3,-6,3,5,6],[3,9,7,2,9,2,3,4,-1,-4,-9,-2],[3,-4,9,6,-6,-7,-3,10,-2,1,-8,-1],[-9,5,4,-4,7,5,-8,7,8,-8,-4,4],[-1,-1,2,-10,-9,-1,-6,-9,-3,-6,-3,-6]],[[8,3,-10,-8,-4,2,3,8,-6,-6,-4,-3],[7,-7,-4,-5,-6,-4,5,-9,-1,6,-2,-9],[-5,-1,9,-5,7,9,6,-6,2,9,10,-8],[-9,-8,-1,1,1,7,10,-6,-6,8,1,-4],[-4,2,-3,8,5,4,10,-1,9,-10,-10,4],[5,7,10,1,-6,-9,-3,2,-2,3,-2,-4],[2,10,2,9,-9,-3,10,2,-9,5,-9,-10],[-3,-2,7,8,10,3,-3,7,-9,-1,-6,-4],[-6,-9,-6,-4,1,-6,4,8,-3,3,-1,7],[5,-8,-1,-8,-3,-1,-3,10,3,-2,1,10],[-1,9,5,4,4,-1,-6,3,5,8,9,3]],[[5,8,5,7,8,8,2,5,5,2,-6,-3],[-6,-10,1,6,9,2,-9,10,5,-5,1,4],[6,1,2,3,-7,5,-6,-3,-5,9,-4,-3],[8,-7,-6,8,8,3,3,9,9,-7,-3,10],[-5,-3,-9,-7,4,7,-8,3,-4,7,-10,-9],[-8,-4,7,10,2,-1,10,9,6,6,-10,-10],[-3,6,-3,4,1,4,-1,-2,-10,5,2,5],[-9,2,2,-8,8,10,-8,5,-2,1,-5,-8],[5,6,7,-5,-6,8,8,-3,-7,-10,-7,6],[3,-7,-10,5,8,5,5,-4,9,-7,5,5],[-2,8,-1,-3,4,5,4,-1,1,10,8,-7]],[[3,5,-3,-1,-7,-8,-7,-3,10,-9,7,-7],[-8,6,-8,-4,-8,-2,-9,-8,3,-3,7,-5],[5,9,4,4,-10,9,-5,2,1,-2,6,7],[8,-4,-7,9,-3,-7,4,-8,-2,-6,-1,8],[-2,-2,-4,10,10,-4,2,-2,4,1,-1,-4],[-7,1,7,-10,4,9,-3,-8,4,-2,7,-1],[-3,1,-3,-8,3,8,9,-1,10,-8,9,-5],[-2,-9,-1,2,-5,8,7,-10,-3,4,-6,4],[-7,8,2,8,10,-5,-2,-5,-1,6,-8,10],[-7,-7,9,1,-8,1,4,-6,-9,-5,7,9],[-4,-5,1,8,-8,-3,6,5,2,-4,7,1]],[[10,-8,-8,6,-10,-4,6,1,7,-3,7,-7],[-3,-5,2,6,-2,2,1,-1,8,-4,-9,8],[-10,-9,8,5,-10,2,6,5,-4,7,-4,6],[6,-6,-6,1,7,2,7,-9,-8,10,-2,-2],[-1,-10,9,-8,-8,10,-9,2,10,-5,3,-5],[-6,-7,-9,5,-9,-6,2,3,-8,-4,3,-5],[1,-1,4,3,10,-10,-8,10,9,8,-8,1],[-4,-3,10,2,-9,-4,-1,-5,-9,-2,10,-8],[6,10,5,-1,6,-7,-3,-10,4,-7,4,-7],[-7,-2,1,-7,4,-2,-9,-1,9,3,-9,-4],[6,-1,3,3,-7,10,7,-4,5,3,8,-8]]], dtype = "int64")#candidate|1|(16, 11, 12)|const|int64
bop_2 = relay.maximum(var_0.astype('int64'), const_1.astype('int64')) # shape=(16, 11, 12)
output = relay.Tuple([bop_2,])
output2 = relay.Tuple([bop_2,])
func_24 = relay.Function([var_0,], output)
mod['func_24'] = func_24
mod = relay.transform.InferType()(mod)
mutated_mod['func_24'] = func_24
mutated_mod = relay.transform.InferType()(mutated_mod)
var_25 = relay.var("var_25", dtype = "int64", shape = ())#candidate|25|()|var|int64
func_24_call = mutated_mod.get_global_var('func_24')
call_26 = func_24_call(var_25)
output = call_26
func_27 = relay.Function([var_25], output)
mutated_mod['func_27'] = func_27
mutated_mod = relay.transform.InferType()(mutated_mod)
const_323 = relay.const([[[-1,-5,4,-7,3,-1],[-4,-3,6,-8,-7,8],[7,4,-3,7,3,-6],[-3,-1,5,-7,-2,-4],[8,-7,3,6,-9,7],[5,9,-5,-4,-7,5],[9,-3,-4,1,-8,-6],[-2,-4,-5,4,-4,9],[-7,10,-9,8,-8,-1],[7,-2,-8,10,1,2],[7,-7,10,-2,8,-3],[-4,-5,3,5,-5,6],[5,5,2,-5,5,9]],[[7,-4,-1,2,-1,10],[-2,-5,3,-2,9,-6],[7,1,-3,-9,2,-5],[-4,2,3,-9,-8,4],[8,-10,5,10,-9,-4],[-3,-3,8,-10,7,8],[-6,9,-3,-5,-10,8],[3,9,-10,6,-8,8],[9,10,10,9,7,1],[-10,-1,-3,8,-8,10],[10,1,5,5,7,-1],[3,4,8,10,-2,-10],[1,-1,-5,-8,6,-6]],[[-9,6,-4,3,-7,-9],[-2,2,-1,7,2,-2],[-10,3,-10,-9,-10,4],[-2,-5,-4,5,-3,-8],[-1,8,-4,2,3,-9],[6,1,-1,-2,-2,5],[9,-1,-8,9,-7,-5],[-1,4,2,-4,-1,4],[10,6,-1,7,2,-4],[-1,4,-2,-9,-5,7],[-6,8,8,9,8,-9],[8,-8,-7,1,-7,-6],[-5,2,-7,9,-9,-9]],[[1,-4,-3,9,-10,2],[-1,-5,-9,7,-5,-3],[-7,-4,-3,3,2,2],[-10,-7,-10,-6,-3,7],[-4,-7,3,-1,-4,7],[9,3,7,7,8,8],[4,-7,6,2,-10,7],[8,-6,-5,2,-4,5],[10,-9,-5,-4,-2,7],[-7,-6,-7,2,4,-10],[2,-1,6,-10,-8,-5],[-7,-4,-4,-4,2,-9],[6,-4,9,9,7,8]],[[8,10,-6,-10,7,-1],[-7,-1,-7,-9,10,-5],[-9,-2,4,8,7,-7],[6,-7,1,2,-3,8],[1,-6,3,4,4,6],[6,-2,-5,-8,-6,2],[5,9,8,1,-7,2],[6,1,2,2,5,-10],[2,-9,-7,8,-8,-1],[6,-6,6,-4,6,6],[5,5,-9,8,5,10],[2,-3,4,-7,-5,-5],[2,5,3,5,7,-7]],[[5,8,5,-1,5,-7],[9,1,-8,-6,6,-8],[3,8,-3,8,8,-9],[5,10,-5,1,3,-1],[10,1,9,4,5,5],[5,-8,-1,-8,9,6],[-8,-10,-9,-2,-8,-5],[-2,-2,1,9,-3,10],[5,10,-9,8,3,6],[10,-1,1,-7,4,-4],[-9,10,-1,5,2,10],[4,-9,-9,-9,5,9],[-7,-10,8,-6,6,-8]],[[-10,-3,-2,4,-4,-3],[9,1,-3,9,7,-10],[3,3,-4,8,-7,6],[5,-3,2,9,-7,5],[-1,9,6,-4,-7,-2],[-9,5,-1,-5,-1,-3],[-6,4,5,5,-8,5],[-6,-6,-7,4,-9,3],[-7,4,7,-1,-2,-8],[6,2,-6,9,7,4],[4,-9,6,10,-10,-1],[4,2,9,-10,3,-1],[10,-2,-5,-8,-4,-1]]], dtype = "int8")#candidate|323|(7, 13, 6)|const|int8
var_324 = relay.var("var_324", dtype = "int8", shape = (7, 13, 6))#candidate|324|(7, 13, 6)|var|int8
bop_325 = relay.logical_xor(const_323.astype('int8'), relay.reshape(var_324.astype('int8'), relay.shape_of(const_323))) # shape=(7, 13, 6)
output = relay.Tuple([bop_325,])
output2 = relay.Tuple([bop_325,])
func_341 = relay.Function([var_324,], output)
mod['func_341'] = func_341
mod = relay.transform.InferType()(mod)
mutated_mod['func_341'] = func_341
mutated_mod = relay.transform.InferType()(mutated_mod)
var_342 = relay.var("var_342", dtype = "int8", shape = (7, 13, 6))#candidate|342|(7, 13, 6)|var|int8
func_341_call = mutated_mod.get_global_var('func_341')
call_343 = func_341_call(var_342)
output = call_343
func_344 = relay.Function([var_342], output)
mutated_mod['func_344'] = func_344
mutated_mod = relay.transform.InferType()(mutated_mod)
var_354 = relay.var("var_354", dtype = "float64", shape = (1, 4, 4))#candidate|354|(1, 4, 4)|var|float64
uop_355 = relay.sigmoid(var_354.astype('float64')) # shape=(1, 4, 4)
func_24_call = mod.get_global_var('func_24')
func_27_call = mutated_mod.get_global_var('func_27')
var_377 = relay.var("var_377", dtype = "int64", shape = ())#candidate|377|()|var|int64
call_376 = relay.TupleGetItem(func_24_call(relay.reshape(var_377.astype('int64'), [])), 0)
call_378 = relay.TupleGetItem(func_27_call(relay.reshape(var_377.astype('int64'), [])), 0)
output = relay.Tuple([uop_355,call_376,var_377,])
output2 = relay.Tuple([uop_355,call_378,var_377,])
func_386 = relay.Function([var_354,var_377,], output)
mod['func_386'] = func_386
mod = relay.transform.InferType()(mod)
var_387 = relay.var("var_387", dtype = "float64", shape = (1, 4, 4))#candidate|387|(1, 4, 4)|var|float64
var_388 = relay.var("var_388", dtype = "int64", shape = ())#candidate|388|()|var|int64
output = func_386(var_387,var_388,)
func_389 = relay.Function([var_387,var_388,], output)
mutated_mod['func_389'] = func_389
mutated_mod = relay.transform.InferType()(mutated_mod)
var_481 = relay.var("var_481", dtype = "int8", shape = (15, 10, 6))#candidate|481|(15, 10, 6)|var|int8
const_482 = relay.const([[[-8,-1,-6,-5,-8,7],[5,-5,3,-3,-1,4],[9,-9,6,-9,2,1],[3,-7,9,8,-4,-10],[2,-9,-2,-2,1,-6],[-5,1,-8,-5,10,-1],[8,5,-4,-8,-8,-9],[10,-1,-3,7,-5,5],[-1,-2,4,4,-5,-3],[-3,5,-10,10,-8,-10]],[[-2,-10,5,8,-8,9],[-6,-4,-1,1,-8,3],[-5,-7,-6,5,-5,-4],[-2,6,-3,-4,9,1],[4,2,-2,-7,10,9],[2,5,-9,-8,1,5],[-1,4,-8,8,9,-4],[-6,6,-7,-3,9,6],[7,2,-8,-2,7,-8],[1,7,-7,10,5,7]],[[-3,3,-8,-1,-3,-5],[-8,-9,-10,-10,-5,2],[-1,3,-10,-10,-3,-4],[-1,8,-8,4,-9,-10],[2,-2,6,-6,8,-3],[-2,-3,5,5,-4,10],[7,7,9,-5,-5,7],[-2,-10,-2,9,5,8],[1,6,8,7,-9,1],[10,-8,-4,-10,-8,7]],[[5,-6,9,-10,9,6],[-1,-3,7,-8,-2,4],[3,-10,-6,3,-4,2],[4,4,10,-1,4,3],[9,-10,10,-7,-8,4],[-6,5,-7,-3,-1,-4],[-8,-3,-8,4,10,10],[-8,2,4,1,-4,-7],[-5,2,7,8,1,-8],[8,8,-5,-7,-5,-10]],[[5,-6,10,-8,6,-3],[-5,8,2,5,-7,-7],[1,-7,3,5,1,-4],[7,-7,3,-7,1,-4],[-1,-3,2,-3,6,-1],[-7,4,8,-8,2,-9],[7,5,3,-1,8,3],[5,-7,3,-9,-2,10],[-3,-6,-6,-1,-5,1],[6,10,-5,8,-8,3]],[[10,-4,5,4,-2,6],[-9,1,5,-2,3,7],[-5,-9,7,-6,2,-1],[4,8,10,-6,-10,5],[-8,-4,-10,-8,-5,10],[9,-3,8,9,-3,-9],[-8,4,-3,-1,9,-3],[-8,2,10,-9,9,-9],[6,-8,4,4,2,9],[-10,-6,8,5,-10,3]],[[-10,8,-6,4,-2,3],[-10,7,-4,7,9,-2],[-5,-6,4,7,-4,3],[10,4,-2,10,-3,-5],[-5,10,8,-4,-8,9],[10,8,-9,-5,-10,2],[5,7,-1,2,7,-2],[7,9,6,7,-4,-1],[-8,3,-7,-4,-7,8],[-3,5,-6,6,-5,-7]],[[5,-9,3,-1,8,10],[8,-8,5,6,8,-8],[10,-6,-1,8,-10,-4],[-8,-3,10,4,7,5],[-7,10,4,-10,3,1],[-10,9,-7,5,9,-4],[3,-7,9,4,4,-3],[-3,-3,10,10,5,2],[-2,9,-6,10,-10,-2],[10,-7,10,-3,3,-7]],[[1,3,-7,-10,-3,-2],[-2,8,1,1,6,6],[-7,8,4,-3,5,1],[-10,-2,-1,-1,9,7],[9,-1,-7,10,-5,-4],[-4,-2,-10,10,5,2],[-10,-1,2,1,7,4],[-1,7,-3,-3,-5,-5],[-9,8,8,-1,5,-9],[3,8,-4,-3,-9,10]],[[-1,-8,-9,5,7,-3],[-3,7,-10,5,-8,3],[-5,8,-7,5,-3,-4],[5,10,1,9,10,4],[-2,-3,-1,-2,-1,2],[9,5,2,4,-9,7],[10,7,-2,9,-9,-4],[-9,1,-7,9,2,-7],[5,2,-8,7,-5,-7],[3,-10,-8,-5,1,8]],[[-10,-5,3,7,-3,-4],[-7,8,-3,-10,-9,-1],[5,6,3,-3,3,5],[9,-5,-10,5,10,-1],[8,-1,2,-6,7,4],[-9,3,6,-9,-10,1],[-1,-9,-10,4,-2,7],[-7,4,6,-6,-6,7],[6,6,10,6,-4,4],[5,-3,5,2,2,7]],[[-3,-5,3,8,-9,3],[-4,3,-6,-3,5,10],[6,3,8,-10,-3,10],[10,-5,-6,10,-9,-7],[10,-8,8,6,-9,-5],[-8,-8,1,-7,7,2],[2,3,-5,-8,10,9],[-1,-3,-3,-7,-3,-2],[-4,7,-2,-5,1,6],[8,-10,-10,-8,5,1]],[[-10,-10,7,9,-2,-3],[5,9,-5,1,-8,4],[1,9,3,-5,2,10],[-7,1,3,-6,-3,4],[1,-3,-6,9,9,5],[-9,9,-6,-9,5,-6],[5,9,-8,-7,-8,-8],[-7,4,-4,-2,-9,-4],[-9,2,4,-6,-2,6],[10,7,-4,-4,3,-1]],[[-7,3,5,5,-2,-9],[6,7,2,6,-9,-2],[1,7,6,-2,-10,-2],[-2,-10,3,5,7,-5],[-9,5,-5,2,4,7],[-7,4,-6,6,-1,-4],[-6,-4,-3,5,10,-10],[8,-9,3,-4,-9,-10],[5,4,-2,2,9,4],[5,-4,1,1,7,-4]],[[10,-3,-6,-3,-10,-7],[-5,-2,-5,6,8,-8],[-3,-10,1,-3,2,9],[8,7,6,10,-4,-6],[1,-10,2,-7,9,7],[3,-10,-5,-1,8,1],[-1,-9,-3,4,7,-2],[6,-5,-9,4,4,5],[2,2,-3,7,-4,-10],[1,3,-2,8,4,-2]]], dtype = "int8")#candidate|482|(15, 10, 6)|const|int8
bop_483 = relay.equal(var_481.astype('bool'), relay.reshape(const_482.astype('bool'), relay.shape_of(var_481))) # shape=(15, 10, 6)
output = relay.Tuple([bop_483,])
output2 = relay.Tuple([bop_483,])
func_522 = relay.Function([var_481,], output)
mod['func_522'] = func_522
mod = relay.transform.InferType()(mod)
mutated_mod['func_522'] = func_522
mutated_mod = relay.transform.InferType()(mutated_mod)
var_523 = relay.var("var_523", dtype = "int8", shape = (15, 10, 6))#candidate|523|(15, 10, 6)|var|int8
func_522_call = mutated_mod.get_global_var('func_522')
call_524 = func_522_call(var_523)
output = call_524
func_525 = relay.Function([var_523], output)
mutated_mod['func_525'] = func_525
mutated_mod = relay.transform.InferType()(mutated_mod)
const_589 = relay.const([[[-1,-4,3,-5,-7,10,-2,8,-10],[3,1,-7,-7,-7,4,-4,4,-4],[-3,10,1,-1,-4,3,1,7,-7],[5,7,-10,10,5,-3,-5,-9,-8],[4,-3,8,2,3,3,4,-4,10]],[[1,10,-7,7,1,6,-6,9,-9],[-5,-8,10,10,1,-2,-10,2,1],[4,1,1,5,8,-7,4,-7,4],[-6,-9,8,8,6,-5,1,-2,5],[2,3,7,-6,-5,3,-10,2,6]],[[1,-6,-3,-4,2,-9,-3,10,-8],[7,-6,-8,-2,8,6,-3,-7,7],[-4,6,-9,7,-3,-10,-4,6,-1],[-10,1,-8,1,7,2,10,5,4],[-1,7,-7,-5,-6,-10,-7,2,10]]], dtype = "int8")#candidate|589|(3, 5, 9)|const|int8
var_590 = relay.var("var_590", dtype = "int8", shape = (3, 5, 9))#candidate|590|(3, 5, 9)|var|int8
bop_591 = relay.bitwise_xor(const_589.astype('int8'), relay.reshape(var_590.astype('int8'), relay.shape_of(const_589))) # shape=(3, 5, 9)
output = bop_591
output2 = bop_591
func_607 = relay.Function([var_590,], output)
mod['func_607'] = func_607
mod = relay.transform.InferType()(mod)
mutated_mod['func_607'] = func_607
mutated_mod = relay.transform.InferType()(mutated_mod)
var_608 = relay.var("var_608", dtype = "int8", shape = (3, 5, 9))#candidate|608|(3, 5, 9)|var|int8
func_607_call = mutated_mod.get_global_var('func_607')
call_609 = func_607_call(var_608)
output = call_609
func_610 = relay.Function([var_608], output)
mutated_mod['func_610'] = func_610
mutated_mod = relay.transform.InferType()(mutated_mod)
const_735 = relay.const([[[-4,-7,-6,3,6],[-10,5,-2,7,-9],[-2,6,1,10,-8],[-7,5,-7,8,4]],[[1,6,9,-4,7],[-3,-10,-10,2,-4],[-2,-3,6,9,-2],[-9,-7,9,-4,-2]],[[-4,2,6,8,2],[6,-4,1,1,-5],[1,5,8,3,5],[-5,-10,7,-8,4]],[[9,-4,-1,5,2],[-4,-2,2,1,4],[-1,-8,-5,-9,-4],[-5,-2,-5,5,-4]],[[10,2,7,3,-3],[7,-5,7,2,5],[8,8,-10,-3,-3],[-1,-7,4,-1,3]]], dtype = "uint32")#candidate|735|(5, 4, 5)|const|uint32
var_736 = relay.var("var_736", dtype = "uint32", shape = (5, 4, 5))#candidate|736|(5, 4, 5)|var|uint32
bop_737 = relay.greater(const_735.astype('bool'), relay.reshape(var_736.astype('bool'), relay.shape_of(const_735))) # shape=(5, 4, 5)
bop_753 = relay.multiply(var_736.astype('int16'), relay.reshape(const_735.astype('int16'), relay.shape_of(var_736))) # shape=(5, 4, 5)
uop_756 = relay.asinh(bop_753.astype('float64')) # shape=(5, 4, 5)
output = relay.Tuple([bop_737,uop_756,])
output2 = relay.Tuple([bop_737,uop_756,])
func_759 = relay.Function([var_736,], output)
mod['func_759'] = func_759
mod = relay.transform.InferType()(mod)
var_760 = relay.var("var_760", dtype = "uint32", shape = (5, 4, 5))#candidate|760|(5, 4, 5)|var|uint32
output = func_759(var_760)
func_761 = relay.Function([var_760], output)
mutated_mod['func_761'] = func_761
mutated_mod = relay.transform.InferType()(mutated_mod)
var_837 = relay.var("var_837", dtype = "float64", shape = (13, 4, 9))#candidate|837|(13, 4, 9)|var|float64
uop_838 = relay.asinh(var_837.astype('float64')) # shape=(13, 4, 9)
func_386_call = mod.get_global_var('func_386')
func_389_call = mutated_mod.get_global_var('func_389')
const_841 = relay.const([-5.779170,-0.035620,1.360601,-2.219301,1.047402,-0.093026,5.737115,5.644542,-0.058861,-3.980741,-6.127460,-1.364947,-0.954754,-7.636991,-2.988283,-4.175958], dtype = "float64")#candidate|841|(16,)|const|float64
var_842 = relay.var("var_842", dtype = "int64", shape = ())#candidate|842|()|var|int64
call_840 = relay.TupleGetItem(func_386_call(relay.reshape(const_841.astype('float64'), [1, 4, 4]), relay.reshape(var_842.astype('int64'), []), ), 0)
call_843 = relay.TupleGetItem(func_389_call(relay.reshape(const_841.astype('float64'), [1, 4, 4]), relay.reshape(var_842.astype('int64'), []), ), 0)
output = relay.Tuple([uop_838,call_840,const_841,var_842,])
output2 = relay.Tuple([uop_838,call_843,const_841,var_842,])
func_847 = relay.Function([var_837,var_842,], output)
mod['func_847'] = func_847
mod = relay.transform.InferType()(mod)
var_848 = relay.var("var_848", dtype = "float64", shape = (13, 4, 9))#candidate|848|(13, 4, 9)|var|float64
var_849 = relay.var("var_849", dtype = "int64", shape = ())#candidate|849|()|var|int64
output = func_847(var_848,var_849,)
func_850 = relay.Function([var_848,var_849,], output)
mutated_mod['func_850'] = func_850
mutated_mod = relay.transform.InferType()(mutated_mod)
var_886 = relay.var("var_886", dtype = "float32", shape = (6, 16, 10))#candidate|886|(6, 16, 10)|var|float32
uop_887 = relay.log(var_886.astype('float32')) # shape=(6, 16, 10)
func_607_call = mod.get_global_var('func_607')
func_610_call = mutated_mod.get_global_var('func_610')
const_897 = relay.const([6,7,7,6,3,2,5,-8,7,7,-1,-3,-9,-2,-9,-4,-7,1,-4,-10,10,-1,-5,-3,-8,-4,-1,9,-5,-2,6,-7,6,-6,6,5,8,-1,4,3,-4,-4,6,-7,-2,5,-5,-10,-10,-9,-2,2,-10,-3,7,-8,-5,-8,-4,3,-5,6,1,-9,2,-7,2,-6,-2,-7,-5,4,7,-4,-8,-9,-3,5,2,-5,3,1,-1,8,-4,-6,9,-2,1,-9,2,4,-4,-9,2,-1,6,-10,6,2,-2,2,6,6,-1,8,3,-7,2,3,10,9,-7,2,-9,-7,1,-10,5,-6,-3,10,-8,-4,4,4,-3,-9,4,-6,-4,-3,4,3,9], dtype = "int8")#candidate|897|(135,)|const|int8
call_896 = func_607_call(relay.reshape(const_897.astype('int8'), [3, 5, 9]))
call_898 = func_607_call(relay.reshape(const_897.astype('int8'), [3, 5, 9]))
output = relay.Tuple([uop_887,call_896,const_897,])
output2 = relay.Tuple([uop_887,call_898,const_897,])
func_903 = relay.Function([var_886,], output)
mod['func_903'] = func_903
mod = relay.transform.InferType()(mod)
var_904 = relay.var("var_904", dtype = "float32", shape = (6, 16, 10))#candidate|904|(6, 16, 10)|var|float32
output = func_903(var_904)
func_905 = relay.Function([var_904], output)
mutated_mod['func_905'] = func_905
mutated_mod = relay.transform.InferType()(mutated_mod)
var_973 = relay.var("var_973", dtype = "float32", shape = (6, 1, 8))#candidate|973|(6, 1, 8)|var|float32
uop_974 = relay.log(var_973.astype('float32')) # shape=(6, 1, 8)
func_607_call = mod.get_global_var('func_607')
func_610_call = mutated_mod.get_global_var('func_610')
const_977 = relay.const([-4,-3,1,5,-7,10,1,-2,7,-5,-5,9,-10,-9,2,4,4,8,7,5,-8,-7,4,8,-1,8,-9,-8,-9,-5,7,-6,-9,8,-10,9,2,8,5,-5,-10,2,2,-10,9,2,7,8,-4,1,1,-3,7,-7,9,9,-7,-9,-3,9,-6,-7,-1,-8,-1,-9,2,5,5,-4,-8,-4,-7,5,3,1,5,2,-5,10,-3,10,3,7,-1,-2,5,5,8,2,-4,-1,-3,6,5,-7,5,4,-5,7,3,7,5,9,-10,7,6,-4,2,8,-3,8,2,-7,-4,-5,6,-4,-1,-6,-6,6,2,-2,7,-4,6,-2,5,-7,6,7,-3,-2,-5], dtype = "int8")#candidate|977|(135,)|const|int8
call_976 = func_607_call(relay.reshape(const_977.astype('int8'), [3, 5, 9]))
call_978 = func_607_call(relay.reshape(const_977.astype('int8'), [3, 5, 9]))
output = relay.Tuple([uop_974,call_976,const_977,])
output2 = relay.Tuple([uop_974,call_978,const_977,])
func_994 = relay.Function([var_973,], output)
mod['func_994'] = func_994
mod = relay.transform.InferType()(mod)
mutated_mod['func_994'] = func_994
mutated_mod = relay.transform.InferType()(mutated_mod)
var_995 = relay.var("var_995", dtype = "float32", shape = (6, 1, 8))#candidate|995|(6, 1, 8)|var|float32
func_994_call = mutated_mod.get_global_var('func_994')
call_996 = func_994_call(var_995)
output = call_996
func_997 = relay.Function([var_995], output)
mutated_mod['func_997'] = func_997
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1127 = relay.const([[[9.464563,8.253447,-6.509801,-4.618466,-7.532159,4.475445,3.157982,6.528376,1.009090,0.302254]],[[-4.144985,3.961662,-6.223986,-7.710198,1.253086,8.436492,-8.021559,-8.483744,-4.732534,8.636719]],[[-4.522932,-1.074534,-2.527108,3.856372,6.769777,2.693224,-0.428530,-3.170377,-7.529856,-3.371669]],[[-9.824076,-3.070154,-0.831075,-6.537911,5.780295,0.373131,-4.368035,5.642938,-1.028175,-6.759863]],[[-0.238008,1.248791,-6.606038,4.372493,-8.816867,-5.084174,8.980928,7.528430,6.693249,1.225678]],[[9.772373,-6.013481,-8.553649,2.361484,0.608325,-7.234819,7.429253,-0.540013,1.362906,-5.445521]],[[0.337396,7.090625,4.122657,-3.067483,-1.844386,4.686656,6.797969,6.508510,-1.857924,-4.294460]],[[-4.490677,3.833325,-0.360616,-3.467563,0.349545,3.854498,5.573700,2.757397,9.258716,-6.943673]],[[8.861889,-1.502215,9.194111,-6.572853,-2.178818,4.429702,1.635785,-8.873108,5.277400,-9.848555]],[[-5.681334,9.386626,-6.079273,-0.192308,1.377724,2.374002,9.352561,2.777982,4.133681,-6.215389]],[[-7.133626,-0.449599,-2.823697,9.696317,8.165368,-4.469558,3.580227,-5.325681,-7.743006,3.366973]],[[4.497581,8.813045,-8.184338,1.117011,-9.885826,9.302451,-8.130972,0.662461,7.370633,-5.136340]],[[-6.383563,-4.623945,-4.380616,5.766891,6.385061,-0.769448,7.417220,4.394366,-6.751355,1.129880]],[[-2.561393,7.591599,-1.564028,6.634852,7.038981,7.270768,-9.671108,4.262215,-1.495898,-7.229300]]], dtype = "float32")#candidate|1127|(14, 1, 10)|const|float32
uop_1128 = relay.sinh(const_1127.astype('float32')) # shape=(14, 1, 10)
output = relay.Tuple([uop_1128,])
output2 = relay.Tuple([uop_1128,])
func_1140 = relay.Function([], output)
mod['func_1140'] = func_1140
mod = relay.transform.InferType()(mod)
output = func_1140()
func_1141 = relay.Function([], output)
mutated_mod['func_1141'] = func_1141
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1140_call = mod.get_global_var('func_1140')
func_1141_call = mutated_mod.get_global_var('func_1141')
call_1172 = relay.TupleGetItem(func_1140_call(), 0)
call_1173 = relay.TupleGetItem(func_1141_call(), 0)
output = call_1172
output2 = call_1173
func_1178 = relay.Function([], output)
mod['func_1178'] = func_1178
mod = relay.transform.InferType()(mod)
mutated_mod['func_1178'] = func_1178
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1178_call = mutated_mod.get_global_var('func_1178')
call_1179 = func_1178_call()
output = call_1179
func_1180 = relay.Function([], output)
mutated_mod['func_1180'] = func_1180
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1140_call = mod.get_global_var('func_1140')
func_1141_call = mutated_mod.get_global_var('func_1141')
call_1184 = relay.TupleGetItem(func_1140_call(), 0)
call_1185 = relay.TupleGetItem(func_1141_call(), 0)
output = relay.Tuple([call_1184,])
output2 = relay.Tuple([call_1185,])
func_1187 = relay.Function([], output)
mod['func_1187'] = func_1187
mod = relay.transform.InferType()(mod)
output = func_1187()
func_1188 = relay.Function([], output)
mutated_mod['func_1188'] = func_1188
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1140_call = mod.get_global_var('func_1140')
func_1141_call = mutated_mod.get_global_var('func_1141')
call_1379 = relay.TupleGetItem(func_1140_call(), 0)
call_1380 = relay.TupleGetItem(func_1141_call(), 0)
func_1140_call = mod.get_global_var('func_1140')
func_1141_call = mutated_mod.get_global_var('func_1141')
call_1395 = relay.TupleGetItem(func_1140_call(), 0)
call_1396 = relay.TupleGetItem(func_1141_call(), 0)
func_341_call = mod.get_global_var('func_341')
func_344_call = mutated_mod.get_global_var('func_344')
const_1406 = relay.const([[-6,6,-9,3,-3,-2],[8,-4,1,-10,3,1],[-7,3,-6,6,9,9],[6,-3,7,-1,-1,9],[8,-6,-3,5,10,4],[6,-2,-9,-3,3,3],[-1,6,-9,7,6,-8],[-10,9,-2,8,10,-5],[10,-5,5,-4,2,10],[5,-7,-1,-10,-8,3],[-1,-10,-10,1,2,-5],[-3,5,9,7,3,4],[10,4,-2,-10,7,-5],[4,9,1,-4,2,-4],[-3,4,-6,9,-4,-6],[10,-9,-7,-6,-10,6],[10,10,9,1,-4,9],[5,9,-1,-6,-2,-9],[-1,9,-1,-5,-5,3],[8,8,-10,5,3,7],[-1,-6,-1,-2,-4,-6],[-6,-6,-7,-6,2,10],[-9,1,10,-7,-2,4],[1,-8,6,10,6,-4],[-6,7,-2,-1,-1,-4],[-10,-2,7,-10,1,-3],[-1,-3,-10,9,7,3],[-4,-2,-9,-7,-1,-3],[-4,-7,10,-6,-5,-7],[7,-3,3,-6,2,-5],[-6,10,-1,6,-6,2],[4,-7,8,8,-2,-10],[8,-6,-3,3,-3,-7],[-8,10,7,-1,4,2],[4,7,-2,4,10,2],[1,5,10,8,4,-1],[-2,3,-2,7,-6,1],[1,8,5,7,5,10],[3,-3,-6,9,9,-5],[7,-7,6,9,-3,-1],[8,6,9,1,4,10],[-8,-9,8,-8,-5,8],[-2,1,5,-8,1,6],[-10,3,-1,-3,1,-8],[5,6,2,3,10,-1],[-5,7,3,-7,2,-6],[-4,-2,10,-6,7,-4],[5,-4,1,-9,6,-4],[9,3,-1,4,9,-10],[7,3,9,4,-7,8],[-6,4,-5,1,10,-7],[3,8,-7,-1,6,10],[-3,9,5,-8,6,-10],[-2,5,5,7,-3,-9],[5,7,-4,-7,3,9],[-3,6,-2,-10,-9,10],[-7,1,-4,-10,-8,10],[-4,-3,3,5,-2,5],[9,-10,-10,-4,9,-7],[-6,2,4,8,-9,4],[-4,5,-10,-9,6,9],[2,-3,1,-4,6,10],[9,9,10,7,-2,9],[-5,-3,10,8,-7,2],[10,-4,-3,-10,4,-10],[1,-10,2,-5,8,7],[-1,-9,-6,6,-9,6],[-7,-6,-6,-5,6,9],[5,-4,-3,-2,-7,-5],[-3,1,-3,8,5,-1],[2,7,-1,3,-2,8],[9,-2,-2,9,9,-9],[-1,4,-3,-7,9,3],[2,-6,5,2,8,10],[4,-5,-1,7,3,8],[-6,-3,8,-7,-1,5],[-10,10,4,6,-1,-10],[9,-6,1,-10,-8,-4],[-8,5,5,-7,-8,3],[-9,7,-3,-4,-6,-5],[-2,-6,10,7,2,-1],[-3,-3,7,2,-6,8],[7,2,-10,-2,1,-5],[7,-1,3,5,-10,6],[4,-5,-6,-10,5,-8],[-8,-9,10,2,-5,6],[4,-3,-10,4,-6,6],[6,-7,-7,-7,-7,4],[2,3,-8,7,-2,8],[1,8,5,-1,8,-1],[3,10,4,-5,1,-6]], dtype = "int8")#candidate|1406|(91, 6)|const|int8
call_1405 = relay.TupleGetItem(func_341_call(relay.reshape(const_1406.astype('int8'), [7, 13, 6])), 0)
call_1407 = relay.TupleGetItem(func_344_call(relay.reshape(const_1406.astype('int8'), [7, 13, 6])), 0)
func_386_call = mod.get_global_var('func_386')
func_389_call = mutated_mod.get_global_var('func_389')
var_1414 = relay.var("var_1414", dtype = "float64", shape = (16,))#candidate|1414|(16,)|var|float64
var_1415 = relay.var("var_1415", dtype = "int64", shape = ())#candidate|1415|()|var|int64
call_1413 = relay.TupleGetItem(func_386_call(relay.reshape(var_1414.astype('float64'), [1, 4, 4]), relay.reshape(var_1415.astype('int64'), []), ), 2)
call_1416 = relay.TupleGetItem(func_389_call(relay.reshape(var_1414.astype('float64'), [1, 4, 4]), relay.reshape(var_1415.astype('int64'), []), ), 2)
output = relay.Tuple([call_1379,call_1395,call_1405,const_1406,call_1413,var_1414,var_1415,])
output2 = relay.Tuple([call_1380,call_1396,call_1407,const_1406,call_1416,var_1414,var_1415,])
func_1429 = relay.Function([var_1414,var_1415,], output)
mod['func_1429'] = func_1429
mod = relay.transform.InferType()(mod)
var_1430 = relay.var("var_1430", dtype = "float64", shape = (16,))#candidate|1430|(16,)|var|float64
var_1431 = relay.var("var_1431", dtype = "int64", shape = ())#candidate|1431|()|var|int64
output = func_1429(var_1430,var_1431,)
func_1432 = relay.Function([var_1430,var_1431,], output)
mutated_mod['func_1432'] = func_1432
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1443 = relay.var("var_1443", dtype = "float64", shape = (5, 15, 16))#candidate|1443|(5, 15, 16)|var|float64
var_1444 = relay.var("var_1444", dtype = "float64", shape = (5, 15, 16))#candidate|1444|(5, 15, 16)|var|float64
bop_1445 = relay.floor_divide(var_1443.astype('float64'), relay.reshape(var_1444.astype('float64'), relay.shape_of(var_1443))) # shape=(5, 15, 16)
output = bop_1445
output2 = bop_1445
func_1449 = relay.Function([var_1443,var_1444,], output)
mod['func_1449'] = func_1449
mod = relay.transform.InferType()(mod)
mutated_mod['func_1449'] = func_1449
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1449_call = mutated_mod.get_global_var('func_1449')
var_1451 = relay.var("var_1451", dtype = "float64", shape = (5, 15, 16))#candidate|1451|(5, 15, 16)|var|float64
var_1452 = relay.var("var_1452", dtype = "float64", shape = (5, 15, 16))#candidate|1452|(5, 15, 16)|var|float64
call_1450 = func_1449_call(var_1451,var_1452,)
output = call_1450
func_1453 = relay.Function([var_1451,var_1452,], output)
mutated_mod['func_1453'] = func_1453
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1187_call = mod.get_global_var('func_1187')
func_1188_call = mutated_mod.get_global_var('func_1188')
call_1461 = relay.TupleGetItem(func_1187_call(), 0)
call_1462 = relay.TupleGetItem(func_1188_call(), 0)
func_994_call = mod.get_global_var('func_994')
func_997_call = mutated_mod.get_global_var('func_997')
var_1470 = relay.var("var_1470", dtype = "float32", shape = (2, 24))#candidate|1470|(2, 24)|var|float32
call_1469 = relay.TupleGetItem(func_994_call(relay.reshape(var_1470.astype('float32'), [6, 1, 8])), 0)
call_1471 = relay.TupleGetItem(func_997_call(relay.reshape(var_1470.astype('float32'), [6, 1, 8])), 0)
func_759_call = mod.get_global_var('func_759')
func_761_call = mutated_mod.get_global_var('func_761')
const_1473 = relay.const([-8,-1,-5,-8,-1,6,1,9,6,3,5,-9,-10,2,-1,-1,2,-2,4,1,-9,9,3,-5,-3,4,-10,-7,-6,-10,10,5,-3,8,-7,5,5,5,5,10,10,-6,-9,-3,-5,-1,4,6,5,7,2,7,7,9,5,9,-5,4,-9,-8,-1,9,7,3,1,3,1,3,3,9,3,-3,-3,2,-5,-8,1,2,-7,9,4,-3,3,4,-10,-4,-2,-1,6,-9,-4,-7,-6,-1,3,-1,2,-5,-10,1], dtype = "uint32")#candidate|1473|(100,)|const|uint32
call_1472 = relay.TupleGetItem(func_759_call(relay.reshape(const_1473.astype('uint32'), [5, 4, 5])), 0)
call_1474 = relay.TupleGetItem(func_761_call(relay.reshape(const_1473.astype('uint32'), [5, 4, 5])), 0)
func_1140_call = mod.get_global_var('func_1140')
func_1141_call = mutated_mod.get_global_var('func_1141')
call_1475 = relay.TupleGetItem(func_1140_call(), 0)
call_1476 = relay.TupleGetItem(func_1141_call(), 0)
func_1178_call = mod.get_global_var('func_1178')
func_1180_call = mutated_mod.get_global_var('func_1180')
call_1477 = func_1178_call()
call_1478 = func_1178_call()
output = relay.Tuple([call_1461,call_1469,var_1470,call_1472,const_1473,call_1475,call_1477,])
output2 = relay.Tuple([call_1462,call_1471,var_1470,call_1474,const_1473,call_1476,call_1478,])
func_1486 = relay.Function([var_1470,], output)
mod['func_1486'] = func_1486
mod = relay.transform.InferType()(mod)
var_1487 = relay.var("var_1487", dtype = "float32", shape = (2, 24))#candidate|1487|(2, 24)|var|float32
output = func_1486(var_1487)
func_1488 = relay.Function([var_1487], output)
mutated_mod['func_1488'] = func_1488
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1140_call = mod.get_global_var('func_1140')
func_1141_call = mutated_mod.get_global_var('func_1141')
call_1555 = relay.TupleGetItem(func_1140_call(), 0)
call_1556 = relay.TupleGetItem(func_1141_call(), 0)
func_386_call = mod.get_global_var('func_386')
func_389_call = mutated_mod.get_global_var('func_389')
const_1576 = relay.const([[-3.986239,3.326551,0.937181,3.314529,2.300806,-7.035696,-2.723115,-2.115968,1.396844,-7.530379,1.944158,-3.173340,9.647243,5.411249,1.252286,-6.197791]], dtype = "float64")#candidate|1576|(1, 16)|const|float64
const_1577 = relay.const(-9, dtype = "int64")#candidate|1577|()|const|int64
call_1575 = relay.TupleGetItem(func_386_call(relay.reshape(const_1576.astype('float64'), [1, 4, 4]), relay.reshape(const_1577.astype('int64'), []), ), 2)
call_1578 = relay.TupleGetItem(func_389_call(relay.reshape(const_1576.astype('float64'), [1, 4, 4]), relay.reshape(const_1577.astype('int64'), []), ), 2)
output = relay.Tuple([call_1555,call_1575,const_1576,const_1577,])
output2 = relay.Tuple([call_1556,call_1578,const_1576,const_1577,])
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
call_1596 = relay.TupleGetItem(func_1580_call(), 3)
call_1597 = relay.TupleGetItem(func_1582_call(), 3)
output = relay.Tuple([call_1596,])
output2 = relay.Tuple([call_1597,])
func_1603 = relay.Function([], output)
mod['func_1603'] = func_1603
mod = relay.transform.InferType()(mod)
output = func_1603()
func_1604 = relay.Function([], output)
mutated_mod['func_1604'] = func_1604
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1603_call = mod.get_global_var('func_1603')
func_1604_call = mutated_mod.get_global_var('func_1604')
call_1612 = relay.TupleGetItem(func_1603_call(), 0)
call_1613 = relay.TupleGetItem(func_1604_call(), 0)
func_1580_call = mod.get_global_var('func_1580')
func_1582_call = mutated_mod.get_global_var('func_1582')
call_1617 = relay.TupleGetItem(func_1580_call(), 1)
call_1618 = relay.TupleGetItem(func_1582_call(), 1)
func_522_call = mod.get_global_var('func_522')
func_525_call = mutated_mod.get_global_var('func_525')
const_1620 = relay.const([-8,-2,-7,-1,6,-9,-1,5,-10,-3,-1,-10,-10,-10,-9,-8,5,3,10,-8,-4,-3,-3,5,7,4,-6,10,5,2,-2,-10,-10,-9,-9,-9,2,-9,2,-10,-10,8,1,4,9,-9,-6,-8,-5,9,1,-8,3,2,9,-6,-8,-7,-4,4,-6,-2,3,-1,6,4,-9,4,10,-7,6,10,-8,3,-7,-5,10,-9,9,3,1,5,-10,2,-3,-8,4,2,-6,-6,-2,10,-8,6,1,3,7,-2,4,-6,4,-5,4,2,4,5,-9,-9,3,4,-5,4,2,-8,3,-3,-9,-7,8,3,9,10,-2,-5,-4,-7,-4,2,10,-4,3,-1,-8,5,10,-7,-7,-7,8,2,-10,1,-1,-2,3,3,5,-10,2,6,5,-9,2,1,-7,-2,-3,3,-5,4,-2,6,1,-8,-3,-5,10,3,9,4,9,4,-10,-6,1,5,-1,1,-8,6,-3,-10,-4,-9,-6,-10,-10,5,-9,-6,-4,-4,-3,6,-3,-1,-1,3,3,-8,-6,2,-3,9,9,-2,8,8,2,3,4,2,-6,-3,-7,-7,-1,3,7,4,5,9,-4,5,8,-1,-3,-10,-10,-7,5,-1,3,8,4,-4,-2,4,-9,-1,-8,-1,-7,-9,7,-3,-8,-9,-8,8,1,-3,-6,-10,-10,6,-3,-9,10,-7,-2,9,5,-10,7,7,2,2,10,7,-2,8,-9,-8,-2,8,-5,5,-7,7,3,-1,-5,-6,-4,5,-3,-3,-9,-1,-8,-7,6,-5,7,6,-5,8,9,-4,-5,10,1,10,6,1,10,7,1,10,3,9,-2,-7,-9,5,2,-1,9,-5,3,-7,5,1,-5,4,-9,-5,10,-4,-4,4,-6,-9,8,-10,-9,4,-2,-9,-7,6,-4,9,-2,4,3,2,-4,-4,4,-3,-4,8,-3,-2,8,8,-8,7,-1,-6,10,6,8,6,6,6,6,6,10,2,8,1,9,8,10,6,1,-4,4,10,9,1,-1,-5,-7,-9,8,-2,10,9,-1,2,9,-10,7,-4,-7,10,-2,-7,1,-5,-5,-6,-7,5,-1,10,2,-2,2,-5,-1,-5,9,3,9,1,-6,-9,1,1,-2,2,2,4,2,-1,4,9,9,5,1,-1,2,-8,-5,-9,-9,-10,-6,5,4,4,-3,1,-4,-9,4,-4,4,-3,10,-6,2,-1,2,8,-1,4,-5,5,5,6,6,8,-1,-8,3,-3,-4,5,10,2,8,-3,-4,2,-4,1,-8,1,9,4,5,-9,2,5,-1,-1,-6,2,5,-1,4,-9,10,4,9,-5,5,-5,10,-9,8,8,6,-4,-3,8,-7,-2,6,8,5,-2,-7,-9,7,-8,8,9,-7,3,-9,9,-9,-7,-8,2,8,6,-5,4,1,-8,-1,2,-1,-10,-7,10,-4,3,-2,7,-3,7,8,-9,-7,-9,-2,-6,8,-5,9,-1,2,4,10,-4,-6,8,-4,4,-2,10,6,10,6,-6,-1,-7,-2,-7,-4,-5,3,6,-2,1,-5,-1,8,2,-7,8,-9,2,-8,4,-9,-4,-4,-10,-1,2,1,-5,-3,3,-7,-9,-6,8,10,-5,2,-1,-8,-3,-1,2,-8,-1,6,-4,-4,9,-6,1,-8,-4,6,7,8,4,6,-9,5,-7,3,3,-4,7,-7,5,7,-4,-7,-8,10,2,7,10,3,-2,9,-6,-6,-3,1,8,7,2,2,7,-1,-10,2,2,-1,4,2,3,10,10,-3,-1,2,-4,-3,-8,2,5,-2,-9,-3,-1,10,-2,-1,4,-3,-2,-8,9,9,-6,-7,-5,7,-2,-7,-5,8,-1,-2,-10,-10,1,-1,7,-2,-9,3,-10,7,1,4,5,5,-8,1,-5,-2,-8,9,-1,8,1,-5,2,-2,8,-10,5,-10,-4,3,-1,8,-6,-5,-9,8,-4,1,-4,8,-9,6,-4,9,7,-7,-6,8,-3,2,5,4,-2,-5,9,2,-10,2,-7,1,-4,2,5,-4,10,2,6,5,10,6,-1,-7,-9,6,3,-9,6,-7,-9,1,4,7,9,8,9,-1,4,-3,1,10,7,-9,1,5,-6,3,10,-10,9,-10,-1,3,1,10,-5,5,10,-6,9,-2,10,5,-3,-10,-2,-3,5,10,-1,-7,-1,-2,-6,3,-2,2,-10,3,-1,-8,-5,-6,8,-6,6,-7,8,9,8,1,7,-9,10,10,6,2,8,2,2,7,3,-7,3,-5,8,-10,-7,9,2,-9,-9,10,7,-5,1,-8,-6,-5,1,-10,6,-1,3,-10,-3,-3,-10,-10,-6,7,-5,-2,-2,-9,-7,-3,3,5,5,-8,4,1,-4,-2,-5,8,6], dtype = "int8")#candidate|1620|(900,)|const|int8
call_1619 = relay.TupleGetItem(func_522_call(relay.reshape(const_1620.astype('int8'), [15, 10, 6])), 0)
call_1621 = relay.TupleGetItem(func_525_call(relay.reshape(const_1620.astype('int8'), [15, 10, 6])), 0)
func_1140_call = mod.get_global_var('func_1140')
func_1141_call = mutated_mod.get_global_var('func_1141')
call_1667 = relay.TupleGetItem(func_1140_call(), 0)
call_1668 = relay.TupleGetItem(func_1141_call(), 0)
output = relay.Tuple([call_1612,call_1617,call_1619,const_1620,call_1667,])
output2 = relay.Tuple([call_1613,call_1618,call_1621,const_1620,call_1668,])
func_1674 = relay.Function([], output)
mod['func_1674'] = func_1674
mod = relay.transform.InferType()(mod)
output = func_1674()
func_1675 = relay.Function([], output)
mutated_mod['func_1675'] = func_1675
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1580_call = mod.get_global_var('func_1580')
func_1582_call = mutated_mod.get_global_var('func_1582')
call_1716 = relay.TupleGetItem(func_1580_call(), 3)
call_1717 = relay.TupleGetItem(func_1582_call(), 3)
output = relay.Tuple([call_1716,])
output2 = relay.Tuple([call_1717,])
func_1748 = relay.Function([], output)
mod['func_1748'] = func_1748
mod = relay.transform.InferType()(mod)
mutated_mod['func_1748'] = func_1748
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1748_call = mutated_mod.get_global_var('func_1748')
call_1749 = func_1748_call()
output = call_1749
func_1750 = relay.Function([], output)
mutated_mod['func_1750'] = func_1750
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1674_call = mod.get_global_var('func_1674')
func_1675_call = mutated_mod.get_global_var('func_1675')
call_1776 = relay.TupleGetItem(func_1674_call(), 4)
call_1777 = relay.TupleGetItem(func_1675_call(), 4)
output = call_1776
output2 = call_1777
func_1801 = relay.Function([], output)
mod['func_1801'] = func_1801
mod = relay.transform.InferType()(mod)
mutated_mod['func_1801'] = func_1801
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1801_call = mutated_mod.get_global_var('func_1801')
call_1802 = func_1801_call()
output = call_1802
func_1803 = relay.Function([], output)
mutated_mod['func_1803'] = func_1803
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1748_call = mod.get_global_var('func_1748')
func_1750_call = mutated_mod.get_global_var('func_1750')
call_1843 = relay.TupleGetItem(func_1748_call(), 0)
call_1844 = relay.TupleGetItem(func_1750_call(), 0)
output = relay.Tuple([call_1843,])
output2 = relay.Tuple([call_1844,])
func_1859 = relay.Function([], output)
mod['func_1859'] = func_1859
mod = relay.transform.InferType()(mod)
mutated_mod['func_1859'] = func_1859
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1859_call = mutated_mod.get_global_var('func_1859')
call_1860 = func_1859_call()
output = call_1860
func_1861 = relay.Function([], output)
mutated_mod['func_1861'] = func_1861
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1801_call = mod.get_global_var('func_1801')
func_1803_call = mutated_mod.get_global_var('func_1803')
call_1908 = func_1801_call()
call_1909 = func_1801_call()
func_24_call = mod.get_global_var('func_24')
func_27_call = mutated_mod.get_global_var('func_27')
const_1914 = relay.const(-7, dtype = "int64")#candidate|1914|()|const|int64
call_1913 = relay.TupleGetItem(func_24_call(relay.reshape(const_1914.astype('int64'), [])), 0)
call_1915 = relay.TupleGetItem(func_27_call(relay.reshape(const_1914.astype('int64'), [])), 0)
func_1429_call = mod.get_global_var('func_1429')
func_1432_call = mutated_mod.get_global_var('func_1432')
const_1917 = relay.const([-6.351524,-8.246906,3.967377,-1.433998,1.620952,0.664775,3.692493,-9.508857,-4.786047,-4.988900,6.198151,2.959489,8.294852,-8.869846,0.642474,-4.092237], dtype = "float64")#candidate|1917|(16,)|const|float64
call_1916 = relay.TupleGetItem(func_1429_call(relay.reshape(const_1917.astype('float64'), [16,]), relay.reshape(const_1914.astype('int64'), []), ), 2)
call_1918 = relay.TupleGetItem(func_1432_call(relay.reshape(const_1917.astype('float64'), [16,]), relay.reshape(const_1914.astype('int64'), []), ), 2)
output = relay.Tuple([call_1908,call_1913,const_1914,call_1916,const_1917,])
output2 = relay.Tuple([call_1909,call_1915,const_1914,call_1918,const_1917,])
func_1920 = relay.Function([], output)
mod['func_1920'] = func_1920
mod = relay.transform.InferType()(mod)
mutated_mod['func_1920'] = func_1920
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1920_call = mutated_mod.get_global_var('func_1920')
call_1921 = func_1920_call()
output = call_1921
func_1922 = relay.Function([], output)
mutated_mod['func_1922'] = func_1922
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1580_call = mod.get_global_var('func_1580')
func_1582_call = mutated_mod.get_global_var('func_1582')
call_1929 = relay.TupleGetItem(func_1580_call(), 2)
call_1930 = relay.TupleGetItem(func_1582_call(), 2)
func_994_call = mod.get_global_var('func_994')
func_997_call = mutated_mod.get_global_var('func_997')
const_1933 = relay.const([5.143811,-8.406882,-0.411344,5.547299,-2.015859,3.672181,-9.237216,4.359368,-4.333123,-9.248314,-1.005530,7.737668,9.600684,-2.309460,3.061471,-6.839255,6.921540,9.857547,-8.797884,-0.245862,-3.557462,-7.476187,-5.441971,4.008092,2.748359,-0.439162,-8.880565,2.548977,-1.897553,-0.673326,1.258267,1.902326,1.604521,8.818200,6.850140,8.970249,6.592481,-6.296735,3.164445,-2.837601,4.895103,-8.790004,0.222238,-6.993744,-8.368602,0.526000,1.519383,-7.457726], dtype = "float32")#candidate|1933|(48,)|const|float32
call_1932 = relay.TupleGetItem(func_994_call(relay.reshape(const_1933.astype('float32'), [6, 1, 8])), 0)
call_1934 = relay.TupleGetItem(func_997_call(relay.reshape(const_1933.astype('float32'), [6, 1, 8])), 0)
output = relay.Tuple([call_1929,call_1932,const_1933,])
output2 = relay.Tuple([call_1930,call_1934,const_1933,])
func_1940 = relay.Function([], output)
mod['func_1940'] = func_1940
mod = relay.transform.InferType()(mod)
mutated_mod['func_1940'] = func_1940
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1940_call = mutated_mod.get_global_var('func_1940')
call_1941 = func_1940_call()
output = call_1941
func_1942 = relay.Function([], output)
mutated_mod['func_1942'] = func_1942
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1603_call = mod.get_global_var('func_1603')
func_1604_call = mutated_mod.get_global_var('func_1604')
call_1968 = relay.TupleGetItem(func_1603_call(), 0)
call_1969 = relay.TupleGetItem(func_1604_call(), 0)
func_1140_call = mod.get_global_var('func_1140')
func_1141_call = mutated_mod.get_global_var('func_1141')
call_1974 = relay.TupleGetItem(func_1140_call(), 0)
call_1975 = relay.TupleGetItem(func_1141_call(), 0)
output = relay.Tuple([call_1968,call_1974,])
output2 = relay.Tuple([call_1969,call_1975,])
func_1984 = relay.Function([], output)
mod['func_1984'] = func_1984
mod = relay.transform.InferType()(mod)
output = func_1984()
func_1985 = relay.Function([], output)
mutated_mod['func_1985'] = func_1985
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1748_call = mod.get_global_var('func_1748')
func_1750_call = mutated_mod.get_global_var('func_1750')
call_1998 = relay.TupleGetItem(func_1748_call(), 0)
call_1999 = relay.TupleGetItem(func_1750_call(), 0)
func_1187_call = mod.get_global_var('func_1187')
func_1188_call = mutated_mod.get_global_var('func_1188')
call_2000 = relay.TupleGetItem(func_1187_call(), 0)
call_2001 = relay.TupleGetItem(func_1188_call(), 0)
func_1580_call = mod.get_global_var('func_1580')
func_1582_call = mutated_mod.get_global_var('func_1582')
call_2002 = relay.TupleGetItem(func_1580_call(), 0)
call_2003 = relay.TupleGetItem(func_1582_call(), 0)
bop_2004 = relay.greater_equal(call_2000.astype('bool'), call_1998.astype('bool')) # shape=(14, 1, 10)
bop_2007 = relay.greater_equal(call_2001.astype('bool'), call_1999.astype('bool')) # shape=(14, 1, 10)
output = relay.Tuple([call_2002,bop_2004,])
output2 = relay.Tuple([call_2003,bop_2007,])
func_2009 = relay.Function([], output)
mod['func_2009'] = func_2009
mod = relay.transform.InferType()(mod)
mutated_mod['func_2009'] = func_2009
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2009_call = mutated_mod.get_global_var('func_2009')
call_2010 = func_2009_call()
output = call_2010
func_2011 = relay.Function([], output)
mutated_mod['func_2011'] = func_2011
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2009_call = mod.get_global_var('func_2009')
func_2011_call = mutated_mod.get_global_var('func_2011')
call_2128 = relay.TupleGetItem(func_2009_call(), 0)
call_2129 = relay.TupleGetItem(func_2011_call(), 0)
uop_2132 = relay.atanh(call_2128.astype('float32')) # shape=(14, 1, 10)
uop_2134 = relay.atanh(call_2129.astype('float32')) # shape=(14, 1, 10)
output = relay.Tuple([uop_2132,])
output2 = relay.Tuple([uop_2134,])
func_2145 = relay.Function([], output)
mod['func_2145'] = func_2145
mod = relay.transform.InferType()(mod)
output = func_2145()
func_2146 = relay.Function([], output)
mutated_mod['func_2146'] = func_2146
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1580_call = mod.get_global_var('func_1580')
func_1582_call = mutated_mod.get_global_var('func_1582')
call_2181 = relay.TupleGetItem(func_1580_call(), 0)
call_2182 = relay.TupleGetItem(func_1582_call(), 0)
func_994_call = mod.get_global_var('func_994')
func_997_call = mutated_mod.get_global_var('func_997')
var_2185 = relay.var("var_2185", dtype = "float32", shape = (48,))#candidate|2185|(48,)|var|float32
call_2184 = relay.TupleGetItem(func_994_call(relay.reshape(var_2185.astype('float32'), [6, 1, 8])), 2)
call_2186 = relay.TupleGetItem(func_997_call(relay.reshape(var_2185.astype('float32'), [6, 1, 8])), 2)
func_1674_call = mod.get_global_var('func_1674')
func_1675_call = mutated_mod.get_global_var('func_1675')
call_2187 = relay.TupleGetItem(func_1674_call(), 1)
call_2188 = relay.TupleGetItem(func_1675_call(), 1)
output = relay.Tuple([call_2181,call_2184,var_2185,call_2187,])
output2 = relay.Tuple([call_2182,call_2186,var_2185,call_2188,])
func_2196 = relay.Function([var_2185,], output)
mod['func_2196'] = func_2196
mod = relay.transform.InferType()(mod)
var_2197 = relay.var("var_2197", dtype = "float32", shape = (48,))#candidate|2197|(48,)|var|float32
output = func_2196(var_2197)
func_2198 = relay.Function([var_2197], output)
mutated_mod['func_2198'] = func_2198
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2145_call = mod.get_global_var('func_2145')
func_2146_call = mutated_mod.get_global_var('func_2146')
call_2219 = relay.TupleGetItem(func_2145_call(), 0)
call_2220 = relay.TupleGetItem(func_2146_call(), 0)
func_994_call = mod.get_global_var('func_994')
func_997_call = mutated_mod.get_global_var('func_997')
var_2240 = relay.var("var_2240", dtype = "float32", shape = (48,))#candidate|2240|(48,)|var|float32
call_2239 = relay.TupleGetItem(func_994_call(relay.reshape(var_2240.astype('float32'), [6, 1, 8])), 0)
call_2241 = relay.TupleGetItem(func_997_call(relay.reshape(var_2240.astype('float32'), [6, 1, 8])), 0)
output = relay.Tuple([call_2219,call_2239,var_2240,])
output2 = relay.Tuple([call_2220,call_2241,var_2240,])
func_2243 = relay.Function([var_2240,], output)
mod['func_2243'] = func_2243
mod = relay.transform.InferType()(mod)
var_2244 = relay.var("var_2244", dtype = "float32", shape = (48,))#candidate|2244|(48,)|var|float32
output = func_2243(var_2244)
func_2245 = relay.Function([var_2244], output)
mutated_mod['func_2245'] = func_2245
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1580_call = mod.get_global_var('func_1580')
func_1582_call = mutated_mod.get_global_var('func_1582')
call_2278 = relay.TupleGetItem(func_1580_call(), 0)
call_2279 = relay.TupleGetItem(func_1582_call(), 0)
output = call_2278
output2 = call_2279
func_2282 = relay.Function([], output)
mod['func_2282'] = func_2282
mod = relay.transform.InferType()(mod)
output = func_2282()
func_2283 = relay.Function([], output)
mutated_mod['func_2283'] = func_2283
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1178_call = mod.get_global_var('func_1178')
func_1180_call = mutated_mod.get_global_var('func_1180')
call_2317 = func_1178_call()
call_2318 = func_1178_call()
func_1580_call = mod.get_global_var('func_1580')
func_1582_call = mutated_mod.get_global_var('func_1582')
call_2340 = relay.TupleGetItem(func_1580_call(), 1)
call_2341 = relay.TupleGetItem(func_1582_call(), 1)
func_1674_call = mod.get_global_var('func_1674')
func_1675_call = mutated_mod.get_global_var('func_1675')
call_2345 = relay.TupleGetItem(func_1674_call(), 1)
call_2346 = relay.TupleGetItem(func_1675_call(), 1)
func_903_call = mod.get_global_var('func_903')
func_905_call = mutated_mod.get_global_var('func_905')
var_2348 = relay.var("var_2348", dtype = "float32", shape = (960,))#candidate|2348|(960,)|var|float32
call_2347 = relay.TupleGetItem(func_903_call(relay.reshape(var_2348.astype('float32'), [6, 16, 10])), 1)
call_2349 = relay.TupleGetItem(func_905_call(relay.reshape(var_2348.astype('float32'), [6, 16, 10])), 1)
output = relay.Tuple([call_2317,call_2340,call_2345,call_2347,var_2348,])
output2 = relay.Tuple([call_2318,call_2341,call_2346,call_2349,var_2348,])
func_2351 = relay.Function([var_2348,], output)
mod['func_2351'] = func_2351
mod = relay.transform.InferType()(mod)
mutated_mod['func_2351'] = func_2351
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2352 = relay.var("var_2352", dtype = "float32", shape = (960,))#candidate|2352|(960,)|var|float32
func_2351_call = mutated_mod.get_global_var('func_2351')
call_2353 = func_2351_call(var_2352)
output = call_2353
func_2354 = relay.Function([var_2352], output)
mutated_mod['func_2354'] = func_2354
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2145_call = mod.get_global_var('func_2145')
func_2146_call = mutated_mod.get_global_var('func_2146')
call_2374 = relay.TupleGetItem(func_2145_call(), 0)
call_2375 = relay.TupleGetItem(func_2146_call(), 0)
func_1603_call = mod.get_global_var('func_1603')
func_1604_call = mutated_mod.get_global_var('func_1604')
call_2379 = relay.TupleGetItem(func_1603_call(), 0)
call_2380 = relay.TupleGetItem(func_1604_call(), 0)
output = relay.Tuple([call_2374,call_2379,])
output2 = relay.Tuple([call_2375,call_2380,])
func_2401 = relay.Function([], output)
mod['func_2401'] = func_2401
mod = relay.transform.InferType()(mod)
output = func_2401()
func_2402 = relay.Function([], output)
mutated_mod['func_2402'] = func_2402
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2459 = relay.var("var_2459", dtype = "int8", shape = (6, 16, 1))#candidate|2459|(6, 16, 1)|var|int8
var_2460 = relay.var("var_2460", dtype = "int8", shape = (6, 16, 4))#candidate|2460|(6, 16, 4)|var|int8
bop_2461 = relay.right_shift(var_2459.astype('int8'), var_2460.astype('int8')) # shape=(6, 16, 4)
var_2471 = relay.var("var_2471", dtype = "int8", shape = (6, 16, 4))#candidate|2471|(6, 16, 4)|var|int8
bop_2472 = relay.minimum(bop_2461.astype('uint8'), relay.reshape(var_2471.astype('uint8'), relay.shape_of(bop_2461))) # shape=(6, 16, 4)
func_2351_call = mod.get_global_var('func_2351')
func_2354_call = mutated_mod.get_global_var('func_2354')
const_2484 = relay.const([8.318957,0.193607,4.998498,-7.629045,-2.076735,4.382258,7.296566,-7.800240,6.868983,5.018651,-8.078722,9.808590,5.343112,3.378710,-9.240135,3.810097,-3.809704,-5.771879,-4.103743,0.396822,3.861518,3.002872,-0.953003,1.860809,-9.702377,-5.019237,-5.597591,5.513682,-4.142844,-9.698686,7.951022,-6.749754,-0.453579,8.154030,3.073797,-1.427431,-7.905160,-4.977435,0.150978,-8.426484,-1.219447,-8.135974,-9.613100,-7.010479,1.113096,5.936794,6.655133,-1.338116,-0.253852,-7.150150,-9.042878,-3.692134,8.370408,5.544674,-4.416492,-1.714313,-5.183949,-2.276873,-7.654301,6.995178,0.449078,-5.417387,-9.618188,9.348952,8.454709,5.497866,-5.180041,-0.180014,-4.877646,-9.719883,7.304771,0.258181,-5.092330,-9.105677,-0.569681,-0.426208,-9.854986,-1.763804,5.952946,8.009972,-4.302129,-0.545029,-0.240310,-6.973631,-4.879211,-3.644557,5.991957,8.937283,1.459126,-2.136627,8.864533,9.183588,5.871083,-6.099899,7.527033,0.332904,-3.523271,-3.655458,-6.669726,1.815877,-6.162211,-7.170224,8.339223,1.539451,3.116297,9.099100,-6.783635,-8.305431,-3.477688,-8.092026,-8.794791,8.774984,2.774305,-6.215476,-4.732997,-0.462221,1.496854,-7.310484,-1.052130,3.371745,8.767311,-3.617804,8.083299,-1.586343,6.532028,-8.720273,-5.102524,3.978069,2.553516,-5.398698,3.583385,-6.033833,3.454795,-8.828410,-4.905839,-0.919064,-8.839129,8.917638,4.285659,9.367799,-1.083864,5.904980,-4.418623,-5.885690,-5.507328,9.551592,6.113890,-1.063441,4.782601,-9.681195,-7.938205,0.009304,5.260120,-6.375170,-8.012650,-6.867137,5.629859,-1.208192,-6.951182,-5.732776,3.483776,-7.671540,5.722791,2.681488,4.793327,1.206911,-4.122715,-7.852398,0.529734,9.331800,6.582505,7.618926,6.162541,-2.259867,-5.087223,-2.140568,-8.405185,8.919929,0.934635,-1.913488,-6.431070,-1.818582,7.710756,5.072470,7.755234,-9.839279,-6.094766,-3.052355,1.886867,6.147918,5.708142,9.485571,-1.915500,0.554653,-5.045970,2.846604,8.929187,8.717365,-3.949505,-4.409811,2.129214,-6.247628,-3.011505,7.422096,5.603655,8.293076,-0.580445,8.697858,2.827519,-1.676297,-4.014086,7.482471,3.429432,-8.272909,2.797844,-7.718388,-3.007501,-6.465025,0.017270,-1.948266,-9.761979,8.067988,1.737727,5.571989,7.985775,-6.837530,7.638540,-0.421223,-4.423087,8.358294,9.235599,7.592401,-8.923327,-9.650130,8.835751,6.476268,-5.031320,8.128987,2.368417,2.833072,-9.685471,-4.548034,6.421395,5.979042,-5.813731,4.738507,-3.230483,5.191297,-7.718651,-5.568340,-7.501070,6.166675,-5.137798,-3.914132,6.640554,-6.435622,6.340623,-8.960699,4.061435,8.731957,-8.835899,0.913564,9.088177,6.283498,-8.835270,0.278735,1.656105,-3.452221,1.220660,3.676024,-3.912940,0.788900,8.998037,-6.137537,2.741930,-0.589896,-4.858197,-0.078311,-8.092846,5.613891,3.274654,0.760391,1.804884,-7.026857,2.566707,8.075174,0.267657,9.384345,-1.983283,-9.829239,3.654134,4.665682,-6.638388,0.602434,-5.861603,-8.351806,-0.561906,-1.099025,0.725271,-2.809774,1.523517,-0.833975,-5.618541,5.134784,9.602841,-7.592497,-7.755455,-9.832067,0.054080,6.778902,-0.083673,9.975363,2.356223,-2.304346,-7.753273,1.346313,-5.949078,9.766274,-6.615525,-4.686130,-4.196084,-1.691024,-4.483892,4.851925,8.878576,7.015373,-1.506857,-4.542540,3.811992,-3.751448,1.898548,3.171890,7.142722,0.718316,0.283707,8.567714,-0.464799,-5.137207,-2.455137,9.693710,-7.665984,1.923814,3.518864,-9.344865,-0.844329,0.803450,9.436604,-7.081264,3.561890,-0.073394,2.890413,-9.945525,8.884418,-5.786961,-9.772048,9.911183,4.443717,-7.274178,-5.600144,2.702297,2.342260,6.948176,8.116663,-4.579509,4.522529,7.637742,-3.987960,-7.153008,-6.402443,-7.518000,-6.184817,9.322767,-4.406114,1.742398,-1.431444,-3.739666,3.987914,-1.806684,0.556715,1.300581,3.140371,9.958926,-0.081710,-1.095761,-2.028225,8.055003,-0.507265,-5.437064,-5.352965,-7.936732,-7.102247,1.112165,-2.738702,-9.026908,-1.165190,-8.042370,-9.415913,3.753382,3.015620,6.544359,-0.221783,1.904385,3.861316,-3.204089,0.660729,2.950582,1.522403,3.859155,-4.248608,5.685130,5.269985,7.224039,0.971868,-9.019281,-7.287822,-9.673264,-5.641899,4.904516,-6.421800,-9.582427,-9.410430,9.862635,-2.544598,4.540698,7.156227,9.553251,-0.166898,-7.976108,1.324035,3.767931,4.406452,9.694414,3.240887,9.087095,-5.416641,4.760057,8.965269,-6.872056,4.413842,3.232200,-1.173564,4.096465,3.145920,-9.053499,-0.549523,-0.924142,6.284255,1.592864,-1.936342,-4.538024,-7.486742,-8.389128,7.334134,1.992296,-2.203760,8.048166,6.564879,-2.554966,-2.908388,-3.467232,-0.901023,-3.733193,-1.332545,-6.943498,3.853611,2.264914,-5.857837,3.506542,-4.695173,-3.018494,7.958131,6.337229,-8.431064,5.918690,-2.943081,7.338723,-0.215338,-3.440265,6.265765,-8.625126,-8.902266,4.903713,7.157662,-7.948971,0.387377,-4.972393,-9.838197,-0.516382,5.796295,0.702944,6.816221,-8.290399,4.067020,-3.949836,8.544009,7.729896,-6.045214,-6.767834,3.257765,4.486273,0.859602,-8.443223,7.100640,-1.823377,-7.815967,-1.896652,-7.191942,-3.567022,8.197030,8.998938,5.333837,-8.174225,7.496552,9.028315,3.470932,5.989201,-5.964218,-2.001903,-2.934964,4.930763,2.055470,-9.249844,-1.493388,1.839449,4.543943,4.920646,6.139191,-3.636741,-0.931716,5.970979,-8.659226,6.702081,-0.588316,-2.924349,-8.887857,-4.897148,3.897966,-6.309154,3.141852,-7.658861,-6.416421,2.715631,1.893883,-0.846353,3.598620,-2.202693,-9.302810,-1.861731,2.263235,-8.843774,-2.633856,7.249756,8.449547,-9.289824,0.602733,-1.012139,-4.695327,5.650330,9.117205,6.240419,-8.084458,7.404049,7.291065,6.895257,-3.797329,7.355646,-2.373344,9.356045,-9.811781,-1.776743,-7.856860,8.601950,-5.109454,-1.410469,-6.371898,-8.017715,1.393363,4.784217,-3.595093,-4.244943,-2.960087,5.866760,-5.016779,1.094703,-2.788366,2.159960,-2.806430,0.899962,8.083342,-2.899519,-6.596312,-7.162522,-5.918339,-2.900070,5.077333,-6.129864,-1.326279,-3.182969,-5.879502,6.749648,-3.280087,4.693435,5.696231,5.983740,-6.430153,-9.059126,9.934643,0.607583,1.655725,-2.903345,-7.908679,-5.526847,-5.936788,4.830340,-8.132989,-8.614985,7.779196,0.852800,-8.172452,-2.069054,5.686554,7.046485,2.511222,-5.446306,3.340677,4.015174,7.751554,-0.630784,4.757655,-7.804757,6.916407,-5.659705,-1.317176,8.922451,-7.402427,-9.263147,1.022467,-6.435525,-0.596866,4.412791,9.238829,7.254416,-4.419701,6.788332,4.057172,-8.458573,-5.810807,-4.872592,-6.878603,3.960894,8.385210,-8.392729,-9.308639,3.235477,-9.712255,-8.888022,-5.139849,-4.043067,2.933322,-3.231879,-2.094767,2.298500,4.514995,5.647410,-0.383488,-0.146492,-8.001703,-4.561317,-1.472030,7.779824,-0.811648,-8.814720,1.461512,3.382076,-2.252016,-4.904928,-7.982859,8.608489,9.347086,-0.120930,-0.482263,3.180317,8.355929,7.785276,0.374112,-8.739945,-9.976254,-8.537276,-8.963397,-5.443759,9.083168,7.278260,8.155348,4.000148,1.264925,-8.338388,5.144131,6.602262,7.841406,-8.698489,3.655852,-9.095268,0.717114,-4.876592,-3.009456,0.590627,8.189766,-3.893169,5.206104,8.953968,2.566670,-0.439539,9.733874,2.973980,-2.314425,4.526254,3.895450,5.277989,8.494446,-3.909693,6.666071,0.187564,-6.888898,6.440293,-1.254171,-6.739374,-4.995290,-4.887665,-2.873245,-5.800637,2.889324,6.313627,0.934569,6.337872,-7.302364,-1.112876,9.929509,-9.268399,2.275257,-6.796910,-5.513907,0.900471,1.367766,-4.209059,-4.707954,2.125575,-4.159641,-2.824887,4.313511,-0.614868,7.174084,1.346115,2.791686,-6.004399,3.805688,-6.909797,5.855841,-2.974684,2.637532,4.343571,3.753217,5.035327,9.081653,7.615766,3.815572,-7.755522,6.093856,-7.017991,7.251291,0.355993,1.349657,-9.320375,-3.978887,1.060438,6.818274,7.323518,8.208173,-2.154341,-7.581535,-1.297781,-2.486960,-1.978238,-1.547359,-5.344041,8.745854,4.226867,3.613050,8.524812,-0.738021,9.871712,0.399650,7.971614,7.014198,0.994266,2.400270,0.458947,-7.710772,5.243860,-4.017430,-5.483275,-4.531596,-9.846445,1.996217,7.738203,3.345209,6.791551,9.664378,0.618227,7.281040,-6.388666,-9.916000,-0.852539,9.348319,-1.809305,5.813303,8.014987,-7.233131,3.971653,2.172788,6.096776,9.869138,-3.518934,8.091017,8.413052,-8.168375,-6.020682,2.310975,-7.747791,-4.224312,0.018982,9.293291,7.618084,-2.622805,-9.194431,9.123941,-8.780704,-5.045866,0.054934,5.669181,-8.495005,-4.850673,-4.952446,7.663850,-7.442921,4.840100,6.159670,-9.626076,-5.232670,4.315409,9.006794,7.036207,9.323033,-0.982396,5.352522,2.481601,0.194224,-1.860486,-8.340503,-3.476009,-9.393246,-6.601072,0.352097,-4.208277,7.228651,-5.144545,0.710189,1.997456,2.467201,2.652647,6.951740,0.734050,4.518217,-5.943918,8.089603,-3.789123,1.706172,-4.366862,-3.007375,-9.874657,-4.433201,-0.682977,-6.407501,4.251336,9.797554,2.366040,3.466232,4.925840,-1.344467,-3.039647,9.895212,1.942535,5.191583,4.626880,1.934487,-0.179549,-0.834389,1.315642,-4.137688,-2.971477,9.452303,-6.473263,-4.876785,7.332803,0.032853,5.885028,4.181259,7.735875,-5.091496,-8.161026,2.140367,4.488183,9.741591,-1.589385,2.623381,0.968608,-6.837177,-1.082277,2.300594,-5.938953,7.735091,2.374032,-8.547630,-0.682433,1.160683,-7.160501,5.503976,-8.395872,-3.863352,-9.985762,-5.276283,1.183661,2.138837,2.313215,0.940853,3.192838,8.949131,2.697256,-1.162932,-7.402782,-4.482574,-3.149423,6.746163,-1.153728,2.422190,5.635360,-3.785770,2.034029,-3.642756,2.687781,-2.496247,0.338862,2.841545,8.064020,-2.630597,-2.325830,5.600943,-0.437588,1.588171,-6.344567,7.393927], dtype = "float32")#candidate|2484|(960,)|const|float32
call_2483 = relay.TupleGetItem(func_2351_call(relay.reshape(const_2484.astype('float32'), [960,])), 1)
call_2485 = relay.TupleGetItem(func_2354_call(relay.reshape(const_2484.astype('float32'), [960,])), 1)
output = relay.Tuple([bop_2472,call_2483,const_2484,])
output2 = relay.Tuple([bop_2472,call_2485,const_2484,])
func_2498 = relay.Function([var_2459,var_2460,var_2471,], output)
mod['func_2498'] = func_2498
mod = relay.transform.InferType()(mod)
mutated_mod['func_2498'] = func_2498
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2498_call = mutated_mod.get_global_var('func_2498')
var_2500 = relay.var("var_2500", dtype = "int8", shape = (6, 16, 1))#candidate|2500|(6, 16, 1)|var|int8
var_2501 = relay.var("var_2501", dtype = "int8", shape = (6, 16, 4))#candidate|2501|(6, 16, 4)|var|int8
var_2502 = relay.var("var_2502", dtype = "int8", shape = (6, 16, 4))#candidate|2502|(6, 16, 4)|var|int8
call_2499 = func_2498_call(var_2500,var_2501,var_2502,)
output = call_2499
func_2503 = relay.Function([var_2500,var_2501,var_2502,], output)
mutated_mod['func_2503'] = func_2503
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1178_call = mod.get_global_var('func_1178')
func_1180_call = mutated_mod.get_global_var('func_1180')
call_2505 = func_1178_call()
call_2506 = func_1178_call()
output = call_2505
output2 = call_2506
func_2514 = relay.Function([], output)
mod['func_2514'] = func_2514
mod = relay.transform.InferType()(mod)
output = func_2514()
func_2515 = relay.Function([], output)
mutated_mod['func_2515'] = func_2515
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1674_call = mod.get_global_var('func_1674')
func_1675_call = mutated_mod.get_global_var('func_1675')
call_2722 = relay.TupleGetItem(func_1674_call(), 0)
call_2723 = relay.TupleGetItem(func_1675_call(), 0)
output = call_2722
output2 = call_2723
func_2737 = relay.Function([], output)
mod['func_2737'] = func_2737
mod = relay.transform.InferType()(mod)
output = func_2737()
func_2738 = relay.Function([], output)
mutated_mod['func_2738'] = func_2738
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1859_call = mod.get_global_var('func_1859')
func_1861_call = mutated_mod.get_global_var('func_1861')
call_2766 = relay.TupleGetItem(func_1859_call(), 0)
call_2767 = relay.TupleGetItem(func_1861_call(), 0)
output = relay.Tuple([call_2766,])
output2 = relay.Tuple([call_2767,])
func_2777 = relay.Function([], output)
mod['func_2777'] = func_2777
mod = relay.transform.InferType()(mod)
output = func_2777()
func_2778 = relay.Function([], output)
mutated_mod['func_2778'] = func_2778
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1801_call = mod.get_global_var('func_1801')
func_1803_call = mutated_mod.get_global_var('func_1803')
call_2806 = func_1801_call()
call_2807 = func_1801_call()
uop_2828 = relay.atan(call_2806.astype('float64')) # shape=(14, 1, 10)
uop_2830 = relay.atan(call_2807.astype('float64')) # shape=(14, 1, 10)
func_2777_call = mod.get_global_var('func_2777')
func_2778_call = mutated_mod.get_global_var('func_2778')
call_2843 = relay.TupleGetItem(func_2777_call(), 0)
call_2844 = relay.TupleGetItem(func_2778_call(), 0)
func_607_call = mod.get_global_var('func_607')
func_610_call = mutated_mod.get_global_var('func_610')
const_2851 = relay.const([[-1,-6,5],[-1,2,8],[-1,10,-3],[-1,6,7],[1,-2,7],[10,-2,5],[4,2,3],[1,-7,3],[1,10,-6],[-9,-10,-7],[5,-9,4],[6,-7,3],[10,-6,-8],[-1,-5,-6],[-8,7,6],[-7,1,-9],[7,2,-6],[7,-2,3],[4,-7,-4],[1,10,2],[-9,-8,-6],[-5,2,10],[-2,-4,-10],[2,-10,2],[-4,8,10],[-9,-10,1],[-3,8,4],[5,-4,2],[-5,-7,-5],[-9,-3,-2],[-6,4,-9],[-3,-1,-10],[-8,3,-2],[-8,-9,-2],[-6,-5,7],[-4,10,2],[-2,2,5],[-8,-6,4],[4,-7,-9],[-9,-9,5],[-2,2,4],[-3,-8,-10],[8,-5,-9],[-4,-3,5],[-9,6,-9]], dtype = "int8")#candidate|2851|(45, 3)|const|int8
call_2850 = func_607_call(relay.reshape(const_2851.astype('int8'), [3, 5, 9]))
call_2852 = func_607_call(relay.reshape(const_2851.astype('int8'), [3, 5, 9]))
bop_2859 = relay.divide(call_2850.astype('float64'), call_2843.astype('float64')) # shape=(3, 5, 9)
bop_2862 = relay.divide(call_2852.astype('float64'), call_2844.astype('float64')) # shape=(3, 5, 9)
output = relay.Tuple([uop_2828,const_2851,bop_2859,])
output2 = relay.Tuple([uop_2830,const_2851,bop_2862,])
func_2863 = relay.Function([], output)
mod['func_2863'] = func_2863
mod = relay.transform.InferType()(mod)
mutated_mod['func_2863'] = func_2863
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2863_call = mutated_mod.get_global_var('func_2863')
call_2864 = func_2863_call()
output = call_2864
func_2865 = relay.Function([], output)
mutated_mod['func_2865'] = func_2865
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1940_call = mod.get_global_var('func_1940')
func_1942_call = mutated_mod.get_global_var('func_1942')
call_2902 = relay.TupleGetItem(func_1940_call(), 1)
call_2903 = relay.TupleGetItem(func_1942_call(), 1)
func_2243_call = mod.get_global_var('func_2243')
func_2245_call = mutated_mod.get_global_var('func_2245')
call_2934 = relay.TupleGetItem(func_2243_call(relay.reshape(call_2902.astype('float32'), [48,])), 0)
call_2935 = relay.TupleGetItem(func_2245_call(relay.reshape(call_2902.astype('float32'), [48,])), 0)
func_522_call = mod.get_global_var('func_522')
func_525_call = mutated_mod.get_global_var('func_525')
var_2943 = relay.var("var_2943", dtype = "int8", shape = (900,))#candidate|2943|(900,)|var|int8
call_2942 = relay.TupleGetItem(func_522_call(relay.reshape(var_2943.astype('int8'), [15, 10, 6])), 0)
call_2944 = relay.TupleGetItem(func_525_call(relay.reshape(var_2943.astype('int8'), [15, 10, 6])), 0)
func_847_call = mod.get_global_var('func_847')
func_850_call = mutated_mod.get_global_var('func_850')
const_2951 = relay.const([[9.325609],[-6.862960],[0.025693],[0.307019],[-9.794410],[-2.743453],[2.588886],[1.024601],[6.150873],[-7.196014],[0.879254],[9.677003],[3.882307],[-3.192709],[-4.589843],[7.069187],[-2.095270],[-8.102364],[1.103801],[-9.529371],[2.667531],[-4.494502],[-9.472717],[8.530930],[1.032750],[2.886930],[-9.733327],[8.050535],[6.317712],[6.582494],[-3.365228],[6.422422],[-7.921470],[2.011162],[3.328760],[1.830418],[-9.272847],[-4.136590],[-5.810076],[-8.336898],[3.236338],[-0.481563],[9.737650],[0.835025],[-6.686382],[-0.981494],[-2.448103],[4.438946],[4.813701],[-4.787643],[8.726783],[2.145620],[4.625345],[-1.719446],[7.765319],[-1.836809],[-5.683687],[-7.034219],[-6.026401],[-7.543612],[-0.457256],[-8.864167],[-6.549198],[6.040364],[-4.399820],[-4.106967],[-1.195136],[5.800049],[0.107416],[8.500492],[1.221485],[-1.116959],[-8.262887],[2.716727],[-8.439363],[7.499137],[-7.646680],[7.211731],[-5.677801],[-0.520087],[9.547100],[-0.500377],[-5.346473],[8.718976],[6.790469],[-2.867342],[-3.768923],[-9.052090],[-8.724431],[-2.541552],[8.034083],[1.877149],[5.451979],[-3.453525],[-2.143676],[-1.457327],[0.469967],[0.740996],[-1.742345],[-5.246130],[4.027232],[-0.446027],[4.184237],[-4.737862],[-2.629520],[-2.023984],[6.256954],[2.119494],[5.273111],[-8.287259],[-5.746852],[2.360294],[8.604867],[6.248871],[4.589253],[8.282884],[2.582237],[6.895392],[-3.089813],[-8.476904],[-7.024359],[-1.634621],[-9.817886],[-1.171536],[5.185796],[5.677276],[3.162148],[7.919103],[4.472273],[-6.797251],[-7.801433],[8.962771],[-7.907042],[-3.190198],[5.220701],[1.083285],[-2.143688],[1.305563],[-2.715653],[-1.620581],[-2.577726],[7.398741],[-0.509641],[-0.296015],[-3.423087],[-3.767226],[-7.690174],[-0.077870],[-3.683013],[3.298163],[2.162198],[1.915126],[-4.825036],[-7.666681],[-7.986409],[-4.448934],[5.939682],[-1.953479],[-1.641160],[9.092846],[-7.822371],[-0.074535],[-4.375206],[0.643229],[3.800427],[-7.890198],[6.436314],[-4.280532],[-8.652257],[-6.773165],[4.536161],[4.820623],[5.771904],[-8.629101],[-9.085768],[-9.266329],[-3.652914],[0.084761],[5.040143],[0.876704],[0.477704],[9.630004],[-4.459320],[-2.974707],[-2.313133],[6.128076],[4.236535],[-1.547823],[9.854657],[-6.267969],[8.753976],[-2.898508],[0.889954],[-1.666000],[-3.631995],[-5.958662],[9.170106],[-1.237304],[1.205288],[-1.898169],[-3.667575],[-0.789347],[-8.734593],[-9.756780],[9.923342],[4.021463],[1.117673],[-5.331828],[9.568310],[5.336405],[4.374031],[4.283891],[0.459314],[-4.269700],[-9.950077],[-2.168477],[-5.431301],[-6.200240],[-1.295871],[-8.934375],[2.471049],[-9.759878],[6.868431],[-9.150538],[1.460369],[-4.557665],[0.546128],[0.601887],[-4.318660],[8.968294],[-6.168718],[6.042598],[-1.924844],[7.087119],[-1.712599],[5.612526],[2.633672],[-0.094482],[-2.070006],[7.391991],[-2.784200],[-4.869604],[4.421513],[-6.964331],[8.342538],[-5.243092],[4.427414],[8.346599],[9.305362],[-9.687627],[-2.178109],[9.839043],[9.466317],[3.945190],[-5.923376],[9.922321],[-1.628685],[-0.077473],[6.323851],[4.455379],[7.203794],[-2.718342],[4.729773],[-7.306297],[-3.100349],[-7.872036],[-1.418158],[-8.531460],[1.769452],[-3.131339],[-6.861061],[-7.282148],[6.865821],[-5.461898],[9.874276],[-9.121350],[8.381140],[-0.842928],[-8.871488],[4.095410],[7.661762],[0.437655],[-8.024577],[-1.538462],[8.035518],[7.848302],[-8.072703],[0.592434],[7.629152],[6.124320],[9.176566],[8.154322],[-6.269898],[-2.386350],[-3.010946],[-1.488785],[6.070011],[-5.278741],[3.698376],[-9.203382],[5.863492],[5.991808],[6.171780],[2.113745],[-6.186836],[-1.642175],[-8.012183],[7.551335],[9.543882],[2.266883],[4.523377],[4.309061],[-8.464426],[-7.924032],[-7.459523],[-8.770852],[6.070051],[-9.588913],[-2.165331],[3.198228],[-6.695750],[7.579319],[6.707659],[3.431638],[-6.519344],[-8.268641],[-3.525168],[-6.422525],[8.060568],[4.871949],[2.436809],[5.461806],[7.317153],[-2.155511],[-9.488456],[-8.684086],[2.502854],[5.540423],[-7.220275],[7.652292],[-8.077108],[2.322002],[9.266387],[7.593120],[-5.133672],[1.284562],[-7.144223],[-1.200916],[-7.469081],[-7.079687],[-4.472869],[5.706994],[-6.351576],[-8.047272],[9.987251],[9.760016],[-7.391148],[7.101254],[-1.015914],[-1.970357],[1.535230],[0.156272],[7.220075],[3.596146],[-4.484139],[-9.843785],[-4.774587],[-3.959171],[-5.491747],[-0.833494],[-3.639612],[3.951087],[-9.462773],[-3.855657],[7.648057],[6.040468],[-7.540563],[4.725891],[8.884847],[0.216840],[-1.172236],[-3.216374],[6.170200],[8.455423],[-3.030940],[-0.519293],[9.489314],[6.829668],[-2.968013],[-2.580357],[-9.040089],[-1.120507],[-2.762092],[-0.922698],[-3.192721],[7.205525],[3.873058],[8.994761],[-2.498986],[1.660479],[-8.542273],[9.216946],[4.228818],[2.614854],[7.349377],[-7.170980],[-2.232795],[-0.569884],[-8.647415],[-6.685321],[0.306197],[2.627578],[5.070129],[9.838214],[7.307220],[-4.120087],[-6.073285],[2.879478],[-6.980230],[8.852210],[-7.993588],[-3.767062],[-1.369666],[-7.076882],[9.503858],[3.643268],[-1.562791],[-0.742558],[-6.427485],[-3.812596],[-2.679147],[6.060449],[-6.970156],[-4.510217],[-9.374508],[-2.578940],[6.035105],[9.046847],[-6.682461],[-2.645087],[-2.165854],[-1.423725],[-4.294927],[-4.271597],[-9.102546],[-0.017774],[-3.212077],[-9.760538],[-4.290475],[3.074326],[-2.270034],[-7.166787],[-8.523889],[-0.304585],[5.639148],[4.287025],[-1.333155],[-4.606800],[-5.825752],[4.529631],[6.880136],[5.826600],[-0.314634],[3.650688],[-8.834442],[8.894657],[-5.856587],[4.183866]], dtype = "float64")#candidate|2951|(468, 1)|const|float64
const_2952 = relay.const(-5, dtype = "int64")#candidate|2952|()|const|int64
call_2950 = relay.TupleGetItem(func_847_call(relay.reshape(const_2951.astype('float64'), [13, 4, 9]), relay.reshape(const_2952.astype('int64'), []), ), 0)
call_2953 = relay.TupleGetItem(func_850_call(relay.reshape(const_2951.astype('float64'), [13, 4, 9]), relay.reshape(const_2952.astype('int64'), []), ), 0)
output = relay.Tuple([call_2902,call_2934,call_2942,var_2943,call_2950,const_2951,const_2952,])
output2 = relay.Tuple([call_2903,call_2935,call_2944,var_2943,call_2953,const_2951,const_2952,])
func_2956 = relay.Function([var_2943,], output)
mod['func_2956'] = func_2956
mod = relay.transform.InferType()(mod)
mutated_mod['func_2956'] = func_2956
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2957 = relay.var("var_2957", dtype = "int8", shape = (900,))#candidate|2957|(900,)|var|int8
func_2956_call = mutated_mod.get_global_var('func_2956')
call_2958 = func_2956_call(var_2957)
output = call_2958
func_2959 = relay.Function([var_2957], output)
mutated_mod['func_2959'] = func_2959
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1674_call = mod.get_global_var('func_1674')
func_1675_call = mutated_mod.get_global_var('func_1675')
call_3000 = relay.TupleGetItem(func_1674_call(), 0)
call_3001 = relay.TupleGetItem(func_1675_call(), 0)
func_1984_call = mod.get_global_var('func_1984')
func_1985_call = mutated_mod.get_global_var('func_1985')
call_3012 = relay.TupleGetItem(func_1984_call(), 1)
call_3013 = relay.TupleGetItem(func_1985_call(), 1)
func_522_call = mod.get_global_var('func_522')
func_525_call = mutated_mod.get_global_var('func_525')
var_3026 = relay.var("var_3026", dtype = "int8", shape = (900,))#candidate|3026|(900,)|var|int8
call_3025 = relay.TupleGetItem(func_522_call(relay.reshape(var_3026.astype('int8'), [15, 10, 6])), 0)
call_3027 = relay.TupleGetItem(func_525_call(relay.reshape(var_3026.astype('int8'), [15, 10, 6])), 0)
output = relay.Tuple([call_3000,call_3012,call_3025,var_3026,])
output2 = relay.Tuple([call_3001,call_3013,call_3027,var_3026,])
func_3028 = relay.Function([var_3026,], output)
mod['func_3028'] = func_3028
mod = relay.transform.InferType()(mod)
var_3029 = relay.var("var_3029", dtype = "int8", shape = (900,))#candidate|3029|(900,)|var|int8
output = func_3028(var_3029)
func_3030 = relay.Function([var_3029], output)
mutated_mod['func_3030'] = func_3030
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2145_call = mod.get_global_var('func_2145')
func_2146_call = mutated_mod.get_global_var('func_2146')
call_3034 = relay.TupleGetItem(func_2145_call(), 0)
call_3035 = relay.TupleGetItem(func_2146_call(), 0)
output = call_3034
output2 = call_3035
func_3040 = relay.Function([], output)
mod['func_3040'] = func_3040
mod = relay.transform.InferType()(mod)
mutated_mod['func_3040'] = func_3040
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3040_call = mutated_mod.get_global_var('func_3040')
call_3041 = func_3040_call()
output = call_3041
func_3042 = relay.Function([], output)
mutated_mod['func_3042'] = func_3042
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2777_call = mod.get_global_var('func_2777')
func_2778_call = mutated_mod.get_global_var('func_2778')
call_3046 = relay.TupleGetItem(func_2777_call(), 0)
call_3047 = relay.TupleGetItem(func_2778_call(), 0)
func_1429_call = mod.get_global_var('func_1429')
func_1432_call = mutated_mod.get_global_var('func_1432')
var_3061 = relay.var("var_3061", dtype = "float64", shape = (8, 2))#candidate|3061|(8, 2)|var|float64
call_3060 = relay.TupleGetItem(func_1429_call(relay.reshape(var_3061.astype('float64'), [16,]), relay.reshape(call_3046.astype('int64'), []), ), 1)
call_3062 = relay.TupleGetItem(func_1432_call(relay.reshape(var_3061.astype('float64'), [16,]), relay.reshape(call_3046.astype('int64'), []), ), 1)
bop_3063 = relay.logical_and(call_3046.astype('bool'), call_3060.astype('bool')) # shape=(14, 1, 10)
bop_3066 = relay.logical_and(call_3047.astype('bool'), call_3062.astype('bool')) # shape=(14, 1, 10)
func_2282_call = mod.get_global_var('func_2282')
func_2283_call = mutated_mod.get_global_var('func_2283')
call_3099 = func_2282_call()
call_3100 = func_2282_call()
func_847_call = mod.get_global_var('func_847')
func_850_call = mutated_mod.get_global_var('func_850')
const_3102 = relay.const([0.634891,-6.119726,-3.346515,-8.723105,-8.146012,-1.802923,-8.110660,8.168578,3.154566,-7.622368,-3.619941,-9.636120,7.601404,-9.771762,4.081016,-0.919891,9.854279,4.467328,-2.542451,5.708799,-8.961095,2.805814,1.336899,6.135019,3.691605,-0.528172,-2.023882,3.678965,-5.903103,-0.679864,6.077214,-4.897270,-4.511032,-3.789187,-4.892345,2.071953,-4.210361,3.125708,-2.963336,-8.480157,-5.321151,2.591962,7.399032,-2.736277,-0.632055,6.839239,9.339194,0.010267,-5.831748,7.507630,1.049318,1.319859,0.356283,-3.049150,6.606345,5.142494,1.311853,-2.916476,9.333846,-5.452730,-8.541088,-2.341581,-5.565169,1.798718,6.125548,3.654008,9.916702,-7.068809,7.193255,-8.060878,-2.033029,-4.509904,9.089087,-2.983157,2.609992,-8.897075,0.132839,-9.768166,-9.741386,-5.395799,-3.232322,3.739851,-2.029317,-1.581805,-1.036619,4.389808,0.831497,-5.425580,-1.877292,5.916495,7.126327,8.496964,-7.859793,-5.243346,3.553609,3.875114,-4.701414,-2.275897,-1.650409,-4.593629,7.696799,5.509607,3.148309,1.399735,8.122623,-9.338064,3.878589,0.811628,1.166871,-8.990845,-7.522260,-6.694875,-4.688811,3.205761,2.475331,6.424779,3.698419,8.488654,-9.520854,6.591649,-5.989623,9.699743,3.467438,8.201680,-1.294327,-5.247531,8.329019,-2.032020,9.958096,7.683783,6.895193,8.456585,9.749922,-6.586300,-1.913480,5.753332,0.527899,-3.352808,5.751401,1.268515,2.334478,-4.012340,-3.587805,6.868398,4.064449,-2.066159,8.804632,9.481561,2.216775,5.794628,8.894557,-0.767838,7.730701,-5.637459,-2.125371,-6.679354,0.951610,6.174157,9.300352,9.990639,8.933062,-0.605259,6.540653,8.529224,9.765138,-1.114655,-0.042047,1.669010,8.012265,-1.269295,3.116055,-5.757207,-6.394469,-3.570429,-8.440514,-6.367996,5.789561,-8.642558,-9.804313,6.307668,-1.949563,9.025677,-6.426569,-9.459543,-0.409187,-1.815084,-3.583315,-0.372254,-1.975486,-0.211667,-0.966374,-7.889327,1.663411,-7.461964,-0.113782,7.238975,-6.752429,3.229948,1.160619,-0.300210,8.249349,0.318731,5.068342,-0.118560,-7.730603,-3.243123,1.135574,3.705842,-1.221358,-5.045256,7.513126,0.197394,-4.045832,4.533220,7.728563,0.702030,-8.182432,-4.879514,-9.857698,1.450688,8.540155,6.869789,-1.349407,-5.750260,1.443047,3.874737,-5.683536,-3.976502,-4.328139,6.146267,4.958356,-5.179402,7.884156,-9.482974,7.708915,4.313698,1.974906,0.665767,5.198511,-8.687175,-5.144683,7.423549,1.440849,-3.323429,9.645454,3.366882,-3.861472,-2.143854,-0.780940,-0.121657,-0.287536,-4.767900,-8.594184,1.078858,8.755165,-6.157317,-4.925843,7.834340,3.486871,8.172378,8.933443,-7.388721,-8.602652,1.622532,7.507304,-2.217553,9.122653,3.581822,-8.941894,3.378948,9.138656,9.135940,-4.338698,3.577319,-6.586396,-7.467710,5.025147,-5.792377,-8.104267,-0.126909,1.541364,6.986682,1.116447,-7.554855,-2.738936,-1.394706,-4.260577,6.656821,-5.894057,-0.456610,9.937091,-6.696260,2.335036,-4.615352,-9.908762,7.998466,8.366057,3.452120,-3.172243,-8.423657,7.882242,-4.837934,-8.127975,-4.858261,-3.893060,-4.071958,-4.581797,-3.860797,9.615530,4.827498,1.096634,8.892958,7.287857,5.162552,-5.052024,-2.308204,-4.623267,7.393619,-3.026230,7.836570,2.222560,-8.340958,-5.418902,1.630184,6.028198,-8.274224,-0.794945,6.144336,-4.815200,2.674582,-7.231009,-7.063328,-4.731250,-7.467252,-6.194814,8.785798,9.929383,5.425727,-6.495950,8.450374,0.792807,-8.046525,9.436676,6.748693,-3.617824,-9.376478,1.892298,-6.572384,9.841198,-7.276515,-9.479785,2.582611,-5.060811,-7.336184,2.480390,-3.575949,7.765802,-8.005888,9.038489,-3.052573,-2.976505,-7.670707,5.687310,0.739014,3.442762,-5.782314,3.180958,9.416324,-0.388015,-8.947327,5.455628,-5.657219,1.157214,1.919791,8.394709,1.183285,4.785381,8.762068,-1.478077,7.144819,-3.318819,4.378552,5.080210,8.993441,-4.829538,2.342768,1.605065,-1.571705,9.790191,9.791576,0.160262,-7.766891,-6.830966,-3.643487,9.092015,5.621548,8.267661,2.135560,3.053547,6.494286,2.023783,-0.142764,-1.652809,3.937043,-6.609681,-1.999670,9.821365,-3.857403,-4.254799,-3.126528,-2.630525,-3.429708,2.051237,-8.210012,-2.287036,-4.047472,2.584518,-5.429361,-6.447782,0.011620,-4.589378,-5.778600,-5.101768,-4.148738,5.616436,-8.307560,-7.317210,-9.891985,8.698834,-3.688231,-1.470704,8.470826,7.334965,4.250577,7.857141,1.564823,8.138839,-5.645538,-1.950018,-6.927483,0.733208,-3.950724,2.694525,4.580807,9.583412,7.158104,4.394389,6.006360,-1.368790,-2.126087,6.698686,-0.276897,0.377092,8.970477,5.225681,-8.255135,-2.769472,-5.388910,5.667004,-1.677841,1.202974,-3.817140,-8.475167,-8.320448,-3.091360,9.969027,-1.045999,-3.758351], dtype = "float64")#candidate|3102|(468,)|const|float64
call_3101 = relay.TupleGetItem(func_847_call(relay.reshape(const_3102.astype('float64'), [13, 4, 9]), relay.reshape(call_3046.astype('int64'), []), ), 2)
call_3103 = relay.TupleGetItem(func_850_call(relay.reshape(const_3102.astype('float64'), [13, 4, 9]), relay.reshape(call_3046.astype('int64'), []), ), 2)
func_341_call = mod.get_global_var('func_341')
func_344_call = mutated_mod.get_global_var('func_344')
const_3106 = relay.const([-4,-7,4,9,2,-3,-8,-3,-6,5,-5,-9,4,8,3,-8,-8,3,-8,3,6,-7,9,-9,3,7,9,-2,-1,2,-8,10,-5,7,7,5,4,-8,-4,-9,10,-6,1,3,2,7,-8,-5,2,-8,10,4,7,-8,-10,-7,-3,9,-5,-8,-2,7,2,4,-2,2,-8,-7,-10,-4,-3,9,6,-10,4,7,2,5,6,7,4,1,6,6,4,-6,-3,-3,-5,-9,2,7,10,10,-3,-3,6,8,-3,-10,4,-3,1,5,2,6,-2,10,5,9,4,-5,-5,2,5,4,-6,-6,5,-4,9,-3,-3,4,-2,5,4,-8,-3,6,2,7,7,8,7,10,-2,-7,-7,-2,-6,7,-9,9,-5,7,-5,9,10,-7,-9,-2,-2,-5,-2,8,-6,-7,1,-4,-9,8,-7,-7,4,3,10,4,6,1,-8,7,-5,8,8,-4,7,2,-9,-1,2,-6,-1,4,-10,7,-5,2,7,-6,6,-4,2,-6,-7,-3,3,1,10,3,-2,9,-3,7,-5,-6,5,-3,-10,-7,8,-5,-1,-6,6,4,10,-3,-6,-2,5,9,10,6,-3,-6,-5,3,-1,-1,-10,3,8,-10,8,3,-2,3,6,-3,-4,-9,1,-7,3,-7,2,-1,-10,3,5,-3,-10,-10,-8,7,-1,1,10,-4,7,-6,-3,-7,9,1,8,10,2,6,2,-10,-2,7,-2,-5,-2,7,-7,8,-6,10,3,-4,2,5,-3,-1,7,-7,6,-7,2,-4,8,-6,1,10,8,10,-4,-7,9,4,-5,4,-2,2,3,-6,7,7,8,3,1,-7,8,2,2,-3,6,8,8,-3,-3,-4,-10,8,10,3,5,-6,2,10,1,-8,-1,-6,-6,10,7,2,6,-3,-3,10,6,1,-2,-1,4,-2,8,4,7,5,-9,-1,-9,5,-3,-10,-9,-7,9,5,-9,-8,5,3,7,5,-7,5,3,7,-3,2,-5,-2,-7,8,6,-1,8,-4,-3,3,7,3,-5,5,7,-1,-4,-7,-2,7,10,10,3,3,4,4,-3,1,-9,-8,-4,1,4,1,2,3,-5,10,-8,1,-8,-5,-4,-10,5,-1,9,-8,-9,-8,-6,-3,-5,-8,7,-8,6,7,-2,-7,7,5,-2,-8,2,2,-6,-7,-1,7,-6,-2,-6,4,-5,4,-9,-7,-2,1,-10,1,1,8,-3,-7,-10,1,7,-4,4,-4,7,-3,-8,-2,-7,-8,-1,10,1,-4,6,7,-1,-8,10,-10,-5,7,-7,-6,2,-5,-10,10,2,-4,-9,2,3,7,-3,-10,9,-4,6,5,3,4,6,-5,-6,-7,-10,-5,10,-6,-6,-1,-6,5,6,2,1,1,8,6,-4,8,-3,-9,-2,5,-3,-7,3,1,-2,-7,8,10,3,-9,8,-3,10,-1], dtype = "int8")#candidate|3106|(546,)|const|int8
call_3105 = relay.TupleGetItem(func_341_call(relay.reshape(const_3106.astype('int8'), [7, 13, 6])), 0)
call_3107 = relay.TupleGetItem(func_344_call(relay.reshape(const_3106.astype('int8'), [7, 13, 6])), 0)
func_759_call = mod.get_global_var('func_759')
func_761_call = mutated_mod.get_global_var('func_761')
const_3112 = relay.const([9,-3,1,8,10,3,-2,-10,-8,-3,2,9,-10,9,-6,-5,2,-5,-9,4,-1,-3,-6,7,-9,-4,8,-10,8,6,-10,10,10,7,-10,-9,8,4,-8,-1,3,9,9,-10,9,-2,8,2,-9,5,10,10,9,-3,9,5,-9,5,-4,-4,2,1,-10,-6,-2,8,-9,9,6,-7,5,-7,8,2,-7,-4,-4,9,-10,3,-7,5,3,4,-5,4,-4,-6,-3,4,-7,-8,-5,-5,1,-10,-10,4,6,-3], dtype = "uint32")#candidate|3112|(100,)|const|uint32
call_3111 = relay.TupleGetItem(func_759_call(relay.reshape(const_3112.astype('uint32'), [5, 4, 5])), 0)
call_3113 = relay.TupleGetItem(func_761_call(relay.reshape(const_3112.astype('uint32'), [5, 4, 5])), 0)
output = relay.Tuple([var_3061,bop_3063,call_3099,call_3101,const_3102,call_3105,const_3106,call_3111,const_3112,])
output2 = relay.Tuple([var_3061,bop_3066,call_3100,call_3103,const_3102,call_3107,const_3106,call_3113,const_3112,])
func_3123 = relay.Function([var_3061,], output)
mod['func_3123'] = func_3123
mod = relay.transform.InferType()(mod)
var_3124 = relay.var("var_3124", dtype = "float64", shape = (8, 2))#candidate|3124|(8, 2)|var|float64
output = func_3123(var_3124)
func_3125 = relay.Function([var_3124], output)
mutated_mod['func_3125'] = func_3125
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3164 = relay.var("var_3164", dtype = "float32", shape = (7, 1, 16))#candidate|3164|(7, 1, 16)|var|float32
uop_3165 = relay.atanh(var_3164.astype('float32')) # shape=(7, 1, 16)
uop_3169 = relay.exp(uop_3165.astype('float64')) # shape=(7, 1, 16)
func_3123_call = mod.get_global_var('func_3123')
func_3125_call = mutated_mod.get_global_var('func_3125')
const_3179 = relay.const([-3.966918,-8.660367,-1.834727,1.443923,-6.158758,9.216172,-2.573583,-0.323548,3.190016,0.583064,-5.263943,-6.847375,0.438701,-7.442939,-8.953250,0.610394], dtype = "float64")#candidate|3179|(16,)|const|float64
call_3178 = relay.TupleGetItem(func_3123_call(relay.reshape(const_3179.astype('float64'), [8, 2])), 8)
call_3180 = relay.TupleGetItem(func_3125_call(relay.reshape(const_3179.astype('float64'), [8, 2])), 8)
var_3185 = relay.var("var_3185", dtype = "float64", shape = (7, 1, 16))#candidate|3185|(7, 1, 16)|var|float64
bop_3186 = relay.left_shift(uop_3169.astype('int64'), relay.reshape(var_3185.astype('int64'), relay.shape_of(uop_3169))) # shape=(7, 1, 16)
output = relay.Tuple([call_3178,const_3179,bop_3186,])
output2 = relay.Tuple([call_3180,const_3179,bop_3186,])
func_3196 = relay.Function([var_3164,var_3185,], output)
mod['func_3196'] = func_3196
mod = relay.transform.InferType()(mod)
mutated_mod['func_3196'] = func_3196
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3196_call = mutated_mod.get_global_var('func_3196')
var_3198 = relay.var("var_3198", dtype = "float32", shape = (7, 1, 16))#candidate|3198|(7, 1, 16)|var|float32
var_3199 = relay.var("var_3199", dtype = "float64", shape = (7, 1, 16))#candidate|3199|(7, 1, 16)|var|float64
call_3197 = func_3196_call(var_3198,var_3199,)
output = call_3197
func_3200 = relay.Function([var_3198,var_3199,], output)
mutated_mod['func_3200'] = func_3200
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1187_call = mod.get_global_var('func_1187')
func_1188_call = mutated_mod.get_global_var('func_1188')
call_3215 = relay.TupleGetItem(func_1187_call(), 0)
call_3216 = relay.TupleGetItem(func_1188_call(), 0)
func_2351_call = mod.get_global_var('func_2351')
func_2354_call = mutated_mod.get_global_var('func_2354')
const_3224 = relay.const([[6.385603,-6.092696,-8.523285,2.656173,-0.214357,2.183021,0.280370,-6.931020,8.047956,6.126879,0.915877,-5.188823,2.099127,-1.909999,0.370247,6.231566,0.327237,9.743782,-7.686757,-5.764593,-4.946145,5.163953,-3.416028,-0.836493,2.009255,2.597217,-9.381543,8.101061,1.148095,0.277639,-5.554886,0.945635,-6.649558,0.831609,-6.454020,5.744232,1.192597,-9.901933,-9.732355,8.864481,-9.639337,9.886188,9.985009,-8.371114,-1.361907,7.034867,1.922678,-6.518165,1.060958,-0.634671,2.116848,0.919921,9.449912,-0.669442,-9.869190,5.531917,0.027399,0.291018,1.796103,5.650052,8.503797,-7.903545,-5.959616,3.701196,-7.091961,8.621210,4.877250,-0.118552,-8.764661,5.990553,-6.229108,0.900869,1.749664,-1.612919,3.698214,-2.096731,3.896205,4.756136,2.629624,6.434333,-2.154040,2.768856,8.811186,-3.180816,7.178400,-4.023091,-6.569193,3.987723,-6.744157,-5.670782,5.046570,2.795668,3.058975,-7.712517,6.627741,-1.893508],[-7.418564,9.418814,1.437213,3.902149,1.455529,4.051772,-9.372939,9.728679,-3.768546,-1.347822,-6.997596,-3.693773,-1.133371,-4.094925,7.394124,7.487203,8.203069,9.890598,1.980040,0.742370,5.175441,-4.422460,9.131914,-0.098593,-7.218525,9.194832,-1.467080,-9.463724,3.573260,-0.405785,-6.906820,-4.978433,9.247741,-5.645253,1.625726,4.614888,-6.470452,-8.706022,-1.380931,-6.595434,0.684169,0.553558,0.396967,-0.812717,8.962767,5.273528,-2.331721,8.714850,-7.152891,-0.524324,8.539006,-2.221375,-4.740520,0.997645,7.621106,5.626834,2.317738,8.551104,-1.192427,3.177283,-7.125691,2.797674,4.040890,-3.505019,9.004845,9.606481,3.545095,-9.855775,-7.747174,-0.183331,5.427550,-0.354264,-0.642130,-5.623504,3.966324,-3.001228,-1.499203,-7.830268,-5.626288,9.596872,-2.780235,-7.744148,-6.298865,8.993748,-5.798539,9.966341,2.782244,7.804805,1.505099,-7.363031,1.048198,-2.753701,2.373163,4.180243,-3.840240,8.410050],[5.352839,-0.169181,-3.822292,-2.041766,3.220105,4.569694,4.882400,-4.251106,-5.484103,0.171225,-5.801677,3.957356,2.646039,4.824679,-2.895861,-4.310216,2.087117,3.132322,-6.759078,-0.895784,2.566038,-0.696784,-1.774492,4.538318,6.583387,4.499642,8.635422,5.920009,7.115347,-0.522397,4.037550,-3.675325,9.454465,8.417250,0.032378,3.203806,6.846683,-0.202740,-4.199673,-6.175612,-8.170786,4.266946,-8.740502,-2.166060,-0.340750,2.118465,8.871678,-4.285881,-3.149548,-7.224144,3.698142,-9.868550,6.694180,1.660255,5.475779,-7.980159,3.531435,0.609852,-8.596069,9.806635,-8.232479,2.594236,-9.566552,-5.176246,9.553366,0.325170,-0.169015,4.593531,-1.345169,7.498197,-7.558818,2.642602,-0.572784,0.978513,8.899517,9.995762,-0.507109,0.468867,-0.445120,3.722585,3.287957,-6.366136,-7.148143,3.870552,-6.395547,-5.942340,-8.909833,-1.477924,-2.396458,-2.963648,1.205121,7.473266,-8.026854,-3.188731,-1.356721,-4.371162],[-7.285092,7.059400,-9.729877,8.291719,-9.472222,7.539551,-0.597909,3.291441,6.472907,-7.602850,3.553019,-0.067411,-5.575690,-4.695224,-4.724675,-1.479381,0.962007,-3.323926,7.734530,9.026240,4.929216,-5.575304,-6.922429,7.544325,4.588187,-5.521053,1.825869,-5.272488,-7.047496,3.304457,5.323075,3.792306,3.686091,-5.385570,-1.398924,-9.966948,-5.895625,3.632196,-3.101409,5.188922,-2.308391,-2.982405,-6.513543,5.253092,2.590641,-8.931372,5.780803,-5.819332,5.234425,0.662046,-7.495960,7.499880,-5.358183,0.888623,6.883340,0.046945,0.794670,-6.878871,-9.025644,-6.327337,-1.371918,0.502197,-6.023725,-7.925145,-2.159118,1.548207,-9.318834,-1.313066,7.617942,5.214460,-4.136295,-8.343522,6.853500,9.500377,3.170365,5.874802,-2.532798,5.958955,-1.059849,-5.278652,5.193550,1.234706,0.446233,-8.038166,-4.581278,2.999395,-0.236143,-5.386728,-4.168114,-9.768333,0.741033,1.307578,-0.089304,-4.370563,3.924766,0.934398],[8.425692,-8.814796,-3.368684,3.856812,-6.245690,4.615847,9.884215,-5.063273,-5.037180,7.065285,9.336741,0.357339,5.653615,-5.898086,2.329042,4.503388,1.282056,4.132707,-4.954298,-1.593048,4.936673,-7.231127,8.451820,1.818648,0.709843,1.269018,2.373624,-7.561735,-0.130582,6.846831,-0.957472,-7.636369,-2.609449,-7.751818,9.598349,-0.290401,-0.748857,8.920441,9.819596,1.608790,3.605486,7.697162,-8.704162,1.271294,5.108346,-1.381523,5.932375,4.666368,-5.223286,-9.028206,-3.713555,-1.042199,6.191921,-3.195684,-9.681851,1.202344,-9.042104,2.732743,-7.226084,8.751439,5.908759,-1.499049,4.871532,2.168574,0.096681,3.810120,-3.159673,-3.379638,3.891456,-8.265053,6.548461,3.991233,1.576613,-4.703587,0.072065,8.381582,5.965180,9.668786,7.978218,-8.103719,-4.285594,-9.458884,3.559443,6.164390,8.127799,7.882615,1.546368,-6.837226,3.205950,7.122934,-3.722656,3.747154,-9.691658,-2.391169,0.811378,-6.261156],[-6.577915,-3.800592,8.434470,-9.474211,-4.215066,2.571139,-6.696840,-5.705600,-9.470892,-3.837148,-7.275735,-1.481938,-4.849099,-5.068354,9.067621,-5.703798,9.953165,-6.020273,-7.568369,6.039609,-5.170208,-6.869274,-9.592993,-8.818616,-6.942841,5.236746,-2.140198,0.727902,9.958475,9.474852,-5.702870,-8.953502,-1.624602,9.702032,-9.683541,8.340060,4.928924,9.688328,-4.872987,8.512492,9.857654,8.655255,-1.055854,-7.337701,-5.537341,4.871378,0.603611,-7.940085,-5.092010,-4.766191,-3.486455,8.239176,-1.091933,6.211888,-6.214335,2.452921,-5.080019,6.713200,-5.614775,-5.945523,1.500048,1.943448,4.930820,7.158022,9.816351,-3.693589,4.695249,-0.702096,0.783505,6.627856,-3.495087,7.723037,9.349226,1.216927,-8.416351,1.801782,2.202281,9.915124,-5.398083,-9.617065,-5.096963,-7.319025,-9.989456,7.409677,-2.977110,6.031523,-8.754152,6.879985,-4.881399,1.641683,-3.683939,-7.672002,5.086891,1.030403,-2.770109,-5.963938],[-2.335425,6.438505,7.892086,-1.914496,8.312436,-9.395217,-7.189667,0.150217,-9.764124,-1.895700,4.053750,7.833075,-1.661172,3.418402,-0.389402,6.208355,-1.443432,-5.994359,-7.084463,4.242806,-7.380222,5.521753,-1.331858,4.648798,6.512530,1.386921,4.402862,0.594502,0.061057,-5.180602,-9.839309,8.862833,-6.141600,-8.942004,-4.417769,-1.325957,0.307952,-6.898964,0.192884,2.946650,7.989072,3.899150,6.599409,-5.932149,4.409398,-1.585759,-1.036603,-3.937355,0.453640,6.457047,9.386785,5.591717,6.713574,-7.076421,6.929444,1.819753,-1.220875,6.599614,-1.626402,5.739900,9.822296,5.390673,1.368042,-1.665530,2.829765,-7.861929,-2.439544,9.445557,3.643421,-8.037933,7.835666,7.603826,-6.136788,3.785770,-5.938196,2.331419,1.283677,-1.843883,-1.610660,6.928985,-0.608824,-5.706405,8.958004,2.312453,6.012376,-2.552137,2.720492,7.742362,-4.823020,-1.270733,6.725657,-1.859188,2.153925,2.222437,-0.591248,6.013378],[-7.447005,5.458749,7.827839,3.418944,-0.672313,-5.910027,4.241781,4.371789,-6.536244,8.415959,4.740053,-7.707795,-9.284664,0.336705,9.557442,8.445356,-2.538947,6.628150,8.474128,4.732643,-0.001373,-0.851179,6.774222,-2.206360,3.325244,4.289163,8.693686,1.958530,8.893782,-2.338555,8.555801,-6.339420,-1.770003,-7.725780,-3.961415,1.501665,3.853909,4.276613,-2.488997,-1.685629,5.121179,-6.918668,-2.380734,-6.266070,-3.434665,-5.800669,-7.481175,-4.017973,-2.581128,7.645474,-4.914858,-2.713478,-7.969295,-8.641220,8.032955,-5.473286,-6.309037,3.983122,0.193689,-7.320314,7.821053,3.511764,2.378296,-1.184810,-2.151571,1.852106,4.598197,-4.896085,7.943243,-8.106147,-4.559381,1.888740,0.019968,9.639641,-0.136897,6.160977,-0.852760,0.720279,-0.540332,0.145210,2.243538,0.056249,-4.784764,-3.090785,-5.280122,-9.676938,-0.365002,7.528513,2.532659,-2.402745,-7.502500,8.236933,-0.312061,-6.839300,-6.996273,-5.861585],[-1.924535,-3.176076,1.633374,-1.836389,3.850735,-2.419796,-3.584420,-5.631997,-6.552645,2.109252,-9.760672,2.602066,-0.304195,9.715412,-4.086125,-0.161054,5.665115,1.470841,-4.068305,-8.109966,4.027365,6.944433,-9.078677,8.828199,-7.930656,1.510416,1.047533,5.851388,-6.849370,-8.061402,-5.082031,-8.294105,-5.891971,2.119525,4.719912,-8.551451,-1.744599,5.186520,4.563082,-2.336237,8.628553,-0.987708,-6.373022,-0.606362,-3.575462,8.872757,-4.285634,-6.149755,-9.102525,8.417528,3.322101,-1.941931,9.210714,-7.327414,-8.246823,-0.742247,-7.894593,-2.925892,-6.535387,-3.280299,9.701940,-7.846078,0.377718,-2.847758,-8.765965,7.908835,-0.109386,4.427856,4.930092,-0.713593,-4.724088,-0.767529,-0.332248,-9.888057,0.459406,7.714735,-0.587785,-8.714428,9.828413,6.021185,-7.656575,0.374748,-5.967900,-5.976598,9.425137,5.797013,7.268552,-0.404199,-0.221752,1.317344,2.691027,9.777254,-8.210590,8.298814,-4.063007,5.583752],[-5.513010,1.490242,2.634708,-2.860270,3.822715,9.283834,4.357626,-9.292278,-0.375428,-7.059516,-4.426850,2.346610,5.009394,-6.317794,-1.991100,8.904368,6.808977,6.530229,-4.183874,4.080784,-9.284768,4.627376,-9.368045,0.145608,2.896536,0.839079,5.456041,-3.004525,0.196373,7.952906,-1.411924,-9.385496,4.334485,-2.312925,-2.270914,2.388474,-1.380533,-9.893073,-0.228766,6.905601,2.317757,-4.506180,-9.043394,-3.847328,3.266783,3.384783,-7.166770,2.140872,8.481274,9.406996,5.797687,-7.380969,4.307637,5.024440,3.195989,9.769704,0.208535,0.949317,-3.548745,8.137792,3.956717,8.224139,0.963834,-5.896242,7.014726,-5.896101,-3.595768,-6.932319,6.494115,-1.367222,2.257282,-6.364702,2.498052,-2.922694,8.955759,6.791911,-4.234458,-3.673659,-5.732604,-4.673947,-2.272242,-5.351618,-3.442327,4.033854,-3.357670,-2.557869,3.161599,-6.324266,-3.791605,3.607552,4.858558,7.971406,7.659342,8.454715,-7.517569,0.175270]], dtype = "float32")#candidate|3224|(10, 96)|const|float32
call_3223 = relay.TupleGetItem(func_2351_call(relay.reshape(const_3224.astype('float32'), [960,])), 3)
call_3225 = relay.TupleGetItem(func_2354_call(relay.reshape(const_3224.astype('float32'), [960,])), 3)
const_3295 = relay.const([[[-8,9,5,-3,8,-7,10,3,-5],[-2,9,-2,9,-2,10,4,-8,-9],[9,-1,5,-7,-2,-5,-9,1,-2],[7,-7,-6,-4,6,-3,4,6,6],[3,-4,-4,-1,5,3,5,9,-8]],[[10,7,-3,-8,2,-4,5,2,2],[8,2,-3,3,6,1,-8,5,4],[6,5,-8,-6,6,-2,-5,10,-6],[-4,-3,10,2,5,-5,-5,3,-9],[-1,-5,3,5,-8,7,8,-4,10]],[[4,-3,-1,-10,-1,10,-5,5,8],[-7,-7,-8,2,6,8,9,-9,-3],[-3,9,-7,2,-8,3,-6,-10,9],[9,-5,-5,-10,9,7,10,-6,-1],[-5,-4,-3,-2,-9,-4,-2,8,-8]]], dtype = "int8")#candidate|3295|(3, 5, 9)|const|int8
bop_3296 = relay.multiply(call_3223.astype('int32'), relay.reshape(const_3295.astype('int32'), relay.shape_of(call_3223))) # shape=(3, 5, 9)
bop_3299 = relay.multiply(call_3225.astype('int32'), relay.reshape(const_3295.astype('int32'), relay.shape_of(call_3225))) # shape=(3, 5, 9)
func_994_call = mod.get_global_var('func_994')
func_997_call = mutated_mod.get_global_var('func_997')
var_3322 = relay.var("var_3322", dtype = "float32", shape = (48,))#candidate|3322|(48,)|var|float32
call_3321 = relay.TupleGetItem(func_994_call(relay.reshape(var_3322.astype('float32'), [6, 1, 8])), 2)
call_3323 = relay.TupleGetItem(func_997_call(relay.reshape(var_3322.astype('float32'), [6, 1, 8])), 2)
func_1580_call = mod.get_global_var('func_1580')
func_1582_call = mutated_mod.get_global_var('func_1582')
call_3325 = relay.TupleGetItem(func_1580_call(), 1)
call_3326 = relay.TupleGetItem(func_1582_call(), 1)
output = relay.Tuple([call_3215,const_3224,bop_3296,call_3321,var_3322,call_3325,])
output2 = relay.Tuple([call_3216,const_3224,bop_3299,call_3323,var_3322,call_3326,])
func_3345 = relay.Function([var_3322,], output)
mod['func_3345'] = func_3345
mod = relay.transform.InferType()(mod)
var_3346 = relay.var("var_3346", dtype = "float32", shape = (48,))#candidate|3346|(48,)|var|float32
output = func_3345(var_3346)
func_3347 = relay.Function([var_3346], output)
mutated_mod['func_3347'] = func_3347
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3387 = relay.var("var_3387", dtype = "float32", shape = (6, 7, 10))#candidate|3387|(6, 7, 10)|var|float32
var_3388 = relay.var("var_3388", dtype = "float32", shape = (6, 7, 10))#candidate|3388|(6, 7, 10)|var|float32
bop_3389 = relay.power(var_3387.astype('float32'), relay.reshape(var_3388.astype('float32'), relay.shape_of(var_3387))) # shape=(6, 7, 10)
func_1940_call = mod.get_global_var('func_1940')
func_1942_call = mutated_mod.get_global_var('func_1942')
call_3396 = relay.TupleGetItem(func_1940_call(), 1)
call_3397 = relay.TupleGetItem(func_1942_call(), 1)
output = relay.Tuple([bop_3389,call_3396,])
output2 = relay.Tuple([bop_3389,call_3397,])
func_3402 = relay.Function([var_3387,var_3388,], output)
mod['func_3402'] = func_3402
mod = relay.transform.InferType()(mod)
var_3403 = relay.var("var_3403", dtype = "float32", shape = (6, 7, 10))#candidate|3403|(6, 7, 10)|var|float32
var_3404 = relay.var("var_3404", dtype = "float32", shape = (6, 7, 10))#candidate|3404|(6, 7, 10)|var|float32
output = func_3402(var_3403,var_3404,)
func_3405 = relay.Function([var_3403,var_3404,], output)
mutated_mod['func_3405'] = func_3405
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3423 = relay.const([[[-7,6,-9,-1,4,-10,-2,-8,-9,-3],[7,4,-5,-6,2,-6,6,-10,4,-5],[-5,-7,-6,-4,-10,-9,3,4,-4,7],[-4,-4,-7,-5,-6,-9,-7,-9,-1,-8],[-8,-8,8,8,-2,-7,10,-7,8,9],[-4,6,-5,4,8,7,-7,-8,4,-9],[3,-5,9,-1,3,10,10,-1,-3,-1]],[[7,6,2,10,-9,4,-5,6,-10,9],[-9,-3,9,4,-8,-10,4,8,-1,1],[9,4,4,-8,-7,8,-7,4,2,7],[-4,5,-4,-3,-3,-7,-2,6,10,-8],[10,2,-4,5,-4,-6,-9,8,3,-10],[-8,1,-7,3,1,-4,-7,2,1,-9],[-10,-5,5,-4,-5,-9,5,-10,-6,-10]]], dtype = "uint32")#candidate|3423|(2, 7, 10)|const|uint32
var_3424 = relay.var("var_3424", dtype = "uint32", shape = (2, 7, 10))#candidate|3424|(2, 7, 10)|var|uint32
bop_3425 = relay.bitwise_xor(const_3423.astype('uint32'), relay.reshape(var_3424.astype('uint32'), relay.shape_of(const_3423))) # shape=(2, 7, 10)
func_2196_call = mod.get_global_var('func_2196')
func_2198_call = mutated_mod.get_global_var('func_2198')
const_3429 = relay.const([-6.186853,1.436147,9.953451,-9.773287,-0.267867,2.278009,-2.073415,-0.204169,2.094786,-1.773580,4.535538,-8.538006,-0.217957,-0.823969,-2.956016,0.022939,2.624750,-8.412059,-5.081662,-6.270142,-8.984548,-8.594098,1.596525,6.406491,8.188298,8.528781,-5.863858,4.795326,3.042122,9.829416,0.472977,-0.531099,3.828975,-1.846090,6.398489,2.898235,-4.675884,7.744573,-8.121392,-1.755439,-8.187051,-3.261902,-1.596685,-6.643510,-0.120941,7.124274,-9.682410,-0.711816], dtype = "float32")#candidate|3429|(48,)|const|float32
call_3428 = relay.TupleGetItem(func_2196_call(relay.reshape(const_3429.astype('float32'), [48,])), 1)
call_3430 = relay.TupleGetItem(func_2198_call(relay.reshape(const_3429.astype('float32'), [48,])), 1)
func_1178_call = mod.get_global_var('func_1178')
func_1180_call = mutated_mod.get_global_var('func_1180')
call_3435 = func_1178_call()
call_3436 = func_1178_call()
func_1449_call = mod.get_global_var('func_1449')
func_1453_call = mutated_mod.get_global_var('func_1453')
var_3438 = relay.var("var_3438", dtype = "float64", shape = (1200,))#candidate|3438|(1200,)|var|float64
call_3437 = func_1449_call(relay.reshape(var_3438.astype('float64'), [5, 15, 16]), relay.reshape(var_3438.astype('float64'), [5, 15, 16]), )
call_3439 = func_1449_call(relay.reshape(var_3438.astype('float64'), [5, 15, 16]), relay.reshape(var_3438.astype('float64'), [5, 15, 16]), )
output = relay.Tuple([bop_3425,call_3428,const_3429,call_3435,call_3437,var_3438,])
output2 = relay.Tuple([bop_3425,call_3430,const_3429,call_3436,call_3439,var_3438,])
func_3444 = relay.Function([var_3424,var_3438,], output)
mod['func_3444'] = func_3444
mod = relay.transform.InferType()(mod)
mutated_mod['func_3444'] = func_3444
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3444_call = mutated_mod.get_global_var('func_3444')
var_3446 = relay.var("var_3446", dtype = "uint32", shape = (2, 7, 10))#candidate|3446|(2, 7, 10)|var|uint32
var_3447 = relay.var("var_3447", dtype = "float64", shape = (1200,))#candidate|3447|(1200,)|var|float64
call_3445 = func_3444_call(var_3446,var_3447,)
output = call_3445
func_3448 = relay.Function([var_3446,var_3447,], output)
mutated_mod['func_3448'] = func_3448
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1187_call = mod.get_global_var('func_1187')
func_1188_call = mutated_mod.get_global_var('func_1188')
call_3454 = relay.TupleGetItem(func_1187_call(), 0)
call_3455 = relay.TupleGetItem(func_1188_call(), 0)
output = call_3454
output2 = call_3455
func_3508 = relay.Function([], output)
mod['func_3508'] = func_3508
mod = relay.transform.InferType()(mod)
mutated_mod['func_3508'] = func_3508
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3508_call = mutated_mod.get_global_var('func_3508')
call_3509 = func_3508_call()
output = call_3509
func_3510 = relay.Function([], output)
mutated_mod['func_3510'] = func_3510
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1187_call = mod.get_global_var('func_1187')
func_1188_call = mutated_mod.get_global_var('func_1188')
call_3523 = relay.TupleGetItem(func_1187_call(), 0)
call_3524 = relay.TupleGetItem(func_1188_call(), 0)
output = relay.Tuple([call_3523,])
output2 = relay.Tuple([call_3524,])
func_3533 = relay.Function([], output)
mod['func_3533'] = func_3533
mod = relay.transform.InferType()(mod)
output = func_3533()
func_3534 = relay.Function([], output)
mutated_mod['func_3534'] = func_3534
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1178_call = mod.get_global_var('func_1178')
func_1180_call = mutated_mod.get_global_var('func_1180')
call_3551 = func_1178_call()
call_3552 = func_1178_call()
func_607_call = mod.get_global_var('func_607')
func_610_call = mutated_mod.get_global_var('func_610')
var_3593 = relay.var("var_3593", dtype = "int8", shape = (135,))#candidate|3593|(135,)|var|int8
call_3592 = func_607_call(relay.reshape(var_3593.astype('int8'), [3, 5, 9]))
call_3594 = func_607_call(relay.reshape(var_3593.astype('int8'), [3, 5, 9]))
func_24_call = mod.get_global_var('func_24')
func_27_call = mutated_mod.get_global_var('func_27')
var_3606 = relay.var("var_3606", dtype = "int64", shape = ())#candidate|3606|()|var|int64
call_3605 = relay.TupleGetItem(func_24_call(relay.reshape(var_3606.astype('int64'), [])), 0)
call_3607 = relay.TupleGetItem(func_27_call(relay.reshape(var_3606.astype('int64'), [])), 0)
output = relay.Tuple([call_3551,call_3592,var_3593,call_3605,var_3606,])
output2 = relay.Tuple([call_3552,call_3594,var_3593,call_3607,var_3606,])
func_3610 = relay.Function([var_3593,var_3606,], output)
mod['func_3610'] = func_3610
mod = relay.transform.InferType()(mod)
var_3611 = relay.var("var_3611", dtype = "int8", shape = (135,))#candidate|3611|(135,)|var|int8
var_3612 = relay.var("var_3612", dtype = "int64", shape = ())#candidate|3612|()|var|int64
output = func_3610(var_3611,var_3612,)
func_3613 = relay.Function([var_3611,var_3612,], output)
mutated_mod['func_3613'] = func_3613
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1140_call = mod.get_global_var('func_1140')
func_1141_call = mutated_mod.get_global_var('func_1141')
call_3628 = relay.TupleGetItem(func_1140_call(), 0)
call_3629 = relay.TupleGetItem(func_1141_call(), 0)
uop_3636 = relay.cosh(call_3628.astype('float64')) # shape=(14, 1, 10)
uop_3638 = relay.cosh(call_3629.astype('float64')) # shape=(14, 1, 10)
output = relay.Tuple([uop_3636,])
output2 = relay.Tuple([uop_3638,])
func_3650 = relay.Function([], output)
mod['func_3650'] = func_3650
mod = relay.transform.InferType()(mod)
output = func_3650()
func_3651 = relay.Function([], output)
mutated_mod['func_3651'] = func_3651
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1920_call = mod.get_global_var('func_1920')
func_1922_call = mutated_mod.get_global_var('func_1922')
call_3668 = relay.TupleGetItem(func_1920_call(), 4)
call_3669 = relay.TupleGetItem(func_1922_call(), 4)
output = relay.Tuple([call_3668,])
output2 = relay.Tuple([call_3669,])
func_3670 = relay.Function([], output)
mod['func_3670'] = func_3670
mod = relay.transform.InferType()(mod)
mutated_mod['func_3670'] = func_3670
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3670_call = mutated_mod.get_global_var('func_3670')
call_3671 = func_3670_call()
output = call_3671
func_3672 = relay.Function([], output)
mutated_mod['func_3672'] = func_3672
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3714 = relay.var("var_3714", dtype = "float64", shape = ())#candidate|3714|()|var|float64
var_3715 = relay.var("var_3715", dtype = "float64", shape = (2, 10, 14))#candidate|3715|(2, 10, 14)|var|float64
bop_3716 = relay.divide(var_3714.astype('float64'), var_3715.astype('float64')) # shape=(2, 10, 14)
output = relay.Tuple([bop_3716,])
output2 = relay.Tuple([bop_3716,])
func_3721 = relay.Function([var_3714,var_3715,], output)
mod['func_3721'] = func_3721
mod = relay.transform.InferType()(mod)
mutated_mod['func_3721'] = func_3721
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3721_call = mutated_mod.get_global_var('func_3721')
var_3723 = relay.var("var_3723", dtype = "float64", shape = ())#candidate|3723|()|var|float64
var_3724 = relay.var("var_3724", dtype = "float64", shape = (2, 10, 14))#candidate|3724|(2, 10, 14)|var|float64
call_3722 = func_3721_call(var_3723,var_3724,)
output = call_3722
func_3725 = relay.Function([var_3723,var_3724,], output)
mutated_mod['func_3725'] = func_3725
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3670_call = mod.get_global_var('func_3670')
func_3672_call = mutated_mod.get_global_var('func_3672')
call_3791 = relay.TupleGetItem(func_3670_call(), 0)
call_3792 = relay.TupleGetItem(func_3672_call(), 0)
output = relay.Tuple([call_3791,])
output2 = relay.Tuple([call_3792,])
func_3793 = relay.Function([], output)
mod['func_3793'] = func_3793
mod = relay.transform.InferType()(mod)
output = func_3793()
func_3794 = relay.Function([], output)
mutated_mod['func_3794'] = func_3794
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3859 = relay.var("var_3859", dtype = "int16", shape = (15, 7, 8))#candidate|3859|(15, 7, 8)|var|int16
var_3860 = relay.var("var_3860", dtype = "int16", shape = (15, 7, 8))#candidate|3860|(15, 7, 8)|var|int16
bop_3861 = relay.less_equal(var_3859.astype('bool'), relay.reshape(var_3860.astype('bool'), relay.shape_of(var_3859))) # shape=(15, 7, 8)
func_3610_call = mod.get_global_var('func_3610')
func_3613_call = mutated_mod.get_global_var('func_3613')
const_3890 = relay.const([5,-10,9,3,5,-4,-5,-1,-2,1,1,8,6,8,-2,-8,7,9,3,5,-5,2,-4,6,7,10,1,-4,9,-3,-10,-9,8,-2,1,3,-4,8,10,-6,3,5,-1,-3,2,5,-8,9,-2,8,-6,-1,-8,8,3,2,-9,-2,-9,-3,10,3,10,-3,-10,-6,-4,7,-6,-7,-1,6,10,-8,-2,10,-1,-9,4,3,-3,-10,-6,8,-4,-2,3,-2,-6,10,5,2,-2,5,3,9,9,-4,8,10,4,-6,-9,-10,3,7,-9,-2,-7,6,-6,-7,-6,-3,-2,8,-2,3,-7,10,-2,-7,-5,-3,-7,4,5,10,4,-8,4,-2,-2,-2,9], dtype = "int8")#candidate|3890|(135,)|const|int8
var_3891 = relay.var("var_3891", dtype = "int64", shape = ())#candidate|3891|()|var|int64
call_3889 = relay.TupleGetItem(func_3610_call(relay.reshape(const_3890.astype('int8'), [135,]), relay.reshape(var_3891.astype('int64'), []), ), 2)
call_3892 = relay.TupleGetItem(func_3613_call(relay.reshape(const_3890.astype('int8'), [135,]), relay.reshape(var_3891.astype('int64'), []), ), 2)
func_2737_call = mod.get_global_var('func_2737')
func_2738_call = mutated_mod.get_global_var('func_2738')
call_3899 = func_2737_call()
call_3900 = func_2737_call()
output = relay.Tuple([bop_3861,call_3889,const_3890,var_3891,call_3899,])
output2 = relay.Tuple([bop_3861,call_3892,const_3890,var_3891,call_3900,])
func_3903 = relay.Function([var_3859,var_3860,var_3891,], output)
mod['func_3903'] = func_3903
mod = relay.transform.InferType()(mod)
var_3904 = relay.var("var_3904", dtype = "int16", shape = (15, 7, 8))#candidate|3904|(15, 7, 8)|var|int16
var_3905 = relay.var("var_3905", dtype = "int16", shape = (15, 7, 8))#candidate|3905|(15, 7, 8)|var|int16
var_3906 = relay.var("var_3906", dtype = "int64", shape = ())#candidate|3906|()|var|int64
output = func_3903(var_3904,var_3905,var_3906,)
func_3907 = relay.Function([var_3904,var_3905,var_3906,], output)
mutated_mod['func_3907'] = func_3907
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2401_call = mod.get_global_var('func_2401')
func_2402_call = mutated_mod.get_global_var('func_2402')
call_3919 = relay.TupleGetItem(func_2401_call(), 1)
call_3920 = relay.TupleGetItem(func_2402_call(), 1)
output = relay.Tuple([call_3919,])
output2 = relay.Tuple([call_3920,])
func_3925 = relay.Function([], output)
mod['func_3925'] = func_3925
mod = relay.transform.InferType()(mod)
output = func_3925()
func_3926 = relay.Function([], output)
mutated_mod['func_3926'] = func_3926
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1187_call = mod.get_global_var('func_1187')
func_1188_call = mutated_mod.get_global_var('func_1188')
call_3970 = relay.TupleGetItem(func_1187_call(), 0)
call_3971 = relay.TupleGetItem(func_1188_call(), 0)
func_3533_call = mod.get_global_var('func_3533')
func_3534_call = mutated_mod.get_global_var('func_3534')
call_3978 = relay.TupleGetItem(func_3533_call(), 0)
call_3979 = relay.TupleGetItem(func_3534_call(), 0)
func_1940_call = mod.get_global_var('func_1940')
func_1942_call = mutated_mod.get_global_var('func_1942')
call_3987 = relay.TupleGetItem(func_1940_call(), 2)
call_3988 = relay.TupleGetItem(func_1942_call(), 2)
func_24_call = mod.get_global_var('func_24')
func_27_call = mutated_mod.get_global_var('func_27')
var_3999 = relay.var("var_3999", dtype = "int64", shape = ())#candidate|3999|()|var|int64
call_3998 = relay.TupleGetItem(func_24_call(relay.reshape(var_3999.astype('int64'), [])), 0)
call_4000 = relay.TupleGetItem(func_27_call(relay.reshape(var_3999.astype('int64'), [])), 0)
output = relay.Tuple([call_3970,call_3978,call_3987,call_3998,var_3999,])
output2 = relay.Tuple([call_3971,call_3979,call_3988,call_4000,var_3999,])
func_4005 = relay.Function([var_3999,], output)
mod['func_4005'] = func_4005
mod = relay.transform.InferType()(mod)
var_4006 = relay.var("var_4006", dtype = "int64", shape = ())#candidate|4006|()|var|int64
output = func_4005(var_4006)
func_4007 = relay.Function([var_4006], output)
mutated_mod['func_4007'] = func_4007
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2777_call = mod.get_global_var('func_2777')
func_2778_call = mutated_mod.get_global_var('func_2778')
call_4019 = relay.TupleGetItem(func_2777_call(), 0)
call_4020 = relay.TupleGetItem(func_2778_call(), 0)
func_2863_call = mod.get_global_var('func_2863')
func_2865_call = mutated_mod.get_global_var('func_2865')
call_4055 = relay.TupleGetItem(func_2863_call(), 1)
call_4056 = relay.TupleGetItem(func_2865_call(), 1)
output = relay.Tuple([call_4019,call_4055,])
output2 = relay.Tuple([call_4020,call_4056,])
func_4057 = relay.Function([], output)
mod['func_4057'] = func_4057
mod = relay.transform.InferType()(mod)
output = func_4057()
func_4058 = relay.Function([], output)
mutated_mod['func_4058'] = func_4058
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2514_call = mod.get_global_var('func_2514')
func_2515_call = mutated_mod.get_global_var('func_2515')
call_4070 = func_2514_call()
call_4071 = func_2514_call()
output = relay.Tuple([call_4070,])
output2 = relay.Tuple([call_4071,])
func_4082 = relay.Function([], output)
mod['func_4082'] = func_4082
mod = relay.transform.InferType()(mod)
output = func_4082()
func_4083 = relay.Function([], output)
mutated_mod['func_4083'] = func_4083
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2282_call = mod.get_global_var('func_2282')
func_2283_call = mutated_mod.get_global_var('func_2283')
call_4089 = func_2282_call()
call_4090 = func_2282_call()
output = call_4089
output2 = call_4090
func_4125 = relay.Function([], output)
mod['func_4125'] = func_4125
mod = relay.transform.InferType()(mod)
mutated_mod['func_4125'] = func_4125
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4125_call = mutated_mod.get_global_var('func_4125')
call_4126 = func_4125_call()
output = call_4126
func_4127 = relay.Function([], output)
mutated_mod['func_4127'] = func_4127
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1801_call = mod.get_global_var('func_1801')
func_1803_call = mutated_mod.get_global_var('func_1803')
call_4136 = func_1801_call()
call_4137 = func_1801_call()
output = relay.Tuple([call_4136,])
output2 = relay.Tuple([call_4137,])
func_4151 = relay.Function([], output)
mod['func_4151'] = func_4151
mod = relay.transform.InferType()(mod)
mutated_mod['func_4151'] = func_4151
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4151_call = mutated_mod.get_global_var('func_4151')
call_4152 = func_4151_call()
output = call_4152
func_4153 = relay.Function([], output)
mutated_mod['func_4153'] = func_4153
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1940_call = mod.get_global_var('func_1940')
func_1942_call = mutated_mod.get_global_var('func_1942')
call_4174 = relay.TupleGetItem(func_1940_call(), 1)
call_4175 = relay.TupleGetItem(func_1942_call(), 1)
output = call_4174
output2 = call_4175
func_4178 = relay.Function([], output)
mod['func_4178'] = func_4178
mod = relay.transform.InferType()(mod)
output = func_4178()
func_4179 = relay.Function([], output)
mutated_mod['func_4179'] = func_4179
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2514_call = mod.get_global_var('func_2514')
func_2515_call = mutated_mod.get_global_var('func_2515')
call_4220 = func_2514_call()
call_4221 = func_2514_call()
var_4222 = relay.var("var_4222", dtype = "float32", shape = (14, 3, 10))#candidate|4222|(14, 3, 10)|var|float32
bop_4223 = relay.not_equal(call_4220.astype('bool'), var_4222.astype('bool')) # shape=(14, 3, 10)
bop_4226 = relay.not_equal(call_4221.astype('bool'), var_4222.astype('bool')) # shape=(14, 3, 10)
bop_4237 = relay.greater_equal(call_4220.astype('bool'), var_4222.astype('bool')) # shape=(14, 3, 10)
bop_4240 = relay.greater_equal(call_4221.astype('bool'), var_4222.astype('bool')) # shape=(14, 3, 10)
func_607_call = mod.get_global_var('func_607')
func_610_call = mutated_mod.get_global_var('func_610')
const_4247 = relay.const([9,-7,-4,-2,-5,-7,-1,1,-6,-1,2,-5,1,-3,1,1,7,-2,6,-2,-1,7,-1,-1,5,-7,-1,-3,8,-3,9,10,3,-7,-10,-8,-9,-2,-3,9,-8,-4,-3,-9,-4,-2,6,9,8,8,6,-8,3,5,-4,6,3,10,9,-6,2,8,-4,9,4,9,-3,4,6,4,6,-3,-1,4,2,5,-10,4,-9,-5,10,2,10,1,-5,-7,4,9,-2,-5,5,-6,10,-10,-3,-3,-6,8,3,1,4,-9,7,-4,-3,1,7,-4,9,10,-6,7,-10,-9,4,-10,-7,7,-1,2,9,1,-3,5,-8,8,-7,-7,9,1,5,4,-2,-7,-1], dtype = "int8")#candidate|4247|(135,)|const|int8
call_4246 = func_607_call(relay.reshape(const_4247.astype('int8'), [3, 5, 9]))
call_4248 = func_607_call(relay.reshape(const_4247.astype('int8'), [3, 5, 9]))
output = relay.Tuple([bop_4223,bop_4237,call_4246,const_4247,])
output2 = relay.Tuple([bop_4226,bop_4240,call_4248,const_4247,])
func_4249 = relay.Function([var_4222,], output)
mod['func_4249'] = func_4249
mod = relay.transform.InferType()(mod)
mutated_mod['func_4249'] = func_4249
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4250 = relay.var("var_4250", dtype = "float32", shape = (14, 3, 10))#candidate|4250|(14, 3, 10)|var|float32
func_4249_call = mutated_mod.get_global_var('func_4249')
call_4251 = func_4249_call(var_4250)
output = call_4251
func_4252 = relay.Function([var_4250], output)
mutated_mod['func_4252'] = func_4252
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3040_call = mod.get_global_var('func_3040')
func_3042_call = mutated_mod.get_global_var('func_3042')
call_4265 = func_3040_call()
call_4266 = func_3040_call()
func_1748_call = mod.get_global_var('func_1748')
func_1750_call = mutated_mod.get_global_var('func_1750')
call_4272 = relay.TupleGetItem(func_1748_call(), 0)
call_4273 = relay.TupleGetItem(func_1750_call(), 0)
func_3721_call = mod.get_global_var('func_3721')
func_3725_call = mutated_mod.get_global_var('func_3725')
var_4300 = relay.var("var_4300", dtype = "float64", shape = (1, 280))#candidate|4300|(1, 280)|var|float64
call_4299 = relay.TupleGetItem(func_3721_call(relay.reshape(call_4272.astype('float64'), []), relay.reshape(var_4300.astype('float64'), [2, 10, 14]), ), 0)
call_4301 = relay.TupleGetItem(func_3725_call(relay.reshape(call_4272.astype('float64'), []), relay.reshape(var_4300.astype('float64'), [2, 10, 14]), ), 0)
output = relay.Tuple([call_4265,call_4272,call_4299,var_4300,])
output2 = relay.Tuple([call_4266,call_4273,call_4301,var_4300,])
func_4302 = relay.Function([var_4300,], output)
mod['func_4302'] = func_4302
mod = relay.transform.InferType()(mod)
var_4303 = relay.var("var_4303", dtype = "float64", shape = (1, 280))#candidate|4303|(1, 280)|var|float64
output = func_4302(var_4303)
func_4304 = relay.Function([var_4303], output)
mutated_mod['func_4304'] = func_4304
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1859_call = mod.get_global_var('func_1859')
func_1861_call = mutated_mod.get_global_var('func_1861')
call_4317 = relay.TupleGetItem(func_1859_call(), 0)
call_4318 = relay.TupleGetItem(func_1861_call(), 0)
output = relay.Tuple([call_4317,])
output2 = relay.Tuple([call_4318,])
func_4319 = relay.Function([], output)
mod['func_4319'] = func_4319
mod = relay.transform.InferType()(mod)
output = func_4319()
func_4320 = relay.Function([], output)
mutated_mod['func_4320'] = func_4320
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1603_call = mod.get_global_var('func_1603')
func_1604_call = mutated_mod.get_global_var('func_1604')
call_4380 = relay.TupleGetItem(func_1603_call(), 0)
call_4381 = relay.TupleGetItem(func_1604_call(), 0)
func_1187_call = mod.get_global_var('func_1187')
func_1188_call = mutated_mod.get_global_var('func_1188')
call_4386 = relay.TupleGetItem(func_1187_call(), 0)
call_4387 = relay.TupleGetItem(func_1188_call(), 0)
func_994_call = mod.get_global_var('func_994')
func_997_call = mutated_mod.get_global_var('func_997')
var_4389 = relay.var("var_4389", dtype = "float32", shape = (24, 2))#candidate|4389|(24, 2)|var|float32
call_4388 = relay.TupleGetItem(func_994_call(relay.reshape(var_4389.astype('float32'), [6, 1, 8])), 1)
call_4390 = relay.TupleGetItem(func_997_call(relay.reshape(var_4389.astype('float32'), [6, 1, 8])), 1)
func_1859_call = mod.get_global_var('func_1859')
func_1861_call = mutated_mod.get_global_var('func_1861')
call_4391 = relay.TupleGetItem(func_1859_call(), 0)
call_4392 = relay.TupleGetItem(func_1861_call(), 0)
output = relay.Tuple([call_4380,call_4386,call_4388,var_4389,call_4391,])
output2 = relay.Tuple([call_4381,call_4387,call_4390,var_4389,call_4392,])
func_4398 = relay.Function([var_4389,], output)
mod['func_4398'] = func_4398
mod = relay.transform.InferType()(mod)
mutated_mod['func_4398'] = func_4398
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4399 = relay.var("var_4399", dtype = "float32", shape = (24, 2))#candidate|4399|(24, 2)|var|float32
func_4398_call = mutated_mod.get_global_var('func_4398')
call_4400 = func_4398_call(var_4399)
output = call_4400
func_4401 = relay.Function([var_4399], output)
mutated_mod['func_4401'] = func_4401
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4472 = relay.var("var_4472", dtype = "float32", shape = (10, 4, 10))#candidate|4472|(10, 4, 10)|var|float32
const_4473 = relay.const([[[0.095145,6.365803,-2.703541,-3.926579,-8.769385,-8.039802,2.141231,-5.183377,6.552878,-1.993736],[-3.909729,6.035856,3.025725,-0.948549,-5.514972,5.392063,1.371624,-5.409720,-9.561124,5.070581],[9.239568,4.247819,3.300048,4.340950,-1.414076,-8.041157,-3.722046,-4.785718,8.662695,2.026034],[-4.909574,5.031910,0.304511,3.864750,8.715143,-5.499178,9.283679,5.310734,-9.176676,0.166381]],[[-1.221337,0.684794,-2.668349,-1.766361,-1.647233,4.905296,-6.911573,-1.273652,2.950068,7.595224],[2.432871,1.797443,6.435137,5.602321,-4.815712,6.342801,-2.546482,0.840178,-6.925499,3.984632],[4.872260,0.711905,8.769765,7.080946,9.307758,2.425433,0.517009,5.850296,-1.667553,-8.125897],[-9.184673,2.978153,-8.372211,3.219598,8.847142,9.640524,7.543974,-2.378018,-7.153638,9.092417]],[[3.105228,-8.687962,-5.240118,5.784786,-3.051710,9.225173,6.222729,-8.563710,2.569617,-6.373101],[-1.347785,-7.794479,-2.490544,-1.191850,-7.787968,2.176056,9.984702,-8.576614,4.713880,-7.978120],[4.997054,-7.669916,-0.946550,-4.985701,-1.975121,-2.750881,-7.362970,7.668125,-4.498286,-8.954107],[5.117806,-4.628939,7.210886,-6.772401,-6.511288,9.622464,-5.584309,7.931298,-1.749600,5.249905]],[[-8.225314,1.691530,-2.177787,-0.598166,-2.768441,4.108457,-1.751112,-5.764003,9.981499,-6.038618],[5.825354,2.858184,-7.540296,1.254717,1.066058,8.993481,-7.069213,-2.797234,5.762725,1.544845],[9.677475,-8.593316,-5.822112,-8.700118,2.526338,-5.943000,-6.648833,0.803971,-8.220515,1.115402],[7.542754,2.661918,6.575149,-4.310351,-7.028671,-0.952367,-4.061712,4.395711,-5.858622,-1.489285]],[[9.778487,-4.465224,1.011430,-6.691644,-4.164780,5.153178,-1.829655,-7.345919,-0.505354,1.346737],[-5.643590,5.108986,-5.247948,-0.851968,-4.597806,-4.454378,5.880639,7.835010,-2.873244,-0.648231],[6.132311,-7.374235,-7.981111,0.962434,5.285050,-7.498810,-9.375057,2.929592,-5.949376,6.794954],[-2.117578,-9.421862,1.662776,-7.291074,0.215403,-6.185421,-4.314537,3.850888,5.621653,-2.351202]],[[3.502628,7.785362,-3.515198,-8.013341,-2.748837,8.523523,5.609980,-3.967635,9.144439,4.143685],[4.053278,3.043069,-1.488804,-3.412802,8.073662,4.044867,9.984166,-9.124574,4.756324,9.569053],[1.584546,-5.458238,-2.037877,2.635281,-1.228790,0.843706,-6.528668,3.997060,9.424420,4.409920],[-3.431236,4.490444,6.351375,9.278082,-4.206491,-8.731505,3.697987,-5.736249,5.101022,2.699008]],[[-7.770765,3.171373,1.823030,-0.209053,-0.082692,0.426387,-4.052984,4.953422,9.112291,-2.982569],[8.051887,6.104730,2.604616,-8.180790,3.566699,-5.984294,-3.413074,-2.007475,4.353201,-8.857869],[-0.950468,-7.557251,-4.922213,-2.196010,6.671744,5.910123,0.012826,2.203398,8.704044,6.458998],[-2.430945,-5.056599,2.439720,-1.518806,5.393792,3.710286,7.271955,-4.614580,9.206045,3.335102]],[[4.773457,6.517945,8.205289,-8.979806,-6.483366,7.196709,3.302316,-4.672889,-3.048846,7.354358],[0.203258,-6.572118,6.419039,4.992217,8.596993,3.754078,9.992703,-6.678049,6.290513,1.176457],[-7.745323,-5.604559,4.653269,2.946597,-7.792523,3.181587,1.009953,-5.509695,4.727911,6.176120],[-0.847296,2.731267,9.291853,-7.366829,-9.479489,-0.132619,-1.980923,6.096121,5.020993,9.658598]],[[6.039718,-6.310754,-8.458469,5.084614,-8.229711,9.462822,2.280219,-3.418415,-6.867614,-5.270947],[2.868253,0.634958,6.002595,6.916073,5.470344,-6.986221,9.027136,3.266251,3.587681,8.179997],[7.774883,-3.482706,-9.335672,3.580099,0.719977,1.064921,0.610310,-4.123654,2.999152,6.518365],[2.384670,-6.536416,-7.454813,-3.254653,-9.035360,1.083847,-0.634145,3.733165,9.989583,0.448096]],[[-2.413476,0.482465,-1.291017,-4.743628,9.006711,-9.500082,-9.102153,0.795617,1.873831,-7.451496],[-0.782236,5.755788,-3.649547,3.449781,-2.618144,-1.839877,0.354758,-6.099303,-4.387922,-9.473786],[-1.577500,-1.730058,7.491328,-8.196583,7.037329,-0.025933,-2.556930,6.137749,-0.897020,-3.746782],[1.517792,5.053581,-9.514275,-7.097842,9.098784,-1.912053,-8.898186,-2.454098,9.798833,-2.707675]]], dtype = "float32")#candidate|4473|(10, 4, 10)|const|float32
bop_4474 = relay.divide(var_4472.astype('float32'), relay.reshape(const_4473.astype('float32'), relay.shape_of(var_4472))) # shape=(10, 4, 10)
func_4398_call = mod.get_global_var('func_4398')
func_4401_call = mutated_mod.get_global_var('func_4401')
var_4501 = relay.var("var_4501", dtype = "float32", shape = (48,))#candidate|4501|(48,)|var|float32
call_4500 = relay.TupleGetItem(func_4398_call(relay.reshape(var_4501.astype('float32'), [24, 2])), 0)
call_4502 = relay.TupleGetItem(func_4401_call(relay.reshape(var_4501.astype('float32'), [24, 2])), 0)
output = relay.Tuple([bop_4474,call_4500,var_4501,])
output2 = relay.Tuple([bop_4474,call_4502,var_4501,])
func_4504 = relay.Function([var_4472,var_4501,], output)
mod['func_4504'] = func_4504
mod = relay.transform.InferType()(mod)
mutated_mod['func_4504'] = func_4504
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4504_call = mutated_mod.get_global_var('func_4504')
var_4506 = relay.var("var_4506", dtype = "float32", shape = (10, 4, 10))#candidate|4506|(10, 4, 10)|var|float32
var_4507 = relay.var("var_4507", dtype = "float32", shape = (48,))#candidate|4507|(48,)|var|float32
call_4505 = func_4504_call(var_4506,var_4507,)
output = call_4505
func_4508 = relay.Function([var_4506,var_4507,], output)
mutated_mod['func_4508'] = func_4508
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1674_call = mod.get_global_var('func_1674')
func_1675_call = mutated_mod.get_global_var('func_1675')
call_4512 = relay.TupleGetItem(func_1674_call(), 2)
call_4513 = relay.TupleGetItem(func_1675_call(), 2)
var_4532 = relay.var("var_4532", dtype = "bool", shape = (15, 10, 6))#candidate|4532|(15, 10, 6)|var|bool
bop_4533 = relay.logical_or(call_4512.astype('bool'), relay.reshape(var_4532.astype('bool'), relay.shape_of(call_4512))) # shape=(15, 10, 6)
bop_4536 = relay.logical_or(call_4513.astype('bool'), relay.reshape(var_4532.astype('bool'), relay.shape_of(call_4513))) # shape=(15, 10, 6)
func_3508_call = mod.get_global_var('func_3508')
func_3510_call = mutated_mod.get_global_var('func_3510')
call_4549 = func_3508_call()
call_4550 = func_3508_call()
func_3508_call = mod.get_global_var('func_3508')
func_3510_call = mutated_mod.get_global_var('func_3510')
call_4567 = func_3508_call()
call_4568 = func_3508_call()
output = relay.Tuple([bop_4533,call_4549,call_4567,])
output2 = relay.Tuple([bop_4536,call_4550,call_4568,])
func_4569 = relay.Function([var_4532,], output)
mod['func_4569'] = func_4569
mod = relay.transform.InferType()(mod)
var_4570 = relay.var("var_4570", dtype = "bool", shape = (15, 10, 6))#candidate|4570|(15, 10, 6)|var|bool
output = func_4569(var_4570)
func_4571 = relay.Function([var_4570], output)
mutated_mod['func_4571'] = func_4571
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2282_call = mod.get_global_var('func_2282')
func_2283_call = mutated_mod.get_global_var('func_2283')
call_4578 = func_2282_call()
call_4579 = func_2282_call()
func_994_call = mod.get_global_var('func_994')
func_997_call = mutated_mod.get_global_var('func_997')
var_4581 = relay.var("var_4581", dtype = "float32", shape = (48,))#candidate|4581|(48,)|var|float32
call_4580 = relay.TupleGetItem(func_994_call(relay.reshape(var_4581.astype('float32'), [6, 1, 8])), 1)
call_4582 = relay.TupleGetItem(func_997_call(relay.reshape(var_4581.astype('float32'), [6, 1, 8])), 1)
func_2737_call = mod.get_global_var('func_2737')
func_2738_call = mutated_mod.get_global_var('func_2738')
call_4589 = func_2737_call()
call_4590 = func_2737_call()
output = relay.Tuple([call_4578,call_4580,var_4581,call_4589,])
output2 = relay.Tuple([call_4579,call_4582,var_4581,call_4590,])
func_4603 = relay.Function([var_4581,], output)
mod['func_4603'] = func_4603
mod = relay.transform.InferType()(mod)
var_4604 = relay.var("var_4604", dtype = "float32", shape = (48,))#candidate|4604|(48,)|var|float32
output = func_4603(var_4604)
func_4605 = relay.Function([var_4604], output)
mutated_mod['func_4605'] = func_4605
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2009_call = mod.get_global_var('func_2009')
func_2011_call = mutated_mod.get_global_var('func_2011')
call_4609 = relay.TupleGetItem(func_2009_call(), 1)
call_4610 = relay.TupleGetItem(func_2011_call(), 1)
uop_4617 = relay.log2(call_4609.astype('float64')) # shape=(14, 1, 10)
uop_4619 = relay.log2(call_4610.astype('float64')) # shape=(14, 1, 10)
func_2863_call = mod.get_global_var('func_2863')
func_2865_call = mutated_mod.get_global_var('func_2865')
call_4633 = relay.TupleGetItem(func_2863_call(), 0)
call_4634 = relay.TupleGetItem(func_2865_call(), 0)
var_4640 = relay.var("var_4640", dtype = "float64", shape = (14, 1, 10))#candidate|4640|(14, 1, 10)|var|float64
bop_4641 = relay.minimum(uop_4617.astype('uint16'), relay.reshape(var_4640.astype('uint16'), relay.shape_of(uop_4617))) # shape=(14, 1, 10)
bop_4644 = relay.minimum(uop_4619.astype('uint16'), relay.reshape(var_4640.astype('uint16'), relay.shape_of(uop_4619))) # shape=(14, 1, 10)
output = relay.Tuple([call_4633,bop_4641,])
output2 = relay.Tuple([call_4634,bop_4644,])
func_4645 = relay.Function([var_4640,], output)
mod['func_4645'] = func_4645
mod = relay.transform.InferType()(mod)
mutated_mod['func_4645'] = func_4645
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4646 = relay.var("var_4646", dtype = "float64", shape = (14, 1, 10))#candidate|4646|(14, 1, 10)|var|float64
func_4645_call = mutated_mod.get_global_var('func_4645')
call_4647 = func_4645_call(var_4646)
output = call_4647
func_4648 = relay.Function([var_4646], output)
mutated_mod['func_4648'] = func_4648
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3670_call = mod.get_global_var('func_3670')
func_3672_call = mutated_mod.get_global_var('func_3672')
call_4686 = relay.TupleGetItem(func_3670_call(), 0)
call_4687 = relay.TupleGetItem(func_3672_call(), 0)
output = call_4686
output2 = call_4687
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
func_2737_call = mod.get_global_var('func_2737')
func_2738_call = mutated_mod.get_global_var('func_2738')
call_4727 = func_2737_call()
call_4728 = func_2737_call()
output = relay.Tuple([call_4727,])
output2 = relay.Tuple([call_4728,])
func_4735 = relay.Function([], output)
mod['func_4735'] = func_4735
mod = relay.transform.InferType()(mod)
output = func_4735()
func_4736 = relay.Function([], output)
mutated_mod['func_4736'] = func_4736
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4739 = relay.var("var_4739", dtype = "int8", shape = (2, 16, 12))#candidate|4739|(2, 16, 12)|var|int8
const_4740 = relay.const([[[4,1,9,-8,9,4,7,-3,-2,5,3,-8],[-9,1,3,-7,1,-6,3,9,-2,-7,-5,-5],[9,10,-1,-6,-9,6,-8,8,-2,-4,-10,8],[5,2,8,-7,-9,-8,7,3,-10,7,3,-9],[-4,9,-5,-8,4,10,-7,-8,6,-9,1,-7],[10,-1,3,-5,5,3,-2,-10,-2,8,-9,-8],[-2,6,-8,6,-10,10,-9,2,-10,5,7,8],[-8,-1,-3,-2,5,-10,-2,2,3,5,8,7],[-4,1,10,3,6,-6,10,-5,5,-9,-2,-9],[4,9,1,9,10,9,9,-9,5,-5,-5,-3],[4,7,2,10,-10,-7,5,-8,-5,-7,10,-1],[-5,-1,5,-3,3,-4,6,2,-3,8,-4,6],[-3,4,-3,6,1,8,-1,-6,1,-1,6,-2],[10,-10,6,4,9,1,-4,9,6,3,8,-2],[-9,-5,-6,-5,-9,-1,-9,4,-2,1,6,3],[-9,1,-6,-6,8,2,-2,-10,-2,-8,5,-2]],[[-9,-5,4,8,4,1,-2,7,-10,-4,5,-5],[-5,9,-7,9,3,10,3,1,7,7,8,-9],[-2,3,7,6,1,1,8,3,-5,-9,2,6],[-1,-1,5,-7,3,6,-8,-9,10,8,-4,-9],[5,-7,-9,6,-6,-9,7,9,8,7,10,8],[9,-7,-6,-2,-6,7,4,5,2,-2,-4,8],[-10,1,-4,1,-2,6,5,-6,-9,-6,6,-2],[7,-7,8,-4,-4,-8,3,-2,8,-10,6,-3],[1,-7,-1,7,-6,3,-4,2,-4,-6,2,10],[6,2,-8,-8,-4,-7,-7,-5,1,-6,-4,10],[-1,-3,-6,2,4,5,-8,-4,9,7,8,-8],[-9,1,-7,1,1,2,10,-9,-7,-10,-9,-5],[-6,6,-2,2,-1,7,5,-5,-4,4,-10,-10],[-7,-9,-5,-7,-5,-4,7,10,-8,-5,7,-1],[-6,6,-8,-10,7,3,4,-2,1,7,1,-6],[-6,-3,-1,-3,9,-5,-6,-4,-6,4,7,8]]], dtype = "int8")#candidate|4740|(2, 16, 12)|const|int8
bop_4741 = relay.multiply(var_4739.astype('int8'), relay.reshape(const_4740.astype('int8'), relay.shape_of(var_4739))) # shape=(2, 16, 12)
uop_4760 = relay.erf(var_4739.astype('float64')) # shape=(2, 16, 12)
output = relay.Tuple([bop_4741,uop_4760,])
output2 = relay.Tuple([bop_4741,uop_4760,])
func_4765 = relay.Function([var_4739,], output)
mod['func_4765'] = func_4765
mod = relay.transform.InferType()(mod)
mutated_mod['func_4765'] = func_4765
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4766 = relay.var("var_4766", dtype = "int8", shape = (2, 16, 12))#candidate|4766|(2, 16, 12)|var|int8
func_4765_call = mutated_mod.get_global_var('func_4765')
call_4767 = func_4765_call(var_4766)
output = call_4767
func_4768 = relay.Function([var_4766], output)
mutated_mod['func_4768'] = func_4768
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3650_call = mod.get_global_var('func_3650')
func_3651_call = mutated_mod.get_global_var('func_3651')
call_4777 = relay.TupleGetItem(func_3650_call(), 0)
call_4778 = relay.TupleGetItem(func_3651_call(), 0)
output = call_4777
output2 = call_4778
func_4785 = relay.Function([], output)
mod['func_4785'] = func_4785
mod = relay.transform.InferType()(mod)
mutated_mod['func_4785'] = func_4785
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4785_call = mutated_mod.get_global_var('func_4785')
call_4786 = func_4785_call()
output = call_4786
func_4787 = relay.Function([], output)
mutated_mod['func_4787'] = func_4787
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2145_call = mod.get_global_var('func_2145')
func_2146_call = mutated_mod.get_global_var('func_2146')
call_4807 = relay.TupleGetItem(func_2145_call(), 0)
call_4808 = relay.TupleGetItem(func_2146_call(), 0)
output = relay.Tuple([call_4807,])
output2 = relay.Tuple([call_4808,])
func_4837 = relay.Function([], output)
mod['func_4837'] = func_4837
mod = relay.transform.InferType()(mod)
output = func_4837()
func_4838 = relay.Function([], output)
mutated_mod['func_4838'] = func_4838
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3040_call = mod.get_global_var('func_3040')
func_3042_call = mutated_mod.get_global_var('func_3042')
call_4908 = func_3040_call()
call_4909 = func_3040_call()
output = call_4908
output2 = call_4909
func_4910 = relay.Function([], output)
mod['func_4910'] = func_4910
mod = relay.transform.InferType()(mod)
mutated_mod['func_4910'] = func_4910
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4910_call = mutated_mod.get_global_var('func_4910')
call_4911 = func_4910_call()
output = call_4911
func_4912 = relay.Function([], output)
mutated_mod['func_4912'] = func_4912
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2282_call = mod.get_global_var('func_2282')
func_2283_call = mutated_mod.get_global_var('func_2283')
call_4937 = func_2282_call()
call_4938 = func_2282_call()
func_847_call = mod.get_global_var('func_847')
func_850_call = mutated_mod.get_global_var('func_850')
var_4946 = relay.var("var_4946", dtype = "float64", shape = (234, 2))#candidate|4946|(234, 2)|var|float64
var_4947 = relay.var("var_4947", dtype = "int64", shape = ())#candidate|4947|()|var|int64
call_4945 = relay.TupleGetItem(func_847_call(relay.reshape(var_4946.astype('float64'), [13, 4, 9]), relay.reshape(var_4947.astype('int64'), []), ), 3)
call_4948 = relay.TupleGetItem(func_850_call(relay.reshape(var_4946.astype('float64'), [13, 4, 9]), relay.reshape(var_4947.astype('int64'), []), ), 3)
output = relay.Tuple([call_4937,call_4945,var_4946,var_4947,])
output2 = relay.Tuple([call_4938,call_4948,var_4946,var_4947,])
func_4955 = relay.Function([var_4946,var_4947,], output)
mod['func_4955'] = func_4955
mod = relay.transform.InferType()(mod)
mutated_mod['func_4955'] = func_4955
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4955_call = mutated_mod.get_global_var('func_4955')
var_4957 = relay.var("var_4957", dtype = "float64", shape = (234, 2))#candidate|4957|(234, 2)|var|float64
var_4958 = relay.var("var_4958", dtype = "int64", shape = ())#candidate|4958|()|var|int64
call_4956 = func_4955_call(var_4957,var_4958,)
output = call_4956
func_4959 = relay.Function([var_4957,var_4958,], output)
mutated_mod['func_4959'] = func_4959
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1940_call = mod.get_global_var('func_1940')
func_1942_call = mutated_mod.get_global_var('func_1942')
call_4975 = relay.TupleGetItem(func_1940_call(), 1)
call_4976 = relay.TupleGetItem(func_1942_call(), 1)
var_4997 = relay.var("var_4997", dtype = "float32", shape = (6, 4, 8))#candidate|4997|(6, 4, 8)|var|float32
bop_4998 = relay.floor_mod(call_4975.astype('float32'), var_4997.astype('float32')) # shape=(6, 4, 8)
bop_5001 = relay.floor_mod(call_4976.astype('float32'), var_4997.astype('float32')) # shape=(6, 4, 8)
output = relay.Tuple([bop_4998,])
output2 = relay.Tuple([bop_5001,])
func_5020 = relay.Function([var_4997,], output)
mod['func_5020'] = func_5020
mod = relay.transform.InferType()(mod)
mutated_mod['func_5020'] = func_5020
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5021 = relay.var("var_5021", dtype = "float32", shape = (6, 4, 8))#candidate|5021|(6, 4, 8)|var|float32
func_5020_call = mutated_mod.get_global_var('func_5020')
call_5022 = func_5020_call(var_5021)
output = call_5022
func_5023 = relay.Function([var_5021], output)
mutated_mod['func_5023'] = func_5023
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4689_call = mod.get_global_var('func_4689')
func_4691_call = mutated_mod.get_global_var('func_4691')
call_5035 = func_4689_call()
call_5036 = func_4689_call()
output = call_5035
output2 = call_5036
func_5040 = relay.Function([], output)
mod['func_5040'] = func_5040
mod = relay.transform.InferType()(mod)
output = func_5040()
func_5041 = relay.Function([], output)
mutated_mod['func_5041'] = func_5041
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3650_call = mod.get_global_var('func_3650')
func_3651_call = mutated_mod.get_global_var('func_3651')
call_5118 = relay.TupleGetItem(func_3650_call(), 0)
call_5119 = relay.TupleGetItem(func_3651_call(), 0)
func_3345_call = mod.get_global_var('func_3345')
func_3347_call = mutated_mod.get_global_var('func_3347')
var_5133 = relay.var("var_5133", dtype = "float32", shape = (48,))#candidate|5133|(48,)|var|float32
call_5132 = relay.TupleGetItem(func_3345_call(relay.reshape(var_5133.astype('float32'), [48,])), 4)
call_5134 = relay.TupleGetItem(func_3347_call(relay.reshape(var_5133.astype('float32'), [48,])), 4)
func_4319_call = mod.get_global_var('func_4319')
func_4320_call = mutated_mod.get_global_var('func_4320')
call_5150 = relay.TupleGetItem(func_4319_call(), 0)
call_5151 = relay.TupleGetItem(func_4320_call(), 0)
func_1984_call = mod.get_global_var('func_1984')
func_1985_call = mutated_mod.get_global_var('func_1985')
call_5172 = relay.TupleGetItem(func_1984_call(), 1)
call_5173 = relay.TupleGetItem(func_1985_call(), 1)
func_1859_call = mod.get_global_var('func_1859')
func_1861_call = mutated_mod.get_global_var('func_1861')
call_5174 = relay.TupleGetItem(func_1859_call(), 0)
call_5175 = relay.TupleGetItem(func_1861_call(), 0)
func_4398_call = mod.get_global_var('func_4398')
func_4401_call = mutated_mod.get_global_var('func_4401')
call_5176 = relay.TupleGetItem(func_4398_call(relay.reshape(call_5132.astype('float32'), [24, 2])), 1)
call_5177 = relay.TupleGetItem(func_4401_call(relay.reshape(call_5132.astype('float32'), [24, 2])), 1)
output = relay.Tuple([call_5118,call_5132,var_5133,call_5150,call_5172,call_5174,call_5176,])
output2 = relay.Tuple([call_5119,call_5134,var_5133,call_5151,call_5173,call_5175,call_5177,])
func_5178 = relay.Function([var_5133,], output)
mod['func_5178'] = func_5178
mod = relay.transform.InferType()(mod)
var_5179 = relay.var("var_5179", dtype = "float32", shape = (48,))#candidate|5179|(48,)|var|float32
output = func_5178(var_5179)
func_5180 = relay.Function([var_5179], output)
mutated_mod['func_5180'] = func_5180
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3793_call = mod.get_global_var('func_3793')
func_3794_call = mutated_mod.get_global_var('func_3794')
call_5256 = relay.TupleGetItem(func_3793_call(), 0)
call_5257 = relay.TupleGetItem(func_3794_call(), 0)
func_1140_call = mod.get_global_var('func_1140')
func_1141_call = mutated_mod.get_global_var('func_1141')
call_5258 = relay.TupleGetItem(func_1140_call(), 0)
call_5259 = relay.TupleGetItem(func_1141_call(), 0)
func_24_call = mod.get_global_var('func_24')
func_27_call = mutated_mod.get_global_var('func_27')
var_5294 = relay.var("var_5294", dtype = "int64", shape = ())#candidate|5294|()|var|int64
call_5293 = relay.TupleGetItem(func_24_call(relay.reshape(var_5294.astype('int64'), [])), 0)
call_5295 = relay.TupleGetItem(func_27_call(relay.reshape(var_5294.astype('int64'), [])), 0)
func_4398_call = mod.get_global_var('func_4398')
func_4401_call = mutated_mod.get_global_var('func_4401')
var_5298 = relay.var("var_5298", dtype = "float32", shape = (48,))#candidate|5298|(48,)|var|float32
call_5297 = relay.TupleGetItem(func_4398_call(relay.reshape(var_5298.astype('float32'), [24, 2])), 1)
call_5299 = relay.TupleGetItem(func_4401_call(relay.reshape(var_5298.astype('float32'), [24, 2])), 1)
func_3508_call = mod.get_global_var('func_3508')
func_3510_call = mutated_mod.get_global_var('func_3510')
call_5307 = func_3508_call()
call_5308 = func_3508_call()
output = relay.Tuple([call_5256,call_5258,call_5293,var_5294,call_5297,var_5298,call_5307,])
output2 = relay.Tuple([call_5257,call_5259,call_5295,var_5294,call_5299,var_5298,call_5308,])
func_5311 = relay.Function([var_5294,var_5298,], output)
mod['func_5311'] = func_5311
mod = relay.transform.InferType()(mod)
mutated_mod['func_5311'] = func_5311
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5311_call = mutated_mod.get_global_var('func_5311')
var_5313 = relay.var("var_5313", dtype = "int64", shape = ())#candidate|5313|()|var|int64
var_5314 = relay.var("var_5314", dtype = "float32", shape = (48,))#candidate|5314|(48,)|var|float32
call_5312 = func_5311_call(var_5313,var_5314,)
output = call_5312
func_5315 = relay.Function([var_5313,var_5314,], output)
mutated_mod['func_5315'] = func_5315
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3533_call = mod.get_global_var('func_3533')
func_3534_call = mutated_mod.get_global_var('func_3534')
call_5372 = relay.TupleGetItem(func_3533_call(), 0)
call_5373 = relay.TupleGetItem(func_3534_call(), 0)
output = call_5372
output2 = call_5373
func_5379 = relay.Function([], output)
mod['func_5379'] = func_5379
mod = relay.transform.InferType()(mod)
output = func_5379()
func_5380 = relay.Function([], output)
mutated_mod['func_5380'] = func_5380
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1801_call = mod.get_global_var('func_1801')
func_1803_call = mutated_mod.get_global_var('func_1803')
call_5390 = func_1801_call()
call_5391 = func_1801_call()
output = relay.Tuple([call_5390,])
output2 = relay.Tuple([call_5391,])
func_5392 = relay.Function([], output)
mod['func_5392'] = func_5392
mod = relay.transform.InferType()(mod)
mutated_mod['func_5392'] = func_5392
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5392_call = mutated_mod.get_global_var('func_5392')
call_5393 = func_5392_call()
output = call_5393
func_5394 = relay.Function([], output)
mutated_mod['func_5394'] = func_5394
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4319_call = mod.get_global_var('func_4319')
func_4320_call = mutated_mod.get_global_var('func_4320')
call_5399 = relay.TupleGetItem(func_4319_call(), 0)
call_5400 = relay.TupleGetItem(func_4320_call(), 0)
output = call_5399
output2 = call_5400
func_5411 = relay.Function([], output)
mod['func_5411'] = func_5411
mod = relay.transform.InferType()(mod)
output = func_5411()
func_5412 = relay.Function([], output)
mutated_mod['func_5412'] = func_5412
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1178_call = mod.get_global_var('func_1178')
func_1180_call = mutated_mod.get_global_var('func_1180')
call_5415 = func_1178_call()
call_5416 = func_1178_call()
const_5429 = relay.const([[[9.673619,-7.389125,3.120891,6.880805,2.668053,-6.431307,-6.226211,2.428077,-1.608909,-4.409865],[3.504422,-5.482927,-1.899010,3.920074,5.856317,-6.972127,-7.827107,9.546880,-6.984955,9.440135],[8.143103,-3.628760,-6.183122,2.024587,-4.361611,-9.830462,7.784073,5.552968,4.243419,6.846826],[5.570072,-9.848435,-4.551162,-0.278123,-1.273251,4.328222,5.764010,9.044242,7.338229,-1.706714],[-7.140503,4.055706,-9.492246,4.053351,-4.206879,-9.983982,9.699282,2.607364,-9.275569,-5.131288],[-6.735299,-0.490631,1.976303,0.414186,-9.999597,-8.540927,-0.715326,-7.425137,-0.004186,-9.117526],[5.181939,-1.182898,1.607341,-5.459577,6.010636,0.255883,-1.564206,-3.160467,0.637357,-8.450439],[4.078620,8.159357,5.288674,-3.277046,3.377413,-2.124901,4.792080,6.919574,-4.660245,-6.388387],[-7.900725,6.171512,-9.971121,-4.328272,1.274213,1.585279,2.761977,-0.143370,7.102040,-7.909206],[-8.798842,9.831322,-6.616390,-4.544310,-2.333381,-2.682818,-4.181134,-1.728482,6.046093,4.037192],[4.410274,-0.639405,4.196555,7.748386,4.505824,6.333756,-6.081654,-4.019819,-8.084468,-1.395724],[4.417216,3.527972,-1.342735,-5.299272,2.087189,6.924082,8.560204,5.187293,-2.092858,9.454060],[9.081100,8.002757,6.563896,-8.933351,7.923121,-7.640860,7.431100,-2.996695,0.540269,-9.021596],[-0.762788,-4.756354,9.917417,-4.012299,-8.100112,0.993612,6.175152,-6.506156,-0.182198,-8.708681],[0.362191,6.677748,-5.169989,-6.753871,-0.013122,-4.040609,-0.337851,-6.576167,2.925394,-3.569894]],[[-1.620935,2.270052,-3.993578,-0.203666,-7.542211,-9.104655,-5.068675,-9.602126,-7.467045,-4.454407],[6.426516,4.319187,2.180057,8.865790,9.559639,3.193020,-9.953187,1.192162,-4.805046,7.612328],[-8.794543,-2.438072,7.251109,5.408406,9.117812,8.110564,3.318854,0.447072,-6.345368,0.623730],[-4.829763,-2.323753,8.405662,4.500591,3.511012,-8.548290,1.351736,-3.068713,0.548983,-9.360209],[-0.571388,-3.504163,-0.545211,-7.235065,-4.136352,-4.871606,-8.379326,8.756476,-9.207568,8.465091],[-8.579645,5.069901,-3.089372,-8.934827,-3.588888,0.250944,-5.161200,-9.632012,3.237944,-6.735142],[-2.746051,-9.874257,7.923784,-2.861496,-5.129285,2.608604,5.326181,-1.562671,2.797944,0.587682],[7.775294,-1.152609,-7.242643,6.932052,4.126644,-7.331339,-2.577729,4.904465,-3.711913,-1.093723],[4.120839,6.930841,-0.366063,7.303145,9.124102,2.043767,0.370404,-7.410852,-7.656009,9.857260],[6.067178,8.003694,-2.995045,4.760512,-1.409485,3.894399,-0.106353,-1.947941,2.934835,-6.508805],[7.324461,6.006474,4.423990,-8.673406,9.068689,5.897786,8.926338,2.738532,7.550496,5.737773],[-8.106845,-1.445025,8.264308,8.941374,-8.948936,9.982422,-4.923858,-6.061506,4.012377,4.068296],[-4.071101,9.320956,-8.489298,0.238206,-7.101849,9.984042,0.921587,6.675985,4.467997,8.328020],[-9.478736,4.412591,-7.444019,-8.025677,-3.640272,-1.822943,-2.148146,4.675412,-7.688964,5.516125],[8.021951,8.764597,-0.484297,3.236505,-5.452869,6.005802,-4.745300,9.017842,-1.081817,-9.936739]],[[8.956811,0.112137,-8.503441,-2.454364,1.993764,6.690068,0.376220,6.583560,8.319297,8.185327],[-3.082737,-3.976087,2.159924,4.927848,3.029673,-4.754403,-4.239626,7.868613,-0.700960,-9.702366],[3.248392,-6.904147,-8.106953,-8.112969,4.999814,2.315720,-5.230656,-2.284493,7.783373,8.027332],[7.641223,-4.180916,6.977584,-2.104902,7.194476,4.780915,8.883461,3.647972,8.039104,8.718363],[7.239623,-8.534787,0.374428,4.616710,-8.861956,4.893058,0.117834,-2.281973,4.974977,-6.478867],[1.804965,5.958576,-5.473300,-9.259606,-1.425242,-9.513299,1.781290,6.104861,2.647470,4.276320],[7.355689,7.371483,-8.066227,4.634600,-8.543868,8.471485,3.267476,-8.482129,0.744012,-6.919655],[9.908465,-4.565103,0.825147,5.411254,-8.113590,5.322497,6.716575,-7.590975,-2.237694,-7.977186],[-8.771024,-6.726144,-3.405289,6.950213,0.143046,-4.114187,-4.965314,3.736604,-1.419649,-8.053623],[-9.073938,6.192716,-3.216577,4.572381,8.251916,2.668463,6.695126,-2.575079,8.008323,-2.326175],[2.744597,3.625824,8.655601,0.735620,2.957226,-8.772243,0.364018,2.962928,-0.865932,-5.149953],[-8.774648,2.016597,7.073670,-6.977883,6.180063,-7.303317,7.673510,-6.680322,-3.286549,-1.318178],[9.321324,4.771989,-1.419400,-2.203804,-7.485694,8.924496,-6.624597,-3.549218,-3.276774,-1.781249],[0.497597,-4.610605,-9.378489,2.432593,-1.515442,-2.794358,2.055647,7.652831,1.780590,-7.123192],[-2.513363,-7.483673,-7.963040,2.641420,9.209548,-0.465948,-2.271781,9.626735,6.896893,7.113145]],[[1.048526,1.452562,-7.197039,-4.892510,-2.056412,7.688907,-0.561882,0.831130,-4.202400,9.306926],[4.601115,2.505930,-1.353405,-1.067720,6.914883,-4.644937,-3.277587,7.520174,-5.129035,-9.613694],[-5.503967,6.115513,3.597647,8.206722,5.925057,-2.881881,-1.147845,-0.631609,-3.387414,-3.335307],[0.789526,-6.712725,-7.722270,-3.827992,-1.888465,4.200094,-6.362309,8.542335,-6.866300,3.474795],[-0.880968,-0.524339,4.457437,0.465599,1.003415,-6.924020,-8.436357,-4.642683,-9.006711,8.587718],[7.002196,-8.524714,-8.559898,-1.890144,-4.463618,-3.045646,6.923659,-4.555936,-5.986744,-0.290531],[5.939889,-7.827868,-2.025328,7.148464,1.059558,2.591636,7.102143,-8.889788,8.010248,-3.928763],[-8.323843,-7.645252,5.559853,7.547207,3.958209,-3.086480,-4.157140,-2.308117,0.181044,6.193935],[1.169519,-2.440953,-8.036505,-9.040569,3.095851,-2.932399,8.907388,1.266093,6.499277,-3.628729],[-6.091487,2.949588,8.551133,2.868022,0.357530,6.873846,2.472531,-3.334066,-7.065777,-4.666748],[2.773354,-8.124650,8.059102,-4.427548,-3.701552,6.928576,7.511544,3.696908,6.418178,4.544556],[5.928524,7.647211,-5.183812,1.886025,-3.907688,-0.800439,-9.948604,-8.456082,-8.388878,-7.267261],[-5.217957,-6.574390,-0.077430,-1.879192,-2.713718,3.764202,8.011103,3.236909,-4.638835,-5.048169],[-2.321448,-1.955889,0.377562,-6.304983,3.779635,-6.552264,7.324716,8.520831,-8.997723,6.147564],[-9.849578,8.801243,5.659122,4.802670,8.761924,-7.619525,1.706273,-3.833821,2.763251,-0.839137]],[[7.414925,-7.629920,6.273980,-5.216476,-1.317662,3.037889,-2.712129,-0.437263,7.458346,4.292494],[7.681976,-6.499837,6.655595,-8.163530,9.153921,4.162069,9.180957,5.120498,-8.157651,9.228808],[0.658776,0.012402,9.009275,0.496439,8.468830,6.758200,-2.886685,4.543111,-1.382213,9.156225],[5.440957,-3.046358,-0.247554,9.646177,0.104833,8.090224,1.297109,2.369674,-0.379740,8.512716],[0.489340,8.925271,-5.738654,2.668323,-2.329608,1.574218,-9.182421,-3.364401,1.760302,6.204465],[-1.237587,-0.793985,1.654342,-7.845649,-9.800868,6.158481,-9.525767,-3.921339,-1.271278,0.379773],[-1.145309,-8.475019,-5.968651,6.256861,-6.430081,5.600239,-5.710833,1.585341,4.022602,8.116625],[8.200903,3.610905,7.681579,2.958278,-8.641931,-9.621842,2.937584,3.055539,-3.455579,6.238720],[9.255657,6.745340,-4.864256,1.933769,3.365228,-8.872917,3.712888,-3.099001,9.182433,-1.185838],[0.048332,-9.055213,9.686491,-5.673716,-1.738883,5.171224,-0.271494,5.565113,8.913506,-5.917769],[-6.781084,4.750795,1.795159,-0.702123,4.130876,-2.437789,-6.300728,3.139177,-2.101418,2.340966],[-8.325477,-6.154379,1.212018,3.312326,-5.346199,5.258123,-9.645331,-6.626260,6.452526,-2.440625],[-7.726113,4.636400,5.412063,-8.230497,-5.399533,9.251970,-3.389006,-0.950839,5.119575,-1.324536],[3.303519,-5.917654,5.730792,5.863747,-3.640198,7.278473,-9.151758,4.569863,-9.929797,7.539195],[1.611716,9.507951,-0.450130,2.907997,1.810994,3.274896,-8.958748,3.997171,1.470035,-0.150966]],[[-0.144527,-7.192126,-8.129752,6.422152,7.477435,3.944682,7.513685,8.909646,-6.397542,0.003429],[-6.193065,8.478036,4.789724,-7.056311,0.079844,-0.551698,0.723974,7.084781,-7.099645,-3.924688],[3.387237,-1.225375,-4.559003,9.079790,-0.805278,-5.063017,8.237640,4.286954,-3.732679,2.300093],[-4.528360,-0.074611,-1.147102,3.616438,-2.299597,3.838258,-1.189919,-5.530758,4.648190,2.900658],[-4.582116,-0.628587,3.337815,-9.313306,-6.701161,-4.127649,0.599164,-7.601305,-8.244917,-6.811608],[2.125957,-3.353065,9.603008,-6.689423,-8.491972,9.100074,7.097178,9.769665,3.618425,3.888982],[6.979793,9.074301,-7.646772,3.988418,4.421973,0.162937,5.518576,-6.764867,-4.353973,3.403986],[3.445939,9.129632,-0.163287,8.825301,2.189462,6.506625,-9.092358,7.627634,-1.619204,6.947833],[8.993668,-6.188797,9.221970,1.585809,1.620026,-4.707627,1.277379,-9.706865,-0.862274,-3.996995],[-5.940570,0.117843,-5.053391,1.491849,7.953107,-2.485386,6.401147,8.392654,-5.021570,-3.130435],[0.281720,-5.572859,-5.843669,-1.180943,-3.324892,-0.988961,1.800485,-4.240406,9.353843,-9.395883],[-9.284038,7.924970,-3.041078,-5.445024,0.866569,-5.823408,-6.337810,-7.028692,1.429582,9.474695],[9.664721,-5.848235,6.462366,-1.651328,-5.941689,4.417553,1.705692,-2.903535,5.347543,-5.448763],[1.586905,3.588181,3.750672,8.286004,0.353131,4.093059,-3.845457,9.477470,-6.719101,-5.759462],[-9.521907,7.559120,-8.919624,7.616145,6.671993,8.025178,3.673434,-5.694743,-4.807280,9.597768]],[[-2.674369,-4.610654,8.363971,6.498659,2.864033,-4.926112,2.002404,8.600891,-4.110529,-5.182372],[7.386198,-7.930838,-5.370952,7.959494,-9.073573,-1.051685,3.785886,-4.360761,-7.096205,-8.060399],[4.843072,-0.006140,3.347619,9.943086,-5.148346,4.185588,5.507174,-5.907552,-7.932651,-3.967901],[8.872057,0.698993,9.425043,3.196721,2.995178,2.980652,-8.629017,-3.141623,9.982711,2.395209],[8.699019,5.315372,6.964454,-7.982051,-1.548383,-1.858649,-1.592047,-7.515575,4.221969,0.596941],[-1.920562,-1.099209,-1.298702,-8.314690,-2.888000,-1.078251,-2.480973,-9.753060,3.846144,9.273270],[3.877412,0.446326,5.974126,8.237070,4.821424,-8.936223,6.875366,7.791230,3.529382,5.538643],[0.572422,8.962581,-9.514931,7.719591,-3.091912,1.265244,7.482931,0.842489,-2.525764,4.202295],[-1.333326,4.588731,-5.300248,4.518626,-7.198551,7.654364,-0.813734,8.530954,-2.443498,5.566969],[2.907456,-9.971510,0.219390,-1.217596,-9.137907,-7.385371,3.204387,-3.332348,-4.692520,5.356357],[5.623432,-1.275602,9.951980,-7.125620,9.344826,-9.022241,-9.621391,5.600819,2.733470,4.061551],[4.506376,-4.693462,-3.961931,3.600304,-2.636837,0.578850,8.217919,-9.650024,-9.397188,5.028590],[-0.599490,-9.591190,-2.564420,-9.927283,3.148249,-3.612261,8.248542,0.249114,8.259293,-8.354408],[3.938695,5.778026,-7.832836,1.028272,-2.013798,-7.039388,1.957067,4.149332,-9.031619,8.986583],[-3.383129,-7.446942,-4.469419,3.356046,-0.924671,0.462831,9.475045,9.107077,-7.940683,-0.731227]],[[4.104166,3.411816,-1.300510,-5.198114,6.998572,-5.974917,9.642889,4.973679,2.401044,-7.975717],[9.947090,7.652890,-9.372534,-9.425686,-5.362109,-0.548072,1.512563,-5.620746,-0.440425,-1.036351],[-4.620199,5.981763,2.362104,8.509882,7.100470,0.968533,2.627495,-3.983103,9.118422,3.362572],[1.340190,3.044904,8.709963,-0.581888,-8.070352,4.605935,-0.758463,3.485107,-8.264206,-5.193512],[-8.678593,-3.701684,-5.825371,3.558767,9.198171,3.879197,-8.291689,4.837444,-1.473370,-0.506590],[-0.464610,7.175328,-0.481005,-4.669692,6.545235,3.359042,-9.913583,-8.039965,-2.529789,-4.166037],[-2.415365,-8.720180,-6.906689,-8.076239,-2.304220,-4.769292,0.927319,5.070670,-6.742566,-9.033904],[-3.487773,6.918912,9.965508,4.454478,8.476966,1.032370,-4.597569,6.847673,6.156924,2.256238],[-6.722391,-2.406091,-5.798722,5.669423,7.151243,-8.433188,3.662623,9.255957,0.990609,-3.874600],[-8.079015,-0.186472,-9.123252,-6.193857,-2.473523,2.192613,6.612927,-1.232147,5.454869,-4.214337],[2.357842,-4.789688,-7.915626,7.666889,-1.230813,-4.469294,4.528741,6.447405,-1.061570,1.590968],[-5.108422,5.287546,-8.166362,4.229076,-5.472164,-7.205954,-1.691637,-0.528773,-6.498379,8.494367],[-5.058049,-0.453572,-8.267390,8.984342,1.831664,2.638288,9.536595,9.021910,-7.888533,0.043151],[-4.171048,-8.228715,-4.679972,9.837397,-8.192168,4.835122,-9.236642,-2.745599,-7.280730,-2.208436],[-2.322534,8.557594,-6.368186,5.984008,2.480013,6.819148,0.120320,-7.103250,2.405250,-1.608645]],[[-8.157095,-1.128459,6.863058,-7.012414,-7.375099,4.308533,-0.392780,-3.156667,2.428360,-2.300582],[-2.652790,-3.435478,5.876385,2.789680,-2.106915,0.760051,5.002124,-9.803473,-1.600414,-4.123227],[6.208017,-2.090210,-8.835982,-3.061151,-9.350433,-0.455878,8.694344,-2.493433,-7.484205,2.977907],[-3.827753,5.692233,-5.814285,-3.876052,-4.712804,2.336169,4.123059,-3.178190,-4.782101,7.069568],[0.035051,2.460638,1.704866,3.154840,0.501594,-1.787781,1.775767,9.675867,3.850204,2.464770],[9.126350,8.867171,-8.238560,-4.570976,9.593973,1.852452,-9.278492,4.459834,1.208581,5.379305],[8.887978,-3.425128,1.942265,-7.890875,8.383298,7.690075,-6.887389,7.079460,-5.640112,2.589906],[-0.319852,-6.091890,6.147768,-5.707249,-3.742693,7.617257,7.243132,6.008262,7.520077,-3.071431],[2.849577,9.199152,-8.492800,-6.366162,4.696891,-0.458412,-7.508295,-0.235020,-3.450501,-9.693377],[-6.434992,-2.980138,1.353684,-1.854509,9.740354,-9.339445,-5.778453,-3.558488,-4.468432,4.918848],[-2.050110,3.159358,-1.079651,-2.166382,-3.869087,-2.731700,-9.542050,4.811449,-2.235719,1.359471],[-0.789350,-4.014564,9.840907,9.983011,0.957056,4.195070,9.244936,-3.669909,-5.713406,-5.253196],[-5.421428,8.758875,-6.889205,-6.507605,4.254452,-5.065767,8.260346,-0.428296,-0.404026,1.057377],[4.590943,7.575374,3.215879,-1.877306,6.724231,6.443332,3.465220,-6.774185,6.330890,-2.896234],[-4.239803,-4.725223,8.986149,1.421052,-3.912450,3.982218,7.233464,-0.420575,5.381245,9.756401]],[[-6.770749,-4.329746,6.758835,7.565353,6.455163,2.500410,-1.832681,-2.020562,3.328713,5.831891],[-0.990463,3.371150,-4.186103,-5.861297,-2.468918,-0.719887,-3.401015,3.620958,5.890211,-0.465471],[-4.194071,7.344551,8.464289,7.628890,6.698335,5.840650,9.234249,9.328469,-0.947273,7.478261],[2.909242,5.602561,-7.141466,-4.946113,4.165366,1.904168,-3.041973,1.993751,-0.897264,-0.028465],[2.911464,4.749942,-9.616712,-3.506269,-3.317399,-2.869320,1.329197,-7.922771,-6.948401,-0.083496],[1.893647,3.786534,-6.617372,-8.747273,5.598124,-6.787250,-8.301122,-2.965992,-4.309669,4.199729],[-1.706594,0.520588,-9.653406,-2.462401,-0.588995,-2.215769,-5.541579,9.233801,-6.868795,0.044849],[2.057413,8.612292,3.655274,-0.040196,-2.383163,-8.051135,3.379101,8.077378,9.988229,-9.660905],[-8.647756,-0.258887,5.532826,1.648675,9.633860,4.468420,-1.030308,-5.788813,-2.102167,0.045753],[-8.825467,-0.768068,6.750106,2.977755,3.222199,-3.394449,2.885505,-8.198893,1.352016,-4.275880],[-2.395153,2.858149,-5.729633,-7.852562,-1.590045,-4.417671,5.548003,5.749772,-5.294549,-1.579880],[-0.740881,3.028731,4.460920,-6.465145,3.142948,8.620280,2.611476,-7.061856,-8.116130,-2.864365],[-8.433454,7.991432,2.996515,4.448458,-6.783897,3.328470,-7.334670,-3.194779,-7.929401,-6.064097],[4.212338,7.462536,-7.974335,7.310068,-5.689872,-1.215318,-2.677915,4.026888,-7.114431,5.833757],[-5.312151,2.566282,0.362422,-3.106119,7.984018,2.370756,-2.788461,0.852423,-4.791478,1.601884]],[[-4.493905,0.245096,7.709918,2.559838,4.504704,-6.421605,9.731759,0.936493,7.038404,7.529827],[-2.049185,-1.698195,6.534588,-8.345522,-3.252678,1.572744,1.249221,9.739161,6.833731,-6.236098],[8.269717,-3.068664,-9.184520,4.441420,3.737101,-4.353360,7.234466,-7.614261,-5.601168,-6.027699],[-7.709496,-7.314133,-1.791988,-9.685922,-3.810782,1.567133,-9.459370,-5.545481,2.487419,-8.523721],[-1.281607,-8.199707,0.971729,7.408223,8.032912,-3.457243,0.116358,5.256153,-3.235907,4.109409],[-1.857241,-7.569560,-1.236821,-0.648636,-2.744719,-1.417487,1.429291,-8.938947,5.453537,2.501398],[2.033390,-1.026856,-6.176943,6.888035,8.101603,5.348087,0.344190,-9.961701,-5.129786,5.415143],[-6.046686,-1.491680,-9.018638,-8.810627,-2.760846,3.577385,-6.907091,-0.194029,0.316429,8.458039],[-0.980874,9.325990,3.596253,8.405842,-1.620906,-7.103230,-8.871997,-6.676417,-5.979953,-1.368677],[-8.237533,-1.312073,3.742320,7.397018,-6.573954,1.366785,7.266063,-1.374182,6.053503,1.292031],[-1.870421,-7.790348,-0.962291,-6.606626,5.254814,1.152120,-9.331407,-6.788584,-2.908545,-3.096591],[2.900261,0.614606,-3.655617,6.626901,0.292208,3.005338,-7.677620,-0.905691,8.637685,3.992481],[4.920528,-5.351770,6.275404,8.149944,2.590479,-5.856166,9.513516,8.383521,-4.192765,4.392918],[3.398303,9.703644,-7.906771,-9.231321,-2.669028,0.326964,-4.843812,4.745170,-5.914832,0.960727],[6.607338,-8.475086,2.050290,-0.190070,-7.134751,7.436925,8.757609,-7.792724,-6.032589,0.582886]],[[-7.510547,-1.232676,-8.981633,-6.216001,-2.054921,-8.988472,-3.936877,6.084241,0.868416,3.568051],[1.749345,7.096865,0.329346,5.401705,0.286330,3.640862,1.857514,-3.707627,5.205198,-4.964220],[9.770183,2.180163,-1.276812,4.198770,5.089409,6.908224,-2.652372,1.371525,-4.468703,4.171858],[3.590833,-0.334131,1.602539,-6.974965,2.308685,-7.204276,-4.268384,-8.926529,-8.490815,-5.769021],[-6.158157,8.059076,-4.679380,3.348858,0.343431,-0.556674,4.926144,9.280924,-7.865418,6.950123],[-1.514736,-1.739809,-8.298308,5.891954,-0.266007,-0.037982,-9.234566,1.558805,-4.160350,9.655541],[-4.594495,-1.161349,-4.609927,-7.745799,6.843017,1.633741,3.658622,-8.232115,-1.391593,7.642938],[0.363378,-1.118444,0.539141,3.580724,-0.626879,8.620585,-1.621716,-3.576843,0.427904,2.590954],[-3.783060,-4.883657,-9.958382,1.933713,4.841377,-8.237006,-5.337201,-4.412216,-0.294357,6.068919],[-4.498685,1.483081,-9.539000,-7.127307,-5.642442,8.857961,-3.066580,7.012129,-5.753067,7.106170],[0.198501,4.653339,-7.954181,5.170565,9.204270,9.898269,4.169453,-0.853991,-2.302425,4.956304],[5.968193,-6.479668,-9.799719,-0.505952,-9.182640,-3.028240,5.455497,-7.993732,7.667265,4.508104],[-9.351010,8.134363,0.221075,-9.058870,-4.217286,8.517035,-6.266707,1.312007,9.484889,0.602915],[0.030786,2.914280,4.713874,8.135798,6.614810,8.928134,2.532489,8.177823,2.990694,7.861083],[4.092666,8.805776,-9.543628,-9.201906,-6.419375,0.353698,-3.727287,9.493248,-0.402932,-6.699766]],[[4.121498,-3.546252,-0.090481,5.569358,0.123002,9.876338,2.301139,-9.156204,6.336009,6.301252],[-4.716753,-8.608012,8.901620,0.842364,-3.086833,5.973642,7.882528,-8.792490,3.643100,2.120042],[-9.848886,8.827955,1.980306,6.852612,0.470572,6.589275,-4.370375,-7.191058,7.161411,8.766289],[3.692355,7.130803,-8.791829,9.647668,6.999284,-8.484747,2.898914,-0.153726,7.295952,-2.397380],[-6.611626,7.024727,9.484452,1.248826,1.236530,-8.610129,2.021317,5.617682,8.517430,-9.498776],[-5.106619,8.946704,-9.251352,-0.544309,4.598457,-2.421637,-8.544019,-9.027434,8.040606,-5.891467],[9.035202,-3.025911,-1.008414,-8.220236,-6.577920,6.027780,-7.143623,-4.728618,-2.208635,-4.605344],[5.005738,0.839947,-5.061174,3.329189,4.565061,-0.574963,-4.738763,-3.350947,2.597332,9.000277],[7.836521,-1.086395,9.562282,-2.814179,9.112317,6.639285,-2.947457,3.714196,1.021023,-9.413096],[-1.561629,7.193555,1.795850,-8.144133,-2.842048,-5.138265,-3.913042,2.471058,-7.827394,2.372313],[6.001390,-1.265355,6.069689,-1.919443,5.396168,-3.333951,-6.222293,-8.185062,5.261136,-7.708948],[-4.092141,2.178328,1.324976,-7.589098,-6.904554,4.504156,7.238403,7.215716,6.637809,1.096652],[7.005739,1.580146,2.703735,8.846915,-1.899331,-2.930265,2.425098,4.998731,3.208317,-4.738561],[6.189933,6.062777,9.275780,8.050988,-7.516847,3.668146,-1.910899,2.285058,5.792285,-8.070458],[-5.629237,-3.075694,-0.711159,-4.374527,-4.388874,-8.077968,7.244061,-6.258979,-7.951441,6.421663]],[[-2.058918,-7.607077,0.891131,-9.013708,2.289084,-6.551551,9.943699,5.811176,-8.562026,5.871288],[-1.867811,-6.399465,8.123488,-2.173771,8.617301,7.452258,6.887494,-6.994307,4.292455,7.335714],[-0.716227,9.021871,-9.177070,8.462259,-8.580056,2.740045,-5.492322,-4.240835,-9.104844,-6.112959],[0.248221,8.324224,2.834468,7.497819,-0.170563,9.952029,8.218443,5.978001,1.739910,-5.992381],[0.028363,-7.523434,-3.275377,-7.072951,-9.429262,-2.122115,-1.594175,-4.905820,1.560707,-4.779286],[-9.765273,-4.272865,-0.219799,2.441800,5.150270,-9.757437,-7.641958,-9.376212,0.608288,0.622602],[5.337921,8.223558,-5.934770,-3.077631,-2.872440,6.539681,-7.970261,-0.634453,0.406656,6.375624],[4.669972,-9.368229,-2.117988,-9.218214,6.655488,4.822046,6.093612,-2.938042,-7.018980,-8.123590],[9.235520,1.081824,1.912180,9.449729,-4.713348,0.748211,-2.732088,4.365165,3.132224,-8.975645],[2.376447,2.343121,6.538600,-8.674139,-9.786003,-3.751399,1.728918,-6.363921,4.151613,1.604962],[-1.676279,7.831233,-9.753191,8.874345,2.653419,-5.968155,-4.302809,5.266470,9.594126,9.408206],[-6.000446,-0.365305,-8.706872,2.067343,-3.686999,7.833335,2.686261,3.505695,7.735853,2.948299],[-7.547928,7.330299,-9.724080,-7.674276,7.579008,1.791898,5.827243,4.929158,-7.975418,3.039650],[3.734315,9.287973,-2.828833,3.995064,-4.114697,-9.191028,-6.096658,8.248986,-3.080335,2.276861],[7.171983,-4.088591,-6.087842,-4.417882,-9.392848,0.239591,-8.929779,-7.888916,8.839564,-4.670272]]], dtype = "float32")#candidate|5429|(14, 15, 10)|const|float32
bop_5430 = relay.logical_xor(call_5415.astype('int8'), const_5429.astype('int8')) # shape=(14, 15, 10)
bop_5433 = relay.logical_xor(call_5416.astype('int8'), const_5429.astype('int8')) # shape=(14, 15, 10)
output = bop_5430
output2 = bop_5433
func_5441 = relay.Function([], output)
mod['func_5441'] = func_5441
mod = relay.transform.InferType()(mod)
mutated_mod['func_5441'] = func_5441
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5441_call = mutated_mod.get_global_var('func_5441')
call_5442 = func_5441_call()
output = call_5442
func_5443 = relay.Function([], output)
mutated_mod['func_5443'] = func_5443
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1603_call = mod.get_global_var('func_1603')
func_1604_call = mutated_mod.get_global_var('func_1604')
call_5463 = relay.TupleGetItem(func_1603_call(), 0)
call_5464 = relay.TupleGetItem(func_1604_call(), 0)
output = call_5463
output2 = call_5464
func_5467 = relay.Function([], output)
mod['func_5467'] = func_5467
mod = relay.transform.InferType()(mod)
mutated_mod['func_5467'] = func_5467
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5467_call = mutated_mod.get_global_var('func_5467')
call_5468 = func_5467_call()
output = call_5468
func_5469 = relay.Function([], output)
mutated_mod['func_5469'] = func_5469
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2777_call = mod.get_global_var('func_2777')
func_2778_call = mutated_mod.get_global_var('func_2778')
call_5483 = relay.TupleGetItem(func_2777_call(), 0)
call_5484 = relay.TupleGetItem(func_2778_call(), 0)
func_1486_call = mod.get_global_var('func_1486')
func_1488_call = mutated_mod.get_global_var('func_1488')
const_5494 = relay.const([[-5.279565,5.850599,4.413702,4.959449,-8.391476,8.890724,6.838055,-5.663203,-6.475575,7.682296,1.440237,5.978817],[6.865899,7.187766,1.808609,-6.948529,-5.548008,4.337477,-2.610409,4.987901,3.635512,2.872456,7.062930,-0.122635],[-8.294098,-2.439409,-3.685049,-8.880422,-1.212929,-2.175580,-9.246875,4.919376,-8.185731,-7.929333,3.416422,1.313019],[3.130854,4.101358,7.900881,-4.783368,-1.069890,5.755947,-8.198456,-5.088977,5.905653,-7.215614,4.303897,-9.233898]], dtype = "float32")#candidate|5494|(4, 12)|const|float32
call_5493 = relay.TupleGetItem(func_1486_call(relay.reshape(const_5494.astype('float32'), [2, 24])), 4)
call_5495 = relay.TupleGetItem(func_1488_call(relay.reshape(const_5494.astype('float32'), [2, 24])), 4)
func_4504_call = mod.get_global_var('func_4504')
func_4508_call = mutated_mod.get_global_var('func_4508')
var_5499 = relay.var("var_5499", dtype = "float32", shape = (2, 200))#candidate|5499|(2, 200)|var|float32
call_5498 = relay.TupleGetItem(func_4504_call(relay.reshape(var_5499.astype('float32'), [10, 4, 10]), relay.reshape(const_5494.astype('float32'), [48,]), ), 0)
call_5500 = relay.TupleGetItem(func_4508_call(relay.reshape(var_5499.astype('float32'), [10, 4, 10]), relay.reshape(const_5494.astype('float32'), [48,]), ), 0)
bop_5503 = relay.logical_or(var_5499.astype('bool'), call_5483.astype('bool')) # shape=(2, 200)
bop_5506 = relay.logical_or(var_5499.astype('bool'), call_5484.astype('bool')) # shape=(2, 200)
func_4955_call = mod.get_global_var('func_4955')
func_4959_call = mutated_mod.get_global_var('func_4959')
var_5515 = relay.var("var_5515", dtype = "float64", shape = (468,))#candidate|5515|(468,)|var|float64
call_5514 = relay.TupleGetItem(func_4955_call(relay.reshape(var_5515.astype('float64'), [234, 2]), relay.reshape(call_5483.astype('int64'), []), ), 3)
call_5516 = relay.TupleGetItem(func_4959_call(relay.reshape(var_5515.astype('float64'), [234, 2]), relay.reshape(call_5483.astype('int64'), []), ), 3)
func_2196_call = mod.get_global_var('func_2196')
func_2198_call = mutated_mod.get_global_var('func_2198')
call_5518 = relay.TupleGetItem(func_2196_call(relay.reshape(const_5494.astype('float32'), [48,])), 3)
call_5519 = relay.TupleGetItem(func_2198_call(relay.reshape(const_5494.astype('float32'), [48,])), 3)
output = relay.Tuple([call_5493,const_5494,call_5498,bop_5503,call_5514,var_5515,call_5518,])
output2 = relay.Tuple([call_5495,const_5494,call_5500,bop_5506,call_5516,var_5515,call_5519,])
func_5520 = relay.Function([var_5499,var_5515,], output)
mod['func_5520'] = func_5520
mod = relay.transform.InferType()(mod)
var_5521 = relay.var("var_5521", dtype = "float32", shape = (2, 200))#candidate|5521|(2, 200)|var|float32
var_5522 = relay.var("var_5522", dtype = "float64", shape = (468,))#candidate|5522|(468,)|var|float64
output = func_5520(var_5521,var_5522,)
func_5523 = relay.Function([var_5521,var_5522,], output)
mutated_mod['func_5523'] = func_5523
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4082_call = mod.get_global_var('func_4082')
func_4083_call = mutated_mod.get_global_var('func_4083')
call_5595 = relay.TupleGetItem(func_4082_call(), 0)
call_5596 = relay.TupleGetItem(func_4083_call(), 0)
func_2243_call = mod.get_global_var('func_2243')
func_2245_call = mutated_mod.get_global_var('func_2245')
const_5602 = relay.const([[5.004133],[-2.977688],[-7.415725],[4.585681],[2.679048],[-3.138312],[-6.885784],[0.779952],[-2.274553],[-6.387013],[1.597935],[5.687372],[0.078350],[6.837935],[2.342110],[2.672993],[-0.401333],[2.984330],[-8.858259],[8.147460],[-2.092460],[1.263359],[5.252866],[3.408437],[-0.733324],[1.754207],[-1.564911],[3.264051],[7.353713],[-4.396041],[-6.338852],[4.641616],[3.390474],[3.367106],[-1.631210],[-2.098171],[-9.992727],[6.775074],[-5.623226],[5.866654],[7.544130],[-2.753269],[-6.305141],[4.661758],[-2.662344],[-9.016212],[6.556940],[-1.500705]], dtype = "float32")#candidate|5602|(48, 1)|const|float32
call_5601 = relay.TupleGetItem(func_2243_call(relay.reshape(const_5602.astype('float32'), [48,])), 0)
call_5603 = relay.TupleGetItem(func_2245_call(relay.reshape(const_5602.astype('float32'), [48,])), 0)
output = relay.Tuple([call_5595,call_5601,const_5602,])
output2 = relay.Tuple([call_5596,call_5603,const_5602,])
func_5634 = relay.Function([], output)
mod['func_5634'] = func_5634
mod = relay.transform.InferType()(mod)
output = func_5634()
func_5635 = relay.Function([], output)
mutated_mod['func_5635'] = func_5635
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3508_call = mod.get_global_var('func_3508')
func_3510_call = mutated_mod.get_global_var('func_3510')
call_5666 = func_3508_call()
call_5667 = func_3508_call()
func_3925_call = mod.get_global_var('func_3925')
func_3926_call = mutated_mod.get_global_var('func_3926')
call_5668 = relay.TupleGetItem(func_3925_call(), 0)
call_5669 = relay.TupleGetItem(func_3926_call(), 0)
output = relay.Tuple([call_5666,call_5668,])
output2 = relay.Tuple([call_5667,call_5669,])
func_5674 = relay.Function([], output)
mod['func_5674'] = func_5674
mod = relay.transform.InferType()(mod)
mutated_mod['func_5674'] = func_5674
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5674_call = mutated_mod.get_global_var('func_5674')
call_5675 = func_5674_call()
output = call_5675
func_5676 = relay.Function([], output)
mutated_mod['func_5676'] = func_5676
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5718 = relay.var("var_5718", dtype = "int8", shape = ())#candidate|5718|()|var|int8
const_5719 = relay.const([[6],[-1],[1],[5],[8],[-8],[-8],[-6],[3],[-3],[10],[-7],[6],[-8],[3]], dtype = "int8")#candidate|5719|(15, 1)|const|int8
bop_5720 = relay.less_equal(var_5718.astype('bool'), const_5719.astype('bool')) # shape=(15, 1)
func_4955_call = mod.get_global_var('func_4955')
func_4959_call = mutated_mod.get_global_var('func_4959')
var_5738 = relay.var("var_5738", dtype = "float64", shape = (468,))#candidate|5738|(468,)|var|float64
call_5737 = relay.TupleGetItem(func_4955_call(relay.reshape(var_5738.astype('float64'), [234, 2]), relay.reshape(var_5718.astype('int64'), []), ), 3)
call_5739 = relay.TupleGetItem(func_4959_call(relay.reshape(var_5738.astype('float64'), [234, 2]), relay.reshape(var_5718.astype('int64'), []), ), 3)
output = relay.Tuple([bop_5720,call_5737,var_5738,])
output2 = relay.Tuple([bop_5720,call_5739,var_5738,])
func_5749 = relay.Function([var_5718,var_5738,], output)
mod['func_5749'] = func_5749
mod = relay.transform.InferType()(mod)
mutated_mod['func_5749'] = func_5749
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5749_call = mutated_mod.get_global_var('func_5749')
var_5751 = relay.var("var_5751", dtype = "int8", shape = ())#candidate|5751|()|var|int8
var_5752 = relay.var("var_5752", dtype = "float64", shape = (468,))#candidate|5752|(468,)|var|float64
call_5750 = func_5749_call(var_5751,var_5752,)
output = call_5750
func_5753 = relay.Function([var_5751,var_5752,], output)
mutated_mod['func_5753'] = func_5753
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4689_call = mod.get_global_var('func_4689')
func_4691_call = mutated_mod.get_global_var('func_4691')
call_5758 = func_4689_call()
call_5759 = func_4689_call()
func_2282_call = mod.get_global_var('func_2282')
func_2283_call = mutated_mod.get_global_var('func_2283')
call_5760 = func_2282_call()
call_5761 = func_2282_call()
output = relay.Tuple([call_5758,call_5760,])
output2 = relay.Tuple([call_5759,call_5761,])
func_5763 = relay.Function([], output)
mod['func_5763'] = func_5763
mod = relay.transform.InferType()(mod)
output = func_5763()
func_5764 = relay.Function([], output)
mutated_mod['func_5764'] = func_5764
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5911 = relay.var("var_5911", dtype = "uint16", shape = ())#candidate|5911|()|var|uint16
var_5912 = relay.var("var_5912", dtype = "uint16", shape = (7, 6, 1))#candidate|5912|(7, 6, 1)|var|uint16
bop_5913 = relay.maximum(var_5911.astype('uint16'), var_5912.astype('uint16')) # shape=(7, 6, 1)
func_5311_call = mod.get_global_var('func_5311')
func_5315_call = mutated_mod.get_global_var('func_5315')
const_5922 = relay.const([6.316906,9.371614,-2.359254,9.980392,7.537358,0.711511,9.316764,1.718644,-8.027341,-6.389009,2.903302,-1.213029,-0.688887,-2.406877,-8.713283,-0.815679,2.812420,-6.998872,4.631913,2.809876,-4.910871,6.073074,7.105097,2.793920,-5.145659,-0.030519,6.887069,-4.715282,-2.648796,7.895943,-2.429055,3.254119,0.689506,-8.280217,0.509062,-2.802004,-6.150925,-1.483117,-7.314336,3.029215,7.414878,-9.515257,-6.871310,-3.222734,-1.034007,2.860136,-2.642198,-0.874450], dtype = "float32")#candidate|5922|(48,)|const|float32
call_5921 = relay.TupleGetItem(func_5311_call(relay.reshape(var_5911.astype('int64'), []), relay.reshape(const_5922.astype('float32'), [48,]), ), 2)
call_5923 = relay.TupleGetItem(func_5315_call(relay.reshape(var_5911.astype('int64'), []), relay.reshape(const_5922.astype('float32'), [48,]), ), 2)
output = relay.Tuple([bop_5913,call_5921,const_5922,])
output2 = relay.Tuple([bop_5913,call_5923,const_5922,])
func_5924 = relay.Function([var_5911,var_5912,], output)
mod['func_5924'] = func_5924
mod = relay.transform.InferType()(mod)
var_5925 = relay.var("var_5925", dtype = "uint16", shape = ())#candidate|5925|()|var|uint16
var_5926 = relay.var("var_5926", dtype = "uint16", shape = (7, 6, 1))#candidate|5926|(7, 6, 1)|var|uint16
output = func_5924(var_5925,var_5926,)
func_5927 = relay.Function([var_5925,var_5926,], output)
mutated_mod['func_5927'] = func_5927
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1859_call = mod.get_global_var('func_1859')
func_1861_call = mutated_mod.get_global_var('func_1861')
call_5929 = relay.TupleGetItem(func_1859_call(), 0)
call_5930 = relay.TupleGetItem(func_1861_call(), 0)
output = call_5929
output2 = call_5930
func_5951 = relay.Function([], output)
mod['func_5951'] = func_5951
mod = relay.transform.InferType()(mod)
output = func_5951()
func_5952 = relay.Function([], output)
mutated_mod['func_5952'] = func_5952
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2282_call = mod.get_global_var('func_2282')
func_2283_call = mutated_mod.get_global_var('func_2283')
call_5992 = func_2282_call()
call_5993 = func_2282_call()
func_2498_call = mod.get_global_var('func_2498')
func_2503_call = mutated_mod.get_global_var('func_2503')
const_6001 = relay.const([8,8,9,7,-2,-6,6,6,-2,4,-6,-8,-3,5,6,4,8,-8,-10,2,10,6,10,6,3,-7,-6,5,2,5,-7,-4,3,-1,6,4,-5,-10,2,-8,7,3,2,3,9,-4,8,-1,-9,-3,10,-1,-8,2,10,-5,5,10,-6,-3,-2,-3,-6,-3,-9,-2,-4,5,-5,-1,5,9,4,7,-2,-6,9,7,4,-10,8,3,4,-5,-3,3,-4,7,-4,9,5,4,-7,-9,3,-5], dtype = "int8")#candidate|6001|(96,)|const|int8
const_6002 = relay.const([3,5,2,4,-5,-2,8,7,3,5,7,-8,-4,-4,-4,-8,-6,-6,-9,8,9,-6,-3,6,-6,5,4,8,6,8,6,-8,-7,3,-5,1,8,-2,-10,-10,9,8,9,-1,9,-5,-5,7,7,1,-2,5,10,4,-6,-8,8,-6,3,9,9,7,7,10,-8,6,-5,-10,8,7,-6,7,-3,10,2,-10,-3,9,-2,6,1,-8,2,-3,3,4,-7,5,6,5,-3,1,1,10,10,-3,-7,-7,-2,9,10,-5,4,6,3,10,-6,6,2,3,9,2,9,-6,10,4,-9,-7,-1,7,-4,-4,7,-10,-3,2,8,-9,-3,-8,2,-3,3,8,-4,-9,-9,1,-2,-6,5,-8,-1,-10,4,9,9,9,-3,9,-9,6,-3,5,-9,10,-8,-6,7,-5,-5,-9,6,10,4,-7,-8,-10,-3,6,-5,-7,-7,5,-1,7,3,-2,-5,-8,-2,9,-1,10,-5,5,5,4,-5,5,9,3,9,1,-8,2,-8,-9,-1,1,7,5,-8,-3,-8,-8,-4,9,6,9,2,1,4,9,1,1,-7,-10,-5,-7,-5,2,-6,5,4,6,-7,6,-7,7,6,-5,-4,6,-10,-4,8,4,-6,7,-3,6,10,-3,8,4,-8,6,4,1,7,-8,-1,10,-1,9,-8,6,-10,4,9,-1,8,10,1,7,9,2,8,-1,-9,-5,-7,4,1,5,-7,-6,-6,-9,8,-7,-1,-8,3,10,-8,-10,7,4,3,10,6,4,-2,10,-1,8,-8,-3,-4,2,9,10,-7,5,-2,9,-1,-3,-8,-5,-2,10,-9,-10,7,8,-3,3,-1,-9,3,2,-2,1,9,-8,-10,8,3,-6,-9,6,1,3,8,-4,1,9,2,-3,5,-10,2,-6,-6,-5,7,1,3,-7,-6,-3,8,10,3,8,5,-5,-8,3,-5,10,-2,-9,5,-5,6,9,4,-1,3,5,9,-6,-4,10,-9,-3,-1,3,8,-6], dtype = "int8")#candidate|6002|(384,)|const|int8
call_6000 = relay.TupleGetItem(func_2498_call(relay.reshape(const_6001.astype('int8'), [6, 16, 1]), relay.reshape(const_6002.astype('int8'), [6, 16, 4]), relay.reshape(const_6002.astype('int8'), [6, 16, 4]), ), 1)
call_6003 = relay.TupleGetItem(func_2503_call(relay.reshape(const_6001.astype('int8'), [6, 16, 1]), relay.reshape(const_6002.astype('int8'), [6, 16, 4]), relay.reshape(const_6002.astype('int8'), [6, 16, 4]), ), 1)
func_3196_call = mod.get_global_var('func_3196')
func_3200_call = mutated_mod.get_global_var('func_3200')
var_6008 = relay.var("var_6008", dtype = "float32", shape = (112,))#candidate|6008|(112,)|var|float32
call_6007 = relay.TupleGetItem(func_3196_call(relay.reshape(var_6008.astype('float32'), [7, 1, 16]), relay.reshape(var_6008.astype('float64'), [7, 1, 16]), ), 0)
call_6009 = relay.TupleGetItem(func_3200_call(relay.reshape(var_6008.astype('float32'), [7, 1, 16]), relay.reshape(var_6008.astype('float64'), [7, 1, 16]), ), 0)
output = relay.Tuple([call_5992,call_6000,const_6001,const_6002,call_6007,var_6008,])
output2 = relay.Tuple([call_5993,call_6003,const_6001,const_6002,call_6009,var_6008,])
func_6019 = relay.Function([var_6008,], output)
mod['func_6019'] = func_6019
mod = relay.transform.InferType()(mod)
var_6020 = relay.var("var_6020", dtype = "float32", shape = (112,))#candidate|6020|(112,)|var|float32
output = func_6019(var_6020)
func_6021 = relay.Function([var_6020], output)
mutated_mod['func_6021'] = func_6021
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4910_call = mod.get_global_var('func_4910')
func_4912_call = mutated_mod.get_global_var('func_4912')
call_6037 = func_4910_call()
call_6038 = func_4910_call()
func_759_call = mod.get_global_var('func_759')
func_761_call = mutated_mod.get_global_var('func_761')
const_6056 = relay.const([7,3,1,-9,3,2,3,2,2,-1,7,-2,5,6,-4,-5,-4,10,-4,-2,1,10,-7,9,10,10,-3,-10,4,10,-9,-2,5,-6,-9,6,4,5,10,-1,-3,8,5,4,3,9,9,3,-5,5,-7,5,6,-3,5,7,-4,2,2,-1,10,-5,3,-6,-8,2,9,9,9,-10,-5,-2,1,-8,-2,7,1,2,1,10,-7,7,2,-1,-7,7,9,8,-5,-4,9,10,1,-2,10,-4,-6,4,4,-1], dtype = "uint32")#candidate|6056|(100,)|const|uint32
call_6055 = relay.TupleGetItem(func_759_call(relay.reshape(const_6056.astype('uint32'), [5, 4, 5])), 0)
call_6057 = relay.TupleGetItem(func_761_call(relay.reshape(const_6056.astype('uint32'), [5, 4, 5])), 0)
func_5379_call = mod.get_global_var('func_5379')
func_5380_call = mutated_mod.get_global_var('func_5380')
call_6059 = func_5379_call()
call_6060 = func_5379_call()
bop_6071 = relay.floor_divide(call_6037.astype('float32'), relay.reshape(call_6059.astype('float32'), relay.shape_of(call_6037))) # shape=(14, 1, 10)
bop_6074 = relay.floor_divide(call_6038.astype('float32'), relay.reshape(call_6060.astype('float32'), relay.shape_of(call_6038))) # shape=(14, 1, 10)
func_1801_call = mod.get_global_var('func_1801')
func_1803_call = mutated_mod.get_global_var('func_1803')
call_6094 = func_1801_call()
call_6095 = func_1801_call()
output = relay.Tuple([call_6055,const_6056,bop_6071,call_6094,])
output2 = relay.Tuple([call_6057,const_6056,bop_6074,call_6095,])
func_6123 = relay.Function([], output)
mod['func_6123'] = func_6123
mod = relay.transform.InferType()(mod)
mutated_mod['func_6123'] = func_6123
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6123_call = mutated_mod.get_global_var('func_6123')
call_6124 = func_6123_call()
output = call_6124
func_6125 = relay.Function([], output)
mutated_mod['func_6125'] = func_6125
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1748_call = mod.get_global_var('func_1748')
func_1750_call = mutated_mod.get_global_var('func_1750')
call_6151 = relay.TupleGetItem(func_1748_call(), 0)
call_6152 = relay.TupleGetItem(func_1750_call(), 0)
func_1748_call = mod.get_global_var('func_1748')
func_1750_call = mutated_mod.get_global_var('func_1750')
call_6167 = relay.TupleGetItem(func_1748_call(), 0)
call_6168 = relay.TupleGetItem(func_1750_call(), 0)
func_1801_call = mod.get_global_var('func_1801')
func_1803_call = mutated_mod.get_global_var('func_1803')
call_6174 = func_1801_call()
call_6175 = func_1801_call()
output = relay.Tuple([call_6151,call_6167,call_6174,])
output2 = relay.Tuple([call_6152,call_6168,call_6175,])
func_6200 = relay.Function([], output)
mod['func_6200'] = func_6200
mod = relay.transform.InferType()(mod)
output = func_6200()
func_6201 = relay.Function([], output)
mutated_mod['func_6201'] = func_6201
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4057_call = mod.get_global_var('func_4057')
func_4058_call = mutated_mod.get_global_var('func_4058')
call_6211 = relay.TupleGetItem(func_4057_call(), 1)
call_6212 = relay.TupleGetItem(func_4058_call(), 1)
func_5020_call = mod.get_global_var('func_5020')
func_5023_call = mutated_mod.get_global_var('func_5023')
var_6226 = relay.var("var_6226", dtype = "float32", shape = (192,))#candidate|6226|(192,)|var|float32
call_6225 = relay.TupleGetItem(func_5020_call(relay.reshape(var_6226.astype('float32'), [6, 4, 8])), 0)
call_6227 = relay.TupleGetItem(func_5023_call(relay.reshape(var_6226.astype('float32'), [6, 4, 8])), 0)
uop_6238 = relay.cosh(call_6225.astype('float32')) # shape=(6, 4, 8)
uop_6240 = relay.cosh(call_6227.astype('float32')) # shape=(6, 4, 8)
output = relay.Tuple([call_6211,var_6226,uop_6238,])
output2 = relay.Tuple([call_6212,var_6226,uop_6240,])
func_6258 = relay.Function([var_6226,], output)
mod['func_6258'] = func_6258
mod = relay.transform.InferType()(mod)
mutated_mod['func_6258'] = func_6258
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6259 = relay.var("var_6259", dtype = "float32", shape = (192,))#candidate|6259|(192,)|var|float32
func_6258_call = mutated_mod.get_global_var('func_6258')
call_6260 = func_6258_call(var_6259)
output = call_6260
func_6261 = relay.Function([var_6259], output)
mutated_mod['func_6261'] = func_6261
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4151_call = mod.get_global_var('func_4151')
func_4153_call = mutated_mod.get_global_var('func_4153')
call_6286 = relay.TupleGetItem(func_4151_call(), 0)
call_6287 = relay.TupleGetItem(func_4153_call(), 0)
var_6291 = relay.var("var_6291", dtype = "float32", shape = (14, 16, 10))#candidate|6291|(14, 16, 10)|var|float32
bop_6292 = relay.logical_and(call_6286.astype('bool'), var_6291.astype('bool')) # shape=(14, 16, 10)
bop_6295 = relay.logical_and(call_6287.astype('bool'), var_6291.astype('bool')) # shape=(14, 16, 10)
func_2145_call = mod.get_global_var('func_2145')
func_2146_call = mutated_mod.get_global_var('func_2146')
call_6296 = relay.TupleGetItem(func_2145_call(), 0)
call_6297 = relay.TupleGetItem(func_2146_call(), 0)
output = relay.Tuple([bop_6292,call_6296,])
output2 = relay.Tuple([bop_6295,call_6297,])
func_6303 = relay.Function([var_6291,], output)
mod['func_6303'] = func_6303
mod = relay.transform.InferType()(mod)
mutated_mod['func_6303'] = func_6303
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6304 = relay.var("var_6304", dtype = "float32", shape = (14, 16, 10))#candidate|6304|(14, 16, 10)|var|float32
func_6303_call = mutated_mod.get_global_var('func_6303')
call_6305 = func_6303_call(var_6304)
output = call_6305
func_6306 = relay.Function([var_6304], output)
mutated_mod['func_6306'] = func_6306
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5411_call = mod.get_global_var('func_5411')
func_5412_call = mutated_mod.get_global_var('func_5412')
call_6312 = func_5411_call()
call_6313 = func_5411_call()
func_386_call = mod.get_global_var('func_386')
func_389_call = mutated_mod.get_global_var('func_389')
const_6348 = relay.const([[5.607375,0.218344,-6.214940,-0.260266,-4.715767,9.488566,6.034180,7.700685,8.308146,7.364573,-3.913968,-8.176149,4.025239,7.103543,-7.882124,7.545725]], dtype = "float64")#candidate|6348|(1, 16)|const|float64
call_6347 = relay.TupleGetItem(func_386_call(relay.reshape(const_6348.astype('float64'), [1, 4, 4]), relay.reshape(call_6312.astype('int64'), []), ), 2)
call_6349 = relay.TupleGetItem(func_389_call(relay.reshape(const_6348.astype('float64'), [1, 4, 4]), relay.reshape(call_6312.astype('int64'), []), ), 2)
func_5951_call = mod.get_global_var('func_5951')
func_5952_call = mutated_mod.get_global_var('func_5952')
call_6350 = func_5951_call()
call_6351 = func_5951_call()
output = relay.Tuple([call_6312,call_6347,const_6348,call_6350,])
output2 = relay.Tuple([call_6313,call_6349,const_6348,call_6351,])
func_6352 = relay.Function([], output)
mod['func_6352'] = func_6352
mod = relay.transform.InferType()(mod)
output = func_6352()
func_6353 = relay.Function([], output)
mutated_mod['func_6353'] = func_6353
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1801_call = mod.get_global_var('func_1801')
func_1803_call = mutated_mod.get_global_var('func_1803')
call_6372 = func_1801_call()
call_6373 = func_1801_call()
func_4302_call = mod.get_global_var('func_4302')
func_4304_call = mutated_mod.get_global_var('func_4304')
const_6380 = relay.const([[1.493262],[2.108420],[3.399804],[-5.428031],[-4.855078],[0.273107],[-4.318488],[7.119862],[5.090625],[-5.703458],[4.571325],[8.707425],[-4.187750],[-7.617481],[4.339878],[0.538316],[-5.446571],[-8.999441],[1.134253],[7.460429],[0.828094],[3.146579],[-5.884495],[6.213610],[4.184646],[4.585957],[6.112362],[-7.024959],[-9.992260],[7.356101],[9.528667],[-9.513559],[4.384807],[-7.930476],[-0.508522],[1.734848],[-3.112638],[7.905431],[3.748617],[-4.936649],[1.342740],[-1.804885],[1.611598],[-3.198116],[7.279334],[8.554323],[-8.651846],[1.139666],[9.023093],[-0.006202],[8.232623],[0.549340],[4.625603],[1.479329],[6.087857],[8.218335],[3.002073],[-1.103056],[-1.424131],[-0.635915],[-6.043804],[-4.190159],[-7.265856],[-9.895705],[5.703450],[9.215744],[-9.924333],[9.223996],[7.954725],[1.677897],[-3.778914],[9.651982],[-7.436595],[-7.471468],[5.605576],[-5.668903],[7.314338],[-8.093953],[-9.695999],[7.789350],[-7.383730],[7.612704],[4.154048],[-7.258760],[8.368646],[-7.166904],[-5.994765],[6.432721],[7.778627],[6.053180],[1.757799],[-9.433263],[-7.929223],[-0.727361],[3.316291],[4.612714],[-7.020349],[7.818115],[8.881413],[-5.840337],[3.868461],[-6.571551],[6.117071],[-3.924142],[-8.283596],[0.606210],[5.116687],[-3.417069],[-8.488021],[5.164786],[-2.155110],[2.885797],[6.426509],[-6.930434],[-9.954284],[4.746067],[4.399506],[3.145912],[8.002827],[3.412669],[9.900826],[0.643163],[-6.217192],[0.665856],[-5.448758],[2.237589],[8.601708],[6.810509],[0.261094],[3.772656],[7.952504],[7.214406],[-7.268177],[5.634742],[-0.049677],[4.655665],[2.911707],[-5.385226],[-5.628294],[-6.685707],[-2.484647],[9.795317],[6.237080],[-7.586974],[6.681399],[-3.321646],[-5.660212],[1.644672],[4.363328],[5.841518],[-8.905409],[7.082865],[7.115090],[6.552664],[5.435300],[7.177878],[3.397706],[1.679882],[3.216734],[7.775861],[2.176786],[0.961258],[8.887600],[7.379396],[6.905627],[-2.635059],[9.047865],[2.081376],[-4.086933],[2.023644],[6.226552],[4.252979],[1.341631],[6.237211],[1.751386],[7.829373],[-9.497915],[-3.309343],[-0.042174],[-0.740714],[-8.369253],[4.549636],[5.410151],[4.158608],[8.787564],[7.034347],[9.463982],[-9.627332],[-1.397174],[0.553449],[-2.492002],[-1.875868],[-0.145466],[7.116273],[-6.617610],[-1.732731],[-7.600802],[4.587739],[6.441952],[2.455599],[6.035757],[8.558548],[-9.018709],[4.187284],[7.589948],[-3.250296],[-3.164332],[-4.461318],[8.402068],[2.218940],[-7.290618],[6.999697],[1.626093],[-2.305444],[4.474753],[4.653781],[-4.273344],[7.744448],[-9.373950],[2.984127],[0.710068],[-1.172541],[4.976512],[-2.778720],[-3.639853],[-4.761335],[-5.653213],[7.228408],[-2.251656],[-6.202150],[-3.599506],[-8.610623],[-2.716347],[8.947436],[2.442260],[-2.762854],[-6.865333],[-0.067166],[9.263608],[-9.528321],[-9.065116],[-0.941524],[-8.387985],[-5.007287],[1.990159],[-6.428610],[-7.446977],[6.658565],[-9.385006],[-1.654127],[2.800833],[2.250355],[4.103518],[9.591222],[-5.756729],[-0.373706],[8.310113],[7.122762],[-5.675819],[-8.398517],[-3.225087],[0.759833],[-1.652559],[1.803083],[1.401585],[-3.519662],[-9.290452],[-0.733128],[5.656907],[0.647852],[-7.643080],[-5.330986],[-0.044825],[4.991119],[1.588380],[9.867011],[4.926745],[-1.013372],[9.305672],[-0.967034]], dtype = "float64")#candidate|6380|(280, 1)|const|float64
call_6379 = relay.TupleGetItem(func_4302_call(relay.reshape(const_6380.astype('float64'), [1, 280])), 3)
call_6381 = relay.TupleGetItem(func_4304_call(relay.reshape(const_6380.astype('float64'), [1, 280])), 3)
func_903_call = mod.get_global_var('func_903')
func_905_call = mutated_mod.get_global_var('func_905')
var_6384 = relay.var("var_6384", dtype = "float32", shape = (2, 480))#candidate|6384|(2, 480)|var|float32
call_6383 = relay.TupleGetItem(func_903_call(relay.reshape(var_6384.astype('float32'), [6, 16, 10])), 2)
call_6385 = relay.TupleGetItem(func_905_call(relay.reshape(var_6384.astype('float32'), [6, 16, 10])), 2)
output = relay.Tuple([call_6372,call_6379,const_6380,call_6383,var_6384,])
output2 = relay.Tuple([call_6373,call_6381,const_6380,call_6385,var_6384,])
func_6386 = relay.Function([var_6384,], output)
mod['func_6386'] = func_6386
mod = relay.transform.InferType()(mod)
var_6387 = relay.var("var_6387", dtype = "float32", shape = (2, 480))#candidate|6387|(2, 480)|var|float32
output = func_6386(var_6387)
func_6388 = relay.Function([var_6387], output)
mutated_mod['func_6388'] = func_6388
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6414 = relay.var("var_6414", dtype = "float32", shape = (15, 12, 14))#candidate|6414|(15, 12, 14)|var|float32
uop_6415 = relay.atan(var_6414.astype('float32')) # shape=(15, 12, 14)
func_6123_call = mod.get_global_var('func_6123')
func_6125_call = mutated_mod.get_global_var('func_6125')
call_6417 = relay.TupleGetItem(func_6123_call(), 2)
call_6418 = relay.TupleGetItem(func_6125_call(), 2)
func_5379_call = mod.get_global_var('func_5379')
func_5380_call = mutated_mod.get_global_var('func_5380')
call_6431 = func_5379_call()
call_6432 = func_5379_call()
func_6386_call = mod.get_global_var('func_6386')
func_6388_call = mutated_mod.get_global_var('func_6388')
const_6437 = relay.const([[7.984240,1.061349,2.749691,4.989913],[-9.027467,-5.092088,0.906551,-3.811494],[2.266328,1.320664,5.163815,9.627034],[-5.071818,0.169967,8.100091,-5.862860],[-4.540592,1.158150,-2.355106,-7.825237],[1.564250,-6.226919,7.529486,6.097291],[1.465604,7.737835,-7.844237,9.371944],[3.610335,8.468711,-4.407061,5.185747],[-6.224778,-0.824056,-0.021445,1.745572],[-3.820665,-4.079106,-7.291043,-6.022861],[2.902360,1.765364,-7.355436,-0.386903],[8.324768,5.684624,2.172432,-3.496444],[5.636698,-5.499890,-8.659858,-1.936140],[8.656525,-7.509474,-1.536575,-0.971446],[-5.423328,4.262799,-6.769291,-2.928402],[-5.184439,-8.042622,1.083105,5.153106],[5.279965,-4.717469,7.502805,-2.693978],[2.417191,5.668466,-0.145548,2.649300],[7.180310,7.951946,7.918262,2.295189],[9.971746,9.708106,8.469473,-7.428456],[4.324619,-8.080519,0.688195,1.509265],[5.719443,-3.230430,-6.673213,2.489670],[-8.234355,-1.228428,-6.334601,7.252637],[6.174309,-6.163100,5.049321,6.240148],[3.440932,-6.223922,4.855705,-8.655029],[-7.596446,-4.402960,-0.056970,-4.388852],[-9.881882,-3.708548,-1.337327,6.876613],[2.244508,-9.643166,-1.763472,4.957250],[9.917681,-5.346135,7.177207,-0.006936],[8.384487,9.690162,-1.660824,-4.429865],[-2.322944,9.688706,1.566982,-9.000834],[5.506931,7.987086,-2.811027,2.314156],[-2.821908,-7.264580,-6.752029,6.157304],[4.174649,-0.510252,-9.035074,7.229735],[5.375043,-7.956375,2.611764,7.034638],[2.443596,-1.608205,3.207590,-5.167659],[1.805009,-8.921169,6.479123,3.350905],[-0.304990,-2.758988,-4.086775,9.534618],[-6.480707,-3.576026,-5.503969,-8.845479],[2.116033,0.089122,6.958832,-7.631474],[6.136562,-1.732280,6.430315,0.997622],[2.504649,-1.322556,8.333424,-3.853343],[5.372302,0.094746,-1.443919,-1.195444],[-7.883409,8.681629,5.407562,-8.929824],[-7.322149,1.854251,-1.811672,4.430655],[-6.767473,-0.470539,6.071972,9.076425],[3.429876,-5.406957,5.941151,2.182788],[-7.037873,7.865807,4.612028,-9.521555],[-0.373916,2.648278,0.478078,9.153430],[-0.581681,3.643371,-7.233925,6.841761],[-2.853477,3.972372,-0.654979,6.392933],[2.099501,-2.594215,0.806381,-8.965399],[-1.758455,-6.719924,-4.883559,0.820301],[5.205234,-2.300550,4.301477,-3.495773],[9.047142,4.164276,-7.165131,3.226149],[8.164035,-0.127302,-9.855335,7.689980],[-2.852163,-5.412597,9.471273,-6.812275],[1.434016,-8.669757,-8.883910,-8.694638],[-6.461914,5.615523,-6.244447,8.199540],[-8.616827,-9.448744,-3.687657,9.298507],[-0.650028,-1.198938,0.311210,-9.725575],[7.512490,0.817958,4.659081,-0.327976],[-9.424132,0.494648,-7.008259,-5.458132],[-6.493313,7.455337,-3.628793,-5.107726],[3.221410,-2.115293,9.913707,0.505017],[4.290373,-7.688975,-6.100816,7.074037],[-4.233120,5.897678,8.089695,1.028054],[1.114029,-7.385454,1.104499,-8.748954],[5.130291,6.718405,9.100029,-9.848102],[9.621003,-9.963665,7.689218,-7.253811],[-2.099803,-3.098588,-1.427644,9.583958],[-0.652380,3.179506,-4.692330,-9.911246],[4.126058,-6.876694,-7.824680,5.848626],[9.480548,5.765347,9.183252,-0.050292],[-2.869247,5.792839,-9.794554,-1.907109],[5.744363,-2.093954,8.507251,0.126904],[-8.752954,9.433374,-1.940049,6.073072],[-0.150583,-6.614496,-5.696871,5.015140],[6.268138,6.356903,-3.073005,6.664494],[-1.130860,5.481501,-1.787525,-0.186807],[0.165046,-1.820012,-6.547652,5.238291],[-8.610984,2.757258,2.540804,9.489285],[4.434861,-4.690085,-4.113378,8.065005],[-4.836389,-9.052368,-8.467937,7.769913],[3.296070,4.079148,6.387496,-3.293459],[3.594210,9.986476,5.288029,1.630147],[1.866497,-4.872265,0.861008,-2.465429],[-5.113029,7.079576,5.649058,-5.459645],[-3.005954,5.192103,3.908509,2.605707],[7.215922,4.060600,-2.327037,9.834783],[-2.252784,2.086266,-4.006910,3.348365],[9.535192,6.017008,-1.381246,7.919749],[6.032138,-6.413850,-6.473002,0.834969],[-5.229615,-3.084317,-3.857083,8.087705],[9.551794,-2.519040,-0.819484,3.405467],[-1.246988,6.805539,-6.427706,3.887028],[1.192393,-2.495539,-6.267638,6.074889],[-9.281565,2.164843,3.242882,-0.494240],[9.302530,-7.763427,-0.405573,6.574826],[-2.694739,9.293113,7.069517,5.708495],[9.521454,5.819185,1.760595,-9.473823],[-2.817583,-6.992399,-2.895269,4.171965],[-8.784745,-9.869280,0.913679,4.478535],[-1.854912,-0.148325,-2.621313,-3.934790],[-9.175484,0.640681,-6.710600,7.429698],[0.777968,-4.401033,-3.406299,7.252054],[-2.854653,-5.343022,-2.816647,5.335742],[-7.771240,-4.584537,9.698436,-6.457665],[-6.108774,-7.969272,-0.940180,-3.926899],[9.091178,1.419177,-8.944461,-1.765016],[-2.782435,-5.803889,8.472643,7.976425],[3.981372,-3.892313,-0.918920,-1.162516],[-7.103975,9.378905,2.638332,-6.909248],[8.688610,-5.234668,-5.797011,-2.850604],[9.636320,1.268156,-0.887932,6.633527],[5.778256,3.116087,-8.838814,-8.791692],[-8.388853,3.815287,6.743600,-7.835175],[-0.817685,-0.192734,-2.739166,6.184726],[5.345031,-6.159018,-3.373357,-8.479305],[3.436178,3.442024,3.323039,-3.760095],[-3.823874,4.684027,8.225287,-1.862699],[6.838684,-6.833233,6.093202,3.384384],[8.314795,-5.661405,9.503686,2.180989],[-4.903141,4.875132,-1.391597,6.951104],[2.170668,0.065320,2.250454,-6.520550],[-1.748134,-6.178225,7.117206,9.376078],[0.382197,-6.038208,-7.484538,8.659422],[-3.188975,-0.945006,-0.799979,2.346093],[4.452896,-1.237322,-1.784689,1.127442],[5.118335,-4.230020,2.066096,8.993106],[-5.495496,-8.307243,4.698389,1.411335],[-9.868575,4.416874,-8.772887,-4.307877],[4.788537,-8.338218,-0.757659,-1.615696],[9.057650,-6.365929,-6.312049,1.385460],[2.486780,6.603069,4.171696,-7.079160],[7.456346,-4.295412,8.781762,5.808603],[0.390845,-2.043717,3.107386,6.560489],[-0.473009,0.077649,-6.638744,5.199926],[-7.891578,-2.116335,4.531792,0.925296],[-3.557776,-1.580291,3.639125,-0.487247],[7.867624,-1.020662,-5.774501,3.232347],[5.190473,1.966548,8.306063,9.433118],[-5.331898,8.383276,-8.852002,-2.623939],[-9.098170,-7.294458,-5.925576,-9.344667],[-9.798932,-9.033472,2.513207,3.464350],[-8.648582,-0.183913,9.558559,-6.261962],[0.046616,4.502201,-0.893244,5.997080],[4.664445,-0.944249,-9.893364,7.256142],[2.234659,3.072482,-6.303398,6.702521],[-9.915028,-5.941024,8.357290,9.927448],[8.617312,6.822186,-2.999226,-3.336536],[-1.462241,5.990905,-0.770391,8.295616],[-8.835441,-3.251590,6.111322,3.055627],[4.375656,3.443042,-8.720026,6.705813],[-5.521726,-1.378154,8.341321,-1.579719],[6.222415,0.699759,-8.494583,-7.201519],[9.780257,1.415765,-2.984587,-8.143001],[2.045722,3.656415,-2.569379,9.693736],[6.959931,6.426575,-7.688992,-3.515758],[7.786855,8.712899,5.596925,-9.726819],[-1.801424,1.273880,2.664776,-5.862972],[-4.793115,-0.885626,4.623241,4.510724],[7.603392,5.243722,-0.936686,-8.969377],[5.479744,6.204566,7.896431,-3.050353],[-9.749080,-3.103819,2.580481,-7.124998],[-7.599840,0.150475,-8.713494,-0.540959],[3.369051,8.425379,-7.049915,-3.906612],[-2.247585,-2.888174,0.112954,9.275237],[-9.756344,0.424642,6.915942,8.683037],[9.764649,5.520330,5.741691,6.610267],[3.112551,-4.819753,-9.140859,-5.513517],[7.617799,-4.503047,9.975636,-0.098494],[-9.418521,5.350818,0.943337,1.955979],[5.882487,-9.587272,8.713315,-7.221688],[-6.792605,-9.544393,2.628350,8.314001],[5.750725,9.064320,-4.578295,-7.837888],[-8.982366,-6.117980,1.459597,-2.068571],[-8.151600,7.294171,-1.328118,-3.209270],[9.105887,-2.904534,0.337056,0.982284],[8.894505,8.669454,-5.695341,-0.855856],[-0.158755,-5.509780,5.317265,-6.719554],[1.615071,5.627405,5.233169,-4.923660],[-8.672334,1.335207,7.967117,-1.215375],[-0.287909,-3.785551,1.273411,6.983082],[6.280761,3.482273,-1.414478,-0.383834],[-0.935889,1.588337,9.672220,-1.553020],[-7.454846,-3.379158,-6.347978,0.729498],[-8.036084,2.579963,-1.162836,3.747409],[-6.593859,-7.607392,3.646736,-0.636314],[-7.963282,4.579055,2.793024,8.859789],[-3.150549,6.065550,-5.433166,3.406992],[-3.455936,1.734447,1.547244,-6.157660],[3.442953,-1.530956,9.448338,-8.921506],[-9.953274,-6.428332,6.973834,-0.385025],[0.463619,-7.106854,-5.912468,-7.917965],[-8.438350,1.359578,9.460690,2.950059],[3.634151,3.041733,-9.374490,-9.319397],[5.855043,3.333788,9.566590,-4.891901],[0.281315,-9.022419,-8.136495,6.237771],[-2.229366,-1.525680,-1.196456,6.428853],[1.801259,3.243132,-5.797977,4.398680],[-6.350391,9.219981,-9.060391,-2.541420],[-6.114446,9.655349,5.871835,-8.899833],[3.894254,0.259843,-6.312492,7.942932],[0.660721,-0.168136,0.622335,-5.758105],[-3.516000,7.947320,3.821685,-5.976639],[-8.763397,9.848380,-7.026737,-9.328234],[-0.541744,-5.891589,-1.276487,6.411689],[-1.421953,9.918475,4.405652,1.013987],[1.777471,-1.019231,-0.418956,4.826016],[-8.953516,-2.668596,-6.899607,-3.067313],[5.305910,4.419681,5.366741,1.757611],[-5.459145,9.426429,-4.435725,9.372203],[9.999788,0.599517,0.368168,-1.646240],[5.680088,-7.026809,6.093306,-4.041243],[0.176470,-0.438820,-4.938157,-4.871589],[6.010339,-9.482146,-0.878194,6.273005],[6.850014,1.442124,2.081648,-6.567134],[9.508221,-1.402405,-2.247051,4.073781],[8.804058,-5.745350,6.474537,-8.651471],[-5.730947,2.486418,6.845362,-5.483904],[2.359153,0.910149,6.198334,1.817499],[-1.911039,-3.877328,-9.250606,7.478963],[4.309085,-5.737501,-7.723825,4.170288],[2.687735,-2.031914,-7.436706,-9.246612],[-8.683286,-6.097970,6.963801,-3.836014],[-5.770993,-7.557197,-9.995718,-9.548794],[9.251433,8.997527,0.543962,-3.986868],[8.174567,4.588694,8.305734,3.642249],[4.119606,-9.533823,1.268707,9.767138],[6.329864,-5.755286,0.013927,2.528866],[0.687999,-0.556873,-4.248365,-9.906636],[0.221033,8.045180,3.959961,4.650039],[-2.465521,2.671384,-5.959674,5.890501],[8.884029,-1.152163,-3.000445,4.017846],[-8.021154,3.491261,4.388726,-5.196797],[8.396657,4.253628,-7.989550,-9.905071],[-4.569302,-6.349799,-5.029677,-6.360541],[0.907032,-9.346594,4.321095,-5.915821],[5.987403,-7.099456,5.675080,-2.515654]], dtype = "float32")#candidate|6437|(240, 4)|const|float32
call_6436 = relay.TupleGetItem(func_6386_call(relay.reshape(const_6437.astype('float32'), [2, 480])), 3)
call_6438 = relay.TupleGetItem(func_6388_call(relay.reshape(const_6437.astype('float32'), [2, 480])), 3)
func_3533_call = mod.get_global_var('func_3533')
func_3534_call = mutated_mod.get_global_var('func_3534')
call_6440 = relay.TupleGetItem(func_3533_call(), 0)
call_6441 = relay.TupleGetItem(func_3534_call(), 0)
output = relay.Tuple([uop_6415,call_6417,call_6431,call_6436,const_6437,call_6440,])
output2 = relay.Tuple([uop_6415,call_6418,call_6432,call_6438,const_6437,call_6441,])
func_6449 = relay.Function([var_6414,], output)
mod['func_6449'] = func_6449
mod = relay.transform.InferType()(mod)
mutated_mod['func_6449'] = func_6449
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6450 = relay.var("var_6450", dtype = "float32", shape = (15, 12, 14))#candidate|6450|(15, 12, 14)|var|float32
func_6449_call = mutated_mod.get_global_var('func_6449')
call_6451 = func_6449_call(var_6450)
output = call_6451
func_6452 = relay.Function([var_6450], output)
mutated_mod['func_6452'] = func_6452
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1859_call = mod.get_global_var('func_1859')
func_1861_call = mutated_mod.get_global_var('func_1861')
call_6486 = relay.TupleGetItem(func_1859_call(), 0)
call_6487 = relay.TupleGetItem(func_1861_call(), 0)
output = relay.Tuple([call_6486,])
output2 = relay.Tuple([call_6487,])
func_6494 = relay.Function([], output)
mod['func_6494'] = func_6494
mod = relay.transform.InferType()(mod)
output = func_6494()
func_6495 = relay.Function([], output)
mutated_mod['func_6495'] = func_6495
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1674_call = mod.get_global_var('func_1674')
func_1675_call = mutated_mod.get_global_var('func_1675')
call_6496 = relay.TupleGetItem(func_1674_call(), 2)
call_6497 = relay.TupleGetItem(func_1675_call(), 2)
output = relay.Tuple([call_6496,])
output2 = relay.Tuple([call_6497,])
func_6503 = relay.Function([], output)
mod['func_6503'] = func_6503
mod = relay.transform.InferType()(mod)
output = func_6503()
func_6504 = relay.Function([], output)
mutated_mod['func_6504'] = func_6504
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2863_call = mod.get_global_var('func_2863')
func_2865_call = mutated_mod.get_global_var('func_2865')
call_6608 = relay.TupleGetItem(func_2863_call(), 0)
call_6609 = relay.TupleGetItem(func_2865_call(), 0)
func_1449_call = mod.get_global_var('func_1449')
func_1453_call = mutated_mod.get_global_var('func_1453')
const_6614 = relay.const([7.103874,6.859364,1.705551,0.897507,7.241648,-3.858624,9.902909,-3.544833,8.888963,-3.093896,8.449316,-6.337938,-4.046544,-1.559974,-5.405400,2.951226,2.092118,-1.739225,2.826304,-3.308755,2.493682,9.502354,-5.348854,1.733026,-9.612388,6.120041,2.084839,9.890701,-3.728025,5.178470,4.164055,-2.805585,3.588649,8.178081,-9.054176,-5.619488,-7.997890,5.088205,6.299421,-4.982198,-3.367781,5.754308,6.440792,-4.113271,6.854506,1.823029,-3.549294,1.950885,-3.298233,-8.794248,8.582949,-7.058773,-0.567160,-3.384637,-2.421266,6.267470,-6.118767,-9.976543,6.575439,5.519107,-7.426780,5.119529,0.496853,7.048263,5.633391,-1.513637,-3.635862,-0.985831,-0.668941,-0.522719,2.289545,-1.651464,-2.118699,-3.641026,6.414076,-3.082128,-6.568541,-8.466999,8.372051,7.135782,4.046064,3.320767,8.939090,-4.394959,-0.811170,-5.831026,-9.884671,9.257828,-3.214227,5.121908,0.659575,2.663175,7.808141,0.449560,3.749700,-0.962208,2.387344,-6.054839,6.033619,-9.524668,3.211047,-7.501577,7.279956,7.322582,1.809404,5.935032,-2.526792,-5.411061,-2.014419,-5.770280,-9.330533,-7.734245,-4.510454,-9.393595,7.177638,7.440904,-8.633969,5.018270,5.181178,3.682122,3.755374,-2.204763,6.049963,4.770563,-5.151605,-9.222474,-1.193018,-8.285078,1.171403,3.888423,-4.357497,-8.029436,-7.842943,-2.502481,-8.344790,-1.277658,8.190203,8.572663,8.699699,-8.053015,5.482556,-5.693040,-0.410913,-1.961781,-4.429856,-1.903185,3.571821,5.687865,-7.562772,6.801032,2.903936,-7.557182,-1.312338,8.338368,2.276662,-8.109729,-4.842589,-9.707214,4.330737,7.411016,-4.564791,-7.352290,-4.014210,6.891532,-3.732806,3.708999,-0.875316,-7.670346,1.864137,-0.318385,0.379940,3.863421,-4.698826,-2.828623,4.704918,5.624167,-6.830558,9.785245,2.858950,2.616742,9.177222,8.765212,5.497951,4.349763,0.166066,6.851325,-3.498001,8.761137,-8.697083,-7.747464,7.735724,-1.730631,-1.736920,-7.300883,-3.042822,9.349081,-8.613756,-8.350704,-4.346613,-4.576515,2.988697,-7.810228,1.262968,-8.456721,-0.281825,1.769664,-4.349107,1.918549,0.737597,-6.450919,0.574690,8.737587,-1.122486,8.061517,0.594617,8.841524,7.989670,-6.597843,5.502016,5.091016,-0.153742,2.870251,-8.827911,6.206039,-8.391190,2.797115,4.033119,0.180161,-1.466116,-0.245951,-3.474625,9.049872,9.015757,-5.900921,-8.811404,-8.998189,-0.868123,-8.191058,-6.570918,-6.683791,1.319125,9.364450,2.128856,2.299823,7.136274,4.645197,2.761317,-4.457865,5.255034,6.407770,-4.550372,-4.794682,6.304972,1.838778,-4.272655,-9.729172,6.889723,-3.317459,-6.677217,9.066669,8.539692,0.719486,8.652782,0.744414,7.223626,-6.780541,9.763564,-3.549422,4.182542,-8.476183,-4.076340,-5.084389,-6.517631,-5.390014,-1.815545,7.367586,-6.359397,-8.488414,-1.161238,-2.704796,-2.453038,5.285989,0.350448,-9.988390,6.072014,-7.194225,4.595913,6.954106,0.473558,-0.486798,5.835362,4.212858,-7.770414,0.566019,-6.916541,-6.109166,4.864382,-2.666757,-3.092236,1.620269,7.250668,2.406043,-6.820197,3.587967,-1.162053,3.080197,7.444806,4.512047,-2.000850,-1.261986,3.828769,4.149578,-8.295148,9.446208,-8.475407,-3.611288,2.533212,-4.240358,-7.079459,5.020356,0.012785,6.740533,-8.463632,4.759003,5.293332,8.834987,-7.760617,0.322615,-1.453463,3.433459,-3.235560,-7.114516,5.639332,4.367639,-9.756248,-2.167694,-0.203378,-8.703250,1.464464,5.292781,1.805481,8.000792,-5.240025,-9.178147,8.974882,5.425292,8.335403,5.125770,8.839309,9.384611,-4.352030,2.815837,1.035368,4.097986,8.213663,8.852588,7.722877,6.657825,-8.819695,-6.571833,5.241112,4.397155,1.177840,-1.431314,9.193158,5.579003,8.895914,-9.015498,-8.546707,6.365691,7.979411,9.372347,5.884686,-4.226965,-6.977040,-6.510903,-3.494496,4.425928,-8.044061,-8.516233,0.101285,1.889650,8.985402,7.693022,3.289431,9.639030,1.123251,3.227890,5.738419,-5.229755,-8.298349,-5.810952,-7.061856,7.927487,6.254245,7.819056,3.934512,6.508265,-8.537142,-5.818879,-6.776020,-7.894745,-6.511673,-8.962835,3.157062,-4.245784,8.174007,0.264550,-8.168119,3.059470,-4.532560,-4.621126,3.891106,-8.943537,-1.464663,-5.598433,6.403999,-2.767658,-3.652707,7.161640,-7.348065,-6.564874,-6.544930,1.901424,-8.180334,-0.657209,1.712586,-7.948886,1.423506,5.922229,8.932329,-3.359401,-2.134562,5.373653,9.681946,4.302760,-2.521182,-0.919412,0.316102,5.467488,-4.437445,-6.036026,-3.006507,-7.546040,-2.566115,2.728375,6.679870,-7.531493,-6.591662,7.075876,-4.787245,7.411402,-3.136010,-1.514233,-0.232314,8.210644,5.428155,-0.872411,-6.471905,6.353567,-9.931714,-2.306314,-5.204694,-6.009224,-2.592469,9.206964,-2.849678,2.330107,-2.342615,-0.728426,8.327646,2.492624,6.749884,-3.160035,-8.497501,-4.091671,-7.388985,4.245714,4.138279,-0.587014,2.724876,9.826437,-1.684465,-6.413871,-9.853850,3.434296,-6.745041,-6.405459,8.090651,4.957583,4.774571,-5.207546,-8.180213,-4.248562,8.696866,-4.939881,-6.206127,-2.042044,-1.556925,9.348525,8.468078,4.168525,1.322710,-1.853378,-4.404886,2.387932,8.556625,-3.437061,6.468276,-2.477299,0.164856,2.843424,-0.690603,-4.833916,-2.169749,7.785384,6.083134,7.510323,-5.753543,2.934753,0.687236,-7.997294,-0.981651,-2.655044,-1.864240,5.059101,0.553416,3.277155,-1.735206,5.325651,-1.537808,4.362422,3.821022,-1.118043,-9.475927,-4.604601,-7.651756,-6.193483,9.778689,-7.497511,2.323948,3.291078,-7.669348,-0.907556,9.910630,5.733437,-8.170025,2.270282,0.781079,-3.932427,4.542858,4.734408,6.824142,-4.745638,1.291044,-2.360049,-9.531928,9.309240,1.211189,-6.762927,7.331160,-4.118784,-8.654326,3.164915,7.619721,0.083446,9.584495,7.146280,-5.906733,8.484761,-5.747824,6.615263,-6.272356,-9.033057,-5.300411,-7.630269,-6.970436,-0.451458,-6.798858,1.629996,2.764489,-9.013213,4.230460,3.909313,4.767022,9.886178,1.300006,0.453536,-4.662288,5.121646,-8.577547,-2.073942,-1.890122,1.946734,7.381723,-3.298488,0.559117,6.810723,-4.342416,-4.133083,5.995044,-2.526617,-8.526790,-4.059163,4.655995,-8.367396,2.675908,-5.987954,7.632915,-7.799060,-3.536502,5.126514,0.126351,4.589014,5.439781,-8.918322,4.201299,4.018364,-6.860832,-3.339416,9.547824,2.172351,-6.563249,-1.805132,9.692085,-4.830980,-3.916451,3.427025,-2.135619,1.601296,-3.801093,-3.301769,-7.931944,-5.147231,-5.885730,-6.306109,4.317887,-5.104680,-3.175635,9.054827,-1.569646,0.333352,6.426732,-6.992753,6.055980,6.689174,5.553499,-1.675238,-0.151845,-1.316434,6.104042,-5.207445,-4.046080,-7.898334,-3.029565,-5.899631,6.604080,1.658634,-3.195930,-2.554536,4.460229,-1.693538,-0.572794,2.775108,9.932816,7.822341,-3.084756,8.453967,-1.612973,8.528749,1.550510,2.671077,-2.581160,4.376691,0.213831,-4.223483,9.271582,6.628683,0.772482,-8.648107,5.007512,-8.780743,-0.827046,-9.683607,8.668711,1.208486,-3.978082,-4.107521,7.717295,9.271415,3.810548,7.729567,-7.812483,-2.405380,1.395864,-5.281027,-4.428465,5.851791,-6.853657,-1.441405,9.685619,-4.141502,-4.533411,-3.581718,-8.615390,-2.742295,-5.870576,2.772324,4.930971,-1.931900,-3.224360,5.601803,6.893911,9.000254,-5.846387,-6.396823,6.626662,2.176007,4.079635,2.065288,-8.956541,6.049351,-8.592006,7.137590,7.537595,-6.446431,8.184307,-4.963572,-8.416870,-2.416830,6.645743,0.766884,-6.424629,3.134903,-8.462409,8.181799,-3.041946,2.418820,4.484764,-2.275902,4.203376,2.379907,-2.029633,5.938020,8.055872,-2.059738,-6.853614,-8.301010,-0.454218,-9.737323,-8.978396,4.290852,9.645974,1.056320,-1.259516,5.023601,6.045536,-0.269158,-2.980636,-1.887922,5.340264,9.457840,-1.835817,-8.205830,9.436449,-3.944178,7.909161,-0.753555,-7.290674,4.944925,-9.171587,-1.356133,9.210650,1.752257,3.766278,-1.603829,-1.106435,-7.674463,7.214554,-7.659410,-3.186129,-9.905240,-2.078619,-5.207878,5.239296,9.055154,-1.431351,2.132957,-7.395521,9.749971,-3.902486,4.159545,5.595418,-8.488587,-6.870684,1.479997,4.146346,-5.872275,5.950614,-0.213849,3.769166,-5.189251,-6.918847,3.568552,-2.418269,-7.970399,-6.229778,-5.465812,2.421096,-9.035357,0.734490,-7.853229,-1.092529,-7.145629,6.180543,-0.316270,9.604698,-6.758309,-8.216333,-1.112283,7.856089,4.065962,-2.286042,3.625923,-3.070738,-5.700405,-5.879836,-5.611023,0.533248,-3.601774,-8.135123,4.903657,1.580169,8.935338,-9.526777,-8.271093,-0.323481,9.178886,1.543084,-0.273765,4.239943,4.016178,-2.625739,-8.781130,8.662212,-5.603046,6.911832,7.156612,-9.679565,-5.725383,-5.952557,-3.627571,-1.098770,-2.402320,-0.001943,-4.570521,2.339268,6.045470,0.106151,0.672347,-7.092911,-1.991825,-6.947490,-7.669980,-4.911028,3.306316,-6.233441,5.897006,6.090093,-7.367689,3.810035,6.298399,6.303695,-6.104530,-6.461344,7.661887,6.040124,-2.499476,8.032227,-1.409643,5.240746,-5.526275,2.759293,8.218785,6.227554,5.830409,-3.871725,7.481929,6.158066,-1.117248,-2.538709,1.894728,-6.470034,6.261886,-6.040305,3.507043,5.170118,0.654283,-6.696197,0.990186,4.186497,-4.296916,-0.854293,0.700597,4.274557,8.210415,0.753275,3.177234,0.021667,7.879783,7.885325,1.373618,-9.816511,7.241307,4.047706,3.471199,2.074878,-0.062304,5.025876,-9.541256,-2.772482,-2.680846,-5.014264,8.407331,-6.360727,1.872515,2.011817,-7.663626,-4.873399,-9.888852,1.762473,-2.685303,1.235568,-8.054440,-1.143803,6.972201,-6.911632,-5.284893,-5.906930,-7.305426,-7.234189,-9.943897,9.507307,7.150207,-1.577260,8.027128,2.538681,2.464869,3.607549,-2.797761,-2.436044,-4.803872,8.309404,9.954122,-7.279893,9.022038,9.663510,-5.444465,-2.187795,-9.949050,-6.041876,-1.294644,6.702307,-3.641854,3.313870,-8.478859,0.220383,8.707019,9.677319,-4.437152,-5.715593,-0.169019,9.128850,-5.216463,3.802931,-0.628070,2.352563,1.855983,-0.938876,7.672708,-0.392294,5.428460,-6.871163,1.111338,8.978534,6.587016,9.374951,-3.412302,-2.307327,-3.945390,8.917383,7.424168,-8.741325,-5.838958,0.934827,-2.436982,7.563696,4.962708,-6.382873,-0.801625,-1.286675,-3.730264,4.122833,-4.369802,6.679992,3.115569,0.085756,6.173059,-0.816440,5.008415,0.425566,3.879629,4.535475,-4.374079,6.763875,-3.696215,-7.965338,5.917968,7.809525,-6.947692,7.789800,9.082818,-3.432505,-5.741239,-2.181819,-5.114427,1.576393,9.304392,-6.856231,8.949956,-4.977929,3.493494,-2.690432,-6.196183,-7.661531,-5.547396,9.798844,2.971308,4.832364,-4.441382,3.473347,5.194890,-4.605251,4.511744,6.799393,4.798266,-7.350840,-9.325067,2.270768,-5.633705,2.577746,1.365095,5.656251,5.212632,-8.911775,-3.311929,-5.192592,1.329457,-6.735367,-9.418495,0.545785,7.816902,-8.465399,-5.166034,0.374191,-4.334255,8.700781,2.324076,-4.475003,6.899715,-2.080766,-6.933767,-1.392994,4.109082,-7.839025,-0.105694,2.259779,-2.822643,0.451623,-1.639450,1.996359,-3.223478,-8.006270,9.631212,-1.453652,-5.671307,3.578475,0.432023,-6.495150,-8.225045,-6.010564,-6.098884,4.364916,-2.869311,3.177503,7.640310,2.868793,0.125715,0.066408,-1.853777,-2.917645,-5.818301,8.775501,5.087141,-5.672047,-8.517810,-6.441324,0.545189,5.926041,-5.514307,-7.354661,-6.478124,8.361061,4.519298,-6.024933,-7.749981,-4.567563,-8.566170,7.649223,0.185227,-0.963814,-0.898019,-8.701549,-8.204718,2.003289,-1.203924,-1.649204,9.427133,0.215166,-5.532185,-0.386384,-6.296344,3.995451,-1.357731,-8.898375,-0.496268,-2.287028,9.098220,-6.257309,-7.024130,-9.139490,7.025792,8.955529,4.882612,-2.921336,1.984980,-6.812388,1.623356,-2.780550,-8.864401,-1.582407,0.644609,-3.007533,7.253444,-3.449336,-8.736842,6.392026,3.367680,9.852060,6.244772,-9.735570,-2.557754,-9.000010,-5.979204,-3.032830,4.602071,-6.975295,0.585968,4.443116,2.152052,-3.221869,-2.950906,-7.339803,3.694392,-5.766797,9.245881,8.331425,-6.655353,0.740509,-7.024636,4.119166,-8.123171,8.026209,-3.098643,3.787549,-6.724347,-1.401780,1.901670,9.133960,-1.430144,0.381602,-0.207845,6.399282,-5.039763,-6.583346,-1.101418,-2.779896,1.043334,-3.001091,-2.299656], dtype = "float64")#candidate|6614|(1200,)|const|float64
call_6613 = func_1449_call(relay.reshape(const_6614.astype('float64'), [5, 15, 16]), relay.reshape(const_6614.astype('float64'), [5, 15, 16]), )
call_6615 = func_1449_call(relay.reshape(const_6614.astype('float64'), [5, 15, 16]), relay.reshape(const_6614.astype('float64'), [5, 15, 16]), )
output = relay.Tuple([call_6608,call_6613,const_6614,])
output2 = relay.Tuple([call_6609,call_6615,const_6614,])
func_6624 = relay.Function([], output)
mod['func_6624'] = func_6624
mod = relay.transform.InferType()(mod)
mutated_mod['func_6624'] = func_6624
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6624_call = mutated_mod.get_global_var('func_6624')
call_6625 = func_6624_call()
output = call_6625
func_6626 = relay.Function([], output)
mutated_mod['func_6626'] = func_6626
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6633 = relay.var("var_6633", dtype = "float32", shape = (7, 16, 6))#candidate|6633|(7, 16, 6)|var|float32
uop_6634 = relay.rsqrt(var_6633.astype('float32')) # shape=(7, 16, 6)
output = uop_6634
output2 = uop_6634
func_6637 = relay.Function([var_6633,], output)
mod['func_6637'] = func_6637
mod = relay.transform.InferType()(mod)
mutated_mod['func_6637'] = func_6637
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6638 = relay.var("var_6638", dtype = "float32", shape = (7, 16, 6))#candidate|6638|(7, 16, 6)|var|float32
func_6637_call = mutated_mod.get_global_var('func_6637')
call_6639 = func_6637_call(var_6638)
output = call_6639
func_6640 = relay.Function([var_6638], output)
mutated_mod['func_6640'] = func_6640
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1140_call = mod.get_global_var('func_1140')
func_1141_call = mutated_mod.get_global_var('func_1141')
call_6668 = relay.TupleGetItem(func_1140_call(), 0)
call_6669 = relay.TupleGetItem(func_1141_call(), 0)
func_4057_call = mod.get_global_var('func_4057')
func_4058_call = mutated_mod.get_global_var('func_4058')
call_6685 = relay.TupleGetItem(func_4057_call(), 0)
call_6686 = relay.TupleGetItem(func_4058_call(), 0)
func_2009_call = mod.get_global_var('func_2009')
func_2011_call = mutated_mod.get_global_var('func_2011')
call_6688 = relay.TupleGetItem(func_2009_call(), 1)
call_6689 = relay.TupleGetItem(func_2011_call(), 1)
output = relay.Tuple([call_6668,call_6685,call_6688,])
output2 = relay.Tuple([call_6669,call_6686,call_6689,])
func_6701 = relay.Function([], output)
mod['func_6701'] = func_6701
mod = relay.transform.InferType()(mod)
mutated_mod['func_6701'] = func_6701
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6701_call = mutated_mod.get_global_var('func_6701')
call_6702 = func_6701_call()
output = call_6702
func_6703 = relay.Function([], output)
mutated_mod['func_6703'] = func_6703
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5634_call = mod.get_global_var('func_5634')
func_5635_call = mutated_mod.get_global_var('func_5635')
call_6726 = relay.TupleGetItem(func_5634_call(), 2)
call_6727 = relay.TupleGetItem(func_5635_call(), 2)
uop_6738 = relay.asin(call_6726.astype('float64')) # shape=(48, 1)
uop_6740 = relay.asin(call_6727.astype('float64')) # shape=(48, 1)
func_2243_call = mod.get_global_var('func_2243')
func_2245_call = mutated_mod.get_global_var('func_2245')
call_6744 = relay.TupleGetItem(func_2243_call(relay.reshape(call_6726.astype('float32'), [48,])), 2)
call_6745 = relay.TupleGetItem(func_2245_call(relay.reshape(call_6726.astype('float32'), [48,])), 2)
func_5311_call = mod.get_global_var('func_5311')
func_5315_call = mutated_mod.get_global_var('func_5315')
const_6748 = relay.const(5, dtype = "int64")#candidate|6748|()|const|int64
call_6747 = relay.TupleGetItem(func_5311_call(relay.reshape(const_6748.astype('int64'), []), relay.reshape(call_6744.astype('float32'), [48,]), ), 3)
call_6749 = relay.TupleGetItem(func_5315_call(relay.reshape(const_6748.astype('int64'), []), relay.reshape(call_6744.astype('float32'), [48,]), ), 3)
func_1486_call = mod.get_global_var('func_1486')
func_1488_call = mutated_mod.get_global_var('func_1488')
call_6770 = relay.TupleGetItem(func_1486_call(relay.reshape(call_6726.astype('float32'), [2, 24])), 2)
call_6771 = relay.TupleGetItem(func_1488_call(relay.reshape(call_6726.astype('float32'), [2, 24])), 2)
output = relay.Tuple([uop_6738,call_6744,call_6747,const_6748,call_6770,])
output2 = relay.Tuple([uop_6740,call_6745,call_6749,const_6748,call_6771,])
func_6774 = relay.Function([], output)
mod['func_6774'] = func_6774
mod = relay.transform.InferType()(mod)
mutated_mod['func_6774'] = func_6774
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6774_call = mutated_mod.get_global_var('func_6774')
call_6775 = func_6774_call()
output = call_6775
func_6776 = relay.Function([], output)
mutated_mod['func_6776'] = func_6776
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5674_call = mod.get_global_var('func_5674')
func_5676_call = mutated_mod.get_global_var('func_5676')
call_6781 = relay.TupleGetItem(func_5674_call(), 0)
call_6782 = relay.TupleGetItem(func_5676_call(), 0)
output = call_6781
output2 = call_6782
func_6785 = relay.Function([], output)
mod['func_6785'] = func_6785
mod = relay.transform.InferType()(mod)
output = func_6785()
func_6786 = relay.Function([], output)
mutated_mod['func_6786'] = func_6786
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6352_call = mod.get_global_var('func_6352')
func_6353_call = mutated_mod.get_global_var('func_6353')
call_6822 = relay.TupleGetItem(func_6352_call(), 1)
call_6823 = relay.TupleGetItem(func_6353_call(), 1)
var_6830 = relay.var("var_6830", dtype = "int64", shape = (6, 1, 6))#candidate|6830|(6, 1, 6)|var|int64
bop_6831 = relay.bitwise_and(call_6822.astype('int16'), var_6830.astype('int16')) # shape=(6, 1, 6)
bop_6834 = relay.bitwise_and(call_6823.astype('int16'), var_6830.astype('int16')) # shape=(6, 1, 6)
func_3533_call = mod.get_global_var('func_3533')
func_3534_call = mutated_mod.get_global_var('func_3534')
call_6835 = relay.TupleGetItem(func_3533_call(), 0)
call_6836 = relay.TupleGetItem(func_3534_call(), 0)
output = relay.Tuple([bop_6831,call_6835,])
output2 = relay.Tuple([bop_6834,call_6836,])
func_6839 = relay.Function([var_6830,], output)
mod['func_6839'] = func_6839
mod = relay.transform.InferType()(mod)
mutated_mod['func_6839'] = func_6839
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6840 = relay.var("var_6840", dtype = "int64", shape = (6, 1, 6))#candidate|6840|(6, 1, 6)|var|int64
func_6839_call = mutated_mod.get_global_var('func_6839')
call_6841 = func_6839_call(var_6840)
output = call_6841
func_6842 = relay.Function([var_6840], output)
mutated_mod['func_6842'] = func_6842
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2282_call = mod.get_global_var('func_2282')
func_2283_call = mutated_mod.get_global_var('func_2283')
call_6905 = func_2282_call()
call_6906 = func_2282_call()
var_6920 = relay.var("var_6920", dtype = "float32", shape = (14, 13, 10))#candidate|6920|(14, 13, 10)|var|float32
bop_6921 = relay.logical_xor(call_6905.astype('int16'), var_6920.astype('int16')) # shape=(14, 13, 10)
bop_6924 = relay.logical_xor(call_6906.astype('int16'), var_6920.astype('int16')) # shape=(14, 13, 10)
func_4398_call = mod.get_global_var('func_4398')
func_4401_call = mutated_mod.get_global_var('func_4401')
var_6926 = relay.var("var_6926", dtype = "float32", shape = (48, 1))#candidate|6926|(48, 1)|var|float32
call_6925 = relay.TupleGetItem(func_4398_call(relay.reshape(var_6926.astype('float32'), [24, 2])), 2)
call_6927 = relay.TupleGetItem(func_4401_call(relay.reshape(var_6926.astype('float32'), [24, 2])), 2)
func_1859_call = mod.get_global_var('func_1859')
func_1861_call = mutated_mod.get_global_var('func_1861')
call_6932 = relay.TupleGetItem(func_1859_call(), 0)
call_6933 = relay.TupleGetItem(func_1861_call(), 0)
uop_6940 = relay.sinh(bop_6921.astype('float64')) # shape=(14, 13, 10)
uop_6942 = relay.sinh(bop_6924.astype('float64')) # shape=(14, 13, 10)
uop_6956 = relay.atanh(uop_6940.astype('float32')) # shape=(14, 13, 10)
uop_6958 = relay.atanh(uop_6942.astype('float32')) # shape=(14, 13, 10)
output = relay.Tuple([call_6925,var_6926,call_6932,uop_6956,])
output2 = relay.Tuple([call_6927,var_6926,call_6933,uop_6958,])
func_6959 = relay.Function([var_6920,var_6926,], output)
mod['func_6959'] = func_6959
mod = relay.transform.InferType()(mod)
mutated_mod['func_6959'] = func_6959
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6959_call = mutated_mod.get_global_var('func_6959')
var_6961 = relay.var("var_6961", dtype = "float32", shape = (14, 13, 10))#candidate|6961|(14, 13, 10)|var|float32
var_6962 = relay.var("var_6962", dtype = "float32", shape = (48, 1))#candidate|6962|(48, 1)|var|float32
call_6960 = func_6959_call(var_6961,var_6962,)
output = call_6960
func_6963 = relay.Function([var_6961,var_6962,], output)
mutated_mod['func_6963'] = func_6963
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5441_call = mod.get_global_var('func_5441')
func_5443_call = mutated_mod.get_global_var('func_5443')
call_6965 = func_5441_call()
call_6966 = func_5441_call()
output = call_6965
output2 = call_6966
func_6975 = relay.Function([], output)
mod['func_6975'] = func_6975
mod = relay.transform.InferType()(mod)
output = func_6975()
func_6976 = relay.Function([], output)
mutated_mod['func_6976'] = func_6976
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6624_call = mod.get_global_var('func_6624')
func_6626_call = mutated_mod.get_global_var('func_6626')
call_7041 = relay.TupleGetItem(func_6624_call(), 1)
call_7042 = relay.TupleGetItem(func_6626_call(), 1)
func_3028_call = mod.get_global_var('func_3028')
func_3030_call = mutated_mod.get_global_var('func_3030')
var_7051 = relay.var("var_7051", dtype = "int8", shape = (9, 100))#candidate|7051|(9, 100)|var|int8
call_7050 = relay.TupleGetItem(func_3028_call(relay.reshape(var_7051.astype('int8'), [900,])), 1)
call_7052 = relay.TupleGetItem(func_3030_call(relay.reshape(var_7051.astype('int8'), [900,])), 1)
var_7055 = relay.var("var_7055", dtype = "float32", shape = (14, 9, 10))#candidate|7055|(14, 9, 10)|var|float32
bop_7056 = relay.bitwise_xor(call_7050.astype('uint16'), var_7055.astype('uint16')) # shape=(14, 9, 10)
bop_7059 = relay.bitwise_xor(call_7052.astype('uint16'), var_7055.astype('uint16')) # shape=(14, 9, 10)
uop_7081 = relay.sinh(bop_7056.astype('float32')) # shape=(14, 9, 10)
uop_7083 = relay.sinh(bop_7059.astype('float32')) # shape=(14, 9, 10)
func_6200_call = mod.get_global_var('func_6200')
func_6201_call = mutated_mod.get_global_var('func_6201')
call_7086 = relay.TupleGetItem(func_6200_call(), 0)
call_7087 = relay.TupleGetItem(func_6201_call(), 0)
bop_7094 = relay.add(uop_7081.astype('uint8'), relay.reshape(var_7055.astype('uint8'), relay.shape_of(uop_7081))) # shape=(14, 9, 10)
bop_7097 = relay.add(uop_7083.astype('uint8'), relay.reshape(var_7055.astype('uint8'), relay.shape_of(uop_7083))) # shape=(14, 9, 10)
output = relay.Tuple([call_7041,var_7051,call_7086,bop_7094,])
output2 = relay.Tuple([call_7042,var_7051,call_7087,bop_7097,])
func_7100 = relay.Function([var_7051,var_7055,], output)
mod['func_7100'] = func_7100
mod = relay.transform.InferType()(mod)
var_7101 = relay.var("var_7101", dtype = "int8", shape = (9, 100))#candidate|7101|(9, 100)|var|int8
var_7102 = relay.var("var_7102", dtype = "float32", shape = (14, 9, 10))#candidate|7102|(14, 9, 10)|var|float32
output = func_7100(var_7101,var_7102,)
func_7103 = relay.Function([var_7101,var_7102,], output)
mutated_mod['func_7103'] = func_7103
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2009_call = mod.get_global_var('func_2009')
func_2011_call = mutated_mod.get_global_var('func_2011')
call_7105 = relay.TupleGetItem(func_2009_call(), 0)
call_7106 = relay.TupleGetItem(func_2011_call(), 0)
func_7100_call = mod.get_global_var('func_7100')
func_7103_call = mutated_mod.get_global_var('func_7103')
var_7110 = relay.var("var_7110", dtype = "int8", shape = (900,))#candidate|7110|(900,)|var|int8
const_7111 = relay.const([-6.180093,5.656422,1.381204,4.774217,-3.848085,-9.065937,1.579155,7.497416,-0.342909,-6.841407,3.360708,-6.056659,-8.685766,-1.234300,9.851456,-4.844668,7.499146,6.086486,4.157348,3.114757,7.885766,-6.700782,7.064050,0.278576,0.615276,-4.676781,7.810470,9.986240,-7.826480,8.839260,3.751659,9.407537,7.394791,5.803962,7.551447,6.605122,-7.931337,-8.895615,5.738812,6.538956,2.308402,4.912024,-7.313322,4.123012,-2.809596,-7.418649,-0.616319,-9.405041,2.133198,-9.041245,5.786230,8.539726,2.794548,5.445646,1.998795,-4.922516,-3.724309,5.302968,-6.319882,5.223506,3.050638,-4.177758,-2.345770,-6.538430,-9.937505,-7.125981,-3.586101,-1.110521,4.953894,-3.455456,-6.422640,-2.304541,9.971103,-8.581929,-8.561746,-1.093791,3.523856,5.461519,-8.150223,5.564042,4.696687,-4.042072,8.127330,3.157450,-7.808300,-2.700629,-7.370738,-5.871542,-3.355765,9.809389,-4.113249,3.981994,-5.336216,8.882774,-3.663511,-2.760325,7.174958,5.234029,1.611516,2.880067,-8.336851,-8.522454,-7.076002,-6.700185,3.346297,9.035956,-0.082478,-2.987999,-0.908054,8.182789,-9.806366,-4.281290,-1.601740,6.932832,-4.272123,9.469732,-7.994647,-3.872732,-6.972261,5.120830,-4.069052,-2.317854,2.051517,-2.353906,-1.378563,-0.168804,8.977335,-7.167014,-5.334240,0.161505,4.450703,-5.750720,-4.090221,-1.630854,2.790773,2.235051,5.204380,-7.061554,-8.444052,-5.936258,-6.176644,1.382482,3.705924,3.990124,2.891999,-2.211170,-8.180993,-2.216763,6.641408,8.040949,5.812039,0.706695,-5.706725,5.850096,-6.204499,-8.082124,6.221467,-1.197546,6.988735,-1.281150,-1.007930,2.819540,8.687825,9.889952,4.101763,-4.463795,5.755783,9.199184,2.872974,-0.957353,-2.156661,9.673076,2.635172,-8.331805,7.686072,4.245075,4.216249,-7.760798,3.634247,-6.427025,9.146201,1.083034,-1.635151,-3.730162,0.936592,5.319860,9.643082,3.460306,-4.497887,-6.120707,0.986464,7.325858,-2.470747,8.421015,9.252841,-4.256653,-9.176465,-2.314729,-5.653126,6.139969,9.030771,8.191548,2.748451,2.483211,-5.620818,2.656012,-1.899891,0.183259,2.683257,-1.254337,-1.220563,4.044190,-2.061485,7.526951,-3.621915,-9.309194,4.318131,7.709776,8.959952,-0.792548,-1.801195,2.938843,-3.096661,7.152263,4.449988,-9.522451,8.976001,4.310291,1.073424,-0.377405,2.532247,-2.906689,9.552487,2.854565,-6.799113,-9.876017,1.863370,9.259209,-1.201081,8.586039,-5.411279,6.770923,3.250382,0.072292,7.126050,5.590997,4.005513,6.096692,5.100891,4.430454,-8.694261,-0.609429,2.186669,3.595750,-7.412137,9.762878,4.307248,-4.084279,8.848242,5.986252,-2.468807,6.518178,-0.977594,-4.529673,8.149175,-9.038622,3.627843,-4.311848,-1.114705,6.576453,-8.721733,-7.476507,9.620100,7.651339,-7.846207,-0.377435,5.449615,-8.053181,-1.939092,1.760861,-9.096030,-1.938013,-9.630424,-2.312231,-5.675928,1.818221,7.206721,-8.193733,9.514156,7.459713,3.886927,-1.158691,-5.155039,-2.460306,5.146995,-7.979195,1.300723,0.441806,5.300453,6.216764,9.148800,3.433787,-6.863868,-9.473997,5.894335,1.535193,4.895082,5.622730,9.416388,-2.534556,4.450918,-4.294396,2.778662,-6.354778,-8.688231,3.441175,-4.550562,-9.030761,-9.498486,-7.233171,-3.834857,-2.103200,9.927113,1.074979,-6.965866,0.239381,4.323608,-1.978884,-0.929714,4.513522,-9.500512,-6.055374,7.264308,7.697717,5.745720,1.383949,-2.992016,2.310675,4.186510,-6.169908,9.973638,2.684906,4.649318,6.577717,-1.791506,-2.247982,3.698435,-4.963232,3.222839,6.580288,1.893736,5.147587,-5.058746,-4.932232,8.251749,8.130949,-7.765921,4.935370,5.128044,3.413069,-8.888474,-6.908947,3.414305,-7.562708,4.351261,3.882274,8.537289,-6.513875,-3.718771,7.504100,7.142187,-8.763103,-9.929440,6.406550,-6.276171,9.167720,3.428364,2.737903,-3.094525,1.651418,5.544653,8.798943,1.159320,-6.102765,-4.490241,-1.790932,8.129285,0.467127,-1.682218,4.242840,-7.780928,4.208633,-5.499018,-5.574677,9.278067,-1.280851,-4.893189,9.467972,9.184783,1.420250,1.573343,4.408201,-6.223057,-4.305152,-8.306176,-7.444042,5.807015,-1.570932,-8.210851,-9.636258,-7.064986,-1.700679,-4.337441,3.335611,1.671046,4.839466,-2.288629,8.922189,-8.175319,7.937286,8.544312,9.738344,-1.575258,0.933201,-9.546091,-1.998173,-4.409228,5.000099,-4.468318,8.421506,-8.454412,-1.350743,2.721519,2.004403,-5.060604,-5.829670,-0.868800,-2.693904,7.729092,5.353738,8.466522,6.368839,-9.864116,6.743509,7.465194,0.684571,4.817665,-6.500007,3.036447,-9.189885,-7.844340,-8.525669,-8.613432,8.277225,-8.025697,3.848483,-9.580138,6.306050,-4.065619,7.513243,0.076313,6.552666,5.445145,-7.073515,0.432682,-4.098388,8.637531,6.572386,1.352615,-5.311559,7.424771,5.065918,-0.563348,7.819829,4.847166,-9.780578,1.144631,-7.973224,3.668859,6.480498,6.266005,-0.845307,-3.951121,8.314573,0.337809,9.129817,8.688523,-5.839199,-1.226942,-2.602333,5.755840,-8.463924,-8.792163,0.886686,8.279829,9.498407,-1.451133,-7.905020,2.506121,-0.331894,8.134183,7.682448,-9.628296,-9.888448,3.869538,4.964706,0.846428,7.928837,-2.257303,3.720413,-7.551447,-6.392266,-2.312915,1.448116,-8.427822,-0.145196,-7.414718,3.110443,-6.107969,7.912383,-1.677523,-6.740808,-2.870655,-3.980801,-2.167326,4.974563,-7.259036,1.981355,-9.604099,-4.288859,-6.207294,-7.749453,-8.543098,9.211181,7.417881,4.944490,7.380010,6.744884,8.407461,-6.553171,5.353631,-4.943688,-2.129753,-4.343539,4.060706,9.123482,-1.724890,-2.973131,7.437322,1.246900,-1.741127,3.419528,-5.166925,7.813133,-7.973519,9.436236,5.148169,3.898840,9.090784,-2.903998,-7.408095,-8.225626,2.460842,0.112400,-4.041208,5.639971,4.322400,2.218774,6.754579,-3.619480,-1.239571,2.908288,0.832250,4.500070,9.716091,7.718470,-4.971431,-4.738170,-1.649929,-5.078370,-2.472729,8.413511,-3.568079,9.035982,-1.389351,0.973075,8.330008,-9.448067,2.589277,4.301184,-2.480771,-3.587164,-3.152648,-7.689925,0.146598,5.463692,3.168063,5.484374,3.664202,8.482173,-2.070183,6.868672,-4.262797,7.522233,8.565134,-3.852827,4.943339,-2.942661,0.406006,6.289723,-2.779934,-2.757713,6.981145,1.714750,-6.256895,-4.348158,-9.203828,-0.717779,-6.552078,-0.864399,-5.949641,3.779565,-5.469672,2.932412,-3.671620,-9.771920,7.126439,-7.653574,-9.977629,-5.659321,1.550325,-2.735221,-5.781070,-0.954352,-1.488744,-7.706520,9.786394,-9.164790,-0.527331,6.464711,-6.547419,0.481098,-5.864064,9.471969,8.070958,3.218206,-8.525495,-4.918361,-2.468056,6.255574,-0.415061,6.423576,8.094541,8.932332,5.803710,0.082792,-6.720762,0.749010,-9.960012,0.702728,-6.752972,-2.667094,-9.856138,6.594025,2.228030,8.200495,9.054233,4.834901,1.910143,-9.607508,3.952489,-6.737982,-3.795168,-7.672617,-9.570586,-8.807954,-8.589414,-4.736232,-8.287009,0.804223,-5.960781,4.343087,2.194897,1.000229,0.267735,8.674328,9.598950,-2.758766,-1.124159,-5.961214,-0.462424,8.522980,-3.870341,-7.052391,-9.906117,-3.273204,-3.154277,-4.926745,3.412057,-5.904618,1.603397,8.344140,-5.178426,-1.437061,6.882558,3.536402,3.977464,-8.423888,-8.416983,-0.391383,3.822472,-8.483427,-6.806508,2.511760,-9.837210,-1.861537,-3.808760,-2.898766,2.513978,8.555424,5.884729,5.805718,1.581472,-7.899891,-6.633382,-2.168617,-8.382656,3.568591,4.708802,-8.190296,3.731385,2.606485,-1.363715,-1.143302,-9.504096,-0.276129,-7.386336,1.447002,-9.984537,-3.496123,-2.294027,-4.696205,7.964840,-5.154948,-0.703272,-4.354808,8.260912,1.239756,5.772655,-0.563794,2.032584,3.336699,-6.547109,-8.192837,8.852882,5.410724,1.587482,-9.309480,6.612609,-1.682345,3.178183,1.100257,-8.326812,-3.571002,-4.318834,-6.802271,-4.750844,-1.648259,-8.238045,0.072676,0.798552,4.179675,-7.846639,0.039383,-7.612116,6.959081,-1.161916,1.396065,-0.668702,-9.581309,-1.369095,-3.161009,-5.219956,9.853328,7.483571,-7.046397,1.233361,-7.668674,1.486179,7.847560,3.126413,1.570730,-3.929526,-7.332168,2.400743,4.131026,8.680136,-1.362207,-7.420255,-8.249796,-6.130726,-8.690090,2.011219,1.094038,-7.185946,-3.349362,6.278623,1.694341,-5.432864,-4.914433,-8.848009,1.170426,-8.909137,-4.779503,7.483789,-0.952101,5.083511,5.622135,7.161222,-9.173274,-5.313115,8.651610,-5.206463,6.151818,3.906294,-0.461124,2.983432,6.360037,5.207582,0.726498,6.568782,-5.432121,-2.768095,6.784917,-7.602810,-5.621933,-8.522738,0.556990,-6.987619,-2.000739,-2.692640,-9.491082,-7.478393,7.427962,2.413401,5.392314,1.123873,4.634801,7.292636,3.038648,-8.556199,-7.944912,-5.933685,-3.994862,-8.564813,-5.824028,0.234298,4.934020,-1.681676,-0.517718,0.578685,-4.302715,0.093006,-9.513455,-2.712116,3.255741,6.814579,-9.727922,4.764119,0.928766,5.280959,-3.035227,-6.981577,-7.419918,6.337117,-5.890583,-3.421274,2.120281,-8.772616,5.298688,6.699122,-3.061105,-4.516748,-8.151608,1.779797,-0.394881,6.984810,4.605749,-2.782891,0.946255,-1.769154,-6.538934,-8.815559,0.498259,9.213724,-2.760395,7.231772,-1.972436,6.593670,3.269465,-2.744051,7.829131,-7.112696,6.256294,-6.098461,-7.390266,-6.143598,-2.738252,-8.902246,1.704968,-0.366624,6.285215,-1.305158,5.942979,-1.103471,-3.136155,-3.165192,6.605722,5.996954,9.647359,9.547885,-7.502216,-2.027170,-2.793963,-6.961820,1.640268,7.410832,-1.707554,-4.879242,7.829836,-5.571779,1.935607,1.272758,-7.283878,9.348869,1.478022,7.808961,-5.837065,-7.252337,1.666598,-9.697362,2.053525,0.120221,-9.625541,0.101218,-7.195097,7.727193,5.326715,-5.896299,6.208931,2.517499,-5.379975,4.061157,6.181992,-9.758658,-6.417759,0.205654,-4.232391,-1.609123,-9.419188,1.639182,3.896432,-7.441102,1.782942,-9.259819,-8.013368,7.769429,5.154926,6.352351,-6.850087,0.229067,-1.356194,-5.400261,4.752978,5.829344,6.572278,-4.419365,-5.424778,9.083407,-3.151967,-1.060796,7.365517,3.774574,-2.107437,4.261979,-4.429400,-9.533825,1.439635,-1.710656,4.525758,-3.262771,-7.566594,2.038588,1.232720,-8.564809,6.457576,-6.994931,7.585871,8.582498,-5.817126,-8.327630,4.929911,-5.526801,-9.958957,8.490061,-7.918313,-1.868893,-6.632987,0.299364,-5.048975,9.852289,1.088930,-7.959281,-5.072073,-3.553532,2.927082,0.706753,3.974630,1.195464,-2.173378,9.603506,8.178852,9.618094,-5.134760,1.403205,0.889837,-5.341768,7.902622,6.782122,-2.279780,-1.936585,-4.620263,-7.534916,2.529070,2.538624,-8.823740,7.933082,-6.851538,5.343065,9.264254,2.526144,-0.397317,7.135044,1.062513,9.802991,2.671094,1.902754,2.487918,6.036409,1.520528,0.810237,-8.114097,9.047618,0.994202,8.432476,-0.911432,8.759048,-5.364615,-1.359084,3.587404,1.389189,9.445034,0.007590,-8.410263,-2.590014,9.223325,3.058235,-9.876234,9.718976,9.568262,-0.009255,2.034390,-3.091945,0.927347,2.740445,-7.506367,9.832594,9.889797,5.934767,4.477837,-4.969847,6.348317,-5.980962,-4.981042,9.359945,-5.987760,4.793415,-0.717292,0.142221,-9.060477,-8.411223,3.830732,3.079298,-8.933803,-3.236521,-5.752000,5.784081,-9.645771,2.210163,5.821163,7.435467,-3.362107,4.022092,-1.723364,-6.072752,-7.222790,-7.727959,-8.719235,-2.002974,-3.434669,7.569058,7.178165,-6.438220,-4.258801,7.557577,-3.902948,-5.006689,2.121053,9.781176,-1.554934,0.438135,9.497671,1.263127,0.278797,-2.633880,-8.807429,-2.759463,-3.313299,-1.287984,-3.400493,-8.688922,-0.578416,5.079580,9.685904,6.895349,7.188302,-3.339965,-0.067288,-6.787726,8.233136,5.689817,-5.289176,-6.196746,-4.718719,-7.920341,-9.859925,-3.629960,4.803568,-4.869154,-8.366945,-4.743901,-9.525073,-4.471297,-5.258779,-2.445095,-8.373417,-4.811271,9.554455,7.250062,2.308423,-3.526679,2.830830,-0.728908,4.153058,7.872167,-5.320366,2.342051,-6.729041,-6.284107,-2.052466,-1.301673,-3.489643,-8.562728,2.136416,-0.432208,6.853136,-5.609675,8.145338,5.969011,-7.496227,-9.396305,-2.283077,7.504332,-0.069168,-3.122035,2.020394,5.381598,9.015791,8.825004,9.309835,7.323379,3.692263,6.986419,-4.846408,5.783263,0.076515,0.726253,8.972267,-9.652727,-1.320006,-8.046408,-3.822216,-3.002855,6.228366,-2.373676,8.211588,2.010995,-5.632122,8.482498,7.382734,0.215953,-3.451184,9.115181,6.740957,4.752778,-0.210250,8.722513,8.502326,-4.236472,-5.947569,-6.670250,-4.472654,-4.706557,-9.169681,6.060423,-6.341544,0.616491,5.263786,-9.979703,-3.415673,9.072801,6.374047,8.984473,-6.394091,-9.915367,2.164044,-3.441992,-4.323342,-2.743323,-0.251479,6.918558,-4.407113,5.228427,5.264275,-6.062001,-2.480797,-9.705189,3.954590,-1.214573,9.940946,-8.078727,0.783284,-1.132408,6.356835,3.336990,-5.881536,-5.527298,6.444941,-0.654889,5.293977], dtype = "float32")#candidate|7111|(1260,)|const|float32
call_7109 = relay.TupleGetItem(func_7100_call(relay.reshape(var_7110.astype('int8'), [9, 100]), relay.reshape(const_7111.astype('float32'), [14, 9, 10]), ), 3)
call_7112 = relay.TupleGetItem(func_7103_call(relay.reshape(var_7110.astype('int8'), [9, 100]), relay.reshape(const_7111.astype('float32'), [14, 9, 10]), ), 3)
const_7125 = relay.const([[[3.408142,2.715149,-2.255025,-3.476456,-7.805716,-7.506622,0.182638,-8.186728,-8.159708,-1.596996],[-3.106294,-8.545503,0.336802,-2.678253,-2.605638,2.031662,7.720855,3.377583,7.733375,-0.450091],[-8.302345,0.923512,9.846565,-6.941155,3.360146,9.349732,-5.019197,-9.088642,-2.844855,2.775045],[-9.839034,6.702688,1.361315,-9.068993,-6.586879,-0.616949,1.796970,-7.444373,9.594743,-2.295617]],[[1.409444,-6.759950,8.311526,0.394561,8.801611,-9.514815,7.970552,6.012749,4.827263,-1.202474],[-7.027763,-4.134449,-8.571005,5.479973,-6.857641,9.188468,3.330538,1.001176,-1.800079,-6.349064],[5.177832,1.980202,-4.496685,8.281960,-9.818417,5.654839,-5.737166,-6.535190,8.950381,-1.480041],[9.879260,7.913931,3.792939,1.970590,-6.517396,3.255662,6.954414,-1.134247,-8.879574,9.844689]],[[8.926592,6.642422,-5.599613,0.427584,6.491697,0.603900,9.817593,2.095160,9.932792,-2.197891],[0.901069,8.878337,-0.975322,-8.133891,2.719461,-5.276675,1.808190,-4.628628,2.242627,7.698536],[0.723180,-3.763662,6.213567,5.586792,-9.374254,-5.701799,-3.248104,-4.045695,-4.783537,4.222818],[-9.635927,-9.450539,6.961022,-4.134499,-4.222061,-6.772720,-8.882218,-3.451269,-2.446460,4.936505]],[[6.320789,-4.821900,9.485310,1.145435,-7.522574,-6.709494,-7.981680,-4.433876,9.574667,-9.261890],[-3.841117,-3.393792,2.629936,-8.988243,-0.161118,7.629710,-0.249842,7.503392,-5.265355,8.953663],[7.301159,-2.047007,-4.908069,-3.756481,5.413579,-7.019332,9.372209,-8.546555,0.659611,-5.085997],[-8.256147,-8.109442,-6.347051,3.459948,-8.840901,7.367645,-1.377129,6.762613,-3.327419,-2.876828]],[[-7.048078,0.001797,7.987861,0.051302,-9.560438,1.413364,7.661994,6.637145,8.937184,-2.223533],[0.625939,-9.735155,5.924262,1.012830,9.460618,0.309160,-0.852442,4.896508,5.200078,-7.319212],[-4.120326,-9.998118,6.633672,3.690312,-4.820572,-2.097177,1.083560,6.811854,-4.335704,-5.375762],[8.682077,-8.781218,-6.343447,7.572855,-1.201456,-4.888450,7.973847,-0.481350,-8.901957,-0.209298]],[[8.925598,1.012380,9.350115,-9.326948,5.571221,0.927996,-7.023105,-2.590823,9.689640,-3.792968],[9.496949,-0.810421,-2.075699,-8.432710,3.953658,9.424003,6.420426,4.703838,-2.659905,1.008409],[8.243879,-1.042605,-8.008020,-2.724250,-4.305463,2.670798,7.068516,4.232498,-6.631279,7.660778],[-4.565808,-6.493006,3.087341,-0.191912,3.919211,2.524604,-7.168394,2.660215,-6.321044,-2.450418]],[[-7.903099,-1.123288,8.000172,2.388407,5.616035,0.802608,-5.139134,-8.982448,-1.607195,5.957692],[-7.920457,-5.779181,-4.845254,6.037792,7.437039,8.397134,0.764049,-2.479738,3.822451,-8.950066],[-2.398832,-4.749019,0.773845,-9.471019,6.655739,-4.179221,-6.251782,-6.683049,-9.975577,0.269088],[6.621947,6.079851,-5.884775,-4.633537,-1.147716,2.097088,-2.669868,6.280981,-3.712583,3.626840]],[[7.540170,4.137389,-5.057571,-2.841985,0.206150,8.416090,-9.942075,7.116032,-0.782000,8.928718],[-5.012537,9.483853,-4.582378,-9.931428,-9.844645,8.097247,8.748494,4.741928,-2.495455,-1.085812],[2.102055,0.161474,3.251321,-0.563082,-2.619783,-2.220549,-7.597911,7.041201,-6.930071,9.939600],[-9.926311,-1.486511,1.712224,2.742126,7.020374,5.172889,0.920056,-2.175603,3.257325,-3.056469]],[[-9.895884,-2.944165,-3.751276,-7.669118,-6.481952,6.661460,-8.611057,-4.528188,1.993897,9.316985],[-6.663385,5.905459,9.129202,-8.626899,6.268536,-7.981805,4.083776,-2.837943,7.540499,-3.745789],[4.073672,-9.883938,4.599710,9.377676,-7.901223,4.250819,-3.378904,3.532679,-3.789666,-1.879422],[-7.761680,-2.882674,-0.539754,-7.502736,6.482320,7.646773,-2.589769,-4.157823,-7.438037,2.069391]],[[-8.366509,0.362168,4.846894,0.890106,-4.960175,1.942747,-2.247135,-3.802798,4.260022,-8.735626],[6.490957,7.850765,1.409699,6.382961,9.163290,9.745429,5.620982,-2.252658,6.867687,7.321021],[-8.388240,-7.518751,-5.991006,7.213607,0.594007,-6.729133,0.454219,0.299887,1.878027,-9.502352],[7.017926,-0.202642,2.235492,1.450145,-3.031359,-8.737420,-1.166058,-3.611022,-2.263235,-3.031150]],[[1.942400,-2.437297,-6.608055,-1.921979,6.794103,-0.371143,-6.860002,2.753475,-5.378011,-1.394849],[4.751041,0.578740,7.086916,-4.639959,4.971559,-3.443088,5.811822,8.014978,-0.142286,2.510777],[-6.487687,-3.796132,7.469509,-8.214985,-2.390847,-0.607972,-5.117284,0.173051,6.899678,9.906453],[-6.667349,-3.725434,-8.695628,7.525234,5.900104,-2.446002,8.617297,-7.799439,7.181455,-7.146202]],[[5.433501,6.471857,-5.399127,2.828864,8.961939,-8.868493,-8.853014,2.873409,-1.102024,6.474579],[-0.173256,1.667336,-5.243278,-7.449156,9.272642,-7.974567,8.415439,-3.498612,-7.377515,-6.584994],[-4.069850,-1.595865,7.366341,7.148532,-2.894391,8.952373,4.934541,-5.701481,-2.779715,4.146559],[7.218423,-4.181050,0.610000,-6.503107,-2.019468,9.016893,7.401403,-0.048963,-1.688738,-4.589996]],[[-9.952308,0.741293,9.415186,-9.640370,-4.751273,2.271202,8.834117,-0.466079,-4.492214,-5.364389],[2.865531,9.626455,0.035570,9.669616,0.221714,3.232995,6.884021,2.052733,-5.879619,-4.414671],[3.141353,5.579187,7.254194,-8.568105,-1.668976,3.795646,-9.512746,7.403146,-6.403483,5.402859],[-7.586965,1.447329,6.845329,-1.305170,-7.025713,-5.010204,-7.722247,-6.743099,-1.880991,4.843881]],[[-6.016988,-1.885727,8.117880,-0.116680,5.009564,-2.448185,-3.997898,3.733607,-2.780567,-0.737330],[8.657141,4.411257,-4.509060,7.268384,-2.868476,2.571779,6.156507,5.407666,2.899474,-5.947913],[-4.698372,9.997498,3.052406,-7.663723,-6.076560,-1.427271,-1.499091,-7.624288,-6.288767,5.337161],[-4.826078,4.093637,-0.185443,6.700426,-5.273926,-1.158507,-3.153239,-9.063388,5.595539,1.634019]]], dtype = "float32")#candidate|7125|(14, 4, 10)|const|float32
bop_7126 = relay.power(call_7105.astype('float32'), const_7125.astype('float32')) # shape=(14, 4, 10)
bop_7129 = relay.power(call_7106.astype('float32'), const_7125.astype('float32')) # shape=(14, 4, 10)
func_3123_call = mod.get_global_var('func_3123')
func_3125_call = mutated_mod.get_global_var('func_3125')
var_7138 = relay.var("var_7138", dtype = "float64", shape = (16,))#candidate|7138|(16,)|var|float64
call_7137 = relay.TupleGetItem(func_3123_call(relay.reshape(var_7138.astype('float64'), [8, 2])), 6)
call_7139 = relay.TupleGetItem(func_3125_call(relay.reshape(var_7138.astype('float64'), [8, 2])), 6)
output = relay.Tuple([call_7109,var_7110,const_7111,bop_7126,call_7137,var_7138,])
output2 = relay.Tuple([call_7112,var_7110,const_7111,bop_7129,call_7139,var_7138,])
func_7141 = relay.Function([var_7110,var_7138,], output)
mod['func_7141'] = func_7141
mod = relay.transform.InferType()(mod)
var_7142 = relay.var("var_7142", dtype = "int8", shape = (900,))#candidate|7142|(900,)|var|int8
var_7143 = relay.var("var_7143", dtype = "float64", shape = (16,))#candidate|7143|(16,)|var|float64
output = func_7141(var_7142,var_7143,)
func_7144 = relay.Function([var_7142,var_7143,], output)
mutated_mod['func_7144'] = func_7144
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4910_call = mod.get_global_var('func_4910')
func_4912_call = mutated_mod.get_global_var('func_4912')
call_7194 = func_4910_call()
call_7195 = func_4910_call()
output = call_7194
output2 = call_7195
func_7200 = relay.Function([], output)
mod['func_7200'] = func_7200
mod = relay.transform.InferType()(mod)
output = func_7200()
func_7201 = relay.Function([], output)
mutated_mod['func_7201'] = func_7201
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5763_call = mod.get_global_var('func_5763')
func_5764_call = mutated_mod.get_global_var('func_5764')
call_7281 = relay.TupleGetItem(func_5763_call(), 1)
call_7282 = relay.TupleGetItem(func_5764_call(), 1)
output = relay.Tuple([call_7281,])
output2 = relay.Tuple([call_7282,])
func_7289 = relay.Function([], output)
mod['func_7289'] = func_7289
mod = relay.transform.InferType()(mod)
output = func_7289()
func_7290 = relay.Function([], output)
mutated_mod['func_7290'] = func_7290
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7323 = relay.const([[[10,7,1,3,-6,-2,10,1,2,2,-10,-6,9,1,-7,-3],[1,8,-2,9,-6,8,7,-7,-5,-2,-5,5,6,-1,-4,-2],[6,9,1,-5,9,4,-3,2,7,6,-6,-7,6,3,-4,-5],[5,8,1,4,7,5,-8,-9,-5,-8,-3,-1,-2,-8,-3,9],[-6,5,-2,-9,-6,8,-3,10,1,9,2,-6,-8,3,7,9],[-10,-3,3,1,6,3,8,9,9,7,10,8,-8,-7,-4,10],[-1,4,5,-3,-7,-2,8,-4,9,-10,5,-5,10,7,10,-8],[10,-7,9,8,6,9,-1,-3,-4,-9,1,-1,-8,5,-6,1]]], dtype = "uint16")#candidate|7323|(1, 8, 16)|const|uint16
var_7324 = relay.var("var_7324", dtype = "uint16", shape = (4, 8, 16))#candidate|7324|(4, 8, 16)|var|uint16
bop_7325 = relay.bitwise_or(const_7323.astype('uint16'), var_7324.astype('uint16')) # shape=(4, 8, 16)
func_4151_call = mod.get_global_var('func_4151')
func_4153_call = mutated_mod.get_global_var('func_4153')
call_7332 = relay.TupleGetItem(func_4151_call(), 0)
call_7333 = relay.TupleGetItem(func_4153_call(), 0)
uop_7334 = relay.log2(const_7323.astype('float64')) # shape=(1, 8, 16)
bop_7336 = relay.bitwise_or(uop_7334.astype('int8'), relay.reshape(const_7323.astype('int8'), relay.shape_of(uop_7334))) # shape=(1, 8, 16)
func_4082_call = mod.get_global_var('func_4082')
func_4083_call = mutated_mod.get_global_var('func_4083')
call_7348 = relay.TupleGetItem(func_4082_call(), 0)
call_7349 = relay.TupleGetItem(func_4083_call(), 0)
var_7353 = relay.var("var_7353", dtype = "float64", shape = (5, 8, 16))#candidate|7353|(5, 8, 16)|var|float64
bop_7354 = relay.left_shift(uop_7334.astype('int32'), var_7353.astype('int32')) # shape=(5, 8, 16)
output = relay.Tuple([bop_7325,call_7332,bop_7336,call_7348,bop_7354,])
output2 = relay.Tuple([bop_7325,call_7333,bop_7336,call_7349,bop_7354,])
func_7360 = relay.Function([var_7324,var_7353,], output)
mod['func_7360'] = func_7360
mod = relay.transform.InferType()(mod)
var_7361 = relay.var("var_7361", dtype = "uint16", shape = (4, 8, 16))#candidate|7361|(4, 8, 16)|var|uint16
var_7362 = relay.var("var_7362", dtype = "float64", shape = (5, 8, 16))#candidate|7362|(5, 8, 16)|var|float64
output = func_7360(var_7361,var_7362,)
func_7363 = relay.Function([var_7361,var_7362,], output)
mutated_mod['func_7363'] = func_7363
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4735_call = mod.get_global_var('func_4735')
func_4736_call = mutated_mod.get_global_var('func_4736')
call_7379 = relay.TupleGetItem(func_4735_call(), 0)
call_7380 = relay.TupleGetItem(func_4736_call(), 0)
func_1920_call = mod.get_global_var('func_1920')
func_1922_call = mutated_mod.get_global_var('func_1922')
call_7407 = relay.TupleGetItem(func_1920_call(), 2)
call_7408 = relay.TupleGetItem(func_1922_call(), 2)
output = relay.Tuple([call_7379,call_7407,])
output2 = relay.Tuple([call_7380,call_7408,])
func_7410 = relay.Function([], output)
mod['func_7410'] = func_7410
mod = relay.transform.InferType()(mod)
mutated_mod['func_7410'] = func_7410
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7410_call = mutated_mod.get_global_var('func_7410')
call_7411 = func_7410_call()
output = call_7411
func_7412 = relay.Function([], output)
mutated_mod['func_7412'] = func_7412
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1859_call = mod.get_global_var('func_1859')
func_1861_call = mutated_mod.get_global_var('func_1861')
call_7472 = relay.TupleGetItem(func_1859_call(), 0)
call_7473 = relay.TupleGetItem(func_1861_call(), 0)
func_4910_call = mod.get_global_var('func_4910')
func_4912_call = mutated_mod.get_global_var('func_4912')
call_7483 = func_4910_call()
call_7484 = func_4910_call()
output = relay.Tuple([call_7472,call_7483,])
output2 = relay.Tuple([call_7473,call_7484,])
func_7501 = relay.Function([], output)
mod['func_7501'] = func_7501
mod = relay.transform.InferType()(mod)
mutated_mod['func_7501'] = func_7501
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7501_call = mutated_mod.get_global_var('func_7501')
call_7502 = func_7501_call()
output = call_7502
func_7503 = relay.Function([], output)
mutated_mod['func_7503'] = func_7503
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3650_call = mod.get_global_var('func_3650')
func_3651_call = mutated_mod.get_global_var('func_3651')
call_7504 = relay.TupleGetItem(func_3650_call(), 0)
call_7505 = relay.TupleGetItem(func_3651_call(), 0)
func_1140_call = mod.get_global_var('func_1140')
func_1141_call = mutated_mod.get_global_var('func_1141')
call_7508 = relay.TupleGetItem(func_1140_call(), 0)
call_7509 = relay.TupleGetItem(func_1141_call(), 0)
func_6200_call = mod.get_global_var('func_6200')
func_6201_call = mutated_mod.get_global_var('func_6201')
call_7535 = relay.TupleGetItem(func_6200_call(), 1)
call_7536 = relay.TupleGetItem(func_6201_call(), 1)
func_2243_call = mod.get_global_var('func_2243')
func_2245_call = mutated_mod.get_global_var('func_2245')
const_7538 = relay.const([[7.238604],[-8.680130],[-0.152394],[-0.681084],[1.763868],[-9.885015],[-7.779178],[-9.122363],[3.128690],[-1.690620],[-2.536182],[-0.932439],[-0.494758],[-1.240975],[4.329878],[-8.437971],[9.273781],[-6.242190],[9.842034],[-9.464265],[7.823368],[5.722124],[5.500568],[1.607712],[0.288028],[9.974377],[6.111041],[7.709120],[4.675778],[-2.918376],[-8.674356],[8.098501],[7.963424],[-7.492290],[3.064806],[3.764928],[6.525731],[-3.441429],[-4.982462],[9.006750],[8.174759],[-1.313314],[-3.985453],[-5.708814],[1.173784],[6.147562],[4.333651],[8.797916]], dtype = "float32")#candidate|7538|(48, 1)|const|float32
call_7537 = relay.TupleGetItem(func_2243_call(relay.reshape(const_7538.astype('float32'), [48,])), 0)
call_7539 = relay.TupleGetItem(func_2245_call(relay.reshape(const_7538.astype('float32'), [48,])), 0)
output = relay.Tuple([call_7504,call_7508,call_7535,call_7537,const_7538,])
output2 = relay.Tuple([call_7505,call_7509,call_7536,call_7539,const_7538,])
func_7540 = relay.Function([], output)
mod['func_7540'] = func_7540
mod = relay.transform.InferType()(mod)
mutated_mod['func_7540'] = func_7540
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7540_call = mutated_mod.get_global_var('func_7540')
call_7541 = func_7540_call()
output = call_7541
func_7542 = relay.Function([], output)
mutated_mod['func_7542'] = func_7542
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7200_call = mod.get_global_var('func_7200')
func_7201_call = mutated_mod.get_global_var('func_7201')
call_7548 = func_7200_call()
call_7549 = func_7200_call()
output = relay.Tuple([call_7548,])
output2 = relay.Tuple([call_7549,])
func_7563 = relay.Function([], output)
mod['func_7563'] = func_7563
mod = relay.transform.InferType()(mod)
mutated_mod['func_7563'] = func_7563
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7563_call = mutated_mod.get_global_var('func_7563')
call_7564 = func_7563_call()
output = call_7564
func_7565 = relay.Function([], output)
mutated_mod['func_7565'] = func_7565
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7604 = relay.var("var_7604", dtype = "uint64", shape = (15, 11, 4))#candidate|7604|(15, 11, 4)|var|uint64
var_7605 = relay.var("var_7605", dtype = "uint64", shape = (15, 11, 4))#candidate|7605|(15, 11, 4)|var|uint64
bop_7606 = relay.less_equal(var_7604.astype('bool'), relay.reshape(var_7605.astype('bool'), relay.shape_of(var_7604))) # shape=(15, 11, 4)
func_903_call = mod.get_global_var('func_903')
func_905_call = mutated_mod.get_global_var('func_905')
var_7611 = relay.var("var_7611", dtype = "float32", shape = (10, 96))#candidate|7611|(10, 96)|var|float32
call_7610 = relay.TupleGetItem(func_903_call(relay.reshape(var_7611.astype('float32'), [6, 16, 10])), 2)
call_7612 = relay.TupleGetItem(func_905_call(relay.reshape(var_7611.astype('float32'), [6, 16, 10])), 2)
func_1859_call = mod.get_global_var('func_1859')
func_1861_call = mutated_mod.get_global_var('func_1861')
call_7656 = relay.TupleGetItem(func_1859_call(), 0)
call_7657 = relay.TupleGetItem(func_1861_call(), 0)
output = relay.Tuple([bop_7606,call_7610,var_7611,call_7656,])
output2 = relay.Tuple([bop_7606,call_7612,var_7611,call_7657,])
func_7659 = relay.Function([var_7604,var_7605,var_7611,], output)
mod['func_7659'] = func_7659
mod = relay.transform.InferType()(mod)
mutated_mod['func_7659'] = func_7659
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7659_call = mutated_mod.get_global_var('func_7659')
var_7661 = relay.var("var_7661", dtype = "uint64", shape = (15, 11, 4))#candidate|7661|(15, 11, 4)|var|uint64
var_7662 = relay.var("var_7662", dtype = "uint64", shape = (15, 11, 4))#candidate|7662|(15, 11, 4)|var|uint64
var_7663 = relay.var("var_7663", dtype = "float32", shape = (10, 96))#candidate|7663|(10, 96)|var|float32
call_7660 = func_7659_call(var_7661,var_7662,var_7663,)
output = call_7660
func_7664 = relay.Function([var_7661,var_7662,var_7663,], output)
mutated_mod['func_7664'] = func_7664
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1920_call = mod.get_global_var('func_1920')
func_1922_call = mutated_mod.get_global_var('func_1922')
call_7668 = relay.TupleGetItem(func_1920_call(), 1)
call_7669 = relay.TupleGetItem(func_1922_call(), 1)
uop_7674 = relay.exp(call_7668.astype('float64')) # shape=(16, 11, 12)
uop_7676 = relay.exp(call_7669.astype('float64')) # shape=(16, 11, 12)
output = relay.Tuple([uop_7674,])
output2 = relay.Tuple([uop_7676,])
func_7689 = relay.Function([], output)
mod['func_7689'] = func_7689
mod = relay.transform.InferType()(mod)
output = func_7689()
func_7690 = relay.Function([], output)
mutated_mod['func_7690'] = func_7690
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3040_call = mod.get_global_var('func_3040')
func_3042_call = mutated_mod.get_global_var('func_3042')
call_7780 = func_3040_call()
call_7781 = func_3040_call()
var_7795 = relay.var("var_7795", dtype = "float32", shape = (14, 14, 10))#candidate|7795|(14, 14, 10)|var|float32
bop_7796 = relay.logical_xor(call_7780.astype('uint32'), var_7795.astype('uint32')) # shape=(14, 14, 10)
bop_7799 = relay.logical_xor(call_7781.astype('uint32'), var_7795.astype('uint32')) # shape=(14, 14, 10)
var_7808 = relay.var("var_7808", dtype = "float32", shape = (14, 5, 10))#candidate|7808|(14, 5, 10)|var|float32
bop_7809 = relay.logical_xor(call_7780.astype('uint64'), var_7808.astype('uint64')) # shape=(14, 5, 10)
bop_7812 = relay.logical_xor(call_7781.astype('uint64'), var_7808.astype('uint64')) # shape=(14, 5, 10)
func_3670_call = mod.get_global_var('func_3670')
func_3672_call = mutated_mod.get_global_var('func_3672')
call_7814 = relay.TupleGetItem(func_3670_call(), 0)
call_7815 = relay.TupleGetItem(func_3672_call(), 0)
output = relay.Tuple([bop_7796,bop_7809,call_7814,])
output2 = relay.Tuple([bop_7799,bop_7812,call_7815,])
func_7821 = relay.Function([var_7795,var_7808,], output)
mod['func_7821'] = func_7821
mod = relay.transform.InferType()(mod)
var_7822 = relay.var("var_7822", dtype = "float32", shape = (14, 14, 10))#candidate|7822|(14, 14, 10)|var|float32
var_7823 = relay.var("var_7823", dtype = "float32", shape = (14, 5, 10))#candidate|7823|(14, 5, 10)|var|float32
output = func_7821(var_7822,var_7823,)
func_7824 = relay.Function([var_7822,var_7823,], output)
mutated_mod['func_7824'] = func_7824
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1580_call = mod.get_global_var('func_1580')
func_1582_call = mutated_mod.get_global_var('func_1582')
call_7850 = relay.TupleGetItem(func_1580_call(), 2)
call_7851 = relay.TupleGetItem(func_1582_call(), 2)
func_2009_call = mod.get_global_var('func_2009')
func_2011_call = mutated_mod.get_global_var('func_2011')
call_7863 = relay.TupleGetItem(func_2009_call(), 0)
call_7864 = relay.TupleGetItem(func_2011_call(), 0)
func_1449_call = mod.get_global_var('func_1449')
func_1453_call = mutated_mod.get_global_var('func_1453')
const_7877 = relay.const([4.430245,-6.942659,9.349827,-4.160236,-8.834447,-8.170954,0.133198,-1.740122,1.252870,2.211476,8.992768,4.579043,-0.108668,8.658547,-1.409309,-0.762196,-1.957067,-8.926640,2.697592,5.270434,3.213317,-7.779516,-0.216298,-2.465944,-7.587629,8.734447,0.879702,1.590629,-7.740848,5.309578,5.874232,9.730607,1.069566,6.860141,-5.247345,-1.943296,-2.917596,-3.167225,0.805137,3.679432,-0.160034,3.119600,8.956348,5.583610,1.330312,-7.449136,-0.160202,7.308176,4.509469,-1.988956,0.729805,-8.790381,9.620907,7.501927,8.917358,1.570783,3.424434,6.610932,7.504948,3.827931,-5.943082,4.287413,0.598238,-9.561657,9.726256,-8.933392,5.652721,-6.997156,1.749641,3.608467,-7.597852,1.721471,2.593572,9.986131,6.957189,8.004591,-2.310949,9.236719,6.299392,6.764560,-0.592480,-2.457887,-1.531749,9.105698,-5.526657,-6.664092,0.581376,-1.521713,-4.359292,4.573361,-7.687384,9.113609,3.869530,-0.388891,-4.567366,8.051686,6.784980,-3.640263,-0.983159,-5.241842,-5.905192,-5.584527,-7.161952,-7.337839,-2.907420,-1.134546,2.888885,7.224905,-2.647022,1.490579,2.459108,-6.708469,-3.238399,-7.201259,-2.726222,3.583351,9.198498,-5.612286,2.912462,9.635905,-4.265202,-6.100552,9.572963,-4.078883,-1.051925,5.075478,-1.088759,-6.833125,-1.209567,2.917369,4.705158,-8.176626,-5.220322,-6.252898,3.685917,9.310370,-1.708910,8.253605,-6.089604,8.237799,-2.110321,-8.637721,-2.326708,4.539915,-6.076129,1.783441,-8.089156,-4.001147,-8.463305,-6.009109,-4.778158,1.075307,2.302347,7.097575,-3.644045,-8.436155,2.963414,5.937525,-8.760106,-1.621423,-2.370505,-7.681085,5.393191,5.657794,-1.903697,-1.453559,-8.772906,1.916951,-9.264098,2.574260,9.042685,6.250529,-1.470684,6.849254,-0.465077,8.649906,9.009289,7.442837,8.013408,9.181635,-1.920330,-3.249035,1.562720,-7.147402,-6.935275,1.577029,-2.448593,-8.381352,0.062602,8.140515,-4.170841,-9.750821,-4.938774,-6.186026,0.410741,3.345142,9.678250,-1.371881,2.918545,1.593694,-7.433373,-2.522638,3.541760,5.399886,-5.773588,-0.691906,-8.748853,-7.202407,-9.103566,-3.797401,-3.983407,4.689479,9.171900,4.675904,3.817726,4.623946,6.768121,-1.224433,-5.781668,3.752895,-4.248812,1.595256,0.325232,4.322200,7.055719,4.489380,-1.054898,7.094861,-8.795387,-6.248448,4.956187,6.403201,6.637870,-0.295275,2.219167,-8.156788,0.113608,-5.669973,-2.564608,0.425853,2.476263,8.249842,4.724524,-7.059957,0.216910,7.523543,-9.258797,5.345963,-1.182432,3.947117,-9.737864,5.979676,-6.453375,-1.598854,-4.239163,-5.765611,-4.814580,8.117226,-7.621769,2.931282,-3.700469,2.790907,0.232499,1.345514,-8.620630,2.095490,-8.815780,-4.113376,6.558295,9.446863,-5.057591,9.464169,-8.608386,1.982708,-3.547130,-6.379202,6.556319,4.057731,3.039469,1.639376,-5.834294,-5.461100,5.798212,1.897550,8.702481,-7.424487,-6.197061,-0.532245,-2.977113,5.223472,-1.904820,-6.212634,9.293693,-2.157321,-5.580417,-0.490345,-9.243479,1.495851,-6.260580,-8.572083,-7.004364,5.287052,3.987899,9.486938,5.394722,-3.301544,-2.146687,-8.102050,8.937907,-6.122224,-9.410293,-8.992975,8.662768,-9.163650,-4.843223,1.561661,-0.327031,6.504582,-5.555560,8.291687,9.808945,5.963395,-6.804503,-5.920965,-2.590319,3.538170,5.011794,-5.173707,-4.334936,-2.012081,5.216977,6.005167,5.479790,4.565031,6.153807,3.919793,4.431015,-5.029050,-8.391384,0.116198,-4.320403,4.848882,-3.250442,-2.602853,2.436544,3.622114,0.455959,-8.815979,4.244090,-0.099109,-7.414293,2.193213,5.609349,-5.532265,-1.500240,-4.433915,-7.998306,1.478989,0.509326,1.144525,-5.544354,-9.099329,3.132754,-3.284038,-0.802212,9.146110,2.221489,-0.247691,6.394528,-1.714462,-0.789038,-1.747518,8.206797,1.781969,7.679371,2.628028,6.402462,5.850984,-5.733204,2.616614,5.246961,7.628301,-5.979948,6.793992,-4.845935,2.908090,-4.299147,-3.445047,3.957780,7.154512,-4.850717,0.208416,-2.861597,8.295529,-7.409898,9.323881,8.983969,-5.040330,2.389256,5.294140,-3.552167,-1.651183,-9.882949,-5.893531,6.116115,9.583318,-8.295044,5.887357,4.478551,5.113698,-4.282403,5.949873,3.831867,2.214668,9.408986,6.032292,0.287598,9.811350,-4.743810,-0.656961,6.607295,6.210979,-5.923702,-6.447263,2.140369,4.524413,-9.190090,-6.693946,2.112926,-5.088092,-6.872434,-4.818692,-5.216946,-8.474413,4.131757,-8.859823,-0.442672,-9.509903,-8.802434,-7.941828,-6.730691,1.829017,9.979540,-0.840991,6.417795,5.957515,-6.787273,-9.079484,5.451768,0.100916,8.450918,1.275901,-4.314419,-1.265940,-2.636071,-5.893295,-1.735857,-8.565894,1.468335,-3.526480,3.517309,2.822357,4.607003,-6.151887,-7.838405,7.970237,5.805920,0.597897,-3.899363,9.102199,-1.661549,6.903763,2.847188,-3.728178,8.540513,-1.733286,9.238983,-8.097018,4.569358,7.001455,6.409196,6.067433,-7.104882,-3.753613,-2.197040,8.154466,6.650180,2.453163,-1.650661,-3.026374,6.979008,6.747478,-8.787234,4.959549,-0.281171,4.915663,-5.275723,5.131189,0.634474,9.958988,5.330450,-4.140264,-9.650414,0.592002,-1.615304,-5.338623,-5.897924,-1.752117,7.001298,-1.744720,-7.634545,3.373499,-9.047133,3.946635,-2.135381,0.053009,-2.094106,8.234439,-0.497329,5.026706,-0.328019,-7.238245,7.605768,6.401276,-0.053552,5.198817,6.464001,6.272578,6.206448,7.391723,-6.880816,0.899586,-1.224264,2.179171,3.969471,1.349001,-3.796910,5.756942,-5.341370,-7.323054,-7.978170,-9.778804,7.778154,-9.757128,-8.185365,-7.254205,-0.074993,6.933554,-9.268259,5.450122,-6.939233,8.604588,-4.919054,-2.081543,1.020404,-6.579184,-6.788594,9.586118,-2.996904,-2.812127,6.344664,0.409394,-1.451825,7.033429,1.095986,3.079714,2.534232,-1.014747,5.182618,9.338897,-7.560907,-5.387207,-5.408727,-8.737803,3.171597,5.788498,1.540158,4.934485,-9.237786,7.729666,6.715049,6.810051,4.995017,1.018578,-2.436528,-1.602289,-9.289774,-5.723866,-5.753447,3.246214,9.681348,5.796669,-1.650432,3.406529,8.395540,-3.382500,6.150561,0.936895,-8.872063,1.121788,1.736470,9.506853,-7.294245,-2.291755,-7.777628,9.797857,0.872938,-3.631014,9.462801,-1.585651,-8.496636,1.055910,-3.027299,8.740720,5.181276,1.066487,-4.646786,-7.722864,-1.257127,4.318870,5.432508,7.109861,5.042104,-9.495490,3.860522,4.876378,1.455349,6.824828,-7.764827,-8.821406,0.761357,-7.364754,-0.255306,-9.557455,-2.830230,4.725398,-3.321805,-9.640422,5.049082,-7.677262,4.869179,-9.962471,2.605171,-9.865462,-7.349710,3.715359,-8.608517,2.083789,3.449229,-6.473500,-7.707629,5.198674,-3.747179,-4.239936,-1.549922,-0.353489,5.805639,-0.210067,-5.538466,-1.615435,-0.759320,-1.755386,8.318031,5.879812,9.897462,-9.676236,-8.196986,4.201554,8.839726,-9.499963,-4.884096,7.278014,3.594049,-3.217428,-0.827303,6.581150,5.681202,-9.429313,1.216860,6.378590,7.525419,-5.947112,6.286636,-6.771908,-8.050774,-2.955147,1.213674,-2.747532,4.044875,-3.254788,0.016870,-9.311206,4.032671,7.575275,7.418305,5.184236,8.155842,-8.583297,5.816862,3.081089,8.544757,0.645134,-8.879961,4.897909,-9.414837,1.529811,0.739713,-4.264204,-7.850790,-3.125068,-3.300842,-5.566775,6.536183,-3.919113,8.266880,-5.676721,7.590402,1.616498,7.957380,-1.257277,-9.560088,3.222534,4.723635,-7.050963,-9.267643,8.533166,0.985744,-1.609322,-4.784158,9.080839,-1.584070,-8.207244,6.991530,2.974226,6.032941,9.878216,-4.590196,4.966874,-1.858930,8.637384,-9.387131,-3.474945,0.143990,2.364294,5.813230,4.353655,-8.472345,-2.483411,-9.321416,1.167046,6.525778,9.676594,0.727985,0.078159,7.847228,-2.576071,-3.702208,4.324698,7.809570,4.868701,2.429855,0.997984,4.911992,-5.439040,3.131446,3.186223,-8.017685,-0.680357,7.004346,2.852504,3.002116,5.667680,-4.405301,0.193393,2.341827,9.876128,7.883541,-1.494256,-2.957078,-3.051356,-1.847798,-2.056215,3.850472,0.949458,-7.958618,7.571292,-6.904796,4.901949,0.948583,0.231106,-6.398625,0.184268,0.615789,-6.169859,-0.426735,7.696782,-5.002848,9.165546,6.827558,-3.005779,-4.194517,6.778881,-3.290082,0.039614,0.930268,-6.448541,4.397171,6.768296,-9.978580,-8.422134,0.388950,5.630045,5.358984,5.836944,7.104813,6.633272,5.635503,0.536925,8.879604,7.098474,3.815137,-2.003140,9.327936,5.905963,4.641891,7.113327,0.155394,-1.506661,9.734459,2.774866,-4.495376,-9.348818,8.032703,5.413726,4.414703,1.349441,7.928209,6.528700,-8.986508,-7.037095,4.191151,-3.515140,-1.881799,3.635883,-5.458431,6.314572,3.425751,-5.823054,8.096379,-2.121075,-5.075074,7.046580,8.269977,-6.121704,3.415361,-7.724904,-2.746919,2.816058,5.383732,0.482130,-1.484072,-5.905340,-9.827735,-8.494474,6.398872,-7.029071,4.807986,5.782551,8.224990,-4.469211,-5.657130,7.211528,1.534273,5.911108,1.236502,-0.362620,6.449648,-3.720220,4.131545,2.565660,0.378363,-4.333931,3.429075,3.393868,5.283721,8.043308,-9.764640,2.566597,-3.969469,3.107619,8.796199,6.185481,-5.869962,-3.939280,-7.603389,-0.208701,-8.215652,-1.698355,-6.224777,-2.982507,9.497848,9.251927,-7.822599,1.713527,-2.769633,-7.994619,-4.203758,-1.357302,5.564872,-7.839342,7.182143,5.559174,5.218760,3.079919,-5.152298,-5.344494,-9.336498,2.773643,-9.735585,1.997387,4.907927,-6.876384,1.270936,2.839857,6.138102,-7.012941,-3.566390,-1.507763,-7.563163,-6.212031,9.661607,-3.884470,-0.465122,-9.505506,8.719487,0.397095,-4.312512,-0.196978,1.269595,-5.091350,-7.508334,9.063305,3.917395,-2.699396,4.717114,-5.704022,3.040696,-7.212483,-7.627266,-5.555390,-3.512192,0.923607,0.856534,-6.171217,6.007143,-1.358521,-2.396741,-2.768433,5.880647,5.871634,0.501804,-2.651946,-7.440810,0.975669,7.786462,-5.244990,5.910129,-6.158742,-3.100826,5.895325,-4.888583,9.639103,6.018189,-3.601954,-3.255064,-2.361792,5.304006,8.305537,8.230698,-2.974582,-7.704009,7.877574,-2.325199,9.433773,-2.579263,-7.294417,-9.373443,5.076299,-4.562678,-3.136581,6.894966,-5.107804,0.990685,6.369017,-5.841003,-5.094957,-9.135990,7.581886,4.496570,8.102428,2.984944,-7.776927,0.422265,-5.024917,0.930069,1.816109,5.567767,8.763590,8.885274,1.789516,2.504575,-7.573649,3.100529,-4.600612,-9.232149,7.100359,-0.313445,9.595194,8.081756,0.938669,3.323685,-2.842530,-1.168197,7.976732,-9.472397,-2.607248,-6.429753,4.846233,-3.294884,7.348258,-0.365307,-7.840086,-6.468379,-3.243209,3.682740,2.845336,-9.482998,9.359351,8.279063,-7.965870,-0.127590,7.464814,-6.493042,-1.175641,2.799273,4.446832,-4.345222,-4.981832,-2.253452,8.805883,-5.629980,-1.910872,-4.317376,9.023701,-5.458632,6.391285,-1.267078,-7.033603,4.009492,2.653329,-0.396463,-6.585635,8.271302,6.568776,-0.249460,3.486536,2.386905,8.450823,-9.435735,-0.217145,8.266227,9.014986,-5.110964,-0.172122,-1.145064,-4.665308,-8.052316,-9.879645,8.095876,4.445052,-6.514049,-5.602595,-7.946348,4.075247,6.334884,-0.102783,5.174258,-0.764776,1.379033,7.556536,4.487069,-1.976449,5.994714,6.002870,-9.891866,-8.436933,0.332322,1.157157,-9.867364,-7.348123,-2.553426,-0.810339,-2.105053,6.427561,6.840664,-0.584041,7.422324,0.439906,8.860666,6.038321,9.167400,-6.076462,9.550411,2.456707,-7.343243,9.601086,-4.027597,-4.848004,-2.746243,-0.413020,-0.872042,-6.128515,7.331131,-9.801633,-2.331782,-7.887282,3.980146,9.333928,-7.185017,8.371773,-7.627140,5.562861,-1.056039,-7.254529,-4.568071,2.699453,1.501872,-9.312526,5.128617,1.964513,-2.955036,8.395410,-1.856974,-9.322722,7.094302,8.548742,-3.691897,-3.272255,-4.628142,-1.961671,9.355530,5.980084,2.964377,2.299283,6.662171,5.548503,2.938638,3.656848,1.598822,-0.649192,7.450097,-6.703274,9.606908,6.532972,9.557307,-4.823796,0.835082,5.794407,7.743168,0.404979,5.068860,-0.348423,8.364070,-0.021824,-2.869797,-4.270068,-6.662258,5.697020,3.260395,9.864340,-5.440110,-7.555080,-7.588179,9.581376,-6.714521,-6.873784,1.512394,-4.073696,-3.305229,0.454379,-7.079717,3.765838,-4.834138,-9.328932,4.628011,8.563056,5.358674,1.662678,4.662515,1.543477], dtype = "float64")#candidate|7877|(1200,)|const|float64
call_7876 = func_1449_call(relay.reshape(const_7877.astype('float64'), [5, 15, 16]), relay.reshape(const_7877.astype('float64'), [5, 15, 16]), )
call_7878 = func_1449_call(relay.reshape(const_7877.astype('float64'), [5, 15, 16]), relay.reshape(const_7877.astype('float64'), [5, 15, 16]), )
func_5020_call = mod.get_global_var('func_5020')
func_5023_call = mutated_mod.get_global_var('func_5023')
const_7885 = relay.const([3.034380,-6.263731,0.077376,6.171040,-4.857195,-0.838651,-6.971818,0.147301,-0.672797,0.189628,-8.662817,9.782527,1.424737,-8.692413,2.255762,7.786508,-9.630797,3.810238,-2.476487,-0.873264,-3.290553,-5.226783,7.715538,-7.774500,-8.726265,-4.862089,-0.350695,-0.586806,9.490062,-0.093384,8.523287,3.023928,2.612315,7.458811,-7.246202,-5.764389,1.982856,0.595752,6.050104,-2.475881,2.350247,-0.681922,-4.536200,-3.378599,9.007965,0.746250,-0.644863,-1.303670,4.897632,3.231212,7.640551,-4.975527,-9.025274,6.225478,4.360483,2.772291,5.219619,6.013394,5.799561,4.614464,-8.063783,5.358353,5.203921,2.179756,5.116092,-7.578394,-1.379429,2.676796,-7.279849,-3.130118,8.376241,4.213126,9.393924,-3.676687,-0.255251,9.368908,-6.511278,1.074362,-5.248975,-0.801863,7.332424,-8.582153,-0.296119,1.243931,1.306332,-5.288689,9.603877,1.236332,-8.108162,0.282642,4.284084,-4.467757,3.314756,8.194745,-0.005585,-4.831111,1.203242,9.967633,-7.706950,-0.095158,8.269906,-0.162575,-6.429870,2.362454,-9.064613,4.026942,-5.910347,4.580680,6.315623,1.833187,8.589734,-7.858609,0.396189,-0.619651,-2.440554,8.779509,1.454182,-3.968047,0.700368,3.084543,6.658686,9.330489,-6.907792,1.675036,1.445186,3.678970,-9.628055,5.403640,8.615489,-7.647801,3.554394,8.883224,6.580203,-8.259746,-4.982592,-4.294758,6.408844,9.220187,3.335774,8.817013,6.676306,1.771364,-1.841269,9.812055,-0.443095,8.308063,3.840068,-2.006777,4.205381,6.220532,-4.952003,7.550687,5.439934,0.242370,7.750382,-3.033442,0.528552,3.803853,-1.418091,-4.687623,-5.396171,-1.353779,-6.918639,-0.958814,-1.140110,8.173600,-2.578445,-0.273415,4.397820,-5.887521,-9.865586,-5.349088,-3.481068,-2.158179,-5.855351,2.544366,-6.068491,7.189772,-9.819012,-9.957317,7.291833,-3.001256,-1.541885,-8.481062,-5.216361,2.709283,2.497272,3.974719,3.501957,-4.235929,-0.713373,-4.537813], dtype = "float32")#candidate|7885|(192,)|const|float32
call_7884 = relay.TupleGetItem(func_5020_call(relay.reshape(const_7885.astype('float32'), [6, 4, 8])), 0)
call_7886 = relay.TupleGetItem(func_5023_call(relay.reshape(const_7885.astype('float32'), [6, 4, 8])), 0)
output = relay.Tuple([call_7850,call_7863,call_7876,const_7877,call_7884,const_7885,])
output2 = relay.Tuple([call_7851,call_7864,call_7878,const_7877,call_7886,const_7885,])
func_7906 = relay.Function([], output)
mod['func_7906'] = func_7906
mod = relay.transform.InferType()(mod)
mutated_mod['func_7906'] = func_7906
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7906_call = mutated_mod.get_global_var('func_7906')
call_7907 = func_7906_call()
output = call_7907
func_7908 = relay.Function([], output)
mutated_mod['func_7908'] = func_7908
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3925_call = mod.get_global_var('func_3925')
func_3926_call = mutated_mod.get_global_var('func_3926')
call_7955 = relay.TupleGetItem(func_3925_call(), 0)
call_7956 = relay.TupleGetItem(func_3926_call(), 0)
func_2401_call = mod.get_global_var('func_2401')
func_2402_call = mutated_mod.get_global_var('func_2402')
call_7957 = relay.TupleGetItem(func_2401_call(), 1)
call_7958 = relay.TupleGetItem(func_2402_call(), 1)
output = relay.Tuple([call_7955,call_7957,])
output2 = relay.Tuple([call_7956,call_7958,])
func_7959 = relay.Function([], output)
mod['func_7959'] = func_7959
mod = relay.transform.InferType()(mod)
mutated_mod['func_7959'] = func_7959
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7959_call = mutated_mod.get_global_var('func_7959')
call_7960 = func_7959_call()
output = call_7960
func_7961 = relay.Function([], output)
mutated_mod['func_7961'] = func_7961
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4689_call = mod.get_global_var('func_4689')
func_4691_call = mutated_mod.get_global_var('func_4691')
call_7969 = func_4689_call()
call_7970 = func_4689_call()
output = relay.Tuple([call_7969,])
output2 = relay.Tuple([call_7970,])
func_7971 = relay.Function([], output)
mod['func_7971'] = func_7971
mod = relay.transform.InferType()(mod)
mutated_mod['func_7971'] = func_7971
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7971_call = mutated_mod.get_global_var('func_7971')
call_7972 = func_7971_call()
output = call_7972
func_7973 = relay.Function([], output)
mutated_mod['func_7973'] = func_7973
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2737_call = mod.get_global_var('func_2737')
func_2738_call = mutated_mod.get_global_var('func_2738')
call_7977 = func_2737_call()
call_7978 = func_2737_call()
output = call_7977
output2 = call_7978
func_7990 = relay.Function([], output)
mod['func_7990'] = func_7990
mod = relay.transform.InferType()(mod)
mutated_mod['func_7990'] = func_7990
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7990_call = mutated_mod.get_global_var('func_7990')
call_7991 = func_7990_call()
output = call_7991
func_7992 = relay.Function([], output)
mutated_mod['func_7992'] = func_7992
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4319_call = mod.get_global_var('func_4319')
func_4320_call = mutated_mod.get_global_var('func_4320')
call_8005 = relay.TupleGetItem(func_4319_call(), 0)
call_8006 = relay.TupleGetItem(func_4320_call(), 0)
output = call_8005
output2 = call_8006
func_8017 = relay.Function([], output)
mod['func_8017'] = func_8017
mod = relay.transform.InferType()(mod)
mutated_mod['func_8017'] = func_8017
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8017_call = mutated_mod.get_global_var('func_8017')
call_8018 = func_8017_call()
output = call_8018
func_8019 = relay.Function([], output)
mutated_mod['func_8019'] = func_8019
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1140_call = mod.get_global_var('func_1140')
func_1141_call = mutated_mod.get_global_var('func_1141')
call_8020 = relay.TupleGetItem(func_1140_call(), 0)
call_8021 = relay.TupleGetItem(func_1141_call(), 0)
output = call_8020
output2 = call_8021
func_8022 = relay.Function([], output)
mod['func_8022'] = func_8022
mod = relay.transform.InferType()(mod)
mutated_mod['func_8022'] = func_8022
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8022_call = mutated_mod.get_global_var('func_8022')
call_8023 = func_8022_call()
output = call_8023
func_8024 = relay.Function([], output)
mutated_mod['func_8024'] = func_8024
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1603_call = mod.get_global_var('func_1603')
func_1604_call = mutated_mod.get_global_var('func_1604')
call_8059 = relay.TupleGetItem(func_1603_call(), 0)
call_8060 = relay.TupleGetItem(func_1604_call(), 0)
func_7689_call = mod.get_global_var('func_7689')
func_7690_call = mutated_mod.get_global_var('func_7690')
call_8061 = relay.TupleGetItem(func_7689_call(), 0)
call_8062 = relay.TupleGetItem(func_7690_call(), 0)
func_1178_call = mod.get_global_var('func_1178')
func_1180_call = mutated_mod.get_global_var('func_1180')
call_8080 = func_1178_call()
call_8081 = func_1178_call()
func_8017_call = mod.get_global_var('func_8017')
func_8019_call = mutated_mod.get_global_var('func_8019')
call_8095 = func_8017_call()
call_8096 = func_8017_call()
func_759_call = mod.get_global_var('func_759')
func_761_call = mutated_mod.get_global_var('func_761')
const_8118 = relay.const([-5,-1,-1,4,1,-7,9,-1,-5,-5,-10,10,-5,-8,-8,-2,-7,5,-4,-6,-3,7,8,-2,4,9,-4,-1,-7,-2,3,-6,-6,8,10,-3,8,-2,-2,9,-6,2,-7,-3,-10,-7,-8,5,6,2,-9,8,6,2,-8,6,1,-6,-8,3,1,-3,5,-2,3,-6,10,-10,5,6,4,7,-9,2,-1,7,4,-2,-10,-1,-10,-7,-2,9,-8,-3,9,6,3,5,-4,8,2,9,4,-7,9,-5,1,-10], dtype = "uint32")#candidate|8118|(100,)|const|uint32
call_8117 = relay.TupleGetItem(func_759_call(relay.reshape(const_8118.astype('uint32'), [5, 4, 5])), 0)
call_8119 = relay.TupleGetItem(func_761_call(relay.reshape(const_8118.astype('uint32'), [5, 4, 5])), 0)
output = relay.Tuple([call_8059,call_8061,call_8080,call_8095,call_8117,const_8118,])
output2 = relay.Tuple([call_8060,call_8062,call_8081,call_8096,call_8119,const_8118,])
func_8127 = relay.Function([], output)
mod['func_8127'] = func_8127
mod = relay.transform.InferType()(mod)
output = func_8127()
func_8128 = relay.Function([], output)
mutated_mod['func_8128'] = func_8128
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5763_call = mod.get_global_var('func_5763')
func_5764_call = mutated_mod.get_global_var('func_5764')
call_8173 = relay.TupleGetItem(func_5763_call(), 1)
call_8174 = relay.TupleGetItem(func_5764_call(), 1)
func_5020_call = mod.get_global_var('func_5020')
func_5023_call = mutated_mod.get_global_var('func_5023')
var_8180 = relay.var("var_8180", dtype = "float32", shape = (192,))#candidate|8180|(192,)|var|float32
call_8179 = relay.TupleGetItem(func_5020_call(relay.reshape(var_8180.astype('float32'), [6, 4, 8])), 0)
call_8181 = relay.TupleGetItem(func_5023_call(relay.reshape(var_8180.astype('float32'), [6, 4, 8])), 0)
func_1984_call = mod.get_global_var('func_1984')
func_1985_call = mutated_mod.get_global_var('func_1985')
call_8182 = relay.TupleGetItem(func_1984_call(), 1)
call_8183 = relay.TupleGetItem(func_1985_call(), 1)
func_4569_call = mod.get_global_var('func_4569')
func_4571_call = mutated_mod.get_global_var('func_4571')
var_8201 = relay.var("var_8201", dtype = "bool", shape = (900,))#candidate|8201|(900,)|var|bool
call_8200 = relay.TupleGetItem(func_4569_call(relay.reshape(var_8201.astype('bool'), [15, 10, 6])), 0)
call_8202 = relay.TupleGetItem(func_4571_call(relay.reshape(var_8201.astype('bool'), [15, 10, 6])), 0)
func_6494_call = mod.get_global_var('func_6494')
func_6495_call = mutated_mod.get_global_var('func_6495')
call_8207 = relay.TupleGetItem(func_6494_call(), 0)
call_8208 = relay.TupleGetItem(func_6495_call(), 0)
uop_8214 = relay.sin(call_8179.astype('float32')) # shape=(6, 4, 8)
uop_8216 = relay.sin(call_8181.astype('float32')) # shape=(6, 4, 8)
func_994_call = mod.get_global_var('func_994')
func_997_call = mutated_mod.get_global_var('func_997')
const_8223 = relay.const([-4.152443,-3.594392,4.546914,-0.931948,8.586176,3.259305,-1.215504,6.441084,-3.712029,-0.825797,3.685855,6.242668,-2.691518,-1.060296,-9.407429,2.857937,-7.151100,3.934702,2.427270,6.127160,7.764950,7.233561,-0.911318,-9.227685,2.746873,0.975347,3.962604,-6.298533,-9.343730,-4.980731,-3.749856,-0.493195,4.815303,-6.837759,1.586558,-2.513178,-9.435637,2.267163,-8.665096,-1.253425,-2.987177,0.088004,-1.688721,5.307794,-1.628345,2.153024,-8.142334,7.013432], dtype = "float32")#candidate|8223|(48,)|const|float32
call_8222 = relay.TupleGetItem(func_994_call(relay.reshape(const_8223.astype('float32'), [6, 1, 8])), 1)
call_8224 = relay.TupleGetItem(func_997_call(relay.reshape(const_8223.astype('float32'), [6, 1, 8])), 1)
output = relay.Tuple([call_8173,var_8180,call_8182,call_8200,var_8201,call_8207,uop_8214,call_8222,const_8223,])
output2 = relay.Tuple([call_8174,var_8180,call_8183,call_8202,var_8201,call_8208,uop_8216,call_8224,const_8223,])
func_8247 = relay.Function([var_8180,var_8201,], output)
mod['func_8247'] = func_8247
mod = relay.transform.InferType()(mod)
mutated_mod['func_8247'] = func_8247
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8247_call = mutated_mod.get_global_var('func_8247')
var_8249 = relay.var("var_8249", dtype = "float32", shape = (192,))#candidate|8249|(192,)|var|float32
var_8250 = relay.var("var_8250", dtype = "bool", shape = (900,))#candidate|8250|(900,)|var|bool
call_8248 = func_8247_call(var_8249,var_8250,)
output = call_8248
func_8251 = relay.Function([var_8249,var_8250,], output)
mutated_mod['func_8251'] = func_8251
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1920_call = mod.get_global_var('func_1920')
func_1922_call = mutated_mod.get_global_var('func_1922')
call_8263 = relay.TupleGetItem(func_1920_call(), 0)
call_8264 = relay.TupleGetItem(func_1922_call(), 0)
output = relay.Tuple([call_8263,])
output2 = relay.Tuple([call_8264,])
func_8276 = relay.Function([], output)
mod['func_8276'] = func_8276
mod = relay.transform.InferType()(mod)
mutated_mod['func_8276'] = func_8276
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8276_call = mutated_mod.get_global_var('func_8276')
call_8277 = func_8276_call()
output = call_8277
func_8278 = relay.Function([], output)
mutated_mod['func_8278'] = func_8278
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1187_call = mod.get_global_var('func_1187')
func_1188_call = mutated_mod.get_global_var('func_1188')
call_8339 = relay.TupleGetItem(func_1187_call(), 0)
call_8340 = relay.TupleGetItem(func_1188_call(), 0)
func_3925_call = mod.get_global_var('func_3925')
func_3926_call = mutated_mod.get_global_var('func_3926')
call_8348 = relay.TupleGetItem(func_3925_call(), 0)
call_8349 = relay.TupleGetItem(func_3926_call(), 0)
func_2401_call = mod.get_global_var('func_2401')
func_2402_call = mutated_mod.get_global_var('func_2402')
call_8351 = relay.TupleGetItem(func_2401_call(), 1)
call_8352 = relay.TupleGetItem(func_2402_call(), 1)
output = relay.Tuple([call_8339,call_8348,call_8351,])
output2 = relay.Tuple([call_8340,call_8349,call_8352,])
func_8355 = relay.Function([], output)
mod['func_8355'] = func_8355
mod = relay.transform.InferType()(mod)
output = func_8355()
func_8356 = relay.Function([], output)
mutated_mod['func_8356'] = func_8356
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8374 = relay.var("var_8374", dtype = "float64", shape = (11, 4, 14))#candidate|8374|(11, 4, 14)|var|float64
uop_8375 = relay.asin(var_8374.astype('float64')) # shape=(11, 4, 14)
uop_8383 = relay.acosh(uop_8375.astype('float64')) # shape=(11, 4, 14)
output = uop_8383
output2 = uop_8383
func_8385 = relay.Function([var_8374,], output)
mod['func_8385'] = func_8385
mod = relay.transform.InferType()(mod)
var_8386 = relay.var("var_8386", dtype = "float64", shape = (11, 4, 14))#candidate|8386|(11, 4, 14)|var|float64
output = func_8385(var_8386)
func_8387 = relay.Function([var_8386], output)
mutated_mod['func_8387'] = func_8387
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3533_call = mod.get_global_var('func_3533')
func_3534_call = mutated_mod.get_global_var('func_3534')
call_8403 = relay.TupleGetItem(func_3533_call(), 0)
call_8404 = relay.TupleGetItem(func_3534_call(), 0)
output = relay.Tuple([call_8403,])
output2 = relay.Tuple([call_8404,])
func_8405 = relay.Function([], output)
mod['func_8405'] = func_8405
mod = relay.transform.InferType()(mod)
mutated_mod['func_8405'] = func_8405
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8405_call = mutated_mod.get_global_var('func_8405')
call_8406 = func_8405_call()
output = call_8406
func_8407 = relay.Function([], output)
mutated_mod['func_8407'] = func_8407
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7689_call = mod.get_global_var('func_7689')
func_7690_call = mutated_mod.get_global_var('func_7690')
call_8494 = relay.TupleGetItem(func_7689_call(), 0)
call_8495 = relay.TupleGetItem(func_7690_call(), 0)
uop_8501 = relay.log10(call_8494.astype('float64')) # shape=(16, 11, 12)
uop_8503 = relay.log10(call_8495.astype('float64')) # shape=(16, 11, 12)
func_5392_call = mod.get_global_var('func_5392')
func_5394_call = mutated_mod.get_global_var('func_5394')
call_8518 = relay.TupleGetItem(func_5392_call(), 0)
call_8519 = relay.TupleGetItem(func_5394_call(), 0)
func_386_call = mod.get_global_var('func_386')
func_389_call = mutated_mod.get_global_var('func_389')
const_8523 = relay.const([-7.136212,5.014979,-0.734190,7.030654,0.536112,3.263629,-5.935960,5.656870,-3.301072,-6.049018,4.462876,-1.303668,-0.400148,-7.214390,-3.515030,0.349310], dtype = "float64")#candidate|8523|(16,)|const|float64
var_8524 = relay.var("var_8524", dtype = "int64", shape = ())#candidate|8524|()|var|int64
call_8522 = relay.TupleGetItem(func_386_call(relay.reshape(const_8523.astype('float64'), [1, 4, 4]), relay.reshape(var_8524.astype('int64'), []), ), 1)
call_8525 = relay.TupleGetItem(func_389_call(relay.reshape(const_8523.astype('float64'), [1, 4, 4]), relay.reshape(var_8524.astype('int64'), []), ), 1)
func_1859_call = mod.get_global_var('func_1859')
func_1861_call = mutated_mod.get_global_var('func_1861')
call_8537 = relay.TupleGetItem(func_1859_call(), 0)
call_8538 = relay.TupleGetItem(func_1861_call(), 0)
func_2863_call = mod.get_global_var('func_2863')
func_2865_call = mutated_mod.get_global_var('func_2865')
call_8543 = relay.TupleGetItem(func_2863_call(), 0)
call_8544 = relay.TupleGetItem(func_2865_call(), 0)
output = relay.Tuple([uop_8501,call_8518,call_8522,const_8523,var_8524,call_8537,call_8543,])
output2 = relay.Tuple([uop_8503,call_8519,call_8525,const_8523,var_8524,call_8538,call_8544,])
func_8546 = relay.Function([var_8524,], output)
mod['func_8546'] = func_8546
mod = relay.transform.InferType()(mod)
var_8547 = relay.var("var_8547", dtype = "int64", shape = ())#candidate|8547|()|var|int64
output = func_8546(var_8547)
func_8548 = relay.Function([var_8547], output)
mutated_mod['func_8548'] = func_8548
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3670_call = mod.get_global_var('func_3670')
func_3672_call = mutated_mod.get_global_var('func_3672')
call_8563 = relay.TupleGetItem(func_3670_call(), 0)
call_8564 = relay.TupleGetItem(func_3672_call(), 0)
func_5951_call = mod.get_global_var('func_5951')
func_5952_call = mutated_mod.get_global_var('func_5952')
call_8595 = func_5951_call()
call_8596 = func_5951_call()
output = relay.Tuple([call_8563,call_8595,])
output2 = relay.Tuple([call_8564,call_8596,])
func_8617 = relay.Function([], output)
mod['func_8617'] = func_8617
mod = relay.transform.InferType()(mod)
mutated_mod['func_8617'] = func_8617
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8617_call = mutated_mod.get_global_var('func_8617')
call_8618 = func_8617_call()
output = call_8618
func_8619 = relay.Function([], output)
mutated_mod['func_8619'] = func_8619
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5634_call = mod.get_global_var('func_5634')
func_5635_call = mutated_mod.get_global_var('func_5635')
call_8644 = relay.TupleGetItem(func_5634_call(), 2)
call_8645 = relay.TupleGetItem(func_5635_call(), 2)
var_8646 = relay.var("var_8646", dtype = "float32", shape = (48, 14))#candidate|8646|(48, 14)|var|float32
bop_8647 = relay.maximum(call_8644.astype('uint64'), var_8646.astype('uint64')) # shape=(48, 14)
bop_8650 = relay.maximum(call_8645.astype('uint64'), var_8646.astype('uint64')) # shape=(48, 14)
output = relay.Tuple([bop_8647,])
output2 = relay.Tuple([bop_8650,])
func_8652 = relay.Function([var_8646,], output)
mod['func_8652'] = func_8652
mod = relay.transform.InferType()(mod)
mutated_mod['func_8652'] = func_8652
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8653 = relay.var("var_8653", dtype = "float32", shape = (48, 14))#candidate|8653|(48, 14)|var|float32
func_8652_call = mutated_mod.get_global_var('func_8652')
call_8654 = func_8652_call(var_8653)
output = call_8654
func_8655 = relay.Function([var_8653], output)
mutated_mod['func_8655'] = func_8655
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4057_call = mod.get_global_var('func_4057')
func_4058_call = mutated_mod.get_global_var('func_4058')
call_8675 = relay.TupleGetItem(func_4057_call(), 1)
call_8676 = relay.TupleGetItem(func_4058_call(), 1)
output = call_8675
output2 = call_8676
func_8682 = relay.Function([], output)
mod['func_8682'] = func_8682
mod = relay.transform.InferType()(mod)
mutated_mod['func_8682'] = func_8682
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8682_call = mutated_mod.get_global_var('func_8682')
call_8683 = func_8682_call()
output = call_8683
func_8684 = relay.Function([], output)
mutated_mod['func_8684'] = func_8684
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7540_call = mod.get_global_var('func_7540')
func_7542_call = mutated_mod.get_global_var('func_7542')
call_8706 = relay.TupleGetItem(func_7540_call(), 1)
call_8707 = relay.TupleGetItem(func_7542_call(), 1)
func_2956_call = mod.get_global_var('func_2956')
func_2959_call = mutated_mod.get_global_var('func_2959')
const_8710 = relay.const([-1,10,-7,-10,-4,-1,-10,-10,7,-7,-4,2,-4,-8,-2,-2,-6,-8,7,-1,9,-9,-10,4,-8,-8,-5,2,5,10,-5,-10,-5,5,-8,-4,-2,-10,3,-2,4,3,2,9,-3,3,-3,10,5,1,-6,2,9,10,3,5,2,9,3,-9,8,6,-9,9,-4,5,7,-7,9,-10,-9,-2,-3,5,10,2,-10,-9,-5,-10,1,8,-5,6,-10,8,3,2,-10,2,3,-8,-4,-9,-7,9,-8,-6,10,7,-8,1,5,-9,-10,-5,-7,-5,9,-10,-5,-6,6,6,-4,7,-7,5,-4,7,5,7,4,-3,-6,-1,3,-3,-9,-4,1,-9,2,10,-10,9,8,7,10,5,6,8,-3,-10,-10,-7,8,1,2,5,8,-7,-10,6,-6,-7,-7,2,7,-4,6,10,-9,-3,2,-1,10,5,-2,-1,2,-9,-6,-10,-2,-2,8,-2,2,-6,-3,-5,2,-4,-10,3,4,4,-4,3,-9,-6,-6,1,-6,-4,-3,2,8,-2,-1,-4,-6,5,1,7,4,6,-4,9,6,-8,2,-6,4,-1,-2,9,1,9,-5,-5,-4,6,10,9,-9,-6,-7,-1,10,-5,7,2,2,-4,-2,4,2,3,7,9,-8,-9,7,5,4,-2,6,2,7,-4,5,-4,-2,-8,-8,-7,1,-1,-5,-10,6,1,7,-1,9,5,5,-2,6,-6,-8,3,8,-2,8,-4,-3,6,8,8,3,3,3,-7,-7,7,5,-5,-2,5,-8,-4,-4,2,-8,-1,-2,-2,-2,-7,-9,2,-2,6,3,-4,10,1,8,8,-4,8,-5,-4,-9,-6,3,4,-9,9,-2,5,3,-8,1,-7,-6,2,7,-10,7,7,-8,-7,-1,-10,-1,7,-1,3,10,7,-8,9,7,4,-9,-3,-1,-5,7,7,8,-10,-8,1,6,6,-8,-1,-8,8,7,-6,10,-3,5,-4,4,2,-8,2,2,10,-4,-7,-6,-10,6,3,7,2,-8,5,-10,-5,-1,-4,4,-6,-3,-1,-10,3,-8,2,2,5,2,-1,-6,-3,-3,1,9,6,-10,2,-9,-6,1,2,5,1,-7,2,-9,4,3,7,-3,-5,-1,3,-2,-9,-8,-6,8,2,10,-1,-10,10,10,-5,-2,6,-7,-5,1,-4,5,-3,9,-8,-9,9,6,3,7,-9,-10,4,7,8,5,6,-2,-5,-6,2,-4,7,8,-5,9,6,2,-7,-9,-6,9,-6,-3,-3,-4,4,-4,9,10,7,-10,1,2,1,-4,-8,1,5,-5,-10,-1,-8,-5,7,10,7,8,4,-7,-3,-3,4,-7,7,7,-10,4,-3,6,6,-7,-8,10,-5,8,-8,1,5,10,9,-9,-6,-8,2,1,9,-3,-3,10,10,7,1,9,-5,9,-6,4,1,-3,5,-3,1,3,8,3,-5,5,10,3,-5,-9,1,5,5,-7,1,7,7,-6,-5,-3,9,6,4,-5,2,-3,7,-6,-7,5,6,-10,1,-6,-2,5,-8,1,2,2,9,-8,-3,-3,9,8,9,8,1,4,-4,-5,2,4,-1,8,4,-8,-2,7,8,-9,-3,-7,-1,-10,-2,7,2,-9,-10,4,-5,-2,5,8,-7,2,-4,-6,2,7,-2,1,8,8,-7,3,-7,8,-4,-7,5,-3,-10,1,-5,-7,5,-3,-8,-2,-5,6,9,4,-2,6,-2,-6,6,-4,8,-1,1,-9,-7,3,-7,4,5,-9,10,-6,-4,7,-10,2,4,2,-9,4,1,8,8,-3,-1,-10,8,5,8,2,5,-5,-9,-6,-5,4,8,3,-3,9,-9,-5,4,-8,2,-2,6,-5,4,5,2,5,-1,-5,5,6,-2,-10,1,-1,-10,7,10,-4,3,-4,-7,4,9,2,-3,7,-1,4,-7,-4,-7,6,5,2,9,3,-6,6,10,1,-8,9,-7,1,7,2,6,-3,-10,-9,2,-7,-2,-4,-10,-4,-3,-8,-7,4,-4,-1,-4,1,1,3,1,2,2,6,10,10,4,-4,9,-4,-4,-3,-1,-4,-4,6,6,9,-3,-10,6,10,10,-10,4,1,-10,8,-9,-2,1,6,-5,9,-3,-4,-1,-6,8,9,9,10,4,-9,-2,6,8,-5,1,2,3,1,-10,-4,-3,10,6,-1,10,5,-2,7,3,4,8,-5,4,4,3,2,-4,9,-4,10,2,-6,-6,-4,-9,-2,6,7,-5,4,10,7,-10,-3,7,-8,1,-1,1,8,6,4,-1,-10,3,-8,9,6,-2,-4,6,-5,-8,-6,6,8,7,-1,-4,-7,-6,9,-10,5,-5,10,2,8,6,10,1,-3,1,-9,7,-3,2], dtype = "int8")#candidate|8710|(900,)|const|int8
call_8709 = relay.TupleGetItem(func_2956_call(relay.reshape(const_8710.astype('int8'), [900,])), 1)
call_8711 = relay.TupleGetItem(func_2959_call(relay.reshape(const_8710.astype('int8'), [900,])), 1)
func_8617_call = mod.get_global_var('func_8617')
func_8619_call = mutated_mod.get_global_var('func_8619')
call_8715 = relay.TupleGetItem(func_8617_call(), 0)
call_8716 = relay.TupleGetItem(func_8619_call(), 0)
func_8276_call = mod.get_global_var('func_8276')
func_8278_call = mutated_mod.get_global_var('func_8278')
call_8725 = relay.TupleGetItem(func_8276_call(), 0)
call_8726 = relay.TupleGetItem(func_8278_call(), 0)
func_4837_call = mod.get_global_var('func_4837')
func_4838_call = mutated_mod.get_global_var('func_4838')
call_8729 = relay.TupleGetItem(func_4837_call(), 0)
call_8730 = relay.TupleGetItem(func_4838_call(), 0)
output = relay.Tuple([call_8706,call_8709,const_8710,call_8715,call_8725,call_8729,])
output2 = relay.Tuple([call_8707,call_8711,const_8710,call_8716,call_8726,call_8730,])
func_8736 = relay.Function([], output)
mod['func_8736'] = func_8736
mod = relay.transform.InferType()(mod)
output = func_8736()
func_8737 = relay.Function([], output)
mutated_mod['func_8737'] = func_8737
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1984_call = mod.get_global_var('func_1984')
func_1985_call = mutated_mod.get_global_var('func_1985')
call_8864 = relay.TupleGetItem(func_1984_call(), 0)
call_8865 = relay.TupleGetItem(func_1985_call(), 0)
var_8872 = relay.var("var_8872", dtype = "int64", shape = (3, 3, 3))#candidate|8872|(3, 3, 3)|var|int64
bop_8873 = relay.add(call_8864.astype('uint8'), var_8872.astype('uint8')) # shape=(3, 3, 3)
bop_8876 = relay.add(call_8865.astype('uint8'), var_8872.astype('uint8')) # shape=(3, 3, 3)
func_7821_call = mod.get_global_var('func_7821')
func_7824_call = mutated_mod.get_global_var('func_7824')
var_8885 = relay.var("var_8885", dtype = "float32", shape = (1960,))#candidate|8885|(1960,)|var|float32
var_8886 = relay.var("var_8886", dtype = "float32", shape = (700,))#candidate|8886|(700,)|var|float32
call_8884 = relay.TupleGetItem(func_7821_call(relay.reshape(var_8885.astype('float32'), [14, 14, 10]), relay.reshape(var_8886.astype('float32'), [14, 5, 10]), ), 0)
call_8887 = relay.TupleGetItem(func_7824_call(relay.reshape(var_8885.astype('float32'), [14, 14, 10]), relay.reshape(var_8886.astype('float32'), [14, 5, 10]), ), 0)
output = relay.Tuple([bop_8873,call_8884,var_8885,var_8886,])
output2 = relay.Tuple([bop_8876,call_8887,var_8885,var_8886,])
func_8892 = relay.Function([var_8872,var_8885,var_8886,], output)
mod['func_8892'] = func_8892
mod = relay.transform.InferType()(mod)
var_8893 = relay.var("var_8893", dtype = "int64", shape = (3, 3, 3))#candidate|8893|(3, 3, 3)|var|int64
var_8894 = relay.var("var_8894", dtype = "float32", shape = (1960,))#candidate|8894|(1960,)|var|float32
var_8895 = relay.var("var_8895", dtype = "float32", shape = (700,))#candidate|8895|(700,)|var|float32
output = func_8892(var_8893,var_8894,var_8895,)
func_8896 = relay.Function([var_8893,var_8894,var_8895,], output)
mutated_mod['func_8896'] = func_8896
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1801_call = mod.get_global_var('func_1801')
func_1803_call = mutated_mod.get_global_var('func_1803')
call_8941 = func_1801_call()
call_8942 = func_1801_call()
func_2243_call = mod.get_global_var('func_2243')
func_2245_call = mutated_mod.get_global_var('func_2245')
const_8992 = relay.const([0.369060,-1.300608,-6.423222,3.662819,-6.817887,-5.924420,-5.751393,7.506412,1.826790,4.892841,-9.038030,-8.534267,-5.565294,-8.449578,-9.973748,-7.911289,0.896531,7.411025,4.949668,-5.821097,-2.677139,6.317794,-1.601484,-3.578190,4.531620,-7.275949,-6.666212,-5.639469,-3.068807,1.640684,-7.798630,-9.708332,-8.041019,6.166314,-5.620141,9.771302,-3.456788,-0.518704,3.468640,4.900269,-8.788770,-2.322012,-1.570231,-7.669748,9.346697,3.505330,9.676224,-7.219960], dtype = "float32")#candidate|8992|(48,)|const|float32
call_8991 = relay.TupleGetItem(func_2243_call(relay.reshape(const_8992.astype('float32'), [48,])), 2)
call_8993 = relay.TupleGetItem(func_2245_call(relay.reshape(const_8992.astype('float32'), [48,])), 2)
func_4057_call = mod.get_global_var('func_4057')
func_4058_call = mutated_mod.get_global_var('func_4058')
call_9018 = relay.TupleGetItem(func_4057_call(), 0)
call_9019 = relay.TupleGetItem(func_4058_call(), 0)
output = relay.Tuple([call_8941,call_8991,const_8992,call_9018,])
output2 = relay.Tuple([call_8942,call_8993,const_8992,call_9019,])
func_9036 = relay.Function([], output)
mod['func_9036'] = func_9036
mod = relay.transform.InferType()(mod)
output = func_9036()
func_9037 = relay.Function([], output)
mutated_mod['func_9037'] = func_9037
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4319_call = mod.get_global_var('func_4319')
func_4320_call = mutated_mod.get_global_var('func_4320')
call_9038 = relay.TupleGetItem(func_4319_call(), 0)
call_9039 = relay.TupleGetItem(func_4320_call(), 0)
output = relay.Tuple([call_9038,])
output2 = relay.Tuple([call_9039,])
func_9048 = relay.Function([], output)
mod['func_9048'] = func_9048
mod = relay.transform.InferType()(mod)
output = func_9048()
func_9049 = relay.Function([], output)
mutated_mod['func_9049'] = func_9049
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5392_call = mod.get_global_var('func_5392')
func_5394_call = mutated_mod.get_global_var('func_5394')
call_9055 = relay.TupleGetItem(func_5392_call(), 0)
call_9056 = relay.TupleGetItem(func_5394_call(), 0)
func_8247_call = mod.get_global_var('func_8247')
func_8251_call = mutated_mod.get_global_var('func_8251')
const_9061 = relay.const([7.563562,0.694157,-5.135720,-0.520146,-8.302373,-1.658977,-2.180656,4.703397,9.689169,-8.930904,2.132184,8.546381,-0.786914,-8.600943,7.344298,-9.955071,-0.721988,-2.083876,5.619431,-8.759220,7.537253,-6.184348,-6.262284,-7.141844,7.906197,9.316693,1.743228,-5.711687,6.069418,-3.663127,-6.202945,6.260904,-7.609851,6.045831,-0.477427,-4.091472,-9.122468,9.350604,-0.403185,4.188679,0.744735,-5.468257,4.095760,-2.280630,-4.303724,3.504716,0.376216,9.563067,-2.715370,1.761161,-0.154039,-2.125037,-0.966609,9.110974,7.573743,-7.354723,-3.186032,-7.498181,-1.643300,-5.613837,9.325106,4.923042,6.549349,-8.462785,-7.849708,-2.526079,4.759422,4.228696,8.793046,3.447085,8.352742,3.543725,-7.508378,2.349057,-5.974252,9.942621,-2.165583,-8.307507,8.135037,2.240314,5.667000,-6.094720,9.969967,-5.616926,0.807729,2.337962,-6.125584,-3.050453,-4.574656,8.546853,0.176025,-5.906338,6.964805,2.785055,-9.704854,-0.834552,9.303866,-5.898430,6.137418,7.558434,-3.678738,0.478656,4.802333,-3.782430,-2.744381,-5.992121,-4.810134,3.126968,7.677828,1.357370,4.977495,7.693929,-5.005868,1.752273,9.216462,-6.076151,-1.164608,-3.356561,2.098161,1.456339,-1.405985,-5.792417,4.995314,-8.784271,-8.994470,-2.160804,-2.410829,-2.075595,2.316733,-2.275706,-5.915422,8.216404,-2.603100,-0.375416,-3.092849,4.562456,6.933364,4.449131,9.171635,-0.468237,3.499845,-5.805748,-4.235788,4.670139,-8.550288,-6.298393,-2.709088,7.847895,8.143278,1.970079,-2.805943,-6.776862,-1.232988,-2.418946,-3.866522,8.533802,8.501325,1.990641,9.091235,7.785018,-5.978907,-0.638996,1.966706,7.173970,-3.922609,-2.144474,-9.810198,-3.945709,9.303620,-2.187022,4.776574,6.290135,7.999401,0.828795,6.907270,9.988186,-7.093247,3.659515,0.450486,1.846193,9.073175,-0.460117,-8.345219,-5.615960,3.278234,6.217236,-3.695953,4.560045,1.834333,-3.401428,-8.077371,-2.075993], dtype = "float32")#candidate|9061|(192,)|const|float32
var_9062 = relay.var("var_9062", dtype = "bool", shape = (900, 1))#candidate|9062|(900, 1)|var|bool
call_9060 = relay.TupleGetItem(func_8247_call(relay.reshape(const_9061.astype('float32'), [192,]), relay.reshape(var_9062.astype('bool'), [900,]), ), 8)
call_9063 = relay.TupleGetItem(func_8251_call(relay.reshape(const_9061.astype('float32'), [192,]), relay.reshape(var_9062.astype('bool'), [900,]), ), 8)
func_5379_call = mod.get_global_var('func_5379')
func_5380_call = mutated_mod.get_global_var('func_5380')
call_9066 = func_5379_call()
call_9067 = func_5379_call()
func_1178_call = mod.get_global_var('func_1178')
func_1180_call = mutated_mod.get_global_var('func_1180')
call_9068 = func_1178_call()
call_9069 = func_1178_call()
func_386_call = mod.get_global_var('func_386')
func_389_call = mutated_mod.get_global_var('func_389')
var_9084 = relay.var("var_9084", dtype = "float64", shape = (16,))#candidate|9084|(16,)|var|float64
const_9085 = relay.const(7, dtype = "int64")#candidate|9085|()|const|int64
call_9083 = relay.TupleGetItem(func_386_call(relay.reshape(var_9084.astype('float64'), [1, 4, 4]), relay.reshape(const_9085.astype('int64'), []), ), 0)
call_9086 = relay.TupleGetItem(func_389_call(relay.reshape(var_9084.astype('float64'), [1, 4, 4]), relay.reshape(const_9085.astype('int64'), []), ), 0)
output = relay.Tuple([call_9055,call_9060,const_9061,var_9062,call_9066,call_9068,call_9083,var_9084,const_9085,])
output2 = relay.Tuple([call_9056,call_9063,const_9061,var_9062,call_9067,call_9069,call_9086,var_9084,const_9085,])
func_9105 = relay.Function([var_9062,var_9084,], output)
mod['func_9105'] = func_9105
mod = relay.transform.InferType()(mod)
var_9106 = relay.var("var_9106", dtype = "bool", shape = (900, 1))#candidate|9106|(900, 1)|var|bool
var_9107 = relay.var("var_9107", dtype = "float64", shape = (16,))#candidate|9107|(16,)|var|float64
output = func_9105(var_9106,var_9107,)
func_9108 = relay.Function([var_9106,var_9107,], output)
mutated_mod['func_9108'] = func_9108
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8405_call = mod.get_global_var('func_8405')
func_8407_call = mutated_mod.get_global_var('func_8407')
call_9113 = relay.TupleGetItem(func_8405_call(), 0)
call_9114 = relay.TupleGetItem(func_8407_call(), 0)
func_5924_call = mod.get_global_var('func_5924')
func_5927_call = mutated_mod.get_global_var('func_5927')
const_9127 = relay.const(-2, dtype = "uint16")#candidate|9127|()|const|uint16
const_9128 = relay.const([-2,-6,-5,2,6,2,8,-2,-6,8,9,2,-5,-7,7,2,10,6,6,1,1,-1,5,5,-10,-3,8,-8,6,-10,1,2,1,-9,7,8,-1,-6,2,10,-4,-2], dtype = "uint16")#candidate|9128|(42,)|const|uint16
call_9126 = relay.TupleGetItem(func_5924_call(relay.reshape(const_9127.astype('uint16'), []), relay.reshape(const_9128.astype('uint16'), [7, 6, 1]), ), 2)
call_9129 = relay.TupleGetItem(func_5927_call(relay.reshape(const_9127.astype('uint16'), []), relay.reshape(const_9128.astype('uint16'), [7, 6, 1]), ), 2)
func_4319_call = mod.get_global_var('func_4319')
func_4320_call = mutated_mod.get_global_var('func_4320')
call_9130 = relay.TupleGetItem(func_4319_call(), 0)
call_9131 = relay.TupleGetItem(func_4320_call(), 0)
output = relay.Tuple([call_9113,call_9126,const_9127,const_9128,call_9130,])
output2 = relay.Tuple([call_9114,call_9129,const_9127,const_9128,call_9131,])
func_9135 = relay.Function([], output)
mod['func_9135'] = func_9135
mod = relay.transform.InferType()(mod)
mutated_mod['func_9135'] = func_9135
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9135_call = mutated_mod.get_global_var('func_9135')
call_9136 = func_9135_call()
output = call_9136
func_9137 = relay.Function([], output)
mutated_mod['func_9137'] = func_9137
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8405_call = mod.get_global_var('func_8405')
func_8407_call = mutated_mod.get_global_var('func_8407')
call_9266 = relay.TupleGetItem(func_8405_call(), 0)
call_9267 = relay.TupleGetItem(func_8407_call(), 0)
func_7659_call = mod.get_global_var('func_7659')
func_7664_call = mutated_mod.get_global_var('func_7664')
const_9289 = relay.const([-2,-10,9,7,-4,1,-7,6,4,5,-8,9,-10,4,-4,4,7,-10,3,-10,-4,8,7,9,7,-5,8,6,2,6,6,10,7,10,9,7,-2,-7,3,8,-9,-7,-6,7,-3,-4,6,-2,5,-2,-3,-6,-6,-2,10,-8,-5,-7,8,-1,-10,1,10,-6,-7,-7,-7,-3,-7,-1,5,7,-4,2,-10,-4,9,-6,-1,2,-1,6,2,-1,4,-8,-1,10,-1,9,7,-2,1,3,-10,-7,6,1,3,-8,3,-10,3,2,-4,5,-6,-8,-7,-8,8,10,-9,1,-2,-2,7,1,-2,3,-6,7,-9,1,-6,5,-4,-5,7,-8,-6,-5,-2,2,1,-2,-6,-9,4,1,8,-3,2,-7,5,-9,6,4,2,4,1,-8,-4,2,-8,-7,8,1,9,10,-5,-7,-4,-1,-6,8,2,4,5,-6,-8,9,5,7,-10,-10,-7,6,-7,-6,1,-10,-9,10,2,-7,9,8,8,9,-4,10,5,3,-2,-5,-4,-7,1,9,3,4,3,-5,-7,8,-3,-5,6,-10,-8,5,-2,-6,-10,-6,10,5,2,-6,-4,2,-7,-8,6,5,-5,-7,3,-9,8,-7,7,-4,4,8,8,-7,-1,-10,-3,1,3,6,-1,8,2,10,7,-8,5,9,8,-8,1,5,3,3,-6,-2,5,6,5,-7,-1,-3,3,-2,10,-1,10,-6,-4,6,9,6,-8,-3,10,5,-7,10,10,2,-3,-10,8,3,6,-9,9,-9,10,2,-4,-3,-3,10,6,1,4,10,7,2,-7,8,-8,7,-1,-10,-3,-5,-8,2,-6,1,6,9,-9,9,-4,5,4,-2,8,9,6,2,6,8,-6,-3,4,-6,-5,-2,1,-2,9,9,9,1,-9,-1,-4,10,-2,2,5,1,-4,8,10,10,6,-7,7,-10,10,5,2,7,6,-10,-9,10,5,9,-10,5,10,2,-1,-6,-6,8,-6,-2,4,5,4,-9,5,-6,-8,-10,-4,-6,5,-9,-4,-10,2,5,5,-3,5,-2,1,5,9,-10,10,-2,-9,-7,-8,3,1,7,-8,-7,-2,5,-6,-7,-8,2,4,-4,-2,7,-9,9,-10,6,-7,-3,3,-6,-8,6,9,-5,-9,-5,-9,-3,3,-10,8,-1,10,-8,1,4,7,5,-7,9,9,-10,-6,-9,-5,-4,-7,-2,8,-4,5,8,7,10,-6,-1,-2,-5,4,-9,-5,3,-7,-10,4,4,1,1,-9,-1,9,10,-5,-2,-1,9,4,-9,-7,-8,3,2,5,-2,-4,1,-9,7,-8,-4,-1,-8,-6,-8,5,6,9,4,1,10,2,-1,2,6,8,-2,6,-6,4,5,-9,1,-9,3,4,-7,5,-9,7,-1,-9,4,1,-6,-3,6,4,-1,4,-2,9,7,7,-3,1,-9,-6,-4,4,-4,4,10,-9,8,-5,4,-2,-8,-6,5,-6,8,9,1,-5,-2,-6,5,-1,1,-7,-2,7,-8,-2,10,7,-3,1,10,8,-5,4,10,-4,3,-5,8,4,4,-9,5,-2,10,2,-1,4,7,-5,3,-7,1,-1,3,-7,1,-1,9,7,-9,3,-1,4,-5,4,-8,-6,2,-10,-3,2,-10,-4,-6,-10,10,-3,-2,-1,-7,7,-8,4,2,-7,-10,1,-1,3,-6,2,-8,-10,-3,-9,8,6,9,-5,6,6,-10,8,-1,-1,-5,4,-8,-4,-7], dtype = "uint64")#candidate|9289|(660,)|const|uint64
var_9290 = relay.var("var_9290", dtype = "float32", shape = (960,))#candidate|9290|(960,)|var|float32
call_9288 = relay.TupleGetItem(func_7659_call(relay.reshape(const_9289.astype('uint64'), [15, 11, 4]), relay.reshape(const_9289.astype('uint64'), [15, 11, 4]), relay.reshape(var_9290.astype('float32'), [10, 96]), ), 0)
call_9291 = relay.TupleGetItem(func_7664_call(relay.reshape(const_9289.astype('uint64'), [15, 11, 4]), relay.reshape(const_9289.astype('uint64'), [15, 11, 4]), relay.reshape(var_9290.astype('float32'), [10, 96]), ), 0)
output = relay.Tuple([call_9266,call_9288,const_9289,var_9290,])
output2 = relay.Tuple([call_9267,call_9291,const_9289,var_9290,])
func_9292 = relay.Function([var_9290,], output)
mod['func_9292'] = func_9292
mod = relay.transform.InferType()(mod)
var_9293 = relay.var("var_9293", dtype = "float32", shape = (960,))#candidate|9293|(960,)|var|float32
output = func_9292(var_9293)
func_9294 = relay.Function([var_9293], output)
mutated_mod['func_9294'] = func_9294
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6624_call = mod.get_global_var('func_6624')
func_6626_call = mutated_mod.get_global_var('func_6626')
call_9448 = relay.TupleGetItem(func_6624_call(), 0)
call_9449 = relay.TupleGetItem(func_6626_call(), 0)
output = relay.Tuple([call_9448,])
output2 = relay.Tuple([call_9449,])
func_9457 = relay.Function([], output)
mod['func_9457'] = func_9457
mod = relay.transform.InferType()(mod)
mutated_mod['func_9457'] = func_9457
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9457_call = mutated_mod.get_global_var('func_9457')
call_9458 = func_9457_call()
output = call_9458
func_9459 = relay.Function([], output)
mutated_mod['func_9459'] = func_9459
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9457_call = mod.get_global_var('func_9457')
func_9459_call = mutated_mod.get_global_var('func_9459')
call_9465 = relay.TupleGetItem(func_9457_call(), 0)
call_9466 = relay.TupleGetItem(func_9459_call(), 0)
func_6503_call = mod.get_global_var('func_6503')
func_6504_call = mutated_mod.get_global_var('func_6504')
call_9475 = relay.TupleGetItem(func_6503_call(), 0)
call_9476 = relay.TupleGetItem(func_6504_call(), 0)
output = relay.Tuple([call_9465,call_9475,])
output2 = relay.Tuple([call_9466,call_9476,])
func_9477 = relay.Function([], output)
mod['func_9477'] = func_9477
mod = relay.transform.InferType()(mod)
output = func_9477()
func_9478 = relay.Function([], output)
mutated_mod['func_9478'] = func_9478
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8022_call = mod.get_global_var('func_8022')
func_8024_call = mutated_mod.get_global_var('func_8024')
call_9512 = func_8022_call()
call_9513 = func_8022_call()
var_9521 = relay.var("var_9521", dtype = "float32", shape = (14, 12, 10))#candidate|9521|(14, 12, 10)|var|float32
bop_9522 = relay.logical_xor(call_9512.astype('int64'), var_9521.astype('int64')) # shape=(14, 12, 10)
bop_9525 = relay.logical_xor(call_9513.astype('int64'), var_9521.astype('int64')) # shape=(14, 12, 10)
func_6123_call = mod.get_global_var('func_6123')
func_6125_call = mutated_mod.get_global_var('func_6125')
call_9534 = relay.TupleGetItem(func_6123_call(), 1)
call_9535 = relay.TupleGetItem(func_6125_call(), 1)
output = relay.Tuple([bop_9522,call_9534,])
output2 = relay.Tuple([bop_9525,call_9535,])
func_9552 = relay.Function([var_9521,], output)
mod['func_9552'] = func_9552
mod = relay.transform.InferType()(mod)
mutated_mod['func_9552'] = func_9552
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9553 = relay.var("var_9553", dtype = "float32", shape = (14, 12, 10))#candidate|9553|(14, 12, 10)|var|float32
func_9552_call = mutated_mod.get_global_var('func_9552')
call_9554 = func_9552_call(var_9553)
output = call_9554
func_9555 = relay.Function([var_9553], output)
mutated_mod['func_9555'] = func_9555
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8355_call = mod.get_global_var('func_8355')
func_8356_call = mutated_mod.get_global_var('func_8356')
call_9566 = relay.TupleGetItem(func_8355_call(), 2)
call_9567 = relay.TupleGetItem(func_8356_call(), 2)
func_7689_call = mod.get_global_var('func_7689')
func_7690_call = mutated_mod.get_global_var('func_7690')
call_9594 = relay.TupleGetItem(func_7689_call(), 0)
call_9595 = relay.TupleGetItem(func_7690_call(), 0)
func_6503_call = mod.get_global_var('func_6503')
func_6504_call = mutated_mod.get_global_var('func_6504')
call_9604 = relay.TupleGetItem(func_6503_call(), 0)
call_9605 = relay.TupleGetItem(func_6504_call(), 0)
bop_9613 = relay.bitwise_and(call_9566.astype('int16'), call_9604.astype('int16')) # shape=(15, 10, 6)
bop_9616 = relay.bitwise_and(call_9567.astype('int16'), call_9605.astype('int16')) # shape=(15, 10, 6)
func_3508_call = mod.get_global_var('func_3508')
func_3510_call = mutated_mod.get_global_var('func_3510')
call_9630 = func_3508_call()
call_9631 = func_3508_call()
output = relay.Tuple([call_9594,bop_9613,call_9630,])
output2 = relay.Tuple([call_9595,bop_9616,call_9631,])
func_9642 = relay.Function([], output)
mod['func_9642'] = func_9642
mod = relay.transform.InferType()(mod)
mutated_mod['func_9642'] = func_9642
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9642_call = mutated_mod.get_global_var('func_9642')
call_9643 = func_9642_call()
output = call_9643
func_9644 = relay.Function([], output)
mutated_mod['func_9644'] = func_9644
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6975_call = mod.get_global_var('func_6975')
func_6976_call = mutated_mod.get_global_var('func_6976')
call_9691 = func_6975_call()
call_9692 = func_6975_call()
func_5441_call = mod.get_global_var('func_5441')
func_5443_call = mutated_mod.get_global_var('func_5443')
call_9704 = func_5441_call()
call_9705 = func_5441_call()
output = relay.Tuple([call_9691,call_9704,])
output2 = relay.Tuple([call_9692,call_9705,])
func_9708 = relay.Function([], output)
mod['func_9708'] = func_9708
mod = relay.transform.InferType()(mod)
output = func_9708()
func_9709 = relay.Function([], output)
mutated_mod['func_9709'] = func_9709
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8682_call = mod.get_global_var('func_8682')
func_8684_call = mutated_mod.get_global_var('func_8684')
call_9820 = func_8682_call()
call_9821 = func_8682_call()
uop_9826 = relay.rsqrt(call_9820.astype('float64')) # shape=(45, 3)
uop_9828 = relay.rsqrt(call_9821.astype('float64')) # shape=(45, 3)
bop_9833 = relay.left_shift(call_9820.astype('int8'), relay.reshape(uop_9826.astype('int8'), relay.shape_of(call_9820))) # shape=(45, 3)
bop_9836 = relay.left_shift(call_9821.astype('int8'), relay.reshape(uop_9828.astype('int8'), relay.shape_of(call_9821))) # shape=(45, 3)
output = relay.Tuple([bop_9833,])
output2 = relay.Tuple([bop_9836,])
func_9838 = relay.Function([], output)
mod['func_9838'] = func_9838
mod = relay.transform.InferType()(mod)
mutated_mod['func_9838'] = func_9838
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9838_call = mutated_mod.get_global_var('func_9838')
call_9839 = func_9838_call()
output = call_9839
func_9840 = relay.Function([], output)
mutated_mod['func_9840'] = func_9840
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7689_call = mod.get_global_var('func_7689')
func_7690_call = mutated_mod.get_global_var('func_7690')
call_9896 = relay.TupleGetItem(func_7689_call(), 0)
call_9897 = relay.TupleGetItem(func_7690_call(), 0)
func_4504_call = mod.get_global_var('func_4504')
func_4508_call = mutated_mod.get_global_var('func_4508')
var_9899 = relay.var("var_9899", dtype = "float32", shape = (400,))#candidate|9899|(400,)|var|float32
var_9900 = relay.var("var_9900", dtype = "float32", shape = (24, 2))#candidate|9900|(24, 2)|var|float32
call_9898 = relay.TupleGetItem(func_4504_call(relay.reshape(var_9899.astype('float32'), [10, 4, 10]), relay.reshape(var_9900.astype('float32'), [48,]), ), 2)
call_9901 = relay.TupleGetItem(func_4508_call(relay.reshape(var_9899.astype('float32'), [10, 4, 10]), relay.reshape(var_9900.astype('float32'), [48,]), ), 2)
output = relay.Tuple([call_9896,call_9898,var_9899,var_9900,])
output2 = relay.Tuple([call_9897,call_9901,var_9899,var_9900,])
func_9906 = relay.Function([var_9899,var_9900,], output)
mod['func_9906'] = func_9906
mod = relay.transform.InferType()(mod)
var_9907 = relay.var("var_9907", dtype = "float32", shape = (400,))#candidate|9907|(400,)|var|float32
var_9908 = relay.var("var_9908", dtype = "float32", shape = (24, 2))#candidate|9908|(24, 2)|var|float32
output = func_9906(var_9907,var_9908,)
func_9909 = relay.Function([var_9907,var_9908,], output)
mutated_mod['func_9909'] = func_9909
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1187_call = mod.get_global_var('func_1187')
func_1188_call = mutated_mod.get_global_var('func_1188')
call_9921 = relay.TupleGetItem(func_1187_call(), 0)
call_9922 = relay.TupleGetItem(func_1188_call(), 0)
output = call_9921
output2 = call_9922
func_9932 = relay.Function([], output)
mod['func_9932'] = func_9932
mod = relay.transform.InferType()(mod)
output = func_9932()
func_9933 = relay.Function([], output)
mutated_mod['func_9933'] = func_9933
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7971_call = mod.get_global_var('func_7971')
func_7973_call = mutated_mod.get_global_var('func_7973')
call_10002 = relay.TupleGetItem(func_7971_call(), 0)
call_10003 = relay.TupleGetItem(func_7973_call(), 0)
func_7289_call = mod.get_global_var('func_7289')
func_7290_call = mutated_mod.get_global_var('func_7290')
call_10007 = relay.TupleGetItem(func_7289_call(), 0)
call_10008 = relay.TupleGetItem(func_7290_call(), 0)
func_3670_call = mod.get_global_var('func_3670')
func_3672_call = mutated_mod.get_global_var('func_3672')
call_10044 = relay.TupleGetItem(func_3670_call(), 0)
call_10045 = relay.TupleGetItem(func_3672_call(), 0)
output = relay.Tuple([call_10002,call_10007,call_10044,])
output2 = relay.Tuple([call_10003,call_10008,call_10045,])
func_10058 = relay.Function([], output)
mod['func_10058'] = func_10058
mod = relay.transform.InferType()(mod)
mutated_mod['func_10058'] = func_10058
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10058_call = mutated_mod.get_global_var('func_10058')
call_10059 = func_10058_call()
output = call_10059
func_10060 = relay.Function([], output)
mutated_mod['func_10060'] = func_10060
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4735_call = mod.get_global_var('func_4735')
func_4736_call = mutated_mod.get_global_var('func_4736')
call_10067 = relay.TupleGetItem(func_4735_call(), 0)
call_10068 = relay.TupleGetItem(func_4736_call(), 0)
output = call_10067
output2 = call_10068
func_10072 = relay.Function([], output)
mod['func_10072'] = func_10072
mod = relay.transform.InferType()(mod)
mutated_mod['func_10072'] = func_10072
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10072_call = mutated_mod.get_global_var('func_10072')
call_10073 = func_10072_call()
output = call_10073
func_10074 = relay.Function([], output)
mutated_mod['func_10074'] = func_10074
mutated_mod = relay.transform.InferType()(mutated_mod)
const_10088 = relay.const([[[1.170664,1.297673,3.233466,-4.842640,-7.711074,9.666435,1.869642,6.949561,-1.340158,-9.647991],[2.741801,6.129880,2.085818,-2.525643,-1.894561,-1.380223,-0.550697,0.943851,0.433239,-3.775066],[-9.696301,0.695577,0.702445,-1.140947,-7.003940,0.288881,0.913524,1.548992,-9.015154,-3.161293],[-6.264461,-1.477088,0.640387,-4.641961,1.147054,-3.074406,2.512270,1.031809,-4.851819,-0.987451],[-0.825913,-3.438221,-3.423445,1.622852,-1.104018,2.637461,-4.010652,6.953676,9.009089,5.012439],[-8.836190,-8.013920,1.500208,-8.383526,-3.789562,-4.408423,-9.902495,-0.030876,1.738239,7.077893],[-1.669069,-7.257048,5.932202,-6.003677,4.987093,2.250010,6.089109,5.854284,-6.043875,-2.541061],[7.101627,0.613539,-4.519487,-7.727192,8.665784,0.800004,8.034352,2.215685,2.638140,7.602654],[7.949371,-6.778232,1.125050,3.328966,0.043385,-4.743109,0.141459,-2.302409,3.068577,4.131979]],[[4.423124,-2.804065,-2.554903,3.071124,7.946168,-3.895153,8.484644,3.031562,2.591241,-9.091986],[0.561728,6.144003,9.095649,-6.983217,-0.226074,3.391950,-6.730959,-0.409168,8.593045,-0.568442],[3.382246,3.829528,4.537302,1.969335,-9.944539,0.069864,-6.109667,-8.137927,-6.836876,-1.155326],[-1.037435,-5.289310,-2.916201,3.547905,-5.033776,-6.202670,-9.415196,7.075972,1.556364,-4.477200],[-3.160445,5.356989,-1.135552,-5.035906,-0.212848,-8.632638,1.381436,4.507690,2.402190,2.293668],[-3.222161,1.938416,-8.334628,-7.301392,9.995412,9.121983,-6.634927,-1.629446,-4.140424,2.266990],[-0.832707,4.144146,3.348045,6.306001,9.629027,-1.952587,-9.748225,-8.948773,-9.815726,-0.871081],[-6.193236,-6.506731,-0.466634,5.337026,1.620032,7.470113,-5.041879,3.736738,6.736635,9.746505],[-3.911175,-7.164507,5.798290,7.753397,0.807367,-6.391788,9.265487,-8.384274,8.560490,-1.348034]],[[5.683202,-4.388427,-9.064810,6.889256,-0.645818,-8.797286,-2.413627,-1.917870,1.965912,-7.915728],[9.878635,-8.500995,3.758872,2.422533,0.165010,5.767792,7.874705,-9.767177,-1.463100,-2.847632],[-0.702416,3.863454,7.414394,7.957215,8.204924,-4.976787,-5.450919,7.624101,1.490995,-5.104223],[-0.870572,4.385461,-4.424866,0.382794,1.430418,1.292011,-1.086731,1.461006,-2.596172,-1.220062],[-2.054280,3.144400,-7.732067,-0.921274,4.851435,-7.542612,-2.628026,2.195565,2.584344,7.915988],[-2.912455,9.081013,6.200987,6.798996,5.783679,0.622936,-3.329180,-1.324166,0.203122,-5.842810],[5.195726,-0.348083,3.330627,-9.112588,-1.517044,9.931091,2.897121,1.395397,0.052962,-8.258196],[5.919954,-8.678326,-9.650075,-7.930587,7.948677,-5.370431,5.501252,4.900507,5.731366,2.846325],[1.009753,-8.850602,0.022287,-8.840565,-4.484764,7.814890,-2.022088,8.509719,-4.936497,6.202772]],[[8.875069,1.869818,-3.692917,1.115500,-6.230213,-4.028098,5.723705,-2.371681,-5.108179,-1.972902],[-5.725935,-9.640274,5.616458,6.735063,4.570889,-6.603998,8.083458,7.196357,-9.024183,6.787241],[-7.151228,-2.306747,-5.757604,-1.691414,3.708436,-2.566199,4.441354,8.488170,-9.301343,-1.418126],[7.522144,-3.247887,-4.585959,-2.425715,-7.347858,-8.579305,6.078315,5.336171,3.961857,2.273481],[-1.481661,-6.330597,-8.421438,-4.667785,8.061750,1.053012,0.107962,9.981521,3.061086,-5.359541],[4.135551,-3.684309,-6.403675,-0.412318,-0.317540,-0.028803,4.593684,-3.475345,-2.322564,0.150281],[1.887676,-4.320999,-3.813362,0.883850,-8.223091,-0.256841,-5.074537,-5.191334,-7.314999,-8.019545],[-0.946322,4.955679,-1.714249,-4.958379,-8.602538,-0.128178,-5.959678,5.583828,-7.433521,-9.296052],[-9.942149,-6.162990,-7.574187,2.859281,0.270202,3.501274,7.953406,-0.077280,-3.056926,-2.574028]]], dtype = "float64")#candidate|10088|(4, 9, 10)|const|float64
uop_10089 = relay.cos(const_10088.astype('float64')) # shape=(4, 9, 10)
func_9105_call = mod.get_global_var('func_9105')
func_9108_call = mutated_mod.get_global_var('func_9108')
var_10097 = relay.var("var_10097", dtype = "bool", shape = (900,))#candidate|10097|(900,)|var|bool
var_10098 = relay.var("var_10098", dtype = "float64", shape = (16,))#candidate|10098|(16,)|var|float64
call_10096 = relay.TupleGetItem(func_9105_call(relay.reshape(var_10097.astype('bool'), [900, 1]), relay.reshape(var_10098.astype('float64'), [16,]), ), 4)
call_10099 = relay.TupleGetItem(func_9108_call(relay.reshape(var_10097.astype('bool'), [900, 1]), relay.reshape(var_10098.astype('float64'), [16,]), ), 4)
func_3610_call = mod.get_global_var('func_3610')
func_3613_call = mutated_mod.get_global_var('func_3613')
const_10122 = relay.const([1,5,-2,-10,9,3,-7,-4,-5,-5,-9,-2,2,-8,7,3,-9,-7,3,3,-1,4,7,-4,4,-1,-2,10,7,7,1,-1,-10,3,-8,-9,-3,9,-10,2,2,7,-10,-8,-4,2,6,-8,-4,4,-5,10,-6,8,2,2,-5,10,7,-2,-4,8,8,10,7,3,-7,-10,2,2,9,-9,-2,-2,8,2,10,4,6,-9,8,-4,7,-9,-3,-4,-5,-9,-2,8,4,-4,7,-2,1,-7,5,5,7,-10,7,5,9,-10,4,2,5,-2,-3,-7,-6,-5,-8,-3,-8,-9,9,6,-9,-8,2,1,-6,-2,-5,-3,-7,-4,-1,-2,-1,4,7,9,-8], dtype = "int8")#candidate|10122|(135,)|const|int8
const_10123 = relay.const(2, dtype = "int64")#candidate|10123|()|const|int64
call_10121 = relay.TupleGetItem(func_3610_call(relay.reshape(const_10122.astype('int8'), [135,]), relay.reshape(const_10123.astype('int64'), []), ), 1)
call_10124 = relay.TupleGetItem(func_3613_call(relay.reshape(const_10122.astype('int8'), [135,]), relay.reshape(const_10123.astype('int64'), []), ), 1)
func_7200_call = mod.get_global_var('func_7200')
func_7201_call = mutated_mod.get_global_var('func_7201')
call_10127 = func_7200_call()
call_10128 = func_7200_call()
func_7200_call = mod.get_global_var('func_7200')
func_7201_call = mutated_mod.get_global_var('func_7201')
call_10134 = func_7200_call()
call_10135 = func_7200_call()
output = relay.Tuple([uop_10089,call_10096,var_10097,var_10098,call_10121,const_10122,const_10123,call_10127,call_10134,])
output2 = relay.Tuple([uop_10089,call_10099,var_10097,var_10098,call_10124,const_10122,const_10123,call_10128,call_10135,])
func_10137 = relay.Function([var_10097,var_10098,], output)
mod['func_10137'] = func_10137
mod = relay.transform.InferType()(mod)
mutated_mod['func_10137'] = func_10137
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10137_call = mutated_mod.get_global_var('func_10137')
var_10139 = relay.var("var_10139", dtype = "bool", shape = (900,))#candidate|10139|(900,)|var|bool
var_10140 = relay.var("var_10140", dtype = "float64", shape = (16,))#candidate|10140|(16,)|var|float64
call_10138 = func_10137_call(var_10139,var_10140,)
output = call_10138
func_10141 = relay.Function([var_10139,var_10140,], output)
mutated_mod['func_10141'] = func_10141
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6785_call = mod.get_global_var('func_6785')
func_6786_call = mutated_mod.get_global_var('func_6786')
call_10210 = func_6785_call()
call_10211 = func_6785_call()
output = call_10210
output2 = call_10211
func_10229 = relay.Function([], output)
mod['func_10229'] = func_10229
mod = relay.transform.InferType()(mod)
mutated_mod['func_10229'] = func_10229
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10229_call = mutated_mod.get_global_var('func_10229')
call_10230 = func_10229_call()
output = call_10230
func_10231 = relay.Function([], output)
mutated_mod['func_10231'] = func_10231
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9036_call = mod.get_global_var('func_9036')
func_9037_call = mutated_mod.get_global_var('func_9037')
call_10238 = relay.TupleGetItem(func_9036_call(), 3)
call_10239 = relay.TupleGetItem(func_9037_call(), 3)
output = call_10238
output2 = call_10239
func_10240 = relay.Function([], output)
mod['func_10240'] = func_10240
mod = relay.transform.InferType()(mod)
mutated_mod['func_10240'] = func_10240
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10240_call = mutated_mod.get_global_var('func_10240')
call_10241 = func_10240_call()
output = call_10241
func_10242 = relay.Function([], output)
mutated_mod['func_10242'] = func_10242
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5951_call = mod.get_global_var('func_5951')
func_5952_call = mutated_mod.get_global_var('func_5952')
call_10271 = func_5951_call()
call_10272 = func_5951_call()
output = call_10271
output2 = call_10272
func_10292 = relay.Function([], output)
mod['func_10292'] = func_10292
mod = relay.transform.InferType()(mod)
mutated_mod['func_10292'] = func_10292
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10292_call = mutated_mod.get_global_var('func_10292')
call_10293 = func_10292_call()
output = call_10293
func_10294 = relay.Function([], output)
mutated_mod['func_10294'] = func_10294
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10323 = relay.var("var_10323", dtype = "uint16", shape = ())#candidate|10323|()|var|uint16
const_10324 = relay.const([[[6,-4,-2,-7,-8,8,-1,3,5]],[[1,2,1,2,-9,3,8,-7,-2]],[[5,2,2,-3,5,7,6,9,-8]],[[6,-10,-6,4,4,-4,2,8,5]],[[4,-3,3,-2,9,-7,-2,6,9]],[[-6,-4,4,-9,-9,10,4,-1,-6]],[[-8,3,10,4,-2,-5,-2,4,3]],[[4,-4,-8,-9,10,-1,2,7,-7]],[[-5,10,-1,8,7,-7,-10,4,-6]],[[-10,-5,4,-9,3,4,-2,1,8]],[[-8,-3,-10,9,3,-4,4,-5,6]],[[-2,8,8,7,2,-3,-8,-9,-10]],[[-3,-9,-2,7,-8,-4,-4,9,6]]], dtype = "uint16")#candidate|10324|(13, 1, 9)|const|uint16
bop_10325 = relay.subtract(var_10323.astype('uint16'), const_10324.astype('uint16')) # shape=(13, 1, 9)
func_3402_call = mod.get_global_var('func_3402')
func_3405_call = mutated_mod.get_global_var('func_3405')
const_10331 = relay.const([4.105771,-0.736189,2.760611,-1.133849,8.572002,-9.519497,1.720957,-4.763144,1.764419,-6.087571,4.258340,2.537809,4.219752,7.568766,8.451062,6.632349,7.525206,6.772492,5.406940,-1.675253,1.407619,-0.816088,1.890742,-4.508391,-3.717580,-4.268039,-0.230980,3.026269,3.452062,-1.010986,4.058471,-6.799885,3.862805,-2.113917,3.086221,8.856565,4.143662,0.705379,1.835783,-1.161525,1.694923,6.534530,-0.355578,4.605126,9.602225,5.697738,9.490591,5.358381,9.490626,8.268723,3.642469,9.159634,-9.352149,0.445656,-1.423757,-1.180704,-6.594335,8.815564,-7.905615,2.139705,-7.531512,8.226120,-5.087960,-7.362482,-6.490930,-8.454007,3.318331,-8.412396,-9.541142,1.186194,4.533540,-4.737688,7.973294,6.873654,2.277366,5.932323,2.719120,9.944130,8.132661,1.096953,-3.133737,0.125312,6.909300,7.012716,5.895005,4.922911,-0.288033,6.534284,1.927733,-0.573431,5.037147,1.418249,-0.265967,-9.545501,-8.640557,6.543281,9.671053,-0.066979,-4.193304,-2.286144,-6.361822,9.561847,-9.927497,-7.727691,9.395068,-5.977818,-0.244493,5.678606,-3.410019,2.393311,3.646388,1.574148,1.764857,8.513279,-1.555489,-1.905053,5.076094,8.734836,-0.437276,-9.583100,-5.447305,-3.843540,-6.355493,0.999554,7.718042,0.651171,1.397650,9.224534,8.710181,4.750081,-0.019168,-1.283679,0.583066,7.190567,-5.101528,1.484454,-7.659568,2.797478,6.427580,-9.639443,0.633106,2.251579,-9.779061,-1.465636,5.055270,6.002634,7.906877,-9.331029,-6.440611,-6.657934,2.122714,2.884849,9.709351,-7.259051,-7.960931,2.586687,-1.377395,-1.364260,1.617160,-9.161729,-6.789203,-5.734055,-4.185621,-7.217686,9.289320,7.569395,-8.242262,-9.091657,9.510477,-0.254540,1.788416,-5.445613,-2.840077,9.625919,4.800168,8.284277,5.708826,8.719364,-4.913593,-2.937671,-8.295521,-3.699745,4.613115,-7.402886,1.058275,-3.514116,-9.816149,-6.128995,9.741795,-1.742928,-8.980418,3.253990,4.677746,5.464245,-6.441196,7.366909,5.297385,-9.094382,9.342502,5.376540,7.754846,6.763337,-8.340564,6.176831,7.006018,-6.323231,1.887344,-7.822895,-8.757318,-1.058869,0.962558,5.178055,7.736248,9.196518,-1.840418,7.967302,-5.027434,5.531117,-4.105561,7.778276,-2.258358,6.550265,2.683879,6.808631,2.817444,-7.964435,1.583707,7.560697,7.735381,7.785813,-0.353977,-1.584277,-2.964016,4.338037,-9.514143,-1.278054,1.173252,-9.194820,9.999682,-4.702853,9.146547,-3.055726,7.285257,9.118011,-3.273616,-8.671102,7.752341,-4.824561,6.386619,-8.023852,-7.557279,-9.922014,6.987983,-1.145531,-0.584523,5.756140,4.919357,9.199165,-6.190573,-2.668165,0.169335,6.300097,9.442326,-6.231824,2.335961,-1.796523,-5.235796,4.684933,5.253125,-7.520821,7.127490,7.226919,3.772765,1.404461,1.612603,2.650245,-5.739541,5.244024,-8.898290,-7.385553,-7.164185,4.822695,-8.433132,-8.257489,-2.296082,5.056809,8.127354,-6.611754,5.491052,-4.789256,6.220858,-7.155980,-1.087914,8.492324,8.764537,-8.799214,-7.794018,-9.784191,4.389678,-3.227860,-8.248843,7.759073,-9.239548,-7.486575,6.272517,-7.736406,-5.362260,-1.074553,-9.870732,0.597734,-9.547380,-2.470578,6.223700,2.060980,7.531184,-3.846323,7.173429,7.299181,-0.831476,-3.857118,-9.866447,-3.495366,8.090460,1.019709,7.689109,9.697258,0.421534,-5.912020,2.454471,6.107186,-2.658885,-0.764151,3.212503,4.682303,0.242214,1.689208,0.866073,5.726540,-7.668080,-0.608253,6.730904,8.751859,9.731813,-5.648609,6.435461,-7.819427,0.573560,-3.826194,-9.876549,-4.563392,8.673266,-2.736123,-5.226244,4.404313,-1.770372,-0.604494,0.215396,-8.356895,5.636706,7.921486,-2.498429,-7.253819,-7.574459,-8.244689,8.025445,4.032638,-9.749893,8.097928,1.469450,-9.875651,-1.665132,3.453041,-1.173426,6.493910,-2.242581,1.023627,-5.310453,3.995857,-6.970593,6.889651,-3.981864,-7.289553,-3.810909,4.898193,-9.721970,-6.865175,-3.771411,-2.687609,6.401301,8.752550,7.687024,0.534794,-1.142802,-7.546904,-8.314186,-7.002452,-4.226238,-0.977258,-5.347896,-6.860663,8.092057,-8.138789,1.695050,-2.576973,-2.675239,-8.438059,-1.221028,2.301818,-0.004149,9.147588,4.917574,-4.697758,-9.803196,4.332727,-1.168074,8.131765,-1.696295,-7.661015,2.794957,-7.764447], dtype = "float32")#candidate|10331|(420,)|const|float32
call_10330 = relay.TupleGetItem(func_3402_call(relay.reshape(const_10331.astype('float32'), [6, 7, 10]), relay.reshape(const_10331.astype('float32'), [6, 7, 10]), ), 1)
call_10332 = relay.TupleGetItem(func_3405_call(relay.reshape(const_10331.astype('float32'), [6, 7, 10]), relay.reshape(const_10331.astype('float32'), [6, 7, 10]), ), 1)
output = relay.Tuple([bop_10325,call_10330,const_10331,])
output2 = relay.Tuple([bop_10325,call_10332,const_10331,])
func_10336 = relay.Function([var_10323,], output)
mod['func_10336'] = func_10336
mod = relay.transform.InferType()(mod)
var_10337 = relay.var("var_10337", dtype = "uint16", shape = ())#candidate|10337|()|var|uint16
output = func_10336(var_10337)
func_10338 = relay.Function([var_10337], output)
mutated_mod['func_10338'] = func_10338
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9932_call = mod.get_global_var('func_9932')
func_9933_call = mutated_mod.get_global_var('func_9933')
call_10353 = func_9932_call()
call_10354 = func_9932_call()
func_24_call = mod.get_global_var('func_24')
func_27_call = mutated_mod.get_global_var('func_27')
const_10356 = relay.const(-10, dtype = "int64")#candidate|10356|()|const|int64
call_10355 = relay.TupleGetItem(func_24_call(relay.reshape(const_10356.astype('int64'), [])), 0)
call_10357 = relay.TupleGetItem(func_27_call(relay.reshape(const_10356.astype('int64'), [])), 0)
output = relay.Tuple([call_10353,call_10355,const_10356,])
output2 = relay.Tuple([call_10354,call_10357,const_10356,])
func_10368 = relay.Function([], output)
mod['func_10368'] = func_10368
mod = relay.transform.InferType()(mod)
output = func_10368()
func_10369 = relay.Function([], output)
mutated_mod['func_10369'] = func_10369
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8276_call = mod.get_global_var('func_8276')
func_8278_call = mutated_mod.get_global_var('func_8278')
call_10406 = relay.TupleGetItem(func_8276_call(), 0)
call_10407 = relay.TupleGetItem(func_8278_call(), 0)
output = relay.Tuple([call_10406,])
output2 = relay.Tuple([call_10407,])
func_10412 = relay.Function([], output)
mod['func_10412'] = func_10412
mod = relay.transform.InferType()(mod)
mutated_mod['func_10412'] = func_10412
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10412_call = mutated_mod.get_global_var('func_10412')
call_10413 = func_10412_call()
output = call_10413
func_10414 = relay.Function([], output)
mutated_mod['func_10414'] = func_10414
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4735_call = mod.get_global_var('func_4735')
func_4736_call = mutated_mod.get_global_var('func_4736')
call_10427 = relay.TupleGetItem(func_4735_call(), 0)
call_10428 = relay.TupleGetItem(func_4736_call(), 0)
func_2282_call = mod.get_global_var('func_2282')
func_2283_call = mutated_mod.get_global_var('func_2283')
call_10437 = func_2282_call()
call_10438 = func_2282_call()
var_10440 = relay.var("var_10440", dtype = "int64", shape = (1, 15, 10))#candidate|10440|(1, 15, 10)|var|int64
bop_10441 = relay.less_equal(call_10427.astype('bool'), var_10440.astype('bool')) # shape=(1, 15, 10)
bop_10444 = relay.less_equal(call_10428.astype('bool'), var_10440.astype('bool')) # shape=(1, 15, 10)
output = relay.Tuple([call_10437,bop_10441,])
output2 = relay.Tuple([call_10438,bop_10444,])
func_10448 = relay.Function([var_10440,], output)
mod['func_10448'] = func_10448
mod = relay.transform.InferType()(mod)
var_10449 = relay.var("var_10449", dtype = "int64", shape = (1, 15, 10))#candidate|10449|(1, 15, 10)|var|int64
output = func_10448(var_10449)
func_10450 = relay.Function([var_10449], output)
mutated_mod['func_10450'] = func_10450
mutated_mod = relay.transform.InferType()(mutated_mod)
const_10493 = relay.const([[[-9,7,-4,-5,-4,-2],[-4,-1,-7,-8,-6,1],[-5,1,-8,2,-5,-1],[-5,-4,3,-9,2,7],[-3,-2,-7,8,-2,4],[10,-7,-6,-4,5,3],[-3,-8,-2,-8,1,5],[3,-9,-4,6,8,9],[-4,-8,2,-10,6,1],[2,-3,1,2,-3,2],[-4,3,4,8,8,8]],[[9,-4,5,-3,9,9],[-5,-6,1,-10,-6,7],[-7,-9,-2,5,-4,-6],[-8,-5,4,7,-4,2],[10,-10,-4,-10,1,8],[-6,-7,-3,1,-4,8],[-2,-9,-9,4,10,-10],[9,5,-9,5,5,-8],[-7,-2,9,8,9,10],[6,-9,-5,1,7,6],[-9,3,-5,4,4,-2]],[[10,-4,7,4,7,-2],[-2,-6,10,-7,5,5],[-1,-1,-9,-7,4,5],[-7,-7,-4,-7,-3,-5],[7,4,-10,-1,1,9],[6,8,-9,-1,4,3],[6,-2,4,-2,7,-4],[-4,-1,8,5,-6,-6],[-6,3,5,-5,5,2],[5,2,-9,-1,9,9],[2,1,-7,-2,4,-2]]], dtype = "uint16")#candidate|10493|(3, 11, 6)|const|uint16
var_10494 = relay.var("var_10494", dtype = "uint16", shape = (3, 11, 6))#candidate|10494|(3, 11, 6)|var|uint16
bop_10495 = relay.add(const_10493.astype('uint16'), relay.reshape(var_10494.astype('uint16'), relay.shape_of(const_10493))) # shape=(3, 11, 6)
func_10368_call = mod.get_global_var('func_10368')
func_10369_call = mutated_mod.get_global_var('func_10369')
call_10535 = relay.TupleGetItem(func_10368_call(), 0)
call_10536 = relay.TupleGetItem(func_10369_call(), 0)
func_2009_call = mod.get_global_var('func_2009')
func_2011_call = mutated_mod.get_global_var('func_2011')
call_10542 = relay.TupleGetItem(func_2009_call(), 0)
call_10543 = relay.TupleGetItem(func_2011_call(), 0)
func_6785_call = mod.get_global_var('func_6785')
func_6786_call = mutated_mod.get_global_var('func_6786')
call_10565 = func_6785_call()
call_10566 = func_6785_call()
func_4151_call = mod.get_global_var('func_4151')
func_4153_call = mutated_mod.get_global_var('func_4153')
call_10570 = relay.TupleGetItem(func_4151_call(), 0)
call_10571 = relay.TupleGetItem(func_4153_call(), 0)
output = relay.Tuple([bop_10495,call_10535,call_10542,call_10565,call_10570,])
output2 = relay.Tuple([bop_10495,call_10536,call_10543,call_10566,call_10571,])
func_10582 = relay.Function([var_10494,], output)
mod['func_10582'] = func_10582
mod = relay.transform.InferType()(mod)
mutated_mod['func_10582'] = func_10582
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10583 = relay.var("var_10583", dtype = "uint16", shape = (3, 11, 6))#candidate|10583|(3, 11, 6)|var|uint16
func_10582_call = mutated_mod.get_global_var('func_10582')
call_10584 = func_10582_call(var_10583)
output = call_10584
func_10585 = relay.Function([var_10583], output)
mutated_mod['func_10585'] = func_10585
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1603_call = mod.get_global_var('func_1603')
func_1604_call = mutated_mod.get_global_var('func_1604')
call_10599 = relay.TupleGetItem(func_1603_call(), 0)
call_10600 = relay.TupleGetItem(func_1604_call(), 0)
output = call_10599
output2 = call_10600
func_10601 = relay.Function([], output)
mod['func_10601'] = func_10601
mod = relay.transform.InferType()(mod)
mutated_mod['func_10601'] = func_10601
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10601_call = mutated_mod.get_global_var('func_10601')
call_10602 = func_10601_call()
output = call_10602
func_10603 = relay.Function([], output)
mutated_mod['func_10603'] = func_10603
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10612 = relay.var("var_10612", dtype = "bool", shape = (1, 11, 9))#candidate|10612|(1, 11, 9)|var|bool
const_10613 = relay.const([[[True,False,False,False,True,True,False,False,False],[False,True,True,True,True,False,True,False,True],[False,True,False,False,True,True,True,False,True],[True,True,True,False,True,True,False,True,True],[True,False,True,True,False,False,False,True,True],[False,False,True,False,False,False,False,False,False],[True,False,False,False,True,True,False,True,False],[True,True,False,False,True,False,True,False,False],[True,True,True,False,True,True,False,True,True],[False,True,True,False,False,True,False,True,True],[False,True,False,False,False,False,False,True,True]]], dtype = "bool")#candidate|10613|(1, 11, 9)|const|bool
bop_10614 = relay.logical_and(var_10612.astype('bool'), relay.reshape(const_10613.astype('bool'), relay.shape_of(var_10612))) # shape=(1, 11, 9)
bop_10656 = relay.multiply(bop_10614.astype('int32'), relay.reshape(var_10612.astype('int32'), relay.shape_of(bop_10614))) # shape=(1, 11, 9)
func_2737_call = mod.get_global_var('func_2737')
func_2738_call = mutated_mod.get_global_var('func_2738')
call_10693 = func_2737_call()
call_10694 = func_2737_call()
output = relay.Tuple([bop_10656,call_10693,])
output2 = relay.Tuple([bop_10656,call_10694,])
func_10696 = relay.Function([var_10612,], output)
mod['func_10696'] = func_10696
mod = relay.transform.InferType()(mod)
var_10697 = relay.var("var_10697", dtype = "bool", shape = (1, 11, 9))#candidate|10697|(1, 11, 9)|var|bool
output = func_10696(var_10697)
func_10698 = relay.Function([var_10697], output)
mutated_mod['func_10698'] = func_10698
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3650_call = mod.get_global_var('func_3650')
func_3651_call = mutated_mod.get_global_var('func_3651')
call_10732 = relay.TupleGetItem(func_3650_call(), 0)
call_10733 = relay.TupleGetItem(func_3651_call(), 0)
func_2243_call = mod.get_global_var('func_2243')
func_2245_call = mutated_mod.get_global_var('func_2245')
const_10745 = relay.const([1.465364,9.143058,-4.551262,5.625720,1.939276,5.190918,-2.248550,-4.561425,-6.017789,3.587726,-9.174636,-7.216053,-6.305735,-6.577527,1.978949,-8.174999,-3.875953,-8.373094,-2.044762,8.379804,6.985267,3.705100,6.697982,5.536459,0.535653,-8.628795,6.995037,-9.699299,6.277850,0.616040,-2.736392,6.987576,8.358905,2.096858,6.898334,3.900058,6.141008,4.599366,-5.923221,-5.917519,4.772677,1.742013,-9.536880,-5.319372,7.506257,-9.016911,0.058968,-8.297376], dtype = "float32")#candidate|10745|(48,)|const|float32
call_10744 = relay.TupleGetItem(func_2243_call(relay.reshape(const_10745.astype('float32'), [48,])), 1)
call_10746 = relay.TupleGetItem(func_2245_call(relay.reshape(const_10745.astype('float32'), [48,])), 1)
func_7659_call = mod.get_global_var('func_7659')
func_7664_call = mutated_mod.get_global_var('func_7664')
const_10759 = relay.const([-10,-9,10,4,2,-6,5,-2,1,-7,-5,3,9,-9,2,3,-8,-9,-4,10,2,7,-1,-10,-10,-9,1,8,-7,-8,1,-4,-6,7,6,7,3,-5,4,-1,4,7,3,7,4,-10,7,-6,-5,-4,-10,8,9,-10,-1,-7,-2,-10,2,4,3,3,-7,4,9,4,-10,-3,-10,-2,-3,-5,3,-9,-5,1,8,-9,-2,-1,-10,10,-9,-1,-5,9,-1,-4,-4,-7,5,-8,-1,-2,-9,-6,7,-2,-9,5,-5,-4,1,-9,1,3,-6,-1,-7,2,5,6,1,8,1,6,10,-10,-7,5,7,-6,-8,-9,-9,2,6,3,7,1,-5,-4,8,5,5,5,-7,-2,-7,1,-2,7,-2,-7,-4,-7,-5,5,6,-1,9,2,7,2,-7,-8,-3,-6,9,-3,10,-1,2,-10,-5,9,7,1,-7,5,-5,10,-2,-2,10,2,-7,6,-3,8,-5,4,-8,5,-10,-9,5,-3,-8,6,2,9,-4,-9,-1,-5,-3,10,7,-7,6,-10,-7,-8,9,4,-3,-3,10,-4,-8,-9,9,4,-5,-3,-9,1,-7,3,-2,-9,10,2,3,-10,6,-4,9,2,-9,4,-7,3,2,2,-3,-9,-3,2,8,9,-1,10,8,-3,-5,4,10,10,3,9,2,-10,10,3,6,-1,-2,7,3,9,-7,-3,-2,2,-2,-3,9,-1,7,-9,5,-10,-1,9,8,-3,2,-3,-7,-4,-6,-7,-2,7,2,10,6,-6,-6,-2,-6,-9,-2,-5,-9,-10,-5,3,-5,7,-4,7,-9,-8,10,1,-6,-4,-5,7,-7,-1,6,-2,-4,-10,-5,10,-10,1,10,-3,2,-5,8,1,1,-10,7,7,8,-2,2,9,2,-1,-9,9,6,8,-5,9,-2,2,10,1,-5,-3,4,-1,3,7,10,5,9,8,-4,-10,6,6,-9,4,-9,-5,2,-9,9,6,3,5,-5,-6,4,5,-7,-5,-9,4,-9,-1,4,3,8,-5,1,3,-7,-4,4,-10,-2,9,8,-9,2,-8,-10,2,-2,-8,-8,-8,-9,-7,-4,6,-4,7,-8,-8,6,7,-7,-3,5,-2,2,10,-4,4,4,4,-5,-9,-7,5,1,9,-10,-6,6,8,10,9,4,2,3,7,8,3,3,9,10,1,-2,3,-7,-6,-10,8,8,6,-7,9,9,1,10,5,7,9,4,-7,-4,5,8,10,5,-5,-6,-6,-8,6,-6,-9,-6,-4,2,-1,-6,10,10,-8,-5,7,-1,8,-1,-7,-7,2,7,-6,-1,5,1,-1,-9,-8,-4,-8,10,-4,4,8,10,-5,-9,-7,-7,-6,-10,-1,-6,3,-6,6,-1,-6,2,6,-5,-2,-3,-5,-1,-9,7,-2,-9,-6,-10,-10,3,-3,2,-10,2,3,8,4,-8,4,2,-10,-3,-7,-9,3,7,-8,7,5,-7,-3,-4,-8,-1,-8,8,-6,-6,-5,4,-8,4,-7,3,10,-10,-9,-1,9,-9,7,-6,-10,7,-9,3,-1,3,-8,2,8,-1,8,-4,-6,-5,2,-7,8,-10,-7,6,10,10,8,7,5,3,-2,2,9,2,-1,-4,4,-7,6,3,-3,-7,-4,-6,-2,2,-5,-1,-4,-4,5,5,1,-2,-3,5,7,-6,-6,-10,1,-2,8,1,-8,8,-2,-3,-5,1,2,-6,8,2,6,2,-3,6,-8,5,1,-1,6,-5,1,-9,-2], dtype = "uint64")#candidate|10759|(660,)|const|uint64
const_10760 = relay.const([[4.746463,-8.029311],[-7.176104,0.680020],[-3.778347,9.398673],[-8.431231,6.428270],[9.133301,4.058753],[-6.706543,2.181724],[9.883970,-0.151532],[7.551858,-7.543826],[7.936393,1.258272],[-9.210211,9.856683],[-6.718681,-1.294558],[2.878846,-0.596517],[2.291759,-4.483105],[2.728362,-5.515713],[-4.181634,2.800205],[0.380022,0.365900],[-8.285173,0.672370],[5.828825,4.576939],[9.294013,-8.164156],[0.870874,4.750781],[-7.884565,-4.749147],[9.940645,-0.766668],[8.493926,-8.368989],[9.611322,8.464671],[-8.627494,6.521259],[1.033226,1.748175],[-9.144095,8.192394],[2.397415,1.063239],[3.032295,4.899710],[-3.847032,-0.460092],[2.924711,-4.599536],[-4.460847,-4.347407],[-8.561692,-4.946856],[-0.850834,-0.798991],[4.082054,-7.916330],[-4.706229,-8.787772],[6.141735,3.084162],[-5.818396,1.840816],[-8.060372,-7.993879],[3.230325,4.282898],[-9.446621,8.996299],[5.561351,-8.575706],[-0.917230,3.707408],[-5.113124,-5.157813],[-0.213724,4.268759],[8.812924,-9.013302],[-1.051194,2.798545],[-8.737413,-6.063502],[-3.905583,3.298560],[5.282487,1.299749],[9.533512,1.423916],[-1.141686,2.128953],[9.742179,1.321966],[-3.300156,-2.372893],[1.012412,-3.194718],[-4.057953,-6.981800],[2.907499,-5.490104],[9.945038,-3.738120],[0.438590,-0.435864],[2.527065,-6.527582],[-3.019247,6.006242],[7.012512,-3.010065],[3.192614,-3.376494],[5.545423,3.256354],[7.375200,8.627684],[9.252710,4.775742],[6.978572,-5.536763],[3.972546,0.194231],[6.347350,-7.304084],[-1.974204,9.322578],[-6.111469,7.309420],[-4.961576,-2.691744],[9.935759,8.369437],[8.593945,8.080705],[-1.048896,3.420246],[-6.916381,-4.943200],[3.842921,-2.550631],[0.815030,-3.550044],[-7.924918,5.799332],[-3.607922,-8.460642],[3.469084,-5.815928],[-3.661145,-4.917190],[8.104132,-1.929443],[-6.977086,9.605425],[-6.008549,-4.138454],[9.579255,9.800722],[-1.278071,1.701746],[-9.752957,-5.555163],[6.304391,-4.387530],[-5.301502,-6.089281],[-5.033338,3.304181],[1.903380,-9.758851],[6.026096,4.336659],[0.022028,-9.070832],[1.351778,-7.599713],[2.181025,-1.036881],[8.112741,-0.006291],[2.627875,-3.768233],[6.998731,-9.124432],[-6.154904,-9.112391],[8.039353,5.741817],[-4.511668,2.288728],[2.361465,0.940927],[-4.942978,7.545854],[-4.797228,-2.875600],[-4.312591,6.395814],[-0.567869,1.721625],[6.380644,-7.990644],[2.304852,9.982491],[2.972625,-7.947057],[5.181621,6.617347],[0.013274,7.963829],[-5.735997,3.322925],[-9.718879,6.420589],[-2.991353,-7.483957],[-5.157681,8.205009],[-8.100682,-1.839449],[0.558485,-7.079092],[-7.554823,-1.627442],[-9.607534,-7.399101],[9.619174,1.596204],[-1.388990,2.208032],[0.987353,-7.723818],[-9.593953,-6.483141],[4.565593,3.912110],[0.438395,0.761691],[6.746535,0.844945],[5.116424,3.205901],[7.877061,2.269965],[9.140890,-8.181980],[-5.807336,-7.038159],[-0.552536,0.201384],[1.066975,-2.555299],[-2.353529,9.308482],[-5.168056,3.484626],[-3.214022,-7.887615],[1.277565,2.754614],[-6.120569,-1.808029],[4.701437,-3.668597],[6.973380,5.843575],[-5.050149,0.520720],[7.453291,-6.182748],[3.655978,5.358010],[-8.042221,9.414925],[9.098583,-5.895008],[-1.579905,-2.374136],[-8.708752,-3.315937],[-7.332976,-4.494100],[8.701454,0.653158],[-8.341174,-3.621782],[9.751206,5.597648],[-7.956151,-2.998180],[-2.892040,1.600422],[0.869102,-2.723922],[-6.147982,8.646372],[-0.004611,4.937110],[9.086221,-6.475741],[9.979386,3.148381],[-3.190088,-2.667206],[8.167259,1.017032],[-4.609737,-0.296181],[-9.282903,0.947457],[3.434305,-0.767336],[-9.523842,-2.144876],[-8.023186,-8.922871],[4.271078,7.929703],[-4.290180,-6.069129],[-7.881334,3.544669],[0.973380,-4.187457],[-2.721885,-5.517388],[-0.592356,2.292282],[2.327623,-9.843437],[-1.718354,1.041413],[-3.815170,-1.319346],[-4.167564,-3.536760],[-1.341346,9.193146],[6.060232,4.885107],[9.473777,-4.976600],[-7.569697,8.434607],[6.845795,-5.013588],[-5.741924,4.179453],[-4.736109,7.690442],[6.254936,4.262780],[-1.363215,0.952198],[-0.067827,5.345952],[-6.207824,8.775743],[-7.768325,-9.314518],[-1.039258,7.101866],[-5.477352,9.597450],[-2.445937,-8.179706],[-0.884225,6.572148],[-6.321463,-7.092621],[-4.538868,1.030144],[2.758804,3.785769],[6.840218,7.395789],[-7.705352,-3.935265],[-8.983278,8.192787],[-9.410391,-1.586894],[0.875622,6.410148],[-8.023766,-0.412684],[-3.492330,4.762085],[-9.223599,0.038176],[3.558114,2.650882],[5.069883,-0.788010],[9.030351,5.897016],[0.898462,-5.077728],[9.746474,2.410219],[-8.575061,-7.888277],[1.364397,-1.313637],[3.243817,0.671397],[6.115798,-3.843148],[-9.637679,-4.274300],[4.029323,4.680279],[2.996097,2.596611],[-8.185104,-3.307245],[4.601136,9.123218],[-2.201835,-2.460851],[4.747573,-4.583441],[8.329229,1.393222],[-6.401860,5.708292],[7.039939,-6.953211],[3.670756,-5.867413],[-5.364159,-8.231440],[0.790019,-9.382803],[4.703722,5.184008],[-4.830019,7.269002],[6.500319,5.131038],[-2.621578,4.139218],[-3.918861,-6.956760],[3.520140,5.959916],[1.431768,3.457593],[8.886400,7.203876],[7.473171,4.547411],[-4.471744,6.434595],[3.422272,4.412631],[5.968224,-6.883405],[0.387384,1.035524],[4.556022,-7.205506],[-3.574311,1.741834],[-1.522608,7.975002],[-8.317154,4.734946],[8.480518,-4.647094],[-9.296268,3.199146],[-4.327219,2.830910],[-6.800597,-2.930569],[9.247798,7.545295],[0.418236,9.297614],[6.771318,3.522832],[8.306730,-5.303996],[1.106686,8.487495],[3.728072,7.170105],[-2.258759,1.716886],[-6.626622,-3.889135],[-7.928426,1.832744],[7.585615,9.098714],[3.806878,-6.088246],[-1.329648,-8.100268],[2.313064,7.292974],[-7.778678,-0.944857],[4.164995,1.671517],[7.988043,4.657480],[6.686486,1.803952],[5.587840,4.809786],[9.383293,7.696735],[8.363794,3.970635],[1.737629,7.143370],[-5.877837,0.507180],[1.906804,7.985153],[-3.423938,-9.722443],[3.236285,-4.110213],[3.058030,-7.417652],[6.068397,-7.322313],[8.922301,3.765706],[-4.368268,-0.398699],[-1.231158,-3.772714],[-7.060762,8.147711],[-6.879146,2.517568],[9.232150,-7.850227],[7.909856,-0.797889],[-4.025069,9.834151],[-6.970481,-5.004856],[8.701651,3.056045],[-8.458949,3.665252],[3.963636,-5.104377],[0.689354,-4.489097],[9.164791,2.558909],[6.193333,-2.201661],[-7.236265,2.172876],[-6.482057,4.074794],[-6.100973,-0.128301],[-0.445679,8.502544],[-5.114435,7.545362],[5.904628,-7.943138],[-1.653117,-3.713811],[8.329350,7.213300],[-2.036730,8.751345],[-1.044869,5.278463],[0.457156,-0.743969],[5.418879,-6.101985],[1.890033,3.420356],[9.513168,8.176293],[0.498033,6.238055],[-8.576413,-3.813517],[3.988807,-9.220685],[-1.588179,-3.450552],[7.593512,8.430051],[-5.672711,-5.567494],[9.588799,4.189969],[9.638513,-2.911551],[-8.942178,-4.506762],[-5.045428,2.406359],[-9.145071,-3.600985],[7.149902,-8.097198],[4.702865,-3.976192],[4.563501,7.858162],[-7.536775,9.400521],[8.136239,0.878582],[3.756192,4.255399],[-7.000838,7.653478],[-4.713647,-4.578269],[-6.821892,-0.223731],[-6.171390,-8.613974],[1.068542,3.829179],[-7.393490,3.471053],[-4.679188,9.318461],[-0.053343,-2.947390],[9.027624,6.651633],[3.286007,-9.504009],[6.301398,3.213350],[3.754332,1.179620],[8.541823,-8.885471],[-9.533342,5.775602],[-9.258298,-4.987040],[3.140742,-8.730055],[8.939832,-0.197017],[1.580705,-1.542471],[3.769601,-6.657346],[1.914763,2.810061],[-5.787592,-1.375329],[-2.736375,-6.390934],[-8.945883,6.801555],[6.855412,2.184443],[-3.227738,3.465443],[-0.075452,-3.564156],[4.110918,-7.158215],[-4.789796,5.653673],[1.677048,5.081452],[1.298951,9.842994],[3.450148,-9.303056],[-5.477434,3.481680],[0.512331,-6.055202],[-9.228551,-5.927928],[9.908395,0.295313],[-4.298285,2.231165],[-9.367757,8.841113],[-8.645792,-1.678205],[-8.129233,-6.602115],[-3.008636,2.413650],[-4.620011,8.390460],[-5.536205,-1.274491],[-7.702119,5.039130],[-6.970092,-5.561958],[-8.042588,-9.657010],[-3.413751,-3.662928],[5.774698,8.860977],[-8.409416,-5.496155],[-4.005102,2.244406],[5.584561,5.187250],[4.689228,-6.299418],[9.855416,5.428296],[6.339964,-0.813799],[-2.669079,-5.167374],[2.190972,4.453499],[-8.270663,-4.540095],[0.017688,4.545998],[2.718576,-4.751685],[0.643878,-9.369978],[1.451379,-8.532465],[5.152870,5.855978],[2.471207,-0.299597],[8.728295,-7.237019],[4.680524,9.182351],[7.834988,6.913318],[4.100258,5.636890],[-0.646251,3.613082],[8.027152,-3.143398],[-4.455900,-9.663425],[8.365022,-0.050595],[-0.211789,-7.201221],[2.284397,-8.669369],[-2.020172,3.074018],[2.978886,9.092788],[-2.271240,-6.172870],[-2.499862,-9.750605],[-7.122572,2.852819],[0.452553,-3.221236],[-2.570475,7.934594],[-1.854797,-7.800342],[1.618282,-1.146180],[2.830791,2.712352],[-9.713657,1.034685],[-0.691674,9.926844],[6.866402,0.507432],[-7.261030,-8.531769],[-7.198653,-8.302926],[-3.767523,-7.831306],[-4.412486,-8.356303],[-0.110308,5.897452],[4.248266,8.462314],[1.762481,-1.384182],[3.247896,2.005348],[-7.124799,0.722415],[-6.032230,0.638018],[-9.563840,-1.316902],[4.762652,-9.123593],[-1.743801,-4.490595],[6.771565,-8.286708],[5.908542,0.965121],[-4.914180,-2.261305],[-0.486109,9.616371],[-0.626186,7.907975],[-2.834042,7.374995],[9.377870,1.899594],[-5.809310,5.674232],[-2.308607,-4.599812],[8.305125,-1.292050],[-8.675711,-6.195292],[-7.181534,1.845874],[-7.868032,-3.279700],[7.666450,-3.184266],[7.671629,-0.533470],[-1.873883,7.820421],[4.017493,-3.507305],[3.151992,-7.350802],[1.559883,2.763914],[7.386402,-6.582637],[0.500466,-8.041863],[3.435415,9.992967],[0.347953,-9.919182],[-5.769423,-8.577997],[1.831389,-9.336075],[1.506515,-8.575454],[0.472455,2.455576],[2.613883,-9.399609],[-0.739415,1.169050],[-4.792283,-7.480605],[-1.205672,0.753164],[0.901001,3.372212],[-5.406722,3.396304],[-9.588371,-3.596275],[3.621947,-0.121677],[-6.122719,-7.121037],[-0.266620,-5.502626],[-8.768505,-9.829915],[2.357375,0.269297],[6.727181,9.041514],[-2.673663,6.978120],[-1.752524,-2.235802],[3.915339,-9.275981],[-9.617430,-8.020395],[-1.819889,6.019297],[-4.597151,-4.333098],[8.964694,-3.887140],[-6.089761,-2.106952],[-2.894651,4.630059],[8.801234,0.496461],[0.758041,-7.266003],[-5.120620,-7.500235],[9.575306,4.606112],[7.076014,6.388974],[-2.495909,7.111915],[8.585152,9.596628],[5.055446,4.884559],[2.811509,-5.209786],[-8.885969,-4.141953],[3.479563,-8.718492],[-5.619383,-1.448242],[6.716954,-0.893696],[4.909943,-2.137788],[8.591203,4.366435]], dtype = "float32")#candidate|10760|(480, 2)|const|float32
call_10758 = relay.TupleGetItem(func_7659_call(relay.reshape(const_10759.astype('uint64'), [15, 11, 4]), relay.reshape(const_10759.astype('uint64'), [15, 11, 4]), relay.reshape(const_10760.astype('float32'), [10, 96]), ), 3)
call_10761 = relay.TupleGetItem(func_7664_call(relay.reshape(const_10759.astype('uint64'), [15, 11, 4]), relay.reshape(const_10759.astype('uint64'), [15, 11, 4]), relay.reshape(const_10760.astype('float32'), [10, 96]), ), 3)
func_4249_call = mod.get_global_var('func_4249')
func_4252_call = mutated_mod.get_global_var('func_4252')
var_10778 = relay.var("var_10778", dtype = "float32", shape = (420,))#candidate|10778|(420,)|var|float32
call_10777 = relay.TupleGetItem(func_4249_call(relay.reshape(var_10778.astype('float32'), [14, 3, 10])), 2)
call_10779 = relay.TupleGetItem(func_4252_call(relay.reshape(var_10778.astype('float32'), [14, 3, 10])), 2)
output = relay.Tuple([call_10732,call_10744,const_10745,call_10758,const_10759,const_10760,call_10777,var_10778,])
output2 = relay.Tuple([call_10733,call_10746,const_10745,call_10761,const_10759,const_10760,call_10779,var_10778,])
func_10780 = relay.Function([var_10778,], output)
mod['func_10780'] = func_10780
mod = relay.transform.InferType()(mod)
mutated_mod['func_10780'] = func_10780
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10781 = relay.var("var_10781", dtype = "float32", shape = (420,))#candidate|10781|(420,)|var|float32
func_10780_call = mutated_mod.get_global_var('func_10780')
call_10782 = func_10780_call(var_10781)
output = call_10782
func_10783 = relay.Function([var_10781], output)
mutated_mod['func_10783'] = func_10783
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4735_call = mod.get_global_var('func_4735')
func_4736_call = mutated_mod.get_global_var('func_4736')
call_10862 = relay.TupleGetItem(func_4735_call(), 0)
call_10863 = relay.TupleGetItem(func_4736_call(), 0)
output = relay.Tuple([call_10862,])
output2 = relay.Tuple([call_10863,])
func_10870 = relay.Function([], output)
mod['func_10870'] = func_10870
mod = relay.transform.InferType()(mod)
mutated_mod['func_10870'] = func_10870
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10870_call = mutated_mod.get_global_var('func_10870')
call_10871 = func_10870_call()
output = call_10871
func_10872 = relay.Function([], output)
mutated_mod['func_10872'] = func_10872
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8355_call = mod.get_global_var('func_8355')
func_8356_call = mutated_mod.get_global_var('func_8356')
call_10925 = relay.TupleGetItem(func_8355_call(), 0)
call_10926 = relay.TupleGetItem(func_8356_call(), 0)
output = call_10925
output2 = call_10926
func_10929 = relay.Function([], output)
mod['func_10929'] = func_10929
mod = relay.transform.InferType()(mod)
mutated_mod['func_10929'] = func_10929
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10929_call = mutated_mod.get_global_var('func_10929')
call_10930 = func_10929_call()
output = call_10930
func_10931 = relay.Function([], output)
mutated_mod['func_10931'] = func_10931
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1580_call = mod.get_global_var('func_1580')
func_1582_call = mutated_mod.get_global_var('func_1582')
call_10936 = relay.TupleGetItem(func_1580_call(), 1)
call_10937 = relay.TupleGetItem(func_1582_call(), 1)
func_7540_call = mod.get_global_var('func_7540')
func_7542_call = mutated_mod.get_global_var('func_7542')
call_10949 = relay.TupleGetItem(func_7540_call(), 0)
call_10950 = relay.TupleGetItem(func_7542_call(), 0)
func_4569_call = mod.get_global_var('func_4569')
func_4571_call = mutated_mod.get_global_var('func_4571')
const_10962 = relay.const([False,True,False,False,True,False,False,False,True,True,False,False,True,True,False,True,False,False,False,True,True,True,False,False,False,True,True,True,True,False,True,False,True,False,False,False,False,False,False,False,False,True,False,True,False,False,False,False,True,True,False,False,False,False,False,True,True,True,False,True,True,True,True,False,True,True,True,False,False,True,False,False,False,False,True,True,False,True,True,True,False,True,True,True,True,True,False,True,True,False,False,False,True,True,True,True,False,False,True,False,True,True,False,False,True,True,True,True,True,False,True,True,False,False,False,True,False,False,False,True,False,False,True,False,True,False,True,False,False,False,False,False,True,True,False,False,False,True,True,True,True,False,True,True,True,True,True,True,False,True,False,False,False,True,False,True,False,True,True,False,True,False,False,False,True,False,False,True,True,False,True,True,False,False,False,True,True,True,False,True,True,False,False,True,False,False,False,False,False,False,False,True,False,True,False,True,True,False,False,True,False,True,False,True,True,False,False,True,False,True,False,True,True,False,False,True,True,False,True,True,False,False,False,False,True,False,True,False,True,False,True,True,True,True,False,True,False,True,False,False,False,False,True,True,True,True,True,False,True,False,True,False,False,True,False,True,False,False,False,True,False,True,False,True,True,True,False,True,False,False,True,False,True,False,True,False,True,False,False,False,True,True,False,True,False,True,True,False,True,True,True,True,False,False,False,True,True,True,False,True,True,True,True,False,True,False,False,False,True,False,True,False,True,True,True,False,False,False,False,True,True,False,False,False,False,True,True,True,False,False,False,True,True,True,False,True,True,False,True,False,True,False,False,False,False,False,False,False,False,True,False,False,True,False,False,True,True,True,False,True,True,False,True,True,True,True,False,False,True,True,True,False,False,True,True,False,True,True,False,False,False,False,False,True,True,False,False,False,True,False,False,True,False,True,False,True,False,False,False,True,True,True,False,True,False,True,True,False,False,False,False,True,False,False,False,True,False,True,False,True,True,False,False,False,True,False,True,True,False,True,False,False,False,False,True,True,True,True,True,False,True,True,True,True,True,True,True,True,False,True,False,False,True,True,False,False,True,True,True,False,True,True,False,True,False,True,False,True,False,True,True,True,False,False,True,True,False,False,False,False,True,True,False,False,False,False,False,True,False,True,True,True,False,True,False,False,True,True,False,True,False,True,True,True,False,False,False,False,False,True,False,True,False,True,True,False,True,True,True,True,False,True,False,False,False,True,True,True,False,True,True,False,False,False,True,False,False,False,False,False,True,True,True,True,False,False,True,True,True,False,True,True,True,True,True,False,False,False,True,False,True,False,True,False,False,False,False,False,False,True,False,True,False,True,False,False,True,True,True,False,False,False,True,True,False,True,True,False,True,True,True,True,True,False,True,False,False,True,False,True,False,True,False,False,False,True,False,False,False,False,False,False,False,False,False,False,True,True,True,False,False,False,True,False,False,False,False,False,False,False,True,False,True,False,True,False,True,True,False,True,True,False,False,False,False,False,False,True,True,True,False,False,True,True,False,True,False,False,False,False,False,True,False,False,True,True,False,False,True,False,False,False,False,False,False,True,False,True,False,True,False,False,True,False,False,True,True,False,True,True,False,False,True,False,False,False,False,False,True,True,False,True,True,False,True,False,True,True,True,False,False,True,False,False,True,False,True,True,False,True,False,False,True,True,True,True,False,True,True,True,False,True,False,True,True,True,True,True,False,False,True,False,False,True,False,True,False,False,False,False,True,True,True,False,False,False,True,False,True,False,True,True,True,True,False,False,False,False,True,False,False,False,True,False,False,True,False,False,True,False,False,False,True,True,False,False,True,True,False,False,True,False,True,False,True,False,True,False,False,False,False,False,True,True,True,True,True,True,True,False,True,True,True,True,True,True,True,False,True,True,True,False,True,False,True,True,False,False,True,False,False,True,True,True,True,False,False,False,True,True,False,False,True,True,True,False,True,False,False,False,False,True,False,True,False,True,False,False,True,True,True,False,True,False,True,False,False,False,False,True,True,False,True,False,False,True,False,True,True,True,True,True,False,True,True,False,True,True,True,False,True,False,False,False,False,False,False,False,False,False], dtype = "bool")#candidate|10962|(900,)|const|bool
call_10961 = relay.TupleGetItem(func_4569_call(relay.reshape(const_10962.astype('bool'), [15, 10, 6])), 1)
call_10963 = relay.TupleGetItem(func_4571_call(relay.reshape(const_10962.astype('bool'), [15, 10, 6])), 1)
output = relay.Tuple([call_10936,call_10949,call_10961,const_10962,])
output2 = relay.Tuple([call_10937,call_10950,call_10963,const_10962,])
func_10978 = relay.Function([], output)
mod['func_10978'] = func_10978
mod = relay.transform.InferType()(mod)
output = func_10978()
func_10979 = relay.Function([], output)
mutated_mod['func_10979'] = func_10979
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10368_call = mod.get_global_var('func_10368')
func_10369_call = mutated_mod.get_global_var('func_10369')
call_11037 = relay.TupleGetItem(func_10368_call(), 0)
call_11038 = relay.TupleGetItem(func_10369_call(), 0)
output = relay.Tuple([call_11037,])
output2 = relay.Tuple([call_11038,])
func_11040 = relay.Function([], output)
mod['func_11040'] = func_11040
mod = relay.transform.InferType()(mod)
output = func_11040()
func_11041 = relay.Function([], output)
mutated_mod['func_11041'] = func_11041
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9642_call = mod.get_global_var('func_9642')
func_9644_call = mutated_mod.get_global_var('func_9644')
call_11124 = relay.TupleGetItem(func_9642_call(), 0)
call_11125 = relay.TupleGetItem(func_9644_call(), 0)
output = call_11124
output2 = call_11125
func_11132 = relay.Function([], output)
mod['func_11132'] = func_11132
mod = relay.transform.InferType()(mod)
output = func_11132()
func_11133 = relay.Function([], output)
mutated_mod['func_11133'] = func_11133
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11145 = relay.var("var_11145", dtype = "float32", shape = (14, 2, 1))#candidate|11145|(14, 2, 1)|var|float32
uop_11146 = relay.exp(var_11145.astype('float32')) # shape=(14, 2, 1)
output = relay.Tuple([uop_11146,])
output2 = relay.Tuple([uop_11146,])
func_11159 = relay.Function([var_11145,], output)
mod['func_11159'] = func_11159
mod = relay.transform.InferType()(mod)
mutated_mod['func_11159'] = func_11159
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11160 = relay.var("var_11160", dtype = "float32", shape = (14, 2, 1))#candidate|11160|(14, 2, 1)|var|float32
func_11159_call = mutated_mod.get_global_var('func_11159')
call_11161 = func_11159_call(var_11160)
output = call_11161
func_11162 = relay.Function([var_11160], output)
mutated_mod['func_11162'] = func_11162
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5379_call = mod.get_global_var('func_5379')
func_5380_call = mutated_mod.get_global_var('func_5380')
call_11283 = func_5379_call()
call_11284 = func_5379_call()
const_11303 = relay.const([[[-9.471510,2.773706,4.362722,-1.508284,7.557585,-3.953262,9.500608,-8.308042,3.123989,2.838013],[-4.013907,-7.035013,-6.892059,6.928711,4.008079,7.426210,8.519685,9.896738,3.028687,8.328488],[-2.939263,8.318355,6.655387,-6.135773,0.397283,1.083128,-2.396047,1.278542,2.706769,-5.723371],[8.380292,-8.497798,9.712538,1.894792,7.624369,7.399144,-5.761106,2.813927,3.831848,-6.556905],[-9.069278,-6.976580,6.202058,9.882938,-8.840950,-3.894497,7.899593,-0.196578,-5.653894,4.980421],[-3.298570,5.554273,2.634124,-9.430717,-5.132389,-4.342464,1.600340,2.337642,-6.352081,2.400762],[3.737746,-0.744428,4.451040,9.926185,-8.558892,3.488127,5.290810,7.704936,-6.013970,7.198135],[-5.821560,7.532044,-2.118996,6.136952,3.301458,3.512734,-8.354974,3.066381,1.319703,5.145674],[4.379989,-3.737586,6.044604,-0.756357,-3.775357,8.939363,8.419159,-1.656610,8.335427,-3.998603]],[[-6.796361,6.958669,7.929923,-3.036888,5.807654,-3.958292,6.036474,-5.472521,-9.668519,-9.273974],[-5.686848,6.113615,-5.951960,-7.670562,6.545122,-3.703037,-6.657446,-3.191460,-8.804341,-6.914147],[-8.255349,-2.037691,-2.708013,8.001415,0.347248,2.671755,9.087229,2.256695,-3.686539,9.518005],[-1.119913,2.950421,-7.603482,-7.899322,1.931137,-9.960168,6.777973,1.018668,1.273937,-0.813583],[-3.446441,9.293925,9.569917,9.450336,-8.199379,8.880812,-6.122072,0.707582,4.865471,0.488354],[7.775562,-8.646171,-9.075734,-8.121143,-8.992457,7.309595,-8.083286,-7.089582,7.050454,3.525107],[9.514225,4.224025,7.950284,-4.231564,-0.820437,1.905723,3.831519,3.044450,9.697384,-3.892093],[-8.465579,-8.640126,-8.358281,-6.667382,-6.224494,8.277823,8.714102,3.659479,0.034460,6.647127],[5.379563,3.177408,-7.806339,9.683942,-0.788722,-6.204300,9.068892,0.663884,6.382426,2.161114]],[[7.198204,7.140854,4.590465,-1.394530,-3.713652,8.114696,-5.451707,0.817050,5.398587,8.175235],[-1.059768,-3.720607,-7.265560,3.253449,-7.249895,-8.851285,0.378392,-5.140063,-5.656518,9.020813],[-3.038469,7.782505,-7.853701,2.381470,8.390345,5.974535,-1.817105,3.740790,-0.753930,0.907191],[2.385339,-8.009672,9.191183,-5.524772,6.445870,6.260566,-0.085588,2.730677,0.957342,-7.228573],[3.112753,-3.148959,1.027905,-6.599592,-2.187000,-8.185543,1.519283,-1.097586,8.009744,8.556473],[-3.692008,-2.786679,1.682764,6.055432,0.352714,7.620925,-0.048948,-4.080568,5.569470,7.616757],[-7.293100,1.686612,-2.107154,0.741735,-9.231163,4.091011,9.983547,4.823973,1.519129,0.251153],[-8.035240,6.859016,-3.615810,3.503173,-4.605838,7.731020,-3.643610,9.393168,-9.112761,4.709453],[6.722988,6.607960,-5.526907,6.085400,-2.765326,-6.732471,0.221536,8.054356,-0.179482,9.638900]],[[5.676346,5.540141,5.496252,-7.125284,1.412084,5.064255,-3.881771,1.599408,8.398715,-9.821181],[8.585015,6.441488,-6.330227,-6.417548,5.100826,-4.086455,-6.561677,-4.820415,-5.524046,4.998189],[-4.671194,-7.751422,-7.987840,-2.977542,-6.900578,3.025447,2.997714,-0.272879,6.100247,-4.184961],[-3.682589,1.388938,9.513196,-3.147368,-0.504722,6.989165,-3.123361,-2.167618,-4.098841,7.357253],[7.274445,-6.042823,5.016301,9.084959,-0.443341,9.768626,-3.489113,4.521591,-1.863019,2.908679],[-6.008098,-7.760616,-3.742038,6.796352,5.808848,5.065688,3.793570,1.905173,-6.408669,8.576286],[2.085786,9.249702,1.265095,9.540480,-6.396993,-1.090870,4.381118,-6.397711,4.292569,-8.430525],[-6.758337,-9.498082,-2.873552,-6.230527,-2.986709,9.307367,-6.449847,6.808018,9.560781,9.405097],[8.243102,-2.079956,-9.214691,-2.839221,-2.311709,-8.492170,-7.073023,-9.417408,8.890158,7.306443]],[[-5.196333,1.575739,2.597025,-9.578051,8.734250,-0.858536,-9.315785,8.836741,6.045869,-4.511540],[7.696525,-8.831152,2.935559,-9.428099,8.930052,-7.439968,-9.594543,-9.874052,-0.631637,-5.605945],[7.362315,-4.532193,-2.839791,-8.137510,4.814934,5.774936,-6.461310,-7.987364,5.498048,-3.218923],[-9.951530,-0.227005,-6.332216,-7.203755,-6.175930,-9.486764,-5.706069,5.902079,-2.381883,-0.454250],[-4.791584,-6.469344,-9.766050,9.770910,4.633208,-9.607293,-1.374452,-5.322999,-1.194282,-1.823641],[-6.022264,-3.060776,2.357787,2.472232,2.503913,-9.397768,3.212224,-9.931171,3.794266,4.618608],[8.397266,0.498509,6.026485,-4.749358,-2.274008,-8.105790,3.587507,6.738271,-4.660971,3.936029],[8.516389,6.465245,-4.715561,-6.640334,2.704720,0.709530,1.237269,5.528041,-9.572242,-4.835414],[-6.612993,7.421393,7.372163,-0.268305,4.802762,-9.682949,7.892707,-2.484029,5.801318,-2.979324]],[[-2.338414,-1.979522,-8.957402,-8.746257,8.053488,7.720281,6.322599,-8.274368,-9.631896,-3.463488],[-9.680548,-3.190384,6.869211,6.797946,2.820263,3.800503,6.664944,5.146704,3.720310,4.968769],[4.367108,-1.868563,7.782062,5.691919,-8.975782,-4.585095,-2.940666,-4.415177,7.851649,1.899971],[4.183928,-1.793348,-3.642062,-9.297881,-7.461524,-2.138428,1.520706,-3.352310,7.551789,-5.978200],[-5.163945,-2.626729,9.630812,-2.535386,0.652030,4.780372,-4.550640,3.679262,4.298338,3.365646],[8.249645,0.716858,-5.521462,-1.601152,-4.678982,9.913888,0.561349,3.039845,3.230311,0.221246],[7.784507,1.404583,-7.589310,-0.277459,9.416301,9.215508,-6.150053,6.292340,9.473248,-2.693161],[-7.471527,-1.188184,-1.671838,-7.470758,1.443271,-0.671662,-4.894696,-2.993346,-7.842543,-3.213536],[-1.648515,0.774454,4.223394,-8.073336,-2.480220,-0.761482,-0.824510,-4.141883,-4.552613,-7.904408]],[[-5.686093,5.520045,2.700630,4.850014,-0.979991,9.706980,-1.423377,2.681156,9.603278,-0.905239],[9.217238,-7.857037,4.822168,-1.425495,3.162365,7.988686,2.246595,-6.111071,-1.314075,-5.717829],[7.729835,-6.343708,-1.775625,9.819803,9.594434,7.266623,-9.509356,-4.080724,-1.222345,-7.730273],[-8.209751,6.019158,-2.119531,-0.571385,-4.038547,8.965936,-1.760603,0.539310,-7.094902,-5.660486],[-1.200405,-1.107358,5.266766,-9.036669,6.924955,7.256483,-1.938419,8.523682,-5.708780,6.205070],[-2.537579,-2.027184,-5.021958,-7.969350,7.089856,-0.038025,-0.439492,-4.895385,-2.619154,-2.755207],[7.458660,6.381901,-9.025754,-8.983123,-2.970494,0.760743,2.023971,1.418908,4.463633,-3.658757],[-7.195938,-0.470063,1.426647,-7.560325,2.641042,7.684016,-1.964280,-1.967514,3.453508,3.410250],[2.279593,-9.616401,-1.693548,-8.823745,2.149360,-2.321912,-0.132092,6.535374,-7.170271,2.820445]],[[-3.204790,-9.737532,0.803582,2.948558,-3.614753,-1.948362,-5.286370,-8.698075,-1.493119,-6.409738],[6.550542,6.083990,-7.733301,4.866473,-6.346733,-8.051424,7.996563,5.005451,-1.073532,9.131476],[6.339616,-7.316648,-8.805785,-6.884310,9.508922,1.569768,-2.570418,-7.562718,6.365947,5.014853],[-7.152945,-7.329897,-2.758647,-5.463167,-0.071902,3.561411,0.346827,2.941677,-8.293009,-7.355726],[5.957294,-5.527713,-1.681010,-8.276390,-3.173365,5.756750,6.643764,-4.127614,0.649474,-0.178816],[-3.801548,4.899301,9.374775,-1.928974,5.076478,-0.995905,-8.681667,-8.602138,6.105108,-6.827823],[-8.178239,9.553953,6.197102,9.734681,-4.874537,-9.929317,-7.912195,9.888228,3.325877,4.331650],[-4.452720,3.674757,8.996735,-4.036966,-6.273080,-7.420100,-3.948720,-5.662797,-3.468956,9.523434],[-7.336685,3.585580,9.990311,-2.001628,-3.735780,5.860371,4.012183,0.084281,-0.212651,-9.690332]],[[-1.435026,2.966778,-6.402994,-9.070107,-8.330136,9.800396,-5.962949,4.761289,7.607454,-9.860715],[6.712180,3.090943,-0.087819,5.453835,-4.243658,8.953701,9.044092,5.972480,-5.375032,-7.296661],[7.335860,4.743197,-2.585728,-9.502256,2.133435,-2.149909,-3.704612,3.208532,-1.209403,-2.784452],[-7.103953,-5.039223,-4.089944,2.295377,8.001836,5.061653,-4.607536,-2.636674,0.322482,-9.590992],[3.449315,-4.970442,-3.628639,-0.946903,-2.666498,4.916969,-5.213959,-5.315606,-3.034410,-8.849674],[4.669354,-0.202495,-6.042730,7.271881,3.515738,-4.797171,-3.093349,2.349936,2.797439,7.740601],[-4.443948,-1.218263,-8.897111,1.436064,4.942209,4.177440,-9.580757,-6.880133,-4.545052,-7.629838],[7.641595,2.419888,2.667403,9.340103,-4.976517,4.139170,7.441184,-7.474583,-8.425349,-8.536684],[8.894683,5.549702,-3.023479,-4.239235,6.816794,-5.232118,-2.783685,-6.583141,-7.161906,-4.113671]],[[-1.244890,0.384734,1.947908,-0.984271,-5.182214,2.332619,-2.199183,4.129722,-7.521632,7.317455],[-3.425437,5.446559,3.219353,0.457166,3.257733,9.042073,5.275173,3.263913,-5.420476,-0.533317],[0.832206,-9.043111,-3.391040,-1.397294,3.457828,-9.243480,0.671581,-7.351156,2.381720,4.653706],[6.541517,8.135829,2.930584,-1.136743,-3.752472,-8.436822,-9.639557,6.350209,-8.082535,-0.799478],[8.669469,-2.847592,-6.556435,-2.559211,-9.312281,-7.498953,-3.156935,-1.471702,-6.135475,8.056338],[9.221599,-5.008909,-8.330591,6.509203,5.955778,-7.971177,-4.045967,-9.251521,-5.073962,2.724696],[-7.989376,-6.264277,3.853954,-2.678699,3.334131,-1.503669,-9.119708,8.858285,-8.079716,0.072791],[-4.836360,-8.222492,-8.481280,5.430905,8.963809,2.789263,-5.160363,-4.967501,-4.768239,0.083274],[-2.206344,7.164260,9.372311,7.308015,6.929659,2.378987,0.077129,-7.211547,-4.953501,-2.162867]],[[-8.019429,2.598910,1.593955,-0.678726,0.582798,-9.644885,8.999050,-3.253704,-9.865402,-6.127342],[-7.071139,0.730693,-2.021190,-2.163925,5.234176,-7.633986,-3.030875,-6.064984,-4.321461,-1.752835],[-4.363367,6.636763,-3.476653,-2.200739,-8.342768,-5.034611,2.087475,-9.559486,5.117573,-6.269767],[7.009106,3.552335,4.370406,3.171386,-3.790100,0.800919,-2.486063,4.385103,-8.687005,9.940730],[-6.971958,3.352367,0.892818,9.417020,-3.679307,1.883510,0.214375,-2.307974,-8.829546,-2.251957],[4.031761,-5.734153,-9.172743,-8.535046,1.237170,3.675921,5.026470,6.013605,-7.536294,5.479667],[0.948034,-5.569513,8.094540,7.307701,9.543716,9.598067,0.208854,-8.672207,1.271540,-7.019813],[6.323610,-3.116485,-3.998763,5.562238,8.484797,-4.252673,-4.692568,9.087321,2.186917,6.119118],[-2.238830,7.142869,-5.650440,2.479855,-4.617099,2.067479,-1.226143,-4.840560,5.866092,1.893034]],[[-9.595500,1.966866,5.612711,7.974123,6.856570,3.713072,9.913752,7.329824,-3.672212,4.616957],[-3.591810,-9.181856,-5.470008,-6.447500,2.628768,-9.802999,0.327645,-7.740661,-7.932178,5.058112],[-6.067289,8.503226,4.016762,-6.909032,-6.081474,-4.906469,-0.673169,6.565807,5.799407,-9.530134],[7.902995,-5.625236,1.362610,8.415955,-3.247211,4.434538,5.043867,-0.095883,-0.268735,0.550827],[-8.554906,4.624802,-5.259720,-3.853078,-7.292393,-9.272406,5.398819,-0.989065,2.408818,9.355603],[-7.696112,6.908167,8.150689,-1.520606,-8.745422,-8.505415,6.196774,0.515741,-2.291950,6.763712],[-5.725460,0.345537,9.037822,-8.074785,8.780753,-6.348016,0.397079,-7.020065,-6.099506,-9.858328],[-5.470099,0.127839,-0.952610,3.370272,-6.671163,-3.887667,7.501463,6.451018,4.603531,3.402597],[6.859923,2.923028,8.000093,0.362302,-5.653117,-3.507127,2.042639,2.771497,-9.406715,-4.549276]],[[9.171362,-6.998676,-8.172371,9.515685,8.179644,1.791933,1.727811,4.769208,-5.283660,-6.190526],[-1.061273,4.486426,-4.903824,-4.380471,0.361331,-1.899316,1.452017,7.734296,-1.558899,2.105433],[-4.211810,-5.978917,4.053061,-3.169615,-3.412097,2.989356,-3.964845,-1.726479,4.230392,0.818477],[-9.506731,0.323969,-9.019680,2.375579,-7.851087,3.461648,1.628681,-8.541112,9.928239,-8.619853],[6.012976,1.701113,-2.405878,-6.679256,-7.962484,0.003783,6.839358,-3.966944,2.129468,-1.296361],[-1.026214,-3.868990,0.512362,4.841905,-1.561708,7.205424,5.308307,6.037145,-5.994025,8.326391],[4.713046,9.597055,8.479348,4.819468,-8.791319,-1.233759,3.339012,-3.641116,3.422508,9.125432],[-8.512325,4.354484,4.975732,2.148626,3.373765,-7.269732,3.524467,6.014413,5.576516,-0.420152],[5.738735,0.502951,1.077278,0.326191,6.191892,-3.840941,9.492438,7.941726,-1.702844,6.129189]],[[2.590923,6.241098,5.289792,4.681509,2.240177,-0.513036,2.360404,7.693436,-6.472210,2.414105],[3.579304,7.650722,-9.773826,-4.831811,0.244507,-3.472541,6.207293,-0.411362,-2.899771,-1.206640],[4.702857,-1.711291,-3.272057,8.867833,6.344944,-3.733242,5.647316,4.297005,-3.299404,-9.793295],[0.977903,-2.264159,-5.532586,-9.330352,-6.977911,-2.808935,1.734387,-3.288098,-6.414554,-2.678004],[2.044311,3.292586,-7.786591,-7.677864,-4.307067,1.707138,2.154757,-1.472102,-7.700351,-0.095147],[4.266741,-0.698065,-8.130075,-1.945093,-2.777856,-7.617105,9.069242,-3.267331,-3.029112,-2.167657],[-7.559734,1.497636,7.884092,4.880862,-5.364014,1.468035,0.255851,-5.151802,-0.774322,-0.572634],[-4.347628,-1.983352,-7.512087,8.602730,1.998029,2.074151,4.758804,9.429017,3.969159,-5.614996],[6.339681,8.970376,4.857924,-2.254591,1.951532,9.825998,0.936152,2.069570,-8.942509,-2.661764]]], dtype = "float32")#candidate|11303|(14, 9, 10)|const|float32
bop_11304 = relay.divide(call_11283.astype('float64'), const_11303.astype('float64')) # shape=(14, 9, 10)
bop_11307 = relay.divide(call_11284.astype('float64'), const_11303.astype('float64')) # shape=(14, 9, 10)
uop_11308 = relay.acosh(const_11303.astype('float32')) # shape=(14, 9, 10)
func_2351_call = mod.get_global_var('func_2351')
func_2354_call = mutated_mod.get_global_var('func_2354')
const_11312 = relay.const([8.942068,9.691403,-0.144915,7.205603,-7.902011,5.007724,-9.477694,-9.407796,8.932820,-6.633810,-2.237789,-5.812157,-7.508650,-7.428611,7.059758,2.544593,8.717775,-2.098614,-6.569073,2.646885,4.322042,-9.061863,3.917201,8.715276,9.919194,2.426468,8.082851,-2.987834,8.896729,-8.439863,-9.526047,5.894568,-5.369873,-2.662038,-0.179651,7.369267,-4.900755,7.198772,-8.651421,-6.198914,1.716239,-9.186658,5.048783,-1.471887,2.017869,3.793873,-2.693311,0.830053,-7.698539,9.989771,-1.255480,-3.000351,-5.376472,-9.436479,9.371095,-0.301617,-6.996287,9.900240,-5.644470,-8.618130,-3.395969,2.391615,1.637777,-3.021086,-4.843386,-3.233638,-2.360315,8.682049,-0.738918,-8.803933,-8.607380,-4.123194,6.252908,1.187621,3.651063,7.717217,7.955949,6.286079,-7.131502,1.647214,6.728945,1.086084,-7.107998,1.546876,-6.848239,-3.593541,-3.588886,-3.634596,4.981715,8.786745,8.560093,-5.743370,-1.509416,6.445015,8.716771,4.896610,-6.588640,8.868823,-7.695183,-4.002703,-6.126932,8.935033,8.352108,-4.128866,6.340595,-2.508580,-0.900620,-4.590093,-0.432749,3.963816,-1.358270,-1.638813,0.176342,2.285245,-6.302841,8.119298,5.344308,-4.074365,-0.235059,0.998457,-9.825775,-4.293199,-4.150976,1.669483,8.030812,8.240057,-7.987059,-9.900041,7.492010,3.174019,8.167066,-5.361689,0.890455,-0.592963,7.148498,-4.170488,5.213469,-8.335239,9.463268,-2.650361,6.332878,-2.432199,2.656980,4.845421,-1.505096,2.760301,4.385245,-3.944210,-7.654691,-1.985120,-2.188467,4.383736,-4.332532,-1.351877,-7.974561,-0.424847,-3.121201,5.049003,2.544542,-1.363064,6.956080,-8.338814,9.575565,4.448740,9.658623,7.975365,-6.350441,9.491420,-3.962581,-3.704466,-7.756443,-5.128688,9.431051,-3.063467,4.158295,2.882350,-4.590827,3.258127,-5.887153,5.647139,7.488777,-7.920815,-2.531789,-3.613953,0.279137,1.088891,4.574032,-7.958651,8.010225,1.821109,8.132835,4.866062,-2.105811,7.111038,1.362350,-8.596699,2.525234,5.162919,-9.174620,-1.038112,-7.491221,4.914660,-6.538257,4.514035,8.893473,-5.227194,7.247496,-4.354427,-3.987390,-5.139701,9.906313,-3.487546,0.187941,-2.307548,8.586402,1.802459,-7.392052,9.057882,-0.707818,-4.528069,-7.438352,-6.850112,-9.742906,3.427006,-6.471617,-2.792984,4.839501,-2.879951,-4.150727,-6.082769,-5.601607,-0.250933,1.069478,3.839506,-4.580040,7.280174,-5.832594,-6.041246,-6.728049,2.081492,3.876881,-2.578649,4.608521,-6.836656,3.823861,9.039207,-6.268853,-9.832815,-4.091889,-6.794954,5.551778,3.323495,0.678734,-4.084928,5.597343,6.854736,-5.035856,2.599593,-8.449876,1.985641,8.857916,2.270072,-1.171091,1.018948,9.626103,9.886099,6.386859,-6.787170,-0.324563,-1.712467,9.391511,9.023331,-6.259130,9.799730,-8.550020,-1.639009,1.814309,1.783267,-8.256039,-8.702018,-2.239181,-6.961535,-1.865021,9.301430,-7.263587,2.125206,8.420043,2.587939,4.667447,-6.247719,8.766019,3.125802,7.266695,3.036039,3.124294,7.136128,5.494085,5.592085,0.537788,8.867814,9.272800,8.235599,8.943795,-5.887724,3.099774,-7.410853,3.661494,1.293492,-8.866031,-2.088578,0.532428,-3.438350,-0.597038,-2.324589,-1.354734,7.509882,-0.522205,-2.548782,5.883996,6.296223,0.245882,8.530622,1.197382,8.586428,5.020287,-6.365288,-4.560951,-4.244462,-6.890468,-0.336918,-2.214215,-1.352600,-0.132952,-2.561167,7.147529,-4.009321,8.367259,-1.405284,-4.175425,-2.612561,0.440236,-3.918369,1.004527,-4.834523,-1.848661,-7.045585,-4.145627,4.068635,9.378705,-0.725990,3.456336,-7.687855,5.807578,-4.900871,-9.475073,5.121578,7.040460,1.707711,-7.520547,-7.145689,-3.903329,5.632084,-9.133551,9.637199,-3.437913,-2.976869,-2.699079,-1.490177,3.828508,-3.037651,-9.976255,-7.797199,8.917411,-1.951122,6.040558,-8.500352,-0.148270,7.191173,4.967809,-6.804989,-9.675796,8.652833,4.725140,-8.999664,-0.655436,7.225440,7.318651,-3.870673,2.173407,-4.747102,-7.030138,7.931350,2.269164,4.413734,4.870597,-5.744316,-1.210791,3.875487,-9.556893,3.989496,-7.328514,9.782629,-1.143068,-9.278126,-5.631336,-3.884896,-0.085281,2.641348,-5.369083,-1.151299,9.409003,-1.152244,-1.036460,8.593644,8.969120,-1.784712,4.999621,6.672753,0.692735,-9.572312,6.616500,-6.891723,-6.540285,7.317545,-5.961152,-0.098959,-6.487128,-3.475200,-7.560140,2.623339,-4.911874,1.529212,8.371661,2.090568,7.578643,4.333440,-5.037363,-2.719300,8.071139,-5.546906,5.698254,3.736687,4.960367,-8.035506,-2.497040,8.798680,4.815056,-3.254549,-6.700881,-5.371307,7.038451,-0.551393,8.785937,-2.825037,-8.397330,9.391709,-6.612017,5.546669,-9.053887,1.594980,-0.162939,3.715404,-8.677527,-1.835729,0.655184,-7.784560,-6.678256,-5.124136,0.716549,1.477959,2.055349,0.047767,4.051818,8.361047,-9.388395,-2.341283,-6.308912,4.337153,-9.814298,3.149321,-3.139965,-2.304877,-0.702954,-1.039504,-0.158363,3.310169,-6.967433,6.003183,8.300616,0.361335,7.638315,-8.469087,9.610307,-6.865838,-4.311054,0.512896,2.192973,5.479738,4.513841,2.082522,4.635615,4.487872,9.105305,-1.729212,-0.123393,4.924559,3.059732,4.930251,3.574164,-5.463236,4.042299,-7.919090,-9.667910,-8.279419,8.360565,8.945750,-7.799329,4.516054,9.928927,-1.508962,7.886012,5.689972,-6.349382,-5.716814,7.727540,2.826119,-8.933468,8.444712,4.917217,-4.842846,-3.974949,-8.272967,3.608827,-7.802492,5.547725,-2.305545,-4.155249,5.332101,-6.296659,-2.681753,5.890674,-2.087537,6.667904,-8.380057,6.004724,-5.746766,-0.091487,-4.233901,-0.339033,-4.221996,8.017249,-4.019594,-1.515305,-3.647296,3.017602,-0.746065,-9.241461,7.046208,0.277737,9.768825,-8.645384,-1.256981,-5.652681,-8.535247,9.745752,-8.021097,5.352100,1.111599,-9.827589,-0.680092,-9.423152,-9.941241,5.543626,6.700539,6.835320,0.497666,-0.911069,-0.958099,-1.788070,4.908082,7.082934,2.133588,-2.379232,8.199155,-2.875647,7.769971,-0.655129,-1.083821,3.098817,-5.146218,-3.314961,-9.212148,9.345273,0.821620,-0.710258,-5.320603,-7.333918,-2.879050,-2.162497,8.949210,-9.409280,4.430466,3.137951,-2.779627,1.281287,6.692336,4.945847,-3.306560,4.588948,-7.033802,-9.114964,2.290091,-2.047382,-0.445236,1.637423,-6.019829,-4.429783,2.050705,0.500030,-4.874599,-5.164885,-7.036630,4.709666,2.400356,-8.124658,-1.507765,-6.677397,3.323184,-6.274595,1.766472,3.989875,2.177496,7.131191,9.651847,-5.713775,-9.309000,-0.129483,-6.704259,7.946452,-6.514582,-1.264574,0.462342,-0.274055,1.042925,-2.998290,2.434593,-5.097709,8.536840,7.827783,-6.519958,-9.697874,-4.382589,7.468285,-6.856787,-3.405157,-9.877872,-5.309105,5.925129,-0.397346,0.406070,3.031123,9.396613,2.522343,-9.184637,1.476924,-3.060562,1.269680,-5.690289,-0.571183,9.435317,2.241822,9.613981,8.281251,6.134883,8.647135,-8.483460,4.195004,6.535336,-6.482606,5.732305,-1.495830,0.909418,-4.033095,8.188165,3.525580,-0.476804,-0.787178,-3.318697,-1.711879,-1.869416,-0.681288,6.039442,-3.552533,-0.352115,-1.888734,-9.493976,7.390610,-0.277245,-3.241819,-1.510628,-8.039863,-0.780404,-1.216629,5.679996,-2.107984,8.771111,-0.711667,-9.497835,7.075819,-8.634981,-3.684361,-8.599145,-1.343813,-2.963125,-1.777891,-5.680240,2.373538,-8.881261,2.580237,-0.181521,9.551411,-7.946467,-0.420994,-0.346186,1.789035,3.693867,4.339454,-3.021945,-7.393655,-6.234665,3.057034,-1.732285,-1.755574,9.466531,-4.031926,0.687056,1.796064,0.153615,4.563039,5.580785,-3.252911,-2.646251,-4.971166,-8.901551,8.759195,-2.101893,7.291609,6.133195,8.009295,-7.308612,7.614836,5.804460,1.241237,-3.242753,-2.602751,-0.614064,6.037030,-8.126160,6.708521,-4.003817,-0.370183,5.798977,0.251959,7.960707,7.375686,-2.894351,4.666569,7.686967,8.747101,9.341316,1.255350,-3.763531,5.599434,9.120126,7.770760,8.050682,-3.558971,-2.012177,-0.871484,-6.007752,0.792338,-7.471838,-3.130448,1.696719,4.084923,8.206037,-5.694752,2.714549,-7.123368,-1.601157,4.380850,0.608865,3.756449,6.117697,4.502983,0.012536,5.500847,-7.112873,-6.562170,8.188842,-1.453877,-3.336933,-5.346800,-1.660653,-7.584236,1.999772,2.399116,1.691722,-6.606788,-4.441725,-9.599031,-7.747467,2.360753,1.736983,-9.319320,3.934618,0.016995,-4.611467,-2.596076,7.732204,6.813574,-9.031717,2.651049,0.782438,-1.048873,-5.670700,-2.766934,-2.094689,0.931292,0.737672,-9.450028,-7.386152,-2.861095,-5.259878,-4.196053,-9.994125,-7.958256,-2.161458,-9.285132,8.047782,2.228190,-0.660185,-0.601225,5.691572,-6.463497,4.518570,2.083617,4.145579,-7.677204,-2.198341,9.043961,2.147776,7.714633,6.153530,0.466358,5.714969,-4.728785,-5.246976,-9.622115,-8.326007,-9.785961,-0.570574,-7.541933,-0.983140,3.368119,6.416592,3.617256,-4.773344,-8.219439,-1.173080,-8.719003,-1.671992,0.301679,6.089163,-2.363627,5.447887,4.696492,-7.859564,0.520424,1.920541,-8.041955,2.540081,4.597090,-5.794455,0.315501,9.586342,-1.614122,5.090765,6.678456,-8.307164,-6.195444,-2.445744,7.663313,5.806621,3.534335,7.317683,5.321542,4.512849,-6.915391,-9.881211,0.518527,5.203520,8.739121,3.087433,2.177538,-9.169437,0.331520,8.152976,-7.027724,7.794348,8.601797,2.318204,1.911110,5.098989,-4.470017,-4.575826,-3.304717,-0.576951,-4.497646,-1.195089,8.934645,5.638884,1.338777,1.290189,-5.850040,-6.553744,0.483811,-4.114128,-6.136935,-4.827984,-3.142719,-2.231221,-2.742000,-2.401468,4.228810,-4.322345,-9.416585,3.984675,-3.422905,1.144102,-6.620262,4.630224,2.421597,-2.768942,1.319417,-4.620300,0.676332,-2.494063,2.049970,-6.388100,3.300233,7.535861,5.332965,-3.198315,0.473691,-1.990843,5.718315,2.804272,9.567926,-1.995727], dtype = "float32")#candidate|11312|(960,)|const|float32
call_11311 = relay.TupleGetItem(func_2351_call(relay.reshape(const_11312.astype('float32'), [960,])), 3)
call_11313 = relay.TupleGetItem(func_2354_call(relay.reshape(const_11312.astype('float32'), [960,])), 3)
bop_11314 = relay.logical_xor(uop_11308.astype('uint32'), relay.reshape(const_11303.astype('uint32'), relay.shape_of(uop_11308))) # shape=(14, 9, 10)
output = relay.Tuple([bop_11304,call_11311,const_11312,bop_11314,])
output2 = relay.Tuple([bop_11307,call_11313,const_11312,bop_11314,])
func_11328 = relay.Function([], output)
mod['func_11328'] = func_11328
mod = relay.transform.InferType()(mod)
mutated_mod['func_11328'] = func_11328
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11328_call = mutated_mod.get_global_var('func_11328')
call_11329 = func_11328_call()
output = call_11329
func_11330 = relay.Function([], output)
mutated_mod['func_11330'] = func_11330
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4785_call = mod.get_global_var('func_4785')
func_4787_call = mutated_mod.get_global_var('func_4787')
call_11358 = func_4785_call()
call_11359 = func_4785_call()
func_4302_call = mod.get_global_var('func_4302')
func_4304_call = mutated_mod.get_global_var('func_4304')
var_11365 = relay.var("var_11365", dtype = "float64", shape = (280,))#candidate|11365|(280,)|var|float64
call_11364 = relay.TupleGetItem(func_4302_call(relay.reshape(var_11365.astype('float64'), [1, 280])), 1)
call_11366 = relay.TupleGetItem(func_4304_call(relay.reshape(var_11365.astype('float64'), [1, 280])), 1)
func_2282_call = mod.get_global_var('func_2282')
func_2283_call = mutated_mod.get_global_var('func_2283')
call_11385 = func_2282_call()
call_11386 = func_2282_call()
func_8017_call = mod.get_global_var('func_8017')
func_8019_call = mutated_mod.get_global_var('func_8019')
call_11391 = func_8017_call()
call_11392 = func_8017_call()
output = relay.Tuple([call_11358,call_11364,var_11365,call_11385,call_11391,])
output2 = relay.Tuple([call_11359,call_11366,var_11365,call_11386,call_11392,])
func_11397 = relay.Function([var_11365,], output)
mod['func_11397'] = func_11397
mod = relay.transform.InferType()(mod)
mutated_mod['func_11397'] = func_11397
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11398 = relay.var("var_11398", dtype = "float64", shape = (280,))#candidate|11398|(280,)|var|float64
func_11397_call = mutated_mod.get_global_var('func_11397')
call_11399 = func_11397_call(var_11398)
output = call_11399
func_11400 = relay.Function([var_11398], output)
mutated_mod['func_11400'] = func_11400
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2009_call = mod.get_global_var('func_2009')
func_2011_call = mutated_mod.get_global_var('func_2011')
call_11407 = relay.TupleGetItem(func_2009_call(), 0)
call_11408 = relay.TupleGetItem(func_2011_call(), 0)
output = relay.Tuple([call_11407,])
output2 = relay.Tuple([call_11408,])
func_11409 = relay.Function([], output)
mod['func_11409'] = func_11409
mod = relay.transform.InferType()(mod)
output = func_11409()
func_11410 = relay.Function([], output)
mutated_mod['func_11410'] = func_11410
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6785_call = mod.get_global_var('func_6785')
func_6786_call = mutated_mod.get_global_var('func_6786')
call_11440 = func_6785_call()
call_11441 = func_6785_call()
output = call_11440
output2 = call_11441
func_11443 = relay.Function([], output)
mod['func_11443'] = func_11443
mod = relay.transform.InferType()(mod)
output = func_11443()
func_11444 = relay.Function([], output)
mutated_mod['func_11444'] = func_11444
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10058_call = mod.get_global_var('func_10058')
func_10060_call = mutated_mod.get_global_var('func_10060')
call_11476 = relay.TupleGetItem(func_10058_call(), 1)
call_11477 = relay.TupleGetItem(func_10060_call(), 1)
output = call_11476
output2 = call_11477
func_11493 = relay.Function([], output)
mod['func_11493'] = func_11493
mod = relay.transform.InferType()(mod)
mutated_mod['func_11493'] = func_11493
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11493_call = mutated_mod.get_global_var('func_11493')
call_11494 = func_11493_call()
output = call_11494
func_11495 = relay.Function([], output)
mutated_mod['func_11495'] = func_11495
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9932_call = mod.get_global_var('func_9932')
func_9933_call = mutated_mod.get_global_var('func_9933')
call_11525 = func_9932_call()
call_11526 = func_9932_call()
func_6258_call = mod.get_global_var('func_6258')
func_6261_call = mutated_mod.get_global_var('func_6261')
const_11531 = relay.const([[8.354875,-0.555150,-6.671600,-8.088957,-4.427976,9.147550,1.675562,-2.284511,-1.955951,9.868437,-3.687098,-3.151799,8.273446,4.799861,-8.951028,8.240665,0.758894,-7.174861,7.906333,4.964630,5.038845,-8.093365,-2.131610,-9.216684],[-9.181644,7.396990,-2.599411,5.414874,5.681891,0.185470,-0.072569,-7.206551,-1.664115,0.467131,0.994299,-9.764010,3.718926,7.645356,1.115875,-1.470537,8.952856,-5.519167,-8.671767,-2.148237,-6.500240,4.222484,-3.945199,2.997702],[2.677082,5.341739,2.786674,4.606550,-6.824077,-2.084289,-4.566418,-6.654469,-6.400820,1.749367,-0.795867,3.468517,-5.697555,2.321136,-7.089840,1.789361,0.970523,-8.692802,-0.931481,-9.227854,-9.449801,-2.885632,6.831378,6.511003],[-0.806837,-4.584835,-1.257690,4.280098,2.560307,2.925506,2.476408,1.851053,8.746743,1.980371,4.494711,7.989698,-5.879362,-9.986919,-6.590547,-6.221514,5.200032,6.309300,-9.064058,-0.488823,9.319927,0.197544,-0.441643,8.933666],[-2.287229,-5.760975,-6.263341,2.177715,7.527229,1.276090,8.639230,-0.072364,-5.697854,-0.569813,1.518517,-5.790073,0.846825,8.089802,-2.635893,2.850951,-9.193571,-7.471254,4.147629,8.639480,-4.657678,-1.330628,-7.895008,-6.509195],[-6.870570,2.395685,5.511346,-2.854554,2.709859,-8.810506,4.018856,-7.255408,6.355257,-6.990894,2.675362,-9.619089,-4.873943,1.260126,9.226585,-6.913517,6.083939,5.877822,8.535207,4.899606,-4.079386,9.224359,8.801841,6.403211],[-3.439277,-9.423794,7.032382,3.027504,9.457040,5.718294,-8.694911,1.401538,4.164819,-2.379346,-4.534333,-2.508353,-7.014731,-9.642067,9.807605,-7.794352,-0.720139,4.182780,6.511819,1.313942,-0.517598,-8.335740,-2.897389,-1.141709],[-8.890125,0.020967,-8.229960,6.687391,1.582583,-2.507398,8.316548,-4.260576,3.613427,-8.180446,1.212710,-5.100075,-2.790033,-1.776235,-1.802360,-0.382561,-0.238965,7.984582,8.694516,1.613965,6.104956,-4.335138,-6.021021,-0.752316]], dtype = "float32")#candidate|11531|(8, 24)|const|float32
call_11530 = relay.TupleGetItem(func_6258_call(relay.reshape(const_11531.astype('float32'), [192,])), 2)
call_11532 = relay.TupleGetItem(func_6261_call(relay.reshape(const_11531.astype('float32'), [192,])), 2)
output = relay.Tuple([call_11525,call_11530,const_11531,])
output2 = relay.Tuple([call_11526,call_11532,const_11531,])
func_11533 = relay.Function([], output)
mod['func_11533'] = func_11533
mod = relay.transform.InferType()(mod)
mutated_mod['func_11533'] = func_11533
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11533_call = mutated_mod.get_global_var('func_11533')
call_11534 = func_11533_call()
output = call_11534
func_11535 = relay.Function([], output)
mutated_mod['func_11535'] = func_11535
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8405_call = mod.get_global_var('func_8405')
func_8407_call = mutated_mod.get_global_var('func_8407')
call_11539 = relay.TupleGetItem(func_8405_call(), 0)
call_11540 = relay.TupleGetItem(func_8407_call(), 0)
func_4603_call = mod.get_global_var('func_4603')
func_4605_call = mutated_mod.get_global_var('func_4605')
const_11547 = relay.const([[-4.439245,4.960879],[7.086557,2.265424],[-2.804952,-1.753717],[-7.523125,-7.283973],[8.846666,5.980224],[-6.798931,-3.416950],[-1.788947,2.887490],[2.124463,-1.436185],[-1.750654,-6.036890],[-8.761810,3.515149],[-5.941573,-4.394695],[3.781740,9.013436],[7.632809,8.208986],[-7.512847,0.883911],[4.216506,9.921848],[2.126462,-1.406596],[-5.808446,-9.376026],[-6.071046,4.291381],[7.738459,4.347704],[-0.670014,9.300033],[-2.528272,-6.134587],[-8.043634,5.806765],[-5.117925,-2.676591],[-3.394492,-6.260001]], dtype = "float32")#candidate|11547|(24, 2)|const|float32
call_11546 = relay.TupleGetItem(func_4603_call(relay.reshape(const_11547.astype('float32'), [48,])), 0)
call_11548 = relay.TupleGetItem(func_4605_call(relay.reshape(const_11547.astype('float32'), [48,])), 0)
output = relay.Tuple([call_11539,call_11546,const_11547,])
output2 = relay.Tuple([call_11540,call_11548,const_11547,])
func_11551 = relay.Function([], output)
mod['func_11551'] = func_11551
mod = relay.transform.InferType()(mod)
output = func_11551()
func_11552 = relay.Function([], output)
mutated_mod['func_11552'] = func_11552
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7959_call = mod.get_global_var('func_7959')
func_7961_call = mutated_mod.get_global_var('func_7961')
call_11587 = relay.TupleGetItem(func_7959_call(), 1)
call_11588 = relay.TupleGetItem(func_7961_call(), 1)
func_5951_call = mod.get_global_var('func_5951')
func_5952_call = mutated_mod.get_global_var('func_5952')
call_11610 = func_5951_call()
call_11611 = func_5951_call()
func_3040_call = mod.get_global_var('func_3040')
func_3042_call = mutated_mod.get_global_var('func_3042')
call_11615 = func_3040_call()
call_11616 = func_3040_call()
func_8276_call = mod.get_global_var('func_8276')
func_8278_call = mutated_mod.get_global_var('func_8278')
call_11622 = relay.TupleGetItem(func_8276_call(), 0)
call_11623 = relay.TupleGetItem(func_8278_call(), 0)
output = relay.Tuple([call_11587,call_11610,call_11615,call_11622,])
output2 = relay.Tuple([call_11588,call_11611,call_11616,call_11623,])
func_11628 = relay.Function([], output)
mod['func_11628'] = func_11628
mod = relay.transform.InferType()(mod)
mutated_mod['func_11628'] = func_11628
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11628_call = mutated_mod.get_global_var('func_11628')
call_11629 = func_11628_call()
output = call_11629
func_11630 = relay.Function([], output)
mutated_mod['func_11630'] = func_11630
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8022_call = mod.get_global_var('func_8022')
func_8024_call = mutated_mod.get_global_var('func_8024')
call_11638 = func_8022_call()
call_11639 = func_8022_call()
output = relay.Tuple([call_11638,])
output2 = relay.Tuple([call_11639,])
func_11660 = relay.Function([], output)
mod['func_11660'] = func_11660
mod = relay.transform.InferType()(mod)
mutated_mod['func_11660'] = func_11660
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11660_call = mutated_mod.get_global_var('func_11660')
call_11661 = func_11660_call()
output = call_11661
func_11662 = relay.Function([], output)
mutated_mod['func_11662'] = func_11662
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9477_call = mod.get_global_var('func_9477')
func_9478_call = mutated_mod.get_global_var('func_9478')
call_11674 = relay.TupleGetItem(func_9477_call(), 0)
call_11675 = relay.TupleGetItem(func_9478_call(), 0)
func_11328_call = mod.get_global_var('func_11328')
func_11330_call = mutated_mod.get_global_var('func_11330')
call_11676 = relay.TupleGetItem(func_11328_call(), 0)
call_11677 = relay.TupleGetItem(func_11330_call(), 0)
var_11683 = relay.var("var_11683", dtype = "float64", shape = (14, 12, 10))#candidate|11683|(14, 12, 10)|var|float64
bop_11684 = relay.less_equal(call_11674.astype('bool'), var_11683.astype('bool')) # shape=(14, 12, 10)
bop_11687 = relay.less_equal(call_11675.astype('bool'), var_11683.astype('bool')) # shape=(14, 12, 10)
output = relay.Tuple([call_11676,bop_11684,])
output2 = relay.Tuple([call_11677,bop_11687,])
func_11705 = relay.Function([var_11683,], output)
mod['func_11705'] = func_11705
mod = relay.transform.InferType()(mod)
mutated_mod['func_11705'] = func_11705
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11706 = relay.var("var_11706", dtype = "float64", shape = (14, 12, 10))#candidate|11706|(14, 12, 10)|var|float64
func_11705_call = mutated_mod.get_global_var('func_11705')
call_11707 = func_11705_call(var_11706)
output = call_11707
func_11708 = relay.Function([var_11706], output)
mutated_mod['func_11708'] = func_11708
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4082_call = mod.get_global_var('func_4082')
func_4083_call = mutated_mod.get_global_var('func_4083')
call_11715 = relay.TupleGetItem(func_4082_call(), 0)
call_11716 = relay.TupleGetItem(func_4083_call(), 0)
const_11731 = relay.const([[[7.005632,-8.477715,-4.022638,3.620456,-3.507356,-6.493609,-1.475614,6.626989,-2.668246,5.312493],[4.622707,0.635188,-3.277695,-0.827180,2.250009,2.872151,-6.412254,0.224938,-5.894138,-0.598552],[2.211905,9.700505,1.912317,-4.173800,-5.390444,3.153850,6.964588,-6.335084,-8.147318,2.090114],[-3.618929,-0.043452,3.708518,-3.437549,-4.829006,-3.928710,4.126739,-6.425791,-9.927929,-0.596290],[-9.615882,-7.408089,-7.606231,9.824881,7.634899,2.012183,9.033189,-2.610112,3.064796,-7.513491]],[[-3.710895,-7.621919,0.667946,-4.286376,5.022961,-1.759012,-4.516732,2.408768,7.049670,5.163263],[-4.695540,6.034806,-7.244387,-8.497639,-6.940038,-9.192192,1.330317,-5.799728,1.621891,-3.322635],[8.149501,-2.236947,-8.406715,-7.972818,-5.683443,-0.832370,-5.969993,3.283061,-8.845417,7.117082],[-2.039448,5.240152,-9.376477,-8.068233,-6.546862,-5.554203,1.399213,2.618116,-5.470941,-1.202726],[2.733811,3.946075,-0.568535,-5.439437,-6.353980,5.904800,7.205069,-4.818581,-0.125545,7.059562]],[[-9.146115,-8.295087,-2.644588,8.652062,8.246898,-2.963320,-4.708635,1.463527,-8.663301,3.334700],[1.756710,4.091222,2.962805,-7.707901,8.118909,-9.956215,1.279317,0.883273,-4.433426,-1.138165],[-7.405404,-7.521550,3.575149,0.549759,-8.110045,-8.239802,4.780679,-6.281630,-5.463338,-9.470033],[5.969167,2.577324,8.322297,-0.960306,3.136064,-8.181420,5.954286,-6.845789,-1.068995,-6.563969],[1.217473,-1.983352,1.930439,9.535903,2.552915,0.115815,7.793622,3.938608,0.117680,-5.153085]],[[-4.910221,4.385340,-8.970229,-0.936922,8.105168,9.165255,-0.659532,-0.940501,-4.224366,2.229405],[5.223299,-3.237527,1.311985,-1.387135,-8.857827,3.416037,1.969857,-2.845693,-1.371924,-4.068115],[-5.989878,-1.945364,5.276345,-5.282165,5.765563,8.809018,-4.818320,8.219570,8.403783,-1.192495],[-7.485036,-9.757168,-7.630944,1.438165,-0.588128,8.210132,5.983366,3.686609,-9.839750,2.801039],[6.006648,-6.638249,-6.072763,6.435652,0.548575,6.231753,0.509650,8.536748,9.665662,-4.826190]],[[-5.115147,-9.881069,-1.441527,-0.253802,6.997414,-2.297715,-5.444325,-9.336184,-5.900361,-7.027106],[9.122091,2.124312,-1.542076,2.930483,-8.005272,9.503806,3.835199,-8.369614,6.157560,-7.378415],[-1.262629,4.507943,0.692955,-1.858517,9.584480,-2.097547,-3.275432,5.739256,-4.511956,-4.747735],[-5.381657,-0.230458,1.024587,9.932403,4.525081,4.425501,-9.374677,7.509685,-5.336369,3.839444],[-9.330164,3.696792,-8.745006,1.532336,9.644778,5.814100,1.757881,9.137769,-3.043079,4.138779]],[[-9.621255,-0.484323,6.119930,-4.877786,6.226518,4.180768,7.870309,-7.406981,1.373518,2.244015],[-2.016509,4.322826,-1.916766,-3.529027,5.004025,-0.451604,0.713728,7.570144,-2.389139,-0.890725],[8.048132,-4.581632,-2.878834,-5.536496,-2.942462,-0.930704,-7.465116,1.016262,-0.925506,-8.384043],[9.520067,1.222333,5.926477,-7.004268,3.973853,0.927537,-1.178176,2.717649,-6.844949,3.336236],[5.462376,5.758317,7.301595,-7.533110,4.547730,9.847155,-6.111499,0.074973,9.646990,8.477586]],[[-6.115507,-7.985831,-8.136176,-2.811642,0.745337,-4.732846,2.657971,8.837746,-0.564362,0.862867],[-9.790202,-2.681532,9.794858,-1.384855,7.549793,9.039281,-3.838431,3.882137,-9.175946,6.102218],[5.685352,-3.181610,-8.813433,4.316031,-8.700385,-9.528928,8.499263,7.849510,-5.842867,-3.701365],[5.485445,6.097289,7.352940,0.499134,-2.103896,6.762675,-1.786745,2.348912,9.287014,8.618934],[5.910340,-6.557974,-0.098212,9.740674,9.141647,8.690849,-2.658986,-2.189789,6.592825,4.909631]],[[1.870410,9.976842,-8.122203,-4.447171,5.356178,4.913221,1.545731,7.435633,9.992668,-8.394222],[-4.913599,-5.729130,-2.423672,-1.573399,-9.740194,-3.420528,8.331622,0.405493,-1.434448,5.579379],[6.863914,-0.410123,7.088035,-4.770998,-3.471973,8.127508,-5.433162,2.416231,2.245135,-9.906400],[2.187949,0.578229,-1.663910,8.171391,-0.272708,-6.777388,4.646470,-1.936593,4.449816,-1.050850],[2.718734,-5.173387,4.579202,-1.791803,-3.025007,-9.483892,8.628565,-9.442339,-6.419946,-8.222028]],[[-7.259157,-6.804453,1.099565,-2.468958,4.595777,7.551936,9.885722,3.905962,4.681110,9.722152],[-8.916621,-9.022876,9.511934,-5.534947,-5.140568,-2.829613,5.994141,-1.223711,8.528987,3.895127],[8.959389,6.358652,2.501174,7.262382,-9.111623,-1.500945,-9.512631,6.036350,7.166478,1.305111],[-6.552689,-8.666742,-0.071772,8.875541,-0.277971,1.822900,4.625715,-0.121068,3.109432,6.809010],[-0.017271,-4.722750,-5.456422,-8.024807,1.226797,8.333833,1.425156,-1.623385,1.183677,0.119396]],[[-5.820636,8.604512,2.442069,-2.135669,-0.476329,-5.380774,7.505870,0.316958,-8.280194,1.105303],[-3.558193,-6.379310,2.902164,0.155519,-3.482010,-1.580012,0.241750,-1.860259,4.173896,9.384360],[-4.677844,-8.125420,4.627339,-3.565619,4.654610,4.248261,-0.244529,1.538474,-1.297778,-4.046051],[3.411943,-8.787144,5.456064,9.788337,9.938498,-7.571013,-8.114214,-5.277426,-0.024069,-9.911361],[-6.008372,3.002349,0.558348,-9.061104,-7.746639,-0.852652,2.838586,-5.046623,6.283158,8.861958]],[[2.901273,-1.717974,-1.191866,0.681261,6.385023,-0.397290,7.804556,1.150856,-9.521370,5.076476],[-3.979040,-0.407637,-8.958750,-8.260877,-7.191840,-1.774372,1.423902,-2.297299,2.185452,2.556509],[2.665461,1.099154,6.732238,6.520422,-0.747108,-9.327403,-9.579100,3.784593,-2.831059,-5.385477],[5.738938,-5.871385,6.984727,3.116176,-3.972874,-8.617135,-7.905754,-6.942784,-0.043685,-3.191446],[-7.121458,0.889643,9.174397,8.982253,9.594448,0.406850,5.400521,2.645773,-1.149832,4.553203]],[[8.837525,-3.186926,2.662556,-6.752300,-3.955980,5.041991,9.676790,6.551140,5.908426,-7.160652],[-0.411801,5.549349,1.181649,-9.112181,9.821700,-5.440305,2.674790,3.677853,-4.405945,-9.237667],[-7.845761,9.428786,0.068130,-1.792498,-3.266627,7.722338,-0.355944,-1.257381,7.289693,5.292246],[-3.104200,-3.185232,-5.128791,8.056545,7.740282,7.421429,6.505980,3.431361,1.105347,0.746792],[6.178534,-2.573716,4.477364,7.107171,-3.332197,-7.587337,5.192123,-1.127261,-7.242797,-3.794576]],[[-7.866349,7.471083,-0.808619,-8.246937,-1.058457,1.350218,-4.772044,-2.065904,-6.954296,-0.567450],[-6.780955,-7.392386,9.258864,-5.824483,-6.637941,5.572008,-2.601796,-0.522132,-2.785471,9.603487],[-2.613291,-5.558696,-9.766196,-3.898519,-8.129382,7.659335,1.834623,-6.670814,6.137374,-1.028379],[9.862790,-3.887711,-6.232118,5.437408,5.155612,-0.227604,0.311162,-1.623310,1.112074,4.252701],[9.002609,-1.698192,-9.601634,-5.873953,3.077714,9.720118,-1.279534,0.027736,-8.424507,3.158268]],[[4.353527,7.918450,-8.942804,-0.119258,-1.347795,-9.849351,0.899749,6.894037,4.766345,2.536828],[-0.197561,-8.065719,-5.637446,-1.958535,-8.778300,-7.363572,9.244060,-9.094355,8.422870,8.217529],[-7.353944,6.511478,-4.635711,1.015188,-0.954807,6.657526,0.584655,-7.363213,8.081257,-1.302055],[-4.550259,3.609313,-1.125678,-9.897499,-6.704100,-5.165649,1.258284,-2.643737,-9.507562,3.683099],[-2.565859,8.015603,-1.707192,8.257355,-0.239054,3.143630,-4.412548,-1.911458,1.853432,-8.904234]]], dtype = "float32")#candidate|11731|(14, 5, 10)|const|float32
bop_11732 = relay.right_shift(call_11715.astype('int16'), const_11731.astype('int16')) # shape=(14, 5, 10)
bop_11735 = relay.right_shift(call_11716.astype('int16'), const_11731.astype('int16')) # shape=(14, 5, 10)
func_9932_call = mod.get_global_var('func_9932')
func_9933_call = mutated_mod.get_global_var('func_9933')
call_11749 = func_9932_call()
call_11750 = func_9932_call()
output = relay.Tuple([bop_11732,call_11749,])
output2 = relay.Tuple([bop_11735,call_11750,])
func_11751 = relay.Function([], output)
mod['func_11751'] = func_11751
mod = relay.transform.InferType()(mod)
mutated_mod['func_11751'] = func_11751
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11751_call = mutated_mod.get_global_var('func_11751')
call_11752 = func_11751_call()
output = call_11752
func_11753 = relay.Function([], output)
mutated_mod['func_11753'] = func_11753
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5441_call = mod.get_global_var('func_5441')
func_5443_call = mutated_mod.get_global_var('func_5443')
call_11770 = func_5441_call()
call_11771 = func_5441_call()
func_4765_call = mod.get_global_var('func_4765')
func_4768_call = mutated_mod.get_global_var('func_4768')
const_11776 = relay.const([-1,-6,7,9,7,-2,5,5,-6,-10,-3,2,2,3,5,3,6,-8,-7,-2,10,-9,9,10,-10,8,7,-3,4,-4,-3,-4,6,3,8,2,-1,-4,6,8,6,-1,-8,5,-2,10,4,6,7,-7,-5,2,9,-8,1,3,4,2,8,-3,-4,8,6,-2,-3,7,-8,-8,4,-4,-4,2,-10,-1,10,3,-6,4,4,4,-2,9,-9,-9,-3,-7,9,-6,-4,1,10,9,-2,-7,-8,-6,-1,2,-10,-2,-3,1,-10,3,3,-9,-6,6,-1,4,3,10,5,-5,-1,9,7,6,-8,-9,-10,3,-7,4,3,7,-10,-1,9,3,2,-5,-3,-6,1,1,4,-7,-4,-10,3,-2,-6,-9,8,8,3,8,-6,8,-10,1,4,8,1,6,7,6,-10,10,-8,-7,-2,8,1,-7,6,8,6,-9,-4,-10,2,4,-4,9,3,-2,2,4,7,-8,-1,-6,-2,5,-1,-7,-2,4,-7,7,-8,6,-10,-7,4,-3,-10,4,-3,10,-4,6,9,-2,-2,6,-8,2,-3,-9,4,3,-9,6,6,6,2,-5,-2,9,8,6,8,-7,6,-1,6,-4,3,-8,7,-8,-8,2,-4,5,-6,9,6,-6,-10,5,-3,2,9,4,6,7,-6,5,9,1,9,-9,6,1,4,-3,-3,10,6,9,5,7,4,1,-2,-9,2,9,-3,5,4,-4,-4,-10,8,4,7,5,7,-5,10,-1,-1,-2,1,-4,7,2,2,-4,5,-6,-1,-4,-8,-7,-2,-3,-9,9,-4,4,3,-3,-10,-7,-4,7,-5,4,-1,-4,-1,10,-3,9,4,-9,1,-1,-10,8,-3,-1,-10,-4,8,-6,6,-1,4,4,-5,-4,8,1,-6,-2,-6,9,-10,8,2,6,-9,7,-9,3,8,2,3,-2,2,9,-8,5,3,5,7,-5,10,-2,-5,-3,-10,-8,6,-3,-3,8,1,9,-5,1,-6,8,8,-5,3,-7], dtype = "int8")#candidate|11776|(384,)|const|int8
call_11775 = relay.TupleGetItem(func_4765_call(relay.reshape(const_11776.astype('int8'), [2, 16, 12])), 1)
call_11777 = relay.TupleGetItem(func_4768_call(relay.reshape(const_11776.astype('int8'), [2, 16, 12])), 1)
output = relay.Tuple([call_11770,call_11775,const_11776,])
output2 = relay.Tuple([call_11771,call_11777,const_11776,])
func_11795 = relay.Function([], output)
mod['func_11795'] = func_11795
mod = relay.transform.InferType()(mod)
output = func_11795()
func_11796 = relay.Function([], output)
mutated_mod['func_11796'] = func_11796
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11795_call = mod.get_global_var('func_11795')
func_11796_call = mutated_mod.get_global_var('func_11796')
call_11840 = relay.TupleGetItem(func_11795_call(), 1)
call_11841 = relay.TupleGetItem(func_11796_call(), 1)
func_5749_call = mod.get_global_var('func_5749')
func_5753_call = mutated_mod.get_global_var('func_5753')
const_11843 = relay.const(-7, dtype = "int8")#candidate|11843|()|const|int8
var_11844 = relay.var("var_11844", dtype = "float64", shape = (468,))#candidate|11844|(468,)|var|float64
call_11842 = relay.TupleGetItem(func_5749_call(relay.reshape(const_11843.astype('int8'), []), relay.reshape(var_11844.astype('float64'), [468,]), ), 1)
call_11845 = relay.TupleGetItem(func_5753_call(relay.reshape(const_11843.astype('int8'), []), relay.reshape(var_11844.astype('float64'), [468,]), ), 1)
output = relay.Tuple([call_11840,call_11842,const_11843,var_11844,])
output2 = relay.Tuple([call_11841,call_11845,const_11843,var_11844,])
func_11858 = relay.Function([var_11844,], output)
mod['func_11858'] = func_11858
mod = relay.transform.InferType()(mod)
var_11859 = relay.var("var_11859", dtype = "float64", shape = (468,))#candidate|11859|(468,)|var|float64
output = func_11858(var_11859)
func_11860 = relay.Function([var_11859], output)
mutated_mod['func_11860'] = func_11860
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1178_call = mod.get_global_var('func_1178')
func_1180_call = mutated_mod.get_global_var('func_1180')
call_11862 = func_1178_call()
call_11863 = func_1178_call()
output = call_11862
output2 = call_11863
func_11895 = relay.Function([], output)
mod['func_11895'] = func_11895
mod = relay.transform.InferType()(mod)
output = func_11895()
func_11896 = relay.Function([], output)
mutated_mod['func_11896'] = func_11896
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9036_call = mod.get_global_var('func_9036')
func_9037_call = mutated_mod.get_global_var('func_9037')
call_11957 = relay.TupleGetItem(func_9036_call(), 0)
call_11958 = relay.TupleGetItem(func_9037_call(), 0)
output = call_11957
output2 = call_11958
func_11963 = relay.Function([], output)
mod['func_11963'] = func_11963
mod = relay.transform.InferType()(mod)
output = func_11963()
func_11964 = relay.Function([], output)
mutated_mod['func_11964'] = func_11964
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7990_call = mod.get_global_var('func_7990')
func_7992_call = mutated_mod.get_global_var('func_7992')
call_12001 = func_7990_call()
call_12002 = func_7990_call()
output = relay.Tuple([call_12001,])
output2 = relay.Tuple([call_12002,])
func_12028 = relay.Function([], output)
mod['func_12028'] = func_12028
mod = relay.transform.InferType()(mod)
output = func_12028()
func_12029 = relay.Function([], output)
mutated_mod['func_12029'] = func_12029
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6494_call = mod.get_global_var('func_6494')
func_6495_call = mutated_mod.get_global_var('func_6495')
call_12039 = relay.TupleGetItem(func_6494_call(), 0)
call_12040 = relay.TupleGetItem(func_6495_call(), 0)
func_9932_call = mod.get_global_var('func_9932')
func_9933_call = mutated_mod.get_global_var('func_9933')
call_12056 = func_9932_call()
call_12057 = func_9932_call()
func_4735_call = mod.get_global_var('func_4735')
func_4736_call = mutated_mod.get_global_var('func_4736')
call_12060 = relay.TupleGetItem(func_4735_call(), 0)
call_12061 = relay.TupleGetItem(func_4736_call(), 0)
func_11132_call = mod.get_global_var('func_11132')
func_11133_call = mutated_mod.get_global_var('func_11133')
call_12064 = func_11132_call()
call_12065 = func_11132_call()
output = relay.Tuple([call_12039,call_12056,call_12060,call_12064,])
output2 = relay.Tuple([call_12040,call_12057,call_12061,call_12065,])
func_12090 = relay.Function([], output)
mod['func_12090'] = func_12090
mod = relay.transform.InferType()(mod)
output = func_12090()
func_12091 = relay.Function([], output)
mutated_mod['func_12091'] = func_12091
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8127_call = mod.get_global_var('func_8127')
func_8128_call = mutated_mod.get_global_var('func_8128')
call_12095 = relay.TupleGetItem(func_8127_call(), 5)
call_12096 = relay.TupleGetItem(func_8128_call(), 5)
output = call_12095
output2 = call_12096
func_12097 = relay.Function([], output)
mod['func_12097'] = func_12097
mod = relay.transform.InferType()(mod)
output = func_12097()
func_12098 = relay.Function([], output)
mutated_mod['func_12098'] = func_12098
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7289_call = mod.get_global_var('func_7289')
func_7290_call = mutated_mod.get_global_var('func_7290')
call_12169 = relay.TupleGetItem(func_7289_call(), 0)
call_12170 = relay.TupleGetItem(func_7290_call(), 0)
func_11895_call = mod.get_global_var('func_11895')
func_11896_call = mutated_mod.get_global_var('func_11896')
call_12174 = func_11895_call()
call_12175 = func_11895_call()
output = relay.Tuple([call_12169,call_12174,])
output2 = relay.Tuple([call_12170,call_12175,])
func_12183 = relay.Function([], output)
mod['func_12183'] = func_12183
mod = relay.transform.InferType()(mod)
mutated_mod['func_12183'] = func_12183
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12183_call = mutated_mod.get_global_var('func_12183')
call_12184 = func_12183_call()
output = call_12184
func_12185 = relay.Function([], output)
mutated_mod['func_12185'] = func_12185
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10292_call = mod.get_global_var('func_10292')
func_10294_call = mutated_mod.get_global_var('func_10294')
call_12211 = func_10292_call()
call_12212 = func_10292_call()
output = call_12211
output2 = call_12212
func_12229 = relay.Function([], output)
mod['func_12229'] = func_12229
mod = relay.transform.InferType()(mod)
mutated_mod['func_12229'] = func_12229
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12229_call = mutated_mod.get_global_var('func_12229')
call_12230 = func_12229_call()
output = call_12230
func_12231 = relay.Function([], output)
mutated_mod['func_12231'] = func_12231
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6200_call = mod.get_global_var('func_6200')
func_6201_call = mutated_mod.get_global_var('func_6201')
call_12238 = relay.TupleGetItem(func_6200_call(), 0)
call_12239 = relay.TupleGetItem(func_6201_call(), 0)
func_5749_call = mod.get_global_var('func_5749')
func_5753_call = mutated_mod.get_global_var('func_5753')
const_12246 = relay.const([-0.259694,5.693639,8.673704,-4.757560,-6.993091,-7.849630,6.563602,6.599324,-7.752831,-5.894748,-8.577254,-1.062161,-7.061143,3.797068,0.134740,6.457825,8.575489,-8.284396,0.350121,-7.302031,-6.766970,-3.601486,-9.554619,2.920329,-9.846082,-9.948235,8.496230,8.640260,-8.280073,-6.564645,-1.275613,-4.285487,-2.331033,-4.414923,8.365554,3.305182,6.376329,5.392899,5.519298,2.241322,-8.153080,9.631395,-4.696799,-6.392188,2.476923,-0.309820,-1.074760,3.584826,8.265186,2.921402,4.720217,6.140732,-5.118039,-9.988030,1.034324,-3.385381,2.784250,8.671379,-1.656129,-1.136057,-8.522620,1.218451,0.981093,-8.342848,-6.770201,5.319072,-5.761607,1.904992,-4.629970,2.055893,1.468719,5.768625,4.627159,-4.042914,-9.324908,7.823540,7.077475,-9.069382,1.212582,7.943493,-4.564215,2.431704,3.045354,5.113500,-5.720549,3.122378,-5.510236,-1.718213,-1.848108,9.264734,-3.142179,7.687972,4.565866,-7.250041,-9.245520,9.971627,0.419750,-6.203537,7.931167,-5.822222,-5.394129,6.802765,-2.187006,-7.805730,-3.282489,-7.578547,-6.654385,-9.849159,4.848646,-3.680411,-2.222462,-8.675912,5.879633,2.387037,-8.716256,-8.666858,1.523164,-6.933211,-8.398575,-3.599758,-8.456539,3.263687,6.523144,9.906420,-1.907735,-9.628110,3.835136,-8.539847,1.614496,2.245076,0.634520,-0.864975,1.855556,4.680226,0.976808,-8.214488,-4.275753,-4.301907,1.907394,-0.132870,-5.306070,-3.927683,7.203836,-1.002836,-7.231107,-1.881408,6.704366,1.683471,6.256129,-2.762327,-4.078099,7.282537,-0.196621,-2.245162,7.434227,-0.488499,-0.945880,6.490487,6.050749,-4.891418,4.576019,-3.033098,-6.068915,2.555751,-8.990729,-2.863545,-8.334060,7.620700,-0.120420,-3.800039,-9.336041,1.380406,0.903513,-8.991256,-3.753706,6.259450,2.877181,-6.501682,8.172554,-9.057926,-4.430827,-0.856672,-6.522148,7.818294,-8.758068,-7.438970,-6.396345,1.155729,-2.103244,0.509747,-7.088210,-0.775657,-9.395272,3.738246,-8.244642,3.611333,9.079153,5.449561,8.464377,-3.885962,-2.774936,-7.304184,-2.794380,-7.827091,8.740577,6.923219,-4.074768,2.610933,-1.487478,-2.099740,-8.079814,1.347779,-6.981029,4.315243,-5.260642,0.247916,-2.386977,9.321572,4.967102,4.608167,7.336085,-8.292981,-6.617227,-1.012514,9.874625,4.169125,-6.007254,9.414737,3.259625,-8.942682,-1.984868,-3.707844,5.466822,2.074802,-4.704036,1.153427,1.707000,2.346264,-9.047142,-0.257974,8.996870,3.603541,1.687995,-2.960584,-3.841370,-7.451879,-7.554296,6.412264,-3.394660,-5.046751,-2.815668,9.193278,9.022361,6.809998,-6.367714,0.212516,-5.168741,-0.415326,7.817074,-0.854597,3.537628,-7.924912,-8.229722,-9.191483,-7.693116,0.640039,-4.683964,-2.701562,3.448680,3.480803,-3.001932,4.193274,-7.702774,-9.238453,-4.417413,1.002043,6.190258,9.563752,3.008805,-0.417488,-9.965707,-2.070198,-1.365449,3.999900,8.360754,-8.141280,1.908818,-5.810465,1.509398,-7.112582,7.986795,2.435090,7.760793,-6.798793,-0.999580,6.442187,-6.829832,-6.461491,-5.033550,0.125278,-4.427495,6.713365,8.564651,3.567840,-4.400181,9.839288,8.703538,-5.016579,9.081980,-4.598842,-5.954593,3.280176,7.048962,7.967703,5.254042,0.386178,-8.700532,1.980050,-9.017387,-3.978167,-8.103511,7.631074,5.672144,4.233799,-4.510769,-3.270717,2.365208,-4.444856,5.201110,-3.735270,-6.328971,9.054339,5.867301,-8.159072,0.316257,-0.392490,-6.786968,-7.235125,-9.849153,1.421652,3.159612,9.478100,7.587982,1.804871,1.436489,7.438493,-0.245558,0.266464,4.507401,0.883422,-2.619500,5.650443,9.859855,-7.204308,2.917449,9.301098,-3.708930,3.229577,-0.704755,-8.599814,-4.383599,1.531851,-8.564622,-5.771053,-1.894916,6.244207,-1.820177,-4.887125,-8.128384,3.533663,-3.612109,-4.077307,3.075337,-9.315423,-1.771030,2.039238,-2.597843,6.737084,2.736724,-6.904406,-5.808572,8.091444,-7.595713,-7.156468,-1.452140,-9.670769,-2.648595,6.818701,-1.403012,1.802800,3.417925,-8.253978,7.558186,-1.409510,7.043762,6.276546,-4.149908,-6.360025,-1.207673,7.494884,-2.500151,6.529553,-7.187473,-7.769760,-3.555845,-0.146050,2.157188,5.784852,-2.724423,6.221061,-6.144340,4.714095,3.971489,-2.179557,5.098793,3.353781,8.636262,-4.852007,7.727420,9.108553,8.053137,3.961203,-0.180465,6.975975,9.682232,-7.218312,9.080085,-5.014552,-4.978917,-3.096734,4.262300,0.792429,-1.909490,-9.399821,9.611086,6.536268,1.717686,7.716835,8.892277,3.864453,8.214335,2.037102,3.529637,-0.437186,-4.090187,1.035171,-6.773970,-3.649361,3.506895,-7.052633,-4.120094,1.370710,7.075924,8.447866,8.902369,9.209999,8.580203,-5.317594,-4.611687,-9.024485,4.933503,-7.780506,-9.646480,6.764596,-0.524771,-0.045774,8.895089,-6.823242], dtype = "float64")#candidate|12246|(468,)|const|float64
call_12245 = relay.TupleGetItem(func_5749_call(relay.reshape(call_12238.astype('int8'), []), relay.reshape(const_12246.astype('float64'), [468,]), ), 2)
call_12247 = relay.TupleGetItem(func_5753_call(relay.reshape(call_12238.astype('int8'), []), relay.reshape(const_12246.astype('float64'), [468,]), ), 2)
output = relay.Tuple([call_12238,call_12245,const_12246,])
output2 = relay.Tuple([call_12239,call_12247,const_12246,])
func_12249 = relay.Function([], output)
mod['func_12249'] = func_12249
mod = relay.transform.InferType()(mod)
mutated_mod['func_12249'] = func_12249
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12249_call = mutated_mod.get_global_var('func_12249')
call_12250 = func_12249_call()
output = call_12250
func_12251 = relay.Function([], output)
mutated_mod['func_12251'] = func_12251
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5392_call = mod.get_global_var('func_5392')
func_5394_call = mutated_mod.get_global_var('func_5394')
call_12325 = relay.TupleGetItem(func_5392_call(), 0)
call_12326 = relay.TupleGetItem(func_5394_call(), 0)
output = call_12325
output2 = call_12326
func_12330 = relay.Function([], output)
mod['func_12330'] = func_12330
mod = relay.transform.InferType()(mod)
mutated_mod['func_12330'] = func_12330
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12330_call = mutated_mod.get_global_var('func_12330')
call_12331 = func_12330_call()
output = call_12331
func_12332 = relay.Function([], output)
mutated_mod['func_12332'] = func_12332
mutated_mod = relay.transform.InferType()(mutated_mod)
const_12333 = relay.const([[[0.739500,1.851108,3.393500,3.785314,9.991371,-6.547604,-9.831838,-3.793691,5.220698,-1.338075,-4.021319],[-4.734557,5.990143,-5.345791,4.361963,6.140457,-1.973886,-5.478429,3.530274,-3.323910,5.017908,6.818784],[-2.885967,8.389287,-9.195280,-5.675320,-2.864279,2.962991,2.764293,3.966990,5.328272,7.089841,0.433919],[-5.195661,5.854803,-6.834988,9.012065,0.273484,8.387072,2.171589,-0.812699,-4.072970,9.839900,5.457652],[8.185921,6.900359,6.377424,-6.309704,-0.093755,-1.366177,9.357438,9.533729,-8.761254,0.307333,0.193156],[-8.267338,-2.805751,4.929858,-6.415181,-8.200896,8.434586,-0.372415,-6.948106,3.695830,9.269431,5.493251],[-5.623688,-1.620094,1.530609,-2.304402,-7.385654,-9.453455,-8.220761,-4.221702,-6.733388,-4.895441,1.854889],[9.586931,-5.277012,-1.018227,-0.204225,-5.292109,-2.275821,5.110610,-0.375517,9.264991,-0.124013,8.801696],[3.424133,1.187131,-8.162291,7.836740,6.191035,-7.342599,2.889825,7.097414,-5.471161,4.170138,-7.905992],[-8.384835,-0.484686,-7.127697,9.901688,3.325962,3.957497,0.773077,4.100521,2.759963,2.615557,-2.322761],[1.488209,-2.373708,0.200322,-2.937560,-2.657359,4.285144,-9.620030,-4.070949,3.405780,-0.292745,-6.302233],[1.988698,-8.396903,-4.613053,-8.606838,8.587531,4.043924,0.418489,6.299005,-3.235897,-3.474731,-5.665648],[6.761412,-8.659307,2.778251,-2.149202,-3.049794,6.798355,-8.761073,-7.192672,-3.921736,-8.400118,4.655335],[-1.460353,-6.857013,0.279063,-7.436614,6.502982,-7.803998,1.780037,0.335985,7.154716,4.795960,-3.247425],[4.330237,-1.214913,-5.806252,6.586906,-0.340266,-6.489973,-7.340604,9.241272,-9.501318,1.840950,-4.989896],[-3.796292,-5.272034,-9.604460,-5.513000,9.741772,5.219618,0.525784,1.068149,-4.369277,-5.222438,-5.604460]],[[-0.202612,-3.057517,-0.046254,9.462465,-7.753067,-6.201365,3.359551,-5.425544,-9.391548,9.223810,1.149096],[6.400800,1.364329,-0.824774,4.697128,2.121787,-8.693606,-7.597156,3.960108,1.704758,4.476512,-5.147346],[-7.592561,-1.430161,-8.971445,2.955473,-3.370798,-8.597281,-9.054814,8.431143,6.201566,5.692957,-7.641792],[6.770850,8.275834,0.338919,-8.086028,5.218371,-4.066494,2.565981,-8.988585,-8.504680,-8.184959,-8.744840],[2.603837,-2.884431,-2.366503,-2.803151,8.872738,-0.816889,0.877770,3.135606,2.213004,-3.071814,-1.535331],[3.189999,-0.990864,3.625641,-7.795800,3.898452,6.435293,7.651164,0.545200,6.778517,7.408051,8.853001],[5.726094,-9.423964,-4.771667,8.616082,6.555458,5.819403,-3.226471,-5.333534,-3.331496,1.609968,5.819843],[-5.037130,-7.927381,7.980009,9.912049,-1.950580,6.542923,-2.018407,-7.647668,-6.211647,-0.345302,7.925182],[-2.373737,6.358927,-5.580645,-5.793399,0.453986,-0.092188,-5.082520,3.387840,7.701966,0.501031,1.334048],[-7.309221,3.522795,2.028145,-0.682686,-8.058525,-1.037339,3.010206,-1.237647,-8.838749,-9.474798,-5.953792],[-5.206648,7.764979,9.409470,-9.592473,-5.456131,-3.118081,1.303354,1.528486,3.757573,-7.181845,4.565908],[-7.117050,0.594123,-8.314157,5.974017,1.831888,-9.612128,7.914368,3.096080,-8.065816,-2.909890,8.278147],[-7.013259,0.079551,-2.811136,6.666094,-1.166393,-4.541958,-0.176752,3.238972,0.658634,7.428078,2.115603],[0.212180,-3.679205,-7.641044,9.860456,-8.278239,-9.761545,5.203310,2.564141,1.571946,-0.560612,-1.218815],[-4.833081,-9.813905,-4.121456,9.870891,4.453359,-9.601414,3.831211,-7.417186,-5.937949,-8.044114,5.094723],[4.647814,8.799717,-0.732911,-0.941083,-4.299007,-5.459598,-0.644240,3.480257,5.844109,2.385066,-8.057077]],[[-1.039931,7.039337,-8.828980,-3.184935,4.873481,-5.860215,-2.863273,-8.354102,9.429751,6.382661,2.246847],[-7.293634,4.687138,4.017512,2.863557,4.968671,8.597958,-3.726278,0.135919,4.924107,0.650503,5.418468],[-4.761578,-9.835074,-4.555980,4.217590,-5.488726,-3.210883,2.800150,-2.338673,-3.317741,5.763590,-1.698504],[9.014509,-5.542764,-8.922487,-8.160354,9.334608,3.183671,9.957547,9.529410,9.865852,-7.974229,1.861728],[-0.535882,3.243840,-9.688634,-6.542145,-7.989047,-1.815922,-5.810725,-0.243047,-1.725196,9.188954,-3.059126],[0.145363,6.381004,5.148468,3.384311,-8.305317,-6.524028,-4.647297,-0.695447,6.544151,-0.410535,7.691226],[-9.140915,4.911098,8.095659,-7.137574,4.568230,1.583448,-4.532074,0.017424,6.264639,9.962592,1.000889],[-8.304470,-4.971701,-2.403354,1.899441,1.994671,-9.377764,-4.397421,9.502521,1.215122,8.093324,-2.433386],[2.013900,2.118890,7.085284,-2.842285,-0.598653,-6.699612,-8.227442,3.369084,-6.960913,6.717748,6.233659],[-0.527869,-2.814283,-4.596573,-7.883653,5.301498,-7.360834,-0.711013,-0.237573,-4.725841,-4.903441,3.158272],[5.491609,-9.930264,-3.597980,-1.080411,-2.881205,-6.339587,-7.560329,-7.973016,3.763501,-3.068115,-6.343849],[5.703966,3.177112,7.704662,-1.770724,-7.460436,8.809594,6.192291,-0.528533,2.710119,-3.619208,1.178012],[-9.692874,8.615258,-5.248978,0.060187,4.812424,4.069887,-5.269590,-3.413287,6.988845,0.461859,8.279150],[-2.705286,-5.016812,-7.886674,-8.342417,-8.438587,6.118870,-7.678903,5.845952,-2.260387,8.034273,-1.949171],[-8.942917,-1.116273,2.677369,-8.690746,7.085217,6.911531,1.106529,-6.237277,4.269354,-2.382164,2.787266],[-0.938781,9.459447,6.623571,-1.330979,-7.576384,-6.405732,5.537166,-0.035277,-4.158403,-8.248139,-8.322113]],[[-7.201791,1.900541,1.631284,-1.226152,8.698482,6.062013,-5.152763,6.431601,-7.489236,8.742417,-1.954787],[2.904522,2.245585,-7.583616,8.893320,3.195766,-2.188627,7.416407,-2.016962,-2.736171,8.142745,-9.058686],[-2.235352,-6.872861,-1.069618,1.985973,-4.616687,4.832210,-3.984667,-3.058405,-5.611830,2.613663,-6.280033],[-3.665794,1.650270,-9.584289,5.092773,-3.604159,-3.884732,-0.319527,-6.201808,-8.269125,-3.745929,-1.358495],[5.807004,-5.077288,-7.591742,-4.586336,9.420407,-6.362416,5.725047,7.207653,6.220465,-4.090707,-2.350789],[-9.882983,-3.966569,-7.468364,3.630507,-4.404586,5.499740,-4.464463,-0.307678,-6.537992,-4.981463,-8.023190],[-8.726022,-5.997799,7.715110,9.347308,9.520988,7.997153,-2.161341,3.906125,-0.789449,1.787756,-8.942303],[-7.553022,-1.376734,-7.255411,8.244287,0.350989,-3.525575,7.149507,-0.977041,-7.682052,0.434562,-5.291876],[1.307715,0.657859,5.605039,5.041227,-2.226279,-1.160312,-5.566708,8.041589,-4.948121,7.852293,-4.853446],[-0.544472,-7.278555,3.997489,-3.996250,1.220290,6.716905,-4.277487,1.050206,-1.328279,3.669628,9.396127],[-4.796528,0.530460,3.209691,5.982782,6.302715,-8.759501,-5.159865,2.087866,5.877693,-2.011950,6.876804],[3.319125,-6.425205,4.488140,5.953440,-0.874538,0.652425,-0.138767,-1.979008,8.738283,8.798293,0.753526],[3.792055,7.268408,-2.120023,0.808342,-5.460603,-0.675273,-4.960293,-0.875891,-5.501738,5.091863,-6.967802],[-5.997000,-7.265334,-5.764190,-5.579100,6.152778,3.916980,-5.333760,7.447591,2.221653,4.929948,-4.756311],[2.232166,8.541380,5.971743,-2.356447,-2.974922,0.639634,-1.629831,-4.796569,1.070465,-4.736510,-5.646463],[-7.889911,-0.018851,4.147424,-6.792446,3.167761,-1.850940,1.823749,-9.320652,0.273332,7.802911,7.275072]],[[7.837129,-9.261133,1.746348,3.905079,4.216528,3.570587,5.540076,0.856402,3.909759,-3.676222,2.787534],[7.266144,2.296249,-6.471885,8.381134,-3.404732,-3.973167,-5.279132,4.013964,5.070334,0.563004,-7.565751],[-3.173197,-5.748480,-2.449448,5.846104,8.164361,7.197008,-8.039890,2.740586,2.883415,-4.257183,-5.327382],[-2.681894,-0.623259,-7.596328,-7.053024,-1.441681,0.838582,-5.739180,8.486961,3.084425,2.600485,1.100690],[6.460755,9.093033,-0.386127,-1.709388,-5.152099,-3.544495,-3.231324,9.859019,9.892586,0.116006,-2.693490],[8.515218,-9.541853,-7.319037,5.748260,0.427606,-6.106437,-0.059333,-9.627208,0.650612,8.278185,0.409414],[2.981191,-3.928697,-0.592001,8.157787,-5.871303,3.605411,7.792267,-5.925098,8.261211,5.733821,-1.985299],[3.401995,-5.802848,-0.418076,-6.368132,-2.317590,-8.633600,3.256156,-6.149441,1.420877,7.633850,2.518628],[6.170912,3.324557,5.618046,-9.185652,-6.473419,-3.371351,2.928130,-5.840326,-3.948803,7.666948,-6.380861],[-7.278719,5.840564,3.917007,-5.406391,4.796416,-4.006622,-3.245898,-0.191923,4.897052,-8.718916,0.910221],[-8.228461,-9.984613,-6.802127,7.920830,-6.928351,-8.083255,-8.074378,-8.115617,-5.776206,-6.138473,-6.856772],[3.570748,8.350907,-3.049538,-3.931509,9.937008,6.643869,-9.500497,0.408643,-6.110663,9.004420,1.843441],[-9.819272,-0.095315,-3.551311,7.681001,5.141499,5.604240,-8.458615,7.000203,1.644476,7.059589,-9.584877],[2.117505,-8.925732,8.009392,-1.299824,2.890366,-1.669384,5.034721,-7.862045,0.352958,5.837967,-5.833064],[-5.506114,0.564607,0.550575,7.433625,-9.516918,1.998348,-5.374841,-2.090633,-9.552835,-1.297815,2.394921],[6.983705,-7.685256,7.070403,6.893030,9.379389,0.366682,4.920141,-9.083127,-9.253693,1.556070,4.991032]],[[-1.956811,-0.042397,3.902014,3.731746,9.756182,-9.813030,-4.378215,5.770920,1.249188,8.536741,3.682389],[8.825098,0.028123,-5.935705,-8.230333,3.131785,4.412174,0.680668,-3.769608,9.345256,2.679903,2.492871],[-3.682516,9.670945,-8.676746,-2.372426,9.146585,7.904830,-8.735208,-7.056114,4.645361,1.089274,8.099680],[7.230800,-5.842069,1.415306,-4.327683,8.027426,-9.869601,-5.640950,6.640512,-6.933366,3.346342,-6.667810],[-0.418843,-2.226397,-1.251312,-1.461835,-7.122731,6.423005,9.109205,-9.671304,9.575126,-5.610789,-9.768302],[-1.427260,6.504272,-0.289973,-9.347320,-0.188411,0.323379,-2.434643,0.664886,-7.189542,-8.001964,-5.285981],[-1.103262,4.445773,-9.358739,1.121910,7.705270,-8.442857,5.257555,1.622417,7.594518,-9.249708,-4.563471],[-3.791907,1.425478,0.495076,-1.985688,3.810717,-9.428923,0.273345,-6.274178,4.697090,-0.752787,1.778559],[-6.459473,-9.550285,-2.594112,7.727508,3.304817,-0.853164,-9.340207,3.159571,4.253120,0.337793,8.144546],[-3.516674,-1.124261,5.153717,-7.348517,-3.205438,1.598897,-9.897586,0.359690,-4.849831,-0.610055,4.870514],[-1.076635,8.021003,-0.324524,2.068570,5.580233,3.000523,9.610894,0.840322,1.835490,4.939621,-2.120537],[1.433046,2.184203,-0.597954,-1.661360,-2.830869,-7.226086,4.251048,-4.047316,3.251118,-9.523022,1.013566],[7.567643,9.082669,-1.978063,-8.971117,0.745720,-8.234464,6.022822,-1.009327,1.724523,3.579408,-5.540058],[-3.001344,7.240344,4.867419,-8.566120,-4.205151,7.100518,2.494674,-3.115994,-8.667031,4.911432,-5.582968],[4.115668,-8.088458,7.814175,4.834739,-4.554276,-7.715919,9.856301,-3.246046,1.142851,5.822770,-4.804549],[-6.281338,-3.097814,-1.814386,-4.447765,6.341961,9.388482,-6.903898,4.736576,4.570906,8.845380,9.315038]],[[4.710657,-0.188709,-8.697036,4.556265,-9.653558,0.640841,-3.986578,-3.355208,-8.555827,-3.524095,-7.445761],[-5.402713,-6.366947,2.490075,-7.874533,-0.737323,-7.741457,-7.951205,7.233191,-4.450557,0.959005,-9.460827],[1.927942,-0.419935,-2.236612,-7.481775,9.934888,-6.204374,-3.649770,5.216861,6.935486,-3.234020,9.878889],[-2.888933,-2.741698,-6.584985,8.827462,4.695566,-0.683767,-6.106896,-5.190734,5.792575,-0.250549,-6.695432],[8.422147,4.527676,1.197192,7.103210,-5.823667,4.289876,-9.160103,-4.786584,7.552080,-3.636269,-8.062173],[-2.427545,1.614717,-1.986462,-3.860015,-5.139384,6.263080,-8.282653,4.765501,9.565790,4.251864,-2.939805],[-7.533159,4.847456,-5.174511,3.148682,6.871104,-0.986482,0.314181,-8.928375,5.092059,-8.606314,-7.158807],[5.504679,-0.208812,4.400410,-6.534234,6.287936,-2.551253,-7.481657,-4.299959,6.713446,1.613567,1.117905],[5.899018,-5.528610,-6.084954,9.695687,2.638449,3.742337,3.764781,-0.466586,-6.284020,-7.176971,-4.917928],[-2.850645,4.274972,-3.273091,5.557641,9.631506,2.962465,1.302312,-7.591118,-2.964548,2.567812,4.493662],[-5.125093,-1.374696,3.524853,-0.547822,2.108467,8.202662,-3.570092,-5.793964,1.804779,-4.331306,6.623120],[-8.674450,-4.277636,-7.461682,-1.082379,-7.952488,4.117272,-3.027066,-9.787984,-2.390224,0.021338,-4.469224],[-8.251116,3.277012,-3.057309,-7.244476,0.489404,-4.997075,-2.712479,2.898777,-3.984085,9.126613,6.207699],[5.903567,-1.607961,1.324490,9.444629,-4.504064,-7.436536,1.891970,5.132609,0.643382,-9.676519,9.681651],[-6.750034,-6.196989,-9.185522,-2.070448,3.522851,3.415169,8.158438,0.463707,-0.770010,-4.901579,2.440228],[-3.813659,-5.531371,0.525628,8.971537,9.960390,7.453029,-6.947235,5.109853,3.397471,-5.400789,9.138636]],[[-0.107250,-2.647067,-1.765111,8.163872,-8.646298,-3.988128,3.492666,-7.865550,-8.149037,-4.751895,2.011045],[-3.685432,2.761845,2.171035,-6.963019,-6.194743,3.016073,-1.505527,3.562858,8.066725,7.152367,-2.453188],[5.159980,0.296000,-0.011301,4.706856,-5.446466,6.326001,-9.375854,-3.282179,2.329593,4.778861,9.371306],[-8.807091,9.754868,7.747393,5.932845,-1.110229,-4.026199,7.486920,9.864573,-2.411240,-0.816803,-4.186999],[-9.226644,6.557360,9.652088,-6.877597,-0.631688,4.690288,-1.491368,-5.541349,7.400782,-3.136324,-5.504511],[-5.866183,-1.004151,-4.882989,-9.504359,8.682905,9.680295,-1.587309,8.172245,9.221375,3.622728,-9.642372],[5.418054,-6.739502,0.740774,-3.738747,-6.146414,2.784464,7.076328,3.463014,-3.274548,-0.278312,1.846125],[-6.471719,5.141412,9.721181,3.822105,-5.880570,-4.316913,6.195417,1.634083,-3.315381,-2.445542,6.928809],[5.636277,-0.318785,7.097886,3.927028,7.845734,-1.060848,4.441067,-7.497370,2.316136,-2.398065,4.707178],[7.014711,9.272167,-4.477013,6.728729,-9.795553,-5.615305,6.694937,7.466010,-6.538369,-1.040832,-6.269508],[-4.724726,-8.423438,2.585784,-9.009943,-8.811401,-1.659229,3.416608,-1.087332,-0.925449,8.429733,0.602921],[-8.099639,5.835847,2.422725,1.674598,9.034618,-6.976937,5.949593,-2.205067,-2.416009,2.791487,8.580508],[8.083813,-6.899149,-5.107689,-6.805841,-1.944421,-2.752554,-0.438655,3.336367,6.998968,5.058471,0.559705],[-5.395130,-6.087029,-4.260944,3.444950,-2.215472,3.855944,-8.647969,-2.150445,6.456637,9.140817,-8.038496],[-9.176339,-4.074444,9.280579,0.814343,-2.760637,-8.619893,6.134780,2.848988,-8.588664,6.916716,-9.012654],[6.267555,0.891615,0.758381,8.531008,-1.722589,0.604076,3.140045,-0.298310,5.429385,-0.985047,-5.431209]],[[4.021327,-9.808253,3.368463,3.716605,6.180713,3.489162,-3.362695,-0.493502,-8.213998,6.978481,3.286267],[-0.203319,9.558443,-8.063857,-8.488280,6.984658,-2.009213,0.068298,-9.347168,5.244296,-4.522858,-3.471760],[7.966370,-6.628644,7.046793,-1.548817,-9.591151,-6.958438,-7.237627,-4.932775,8.593146,-2.431811,4.669751],[-8.621247,3.460268,-0.173059,-6.362468,-5.220170,5.368257,3.312178,-9.888655,9.600357,0.602919,-2.009606],[-8.038220,-6.513594,1.358896,-7.983114,-1.279229,-0.596966,-5.733522,5.919828,2.648688,5.228350,-8.211740],[6.884063,-1.679536,-7.197034,-8.619100,9.784113,2.446793,3.052949,3.300370,0.436309,-6.304642,0.595361],[-3.754595,8.341138,-2.489429,-9.965541,5.885654,2.819754,-7.981710,5.054709,-4.806024,-8.600448,-8.400521],[-8.005824,4.946876,-7.830851,9.228827,-5.661149,-0.733583,8.449990,-6.637201,-4.580815,6.396672,2.454116],[1.033814,8.170477,-5.787457,0.040903,4.568283,-7.478524,2.631166,-6.126755,-7.424460,6.766212,-8.155347],[7.392962,-6.773745,-1.520255,3.747644,-1.048126,0.579281,-4.662817,1.866775,-8.844215,-3.260720,7.517412],[0.054486,-6.118821,-1.944066,8.674687,3.834916,-0.242975,-0.369044,2.431290,-0.573900,-5.454165,9.458409],[3.551316,-4.475028,4.866041,-4.300843,-6.927676,-1.149621,5.373062,-9.742500,5.747176,8.745442,-4.393332],[7.113593,2.710107,6.642816,8.054241,5.690849,5.955465,-1.763644,-2.547909,4.715310,9.191062,8.516048],[-5.965848,0.743620,1.635448,3.417592,-2.270544,-2.852747,7.689468,4.283334,-8.686987,0.357668,-2.685517],[4.074514,2.714765,2.505690,-0.392391,1.972423,4.657735,9.262959,-7.287909,-8.145927,1.041292,-1.285698],[-8.352378,5.783679,-2.458043,-0.328606,-1.186501,5.129669,-7.505670,-2.237367,-7.026788,4.354435,-7.396890]],[[-2.087091,-5.259083,4.962220,7.492859,-8.308642,4.937322,4.720225,-7.591036,-7.553209,2.262675,-2.221838],[0.874284,-6.962683,8.409387,8.261323,-5.315161,-5.508145,-7.771388,-8.305863,9.910903,1.889647,-3.932702],[9.546843,-0.479112,-4.605509,3.236332,5.291816,3.643054,-3.663904,7.233336,5.558131,-8.507158,-0.927300],[3.262831,-9.023677,7.215975,-8.879085,-3.583175,3.304367,6.473513,-2.650273,-3.380337,8.701123,-7.452384],[-9.396600,6.442889,2.425603,7.139557,-6.221167,5.784675,-2.992250,-0.618054,-9.987434,-3.020081,8.114910],[5.201763,-5.497385,1.362487,-7.127212,-8.959952,-6.603418,-1.221763,6.790008,0.334163,-9.313417,-6.985704],[-9.182998,2.560558,-1.063962,-4.834048,-1.797772,1.234495,7.867739,-4.911366,-6.149411,3.717417,3.374729],[2.445844,7.656794,-9.541061,4.059694,-7.038199,-3.858629,-1.510252,5.158488,-3.877107,8.267468,3.283415],[9.274186,-5.669045,-3.145790,-6.162920,8.016989,-6.096062,-8.534555,-8.544729,1.836800,6.038742,8.839566],[-8.089005,-7.746337,-8.035659,2.393496,9.234940,4.238960,-0.162124,0.979960,4.419544,-7.610713,0.304909],[9.118271,-2.776730,4.238854,-2.599667,-6.892628,7.227883,7.884281,-4.597700,4.863699,6.389573,2.680212],[-7.126208,-4.082163,4.076343,9.020133,-3.887249,-5.536391,-3.231982,-3.509432,-0.306618,3.526466,-7.092873],[7.694792,4.331570,-3.436033,-3.854566,3.405371,-9.160868,-5.678035,-8.859354,-9.198819,-1.354501,-9.337772],[-7.344426,4.209656,6.706185,4.703569,-9.021219,-4.797947,3.558825,-3.523985,-5.631372,8.109703,-4.168339],[-1.356562,0.166266,1.893344,3.423093,-4.248126,-9.836948,3.165208,2.962837,7.717642,4.627329,5.657006],[-2.629729,-0.743779,1.480736,9.623774,-4.657140,9.199787,1.511567,0.017026,-6.942634,-6.075667,-4.327824]],[[-3.099165,-7.890196,2.544420,6.321683,8.479012,-7.441304,-0.419805,0.714278,7.642299,7.309001,0.081715],[9.322021,0.163259,5.505943,8.353923,8.386231,4.231341,3.206848,-0.076615,7.537444,4.047126,7.483643],[-6.542772,2.500357,-4.760780,-5.899617,3.784283,1.648275,3.302955,9.002813,-6.841468,-6.611238,-1.203225],[-1.665637,-7.494968,-6.712442,4.263618,0.104532,-5.895239,-5.990291,4.422943,6.444432,-0.148334,1.052825],[0.296388,-9.221469,-4.799967,4.638926,6.084157,6.864654,4.594456,1.539605,7.102781,-5.326265,8.173251],[4.281392,5.243955,-3.225896,6.488728,2.211531,-1.506149,-3.367090,-9.703010,8.348253,5.041543,6.631604],[6.138075,8.290292,6.260503,-0.330891,-7.411197,9.584854,-0.142849,-9.627050,-2.288613,-7.894391,3.459082],[3.408148,-4.489702,6.941326,9.668650,9.509019,1.404286,9.945628,-8.531932,-6.996401,4.542657,2.071934],[5.455766,0.202240,6.244890,-5.090095,-0.874589,7.454500,-8.608832,-1.151801,1.176523,-2.748381,7.169015],[-7.973571,-1.698845,-8.802045,-5.686778,5.689497,2.625130,6.312555,2.129424,-6.747386,1.950137,-9.465558],[-9.263345,6.788405,-6.353234,3.039534,-8.301197,-4.508866,-7.145525,-8.992479,-0.474138,-4.634117,8.475992],[-4.332489,5.997119,-2.741565,-8.447637,-4.095557,-2.105557,5.273056,-5.436166,-0.390882,-9.293279,2.171673],[9.914180,3.312741,4.368013,-5.456663,-8.956131,8.907363,8.377044,-0.449703,1.205266,-0.410311,1.891786],[-2.579563,-7.537363,-8.786197,9.226676,1.826040,3.227949,-6.982842,-2.652143,5.463009,-1.495084,-6.376025],[3.468056,2.649370,-6.826556,-5.206338,4.534183,7.198613,4.764082,-5.864242,2.906053,8.089377,5.736732],[8.268487,-3.014867,-2.134322,-7.635290,-8.099590,5.256809,-0.111986,-8.101326,5.415883,6.471954,4.563278]],[[-0.603403,-2.711402,-0.396760,4.474289,9.601088,9.648954,9.584762,-7.866206,4.916560,1.410819,2.196032],[-6.007328,-8.992521,7.239546,-5.253639,-2.910224,7.786470,-0.941019,3.316235,7.059149,-2.723471,-1.781206],[-4.572985,5.268775,-1.769498,-5.809079,-0.235094,9.903403,7.481712,8.984543,7.984920,-2.901052,-0.916264],[-9.881570,-9.282473,-8.033657,1.378601,7.660899,-6.243592,9.990970,1.473004,-7.094321,-5.225848,3.900141],[-4.986291,1.284040,-9.976478,-8.058252,-9.878000,-1.155492,-6.918366,1.595860,-2.809775,3.773185,-1.781501],[8.886323,8.966392,8.075380,9.453816,1.919546,6.085516,5.052559,-1.494718,-9.783159,9.780063,-4.739466],[-1.159512,0.377351,-0.391334,7.420550,9.581852,-1.301387,-5.862825,-1.888942,-9.941057,1.616105,-8.241528],[-8.128714,7.681339,2.415944,4.407878,-8.939379,8.386085,-1.440949,9.464751,-8.911699,-4.840254,6.375317],[1.338267,-1.632595,5.117104,7.173426,2.698231,-8.027724,1.123223,0.381723,5.092274,-1.231146,8.586615],[-8.544662,-9.883020,0.601432,-2.367747,2.773295,-8.717616,8.135464,5.835526,2.029259,-0.290719,6.502405],[8.885514,6.654029,8.807557,4.024467,-1.836018,4.720031,0.670947,-1.856544,1.332629,3.779305,3.584921],[8.038828,2.878139,2.084153,-8.187548,7.882864,5.914521,2.543708,-3.520910,1.928966,-2.318538,8.771037],[6.239601,8.682540,7.950580,-7.746007,-4.412493,-8.818998,-1.325152,6.900891,-2.614231,-7.497106,2.107338],[-1.762640,4.057702,1.901847,-8.198763,4.930898,-7.723681,-1.738676,0.458500,-2.585193,-3.260883,3.385829],[4.287609,-4.210855,-9.019007,4.977619,-5.382745,1.201701,-7.475143,9.063911,-8.192334,-7.007706,-9.688093],[-2.542303,-6.726749,0.267488,5.941479,8.706310,6.713542,1.541411,4.534572,-0.187569,-4.792586,2.042794]],[[-5.613439,-1.631731,6.022783,6.356003,1.805827,6.059097,-5.973478,0.767656,6.305305,-1.404821,-5.237724],[-0.812689,9.406489,7.019558,2.570274,-7.412166,7.635322,-2.256532,7.161864,-3.265753,5.211591,-6.557803],[-9.039628,-3.857076,3.064072,1.324120,-7.787048,3.723259,-1.287035,2.415652,5.936110,4.967104,-2.861953],[5.322041,6.524222,0.775541,0.792474,-0.612270,0.964532,7.445045,-0.880169,-9.187054,0.987116,-0.782974],[-3.598340,4.558341,2.148011,-4.284311,-5.026027,6.872443,-7.037754,-7.552472,7.253518,4.300066,0.142359],[2.803522,6.068095,-6.614322,7.771458,-3.123926,1.115557,2.296617,-0.839756,-1.756216,8.427875,-3.879929],[-7.329803,9.314719,-6.761820,-3.213550,8.592958,8.418392,9.775759,1.123257,-9.348888,-3.637988,4.325769],[-3.664369,-6.801239,-9.490767,-5.177220,4.962093,-8.284521,-5.928221,8.140102,-7.731658,-1.543658,-7.601583],[-2.567781,-9.327354,2.714863,-4.388224,-0.999862,7.282240,6.826495,-5.779299,-5.091790,7.355547,-9.652346],[7.956035,-3.331871,9.716466,0.439609,7.431436,5.577341,-2.467331,-7.174900,-8.731398,8.785014,9.470025],[7.625017,9.377843,6.159262,-0.046589,-5.379828,-8.960978,-7.473457,-5.108386,8.854922,8.603043,6.118099],[9.801855,-6.082035,4.452788,0.670810,-5.772991,-9.596436,3.378907,-8.146078,-4.319806,5.838727,-6.049472],[-7.682041,-0.277809,-1.791611,-2.798722,8.218039,4.312918,6.933286,-0.284135,-7.570126,-0.713197,-1.362886],[-4.998313,0.230043,0.401844,5.307695,-7.076644,-3.197495,4.832407,-6.153967,6.452089,-2.112989,7.573058],[7.266473,-0.974254,0.548168,-6.933251,-6.252666,-6.516874,6.342863,7.925372,7.287681,-4.470556,-7.200791],[-6.923352,-7.724430,-7.970560,8.059560,-1.530798,0.059990,-2.628538,8.960780,-8.991147,2.108408,-3.160450]]], dtype = "float32")#candidate|12333|(13, 16, 11)|const|float32
uop_12334 = relay.log10(const_12333.astype('float32')) # shape=(13, 16, 11)
output = uop_12334
output2 = uop_12334
func_12339 = relay.Function([], output)
mod['func_12339'] = func_12339
mod = relay.transform.InferType()(mod)
mutated_mod['func_12339'] = func_12339
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12339_call = mutated_mod.get_global_var('func_12339')
call_12340 = func_12339_call()
output = call_12340
func_12341 = relay.Function([], output)
mutated_mod['func_12341'] = func_12341
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4735_call = mod.get_global_var('func_4735')
func_4736_call = mutated_mod.get_global_var('func_4736')
call_12345 = relay.TupleGetItem(func_4735_call(), 0)
call_12346 = relay.TupleGetItem(func_4736_call(), 0)
output = call_12345
output2 = call_12346
func_12366 = relay.Function([], output)
mod['func_12366'] = func_12366
mod = relay.transform.InferType()(mod)
output = func_12366()
func_12367 = relay.Function([], output)
mutated_mod['func_12367'] = func_12367
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8736_call = mod.get_global_var('func_8736')
func_8737_call = mutated_mod.get_global_var('func_8737')
call_12370 = relay.TupleGetItem(func_8736_call(), 5)
call_12371 = relay.TupleGetItem(func_8737_call(), 5)
output = relay.Tuple([call_12370,])
output2 = relay.Tuple([call_12371,])
func_12397 = relay.Function([], output)
mod['func_12397'] = func_12397
mod = relay.transform.InferType()(mod)
output = func_12397()
func_12398 = relay.Function([], output)
mutated_mod['func_12398'] = func_12398
mutated_mod = relay.transform.InferType()(mutated_mod)
const_12422 = relay.const([[[8,5,1,8,1,8],[7,8,2,8,4,1],[4,8,10,5,6,-6],[1,2,5,9,9,9],[7,7,1,-7,5,2],[-5,-3,-8,9,-6,-3],[-3,10,4,-5,7,2],[9,-5,-7,10,-4,5],[4,5,-7,1,-5,-3],[-10,-9,2,5,1,6],[6,9,8,6,-10,-2],[-9,8,-3,2,1,10]],[[-3,5,-4,-3,6,2],[8,6,9,4,10,-2],[4,8,-5,9,3,3],[4,8,10,1,-8,-3],[-6,4,8,1,-2,-7],[5,-7,9,-6,8,2],[5,-5,2,-1,4,6],[-3,-3,-6,-4,-6,9],[-2,8,-10,9,8,10],[1,-10,-7,8,3,-3],[-2,8,-7,-3,4,3],[6,9,6,-3,1,6]],[[8,-5,7,-8,6,-9],[4,6,-7,-4,-10,4],[4,-7,-9,-2,6,7],[-7,4,-2,-8,5,6],[2,-5,-3,-10,-4,-2],[9,1,-3,-1,-5,6],[8,-6,10,6,-2,-4],[-10,3,-3,-9,9,10],[-10,4,5,-5,-6,7],[4,9,4,2,10,-10],[-10,-5,-10,-3,-5,-8],[-9,-5,-5,-2,-8,7]],[[-4,8,6,-7,6,5],[7,6,5,2,8,-10],[8,2,-2,-7,-7,2],[-2,10,-1,4,3,9],[6,3,-7,-5,-4,2],[-5,6,-6,7,-7,6],[2,-7,-1,-6,-8,-1],[1,-9,-2,-4,-9,-10],[7,3,-4,6,-8,-4],[9,-6,-10,-1,4,7],[2,4,2,-6,-1,4],[9,-3,5,8,9,3]],[[2,10,6,1,-9,-7],[8,1,-6,5,7,2],[9,-5,5,-8,2,4],[-5,3,-9,6,-8,7],[2,-9,1,-8,-3,-9],[-1,-9,4,10,-8,5],[7,-5,6,9,3,6],[9,-4,-7,3,1,2],[3,7,8,9,3,8],[-3,9,5,9,9,6],[-8,5,-9,7,2,-5],[5,-4,5,10,-1,3]],[[-2,9,8,7,-4,-9],[1,7,1,-4,4,-7],[-3,9,5,1,-8,1],[6,4,-4,5,1,1],[-1,-10,-4,-8,-5,-3],[2,-2,-4,6,2,-2],[-5,4,-8,-9,9,-6],[6,3,2,4,2,4],[-8,8,4,-8,6,6],[4,-2,5,-9,-1,-4],[8,9,-3,-6,5,3],[-3,-8,-3,-10,2,-2]],[[-10,-9,3,6,-3,-3],[-9,-7,2,-4,3,1],[-8,2,3,-6,7,3],[-9,5,-3,-8,7,7],[-7,4,2,-5,6,-10],[-3,9,-10,-2,-1,-2],[-5,-9,8,-2,8,7],[1,2,-1,-6,7,-4],[8,-9,-5,7,3,-2],[3,-10,-10,-3,-8,8],[-7,4,10,2,-6,-10],[2,-8,-5,-8,4,1]],[[4,5,-9,3,-5,-10],[5,-4,-5,-9,-10,-3],[-9,3,-8,9,10,-4],[-7,7,-4,-9,-10,-9],[7,-1,-6,2,-5,1],[3,5,-4,-4,-8,6],[-7,2,-8,-2,8,2],[8,-9,2,6,8,1],[-2,6,6,-3,-7,-2],[-5,-9,-8,7,8,-10],[-4,8,-10,7,-3,-4],[-4,-2,10,-5,-8,8]],[[-9,3,10,10,2,7],[8,-3,-6,-10,2,1],[-5,8,5,1,-2,-3],[-10,4,2,3,7,3],[-3,-4,-4,-8,3,2],[6,2,-10,8,-8,9],[6,-4,-7,6,9,-4],[5,1,2,6,7,-3],[10,6,-6,10,8,-4],[-10,-7,-2,-9,5,-5],[-5,4,-6,10,10,6],[2,9,1,-7,6,9]],[[4,-5,9,-5,-10,6],[-8,3,-2,-6,-8,-4],[-10,9,4,-6,-7,-7],[-10,9,-3,-5,3,1],[-9,-2,3,6,-9,-1],[-3,1,-5,-6,-1,4],[-4,-5,1,4,4,-6],[2,-10,9,3,-8,3],[3,10,-4,7,7,5],[-9,-7,5,-2,5,9],[5,7,-8,-9,-8,6],[5,-2,-5,-10,7,9]],[[-1,10,-5,2,-5,-3],[9,-6,1,1,-5,-8],[-1,9,6,-10,9,6],[3,3,-7,2,8,-3],[2,-5,-8,-9,3,-6],[6,-7,10,-10,-3,2],[9,8,-6,4,-6,6],[2,-2,1,-6,-6,3],[-6,10,6,-1,-7,-10],[-9,-2,-5,-8,2,-4],[2,2,-2,-5,-8,10],[-8,-8,-8,-10,5,4]],[[8,1,-6,5,-4,5],[3,-6,4,4,-9,-8],[1,5,-8,9,3,-6],[-2,4,-9,4,8,3],[-10,-5,-7,5,1,-7],[-1,4,4,-10,2,-6],[4,3,2,5,10,10],[-4,-9,-6,-3,3,-8],[7,7,3,-2,-3,-10],[-10,-6,6,-2,-2,-7],[-9,3,6,-1,3,-4],[-3,-3,3,1,10,-8]]], dtype = "int16")#candidate|12422|(12, 12, 6)|const|int16
const_12423 = relay.const([[[1,-7,-5,-3,8,-1],[7,-5,-10,10,6,-2],[-8,-10,5,4,-7,8],[-7,7,7,8,-5,10],[-5,5,-6,2,5,2],[-1,7,7,-10,-8,-10],[8,9,-3,9,7,9],[1,9,5,-8,-8,-4],[2,-9,-4,-5,9,4],[-1,1,-6,-3,-4,-5],[-4,5,9,6,7,4],[-6,-2,3,10,10,5]],[[-2,3,3,-4,2,-8],[1,4,1,7,-7,4],[-8,5,6,4,-8,-1],[-6,7,-4,-8,-1,3],[10,-1,1,-6,-10,7],[-1,-1,7,-10,-8,-8],[4,-9,6,-8,2,-3],[3,-1,2,-10,-8,-4],[4,5,-4,6,1,-4],[-7,-3,-10,-1,-10,7],[-2,-7,-9,-3,-8,6],[-5,10,10,-3,4,8]],[[-4,8,-3,8,-3,4],[-7,-4,-9,-4,5,-8],[-8,1,-7,-8,8,-7],[-3,6,9,6,1,8],[10,-2,-8,9,-1,9],[-9,-1,5,8,10,-5],[-6,-4,3,-6,-5,-8],[-9,10,7,-8,-8,-3],[-6,2,5,-6,10,-9],[-3,6,3,3,-2,2],[2,-6,-10,5,10,-3],[-7,-9,8,-10,2,10]],[[-1,-5,-6,2,10,10],[7,-7,5,5,6,10],[3,-6,-5,8,7,-9],[-4,-3,-9,4,6,-6],[-1,4,-6,-3,2,1],[6,-5,5,-8,-5,1],[1,9,-9,10,-7,-7],[-7,-1,2,8,3,10],[7,5,6,3,3,5],[-8,-2,-9,9,3,-5],[-2,-10,-6,3,8,-3],[-3,-2,-10,-8,3,-5]],[[-1,8,-4,9,-4,1],[1,3,-1,4,3,-10],[-6,-3,-8,-1,3,-5],[2,3,4,8,-9,5],[-7,1,6,5,10,10],[8,-1,3,-8,-9,-3],[-8,-8,-9,-4,-1,-6],[-8,8,-1,-8,-4,-10],[4,-3,2,7,4,4],[8,2,6,-6,-1,2],[7,-2,8,9,1,-4],[6,10,9,-7,-5,8]],[[-9,6,1,5,-8,10],[-9,6,8,3,-5,8],[-9,1,-6,-5,-5,8],[-9,-5,-9,10,3,8],[-10,-7,-3,9,2,8],[-10,4,6,-3,-6,-1],[-3,-3,-9,-8,-9,5],[4,4,5,5,-6,1],[4,8,-2,4,-10,-2],[5,9,6,4,8,-7],[3,-8,-2,3,-3,-3],[10,8,2,10,-9,1]],[[-2,7,-6,-3,-6,-8],[-10,-2,3,-7,5,-2],[5,-6,2,-4,-4,-4],[-5,7,-10,10,9,-2],[-1,5,4,3,-1,8],[6,-8,2,9,1,-9],[-5,2,2,6,4,-9],[9,10,3,-3,-9,-9],[3,8,-8,-8,7,6],[-5,-5,2,-9,-8,-2],[6,-9,-6,-6,10,4],[1,8,-1,9,7,-5]],[[8,1,-3,-6,-10,-6],[7,7,5,3,5,-4],[-8,-4,-5,-3,3,10],[6,-6,2,5,1,-7],[5,-2,3,-9,-9,5],[4,-8,9,2,3,-6],[-10,-8,-4,9,7,2],[-7,3,5,-1,-4,-5],[-6,-10,7,-6,6,-9],[-1,10,10,-9,6,-5],[10,10,-7,-8,-4,-2],[6,-7,3,3,-4,1]],[[-8,3,2,4,5,7],[1,-5,-4,5,6,-4],[-7,3,1,-5,6,-2],[-7,-2,2,-6,-5,-7],[7,-10,-5,-4,-1,-4],[-2,-3,1,9,-4,2],[-10,-1,1,-3,2,-3],[-6,-9,-7,9,-6,-10],[-10,4,-9,1,9,2],[2,10,7,-10,2,7],[-6,1,-1,-8,-7,8],[-1,5,3,-9,1,8]],[[3,-10,-1,6,-7,9],[7,2,10,-2,-9,10],[-2,-6,8,-2,5,-10],[3,4,-5,8,10,6],[10,-10,2,-10,9,-1],[1,10,9,4,5,10],[3,-2,9,-3,-3,-5],[-3,3,-2,-8,2,-1],[-7,-1,-5,2,10,-2],[-1,8,-8,-3,10,10],[2,7,6,-3,4,-5],[6,10,-3,-6,7,-10]],[[-9,-5,-9,-10,-5,-3],[6,-3,-1,-3,10,-2],[4,-7,2,-8,-10,-9],[-8,-8,-8,3,10,-6],[8,7,-3,-1,8,9],[-7,10,-10,6,8,10],[-6,3,2,-8,-1,8],[-5,2,-9,5,8,3],[4,5,-3,1,-1,-7],[4,-3,2,8,10,-3],[10,3,3,7,5,-1],[-8,-10,-7,-2,-2,-5]],[[-6,-4,-2,5,6,2],[-6,-1,3,-9,-4,-2],[6,1,10,-4,8,5],[8,-6,10,6,-8,-4],[8,-2,10,3,-9,-6],[10,-7,8,2,4,10],[5,7,-2,-4,4,-5],[1,2,4,-9,8,5],[-2,3,5,7,1,1],[6,-6,-3,-9,-8,-4],[-9,-7,1,-4,-10,-8],[-10,3,8,5,-1,-6]]], dtype = "int16")#candidate|12423|(12, 12, 6)|const|int16
bop_12424 = relay.maximum(const_12422.astype('int16'), relay.reshape(const_12423.astype('int16'), relay.shape_of(const_12422))) # shape=(12, 12, 6)
output = relay.Tuple([bop_12424,])
output2 = relay.Tuple([bop_12424,])
func_12438 = relay.Function([], output)
mod['func_12438'] = func_12438
mod = relay.transform.InferType()(mod)
mutated_mod['func_12438'] = func_12438
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12438_call = mutated_mod.get_global_var('func_12438')
call_12439 = func_12438_call()
output = call_12439
func_12440 = relay.Function([], output)
mutated_mod['func_12440'] = func_12440
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5379_call = mod.get_global_var('func_5379')
func_5380_call = mutated_mod.get_global_var('func_5380')
call_12460 = func_5379_call()
call_12461 = func_5379_call()
func_4504_call = mod.get_global_var('func_4504')
func_4508_call = mutated_mod.get_global_var('func_4508')
const_12466 = relay.const([3.821333,-5.684133,-6.211576,-4.631555,-6.500393,-5.356629,-4.076846,1.739240,9.194804,-2.419093,-2.442271,-0.655351,4.108888,7.515629,8.296945,-8.636186,-5.347834,-9.546534,-2.257588,-8.395462,-9.304434,3.103039,-3.747902,-2.598263,9.240314,1.586369,5.554146,-0.360710,5.279909,5.144427,-3.924592,4.929210,3.064902,5.233399,2.071576,-0.610293,7.696043,-5.588437,-3.464187,6.969492,6.613427,7.245661,-0.838912,-9.307779,7.054032,-5.194735,7.875881,9.818580,5.058502,0.357696,-5.298573,7.110582,5.478953,7.315912,-8.089396,-4.925946,6.486396,-0.951544,9.013744,6.356705,5.623357,-9.371030,7.072740,4.128732,-5.856569,4.594330,-0.333860,-7.211712,-2.160018,8.278432,4.955372,7.929965,-3.506362,-6.793932,-8.568237,-2.040421,-4.725128,-9.627580,-0.924070,-8.713769,-8.966021,1.672558,-9.083656,6.747265,8.188574,-7.627291,-4.998949,0.204957,1.353918,-0.257709,1.317037,1.264153,6.613117,-9.218217,9.071943,-7.206805,-7.428099,-1.144272,-9.715659,-4.321733,6.415171,-8.274055,-8.270625,-2.697730,9.404755,0.807192,6.458394,-2.324172,-6.153876,2.100651,-8.450023,-7.400975,7.486695,5.037588,-2.560475,-4.286033,-9.162657,5.263986,-5.363665,9.660990,-4.628879,0.252142,6.875688,-4.474246,-4.395027,-9.921405,4.251359,8.253781,8.645820,-7.751559,-5.118725,0.559472,8.659651,0.044351,-5.631795,-6.004911,7.632553,3.074843,1.917558,4.876116,4.894446,-4.261197,-5.850732,1.847973,1.992235,6.830436,-0.378870,-2.266915,4.088702,-5.377135,-3.037048,-5.369077,-3.639745,8.324398,5.010526,4.759174,-4.250062,4.423850,4.185998,-2.395165,4.635519,7.988266,6.192826,6.009972,1.547593,-9.632622,-2.504552,-5.021646,-6.159059,0.646857,-4.171115,-3.657408,-2.329149,0.890728,7.197406,-7.648369,6.405929,-6.629670,-6.711988,8.527206,4.412277,1.671759,-1.119236,-8.371522,4.298256,-0.430679,-8.677710,-3.518096,-9.649326,5.566696,-5.759751,-3.210473,0.169563,-5.532472,1.452789,7.994177,9.679297,-0.948284,-0.925088,8.849379,-5.365585,3.441653,-9.696932,-2.827730,5.941792,-9.744259,4.287983,8.952280,-8.174771,-5.722956,8.326643,-0.039938,0.765653,-8.381766,-1.021808,6.621494,8.485865,6.869319,5.436345,5.175064,6.091781,-7.501463,-6.055109,4.637222,9.266172,-1.612483,-3.784220,7.187889,-7.782865,7.349143,0.384775,6.482103,-0.168468,2.832240,-3.714213,-5.700520,-3.231643,7.969022,6.546837,1.461122,-2.714694,0.612655,3.558812,-8.563966,6.923286,-0.704245,5.036931,7.371270,-5.786393,8.459758,2.689926,8.195089,-7.103618,3.832475,5.703383,-9.767876,-3.042046,-9.901527,-3.264952,9.591061,9.192304,8.448761,-2.034085,-7.283871,1.961853,9.813998,6.203717,-5.597177,5.898754,4.663418,1.560583,8.394799,-1.491783,9.791305,-0.692746,-6.511558,-3.090947,-8.036028,-6.000394,7.946409,-1.865606,9.297689,6.748236,3.484826,5.119776,-3.232194,-2.039908,-8.424354,3.970731,-5.643468,4.874008,5.348092,-8.699828,-6.774418,-7.498076,-1.706020,-3.295935,3.828370,4.367400,8.168716,3.826464,0.157297,6.373823,-3.668491,3.453616,-9.569886,9.545551,-8.115012,-7.238177,2.365817,9.327980,5.929201,3.700027,3.071010,-2.422643,8.855347,-9.259567,6.942086,-6.586680,2.270700,-3.965842,-6.452196,4.107967,1.864356,6.369825,3.420171,-9.625948,1.719882,5.733333,2.831167,9.876214,8.144843,5.471479,4.234387,6.157141,-4.918226,-7.100252,4.294034,3.752367,4.256132,0.915845,8.996707,-7.835673,6.166187,-6.483828,5.113397,2.567272,3.121090,5.099706,5.946199,3.421753,1.528991,-0.448171,-2.025269,8.482105,2.557557,-9.015241,6.253626,1.758616,-4.510292,7.901313,2.450584,-3.214419,3.641806,1.532374,-9.306451,-8.220089,-4.666725,4.080721,3.747513,8.918694,7.455744,4.561874,-1.200674,-0.567138,-7.761665,-6.201686,-2.276828,4.778626,-5.275124,-0.572431,2.443955,-0.291080,-2.737506,-5.269220,2.404721,-8.362916,7.811991,5.804515,-8.809381,-8.765705,9.922645,-5.534793,-8.566632,0.528756,-7.189099,3.401787,5.198008,1.910740,5.111620], dtype = "float32")#candidate|12466|(400,)|const|float32
const_12467 = relay.const([-2.517508,7.171276,-8.993578,0.448787,5.438685,4.324206,-2.851195,8.482067,5.668781,-5.443671,1.571591,-4.432258,2.068495,1.846789,-0.933992,-4.925444,8.858171,-2.142667,7.068467,1.304390,-4.045811,-0.956500,-0.011607,7.257120,9.230347,-5.569841,5.242039,9.343693,9.462868,6.760893,-4.242148,-1.581067,7.958930,6.342667,-5.679459,1.798938,-1.114088,8.388685,1.867123,-3.363397,-4.212883,-2.189640,2.392131,-4.443957,-5.235664,6.015557,1.420401,-0.067066], dtype = "float32")#candidate|12467|(48,)|const|float32
call_12465 = relay.TupleGetItem(func_4504_call(relay.reshape(const_12466.astype('float32'), [10, 4, 10]), relay.reshape(const_12467.astype('float32'), [48,]), ), 2)
call_12468 = relay.TupleGetItem(func_4508_call(relay.reshape(const_12466.astype('float32'), [10, 4, 10]), relay.reshape(const_12467.astype('float32'), [48,]), ), 2)
func_7990_call = mod.get_global_var('func_7990')
func_7992_call = mutated_mod.get_global_var('func_7992')
call_12478 = func_7990_call()
call_12479 = func_7990_call()
output = relay.Tuple([call_12460,call_12465,const_12466,const_12467,call_12478,])
output2 = relay.Tuple([call_12461,call_12468,const_12466,const_12467,call_12479,])
func_12503 = relay.Function([], output)
mod['func_12503'] = func_12503
mod = relay.transform.InferType()(mod)
output = func_12503()
func_12504 = relay.Function([], output)
mutated_mod['func_12504'] = func_12504
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1984_call = mod.get_global_var('func_1984')
func_1985_call = mutated_mod.get_global_var('func_1985')
call_12555 = relay.TupleGetItem(func_1984_call(), 0)
call_12556 = relay.TupleGetItem(func_1985_call(), 0)
func_12229_call = mod.get_global_var('func_12229')
func_12231_call = mutated_mod.get_global_var('func_12231')
call_12563 = func_12229_call()
call_12564 = func_12229_call()
func_3402_call = mod.get_global_var('func_3402')
func_3405_call = mutated_mod.get_global_var('func_3405')
const_12586 = relay.const([0.361361,-9.173066,-3.630295,-1.104555,-7.497069,-6.101867,-1.836351,3.311039,7.206960,-3.298111,-4.810995,3.963610,-1.395564,1.906023,7.458712,7.319848,-6.892791,3.786835,9.298640,3.712472,-3.341142,2.095883,-5.203675,0.953884,-0.898604,7.924002,5.006496,-6.379822,2.892953,4.663274,1.804425,1.527376,3.215286,4.709418,4.186112,-0.339817,-3.692156,-8.466418,-5.379679,-6.743214,2.034530,-7.764124,0.779184,1.801979,-0.558522,5.203449,0.195375,4.773756,-6.541299,0.519625,4.631769,7.769230,2.494069,-9.709241,-2.132750,-8.916427,4.052605,-6.120195,-5.145495,7.516529,-1.699834,-2.962894,-8.360952,-6.048502,-6.508431,-8.983201,2.487548,3.851482,2.959087,5.776143,1.719870,-1.082414,-3.204803,8.834828,-5.146673,4.721422,4.154591,-9.492031,3.345067,-1.353308,-9.836008,-6.029896,1.135033,1.231599,5.608289,-3.115105,-9.660450,8.192542,5.163150,8.635103,-6.242589,-8.897001,2.126351,2.683106,-0.856560,-3.735524,-7.846299,-5.338854,7.877359,-7.526379,-5.990541,9.081342,6.796829,7.626562,9.741740,-4.260763,5.009344,4.644331,9.180815,-6.071894,7.200154,2.416286,0.344649,1.445534,4.533567,8.613899,-5.849168,-5.224084,-4.671760,-7.154767,4.841493,1.500191,9.168990,8.275695,4.181734,-2.958052,-6.188006,-4.956726,-5.165648,-3.570986,6.810700,6.029591,-1.311819,-1.479326,-8.667516,-3.498804,3.887082,-7.836012,2.206000,-6.380408,0.348117,5.647156,-1.786794,9.739628,3.396819,-1.263952,-2.433570,-7.187138,6.998732,6.463119,8.431091,4.649708,5.336985,2.162559,8.465300,1.981081,1.644786,4.495393,-9.974712,-4.133789,-3.507136,-5.049758,-6.835187,-2.906698,8.189916,8.912877,0.615963,-0.578932,0.538313,9.193455,0.117348,6.843412,2.757237,-0.643181,-3.677546,8.896586,2.472632,2.717658,-5.306779,6.889484,1.416133,-8.583103,-3.303666,1.724339,6.157313,-2.424231,3.686458,0.096298,-0.809342,-3.675900,-8.674458,-9.535987,9.334102,8.834812,9.548990,-7.518909,-1.924792,4.285008,3.938300,-8.725979,-9.137978,6.205433,-8.861532,-0.699454,-2.221366,3.368542,6.285233,-2.841537,8.178003,-0.670236,-7.328642,2.958564,-9.849331,4.633549,7.870923,-5.276351,1.715658,9.544293,-1.010550,-0.103757,-6.254716,7.707601,3.357218,6.427819,8.126415,9.504577,-7.256825,-5.824002,-2.146142,-5.788293,1.673131,0.170891,-9.163837,9.092357,-4.626625,7.387782,0.767655,-8.138513,-4.829395,-1.968790,-1.809833,9.833308,-6.990145,6.012616,-3.291407,6.297700,-1.493996,-3.902266,4.313333,1.893442,2.476554,3.931246,8.483334,-8.427867,2.296016,7.070557,-1.058329,-2.853368,0.634198,6.954167,6.244647,2.857159,4.435293,-8.135852,3.448932,6.897949,-8.614507,-1.067168,-1.006524,8.924949,2.490185,4.397725,1.212378,-1.261394,0.220855,-5.196961,-0.494777,-4.903175,4.076117,7.320430,-0.867854,-1.535371,7.237755,-5.237835,6.978291,1.712834,3.645339,-7.603022,-2.412499,7.353723,2.437435,-9.716182,7.390163,3.910116,6.590945,-2.306426,9.169086,-6.153541,1.227943,4.586979,-5.607437,1.454190,0.583162,-5.627975,-3.532277,-3.197023,-7.603766,-1.619796,4.546472,-5.395853,-0.659812,1.786565,8.028955,-3.744376,-4.558783,5.888043,-9.228935,-8.618899,9.539194,8.850764,-4.349973,3.974951,-5.810316,8.232240,1.031804,-8.546201,-0.559509,-7.541430,5.939260,-5.067579,-6.676984,-4.824888,-0.925472,-3.774656,9.517015,2.734036,8.673653,-5.082667,-0.582611,-7.281091,-5.572983,1.377199,-3.756080,-6.656166,-0.522066,1.746648,6.961391,2.411175,8.614627,2.944873,2.437731,-1.817529,6.653407,-9.688306,-4.894069,2.857017,7.478505,2.893086,-0.279849,8.490128,-3.989488,2.402462,-0.821470,6.434902,5.437885,7.230538,-2.430142,6.619842,-7.474767,0.100062,-6.139832,6.745943,-3.165448,2.362305,1.137916,2.494523,-1.799344,9.511843,-9.026356,-1.034830,2.839530,-0.725136,6.015759,6.325042,-9.530115,6.247754,9.375615,-3.759763,2.025140,2.123874,9.641963,8.384936,8.102531,-4.801164,7.014956,9.630235,-9.822359,-6.104224,-2.572028,-2.162816,4.553018,2.303870,-7.029701,-7.058865,-3.439095,-1.275552,-6.828176,2.328034,-6.927256,9.815018,-1.973306,-4.674946,5.861117,-1.873886,-4.091025,-6.675648,-3.576670,5.403455,4.476977,6.846935], dtype = "float32")#candidate|12586|(420,)|const|float32
call_12585 = relay.TupleGetItem(func_3402_call(relay.reshape(const_12586.astype('float32'), [6, 7, 10]), relay.reshape(const_12586.astype('float32'), [6, 7, 10]), ), 0)
call_12587 = relay.TupleGetItem(func_3405_call(relay.reshape(const_12586.astype('float32'), [6, 7, 10]), relay.reshape(const_12586.astype('float32'), [6, 7, 10]), ), 0)
output = relay.Tuple([call_12555,call_12563,call_12585,const_12586,])
output2 = relay.Tuple([call_12556,call_12564,call_12587,const_12586,])
func_12590 = relay.Function([], output)
mod['func_12590'] = func_12590
mod = relay.transform.InferType()(mod)
mutated_mod['func_12590'] = func_12590
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12590_call = mutated_mod.get_global_var('func_12590')
call_12591 = func_12590_call()
output = call_12591
func_12592 = relay.Function([], output)
mutated_mod['func_12592'] = func_12592
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12366_call = mod.get_global_var('func_12366')
func_12367_call = mutated_mod.get_global_var('func_12367')
call_12598 = func_12366_call()
call_12599 = func_12366_call()
func_4910_call = mod.get_global_var('func_4910')
func_4912_call = mutated_mod.get_global_var('func_4912')
call_12619 = func_4910_call()
call_12620 = func_4910_call()
output = relay.Tuple([call_12598,call_12619,])
output2 = relay.Tuple([call_12599,call_12620,])
func_12622 = relay.Function([], output)
mod['func_12622'] = func_12622
mod = relay.transform.InferType()(mod)
mutated_mod['func_12622'] = func_12622
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12622_call = mutated_mod.get_global_var('func_12622')
call_12623 = func_12622_call()
output = call_12623
func_12624 = relay.Function([], output)
mutated_mod['func_12624'] = func_12624
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12183_call = mod.get_global_var('func_12183')
func_12185_call = mutated_mod.get_global_var('func_12185')
call_12660 = relay.TupleGetItem(func_12183_call(), 0)
call_12661 = relay.TupleGetItem(func_12185_call(), 0)
func_4837_call = mod.get_global_var('func_4837')
func_4838_call = mutated_mod.get_global_var('func_4838')
call_12664 = relay.TupleGetItem(func_4837_call(), 0)
call_12665 = relay.TupleGetItem(func_4838_call(), 0)
output = relay.Tuple([call_12660,call_12664,])
output2 = relay.Tuple([call_12661,call_12665,])
func_12668 = relay.Function([], output)
mod['func_12668'] = func_12668
mod = relay.transform.InferType()(mod)
output = func_12668()
func_12669 = relay.Function([], output)
mutated_mod['func_12669'] = func_12669
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12673 = relay.var("var_12673", dtype = "int64", shape = (12, 11, 9))#candidate|12673|(12, 11, 9)|var|int64
var_12674 = relay.var("var_12674", dtype = "int64", shape = (12, 11, 9))#candidate|12674|(12, 11, 9)|var|int64
bop_12675 = relay.left_shift(var_12673.astype('int64'), relay.reshape(var_12674.astype('int64'), relay.shape_of(var_12673))) # shape=(12, 11, 9)
uop_12696 = relay.sinh(bop_12675.astype('float32')) # shape=(12, 11, 9)
func_4785_call = mod.get_global_var('func_4785')
func_4787_call = mutated_mod.get_global_var('func_4787')
call_12701 = func_4785_call()
call_12702 = func_4785_call()
func_9292_call = mod.get_global_var('func_9292')
func_9294_call = mutated_mod.get_global_var('func_9294')
const_12704 = relay.const([-8.946267,-3.600187,-1.387683,3.308825,-0.774155,8.525631,5.754319,9.364083,-6.776766,2.784018,-1.840259,7.887086,-9.862777,-3.020700,-3.707606,4.393851,-7.120546,2.090456,-0.158440,8.363624,-2.837084,-5.648351,-9.431972,9.045905,-5.815740,7.868093,-5.057578,-6.075466,-0.219150,-4.342117,-2.811510,8.055314,-3.976580,2.589879,-8.666539,4.242953,9.203063,-1.911599,-3.845842,3.516497,-5.747521,3.761450,6.642628,4.068773,6.461468,5.819001,1.950137,-4.328155,3.681017,-4.503961,-2.756263,-3.225114,-7.291790,-4.753227,-5.464038,2.112392,-2.844600,1.510698,-2.322501,-4.801729,9.168981,2.328590,-2.888561,-2.759672,-7.254747,3.924054,-5.261592,-9.477689,-9.116310,3.944643,-8.039317,0.253449,-9.673222,8.118462,2.025331,-3.406759,9.221846,2.048470,3.719645,1.166605,9.961347,4.346226,1.027236,-1.508745,-9.753736,-9.579031,-1.293960,4.598227,1.297612,3.066177,-3.381356,7.511330,8.998990,-9.061054,-9.418492,-0.790379,-2.459602,0.982255,-1.064662,-7.838631,-2.562548,2.756713,-5.347305,2.781453,5.859095,0.766597,-0.979705,4.782238,1.022381,-8.617053,-5.240022,6.228183,-6.567521,-5.801742,-2.749156,7.334242,1.670536,9.833939,-0.967847,7.380021,7.192390,8.541547,0.147173,-9.462090,-3.668718,-3.194999,0.825477,-0.765651,4.703000,-5.047550,0.012003,-2.492090,4.352527,-4.869897,-9.787601,8.732525,-3.190032,3.435872,-4.037932,0.775632,-0.945735,2.783331,2.018761,-8.488528,-2.820281,2.782714,-0.548381,-1.762537,4.306089,5.792316,2.501034,-1.461527,-0.635883,6.521868,5.921201,8.973482,5.742948,2.975518,-2.641842,9.224548,6.171617,-3.711497,-1.174825,8.672017,-0.999458,2.774636,3.197859,1.120625,5.776739,-0.729084,9.188808,-1.793686,-4.254576,-6.402218,4.410418,4.212403,-1.543715,5.074283,8.817877,-8.283449,4.361431,0.404976,0.024981,-4.482238,1.508174,8.361472,6.100859,9.341980,-0.005055,-4.992324,2.959323,-6.290628,-1.792055,-7.735743,-7.359259,9.247908,-5.597190,-5.549795,6.309303,-8.061504,-4.197264,-2.180556,-4.013339,8.528433,7.408791,-1.020764,-5.341165,-7.778446,-5.861975,-5.868304,9.135574,6.493332,-9.804759,-4.814703,-0.264521,-6.636146,-9.492312,-3.261686,7.407412,7.121001,-9.122343,9.311780,-3.703158,8.523571,8.707875,9.705838,8.648694,-3.312536,5.400653,4.026831,-5.397222,-0.373572,-7.996829,4.421735,-4.243322,-0.547403,-2.545255,8.230937,3.022495,-9.184324,-2.006929,-2.089767,-0.239505,2.442647,5.604724,6.639024,4.862027,-4.459149,7.865948,5.503115,1.054700,-9.232335,0.352653,-0.104700,-6.857420,0.468455,8.332601,-8.301585,7.918468,1.792320,-8.437695,-0.815327,-5.343586,-9.745743,-2.504084,6.626098,6.159920,1.491938,-0.622905,-6.874761,-2.482180,5.079307,2.704040,8.989231,-8.516725,8.709947,-5.013842,-1.638254,-5.892263,-2.878593,-5.161763,-5.786522,7.369923,-0.080045,-7.598764,-8.831716,2.143301,-9.194152,3.953584,5.157835,-9.438404,-1.075930,-3.014566,5.072613,2.000455,4.769238,0.703913,-5.090659,6.274301,-6.052345,3.500900,5.775103,3.038428,0.929339,8.445243,-0.747239,1.757049,-6.536433,8.113341,-8.455409,7.714344,-7.060060,-7.041073,7.324311,5.279811,7.551609,-9.934421,7.834171,-8.881719,-3.994380,0.075839,8.333477,-0.632725,-3.125388,7.086012,-4.769497,-5.924881,8.957059,4.981694,7.153489,9.375746,7.270152,2.231923,6.332254,9.533312,2.655672,-9.923989,4.526128,1.524384,-1.732672,5.393443,8.447169,4.056654,-0.320413,-2.830774,4.229276,-1.982705,6.967948,-5.463734,2.202542,1.225273,-1.147555,8.655256,-6.296623,-0.315797,7.674897,4.234627,2.482046,4.090812,-2.606968,3.207570,7.525602,-1.729774,4.333720,2.559771,2.438739,-4.384410,-3.460473,4.640165,-5.557134,2.471857,1.920464,-7.673881,0.537918,-4.801063,7.249780,-0.684696,5.380830,-5.466165,2.144415,1.634404,-7.596508,-0.565553,7.276495,8.426921,0.038351,2.351896,4.035294,-9.573377,-8.769763,-8.479378,-9.140260,-3.730954,-0.959744,0.652282,1.886158,-3.727685,-7.983636,-9.675662,-1.812083,4.395505,5.032989,7.600662,-7.973807,6.960013,-6.950352,7.487467,-2.245731,2.153635,-4.492148,-4.576560,1.594090,5.595547,-3.846406,-8.218002,4.492057,-3.054603,-6.114223,3.679247,4.503126,5.974515,0.972147,6.691226,7.938820,-1.151558,5.846340,8.348512,9.751749,-1.046374,-2.615590,-3.812308,-7.289673,-8.822216,-1.823482,5.930925,7.933631,-2.433505,9.563588,-8.707458,-9.889453,-2.421225,-8.456348,-1.051818,-9.518012,4.430412,7.225699,-9.142533,-5.857826,6.136826,4.083060,5.760583,3.890578,0.599341,3.924117,3.837146,-3.117311,5.769355,9.444233,-1.934716,-1.529024,1.649158,1.164936,2.419702,-2.504687,5.754216,3.952547,-1.890284,-7.919845,-1.495330,-7.254734,7.655449,1.419301,5.405780,-9.214697,4.632663,9.003538,1.349785,-2.312414,-8.121423,4.017166,-4.961882,-2.019483,3.340815,-9.611663,-7.073220,-1.914789,7.898059,-4.044499,-9.111169,-0.653001,2.053395,-8.032377,4.842918,1.741427,-4.924696,0.407143,-8.965117,2.979568,-7.777355,7.783495,-8.291994,-3.462717,8.522456,-2.913561,0.507195,1.880019,-4.091471,7.301642,8.337548,-4.278930,7.490291,-2.054268,2.617429,-4.595066,-4.297304,1.063861,7.464932,-5.055973,-5.818041,-3.275375,-4.367734,2.517216,-4.357706,-6.863737,6.210470,5.407820,-2.364252,-9.748919,4.092666,2.212686,-6.269459,4.608906,-4.706838,7.418299,-1.753094,-4.742637,9.419674,-8.280479,2.897286,0.179376,1.576307,8.414295,2.853907,7.077251,-0.123065,-7.522162,2.120574,-7.223879,8.850535,0.427888,-0.585239,-0.188690,2.039343,4.264773,2.765365,2.508042,1.056396,-4.776336,1.263643,2.845789,-9.399247,-8.085549,5.792926,4.595151,-8.583382,9.935053,9.956814,5.213607,-0.618525,2.612137,0.110600,-9.525155,5.844915,1.874254,-2.114697,5.180997,-2.245225,2.358247,-3.063563,8.008090,5.158047,3.726104,-2.107892,2.341659,9.454208,2.496305,7.684559,6.814493,-3.660307,6.931104,-0.328383,-1.653161,1.585589,-0.781996,-1.628805,-1.265611,-7.569815,-2.187658,-9.916578,2.884655,-2.743629,9.374562,-9.871984,9.350136,8.805365,-5.551901,2.446278,1.957914,-9.313084,-9.348631,7.941833,-7.726229,6.343284,-5.186006,-2.822009,3.878777,-7.024605,-2.540228,-9.628668,-7.893605,9.908528,0.430966,9.238654,9.739727,-2.276637,-6.497311,-2.287472,-8.518652,-3.914889,-1.990016,-3.313439,4.566098,-9.108132,-8.154982,0.272758,-1.051017,1.200889,8.400588,-9.160515,-1.283920,6.876001,-6.757423,9.733320,4.699451,-8.767245,-7.291829,7.361451,0.494396,3.416303,-2.038385,-9.120606,1.537978,-3.090424,-6.801938,1.454743,-5.922237,-7.394509,2.110101,2.234977,0.201991,-6.332301,-4.127577,8.765720,3.466490,8.376506,-8.534533,-2.251492,7.393875,-5.467118,-1.852375,-2.274833,-4.573958,2.898298,-7.253837,-1.328969,-2.297047,8.910978,8.761504,1.222555,-8.341182,-0.277727,-6.861092,-8.165952,-6.480835,-6.462869,4.204783,1.233142,9.373170,0.457536,0.816827,8.198695,-6.541862,-8.907626,2.179104,-4.341011,5.788752,-6.382657,5.633798,3.636299,-7.381510,-4.271551,0.111187,3.853893,4.078656,-8.578677,6.752795,-2.458901,6.127428,6.249273,-0.021353,-5.287600,-6.505336,-9.301737,0.349633,1.468159,5.724866,3.451619,3.050938,2.594047,7.782368,8.282532,2.013185,-2.194220,4.099684,7.766458,3.416882,2.379978,1.161196,-8.707848,6.926543,-6.934199,1.035099,8.866082,-3.468685,7.833440,2.700222,-7.852072,8.274449,8.689975,-4.065417,-2.050930,-2.256358,-7.527085,0.288237,-2.096292,-8.068741,7.754672,3.710598,5.505727,5.821744,3.598127,4.465319,9.178146,0.083946,5.129881,-3.442663,8.041062,4.972330,-5.672964,-7.932802,-6.662577,4.159171,1.549270,-6.741004,-4.307715,6.892582,-3.239740,-6.058381,0.534303,-7.386821,9.885404,6.388919,4.845784,-7.176186,4.888895,0.783295,-8.192676,-1.093474,9.587285,-0.411861,-3.969563,1.005356,-4.296967,6.586456,3.185882,4.511727,-0.689473,-6.871145,7.145165,1.093688,4.000802,-9.891136,8.192183,3.653069,-4.227028,-9.166554,-7.551519,7.831088,6.800911,-5.965323,7.791448,-0.917402,-7.910652,3.135628,3.744252,1.218353,3.573172,-4.460168,-6.154359,1.222270,8.413257,2.967482,-3.353059,5.562750,1.012414,-9.606692,8.836675,-8.629835,2.764834,2.866175,-5.269725,-3.583217,2.102796,-1.268366,-5.348185,-6.373431,-3.844529,5.706300,-5.404243,-3.229146,4.595298,-2.246991,1.910597,-6.005764,5.508355,-4.421154,-4.570128,5.475694,4.742692,7.411657,-8.962099,-3.178967,-3.468181,9.705003,-1.979206,-5.470009,-3.521060,-9.199124,-9.747395,8.731572,-0.918503,6.807278,-5.163560,-7.712907,6.719883,1.642995,0.831039,-5.970994,-1.956040,2.596394,3.372402,-6.010936,-7.909910,-4.787795,6.323240,-7.914715,2.169753,4.741768,0.372523,5.208060,7.213865,-8.294142,-9.086811,-6.646256,-2.450254,0.523966,-7.889707,6.365379,-4.421574,4.650519,7.351033,-5.545974,9.548355,-9.082250,1.026746,5.252914,6.350158,-0.841252,-2.782271,-4.922682,-1.633060,6.387512,5.187213,6.374363,-6.253083,8.076520,9.953641,-6.791882,7.176779,4.247702,-4.485252,-2.750453,-1.054290,-5.849073,4.615945,9.966348,-1.022856,-8.144701,8.400154,-8.163983,-4.911230,-3.126028,9.344223,3.867470,1.233250,3.167148,4.072688,1.995924,-0.690505,9.422757,-8.072246,6.560356,5.679747,-3.387135,-0.762370,-5.124457,2.147009,-7.614374,2.772040,2.616949,-3.401173,-2.853699,-2.824469,4.257638,9.542942,9.139929,7.176459,4.611715,-9.094764,0.185138,-2.247304,-0.985814,-3.636248,-8.681750,-8.005676,4.457836,-4.800908,-6.414088,6.666251,-7.688521,-8.607537,4.305252,-7.950148,-4.940514,-1.538435,3.997294,7.039004,-6.846678,-2.417791,9.130973], dtype = "float32")#candidate|12704|(960,)|const|float32
call_12703 = relay.TupleGetItem(func_9292_call(relay.reshape(const_12704.astype('float32'), [960,])), 1)
call_12705 = relay.TupleGetItem(func_9294_call(relay.reshape(const_12704.astype('float32'), [960,])), 1)
output = relay.Tuple([uop_12696,call_12701,call_12703,const_12704,])
output2 = relay.Tuple([uop_12696,call_12702,call_12705,const_12704,])
func_12744 = relay.Function([var_12673,var_12674,], output)
mod['func_12744'] = func_12744
mod = relay.transform.InferType()(mod)
mutated_mod['func_12744'] = func_12744
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12744_call = mutated_mod.get_global_var('func_12744')
var_12746 = relay.var("var_12746", dtype = "int64", shape = (12, 11, 9))#candidate|12746|(12, 11, 9)|var|int64
var_12747 = relay.var("var_12747", dtype = "int64", shape = (12, 11, 9))#candidate|12747|(12, 11, 9)|var|int64
call_12745 = func_12744_call(var_12746,var_12747,)
output = call_12745
func_12748 = relay.Function([var_12746,var_12747,], output)
mutated_mod['func_12748'] = func_12748
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10601_call = mod.get_global_var('func_10601')
func_10603_call = mutated_mod.get_global_var('func_10603')
call_12786 = func_10601_call()
call_12787 = func_10601_call()
output = call_12786
output2 = call_12787
func_12792 = relay.Function([], output)
mod['func_12792'] = func_12792
mod = relay.transform.InferType()(mod)
mutated_mod['func_12792'] = func_12792
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12792_call = mutated_mod.get_global_var('func_12792')
call_12793 = func_12792_call()
output = call_12793
func_12794 = relay.Function([], output)
mutated_mod['func_12794'] = func_12794
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9457_call = mod.get_global_var('func_9457')
func_9459_call = mutated_mod.get_global_var('func_9459')
call_12800 = relay.TupleGetItem(func_9457_call(), 0)
call_12801 = relay.TupleGetItem(func_9459_call(), 0)
func_7410_call = mod.get_global_var('func_7410')
func_7412_call = mutated_mod.get_global_var('func_7412')
call_12815 = relay.TupleGetItem(func_7410_call(), 0)
call_12816 = relay.TupleGetItem(func_7412_call(), 0)
output = relay.Tuple([call_12800,call_12815,])
output2 = relay.Tuple([call_12801,call_12816,])
func_12820 = relay.Function([], output)
mod['func_12820'] = func_12820
mod = relay.transform.InferType()(mod)
mutated_mod['func_12820'] = func_12820
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12820_call = mutated_mod.get_global_var('func_12820')
call_12821 = func_12820_call()
output = call_12821
func_12822 = relay.Function([], output)
mutated_mod['func_12822'] = func_12822
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3925_call = mod.get_global_var('func_3925')
func_3926_call = mutated_mod.get_global_var('func_3926')
call_12841 = relay.TupleGetItem(func_3925_call(), 0)
call_12842 = relay.TupleGetItem(func_3926_call(), 0)
func_2498_call = mod.get_global_var('func_2498')
func_2503_call = mutated_mod.get_global_var('func_2503')
var_12849 = relay.var("var_12849", dtype = "int8", shape = (8, 12))#candidate|12849|(8, 12)|var|int8
var_12850 = relay.var("var_12850", dtype = "int8", shape = (384,))#candidate|12850|(384,)|var|int8
call_12848 = relay.TupleGetItem(func_2498_call(relay.reshape(var_12849.astype('int8'), [6, 16, 1]), relay.reshape(var_12850.astype('int8'), [6, 16, 4]), relay.reshape(var_12850.astype('int8'), [6, 16, 4]), ), 2)
call_12851 = relay.TupleGetItem(func_2503_call(relay.reshape(var_12849.astype('int8'), [6, 16, 1]), relay.reshape(var_12850.astype('int8'), [6, 16, 4]), relay.reshape(var_12850.astype('int8'), [6, 16, 4]), ), 2)
func_3670_call = mod.get_global_var('func_3670')
func_3672_call = mutated_mod.get_global_var('func_3672')
call_12859 = relay.TupleGetItem(func_3670_call(), 0)
call_12860 = relay.TupleGetItem(func_3672_call(), 0)
output = relay.Tuple([call_12841,call_12848,var_12849,var_12850,call_12859,])
output2 = relay.Tuple([call_12842,call_12851,var_12849,var_12850,call_12860,])
func_12867 = relay.Function([var_12849,var_12850,], output)
mod['func_12867'] = func_12867
mod = relay.transform.InferType()(mod)
mutated_mod['func_12867'] = func_12867
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12867_call = mutated_mod.get_global_var('func_12867')
var_12869 = relay.var("var_12869", dtype = "int8", shape = (8, 12))#candidate|12869|(8, 12)|var|int8
var_12870 = relay.var("var_12870", dtype = "int8", shape = (384,))#candidate|12870|(384,)|var|int8
call_12868 = func_12867_call(var_12869,var_12870,)
output = call_12868
func_12871 = relay.Function([var_12869,var_12870,], output)
mutated_mod['func_12871'] = func_12871
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10292_call = mod.get_global_var('func_10292')
func_10294_call = mutated_mod.get_global_var('func_10294')
call_12878 = func_10292_call()
call_12879 = func_10292_call()
func_7971_call = mod.get_global_var('func_7971')
func_7973_call = mutated_mod.get_global_var('func_7973')
call_12881 = relay.TupleGetItem(func_7971_call(), 0)
call_12882 = relay.TupleGetItem(func_7973_call(), 0)
var_12887 = relay.var("var_12887", dtype = "int64", shape = (5, 10, 8))#candidate|12887|(5, 10, 8)|var|int64
bop_12888 = relay.left_shift(call_12878.astype('uint16'), var_12887.astype('uint16')) # shape=(5, 10, 8)
bop_12891 = relay.left_shift(call_12879.astype('uint16'), var_12887.astype('uint16')) # shape=(5, 10, 8)
output = relay.Tuple([call_12881,bop_12888,])
output2 = relay.Tuple([call_12882,bop_12891,])
func_12899 = relay.Function([var_12887,], output)
mod['func_12899'] = func_12899
mod = relay.transform.InferType()(mod)
var_12900 = relay.var("var_12900", dtype = "int64", shape = (5, 10, 8))#candidate|12900|(5, 10, 8)|var|int64
output = func_12899(var_12900)
func_12901 = relay.Function([var_12900], output)
mutated_mod['func_12901'] = func_12901
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6352_call = mod.get_global_var('func_6352')
func_6353_call = mutated_mod.get_global_var('func_6353')
call_12966 = relay.TupleGetItem(func_6352_call(), 3)
call_12967 = relay.TupleGetItem(func_6353_call(), 3)
func_6352_call = mod.get_global_var('func_6352')
func_6353_call = mutated_mod.get_global_var('func_6353')
call_12968 = relay.TupleGetItem(func_6352_call(), 1)
call_12969 = relay.TupleGetItem(func_6353_call(), 1)
output = relay.Tuple([call_12966,call_12968,])
output2 = relay.Tuple([call_12967,call_12969,])
func_12983 = relay.Function([], output)
mod['func_12983'] = func_12983
mod = relay.transform.InferType()(mod)
mutated_mod['func_12983'] = func_12983
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12983_call = mutated_mod.get_global_var('func_12983')
call_12984 = func_12983_call()
output = call_12984
func_12985 = relay.Function([], output)
mutated_mod['func_12985'] = func_12985
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12986 = relay.var("var_12986", dtype = "float32", shape = (11, 1, 12))#candidate|12986|(11, 1, 12)|var|float32
uop_12987 = relay.acosh(var_12986.astype('float32')) # shape=(11, 1, 12)
bop_12989 = relay.divide(uop_12987.astype('float32'), relay.reshape(var_12986.astype('float32'), relay.shape_of(uop_12987))) # shape=(11, 1, 12)
func_10137_call = mod.get_global_var('func_10137')
func_10141_call = mutated_mod.get_global_var('func_10141')
const_13007 = relay.const([False,True,False,False,True,False,True,False,False,True,True,False,False,True,True,True,True,True,True,False,False,True,False,True,True,False,True,True,True,True,False,False,False,False,False,True,False,True,False,True,True,True,True,True,False,False,False,False,True,False,False,True,True,True,False,False,True,True,True,False,True,True,False,True,True,True,True,False,False,True,True,True,False,False,True,False,False,True,False,True,True,True,False,False,False,False,False,True,False,False,True,True,True,False,False,True,True,True,True,True,False,False,True,False,False,False,True,False,True,True,True,True,False,True,True,False,True,False,True,True,False,True,False,True,True,True,False,False,False,True,True,True,True,False,True,True,False,False,True,False,False,False,True,False,True,False,True,True,False,False,False,False,True,True,False,False,False,False,False,False,False,False,True,True,False,True,True,True,True,False,True,True,True,False,False,False,False,True,True,True,True,False,True,True,True,True,True,True,False,False,True,False,False,True,True,False,False,False,True,True,True,False,True,False,False,True,False,True,False,False,False,True,False,True,False,True,True,False,False,True,False,True,True,False,False,False,False,False,True,False,False,False,False,True,False,True,False,False,False,False,False,False,True,False,True,False,True,False,False,True,True,False,True,False,False,True,True,False,False,False,False,False,False,True,True,False,False,True,False,False,True,True,False,False,True,True,False,True,False,False,False,True,False,True,False,False,True,True,True,True,True,True,True,True,False,False,True,False,True,True,False,False,False,False,False,False,False,True,True,False,True,True,True,False,True,True,False,False,False,True,True,True,True,False,False,True,False,True,False,True,True,False,True,True,True,True,True,True,False,False,True,False,False,False,False,True,False,False,True,False,False,False,False,True,False,False,False,False,False,False,True,True,True,False,False,False,True,False,True,False,False,False,False,False,False,False,True,False,False,False,True,False,False,True,True,False,True,False,False,True,False,True,False,True,True,True,True,True,True,False,True,True,False,True,False,True,True,True,True,True,False,False,False,False,True,True,True,True,True,True,False,False,True,True,True,False,False,True,True,True,True,False,False,False,True,False,True,False,False,False,False,False,True,False,False,False,True,True,True,True,True,False,True,False,True,False,False,True,True,False,False,True,False,False,True,False,True,False,False,True,False,False,True,True,False,True,False,False,True,True,True,False,True,False,False,False,False,False,True,False,False,True,True,True,False,False,True,True,False,True,False,False,False,True,False,False,False,False,False,True,True,True,True,True,True,True,True,False,False,True,False,False,False,True,True,False,True,False,True,True,False,True,True,False,False,True,False,True,True,True,False,True,False,False,False,False,True,True,False,True,False,False,False,True,True,True,True,False,False,True,True,False,False,False,False,True,False,False,False,True,True,False,False,False,False,False,False,False,False,False,True,False,False,True,True,True,True,True,True,True,False,False,True,False,False,True,True,False,True,True,False,True,False,False,True,False,True,True,False,True,True,False,True,True,True,True,False,False,False,True,True,False,True,False,False,True,True,False,False,True,True,False,False,True,False,True,False,True,False,False,False,True,False,False,False,False,True,False,False,True,True,False,True,False,False,True,True,False,True,True,True,True,True,True,False,False,False,False,True,False,True,False,True,True,False,True,True,True,True,False,False,False,False,True,False,False,False,True,False,False,True,True,True,False,False,True,False,False,False,False,False,True,False,True,False,False,False,False,True,True,False,True,True,False,False,True,False,False,True,True,False,False,False,True,False,True,True,True,True,True,True,False,False,True,True,False,True,False,False,False,True,False,True,True,False,True,False,True,True,True,False,False,True,False,True,False,True,False,True,True,True,False,True,True,True,False,False,False,False,False,False,False,True,True,True,True,False,True,False,True,True,False,True,False,True,True,False,False,True,True,True,True,True,False,False,False,True,False,False,True,True,False,True,False,True,False,True,True,False,False,True,True,False,False,True,True,True,False,False,True,True,True,False,True,False,False,True,True,True,False,False,False,False,False,False,False,False,True,True,False,True,False,True,False,True,True,True,False,True,True,True,False,True,True,True,True,False,True,False,True,True,False,True,True,False,True,True,True,False,True,True,False,True,True,False,False,False,True,True,True,True,False,True,False,False,True,True,False,False,True,True,True,True,False,False,False,True,False,True,True], dtype = "bool")#candidate|13007|(900,)|const|bool
var_13008 = relay.var("var_13008", dtype = "float64", shape = (16,))#candidate|13008|(16,)|var|float64
call_13006 = relay.TupleGetItem(func_10137_call(relay.reshape(const_13007.astype('bool'), [900,]), relay.reshape(var_13008.astype('float64'), [16,]), ), 3)
call_13009 = relay.TupleGetItem(func_10141_call(relay.reshape(const_13007.astype('bool'), [900,]), relay.reshape(var_13008.astype('float64'), [16,]), ), 3)
bop_13024 = relay.not_equal(var_12986.astype('bool'), relay.reshape(uop_12987.astype('bool'), relay.shape_of(var_12986))) # shape=(11, 1, 12)
output = relay.Tuple([bop_12989,call_13006,const_13007,var_13008,bop_13024,])
output2 = relay.Tuple([bop_12989,call_13009,const_13007,var_13008,bop_13024,])
func_13029 = relay.Function([var_12986,var_13008,], output)
mod['func_13029'] = func_13029
mod = relay.transform.InferType()(mod)
mutated_mod['func_13029'] = func_13029
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13029_call = mutated_mod.get_global_var('func_13029')
var_13031 = relay.var("var_13031", dtype = "float32", shape = (11, 1, 12))#candidate|13031|(11, 1, 12)|var|float32
var_13032 = relay.var("var_13032", dtype = "float64", shape = (16,))#candidate|13032|(16,)|var|float64
call_13030 = func_13029_call(var_13031,var_13032,)
output = call_13030
func_13033 = relay.Function([var_13031,var_13032,], output)
mutated_mod['func_13033'] = func_13033
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7990_call = mod.get_global_var('func_7990')
func_7992_call = mutated_mod.get_global_var('func_7992')
call_13172 = func_7990_call()
call_13173 = func_7990_call()
func_7100_call = mod.get_global_var('func_7100')
func_7103_call = mutated_mod.get_global_var('func_7103')
const_13185 = relay.const([[2,3,7,-2,3,-10,7,-2,7,2,-5,9,-3,6,8,-8,-9,6,2,-4,4,-6,8,-1,-1,9,5,4,7,-8,7,7,-8,3,-1,-5,-10,7,2,-5,10,-9,-1,6,2,-5,1,-6,-5,1],[5,-2,-8,5,6,2,-3,2,3,-4,-2,-5,-10,-4,-9,10,10,1,10,9,-7,3,-2,-5,-3,-4,-9,7,-2,-4,-5,-7,6,-6,-7,4,6,5,2,-4,1,9,-7,-9,9,-9,8,1,5,4],[-2,7,6,5,4,-5,7,6,10,10,1,-4,-7,-6,-4,-6,9,-6,5,-4,-1,5,3,-2,9,2,3,-10,3,-3,-4,-3,2,7,1,8,10,-1,-7,6,5,5,-4,-8,-10,-3,-2,9,-8,-1],[10,2,-3,3,-6,-5,8,10,-6,8,9,-2,2,5,8,8,7,9,4,9,2,-4,-5,-2,-3,7,-6,5,10,5,-7,-7,-4,4,10,-10,9,-5,-10,-7,9,-7,5,-2,-3,5,1,-6,-10,-5],[-8,-5,10,-3,-6,3,4,-10,-5,4,-1,-10,2,-9,10,3,10,-7,7,-3,10,-8,-10,-3,-3,3,-9,6,10,-4,-9,10,-6,-2,-7,-5,2,3,-2,-7,5,-8,-2,6,8,-4,-8,6,3,6],[-4,-7,4,10,-6,10,-6,8,1,-10,3,-7,8,4,5,1,10,-8,10,10,-7,-9,-9,9,-10,-2,-2,-1,-4,2,-4,-9,-3,-9,-6,-10,9,6,-8,-9,-3,-9,-10,5,-7,1,2,-8,-8,-9],[-5,-7,-8,-4,7,5,4,7,8,8,-1,-7,-3,-9,1,5,-6,-10,-5,-3,8,6,-3,8,5,7,8,-2,-10,-10,-8,8,-7,-8,-3,-7,-8,4,6,-5,7,10,7,-4,2,9,-9,1,5,10],[-2,-8,-2,4,-4,10,10,-7,-9,-3,7,10,-8,3,2,-1,4,7,-4,5,-9,-7,4,-5,5,5,-1,-7,8,2,5,6,-5,-5,-3,4,5,10,-5,2,4,-3,4,4,2,-2,9,6,1,10],[-2,-6,8,-6,-3,-7,8,2,10,4,1,-8,-3,4,-6,8,1,-4,-1,3,1,-1,-10,2,8,-1,-9,-9,3,-8,2,-6,-1,-3,3,8,-8,4,3,-5,2,-2,-4,5,6,6,-9,-10,-3,7],[-9,-1,-6,-4,-2,2,6,5,4,-9,1,-8,-10,-3,1,10,-4,8,7,-1,-10,3,6,10,-7,-2,-4,1,9,6,5,-2,8,-1,2,2,-6,10,2,-3,8,-7,6,-6,-3,4,10,-5,4,3],[-7,-9,-1,-6,-10,-2,-4,1,-7,4,-3,6,-4,2,-8,-5,-2,-9,-5,6,3,2,-6,-9,3,-3,-2,10,1,-6,-8,7,7,-3,-2,-6,6,4,2,-5,7,-9,-6,-6,2,-7,3,10,-1,-10],[3,-7,5,-1,3,10,-1,-8,10,5,4,-2,-5,8,-9,-8,-6,3,4,-8,7,4,9,-6,-6,2,-2,-10,1,4,6,-2,7,-4,9,-8,10,-6,-6,9,-3,1,-7,6,-8,-8,2,-9,-5,-10],[6,1,-9,-6,-9,-4,-8,-2,7,3,-8,-2,-10,9,-3,-10,-6,7,-7,-10,-10,1,-1,-4,-10,-6,9,9,10,-7,-9,-3,9,10,-1,-4,-5,10,9,8,3,8,-3,-3,6,-5,-10,-10,6,-7],[-2,-9,-8,-5,-3,8,9,9,-4,-5,4,-5,-10,-3,7,-5,-1,-6,-5,5,7,5,-9,8,-7,-2,-4,-5,-4,-1,8,-9,-4,5,-9,-9,-4,-2,1,4,2,-2,5,-3,8,1,1,3,9,7],[10,4,-4,-7,-6,-6,-9,7,6,6,-3,9,8,-3,2,5,-8,6,-3,9,-5,10,-3,-1,-6,-4,3,6,5,-8,-9,-1,-10,-1,1,6,6,2,-2,10,-2,-8,-8,-6,-4,-2,-7,-10,-1,2],[10,9,-4,5,6,6,2,2,-10,6,3,9,-2,-9,-9,-4,10,6,4,10,1,-7,9,4,8,-5,10,4,-2,-5,-3,3,2,-7,-3,8,4,6,7,-5,9,-9,-4,1,4,-9,4,-2,1,7],[-8,-7,-2,-6,-2,5,10,2,-5,-10,-8,-7,8,1,1,-3,-4,-1,-3,7,-7,9,-6,-1,-2,9,-7,4,-8,-5,4,-7,-8,9,5,-7,8,-2,-6,5,-4,-10,1,-6,-1,-7,1,-5,2,10],[-10,2,2,-2,6,8,2,-3,-2,-1,2,-7,-3,1,8,5,-10,-6,2,3,-7,-10,-9,-1,1,-3,1,-5,-4,-10,-10,10,3,-2,-8,-4,6,-2,-6,5,5,10,9,10,6,8,8,-7,6,7]], dtype = "int8")#candidate|13185|(18, 50)|const|int8
var_13186 = relay.var("var_13186", dtype = "float32", shape = (1260,))#candidate|13186|(1260,)|var|float32
call_13184 = relay.TupleGetItem(func_7100_call(relay.reshape(const_13185.astype('int8'), [9, 100]), relay.reshape(var_13186.astype('float32'), [14, 9, 10]), ), 2)
call_13187 = relay.TupleGetItem(func_7103_call(relay.reshape(const_13185.astype('int8'), [9, 100]), relay.reshape(var_13186.astype('float32'), [14, 9, 10]), ), 2)
var_13198 = relay.var("var_13198", dtype = "int8", shape = (18, 50))#candidate|13198|(18, 50)|var|int8
bop_13199 = relay.bitwise_xor(const_13185.astype('int8'), relay.reshape(var_13198.astype('int8'), relay.shape_of(const_13185))) # shape=(18, 50)
func_6258_call = mod.get_global_var('func_6258')
func_6261_call = mutated_mod.get_global_var('func_6261')
const_13203 = relay.const([-3.674885,4.708219,3.324474,2.158209,-5.866303,-3.090097,4.933395,2.020674,-7.427636,2.151747,3.722896,5.672481,-8.502281,0.524353,2.733679,9.646910,-5.412067,8.101516,6.738806,8.546315,-8.336166,-9.789017,-0.550260,0.749419,-7.814543,7.168920,4.490823,2.662496,1.297210,9.618962,-3.582325,-9.525193,5.157454,-1.306676,-7.984765,-1.514405,2.141964,-0.863777,-5.502070,5.970294,2.358882,-0.874797,8.874374,-3.540623,-0.941416,-4.880098,2.484714,5.661823,-9.616331,7.503756,9.789686,3.180177,-8.407660,1.902717,-6.644765,-5.716861,8.891644,-9.233740,-6.505149,7.137032,-3.055504,-3.428001,-5.748361,-0.173542,3.888327,-1.737437,2.014297,-3.881865,8.873953,-3.461308,-7.237695,6.278146,-9.741688,-8.679392,8.066565,9.718148,0.730841,2.150925,-9.243887,2.759457,9.734736,-9.763516,8.283312,2.608626,-3.114364,-9.297816,-9.163622,5.678588,4.124790,6.351754,9.533771,-3.506028,-2.697715,6.337221,2.750057,8.152800,-0.343903,7.877076,-9.671087,-9.795780,9.825685,3.785626,2.548670,-4.334477,-2.791533,8.556351,-4.404193,2.499053,4.340226,1.322256,3.878470,7.755587,2.152267,9.454736,2.430076,-5.198975,9.628512,-9.597081,-5.529691,8.855087,3.275688,4.700801,5.330674,-5.769716,9.967161,7.164382,-9.983215,-5.484795,-2.741661,1.346157,2.724645,-5.717005,9.243754,4.837217,4.057579,6.623589,9.944737,-6.614820,5.504625,2.040779,6.660785,6.857295,-1.598425,1.313673,0.713248,-7.203118,-7.072104,3.889203,-2.183991,-4.377472,-8.761914,-7.923201,-5.127022,-4.356684,4.250440,-4.339309,-3.288641,6.742980,5.199374,9.701371,5.807631,7.853216,-0.870874,-2.732228,-7.805501,-7.931793,-7.688141,-0.192059,-1.650972,-4.738992,1.260668,-1.212933,-5.409109,-4.661185,-7.505780,-1.185030,9.532999,6.598121,9.508575,-6.746307,-9.178003,-7.874381,5.582092,0.489075,8.101932,-3.557807,-2.461154,-1.209061,-7.531392,-4.525705,5.900568,-8.232417], dtype = "float32")#candidate|13203|(192,)|const|float32
call_13202 = relay.TupleGetItem(func_6258_call(relay.reshape(const_13203.astype('float32'), [192,])), 1)
call_13204 = relay.TupleGetItem(func_6261_call(relay.reshape(const_13203.astype('float32'), [192,])), 1)
uop_13213 = relay.cos(bop_13199.astype('float64')) # shape=(18, 50)
uop_13218 = relay.tan(uop_13213.astype('float32')) # shape=(18, 50)
output = relay.Tuple([call_13172,call_13184,var_13186,call_13202,const_13203,uop_13218,])
output2 = relay.Tuple([call_13173,call_13187,var_13186,call_13204,const_13203,uop_13218,])
func_13233 = relay.Function([var_13186,var_13198,], output)
mod['func_13233'] = func_13233
mod = relay.transform.InferType()(mod)
mutated_mod['func_13233'] = func_13233
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13233_call = mutated_mod.get_global_var('func_13233')
var_13235 = relay.var("var_13235", dtype = "float32", shape = (1260,))#candidate|13235|(1260,)|var|float32
var_13236 = relay.var("var_13236", dtype = "int8", shape = (18, 50))#candidate|13236|(18, 50)|var|int8
call_13234 = func_13233_call(var_13235,var_13236,)
output = call_13234
func_13237 = relay.Function([var_13235,var_13236,], output)
mutated_mod['func_13237'] = func_13237
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12397_call = mod.get_global_var('func_12397')
func_12398_call = mutated_mod.get_global_var('func_12398')
call_13327 = relay.TupleGetItem(func_12397_call(), 0)
call_13328 = relay.TupleGetItem(func_12398_call(), 0)
output = relay.Tuple([call_13327,])
output2 = relay.Tuple([call_13328,])
func_13338 = relay.Function([], output)
mod['func_13338'] = func_13338
mod = relay.transform.InferType()(mod)
mutated_mod['func_13338'] = func_13338
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13338_call = mutated_mod.get_global_var('func_13338')
call_13339 = func_13338_call()
output = call_13339
func_13340 = relay.Function([], output)
mutated_mod['func_13340'] = func_13340
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3650_call = mod.get_global_var('func_3650')
func_3651_call = mutated_mod.get_global_var('func_3651')
call_13347 = relay.TupleGetItem(func_3650_call(), 0)
call_13348 = relay.TupleGetItem(func_3651_call(), 0)
output = call_13347
output2 = call_13348
func_13350 = relay.Function([], output)
mod['func_13350'] = func_13350
mod = relay.transform.InferType()(mod)
output = func_13350()
func_13351 = relay.Function([], output)
mutated_mod['func_13351'] = func_13351
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11660_call = mod.get_global_var('func_11660')
func_11662_call = mutated_mod.get_global_var('func_11662')
call_13360 = relay.TupleGetItem(func_11660_call(), 0)
call_13361 = relay.TupleGetItem(func_11662_call(), 0)
output = call_13360
output2 = call_13361
func_13388 = relay.Function([], output)
mod['func_13388'] = func_13388
mod = relay.transform.InferType()(mod)
output = func_13388()
func_13389 = relay.Function([], output)
mutated_mod['func_13389'] = func_13389
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9642_call = mod.get_global_var('func_9642')
func_9644_call = mutated_mod.get_global_var('func_9644')
call_13427 = relay.TupleGetItem(func_9642_call(), 1)
call_13428 = relay.TupleGetItem(func_9644_call(), 1)
output = call_13427
output2 = call_13428
func_13437 = relay.Function([], output)
mod['func_13437'] = func_13437
mod = relay.transform.InferType()(mod)
mutated_mod['func_13437'] = func_13437
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13437_call = mutated_mod.get_global_var('func_13437')
call_13438 = func_13437_call()
output = call_13438
func_13439 = relay.Function([], output)
mutated_mod['func_13439'] = func_13439
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5634_call = mod.get_global_var('func_5634')
func_5635_call = mutated_mod.get_global_var('func_5635')
call_13471 = relay.TupleGetItem(func_5634_call(), 0)
call_13472 = relay.TupleGetItem(func_5635_call(), 0)
output = call_13471
output2 = call_13472
func_13473 = relay.Function([], output)
mod['func_13473'] = func_13473
mod = relay.transform.InferType()(mod)
mutated_mod['func_13473'] = func_13473
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13473_call = mutated_mod.get_global_var('func_13473')
call_13474 = func_13473_call()
output = call_13474
func_13475 = relay.Function([], output)
mutated_mod['func_13475'] = func_13475
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12090_call = mod.get_global_var('func_12090')
func_12091_call = mutated_mod.get_global_var('func_12091')
call_13497 = relay.TupleGetItem(func_12090_call(), 0)
call_13498 = relay.TupleGetItem(func_12091_call(), 0)
func_4785_call = mod.get_global_var('func_4785')
func_4787_call = mutated_mod.get_global_var('func_4787')
call_13504 = func_4785_call()
call_13505 = func_4785_call()
output = relay.Tuple([call_13497,call_13504,])
output2 = relay.Tuple([call_13498,call_13505,])
func_13514 = relay.Function([], output)
mod['func_13514'] = func_13514
mod = relay.transform.InferType()(mod)
output = func_13514()
func_13515 = relay.Function([], output)
mutated_mod['func_13515'] = func_13515
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12330_call = mod.get_global_var('func_12330')
func_12332_call = mutated_mod.get_global_var('func_12332')
call_13576 = func_12330_call()
call_13577 = func_12330_call()
output = call_13576
output2 = call_13577
func_13578 = relay.Function([], output)
mod['func_13578'] = func_13578
mod = relay.transform.InferType()(mod)
output = func_13578()
func_13579 = relay.Function([], output)
mutated_mod['func_13579'] = func_13579
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6123_call = mod.get_global_var('func_6123')
func_6125_call = mutated_mod.get_global_var('func_6125')
call_13585 = relay.TupleGetItem(func_6123_call(), 1)
call_13586 = relay.TupleGetItem(func_6125_call(), 1)
output = call_13585
output2 = call_13586
func_13610 = relay.Function([], output)
mod['func_13610'] = func_13610
mod = relay.transform.InferType()(mod)
output = func_13610()
func_13611 = relay.Function([], output)
mutated_mod['func_13611'] = func_13611
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12229_call = mod.get_global_var('func_12229')
func_12231_call = mutated_mod.get_global_var('func_12231')
call_13620 = func_12229_call()
call_13621 = func_12229_call()
output = relay.Tuple([call_13620,])
output2 = relay.Tuple([call_13621,])
func_13625 = relay.Function([], output)
mod['func_13625'] = func_13625
mod = relay.transform.InferType()(mod)
mutated_mod['func_13625'] = func_13625
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13625_call = mutated_mod.get_global_var('func_13625')
call_13626 = func_13625_call()
output = call_13626
func_13627 = relay.Function([], output)
mutated_mod['func_13627'] = func_13627
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8355_call = mod.get_global_var('func_8355')
func_8356_call = mutated_mod.get_global_var('func_8356')
call_13630 = relay.TupleGetItem(func_8355_call(), 1)
call_13631 = relay.TupleGetItem(func_8356_call(), 1)
func_7659_call = mod.get_global_var('func_7659')
func_7664_call = mutated_mod.get_global_var('func_7664')
const_13652 = relay.const([-10,-5,-10,7,-2,-9,5,-5,6,2,-5,6,9,-3,10,8,5,-1,2,2,-4,10,-4,2,-8,-1,-5,7,6,-2,-4,-6,-4,3,-7,-10,9,-10,-7,-5,7,10,-3,-5,-6,5,9,-8,-8,-1,-7,6,4,-1,8,-6,1,8,-2,3,2,-6,7,6,-9,10,1,-4,-2,6,10,-5,-9,-5,6,6,3,-8,10,-8,4,-4,4,8,2,5,7,5,5,-4,7,8,4,2,4,2,8,1,-6,1,4,-2,-8,-6,6,-3,-1,-2,-8,10,6,10,-10,7,1,-3,-6,7,-1,-6,-2,-1,9,-10,2,1,-4,2,-1,9,9,-6,-9,6,7,-9,10,-3,-5,-7,5,-5,-8,-2,-5,8,2,-6,8,-1,5,-3,-1,-5,-1,3,2,-2,4,7,4,-3,3,7,3,-8,9,-5,-10,-7,7,-5,-8,1,-3,-1,-6,-3,-6,-2,-10,9,-2,10,-9,10,-6,6,4,-8,-6,1,-3,-2,-7,-8,-5,-6,3,6,10,-9,3,-2,3,-5,9,4,2,-1,-2,-6,7,-3,-6,2,9,4,-7,10,-6,-8,10,-9,7,1,-10,-8,9,-7,10,-10,-1,10,3,-7,-6,-8,-6,-9,8,4,-7,4,4,8,1,5,-6,-1,7,-8,2,9,2,2,-8,-7,-1,-8,4,-8,-7,8,-8,-2,4,9,-7,-3,6,8,-4,-8,8,9,-5,-7,-10,6,4,6,-10,-6,-3,6,6,5,1,-6,-1,-10,-2,9,-4,3,-6,7,-3,-3,-6,8,-4,-4,6,5,5,-4,-2,10,-9,-3,-1,1,7,-2,4,5,-3,-3,2,-6,3,5,-2,-1,-7,8,-9,4,2,7,8,-3,4,9,4,-3,5,2,3,8,10,-2,6,2,-1,-5,-4,9,-4,6,-4,-3,-6,-6,-8,3,-2,-6,-8,-6,9,10,-10,1,-9,-2,-5,2,1,4,-2,-7,9,-5,-2,-8,4,4,8,8,4,10,4,-5,-2,4,4,-10,-7,-2,8,1,9,-4,5,-6,-1,-2,-10,7,6,8,5,4,5,-2,-3,2,10,-1,-9,6,5,2,5,-9,-3,2,7,9,-10,-2,3,9,2,-8,6,1,-4,-9,4,-1,-5,6,-8,3,-5,-5,10,4,1,-3,8,10,-6,-2,-7,9,7,-3,10,5,10,6,1,2,-3,-2,-8,2,1,6,8,-9,1,-8,-9,-8,2,-9,-3,-6,7,-7,10,10,-5,9,-2,-6,2,3,8,2,-5,-4,1,7,8,4,-5,-9,-1,-4,9,-5,8,4,-9,-8,7,-7,4,8,-1,-1,-7,9,-1,8,-4,2,-10,8,3,8,-7,-10,-10,-4,1,7,6,-3,-10,-6,5,-8,6,-4,1,-1,-8,1,1,9,1,-1,4,3,-8,-10,-8,-6,2,5,4,6,-1,10,-2,-6,-6,9,3,-6,10,-2,4,-3,1,-2,8,-9,-4,-10,9,-7,-5,7,-8,-10,8,-7,1,-9,-1,-9,8,7,6,-8,5,10,-2,9,1,-8,-1,-1,8,7,2,8,4,2,1,3,-7,-6,-1,1,-4,10,6,10,-1,3,4,5,-5,8,-9,3,-7,5,6,1,-6,5,-2,8,-5,9,2,-1,-1,6,1,5,10,5,5,6,-7,-3,-10,-6,-2,6,1,3,-6,1,8,-5,-6,-4,8,-4,3,-6,8,9,9,4,-3,-1], dtype = "uint64")#candidate|13652|(660,)|const|uint64
const_13653 = relay.const([[8.164979,2.155627,-4.501503,-4.465688,-5.655754,1.117810,-5.157522,2.397416,-0.710879,5.214297,1.321401,-6.284804,4.229898,-9.255742,9.932830,9.958900,-7.888761,8.939543,8.268799,-3.837979,7.279671,-5.599951,-8.238376,3.285154,2.892178,-0.208866,2.947127,-3.060973,-1.357133,-3.521769,-8.607274,6.871420,-8.497866,4.091842,-1.193058,2.893256,7.609209,9.557125,-3.635840,-5.789231,-6.197990,-9.801206,6.533412,-6.561816,0.755333,2.630447,-1.318444,-4.163248,-8.657584,2.193813,-6.140013,-7.083381,-5.887050,9.192396,1.044792,1.793488,9.643658,3.170669,-6.246149,-7.949285,-9.630310,2.818014,-7.071527,-3.706185,0.192264,-6.849309,-4.973380,8.774212,-8.431676,3.424548,2.435213,2.540845,-2.600909,5.954885,6.017717,-6.395435,-2.105728,-7.891288,-9.291858,8.218467,-2.139041,8.849672,-8.212715,-2.355137,2.505835,-6.823318,-3.614166,5.828918,-1.642618,8.639868,0.627096,-1.058283,2.405577,-6.109229,5.436676,0.007026,2.145986,-0.444872,7.501210,9.886378,3.101206,0.490021,6.685308,-2.508277,-0.050839,6.419279,-2.835730,1.894404,4.953314,9.010157,3.855480,-3.840163,9.174844,-7.647845,4.195232,0.321457,-9.636500,-0.236453,-9.322129,1.230572,-4.245940,-8.708306,-4.011432,-7.131234,0.943671,-8.167519,-0.609094,-2.728268,-9.562211,5.928302,-6.947205,-7.553577,0.759957,-6.325816,4.688892,-2.235773,1.873246,-4.918983,-8.510764,7.845210,-8.310336,-4.737470,-7.752353,-0.483243,-6.643843,2.048207,9.164694,0.263742,-0.748518,-3.364020,4.231441,-0.161931,1.003168,1.996171,0.734082,7.149740,-8.030744,6.291612,-0.626652,4.229390,8.974533,7.948051,-7.397565,5.633596,5.063613,6.239032,0.724357,1.298118,-0.968155,-8.046326,7.644919,-2.167079,-0.745960,-3.906410,2.822228,9.831377,-7.802821,2.179876,0.293513,-9.119824,-4.511888,3.950814,3.347892,-7.417351,0.014403,5.031067,4.060942,9.170132,8.249011,-9.087517,4.931610,3.677080,2.635721,0.870833,-6.775369,9.837029,8.792213,-6.935556,4.974594,-7.083192,9.253392,2.841342,6.488421,-5.302412,-0.361247,-5.185560,-7.511277,-4.800939,-9.489425,-6.950360,0.459203,-1.432120,1.546441,5.631197,9.293408,1.772691,2.140441,5.621653,6.917325,-5.226118,1.867826,-8.191977,-4.187915,0.408280,-5.838327,2.826731,5.948564,-0.308322,-9.871785,0.262868,5.527738,2.090642,3.209079,-5.953846,-8.252573,-3.569715,8.605534,-3.539735,5.032360,-5.972123,0.633520,9.727077,2.132037,8.314936,5.960085,-1.005803,-2.454277,-1.985747,-3.329971,-2.200530,2.011859,-7.125818,9.548182,-0.466109,-3.381229,-3.097895,8.288088,-6.023992,8.261676,-6.537477,-4.289775,-3.573329,-2.872355,-6.835090,2.632809,-4.212862,-2.885592,4.672686,0.027269,-8.709525,-1.236471,6.839164,6.891760,0.375719,-8.312622,5.403776,-6.068147,9.372262,-2.297663,2.495820,-2.814789,-4.826332,5.893579,8.269839,-9.050637,-3.991944,-9.716837,-6.322251,-3.803628,5.690399,9.656417,8.908496,-8.061074,9.533813,1.233269,-8.862481,-2.440302,-9.846356,-8.447682,-5.444589,8.505730,3.627365,-4.166619,6.322806,5.221652,9.906546,-1.729758,-0.077722,3.178554,6.359833,1.761152,4.123287,0.326467,0.564129,3.919473,-5.114104,-6.358360,-6.824153,0.052292,1.083867,-3.368409,4.963273,-3.761321,7.819069,8.903028,-3.173847,-4.553339,-7.210574,7.070443,1.021600,0.028625,4.392446,-4.205353,2.116522,-6.192810,-9.992425,5.904477,4.503281,-3.550542,-1.528054,4.567792,-8.882627,-2.264904,9.921275,-3.880181,-7.397647,-6.064024,8.055724,1.591546,-3.199265,-2.147956,6.971147,0.432930,1.106728,7.903407,8.767182,-3.899991,4.100386,2.225153,-7.958095,5.029423,5.468418,-9.986515,-9.893612,1.044929,0.549720,-7.473460,-5.708688,3.554164,6.124064,2.977638,-5.887869,-5.703190,-6.844557,-0.954916,5.040402,8.797533,-0.391192,7.281536,7.239478,2.688836,-0.114794,2.635787,1.741567,-3.814505,-5.995397,-2.642599,3.287416,-4.144860,-7.359157,-7.635304,-6.597356,-8.658723,-1.196309,-1.349721,8.327502,-5.586394,0.864501,-0.993962,8.558854,3.923666,-6.042470,-5.845849,-9.814856,8.653974,2.675235,-3.030283,2.923366,-2.380502,-0.097449,0.020564,3.900381,-4.024554,-3.587551,9.886590,5.616423,5.245055,-7.748128,-0.477070,-2.338516,9.633616,0.213746,5.892916,2.593649,-3.442104,-1.909797,1.525515,-6.426425,-1.917758,-2.972484,-0.783041,-8.244452,3.044664,3.861180,4.469585,7.992433,5.219345,-5.371215,0.038151,2.757849,-0.770345,4.909617,2.986496,3.224478,-9.878111,3.692753,6.537836,-9.588699,5.204450,-4.954745,8.175707,5.870119,8.932939,-6.262001,4.267399,-6.228199,5.652448,6.948710,7.637310,1.814664,-6.422217,-7.777093,-8.745024,-3.312425,-2.747565,8.609447,-9.627462,1.373707,-1.736558,-8.391491,5.289106,0.796284,0.241378,3.755520,9.167076,-6.286230,9.086734,-7.765156,-7.957861,2.811427,1.707820,-7.585205,-2.247860,0.143162,1.144966,-1.969935,1.872362,-3.508819,9.291786,5.420417,-3.052546,-1.223212,9.096536,0.018205,-5.574166,-8.297015,0.218707,5.922061,-1.433450,0.311822,9.638003,-9.963806,0.713683,3.615118,-2.385081,-3.149341,-7.060177,1.216572,0.113007,8.532374,0.387218,6.253816,8.708455,-7.108482,-3.492588,8.535867,-5.888063,-5.366888,-5.174737,-8.364055,-1.460051,0.944023,6.050180,-2.425317,-5.698873,-7.378394,-6.985049,-8.160832,7.113267,4.399692,-6.527010,3.011803,8.491790,3.688637,8.210147,-1.864742,-0.088580,-7.173659,-5.989613,-4.505232,1.249869,6.567223,-4.114363,4.696972,-9.238934,5.881885,2.360290,6.413230,-8.702852,5.643591,-2.389347,-7.245624,4.003854,7.597935,5.281545,-1.126575,-0.376303,-8.184343,-5.662982,-4.848876,3.549905,5.963609,-2.441772,8.530988,7.881878,-5.704044,-4.533975,-1.373726,-2.260347,-6.276445,7.284275,-6.584573,-8.015227,7.058236,-0.248886,4.703920,2.180889,-9.938841,-0.152362,0.943906,-4.205236,0.299835,-7.377709,6.808025,4.079254,-8.751038,-2.896544,2.929055,-4.917423,4.838590,-8.732397,-4.394930,-9.689835,-6.543666,-4.921124,-1.765533,0.074807,5.324092,-4.896074,-5.622211,-3.315568,-5.441579,8.903628,6.656091,-0.795609,-1.221241,-1.769768,3.748764,-6.457406,5.825078,8.150032,7.231801,4.420733,-1.722902,0.418696,-3.798540,2.658701,5.281971,-4.882696,-2.717349,9.791261,7.351734,8.245380,-7.419707,-4.021299,-7.710900,-7.010718,6.157660,2.136165,4.254976,-2.729177,-6.071696,-8.890282,3.406816,4.151078,-5.531026,-9.908304,-5.049440,-6.957950,4.471520,-0.114667,-1.717980,-0.001552,-1.397265,0.736432,-5.362654,2.467951,6.501145,-2.562900,-5.459958,0.852240,0.326291,1.639967,8.720538,-8.552353,-8.806584,8.453760,0.799600,-8.194644,2.002370,2.644769,-2.407844,-0.236903,3.341136,-7.142187,-6.903555,-5.191191,6.665721,5.762470,0.783798,-3.148434,-3.992089,-3.675238,4.459179,-3.331298,-1.273704,-3.738048,-1.243466,-9.403133,-0.727677,-9.222009,-0.254406,-4.793412,-1.146206,1.684339,6.777279,5.557022,6.022582,-0.522636,7.135576,4.211307,-6.288602,-6.671693,-7.087314,-4.011270,3.553466,-9.869274,4.098884,1.417257,-8.434853,3.507152,-8.145631,-5.799515,-1.638216,-1.549939,6.890342,4.225479,-1.982480,-7.386881,5.872700,3.349530,1.929321,-0.862640,-1.530975,-5.796479,-7.092365,-2.056975,6.582143,-3.833398,7.132165,3.227284,-9.635911,2.032919,-6.482633,-1.575754,-5.114793,-2.611388,7.566383,4.896326,-8.466253,-2.297968,8.600794,-6.096060,1.059170,6.805128,5.739239,9.119826,3.194342,-1.977024,6.377363,6.842428,-3.120531,7.492350,1.651837,4.598401,2.425476,-5.891463,8.561888,7.148534,-8.305001,8.277304,1.701183,6.095614,5.109768,-3.848127,-5.590455,0.921729,1.766971,-4.453781,2.243193,-1.524551,-8.095287,8.938634,9.476771,-8.034399,3.394082,-8.089962,0.783188,-2.433029,1.579347,9.905940,-7.834284,6.070387,1.147033,-6.092760,0.441717,6.571722,-1.577085,0.086868,3.408477,7.064952,-2.888488,3.161944,3.423428,-5.254385,-5.672778,8.358129,-6.512995,-8.358171,-6.138424,-1.056449,-3.675273,0.138604,7.469490,-0.258454,0.865301,4.620552,3.713468,7.263666,-0.099125,-8.275870,7.956140,-9.313769,-8.750578,5.545630,7.382764,-6.204177,-3.549073,-0.091362,3.658035,-8.622605,-5.895374,-0.815197,6.932421,5.214015,9.102749,-3.632348,9.572499,4.429790,-1.112717,-4.200521,-5.934270,1.991108,7.676625,-4.807364,-8.113444,6.079493,0.917734,7.349674,4.099257,-0.506540,-7.979549,3.708093,7.322502,9.164417,0.095061,-5.333379,-8.119414,-5.549367,4.857776,-5.363447,-5.426429,5.032031,4.524433,-6.736758,3.807171,-0.629119,3.940351,3.139705,-0.067295,-6.875749,-2.649610,0.772392,-1.777972,-1.390761,3.283370,-9.687526,-5.930615,4.487863,-8.151766,-4.899588,-7.452511,3.779625,-2.565385,3.051924,1.285147,9.499458,-5.626094,-0.156414,-7.665955,-6.355856,-0.932003,5.997931,-8.042369,-1.131570,-7.461079,-2.936079,6.782134,9.120146,-3.044602,-1.708780,-3.026580,-2.348356,2.141536,-5.971114,9.152543,9.787089,0.640832,6.379352,7.079729,-0.262019,-9.325129,-3.903230,-8.914695,-8.507162,-4.920520,-5.754143,-9.807476,3.207140,7.987978,4.404943,1.464482,-0.938167,-1.097145,-8.271230,-1.866833,1.145349,-0.986547,-4.181750,1.021783,3.619270,-4.291029,2.017967,-5.702242,-5.537272,-1.013348,5.145831,-8.264232,-8.803552,3.867733,-4.139726,5.063866,-1.625824,2.381874,-2.542584,9.974587,3.891645,3.318871,-1.206523,1.990577,5.276214,3.840875,4.107384,7.315873,-4.275145,3.926001,-6.446753,-5.203842,-3.768569,6.446795,1.471540,-5.064687,-5.765750,9.407759,-8.618256,4.272288,-0.474402,-9.299076,-7.931184,6.175678,-9.416564,6.411426,3.799964,9.202589,-8.584640,-9.137883,-0.476973,-0.417260,-2.022273,4.984226]], dtype = "float32")#candidate|13653|(1, 960)|const|float32
call_13651 = relay.TupleGetItem(func_7659_call(relay.reshape(const_13652.astype('uint64'), [15, 11, 4]), relay.reshape(const_13652.astype('uint64'), [15, 11, 4]), relay.reshape(const_13653.astype('float32'), [10, 96]), ), 3)
call_13654 = relay.TupleGetItem(func_7664_call(relay.reshape(const_13652.astype('uint64'), [15, 11, 4]), relay.reshape(const_13652.astype('uint64'), [15, 11, 4]), relay.reshape(const_13653.astype('float32'), [10, 96]), ), 3)
func_13437_call = mod.get_global_var('func_13437')
func_13439_call = mutated_mod.get_global_var('func_13439')
call_13656 = func_13437_call()
call_13657 = func_13437_call()
func_6701_call = mod.get_global_var('func_6701')
func_6703_call = mutated_mod.get_global_var('func_6703')
call_13666 = relay.TupleGetItem(func_6701_call(), 0)
call_13667 = relay.TupleGetItem(func_6703_call(), 0)
output = relay.Tuple([call_13630,call_13651,const_13652,const_13653,call_13656,call_13666,])
output2 = relay.Tuple([call_13631,call_13654,const_13652,const_13653,call_13657,call_13667,])
func_13671 = relay.Function([], output)
mod['func_13671'] = func_13671
mod = relay.transform.InferType()(mod)
output = func_13671()
func_13672 = relay.Function([], output)
mutated_mod['func_13672'] = func_13672
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12330_call = mod.get_global_var('func_12330')
func_12332_call = mutated_mod.get_global_var('func_12332')
call_13678 = func_12330_call()
call_13679 = func_12330_call()
output = call_13678
output2 = call_13679
func_13699 = relay.Function([], output)
mod['func_13699'] = func_13699
mod = relay.transform.InferType()(mod)
output = func_13699()
func_13700 = relay.Function([], output)
mutated_mod['func_13700'] = func_13700
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10368_call = mod.get_global_var('func_10368')
func_10369_call = mutated_mod.get_global_var('func_10369')
call_13819 = relay.TupleGetItem(func_10368_call(), 0)
call_13820 = relay.TupleGetItem(func_10369_call(), 0)
func_5951_call = mod.get_global_var('func_5951')
func_5952_call = mutated_mod.get_global_var('func_5952')
call_13821 = func_5951_call()
call_13822 = func_5951_call()
output = relay.Tuple([call_13819,call_13821,])
output2 = relay.Tuple([call_13820,call_13822,])
func_13839 = relay.Function([], output)
mod['func_13839'] = func_13839
mod = relay.transform.InferType()(mod)
mutated_mod['func_13839'] = func_13839
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13839_call = mutated_mod.get_global_var('func_13839')
call_13840 = func_13839_call()
output = call_13840
func_13841 = relay.Function([], output)
mutated_mod['func_13841'] = func_13841
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13625_call = mod.get_global_var('func_13625')
func_13627_call = mutated_mod.get_global_var('func_13627')
call_13991 = relay.TupleGetItem(func_13625_call(), 0)
call_13992 = relay.TupleGetItem(func_13627_call(), 0)
output = call_13991
output2 = call_13992
func_14010 = relay.Function([], output)
mod['func_14010'] = func_14010
mod = relay.transform.InferType()(mod)
output = func_14010()
func_14011 = relay.Function([], output)
mutated_mod['func_14011'] = func_14011
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11660_call = mod.get_global_var('func_11660')
func_11662_call = mutated_mod.get_global_var('func_11662')
call_14077 = relay.TupleGetItem(func_11660_call(), 0)
call_14078 = relay.TupleGetItem(func_11662_call(), 0)
func_4057_call = mod.get_global_var('func_4057')
func_4058_call = mutated_mod.get_global_var('func_4058')
call_14079 = relay.TupleGetItem(func_4057_call(), 0)
call_14080 = relay.TupleGetItem(func_4058_call(), 0)
output = relay.Tuple([call_14077,call_14079,])
output2 = relay.Tuple([call_14078,call_14080,])
func_14084 = relay.Function([], output)
mod['func_14084'] = func_14084
mod = relay.transform.InferType()(mod)
mutated_mod['func_14084'] = func_14084
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14084_call = mutated_mod.get_global_var('func_14084')
call_14085 = func_14084_call()
output = call_14085
func_14086 = relay.Function([], output)
mutated_mod['func_14086'] = func_14086
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9048_call = mod.get_global_var('func_9048')
func_9049_call = mutated_mod.get_global_var('func_9049')
call_14124 = relay.TupleGetItem(func_9048_call(), 0)
call_14125 = relay.TupleGetItem(func_9049_call(), 0)
func_14084_call = mod.get_global_var('func_14084')
func_14086_call = mutated_mod.get_global_var('func_14086')
call_14140 = relay.TupleGetItem(func_14084_call(), 1)
call_14141 = relay.TupleGetItem(func_14086_call(), 1)
output = relay.Tuple([call_14124,call_14140,])
output2 = relay.Tuple([call_14125,call_14141,])
func_14158 = relay.Function([], output)
mod['func_14158'] = func_14158
mod = relay.transform.InferType()(mod)
mutated_mod['func_14158'] = func_14158
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14158_call = mutated_mod.get_global_var('func_14158')
call_14159 = func_14158_call()
output = call_14159
func_14160 = relay.Function([], output)
mutated_mod['func_14160'] = func_14160
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10292_call = mod.get_global_var('func_10292')
func_10294_call = mutated_mod.get_global_var('func_10294')
call_14191 = func_10292_call()
call_14192 = func_10292_call()
func_5749_call = mod.get_global_var('func_5749')
func_5753_call = mutated_mod.get_global_var('func_5753')
const_14213 = relay.const([-7.390234,0.856490,-7.949698,-8.015164,-3.629114,4.541522,-3.590908,7.339309,-3.531943,-3.022520,-8.476836,1.052349,-7.348463,-6.824378,-8.765993,3.184510,-9.382917,0.292260,0.405293,1.508007,-8.295614,2.854745,3.122171,-0.983009,5.778299,-9.855950,8.481556,7.501046,-8.994403,8.007158,3.015074,6.433181,-6.136569,2.107786,-6.161231,1.267021,1.910985,0.816257,2.003433,-4.052247,-2.889344,-9.839881,-0.514113,-7.071389,1.283993,5.155823,-4.727103,-9.478413,4.472855,-3.494737,5.904796,-2.070059,-8.000655,7.523141,-0.050515,-4.927745,-8.480298,-4.777265,-2.035769,9.040482,-2.785644,8.480704,-6.635297,7.690141,0.730096,4.076081,8.307778,1.605649,-7.665445,5.925207,-1.310544,6.073086,-2.306480,-4.807326,-2.830538,7.006792,-5.672184,4.508637,-8.185779,0.244090,-2.218091,-6.340861,-5.885617,-4.351720,-6.323108,4.945728,8.946850,5.694514,-3.832663,9.572431,-1.304635,-4.504108,1.381007,3.408904,-3.780522,9.599293,6.255360,0.759880,9.992390,-7.980416,8.860934,-5.304661,1.913689,3.023486,8.277143,-5.685879,7.987436,4.934305,4.975775,-4.186810,4.540452,-2.945625,-7.858592,-3.995792,5.447900,3.981297,2.016360,-3.519488,-4.030290,-4.940385,-7.818232,4.694175,9.290787,-1.535320,3.826348,8.487143,-0.689141,7.938522,3.301753,-2.846670,0.004252,9.099483,6.192371,0.537425,6.599940,-3.506047,-7.558786,8.884664,-0.053034,-8.949757,6.904085,-7.966290,-2.201369,-0.465083,1.859532,-1.881673,-7.353719,0.708065,6.036134,0.715855,5.372283,-0.473492,1.915902,4.974769,5.183640,4.288293,4.672813,-8.297644,-9.573401,9.571072,4.344982,-4.198528,-8.641635,-7.921750,-5.318739,-2.727651,8.819824,8.893504,5.960368,-7.642569,9.430268,8.762817,5.881394,-7.941274,-4.897279,5.941917,7.066981,8.185522,-5.180926,-6.522435,-6.998365,-8.562737,7.993256,-4.713746,-6.413504,-8.483051,1.801808,3.082941,4.880264,-4.580400,6.294115,-7.004274,0.625900,-0.878856,9.055452,-1.415171,-2.820427,1.373595,-9.732432,-6.199823,-9.353905,-3.680376,-4.570856,-5.067196,0.429062,6.928689,-9.810839,-8.199047,4.911245,4.102810,7.168377,-2.685200,-3.249753,6.958743,-1.939699,-5.289195,-5.913073,-0.786201,-2.432116,8.327766,2.763675,-2.882520,-7.621403,2.596899,-5.813158,-2.140896,-0.731333,8.115918,-1.761697,1.729734,-5.550052,4.364929,0.439612,5.597070,-9.455710,7.156736,6.846328,0.086068,-8.404047,3.410680,-3.614866,-6.122649,0.965435,1.989044,7.281142,-8.994345,-0.764386,-3.667189,5.683344,4.196946,-3.844358,5.556896,2.167546,1.825403,6.904596,-5.736396,-9.529995,-3.822895,-4.968440,3.230688,-2.175031,9.305333,3.163610,-3.509912,3.894493,-3.333784,8.691083,0.741140,8.549890,-2.035376,5.689879,-0.713276,-4.716048,9.864832,-2.820928,-2.690553,-6.888362,-8.380463,7.317982,-3.001430,-1.525437,2.689476,-6.708578,-6.365498,0.814565,-3.415237,9.824620,0.598577,0.465542,-0.404892,1.056552,7.762973,-5.693416,-6.547881,-9.312862,-2.971702,3.719286,-7.017113,-7.821570,4.352137,-9.471103,7.431406,-0.983479,5.691386,9.959210,-8.812249,-8.229165,6.842128,2.953716,-2.239348,-3.668727,-5.538572,-3.875879,-5.296340,-2.866796,2.781346,8.601544,-3.226875,9.269478,-1.813448,-1.184131,0.653456,-9.399681,8.695627,-1.624652,9.310505,6.972612,3.704817,8.059925,-1.803903,6.182438,-4.068830,-9.381840,7.690978,-6.564851,9.485675,-3.508022,0.776908,7.730389,-3.359988,-9.606608,-5.417927,8.051896,-2.403374,3.599737,-8.249482,-2.387101,-8.648064,-9.947734,-7.423008,7.940942,9.099432,-0.458533,-0.115703,9.898384,-0.164371,-9.660160,4.254115,-7.725654,-1.632652,7.342596,-6.752109,9.483646,-4.049961,-3.243176,-4.661905,-5.860009,6.198752,-5.168181,-3.618749,-4.196387,-4.358694,-2.428962,2.572149,9.760993,-4.551677,-6.189816,-9.288076,7.017050,9.023842,0.950068,1.258533,9.399975,-5.887121,-6.352192,-8.270703,5.270871,-4.189198,-2.339015,-1.362293,2.251443,-2.280006,-6.839202,-7.332292,-7.366903,9.384303,7.690069,4.828200,-9.696206,5.320322,2.775671,5.341454,-6.128884,-4.945700,5.995351,-6.265053,7.466264,0.492109,0.716695,-8.550657,7.981334,6.057724,-5.934541,-8.900073,-3.981735,-2.821318,1.068475,0.793936,8.599507,-5.192284,-4.551436,0.182877,-3.192306,6.696287,-7.495903,0.285917,-2.534419,8.253911,0.463313,8.796555,0.525348,5.279455,2.203220,-6.306522,-7.357796,-5.953274,7.460779,3.396828,-1.759493,2.825148,-9.712509,-4.951352,4.698517,1.887791,6.632731,-6.251221,-0.355710,5.870812,-3.081590,-1.744776,1.345247,-0.305257,3.320446,-8.592837,-6.098335,-9.444454,-0.214173,1.083819,-3.622388,-1.568539,0.018105,-8.394550,6.211964,-9.079956,5.785882,-9.748870,5.883672,7.817311], dtype = "float64")#candidate|14213|(468,)|const|float64
call_14212 = relay.TupleGetItem(func_5749_call(relay.reshape(call_14191.astype('int8'), []), relay.reshape(const_14213.astype('float64'), [468,]), ), 0)
call_14214 = relay.TupleGetItem(func_5753_call(relay.reshape(call_14191.astype('int8'), []), relay.reshape(const_14213.astype('float64'), [468,]), ), 0)
bop_14220 = relay.bitwise_xor(const_14213.astype('int8'), call_14212.astype('int8')) # shape=(15, 468)
bop_14223 = relay.bitwise_xor(const_14213.astype('int8'), call_14214.astype('int8')) # shape=(15, 468)
func_3402_call = mod.get_global_var('func_3402')
func_3405_call = mutated_mod.get_global_var('func_3405')
var_14232 = relay.var("var_14232", dtype = "float32", shape = (420,))#candidate|14232|(420,)|var|float32
call_14231 = relay.TupleGetItem(func_3402_call(relay.reshape(var_14232.astype('float32'), [6, 7, 10]), relay.reshape(var_14232.astype('float32'), [6, 7, 10]), ), 1)
call_14233 = relay.TupleGetItem(func_3405_call(relay.reshape(var_14232.astype('float32'), [6, 7, 10]), relay.reshape(var_14232.astype('float32'), [6, 7, 10]), ), 1)
func_11132_call = mod.get_global_var('func_11132')
func_11133_call = mutated_mod.get_global_var('func_11133')
call_14235 = func_11132_call()
call_14236 = func_11132_call()
func_9036_call = mod.get_global_var('func_9036')
func_9037_call = mutated_mod.get_global_var('func_9037')
call_14239 = relay.TupleGetItem(func_9036_call(), 2)
call_14240 = relay.TupleGetItem(func_9037_call(), 2)
uop_14276 = relay.acosh(bop_14220.astype('float64')) # shape=(15, 468)
uop_14278 = relay.acosh(bop_14223.astype('float64')) # shape=(15, 468)
var_14286 = relay.var("var_14286", dtype = "float64", shape = (15, 468))#candidate|14286|(15, 468)|var|float64
bop_14287 = relay.floor_mod(uop_14276.astype('float32'), relay.reshape(var_14286.astype('float32'), relay.shape_of(uop_14276))) # shape=(15, 468)
bop_14290 = relay.floor_mod(uop_14278.astype('float32'), relay.reshape(var_14286.astype('float32'), relay.shape_of(uop_14278))) # shape=(15, 468)
output = relay.Tuple([call_14191,call_14231,var_14232,call_14235,call_14239,bop_14287,])
output2 = relay.Tuple([call_14192,call_14233,var_14232,call_14236,call_14240,bop_14290,])
F = relay.Function([var_14232,var_14286,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_14232,var_14286,], output2)
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
