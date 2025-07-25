import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_300 = relay.var("var_300", dtype = "uint64", shape = ())#candidate|300|()|var|uint64
const_301 = relay.const([[[2],[-6],[-2],[5],[1],[2],[3],[-10],[7],[-2],[5]]], dtype = "uint64")#candidate|301|(1, 11, 1)|const|uint64
bop_302 = relay.bitwise_or(var_300.astype('uint64'), const_301.astype('uint64')) # shape=(1, 11, 1)
output = relay.Tuple([bop_302,])
output2 = relay.Tuple([bop_302,])
func_308 = relay.Function([var_300,], output)
mod['func_308'] = func_308
mod = relay.transform.InferType()(mod)
mutated_mod['func_308'] = func_308
mutated_mod = relay.transform.InferType()(mutated_mod)
var_309 = relay.var("var_309", dtype = "uint64", shape = ())#candidate|309|()|var|uint64
func_308_call = mutated_mod.get_global_var('func_308')
call_310 = func_308_call(var_309)
output = call_310
func_311 = relay.Function([var_309], output)
mutated_mod['func_311'] = func_311
mutated_mod = relay.transform.InferType()(mutated_mod)
const_394 = relay.const(-5, dtype = "int32")#candidate|394|()|const|int32
const_395 = relay.const([[[-10,-5,8,-9,7,8,9,7,-5,9,2,-5,3],[-5,-1,-10,-9,-2,-3,2,8,-1,3,8,-9,-4],[-7,3,6,-2,4,-10,9,2,4,1,5,8,10],[-6,5,3,10,-1,3,3,-7,2,8,5,9,5],[-8,4,1,10,-9,-7,8,-5,-1,-10,-5,2,8]],[[7,-5,-3,-5,2,6,-1,2,6,-4,-1,-1,-3],[5,10,-5,1,9,-3,-9,-10,9,-10,9,-1,6],[10,-6,6,10,-3,2,5,5,6,4,-1,-7,-6],[-8,1,-10,3,-6,7,6,-1,1,-10,5,-4,-9],[-4,7,-5,6,9,1,-3,-3,-4,-10,7,-10,-10]],[[2,6,9,10,-9,-1,4,-4,-3,1,7,5,10],[-1,-9,-5,-6,-4,2,-3,10,-7,-3,9,-8,-4],[-6,4,-2,-6,5,4,6,-8,-4,1,-4,-10,1],[-5,-2,6,9,-5,7,4,5,-5,9,-9,-4,-9],[-1,5,10,1,-10,-1,-8,-2,8,-9,5,3,-7]],[[9,5,2,-8,-7,9,-10,6,-10,6,9,7,6],[-4,-7,5,4,3,7,-3,10,4,-10,3,-5,9],[2,4,1,-9,8,-6,6,-10,-3,-7,4,-4,2],[-4,6,-10,1,-8,-9,5,-1,-4,2,-9,-7,-9],[10,5,1,-6,3,7,10,-10,-2,-10,6,1,-8]],[[-3,9,-5,-7,8,10,-7,9,-10,-9,10,5,-6],[4,1,10,-4,-7,-5,-1,-4,-6,-7,5,6,10],[-9,5,-8,-5,-8,2,-1,3,5,8,7,10,-10],[1,-3,3,-6,7,7,2,6,-9,2,4,6,-7],[-9,6,4,-5,-10,8,7,9,-9,9,-2,-2,-10]],[[4,-2,8,-1,-1,6,3,6,-10,-9,7,10,1],[2,-10,4,8,-6,5,5,-4,4,4,9,3,5],[-5,-3,6,-2,10,2,-1,-6,-8,4,9,9,6],[-9,5,-8,-6,-7,-8,1,-4,-8,3,-1,3,3],[1,-7,-10,-7,-10,-5,6,1,10,4,6,9,5]],[[10,-5,-2,-5,-7,-7,1,-9,-4,-8,-3,-8,4],[-10,-3,5,5,-8,-8,7,-1,-2,-2,9,-10,-10],[7,1,-9,-4,-7,10,1,-10,3,6,4,6,-1],[-1,-2,-5,6,-10,-8,-1,-7,9,-9,7,-10,7],[5,9,10,8,-10,1,-10,5,9,-4,-7,4,-6]],[[9,8,-10,-3,8,9,-5,8,7,9,7,-5,6],[-6,9,5,-7,-6,-3,-6,-2,6,3,3,3,1],[-4,1,-8,2,2,-5,-8,6,10,4,-6,-9,-6],[1,4,1,8,-8,10,6,-9,1,-2,1,-10,5],[-7,6,-7,-5,9,-1,-8,3,-10,2,-10,7,9]],[[-7,2,4,8,-5,7,8,-5,-2,7,-3,-6,6],[-7,1,2,-6,2,6,-9,7,-2,-3,3,2,-5],[-8,-9,9,1,5,-8,10,10,-9,8,9,10,-6],[9,4,-2,-7,9,8,-5,-3,-3,-2,10,6,-7],[7,6,10,-9,1,7,2,-3,-7,-5,-3,5,5]],[[-9,5,-5,5,6,-7,10,-6,-6,-4,-3,7,-1],[-10,6,-2,-6,2,9,-3,5,-10,9,-3,-8,-2],[-5,-1,-7,-3,-6,-9,3,-6,-1,7,-10,-2,-7],[-2,9,6,-2,2,-9,4,1,-10,7,9,4,3],[-5,2,9,6,7,3,10,9,-10,7,-6,-8,-4]],[[8,-2,-1,-7,8,-7,3,-6,-1,2,8,-3,-5],[-3,-10,7,4,-3,4,-7,6,-7,-6,-5,-3,-9],[9,7,10,5,6,2,-1,4,4,10,-5,-9,1],[-2,-1,5,-2,3,2,-4,2,-8,-10,10,6,-2],[-8,4,4,-4,-8,6,1,3,-9,-2,4,6,4]]], dtype = "int32")#candidate|395|(11, 5, 13)|const|int32
bop_396 = relay.bitwise_or(const_394.astype('int32'), const_395.astype('int32')) # shape=(11, 5, 13)
uop_409 = relay.erf(bop_396.astype('float32')) # shape=(11, 5, 13)
func_308_call = mod.get_global_var('func_308')
func_311_call = mutated_mod.get_global_var('func_311')
call_415 = relay.TupleGetItem(func_308_call(relay.reshape(const_394.astype('uint64'), [])), 0)
call_416 = relay.TupleGetItem(func_311_call(relay.reshape(const_394.astype('uint64'), [])), 0)
bop_420 = relay.greater_equal(call_415.astype('bool'), const_394.astype('bool')) # shape=(1, 11, 1)
bop_423 = relay.greater_equal(call_416.astype('bool'), const_394.astype('bool')) # shape=(1, 11, 1)
bop_450 = relay.power(bop_396.astype('float32'), relay.reshape(uop_409.astype('float32'), relay.shape_of(bop_396))) # shape=(11, 5, 13)
func_308_call = mod.get_global_var('func_308')
func_311_call = mutated_mod.get_global_var('func_311')
call_458 = relay.TupleGetItem(func_308_call(relay.reshape(const_394.astype('uint64'), [])), 0)
call_459 = relay.TupleGetItem(func_311_call(relay.reshape(const_394.astype('uint64'), [])), 0)
bop_464 = relay.equal(bop_450.astype('bool'), relay.reshape(uop_409.astype('bool'), relay.shape_of(bop_450))) # shape=(11, 5, 13)
func_308_call = mod.get_global_var('func_308')
func_311_call = mutated_mod.get_global_var('func_311')
call_467 = relay.TupleGetItem(func_308_call(relay.reshape(const_394.astype('uint64'), [])), 0)
call_468 = relay.TupleGetItem(func_311_call(relay.reshape(const_394.astype('uint64'), [])), 0)
func_308_call = mod.get_global_var('func_308')
func_311_call = mutated_mod.get_global_var('func_311')
call_487 = relay.TupleGetItem(func_308_call(relay.reshape(const_394.astype('uint64'), [])), 0)
call_488 = relay.TupleGetItem(func_311_call(relay.reshape(const_394.astype('uint64'), [])), 0)
var_491 = relay.var("var_491", dtype = "bool", shape = (11, 5, 13))#candidate|491|(11, 5, 13)|var|bool
bop_492 = relay.logical_and(bop_464.astype('bool'), relay.reshape(var_491.astype('bool'), relay.shape_of(bop_464))) # shape=(11, 5, 13)
func_308_call = mod.get_global_var('func_308')
func_311_call = mutated_mod.get_global_var('func_311')
call_499 = relay.TupleGetItem(func_308_call(relay.reshape(const_394.astype('uint64'), [])), 0)
call_500 = relay.TupleGetItem(func_311_call(relay.reshape(const_394.astype('uint64'), [])), 0)
output = relay.Tuple([bop_420,call_458,call_467,call_487,bop_492,call_499,])
output2 = relay.Tuple([bop_423,call_459,call_468,call_488,bop_492,call_500,])
func_504 = relay.Function([var_491,], output)
mod['func_504'] = func_504
mod = relay.transform.InferType()(mod)
mutated_mod['func_504'] = func_504
mutated_mod = relay.transform.InferType()(mutated_mod)
var_505 = relay.var("var_505", dtype = "bool", shape = (11, 5, 13))#candidate|505|(11, 5, 13)|var|bool
func_504_call = mutated_mod.get_global_var('func_504')
call_506 = func_504_call(var_505)
output = call_506
func_507 = relay.Function([var_505], output)
mutated_mod['func_507'] = func_507
mutated_mod = relay.transform.InferType()(mutated_mod)
const_704 = relay.const([[[-2,-8,-2,-6,8,-4,-3,-3,-1,-7,1],[-10,3,1,-9,9,-5,4,-6,10,-4,3],[3,8,2,-7,-7,-3,-8,4,-3,3,-10],[7,9,9,4,-3,-5,10,-6,10,4,6],[10,-1,2,4,1,9,-9,-5,2,9,-1],[-7,-8,2,4,5,-7,8,-2,-3,-4,-5],[3,-7,8,-2,-6,5,8,7,-5,-6,9],[-2,-6,4,-7,4,-8,5,-8,-2,6,10],[5,7,-2,-2,9,-1,-1,7,-5,10,-4],[7,1,-8,-9,2,8,5,2,-10,-5,8],[-8,-6,5,-6,10,-1,-5,8,9,-7,1]],[[6,1,-6,9,-2,8,1,3,-4,-1,4],[6,-9,5,-4,9,-2,8,-7,-4,5,9],[7,3,5,-6,1,2,-9,-5,-5,-2,5],[7,-8,-10,-2,1,3,1,-10,-8,3,1],[8,2,8,-10,-4,4,-7,7,5,9,3],[-5,-10,-6,-4,-2,10,-6,8,1,1,5],[2,-7,1,-5,7,9,-5,-8,-9,1,-4],[10,-3,5,-8,1,-4,5,6,2,-9,1],[-4,-3,9,6,3,7,-7,-9,7,-5,10],[-8,9,10,-9,-4,-9,-7,4,-4,-1,10],[-5,5,1,-3,-7,7,-1,7,-7,-2,-9]],[[7,-6,10,-3,-5,9,10,-7,1,6,-1],[-5,6,1,-10,-10,-4,7,-2,-4,9,-7],[5,4,10,-4,-8,1,-2,-3,-3,-9,-9],[-2,-9,8,-10,-6,8,1,-3,-9,3,-4],[-2,-7,-10,-1,3,8,10,9,-2,6,-9],[8,-9,3,-8,-7,2,5,-8,-10,10,4],[-5,-1,-10,-9,-2,-8,-5,-5,8,1,-5],[3,-3,-6,-1,4,-5,-5,9,-1,10,-6],[-2,7,-2,-1,5,2,-5,2,1,3,10],[-9,1,-2,3,5,-8,7,-1,8,-2,-7],[-9,4,4,5,5,-4,6,-7,-3,-6,7]],[[2,-2,5,1,3,-10,9,4,9,-10,8],[-1,6,-9,5,-6,3,9,3,9,-7,3],[-6,-2,8,10,-7,-3,4,-5,-8,-8,-2],[1,5,1,1,-10,3,-2,3,7,2,2],[1,-5,-10,-2,-9,6,-2,-8,3,10,1],[4,-5,-3,-10,2,-10,-4,1,-1,-8,-4],[5,3,-9,3,8,-3,10,-1,9,-4,2],[1,4,6,2,2,2,-7,-2,-3,8,3],[-2,-10,10,3,-2,7,-8,-7,3,-10,-7],[-7,9,-9,-8,7,-7,-2,-1,-8,1,8],[-6,-2,6,-3,-10,4,-2,8,-3,9,-2]],[[-6,-8,-5,-8,10,1,3,5,2,8,-7],[-7,8,10,2,10,4,-2,9,-3,6,-3],[3,6,-5,9,3,-5,-8,10,-6,7,10],[-8,-9,-8,-6,5,10,5,6,-5,4,9],[6,1,10,3,-7,-1,-3,3,-1,-1,8],[4,3,-2,-3,8,-2,5,-9,4,-9,-4],[3,2,-4,4,-2,-5,-2,-2,9,8,9],[5,-10,-3,5,1,-3,-1,7,-10,-6,2],[3,4,-3,3,-4,1,-9,-2,4,-2,6],[5,-1,-2,9,4,9,-1,-8,6,7,5],[6,2,-1,-6,-10,-10,-5,9,-6,3,10]],[[-8,2,-2,5,-7,-5,10,5,-4,-8,-7],[5,-6,-6,-6,5,-7,-10,-8,-6,-6,3],[-8,-2,3,-7,3,-6,-2,-8,-1,2,9],[-6,-9,-1,-3,10,5,6,-2,-8,-4,1],[-7,4,-9,-5,-2,-7,-3,-3,5,10,5],[-7,10,9,-10,-9,9,-6,-2,9,1,-5],[6,-1,-1,-8,10,3,-3,-1,3,1,-5],[-10,-9,1,9,-6,-5,-6,9,-5,1,8],[-10,-6,-9,7,-5,1,10,-6,9,1,-9],[10,-3,9,-3,-8,6,-10,-3,8,-5,-4],[2,-1,-1,5,-1,10,-2,-10,5,-9,-1]],[[5,3,-2,4,-3,-5,9,9,8,1,-6],[8,-7,3,4,-5,8,6,-8,5,9,6],[-7,-4,-6,2,9,1,3,-3,10,9,10],[7,6,-9,-3,4,1,5,-4,-3,-7,2],[8,10,-5,-5,6,3,5,8,-7,8,-10],[-9,-9,9,7,-9,-7,3,2,7,2,-2],[1,7,-4,-10,-7,1,9,6,-1,3,6],[2,-5,-5,-8,-6,-7,-9,-9,5,7,-3],[-6,-4,-4,7,-2,7,7,-8,9,5,8],[-6,4,10,7,-8,4,2,-9,-7,7,10],[-6,-8,-2,-10,9,-5,7,-4,1,-9,-4]],[[-3,9,3,4,9,-10,6,2,-10,1,-3],[3,7,1,-8,-9,7,-1,-6,-2,8,4],[3,9,4,-3,2,-6,9,-5,2,10,-5],[-8,7,-8,3,8,-5,-3,6,-7,1,7],[3,-9,-9,-4,1,5,-1,4,4,-2,-8],[9,-9,4,2,-10,-5,-9,9,9,5,-9],[-9,-4,6,2,-1,1,9,-9,-9,5,-1],[10,-2,-1,5,5,6,4,5,7,-9,5],[-6,-9,7,-2,-2,8,1,1,1,9,7],[-9,-1,8,5,-8,-10,-7,-2,-5,1,-6],[-3,10,5,1,-3,4,-7,6,10,4,-2]]], dtype = "int64")#candidate|704|(8, 11, 11)|const|int64
var_705 = relay.var("var_705", dtype = "int64", shape = (8, 11, 11))#candidate|705|(8, 11, 11)|var|int64
bop_706 = relay.less(const_704.astype('bool'), relay.reshape(var_705.astype('bool'), relay.shape_of(const_704))) # shape=(8, 11, 11)
func_308_call = mod.get_global_var('func_308')
func_311_call = mutated_mod.get_global_var('func_311')
var_711 = relay.var("var_711", dtype = "uint64", shape = ())#candidate|711|()|var|uint64
call_710 = relay.TupleGetItem(func_308_call(relay.reshape(var_711.astype('uint64'), [])), 0)
call_712 = relay.TupleGetItem(func_311_call(relay.reshape(var_711.astype('uint64'), [])), 0)
uop_715 = relay.log2(bop_706.astype('float64')) # shape=(8, 11, 11)
func_504_call = mod.get_global_var('func_504')
func_507_call = mutated_mod.get_global_var('func_507')
const_741 = relay.const([True,False,False,True,True,True,True,True,True,True,False,False,True,False,False,True,True,True,False,False,False,True,True,False,False,False,False,False,True,False,True,False,True,False,True,False,True,False,False,False,False,False,False,True,False,False,False,False,True,False,False,True,True,True,True,False,True,False,False,True,False,True,True,True,True,True,False,False,True,False,False,True,False,True,True,False,True,True,False,True,False,False,False,True,False,False,True,True,False,True,False,False,True,False,False,False,True,False,True,False,False,True,False,False,False,True,False,False,False,True,True,False,True,True,False,True,True,True,True,True,True,True,False,False,True,False,False,False,False,True,True,False,True,True,False,True,False,False,True,False,True,False,True,True,False,True,False,True,False,True,True,True,True,True,True,False,True,False,True,True,True,False,True,False,True,True,False,True,True,True,True,True,False,False,False,False,True,False,True,False,False,False,True,True,True,True,True,False,True,False,True,False,False,False,True,True,True,True,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,True,True,False,False,True,False,True,True,False,False,False,False,True,True,False,False,False,True,False,False,True,True,False,True,True,False,True,True,False,False,False,False,True,False,False,False,False,False,False,False,False,False,True,True,True,True,True,True,False,True,True,True,False,False,False,False,False,True,True,True,True,True,True,True,True,True,True,False,True,True,False,True,True,True,False,True,False,True,False,False,True,False,True,True,False,True,True,False,True,True,True,False,False,False,True,False,False,True,False,True,False,False,True,False,False,True,True,False,True,True,True,False,True,False,True,True,False,True,False,True,False,True,True,False,False,True,False,False,False,False,True,False,True,False,False,True,False,True,True,True,True,False,True,False,True,False,False,True,True,False,False,True,True,True,False,True,False,False,True,False,True,True,True,False,True,True,True,True,True,False,False,False,True,True,False,False,False,False,True,True,False,True,True,False,False,True,True,True,True,True,True,False,False,False,False,True,False,True,True,True,False,True,True,True,True,True,True,True,False,False,False,False,True,True,False,True,False,False,False,False,True,False,False,True,False,True,False,False,False,True,True,False,True,False,True,False,False,False,True,False,False,True,False,True,True,True,True,True,True,True,True,False,True,False,True,False,True,True,False,True,True,False,False,False,False,True,False,False,False,True,False,False,False,True,False,True,False,True,True,True,False,False,True,False,False,False,False,True,True,False,True,False,False,True,False,True,False,False,True,False,True,False,True,False,True,True,True,True,False,False,False,False,True,True,False,True,True,False,True,False,True,False,True,True,True,True,False,True,False,False,False,True,False,True,True,True,False,True,False,False,True,False,False,False,True,True,False,False,True,True,False,False,True,True,False,False,True,False,True,True,False,True,False,False,False,False,True,False,True,True,False,False,True,True,True,False,False,True,False,True,False,True,False,True,False,False,True,True,False,False,False,True,False,True,True,False,True,True,True,False,False,True,False,False,False,True,False,False,False,True,False,False,False,False,True,False,False,False,False,False,True,False,True,True,True,True,True,False,False,False,False,False,False,True,False,False,False,True,True,True,False,True,True,False,True,True,False,True,True,False,True,False,True,True,True,False,False,True,True,False,True,True,False,True,False,True,False,True,False,True,False,False,False,True,False,True,False,False,False,False,True,True,False,False,False,False,False,False,True,True,False,False,True,True,False,True,False,False,False,False,True,False], dtype = "bool")#candidate|741|(715,)|const|bool
call_740 = relay.TupleGetItem(func_504_call(relay.reshape(const_741.astype('bool'), [11, 5, 13])), 1)
call_742 = relay.TupleGetItem(func_507_call(relay.reshape(const_741.astype('bool'), [11, 5, 13])), 1)
func_504_call = mod.get_global_var('func_504')
func_507_call = mutated_mod.get_global_var('func_507')
call_749 = relay.TupleGetItem(func_504_call(relay.reshape(const_741.astype('bool'), [11, 5, 13])), 0)
call_750 = relay.TupleGetItem(func_507_call(relay.reshape(const_741.astype('bool'), [11, 5, 13])), 0)
func_308_call = mod.get_global_var('func_308')
func_311_call = mutated_mod.get_global_var('func_311')
call_752 = relay.TupleGetItem(func_308_call(relay.reshape(var_711.astype('uint64'), [])), 0)
call_753 = relay.TupleGetItem(func_311_call(relay.reshape(var_711.astype('uint64'), [])), 0)
output = relay.Tuple([call_710,var_711,uop_715,call_740,const_741,call_749,call_752,])
output2 = relay.Tuple([call_712,var_711,uop_715,call_742,const_741,call_750,call_753,])
func_755 = relay.Function([var_705,var_711,], output)
mod['func_755'] = func_755
mod = relay.transform.InferType()(mod)
var_756 = relay.var("var_756", dtype = "int64", shape = (8, 11, 11))#candidate|756|(8, 11, 11)|var|int64
var_757 = relay.var("var_757", dtype = "uint64", shape = ())#candidate|757|()|var|uint64
output = func_755(var_756,var_757,)
func_758 = relay.Function([var_756,var_757,], output)
mutated_mod['func_758'] = func_758
mutated_mod = relay.transform.InferType()(mutated_mod)
var_805 = relay.var("var_805", dtype = "int64", shape = (4, 13, 7))#candidate|805|(4, 13, 7)|var|int64
var_806 = relay.var("var_806", dtype = "int64", shape = (4, 13, 7))#candidate|806|(4, 13, 7)|var|int64
bop_807 = relay.minimum(var_805.astype('int64'), relay.reshape(var_806.astype('int64'), relay.shape_of(var_805))) # shape=(4, 13, 7)
output = relay.Tuple([bop_807,])
output2 = relay.Tuple([bop_807,])
func_818 = relay.Function([var_805,var_806,], output)
mod['func_818'] = func_818
mod = relay.transform.InferType()(mod)
mutated_mod['func_818'] = func_818
mutated_mod = relay.transform.InferType()(mutated_mod)
func_818_call = mutated_mod.get_global_var('func_818')
var_820 = relay.var("var_820", dtype = "int64", shape = (4, 13, 7))#candidate|820|(4, 13, 7)|var|int64
var_821 = relay.var("var_821", dtype = "int64", shape = (4, 13, 7))#candidate|821|(4, 13, 7)|var|int64
call_819 = func_818_call(var_820,var_821,)
output = call_819
func_822 = relay.Function([var_820,var_821,], output)
mutated_mod['func_822'] = func_822
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1037 = relay.var("var_1037", dtype = "uint16", shape = ())#candidate|1037|()|var|uint16
var_1038 = relay.var("var_1038", dtype = "uint16", shape = (11, 16, 5))#candidate|1038|(11, 16, 5)|var|uint16
bop_1039 = relay.not_equal(var_1037.astype('bool'), var_1038.astype('bool')) # shape=(11, 16, 5)
func_755_call = mod.get_global_var('func_755')
func_758_call = mutated_mod.get_global_var('func_758')
const_1043 = relay.const([[8,-7,-1,-5,-3,10,-8,9,3,8,3,5,-8,-8,4,-7,3,3,8,6,-10,7,1,9,-9,-3,-10,-2,1,1,6,-10,-4,3,-2,3,-7,1,-8,6,-7,2,7,-6,-8,6,8,4,-10,6,-8,-3,1,7,-6,9,-9,-3,-8,5,-9,-9,6,9,-10,9,3,-5,7,6,-4,-1,5,-1,6,-9,8,9,9,1,2,9,1,-2,5,-4,-2,-2],[-10,9,9,-8,-6,-3,7,-4,4,-6,7,-3,-5,-9,-3,-3,-6,-8,10,3,5,1,-10,10,-8,8,6,8,-10,8,10,8,-4,10,-2,-2,-9,-6,-7,10,5,-3,-1,2,-9,-7,-2,6,1,1,-9,10,-3,-6,5,10,-5,-4,-5,8,-9,-5,-1,-6,-5,6,10,-3,-2,-5,-6,-10,-7,7,-1,6,-9,-8,9,3,-4,9,4,-7,2,5,9,7],[8,-8,9,6,4,-10,-1,-9,1,9,2,2,-9,2,-2,6,2,-8,9,-1,-9,5,6,-5,2,4,9,7,-5,-10,7,7,-9,2,-7,10,-6,8,-9,-8,-6,-8,-10,-4,6,-10,-9,4,-1,5,-1,-6,2,-8,-6,5,-1,-6,7,-4,4,-6,2,-1,6,1,-3,-4,-10,7,1,7,-2,-2,2,2,3,-1,5,8,-9,9,-5,-8,-7,2,-8,3],[9,-1,-3,-9,8,-3,-1,6,-9,4,2,-2,9,-9,10,-7,7,-2,-10,9,2,-4,-3,4,7,-8,2,-8,-2,7,8,3,-3,-8,-7,-2,-10,-3,-9,7,-7,-5,-4,9,9,-10,-2,-4,9,8,2,-6,-8,-5,5,3,6,-8,-10,-8,3,-7,2,-9,-5,8,9,-10,-2,6,-7,-7,6,5,4,-4,-3,9,-2,10,-7,7,-2,-7,-3,10,-3,-5],[6,-4,3,-5,-8,-4,5,10,-2,-10,-3,9,-9,8,-9,10,4,4,-3,-6,5,3,-5,4,9,2,-10,-2,1,10,4,5,-5,5,-8,-8,2,5,-4,5,-4,7,-1,2,8,3,-3,8,-7,-3,-6,8,-2,-5,3,-10,-10,-10,8,4,5,8,6,-7,10,6,10,-4,-10,-1,-3,-9,-1,-6,4,-5,-7,-8,-10,6,4,6,7,-8,-2,-1,1,-10],[2,1,9,-4,8,9,-6,8,8,-3,5,-3,2,2,5,-6,-1,10,3,-6,3,-7,-2,-8,8,-5,-5,-9,-2,2,4,-2,-7,5,-4,10,-6,-8,-1,-9,8,-1,-2,-9,1,2,1,10,-6,-7,6,10,4,2,-2,6,7,-2,8,-5,-7,6,-1,-6,-1,-5,-10,-1,-3,-2,6,-7,-5,-3,-4,-4,5,9,-8,3,9,8,-5,4,2,4,-3,-2],[-2,3,-5,-5,9,-8,-8,-6,-1,6,3,-3,-7,-2,10,1,1,5,1,8,-3,-8,-9,10,9,5,8,-7,-7,-5,7,8,-10,-5,5,2,2,-1,-4,-3,6,5,6,-9,2,-9,-10,8,1,10,9,-6,-1,3,9,-8,-4,9,6,-4,-1,-9,1,2,1,8,5,-10,-2,-2,1,-5,3,-4,1,-7,-10,-5,4,-2,1,-2,5,-3,-8,-1,-4,-1],[-2,8,-2,8,-1,-2,-2,7,-6,10,-4,-2,9,-1,-10,2,9,5,-4,3,8,10,2,1,-10,-9,5,5,3,-7,-8,4,10,9,2,9,9,-8,-9,-9,2,-1,9,1,4,6,-10,1,10,3,-6,-4,2,-6,-2,9,-2,3,8,5,3,-8,-4,2,-1,-9,-7,-1,-4,-1,-1,4,-1,-5,2,-5,-3,-7,-1,2,6,-10,2,-2,-8,7,-1,1],[8,5,7,-5,10,-7,5,-5,-9,-1,-6,-9,6,-4,-7,-1,2,-6,-3,-9,-7,7,4,-10,-7,-3,-6,9,-8,-8,-9,-1,4,-2,-8,-3,-7,-6,4,-3,-9,-6,-1,-6,10,-8,-5,-2,6,-10,-2,9,5,10,1,10,2,-2,3,-5,-4,-1,-10,7,-4,-10,2,-6,5,4,-1,-6,10,-7,-8,5,-5,-10,-7,3,-6,8,4,-4,-3,-7,-3,-7],[-2,6,-7,3,-5,-9,2,6,4,-7,-1,1,7,6,2,-3,-8,-8,1,-8,-6,1,-8,-7,10,-3,3,2,-2,2,-4,10,-5,8,10,2,-5,-4,-9,-5,3,1,4,7,-4,1,3,1,-2,4,6,-7,-1,4,-2,-3,1,-2,-9,-2,-8,-10,-6,9,-1,9,-2,-10,7,-5,5,3,-1,-10,4,3,4,-2,-6,6,7,7,-2,-2,-9,8,-6,1],[-8,8,-2,3,-4,-6,-8,-10,-10,4,-1,10,5,5,9,-9,-6,8,-7,4,7,-4,2,10,10,-3,10,3,1,7,4,8,2,-8,8,10,9,2,7,-3,-6,8,-2,-3,8,5,-7,-2,9,-8,1,4,-4,-3,-8,10,5,-2,-10,9,7,10,9,5,-3,6,-4,5,-7,-1,-5,9,-10,6,-7,7,-3,10,-10,-9,-9,-8,5,1,10,-9,4,4]], dtype = "int64")#candidate|1043|(11, 88)|const|int64
call_1042 = relay.TupleGetItem(func_755_call(relay.reshape(const_1043.astype('int64'), [8, 11, 11]), relay.reshape(var_1037.astype('uint64'), []), ), 4)
call_1044 = relay.TupleGetItem(func_758_call(relay.reshape(const_1043.astype('int64'), [8, 11, 11]), relay.reshape(var_1037.astype('uint64'), []), ), 4)
func_308_call = mod.get_global_var('func_308')
func_311_call = mutated_mod.get_global_var('func_311')
call_1045 = relay.TupleGetItem(func_308_call(relay.reshape(var_1037.astype('uint64'), [])), 0)
call_1046 = relay.TupleGetItem(func_311_call(relay.reshape(var_1037.astype('uint64'), [])), 0)
output = relay.Tuple([bop_1039,call_1042,const_1043,call_1045,])
output2 = relay.Tuple([bop_1039,call_1044,const_1043,call_1046,])
func_1053 = relay.Function([var_1037,var_1038,], output)
mod['func_1053'] = func_1053
mod = relay.transform.InferType()(mod)
mutated_mod['func_1053'] = func_1053
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1053_call = mutated_mod.get_global_var('func_1053')
var_1055 = relay.var("var_1055", dtype = "uint16", shape = ())#candidate|1055|()|var|uint16
var_1056 = relay.var("var_1056", dtype = "uint16", shape = (11, 16, 5))#candidate|1056|(11, 16, 5)|var|uint16
call_1054 = func_1053_call(var_1055,var_1056,)
output = call_1054
func_1057 = relay.Function([var_1055,var_1056,], output)
mutated_mod['func_1057'] = func_1057
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1457 = relay.var("var_1457", dtype = "float64", shape = (9, 14, 16))#candidate|1457|(9, 14, 16)|var|float64
uop_1458 = relay.log(var_1457.astype('float64')) # shape=(9, 14, 16)
func_1053_call = mod.get_global_var('func_1053')
func_1057_call = mutated_mod.get_global_var('func_1057')
const_1461 = relay.const(-2, dtype = "uint16")#candidate|1461|()|const|uint16
var_1462 = relay.var("var_1462", dtype = "uint16", shape = (880,))#candidate|1462|(880,)|var|uint16
call_1460 = relay.TupleGetItem(func_1053_call(relay.reshape(const_1461.astype('uint16'), []), relay.reshape(var_1462.astype('uint16'), [11, 16, 5]), ), 2)
call_1463 = relay.TupleGetItem(func_1057_call(relay.reshape(const_1461.astype('uint16'), []), relay.reshape(var_1462.astype('uint16'), [11, 16, 5]), ), 2)
func_308_call = mod.get_global_var('func_308')
func_311_call = mutated_mod.get_global_var('func_311')
call_1468 = relay.TupleGetItem(func_308_call(relay.reshape(const_1461.astype('uint64'), [])), 0)
call_1469 = relay.TupleGetItem(func_311_call(relay.reshape(const_1461.astype('uint64'), [])), 0)
output = relay.Tuple([uop_1458,call_1460,const_1461,var_1462,call_1468,])
output2 = relay.Tuple([uop_1458,call_1463,const_1461,var_1462,call_1469,])
func_1484 = relay.Function([var_1457,var_1462,], output)
mod['func_1484'] = func_1484
mod = relay.transform.InferType()(mod)
mutated_mod['func_1484'] = func_1484
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1484_call = mutated_mod.get_global_var('func_1484')
var_1486 = relay.var("var_1486", dtype = "float64", shape = (9, 14, 16))#candidate|1486|(9, 14, 16)|var|float64
var_1487 = relay.var("var_1487", dtype = "uint16", shape = (880,))#candidate|1487|(880,)|var|uint16
call_1485 = func_1484_call(var_1486,var_1487,)
output = call_1485
func_1488 = relay.Function([var_1486,var_1487,], output)
mutated_mod['func_1488'] = func_1488
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1705 = relay.var("var_1705", dtype = "float32", shape = (5, 9, 4))#candidate|1705|(5, 9, 4)|var|float32
uop_1706 = relay.asin(var_1705.astype('float32')) # shape=(5, 9, 4)
func_755_call = mod.get_global_var('func_755')
func_758_call = mutated_mod.get_global_var('func_758')
var_1717 = relay.var("var_1717", dtype = "int64", shape = (968,))#candidate|1717|(968,)|var|int64
const_1718 = relay.const(-3, dtype = "uint64")#candidate|1718|()|const|uint64
call_1716 = relay.TupleGetItem(func_755_call(relay.reshape(var_1717.astype('int64'), [8, 11, 11]), relay.reshape(const_1718.astype('uint64'), []), ), 0)
call_1719 = relay.TupleGetItem(func_758_call(relay.reshape(var_1717.astype('int64'), [8, 11, 11]), relay.reshape(const_1718.astype('uint64'), []), ), 0)
bop_1743 = relay.less(uop_1706.astype('bool'), const_1718.astype('bool')) # shape=(5, 9, 4)
func_818_call = mod.get_global_var('func_818')
func_822_call = mutated_mod.get_global_var('func_822')
var_1761 = relay.var("var_1761", dtype = "int64", shape = (364,))#candidate|1761|(364,)|var|int64
call_1760 = relay.TupleGetItem(func_818_call(relay.reshape(var_1761.astype('int64'), [4, 13, 7]), relay.reshape(var_1761.astype('int64'), [4, 13, 7]), ), 0)
call_1762 = relay.TupleGetItem(func_822_call(relay.reshape(var_1761.astype('int64'), [4, 13, 7]), relay.reshape(var_1761.astype('int64'), [4, 13, 7]), ), 0)
output = relay.Tuple([call_1716,var_1717,bop_1743,call_1760,var_1761,])
output2 = relay.Tuple([call_1719,var_1717,bop_1743,call_1762,var_1761,])
func_1763 = relay.Function([var_1705,var_1717,var_1761,], output)
mod['func_1763'] = func_1763
mod = relay.transform.InferType()(mod)
mutated_mod['func_1763'] = func_1763
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1763_call = mutated_mod.get_global_var('func_1763')
var_1765 = relay.var("var_1765", dtype = "float32", shape = (5, 9, 4))#candidate|1765|(5, 9, 4)|var|float32
var_1766 = relay.var("var_1766", dtype = "int64", shape = (968,))#candidate|1766|(968,)|var|int64
var_1767 = relay.var("var_1767", dtype = "int64", shape = (364,))#candidate|1767|(364,)|var|int64
call_1764 = func_1763_call(var_1765,var_1766,var_1767,)
output = call_1764
func_1768 = relay.Function([var_1765,var_1766,var_1767,], output)
mutated_mod['func_1768'] = func_1768
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1773 = relay.const([[[9.914673,-0.045698,-7.885561,-7.655293,-3.525298,-2.821915,1.667447,7.011138,5.974005,8.102469,-7.657307],[-1.257692,-7.867180,9.063960,-0.771657,1.446368,9.426655,1.595954,0.160771,6.153062,-4.484009,1.092106],[-4.135267,4.928627,-6.370210,-1.727042,-7.729291,-2.301328,2.860948,6.558073,-1.794151,8.635365,-9.673221],[3.444177,6.568245,2.053737,-3.444234,8.525262,8.320179,-9.625931,2.317454,3.450493,9.165880,-4.267081],[8.150656,-5.409459,8.084243,3.444763,-8.559988,2.058684,2.061568,-0.918403,4.950967,-5.097602,-9.600875],[-4.204227,4.349101,-4.658240,8.464098,5.670201,-3.487435,-5.658731,-4.504149,2.254767,-2.778619,-3.010792],[1.537486,9.230994,-4.438974,7.509871,-0.913170,-5.255450,0.684915,5.639729,-2.007903,7.939539,-5.273125],[-7.408372,5.708728,-3.909671,-9.714322,-6.131251,4.470618,-4.890824,6.351679,-4.236476,0.535839,-5.302552],[1.453339,3.386279,-2.922461,-7.085608,-9.186936,2.747278,-6.484618,5.068477,-3.009554,-8.896262,3.085573],[1.105374,8.376408,-1.763946,6.392590,1.550899,-8.430898,-5.287211,-8.770988,-9.551085,4.186486,-6.162232],[5.520440,-7.997496,0.671457,9.250119,0.949586,-9.540913,-1.296472,0.719894,5.548130,5.823497,5.786560],[-6.480583,-6.009975,-5.745297,7.459668,-8.396359,-7.102377,-3.261687,3.652278,-6.452767,1.380102,6.766316],[7.686040,5.495313,-4.238103,9.712282,-7.881115,8.527011,-3.190877,-9.067318,-4.044209,-9.797158,1.553516],[3.467302,-7.102758,4.234431,-8.895312,6.398644,0.217918,-9.726447,1.777439,2.430948,2.027025,9.278602]]], dtype = "float64")#candidate|1773|(1, 14, 11)|const|float64
uop_1774 = relay.cos(const_1773.astype('float64')) # shape=(1, 14, 11)
func_308_call = mod.get_global_var('func_308')
func_311_call = mutated_mod.get_global_var('func_311')
var_1778 = relay.var("var_1778", dtype = "uint64", shape = ())#candidate|1778|()|var|uint64
call_1777 = relay.TupleGetItem(func_308_call(relay.reshape(var_1778.astype('uint64'), [])), 0)
call_1779 = relay.TupleGetItem(func_311_call(relay.reshape(var_1778.astype('uint64'), [])), 0)
func_818_call = mod.get_global_var('func_818')
func_822_call = mutated_mod.get_global_var('func_822')
const_1800 = relay.const([5,-6,1,10,7,6,8,4,6,4,2,3,1,-8,2,3,-3,8,6,-1,4,10,3,-6,1,-4,-2,-4,-5,-8,-6,-8,-9,-2,-6,9,-8,-4,2,9,9,-8,-2,-4,9,-6,2,-1,-10,-7,5,6,4,4,7,-1,7,-7,-4,-6,2,7,5,4,-2,-2,6,8,-8,-6,-6,-3,-8,9,-3,6,-6,9,10,9,-6,-9,-8,2,1,-3,7,-7,-6,7,-3,7,6,1,1,10,-10,2,9,-6,-4,-7,-4,-7,5,2,-9,-7,4,2,9,-7,-4,9,-4,4,-3,-2,9,9,-5,10,-9,8,-7,3,6,-5,10,4,8,-6,10,7,-7,-3,-9,-6,-2,-4,-7,-2,-8,3,-8,3,-6,-6,7,8,-4,-6,-4,1,-7,4,5,-6,3,-10,8,-9,-2,-3,-10,3,-1,-7,1,2,7,3,10,-5,-9,-3,8,-1,7,-9,4,3,1,2,-9,4,-8,8,-4,-2,7,10,-7,6,-5,-3,7,6,-7,3,-1,-4,2,9,-6,-9,-6,8,1,9,9,9,-9,5,3,2,3,-5,9,-10,-4,-7,1,-4,-9,10,-5,3,4,-10,4,-1,9,1,-1,-2,-2,-5,-4,7,4,-1,-8,2,2,9,3,4,-7,1,-8,2,2,4,8,9,-9,-10,-5,-1,4,3,-1,1,-2,7,-3,-1,-6,-3,6,-6,-2,-4,-9,-4,-4,-2,1,-6,-4,-4,-1,6,-2,2,10,-5,-6,-1,-5,-10,9,-7,-5,-5,3,10,6,1,-4,8,-3,-8,3,6,4,10,-9,-6,-7,5,-2,-3,-10,6,7,10,8,-1,-7,10,4,-5,-6,-9,-1,2,1,2,10,-7,-2,9,3,1,-6,1,3,-2,6,10,6,-1,-9,-10,10,6,-2,-2,-4,5,5,9,-4,7,-4,7,10,9,-10,-6,4,-4], dtype = "int64")#candidate|1800|(364,)|const|int64
call_1799 = relay.TupleGetItem(func_818_call(relay.reshape(const_1800.astype('int64'), [4, 13, 7]), relay.reshape(const_1800.astype('int64'), [4, 13, 7]), ), 0)
call_1801 = relay.TupleGetItem(func_822_call(relay.reshape(const_1800.astype('int64'), [4, 13, 7]), relay.reshape(const_1800.astype('int64'), [4, 13, 7]), ), 0)
output = relay.Tuple([uop_1774,call_1777,var_1778,call_1799,const_1800,])
output2 = relay.Tuple([uop_1774,call_1779,var_1778,call_1801,const_1800,])
func_1806 = relay.Function([var_1778,], output)
mod['func_1806'] = func_1806
mod = relay.transform.InferType()(mod)
mutated_mod['func_1806'] = func_1806
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1807 = relay.var("var_1807", dtype = "uint64", shape = ())#candidate|1807|()|var|uint64
func_1806_call = mutated_mod.get_global_var('func_1806')
call_1808 = func_1806_call(var_1807)
output = call_1808
func_1809 = relay.Function([var_1807], output)
mutated_mod['func_1809'] = func_1809
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1821 = relay.const([[[-8,2,3,-7,-3,8],[-8,-10,-1,-6,2,7],[-5,-10,-7,-4,9,2],[-5,3,-4,1,-5,4],[7,4,5,-9,-10,-7]]], dtype = "uint64")#candidate|1821|(1, 5, 6)|const|uint64
var_1822 = relay.var("var_1822", dtype = "uint64", shape = (5, 5, 6))#candidate|1822|(5, 5, 6)|var|uint64
bop_1823 = relay.multiply(const_1821.astype('uint64'), var_1822.astype('uint64')) # shape=(5, 5, 6)
func_818_call = mod.get_global_var('func_818')
func_822_call = mutated_mod.get_global_var('func_822')
var_1850 = relay.var("var_1850", dtype = "int64", shape = (182, 2))#candidate|1850|(182, 2)|var|int64
call_1849 = relay.TupleGetItem(func_818_call(relay.reshape(var_1850.astype('int64'), [4, 13, 7]), relay.reshape(var_1850.astype('int64'), [4, 13, 7]), ), 0)
call_1851 = relay.TupleGetItem(func_822_call(relay.reshape(var_1850.astype('int64'), [4, 13, 7]), relay.reshape(var_1850.astype('int64'), [4, 13, 7]), ), 0)
var_1858 = relay.var("var_1858", dtype = "int64", shape = (4, 13, 7))#candidate|1858|(4, 13, 7)|var|int64
bop_1859 = relay.floor_divide(call_1849.astype('float32'), relay.reshape(var_1858.astype('float32'), relay.shape_of(call_1849))) # shape=(4, 13, 7)
bop_1862 = relay.floor_divide(call_1851.astype('float32'), relay.reshape(var_1858.astype('float32'), relay.shape_of(call_1851))) # shape=(4, 13, 7)
bop_1865 = relay.less(call_1849.astype('bool'), relay.reshape(bop_1859.astype('bool'), relay.shape_of(call_1849))) # shape=(4, 13, 7)
bop_1868 = relay.less(call_1851.astype('bool'), relay.reshape(bop_1862.astype('bool'), relay.shape_of(call_1851))) # shape=(4, 13, 7)
func_504_call = mod.get_global_var('func_504')
func_507_call = mutated_mod.get_global_var('func_507')
var_1877 = relay.var("var_1877", dtype = "bool", shape = (715,))#candidate|1877|(715,)|var|bool
call_1876 = relay.TupleGetItem(func_504_call(relay.reshape(var_1877.astype('bool'), [11, 5, 13])), 4)
call_1878 = relay.TupleGetItem(func_507_call(relay.reshape(var_1877.astype('bool'), [11, 5, 13])), 4)
output = relay.Tuple([bop_1823,var_1850,bop_1865,call_1876,var_1877,])
output2 = relay.Tuple([bop_1823,var_1850,bop_1868,call_1878,var_1877,])
func_1879 = relay.Function([var_1822,var_1850,var_1858,var_1877,], output)
mod['func_1879'] = func_1879
mod = relay.transform.InferType()(mod)
var_1880 = relay.var("var_1880", dtype = "uint64", shape = (5, 5, 6))#candidate|1880|(5, 5, 6)|var|uint64
var_1881 = relay.var("var_1881", dtype = "int64", shape = (182, 2))#candidate|1881|(182, 2)|var|int64
var_1882 = relay.var("var_1882", dtype = "int64", shape = (4, 13, 7))#candidate|1882|(4, 13, 7)|var|int64
var_1883 = relay.var("var_1883", dtype = "bool", shape = (715,))#candidate|1883|(715,)|var|bool
output = func_1879(var_1880,var_1881,var_1882,var_1883,)
func_1884 = relay.Function([var_1880,var_1881,var_1882,var_1883,], output)
mutated_mod['func_1884'] = func_1884
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2022 = relay.var("var_2022", dtype = "float64", shape = (8, 11, 8))#candidate|2022|(8, 11, 8)|var|float64
uop_2023 = relay.atan(var_2022.astype('float64')) # shape=(8, 11, 8)
output = relay.Tuple([uop_2023,])
output2 = relay.Tuple([uop_2023,])
func_2031 = relay.Function([var_2022,], output)
mod['func_2031'] = func_2031
mod = relay.transform.InferType()(mod)
var_2032 = relay.var("var_2032", dtype = "float64", shape = (8, 11, 8))#candidate|2032|(8, 11, 8)|var|float64
output = func_2031(var_2032)
func_2033 = relay.Function([var_2032], output)
mutated_mod['func_2033'] = func_2033
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2230 = relay.var("var_2230", dtype = "float32", shape = (7, 1, 8))#candidate|2230|(7, 1, 8)|var|float32
const_2231 = relay.const([[[9.728153,6.483611,3.540950,2.439871,-0.951523,-7.169926,5.469932,-5.647206]],[[-3.811961,-8.464746,9.939907,3.042660,4.338636,-5.254196,-4.715799,-3.013977]],[[-3.688459,3.488840,-2.022541,-2.770103,-0.778516,2.438881,-5.486302,9.169509]],[[-9.214698,-2.704012,2.935885,0.771801,8.130579,5.380622,3.575523,7.197733]],[[1.192953,1.796954,-3.520362,8.307778,-4.324561,-1.152531,-3.828569,9.999495]],[[8.576508,-8.019734,-5.517105,-0.850957,-7.627268,7.546534,8.402717,0.542598]],[[6.845597,-5.231935,-8.700610,-1.791333,-3.457557,-2.765532,-9.987433,-9.437775]]], dtype = "float32")#candidate|2231|(7, 1, 8)|const|float32
bop_2232 = relay.minimum(var_2230.astype('float32'), relay.reshape(const_2231.astype('float32'), relay.shape_of(var_2230))) # shape=(7, 1, 8)
uop_2235 = relay.log(const_2231.astype('float32')) # shape=(7, 1, 8)
output = relay.Tuple([bop_2232,uop_2235,])
output2 = relay.Tuple([bop_2232,uop_2235,])
func_2239 = relay.Function([var_2230,], output)
mod['func_2239'] = func_2239
mod = relay.transform.InferType()(mod)
var_2240 = relay.var("var_2240", dtype = "float32", shape = (7, 1, 8))#candidate|2240|(7, 1, 8)|var|float32
output = func_2239(var_2240)
func_2241 = relay.Function([var_2240], output)
mutated_mod['func_2241'] = func_2241
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2682 = relay.var("var_2682", dtype = "float64", shape = (5, 2, 12))#candidate|2682|(5, 2, 12)|var|float64
const_2683 = relay.const([[[-6.216696,7.136975,8.904576,-2.250554,-9.714249,8.581188,5.618181,5.452740,9.156566,5.988768,-4.374288,-5.596413],[5.725073,1.587294,6.606773,5.268960,7.885651,1.754464,-9.995450,4.429475,-5.228108,8.490509,-4.704825,-9.280098]],[[2.089303,6.666205,-0.869756,-6.180734,-0.376827,6.433708,-2.401558,5.994269,2.226480,-0.152192,-1.043601,-4.097152],[7.514079,-2.443303,-1.992428,1.588423,-2.864041,9.445962,-9.032073,-2.871731,6.445257,3.737735,-0.726507,-3.106532]],[[7.732723,2.390662,-6.631430,-6.245801,8.586920,3.934355,9.651462,4.107731,8.718604,2.253537,-6.739677,-8.816576],[1.713380,8.212087,-2.702068,2.436407,6.635224,-2.890794,-4.053968,4.286405,2.647299,-3.258007,0.225828,7.858349]],[[-6.314825,0.254068,-9.558379,1.063306,4.071459,-5.621519,-6.395081,9.985268,-6.327267,0.040380,-8.798474,2.165107],[3.881751,-0.832552,2.062041,7.560938,-2.556028,5.083949,-6.412919,-7.262184,2.212369,4.166423,-9.944026,5.337221]],[[-1.467317,-6.063905,2.990776,2.048798,2.676721,-9.083755,6.834185,-6.625199,-3.171410,-2.584462,-2.898024,-4.357521],[9.301084,5.643549,-3.725981,5.321701,5.007042,7.429134,9.751895,3.960460,-2.709207,7.331924,6.681171,-6.325227]]], dtype = "float64")#candidate|2683|(5, 2, 12)|const|float64
bop_2684 = relay.floor_divide(var_2682.astype('float64'), relay.reshape(const_2683.astype('float64'), relay.shape_of(var_2682))) # shape=(5, 2, 12)
func_1053_call = mod.get_global_var('func_1053')
func_1057_call = mutated_mod.get_global_var('func_1057')
var_2698 = relay.var("var_2698", dtype = "uint16", shape = ())#candidate|2698|()|var|uint16
const_2699 = relay.const([[9,9,-3,1,-10,5,1,-1,8,6,-10,-7,-3,-1,5,10,-9,7,4,5,-10,-5],[-4,3,2,1,-8,-8,5,10,5,5,-10,7,4,-7,-2,5,-1,-8,-8,8,7,-6],[5,2,9,5,4,3,-4,2,3,2,8,8,8,3,-1,-8,9,8,1,-7,-7,-1],[-1,9,-2,9,-10,9,4,-5,-3,3,3,9,-7,9,9,5,4,-5,4,10,2,5],[-1,10,3,5,-7,2,-3,7,10,3,7,-4,-9,-6,4,-6,2,-7,1,1,-8,-1],[-3,-4,-2,8,-2,-10,-7,-5,-8,3,9,2,-4,8,-5,5,-9,10,-6,1,-3,3],[9,-2,-9,6,-7,-5,-1,-4,-4,-6,-8,6,-5,3,10,-9,-4,-4,7,10,-8,6],[-10,10,7,-6,-10,-10,9,-6,-1,-8,7,-7,-3,8,-4,3,-3,7,-8,-7,-5,-7],[10,3,-8,6,4,8,10,9,8,-7,6,3,9,4,6,-8,5,-8,4,-8,7,4],[-4,3,-8,5,6,-9,7,-7,-7,9,-8,-4,-1,1,-2,7,-9,-8,-1,-2,-2,-2],[-4,-3,-5,2,-1,6,-3,-2,-3,9,-9,10,1,-9,-2,-3,9,9,8,7,-10,-3],[-1,5,4,-7,-2,-5,8,-7,2,-9,4,4,9,-1,-6,3,-9,-3,-4,-8,-7,1],[-4,6,-8,4,2,6,-1,2,3,-5,4,7,-10,6,5,-3,-8,2,5,-10,6,-10],[-4,4,-8,10,-9,-9,10,-6,-3,-4,9,6,4,3,-3,8,-7,-5,-3,8,3,-1],[-5,10,6,-8,9,-1,2,-2,-6,2,-3,10,-5,-8,-6,-3,-5,-6,6,8,-9,-8],[-2,8,3,3,9,3,-10,4,9,-6,10,-7,-7,10,3,-9,-10,-5,8,-10,1,-3],[-4,8,4,-10,-5,9,-2,-10,-10,-10,-7,-5,2,6,-9,-6,-7,8,8,6,-5,-5],[-5,-3,-7,5,-7,1,-8,-5,-7,1,3,5,-9,5,5,2,9,5,8,10,-4,5],[9,10,10,9,-3,7,3,-10,3,8,-7,8,5,-3,2,-1,-7,-6,-4,-2,-7,-1],[-2,9,-2,9,-2,-7,8,7,7,10,1,-2,-3,2,-5,2,-5,-3,10,6,-1,-2],[-4,-7,-9,6,-5,4,5,9,10,-7,4,2,2,-7,-5,-1,8,-10,7,6,4,-1],[8,1,1,3,-8,9,-6,-2,-5,-10,1,7,-3,1,3,-8,-3,-8,-7,-10,-7,4],[5,-4,8,-1,-3,-8,-1,6,2,4,-5,10,3,-6,8,6,3,-4,-6,-10,5,-5],[-7,-4,-5,4,1,1,-3,6,4,-5,-4,9,-7,-8,9,1,-4,-6,-3,10,-4,8],[7,-1,8,9,-6,-3,-9,5,6,-5,3,1,2,10,2,5,1,-10,1,-2,-10,-10],[-6,9,1,4,7,-9,-9,-5,6,2,-4,-8,-4,2,5,-4,-6,-5,-9,2,6,-3],[2,-6,9,-10,2,8,8,9,3,-6,-8,-8,10,3,3,1,-5,6,6,-7,-5,6],[6,-9,-1,-9,-8,6,-9,3,4,-9,-2,-2,-2,9,-5,-3,10,-3,-8,10,9,3],[-4,2,-4,-6,8,5,1,9,8,-9,5,9,-4,9,-4,3,-1,-5,-6,1,1,7],[-1,7,10,2,-10,9,10,7,-2,-4,-5,-10,-10,-6,9,4,-2,3,-9,-9,6,2],[8,3,-2,-5,-4,10,7,6,9,-10,-2,-5,8,1,2,1,5,-9,9,-5,-10,8],[1,5,-5,-3,8,10,-9,-9,6,-10,3,1,-5,4,1,7,7,4,-7,-3,-6,-10],[-5,8,8,-6,7,-3,-2,-2,-1,7,-10,-4,-9,-1,-9,9,-1,-9,3,2,-1,-6],[3,5,4,-6,2,-1,-6,-3,-7,-2,7,1,-5,4,9,-8,-6,8,7,-6,3,-2],[-2,-5,7,-7,-7,8,1,-7,-10,5,-9,7,9,7,-1,-1,3,-1,-3,9,-9,3],[9,-2,-6,6,-10,-3,8,-10,-10,3,-1,6,-7,6,-3,7,1,-10,6,4,1,-6],[-1,10,-9,5,-1,4,9,3,-10,-2,10,8,10,-4,1,-1,-6,4,-8,-7,-3,7],[2,-1,-2,3,-7,-8,5,1,1,10,5,-3,4,-1,1,-8,10,5,-4,-6,1,9],[5,2,4,-3,8,3,6,-1,-4,9,-10,-7,-5,7,-6,-2,8,7,7,-10,-6,7],[9,-6,-8,-6,-3,3,6,4,8,-3,1,10,-1,-5,5,6,1,-6,1,7,7,-2]], dtype = "uint16")#candidate|2699|(40, 22)|const|uint16
call_2697 = relay.TupleGetItem(func_1053_call(relay.reshape(var_2698.astype('uint16'), []), relay.reshape(const_2699.astype('uint16'), [11, 16, 5]), ), 3)
call_2700 = relay.TupleGetItem(func_1057_call(relay.reshape(var_2698.astype('uint16'), []), relay.reshape(const_2699.astype('uint16'), [11, 16, 5]), ), 3)
bop_2701 = relay.left_shift(const_2699.astype('int64'), var_2698.astype('int64')) # shape=(40, 22)
uop_2715 = relay.acosh(const_2683.astype('float64')) # shape=(5, 2, 12)
output = relay.Tuple([bop_2684,call_2697,bop_2701,uop_2715,])
output2 = relay.Tuple([bop_2684,call_2700,bop_2701,uop_2715,])
func_2722 = relay.Function([var_2682,var_2698,], output)
mod['func_2722'] = func_2722
mod = relay.transform.InferType()(mod)
mutated_mod['func_2722'] = func_2722
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2722_call = mutated_mod.get_global_var('func_2722')
var_2724 = relay.var("var_2724", dtype = "float64", shape = (5, 2, 12))#candidate|2724|(5, 2, 12)|var|float64
var_2725 = relay.var("var_2725", dtype = "uint16", shape = ())#candidate|2725|()|var|uint16
call_2723 = func_2722_call(var_2724,var_2725,)
output = call_2723
func_2726 = relay.Function([var_2724,var_2725,], output)
mutated_mod['func_2726'] = func_2726
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2764 = relay.var("var_2764", dtype = "float64", shape = (6, 15, 2))#candidate|2764|(6, 15, 2)|var|float64
uop_2765 = relay.cosh(var_2764.astype('float64')) # shape=(6, 15, 2)
output = uop_2765
output2 = uop_2765
func_2768 = relay.Function([var_2764,], output)
mod['func_2768'] = func_2768
mod = relay.transform.InferType()(mod)
mutated_mod['func_2768'] = func_2768
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2769 = relay.var("var_2769", dtype = "float64", shape = (6, 15, 2))#candidate|2769|(6, 15, 2)|var|float64
func_2768_call = mutated_mod.get_global_var('func_2768')
call_2770 = func_2768_call(var_2769)
output = call_2770
func_2771 = relay.Function([var_2769], output)
mutated_mod['func_2771'] = func_2771
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2884 = relay.var("var_2884", dtype = "int16", shape = (11, 10, 14))#candidate|2884|(11, 10, 14)|var|int16
const_2885 = relay.const([[[-6,-4,1,4,-1,-8,7,6,8,2,-6,8,1,-3],[10,7,-10,-2,10,8,-5,6,2,-3,-9,10,9,5],[1,-1,1,-9,-8,3,7,1,-8,3,8,2,-2,-5],[2,1,5,-8,-1,-1,-8,-6,6,6,-4,-5,6,2],[-10,10,-6,-9,4,-9,-2,3,5,-4,9,-4,-10,7],[-6,5,5,-2,-8,-2,-6,-9,-3,10,-2,-8,6,-3],[-3,-2,9,-9,-5,-3,-9,9,-10,-6,1,-1,-10,-5],[3,3,-10,6,-4,-2,-3,-6,-4,10,3,4,-1,10],[-4,-8,-5,-2,5,2,3,10,3,-10,1,8,5,-10],[7,-8,5,7,-4,-2,-6,-10,-10,-7,-8,-9,-7,3]],[[-9,8,2,-8,-1,-4,-3,-6,3,-10,-8,-8,-1,3],[4,-2,10,-10,10,-9,2,-6,2,-5,-7,9,-9,-10],[-4,2,1,-8,8,3,-7,-6,6,5,3,-4,-5,6],[2,8,-2,-1,-4,6,-8,-9,1,-3,9,-8,9,5],[-7,-10,10,4,-8,-7,-5,-6,1,-9,3,3,1,6],[-5,6,3,-2,5,5,10,-8,4,-9,1,9,-9,6],[4,-2,3,1,-5,9,7,-3,-5,-4,-5,3,-1,10],[5,-2,7,5,3,6,-7,7,-8,-2,1,3,9,4],[10,-9,-9,1,-6,-6,4,-6,6,6,-6,-8,-6,-5],[-8,-4,2,-3,-6,-8,3,-9,7,-8,3,-8,4,-5]],[[10,-7,8,9,5,-2,-6,-3,-6,8,10,-8,-1,1],[4,-6,-6,5,4,-8,3,2,-10,-2,7,-10,5,-9],[4,-2,6,7,10,-7,-3,3,-5,-7,10,-1,-9,-4],[-9,-3,-1,-5,10,8,-1,2,2,-2,-2,1,-10,7],[-1,6,-3,5,1,-10,2,-2,-5,-9,-2,3,9,6],[-4,1,-5,7,5,2,4,10,2,-8,-6,5,5,-4],[9,6,-2,-1,3,4,2,7,-10,1,-6,-10,-8,-2],[2,-9,-5,-6,-3,3,7,-5,5,-8,-8,-6,9,-9],[-8,2,-9,1,-8,-3,6,-7,5,-5,-4,3,1,6],[-5,7,-10,-5,1,-2,-5,-8,-1,5,6,6,2,-2]],[[1,2,-7,-1,-1,-5,-2,-9,-2,-9,3,2,-3,-1],[-10,-9,3,6,4,6,-6,6,-7,-7,4,-5,10,-6],[6,10,-10,-6,2,-4,1,-10,10,5,2,10,5,-5],[-3,-8,8,-4,8,-3,1,-7,-9,9,4,9,-5,-4],[-6,-7,-9,9,-4,-8,-2,3,10,8,-6,1,3,5],[-8,-8,5,-3,-2,-2,5,9,2,-1,-1,-4,-5,6],[-4,6,10,-8,1,9,-6,-10,-2,-8,-10,-1,-9,-9],[-9,-4,5,-4,-6,-2,-4,10,6,10,-8,4,-9,-10],[-9,3,-5,-8,-7,-7,-7,-9,2,10,9,5,10,7],[4,6,-8,1,5,6,-4,-4,4,3,-3,5,4,-9]],[[-1,4,4,9,2,-7,-9,-1,-8,5,8,-1,2,-3],[7,-3,-8,4,-8,6,-4,6,-8,8,2,1,3,1],[9,2,-5,2,1,-5,-10,-10,6,8,3,-3,3,-6],[-7,2,10,9,8,-7,1,9,-5,-6,4,-8,-3,-5],[6,-1,-6,-8,-8,2,-2,6,-2,-5,-5,-1,-6,-10],[-9,-5,4,-9,-10,9,-6,3,-1,-9,5,2,-6,1],[-2,-3,3,8,-4,10,-4,2,-1,5,-4,-4,10,-9],[9,-8,-8,-1,-1,-2,6,8,2,-9,5,-4,-10,-7],[4,-7,-5,-3,-8,-6,5,-3,-10,2,-3,5,-7,-8],[-5,7,3,2,9,-1,-2,-3,4,10,6,-6,-5,8]],[[7,-10,3,4,1,3,3,-6,-10,-4,4,-8,7,1],[4,5,5,8,3,3,-9,-6,10,-9,-1,-7,-6,7],[-9,-5,-8,-4,4,-1,3,-2,10,-7,10,-3,9,-7],[-4,-6,3,-6,2,1,4,-4,6,1,6,10,-4,-6],[-2,-5,7,1,-5,-8,9,-4,3,-9,-5,-7,-10,4],[10,4,3,2,5,10,10,-8,7,-1,-9,1,3,-5],[-7,-5,-1,10,-2,-5,-6,8,3,7,7,2,8,-2],[-3,2,-7,8,-9,5,-3,-10,-5,6,-4,10,9,-1],[-5,-8,9,-10,-10,-8,7,10,-6,-8,9,-1,-7,8],[2,4,2,8,3,-2,4,-4,5,-10,4,-6,-2,-10]],[[7,-6,7,8,2,-3,-4,2,6,1,-9,4,9,-8],[6,-1,-8,-2,6,6,-8,5,-5,1,2,-5,-3,4],[-9,-2,-4,8,9,-9,-1,-3,6,-10,8,4,-3,10],[-6,-9,-9,-9,-5,5,6,9,8,4,-3,-7,-8,-10],[10,9,4,-10,-9,8,-6,8,-6,9,10,-10,-10,1],[-9,-8,-10,-4,3,9,-5,-5,-7,-4,9,-9,-9,-1],[7,6,4,-3,-1,9,3,7,3,10,7,5,9,5],[2,-6,8,4,-6,-6,-6,-4,-1,8,4,-5,1,-5],[5,-8,-5,-7,6,5,-10,10,4,-6,6,-10,-1,-9],[7,5,-3,-1,7,1,9,5,5,-7,1,5,-9,-8]],[[-1,5,1,2,-2,4,10,1,1,9,5,-6,-1,-6],[7,-1,10,-8,5,-9,-2,-4,-10,2,-3,1,8,6],[8,10,-5,4,4,-6,-4,5,10,8,4,-3,-4,-9],[-2,2,7,5,-2,7,5,-6,-10,4,-10,-10,-4,-3],[7,-1,-7,9,8,5,-7,7,-8,10,3,8,6,-10],[-2,1,5,8,-6,7,1,3,8,7,-4,-6,10,-2],[3,-9,5,4,-3,-3,7,4,-5,5,10,9,-10,-2],[-8,-9,4,-6,9,10,-4,2,4,1,-4,1,10,-7],[-5,-3,1,4,9,6,-1,9,-1,9,6,5,8,-3],[5,1,6,3,-5,5,-6,-1,9,-4,-10,6,-3,-7]],[[6,-9,7,-3,5,2,-10,5,10,-4,-7,-9,-1,4],[-5,-5,10,-4,-8,-4,2,5,3,-9,-6,-3,-1,-10],[7,-6,-7,-3,-7,-8,3,-5,5,6,-10,2,8,-8],[10,-1,4,-9,-8,-9,-1,-7,-6,9,2,3,10,7],[3,-9,3,-9,-7,9,-3,8,7,10,8,9,7,-4],[-7,7,6,10,3,-10,10,-4,10,-8,-7,-2,-10,-9],[-1,3,3,8,3,-3,-9,-9,-2,1,4,1,-10,10],[-4,-6,-1,-4,1,8,-2,-2,-3,10,-3,9,2,3],[-5,-1,-2,-7,-10,-7,-5,-6,-7,-9,-9,-8,-10,2],[-9,4,-9,-4,-4,2,-1,4,8,-2,10,5,-10,4]],[[10,-4,2,-4,4,2,8,-3,-6,7,-9,-7,10,-8],[5,-2,9,-3,-5,4,6,7,-9,-4,-7,9,10,5],[-7,2,-5,6,-2,7,-7,-5,6,-6,-2,1,1,-3],[5,-1,-1,4,-9,1,9,-9,10,9,7,4,8,-7],[5,-10,-10,-3,-5,-8,-7,-6,-1,-3,10,-9,-9,-6],[-8,6,5,-2,-10,-7,-1,-1,-7,5,3,-9,9,-10],[10,-5,-9,10,10,10,-8,-5,5,7,5,8,-9,-3],[-6,9,8,-4,9,-2,5,-9,10,-2,-1,7,-1,4],[-3,-2,-1,-4,-7,8,2,4,-4,2,6,9,3,3],[-2,-5,5,5,-10,-5,-7,4,-4,7,-1,2,-3,7]],[[8,9,9,6,-3,10,-9,-10,-7,-4,-3,9,-9,3],[3,-7,2,-2,2,-6,10,-8,-2,-5,-3,2,-1,-1],[-1,4,8,6,7,-2,-9,-6,6,-7,-2,-9,-1,-2],[3,5,-2,9,-8,10,6,-6,4,-1,-4,1,1,3],[-3,6,-10,2,-8,2,8,3,5,9,1,-10,-10,-5],[2,-5,-4,-5,-2,8,7,-7,-3,-3,2,-8,3,10],[-2,6,-4,1,2,4,-2,-3,2,8,-2,6,2,-9],[-3,-8,-5,-10,-5,-4,-6,10,-1,-9,-3,-10,7,-9],[9,1,6,-8,-6,-7,-1,8,9,7,1,5,-2,-10],[-9,7,-6,4,8,2,-10,4,10,-9,2,-1,2,8]]], dtype = "int16")#candidate|2885|(11, 10, 14)|const|int16
bop_2886 = relay.greater_equal(var_2884.astype('bool'), relay.reshape(const_2885.astype('bool'), relay.shape_of(var_2884))) # shape=(11, 10, 14)
func_818_call = mod.get_global_var('func_818')
func_822_call = mutated_mod.get_global_var('func_822')
var_2893 = relay.var("var_2893", dtype = "int64", shape = (364,))#candidate|2893|(364,)|var|int64
call_2892 = relay.TupleGetItem(func_818_call(relay.reshape(var_2893.astype('int64'), [4, 13, 7]), relay.reshape(var_2893.astype('int64'), [4, 13, 7]), ), 0)
call_2894 = relay.TupleGetItem(func_822_call(relay.reshape(var_2893.astype('int64'), [4, 13, 7]), relay.reshape(var_2893.astype('int64'), [4, 13, 7]), ), 0)
bop_2901 = relay.subtract(var_2884.astype('uint16'), relay.reshape(const_2885.astype('uint16'), relay.shape_of(var_2884))) # shape=(11, 10, 14)
output = relay.Tuple([bop_2886,call_2892,var_2893,bop_2901,])
output2 = relay.Tuple([bop_2886,call_2894,var_2893,bop_2901,])
func_2907 = relay.Function([var_2884,var_2893,], output)
mod['func_2907'] = func_2907
mod = relay.transform.InferType()(mod)
mutated_mod['func_2907'] = func_2907
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2907_call = mutated_mod.get_global_var('func_2907')
var_2909 = relay.var("var_2909", dtype = "int16", shape = (11, 10, 14))#candidate|2909|(11, 10, 14)|var|int16
var_2910 = relay.var("var_2910", dtype = "int64", shape = (364,))#candidate|2910|(364,)|var|int64
call_2908 = func_2907_call(var_2909,var_2910,)
output = call_2908
func_2911 = relay.Function([var_2909,var_2910,], output)
mutated_mod['func_2911'] = func_2911
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2998 = relay.var("var_2998", dtype = "uint64", shape = (5, 10, 2))#candidate|2998|(5, 10, 2)|var|uint64
const_2999 = relay.const([[[1,4],[4,9],[-7,-4],[-9,8],[9,-10],[7,9],[-6,-10],[9,-8],[-8,8],[-10,-2]],[[10,-6],[10,-4],[-8,-7],[8,10],[10,4],[-4,2],[5,-1],[-6,3],[-9,-7],[-3,-2]],[[-5,-5],[-7,-1],[-7,-8],[9,2],[-1,10],[8,-7],[2,-7],[-7,7],[8,-9],[9,1]],[[4,6],[1,-7],[2,2],[-1,-6],[5,8],[-2,3],[9,6],[1,3],[-9,9],[8,4]],[[3,10],[7,7],[-9,3],[1,1],[10,-7],[7,6],[-2,7],[1,2],[1,10],[-7,-1]]], dtype = "uint64")#candidate|2999|(5, 10, 2)|const|uint64
bop_3000 = relay.less(var_2998.astype('bool'), relay.reshape(const_2999.astype('bool'), relay.shape_of(var_2998))) # shape=(5, 10, 2)
func_818_call = mod.get_global_var('func_818')
func_822_call = mutated_mod.get_global_var('func_822')
const_3017 = relay.const([7,-2,-7,3,8,4,-2,6,2,9,10,-1,-5,-7,7,-7,5,-1,8,8,8,10,4,1,3,3,-8,-8,-1,9,10,-2,-9,1,-7,-5,-1,-8,-2,3,9,-9,-2,-9,3,-3,-7,-9,-10,-4,-9,3,-4,7,9,3,7,6,-10,-2,-4,7,-2,8,9,10,-10,10,-3,4,-6,-10,9,-2,-1,-2,-1,-8,7,6,9,4,8,-5,-2,3,-6,-2,-10,-5,-3,8,8,-9,-4,-1,-9,-4,10,8,-10,9,-5,-4,7,6,8,4,-3,-3,7,10,8,5,-5,9,3,1,8,2,5,-7,-5,-1,5,-3,-7,-10,-9,4,-5,7,-10,5,6,-5,-7,-5,3,-9,1,1,-7,4,4,-9,-10,7,7,-6,-1,-5,3,-1,8,-3,3,7,-4,7,-1,-7,5,9,-7,-4,-7,-9,8,7,1,5,5,-8,-6,-7,3,6,-7,7,-9,4,-1,6,-2,-7,4,-7,-5,6,-1,-6,6,-10,6,-8,-10,1,-5,1,10,8,-10,-1,-1,-8,-3,-7,-8,-3,-4,-9,3,-8,-7,-6,8,10,-1,5,-1,6,-7,2,-8,10,-8,-10,9,1,-6,-2,3,4,-7,7,2,-4,6,4,3,-10,3,5,-6,7,-3,8,-4,-1,-9,-1,-4,2,10,-6,10,-5,-3,-6,-7,3,-1,-8,-1,-6,-7,-3,-1,-1,-1,-6,-2,-5,-3,6,-3,4,9,-10,10,3,4,-10,-1,8,9,-4,-6,6,1,1,-10,-9,-6,-9,9,-8,10,-8,3,4,9,-3,-8,-6,10,4,-4,-6,3,9,-9,-7,-6,-9,-10,-1,2,7,2,8,3,-9,-6,7,4,3,4,-2,4,1,6,-6,3,-8,-9,6,-2,-6,2,10,-9,9,5,-4,-7,-7,-7,3,8,-7,-10,6,-8,10,8,-5,-5,10,10,-10,-1,1], dtype = "int64")#candidate|3017|(364,)|const|int64
call_3016 = relay.TupleGetItem(func_818_call(relay.reshape(const_3017.astype('int64'), [4, 13, 7]), relay.reshape(const_3017.astype('int64'), [4, 13, 7]), ), 0)
call_3018 = relay.TupleGetItem(func_822_call(relay.reshape(const_3017.astype('int64'), [4, 13, 7]), relay.reshape(const_3017.astype('int64'), [4, 13, 7]), ), 0)
uop_3019 = relay.asinh(bop_3000.astype('float64')) # shape=(5, 10, 2)
bop_3021 = relay.greater_equal(uop_3019.astype('bool'), relay.reshape(var_2998.astype('bool'), relay.shape_of(uop_3019))) # shape=(5, 10, 2)
output = relay.Tuple([call_3016,const_3017,bop_3021,])
output2 = relay.Tuple([call_3018,const_3017,bop_3021,])
func_3042 = relay.Function([var_2998,], output)
mod['func_3042'] = func_3042
mod = relay.transform.InferType()(mod)
var_3043 = relay.var("var_3043", dtype = "uint64", shape = (5, 10, 2))#candidate|3043|(5, 10, 2)|var|uint64
output = func_3042(var_3043)
func_3044 = relay.Function([var_3043], output)
mutated_mod['func_3044'] = func_3044
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3080 = relay.var("var_3080", dtype = "float32", shape = ())#candidate|3080|()|var|float32
var_3081 = relay.var("var_3081", dtype = "float32", shape = (11, 6, 1))#candidate|3081|(11, 6, 1)|var|float32
bop_3082 = relay.floor_divide(var_3080.astype('float32'), var_3081.astype('float32')) # shape=(11, 6, 1)
output = relay.Tuple([bop_3082,])
output2 = relay.Tuple([bop_3082,])
func_3087 = relay.Function([var_3080,var_3081,], output)
mod['func_3087'] = func_3087
mod = relay.transform.InferType()(mod)
var_3088 = relay.var("var_3088", dtype = "float32", shape = ())#candidate|3088|()|var|float32
var_3089 = relay.var("var_3089", dtype = "float32", shape = (11, 6, 1))#candidate|3089|(11, 6, 1)|var|float32
output = func_3087(var_3088,var_3089,)
func_3090 = relay.Function([var_3088,var_3089,], output)
mutated_mod['func_3090'] = func_3090
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3180 = relay.var("var_3180", dtype = "int32", shape = (11, 16, 12))#candidate|3180|(11, 16, 12)|var|int32
const_3181 = relay.const([[[2,10,-9,-8,7,10,-9,-6,10,-2,-10,5],[4,-3,4,-6,-3,2,-5,2,10,-7,-2,-1],[-6,3,-9,1,8,8,9,10,-10,-3,-3,-8],[-5,-1,7,3,-2,3,-5,-7,-2,6,-10,-1],[-9,7,9,6,-10,5,8,5,4,-3,4,-3],[8,-8,-6,-9,5,-8,1,10,-10,3,3,-9],[-7,8,-4,-10,10,1,6,2,5,-8,5,-10],[-5,4,2,-6,6,2,5,-4,-9,9,-4,9],[-1,8,6,-3,-4,8,-8,4,-8,-6,8,6],[-5,-5,7,10,2,6,-9,-9,-3,8,-3,7],[-9,-4,5,6,-4,2,-8,1,-2,10,-5,-4],[-7,-10,-5,2,2,-2,-4,8,1,3,-2,-9],[-1,-8,7,-5,-4,-3,-3,-10,-10,3,-1,6],[-1,-1,-1,-9,-9,-9,9,-1,10,-10,10,8],[-4,-6,4,-9,10,9,-2,6,-7,10,-10,9],[-4,2,10,-5,-3,-1,2,-3,2,4,2,7]],[[-4,5,5,-3,-2,-4,7,7,8,-8,-8,3],[-2,-3,-6,4,-7,-5,3,-3,4,-7,7,-2],[4,7,10,-1,8,7,-4,7,7,6,-1,5],[6,-10,-8,8,-2,-3,5,-5,7,9,2,-5],[-8,-1,9,6,-9,-6,9,-8,-9,5,4,8],[-3,-5,3,-6,-2,-1,2,-6,-4,-8,6,-5],[-7,-2,-2,4,-9,10,10,2,4,3,-1,-9],[-9,9,4,-4,-6,-4,7,4,5,-8,2,7],[3,4,-6,10,-9,-5,-3,-6,5,7,-7,8],[5,-9,7,-4,5,-4,-8,-8,-3,4,10,-5],[9,7,-5,8,-2,-8,2,-1,10,7,2,-7],[-8,1,10,-5,1,2,8,5,-6,10,7,-4],[7,-4,-7,-3,1,-5,3,-7,1,-10,1,10],[10,-5,1,1,9,8,6,10,-9,-6,4,-7],[-3,3,-2,-3,-5,9,-6,-6,6,2,7,-9],[9,-9,9,10,-4,-7,-8,-9,9,-8,10,3]],[[-8,-10,-8,-1,4,-4,9,6,6,10,-4,-6],[-8,-9,6,6,6,9,5,-5,-2,-4,10,4],[3,-10,2,-1,10,-1,-1,-2,-3,3,3,-8],[4,7,2,-1,-3,2,-9,-8,-3,7,5,1],[2,-9,1,-9,-9,-2,-8,-6,4,-10,10,-3],[-6,9,2,3,-3,7,10,-10,6,2,4,7],[-5,-2,5,-2,-8,4,10,-3,8,8,8,8],[1,-8,-7,7,-1,1,-6,7,-3,-3,-8,7],[-8,5,6,-2,5,-3,4,-6,-9,-1,9,9],[8,-4,-10,-4,5,-6,5,7,-7,-10,-10,-8],[-3,-4,-6,2,-8,-2,-7,-9,-8,-3,-3,10],[-3,-1,-7,2,7,-2,-2,10,-1,10,-1,-2],[4,-9,-8,-6,-1,3,-5,10,4,6,-8,-6],[1,9,-3,-10,-6,5,-9,-2,8,-8,2,-7],[-10,2,1,9,2,-3,-8,-3,1,-6,-8,1],[-6,9,7,-4,-8,6,-2,1,-2,-2,-7,-5]],[[-4,-1,1,-6,-10,-7,-10,-5,7,6,-6,-7],[1,-1,4,-9,6,1,-1,-8,-2,6,-8,-8],[2,-6,3,1,5,-6,-7,-7,4,-2,-5,-6],[5,-8,-4,-8,4,-9,1,3,-9,3,4,8],[-10,-5,-3,3,-4,1,-9,6,-6,10,-4,-1],[4,8,-8,7,1,2,-2,1,5,-6,4,-8],[7,-6,-1,-2,3,-2,-10,-8,1,-4,6,-1],[-9,7,-8,-2,1,4,6,-8,9,9,-8,-8],[-6,4,-10,-3,3,-2,3,6,3,9,-7,8],[4,5,2,-3,-8,10,-5,6,-3,10,10,3],[7,3,-6,10,-8,-5,8,9,-4,-3,4,-8],[-6,6,-4,1,8,5,-7,-7,2,5,10,8],[-5,-5,-10,7,-9,6,-1,-5,5,6,-7,-4],[4,10,3,8,-1,-8,-3,-9,-9,8,-3,10],[4,-9,8,-1,5,8,1,6,8,3,1,6],[6,-2,6,9,8,1,3,10,-5,-6,4,-6]],[[-9,4,10,2,5,-9,5,-10,-7,-1,-5,10],[9,8,-9,-6,3,8,1,1,3,-6,9,-1],[7,9,-3,3,5,5,-6,-2,-10,-4,10,8],[7,-10,-10,-3,3,10,-10,-7,-6,1,-1,3],[-3,6,-6,7,-8,10,-9,4,6,9,-9,-3],[7,7,6,1,10,-5,10,8,10,-6,2,3],[6,-3,6,-9,1,1,7,7,9,-4,5,-9],[-1,-3,4,10,-10,4,1,1,1,-7,5,-10],[7,5,5,6,6,-8,9,-2,-10,-5,4,-3],[9,7,-8,-10,8,-9,-7,10,6,8,5,2],[-10,10,-6,-9,3,-1,-3,-5,6,4,9,-1],[-4,-8,-10,-6,-1,4,-9,2,-1,2,6,4],[3,9,4,7,-10,-6,-7,-1,-1,6,10,-2],[5,-4,3,-6,6,8,-7,7,-8,-8,-7,5],[-5,-6,3,3,-3,-8,5,-3,-9,-10,-4,4],[9,-10,2,-4,8,-10,-9,-6,2,-9,10,-5]],[[-4,7,-3,1,4,10,-7,-1,-6,6,5,-8],[-10,3,2,10,4,-4,-8,-1,-6,-8,-5,10],[3,-7,-7,-5,-3,-6,-8,-10,4,9,7,-6],[-1,8,5,-7,3,7,10,-9,-2,-7,1,-3],[1,7,-4,-5,-9,-2,10,-3,5,2,-5,8],[6,-8,-5,2,-2,6,-3,-2,-3,-9,4,-5],[-3,2,-8,5,-6,-2,5,6,4,5,2,-2],[-10,7,2,-10,-9,-2,5,-2,2,1,-6,7],[1,-9,-9,-10,-1,-2,-9,9,7,4,1,-2],[-7,-2,-1,5,3,9,-7,9,-5,1,5,1],[-1,3,-10,7,-9,-2,-10,-6,-3,2,-3,-7],[4,-2,8,-3,10,-3,3,8,10,4,-9,2],[-5,-3,9,-7,-8,4,-4,-6,-4,-5,-6,-3],[-6,-6,-7,-8,-5,1,1,-9,-8,-6,1,-7],[9,-6,-8,3,5,-1,-10,-5,10,-10,-3,-1],[-3,3,6,-1,-5,-2,-5,7,6,4,-6,4]],[[-4,-8,-5,-8,-5,4,-3,8,1,1,7,-8],[5,-3,-1,-9,-1,-4,10,-7,-2,-8,-6,-3],[10,-7,-1,4,-6,-8,-1,-2,6,1,5,-2],[-8,4,-1,-3,8,-10,4,4,8,-5,-1,-3],[2,-4,1,5,-8,-5,5,-8,7,-3,-1,-9],[9,9,-2,8,8,10,-7,1,2,-2,4,-10],[-9,2,-10,-10,6,10,2,9,-9,9,1,-9],[6,2,3,-8,6,4,-10,6,4,3,5,7],[-10,10,-6,6,2,1,1,10,1,3,10,9],[-7,-1,-4,-6,7,-6,5,-7,2,-2,9,-8],[8,4,-3,4,-5,10,-5,4,2,-7,1,-2],[1,-4,8,3,-5,5,-9,-8,8,-4,4,-5],[7,3,-5,1,-1,-8,-8,4,-9,-3,-10,5],[-9,-10,-8,-9,-8,-4,-9,1,-9,6,2,-3],[3,-1,5,10,6,6,9,-10,-10,-2,-7,-9],[-1,-6,-9,6,-4,-4,3,-2,-5,3,-6,1]],[[-7,-6,-3,3,-4,-1,-7,-2,3,10,9,5],[2,8,-2,5,9,6,-10,9,7,4,4,4],[3,5,6,8,9,6,-2,-5,-4,-4,-9,8],[-1,-1,-2,4,7,-9,-1,-10,10,4,-7,-2],[1,7,9,7,2,6,-2,-1,-2,-3,5,5],[-7,9,7,9,9,9,3,-7,3,1,6,6],[2,2,1,5,6,4,-5,-3,-8,4,6,8],[-7,-7,-3,-2,10,-2,-9,9,-1,9,5,-4],[-2,-6,-10,-10,-5,9,-9,3,-4,10,-2,-9],[5,2,-9,5,-3,-2,7,-9,10,-2,-8,8],[-10,7,9,-8,3,-4,-6,-6,10,-1,3,-1],[9,-1,10,1,8,-3,-4,-1,3,-1,-4,8],[-8,-3,9,3,-1,7,2,1,-5,-6,7,8],[-3,-7,-6,3,3,5,3,-2,-10,4,-8,-1],[9,-4,7,4,-8,8,-5,-10,-8,10,2,-4],[2,6,2,3,-7,8,8,3,-3,4,2,6]],[[-8,1,-10,-4,-4,-4,-8,-8,5,-8,-7,1],[-3,-8,8,9,2,-5,7,-7,-10,9,-8,-2],[2,6,-2,-9,-1,-4,-3,-4,-10,-9,10,10],[-7,-7,-6,7,-8,9,-1,7,-9,10,1,-7],[7,-10,2,-9,8,3,5,-6,-5,5,5,-8],[2,-6,-6,-3,-9,-1,4,-1,8,-10,5,5],[1,8,1,-8,-7,-3,-7,7,-3,8,-10,2],[4,10,8,-1,-5,-2,-6,7,-7,6,9,2],[4,9,-1,-4,5,-4,1,-9,-4,-3,5,4],[2,-8,5,-3,1,7,-7,7,-8,4,-6,-6],[-5,-5,-10,-4,10,5,3,-8,-2,-8,-7,10],[8,5,-6,-6,-1,-3,9,5,-1,-7,-10,1],[-2,-10,6,6,-3,-7,3,2,-6,7,2,7],[4,-8,-2,6,-9,-3,-8,8,10,-2,1,-7],[1,-4,-9,8,6,-8,6,2,-10,-10,-6,2],[6,-8,-10,-3,2,5,10,-3,-9,5,-4,-9]],[[-4,5,-7,-5,-2,9,-10,2,2,3,9,8],[-8,-3,2,9,1,3,2,3,2,6,8,6],[-3,2,5,-2,-5,-7,7,2,-1,-9,4,5],[-8,8,8,6,2,-5,-9,2,-2,-10,5,8],[-8,9,1,-6,4,2,7,-5,-5,-6,9,-8],[-8,-1,-2,-9,8,-10,1,-7,-1,8,7,9],[-4,-8,-4,4,-5,-5,6,7,1,2,-5,-8],[7,6,-9,-8,1,-6,2,-7,6,6,-5,5],[-10,7,-5,-2,10,6,5,2,2,9,9,5],[-7,9,-3,7,1,-1,-8,7,-2,-9,1,-1],[1,-10,-5,8,-5,-3,1,-4,-3,-9,7,-2],[2,-4,-3,7,6,-6,2,2,-3,8,6,-6],[-8,-1,-2,-3,-4,-7,-3,-5,-2,9,-5,5],[-7,-3,6,1,6,-6,7,-3,8,10,-4,10],[5,4,-2,9,-2,10,2,10,5,6,-9,3],[-1,-1,-9,3,-2,-4,-5,-2,5,-5,-5,-7]],[[-2,10,-4,-9,7,1,2,-8,2,9,-8,4],[-4,2,-5,2,4,9,5,2,-1,-8,9,-7],[9,-8,-8,-10,-1,-4,1,-4,-7,2,4,-6],[9,7,-9,6,-10,-4,-7,1,-9,4,10,-5],[-4,1,-3,2,8,-9,-2,6,9,10,-6,-6],[7,-5,10,6,-6,-2,1,-10,-1,-7,-4,-7],[-4,-9,-10,-5,6,4,7,2,6,-2,-7,-9],[9,-3,10,6,-9,-4,1,-3,-7,-5,-10,10],[2,-4,-4,1,-10,8,6,-6,10,-1,-7,-2],[-5,3,-5,-1,4,-9,-10,-6,5,-10,10,6],[-6,-3,-3,-1,3,4,-6,-6,-10,-1,-3,1],[-10,9,-9,-10,-3,-9,-9,5,-2,-9,-5,9],[7,-6,-6,10,-1,6,5,-4,8,-5,6,6],[-10,-8,-9,10,8,10,-6,10,1,-7,3,-5],[7,-7,-9,-10,-9,3,5,5,3,7,-6,-5],[4,-1,5,7,5,4,-8,-2,3,4,3,1]]], dtype = "int32")#candidate|3181|(11, 16, 12)|const|int32
bop_3182 = relay.bitwise_and(var_3180.astype('int32'), relay.reshape(const_3181.astype('int32'), relay.shape_of(var_3180))) # shape=(11, 16, 12)
func_1484_call = mod.get_global_var('func_1484')
func_1488_call = mutated_mod.get_global_var('func_1488')
const_3209 = relay.const([[-9.487269,4.401241,0.591299,-9.724839,-2.946280,2.694849,0.064972,4.259278,7.031888,4.896619,5.976131,-0.478969,1.592623,5.690540,0.546754,-1.431253,2.493895,-1.557135,-4.385240,2.773467,4.989979,8.729961,0.717540,1.587104,9.411649,-2.664691,-6.196701,-2.226509,0.040056,3.773991,4.339157,-4.329690,-6.522708,8.009384,2.755489,7.836928,8.159782,9.493279,6.845599,0.162093,7.755545,0.810392,-4.953419,-9.425748,-1.370590,0.017994,2.254626,-5.387079,-5.066559,9.893435,-7.161532,6.764389,4.284169,-3.205906,4.482099,-6.914725,-2.684944,-7.024882,5.762123,-8.549007,-5.038164,2.553976,0.016201,7.582169,8.464333,5.874446,3.189324,4.384741,7.801602,6.798760,-2.042743,-8.350273,-4.782067,5.107035,6.724415,1.873208,2.280775,5.184890,-3.430473,6.806043,0.586065,-1.782877,7.555994,-5.563999,5.179234,7.757906,7.573759,-6.005295,-4.853651,1.871996,0.150270,1.715362,1.881243,8.401969,-0.935266,8.605110,0.265641,-9.628705,3.579099,-8.532048,1.614469,-4.363908,2.460197,-8.181159,8.454192,4.379926,-9.004730,5.200833,6.045495,2.886609,2.305068,-3.013801,-9.224402,6.715139,7.825988,2.379420,2.376035,2.539312,-3.315587,-8.425103,3.319018,3.345381,8.496152,1.711989,4.076055,-0.679883,4.657840,-9.781607,7.471321,6.235102,7.338993,1.476487,1.631838,4.365219,-1.525805,6.065277,9.887917,9.094744,1.122017,8.715053,-4.008705,-1.261275,-4.624233,5.183163,-7.707076,-8.005260,2.694198,7.327015,-8.990145,5.748485,-7.706667,-4.488338,0.775133,-7.685047,-8.164956,3.165428,2.125558,-4.240653,-7.044734,-2.458052,2.904825,-3.855627,-8.362940,6.787840,-8.238623,-8.194448,8.381125,-3.933656,-7.139834,8.260313,5.096645,9.577273,-1.845918,-4.326180,-6.908591,-3.846912,-2.390928,-2.247108,-8.807119,4.430407,-9.956865,1.618912,1.494193,-3.825678,8.012429,-1.578235,9.375765,5.000282,-8.530945,-3.704260,-5.963091,-0.321577,-3.801215,-0.936045,-5.427159,5.081961,3.917535,-2.696060,9.798652,-3.040606,-8.669745,2.452795,9.433839,-4.878275,-2.140218,-1.146595,3.743112,2.306985,4.064960,-0.949392,-3.773301,8.827703,-7.186827,-6.213726,-0.406833,-5.633525,1.882732,-7.995496,0.159307,-0.591733,-0.843943,-0.133776,0.354822,8.873277,5.285476,-3.773448,2.816237,1.588084,8.004016,8.887325,3.486552,2.929587,3.243243,8.202489,-8.024020,4.507580,-7.858026,-0.871067,2.025804,-3.567552,9.481213,-1.561974,-1.036392,-6.115958,8.684132,-7.525005,-8.661792,-1.422483,4.204337,-7.100770,5.355405,-7.715329,8.045413,-4.624561,-8.699172,-4.934337,8.153445,3.624222,-9.680144,-2.271932,9.800319,-1.197400,-7.147596,-9.554387,-8.706008,4.863856,-4.582846,7.748333,-2.861309,-2.435362,1.299231,-4.475691,-8.487982,-5.690297,6.376831,-6.361104,1.052001,-1.794205,9.516289,-4.898954,1.396794,-2.806662,2.081425,-1.679320,3.953574,1.124661,1.227860,2.604633,9.172027,-9.507631,-4.283374,1.964116,-0.472235,6.430070,-4.768186,5.539057,3.348847,4.699029,-1.980349,-4.312362,1.914252,-6.463345,7.301758,-8.529617,5.954826,-9.027589,6.731853,-8.867509,9.621841,-4.388751,1.477138,-7.951369,7.335880,1.389660,7.988315,8.720270,3.285424,3.603922,5.306132,1.955885,-8.943776,3.849842,-3.955127,4.427163,1.365409,2.491245,-4.342448,-3.605765,-3.873324,9.530774,4.795143,-0.529306,-2.510576,-5.147926,8.795483,-4.395635,1.961285,5.942802,9.647425,3.010482,-7.769408,9.359843,-5.356605,-4.301918,-9.420765,-8.935151,-3.012445,-2.939857,-5.518365,1.194094,3.370199,-0.569962,3.449566,-5.757173,-3.195631,6.351350,-7.842298,9.950976,-2.647122,4.167485,2.498065,5.972596,-6.042630,-8.488797,-4.657147,-4.394471,-7.540205,-6.622737,9.998653,-4.028939,-5.705992,-8.072136,8.001210,-2.133561,-2.573221,-3.541168,3.146531,7.040421,4.427292,3.853434,5.219218,9.856007,-7.365670,1.746569,-5.586499,2.065923,-9.603731,-2.114394,-4.998726,8.211237,-7.116529,-9.662660,7.795383,-0.406868,-0.487163,-4.859753,8.344254,1.565008,6.947100,8.626212,-2.748992,5.814093,0.378140,-2.055326,-8.941267,-4.138814,6.121918,-9.826600,-7.245690,-3.158849,-7.817891,3.627539,-7.190046,5.560563,1.103919,-7.293905,-5.953767,-1.515738,7.536087,7.862401,2.109666,-1.037073,-3.086613,0.636124,8.080059,2.655220,2.173556,-8.958556,9.637195,7.639570,-3.513041,5.722243,0.733499,-1.291208,-9.255921,-9.517025,2.784686,6.190292,-2.600584,1.163197,-6.983721,4.548339,2.221722,8.628729,-3.238645,2.456768,-7.800503,1.346639,3.617916,-7.376154,6.518835,0.613875,-4.331468,-9.452564,7.464219,-4.094589,8.337720,1.300138,6.315619,2.180266,-1.536730,7.137329,5.918458,-4.782448,-8.968619,3.136703,-4.129702,7.322023,1.557847,7.473924,0.961796,-4.421106,5.611696,5.128100,-7.308697,-5.823760,5.166899,-7.879547,-2.609191,5.280083,3.422116,-4.244565,5.544339,-4.127769,-7.948651,-8.137421,-9.698068,-6.238879,-8.282453,-9.572067,-1.455497,4.374337,-9.074060,7.150672,9.214692,-8.732584,9.342916,-5.337574,-0.133761,6.918422,-5.554950,-5.080107,-1.285062,-4.413210,-7.120809,8.063214,-2.336182,-6.705108,-0.503203,6.889370,3.664882,1.564162,7.499452,1.174859,-1.430859,-1.466659,-8.480978,0.577223,2.230117,-2.388038,8.097694,-9.544706,-1.196257,-4.348619,-6.880599,-3.025286,7.804077,-8.147865,9.679376,-4.531030,-4.488007,-6.087512,0.118200,9.369676,-8.629354,-4.558156,-5.330662,1.946022,-8.148340,3.318378,9.413084,-4.382694,6.887115,1.591296,-3.012113,2.872695,-9.841837,-2.517520,8.980217,-8.598785,9.577001,3.040854,-5.806578,-3.369923,5.083227,7.281101,-4.442546,5.750177,9.727466,-7.315588,3.098550,-1.957635,-0.519221,2.181082,5.522385,8.451659,9.561588,-1.118479,3.514762,-0.354902,-5.026458,5.250262,1.913692,7.366197,-2.335808,-2.448248,0.361395,3.908247,0.033669,6.420461,1.111837,4.975762,-9.117228,-5.903645,1.117815,-0.358485,-5.683770,-7.954114,-4.918316,-9.193356,8.987627,-4.057108,-0.539502,-5.940822,1.438577,-5.894289,-4.127600,0.965928,8.446883,-7.526659,-5.595767,-4.784800,9.137135,-7.358227,-4.300903,-0.739355,0.330623,-1.025235,-7.244794,-7.924036,1.976227,-0.029128,-5.180314,-4.949490,8.684875,-9.230772,8.436430,1.200965,5.938683,-9.330986,-3.091818,-2.528818,-3.196980,9.329665,0.897150,-5.099873,-3.037636,0.072055,-5.383133,-6.833241,-0.096590,1.174396,-2.316624,-9.390536,-3.351212,8.846455,4.836404,-6.615967,8.667871,1.514529,9.024986,0.621349,-7.146523,5.812871,-3.597188,4.794981,-7.331591,-4.503782,8.562787,5.102782,7.365592,-6.404586,-2.152867,-9.917031,6.224839,-7.284177,7.431637,-9.857321,-8.738566,-0.523050,-7.973640,-1.037850,-4.885830,7.251546,4.869906,2.747201,1.906202,-4.613102,9.455418,3.547029,-8.987101,3.229838,6.915137,6.932300,4.164405,-0.442908,6.088178,2.473351,1.901621,9.091225,4.523529,-3.207517,8.238398,-0.649234,7.227635,5.023232,7.801570,-5.192301,-5.133045,9.853654,3.986847,2.495981,-3.804027,7.359138,3.585726,-0.711054,9.205834,-0.851176,9.888935,7.426823,-0.689878,-3.248172,-8.364856,8.512585,6.544766,-5.371244,-1.811649,4.647649,-5.014256,0.106137,-7.422968,-6.469484,-1.616108,-2.643626,6.878314,-0.650898,-7.895639,-1.407026,2.515063,4.572868,-1.063905,-6.100292,-7.614637,1.680532,-4.895013,-5.935158,-7.283701,-1.233264,0.819335,1.591770,6.483440,1.367493,-5.565762,-1.646369,6.326864,-4.395581,0.148398,-6.493187,2.654366,1.082084,-5.777582,-8.705177,-6.730936,4.267307,3.148047,6.012988,2.482377,-9.685111,-9.151430,2.799015,-2.320791,5.686579,-1.190614,8.607125,0.944840,4.278612,7.369962,-3.450898,7.024143,2.009126,-8.660512,5.018758,5.972243,-3.360983,-7.910220,7.455211,2.927284,-8.870633,1.625101,6.509436,-5.333127,-2.557869,-2.916338,-0.071381,7.994041,-0.013057,-1.546733,7.142780,3.114481,6.322368,4.100416,1.577479,4.765474,4.575957,2.916435,4.064474,0.648524,9.885179,-3.442684,0.267134,-8.070187,-0.299475,0.210361,-3.418107,4.009024,-7.565554,8.462519,5.216767,-0.318859,3.634641,-2.379840,3.287431,-9.156517,7.035627,-1.460608,-0.071728,4.034938,2.181273,-1.517045,5.565457,2.288406,7.567393,9.573386,8.783459,0.498169,-2.751136,9.611941,8.067116,-9.629076,4.457090,-0.238851,7.867351,-0.124373,-8.158956,5.003432,-9.988024,-2.995073,7.252174,-3.518627,4.072876,3.493556,1.185607,8.367963,-2.624152,-9.159565,4.626817,-8.382870,-6.760919,4.403542,4.380148,-4.932920,-8.072767,0.479033,9.028673,-6.102434,1.937114,-9.026850,3.363877,-7.082534,5.620688,1.704323,8.222627,-6.941869,-8.778072,-3.809731,-2.734212,4.857873,9.852919,-0.334119,-4.345228,0.452513,-1.106758,2.603458,-9.875386,2.233257,-7.365640,-4.249358,-5.801575,0.257327,-6.718140,0.637855,-9.798001,8.572094,3.395244,-3.561811,3.898435,-5.666373,6.342346,5.760628,6.227779,-2.847822,3.415837,0.562092,5.355240,-2.399768,-3.448854,-4.955000,-0.273837,2.861275,0.724631,0.793421,7.149433,-9.402031,4.991559,-2.100887,-9.137576,-5.319749,9.170678,-1.650272,-5.316409,1.897821,-4.351715,-9.082398,7.861582,-2.765782,4.577863,2.122376,3.625428,-5.575012,2.826863,6.560894,7.789950,4.161503,8.485656,6.739348,-2.589782,6.688243,-6.981439,0.055801,5.737841,-6.194632,-0.271044,4.141746,3.867702,-8.811595,7.028711,-1.104935,-6.486957,9.518088,8.613325,4.985894,4.925614,-9.308293,-5.581076,-6.733083,-9.510039,2.505517,-7.693666,-2.278566,-4.770467,0.943028,6.243546,-7.352120,5.510614,9.129649,-6.002647,1.645977,0.062868,0.460997,4.375014,6.964788,-6.494447,-1.609657,-4.178366,-3.184787,-3.308578,-3.011283,2.043234,2.139977,-9.126176,-4.054733,0.858219,5.281659,3.661080,3.067975,-7.717218,-9.681702,8.781820,6.621839,-3.072498,-3.657572,5.207448,-6.788548,0.666607,-2.105103,-5.614981,-4.512188,-0.557214,7.822905,-7.485566,-7.295642,9.332566,2.263843,-2.014449,-8.027092,-0.890769,6.733433,3.732629,-2.900388,7.366389,3.729840,6.987874,3.756443,7.653941,-7.991560,6.473064,-1.000213,1.529114,0.449653,-6.561283,-5.503065,-5.062010,0.932839,8.619189,-3.779823,-0.188676,7.228478,7.062358,5.562178,9.739475,-5.381595,-3.698210,8.233673,-4.840989,9.073775,2.947851,1.690366,1.737845,3.423854,5.712644,0.315806,2.008374,1.267852,-7.181294,8.363833,-8.586101,-3.079044,-0.180307,6.879062,2.342666,-0.430589,-7.771555,-7.360784,-2.107079,3.819191,-2.343253,8.373051,9.519487,-5.664349,6.630544,7.419219,-2.425946,-9.838235,0.184693,5.132830,3.479936,4.168202,-1.584396,8.249300,-3.495204,-0.145976,-6.045608,-2.624004,-9.834104,3.100270,5.709080,-5.126165,-5.856525,-5.119521,-7.092635,-2.546029,1.218655,3.064832,-0.658802,-2.981281,8.127801,4.089159,-5.052474,2.849789,-9.256310,-4.565001,6.435372,8.342266,-6.155394,-2.067625,-1.164685,-3.536389,-2.117916,5.332566,-9.984714,8.985349,-5.793163,8.461785,2.713153,5.622391,9.435136,7.199333,-4.474170,4.891612,-4.791195,4.186660,-6.053015,0.261673,-6.981821,5.707102,-3.494762,-0.018707,1.784135,-8.554017,5.298640,5.144233,5.633145,7.656358,9.874855,-3.897231,-9.649297,-7.726376,9.188682,-7.633827,-4.065560,6.809417,-8.813839,1.358511,3.672751,-5.509703,-6.368284,-2.442321,-6.012599,9.534383,-3.462699,-1.757852,-1.093024,7.521298,-3.631951,4.318407,-2.847115,5.186158,-7.046423,-9.998692,-3.460390,-7.371553,-8.061076,7.226805,4.520192,3.530671,-1.126682,-6.778882,-8.229734,8.759313,4.156048,-3.115045,0.001606,5.340546,-8.921392,6.785158,-4.479853,3.271959,-8.148453,-5.246920,-4.847972,9.130623,8.609296,5.430569,-0.317538,-3.306478,1.952842,9.853200,-2.786028,-4.402350,-9.198060,-6.002405,-3.005048,-5.995132,-5.746185,-7.725095,-5.597194,6.818146,4.443451,2.151041,8.543349,-5.562602,-2.075243,4.718133,-4.416731,-9.490183,-8.258859,5.857816,-3.362614,8.289825,-0.355339,0.358674,-2.645840,-5.548670,3.358930,0.251570,9.626567,2.189785,8.825202,0.411877,4.087273,-6.263800,-4.644800,-4.738066,0.393714,5.955638,7.944568,-7.300955,1.373664,6.866673,1.325756,-0.744909,-9.322387,-7.387294,-5.878800,7.245128,6.630101,6.275060,-8.658472,0.431296,-1.794368,5.092834,6.582061,8.598593,0.052286,-9.898411,1.108478,2.459163,-3.093338,1.940756,5.736703,-1.410688,-9.321216,-1.959422,4.097815,0.544480,-5.571592,4.656107,-5.887925,6.111941,-0.440437,-5.033391,-5.992510,7.156909,-5.023035,7.471004,-2.476931,-4.073035,-7.766997,2.554245,-7.813456,9.592320,3.404739,5.709773,2.769504,6.875116,-7.233549,6.383689,-7.595461,4.428551,8.066652,-7.458247,3.813086,-8.944931,-9.398241,0.951167,-9.534086,7.710732,-2.530904,-5.364430,4.411940,1.702554,6.302900,-2.841402,5.288869,-9.971031,7.857997,-9.248114,-8.733669,-2.320269,-0.744987,6.718882,-4.133258,5.354262,5.984359,-6.182098,0.863731,-6.810805,-4.080035,-0.170953,3.796531,-2.953509,-8.396599,3.405193,4.754249,8.630051,7.187364,2.610629,4.732323,-4.745296,-2.509947,-8.136933,-0.488644,-0.056998,8.802220,5.345246,-2.520628,3.403991,-8.860371,5.012162,-7.636650,-4.028543,8.837576,6.801196,-0.274944,-2.734877,-8.816970,-2.195544,4.260060,4.717693,-1.488509,8.629165,-3.605152,0.155264,9.851211,0.258622,4.009601,-9.772995,1.509872,6.505921,9.054528,-9.756174,-6.162510,1.753057,4.032948,3.177773,6.211996,-2.286793,7.997816,-2.338028,-2.416539,8.752804,0.786979,6.643051,5.609723,-0.280660,-6.756163,2.040259,-0.394542,-6.752455,3.396111,8.281913,4.200355,6.437725,9.608541,6.204912,5.573715,2.319230,-3.276315,4.689655,3.537585,8.428595,-1.944201,6.222208,0.887748,-7.778415,7.085254,3.830883,-9.429927,7.459003,-1.473182,6.745683,4.255547,4.675421,9.189551,-8.994679,-1.771204,-2.043461,-6.938749,0.188790,-5.101576,-5.929549,6.990668,-1.031697,-0.546294,8.285097,-8.826963,-6.741345,8.958749,-0.399442,-4.584419,-3.654162,-2.160953,4.818401,-9.935536,-6.646984,9.041420,-1.162423,-1.163466,-4.759437,-2.110895,4.023222,-1.426447,6.598052,7.002146,3.989976,-2.337347,3.455421,-7.438276,4.788974,1.928545,0.732491,-4.330744,-6.255630,-8.505072,-0.515800,-3.760251,-0.606974,5.631508,7.025328,2.852027,6.286117,-6.883904,-6.990426,6.833541,3.408211,6.723757,3.072221,-9.321763,-1.364929,-4.425792,3.496128,-9.172068,-0.791666,0.908091,0.665423,-6.977857,-0.136055,4.514178,5.234918,-9.754059,5.072584,-4.348003,-5.014296,-9.479628,8.332764,3.942750,-0.681621,-2.437733,2.488412,-4.575136,-0.995604,8.726446,0.093548,5.072023,-3.915084,1.025373,2.294209,-9.789121,-8.613266,-8.318429,-0.203089,-2.996119,-5.833219,1.180935,7.206733,-6.325729,-2.553672,-0.851787,-4.617927,-7.953953,-5.318335,-6.181732,9.990751,3.869461,-8.524888,-4.725992,5.516250,7.259132,0.450647,4.445596,-8.064057,6.852068,-0.088691,-2.174355,1.414490,2.650273,-3.582136,-3.516552,-6.270894,0.288296,9.859950,2.668758,-6.609236,-4.235516,8.972906,-7.917684,6.342965,-7.214348,-6.062628,-6.522765,-9.611722,1.236828,-8.455659,-4.465244,8.244093,9.873428,6.993886,1.693210,3.642366,-6.871776,8.838381,-4.733151,-7.296573,-0.077857,6.404373,-6.816292,-6.956720,-9.982226,1.682645,-4.507829,-2.933698,-0.216147,-0.761949,0.429892,6.165585,1.992103,7.547207,-3.220295,-3.913392,-3.270227,4.336332,0.184187,-2.699088,-0.943510,7.854100,-2.681089,-9.178341,6.610264,-3.869265,-3.137706,-9.449955,-7.169338,1.087975,3.394798,-0.940118,7.349460,7.910320,7.806784,-1.067788,5.896396,-8.170671,8.921245,-5.241624,-1.491009,-0.292891,9.056274,-1.937589,-0.631449,-9.138438,3.151696,3.238409,-8.564473,-9.506095,-9.897668,-9.593151,-2.938126,0.077757,9.664039,-7.409477,-2.108077,7.746835,-6.055733,9.988527,5.311976,-8.240820,-7.808863,-6.298839,-0.858759,0.779454,8.248962,9.684178,-9.538900,-2.280433,-6.939329,2.324961,8.675529,-2.512649,-6.832683,-2.941288,0.488387,2.428927,-6.830421,2.170705,-1.361836,8.430083,-2.693859,1.827300,7.649979,-2.129045,-0.240310,-3.044069,-1.006611,3.612770,-3.734725,8.072874,7.385540,-8.676289,-6.238889,-0.453789,-6.348777,-3.475671,-1.406278,5.731409,4.898053,-0.257032,-6.044354,1.749138,2.786249,8.695541,-9.587125,-7.878750,5.482773,2.761407,-0.683027,-1.699664,5.948655,7.259383,-2.808828,0.515192,-7.753000,-8.646397,-0.867055,-5.336759,-2.582697,-4.531782,-7.898019,-6.524002,5.768803,4.535297,-6.466386,-3.996175,-3.569128,5.224776,-0.471896,3.058274,-9.430443,0.463837,3.225696,0.205062,-9.155494,3.318408,-0.130710,-8.572683,8.857425,9.076486,-2.331005,-7.104890,4.893517,5.650008,-0.009436,-6.819474,-3.081796,-8.904647,8.778046,-3.663478,8.053971,-1.971433,1.442978,0.511960,-4.338240,-0.955629,-4.907447,-5.856870,9.456932,2.308383,-7.980261,-5.532041,-9.514345,-1.644117,-5.738299,2.855051,-4.158808,0.728787,-5.093267,9.795288,9.576521,2.454297,-7.883272,7.346120,-4.040360,2.049727,8.694745,8.334244,-9.559752,8.802975,-3.765063,-0.467500,9.181491,8.448445,-5.902060,-8.441444,-1.935510,3.228507,9.704961,-3.048771,-2.118313,-5.834245,-6.399828,9.649799,-9.055664,9.627532,3.859733,1.865346,-1.627027,-4.252474,0.094726,-6.505624,7.979222,-9.389075,4.296806,-2.250361,6.060256,9.248264,-0.713897,-5.039156,9.310166,-9.309085,-9.549167,8.718273,-2.953252,5.520349,8.577469,3.167307,-7.075929,7.274252,5.908245,6.419730,3.469307,-7.825988,9.699061,-6.377996,-9.333135,0.510924,-4.559556,7.887123,-8.763496,6.797796,0.015958,-2.818911,-3.552052,6.476837,3.504020,-1.082133,2.340151,8.505521,-8.493315,3.217239,-8.990001,1.678961,-4.382994,3.567051,6.250374,-5.338678,9.584791,-7.049097,-2.261778,7.096349,-6.648085,-5.006741,-8.888840,-2.242608,7.873267,-0.877920,-8.620920,9.454383,-4.769889,-1.974617,0.152516,-6.038579,2.739318,-7.455474,-8.986541,-2.193230,-1.244890,-9.609076,-9.989407,2.278143,2.452969,5.379554,1.766217,-5.010543,8.568387,5.680456,8.543994,3.015742,4.491410,-8.242805,-6.991498,-4.505028,-0.256697,8.113599,-7.105236,-3.221447,-9.943133,8.818839,-2.765990,-4.520557,-1.804563,-1.057717,9.860409,8.435401,-5.126443,5.542900,-6.634019,4.448410,-9.541626,6.904124,1.130460,-2.684607,5.877679,3.234503,6.334398,8.210790,9.638394,1.430911,3.209099,6.766165,5.077989,-7.147096,5.991609,-8.830473,2.278453,-1.979291,5.369071,-7.164365,-5.749070,2.127738,0.224854,-9.316689,-6.056884,-7.623314,-5.560542,7.178797,-9.371313,7.099291,7.264017,0.892770,9.095670,8.283456,8.684917,7.556745,0.869302,7.090320,6.217512,-0.692023,-9.664255,3.302058,-2.522408,-1.689518,7.449766,-0.346821,5.367841,3.642821,6.334967,5.591630,-4.721134,2.619914,6.881421,4.646380,-2.073568,2.056729,-9.891184,7.745810,8.367712,2.973239,1.621340,-7.355910,5.830793,3.328213,-0.547428,2.093478,9.841497,7.569971,-1.096290,8.226262,-9.668321,2.850275,2.106978,6.344997,-5.161844,7.983654,4.164594,-3.173076,0.942532,9.432941,-9.290094,9.305899,1.712404,2.539677,7.329958,-3.386800,9.948650,-2.496436,-9.727953,8.270842,-4.562102,-1.154094,-5.738746,-7.955973,-9.189225,-0.243080,4.056328,-3.418726,-3.160184,-6.046892,-4.664626,3.549685,-4.156085,9.748098,1.430006,0.582778,4.732259,8.449438,-0.703930,-2.696717,-2.420945,1.908503,-8.398370,-9.608853,8.936821,-2.513327,-8.414523,2.885789,1.598741,9.849374,-8.769913,-2.038882,2.244871,9.501467,0.693103,-2.531013,-8.001780,4.751451,-4.726524,5.737794,-0.163776,2.908127,0.244634,3.644041,0.964172,-9.537465,6.830430,-2.073709,-2.140568,-2.061524,5.811666,6.785332,0.059021,-8.128174,0.685877,1.643241,2.584828,-3.089571,-2.756220,6.008748,-5.527300,3.888793,-1.987090,-7.270507,3.925551,-0.193394,-3.065719,0.239127,7.542236,4.713198,7.466660,-7.460557,2.771558,-7.673755,2.957487,-1.310167,0.467063,1.937773,3.392435,-3.785586,9.543943,5.340411,5.630432,5.631108,-1.427590,7.336283,1.905724,-2.366923,-9.276524,-0.413653,-6.877160,9.708346,-3.459716,9.523090,1.223520,9.484510,-7.624510,-1.111888,1.073731,-1.378315,-2.011031,0.105010,-7.840735,-0.513668,-1.782183,-1.323364,6.630178,-3.539477,-6.877471,3.313243,-3.830096,-6.470090,8.237407,-1.446240,-5.759023,-1.309970,-4.556813,1.497752,9.166674,0.336569,-6.618000]], dtype = "float64")#candidate|3209|(1, 2016)|const|float64
var_3210 = relay.var("var_3210", dtype = "uint16", shape = (880,))#candidate|3210|(880,)|var|uint16
call_3208 = relay.TupleGetItem(func_1484_call(relay.reshape(const_3209.astype('float64'), [9, 14, 16]), relay.reshape(var_3210.astype('uint16'), [880,]), ), 1)
call_3211 = relay.TupleGetItem(func_1488_call(relay.reshape(const_3209.astype('float64'), [9, 14, 16]), relay.reshape(var_3210.astype('uint16'), [880,]), ), 1)
func_1763_call = mod.get_global_var('func_1763')
func_1768_call = mutated_mod.get_global_var('func_1768')
var_3238 = relay.var("var_3238", dtype = "float32", shape = (180,))#candidate|3238|(180,)|var|float32
var_3239 = relay.var("var_3239", dtype = "int64", shape = (364,))#candidate|3239|(364,)|var|int64
call_3237 = relay.TupleGetItem(func_1763_call(relay.reshape(var_3238.astype('float32'), [5, 9, 4]), relay.reshape(call_3208.astype('int64'), [968,]), relay.reshape(var_3239.astype('int64'), [364,]), ), 1)
call_3240 = relay.TupleGetItem(func_1768_call(relay.reshape(var_3238.astype('float32'), [5, 9, 4]), relay.reshape(call_3208.astype('int64'), [968,]), relay.reshape(var_3239.astype('int64'), [364,]), ), 1)
func_2031_call = mod.get_global_var('func_2031')
func_2033_call = mutated_mod.get_global_var('func_2033')
var_3264 = relay.var("var_3264", dtype = "float64", shape = (88, 8))#candidate|3264|(88, 8)|var|float64
call_3263 = relay.TupleGetItem(func_2031_call(relay.reshape(var_3264.astype('float64'), [8, 11, 8])), 0)
call_3265 = relay.TupleGetItem(func_2033_call(relay.reshape(var_3264.astype('float64'), [8, 11, 8])), 0)
output = relay.Tuple([bop_3182,call_3208,const_3209,var_3210,call_3237,var_3238,var_3239,call_3263,var_3264,])
output2 = relay.Tuple([bop_3182,call_3211,const_3209,var_3210,call_3240,var_3238,var_3239,call_3265,var_3264,])
func_3269 = relay.Function([var_3180,var_3210,var_3238,var_3239,var_3264,], output)
mod['func_3269'] = func_3269
mod = relay.transform.InferType()(mod)
mutated_mod['func_3269'] = func_3269
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3269_call = mutated_mod.get_global_var('func_3269')
var_3271 = relay.var("var_3271", dtype = "int32", shape = (11, 16, 12))#candidate|3271|(11, 16, 12)|var|int32
var_3272 = relay.var("var_3272", dtype = "uint16", shape = (880,))#candidate|3272|(880,)|var|uint16
var_3273 = relay.var("var_3273", dtype = "float32", shape = (180,))#candidate|3273|(180,)|var|float32
var_3274 = relay.var("var_3274", dtype = "int64", shape = (364,))#candidate|3274|(364,)|var|int64
var_3275 = relay.var("var_3275", dtype = "float64", shape = (88, 8))#candidate|3275|(88, 8)|var|float64
call_3270 = func_3269_call(var_3271,var_3272,var_3273,var_3274,var_3275,)
output = call_3270
func_3276 = relay.Function([var_3271,var_3272,var_3273,var_3274,var_3275,], output)
mutated_mod['func_3276'] = func_3276
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3431 = relay.var("var_3431", dtype = "float32", shape = (5, 15, 6))#candidate|3431|(5, 15, 6)|var|float32
uop_3432 = relay.acos(var_3431.astype('float32')) # shape=(5, 15, 6)
uop_3438 = relay.cosh(uop_3432.astype('float32')) # shape=(5, 15, 6)
bop_3440 = relay.logical_or(uop_3432.astype('bool'), relay.reshape(uop_3438.astype('bool'), relay.shape_of(uop_3432))) # shape=(5, 15, 6)
func_1806_call = mod.get_global_var('func_1806')
func_1809_call = mutated_mod.get_global_var('func_1809')
var_3450 = relay.var("var_3450", dtype = "uint64", shape = ())#candidate|3450|()|var|uint64
call_3449 = relay.TupleGetItem(func_1806_call(relay.reshape(var_3450.astype('uint64'), [])), 2)
call_3451 = relay.TupleGetItem(func_1809_call(relay.reshape(var_3450.astype('uint64'), [])), 2)
output = relay.Tuple([bop_3440,call_3449,var_3450,])
output2 = relay.Tuple([bop_3440,call_3451,var_3450,])
func_3452 = relay.Function([var_3431,var_3450,], output)
mod['func_3452'] = func_3452
mod = relay.transform.InferType()(mod)
mutated_mod['func_3452'] = func_3452
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3452_call = mutated_mod.get_global_var('func_3452')
var_3454 = relay.var("var_3454", dtype = "float32", shape = (5, 15, 6))#candidate|3454|(5, 15, 6)|var|float32
var_3455 = relay.var("var_3455", dtype = "uint64", shape = ())#candidate|3455|()|var|uint64
call_3453 = func_3452_call(var_3454,var_3455,)
output = call_3453
func_3456 = relay.Function([var_3454,var_3455,], output)
mutated_mod['func_3456'] = func_3456
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3618 = relay.const([[[-1.792917,8.155249,7.846116],[-4.369747,-8.930748,-1.738292],[-0.724083,-5.946030,4.298518],[6.663656,4.167094,-0.191780],[6.379710,-3.418182,0.674179],[7.275701,0.189094,-7.890802],[-1.613916,4.400408,-7.305851],[7.705174,-9.078066,6.418460],[-2.058754,-4.898832,-3.032096],[-9.178061,-0.685163,-2.358029],[-8.935278,4.456709,-0.823858],[5.913813,1.080191,7.014467],[-2.161877,-3.621513,-8.411450],[-2.652182,-9.822833,8.582814]],[[-1.913766,-3.371883,-9.127944],[-1.522382,-5.728471,-1.513828],[-0.080419,4.654404,-6.809920],[7.235876,9.021031,7.986890],[-7.734735,-9.056269,5.389603],[5.523720,-4.734724,-3.166652],[6.535691,2.668448,-3.520377],[-2.973625,0.669597,-8.021482],[3.844039,3.493294,8.797017],[-7.634567,-8.665967,-4.316361],[-5.704205,2.053457,1.976240],[0.029510,3.775312,-8.798868],[-1.367152,-3.835478,9.433707],[-9.652136,-5.805581,9.875723]],[[-2.754375,4.647840,3.843860],[-1.700527,-6.906189,-2.502335],[5.025825,-2.489240,-1.377395],[9.813792,8.980212,8.146902],[-2.130529,9.926051,0.463598],[9.294278,5.903245,-5.214858],[-2.148493,-3.930497,7.505906],[5.631620,5.042780,3.888546],[-2.401081,-2.487282,-1.893174],[-0.384370,9.872749,8.589722],[4.883867,6.562780,-2.680416],[3.857845,-3.731334,1.661261],[-1.824400,0.356696,-0.780825],[4.141289,8.019917,-9.012143]],[[7.102862,-9.700044,4.520909],[5.193028,-5.957521,7.279760],[9.960519,-6.286419,-2.458753],[8.528255,-9.943869,-7.459784],[0.292747,1.053392,-7.040981],[-2.863727,7.124164,-6.875828],[-7.881612,0.732792,-0.115998],[8.290162,8.956622,-8.706381],[3.089775,-7.751073,-8.084854],[-9.441778,-6.604977,-2.222249],[-4.852874,3.016805,8.501281],[-6.126937,1.511160,6.852451],[-6.472870,2.131382,-4.333163],[7.825989,7.110636,3.949299]],[[7.118523,3.433047,2.035256],[-0.794464,-3.700343,5.789008],[9.152097,-0.114956,3.971790],[4.037963,-3.974538,7.258361],[-7.604637,9.746082,-7.370262],[0.219209,-4.010098,-8.647015],[-7.908424,5.105525,-2.619870],[-8.764342,-0.313615,-7.625591],[-5.739765,6.029130,7.003325],[4.470405,-4.506832,4.266977],[7.468228,-6.748141,-3.680824],[-9.610138,0.162658,6.324729],[-4.778763,8.789476,-4.569244],[6.805029,1.943393,-0.606165]],[[4.411376,-8.647312,-2.742121],[2.043180,-3.446391,2.408758],[-0.361521,6.886836,-6.265140],[9.305024,2.720112,6.426261],[-1.415309,-8.312433,-8.526057],[-5.232247,3.169599,3.509941],[7.525572,2.495923,-7.001492],[-8.075572,-2.962437,-8.179253],[-1.931549,-7.551776,-5.482976],[-0.433736,-7.080548,5.168024],[8.938155,-8.333711,-6.498416],[-3.861808,-5.344881,-9.194374],[-2.060228,0.041133,-4.009008],[5.102418,1.639784,-2.511998]],[[-1.726624,7.954852,-9.079626],[2.104941,-9.603527,-4.399375],[1.403792,-2.659654,-9.941405],[-5.913451,1.263804,-1.428017],[3.802663,3.608245,4.092352],[-3.398181,-3.406710,-9.295396],[-1.847502,-6.998252,1.776731],[-0.652440,2.230754,9.740566],[0.021115,-6.117069,8.362437],[-0.170271,5.606661,-4.375321],[-0.524736,-3.221257,-9.748382],[2.120240,-2.920010,6.156685],[-1.788257,-4.063385,9.986066],[1.326230,8.267655,3.179643]],[[-6.741645,1.634709,2.042775],[-2.191591,-1.100764,-1.094228],[0.297071,-1.901992,6.003598],[-7.090728,4.727768,2.766876],[-9.734343,8.257217,5.747476],[-4.382536,-7.518786,0.067037],[3.020566,3.544857,-8.593979],[-1.005739,7.165104,4.404001],[3.130945,-2.371039,-4.792979],[0.863962,6.217257,-9.641958],[0.024869,-0.990480,-8.434223],[-8.982619,-9.093858,8.353876],[8.777359,-7.454942,-8.787418],[-2.082312,2.774903,-3.089958]],[[-1.273011,-9.913864,-3.235387],[-1.094373,-4.773373,-2.402819],[-1.384477,-5.161991,-5.557342],[9.872291,-1.669132,3.796242],[2.393700,-3.133607,-8.913052],[-8.239535,-6.730841,-8.735208],[8.074658,-7.188797,-2.137780],[-3.516310,5.917801,8.820670],[9.456740,-2.426846,-3.617767],[-4.964808,2.190351,8.648899],[-0.497739,-4.291097,-0.173683],[8.488039,-3.427414,9.821533],[-4.814345,0.931872,4.153202],[-8.875604,-6.579727,-0.595601]],[[-4.788909,-6.125251,0.540695],[7.517539,-4.982818,-6.977924],[4.361257,-6.362090,4.079196],[-8.442152,-0.535853,-8.867287],[-4.207898,-8.225853,4.282677],[7.129008,8.379482,4.004535],[0.572642,-4.366158,-6.362139],[5.961293,8.993304,2.926157],[4.348121,-6.394690,-9.500601],[5.281618,2.573888,0.647635],[-4.161576,-4.374983,-5.040334],[-3.314489,3.144571,8.093480],[2.583655,0.395935,3.013478],[-7.307408,-4.693998,-0.472527]],[[9.330164,1.723985,4.749459],[5.766817,5.141957,9.111993],[9.259901,-1.732941,9.731277],[-2.828021,-3.530444,7.906759],[5.167912,-2.765736,-8.561810],[-8.486475,0.909781,2.316239],[-1.147775,-3.904162,-1.128701],[1.916044,-0.186388,-6.908651],[-8.774520,-2.769793,-3.016013],[-9.942108,5.762417,8.646403],[4.582063,6.536846,0.536443],[0.641271,7.278363,-5.418687],[1.141223,3.141347,0.770235],[9.550753,6.342870,-3.919234]],[[4.867698,5.454344,6.175014],[7.447569,-1.829414,8.051521],[3.357995,4.969320,1.888740],[-5.172216,9.272822,-7.692389],[-3.395179,-0.706251,4.526338],[2.285158,0.990863,-1.731497],[-8.276951,6.422368,-1.826212],[-2.578457,7.033065,5.916879],[6.128829,-9.564044,1.435676],[6.725260,-9.537973,5.692225],[-0.660886,7.538745,9.219140],[0.128823,2.234573,-8.289971],[4.289438,4.153350,-8.276983],[3.246979,-5.289611,0.507163]],[[-0.351249,4.783482,-3.801513],[6.510883,-0.685155,5.904074],[-7.031633,0.167042,3.321835],[3.967140,-3.972707,-5.171958],[4.120278,5.001498,9.890424],[-4.009981,7.596261,-5.873300],[-6.386429,9.112789,-2.713304],[4.331805,7.126830,-8.083976],[-6.856962,5.936799,-9.096195],[-5.775571,-3.978824,-5.671198],[-1.877864,4.094254,-0.342649],[7.450854,8.955415,0.842846],[3.832477,-1.019761,5.778432],[-9.622808,9.848355,9.092743]]], dtype = "float64")#candidate|3618|(13, 14, 3)|const|float64
var_3619 = relay.var("var_3619", dtype = "float64", shape = (13, 14, 3))#candidate|3619|(13, 14, 3)|var|float64
bop_3620 = relay.divide(const_3618.astype('float64'), relay.reshape(var_3619.astype('float64'), relay.shape_of(const_3618))) # shape=(13, 14, 3)
output = bop_3620
output2 = bop_3620
func_3623 = relay.Function([var_3619,], output)
mod['func_3623'] = func_3623
mod = relay.transform.InferType()(mod)
var_3624 = relay.var("var_3624", dtype = "float64", shape = (13, 14, 3))#candidate|3624|(13, 14, 3)|var|float64
output = func_3623(var_3624)
func_3625 = relay.Function([var_3624], output)
mutated_mod['func_3625'] = func_3625
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3792 = relay.var("var_3792", dtype = "float64", shape = (12, 4, 10))#candidate|3792|(12, 4, 10)|var|float64
uop_3793 = relay.atan(var_3792.astype('float64')) # shape=(12, 4, 10)
output = uop_3793
output2 = uop_3793
func_3802 = relay.Function([var_3792,], output)
mod['func_3802'] = func_3802
mod = relay.transform.InferType()(mod)
var_3803 = relay.var("var_3803", dtype = "float64", shape = (12, 4, 10))#candidate|3803|(12, 4, 10)|var|float64
output = func_3802(var_3803)
func_3804 = relay.Function([var_3803], output)
mutated_mod['func_3804'] = func_3804
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4626 = relay.var("var_4626", dtype = "int64", shape = ())#candidate|4626|()|var|int64
const_4627 = relay.const([[[8,7,-4,-6,5,-9,-8,9,-6,-6,-4],[-8,4,2,-1,-9,-4,-3,-9,9,-8,6],[-9,10,1,10,2,4,9,8,-8,-9,3],[3,8,5,-4,3,-7,-9,-9,-6,9,9],[-8,8,-3,-10,-8,8,9,-3,6,6,-9],[2,4,-10,-9,-10,7,-3,-6,7,-10,-1],[10,-9,10,-8,10,8,9,6,-9,7,8],[-6,-6,10,10,2,5,-4,7,-5,-5,1],[-3,4,-7,9,2,10,10,2,1,-10,7],[1,-10,-3,9,9,-2,7,-5,-5,-4,4],[2,4,2,-2,-9,-5,9,-4,-1,-4,7],[2,-8,10,9,3,-10,7,-2,2,-1,-2],[4,-3,-10,-8,6,10,5,3,-2,7,7]],[[7,-2,3,-6,6,-3,-7,-5,10,2,-7],[-2,1,1,7,2,7,2,9,-7,10,-5],[-2,1,-6,-4,10,-5,9,10,4,-1,-8],[-3,3,-4,-7,-1,3,-1,-4,10,-10,-6],[-1,-6,-8,5,9,3,-5,4,-7,-3,6],[-9,-8,6,-6,-8,9,-1,10,-3,4,-1],[-4,-3,10,3,-9,-8,-1,-6,7,3,1],[-2,-2,9,10,6,-7,-7,6,-4,-2,3],[-7,10,6,-9,-9,-7,-6,8,-8,-10,-5],[1,6,-8,10,-2,2,-10,-5,-5,-9,-7],[9,-1,-10,-2,-9,-6,-10,1,-6,8,5],[8,8,6,6,-4,-1,-3,-9,5,10,1],[8,2,7,3,10,3,5,-9,7,7,2]],[[6,-7,-7,4,8,4,-7,-2,2,-2,-1],[-8,-9,6,10,5,9,-9,-8,-8,7,6],[10,4,9,-1,-4,-3,-2,8,8,8,-5],[8,3,10,6,4,4,-10,-8,3,9,-5],[-8,-3,-8,6,9,9,-9,-2,4,1,-7],[-9,5,9,2,5,8,-8,10,-2,-9,-10],[9,-3,1,-1,8,-5,3,-5,7,7,-7],[-4,1,5,-8,-8,1,1,7,2,1,-6],[-1,-1,2,-8,5,7,9,-3,9,3,5],[3,6,-7,3,3,-6,-4,2,-1,-3,2],[10,-8,-9,10,7,-5,-9,1,-6,7,7],[-4,5,-8,6,2,-7,7,-5,9,-2,-6],[9,-4,10,-8,-5,9,-10,2,-9,1,7]],[[4,-9,-4,9,2,9,-2,-7,7,-5,-6],[5,2,-2,-2,3,9,-10,2,6,7,2],[-2,2,-3,-8,-3,-6,-1,-7,5,10,3],[10,-9,-1,-10,8,2,-3,-6,-5,-8,-3],[7,-1,-2,-10,-10,2,5,-8,4,8,5],[-10,-6,1,6,-10,-3,-7,1,2,8,-3],[-5,9,-8,-5,10,-5,2,8,-1,3,1],[-1,-9,-4,-4,1,9,-1,7,-1,5,1],[3,7,10,-7,4,-3,-10,-2,-5,6,-5],[10,-4,8,8,-9,1,-4,8,9,-1,6],[1,-8,5,10,-2,1,-1,5,8,-10,-10],[9,-8,-1,-3,2,7,10,-5,-9,9,5],[10,-9,4,9,-4,3,9,2,-8,-5,4]],[[6,-6,-8,-8,-6,3,-5,7,-10,-2,-4],[6,2,8,-1,-5,-4,4,5,-5,8,-6],[-6,9,-3,-8,4,3,-7,7,5,-7,-2],[-3,2,-8,9,-7,7,10,1,-9,1,2],[2,10,-1,8,-7,-10,2,-3,-2,-3,-8],[-2,-10,-3,2,-3,-5,4,7,9,7,-4],[7,-10,-8,9,8,5,4,-9,3,3,-4],[-6,-2,-4,6,8,3,-2,2,7,7,-8],[-1,-7,10,4,10,-2,7,-1,-5,-4,-8],[-9,2,-10,9,-9,-6,7,-8,-7,-1,1],[8,8,-3,-2,-3,-1,9,5,9,10,-2],[-9,-8,-1,9,6,5,9,-10,-7,1,7],[9,-10,8,4,-9,-10,-1,-5,-4,6,-6]],[[-5,5,9,-2,-6,10,9,-7,8,6,-2],[-9,-7,-7,2,9,2,-3,-10,9,6,-3],[9,-8,6,5,2,7,10,-4,9,-2,-9],[-4,-10,4,-6,10,9,-4,-1,4,-6,-5],[-5,9,-4,9,-7,-2,-7,2,-5,1,-10],[8,-4,5,3,6,-8,-6,-7,-6,7,1],[4,9,8,3,5,-9,4,-10,-3,9,-1],[-4,1,3,7,3,-7,-3,4,-3,7,-9],[6,-10,-6,-2,7,5,7,-5,10,-10,-2],[-4,-6,5,-10,4,4,7,-6,-4,7,10],[-5,-10,5,-6,2,-5,-8,4,5,-6,-4],[6,1,3,-1,-4,10,-3,-6,3,-10,8],[1,8,10,6,6,-5,3,-7,-5,-1,8]],[[1,3,-4,4,-3,-6,2,2,1,9,-8],[-8,-7,7,7,3,9,-1,1,7,-10,-2],[10,-8,5,-10,2,-8,-10,-8,-10,4,9],[4,-9,-1,-5,-1,8,-7,9,-5,-5,9],[-6,2,-9,7,2,-5,4,1,-2,6,2],[-4,1,1,10,1,8,-4,-2,3,2,-4],[-8,6,7,-10,5,1,1,4,-3,-9,-10],[8,-4,5,-10,2,4,-6,2,-2,-9,-3],[-7,4,-3,3,-8,5,-9,-9,9,-7,-1],[-4,8,-10,-2,-9,-1,1,6,7,-4,-7],[3,3,5,-3,-2,9,-6,7,1,9,9],[-6,-5,-10,-5,3,10,8,-6,4,-9,-10],[-10,-4,-4,-3,-4,-7,-1,-1,3,2,10]],[[1,-2,-5,-5,-7,1,8,-6,-8,9,3],[-4,4,-8,1,8,-5,-6,-3,-5,-8,6],[4,6,-4,9,4,-4,1,7,-10,-5,-7],[-5,-1,-3,-7,-4,10,-4,4,-6,7,9],[1,-1,2,4,-6,-10,-9,6,3,-8,-8],[1,-4,-2,-6,10,-8,-6,6,10,1,8],[4,-6,4,1,-6,5,9,2,10,-3,-2],[9,-1,1,10,1,-5,-2,-3,-2,5,-1],[-7,-10,-7,-5,1,1,10,3,-5,-3,-3],[1,10,-5,1,1,-2,-2,5,-2,-9,10],[6,1,-10,-2,-3,-9,6,-8,-1,-2,-2],[-6,2,-3,10,4,9,-7,-2,-1,2,8],[3,3,-4,9,-1,-3,2,8,1,9,-7]],[[-10,5,-6,9,-7,9,-6,-6,3,9,-2],[3,-4,2,-8,-10,-2,8,-4,-3,7,10],[8,-10,5,6,2,-7,-6,10,2,2,4],[1,5,8,5,-9,6,-4,9,-8,9,-7],[-8,1,-6,-1,1,6,-5,1,-2,5,-10],[-9,-6,7,-6,-2,-1,4,6,-8,9,-4],[-10,-8,-7,-2,-1,3,-2,5,-7,4,-10],[7,-4,-2,1,-1,2,3,10,6,8,9],[10,-10,10,6,10,5,-8,-1,4,-10,-9],[8,10,-3,1,-10,7,-9,4,1,1,-10],[-5,-10,2,7,-4,-3,7,5,-9,1,7],[-6,-9,4,5,1,-4,-10,2,10,-2,-10],[-10,-9,4,-8,3,-1,-3,2,-1,-7,-7]],[[-3,-4,-3,-7,-5,2,7,-5,-6,-9,1],[-3,9,8,-1,10,-4,-7,1,1,-1,2],[-8,3,5,4,5,9,-3,9,-1,-8,-3],[1,-10,-10,7,9,8,3,7,7,7,7],[2,4,4,8,8,9,-6,-9,2,-8,3],[2,-9,3,5,-5,-3,-10,-10,4,10,6],[-4,-8,-4,-7,-10,-8,-7,4,-10,-7,-8],[9,7,-8,9,-4,-10,9,9,-4,4,7],[-10,1,1,-2,-7,9,-6,-1,-2,8,-7],[9,-5,-6,-2,10,5,-3,-1,5,7,2],[-2,8,9,-7,7,4,-10,10,-5,-5,2],[-5,4,1,-4,7,-7,10,-3,2,-5,-1],[-9,9,1,-4,-4,10,-1,-9,3,2,3]],[[5,1,5,8,-2,-6,10,-5,-4,5,6],[2,-2,-3,6,6,-1,3,-4,-1,7,-7],[5,-3,-10,-1,-4,-6,-2,9,-7,1,2],[4,-4,-2,10,-8,-1,6,-9,10,1,-10],[-4,-3,3,-9,-8,3,-7,5,-2,4,5],[-5,-6,10,8,2,-8,-5,1,-10,-8,-2],[-5,2,-9,-3,6,-9,-10,4,8,3,3],[10,1,-2,10,4,1,5,2,-4,-5,-5],[-3,-4,-4,-8,-5,10,6,-5,-6,-4,-4],[-6,-8,-9,5,-7,-2,1,7,3,-6,10],[-5,-10,3,-7,-4,5,5,-2,-7,-1,1],[-7,1,-2,2,-9,-6,-7,3,-8,-9,9],[-9,4,-2,-7,9,3,3,-7,9,6,-6]],[[-6,9,6,-9,9,7,-5,10,-2,-7,9],[4,7,-3,-1,-5,10,3,9,-2,-1,4],[8,10,-5,8,-9,3,8,-8,-6,7,9],[3,-3,8,6,4,10,-3,-2,-10,-3,-6],[10,9,-9,4,-8,7,4,7,-7,-3,4],[-3,-8,7,7,-4,9,5,-2,5,-7,-9],[-8,-2,-7,4,-4,-8,-10,-6,8,4,-3],[-7,-9,5,7,-1,-2,9,-10,1,-10,6],[5,6,2,-3,10,-2,-2,-7,2,-3,-10],[6,-5,-6,7,4,-4,7,10,-4,10,9],[4,-1,1,3,-6,3,-7,8,-1,-7,-5],[-2,6,7,-4,2,-2,6,-8,-7,7,8],[7,9,-2,-4,3,-2,-3,-9,-5,5,-3]]], dtype = "int64")#candidate|4627|(12, 13, 11)|const|int64
bop_4628 = relay.equal(var_4626.astype('bool'), const_4627.astype('bool')) # shape=(12, 13, 11)
func_818_call = mod.get_global_var('func_818')
func_822_call = mutated_mod.get_global_var('func_822')
var_4634 = relay.var("var_4634", dtype = "int64", shape = (364,))#candidate|4634|(364,)|var|int64
call_4633 = relay.TupleGetItem(func_818_call(relay.reshape(var_4634.astype('int64'), [4, 13, 7]), relay.reshape(var_4634.astype('int64'), [4, 13, 7]), ), 0)
call_4635 = relay.TupleGetItem(func_822_call(relay.reshape(var_4634.astype('int64'), [4, 13, 7]), relay.reshape(var_4634.astype('int64'), [4, 13, 7]), ), 0)
func_3269_call = mod.get_global_var('func_3269')
func_3276_call = mutated_mod.get_global_var('func_3276')
const_4647 = relay.const([[-4],[3],[-6],[3],[9],[1],[-9],[-5],[5],[-8],[5],[-8],[7],[10],[1],[-10],[-9],[-7],[4],[-8],[-10],[-6],[1],[9],[-9],[10],[5],[6],[9],[7],[-2],[-5],[1],[-7],[-3],[-7],[3],[3],[-7],[1],[-9],[9],[8],[7],[1],[-7],[10],[5],[5],[-6],[8],[-3],[-9],[6],[-9],[1],[7],[2],[-5],[-5],[5],[-1],[-6],[-6],[-10],[-1],[-8],[-9],[3],[2],[-2],[9],[-4],[7],[4],[-6],[-7],[-3],[5],[6],[-4],[4],[-3],[10],[10],[-9],[-6],[6],[-1],[-9],[-6],[-3],[-2],[-6],[6],[2],[10],[5],[-1],[-1],[-6],[7],[-1],[1],[-5],[-9],[5],[-4],[8],[6],[3],[-5],[6],[-8],[4],[1],[-2],[-3],[-1],[-4],[-5],[9],[-5],[-1],[-4],[-7],[6],[2],[2],[10],[9],[-6],[-10],[-1],[3],[7],[-10],[-2],[-9],[10],[-9],[-2],[10],[7],[-4],[-8],[10],[4],[-2],[3],[2],[-5],[-8],[1],[-9],[3],[-9],[3],[1],[-3],[-10],[-7],[-6],[-10],[-6],[4],[-3],[-4],[6],[-10],[-6],[5],[10],[-9],[9],[-7],[5],[-9],[5],[-7],[-2],[-2],[-2],[8],[2],[4],[-1],[-5],[6],[-3],[8],[-6],[-3],[1],[-4],[-10],[-1],[-3],[-9],[-10],[-9],[8],[1],[2],[-1],[-2],[2],[-9],[-3],[-3],[-9],[3],[-7],[3],[-7],[6],[-5],[-7],[-2],[-6],[1],[-2],[-6],[-8],[-1],[5],[-3],[-10],[-5],[6],[-5],[-8],[-9],[-9],[-4],[-5],[-4],[8],[6],[-8],[8],[-7],[-2],[-1],[1],[8],[4],[-8],[-3],[-5],[3],[9],[-7],[-7],[4],[1],[9],[-3],[6],[-9],[-5],[-5],[-7],[1],[10],[-4],[-8],[-8],[2],[7],[1],[8],[-8],[4],[-8],[3],[1],[10],[8],[7],[-9],[-1],[-6],[1],[4],[-3],[-6],[6],[5],[7],[4],[7],[-5],[5],[-10],[1],[3],[-8],[1],[-6],[7],[-2],[4],[6],[8],[3],[1],[-7],[-6],[-2],[-5],[8],[5],[7],[-3],[-10],[2],[-3],[10],[6],[-3],[1],[-6],[4],[1],[8],[9],[5],[2],[-9],[-7],[-7],[-1],[-7],[-2],[-10],[-1],[-10],[-9],[1],[-10],[-9],[-7],[-10],[-8],[-3],[-8],[-6],[-3],[-1],[-6],[-1],[-1],[-8],[-7],[2],[9],[6],[-8],[4],[7],[-1],[-2],[-5],[9],[-1],[8],[6],[4],[2],[4],[-1],[-7],[-1],[-3],[-1],[6],[7],[-10],[-10],[-8],[-8],[2],[-8],[7],[-10],[-5],[-3],[5],[-7],[1],[-1],[3],[-3],[-2],[-4],[6],[9],[-7],[4],[6],[-4],[-4],[3],[-3],[10],[-2],[10],[-10],[-8],[8],[3],[5],[1],[8],[7],[-1],[6],[10],[-5],[-2],[8],[7],[-9],[5],[-9],[9],[-6],[-5],[-8],[4],[8],[-6],[1],[6],[10],[10],[-1],[-10],[-3],[-6],[-7],[-4],[3],[1],[4],[-9],[-3],[7],[-3],[-9],[-10],[-3],[-3],[1],[-7],[8],[-6],[-6],[-4],[2],[-4],[-10],[-8],[-8],[-1],[-3],[5],[2],[-10],[-4],[2],[10],[4],[6],[-3],[-4],[9],[-2],[3],[5],[-9],[3],[-8],[-2],[9],[-5],[7],[8],[-1],[7],[-1],[1],[-7],[7],[4],[-1],[2],[-9],[-2],[1],[4],[-4],[-1],[-2],[7],[6],[-2],[-9],[1],[10],[10],[10],[-9],[4],[-9],[-5],[-1],[4],[1],[4],[-7],[7],[-9],[-10],[-4],[6],[2],[-6],[7],[2],[-5],[7],[-6],[-7],[8],[7],[4],[-5],[-2],[-3],[-5],[-8],[7],[10],[4],[-7],[1],[-2],[-6],[-5],[10],[2],[-6],[7],[1],[-4],[-9],[7],[-6],[9],[1],[6],[10],[10],[-9],[-4],[7],[-5],[2],[2],[-1],[2],[-7],[-7],[8],[-3],[-2],[4],[7],[1],[8],[-4],[-1],[9],[2],[7],[-8],[-5],[-9],[-9],[8],[9],[-9],[3],[-4],[-3],[-8],[-9],[-8],[2],[-10],[3],[-7],[-2],[-3],[-5],[-1],[1],[5],[9],[8],[4],[-10],[7],[-1],[-8],[-8],[-8],[9],[3],[-1],[3],[3],[5],[9],[9],[-5],[-5],[8],[-3],[-1],[-2],[9],[-3],[-2],[-2],[-5],[6],[-2],[7],[-4],[-1],[3],[-3],[10],[-2],[6],[9],[7],[-6],[10],[-1],[-5],[-2],[7],[-8],[-8],[-9],[-7],[-4],[8],[-5],[3],[10],[7],[7],[5],[2],[-5],[9],[-6],[3],[6],[-8],[4],[-7],[9],[9],[-9],[10],[-6],[-3],[6],[-3],[2],[3],[8],[3],[-9],[6],[-3],[8],[-8],[-4],[5],[-3],[4],[3],[1],[-1],[5],[10],[-1],[7],[6],[-5],[-10],[-2],[9],[5],[1],[-6],[4],[-5],[5],[-10],[1],[6],[-5],[-3],[-8],[-9],[-1],[-7],[7],[6],[-10],[3],[4],[-2],[1],[9],[-2],[-3],[8],[7],[4],[6],[-8],[-6],[5],[-3],[4],[2],[3],[7],[4],[7],[3],[-2],[-5],[10],[-6],[5],[-7],[1],[2],[-8],[1],[4],[-4],[9],[1],[1],[-5],[6],[3],[-1],[10],[2],[-6],[-3],[8],[-5],[-3],[-2],[-4],[-2],[-4],[-8],[7],[1],[1],[8],[-10],[1],[5],[4],[-7],[-4],[-10],[7],[7],[8],[4],[2],[-1],[5],[7],[-3],[6],[-2],[-10],[-8],[-5],[-9],[-7],[8],[8],[7],[1],[7],[-2],[-4],[-4],[5],[3],[-4],[-4],[-3],[-3],[6],[9],[-5],[-10],[-10],[10],[5],[-8],[3],[5],[3],[-7],[-2],[9],[2],[8],[-3],[-1],[-5],[-9],[-2],[-10],[4],[-5],[9],[9],[10],[1],[1],[-1],[-4],[-10],[-7],[5],[4],[7],[-6],[-4],[-5],[9],[10],[8],[-4],[-6],[-8],[7],[-6],[-1],[1],[-5],[2],[2],[8],[-8],[4],[-7],[-5],[-8],[3],[-5],[9],[-5],[2],[7],[1],[-8],[-3],[9],[-6],[-4],[-6],[7],[-5],[2],[9],[9],[1],[4],[-9],[7],[-5],[1],[7],[1],[10],[-6],[-6],[8],[9],[9],[7],[-5],[-1],[2],[-2],[-8],[-3],[-6],[2],[4],[3],[-8],[4],[-2],[6],[-9],[7],[-1],[-7],[-8],[9],[-7],[-6],[5],[-2],[-2],[10],[6],[8],[4],[-9],[-6],[1],[5],[-8],[6],[-9],[-4],[-7],[7],[-9],[-4],[2],[10],[10],[-3],[1],[5],[9],[-7],[-3],[8],[7],[10],[-10],[-3],[7],[5],[-9],[-9],[-3],[6],[-4],[-3],[1],[1],[6],[-7],[-1],[6],[6],[-8],[7],[2],[10],[-3],[-6],[4],[-1],[4],[-10],[7],[6],[8],[-3],[-7],[-4],[-3],[10],[-6],[-7],[-1],[9],[-4],[6],[-4],[4],[-2],[-7],[6],[-5],[-2],[9],[1],[-1],[10],[-8],[-2],[8],[-9],[5],[-1],[-7],[7],[-3],[6],[9],[-8],[-3],[8],[6],[1],[-8],[-10],[10],[-1],[5],[2],[-4],[7],[-6],[-5],[1],[3],[-4],[8],[-10],[-3],[4],[7],[5],[9],[-1],[-3],[1],[-2],[3],[10],[-3],[-9],[-6],[7],[6],[4],[-5],[3],[8],[-1],[2],[4],[6],[-8],[3],[4],[-3],[-3],[10],[4],[-9],[-5],[9],[6],[10],[8],[3],[-5],[6],[-9],[-3],[5],[8],[6],[-7],[3],[9],[2],[-7],[-7],[6],[-1],[7],[-2],[-9],[-4],[-6],[10],[-8],[-1],[7],[2],[-1],[3],[-3],[-7],[8],[-1],[-3],[-8],[6],[7],[-10],[5],[5],[4],[9],[7],[-2],[-9],[3],[-5],[-3],[-5],[-1],[-9],[2],[8],[-6],[1],[-8],[-3],[-1],[-10],[5],[8],[-7],[-10],[-1],[-9],[6],[1],[5],[-2],[-4],[-4],[6],[-3],[10],[-7],[-5],[4],[10],[-4],[-6],[7],[-10],[-10],[10],[8],[4],[8],[1],[-4],[7],[7],[-8],[1],[2],[-1],[8],[-10],[6],[5],[-3],[2],[9],[5],[5],[1],[5],[-1],[-7],[-3],[10],[7],[3],[8],[9],[-9],[-8],[-10],[-5],[5],[6],[-10],[-3],[6],[-5],[-1],[6],[-3],[-5],[-10],[4],[-9],[-2],[-9],[3],[5],[-1],[-10],[5],[-6],[-8],[5],[5],[3],[-7],[-8],[-6],[-3],[-3],[-3],[8],[6],[4],[6],[6],[10],[-9],[8],[-3],[7],[7],[2],[10],[10],[-8],[10],[5],[-5],[-5],[-8],[5],[5],[-5],[1],[3],[9],[-1],[3],[-6],[5],[-10],[-10],[-4],[-1],[10],[-10],[-1],[10],[-5],[5],[6],[9],[-5],[-9],[7],[-3],[-2],[1],[-9],[-4],[4],[-3],[-6],[-1],[1],[10],[10],[-7],[6],[-3],[1],[-2],[-10],[8],[5],[-8],[4],[2],[-4],[1],[-8],[7],[4],[10],[9],[3],[-9],[2],[5],[-1],[-1],[-9],[-2],[-5],[5],[4],[-10],[-3],[4],[-2],[-9],[4],[1],[-9],[7],[9],[9],[-3],[9],[9],[-5],[-1],[-5],[-7],[10],[-3],[-8],[8],[4],[-6],[-7],[7],[2],[-9],[9],[9],[1],[8],[4],[7],[9],[-2],[-9],[-6],[8],[-2],[-8],[-3],[10],[-3],[9],[2],[2],[10],[-7],[10],[6],[-3],[-2],[6],[3],[-7],[10],[3],[-3],[8],[10],[6],[1],[-10],[2],[4],[-3],[3],[-6],[-7],[10],[9],[-5],[9],[-1],[-4],[8],[-5],[-5],[-7],[4],[-2],[-8],[2],[5],[-10],[5],[-4],[-4],[-10],[9],[-7],[1],[6],[-4],[10],[-4],[-5],[-1],[-4],[-8],[3],[8],[4],[8],[8],[-8],[-4],[5],[-5],[-3],[-1],[1],[-1],[4],[-9],[2],[8],[9],[1],[-7],[-7],[-3],[4],[-1],[1],[5],[-4],[7],[-9],[1],[-5],[-3],[-4],[-6],[2],[-5],[6],[9],[6],[-10],[5],[8],[-2],[-5],[7],[-2],[-10],[5],[7],[-10],[-5],[-7],[-10],[3],[-6],[4],[6],[3],[6],[2],[3],[-6],[-9],[6],[4],[-5],[10],[10],[-8],[-8],[5],[10],[-2],[3],[10],[-1],[-9],[5],[-8],[6],[-8],[1],[-2],[-5],[-7],[7],[-5],[-5],[-9],[-6],[4],[-1],[4],[3],[-8],[6],[-9],[-1],[9],[3],[1],[7],[-8],[-4],[9],[-5],[5],[5],[1],[-3],[-6],[-4],[-5],[6],[-3],[1],[-1],[-1],[-3],[6],[-4],[6],[-7],[1],[9],[-7],[-3],[8],[8],[-6],[-2],[-6],[-7],[2],[3],[-1],[-8],[-6],[-8],[-5],[3],[1],[-4],[5],[-2],[-2],[8],[-9],[-8],[-5],[8],[-8],[1],[-5],[5],[5],[3],[3],[5],[-9],[9],[-5],[-1],[3],[5],[2],[2],[-4],[-6],[-3],[9],[8],[-1],[7],[-10],[-5],[10],[-7],[-4],[2],[-6],[5],[-4],[2],[-7],[2],[2],[6],[-2],[-1],[1],[-3],[-6],[4],[1],[-1],[8],[-9],[-4],[4],[-8],[5],[-8],[-3],[-6],[-5],[2],[10],[8],[-10],[-7],[8],[-7],[-10],[7],[-10],[4],[-5],[8],[5],[4],[-1],[-7],[4],[4],[-6],[5],[8],[10],[2],[-6],[2],[-10],[2],[-7],[-2],[-6],[7],[5],[-9],[-5],[1],[9],[-1],[9],[-6],[-8],[5],[-7],[5],[-2],[5],[1],[1],[3],[-6],[5],[10],[7],[2],[-7],[-3],[9],[2],[-4],[2],[-4],[-4],[-8],[3],[-7],[2],[8],[-7],[-5],[3],[9],[6],[3],[-6],[5],[-5],[-4],[5],[5],[3],[-1],[-5],[5],[6],[-1],[4],[6],[-2],[8],[-7],[5],[-3],[10],[10],[8],[-7],[-8],[-7],[-4],[-5],[-1],[-7],[-8],[7],[-6],[-10],[-4],[-1],[-1],[-10],[-6],[-9],[1],[7],[9],[10],[-10],[-9],[5],[-6],[-8],[-1],[9],[9],[-7],[-10],[-7],[-9],[-5],[4],[10],[-3],[1],[9],[-6],[5],[1],[-10],[-2],[-2],[-9],[-3],[-1],[7],[-9],[-7],[-4],[-1],[2],[1],[7],[6],[3],[-10],[-5],[5],[-5],[4],[-9],[10],[-1],[8],[9],[2],[-9],[1],[-8],[4],[3],[8],[6],[-3],[2],[-5],[-8],[10],[5],[-7],[-7],[-8],[-10],[4],[6],[-1],[2],[6],[-5],[-9],[8],[-7],[-10],[-8],[-6],[9],[-3],[-4],[6],[3],[6],[10],[7],[7],[8],[-8],[-9],[-3],[-3],[6],[-7],[5],[-4],[5],[6],[1],[-5],[-9],[-8],[2],[-4],[2],[-7],[-4],[7],[10],[-7],[-6],[-5],[-2],[-10],[-3],[5],[-7],[10],[-8],[-2],[-8],[7],[-7],[-4],[-10],[5],[3],[-6],[1],[9],[3],[7],[8],[9],[-2],[6],[8],[-3],[-10],[6],[-9],[6],[3],[8],[-10],[-7],[2],[4],[1],[-6],[4],[4],[7],[-1],[-6],[5],[-9],[1],[4],[5],[8],[-8],[-8],[-8],[6],[4],[6],[-4],[-7],[10],[-1],[1],[7],[-10],[-3],[7],[-7],[-10],[7],[-5],[-2],[5],[-9],[2],[3],[9],[6],[-1],[-6],[-2],[-6],[-8],[5],[-9],[10],[7],[5],[1],[-10],[-9],[-3],[-4],[10],[2],[6],[5],[-4],[-8],[-5],[-1],[-3],[6],[-10],[-1],[9],[3],[8],[-3],[-3],[-6],[-8],[5],[-6],[-8],[10],[-5],[-8],[10],[-7],[8],[10],[-10],[-9],[7],[-5],[-2],[-4],[4],[10],[10],[-5],[-2],[5],[1],[-4],[9],[-2],[-2],[-9],[2],[-2],[8],[1],[-7],[-8],[-10],[3],[4],[-7],[-1],[7],[5],[-9],[8],[-6],[4],[5],[5],[6],[9],[-8],[-6],[3],[10],[-6],[1],[2],[-3],[-4],[3],[-1],[9],[10],[4],[-3],[-1],[1],[3],[-7],[6],[-3],[9],[4],[8],[-2],[10],[-7],[3],[-3],[5],[-9],[-9],[4],[-8],[3],[6],[-10],[3],[8],[-6],[4],[8],[-6],[-1],[8],[-7],[4],[9],[7],[1],[-1],[8],[-6],[5],[-4],[-6],[6],[-10],[-5],[-3],[8],[-9],[-5],[-10],[-6],[-4],[10],[8],[5],[-9],[6],[-7],[-9],[7],[9],[4],[10],[-2],[4],[9],[5],[-6],[-5],[10],[-10],[9],[6],[10],[-5],[9],[7],[-3],[-9],[-3],[-5],[2],[4],[-6],[4],[9]], dtype = "int32")#candidate|4647|(2112, 1)|const|int32
var_4648 = relay.var("var_4648", dtype = "uint16", shape = (880,))#candidate|4648|(880,)|var|uint16
var_4649 = relay.var("var_4649", dtype = "float32", shape = (90, 2))#candidate|4649|(90, 2)|var|float32
var_4650 = relay.var("var_4650", dtype = "float64", shape = (704,))#candidate|4650|(704,)|var|float64
call_4646 = relay.TupleGetItem(func_3269_call(relay.reshape(const_4647.astype('int32'), [11, 16, 12]), relay.reshape(var_4648.astype('uint16'), [880,]), relay.reshape(var_4649.astype('float32'), [180,]), relay.reshape(var_4634.astype('int64'), [364,]), relay.reshape(var_4650.astype('float64'), [88, 8]), ), 0)
call_4651 = relay.TupleGetItem(func_3276_call(relay.reshape(const_4647.astype('int32'), [11, 16, 12]), relay.reshape(var_4648.astype('uint16'), [880,]), relay.reshape(var_4649.astype('float32'), [180,]), relay.reshape(var_4634.astype('int64'), [364,]), relay.reshape(var_4650.astype('float64'), [88, 8]), ), 0)
output = relay.Tuple([bop_4628,call_4633,var_4634,call_4646,const_4647,var_4648,var_4649,var_4650,])
output2 = relay.Tuple([bop_4628,call_4635,var_4634,call_4651,const_4647,var_4648,var_4649,var_4650,])
func_4652 = relay.Function([var_4626,var_4634,var_4648,var_4649,var_4650,], output)
mod['func_4652'] = func_4652
mod = relay.transform.InferType()(mod)
var_4653 = relay.var("var_4653", dtype = "int64", shape = ())#candidate|4653|()|var|int64
var_4654 = relay.var("var_4654", dtype = "int64", shape = (364,))#candidate|4654|(364,)|var|int64
var_4655 = relay.var("var_4655", dtype = "uint16", shape = (880,))#candidate|4655|(880,)|var|uint16
var_4656 = relay.var("var_4656", dtype = "float32", shape = (90, 2))#candidate|4656|(90, 2)|var|float32
var_4657 = relay.var("var_4657", dtype = "float64", shape = (704,))#candidate|4657|(704,)|var|float64
output = func_4652(var_4653,var_4654,var_4655,var_4656,var_4657,)
func_4658 = relay.Function([var_4653,var_4654,var_4655,var_4656,var_4657,], output)
mutated_mod['func_4658'] = func_4658
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4673 = relay.const([[[4.164426,-5.948080,8.773578,8.761389,-8.261771],[-9.687562,-5.036593,-5.210934,3.993671,-9.558172],[-3.857872,-0.415334,3.081597,-8.517468,0.108519],[2.559093,-7.540210,9.103003,-3.157326,6.453935],[-4.654219,-3.184690,1.557431,7.830434,-0.983371],[7.595876,-3.430418,-8.897949,-3.185595,5.015427],[5.835593,-6.602586,-3.908267,9.919674,-5.560454]],[[-7.265014,-2.519367,2.107155,7.497727,-7.410383],[9.145493,-6.495254,8.970989,5.666696,-3.607461],[7.210574,2.053985,8.500938,-9.674460,9.496185],[9.731528,8.520937,-4.654597,6.032040,8.130914],[3.349456,-0.680897,7.277141,3.126932,4.303837],[6.950257,7.855095,-8.334690,-6.562979,3.404753],[8.026145,6.852808,-3.931001,4.696865,-2.857561]],[[1.664908,9.179402,7.457139,4.058217,-0.063274],[-2.573572,1.887653,-6.290832,-3.541051,-0.788034],[-9.957388,-3.886345,7.831619,3.405031,5.243699],[9.617178,-9.405608,-2.339684,2.648973,-3.335638],[-0.201087,7.305983,-3.135471,8.591076,2.400116],[-4.666119,7.580200,5.990303,7.197781,9.625686],[-2.192736,1.805720,-7.648798,3.870873,7.296678]],[[3.252680,-6.479197,3.928222,-8.148864,-4.525508],[3.757672,-4.966043,2.144374,4.544794,-2.606750],[1.894656,4.164207,9.983118,-4.765049,-6.271543],[-4.250702,5.803444,-1.608332,2.865083,7.280639],[-7.351256,-7.250213,7.057029,6.188903,-5.303045],[-1.171075,-8.201329,-8.718863,6.697467,-1.393576],[-4.838769,8.594586,-0.693138,6.405974,-3.618614]],[[2.183099,0.576553,1.459003,5.930113,3.487082],[5.583648,-2.374888,7.435263,5.403148,5.371189],[-2.647957,6.936322,-1.865556,-6.047258,8.212638],[-2.765271,9.598902,5.743379,1.841919,9.181868],[-0.368151,-9.562374,0.225464,-9.653299,-0.949092],[-8.794744,3.431540,-7.000040,1.925379,4.592063],[3.398410,6.743978,4.449437,-5.573525,-2.621774]],[[3.503002,-6.915029,1.491063,-8.748181,-6.030614],[2.556539,4.469110,-0.691549,-1.730992,-1.853961],[9.336416,-5.273552,6.277595,8.739269,-6.918073],[1.683450,-8.243663,9.082253,9.106177,1.146238],[-6.846770,5.610504,-9.967749,5.732434,2.877162],[-6.891366,7.464670,-3.131444,3.644673,-6.661537],[3.456327,3.515002,2.123405,8.022231,-1.236274]],[[0.946087,1.408954,0.603534,-7.945142,2.060857],[-9.581232,-2.043005,-3.554937,-1.960006,-1.076104],[3.902361,8.990455,-6.432100,2.837626,6.418563],[-5.359376,-0.093184,4.365742,8.806369,-7.264000],[-0.069079,6.392202,-8.474447,5.279858,7.566244],[-0.989472,4.588450,9.434393,-8.206129,8.505972],[0.908587,-5.953044,1.445675,4.293963,-4.054315]],[[9.718318,-3.563867,9.403922,-7.481957,-9.017352],[0.872096,-6.392722,-5.991588,-1.160964,-8.083924],[-8.703973,4.992810,0.836062,4.661908,-3.305864],[-4.770799,-3.078976,-5.940595,-0.540115,-1.810812],[-8.665720,7.986806,-9.292750,-6.965658,-2.311225],[-0.712789,-2.902949,-4.915763,-7.061627,-7.632581],[8.612622,1.416544,-9.805522,7.692364,-8.169673]],[[3.958461,0.538696,-0.401440,-4.400309,-8.196683],[9.175085,3.737699,3.723434,-7.702579,1.370066],[-9.734791,8.334251,-2.462261,6.649384,-6.350730],[3.271481,-2.895720,-2.297452,-3.640600,8.034671],[-4.286105,9.152559,0.575775,5.598257,5.387640],[-4.799588,8.383302,3.730067,1.043624,7.601184],[-7.259276,4.507072,-2.116432,7.516643,-2.592643]],[[1.469696,-0.090861,6.624583,1.762355,2.942910],[6.834372,-1.217705,3.305479,5.543825,-2.801588],[8.486726,8.012399,6.524790,-3.660416,7.161586],[-9.194373,5.658898,8.186581,-8.203021,1.319086],[8.642536,0.273946,5.893890,6.445733,-3.993650],[-4.156676,0.471892,-8.419066,2.428650,0.990226],[-3.651517,5.957168,-9.103405,-9.476192,-0.596822]],[[-7.685825,-4.469810,5.308078,0.311602,-4.286702],[9.887947,7.959858,5.775155,4.644151,-0.852006],[6.319586,-7.656924,1.703900,8.910737,4.350881],[8.707883,-6.808808,-9.120184,-4.891068,-0.658907],[9.698865,2.871236,-8.577459,-8.388836,3.718180],[6.556751,9.602617,5.679454,-3.485553,-9.588237],[-1.290101,-6.437979,-1.443890,1.999568,-2.944306]]], dtype = "float64")#candidate|4673|(11, 7, 5)|const|float64
uop_4674 = relay.sinh(const_4673.astype('float64')) # shape=(11, 7, 5)
func_3802_call = mod.get_global_var('func_3802')
func_3804_call = mutated_mod.get_global_var('func_3804')
var_4679 = relay.var("var_4679", dtype = "float64", shape = (480,))#candidate|4679|(480,)|var|float64
call_4678 = func_3802_call(relay.reshape(var_4679.astype('float64'), [12, 4, 10]))
call_4680 = func_3802_call(relay.reshape(var_4679.astype('float64'), [12, 4, 10]))
output = relay.Tuple([uop_4674,call_4678,var_4679,])
output2 = relay.Tuple([uop_4674,call_4680,var_4679,])
func_4683 = relay.Function([var_4679,], output)
mod['func_4683'] = func_4683
mod = relay.transform.InferType()(mod)
var_4684 = relay.var("var_4684", dtype = "float64", shape = (480,))#candidate|4684|(480,)|var|float64
output = func_4683(var_4684)
func_4685 = relay.Function([var_4684], output)
mutated_mod['func_4685'] = func_4685
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4687 = relay.var("var_4687", dtype = "float32", shape = (5, 13, 4))#candidate|4687|(5, 13, 4)|var|float32
uop_4688 = relay.sigmoid(var_4687.astype('float32')) # shape=(5, 13, 4)
output = relay.Tuple([uop_4688,])
output2 = relay.Tuple([uop_4688,])
func_4693 = relay.Function([var_4687,], output)
mod['func_4693'] = func_4693
mod = relay.transform.InferType()(mod)
mutated_mod['func_4693'] = func_4693
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4694 = relay.var("var_4694", dtype = "float32", shape = (5, 13, 4))#candidate|4694|(5, 13, 4)|var|float32
func_4693_call = mutated_mod.get_global_var('func_4693')
call_4695 = func_4693_call(var_4694)
output = call_4695
func_4696 = relay.Function([var_4694], output)
mutated_mod['func_4696'] = func_4696
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5309 = relay.var("var_5309", dtype = "int64", shape = (13, 2, 15))#candidate|5309|(13, 2, 15)|var|int64
var_5310 = relay.var("var_5310", dtype = "int64", shape = (13, 2, 15))#candidate|5310|(13, 2, 15)|var|int64
bop_5311 = relay.not_equal(var_5309.astype('bool'), relay.reshape(var_5310.astype('bool'), relay.shape_of(var_5309))) # shape=(13, 2, 15)
uop_5318 = relay.atanh(var_5310.astype('float32')) # shape=(13, 2, 15)
uop_5322 = relay.log10(bop_5311.astype('float32')) # shape=(13, 2, 15)
func_3042_call = mod.get_global_var('func_3042')
func_3044_call = mutated_mod.get_global_var('func_3044')
var_5330 = relay.var("var_5330", dtype = "uint64", shape = (100,))#candidate|5330|(100,)|var|uint64
call_5329 = relay.TupleGetItem(func_3042_call(relay.reshape(var_5330.astype('uint64'), [5, 10, 2])), 1)
call_5331 = relay.TupleGetItem(func_3044_call(relay.reshape(var_5330.astype('uint64'), [5, 10, 2])), 1)
func_755_call = mod.get_global_var('func_755')
func_758_call = mutated_mod.get_global_var('func_758')
var_5338 = relay.var("var_5338", dtype = "int64", shape = (968,))#candidate|5338|(968,)|var|int64
const_5339 = relay.const(9, dtype = "uint64")#candidate|5339|()|const|uint64
call_5337 = relay.TupleGetItem(func_755_call(relay.reshape(var_5338.astype('int64'), [8, 11, 11]), relay.reshape(const_5339.astype('uint64'), []), ), 6)
call_5340 = relay.TupleGetItem(func_758_call(relay.reshape(var_5338.astype('int64'), [8, 11, 11]), relay.reshape(const_5339.astype('uint64'), []), ), 6)
output = relay.Tuple([uop_5318,uop_5322,call_5329,var_5330,call_5337,var_5338,const_5339,])
output2 = relay.Tuple([uop_5318,uop_5322,call_5331,var_5330,call_5340,var_5338,const_5339,])
func_5341 = relay.Function([var_5309,var_5310,var_5330,var_5338,], output)
mod['func_5341'] = func_5341
mod = relay.transform.InferType()(mod)
mutated_mod['func_5341'] = func_5341
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5341_call = mutated_mod.get_global_var('func_5341')
var_5343 = relay.var("var_5343", dtype = "int64", shape = (13, 2, 15))#candidate|5343|(13, 2, 15)|var|int64
var_5344 = relay.var("var_5344", dtype = "int64", shape = (13, 2, 15))#candidate|5344|(13, 2, 15)|var|int64
var_5345 = relay.var("var_5345", dtype = "uint64", shape = (100,))#candidate|5345|(100,)|var|uint64
var_5346 = relay.var("var_5346", dtype = "int64", shape = (968,))#candidate|5346|(968,)|var|int64
call_5342 = func_5341_call(var_5343,var_5344,var_5345,var_5346,)
output = call_5342
func_5347 = relay.Function([var_5343,var_5344,var_5345,var_5346,], output)
mutated_mod['func_5347'] = func_5347
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5554 = relay.const([[[4.558372,-6.810033,-2.155995,1.079766,-3.291114,1.971447],[8.995116,4.635934,5.393240,-5.838611,6.751968,-9.881766],[9.000492,9.133238,6.406749,0.657970,-9.685211,-8.812830],[-3.249247,-8.888736,4.864680,-3.084538,-1.885656,-2.343359],[-6.769265,-3.972779,3.996490,-9.197015,-1.826170,-3.912433],[-3.633200,-4.021109,0.137524,2.760862,0.141723,3.904437],[5.233470,7.755699,5.834393,1.800255,-2.221910,1.920718],[-1.950019,-9.947289,3.734723,-0.604789,4.290912,-4.675437],[-2.613233,-4.991714,-8.279672,-7.655009,-6.492689,2.848792]]], dtype = "float64")#candidate|5554|(1, 9, 6)|const|float64
const_5555 = relay.const([[[-3.606824,-5.938232,-8.140376,7.699017,4.057527,6.052126],[-4.616965,-5.196640,3.470867,-8.827017,-9.558785,4.008507],[-1.877691,-9.887888,-9.547284,-8.895248,-2.139732,4.835387],[3.205194,-4.515315,8.258702,8.492410,-8.130347,-5.864245],[6.433446,7.713713,8.238087,-5.404570,2.953438,-6.181460],[-6.901823,-4.253835,3.995517,7.679326,-6.565619,2.975710],[4.118936,1.322105,-9.484393,7.294762,8.659661,2.062142],[8.164127,-2.391086,-9.318838,-7.860371,0.342489,8.835892],[1.201917,-9.635528,4.978675,4.019327,-6.157242,-7.472547]],[[-9.172046,-3.272298,-7.090852,-8.287989,8.019739,-3.676266],[4.254325,-4.583563,4.344731,7.303147,-4.278785,-2.685118],[-8.858033,-4.958562,-8.495008,0.338117,-6.618472,-2.858340],[-4.489719,8.583187,-7.526065,1.352452,-2.175368,-5.505987],[-7.827103,-7.796418,7.071558,-0.218205,-8.302339,8.017348],[3.980653,1.763368,-6.563400,-4.274711,1.955264,0.453246],[9.783923,3.080674,-1.150588,6.381891,-3.277836,-0.045639],[-5.722350,6.445898,9.112768,1.440985,6.810689,2.459470],[2.091104,-4.563439,7.726648,-7.467106,3.078928,-5.704230]],[[7.859043,-4.558053,-8.137630,-5.221076,2.906931,7.698188],[-2.067811,2.325860,-0.472293,1.821050,-3.697284,-4.307423],[0.053211,-3.201686,-3.548067,5.225592,-2.548350,3.441847],[-4.169491,6.522637,9.207168,-4.146434,1.103420,-1.732656],[-5.583877,6.840823,6.773960,-4.703507,-7.052018,0.575674],[-6.199893,5.913495,-7.016755,5.852398,-1.186279,-6.264951],[9.331576,3.182328,-8.593378,-6.250556,5.969794,4.080564],[5.091676,-8.888834,-8.272300,1.609510,-1.101140,7.763353],[8.357844,5.695256,9.510403,-9.709603,-9.260296,-2.922631]],[[2.258307,-6.439110,-3.763935,1.842702,8.519238,-5.921756],[-1.960284,-7.545381,-1.484711,8.206017,-1.529941,4.491537],[9.862435,5.070347,6.169530,-9.060416,-1.505012,7.479849],[8.163319,4.973158,-2.143583,-2.682263,5.412268,5.009530],[8.900406,6.283341,1.642856,2.334092,-3.968675,1.990098],[-1.772138,-0.746087,-6.783128,-2.329154,5.740460,-0.981737],[9.000314,-2.040875,-7.423153,-9.142436,-8.285262,4.140218],[-0.701576,-4.946910,7.042485,-3.675160,-8.893993,6.338398],[-8.530438,-6.430704,9.941304,-9.534052,9.068528,4.378244]],[[-0.650876,9.645867,8.255354,4.106745,-2.256164,0.213961],[8.007486,3.620681,-5.281997,-8.375080,-9.730190,-4.253085],[4.838622,-1.146772,9.995217,-2.465437,8.823154,9.951683],[4.270735,-0.350243,-1.016864,4.902237,1.530894,5.400556],[2.190873,0.446522,-9.641696,0.212394,-4.951997,3.865823],[9.187812,9.676862,7.089944,-1.371121,6.621866,-9.824279],[-1.424431,3.474367,8.438441,2.223330,-7.798085,-5.671411],[9.567074,8.458368,-6.384065,8.167272,-8.100768,-2.543374],[8.593878,-8.118616,-0.359726,5.465046,3.596702,-8.348738]],[[3.200460,1.740781,-1.385812,8.734599,-2.353307,1.647243],[7.566930,-2.702068,-4.484236,0.320378,1.960686,-0.247481],[2.241449,-4.881886,1.752638,3.874283,7.469675,-0.164919],[-3.497929,3.955239,-7.649243,8.464680,7.854547,-0.656565],[4.245425,-0.923432,3.900192,-9.990881,-5.767284,8.769119],[3.996295,-5.749405,-8.028149,1.038613,-2.453294,6.144628],[3.059404,-6.423149,-8.451037,-7.576611,3.667676,2.013768],[-7.108911,1.643937,-1.442340,-0.112439,8.979098,-4.551514],[5.252386,-4.367503,-6.471450,9.154471,8.537941,9.352806]],[[-0.013077,1.205674,-0.840054,-9.605015,-3.901838,9.113945],[1.006337,-7.949476,-3.646440,-2.501052,-4.363911,-9.442902],[-5.444351,0.625661,1.340114,4.942198,-0.502318,6.054949],[6.409774,3.641432,7.387038,6.646380,-9.296578,2.869669],[-1.895345,0.342023,9.205936,-4.419829,6.951385,7.837344],[-6.776819,-7.995449,2.900979,2.024616,3.495107,-0.540023],[8.451412,0.033271,4.084117,-2.699838,-5.513770,9.060331],[9.045342,8.467652,9.918754,-1.385989,-7.171492,-3.548098],[-2.308635,-5.356719,7.939054,9.859815,-0.516927,-0.310711]],[[0.279564,-1.997623,-7.652829,5.334024,4.281223,-9.300539],[0.573623,-3.314336,5.008415,7.727905,-8.741646,-3.302066],[-5.573001,-1.719779,-3.850420,5.299589,1.436073,-5.667760],[1.713559,-9.220269,-9.322570,3.256440,3.214194,7.050618],[-7.290036,-2.829352,5.326453,-1.843639,-3.364127,-0.389259],[-8.682040,1.423252,7.740326,5.296620,8.904603,8.477312],[9.366245,-3.189320,-9.130617,3.938585,-1.226555,5.553588],[-8.074354,-1.729001,-4.369731,-0.441267,-7.606734,8.602279],[3.239997,-0.713765,-3.916660,-9.529519,-9.645840,-9.668115]],[[6.076703,9.605213,8.315395,4.923604,2.917391,7.677224],[-2.946352,-9.008139,0.500345,2.345416,-4.204790,9.654374],[8.145893,-4.509216,-4.147824,6.841688,6.421790,-4.213815],[6.470547,-1.578271,1.804482,6.487074,7.613045,-1.394545],[3.820307,3.670064,2.475095,-0.093353,1.994023,-2.660522],[9.570134,1.225136,-4.865019,7.402663,1.865147,-6.321666],[1.409616,-3.434371,8.855163,9.270472,-6.760776,3.422468],[-3.616055,3.403219,-1.857560,0.110659,2.252001,-6.944704],[-4.707803,6.121126,-2.813495,-4.864574,4.208585,-9.959183]],[[4.653322,3.657144,3.249524,7.367945,-3.635559,9.481075],[-6.258465,-8.029388,7.854249,-5.580417,9.166063,8.901577],[3.289905,8.037401,-9.925180,-8.348929,-0.548838,-8.932488],[-7.317970,3.349273,-2.393171,3.261520,7.779441,-4.773938],[2.386687,2.829744,-4.770677,-4.801351,-8.336638,4.425619],[7.465596,9.648471,7.126745,0.933855,6.518013,5.236906],[6.937453,9.825291,-5.124121,3.357265,-8.118123,-2.710992],[5.175793,-9.120301,3.321763,4.907596,6.994711,-0.865099],[-6.415448,-6.785533,-7.793673,9.084512,0.901864,-7.961705]],[[-3.324360,4.205711,-0.256170,1.355984,-7.237397,-7.657262],[0.273021,-5.074841,-2.093984,-4.281449,4.581952,-5.444157],[-9.128801,6.120110,-0.387643,7.007796,-9.945161,5.904265],[2.527002,-7.222873,1.500645,4.321215,-1.874201,2.279617],[-7.459227,5.520395,0.102249,0.475345,2.848450,7.139573],[-1.308095,-6.168166,2.607538,-2.062159,6.395635,-3.277534],[1.674002,9.534180,9.562207,-5.497425,-5.892842,0.953553],[6.622470,0.274789,-1.144314,1.921520,-9.032344,3.731108],[8.541923,-9.129083,-5.329174,6.056125,-4.448988,-7.180764]],[[-6.326637,3.773502,-1.156978,-5.934971,6.968218,5.016793],[-5.597381,-2.810978,-6.080891,-8.706762,2.634090,-8.211189],[0.116237,1.321815,4.713894,6.865214,-3.119529,-1.357052],[-9.963153,5.005008,3.306274,7.716796,3.615533,-7.892903],[6.971798,7.546563,6.182698,-2.559274,-8.619717,-6.885903],[4.744388,9.449323,-9.821288,9.926176,-0.956844,-5.023857],[4.220471,7.554042,5.775427,-7.868312,-7.023534,-9.583147],[-3.110970,-4.523292,-2.387201,-4.195476,-5.268887,-1.059591],[2.583500,9.215015,-2.270304,6.392683,5.480461,-4.629163]],[[-7.753874,4.290599,-6.909185,-9.070908,2.780461,7.026578],[8.936818,5.773009,7.248349,-8.601615,5.275706,-5.596162],[5.516398,8.667980,-1.603657,-7.071579,5.210048,0.355737],[6.012490,-8.182606,-2.591193,-0.132310,5.744726,-9.760508],[6.712777,1.381135,-4.267342,-5.493360,-5.328260,5.196379],[8.060803,2.551635,6.879943,2.046219,0.465940,6.936265],[6.067243,1.866857,-5.742481,-8.375925,2.195660,-3.693760],[8.074574,5.847304,3.071953,6.167436,-0.658267,2.415777],[2.271372,-9.819197,-7.303088,7.085597,-6.798411,-9.377764]],[[-1.954863,-8.267372,-3.775912,6.653443,-3.549078,9.088895],[7.250954,-8.579646,-5.226248,-4.533690,-1.040549,-8.657376],[-7.701286,4.526336,-4.623635,6.904030,-3.205236,-1.033871],[7.813086,-1.251542,0.303774,4.628484,-2.621927,-0.903988],[7.307830,9.811518,-8.839682,-0.508912,0.783904,0.649928],[9.885795,-4.823315,-4.978633,-8.938422,-7.802005,1.008731],[2.749215,3.178223,4.893755,-7.363101,-5.380936,-3.695921],[1.312964,2.195858,-5.310087,-3.817955,-6.787198,6.791402],[-0.691380,-4.284508,4.937226,-1.570041,-8.961014,-2.754634]],[[1.058446,-5.470850,-4.679130,-0.997955,5.492505,-9.264583],[-6.628912,5.952557,0.013725,-8.497680,-3.274225,4.777313],[-7.055159,-2.339240,0.021634,-6.471479,3.432401,-7.860326],[-6.486861,4.691691,-9.119062,1.596144,0.669354,9.109258],[-6.445980,-7.060277,-1.257276,-1.022835,1.688142,1.822610],[1.370935,8.364804,-7.348662,3.495805,4.657453,-6.704129],[-9.520398,-6.458378,-0.563196,7.812114,8.240851,-4.620030],[9.834897,8.140486,3.672166,5.131715,-6.322906,-8.207337],[-3.720815,6.093371,-0.184638,8.973900,-2.504439,-2.897210]]], dtype = "float64")#candidate|5555|(15, 9, 6)|const|float64
bop_5556 = relay.minimum(const_5554.astype('float64'), const_5555.astype('float64')) # shape=(15, 9, 6)
output = relay.Tuple([bop_5556,])
output2 = relay.Tuple([bop_5556,])
func_5560 = relay.Function([], output)
mod['func_5560'] = func_5560
mod = relay.transform.InferType()(mod)
output = func_5560()
func_5561 = relay.Function([], output)
mutated_mod['func_5561'] = func_5561
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5585 = relay.const([[[1.917286,-9.696021,-5.858124,0.898168,-8.050915,-4.429181,4.897667,-0.943846,-5.573888,-3.810998,8.486882,0.928585,1.933861],[-8.264794,-9.294696,-1.355637,-1.879076,-1.420064,-9.858790,1.962115,-0.178624,-1.509306,2.396998,-9.523698,9.650069,-3.092671]],[[-2.274739,-6.805253,-9.516301,-8.556552,-1.628459,-9.485457,-2.563862,7.289101,7.000911,0.351543,3.132478,7.781934,-7.230414],[-5.220603,-1.807414,0.310777,-2.089156,-8.138727,-0.860629,4.247891,0.308511,1.877618,-4.114299,2.352117,4.065668,4.546660]],[[-2.979460,4.251662,4.994725,-8.131385,6.965799,-8.910466,7.122430,-0.565921,6.056702,4.175189,6.297350,-1.104681,1.875766],[9.426863,9.249889,0.433496,4.625851,-4.236552,-8.481309,0.012603,-1.185456,-0.184838,-8.127679,7.570444,-0.867831,2.236584]],[[-5.043497,-9.949113,9.168876,-6.475994,-1.440740,-2.332089,0.676044,-3.878630,-0.441683,7.634594,6.326437,-3.457999,-6.687441],[-6.415695,-6.297281,-9.207325,0.408172,8.989524,6.830200,1.609500,6.998811,8.895630,1.571794,8.822539,1.103795,-3.205104]]], dtype = "float32")#candidate|5585|(4, 2, 13)|const|float32
uop_5586 = relay.log(const_5585.astype('float32')) # shape=(4, 2, 13)
uop_5589 = relay.erf(uop_5586.astype('float64')) # shape=(4, 2, 13)
func_5341_call = mod.get_global_var('func_5341')
func_5347_call = mutated_mod.get_global_var('func_5347')
var_5600 = relay.var("var_5600", dtype = "int64", shape = (390,))#candidate|5600|(390,)|var|int64
const_5601 = relay.const([10,-3,9,3,-2,5,3,9,-10,-2,3,8,-1,5,3,-4,-9,9,8,9,6,2,-9,5,-1,4,-3,8,-5,3,-6,10,-3,-5,-10,3,-10,9,-5,-1,-1,2,9,9,6,-3,-8,-8,-9,-4,-9,7,1,3,10,4,-10,9,-8,-5,-10,-7,-1,-9,-9,-1,9,10,-6,6,8,1,-8,-9,-7,-1,5,7,-4,-6,1,-1,-7,-10,5,-9,8,1,10,-2,-6,-6,-2,5,-1,-7,8,3,-1,8], dtype = "uint64")#candidate|5601|(100,)|const|uint64
const_5602 = relay.const([-9,7,-2,-1,4,7,8,-4,3,4,8,-10,-9,3,6,-4,-10,-4,10,7,3,-3,-3,-6,4,8,3,-2,8,-2,9,7,9,-2,-9,2,-2,4,3,4,9,-7,10,7,-7,2,4,-5,-3,1,-9,3,-7,-7,-7,6,-2,8,-4,-10,5,7,3,2,3,5,4,3,7,2,10,-9,2,-4,6,9,8,-1,-10,-5,4,-4,2,-2,7,2,-1,-10,2,-1,-10,10,-6,8,-3,8,-7,-8,10,-7,-3,4,3,6,10,6,8,9,-8,-10,4,-10,10,9,7,7,-6,-3,7,-6,9,-8,-9,-8,5,-8,8,9,4,-8,-5,-3,9,10,7,2,6,-10,-6,2,8,2,5,-4,1,-4,-10,-5,-4,5,-1,-5,9,-3,-8,8,-2,4,4,-10,1,-9,-10,-9,1,4,-3,10,8,6,-6,-4,7,-8,5,3,-2,6,-1,6,1,4,3,-5,-5,7,-7,2,8,-2,1,-10,10,-7,-2,-4,5,8,-2,-8,-4,-2,7,-5,-5,-1,-2,9,6,-4,-9,1,6,1,-2,9,-6,-9,5,10,-8,-8,2,4,-3,6,7,-5,9,-3,5,-9,2,-3,-1,-9,-6,1,4,5,8,-1,-9,9,2,-8,-3,7,-4,-2,-7,-4,-10,2,4,3,-9,6,9,-7,-5,-8,-2,4,7,-3,-1,-7,3,4,7,9,10,-3,9,1,-4,4,4,-4,-8,-3,-5,9,-10,-9,-8,10,-4,-8,4,8,-8,6,2,5,8,-8,-10,4,8,6,10,6,10,6,5,2,8,-9,7,-10,-4,9,-3,-4,6,1,-8,1,-2,4,3,-3,5,1,6,8,-8,-5,-3,6,-1,-7,-3,-8,7,4,-9,3,1,-5,-3,-8,-3,-4,2,-6,-4,-1,-1,-3,9,10,-4,-2,-7,1,-4,-1,-2,3,-4,4,-2,-8,-1,3,8,-10,8,-7,-2,3,9,-1,10,2,3,-3,-10,9,-1,5,-8,2,-8,-9,9,-4,-5,-9,1,10,-9,10,-5,3,1,-5,-5,-3,6,-3,3,3,-6,-4,6,-2,8,-6,-1,8,7,1,10,6,5,3,9,-7,-10,4,4,1,-8,-6,6,-10,-9,8,4,-7,3,8,-8,9,-5,-6,-10,2,5,-8,-2,-5,-1,2,7,6,-1,-4,-9,-9,-7,-3,1,5,-1,-7,1,-6,5,8,7,-1,-8,7,7,2,-8,-9,8,5,8,6,5,2,8,-1,-7,5,-5,-5,-8,-6,-1,7,10,-1,-5,-8,9,-2,3,3,-6,-5,1,-5,6,5,-6,-7,6,5,-6,-4,4,-3,-9,-6,5,8,-1,2,2,-3,2,5,9,-1,-2,10,-3,2,7,7,-9,-7,5,6,-9,-6,-8,-8,10,1,-6,-5,-4,-1,4,5,2,-2,3,6,6,2,-4,2,-2,3,4,9,6,-10,-7,-4,7,7,5,-2,7,6,8,5,-2,10,-10,-3,8,-9,-8,-3,2,-5,-5,-9,-4,-4,-4,4,1,2,-4,8,-8,-6,-3,-1,1,1,4,-10,6,3,-5,5,-3,-5,-4,9,-3,8,6,-8,-7,2,-8,2,-6,-5,-3,7,7,-1,9,3,-4,6,4,6,-5,-5,-3,-9,3,2,-2,10,-4,-2,-2,5,-10,6,4,-5,2,-2,-8,-6,4,-7,-8,8,9,-7,7,-6,10,10,4,3,-5,1,-7,-4,-4,7,-7,7,7,6,-3,-2,2,9,9,-2,-8,-8,7,-5,-3,6,-9,6,5,1,-2,-1,9,10,1,-2,2,-5,2,-3,-2,4,10,-7,-2,4,-5,10,-4,-10,4,-5,4,7,-10,2,9,-1,-10,5,9,7,4,-8,8,7,-1,-10,2,2,8,-4,-4,8,-5,5,2,-8,9,-9,5,1,-6,-1,-8,2,1,-5,-1,8,-7,2,4,8,-7,10,-10,-7,2,9,-5,8,-7,10,5,5,-10,1,-8,-7,5,6,2,6,-3,4,5,1,-4,-1,-10,10,5,6,-10,10,-2,-3,-2,-8,5,3,5,-4,-7,-7,3,-7,-7,-4,5,4,-10,4,7,7,6,-2,3,8,-10,9,10,-4,8,-6,9,2,1,1,6,2,7,-2,1,-2,-5,-6,6,4,5,-7,-3,4,-5,-4,5,4,1,2,-6,-2,-5,5,-8,5,10,8,3,9,-8,-8,10,-5,-7,-2,-5,-3,-5,-2,-9,4,1,5,5,1,-7,-8,-2,-8,2,-4,-6,-7,-5,-4,10,-6,-2,-6,-4,-2,-7,-10,1,-9,-9,2,-10,-4,10,1,-8,2,7,6,-4,-4,7,1,3,-5,-5,-6,5,-1,-10,6,9,-7,-5,-8,1,1,8,-8,-6,-1,-7,5,9,-9,-8,8,-5,4,5,-9,5,-4,4,6,-2,-10,-6,-3,2,-7,-10,-8,7,3,5,10,-3,-5,-6,-8,9,-9,6,-3,7,1,-2,-10,-2,-3,-8,8,-7,10,-5,-2,-10,-3,-5,7,6,-9,8,9,6,-6,5,6], dtype = "int64")#candidate|5602|(968,)|const|int64
call_5599 = relay.TupleGetItem(func_5341_call(relay.reshape(var_5600.astype('int64'), [13, 2, 15]), relay.reshape(var_5600.astype('int64'), [13, 2, 15]), relay.reshape(const_5601.astype('uint64'), [100,]), relay.reshape(const_5602.astype('int64'), [968,]), ), 6)
call_5603 = relay.TupleGetItem(func_5347_call(relay.reshape(var_5600.astype('int64'), [13, 2, 15]), relay.reshape(var_5600.astype('int64'), [13, 2, 15]), relay.reshape(const_5601.astype('uint64'), [100,]), relay.reshape(const_5602.astype('int64'), [968,]), ), 6)
func_2768_call = mod.get_global_var('func_2768')
func_2771_call = mutated_mod.get_global_var('func_2771')
var_5606 = relay.var("var_5606", dtype = "float64", shape = (180,))#candidate|5606|(180,)|var|float64
call_5605 = func_2768_call(relay.reshape(var_5606.astype('float64'), [6, 15, 2]))
call_5607 = func_2768_call(relay.reshape(var_5606.astype('float64'), [6, 15, 2]))
func_2239_call = mod.get_global_var('func_2239')
func_2241_call = mutated_mod.get_global_var('func_2241')
var_5612 = relay.var("var_5612", dtype = "float32", shape = (56,))#candidate|5612|(56,)|var|float32
call_5611 = relay.TupleGetItem(func_2239_call(relay.reshape(var_5612.astype('float32'), [7, 1, 8])), 1)
call_5613 = relay.TupleGetItem(func_2241_call(relay.reshape(var_5612.astype('float32'), [7, 1, 8])), 1)
func_3623_call = mod.get_global_var('func_3623')
func_3625_call = mutated_mod.get_global_var('func_3625')
var_5645 = relay.var("var_5645", dtype = "float64", shape = (7, 78))#candidate|5645|(7, 78)|var|float64
call_5644 = func_3623_call(relay.reshape(var_5645.astype('float64'), [13, 14, 3]))
call_5646 = func_3623_call(relay.reshape(var_5645.astype('float64'), [13, 14, 3]))
output = relay.Tuple([uop_5589,call_5599,var_5600,const_5601,const_5602,call_5605,var_5606,call_5611,var_5612,call_5644,var_5645,])
output2 = relay.Tuple([uop_5589,call_5603,var_5600,const_5601,const_5602,call_5607,var_5606,call_5613,var_5612,call_5646,var_5645,])
func_5655 = relay.Function([var_5600,var_5606,var_5612,var_5645,], output)
mod['func_5655'] = func_5655
mod = relay.transform.InferType()(mod)
mutated_mod['func_5655'] = func_5655
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5655_call = mutated_mod.get_global_var('func_5655')
var_5657 = relay.var("var_5657", dtype = "int64", shape = (390,))#candidate|5657|(390,)|var|int64
var_5658 = relay.var("var_5658", dtype = "float64", shape = (180,))#candidate|5658|(180,)|var|float64
var_5659 = relay.var("var_5659", dtype = "float32", shape = (56,))#candidate|5659|(56,)|var|float32
var_5660 = relay.var("var_5660", dtype = "float64", shape = (7, 78))#candidate|5660|(7, 78)|var|float64
call_5656 = func_5655_call(var_5657,var_5658,var_5659,var_5660,)
output = call_5656
func_5661 = relay.Function([var_5657,var_5658,var_5659,var_5660,], output)
mutated_mod['func_5661'] = func_5661
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5560_call = mod.get_global_var('func_5560')
func_5561_call = mutated_mod.get_global_var('func_5561')
call_5670 = relay.TupleGetItem(func_5560_call(), 0)
call_5671 = relay.TupleGetItem(func_5561_call(), 0)
output = call_5670
output2 = call_5671
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
func_5674_call = mod.get_global_var('func_5674')
func_5676_call = mutated_mod.get_global_var('func_5676')
call_5710 = func_5674_call()
call_5711 = func_5674_call()
output = relay.Tuple([call_5710,])
output2 = relay.Tuple([call_5711,])
func_5717 = relay.Function([], output)
mod['func_5717'] = func_5717
mod = relay.transform.InferType()(mod)
output = func_5717()
func_5718 = relay.Function([], output)
mutated_mod['func_5718'] = func_5718
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5674_call = mod.get_global_var('func_5674')
func_5676_call = mutated_mod.get_global_var('func_5676')
call_5725 = func_5674_call()
call_5726 = func_5674_call()
output = relay.Tuple([call_5725,])
output2 = relay.Tuple([call_5726,])
func_5727 = relay.Function([], output)
mod['func_5727'] = func_5727
mod = relay.transform.InferType()(mod)
output = func_5727()
func_5728 = relay.Function([], output)
mutated_mod['func_5728'] = func_5728
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5727_call = mod.get_global_var('func_5727')
func_5728_call = mutated_mod.get_global_var('func_5728')
call_5743 = relay.TupleGetItem(func_5727_call(), 0)
call_5744 = relay.TupleGetItem(func_5728_call(), 0)
func_2239_call = mod.get_global_var('func_2239')
func_2241_call = mutated_mod.get_global_var('func_2241')
var_5763 = relay.var("var_5763", dtype = "float32", shape = (56,))#candidate|5763|(56,)|var|float32
call_5762 = relay.TupleGetItem(func_2239_call(relay.reshape(var_5763.astype('float32'), [7, 1, 8])), 1)
call_5764 = relay.TupleGetItem(func_2241_call(relay.reshape(var_5763.astype('float32'), [7, 1, 8])), 1)
output = relay.Tuple([call_5743,call_5762,var_5763,])
output2 = relay.Tuple([call_5744,call_5764,var_5763,])
func_5791 = relay.Function([var_5763,], output)
mod['func_5791'] = func_5791
mod = relay.transform.InferType()(mod)
mutated_mod['func_5791'] = func_5791
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5792 = relay.var("var_5792", dtype = "float32", shape = (56,))#candidate|5792|(56,)|var|float32
func_5791_call = mutated_mod.get_global_var('func_5791')
call_5793 = func_5791_call(var_5792)
output = call_5793
func_5794 = relay.Function([var_5792], output)
mutated_mod['func_5794'] = func_5794
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5717_call = mod.get_global_var('func_5717')
func_5718_call = mutated_mod.get_global_var('func_5718')
call_6014 = relay.TupleGetItem(func_5717_call(), 0)
call_6015 = relay.TupleGetItem(func_5718_call(), 0)
uop_6017 = relay.sqrt(call_6014.astype('float32')) # shape=(15, 9, 6)
uop_6019 = relay.sqrt(call_6015.astype('float32')) # shape=(15, 9, 6)
uop_6020 = relay.atan(call_6014.astype('float64')) # shape=(15, 9, 6)
uop_6022 = relay.atan(call_6015.astype('float64')) # shape=(15, 9, 6)
output = relay.Tuple([uop_6017,uop_6020,])
output2 = relay.Tuple([uop_6019,uop_6022,])
func_6025 = relay.Function([], output)
mod['func_6025'] = func_6025
mod = relay.transform.InferType()(mod)
output = func_6025()
func_6026 = relay.Function([], output)
mutated_mod['func_6026'] = func_6026
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6025_call = mod.get_global_var('func_6025')
func_6026_call = mutated_mod.get_global_var('func_6026')
call_6042 = relay.TupleGetItem(func_6025_call(), 1)
call_6043 = relay.TupleGetItem(func_6026_call(), 1)
func_4652_call = mod.get_global_var('func_4652')
func_4658_call = mutated_mod.get_global_var('func_4658')
const_6057 = relay.const(10, dtype = "int64")#candidate|6057|()|const|int64
const_6058 = relay.const([-6,-7,-4,7,3,3,10,-8,7,9,-3,6,4,1,3,-1,10,-8,-10,-6,-8,2,2,5,5,1,-4,9,-4,-1,8,-6,1,-3,-8,-5,-5,4,-8,-9,4,-10,4,6,10,4,3,-6,-5,7,-5,-10,9,2,-5,-4,-10,7,4,1,-5,1,7,2,4,7,-2,-4,3,10,-6,6,9,-7,1,4,-4,-3,2,-5,3,-10,9,5,9,-9,-2,-8,-10,-3,-4,6,1,1,3,2,9,2,-3,9,4,4,3,-6,-8,4,5,-9,7,2,7,-7,-5,4,8,1,-1,8,8,7,-5,5,10,8,6,-9,-3,9,5,-7,7,7,-2,2,-10,-5,3,-7,-6,2,5,4,8,-8,-7,8,-3,-1,-9,-7,5,6,-2,1,-5,9,-4,10,10,-7,-4,-2,1,6,-8,10,4,1,8,3,5,-7,-7,-1,6,-4,6,-1,-1,6,7,5,6,7,-10,-9,-4,-3,3,8,3,-4,-9,-5,-10,-2,-9,-10,4,8,10,8,6,-5,-7,-10,8,-9,-7,-9,-5,5,9,10,-5,-7,8,10,-7,4,-9,-4,8,-6,-8,-3,-6,-1,-6,-8,9,-9,-1,2,-4,-3,1,-2,3,-6,-2,7,9,-5,-9,9,8,-7,-7,-8,5,7,-3,7,-6,-8,-3,-8,-3,9,-4,1,8,-3,-9,7,-4,-2,-5,2,1,10,7,8,1,-3,8,8,-2,-3,4,4,6,7,-4,-3,-3,1,-2,-1,6,7,9,-2,-8,3,4,-2,-5,2,-9,6,-7,-1,6,10,-9,-8,4,-1,-4,4,4,-10,4,8,-4,-3,-5,-10,10,5,-8,-6,-4,3,-1,-7,3,-4,9,8,10,6,10,6,-7,7,-5,-6,-10,-8,7,8,5,5,-7,9,8,3,-1,-6,-2,-4,6,8,10,-10,5,7,3,-2,-6,-8], dtype = "int64")#candidate|6058|(364,)|const|int64
var_6059 = relay.var("var_6059", dtype = "uint16", shape = (40, 22))#candidate|6059|(40, 22)|var|uint16
const_6060 = relay.const([9.692938,-0.595743,-1.122338,7.712538,2.038479,-6.776432,-3.947970,1.746292,2.866298,-0.380854,-0.793745,4.011357,3.761110,2.040504,-5.669927,-6.404850,1.813279,-4.339531,-8.230639,5.300690,2.855586,3.399756,0.510184,2.400749,-9.176668,-0.872609,-8.416269,0.728550,9.893974,-9.360605,-5.544634,-7.804073,1.526570,3.976510,-5.409494,6.204390,-2.689201,4.118670,5.066645,-6.653966,-7.741608,-9.159815,6.466460,-8.529384,4.968873,-2.283571,3.252058,8.788407,4.087531,6.314931,-3.813697,-4.915243,0.617372,-2.050400,-5.535179,1.935239,2.075087,6.785122,6.631717,1.020233,1.739748,-0.795626,-7.627164,8.293072,2.360956,3.502379,-9.505283,-3.902171,3.855822,-9.715380,-1.807315,-3.472609,-6.006723,-9.847921,-7.780287,-0.036926,2.101199,-4.307683,-9.506843,8.455512,-3.895142,9.322947,-0.065452,2.086833,-6.746781,4.150115,2.681687,-9.207859,-9.338664,1.860215,3.238979,-6.395290,2.155624,-4.797619,-9.065475,4.790466,7.362073,5.492843,-7.802760,9.765717,2.406483,6.690456,9.007012,-0.954722,-1.983567,-9.374024,7.281773,-4.482128,5.665394,-5.933187,0.152546,0.046736,5.865368,-1.575123,4.776101,-1.800612,6.020017,1.914670,-6.999612,-0.838006,2.442013,-9.902597,2.346217,8.471989,7.454007,-1.575571,8.691808,6.097447,1.578848,1.179040,-0.389259,5.395813,0.137168,-5.948144,-9.092613,7.317925,9.758068,-4.385312,-0.762495,5.788151,3.367806,-1.053232,3.295886,3.743191,-0.464965,3.332667,8.513547,-2.258980,6.021957,-9.826173,2.576290,-7.914708,3.778953,3.539931,-5.857836,2.147740,-3.122083,8.672595,-0.527787,-6.470218,4.911458,5.175785,-3.006585,1.737581,-8.525489,8.982965,2.481969,-9.895944,-2.495206,5.245256,-3.507743,9.617015,-4.945370,4.873257,2.849078,8.527950,2.196665,0.898682,-0.591449,-4.962560], dtype = "float32")#candidate|6060|(180,)|const|float32
var_6061 = relay.var("var_6061", dtype = "float64", shape = (704,))#candidate|6061|(704,)|var|float64
call_6056 = relay.TupleGetItem(func_4652_call(relay.reshape(const_6057.astype('int64'), []), relay.reshape(const_6058.astype('int64'), [364,]), relay.reshape(var_6059.astype('uint16'), [880,]), relay.reshape(const_6060.astype('float32'), [90, 2]), relay.reshape(var_6061.astype('float64'), [704,]), ), 5)
call_6062 = relay.TupleGetItem(func_4658_call(relay.reshape(const_6057.astype('int64'), []), relay.reshape(const_6058.astype('int64'), [364,]), relay.reshape(var_6059.astype('uint16'), [880,]), relay.reshape(const_6060.astype('float32'), [90, 2]), relay.reshape(var_6061.astype('float64'), [704,]), ), 5)
bop_6064 = relay.right_shift(var_6061.astype('uint64'), const_6057.astype('uint64')) # shape=(704,)
func_1763_call = mod.get_global_var('func_1763')
func_1768_call = mutated_mod.get_global_var('func_1768')
var_6072 = relay.var("var_6072", dtype = "int64", shape = (968,))#candidate|6072|(968,)|var|int64
call_6071 = relay.TupleGetItem(func_1763_call(relay.reshape(const_6060.astype('float32'), [5, 9, 4]), relay.reshape(var_6072.astype('int64'), [968,]), relay.reshape(const_6058.astype('int64'), [364,]), ), 1)
call_6073 = relay.TupleGetItem(func_1768_call(relay.reshape(const_6060.astype('float32'), [5, 9, 4]), relay.reshape(var_6072.astype('int64'), [968,]), relay.reshape(const_6058.astype('int64'), [364,]), ), 1)
output = relay.Tuple([call_6042,call_6056,const_6058,var_6059,const_6060,bop_6064,call_6071,var_6072,])
output2 = relay.Tuple([call_6043,call_6062,const_6058,var_6059,const_6060,bop_6064,call_6073,var_6072,])
func_6080 = relay.Function([var_6059,var_6061,var_6072,], output)
mod['func_6080'] = func_6080
mod = relay.transform.InferType()(mod)
mutated_mod['func_6080'] = func_6080
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6080_call = mutated_mod.get_global_var('func_6080')
var_6082 = relay.var("var_6082", dtype = "uint16", shape = (40, 22))#candidate|6082|(40, 22)|var|uint16
var_6083 = relay.var("var_6083", dtype = "float64", shape = (704,))#candidate|6083|(704,)|var|float64
var_6084 = relay.var("var_6084", dtype = "int64", shape = (968,))#candidate|6084|(968,)|var|int64
call_6081 = func_6080_call(var_6082,var_6083,var_6084,)
output = call_6081
func_6085 = relay.Function([var_6082,var_6083,var_6084,], output)
mutated_mod['func_6085'] = func_6085
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6025_call = mod.get_global_var('func_6025')
func_6026_call = mutated_mod.get_global_var('func_6026')
call_6147 = relay.TupleGetItem(func_6025_call(), 1)
call_6148 = relay.TupleGetItem(func_6026_call(), 1)
uop_6149 = relay.cosh(call_6147.astype('float32')) # shape=(15, 9, 6)
uop_6151 = relay.cosh(call_6148.astype('float32')) # shape=(15, 9, 6)
output = relay.Tuple([uop_6149,])
output2 = relay.Tuple([uop_6151,])
func_6187 = relay.Function([], output)
mod['func_6187'] = func_6187
mod = relay.transform.InferType()(mod)
output = func_6187()
func_6188 = relay.Function([], output)
mutated_mod['func_6188'] = func_6188
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5727_call = mod.get_global_var('func_5727')
func_5728_call = mutated_mod.get_global_var('func_5728')
call_6281 = relay.TupleGetItem(func_5727_call(), 0)
call_6282 = relay.TupleGetItem(func_5728_call(), 0)
uop_6287 = relay.rsqrt(call_6281.astype('float32')) # shape=(15, 9, 6)
uop_6289 = relay.rsqrt(call_6282.astype('float32')) # shape=(15, 9, 6)
func_3623_call = mod.get_global_var('func_3623')
func_3625_call = mutated_mod.get_global_var('func_3625')
const_6294 = relay.const([5.855013,-8.119822,0.287503,6.956108,-1.819555,-1.753161,3.867150,-9.248879,-8.018027,-7.157940,-6.472307,-0.890235,-9.494650,9.422274,-9.400950,0.036928,-6.234727,-1.770542,-4.134186,-4.567426,-2.600791,-2.857020,-7.233784,0.800173,6.606497,9.867365,2.873143,-4.851394,-1.197574,9.160014,-9.845787,1.280644,-6.615679,-8.224594,0.777772,1.426962,-1.154840,5.925676,7.812891,0.452463,3.902780,-4.741673,-8.324700,-6.906798,-3.121665,3.499604,4.719555,7.861958,-7.114977,-2.288374,0.841085,3.039835,8.928469,-4.009026,-5.469061,0.596047,5.248311,-4.783315,4.734265,-0.430021,-5.775607,-4.259815,-9.931264,-6.858105,-9.821002,6.313137,-9.234772,0.345936,1.598425,-7.202820,1.302381,1.793301,-0.071923,1.457899,6.822250,8.649491,5.589481,9.796007,-4.026344,0.883248,-0.296126,-5.116010,3.517305,5.505382,4.402564,-9.494066,2.496762,2.078120,6.132003,1.486999,3.235960,7.367723,2.928727,-8.601917,-5.967892,-4.724763,-9.723819,8.934202,-3.990556,1.465516,7.948774,-2.909632,1.094163,-2.474881,-6.759855,4.279379,-5.410011,2.053160,4.357776,2.517897,4.985768,7.592688,-2.523206,6.225255,7.716859,5.848432,5.960147,6.664647,5.249596,8.336463,-5.450073,8.279233,9.417742,-1.916043,6.978105,-4.686692,1.425539,-0.424312,7.586992,-3.149002,-7.140667,0.019637,8.597890,4.250298,-9.244381,7.856706,3.079997,7.932837,0.237553,-9.383531,-7.938673,5.974690,-8.941658,5.420948,0.627746,-7.073168,6.004503,4.816439,-5.025258,-8.949016,-2.441445,7.103750,-4.530407,-2.939829,-5.648893,-1.944643,-1.520885,-3.731441,-0.667304,-0.159951,7.056985,6.808189,-8.597551,-3.901053,4.005053,3.068690,-6.698927,-4.034385,8.513953,-4.161568,1.628809,-0.630883,-2.265520,-5.225528,0.624561,-4.051023,9.686566,9.161866,6.906651,-3.646062,-7.538344,-8.694957,7.798993,-1.047982,7.522834,-2.259843,0.096108,-1.339235,-5.129691,-8.825969,8.788392,-4.339511,0.157854,-0.066060,3.041882,8.054841,-7.787615,-9.297813,-1.309257,4.756732,3.983594,-7.710770,-1.122819,-0.343571,7.029969,-7.219990,-9.541893,7.194021,1.513072,-3.169828,4.451825,-7.951600,7.161456,9.672065,3.364676,0.317048,-8.539523,-3.233377,0.567157,9.728182,1.454069,8.921186,8.442691,5.843100,7.847270,3.497162,-2.775786,-9.032214,2.219709,8.681245,-3.838797,2.347578,2.778367,-5.766255,6.437499,2.253447,4.368416,-0.876495,-9.868062,3.042290,9.785070,-3.123067,5.455263,7.694504,-9.573253,8.574560,1.328944,4.886997,-1.903709,3.768823,-6.759695,2.584192,-8.616899,-8.806381,0.249891,-6.211069,-9.668261,-2.641442,5.064887,-7.231975,1.921787,4.420735,3.491412,7.448539,-0.563826,3.338320,4.561397,-4.265395,-4.435167,-7.128715,2.905320,-4.254227,9.356446,1.265397,-5.103264,-8.880445,9.680570,-4.856822,7.108330,9.629159,2.553106,-4.770763,7.681916,-1.962880,8.073516,6.629027,4.111857,-8.726599,7.877098,1.489672,-4.072347,4.669559,6.962312,-3.198318,5.292900,-7.191938,-4.414854,8.812453,-6.475059,5.837515,0.285969,-5.018124,-2.965698,1.616950,-0.077908,1.997375,0.603906,-8.551730,-1.653328,8.827286,-1.284165,-1.744556,-1.515473,-5.456561,3.004471,-8.950840,8.265582,5.159330,6.765436,7.422323,-4.156514,-8.596002,1.742342,-9.966861,2.534208,7.513100,-8.117525,-0.939772,2.714124,9.450735,-7.409073,1.572774,-4.272771,3.692352,-6.943521,2.955546,5.661397,-3.218431,-0.065255,0.821093,-6.086831,-0.602464,-7.517426,6.177080,3.432544,6.466270,-8.568657,5.161838,3.009153,-6.623168,0.551626,-1.341993,-8.641084,4.869813,-2.479063,-2.885482,2.274888,1.587110,-1.377689,-9.340337,2.427004,2.034784,-5.657054,-8.694468,-7.865617,9.588496,-1.028157,-2.235659,-7.844496,9.303415,-1.105170,1.456725,-8.351028,-5.410193,5.378984,5.895877,-2.376767,-9.398783,8.666671,-5.919522,-9.507528,-5.288218,-7.206070,5.518226,-3.276375,0.924055,-3.352437,4.087311,3.976068,2.333047,-3.107968,0.224475,-3.933369,9.736325,-5.476120,8.747559,-7.229108,7.513171,-8.140653,1.096675,1.405144,-4.803538,-6.362320,6.105876,6.538962,-9.978450,9.858773,-0.997817,-5.113349,6.175856,1.698557,9.313913,-5.388152,-4.854551,2.558237,-3.833544,-2.855925,-4.990526,-1.262525,-9.338414,5.568715,5.081911,-9.124791,-2.144389,8.798220,5.965104,-9.944854,-3.956161,6.329592,8.184972,5.404986,-3.949571,-6.079943,-6.632990,-8.858001,-4.807957,5.892421,-5.900739,6.405768,-6.964141,-6.730333,-9.993259,-6.444924,-4.505606,9.005379,-8.026038,2.206553,7.565848,-8.964367,-4.500289,-4.191413,-7.642512,-5.239149,-8.242199,6.989381,-2.238506,-4.075692,-5.138421,-0.275105,3.817714,-4.226247,-3.571956,-2.008274,-8.161206,9.578539,3.426231,2.874822,0.883713,-8.589084,-0.611519,5.084738,4.527280,1.292565,-6.344944,-7.092778,9.745322,-7.033213,-4.827355,5.613207,3.271851,8.501499,9.127798,-0.122267,-6.229061,-2.221134,-7.672436,-3.417385,7.035584,8.147539,3.704959,5.582814,-9.703595,-5.132897,-4.955441,8.646660,-1.850046,-7.991746,-5.570361,-5.092263,2.312906,6.905486,-9.291369,-0.922344,5.167843,-1.880638,8.689721,8.080950,3.886143,4.387202,-9.845334,9.918675,3.827318,-7.210079,-2.571462,4.116284,8.734780,9.460627,-5.344635,5.041142,2.079230,-4.708578,-3.097966,-2.969287,0.090969,3.218968,9.317900,-1.287474,2.833252,-5.052668,4.704720,1.158425,-3.017022,9.930322,-2.000520,-7.214159,-2.369653,2.305586,-7.759659,-9.385116,8.269455,9.488743,-3.125782,3.185630,-9.373766,2.173991,4.444966], dtype = "float64")#candidate|6294|(546,)|const|float64
call_6293 = func_3623_call(relay.reshape(const_6294.astype('float64'), [13, 14, 3]))
call_6295 = func_3623_call(relay.reshape(const_6294.astype('float64'), [13, 14, 3]))
output = relay.Tuple([uop_6287,call_6293,const_6294,])
output2 = relay.Tuple([uop_6289,call_6295,const_6294,])
func_6319 = relay.Function([], output)
mod['func_6319'] = func_6319
mod = relay.transform.InferType()(mod)
mutated_mod['func_6319'] = func_6319
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6319_call = mutated_mod.get_global_var('func_6319')
call_6320 = func_6319_call()
output = call_6320
func_6321 = relay.Function([], output)
mutated_mod['func_6321'] = func_6321
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6187_call = mod.get_global_var('func_6187')
func_6188_call = mutated_mod.get_global_var('func_6188')
call_6506 = relay.TupleGetItem(func_6187_call(), 0)
call_6507 = relay.TupleGetItem(func_6188_call(), 0)
output = call_6506
output2 = call_6507
func_6522 = relay.Function([], output)
mod['func_6522'] = func_6522
mod = relay.transform.InferType()(mod)
output = func_6522()
func_6523 = relay.Function([], output)
mutated_mod['func_6523'] = func_6523
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5727_call = mod.get_global_var('func_5727')
func_5728_call = mutated_mod.get_global_var('func_5728')
call_6524 = relay.TupleGetItem(func_5727_call(), 0)
call_6525 = relay.TupleGetItem(func_5728_call(), 0)
output = relay.Tuple([call_6524,])
output2 = relay.Tuple([call_6525,])
func_6536 = relay.Function([], output)
mod['func_6536'] = func_6536
mod = relay.transform.InferType()(mod)
mutated_mod['func_6536'] = func_6536
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6536_call = mutated_mod.get_global_var('func_6536')
call_6537 = func_6536_call()
output = call_6537
func_6538 = relay.Function([], output)
mutated_mod['func_6538'] = func_6538
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5560_call = mod.get_global_var('func_5560')
func_5561_call = mutated_mod.get_global_var('func_5561')
call_6554 = relay.TupleGetItem(func_5560_call(), 0)
call_6555 = relay.TupleGetItem(func_5561_call(), 0)
func_5341_call = mod.get_global_var('func_5341')
func_5347_call = mutated_mod.get_global_var('func_5347')
var_6563 = relay.var("var_6563", dtype = "int64", shape = (390,))#candidate|6563|(390,)|var|int64
const_6564 = relay.const([[2,3,7,8],[-7,-9,-2,-2],[9,8,2,-3],[-2,6,6,2],[-5,7,4,-2],[-8,2,1,-6],[3,4,-1,2],[10,7,-7,8],[-3,-4,10,-9],[-6,2,-8,6],[4,9,-10,9],[10,-8,4,-8],[10,-5,7,3],[-9,-1,-3,8],[-8,3,9,-8],[9,-5,3,-1],[5,-7,3,8],[-5,9,-5,-7],[6,-2,1,6],[-7,2,-6,7],[10,6,4,-5],[2,-6,3,-9],[-3,-5,-1,4],[-4,2,-1,1],[-10,7,10,2]], dtype = "uint64")#candidate|6564|(25, 4)|const|uint64
var_6565 = relay.var("var_6565", dtype = "int64", shape = (11, 88))#candidate|6565|(11, 88)|var|int64
call_6562 = relay.TupleGetItem(func_5341_call(relay.reshape(var_6563.astype('int64'), [13, 2, 15]), relay.reshape(var_6563.astype('int64'), [13, 2, 15]), relay.reshape(const_6564.astype('uint64'), [100,]), relay.reshape(var_6565.astype('int64'), [968,]), ), 5)
call_6566 = relay.TupleGetItem(func_5347_call(relay.reshape(var_6563.astype('int64'), [13, 2, 15]), relay.reshape(var_6563.astype('int64'), [13, 2, 15]), relay.reshape(const_6564.astype('uint64'), [100,]), relay.reshape(var_6565.astype('int64'), [968,]), ), 5)
func_3623_call = mod.get_global_var('func_3623')
func_3625_call = mutated_mod.get_global_var('func_3625')
var_6571 = relay.var("var_6571", dtype = "float64", shape = (546,))#candidate|6571|(546,)|var|float64
call_6570 = func_3623_call(relay.reshape(var_6571.astype('float64'), [13, 14, 3]))
call_6572 = func_3623_call(relay.reshape(var_6571.astype('float64'), [13, 14, 3]))
uop_6583 = relay.tan(var_6565.astype('float32')) # shape=(11, 88)
func_755_call = mod.get_global_var('func_755')
func_758_call = mutated_mod.get_global_var('func_758')
const_6586 = relay.const(5, dtype = "uint64")#candidate|6586|()|const|uint64
call_6585 = relay.TupleGetItem(func_755_call(relay.reshape(call_6562.astype('int64'), [8, 11, 11]), relay.reshape(const_6586.astype('uint64'), []), ), 5)
call_6587 = relay.TupleGetItem(func_758_call(relay.reshape(call_6562.astype('int64'), [8, 11, 11]), relay.reshape(const_6586.astype('uint64'), []), ), 5)
uop_6590 = relay.sigmoid(uop_6583.astype('float64')) # shape=(11, 88)
output = relay.Tuple([call_6554,call_6562,var_6563,const_6564,call_6570,var_6571,call_6585,const_6586,uop_6590,])
output2 = relay.Tuple([call_6555,call_6566,var_6563,const_6564,call_6572,var_6571,call_6587,const_6586,uop_6590,])
func_6610 = relay.Function([var_6563,var_6565,var_6571,], output)
mod['func_6610'] = func_6610
mod = relay.transform.InferType()(mod)
mutated_mod['func_6610'] = func_6610
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6610_call = mutated_mod.get_global_var('func_6610')
var_6612 = relay.var("var_6612", dtype = "int64", shape = (390,))#candidate|6612|(390,)|var|int64
var_6613 = relay.var("var_6613", dtype = "int64", shape = (11, 88))#candidate|6613|(11, 88)|var|int64
var_6614 = relay.var("var_6614", dtype = "float64", shape = (546,))#candidate|6614|(546,)|var|float64
call_6611 = func_6610_call(var_6612,var_6613,var_6614,)
output = call_6611
func_6615 = relay.Function([var_6612,var_6613,var_6614,], output)
mutated_mod['func_6615'] = func_6615
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6025_call = mod.get_global_var('func_6025')
func_6026_call = mutated_mod.get_global_var('func_6026')
call_6631 = relay.TupleGetItem(func_6025_call(), 0)
call_6632 = relay.TupleGetItem(func_6026_call(), 0)
func_4693_call = mod.get_global_var('func_4693')
func_4696_call = mutated_mod.get_global_var('func_4696')
var_6643 = relay.var("var_6643", dtype = "float32", shape = (260,))#candidate|6643|(260,)|var|float32
call_6642 = relay.TupleGetItem(func_4693_call(relay.reshape(var_6643.astype('float32'), [5, 13, 4])), 0)
call_6644 = relay.TupleGetItem(func_4696_call(relay.reshape(var_6643.astype('float32'), [5, 13, 4])), 0)
func_5791_call = mod.get_global_var('func_5791')
func_5794_call = mutated_mod.get_global_var('func_5794')
const_6649 = relay.const([9.087960,-1.369045,-0.329029,5.057223,-3.537773,-5.525119,-6.608282,-4.446433,5.509684,4.146153,0.568124,1.744179,7.243161,-0.635032,-0.977427,-0.330130,-2.845397,0.182293,-9.029757,2.075492,-3.820403,9.158554,-9.981090,9.654149,1.195106,0.128965,-8.708821,-0.766130,-7.123987,-7.066738,0.403744,-7.105875,6.918437,-3.796191,-8.933539,9.091150,-3.823891,-3.838917,-4.082716,-6.857974,-0.195147,-5.421168,-5.343594,3.649323,8.125012,4.145686,-9.137651,7.399354,6.967054,3.775644,6.769590,-7.506405,9.197288,-8.368171,8.161890,0.607563], dtype = "float32")#candidate|6649|(56,)|const|float32
call_6648 = relay.TupleGetItem(func_5791_call(relay.reshape(const_6649.astype('float32'), [56,])), 0)
call_6650 = relay.TupleGetItem(func_5794_call(relay.reshape(const_6649.astype('float32'), [56,])), 0)
output = relay.Tuple([call_6631,call_6642,var_6643,call_6648,const_6649,])
output2 = relay.Tuple([call_6632,call_6644,var_6643,call_6650,const_6649,])
func_6663 = relay.Function([var_6643,], output)
mod['func_6663'] = func_6663
mod = relay.transform.InferType()(mod)
var_6664 = relay.var("var_6664", dtype = "float32", shape = (260,))#candidate|6664|(260,)|var|float32
output = func_6663(var_6664)
func_6665 = relay.Function([var_6664], output)
mutated_mod['func_6665'] = func_6665
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5560_call = mod.get_global_var('func_5560')
func_5561_call = mutated_mod.get_global_var('func_5561')
call_6676 = relay.TupleGetItem(func_5560_call(), 0)
call_6677 = relay.TupleGetItem(func_5561_call(), 0)
output = relay.Tuple([call_6676,])
output2 = relay.Tuple([call_6677,])
func_6678 = relay.Function([], output)
mod['func_6678'] = func_6678
mod = relay.transform.InferType()(mod)
mutated_mod['func_6678'] = func_6678
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6678_call = mutated_mod.get_global_var('func_6678')
call_6679 = func_6678_call()
output = call_6679
func_6680 = relay.Function([], output)
mutated_mod['func_6680'] = func_6680
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6522_call = mod.get_global_var('func_6522')
func_6523_call = mutated_mod.get_global_var('func_6523')
call_6691 = func_6522_call()
call_6692 = func_6522_call()
var_6699 = relay.var("var_6699", dtype = "float32", shape = (15, 9, 6))#candidate|6699|(15, 9, 6)|var|float32
bop_6700 = relay.less(call_6691.astype('bool'), relay.reshape(var_6699.astype('bool'), relay.shape_of(call_6691))) # shape=(15, 9, 6)
bop_6703 = relay.less(call_6692.astype('bool'), relay.reshape(var_6699.astype('bool'), relay.shape_of(call_6692))) # shape=(15, 9, 6)
const_6712 = relay.const([[[True,False,True,True,True,False],[True,True,False,False,False,False],[True,False,True,True,False,True],[False,True,True,False,False,False],[False,True,True,False,True,True],[False,False,False,False,True,True],[False,False,False,False,False,True],[False,True,True,True,True,True],[True,True,True,False,True,True]],[[False,True,False,False,True,False],[True,False,False,True,False,False],[True,False,False,True,False,True],[False,False,False,True,False,True],[True,True,False,False,True,True],[True,False,False,False,False,False],[False,True,False,False,True,False],[False,False,False,True,True,False],[False,False,False,False,True,False]],[[False,False,True,False,False,True],[False,False,True,False,False,True],[False,False,False,False,False,True],[False,True,True,False,False,True],[False,False,True,True,False,False],[True,False,True,True,True,True],[False,True,True,True,True,True],[False,False,True,False,False,False],[False,True,True,True,True,True]],[[False,False,True,True,True,True],[False,False,False,True,True,True],[False,True,False,False,False,True],[True,False,True,True,True,False],[True,True,True,False,False,False],[True,True,False,False,False,True],[True,False,False,True,True,True],[False,False,True,False,False,True],[False,True,False,True,False,True]],[[True,True,False,False,True,False],[True,False,True,True,False,False],[True,False,False,True,True,False],[False,False,False,True,False,False],[True,False,True,True,False,False],[False,True,True,False,False,True],[False,True,True,False,False,False],[False,True,False,False,False,True],[False,True,True,False,False,False]],[[False,True,False,False,False,False],[False,False,False,True,False,False],[False,True,True,False,True,True],[False,True,True,False,True,True],[True,False,False,True,False,True],[True,True,False,True,True,True],[False,True,True,False,False,False],[False,True,True,True,True,False],[False,True,True,True,True,False]],[[True,False,False,True,True,True],[False,False,False,True,False,True],[False,False,False,True,False,False],[True,False,True,False,True,False],[False,True,True,True,True,False],[False,False,True,False,True,False],[True,False,True,True,True,True],[False,True,True,False,False,True],[True,False,True,False,False,False]],[[True,True,True,False,False,False],[True,False,False,False,True,False],[False,False,False,True,False,True],[False,False,False,True,True,False],[False,False,False,True,False,True],[True,True,False,True,False,False],[True,True,True,False,True,False],[False,True,False,False,True,False],[True,True,True,True,True,False]],[[True,True,False,False,True,False],[True,False,False,True,True,False],[True,True,True,False,True,False],[False,True,True,True,True,False],[True,False,False,False,True,True],[False,False,False,False,False,True],[True,True,False,True,False,True],[True,False,False,False,False,True],[False,True,False,True,False,True]],[[False,True,True,False,False,False],[True,False,True,True,True,True],[True,False,True,True,True,True],[False,False,True,True,False,False],[False,False,True,True,True,True],[False,True,False,False,True,False],[False,False,True,True,False,False],[True,True,False,False,False,True],[True,False,True,True,True,True]],[[True,False,True,False,True,False],[True,True,False,True,True,True],[False,False,False,True,True,False],[True,False,True,True,False,True],[False,False,True,True,True,True],[False,False,True,True,False,False],[True,True,True,True,False,True],[True,False,True,True,True,False],[True,False,True,False,True,True]],[[True,True,True,False,False,False],[True,False,False,False,True,False],[False,True,True,False,False,False],[True,True,False,False,False,False],[False,True,False,True,True,False],[True,False,True,False,True,False],[True,False,False,True,True,False],[False,True,True,True,True,True],[True,False,True,False,False,True]],[[False,True,True,False,False,False],[False,True,True,False,False,False],[False,True,False,False,False,True],[False,False,True,True,False,False],[True,True,True,False,True,True],[True,True,False,False,False,True],[True,False,False,False,False,False],[False,False,True,False,True,False],[False,True,False,True,True,False]],[[True,False,False,False,False,True],[False,True,True,False,False,True],[True,True,True,False,True,False],[False,True,False,False,True,True],[False,True,True,False,False,False],[True,False,False,True,False,False],[False,False,True,True,True,True],[False,False,False,False,False,True],[False,True,False,False,True,False]],[[False,True,True,True,True,False],[True,False,False,True,True,False],[True,False,True,False,True,False],[False,False,False,False,False,True],[False,False,False,False,False,True],[False,False,False,False,True,True],[False,False,False,False,True,True],[False,False,True,True,True,True],[True,True,True,False,True,True]]], dtype = "bool")#candidate|6712|(15, 9, 6)|const|bool
bop_6713 = relay.floor_divide(bop_6700.astype('float32'), relay.reshape(const_6712.astype('float32'), relay.shape_of(bop_6700))) # shape=(15, 9, 6)
bop_6716 = relay.floor_divide(bop_6703.astype('float32'), relay.reshape(const_6712.astype('float32'), relay.shape_of(bop_6703))) # shape=(15, 9, 6)
uop_6733 = relay.exp(const_6712.astype('float64')) # shape=(15, 9, 6)
output = relay.Tuple([bop_6713,uop_6733,])
output2 = relay.Tuple([bop_6716,uop_6733,])
func_6741 = relay.Function([var_6699,], output)
mod['func_6741'] = func_6741
mod = relay.transform.InferType()(mod)
mutated_mod['func_6741'] = func_6741
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6742 = relay.var("var_6742", dtype = "float32", shape = (15, 9, 6))#candidate|6742|(15, 9, 6)|var|float32
func_6741_call = mutated_mod.get_global_var('func_6741')
call_6743 = func_6741_call(var_6742)
output = call_6743
func_6744 = relay.Function([var_6742], output)
mutated_mod['func_6744'] = func_6744
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5717_call = mod.get_global_var('func_5717')
func_5718_call = mutated_mod.get_global_var('func_5718')
call_6796 = relay.TupleGetItem(func_5717_call(), 0)
call_6797 = relay.TupleGetItem(func_5718_call(), 0)
output = call_6796
output2 = call_6797
func_6812 = relay.Function([], output)
mod['func_6812'] = func_6812
mod = relay.transform.InferType()(mod)
mutated_mod['func_6812'] = func_6812
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6812_call = mutated_mod.get_global_var('func_6812')
call_6813 = func_6812_call()
output = call_6813
func_6814 = relay.Function([], output)
mutated_mod['func_6814'] = func_6814
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6985 = relay.var("var_6985", dtype = "bool", shape = ())#candidate|6985|()|var|bool
const_6986 = relay.const([[[True,True,False,True,True,True,False,True],[True,False,True,True,True,False,False,True],[False,False,True,True,True,False,False,False],[True,False,False,False,False,True,False,True],[False,True,False,True,False,False,False,True],[True,False,False,False,False,False,True,False],[False,False,True,False,True,False,False,False]],[[False,False,False,True,True,True,False,False],[False,True,True,False,True,False,True,False],[False,True,False,False,True,True,False,True],[False,True,True,True,True,False,True,False],[False,True,True,False,False,True,False,False],[False,True,False,False,True,True,False,True],[False,True,True,True,False,True,True,False]],[[True,False,True,False,False,False,False,True],[False,True,True,False,True,True,True,True],[False,True,True,False,True,False,True,True],[True,True,True,True,False,False,False,True],[False,True,False,True,False,False,False,False],[False,True,False,True,False,True,False,False],[True,False,False,False,False,False,True,True]],[[True,False,False,True,False,False,True,True],[False,True,False,False,True,False,False,True],[True,False,False,True,False,True,True,True],[True,False,True,True,False,False,False,True],[True,False,False,True,True,True,False,True],[False,False,True,False,False,True,True,True],[True,False,False,True,True,False,False,False]]], dtype = "bool")#candidate|6986|(4, 7, 8)|const|bool
bop_6987 = relay.logical_or(var_6985.astype('bool'), const_6986.astype('bool')) # shape=(4, 7, 8)
func_1806_call = mod.get_global_var('func_1806')
func_1809_call = mutated_mod.get_global_var('func_1809')
call_6998 = relay.TupleGetItem(func_1806_call(relay.reshape(var_6985.astype('uint64'), [])), 3)
call_6999 = relay.TupleGetItem(func_1809_call(relay.reshape(var_6985.astype('uint64'), [])), 3)
func_1879_call = mod.get_global_var('func_1879')
func_1884_call = mutated_mod.get_global_var('func_1884')
var_7005 = relay.var("var_7005", dtype = "uint64", shape = (150,))#candidate|7005|(150,)|var|uint64
var_7006 = relay.var("var_7006", dtype = "bool", shape = (715,))#candidate|7006|(715,)|var|bool
call_7004 = relay.TupleGetItem(func_1879_call(relay.reshape(var_7005.astype('uint64'), [5, 5, 6]), relay.reshape(call_6998.astype('int64'), [182, 2]), relay.reshape(call_6998.astype('int64'), [4, 13, 7]), relay.reshape(var_7006.astype('bool'), [715,]), ), 3)
call_7007 = relay.TupleGetItem(func_1884_call(relay.reshape(var_7005.astype('uint64'), [5, 5, 6]), relay.reshape(call_6998.astype('int64'), [182, 2]), relay.reshape(call_6998.astype('int64'), [4, 13, 7]), relay.reshape(var_7006.astype('bool'), [715,]), ), 3)
output = relay.Tuple([bop_6987,call_6998,call_7004,var_7005,var_7006,])
output2 = relay.Tuple([bop_6987,call_6999,call_7007,var_7005,var_7006,])
func_7008 = relay.Function([var_6985,var_7005,var_7006,], output)
mod['func_7008'] = func_7008
mod = relay.transform.InferType()(mod)
mutated_mod['func_7008'] = func_7008
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7008_call = mutated_mod.get_global_var('func_7008')
var_7010 = relay.var("var_7010", dtype = "bool", shape = ())#candidate|7010|()|var|bool
var_7011 = relay.var("var_7011", dtype = "uint64", shape = (150,))#candidate|7011|(150,)|var|uint64
var_7012 = relay.var("var_7012", dtype = "bool", shape = (715,))#candidate|7012|(715,)|var|bool
call_7009 = func_7008_call(var_7010,var_7011,var_7012,)
output = call_7009
func_7013 = relay.Function([var_7010,var_7011,var_7012,], output)
mutated_mod['func_7013'] = func_7013
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6319_call = mod.get_global_var('func_6319')
func_6321_call = mutated_mod.get_global_var('func_6321')
call_7015 = relay.TupleGetItem(func_6319_call(), 2)
call_7016 = relay.TupleGetItem(func_6321_call(), 2)
func_2031_call = mod.get_global_var('func_2031')
func_2033_call = mutated_mod.get_global_var('func_2033')
const_7027 = relay.const([-8.250960,-1.999638,-1.955179,4.460328,-5.020670,-3.028622,-2.117927,8.584684,-5.695928,0.469779,2.799269,4.120606,-2.924662,8.808847,-5.627022,2.981272,-0.760337,-0.147598,-7.617279,-7.123017,-5.756286,9.244613,-4.353498,9.129595,-6.892544,-9.213923,1.926194,-2.002459,3.208964,-1.188962,-8.947808,-1.739984,9.190291,6.729843,-2.225871,-0.105811,-9.530145,7.959114,-3.656418,5.913309,-7.329668,7.913459,4.533133,8.976134,7.502288,2.782495,9.120503,-5.594009,-1.331902,-7.148940,7.622114,9.178910,-9.538262,-2.165777,-3.131395,-0.608765,3.991062,-5.272862,6.432164,3.979442,5.591469,-0.464941,-3.606227,9.813158,-9.150119,3.963670,1.902646,-8.348150,-4.885999,-1.085536,-8.305707,8.688685,-8.566579,1.142084,7.689393,-7.598442,6.230915,3.995475,1.699163,-8.917021,6.534348,8.670196,2.457362,-9.073765,-8.403435,-5.171232,0.517139,6.611523,1.322689,4.593617,9.465943,-2.892485,-5.402346,6.290887,-3.288761,-0.243943,8.632502,-7.658510,9.356653,-0.274615,-4.140043,-4.266210,-5.527847,9.864148,-0.698175,-9.496583,7.835084,-2.173217,6.457849,3.692819,-1.763037,3.091596,-2.746011,-4.393780,-7.432330,5.071078,7.133340,8.714075,2.554773,5.693930,8.199543,-7.690001,-8.582068,3.704869,-1.954910,-4.728241,-3.822809,-7.128419,3.965687,-2.503964,-5.706721,-0.493748,0.352861,3.976935,8.043856,9.421909,1.390612,9.359428,-2.023070,5.871772,0.845809,9.055583,1.193081,-2.459516,-7.649888,-0.154792,2.939297,-6.383963,-9.541821,5.067363,9.609884,4.296597,-0.554355,-7.642637,2.277015,7.930253,1.851696,-8.727126,8.733824,-8.141608,0.269475,-3.795554,3.351915,3.039288,-5.572595,2.716513,1.814145,-5.979335,8.420903,2.027165,-4.263371,-8.960285,4.487630,-2.389731,3.782300,5.936463,-4.316799,8.754609,-8.842175,3.441351,-6.455138,-4.602595,0.499957,6.587639,-9.745256,0.745637,-1.448333,-4.222738,-3.821060,-1.033369,1.321624,-7.224549,7.544548,-9.287727,3.870091,-5.761589,-5.504897,2.544230,-7.104135,7.224320,1.017931,2.167240,-8.908218,-2.718267,3.743469,-6.902451,-9.399023,-6.719397,5.474251,7.161891,-5.422473,-5.352324,0.605414,8.380585,-5.683108,-4.345400,1.645369,3.418093,4.588100,2.476707,-9.443108,-4.484311,-8.514283,-0.326718,7.775284,-7.951575,-6.786527,-3.137627,1.293198,5.735758,-9.255819,7.466602,9.824677,1.385012,-9.793872,2.329716,0.988986,4.414400,-6.328744,3.650719,-0.607018,-6.878012,-8.883034,-2.639245,-0.856200,9.378393,7.280563,-4.301461,-3.750421,6.903954,-9.374414,1.253863,-6.782330,-6.077481,4.421654,-0.868340,2.221615,-5.604119,-2.370384,2.231685,-2.240923,6.670137,-3.505544,-3.149863,-8.124499,7.550815,0.528072,-7.799952,-9.534541,-0.768443,-1.521784,5.858960,5.576993,8.590794,-6.303825,-6.109203,7.781434,-7.192415,-1.918425,-8.104760,-0.083875,4.295211,3.873384,-9.053172,-7.593209,4.106486,4.187464,3.186406,-7.369665,-9.380063,6.772361,7.103078,1.992387,-5.699169,-6.418793,-9.668494,7.314824,-1.627375,1.380537,-3.250140,-1.983404,-0.754465,-4.612441,-4.942941,-6.978884,7.354191,-1.702978,-0.530449,-2.556554,3.573876,-6.668807,0.135965,5.839364,-2.817573,-9.657464,2.392923,-0.128450,6.320649,9.678562,9.362653,-2.786485,4.691021,2.543048,-0.234049,8.023720,-0.119971,8.519798,9.275759,-2.942338,6.085758,-5.704048,3.595321,-3.764597,9.804294,-6.522818,4.102269,4.469074,5.599841,2.647094,-0.214353,2.969250,-7.955772,-9.678807,-5.094419,4.111231,-1.592825,-4.785624,-6.816036,-8.976251,-4.710494,-4.412007,2.509271,-7.767948,-0.253977,4.291918,-9.240180,5.358891,6.373213,-2.218852,-4.530288,-7.455916,9.766761,-3.872481,9.949659,2.753303,-9.715571,-4.861888,4.570860,-6.520559,-8.291741,-8.658223,6.216974,8.132197,-2.247331,-1.520028,1.404295,2.167428,0.586666,-9.383830,-2.509185,-6.354493,3.947752,-8.393253,2.145709,-2.198290,-6.667455,6.126851,-9.866267,6.812430,-8.558752,-4.696529,-1.125684,7.722676,9.482661,-7.359824,8.793766,-2.703581,8.511528,-8.200036,-1.707706,-4.263545,8.793260,-7.331218,-4.204413,-6.836553,6.774538,-0.854235,-9.984563,7.067787,7.517346,9.015008,-9.090339,2.462630,9.055933,-5.160463,-5.071584,-5.660593,-2.130384,-2.664675,-2.989793,-8.231138,4.234621,4.439719,-0.290888,5.526825,2.347493,-5.826293,3.319245,5.752739,4.331996,-1.150974,2.543008,-6.687685,4.623721,-0.699465,2.635123,8.934584,-9.915047,5.073222,6.787507,-9.589722,4.963359,-4.157189,5.552454,9.721975,9.096791,-2.095420,7.375994,7.634477,8.938377,-0.825786,-3.392852,7.544603,5.746677,2.082275,-1.596545,1.652355,-8.261218,-5.991017,1.738623,8.777215,5.060132,6.085345,-5.480476,1.177128,1.835530,-7.500703,1.676293,-6.489888,-9.679999,1.327886,3.113965,4.879488,-7.384548,8.509478,4.889845,-7.040165,1.602018,1.142996,-0.467809,1.190146,2.326081,3.326427,-7.676545,4.303907,3.566849,1.060477,7.145813,1.776030,-7.345147,0.624529,6.611840,-4.393321,-3.775176,-7.606926,-3.749639,-9.884558,5.342700,-6.074178,9.272914,8.767300,-7.405151,0.995940,9.819227,7.412312,-9.417534,5.214489,-0.443510,-3.924737,-0.749172,-6.901188,-2.666923,-7.506967,-0.154650,4.752683,-7.218747,3.184594,2.228187,-6.928977,3.788738,-5.408917,-4.576655,6.366453,8.105425,3.532642,-0.798238,-0.272425,-8.965733,-1.440831,4.531670,-5.464753,-4.539292,-9.102823,0.275701,-9.387202,-8.368831,-9.352363,3.771661,-0.398310,5.904964,-3.289154,3.633383,-1.251022,8.674314,-7.323594,5.136324,-3.887548,-0.938274,2.108993,5.367927,-6.556511,6.990691,-7.939950,-7.337683,8.637091,0.770316,2.002412,9.895027,-0.883849,4.022376,0.671734,-8.993033,-2.372942,5.707681,-1.414305,-5.983793,-0.374199,3.996279,-4.164829,7.327677,6.729970,1.306753,6.236797,-9.289624,2.684719,6.778590,-5.444507,-3.684273,-4.673048,7.189855,-2.174027,-4.913568,5.157845,7.913940,9.253449,6.369063,3.827380,-4.238360,9.985822,8.375900,-8.513807,-4.644120,-6.056470,2.272458,-2.726348,5.212896,-7.447733,1.146600,7.882537,5.951360,-1.084668,5.242561,2.831120,-8.460082,-3.436193,8.041831,-6.787959,-0.394850,-8.602907,-1.071580,-0.073684,1.017582,3.965773,-3.838901,-8.406291,1.040231,-9.890904,-2.080966,-1.689105,1.259205,-8.838652,5.693193,-5.292640,2.407104,-9.545555,5.350682,9.372486,7.335827,3.303379,9.962187,-5.908813,-8.671401,8.556672,-0.569798,-3.623189,5.302809,2.743131,9.653451,-1.230311,-8.841034,-9.257812,7.882876,7.795731,-3.951493,-3.139489,-6.980448,5.421004,9.006051,6.999899,-8.934361,3.253922,8.709967,9.843455,-8.397000,4.566183,-7.400673,-3.599288,-7.147311,-6.303582,7.010250,-2.617620,4.029311,-3.417865,9.204530,0.928848,2.153712,7.459649,3.868303,-4.839856,-6.565688,-0.680938,8.918266,-2.969396,-9.617535,9.750248,3.429374,4.945386,0.127277,9.673767,-6.875782,-4.997785,-3.454494,-7.048173,-4.184722,2.783335,-4.787957,0.676465,7.783548,7.481323,8.196073,8.844335,1.552676,9.561462,-8.176572,8.292984,3.649842,3.414140,4.031437,9.518486,-4.973532,-4.744210,1.570230,-7.568078,0.999625], dtype = "float64")#candidate|7027|(704,)|const|float64
call_7026 = relay.TupleGetItem(func_2031_call(relay.reshape(const_7027.astype('float64'), [8, 11, 8])), 0)
call_7028 = relay.TupleGetItem(func_2033_call(relay.reshape(const_7027.astype('float64'), [8, 11, 8])), 0)
func_5791_call = mod.get_global_var('func_5791')
func_5794_call = mutated_mod.get_global_var('func_5794')
var_7034 = relay.var("var_7034", dtype = "float32", shape = (56,))#candidate|7034|(56,)|var|float32
call_7033 = relay.TupleGetItem(func_5791_call(relay.reshape(var_7034.astype('float32'), [56,])), 1)
call_7035 = relay.TupleGetItem(func_5794_call(relay.reshape(var_7034.astype('float32'), [56,])), 1)
output = relay.Tuple([call_7015,call_7026,const_7027,call_7033,var_7034,])
output2 = relay.Tuple([call_7016,call_7028,const_7027,call_7035,var_7034,])
func_7044 = relay.Function([var_7034,], output)
mod['func_7044'] = func_7044
mod = relay.transform.InferType()(mod)
var_7045 = relay.var("var_7045", dtype = "float32", shape = (56,))#candidate|7045|(56,)|var|float32
output = func_7044(var_7045)
func_7046 = relay.Function([var_7045], output)
mutated_mod['func_7046'] = func_7046
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6187_call = mod.get_global_var('func_6187')
func_6188_call = mutated_mod.get_global_var('func_6188')
call_7214 = relay.TupleGetItem(func_6187_call(), 0)
call_7215 = relay.TupleGetItem(func_6188_call(), 0)
var_7216 = relay.var("var_7216", dtype = "float32", shape = (15, 9, 6))#candidate|7216|(15, 9, 6)|var|float32
bop_7217 = relay.divide(call_7214.astype('float32'), relay.reshape(var_7216.astype('float32'), relay.shape_of(call_7214))) # shape=(15, 9, 6)
bop_7220 = relay.divide(call_7215.astype('float32'), relay.reshape(var_7216.astype('float32'), relay.shape_of(call_7215))) # shape=(15, 9, 6)
func_6610_call = mod.get_global_var('func_6610')
func_6615_call = mutated_mod.get_global_var('func_6615')
var_7222 = relay.var("var_7222", dtype = "int64", shape = (5, 78))#candidate|7222|(5, 78)|var|int64
const_7223 = relay.const([-2,-8,-4,-2,8,-7,3,-7,-2,2,2,-4,8,8,-7,-9,-9,-5,5,-4,-1,8,-10,-9,-9,-10,8,8,5,-2,-10,3,-7,-4,6,-7,-1,-10,-9,7,-1,-1,-8,5,-4,8,-5,5,9,-8,9,3,2,1,2,1,5,-10,-10,8,9,2,-7,10,6,1,3,5,7,9,6,-3,-4,5,8,-2,7,5,-10,-10,-2,2,-4,3,5,-1,3,-1,6,3,-7,-5,6,10,4,2,2,-3,3,10,-7,-8,-4,7,4,8,-2,10,2,6,2,3,-4,-10,2,6,10,8,-2,8,3,-1,-8,7,-1,-7,10,6,-6,-2,6,-6,1,-2,10,-3,5,-10,-3,4,-9,-8,1,-5,-8,-5,-7,1,-8,-3,1,3,-9,9,-1,9,-4,-1,9,-5,-6,-3,5,1,7,2,-1,5,10,-6,-7,-3,10,-9,1,-7,-6,8,-4,-3,-6,-10,1,-10,9,2,-9,-10,-8,-7,5,-3,-4,-2,-3,-1,1,-7,7,3,-3,6,1,-10,-7,7,-3,-4,-3,-7,-1,-7,-10,-5,2,-4,7,7,-8,-7,6,-8,6,7,-8,8,-3,-4,-9,-1,-10,-6,-5,-5,9,-9,-7,5,-10,-5,-7,2,9,-4,-4,1,-9,1,9,-8,-9,3,-7,1,1,8,2,9,-5,-10,-9,4,-8,-4,2,-3,-1,9,5,7,-10,5,6,-3,-6,-9,4,2,10,-6,8,-5,10,-10,8,2,-2,-9,-8,9,-5,-10,4,10,-8,10,8,8,3,-2,3,10,10,6,-2,-3,-5,-8,4,5,-4,9,-2,9,-3,8,-4,5,-8,1,6,-8,8,-10,-4,4,1,10,-10,-1,-2,3,7,-10,-9,-4,-7,-3,-8,7,1,-10,5,-8,-10,2,-1,-8,10,-3,2,-3,-10,4,-1,-2,4,-5,-1,-6,5,3,-2,4,8,3,5,-1,-4,4,7,10,-7,2,1,1,7,-1,2,1,3,3,1,2,8,1,-4,-9,-7,3,9,1,7,-5,7,10,-1,7,-7,-5,7,-10,-8,-5,8,-10,-1,4,-5,6,4,-4,-1,7,2,-10,-10,3,9,-3,-6,-7,4,-5,-10,-2,9,1,9,-5,-10,1,7,-5,1,-7,-1,-4,-8,5,-9,2,5,7,1,-4,-9,8,6,-6,3,4,10,10,-6,-5,2,-5,1,10,6,-3,-8,2,-6,2,4,3,3,-1,6,8,-3,6,6,8,-9,-6,-9,2,-9,-5,10,6,-9,2,10,5,2,-7,-9,-10,-5,-7,7,10,-4,8,2,7,10,7,1,5,-5,-4,9,-3,2,-9,-1,-6,3,-1,9,-4,-7,-1,7,4,8,6,-1,2,-1,2,-7,7,2,4,-5,-2,-3,3,-7,-2,2,-4,9,6,-4,-1,9,-2,-7,-4,-7,5,7,10,4,3,-1,8,-1,-9,-5,8,10,4,-6,-10,-5,3,-2,8,-2,-1,-7,3,5,5,-4,-3,4,-4,8,-3,8,6,6,5,6,1,6,1,7,1,-2,-10,4,7,9,-4,4,8,-6,10,-10,3,-8,-7,-4,-8,5,-3,1,10,9,-6,5,-5,-8,3,7,-6,-4,-9,1,7,5,-4,9,8,-9,-1,2,-7,2,-8,10,3,7,2,-1,-6,10,-5,-6,-7,1,1,-5,-4,2,5,8,-4,1,-4,7,-1,2,6,-10,4,10,-5,-8,3,10,10,7,2,-1,2,-10,7,-10,-1,5,-4,-3,-9,7,-10,9,7,-5,-7,7,6,-4,-1,-5,7,-8,-4,-9,5,-6,-4,-7,4,10,-8,-3,-6,9,-1,10,6,-10,-10,-7,6,-9,10,-1,-8,6,-10,2,5,-3,-8,6,-10,6,7,6,7,-6,-3,-1,-10,9,-7,-5,-4,9,-1,8,1,-3,7,4,7,3,4,1,3,3,-10,-10,-1,6,6,-5,-6,-7,-10,-9,8,-6,-5,8,6,-8,2,-1,-1,-4,9,-3,-10,9,1,6,9,-4,9,-4,5,-3,4,-1,9,1,7,-4,-6,6,3,9,-3,8,-6,7,4,10,4,-2,-9,10,9,-4,8,-4,-1,5,-7,4,-3,7,-2,7,10,-8,4,-4,3,10,7,4,-7,2,10,-9,8,2,3,-6,1,-2,10,-2,6,-6,-3,3,-7,-4,-10,10,9,7,-3,4,5,-3,-2,9,4,-2,-6,-9,-9,-2,7,6,5,-5,8,-4,-5,-9,-9,-4,-6,4,-1,-6,5,9,1,-8,-1,-7,-2,2,-8,-6,-3,-2,9,4,-8,-10,10,6,9,8,-5,-8,5,-8,-5,10,5,9,-9,-3,3,1,-7,5,-9,5,-7,4,-5,5,-5,7,10,-3,9,5,3,5,2,-3,4,-4,-3,5,1,7,6,7,2,-6,-9,-4,6,10,1,9,-3,4,-3,3,10,1,6,3,-9,-10,9,-9,-5,-5,4,10,8,1,-5,-5,-4,3,6,9,-5,4,-5,1,3,6,1,-5,10,-10,10,-1,6,6,2], dtype = "int64")#candidate|7223|(968,)|const|int64
const_7224 = relay.const([[-7.699547,-5.294268,-6.741393,3.874683,-7.221485,2.198203,-9.764085,-2.503816,-3.652581,-9.103870,-7.642110,9.819664,-3.352834,-3.428548,-4.069597,-8.721783,0.690354,2.942672,-7.907077,5.425221,9.660340,9.824646,-0.875231,-2.916610,-5.800637,1.716250,0.315157,-9.613731,8.360666,-4.005771,-2.982777,5.938439,5.366105,6.485389,5.764921,1.080652,1.706467,-1.551073,-1.935628,5.788291,5.706961,-9.829580,9.525831,-0.448781,9.617192,-9.844440,-1.323417,0.493152,-8.946529,3.304598,-8.445870,-6.525977,0.740815,1.880399,8.387480,-4.206693,4.795464,2.348156,-1.704460,-4.008767,-8.931426,3.210741,-2.380717,4.618836,2.374197,-2.518193,3.649329,-8.641615,-4.724913,-1.375574,-5.726826,-4.343717,7.536132,-6.311153,-7.669048,5.954333,8.207668,7.910520,-9.448686,-9.502744,2.868791,8.075724,1.737405,4.619867,6.487154,-0.936396,-0.380909,-2.100791,-7.952960,0.834412,2.996448,-5.874982,1.285164,-1.778276,-1.851424,-6.967413,1.951334,-8.900711,9.503722,-2.044992,7.876607,-5.096803,-6.281674,-0.759000,4.706849,9.443532,-6.521280,9.999917,4.560817,6.794651,-7.797074,1.130203,0.766131,-1.894234,3.510871,-3.982493,4.372763,-2.515451,4.222364,6.197048,9.751647,7.052287,-5.686139,7.230973,-1.176764,2.776563,-3.708584,-2.857883,-3.590725,-8.796155,-9.647763,-2.960166,0.963123,1.823745,3.050710,4.580958,4.761781,4.185892,5.243826,4.651151,3.685432,-7.292927,2.501514,-9.122815,-9.408580,3.616479,2.156218,-0.907722,-1.994460,2.500123,-3.773609,-1.832111,4.585076,5.856337,4.866308,-3.804478,8.671422,-9.039727,2.773102,-8.079703,-6.304752,-0.143206,-6.684845,-3.896589,-6.047523,-3.719425,6.347244,-7.085194,-8.505562,5.531699,-1.994187,9.605188,2.477274,-5.535947,-9.385116,-9.368516,-4.908412,-3.267639,5.944602,-5.584787,-6.085565,4.782533,6.642420,-2.762544,4.375624,0.164509,0.945687,-6.953308,4.247084,5.423115,8.592116,-9.307954,0.149774,-3.437372,3.507971,-0.625714,-3.469774,3.356085,-6.161802,4.195650,-9.914614,1.535937,1.699121,-7.671293,9.397235,-8.588735,5.519593,-9.224226,0.279142,5.985116,6.859018,-6.678086,5.706071,-0.809548,7.884671,-9.549804,-6.791140,7.941332,1.069002,-3.666257,-6.653448,0.868521,1.763681,-6.186198,6.928816,-3.408960,4.904170,-6.388423,-4.602270,-1.058549,-2.159212,0.482196,0.251536,8.796622,-7.383163,8.739845,-3.864280,-4.709795,-8.782777,6.233772,9.300384,1.659878,-8.059943,3.995406,-9.608283,5.819484,-1.004806,9.362904,0.077068,-4.070416,3.369813,-6.469103,9.173651,4.705480,9.188183,3.155449,-4.061058,-6.782957,-4.019777,-0.577765,1.749116,5.814692,-6.636523,4.523654,2.144400,-1.579668,5.799342,5.697358,4.368325,1.918824,3.380314,8.220897,2.670734,-8.505992,-8.762493,-7.418434,-9.183259,2.859607,-5.502374,1.156734,9.168997,-2.868282,-7.575213,2.766064,6.649059,7.335230,2.123756,-3.124974,-7.770994,-2.511565,3.351609,-2.588192,-7.449191,0.931718,7.905167,4.780338,-3.776406,5.890454,1.730471,-6.889013,7.203217,3.558654,4.613742,3.539988,-2.351534,-6.829157,-9.297927,-7.105577,-4.410310,-3.158993,-3.581463,-1.330452,6.911881,5.881402,-9.983444,8.235959,4.163686,-9.444969,7.387077,-3.213488,2.274061,8.385997,-0.577257,3.797636,6.310014,-5.838739,1.123285,-7.747446,-1.961339,3.375703,-1.768502,7.673795,1.781433,-1.918721,2.092294,-5.530835,0.772887,0.025658,0.725159,-6.513252,-4.796357,-5.296687,-2.503811,-5.805041,8.315738,1.676107,7.009881,5.848282,4.611035,1.364789,0.138947,5.423375,0.649339,-2.408114,8.283981,-4.932369,7.562094,3.359628,8.198556,-2.328614,8.888497,-7.892897,-6.300039,1.455255,4.101062,3.865128,0.659014,2.198321,6.498440,3.924441,6.668109,-1.395538,9.473809,-8.432812,6.709565,5.759633,-0.728175,6.491076,6.916061,-3.199759,8.980946,2.930027,2.085063,-2.240501,-3.433570,0.170613,9.598165,-6.842531,-1.675945,3.939096,-4.275542,-0.634975,8.667438,3.648670,7.391498,0.427353,8.865488,3.330562,-2.354713,5.549042,0.971163,-5.468072,-6.905404,2.615046,5.222199,2.376217,8.789739,-1.837464,1.917895,-6.649300,-6.432001,-4.722299,-2.292362,-5.114097,8.661911,-8.743656,-4.507785,5.397431,7.795272,1.915493,7.095585,-6.019424,5.720424,6.454033,9.992661,6.669911,-0.151155,0.421308,0.985996,1.714211,-4.830391,4.850339,-1.562530,2.788669,-7.012185,-7.201932,8.572876,-3.941798,7.610259,-8.491155,1.749596,-3.856930,9.786061,0.999026,6.171597,7.626537,-2.133610,7.729578,3.777119,-8.718082,5.434903,7.093591,-5.089033,4.936209,-4.015808,-0.696488,0.816287,1.057789,-4.622563,0.621526,7.230440,7.651696,-3.410856,-1.773064,-6.551726,7.573467,4.725039,-5.132129,-8.457136,1.209883,6.833550,5.481922,7.493169,7.356714,2.605352,8.910813,2.791914,-5.794376,8.915715,0.125092,7.489415,-6.958190,-2.708416,-6.463110,-5.809992,4.387086,0.475853,7.577104,0.036245,1.570549,7.713703,7.710534,5.414782,-4.380863,-0.950991,-0.613494,-5.597099,-1.592722,-6.468097,-0.545142,-6.366188,-9.110991,-2.676369,-0.617837,9.198713,-6.888926,8.998774,0.147297,1.434395,0.946202,-0.836088,2.740176,-6.707655,3.187097,5.457384,-4.091687,8.847029,8.339889,-7.977750,0.727940,8.983827,-1.820262,4.898435,-1.081100,-7.623824,-4.786792,7.465234,4.334084,5.520013,-2.605895,-5.775046,-3.028488,-0.545629,8.832572,-2.688202,-8.210613,-2.691240,-9.515807,-5.297528,-0.949535,-0.238383,4.854189,2.647788,-4.269810,7.270464,0.551892]], dtype = "float64")#candidate|7224|(1, 546)|const|float64
call_7221 = relay.TupleGetItem(func_6610_call(relay.reshape(var_7222.astype('int64'), [390,]), relay.reshape(const_7223.astype('int64'), [11, 88]), relay.reshape(const_7224.astype('float64'), [546,]), ), 7)
call_7225 = relay.TupleGetItem(func_6615_call(relay.reshape(var_7222.astype('int64'), [390,]), relay.reshape(const_7223.astype('int64'), [11, 88]), relay.reshape(const_7224.astype('float64'), [546,]), ), 7)
output = relay.Tuple([bop_7217,call_7221,var_7222,const_7223,const_7224,])
output2 = relay.Tuple([bop_7220,call_7225,var_7222,const_7223,const_7224,])
func_7231 = relay.Function([var_7216,var_7222,], output)
mod['func_7231'] = func_7231
mod = relay.transform.InferType()(mod)
var_7232 = relay.var("var_7232", dtype = "float32", shape = (15, 9, 6))#candidate|7232|(15, 9, 6)|var|float32
var_7233 = relay.var("var_7233", dtype = "int64", shape = (5, 78))#candidate|7233|(5, 78)|var|int64
output = func_7231(var_7232,var_7233,)
func_7234 = relay.Function([var_7232,var_7233,], output)
mutated_mod['func_7234'] = func_7234
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6522_call = mod.get_global_var('func_6522')
func_6523_call = mutated_mod.get_global_var('func_6523')
call_7252 = func_6522_call()
call_7253 = func_6522_call()
uop_7264 = relay.acos(call_7252.astype('float64')) # shape=(15, 9, 6)
uop_7266 = relay.acos(call_7253.astype('float64')) # shape=(15, 9, 6)
func_1879_call = mod.get_global_var('func_1879')
func_1884_call = mutated_mod.get_global_var('func_1884')
var_7275 = relay.var("var_7275", dtype = "uint64", shape = (150,))#candidate|7275|(150,)|var|uint64
var_7276 = relay.var("var_7276", dtype = "int64", shape = (364,))#candidate|7276|(364,)|var|int64
var_7277 = relay.var("var_7277", dtype = "bool", shape = (715,))#candidate|7277|(715,)|var|bool
call_7274 = relay.TupleGetItem(func_1879_call(relay.reshape(var_7275.astype('uint64'), [5, 5, 6]), relay.reshape(var_7276.astype('int64'), [182, 2]), relay.reshape(var_7276.astype('int64'), [4, 13, 7]), relay.reshape(var_7277.astype('bool'), [715,]), ), 2)
call_7278 = relay.TupleGetItem(func_1884_call(relay.reshape(var_7275.astype('uint64'), [5, 5, 6]), relay.reshape(var_7276.astype('int64'), [182, 2]), relay.reshape(var_7276.astype('int64'), [4, 13, 7]), relay.reshape(var_7277.astype('bool'), [715,]), ), 2)
output = relay.Tuple([uop_7264,call_7274,var_7275,var_7276,var_7277,])
output2 = relay.Tuple([uop_7266,call_7278,var_7275,var_7276,var_7277,])
func_7302 = relay.Function([var_7275,var_7276,var_7277,], output)
mod['func_7302'] = func_7302
mod = relay.transform.InferType()(mod)
var_7303 = relay.var("var_7303", dtype = "uint64", shape = (150,))#candidate|7303|(150,)|var|uint64
var_7304 = relay.var("var_7304", dtype = "int64", shape = (364,))#candidate|7304|(364,)|var|int64
var_7305 = relay.var("var_7305", dtype = "bool", shape = (715,))#candidate|7305|(715,)|var|bool
output = func_7302(var_7303,var_7304,var_7305,)
func_7306 = relay.Function([var_7303,var_7304,var_7305,], output)
mutated_mod['func_7306'] = func_7306
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6025_call = mod.get_global_var('func_6025')
func_6026_call = mutated_mod.get_global_var('func_6026')
call_7360 = relay.TupleGetItem(func_6025_call(), 0)
call_7361 = relay.TupleGetItem(func_6026_call(), 0)
const_7370 = relay.const([[[7.750822,-7.083977,-7.314552,4.809268,-0.393316,-7.249121],[6.714920,8.535597,2.373417,7.049075,0.460129,-1.225964],[8.831844,-9.142942,0.107135,-4.478202,2.979391,6.644878],[7.825415,4.517498,5.951655,-3.037595,5.238081,9.544734],[-3.323777,-5.840325,-0.801455,2.927260,-0.358480,9.836170],[-6.029344,-1.017923,-9.504421,9.467478,-8.584990,-9.587309],[2.176087,-9.423751,-1.181772,1.354408,6.659334,-4.720494],[-1.729596,3.423534,9.034387,-9.958216,-6.744310,9.346130],[-6.216983,-7.845677,6.830845,-6.446812,7.683197,0.355580]],[[8.782996,-1.967272,2.260858,-9.703863,7.480157,-0.441707],[2.198216,-1.395180,6.178616,-8.372498,-3.930810,-9.558985],[5.140188,-0.019624,7.352924,-4.837719,-0.608043,2.715439],[3.891763,2.710476,8.905591,-5.293193,-4.460960,-5.356185],[-7.028701,-3.124069,-7.801532,9.166433,6.778728,-7.230705],[0.935825,2.513191,-8.151660,8.227802,3.573240,-4.831470],[-0.591468,3.502345,7.930839,-4.510700,-9.934095,-0.544124],[0.318221,3.057489,-2.788546,-6.211025,-0.835297,8.059482],[-2.296603,4.882286,-2.923429,1.207581,-5.683441,1.617560]],[[-1.478491,0.629282,-0.481313,0.528185,5.749653,5.754390],[7.379823,-6.173092,3.448758,-3.108538,-3.069107,2.784125],[6.825889,-7.477589,6.953946,9.733222,5.246015,8.055078],[-8.091366,-6.714169,1.761893,6.766023,5.417440,-9.347606],[-8.086545,-4.398265,-7.536270,8.313917,-3.624008,1.959940],[8.282562,-4.548748,-5.267758,8.125546,-6.669001,-9.019704],[2.840463,-1.406000,0.772344,2.698105,5.235463,9.934898],[-2.350864,5.892049,-1.249623,-1.344112,5.861712,-8.195218],[-9.775846,6.689610,1.005987,-3.409583,3.111100,8.420104]],[[-6.214180,-1.652967,7.825562,7.160419,-2.219929,-3.220517],[-5.518236,3.473992,7.766040,3.065047,6.433655,0.714002],[-0.606334,6.032125,-6.835973,6.242816,8.631164,7.180719],[9.854362,-5.562995,3.602333,-9.120825,-6.908974,-7.185565],[2.596241,1.654117,-7.983536,-3.661557,8.426947,-6.528063],[-4.238758,-5.204247,-2.061839,-4.480067,-7.648101,2.534246],[-1.731445,9.330488,3.796330,-5.758737,7.510361,7.603583],[-4.996007,7.038061,9.956562,-1.526882,7.143686,-2.568328],[-1.982220,1.191630,3.161963,-7.266013,-3.329069,-4.365379]],[[6.046642,-7.665077,0.275029,-0.015973,5.926807,3.587216],[-0.686550,6.045077,-5.162294,1.852838,-7.597853,8.224206],[0.170083,2.909079,-7.795462,-7.454038,2.434949,-8.511063],[-9.098634,-1.394826,-2.363268,1.601192,4.521021,-6.629884],[-6.785954,-4.905343,-6.153289,-3.690334,-5.781626,6.101896],[-7.378626,-8.923104,0.114324,-0.466327,-5.136926,8.223670],[-7.002684,0.295982,6.647614,8.057113,1.214076,0.419719],[7.438694,6.039085,6.683402,-0.238539,-4.693958,2.060400],[-7.535857,-7.194831,5.585140,4.607870,-9.745957,9.707858]],[[2.345678,4.572351,1.609294,-2.620458,-0.531373,-3.569846],[6.861170,6.011995,4.131417,4.688796,-8.857318,-1.590985],[6.922037,9.673207,-4.536893,-7.119117,1.074975,-5.777820],[-8.774892,-9.108884,1.249497,-2.006235,8.587778,-8.849878],[7.633999,-9.703787,4.027843,3.224567,4.332283,-2.879160],[2.129497,4.792594,-1.463896,5.622294,-4.288245,-7.891080],[-7.699079,-3.195499,-1.625859,7.453739,-2.558497,-2.368476],[-2.795001,9.571976,-5.596894,-2.654701,-6.810113,8.052142],[5.798532,5.404077,-2.830875,2.936867,-8.190508,-2.185339]],[[2.865213,-7.619494,-3.879451,0.717261,-0.402493,-1.383474],[9.865763,8.829011,-8.046864,-1.466834,4.068899,3.438461],[7.132136,7.376733,6.279174,4.734750,3.734457,-2.661299],[-3.268313,-9.512990,-1.625221,9.499854,7.504840,9.741526],[8.300070,-5.041529,5.419713,-6.422491,-9.991611,9.984889],[-7.016940,-0.734129,-6.964474,0.828550,7.225916,-5.576536],[-8.615789,4.694025,-2.818913,4.863212,-3.861167,-6.024747],[4.499375,1.627214,-2.539497,0.812791,5.221855,-5.268906],[3.765928,-6.824273,-0.515807,-6.512352,-1.811436,-9.454229]],[[6.101723,8.613091,7.887722,6.518873,-3.512868,8.766000],[8.460302,3.437764,-7.007958,0.272074,3.669172,-5.826138],[-1.387601,-3.262868,-9.572132,0.298601,-8.168492,-2.571314],[-1.772522,7.071327,-3.139143,-3.489543,9.852074,-2.675914],[5.422427,2.314490,0.088946,-1.419631,0.738668,-9.144836],[-5.839124,6.067323,-0.791913,-2.996907,0.324575,-1.237802],[-9.070805,-6.599975,-7.209444,-4.713392,-5.743469,1.748345],[6.623191,3.192979,-3.316025,6.806391,7.361593,-6.284164],[-9.799595,-8.735284,-1.526526,5.044570,9.190705,-5.597728]],[[-8.059119,-1.289024,7.626889,-8.130013,8.913203,1.609507],[7.427135,-3.930587,4.089760,3.842233,-8.607334,7.406184],[-3.005872,6.799125,-6.806368,8.213025,-8.047670,1.727918],[4.052014,1.150839,5.696351,5.289046,5.654374,3.675675],[-9.641889,-9.202246,6.643278,2.687832,-4.548054,0.975499],[-3.070644,7.135952,-7.337135,-4.909834,-9.232471,8.843286],[-9.241095,-1.913031,-3.084531,-2.154260,-9.740466,9.316960],[7.863331,8.910319,-2.284270,-7.638565,-5.922415,3.984850],[8.899762,-8.769223,4.790353,4.767453,-6.039520,5.396533]],[[-5.063907,8.626441,-1.133752,-2.558991,7.546311,9.594053],[-9.215560,4.080058,0.339415,-7.921487,-4.251652,-2.742746],[-8.443934,-9.482917,-0.530032,7.267942,1.000242,9.572423],[-8.808141,2.735630,-5.195807,3.172048,3.144382,7.546977],[9.628354,6.205575,-7.434768,-9.500022,3.106812,-2.256074],[-7.626995,-2.213524,-6.961008,-6.066969,4.801950,5.072155],[-5.458184,0.451712,4.298534,4.653482,-8.319195,-1.798737],[-3.438893,6.556953,9.774347,0.793677,8.862875,-8.819045],[-6.706380,-8.146843,-0.110202,7.301433,-2.190973,-9.351622]],[[7.805747,3.529248,-1.396892,-9.663101,-5.530900,4.861986],[6.901747,7.578584,-0.847512,5.782589,-7.355428,2.646786],[5.346058,-0.784404,6.783094,7.884458,-1.553168,-3.300832],[-5.669097,5.988138,-1.984767,3.840230,-1.055269,-3.835121],[-1.798029,6.009126,-1.313833,5.527126,8.501475,3.717931],[3.575789,0.272604,3.906177,-5.206131,-9.241116,-8.144156],[-4.692714,1.476045,5.582742,-7.149333,8.214344,-5.025017],[-4.242382,8.778788,1.274275,-2.873975,7.796185,-3.076963],[8.801015,-9.094222,8.899508,-2.634372,-1.782408,-9.824945]],[[1.012685,4.719684,-0.751328,-7.753922,-0.383854,-6.116583],[8.919537,-5.625063,-6.134645,4.896325,5.012505,1.149028],[4.459064,1.412981,8.244834,0.091372,-2.585019,7.831837],[-4.944933,1.217601,0.238117,4.015717,-2.127122,9.133554],[-8.489266,-9.073152,8.081216,-3.747827,9.897059,-2.943693],[3.404765,3.484560,8.651038,-0.293210,0.337770,-4.820286],[6.546936,5.563247,8.120866,-9.991645,5.462228,8.883681],[4.624344,2.387317,4.868479,5.660441,0.575451,-6.221340],[-9.004058,8.235956,-8.016305,-1.802748,3.107493,3.031990]],[[8.499040,-9.698871,-9.691131,6.836542,-7.731028,-3.808273],[-2.909674,-7.719669,2.929508,-9.535748,-7.651957,1.661948],[5.990755,-1.222555,9.988880,9.007121,-1.201485,6.871712],[-5.023150,-9.701454,-6.898423,-6.236843,-5.551466,-9.481509],[-2.320986,5.884803,-0.439724,2.342784,3.839368,-9.277393],[-0.395803,4.585582,-8.913028,6.963156,4.822008,4.280535],[8.550744,-1.904413,-4.683302,8.809551,-9.764849,0.055423],[2.477447,-7.983594,1.691734,8.846129,2.554412,-3.842676],[4.179894,-1.755402,5.270842,-5.632123,3.411578,-7.197384]],[[-5.763844,-1.121169,2.623307,7.935082,0.321665,1.837824],[5.619333,-1.414983,2.127038,-3.634629,-6.709692,6.879344],[-0.945856,-6.659599,-3.941421,2.287645,-8.037668,3.903684],[-1.865405,-6.839583,4.602037,-3.720126,-7.360246,2.198236],[5.348917,2.875041,-2.405223,7.021343,-8.396216,-7.439539],[-3.664243,9.754626,-1.554198,-1.639223,-7.119059,-3.551298],[-3.839907,-5.223804,1.403787,-2.881050,2.466710,-2.288402],[-2.050877,-4.647270,-9.244158,-1.564912,-3.620676,7.561809],[-6.407799,4.441713,7.028964,-7.174188,-6.925262,-6.631987]],[[-4.610664,-1.138775,-1.566505,7.017327,-6.764604,-7.671847],[0.010962,-8.596743,-7.136687,-2.383328,2.089456,3.681320],[7.430394,0.764976,-7.584440,8.712389,-7.545955,-5.154703],[-0.198513,-8.425514,4.444077,1.152140,7.245135,6.693996],[-0.335392,-8.236358,8.553709,-9.048488,-8.558679,2.321543],[9.884720,0.977144,-8.196402,3.910843,-1.301747,-9.004777],[-8.145209,-4.462728,6.896347,7.273330,3.866710,4.920984],[-6.891798,7.255813,9.135585,6.011576,6.710109,8.680444],[7.348554,-2.460925,-2.673154,0.016075,3.706322,-7.983143]]], dtype = "float32")#candidate|7370|(15, 9, 6)|const|float32
bop_7371 = relay.greater_equal(call_7360.astype('bool'), relay.reshape(const_7370.astype('bool'), relay.shape_of(call_7360))) # shape=(15, 9, 6)
bop_7374 = relay.greater_equal(call_7361.astype('bool'), relay.reshape(const_7370.astype('bool'), relay.shape_of(call_7361))) # shape=(15, 9, 6)
output = relay.Tuple([bop_7371,])
output2 = relay.Tuple([bop_7374,])
func_7376 = relay.Function([], output)
mod['func_7376'] = func_7376
mod = relay.transform.InferType()(mod)
mutated_mod['func_7376'] = func_7376
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7376_call = mutated_mod.get_global_var('func_7376')
call_7377 = func_7376_call()
output = call_7377
func_7378 = relay.Function([], output)
mutated_mod['func_7378'] = func_7378
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5674_call = mod.get_global_var('func_5674')
func_5676_call = mutated_mod.get_global_var('func_5676')
call_7431 = func_5674_call()
call_7432 = func_5674_call()
output = relay.Tuple([call_7431,])
output2 = relay.Tuple([call_7432,])
func_7447 = relay.Function([], output)
mod['func_7447'] = func_7447
mod = relay.transform.InferType()(mod)
output = func_7447()
func_7448 = relay.Function([], output)
mutated_mod['func_7448'] = func_7448
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7449 = relay.var("var_7449", dtype = "int32", shape = (11, 6, 8))#candidate|7449|(11, 6, 8)|var|int32
const_7450 = relay.const([[[1,-5,-6,2,-8,6,5,8],[10,7,-5,3,-5,-1,9,8],[5,-4,6,6,3,4,3,9],[3,-7,10,6,8,-2,-7,6],[4,4,6,-3,-9,6,-6,7],[-4,6,6,-9,1,3,2,9]],[[-1,-5,2,-7,-5,-5,9,-2],[6,-7,4,-9,9,-3,3,-6],[-7,-1,-1,10,-1,-10,-6,-5],[2,9,10,-1,9,-10,9,7],[9,3,-6,7,-9,-8,-1,9],[7,-9,5,-7,-7,-9,3,10]],[[-3,1,7,7,-8,3,9,3],[2,-2,4,-3,6,-5,7,-10],[-10,10,-10,-5,1,8,-2,6],[4,10,9,1,5,-4,-3,5],[-5,3,1,6,6,1,-8,1],[-7,2,-4,9,10,4,-8,-7]],[[3,10,9,-5,3,-4,-5,3],[-6,5,-1,-9,-10,4,-1,10],[-2,7,6,6,-8,-10,-5,-4],[-1,1,7,-1,-3,4,-6,8],[-5,-9,7,-2,-8,-9,-7,-6],[-5,-8,-4,-9,6,1,-8,-3]],[[-3,7,10,8,-4,-2,1,-9],[4,-7,8,5,9,-9,-6,1],[-5,-3,10,4,6,2,6,2],[-1,-6,6,5,1,4,6,-9],[6,5,-1,9,-7,-7,-2,-2],[-9,-4,-2,-2,-4,-10,-4,3]],[[-9,5,9,9,4,-10,-4,-1],[-1,-10,5,7,6,10,-6,-9],[1,-7,9,8,-2,2,-1,1],[-10,-8,-10,-2,4,-8,7,9],[5,-10,-4,10,9,3,6,3],[-4,-1,-7,5,-7,2,-2,1]],[[7,-2,2,-8,-3,-10,-5,-7],[3,5,2,-1,-3,-2,6,-10],[9,-5,-5,1,-1,9,3,7],[3,-7,-2,-4,3,-7,3,1],[3,-2,-6,6,-3,5,2,-3],[-6,2,1,2,-3,-3,10,8]],[[-10,2,3,-7,-3,-2,6,10],[8,-9,-7,4,-2,8,-1,-3],[-9,10,3,8,-2,2,10,2],[-3,6,4,2,7,5,-8,-2],[5,1,-1,-5,1,-3,-7,-8],[5,-4,6,-4,8,2,2,-5]],[[7,-5,6,1,5,-10,-6,7],[-4,2,-7,-4,10,2,-1,-6],[-4,-7,3,10,10,2,-8,-9],[10,-4,-10,1,-6,1,-2,6],[-10,-8,8,10,-8,4,-3,-10],[-6,9,5,-7,5,-6,5,-4]],[[-4,-9,-2,10,3,-8,9,-7],[-4,-3,10,-10,8,-3,8,1],[2,6,-8,6,2,-6,-1,8],[-3,6,10,8,2,2,-3,-3],[2,-10,8,10,7,-5,-2,8],[5,-7,-8,5,-10,-1,2,9]],[[5,-2,3,-5,1,3,-2,-7],[2,1,2,-3,5,-5,-8,-10],[-4,-6,-6,9,10,1,10,-8],[-5,-6,7,1,-3,-8,3,-4],[10,-3,-2,8,-4,-5,-8,-9],[-3,1,-4,1,-1,10,7,-10]]], dtype = "int32")#candidate|7450|(11, 6, 8)|const|int32
bop_7451 = relay.add(var_7449.astype('int32'), relay.reshape(const_7450.astype('int32'), relay.shape_of(var_7449))) # shape=(11, 6, 8)
output = bop_7451
output2 = bop_7451
func_7456 = relay.Function([var_7449,], output)
mod['func_7456'] = func_7456
mod = relay.transform.InferType()(mod)
var_7457 = relay.var("var_7457", dtype = "int32", shape = (11, 6, 8))#candidate|7457|(11, 6, 8)|var|int32
output = func_7456(var_7457)
func_7458 = relay.Function([var_7457], output)
mutated_mod['func_7458'] = func_7458
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6678_call = mod.get_global_var('func_6678')
func_6680_call = mutated_mod.get_global_var('func_6680')
call_7483 = relay.TupleGetItem(func_6678_call(), 0)
call_7484 = relay.TupleGetItem(func_6680_call(), 0)
uop_7496 = relay.log2(call_7483.astype('float32')) # shape=(15, 9, 6)
uop_7498 = relay.log2(call_7484.astype('float32')) # shape=(15, 9, 6)
func_3802_call = mod.get_global_var('func_3802')
func_3804_call = mutated_mod.get_global_var('func_3804')
var_7505 = relay.var("var_7505", dtype = "float64", shape = (480, 1))#candidate|7505|(480, 1)|var|float64
call_7504 = func_3802_call(relay.reshape(var_7505.astype('float64'), [12, 4, 10]))
call_7506 = func_3802_call(relay.reshape(var_7505.astype('float64'), [12, 4, 10]))
func_5560_call = mod.get_global_var('func_5560')
func_5561_call = mutated_mod.get_global_var('func_5561')
call_7507 = relay.TupleGetItem(func_5560_call(), 0)
call_7508 = relay.TupleGetItem(func_5561_call(), 0)
output = relay.Tuple([uop_7496,call_7504,var_7505,call_7507,])
output2 = relay.Tuple([uop_7498,call_7506,var_7505,call_7508,])
func_7515 = relay.Function([var_7505,], output)
mod['func_7515'] = func_7515
mod = relay.transform.InferType()(mod)
mutated_mod['func_7515'] = func_7515
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7516 = relay.var("var_7516", dtype = "float64", shape = (480, 1))#candidate|7516|(480, 1)|var|float64
func_7515_call = mutated_mod.get_global_var('func_7515')
call_7517 = func_7515_call(var_7516)
output = call_7517
func_7518 = relay.Function([var_7516], output)
mutated_mod['func_7518'] = func_7518
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7536 = relay.var("var_7536", dtype = "float64", shape = (9, 3, 5))#candidate|7536|(9, 3, 5)|var|float64
uop_7537 = relay.cos(var_7536.astype('float64')) # shape=(9, 3, 5)
func_308_call = mod.get_global_var('func_308')
func_311_call = mutated_mod.get_global_var('func_311')
var_7540 = relay.var("var_7540", dtype = "uint64", shape = ())#candidate|7540|()|var|uint64
call_7539 = relay.TupleGetItem(func_308_call(relay.reshape(var_7540.astype('uint64'), [])), 0)
call_7541 = relay.TupleGetItem(func_311_call(relay.reshape(var_7540.astype('uint64'), [])), 0)
output = relay.Tuple([uop_7537,call_7539,var_7540,])
output2 = relay.Tuple([uop_7537,call_7541,var_7540,])
func_7549 = relay.Function([var_7536,var_7540,], output)
mod['func_7549'] = func_7549
mod = relay.transform.InferType()(mod)
mutated_mod['func_7549'] = func_7549
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7549_call = mutated_mod.get_global_var('func_7549')
var_7551 = relay.var("var_7551", dtype = "float64", shape = (9, 3, 5))#candidate|7551|(9, 3, 5)|var|float64
var_7552 = relay.var("var_7552", dtype = "uint64", shape = ())#candidate|7552|()|var|uint64
call_7550 = func_7549_call(var_7551,var_7552,)
output = call_7550
func_7553 = relay.Function([var_7551,var_7552,], output)
mutated_mod['func_7553'] = func_7553
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6319_call = mod.get_global_var('func_6319')
func_6321_call = mutated_mod.get_global_var('func_6321')
call_7560 = relay.TupleGetItem(func_6319_call(), 0)
call_7561 = relay.TupleGetItem(func_6321_call(), 0)
func_5717_call = mod.get_global_var('func_5717')
func_5718_call = mutated_mod.get_global_var('func_5718')
call_7589 = relay.TupleGetItem(func_5717_call(), 0)
call_7590 = relay.TupleGetItem(func_5718_call(), 0)
func_2722_call = mod.get_global_var('func_2722')
func_2726_call = mutated_mod.get_global_var('func_2726')
const_7596 = relay.const([[-2.069010,2.499948,4.165901,0.604689,-7.434837,-8.533435,-2.879605,-8.955036,3.832677,-0.481790,3.460105,8.157223,2.126002,0.288661,-1.589005,3.260475,5.640160,5.515138,-8.258023,4.642803],[5.222663,8.400315,8.280978,-4.030841,-0.742492,-5.704129,7.951043,-7.732494,-6.580202,2.592871,7.986954,8.975009,2.509935,6.445697,1.397432,2.110941,7.093593,0.652341,-0.021374,9.375805],[-9.912465,-4.052241,-3.575165,-4.506432,1.197482,1.408817,-4.844706,7.307378,0.034198,9.511672,-3.560781,4.193031,0.127420,-9.701097,2.441173,-4.034827,9.435113,9.831799,9.992408,-8.601543],[8.042587,7.903770,3.816314,-5.933520,-1.937324,0.800661,-0.885815,-5.161788,8.309614,6.792270,-2.374706,-0.288237,-3.519772,7.928061,9.071360,-5.844142,-1.482495,-5.895007,2.903739,-0.845842],[-9.974905,-9.682154,2.550458,-9.753833,2.274006,7.521876,1.405742,6.213860,9.780132,-9.126555,-5.033541,-0.096296,-5.943508,-9.595554,0.033177,5.496670,9.897060,-4.974216,-7.866759,6.678717],[-7.894553,-0.984057,8.083272,0.016263,-6.096786,4.606231,7.368355,8.003277,4.230766,8.154653,0.990706,-5.575274,-7.493684,1.851322,-2.114179,-7.902457,0.260450,-2.767362,-2.974566,5.440322]], dtype = "float64")#candidate|7596|(6, 20)|const|float64
const_7597 = relay.const(-1, dtype = "uint16")#candidate|7597|()|const|uint16
call_7595 = relay.TupleGetItem(func_2722_call(relay.reshape(const_7596.astype('float64'), [5, 2, 12]), relay.reshape(const_7597.astype('uint16'), []), ), 0)
call_7598 = relay.TupleGetItem(func_2726_call(relay.reshape(const_7596.astype('float64'), [5, 2, 12]), relay.reshape(const_7597.astype('uint16'), []), ), 0)
func_7302_call = mod.get_global_var('func_7302')
func_7306_call = mutated_mod.get_global_var('func_7306')
const_7610 = relay.const([[2,-9,-4,-3,2,7,2,-5,2,4,-8,-5,-6,-8,-4,-7,-10,-1,-7,-7,10,9,5,8,4,1,9,-4,-2,-7,-3,-7,1,9,4,9,3,-6,1,-6,-8,-9,-4,-3,5,5,2,-5,9,1,2,-7,-7,3,-9,-3,7,3,4,10,-5,9,6,-10,-8,8,10,-4,10,-3,8,5,9,-9,-5,-4,5,-8,7,-7,9,-4,-3,-6,-8,4,-8,-3,7,1,2,-2,9,9,-10,-9,-4,-9,-1,-1,-5,-5,4,-9,-4,4,-6,-3,8,8,-10,10,10,-2,4,2,-8,2,6,2,-2,6,-5,-10,2,-3,-7,-6,-4,-1,-10,10,9,10,3,-5,-10,-10,1,8,-10,-6,5,7,10,8,9,10,1,-5]], dtype = "uint64")#candidate|7610|(1, 150)|const|uint64
const_7611 = relay.const([7,3,-8,9,-10,8,7,7,3,-2,-9,-2,-8,10,5,-6,-7,-2,-3,-1,-2,-10,4,-3,-7,9,-5,-5,-4,-8,8,-3,-3,10,-8,1,-9,8,-8,-2,7,1,4,7,-10,-7,9,3,-5,-9,3,-2,3,-8,5,6,-1,6,-4,1,9,4,10,-1,-10,9,-2,-6,2,-6,3,-1,-10,8,-1,9,1,-8,-1,-5,1,4,6,8,5,-5,9,-3,-2,-2,3,10,5,4,-9,6,-4,3,4,8,-7,-8,-8,5,3,2,1,10,4,-3,-5,-10,1,9,-5,5,-9,-8,5,8,3,3,-5,-1,9,9,2,4,-5,9,1,3,8,-10,7,2,-9,-5,10,-1,-7,-4,2,-4,-5,8,-8,8,4,-10,6,-4,-7,-7,-4,-7,-1,-2,2,-9,-9,-3,-9,5,-10,6,-5,3,7,10,-10,-2,1,-3,10,-10,-10,7,5,-3,-7,3,9,-5,-7,10,5,8,8,6,7,8,-10,-9,7,2,-2,7,2,-8,10,-6,-9,-8,8,-4,2,2,-7,7,-4,-9,5,-8,1,-7,5,5,-8,3,-6,10,-1,10,-5,3,5,8,9,10,-3,10,-10,3,7,-5,3,3,-2,-1,7,8,7,3,-1,5,-9,1,-1,9,-10,-2,-2,8,-5,10,-4,-5,4,6,-2,9,-9,3,3,-7,8,6,4,3,5,-1,-4,10,6,-5,-9,2,-5,8,-8,-2,4,-8,4,-8,-7,-5,-7,10,1,2,8,-7,-8,2,10,2,-2,2,4,-2,-9,3,-2,-9,-6,2,-6,8,4,10,4,7,6,9,-9,10,-7,-6,-4,1,-6,8,10,6,8,7,1,5,3,-7,4,-2,8,10,-3,-6,2,10,1,-7,5,-10,-7,-4,-10,5,-6,-7,-5,8,7,-6,7,-2,-6,-7,4,7,-4,-4,-2,10], dtype = "int64")#candidate|7611|(364,)|const|int64
const_7612 = relay.const([[False,False,True,False,True,True,True,False,False,False,False,True,True,True,True,False,True,True,True,True,True,False,False,False,True,True,True,False,True,True,True,False,True,False,False,False,False,False,True,False,False,True,True,True,False,False,True,True,False,False,False,True,True,False,True],[False,True,False,False,True,True,False,True,True,False,True,True,False,True,False,False,True,True,True,False,False,False,False,True,False,False,False,True,True,False,False,False,False,False,False,True,False,False,False,True,True,True,False,True,True,True,False,False,False,True,True,False,True,True,False],[True,True,False,False,True,False,False,True,False,True,True,True,True,False,True,False,True,True,False,False,False,True,False,False,False,False,True,False,True,False,False,True,False,False,True,True,True,False,False,True,True,True,True,False,True,False,False,False,True,False,True,True,False,True,False],[False,True,True,False,True,False,True,False,False,True,True,True,False,True,True,False,False,False,True,False,False,True,False,False,True,True,True,False,True,True,False,True,False,False,True,True,False,False,True,False,False,True,True,False,False,False,False,True,False,True,True,False,True,False,True],[False,True,False,False,False,True,True,True,False,True,False,True,True,True,True,True,True,False,False,True,False,False,False,True,False,True,True,True,False,True,False,False,False,False,True,False,False,False,True,False,True,True,True,False,False,False,True,True,False,True,True,True,True,True,False],[True,False,True,False,True,False,False,True,False,True,False,False,True,False,True,True,True,True,False,True,True,True,False,True,True,True,False,False,False,True,True,False,True,False,False,False,True,True,False,True,False,False,False,True,True,True,False,False,False,False,False,False,True,False,True],[True,False,True,True,False,False,False,False,True,True,True,False,False,False,False,True,False,False,True,True,True,True,True,False,True,True,False,True,True,False,False,False,False,True,True,True,True,False,True,True,True,False,True,True,False,True,False,False,True,False,True,True,True,False,True],[False,False,True,False,True,True,False,True,False,False,False,True,True,False,False,False,True,True,True,False,True,False,True,False,False,True,True,True,False,False,False,False,False,True,False,True,False,True,False,False,True,False,True,False,True,False,True,False,True,False,True,False,True,False,False],[True,True,False,False,True,False,False,True,False,True,False,True,True,True,True,False,False,True,True,False,False,True,True,True,False,False,False,True,True,False,True,False,True,True,False,False,True,False,True,True,True,True,False,False,False,True,False,False,True,False,True,True,True,False,False],[False,False,False,True,True,False,False,True,True,False,True,True,True,True,True,True,False,False,True,True,True,True,True,True,False,True,False,True,True,True,False,True,True,False,False,True,True,False,False,False,False,False,False,False,True,True,True,False,True,False,True,False,True,False,False],[True,False,False,True,True,True,True,False,True,True,False,False,False,False,False,True,True,False,True,True,False,False,False,False,True,False,True,False,False,True,False,True,True,False,False,False,False,True,False,True,True,False,True,True,True,True,False,False,False,True,True,False,True,True,False],[True,True,True,True,True,False,True,True,False,True,True,False,True,True,True,False,False,True,True,True,False,True,False,False,True,True,True,True,True,False,True,False,False,False,True,True,False,False,False,False,True,False,True,True,True,False,True,True,True,True,False,False,False,False,False],[True,False,False,False,True,False,True,True,False,True,False,False,True,False,False,False,True,False,True,False,True,True,False,False,False,True,True,False,True,True,True,False,True,True,False,False,True,True,True,False,False,True,False,True,True,False,True,True,True,False,True,False,True,True,True]], dtype = "bool")#candidate|7612|(13, 55)|const|bool
call_7609 = relay.TupleGetItem(func_7302_call(relay.reshape(const_7610.astype('uint64'), [150,]), relay.reshape(const_7611.astype('int64'), [364,]), relay.reshape(const_7612.astype('bool'), [715,]), ), 4)
call_7613 = relay.TupleGetItem(func_7306_call(relay.reshape(const_7610.astype('uint64'), [150,]), relay.reshape(const_7611.astype('int64'), [364,]), relay.reshape(const_7612.astype('bool'), [715,]), ), 4)
uop_7620 = relay.asinh(const_7612.astype('float64')) # shape=(13, 55)
uop_7630 = relay.sqrt(uop_7620.astype('float64')) # shape=(13, 55)
bop_7632 = relay.less(uop_7630.astype('bool'), relay.reshape(const_7612.astype('bool'), relay.shape_of(uop_7630))) # shape=(13, 55)
output = relay.Tuple([call_7560,call_7589,call_7595,const_7596,const_7597,call_7609,const_7610,const_7611,bop_7632,])
output2 = relay.Tuple([call_7561,call_7590,call_7598,const_7596,const_7597,call_7613,const_7610,const_7611,bop_7632,])
func_7639 = relay.Function([], output)
mod['func_7639'] = func_7639
mod = relay.transform.InferType()(mod)
mutated_mod['func_7639'] = func_7639
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7639_call = mutated_mod.get_global_var('func_7639')
call_7640 = func_7639_call()
output = call_7640
func_7641 = relay.Function([], output)
mutated_mod['func_7641'] = func_7641
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6522_call = mod.get_global_var('func_6522')
func_6523_call = mutated_mod.get_global_var('func_6523')
call_7662 = func_6522_call()
call_7663 = func_6522_call()
func_3802_call = mod.get_global_var('func_3802')
func_3804_call = mutated_mod.get_global_var('func_3804')
var_7668 = relay.var("var_7668", dtype = "float64", shape = (480,))#candidate|7668|(480,)|var|float64
call_7667 = func_3802_call(relay.reshape(var_7668.astype('float64'), [12, 4, 10]))
call_7669 = func_3802_call(relay.reshape(var_7668.astype('float64'), [12, 4, 10]))
uop_7688 = relay.log10(call_7662.astype('float64')) # shape=(15, 9, 6)
uop_7690 = relay.log10(call_7663.astype('float64')) # shape=(15, 9, 6)
func_1879_call = mod.get_global_var('func_1879')
func_1884_call = mutated_mod.get_global_var('func_1884')
const_7696 = relay.const([-6,-4,6,9,-1,-5,2,10,7,-4,2,5,7,8,-2,4,9,-7,1,-9,6,-9,-6,-10,4,7,-9,-5,10,-8,4,10,-1,-10,-3,-7,5,-9,6,3,-5,-6,-5,-3,-4,-7,3,4,2,-6,-5,6,-6,10,-4,2,3,6,-8,-5,9,3,-9,4,2,-8,3,-6,7,-1,-7,2,10,10,-4,10,-6,5,-3,9,-1,2,-1,2,-2,-10,-7,-1,-8,-5,-7,-8,-10,-10,-4,-8,-8,-6,9,-6,3,2,-8,-7,5,1,-6,8,-3,-1,-9,-1,-1,5,-7,3,-7,-1,9,1,9,9,-4,3,5,-6,5,1,-8,-10,-7,6,9,9,5,-5,6,10,-8,9,7,8,-5,-1,-7,-8,3,10,-1,-1], dtype = "uint64")#candidate|7696|(150,)|const|uint64
const_7697 = relay.const([-1,-7,10,3,1,-5,3,-9,-10,5,-3,-4,-2,4,-3,9,-5,-2,4,-2,-7,-3,6,-7,10,-8,2,-6,7,8,-4,-4,3,-3,3,-1,4,-1,8,9,-1,1,-9,8,6,5,-2,10,-7,4,10,-10,-1,-7,10,5,4,-5,-4,10,8,1,-6,-7,5,1,-9,2,-2,7,8,3,1,-7,-10,2,-2,-10,-5,9,2,-5,-3,-1,9,-6,1,9,7,6,2,-7,-2,-3,8,4,6,-1,8,3,-9,4,-10,1,-10,-7,4,9,3,-2,5,-2,-5,9,4,-3,-3,-2,-2,4,-1,-4,-7,2,4,2,8,-10,5,-8,-1,2,8,1,-9,1,6,-5,-10,-4,9,-6,9,3,5,-5,-2,2,-10,-9,-10,1,6,10,2,-10,9,1,-2,-4,-6,5,5,-10,-2,6,-9,-7,-2,1,-2,-9,9,-9,-6,9,-1,10,2,10,8,8,-2,2,-4,2,-6,-5,2,-5,8,-10,8,2,9,6,8,3,-8,8,8,6,-2,8,-8,4,-6,-4,4,6,9,-1,5,9,-8,7,-8,9,-5,-7,9,8,4,2,9,-1,2,-5,7,2,4,3,-2,3,-9,-2,-2,6,4,5,-5,-2,-10,4,3,-3,7,1,8,7,-6,8,9,5,-1,9,-9,-3,-9,6,-4,1,7,-1,7,6,6,3,-7,3,9,6,-4,-6,-7,-7,3,4,-1,9,-4,-3,-9,10,-5,6,4,1,-2,-10,-9,-3,6,-4,-4,-5,6,-3,-4,-2,5,-2,-9,-8,8,-1,-7,-9,4,10,-6,10,-2,-6,-5,5,6,10,8,8,10,-5,6,1,-7,9,5,5,2,4,-2,9,6,-3,1,-10,-3,-9,-9,8,-3,-1,-10,-8,10,2,-10,-9,-2,1,-4,-4,8,-5,-6,-4,3,7,-4,6,6,-7,8,-3], dtype = "int64")#candidate|7697|(364,)|const|int64
const_7698 = relay.const([[True,False,True,False,False,True,True,True,False,True,True,True,True,True,True,False,True,False,False,False,False,False,True,True,False,True,False,False,True,True,False,True,False,False,True,False,True,True,False,False,False,True,True,True,False,False,True,True,False,True,False,False,True,True,True,True,True,False,True,False,True,False,True,True,False,True,False,True,False,False,True,False,True,False,True,True,False,False,True,False,True,True,False,False,False,False,True,True,False,True,False,True,True,True,True,True,False,True,False,False,True,False,False,False,False,True,True,True,True,False,True,False,True,False,False,False,False,False,True,False,True,True,True,False,True,False,True,True,True,True,False,False,True,False,False,False,False,False,True,True,False,False,False,False,False,False,False,False,False,True,False,True,True,False,True,False,False,False,True,False,False,True,False,True,False,True,True,False,True,False,True,True,True,True,True,True,False,True,False,False,True,False,False,False,False,True,False,True,False,True,True,False,True,True,True,True,False,True,True,True,True,False,True,False,False,False,False,False,False,False,False,True,False,False,True,True,False,True,False,False,False,True,False,True,False,True,False,True,False,True,False,False,False,True,False,False,False,False,False,False,False,False,True,True,True,False,False,True,True,False,True,True,True,True,True,True,False,True,False,True,True,True,True,True,False,True,True,False,False,True,False,False,True,True,True,False,True,True,True,False,True,False,False,False,True,True,False,False,False,False,True,True,True,False,False,False,True,True,False,True,False,True,False,False,False,True,False,False,True,False,False,False,False,False,True,False,True,True,False,False,True,True,True,True,True,False,True,False,True,True,False,False,False,False,False,True,True,False,True,False,False,True,True,True,False,False,True,True,True,True,True,False,False,True,True,True,True,False,True,False,False,True,False,False,True,False,True,True,True,False,True,True,False,False,False,False,False,True,True,True,False,True,False,False,False,True,True,True,False,True,True,False,False,False,False,False,False,False,True,True,False,False,True,False,True,True,False,True,True,False,True,True,True,True,False,True,False,True,False,False,False,True,False,True,True,True,True,False,True,False,True,True,False,False,False,True,False,False,True,True,False,False,False,True,True,False,False,True,False,False,False,False,False,False,True,True,True,False,True,False,False,True,False,True,True,False,False,True,False,True,False,True,True,True,False,False,True,True,False,True,True,False,False,True,False,True,True,False,False,False,False,False,True,False,True,True,False,False,False,True,True,True,False,True,False,False,True,True,True,True,True,True,True,True,False,False,False,True,False,False,False,False,True,True,True,False,False,True,False,True,False,False,False,False,True,False,True,False,True,False,False,False,True,True,True,False,True,False,True,True,False,True,False,True,True,True,False,True,False,False,False,True,False,False,True,True,False,False,False,False,True,False,False,False,True,False,False,True,False,False,False,False,True,False,False,False,True,False,False,False,False,False,True,True,True,False,False,True,True,False,True,False,False,False,False,False,False,True,True,False,True,True,False,False,False,False,True,True,False,True,True,True,True,False,False,False,True,False,False,False,True,True,False,True,True,False,True,True,True,False,True,False,False,False,True,False,False,False,True,True,True,True,False,False,True,False,True,False,False,True,False,True,False,False,True,False,True,False,True,False,True,True,True,True,True,False,True,True,False,False,False,True,True,False,True,True,False,False,True,True,True,False,False,False,False,True,False,True,False,True,False,True,False,True,False,True,True,True,True,True,True,True,False,True,False]], dtype = "bool")#candidate|7698|(1, 715)|const|bool
call_7695 = relay.TupleGetItem(func_1879_call(relay.reshape(const_7696.astype('uint64'), [5, 5, 6]), relay.reshape(const_7697.astype('int64'), [182, 2]), relay.reshape(const_7697.astype('int64'), [4, 13, 7]), relay.reshape(const_7698.astype('bool'), [715,]), ), 0)
call_7699 = relay.TupleGetItem(func_1884_call(relay.reshape(const_7696.astype('uint64'), [5, 5, 6]), relay.reshape(const_7697.astype('int64'), [182, 2]), relay.reshape(const_7697.astype('int64'), [4, 13, 7]), relay.reshape(const_7698.astype('bool'), [715,]), ), 0)
output = relay.Tuple([call_7667,var_7668,uop_7688,call_7695,const_7696,const_7697,const_7698,])
output2 = relay.Tuple([call_7669,var_7668,uop_7690,call_7699,const_7696,const_7697,const_7698,])
func_7711 = relay.Function([var_7668,], output)
mod['func_7711'] = func_7711
mod = relay.transform.InferType()(mod)
var_7712 = relay.var("var_7712", dtype = "float64", shape = (480,))#candidate|7712|(480,)|var|float64
output = func_7711(var_7712)
func_7713 = relay.Function([var_7712], output)
mutated_mod['func_7713'] = func_7713
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7447_call = mod.get_global_var('func_7447')
func_7448_call = mutated_mod.get_global_var('func_7448')
call_7795 = relay.TupleGetItem(func_7447_call(), 0)
call_7796 = relay.TupleGetItem(func_7448_call(), 0)
output = call_7795
output2 = call_7796
func_7798 = relay.Function([], output)
mod['func_7798'] = func_7798
mod = relay.transform.InferType()(mod)
mutated_mod['func_7798'] = func_7798
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7798_call = mutated_mod.get_global_var('func_7798')
call_7799 = func_7798_call()
output = call_7799
func_7800 = relay.Function([], output)
mutated_mod['func_7800'] = func_7800
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5674_call = mod.get_global_var('func_5674')
func_5676_call = mutated_mod.get_global_var('func_5676')
call_7836 = func_5674_call()
call_7837 = func_5674_call()
output = call_7836
output2 = call_7837
func_7844 = relay.Function([], output)
mod['func_7844'] = func_7844
mod = relay.transform.InferType()(mod)
mutated_mod['func_7844'] = func_7844
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7844_call = mutated_mod.get_global_var('func_7844')
call_7845 = func_7844_call()
output = call_7845
func_7846 = relay.Function([], output)
mutated_mod['func_7846'] = func_7846
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6678_call = mod.get_global_var('func_6678')
func_6680_call = mutated_mod.get_global_var('func_6680')
call_7853 = relay.TupleGetItem(func_6678_call(), 0)
call_7854 = relay.TupleGetItem(func_6680_call(), 0)
func_5791_call = mod.get_global_var('func_5791')
func_5794_call = mutated_mod.get_global_var('func_5794')
var_7860 = relay.var("var_7860", dtype = "float32", shape = (1, 56))#candidate|7860|(1, 56)|var|float32
call_7859 = relay.TupleGetItem(func_5791_call(relay.reshape(var_7860.astype('float32'), [56,])), 2)
call_7861 = relay.TupleGetItem(func_5794_call(relay.reshape(var_7860.astype('float32'), [56,])), 2)
func_3042_call = mod.get_global_var('func_3042')
func_3044_call = mutated_mod.get_global_var('func_3044')
var_7869 = relay.var("var_7869", dtype = "uint64", shape = (100,))#candidate|7869|(100,)|var|uint64
call_7868 = relay.TupleGetItem(func_3042_call(relay.reshape(var_7869.astype('uint64'), [5, 10, 2])), 0)
call_7870 = relay.TupleGetItem(func_3044_call(relay.reshape(var_7869.astype('uint64'), [5, 10, 2])), 0)
func_7844_call = mod.get_global_var('func_7844')
func_7846_call = mutated_mod.get_global_var('func_7846')
call_7881 = func_7844_call()
call_7882 = func_7844_call()
func_755_call = mod.get_global_var('func_755')
func_758_call = mutated_mod.get_global_var('func_758')
const_7900 = relay.const([5,-3,6,-10,-9,5,4,5,-4,-6,-5,4,-8,-6,-2,-4,-10,-2,9,1,10,-1,-3,2,5,8,1,-1,-4,-1,-6,5,-4,-4,-2,-10,3,9,-6,-3,9,2,-3,8,-10,4,-3,-3,8,9,2,-2,-9,-1,2,-7,-5,-2,9,-8,8,-6,2,8,-5,-10,4,-4,-5,-9,8,9,-2,6,10,2,-9,-8,6,-3,-3,-9,-6,-10,-7,7,5,-1,-6,8,-2,-3,7,-1,9,5,6,-9,-5,5,-9,7,8,-1,-4,2,9,6,9,10,-3,10,-7,4,-9,3,-1,4,-8,-6,3,-10,-3,10,-8,-10,5,10,8,-5,-5,4,1,-9,-2,3,3,10,2,10,2,10,-9,-1,-6,-3,-7,9,7,-6,3,6,5,-3,-10,8,2,-1,-8,-9,1,5,3,5,-2,-10,-2,-10,-6,5,-6,8,-1,-1,1,3,-4,-9,4,6,5,-10,2,-6,-3,-4,4,-10,-9,3,-3,-2,-9,-3,-3,9,-4,-8,9,7,-5,-2,1,3,3,9,-6,-2,-2,-8,-5,-4,5,7,6,-5,-3,9,9,5,9,7,-7,-10,5,5,-4,8,2,3,-7,6,-5,7,6,7,8,-1,-4,-5,1,-10,-10,6,4,-8,10,-5,1,-1,4,4,-2,10,-8,-7,-6,3,5,-5,-9,-4,-1,5,10,10,-2,9,-1,-9,3,-7,-3,4,10,-1,-6,-9,3,-10,-8,9,5,5,7,5,2,-1,-2,6,-6,-2,-9,9,5,-5,10,-4,-1,2,-6,10,-7,-6,-7,1,-7,-6,-4,-8,-6,1,-6,2,-5,-7,-9,1,-9,-7,7,-2,10,3,-4,-10,-4,8,-5,9,-5,5,7,-2,-2,5,-6,6,-4,8,9,-10,-9,5,9,8,-4,7,-8,8,-7,-9,-7,-9,-5,-8,-2,-9,7,9,-10,7,7,-3,-7,4,3,9,2,10,-2,4,-9,7,9,-9,2,-2,3,3,-8,4,-2,-1,8,2,4,-5,8,-6,-9,-5,4,-9,5,-7,-1,-6,5,-5,-1,-4,-2,-5,-1,7,-9,-1,10,-1,4,-9,10,-7,-3,7,-1,10,-10,-4,-7,2,-1,-10,-3,-7,-7,-1,4,-4,-10,2,4,5,-6,-6,9,-10,3,3,-10,-4,-9,-6,4,-9,-10,8,-2,9,-1,4,5,10,5,-5,-4,-2,5,-5,7,-3,-4,5,3,5,-1,2,2,-5,5,-9,-10,-3,10,-3,-1,-8,-7,-2,-6,-4,5,-4,-2,-3,-10,8,-5,4,1,4,6,-9,-2,-5,8,-5,7,-8,-10,-6,5,-10,-8,-6,4,1,10,4,2,2,1,3,-9,-7,-3,-9,10,7,-6,7,10,1,-9,-4,4,-1,5,3,4,-3,6,5,1,-3,4,-8,-7,6,4,9,8,-5,5,-7,1,-7,-1,-4,-4,-3,7,5,-10,4,-5,-4,-4,-3,8,-9,9,-5,-8,-7,5,3,9,8,2,-5,-4,7,-9,-6,-2,7,10,-6,-10,5,2,7,-7,-3,6,4,-9,9,-5,7,1,1,-6,4,-9,-1,-6,-2,-5,9,-3,3,-8,-9,9,-10,-10,6,7,1,-6,5,-3,2,-2,-1,-8,6,-9,8,-3,-2,7,-8,-5,-10,-1,2,2,2,-9,-8,9,2,10,-10,8,5,-8,-2,2,-6,7,-9,-4,-2,5,-1,-3,-4,4,-6,-4,2,4,6,7,8,-2,2,7,-10,-3,7,-5,-9,-5,-5,-5,-2,10,4,-10,1,9,-7,-7,-1,9,8,-8,-4,3,-3,-6,-5,3,-4,-2,-6,-8,9,1,8,5,3,-5,8,6,-4,6,-9,-1,-1,-7,3,-9,3,-10,9,6,-3,-1,-9,-2,-1,4,-5,-2,7,-5,-7,3,-6,10,10,-9,9,4,9,2,-4,10,1,-10,-3,9,1,9,-6,-5,7,1,-6,-5,-1,-4,3,-6,6,-5,1,9,5,-1,9,7,-2,3,3,2,4,1,-10,4,-3,4,-2,-7,-5,7,-4,9,3,3,-9,-2,-3,-10,1,8,2,9,-7,10,7,-5,4,-7,7,4,5,6,-10,10,10,-9,-9,4,-7,7,4,2,-5,4,9,7,6,3,-10,1,-8,-2,-9,3,3,-9,-2,-4,2,-9,7,-6,-9,-1,9,-1,-2,-3,1,8,-6,2,10,4,-3,-4,9,5,10,-9,10,7,2,3,-8,7,10,3,-5,-1,-2,-1,8,10,-4,6,-8,-5,2,4,-1,-3,2,10,-5,-10,-7,-9,-6,2,10,3,-8,8,6,-2,-5,-7,-3,8,7,4,-8,-10,3,-4,9,-3,-6,9,-5,1,5,10,-5,5,-4,-10,3,-7,-4,-1,2,2,-7,2,-1,5,-10,-6,-5,9,-10,-2,-10,9,-3,7,-6,-3,-9,8,-7,7,-10,-4,-2,4,3,4,6,9,6,5,6,-7,-1,4,8,7,4,2,-4,7,2,-5,7,-8,-2,6,-10,-3,-8,1,8,-3,-9,10,1,3,1,4,3,-10,4], dtype = "int64")#candidate|7900|(968,)|const|int64
const_7901 = relay.const(3, dtype = "uint64")#candidate|7901|()|const|uint64
call_7899 = relay.TupleGetItem(func_755_call(relay.reshape(const_7900.astype('int64'), [8, 11, 11]), relay.reshape(const_7901.astype('uint64'), []), ), 1)
call_7902 = relay.TupleGetItem(func_758_call(relay.reshape(const_7900.astype('int64'), [8, 11, 11]), relay.reshape(const_7901.astype('uint64'), []), ), 1)
output = relay.Tuple([call_7853,call_7859,var_7860,call_7868,var_7869,call_7881,call_7899,const_7900,const_7901,])
output2 = relay.Tuple([call_7854,call_7861,var_7860,call_7870,var_7869,call_7882,call_7902,const_7900,const_7901,])
func_7915 = relay.Function([var_7860,var_7869,], output)
mod['func_7915'] = func_7915
mod = relay.transform.InferType()(mod)
var_7916 = relay.var("var_7916", dtype = "float32", shape = (1, 56))#candidate|7916|(1, 56)|var|float32
var_7917 = relay.var("var_7917", dtype = "uint64", shape = (100,))#candidate|7917|(100,)|var|uint64
output = func_7915(var_7916,var_7917,)
func_7918 = relay.Function([var_7916,var_7917,], output)
mutated_mod['func_7918'] = func_7918
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5717_call = mod.get_global_var('func_5717')
func_5718_call = mutated_mod.get_global_var('func_5718')
call_7923 = relay.TupleGetItem(func_5717_call(), 0)
call_7924 = relay.TupleGetItem(func_5718_call(), 0)
output = call_7923
output2 = call_7924
func_7929 = relay.Function([], output)
mod['func_7929'] = func_7929
mod = relay.transform.InferType()(mod)
output = func_7929()
func_7930 = relay.Function([], output)
mutated_mod['func_7930'] = func_7930
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6319_call = mod.get_global_var('func_6319')
func_6321_call = mutated_mod.get_global_var('func_6321')
call_7951 = relay.TupleGetItem(func_6319_call(), 0)
call_7952 = relay.TupleGetItem(func_6321_call(), 0)
func_1806_call = mod.get_global_var('func_1806')
func_1809_call = mutated_mod.get_global_var('func_1809')
const_7958 = relay.const(-2, dtype = "uint64")#candidate|7958|()|const|uint64
call_7957 = relay.TupleGetItem(func_1806_call(relay.reshape(const_7958.astype('uint64'), [])), 0)
call_7959 = relay.TupleGetItem(func_1809_call(relay.reshape(const_7958.astype('uint64'), [])), 0)
func_5341_call = mod.get_global_var('func_5341')
func_5347_call = mutated_mod.get_global_var('func_5347')
var_7963 = relay.var("var_7963", dtype = "int64", shape = (390,))#candidate|7963|(390,)|var|int64
const_7964 = relay.const([4,4,-2,-8,-6,7,10,-1,-10,3,9,9,3,-3,8,-2,-6,8,1,-2,-1,-10,-10,-3,3,8,-6,-10,-4,-5,4,5,-6,-8,8,-3,-9,-2,-5,9,-9,-10,5,5,4,2,-1,-10,9,-3,9,8,10,-7,2,-3,-5,7,6,1,-6,-9,-9,4,-8,9,-3,-5,6,8,-10,-1,7,-4,4,2,-8,6,2,9,7,7,-4,4,6,8,-4,-10,-6,1,-2,9,8,9,-7,9,-6,-5,1,-8], dtype = "uint64")#candidate|7964|(100,)|const|uint64
const_7965 = relay.const([3,-4,-6,1,-2,2,5,9,7,-4,-2,-5,1,-8,2,-7,-7,-2,-5,10,-6,-1,10,4,-5,-8,-7,4,8,8,-3,7,-8,-3,-1,-10,-3,7,8,3,-8,-10,3,-4,6,-2,-7,-9,9,-7,2,9,-8,-1,6,2,6,-10,8,1,-5,4,-4,-6,4,-5,-1,-6,-9,-5,-4,10,9,-10,-1,10,5,-10,9,-4,-1,1,-3,1,5,-8,3,8,5,10,8,6,5,4,1,-7,7,4,-7,2,1,9,-8,-9,-5,-1,-8,-8,-2,-9,10,-5,5,5,-4,-2,-8,10,-7,9,7,-7,-8,10,-9,4,6,-6,-1,-1,-9,2,3,3,3,4,-3,-7,-9,-2,-7,-10,6,-3,1,1,-6,-7,-5,1,-2,7,9,8,-2,-8,7,-1,-6,-9,8,-6,3,5,6,9,4,-5,2,1,-6,-1,7,-7,6,-9,-7,9,10,1,2,6,-6,9,6,9,8,-4,-4,7,8,4,-3,-5,-9,-1,-6,8,-9,7,-6,-7,8,9,-4,-2,4,-6,-9,2,-9,10,1,5,-5,-5,-1,-7,-4,1,-5,-10,6,-8,7,2,6,-9,-10,-8,9,7,-6,10,-3,9,1,8,3,4,-7,-8,-8,1,3,2,1,-3,6,-8,-2,10,6,5,-4,-1,-5,6,-8,-1,4,-3,7,-3,-9,3,-10,7,10,7,-10,7,-9,-9,1,6,-5,2,6,4,-10,7,1,8,-5,-7,5,-8,-8,1,-7,7,-7,4,6,-9,9,8,7,3,-1,6,-4,-2,3,4,-2,4,9,5,9,2,9,8,-8,-9,-1,6,-1,-10,2,8,2,-7,1,-6,5,8,10,9,9,6,5,5,-10,2,-6,8,-4,9,-7,6,5,-6,-2,-2,5,8,9,5,8,-3,-10,4,-8,-9,-10,-8,9,-9,-1,1,-8,-3,4,-6,7,-9,-4,1,8,6,-5,10,-8,-6,-9,-4,-9,3,9,6,-1,-5,7,-7,-5,2,7,5,-2,-6,-1,-7,-9,4,10,-4,-6,-7,4,-10,7,1,4,3,9,7,2,-10,2,9,-3,-4,3,-4,5,7,5,-10,-4,-7,2,2,-7,5,6,3,10,-2,9,9,9,-8,4,5,10,-2,3,-8,-8,-10,-8,8,10,-10,-6,-5,-5,-1,-10,6,8,2,-3,4,5,8,8,-1,3,-7,10,-4,-4,5,-1,4,8,3,-8,5,-10,7,6,-6,9,8,5,8,8,5,-2,-9,5,-6,-6,6,-3,-3,1,9,-5,3,10,-1,-3,-8,-5,9,-8,5,-5,1,4,-6,5,6,2,-10,-1,1,-7,-10,5,-2,-2,6,-10,5,10,10,7,-3,-7,1,4,-1,10,-3,1,-7,-4,10,7,9,-7,1,7,2,9,-2,-7,3,-6,-4,4,10,2,4,-5,5,2,-3,3,4,9,4,1,-5,4,6,9,-5,-5,-10,-2,2,4,4,1,7,4,-7,-9,-3,-2,-2,-4,3,8,8,10,-5,-5,10,-6,7,-10,-6,9,-3,-8,-5,4,2,3,1,1,-8,4,4,8,-10,8,-7,-5,1,5,-8,3,-10,-1,10,6,10,-7,-8,8,1,-3,-6,-1,2,2,-7,-1,1,-6,3,8,-2,10,8,-7,5,-9,6,7,-6,-9,3,-9,-1,-5,9,-10,8,10,-9,5,6,-6,-4,4,1,4,-5,-8,10,-3,-7,-1,-4,-1,7,-6,1,-9,4,-6,7,8,-5,-8,-2,-5,3,-5,6,-9,-3,-7,-8,1,10,-8,-7,8,-5,-8,-5,-7,8,7,-10,-8,3,9,-4,5,8,-10,10,-9,-2,3,10,8,-5,-4,3,-10,-9,-10,-9,-6,10,2,-2,6,-7,-3,-2,9,-8,-2,6,9,-1,10,-6,7,-10,6,1,8,-5,-7,4,2,-10,4,6,-5,4,7,2,6,2,-4,5,10,-2,7,-4,7,5,4,-5,-6,-4,9,-6,6,6,-10,-3,-1,9,1,6,9,-9,3,-2,3,4,2,6,8,9,4,-2,6,-4,-7,5,4,-1,-8,-5,-10,4,9,-1,5,-8,-1,6,2,-6,-10,8,-3,-10,5,5,-4,-7,-10,-1,8,5,-10,1,-1,-2,6,-7,-1,3,4,-1,-6,3,-9,-2,-6,8,-10,-7,-6,5,10,-2,-1,-7,2,5,-8,-5,-5,-6,5,-4,-5,-7,-9,-2,4,-2,-10,2,-8,-1,5,5,-4,-10,7,6,-4,-2,3,4,1,-4,4,4,-3,2,2,8,8,-8,10,6,7,9,-3,9,8,4,9,7,2,8,5,-3,3,-10,5,9,4,-2,-2,1,-6,3,1,-7,-7,1,2,9,-5,-10,-6,4,6,9,9,-7,2,-10,2,-8,-4,-3,4,2,2,2,1,-10,-2,-5,8,5,2,5,-5,-2,-5,-5,-10,10,9,2,8,4,-2,10,-1,-3,2,-8,4,-6,-9,-8,8,-1,-10,6,6,7,-1,9,5,6,2,6,3,5,-3,-1], dtype = "int64")#candidate|7965|(968,)|const|int64
call_7962 = relay.TupleGetItem(func_5341_call(relay.reshape(var_7963.astype('int64'), [13, 2, 15]), relay.reshape(var_7963.astype('int64'), [13, 2, 15]), relay.reshape(const_7964.astype('uint64'), [100,]), relay.reshape(const_7965.astype('int64'), [968,]), ), 6)
call_7966 = relay.TupleGetItem(func_5347_call(relay.reshape(var_7963.astype('int64'), [13, 2, 15]), relay.reshape(var_7963.astype('int64'), [13, 2, 15]), relay.reshape(const_7964.astype('uint64'), [100,]), relay.reshape(const_7965.astype('int64'), [968,]), ), 6)
func_5791_call = mod.get_global_var('func_5791')
func_5794_call = mutated_mod.get_global_var('func_5794')
const_7969 = relay.const([[4.982824,-2.548701,-3.273271,0.672709],[-6.872816,1.329236,0.348082,9.019683],[1.680851,-3.014374,0.352960,-6.325109],[1.101917,-6.546549,2.681704,7.848062],[-8.864241,3.789713,-4.000789,-8.142797],[-4.996974,8.502705,-8.122029,-0.766811],[-6.018588,6.697401,4.473992,-0.667226],[5.444893,-7.627300,6.032450,1.421023],[-0.432126,-4.310011,0.378525,0.513396],[-8.537570,-9.629627,-4.184221,-1.326522],[0.324242,-8.322027,-8.132120,1.260134],[0.861110,-0.981476,7.439107,2.518487],[-9.317595,-7.808667,-7.213934,3.678894],[9.197120,-0.241989,-3.339575,-6.668227]], dtype = "float32")#candidate|7969|(14, 4)|const|float32
call_7968 = relay.TupleGetItem(func_5791_call(relay.reshape(const_7969.astype('float32'), [56,])), 2)
call_7970 = relay.TupleGetItem(func_5794_call(relay.reshape(const_7969.astype('float32'), [56,])), 2)
output = relay.Tuple([call_7951,call_7957,const_7958,call_7962,var_7963,const_7964,const_7965,call_7968,const_7969,])
output2 = relay.Tuple([call_7952,call_7959,const_7958,call_7966,var_7963,const_7964,const_7965,call_7970,const_7969,])
func_7973 = relay.Function([var_7963,], output)
mod['func_7973'] = func_7973
mod = relay.transform.InferType()(mod)
var_7974 = relay.var("var_7974", dtype = "int64", shape = (390,))#candidate|7974|(390,)|var|int64
output = func_7973(var_7974)
func_7975 = relay.Function([var_7974], output)
mutated_mod['func_7975'] = func_7975
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7844_call = mod.get_global_var('func_7844')
func_7846_call = mutated_mod.get_global_var('func_7846')
call_7996 = func_7844_call()
call_7997 = func_7844_call()
func_7798_call = mod.get_global_var('func_7798')
func_7800_call = mutated_mod.get_global_var('func_7800')
call_8040 = func_7798_call()
call_8041 = func_7798_call()
func_6663_call = mod.get_global_var('func_6663')
func_6665_call = mutated_mod.get_global_var('func_6665')
var_8050 = relay.var("var_8050", dtype = "float32", shape = (260,))#candidate|8050|(260,)|var|float32
call_8049 = relay.TupleGetItem(func_6663_call(relay.reshape(var_8050.astype('float32'), [260,])), 2)
call_8051 = relay.TupleGetItem(func_6665_call(relay.reshape(var_8050.astype('float32'), [260,])), 2)
func_4652_call = mod.get_global_var('func_4652')
func_4658_call = mutated_mod.get_global_var('func_4658')
var_8054 = relay.var("var_8054", dtype = "int64", shape = ())#candidate|8054|()|var|int64
var_8055 = relay.var("var_8055", dtype = "int64", shape = (364,))#candidate|8055|(364,)|var|int64
var_8056 = relay.var("var_8056", dtype = "uint16", shape = (880,))#candidate|8056|(880,)|var|uint16
var_8057 = relay.var("var_8057", dtype = "float32", shape = (180,))#candidate|8057|(180,)|var|float32
var_8058 = relay.var("var_8058", dtype = "float64", shape = (352, 2))#candidate|8058|(352, 2)|var|float64
call_8053 = relay.TupleGetItem(func_4652_call(relay.reshape(var_8054.astype('int64'), []), relay.reshape(var_8055.astype('int64'), [364,]), relay.reshape(var_8056.astype('uint16'), [880,]), relay.reshape(var_8057.astype('float32'), [90, 2]), relay.reshape(var_8058.astype('float64'), [704,]), ), 5)
call_8059 = relay.TupleGetItem(func_4658_call(relay.reshape(var_8054.astype('int64'), []), relay.reshape(var_8055.astype('int64'), [364,]), relay.reshape(var_8056.astype('uint16'), [880,]), relay.reshape(var_8057.astype('float32'), [90, 2]), relay.reshape(var_8058.astype('float64'), [704,]), ), 5)
output = relay.Tuple([call_7996,call_8040,call_8049,var_8050,call_8053,var_8054,var_8055,var_8056,var_8057,var_8058,])
output2 = relay.Tuple([call_7997,call_8041,call_8051,var_8050,call_8059,var_8054,var_8055,var_8056,var_8057,var_8058,])
func_8070 = relay.Function([var_8050,var_8054,var_8055,var_8056,var_8057,var_8058,], output)
mod['func_8070'] = func_8070
mod = relay.transform.InferType()(mod)
var_8071 = relay.var("var_8071", dtype = "float32", shape = (260,))#candidate|8071|(260,)|var|float32
var_8072 = relay.var("var_8072", dtype = "int64", shape = ())#candidate|8072|()|var|int64
var_8073 = relay.var("var_8073", dtype = "int64", shape = (364,))#candidate|8073|(364,)|var|int64
var_8074 = relay.var("var_8074", dtype = "uint16", shape = (880,))#candidate|8074|(880,)|var|uint16
var_8075 = relay.var("var_8075", dtype = "float32", shape = (180,))#candidate|8075|(180,)|var|float32
var_8076 = relay.var("var_8076", dtype = "float64", shape = (352, 2))#candidate|8076|(352, 2)|var|float64
output = func_8070(var_8071,var_8072,var_8073,var_8074,var_8075,var_8076,)
func_8077 = relay.Function([var_8071,var_8072,var_8073,var_8074,var_8075,var_8076,], output)
mutated_mod['func_8077'] = func_8077
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6025_call = mod.get_global_var('func_6025')
func_6026_call = mutated_mod.get_global_var('func_6026')
call_8089 = relay.TupleGetItem(func_6025_call(), 0)
call_8090 = relay.TupleGetItem(func_6026_call(), 0)
uop_8101 = relay.asin(call_8089.astype('float32')) # shape=(15, 9, 6)
uop_8103 = relay.asin(call_8090.astype('float32')) # shape=(15, 9, 6)
func_1484_call = mod.get_global_var('func_1484')
func_1488_call = mutated_mod.get_global_var('func_1488')
var_8106 = relay.var("var_8106", dtype = "float64", shape = (2016,))#candidate|8106|(2016,)|var|float64
const_8107 = relay.const([[3,-3,8,-5,8,5,9,3,-6,6,8,-3,6,-5,-5,4,5,-5,1,3,7,-9,-9,-4,7,-8,-5,7,5,10,-8,-8,-2,-7,4,4,8,-8,8,-4,4,-1,5,10,-9,-1,-5,-2,-3,1,9,-9,-1,-5,-10,3,5,5,-3,1,7,8,3,10,1,3,9,6,-8,-8,-10,-4,-8,-6,-6,-2,8,-7,-2,-7,2,-10,2,10,6,10,-2,4,5,-8,4,-6,-10,7,1,4,4,4,-3,-7,4,-7,-2,-6,-1,-10,4,1,-8,-9,-2,2,-10,-3,-1,-2,-10,1,1,10,4,7,7,-4,-6,-6,8,4,4,-9,-2,2,-1,5,-2,2,-7,4,8,-9,-2,1,-2,-8,-6,3,-9,9,10,9,-9,8,1,9,1,-2,-2,-5,-1,3,1,5,-3,-9,8,-4,1,4,5,1,-1,1,7,-10,-8,-4,-2,-10,-3,7,6,-8,-5,-9,6,-6,-3,2,2,8,6,-10,3,3,-8,-5,2,-1,6,5,10,-8,-8,-4,-4,-10,-6,-9,2,-3,2,5,5,-1,10,4,-9,4,3,-10,2,-7,2,-7,2,5,2,-8,-9,-8,6,8,4,-5,-4,6,-4,-4,3,-1,3,-8,7,2,4,-5,-1,6,-7,-4,5,-6,-5,7,6,-10,5,4,4,10,-7,8,9,3,4,-8,-9,8,-7,-9,-3,1,-9,-2,2,-2,-6,-7,4,-1,-9,-7,-3,10,8,-2,2,-8,2,-5,1,-3,6,10,-2,-10,7,-9,10,10,-1,-10,-10,6,-10,6,6,8,9,-4,8,2,-1,6,10,-1,10,6,2,2,2,-3,7,-2,9,9,-2,-3,-2,6,8,-5,-9,-10,2,2,8,-2,-7,1,-4,5,1,-9,-8,-7,2,-7,-2,3,7,-9,1,9,-8,7,-1,8,-10,-7,3,7,5,-10,8,-4,-9,1,-4,9,1,6,8,-5,4,-9,5,6,-9,-10,8,-6,-5,-6,-7,5,-2,-1,-8,9,10,8,-5,7,1,-4,1,7,-5,7,1,-2,-4,3,9,3,-1,5,5,9,1,-6,-3,8,-7,2,8,1,6,3,6,-5,7,3,3,-2,5,-7,-3,8,10,8,-5,2,-10,7,1,3,3,1],[-7,-10,-1,3,-2,3,-3,1,-7,7,8,-3,7,8,-1,-8,4,-1,5,-8,-4,-10,-10,-3,4,6,6,-10,7,-7,-8,5,2,-6,9,-5,-3,-8,-8,3,2,3,-1,5,2,6,-6,2,6,-7,10,-8,9,-9,8,8,-3,10,-5,-2,6,6,9,-9,6,2,10,-10,-5,-5,-10,2,3,7,-4,4,7,1,-10,2,8,1,-3,6,-9,-10,-5,4,2,-7,-10,-8,3,-6,-10,8,-4,6,1,5,5,2,-8,8,-6,8,-8,-5,-8,5,-9,5,-3,1,3,5,-3,-7,-3,-3,-2,7,9,-2,-4,4,1,9,10,-9,7,-2,2,3,6,4,-9,9,-6,-5,-9,6,-8,-5,6,-5,9,7,-7,-7,-6,-1,6,3,1,2,6,-10,-4,7,9,7,9,1,2,-9,3,-3,7,10,-3,8,10,-6,-2,-6,-4,3,5,-9,6,-9,-7,-7,-8,4,9,5,-9,6,5,-4,-3,4,1,-8,3,-5,10,5,-10,3,1,9,-8,-3,6,-4,4,-10,-1,-3,6,5,1,7,-10,-9,8,-1,4,1,-3,1,-1,4,7,-10,-5,-2,6,-6,-10,7,6,6,2,-9,2,-2,-9,9,-4,-3,-4,7,-4,6,1,-4,1,-6,9,10,5,6,-10,2,-4,5,9,9,7,7,-1,3,-5,9,-4,5,2,-3,-8,6,-1,-1,-3,4,-10,-7,4,-6,-1,-2,5,6,1,-10,6,3,7,6,8,9,10,10,-10,-2,-1,-7,2,-4,3,-3,9,4,4,3,1,10,2,5,6,2,-2,4,10,-8,-3,2,9,-6,-10,-2,5,-2,2,8,7,-5,-8,-2,8,-1,-10,-3,-1,-9,9,1,5,-10,3,3,7,8,7,-4,-9,-8,-10,-8,-9,3,10,2,1,10,-4,-3,-1,8,2,-4,9,-10,10,-1,6,-9,-1,-2,6,6,7,1,-2,-7,-1,5,-1,-8,-4,-2,-4,-9,-3,-9,4,-7,7,-10,-6,-3,-8,-4,5,1,-2,2,-5,5,1,-5,7,8,9,-3,7,-10,8,3,8,5,-9,8,-7,2,-4,2,8,-7,8,-9,-8,9,5,-9,7,4,2,-2,4,-6,-10,2,-8,4,-3,-10]], dtype = "uint16")#candidate|8107|(2, 440)|const|uint16
call_8105 = relay.TupleGetItem(func_1484_call(relay.reshape(var_8106.astype('float64'), [9, 14, 16]), relay.reshape(const_8107.astype('uint16'), [880,]), ), 0)
call_8108 = relay.TupleGetItem(func_1488_call(relay.reshape(var_8106.astype('float64'), [9, 14, 16]), relay.reshape(const_8107.astype('uint16'), [880,]), ), 0)
uop_8111 = relay.atanh(var_8106.astype('float64')) # shape=(2016,)
output = relay.Tuple([uop_8101,call_8105,const_8107,uop_8111,])
output2 = relay.Tuple([uop_8103,call_8108,const_8107,uop_8111,])
func_8113 = relay.Function([var_8106,], output)
mod['func_8113'] = func_8113
mod = relay.transform.InferType()(mod)
var_8114 = relay.var("var_8114", dtype = "float64", shape = (2016,))#candidate|8114|(2016,)|var|float64
output = func_8113(var_8114)
func_8115 = relay.Function([var_8114], output)
mutated_mod['func_8115'] = func_8115
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8150 = relay.var("var_8150", dtype = "float64", shape = (11, 3, 3))#candidate|8150|(11, 3, 3)|var|float64
uop_8151 = relay.rsqrt(var_8150.astype('float64')) # shape=(11, 3, 3)
bop_8173 = relay.minimum(uop_8151.astype('uint64'), relay.reshape(var_8150.astype('uint64'), relay.shape_of(uop_8151))) # shape=(11, 3, 3)
output = relay.Tuple([bop_8173,])
output2 = relay.Tuple([bop_8173,])
func_8183 = relay.Function([var_8150,], output)
mod['func_8183'] = func_8183
mod = relay.transform.InferType()(mod)
mutated_mod['func_8183'] = func_8183
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8184 = relay.var("var_8184", dtype = "float64", shape = (11, 3, 3))#candidate|8184|(11, 3, 3)|var|float64
func_8183_call = mutated_mod.get_global_var('func_8183')
call_8185 = func_8183_call(var_8184)
output = call_8185
func_8186 = relay.Function([var_8184], output)
mutated_mod['func_8186'] = func_8186
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6319_call = mod.get_global_var('func_6319')
func_6321_call = mutated_mod.get_global_var('func_6321')
call_8211 = relay.TupleGetItem(func_6319_call(), 2)
call_8212 = relay.TupleGetItem(func_6321_call(), 2)
output = call_8211
output2 = call_8212
func_8246 = relay.Function([], output)
mod['func_8246'] = func_8246
mod = relay.transform.InferType()(mod)
output = func_8246()
func_8247 = relay.Function([], output)
mutated_mod['func_8247'] = func_8247
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7929_call = mod.get_global_var('func_7929')
func_7930_call = mutated_mod.get_global_var('func_7930')
call_8262 = func_7929_call()
call_8263 = func_7929_call()
output = call_8262
output2 = call_8263
func_8298 = relay.Function([], output)
mod['func_8298'] = func_8298
mod = relay.transform.InferType()(mod)
mutated_mod['func_8298'] = func_8298
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8298_call = mutated_mod.get_global_var('func_8298')
call_8299 = func_8298_call()
output = call_8299
func_8300 = relay.Function([], output)
mutated_mod['func_8300'] = func_8300
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8298_call = mod.get_global_var('func_8298')
func_8300_call = mutated_mod.get_global_var('func_8300')
call_8310 = func_8298_call()
call_8311 = func_8298_call()
func_6610_call = mod.get_global_var('func_6610')
func_6615_call = mutated_mod.get_global_var('func_6615')
var_8313 = relay.var("var_8313", dtype = "int64", shape = (390,))#candidate|8313|(390,)|var|int64
const_8314 = relay.const([-9,-2,-9,5,5,-2,-2,7,-4,-9,6,6,-8,-5,-1,10,5,-9,5,6,10,2,-1,-3,-1,-8,2,10,3,8,4,-5,2,-3,-8,6,9,9,6,-4,6,3,-6,-6,8,2,-4,1,1,-2,3,8,-5,-3,-10,-5,9,-2,10,-3,-4,10,-3,5,-5,4,4,-3,10,-7,2,-5,-1,-7,7,-9,6,2,-10,-3,3,-2,-1,5,10,-10,-7,5,-1,10,2,-10,9,-8,-8,-4,10,9,1,-1,-7,5,-7,1,5,-8,1,5,-10,10,6,1,10,-5,2,-1,-8,-3,9,5,-7,10,10,9,10,10,-3,-10,-8,3,-3,-1,3,6,-9,-5,-3,-4,2,-5,-3,10,3,-9,7,3,10,-2,7,6,-8,-2,-10,6,-10,-6,-5,8,-8,-10,-1,-4,-8,-6,6,-3,-5,-7,-9,-6,-3,1,9,-5,8,-2,10,-2,4,-5,9,5,1,8,-5,1,7,6,-5,2,8,-4,2,9,5,-6,-2,-10,-1,6,-3,3,-1,5,-2,9,3,-10,-1,-2,-5,-5,-7,3,-3,5,-6,-7,9,-10,1,1,-3,2,2,-2,-10,5,2,-7,-6,3,3,8,-2,-1,8,-8,2,4,-3,10,-3,-3,4,-2,-4,-4,-4,7,9,-10,1,-7,-7,-7,-9,-4,-4,9,-8,-10,-5,7,5,7,5,2,-5,-1,1,-5,-6,5,7,-10,5,5,-2,-1,-10,4,8,-3,6,7,3,10,-2,-1,-6,-4,-9,-1,5,2,10,3,2,1,10,-7,-2,2,9,5,-4,-6,-9,-6,1,-10,-3,-9,8,5,1,-1,-9,9,6,-5,2,-3,-10,-5,-8,2,-9,6,-4,-5,5,8,-9,-1,-8,5,-10,10,9,1,-2,9,-5,-7,8,-1,-8,-6,-5,-3,-5,-4,-1,5,10,7,10,-3,3,-3,4,5,-5,2,-9,-5,-5,9,3,-6,-1,-5,1,5,10,4,-4,-7,-9,10,-3,-4,4,-6,9,-8,-7,3,-4,9,-8,9,1,2,-6,9,7,-2,9,6,2,-10,10,6,-2,10,-9,2,9,-3,6,6,5,4,8,4,5,-8,5,-1,-10,-7,-9,2,-2,-3,-6,4,9,-7,-10,-6,3,2,-9,-7,1,9,-4,8,-3,-8,9,2,2,4,10,-8,3,3,2,-10,-7,-5,-9,8,-3,3,-8,2,4,-1,6,-9,7,3,-3,2,-4,-10,-9,7,5,-4,6,-1,3,-7,9,-2,-8,-8,9,-1,-7,6,-9,8,4,7,9,2,-9,-3,-7,-9,-9,7,6,-1,-9,9,-1,-4,-10,-4,-8,-4,-9,7,1,2,2,-10,-9,1,7,8,10,2,2,10,-6,6,1,-3,1,6,5,4,-6,-4,9,-2,3,-9,-2,4,3,-3,-5,-1,-10,-2,1,-10,2,-2,5,10,-10,2,7,-7,-6,-9,5,-9,-4,-1,-8,-4,7,3,-1,-10,3,-10,8,3,8,-4,9,-9,4,-10,4,-5,1,3,-5,3,-4,8,-2,5,4,-4,-5,-8,6,-3,1,1,8,-1,4,-10,-9,-10,1,1,-7,10,10,10,5,6,3,-5,-9,5,4,-2,4,-4,-9,2,-1,-7,10,7,-3,1,-8,9,7,-1,-9,-2,8,10,10,-5,-4,-2,-4,-10,-9,4,-9,5,7,7,-10,1,-6,7,-2,-6,7,-1,-6,7,-5,-5,4,-2,-7,-10,-9,-8,1,10,-8,-10,-6,-3,3,8,-2,4,-4,-8,-5,-1,-9,-1,4,4,10,4,-6,-8,8,-6,-10,6,-7,8,-5,8,10,4,1,-4,3,-4,-7,-7,8,-5,6,-4,-8,-6,-3,-6,-6,-5,-2,7,-8,-4,5,2,-7,-4,2,5,-2,4,-9,-8,-3,-1,3,10,-9,6,6,-9,-7,-5,3,-9,-4,2,-3,6,3,-3,-5,10,7,-10,-6,-5,2,-3,1,1,7,7,-4,-8,-2,5,-3,-1,-1,-5,-10,1,2,8,-6,-9,2,4,10,-3,2,10,-3,10,-6,10,-5,9,-4,1,5,4,-5,-3,10,-9,-4,-10,4,10,4,5,8,7,2,-4,7,6,6,-10,5,-9,-10,7,-8,1,4,1,1,-6,5,10,7,5,5,-10,-5,-3,-7,-9,7,6,8,-5,-5,-10,2,4,7,-3,-7,5,1,8,-8,2,9,-7,7,-7,-5,-5,-8,8,-10,-6,-5,10,-8,-5,-9,2,-7,6,2,-6,-10,-6,2,2,7,1,-10,10,-1,-6,2,-10,-8,-2,-10,7,-9,-8,9,3,9,-9,-4,1,-2,8,7,-2,4,5,-2,4,9,4,-4,-3,-10,-6,-1,-4,5,8,9,9,6,7,-8,1,5,-5,-4,-3,-1,3,-5,-7,-8,-4,-7,-2,7,-10,2,-4,1,-7,-8,-3,9,-10,-2,7,-2,-9,-4,-1,-10,-7,4,-1,-3,-10,-9,1,-9,-4,-10,3,2,10,-2,-6,-1,7,8,-10,8,-1,5,5,-3,-6,-10,6,2,-9,-8,-9], dtype = "int64")#candidate|8314|(968,)|const|int64
const_8315 = relay.const([-2.547187,1.232650,3.343376,-8.894451,-7.464345,8.535183,-1.339957,1.912547,-9.590383,-6.801952,3.253215,-4.185334,-4.036515,7.164922,-5.027919,-1.739557,-9.569383,3.949426,0.230872,2.174784,0.282992,0.534841,4.439075,0.784706,-1.494938,-5.381653,-2.779594,-7.801363,-7.559753,-1.856823,-1.256355,5.946763,-2.173773,-7.434251,-8.765451,-4.007403,-8.726219,-2.326072,-2.714697,-8.671756,7.356754,-2.655037,2.218361,2.463497,8.153962,-7.680627,-4.654786,-2.503226,-7.522967,-6.252089,0.173713,-6.505337,-7.157720,6.100472,-2.156504,5.432696,4.471772,0.813177,-7.613761,-6.806181,7.733444,2.350588,-4.431630,-1.061984,9.381167,-6.720161,5.398821,-1.248512,2.052939,-6.367190,9.055679,8.746541,-1.945840,-9.248642,4.667528,-4.810285,7.528980,-9.301072,3.003200,9.666508,-3.217046,5.860845,-6.896105,4.958417,-5.265799,-6.330905,-1.708689,-4.331317,-0.703508,9.971358,8.781110,-6.209113,-2.451370,-9.157113,-8.275166,-6.453714,8.242161,-3.992031,1.055142,0.194249,-7.813643,-7.846831,-2.404634,0.991950,4.031448,-7.625957,-4.347851,3.716135,-8.197824,-6.287794,3.050389,0.566300,6.800079,9.487673,8.416820,-6.925761,-6.748030,-0.696685,9.456954,4.986771,3.941443,7.858654,1.721601,-1.375424,-8.806636,-8.617228,8.261668,7.457135,5.143541,2.015943,6.550508,-8.789948,-8.737587,-6.620547,-4.169192,-6.318255,-7.880590,3.083553,6.409080,0.950899,7.904729,6.247701,1.616478,3.955007,2.089726,7.105306,-3.828159,-3.897988,2.994358,-6.377469,2.479445,9.178797,-5.965539,7.177555,-5.721684,3.207971,-5.040802,-5.698771,3.174827,-1.332838,-3.445481,-8.830410,-3.013595,-9.357240,1.969133,5.498633,7.926775,-8.776892,-6.958918,0.211411,-3.413527,-4.320607,-4.082591,-5.967906,-2.356232,-1.591858,4.433358,9.634445,-9.560651,6.217504,-7.329270,-5.733768,2.224383,4.347417,-2.198678,-6.471969,1.853613,8.979578,9.134835,-6.571600,-3.085670,-1.774693,8.989518,9.691901,5.069576,1.745844,-4.027843,-6.250685,3.937746,9.614861,-6.082328,-3.173933,-7.336008,7.275304,-5.716364,4.149523,4.272067,-9.304657,4.177418,-1.870015,-4.274859,-1.695679,2.991301,-9.540737,-5.509125,-0.862331,7.224541,-0.213089,-6.032625,0.145476,3.163518,3.924053,-0.250779,7.663188,-0.086894,8.788165,-7.504699,4.565322,-4.370551,-8.007379,6.754654,2.591294,4.452093,-1.337165,-5.191232,-8.051993,-6.792779,-2.812149,7.304839,-0.366923,3.065423,-6.378693,0.625321,8.476238,1.362639,-3.148892,-1.578684,5.157031,1.148524,2.462015,6.086614,-6.002850,2.889417,9.928430,-1.863184,-8.332296,7.803064,0.483053,-0.433181,-9.511630,-7.129510,-5.666748,-1.009634,9.555863,5.997046,5.184989,-7.507952,-4.756950,-1.550930,3.977112,8.919460,-7.569045,-8.685445,8.385771,-0.246458,9.481303,-9.262410,1.123035,6.673327,9.013993,8.730539,-4.608322,-0.419985,-9.251384,-8.522062,2.656156,6.420123,-4.263075,-8.630439,6.032229,3.813052,5.875161,-7.853590,-2.494824,3.273310,4.542052,1.814583,7.492815,-3.733537,-3.903306,1.078724,5.288097,-0.553319,-5.139725,2.678883,7.269805,-2.003219,6.944823,-9.539193,9.866685,3.474008,-0.251991,-8.808496,-4.046966,9.717897,8.209165,-3.477784,-7.407506,-8.091723,6.800162,-1.353261,-3.707325,-1.439897,5.025748,9.075452,-5.440611,4.586601,4.216914,-3.759661,0.698477,2.458149,-9.765536,0.692188,-2.512784,-6.642760,9.477964,-1.593655,7.539640,6.715529,9.587175,2.891525,7.807401,7.030280,-8.720608,-0.686043,1.508017,-8.127165,-1.547709,-7.921643,3.443118,-5.579851,6.946292,-1.946640,3.378830,-6.406596,1.848395,2.589022,-9.034827,0.369427,-0.907309,-4.204197,3.626137,-2.569557,-5.332631,-7.769727,0.518329,0.754763,-1.056368,2.806134,6.286105,-0.488223,-6.966068,-0.289895,-5.182410,0.217568,3.017195,9.842438,5.213943,-5.957273,-4.972623,3.209067,-7.331580,0.877405,8.401744,-3.478819,-3.820394,3.688019,-3.696017,4.389694,5.382042,-6.673448,5.946889,-5.933913,6.336059,-1.412247,1.866429,8.864237,-5.719619,-2.188927,4.021794,8.417190,-0.992160,-7.055779,-4.892626,5.358411,2.781995,-0.644252,2.638756,5.577311,-5.053010,4.088049,8.075386,6.343124,8.958832,8.080452,-3.997177,-5.799363,7.735170,-1.453231,-0.813689,-6.931528,9.481139,-2.474236,5.837616,6.738556,-7.737251,9.632564,0.300086,1.113233,9.707203,0.580631,6.449928,-4.859861,8.112110,-3.215642,-5.378731,8.640729,-8.888801,7.210925,2.691422,6.921516,1.323041,4.246809,9.127333,5.433864,-3.367857,-4.235481,-8.508280,-6.587091,5.971198,6.114322,1.730389,2.165578,6.064012,6.563892,2.042415,-1.991252,-3.639224,7.654304,-6.820095,-7.170850,-1.078614,9.224245,5.471579,-1.551870,-0.812860,-7.111969,-8.498903,8.712245,-4.538516,-3.334726,1.833520,-1.047219,-4.400615,0.609355,-3.772894,8.099293,6.994028,2.795457,4.345742,8.891164,-6.746664,9.630037,-7.563202,-8.113813,-5.443934,-1.809022,0.982551,4.262892,2.168329,-0.837100,-0.796596,-9.520660,-9.284488,-0.601464,7.483889,-2.264119,3.486098,-7.025505,-6.515147,0.643432,6.045376,7.522701,-5.857979,-7.136907,6.673250,-7.042123,7.190727,8.093379,-7.908023,9.451340,-6.759164,9.178448,6.722124,1.664348,-9.372480,-2.346441,-9.435400,-5.430855,-0.686242,-3.684621,-4.708432,6.154076,8.727476,3.317693,-7.254883,5.335065,-8.372085,5.082342,-3.493106,-4.054105,4.333270,-3.740768,-3.497682,-9.191852,-4.405099,-2.238483,0.071780,-1.251468,9.555202,6.435504,-4.158311,-7.784662,6.110393,-5.552706,-2.755314], dtype = "float64")#candidate|8315|(546,)|const|float64
call_8312 = relay.TupleGetItem(func_6610_call(relay.reshape(var_8313.astype('int64'), [390,]), relay.reshape(const_8314.astype('int64'), [11, 88]), relay.reshape(const_8315.astype('float64'), [546,]), ), 1)
call_8316 = relay.TupleGetItem(func_6615_call(relay.reshape(var_8313.astype('int64'), [390,]), relay.reshape(const_8314.astype('int64'), [11, 88]), relay.reshape(const_8315.astype('float64'), [546,]), ), 1)
func_6536_call = mod.get_global_var('func_6536')
func_6538_call = mutated_mod.get_global_var('func_6538')
call_8319 = relay.TupleGetItem(func_6536_call(), 0)
call_8320 = relay.TupleGetItem(func_6538_call(), 0)
func_1484_call = mod.get_global_var('func_1484')
func_1488_call = mutated_mod.get_global_var('func_1488')
const_8325 = relay.const([[5.443061,-7.451458,-6.283655,4.855449,-0.255920,1.842028,1.174961,-8.032260],[0.530392,6.286782,2.925481,-0.088944,9.752860,6.001744,9.781112,-5.358693],[-1.955228,-1.628052,-9.739854,-1.166814,-5.878819,-4.384125,1.297480,6.199410],[4.115738,-0.009519,3.087604,-3.963122,-0.261444,-8.469395,9.755458,-0.882561],[2.390644,6.113513,-1.973687,9.498738,3.064282,-7.472148,-9.626712,5.863777],[-8.084017,-9.535780,-1.196788,-3.975115,-4.044998,8.610943,0.595854,5.406213],[-9.052376,1.041180,-8.405024,5.729538,-6.331141,9.352233,-4.893945,-1.555203],[-6.523497,-0.755399,-1.841541,6.146224,6.179314,-1.914346,-1.975303,9.118577],[-5.650003,-8.677039,9.761561,0.679729,7.107778,-2.969943,4.169427,7.665626],[8.818085,1.510492,-4.492110,7.836233,1.155070,5.137760,3.929995,-1.603910],[4.565798,5.323069,2.787374,-4.078853,8.225687,-7.977271,-5.899532,-2.600743],[7.132625,1.813825,-3.875169,6.594401,-4.698468,3.161640,8.563865,-1.525625],[-3.726263,-4.565180,-0.166119,1.454587,6.931325,-0.087571,3.773176,-0.105956],[-2.665949,-1.370488,-1.140707,-2.275715,-4.330472,-2.732996,-6.000391,-0.011671],[-3.190217,-3.560025,-2.281188,-3.843272,3.869510,4.711944,8.619576,6.111469],[5.663294,-5.440732,1.530821,-7.532637,6.164694,5.716245,7.051151,-2.043114],[-1.255940,-7.618832,-9.801551,4.342787,-0.093844,-5.573881,-7.794378,5.137947],[-5.929244,1.736765,5.640399,0.965297,-7.037113,-4.850953,0.603050,-8.119010],[7.880810,-8.402313,6.698919,3.090605,-8.528308,-9.632570,1.001688,-9.905351],[7.733195,4.151909,6.480654,0.710698,1.189115,-9.646168,5.841847,5.137506],[5.001418,-1.941128,2.252829,-1.322441,-0.922129,-5.901413,0.519439,9.585039],[-0.829537,2.866721,8.057929,2.616005,-3.411818,8.007210,-9.245927,-1.699988],[-7.649342,3.813608,-6.186535,4.381710,-9.135783,-2.798538,-8.983729,-9.865613],[-7.546385,3.997284,0.427562,-3.708196,-0.139916,0.898755,-9.192644,-4.999450],[-8.597080,-2.951301,-1.041810,1.235198,0.616153,-4.154595,1.194648,-0.612667],[-9.987178,-1.871836,6.136681,7.773653,-1.542208,-0.901229,-7.861045,-2.397904],[-4.334611,4.592997,-8.090110,4.942962,-0.726791,-3.569594,4.903880,9.917513],[-4.626066,7.895214,-9.117450,7.163064,2.938968,-2.660584,-0.833048,-5.447237],[2.194905,5.601991,1.597947,-0.004922,-0.009422,2.614968,2.618952,0.687795],[-2.966693,7.632104,4.794626,-0.951746,8.266320,-4.807894,2.644318,-1.480352],[-2.845872,-7.094018,0.870822,5.870348,0.903904,3.715882,1.864372,-2.255611],[5.799926,9.644777,-7.373365,0.595339,-4.960390,-8.149467,-6.420328,-6.783927],[-5.841873,-5.259290,8.012048,-9.613850,0.129111,-9.557287,-0.555645,-9.783190],[-4.268006,7.483254,5.608735,-4.190993,-4.637166,2.645180,-8.035788,-6.173423],[2.261968,-7.061787,-1.884144,7.923855,-7.103199,0.314708,3.621462,-0.231835],[2.680112,-3.866901,-8.310132,-2.369967,9.849821,2.947048,7.994066,0.832496],[0.600465,-5.192762,-2.111183,4.052256,8.118871,7.768163,-1.067892,-1.529910],[1.230079,4.532412,-5.795221,2.805594,0.495870,3.121490,-8.561109,2.951728],[-8.548840,0.056271,-3.905830,9.865400,6.546653,-7.812121,-4.113414,3.041048],[4.314041,3.300131,-5.528353,-4.146180,6.811592,2.460061,-6.698227,0.860598],[-9.971505,5.112256,8.434987,-4.378314,4.879919,8.253310,4.704013,-4.655375],[4.040967,-6.784011,-6.849307,3.521238,-7.897665,6.126053,-0.128654,9.496302],[6.950811,3.853727,1.995566,-0.633997,-6.399913,-4.323313,-1.953637,-5.099521],[-8.892880,-3.149870,1.663606,7.599066,-9.251537,-1.365918,9.583226,6.617594],[-2.782384,-4.541441,-6.773372,6.498196,-4.720900,-3.323090,-4.407927,-0.367165],[-7.030280,4.479780,-2.365017,8.314765,2.048149,5.884348,-5.456113,3.732084],[9.848368,-9.112186,-3.590131,-0.146164,-8.249829,-8.249244,-5.652997,2.170966],[6.179619,-3.333009,8.957096,-6.143543,-8.268661,-2.497985,-4.857182,6.641560],[4.858701,3.709292,2.311461,-0.705263,-3.223929,-9.236780,5.807214,2.578154],[-2.541818,-6.896986,-2.530200,-1.523835,8.418997,9.624473,1.309559,4.943098],[-8.279197,-0.574031,8.234087,9.229563,6.881007,-8.266274,-9.397445,4.789882],[1.299982,-9.106837,-9.071466,-2.258288,1.416329,0.547712,8.220098,4.539832],[2.079073,6.868796,-1.299903,7.161092,6.993447,-7.421027,9.695229,-9.829479],[-8.112050,-1.725601,-3.541599,-1.681314,-5.017073,-8.884489,-4.196193,-9.389308],[5.008257,-1.174596,-6.018201,-5.433947,9.731500,8.503042,-6.725838,-3.565463],[0.004237,-6.773588,8.713172,1.473681,-8.477253,7.228407,-9.578470,1.166860],[-8.586568,4.344706,4.053449,-0.643117,3.035782,6.036652,7.874306,-0.055874],[3.229796,-2.973592,8.770600,-2.128030,4.512944,-8.067481,0.627162,-7.851201],[-2.185710,7.307656,5.501814,-0.294258,5.364384,-0.363514,1.568987,8.544132],[2.207859,-7.397938,-1.237848,5.870604,-9.177214,3.165024,8.342297,0.989991],[6.850926,4.731331,-1.570486,2.441757,1.974123,5.741199,-6.679511,1.608705],[-8.784853,-5.468909,7.898295,6.025103,-1.039323,7.444432,-0.563108,8.365087],[0.898970,-4.782120,-0.695725,-0.235163,3.895372,1.459225,-9.884519,-6.498134],[-3.144050,0.734277,-0.529587,4.187953,3.576081,-0.931396,-2.432386,-0.604560],[-4.986670,1.432158,-4.034121,-4.097479,3.453229,-6.307595,8.017985,6.662303],[2.015609,3.521339,0.560666,-6.365927,4.626662,-3.391732,-2.459452,-2.200498],[7.723235,-6.176726,2.849260,5.149861,-6.711025,-1.917460,-1.174593,5.441634],[7.009610,5.512511,2.169401,5.454927,-7.762558,-0.347481,-5.933742,7.982685],[4.117464,-1.912202,8.726466,8.732782,2.519246,2.141938,4.499702,5.350495],[0.097514,0.548964,3.744202,9.621671,-2.131962,-7.229073,-6.898998,-3.293351],[7.965179,-5.394059,4.184482,-8.211657,-2.240139,-2.803155,-5.977596,-7.937687],[3.214041,4.240458,-4.690012,-3.815919,-7.951958,-9.574111,4.093235,-5.158111],[7.527692,6.853497,3.060115,7.818012,3.403250,8.459407,8.156695,7.182837],[-8.079093,8.198040,5.385776,3.384790,5.013820,9.367863,6.030186,3.072930],[-4.529202,7.455027,8.306664,8.637421,-4.196197,-0.882852,-0.568285,-1.754465],[-7.470517,-5.706752,-2.097411,-5.321200,8.810107,-9.822834,1.139807,3.011942],[-5.607569,8.092062,7.366100,-1.907250,-5.654262,3.407365,-6.264821,4.978010],[-3.837873,-0.785957,8.974298,-7.080371,-2.063686,3.937121,-8.789140,-9.616701],[7.255474,-8.449018,-1.736288,5.473575,-8.233601,-8.301105,-4.522584,5.550244],[6.021105,4.167131,-6.632627,4.009824,-4.359232,4.948338,9.541422,0.998907],[3.493463,3.278673,-5.211119,-1.601035,3.517415,1.775773,-2.185987,-2.197187],[6.560083,3.964886,1.883199,-6.725451,9.648823,0.664578,4.456125,-0.126972],[-4.222777,9.698923,-1.533265,7.671747,-8.797250,8.914429,-5.195834,-9.537245],[-0.978097,5.172146,-2.939309,4.089910,0.143181,-4.551233,-9.525089,-8.194203],[-0.338216,5.917953,1.708785,-2.522658,-8.663886,9.188982,-8.858789,-5.849106],[2.699559,-1.006365,3.816784,8.070876,-4.988993,-8.446252,-3.483111,-5.484960],[-8.709629,8.760482,-3.897387,3.590344,-2.329337,8.595461,-3.016218,6.841441],[-0.799084,8.027458,9.287745,-8.327702,-4.240295,-9.399547,9.962576,5.202061],[5.700272,-3.879573,-9.948266,-8.908760,-1.640532,9.065791,1.335384,-4.424033],[1.920800,6.862980,-4.567319,-7.580850,-0.063407,-2.866288,6.412519,3.995417],[-1.145945,2.772918,7.331174,2.304804,9.050095,-1.950195,0.705097,-3.185417],[-1.661146,-2.044762,-5.180006,9.645775,7.867577,-9.466335,7.189505,7.339126],[0.463949,5.425781,-8.211196,-7.027159,0.865974,-2.702480,9.856061,5.427423],[9.829784,4.057332,2.366331,-0.897634,-4.753251,1.720012,3.104282,0.309280],[0.300790,3.325551,-1.877306,-7.584748,7.564888,-0.367346,0.077322,-1.598837],[8.899210,-8.408707,4.430005,-4.016136,-0.480444,8.411748,-6.703945,-8.762260],[1.176116,-3.742419,-0.447810,-5.215991,0.797903,-4.222016,-9.601783,8.162097],[-4.921807,-9.853356,6.487056,6.561686,3.126375,0.015964,-4.562636,3.711835],[0.295665,8.299864,-6.415206,0.999433,-9.972770,2.258787,6.219816,9.439117],[-5.687564,3.802187,-6.433409,9.791359,9.216352,3.760200,6.014351,-0.018003],[-6.007681,-4.806520,8.307263,2.391732,4.731243,-9.477407,6.242128,4.021276],[-5.070737,3.523671,3.706430,-5.726509,5.700254,-9.918210,-5.242306,-8.034874],[-2.691555,-3.970440,-9.439279,-4.821704,-0.495231,-4.597329,-8.266559,7.332900],[-1.815817,3.390971,-1.718856,6.796066,8.039282,-8.639144,-0.703616,1.781063],[9.954266,-3.777931,3.868769,6.432940,9.197227,0.657079,2.763332,-4.986778],[-3.142297,-7.275236,6.570061,-0.203142,0.714732,0.026068,9.341888,5.970794],[-4.564432,8.991428,-9.066111,9.338190,-1.585444,7.548855,3.638670,-7.841832],[1.341553,-7.155933,-9.196778,7.235210,5.352569,2.873816,5.463504,0.465227],[-7.049530,1.570741,-6.090935,-2.484359,-1.399606,-7.774427,-9.524108,9.879511],[0.139534,-9.456377,-0.027845,-1.992143,-4.637910,6.610943,-1.391250,6.506991],[6.338742,2.691568,3.743561,-1.213636,8.356125,-0.718828,8.833502,1.890255],[2.908802,-3.909575,5.517755,-3.273790,-2.345854,-7.983745,-1.021379,2.271781],[-2.079858,6.343851,7.127959,9.719135,1.746769,-8.331123,5.264917,3.413061],[8.039333,5.000188,-0.670211,0.567198,8.538469,0.590686,0.785072,2.283111],[0.826960,-6.210769,-9.160041,6.557941,6.321354,1.116153,3.505238,4.566863],[-8.656001,-9.500063,-9.235620,-2.800898,5.759927,-5.027213,-9.437135,-7.956519],[-6.078096,-0.847986,7.998463,-5.565283,9.562467,2.779100,0.335971,-2.563271],[4.831622,-6.961142,-1.797524,0.919113,5.765312,-2.405735,7.426223,7.395490],[4.096294,4.285011,-0.841031,4.555722,2.853029,-5.820615,-4.970388,-0.191858],[5.251595,8.454242,4.398806,8.084228,-7.700180,8.985797,7.310589,-0.236106],[-0.209742,3.470489,7.592138,6.530262,3.184337,8.992457,-3.771823,-4.023856],[3.341567,8.270880,-5.161480,9.897402,-5.255816,5.277328,8.643335,3.634273],[5.777562,-8.813463,5.818876,0.240400,-9.762666,-1.676513,-2.059299,-2.922482],[8.273211,7.340402,9.398822,-7.456164,6.264077,3.851293,4.747397,-4.498470],[4.848825,-6.424968,-1.558150,7.481576,-1.934827,4.388940,-3.468704,-0.569038],[9.521979,-8.483215,-7.102136,9.425707,-6.592066,9.182532,6.845760,-3.718209],[-0.678868,4.792439,-5.973491,0.766636,3.822708,1.953346,8.449550,8.339204],[0.519224,0.809424,-9.877613,2.725814,0.660000,1.259616,2.365918,8.790832],[-7.111054,-9.687318,0.249458,3.182965,9.498685,4.631897,4.010185,7.890324],[-8.779659,-1.227405,5.641410,4.232085,-4.256633,7.446507,-2.319998,-3.071474],[-0.551821,2.491617,-2.696685,-2.434772,8.795090,-3.126292,-3.184220,-9.533589],[-5.201235,5.732811,-0.430539,-1.943390,6.088396,-8.722161,-2.069213,-9.806946],[-2.524822,9.540810,5.432356,-1.993406,5.549164,0.820020,-5.983864,-0.217854],[-0.642169,5.124173,-3.271783,-1.173457,0.118175,2.628799,6.011487,-6.574611],[8.445416,-2.477595,6.433058,8.652210,-2.605909,-3.375613,-7.215654,1.219439],[8.700852,-1.997196,7.727860,6.241979,0.782930,-3.294146,2.370410,-4.100112],[-0.987740,9.281781,2.675967,-1.963396,2.046749,1.276334,9.951333,-7.429639],[7.371496,-5.551691,6.089107,7.828454,-3.535270,1.015123,7.199689,-8.646928],[3.690151,4.395679,3.801766,-3.778668,7.680223,-5.639418,-6.603837,7.636385],[2.108142,-2.049047,5.836653,-2.930021,-8.714306,7.262390,4.732625,1.521260],[8.123211,-6.811636,7.775731,9.656583,-1.049058,3.173007,2.149446,-5.247733],[4.112100,1.153939,-6.694381,-2.799097,-9.876343,-5.133021,-6.527093,-4.461052],[4.344592,-6.125495,3.101719,0.819333,1.448210,-6.356903,7.320226,-4.203289],[-7.122428,4.833401,9.348090,2.050096,-0.086660,6.150063,6.100134,-9.144621],[-5.251128,2.138114,4.541139,1.254542,-6.992785,1.601986,-0.679993,-8.307524],[6.138267,-2.854378,5.689297,-0.713931,5.839118,-9.050768,6.693329,7.220775],[9.319238,4.178652,0.722459,-3.905548,7.012003,4.459130,0.941095,-0.188989],[-3.535860,3.220195,-0.563984,1.525089,2.842195,-3.358272,-9.450554,5.744579],[2.436305,-6.994151,8.769837,-9.882842,-7.339810,2.164977,1.127215,3.057703],[-5.361036,0.358666,-2.171786,-9.879359,7.103981,8.794719,7.393508,9.028811],[6.827581,5.643379,-6.869190,9.204226,-7.373051,-1.401310,-6.230715,3.956559],[-5.477522,2.237811,3.751543,2.802202,8.870932,-9.817729,2.408707,7.271855],[-2.137902,4.373890,-2.395487,2.329759,2.117917,-3.031477,7.547262,-4.755754],[-7.782459,1.673926,-7.519443,-9.544667,2.528460,-8.014291,0.151206,1.803419],[-5.196913,-3.604852,-4.274377,2.108531,-7.823467,9.166353,7.683039,4.239407],[-3.805980,3.653250,1.546559,-0.385132,4.923455,3.745194,-5.302238,-3.690238],[-8.029875,4.660176,-6.096947,-6.485929,-5.778253,5.776163,-7.355881,6.406003],[7.260567,5.029803,6.531789,1.683375,-4.873433,1.526124,8.726160,0.644524],[-9.451062,-7.352077,-7.084604,7.476388,4.842487,-5.492769,-1.152280,-5.985669],[2.972045,-3.723934,4.461504,2.760648,6.509456,-6.167265,-1.831110,-8.164239],[-0.119478,7.520520,5.095275,0.407342,6.353813,-4.753157,7.308082,5.820263],[-3.429818,4.998003,6.985758,1.625275,9.561529,-4.241709,-2.953067,1.292080],[7.709385,3.830154,5.000200,3.924125,-7.671297,-8.780719,-2.386617,-8.506650],[-0.883261,-7.955838,-9.192129,-5.871010,7.299799,6.327114,9.466503,-4.488962],[-5.903819,5.939004,-9.780688,-6.751021,0.362834,4.092320,8.324802,-3.834014],[1.825764,2.022105,0.194542,-7.274401,-4.123670,-0.294205,-3.447566,2.795895],[-0.477345,-6.367206,5.194559,2.498124,-5.213961,1.558635,9.816932,2.967390],[-4.547535,-1.122818,-1.660378,7.589893,1.768268,-4.760419,-4.581217,-1.496428],[-5.956392,-0.119196,2.174718,-9.669823,-9.834923,3.224914,-6.316363,-3.368724],[-3.417576,-9.850915,1.023764,4.304891,1.796732,-1.106968,1.338435,-6.803520],[-8.554203,-5.725127,-7.848255,7.980486,-6.846361,-4.171152,7.557019,8.210120],[-7.095654,-6.511130,0.406569,-1.035399,6.791881,6.882567,6.482545,-5.940054],[-3.650732,8.681314,-3.061098,4.564656,-5.250439,1.963929,-9.909812,9.139482],[-8.027665,7.294861,7.216175,-4.739589,-6.904776,-6.778902,1.197519,1.818722],[3.162439,-0.848596,7.725914,-1.804453,-8.711364,7.738637,-7.376546,3.283683],[-3.773441,0.359964,-7.607590,-3.317908,6.621834,-4.493191,-2.160374,-6.843131],[-2.573996,4.404345,-1.037204,6.223135,9.373828,1.769970,4.069690,-9.943937],[8.216621,-4.166911,1.692598,7.963852,0.453693,7.698139,3.132802,5.932735],[-7.160025,-2.428378,-2.024553,7.968530,-2.868834,3.690330,5.960295,-7.786323],[4.612593,-8.602317,3.582406,9.812807,4.754579,-5.188020,-5.046699,0.300598],[-1.285856,2.744556,9.674942,-1.086344,-0.460477,-6.875113,5.313350,-8.491162],[8.277992,1.808528,-4.077526,6.925670,6.125702,9.166696,6.621491,1.528926],[-1.052111,-3.877036,0.927919,4.497064,-4.404247,-2.106565,-4.042180,4.707516],[3.627512,3.317573,0.820259,-0.873411,-4.112119,1.899287,-4.192663,-9.116548],[7.666112,-3.322077,3.782532,-3.817319,6.807364,-9.683162,-3.760837,8.496053],[-3.791672,7.540915,4.553498,1.606804,9.598126,7.430533,1.402779,-9.205830],[-5.767779,4.257801,5.292882,-0.187390,-1.441687,-2.281695,-5.936524,3.733113],[-7.936066,-7.357541,-7.125916,-9.485982,-0.289403,3.064329,6.321684,2.417488],[-9.780980,1.407612,-6.798667,8.947519,-4.176420,9.158433,5.643782,-5.726476],[-8.092685,-3.910716,-9.864950,-8.741494,-3.946023,-7.949000,-9.698196,-1.418833],[-9.094428,-8.992912,4.337178,-2.879810,1.775266,-1.470547,-6.991227,3.776124],[2.014416,8.166611,-9.651402,0.097527,5.332336,-4.756839,6.012832,-4.441261],[-5.971183,-7.140404,-9.465739,-9.031177,8.673854,3.165743,9.982578,-6.125191],[-0.550227,-1.141533,0.069441,4.052307,4.724654,-1.094337,-1.236087,-1.145516],[6.857598,-3.862268,6.702832,-7.978639,9.926952,-3.812024,-9.048236,-5.343607],[-9.019863,1.781737,-7.800592,-7.344567,-2.588161,-7.287377,-5.581331,2.917072],[0.041065,5.514512,-2.943122,6.472633,0.803597,-0.756083,-3.313266,-5.581372],[2.990458,9.181888,6.856589,3.395534,-9.023718,-0.210279,9.017796,1.494585],[-3.887714,9.085482,-8.379655,-8.703049,1.360462,8.003685,6.392951,-3.201627],[3.640575,-2.664143,-5.411070,-4.299898,8.529619,0.654983,-4.023901,-1.069920],[0.154786,-0.163978,-9.718379,-0.785366,2.665615,-3.989783,5.588526,-8.681370],[-7.545493,7.823760,-7.851682,1.019519,5.394799,-8.140507,6.680990,-8.249595],[1.748953,-0.993098,8.705327,4.505855,-4.136463,-9.698307,-4.250601,-9.407096],[4.906169,4.353587,0.057050,-4.339599,0.897320,9.135692,9.052128,-1.851309],[-4.601971,-7.094191,8.961257,-4.412164,8.905287,2.051807,2.738161,-1.076958],[-4.316496,4.354701,9.010461,-3.024948,-9.894857,4.824886,0.849081,-5.724228],[6.008888,4.491344,-7.403758,-8.164241,-2.395051,-8.892589,-4.712928,9.881091],[-9.836773,-5.272041,-1.376625,6.469357,-1.819472,-8.574784,-4.947878,3.687119],[2.096329,-8.583825,7.012369,-4.176037,-3.295054,0.438470,8.883755,7.794913],[6.378142,8.575526,-8.496440,3.453192,-3.962760,-9.878869,-5.749042,-4.894281],[8.538258,-0.569860,7.125980,-1.798694,7.658110,-1.059323,-0.296160,-5.787671],[-6.026907,7.480142,-2.615909,3.387033,-5.195728,3.755852,-6.185841,5.605951],[-6.490081,-2.782568,-1.144598,-3.734237,-9.002350,-8.329126,-8.382149,3.766412],[4.000977,-6.065837,1.036484,-5.853029,8.112817,-6.624691,4.886349,1.668411],[2.005831,6.929775,9.308314,6.836352,3.323375,-4.306949,1.368597,-3.632506],[1.212257,-3.341110,-6.864069,-9.452652,4.411504,7.955597,-6.159129,-2.570996],[-6.041628,1.243168,4.292483,-6.975319,3.038639,4.919789,-9.119313,8.008018],[-6.887508,-0.886505,-2.627039,-2.391038,4.106448,-2.974424,4.550769,-5.804686],[-0.843849,9.061235,-1.349905,-2.245944,-6.595832,-6.128085,2.053569,-7.307890],[-0.345658,1.018717,-5.608848,-8.217713,8.245997,2.751621,2.795149,1.656504],[-0.415428,-2.961023,-6.533198,-6.160492,-4.712471,1.638779,-5.155406,7.807277],[-4.386482,0.076096,-0.360555,-6.120857,-1.414843,-5.459915,9.947113,7.470022],[-0.805421,0.266840,3.186471,-3.971734,-1.883752,0.385551,7.363077,6.916956],[7.959010,-1.926072,-5.141723,-8.536981,0.615080,7.730210,-5.742853,-9.960060],[-9.820841,5.323792,8.838418,6.176075,0.845368,-7.442594,7.044204,-2.516414],[-7.644607,-5.994144,8.863976,2.295554,-8.961525,-9.479814,9.410264,6.963530],[-7.570719,6.241335,-4.062527,3.879891,-6.378624,5.284668,-3.190223,-9.180195],[-1.803878,7.977028,3.188296,-9.120831,9.769010,-0.015096,9.733444,-0.386329],[-2.081917,1.307023,-4.972088,-8.505288,-7.802951,-5.306350,9.644452,9.745332],[-8.721945,-0.482315,5.138090,3.646096,4.445969,-3.280158,8.428467,-1.626635],[-1.556461,9.266577,-0.086970,7.419673,4.351205,7.941732,2.595243,-5.002107],[-0.803827,0.874591,-1.247933,-2.224185,8.659826,-1.230505,-7.660462,-6.617162],[8.434383,5.834977,-7.213160,-5.227398,0.797726,-9.954572,1.908071,-3.164130],[2.118262,9.659974,-2.224877,1.065680,-1.983577,-0.526348,-0.929098,-1.873837],[-1.402724,-5.672455,-3.047854,-3.303087,-4.713694,-5.882684,-8.513492,6.113489],[1.507740,1.011818,7.653084,4.142592,-3.371956,-9.593570,-2.763203,-0.187434],[-3.497574,5.434149,-3.466423,-8.114565,8.946945,-6.392511,4.405682,9.308207],[-0.567265,-9.381738,-4.990994,-6.438944,-7.985773,7.099035,0.417846,1.771761],[-6.063318,-7.312698,2.003538,-7.875108,-4.330615,-9.951221,-8.402336,-3.470168],[-4.647904,-2.742166,-4.392443,2.756685,1.718836,6.671185,1.073635,6.380114],[-6.224354,-8.151478,-3.741016,-7.874780,0.706527,3.412892,-3.284271,-4.592370],[-7.962428,5.044490,9.240923,0.090090,-5.183820,5.589295,-5.959038,0.435834],[0.369835,-4.627885,-4.424174,-5.080060,1.860043,-6.546830,9.661736,-2.134380],[0.870226,-2.015490,-3.861179,-4.651470,-7.979097,-2.694966,-4.256139,0.299099],[2.264127,2.560187,-2.994472,7.473024,3.609367,-8.385727,2.997704,9.378178],[-7.984493,9.064379,1.855633,1.689967,-8.856751,-8.532245,-3.607180,-6.701840],[4.039896,2.512849,6.439289,5.824459,-6.816008,2.217469,-5.769666,8.131218],[-4.214726,-2.623722,-7.395048,3.718450,9.435357,0.348343,-6.079731,-1.919933],[7.376450,4.724859,-0.618376,-3.132057,-1.663728,-7.840590,-8.806879,-1.094935],[3.455304,-4.567714,-1.490743,-2.387283,-4.372041,0.521666,4.936138,-3.830574],[-9.829384,4.877145,5.325164,0.769106,2.158310,-3.596303,0.602174,-4.340672],[1.142548,-6.807902,-0.130240,-2.944417,-8.791712,3.324743,1.645240,0.355524]], dtype = "float64")#candidate|8325|(252, 8)|const|float64
var_8326 = relay.var("var_8326", dtype = "uint16", shape = (4, 220))#candidate|8326|(4, 220)|var|uint16
call_8324 = relay.TupleGetItem(func_1484_call(relay.reshape(const_8325.astype('float64'), [9, 14, 16]), relay.reshape(var_8326.astype('uint16'), [880,]), ), 2)
call_8327 = relay.TupleGetItem(func_1488_call(relay.reshape(const_8325.astype('float64'), [9, 14, 16]), relay.reshape(var_8326.astype('uint16'), [880,]), ), 2)
func_5727_call = mod.get_global_var('func_5727')
func_5728_call = mutated_mod.get_global_var('func_5728')
call_8335 = relay.TupleGetItem(func_5727_call(), 0)
call_8336 = relay.TupleGetItem(func_5728_call(), 0)
func_3087_call = mod.get_global_var('func_3087')
func_3090_call = mutated_mod.get_global_var('func_3090')
const_8345 = relay.const([-3.981496,2.929626,9.659716,-3.062099,-8.137109,-1.735936,-0.837278,7.650826,7.303563,-0.421738,3.780854,-1.302734,0.015285,-3.909626,3.054781,-4.267214,3.914314,-9.746520,9.424237,-7.156583,1.426029,5.710451,-8.613276,-9.609279,8.181742,-8.767742,0.925335,-6.435801,-5.724957,-1.053324,-6.515141,8.849097,-0.380688,-3.688363,6.828379,4.822722,-8.281206,-8.696475,8.403488,-7.102595,5.215259,4.926564,6.160314,2.814512,-3.244642,7.908680,-4.657723,-1.513741,8.627185,-5.424548,-4.927191,9.683769,-6.783693,6.091458,-3.203644,1.213661,-4.356827,3.359045,-2.233586,7.251907,-1.569150,-8.919630,-0.378490,3.827194,5.562476,-5.529284], dtype = "float32")#candidate|8345|(66,)|const|float32
call_8344 = relay.TupleGetItem(func_3087_call(relay.reshape(call_8324.astype('float32'), []), relay.reshape(const_8345.astype('float32'), [11, 6, 1]), ), 0)
call_8346 = relay.TupleGetItem(func_3090_call(relay.reshape(call_8324.astype('float32'), []), relay.reshape(const_8345.astype('float32'), [11, 6, 1]), ), 0)
func_308_call = mod.get_global_var('func_308')
func_311_call = mutated_mod.get_global_var('func_311')
call_8353 = relay.TupleGetItem(func_308_call(relay.reshape(call_8324.astype('uint64'), [])), 0)
call_8354 = relay.TupleGetItem(func_311_call(relay.reshape(call_8324.astype('uint64'), [])), 0)
bop_8357 = relay.floor_mod(var_8313.astype('float32'), call_8353.astype('float32')) # shape=(1, 11, 390)
bop_8360 = relay.floor_mod(var_8313.astype('float32'), call_8354.astype('float32')) # shape=(1, 11, 390)
func_6678_call = mod.get_global_var('func_6678')
func_6680_call = mutated_mod.get_global_var('func_6680')
call_8366 = relay.TupleGetItem(func_6678_call(), 0)
call_8367 = relay.TupleGetItem(func_6680_call(), 0)
func_7549_call = mod.get_global_var('func_7549')
func_7553_call = mutated_mod.get_global_var('func_7553')
const_8374 = relay.const([4.094912,-1.874418,-9.000286,6.179454,4.995029,-6.122396,-8.602758,4.613679,-8.666452,6.905687,8.536685,7.172995,-2.688150,4.133575,-7.540537,-3.479579,-7.978001,-1.091040,4.108925,1.364656,3.492887,-3.939769,6.847945,2.367952,8.708789,-7.958496,-9.416508,-6.861332,5.120479,4.718703,-0.010835,7.780295,-1.225968,-7.093663,5.688810,-1.450549,6.617846,0.740668,-6.586221,-3.599553,1.033968,-9.346619,0.357775,-5.966429,2.574233,-4.084567,2.076179,-4.059421,9.611614,2.956859,6.125714,4.189655,-4.091843,3.913088,-9.457743,-6.218423,-3.546448,6.591798,8.792606,-0.693838,3.277240,4.418336,-4.112573,-3.700216,-6.878263,-7.261266,-5.933406,-4.551076,-3.963304,3.382163,6.240103,-6.192068,9.735877,1.153683,2.584349,9.165435,2.021775,9.470376,-7.388138,5.073539,-9.387456,-4.080854,-1.301177,1.404304,-5.252983,0.383363,0.876112,3.626416,1.696320,1.810541,-4.144883,-5.758648,4.479348,9.991853,1.895746,-9.368274,2.606265,-2.474196,0.345799,-4.690208,9.951240,-1.499811,-5.170558,5.276002,-8.728827,-2.024371,9.141852,-5.527161,4.633991,-5.011408,3.480740,-3.843524,-3.447176,-4.416614,-0.983143,3.352809,-5.075003,-5.958054,-6.026749,-2.589534,4.477832,6.693805,5.123944,0.483396,-0.008474,-4.919883,9.941438,-3.567385,1.336319,4.410193,8.951880,4.560956,-7.445069,-0.204782,3.230823], dtype = "float64")#candidate|8374|(135,)|const|float64
call_8373 = relay.TupleGetItem(func_7549_call(relay.reshape(const_8374.astype('float64'), [9, 3, 5]), relay.reshape(call_8324.astype('uint64'), []), ), 2)
call_8375 = relay.TupleGetItem(func_7553_call(relay.reshape(const_8374.astype('float64'), [9, 3, 5]), relay.reshape(call_8324.astype('uint64'), []), ), 2)
output = relay.Tuple([call_8310,call_8312,const_8314,const_8315,call_8319,call_8324,const_8325,var_8326,call_8335,call_8344,const_8345,bop_8357,call_8366,call_8373,const_8374,])
output2 = relay.Tuple([call_8311,call_8316,const_8314,const_8315,call_8320,call_8327,const_8325,var_8326,call_8336,call_8346,const_8345,bop_8360,call_8367,call_8375,const_8374,])
func_8379 = relay.Function([var_8313,var_8326,], output)
mod['func_8379'] = func_8379
mod = relay.transform.InferType()(mod)
mutated_mod['func_8379'] = func_8379
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8379_call = mutated_mod.get_global_var('func_8379')
var_8381 = relay.var("var_8381", dtype = "int64", shape = (390,))#candidate|8381|(390,)|var|int64
var_8382 = relay.var("var_8382", dtype = "uint16", shape = (4, 220))#candidate|8382|(4, 220)|var|uint16
call_8380 = func_8379_call(var_8381,var_8382,)
output = call_8380
func_8383 = relay.Function([var_8381,var_8382,], output)
mutated_mod['func_8383'] = func_8383
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7844_call = mod.get_global_var('func_7844')
func_7846_call = mutated_mod.get_global_var('func_7846')
call_8389 = func_7844_call()
call_8390 = func_7844_call()
var_8395 = relay.var("var_8395", dtype = "float64", shape = (15, 9, 6))#candidate|8395|(15, 9, 6)|var|float64
bop_8396 = relay.maximum(call_8389.astype('float32'), relay.reshape(var_8395.astype('float32'), relay.shape_of(call_8389))) # shape=(15, 9, 6)
bop_8399 = relay.maximum(call_8390.astype('float32'), relay.reshape(var_8395.astype('float32'), relay.shape_of(call_8390))) # shape=(15, 9, 6)
output = relay.Tuple([bop_8396,])
output2 = relay.Tuple([bop_8399,])
func_8402 = relay.Function([var_8395,], output)
mod['func_8402'] = func_8402
mod = relay.transform.InferType()(mod)
mutated_mod['func_8402'] = func_8402
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8403 = relay.var("var_8403", dtype = "float64", shape = (15, 9, 6))#candidate|8403|(15, 9, 6)|var|float64
func_8402_call = mutated_mod.get_global_var('func_8402')
call_8404 = func_8402_call(var_8403)
output = call_8404
func_8405 = relay.Function([var_8403], output)
mutated_mod['func_8405'] = func_8405
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7639_call = mod.get_global_var('func_7639')
func_7641_call = mutated_mod.get_global_var('func_7641')
call_8420 = relay.TupleGetItem(func_7639_call(), 7)
call_8421 = relay.TupleGetItem(func_7641_call(), 7)
output = relay.Tuple([call_8420,])
output2 = relay.Tuple([call_8421,])
func_8448 = relay.Function([], output)
mod['func_8448'] = func_8448
mod = relay.transform.InferType()(mod)
output = func_8448()
func_8449 = relay.Function([], output)
mutated_mod['func_8449'] = func_8449
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8529 = relay.var("var_8529", dtype = "float64", shape = (10, 10, 12))#candidate|8529|(10, 10, 12)|var|float64
uop_8530 = relay.asin(var_8529.astype('float64')) # shape=(10, 10, 12)
func_1879_call = mod.get_global_var('func_1879')
func_1884_call = mutated_mod.get_global_var('func_1884')
const_8537 = relay.const([-6,-2,-8,10,-1,-7,-2,-2,1,-8,-3,10,5,-7,7,7,5,-6,2,-4,-9,-5,2,-3,-9,1,-5,-8,-10,7,2,-3,-5,-9,4,-10,-6,5,-6,-2,-1,-7,-3,7,1,-1,9,-10,-2,3,-4,-1,10,2,-6,1,7,-2,-4,-4,-2,-5,-10,5,-4,9,1,-2,-8,9,7,1,-7,-4,1,-5,4,4,-5,-7,-7,-10,-8,1,9,2,-9,9,4,-8,-3,8,3,3,-10,10,7,-8,-4,-3,-9,8,5,-6,3,6,7,5,-5,-9,-1,4,10,-2,-1,7,7,-9,-3,3,-9,5,-2,-7,1,4,6,9,-8,-10,6,-10,-1,7,-4,-3,1,8,-8,-2,2,10,-2,3,10,10,1,8,8,7], dtype = "uint64")#candidate|8537|(150,)|const|uint64
var_8538 = relay.var("var_8538", dtype = "int64", shape = (364,))#candidate|8538|(364,)|var|int64
var_8539 = relay.var("var_8539", dtype = "bool", shape = (715,))#candidate|8539|(715,)|var|bool
call_8536 = relay.TupleGetItem(func_1879_call(relay.reshape(const_8537.astype('uint64'), [5, 5, 6]), relay.reshape(var_8538.astype('int64'), [182, 2]), relay.reshape(var_8538.astype('int64'), [4, 13, 7]), relay.reshape(var_8539.astype('bool'), [715,]), ), 1)
call_8540 = relay.TupleGetItem(func_1884_call(relay.reshape(const_8537.astype('uint64'), [5, 5, 6]), relay.reshape(var_8538.astype('int64'), [182, 2]), relay.reshape(var_8538.astype('int64'), [4, 13, 7]), relay.reshape(var_8539.astype('bool'), [715,]), ), 1)
output = relay.Tuple([uop_8530,call_8536,const_8537,var_8538,var_8539,])
output2 = relay.Tuple([uop_8530,call_8540,const_8537,var_8538,var_8539,])
func_8542 = relay.Function([var_8529,var_8538,var_8539,], output)
mod['func_8542'] = func_8542
mod = relay.transform.InferType()(mod)
var_8543 = relay.var("var_8543", dtype = "float64", shape = (10, 10, 12))#candidate|8543|(10, 10, 12)|var|float64
var_8544 = relay.var("var_8544", dtype = "int64", shape = (364,))#candidate|8544|(364,)|var|int64
var_8545 = relay.var("var_8545", dtype = "bool", shape = (715,))#candidate|8545|(715,)|var|bool
output = func_8542(var_8543,var_8544,var_8545,)
func_8546 = relay.Function([var_8543,var_8544,var_8545,], output)
mutated_mod['func_8546'] = func_8546
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5717_call = mod.get_global_var('func_5717')
func_5718_call = mutated_mod.get_global_var('func_5718')
call_8548 = relay.TupleGetItem(func_5717_call(), 0)
call_8549 = relay.TupleGetItem(func_5718_call(), 0)
func_3087_call = mod.get_global_var('func_3087')
func_3090_call = mutated_mod.get_global_var('func_3090')
var_8554 = relay.var("var_8554", dtype = "float32", shape = ())#candidate|8554|()|var|float32
const_8555 = relay.const([[-6.727569,-4.633841,-3.655581,-7.369755,-7.982997,-9.332621],[1.376758,-9.351213,-0.678819,-6.575157,5.078291,7.566955],[6.544022,2.703433,-2.519891,2.645917,9.690330,4.789451],[7.986889,-5.676980,-5.306077,-5.726438,4.819802,9.346789],[3.249834,-5.734541,-8.415484,7.233266,-5.266210,2.674388],[-5.530769,-8.164761,-5.311070,2.922279,3.820837,-1.482115],[-5.013484,2.964888,1.945130,-3.558763,-9.455481,3.206980],[-9.511075,-6.480658,4.290602,6.697720,9.114136,1.878220],[3.710389,6.659397,7.933892,-5.919753,-5.692136,2.493410],[-3.838591,6.754380,7.551272,6.325927,2.596042,-6.404675],[2.008546,-7.424892,1.033745,-1.910818,-8.383614,2.217336]], dtype = "float32")#candidate|8555|(11, 6)|const|float32
call_8553 = relay.TupleGetItem(func_3087_call(relay.reshape(var_8554.astype('float32'), []), relay.reshape(const_8555.astype('float32'), [11, 6, 1]), ), 0)
call_8556 = relay.TupleGetItem(func_3090_call(relay.reshape(var_8554.astype('float32'), []), relay.reshape(const_8555.astype('float32'), [11, 6, 1]), ), 0)
func_6319_call = mod.get_global_var('func_6319')
func_6321_call = mutated_mod.get_global_var('func_6321')
call_8557 = relay.TupleGetItem(func_6319_call(), 2)
call_8558 = relay.TupleGetItem(func_6321_call(), 2)
output = relay.Tuple([call_8548,call_8553,var_8554,const_8555,call_8557,])
output2 = relay.Tuple([call_8549,call_8556,var_8554,const_8555,call_8558,])
func_8563 = relay.Function([var_8554,], output)
mod['func_8563'] = func_8563
mod = relay.transform.InferType()(mod)
var_8564 = relay.var("var_8564", dtype = "float32", shape = ())#candidate|8564|()|var|float32
output = func_8563(var_8564)
func_8565 = relay.Function([var_8564], output)
mutated_mod['func_8565'] = func_8565
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6812_call = mod.get_global_var('func_6812')
func_6814_call = mutated_mod.get_global_var('func_6814')
call_8574 = func_6812_call()
call_8575 = func_6812_call()
output = call_8574
output2 = call_8575
func_8581 = relay.Function([], output)
mod['func_8581'] = func_8581
mod = relay.transform.InferType()(mod)
output = func_8581()
func_8582 = relay.Function([], output)
mutated_mod['func_8582'] = func_8582
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6812_call = mod.get_global_var('func_6812')
func_6814_call = mutated_mod.get_global_var('func_6814')
call_8596 = func_6812_call()
call_8597 = func_6812_call()
output = relay.Tuple([call_8596,])
output2 = relay.Tuple([call_8597,])
func_8600 = relay.Function([], output)
mod['func_8600'] = func_8600
mod = relay.transform.InferType()(mod)
output = func_8600()
func_8601 = relay.Function([], output)
mutated_mod['func_8601'] = func_8601
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6319_call = mod.get_global_var('func_6319')
func_6321_call = mutated_mod.get_global_var('func_6321')
call_8610 = relay.TupleGetItem(func_6319_call(), 0)
call_8611 = relay.TupleGetItem(func_6321_call(), 0)
func_7376_call = mod.get_global_var('func_7376')
func_7378_call = mutated_mod.get_global_var('func_7378')
call_8615 = relay.TupleGetItem(func_7376_call(), 0)
call_8616 = relay.TupleGetItem(func_7378_call(), 0)
output = relay.Tuple([call_8610,call_8615,])
output2 = relay.Tuple([call_8611,call_8616,])
func_8619 = relay.Function([], output)
mod['func_8619'] = func_8619
mod = relay.transform.InferType()(mod)
output = func_8619()
func_8620 = relay.Function([], output)
mutated_mod['func_8620'] = func_8620
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6678_call = mod.get_global_var('func_6678')
func_6680_call = mutated_mod.get_global_var('func_6680')
call_8629 = relay.TupleGetItem(func_6678_call(), 0)
call_8630 = relay.TupleGetItem(func_6680_call(), 0)
output = relay.Tuple([call_8629,])
output2 = relay.Tuple([call_8630,])
func_8633 = relay.Function([], output)
mod['func_8633'] = func_8633
mod = relay.transform.InferType()(mod)
output = func_8633()
func_8634 = relay.Function([], output)
mutated_mod['func_8634'] = func_8634
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7376_call = mod.get_global_var('func_7376')
func_7378_call = mutated_mod.get_global_var('func_7378')
call_8651 = relay.TupleGetItem(func_7376_call(), 0)
call_8652 = relay.TupleGetItem(func_7378_call(), 0)
output = relay.Tuple([call_8651,])
output2 = relay.Tuple([call_8652,])
func_8670 = relay.Function([], output)
mod['func_8670'] = func_8670
mod = relay.transform.InferType()(mod)
output = func_8670()
func_8671 = relay.Function([], output)
mutated_mod['func_8671'] = func_8671
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5674_call = mod.get_global_var('func_5674')
func_5676_call = mutated_mod.get_global_var('func_5676')
call_8692 = func_5674_call()
call_8693 = func_5674_call()
func_3623_call = mod.get_global_var('func_3623')
func_3625_call = mutated_mod.get_global_var('func_3625')
var_8699 = relay.var("var_8699", dtype = "float64", shape = (1, 546))#candidate|8699|(1, 546)|var|float64
call_8698 = func_3623_call(relay.reshape(var_8699.astype('float64'), [13, 14, 3]))
call_8700 = func_3623_call(relay.reshape(var_8699.astype('float64'), [13, 14, 3]))
func_8113_call = mod.get_global_var('func_8113')
func_8115_call = mutated_mod.get_global_var('func_8115')
const_8712 = relay.const([9.466573,4.671132,-1.784512,-4.380206,7.368991,5.474092,-1.720787,8.818140,9.649557,-9.168988,2.932177,-6.436524,4.367234,3.729473,-1.540794,-8.611680,-2.049787,1.791980,-3.098864,-1.430846,-6.479300,6.211509,-0.678569,-9.054948,8.874214,8.724373,-3.284547,8.059077,-6.244652,0.772996,5.440074,4.826625,6.247023,-5.892414,-4.885151,5.356297,7.678893,3.166465,1.045853,1.600813,-1.398133,-1.760779,-1.492903,-1.622249,-1.500890,3.412674,6.583886,-7.345285,8.540423,-5.219591,7.732048,-1.331461,-2.600313,-8.856456,-7.200462,-6.334929,-6.605504,3.498671,-9.677816,-4.772768,3.876920,-0.547053,-7.757168,1.763855,-3.398408,8.746537,-8.459708,-3.077368,8.072051,-6.408491,-6.271670,-6.275407,7.405438,6.459483,0.898985,0.453027,-7.346471,8.800230,-0.560473,-5.033810,-4.766368,-0.254801,-7.785173,0.722787,-5.061201,7.118440,7.345760,3.224008,3.995797,-5.245115,-1.700009,-5.858813,-9.072213,5.992853,-5.432103,1.829463,2.274614,9.950873,-2.551321,8.490885,0.206234,8.718921,-3.672462,7.980548,6.658490,-7.491641,2.408173,-5.833786,-0.412336,-1.583162,-9.096927,0.044377,-6.236451,2.193361,-9.730925,5.077593,9.227253,-6.222466,9.721567,0.868489,6.255603,5.417648,-4.907466,-7.055871,3.324031,-7.707591,-7.228353,-9.318564,-8.354286,5.538379,-2.877778,-0.849510,7.941894,-5.780874,2.695753,-1.344152,8.196582,0.124740,4.931166,4.511764,3.171981,-8.821584,2.480107,-6.859257,-2.667419,-4.319112,-1.347141,-3.564395,8.395266,-2.654486,5.296449,-3.593459,-1.682176,-4.213381,6.657774,9.732033,9.496954,6.973456,-9.967780,5.803483,7.887951,6.888125,-7.497753,-2.427071,-9.040489,-4.245714,3.848421,7.256359,6.439044,9.922457,7.996348,6.065984,2.215595,2.207862,-3.747049,-6.602661,4.470758,1.838577,-0.683266,1.010859,-7.533414,-0.607689,-3.694732,-2.363105,1.966158,6.901335,-9.124383,-7.307228,4.672450,7.761271,-9.236731,5.653520,2.851443,5.636257,-5.476902,7.544646,9.083704,-0.098704,5.163401,1.234095,9.973706,7.292627,2.925066,8.473430,1.493154,-9.919103,-0.214582,0.180946,-5.153409,8.343968,-6.707310,3.199945,-1.775871,8.876272,-0.736769,3.380125,1.672263,8.920304,-2.415680,0.745973,9.896150,3.601247,-0.322304,-2.562175,7.204436,4.376169,-2.095134,0.193192,2.410069,-7.248494,4.162277,1.212281,-2.869837,5.438057,5.053582,-6.977706,-2.145343,-7.580161,7.027853,7.444919,6.066759,-9.960756,-8.645867,-1.801429,-9.143317,8.813230,-0.181843,3.214373,-8.693315,8.526223,3.015053,-1.443430,4.304443,-9.089182,6.546719,-6.365971,2.675351,-4.290426,-0.088195,6.223572,3.565775,0.042488,9.354516,-5.450125,0.693223,0.040970,-4.030688,2.858905,-5.227285,-0.874070,8.914835,-4.413035,5.763567,-8.058815,-0.674759,-2.524763,7.596466,7.350721,-3.054855,-5.644388,-0.029915,5.151270,9.471011,-0.221985,-4.906028,-7.810165,7.108019,-4.269888,0.665831,0.406590,-2.473348,-1.230164,3.111815,-5.433987,1.457654,9.788033,-6.274221,-0.850395,4.349925,-0.971591,8.154138,-4.671895,0.588247,8.322095,0.803118,-6.965034,9.133459,9.941662,6.943795,-6.387859,-1.987430,-9.880770,-9.493126,0.894097,8.123384,-1.432600,-5.290117,-8.909384,0.996761,-5.847443,-2.061168,0.378381,0.200899,-4.666829,-2.823656,-4.107825,-5.107560,-8.319070,4.481200,7.048426,0.676907,-3.808651,-3.552921,6.618533,-3.984036,-3.247336,7.345147,-3.010115,5.593318,6.308298,-1.520403,-9.926618,-8.674619,9.826701,-6.723059,-2.969933,-5.305040,8.192226,2.141945,6.545857,7.338615,-8.196224,5.479568,3.671253,5.606204,-2.104272,-6.738952,7.157151,2.212234,5.118657,3.119265,9.724708,-7.606676,-0.383448,-1.077455,1.195563,4.406840,-5.743265,7.281071,3.658222,-5.518974,-3.742944,4.630708,5.375740,-9.723230,-7.147887,-7.056394,-2.495168,5.453107,7.105849,-0.835658,2.190939,-7.658234,-0.852492,3.085798,1.697001,5.624695,7.579168,5.590180,-5.623024,7.268130,4.117653,-5.137126,-1.461329,-0.935343,9.718947,-9.649159,-7.200627,-0.008178,-2.630636,7.476146,0.100486,4.232951,1.956730,0.416246,6.457188,-2.263468,2.990345,-5.210302,-6.910003,6.168795,7.236251,-7.800690,-5.548567,-0.693615,9.232462,-7.511520,-6.064423,9.171540,-4.978725,1.314264,1.206108,-0.523993,1.477054,-3.108196,1.294234,6.304557,5.066040,6.728209,0.567367,6.895687,3.393034,9.856163,4.395130,8.167862,-0.748367,9.559352,-5.473727,-3.660323,-2.022611,-0.621103,-7.113442,-4.847220,5.531520,0.301364,3.006325,5.341783,4.827128,4.885356,0.156037,-6.904656,5.827175,5.298297,-4.258653,9.063788,-6.879759,-5.176191,-5.797749,6.224622,-0.166479,-7.061166,2.849792,-2.839867,-1.169434,6.074887,-0.847326,7.802519,-2.762146,-6.643624,-2.943654,8.792124,2.831495,9.901248,0.412429,9.962989,-2.216806,1.222450,-6.598104,-1.963981,8.693604,-3.788308,0.290935,-3.744680,3.496761,-0.518457,-3.275712,-8.061642,-2.856743,2.080325,-4.581486,0.099525,-9.345062,-3.402465,2.001561,-3.733605,0.298782,-4.286548,-3.690224,-1.295488,6.046547,-0.489000,-6.297423,8.754257,-4.317998,-8.163617,-3.577382,3.758216,5.271620,3.099035,-0.898459,6.102298,-7.860861,1.359160,-6.783815,-0.198073,-2.175253,-1.593674,-0.295121,2.590216,-7.665046,9.223964,-7.768462,-3.447034,2.456074,-8.170269,1.980049,2.204596,3.411275,-2.518826,-9.363694,-3.947734,3.667245,9.010087,-7.285275,6.043640,4.037455,3.850562,7.651952,3.584814,3.879543,3.809017,8.480918,1.761415,6.590523,4.477238,-7.972133,-1.212446,-2.622657,8.544011,0.869220,5.730785,-7.614962,-1.816570,-2.970446,-1.880777,5.050081,-0.643804,-0.274884,5.131282,-3.382259,5.258454,-1.187985,-1.864238,8.666991,-0.936278,-1.782872,4.388031,-0.281846,0.965899,3.117743,5.362224,3.917263,-1.082793,2.666032,4.127649,-1.814449,-9.203138,-0.178042,2.911395,7.991849,-4.535761,5.792844,-2.497708,8.386890,7.940888,2.528040,2.717515,-8.273583,-0.137618,-6.437938,9.299873,-4.290073,9.784421,3.300355,-7.657683,-9.817660,-5.610348,3.963915,-6.382377,-7.983607,5.319816,-9.553913,-4.612928,-9.313692,-6.983131,-6.917132,2.287870,1.082584,-3.989315,3.504632,2.285504,2.338259,-8.636396,-9.276090,-2.134539,-7.721896,-2.685287,-5.846636,5.869166,0.477867,2.583664,-9.567685,-0.867522,-8.754162,-9.087395,-5.906568,9.752816,8.017243,-1.132190,-1.680669,3.461456,-7.669047,7.649823,-7.251006,-8.634606,-9.180186,-6.902140,-9.208009,9.911619,2.395307,5.276814,6.710819,2.728770,-6.536389,9.467098,-8.462485,3.300419,-5.680783,-3.199984,9.004184,8.301281,-9.767774,-9.179629,-3.235618,3.197421,2.464522,0.185777,-5.999023,-5.836352,-1.438579,5.225854,-7.490502,-8.456153,-1.940655,0.202560,7.133385,6.787828,-6.904433,-0.391001,3.313047,-6.546423,-8.109687,-8.269448,0.448748,1.400041,-9.692841,-1.289192,7.631359,4.715270,4.834992,-0.136218,3.702713,4.164041,0.587301,3.444651,9.160957,-3.085247,3.789116,-9.384674,7.635091,5.612365,8.625123,-3.087842,-4.715845,-9.870517,-9.161406,-5.489443,-4.356101,-8.043121,3.653081,3.510996,9.883105,8.894106,-7.299132,0.227302,2.220344,3.186231,2.586518,-2.596106,2.877655,2.568854,9.362576,-8.324570,5.985907,3.457864,-7.440666,-3.687443,-4.525132,-2.358256,4.757305,-8.499803,-7.014196,3.317480,1.827275,2.979351,-3.744514,9.048327,-3.091196,-3.472441,-4.342016,9.298379,-5.798324,-4.578342,4.896408,7.439294,5.874317,9.631991,9.583233,2.937899,-7.148411,4.801106,5.202980,-7.196676,-3.423463,-8.647850,8.974572,9.485129,1.485378,-5.815435,9.967833,5.648875,-4.531079,-5.883732,-0.131803,-7.322416,0.933573,8.724201,-7.341034,-2.084475,-9.025186,7.315704,-9.613356,7.648336,4.006716,-5.259973,8.856359,7.438434,0.834553,8.034177,6.083607,-6.235938,-1.082292,9.789325,-9.401891,8.744335,-2.986422,-2.020222,-4.704053,-3.278542,7.591480,-4.601400,0.526573,-5.162812,5.983373,-7.526559,-4.092920,4.364261,-2.033789,6.529416,3.990658,-9.871562,-5.028907,-9.747587,-9.048495,-2.954006,-4.988147,6.277180,-7.306728,-7.947682,8.155569,-4.050239,3.730413,-5.895670,-5.120908,-7.362072,2.398313,-7.766367,4.615722,-4.736780,9.584776,-7.523660,0.519158,9.368149,0.289292,3.897302,-7.591288,-3.370873,-0.038875,-0.284456,1.940134,-8.259297,2.283450,-6.123932,1.032298,-4.135090,8.855500,-2.286766,-8.979642,-2.326143,3.171148,2.340945,1.710943,-1.451233,-8.399941,-9.360997,7.457962,-7.427383,7.814614,-8.316574,9.080491,-9.331681,3.421086,7.063169,-8.332798,7.355546,-6.382734,-0.736896,1.184610,2.611462,7.856399,9.449443,-9.117455,7.339099,-0.063194,-9.014484,-6.338641,-6.872716,-9.122425,-5.883839,9.273973,-5.789115,-6.693993,8.559284,8.755488,7.922557,-4.142311,-1.424214,5.912248,2.276759,9.847753,7.927032,-5.738962,1.519621,-1.723930,7.217525,2.475161,4.518101,-4.622337,1.240755,0.175477,-7.930028,3.441479,-5.463234,-1.512152,-7.189879,6.324682,-7.595270,1.066248,-0.586630,0.280933,1.825294,-2.839856,-4.008257,7.677634,-5.093652,-8.648327,2.927455,6.287592,-2.873585,6.715242,4.222579,6.223232,-1.850050,3.156486,-1.379700,-1.580875,-6.832017,-8.984941,-2.425079,-1.669155,-6.034522,1.245659,4.927810,0.149485,9.177085,-6.130051,2.017705,-2.613068,9.665776,4.789055,-7.836949,0.743299,-2.658290,8.621697,-8.418847,6.170663,-0.726111,-8.074395,-1.750494,-1.283878,-8.054925,-5.820555,-9.966457,7.849163,3.326565,5.035413,-1.430762,-6.144676,-7.263685,2.356327,9.875156,6.702496,-7.808189,3.003574,8.560169,-4.788489,8.864423,4.818195,4.666624,2.240018,1.679144,-3.311675,1.864171,-8.154889,-9.254712,-3.267000,1.232210,8.704317,6.412426,-4.264379,-6.517262,-1.572417,5.656604,0.058123,-0.262921,2.226860,3.005456,-3.296706,-3.952863,-6.939569,-7.852950,2.948052,-0.046374,0.693908,6.536432,-6.599952,-5.250580,8.278128,7.026615,-7.156628,6.740371,5.700836,6.705887,-1.935979,9.415699,-4.962246,4.586607,7.998597,8.922919,-7.083708,-9.948859,-9.202207,2.856688,-9.372250,1.362056,9.252060,4.516827,9.148417,-0.514258,-9.270495,5.173746,4.797652,-6.890651,-0.409255,-3.299032,9.437667,-6.904384,5.738788,7.507407,-4.893241,7.052015,-4.735967,-8.696014,1.084973,6.338469,-4.734650,0.839433,1.076340,-7.377859,0.516594,-8.658009,9.002496,-7.240799,7.158157,5.307635,-6.963397,5.469633,1.828631,3.735579,-1.376676,-4.841469,3.572934,-1.807876,-9.042124,-0.681925,3.282581,-6.247278,3.454192,-0.848920,-3.280401,-8.540652,-6.087922,9.048428,-9.115252,-1.539836,8.079741,0.106415,-4.265604,-8.643981,3.270662,-7.083850,1.507197,5.578306,-6.678563,2.134616,9.870780,0.124171,9.776308,9.374294,2.069486,-7.712117,7.387007,9.563601,-4.982978,-4.141798,5.788949,-8.043995,7.185652,2.659659,0.255141,-1.473706,9.638372,-0.532178,9.637762,-4.808984,-7.129312,1.000894,-9.610503,7.399341,-7.984108,-8.152106,6.355623,9.547101,0.813231,-1.954482,8.174723,4.149022,-4.732680,-9.796595,-5.058870,2.445635,9.586494,-2.513237,6.492322,-0.793772,9.181690,1.105062,-1.614690,5.783357,-4.925766,-1.122032,-2.805001,-9.319824,-2.794235,-6.999857,1.494307,4.033308,3.266359,-2.203429,7.997993,-7.948502,-5.648332,8.912419,-3.740569,-8.475463,-8.388251,5.846831,-8.095396,-7.977416,-4.614025,3.225633,-7.537563,-4.284543,-5.260503,-6.044214,-0.702862,-0.840407,8.717098,4.845728,-4.405125,-6.526319,-6.060012,-7.597739,4.151980,1.838189,9.510954,4.056315,8.255456,8.245439,-7.014102,-5.776217,2.017582,1.708908,-1.700370,-4.336744,-6.740191,-4.404171,-5.443466,-5.425153,8.440519,6.839015,-3.015121,-6.668806,8.353899,-1.995885,1.745389,-3.035441,1.125408,1.177603,-4.701383,9.479155,-0.075933,1.705663,-1.136270,-5.454227,-1.039458,-0.430501,-0.567674,-4.318291,8.320090,-7.356410,2.563253,3.139637,-1.011344,8.809408,-6.894798,-7.207071,-7.085010,-2.034427,8.063109,-8.154463,-6.219959,-6.179870,9.825932,-0.529078,7.485979,5.584739,4.712181,-6.964762,-9.185850,-6.311529,-4.569194,3.755084,4.809583,7.529433,7.757237,-7.806105,-5.794842,-0.021097,9.390122,-1.709624,3.825334,-4.992815,-0.772642,5.284234,-6.228115,-3.625646,-8.539603,4.671337,3.411802,-3.712479,-9.183892,-0.429548,4.277478,-2.176256,-2.368532,-3.448257,-6.975839,-6.998654,3.247961,5.264273,-6.152372,-8.559445,-9.763862,-0.363924,-6.447886,-5.486405,9.719569,2.902632,1.986431,4.178958,2.832094,-4.257432,-3.785529,-7.810852,-3.704309,1.379414,3.285359,0.856295,5.954981,5.901596,-4.459982,-3.582141,4.402613,-0.816578,8.841473,-1.217459,1.419052,2.492261,5.206457,8.002739,5.139957,-4.243966,-4.282248,-8.799480,8.407362,1.639716,3.768663,1.841375,-3.604731,-9.982598,-9.445421,-0.661735,1.796046,8.607923,3.776330,-2.994809,-9.949365,-0.248410,-4.493489,-8.141151,-9.013694,7.907509,-3.400710,-7.684487,-6.997522,-3.814284,9.074199,0.419124,-2.553727,-6.552609,1.444328,2.057393,0.739246,9.918998,-4.827289,-5.465604,3.521753,6.216236,-2.129228,-0.727040,-0.828921,2.351220,9.026935,-0.842271,-9.302726,-7.027018,0.972524,3.757451,4.000846,-1.523813,-5.322111,-4.390278,-3.610579,5.570175,-3.949038,4.120415,2.496446,-6.406714,4.685009,-4.408379,4.647117,-2.635200,-2.263072,-6.719640,-8.658358,-1.034160,8.267931,-3.340828,-2.747117,-6.235230,-6.006456,6.487602,6.780204,-9.657913,-9.472465,-3.201975,4.861628,-0.821975,-4.728397,5.079522,6.444428,0.593673,4.045707,-4.586769,-6.415091,-1.262802,-6.166391,-5.885066,0.516810,7.356084,8.165064,-3.140487,-0.238457,4.576008,9.207920,3.931411,-8.467711,9.457025,-2.667418,0.429447,-4.284976,5.539299,4.576721,-7.752866,7.927449,-3.325147,1.501953,2.794725,2.728158,-2.867543,-0.488036,7.416236,7.854515,-8.904646,-2.212558,-2.605853,0.874305,6.780657,9.094356,5.688938,4.082474,1.285185,-4.594798,-7.884365,9.565668,-9.926086,-7.673919,-4.458845,-7.417642,-3.935686,-3.206400,-4.585591,-9.301713,-5.553001,9.998778,-9.505323,1.700072,-4.091048,5.308138,8.636903,6.885042,-3.152846,2.604706,0.619591,9.847949,-7.741951,-8.256116,1.396883,7.942814,-1.922084,8.617476,9.322425,0.375331,5.466591,2.125337,8.455450,-8.775441,-7.795339,7.443357,-9.338342,3.892723,-0.809810,4.562920,2.674566,-3.601449,1.585432,-7.919455,-6.074649,-9.442063,-6.477918,3.012483,4.920369,9.369633,3.677372,2.042894,1.993992,2.165470,2.494782,7.639171,1.330067,-3.508030,-4.344390,3.862501,-5.931866,-8.007900,8.876917,2.010555,4.568641,1.454744,8.036365,-3.826971,8.013489,-5.191196,-3.376013,8.284866,2.040747,0.801713,4.617397,1.333378,-0.836220,-3.247535,6.971672,-7.782655,2.440322,6.254990,9.826056,2.813213,6.899729,1.268380,-9.529062,4.016400,-8.109367,8.665220,-1.325145,-2.099054,-3.778375,-6.949827,-7.371722,-1.815438,-6.271660,-1.588047,-2.755041,9.670201,0.650351,4.779357,5.179595,-2.757927,3.861790,4.395969,-7.641073,7.844853,8.017714,-1.738782,-9.806643,6.999518,-0.813162,-0.480023,1.838418,6.592953,-5.008541,-6.297457,2.872770,-0.807919,-8.576881,-1.795851,6.732946,6.894626,-3.266792,-2.688909,4.697772,7.491397,3.486011,-7.480630,7.147739,3.459384,-5.385396,-1.341048,-2.711113,6.972235,-7.000052,5.157798,4.026007,-1.085993,-1.306477,-5.772060,-1.525278,-8.547463,-9.352229,8.227688,-3.945821,6.226584,-3.616390,-4.536828,-8.175495,-6.178656,-2.904232,-9.023142,-6.058718,7.398809,3.047372,-9.381741,9.460006,9.506985,9.401539,-3.489727,-1.134572,7.971797,2.188893,3.684663,4.654486,-0.139237,-2.339255,2.770287,-5.997757,9.897527,-3.718982,1.363527,-4.151466,3.480794,6.379116,5.405112,-4.703505,2.275262,5.180707,8.187956,-8.286098,-6.790882,8.430586,6.583925,-2.699288,6.240695,8.406188,-9.178098,-5.592442,6.391496,9.360752,5.958451,8.475317,6.771572,6.261194,0.323412,6.084693,-7.375632,9.664765,-0.905514,9.624432,5.174894,-5.869538,-7.267565,7.965311,4.793536,4.650092,-5.937887,7.639492,3.845987,9.587311,-0.364262,-2.496976,1.877943,-5.881247,1.346963,3.815225,-6.622445,-1.036260,-6.877195,7.935094,7.773509,-8.523243,4.388308,1.541722,9.018836,-5.328855,3.719740,-9.005821,-8.144447,-0.306630,-3.598947,-4.060722,-7.802512,-2.248757,1.791721,-1.134408,-1.146456,-5.210121,-8.017321,-2.561923,-2.146068,6.822318,8.828897,-6.650494,-0.499821,4.916560,1.920226,-6.666422,-4.860705,-8.553437,-6.877606,-0.692059,-5.076030,-9.250067,8.902778,-1.913962,5.747763,7.563112,2.250346,3.425577,1.604428,1.080651,-5.273894,-5.130489,-6.795366,-3.268401,7.761191,2.482522,-8.470727,-5.404129,-3.975579,8.963779,-0.278948,-9.263307,6.972001,8.489678,-0.696125,2.164143,-8.286488,1.221262,-3.498803,0.655125,4.840157,8.887054,1.015620,8.964140,-5.697286,3.385826,9.037957,2.474041,9.879591,2.524742,6.940693,9.842775,-3.400349,-2.325090,-5.315944,-5.751354,-6.543229,0.805440,2.504176,9.937141,-5.192251,-7.659496,-1.946554,-0.211926,2.494197,4.291199,-9.862771,-1.145550,8.863881,4.248492,1.811543,9.062595,-6.153282,0.763430,4.819373,6.379609,2.990614,-1.061228,0.054985,-3.952720,-8.772956,0.654105,-1.334610,-4.005724,-4.986642,6.206679,9.829743,7.902195,-3.709180,-5.350825,4.416822,6.883126,7.949433,-7.552431,-5.440002,2.154962,-0.401250,7.400083,4.694216,0.605482,2.120499,3.362419,0.047655,-6.195365,1.372908,-2.523987,5.649995,7.473010,0.562861,9.669088,-2.182941,-3.870188,-7.265861,0.893996,6.709029,7.153180,-6.313654,-2.647294,-7.958523,0.503944,1.390574,-5.932014,7.076340,0.589361,-3.264929,-0.933876,-9.037109,6.724122,-4.664241,-6.650401,6.363420,-5.037481,-6.331512,-4.815356,-0.949271,-6.995848,6.988446,-2.163817,-0.019340,7.170888,-4.089082,-8.237021,-2.860176,7.289041,-5.376233,6.820201,-3.782589,7.973634,-7.416672,6.536776,1.650237,-8.870144,-8.268372,7.598043,-6.462920,4.075229,-7.676541,7.156950,-6.504754,8.886126,-8.392178,-6.069344,0.290477,3.599552,2.940565,-1.862433,-1.565394,5.363598,3.492474,-1.949784,5.805485,-3.300256,8.259596,4.961746,8.822935,-6.166313,4.709519,-6.204554,0.979307,-3.700397,-8.049023,7.076331,3.583722,7.962062,-6.158542,-2.226452,-3.111232,9.135279,6.615079,3.648639,-8.564439,-2.537269,-4.750856,-2.923066,0.120489,9.600329,5.920986,-6.883598,6.259553,7.631656,4.323180,-0.528923,-1.488837,3.452868,-1.625704,-2.792732,9.348887,-5.636536,6.564580,5.846313,3.195624,-0.408011,3.613073,6.033947,3.033104,-7.643909,-6.193076,-6.107772,8.813352,-8.386015,-1.292465,-2.446486,-6.952034,7.851313,9.115257,-8.433375,1.030219,6.887849,1.336311,-7.333580,3.620180,-2.084928,6.011517,-4.772176,-4.547454,-8.000166,-6.871087,-5.892247,4.123031,-0.543828,-4.268112,3.003345,-2.628665,8.977526,2.897997,-2.007486,-0.950589,-1.836585,7.075186,-3.421155,-0.170529,-5.829282,9.438450,9.906735,-1.507943,0.148800,-8.952627,0.149750,7.319991,-1.531381,-4.785065,1.297044,2.248230,-7.286957,2.725807,8.075221,4.684443,-9.898616,-6.318305,5.398378,2.441569,-4.223244,3.916415,-5.051960,-5.706955,6.454563,0.784098,0.333726,-2.380631,6.892821,9.545870,0.499068,-5.186507,5.382664,6.991697,-3.756977,-5.290494,-2.219540,-6.453756,-3.768692,-7.359694,4.600771,6.943981,-1.161887,-2.320278,7.280671,-2.771016,-4.682647,-6.872916,-6.349093,-6.882679,-6.541604,7.275151,-3.727366,-1.822035,-8.422680,-6.487408,-1.650911,-2.077822,7.318227,4.779985,-7.131744,-4.765266,-8.276001,1.641516,-9.741352,9.881525,-4.677596,-4.593495,-0.647176,4.458059,8.809705,-4.439040,6.985027,-7.575166,5.530427,0.977012,-0.139091,-2.379084,-6.823644,6.033173,7.802232,-4.752650,6.503751,-9.580765,8.725412,-7.026764,6.710810,-1.485245,1.938573,-9.631337,-1.157929,5.047753,2.454619,-3.119006,2.905035,-9.162655,-3.533939,-2.433668,0.609959,-1.263801,-0.421856,6.987291,9.150933,7.141836,8.759902,-9.473401,3.204308,-5.412912,2.188525,4.440029,-3.483995,-9.633744,-8.672425,-9.011210,2.038908,-2.284757,7.549713,-8.784714,8.586661,2.084092,9.394208,0.246916,1.954622,5.222778,-0.653384,1.849474,-1.155096,0.349646,-8.935020,2.540255,-5.903769,-3.745152,5.145675,2.778325,-6.380548,1.870979,-6.631110,-0.061518,-7.778371,-9.378267,-5.053883,0.031039,9.309939,4.687977,-8.151789,-1.507204], dtype = "float64")#candidate|8712|(2016,)|const|float64
call_8711 = relay.TupleGetItem(func_8113_call(relay.reshape(const_8712.astype('float64'), [2016,])), 3)
call_8713 = relay.TupleGetItem(func_8115_call(relay.reshape(const_8712.astype('float64'), [2016,])), 3)
uop_8724 = relay.acosh(var_8699.astype('float64')) # shape=(1, 546)
func_7711_call = mod.get_global_var('func_7711')
func_7713_call = mutated_mod.get_global_var('func_7713')
var_8734 = relay.var("var_8734", dtype = "float64", shape = (480,))#candidate|8734|(480,)|var|float64
call_8733 = relay.TupleGetItem(func_7711_call(relay.reshape(var_8734.astype('float64'), [480,])), 1)
call_8735 = relay.TupleGetItem(func_7713_call(relay.reshape(var_8734.astype('float64'), [480,])), 1)
func_5341_call = mod.get_global_var('func_5341')
func_5347_call = mutated_mod.get_global_var('func_5347')
const_8750 = relay.const([2,-5,-3,-8,8,10,-2,8,-5,4,6,2,8,6,-6,10,8,-10,-2,9,-2,3,6,-3,-6,4,4,8,4,1,4,-8,7,-3,-6,10,-9,-3,4,6,4,10,8,1,-3,-1,-4,-9,-9,-1,-7,7,3,1,-8,7,-10,10,-6,-1,-3,-6,-3,7,1,9,10,4,-7,-3,3,-7,-7,-1,7,-2,4,7,-6,1,6,-5,-7,-2,-3,9,6,-9,10,8,1,10,-9,-5,5,4,8,-8,8,9,-6,9,4,-5,-9,-4,4,-8,-2,9,10,1,-5,-3,10,6,2,-9,3,-3,-8,3,-2,4,5,-3,9,1,2,8,-9,1,-10,-10,-6,-5,1,-6,-10,-6,8,-8,-3,2,4,-1,-4,6,5,-7,10,-5,10,3,6,5,-1,2,3,-3,-3,1,9,1,3,4,10,4,5,-9,9,4,8,-3,-9,7,-1,7,-6,-3,-6,4,-8,-5,-8,-3,-10,-4,-2,-9,-5,1,9,-7,8,-5,7,-10,10,8,-10,4,8,10,8,9,10,-9,-9,3,8,-2,9,-2,7,-8,10,9,-3,6,-10,5,4,-8,-2,-10,9,5,-4,-7,-6,-10,-9,2,7,3,2,9,4,1,-8,-6,3,-7,8,-9,-10,-1,-7,-1,1,-4,-2,1,10,-1,2,-7,9,-1,-7,1,7,-6,-5,9,-1,-10,-7,6,-4,-10,-4,-1,-3,10,-3,7,5,4,-10,-7,-9,-3,-10,4,6,2,2,-5,-6,-5,7,8,-5,3,7,-6,7,-3,-8,4,-2,6,-8,7,7,2,3,-6,-4,6,9,10,-1,6,1,-5,-6,8,-3,9,-6,4,3,-10,10,-10,9,-8,2,-2,-6,7,2,-8,-10,-5,-8,-8,10,9,5,1,-7,6,5,-2,7,-2,3,-1,7,-1,-4,7,8,-4,-3,-9,-5,2,3,10,-3,6,-2,-1,3,-5,1,-3,-10,-2,-3,5,-5,8,9,5,-2,-10,-8,-5,-2,-1,4,2,10,-7], dtype = "int64")#candidate|8750|(390,)|const|int64
const_8751 = relay.const([2,8,-7,5,10,10,6,1,-5,-7,-8,-9,1,8,10,-5,-7,2,-9,-5,2,2,9,5,-6,3,5,5,-6,1,2,-10,8,6,9,-4,-9,1,2,2,-10,-2,-6,3,1,10,2,6,-2,-5,4,-1,8,2,8,7,-10,-5,7,-10,3,-4,10,3,2,2,-7,-10,-7,-4,6,-2,-10,3,-6,6,5,-4,-9,8,7,9,4,-1,-2,5,6,-6,-6,-4,4,-2,1,3,-7,3,-10,9,2,7], dtype = "uint64")#candidate|8751|(100,)|const|uint64
const_8752 = relay.const([-1,1,9,-8,10,2,-10,-1,5,3,-1,-2,1,2,-7,-9,-2,-6,8,2,8,1,1,1,10,-5,1,3,9,-9,4,5,-10,5,-8,5,4,-4,-8,10,2,-10,3,4,-9,-8,-3,-7,7,1,10,1,-2,9,-1,1,-4,-4,-2,-9,-3,4,-2,-9,4,6,3,-9,2,8,-5,-5,-10,4,-9,-5,-1,-8,-1,-4,6,10,-5,6,-5,1,5,-8,6,9,6,10,4,-2,7,-9,-6,-2,-7,10,-7,3,6,-9,5,2,1,-1,-1,9,9,-3,-8,-5,7,9,6,-6,-3,-9,-2,-2,-4,-9,5,5,5,-8,4,9,1,-5,-2,-3,7,-3,-4,1,9,-3,7,8,-7,-6,2,-2,7,-1,-10,2,-6,-6,4,-8,-7,-7,10,-8,-4,8,4,-8,-9,8,3,7,-8,10,10,5,9,-4,7,-6,10,6,7,-5,-3,6,-4,7,-5,4,-5,5,-10,2,2,-8,-3,-6,-10,-7,-3,-1,5,1,-7,7,3,-7,-8,-2,-9,3,-7,-2,-10,-2,-3,2,-10,-10,-7,10,-7,-2,-6,-7,5,6,-1,-10,9,-5,-4,-10,9,3,7,5,8,10,4,-8,-9,2,3,2,4,4,-8,2,4,-3,-7,-6,-8,9,-6,-2,1,7,-5,-8,10,-5,-6,-6,-4,-5,9,-8,-8,10,5,-8,-5,-2,8,9,2,4,5,-10,1,10,5,-9,-6,-8,3,7,3,-10,9,-8,-7,9,-4,-1,-2,-5,8,3,-6,-4,7,9,-3,2,2,5,2,-1,2,-1,2,5,-1,3,7,6,-1,5,-4,9,7,-5,-7,5,-8,-6,-4,8,9,-3,-1,10,4,7,2,-5,-8,-8,-9,-6,3,7,3,3,9,8,-6,1,8,1,-1,-1,-9,6,3,-6,4,-4,-9,10,-4,7,1,-4,-5,8,-1,9,-7,-9,6,7,-9,8,-9,-7,9,6,3,8,5,7,3,8,-10,-2,-6,-6,-1,2,-5,6,-4,-5,-10,-6,6,-3,-9,1,-1,6,4,-10,-6,-7,-3,6,-3,6,-3,10,-8,-2,-3,-6,6,2,4,6,-6,3,-6,-7,-4,-6,-7,-8,-9,-4,3,-9,-2,10,-2,-7,1,-8,-3,-8,9,-3,10,1,-2,-2,-5,-6,1,-4,-4,1,-3,4,3,-2,-4,9,6,3,-5,5,-7,8,8,-3,2,-10,1,10,4,4,-7,-3,-3,3,1,-9,-8,8,-8,8,5,7,-10,7,1,3,6,-2,-2,6,-2,4,1,-6,5,1,2,5,6,-7,7,8,-5,10,-7,3,-3,-1,-10,-3,3,-6,-5,6,-7,10,-2,-5,9,4,-6,-7,-5,1,-7,4,-2,2,3,9,-10,4,-9,1,-8,4,-4,-1,9,-6,-10,-6,-3,10,-8,-6,9,-2,-10,-6,8,2,-1,2,-7,-8,-9,9,-3,-7,-9,-9,4,-5,-4,7,-1,3,2,-5,4,-5,-8,-6,-5,-1,-8,3,2,10,-8,-8,-4,2,8,6,-1,-6,7,-9,5,-9,2,4,-7,-10,1,-6,10,-2,7,10,-1,6,-8,-2,-5,-3,10,-1,-4,-6,10,10,1,-10,-10,-4,-7,-10,-5,8,-5,7,10,6,2,7,-3,-3,10,3,-4,-2,-7,-7,-9,4,-6,1,2,10,-9,-5,-7,-9,10,7,-8,6,-3,2,8,6,-9,-1,-6,3,9,2,-6,3,2,1,-8,9,-10,1,-7,1,6,6,-3,9,-9,-10,-1,-1,2,5,7,-1,-5,4,-1,-9,-6,-9,6,-1,-9,7,5,-5,8,-6,5,3,-10,-3,1,-8,-7,-6,-6,-5,9,9,10,10,3,6,-1,-8,-5,2,3,4,8,2,-8,-1,10,10,3,9,-4,-1,-3,6,2,-5,7,-4,1,10,-4,6,-10,-6,-6,8,10,-7,-10,3,2,-4,9,-5,-5,-8,6,3,-10,-9,-3,-8,-6,-8,-9,-8,-10,1,4,10,3,-6,-3,6,-9,-2,2,7,-5,8,-9,5,1,-9,-6,-4,-10,-9,-1,-8,2,3,10,-3,9,10,-8,-7,3,-5,8,9,10,-1,-4,1,1,-9,-6,-7,-4,4,2,-4,-9,5,8,5,5,-7,7,5,2,8,-8,4,9,-5,-9,-7,8,8,-7,2,-3,3,8,7,-3,1,-1,5,-3,3,9,-4,2,-3,-9,5,7,-1,5,9,4,-1,-5,4,-7,3,9,-7,1,1,6,-9,3,9,9,-8,-8,-7,5,2,-10,-2,-2,9,-10,3,-6,10,-4,9,-9,-6,6,-1,-5,-7,-7,4,-9,-3,5,6,2,-3,6,-10,9,-5,7,9,6,9,-8,-3,9,-7,-3,8,-10,-2,2,-3,-7,-9,-4,-8,-6,-6,-3,-1,-6,-7,-3,6,5,-10,-1,-10,-3,3,-7,10,10,-6,-6,5,7,-2,-6,-4,8,10,8,8,-6,9,-3,-7,-4,6,-1,-1,-3,-1,-1,2,8,9,-9,-7,9,10,-4,3,-9,-7,9,1], dtype = "int64")#candidate|8752|(968,)|const|int64
call_8749 = relay.TupleGetItem(func_5341_call(relay.reshape(const_8750.astype('int64'), [13, 2, 15]), relay.reshape(const_8750.astype('int64'), [13, 2, 15]), relay.reshape(const_8751.astype('uint64'), [100,]), relay.reshape(const_8752.astype('int64'), [968,]), ), 1)
call_8753 = relay.TupleGetItem(func_5347_call(relay.reshape(const_8750.astype('int64'), [13, 2, 15]), relay.reshape(const_8750.astype('int64'), [13, 2, 15]), relay.reshape(const_8751.astype('uint64'), [100,]), relay.reshape(const_8752.astype('int64'), [968,]), ), 1)
func_2768_call = mod.get_global_var('func_2768')
func_2771_call = mutated_mod.get_global_var('func_2771')
var_8773 = relay.var("var_8773", dtype = "float64", shape = (180,))#candidate|8773|(180,)|var|float64
call_8772 = func_2768_call(relay.reshape(var_8773.astype('float64'), [6, 15, 2]))
call_8774 = func_2768_call(relay.reshape(var_8773.astype('float64'), [6, 15, 2]))
bop_8779 = relay.bitwise_or(uop_8724.astype('int32'), relay.reshape(var_8699.astype('int32'), relay.shape_of(uop_8724))) # shape=(1, 546)
output = relay.Tuple([call_8692,call_8698,call_8711,const_8712,call_8733,var_8734,call_8749,const_8750,const_8751,const_8752,call_8772,var_8773,bop_8779,])
output2 = relay.Tuple([call_8693,call_8700,call_8713,const_8712,call_8735,var_8734,call_8753,const_8750,const_8751,const_8752,call_8774,var_8773,bop_8779,])
func_8791 = relay.Function([var_8699,var_8734,var_8773,], output)
mod['func_8791'] = func_8791
mod = relay.transform.InferType()(mod)
var_8792 = relay.var("var_8792", dtype = "float64", shape = (1, 546))#candidate|8792|(1, 546)|var|float64
var_8793 = relay.var("var_8793", dtype = "float64", shape = (480,))#candidate|8793|(480,)|var|float64
var_8794 = relay.var("var_8794", dtype = "float64", shape = (180,))#candidate|8794|(180,)|var|float64
output = func_8791(var_8792,var_8793,var_8794,)
func_8795 = relay.Function([var_8792,var_8793,var_8794,], output)
mutated_mod['func_8795'] = func_8795
mutated_mod = relay.transform.InferType()(mutated_mod)
const_8949 = relay.const([[[4.842690,-4.124551,-4.549697,3.467874,-2.473640,6.971065,6.035401,8.737256,-7.418964],[-5.032507,-8.517401,-5.075146,-0.321733,7.764702,-0.683954,2.542194,-8.866428,-0.543278],[-7.877611,3.182065,-0.901235,2.179132,9.202946,2.660043,-0.529403,-6.924497,-6.278822],[9.497834,-2.123683,-0.075422,4.584055,-1.693428,4.634630,5.408765,1.877503,-6.404732],[9.302559,9.887217,-7.039726,-1.917151,-5.812698,1.267059,1.584330,5.046633,2.015329],[2.510588,5.358246,7.124873,-0.338706,-8.335273,1.464255,8.217660,1.265315,2.566983],[7.493870,-3.901141,-0.503768,-7.099852,-2.275567,-0.989188,9.396898,8.664150,5.516434],[0.941156,4.248911,7.528617,3.334521,6.639750,3.809194,-1.724986,-2.781569,-5.832613],[0.769836,-5.808421,-6.955041,8.574908,-2.893695,-9.822998,0.140305,-0.024527,-4.582340],[8.362911,-5.777741,-4.595915,2.168289,7.821019,3.392792,3.445340,-8.027270,-0.379536],[-2.814970,8.602680,-2.239629,-2.037348,2.414916,-2.986120,1.728622,7.605942,-7.680858],[2.853564,1.878694,1.132464,9.332619,4.848765,3.134915,-6.074889,4.310782,-5.796501],[-3.202514,-3.900497,0.096997,4.943081,-3.559292,3.553616,-2.157944,5.338641,6.565139]],[[-5.970220,7.241125,-3.259248,5.214471,-3.369238,-5.565104,8.069146,5.714248,1.820935],[-6.299665,8.034325,8.219159,-3.627302,-3.713177,0.457583,-1.865574,-1.984696,4.961519],[-2.779029,5.076227,-4.686103,-8.054581,-9.107874,0.433132,-5.380118,-8.103713,-7.167947],[-2.053696,2.153400,-0.837083,-8.304360,-6.799605,-0.192675,-2.183572,6.324545,4.859909],[2.337328,5.247140,-5.685305,7.657791,-0.169065,-8.502927,-9.589927,0.080629,2.325206],[-4.780324,8.699749,-9.010046,6.688193,-7.984857,0.723277,-3.513828,7.867589,-8.854515],[-8.341097,9.356384,-4.980037,9.103677,-3.086009,-4.691480,9.637844,-6.634836,-9.298790],[-7.299442,6.291040,-1.816927,4.903121,4.118277,-2.525275,-2.576810,-3.634902,4.140517],[4.542841,0.756312,-9.959623,-6.357921,-1.155909,-3.974511,4.141478,-3.651327,4.220397],[5.551564,5.279230,-7.507217,1.327817,-3.001498,-8.781172,-2.879040,1.228625,4.648760],[5.838562,2.076804,-2.038997,-0.779080,-2.809409,-8.676452,0.908712,-2.731323,3.707364],[-9.013890,7.416376,-3.914844,7.371261,-1.750151,-7.196278,-1.745449,6.238627,0.271303],[1.562570,1.541256,9.003664,8.298545,-9.313050,5.180941,-4.583709,-8.921625,9.001718]],[[5.439150,6.541294,8.342482,-9.328175,5.397030,0.592871,4.197473,1.338166,-5.782244],[8.529053,5.030454,-6.772516,9.988851,8.327722,-8.199453,-4.745497,1.840310,1.226527],[4.456043,-2.211579,8.626759,1.689089,-3.401095,-9.523246,5.938867,-2.292012,6.193513],[-0.332985,-6.919091,-3.324594,-6.407440,-2.749784,-9.181408,-5.871934,6.971868,-6.712351],[-8.533934,-3.746053,-0.095013,2.932638,-5.509327,7.306087,-7.473336,-2.036455,8.172629],[-0.088149,0.444203,1.979462,-2.944805,4.328423,-6.389884,6.128769,9.549841,2.008804],[-4.520617,-0.630879,-8.355215,-7.699777,6.265869,7.415976,4.331426,-7.185593,4.085699],[-6.027348,6.666917,9.004812,8.104018,-5.387725,-2.192464,0.295114,-7.978520,4.294667],[5.897934,-5.892578,-7.821954,6.611051,3.303876,-2.280177,8.234221,-5.816499,-8.299562],[-5.155879,-2.131725,3.381757,-6.292020,8.420128,-3.984325,8.028806,-0.211542,-2.300241],[-6.464644,-0.538906,8.412344,-6.155467,2.942040,0.221930,-5.758738,-5.780349,-2.902790],[-2.660770,-8.476853,3.754631,-6.047886,-0.584766,-4.936906,-3.028280,-2.129849,-1.419482],[1.503905,-3.407001,-9.454854,1.606197,2.151750,3.829160,3.351802,-6.847995,-2.683541]],[[-2.912484,-1.494580,6.724328,0.058848,6.772666,3.744224,6.276513,-0.613409,1.173834],[4.246370,-2.865168,-2.577830,-2.872959,4.548667,8.213138,-8.346476,-1.367295,-2.435147],[-7.141403,2.644385,4.907025,7.589114,-6.808207,-1.149356,-3.358904,-5.638392,-7.956998],[9.873287,-7.919332,3.291280,-8.868561,7.839567,1.264295,-4.418253,2.721479,3.303518],[-5.271604,6.206429,8.737023,0.278260,6.865701,-2.311449,-5.445203,-2.171188,-8.461047],[6.920654,8.134204,3.601446,-5.744004,-5.707055,-6.862351,4.597139,7.724790,5.824456],[-9.370292,-6.547921,-9.063256,-0.728088,-8.714689,4.498420,-4.246161,1.234874,6.997640],[-7.389979,0.572544,8.374228,5.955403,-1.237135,0.774619,9.773244,-9.529387,9.310247],[-6.633794,-9.004273,-2.461005,3.024676,-4.209778,-3.798636,9.998633,0.485254,-2.666501],[-6.854958,7.260047,-6.602173,-9.712023,9.530942,9.173452,8.240531,-4.343118,2.704336],[5.237261,9.368416,6.284228,2.926979,6.075995,0.289452,0.492653,2.918672,1.706158],[2.917802,3.252758,-6.814616,4.272627,-7.946433,7.365489,-7.366779,-7.177559,-2.900269],[-5.694833,-5.060893,4.081749,3.662851,-5.240217,1.887079,-5.812227,4.147102,2.897845]],[[-6.466031,-1.934240,-5.490573,-0.537696,-7.320908,5.227639,7.003726,7.015727,0.860603],[0.058425,7.328243,8.910667,4.915598,-6.163834,2.684701,2.299637,-1.047995,-3.527178],[1.134309,-1.487283,0.976418,4.747397,1.200911,-6.349493,7.827801,0.938726,2.223723],[0.700536,-2.528072,-5.821916,-3.517880,2.909919,3.111732,1.216104,0.658234,-9.113840],[5.000875,7.898655,-3.369710,3.208966,3.792004,4.487235,4.495898,-5.342771,-2.913598],[7.814781,-3.343883,5.484106,-8.203263,-6.851691,-7.755513,-5.061311,-5.802948,-0.350843],[-7.748776,-2.711210,-7.668810,-3.913662,7.573175,0.366358,1.301190,-7.348927,-2.392258],[8.417489,-3.335178,-2.250697,5.971853,4.791115,-1.736002,-5.423492,0.233423,-8.780549],[-3.083607,-0.561227,0.933811,4.740309,-6.769015,-4.938028,-9.004014,-8.911691,-0.782085],[7.269198,9.437935,9.345150,7.864555,-2.480847,6.912519,-1.891668,-5.935924,6.825457],[0.574552,-2.468403,-4.024573,-3.647218,2.972769,3.347884,1.092456,8.262235,7.725608],[-0.872511,-3.875217,-2.499039,7.487764,-7.200480,9.984053,-0.045956,-3.338708,-4.917305],[5.538613,3.415570,2.522502,-3.721072,-9.338730,-0.172433,5.879049,-8.207947,7.868709]],[[5.161036,0.090911,-1.058454,1.788193,8.766196,-9.914150,-8.444163,-3.099929,-6.388810],[-7.163434,-1.640074,-0.051796,7.646751,8.100371,8.726699,-3.040338,-1.758060,-5.415098],[-7.488938,7.956231,-1.908805,5.100689,7.293972,-6.409134,-0.933608,2.077956,9.871516],[6.959150,7.556197,-6.497470,1.827404,0.489446,6.906999,3.799704,0.922053,6.103356],[-0.621703,-5.367822,9.213983,1.752757,9.923523,-3.834334,-6.174512,1.273977,1.678818],[-5.786254,-1.885224,-4.350241,-5.016284,2.053687,-7.391874,4.941478,-0.285229,-5.893416],[-8.511539,1.376630,-4.545590,4.120173,7.386863,-1.779686,-9.359438,3.043296,-2.412843],[-6.690546,0.885510,-2.647415,9.648425,-8.825423,2.160485,1.990041,-4.300649,-6.937194],[-5.867466,3.210180,-2.867792,-5.712504,9.478890,-4.571531,3.859202,-1.080723,-9.789060],[-0.073124,-0.878970,2.149595,-2.755341,9.567884,7.917250,6.203134,5.456167,4.242919],[8.447227,7.293305,-1.382093,-1.296760,-4.624106,-9.590032,-5.605234,-5.779042,-9.448534],[-2.403872,-0.409961,6.834996,9.003020,-7.850902,-9.333246,1.741328,9.167648,-3.491426],[-6.867696,-5.223207,6.356293,4.303659,2.698260,-9.221190,-1.443806,-0.979957,-1.404010]],[[-8.097320,1.179516,4.578690,2.087901,5.404214,0.414152,-8.704081,-5.549337,-9.578079],[3.133727,0.492509,-8.151622,-1.523073,3.992351,9.022607,3.405008,9.171997,-8.321219],[-4.681561,6.469960,6.340995,8.919841,-6.490212,-1.701763,0.504344,6.571471,-9.412694],[-8.132905,-6.076019,-4.682239,7.090023,8.289085,-6.886813,1.827756,3.047588,-6.981332],[6.459848,-3.784340,3.223701,5.667274,9.231314,-3.433638,-8.974212,-7.764475,-8.375057],[-9.209566,-2.966970,-1.819696,-3.468788,1.478557,4.607064,-5.792194,1.315059,-7.539718],[8.184518,9.486066,-3.545866,-7.627130,-9.568312,8.007638,6.333455,5.935577,-4.428914],[-0.722788,0.226967,-6.015056,5.445560,-6.952044,-1.531082,-0.070985,-1.570365,-5.234072],[7.127464,5.566728,2.763938,-5.442244,-4.846282,1.236071,4.914674,5.960662,9.767352],[3.139478,-3.198199,-4.266948,5.516824,-5.767303,-5.775078,-9.859536,-0.316383,-6.743461],[1.919667,-8.952544,-7.292531,-3.827764,-7.238675,-0.121563,2.971604,-1.852655,7.102252],[-0.737662,5.182711,-7.999108,3.387873,8.786900,-3.707310,-4.033564,-8.079130,-7.301113],[-6.643243,2.205592,-4.989111,-8.048369,7.025609,-7.282822,8.417549,8.331530,1.230549]],[[0.827594,4.580301,-5.163265,-9.222563,5.291088,-4.986076,9.482817,-8.430824,3.817744],[-6.149367,-1.283343,-2.969690,1.056456,-3.721173,6.763971,-6.199393,-0.928971,1.588035],[-5.028871,2.242438,3.266940,3.410632,-9.961985,3.650207,-9.526404,-4.908765,3.675553],[6.325128,-7.803711,-5.218730,-5.127956,-6.738638,-8.359497,5.629385,7.842538,-2.105544],[-2.848257,6.877626,2.293111,-8.286448,7.259143,-5.569681,-4.009834,4.818910,7.926196],[-3.088228,-6.688953,3.733612,-4.875201,6.354052,3.679226,-3.207844,8.870557,4.652351],[-0.092177,0.128136,-3.549971,3.495965,1.802666,8.179250,-3.104113,-9.357658,3.081488],[5.234138,6.290323,7.998336,-0.184716,-5.248223,-0.216976,-1.964262,-6.579060,-0.115331],[7.779607,8.710896,-2.721295,-7.907804,-2.803849,1.400646,-4.894122,9.646289,-4.238559],[-3.699300,3.096747,-7.551169,-2.185163,-2.531109,-7.727015,4.077394,-9.746292,2.725263],[-3.283467,0.237880,-5.744978,-5.130731,9.107406,-5.174106,-9.709300,-7.596704,-5.964557],[9.095132,6.214477,0.885351,-9.763120,-6.567506,6.624701,9.573402,4.493787,-9.231947],[-4.519176,-5.081519,-4.385812,9.377783,4.712981,-0.629052,-6.160568,6.647155,-6.600021]]], dtype = "float32")#candidate|8949|(8, 13, 9)|const|float32
uop_8950 = relay.asinh(const_8949.astype('float32')) # shape=(8, 13, 9)
output = relay.Tuple([uop_8950,])
output2 = relay.Tuple([uop_8950,])
func_8963 = relay.Function([], output)
mod['func_8963'] = func_8963
mod = relay.transform.InferType()(mod)
mutated_mod['func_8963'] = func_8963
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8963_call = mutated_mod.get_global_var('func_8963')
call_8964 = func_8963_call()
output = call_8964
func_8965 = relay.Function([], output)
mutated_mod['func_8965'] = func_8965
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5674_call = mod.get_global_var('func_5674')
func_5676_call = mutated_mod.get_global_var('func_5676')
call_9006 = func_5674_call()
call_9007 = func_5674_call()
func_4652_call = mod.get_global_var('func_4652')
func_4658_call = mutated_mod.get_global_var('func_4658')
const_9009 = relay.const(-8, dtype = "int64")#candidate|9009|()|const|int64
var_9010 = relay.var("var_9010", dtype = "int64", shape = (364,))#candidate|9010|(364,)|var|int64
const_9011 = relay.const([5,7,7,5,4,-7,3,5,1,2,-8,9,-4,9,2,-6,4,-3,5,4,-1,10,8,10,9,-9,5,-10,-4,5,-1,-5,4,7,-7,-3,-1,-2,8,-6,-6,-1,4,9,2,-4,-5,-7,6,-10,-6,-3,4,4,9,-1,5,-7,-5,7,-10,-2,1,-6,5,3,-7,-8,2,-4,-2,-8,-7,9,1,1,8,-8,5,9,-2,-1,7,-1,-1,-1,-10,-3,-4,-2,8,-6,-9,7,-2,3,-9,2,-4,-8,-8,10,-8,8,5,4,-3,2,-9,-5,-7,5,-3,-3,-8,9,-10,5,-2,-7,-10,10,5,7,-1,5,3,4,-4,10,-8,9,10,5,4,-10,-4,10,-4,-3,1,5,-9,9,-7,-7,-10,2,-8,-3,-8,-9,-3,2,-7,-2,-5,4,5,-9,-2,7,5,-1,4,-7,5,5,-6,7,3,6,6,4,-3,4,-3,7,-8,-1,2,-7,6,7,10,-9,-3,3,-3,1,-1,-1,-5,2,-7,-10,-5,-8,-10,4,10,4,-6,-5,3,-7,2,-1,-6,-2,10,-2,8,5,-6,1,10,-1,2,7,1,-4,-2,2,9,-3,-6,3,6,6,-5,-7,-2,-5,-4,2,8,10,10,-10,-6,10,-7,-7,-9,6,-10,2,3,6,10,5,-3,-8,7,-2,8,-6,-4,-9,-8,8,-7,-9,8,8,-5,-3,-7,3,-8,8,6,-4,-9,-5,7,-4,-6,5,-8,1,5,4,-7,-8,2,3,-2,-10,10,-7,-9,-3,1,8,-2,-5,-4,-1,-5,-6,-4,5,-5,-4,-10,-2,-9,-5,-5,-2,-3,6,-5,6,3,-5,10,1,-6,-10,6,-7,-9,7,-7,-2,5,8,2,-10,-8,4,-6,3,1,-8,7,4,-8,-1,2,-5,-9,7,-7,-10,3,-2,6,10,-9,6,2,4,-1,-4,6,9,2,-1,-4,-5,5,-5,5,10,-2,1,-6,-3,-8,1,-8,-3,8,-3,-7,1,-8,-2,-2,6,-7,-9,2,10,-10,-7,-1,1,6,-4,-2,4,-1,-2,7,8,-5,-8,8,-8,-1,9,5,1,-1,4,-10,-3,3,4,3,7,-9,-6,3,9,1,5,-7,-7,3,-2,-8,-6,2,4,-3,5,5,1,7,3,-6,-4,-9,1,-10,7,-2,2,2,-9,-8,7,8,-3,-5,-3,-7,6,-7,7,4,9,8,9,-9,5,3,-1,9,5,2,-9,-6,6,3,-5,9,2,5,-9,8,-4,-7,1,10,-2,-6,5,5,7,7,3,-6,-5,-6,7,-8,6,-5,1,-5,-10,-3,2,6,-6,-1,-1,5,8,-10,-7,6,-4,-2,-8,10,-7,1,-3,-7,10,-9,5,-6,-7,-7,-5,-10,6,5,-9,2,-8,-5,9,-9,10,-7,1,-7,10,-3,-9,-5,4,-10,3,-9,4,1,6,2,5,2,-5,-4,-4,-1,7,9,3,4,-1,6,-7,-9,-6,-2,10,-9,-4,1,10,-3,5,-10,-1,-2,-9,8,-5,10,7,4,-5,-4,6,7,7,-4,-1,-9,-9,5,-1,-4,1,10,6,-7,7,-10,-9,8,6,-6,-8,-9,10,-5,-10,-9,-4,1,5,3,-1,4,1,-6,3,5,-1,-10,-10,-1,-5,1,1,3,2,-7,-10,-5,-2,9,-2,-9,-9,-3,-4,-1,-7,10,6,6,-9,1,4,2,6,3,8,-3,1,-9,-10,-3,3,-5,-7,7,5,-7,3,-7,5,-8,-2,-3,7,-7,10,-2,-5,2,-9,10,-6,-1,10,-9,-7,-9,8,-3,2,9,-2,-5,-9,3,-3,-10,-3,9,10,-8,4,8,-9,-8,1,-3,10,3,4,-7,-10,5,1,-5,-3,-10,2,1,-6,-2,-6,-3,-4,6,-4,-4,-4,-6,-4,-6,5,4,-3,-1,-1,10,-10,6,1,2,6,8,5,-5,-6,-4,8,-8,-2,-9,-4,2,2,-7,-9,6,5,5,9,-8,4,4,9,-2,5,-4,2,2,-2,-7,-10,-6,9,4,3,3,-4,-9,10,-2,5,-3,-1,-3,4,4,4,-10,1,-3,5,-4,-2,2,8,-7,9,2,-5,-3,-4,4,4,3,7,4,3,-3,-2,-8,-8,-3,-7,8,-7,-10,7,9,7,1,-1,7,2,8,4,2,1,2,-10,9,-3,-10,-2,-4,-2,-2,-9,-6,9,-2,-10,-5,-4,2,-9,-3,9,-3,-4,-9,-1,1,9,10,1,-1,8,5,-4,6,-7,6,-4,-6,-5,5,5,-7,-3,-4,-8,-9,-2,-10,1,-2,7,-4,-4,-9,5,-6,-8,-9,-7], dtype = "uint16")#candidate|9011|(880,)|const|uint16
const_9012 = relay.const([-8.180700,-5.213068,3.461664,5.601382,2.377330,0.255025,-2.099348,3.075747,8.575996,5.473517,-2.102813,3.670111,3.080807,-9.140112,1.716148,-4.633325,6.022454,9.870900,6.601500,7.763767,-9.459764,-3.037466,-7.279221,4.093323,0.967700,-5.249500,-9.184967,9.365672,-6.340704,9.259845,5.924422,6.786510,-5.998932,3.705764,6.096438,-6.202674,1.569692,3.590886,-2.165025,-8.537015,4.809569,-2.885635,-1.618256,-6.335673,6.224204,-5.424066,3.786277,4.342169,0.007512,-1.420061,0.340278,-8.256535,7.624571,0.295121,-2.549919,-4.900773,-4.228249,7.528295,-7.699868,8.456362,3.083384,-9.573111,4.555329,-2.990387,6.894384,-3.991640,1.756063,6.616828,-4.421593,3.701990,-8.039099,-7.686184,-8.232630,-4.124346,6.869432,-1.127836,7.359462,-3.475862,-4.101681,1.792522,8.888493,-4.238833,-3.836323,6.419663,-3.876788,9.578334,-9.677080,-5.892578,-7.153279,-2.742188,-5.941809,-3.493337,5.616098,9.067451,-2.505638,1.573134,-2.055304,-1.701611,-4.882493,4.859379,-9.960302,6.397916,-7.853682,9.941292,-1.117442,7.792694,-8.715314,9.599410,-0.244678,8.271088,3.517371,-5.660778,5.711655,4.123443,-9.230520,-4.599866,1.218791,-5.125574,0.003442,-3.851369,5.901034,8.083310,-9.121504,4.150965,9.304050,9.622733,-6.410128,-3.812476,-2.952640,4.469468,-5.443805,-7.045298,9.753608,1.540505,-4.311941,4.270301,1.160256,-3.003470,6.270300,-7.262404,-2.398510,3.802407,0.301965,-1.919013,0.574040,3.488214,-1.411567,-7.886465,-7.931949,-9.134520,4.267732,-2.673116,-3.670960,-6.611286,-4.612653,-3.670432,-6.064232,4.563658,3.688919,-8.746385,9.164660,-6.171043,0.879757,-3.470178,5.080917,-2.726306,-0.080516,7.485932,0.245795,-7.694111,4.358026,0.350259,-7.333765,5.294991,-6.045222,2.747869,3.803261,7.601936,-0.760224,-6.439628], dtype = "float32")#candidate|9012|(180,)|const|float32
const_9013 = relay.const([[-0.030036,-6.616820],[5.137447,-7.472215],[5.467977,1.527272],[-3.444493,-7.651095],[-5.335342,-9.477267],[-4.243837,4.317834],[-2.164024,-4.792561],[-6.664642,-5.619453],[-4.203694,1.260804],[-8.146836,-2.564288],[-9.761470,6.142297],[-6.249777,-6.788124],[8.411352,-1.532420],[8.664667,7.524245],[-1.169262,8.541914],[4.894466,-0.575396],[-0.652048,8.494221],[9.010313,-0.798892],[-3.755100,-8.206450],[-6.790076,9.960267],[1.671055,8.981263],[7.290963,-4.164427],[-4.259827,-8.834633],[-3.596338,-4.953068],[-8.975918,6.469527],[5.882866,5.614459],[0.980682,-8.175966],[7.825062,-8.189986],[-3.964030,5.208499],[-9.069274,7.306151],[6.812161,-1.763435],[-6.576818,-0.731293],[2.860815,-1.503081],[-9.227065,-6.184450],[-3.740974,9.327408],[-8.054359,-0.295893],[6.350028,-5.788647],[-9.345510,6.016448],[5.394458,7.639051],[-8.104999,-7.010206],[7.127252,-0.997339],[-7.452023,-0.670544],[-5.210068,-3.314895],[5.503512,6.439353],[5.891401,-7.728038],[6.448798,9.138044],[8.078386,3.981632],[5.267654,4.868870],[-5.518612,-3.130339],[-6.801916,3.474191],[-5.942859,1.164137],[6.141728,-0.469764],[-6.935221,-6.006560],[-2.297360,-5.402129],[-5.705061,2.747978],[4.416674,-1.627237],[5.710396,6.343870],[6.393809,-1.669747],[-7.299168,6.939996],[-8.324268,-9.302453],[-6.714337,-5.050356],[7.027502,2.512594],[-3.596621,0.279573],[2.066040,-1.713441],[-6.773961,5.339413],[-4.148506,6.492727],[7.605263,-9.104151],[-8.994058,4.161022],[3.398528,-0.329667],[-1.345683,-8.477756],[-8.249617,9.827160],[-6.573615,-9.663284],[2.233148,-5.290376],[1.216091,-1.248683],[8.981388,-9.242335],[-2.079855,-0.484075],[-3.260967,-5.141021],[-0.433564,1.344901],[-2.862567,3.008006],[-5.587245,6.137166],[3.035630,-1.030049],[1.032256,8.276163],[0.656410,-7.464489],[8.207856,-9.783068],[7.101466,0.752807],[8.559229,7.576669],[1.065154,-2.182269],[-8.641244,7.978780],[-3.372073,7.945787],[-4.390821,-1.111829],[-3.587675,2.006066],[5.132213,4.066121],[-8.683330,8.038565],[-6.771550,4.789299],[7.861643,4.331199],[8.309608,0.925292],[-1.215385,8.184005],[8.030713,7.237056],[8.069127,-2.034418],[-6.517908,1.114689],[-1.565219,-2.470710],[9.437540,-5.558303],[-1.436603,0.388276],[-6.825936,7.173859],[4.699921,0.720117],[-6.381766,-9.107203],[-8.507381,-1.071890],[9.716029,7.244784],[-0.641304,-1.187405],[-8.949860,-4.328820],[-2.931786,-5.715691],[-6.262628,-2.344385],[4.699855,3.796897],[-5.777103,3.296684],[-6.138458,9.356620],[4.182515,3.301708],[-1.568771,-4.182449],[-2.752319,5.451801],[-1.367114,6.802368],[4.404646,-6.146924],[5.893124,-5.259829],[0.690460,-4.174815],[-7.230037,9.527081],[2.981806,5.150361],[-5.089200,-4.254291],[7.516352,-3.570899],[8.923940,-0.756576],[7.553430,4.957330],[-8.449591,-8.929266],[7.322929,3.019037],[-7.058112,-5.088608],[0.680743,6.410510],[3.101235,-6.697355],[-2.304113,-3.965068],[-5.670335,-1.074005],[7.501319,5.768329],[-5.827545,3.930137],[-2.523845,8.967178],[-0.240929,-3.316959],[9.769879,7.170025],[2.512474,5.056277],[-1.916174,-3.387759],[1.639747,-3.850710],[-8.974816,-6.239939],[5.330069,4.614355],[9.829727,-3.554852],[-2.044977,3.196700],[4.248970,-4.021960],[8.361333,-8.729117],[9.904830,-8.775880],[9.914401,8.495726],[-9.879600,-0.397620],[3.545762,-9.029946],[-2.526083,-1.027388],[4.520714,3.850032],[0.580155,-6.195182],[8.139148,-7.284303],[2.291324,8.489697],[-5.056941,-3.361014],[4.200305,-6.828899],[-7.131572,8.352376],[-8.480140,8.480080],[7.609030,-1.590240],[-0.617534,0.968534],[5.977205,-0.488887],[9.652232,3.084271],[-9.421900,-6.344779],[7.796534,5.060115],[7.199610,-8.632977],[-7.659433,-6.106953],[-8.733052,-7.833863],[6.656545,7.162095],[-2.446516,9.001323],[2.998117,8.503401],[-8.267139,5.985825],[-9.749356,-0.803214],[8.711994,7.903494],[-0.731216,-5.421967],[-2.862923,-9.453159],[-2.112883,-8.331633],[3.361862,-1.864792],[6.795670,0.184450],[-6.637641,8.985229],[6.874436,-9.731946],[-5.373697,-1.139560],[3.525292,-5.240166],[-2.417263,2.483548],[-2.380241,7.337620],[7.890494,-9.031595],[1.899713,3.935734],[9.129712,-2.466316],[-5.211642,5.249555],[8.266702,2.564419],[-3.247853,-6.475118],[-4.517603,-2.674273],[-3.656026,5.244672],[2.546016,-1.773968],[9.980807,-1.510358],[-9.502486,8.873639],[-5.768391,2.800909],[-6.737193,-3.129330],[-5.666092,0.334313],[0.826756,5.084052],[7.322134,5.987963],[9.428335,9.048124],[3.941943,0.742269],[5.441036,-3.486725],[0.301051,1.716355],[7.307840,0.314417],[-5.892570,-7.542267],[-9.896097,5.468862],[-7.587032,-5.026627],[-7.246507,-2.443846],[-8.906797,7.929916],[-8.843076,2.724830],[-3.051920,-6.987329],[-2.123015,2.323496],[-5.884060,-0.516297],[-3.727012,1.256573],[7.199204,-3.576651],[7.341343,2.422007],[-4.355118,3.534528],[7.894956,-0.903816],[8.953602,5.895025],[-0.938253,0.120677],[-0.800506,9.833717],[0.716298,-7.272227],[2.200539,4.877042],[7.995348,-3.882505],[4.088751,4.734457],[-0.215407,-2.558728],[-8.670534,6.255907],[8.351337,3.803315],[6.624674,-2.326853],[5.164278,8.439636],[2.452490,-0.314810],[6.076083,-1.115626],[-9.110504,5.275327],[9.768811,1.791773],[7.628311,0.384562],[1.964373,2.288733],[8.208867,4.190144],[-6.639787,1.401246],[1.061153,-9.932139],[-6.487132,-5.219483],[-0.854907,2.194222],[4.667584,6.717430],[-6.745691,0.799832],[-0.456355,-9.262407],[-7.869564,-6.248258],[-3.992275,-1.366019],[8.297405,-9.144705],[1.276686,7.028048],[9.558739,-6.293253],[0.865142,1.385783],[-0.600572,5.547617],[1.718577,-8.499407],[0.311452,-9.661881],[3.393351,-4.825690],[-4.043113,-6.794812],[0.151681,1.610776],[7.700158,3.017950],[-7.178729,-8.568359],[-2.984373,9.648756],[7.685981,2.098661],[-2.981226,-4.383055],[0.129475,0.116897],[0.425877,5.380216],[2.858807,1.839733],[-6.022314,5.797922],[-2.444108,5.195604],[0.631460,-6.388364],[4.587448,6.375269],[-8.750291,6.815630],[-2.653043,9.745658],[-5.622055,-9.851878],[7.004365,-7.148805],[7.582309,-5.069770],[7.600535,-0.181147],[-2.420570,3.060592],[-0.732167,-1.408566],[-6.067579,-3.029424],[-6.272061,0.584075],[5.506071,-2.765219],[5.481479,-4.672435],[-5.452489,-4.551451],[9.923539,-6.025200],[-5.058153,0.431285],[-2.708399,6.991720],[7.663273,-6.044174],[6.748684,-9.546331],[3.076037,6.276593],[-6.094704,2.564698],[6.908422,-6.340910],[-8.296139,-8.399455],[7.196507,-4.954988],[8.681992,-6.271266],[0.107779,-7.440353],[-1.878701,1.452401],[9.087229,5.764626],[7.536144,-4.520285],[-8.890619,2.831293],[0.230419,7.930740],[4.432558,2.239598],[1.991293,3.573779],[-6.571006,6.945832],[-6.955848,-9.898036],[-5.499774,0.318362],[0.867126,-3.769380],[7.927032,-6.162821],[4.390235,6.667087],[5.853573,-9.269201],[-6.068751,-6.028424],[3.381755,-4.561868],[-0.439918,-8.030577],[-5.100376,-3.011948],[2.910600,3.796968],[-0.126566,-6.377771],[-8.620195,-8.645257],[-3.884435,-9.008710],[-6.585265,6.989639],[1.198678,-4.674256],[-3.521953,-9.554714],[-5.457357,-3.669662],[4.743355,-8.343165],[-2.133819,0.942915],[-7.311062,-9.740093],[-7.259017,-7.184035],[5.715518,8.667163],[4.367572,9.896360],[-4.014705,-9.125341],[-4.967448,-4.857486],[-2.316702,-1.858462],[5.017625,0.473772],[3.919998,-2.173918],[3.832829,9.032339],[-0.444065,4.932507],[-1.751869,-7.301844],[-2.442941,0.225453],[0.386455,-0.530606],[3.638829,-2.788855],[-2.823996,-3.991311],[-7.993858,-7.243441],[7.700899,-0.890752],[-2.832027,2.158757],[-3.137099,8.485645],[-5.247485,-7.476759],[-6.204592,-3.051683],[9.186954,7.595809],[-3.766328,1.578313],[-1.653325,-9.103364],[4.322114,-4.256773]], dtype = "float64")#candidate|9013|(352, 2)|const|float64
call_9008 = relay.TupleGetItem(func_4652_call(relay.reshape(const_9009.astype('int64'), []), relay.reshape(var_9010.astype('int64'), [364,]), relay.reshape(const_9011.astype('uint16'), [880,]), relay.reshape(const_9012.astype('float32'), [90, 2]), relay.reshape(const_9013.astype('float64'), [704,]), ), 3)
call_9014 = relay.TupleGetItem(func_4658_call(relay.reshape(const_9009.astype('int64'), []), relay.reshape(var_9010.astype('int64'), [364,]), relay.reshape(const_9011.astype('uint16'), [880,]), relay.reshape(const_9012.astype('float32'), [90, 2]), relay.reshape(const_9013.astype('float64'), [704,]), ), 3)
func_8542_call = mod.get_global_var('func_8542')
func_8546_call = mutated_mod.get_global_var('func_8546')
const_9016 = relay.const([7.730921,-7.215782,7.674814,7.342296,-0.148304,-8.007286,-6.463006,7.786394,0.531318,5.042495,-2.438834,5.517573,8.241920,-4.384703,8.435109,-1.239666,7.591335,-1.083673,-1.567317,0.488002,8.859995,-4.427697,1.595455,6.650245,1.849013,-7.038641,-3.684408,-1.308253,-5.339139,8.997061,-7.334038,-3.607657,-1.123265,-1.684031,-2.570435,0.271409,-2.977539,3.116076,4.131488,-1.022867,-0.496351,-0.321921,-1.441913,-5.135692,7.492695,-7.077258,9.973085,-8.401031,7.818957,-8.795701,-1.989865,-0.954917,6.436387,-0.145857,-7.941737,8.466982,9.273160,7.990521,0.397827,-9.004438,1.072680,-0.510683,-0.881919,3.826305,-7.071570,9.583166,6.485725,5.353173,-1.127959,-3.202278,-9.787761,8.558551,1.656163,0.554495,-3.355817,-8.503992,0.119601,-2.455197,0.011860,1.236063,4.561847,-7.208369,-3.240491,5.557702,-6.520952,3.651131,-5.644909,-9.549950,-7.149238,-7.294753,-3.559672,-8.619563,6.313863,9.028386,-1.179040,-3.850774,4.836277,1.353831,-4.041797,-4.586230,-9.105846,8.896513,-5.078444,-8.815545,-4.693275,5.911325,5.251405,-1.223655,-7.749765,9.275930,-5.490891,-6.748929,8.857186,-9.479818,1.176493,-6.491300,-0.398634,-7.208276,6.185210,3.928538,9.759852,-6.045094,3.257491,8.997895,-6.979555,-0.557972,5.734956,0.409771,-8.205941,-5.894993,-2.954159,2.262796,8.262971,-9.879912,8.014392,-9.088037,-3.363621,0.340841,4.260929,-5.135942,-5.146039,-1.697205,5.042360,-9.127523,6.675400,8.944530,8.795040,1.805475,-9.783377,5.701087,6.636872,-7.021504,2.209467,4.598432,6.885524,-9.066904,6.142330,1.005047,-6.526262,-7.908278,-1.601700,-2.232695,8.125614,-5.917054,8.984374,8.430755,7.316381,-8.829456,6.927615,8.314345,2.011167,-9.332097,7.103295,-8.346150,3.804599,1.684107,-3.059484,7.288351,6.432279,-5.862883,-0.296050,-0.192625,8.459801,-8.171979,-6.623240,6.437263,2.386697,-4.885972,4.645033,3.595993,-7.558604,1.057199,-9.902820,-3.033121,-2.602920,-7.913259,-4.549914,1.273208,5.285587,-5.339561,8.812934,-4.007208,-4.567853,8.638485,6.129078,-2.464333,-5.028917,-3.189655,9.241743,-8.844054,6.345754,-5.376907,0.357540,-6.293823,2.793604,2.103783,-9.720662,1.380876,-5.109906,4.719874,9.443272,5.446273,9.833270,-3.169113,-3.217502,-2.067532,2.099251,4.172163,-9.774704,-7.114154,8.806693,7.676369,9.686689,-8.128294,7.103837,5.556495,5.103174,-5.782648,-6.223677,4.664256,-9.131207,0.871994,-5.821559,-0.909564,-5.556418,-7.576291,-9.405156,9.281542,6.720892,-9.771190,2.495453,7.018507,-8.400416,9.806674,9.449716,-3.071088,2.971931,7.635541,-2.089375,-9.257063,-9.899442,-1.358128,-0.603415,-3.872988,5.816882,0.059075,-7.945425,-9.805162,-2.497696,-0.865634,-8.731238,3.280187,-1.971866,-5.177412,1.109648,4.638317,7.377543,-9.811874,6.292212,8.677464,7.107242,-0.901349,-5.069137,2.687363,-9.194999,-2.794433,-7.844472,-6.149232,-9.231815,0.971280,-3.804305,-9.287864,9.946330,2.587395,3.961487,4.468255,9.714447,5.060069,-1.805373,0.988990,-9.219761,-9.805139,2.905326,3.693255,2.690244,3.199720,5.056191,8.469846,1.688009,6.255740,-4.398770,0.051448,-6.026275,3.230263,3.701817,-2.764118,-7.527347,-4.456037,0.847035,3.490954,5.475057,-9.981852,-3.243822,7.639085,9.799175,9.831475,1.442122,9.356469,7.876473,9.498840,0.602030,-1.957657,-6.871324,-3.330341,-5.179518,-0.278066,-1.600452,-7.068576,-7.614347,-7.615891,-7.024531,4.333685,5.622688,-8.986082,2.313061,0.229635,6.595220,-4.850673,0.427922,2.598626,1.129462,4.566514,9.557716,-4.324317,0.980062,5.637334,-9.006822,3.839905,8.519671,-8.708964,3.979298,-1.693856,2.976504,-2.746604,7.107935,-6.593113,8.656757,-9.372770,5.066385,9.968192,-1.774846,2.998759,7.142191,-5.249200,-9.854179,-6.925648,-5.554624,-4.759733,0.382414,-5.232816,-3.308281,0.353723,-7.733020,-0.411279,1.464350,-7.231705,-0.094533,-3.364114,0.064974,9.874869,-2.350674,5.976079,-8.200542,-4.395811,5.823856,-3.961328,-4.953877,3.074255,6.350251,-6.675076,7.251104,-0.349591,-6.959725,-0.874335,4.780708,4.195094,8.612725,6.879534,-7.805051,4.291799,-0.185915,-3.238379,-9.108717,-4.043127,6.156948,-3.575459,7.136099,9.924664,2.123302,2.841841,8.619996,-9.318930,-7.946425,-5.878899,-5.405861,-1.528332,5.076066,9.037426,-4.239475,0.570246,-3.072950,4.078935,5.636881,-0.827259,-5.698068,5.045345,-4.033894,-4.800553,4.539303,-2.976899,-3.719081,1.176652,6.535889,6.402585,-9.242756,3.767976,-0.952207,-4.869126,3.595471,5.355983,7.641770,2.393637,-6.536078,-3.598582,-2.086250,5.684134,2.495969,-3.573090,7.197817,-3.968371,3.021263,6.704416,-1.495143,6.697073,-2.629401,1.079111,3.960129,2.944921,-1.315744,-4.036861,-4.013411,-9.672838,-4.770198,-5.177619,-2.618662,9.717023,9.364049,-6.131831,-5.884947,9.967640,-1.352222,-1.791960,-8.670038,7.232640,7.536117,9.093346,-7.666241,2.219819,0.919665,-7.473515,4.650757,9.531334,-3.984792,-4.243846,3.809882,6.674212,2.263501,9.238446,-4.298449,-5.993086,-1.669922,4.008723,4.090038,4.456980,5.531725,0.898778,8.868280,9.546512,-3.245051,5.743565,2.915164,2.017831,-0.573619,-9.202017,1.316130,3.432399,4.031580,-3.434182,2.550699,5.616544,-9.742470,0.583499,7.521073,7.468739,2.019225,7.973573,-4.228646,8.628488,5.927137,7.117629,-7.788814,3.178836,7.847182,4.114090,6.432979,8.347920,2.157037,-6.822654,4.548171,-1.623568,-8.250908,-3.571133,-9.637140,1.982670,6.203685,-8.864575,3.922545,6.250047,-6.306121,-5.143279,2.027665,8.236244,-9.872335,2.859174,9.939454,-2.697990,7.857409,-7.969775,-0.840196,-2.079718,-7.989506,-9.238375,-5.626752,0.787130,-2.930614,-2.705316,5.695141,-2.087680,5.360402,-1.220067,2.050446,-7.616933,6.784230,-3.001998,4.618524,3.456683,1.158395,6.126006,-8.077057,-6.356078,-6.874315,-6.027917,-2.338750,-2.366954,5.416240,6.415028,7.889979,4.866947,-2.308792,6.588996,-4.222181,-7.668291,-5.454158,3.655937,-0.600290,6.776402,1.721281,-9.683692,-3.679434,2.154638,2.500342,-8.867732,0.613286,8.387885,5.371745,9.859211,-6.546421,9.570290,8.376008,0.830301,4.101747,2.842325,-4.250754,-7.894191,-3.665996,-8.345488,-0.527293,-5.323925,8.319816,-8.317297,-9.424455,-0.963498,5.151261,2.045457,2.564634,-1.001580,1.593427,8.722987,4.951638,-4.818164,3.941548,-7.223787,3.483197,9.837259,-0.534317,6.806923,2.366900,5.230790,-5.452060,-1.540456,3.231817,-4.491100,-8.893287,9.852090,1.985950,9.602528,-6.133368,5.910941,-3.640945,-5.185744,-9.776263,-0.299040,-6.043979,-5.850363,-5.380136,-3.925164,4.034039,8.398856,-1.359226,2.370497,-0.683690,-5.745188,-6.704587,5.892766,9.887649,-6.400968,3.508395,8.582092,-0.926793,-6.796040,-9.143323,1.312305,5.016307,9.367301,7.060839,-8.590791,9.088986,-4.714007,-6.737968,5.551862,-7.373553,5.788628,-0.588881,2.648285,-5.190296,1.523342,-5.334357,-5.980567,0.433981,7.927340,-9.823370,6.300623,-3.877784,-9.723016,4.957902,-5.915984,8.647389,3.600908,1.262770,-2.779201,7.754214,-3.575339,-4.487791,5.396043,1.309399,-5.685428,-7.363721,6.069136,-8.758234,2.094801,2.580012,7.071552,4.329629,-4.820550,9.884969,-3.872875,6.800374,-4.403388,2.295021,0.416670,-3.584744,7.319977,6.672898,3.850135,-2.482092,7.273096,6.006448,-4.826196,-4.382360,5.563851,3.168894,-5.131971,-1.249448,5.777524,-9.085238,-7.342124,-7.456927,-3.549147,5.255287,6.178409,-8.557360,9.990775,2.210799,8.267743,4.010451,2.186650,-1.552106,4.877867,-8.449362,6.526064,4.547297,4.208801,5.018085,-2.665441,-8.341986,-8.232236,-5.605101,-6.393334,6.302166,6.263868,-1.013591,3.736927,-7.743054,8.408620,0.649823,-4.125613,8.476566,0.927663,1.975326,4.055885,5.011321,-3.079229,3.160549,-7.237550,-0.787099,6.189712,-6.599498,-1.705782,2.679221,-4.535628,-9.710233,-7.400881,-8.691474,-7.800578,6.554943,4.624964,3.525139,-5.368241,-4.061842,4.936010,2.128439,8.028378,0.824573,-7.584322,-6.874722,-5.148452,7.277095,-8.862993,-0.529039,8.600495,-8.354055,-1.324948,0.992961,-7.134969,3.581484,-3.551802,7.671202,0.121074,6.696313,6.969467,-1.605755,-7.159496,-1.586745,3.291236,0.401995,-6.437135,-9.274152,1.336974,-3.975557,9.098640,1.456865,-7.760739,-9.617287,-9.829472,1.965450,1.551123,1.667076,-8.172160,-0.363050,-3.759494,-5.326540,7.158913,5.593036,-3.762709,-0.488569,-9.826937,-7.509267,-4.376118,-4.589911,-2.503953,3.760837,6.931103,-6.432976,-9.838013,3.070502,-3.167981,-8.836144,-2.726428,9.963412,1.711572,5.366559,6.331803,-1.919933,-8.641513,-2.699808,-2.755581,-6.286083,-0.170365,9.786727,0.058824,2.945289,4.161448,5.273522,-5.423810,-5.069153,-8.989554,1.667092,3.775592,-8.484317,-4.432594,9.919681,-3.928502,-3.192965,-7.786967,4.074838,-4.918218,4.363857,-7.846103,-5.801978,5.143194,-5.598781,-4.517446,-7.567088,4.973354,6.365680,6.231093,3.498662,-7.344377,2.273686,1.106294,-0.430986,9.157342,7.643349,-3.082191,-3.274789,4.391606,4.399835,-2.439641,1.526831,-3.847370,8.325735,8.811918,6.396954,-7.445556,-9.614833,-7.062770,-9.833385,3.836889,0.984858,0.870580,3.308470,8.894457,-1.028009,-2.122594,4.368742,-3.878413,2.441366,2.914532,6.445280,1.040145,-0.165348,-8.731666,4.235360,-8.827414,8.487327,2.858047,-7.926070,4.773417,-9.283610,9.568776,9.244940,6.812185,7.369745,1.955807,-3.166137,5.947317,-6.212125,7.356439,3.514417,0.508163,4.414215,0.864252,7.187219,-2.456312,5.473649,9.301350,9.309126,9.538006,-6.801016,2.349787,7.597000,7.050208,-9.238001,9.037626,-6.503702,-8.157677,4.632653,-2.418590,5.587628,9.091615,-6.990820,9.723853,9.954822,-8.258019,3.395725,-9.669134,-3.366978,0.704976,6.270027,-2.512144,7.665030,6.081355,1.755990,5.005223,6.296113,9.606945,9.217305,9.402124,5.241707,-6.941122,-6.422546,7.206089,-9.374334,4.032112,9.409959,-5.188116,7.153441,-9.195704,1.712212,9.117500,-8.839679,-0.166062,4.179112,-1.437701,1.984352,5.807115,3.982072,1.462901,6.143727,4.329708,-0.871254,3.580875,-1.079620,-6.697684,4.074974,-9.084866,-3.254837,-2.400515,-6.906563,-5.368683,3.766517,7.709027,-7.634020,3.633153,-0.719066,2.782719,-1.827053,-4.682149,-4.251085,-7.682818,-8.283848,3.707420,4.311881,-6.293154,-8.030283,5.887832,-2.676599,-2.610110,6.822769,9.798609,7.223714,6.789328,6.962815,-4.297618,-7.588158,-2.271713,8.237773,-2.354199,7.297051,-7.476381,9.763696,7.183615,5.541210,8.344439,7.970097,-5.612253,1.004274,-7.715984,8.485591,-2.651029,7.711896,-7.974602,-7.642106,5.619626,3.463604,3.664984,-3.928067,-5.922137,-6.255168,-4.513816,-3.010998,-9.601098,-5.218910,3.847291,1.305359,-3.289031,-1.428214,0.948561,9.521481,-3.094553,6.642423,2.568526,-4.207255,6.060316,3.202970,1.632863,-5.143823,4.647940,-8.450439,-5.625086,-7.997950,2.596158,8.914273,6.690840,8.722720,3.044864,9.428846,-9.909952,-3.322231,1.180318,-0.912526,-4.255322,-8.506228,6.928066,-6.683072,1.668644,-5.940853,2.669564,0.548871,-3.962493,-3.660385,7.710635,4.443061,5.387448,8.941131,1.346340,3.177385,-2.452848,-7.530573,3.859273,6.369949,5.406706,3.803203,8.900181,-6.192434,7.432938,9.531322,-4.695883,7.029415,0.044662,-2.675505,-8.437365,-4.908983,-2.453337,-0.539369,4.020537,-9.031703,-3.691887,9.773991,-0.803284,3.456455,-1.354152,3.797622,9.345308,-0.983475,9.910154,-6.584223,4.395755,1.368201,5.389850,8.027963,6.869556,0.616690,8.520822,-9.874462,-1.856161,4.404441,-6.863396,-6.676558,9.349989,-2.683030,4.725009,-5.406240,4.339015,-3.123884,-0.499607,4.396083,4.093776,0.525396,2.766539,1.040767,5.777233,-5.295269,2.170105,-2.051048,-5.453511,0.243636,9.995663,-2.690369,6.991668,7.265627,-5.499622,-4.960049,3.897487,-6.757056,4.905152,3.361155,-1.354005,-3.272798,-5.849114,0.773971,-2.882471,-7.817293,-8.360644,-5.270531,-8.914902,4.529660,6.855881,-9.357497,8.118520,4.518189,-7.045121,-3.499847,2.662782,-3.563790,1.451937,-4.733312,4.050913,5.199983,6.332664], dtype = "float64")#candidate|9016|(1200,)|const|float64
const_9017 = relay.const([True,False,False,True,False,True,True,True,True,False,True,True,True,False,True,True,True,False,False,True,True,False,False,True,True,False,True,True,True,True,False,False,True,False,False,False,True,True,True,True,True,False,False,False,False,True,False,False,True,False,True,False,False,True,True,True,False,False,False,True,True,False,True,True,False,True,True,True,False,False,False,True,True,False,False,True,False,False,True,True,False,False,False,False,False,True,True,False,False,True,True,True,True,False,False,True,False,True,False,False,False,True,False,True,True,False,False,True,False,False,True,False,False,True,False,False,False,True,False,False,False,True,False,True,False,False,False,False,False,False,False,False,True,False,True,True,False,True,False,False,True,True,False,False,False,False,False,True,True,True,True,True,False,True,False,False,False,False,False,False,True,True,False,False,True,True,True,False,False,False,False,False,True,True,False,False,True,False,True,True,True,False,False,False,False,True,False,False,True,True,False,False,False,False,True,True,True,False,True,True,False,False,True,False,True,True,False,False,False,True,True,True,True,False,True,True,True,False,True,False,True,True,True,True,True,False,False,False,False,False,False,True,False,True,True,True,True,True,True,True,False,True,False,True,True,False,True,False,False,False,False,True,False,True,False,True,True,False,False,False,False,False,True,False,True,False,True,False,True,True,True,True,False,False,False,True,False,True,True,False,False,True,True,False,True,True,True,False,True,True,False,False,True,True,False,True,True,False,True,False,True,True,True,True,True,False,False,True,True,True,True,True,False,False,True,True,True,True,False,False,False,False,False,False,False,True,True,True,True,False,False,False,True,True,True,False,True,True,True,True,False,False,False,False,False,False,False,True,True,False,False,True,False,False,True,False,True,False,False,False,True,False,False,False,True,True,True,True,False,False,False,False,True,False,True,True,False,True,True,True,True,True,True,True,True,False,False,True,True,False,True,False,False,False,False,True,True,True,False,False,False,False,False,True,True,True,False,True,False,True,True,True,False,False,True,False,False,True,True,True,True,False,True,True,False,False,False,False,True,True,False,True,True,False,False,False,False,True,False,False,False,True,False,True,True,True,True,True,False,False,True,True,False,False,False,True,False,False,True,False,True,True,True,True,True,False,True,True,True,True,False,True,False,False,False,True,True,True,True,True,True,False,False,False,False,False,True,True,False,False,True,False,True,False,True,False,False,False,False,True,False,False,True,False,False,True,False,True,True,True,False,False,True,False,False,True,False,True,False,False,True,True,False,False,False,True,True,False,False,True,False,False,True,True,False,True,False,False,False,True,True,False,False,False,False,False,False,False,False,False,False,True,False,True,False,False,False,True,False,False,False,False,False,True,True,True,False,False,True,False,True,True,False,True,True,False,False,True,False,False,False,False,True,False,True,True,False,False,False,False,False,False,True,True,True,False,False,True,False,True,True,False,False,True,True,False,True,True,True,True,True,True,False,True,True,True,False,True,True,True,False,False,True,True,True,True,True,True,False,False,False,False,False,True,True,True,True,True,True,False,False,False,False,False,True,True,False,False,True,True,True,True,True,False,False,False,True,True,True,False,True,False,False,True,True,True,True,False,False,False,False,True,False,False,True,False,False,True,False,True,True,True,False,False,True,False,True,True,True,False,True,True,False,True,False,True,False,True,True,True,True,False,False,False,False,True,False,False,True,False,True,False,True,True,False], dtype = "bool")#candidate|9017|(715,)|const|bool
call_9015 = relay.TupleGetItem(func_8542_call(relay.reshape(const_9016.astype('float64'), [10, 10, 12]), relay.reshape(var_9010.astype('int64'), [364,]), relay.reshape(const_9017.astype('bool'), [715,]), ), 4)
call_9018 = relay.TupleGetItem(func_8546_call(relay.reshape(const_9016.astype('float64'), [10, 10, 12]), relay.reshape(var_9010.astype('int64'), [364,]), relay.reshape(const_9017.astype('bool'), [715,]), ), 4)
func_3042_call = mod.get_global_var('func_3042')
func_3044_call = mutated_mod.get_global_var('func_3044')
var_9022 = relay.var("var_9022", dtype = "uint64", shape = (25, 4))#candidate|9022|(25, 4)|var|uint64
call_9021 = relay.TupleGetItem(func_3042_call(relay.reshape(var_9022.astype('uint64'), [5, 10, 2])), 1)
call_9023 = relay.TupleGetItem(func_3044_call(relay.reshape(var_9022.astype('uint64'), [5, 10, 2])), 1)
output = relay.Tuple([call_9006,call_9008,const_9009,var_9010,const_9011,const_9012,const_9013,call_9015,const_9016,const_9017,call_9021,var_9022,])
output2 = relay.Tuple([call_9007,call_9014,const_9009,var_9010,const_9011,const_9012,const_9013,call_9018,const_9016,const_9017,call_9023,var_9022,])
func_9028 = relay.Function([var_9010,var_9022,], output)
mod['func_9028'] = func_9028
mod = relay.transform.InferType()(mod)
mutated_mod['func_9028'] = func_9028
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9028_call = mutated_mod.get_global_var('func_9028')
var_9030 = relay.var("var_9030", dtype = "int64", shape = (364,))#candidate|9030|(364,)|var|int64
var_9031 = relay.var("var_9031", dtype = "uint64", shape = (25, 4))#candidate|9031|(25, 4)|var|uint64
call_9029 = func_9028_call(var_9030,var_9031,)
output = call_9029
func_9032 = relay.Function([var_9030,var_9031,], output)
mutated_mod['func_9032'] = func_9032
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6187_call = mod.get_global_var('func_6187')
func_6188_call = mutated_mod.get_global_var('func_6188')
call_9108 = relay.TupleGetItem(func_6187_call(), 0)
call_9109 = relay.TupleGetItem(func_6188_call(), 0)
output = call_9108
output2 = call_9109
func_9119 = relay.Function([], output)
mod['func_9119'] = func_9119
mod = relay.transform.InferType()(mod)
output = func_9119()
func_9120 = relay.Function([], output)
mutated_mod['func_9120'] = func_9120
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6812_call = mod.get_global_var('func_6812')
func_6814_call = mutated_mod.get_global_var('func_6814')
call_9178 = func_6812_call()
call_9179 = func_6812_call()
output = call_9178
output2 = call_9179
func_9226 = relay.Function([], output)
mod['func_9226'] = func_9226
mod = relay.transform.InferType()(mod)
output = func_9226()
func_9227 = relay.Function([], output)
mutated_mod['func_9227'] = func_9227
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8246_call = mod.get_global_var('func_8246')
func_8247_call = mutated_mod.get_global_var('func_8247')
call_9233 = func_8246_call()
call_9234 = func_8246_call()
func_5655_call = mod.get_global_var('func_5655')
func_5661_call = mutated_mod.get_global_var('func_5661')
var_9242 = relay.var("var_9242", dtype = "int64", shape = (390,))#candidate|9242|(390,)|var|int64
const_9243 = relay.const([[-7.105553,6.828869,-3.081054,-6.068240,-3.789241,3.716011,8.979388,-6.255949,7.688498,7.577826,-1.209604,3.805799,-2.878644,-0.403350,0.666558,-5.019228,9.671618,-1.262145,7.352939,7.968899,8.940133,-2.408457,4.785508,3.276425,6.778039,-3.817689,-0.061072,5.683475,5.025848,-3.319238],[1.141701,-0.162419,-8.465465,-3.724682,-3.917522,8.431452,-1.671489,-9.867594,-7.289256,8.109761,-3.385202,5.452464,2.019837,8.791659,-8.141986,-7.997634,7.140457,4.149767,4.338776,7.895084,2.171761,-4.955358,-9.929919,7.278673,-1.163999,-3.409394,-2.449652,-4.166310,-0.823528,-8.046773],[5.540409,-3.606675,-1.116188,-4.127725,-4.078637,1.057604,-8.328105,2.267990,-9.533843,-0.710950,8.487709,2.019585,-6.250745,-1.728973,-6.608262,-8.418782,2.040723,-5.175777,-0.835814,9.871817,-5.987660,-4.338406,-7.722694,0.137736,-9.769820,-2.607781,8.869716,3.513156,6.506429,-9.634109],[3.402837,2.282552,-6.711900,-1.401086,-1.761539,3.176899,-0.722182,7.864824,4.628599,8.230659,-8.013272,-7.218878,8.635409,-1.868567,8.386377,-8.611872,1.900395,8.802657,7.219247,-5.385186,5.727223,-3.263772,3.112597,5.042491,2.918617,-5.879854,-5.133169,0.235839,-3.908946,-1.944419],[-2.921981,-7.174387,-5.471449,3.708412,2.338404,5.837411,0.325295,-1.102092,1.814452,-9.332303,-2.770528,1.540888,3.913594,9.514286,-2.952165,0.870553,-4.536607,-0.978817,4.954461,8.315587,7.588311,5.846970,-4.312356,7.907543,1.393969,-2.709445,-9.772733,-4.632471,-9.914967,7.558369],[5.226069,-1.460200,0.209680,-9.731300,-5.910080,5.663067,-4.154977,1.795899,7.134787,9.693442,-2.524357,-2.752588,2.910548,-3.579251,-0.857466,-0.257394,-2.409320,-0.154385,5.060647,-9.977499,-6.954506,4.268753,-2.978052,2.720857,7.691004,2.530087,7.113860,-4.178748,-9.974596,-7.481296]], dtype = "float64")#candidate|9243|(6, 30)|const|float64
var_9244 = relay.var("var_9244", dtype = "float32", shape = (56,))#candidate|9244|(56,)|var|float32
call_9241 = relay.TupleGetItem(func_5655_call(relay.reshape(var_9242.astype('int64'), [390,]), relay.reshape(const_9243.astype('float64'), [180,]), relay.reshape(var_9244.astype('float32'), [56,]), relay.reshape(call_9233.astype('float64'), [7, 78]), ), 0)
call_9245 = relay.TupleGetItem(func_5661_call(relay.reshape(var_9242.astype('int64'), [390,]), relay.reshape(const_9243.astype('float64'), [180,]), relay.reshape(var_9244.astype('float32'), [56,]), relay.reshape(call_9233.astype('float64'), [7, 78]), ), 0)
output = relay.Tuple([call_9233,call_9241,var_9242,const_9243,var_9244,])
output2 = relay.Tuple([call_9234,call_9245,var_9242,const_9243,var_9244,])
func_9247 = relay.Function([var_9242,var_9244,], output)
mod['func_9247'] = func_9247
mod = relay.transform.InferType()(mod)
mutated_mod['func_9247'] = func_9247
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9247_call = mutated_mod.get_global_var('func_9247')
var_9249 = relay.var("var_9249", dtype = "int64", shape = (390,))#candidate|9249|(390,)|var|int64
var_9250 = relay.var("var_9250", dtype = "float32", shape = (56,))#candidate|9250|(56,)|var|float32
call_9248 = func_9247_call(var_9249,var_9250,)
output = call_9248
func_9251 = relay.Function([var_9249,var_9250,], output)
mutated_mod['func_9251'] = func_9251
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9226_call = mod.get_global_var('func_9226')
func_9227_call = mutated_mod.get_global_var('func_9227')
call_9253 = func_9226_call()
call_9254 = func_9226_call()
func_2768_call = mod.get_global_var('func_2768')
func_2771_call = mutated_mod.get_global_var('func_2771')
const_9268 = relay.const([-3.837694,8.510261,1.958350,6.557518,5.309118,0.883393,5.893335,8.841200,1.021651,2.803002,2.426590,-2.044603,2.646302,-9.181224,-0.359037,4.986202,-7.358691,3.263868,-9.823950,5.357038,-1.317394,7.701163,-5.502627,9.625239,-3.990627,5.204085,-0.961998,7.879369,4.277041,0.117218,3.316294,-1.954760,2.228819,4.926938,-3.760479,9.866194,6.376297,-8.109025,8.932043,-2.713686,-7.593004,-6.722813,6.927592,-2.957513,4.468310,-9.479042,4.547076,-1.367548,-4.176164,-1.486319,-9.773157,8.779480,-0.679468,-9.604329,9.455012,5.377136,-8.766032,6.344817,7.771951,-5.588734,6.604518,2.649128,3.412742,9.098619,-6.202009,-6.833989,7.629268,-5.129852,3.099976,-2.278200,9.792997,-4.820164,9.861684,3.886424,-8.726356,4.339483,-2.668399,-7.572062,-0.207359,2.814604,8.904999,6.560180,-3.796848,4.944105,-0.270561,-6.585850,7.232230,6.668601,-5.783259,-3.710181,-4.418778,-8.300566,-3.495949,-2.754388,-0.992553,6.168578,1.302838,3.169701,9.883023,4.049857,-0.280016,8.163139,8.259042,-6.822837,-8.032328,-0.235054,-1.257023,0.057197,9.168121,8.925989,-0.275892,2.507242,6.035023,9.089798,6.303448,0.939906,-2.128312,-7.814891,5.486352,-3.907022,5.572674,9.204997,3.186981,-7.985876,-3.780897,9.108860,9.148353,1.603630,5.483730,1.928910,5.388873,-0.689123,7.843859,6.210898,0.064500,-6.476251,-1.892929,-8.105836,8.188762,-1.930255,-2.080921,-2.370531,0.795257,-4.892432,-1.409606,8.331736,-3.809619,3.060925,-4.453881,5.028157,-5.700234,-5.436393,5.603187,2.900255,-9.023135,-6.892926,7.621332,-5.570525,-1.842188,4.666326,-2.360955,8.125515,-0.984558,-6.927886,0.405531,-3.587525,-8.374458,1.086603,6.510551,-1.581755,-0.109582,-6.656647,0.500358,-6.394817,8.770743,-9.592023,7.837020,3.634651,-4.542133,-7.967319], dtype = "float64")#candidate|9268|(180,)|const|float64
call_9267 = func_2768_call(relay.reshape(const_9268.astype('float64'), [6, 15, 2]))
call_9269 = func_2768_call(relay.reshape(const_9268.astype('float64'), [6, 15, 2]))
func_7376_call = mod.get_global_var('func_7376')
func_7378_call = mutated_mod.get_global_var('func_7378')
call_9270 = relay.TupleGetItem(func_7376_call(), 0)
call_9271 = relay.TupleGetItem(func_7378_call(), 0)
func_2768_call = mod.get_global_var('func_2768')
func_2771_call = mutated_mod.get_global_var('func_2771')
call_9276 = func_2768_call(relay.reshape(const_9268.astype('float64'), [6, 15, 2]))
call_9277 = func_2768_call(relay.reshape(const_9268.astype('float64'), [6, 15, 2]))
bop_9279 = relay.bitwise_xor(call_9267.astype('int64'), relay.reshape(call_9276.astype('int64'), relay.shape_of(call_9267))) # shape=(6, 15, 2)
bop_9282 = relay.bitwise_xor(call_9269.astype('int64'), relay.reshape(call_9277.astype('int64'), relay.shape_of(call_9269))) # shape=(6, 15, 2)
func_6610_call = mod.get_global_var('func_6610')
func_6615_call = mutated_mod.get_global_var('func_6615')
var_9290 = relay.var("var_9290", dtype = "int64", shape = (1, 390))#candidate|9290|(1, 390)|var|int64
const_9291 = relay.const([8,5,7,1,-7,-4,4,9,-5,7,10,-7,-7,-6,-10,10,-6,-9,-4,-2,3,3,5,9,-2,-7,6,-1,-10,3,-1,-7,-7,-9,-1,9,-1,1,-6,-6,-7,-1,7,-7,1,7,2,-9,2,-9,1,7,2,-7,-10,-7,6,-9,1,1,7,-2,-2,7,8,-9,4,2,5,4,-2,2,8,2,9,-1,-1,-5,-5,1,6,4,-5,4,6,5,9,-8,7,8,5,-2,4,1,10,5,-1,4,7,-6,-7,3,-6,-3,-2,1,-10,-6,-2,4,-1,6,7,-8,9,9,2,-2,-2,-1,5,4,7,-10,10,-1,-2,-3,-8,-5,-2,2,4,-4,8,3,-9,9,-10,7,2,1,8,4,4,4,4,1,10,8,-1,3,9,-8,-2,1,4,9,5,-7,-5,-4,-6,8,-8,-8,-7,-9,-5,-7,1,-1,9,8,-5,10,5,-8,-7,-9,-3,6,-7,6,1,9,1,-10,3,-4,-2,-8,-8,-1,1,2,8,3,2,-9,3,6,1,-6,-3,-3,-5,-3,5,6,6,1,-7,-9,-4,-1,-8,4,-2,-2,-1,9,3,-6,7,-6,1,5,2,6,-4,-4,3,-10,8,-7,8,-4,-1,-1,2,9,7,-1,2,8,2,8,1,10,1,-8,-7,-10,-3,-5,2,-8,2,9,-7,-7,10,6,-3,-1,-6,-3,-3,1,8,1,-2,9,8,-5,7,-6,9,-8,-10,9,10,-9,9,-9,6,6,-8,-9,7,3,-7,-10,-3,-1,9,-9,3,2,-7,-6,-10,10,-1,4,4,1,6,-10,-2,-2,-2,-10,8,-5,-10,10,5,-7,1,-4,9,-10,9,-6,2,1,-8,9,10,10,6,1,-2,-8,10,-1,9,7,-3,8,10,9,2,-3,3,4,5,-1,-2,3,-2,2,-6,-9,2,4,9,-10,-3,-3,6,6,-3,-10,7,-8,8,2,8,2,-9,2,10,-6,2,-1,-7,2,3,6,5,-1,-3,-6,-4,-3,-5,-2,-4,9,-8,-8,9,-6,2,-4,-5,2,2,2,-6,-1,-9,-5,-1,-3,-9,5,-1,-2,-4,-9,-5,-10,-9,-3,7,-6,-4,1,7,4,3,4,2,-6,-4,7,6,-4,-10,-1,-8,-5,-8,-10,8,-3,-5,4,4,-6,-7,-6,2,9,7,-1,7,-9,-2,-3,3,3,4,-9,-9,5,-10,8,-10,-6,-7,2,-4,-2,-10,-9,1,-10,1,-1,6,4,-8,-8,1,7,-4,3,-10,6,-10,-2,9,3,-3,2,-10,-3,-1,7,8,10,-3,-2,8,2,5,8,-7,-7,5,8,-6,-4,-6,6,6,-6,1,-3,-7,6,10,9,-4,8,6,5,-8,6,1,-6,10,-8,-1,9,-8,2,-10,7,-5,-3,2,-2,8,-2,2,6,3,2,-4,2,7,-4,-4,10,8,2,-3,10,-2,10,2,7,-9,9,-3,7,-6,-6,-4,10,4,-1,6,-8,-4,4,2,1,-4,7,3,5,5,-2,2,10,-5,4,-10,10,9,-10,-9,6,-3,-9,7,8,7,-2,3,6,-2,-7,-3,6,5,6,-9,5,3,10,8,-3,-9,8,6,-8,-6,-1,-6,-2,-3,2,1,3,1,-6,-1,-8,4,2,1,8,-7,-6,-6,-1,-9,10,-2,3,-6,6,10,10,9,-5,2,-6,2,9,2,-8,4,-10,1,-2,4,6,10,-7,-6,9,-8,6,-9,-10,6,4,6,-6,7,5,6,3,-5,-6,5,-10,2,-6,2,4,6,6,1,-8,-2,8,-4,3,-3,10,-4,-2,-8,-7,-4,6,10,1,-6,8,2,3,6,5,6,-7,8,7,8,4,-7,-2,-4,6,2,7,1,1,-7,7,2,4,-5,-5,6,-5,-10,10,9,-4,-2,-4,3,10,-2,3,-5,3,9,3,7,-8,4,-1,-6,4,7,2,-3,-10,-3,8,-2,-8,-9,8,-8,3,6,6,2,-1,10,-9,-8,-10,3,-9,-1,6,5,-7,10,-8,7,-10,4,6,-7,-8,5,7,6,-1,-10,-8,-2,-9,-7,3,-1,-1,-6,-10,5,9,-6,5,10,-10,6,-5,-4,-3,1,5,8,-6,6,-7,-6,8,-3,-5,-3,-5,-4,7,7,9,7,2,3,-10,-6,7,-5,3,1,5,2,1,2,-3,10,-9,-7,10,8,8,-1,3,3,-6,-3,-6,-2,-10,5,-5,7,-1,4,-8,-3,6,3,-2,7,-9,-10,7,2,-6,3,1,7,8,-5,-4,3,2,1,-2,-3,-3,6,5,-7,4,-4,4,8,3,-10,-4,6,9,-2,-10,-2,6,-10,5,-3,1,-7,-9,1,-10,8,4,-10,3,-3,-4,5,2,-4,5,7,7,3,9,-7,-4,3,-8,10,4,6,8,-2,7,7,-3,9,8,-5,7,8,-6,-9,5,-8,3,-8,5,3,-6,-5,-7,-9,10,4,6,9,4,-6,7,9,-10,-3,9,-1,8,-5,4,-2,10,2,-9,-7,6,3,9,-3,10], dtype = "int64")#candidate|9291|(968,)|const|int64
var_9292 = relay.var("var_9292", dtype = "float64", shape = (546,))#candidate|9292|(546,)|var|float64
call_9289 = relay.TupleGetItem(func_6610_call(relay.reshape(var_9290.astype('int64'), [390,]), relay.reshape(const_9291.astype('int64'), [11, 88]), relay.reshape(var_9292.astype('float64'), [546,]), ), 3)
call_9293 = relay.TupleGetItem(func_6615_call(relay.reshape(var_9290.astype('int64'), [390,]), relay.reshape(const_9291.astype('int64'), [11, 88]), relay.reshape(var_9292.astype('float64'), [546,]), ), 3)
func_7929_call = mod.get_global_var('func_7929')
func_7930_call = mutated_mod.get_global_var('func_7930')
call_9294 = func_7929_call()
call_9295 = func_7929_call()
output = relay.Tuple([call_9253,const_9268,call_9270,bop_9279,call_9289,var_9290,const_9291,var_9292,call_9294,])
output2 = relay.Tuple([call_9254,const_9268,call_9271,bop_9282,call_9293,var_9290,const_9291,var_9292,call_9295,])
func_9302 = relay.Function([var_9290,var_9292,], output)
mod['func_9302'] = func_9302
mod = relay.transform.InferType()(mod)
mutated_mod['func_9302'] = func_9302
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9302_call = mutated_mod.get_global_var('func_9302')
var_9304 = relay.var("var_9304", dtype = "int64", shape = (1, 390))#candidate|9304|(1, 390)|var|int64
var_9305 = relay.var("var_9305", dtype = "float64", shape = (546,))#candidate|9305|(546,)|var|float64
call_9303 = func_9302_call(var_9304,var_9305,)
output = call_9303
func_9306 = relay.Function([var_9304,var_9305,], output)
mutated_mod['func_9306'] = func_9306
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7639_call = mod.get_global_var('func_7639')
func_7641_call = mutated_mod.get_global_var('func_7641')
call_9310 = relay.TupleGetItem(func_7639_call(), 1)
call_9311 = relay.TupleGetItem(func_7641_call(), 1)
func_3623_call = mod.get_global_var('func_3623')
func_3625_call = mutated_mod.get_global_var('func_3625')
const_9332 = relay.const([-2.950087,9.372757,7.022345,-4.955168,9.312705,-6.638364,3.693465,3.713517,-8.520916,0.808701,-5.549208,0.092004,1.393280,3.191115,8.619815,-1.284038,-1.670461,-6.158520,9.787408,3.764611,-8.533901,0.572469,-5.459632,7.900838,1.820662,5.876456,3.379316,-9.278320,8.857557,-3.910641,-9.655471,-7.425628,-0.769503,-4.725787,1.295123,9.761146,7.832248,-9.751935,6.694801,-5.301571,-9.875737,-2.757033,-8.990700,-2.188129,8.660705,1.113306,0.767755,-9.179207,-2.108524,6.662514,-9.535998,2.246746,3.274687,6.912716,7.534933,3.909050,8.031346,6.105445,4.910731,8.316886,-5.588268,-4.861569,8.580992,-3.674281,-0.843281,0.348284,-8.192908,-0.981640,-6.806320,-0.228954,-5.732156,0.345113,-7.730734,3.082986,-4.428164,-0.899228,2.373620,-3.090328,3.517580,-8.573114,-4.987451,-5.277257,-4.447647,-0.139313,9.713491,-6.496294,7.869067,3.680975,8.964268,3.761013,-6.881919,-1.897264,-2.969603,-8.878802,5.637810,7.674075,-5.841322,-2.132697,1.815840,-8.703180,-3.410678,-2.696188,-9.935344,9.898213,-2.595760,-9.762194,-8.080566,1.863384,0.752698,-5.716514,-0.651582,6.293858,5.478327,-3.937300,-0.434504,8.791922,7.264471,-8.625404,-7.201371,9.948099,-3.424284,2.626764,0.249769,-6.281332,-2.219205,6.532700,-7.770224,3.353631,9.268813,-1.270085,-5.310238,-5.278172,1.757864,-6.185604,-1.103102,5.788679,6.967981,8.662841,3.988312,0.623278,-4.441580,-2.145903,9.356722,-4.111525,3.511326,6.399098,7.222241,-0.782639,-8.847510,-0.193268,-5.591944,-2.948130,-6.126205,-1.370857,7.504420,9.749962,9.158120,-9.506656,5.948427,9.303864,-9.369099,6.969447,-0.059462,-5.132099,-9.984376,6.141232,-8.437280,-9.547133,4.776702,-1.230616,-7.803067,-7.148021,-2.073058,3.211670,9.118450,-2.604181,2.082036,7.555101,6.425650,-0.688761,-1.266446,2.502796,6.360201,0.485158,-7.556403,0.854678,1.662474,-2.951216,4.104439,-3.380396,-0.376648,-8.817511,-2.863047,2.989912,6.385525,0.970911,5.898300,7.607130,-6.355035,8.088151,-1.354802,5.193178,-7.675934,5.432228,3.467445,9.783344,2.735102,9.425356,9.743033,9.637134,4.967285,0.418705,7.643873,3.124089,9.984801,2.748722,-1.785739,-6.705474,-5.511858,-4.866152,1.705502,-8.090874,8.078624,-8.596687,-6.461833,1.316623,-8.690223,6.804513,1.995359,7.265135,6.661981,0.473533,7.679151,7.535406,8.042928,-5.725719,0.987347,1.773629,-7.686818,2.922796,-3.192448,-3.655782,4.157133,-5.234101,4.816003,-8.855958,-1.189405,-9.574399,5.622200,-8.396672,0.254503,6.873676,4.503289,7.233371,-5.563960,-4.727482,7.987204,8.410808,-6.140124,-3.103698,5.538450,1.525943,-6.443400,7.646271,1.069874,-4.078605,-2.378399,8.563011,9.774825,-8.131405,9.464122,-1.929775,6.483947,-4.789690,0.218217,1.290345,9.691774,3.397075,-7.818319,5.854895,-4.140778,-7.170339,9.887501,-6.494847,-6.863072,-0.148056,0.568345,1.285634,-5.134065,0.422516,-8.612329,-3.252155,1.265663,3.592683,-8.669348,7.726683,-4.270834,-0.567463,9.019100,-3.352139,1.686438,8.552789,4.086864,5.704313,-3.677306,-1.209559,-1.871012,-9.626765,-5.842188,4.470469,-4.449251,6.455364,4.123900,-7.363198,-1.565666,-9.459996,0.226453,-5.990135,-4.621881,-7.857198,-4.105652,6.124458,9.581775,-2.779198,6.937904,7.285724,-1.682372,5.850805,-7.325700,-0.200103,-3.197019,-6.378407,2.319574,0.113621,-6.961527,-1.708370,-2.783117,5.392910,-9.655815,9.867292,-8.231539,4.513779,3.595428,-2.327734,8.632226,-7.579897,4.456480,5.034440,6.956165,4.834046,5.084116,0.373009,6.242424,8.225331,-7.919473,-5.934063,0.177810,-6.921084,-1.103463,-4.582867,7.215782,3.541734,1.269280,1.564345,9.076504,7.794550,5.802456,-0.411128,2.037887,-5.485814,-8.565456,-2.682622,-4.527487,-5.968703,0.608262,-3.952242,7.085670,-4.633057,6.782773,-4.778743,-0.599677,9.714150,-4.162374,-4.195815,1.525100,4.295610,2.582777,-6.175678,-5.090617,-1.908005,6.862190,2.883951,2.210559,-4.531453,1.173029,0.169932,-0.416766,1.806166,4.363452,-9.660225,-6.735394,-6.590685,-4.261582,-1.435158,-5.272259,-3.300663,4.261761,-8.188285,0.097449,6.900062,4.376536,-1.328222,0.058924,-0.218402,-0.724712,-4.871896,0.083025,-4.161870,6.100377,-6.211728,-7.535680,5.937158,-4.886175,-1.605291,-5.128238,0.155874,-7.026735,9.206045,9.277522,-9.776418,7.501431,7.026882,-5.771890,-0.308624,-8.208946,9.052371,1.681380,-5.187409,-4.596933,-6.060093,5.327944,5.755783,3.245595,4.343256,-7.168243,-5.663273,-9.732689,-6.065751,-9.774485,-6.477681,-6.458550,7.021108,6.380072,7.958843,-1.641305,-6.491889,2.535123,9.197167,5.213038,-3.752139,5.327472,0.640256,-4.607580,-3.607045,-1.025117,9.669736,-1.322971,-2.013790,-5.004913,4.672397,7.578395,-8.910624,0.801259,-5.260064,3.414046,8.894797,4.525871,-0.032009,-9.020760,-8.873242,-0.565742,0.162020,-4.904556,-2.699328,-5.990195,1.935755,3.117174,-4.687495,-8.704662,3.831806,8.075268,-8.143387,7.744806,-0.924459,1.608561,-9.009355,-9.863848,-1.728693,-9.931631,-9.315938,-4.249752,-7.764286,8.517213,5.989946,5.809155,2.464335,4.915918,-2.771335,3.215381,-0.981202,9.103714,-2.765864,4.008602,4.435318,5.066351,-7.224852,2.394674,8.775345,1.250797,-4.043122,-4.122168,-3.841470,1.015567,-9.107814,6.323121,9.330135,-6.607805,6.759760,-4.750589,0.145819,-7.627459,-4.803594,-8.824597,-2.962078,-2.217396,4.720039,9.907245,-5.689875,-8.291225,5.372784,5.467188,-6.758371,-1.400520,2.778972,-1.777864,-2.366504], dtype = "float64")#candidate|9332|(546,)|const|float64
call_9331 = func_3623_call(relay.reshape(const_9332.astype('float64'), [13, 14, 3]))
call_9333 = func_3623_call(relay.reshape(const_9332.astype('float64'), [13, 14, 3]))
func_1763_call = mod.get_global_var('func_1763')
func_1768_call = mutated_mod.get_global_var('func_1768')
var_9346 = relay.var("var_9346", dtype = "float32", shape = (180,))#candidate|9346|(180,)|var|float32
var_9347 = relay.var("var_9347", dtype = "int64", shape = (968,))#candidate|9347|(968,)|var|int64
var_9348 = relay.var("var_9348", dtype = "int64", shape = (182, 2))#candidate|9348|(182, 2)|var|int64
call_9345 = relay.TupleGetItem(func_1763_call(relay.reshape(var_9346.astype('float32'), [5, 9, 4]), relay.reshape(var_9347.astype('int64'), [968,]), relay.reshape(var_9348.astype('int64'), [364,]), ), 3)
call_9349 = relay.TupleGetItem(func_1768_call(relay.reshape(var_9346.astype('float32'), [5, 9, 4]), relay.reshape(var_9347.astype('int64'), [968,]), relay.reshape(var_9348.astype('int64'), [364,]), ), 3)
uop_9357 = relay.log2(call_9331.astype('float64')) # shape=(13, 14, 3)
uop_9359 = relay.log2(call_9333.astype('float64')) # shape=(13, 14, 3)
output = relay.Tuple([call_9310,const_9332,call_9345,var_9346,var_9347,var_9348,uop_9357,])
output2 = relay.Tuple([call_9311,const_9332,call_9349,var_9346,var_9347,var_9348,uop_9359,])
func_9360 = relay.Function([var_9346,var_9347,var_9348,], output)
mod['func_9360'] = func_9360
mod = relay.transform.InferType()(mod)
var_9361 = relay.var("var_9361", dtype = "float32", shape = (180,))#candidate|9361|(180,)|var|float32
var_9362 = relay.var("var_9362", dtype = "int64", shape = (968,))#candidate|9362|(968,)|var|int64
var_9363 = relay.var("var_9363", dtype = "int64", shape = (182, 2))#candidate|9363|(182, 2)|var|int64
output = func_9360(var_9361,var_9362,var_9363,)
func_9364 = relay.Function([var_9361,var_9362,var_9363,], output)
mutated_mod['func_9364'] = func_9364
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7376_call = mod.get_global_var('func_7376')
func_7378_call = mutated_mod.get_global_var('func_7378')
call_9407 = relay.TupleGetItem(func_7376_call(), 0)
call_9408 = relay.TupleGetItem(func_7378_call(), 0)
func_8070_call = mod.get_global_var('func_8070')
func_8077_call = mutated_mod.get_global_var('func_8077')
var_9411 = relay.var("var_9411", dtype = "float32", shape = (260,))#candidate|9411|(260,)|var|float32
var_9412 = relay.var("var_9412", dtype = "int64", shape = ())#candidate|9412|()|var|int64
const_9413 = relay.const([-1,-4,-10,-7,5,8,10,7,-2,-10,1,-3,-8,-5,3,8,2,2,5,5,-7,-5,8,5,-9,2,-5,-2,-6,-9,7,-3,-9,1,4,5,-10,-8,-4,-10,-6,-2,9,-5,-1,6,-4,-6,-3,9,6,-1,-6,-5,-2,1,1,-10,-9,7,-1,-9,1,-10,-4,-6,-2,-7,7,-9,8,6,5,-10,-3,4,10,-1,-9,-9,-7,-5,1,-9,5,7,10,-3,-1,9,1,-8,-7,6,-9,2,8,-6,9,-9,-3,-8,-10,-8,-5,3,-10,-9,-1,6,-9,-7,-6,-8,-8,9,-3,-4,9,2,-9,-2,-9,8,7,1,2,3,-2,-5,9,-4,3,5,-10,-6,5,9,-10,-5,1,-2,-7,1,9,-10,9,3,3,-4,7,3,-7,-8,-7,3,-1,1,2,-7,-9,9,2,2,10,-10,5,10,6,-10,-1,3,9,-1,-9,10,-5,7,-1,-5,-4,-7,-8,2,5,9,6,1,7,4,8,3,5,3,9,-6,-10,-4,9,4,-10,3,4,-1,6,6,-1,9,9,1,-9,2,9,-10,2,6,7,-9,-5,-4,6,-5,1,5,6,-9,-3,6,7,-4,-2,-2,-2,-1,-1,-6,-5,4,-6,7,6,-7,-8,-3,-1,-3,-9,-1,6,-10,7,4,8,9,8,6,-3,-3,7,6,-6,10,-6,8,3,8,3,-3,1,-5,-9,5,3,4,5,-8,1,-6,-9,8,2,3,10,-6,-9,4,-1,1,-6,-6,7,1,1,4,2,3,1,-7,1,4,4,7,6,1,-5,10,-10,1,-8,5,-10,-2,-6,2,4,-7,-3,-6,-6,-8,4,4,-10,-7,-3,-6,3,-4,9,-6,1,3,-10,4,6,7,-1,-5,-10,-9,7,6,5,6,-3,9,6,9,-9,-1,4,-6,-1,-7,-3,1,-4,-7,6,-5,6,2,-5,9], dtype = "int64")#candidate|9413|(364,)|const|int64
const_9414 = relay.const([-10,8,-3,-5,1,7,-8,-9,-9,10,4,7,-9,9,8,-8,3,4,-6,-6,-9,-8,-3,-5,4,8,1,-7,10,8,10,-6,-1,-8,-1,3,9,-10,10,9,-1,3,-4,4,-6,4,8,2,-2,8,7,7,5,-2,-1,1,8,3,4,-8,10,10,-3,9,3,1,1,7,3,2,-10,7,-5,-10,8,1,9,9,-4,-7,8,-6,-8,-6,2,-7,1,10,4,6,5,1,-9,-6,-9,-9,-3,-7,-7,1,2,-4,2,8,-4,-10,-2,-5,-1,3,5,8,-4,-8,9,4,9,-4,-4,9,-7,-6,-9,-9,3,-10,-1,-6,-3,-9,4,-4,3,-6,-10,-2,-3,7,1,-4,-7,3,-3,4,3,-10,9,2,4,7,-4,-3,9,-10,-6,-5,9,1,-6,9,2,-8,3,-3,9,-1,10,1,5,-10,-8,-4,-6,8,-3,3,6,6,-1,-6,-8,-5,-2,8,10,8,6,4,8,3,-10,-7,-8,-8,2,1,-5,-10,3,-6,-9,-8,6,-6,5,-8,-8,1,-7,-4,5,1,-10,-6,-9,5,-7,-5,-6,-9,-2,3,-1,-5,5,7,3,-1,7,9,2,-5,8,3,-1,-2,-1,-5,3,-1,7,10,6,-6,-1,-10,-8,9,7,9,-6,2,-8,-8,-7,1,6,8,5,6,1,-6,-3,5,8,-7,-7,-2,6,-7,-10,8,2,-10,10,-2,10,-9,4,2,-10,-6,7,-3,7,-7,2,5,-1,-2,8,3,-3,-2,8,9,-2,6,-3,4,3,-7,7,9,-4,3,7,2,8,-7,8,6,-10,-9,3,3,5,3,1,-3,4,-8,10,1,6,6,-5,-3,-5,8,-6,-8,-2,-4,-2,1,-3,-7,1,-2,-7,2,-9,6,9,-5,-6,7,-1,-2,-10,-9,2,-5,-5,1,-3,5,-9,-7,-5,-5,-5,-1,-5,-9,6,9,5,4,-1,3,9,10,-9,8,1,-8,-8,-1,2,10,-10,-9,-3,7,7,1,-8,-5,8,-4,9,-3,1,-1,-8,2,-10,-4,-1,8,-1,-5,10,9,-5,6,2,-10,7,-5,-4,2,-5,8,7,5,7,-8,-2,-4,7,1,-3,-4,4,-5,6,2,-6,-1,-6,-1,-6,7,-4,-5,3,2,-8,-6,6,9,-1,-7,-9,7,5,-8,7,-9,8,-1,1,-9,-2,9,6,-1,-9,1,-7,5,8,-2,-1,-5,-6,-2,-4,6,-3,5,3,6,6,-1,-10,4,-2,-5,7,1,-8,2,1,-9,3,4,10,1,9,-9,-10,7,7,-2,1,10,4,3,-2,-10,6,2,-5,-2,-4,-1,3,-4,-9,-7,-2,2,-10,3,-9,6,10,1,-10,-10,-3,-9,-1,9,3,-10,2,1,9,6,9,-3,-10,4,7,-6,-5,1,8,-5,3,-6,-9,10,2,-6,-8,2,3,-9,2,-5,10,4,-3,1,-4,4,5,-1,-8,10,6,-5,1,-1,9,1,-1,7,2,1,-4,-1,-7,-6,1,-2,-1,6,-10,5,3,9,9,-8,-6,8,4,-9,-4,-9,-2,-2,7,-4,-4,-8,-7,1,-5,-8,9,-10,-7,-5,3,-6,4,-7,3,-10,2,-6,-7,6,7,2,2,-1,9,10,10,7,3,5,-7,4,4,-8,-10,-2,10,5,6,-1,-1,-8,-8,-5,9,10,6,5,6,1,-2,3,7,-2,-3,7,-7,-7,10,-7,-3,-6,2,8,-7,-4,-2,-8,6,-1,6,-4,-2,9,2,-10,-4,-5,8,-4,4,5,-4,4,-7,-10,-2,-6,-5,6,-5,-4,3,-5,5,-9,7,7,-6,-3,8,6,8,-4,-10,-2,-7,2,-8,-2,-6,3,4,7,3,-5,-3,-10,-6,6,5,9,-4,3,-9,6,7,-1,9,2,-7,-2,-9,-3,-9,1,7,-5,2,-3,-4,-8,-8,3,-6,9,4,-6,-4,-10,-10,-6,-10,5,10,2,-9,-4,-7,4,1,-9,-5,-10,5,-1,-10,9,-7,-1,-6,-10,1,-2,10,-2,-1,8,7,4,-9,-5,9,8,-10,-2,1,-1,-5,-1,-1,6,5,8,1,3,7,8,4,4,6,-10,10,-1,4,-10,8,-9,-1,6,8,-3,-7,-3,-8,5,-2,2,6,-7,-7,5,4,-10,-10,-6,-6,-5,9,-4,-2,-2,3,8,-9,-10,-1,-2,1,-9,-8,1,-5,5,-4,-10,9,3,-8,-3,-6,-3,-2,-2,-7,-5,-10,-7,5,-7,-2,-7,1,-6,1,-3,-4,3,-1,8,8,3,4,-10,-3,-9,-8,-9,-6,-7], dtype = "uint16")#candidate|9414|(880,)|const|uint16
var_9415 = relay.var("var_9415", dtype = "float32", shape = (180,))#candidate|9415|(180,)|var|float32
const_9416 = relay.const([[-8.106961,-5.910846,0.360073,3.521737,-6.324244,5.549675,-6.899994,-9.362068,7.914822,-1.020016,1.198290,8.944646,-9.007422,-0.714039,6.864920,0.021221,-4.985374,-4.856436,-9.930517,3.561356,-9.495933,9.271685,1.495752,-0.203873,4.690458,-0.660920,0.030385,-1.212129,6.464100,-4.686362,0.915409,-1.062952,-2.200933,3.612512,-7.361617,0.684400,-8.015838,-5.972565,-5.973169,-6.511444,9.770893,-8.489803,9.668601,-2.601196,5.472983,0.147656,6.262505,-0.996816,0.885056,-0.259229,3.382026,-6.384769,1.921484,1.706611,0.868066,4.332616,-3.265148,-4.732366,-3.375106,-2.827034,4.663757,2.819626,3.731219,-2.998546,5.748455,7.957097,-2.027361,-7.424046,-8.759967,4.133937,-9.318111,-1.636545,-9.305097,-3.325573,-2.897215,-8.391519,-8.027702,-8.846059,-0.987860,-5.287881,8.228074,-0.040916,-6.802482,1.838020,-0.949012,-1.352072,-7.076168,9.553947],[3.987256,5.904738,5.150469,-4.606220,4.209448,7.831311,3.876368,-7.409342,0.749020,8.880849,5.930379,-2.913473,2.758254,-2.313266,-5.233171,3.065390,1.995384,0.084006,-5.737084,7.544559,-6.561274,8.384753,-8.028625,-8.762783,-1.427754,7.526776,1.216655,5.037035,6.206967,-2.536359,-4.495240,4.700915,-6.981193,-9.907272,-7.139819,8.490768,-8.984320,4.958695,-2.300578,6.240544,0.070558,-7.706263,-3.198539,5.799031,-0.088059,5.154924,7.947811,-6.384616,3.908408,6.633098,-1.127579,-6.969731,6.844873,-2.057650,-8.071655,2.607837,-6.400821,-9.051232,5.190424,-2.341281,4.908788,-9.347130,4.275481,-6.940872,8.371564,-7.306773,-6.389142,6.067292,-6.504862,8.379229,0.964741,-7.225226,7.857872,-3.587340,0.448927,-6.768616,7.938317,2.178266,3.902617,5.982420,9.948093,1.674169,9.470841,-7.090163,-6.961748,-4.104287,-0.559931,2.476479],[4.073039,-1.485582,4.459661,7.570129,-0.416936,4.567692,-8.571847,-7.206907,-2.610647,-4.044168,-9.468225,-1.782019,-3.609615,-7.452010,8.967977,-5.843505,-8.714675,7.359799,8.212075,-2.579924,-7.628541,-2.322286,-2.837587,-0.620075,-0.845402,-7.273863,7.959325,3.273866,5.027681,-4.935209,3.736194,8.492517,-0.206728,0.823971,1.766670,5.187627,0.992664,1.690319,-7.880274,4.101023,-9.483634,-0.386083,-6.276778,2.190249,9.044701,-7.500968,8.893524,-6.952887,7.598820,1.494615,9.934447,-7.065081,-1.622193,8.645085,6.079380,9.502647,-5.484510,-7.206807,1.541101,3.184665,8.344192,-7.012909,0.016446,-8.634308,-3.431731,-3.849649,-5.132666,5.605552,-4.350517,-0.912033,9.556555,1.464802,6.560635,-5.137919,0.897896,4.296354,5.491813,7.511783,1.980201,2.187841,-3.078994,6.527194,-3.212233,6.594859,4.553247,9.864699,-2.203508,6.633598],[-3.988283,-4.660377,4.376089,-4.743949,3.576935,8.983380,-4.452323,7.090391,-1.997376,5.202506,2.603350,7.451581,-7.392863,1.241734,1.778561,-6.247592,-6.955059,-1.938613,1.326513,-3.888877,-3.609617,2.757928,4.050151,4.333434,1.631584,-9.908633,-7.096628,-8.127014,-9.662142,6.139199,-5.641931,2.328316,-4.684194,-6.680822,1.134838,6.861428,-3.340304,-3.142343,3.119919,-8.098971,-0.512710,0.507167,-6.560874,-5.719172,3.017680,9.050099,3.567734,-0.999707,-1.447413,8.929716,6.070789,8.168941,7.540779,7.247951,-5.787612,-6.662916,5.942177,0.491520,2.216775,-7.498330,5.838251,-9.630774,6.274879,-8.632658,8.581266,3.123802,-3.939054,-8.599742,-8.036718,-7.124600,7.263663,5.822752,-8.638907,0.691340,-3.880389,-5.563688,2.145650,0.038753,8.832387,-8.426850,7.726690,-3.463988,-5.890776,-6.695192,-8.032632,2.031694,7.669404,-3.459721],[3.310639,4.501907,-9.400442,3.114561,-7.082373,-9.343140,7.991681,-8.089621,-7.664143,-7.242547,8.934357,2.737942,-4.566681,-1.248461,3.853486,1.672917,-5.758765,0.256767,1.667263,-4.357558,9.434313,1.250214,1.351327,7.038669,-4.895276,-3.078469,-1.841879,-6.545222,6.100505,-9.825741,9.336444,6.919024,-5.029559,-0.822114,-9.008905,0.143616,4.164317,-8.820159,-1.753450,-3.584607,7.025248,5.883389,-0.396493,-2.446569,-4.015562,3.901014,4.987848,5.095104,8.281755,7.428595,-2.170067,1.790938,6.963741,-3.438599,0.193357,5.489795,9.521881,8.536571,-9.044165,8.398370,-9.329739,-7.657057,-4.147281,-1.853457,-8.407894,3.560567,-4.402656,-8.195171,-1.430565,-7.500327,-3.853628,-0.174209,-5.895952,7.491545,-7.707543,8.778820,5.781699,-6.342122,9.702682,4.475758,-1.754234,-4.472802,0.601378,-0.181365,2.023956,-5.751630,-7.404067,4.111523],[-6.938917,3.526809,-9.682223,9.410161,6.807202,2.221916,-0.248382,-5.180573,4.007168,-4.155944,3.739277,-3.420860,8.352072,-5.463705,2.616945,-7.522383,1.190310,-6.311232,-9.511236,5.632971,8.220861,-8.829104,-6.780334,-1.645602,2.850508,-7.862389,-2.106928,7.936548,7.239587,2.158202,5.102744,-5.147051,-3.965845,-9.696733,8.974232,-6.301874,-0.203883,-8.765302,0.544761,-0.149770,3.528040,4.668837,2.435167,7.755564,8.581000,-0.720367,-3.272669,3.871047,4.751997,3.524810,5.464812,-2.329863,-1.401122,-7.039480,5.863494,-5.116631,-2.313333,-6.648226,-5.809723,-2.968193,6.197296,0.165743,-1.857071,-5.765840,-0.089716,-2.468844,1.297357,-0.108211,9.051628,0.963479,5.208723,-6.268643,6.480451,-9.931290,-8.493149,0.630642,8.784437,-7.691618,3.343522,1.427912,-8.555608,-0.553702,-4.832124,-2.114676,1.041343,5.920183,7.199681,-9.077738],[-7.569122,9.298909,-3.331236,-4.776256,9.154762,2.656503,4.694207,-9.287942,-2.629419,8.454623,4.352490,-1.549408,4.252708,-8.349216,8.967067,-1.727161,3.669314,3.027794,-4.314141,9.031220,-4.525593,4.433792,5.236403,1.793788,-2.489628,2.974071,-4.449867,-6.792570,4.824245,7.452525,-7.100074,-9.307808,4.549414,8.490841,-4.257612,1.149817,3.884322,-1.609745,-2.334577,-3.360935,6.844467,6.341554,9.313364,0.417065,-4.498172,-2.641671,-8.293388,-6.363530,-9.586361,-4.347640,-6.877460,3.849594,-6.306940,-8.153049,9.640648,3.976486,-9.017428,2.087222,-4.162004,-5.631076,6.326364,8.451007,-3.060115,1.598941,6.352377,6.232510,6.163182,8.794962,-6.909894,-6.736910,-1.765760,-5.837844,-3.339458,4.838165,5.290252,1.889563,-1.561303,-5.556868,-8.357411,8.823298,6.947721,4.571663,9.978755,-7.323083,3.781905,5.982906,-5.168836,-5.478965],[2.158131,-9.386867,-1.713908,5.326904,-3.636069,6.997384,2.718833,7.345612,9.107476,7.712881,8.812218,-1.757008,6.533963,1.965543,-9.300410,-5.396796,9.089371,-9.047088,9.439255,-0.315911,5.427331,-6.545430,-6.802562,-8.467010,7.462329,-7.267420,0.048505,9.504433,-4.105520,5.694202,-5.177876,5.963397,-2.495223,9.506876,7.554303,2.639628,5.676269,-0.500948,8.872559,7.385891,-6.393364,-3.382360,2.555967,-0.706305,-1.298769,-7.264357,-6.917055,-7.489054,3.229940,-4.999428,3.181701,1.154239,3.019565,-2.635964,-6.358534,6.115227,9.764946,1.095738,6.152840,-5.512571,9.025037,7.305552,-2.954780,-0.399813,4.986368,8.081610,-4.118309,-1.636562,-9.662192,3.365325,-2.248889,7.334078,-8.237467,-4.688247,1.751128,1.398192,7.740136,-5.383019,-5.084806,1.812577,4.140559,-2.966565,-4.012873,1.199131,6.817930,4.039417,-5.941707,2.492375]], dtype = "float64")#candidate|9416|(8, 88)|const|float64
call_9410 = relay.TupleGetItem(func_8070_call(relay.reshape(var_9411.astype('float32'), [260,]), relay.reshape(var_9412.astype('int64'), []), relay.reshape(const_9413.astype('int64'), [364,]), relay.reshape(const_9414.astype('uint16'), [880,]), relay.reshape(var_9415.astype('float32'), [180,]), relay.reshape(const_9416.astype('float64'), [352, 2]), ), 5)
call_9417 = relay.TupleGetItem(func_8077_call(relay.reshape(var_9411.astype('float32'), [260,]), relay.reshape(var_9412.astype('int64'), []), relay.reshape(const_9413.astype('int64'), [364,]), relay.reshape(const_9414.astype('uint16'), [880,]), relay.reshape(var_9415.astype('float32'), [180,]), relay.reshape(const_9416.astype('float64'), [352, 2]), ), 5)
output = relay.Tuple([call_9407,call_9410,var_9411,var_9412,const_9413,const_9414,var_9415,const_9416,])
output2 = relay.Tuple([call_9408,call_9417,var_9411,var_9412,const_9413,const_9414,var_9415,const_9416,])
func_9423 = relay.Function([var_9411,var_9412,var_9415,], output)
mod['func_9423'] = func_9423
mod = relay.transform.InferType()(mod)
var_9424 = relay.var("var_9424", dtype = "float32", shape = (260,))#candidate|9424|(260,)|var|float32
var_9425 = relay.var("var_9425", dtype = "int64", shape = ())#candidate|9425|()|var|int64
var_9426 = relay.var("var_9426", dtype = "float32", shape = (180,))#candidate|9426|(180,)|var|float32
output = func_9423(var_9424,var_9425,var_9426,)
func_9427 = relay.Function([var_9424,var_9425,var_9426,], output)
mutated_mod['func_9427'] = func_9427
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6678_call = mod.get_global_var('func_6678')
func_6680_call = mutated_mod.get_global_var('func_6680')
call_9543 = relay.TupleGetItem(func_6678_call(), 0)
call_9544 = relay.TupleGetItem(func_6680_call(), 0)
func_6678_call = mod.get_global_var('func_6678')
func_6680_call = mutated_mod.get_global_var('func_6680')
call_9554 = relay.TupleGetItem(func_6678_call(), 0)
call_9555 = relay.TupleGetItem(func_6680_call(), 0)
func_6187_call = mod.get_global_var('func_6187')
func_6188_call = mutated_mod.get_global_var('func_6188')
call_9566 = relay.TupleGetItem(func_6187_call(), 0)
call_9567 = relay.TupleGetItem(func_6188_call(), 0)
func_8619_call = mod.get_global_var('func_8619')
func_8620_call = mutated_mod.get_global_var('func_8620')
call_9568 = relay.TupleGetItem(func_8619_call(), 1)
call_9569 = relay.TupleGetItem(func_8620_call(), 1)
func_6536_call = mod.get_global_var('func_6536')
func_6538_call = mutated_mod.get_global_var('func_6538')
call_9573 = relay.TupleGetItem(func_6536_call(), 0)
call_9574 = relay.TupleGetItem(func_6538_call(), 0)
output = relay.Tuple([call_9543,call_9554,call_9566,call_9568,call_9573,])
output2 = relay.Tuple([call_9544,call_9555,call_9567,call_9569,call_9574,])
func_9576 = relay.Function([], output)
mod['func_9576'] = func_9576
mod = relay.transform.InferType()(mod)
output = func_9576()
func_9577 = relay.Function([], output)
mutated_mod['func_9577'] = func_9577
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5717_call = mod.get_global_var('func_5717')
func_5718_call = mutated_mod.get_global_var('func_5718')
call_9626 = relay.TupleGetItem(func_5717_call(), 0)
call_9627 = relay.TupleGetItem(func_5718_call(), 0)
func_7844_call = mod.get_global_var('func_7844')
func_7846_call = mutated_mod.get_global_var('func_7846')
call_9638 = func_7844_call()
call_9639 = func_7844_call()
func_7447_call = mod.get_global_var('func_7447')
func_7448_call = mutated_mod.get_global_var('func_7448')
call_9642 = relay.TupleGetItem(func_7447_call(), 0)
call_9643 = relay.TupleGetItem(func_7448_call(), 0)
func_504_call = mod.get_global_var('func_504')
func_507_call = mutated_mod.get_global_var('func_507')
const_9645 = relay.const([[False,True,False,True,False,True,True,True,True,True,True,False,False,True,False,True,False,False,False,True,True,True,False,True,True,False,False,True,False,True,False,True,True,True,False,True,False,True,False,True,False,False,False,True,True,False,False,True,False,True,False,False,False,True,True],[False,True,False,True,True,True,False,False,False,True,False,False,True,False,False,False,False,False,False,True,True,False,False,False,True,True,True,True,True,False,False,True,True,False,True,False,False,True,True,False,False,True,False,True,True,True,True,False,True,False,True,True,False,True,True],[True,False,False,False,False,False,True,True,True,True,False,False,True,True,True,False,True,False,False,False,False,True,False,False,True,False,True,False,False,True,True,False,True,False,False,True,False,True,True,False,True,True,False,False,True,True,False,False,True,True,True,True,False,True,True],[True,True,True,True,True,False,True,True,True,True,False,True,True,True,False,True,False,True,True,True,False,False,True,True,False,False,False,True,True,True,True,False,False,False,False,True,False,True,True,True,False,True,False,True,False,False,True,True,False,False,False,False,True,True,True],[True,False,True,False,True,False,True,True,False,True,True,False,True,False,True,True,False,False,True,False,False,False,True,True,False,True,True,False,False,True,False,True,True,True,False,False,False,True,True,False,True,True,False,False,True,True,True,False,True,True,False,False,True,True,True],[True,False,True,True,True,False,True,False,True,True,False,True,True,False,False,True,True,True,False,True,True,True,True,True,True,False,True,True,True,False,False,False,False,True,True,True,True,True,False,False,False,False,True,True,False,False,False,True,True,False,True,False,False,False,True],[True,False,False,False,True,False,False,True,True,False,False,False,True,True,False,False,True,True,True,False,True,True,True,True,True,True,False,True,True,False,True,False,False,True,False,True,False,True,False,True,True,False,True,False,False,False,False,True,True,False,False,False,True,True,True],[False,False,True,False,False,True,True,False,True,False,True,False,False,False,False,True,True,True,True,True,True,True,False,False,False,False,False,False,True,True,False,False,False,True,False,False,True,True,False,False,True,True,True,False,True,True,True,False,False,False,False,True,True,False,False],[True,False,False,False,True,False,False,True,False,True,True,False,False,False,False,True,False,False,False,False,True,True,True,False,False,False,False,True,True,False,True,True,False,False,True,True,False,True,True,False,False,False,False,True,True,False,False,True,False,False,True,False,True,False,False],[True,False,False,True,False,False,False,True,False,False,False,True,False,True,False,False,True,True,False,False,False,True,False,True,True,False,False,True,False,False,True,True,True,True,False,True,True,True,False,True,True,False,True,False,True,True,False,False,False,True,True,False,False,True,True],[True,False,True,True,False,False,False,True,True,False,False,False,True,True,False,True,False,False,False,False,True,True,True,True,False,False,False,False,False,False,False,True,False,True,False,False,True,True,True,False,True,True,False,False,False,False,True,True,False,True,True,True,True,False,True],[True,False,True,True,False,True,True,False,True,True,False,True,False,True,True,True,False,False,True,True,True,False,False,False,False,False,True,False,True,False,True,False,False,False,True,True,False,True,True,True,False,True,True,False,True,False,True,True,False,True,False,True,True,True,True],[True,True,True,True,False,True,False,False,True,True,True,False,True,False,True,False,False,True,True,True,False,True,False,True,False,True,False,True,False,True,True,False,False,False,True,False,True,False,False,False,True,True,True,False,False,False,False,False,True,False,True,True,True,False,True]], dtype = "bool")#candidate|9645|(13, 55)|const|bool
call_9644 = relay.TupleGetItem(func_504_call(relay.reshape(const_9645.astype('bool'), [11, 5, 13])), 0)
call_9646 = relay.TupleGetItem(func_507_call(relay.reshape(const_9645.astype('bool'), [11, 5, 13])), 0)
output = relay.Tuple([call_9626,call_9638,call_9642,call_9644,const_9645,])
output2 = relay.Tuple([call_9627,call_9639,call_9643,call_9646,const_9645,])
func_9649 = relay.Function([], output)
mod['func_9649'] = func_9649
mod = relay.transform.InferType()(mod)
mutated_mod['func_9649'] = func_9649
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9649_call = mutated_mod.get_global_var('func_9649')
call_9650 = func_9649_call()
output = call_9650
func_9651 = relay.Function([], output)
mutated_mod['func_9651'] = func_9651
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8246_call = mod.get_global_var('func_8246')
func_8247_call = mutated_mod.get_global_var('func_8247')
call_9655 = func_8246_call()
call_9656 = func_8246_call()
output = call_9655
output2 = call_9656
func_9674 = relay.Function([], output)
mod['func_9674'] = func_9674
mod = relay.transform.InferType()(mod)
output = func_9674()
func_9675 = relay.Function([], output)
mutated_mod['func_9675'] = func_9675
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9226_call = mod.get_global_var('func_9226')
func_9227_call = mutated_mod.get_global_var('func_9227')
call_9749 = func_9226_call()
call_9750 = func_9226_call()
output = relay.Tuple([call_9749,])
output2 = relay.Tuple([call_9750,])
func_9755 = relay.Function([], output)
mod['func_9755'] = func_9755
mod = relay.transform.InferType()(mod)
mutated_mod['func_9755'] = func_9755
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9755_call = mutated_mod.get_global_var('func_9755')
call_9756 = func_9755_call()
output = call_9756
func_9757 = relay.Function([], output)
mutated_mod['func_9757'] = func_9757
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9119_call = mod.get_global_var('func_9119')
func_9120_call = mutated_mod.get_global_var('func_9120')
call_9785 = func_9119_call()
call_9786 = func_9119_call()
output = call_9785
output2 = call_9786
func_9808 = relay.Function([], output)
mod['func_9808'] = func_9808
mod = relay.transform.InferType()(mod)
mutated_mod['func_9808'] = func_9808
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9808_call = mutated_mod.get_global_var('func_9808')
call_9809 = func_9808_call()
output = call_9809
func_9810 = relay.Function([], output)
mutated_mod['func_9810'] = func_9810
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7447_call = mod.get_global_var('func_7447')
func_7448_call = mutated_mod.get_global_var('func_7448')
call_9814 = relay.TupleGetItem(func_7447_call(), 0)
call_9815 = relay.TupleGetItem(func_7448_call(), 0)
output = call_9814
output2 = call_9815
func_9863 = relay.Function([], output)
mod['func_9863'] = func_9863
mod = relay.transform.InferType()(mod)
output = func_9863()
func_9864 = relay.Function([], output)
mutated_mod['func_9864'] = func_9864
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7639_call = mod.get_global_var('func_7639')
func_7641_call = mutated_mod.get_global_var('func_7641')
call_9981 = relay.TupleGetItem(func_7639_call(), 2)
call_9982 = relay.TupleGetItem(func_7641_call(), 2)
func_9649_call = mod.get_global_var('func_9649')
func_9651_call = mutated_mod.get_global_var('func_9651')
call_9988 = relay.TupleGetItem(func_9649_call(), 0)
call_9989 = relay.TupleGetItem(func_9651_call(), 0)
output = relay.Tuple([call_9981,call_9988,])
output2 = relay.Tuple([call_9982,call_9989,])
func_9990 = relay.Function([], output)
mod['func_9990'] = func_9990
mod = relay.transform.InferType()(mod)
output = func_9990()
func_9991 = relay.Function([], output)
mutated_mod['func_9991'] = func_9991
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7929_call = mod.get_global_var('func_7929')
func_7930_call = mutated_mod.get_global_var('func_7930')
call_10008 = func_7929_call()
call_10009 = func_7929_call()
output = relay.Tuple([call_10008,])
output2 = relay.Tuple([call_10009,])
func_10022 = relay.Function([], output)
mod['func_10022'] = func_10022
mod = relay.transform.InferType()(mod)
mutated_mod['func_10022'] = func_10022
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10022_call = mutated_mod.get_global_var('func_10022')
call_10023 = func_10022_call()
output = call_10023
func_10024 = relay.Function([], output)
mutated_mod['func_10024'] = func_10024
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6678_call = mod.get_global_var('func_6678')
func_6680_call = mutated_mod.get_global_var('func_6680')
call_10025 = relay.TupleGetItem(func_6678_call(), 0)
call_10026 = relay.TupleGetItem(func_6680_call(), 0)
func_9808_call = mod.get_global_var('func_9808')
func_9810_call = mutated_mod.get_global_var('func_9810')
call_10030 = func_9808_call()
call_10031 = func_9808_call()
func_7711_call = mod.get_global_var('func_7711')
func_7713_call = mutated_mod.get_global_var('func_7713')
var_10035 = relay.var("var_10035", dtype = "float64", shape = (480,))#candidate|10035|(480,)|var|float64
call_10034 = relay.TupleGetItem(func_7711_call(relay.reshape(var_10035.astype('float64'), [480,])), 1)
call_10036 = relay.TupleGetItem(func_7713_call(relay.reshape(var_10035.astype('float64'), [480,])), 1)
output = relay.Tuple([call_10025,call_10030,call_10034,var_10035,])
output2 = relay.Tuple([call_10026,call_10031,call_10036,var_10035,])
func_10046 = relay.Function([var_10035,], output)
mod['func_10046'] = func_10046
mod = relay.transform.InferType()(mod)
var_10047 = relay.var("var_10047", dtype = "float64", shape = (480,))#candidate|10047|(480,)|var|float64
output = func_10046(var_10047)
func_10048 = relay.Function([var_10047], output)
mutated_mod['func_10048'] = func_10048
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6025_call = mod.get_global_var('func_6025')
func_6026_call = mutated_mod.get_global_var('func_6026')
call_10059 = relay.TupleGetItem(func_6025_call(), 0)
call_10060 = relay.TupleGetItem(func_6026_call(), 0)
output = call_10059
output2 = call_10060
func_10061 = relay.Function([], output)
mod['func_10061'] = func_10061
mod = relay.transform.InferType()(mod)
mutated_mod['func_10061'] = func_10061
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10061_call = mutated_mod.get_global_var('func_10061')
call_10062 = func_10061_call()
output = call_10062
func_10063 = relay.Function([], output)
mutated_mod['func_10063'] = func_10063
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8670_call = mod.get_global_var('func_8670')
func_8671_call = mutated_mod.get_global_var('func_8671')
call_10106 = relay.TupleGetItem(func_8670_call(), 0)
call_10107 = relay.TupleGetItem(func_8671_call(), 0)
output = relay.Tuple([call_10106,])
output2 = relay.Tuple([call_10107,])
func_10120 = relay.Function([], output)
mod['func_10120'] = func_10120
mod = relay.transform.InferType()(mod)
output = func_10120()
func_10121 = relay.Function([], output)
mutated_mod['func_10121'] = func_10121
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8448_call = mod.get_global_var('func_8448')
func_8449_call = mutated_mod.get_global_var('func_8449')
call_10136 = relay.TupleGetItem(func_8448_call(), 0)
call_10137 = relay.TupleGetItem(func_8449_call(), 0)
output = relay.Tuple([call_10136,])
output2 = relay.Tuple([call_10137,])
func_10138 = relay.Function([], output)
mod['func_10138'] = func_10138
mod = relay.transform.InferType()(mod)
mutated_mod['func_10138'] = func_10138
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10138_call = mutated_mod.get_global_var('func_10138')
call_10139 = func_10138_call()
output = call_10139
func_10140 = relay.Function([], output)
mutated_mod['func_10140'] = func_10140
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9755_call = mod.get_global_var('func_9755')
func_9757_call = mutated_mod.get_global_var('func_9757')
call_10180 = relay.TupleGetItem(func_9755_call(), 0)
call_10181 = relay.TupleGetItem(func_9757_call(), 0)
output = call_10180
output2 = call_10181
func_10245 = relay.Function([], output)
mod['func_10245'] = func_10245
mod = relay.transform.InferType()(mod)
mutated_mod['func_10245'] = func_10245
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10245_call = mutated_mod.get_global_var('func_10245')
call_10246 = func_10245_call()
output = call_10246
func_10247 = relay.Function([], output)
mutated_mod['func_10247'] = func_10247
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8600_call = mod.get_global_var('func_8600')
func_8601_call = mutated_mod.get_global_var('func_8601')
call_10292 = relay.TupleGetItem(func_8600_call(), 0)
call_10293 = relay.TupleGetItem(func_8601_call(), 0)
uop_10310 = relay.sigmoid(call_10292.astype('float64')) # shape=(15, 9, 6)
uop_10312 = relay.sigmoid(call_10293.astype('float64')) # shape=(15, 9, 6)
func_2768_call = mod.get_global_var('func_2768')
func_2771_call = mutated_mod.get_global_var('func_2771')
var_10314 = relay.var("var_10314", dtype = "float64", shape = (180,))#candidate|10314|(180,)|var|float64
call_10313 = func_2768_call(relay.reshape(var_10314.astype('float64'), [6, 15, 2]))
call_10315 = func_2768_call(relay.reshape(var_10314.astype('float64'), [6, 15, 2]))
output = relay.Tuple([uop_10310,call_10313,var_10314,])
output2 = relay.Tuple([uop_10312,call_10315,var_10314,])
func_10321 = relay.Function([var_10314,], output)
mod['func_10321'] = func_10321
mod = relay.transform.InferType()(mod)
var_10322 = relay.var("var_10322", dtype = "float64", shape = (180,))#candidate|10322|(180,)|var|float64
output = func_10321(var_10322)
func_10323 = relay.Function([var_10322], output)
mutated_mod['func_10323'] = func_10323
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5717_call = mod.get_global_var('func_5717')
func_5718_call = mutated_mod.get_global_var('func_5718')
call_10426 = relay.TupleGetItem(func_5717_call(), 0)
call_10427 = relay.TupleGetItem(func_5718_call(), 0)
func_8670_call = mod.get_global_var('func_8670')
func_8671_call = mutated_mod.get_global_var('func_8671')
call_10432 = relay.TupleGetItem(func_8670_call(), 0)
call_10433 = relay.TupleGetItem(func_8671_call(), 0)
output = relay.Tuple([call_10426,call_10432,])
output2 = relay.Tuple([call_10427,call_10433,])
func_10474 = relay.Function([], output)
mod['func_10474'] = func_10474
mod = relay.transform.InferType()(mod)
output = func_10474()
func_10475 = relay.Function([], output)
mutated_mod['func_10475'] = func_10475
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8246_call = mod.get_global_var('func_8246')
func_8247_call = mutated_mod.get_global_var('func_8247')
call_10476 = func_8246_call()
call_10477 = func_8246_call()
func_10022_call = mod.get_global_var('func_10022')
func_10024_call = mutated_mod.get_global_var('func_10024')
call_10486 = relay.TupleGetItem(func_10022_call(), 0)
call_10487 = relay.TupleGetItem(func_10024_call(), 0)
output = relay.Tuple([call_10476,call_10486,])
output2 = relay.Tuple([call_10477,call_10487,])
func_10501 = relay.Function([], output)
mod['func_10501'] = func_10501
mod = relay.transform.InferType()(mod)
mutated_mod['func_10501'] = func_10501
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10501_call = mutated_mod.get_global_var('func_10501')
call_10502 = func_10501_call()
output = call_10502
func_10503 = relay.Function([], output)
mutated_mod['func_10503'] = func_10503
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9119_call = mod.get_global_var('func_9119')
func_9120_call = mutated_mod.get_global_var('func_9120')
call_10547 = func_9119_call()
call_10548 = func_9119_call()
func_7231_call = mod.get_global_var('func_7231')
func_7234_call = mutated_mod.get_global_var('func_7234')
const_10552 = relay.const([-4,9,-8,10,5,7,3,-6,-5,-5,8,-6,-8,3,1,-3,6,-6,10,-2,-4,-8,-4,2,-5,-8,-2,2,-7,4,-2,3,-6,4,5,-3,-4,-9,-7,-8,5,-5,-2,-7,-9,-9,7,-1,-2,-10,-1,-9,-6,-3,-7,-5,-7,-1,9,-10,-8,-1,2,1,9,3,6,4,10,9,8,-2,-6,6,1,-4,-4,6,-7,1,8,-5,-8,10,-8,-7,-3,-3,-2,-4,4,3,-3,3,-6,5,10,2,-2,-6,-9,9,2,1,-1,-8,-3,3,10,3,2,-3,1,-2,8,-3,3,-9,8,-10,4,-3,8,2,-4,5,-4,-10,-6,8,-10,-10,-5,-9,-10,-1,4,-3,4,10,2,-5,8,1,-8,7,-2,-3,8,9,1,-6,7,-9,7,-8,7,-5,-1,-8,-7,-8,-1,-5,5,9,-5,-2,6,-3,3,2,-7,6,5,-4,8,-1,-5,10,-10,5,-5,8,-8,-4,2,-2,5,6,1,-2,2,-10,10,6,-8,-7,-7,4,-6,8,-6,-9,-8,1,-5,-8,6,3,-7,-8,-9,8,10,3,2,-5,2,7,7,9,1,-8,-7,-5,-3,1,-7,-7,-3,-2,4,3,-1,5,-8,-9,-4,-8,-1,5,-7,5,-7,3,-5,-7,4,4,-10,-3,-1,-9,-1,-6,-9,6,7,-2,-4,-6,-1,7,-1,-1,7,-9,-8,5,-5,-2,2,-2,7,-5,10,1,2,-9,8,4,-5,6,-3,-3,-2,5,-2,4,5,-2,1,-10,-1,8,10,7,-6,3,7,-10,-10,4,-5,3,10,-7,-1,3,-6,3,2,-5,6,10,3,-2,-6,-7,7,-1,9,5,4,4,-9,-10,-9,-1,-5,8,-2,3,9,9,3,-10,-9,-2,4,-7,-3,6,-5,6,-10,10,-5,10,-6,-9,-10,-1,3,-5,9,10,10,3,4,7,-6,-8,1,-4,-8,6,-1,10,-2,10,9,-5,-7,4,10,9,-8,6,6,6,4,-3,-9,-10,10,-2,2,-7], dtype = "int64")#candidate|10552|(390,)|const|int64
call_10551 = relay.TupleGetItem(func_7231_call(relay.reshape(call_10547.astype('float32'), [15, 9, 6]), relay.reshape(const_10552.astype('int64'), [5, 78]), ), 0)
call_10553 = relay.TupleGetItem(func_7234_call(relay.reshape(call_10547.astype('float32'), [15, 9, 6]), relay.reshape(const_10552.astype('int64'), [5, 78]), ), 0)
output = relay.Tuple([call_10547,call_10551,const_10552,])
output2 = relay.Tuple([call_10548,call_10553,const_10552,])
func_10585 = relay.Function([], output)
mod['func_10585'] = func_10585
mod = relay.transform.InferType()(mod)
output = func_10585()
func_10586 = relay.Function([], output)
mutated_mod['func_10586'] = func_10586
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10633 = relay.var("var_10633", dtype = "int16", shape = (5, 4, 11))#candidate|10633|(5, 4, 11)|var|int16
var_10634 = relay.var("var_10634", dtype = "int16", shape = (5, 4, 11))#candidate|10634|(5, 4, 11)|var|int16
bop_10635 = relay.right_shift(var_10633.astype('int16'), relay.reshape(var_10634.astype('int16'), relay.shape_of(var_10633))) # shape=(5, 4, 11)
output = bop_10635
output2 = bop_10635
func_10661 = relay.Function([var_10633,var_10634,], output)
mod['func_10661'] = func_10661
mod = relay.transform.InferType()(mod)
mutated_mod['func_10661'] = func_10661
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10661_call = mutated_mod.get_global_var('func_10661')
var_10663 = relay.var("var_10663", dtype = "int16", shape = (5, 4, 11))#candidate|10663|(5, 4, 11)|var|int16
var_10664 = relay.var("var_10664", dtype = "int16", shape = (5, 4, 11))#candidate|10664|(5, 4, 11)|var|int16
call_10662 = func_10661_call(var_10663,var_10664,)
output = call_10662
func_10665 = relay.Function([var_10663,var_10664,], output)
mutated_mod['func_10665'] = func_10665
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5560_call = mod.get_global_var('func_5560')
func_5561_call = mutated_mod.get_global_var('func_5561')
call_10704 = relay.TupleGetItem(func_5560_call(), 0)
call_10705 = relay.TupleGetItem(func_5561_call(), 0)
output = call_10704
output2 = call_10705
func_10727 = relay.Function([], output)
mod['func_10727'] = func_10727
mod = relay.transform.InferType()(mod)
mutated_mod['func_10727'] = func_10727
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10727_call = mutated_mod.get_global_var('func_10727')
call_10728 = func_10727_call()
output = call_10728
func_10729 = relay.Function([], output)
mutated_mod['func_10729'] = func_10729
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9649_call = mod.get_global_var('func_9649')
func_9651_call = mutated_mod.get_global_var('func_9651')
call_10880 = relay.TupleGetItem(func_9649_call(), 3)
call_10881 = relay.TupleGetItem(func_9651_call(), 3)
func_1763_call = mod.get_global_var('func_1763')
func_1768_call = mutated_mod.get_global_var('func_1768')
var_10903 = relay.var("var_10903", dtype = "float32", shape = (180,))#candidate|10903|(180,)|var|float32
var_10904 = relay.var("var_10904", dtype = "int64", shape = (968,))#candidate|10904|(968,)|var|int64
var_10905 = relay.var("var_10905", dtype = "int64", shape = (364,))#candidate|10905|(364,)|var|int64
call_10902 = relay.TupleGetItem(func_1763_call(relay.reshape(var_10903.astype('float32'), [5, 9, 4]), relay.reshape(var_10904.astype('int64'), [968,]), relay.reshape(var_10905.astype('int64'), [364,]), ), 2)
call_10906 = relay.TupleGetItem(func_1768_call(relay.reshape(var_10903.astype('float32'), [5, 9, 4]), relay.reshape(var_10904.astype('int64'), [968,]), relay.reshape(var_10905.astype('int64'), [364,]), ), 2)
func_10138_call = mod.get_global_var('func_10138')
func_10140_call = mutated_mod.get_global_var('func_10140')
call_10909 = relay.TupleGetItem(func_10138_call(), 0)
call_10910 = relay.TupleGetItem(func_10140_call(), 0)
func_1763_call = mod.get_global_var('func_1763')
func_1768_call = mutated_mod.get_global_var('func_1768')
call_10928 = relay.TupleGetItem(func_1763_call(relay.reshape(var_10903.astype('float32'), [5, 9, 4]), relay.reshape(var_10904.astype('int64'), [968,]), relay.reshape(call_10909.astype('int64'), [364,]), ), 2)
call_10929 = relay.TupleGetItem(func_1768_call(relay.reshape(var_10903.astype('float32'), [5, 9, 4]), relay.reshape(var_10904.astype('int64'), [968,]), relay.reshape(call_10909.astype('int64'), [364,]), ), 2)
output = relay.Tuple([call_10880,call_10902,var_10903,var_10904,var_10905,call_10909,call_10928,])
output2 = relay.Tuple([call_10881,call_10906,var_10903,var_10904,var_10905,call_10910,call_10929,])
func_10930 = relay.Function([var_10903,var_10904,var_10905,], output)
mod['func_10930'] = func_10930
mod = relay.transform.InferType()(mod)
var_10931 = relay.var("var_10931", dtype = "float32", shape = (180,))#candidate|10931|(180,)|var|float32
var_10932 = relay.var("var_10932", dtype = "int64", shape = (968,))#candidate|10932|(968,)|var|int64
var_10933 = relay.var("var_10933", dtype = "int64", shape = (364,))#candidate|10933|(364,)|var|int64
output = func_10930(var_10931,var_10932,var_10933,)
func_10934 = relay.Function([var_10931,var_10932,var_10933,], output)
mutated_mod['func_10934'] = func_10934
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6025_call = mod.get_global_var('func_6025')
func_6026_call = mutated_mod.get_global_var('func_6026')
call_10970 = relay.TupleGetItem(func_6025_call(), 0)
call_10971 = relay.TupleGetItem(func_6026_call(), 0)
func_7844_call = mod.get_global_var('func_7844')
func_7846_call = mutated_mod.get_global_var('func_7846')
call_10977 = func_7844_call()
call_10978 = func_7844_call()
output = relay.Tuple([call_10970,call_10977,])
output2 = relay.Tuple([call_10971,call_10978,])
func_10992 = relay.Function([], output)
mod['func_10992'] = func_10992
mod = relay.transform.InferType()(mod)
mutated_mod['func_10992'] = func_10992
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10992_call = mutated_mod.get_global_var('func_10992')
call_10993 = func_10992_call()
output = call_10993
func_10994 = relay.Function([], output)
mutated_mod['func_10994'] = func_10994
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8298_call = mod.get_global_var('func_8298')
func_8300_call = mutated_mod.get_global_var('func_8300')
call_11012 = func_8298_call()
call_11013 = func_8298_call()
output = relay.Tuple([call_11012,])
output2 = relay.Tuple([call_11013,])
func_11016 = relay.Function([], output)
mod['func_11016'] = func_11016
mod = relay.transform.InferType()(mod)
output = func_11016()
func_11017 = relay.Function([], output)
mutated_mod['func_11017'] = func_11017
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8600_call = mod.get_global_var('func_8600')
func_8601_call = mutated_mod.get_global_var('func_8601')
call_11062 = relay.TupleGetItem(func_8600_call(), 0)
call_11063 = relay.TupleGetItem(func_8601_call(), 0)
func_1763_call = mod.get_global_var('func_1763')
func_1768_call = mutated_mod.get_global_var('func_1768')
const_11090 = relay.const([-5.452754,-9.887413,4.753205,0.219543,-6.525706,-3.060200,-1.055890,3.676318,-2.804149,-5.059894,-6.013349,4.664696,7.975163,9.281208,-8.714061,-1.137007,-7.183934,2.440908,-5.900070,4.418630,-3.794925,0.337706,-5.145580,2.284610,7.239573,-9.428766,9.036911,6.989411,-0.158759,4.006498,-2.437631,-9.464137,-5.855012,-1.365885,-6.579195,2.873346,2.810311,1.052705,8.587049,5.789404,3.209223,4.605184,2.971227,7.639773,9.091044,-5.045100,-8.464815,4.074267,-4.108890,2.212518,0.664550,1.132032,-8.851732,-0.554772,9.936577,-8.236614,-9.566521,-2.169260,1.803894,3.384685,-4.754384,-1.805273,-9.680963,-5.215864,9.000072,6.936971,-8.352884,8.446060,-4.487774,5.449217,7.948603,-1.883859,4.250335,3.201494,-6.459307,7.410280,-7.088560,-8.426387,7.376467,8.665460,-1.156790,-3.913979,-3.022722,9.320890,2.178355,-1.622839,0.751501,-3.181508,2.195141,6.196312,4.426599,3.163954,-8.209925,-4.434742,-2.474196,-1.043891,0.612679,6.766975,-2.045183,-6.705033,8.340313,5.229571,4.265082,1.605049,8.133052,-0.054588,-7.944501,2.235604,8.479741,-1.273123,5.774352,6.744746,8.029128,-4.142113,9.113132,-5.517885,-0.468399,8.975373,5.082047,-8.646193,3.742290,1.192979,-6.871232,-5.215750,9.962480,7.588455,7.239849,8.090530,-0.123745,4.992327,-2.605044,-0.563578,3.911192,-7.701678,7.730174,2.354189,3.772257,-9.032306,4.262964,-7.118163,4.739865,-5.453697,-6.500788,-7.948021,9.297101,-7.306849,4.173859,-0.736934,4.715626,6.976292,-1.580921,7.719702,-0.855280,9.432751,1.290615,-4.379519,-7.917823,0.649487,-0.578847,4.176139,4.781156,0.420944,-8.918724,4.090446,-9.464688,-3.415041,-0.800683,-6.245269,1.219847,-7.063569,1.736593,-1.866304,9.923579,-8.189422,8.341239,-8.374294,-0.981751,9.677945,1.895198,-2.667949], dtype = "float32")#candidate|11090|(180,)|const|float32
const_11091 = relay.const([-4,-9,-1,-3,6,4,8,1,5,4,4,-9,-2,-8,5,-4,-8,10,-7,-4,-10,4,-10,-1,5,-5,1,-2,6,-5,-7,1,-3,5,-1,4,-5,3,-3,10,-2,-9,-2,5,10,8,1,1,10,4,4,5,6,7,-2,9,4,8,-8,-6,5,6,-3,7,-4,7,1,-7,9,8,1,-7,5,4,8,-2,4,-8,4,2,-8,-5,-10,6,8,-3,9,-7,7,8,1,-10,-5,-10,2,8,-1,-9,-9,10,-6,10,3,10,9,7,5,3,-4,2,6,-5,4,8,8,-3,-1,2,10,-5,-9,9,8,7,-8,7,8,3,-8,5,8,-10,3,-2,3,4,-10,9,6,7,2,9,5,-2,-2,-9,-9,1,3,4,3,-2,-2,8,-7,-3,-8,-1,-6,-8,-1,1,9,3,7,10,7,10,2,-9,-4,8,-7,-7,-1,3,3,4,-8,-4,4,5,-5,-1,3,-4,2,-9,10,-2,-2,-2,3,-8,3,-5,7,8,-5,9,-7,-4,-6,8,10,6,8,-8,-4,-1,-10,3,8,-1,8,-10,-6,6,9,9,-5,-1,3,-4,-8,1,3,7,-5,4,-2,-10,1,2,1,9,-4,-1,-2,3,1,-7,-10,-6,5,-8,-6,-7,6,9,9,-3,8,2,-8,9,-1,-4,3,3,1,6,2,6,-1,5,-3,-4,2,-3,1,10,8,-2,-3,10,-8,3,10,-10,-4,-2,1,8,-4,-4,2,-8,7,3,6,-5,-10,8,8,10,1,9,-9,-7,-9,-1,-4,-3,-10,-2,8,3,-6,7,-9,5,8,-3,-10,-4,-1,2,-4,6,-1,-8,-6,8,-2,-7,1,-10,-4,8,5,-5,-4,4,1,-2,10,1,3,-9,4,5,-6,4,9,-7,5,3,-10,7,-8,-4,-9,4,6,-6,-9,-6,7,6,2,-2,-7,6,3,9,-4,-10,9,4,9,-6,2,-5,1,-7,-7,10,6,-1,3,2,4,10,-10,-9,-6,-9,-6,-7,8,-2,3,-10,9,-1,3,10,7,-1,6,-8,-6,1,3,-10,2,-3,3,-5,5,7,-9,-5,8,-7,-9,-7,4,-8,-7,-6,-2,5,4,-10,-6,-9,7,-3,-2,-9,5,-6,5,-4,4,-3,-10,-4,8,3,2,-9,8,3,-2,2,10,6,4,10,-1,6,1,6,-3,-3,3,-5,-4,2,1,-5,4,6,3,-9,1,8,5,-3,-2,-5,-8,7,-7,10,-5,-8,-8,8,-2,-8,4,7,9,-8,-6,-8,-3,6,4,-7,3,-7,-2,4,5,9,9,9,-7,1,-9,-6,3,-2,10,-7,9,-3,10,6,-1,-5,10,10,-10,-1,-9,-1,10,1,-7,2,2,-6,5,10,-5,-8,-8,6,-9,-6,3,3,3,5,10,-5,-7,5,-2,-9,9,-6,8,-4,7,7,5,7,-2,9,2,-6,-4,-10,-7,3,-10,2,9,7,4,-9,-4,9,9,-1,2,9,-8,2,1,1,4,-9,7,-10,4,2,-4,-5,10,3,3,8,10,-7,5,2,1,-4,-1,-1,-4,2,-5,10,-5,7,-4,9,7,6,-4,-1,2,-3,-10,8,9,-9,-7,2,-3,-9,-6,-2,8,2,8,9,1,-5,-8,2,-10,-4,3,10,4,2,10,2,-5,10,-2,-5,10,-1,-2,-8,5,1,7,-3,-1,-3,-10,-8,1,-8,8,-3,3,9,-8,-2,-6,-10,-6,-5,9,-9,3,4,7,7,7,-6,-4,10,9,-5,-4,-9,8,-7,-2,-6,4,-10,-5,-8,7,-5,-6,-2,-4,1,2,6,4,8,10,4,5,-6,-1,3,8,-6,10,1,-5,-1,2,8,3,-5,-2,-6,3,7,8,-9,-9,-3,4,-4,6,-7,-5,8,3,-8,2,-3,-7,10,-2,4,-5,2,-10,-8,2,-9,-4,-2,10,-3,-5,1,9,-7,-10,4,-7,3,-1,-8,-10,-7,-3,1,-8,-10,-1,4,2,-2,-2,6,-1,9,-3,4,-3,6,-1,-1,-3,1,-2,3,8,-6,2,-2,-4,6,7,9,-2,-7,-3,-1,9,-10,8,-7,-1,-9,-7,-7,-1,8,-2,9,1,-6,-2,1,-2,4,-4,-8,-6,-7,7,3,6,5,8,3,-10,6,-7,-5,7,9,-2,6,4,-10,1,9,5,-7,-10,2,9,-5,-4,5,2,3,-3,-2,6,9,5,5,4,3,-2,7,3,-10,-2,6,-1,8,10,2,-1,-3,9,-6,-8,10,-4,-3,-8,-3,8,-6,10,4,5,-6,-6,-3,-5,-1,-8,4,9,8,-8,8,10,-6,10,-8,5,9,3,8,3,-2,2,2,3,9,-8,-9,2,9,-5,-5,3,2,8,-3,-3,1,-10,7,10,7,2,6,-3,-6,-2,-9,-6,10,-4,4,-7,-3,7,-2,-5,-7,-7,10,10,10,-4,-6,1,6,-8,-5,7,-1,7,3,4,-6,3,-3,-2,4,2,-8,-7,-10,-5,9,2,-6,7,8,9,2,-2,4,8,1], dtype = "int64")#candidate|11091|(968,)|const|int64
const_11092 = relay.const([4,-4,-10,-9,10,-1,10,-6,-9,4,7,-8,3,-9,9,4,2,10,-4,1,10,-2,9,-1,-3,2,3,10,-10,-10,7,-2,1,-10,-1,-1,-4,3,1,4,9,5,-7,-9,6,-6,5,-3,-10,-1,4,3,-5,3,-10,-1,4,2,10,10,1,10,-6,2,6,8,-7,7,-7,9,9,6,-7,5,-10,-5,3,-8,-8,4,6,-3,-2,9,3,9,-10,-5,5,-4,7,5,7,-8,4,7,3,-4,-10,-8,-3,-7,4,-9,2,-2,-5,10,10,6,-1,5,3,-10,-4,-10,-5,-1,-6,6,6,-10,4,-2,9,10,3,3,7,-10,2,-10,-4,-6,1,-2,-9,-7,-2,9,9,9,-7,9,-8,6,9,-8,9,7,5,9,10,9,7,3,-9,9,7,-1,8,-8,7,2,-10,-8,-8,9,2,-2,-7,-8,-7,2,6,-10,3,1,-4,6,4,8,-8,2,6,1,-8,10,6,1,5,4,9,-8,10,8,-5,-8,5,2,-5,-5,-2,8,6,9,1,9,-9,-5,-10,-3,-1,-7,2,-8,-2,9,9,-3,-5,6,4,-5,4,-3,5,7,-8,4,4,6,6,-4,-3,10,7,-3,1,7,-2,-10,-8,-4,-1,-6,-10,-5,-10,-3,-3,-10,-9,5,-2,7,-3,-10,-4,-7,3,-2,-10,3,-5,10,9,10,2,8,-8,-8,10,1,-2,-8,4,2,-6,-1,-1,-1,-2,6,8,7,-9,-6,3,-4,4,4,2,1,10,1,4,10,4,-9,2,-6,-1,1,-8,10,6,1,7,10,-5,-9,-2,2,-6,8,-6,-10,-7,-2,-7,10,-4,3,-4,-1,3,-7,-8,3,-1,-6,5,6,9,10,8,-1,-2,6,-5,-6,-4,3,1,9,-7,1,-1,6,4,-7,-8,7,-3,8,9,-6,7,8,-7,2,-10,-6], dtype = "int64")#candidate|11092|(364,)|const|int64
call_11089 = relay.TupleGetItem(func_1763_call(relay.reshape(const_11090.astype('float32'), [5, 9, 4]), relay.reshape(const_11091.astype('int64'), [968,]), relay.reshape(const_11092.astype('int64'), [364,]), ), 1)
call_11093 = relay.TupleGetItem(func_1768_call(relay.reshape(const_11090.astype('float32'), [5, 9, 4]), relay.reshape(const_11091.astype('int64'), [968,]), relay.reshape(const_11092.astype('int64'), [364,]), ), 1)
func_9028_call = mod.get_global_var('func_9028')
func_9032_call = mutated_mod.get_global_var('func_9032')
const_11099 = relay.const([-3,-4,6,7,6,7,-10,8,3,1,9,-4,-6,5,7,4,4,-4,-3,-4,8,-8,-8,-6,-6,-3,-6,-4,-1,-10,10,-8,-4,-5,-5,8,10,2,2,9,6,-5,-8,7,-9,-8,4,5,10,5,-1,-9,-8,-9,10,8,-9,-8,-1,8,5,1,4,7,8,-9,6,-1,8,5,-7,2,8,-5,-9,1,1,-3,-9,-10,2,-7,-7,1,10,3,-10,5,9,7,5,1,-1,4,3,-9,3,-3,6,-8], dtype = "uint64")#candidate|11099|(100,)|const|uint64
call_11098 = relay.TupleGetItem(func_9028_call(relay.reshape(const_11092.astype('int64'), [364,]), relay.reshape(const_11099.astype('uint64'), [25, 4]), ), 6)
call_11100 = relay.TupleGetItem(func_9032_call(relay.reshape(const_11092.astype('int64'), [364,]), relay.reshape(const_11099.astype('uint64'), [25, 4]), ), 6)
output = relay.Tuple([call_11062,call_11089,const_11090,const_11091,const_11092,call_11098,const_11099,])
output2 = relay.Tuple([call_11063,call_11093,const_11090,const_11091,const_11092,call_11100,const_11099,])
func_11108 = relay.Function([], output)
mod['func_11108'] = func_11108
mod = relay.transform.InferType()(mod)
mutated_mod['func_11108'] = func_11108
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11108_call = mutated_mod.get_global_var('func_11108')
call_11109 = func_11108_call()
output = call_11109
func_11110 = relay.Function([], output)
mutated_mod['func_11110'] = func_11110
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7798_call = mod.get_global_var('func_7798')
func_7800_call = mutated_mod.get_global_var('func_7800')
call_11121 = func_7798_call()
call_11122 = func_7798_call()
func_7231_call = mod.get_global_var('func_7231')
func_7234_call = mutated_mod.get_global_var('func_7234')
var_11126 = relay.var("var_11126", dtype = "int64", shape = (390,))#candidate|11126|(390,)|var|int64
call_11125 = relay.TupleGetItem(func_7231_call(relay.reshape(call_11121.astype('float32'), [15, 9, 6]), relay.reshape(var_11126.astype('int64'), [5, 78]), ), 4)
call_11127 = relay.TupleGetItem(func_7234_call(relay.reshape(call_11121.astype('float32'), [15, 9, 6]), relay.reshape(var_11126.astype('int64'), [5, 78]), ), 4)
func_9863_call = mod.get_global_var('func_9863')
func_9864_call = mutated_mod.get_global_var('func_9864')
call_11153 = func_9863_call()
call_11154 = func_9863_call()
var_11162 = relay.var("var_11162", dtype = "float64", shape = (8, 546))#candidate|11162|(8, 546)|var|float64
bop_11163 = relay.less_equal(call_11125.astype('bool'), var_11162.astype('bool')) # shape=(8, 546)
bop_11166 = relay.less_equal(call_11127.astype('bool'), var_11162.astype('bool')) # shape=(8, 546)
const_11178 = relay.const([[-9.544935,-9.953455,-5.461338,-6.964118,-7.010778,2.156377,5.461112,0.462049,-8.150569,-3.860670,2.691537,-4.189938,3.347191,-0.661254,-5.843558,-3.931154,9.358010,-7.340730,-8.839285,4.789862,-1.155498,4.231046,-2.490682,8.853420,-0.981374,-7.154903,3.017373,6.527256,-4.161089,9.817803,3.102643,-9.187982,-3.208659,-2.193872,3.119149,9.122894,-0.988560,2.951982,-3.122592,6.484320,-2.545346,-5.102786,-3.935014,7.266701,3.815512,-0.493206,-3.634666,9.641724,3.482744,0.549472,0.761804,6.078233,8.117229,-3.431504,8.779572,-5.283937,1.010728,-0.369263,-9.877925,2.379019,-0.146230,-8.529536,-1.240317,8.964455,2.521755,-5.688023,-5.861940,-7.155213,0.946924,7.174492,-9.486185,-1.089821,-6.684802,0.087675,-2.000121,-7.284361,-1.816056,8.863088,-2.737986,4.423833,5.233224,-3.311452,7.715893,4.031226,8.748833,8.081206,-1.191472,1.942816,-9.969033,4.993798,2.140067,8.547977,-7.397491,-4.185054,-2.979723,-8.941727,-3.506454,9.579765,6.863629,-6.962858,5.019498,-5.026300,3.307535,-2.659853,6.639373,0.367465,7.449094,-1.540224,1.882670,-7.770821,-7.123049,-6.762753,1.969611,-2.262344,-3.486048,3.099621,1.171370,-1.171311,2.766435,-6.942260,-8.042394,-4.137796,3.794031,-2.618350,6.303893,-7.043073,8.158408,-6.750683,-2.495052,-6.285196,3.142884,-7.695645,1.379161,-2.085155,4.987102,2.235776,-6.106538,9.727555,4.226687,-9.279058,-7.943898,-8.271241,5.652140,-1.609434,-7.559705,3.301188,-9.071035,-7.741266,-4.461679,-6.623177,6.794313,5.906981,7.989795,8.650509,-6.522202,-4.113355,-4.468540,1.185335,5.513183,4.806135,-7.162958,-9.462757,-7.480211,-4.296883,5.756885,-2.712544,4.546402,-7.973087,-4.049646,0.508695,8.512919,4.232683,-5.945852,-6.867287,-7.524975,0.072068,-9.121092,7.306370,-3.930981,2.519446,4.840634,3.622789,3.749748,5.202898,4.097451,0.942798,-9.324203,0.522172,5.307264,5.937806,2.016332,-5.132697,-9.485081,4.004438,7.273230,-4.246423,-2.589654,9.076142,1.891983,-4.483820,2.778390,3.069256,-7.336632,5.313643,-4.430375,-1.422777,1.492048,7.512196,-2.008641,2.561214,7.047670,-3.404873,9.862432,-9.033036,5.124897,9.799748,-9.045954,-5.925495,6.820300,-5.895937,-9.246705,-3.526719,9.088142,5.800612,-3.123744,3.328220,-3.356888,8.328649,-4.455992,-3.744159,-5.304518,-2.790854,9.004186,-4.517185,-4.991877,-1.305337,4.826458,9.203909,7.599517,-0.037832,1.247210,6.945687,-9.144393,9.891013,-5.625358,-5.343824,6.560165,6.471584,1.232387,-0.781357,-4.013293,3.409806,9.201295,-9.389983,8.888250,-4.568561,5.172619,0.518573,-0.079295,-4.565867,-2.162951,-8.884587,2.115145,-3.553012,8.828839,4.967680,-2.545591,8.068306,6.151776,-0.679259,-2.295583,2.534748,-9.451962,4.088164,0.356793,-3.615960,-8.737283,0.770029,-8.913348,0.757244,-7.913426,-6.367036,4.584537,-5.595099,1.180640,5.761835,8.479256,6.719624,7.698303,6.721557,-5.842941,0.401203,-0.172297,4.502836,-2.665945,-0.173749,5.788656,1.296778,-9.797901,3.622362,-3.967284,4.037081,5.943596,-0.653267,-7.699752,8.081274,6.924542,9.373498,6.446479,-7.719011,0.681889,1.877766,1.769535,0.509234,-2.673586,-5.084085,-5.385037,6.594670,-8.994357,-3.285626,5.337070,-7.922727,-9.373892,-8.868729,-1.716673,-2.408600,6.036578,-4.572589,-7.266915,-9.543789,-7.780864,-6.646820,-1.577235,-0.780336,1.895553,2.739136,-7.758444,8.280076,-6.425824,-1.858875,-1.969791,-9.182630,-1.683076,3.068844,7.231452,-0.138754,-4.375735,-6.268640,-3.288586,0.087900,1.597601,-2.729306,-5.947578,0.999262,7.981607,2.469554,-2.507704,5.748712,-6.296765,9.157909,-7.577186,3.496221,-8.029841,0.577732,-8.226844,-2.606415,-8.192250,9.344863,-7.261693,3.008004,7.203767,-3.211645,-3.481641,-0.970824,-2.217248,-9.897567,3.190625,2.246876,9.606773,-1.336999,0.506201,-3.196540,9.778700,9.978501,-6.028821,6.781859,6.386659,9.326397,0.994422,1.878963,7.697814,-7.764005,9.744429,7.365065,4.396672,3.232682,-2.467640,-4.380614,5.921085,-8.885049,-0.872868,7.233455,3.777332,2.237373,8.656215,-1.862569,3.358895,8.144719,-6.664473,6.256178,7.060766,-2.376210,-5.731692,8.796573,-6.630817,0.888972,-3.086496,0.818217,6.832210,-9.307973,7.770569,-0.417072,-9.704796,7.094992,-6.895944,-2.956075,6.761183,6.505134,1.444868,-1.248571,-2.269817,-3.403103,-3.423578,-6.786240,-0.542546,-8.776551,2.633486,-3.140584,0.844948,-2.938364,4.119924,3.729592,-7.977459,-9.188089,7.215137,9.808383,5.690547,-4.973615,1.401013,1.916316,-7.191232,6.707408,-1.354149,0.184994,-4.694526,9.512114,-7.282705,-8.578740,-6.121312,-7.430860,4.666012,3.956994,9.902010,6.669678,5.567132,-0.189720,-5.622937,1.264150,-2.495395,-5.799675,7.345937,-9.055031,-8.194277,-7.394740,4.557731,9.177013,-8.125411,2.923215,-8.994061,3.773946,-3.511866,9.609238,3.148778,3.822719,7.146322,-3.784885,-2.904498,-4.325883,-8.589294,1.859391,5.676388,-6.199825,3.112216,7.430473,-3.972978,0.319045,6.504012,-9.800457,-8.212572,-5.879649,7.214499,-0.412867,8.844459,5.770259,7.286445,0.451209,6.584560,-1.824447,-8.665076,-8.552150,-3.915411,3.400801,8.505877,1.182848,0.370071,5.829397,-9.444307,-2.932381,7.200119,4.394014,-2.065719,4.298989,5.849778,7.183012,-7.398884,-8.492118,0.780407,-7.362312,1.561684,-7.322302,5.219230,-6.860330,7.963362,4.164267,-1.249620,3.494816,5.666894,-8.776396,4.005585,-9.926125,6.391436,-6.424988,-1.255417,1.705099,-0.930986,7.937172],[-8.967866,-0.808462,-3.425469,-2.205921,-8.275801,-1.133821,-1.161295,-7.119656,-3.441298,2.794125,-2.797352,-2.538388,-0.059535,-8.634849,-4.749656,-3.368886,0.196108,-9.173381,-2.333873,-6.952004,6.012125,6.501511,9.495634,3.276404,-2.522374,-3.723051,-1.739955,-3.878840,-2.663443,-7.174106,-8.987174,4.125971,9.144449,4.481139,-3.307595,-2.331151,-0.330121,-8.908761,-8.984967,6.827681,-2.624409,2.604434,9.061105,-6.850436,-9.194359,-9.180465,5.711309,9.864005,7.188517,4.752752,-8.828964,2.555123,7.617019,4.194934,4.750996,-6.876505,-1.769595,5.377723,9.094678,1.494160,-5.446754,-9.287886,-7.254089,-5.715698,3.451741,2.834889,2.728919,-5.033797,-2.090304,-0.326307,8.751263,-9.175684,-6.290196,5.199886,8.863000,-0.847543,-9.973404,8.234648,-3.043960,-7.259884,0.159633,6.484579,5.413765,0.932129,2.627187,8.630905,3.667993,-9.618860,9.853652,6.426518,6.057383,-1.238419,3.272527,-4.182118,6.802778,2.511306,-1.875624,-0.048270,-3.432277,-0.938043,2.380460,-8.279499,4.684516,9.297989,-7.435990,4.469252,-4.575493,0.362851,2.538139,0.134471,2.506699,-0.656914,4.207736,3.514189,-0.228747,-3.933779,0.523809,-9.446343,4.726557,-1.375995,3.606942,0.729478,8.280452,6.601260,-5.167721,-8.899054,2.869225,-5.620396,6.580308,-0.955300,7.729546,8.592747,-7.271574,8.001993,1.056599,4.464986,5.475303,-2.587813,-0.317854,2.235160,-1.521699,-8.053270,-6.690743,2.131048,-3.646219,-4.320445,-9.821323,-4.643424,4.720683,-5.658971,4.166255,1.448425,2.726046,-2.130769,9.415684,-5.655918,1.426294,4.103086,3.609090,0.843439,7.597531,2.302008,2.421662,-0.228753,2.845327,-9.439981,-1.723427,4.248382,9.397854,7.269175,-7.880521,8.229177,-6.759422,5.192640,6.698932,2.810693,-3.887142,-6.906150,4.026939,0.451911,9.148697,1.048894,7.155866,1.196014,-5.456764,-9.043411,0.529718,-4.561329,-3.529351,9.871427,-1.163542,-1.556514,-4.680367,1.195379,7.459703,-8.429399,-5.685845,3.987187,1.521702,-0.499125,9.697282,-6.546051,-1.625018,2.219122,-0.357278,-5.803724,6.988971,-0.162561,0.753205,2.039080,-2.877533,-1.914317,-1.278653,-0.068014,-7.677134,5.964443,3.782340,-4.316175,3.290265,4.476575,9.052358,-8.721774,-1.026013,-2.845774,-1.521431,7.162296,5.885845,2.076095,8.603828,0.386390,3.194935,9.613692,-5.480118,-9.986723,9.581716,-1.082335,-9.287413,-4.811670,2.566289,-8.358798,-3.877007,-6.867408,4.304990,1.941811,8.503038,6.749046,-0.678921,-2.824482,-5.631084,-4.849678,-4.948814,-8.262034,8.449634,7.375805,2.821229,1.469750,2.458447,-2.913309,2.382276,4.244341,-7.645239,4.573183,-9.203087,-6.915472,1.500827,-4.513776,1.318096,-3.478193,0.169674,1.305527,0.177170,6.761383,-1.501617,-8.240706,2.032494,-3.306642,-8.306833,-8.212747,0.423272,2.140363,8.373374,-0.512082,2.635814,-7.197421,4.017577,2.450193,-2.728150,9.693273,-3.409503,-5.359362,-9.758529,-6.730954,6.734668,5.761724,0.390115,1.084848,-1.944733,7.099992,-9.644404,4.685434,0.711121,-5.562395,8.617882,-6.035639,8.881101,1.810194,9.940288,-1.957429,8.882969,-9.984472,0.320729,1.935086,4.586907,1.108666,-0.197783,0.514628,0.704854,9.264675,-7.873724,3.041253,3.144174,6.063974,-7.267853,4.415712,6.369000,-1.057741,8.068249,-4.676931,-2.682639,-6.578870,-0.986190,-9.603206,1.449410,-2.502657,3.010492,-4.200813,1.402338,0.708031,2.093183,3.288637,-3.712319,2.013906,5.774223,7.132162,7.592147,1.438410,7.006128,-8.825250,8.642596,-1.159402,-9.085895,2.694482,-9.027765,9.398233,5.530842,-5.617256,-4.113432,6.427241,-3.349060,5.462661,-0.348031,2.285477,-9.239828,4.203400,1.024019,-2.004398,-8.314765,7.734275,-7.343064,-8.964773,0.170422,-4.310850,4.412567,0.499204,-5.950138,4.187154,8.857632,-7.886247,-6.001514,-5.959743,-9.622096,2.221111,-7.307778,9.394604,4.736884,5.335742,5.901626,-5.058685,9.505574,-9.551216,-5.873763,1.281825,-9.183748,8.493737,6.338651,-0.454313,-4.922725,-3.543204,-4.988824,-1.968457,2.771392,-1.120224,2.319029,6.834118,8.912573,-2.424230,-3.635545,2.731940,3.837477,4.574849,-7.893465,-5.955382,-9.597505,-2.258967,5.413425,-8.099542,-8.306278,6.180513,-8.143499,-5.069911,-5.256496,3.135429,-2.236369,6.145519,-3.043943,-3.463638,0.925569,7.509335,8.588312,-1.577360,-2.104057,-5.964411,-9.050590,-3.552546,-3.225672,-5.787701,5.031160,3.554110,-3.691116,-8.200284,-8.581605,-2.536289,0.496452,8.043433,6.895937,3.962735,-0.606241,-8.917346,3.992593,6.760158,1.038890,-1.300541,-3.605282,8.237543,2.038721,0.123137,-8.368184,4.073599,3.482463,6.440457,-1.741769,3.651709,-2.266562,3.381972,-9.226220,5.164509,-8.783260,1.045734,-7.354761,-4.297147,-4.285912,7.294551,1.530379,-2.371891,7.381044,4.545863,4.209903,-2.467430,-9.317651,8.750243,3.054742,-3.909143,6.256143,-0.482404,-3.960880,3.901201,-7.581722,-1.569483,9.318544,-2.071856,-9.684466,-1.011799,-4.879960,1.880665,5.039801,-2.569098,1.085282,-2.997193,-7.099549,-0.018520,5.482094,8.760207,-4.530343,2.967289,-3.465851,-0.620367,1.559343,-7.325631,-4.528792,-5.384697,4.061511,-0.292661,-3.332056,5.002443,9.018100,9.884987,2.581403,-7.692993,-6.003976,7.259118,6.015127,6.549033,-9.698500,6.729264,8.513469,-3.801022,-0.325767,-5.058847,-1.225303,0.818747,9.459714,-4.945117,2.033862,7.874055,0.090831,-6.097079,-4.026397,4.291655,-8.261207,6.697319,2.603577,-0.277239,-1.646889,-3.622358,-2.435672,-8.243191],[-7.890570,-7.655033,1.820453,-4.551244,-8.442648,-2.625882,-5.561400,9.973562,-5.909368,6.727459,2.276160,8.016488,-8.176598,-4.093164,7.186036,-8.712923,9.402712,6.678447,-3.520550,3.731533,-8.289234,-1.964731,-0.337193,0.334838,-4.341823,-3.657284,-7.733403,-3.751716,9.124250,9.497619,5.559819,-9.080607,-6.577328,-9.343720,5.286991,2.844014,8.878277,0.320010,-2.103147,-0.105778,3.889269,-7.530760,-5.923664,-0.510788,5.221825,-7.773319,8.144823,9.661077,-9.533897,8.530722,-0.686265,4.899934,-6.454427,0.485642,-6.532396,6.509767,-8.148720,9.658007,-3.605940,-2.762200,-3.308889,0.935030,9.765308,1.285603,-7.164453,-4.477433,-5.766686,-3.445938,-1.547439,7.322739,7.986293,-0.277141,-2.827073,-3.065726,2.147579,-3.377358,1.302162,2.242746,-3.078740,-0.232498,8.596300,6.882725,-2.899414,-7.986572,8.816597,2.624115,3.494289,-7.879936,-3.812017,-4.076360,1.956241,8.964258,-3.195937,-4.095978,6.745282,2.430730,3.095218,-8.537143,-5.029017,-3.586295,-3.490616,-6.198132,8.763783,0.387208,4.050117,8.076618,-3.562657,7.256479,4.534132,-9.799952,-2.429456,-4.302296,-0.237719,-5.803699,1.295801,0.554455,-6.204894,9.691561,-6.905193,2.438822,5.211701,0.479094,0.702701,-9.570411,-3.249610,-6.985847,3.036448,-0.163434,8.138121,-2.557373,6.808850,7.750647,-6.237977,8.889718,1.768570,-9.833027,3.456070,1.932273,0.513667,2.300510,-2.395040,-1.439927,-7.083031,4.574699,8.279354,9.972661,2.506542,7.059656,2.656674,6.883744,8.226307,1.123433,4.429358,-1.212467,6.021739,-5.541448,4.362748,7.039089,9.467536,0.702898,-4.984883,8.925262,8.865022,4.745624,5.164749,-9.251388,9.147135,2.601874,-9.667816,0.959144,6.721548,3.904643,-1.088532,6.704886,1.816181,1.545285,4.132237,-8.926906,8.629575,8.466983,-8.067167,2.900930,-6.255097,-0.914347,-1.955077,-9.475548,9.932052,-2.353407,-6.440752,7.181533,6.518221,0.526449,2.369694,9.358474,-7.844371,7.450091,-4.400115,-4.339505,3.999660,6.094416,-1.148902,5.750706,7.319957,4.460209,0.307719,-8.097823,7.972460,6.123404,4.302220,5.605173,-5.434275,-6.126340,-5.039162,4.394116,0.492345,2.287608,-4.852737,5.333142,2.038760,1.295656,4.919438,7.291053,4.619857,2.083118,7.882514,-7.515370,9.904155,5.028870,2.616979,7.382572,3.505365,-4.570935,2.728265,-4.994125,7.598721,-5.996665,3.884221,0.520704,-8.395868,3.591957,-4.543775,1.443138,-6.610637,2.672865,6.601137,-2.840589,3.247473,-0.621173,-3.501939,0.995746,-5.190076,-1.604672,1.142152,9.786334,-1.088289,-5.665064,-5.602731,-0.917697,-1.605513,2.561971,-5.791560,-8.062622,-2.119160,-2.013069,6.997865,-8.278778,6.073580,0.478025,2.377172,4.573378,2.152369,-5.469095,1.697233,-2.152431,-1.796018,-2.928693,5.942557,-8.969515,2.244913,-5.113271,1.174366,1.029506,8.538691,4.497121,2.378240,-6.882714,-6.604048,-4.792975,8.807231,4.051358,-5.527228,-4.712816,4.415994,-1.361908,-5.807280,1.805815,5.985149,-7.745099,-9.562972,1.882080,-8.598043,-0.052335,-3.875650,6.376083,-4.464474,4.700809,-3.030359,-9.499804,2.949594,-9.932984,-2.418027,5.109433,-0.936515,-3.039543,9.366840,-4.598670,-5.899506,3.313057,-2.945002,-4.321880,7.787231,8.929554,-6.801260,6.432750,-2.259460,9.601839,-4.943997,4.226546,-5.588093,8.556644,2.888702,-0.511614,-6.294826,1.718502,-3.485804,7.456266,4.945149,6.519110,4.916996,5.564866,-7.740005,-8.110041,2.508096,-5.059360,0.473375,-1.242312,3.683288,-6.776981,-3.993449,-0.133372,-6.703545,-9.858440,8.216343,8.641663,5.109647,-1.575457,5.854073,-1.865060,-6.643854,-5.075266,-1.948542,3.741583,7.034453,9.280709,9.209765,-8.180406,-2.925376,4.506816,-0.187849,-6.596336,-2.516310,-6.614029,4.716352,-8.538181,4.888523,3.799307,3.690837,7.125729,9.474337,-1.383349,1.557249,-5.625004,-3.650383,8.079275,-9.511057,-3.627875,-0.623663,-4.849109,5.065341,-2.572514,6.624870,-8.995729,-6.630292,-0.150368,-0.240188,-5.884976,0.720189,2.013848,-9.609747,9.691966,-4.120825,5.081820,-9.025222,-0.021324,3.648238,-0.757292,3.035671,7.235024,-4.859098,9.453537,8.768053,-0.356892,-5.162975,-4.473508,-3.997184,3.433721,7.683164,-1.312762,-0.472353,3.724176,3.760055,-6.105550,-0.874354,-6.928040,9.754671,3.792330,9.405404,-0.287467,-8.895882,-7.726359,-1.101110,2.265460,3.433113,6.740250,9.196181,4.179214,-5.082710,4.948430,8.465161,3.694883,2.695898,1.424272,8.822302,-3.352433,-9.402376,-5.947206,-2.612744,-3.734384,5.462316,8.560969,-1.110374,6.856481,-9.254468,3.110120,-4.373840,0.910588,-3.131667,-8.364523,-8.329509,9.099802,-6.706902,6.737651,1.665367,-3.718013,3.405827,7.913827,-3.733888,-2.956319,3.291976,-2.793572,-6.899063,2.419057,5.705733,-9.416015,-4.333401,-4.680164,-1.499679,4.144136,-4.073971,-1.037610,7.539763,1.922720,5.224679,2.491868,-6.589056,-1.939901,1.515347,6.519540,-5.037966,-2.672580,6.867275,6.722820,-3.916643,2.231079,-9.085725,-5.684080,-4.967676,5.401885,3.396384,-8.617044,-2.053699,-5.304814,5.705035,-6.099343,-4.865135,-5.231371,-4.484031,2.939592,6.943769,3.930717,-6.757600,2.157861,2.304064,-9.530893,4.704036,-3.968851,-8.954638,2.182220,-8.446926,8.330391,-6.449034,-0.306003,4.706195,5.656045,1.654330,-8.636182,-2.740434,-2.593329,-9.794322,-8.365073,4.209571,7.525768,-6.346086,8.287958,2.940143,2.346091,4.619538,-1.353639,9.069180,1.512909,-2.088108,-7.046627,4.819628,-0.743020,-2.963107,-3.723102],[-7.281214,3.638757,-8.962723,5.390545,9.183106,-4.322684,5.661991,4.276834,-7.151705,0.024098,-8.709925,-5.106783,-8.923184,8.924225,0.308861,-1.497685,2.424007,-0.098250,1.804241,1.804525,-5.257305,5.379834,-3.728856,-6.250931,0.697967,6.328565,-6.980508,7.238557,5.122714,0.831331,-0.350133,-0.843383,7.179239,-5.368152,-9.724706,8.980343,4.542383,-3.687384,3.891066,-6.674159,-1.530285,-4.246629,5.379466,1.107183,-3.969866,-0.871194,8.681681,-0.681183,6.618325,2.597623,1.917667,6.536067,5.990782,-3.511793,-9.798223,3.145376,3.362058,7.374133,0.701401,4.494786,2.316526,9.333597,-8.170434,4.032814,-1.911425,5.457354,4.401273,-8.945789,9.694935,2.533218,9.866757,-6.142906,-2.233916,-0.685367,6.399978,3.457930,4.814558,6.230622,7.951870,7.334214,2.201723,1.967374,1.303814,2.541852,-4.755073,3.147561,3.847505,-7.341045,4.324319,6.550748,-5.966265,-0.519748,4.837031,7.123317,-8.367364,-7.340110,-9.037352,1.556307,0.644456,-9.524483,5.376689,-3.497031,6.778014,6.616909,0.089177,4.110001,2.190352,9.606329,8.159144,9.288585,7.674838,3.003683,3.552847,-5.776759,6.709013,1.655015,-6.123718,8.185570,-8.398893,-3.389069,-6.064593,-7.180980,9.597833,-0.909313,-1.584367,3.700018,-0.462201,0.837122,0.087986,-2.361469,-4.388398,5.897207,7.898055,2.586924,0.135947,4.022134,7.053453,-2.167868,1.910726,-4.070246,-1.534446,-3.083960,-2.231807,7.823898,8.870573,3.134147,0.475954,-4.643301,8.166401,-0.375478,8.059664,-4.159073,5.650343,-6.531777,-5.309271,4.082311,-8.146262,0.233425,1.841258,-2.137659,-4.422948,3.647772,-8.276833,6.585496,4.636140,8.906249,5.413929,3.943561,-1.541220,-2.617778,-6.552423,6.674676,8.698139,-9.600037,9.781581,1.147439,-0.056525,1.495998,-8.596354,-7.876557,6.425308,-2.522080,-2.323353,7.165499,7.040232,9.923669,9.401377,-7.267856,7.281167,-2.474157,1.638678,-5.396738,-3.859836,5.016371,-4.345225,-8.240037,7.535995,4.632492,-9.280765,-3.776524,-0.915669,-3.309998,-2.741926,-8.199118,7.876221,0.905022,-3.835972,-2.223527,8.091142,4.892913,0.766101,0.578661,-7.814151,-9.115017,-9.654307,3.686215,-9.228236,-0.667453,-9.735862,-4.105895,8.515663,6.956440,-0.757927,-3.723052,5.590578,4.380038,4.823361,4.469019,2.243905,4.854021,-9.398603,-7.559224,-0.039274,8.781485,5.693889,-3.086943,3.031168,-3.410689,6.624913,-3.686169,-0.280980,4.885987,-4.134842,-6.651834,4.667324,8.607607,-0.320869,-3.618722,4.469901,5.703440,-6.073731,5.916084,3.823847,2.337559,3.426337,5.693923,0.097407,8.138299,8.093909,-8.204617,2.527534,-3.387686,3.124423,-8.467336,8.253386,-7.146659,3.675641,6.311643,1.725760,3.762051,-2.674364,4.792868,-6.545313,-0.425051,-9.067852,-0.191373,-8.878798,6.894188,9.561662,-8.535470,4.542019,-8.882982,4.876811,-5.084532,-9.467508,9.301126,-8.476968,2.620192,7.451327,8.491877,-9.453959,-3.218923,-6.875796,-0.354895,9.993947,-1.440120,4.312134,-9.066871,1.760278,-3.643128,-0.131932,-2.942590,-6.089657,6.098732,6.559389,7.975196,-0.782114,7.065250,4.350280,7.024261,-7.618095,1.486554,-1.105489,-9.520720,-0.287105,-4.677176,-8.185913,-5.912535,-3.998879,8.974365,-5.487445,5.600983,-2.951241,3.152758,-8.166417,-7.136536,8.478352,5.143911,6.677089,6.768077,-2.491622,0.375609,-7.184805,3.204616,7.966208,8.017995,1.777170,5.920044,9.720740,0.115864,5.741232,-1.636969,7.659431,-0.718717,-4.426705,7.093138,3.788266,3.622904,-8.351940,-8.550828,3.017778,4.593905,-0.589918,-7.780616,5.912350,-7.315633,-9.634344,2.009731,-1.888003,-1.878922,6.555579,9.482661,-5.251900,6.126779,6.065438,3.245315,1.612020,9.359796,4.940656,8.349216,3.301047,8.637789,-0.737249,3.162269,-2.713528,7.737315,4.811532,8.244444,-3.125070,-4.470555,-4.343437,-3.433020,-4.517293,-1.889199,-3.526503,6.550041,3.102461,8.790361,6.939649,-2.015255,-6.821943,-5.733015,-3.582584,-5.014265,-6.146996,-8.336096,-2.313749,-4.939377,-4.407849,-4.836767,-3.274967,-6.148241,-1.820217,3.188179,-1.548683,1.826401,-8.819193,8.486135,3.098204,0.858185,-4.893632,0.931985,-9.514344,-8.876401,-7.425507,5.719698,-1.814110,-1.408527,8.627980,-8.018325,8.583434,3.162409,3.894000,-7.395788,-1.845530,-6.032873,3.977882,9.331629,2.922691,-9.697028,-4.613502,-1.491485,0.768519,1.998574,0.629443,-6.768914,8.549327,-2.728261,-4.045286,-7.880855,-0.931394,-2.828471,-1.831216,6.293516,0.282515,7.395695,-6.163613,-7.244109,-8.504737,-4.433952,5.243120,-3.566338,-8.626309,-8.241421,6.090090,9.857340,5.451027,7.965322,7.852945,-0.013618,-0.462188,-7.845986,0.766647,-7.340808,-3.903941,3.344140,0.891683,1.907988,-4.683749,2.393535,-1.155024,0.875087,-6.867171,8.174540,-9.134184,-1.162260,3.340183,1.115419,8.600414,-8.786846,-3.215594,0.212003,3.197299,-9.722820,-7.648031,2.149277,-8.048848,5.731343,4.678241,6.106518,-7.650544,-8.826669,-6.916112,-7.808920,2.918114,-9.395900,9.329919,5.432524,-2.042582,-2.573819,0.196757,4.364313,3.091768,-7.791482,1.531164,-6.235995,4.307235,6.133284,-3.035568,8.271100,-7.623997,0.424553,-6.696885,-2.146515,-0.987920,7.555864,-4.948555,-0.793097,5.215369,-3.565093,-6.133618,-6.747109,9.881153,8.918536,-9.932775,9.960160,-1.911586,-7.202417,8.872841,6.981213,9.908702,-6.473245,9.411483,3.686127,4.076052,9.668701,-3.588180,-6.918968,4.172619,6.680595,-4.374122,-2.317686,-2.633616,6.375712,8.048388,8.512376],[-1.384129,-0.172722,-3.116161,-1.531569,2.818121,9.296546,-5.355819,3.786588,-8.805713,1.109455,5.976255,9.663529,-4.991586,-8.637487,-3.130076,-3.047831,9.385817,-0.429917,0.268447,2.533792,9.407046,-4.954710,-8.909298,5.767050,9.999623,-9.906121,6.837125,-8.016327,-5.532935,7.878332,-3.568204,0.633383,3.117364,-1.217713,7.549780,5.188910,-7.349111,-0.570277,-7.032290,0.656911,-7.442266,-8.269751,-7.765385,1.093165,4.059644,2.970139,-7.165612,5.518736,-2.852508,-7.098248,-3.679815,-6.018391,-2.931703,9.427362,6.335091,-9.149322,-4.135196,5.982709,0.384928,-5.002354,5.720258,-0.230139,-3.841136,0.315472,4.935756,-4.343258,-9.386003,9.514649,7.716451,0.557732,0.536167,-4.656650,-7.648376,-9.425601,-6.065604,9.604328,-2.241183,-7.461089,7.133126,-7.118324,0.028918,-7.872868,2.642959,-6.731265,1.027175,6.475164,0.015366,-6.841125,1.900989,5.742037,5.120531,-4.030717,3.455742,6.663427,-6.474659,1.970955,-9.774507,1.870872,8.375657,8.830650,2.422811,-2.726942,-9.236407,0.892714,7.373921,-8.494380,0.790830,2.256831,1.216447,7.636076,-1.314903,7.593478,5.165755,-3.182969,1.616182,2.358339,7.604113,2.674176,-3.530312,5.195741,-4.673808,9.413906,-8.625999,-0.199452,0.977204,-4.801045,-7.079748,-4.071701,-7.434326,8.840802,-8.043683,4.086041,-7.229669,-9.675297,5.841241,-1.138798,6.799254,8.685026,-3.779050,9.127189,0.103208,2.985751,5.959187,6.551428,0.698942,1.667566,5.344923,7.381229,-6.030370,0.312992,3.895496,4.827847,7.378737,6.538025,-5.690167,6.327150,-3.100568,0.204988,-9.057083,5.685464,3.015301,-8.219274,2.741109,-5.964573,6.862951,0.450749,-9.916589,5.683803,9.721148,7.874150,3.940120,-6.433419,-4.509520,9.593750,-1.500462,-8.053497,-5.965200,1.926088,-4.173444,8.546256,7.442107,-3.367996,9.520245,8.370385,-9.474813,-2.766503,6.673932,9.150103,-9.225989,-5.066075,-8.706201,9.237697,9.206857,-7.579822,-7.617303,6.597351,5.442746,3.715609,1.853514,8.293418,-6.047293,5.725592,-0.164203,4.013367,-3.044073,-2.912931,-3.620451,1.740689,-0.673950,5.897604,6.483833,-1.719513,-5.845696,8.708964,-1.933249,-8.216560,-5.304193,-1.298913,-0.794203,3.722359,2.296197,4.963601,6.419514,-7.856871,1.969678,0.259375,-6.754033,5.043048,7.091900,8.678437,8.678922,-5.247701,3.838953,2.006072,-8.338907,-7.914764,-8.391678,0.589806,-0.995166,6.350627,5.376191,-1.409721,-5.319676,2.781426,-9.470312,3.126749,-2.373034,3.472938,-8.474129,1.957462,-3.175954,-9.830562,-5.572295,-5.499471,7.151884,-4.807981,-6.381229,6.734038,-8.779018,9.036653,1.034545,-5.375924,-2.153494,1.551804,-3.852114,-6.355112,5.910716,3.876163,-4.666178,-5.533836,1.570413,2.149713,-4.597597,-0.086274,0.265172,8.200221,-0.980235,-9.133307,-8.951286,0.721753,-1.172501,9.507485,3.879969,8.416428,-2.800065,4.321246,-1.964913,-3.067901,2.227324,0.517131,-3.140446,9.127980,6.195787,8.151147,-7.456486,-7.485146,-9.264137,-9.157853,7.589185,-5.121441,4.736470,2.504644,-9.310181,-0.820728,1.874907,-5.300565,8.923272,-6.169016,7.647636,-1.756389,4.825558,-5.395415,-8.964532,1.233239,5.967991,2.493309,4.795117,-9.191277,-9.786824,-0.127423,1.369205,6.025912,-2.172887,7.780045,-4.398334,7.749643,-7.602880,6.113595,-4.393760,-4.818313,-5.300365,5.152181,2.246501,4.653479,-1.959680,6.995154,-9.121144,-5.484775,-3.288486,-4.536714,4.822438,-5.992853,-9.948519,-8.363343,-7.653655,-7.987965,3.685054,2.110852,5.975435,-2.742052,-5.909218,0.485836,3.522293,6.981170,8.182584,-2.443029,-7.316322,0.853233,-8.116118,3.945648,-0.955492,-4.192457,9.430050,-7.050609,-8.101909,8.987509,-7.156104,-3.277674,-4.112919,-1.765973,3.701993,5.094052,1.207199,-0.263299,-6.178418,3.861742,0.818815,-9.857863,4.080266,-8.450085,-0.185877,-6.520851,-5.914515,-5.903581,-8.477838,3.564675,2.414770,5.306855,6.026715,-9.328460,-4.142387,-4.725254,3.363186,-6.493986,-3.904062,2.425079,-3.960358,6.106293,-3.973650,-2.618673,-7.203307,-3.044906,-3.971359,3.256135,-2.266395,5.535332,9.069775,-9.325517,1.304982,5.281457,5.641020,-3.388788,-9.243732,6.589864,4.464188,9.715855,9.000174,5.344865,-7.208023,6.802797,-8.247931,6.331762,-4.567603,0.942582,-3.127656,6.268467,4.095188,-8.357815,-3.144191,-6.780390,9.039895,0.981457,1.018809,-2.256509,6.971496,-6.453877,-9.737982,1.708527,-2.433967,-9.735171,0.522146,-9.990810,7.120953,-4.031755,-0.595666,8.728831,1.257226,-8.458974,5.916438,-0.719969,-0.729754,6.887283,-0.800881,-0.512058,8.157030,6.721497,-7.067849,1.441903,-6.168453,7.358130,-4.357033,-1.552331,-5.883252,-4.165862,9.259231,-7.837296,-7.301655,7.199546,1.119904,9.564476,-4.586414,7.843026,-1.769723,5.746433,6.981231,-6.062543,8.392596,0.124783,5.539692,-9.828983,-8.118091,0.646215,-3.535598,1.509775,-9.567986,-7.904403,2.707977,9.940364,-9.919763,6.033576,-5.449932,9.957239,-9.620964,5.867106,-8.725569,4.577393,-1.066787,6.203897,1.764426,-4.040543,1.324021,-8.975430,1.850236,3.531258,-2.253320,0.187562,-0.022724,5.946882,7.429443,-1.083768,-7.356187,-1.989767,-4.154847,0.040645,-7.300877,1.534523,-6.155490,-8.132251,-2.520897,6.878532,-7.000937,9.323389,2.637444,-9.603981,8.582976,-0.926715,-1.149828,-5.322953,2.432515,-6.727241,-0.016802,3.718822,0.477452,-6.608088,3.767263,7.434592,-9.495932,-0.211442,8.801257,-1.601734,-0.503776,-6.570761,1.628423,8.494605,-6.951493,-5.882223],[-9.121314,8.978225,7.225824,0.668466,3.046903,2.603489,9.370599,1.905202,-2.531015,1.341152,-7.191134,4.442643,-3.299175,-2.761789,-9.660662,9.759778,3.717094,-8.954447,-7.548228,8.077848,-2.832697,5.963657,4.412737,-8.704049,-3.705686,-4.492554,2.290572,-6.983719,-3.911903,-1.179469,3.801076,5.103467,-2.687345,-1.014482,8.413221,-0.677978,-1.950856,2.758698,-4.830904,0.419382,1.863689,-4.169995,5.412482,3.155353,0.658859,-0.820056,4.453558,3.897637,2.148836,8.318812,-1.532981,8.856315,7.709058,-9.724026,-1.151837,8.489433,2.421492,1.517957,-7.958362,-7.558860,-2.616587,1.786172,2.340795,-3.176151,-4.847560,3.146004,7.668165,9.393361,-8.241888,7.566779,6.910969,-3.918716,-5.015827,2.644671,-7.134715,-5.684834,-3.259724,4.490205,2.781948,-2.588586,7.154744,-6.060951,-6.617175,7.268869,8.073602,-7.343993,4.265774,7.285603,-2.497533,4.658310,-4.962627,2.234773,6.306756,-1.480037,-8.668145,-6.571105,4.459817,2.864809,-1.286398,-4.759350,3.028712,-9.674018,5.324234,-8.039855,-0.305028,5.603573,5.264182,9.071153,3.805328,1.828014,-7.454630,8.288271,-4.445444,-2.275979,3.441354,-7.725009,0.543467,-9.391000,-4.371096,-8.459761,-0.952078,-4.432702,-7.968607,-0.939294,4.429601,-7.672691,1.619776,5.528133,-7.312896,-6.103222,-7.326616,-2.175596,3.481219,1.297717,0.035375,-2.092994,3.637408,0.714159,-1.415110,9.770980,-7.316712,7.935046,7.621174,3.193686,-3.595522,6.853827,9.211845,-8.983704,-6.663636,-7.020121,5.340190,6.789950,4.107548,2.229452,-9.391057,-0.041344,-2.114257,-8.724456,-8.793077,2.485721,8.735507,-3.772591,-5.281104,3.156714,-5.382739,-6.046847,-2.947874,-5.877070,-1.920476,0.574844,-5.035629,1.722424,-6.569443,-0.266643,-8.337367,2.777955,-3.335880,-1.301730,8.211194,-7.192654,8.093486,3.662083,-9.373543,-7.974928,9.823397,-7.310114,7.782668,-9.260714,5.948373,-8.703970,-1.284133,-6.207549,3.074065,3.864050,-7.848427,-6.070377,-8.867514,-0.730476,2.493097,-0.529507,-2.562497,-3.129325,-5.823099,2.391924,6.067891,2.970406,-4.688770,9.468654,-4.298776,-6.772734,-1.485289,1.903205,-6.946749,8.796613,-0.480707,2.767362,-0.315250,-7.008428,-5.891983,3.471782,3.796192,-9.611032,-8.866923,-9.851965,-3.235264,6.312678,7.631317,-6.822220,-2.963019,-3.631168,8.993644,-2.811070,9.206886,-1.930910,-9.256004,-1.929653,5.015799,1.789262,-7.941630,-4.731711,-4.501229,3.243236,-0.659661,-8.417218,4.408891,4.689548,-8.071423,3.824043,-1.566635,2.805182,9.130244,8.709671,-0.251416,-5.516923,-1.774399,-8.817425,-5.869323,-6.223455,5.527078,-1.104730,4.346175,2.082518,7.047014,-5.543994,-7.048534,-1.923371,1.167262,-8.258638,6.637355,-2.259345,-8.939152,-9.304707,-4.775481,3.590549,1.856078,-4.078317,-8.896833,-8.962806,-6.614353,3.601600,2.706873,-1.592950,0.065152,-8.522388,7.951005,-3.548521,7.889534,1.862391,-6.915150,1.384974,-6.512858,-9.752127,0.972883,-3.988739,7.113019,6.011814,6.405133,9.866202,-1.173242,5.761180,-3.494638,5.130844,7.447225,0.590805,-7.863035,1.887589,1.117620,3.091301,6.783089,-1.534269,7.490746,9.323954,-2.310657,-3.287245,-9.017715,-9.374051,8.352537,8.537237,-5.596433,-5.087763,3.434866,5.378168,-6.551984,-5.395357,-3.691605,-8.543614,-6.674823,5.768597,1.132630,9.744282,1.732032,-3.300658,-0.772291,0.617776,6.898716,8.090049,-2.765327,6.139074,9.390433,-6.374407,-7.750821,9.883508,-6.660088,2.777664,-8.357858,1.734126,6.399336,0.171244,3.503336,-4.020239,-4.538403,-8.215781,6.581005,5.069150,3.041957,-5.270956,7.046385,-3.424036,-8.039504,1.464144,-6.354158,8.279961,-0.830605,3.337786,2.286420,-1.548819,2.115189,-0.586616,-5.287338,8.069854,5.910057,-7.622347,-7.284140,-3.666059,-1.213960,7.331843,6.264561,-3.065316,0.603007,9.489032,-5.230954,3.768970,-2.769970,-0.461346,2.646981,-1.156764,6.434916,4.218663,0.398671,3.900440,6.741010,9.836042,4.117945,7.888016,0.598025,7.888726,-6.119354,-9.580777,9.569058,-1.739599,-6.481922,8.625224,1.982120,9.483094,3.618153,-6.445664,-2.597634,1.022098,-2.865150,-2.785942,8.986344,1.531246,-4.520968,7.375019,-3.595237,1.886954,-5.432527,-4.098259,1.928219,8.827092,-0.794995,-4.433479,9.981629,-9.852921,-9.154989,1.989678,9.933403,7.080820,-0.962751,6.141932,-4.271009,-4.909725,0.977952,-1.917439,-9.956756,7.234418,-0.682221,3.535293,3.694759,9.508469,1.464616,-6.899379,6.996422,-1.278403,-5.353526,-5.437702,-0.188852,3.333980,4.372758,1.313151,3.548109,7.034487,-6.085795,9.422053,-9.512330,9.824823,-2.685130,-4.484001,6.428179,4.578266,-5.667245,2.330304,-3.405067,1.836696,-2.254189,-6.240937,6.481258,7.771393,-0.414776,-4.645484,1.214423,-2.986308,8.830461,2.775259,-9.742275,-0.483721,-6.104435,5.882821,-5.490401,4.806421,4.952184,2.115206,6.375611,-6.913851,7.804595,-9.255376,-1.879665,-7.506405,-0.986072,6.548000,0.299831,2.167007,6.918087,-7.099352,0.607913,-8.935256,7.965116,-4.027821,3.704110,8.684284,7.039617,8.514632,-8.247878,1.980232,-4.001568,2.867151,-2.094609,9.599413,-3.079600,5.601065,9.340726,-3.517591,7.739150,3.336713,-9.648483,-6.089994,6.700981,3.175999,7.417931,-2.538938,7.581324,1.561661,-0.942445,6.826708,3.008384,2.533985,7.135777,7.260535,-1.326207,1.363301,1.280507,-3.453177,6.110440,9.709306,-9.728242,-8.197445,4.314833,1.287789,0.077656,-9.958693,4.544823,9.650132,-2.579959,-5.811315,-2.356374,7.898482],[3.132891,-0.237586,5.603056,1.380588,2.158179,-8.313576,-7.690790,-9.999401,-1.487112,-8.318387,-3.976752,-0.571767,-3.500728,0.482406,-3.249046,2.305126,-1.898904,0.942938,4.040759,4.146678,-9.425717,8.147996,3.472504,-3.662598,6.063399,-8.605263,9.529009,-4.336078,7.914383,-8.329054,-4.140408,2.766042,5.212426,-4.953729,9.840612,1.577005,2.105245,-0.304701,-5.138996,6.117290,6.300278,-6.566187,-7.603439,2.549351,-2.299796,-6.993344,8.905171,-0.391534,-4.447279,7.309382,-0.641106,6.207645,7.262354,9.538118,1.784144,7.000670,-6.626482,9.474849,-4.980269,-5.692181,-4.675987,9.960838,-7.559745,-5.703780,6.860706,-1.018270,-0.525314,7.097836,-5.612234,1.386440,5.882859,-5.201155,-0.963129,8.425829,-3.027351,-8.027336,-7.594100,-1.901837,1.475806,1.556669,-9.516415,-7.774726,7.223805,8.673895,-3.902128,2.476146,2.850528,9.989045,7.215928,4.780465,-4.862400,-7.556396,8.218546,1.412085,6.568124,1.209307,3.698928,-0.544669,-1.017615,-8.006461,2.918581,-9.745901,9.328652,-5.548369,-4.390914,4.786620,3.746740,8.123026,-1.252114,9.784770,0.699644,-5.285172,8.722178,-7.863305,-1.486806,-7.791178,-0.078998,-6.284482,0.454540,3.630637,-7.518930,-2.597338,-9.024162,0.619882,2.461572,1.451749,7.861701,3.412125,-1.375237,-0.413387,-6.631215,-9.862008,-8.520613,-4.416070,-2.735690,4.044899,-2.803962,-2.349121,-8.103049,-5.020511,6.237628,-2.139498,0.203873,9.797238,4.375763,-7.451781,-4.149077,9.659492,3.506538,-8.065565,3.762416,9.919526,-4.455707,-5.188566,2.050311,-3.676335,-5.824932,9.782573,-4.887254,-5.062635,3.095142,1.979443,7.506078,-4.199763,-5.517163,-1.337336,-8.557319,-2.164969,-3.806048,6.984721,9.227451,-5.236414,1.944569,3.650527,-0.320789,3.850998,-2.974554,5.684485,7.929658,-6.502147,5.285457,5.846156,-6.515967,-2.021091,0.463837,-1.682502,0.014604,-5.309242,1.605606,-6.402034,0.186923,2.236047,-8.494313,-6.143831,-7.508007,3.786522,3.974276,5.419303,-4.296116,-5.767142,-8.634888,-0.370280,7.187289,-9.789047,-4.608764,-8.525860,-2.842805,4.618315,8.928276,9.097760,8.698883,4.251642,0.252459,-1.190983,-0.597080,8.742892,-3.373060,-3.504350,4.242750,-4.775440,3.368037,4.574425,-1.750934,-1.823131,-6.897836,8.312527,-8.032361,3.395706,9.045453,-2.493426,-9.739363,-6.692823,2.699946,5.052613,6.382506,0.481097,-8.841225,7.957460,9.226198,-2.533922,6.440910,7.768482,-8.507415,5.817644,0.816740,4.420811,-3.962129,-5.690563,-8.628266,-7.653215,2.979735,-1.813659,-1.451359,-7.627444,7.527263,-6.373950,-8.504187,4.504372,-3.155100,-2.369101,-2.445039,7.318256,-2.419637,-1.546765,5.283006,-0.746855,-2.314359,8.158113,-9.504251,4.975971,-3.262108,-5.288215,1.038927,-8.826517,8.489673,6.797214,-8.771152,-6.199776,-9.944198,-1.979427,1.074381,-4.870056,5.568447,-7.084258,4.808882,-8.236045,7.703837,-5.445819,-0.553859,-6.138369,-0.971009,7.317508,7.540479,7.022223,-3.021579,9.032800,-8.301375,-3.177081,0.303786,-7.347801,-0.609288,5.206315,9.643754,-9.092125,-2.954251,8.916576,8.022833,2.882334,-7.013353,-2.961880,-4.114406,-7.651940,-3.611777,9.536260,-8.217470,-4.986871,-9.014017,-8.171337,-6.604397,0.128156,-4.456523,9.177656,1.230601,-1.777673,8.569456,-5.398934,-0.859717,-8.462612,0.216084,1.281245,1.515005,-4.226644,6.611939,-5.877199,-6.256887,-3.916395,-5.653727,-0.251165,-8.454160,-8.723419,3.837607,-5.699737,5.127684,-7.928419,-2.779525,-3.542037,-3.705105,5.270795,-0.755279,6.292981,1.486518,9.820272,6.577623,1.106566,-9.226690,8.418414,-3.613916,6.958970,-9.033475,8.238315,6.724712,1.744889,-8.784055,6.795327,-3.544911,4.568955,-8.913856,4.423605,-3.467429,-8.875536,-8.606489,8.044085,4.783824,1.759616,-8.820227,-8.699180,-6.304640,1.659483,-2.214888,0.860290,7.525226,-3.241130,2.467310,4.209375,-0.883150,-1.063075,0.926851,6.621128,8.065524,4.759962,6.732641,7.440264,0.021865,0.612829,-4.894667,-7.710093,1.846145,5.686441,-2.582331,3.149721,-7.538290,-1.802756,9.538179,-2.620702,-7.656483,-4.654999,3.806745,4.935278,3.948352,-3.467228,-8.680289,6.861406,1.529437,-5.735408,-2.388979,-2.827281,-3.962239,-1.477806,5.629469,-3.222314,-9.514354,8.798361,-9.084434,-0.857243,7.378785,2.972376,8.828905,-2.632836,-3.015567,9.363597,-8.542059,4.953438,-3.665748,-5.347957,1.438732,3.954763,5.184601,3.431548,5.981785,0.317521,1.996731,-5.008112,-9.419537,2.806981,-3.159318,9.047027,4.604629,4.141782,-6.515531,0.122239,-8.500981,-1.634698,1.192761,2.733681,1.734774,-0.784919,-1.935464,-8.513588,1.679857,9.210381,-5.756898,-4.640875,8.333905,7.386501,9.776259,1.635211,1.732580,2.363742,-1.739779,9.561490,-3.547099,-6.246501,7.069314,6.095278,-2.416100,-4.105537,4.500934,-4.281550,-8.187319,-1.578590,-7.756327,1.336150,3.709895,1.853042,0.661530,-2.717662,-4.426948,-6.957212,0.527893,-2.402997,-7.995324,-0.647821,3.674373,5.326030,-7.628174,6.070033,2.106958,-7.622918,5.518519,-7.155384,-0.751095,-1.826855,4.638125,-9.581111,-3.000403,5.778488,2.726798,-3.509220,-1.591076,-2.778993,-8.400525,-0.329720,-5.920707,-7.783708,-6.346662,3.398002,9.300960,1.824590,-0.334394,9.515509,-4.271109,-5.662526,-5.021550,-9.151944,-9.588372,0.012411,-0.582321,-3.954075,-5.989267,-7.884879,-6.173195,-7.941041,-1.590166,-3.438778,7.423674,0.389972,-0.533470,-6.000984,5.521071,-5.291376,6.159771,-8.417136,3.585791,0.611754,2.736776,-2.012711],[2.726337,-3.766584,-1.273372,-5.325777,-0.301485,9.185274,8.010050,-3.739134,-6.708492,-6.110293,-6.731148,0.099249,-3.848692,-3.768659,-5.190880,8.359698,5.368874,3.650493,-9.151279,1.471788,-6.391427,-5.942174,-2.512551,-9.273156,1.742224,5.677307,0.937756,7.576086,5.352852,9.452330,-1.386888,4.678930,-5.065172,5.461142,-2.678966,-7.076681,4.986914,1.678994,6.872048,-3.628445,-4.285039,-6.812621,-7.918192,2.210151,4.512158,3.546776,9.713246,5.356784,-8.065387,6.851197,-0.863875,1.806620,-5.593662,4.726815,-9.192584,-8.511064,5.610697,-7.164425,-1.984111,7.037475,-7.798817,3.541917,9.397798,-0.726492,6.055628,2.548936,3.726033,7.224562,9.783103,7.082940,-5.595018,-0.274349,-4.214162,8.924789,9.019104,0.539900,0.007862,1.128912,4.912584,-4.264110,0.238948,-0.634258,-5.401449,-6.787956,3.110531,2.203529,2.155445,1.995767,-6.142857,-7.129127,-6.758424,-3.084402,-7.197611,-8.405852,6.556837,-6.284182,-9.015844,9.858466,-2.598242,-7.889503,0.275533,1.937408,-0.230931,-5.289709,6.040644,-6.733675,-0.595261,-6.876764,-0.848249,2.924864,1.354294,7.184945,-0.925941,9.718131,-6.511372,-1.960687,3.190046,9.857601,9.151698,7.605303,-8.063153,-2.576550,-6.020095,-9.302910,0.633370,-1.182450,1.880967,3.204503,-2.575698,8.088495,-8.886261,-9.758910,3.786007,3.439904,3.903353,-3.153841,-6.877416,3.354414,5.991740,-4.585226,3.506392,6.271138,-9.073303,-4.421546,6.256489,0.771194,-7.162858,-4.450061,7.476518,-9.135407,-6.022252,9.558336,3.104094,0.625463,-2.191150,1.154993,-3.488984,-2.977064,1.474468,5.072311,-9.317248,6.886880,-6.424933,6.956014,8.049226,-2.185224,-3.801190,1.411096,-4.075882,-5.349776,-0.550419,-5.460244,-8.768477,8.368255,-6.886474,5.534179,0.531469,5.459238,-6.087661,-7.288326,-3.354722,4.606909,-2.005662,-5.525942,2.558474,8.300910,-1.099503,-4.812899,-0.491097,0.286436,-7.306560,-5.365100,4.850496,8.782213,-4.920003,5.649779,-1.851532,5.165767,1.955747,-0.600824,-5.093151,-1.647962,9.190931,8.473031,-2.055188,-7.501945,1.154792,1.438883,-6.244745,-2.761538,-5.928665,1.880327,-2.940393,3.499872,-7.910062,-1.096903,9.678480,-7.718542,7.154537,-3.503048,-9.677853,-7.206099,1.873252,-6.844645,-7.442366,-0.272777,-2.950369,-1.238744,-3.347143,6.896507,8.680403,2.640670,-0.051047,8.509823,-1.955503,-9.754540,6.134003,-1.586073,-0.934382,-6.688258,-1.433047,0.642861,3.622249,4.699811,6.501567,-3.876102,0.128160,0.871539,5.431283,5.640766,-7.680637,-9.924875,6.226570,0.487417,9.281063,-7.757557,-6.912931,5.259244,8.349291,-3.087727,9.195510,6.294330,-0.472798,-3.372218,-7.238245,2.240082,6.952460,-0.225588,9.276099,-6.459829,2.274785,-7.333261,-2.698910,2.455125,-1.422309,-6.497303,0.974950,-1.738012,-1.155528,3.413891,1.225641,-8.250834,1.725318,0.934139,-5.693018,9.658261,-4.671026,9.431264,9.667591,8.483750,-8.167940,0.793857,5.117543,-3.747150,7.490032,-1.902094,-3.823763,6.670031,6.850444,-4.932680,0.040136,-9.705678,0.730417,-5.767332,-2.443260,9.599482,-8.527014,-0.477403,-4.254896,9.047028,2.983790,-8.865189,-0.501057,2.392002,-6.903137,0.683029,9.076220,-7.301724,-2.785321,-8.848635,-4.989798,6.713476,-3.188920,-8.850779,-1.523981,-0.625498,-2.678317,-3.744827,4.644299,-5.982908,9.773006,0.478653,3.330995,-5.696239,-3.437095,0.462153,-6.751365,9.261314,-3.282298,4.521861,-8.584227,-6.092113,1.902507,2.328668,-9.121034,-3.728700,-2.308975,0.930910,0.413049,3.269970,-4.451206,-3.012564,6.509131,0.975497,-9.796516,7.394593,2.589399,4.758729,-5.197194,7.113267,-7.127375,-0.114241,1.124123,0.401101,6.640665,-7.565654,5.145671,-9.772285,6.763646,-0.077261,4.914615,-7.806205,-9.752725,0.253255,-1.365072,4.409319,-5.138480,8.412324,2.188164,2.678352,0.556546,-5.063540,-4.198045,-6.062836,8.598047,2.144960,-1.956726,0.290386,5.442361,2.008247,1.316937,0.874649,-8.260109,2.624024,7.999412,0.905627,-3.616428,2.549404,-3.442584,-0.827679,-1.113204,-9.134270,5.473693,6.091698,-1.572721,6.280492,-0.939923,-3.548642,1.327511,-6.254411,-8.912482,-5.652107,-0.510247,7.864048,0.452275,-8.972897,-4.295958,-0.080021,-2.083786,-9.529704,-3.026838,-2.675273,-6.676984,5.355013,-2.151522,-1.305511,5.424440,3.985885,-4.967094,0.661511,7.735591,-7.733185,-4.651214,7.425251,-7.953880,-7.990181,2.965965,5.472084,8.707689,-5.917508,1.822258,-3.938898,3.637388,-7.952903,-6.476074,5.323960,9.691201,3.835376,-9.966603,-8.714431,0.990348,4.651087,1.377358,-9.797133,7.575391,-8.919004,-8.162254,-4.544079,-3.560244,7.972258,-1.590253,-4.691398,-1.334425,1.476826,1.074760,-8.321130,-5.605859,6.407057,-2.832203,-6.308913,-6.416966,-8.941956,0.371639,-7.552286,2.023298,7.043515,-0.180274,2.301745,8.675304,7.705275,-3.510124,7.498734,2.572914,-1.707700,1.724965,-0.183833,6.964911,-5.616418,3.688434,4.858927,-2.534627,-3.121118,-5.123082,-1.349074,-3.417011,-8.517555,0.018170,-1.956551,6.009866,-2.909053,1.356551,-9.633855,-9.192651,-4.178789,-4.974670,-9.901115,-4.404486,9.952303,4.592049,-3.760296,-4.302562,-7.670481,6.992501,-4.274726,-2.979896,7.515792,6.389877,-9.716880,-6.278269,7.290616,-8.265355,2.071404,-5.161733,-0.909294,-3.461876,-9.226286,9.627507,-8.818446,7.043687,8.493811,-7.586680,3.362956,6.435737,2.843658,-8.300558,-1.490993,-0.580289,5.952571,-6.573374,-3.149328,6.410964,6.811881,-2.411469,2.122195,2.228843,8.150523]], dtype = "float64")#candidate|11178|(8, 546)|const|float64
bop_11179 = relay.minimum(var_11162.astype('float64'), relay.reshape(const_11178.astype('float64'), relay.shape_of(var_11162))) # shape=(8, 546)
var_11187 = relay.var("var_11187", dtype = "float64", shape = (8, 546))#candidate|11187|(8, 546)|var|float64
bop_11188 = relay.right_shift(const_11178.astype('uint16'), relay.reshape(var_11187.astype('uint16'), relay.shape_of(const_11178))) # shape=(8, 546)
func_11016_call = mod.get_global_var('func_11016')
func_11017_call = mutated_mod.get_global_var('func_11017')
call_11193 = relay.TupleGetItem(func_11016_call(), 0)
call_11194 = relay.TupleGetItem(func_11017_call(), 0)
output = relay.Tuple([call_11121,var_11126,call_11153,bop_11163,bop_11179,bop_11188,call_11193,])
output2 = relay.Tuple([call_11122,var_11126,call_11154,bop_11166,bop_11179,bop_11188,call_11194,])
func_11197 = relay.Function([var_11126,var_11162,var_11187,], output)
mod['func_11197'] = func_11197
mod = relay.transform.InferType()(mod)
mutated_mod['func_11197'] = func_11197
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11197_call = mutated_mod.get_global_var('func_11197')
var_11199 = relay.var("var_11199", dtype = "int64", shape = (390,))#candidate|11199|(390,)|var|int64
var_11200 = relay.var("var_11200", dtype = "float64", shape = (8, 546))#candidate|11200|(8, 546)|var|float64
var_11201 = relay.var("var_11201", dtype = "float64", shape = (8, 546))#candidate|11201|(8, 546)|var|float64
call_11198 = func_11197_call(var_11199,var_11200,var_11201,)
output = call_11198
func_11202 = relay.Function([var_11199,var_11200,var_11201,], output)
mutated_mod['func_11202'] = func_11202
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6187_call = mod.get_global_var('func_6187')
func_6188_call = mutated_mod.get_global_var('func_6188')
call_11207 = relay.TupleGetItem(func_6187_call(), 0)
call_11208 = relay.TupleGetItem(func_6188_call(), 0)
output = relay.Tuple([call_11207,])
output2 = relay.Tuple([call_11208,])
func_11219 = relay.Function([], output)
mod['func_11219'] = func_11219
mod = relay.transform.InferType()(mod)
mutated_mod['func_11219'] = func_11219
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11219_call = mutated_mod.get_global_var('func_11219')
call_11220 = func_11219_call()
output = call_11220
func_11221 = relay.Function([], output)
mutated_mod['func_11221'] = func_11221
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7639_call = mod.get_global_var('func_7639')
func_7641_call = mutated_mod.get_global_var('func_7641')
call_11240 = relay.TupleGetItem(func_7639_call(), 2)
call_11241 = relay.TupleGetItem(func_7641_call(), 2)
output = call_11240
output2 = call_11241
func_11246 = relay.Function([], output)
mod['func_11246'] = func_11246
mod = relay.transform.InferType()(mod)
output = func_11246()
func_11247 = relay.Function([], output)
mutated_mod['func_11247'] = func_11247
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8581_call = mod.get_global_var('func_8581')
func_8582_call = mutated_mod.get_global_var('func_8582')
call_11268 = func_8581_call()
call_11269 = func_8581_call()
output = relay.Tuple([call_11268,])
output2 = relay.Tuple([call_11269,])
func_11304 = relay.Function([], output)
mod['func_11304'] = func_11304
mod = relay.transform.InferType()(mod)
output = func_11304()
func_11305 = relay.Function([], output)
mutated_mod['func_11305'] = func_11305
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5674_call = mod.get_global_var('func_5674')
func_5676_call = mutated_mod.get_global_var('func_5676')
call_11348 = func_5674_call()
call_11349 = func_5674_call()
func_8402_call = mod.get_global_var('func_8402')
func_8405_call = mutated_mod.get_global_var('func_8405')
call_11354 = relay.TupleGetItem(func_8402_call(relay.reshape(call_11348.astype('float64'), [15, 9, 6])), 0)
call_11355 = relay.TupleGetItem(func_8405_call(relay.reshape(call_11348.astype('float64'), [15, 9, 6])), 0)
func_4652_call = mod.get_global_var('func_4652')
func_4658_call = mutated_mod.get_global_var('func_4658')
const_11366 = relay.const(-2, dtype = "int64")#candidate|11366|()|const|int64
var_11367 = relay.var("var_11367", dtype = "int64", shape = (1, 364))#candidate|11367|(1, 364)|var|int64
const_11368 = relay.const([-4,3,-8,8,-9,5,-2,10,6,-10,4,-8,6,-3,2,6,-4,4,5,-5,-8,4,5,-9,1,-5,-5,-1,1,-3,9,-9,-2,8,4,10,4,-1,-9,-1,-8,-5,-1,3,-2,5,10,6,-8,9,-8,3,6,2,-2,6,-9,-4,9,10,-6,5,-10,9,-3,-9,9,4,6,9,-7,10,9,-4,-1,-10,-1,6,5,-1,-4,-1,2,8,-9,6,5,-2,1,-1,-2,1,7,7,3,-2,8,-1,7,10,8,2,3,-8,-1,7,1,1,7,1,7,8,7,8,3,-9,-4,-6,6,1,2,-5,6,-2,5,3,-9,7,-4,-9,1,-8,1,-1,-8,6,-10,3,-6,-9,10,-1,4,-4,-3,5,-1,10,-7,-8,-5,4,-5,1,4,10,-1,5,-3,6,-2,-3,-4,-4,5,-7,-6,6,-8,3,-7,7,6,-5,-9,-6,-2,3,-1,6,-10,-6,3,-8,-1,2,3,-7,-1,9,-5,-10,-3,10,1,10,8,8,10,-2,-6,-10,-6,-10,-9,-7,-6,-1,2,-3,-9,6,10,9,-1,-4,9,-8,1,2,-8,6,5,-5,9,4,2,7,6,-6,9,6,2,-3,-1,-2,-3,3,6,-9,-5,-4,4,10,9,9,-6,6,-8,-10,5,5,2,7,7,4,-6,-10,-2,-2,-8,9,-5,-1,-5,1,-7,-5,6,7,-8,7,1,-6,-8,4,-9,-2,-7,9,-6,-9,7,-1,7,-8,3,9,-3,-7,-3,-8,3,9,3,-9,8,-1,1,10,4,-3,1,8,-8,4,-7,6,-2,-7,2,-5,3,5,-10,4,-1,10,10,6,5,9,-4,-2,-9,3,-5,10,-4,4,8,-7,-6,2,7,3,-2,3,-7,-4,4,-8,4,8,2,4,-1,-10,-10,-10,10,6,-8,-8,6,1,-7,-10,6,-1,-2,-8,-7,-8,1,-1,-3,-5,-8,6,-4,5,-8,6,-4,4,-1,-9,-1,5,-6,4,-3,-2,1,8,-7,-9,-7,10,-2,-7,7,1,-4,-1,-3,2,4,-1,-2,-10,-10,-5,-4,10,1,8,3,7,8,-8,3,-8,-3,-1,6,5,8,4,-9,7,2,-8,-5,-2,5,5,-9,-4,-10,7,-4,-5,-4,-4,5,-3,-7,4,5,6,-8,-7,-1,-9,-6,10,-1,-2,-6,-8,-10,-8,1,8,7,-6,-6,-2,-4,2,9,9,7,-5,-10,5,-3,6,4,9,-9,-6,8,3,-9,3,7,8,-3,-8,-7,2,6,1,3,1,5,-8,3,6,-6,-2,10,6,4,-8,-9,-10,-8,4,2,-5,1,3,-3,-8,9,2,1,-5,-4,-9,-3,7,-1,-5,6,-4,-3,1,-6,-5,-10,-6,-6,9,2,-4,-6,-8,-4,3,-3,5,4,2,-6,6,-7,-10,-1,-5,-4,2,10,8,-3,3,8,3,-5,-3,-5,8,1,-5,6,9,-8,9,-1,1,-6,1,2,5,1,10,-6,8,-6,-2,-2,10,2,-8,-8,6,-5,7,2,-5,-1,9,-3,7,-9,-2,9,-10,3,3,-7,5,-5,9,8,2,-1,7,7,3,-4,-8,-7,6,-4,-3,-10,-3,5,-4,-8,-2,-7,-2,4,2,-10,-3,-7,-1,7,-4,-2,-2,10,10,2,8,-1,-6,8,5,8,-9,4,-8,3,10,8,2,9,8,4,-3,-8,1,6,-6,-3,-9,-4,-10,10,2,-5,8,8,7,3,8,6,-1,-7,-7,3,-7,-5,-6,8,-5,-4,-7,8,-8,-2,6,8,-2,-6,3,-7,6,9,8,-2,2,-5,-10,-3,-6,5,-4,-9,7,-5,5,-3,5,5,-1,6,2,-2,-4,3,9,4,-10,-2,-10,-7,3,6,-2,-3,7,-4,-1,-3,1,-7,-3,-8,5,2,-10,-10,9,-1,8,-3,3,8,-6,-1,9,1,-10,-7,-10,-10,-7,1,8,-10,4,-5,-3,-1,4,-9,-1,-6,-9,7,3,-10,-10,10,-3,-6,4,-3,4,7,9,2,-8,10,5,-9,-5,-1,-9,2,-1,-8,2,1,9,-6,6,6,-8,3,4,-2,-10,5,-3,-3,7,-9,-5,5,-10,10,-8,-2,-5,-2,9,-9,8,-10,10,7,-5,6,-9,-1,1,5,-10,-8,1,5,5,-1,-7,-7,-4,-6,-3,6,5,-8,-9,-6,9,-3,5,2,-3,4,-2,10,-7,3,-1,1,8,-10,2,7,9,4,9,5,-7,-1,2,-6,-8,-1,10,4,-1,5,10,7,-4,-5,-8,-5,1,-5,7,-4,-10,3,6,8,-2,3,6], dtype = "uint16")#candidate|11368|(880,)|const|uint16
const_11369 = relay.const([-5.797814,-7.370420,0.399311,2.239301,4.226111,3.677126,1.828794,7.145727,0.353410,0.152069,2.755811,-3.451071,5.203952,-9.751398,7.006792,8.274610,0.721110,-0.932075,5.656989,-3.896084,-1.520393,-3.372263,-7.087087,7.098099,2.486044,-0.858849,1.735746,6.391238,-9.998018,-5.118593,6.166860,4.649430,0.913499,3.642466,-5.080204,9.510302,9.790264,-9.026016,8.558282,-0.479035,-5.262456,1.706507,7.634082,5.113272,-7.575669,7.431841,2.818895,-5.819065,-1.916438,0.844351,-4.639105,3.423059,8.479871,2.064940,6.286001,9.283601,0.008538,-9.129562,6.096402,-5.728775,8.748444,-3.822561,2.949992,1.363361,-1.580653,-4.597479,5.377717,6.483130,8.416731,6.671421,-8.669943,-7.129794,-7.251191,-4.402100,-3.577688,8.687631,-1.348974,-5.293897,6.720237,-9.359103,6.078301,-0.857318,-7.568634,7.277566,-0.266558,0.352031,8.728321,-8.846414,-8.626493,-9.978035,-9.368260,-7.025099,8.782909,-0.445007,-8.844952,-2.776119,0.970938,-9.487667,-9.841406,0.764395,-6.594646,5.953368,-7.353880,0.619555,-3.786957,-2.532412,-2.845437,-5.337092,3.403148,-2.699989,7.015049,2.292806,4.180044,-6.494918,5.770686,-7.740147,-5.607220,-9.593698,-0.802436,7.200337,8.165001,9.836498,-6.680741,4.036747,-2.627062,4.834617,-9.376615,-1.329499,-7.765537,-8.277518,-6.662753,-3.808793,-6.765203,8.697134,-0.914214,-1.622954,-6.529205,2.103419,9.984950,9.967748,-7.505364,4.570470,5.872249,-1.332910,-1.533209,-7.321948,-0.676883,-8.710318,9.502395,7.296746,-0.645030,7.875747,5.367638,-2.109116,9.697511,-4.318522,-6.192339,-3.300638,6.496586,-1.896384,2.242488,-7.690647,3.345977,2.293156,-2.548146,-6.083233,-4.053186,-8.976360,6.769438,-9.339608,-5.826602,-7.861793,-0.595271,-3.110546,-3.929679,4.790148,8.606328,0.719453,-2.128524,1.449303], dtype = "float32")#candidate|11369|(180,)|const|float32
const_11370 = relay.const([[8.284216,2.020736],[2.433913,-0.517996],[-1.511387,7.681579],[-9.660251,3.180820],[3.793900,4.052987],[5.933873,2.078857],[-2.488541,9.347645],[-7.496786,7.503463],[5.677512,8.796433],[-3.349199,-7.337515],[-9.646001,-7.681891],[1.830169,8.750508],[-3.773232,7.670109],[-5.162852,4.587860],[5.686581,3.070133],[9.496775,8.785451],[6.303096,-1.480516],[-7.150486,0.057642],[-1.771279,2.305540],[3.479999,-7.665751],[8.853552,-8.784161],[5.695551,0.680591],[-5.244238,-6.071542],[3.964367,-4.497264],[9.324165,5.710143],[6.258078,-4.953080],[-1.917889,-2.829821],[-0.876284,2.536725],[-5.088829,-8.322820],[5.596109,9.096834],[-8.448645,-4.781349],[7.852946,0.017452],[8.629121,6.120806],[1.080515,-6.336606],[4.324125,5.800270],[8.826361,-5.849384],[-0.718626,7.731505],[-8.319581,8.275814],[8.952865,-6.273109],[-1.750177,6.356722],[-2.610966,8.900675],[-7.698081,3.021023],[-5.305558,-9.180767],[-7.199978,2.432734],[4.186447,-7.714142],[8.096495,-1.172124],[6.758433,-8.984024],[-6.580595,9.738612],[-7.346567,-4.929488],[-4.910393,-7.517378],[5.761324,6.286837],[8.747623,-0.291923],[9.211271,-0.828038],[8.776552,6.804429],[-4.987494,-7.294507],[8.537516,9.181187],[-4.097197,6.989362],[-2.791748,4.332927],[-2.768379,4.022358],[-1.300838,-1.231031],[-0.898310,-5.924322],[6.328684,4.387317],[7.812979,4.289124],[1.679153,-6.854509],[-2.387521,8.079993],[-5.574450,-9.755438],[3.493386,-6.077525],[-3.118953,0.292588],[-3.415224,-9.879671],[-0.165233,3.275810],[5.405498,-9.169695],[0.841055,5.292314],[-8.686348,-7.409067],[6.372206,1.480183],[-0.412206,-2.082692],[-0.711358,-7.665403],[-9.198048,0.382428],[-6.643792,-6.554500],[5.167369,-1.777051],[-4.390806,-0.133664],[-1.451587,1.256514],[-5.227595,-3.520322],[-8.457998,5.224712],[3.463764,7.371073],[-8.050857,-9.112135],[5.066485,-6.751200],[4.239752,-6.055034],[-0.016199,1.627176],[3.797538,1.538271],[7.342637,7.277757],[-0.904748,0.330160],[-5.995275,0.482188],[7.507235,7.414070],[5.593436,9.964018],[-9.663858,-6.253811],[-1.686478,-0.363139],[-3.659966,4.812236],[6.927762,6.085554],[0.040978,2.502154],[-9.039714,-2.083495],[-6.577950,-1.593347],[-2.594453,4.926467],[3.541434,0.953514],[6.108637,-4.185436],[5.857928,7.459203],[-4.065407,7.545332],[6.845226,8.416372],[6.272227,3.670378],[2.740723,6.902629],[2.963366,-6.423930],[-0.522721,2.273126],[0.273927,8.593551],[8.332723,-3.787836],[-6.739883,-3.813309],[-7.018631,0.928051],[9.522907,-0.423257],[-0.829995,-0.338820],[-4.991403,7.541438],[2.558245,-1.800628],[-5.177940,6.983596],[-7.719854,1.256145],[7.938814,5.899145],[0.860498,-7.645912],[8.128476,7.366809],[-9.782011,-4.677686],[-4.760488,-3.260516],[-0.056644,0.909903],[-6.915234,-5.852998],[-8.953510,2.067739],[7.096524,9.596528],[1.456931,-1.135512],[-3.623851,2.187346],[8.665214,0.872726],[4.707849,6.708028],[-9.967640,-4.342021],[-4.894877,-8.421706],[-1.763969,-5.662460],[-2.906483,-5.711212],[7.666012,-2.156180],[-0.631963,6.273770],[0.504025,4.771186],[-7.319585,-6.019697],[2.885679,1.470546],[-3.130373,-1.875963],[-4.006008,-8.025237],[8.273700,-2.175388],[3.312515,-6.264226],[-5.146084,-4.645669],[3.813461,-4.182050],[-4.251314,-8.678495],[7.928325,4.651934],[9.802257,-8.716524],[5.598721,-2.435083],[1.489169,1.384936],[-6.077389,-8.797753],[2.173874,-2.182041],[3.006134,-7.929648],[-5.360503,8.301643],[2.538286,0.314830],[0.499910,-5.020560],[-3.801541,1.031641],[1.928272,4.918340],[-9.816387,5.483522],[-3.208653,-7.554167],[-9.694211,9.649936],[-6.309758,0.924296],[-7.427230,-7.110735],[-1.653634,-8.382685],[-0.891790,9.345468],[-2.658046,9.688119],[-0.431986,5.810224],[-4.847869,-7.541513],[-4.275542,2.315852],[3.256810,-1.011710],[9.839724,4.409380],[2.768109,9.448703],[4.010805,-1.383639],[5.851224,-6.616707],[-1.256251,-3.177940],[-7.126350,6.396774],[-9.274138,3.573298],[4.822458,7.480323],[-7.875752,3.930794],[-8.192434,5.414445],[4.765080,-3.248000],[4.937470,-6.083786],[-9.776698,3.429333],[-1.710038,4.174491],[5.624195,-8.097746],[0.428913,-0.864190],[-0.269424,8.958540],[-4.692857,-1.940292],[-1.076416,-8.978177],[2.054853,9.707108],[8.029161,-0.971210],[-7.226599,-2.658047],[-6.640085,-2.222397],[8.990865,-6.844903],[-0.122997,-0.243841],[-9.958558,-9.734862],[7.829651,6.408636],[-6.699074,-0.270197],[8.929781,4.197760],[0.752725,6.420401],[-9.065473,9.165992],[-0.456437,7.935678],[3.216208,1.681203],[-5.864929,9.035857],[-5.524105,-0.357540],[9.322158,-7.960813],[-2.801552,-7.526857],[-8.864649,1.812694],[-5.317738,-4.682554],[-4.683300,8.807563],[2.299855,-1.715129],[7.737048,-0.928314],[-0.271387,-2.532276],[7.299731,-1.494961],[-8.052808,2.645091],[-2.882364,2.764776],[0.074281,-3.393403],[1.487250,-1.320639],[-1.130607,-6.208557],[-4.243060,-1.490184],[4.260807,-1.998654],[7.220235,-1.507599],[-8.708861,-8.088180],[2.418565,6.095947],[1.668384,-0.978519],[0.666151,-3.193766],[4.087120,9.194124],[9.691725,-3.544578],[-4.487122,7.249936],[7.759498,2.615927],[-4.853788,0.276479],[6.117118,-5.440041],[-0.569680,3.389342],[6.406993,8.254174],[-5.388345,-4.443546],[-7.273915,7.176333],[-7.623202,4.711001],[-7.361222,4.221742],[-2.162887,-0.612535],[5.320819,1.650561],[-4.922349,2.807351],[-1.796832,-0.480031],[-2.373289,-9.883375],[-6.179432,4.700434],[-6.419124,-3.583248],[-2.313880,2.717562],[-4.054457,-6.882748],[5.094530,9.923353],[0.089226,8.791651],[-7.201113,-8.402517],[3.133832,0.578688],[-6.177822,-4.366976],[1.297972,-7.530156],[-9.018054,9.558889],[1.163403,-0.752863],[4.363616,-3.578694],[-2.421298,-4.317859],[-1.627542,2.330247],[7.448670,1.851602],[-7.553675,-7.891420],[-0.011494,0.878686],[1.512738,-0.772780],[-0.969100,9.262109],[-8.190248,-4.208414],[9.336889,4.301211],[-5.773088,5.460505],[-2.101422,1.601784],[-2.339511,-0.617327],[-9.981635,7.706712],[-7.241152,0.719846],[-8.227846,-5.023641],[-2.442197,-1.481605],[2.765308,3.526089],[-8.810843,9.139947],[5.677492,3.761900],[4.443210,4.877244],[3.464830,1.630070],[-1.704947,3.800048],[2.324143,9.441236],[-2.289834,0.714339],[-2.311242,2.271707],[-9.164243,7.143022],[-6.570471,7.704067],[-5.782194,5.408839],[-2.545838,-8.533572],[3.590895,8.107260],[2.912352,3.678259],[-5.945933,-3.261224],[9.978883,-5.877858],[-8.551533,-4.907036],[-9.722796,-2.116027],[-5.835686,9.881149],[-6.929274,3.104875],[4.688221,-3.181451],[9.854356,-8.470206],[2.558831,-4.247017],[0.304660,-5.562722],[-5.121792,-4.719537],[-4.062619,-0.029886],[-3.419585,9.703176],[1.255406,6.056467],[-8.135515,1.703042],[8.778224,5.193988],[-6.865616,5.689571],[-1.928119,-4.748036],[-6.251870,-8.140824],[8.308830,7.527813],[-9.382048,4.618326],[6.844817,-5.154077],[-9.837763,-3.797845],[7.373658,-3.281762],[1.928493,8.086299],[4.165001,9.945565],[-7.674665,7.191340],[-9.017384,-7.742940],[3.724389,-2.445293],[-7.425502,-4.096071],[-6.445673,-6.132470],[0.846428,-3.992204],[-4.470087,-6.280086],[3.817831,-8.384475],[4.044763,3.684506],[-6.200772,-9.603692],[0.951448,2.078085],[6.569838,5.984298],[-1.598126,-9.015413],[-3.137946,-7.337047],[-2.718228,6.224293],[-3.012807,-1.900423],[6.292141,8.343379],[0.803298,0.899271],[-5.176798,-9.069575],[9.410847,-4.810521],[6.021452,7.876382],[1.777299,-6.253238],[-7.435376,3.973994],[5.912476,7.289688],[3.478713,5.897831],[-0.733362,-1.780121],[7.374777,5.589602],[-0.503716,-9.201122],[-3.347047,1.258338],[5.944061,1.865343],[3.254933,4.700343],[-6.996789,4.993833],[3.209346,-9.054365],[-1.013310,7.110060],[6.362676,-0.798372]], dtype = "float64")#candidate|11370|(352, 2)|const|float64
call_11365 = relay.TupleGetItem(func_4652_call(relay.reshape(const_11366.astype('int64'), []), relay.reshape(var_11367.astype('int64'), [364,]), relay.reshape(const_11368.astype('uint16'), [880,]), relay.reshape(const_11369.astype('float32'), [90, 2]), relay.reshape(const_11370.astype('float64'), [704,]), ), 0)
call_11371 = relay.TupleGetItem(func_4658_call(relay.reshape(const_11366.astype('int64'), []), relay.reshape(var_11367.astype('int64'), [364,]), relay.reshape(const_11368.astype('uint16'), [880,]), relay.reshape(const_11369.astype('float32'), [90, 2]), relay.reshape(const_11370.astype('float64'), [704,]), ), 0)
output = relay.Tuple([call_11348,call_11354,call_11365,const_11366,var_11367,const_11368,const_11369,const_11370,])
output2 = relay.Tuple([call_11349,call_11355,call_11371,const_11366,var_11367,const_11368,const_11369,const_11370,])
func_11374 = relay.Function([var_11367,], output)
mod['func_11374'] = func_11374
mod = relay.transform.InferType()(mod)
mutated_mod['func_11374'] = func_11374
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11375 = relay.var("var_11375", dtype = "int64", shape = (1, 364))#candidate|11375|(1, 364)|var|int64
func_11374_call = mutated_mod.get_global_var('func_11374')
call_11376 = func_11374_call(var_11375)
output = call_11376
func_11377 = relay.Function([var_11375], output)
mutated_mod['func_11377'] = func_11377
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6678_call = mod.get_global_var('func_6678')
func_6680_call = mutated_mod.get_global_var('func_6680')
call_11392 = relay.TupleGetItem(func_6678_call(), 0)
call_11393 = relay.TupleGetItem(func_6680_call(), 0)
output = call_11392
output2 = call_11393
func_11397 = relay.Function([], output)
mod['func_11397'] = func_11397
mod = relay.transform.InferType()(mod)
output = func_11397()
func_11398 = relay.Function([], output)
mutated_mod['func_11398'] = func_11398
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6187_call = mod.get_global_var('func_6187')
func_6188_call = mutated_mod.get_global_var('func_6188')
call_11445 = relay.TupleGetItem(func_6187_call(), 0)
call_11446 = relay.TupleGetItem(func_6188_call(), 0)
output = relay.Tuple([call_11445,])
output2 = relay.Tuple([call_11446,])
func_11450 = relay.Function([], output)
mod['func_11450'] = func_11450
mod = relay.transform.InferType()(mod)
output = func_11450()
func_11451 = relay.Function([], output)
mutated_mod['func_11451'] = func_11451
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10120_call = mod.get_global_var('func_10120')
func_10121_call = mutated_mod.get_global_var('func_10121')
call_11556 = relay.TupleGetItem(func_10120_call(), 0)
call_11557 = relay.TupleGetItem(func_10121_call(), 0)
output = call_11556
output2 = call_11557
func_11558 = relay.Function([], output)
mod['func_11558'] = func_11558
mod = relay.transform.InferType()(mod)
mutated_mod['func_11558'] = func_11558
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11558_call = mutated_mod.get_global_var('func_11558')
call_11559 = func_11558_call()
output = call_11559
func_11560 = relay.Function([], output)
mutated_mod['func_11560'] = func_11560
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6536_call = mod.get_global_var('func_6536')
func_6538_call = mutated_mod.get_global_var('func_6538')
call_11601 = relay.TupleGetItem(func_6536_call(), 0)
call_11602 = relay.TupleGetItem(func_6538_call(), 0)
output = relay.Tuple([call_11601,])
output2 = relay.Tuple([call_11602,])
func_11606 = relay.Function([], output)
mod['func_11606'] = func_11606
mod = relay.transform.InferType()(mod)
mutated_mod['func_11606'] = func_11606
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11606_call = mutated_mod.get_global_var('func_11606')
call_11607 = func_11606_call()
output = call_11607
func_11608 = relay.Function([], output)
mutated_mod['func_11608'] = func_11608
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9576_call = mod.get_global_var('func_9576')
func_9577_call = mutated_mod.get_global_var('func_9577')
call_11629 = relay.TupleGetItem(func_9576_call(), 2)
call_11630 = relay.TupleGetItem(func_9577_call(), 2)
output = call_11629
output2 = call_11630
func_11640 = relay.Function([], output)
mod['func_11640'] = func_11640
mod = relay.transform.InferType()(mod)
output = func_11640()
func_11641 = relay.Function([], output)
mutated_mod['func_11641'] = func_11641
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8246_call = mod.get_global_var('func_8246')
func_8247_call = mutated_mod.get_global_var('func_8247')
call_11656 = func_8246_call()
call_11657 = func_8246_call()
output = relay.Tuple([call_11656,])
output2 = relay.Tuple([call_11657,])
func_11662 = relay.Function([], output)
mod['func_11662'] = func_11662
mod = relay.transform.InferType()(mod)
mutated_mod['func_11662'] = func_11662
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11662_call = mutated_mod.get_global_var('func_11662')
call_11663 = func_11662_call()
output = call_11663
func_11664 = relay.Function([], output)
mutated_mod['func_11664'] = func_11664
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6187_call = mod.get_global_var('func_6187')
func_6188_call = mutated_mod.get_global_var('func_6188')
call_11713 = relay.TupleGetItem(func_6187_call(), 0)
call_11714 = relay.TupleGetItem(func_6188_call(), 0)
output = relay.Tuple([call_11713,])
output2 = relay.Tuple([call_11714,])
func_11723 = relay.Function([], output)
mod['func_11723'] = func_11723
mod = relay.transform.InferType()(mod)
output = func_11723()
func_11724 = relay.Function([], output)
mutated_mod['func_11724'] = func_11724
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7844_call = mod.get_global_var('func_7844')
func_7846_call = mutated_mod.get_global_var('func_7846')
call_11807 = func_7844_call()
call_11808 = func_7844_call()
output = relay.Tuple([call_11807,])
output2 = relay.Tuple([call_11808,])
func_11835 = relay.Function([], output)
mod['func_11835'] = func_11835
mod = relay.transform.InferType()(mod)
mutated_mod['func_11835'] = func_11835
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11835_call = mutated_mod.get_global_var('func_11835')
call_11836 = func_11835_call()
output = call_11836
func_11837 = relay.Function([], output)
mutated_mod['func_11837'] = func_11837
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11877 = relay.var("var_11877", dtype = "int8", shape = (11, 3, 5))#candidate|11877|(11, 3, 5)|var|int8
const_11878 = relay.const([[[7,-9,-1,-6,-4],[-4,9,2,3,-2],[6,2,3,-6,5]],[[6,3,10,10,6],[2,-6,1,2,-10],[3,-2,4,4,-8]],[[7,10,7,-3,-7],[-10,-2,-1,4,8],[-2,2,5,-9,-5]],[[5,-1,1,8,-5],[-6,5,-5,8,2],[5,-7,7,-4,-1]],[[3,10,-5,-2,-6],[10,-5,-7,-1,-10],[-3,8,4,1,4]],[[-7,-10,-1,-10,5],[-1,8,-10,-8,2],[-8,5,-6,-3,-6]],[[-1,-2,-2,3,7],[7,-3,-7,10,5],[-1,8,9,4,-2]],[[-9,-7,-1,5,10],[2,-1,2,9,3],[-5,-9,2,-8,-1]],[[9,3,-8,-7,-6],[6,-6,-6,-5,2],[1,2,-4,-9,1]],[[3,8,7,10,-1],[-1,-6,-4,-5,7],[6,-9,-9,5,7]],[[8,7,6,3,6],[-4,-1,-3,-3,3],[-8,-10,-1,1,-7]]], dtype = "int8")#candidate|11878|(11, 3, 5)|const|int8
bop_11879 = relay.greater_equal(var_11877.astype('bool'), relay.reshape(const_11878.astype('bool'), relay.shape_of(var_11877))) # shape=(11, 3, 5)
output = relay.Tuple([bop_11879,])
output2 = relay.Tuple([bop_11879,])
func_11882 = relay.Function([var_11877,], output)
mod['func_11882'] = func_11882
mod = relay.transform.InferType()(mod)
mutated_mod['func_11882'] = func_11882
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11883 = relay.var("var_11883", dtype = "int8", shape = (11, 3, 5))#candidate|11883|(11, 3, 5)|var|int8
func_11882_call = mutated_mod.get_global_var('func_11882')
call_11884 = func_11882_call(var_11883)
output = call_11884
func_11885 = relay.Function([var_11883], output)
mutated_mod['func_11885'] = func_11885
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6812_call = mod.get_global_var('func_6812')
func_6814_call = mutated_mod.get_global_var('func_6814')
call_11932 = func_6812_call()
call_11933 = func_6812_call()
output = relay.Tuple([call_11932,])
output2 = relay.Tuple([call_11933,])
func_11945 = relay.Function([], output)
mod['func_11945'] = func_11945
mod = relay.transform.InferType()(mod)
output = func_11945()
func_11946 = relay.Function([], output)
mutated_mod['func_11946'] = func_11946
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11450_call = mod.get_global_var('func_11450')
func_11451_call = mutated_mod.get_global_var('func_11451')
call_11949 = relay.TupleGetItem(func_11450_call(), 0)
call_11950 = relay.TupleGetItem(func_11451_call(), 0)
var_11953 = relay.var("var_11953", dtype = "float32", shape = (15, 9, 6))#candidate|11953|(15, 9, 6)|var|float32
bop_11954 = relay.less_equal(call_11949.astype('bool'), relay.reshape(var_11953.astype('bool'), relay.shape_of(call_11949))) # shape=(15, 9, 6)
bop_11957 = relay.less_equal(call_11950.astype('bool'), relay.reshape(var_11953.astype('bool'), relay.shape_of(call_11950))) # shape=(15, 9, 6)
output = bop_11954
output2 = bop_11957
func_11958 = relay.Function([var_11953,], output)
mod['func_11958'] = func_11958
mod = relay.transform.InferType()(mod)
var_11959 = relay.var("var_11959", dtype = "float32", shape = (15, 9, 6))#candidate|11959|(15, 9, 6)|var|float32
output = func_11958(var_11959)
func_11960 = relay.Function([var_11959], output)
mutated_mod['func_11960'] = func_11960
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11662_call = mod.get_global_var('func_11662')
func_11664_call = mutated_mod.get_global_var('func_11664')
call_11964 = relay.TupleGetItem(func_11662_call(), 0)
call_11965 = relay.TupleGetItem(func_11664_call(), 0)
output = relay.Tuple([call_11964,])
output2 = relay.Tuple([call_11965,])
func_11968 = relay.Function([], output)
mod['func_11968'] = func_11968
mod = relay.transform.InferType()(mod)
mutated_mod['func_11968'] = func_11968
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11968_call = mutated_mod.get_global_var('func_11968')
call_11969 = func_11968_call()
output = call_11969
func_11970 = relay.Function([], output)
mutated_mod['func_11970'] = func_11970
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12012 = relay.var("var_12012", dtype = "int8", shape = (8, 8, 14))#candidate|12012|(8, 8, 14)|var|int8
var_12013 = relay.var("var_12013", dtype = "int8", shape = (8, 8, 14))#candidate|12013|(8, 8, 14)|var|int8
bop_12014 = relay.bitwise_xor(var_12012.astype('int8'), relay.reshape(var_12013.astype('int8'), relay.shape_of(var_12012))) # shape=(8, 8, 14)
output = relay.Tuple([bop_12014,])
output2 = relay.Tuple([bop_12014,])
func_12024 = relay.Function([var_12012,var_12013,], output)
mod['func_12024'] = func_12024
mod = relay.transform.InferType()(mod)
mutated_mod['func_12024'] = func_12024
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12024_call = mutated_mod.get_global_var('func_12024')
var_12026 = relay.var("var_12026", dtype = "int8", shape = (8, 8, 14))#candidate|12026|(8, 8, 14)|var|int8
var_12027 = relay.var("var_12027", dtype = "int8", shape = (8, 8, 14))#candidate|12027|(8, 8, 14)|var|int8
call_12025 = func_12024_call(var_12026,var_12027,)
output = call_12025
func_12028 = relay.Function([var_12026,var_12027,], output)
mutated_mod['func_12028'] = func_12028
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9226_call = mod.get_global_var('func_9226')
func_9227_call = mutated_mod.get_global_var('func_9227')
call_12037 = func_9226_call()
call_12038 = func_9226_call()
output = call_12037
output2 = call_12038
func_12051 = relay.Function([], output)
mod['func_12051'] = func_12051
mod = relay.transform.InferType()(mod)
mutated_mod['func_12051'] = func_12051
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12051_call = mutated_mod.get_global_var('func_12051')
call_12052 = func_12051_call()
output = call_12052
func_12053 = relay.Function([], output)
mutated_mod['func_12053'] = func_12053
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8670_call = mod.get_global_var('func_8670')
func_8671_call = mutated_mod.get_global_var('func_8671')
call_12062 = relay.TupleGetItem(func_8670_call(), 0)
call_12063 = relay.TupleGetItem(func_8671_call(), 0)
func_11397_call = mod.get_global_var('func_11397')
func_11398_call = mutated_mod.get_global_var('func_11398')
call_12064 = func_11397_call()
call_12065 = func_11397_call()
output = relay.Tuple([call_12062,call_12064,])
output2 = relay.Tuple([call_12063,call_12065,])
func_12067 = relay.Function([], output)
mod['func_12067'] = func_12067
mod = relay.transform.InferType()(mod)
mutated_mod['func_12067'] = func_12067
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12067_call = mutated_mod.get_global_var('func_12067')
call_12068 = func_12067_call()
output = call_12068
func_12069 = relay.Function([], output)
mutated_mod['func_12069'] = func_12069
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11968_call = mod.get_global_var('func_11968')
func_11970_call = mutated_mod.get_global_var('func_11970')
call_12086 = relay.TupleGetItem(func_11968_call(), 0)
call_12087 = relay.TupleGetItem(func_11970_call(), 0)
func_9226_call = mod.get_global_var('func_9226')
func_9227_call = mutated_mod.get_global_var('func_9227')
call_12093 = func_9226_call()
call_12094 = func_9226_call()
func_11640_call = mod.get_global_var('func_11640')
func_11641_call = mutated_mod.get_global_var('func_11641')
call_12095 = func_11640_call()
call_12096 = func_11640_call()
output = relay.Tuple([call_12086,call_12093,call_12095,])
output2 = relay.Tuple([call_12087,call_12094,call_12096,])
func_12106 = relay.Function([], output)
mod['func_12106'] = func_12106
mod = relay.transform.InferType()(mod)
output = func_12106()
func_12107 = relay.Function([], output)
mutated_mod['func_12107'] = func_12107
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7639_call = mod.get_global_var('func_7639')
func_7641_call = mutated_mod.get_global_var('func_7641')
call_12142 = relay.TupleGetItem(func_7639_call(), 3)
call_12143 = relay.TupleGetItem(func_7641_call(), 3)
var_12163 = relay.var("var_12163", dtype = "float64", shape = (6, 20))#candidate|12163|(6, 20)|var|float64
bop_12164 = relay.logical_and(call_12142.astype('bool'), relay.reshape(var_12163.astype('bool'), relay.shape_of(call_12142))) # shape=(6, 20)
bop_12167 = relay.logical_and(call_12143.astype('bool'), relay.reshape(var_12163.astype('bool'), relay.shape_of(call_12143))) # shape=(6, 20)
func_11450_call = mod.get_global_var('func_11450')
func_11451_call = mutated_mod.get_global_var('func_11451')
call_12168 = relay.TupleGetItem(func_11450_call(), 0)
call_12169 = relay.TupleGetItem(func_11451_call(), 0)
output = relay.Tuple([bop_12164,call_12168,])
output2 = relay.Tuple([bop_12167,call_12169,])
func_12170 = relay.Function([var_12163,], output)
mod['func_12170'] = func_12170
mod = relay.transform.InferType()(mod)
var_12171 = relay.var("var_12171", dtype = "float64", shape = (6, 20))#candidate|12171|(6, 20)|var|float64
output = func_12170(var_12171)
func_12172 = relay.Function([var_12171], output)
mutated_mod['func_12172'] = func_12172
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12067_call = mod.get_global_var('func_12067')
func_12069_call = mutated_mod.get_global_var('func_12069')
call_12196 = relay.TupleGetItem(func_12067_call(), 1)
call_12197 = relay.TupleGetItem(func_12069_call(), 1)
output = call_12196
output2 = call_12197
func_12213 = relay.Function([], output)
mod['func_12213'] = func_12213
mod = relay.transform.InferType()(mod)
mutated_mod['func_12213'] = func_12213
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12213_call = mutated_mod.get_global_var('func_12213')
call_12214 = func_12213_call()
output = call_12214
func_12215 = relay.Function([], output)
mutated_mod['func_12215'] = func_12215
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11558_call = mod.get_global_var('func_11558')
func_11560_call = mutated_mod.get_global_var('func_11560')
call_12243 = func_11558_call()
call_12244 = func_11558_call()
func_11558_call = mod.get_global_var('func_11558')
func_11560_call = mutated_mod.get_global_var('func_11560')
call_12255 = func_11558_call()
call_12256 = func_11558_call()
func_11397_call = mod.get_global_var('func_11397')
func_11398_call = mutated_mod.get_global_var('func_11398')
call_12265 = func_11397_call()
call_12266 = func_11397_call()
func_10321_call = mod.get_global_var('func_10321')
func_10323_call = mutated_mod.get_global_var('func_10323')
var_12272 = relay.var("var_12272", dtype = "float64", shape = (180,))#candidate|12272|(180,)|var|float64
call_12271 = relay.TupleGetItem(func_10321_call(relay.reshape(var_12272.astype('float64'), [180,])), 0)
call_12273 = relay.TupleGetItem(func_10323_call(relay.reshape(var_12272.astype('float64'), [180,])), 0)
output = relay.Tuple([call_12243,call_12255,call_12265,call_12271,var_12272,])
output2 = relay.Tuple([call_12244,call_12256,call_12266,call_12273,var_12272,])
func_12276 = relay.Function([var_12272,], output)
mod['func_12276'] = func_12276
mod = relay.transform.InferType()(mod)
var_12277 = relay.var("var_12277", dtype = "float64", shape = (180,))#candidate|12277|(180,)|var|float64
output = func_12276(var_12277)
func_12278 = relay.Function([var_12277], output)
mutated_mod['func_12278'] = func_12278
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6319_call = mod.get_global_var('func_6319')
func_6321_call = mutated_mod.get_global_var('func_6321')
call_12288 = relay.TupleGetItem(func_6319_call(), 2)
call_12289 = relay.TupleGetItem(func_6321_call(), 2)
output = relay.Tuple([call_12288,])
output2 = relay.Tuple([call_12289,])
func_12294 = relay.Function([], output)
mod['func_12294'] = func_12294
mod = relay.transform.InferType()(mod)
mutated_mod['func_12294'] = func_12294
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12294_call = mutated_mod.get_global_var('func_12294')
call_12295 = func_12294_call()
output = call_12295
func_12296 = relay.Function([], output)
mutated_mod['func_12296'] = func_12296
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12373 = relay.var("var_12373", dtype = "float64", shape = (3, 9, 13))#candidate|12373|(3, 9, 13)|var|float64
uop_12374 = relay.acosh(var_12373.astype('float64')) # shape=(3, 9, 13)
output = uop_12374
output2 = uop_12374
func_12390 = relay.Function([var_12373,], output)
mod['func_12390'] = func_12390
mod = relay.transform.InferType()(mod)
var_12391 = relay.var("var_12391", dtype = "float64", shape = (3, 9, 13))#candidate|12391|(3, 9, 13)|var|float64
output = func_12390(var_12391)
func_12392 = relay.Function([var_12391], output)
mutated_mod['func_12392'] = func_12392
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6812_call = mod.get_global_var('func_6812')
func_6814_call = mutated_mod.get_global_var('func_6814')
call_12476 = func_6812_call()
call_12477 = func_6812_call()
output = call_12476
output2 = call_12477
func_12478 = relay.Function([], output)
mod['func_12478'] = func_12478
mod = relay.transform.InferType()(mod)
output = func_12478()
func_12479 = relay.Function([], output)
mutated_mod['func_12479'] = func_12479
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10501_call = mod.get_global_var('func_10501')
func_10503_call = mutated_mod.get_global_var('func_10503')
call_12547 = relay.TupleGetItem(func_10501_call(), 0)
call_12548 = relay.TupleGetItem(func_10503_call(), 0)
func_12051_call = mod.get_global_var('func_12051')
func_12053_call = mutated_mod.get_global_var('func_12053')
call_12569 = func_12051_call()
call_12570 = func_12051_call()
func_8448_call = mod.get_global_var('func_8448')
func_8449_call = mutated_mod.get_global_var('func_8449')
call_12575 = relay.TupleGetItem(func_8448_call(), 0)
call_12576 = relay.TupleGetItem(func_8449_call(), 0)
func_7302_call = mod.get_global_var('func_7302')
func_7306_call = mutated_mod.get_global_var('func_7306')
var_12601 = relay.var("var_12601", dtype = "uint64", shape = (150,))#candidate|12601|(150,)|var|uint64
var_12602 = relay.var("var_12602", dtype = "bool", shape = (715,))#candidate|12602|(715,)|var|bool
call_12600 = relay.TupleGetItem(func_7302_call(relay.reshape(var_12601.astype('uint64'), [150,]), relay.reshape(call_12575.astype('int64'), [364,]), relay.reshape(var_12602.astype('bool'), [715,]), ), 4)
call_12603 = relay.TupleGetItem(func_7306_call(relay.reshape(var_12601.astype('uint64'), [150,]), relay.reshape(call_12575.astype('int64'), [364,]), relay.reshape(var_12602.astype('bool'), [715,]), ), 4)
output = relay.Tuple([call_12547,call_12569,call_12575,call_12600,var_12601,var_12602,])
output2 = relay.Tuple([call_12548,call_12570,call_12576,call_12603,var_12601,var_12602,])
func_12605 = relay.Function([var_12601,var_12602,], output)
mod['func_12605'] = func_12605
mod = relay.transform.InferType()(mod)
mutated_mod['func_12605'] = func_12605
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12605_call = mutated_mod.get_global_var('func_12605')
var_12607 = relay.var("var_12607", dtype = "uint64", shape = (150,))#candidate|12607|(150,)|var|uint64
var_12608 = relay.var("var_12608", dtype = "bool", shape = (715,))#candidate|12608|(715,)|var|bool
call_12606 = func_12605_call(var_12607,var_12608,)
output = call_12606
func_12609 = relay.Function([var_12607,var_12608,], output)
mutated_mod['func_12609'] = func_12609
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12685 = relay.var("var_12685", dtype = "int64", shape = ())#candidate|12685|()|var|int64
var_12686 = relay.var("var_12686", dtype = "int64", shape = (15, 6, 5))#candidate|12686|(15, 6, 5)|var|int64
bop_12687 = relay.equal(var_12685.astype('bool'), var_12686.astype('bool')) # shape=(15, 6, 5)
output = bop_12687
output2 = bop_12687
func_12690 = relay.Function([var_12685,var_12686,], output)
mod['func_12690'] = func_12690
mod = relay.transform.InferType()(mod)
var_12691 = relay.var("var_12691", dtype = "int64", shape = ())#candidate|12691|()|var|int64
var_12692 = relay.var("var_12692", dtype = "int64", shape = (15, 6, 5))#candidate|12692|(15, 6, 5)|var|int64
output = func_12690(var_12691,var_12692,)
func_12693 = relay.Function([var_12691,var_12692,], output)
mutated_mod['func_12693'] = func_12693
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6319_call = mod.get_global_var('func_6319')
func_6321_call = mutated_mod.get_global_var('func_6321')
call_12718 = relay.TupleGetItem(func_6319_call(), 1)
call_12719 = relay.TupleGetItem(func_6321_call(), 1)
output = relay.Tuple([call_12718,])
output2 = relay.Tuple([call_12719,])
func_12720 = relay.Function([], output)
mod['func_12720'] = func_12720
mod = relay.transform.InferType()(mod)
mutated_mod['func_12720'] = func_12720
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12720_call = mutated_mod.get_global_var('func_12720')
call_12721 = func_12720_call()
output = call_12721
func_12722 = relay.Function([], output)
mutated_mod['func_12722'] = func_12722
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9863_call = mod.get_global_var('func_9863')
func_9864_call = mutated_mod.get_global_var('func_9864')
call_12731 = func_9863_call()
call_12732 = func_9863_call()
output = call_12731
output2 = call_12732
func_12733 = relay.Function([], output)
mod['func_12733'] = func_12733
mod = relay.transform.InferType()(mod)
mutated_mod['func_12733'] = func_12733
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12733_call = mutated_mod.get_global_var('func_12733')
call_12734 = func_12733_call()
output = call_12734
func_12735 = relay.Function([], output)
mutated_mod['func_12735'] = func_12735
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10727_call = mod.get_global_var('func_10727')
func_10729_call = mutated_mod.get_global_var('func_10729')
call_12764 = func_10727_call()
call_12765 = func_10727_call()
output = call_12764
output2 = call_12765
func_12772 = relay.Function([], output)
mod['func_12772'] = func_12772
mod = relay.transform.InferType()(mod)
output = func_12772()
func_12773 = relay.Function([], output)
mutated_mod['func_12773'] = func_12773
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10727_call = mod.get_global_var('func_10727')
func_10729_call = mutated_mod.get_global_var('func_10729')
call_12819 = func_10727_call()
call_12820 = func_10727_call()
var_12831 = relay.var("var_12831", dtype = "float64", shape = (15, 9, 6))#candidate|12831|(15, 9, 6)|var|float64
bop_12832 = relay.not_equal(call_12819.astype('bool'), relay.reshape(var_12831.astype('bool'), relay.shape_of(call_12819))) # shape=(15, 9, 6)
bop_12835 = relay.not_equal(call_12820.astype('bool'), relay.reshape(var_12831.astype('bool'), relay.shape_of(call_12820))) # shape=(15, 9, 6)
func_7447_call = mod.get_global_var('func_7447')
func_7448_call = mutated_mod.get_global_var('func_7448')
call_12868 = relay.TupleGetItem(func_7447_call(), 0)
call_12869 = relay.TupleGetItem(func_7448_call(), 0)
func_3802_call = mod.get_global_var('func_3802')
func_3804_call = mutated_mod.get_global_var('func_3804')
const_12876 = relay.const([[8.708953,-9.057021,5.589112,7.813448,-5.580039,-8.529043,0.799724,-4.320657,-5.344538,8.942832,-5.476261,-2.109454],[1.476782,1.854988,5.578764,7.521067,2.378528,-6.783566,-1.964681,-2.630922,-7.548908,-1.094162,-1.324579,-7.211568],[3.731582,-1.618962,-4.103527,8.136411,-8.190020,4.844467,6.267139,-0.076137,0.319695,1.256432,4.682816,-7.242526],[5.710156,4.574831,7.315759,-5.355765,7.016382,7.821761,9.049938,5.640402,7.207560,-0.008695,8.195979,0.098206],[3.613152,-0.789197,-2.521219,-6.444718,7.712671,7.289767,5.550470,-4.978097,3.990497,-2.374806,-6.409094,-6.698211],[5.214676,-9.846421,-6.494649,1.383741,-5.004256,-5.757814,-9.603567,-4.058567,-9.548805,7.370414,3.850200,-5.469666],[9.516965,-3.047809,-4.217777,4.048526,8.644727,-5.406599,4.830522,7.505570,7.611458,-3.115500,-8.382777,1.907864],[7.771242,3.612162,-9.641995,5.364631,-9.383359,8.339332,-5.824755,-7.207706,-7.081639,6.803697,-4.712401,-6.677741],[-7.958259,-6.953030,6.447178,8.026970,-8.064181,-7.679743,-4.905980,-4.815561,3.102453,4.768240,-0.272585,2.364076],[-0.721455,-6.117255,2.571936,-7.423011,1.276063,-5.425284,8.713838,2.245404,-0.561782,-3.953449,9.710230,-0.728254],[2.881607,7.050855,2.258680,-5.221375,7.994688,9.846140,3.436843,4.342139,-0.161407,-8.142113,2.554895,3.391497],[1.489704,7.591643,-6.773971,4.311894,3.667055,4.588837,8.077924,2.404115,-6.733752,4.394640,-2.518196,-9.048883],[-5.017750,-9.722964,7.980514,-4.478971,-1.978861,3.384756,3.311911,-3.037769,8.613262,9.119975,1.207944,-4.395965],[2.117685,-0.937496,-2.222922,-0.008177,8.218256,-5.637712,-3.492744,6.381547,-0.813963,9.363347,4.053302,8.998516],[0.416214,9.546845,0.439788,-2.005977,1.724660,-8.198389,-9.457288,-8.666932,-8.235423,-4.741044,0.951850,7.316376],[-4.735866,7.693792,-1.349154,0.167575,-8.921544,-8.578401,-3.542497,-8.847903,4.594675,3.195848,-4.947449,8.659992],[-7.670046,1.702221,6.917128,-3.572368,-4.760163,9.490428,-8.876424,-9.996426,8.665386,-0.961839,-7.318210,8.299420],[8.246079,7.426463,0.195193,-1.689091,-5.317310,0.626603,-6.327673,0.187866,-0.461424,0.133062,7.836082,6.710744],[2.561681,-8.211352,-9.254773,8.249720,-5.040963,1.674253,-2.623512,-7.963887,-3.782879,-5.795726,1.543812,8.823701],[9.072041,-0.329078,-5.165112,2.469849,3.645312,4.976279,-7.439489,3.782468,9.420459,-3.695471,5.055381,-0.507813],[-3.438174,-1.054205,3.359675,0.667490,2.960480,6.151989,7.230439,6.011073,0.803466,2.836778,2.214043,-9.994160],[8.506861,-9.289430,1.018730,-7.751853,-2.196128,5.421001,-5.782120,-7.263033,-6.616394,-0.147041,-3.313324,-7.822685],[-7.694077,5.977868,9.260141,1.023490,-7.832759,2.008481,-3.325810,-1.665272,-2.614237,-2.593219,-5.121371,-2.864430],[5.131829,3.928281,-2.478801,9.285813,4.367274,9.592458,-2.803492,0.024425,-4.210094,4.536316,7.993444,0.200342],[6.471876,-2.485227,-0.657712,0.296248,6.766054,-3.462912,-6.800306,5.999869,-1.878332,-4.484515,9.997755,-9.072035],[-8.791972,-7.503302,3.941043,-8.594331,-2.854861,-1.339451,5.697282,-9.713078,-0.848147,7.040992,-8.258835,-6.707408],[9.881174,0.929626,5.144919,-4.481811,3.026458,9.515598,4.025861,-0.963403,-5.248765,-2.080506,-2.616198,1.309451],[0.547439,5.974368,4.367773,5.899407,0.730612,9.583143,-5.843763,-2.141624,-7.678523,-4.227342,3.926740,2.279306],[3.829936,-2.284317,-3.946658,8.855770,-8.243919,6.080670,-2.323256,-7.179055,-3.329787,-4.106565,0.358872,-2.070360],[-3.858983,3.471113,1.717423,-9.839246,8.921931,-5.132607,-8.420125,9.108363,1.129439,-4.832395,5.743322,6.642982],[-2.737806,-1.521565,-8.370312,9.692291,7.945538,1.322962,-7.308076,-0.493433,-3.061503,1.008989,-6.985194,3.403652],[-4.670902,5.289105,-9.118489,8.596893,5.736471,-9.227777,-9.316884,-4.815804,5.392307,4.247006,3.526226,0.264669],[-4.270894,-3.190611,0.056513,-2.959147,5.447846,-3.455646,-2.020648,-1.355499,9.876452,-3.876675,8.561693,-7.452164],[-3.138423,-0.674562,3.449714,4.766154,-1.179886,-3.156769,1.785779,8.152359,-0.359909,-4.295754,3.738543,-6.315127],[1.321762,9.751336,-4.506833,0.573981,3.355063,-6.416000,2.020402,-4.373241,-5.238240,-5.077813,-5.111332,-1.847716],[4.679536,8.883652,-5.315087,7.020665,-1.633069,-8.926069,-3.985773,3.567572,4.036069,-9.416906,5.392500,-4.523180],[0.662573,0.325206,5.736880,0.750137,-4.508963,7.835278,-1.594395,7.693803,9.960914,4.403071,8.589849,3.326398],[1.175821,-6.613326,5.390577,-8.516579,3.459730,-4.254365,6.216759,5.200920,-8.946681,-7.288356,4.408372,-9.704736],[1.358718,1.648595,-7.785906,3.035414,-4.685949,3.960223,1.255417,9.441330,4.452993,7.750168,3.443866,8.940127],[6.355110,-4.996477,1.372753,-3.494911,9.040023,8.186390,-9.743236,2.457127,-5.439797,-8.085716,-7.389753,-5.474080]], dtype = "float64")#candidate|12876|(40, 12)|const|float64
call_12875 = func_3802_call(relay.reshape(const_12876.astype('float64'), [12, 4, 10]))
call_12877 = func_3802_call(relay.reshape(const_12876.astype('float64'), [12, 4, 10]))
output = relay.Tuple([bop_12832,call_12868,call_12875,const_12876,])
output2 = relay.Tuple([bop_12835,call_12869,call_12877,const_12876,])
func_12878 = relay.Function([var_12831,], output)
mod['func_12878'] = func_12878
mod = relay.transform.InferType()(mod)
var_12879 = relay.var("var_12879", dtype = "float64", shape = (15, 9, 6))#candidate|12879|(15, 9, 6)|var|float64
output = func_12878(var_12879)
func_12880 = relay.Function([var_12879], output)
mutated_mod['func_12880'] = func_12880
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11108_call = mod.get_global_var('func_11108')
func_11110_call = mutated_mod.get_global_var('func_11110')
call_12882 = relay.TupleGetItem(func_11108_call(), 1)
call_12883 = relay.TupleGetItem(func_11110_call(), 1)
output = relay.Tuple([call_12882,])
output2 = relay.Tuple([call_12883,])
func_12886 = relay.Function([], output)
mod['func_12886'] = func_12886
mod = relay.transform.InferType()(mod)
mutated_mod['func_12886'] = func_12886
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12886_call = mutated_mod.get_global_var('func_12886')
call_12887 = func_12886_call()
output = call_12887
func_12888 = relay.Function([], output)
mutated_mod['func_12888'] = func_12888
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7929_call = mod.get_global_var('func_7929')
func_7930_call = mutated_mod.get_global_var('func_7930')
call_12898 = func_7929_call()
call_12899 = func_7929_call()
func_11304_call = mod.get_global_var('func_11304')
func_11305_call = mutated_mod.get_global_var('func_11305')
call_12903 = relay.TupleGetItem(func_11304_call(), 0)
call_12904 = relay.TupleGetItem(func_11305_call(), 0)
func_4683_call = mod.get_global_var('func_4683')
func_4685_call = mutated_mod.get_global_var('func_4685')
const_12916 = relay.const([7.527013,0.409904,-4.210464,-7.896956,-2.526635,5.085076,8.084467,-1.113924,-2.954584,9.269726,4.218504,6.814737,-3.838521,2.780941,0.517337,1.896128,3.465451,7.031789,2.442150,-8.932153,5.054030,-1.573896,2.173628,-1.635888,1.472473,7.961551,5.915978,1.173019,5.944912,4.173852,1.807764,8.215483,0.024646,2.044935,-9.936409,-5.109032,7.358884,-0.322283,-2.971380,9.400425,6.469213,-3.571702,7.601517,-7.861395,-8.516008,7.763885,-7.152893,-2.837854,9.140677,-2.637661,6.888877,2.568342,2.977864,-2.359768,4.767177,-3.238562,-2.061290,8.186822,-5.790983,-0.312159,2.077206,-6.236844,6.914758,6.144775,-5.585858,-9.685613,-8.216797,6.495736,-4.172940,3.693618,4.244840,-1.446004,-5.527992,3.696433,2.269963,7.869597,0.878380,-8.737975,-4.748620,1.476073,1.136020,5.367967,-9.982514,3.090722,-2.728080,-7.637579,-4.408567,1.251939,-7.040885,0.654031,2.904618,-1.962992,1.105377,4.971895,-7.595330,-8.035464,-0.480963,4.908016,-2.568503,4.530692,-8.647298,-7.224503,-4.488626,3.365840,-3.232397,-3.087964,-1.065456,-4.186540,3.296072,6.399822,6.441965,1.497509,2.533301,-7.000911,-6.399567,-5.574761,6.885080,0.704296,8.537323,-1.630094,-2.925125,4.775738,0.038658,-0.634622,7.787213,-6.231280,1.779613,-5.477463,-4.053896,8.303678,4.868019,8.191386,-5.826825,-7.667769,-6.028473,-9.938047,-3.839707,7.612072,9.301355,-0.621095,7.290836,7.299776,6.268996,-2.067482,-2.811667,-9.809737,6.408846,-2.113572,-2.681783,2.745244,1.022203,5.770448,8.178385,3.576060,-6.931282,9.927646,-2.775496,5.409258,0.419025,-8.653626,1.684571,1.284762,-9.604215,-4.555286,-0.613237,2.082753,7.070695,5.787342,1.277579,-9.729281,5.258503,-9.845445,-5.355848,6.981829,5.946423,-9.671748,-1.283621,7.187628,6.796623,9.236124,-2.929830,-6.810589,-1.192528,-2.438208,-7.422419,2.690957,5.062398,-2.320631,7.207614,9.198905,3.155506,3.937746,7.830661,-8.996336,1.776489,-1.900516,6.889882,8.355570,6.656397,3.315361,-6.239045,4.061268,-7.518712,-5.803375,7.411971,-8.679656,8.810235,-2.521786,7.976075,8.138279,-1.220475,-3.517721,-7.474440,9.675244,4.078613,-1.119258,-5.921241,0.083784,6.106396,-9.889581,3.993122,5.378933,0.057458,1.732924,-1.284263,0.609297,6.311427,-0.742990,2.420271,4.745132,0.453739,3.965053,6.195804,-8.756987,-8.601446,2.462663,-1.054361,-9.602788,-2.156322,-1.389807,-8.383583,6.120075,5.138628,-3.250367,-0.946436,6.484210,0.155739,7.377767,-9.192082,3.013518,-1.860037,-4.607560,4.261720,-6.475420,7.826494,-0.364265,-1.689684,2.496633,-3.026898,1.200563,5.313366,-3.868942,6.962111,9.254780,3.473251,-9.709333,1.041955,-9.308202,8.857917,-1.287712,8.103761,-2.287253,-4.351899,7.903382,9.236261,6.598868,-9.739088,9.804681,3.316318,1.761224,0.453007,6.256503,-7.236258,7.730298,-9.873651,-8.354574,9.449785,-0.467865,-9.858636,-2.720623,-2.828209,-9.200366,1.936680,-9.237188,-8.719479,3.813411,3.338279,-7.241299,4.746136,0.849863,6.305362,7.483782,-5.619598,3.489273,-6.986765,0.265820,0.122319,9.203121,3.413212,-9.476447,8.852368,-7.365621,-0.389327,-3.344474,-5.917202,3.024685,-0.999988,-1.459974,-3.340323,6.099190,2.413185,3.784467,5.457678,0.065695,-5.685026,-2.821851,-6.842727,-3.048293,-3.575002,-6.896282,-9.145861,-9.302194,-1.331739,-6.610881,-9.566701,8.811518,-4.130864,6.943830,6.861412,-8.317157,-4.889287,7.371188,1.495409,7.134364,0.785676,4.440536,5.420361,-4.933585,-3.827887,5.980967,-0.861701,6.946299,1.267698,-0.076937,3.457690,0.011540,-5.809398,-7.524572,-9.296635,2.032398,6.582685,-1.544820,-1.932944,8.177797,5.435198,-6.188287,6.871135,-2.268029,-8.373102,-5.487839,9.625272,5.273612,-8.110171,-8.777938,4.937885,-9.767131,-6.929392,3.644461,9.352337,3.752928,8.769659,7.460445,1.465091,-6.660434,-1.863151,-1.921116,-4.143924,1.850020,2.506218,1.765893,8.305829,-9.153851,-9.293739,6.582893,-5.731171,-7.716460,-1.947507,-6.652946,1.052089,8.899501,1.463454,-1.828448,1.298670,6.528215,7.578928,6.864590,-1.450933,-0.955946,2.404895,9.275686,-2.818303,-1.225144,3.982321,5.036466,0.606803,-4.974228,-2.535823,-8.377448,3.505703,-8.766494,-3.904790,9.553416,2.326478,-5.706873,9.313601,-5.364958,7.790520,-4.420600,-8.630891,-0.329511,-6.163188,-6.258856,1.235765,-4.000701,-6.737721,6.345211,-6.737713,-7.706262,-4.947481,4.002862,-7.323580,9.968683,-7.906349,-2.721204,5.384322,-7.258749,3.036849,-6.041529,0.138745,8.428673,-3.723075,-3.977549,-3.999058,-6.018724,6.533165,-2.352633,-1.537887,-2.895309,-2.136071,3.118826,9.706648,8.732674,-8.553345,0.273396,6.978879,-1.355977,3.701293,-5.788137,4.950681,-5.136447,-6.229819,-1.265260,-1.677531,2.814462,6.217536,3.645887,-5.355391,2.374685,-7.400728,-3.197581], dtype = "float64")#candidate|12916|(480,)|const|float64
call_12915 = relay.TupleGetItem(func_4683_call(relay.reshape(const_12916.astype('float64'), [480,])), 0)
call_12917 = relay.TupleGetItem(func_4685_call(relay.reshape(const_12916.astype('float64'), [480,])), 0)
output = relay.Tuple([call_12898,call_12903,call_12915,const_12916,])
output2 = relay.Tuple([call_12899,call_12904,call_12917,const_12916,])
func_12929 = relay.Function([], output)
mod['func_12929'] = func_12929
mod = relay.transform.InferType()(mod)
output = func_12929()
func_12930 = relay.Function([], output)
mutated_mod['func_12930'] = func_12930
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12992 = relay.var("var_12992", dtype = "float64", shape = ())#candidate|12992|()|var|float64
var_12993 = relay.var("var_12993", dtype = "float64", shape = (15, 6, 4))#candidate|12993|(15, 6, 4)|var|float64
bop_12994 = relay.greater(var_12992.astype('bool'), var_12993.astype('bool')) # shape=(15, 6, 4)
bop_12999 = relay.less_equal(var_12993.astype('bool'), relay.reshape(bop_12994.astype('bool'), relay.shape_of(var_12993))) # shape=(15, 6, 4)
output = relay.Tuple([bop_12999,])
output2 = relay.Tuple([bop_12999,])
func_13007 = relay.Function([var_12992,var_12993,], output)
mod['func_13007'] = func_13007
mod = relay.transform.InferType()(mod)
mutated_mod['func_13007'] = func_13007
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13007_call = mutated_mod.get_global_var('func_13007')
var_13009 = relay.var("var_13009", dtype = "float64", shape = ())#candidate|13009|()|var|float64
var_13010 = relay.var("var_13010", dtype = "float64", shape = (15, 6, 4))#candidate|13010|(15, 6, 4)|var|float64
call_13008 = func_13007_call(var_13009,var_13010,)
output = call_13008
func_13011 = relay.Function([var_13009,var_13010,], output)
mutated_mod['func_13011'] = func_13011
mutated_mod = relay.transform.InferType()(mutated_mod)
var_13075 = relay.var("var_13075", dtype = "float64", shape = (5, 13, 11))#candidate|13075|(5, 13, 11)|var|float64
var_13076 = relay.var("var_13076", dtype = "float64", shape = (5, 13, 11))#candidate|13076|(5, 13, 11)|var|float64
bop_13077 = relay.mod(var_13075.astype('float64'), relay.reshape(var_13076.astype('float64'), relay.shape_of(var_13075))) # shape=(5, 13, 11)
func_7231_call = mod.get_global_var('func_7231')
func_7234_call = mutated_mod.get_global_var('func_7234')
const_13102 = relay.const([0.509683,-8.517527,7.725825,-3.926066,9.116715,1.330787,-8.153352,-3.763636,6.049333,-2.422920,-5.893697,-5.341029,-5.120941,4.985874,4.517397,-2.425387,-4.710620,6.210316,9.934103,-3.505182,-6.978739,5.954608,5.042743,-4.425140,8.584176,0.455196,8.504312,-9.074128,-7.719783,-7.182147,-9.103090,-1.768707,5.565014,-6.650901,2.146053,9.198019,-2.267964,7.815539,-5.099307,4.941656,-9.893411,4.783264,-3.330063,8.690108,9.133901,-1.304557,-9.113793,-7.901245,0.188910,-9.127957,-7.958782,-5.278504,-3.051671,-7.033313,6.097954,-7.210815,-3.724311,-7.221949,7.181229,7.835415,7.808504,-8.520395,3.400904,0.725052,-4.195682,5.034514,8.706231,2.224247,8.794146,-6.342298,9.590036,-1.135342,-2.786333,-5.446074,-9.467564,-2.037027,-7.169084,6.576137,-7.442616,-1.140957,-4.489766,5.032706,2.715659,-1.678966,-6.211285,-8.789919,3.778202,5.534885,6.777015,-4.758713,6.389922,7.811551,4.155628,8.893857,8.031963,-7.091951,-9.685493,5.472172,8.029730,-1.273624,-0.962096,5.119845,-9.815393,9.280976,1.672220,5.895769,-9.427168,-6.384066,-1.824671,6.401053,6.725432,7.606981,3.212250,1.086108,-8.072448,-0.030755,-1.236598,8.231394,-0.577998,-0.852636,-8.821137,9.413122,-6.027488,-8.083606,4.098082,-1.444356,-0.865493,-8.227785,-7.067522,-2.426075,-3.983342,7.880099,-6.055905,6.148393,5.320231,-4.363171,6.704389,4.422528,6.341388,-4.905821,4.466583,2.417463,2.986645,-1.911313,-3.551543,-6.797393,3.561563,8.557238,-3.503698,3.038136,1.437775,9.754830,5.128082,-6.573850,9.232931,8.013662,-3.979371,-3.870014,3.961840,8.226796,6.419951,-0.411574,-7.898900,-2.331651,-8.199319,-1.667267,-9.805933,-4.189231,-7.154468,-4.886754,-7.447650,5.318647,1.015883,-1.660625,-0.916094,-9.390905,1.851289,-4.886563,-6.751501,4.727647,-8.640019,-0.876443,7.366174,-5.886079,-7.140248,2.854539,8.981380,4.619433,-4.312210,8.025796,7.139242,-4.182614,-0.466708,-4.507274,-7.585755,5.931279,-6.764583,7.364644,-4.443731,4.125013,-8.061615,8.748174,9.712304,-3.280070,-7.521314,-1.767850,7.472703,2.792587,-3.025203,2.039378,6.070322,9.465880,-0.418644,3.139417,0.874008,7.157982,-0.661317,6.972980,7.214722,3.952301,4.698523,-4.546544,6.828555,-3.621820,4.314596,-8.352980,-6.443326,-2.175569,-8.984001,9.858454,3.943832,0.932928,-4.381179,8.411878,6.520191,8.041582,9.631333,9.606286,0.676149,-6.899779,4.512681,7.250027,-9.764513,2.021068,-9.071960,-7.094376,1.345248,5.145229,-4.967738,-2.724276,4.014397,-0.503010,5.767431,6.625630,8.513570,1.489145,-1.412093,-7.113973,2.438615,8.151638,4.585519,8.185339,-2.460575,-5.484268,5.146520,-0.970649,-7.094364,9.730564,-1.032915,5.208449,-1.431054,7.744065,5.763228,-9.115602,6.744544,-0.528027,7.177611,9.839869,-7.923891,1.452470,-8.251456,4.279106,-8.163766,-2.031120,2.612075,2.249410,3.052047,4.550914,-2.615618,9.045495,0.839433,-0.238039,1.673449,-4.273049,3.188489,4.712658,2.571760,6.799277,-6.395245,4.238555,5.614992,0.364869,8.515189,4.039237,-7.988785,8.592715,4.241278,0.500921,6.103281,-8.830962,7.305365,3.980301,-9.298955,-8.182599,-4.726195,5.483986,-0.794438,-0.117873,9.620196,-2.379624,-6.813208,8.862015,1.182432,-5.007703,1.519345,-3.204230,0.969839,0.374545,-7.197737,-3.307665,5.876716,-8.540478,-6.301490,8.958836,-4.292927,-4.558535,1.639216,-8.637644,-7.375307,-1.668690,-0.889169,-5.458464,-7.892151,3.935831,5.812100,5.057092,8.126907,0.301769,1.912609,7.844720,-9.220068,-3.803988,-6.610264,-5.089374,-5.894300,-8.803862,4.462107,-6.324730,-4.357190,-7.327524,8.802951,2.070716,2.065397,-1.868373,7.440545,8.959655,7.726367,-3.471093,-6.658326,-4.064947,3.000069,2.975896,5.669495,-6.229438,-2.469359,-8.156909,-0.053880,-0.110983,-5.967218,-3.515490,5.722635,5.906373,-1.251105,-8.153897,-0.692222,8.652607,4.882652,3.554272,-1.676759,-1.944166,-6.951087,-9.983727,-8.970716,5.923125,9.110343,2.972034,3.218155,-3.174212,-4.436842,-0.826973,9.515978,-4.197428,4.462388,-8.854418,8.908809,-9.890009,8.288762,-2.256599,0.852929,-7.896427,-2.167664,3.120689,-4.295847,9.633442,-1.263337,0.645322,8.880109,-1.806268,9.490450,-9.295478,-6.615963,5.116637,4.309100,6.082282,2.766325,4.198404,4.931963,3.692482,-9.117744,-7.289293,-3.427613,7.456703,2.804769,-9.223899,-6.947806,5.061089,2.247018,-4.771572,8.084389,-4.623968,2.268319,-0.467991,-3.289341,-3.347352,-2.797455,-0.938524,-6.445737,-8.984425,0.993037,4.853939,7.400133,-1.523105,4.810118,2.289068,3.650991,1.843673,8.440946,2.658923,2.757128,8.438170,7.665397,-2.150614,9.133921,2.327008,-3.784809,-6.343666,-2.566409,-1.439437,9.716353,-8.829224,3.111729,8.476460,8.616656,1.925294,-0.273970,-0.232303,-3.745957,2.419651,1.534936,-5.217559,2.695109,2.753176,-8.017527,9.958985,7.380818,-0.818435,7.473074,4.901953,-5.680678,9.726451,4.589400,-2.567776,5.916696,7.275584,1.218088,-4.348577,-2.286413,-1.239234,8.395485,-4.480843,8.906772,-1.380337,-9.565697,8.666270,-5.037683,8.303422,-1.069914,7.284406,-9.166115,-8.341677,-4.874272,-2.595919,-4.955486,0.365793,5.966218,-4.676115,-7.021277,9.263553,-7.662628,-6.981351,-3.964737,5.827585,1.494496,-0.145435,3.427354,8.267365,3.550670,1.367755,-1.893923,7.976019,-7.735855,-0.919342,-7.469258,-8.994595,-8.290881,9.052347,-2.162263,3.260617,2.448902,8.182435,-8.651153,2.752993,5.775935,5.894611,0.301613,0.866109,-8.547132,8.763962,2.723757,-6.300476,-1.669493,-9.797043,-9.323748,-9.547683,3.376669,-2.968454,9.527834,7.205745,-7.918567,-5.615402,-1.104496,-9.965865,-0.623334,0.703081,6.906750,2.351355,-6.645759,-1.051712,-3.520790,-1.793639,1.500356,9.351382,-9.746945,3.482875,-5.704187,4.829511,0.027117,4.986201,8.971559,2.266274,-2.882064,-1.670067,5.056257,4.229656,2.705453,8.454866,1.805313,3.327599,-1.286806,-5.808233,6.011315,0.412886,2.705742,-3.193190,0.117161,2.607576,-0.724618,-0.901811,2.180561,5.821606,-1.878471,6.457801,-4.302296,7.823855,8.905249,6.582308,8.747712,4.696363,2.289808,7.909977,6.005794,8.949118,-2.896918,9.700504,1.290164,5.961996,-5.968778,3.178398,0.406548,5.880222,5.236866,0.786647,1.510848,0.364851,-4.413911,5.350725,-3.979934,-2.358009,2.293423,-2.416847,-2.897196,-6.223754,-1.457835,4.414119,-3.216754,-1.939777,1.963588,9.153379,-5.080913,-1.187568,0.876630,-7.659689,-0.200448,6.008651,0.776106,-4.417145,7.891779,-3.916244,5.027073,7.056796,-4.240862,2.072114,-4.754773,-1.536534,0.456416,4.401197,-7.816386,-6.592196,-5.286984,-3.799910,8.678602,-8.097577,1.477987,-6.030947,-3.791718,8.964382,5.935019,2.219989,9.351647,-7.035289,-4.439262,4.166926,-0.257474,5.823059,5.740235,-2.107643,-8.650619,1.035252,2.672135,-4.289516,-5.801862,-6.718030,-1.214045,9.827418,0.797076,5.469210,6.254609,-7.689386,-2.561034,6.823398,-8.936124,8.868128,-1.264359,-2.063502,-0.912370,8.936136,-1.427320,6.573330,8.099885,-6.910952,-6.115010,-3.595021,5.663372,7.586041,-5.440314,6.198207,-6.787398,-7.170156,-7.329143,-5.621153,2.805179,0.719314,2.520544,4.047939,8.110544,9.369763,8.920908,8.458025,9.253322,-6.142243,4.797415,-1.045263,-5.494554,-4.376817,9.392601,-7.565663,5.085839,6.312504,-0.675635,5.988847,-4.305013,4.243133,5.026537,-3.985329,-6.315454,-6.082655,9.633786,4.487732,7.703296,-1.696875,8.587826,-1.424230,-9.927768,2.767848,-4.441941,-4.067533,-6.741445,-3.392723,-4.431784,-7.962046,2.191267,4.674741,0.437988,2.914738,-1.153253,9.893276,-6.917565,-7.235415,9.449433,6.968048,0.885502,9.569825,4.931678,5.575405,-8.984202,-1.858913,-3.921675,-7.785735,9.415478,2.972101,7.282867,7.279409,-4.857446,-2.354168,3.190099,9.213803,9.190117,-4.073186,-2.775210,2.866710,6.715313,-1.793831,4.249822,4.723402,-6.777368,-2.902959,-8.122039,0.932867,-4.860001,-2.904466,4.279633,-7.142094,-3.423342,-9.973360,-6.428675,-5.819481,9.314371,3.554735,6.731113,5.391065,7.090293,-8.972403,3.640869,-0.292348,3.973293,-1.461652,-6.739656,-0.754065,7.476509,0.054691], dtype = "float32")#candidate|13102|(810,)|const|float32
var_13103 = relay.var("var_13103", dtype = "int64", shape = (195, 2))#candidate|13103|(195, 2)|var|int64
call_13101 = relay.TupleGetItem(func_7231_call(relay.reshape(const_13102.astype('float32'), [15, 9, 6]), relay.reshape(var_13103.astype('int64'), [5, 78]), ), 4)
call_13104 = relay.TupleGetItem(func_7234_call(relay.reshape(const_13102.astype('float32'), [15, 9, 6]), relay.reshape(var_13103.astype('int64'), [5, 78]), ), 4)
func_7929_call = mod.get_global_var('func_7929')
func_7930_call = mutated_mod.get_global_var('func_7930')
call_13112 = func_7929_call()
call_13113 = func_7929_call()
func_12478_call = mod.get_global_var('func_12478')
func_12479_call = mutated_mod.get_global_var('func_12479')
call_13114 = func_12478_call()
call_13115 = func_12478_call()
func_11397_call = mod.get_global_var('func_11397')
func_11398_call = mutated_mod.get_global_var('func_11398')
call_13132 = func_11397_call()
call_13133 = func_11397_call()
func_7915_call = mod.get_global_var('func_7915')
func_7918_call = mutated_mod.get_global_var('func_7918')
var_13142 = relay.var("var_13142", dtype = "float32", shape = (56,))#candidate|13142|(56,)|var|float32
var_13143 = relay.var("var_13143", dtype = "uint64", shape = (100,))#candidate|13143|(100,)|var|uint64
call_13141 = relay.TupleGetItem(func_7915_call(relay.reshape(var_13142.astype('float32'), [1, 56]), relay.reshape(var_13143.astype('uint64'), [100,]), ), 6)
call_13144 = relay.TupleGetItem(func_7918_call(relay.reshape(var_13142.astype('float32'), [1, 56]), relay.reshape(var_13143.astype('uint64'), [100,]), ), 6)
func_8298_call = mod.get_global_var('func_8298')
func_8300_call = mutated_mod.get_global_var('func_8300')
call_13149 = func_8298_call()
call_13150 = func_8298_call()
func_8113_call = mod.get_global_var('func_8113')
func_8115_call = mutated_mod.get_global_var('func_8115')
var_13153 = relay.var("var_13153", dtype = "float64", shape = (2016,))#candidate|13153|(2016,)|var|float64
call_13152 = relay.TupleGetItem(func_8113_call(relay.reshape(var_13153.astype('float64'), [2016,])), 3)
call_13154 = relay.TupleGetItem(func_8115_call(relay.reshape(var_13153.astype('float64'), [2016,])), 3)
func_4683_call = mod.get_global_var('func_4683')
func_4685_call = mutated_mod.get_global_var('func_4685')
var_13157 = relay.var("var_13157", dtype = "float64", shape = (480,))#candidate|13157|(480,)|var|float64
call_13156 = relay.TupleGetItem(func_4683_call(relay.reshape(var_13157.astype('float64'), [480,])), 1)
call_13158 = relay.TupleGetItem(func_4685_call(relay.reshape(var_13157.astype('float64'), [480,])), 1)
output = relay.Tuple([bop_13077,call_13101,const_13102,var_13103,call_13112,call_13114,call_13132,call_13141,var_13142,var_13143,call_13149,call_13152,var_13153,call_13156,var_13157,])
output2 = relay.Tuple([bop_13077,call_13104,const_13102,var_13103,call_13113,call_13115,call_13133,call_13144,var_13142,var_13143,call_13150,call_13154,var_13153,call_13158,var_13157,])
func_13159 = relay.Function([var_13075,var_13076,var_13103,var_13142,var_13143,var_13153,var_13157,], output)
mod['func_13159'] = func_13159
mod = relay.transform.InferType()(mod)
var_13160 = relay.var("var_13160", dtype = "float64", shape = (5, 13, 11))#candidate|13160|(5, 13, 11)|var|float64
var_13161 = relay.var("var_13161", dtype = "float64", shape = (5, 13, 11))#candidate|13161|(5, 13, 11)|var|float64
var_13162 = relay.var("var_13162", dtype = "int64", shape = (195, 2))#candidate|13162|(195, 2)|var|int64
var_13163 = relay.var("var_13163", dtype = "float32", shape = (56,))#candidate|13163|(56,)|var|float32
var_13164 = relay.var("var_13164", dtype = "uint64", shape = (100,))#candidate|13164|(100,)|var|uint64
var_13165 = relay.var("var_13165", dtype = "float64", shape = (2016,))#candidate|13165|(2016,)|var|float64
var_13166 = relay.var("var_13166", dtype = "float64", shape = (480,))#candidate|13166|(480,)|var|float64
output = func_13159(var_13160,var_13161,var_13162,var_13163,var_13164,var_13165,var_13166,)
func_13167 = relay.Function([var_13160,var_13161,var_13162,var_13163,var_13164,var_13165,var_13166,], output)
mutated_mod['func_13167'] = func_13167
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11558_call = mod.get_global_var('func_11558')
func_11560_call = mutated_mod.get_global_var('func_11560')
call_13174 = func_11558_call()
call_13175 = func_11558_call()
func_12772_call = mod.get_global_var('func_12772')
func_12773_call = mutated_mod.get_global_var('func_12773')
call_13179 = func_12772_call()
call_13180 = func_12772_call()
output = relay.Tuple([call_13174,call_13179,])
output2 = relay.Tuple([call_13175,call_13180,])
func_13189 = relay.Function([], output)
mod['func_13189'] = func_13189
mod = relay.transform.InferType()(mod)
output = func_13189()
func_13190 = relay.Function([], output)
mutated_mod['func_13190'] = func_13190
mutated_mod = relay.transform.InferType()(mutated_mod)
var_13240 = relay.var("var_13240", dtype = "int32", shape = (8, 16, 2))#candidate|13240|(8, 16, 2)|var|int32
const_13241 = relay.const([[[8,-2],[-8,1],[6,-2],[7,8],[7,4],[5,-4],[3,6],[-2,7],[4,9],[6,-9],[9,-7],[-5,4],[8,-7],[6,-10],[3,8],[6,5]],[[5,-1],[6,-5],[3,-1],[-7,-2],[7,-8],[5,3],[5,-3],[-7,2],[-4,4],[4,5],[1,8],[3,5],[-3,4],[-2,-6],[-8,-1],[-9,8]],[[-7,-5],[2,-10],[8,-5],[2,-2],[4,3],[-2,-4],[-7,-7],[7,2],[-8,6],[-9,-4],[-6,9],[-10,3],[8,3],[-4,-2],[3,9],[-3,-3]],[[10,-2],[6,5],[7,-10],[-8,3],[8,5],[5,2],[7,10],[-4,2],[4,2],[-9,4],[2,5],[8,7],[-5,7],[-2,-10],[4,-8],[2,-2]],[[-3,6],[3,10],[-5,-7],[-4,-8],[-7,-1],[-8,7],[-8,10],[-6,-8],[-1,2],[6,3],[-6,4],[-7,9],[1,-4],[-10,3],[-5,-9],[9,1]],[[-4,4],[-5,-1],[7,3],[10,-9],[-1,-2],[-1,8],[-7,-10],[-6,4],[4,-2],[-7,3],[10,10],[-7,3],[-2,-10],[7,1],[-9,-10],[-2,7]],[[-4,-8],[-3,9],[-5,3],[7,-4],[8,-2],[-4,-9],[-7,-7],[3,6],[4,10],[-3,9],[9,-3],[-8,5],[-3,-3],[3,-9],[10,9],[2,3]],[[-9,3],[6,-3],[-6,9],[-5,1],[5,-2],[-7,7],[9,-3],[3,-6],[2,6],[1,-1],[6,-2],[6,7],[-9,-10],[-2,-4],[-4,1],[-4,10]]], dtype = "int32")#candidate|13241|(8, 16, 2)|const|int32
bop_13242 = relay.bitwise_xor(var_13240.astype('int32'), relay.reshape(const_13241.astype('int32'), relay.shape_of(var_13240))) # shape=(8, 16, 2)
var_13247 = relay.var("var_13247", dtype = "int32", shape = (8, 16, 2))#candidate|13247|(8, 16, 2)|var|int32
bop_13248 = relay.not_equal(const_13241.astype('bool'), relay.reshape(var_13247.astype('bool'), relay.shape_of(const_13241))) # shape=(8, 16, 2)
uop_13257 = relay.log(var_13247.astype('float32')) # shape=(8, 16, 2)
output = relay.Tuple([bop_13242,bop_13248,uop_13257,])
output2 = relay.Tuple([bop_13242,bop_13248,uop_13257,])
func_13261 = relay.Function([var_13240,var_13247,], output)
mod['func_13261'] = func_13261
mod = relay.transform.InferType()(mod)
var_13262 = relay.var("var_13262", dtype = "int32", shape = (8, 16, 2))#candidate|13262|(8, 16, 2)|var|int32
var_13263 = relay.var("var_13263", dtype = "int32", shape = (8, 16, 2))#candidate|13263|(8, 16, 2)|var|int32
output = func_13261(var_13262,var_13263,)
func_13264 = relay.Function([var_13262,var_13263,], output)
mutated_mod['func_13264'] = func_13264
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10061_call = mod.get_global_var('func_10061')
func_10063_call = mutated_mod.get_global_var('func_10063')
call_13314 = func_10061_call()
call_13315 = func_10061_call()
output = call_13314
output2 = call_13315
func_13323 = relay.Function([], output)
mod['func_13323'] = func_13323
mod = relay.transform.InferType()(mod)
output = func_13323()
func_13324 = relay.Function([], output)
mutated_mod['func_13324'] = func_13324
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11450_call = mod.get_global_var('func_11450')
func_11451_call = mutated_mod.get_global_var('func_11451')
call_13341 = relay.TupleGetItem(func_11450_call(), 0)
call_13342 = relay.TupleGetItem(func_11451_call(), 0)
func_8402_call = mod.get_global_var('func_8402')
func_8405_call = mutated_mod.get_global_var('func_8405')
call_13346 = relay.TupleGetItem(func_8402_call(relay.reshape(call_13341.astype('float64'), [15, 9, 6])), 0)
call_13347 = relay.TupleGetItem(func_8405_call(relay.reshape(call_13341.astype('float64'), [15, 9, 6])), 0)
output = relay.Tuple([call_13341,call_13346,])
output2 = relay.Tuple([call_13342,call_13347,])
func_13349 = relay.Function([], output)
mod['func_13349'] = func_13349
mod = relay.transform.InferType()(mod)
mutated_mod['func_13349'] = func_13349
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13349_call = mutated_mod.get_global_var('func_13349')
call_13350 = func_13349_call()
output = call_13350
func_13351 = relay.Function([], output)
mutated_mod['func_13351'] = func_13351
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11397_call = mod.get_global_var('func_11397')
func_11398_call = mutated_mod.get_global_var('func_11398')
call_13367 = func_11397_call()
call_13368 = func_11397_call()
func_10727_call = mod.get_global_var('func_10727')
func_10729_call = mutated_mod.get_global_var('func_10729')
call_13391 = func_10727_call()
call_13392 = func_10727_call()
func_8563_call = mod.get_global_var('func_8563')
func_8565_call = mutated_mod.get_global_var('func_8565')
const_13413 = relay.const(9.948687, dtype = "float32")#candidate|13413|()|const|float32
call_13412 = relay.TupleGetItem(func_8563_call(relay.reshape(const_13413.astype('float32'), [])), 3)
call_13414 = relay.TupleGetItem(func_8565_call(relay.reshape(const_13413.astype('float32'), [])), 3)
output = relay.Tuple([call_13367,call_13391,call_13412,const_13413,])
output2 = relay.Tuple([call_13368,call_13392,call_13414,const_13413,])
func_13421 = relay.Function([], output)
mod['func_13421'] = func_13421
mod = relay.transform.InferType()(mod)
mutated_mod['func_13421'] = func_13421
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13421_call = mutated_mod.get_global_var('func_13421')
call_13422 = func_13421_call()
output = call_13422
func_13423 = relay.Function([], output)
mutated_mod['func_13423'] = func_13423
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9755_call = mod.get_global_var('func_9755')
func_9757_call = mutated_mod.get_global_var('func_9757')
call_13440 = relay.TupleGetItem(func_9755_call(), 0)
call_13441 = relay.TupleGetItem(func_9757_call(), 0)
output = relay.Tuple([call_13440,])
output2 = relay.Tuple([call_13441,])
func_13444 = relay.Function([], output)
mod['func_13444'] = func_13444
mod = relay.transform.InferType()(mod)
output = func_13444()
func_13445 = relay.Function([], output)
mutated_mod['func_13445'] = func_13445
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7447_call = mod.get_global_var('func_7447')
func_7448_call = mutated_mod.get_global_var('func_7448')
call_13451 = relay.TupleGetItem(func_7447_call(), 0)
call_13452 = relay.TupleGetItem(func_7448_call(), 0)
output = relay.Tuple([call_13451,])
output2 = relay.Tuple([call_13452,])
func_13456 = relay.Function([], output)
mod['func_13456'] = func_13456
mod = relay.transform.InferType()(mod)
mutated_mod['func_13456'] = func_13456
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13456_call = mutated_mod.get_global_var('func_13456')
call_13457 = func_13456_call()
output = call_13457
func_13458 = relay.Function([], output)
mutated_mod['func_13458'] = func_13458
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12213_call = mod.get_global_var('func_12213')
func_12215_call = mutated_mod.get_global_var('func_12215')
call_13508 = func_12213_call()
call_13509 = func_12213_call()
output = call_13508
output2 = call_13509
func_13518 = relay.Function([], output)
mod['func_13518'] = func_13518
mod = relay.transform.InferType()(mod)
output = func_13518()
func_13519 = relay.Function([], output)
mutated_mod['func_13519'] = func_13519
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5727_call = mod.get_global_var('func_5727')
func_5728_call = mutated_mod.get_global_var('func_5728')
call_13559 = relay.TupleGetItem(func_5727_call(), 0)
call_13560 = relay.TupleGetItem(func_5728_call(), 0)
output = call_13559
output2 = call_13560
func_13571 = relay.Function([], output)
mod['func_13571'] = func_13571
mod = relay.transform.InferType()(mod)
output = func_13571()
func_13572 = relay.Function([], output)
mutated_mod['func_13572'] = func_13572
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10022_call = mod.get_global_var('func_10022')
func_10024_call = mutated_mod.get_global_var('func_10024')
call_13657 = relay.TupleGetItem(func_10022_call(), 0)
call_13658 = relay.TupleGetItem(func_10024_call(), 0)
func_11304_call = mod.get_global_var('func_11304')
func_11305_call = mutated_mod.get_global_var('func_11305')
call_13666 = relay.TupleGetItem(func_11304_call(), 0)
call_13667 = relay.TupleGetItem(func_11305_call(), 0)
uop_13672 = relay.cos(call_13666.astype('float32')) # shape=(15, 9, 6)
uop_13674 = relay.cos(call_13667.astype('float32')) # shape=(15, 9, 6)
func_6812_call = mod.get_global_var('func_6812')
func_6814_call = mutated_mod.get_global_var('func_6814')
call_13678 = func_6812_call()
call_13679 = func_6812_call()
output = relay.Tuple([call_13657,uop_13672,call_13678,])
output2 = relay.Tuple([call_13658,uop_13674,call_13679,])
func_13680 = relay.Function([], output)
mod['func_13680'] = func_13680
mod = relay.transform.InferType()(mod)
output = func_13680()
func_13681 = relay.Function([], output)
mutated_mod['func_13681'] = func_13681
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9226_call = mod.get_global_var('func_9226')
func_9227_call = mutated_mod.get_global_var('func_9227')
call_13714 = func_9226_call()
call_13715 = func_9226_call()
output = call_13714
output2 = call_13715
func_13718 = relay.Function([], output)
mod['func_13718'] = func_13718
mod = relay.transform.InferType()(mod)
output = func_13718()
func_13719 = relay.Function([], output)
mutated_mod['func_13719'] = func_13719
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10245_call = mod.get_global_var('func_10245')
func_10247_call = mutated_mod.get_global_var('func_10247')
call_13765 = func_10245_call()
call_13766 = func_10245_call()
func_2722_call = mod.get_global_var('func_2722')
func_2726_call = mutated_mod.get_global_var('func_2726')
const_13774 = relay.const([-7.539488,-8.855599,6.876524,4.205633,6.689041,-5.288778,6.020116,-9.735800,3.168971,-0.498860,-5.933834,-9.692632,3.636818,-3.269226,-7.808712,6.570901,-6.172959,9.942745,-1.281923,-8.514028,-1.343913,-3.299913,-6.365885,0.659621,4.472684,-1.055740,-7.675940,-5.850173,-0.483662,-6.595126,-4.189104,4.664464,7.659458,-0.960360,7.722201,-3.511476,5.360686,-4.500330,4.073986,-1.192327,5.571842,-8.626037,6.011210,-3.034723,-1.337575,-7.800032,-4.498633,5.013815,0.823255,-2.219676,-0.892662,-8.870842,8.445364,-1.574785,2.397705,1.579077,6.176639,-3.564050,2.043643,-5.175760,8.261365,-2.687916,-7.210394,0.009488,-1.411111,-1.577469,-1.506767,-6.149629,0.644868,3.090879,1.745935,-6.800754,-8.983121,4.560331,7.258644,2.839675,4.235015,-2.769798,-9.171039,1.992752,0.018816,4.552756,-7.942186,6.341823,-1.414134,-2.406255,-4.275099,-8.278167,1.251888,-0.022951,4.244466,2.068087,2.001852,-2.066529,-6.939746,-0.519076,-8.914229,2.035872,-4.192908,-2.781539,6.342345,-9.778870,6.897846,7.799287,4.418823,2.656862,0.241226,3.638709,7.432591,-0.041208,8.205639,4.180087,0.237389,-5.642465,-0.331887,-7.659889,-3.038302,5.002193,-4.904345,-7.306561], dtype = "float64")#candidate|13774|(120,)|const|float64
var_13775 = relay.var("var_13775", dtype = "uint16", shape = ())#candidate|13775|()|var|uint16
call_13773 = relay.TupleGetItem(func_2722_call(relay.reshape(const_13774.astype('float64'), [5, 2, 12]), relay.reshape(var_13775.astype('uint16'), []), ), 2)
call_13776 = relay.TupleGetItem(func_2726_call(relay.reshape(const_13774.astype('float64'), [5, 2, 12]), relay.reshape(var_13775.astype('uint16'), []), ), 2)
func_1763_call = mod.get_global_var('func_1763')
func_1768_call = mutated_mod.get_global_var('func_1768')
const_13782 = relay.const([-6.130802,-4.761380,6.622912,-9.512601,0.491550,-1.383439,2.593022,9.630001,4.695821,-8.212865,-2.983944,5.300631,-5.563988,4.753158,-9.903199,0.086746,-2.172430,-7.833324,7.044712,-5.475534,7.716455,9.676046,-7.396457,9.479980,3.852819,8.651360,-8.712400,3.763104,5.373830,-7.967972,6.035034,-0.560035,0.101064,6.631036,3.027122,6.926155,8.426833,4.427518,8.268274,1.793641,7.068416,-3.851972,0.212711,-8.700550,4.359577,-8.716249,0.641808,-6.394044,2.417258,4.573863,-0.365498,-5.588773,9.608297,5.658562,-3.998068,5.489943,7.253175,5.601722,8.437886,3.780495,2.300983,-7.964457,1.738558,0.018784,-5.294509,2.682188,-8.317080,-7.389806,-5.989583,-2.159354,0.014231,-9.264983,-7.328154,0.094271,9.695200,-3.936240,2.689887,4.010718,4.821224,1.081250,4.605414,-0.263783,-0.373338,5.662248,-1.267944,-8.731877,6.498864,7.403368,-6.968864,-5.901862,3.624284,-4.630159,3.021989,9.235613,7.946519,-4.090451,-3.385841,-0.244245,-4.410357,6.248266,7.889146,-3.418617,-3.681699,-2.408700,-0.375513,-3.094913,4.265625,-7.299404,6.197306,-8.005716,2.934031,1.409739,1.407779,-3.990739,-5.431663,4.543596,2.693954,-7.351449,1.809470,2.088790,9.600301,6.063036,-7.460294,4.722945,-3.396999,-4.620368,2.557722,2.785087,6.877474,-6.237459,0.290433,-4.009863,3.723549,-0.184466,7.508541,-6.999240,1.107616,-4.277075,-9.428142,2.068041,1.622776,-8.517590,-9.179709,1.221649,1.956344,0.293391,0.176658,-2.318424,-7.878854,2.978090,-4.440504,5.460585,-8.310580,0.475079,5.656232,9.813380,5.164365,8.517926,3.572876,5.466137,-9.430929,4.585491,-4.532202,-3.726084,-2.658103,5.481379,-7.548503,-9.372409,-3.073604,7.782226,5.170017,-2.175575,-3.603475,-3.460460,-3.042035,-8.733234,-0.760849,7.393702,2.810513,4.240742], dtype = "float32")#candidate|13782|(180,)|const|float32
const_13783 = relay.const([-1,-7,4,-8,-1,4,7,-9,-3,8,9,-2,7,10,7,-7,8,-5,-9,9,5,-1,3,3,10,-1,-1,2,4,10,-7,8,-4,-8,-7,-2,10,5,3,9,-9,-6,7,10,2,-1,-10,2,5,4,-7,-4,-10,-2,7,8,-4,-8,-2,10,-10,-1,-3,2,-5,8,3,-10,-1,5,4,5,6,6,-4,2,-9,-4,-7,10,3,5,2,-8,-8,2,-6,9,-4,2,3,-4,6,-7,-4,-5,7,-4,5,-3,-5,-4,-3,5,-8,-5,-10,3,5,-6,-7,8,1,2,-4,-9,-9,3,6,9,-4,2,1,7,5,9,-6,-5,-8,3,3,4,6,4,-5,5,5,-3,-3,6,-4,10,-9,7,2,-3,3,-7,-5,1,3,-1,-3,9,-3,-6,8,-8,-10,8,8,-9,1,2,-10,-7,-8,3,1,1,-9,-4,2,-5,1,-8,-7,10,4,5,6,7,10,-7,-6,-6,7,1,4,-4,1,3,-9,-7,6,7,4,6,-7,-7,-3,-5,5,-10,2,-3,5,5,9,-7,6,7,-1,5,7,-9,5,1,-10,8,-4,-8,-6,-3,7,-10,-5,2,-1,3,9,8,-6,3,-1,-7,-3,-4,-10,-4,8,-7,-2,-10,-5,10,-5,-7,9,-6,-2,-7,-9,-4,9,-3,3,-3,-10,9,-8,-1,-9,-3,-10,-1,3,9,-1,9,10,-9,6,9,7,-3,-7,7,5,-6,-10,-9,-7,4,-3,7,7,-8,10,-8,5,1,8,-8,9,-7,-3,1,-7,9,8,-7,6,9,-5,10,-10,10,8,-8,3,7,4,-9,2,2,6,6,-7,5,-2,1,-7,-10,10,3,3,-1,-7,-9,8,1,-3,5,2,1,6,-7,-5,-7,5,8,1,7,10,9,9,2,-6,1,7,-1,-6,-4,-3,5,3,6,-5,-4,-8,4,10,9,-5,2,-4,2,3,-2,1,4,3,9,-4,-6,3,-10,-8,-9,-9,4,5,-5,4,-5,-7,10,-3,-1,-2,-9,-8,8,-8,-10,7,2,2,2,-5,2,8,-3,2,7,-2,9,-7,-8,3,4,4,3,1,3,-4,1,8,2,9,-2,-10,-1,-7,4,10,1,1,-9,1,2,8,7,7,-6,1,-7,10,-7,-8,-8,-8,10,4,6,3,1,1,-9,-7,7,2,8,10,10,6,-6,-4,-4,10,-4,-7,-6,10,9,8,-5,7,-4,-9,-9,-10,-1,-1,-5,-6,6,3,-4,-5,2,8,-6,3,6,-2,-8,9,-9,6,-3,-2,-4,9,9,2,9,-1,6,5,-7,-6,9,6,-8,-3,-3,-8,-9,-6,2,2,-7,-6,-6,-5,-8,-7,8,7,6,-7,-5,7,-3,-4,2,-8,-8,1,7,-4,7,-4,-9,-1,2,-5,4,-5,-6,3,5,-6,-8,-7,-1,2,6,-4,-10,9,2,3,7,-4,6,-10,9,-6,-3,5,-5,3,-4,4,4,8,-7,-4,8,7,3,7,-5,2,5,1,4,-9,3,-2,7,2,2,10,4,-4,-5,1,-3,6,-10,-5,-3,3,-10,-2,7,-4,-10,1,-10,-2,-7,4,8,7,1,2,-8,9,-10,-6,-4,7,5,-9,4,-1,-6,10,-9,4,1,-3,1,-7,-10,7,5,8,-4,4,-10,-3,-2,-2,10,-8,-4,-9,2,5,1,5,-7,-6,2,3,5,-10,-8,5,-10,10,5,-8,-7,8,-4,4,8,4,-9,3,10,-10,-8,8,-1,4,8,-10,7,-3,-1,-2,-6,-8,-3,1,-4,4,8,-2,10,5,-1,5,5,9,-4,4,7,-4,-2,-6,6,10,1,2,-9,-1,4,-8,-3,-2,8,-6,-7,-7,-5,-5,2,6,-7,-7,7,-9,-6,-9,-4,6,8,-6,2,2,-6,-10,-2,2,-7,10,-6,5,5,-1,-5,-10,-8,-8,10,10,8,-4,8,-4,4,-7,2,-4,-5,6,1,5,-2,2,2,8,3,2,6,6,-7,-2,-6,8,1,-5,1,4,2,7,-9,4,5,-3,2,-4,-2,-10,3,2,-1,8,7,-7,-7,1,-9,8,-2,8,-10,-3,-9,5,-8,-7,3,4,7,-7,8,-10,4,3,-1,-10,-3,5,5,-5,-6,5,-8,-9,10,1,5,-5,1,7,-8,3,1,5,-10,8,-3,-5,-9,7,-10,9,2,-6,-3,5,1,7,7,-5,-10,-3,5,-5,-4,-6,-3,-2,3,9,1,1,1,-2,-8,5,10,-3,6,1,-4,-6,4,-3,-6,-4,6,6,1,-6,-5,-1,9,-1,-3,6,-9,-4,10,1,2,10,-1,5,-6,-3,4,-9,-7,9,-3,9,7,5,3,-3,3,10,4,8,-8,5,4,-6,-4,-4,10,-7,7,6,9,-4,5,-8,3,10,-6,5,7,-2,-4,6,-10,-1,-8,-10,6,-1,9,-1,3,6,-4,-1,10,-4,2,10,-4,10,8,10,3,7,9,6,9,3,-1,-6,8,7,1,-1,-8,6,-2,-2,-8,-10,-6,10,6], dtype = "int64")#candidate|13783|(968,)|const|int64
const_13784 = relay.const([[-8,3,8,-9,3,-4,-2,7,-1,-6,3,-6,-3,6,2,4,-4,-9,-10,-9,-2,9,4,-4,2,-6,4,-4,2,4,3,5,-4,2,-1,-8,-6,10,6,6,4,10,1,-4,3,-10,7,-6,10,-6,2,5,-2,9,9,-3,-5,-10,9,3,3,10,9,-10,5,9,1,-5,-10,-10,-10,-1,-7,5,-6,-8,2,-8,4,-1,5,8,7,-8,10,6,-10,6,10,3,-10,5,-9,-4,-5,3,6,-8,7,-9,-4,6,4,1,-3,-1,3,6,1,4,6,9,-1,6,3,-4,2,2,3,-1,-8,-1,8,-5,-7,8,8,-7,2,-6,9,-3,1,-1,1,-3,4,-9,1,-5,5,-6,-9,-2,6,-8,-10,-10,-8,-7,2,-7,-6,-1,2,-9,-9,10,8,1,-9,-3,-1,2,-1,-10,1,-9,6,7,-8,-7,-3,-5,8,-7,6,-8,10,-8,-10,-3,-8,1,-4,3,9,7,6,3,9,-3,-9,-1,2,1,8,7,8,-9,8,-2,-2,9,2,-2,-1,5,-7,-2,-6,2,-8,-9,7,-7,-7,-2,-10,7,-2,-5,1,6,8,6,10,7,9,4,-1,-2,2,9,6,5,2,-2,2,2,5,-6,-8,-3,-7,4,10,10,2,5,3,6,4,10,-6,-7,-10,6,-4,-8,5,-2,-10,8,-10,-1,-5,-10,-5,-4,-3,-3,-2,3,-7,-8,3,-9,2,4,-8,-7,-2,-1,-7,1,6,5,3,3,-8,-4,2,-5,-9,-6,-6,2,-10,-8,-10,7,2,-1,9,-5,-6,10,-2,-2,-6,10,1,-9,-6,8,-5,-9,6,-2,-5,-3,-5,9,-10,8,1,-7,9,3,-4,-1,-7,-5,-2,1,-3,-10,-9,-6,2,-6,-2,-7,-8,8,3,-10,4,5,-10,5,3,2,4,3,-1,-1,10,6,8,2,5,-2]], dtype = "int64")#candidate|13784|(1, 364)|const|int64
call_13781 = relay.TupleGetItem(func_1763_call(relay.reshape(const_13782.astype('float32'), [5, 9, 4]), relay.reshape(const_13783.astype('int64'), [968,]), relay.reshape(const_13784.astype('int64'), [364,]), ), 3)
call_13785 = relay.TupleGetItem(func_1768_call(relay.reshape(const_13782.astype('float32'), [5, 9, 4]), relay.reshape(const_13783.astype('int64'), [968,]), relay.reshape(const_13784.astype('int64'), [364,]), ), 3)
output = relay.Tuple([call_13765,call_13773,const_13774,var_13775,call_13781,const_13782,const_13783,const_13784,])
output2 = relay.Tuple([call_13766,call_13776,const_13774,var_13775,call_13785,const_13782,const_13783,const_13784,])
func_13809 = relay.Function([var_13775,], output)
mod['func_13809'] = func_13809
mod = relay.transform.InferType()(mod)
mutated_mod['func_13809'] = func_13809
mutated_mod = relay.transform.InferType()(mutated_mod)
var_13810 = relay.var("var_13810", dtype = "uint16", shape = ())#candidate|13810|()|var|uint16
func_13809_call = mutated_mod.get_global_var('func_13809')
call_13811 = func_13809_call(var_13810)
output = call_13811
func_13812 = relay.Function([var_13810], output)
mutated_mod['func_13812'] = func_13812
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6678_call = mod.get_global_var('func_6678')
func_6680_call = mutated_mod.get_global_var('func_6680')
call_13818 = relay.TupleGetItem(func_6678_call(), 0)
call_13819 = relay.TupleGetItem(func_6680_call(), 0)
output = call_13818
output2 = call_13819
func_13827 = relay.Function([], output)
mod['func_13827'] = func_13827
mod = relay.transform.InferType()(mod)
mutated_mod['func_13827'] = func_13827
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13827_call = mutated_mod.get_global_var('func_13827')
call_13828 = func_13827_call()
output = call_13828
func_13829 = relay.Function([], output)
mutated_mod['func_13829'] = func_13829
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13349_call = mod.get_global_var('func_13349')
func_13351_call = mutated_mod.get_global_var('func_13351')
call_13844 = relay.TupleGetItem(func_13349_call(), 0)
call_13845 = relay.TupleGetItem(func_13351_call(), 0)
output = call_13844
output2 = call_13845
func_13869 = relay.Function([], output)
mod['func_13869'] = func_13869
mod = relay.transform.InferType()(mod)
mutated_mod['func_13869'] = func_13869
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13869_call = mutated_mod.get_global_var('func_13869')
call_13870 = func_13869_call()
output = call_13870
func_13871 = relay.Function([], output)
mutated_mod['func_13871'] = func_13871
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9576_call = mod.get_global_var('func_9576')
func_9577_call = mutated_mod.get_global_var('func_9577')
call_13897 = relay.TupleGetItem(func_9576_call(), 1)
call_13898 = relay.TupleGetItem(func_9577_call(), 1)
func_11723_call = mod.get_global_var('func_11723')
func_11724_call = mutated_mod.get_global_var('func_11724')
call_13912 = relay.TupleGetItem(func_11723_call(), 0)
call_13913 = relay.TupleGetItem(func_11724_call(), 0)
func_13456_call = mod.get_global_var('func_13456')
func_13458_call = mutated_mod.get_global_var('func_13458')
call_13929 = relay.TupleGetItem(func_13456_call(), 0)
call_13930 = relay.TupleGetItem(func_13458_call(), 0)
func_3269_call = mod.get_global_var('func_3269')
func_3276_call = mutated_mod.get_global_var('func_3276')
const_13956 = relay.const([[4,10,1,8],[6,-10,7,9],[8,5,2,-2],[4,9,-10,4],[4,-4,5,1],[-7,2,10,-10],[-9,-4,-1,-7],[10,5,-7,-4],[2,-8,-3,10],[-1,1,-2,-10],[10,-2,-2,-5],[3,4,10,2],[5,9,-10,7],[-1,-3,-1,-4],[8,-1,-4,-5],[-6,-6,-7,8],[-10,-2,-6,-10],[-7,-10,7,-9],[-1,-7,5,-2],[3,7,8,-3],[-10,7,-2,-5],[-1,7,-10,-2],[7,3,-3,2],[3,-7,-3,-9],[5,-3,2,-6],[-2,10,-1,10],[-4,-7,10,-7],[9,5,-4,6],[-10,-6,4,7],[7,7,-2,6],[-2,6,-2,-4],[-7,-2,-3,2],[-7,6,-2,-7],[-10,7,-1,-9],[5,4,8,-8],[-9,8,9,5],[-8,-9,-4,9],[3,8,-10,7],[-4,-5,-9,1],[-5,9,-1,-2],[-7,-9,-9,9],[-8,-6,-5,6],[-3,6,-5,-1],[-8,-6,7,7],[-1,7,7,-10],[2,-5,-8,-10],[3,-1,5,-1],[-4,-1,5,5],[4,-3,-7,-6],[-10,9,2,-7],[7,3,1,4],[-1,4,-1,-1],[2,-6,9,-1],[-2,7,2,-9],[1,3,-8,-7],[2,-4,-2,-9],[-10,-7,-6,-10],[-9,-4,-10,-1],[7,-2,1,-3],[-3,-5,1,-3],[-9,-10,7,5],[6,8,-4,-6],[3,5,9,8],[-6,-1,8,-8],[4,-4,-7,-8],[10,-8,7,7],[-1,-5,-2,-4],[-7,-3,-9,-4],[10,-6,8,-1],[-10,-5,2,8],[-4,-6,7,3],[5,8,9,-8],[9,6,-8,8],[-6,6,6,-1],[-10,-9,7,10],[9,9,-10,-9],[-1,-6,1,-8],[10,-3,1,-9],[1,5,-9,1],[2,8,-6,-1],[-1,5,-3,-9],[10,-9,7,9],[5,7,8,-6],[7,4,-2,-10],[4,-4,-2,-1],[-6,1,-10,3],[-4,-1,-8,7],[-2,1,-6,6],[-8,-8,-5,3],[9,5,4,-5],[8,-5,5,-6],[-2,1,-7,9],[-9,-8,-4,-8],[-4,-2,-2,-9],[7,9,-3,-8],[-1,5,8,-5],[-1,-3,-1,1],[5,6,-2,-8],[-8,-10,-3,7],[1,-1,-8,-8],[-9,-5,4,-8],[9,6,8,10],[-2,-6,-1,10],[5,-1,-10,-1],[1,-9,-1,-6],[10,4,6,3],[-4,-7,-4,-7],[10,1,8,-9],[9,6,7,-2],[1,-7,10,9],[1,-1,2,-3],[7,-2,-5,5],[-9,5,10,4],[-5,-2,-1,9],[6,-6,-9,1],[-10,-2,-4,-2],[-6,10,4,1],[3,4,-4,-5],[-6,-9,7,-10],[2,5,-9,-10],[3,2,2,-9],[-9,-10,-8,5],[5,7,-3,10],[-3,3,1,6],[3,-3,3,9],[-3,-5,3,4],[-2,-1,-2,-2],[7,6,9,4],[-9,-7,7,2],[-7,2,7,-10],[-9,-5,4,-5],[-7,1,-2,-7],[9,3,4,-9],[-4,-2,9,1],[-3,-10,-8,-9],[5,-10,-2,9],[-3,-1,-10,7],[-3,5,1,1],[-4,2,-7,4],[1,-10,1,8],[2,2,-2,-5],[7,7,8,3],[-1,6,8,-2],[4,-3,3,-2],[1,-6,10,-7],[1,-7,6,-3],[-5,-6,8,1],[2,-10,7,10],[5,-2,7,-4],[-5,-9,8,-7],[10,-7,3,-4],[-4,-2,6,1],[-7,-6,2,5],[10,-8,6,3],[-1,8,-10,9],[-7,-7,4,-4],[-10,-7,10,-10],[6,9,5,9],[2,-10,-10,-8],[-1,-9,4,-7],[-2,7,-6,2],[-4,1,-1,-5],[-8,7,5,4],[-4,-2,4,3],[4,10,6,10],[-1,9,-3,-6],[1,-8,3,-4],[-5,-5,6,7],[-7,-7,-8,-3],[10,-2,-8,2],[6,-8,2,-5],[-10,5,8,5],[-8,-10,-1,-7],[5,-2,2,4],[5,-6,-6,3],[-1,4,-2,-7],[-3,-9,10,-5],[-7,-9,2,4],[5,-6,1,9],[-10,3,3,-2],[-7,-1,7,1],[5,-3,-3,-6],[-7,1,2,1],[-4,5,6,-4],[-10,-1,4,-3],[2,-8,2,-5],[-6,10,8,-3],[-8,2,6,7],[2,3,2,5],[-1,-10,6,-4],[2,4,5,-4],[6,7,3,-7],[1,-3,7,6],[-2,3,-2,2],[-2,5,4,10],[-7,-1,10,9],[10,-4,-9,-7],[9,-9,-8,2],[-9,-7,8,4],[-2,-8,-3,-4],[9,9,2,-7],[5,-9,-8,1],[10,2,-5,5],[-1,10,10,-6],[5,6,-1,-6],[10,-9,8,8],[8,-6,-6,10],[6,1,7,-4],[5,10,5,-4],[3,5,-3,-9],[-5,-4,8,10],[6,-7,-1,3],[-2,-1,1,2],[-9,3,-2,-5],[-7,-7,4,8],[-9,1,7,5],[9,8,5,3],[-9,-6,-9,7],[9,-3,-3,3],[8,-3,9,6],[-6,-9,-4,-5],[-9,3,3,3],[6,-6,-9,-1],[4,1,2,3],[-2,10,-5,1],[9,1,4,5],[2,-8,-10,-5],[5,-8,-5,-8],[5,5,5,3],[9,-6,-8,2],[-2,-10,-1,7],[-2,4,7,-6],[-10,-2,8,10],[9,-10,-7,-8],[7,1,4,-4],[4,6,10,4],[5,-6,3,-10],[-4,-1,5,9],[-7,9,-2,-8],[3,-8,5,4],[9,-3,-9,-7],[3,3,-7,-1],[-5,-4,3,3],[-5,10,6,10],[-7,-10,-5,-9],[-4,8,5,6],[10,-8,1,1],[-6,-3,-9,8],[5,-2,4,1],[-4,-9,-8,2],[4,-3,3,2],[8,-2,8,3],[-5,-6,-8,6],[5,2,2,-3],[6,-3,1,8],[1,-6,-9,6],[4,2,-8,4],[8,7,10,8],[8,-6,-9,8],[-4,10,-3,-7],[10,-9,-2,10],[-10,1,10,7],[1,7,-8,1],[-9,-7,-9,1],[8,6,4,-1],[6,8,9,4],[-1,-1,5,-2],[3,9,8,1],[-10,5,6,10],[-5,-8,6,-6],[2,-7,-9,5],[10,4,-4,3],[4,9,5,-2],[10,7,-3,-2],[-10,5,-7,1],[-4,7,-4,5],[-10,9,-4,6],[-10,-1,-5,9],[-1,7,5,-7],[-7,-9,7,-8],[-8,2,8,7],[2,3,10,-3],[6,-1,9,10],[-4,-6,4,-10],[1,-6,2,8],[-1,1,3,-4],[-5,-10,3,-10],[-10,10,10,-6],[-1,-1,6,-7],[10,-8,-4,-4],[5,5,3,-7],[-2,6,-4,-5],[5,-8,-5,7],[4,2,6,-9],[1,3,9,-8],[-6,5,9,6],[5,-4,-10,-10],[6,2,-10,-7],[5,5,-9,-5],[9,4,1,3],[-4,10,10,6],[-4,8,-9,6],[-4,-8,-6,-5],[-4,-3,8,2],[-3,-6,2,8],[2,3,2,5],[-10,6,-7,-1],[3,5,1,5],[-10,6,-7,-10],[-10,-2,2,-8],[-2,10,-7,-8],[6,4,-1,-1],[10,-2,4,5],[7,-6,-7,-3],[1,6,-4,-10],[10,-10,-1,-3],[-2,9,9,10],[3,4,10,-9],[-9,-1,-1,-7],[-3,5,2,6],[-3,8,10,5],[-5,3,6,-8],[-7,2,-8,-1],[8,6,2,-3],[-8,6,-10,1],[-1,1,-6,-4],[8,1,7,-8],[9,-4,-7,-7],[-10,2,5,-5],[8,6,5,-7],[8,-8,1,9],[-9,1,9,-10],[1,9,5,-2],[10,-1,10,7],[-7,2,-10,-9],[3,4,10,-1],[5,-8,-5,-7],[10,1,5,7],[-2,1,-9,10],[2,4,-7,-2],[-6,-3,1,-8],[-8,-1,9,-5],[9,5,-8,-8],[9,2,-6,8],[-7,4,1,-10],[-3,1,1,2],[-2,7,-2,-10],[-8,6,-7,7],[5,1,-5,4],[4,-9,3,-4],[-6,5,-8,8],[-7,10,-9,9],[8,2,1,-1],[-3,-1,-2,1],[5,-8,3,9],[-2,-8,-3,9],[-7,7,8,4],[-10,8,-9,4],[7,9,1,1],[-6,-6,-6,-2],[-5,10,9,-5],[-8,-3,-1,4],[-10,-9,-10,4],[-1,-5,-9,-7],[-4,-8,-2,3],[5,8,-4,6],[-5,5,-5,-1],[3,-1,-3,-7],[-9,1,9,1],[10,1,-4,-8],[-10,-6,5,-1],[-3,1,3,4],[-2,-3,-1,-6],[-6,6,4,10],[-8,10,2,-10],[-6,-5,-8,2],[6,-4,2,9],[-6,9,-9,-5],[3,-8,9,-4],[-10,3,-7,-1],[-2,1,2,-1],[3,10,7,8],[-3,7,-6,-4],[-9,4,3,1],[8,-9,-2,-3],[-8,-8,10,-7],[2,-2,4,-5],[-4,8,-6,-5],[3,-9,2,-3],[-4,-7,8,-5],[5,-1,3,1],[6,-7,10,-9],[3,9,9,-8],[-4,-7,-7,5],[10,-1,1,-2],[-9,1,10,4],[9,1,-5,1],[1,2,-2,10],[-2,-7,-10,3],[-8,1,-6,1],[8,3,8,7],[-4,7,-7,-8],[-5,3,3,-7],[2,-9,4,-6],[-10,10,-5,-7],[-5,4,1,-2],[-8,4,-10,-2],[-2,1,-9,-10],[5,6,6,-10],[-10,-4,8,-9],[-10,-6,3,-3],[7,1,-10,-6],[3,-5,-7,-4],[9,10,-4,4],[2,-4,-7,2],[-10,1,-5,5],[1,7,-4,7],[-8,3,-5,-8],[6,-4,9,-7],[8,-9,7,9],[3,-7,8,2],[-2,2,1,-6],[1,10,-3,-3],[4,-2,-5,10],[10,6,-1,7],[-5,-1,-6,3],[-7,1,9,3],[-5,6,-9,-7],[4,-8,-4,-6],[-2,5,-6,-9],[-3,-6,-4,8],[3,1,-2,10],[4,9,-3,-6],[6,6,2,-6],[8,7,-1,3],[-3,-8,3,-1],[6,-2,6,7],[-9,-5,-8,6],[-5,8,-2,-9],[-5,9,5,-2],[9,3,2,-9],[-2,-4,7,6],[4,5,-7,10],[3,8,9,-10],[-4,6,-10,-10],[1,-3,-3,10],[5,5,4,-3],[-5,5,-1,-4],[8,2,9,2],[-6,-10,-8,-6],[8,4,-9,8],[-8,-9,8,3],[-7,5,8,6],[4,3,-8,4],[2,-7,7,-6],[10,3,3,5],[-2,4,10,2],[-7,6,5,1],[-2,-8,-6,3],[2,-8,-3,-2],[5,-4,7,-1],[-10,10,-10,3],[-3,-10,-7,-7],[-10,-3,7,-7],[5,-9,7,9],[-8,-5,1,-8],[-8,3,3,4],[4,6,5,4],[-7,4,-3,-5],[1,-9,7,9],[8,-3,-4,4],[-6,-1,-6,-3],[-10,-8,8,-3],[-3,-5,10,6],[-8,6,-5,9],[-1,-4,-7,-1],[-2,7,-4,2],[3,-6,1,-10],[2,-10,6,-8],[-2,-7,7,-6],[-9,-2,-5,8],[10,-2,7,-2],[10,6,3,-7],[6,6,2,-6],[-6,3,1,-3],[7,-5,-7,-5],[-9,5,7,-1],[-5,-8,-10,7],[-3,9,-4,-6],[-8,-7,-8,-6],[-5,10,-4,-5],[-7,-6,-9,5],[5,-7,-8,2],[-4,3,-3,-8],[1,-10,-9,1],[-2,-5,2,-5],[3,8,5,-7],[8,2,10,-10],[9,5,-7,-6],[-5,-1,10,-6],[8,-4,3,-1],[-5,2,4,-8],[6,-3,-2,-3],[9,-8,8,1],[9,8,-9,2],[-3,-9,10,9],[1,-8,-8,-9],[-3,-7,-10,-6],[4,-10,-4,-4],[1,-1,1,5],[-2,2,-6,-9],[10,1,-4,1],[-2,10,-5,10],[-10,-5,2,10],[6,4,-6,10],[-10,-8,-7,-4],[-9,-2,1,-10],[-6,-1,-8,-10],[4,6,-8,-8],[7,-3,-4,-3],[1,9,1,4],[-8,-4,5,-3],[-10,3,-9,-8],[-6,1,10,-4],[3,-5,-7,-10],[4,-3,9,-2],[-9,9,-3,-4],[-10,10,1,10]], dtype = "int32")#candidate|13956|(528, 4)|const|int32
const_13957 = relay.const([8,4,1,3,-8,4,-1,4,-2,-9,-7,-1,6,1,8,1,-6,-4,-6,4,7,-4,2,-2,-5,1,7,-1,6,1,1,-7,-8,3,8,-7,-7,7,9,2,-10,7,4,10,-9,-3,-4,7,-3,-5,-10,-8,-3,4,4,-7,-10,-2,4,6,5,-6,-2,-9,5,-6,8,2,10,-5,-6,7,-9,-2,-10,-8,8,2,-7,6,8,-7,-7,8,-6,2,-5,8,7,-9,-8,4,1,7,10,7,5,-2,2,-10,3,8,10,-2,-6,7,-7,2,-8,3,-10,6,4,-8,8,-3,-9,-8,9,-7,10,8,5,-5,-7,-1,-9,-4,4,9,1,4,-5,10,-4,-8,3,4,-6,-10,-7,1,9,9,7,-7,10,-10,-4,8,7,2,1,-7,3,9,-2,6,-6,-7,2,3,3,-10,4,-3,-3,-3,1,1,-1,3,-1,-7,3,9,-5,-1,8,7,9,-2,-7,7,7,9,8,-3,1,5,-1,-3,-9,-9,6,-6,6,-9,7,10,-4,3,-2,-1,6,9,2,-8,-6,7,-2,9,5,2,4,5,10,-3,6,-5,2,10,6,5,4,4,-5,4,10,1,6,5,-5,8,2,2,7,-8,-1,-5,-4,-8,3,-10,-6,9,6,9,2,-3,-3,6,8,-5,6,-1,-10,-9,1,-7,10,-10,-10,8,-8,-4,-5,-1,6,-1,7,-1,2,-1,1,1,-4,6,2,5,4,-1,4,1,9,2,-3,-2,-5,8,-8,5,-10,7,-6,1,4,10,-3,7,10,-5,-4,-6,9,7,2,1,-5,-3,-1,-3,-6,2,-4,9,-10,-7,-3,-5,8,10,-4,-4,-9,1,3,4,9,-9,9,-6,-2,5,-5,-8,10,5,-10,2,5,-9,9,8,-3,8,-2,-1,7,-10,6,-5,5,-10,-8,4,6,-10,1,3,-4,6,-5,-2,4,-5,1,5,-2,3,-9,-1,-2,-2,-10,7,-5,-10,9,-5,6,-3,1,-3,5,1,2,-1,-5,-7,7,9,-6,-6,-2,10,-10,3,3,2,-3,-5,5,1,-8,-4,-2,-1,-3,5,-8,1,10,-9,1,2,-4,-9,3,-10,-8,-8,-9,-1,5,-6,-1,-1,1,3,-1,6,-3,6,-6,-7,-3,7,5,4,3,5,7,4,-5,-1,-3,-4,3,10,-8,-6,-5,5,-2,-10,-9,1,-10,-5,4,-3,-5,1,7,-9,-2,8,-1,-5,-3,10,-1,-9,9,-6,-2,-10,-4,-8,6,-7,-4,4,-9,-8,8,-4,2,8,9,-4,2,9,5,-8,5,-9,-10,6,-4,2,6,-10,9,-8,1,9,-6,-9,6,-3,-3,-1,5,-4,4,10,-4,-6,8,1,-8,5,9,-4,-3,7,7,-3,-5,-3,5,-9,-6,1,-9,-5,3,10,6,-8,-10,7,2,10,-6,-6,-6,9,-10,-6,-3,5,-3,-9,-8,7,1,-5,-1,8,-8,8,9,-8,10,-7,6,-2,-6,7,-7,2,-8,8,-2,7,-5,7,-4,3,8,-8,4,5,-10,-6,7,-4,-4,4,-1,7,-8,9,7,8,6,4,-6,3,-1,3,-8,-1,-1,8,6,7,-10,-5,-2,6,1,-7,-9,4,-1,6,-6,-2,1,-1,7,-2,6,-6,2,-6,10,-9,6,-8,2,6,10,5,8,-2,-3,4,2,10,9,-9,3,-9,1,8,1,1,2,7,-3,-6,3,-10,7,-1,7,-9,-7,-9,-8,-4,-1,-2,-5,2,8,-6,8,-8,-5,-5,-8,-3,3,-5,-1,9,6,-4,10,8,-3,-3,-10,8,-9,-10,-7,3,-8,-10,9,-10,1,-7,7,-1,2,3,-4,-9,-6,-3,3,3,-6,8,-10,-4,2,2,-7,-2,-8,10,8,8,-8,6,-8,-3,-2,4,1,5,-7,3,-1,-2,-9,-4,4,2,-4,3,9,-10,9,5,2,-1,6,-5,-8,9,-1,-6,-4,9,9,3,10,-1,7,-8,5,-8,-3,9,9,-9,-10,7,1,3,10,8,-9,-8,4,-3,-5,-3,3,-10,-1,-7,1,-6,-2,4,4,1,-2,10,-4,6,-6,-10,10,-5,10,-1,-8,7,5,1,5,5,-2,3,9,-7,-10,-8,-10,3,-5,-1,1,-4,-9,-8,-8,10,-9,5,-4,-5,-3,5,5,1,2,4,2,-2,4,5,-4,-1,-10,2,-1,8,-9,-5,-1,-4,-2,6,8,-5,7,-4,5,-5,2,-10,-4,6,1,10,10,5,-4,-6,-9,5,-10,-1,4,1,3,6,-10,-5,-4,1,8,-7,-6,-7,5,3], dtype = "uint16")#candidate|13957|(880,)|const|uint16
var_13958 = relay.var("var_13958", dtype = "float32", shape = (180,))#candidate|13958|(180,)|var|float32
var_13959 = relay.var("var_13959", dtype = "int64", shape = (1, 364))#candidate|13959|(1, 364)|var|int64
const_13960 = relay.const([[7.984118,-3.038711,-2.333978,-6.149029,0.242401,-8.214381,3.919490,-5.017815,7.962199,8.795966,-3.885582,-5.227847,0.453314,-9.782426,7.587814,0.158042,-0.514498,9.885978,-8.896060,-3.182651,0.902687,-4.628171,-5.048401,6.595394,-4.644130,-4.580509,-9.352880,2.911905,-1.178815,0.565517,-9.054760,-9.801548,-6.937085,7.636930,1.985897,-8.053141,-0.542437,4.741371,5.654461,-1.535939,-1.450604,-3.431933,1.652606,-7.963816,-6.396760,-7.078638,-3.844433,5.090887,-8.998521,-0.288791,-7.395502,7.225797,5.582571,-3.836450,4.341656,4.437530,0.399152,-7.614057,3.884967,-4.756840,-3.180500,-9.796449,1.755626,-9.501728,-6.491901,6.890408,4.611554,8.019474,6.857634,-8.536171,-1.274131,-9.299150,9.826543,-8.722953,-5.592801,-2.381454,8.803381,9.243704,-6.846300,6.571131,-8.466123,-4.085818,0.385563,4.927292,5.678714,0.763857,1.115520,6.680034,-1.937075,3.194613,-2.013562,0.509179,-2.916079,-8.880929,-1.594207,4.069894,-1.191938,9.586777,3.353620,-2.815564,-9.781493,-0.289774,-4.347111,-2.164804,0.347535,3.848194,-7.925614,-2.795429,1.241196,0.798521,-5.065249,4.641199,-0.365061,-8.488948,6.892231,-7.819616,-7.469753,6.558891,-7.450358,6.275511,2.410072,1.335246,7.419004,-4.922695,-4.011243,7.928043,-8.688316,7.178130,9.244015,-3.991389,4.807022,-3.279564,2.409921,-9.199806,8.438788,6.492853,-7.241360,-5.549183,-8.423450,-2.775084,6.010850,4.806121,-5.612772,-2.400352,-2.016223,-2.681669,-1.506886,5.176221,-7.620910,3.797503,2.128918,-7.534232,-2.114538,-3.932207,8.361924,3.286309,-1.689245,-9.143612,-1.524602,-7.886446,9.113190,-9.706280,0.117052,0.228932,6.015924,3.417665,-6.416840,-1.885245,2.451578,0.516342,9.044056,0.831626,-9.937897,8.037627,-0.474319,4.669210,-3.906213,7.447347,-0.781103,-3.851022,-2.589650,-2.011196,3.702767,9.182497,7.055614,-7.251277,7.680440,-7.869801,5.414488,-8.767673,1.361625,-8.451627,1.638118,2.921086,-5.458796,8.562018,-2.864108,8.042202,-4.235880,-1.421474,-0.733427,7.405390,-0.552352,8.191347,3.572191,3.177398,8.166612,-0.594513,-3.084026,-2.637197,3.561545,2.432091,-9.524375,-0.386071,1.678349,-5.456609,6.119524,3.964848,-6.911334,5.501891,6.818595,-4.530860,-1.568252,4.157136,6.078394,-7.527064,-1.863527,-1.158941,-4.800903,5.969500,5.138846,7.997102,4.960097,-4.311782,0.795039,5.238000,-3.216005,-2.097526,4.652252,3.288993,2.101289,4.001540,1.776160,-8.993104,-5.313346,1.610083,-6.305603,-3.463707,-5.933191,9.158817,5.854561,-4.752020,-2.588051,-1.426901,-5.905658,-2.106568,5.750433,8.052043,9.924649,9.229196,-9.542025,8.606537,7.353692,-4.931422,-4.847446,-5.059771,5.358793,-0.361397,1.693372,1.049276,-0.044538,1.114040,4.188609,3.856013,6.033462,5.059947,9.218046,-3.374794,-0.906438,-4.281030,-5.304937,-8.307397,5.620910,1.518942,-5.987405,9.285425,9.439766,-6.729880,6.857450,2.552507,-6.407246,-6.046136,-3.748532,2.748266,-1.123880,9.149031,-2.547773,-1.390838,-5.469926,-8.688631,-2.706908,-7.758314,-9.645787,-9.710281,-6.675667,-2.987003,-9.322950,-4.528396,4.695955,-3.148593,-2.864465,-9.535242,1.734622,-3.123976,8.821756,-3.919237,-9.509491,0.698732,-8.620186,0.405029,6.622233,9.848518,-3.816214,-4.724170,9.356225,8.152075,3.573492,-2.297821,-7.379810,-4.706125,8.390204,0.303959,9.915549,1.950222,4.378611,-5.515331,-2.653727,-2.661533,-6.664511,3.095118,1.968240,0.224431,-3.047847,-1.121667,-1.599470,-2.202533,5.990545,-1.578749,-0.773672,-7.648819,-3.420062,4.548259],[5.664675,8.643307,-6.962592,0.984074,-7.394879,-9.325120,8.045784,7.001150,-1.437404,3.972496,-6.588251,-8.862656,2.482267,-2.976739,-4.494562,4.466711,3.910379,6.576619,4.470678,-7.862750,5.830102,-7.934223,0.634499,-6.613585,-8.772205,6.943428,0.394372,0.728902,1.586274,-1.685394,1.340763,5.174527,2.086769,0.605777,0.015025,-7.086389,-2.156189,1.782909,-1.838450,6.930140,-7.817775,0.545784,9.689935,-9.106563,-5.748381,-0.277447,-0.478580,5.678199,-2.241621,-6.831980,-0.436233,-3.891157,-0.819856,-6.279967,2.528628,8.140088,-3.747220,-3.101884,7.545367,-9.554260,7.530114,-2.620651,-8.714257,6.389085,-8.318750,8.985728,-6.726439,4.852895,2.560177,-0.913249,-4.434940,-6.906923,-5.776079,-4.066970,-5.694699,-5.368973,6.800968,3.708771,-8.671069,-8.575134,9.946744,4.785973,1.687053,-2.699198,-2.358381,2.104121,-0.931828,4.152877,-3.531822,-1.198049,2.267678,5.083269,0.870336,-3.148467,1.467210,-0.866397,-9.235605,7.604129,5.486668,9.460439,-4.349622,-0.515417,-9.718977,6.687064,4.342371,3.384182,-3.814023,9.092992,-1.682571,1.809314,-8.324346,-4.219560,0.127164,-9.815850,0.247659,-7.532313,-9.474368,-8.776432,8.185486,-8.852670,7.226585,2.277241,-6.305215,-0.260871,-4.934975,-6.931303,7.945480,-2.067243,-5.564350,9.381968,-3.375290,4.586621,-3.214877,3.848666,-9.640404,-4.698178,-5.853301,8.981022,-2.360217,4.825061,-8.937497,2.265280,-7.620865,-2.431325,-6.523042,-6.105655,-0.136135,-0.416397,2.283494,-8.943403,3.929387,4.201859,-3.789515,-2.726736,-8.527066,7.069699,6.915584,1.089655,-6.992356,4.185352,4.569651,1.835908,9.068162,4.668055,-1.882744,-0.569289,-8.234876,9.875520,7.565191,-6.005854,7.405306,-0.663002,-4.661755,-5.607817,8.164130,-2.757943,6.523654,-8.115563,7.341044,2.672305,2.944802,6.221187,7.202047,-0.182305,-3.037311,1.696331,3.722397,-4.100492,6.046345,-5.213828,-6.591714,6.948506,1.004288,5.440650,9.220994,-6.485115,-9.023548,9.933601,-7.271937,-4.688034,-7.525067,-3.171705,3.838088,5.877018,5.581446,-7.280474,-4.299546,9.418567,7.801290,-3.189205,2.027061,-4.327299,-5.756659,3.137434,1.718515,5.156252,5.166092,1.548678,3.381378,6.126963,9.017119,-1.554964,-6.428352,2.675186,-0.299045,-4.982548,-0.350329,-6.520591,-8.413385,6.496722,2.862215,8.971478,-0.636563,-3.680673,-1.385379,-9.535595,0.171724,8.239208,-8.914055,0.076074,9.853900,-2.339758,-3.235900,-8.909606,-1.765854,0.995321,4.519284,1.734282,2.139393,5.848489,6.140590,6.342121,-5.211069,-0.532003,0.444755,-9.739988,-3.814062,-9.954023,5.517444,3.754368,-2.543604,8.085880,-7.619171,2.365680,-8.497686,6.964962,-1.751403,-4.884677,8.221402,4.373716,1.092696,5.594453,-1.203600,-6.935993,7.799934,-7.741226,-0.013162,9.573359,-4.649547,2.405083,4.986027,-8.569427,9.613934,-7.420155,-8.429180,-0.941205,0.580198,8.476861,3.109611,7.226204,4.988518,4.441260,-7.482701,-0.780219,2.007500,5.619403,-3.135085,9.735802,4.582468,3.457041,4.571231,0.944005,0.583150,6.652768,-3.746667,3.038280,-4.121159,-0.335878,8.333045,9.503226,-2.762787,7.053625,-3.072713,-2.894021,3.109684,0.245985,7.639697,6.067468,4.507293,-0.949167,-1.223988,-9.873809,-6.645821,5.183750,3.431369,-4.653657,2.909948,0.154919,-8.895373,7.480676,3.921194,4.162582,3.395370,3.177900,8.974763,0.926832,-0.582618,-1.716335,-2.494837,-0.213580,-1.773193,7.153885,8.070867,7.013285,-2.139784,2.691276,-9.972674,2.938047,5.101429,-0.848306,-8.706871,-5.983399]], dtype = "float64")#candidate|13960|(2, 352)|const|float64
call_13955 = relay.TupleGetItem(func_3269_call(relay.reshape(const_13956.astype('int32'), [11, 16, 12]), relay.reshape(const_13957.astype('uint16'), [880,]), relay.reshape(var_13958.astype('float32'), [180,]), relay.reshape(var_13959.astype('int64'), [364,]), relay.reshape(const_13960.astype('float64'), [88, 8]), ), 0)
call_13961 = relay.TupleGetItem(func_3276_call(relay.reshape(const_13956.astype('int32'), [11, 16, 12]), relay.reshape(const_13957.astype('uint16'), [880,]), relay.reshape(var_13958.astype('float32'), [180,]), relay.reshape(var_13959.astype('int64'), [364,]), relay.reshape(const_13960.astype('float64'), [88, 8]), ), 0)
output = relay.Tuple([call_13897,call_13912,call_13929,call_13955,const_13956,const_13957,var_13958,var_13959,const_13960,])
output2 = relay.Tuple([call_13898,call_13913,call_13930,call_13961,const_13956,const_13957,var_13958,var_13959,const_13960,])
func_13971 = relay.Function([var_13958,var_13959,], output)
mod['func_13971'] = func_13971
mod = relay.transform.InferType()(mod)
var_13972 = relay.var("var_13972", dtype = "float32", shape = (180,))#candidate|13972|(180,)|var|float32
var_13973 = relay.var("var_13973", dtype = "int64", shape = (1, 364))#candidate|13973|(1, 364)|var|int64
output = func_13971(var_13972,var_13973,)
func_13974 = relay.Function([var_13972,var_13973,], output)
mutated_mod['func_13974'] = func_13974
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10474_call = mod.get_global_var('func_10474')
func_10475_call = mutated_mod.get_global_var('func_10475')
call_13985 = relay.TupleGetItem(func_10474_call(), 1)
call_13986 = relay.TupleGetItem(func_10475_call(), 1)
func_12929_call = mod.get_global_var('func_12929')
func_12930_call = mutated_mod.get_global_var('func_12930')
call_13994 = relay.TupleGetItem(func_12929_call(), 0)
call_13995 = relay.TupleGetItem(func_12930_call(), 0)
func_8246_call = mod.get_global_var('func_8246')
func_8247_call = mutated_mod.get_global_var('func_8247')
call_14003 = func_8246_call()
call_14004 = func_8246_call()
func_7447_call = mod.get_global_var('func_7447')
func_7448_call = mutated_mod.get_global_var('func_7448')
call_14009 = relay.TupleGetItem(func_7447_call(), 0)
call_14010 = relay.TupleGetItem(func_7448_call(), 0)
output = relay.Tuple([call_13985,call_13994,call_14003,call_14009,])
output2 = relay.Tuple([call_13986,call_13995,call_14004,call_14010,])
func_14036 = relay.Function([], output)
mod['func_14036'] = func_14036
mod = relay.transform.InferType()(mod)
mutated_mod['func_14036'] = func_14036
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14036_call = mutated_mod.get_global_var('func_14036')
call_14037 = func_14036_call()
output = call_14037
func_14038 = relay.Function([], output)
mutated_mod['func_14038'] = func_14038
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11219_call = mod.get_global_var('func_11219')
func_11221_call = mutated_mod.get_global_var('func_11221')
call_14057 = relay.TupleGetItem(func_11219_call(), 0)
call_14058 = relay.TupleGetItem(func_11221_call(), 0)
func_4693_call = mod.get_global_var('func_4693')
func_4696_call = mutated_mod.get_global_var('func_4696')
var_14071 = relay.var("var_14071", dtype = "float32", shape = (260,))#candidate|14071|(260,)|var|float32
call_14070 = relay.TupleGetItem(func_4693_call(relay.reshape(var_14071.astype('float32'), [5, 13, 4])), 0)
call_14072 = relay.TupleGetItem(func_4696_call(relay.reshape(var_14071.astype('float32'), [5, 13, 4])), 0)
func_10661_call = mod.get_global_var('func_10661')
func_10665_call = mutated_mod.get_global_var('func_10665')
const_14085 = relay.const([2,-9,-9,-10,1,-5,4,-6,6,-3,-3,3,9,1,9,-1,-8,-1,-1,-7,1,-7,2,9,3,8,-8,-10,-9,10,1,-10,4,-5,2,-7,-5,-9,-10,-6,8,-10,7,3,1,3,-7,-2,-4,-5,-10,-1,-9,-4,7,-1,-6,-3,-1,10,-2,-3,-5,9,3,-10,-6,-9,-1,3,5,-7,5,5,-6,5,7,6,-4,-3,-9,-1,4,-10,-3,5,7,10,-9,7,9,5,1,-7,-4,-3,3,-8,3,4,-10,-7,-8,-8,-1,4,8,-5,-1,-5,3,8,3,-5,-5,-4,7,-4,8,3,9,-1,-9,6,-9,6,9,1,1,10,-6,-1,-6,7,-6,-5,-10,-2,3,8,8,-5,8,-1,-2,5,3,-1,10,5,8,1,-10,-6,8,6,-10,3,7,-6,-4,8,-6,8,-7,-2,-7,-3,-5,-10,5,-8,-7,2,6,-6,1,-10,3,5,-1,6,-9,4,10,-4,10,-7,-7,-2,8,-5,-3,8,-1,7,9,1,-2,9,-7,-4,-6,-3,-1,8,-4,-10,8,-5,10,-2,-3,4,-7,7,7,2,-4,8], dtype = "int16")#candidate|14085|(220,)|const|int16
call_14084 = func_10661_call(relay.reshape(const_14085.astype('int16'), [5, 4, 11]), relay.reshape(const_14085.astype('int16'), [5, 4, 11]), )
call_14086 = func_10661_call(relay.reshape(const_14085.astype('int16'), [5, 4, 11]), relay.reshape(const_14085.astype('int16'), [5, 4, 11]), )
output = relay.Tuple([call_14057,call_14070,var_14071,call_14084,const_14085,])
output2 = relay.Tuple([call_14058,call_14072,var_14071,call_14086,const_14085,])
func_14090 = relay.Function([var_14071,], output)
mod['func_14090'] = func_14090
mod = relay.transform.InferType()(mod)
mutated_mod['func_14090'] = func_14090
mutated_mod = relay.transform.InferType()(mutated_mod)
var_14091 = relay.var("var_14091", dtype = "float32", shape = (260,))#candidate|14091|(260,)|var|float32
func_14090_call = mutated_mod.get_global_var('func_14090')
call_14092 = func_14090_call(var_14091)
output = call_14092
func_14093 = relay.Function([var_14091], output)
mutated_mod['func_14093'] = func_14093
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10138_call = mod.get_global_var('func_10138')
func_10140_call = mutated_mod.get_global_var('func_10140')
call_14195 = relay.TupleGetItem(func_10138_call(), 0)
call_14196 = relay.TupleGetItem(func_10140_call(), 0)
func_11304_call = mod.get_global_var('func_11304')
func_11305_call = mutated_mod.get_global_var('func_11305')
call_14197 = relay.TupleGetItem(func_11304_call(), 0)
call_14198 = relay.TupleGetItem(func_11305_call(), 0)
output = relay.Tuple([call_14195,call_14197,])
output2 = relay.Tuple([call_14196,call_14198,])
func_14202 = relay.Function([], output)
mod['func_14202'] = func_14202
mod = relay.transform.InferType()(mod)
output = func_14202()
func_14203 = relay.Function([], output)
mutated_mod['func_14203'] = func_14203
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9649_call = mod.get_global_var('func_9649')
func_9651_call = mutated_mod.get_global_var('func_9651')
call_14204 = relay.TupleGetItem(func_9649_call(), 1)
call_14205 = relay.TupleGetItem(func_9651_call(), 1)
func_12929_call = mod.get_global_var('func_12929')
func_12930_call = mutated_mod.get_global_var('func_12930')
call_14215 = relay.TupleGetItem(func_12929_call(), 1)
call_14216 = relay.TupleGetItem(func_12930_call(), 1)
func_6080_call = mod.get_global_var('func_6080')
func_6085_call = mutated_mod.get_global_var('func_6085')
var_14218 = relay.var("var_14218", dtype = "uint16", shape = (880,))#candidate|14218|(880,)|var|uint16
var_14219 = relay.var("var_14219", dtype = "float64", shape = (704,))#candidate|14219|(704,)|var|float64
var_14220 = relay.var("var_14220", dtype = "int64", shape = (968,))#candidate|14220|(968,)|var|int64
call_14217 = relay.TupleGetItem(func_6080_call(relay.reshape(var_14218.astype('uint16'), [40, 22]), relay.reshape(var_14219.astype('float64'), [704,]), relay.reshape(var_14220.astype('int64'), [968,]), ), 3)
call_14221 = relay.TupleGetItem(func_6085_call(relay.reshape(var_14218.astype('uint16'), [40, 22]), relay.reshape(var_14219.astype('float64'), [704,]), relay.reshape(var_14220.astype('int64'), [968,]), ), 3)
output = relay.Tuple([call_14204,call_14215,call_14217,var_14218,var_14219,var_14220,])
output2 = relay.Tuple([call_14205,call_14216,call_14221,var_14218,var_14219,var_14220,])
func_14233 = relay.Function([var_14218,var_14219,var_14220,], output)
mod['func_14233'] = func_14233
mod = relay.transform.InferType()(mod)
var_14234 = relay.var("var_14234", dtype = "uint16", shape = (880,))#candidate|14234|(880,)|var|uint16
var_14235 = relay.var("var_14235", dtype = "float64", shape = (704,))#candidate|14235|(704,)|var|float64
var_14236 = relay.var("var_14236", dtype = "int64", shape = (968,))#candidate|14236|(968,)|var|int64
output = func_14233(var_14234,var_14235,var_14236,)
func_14237 = relay.Function([var_14234,var_14235,var_14236,], output)
mutated_mod['func_14237'] = func_14237
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11662_call = mod.get_global_var('func_11662')
func_11664_call = mutated_mod.get_global_var('func_11664')
call_14241 = relay.TupleGetItem(func_11662_call(), 0)
call_14242 = relay.TupleGetItem(func_11664_call(), 0)
func_12213_call = mod.get_global_var('func_12213')
func_12215_call = mutated_mod.get_global_var('func_12215')
call_14244 = func_12213_call()
call_14245 = func_12213_call()
func_7929_call = mod.get_global_var('func_7929')
func_7930_call = mutated_mod.get_global_var('func_7930')
call_14256 = func_7929_call()
call_14257 = func_7929_call()
func_3802_call = mod.get_global_var('func_3802')
func_3804_call = mutated_mod.get_global_var('func_3804')
const_14263 = relay.const([0.737644,-7.711302,6.350924,4.175405,-9.594626,-0.768889,4.414295,9.203329,7.102309,3.595480,-1.620011,1.891783,-8.327454,-1.336405,1.103573,-4.561404,5.861654,8.399638,7.471633,-8.458664,-0.552449,7.391460,6.384397,-8.519009,5.538939,9.176364,7.205949,-5.209279,-9.361933,4.034925,-1.451951,-3.678411,9.034094,-0.644956,-2.510730,-3.747488,9.325398,-5.765562,-3.409635,4.517870,6.678800,4.016642,7.980804,-2.449687,-6.660420,5.043266,2.711595,4.851429,-8.489122,3.174606,-0.690547,4.934518,-4.518736,3.690548,7.804803,-1.359449,0.842631,4.829047,3.544250,-3.475601,-9.976305,-1.833119,5.668391,-4.400315,-3.942700,6.391919,7.416383,-5.597185,-4.516281,0.516215,5.354404,-2.742217,9.411479,1.801563,2.222883,0.548332,-2.070564,4.641275,9.250806,5.859200,-9.320896,-8.863937,9.253750,1.494816,-4.462128,9.308213,-6.631534,-8.528624,-1.525056,-2.215046,1.708207,8.685444,2.978641,-1.470906,-8.850708,-1.497979,-9.329173,-4.327498,-2.730467,9.862748,-9.223455,-5.189690,7.936653,2.427064,-2.917054,5.317531,7.934731,0.419896,-7.112075,2.995418,5.072098,6.656801,-3.965737,-5.357128,1.121929,-4.331657,-4.679281,-5.721961,5.062632,5.723903,1.277144,-7.413334,2.941010,7.291187,5.985851,-7.898377,5.481016,-6.804636,-7.098171,-1.335224,-0.310072,9.158579,4.719446,-0.706702,3.178207,-2.419369,9.819415,8.971358,0.408221,-8.794818,1.345298,3.347268,-6.701709,1.263834,-8.975341,-7.428702,-0.488404,-4.534893,8.764637,-2.088640,-1.654907,5.068540,0.736528,2.834069,0.487252,0.784882,-1.673668,4.846115,-3.076052,2.850972,-6.716144,-5.699552,-5.709188,-9.824155,2.222129,-7.369790,-8.931777,2.492487,8.963280,-1.719992,-3.382670,5.514904,-4.075528,8.334752,8.344871,-4.793414,-2.986044,-1.684597,7.687402,-4.184715,-7.180958,-8.022186,-3.167307,-2.208938,-5.127994,9.369244,6.998799,-6.483073,3.420434,-2.342028,-3.160415,8.065047,6.479222,1.665834,-6.290978,-8.400689,7.179318,4.019627,-8.955824,2.616151,-8.579045,-7.694263,2.227569,-3.618049,-2.807776,-7.966118,5.417735,-5.326640,3.929443,3.245622,0.584783,-5.548901,-8.095702,9.811398,-0.314280,-1.722614,8.832670,-9.594369,2.245569,0.977693,9.737942,-8.344438,1.150462,-0.104089,0.144970,2.220608,8.450168,9.532311,1.106676,-5.485789,2.258785,9.637550,5.365323,6.680400,-2.052168,4.166678,-6.455584,-5.223438,-8.926045,4.510526,-6.574315,-3.389921,-3.734256,6.185722,-5.569797,0.746836,-1.618809,-6.462767,-7.962920,-6.802655,3.620303,5.936964,-1.816751,9.371645,-8.462721,-1.925265,2.138698,-6.279721,-2.489095,-1.917737,7.043886,-5.099981,-3.071577,-9.890522,-9.674732,5.787014,-2.232348,-8.526265,-6.518381,6.528676,-2.240713,2.535411,-4.277542,8.594635,3.687142,-8.187790,-1.396314,8.503576,5.084568,3.698084,-4.374008,9.972963,8.587478,0.307852,-6.064317,-8.473198,-9.561730,-4.357668,2.142013,6.330302,0.863059,-1.061742,-2.202115,-9.479831,1.272806,-1.250805,-3.326107,-2.135345,2.857059,3.978608,-9.030182,-0.911714,2.828250,9.231704,-2.210904,-2.989625,-6.870892,2.550807,-0.450985,3.585621,-0.885303,2.288626,5.393977,-0.939803,-7.802010,-7.384199,-6.820598,6.097279,-8.524898,-9.541298,-7.468376,-8.223963,0.464204,4.437003,-2.086244,8.526715,-0.008745,1.071483,-5.793830,-7.579593,-7.763876,6.296204,7.063394,-1.726214,-6.773914,5.225406,8.987784,4.869022,8.992070,-6.738253,4.320114,-4.997137,2.680979,-0.150075,-5.277650,-9.398527,3.213351,5.662000,-8.063679,-8.460507,-7.935602,2.147166,-7.600848,1.923480,-0.333772,2.597900,7.776919,3.797426,0.604781,3.130860,3.784189,-3.295166,4.985415,8.520429,-8.727593,-9.895343,5.055887,-3.543467,9.240320,-2.375247,-8.845273,0.098522,7.809639,-2.554388,-3.583318,-4.105147,8.403808,8.228805,-9.350556,-5.184340,-7.164439,-1.676694,9.002267,6.644978,-2.202196,-7.494452,6.482376,-0.378116,-1.561725,-1.104027,-4.733157,-3.246164,9.571550,5.165688,9.281323,-9.630937,-8.760513,3.790752,-6.570538,-7.895680,-7.104040,9.735587,1.636867,1.646050,-6.178751,-1.718617,-6.612095,-0.001264,-3.373137,-3.200453,1.888085,-9.127197,6.228955,3.095126,-9.337583,-6.204307,-3.593774,1.633926,7.363896,-3.903000,-9.789615,5.375634,7.685040,-9.796095,9.362241,6.329783,-2.627939,-2.205826,-2.696180,2.529063,-9.041916,9.624416,6.619673,-3.355138,7.705900,-5.916118,9.304627,2.256940,5.473384,2.061621,-5.331856,1.828256,-2.832369,-6.630742,-5.582645,7.342122,3.698411,5.915303,7.724146,6.800664,-2.816134,-7.988928,4.669168,8.160543,-8.122484,1.959668,4.817413,1.766888,6.248296,-7.250067,3.664892,-6.173838,8.300501,6.358646,1.487244,4.193737,-9.245305,0.772197,4.820017,-9.749648,5.156644,-1.101631,-8.702171,-3.398857,3.162898,1.537700,8.193779,5.063268,-4.064526,4.473412], dtype = "float64")#candidate|14263|(480,)|const|float64
call_14262 = func_3802_call(relay.reshape(const_14263.astype('float64'), [12, 4, 10]))
call_14264 = func_3802_call(relay.reshape(const_14263.astype('float64'), [12, 4, 10]))
func_8298_call = mod.get_global_var('func_8298')
func_8300_call = mutated_mod.get_global_var('func_8300')
call_14288 = func_8298_call()
call_14289 = func_8298_call()
output = relay.Tuple([call_14241,call_14244,call_14256,call_14262,const_14263,call_14288,])
output2 = relay.Tuple([call_14242,call_14245,call_14257,call_14264,const_14263,call_14289,])
func_14295 = relay.Function([], output)
mod['func_14295'] = func_14295
mod = relay.transform.InferType()(mod)
mutated_mod['func_14295'] = func_14295
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14295_call = mutated_mod.get_global_var('func_14295')
call_14296 = func_14295_call()
output = call_14296
func_14297 = relay.Function([], output)
mutated_mod['func_14297'] = func_14297
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13518_call = mod.get_global_var('func_13518')
func_13519_call = mutated_mod.get_global_var('func_13519')
call_14325 = func_13518_call()
call_14326 = func_13518_call()
output = relay.Tuple([call_14325,])
output2 = relay.Tuple([call_14326,])
func_14335 = relay.Function([], output)
mod['func_14335'] = func_14335
mod = relay.transform.InferType()(mod)
mutated_mod['func_14335'] = func_14335
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14335_call = mutated_mod.get_global_var('func_14335')
call_14336 = func_14335_call()
output = call_14336
func_14337 = relay.Function([], output)
mutated_mod['func_14337'] = func_14337
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7798_call = mod.get_global_var('func_7798')
func_7800_call = mutated_mod.get_global_var('func_7800')
call_14338 = func_7798_call()
call_14339 = func_7798_call()
output = call_14338
output2 = call_14339
func_14340 = relay.Function([], output)
mod['func_14340'] = func_14340
mod = relay.transform.InferType()(mod)
mutated_mod['func_14340'] = func_14340
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14340_call = mutated_mod.get_global_var('func_14340')
call_14341 = func_14340_call()
output = call_14341
func_14342 = relay.Function([], output)
mutated_mod['func_14342'] = func_14342
mutated_mod = relay.transform.InferType()(mutated_mod)
var_14424 = relay.var("var_14424", dtype = "uint32", shape = ())#candidate|14424|()|var|uint32
var_14425 = relay.var("var_14425", dtype = "uint32", shape = (14, 14, 6))#candidate|14425|(14, 14, 6)|var|uint32
bop_14426 = relay.multiply(var_14424.astype('uint32'), var_14425.astype('uint32')) # shape=(14, 14, 6)
func_1484_call = mod.get_global_var('func_1484')
func_1488_call = mutated_mod.get_global_var('func_1488')
const_14430 = relay.const([-7.966567,-1.088568,-7.522933,4.319013,-1.437009,3.422052,-2.987284,7.756348,7.191369,-2.916684,-8.026705,-6.152284,-5.206731,9.022685,0.162285,-2.757390,-4.031162,-7.911212,-9.413147,7.596330,6.063661,1.676251,-3.793416,0.785891,6.184926,-7.687050,7.394596,-0.716128,-7.712652,-3.130339,5.958260,7.784162,1.810868,-8.043523,-1.512595,1.126781,-3.019946,8.833245,3.300045,-4.751901,8.090566,-1.139941,-2.795546,-3.832403,-9.650783,-6.075314,4.210233,-2.275283,1.723252,-2.726046,-9.673557,-3.629473,-5.797096,-8.991340,-4.552296,-3.184505,3.740651,-6.415903,-1.938530,8.041924,2.982522,-2.578399,5.470581,-4.561172,2.530542,-7.868704,-4.403264,-1.027557,2.244921,-8.443579,9.861301,4.906454,3.970129,-7.551706,-5.451598,-1.671426,-8.366405,6.790821,9.446663,-0.744562,-2.942020,0.628447,4.677305,-9.338670,-9.915338,-3.765291,5.556507,-0.248252,-4.781258,-8.406927,-9.388245,-4.899778,9.521455,0.332894,1.102908,6.563219,-6.870978,-1.405336,-2.262686,-4.323677,0.445709,5.197392,-6.854414,9.390318,-8.605214,-5.218696,1.953892,8.373995,-2.737285,7.976097,1.916523,0.065775,0.127151,4.153464,-2.058253,-7.056717,6.656625,9.952268,-7.368494,-5.112055,-4.023036,1.051726,1.741672,7.352435,4.361949,-8.688716,1.412225,6.901754,7.187462,7.116527,-7.405474,-8.677886,7.043755,-8.300308,-7.968823,-6.059571,5.508219,-4.331724,2.199335,-0.830488,2.239847,4.224051,-1.948875,0.833940,7.353762,-1.219188,3.309950,8.643485,-4.639298,-1.800796,-7.331936,8.827250,-3.925866,3.021912,4.698463,5.025331,-9.821261,-5.371326,8.736399,-8.077523,-7.310525,-4.496524,5.475067,-9.110858,6.695711,5.496133,5.007871,7.566520,-5.601395,2.982118,-1.726534,-6.218361,1.809253,-1.793697,0.706914,-8.752517,3.590458,0.267472,-1.059600,-9.898349,-0.850226,-6.338904,-5.080579,5.971060,-7.866782,7.534423,5.805149,4.812146,-0.082376,8.588824,-0.261893,6.429079,0.729513,4.348287,-5.795615,7.730013,1.510941,-1.103400,-3.208488,-8.253626,3.656106,1.956970,-2.461631,4.398687,-9.274993,-1.514006,-5.992692,-1.377204,-6.582040,-0.077766,3.109812,3.801936,1.934998,9.638411,6.927609,-5.879755,3.299607,-4.778137,-4.723664,-7.803986,-5.416771,2.594049,-2.593579,-8.352055,4.362389,4.375134,9.728109,3.515902,-6.971330,-4.044591,0.776062,-1.045337,-8.909998,-5.512076,2.314601,-7.661190,0.944126,-8.208285,8.364183,-6.090944,9.479855,-2.808344,-1.815475,6.369008,-9.320886,-2.829963,-0.631856,-9.771375,2.031029,5.923023,3.520962,1.678974,-6.484958,-2.521444,-2.217609,-5.418540,-0.228517,-5.529055,1.013458,1.598286,4.950257,9.726847,8.236334,7.198451,-0.824174,5.050403,-4.526257,-5.928945,-5.077681,-0.973785,3.176724,7.412599,3.398326,-7.894837,6.549797,-3.288130,8.275072,6.270608,5.039250,-5.015425,7.713507,9.509772,-5.599159,-8.222572,-7.925283,0.509373,-8.647451,9.988364,5.462280,-0.897147,-8.542783,1.628810,-0.784928,-1.233067,4.900436,3.990316,-3.774284,-3.595530,-9.946618,1.239001,-3.630001,-4.837825,2.815416,-3.226233,2.555049,-4.390465,-9.352832,9.249609,-6.169775,-5.053280,-2.109065,-8.643601,1.948083,5.129340,-2.239593,-5.254226,-9.306285,2.488628,7.832721,-7.650034,-9.937751,-5.451356,-2.050484,3.309171,1.623020,7.512576,9.987984,-3.039157,-0.180104,-3.515719,-6.611565,5.138711,7.147992,6.717619,6.547628,2.573805,-0.875894,-2.029441,0.960324,9.992942,4.153351,7.996599,-9.676461,4.346547,9.861981,7.783411,3.711419,-3.980261,3.611297,4.476341,2.496842,-4.868162,-1.459356,0.856684,-8.500321,-8.340257,5.262577,-4.234462,0.066370,-1.399723,0.191209,-9.565768,4.788958,5.589757,-1.923519,9.918809,5.068893,3.286446,-9.435190,-1.231597,5.981046,-5.751201,-9.703513,5.089596,9.628757,-6.562187,5.535217,7.833174,-0.039196,-4.300002,9.859502,-1.902707,9.952666,-7.629123,-8.707073,1.316364,1.308675,-7.148905,-0.939553,4.101345,-4.224365,4.527773,-1.854954,-9.540352,6.225975,-7.321627,-4.168123,-1.525570,-2.515029,8.389515,9.954950,9.925831,-6.555584,-1.232259,9.987756,-4.930171,6.855216,8.280133,-0.791308,-7.413224,-6.958513,-7.566682,-2.560247,6.619559,3.324779,4.038942,1.897544,7.239542,5.479681,-3.453373,7.807239,-5.358432,-9.317308,7.390843,0.164183,0.185593,-7.713362,-7.436597,-4.079266,2.656942,-7.362125,-0.576666,3.510678,5.312759,6.722231,9.085867,6.080181,6.579758,-0.606686,-1.692972,5.859412,3.085215,-2.040814,-1.971022,6.437299,-4.591608,-3.437164,2.731305,4.514813,-1.114010,3.962303,7.560253,7.327141,-0.938126,6.306046,8.741614,-3.864532,-7.849982,-1.102476,7.498901,3.510779,6.068012,-3.104802,4.205025,-3.449202,-8.487631,-6.865971,-0.059703,1.705017,7.634068,7.098557,9.834683,2.201154,-2.190786,-6.701091,-3.389528,-3.081459,5.865090,-4.384510,-5.972207,3.717088,-0.032355,-9.275753,7.640729,-2.960916,6.298220,-8.887211,4.420947,-8.424219,6.710530,-5.291917,-4.827954,-3.881412,7.996248,9.130294,6.566152,9.578681,-0.017389,-2.929181,1.570230,-7.299694,-7.311186,4.722824,-0.173680,-5.696474,-5.023482,6.905237,1.626255,-5.111034,6.694909,-6.822599,-4.891963,-1.635001,8.138376,4.843062,6.016580,3.053773,-0.445733,-8.114957,8.155437,-0.924607,9.271794,-3.689698,4.595251,1.791828,-0.053662,9.231623,1.214821,6.574485,-8.873741,7.803540,-0.392577,-0.431631,7.592057,-3.966530,0.899549,-2.717068,-2.624574,7.007961,-6.939264,-5.746486,-2.070063,1.908239,-0.637553,-9.972070,3.013209,-3.345974,1.776210,-6.586600,1.534940,5.191865,-1.889138,9.115017,-7.946399,-3.490654,-2.494875,-7.199474,9.425950,-2.530573,-1.724229,-1.819405,4.297846,-7.343545,7.563752,7.887712,0.102811,7.324266,2.220331,-3.101604,5.720147,-0.926447,-1.321561,-8.847638,-8.817582,3.499288,-3.754928,5.641470,-4.658184,-8.428280,-6.936328,0.849222,-8.493100,5.626807,3.142220,8.769730,6.056040,-5.795186,-4.960499,5.186116,-9.150386,-8.046240,-7.137651,-8.340965,0.183688,5.259539,-3.515090,5.133068,8.710418,-9.150299,-6.628202,-5.574047,0.989610,3.481373,0.295357,1.384372,3.005561,-3.806602,5.655739,1.072548,2.847351,-1.303024,6.590714,-1.745836,0.401708,8.614500,0.184394,5.119229,8.425700,-6.124833,9.384462,-7.331862,0.045102,-6.619988,0.986582,2.369510,-7.896769,-9.321447,6.612306,0.090354,-1.220233,3.500922,-5.799749,-0.839513,9.555473,-9.246110,-1.942240,-2.036721,-6.125285,-3.005592,-3.932284,-1.729918,-1.386373,-7.010598,-5.084223,-2.143413,-4.755394,-9.756435,-6.187867,-4.148443,9.907132,-8.232502,7.443302,-4.575110,7.523010,2.890399,-3.720545,1.803533,5.235340,8.815954,1.737647,-3.553698,0.507293,-8.217657,6.273951,1.289069,8.416633,7.666520,-1.820101,-3.975469,-0.072293,8.049474,-6.286773,0.620924,-3.033870,0.160938,-1.678229,-1.385754,-6.979654,0.677757,5.884479,-4.577801,-6.732303,-7.983858,5.969447,6.519887,-1.950931,8.837430,9.522022,-4.845487,8.989813,8.743575,4.334652,7.126332,-8.533594,-9.716728,1.064876,-1.943006,-1.889963,3.867692,-3.959271,8.601115,4.216849,6.125376,-9.362623,5.061504,8.718983,8.987674,-6.435406,-3.886211,-8.844025,-4.462424,8.375047,8.340604,6.950702,-5.640699,8.870858,3.149554,-9.997086,8.770736,-1.867405,-1.970071,1.476812,3.420975,-5.829966,-3.871205,-4.643267,-6.696001,-2.082557,1.071471,-3.663293,5.648093,4.046107,6.232365,1.518360,-0.665388,7.190093,8.749878,8.964667,-4.487566,-8.731063,-2.225423,9.026220,-4.027902,-7.513633,-8.109793,4.052051,4.444949,-7.331314,-3.404033,6.107712,4.329985,1.431450,-1.416807,4.107941,-5.261803,4.644745,-0.035707,-7.912712,-7.662831,-0.824546,6.340816,-6.516594,5.847654,8.182262,-0.159611,-7.209556,1.719684,-8.730217,-0.467293,-4.669820,3.148510,5.866989,9.189753,4.093865,6.345382,-4.686585,8.985530,2.574551,0.383212,3.918854,8.456878,3.256397,6.544744,-8.910497,-7.912822,4.856735,4.189508,0.546360,-5.292981,-5.567985,0.386008,-3.205196,-1.675212,5.436145,3.827020,9.041505,-6.955069,7.862965,7.753371,-6.295260,8.317882,3.550243,-4.518782,7.374912,7.983306,-0.091294,-7.469204,-5.523243,-7.852792,-2.987899,-5.985352,6.260315,-3.874844,-5.156212,-9.562789,1.937802,-8.060833,-8.626226,-1.578241,5.861752,-0.136728,-7.951385,7.923725,4.778206,-5.474428,6.859102,6.080948,9.706678,1.070813,8.681771,-7.156838,8.632022,-6.984008,-9.793559,6.216268,-1.762795,9.543672,-3.788138,9.110721,9.219904,8.788621,-4.603690,9.898485,7.234805,-2.549774,-7.573941,6.060575,3.603503,-3.324949,-2.899457,-3.254218,1.534227,4.169654,-1.797829,6.359692,-9.517337,-3.538627,0.213698,6.372175,-1.700152,-7.685330,-9.767660,5.249509,1.636190,3.507440,4.644561,-7.664561,-8.389365,3.298587,1.021390,-1.465588,1.653861,-2.861477,-9.910164,9.898225,5.579140,4.804461,-3.267826,-2.793722,-3.006604,5.694989,6.444661,-5.219743,-2.331960,-8.939596,-3.867254,7.238016,4.566568,6.394279,9.118709,-4.819986,-6.169542,9.887238,-9.751982,-1.136633,9.082368,2.013854,3.464629,-7.767089,4.244659,5.587774,3.640184,6.691451,6.700417,-5.761971,-5.995537,0.495462,4.994166,9.005018,-3.000135,-1.890979,3.008532,-5.822833,-0.609514,-3.257331,9.997065,7.861504,5.934310,9.027525,9.276774,9.594503,5.480916,-2.891708,0.778296,-4.921515,4.268829,-0.649325,-5.088489,-2.009993,6.947352,-0.137187,-3.560293,-4.965189,0.097732,-2.945162,8.564646,-1.776678,1.746541,9.092036,-6.648081,-8.396601,4.029928,-3.001760,-4.077942,-6.400701,-3.491051,-0.318421,-6.026566,-5.784936,8.120521,3.726278,-7.037039,0.268011,-9.700063,9.776387,-2.785325,1.041433,-1.143876,-6.809329,-1.979567,-0.185949,4.762487,2.323967,5.653516,8.003512,9.383003,-2.983127,-2.833312,7.065307,-9.680854,0.224671,-0.629154,-0.757245,1.857816,4.476729,9.451553,-2.714590,9.671820,1.019732,1.964077,8.213939,5.693881,-6.008370,0.241655,-0.901965,-9.450012,-6.362926,-4.219919,4.530321,1.337349,5.435290,1.503637,-9.833024,-5.282545,9.525547,-3.831017,-0.646971,-0.958938,-8.193199,-4.220152,-1.529572,-7.518276,8.696768,6.562853,-8.260704,-4.043366,-5.453401,7.337056,-7.712912,-0.269851,0.312342,-4.979469,-3.988131,2.614660,-9.524228,3.440872,-1.324607,8.694169,7.665053,7.047709,-8.503738,2.932854,1.396349,1.654067,-5.062098,4.277517,-3.775525,1.929976,8.869135,9.501665,-9.958150,-0.335971,1.203277,8.623749,-6.148304,-6.930057,-3.824074,6.314905,3.603457,9.388843,-2.159010,0.413745,-7.335637,2.781643,1.576578,9.712985,-6.802101,1.609504,1.753648,-1.480199,2.655455,-3.938394,-9.644966,6.198936,-0.957255,-8.938474,6.248991,-9.422382,-4.428187,1.994760,-1.683229,-5.318934,-0.497589,-3.379303,-1.100546,-6.537915,-9.449983,4.379178,-9.245521,-4.478895,2.924604,-2.839762,-3.850109,-9.897696,-3.145787,6.419608,-3.329945,5.838290,2.679613,-6.239437,-6.558543,7.367014,-1.331949,-6.421309,7.512566,0.396138,6.584417,9.286160,-7.215316,-2.383130,-0.071573,-9.580464,2.903863,4.203454,0.133304,-5.366071,-3.178603,-5.819842,-9.726736,-1.609284,7.555920,-7.599072,0.593895,0.665568,4.689864,-7.033157,5.006153,-8.338965,4.914654,7.024421,-5.267660,-8.341721,8.308502,2.838053,0.543014,9.088372,9.912798,3.387260,1.244979,2.552822,1.346021,-1.817776,-6.251186,2.313421,7.955938,-3.102746,5.002693,-5.088238,-0.407293,-3.006875,5.695205,-8.181367,-4.114572,7.004109,-7.689013,-1.962654,9.147253,-1.470410,-2.373751,7.028897,-7.169529,6.692432,-3.401856,-7.125043,5.245139,4.747041,-7.392516,7.374607,2.777132,7.719348,3.721558,6.297463,-9.477306,-5.101964,-7.173269,-2.799712,-2.987311,-8.618581,-6.927777,4.313645,1.320718,-6.574461,-3.456705,-3.797927,7.100716,-2.955851,-4.155949,4.310477,0.106677,6.996209,7.568193,3.215244,4.962110,-3.000503,-1.325186,4.914844,-3.570538,-2.165496,2.380731,5.454448,-0.968243,-4.704238,5.808724,1.475158,9.917479,-0.539531,1.367067,-5.602598,0.764400,-7.860731,-7.417654,-2.790219,2.027398,-0.463557,4.305600,8.812645,9.868011,-6.359061,6.717469,4.572693,-9.762719,8.230039,4.786980,-9.249107,9.974348,7.234869,-9.057836,-2.761196,-0.749822,2.456282,-5.932111,0.322966,-5.021894,1.953258,4.260514,-1.084035,-3.490250,9.363246,-6.496948,1.207474,-8.239280,4.272553,-2.158377,1.384020,-2.002649,-4.434315,3.228765,-1.028533,-0.871700,-5.698122,9.774436,3.643222,-8.047637,7.053989,7.836873,-0.145866,4.870214,-7.008226,-2.369652,-4.573065,-9.772707,5.601918,-7.171771,5.335297,2.686091,4.675898,8.349079,7.600681,1.450803,-2.317403,4.384244,1.835749,-8.669796,-6.597282,0.222500,-0.619792,0.517834,7.705246,6.724713,-2.361838,-9.179658,1.609805,8.086939,-3.597683,-0.321111,1.195321,2.907134,-7.119932,-9.831529,-6.668226,-7.370466,-1.595453,6.335949,8.040426,-2.725449,0.417177,8.920607,-4.184668,2.288362,-3.917287,1.667754,7.936559,-0.017775,1.226273,-3.085582,-4.407620,-0.549092,4.894927,-4.510838,-0.478223,-8.566935,-4.993208,1.061535,-8.265322,5.898779,-4.349343,-7.739693,1.266308,5.865524,-6.652696,3.201233,-6.976705,6.631674,1.979006,5.998611,-6.375108,2.168054,3.053125,-5.961725,-8.631371,-4.198013,-5.106608,-6.959728,1.795834,-4.387309,-1.333285,-2.345671,7.163382,-3.688037,-2.924194,0.620376,4.470838,3.916795,8.125423,1.568917,7.283564,-5.569574,-6.214056,3.416251,-5.869204,5.512399,3.610255,-5.749252,4.873158,2.413300,-1.353769,9.446555,-5.532451,-0.858585,-9.533091,1.265705,-8.678151,4.352768,-3.215009,-1.303771,4.630543,4.337380,-7.398536,9.429628,-7.259643,3.907751,7.591232,6.507034,9.621840,6.014869,6.398717,9.418841,-2.886658,-4.172733,3.728089,-8.424135,4.693612,-5.512513,5.204393,9.896308,-4.968493,-5.296278,9.542327,8.896880,3.633413,-3.412009,5.131980,-7.257553,8.338693,0.969369,-2.837211,1.850599,8.719988,8.711612,5.262686,6.694212,9.801858,-6.407399,5.422914,2.303384,-3.349318,7.937721,9.719036,-4.626504,-6.767882,1.388255,9.592785,-8.074950,-9.833053,9.292212,1.620027,-0.362617,-3.383988,3.568537,-0.518299,-3.144314,5.937825,1.318646,-0.402317,1.746292,9.767979,3.204601,8.074294,5.520327,4.348193,6.984060,8.868810,7.646862,-4.494793,3.526273,8.929192,-2.047913,3.298988,6.537912,8.953615,3.264567,0.796094,0.806185,-1.056792,1.290372,8.059773,-6.955755,-2.929962,-7.338909,4.569958,5.047845,6.914653,7.305965,3.258525,-0.236629,3.421208,4.935561,-0.446657,4.723579,-9.936404,-0.168420,6.286450,-7.838987,-9.887993,8.002530,2.266614,-6.898533,-0.326106,2.178375,-7.313187,-6.480046,5.211497,9.868284,-0.875535,9.231733,8.902134,-7.639935,-9.692242,-6.744184,2.115871,-3.659367,-8.468969,8.719826,-8.225638,9.889307,0.209389,-4.239369,4.264058,-3.177289,-8.096997,-8.010370,-9.255305,8.583015,-0.499187,7.592592,5.839474,-8.334652,3.446369,-0.368251,-5.851232,-8.695057,2.148757,3.133810,-1.763878,-9.341653,0.282652,-7.086948,1.379422,-5.913576,4.342026,8.681238,-8.988276,6.706928,6.200494,0.935405,1.150162,4.566727,6.155872,9.777203,1.781639,-5.509624,5.760515,-0.224389,-7.740871,-6.018253,-2.991654,-1.641015,3.431093,-7.041762,9.864289,-2.641844,-2.207805,5.316331,-1.758810,2.986713,-2.042927,-7.102138,3.944089,-7.376690,-0.814963,1.897618,-2.125712,7.323537,0.134100,3.586161,2.207396,8.861920,5.082222,8.820359,-7.310467,9.224991,1.180250,-9.886554,-6.328841,-1.492188,1.437093,-3.192476,-0.384206,8.568115,7.749063,-4.324957,-0.057739,-6.262426,7.357190,-4.337416,6.187031,-7.850462,4.108140,6.071480,-9.982198,-7.327952,9.944275,1.602854,-3.075328,-3.414303,8.617914,6.354934,-1.807496,-7.952914,4.326955,4.084103,-7.256471,6.259330,-4.140141,-9.347577,4.278799,-5.704278,1.984061,-8.595175,-9.091009,6.030674,7.618101,-6.157533,5.882523,0.345372,1.546008,8.189082,1.184280,6.562454,5.014501,-4.904921,1.781268,4.315384,-0.001511,-4.781048,-1.751698,7.187491,-1.926633,-6.592373,-0.308262,3.652999,-5.224721,1.061111,9.672865,-4.272730,-3.792940,8.457957,5.203820,-1.049760,-6.560350,3.387692,5.113186,9.801754,-3.920524,2.075032,1.131660,-4.119002,6.511276,9.778051,-8.145513,1.025357,-9.211518,-6.239406,9.442959,-8.884980,-2.167546,4.351594,-8.239370,6.070002,-8.490070,9.204299,8.549100,7.734002,5.265618,-4.650612,-2.097529,2.164988,-7.128186,2.316383,-4.072841,-9.005475,6.019245,-3.676458,-0.371688,-0.873897,-7.827082,-6.603917,6.339796,-7.011601,5.746427,-4.414915,-6.725479,-2.092986,-2.417343,8.991256,7.555485,5.430759,0.423263,-9.131043,8.402868,-4.815267,-6.436459,-1.099110,-4.850305,6.730052,1.688593,-1.311456,1.933476,-2.516643,-8.783956,-6.305502,2.232978,-4.097136,-7.839180,-1.623104,2.400310,7.871882,-4.406629,5.233682,1.004505,-6.871979,-6.378798,-8.063751,5.857081,9.975740,-5.103979,-1.180260,1.267374,-3.727412,1.694949,-4.218055,3.270810,9.244512,2.877624,4.963180,5.567866,5.391923,-5.382849,8.907779,-1.242910,3.474700,-2.673483,7.939093,-1.516201,7.413111,-3.864066,-8.456028,-0.928555,7.198939,-0.919565,-2.698379,-4.721272,2.019650,6.625929,1.662989,-4.456106,7.022950,-6.259504,-0.975390,-6.566486,-2.076825,3.925002,4.013031,-8.535360,2.616970,3.872485,-8.724714,1.402636,-7.721261,-0.407413,7.468902,-7.711255,-2.372722,4.409955,9.570743,-7.871186,-0.414479,-0.672676,3.063060,1.232379,9.668813,-2.209400,-3.425153,2.156858,6.455134,-3.358611,-6.759484,1.810344,7.898242,-2.083217,-6.626903,5.269162,-9.787002,-9.440693,-8.925830,5.649414,-4.892044,-0.974289,6.401741,4.346966,8.490041,9.367947,-9.996683,-3.174476,7.541666,-0.162183,-3.021201,5.680213,3.719055,-9.498136,9.373127,0.697113,-8.905350,-3.634494,-3.676514,-8.831051,-3.058361,7.545974,-1.523626,-9.905194,-9.255315,2.105009,-3.021184,-0.034211,7.539582,-1.069175,-0.674427,-6.801201,5.337252,-5.955923,4.500028,3.934939,7.940650,-5.040629,3.000290,6.478047,-9.028889,-7.473171,2.981617,-6.597672,3.091679,4.345369,7.057794,-0.184697,2.932769,-4.141894,7.015451,-9.709388,-2.359002,-7.027041,0.077970,-9.635800,5.593330,2.033936,8.580220,9.874712,-4.642323,-6.129864,-5.835446,-1.776575,1.446273,-8.474069,-0.003076,8.619722,-9.666010,-9.047962,-1.899107,3.301817,7.296548,-0.318092,-2.923985,-8.620945,6.805704,-9.216605,1.988088,8.659242,6.217516,-0.478044,-5.155144,4.080996,6.948190,-7.420937,-3.527623,4.519475,-8.524939,-6.760092,7.607363,9.739332,3.457492,8.035524,-9.038801,3.143811,-3.489401,-0.356365,-1.587288,4.870507,5.489911,4.967830,8.855317,-1.837963,-1.542293,9.874930,1.104543,-9.836406,-9.783148,3.197231,-2.111449,5.152006,-9.127177,9.424325,8.538293,1.599107,4.442881,-8.274705,5.578167,-7.898985,8.258542,-6.495508,4.787707,1.865715,-0.226596,-9.305651,2.127100,0.783510,5.608251,-8.219186,-4.665328,-6.983870,-4.427711,-7.458110,1.447777,-3.324997,-2.161075,0.258595,8.277168,-6.691882,8.532000,3.073264,-5.870367,2.903278,0.903138,-9.826836,0.590839,5.944698,0.047574,8.782446,7.462631,1.165570,-9.157674,5.761809,9.576311,1.466736,-9.764894,7.091942,-4.051983,8.923544,8.782505,7.327465,-9.593086,-1.316530,-0.188377,-2.101470,1.258842,-4.913000,-1.575263,-0.262602,0.658531,-7.045087,-2.426212,-4.942290,-6.189766,-5.827253,9.562258,-4.793839,1.412009,8.911418,1.621882,8.733711,1.089447,-0.227187,6.753281,5.514612,4.410301,-3.175188,0.241172,-7.941670,-1.360068,3.362510,-0.519509,1.194418,8.465672,3.101105,-4.733819,6.935391,-6.627295,1.817993,-8.249542,-9.095840,6.456435,1.837995,7.969612,-3.447236,5.298563,5.040953,-9.297122,7.715217,0.769706,-3.527808,3.209276,1.933383,1.576907,4.404920,4.953063,3.243545,-2.865973,-2.315345,-8.089190,-7.719995,-3.071246,5.203070,-2.725350,-3.002970,-1.352559,-3.023885,9.731564,4.555443,-9.374593,-4.059730,1.645382,-4.986570,8.380444,3.131358,-1.825881,6.248688,-9.358042,5.112585,6.449182,-9.027149,-8.596800,3.712021,2.643732,-9.805709,3.651350,3.390796,5.163153,-0.773466,-1.425163,-3.469813,1.135427,-1.936122,3.911569,0.606651,1.329198,-9.075248,-5.917832,7.050581,-4.203356,3.219580,0.155560,-4.734841,6.342959,0.371800,8.313407,-6.656785,8.026496,-3.537923], dtype = "float64")#candidate|14430|(2016,)|const|float64
var_14431 = relay.var("var_14431", dtype = "uint16", shape = (880,))#candidate|14431|(880,)|var|uint16
call_14429 = relay.TupleGetItem(func_1484_call(relay.reshape(const_14430.astype('float64'), [9, 14, 16]), relay.reshape(var_14431.astype('uint16'), [880,]), ), 3)
call_14432 = relay.TupleGetItem(func_1488_call(relay.reshape(const_14430.astype('float64'), [9, 14, 16]), relay.reshape(var_14431.astype('uint16'), [880,]), ), 3)
output = relay.Tuple([bop_14426,call_14429,const_14430,var_14431,])
output2 = relay.Tuple([bop_14426,call_14432,const_14430,var_14431,])
func_14444 = relay.Function([var_14424,var_14425,var_14431,], output)
mod['func_14444'] = func_14444
mod = relay.transform.InferType()(mod)
mutated_mod['func_14444'] = func_14444
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14444_call = mutated_mod.get_global_var('func_14444')
var_14446 = relay.var("var_14446", dtype = "uint32", shape = ())#candidate|14446|()|var|uint32
var_14447 = relay.var("var_14447", dtype = "uint32", shape = (14, 14, 6))#candidate|14447|(14, 14, 6)|var|uint32
var_14448 = relay.var("var_14448", dtype = "uint16", shape = (880,))#candidate|14448|(880,)|var|uint16
call_14445 = func_14444_call(var_14446,var_14447,var_14448,)
output = call_14445
func_14449 = relay.Function([var_14446,var_14447,var_14448,], output)
mutated_mod['func_14449'] = func_14449
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9674_call = mod.get_global_var('func_9674')
func_9675_call = mutated_mod.get_global_var('func_9675')
call_14464 = func_9674_call()
call_14465 = func_9674_call()
output = relay.Tuple([call_14464,])
output2 = relay.Tuple([call_14465,])
func_14472 = relay.Function([], output)
mod['func_14472'] = func_14472
mod = relay.transform.InferType()(mod)
output = func_14472()
func_14473 = relay.Function([], output)
mutated_mod['func_14473'] = func_14473
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14340_call = mod.get_global_var('func_14340')
func_14342_call = mutated_mod.get_global_var('func_14342')
call_14479 = func_14340_call()
call_14480 = func_14340_call()
output = call_14479
output2 = call_14480
func_14483 = relay.Function([], output)
mod['func_14483'] = func_14483
mod = relay.transform.InferType()(mod)
mutated_mod['func_14483'] = func_14483
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14483_call = mutated_mod.get_global_var('func_14483')
call_14484 = func_14483_call()
output = call_14484
func_14485 = relay.Function([], output)
mutated_mod['func_14485'] = func_14485
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5717_call = mod.get_global_var('func_5717')
func_5718_call = mutated_mod.get_global_var('func_5718')
call_14512 = relay.TupleGetItem(func_5717_call(), 0)
call_14513 = relay.TupleGetItem(func_5718_call(), 0)
func_3802_call = mod.get_global_var('func_3802')
func_3804_call = mutated_mod.get_global_var('func_3804')
var_14525 = relay.var("var_14525", dtype = "float64", shape = (480,))#candidate|14525|(480,)|var|float64
call_14524 = func_3802_call(relay.reshape(var_14525.astype('float64'), [12, 4, 10]))
call_14526 = func_3802_call(relay.reshape(var_14525.astype('float64'), [12, 4, 10]))
func_6610_call = mod.get_global_var('func_6610')
func_6615_call = mutated_mod.get_global_var('func_6615')
var_14540 = relay.var("var_14540", dtype = "int64", shape = (390,))#candidate|14540|(390,)|var|int64
const_14541 = relay.const([[-10,-3,10,-5],[2,9,3,8],[-4,-6,-4,-3],[-8,10,4,4],[-4,-6,2,-7],[7,10,8,5],[8,10,-10,-10],[3,4,7,1],[4,8,-9,10],[10,7,-7,-1],[-6,6,-3,-4],[8,6,-5,-9],[-4,-3,-3,-10],[5,5,2,5],[-7,3,1,8],[7,-5,1,-9],[4,-8,7,9],[5,-1,10,-4],[1,8,-5,9],[2,-4,9,-10],[5,9,-5,-3],[-4,9,2,-2],[-1,3,9,-9],[10,-4,7,4],[-1,4,-3,8],[1,3,1,6],[-6,-9,3,-3],[-1,3,-2,-10],[10,-1,-10,10],[10,-5,-9,-4],[-10,-9,3,7],[1,-2,7,-10],[-3,-9,3,4],[-5,4,-10,8],[-3,4,-10,-10],[2,-6,1,7],[-8,-8,-8,-2],[-1,-8,9,2],[4,8,8,-7],[-1,9,-8,7],[-3,-6,-9,-7],[-7,3,2,7],[-1,1,4,-8],[-2,8,-5,7],[2,-2,-2,-1],[-3,-6,-10,-4],[10,8,5,9],[-7,7,-4,10],[6,6,1,8],[4,1,-6,4],[-2,10,-2,-3],[7,-9,-4,6],[-10,-1,-2,5],[2,-9,-10,-4],[7,10,-4,8],[-4,-4,-7,10],[3,-10,-8,-10],[-2,-3,-3,-5],[-3,-2,7,-10],[-9,9,5,5],[1,-4,10,-1],[4,-5,1,1],[-6,-2,-5,5],[-9,1,-4,-5],[-2,5,-2,4],[-10,-4,10,6],[-8,-10,3,8],[10,9,8,10],[-2,1,1,1],[-6,-4,-2,-4],[-9,5,8,5],[3,-3,-7,-10],[-7,-4,-8,-10],[1,5,-2,-4],[-3,-6,-2,-8],[-4,-5,-5,-1],[-8,9,-9,-4],[-2,-4,8,-7],[6,-2,4,-3],[-3,1,-5,-8],[-9,-9,-7,9],[-2,4,-2,8],[2,-8,10,-7],[2,-8,-2,8],[-5,-10,-9,-2],[5,-10,-4,-6],[-10,5,6,4],[-1,2,1,7],[-8,10,9,10],[-5,10,3,-8],[-10,5,-6,-5],[1,4,-9,2],[9,7,-2,-1],[-9,8,9,-5],[8,7,10,3],[-9,-5,-10,-6],[-9,-7,1,-9],[1,2,-3,10],[-8,-7,1,2],[-7,-10,4,-5],[10,3,4,-2],[7,-6,5,-2],[-7,3,-9,7],[2,2,-5,8],[-1,-9,-2,9],[-6,-2,4,-6],[-2,-6,4,8],[3,1,-1,5],[1,-6,-4,-2],[3,-3,-7,6],[10,4,-7,1],[4,-10,-2,-6],[9,-3,8,-3],[-1,-8,7,-10],[5,-10,-8,-4],[2,9,9,6],[7,8,9,10],[10,-8,1,-4],[4,9,-7,-6],[7,5,-1,5],[-2,-7,6,1],[-3,-5,-9,-1],[2,-6,-4,-8],[-8,-8,-3,8],[6,6,-1,10],[-6,-8,-1,-1],[-8,-4,1,-3],[6,-9,6,6],[-3,6,1,-7],[8,-5,4,-5],[-1,5,2,3],[3,9,-9,1],[-1,-3,-10,3],[-8,10,2,-4],[-4,-7,1,6],[-1,-1,-4,-2],[7,9,-8,7],[1,-7,3,-6],[-4,-7,2,-9],[10,3,2,1],[3,-9,4,-6],[-5,6,6,-9],[4,5,9,10],[4,3,1,7],[6,4,6,-5],[-4,-1,2,3],[5,-3,-2,4],[-8,-3,-5,-4],[8,2,-9,5],[9,-4,-7,8],[-4,8,8,3],[-3,7,-7,-8],[9,1,9,1],[-3,1,-1,5],[2,3,-7,5],[3,7,-3,6],[-7,9,-2,-5],[5,-6,5,-4],[-7,8,-1,4],[-7,5,6,-3],[6,-2,-4,5],[1,10,5,4],[10,5,-6,-5],[-10,2,-2,2],[1,-8,8,-6],[9,6,9,7],[3,1,1,-2],[-8,8,1,10],[3,-7,-3,10],[1,7,8,-9],[6,-10,-8,9],[-7,6,8,-10],[-5,-1,-3,2],[9,-4,-3,-9],[5,-5,10,-8],[2,6,9,-2],[4,5,-6,-1],[-6,5,-10,-8],[4,7,-9,2],[9,5,4,4],[-1,-5,-6,4],[-3,-3,1,-7],[5,10,7,7],[-10,5,10,-1],[-8,7,-5,6],[-10,-1,10,-8],[2,-3,2,6],[-4,5,8,-4],[4,-10,4,7],[7,-9,-5,-6],[-4,5,-10,-7],[2,8,-10,8],[-6,3,6,-8],[-7,4,1,-9],[8,3,7,-2],[-4,8,-3,-7],[5,-10,1,6],[2,-2,-9,-2],[-6,-6,-8,1],[7,5,-6,-8],[6,3,-6,5],[-10,-5,-9,7],[3,-8,2,-3],[3,-8,4,-1],[5,-8,-5,-3],[2,-4,-6,-6],[-4,1,8,-4],[4,9,9,-10],[3,9,3,-3],[-9,-7,7,3],[-10,7,8,8],[-7,-2,6,-3],[2,-9,2,-1],[6,-6,-1,-4],[3,10,5,5],[-4,8,-1,-3],[3,-9,1,-7],[-7,-9,4,-1],[7,8,9,3],[8,-5,4,-3],[9,3,-1,-6],[7,-7,1,6],[7,-9,7,2],[-5,6,5,6],[1,-4,2,-9],[7,10,3,-7],[1,-9,-10,-4],[7,4,-9,-6],[10,3,1,-2],[9,8,9,-4],[-3,-1,-3,-8],[4,4,2,6],[-1,-3,10,-3],[-9,-10,-8,1],[7,-4,6,1],[-6,7,-7,10],[-3,-10,-2,1],[4,2,-6,-3],[6,1,3,-5],[-9,9,-5,-3],[3,1,-8,7],[-4,6,-1,-2]], dtype = "int64")#candidate|14541|(242, 4)|const|int64
var_14542 = relay.var("var_14542", dtype = "float64", shape = (546,))#candidate|14542|(546,)|var|float64
call_14539 = relay.TupleGetItem(func_6610_call(relay.reshape(var_14540.astype('int64'), [390,]), relay.reshape(const_14541.astype('int64'), [11, 88]), relay.reshape(var_14542.astype('float64'), [546,]), ), 0)
call_14543 = relay.TupleGetItem(func_6615_call(relay.reshape(var_14540.astype('int64'), [390,]), relay.reshape(const_14541.astype('int64'), [11, 88]), relay.reshape(var_14542.astype('float64'), [546,]), ), 0)
func_4683_call = mod.get_global_var('func_4683')
func_4685_call = mutated_mod.get_global_var('func_4685')
call_14548 = relay.TupleGetItem(func_4683_call(relay.reshape(var_14525.astype('float64'), [480,])), 2)
call_14549 = relay.TupleGetItem(func_4685_call(relay.reshape(var_14525.astype('float64'), [480,])), 2)
func_12690_call = mod.get_global_var('func_12690')
func_12693_call = mutated_mod.get_global_var('func_12693')
const_14553 = relay.const(-7, dtype = "int64")#candidate|14553|()|const|int64
const_14554 = relay.const([2,-5,-7,-9,7,-8,3,-4,-10,7,-8,-8,-8,-3,5,-9,9,3,-3,10,-4,-10,4,-4,-2,8,6,1,8,-1,1,10,-4,-5,5,-6,6,8,1,-6,6,5,9,-6,-9,8,6,9,10,6,1,-8,9,9,-9,7,7,7,-5,1,-1,5,8,7,9,-5,7,-9,9,-8,-1,6,-4,-3,8,-4,-6,6,2,2,-7,4,-10,10,-1,10,3,1,8,8,-2,3,-3,10,2,-1,-8,-3,-9,8,1,-1,3,-2,8,7,6,7,-8,-9,10,-9,4,-9,-5,3,6,-10,8,1,6,7,7,3,3,-6,-3,-3,9,10,-10,9,6,4,5,-9,1,-3,10,-6,2,-9,-8,-10,6,-10,4,10,-3,6,-10,-7,1,-1,-9,-7,10,-4,8,-7,5,-9,-9,10,5,-9,1,10,-7,-4,-10,7,-6,-10,6,-7,5,3,6,7,9,10,2,-1,-3,-9,-7,4,-9,6,-2,-8,8,2,-5,7,2,4,-7,7,4,-4,-2,4,5,-9,-4,5,-10,-8,-3,-9,-2,3,9,-1,5,6,6,-3,2,1,8,-8,10,-3,10,-9,6,4,-3,-8,2,10,-4,10,-2,1,-6,10,6,-8,5,1,-1,-7,-9,5,-1,-9,5,-2,-10,-8,-2,2,-2,-4,-10,-10,-9,-7,4,-10,-6,-1,-8,-7,3,-7,-6,5,-1,-6,-6,-4,-3,-5,-3,-3,2,10,-4,2,-6,4,-8,-1,10,2,4,-10,6,-6,-10,10,1,-4,8,-2,-5,-6,5,-3,-5,-10,-2,-9,-8,9,-4,-2,10,-1,3,5,-2,-4,10,-4,4,-7,-8,5,1,-6,5,-1,-5,7,8,8,5,-8,9,4,-8,8,-5,-2,8,-1,-7,10,-7,-9,-9,4,7,2,4,9,-7,7,-1,8,10,-2,6,-8,9,7,-4,-5,-4,9,3,9,-5,1,9,5,3,-6,-1,1,2,1,10,7,3,2,-3,7,1,-6,-1,10,10,2,-10,3,-4,6,-2,-10,10,-2,-6,1,-9,10,9,4,5,1,1,-7,-10,-1,-7,-9,2,2,-2,-5,-1,3,-4,7,4,-9,4,2,-1,8,3,-7,-9,-4,1,6,-6,-9,-5,-2,-6,4,6,-6,8,-5,1,7,-10,-3,-10,-4,-7,9], dtype = "int64")#candidate|14554|(450,)|const|int64
call_14552 = func_12690_call(relay.reshape(const_14553.astype('int64'), []), relay.reshape(const_14554.astype('int64'), [15, 6, 5]), )
call_14555 = func_12690_call(relay.reshape(const_14553.astype('int64'), []), relay.reshape(const_14554.astype('int64'), [15, 6, 5]), )
output = relay.Tuple([call_14512,call_14524,var_14525,call_14539,var_14540,const_14541,var_14542,call_14548,call_14552,const_14553,const_14554,])
output2 = relay.Tuple([call_14513,call_14526,var_14525,call_14543,var_14540,const_14541,var_14542,call_14549,call_14555,const_14553,const_14554,])
func_14564 = relay.Function([var_14525,var_14540,var_14542,], output)
mod['func_14564'] = func_14564
mod = relay.transform.InferType()(mod)
var_14565 = relay.var("var_14565", dtype = "float64", shape = (480,))#candidate|14565|(480,)|var|float64
var_14566 = relay.var("var_14566", dtype = "int64", shape = (390,))#candidate|14566|(390,)|var|int64
var_14567 = relay.var("var_14567", dtype = "float64", shape = (546,))#candidate|14567|(546,)|var|float64
output = func_14564(var_14565,var_14566,var_14567,)
func_14568 = relay.Function([var_14565,var_14566,var_14567,], output)
mutated_mod['func_14568'] = func_14568
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10120_call = mod.get_global_var('func_10120')
func_10121_call = mutated_mod.get_global_var('func_10121')
call_14592 = relay.TupleGetItem(func_10120_call(), 0)
call_14593 = relay.TupleGetItem(func_10121_call(), 0)
output = call_14592
output2 = call_14593
func_14604 = relay.Function([], output)
mod['func_14604'] = func_14604
mod = relay.transform.InferType()(mod)
output = func_14604()
func_14605 = relay.Function([], output)
mutated_mod['func_14605'] = func_14605
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7447_call = mod.get_global_var('func_7447')
func_7448_call = mutated_mod.get_global_var('func_7448')
call_14623 = relay.TupleGetItem(func_7447_call(), 0)
call_14624 = relay.TupleGetItem(func_7448_call(), 0)
output = relay.Tuple([call_14623,])
output2 = relay.Tuple([call_14624,])
func_14626 = relay.Function([], output)
mod['func_14626'] = func_14626
mod = relay.transform.InferType()(mod)
mutated_mod['func_14626'] = func_14626
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14626_call = mutated_mod.get_global_var('func_14626')
call_14627 = func_14626_call()
output = call_14627
func_14628 = relay.Function([], output)
mutated_mod['func_14628'] = func_14628
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9649_call = mod.get_global_var('func_9649')
func_9651_call = mutated_mod.get_global_var('func_9651')
call_14653 = relay.TupleGetItem(func_9649_call(), 0)
call_14654 = relay.TupleGetItem(func_9651_call(), 0)
output = call_14653
output2 = call_14654
func_14687 = relay.Function([], output)
mod['func_14687'] = func_14687
mod = relay.transform.InferType()(mod)
output = func_14687()
func_14688 = relay.Function([], output)
mutated_mod['func_14688'] = func_14688
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12720_call = mod.get_global_var('func_12720')
func_12722_call = mutated_mod.get_global_var('func_12722')
call_14689 = relay.TupleGetItem(func_12720_call(), 0)
call_14690 = relay.TupleGetItem(func_12722_call(), 0)
func_8246_call = mod.get_global_var('func_8246')
func_8247_call = mutated_mod.get_global_var('func_8247')
call_14703 = func_8246_call()
call_14704 = func_8246_call()
uop_14706 = relay.cos(call_14689.astype('float32')) # shape=(13, 14, 3)
uop_14708 = relay.cos(call_14690.astype('float32')) # shape=(13, 14, 3)
output = relay.Tuple([call_14703,uop_14706,])
output2 = relay.Tuple([call_14704,uop_14708,])
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
