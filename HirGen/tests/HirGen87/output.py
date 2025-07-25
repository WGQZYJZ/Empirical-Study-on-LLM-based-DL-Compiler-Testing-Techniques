import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_236 = relay.var("var_236", dtype = "float32", shape = (6, 8, 14))#candidate|236|(6, 8, 14)|var|float32
uop_237 = relay.cosh(var_236.astype('float32')) # shape=(6, 8, 14)
uop_242 = relay.erf(uop_237.astype('float32')) # shape=(6, 8, 14)
uop_252 = relay.tan(uop_242.astype('float64')) # shape=(6, 8, 14)
output = uop_252
output2 = uop_252
func_256 = relay.Function([var_236,], output)
mod['func_256'] = func_256
mod = relay.transform.InferType()(mod)
var_257 = relay.var("var_257", dtype = "float32", shape = (6, 8, 14))#candidate|257|(6, 8, 14)|var|float32
output = func_256(var_257)
func_258 = relay.Function([var_257], output)
mutated_mod['func_258'] = func_258
mutated_mod = relay.transform.InferType()(mutated_mod)
var_436 = relay.var("var_436", dtype = "uint32", shape = (7, 1, 10))#candidate|436|(7, 1, 10)|var|uint32
const_437 = relay.const([[[1,10,-6,5,3,-6,-5,-6,4,-6],[9,8,-1,-7,2,-1,-5,-8,1,-6],[1,3,-4,6,3,10,2,-3,9,-5],[9,5,-9,6,6,-4,5,3,-6,-7],[1,-3,7,7,8,-8,-10,-3,-4,8],[-3,7,10,9,-8,-7,6,-5,7,-9],[-6,4,-8,4,5,3,4,8,-9,10]],[[-5,-8,8,-2,-5,-2,7,-6,10,-8],[4,5,-1,-2,1,-8,10,7,-7,-4],[9,-3,9,-3,3,-6,-3,5,-5,4],[8,4,8,-5,-10,9,-5,8,-6,-3],[-2,-4,-9,9,-5,-3,7,-10,-1,-3],[-5,2,9,-4,-1,-3,-5,8,-7,1],[1,4,3,6,10,7,-4,-7,-9,7]],[[9,10,7,9,6,6,6,-5,4,7],[1,-3,-10,-7,1,-10,-1,4,10,-2],[7,-2,-7,-4,-10,-7,4,7,10,5],[-5,-4,5,6,3,-2,7,-3,-2,-7],[9,-5,-4,9,6,7,-10,10,9,1],[-6,-4,6,7,-8,2,8,2,-2,8],[-6,-1,-6,-2,-7,-10,-5,-3,-2,10]],[[-5,-7,4,5,-10,-3,-7,-3,-7,1],[5,6,4,2,2,-7,-8,7,6,5],[-6,4,-5,8,9,6,9,-7,-3,-10],[-3,-1,-3,-3,2,-5,-8,-2,6,-7],[-9,3,6,2,1,2,1,4,-4,3],[5,-2,10,8,-6,-3,9,-5,-5,2],[-1,9,10,7,2,-7,1,2,7,-9]],[[4,-8,-7,-7,9,10,6,3,-5,-9],[4,6,9,-9,7,-9,-10,-5,9,-1],[1,-10,3,2,-6,6,9,7,9,4],[4,8,-10,10,3,8,5,1,-1,-7],[-4,-9,5,10,-4,2,10,3,-1,7],[-6,-7,3,10,-1,-1,10,-9,-9,-10],[5,-2,-10,-5,8,6,-9,9,-3,7]],[[6,10,-9,-10,9,-1,2,1,8,2],[2,-4,-10,-4,-1,-8,9,10,6,6],[2,2,-3,-5,-9,-1,-4,3,-7,9],[-7,3,-5,-4,7,-8,1,4,-1,7],[5,-2,-2,-4,-1,6,-10,-4,4,-7],[1,-1,-3,6,-1,5,-10,6,3,2],[-3,-2,7,-9,5,3,1,-6,-8,-10]],[[5,6,6,9,4,-3,-10,-1,10,-10],[-7,-1,-9,-5,-9,-8,2,-2,-10,6],[-4,10,-4,1,-2,-1,5,9,8,3],[-9,-6,6,9,-10,-7,-4,6,-9,-3],[9,-4,-5,8,-7,3,-1,8,8,3],[-2,2,-9,-7,-7,-1,-4,1,-6,-7],[2,-10,10,2,5,3,6,-7,-4,-3]]], dtype = "uint32")#candidate|437|(7, 7, 10)|const|uint32
bop_438 = relay.left_shift(var_436.astype('uint32'), const_437.astype('uint32')) # shape=(7, 7, 10)
output = bop_438
output2 = bop_438
func_456 = relay.Function([var_436,], output)
mod['func_456'] = func_456
mod = relay.transform.InferType()(mod)
mutated_mod['func_456'] = func_456
mutated_mod = relay.transform.InferType()(mutated_mod)
var_457 = relay.var("var_457", dtype = "uint32", shape = (7, 1, 10))#candidate|457|(7, 1, 10)|var|uint32
func_456_call = mutated_mod.get_global_var('func_456')
call_458 = func_456_call(var_457)
output = call_458
func_459 = relay.Function([var_457], output)
mutated_mod['func_459'] = func_459
mutated_mod = relay.transform.InferType()(mutated_mod)
var_679 = relay.var("var_679", dtype = "uint64", shape = (16, 14, 4))#candidate|679|(16, 14, 4)|var|uint64
var_680 = relay.var("var_680", dtype = "uint64", shape = (16, 14, 4))#candidate|680|(16, 14, 4)|var|uint64
bop_681 = relay.less_equal(var_679.astype('bool'), relay.reshape(var_680.astype('bool'), relay.shape_of(var_679))) # shape=(16, 14, 4)
func_456_call = mod.get_global_var('func_456')
func_459_call = mutated_mod.get_global_var('func_459')
var_687 = relay.var("var_687", dtype = "uint32", shape = (70,))#candidate|687|(70,)|var|uint32
call_686 = func_456_call(relay.reshape(var_687.astype('uint32'), [7, 1, 10]))
call_688 = func_456_call(relay.reshape(var_687.astype('uint32'), [7, 1, 10]))
output = relay.Tuple([bop_681,call_686,var_687,])
output2 = relay.Tuple([bop_681,call_688,var_687,])
func_690 = relay.Function([var_679,var_680,var_687,], output)
mod['func_690'] = func_690
mod = relay.transform.InferType()(mod)
mutated_mod['func_690'] = func_690
mutated_mod = relay.transform.InferType()(mutated_mod)
func_690_call = mutated_mod.get_global_var('func_690')
var_692 = relay.var("var_692", dtype = "uint64", shape = (16, 14, 4))#candidate|692|(16, 14, 4)|var|uint64
var_693 = relay.var("var_693", dtype = "uint64", shape = (16, 14, 4))#candidate|693|(16, 14, 4)|var|uint64
var_694 = relay.var("var_694", dtype = "uint32", shape = (70,))#candidate|694|(70,)|var|uint32
call_691 = func_690_call(var_692,var_693,var_694,)
output = call_691
func_695 = relay.Function([var_692,var_693,var_694,], output)
mutated_mod['func_695'] = func_695
mutated_mod = relay.transform.InferType()(mutated_mod)
var_784 = relay.var("var_784", dtype = "float32", shape = (8, 16))#candidate|784|(8, 16)|var|float32
uop_785 = relay.erf(var_784.astype('float32')) # shape=(8, 16)
func_690_call = mod.get_global_var('func_690')
func_695_call = mutated_mod.get_global_var('func_695')
const_797 = relay.const([10,10,1,-5,-8,-8,1,-6,9,9,-7,4,-8,-10,-3,-8,-8,-4,-4,-9,8,-3,-3,-10,-2,6,1,-3,-8,3,8,6,-10,7,1,-8,-3,-10,9,1,-10,3,8,-2,9,-10,7,-6,-8,4,-9,10,3,-10,-1,6,-7,3,-2,-2,2,-1,9,7,8,-7,-4,-3,-9,9,-4,-9,1,6,7,-8,1,-8,-7,-10,-8,4,-5,9,9,-2,-5,6,3,3,4,-8,1,7,-3,-2,3,-3,4,10,1,6,5,4,-6,7,-10,-4,1,8,-8,4,-6,-10,8,4,4,-5,-4,4,-10,1,-7,9,-8,-1,7,10,2,-6,9,-10,-9,-9,-8,6,-5,-5,2,10,3,8,9,-5,-5,-3,-10,7,-8,4,-3,-3,7,-3,-6,-3,-6,-2,9,10,-8,-10,4,10,8,-1,6,1,3,-4,-9,-1,8,-4,1,-2,-4,9,-4,3,3,-4,7,-2,-1,3,-5,-7,-8,-1,4,9,-10,10,-7,5,-5,9,-6,4,1,-7,2,1,-6,10,-10,2,7,-3,2,-4,-8,-3,-6,-10,-6,5,-3,-7,-1,-1,-6,-10,-4,5,2,7,4,4,6,-9,3,10,8,-6,-6,1,-9,-3,3,-9,9,7,-5,-3,3,3,6,3,-1,-5,6,-9,7,8,-3,-7,4,-8,-2,-9,-5,-2,-6,-4,-4,5,5,6,7,-3,2,3,-3,4,3,2,-6,8,-3,-8,-3,8,-7,1,-10,-4,-4,10,-9,-5,-8,2,-5,-3,-3,7,5,4,-2,8,9,6,-1,5,3,-4,-8,4,-7,2,-9,7,-4,8,8,-8,5,2,-2,-8,6,-5,-2,-8,7,10,10,-2,8,10,3,5,-4,8,4,1,1,6,7,2,-7,10,8,2,1,4,-4,5,-5,-5,10,3,-4,-3,-5,2,5,-9,-5,3,-5,-3,-5,8,-1,3,9,-1,4,-3,-8,1,9,10,-9,2,-9,6,3,-6,-6,-4,-6,9,10,9,9,3,7,1,-6,3,-8,-9,-2,-5,-5,-5,-5,-3,8,-5,3,2,3,8,-8,3,2,9,9,2,3,7,2,5,3,5,-9,-5,-4,-10,-6,2,-6,-1,3,9,1,-5,5,2,-1,-3,8,3,-3,-8,-7,-8,-9,8,-4,-9,-2,-7,4,6,-10,6,-6,-4,3,9,-10,4,6,1,-6,5,5,-6,5,6,10,-7,-2,-5,-1,-6,-1,-10,2,-9,4,-6,-7,-1,4,-10,-1,1,8,-10,-2,1,9,-4,-5,-9,8,1,8,10,9,-6,-8,4,7,-4,4,-4,-9,4,-3,6,-8,9,-6,10,10,6,5,4,7,2,-5,2,7,9,-9,-5,9,5,-4,3,-2,-2,2,-10,-3,-8,-9,2,8,-9,-4,6,-8,-3,7,-4,6,6,1,-6,-6,-3,-9,-2,6,-6,6,6,-6,-6,-4,9,-8,9,-1,-4,-1,4,1,7,-9,-8,8,1,-2,4,-9,5,8,-7,-2,7,-7,3,7,5,-6,5,8,7,-2,3,6,9,5,4,-4,-1,2,-10,6,6,-10,-8,-6,-8,8,10,-1,-9,-2,4,-5,-8,8,5,5,8,4,-4,10,9,-3,-1,7,-3,-4,6,1,-6,1,-7,-5,-2,10,1,9,-8,-10,-1,9,-5,-10,-4,-4,3,4,-4,2,1,-3,4,2,-8,-8,-7,-10,4,5,4,10,7,-5,4,6,-1,-6,2,-4,-10,9,3,-2,-1,5,-6,-3,9,-3,-5,-8,9,3,4,4,-4,-1,-2,4,-10,1,5,9,1,-1,-1,5,5,-3,-7,-2,10,8,6,7,2,-2,-3,-5,2,-1,4,-5,5,-9,5,-1,-3,-8,10,5,-5,-3,5,-3,3,-2,-9,8,-6,-6,8,-7,6,-10,-3,10,-1,6,-10,-4,2,-2,4,-7,-8,-5,-8,-7,-10,-3,-3,10,-6,1,7,9,-1,2,-4,10,-2,10,9,-6,-6,3,2,5,-2,-3,2,-8,-6,2,9,-2,7,1,-9,7,8,9,5,-7,10,8,4,7,-10,10,1,10,-5,-5,2,2,-6,-7,4,-10,5,-8,-7,9,-6,-7,-4,-4,-2,3,-5,-1,7,1,-3,8,2,7,5,-5,8,5,-8,8,1,1,8,8,1,9,-2,-2,-4,-4,-6,9,8,3,-4,6,-4,-3,1,10,-3,-8,7,-1,-8,2,-1,-7,5,-7,-2,-6,3,9,-3,8,7,10,5,-4,6,8,-5,8,-4,8,-9,-10,-6,-6,9,4,9,9,5,8,1,1,-10,7,6,-10,2,7,1,6,9,-8,-3,-4,-2,2,-8], dtype = "uint64")#candidate|797|(896,)|const|uint64
var_798 = relay.var("var_798", dtype = "uint32", shape = (70,))#candidate|798|(70,)|var|uint32
call_796 = relay.TupleGetItem(func_690_call(relay.reshape(const_797.astype('uint64'), [16, 14, 4]), relay.reshape(const_797.astype('uint64'), [16, 14, 4]), relay.reshape(var_798.astype('uint32'), [70,]), ), 1)
call_799 = relay.TupleGetItem(func_695_call(relay.reshape(const_797.astype('uint64'), [16, 14, 4]), relay.reshape(const_797.astype('uint64'), [16, 14, 4]), relay.reshape(var_798.astype('uint32'), [70,]), ), 1)
output = relay.Tuple([uop_785,call_796,const_797,var_798,])
output2 = relay.Tuple([uop_785,call_799,const_797,var_798,])
func_824 = relay.Function([var_784,var_798,], output)
mod['func_824'] = func_824
mod = relay.transform.InferType()(mod)
var_825 = relay.var("var_825", dtype = "float32", shape = (8, 16))#candidate|825|(8, 16)|var|float32
var_826 = relay.var("var_826", dtype = "uint32", shape = (70,))#candidate|826|(70,)|var|uint32
output = func_824(var_825,var_826,)
func_827 = relay.Function([var_825,var_826,], output)
mutated_mod['func_827'] = func_827
mutated_mod = relay.transform.InferType()(mutated_mod)
var_903 = relay.var("var_903", dtype = "int64", shape = (10, 14, 9))#candidate|903|(10, 14, 9)|var|int64
const_904 = relay.const([[[-10,8,6,-6,7,-9,4,9,2],[9,-3,-8,10,9,7,-4,10,8],[3,2,9,3,9,-5,3,-4,4],[-1,1,2,7,-6,-6,-3,-2,1],[6,7,5,6,-5,-6,-4,7,6],[-3,5,-10,-6,2,-7,9,6,-1],[-9,2,-7,5,3,7,1,-2,9],[-7,-6,5,1,-9,10,-1,6,5],[10,-7,1,-4,-3,-9,2,-1,5],[4,-10,7,2,10,-1,-3,4,8],[5,-10,-10,-5,4,-1,-2,9,7],[-3,-3,-8,8,5,-3,-7,-5,-9],[5,9,9,-2,-4,-2,-6,1,8],[2,-3,5,-2,-6,-1,-3,-10,8]],[[2,-8,-1,-9,-5,-6,10,-6,7],[-10,-6,-7,3,3,-2,-1,-1,1],[9,-10,-10,7,4,-2,-5,-1,9],[9,-10,3,3,6,-5,7,9,-10],[4,1,-9,1,5,6,-4,8,-7],[-3,7,6,6,-5,3,-6,-3,4],[-9,-7,-1,-10,9,-6,-9,9,-8],[-7,10,-1,-9,9,3,-3,10,-7],[-4,7,-7,2,-2,3,7,8,5],[-10,6,6,3,-2,-9,8,-9,1],[-8,3,5,3,9,-9,1,-7,-9],[6,2,8,8,9,1,-5,-2,-8],[-6,8,10,-8,-7,10,9,9,-6],[3,3,3,-1,-10,7,-9,-8,-8]],[[6,-3,-2,10,-9,-3,4,-10,9],[8,2,-2,-7,-3,1,7,-9,10],[-1,5,9,-6,-5,1,-10,3,-8],[-4,-9,2,-10,5,7,-5,8,-10],[-9,10,-3,-9,2,6,8,-5,-8],[-6,5,-10,-9,-3,-4,-3,-9,6],[-6,4,8,7,1,4,2,10,1],[2,-6,8,9,-4,6,10,-6,1],[-6,9,-2,-9,-2,2,2,5,2],[-7,-5,-9,2,5,4,1,6,-9],[2,3,-8,9,-2,7,8,-4,6],[5,3,-5,8,8,5,-2,-5,3],[1,-5,-6,6,-8,-8,4,-2,5],[-7,-3,-7,-2,5,6,-3,10,10]],[[10,-2,6,5,-5,-8,-6,5,10],[10,-3,-3,5,-3,-6,2,1,-6],[-4,-7,-10,9,-10,9,-8,-3,-6],[-9,-4,7,-7,6,3,-5,5,-3],[-6,2,9,-5,-10,8,-7,-6,-9],[-9,-2,-4,-8,-1,10,-1,8,-2],[7,-6,6,-3,-2,3,4,10,6],[-2,-5,-1,-6,-1,6,-3,-9,-9],[4,-9,3,-8,4,6,1,6,10],[1,2,2,3,10,-6,-8,-3,5],[-9,-4,10,-2,-7,-7,10,4,-7],[-7,-2,4,-7,8,-1,5,-5,-4],[-8,-6,-7,-5,2,-6,-6,1,1],[5,10,-6,-6,3,-10,8,3,7]],[[8,6,9,-9,8,-4,5,-7,-5],[-6,-5,-4,-5,-5,6,-8,-3,-4],[-8,-9,5,5,5,7,-6,10,-3],[8,-9,-6,-6,1,9,-6,-2,-3],[-10,-9,2,-4,-2,-2,1,2,-7],[-6,5,6,5,-2,7,-4,-6,10],[10,8,8,-6,2,-10,-8,-3,6],[-8,-1,7,-6,3,-5,-1,8,-6],[9,-9,2,1,-6,3,-6,-2,-1],[-5,2,-10,4,4,9,8,4,1],[7,-5,6,6,9,1,8,7,-5],[-9,-8,-8,-6,7,6,-5,-9,7],[-8,-9,10,7,5,8,-2,-6,-3],[-7,5,-9,3,-5,4,-8,-6,1]],[[7,3,-1,10,9,4,-4,-1,7],[1,3,2,9,-10,-7,2,9,3],[-8,3,-3,-9,10,-6,-7,-6,-3],[8,10,-9,-10,-10,6,-1,10,-2],[-3,-10,9,9,-2,-8,5,1,5],[10,-10,-6,-6,1,-3,7,-3,6],[-4,10,9,-3,4,-8,3,-4,-10],[9,7,2,-2,3,-7,-9,-5,-6],[-7,-9,-2,-9,8,-8,-4,-6,7],[-1,8,-6,5,7,6,-4,-4,-5],[-1,3,-8,10,10,-4,-6,7,1],[3,1,-5,5,10,-2,8,-9,-5],[-4,2,-10,10,-3,2,-10,-9,-4],[8,6,9,-4,3,7,-2,-4,-2]],[[3,2,9,-10,-10,-2,5,-2,-1],[-9,7,10,-2,5,-9,2,-1,5],[-2,-10,6,-5,-3,2,-9,1,-4],[9,3,4,3,3,-4,-5,-5,-7],[9,10,2,-8,-2,6,-9,-2,1],[6,3,7,10,-2,-8,-4,4,9],[-7,-4,7,4,6,-2,-3,-8,-8],[4,8,-2,8,1,1,5,-10,-8],[-10,5,-10,1,-7,-10,6,4,-1],[-10,2,8,-3,3,3,-2,-6,6],[-6,-9,-6,8,6,-7,8,-5,-9],[6,-7,7,2,2,-8,6,-7,-9],[-6,6,8,-9,9,9,-1,9,-7],[10,6,9,-2,10,-10,2,-5,-7]],[[2,-1,4,-10,-8,4,5,-5,6],[7,-7,-9,5,2,-2,2,9,-6],[7,7,-4,1,5,-2,-9,2,7],[4,3,-1,7,10,9,10,-1,-1],[9,8,-7,-8,-1,-6,-10,-10,6],[-9,-5,10,4,-1,-6,1,4,1],[2,-2,10,3,6,-4,-5,5,9],[-5,5,7,8,-9,9,-6,9,-6],[-3,10,2,-4,-6,-8,-4,9,1],[-5,6,-3,-5,-8,8,5,10,-5],[-7,9,5,10,2,-3,5,-6,-1],[6,10,10,5,-3,9,9,-4,1],[8,3,1,7,-3,7,-1,-9,6],[-3,7,7,-2,3,-7,-9,10,-8]],[[-7,6,-7,-5,-5,-1,8,-1,-8],[10,-5,9,-1,-8,10,1,1,7],[-10,6,9,-6,1,-1,-8,-10,7],[-6,8,9,-9,5,-10,8,7,5],[3,-4,-3,-3,7,5,-5,-4,4],[-2,6,3,-10,-5,-6,4,6,-4],[-2,-9,4,-6,-4,3,4,10,-3],[-5,7,9,-2,5,-10,6,-7,4],[8,10,8,9,9,5,6,4,-2],[7,5,-4,10,-6,5,-6,-9,5],[10,-1,-5,10,8,5,4,-4,5],[-3,-5,1,10,-5,6,8,5,-4],[8,4,-7,-4,2,-1,5,1,4],[2,-1,-4,-6,-2,2,3,-9,5]],[[-5,-8,-6,-3,2,3,-8,-1,1],[-6,8,9,-4,-9,7,-9,-3,-9],[-6,10,-6,8,-7,3,-6,6,-4],[3,7,-1,8,-7,10,1,-6,-6],[5,8,-4,-1,-7,4,2,-1,1],[-1,5,1,-4,1,-5,-4,-2,-2],[3,-7,-10,4,-8,1,9,10,2],[9,-6,-7,9,1,6,-8,-9,-9],[-3,1,10,-3,-3,-4,6,10,6],[-3,9,-6,7,3,-6,5,5,-5],[5,5,2,-3,-5,-10,-8,-5,5],[3,-3,10,-9,3,10,-1,7,-2],[-7,5,8,2,8,-5,7,7,-4],[-3,1,-7,5,5,-3,-9,2,2]]], dtype = "int64")#candidate|904|(10, 14, 9)|const|int64
bop_905 = relay.bitwise_and(var_903.astype('int64'), relay.reshape(const_904.astype('int64'), relay.shape_of(var_903))) # shape=(10, 14, 9)
output = relay.Tuple([bop_905,])
output2 = relay.Tuple([bop_905,])
func_910 = relay.Function([var_903,], output)
mod['func_910'] = func_910
mod = relay.transform.InferType()(mod)
var_911 = relay.var("var_911", dtype = "int64", shape = (10, 14, 9))#candidate|911|(10, 14, 9)|var|int64
output = func_910(var_911)
func_912 = relay.Function([var_911], output)
mutated_mod['func_912'] = func_912
mutated_mod = relay.transform.InferType()(mutated_mod)
var_923 = relay.var("var_923", dtype = "float32", shape = (10, 2, 16))#candidate|923|(10, 2, 16)|var|float32
uop_924 = relay.exp(var_923.astype('float32')) # shape=(10, 2, 16)
output = uop_924
output2 = uop_924
func_927 = relay.Function([var_923,], output)
mod['func_927'] = func_927
mod = relay.transform.InferType()(mod)
var_928 = relay.var("var_928", dtype = "float32", shape = (10, 2, 16))#candidate|928|(10, 2, 16)|var|float32
output = func_927(var_928)
func_929 = relay.Function([var_928], output)
mutated_mod['func_929'] = func_929
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1005 = relay.var("var_1005", dtype = "float64", shape = (7, 3, 1))#candidate|1005|(7, 3, 1)|var|float64
uop_1006 = relay.atan(var_1005.astype('float64')) # shape=(7, 3, 1)
uop_1011 = relay.sinh(uop_1006.astype('float64')) # shape=(7, 3, 1)
bop_1019 = relay.bitwise_or(uop_1011.astype('uint64'), relay.reshape(uop_1006.astype('uint64'), relay.shape_of(uop_1011))) # shape=(7, 3, 1)
output = bop_1019
output2 = bop_1019
func_1022 = relay.Function([var_1005,], output)
mod['func_1022'] = func_1022
mod = relay.transform.InferType()(mod)
var_1023 = relay.var("var_1023", dtype = "float64", shape = (7, 3, 1))#candidate|1023|(7, 3, 1)|var|float64
output = func_1022(var_1023)
func_1024 = relay.Function([var_1023], output)
mutated_mod['func_1024'] = func_1024
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1097 = relay.var("var_1097", dtype = "int64", shape = (4, 11, 15))#candidate|1097|(4, 11, 15)|var|int64
var_1098 = relay.var("var_1098", dtype = "int64", shape = (4, 11, 15))#candidate|1098|(4, 11, 15)|var|int64
bop_1099 = relay.add(var_1097.astype('int64'), relay.reshape(var_1098.astype('int64'), relay.shape_of(var_1097))) # shape=(4, 11, 15)
const_1103 = relay.const([[[6,-3,10,10,-2,-2,10,-1,-3,-9,-9,9,-1,4,6],[9,1,-10,-6,6,9,-4,7,5,6,1,4,-5,-3,-7],[6,-2,-10,2,5,3,6,-10,-3,-3,10,4,5,9,10],[-8,-1,-7,-5,6,7,-1,-9,5,7,-8,-1,-10,-6,6],[-4,2,7,8,-8,-9,6,-7,-2,-4,10,5,-8,10,4],[8,10,-5,1,8,-8,4,10,8,4,10,-5,7,-2,5],[-3,-5,-7,10,4,9,9,-7,-5,-9,-6,-4,8,4,10],[-9,6,-6,6,1,5,3,3,1,6,8,-2,5,-8,1],[10,-1,-4,9,2,-2,-10,-1,7,-1,-5,-5,5,-5,10],[-9,6,7,6,9,-6,6,-8,-8,-10,-7,10,-10,-3,6],[-2,4,-6,7,-6,9,-9,-7,4,3,-4,9,-4,9,-7]],[[-3,-1,-7,9,-8,-4,9,3,-2,9,1,8,9,8,-1],[2,-3,2,-1,-8,8,-9,-7,10,7,7,-5,7,-8,2],[9,-5,9,6,8,3,6,-4,-2,4,-6,-9,-7,4,3],[-5,2,-7,-7,4,-7,-3,7,-5,4,10,2,2,8,-5],[4,3,1,-8,3,6,-7,2,-8,4,-8,-1,-8,2,-1],[-6,8,-2,9,7,-9,3,-4,3,2,4,-6,2,10,-9],[-10,5,-2,9,6,-5,-1,-3,3,-4,3,-7,-3,-2,-1],[-3,6,1,6,1,-7,6,-5,2,-5,3,6,-9,-6,-3],[4,10,-5,-7,-2,-2,-5,7,-7,5,7,2,-5,2,3],[-10,1,-4,10,9,10,-1,8,-2,-8,7,-5,9,-1,5],[8,1,-5,8,-8,9,8,2,9,3,5,5,10,-1,-6]],[[-2,-2,-6,8,4,2,-6,3,-6,-6,-10,-8,10,-10,8],[-9,-2,3,-10,3,1,-5,-6,4,1,-1,-10,7,-7,-5],[6,-5,-7,-8,3,8,9,-10,-4,-4,-6,-5,4,-8,-2],[5,-7,8,-1,8,10,-8,1,-1,-4,-9,10,9,-7,-4],[-10,-9,-9,10,3,-6,7,-9,3,5,-7,-8,-8,10,3],[-8,-4,1,-2,-5,-2,8,-6,10,-7,7,-7,10,1,5],[-7,-9,8,6,1,-4,4,-4,9,10,-7,9,-3,3,2],[-9,9,-9,8,-6,7,-3,2,-3,-1,8,-9,4,-7,-7],[-3,5,4,8,9,2,5,-1,3,9,-7,2,3,10,-2],[-8,-3,6,7,9,7,-6,-7,1,-10,-5,-7,-3,-2,-10],[-9,-9,1,10,-1,-8,2,-3,10,2,4,7,4,-2,2]],[[-3,10,1,-9,-1,-2,1,2,5,-7,2,-4,-1,-8,5],[6,-8,9,-8,-4,9,6,2,-3,10,5,1,10,6,-6],[-7,-6,-9,-8,-5,5,-8,5,9,-8,8,-10,1,-3,-9],[7,-1,4,-9,-6,5,-8,4,-5,-3,-1,-6,-2,-4,-3],[3,-10,-4,8,-9,10,8,8,-3,-3,6,9,-7,-9,5],[-4,4,7,-2,-3,-7,-4,-3,7,3,-4,5,3,2,5],[-3,-8,-4,-9,7,-7,7,1,4,-7,7,-8,-3,-6,-2],[-4,9,6,-4,2,-6,-6,-10,2,5,3,-1,6,-1,-10],[-3,-9,-6,-10,7,2,10,-6,-6,-8,-10,-7,-1,8,7],[-6,2,-7,-10,1,-6,3,-4,10,-1,-3,9,-3,-4,4],[-9,-4,-6,3,7,-7,6,10,-9,10,-9,3,6,8,-9]]], dtype = "int64")#candidate|1103|(4, 11, 15)|const|int64
bop_1104 = relay.bitwise_or(var_1098.astype('int64'), relay.reshape(const_1103.astype('int64'), relay.shape_of(var_1098))) # shape=(4, 11, 15)
func_690_call = mod.get_global_var('func_690')
func_695_call = mutated_mod.get_global_var('func_695')
var_1120 = relay.var("var_1120", dtype = "uint64", shape = (896,))#candidate|1120|(896,)|var|uint64
const_1121 = relay.const([-2,-5,-5,-8,4,-7,-9,5,4,3,-10,6,9,4,-7,-2,-5,1,-4,6,2,8,-10,5,5,-3,8,2,7,-9,-2,-3,-2,4,-3,5,-4,7,3,10,-9,5,-4,7,3,-4,-10,2,1,-7,8,2,-4,8,2,-7,2,-10,-9,6,4,-8,8,4,8,6,3,2,10,5], dtype = "uint32")#candidate|1121|(70,)|const|uint32
call_1119 = relay.TupleGetItem(func_690_call(relay.reshape(var_1120.astype('uint64'), [16, 14, 4]), relay.reshape(var_1120.astype('uint64'), [16, 14, 4]), relay.reshape(const_1121.astype('uint32'), [70,]), ), 1)
call_1122 = relay.TupleGetItem(func_695_call(relay.reshape(var_1120.astype('uint64'), [16, 14, 4]), relay.reshape(var_1120.astype('uint64'), [16, 14, 4]), relay.reshape(const_1121.astype('uint32'), [70,]), ), 1)
output = relay.Tuple([bop_1099,bop_1104,call_1119,var_1120,const_1121,])
output2 = relay.Tuple([bop_1099,bop_1104,call_1122,var_1120,const_1121,])
func_1128 = relay.Function([var_1097,var_1098,var_1120,], output)
mod['func_1128'] = func_1128
mod = relay.transform.InferType()(mod)
var_1129 = relay.var("var_1129", dtype = "int64", shape = (4, 11, 15))#candidate|1129|(4, 11, 15)|var|int64
var_1130 = relay.var("var_1130", dtype = "int64", shape = (4, 11, 15))#candidate|1130|(4, 11, 15)|var|int64
var_1131 = relay.var("var_1131", dtype = "uint64", shape = (896,))#candidate|1131|(896,)|var|uint64
output = func_1128(var_1129,var_1130,var_1131,)
func_1132 = relay.Function([var_1129,var_1130,var_1131,], output)
mutated_mod['func_1132'] = func_1132
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1255 = relay.var("var_1255", dtype = "int32", shape = (6, 10, 15))#candidate|1255|(6, 10, 15)|var|int32
var_1256 = relay.var("var_1256", dtype = "int32", shape = (6, 10, 15))#candidate|1256|(6, 10, 15)|var|int32
bop_1257 = relay.maximum(var_1255.astype('int32'), relay.reshape(var_1256.astype('int32'), relay.shape_of(var_1255))) # shape=(6, 10, 15)
func_456_call = mod.get_global_var('func_456')
func_459_call = mutated_mod.get_global_var('func_459')
const_1274 = relay.const([[-4,-6,10,-9,-5],[10,-5,-1,-10,-10],[6,-2,5,-7,10],[8,4,6,3,-9],[-10,6,-5,2,-10],[4,-8,-2,6,5],[5,-10,9,-3,3],[3,-10,1,-4,9],[-5,-9,-9,7,-10],[-1,-6,-4,-9,9],[8,7,1,-1,3],[8,-3,3,7,9],[-2,4,3,7,6],[6,-8,-2,-3,3]], dtype = "uint32")#candidate|1274|(14, 5)|const|uint32
call_1273 = func_456_call(relay.reshape(const_1274.astype('uint32'), [7, 1, 10]))
call_1275 = func_456_call(relay.reshape(const_1274.astype('uint32'), [7, 1, 10]))
output = relay.Tuple([bop_1257,call_1273,const_1274,])
output2 = relay.Tuple([bop_1257,call_1275,const_1274,])
func_1286 = relay.Function([var_1255,var_1256,], output)
mod['func_1286'] = func_1286
mod = relay.transform.InferType()(mod)
var_1287 = relay.var("var_1287", dtype = "int32", shape = (6, 10, 15))#candidate|1287|(6, 10, 15)|var|int32
var_1288 = relay.var("var_1288", dtype = "int32", shape = (6, 10, 15))#candidate|1288|(6, 10, 15)|var|int32
output = func_1286(var_1287,var_1288,)
func_1289 = relay.Function([var_1287,var_1288,], output)
mutated_mod['func_1289'] = func_1289
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1505 = relay.var("var_1505", dtype = "int32", shape = (1, 12, 15))#candidate|1505|(1, 12, 15)|var|int32
var_1506 = relay.var("var_1506", dtype = "int32", shape = (6, 12, 15))#candidate|1506|(6, 12, 15)|var|int32
bop_1507 = relay.right_shift(var_1505.astype('int32'), var_1506.astype('int32')) # shape=(6, 12, 15)
func_1128_call = mod.get_global_var('func_1128')
func_1132_call = mutated_mod.get_global_var('func_1132')
const_1534 = relay.const([3,1,5,8,-9,10,-10,5,-5,10,-7,-1,8,6,-4,-5,10,-7,-9,-8,10,4,-1,8,6,-9,6,7,-7,10,-1,-8,-1,8,2,8,-4,-3,-3,-10,8,-1,-9,-8,3,-8,3,9,-1,-5,1,-6,-6,-9,-10,8,-8,2,-1,-4,10,-1,7,6,7,4,5,-4,-1,-1,-1,8,-10,-9,-5,-7,6,-6,8,-3,-3,4,7,8,10,-8,8,4,-8,-1,7,-6,6,6,-5,-10,7,6,-1,-3,-4,5,9,-10,-2,10,8,2,1,7,-8,2,-10,-1,-3,-3,-5,8,8,1,-8,-9,10,-8,1,4,-2,-7,7,3,-4,4,7,-5,10,6,8,6,-9,8,-10,9,3,4,6,7,-6,-1,-4,9,-2,-4,10,-10,-4,9,5,8,6,7,3,-3,-6,3,1,-6,7,-7,9,6,-10,-7,-2,2,-1,9,-4,3,7,1,-8,-2,6,1,-9,-7,3,3,-1,3,-7,-5,5,10,-4,9,-8,8,-4,-7,8,-1,10,-6,2,-4,-2,-9,-7,-8,-2,6,1,3,-10,8,6,9,-5,8,4,4,1,2,2,2,10,3,-9,-9,-9,-9,6,1,-2,-9,-1,2,-8,-3,-8,-6,10,-2,-8,-9,7,1,5,5,3,4,8,-7,4,-7,-4,1,-2,4,-3,6,3,5,9,7,-5,5,1,-8,-3,-5,9,10,10,-3,9,5,7,1,-10,-8,-1,8,7,7,4,7,-10,5,5,3,7,7,9,-10,8,6,2,-1,2,1,2,9,6,-1,2,-4,-3,-3,-9,-3,-2,6,3,-3,7,-10,1,-10,1,-10,5,-4,-5,3,1,-2,-3,6,-8,-10,2,-6,7,-4,7,-5,-7,3,9,7,1,2,-8,1,-7,2,3,6,4,-2,3,-5,6,4,5,-5,1,-2,8,-6,6,-6,-4,9,-2,8,8,-6,3,-2,-1,7,-6,2,4,-1,-4,9,9,5,-1,-7,-8,3,-2,4,-4,5,1,6,-5,-8,-3,-8,-7,4,-8,6,3,-9,-6,6,5,-2,1,4,4,-7,-8,-9,-8,4,-3,3,-4,1,-7,-2,10,-9,-1,-9,2,1,-10,9,-5,-5,-5,-6,-3,9,-6,2,-4,-9,3,-9,5,-7,4,7,10,10,2,-6,-3,-5,-5,-4,-8,-5,2,-8,-6,6,-2,9,-4,-9,3,1,10,4,5,-6,9,-5,-5,-10,7,-1,8,3,9,10,7,9,-1,5,-8,-10,2,10,8,10,-5,-8,-5,8,-3,5,2,-7,4,9,-3,-1,-6,-4,-10,-2,9,1,-1,7,9,-3,-7,-6,-10,-5,5,10,6,6,2,4,-9,7,-3,-3,-8,3,-7,-8,-5,-2,10,10,9,3,-5,5,1,-4,-8,-7,3,4,1,9,-7,-6,4,-5,1,6,-5,10,3,-10,-10,9,-9,5,9,7,6,4,-9,-5,-7,6,2,-5,7,7,-4,-3,3,4,4,7,3,2,-10,-2,-7,-6,2,3,-9,-9,9,4,1,-2,-9,5,-2,-6,3,9,6,-9,9,10,-4,-8,10,-5,-2,-6,-7,5,-9,4,-8,-1,8,-5,-4,4,-3,-3,6,3,-6,-9,1,4,6,3,-1,-10,-6,8,9,10,-4,-4,10,8,-8,10,-4,1,-4,-6,1,-6,1,7,-5,10,7,-2,3,2,1,-3,8,-3,-10,-7,-4,-8], dtype = "int64")#candidate|1534|(660,)|const|int64
var_1535 = relay.var("var_1535", dtype = "uint64", shape = (896,))#candidate|1535|(896,)|var|uint64
call_1533 = relay.TupleGetItem(func_1128_call(relay.reshape(const_1534.astype('int64'), [4, 11, 15]), relay.reshape(const_1534.astype('int64'), [4, 11, 15]), relay.reshape(var_1535.astype('uint64'), [896,]), ), 0)
call_1536 = relay.TupleGetItem(func_1132_call(relay.reshape(const_1534.astype('int64'), [4, 11, 15]), relay.reshape(const_1534.astype('int64'), [4, 11, 15]), relay.reshape(var_1535.astype('uint64'), [896,]), ), 0)
func_1128_call = mod.get_global_var('func_1128')
func_1132_call = mutated_mod.get_global_var('func_1132')
call_1537 = relay.TupleGetItem(func_1128_call(relay.reshape(const_1534.astype('int64'), [4, 11, 15]), relay.reshape(const_1534.astype('int64'), [4, 11, 15]), relay.reshape(var_1535.astype('uint64'), [896,]), ), 0)
call_1538 = relay.TupleGetItem(func_1132_call(relay.reshape(const_1534.astype('int64'), [4, 11, 15]), relay.reshape(const_1534.astype('int64'), [4, 11, 15]), relay.reshape(var_1535.astype('uint64'), [896,]), ), 0)
func_690_call = mod.get_global_var('func_690')
func_695_call = mutated_mod.get_global_var('func_695')
var_1542 = relay.var("var_1542", dtype = "uint32", shape = (7, 10))#candidate|1542|(7, 10)|var|uint32
call_1541 = relay.TupleGetItem(func_690_call(relay.reshape(var_1535.astype('uint64'), [16, 14, 4]), relay.reshape(var_1535.astype('uint64'), [16, 14, 4]), relay.reshape(var_1542.astype('uint32'), [70,]), ), 1)
call_1543 = relay.TupleGetItem(func_695_call(relay.reshape(var_1535.astype('uint64'), [16, 14, 4]), relay.reshape(var_1535.astype('uint64'), [16, 14, 4]), relay.reshape(var_1542.astype('uint32'), [70,]), ), 1)
func_1128_call = mod.get_global_var('func_1128')
func_1132_call = mutated_mod.get_global_var('func_1132')
call_1545 = relay.TupleGetItem(func_1128_call(relay.reshape(call_1533.astype('int64'), [4, 11, 15]), relay.reshape(call_1537.astype('int64'), [4, 11, 15]), relay.reshape(var_1535.astype('uint64'), [896,]), ), 0)
call_1546 = relay.TupleGetItem(func_1132_call(relay.reshape(call_1533.astype('int64'), [4, 11, 15]), relay.reshape(call_1537.astype('int64'), [4, 11, 15]), relay.reshape(var_1535.astype('uint64'), [896,]), ), 0)
uop_1552 = relay.sqrt(call_1545.astype('float32')) # shape=(4, 11, 15)
uop_1554 = relay.sqrt(call_1546.astype('float32')) # shape=(4, 11, 15)
func_927_call = mod.get_global_var('func_927')
func_929_call = mutated_mod.get_global_var('func_929')
const_1559 = relay.const([9.915376,-9.807404,2.398821,-4.817805,-5.260966,1.554890,-2.499294,-0.152175,-3.815354,-2.555275,-4.521012,-5.353953,5.155642,4.498296,-6.651173,2.169226,3.479100,5.489700,3.506825,6.231609,4.825129,6.615833,-9.802514,-3.784577,-1.063622,0.304373,-1.689694,-9.834248,-2.432072,-6.644277,-4.923156,-9.509974,-9.296310,-9.465535,1.688065,6.301112,-3.966507,6.800122,-7.836137,-8.124025,-9.135295,-4.449511,6.131347,4.557443,-1.766373,-7.854865,3.681948,-1.755091,-9.933016,-9.128881,-2.061475,5.053092,-4.750702,-8.618426,-6.028075,8.199239,-8.094084,5.861411,-7.027847,1.928216,5.629635,-5.676087,-5.897671,-4.379283,6.444076,2.112694,-6.947179,0.397119,3.836334,-2.167596,-9.492430,-3.112141,8.119276,-9.629144,-6.757931,-4.304745,-8.077907,4.232620,-2.027651,2.376805,-3.575022,3.736615,6.384979,4.118948,-4.804284,6.167353,6.332549,1.796245,4.966427,-2.584448,7.359579,6.582628,1.193276,5.877799,-4.863621,-0.047953,6.060535,-7.832967,-2.981620,0.034282,8.992523,4.827487,-6.601016,7.616236,-7.433293,-1.705445,-6.663706,3.230773,-0.016095,0.379548,-3.745925,2.150145,-9.361246,-3.181097,1.528831,3.456503,-5.383783,3.169402,-4.990201,6.877444,-3.411239,-3.972405,7.059717,4.764547,-3.748009,1.952988,-2.914964,-2.772935,-4.772145,1.791144,-6.688321,-1.344765,9.335843,-9.111092,-1.811272,-3.771228,8.258386,6.042687,1.791608,-0.821641,-4.631111,-3.338371,-1.987636,2.660550,2.298834,-1.399698,1.825056,4.237064,-0.188624,-9.570033,3.181885,5.806677,-2.134210,0.366412,8.313767,4.627047,0.997320,-6.390969,9.070389,-4.202127,-3.003465,-3.685492,4.666277,-5.150426,4.420764,-8.662349,-2.058359,3.608843,8.651332,-7.272059,-1.603814,-6.970317,1.513002,3.797645,-6.974677,1.582942,-1.511994,-8.353886,2.666165,5.256328,-3.695135,3.209096,-0.224167,8.897290,-3.553711,-4.184743,9.210212,-8.466732,-1.059083,5.818816,-6.965473,3.082199,7.364324,-1.745551,1.610903,3.957851,-7.360496,-4.248540,-6.728796,-1.332164,8.508586,8.995468,3.557674,9.287968,-2.826730,-1.821165,8.069459,4.570048,7.357562,-6.608181,-1.132652,-5.356283,-2.331792,7.864364,-9.753453,2.299546,-8.991341,4.394395,3.698803,5.022052,4.933024,-4.810677,-5.114267,8.338583,7.534160,-9.371966,-2.142853,-4.400400,4.080173,5.710669,6.547701,9.035455,2.946669,6.243614,2.561355,-9.379527,-0.914145,9.314127,4.047435,0.180268,-0.340900,-9.508410,-1.737198,-6.420526,-7.865873,-6.044225,-9.676452,6.444770,-6.962858,-1.004885,-9.324769,-1.498924,1.235995,2.586757,5.924708,-5.764688,-2.498947,-1.248682,4.692821,-7.261370,-2.977483,-1.282134,-4.360565,-7.894152,-5.882561,-2.233406,-5.222661,-0.388238,-5.928782,-8.566024,-0.955767,-7.359806,2.192541,1.521337,8.125727,-4.743533,-3.500536,-8.151255,-7.060090,2.891438,-2.975578,5.972225,0.203245,-2.114813,5.040365,2.514457,0.032320,-3.849971,-1.593324,-2.943250,4.052705,4.285143,7.746924,-5.125324,-4.344004,-9.973480,0.528770,3.112463,8.883358,0.920301,-5.047901,-1.396641,-3.085239,-2.769366,1.029374,-2.450786,1.761867,-6.326439,3.808644,2.251286,4.307410,-5.942509,0.492298,0.991614,-2.577499,-3.034064,2.797482,-1.176391,6.737874,-6.415167], dtype = "float32")#candidate|1559|(320,)|const|float32
call_1558 = func_927_call(relay.reshape(const_1559.astype('float32'), [10, 2, 16]))
call_1560 = func_927_call(relay.reshape(const_1559.astype('float32'), [10, 2, 16]))
func_456_call = mod.get_global_var('func_456')
func_459_call = mutated_mod.get_global_var('func_459')
call_1565 = func_456_call(relay.reshape(var_1542.astype('uint32'), [7, 1, 10]))
call_1566 = func_456_call(relay.reshape(var_1542.astype('uint32'), [7, 1, 10]))
output = relay.Tuple([bop_1507,call_1533,const_1534,var_1535,call_1537,call_1541,var_1542,uop_1552,call_1558,const_1559,call_1565,])
output2 = relay.Tuple([bop_1507,call_1536,const_1534,var_1535,call_1538,call_1543,var_1542,uop_1554,call_1560,const_1559,call_1566,])
func_1580 = relay.Function([var_1505,var_1506,var_1535,var_1542,], output)
mod['func_1580'] = func_1580
mod = relay.transform.InferType()(mod)
mutated_mod['func_1580'] = func_1580
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1580_call = mutated_mod.get_global_var('func_1580')
var_1582 = relay.var("var_1582", dtype = "int32", shape = (1, 12, 15))#candidate|1582|(1, 12, 15)|var|int32
var_1583 = relay.var("var_1583", dtype = "int32", shape = (6, 12, 15))#candidate|1583|(6, 12, 15)|var|int32
var_1584 = relay.var("var_1584", dtype = "uint64", shape = (896,))#candidate|1584|(896,)|var|uint64
var_1585 = relay.var("var_1585", dtype = "uint32", shape = (7, 10))#candidate|1585|(7, 10)|var|uint32
call_1581 = func_1580_call(var_1582,var_1583,var_1584,var_1585,)
output = call_1581
func_1586 = relay.Function([var_1582,var_1583,var_1584,var_1585,], output)
mutated_mod['func_1586'] = func_1586
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1710 = relay.var("var_1710", dtype = "float64", shape = (9, 12, 10))#candidate|1710|(9, 12, 10)|var|float64
var_1711 = relay.var("var_1711", dtype = "float64", shape = (9, 12, 10))#candidate|1711|(9, 12, 10)|var|float64
bop_1712 = relay.floor_divide(var_1710.astype('float64'), relay.reshape(var_1711.astype('float64'), relay.shape_of(var_1710))) # shape=(9, 12, 10)
output = relay.Tuple([bop_1712,])
output2 = relay.Tuple([bop_1712,])
func_1719 = relay.Function([var_1710,var_1711,], output)
mod['func_1719'] = func_1719
mod = relay.transform.InferType()(mod)
mutated_mod['func_1719'] = func_1719
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1719_call = mutated_mod.get_global_var('func_1719')
var_1721 = relay.var("var_1721", dtype = "float64", shape = (9, 12, 10))#candidate|1721|(9, 12, 10)|var|float64
var_1722 = relay.var("var_1722", dtype = "float64", shape = (9, 12, 10))#candidate|1722|(9, 12, 10)|var|float64
call_1720 = func_1719_call(var_1721,var_1722,)
output = call_1720
func_1723 = relay.Function([var_1721,var_1722,], output)
mutated_mod['func_1723'] = func_1723
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1725 = relay.const([[[True,False,False,False,False,False,True,False,True,True,False,True,False,True,False],[False,True,False,True,False,False,False,False,True,False,False,False,True,False,True],[True,False,True,False,False,True,False,True,True,True,False,False,True,False,True],[True,False,True,True,True,True,True,True,True,True,True,True,True,True,True],[False,False,True,True,False,True,False,False,False,False,False,True,False,True,True],[True,False,False,False,False,True,True,True,True,False,False,False,True,False,True],[True,False,False,False,False,False,False,False,True,False,False,True,True,False,False],[True,False,False,True,False,False,False,False,False,True,False,False,False,False,False],[True,True,True,True,True,True,False,True,True,True,False,False,False,True,False],[False,False,False,False,True,True,True,False,True,True,True,True,True,True,True],[False,True,False,True,False,False,False,False,True,True,True,True,True,True,True]],[[False,True,True,False,False,True,True,True,True,False,False,False,False,True,False],[True,True,True,False,False,True,False,False,False,True,False,True,True,True,True],[False,True,False,True,False,False,False,True,True,True,False,True,False,False,True],[False,True,False,True,True,True,False,True,True,False,True,True,False,False,True],[True,False,False,True,True,False,False,False,False,True,True,False,True,True,False],[False,True,True,False,False,True,True,True,False,True,True,True,False,True,True],[True,False,True,False,False,True,False,False,True,False,True,False,False,False,False],[False,False,True,False,True,False,True,False,True,True,True,False,True,False,False],[False,True,False,False,True,False,True,False,False,False,False,False,False,True,False],[False,True,True,False,True,False,False,False,False,True,False,False,True,True,False],[True,True,True,False,True,True,False,False,True,True,False,True,True,True,False]],[[True,True,False,False,True,True,False,True,False,True,False,False,True,False,True],[True,True,False,False,True,False,True,False,False,False,True,True,False,False,False],[False,True,True,False,False,True,False,False,False,False,True,True,False,False,True],[True,True,False,True,False,False,True,True,False,False,False,True,True,False,True],[True,False,False,False,True,False,True,True,True,False,True,False,True,True,True],[False,False,False,False,True,False,False,True,False,False,True,False,True,False,False],[False,True,False,True,True,True,True,True,False,False,True,True,True,False,False],[False,False,False,False,False,False,True,True,True,True,True,False,True,True,False],[True,True,True,True,False,False,True,False,True,True,False,False,True,True,False],[True,True,False,False,False,True,False,True,False,True,False,True,True,True,False],[True,False,False,False,True,False,False,False,False,False,False,True,False,True,False]],[[True,False,False,True,False,False,False,False,True,False,True,True,False,False,False],[False,True,False,False,True,True,True,False,False,True,False,False,False,False,True],[True,True,True,True,True,False,True,True,False,False,False,False,True,False,False],[True,False,False,True,True,True,False,False,True,False,True,True,False,False,False],[True,True,True,True,False,False,True,True,False,True,True,False,True,False,False],[False,True,False,False,False,True,True,False,True,True,True,True,False,True,True],[False,True,False,False,False,False,False,True,True,False,False,False,False,False,False],[False,False,True,True,False,True,False,True,True,False,False,False,True,True,False],[False,True,True,False,True,True,False,False,False,True,False,False,True,True,False],[True,True,False,False,False,False,True,True,False,False,True,False,True,False,True],[True,False,True,False,False,False,True,False,False,True,True,True,True,False,False]],[[False,True,True,False,True,False,True,False,True,True,False,False,True,True,False],[True,False,False,False,False,False,False,True,False,True,False,True,False,False,True],[False,False,False,True,False,True,True,True,True,False,False,True,False,False,True],[False,True,True,False,True,False,False,True,True,False,False,False,True,False,False],[False,False,False,False,False,False,True,True,False,False,False,False,False,False,False],[True,True,True,False,True,False,False,False,False,False,False,False,False,False,True],[False,False,True,False,True,True,False,False,True,False,True,True,True,True,True],[True,False,False,True,False,False,True,True,False,True,True,False,False,True,False],[True,True,True,False,True,False,False,True,False,True,False,True,False,True,False],[True,False,False,False,True,True,False,True,False,False,False,True,False,False,False],[True,True,True,False,False,False,False,False,True,False,True,True,False,True,False]],[[False,False,True,True,False,False,False,False,True,False,False,False,True,True,False],[True,False,False,False,False,False,False,False,False,True,False,True,True,False,False],[True,True,False,False,False,True,True,False,True,False,False,False,False,True,True],[True,False,True,True,False,True,True,False,True,True,True,True,False,False,False],[False,False,True,False,False,True,True,True,True,True,False,True,True,False,False],[False,True,False,True,False,False,False,True,False,True,False,True,False,False,False],[False,False,False,True,True,False,False,False,False,True,True,False,False,False,False],[False,False,False,False,True,False,False,True,False,False,False,False,False,True,True],[False,True,True,False,True,False,False,True,True,False,True,False,False,True,True],[True,False,True,True,False,True,True,True,False,True,True,True,False,True,False],[True,True,True,False,True,False,True,False,False,False,False,True,False,True,False]],[[True,False,False,True,True,True,False,False,False,False,False,True,True,False,True],[True,True,False,True,True,False,True,False,False,True,False,False,False,True,True],[True,False,True,True,True,False,False,True,True,False,False,True,False,True,True],[True,True,False,True,False,True,True,True,False,True,True,False,False,True,True],[True,False,False,True,False,True,True,False,True,False,True,True,True,True,False],[False,False,True,False,True,True,False,True,True,False,False,False,False,False,True],[False,False,False,False,True,False,True,False,False,False,True,True,True,False,False],[False,True,False,True,True,False,True,True,True,False,True,True,False,False,False],[True,False,False,True,False,True,True,True,True,False,False,False,True,True,True],[False,True,False,False,True,True,False,False,True,True,False,False,True,False,False],[True,True,False,True,True,False,False,False,False,True,False,False,False,False,True]],[[True,False,True,True,False,False,False,True,False,True,False,False,False,True,False],[False,False,True,True,True,False,True,True,True,True,True,True,True,True,True],[True,False,True,False,True,False,False,True,True,False,True,True,False,True,True],[False,True,True,True,False,True,False,False,False,True,True,True,False,True,False],[False,False,False,True,False,True,True,False,True,False,False,False,False,False,True],[True,False,False,False,True,True,True,True,True,False,False,False,True,True,True],[False,True,True,False,False,True,False,False,True,True,False,True,True,False,True],[False,True,True,False,False,True,True,True,False,False,True,True,True,True,False],[False,True,True,False,True,True,True,True,True,True,False,False,False,True,False],[False,True,False,True,False,False,False,True,True,True,False,True,False,True,False],[False,True,True,True,True,False,False,True,False,False,False,False,False,False,False]]], dtype = "bool")#candidate|1725|(8, 11, 15)|const|bool
var_1726 = relay.var("var_1726", dtype = "bool", shape = (8, 11, 15))#candidate|1726|(8, 11, 15)|var|bool
bop_1727 = relay.logical_or(const_1725.astype('bool'), relay.reshape(var_1726.astype('bool'), relay.shape_of(const_1725))) # shape=(8, 11, 15)
func_456_call = mod.get_global_var('func_456')
func_459_call = mutated_mod.get_global_var('func_459')
var_1734 = relay.var("var_1734", dtype = "uint32", shape = (70,))#candidate|1734|(70,)|var|uint32
call_1733 = func_456_call(relay.reshape(var_1734.astype('uint32'), [7, 1, 10]))
call_1735 = func_456_call(relay.reshape(var_1734.astype('uint32'), [7, 1, 10]))
output = relay.Tuple([bop_1727,call_1733,var_1734,])
output2 = relay.Tuple([bop_1727,call_1735,var_1734,])
func_1745 = relay.Function([var_1726,var_1734,], output)
mod['func_1745'] = func_1745
mod = relay.transform.InferType()(mod)
mutated_mod['func_1745'] = func_1745
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1745_call = mutated_mod.get_global_var('func_1745')
var_1747 = relay.var("var_1747", dtype = "bool", shape = (8, 11, 15))#candidate|1747|(8, 11, 15)|var|bool
var_1748 = relay.var("var_1748", dtype = "uint32", shape = (70,))#candidate|1748|(70,)|var|uint32
call_1746 = func_1745_call(var_1747,var_1748,)
output = call_1746
func_1749 = relay.Function([var_1747,var_1748,], output)
mutated_mod['func_1749'] = func_1749
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1925 = relay.var("var_1925", dtype = "bool", shape = (16, 8, 3))#candidate|1925|(16, 8, 3)|var|bool
var_1926 = relay.var("var_1926", dtype = "bool", shape = (16, 8, 3))#candidate|1926|(16, 8, 3)|var|bool
bop_1927 = relay.logical_or(var_1925.astype('bool'), relay.reshape(var_1926.astype('bool'), relay.shape_of(var_1925))) # shape=(16, 8, 3)
func_1580_call = mod.get_global_var('func_1580')
func_1586_call = mutated_mod.get_global_var('func_1586')
var_1936 = relay.var("var_1936", dtype = "int32", shape = (180,))#candidate|1936|(180,)|var|int32
var_1937 = relay.var("var_1937", dtype = "int32", shape = (1080,))#candidate|1937|(1080,)|var|int32
const_1938 = relay.const([1,-4,8,4,-2,-8,5,6,8,-4,9,7,9,9,-5,6,4,-5,-7,10,8,-4,1,-4,4,-7,-4,-8,10,-8,6,3,2,-6,6,10,1,-7,-6,3,-1,-10,-5,-7,8,9,9,-7,7,4,7,-7,10,3,7,3,-4,-2,-3,-3,-6,6,2,8,7,5,8,2,-8,-3,1,-4,2,6,-6,-6,-1,10,8,-7,2,8,-5,-9,5,9,-9,-3,-10,-6,-7,-9,-5,-2,-8,7,-10,-9,5,-10,-9,8,-4,9,-9,-2,-7,5,-1,6,-5,-7,-6,-9,-4,3,10,1,2,1,5,8,-4,4,1,5,1,-10,-10,-9,-2,8,-4,7,9,7,-1,3,-9,3,5,5,-9,4,-8,4,5,-1,2,-5,5,-4,9,4,-4,-8,-4,-6,2,4,5,7,1,9,5,4,-3,6,6,10,6,9,-4,3,-5,3,7,9,7,9,9,-2,2,6,10,5,7,8,-9,7,-9,5,10,2,-2,-1,-6,7,3,-3,-9,-8,2,-8,-8,8,-5,1,-9,-7,6,5,-1,8,-6,-4,9,3,-10,6,-8,-5,-9,2,-1,-10,7,9,-10,9,-9,-10,6,2,6,4,-2,9,-3,-9,8,-1,7,-10,-8,2,1,-6,7,3,-5,9,3,-9,7,-3,9,1,-6,4,1,1,-10,-10,-6,4,9,-9,1,1,7,-4,-9,-4,-9,9,4,1,7,-3,-4,4,-10,6,-2,9,2,-6,10,6,-8,-9,-4,-8,-4,4,10,1,-1,-1,-3,-2,4,4,8,3,-4,2,-5,-9,-3,-6,8,-5,4,2,6,2,2,6,-7,-9,3,1,2,-6,-10,10,-2,9,-8,-5,4,4,5,-9,-1,5,10,4,5,-8,6,3,2,-4,-2,5,-8,6,-3,8,-3,-9,-1,6,-3,-1,2,-7,-7,-5,1,6,2,-5,-7,8,9,7,-8,-6,-9,2,-2,-8,-1,9,-4,5,9,1,-4,9,4,-5,-1,5,-9,-3,-7,1,5,-4,-7,5,1,-3,4,-10,8,-1,6,8,7,6,2,6,9,6,-8,-3,8,-6,8,1,9,2,1,1,-1,2,6,9,-7,-1,-8,6,10,8,-7,-3,-2,6,-7,1,-5,9,2,-7,5,-6,4,-8,-5,4,5,2,2,-1,4,7,5,-3,6,-6,9,3,-7,2,7,-5,1,10,-7,2,-2,-1,5,-4,3,3,3,9,-8,1,5,10,5,-1,4,4,-4,-3,-8,-1,8,-4,1,10,-4,-9,-8,7,2,6,3,9,4,6,10,4,3,-8,3,8,-8,-8,-5,-10,3,10,-7,-3,3,-4,1,9,-7,-2,5,-2,4,-1,-5,5,-8,-7,-6,-7,-2,-9,8,8,-7,10,10,-6,9,5,-10,-5,-5,-5,-3,-9,-3,9,-10,-9,-9,10,-10,-4,-8,5,9,-8,2,-7,-6,-1,7,-4,-9,6,3,-9,-6,2,-2,-2,8,-5,-3,-7,-1,10,2,-6,9,1,2,3,-3,-10,1,-5,-1,-1,-5,3,-1,-5,-9,4,-7,-7,4,-4,6,-1,-7,-8,-9,1,9,9,9,3,-8,-5,3,-1,4,4,-1,-9,-3,7,7,-5,3,6,-9,9,5,10,6,5,-9,1,5,-10,-6,8,6,10,7,-1,-5,4,4,10,-7,1,-3,8,4,-6,-7,-6,10,-4,1,5,-8,10,5,4,-4,-8,7,6,-5,4,9,-9,-3,9,-10,4,3,10,5,-10,8,5,-5,9,-3,6,-10,-2,7,10,6,-5,-1,9,-8,-2,-10,-4,-8,-6,5,-5,-6,9,-8,1,7,5,5,-2,4,1,-3,-8,7,3,6,6,-5,-5,8,-9,6,-10,9,-3,-8,-6,9,-1,9,-8,-10,-9,3,-9,2,5,3,10,-7,-4,7,-5,5,-3,-8,9,7,-2,-2,9,-1,3,-10,-4,5,-4,-8,-9,3,-7,-4,8,2,10,-10,-9,5,-5,-4,6,6,2,-6,-9,4,9,-10,-9,-6,-10,2,-9,1,6,2,-5,-9,-4,-9,-6,-9,-2,2,5,2,6,5,1,-9,1,6,-2,2,-1,-1,3,2,8,7,-3,9,3,5,9,-10,7,-4,-2,-7,7,-10,5,-8,-7,8,-5,9,2,1,-10,-2,8,6,-2,5,-10,-4,8,-9,10,-4,8,-1,7,-4,3,-4,1,1,4,5,-2,8,-4,4,8,-8,-3,-7,-3,7,-6,-6,-4,10,-2,1,-7,-3,-8,4,-7,2,-3,2,1,-1,2,-2,6,-4,9,2,6,7,-4,-2,3,-3,-5,4,4,-5,-3,-5,-10,-7,6], dtype = "uint64")#candidate|1938|(896,)|const|uint64
const_1939 = relay.const([[-1,-10,-7,-5,-6],[8,-5,7,-8,5],[2,7,-1,9,-8],[-9,7,-10,-4,9],[-7,3,1,4,-6],[7,2,8,-9,-7],[-7,8,6,10,-2],[-1,5,-2,2,8],[-5,-6,9,4,2],[-4,6,2,-9,-3],[3,-9,5,-7,-7],[7,-9,3,-8,3],[6,8,9,-5,4],[9,-9,-8,-10,-3]], dtype = "uint32")#candidate|1939|(14, 5)|const|uint32
call_1935 = relay.TupleGetItem(func_1580_call(relay.reshape(var_1936.astype('int32'), [1, 12, 15]), relay.reshape(var_1937.astype('int32'), [6, 12, 15]), relay.reshape(const_1938.astype('uint64'), [896,]), relay.reshape(const_1939.astype('uint32'), [7, 10]), ), 7)
call_1940 = relay.TupleGetItem(func_1586_call(relay.reshape(var_1936.astype('int32'), [1, 12, 15]), relay.reshape(var_1937.astype('int32'), [6, 12, 15]), relay.reshape(const_1938.astype('uint64'), [896,]), relay.reshape(const_1939.astype('uint32'), [7, 10]), ), 7)
bop_1962 = relay.left_shift(var_1925.astype('uint32'), relay.reshape(bop_1927.astype('uint32'), relay.shape_of(var_1925))) # shape=(16, 8, 3)
func_1128_call = mod.get_global_var('func_1128')
func_1132_call = mutated_mod.get_global_var('func_1132')
call_1965 = relay.TupleGetItem(func_1128_call(relay.reshape(call_1935.astype('int64'), [4, 11, 15]), relay.reshape(call_1935.astype('int64'), [4, 11, 15]), relay.reshape(const_1938.astype('uint64'), [896,]), ), 4)
call_1966 = relay.TupleGetItem(func_1132_call(relay.reshape(call_1935.astype('int64'), [4, 11, 15]), relay.reshape(call_1935.astype('int64'), [4, 11, 15]), relay.reshape(const_1938.astype('uint64'), [896,]), ), 4)
const_2018 = relay.const([[[-2,-4,-7],[10,10,-1],[-9,-4,-1],[-9,10,3],[-9,4,8],[3,7,6],[2,5,-7],[6,7,4]],[[-6,10,4],[-5,4,8],[1,1,-9],[-2,-6,-2],[-7,6,-8],[-1,5,2],[7,-2,-7],[2,-4,-6]],[[1,-5,-6],[9,-7,5],[-5,-10,10],[-10,9,7],[-6,2,3],[4,-5,-2],[-8,-2,5],[-10,8,3]],[[-4,-4,-6],[-9,-1,4],[-8,-9,-7],[-3,1,2],[5,-6,-4],[10,1,10],[-6,-10,9],[-2,-2,1]],[[-1,8,10],[-7,2,7],[-2,3,-10],[3,-4,-4],[6,-2,-6],[-2,9,-10],[-10,5,10],[-7,8,8]],[[-6,5,-3],[-5,-4,9],[-1,-8,1],[-1,-5,-2],[-8,-9,-10],[6,5,8],[-10,-7,1],[8,-9,4]],[[6,-8,2],[8,-8,6],[-4,-7,-4],[7,7,2],[-3,10,7],[-1,-9,-6],[10,1,-10],[7,-1,-3]],[[9,-3,-5],[2,5,10],[-6,-7,-10],[6,-6,10],[-7,-8,-3],[-3,10,-7],[-1,10,3],[-10,-1,-3]],[[-9,-2,9],[-10,1,5],[6,6,-6],[-10,-4,-2],[2,-7,8],[-7,1,1],[3,8,-9],[8,1,-3]],[[9,-3,-6],[1,7,-3],[9,4,-1],[-2,6,8],[3,3,2],[-2,-1,-5],[1,7,5],[3,-1,-4]],[[1,7,-7],[7,1,-5],[-7,-3,1],[-7,5,10],[-7,-3,-1],[-3,4,2],[-4,-1,-10],[-7,3,-7]],[[-9,7,-10],[3,-2,-8],[-3,5,-10],[9,5,-9],[6,4,-8],[-4,-5,1],[9,-5,-10],[6,-1,-5]],[[8,-4,-3],[10,3,-9],[-4,9,5],[5,4,9],[-2,-1,5],[-5,-9,-8],[4,-4,-1],[-9,7,4]],[[-8,7,10],[9,-10,4],[-6,8,8],[10,5,10],[-6,-3,-6],[6,-8,5],[-1,-10,5],[-8,-3,-6]],[[2,4,7],[-5,4,7],[-5,-2,-8],[-10,1,1],[4,-7,-4],[9,-9,5],[-8,1,8],[-9,-1,-5]],[[10,-7,7],[-9,5,-9],[8,-7,10],[3,4,-9],[-1,3,-1],[-10,-6,-4],[-5,6,-8],[1,3,-5]]], dtype = "uint32")#candidate|2018|(16, 8, 3)|const|uint32
bop_2019 = relay.right_shift(bop_1962.astype('uint8'), relay.reshape(const_2018.astype('uint8'), relay.shape_of(bop_1962))) # shape=(16, 8, 3)
output = relay.Tuple([call_1935,var_1936,var_1937,const_1938,const_1939,call_1965,bop_2019,])
output2 = relay.Tuple([call_1940,var_1936,var_1937,const_1938,const_1939,call_1966,bop_2019,])
func_2041 = relay.Function([var_1925,var_1926,var_1936,var_1937,], output)
mod['func_2041'] = func_2041
mod = relay.transform.InferType()(mod)
var_2042 = relay.var("var_2042", dtype = "bool", shape = (16, 8, 3))#candidate|2042|(16, 8, 3)|var|bool
var_2043 = relay.var("var_2043", dtype = "bool", shape = (16, 8, 3))#candidate|2043|(16, 8, 3)|var|bool
var_2044 = relay.var("var_2044", dtype = "int32", shape = (180,))#candidate|2044|(180,)|var|int32
var_2045 = relay.var("var_2045", dtype = "int32", shape = (1080,))#candidate|2045|(1080,)|var|int32
output = func_2041(var_2042,var_2043,var_2044,var_2045,)
func_2046 = relay.Function([var_2042,var_2043,var_2044,var_2045,], output)
mutated_mod['func_2046'] = func_2046
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2090 = relay.var("var_2090", dtype = "float32", shape = (7, 16, 9))#candidate|2090|(7, 16, 9)|var|float32
uop_2091 = relay.log(var_2090.astype('float32')) # shape=(7, 16, 9)
output = relay.Tuple([uop_2091,])
output2 = relay.Tuple([uop_2091,])
func_2104 = relay.Function([var_2090,], output)
mod['func_2104'] = func_2104
mod = relay.transform.InferType()(mod)
var_2105 = relay.var("var_2105", dtype = "float32", shape = (7, 16, 9))#candidate|2105|(7, 16, 9)|var|float32
output = func_2104(var_2105)
func_2106 = relay.Function([var_2105], output)
mutated_mod['func_2106'] = func_2106
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2116 = relay.var("var_2116", dtype = "float32", shape = (9, 7, 14))#candidate|2116|(9, 7, 14)|var|float32
uop_2117 = relay.acos(var_2116.astype('float32')) # shape=(9, 7, 14)
uop_2122 = relay.log10(var_2116.astype('float64')) # shape=(9, 7, 14)
output = relay.Tuple([uop_2117,uop_2122,])
output2 = relay.Tuple([uop_2117,uop_2122,])
func_2128 = relay.Function([var_2116,], output)
mod['func_2128'] = func_2128
mod = relay.transform.InferType()(mod)
var_2129 = relay.var("var_2129", dtype = "float32", shape = (9, 7, 14))#candidate|2129|(9, 7, 14)|var|float32
output = func_2128(var_2129)
func_2130 = relay.Function([var_2129], output)
mutated_mod['func_2130'] = func_2130
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2441 = relay.var("var_2441", dtype = "float32", shape = (10, 10, 15))#candidate|2441|(10, 10, 15)|var|float32
uop_2442 = relay.sin(var_2441.astype('float32')) # shape=(10, 10, 15)
output = uop_2442
output2 = uop_2442
func_2446 = relay.Function([var_2441,], output)
mod['func_2446'] = func_2446
mod = relay.transform.InferType()(mod)
mutated_mod['func_2446'] = func_2446
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2447 = relay.var("var_2447", dtype = "float32", shape = (10, 10, 15))#candidate|2447|(10, 10, 15)|var|float32
func_2446_call = mutated_mod.get_global_var('func_2446')
call_2448 = func_2446_call(var_2447)
output = call_2448
func_2449 = relay.Function([var_2447], output)
mutated_mod['func_2449'] = func_2449
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2471 = relay.var("var_2471", dtype = "float32", shape = (9, 16))#candidate|2471|(9, 16)|var|float32
var_2472 = relay.var("var_2472", dtype = "float32", shape = (9, 16))#candidate|2472|(9, 16)|var|float32
bop_2473 = relay.power(var_2471.astype('float32'), relay.reshape(var_2472.astype('float32'), relay.shape_of(var_2471))) # shape=(9, 16)
func_456_call = mod.get_global_var('func_456')
func_459_call = mutated_mod.get_global_var('func_459')
const_2487 = relay.const([[-7],[-3],[4],[9],[1],[-9],[10],[-2],[6],[-8],[1],[3],[-8],[-1],[-3],[5],[3],[-9],[10],[-7],[9],[7],[-5],[-4],[8],[-4],[-3],[3],[7],[6],[-4],[2],[-10],[2],[-8],[-2],[6],[-4],[10],[-2],[1],[-7],[2],[-6],[3],[3],[-4],[5],[-5],[-8],[8],[7],[1],[5],[-3],[-2],[-4],[1],[-1],[8],[-10],[3],[5],[9],[-5],[-2],[7],[8],[-5],[9]], dtype = "uint32")#candidate|2487|(70, 1)|const|uint32
call_2486 = func_456_call(relay.reshape(const_2487.astype('uint32'), [7, 1, 10]))
call_2488 = func_456_call(relay.reshape(const_2487.astype('uint32'), [7, 1, 10]))
uop_2502 = relay.asinh(const_2487.astype('float32')) # shape=(70, 1)
bop_2506 = relay.floor_divide(uop_2502.astype('float64'), relay.reshape(const_2487.astype('float64'), relay.shape_of(uop_2502))) # shape=(70, 1)
bop_2516 = relay.subtract(uop_2502.astype('int64'), relay.reshape(const_2487.astype('int64'), relay.shape_of(uop_2502))) # shape=(70, 1)
func_927_call = mod.get_global_var('func_927')
func_929_call = mutated_mod.get_global_var('func_929')
var_2522 = relay.var("var_2522", dtype = "float32", shape = (320,))#candidate|2522|(320,)|var|float32
call_2521 = func_927_call(relay.reshape(var_2522.astype('float32'), [10, 2, 16]))
call_2523 = func_927_call(relay.reshape(var_2522.astype('float32'), [10, 2, 16]))
func_256_call = mod.get_global_var('func_256')
func_258_call = mutated_mod.get_global_var('func_258')
var_2530 = relay.var("var_2530", dtype = "float32", shape = (672,))#candidate|2530|(672,)|var|float32
call_2529 = func_256_call(relay.reshape(var_2530.astype('float32'), [6, 8, 14]))
call_2531 = func_256_call(relay.reshape(var_2530.astype('float32'), [6, 8, 14]))
func_1580_call = mod.get_global_var('func_1580')
func_1586_call = mutated_mod.get_global_var('func_1586')
var_2546 = relay.var("var_2546", dtype = "int32", shape = (180,))#candidate|2546|(180,)|var|int32
var_2547 = relay.var("var_2547", dtype = "int32", shape = (1080,))#candidate|2547|(1080,)|var|int32
var_2548 = relay.var("var_2548", dtype = "uint64", shape = (896,))#candidate|2548|(896,)|var|uint64
call_2545 = relay.TupleGetItem(func_1580_call(relay.reshape(var_2546.astype('int32'), [1, 12, 15]), relay.reshape(var_2547.astype('int32'), [6, 12, 15]), relay.reshape(var_2548.astype('uint64'), [896,]), relay.reshape(bop_2506.astype('uint32'), [7, 10]), ), 3)
call_2549 = relay.TupleGetItem(func_1586_call(relay.reshape(var_2546.astype('int32'), [1, 12, 15]), relay.reshape(var_2547.astype('int32'), [6, 12, 15]), relay.reshape(var_2548.astype('uint64'), [896,]), relay.reshape(bop_2506.astype('uint32'), [7, 10]), ), 3)
output = relay.Tuple([bop_2473,call_2486,bop_2506,bop_2516,call_2521,var_2522,call_2529,var_2530,call_2545,var_2546,var_2547,var_2548,])
output2 = relay.Tuple([bop_2473,call_2488,bop_2506,bop_2516,call_2523,var_2522,call_2531,var_2530,call_2549,var_2546,var_2547,var_2548,])
func_2561 = relay.Function([var_2471,var_2472,var_2522,var_2530,var_2546,var_2547,var_2548,], output)
mod['func_2561'] = func_2561
mod = relay.transform.InferType()(mod)
var_2562 = relay.var("var_2562", dtype = "float32", shape = (9, 16))#candidate|2562|(9, 16)|var|float32
var_2563 = relay.var("var_2563", dtype = "float32", shape = (9, 16))#candidate|2563|(9, 16)|var|float32
var_2564 = relay.var("var_2564", dtype = "float32", shape = (320,))#candidate|2564|(320,)|var|float32
var_2565 = relay.var("var_2565", dtype = "float32", shape = (672,))#candidate|2565|(672,)|var|float32
var_2566 = relay.var("var_2566", dtype = "int32", shape = (180,))#candidate|2566|(180,)|var|int32
var_2567 = relay.var("var_2567", dtype = "int32", shape = (1080,))#candidate|2567|(1080,)|var|int32
var_2568 = relay.var("var_2568", dtype = "uint64", shape = (896,))#candidate|2568|(896,)|var|uint64
output = func_2561(var_2562,var_2563,var_2564,var_2565,var_2566,var_2567,var_2568,)
func_2569 = relay.Function([var_2562,var_2563,var_2564,var_2565,var_2566,var_2567,var_2568,], output)
mutated_mod['func_2569'] = func_2569
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2685 = relay.var("var_2685", dtype = "float64", shape = (6, 16, 12))#candidate|2685|(6, 16, 12)|var|float64
uop_2686 = relay.tan(var_2685.astype('float64')) # shape=(6, 16, 12)
output = relay.Tuple([uop_2686,])
output2 = relay.Tuple([uop_2686,])
func_2688 = relay.Function([var_2685,], output)
mod['func_2688'] = func_2688
mod = relay.transform.InferType()(mod)
var_2689 = relay.var("var_2689", dtype = "float64", shape = (6, 16, 12))#candidate|2689|(6, 16, 12)|var|float64
output = func_2688(var_2689)
func_2690 = relay.Function([var_2689], output)
mutated_mod['func_2690'] = func_2690
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2692 = relay.var("var_2692", dtype = "bool", shape = (8, 4, 15))#candidate|2692|(8, 4, 15)|var|bool
var_2693 = relay.var("var_2693", dtype = "bool", shape = (8, 4, 15))#candidate|2693|(8, 4, 15)|var|bool
bop_2694 = relay.logical_or(var_2692.astype('bool'), relay.reshape(var_2693.astype('bool'), relay.shape_of(var_2692))) # shape=(8, 4, 15)
output = bop_2694
output2 = bop_2694
func_2703 = relay.Function([var_2692,var_2693,], output)
mod['func_2703'] = func_2703
mod = relay.transform.InferType()(mod)
var_2704 = relay.var("var_2704", dtype = "bool", shape = (8, 4, 15))#candidate|2704|(8, 4, 15)|var|bool
var_2705 = relay.var("var_2705", dtype = "bool", shape = (8, 4, 15))#candidate|2705|(8, 4, 15)|var|bool
output = func_2703(var_2704,var_2705,)
func_2706 = relay.Function([var_2704,var_2705,], output)
mutated_mod['func_2706'] = func_2706
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2949 = relay.const([[[6,5,-2],[-6,9,4],[4,1,-3],[-2,-10,-5],[8,-6,-2],[4,-4,8],[5,-7,-7],[-10,-4,2],[-3,8,-7]],[[10,4,10],[-6,4,5],[-6,-7,5],[-1,6,8],[-3,-4,8],[-3,-9,-2],[-3,-5,-8],[8,-1,4],[10,2,3]],[[5,3,-6],[-3,7,5],[2,10,2],[8,-2,6],[6,3,3],[-8,-3,-2],[-9,-7,-8],[8,10,-7],[-5,-4,-5]],[[-5,8,7],[-4,-2,5],[6,-8,2],[7,5,-9],[-8,9,-3],[4,-5,6],[4,8,-8],[9,-9,-9],[4,-3,1]],[[-5,-6,5],[-9,7,-9],[-6,4,-8],[-9,6,-5],[-8,-3,2],[-3,-7,1],[10,8,2],[2,-10,-3],[9,-7,-9]],[[2,-3,-8],[-10,-10,-4],[6,-1,-5],[4,2,-4],[-4,9,9],[-6,-5,5],[4,6,2],[-6,-8,-5],[-9,-10,2]],[[-10,-6,10],[4,6,2],[3,-9,-1],[3,-1,2],[1,6,-4],[5,7,-2],[-7,-10,6],[-6,-10,-1],[8,-6,-4]],[[7,-2,7],[1,2,5],[4,10,7],[-8,8,10],[8,-3,8],[-5,-3,6],[-4,3,-5],[-10,2,-3],[-8,4,10]],[[5,-3,-6],[-6,-6,9],[10,-10,-9],[-1,4,-9],[-10,9,-2],[7,8,-6],[1,-7,-10],[8,8,-2],[5,-6,-7]],[[-5,3,-3],[4,4,2],[-8,3,-9],[-10,4,-6],[-6,10,-9],[8,-3,9],[-8,6,9],[-4,-10,-2],[10,7,-1]],[[10,4,-1],[6,9,2],[7,-5,4],[2,8,-4],[10,-2,10],[10,3,2],[8,-1,9],[-9,5,-9],[5,-6,-3]],[[5,8,2],[3,2,7],[7,-1,-6],[-4,-7,6],[-8,9,-6],[-8,-8,10],[-8,2,-8],[3,-8,-8],[9,9,2]],[[3,-8,8],[5,-7,-4],[-2,2,2],[7,-7,-4],[-9,-6,-8],[-4,10,3],[8,-2,4],[-1,-10,-2],[-3,2,2]]], dtype = "int16")#candidate|2949|(13, 9, 3)|const|int16
var_2950 = relay.var("var_2950", dtype = "int16", shape = (13, 9, 3))#candidate|2950|(13, 9, 3)|var|int16
bop_2951 = relay.equal(const_2949.astype('bool'), relay.reshape(var_2950.astype('bool'), relay.shape_of(const_2949))) # shape=(13, 9, 3)
output = bop_2951
output2 = bop_2951
func_2959 = relay.Function([var_2950,], output)
mod['func_2959'] = func_2959
mod = relay.transform.InferType()(mod)
mutated_mod['func_2959'] = func_2959
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2960 = relay.var("var_2960", dtype = "int16", shape = (13, 9, 3))#candidate|2960|(13, 9, 3)|var|int16
func_2959_call = mutated_mod.get_global_var('func_2959')
call_2961 = func_2959_call(var_2960)
output = call_2961
func_2962 = relay.Function([var_2960], output)
mutated_mod['func_2962'] = func_2962
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3977 = relay.var("var_3977", dtype = "int64", shape = ())#candidate|3977|()|var|int64
var_3978 = relay.var("var_3978", dtype = "int64", shape = (15, 15, 16))#candidate|3978|(15, 15, 16)|var|int64
bop_3979 = relay.bitwise_xor(var_3977.astype('int64'), var_3978.astype('int64')) # shape=(15, 15, 16)
output = bop_3979
output2 = bop_3979
func_3985 = relay.Function([var_3977,var_3978,], output)
mod['func_3985'] = func_3985
mod = relay.transform.InferType()(mod)
mutated_mod['func_3985'] = func_3985
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3985_call = mutated_mod.get_global_var('func_3985')
var_3987 = relay.var("var_3987", dtype = "int64", shape = ())#candidate|3987|()|var|int64
var_3988 = relay.var("var_3988", dtype = "int64", shape = (15, 15, 16))#candidate|3988|(15, 15, 16)|var|int64
call_3986 = func_3985_call(var_3987,var_3988,)
output = call_3986
func_3989 = relay.Function([var_3987,var_3988,], output)
mutated_mod['func_3989'] = func_3989
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4216 = relay.var("var_4216", dtype = "float64", shape = (1, 11, 3))#candidate|4216|(1, 11, 3)|var|float64
uop_4217 = relay.sigmoid(var_4216.astype('float64')) # shape=(1, 11, 3)
func_910_call = mod.get_global_var('func_910')
func_912_call = mutated_mod.get_global_var('func_912')
const_4220 = relay.const([-6,10,9,-8,-4,-5,10,-7,7,10,-1,7,-8,-9,2,-5,-10,-4,10,4,-1,-8,-6,-1,-5,8,-4,9,-8,1,6,-2,10,5,-10,-3,-9,-1,-8,-9,-5,-10,-6,1,9,5,5,-6,-3,-4,-2,-3,-7,-10,-9,9,-10,3,8,-9,3,6,1,-4,3,-9,-4,-9,-7,8,-10,9,6,5,3,2,-7,-5,-2,-5,6,1,-6,-1,-1,-8,7,-10,-9,-8,-8,8,3,-6,-2,-10,-6,-6,-3,-5,9,-5,1,1,10,-2,-2,-4,6,7,-2,6,-10,-10,1,-9,-1,7,2,3,7,-10,8,5,-3,-1,1,-5,-2,-8,-2,-5,3,-8,10,-9,-9,-10,-3,2,-7,-5,2,1,-6,-9,8,-3,4,8,-5,4,5,2,9,6,-10,-4,10,8,-6,4,9,-7,-1,8,3,9,-8,-8,8,2,-4,10,-4,7,3,6,-1,6,9,7,8,9,-8,2,10,3,2,7,-2,-8,6,-9,-10,-8,-9,-10,-2,4,6,7,1,10,-3,-9,-1,-10,-4,5,-3,2,9,-10,1,-2,-1,-4,9,6,-1,7,-6,9,7,4,7,4,8,-7,-10,-7,-8,-5,-5,8,-6,7,3,1,-2,-2,1,-6,-9,-7,2,2,-6,-6,8,8,1,7,3,-6,3,5,3,4,-4,3,-6,7,-3,-3,-9,8,-6,5,-3,4,8,-1,-1,-7,7,-3,6,-2,-3,2,6,1,5,1,9,-5,5,10,-4,-2,-6,1,-5,4,10,9,8,-7,-7,2,-4,-3,-4,4,1,-6,-1,10,1,-3,2,6,3,10,2,6,-8,2,5,1,-1,2,5,7,5,-7,-1,4,6,6,7,-1,-4,-10,-10,2,9,3,-5,4,-10,7,-3,9,-9,7,-8,5,-3,2,6,-3,9,3,-6,-4,-7,10,-5,9,-4,2,-7,8,9,-1,4,-4,-2,7,-3,6,5,9,-5,-4,7,2,2,-1,-10,10,8,6,-10,-10,5,2,-2,-10,9,7,-9,-9,-1,-3,-3,-4,6,1,-3,8,6,8,1,6,-1,8,-4,-2,-5,5,-10,9,8,-2,10,9,-2,-6,2,-4,7,-4,7,7,10,2,-10,8,4,1,1,-9,-6,9,7,2,5,6,-1,-6,4,3,-2,5,10,-9,5,-8,-3,8,8,5,-5,7,-1,-7,2,2,-10,9,1,2,6,-7,-7,-10,-7,10,5,8,-10,-2,6,8,8,-5,-5,-7,9,1,-8,-2,-7,9,-2,7,-1,-6,-2,-2,-4,-1,7,2,-1,3,6,-6,-10,3,1,5,1,-10,8,3,-2,10,4,5,-5,-7,-6,3,10,-9,8,-7,-7,-9,-1,-6,-1,-10,10,-2,-6,5,-6,9,4,8,-1,-10,2,-3,6,-3,8,1,1,-3,2,10,-8,-3,6,-6,-6,5,-8,8,10,10,-7,5,4,-6,8,6,4,8,-1,-6,1,-3,-4,4,2,-3,4,-6,8,7,-7,-3,2,-10,-8,-8,-2,9,-3,9,8,4,-1,-2,-4,6,2,2,-3,-5,-9,-1,5,6,-4,3,8,-3,10,8,4,7,5,10,-2,-10,-9,3,-2,3,-3,-7,-4,9,-8,1,-1,10,8,4,6,-10,-7,-10,-1,5,9,-6,-6,10,2,-10,10,6,1,-7,-6,-3,-1,3,7,-7,-4,1,7,-4,5,-9,5,2,-9,-2,-5,9,-9,7,10,4,6,-4,1,10,-3,8,6,1,-8,-2,9,10,-4,5,10,10,7,6,3,3,-7,-3,2,10,-8,-4,6,6,-10,5,-2,-5,-10,-8,-9,8,-1,-2,-6,2,7,-2,1,-4,-1,-10,-4,4,8,-7,-3,6,8,9,-10,-10,9,1,-2,-9,-4,5,-6,3,3,2,9,-9,5,2,9,6,6,7,10,10,-7,-3,-6,-10,6,-4,-1,1,3,5,5,-1,7,-8,4,-3,5,-7,-2,-1,-10,-3,-9,8,10,-3,3,8,2,8,-6,-10,-7,-3,3,-9,-10,-3,-9,-3,2,-5,-10,4,-1,-7,-5,9,3,3,7,-10,-6,-7,3,5,-6,2,-5,7,1,4,-10,-2,-4,-10,8,-9,-2,-9,-8,2,-7,1,1,2,1,-1,-9,-5,-9,6,-4,2,-5,3,-7,9,-9,10,8,3,-7,2,7,-1,-4,-2,3,-6,-6,2,-4,-1,-1,5,2,9,-2,9,8,-6,8,1,-3,-2,6,6,6,4,-8,-7,9,-4,-4,-10,5,-3,5,6,10,1,-5,5,4,-9,10,-7,-1,-2,3,5,10,-3,-3,5,9,7,-2,-5,6,1,9,7,-10,-5,10,1,10,-5,4,-6,5,-7,8,5,8,-1,5,-9,4,-8,-3,-4,-4,8,10,-1,7,-4,-1,-8,5,8,-5,5,-10,-6,5,-8,3,-6,-7,-8,8,9,10,-10,5,7,6,1,-6,-7,-9,1,-10,-4,6,3,-5,7,10,-2,-7,6,2,7,6,-10,-10,8,-8,7,4,9,-2,7,-4,-6,-6,4,10,6,7,1,-7,-5,1,8,-4,7,5,-8,2,2,4,8,7,-10,-9,2,-1,-10,3,-10,-9,2,2,3,-2,2,10,2,3,2,6,-2,2,-1,-2,-1,9,-4,-1,-5,-1,3,-8,-1,-10,6,8,4,10,7,6,2,1,-6,-3,9,9,-7,6,9,2,3,3,-2,-1,-2,6,2,-10,-2,-1,-8,1,-9,-7,7,4,-1,-5,8,3,5,-6,9,-9,-10,9,1,7,-1,10,4,-5,-3,-8,-8,-2,10,-4,-5,-7,-1,5,8,-6,6,4,10,-3,-2,3,-1,5,-5,10,9,-5,4,6,1,1,-6,5,6,10,-10,8,-9,3,-1,4,-10,2,-10,-8,-10,6,7,3,-3,1,-5,-5,3,6,10,-6,10,4,8,-1,-2,4,10,3,10,7,7,8,1,-8,8,3,3,8,-1,10,5,5,3,1,5,9,-1,4,4,6,5,10,7,9,-6,-5,7,10,-9,-5,10,-6,2,-4,-1,8,10,-4,-7,-6,4,-8,1,-10,9,-7,-9,8,5,10,4,4,8,-10,-2,10,8,-6,-5,3,2,-1,-5,4,2,-7,-2,10,-10,-4,7,-10,-3,-7,-5,-2,-2,-7,3,6,5,-4,8,-6,-4,-3,-8,9,-9,2,9,-10,7,8,1,7,-1,3,-5,-8,-3,4,-1,-5,-9,4,-10,-1,-4,-9,4,10,-7,3,-4,-2,1,10,-9,4,-9,10,-5,-8,-9], dtype = "int64")#candidate|4220|(1260,)|const|int64
call_4219 = relay.TupleGetItem(func_910_call(relay.reshape(const_4220.astype('int64'), [10, 14, 9])), 0)
call_4221 = relay.TupleGetItem(func_912_call(relay.reshape(const_4220.astype('int64'), [10, 14, 9])), 0)
output = relay.Tuple([uop_4217,call_4219,const_4220,])
output2 = relay.Tuple([uop_4217,call_4221,const_4220,])
func_4229 = relay.Function([var_4216,], output)
mod['func_4229'] = func_4229
mod = relay.transform.InferType()(mod)
mutated_mod['func_4229'] = func_4229
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4230 = relay.var("var_4230", dtype = "float64", shape = (1, 11, 3))#candidate|4230|(1, 11, 3)|var|float64
func_4229_call = mutated_mod.get_global_var('func_4229')
call_4231 = func_4229_call(var_4230)
output = call_4231
func_4232 = relay.Function([var_4230], output)
mutated_mod['func_4232'] = func_4232
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4275 = relay.var("var_4275", dtype = "int64", shape = (13, 8, 7))#candidate|4275|(13, 8, 7)|var|int64
var_4276 = relay.var("var_4276", dtype = "int64", shape = (13, 8, 7))#candidate|4276|(13, 8, 7)|var|int64
bop_4277 = relay.bitwise_xor(var_4275.astype('int64'), relay.reshape(var_4276.astype('int64'), relay.shape_of(var_4275))) # shape=(13, 8, 7)
func_2703_call = mod.get_global_var('func_2703')
func_2706_call = mutated_mod.get_global_var('func_2706')
var_4283 = relay.var("var_4283", dtype = "bool", shape = (480,))#candidate|4283|(480,)|var|bool
call_4282 = func_2703_call(relay.reshape(var_4283.astype('bool'), [8, 4, 15]), relay.reshape(var_4283.astype('bool'), [8, 4, 15]), )
call_4284 = func_2703_call(relay.reshape(var_4283.astype('bool'), [8, 4, 15]), relay.reshape(var_4283.astype('bool'), [8, 4, 15]), )
uop_4291 = relay.rsqrt(call_4282.astype('float32')) # shape=(8, 4, 15)
uop_4293 = relay.rsqrt(call_4284.astype('float32')) # shape=(8, 4, 15)
output = relay.Tuple([bop_4277,var_4283,uop_4291,])
output2 = relay.Tuple([bop_4277,var_4283,uop_4293,])
func_4304 = relay.Function([var_4275,var_4276,var_4283,], output)
mod['func_4304'] = func_4304
mod = relay.transform.InferType()(mod)
var_4305 = relay.var("var_4305", dtype = "int64", shape = (13, 8, 7))#candidate|4305|(13, 8, 7)|var|int64
var_4306 = relay.var("var_4306", dtype = "int64", shape = (13, 8, 7))#candidate|4306|(13, 8, 7)|var|int64
var_4307 = relay.var("var_4307", dtype = "bool", shape = (480,))#candidate|4307|(480,)|var|bool
output = func_4304(var_4305,var_4306,var_4307,)
func_4308 = relay.Function([var_4305,var_4306,var_4307,], output)
mutated_mod['func_4308'] = func_4308
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4568 = relay.var("var_4568", dtype = "bool", shape = (11, 7, 14))#candidate|4568|(11, 7, 14)|var|bool
const_4569 = relay.const([[[False,False,True,False,True,True,True,False,False,False,False,True,True,False],[False,True,False,True,False,False,False,True,False,False,True,False,True,True],[True,True,True,True,False,False,True,True,True,False,False,False,False,False],[True,True,False,True,True,False,False,True,True,True,False,True,True,True],[True,False,True,False,False,False,False,False,True,True,True,False,False,True],[False,False,True,True,False,False,False,True,False,True,False,True,False,True],[True,True,False,False,False,True,True,False,False,True,False,True,False,True]],[[True,False,True,False,True,False,True,True,False,False,False,True,True,False],[False,True,True,True,False,False,False,False,True,True,False,True,False,False],[False,False,False,False,True,True,False,False,True,True,True,False,True,True],[True,False,True,True,True,True,True,False,True,True,False,False,False,True],[False,False,True,False,False,True,False,True,False,False,True,False,False,False],[False,True,True,True,False,True,False,True,False,True,True,True,False,False],[True,False,True,True,False,False,False,True,False,False,False,False,True,False]],[[False,True,False,False,False,False,True,False,True,False,False,True,True,True],[False,False,True,True,False,False,True,True,True,True,False,True,True,False],[True,False,False,False,True,True,False,False,True,False,False,False,False,False],[True,True,False,True,True,True,False,False,False,True,True,True,False,True],[False,False,True,True,False,False,True,False,True,False,False,False,False,False],[False,False,True,True,True,True,False,True,False,False,True,False,False,False],[True,False,True,True,False,False,True,True,False,False,True,True,False,True]],[[True,False,True,True,False,False,False,False,True,False,True,False,True,False],[False,True,False,False,True,True,True,False,True,False,True,False,True,False],[True,True,True,True,False,False,False,False,True,True,False,False,True,True],[False,False,True,True,True,True,True,True,False,False,True,False,True,False],[False,False,False,True,True,True,False,True,True,True,False,False,False,False],[True,True,False,True,False,True,False,True,True,True,False,True,False,True],[True,True,True,True,True,True,True,False,False,True,False,False,False,False]],[[False,False,False,True,False,False,True,False,False,True,True,True,True,False],[False,True,True,False,False,True,True,True,False,False,True,True,False,True],[True,False,True,True,True,False,True,True,False,False,True,False,True,False],[True,False,False,False,True,False,False,True,True,True,False,True,False,False],[False,False,True,True,False,True,True,True,True,False,False,True,False,True],[False,True,False,True,False,False,True,True,False,True,True,True,True,True],[True,True,True,True,True,True,True,True,False,False,True,True,False,True]],[[False,False,True,False,True,True,False,True,True,True,True,False,True,False],[True,False,True,False,True,True,False,False,False,True,True,False,True,False],[True,True,False,True,True,True,False,False,False,False,False,True,True,True],[True,False,True,True,False,False,True,True,True,True,True,True,False,True],[True,True,True,False,False,True,False,True,False,False,False,False,False,False],[False,True,True,True,False,False,False,False,False,False,False,False,True,True],[True,False,False,True,True,False,True,False,True,True,True,False,True,True]],[[False,True,True,False,True,False,False,True,False,False,True,True,False,True],[True,False,True,False,False,True,True,True,True,True,True,True,False,True],[True,False,False,True,True,False,False,False,False,False,True,True,False,True],[False,True,False,True,True,True,True,True,True,True,False,False,False,False],[True,False,True,False,False,True,False,False,True,False,False,False,False,False],[True,False,True,True,True,True,False,False,True,True,True,False,False,False],[False,False,False,False,True,True,False,True,False,False,True,False,False,False]],[[False,False,False,True,True,True,False,False,False,False,True,True,True,False],[True,False,False,False,False,False,False,True,True,False,True,False,True,False],[False,True,False,False,False,False,True,True,True,True,True,False,True,False],[True,False,True,True,False,True,True,True,False,True,False,True,True,True],[True,False,False,True,False,False,True,False,True,False,True,False,True,False],[False,False,True,False,True,False,True,True,True,False,False,True,True,True],[True,False,False,False,True,False,False,True,True,True,True,False,False,False]],[[False,True,False,True,False,True,True,True,True,False,False,True,False,True],[False,True,False,True,True,False,False,False,True,False,True,False,True,False],[False,True,False,False,True,True,True,True,False,False,False,False,False,False],[True,False,True,True,True,True,True,True,False,True,True,True,True,True],[True,False,True,True,False,False,True,True,True,True,False,True,True,False],[True,False,False,False,False,False,False,False,True,True,True,True,False,False],[False,True,True,True,True,True,False,True,True,False,False,False,True,False]],[[True,False,False,True,False,True,True,True,True,True,True,False,False,False],[False,False,False,False,True,False,False,True,True,False,False,False,False,True],[False,True,True,True,False,False,False,False,True,False,True,False,True,False],[False,False,False,False,False,True,True,False,True,True,True,False,True,True],[False,False,False,False,True,False,True,True,False,False,False,True,False,True],[True,True,False,True,True,False,False,False,True,True,False,False,False,True],[False,True,False,False,True,True,False,True,True,False,False,True,False,False]],[[False,False,False,True,True,False,False,True,False,False,True,False,True,True],[False,True,False,True,True,False,True,False,True,False,True,False,False,False],[True,False,False,True,False,False,False,True,False,True,False,True,True,True],[True,True,False,True,False,False,False,True,True,False,False,False,False,True],[True,False,True,False,False,False,False,False,False,False,True,True,True,False],[False,True,True,True,False,False,False,False,False,True,False,True,True,False],[False,True,True,True,True,True,True,True,True,True,True,True,False,False]]], dtype = "bool")#candidate|4569|(11, 7, 14)|const|bool
bop_4570 = relay.logical_and(var_4568.astype('bool'), relay.reshape(const_4569.astype('bool'), relay.shape_of(var_4568))) # shape=(11, 7, 14)
output = bop_4570
output2 = bop_4570
func_4574 = relay.Function([var_4568,], output)
mod['func_4574'] = func_4574
mod = relay.transform.InferType()(mod)
mutated_mod['func_4574'] = func_4574
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4575 = relay.var("var_4575", dtype = "bool", shape = (11, 7, 14))#candidate|4575|(11, 7, 14)|var|bool
func_4574_call = mutated_mod.get_global_var('func_4574')
call_4576 = func_4574_call(var_4575)
output = call_4576
func_4577 = relay.Function([var_4575], output)
mutated_mod['func_4577'] = func_4577
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4823 = relay.var("var_4823", dtype = "float64", shape = (2, 8, 14))#candidate|4823|(2, 8, 14)|var|float64
uop_4824 = relay.asin(var_4823.astype('float64')) # shape=(2, 8, 14)
func_2104_call = mod.get_global_var('func_2104')
func_2106_call = mutated_mod.get_global_var('func_2106')
const_4843 = relay.const([-7.365416,6.361721,-2.747851,9.259604,0.040897,-5.602470,1.956931,-1.227993,-1.372138,-6.852961,7.985105,7.302880,-1.735582,6.078248,-1.039431,-3.570605,0.784193,-7.663103,8.634579,8.836867,3.575160,0.066394,-0.040017,-3.278633,-7.878535,0.811574,-0.899295,6.548688,3.421812,-5.140876,3.718083,4.824222,-6.016749,-5.767651,5.118686,6.007555,8.866718,5.166151,-0.390082,-5.212115,-7.520808,-3.510886,7.560606,-1.307933,5.088638,-7.766230,3.578341,7.657567,0.841827,6.926461,4.551486,3.770425,8.622008,-2.977546,-4.683088,-3.552622,-6.496466,7.044297,-2.395419,4.739093,8.364021,-2.410730,6.644463,-9.630239,3.165200,7.686773,-5.513352,-9.639712,-7.458016,-6.058026,4.021286,3.219131,8.587031,9.192653,-1.092363,0.097042,8.398741,8.192227,0.632132,2.954589,1.484950,-7.401251,-6.487158,-1.785172,6.199076,1.198109,2.535450,6.551381,-1.269142,8.637588,7.366401,-4.857311,-9.862008,4.727432,8.859600,7.579995,2.353499,8.667106,-0.564746,-3.657649,-3.637452,-0.356155,8.268917,-4.621217,0.865243,-0.719905,3.374101,8.343115,-1.900077,5.015183,1.532058,1.250017,-5.691281,-7.045735,-8.394031,6.742425,3.080933,-8.385792,1.392777,-9.617372,-4.390162,8.743718,9.796756,-4.490067,8.732321,2.738646,-4.478522,5.681935,4.115572,5.786424,7.725884,-7.148712,-5.429018,2.571713,-4.157562,-8.768673,-4.128157,-4.184575,-6.419126,-6.425967,-3.440541,4.735656,-9.998241,-6.480380,-7.546402,3.370054,-1.333850,-6.804030,-3.282625,-2.429789,1.549209,-8.849592,-9.180801,9.329144,2.955454,-2.209875,-0.851585,-9.628391,-4.390830,-5.671631,-2.764099,-0.627430,-0.044382,1.156430,-8.112700,0.210986,0.872967,-0.889178,-0.349769,-1.439857,6.123492,1.786311,-4.347475,-1.594831,-1.446390,-6.290187,-9.306334,6.492822,3.993636,5.895398,-2.703115,-9.729879,-3.990135,2.976304,-5.146413,-8.651740,-1.509939,6.115283,0.726724,-9.982325,4.109257,-6.397156,4.345350,-3.195875,6.855023,3.473486,-8.177075,9.434125,-5.742799,1.266312,-5.974965,-6.262389,7.355911,-8.535200,8.606871,0.795329,8.945158,-0.505900,3.981368,1.642786,-0.312740,2.506190,-3.368543,-7.791399,5.747158,-2.392625,3.612994,4.185907,-6.181919,-8.373243,-1.361220,-1.629294,0.408747,-5.122187,6.178097,4.205057,-6.837904,-1.806409,1.731551,3.671293,-3.326898,1.297548,-3.405342,1.501071,-9.636172,-5.315088,7.261952,-8.056201,2.977550,5.594008,-0.397292,5.331734,9.826946,-1.724176,-4.285581,-5.048243,3.972666,-9.141467,-8.762694,-7.705299,0.665399,5.032435,-5.066271,-8.436267,-8.343448,-4.995391,-4.282287,-4.859286,-5.279253,2.493649,-9.267085,7.953283,2.300983,-1.672639,3.501344,-0.054557,3.122980,7.699962,8.392127,-3.849305,-4.825936,-0.609113,-0.263324,-2.194552,8.070493,2.896084,3.164526,4.859765,-0.393306,-4.081618,2.931189,1.411263,-3.227785,-1.685458,-5.573522,-6.573865,3.584951,7.594740,2.729089,-1.282192,0.413886,-3.203678,9.847317,0.935787,4.279394,4.490493,-7.250685,-3.862397,-1.816474,-8.334114,9.868437,4.194788,-3.626393,-4.334770,-4.007621,-1.290074,-1.685322,9.389710,7.296580,3.479762,-8.067292,3.655882,8.021618,-2.992162,-9.204367,-4.761172,7.451364,-9.716100,7.820419,7.685110,-7.479961,2.133352,-8.187763,-5.814434,-3.327323,4.859851,-8.839999,1.519791,-6.115501,8.827937,0.820633,-4.867682,7.759856,-9.508064,7.086406,0.906945,1.179450,-2.018088,5.676164,9.090248,-8.030173,-6.027291,2.304687,8.395945,2.464085,-6.976922,-6.840804,8.728471,-5.369114,-8.077517,3.915857,2.404881,6.140262,4.259142,-6.809290,-7.631329,9.930178,2.393730,-9.316546,-7.949349,-2.119937,-0.373594,5.879197,-7.656169,5.741805,1.047775,-0.027402,-5.141216,-3.312393,-3.035460,-8.368947,4.477111,-1.795583,7.468911,6.274873,-4.464729,-6.931251,4.360572,9.546357,7.179551,-3.542714,2.813559,3.753624,-2.630520,5.758140,-8.770786,3.887583,0.676749,6.675468,5.039482,-7.662937,-9.955492,-5.942232,-4.226437,6.400622,1.434923,-4.832400,8.925386,-7.898246,6.535481,-3.050166,7.110585,-1.728797,1.405030,9.291761,-1.828291,3.946255,0.244189,-5.536184,8.343601,2.688343,-5.928123,5.652148,-8.394480,2.295276,-3.395279,3.802842,-1.487150,-4.662207,7.458505,-2.348479,-5.938316,-4.551914,7.584862,4.658868,5.696629,2.162859,8.010509,1.481337,-7.818475,2.161366,-5.889734,3.923421,-5.671124,3.434806,9.049210,-2.222904,6.893525,8.194820,2.807534,3.872722,-4.772004,-6.871408,0.200764,0.318575,1.729365,-9.842027,4.142610,-0.509323,-3.808670,-4.495502,4.971804,9.866777,8.601246,2.949560,6.105718,8.779247,-5.242496,7.561860,1.514888,9.276935,-9.072793,9.321036,2.158882,7.162021,5.389234,-4.663459,-7.699402,5.821738,-1.307505,7.689614,5.847750,5.437336,-4.919796,2.067335,5.445252,-8.931228,6.031549,-3.256104,2.268271,-3.348243,9.118709,0.651720,-5.571055,3.544088,-4.295228,-9.281256,-1.672813,3.187900,7.024041,-5.400471,9.601229,-4.471140,-8.358858,-0.639040,-2.825728,-7.944436,5.661126,-8.430297,-2.157201,-8.389653,-0.398941,-2.729111,1.954828,3.655940,3.650237,1.109423,5.743576,5.006980,-9.772460,2.035518,-8.853865,-2.725668,-6.716022,3.955819,3.525669,7.905542,-6.024775,-4.646052,8.930166,-8.784766,1.213881,7.579962,2.812358,3.999931,-8.820724,6.760646,-6.030102,-3.631389,-6.360116,-1.705216,-6.874404,8.072825,9.678436,-4.227808,7.825370,0.299101,-1.470957,1.359372,7.039462,-7.497438,-7.028852,-0.708653,6.501782,9.223391,-4.640840,3.609194,0.197522,-3.626437,-8.035176,9.515733,5.100624,2.507677,9.545352,-5.364731,8.862775,9.712088,-1.708765,-0.407558,-5.750500,7.797002,3.719429,4.416879,2.813649,-3.011630,-4.811176,9.839165,-4.131657,-1.868477,-9.119498,3.256562,8.048485,5.319432,-5.029143,5.553323,3.519409,-3.090559,-2.625519,7.177113,4.576111,1.760388,6.298199,0.700063,9.406249,8.796007,-6.627494,8.807213,8.346455,7.630908,1.008463,4.060958,1.258241,8.338269,1.767731,9.850123,-4.509617,2.490682,-8.976539,-5.729390,-8.883814,7.457975,-7.156776,-7.952899,3.064927,7.311517,-4.934311,9.221304,-5.851401,4.030963,8.455984,-8.736256,-3.869614,1.893234,9.033121,-8.931493,8.871859,-3.601171,0.315179,-0.308026,5.822031,9.334786,-5.990006,2.096538,6.565747,-7.957188,-4.144252,7.002269,-8.919355,2.458001,-3.014274,2.404559,5.121671,6.369020,-0.303141,8.556192,1.330420,-1.272533,9.669372,8.558026,-9.126108,8.794495,-8.440566,1.042800,5.736528,-5.631019,2.886065,2.497250,-5.445234,3.174234,-5.238982,-8.061539,5.857859,4.127580,-0.022096,3.996141,6.492649,5.055439,4.279342,-4.804335,2.457641,-8.803769,0.983015,1.685333,-5.077853,-5.100670,5.035523,4.644423,0.166757,4.592309,8.924647,6.740809,5.818429,-1.731791,4.057653,6.600890,-1.820650,2.666664,-6.447047,0.059529,9.377627,4.709846,-5.700031,1.484778,-5.074261,2.209880,-3.070744,-8.706664,-1.441444,-2.703175,7.606197,-6.058873,-1.808792,2.406758,6.069873,1.414133,9.400105,3.054924,7.818178,4.678473,-3.533193,1.740460,2.826694,-9.825036,8.043644,-6.956444,5.550673,-8.594127,-1.860110,-2.809516,-5.939877,7.519438,-6.938829,8.356163,4.836621,9.137795,7.128591,-0.590566,-9.771898,-1.910916,-9.899591,2.036496,-2.218571,5.226089,2.306589,-5.230257,9.241968,3.595603,-1.258647,-9.127198,-9.448313,9.023755,-1.751700,-2.984664,6.453125,-3.483705,9.871811,1.746491,0.357713,1.638336,-1.379934,-8.754642,7.182577,7.017523,-9.870001,4.297544,-4.953779,0.700165,4.335513,8.783607,-2.026928,-3.411607,4.696332,1.646697,-4.906155,-8.131652,-5.740510,-3.693839,-3.686590,-5.560040,5.465850,6.919851,-8.892985,6.712904,4.530645,-6.220220,-6.580444,3.524369,-9.649160,1.880496,9.987550,4.141254,-8.783879,6.624876,-7.707426,-5.179787,-4.346123,0.426172,-3.693941,-4.904659,5.987596,9.294617,4.250868,-7.603122,-8.568818,-5.303498,8.466754,4.129178,0.789370,-7.806316,-1.973405,-2.099672,1.493459,-5.030257,-2.965068,1.989270,3.644469,6.529491,3.630043,9.595451,2.640215,-1.898246,7.124812,9.397078,-3.309292,-1.249816,-7.269737,2.503211,-4.091866,6.639541,-8.556308,4.314625,9.010739,-2.202821,-3.689622,-8.468670,8.908005,-6.029246,0.920241,-8.271480,3.024454,-6.489763,9.880766,1.985424,9.090208,-0.359553,2.604907,-7.622529,-2.059045,-4.341089,-6.520687,1.634426,2.428256,-8.282651,6.334848,-7.647902,-4.145441,-0.719555,2.037582,5.230054,-0.382928,-2.453881,9.758352,-1.518493,-8.626515,-7.286203,-1.800352,-4.940456,7.731148,-1.507113,8.415189,-9.268117,5.339133,0.875862,-5.203121,-6.635943,-7.866660,0.611374,3.614378,-1.089521,-6.649428,-0.358864,-1.025415,-0.019089,9.190535,-0.696674,0.468174,-6.802708,5.497262,1.259511,5.702635,-7.339950,2.138183,7.196156,0.986736,-0.190641,7.038228,-7.869835,7.506988,4.592768,4.308228,-0.042378,-5.184588,-7.078349,-8.159426,-3.031687,4.049730,-0.385560,-2.375404,0.624151,6.837008,6.138277,-0.313331,-4.398954,-8.559485,-8.131425,3.432386,-2.981294,-7.450081,9.372682,1.374564,-9.337350,-2.403639,6.434940,-2.084826,-4.077354,-1.360125,-7.737283,-0.406171,-2.192769,1.462222,-6.355298,7.519326,-4.549723,7.272711,5.950926,7.301321,1.167800,-1.727201,-9.101483,1.644074,-4.547542,-4.304592,-9.791432,0.185657,6.117732,-0.694157,5.448941,8.627165,7.111950,8.854501,1.579777,-2.495158,-7.424019,4.096409,3.558863,3.632639,-1.571506,1.170935,-8.057735,9.292173,4.870551,-7.534100,-5.309657,-0.614284,-2.240541,-3.991082,2.137278,0.958671,6.648858,-1.946511,4.638186,-6.092769,-5.813040,9.990942,-6.741195,-5.393403,-9.445270,-0.593480,-7.061897,-4.889705,-0.261369,-3.607823,7.993537,2.030471,-3.599550,1.438038,7.817822,4.577261,4.074503,6.471335,-6.684066,7.831011,-8.054180,7.342902,6.621320,9.254226,-0.778550,6.841649,5.955937,-3.201930,-5.715384,-6.441072,8.044648,5.403386,-7.922663,-7.364503,9.920594,6.047029,8.288398,-5.968958,-4.410690,-7.105391,-1.781605,-3.232000,-1.307941,8.878192,-5.480223,-8.999827,-8.547333,0.166423,-2.799817,9.731101,8.389473,3.381783,7.159773,9.942314,-6.440938,-7.101086], dtype = "float32")#candidate|4843|(1008,)|const|float32
call_4842 = relay.TupleGetItem(func_2104_call(relay.reshape(const_4843.astype('float32'), [7, 16, 9])), 0)
call_4844 = relay.TupleGetItem(func_2106_call(relay.reshape(const_4843.astype('float32'), [7, 16, 9])), 0)
func_2561_call = mod.get_global_var('func_2561')
func_2569_call = mutated_mod.get_global_var('func_2569')
const_4850 = relay.const([-8.575247,5.881105,8.070964,3.043003,-0.449751,-0.261202,9.689044,-4.906816,-6.374128,9.373571,-1.370562,-2.862266,-7.199630,-3.808676,7.435447,-1.551520,1.805142,-3.016411,-6.608940,-9.408245,-6.784128,1.880088,6.478680,9.915086,5.046901,-1.710700,-7.958016,6.136090,8.419150,-8.062049,-1.111619,0.661676,-8.999382,-7.581872,4.406235,-1.210314,-4.305211,0.195550,3.127832,3.007082,-3.536001,-7.992482,6.151580,6.917355,7.937458,4.944478,-3.918702,-5.575911,8.594366,-7.361244,3.720397,-9.989687,-8.665930,9.746186,6.911560,-6.852392,1.908951,-2.250326,2.142308,2.054867,4.674382,-7.091252,2.856218,-1.162137,2.227781,4.173960,3.701286,-3.165881,-2.835746,6.568275,3.316526,8.826877,3.274114,2.493402,8.311100,1.295470,1.489940,-9.959402,-4.365303,4.011545,1.887307,-5.931319,8.838130,2.864725,3.086940,0.549868,-9.557570,7.826022,-2.185715,-6.204853,2.393626,-8.094380,8.160940,-0.534760,8.056256,-0.164537,-5.959744,-0.875287,7.624198,7.821688,-7.404198,3.754618,6.060801,-4.224619,1.940929,4.698876,7.335492,-3.532831,7.049342,-2.562246,-5.510550,9.083764,-9.077192,-9.291633,9.508528,-7.863882,-9.309598,6.002401,-3.845835,9.067004,-5.616703,-2.987903,-7.805290,4.434996,4.838412,6.752740,-7.020188,6.274213,-3.345409,-3.037017,4.184905,4.745431,7.422269,-0.699337,9.569816,9.377787,-0.014318,0.936451,-6.262459,-5.659618,-7.811005,-8.613879,5.569902,9.563284], dtype = "float32")#candidate|4850|(144,)|const|float32
const_4851 = relay.const([0.992810,1.476630,6.725681,3.944806,4.546306,6.364183,7.973364,0.499084,6.066703,7.050437,-0.649974,3.686537,-5.648415,1.071041,-7.129946,-5.480936,5.275150,8.557800,-8.786424,-1.631783,-6.707763,-7.435859,7.223263,-4.378939,-9.558247,-9.722701,-0.247667,-9.643847,7.761751,-9.492906,-4.787020,0.878004,8.080876,-4.237251,8.057916,8.057129,-4.976727,7.665469,7.352856,6.757065,2.782905,-4.493717,0.389926,-3.524279,-1.176886,-6.438749,-2.510161,8.212036,-1.110039,3.930754,-8.583103,-0.395047,1.175838,-0.298270,0.173569,-2.081861,-6.791153,-2.841327,1.352452,-4.644924,9.557785,-8.243448,-7.272069,9.538384,-3.022480,-7.226839,3.629169,7.578116,1.622019,5.677666,0.368767,9.427724,-3.091591,-8.749331,7.536472,-8.335026,4.492102,-3.304397,-0.517413,0.125284,-8.412027,5.225142,-8.295694,-2.300510,-7.151284,-6.167263,8.258217,5.456934,6.124790,-6.675118,-5.923232,0.327435,1.678740,7.694764,-2.965154,-9.188244,8.293244,-2.617696,9.868948,5.833211,2.776529,5.223352,2.149409,-5.275440,-5.556970,4.618316,3.165890,3.229931,-5.549643,-1.530845,5.157870,-7.208902,-3.973231,-5.747445,4.625151,-6.348417,7.664966,-0.576391,-6.229407,3.386675,4.136414,-7.918559,8.029349,1.263529,-2.013127,-5.513911,0.202328,-2.050885,-6.257524,6.389629,-8.480719,-8.087101,2.916183,9.255120,3.965539,6.393273,6.742195,-3.007962,7.318292,4.668944,2.574958,2.039794,-9.056396,2.578772,-7.833544,-0.066550,-5.298916,-7.825066,9.510476,9.121128,-5.626980,7.071620,-0.574205,-1.524785,-1.714926,-3.771954,-1.671698,-5.082140,4.728852,4.812689,-2.829148,3.316705,-2.681008,-5.751419,4.835082,-0.546629,-0.991181,9.911090,0.629834,-2.547076,7.271722,-7.943914,-0.557289,-8.250545,-5.524236,7.962767,-1.917496,2.799487,-5.638894,-7.392378,1.021530,8.662254,5.715219,2.735981,1.266448,-7.101498,-4.225607,-1.078295,6.287955,-6.748720,-1.401728,-8.940057,-9.708590,4.335712,0.725291,-5.384039,-0.610962,3.032411,2.149151,8.309777,-3.174416,6.817461,-9.571231,-3.598507,1.106825,7.365346,-3.660505,-9.076474,8.517867,-3.301766,3.891634,9.133928,-9.159206,8.836182,8.420186,-7.271722,-9.054424,-1.684519,3.425343,-2.200888,-0.681431,-5.799276,4.578962,8.916193,-3.139836,-7.215471,4.267127,-7.996232,-1.916370,8.117241,-7.774349,1.706929,6.373958,2.971324,-2.476936,5.587161,4.732499,-0.545739,-3.184806,9.929151,8.659687,3.264375,0.638120,-0.220491,5.333006,-0.111566,-9.741529,9.130870,3.350418,-2.426841,-0.560010,-3.863418,-5.403379,1.594299,7.576395,2.141603,-3.105458,7.790276,-7.455794,3.788169,3.724448,9.791667,8.958442,7.271721,4.006776,8.342703,-5.467243,0.803907,-7.756902,5.722537,0.224835,-3.433774,6.044047,-6.039482,8.772179,-2.317239,7.475988,-9.167752,-0.562962,4.535919,-9.574170,0.813996,2.167913,3.865954,8.627015,7.927023,6.542474,-5.301997,0.163289,3.564745,-8.736617,2.143052,0.799958,6.806926,7.931356,-0.277653,8.112913,-9.012829,-2.158362,-0.736708,4.834403,6.620029,2.860789,2.795996,-4.161829,3.623565,-5.222851,-6.681487,1.556460,9.393051,-0.985551,-1.385617,-0.731828,-4.208868,-8.990256,-4.812505,-6.354042,-3.531145,-7.436410,-7.386058], dtype = "float32")#candidate|4851|(320,)|const|float32
var_4852 = relay.var("var_4852", dtype = "float32", shape = (672,))#candidate|4852|(672,)|var|float32
var_4853 = relay.var("var_4853", dtype = "int32", shape = (180,))#candidate|4853|(180,)|var|int32
const_4854 = relay.const([4,4,-10,-9,-7,-5,7,3,-10,2,-5,-4,-3,5,6,9,-6,7,-8,-3,1,-7,7,-6,4,6,10,10,-2,5,7,-7,-6,10,-1,2,2,-2,9,5,-6,5,-1,-1,2,-3,1,1,-4,-3,4,9,-5,5,1,-9,1,4,1,-4,-3,-9,9,-2,-10,10,-2,-10,-1,3,4,-8,-8,-6,-10,-9,9,5,-9,-1,-4,5,-9,1,1,-2,5,-2,4,1,10,7,1,9,1,-9,10,-10,-10,-1,-6,9,-6,-6,1,-6,-9,-2,7,10,-1,2,4,2,-5,-6,7,4,-6,-4,8,-10,5,7,3,-9,-6,-8,4,-4,-3,2,8,3,-6,1,-9,1,4,5,3,4,4,10,1,9,-6,4,-4,-10,-8,-4,-3,-2,-1,4,10,5,-9,-1,3,-4,10,-5,-7,-5,-5,3,-4,-4,-1,-2,8,4,-4,-6,7,-8,-8,-3,7,1,9,-1,-8,-1,-7,1,-10,-1,-3,3,-8,9,3,2,-2,-3,6,7,3,4,-8,-3,1,-7,2,-6,-3,6,-9,-10,-1,3,7,1,7,-9,-2,5,6,-10,6,-9,-3,8,5,-4,-9,4,-8,-7,2,-9,-8,-10,8,5,9,4,-10,5,-8,-2,5,-6,-10,-7,-9,-9,-3,-1,10,-7,-9,1,3,5,-5,2,-4,7,1,6,-10,-7,3,-4,-2,-4,-1,-10,-2,-10,3,-1,10,1,-9,1,4,-2,4,10,8,8,-8,6,5,-9,7,7,5,9,7,-5,10,7,-5,1,-2,3,-7,-2,-4,-3,10,-10,-10,-8,1,-9,1,6,-7,-9,7,-9,-8,9,1,-5,-5,-5,-6,-3,8,-7,-2,-5,1,7,6,2,-8,-8,-6,1,7,-6,1,-9,3,-8,-10,-3,-8,9,-8,-8,6,7,-8,-1,4,-8,-7,4,5,-5,6,8,-8,-6,9,-3,9,-7,10,-3,-5,1,-10,-10,-6,1,-2,-6,5,-9,7,9,3,2,-4,-8,-6,9,-4,2,-5,-2,2,-1,9,3,-1,-1,-8,8,7,-3,6,10,2,-4,5,-7,-5,3,-8,1,9,-4,4,-1,9,-8,7,-9,-2,-7,8,-1,2,-6,-10,-10,8,8,-7,6,2,-2,-2,7,3,-10,-9,3,-6,-4,5,-7,-9,6,-3,-9,-6,5,4,-3,-7,-8,-5,2,2,-2,-1,2,4,-3,10,-4,-4,6,1,7,-4,8,7,-5,-7,6,5,-9,7,6,5,8,8,-9,5,9,-10,1,9,6,2,-8,-3,-6,7,10,3,-3,-1,-10,-8,-8,-7,8,4,4,8,-4,6,-1,-5,7,10,7,-4,-8,7,5,-4,2,8,5,-9,-7,1,10,-3,-2,-10,-4,9,7,7,-1,-4,8,-8,-8,-2,-2,6,-8,2,2,10,-6,-6,-6,6,4,8,-2,3,-5,-6,7,-10,1,-5,-4,8,6,3,-7,-7,9,-10,-4,-10,9,6,9,9,10,2,-8,3,4,-4,-7,3,8,6,8,1,-3,3,4,4,5,9,-8,-7,-10,-5,-4,4,4,4,-7,1,-3,-4,6,3,5,5,6,-4,-5,-5,9,-8,9,-9,6,-8,4,-8,-1,-4,-4,-8,2,-7,4,3,9,-8,-5,5,-7,-2,9,5,-10,-4,9,3,5,8,1,-3,-7,9,8,-3,10,-9,-5,9,-1,-10,-7,4,4,-3,5,5,9,-4,-1,3,10,10,-4,3,-2,-10,7,-2,5,-5,-1,4,6,8,-3,-1,-3,-10,-10,6,5,2,7,-2,9,-5,-10,10,-7,5,9,4,-7,-1,-9,-8,3,8,-3,-4,-8,3,-8,-5,-3,-6,4,-6,-6,7,-4,-2,4,6,-10,10,-9,-9,-7,-5,-3,-3,-1,-8,-6,6,10,6,10,1,-2,2,-5,-2,3,3,8,-3,-4,8,7,-1,-2,1,1,-3,-7,6,-4,-4,-8,3,4,-3,-10,-10,4,4,-8,-9,-10,-2,5,-7,-8,8,-10,10,-8,2,-5,-4,4,7,4,-3,-6,9,4,-2,9,-8,2,2,-4,-7,9,-10,-1,6,-2,-8,-3,4,5,10,8,4,10,10,-2,-3,-10,3,1,-7,-6,5,-3,7,-5,-3,-4,2,3,-8,-1,-4,-5,2,-4,-10,5,-2,-4,-6,3,-3,4,-3,-7,2,3,9,-2,-5,-2,-9,-2,-5,9,7,-1,-10,-6,-4,5,1,1,-5,10,1,5,-9,10,-3,-7,2,-1,-7,-7,-9,8,-10,7,3,-5,1,4,-9,8,-5,4,-5,10,-1,-4,9,10,2,-5,7,9,10,-2,2,-10,-4,-4,9,-2,1,1,-7,-9,8,-4,-6,5,-8,6,6,7,-2,9,-3,2,-7,5,-5,3,-10,10,-1,3,-3,-1,5,-7,9,8,8,-7,4,1,6,-3,-2,-4,10,-4,4,-10,-3,6,4,3,4,7,2,7,1,-6,-5,-7,8,5,-7,1,-1,-4,-10,7,7,-4,-3,8,-3,8,-5,-2,-6,-4,-2,-7,-3,8,-7,9,-2,-2,-6,-10,5,8,2,-2,4,3,3,9,-10,9,-5,-9,1,-1,-2,-7,-8,8,2,-10,7,2,-5,6,-9,1,3,-10,-3,-1,-1,-3,-3,1,-2,2,6,1,-7,5,2,-10,7,-9,-1,9,-9,5,5,7,-8,-7,5,4,-3,-7,-6,-1,-7,7,-1,1,9,3,-1,9,1,4,4,-7,-8,3,3,10,4,-9,-2,-6,6,4,2,-9,-9,-9,10,9,2,3,-8,5,-10,7,-5,-4,-4,2,-2,-9,3,-6,-3,2,-9,-1,10,8], dtype = "int32")#candidate|4854|(1080,)|const|int32
var_4855 = relay.var("var_4855", dtype = "uint64", shape = (896,))#candidate|4855|(896,)|var|uint64
call_4849 = relay.TupleGetItem(func_2561_call(relay.reshape(const_4850.astype('float32'), [9, 16]), relay.reshape(const_4850.astype('float32'), [9, 16]), relay.reshape(const_4851.astype('float32'), [320,]), relay.reshape(var_4852.astype('float32'), [672,]), relay.reshape(var_4853.astype('int32'), [180,]), relay.reshape(const_4854.astype('int32'), [1080,]), relay.reshape(var_4855.astype('uint64'), [896,]), ), 7)
call_4856 = relay.TupleGetItem(func_2569_call(relay.reshape(const_4850.astype('float32'), [9, 16]), relay.reshape(const_4850.astype('float32'), [9, 16]), relay.reshape(const_4851.astype('float32'), [320,]), relay.reshape(var_4852.astype('float32'), [672,]), relay.reshape(var_4853.astype('int32'), [180,]), relay.reshape(const_4854.astype('int32'), [1080,]), relay.reshape(var_4855.astype('uint64'), [896,]), ), 7)
bop_4860 = relay.multiply(uop_4824.astype('int32'), relay.reshape(var_4823.astype('int32'), relay.shape_of(uop_4824))) # shape=(2, 8, 14)
const_4866 = relay.const([4,-6,9,-3,-6,-4,6,-3,7,9,3,-2,-5,3,-8,-4,8,-7,6,4,5,-2,5,7,7,-4,3,5,-6,-10,1,9,7,-6,5,8,-7,2,-8,-8,8,7,-7,9,-3,10,-4,3,6,-6,-1,-1,-5,-4,6,9,-3,-5,-3,6,3,9,-6,1,-4,-4,-9,5,10,8,1,-9,-6,-5,-9,4,-8,1,5,-7,-9,4,-6,2,10,3,7,-8,-6,-3,-5,-7,8,-6,-10,-2,3,-6,6,-6,-10,-10,1,-4,-10,-2,-2,7,-8,2,5,8,-1,9,-4,6,6,-5,-3,-3,-3,-9,5,6,-8,-3,2,2,-8,1,-8,10,-2,-10,-1,1,10,-9,-3,-10,3,5,-7,-1,2,10,8,5,-2,-6,-7,-7,4,-4,2,9,9,1,2,4,-3,-3,2,-10,2,9,2,8,3,6,-8,-9,10,7,-3,8,-5,6,9,-4,-3,-2,-9,2,6,5,4,5,5,7,-2,5,-6,-7,-6,-9,3,5,-4,6,-4,6,-7,1,-10,2,-3,-1,8,5,-10,5,6,7,-7,-1,-4,-9,5,-2,8,9,1,-2,10,4,-2,3,-9,1,3,-8,-7,7,7,-9,1,10,-9,-2,-10,9,7,1,4,3,3,6,8,-4,-1,4,2,-6,6,2,-4,7,4,-7,-1,-10,2,6,7,7,-2,2,6,-7,-5,6,1,-3,5,-7,-2,1,-1,6,-7,-6,5,-5,5,3,2,-1,5,9,-4,8,-3,10,6,-2,10,-3,5,5,-1,-1,-10,-7,-6,6,-3,6,3,-10,1,-5,-1,5,8,7,10,4,10,-6,-8,-6,7,6,7,3,7,10,-6,-3,7,-4,8,9,-9,-6,-7,9,6,6,-1,-3,6,-8,8,-7,-1,-6,-10,1,-1,-10,1,6,3,3,10,-4,-9,1,4,-6,10,8,-8,3,5,-10,1,6,-8,9,2,8,-8,1,-4,10,9,-6,-8,8,10,-2,6,6,4,3,1,-9,10,-4,9,10,4,6,-5,-5,-4,6,4,3,-7,6,-10,10,7,4,-10,3,-10,-5,-7,8,7,1,-7,-1,-5,-6,-2,-2,-2,4,-3,-5,-7,-6,3,6,-9,3,-3,2,-1,-2,-5,-1,-3,9,3,-6,6,-7,-7,9,1,-2,8,2,-2,-2,9,2,-8,7,-6,-2,-7,1,1,10,4,6,-7,1,3,6,7,-3,10,-8,4,-9,8,-5,-10,3,-10,-5,-7,8,-10,-1,4,-3,5,3,1,10,-1,-2,-3,-6,4,-2,8,9,4,-4,-4,-7,10,8,-3,5,-7,-7,-2,3,-4,4,-5,-9,-5,-9,2,9,5,5,10,-2,-5,-7,-1,2,7,7,-3,3,9,-8,-8,-3,6,1,-8,-3,1,9,-2,7,-8,-1,9,8,6,9,5,-6,-1,-7,9,1,1,2,-2,-3,1,1,10,10,-7,9,-2,-5,4,-2,-3,3,-3,-9,3,-5,-8,6,8,-5,4,7,10,9,-5,5,5,1,-2,-5,4,9,6,1,9,9,9,9,9,3,10,9,5,-5,4,-4,-10,2,8,2,-1,-3,8,-10,-10,8,-1,7,-10,-7,-2,3,-3,8,10,1,2,2,5,-4,4,-7,2,3,6,-6,-10,-10,6,4,-9,-5,-8,10,8,-10,-7,-9,3,-3,-3,-9,10,6,1,-1,-5,-3,5,6,-7,-8,-3,5,1,7,7,-9,-7,-4,-2,-1,3,-10,5,-2,2,1,8,-1,6,-5,6,-1,-8,3,7,-9,-8,-9,-4,-7,2,2,-6,3,5,-4,-1,-7,-7,10,-6,6,-9,9,5,-2,6,1,8,-3,-1,5,-1,2,3,-3,1,3,4,3,-7,-8,-8,-4,-2,-1,-3,4,9,3,-8,-10,-8,10,2,3,8,-4,-2,-7,5,-7,4,-4,7,-4,-6,7,7,7,-1,-1,-4,7,3,-10,4,9,-1,3,-2,5,1,-1,-9,8,-9,-1,3,-10,-4,5,10,-7,6,-8,-7,6,9,4,8,-8,-2,1,-6,2,-3,-7,-2,3,4,-8,-8,-7,-4,5,-5,-2,-1,-4,5,-7,4,3,-10,-6,10,3,10,7,3,7,-4,-4,-1,-1,4,-7,6,6,6,10,10,6,-3,6,-4,3,2,-2,-8,3,5,-2,-10,6,-4,2,10,-4,2,9,2,3,-3,-1,9,3,-4,2,-7,9,-7,-7,-10,9,10,-7,4,-10,-4,8,-7,-5,7,-4,-10,-8,-6,1,6,2,-2,10,-9,-10,1,6,8,8,1,-4,9,-7,6,2,9,-8,3,4,-10,4,-4,-1,2,-2], dtype = "uint64")#candidate|4866|(896,)|const|uint64
bop_4867 = relay.add(var_4855.astype('uint8'), relay.reshape(const_4866.astype('uint8'), relay.shape_of(var_4855))) # shape=(896,)
output = relay.Tuple([call_4842,const_4843,call_4849,const_4850,const_4851,var_4852,var_4853,const_4854,bop_4860,bop_4867,])
output2 = relay.Tuple([call_4844,const_4843,call_4856,const_4850,const_4851,var_4852,var_4853,const_4854,bop_4860,bop_4867,])
func_4870 = relay.Function([var_4823,var_4852,var_4853,var_4855,], output)
mod['func_4870'] = func_4870
mod = relay.transform.InferType()(mod)
mutated_mod['func_4870'] = func_4870
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4870_call = mutated_mod.get_global_var('func_4870')
var_4872 = relay.var("var_4872", dtype = "float64", shape = (2, 8, 14))#candidate|4872|(2, 8, 14)|var|float64
var_4873 = relay.var("var_4873", dtype = "float32", shape = (672,))#candidate|4873|(672,)|var|float32
var_4874 = relay.var("var_4874", dtype = "int32", shape = (180,))#candidate|4874|(180,)|var|int32
var_4875 = relay.var("var_4875", dtype = "uint64", shape = (896,))#candidate|4875|(896,)|var|uint64
call_4871 = func_4870_call(var_4872,var_4873,var_4874,var_4875,)
output = call_4871
func_4876 = relay.Function([var_4872,var_4873,var_4874,var_4875,], output)
mutated_mod['func_4876'] = func_4876
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5079 = relay.var("var_5079", dtype = "float64", shape = (8, 4, 5))#candidate|5079|(8, 4, 5)|var|float64
uop_5080 = relay.atanh(var_5079.astype('float64')) # shape=(8, 4, 5)
func_2561_call = mod.get_global_var('func_2561')
func_2569_call = mutated_mod.get_global_var('func_2569')
const_5084 = relay.const([8.782751,7.546429,-3.893305,-0.820897,8.501262,-2.080911,-9.893933,3.884228,8.882544,7.430196,-7.641926,1.134710,-2.190697,9.319632,1.640594,4.224306,-6.672009,3.591606,7.083674,3.955008,-7.732276,-6.445385,8.494387,-5.337794,5.689460,1.484691,-6.584869,3.355128,9.464071,-0.839873,3.554467,-0.053770,1.197918,-4.818329,7.884756,0.488361,0.208884,4.144965,7.416617,5.210593,8.371988,-5.920009,-8.526138,-0.091169,-0.246912,-7.534648,-4.866039,3.887307,-2.600158,-9.540796,-2.405532,-6.575912,-5.712322,-6.508492,2.412377,-3.459910,9.483781,4.876643,-5.299130,1.529667,-7.801441,-6.167170,-7.793047,-8.975631,5.226916,6.162672,-3.329052,-5.796231,0.466581,-3.331705,-0.378783,7.983844,-1.819464,0.591541,-2.407773,7.906504,-1.386058,7.892047,-3.766159,-6.859615,-3.592322,1.403611,7.763895,6.626073,-7.379992,7.906554,-2.277845,-2.200267,5.446914,3.021019,6.451468,9.139286,-5.574989,-0.803105,-1.542440,8.212049,-4.567124,-7.038188,-4.365373,-5.032286,4.494462,2.993177,-5.510693,-8.315473,-7.881828,4.573796,0.349681,9.699803,3.097998,-5.303852,-1.963300,6.458792,-9.492186,-6.272349,9.867692,1.587464,5.325531,1.733982,0.543952,1.256265,1.576799,2.860771,0.393233,9.348345,-4.462525,9.084617,6.404441,-9.368407,-2.124203,-3.786651,3.976960,-9.454222,-0.324325,3.451320,-3.708699,7.366566,1.764308,-9.853106,-4.225076,-0.236909,1.579907,7.927208,-7.666190,-7.883477], dtype = "float32")#candidate|5084|(144,)|const|float32
var_5085 = relay.var("var_5085", dtype = "float32", shape = (320,))#candidate|5085|(320,)|var|float32
const_5086 = relay.const([-1.269532,9.007652,2.926290,-7.865357,-0.310082,5.171907,-3.631339,-2.274297,6.306284,7.115125,6.298847,-3.346171,5.081552,-6.562434,9.581725,6.427264,4.635781,-1.088937,-8.320082,-1.782478,6.959567,1.123069,-8.874766,1.102627,-9.202176,0.224178,5.194632,2.263618,9.751093,3.267289,8.057220,-0.761989,-5.674767,7.615232,-5.990186,9.551873,9.651789,1.382895,-3.471331,5.071993,7.982631,-9.303803,-4.355791,5.265345,6.073795,-4.841536,-5.213295,-1.702993,5.729819,7.706220,0.247232,5.671457,9.772267,6.997576,-6.722645,-4.497840,8.690215,-1.832865,-7.417552,4.082656,5.978103,-3.014011,4.787562,-4.626286,-1.080711,-3.782538,-5.533920,-2.407128,-4.245047,5.762983,-9.430491,-0.073740,-9.954734,7.048637,-6.520849,-2.822175,7.410880,6.817764,9.683543,5.320785,8.531858,-2.769413,-3.548775,1.060187,-7.977416,2.646140,-9.159172,-8.577609,-7.931687,-9.543187,0.554596,-1.756360,3.954108,0.900334,2.017059,9.044512,-2.024332,-9.678464,-4.041953,1.492048,-7.507276,-3.420932,-2.554489,4.039324,-3.368072,9.917920,3.175327,-5.904975,-6.580634,9.809132,6.491757,-7.935654,-8.526594,-5.460211,4.495694,1.398321,-4.892285,-7.618540,8.017161,1.392512,2.746371,5.444476,4.765210,-4.095904,3.665339,3.060662,-9.313823,-1.233606,0.844959,7.222960,-0.421174,-9.605707,-2.722383,5.443601,0.954770,-1.744603,3.929705,3.995079,1.851060,-1.802009,8.088304,9.469483,-5.428667,3.057700,-0.967342,-7.769751,6.857471,8.189128,1.062192,3.696791,-2.045614,-7.693102,9.770434,-4.980458,5.156496,2.818685,-1.173612,-3.308224,-7.075556,-2.019440,-3.890269,7.132044,-2.815214,-4.587784,8.858391,-3.355195,1.797486,-0.246575,-9.715299,0.687640,9.931726,-4.843293,-8.829826,-1.975106,-0.552683,4.826829,0.560101,0.885182,-9.930373,-5.887342,2.303530,2.833686,1.263627,-3.499016,-5.467334,0.865864,-0.684932,8.013590,-8.113474,-2.779456,6.197806,6.645920,-8.611707,-5.683272,-7.079682,0.992831,8.500821,-6.387727,-2.082174,-1.522082,0.548263,-5.463677,6.378250,-8.802089,-9.430893,9.017825,-9.489936,-0.476209,7.302891,7.816681,9.248820,7.957239,3.606400,8.468255,-6.540588,-5.154328,1.002433,-4.438921,4.910023,-8.054782,4.275073,8.105835,3.190979,-4.210124,-0.124019,-6.407467,-5.655324,-0.535934,-9.865319,2.716802,5.953687,-0.826563,1.151987,8.673016,7.527971,-0.571809,8.127131,-4.894894,2.940602,8.850231,5.940993,-7.972438,-8.990096,3.147275,-9.215091,2.656771,8.986532,8.787795,-2.566147,4.191527,-5.816935,-0.652438,7.474698,-3.904430,-5.006608,-2.240479,-0.107699,6.366420,7.198755,7.878500,-1.952578,3.547500,-6.509522,-5.705458,7.883426,-7.688344,9.830210,-8.807172,9.257145,1.888319,-6.403394,5.986812,-7.829016,6.889975,-9.665159,-7.086387,-0.194474,-7.922212,-3.928123,7.541356,-0.954189,1.796773,6.209564,-6.477227,9.474321,-3.511596,5.430608,-4.616107,-5.763109,9.087280,-9.416599,4.129055,4.697815,2.954812,-4.907967,1.845572,-9.724991,-2.661416,-0.507499,-0.648770,2.043653,-4.679023,8.322628,-0.191728,-3.675204,-1.164656,1.216006,1.960137,5.745962,-4.710442,-6.917415,-5.671326,3.562828,-3.323333,8.240576,7.113869,2.670368,6.019831,-1.044196,-3.758622,3.804596,6.127015,8.899693,0.168574,4.408084,-2.516340,6.599986,-3.382680,-0.406611,2.291070,5.318719,-2.578474,-2.917316,5.529494,6.232008,7.750048,-6.044328,-9.931542,-8.632410,-2.946728,9.206485,4.419441,1.699181,9.701948,-6.800910,9.801923,6.153141,-5.309690,2.690082,-7.906623,0.777796,0.109671,-8.242229,4.316194,4.573756,-9.417727,6.724020,-0.344128,7.371380,-9.343983,-3.328586,-8.090742,6.208702,7.941852,-8.737996,0.251215,7.072386,-0.115963,-7.039165,-0.711218,9.549428,8.380148,-2.231037,-9.200155,2.129796,5.343548,-0.545122,-5.437327,-0.484462,1.056566,7.799719,7.726232,9.537622,2.419149,2.413819,-7.109580,-0.059274,4.755915,1.184433,3.492120,-4.536501,-7.174092,-4.034012,-0.208694,-2.045025,5.979232,8.383054,-1.955240,-6.151899,-5.773385,-4.485468,8.005638,-8.899149,3.592045,-8.140630,0.192153,-2.681758,0.333648,-3.899604,4.380381,1.474235,-5.879584,9.537182,-5.197615,-4.570928,-6.071083,0.228699,-7.616316,-8.868665,8.580420,-3.975613,-2.027019,-3.897839,8.444929,1.716398,7.702239,6.997274,8.296674,-8.876902,0.087417,6.668614,1.032235,9.045811,-8.010656,-7.744208,-2.636388,-3.991143,8.047165,-1.967574,5.493160,6.704474,0.023283,3.888577,-9.199719,-1.331500,-9.272823,0.041577,-5.315641,7.116881,-3.977496,-7.584987,-7.466375,9.190403,7.868683,-6.819697,-6.020700,6.557581,9.998555,-0.506265,-5.176087,0.768129,-0.465166,1.868032,2.680184,-6.442549,-2.027508,-4.855954,3.926146,-5.466061,3.483272,-1.130342,-0.785195,3.209869,-7.587923,0.507374,-9.324203,9.590239,9.475576,6.478147,-7.834310,1.195829,-7.844617,5.303422,9.736195,-9.475863,9.388460,-4.650706,-0.583065,9.112852,-5.077964,-4.887781,5.880937,9.482155,-6.135193,8.852546,-2.229526,5.718828,-1.230875,6.886105,-7.467439,-3.213731,-7.278664,4.078332,5.260718,9.653144,-7.922405,-2.577856,7.230920,-0.779690,6.362086,-4.454971,-8.278827,-9.834612,7.015929,7.031287,-2.567680,8.014512,-4.006077,6.138601,1.323767,4.577530,-3.622702,4.248280,-6.315532,7.942215,7.026442,9.371404,6.368258,-2.917786,5.367266,-3.148800,5.347931,-3.618602,2.746461,0.323892,-2.767830,-1.389507,0.854991,6.094414,9.504576,7.375707,-3.493139,5.179247,-1.896051,-7.104130,3.410547,3.643146,-2.912304,-8.169580,-8.186691,-4.536840,3.229685,4.524125,-5.485807,-7.578990,-2.199974,-9.346959,-2.726052,-2.804601,4.070950,6.245990,-2.240113,-6.041395,-8.427913,-0.317180,-1.142646,-9.063416,8.584352,-9.364876,-6.702673,9.010081,-8.425142,2.710010,4.075743,-5.687854,4.334585,8.841250,-4.282769,-2.428220,0.141438,5.421204,-6.574984,8.814804,-2.528929,2.475992,-7.195695,6.776068,3.042042,9.938775,-7.089108,7.417463,8.015937,8.205115,-0.123376,3.906468,-7.799406,-6.322440,-6.384702,-1.761071,7.962343,6.394982,9.499103,8.441239,0.651097,2.732792,-6.276996,8.035913,-0.387907,0.644921,5.485736,-1.057186,-8.191385,-4.874781,-5.625487,7.057319,-4.952975,7.559700,0.005790,-7.326614,1.100198,-8.590489,9.740004,-2.232386,4.206807,-2.113073,-8.519955,-5.558410,1.497247,5.098663,-9.949022,-8.892821,8.717142,-6.316040,-8.895869,0.191829,-9.940031,1.526376,-7.250037,0.577257,0.278666,-2.276494,-8.993928,-8.596588,8.124132,5.076485,-5.922163,-3.431427,4.383690,-2.147018,-9.863587,-3.189798,-6.416252,-4.205735,8.073006,-0.765103,0.145272,-1.652380,5.768054,-5.293072,-6.698179,-4.551904,4.303219,-2.806410,5.649992,-8.825264,-1.121052,6.452655,-9.303245,2.192297,9.640838,-9.843946,-6.737696], dtype = "float32")#candidate|5086|(672,)|const|float32
const_5087 = relay.const([[3],[-2],[1],[-5],[8],[-5],[6],[9],[9],[8],[10],[7],[-6],[9],[-4],[-7],[-2],[-7],[10],[3],[1],[-8],[10],[-4],[3],[6],[2],[5],[8],[1],[2],[-8],[8],[7],[-9],[-5],[8],[7],[3],[8],[-5],[-1],[-8],[6],[2],[-7],[-7],[9],[2],[3],[-4],[-2],[-4],[-2],[-10],[4],[7],[-4],[-2],[2],[-10],[-8],[-5],[10],[1],[-1],[-6],[1],[3],[8],[6],[-1],[-9],[-9],[-7],[-7],[-1],[2],[10],[-5],[9],[-9],[-10],[6],[4],[9],[8],[-4],[-6],[10],[-3],[8],[1],[-9],[-4],[-3],[-2],[-8],[3],[-6],[-8],[6],[4],[4],[2],[-1],[2],[10],[-1],[-4],[3],[8],[2],[-8],[9],[-3],[-8],[2],[-10],[1],[-2],[-10],[6],[-6],[6],[2],[9],[-7],[-7],[7],[6],[1],[-10],[7],[1],[3],[-2],[6],[10],[-5],[-1],[-8],[-8],[-1],[-9],[-8],[-8],[-10],[-6],[-8],[4],[-8],[2],[-2],[-5],[-1],[-5],[-5],[5],[5],[4],[-8],[6],[1],[-4],[7],[-10],[-2],[-9],[7],[3],[-10],[-10],[-1],[-3],[-8],[2],[1],[5],[-10]], dtype = "int32")#candidate|5087|(180, 1)|const|int32
const_5088 = relay.const([[10],[8],[1],[-1],[9],[-5],[8],[9],[-5],[-2],[-9],[5],[4],[6],[9],[7],[-6],[-5],[-2],[-3],[-4],[-8],[-2],[-6],[-3],[9],[7],[9],[2],[-3],[1],[-2],[8],[4],[-2],[9],[-5],[-2],[-5],[3],[-9],[1],[8],[7],[-7],[-3],[-4],[-3],[-10],[2],[-4],[-10],[9],[6],[-10],[-1],[3],[5],[2],[-1],[6],[-7],[-7],[-3],[-9],[-1],[-8],[-4],[10],[-1],[10],[9],[4],[3],[8],[6],[10],[-4],[-6],[-5],[6],[10],[6],[-10],[-3],[-7],[3],[-6],[-2],[4],[5],[-3],[5],[-3],[6],[8],[6],[5],[1],[6],[-6],[-8],[-1],[-7],[-3],[2],[-5],[6],[-4],[-1],[-9],[-4],[6],[-4],[-5],[-10],[5],[2],[-2],[10],[2],[-7],[1],[-6],[-2],[-7],[7],[-5],[9],[9],[-2],[-4],[9],[-5],[-5],[-10],[1],[5],[-1],[-6],[2],[-6],[-5],[2],[-10],[9],[-2],[-9],[1],[1],[2],[-6],[-9],[4],[-3],[-4],[6],[-6],[1],[-6],[-2],[3],[9],[4],[7],[-7],[-9],[10],[3],[-7],[-6],[3],[-1],[4],[10],[-2],[-6],[6],[-6],[-5],[-6],[-10],[3],[-2],[-5],[5],[1],[7],[9],[-3],[3],[3],[10],[-3],[10],[7],[-10],[10],[6],[2],[-10],[-5],[4],[-3],[3],[-4],[-3],[4],[-4],[8],[-8],[-9],[-10],[4],[10],[9],[2],[3],[6],[-9],[-5],[-7],[-9],[10],[1],[9],[-2],[8],[9],[10],[-7],[-1],[5],[-6],[-3],[-1],[-9],[-7],[-1],[-4],[-6],[10],[3],[-2],[9],[2],[-2],[-6],[1],[7],[-7],[4],[-9],[6],[1],[-10],[5],[5],[-7],[2],[8],[3],[-9],[7],[1],[7],[4],[-7],[4],[3],[-3],[2],[-3],[8],[3],[-6],[-4],[-3],[10],[-4],[-3],[10],[-4],[-10],[-10],[6],[4],[-3],[-5],[6],[1],[-1],[3],[-9],[-1],[3],[-7],[1],[1],[10],[4],[5],[3],[6],[-1],[6],[-8],[-8],[-8],[-3],[3],[2],[8],[9],[-7],[-1],[6],[1],[-3],[7],[-3],[5],[-9],[-10],[1],[7],[9],[4],[-5],[9],[4],[4],[-3],[7],[-6],[-2],[-7],[-8],[-2],[-5],[-4],[-7],[-2],[-10],[-3],[-10],[6],[-5],[1],[-9],[-8],[3],[7],[-4],[-2],[2],[-9],[-8],[-9],[9],[-7],[9],[3],[6],[-7],[10],[-3],[-3],[-8],[9],[-5],[-7],[1],[9],[-4],[-4],[-5],[6],[-8],[-3],[-7],[-2],[-10],[3],[3],[-10],[-5],[7],[2],[6],[2],[7],[-2],[7],[-7],[-4],[-5],[-5],[1],[-5],[-9],[5],[9],[2],[5],[7],[7],[-7],[9],[8],[8],[8],[-10],[10],[-10],[8],[-7],[-5],[-4],[-8],[-4],[-10],[-1],[1],[-3],[-3],[5],[-4],[-6],[-8],[9],[-6],[-8],[5],[-8],[5],[-9],[5],[4],[-9],[-9],[7],[6],[8],[-6],[-8],[2],[-3],[7],[-6],[-2],[10],[-8],[1],[-3],[8],[-3],[-7],[-6],[2],[-1],[9],[6],[-6],[2],[9],[3],[-5],[-4],[-2],[7],[10],[-4],[-10],[4],[-4],[-2],[-8],[7],[-1],[-6],[-2],[10],[1],[-6],[-3],[-2],[2],[2],[8],[-3],[8],[-7],[4],[-2],[2],[-7],[-8],[-4],[9],[1],[-2],[6],[9],[-5],[1],[9],[-7],[-10],[10],[-8],[-10],[1],[-10],[-5],[4],[2],[9],[1],[6],[-4],[5],[-8],[2],[5],[-8],[6],[-8],[5],[1],[-10],[8],[-2],[-1],[-6],[8],[2],[5],[-8],[-8],[9],[-6],[5],[2],[-1],[-2],[10],[2],[-6],[5],[-8],[1],[-8],[1],[-3],[9],[-4],[-7],[-8],[-9],[-3],[-9],[-10],[5],[5],[-7],[2],[-6],[6],[8],[-6],[-3],[5],[-9],[10],[1],[8],[4],[-4],[3],[8],[-4],[-10],[5],[-10],[5],[-4],[-8],[8],[-10],[-7],[2],[5],[-5],[-7],[-2],[-10],[7],[9],[-6],[-7],[-4],[-1],[7],[-10],[-10],[2],[-4],[9],[7],[8],[3],[6],[-10],[4],[-3],[-8],[9],[7],[-9],[-5],[-6],[10],[-3],[7],[-7],[9],[-5],[-3],[-9],[2],[7],[7],[9],[4],[-3],[-6],[5],[8],[7],[7],[-2],[-5],[1],[-1],[-3],[2],[-3],[10],[5],[10],[2],[-8],[2],[-6],[-3],[2],[-1],[-2],[4],[-3],[-4],[-9],[-6],[-9],[-2],[10],[2],[4],[5],[-4],[2],[4],[4],[-6],[-9],[5],[5],[-10],[-2],[1],[-7],[9],[-10],[5],[2],[-6],[7],[8],[7],[-8],[-2],[-2],[9],[-6],[-1],[7],[10],[9],[-9],[-7],[-6],[-5],[-4],[4],[6],[10],[5],[5],[-3],[4],[-9],[-4],[-7],[9],[7],[-8],[9],[-6],[6],[-6],[2],[-10],[-5],[-2],[7],[-4],[9],[3],[1],[3],[-8],[-1],[-2],[-9],[6],[3],[-9],[-4],[10],[-5],[-4],[-1],[-7],[8],[-8],[5],[9],[10],[2],[-4],[-3],[8],[-9],[-10],[-10],[4],[-4],[-6],[1],[8],[-4],[3],[9],[-7],[-3],[1],[7],[1],[2],[5],[-4],[6],[5],[-8],[8],[8],[-9],[5],[6],[-10],[2],[-6],[1],[-5],[9],[-6],[10],[-3],[-6],[5],[-9],[5],[-4],[5],[-2],[-9],[-6],[-3],[6],[-3],[1],[-10],[-3],[-8],[-5],[2],[6],[3],[8],[1],[3],[-4],[9],[-8],[-9],[-8],[10],[1],[-2],[-2],[-6],[3],[4],[3],[4],[-1],[6],[-7],[-7],[7],[-8],[6],[4],[1],[10],[5],[2],[7],[1],[-7],[4],[1],[-7],[4],[-3],[-2],[8],[9],[9],[2],[-5],[-5],[-2],[-2],[-2],[10],[-1],[7],[-1],[-4],[4],[7],[3],[-7],[-8],[-2],[-5],[-2],[9],[2],[7],[9],[-6],[5],[-1],[-4],[-4],[8],[7],[-10],[6],[9],[-8],[8],[7],[9],[3],[1],[6],[7],[-5],[-2],[-1],[6],[8],[4],[9],[5],[6],[-5],[3],[-6],[-3],[8],[-3],[5],[-7],[6],[-9],[-8],[10],[1],[7],[7],[9],[-8],[-7],[1],[-3],[7],[5],[3],[1],[9],[-4],[7],[9],[3],[5],[-1],[3],[7],[4],[-8],[-6],[-3],[9],[2],[-9],[-9],[8],[-7],[5],[-2],[10],[-5],[3],[-3],[-1],[-5],[5],[9],[-8],[-5],[-1],[-8],[-10],[5],[4],[4],[-1],[9],[2],[-2],[-2],[-9],[7],[-3],[8],[-1],[-2],[-8],[-3],[6],[10],[-5],[10],[6],[7],[-2],[-7],[8],[-10],[10],[-10],[-6],[10],[-5],[-7],[-4],[4],[10],[5],[-5],[-6],[-1],[-9],[-10],[9],[6],[10],[2],[-6],[-7],[-9],[-1],[-10],[6],[-9],[-8],[-7],[1],[-8],[-6],[10],[6],[3],[-2],[-6],[-1],[-9],[7],[-3],[7],[-3],[6],[-5],[-7],[-7],[-10],[4],[7],[-8],[6],[9],[9],[10],[-1],[1],[5],[-4],[4],[-10],[-2],[6],[4],[-2],[9],[3],[3],[3],[-1],[-2],[-5],[2],[-6],[3],[-6],[3],[-9],[-4],[10],[5],[7],[5],[9],[-4],[2],[-5],[-8],[9],[3],[-6],[-2],[-1],[-9],[-6],[-10],[-10]], dtype = "int32")#candidate|5088|(1080, 1)|const|int32
const_5089 = relay.const([6,4,10,-7,-3,10,-1,-3,-2,-5,7,-7,-4,-2,-5,-9,8,-3,9,3,-9,5,6,6,-2,2,-6,10,5,6,4,-2,-9,3,9,2,-1,-5,-3,-6,3,-4,-4,-10,-8,-2,2,-9,1,2,9,5,1,6,2,-10,-7,-5,-9,-3,-3,-3,7,9,3,-7,5,2,-5,-9,8,3,4,-8,6,1,-6,-6,6,2,-7,4,4,-10,-2,-7,8,10,9,4,1,7,-2,10,-10,-7,-3,1,-7,-8,9,3,-7,-1,1,2,-3,-9,3,2,4,-10,-2,-8,-1,-8,-2,-10,-4,-5,-6,-6,7,-3,7,-2,5,-9,5,6,4,8,4,4,9,-2,-8,6,-6,-6,4,-5,1,8,3,-4,7,-2,-2,-9,-8,7,-1,-1,-2,1,6,7,-10,-7,-6,-10,5,-3,10,1,7,4,-1,-7,4,10,-6,1,-9,-10,1,7,-2,4,-6,-10,5,1,10,10,7,-8,-7,8,-7,-3,8,6,-2,-4,7,9,1,-7,-7,-7,-9,7,3,-1,4,1,-4,4,9,-4,5,10,5,-6,-6,-9,7,-8,3,-5,3,-1,-4,3,-4,-2,4,2,1,4,-1,2,-10,10,-2,-10,-10,-4,-3,-10,5,5,-5,-9,-5,4,7,-5,10,10,-2,-9,-9,-9,-9,9,-2,-5,1,3,-8,-5,-5,-4,8,7,2,4,-8,-4,-3,-2,9,-2,-1,10,2,-6,6,9,2,5,1,-7,-4,5,6,-2,5,9,9,-7,5,-5,3,-8,-2,-1,4,-4,-1,-8,8,-3,-6,-1,4,-5,1,-1,-7,-1,3,4,10,-10,10,-7,9,-5,4,1,4,-6,-7,-9,-7,-5,-2,10,8,-4,-7,9,1,-5,10,3,-2,-10,8,-3,-10,7,-7,6,8,-6,-1,5,10,6,-3,-5,8,6,-5,-2,7,-8,8,-2,6,-3,6,10,7,-8,-7,-7,-6,-2,10,-5,3,3,-1,-10,-6,5,-1,8,1,10,8,-4,8,5,-9,-7,8,-6,7,-6,-8,-5,-6,-9,-10,6,6,-2,5,2,-2,8,7,8,1,6,-7,-2,-3,-9,-2,1,-4,-10,-4,4,-9,5,10,1,9,3,-8,6,-6,4,-1,-5,10,3,6,-10,-4,3,8,5,1,1,3,-1,-4,6,-2,10,6,5,-5,-9,8,2,7,-3,-5,8,-4,6,3,-5,5,-6,3,5,6,6,5,2,-5,-10,9,-8,-6,3,8,-6,-7,6,-6,7,-2,-6,3,8,-2,10,-6,-4,-5,-4,9,8,4,6,-4,2,8,-4,5,-8,-2,-6,-9,3,-1,8,8,-4,9,-4,2,10,1,10,-6,3,-9,6,-1,-3,-5,2,7,8,5,1,-6,-7,5,-5,8,-8,-8,6,-3,-4,9,6,2,-4,-5,-6,7,10,-3,-2,-4,9,-5,1,-5,10,9,-10,9,-9,10,-7,-9,9,-5,-4,-1,1,9,8,7,5,-6,-8,-2,1,-2,-9,7,-4,8,1,2,-5,-4,-2,3,-8,6,-3,-4,-10,-3,9,6,-4,3,4,-7,-6,-4,-3,-8,5,8,-2,-10,-1,1,5,-5,-6,4,4,10,2,8,2,-6,-2,5,-9,6,10,-1,-9,-5,7,-4,1,-2,-2,10,-8,3,3,4,2,3,1,8,2,-4,5,9,4,10,-2,1,7,10,1,1,5,-7,7,4,-1,8,6,3,-1,-7,-1,2,2,7,5,-7,1,-5,-3,8,9,1,5,7,-5,8,-3,-6,-2,8,-3,8,-1,4,3,-8,-8,-10,-1,9,-3,3,-5,1,-4,-7,-4,-10,-7,8,8,6,5,9,5,3,4,6,-7,-9,5,-9,-10,-5,5,8,-9,9,10,-1,7,5,-2,-1,7,1,7,-3,8,3,-9,-7,5,2,4,-2,-7,-2,-9,9,6,-10,-9,7,8,3,1,8,5,-1,5,-2,10,3,-9,-5,-4,8,-5,3,5,5,-5,1,-4,9,-4,2,-4,-3,-9,10,1,-7,10,-4,-7,2,1,-3,4,2,4,-1,-9,3,-3,1,8,-2,1,7,4,-1,-1,-8,8,-4,-6,-3,9,2,9,-6,3,-9,-4,2,4,-3,-10,1,-4,2,-9,-2,-3,2,10,-2,6,5,8,1,1,-8,-6,-10,-3,8,-1,2,-9,-7,10,9,-1,-9,-4,-10,4,-7,-4,-3,-3,-10,-3,8,5,-10,3,5,6,2,4,-6,-7,-1,9,-9,-4,7,-1,1,8,-5,5,-6,3,2,9,8,-8,-8,-10,1,8,-3,-3,-7,8,-6,9,3,-2,-1,-10,9,-5,-8,6,1,9], dtype = "uint64")#candidate|5089|(896,)|const|uint64
call_5083 = relay.TupleGetItem(func_2561_call(relay.reshape(const_5084.astype('float32'), [9, 16]), relay.reshape(const_5084.astype('float32'), [9, 16]), relay.reshape(var_5085.astype('float32'), [320,]), relay.reshape(const_5086.astype('float32'), [672,]), relay.reshape(const_5087.astype('int32'), [180,]), relay.reshape(const_5088.astype('int32'), [1080,]), relay.reshape(const_5089.astype('uint64'), [896,]), ), 8)
call_5090 = relay.TupleGetItem(func_2569_call(relay.reshape(const_5084.astype('float32'), [9, 16]), relay.reshape(const_5084.astype('float32'), [9, 16]), relay.reshape(var_5085.astype('float32'), [320,]), relay.reshape(const_5086.astype('float32'), [672,]), relay.reshape(const_5087.astype('int32'), [180,]), relay.reshape(const_5088.astype('int32'), [1080,]), relay.reshape(const_5089.astype('uint64'), [896,]), ), 8)
output = relay.Tuple([uop_5080,call_5083,const_5084,var_5085,const_5086,const_5087,const_5088,const_5089,])
output2 = relay.Tuple([uop_5080,call_5090,const_5084,var_5085,const_5086,const_5087,const_5088,const_5089,])
func_5096 = relay.Function([var_5079,var_5085,], output)
mod['func_5096'] = func_5096
mod = relay.transform.InferType()(mod)
mutated_mod['func_5096'] = func_5096
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5096_call = mutated_mod.get_global_var('func_5096')
var_5098 = relay.var("var_5098", dtype = "float64", shape = (8, 4, 5))#candidate|5098|(8, 4, 5)|var|float64
var_5099 = relay.var("var_5099", dtype = "float32", shape = (320,))#candidate|5099|(320,)|var|float32
call_5097 = func_5096_call(var_5098,var_5099,)
output = call_5097
func_5100 = relay.Function([var_5098,var_5099,], output)
mutated_mod['func_5100'] = func_5100
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5266 = relay.var("var_5266", dtype = "float32", shape = (10, 12, 10))#candidate|5266|(10, 12, 10)|var|float32
uop_5267 = relay.exp(var_5266.astype('float32')) # shape=(10, 12, 10)
uop_5278 = relay.log(var_5266.astype('float64')) # shape=(10, 12, 10)
bop_5286 = relay.subtract(uop_5267.astype('uint16'), relay.reshape(var_5266.astype('uint16'), relay.shape_of(uop_5267))) # shape=(10, 12, 10)
func_1580_call = mod.get_global_var('func_1580')
func_1586_call = mutated_mod.get_global_var('func_1586')
const_5297 = relay.const([-1,2,10,6,-8,8,5,1,1,10,-7,-5,5,-1,-3,2,7,-9,-7,-4,-1,7,6,8,8,-3,-10,-9,-10,-10,1,6,5,4,-4,9,3,-1,-1,-8,7,-6,-10,2,7,3,-5,7,6,-3,2,-6,-7,-3,6,-9,-3,-9,-2,-2,-4,-9,4,10,7,-10,5,-3,-5,-1,6,-3,5,-3,-5,-7,2,10,4,-5,3,-10,-5,9,9,-10,-9,5,7,2,5,-2,9,-10,-2,-4,4,3,8,9,3,-4,2,-6,-7,10,-2,-6,4,4,5,-3,3,-8,2,-10,-7,-5,4,-8,2,3,-10,-4,7,2,-7,2,-3,-3,-8,-9,-5,-3,-8,10,-1,-5,-1,7,1,1,6,-8,-4,5,-1,-8,-9,-7,-4,-8,-9,-7,-5,10,6,2,5,-1,10,-2,10,-9,-10,5,-5,-10,7,-7,-2,8,10,-7,1,-5,-6,2,-6,-3], dtype = "int32")#candidate|5297|(180,)|const|int32
const_5298 = relay.const([-2,-3,1,8,4,-6,-7,4,3,-6,4,5,5,9,10,8,-6,-2,4,-4,-1,1,-9,6,10,-2,3,2,-1,-8,3,-2,-8,4,6,10,-10,-9,-8,3,-8,-2,-4,-9,-7,5,2,7,-4,3,10,-1,-4,1,7,8,1,-4,-6,10,-9,-3,4,2,2,-10,-9,-5,1,-5,-2,-2,4,-9,-1,4,-8,5,-9,-2,4,-1,10,6,-2,10,5,-8,-9,9,-8,2,-2,-9,-5,1,-10,-2,10,4,8,-7,-5,2,-4,4,6,9,4,-10,-9,-8,-5,1,-6,-7,-8,-7,-1,-7,-2,10,-8,7,-9,10,-9,-6,9,-10,-2,-1,-3,-1,9,-3,10,8,-2,-9,3,-8,-10,-1,-2,3,-9,-4,3,1,3,3,-5,1,-6,-8,-2,5,1,-10,-6,6,-7,2,-8,-2,-6,4,5,-1,-8,2,-5,3,-3,-10,-9,-8,9,-8,2,-7,4,10,-9,-10,9,-10,-3,2,-9,6,-3,4,-4,-8,-2,-5,-10,-6,5,7,-2,-10,-1,10,9,6,2,-3,-2,-3,9,1,-4,-8,6,4,-4,10,9,5,-8,7,3,-6,-2,-1,8,10,-10,-2,-4,4,-3,5,-6,7,3,2,7,-5,9,-9,8,1,-8,6,-1,1,-5,-5,9,3,-9,10,-6,-4,10,2,-3,-8,9,-4,-2,-6,1,6,-5,-2,7,-10,-6,8,8,-4,6,-3,-3,7,1,-2,7,2,10,-8,-5,-2,3,-7,-1,-3,10,-1,-4,-10,-4,-7,4,-2,-3,-3,-9,9,2,-2,-4,9,-4,9,-1,-10,5,3,-7,4,-5,8,10,5,-1,7,5,-1,10,-4,-3,5,4,-7,-5,10,-6,6,-6,-9,8,-4,4,2,7,5,4,10,-10,-8,-6,6,7,-7,3,-9,2,5,-9,7,5,-10,2,7,-4,6,3,1,4,-10,4,9,3,1,3,9,-2,6,-6,-5,-8,-10,4,1,-1,-6,-2,-2,-9,6,1,-9,-6,-6,-10,5,-3,-8,-8,7,-2,4,-8,-9,-9,10,-2,-4,5,-3,2,-2,-2,-4,-1,-10,1,-9,10,5,-4,-9,5,-7,3,7,5,-10,2,-7,-2,8,-1,-4,6,8,6,8,-1,4,-2,-7,2,6,-3,9,-10,-1,-5,-1,4,-2,-9,4,3,1,-10,-6,8,-6,-5,-8,-5,7,4,2,-9,10,3,5,-3,3,7,-6,1,7,9,2,-2,4,9,6,10,-6,-2,-9,7,8,1,-10,8,-8,-3,-2,1,3,-4,8,4,5,4,3,-5,-9,5,-9,-7,1,-7,-4,-1,-10,5,6,-1,7,6,1,1,10,-9,10,-5,-5,5,3,-8,10,-1,5,9,9,4,-7,-2,-2,7,9,4,-4,-7,7,-10,-9,3,-4,7,-8,-7,-7,-3,2,-2,1,6,7,4,7,10,6,-1,8,6,-1,2,-2,7,-4,-4,5,10,-3,7,-10,-9,4,9,-8,-7,-9,-6,-5,-4,2,-4,10,-10,-2,-7,7,1,4,3,-8,-10,1,-8,7,-5,-10,7,-5,-2,-5,9,5,-5,-1,-10,1,6,5,10,3,-2,-4,-2,-7,6,-3,6,-7,6,1,7,-7,-6,4,-4,-3,10,7,-6,8,6,9,1,3,3,3,-8,2,3,-1,-5,-5,-2,6,-5,-2,-8,-3,6,-6,1,-9,-2,-4,9,1,-10,6,7,9,-10,2,-3,-5,-2,8,-2,4,-9,8,4,9,-6,-3,1,-4,5,9,3,-7,-4,-10,-3,10,-3,-2,-8,10,-10,-6,6,-1,7,7,3,7,-10,-6,3,8,6,4,3,-7,-6,-3,4,1,4,-3,5,-8,9,9,2,10,7,4,-8,10,-4,6,9,-9,-9,-3,2,-7,-5,-5,-4,-7,-10,1,-9,-2,6,-1,7,-9,2,-9,1,-7,4,3,8,-9,8,6,2,2,-8,-4,-5,-1,5,3,-8,4,6,-10,-9,3,-2,7,-9,-2,6,-1,-1,9,-2,3,7,-10,7,7,2,5,1,7,-3,-6,-7,1,9,3,4,-9,-3,2,-2,6,-1,9,-3,3,-5,6,-7,-9,6,-10,-6,-1,-10,1,-4,-10,-7,6,-3,-9,-7,2,3,2,1,-2,-1,-10,-6,6,7,2,3,8,-8,-6,-4,-10,-8,-6,4,-10,1,-7,8,-4,9,10,5,-8,5,-7,-2,5,9,3,-1,10,2,6,3,6,9,4,4,-6,-7,9,10,-3,7,-6,-8,10,-6,-9,-10,10,3,-1,9,-7,2,8,-9,-5,-7,-7,-5,-5,5,9,9,3,7,-8,-3,3,-2,-9,3,1,3,5,3,1,5,3,1,-7,-10,-5,1,-10,10,-8,-1,3,5,4,-9,7,-6,10,-6,8,-2,-3,-2,8,10,6,-2,-7,-8,-6,7,3,-6,1,-7,-10,-3,-2,5,8,7,-9,5,-8,9,2,-9,-9,7,9,-10,-3,-1,7,-6,-1,1,1,-6,-8,5,10,4,-9,9,5,8,-2,2,6,4,-2,-7,-10,-4,-9,10,-2,-9,7,10,9,9,-6,-1,-10,10,-2,5,-2,-2,-7,-2,-7,10,1,6,-8,1,6,6,7,-8,-5,-2,-9,9,7,4,2,-7,-6,5,8,9,10,-9,-1,7,-9,2,3,5,3,-3,-5,-2,-7,-6,4,10,1,10,-8,10,6,-5,-5,9,2,-3,-6,8,1,-8,-7,9,-8,4,6,3,-7,-10,-9,-8,-5,-7,-5,4,-7,3,9,-6,10,4,3,7,4,-2,-8,-5,1,-4,7,6,-10,-1,-10,-7,6], dtype = "int32")#candidate|5298|(1080,)|const|int32
var_5299 = relay.var("var_5299", dtype = "uint64", shape = (224, 4))#candidate|5299|(224, 4)|var|uint64
const_5300 = relay.const([2,10,10,-1,4,9,9,6,-7,-4,5,-5,7,-10,-1,-6,-2,10,-6,6,-4,1,3,7,-4,-6,-5,4,4,-8,-6,9,-9,-9,9,7,10,-7,7,-2,-9,2,9,3,-1,-2,3,4,-2,1,8,-5,7,-3,9,7,-6,-9,6,-10,-3,1,-4,2,-8,7,10,-6,5,-1], dtype = "uint32")#candidate|5300|(70,)|const|uint32
call_5296 = relay.TupleGetItem(func_1580_call(relay.reshape(const_5297.astype('int32'), [1, 12, 15]), relay.reshape(const_5298.astype('int32'), [6, 12, 15]), relay.reshape(var_5299.astype('uint64'), [896,]), relay.reshape(const_5300.astype('uint32'), [7, 10]), ), 10)
call_5301 = relay.TupleGetItem(func_1586_call(relay.reshape(const_5297.astype('int32'), [1, 12, 15]), relay.reshape(const_5298.astype('int32'), [6, 12, 15]), relay.reshape(var_5299.astype('uint64'), [896,]), relay.reshape(const_5300.astype('uint32'), [7, 10]), ), 10)
uop_5310 = relay.atanh(var_5299.astype('float32')) # shape=(224, 4)
output = relay.Tuple([uop_5278,bop_5286,call_5296,const_5297,const_5298,const_5300,uop_5310,])
output2 = relay.Tuple([uop_5278,bop_5286,call_5301,const_5297,const_5298,const_5300,uop_5310,])
func_5313 = relay.Function([var_5266,var_5299,], output)
mod['func_5313'] = func_5313
mod = relay.transform.InferType()(mod)
var_5314 = relay.var("var_5314", dtype = "float32", shape = (10, 12, 10))#candidate|5314|(10, 12, 10)|var|float32
var_5315 = relay.var("var_5315", dtype = "uint64", shape = (224, 4))#candidate|5315|(224, 4)|var|uint64
output = func_5313(var_5314,var_5315,)
func_5316 = relay.Function([var_5314,var_5315,], output)
mutated_mod['func_5316'] = func_5316
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5342 = relay.var("var_5342", dtype = "uint64", shape = (1, 8, 9))#candidate|5342|(1, 8, 9)|var|uint64
var_5343 = relay.var("var_5343", dtype = "uint64", shape = (4, 8, 9))#candidate|5343|(4, 8, 9)|var|uint64
bop_5344 = relay.bitwise_xor(var_5342.astype('uint64'), var_5343.astype('uint64')) # shape=(4, 8, 9)
func_1719_call = mod.get_global_var('func_1719')
func_1723_call = mutated_mod.get_global_var('func_1723')
var_5355 = relay.var("var_5355", dtype = "float64", shape = (1080,))#candidate|5355|(1080,)|var|float64
call_5354 = relay.TupleGetItem(func_1719_call(relay.reshape(var_5355.astype('float64'), [9, 12, 10]), relay.reshape(var_5355.astype('float64'), [9, 12, 10]), ), 0)
call_5356 = relay.TupleGetItem(func_1723_call(relay.reshape(var_5355.astype('float64'), [9, 12, 10]), relay.reshape(var_5355.astype('float64'), [9, 12, 10]), ), 0)
output = relay.Tuple([bop_5344,call_5354,var_5355,])
output2 = relay.Tuple([bop_5344,call_5356,var_5355,])
func_5363 = relay.Function([var_5342,var_5343,var_5355,], output)
mod['func_5363'] = func_5363
mod = relay.transform.InferType()(mod)
var_5364 = relay.var("var_5364", dtype = "uint64", shape = (1, 8, 9))#candidate|5364|(1, 8, 9)|var|uint64
var_5365 = relay.var("var_5365", dtype = "uint64", shape = (4, 8, 9))#candidate|5365|(4, 8, 9)|var|uint64
var_5366 = relay.var("var_5366", dtype = "float64", shape = (1080,))#candidate|5366|(1080,)|var|float64
output = func_5363(var_5364,var_5365,var_5366,)
func_5367 = relay.Function([var_5364,var_5365,var_5366,], output)
mutated_mod['func_5367'] = func_5367
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5768 = relay.const([[[5.391529,1.658600,3.877716,0.601112,5.264083,6.790661],[-7.130890,8.396740,2.239732,-9.718015,-4.658336,-4.141586]],[[-6.420394,4.713623,6.458584,8.754008,-4.872627,4.874676],[-7.986397,3.906593,-7.983571,-5.728423,5.998121,-4.213451]],[[-9.419157,6.965209,1.985623,2.080732,-0.729386,2.467393],[5.267158,-2.677165,7.788540,0.082459,2.529929,5.801577]],[[9.836430,-7.580205,-7.269979,-6.599945,0.930694,0.034835],[6.097741,-7.661704,5.687621,2.395719,-2.986218,-3.791880]],[[-4.197377,-2.814513,9.294194,9.724241,7.342503,5.839541],[7.823494,9.858416,4.903194,0.437378,6.617849,-8.942336]],[[5.569079,2.875928,-9.938812,4.995895,9.844908,-7.864028],[-4.217227,9.378864,7.599003,4.254623,-9.440174,3.414877]],[[1.060669,6.249855,-3.815700,7.086287,7.759048,-9.190474],[8.673987,-5.823479,7.349395,3.721969,4.232867,7.136592]],[[3.444726,4.361864,7.826040,-0.330832,9.388765,4.345346],[8.502884,-3.680274,6.811222,-7.287296,-9.600982,0.653234]],[[7.863593,8.937697,-6.414295,7.703256,9.178274,2.114159],[4.012357,6.612344,2.869714,3.558127,-2.619069,-7.442750]]], dtype = "float32")#candidate|5768|(9, 2, 6)|const|float32
uop_5769 = relay.log(const_5768.astype('float32')) # shape=(9, 2, 6)
output = uop_5769
output2 = uop_5769
func_5773 = relay.Function([], output)
mod['func_5773'] = func_5773
mod = relay.transform.InferType()(mod)
output = func_5773()
func_5774 = relay.Function([], output)
mutated_mod['func_5774'] = func_5774
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5816 = relay.var("var_5816", dtype = "float64", shape = (16, 9, 13))#candidate|5816|(16, 9, 13)|var|float64
uop_5817 = relay.cosh(var_5816.astype('float64')) # shape=(16, 9, 13)
func_1022_call = mod.get_global_var('func_1022')
func_1024_call = mutated_mod.get_global_var('func_1024')
var_5821 = relay.var("var_5821", dtype = "float64", shape = (21,))#candidate|5821|(21,)|var|float64
call_5820 = func_1022_call(relay.reshape(var_5821.astype('float64'), [7, 3, 1]))
call_5822 = func_1022_call(relay.reshape(var_5821.astype('float64'), [7, 3, 1]))
func_1128_call = mod.get_global_var('func_1128')
func_1132_call = mutated_mod.get_global_var('func_1132')
var_5826 = relay.var("var_5826", dtype = "int64", shape = (660,))#candidate|5826|(660,)|var|int64
const_5827 = relay.const([[-3,4,-8,8],[7,-7,-4,5],[10,-9,-7,2],[5,-2,3,-9],[-10,10,6,-4],[-6,3,4,5],[-3,8,1,3],[-4,-10,4,-3],[-4,2,3,-3],[9,-8,-6,-6],[-9,9,6,5],[9,-9,7,-7],[7,3,7,8],[1,-8,-8,6],[-9,-7,-8,-7],[2,-8,-9,1],[6,7,-9,-9],[2,-7,-4,-10],[-7,9,1,-2],[3,-3,-7,-10],[8,6,4,-6],[-5,-9,-8,-1],[7,-10,-6,-3],[-4,-1,1,-2],[1,-4,5,3],[5,-8,-10,7],[9,-8,-2,3],[-5,5,-8,-5],[-8,3,-1,3],[8,-8,-2,-6],[4,9,-4,10],[-9,-7,5,-5],[1,6,4,-7],[-3,-3,-9,10],[-4,9,-1,9],[-5,6,-8,-3],[-9,-10,-8,-9],[1,-8,2,6],[-4,4,-4,-5],[7,9,2,-6],[-10,-8,-3,-9],[-9,-9,-4,-5],[-9,-4,-1,-2],[-8,-6,2,3],[-8,10,6,-8],[-6,-3,1,7],[-6,3,-9,6],[3,-8,-3,6],[-10,3,-4,10],[-7,10,-3,-5],[9,-6,2,-6],[5,-1,4,8],[-2,1,-1,7],[6,-5,6,7],[8,4,7,-7],[5,-9,-3,-5],[1,2,1,-9],[9,-5,3,-2],[7,-3,7,7],[9,-1,6,-9],[5,6,-3,10],[-10,-6,-1,6],[-4,4,-10,-5],[8,1,-3,-8],[4,-4,-2,8],[1,3,-2,-2],[7,-10,-7,-7],[-1,9,-1,-4],[-5,-1,-3,7],[2,-8,8,-3],[-5,5,7,1],[10,-4,8,-7],[6,-8,-8,-5],[-4,7,4,-10],[-2,-5,6,-9],[-5,-1,-2,-4],[8,-9,8,1],[8,5,-7,-1],[9,-7,1,3],[-8,-6,3,-1],[5,-1,6,4],[-9,8,-3,4],[6,-7,7,10],[4,-8,-10,-2],[-10,8,5,4],[9,2,2,4],[-9,-4,2,-4],[1,-7,-4,8],[2,-2,7,4],[7,-10,4,-6],[6,1,-3,6],[10,9,-2,8],[2,-4,-5,5],[-4,2,10,3],[7,3,1,-5],[5,-3,-10,3],[-10,-1,7,8],[2,1,7,7],[8,-3,1,9],[2,5,4,6],[-6,10,4,5],[7,9,10,7],[7,-8,-8,6],[-1,-3,-10,-1],[-5,-10,-1,4],[-2,4,-8,1],[-1,-6,8,-8],[-3,-5,10,-1],[-9,2,7,9],[-1,-1,-4,-6],[3,-3,-6,-1],[-3,-3,-2,-6],[5,-8,7,2],[-10,9,-7,-10],[-9,-3,-5,-3],[9,-9,-10,10],[6,8,7,1],[2,3,9,2],[-6,2,-9,10],[-10,-9,-6,8],[10,5,-5,-7],[10,-6,5,4],[3,5,-10,-10],[-5,-3,-1,-3],[6,-10,-8,-7],[1,5,1,9],[7,6,10,10],[-8,-6,-5,-1],[9,-3,10,-3],[-3,-7,10,-10],[2,6,3,-5],[10,-9,-10,-9],[2,6,-2,-3],[9,-9,5,-8],[7,-7,10,1],[-5,9,3,-6],[10,6,-3,4],[6,1,-7,8],[-2,4,9,4],[-8,-1,10,3],[-1,1,8,6],[-1,7,7,-1],[2,-3,-1,-7],[1,-7,5,-3],[10,2,9,4],[-6,-9,-8,-4],[-6,-1,7,3],[6,-10,-1,-9],[7,9,-7,8],[-5,8,7,-4],[-2,-7,1,-6],[-1,7,-9,3],[6,-2,6,-10],[-6,4,4,-6],[3,3,5,-2],[-6,-8,-7,-3],[-2,8,4,9],[-8,-3,3,9],[3,9,-3,-4],[-9,-6,-3,1],[-3,-3,9,-4],[5,9,5,3],[2,-7,2,-4],[4,-9,-10,-2],[9,7,-5,5],[8,-9,2,2],[5,-8,1,-10],[-3,-1,9,-3],[9,6,-1,-8],[-5,-6,1,2],[9,3,-2,-6],[9,-8,-3,7],[-3,5,-4,-4],[10,-7,-8,-6],[-8,9,-1,-7],[-2,-1,7,4],[10,3,2,2],[-7,-4,-7,4],[-9,-7,7,1],[8,2,-7,-3],[-8,1,-6,-2],[2,-10,4,6],[8,-4,-5,4],[-4,-9,3,-9],[10,10,3,-9],[-8,3,6,7],[-3,8,-3,-3],[9,9,-6,2],[8,-2,-4,5],[-1,-5,-10,-10],[1,-10,10,-5],[-5,-10,5,-9],[-4,4,-3,9],[1,-2,6,5],[1,6,-1,10],[-5,9,2,3],[-10,-3,9,-8],[6,3,-1,1],[-6,-3,6,-4],[-2,1,2,10],[-2,-2,7,-3],[-9,6,7,-4],[-2,1,-8,1],[8,6,7,-10],[8,-1,-6,-7],[1,7,-9,-10],[-7,9,5,-7],[-1,3,-8,-6],[-8,9,-1,9],[8,-9,-6,-9],[9,-10,7,7],[10,-7,-6,-5],[2,-6,-10,5],[2,6,5,3],[-3,-8,10,-10],[9,1,4,8],[9,1,1,-7],[1,3,9,10],[8,-2,-5,-1],[4,8,7,4],[-1,5,-2,-7],[8,-9,-3,-10],[-6,1,7,-6],[5,10,1,10]], dtype = "uint64")#candidate|5827|(224, 4)|const|uint64
call_5825 = relay.TupleGetItem(func_1128_call(relay.reshape(var_5826.astype('int64'), [4, 11, 15]), relay.reshape(var_5826.astype('int64'), [4, 11, 15]), relay.reshape(const_5827.astype('uint64'), [896,]), ), 2)
call_5828 = relay.TupleGetItem(func_1132_call(relay.reshape(var_5826.astype('int64'), [4, 11, 15]), relay.reshape(var_5826.astype('int64'), [4, 11, 15]), relay.reshape(const_5827.astype('uint64'), [896,]), ), 2)
output = relay.Tuple([uop_5817,call_5820,var_5821,call_5825,var_5826,const_5827,])
output2 = relay.Tuple([uop_5817,call_5822,var_5821,call_5828,var_5826,const_5827,])
func_5829 = relay.Function([var_5816,var_5821,var_5826,], output)
mod['func_5829'] = func_5829
mod = relay.transform.InferType()(mod)
var_5830 = relay.var("var_5830", dtype = "float64", shape = (16, 9, 13))#candidate|5830|(16, 9, 13)|var|float64
var_5831 = relay.var("var_5831", dtype = "float64", shape = (21,))#candidate|5831|(21,)|var|float64
var_5832 = relay.var("var_5832", dtype = "int64", shape = (660,))#candidate|5832|(660,)|var|int64
output = func_5829(var_5830,var_5831,var_5832,)
func_5833 = relay.Function([var_5830,var_5831,var_5832,], output)
mutated_mod['func_5833'] = func_5833
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5773_call = mod.get_global_var('func_5773')
func_5774_call = mutated_mod.get_global_var('func_5774')
call_5874 = func_5773_call()
call_5875 = func_5773_call()
func_5096_call = mod.get_global_var('func_5096')
func_5100_call = mutated_mod.get_global_var('func_5100')
var_5893 = relay.var("var_5893", dtype = "float64", shape = (160,))#candidate|5893|(160,)|var|float64
var_5894 = relay.var("var_5894", dtype = "float32", shape = (320,))#candidate|5894|(320,)|var|float32
call_5892 = relay.TupleGetItem(func_5096_call(relay.reshape(var_5893.astype('float64'), [8, 4, 5]), relay.reshape(var_5894.astype('float32'), [320,]), ), 7)
call_5895 = relay.TupleGetItem(func_5100_call(relay.reshape(var_5893.astype('float64'), [8, 4, 5]), relay.reshape(var_5894.astype('float32'), [320,]), ), 7)
output = relay.Tuple([call_5874,call_5892,var_5893,var_5894,])
output2 = relay.Tuple([call_5875,call_5895,var_5893,var_5894,])
func_5899 = relay.Function([var_5893,var_5894,], output)
mod['func_5899'] = func_5899
mod = relay.transform.InferType()(mod)
mutated_mod['func_5899'] = func_5899
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5899_call = mutated_mod.get_global_var('func_5899')
var_5901 = relay.var("var_5901", dtype = "float64", shape = (160,))#candidate|5901|(160,)|var|float64
var_5902 = relay.var("var_5902", dtype = "float32", shape = (320,))#candidate|5902|(320,)|var|float32
call_5900 = func_5899_call(var_5901,var_5902,)
output = call_5900
func_5903 = relay.Function([var_5901,var_5902,], output)
mutated_mod['func_5903'] = func_5903
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5773_call = mod.get_global_var('func_5773')
func_5774_call = mutated_mod.get_global_var('func_5774')
call_5947 = func_5773_call()
call_5948 = func_5773_call()
output = relay.Tuple([call_5947,])
output2 = relay.Tuple([call_5948,])
func_5955 = relay.Function([], output)
mod['func_5955'] = func_5955
mod = relay.transform.InferType()(mod)
mutated_mod['func_5955'] = func_5955
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5955_call = mutated_mod.get_global_var('func_5955')
call_5956 = func_5955_call()
output = call_5956
func_5957 = relay.Function([], output)
mutated_mod['func_5957'] = func_5957
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5955_call = mod.get_global_var('func_5955')
func_5957_call = mutated_mod.get_global_var('func_5957')
call_5970 = relay.TupleGetItem(func_5955_call(), 0)
call_5971 = relay.TupleGetItem(func_5957_call(), 0)
output = call_5970
output2 = call_5971
func_5978 = relay.Function([], output)
mod['func_5978'] = func_5978
mod = relay.transform.InferType()(mod)
output = func_5978()
func_5979 = relay.Function([], output)
mutated_mod['func_5979'] = func_5979
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5955_call = mod.get_global_var('func_5955')
func_5957_call = mutated_mod.get_global_var('func_5957')
call_5980 = relay.TupleGetItem(func_5955_call(), 0)
call_5981 = relay.TupleGetItem(func_5957_call(), 0)
func_4870_call = mod.get_global_var('func_4870')
func_4876_call = mutated_mod.get_global_var('func_4876')
var_5985 = relay.var("var_5985", dtype = "float64", shape = (224,))#candidate|5985|(224,)|var|float64
const_5986 = relay.const([-2.973579,8.378474,-9.685435,2.551626,-2.091135,0.620105,7.716203,-1.931548,-3.462853,0.371326,-9.555840,0.295263,-9.933818,-0.476618,-0.690503,7.968428,-7.198701,3.853733,-2.894557,4.208267,7.967563,-4.982344,7.101189,5.937221,-4.347035,9.822052,6.851150,9.831023,1.819276,2.366566,4.875189,-3.220153,5.029142,-2.202526,-7.689018,-2.949511,6.195417,-7.723963,-0.511825,-7.651064,1.889404,3.188827,-0.650421,-2.298724,-3.743180,-6.127240,-4.867160,-4.018453,-9.314238,6.052283,-8.790014,-5.951209,6.515001,4.001935,4.301176,-1.296499,0.174940,4.943981,-1.567153,2.920096,0.626506,-5.601881,-2.426634,2.630405,-6.346236,6.447240,8.161973,-2.601950,8.453537,-4.370931,6.570467,9.818466,-4.805788,8.235702,-4.150994,-6.829251,-2.602388,8.201901,2.360585,3.468624,-2.088922,-9.143192,-4.302702,-2.716290,-1.283828,-5.945462,7.912150,-0.344243,-9.597074,-7.946200,-1.112556,-7.027778,-9.781730,2.919361,1.879694,1.159484,-6.404461,8.410164,-1.460526,-7.040831,-6.090140,-5.664251,-5.366884,9.896015,-5.329192,6.776359,-9.689104,4.657492,0.407848,-3.458068,5.566180,-1.338398,-2.522875,7.915748,3.354088,8.833229,-0.780281,3.516900,8.257854,-7.009426,5.705994,-2.616132,0.070453,-6.062615,3.264062,0.107019,-7.332308,-2.233919,6.843189,5.368276,4.130369,-7.402795,-6.675314,-2.794800,5.563848,-6.770408,-1.162583,-2.674279,-7.151976,-6.215685,-5.515475,6.043661,-4.123605,1.675888,9.341074,-7.765975,7.921771,-0.572034,3.594537,3.259565,2.703203,0.953060,5.040983,-9.513445,-0.727570,9.717870,-0.783596,1.437619,-2.941882,1.461754,6.615050,-8.351851,-5.063276,-4.035964,9.989662,-3.581586,6.171483,-9.757326,-7.314276,2.374025,9.487526,7.485775,5.651660,-7.608647,5.302023,3.880122,-7.827663,5.912235,-4.948069,-1.642318,-3.627119,3.329732,-4.798057,-8.805417,-5.134599,8.926764,-4.567744,6.725636,6.767413,7.178551,5.708372,1.724691,-4.991233,8.382637,-3.563309,-8.486557,-5.978517,9.605474,9.508221,3.406370,0.770501,0.842746,0.856501,7.165049,1.316624,0.544609,5.298592,-7.008792,-9.634258,-0.451963,9.586256,6.330316,-5.622236,-4.539420,-0.027314,4.919921,-0.079209,4.678021,-0.658793,-9.020366,8.641150,-2.539854,-0.206758,-7.982780,-3.779925,2.779867,0.118872,-3.921708,4.519082,1.728345,-3.663678,7.562621,5.842902,7.055244,8.552479,1.555492,9.614763,7.734377,-8.365880,-0.786261,4.632403,-5.922159,-6.062033,-6.075422,9.838894,8.842977,0.730244,-2.798792,5.130859,-3.420490,0.625739,0.587039,5.311387,-9.442739,-2.681428,6.927947,1.090465,-9.953630,-0.564766,3.685254,-1.703597,5.833279,-6.848072,7.117588,6.142478,-0.783478,1.740859,-2.976564,0.459695,2.390778,4.697828,1.031565,-4.230896,2.064204,-8.985950,0.773097,1.780639,-0.080129,-1.968457,-0.235052,2.669090,9.411024,-1.252901,-7.593573,-1.629670,-9.710141,-7.768121,-9.750572,2.044765,5.709432,1.569119,5.157198,0.775785,-6.441700,9.567291,-9.303260,0.998061,0.434150,6.613035,9.775114,1.807857,4.361812,5.556789,9.148770,3.549269,6.537988,1.338457,-1.953058,-4.242173,-9.803477,8.827373,9.271533,-5.486087,-6.647523,-6.194079,-4.656770,0.396230,2.562191,9.301017,-5.907423,9.431540,1.245877,-5.942004,8.742319,-6.359019,-5.816554,-2.503459,0.190276,-4.895210,-8.694803,9.979418,3.277548,5.037551,-6.547137,7.575860,9.080521,-4.680130,7.920668,-5.786508,7.387185,-1.002638,-4.035581,3.356167,-7.396342,-2.029335,-3.337791,7.032444,-0.613065,-4.772568,9.613944,3.319553,-0.940820,-3.874019,-9.985605,3.834694,8.904623,2.638514,-3.904211,4.023936,6.652542,-1.804248,-6.534608,0.541699,-1.721655,1.997764,6.271866,-0.204053,-5.382898,3.965994,-0.526706,-2.982309,-9.242773,4.708349,4.441822,4.806866,-4.972287,-0.310377,4.022637,-3.883185,-5.841421,-2.845344,-3.994025,2.579458,5.199743,-9.078728,9.965236,0.030950,-1.947652,3.667146,-1.044663,-7.553489,-6.942046,9.488448,-8.604568,4.923577,8.196328,-5.775980,-8.228964,-8.709136,-3.296257,6.394813,2.207504,-0.568195,-9.232428,9.082908,-5.273261,8.541155,1.728895,0.545061,-3.223661,-1.653124,-3.763089,-5.317998,-8.601673,-8.098352,8.578413,9.841259,-0.431834,-8.262155,0.674515,8.348467,-7.723171,-9.966314,2.670874,4.120278,-2.850744,0.792239,1.942165,7.101391,-8.037944,-9.382759,-6.006272,7.896636,4.018466,5.617675,2.215866,0.061204,2.257794,8.426465,1.657251,5.541905,-7.630807,-6.244307,-9.680486,-1.523998,9.708388,-0.722487,-5.561036,-5.288699,5.352527,-0.903341,5.774381,-2.653155,5.418727,7.789752,2.053976,-8.518949,-5.501250,9.878756,-1.908523,0.844540,-4.555188,2.877571,6.249826,3.691512,0.463299,-4.212113,4.321662,-6.431786,-1.110511,8.888559,-9.900107,-8.675805,-3.427027,9.798024,8.323412,-6.212203,-1.357627,-9.683765,8.752818,-9.106997,9.143548,7.853091,-4.953622,6.831621,-9.582138,-3.796766,-5.994050,7.870456,-7.581821,6.979494,9.357057,1.806384,-0.878923,-0.886981,3.863651,-9.836269,0.991432,9.756373,6.224651,-6.541108,7.181572,-3.099536,5.677133,-3.061221,-5.347336,1.856800,5.634477,6.026326,-7.504456,-2.762897,8.487651,-8.867889,-2.262975,-0.224289,-3.651579,4.954269,0.206535,6.761589,4.229448,-6.057680,-6.443363,-0.055763,-9.081795,0.180568,3.538772,9.965912,-3.725549,2.866684,5.015841,4.611744,-3.573802,-6.937905,-8.665298,6.203519,1.795372,-6.131822,2.348770,-8.653914,-0.595769,1.577803,2.618238,-6.939487,-5.931390,-5.151920,5.936475,-5.196479,6.232104,4.497260,-3.401673,6.734797,-3.297194,2.917318,-0.205324,-0.350951,7.007275,-6.833095,-5.054704,7.492660,-4.380056,-0.575891,3.556884,-3.933019,1.736560,-1.510175,-4.484560,-9.361069,3.385624,-9.083822,2.986604,4.546832,-0.222832,0.959496,-0.637837,-3.714831,-8.152306,7.503275,1.119873,-8.024984,4.569168,-0.471050,9.040232,6.042504,7.377855,-3.997115,-4.714925,2.049461,-2.744481,2.736105,2.164801,8.420879,-0.482309,8.980377,-6.077913,7.876886,0.947430,3.797278,-7.555115,0.847617,5.439443,-0.219795,6.703790,-1.821067,-4.890528,5.037645,7.382679,2.155630,2.128137,0.928194,8.363715,8.565861,7.905593,6.152763,8.962922,5.713108,-0.895696,-2.086101,7.554124,3.503986,-7.305899,-6.715588,-5.993119,-8.899088,-6.888505,9.702530,-7.667011,-5.493558,-0.031257,2.547031,7.635626,-1.152266,-6.629990,2.895189,8.840364,4.330038,8.439164,-7.536321,8.810956,5.687373,-8.048351,4.692602,-0.564735,-4.799636,1.898520,-2.438392,-1.093922,3.101208,-7.046803,8.537152,5.953904,5.408612,-7.784614,-0.966876,-0.049360,7.944782,6.827358,0.744611,8.355922,-1.598731,1.822913,4.195220,1.500005,-7.667900,8.919498,9.791434,-2.471844,-0.377236,-9.942229,7.791161,-3.967892,-0.012835,5.963632], dtype = "float32")#candidate|5986|(672,)|const|float32
const_5987 = relay.const([6,-1,10,-6,-2,-2,-2,6,-7,-1,9,-6,-1,-3,-2,6,-2,10,-6,4,9,-9,-9,8,-8,-4,2,-3,4,-3,2,6,-8,-7,5,4,-7,4,8,3,2,4,-7,5,4,-10,9,10,2,-4,9,10,1,-2,-7,-8,2,3,8,5,-7,-8,-10,-6,6,-1,9,10,9,-10,7,-5,9,-2,-7,-7,-1,3,-5,-6,-2,-5,10,3,-7,8,-3,7,-3,7,6,-4,-10,10,7,-6,5,-10,-7,6,5,10,-7,8,-5,-9,10,8,2,5,4,-8,3,5,10,5,-5,1,-1,-1,-7,-7,-4,7,5,-5,5,7,1,9,-5,-5,1,-10,9,1,2,3,5,1,-3,-6,-2,-8,8,2,-2,-2,7,5,5,-1,2,-4,5,-6,4,9,-6,6,-4,7,-9,7,3,3,-8,7,-2,8,8,6,-5,-7,1,4,4,-1,10,-3], dtype = "int32")#candidate|5987|(180,)|const|int32
var_5988 = relay.var("var_5988", dtype = "uint64", shape = (896,))#candidate|5988|(896,)|var|uint64
call_5984 = relay.TupleGetItem(func_4870_call(relay.reshape(var_5985.astype('float64'), [2, 8, 14]), relay.reshape(const_5986.astype('float32'), [672,]), relay.reshape(const_5987.astype('int32'), [180,]), relay.reshape(var_5988.astype('uint64'), [896,]), ), 5)
call_5989 = relay.TupleGetItem(func_4876_call(relay.reshape(var_5985.astype('float64'), [2, 8, 14]), relay.reshape(const_5986.astype('float32'), [672,]), relay.reshape(const_5987.astype('int32'), [180,]), relay.reshape(var_5988.astype('uint64'), [896,]), ), 5)
func_2703_call = mod.get_global_var('func_2703')
func_2706_call = mutated_mod.get_global_var('func_2706')
var_5993 = relay.var("var_5993", dtype = "bool", shape = (480,))#candidate|5993|(480,)|var|bool
call_5992 = func_2703_call(relay.reshape(var_5993.astype('bool'), [8, 4, 15]), relay.reshape(var_5993.astype('bool'), [8, 4, 15]), )
call_5994 = func_2703_call(relay.reshape(var_5993.astype('bool'), [8, 4, 15]), relay.reshape(var_5993.astype('bool'), [8, 4, 15]), )
uop_6019 = relay.tan(call_5984.astype('float64')) # shape=(672,)
uop_6021 = relay.tan(call_5989.astype('float64')) # shape=(672,)
output = relay.Tuple([call_5980,var_5985,const_5986,const_5987,var_5988,call_5992,var_5993,uop_6019,])
output2 = relay.Tuple([call_5981,var_5985,const_5986,const_5987,var_5988,call_5994,var_5993,uop_6021,])
func_6028 = relay.Function([var_5985,var_5988,var_5993,], output)
mod['func_6028'] = func_6028
mod = relay.transform.InferType()(mod)
mutated_mod['func_6028'] = func_6028
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6028_call = mutated_mod.get_global_var('func_6028')
var_6030 = relay.var("var_6030", dtype = "float64", shape = (224,))#candidate|6030|(224,)|var|float64
var_6031 = relay.var("var_6031", dtype = "uint64", shape = (896,))#candidate|6031|(896,)|var|uint64
var_6032 = relay.var("var_6032", dtype = "bool", shape = (480,))#candidate|6032|(480,)|var|bool
call_6029 = func_6028_call(var_6030,var_6031,var_6032,)
output = call_6029
func_6033 = relay.Function([var_6030,var_6031,var_6032,], output)
mutated_mod['func_6033'] = func_6033
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5773_call = mod.get_global_var('func_5773')
func_5774_call = mutated_mod.get_global_var('func_5774')
call_6075 = func_5773_call()
call_6076 = func_5773_call()
var_6110 = relay.var("var_6110", dtype = "float32", shape = (9, 2, 6))#candidate|6110|(9, 2, 6)|var|float32
bop_6111 = relay.bitwise_and(call_6075.astype('uint64'), relay.reshape(var_6110.astype('uint64'), relay.shape_of(call_6075))) # shape=(9, 2, 6)
bop_6114 = relay.bitwise_and(call_6076.astype('uint64'), relay.reshape(var_6110.astype('uint64'), relay.shape_of(call_6076))) # shape=(9, 2, 6)
output = relay.Tuple([bop_6111,])
output2 = relay.Tuple([bop_6114,])
func_6121 = relay.Function([var_6110,], output)
mod['func_6121'] = func_6121
mod = relay.transform.InferType()(mod)
var_6122 = relay.var("var_6122", dtype = "float32", shape = (9, 2, 6))#candidate|6122|(9, 2, 6)|var|float32
output = func_6121(var_6122)
func_6123 = relay.Function([var_6122], output)
mutated_mod['func_6123'] = func_6123
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5773_call = mod.get_global_var('func_5773')
func_5774_call = mutated_mod.get_global_var('func_5774')
call_6132 = func_5773_call()
call_6133 = func_5773_call()
output = relay.Tuple([call_6132,])
output2 = relay.Tuple([call_6133,])
func_6134 = relay.Function([], output)
mod['func_6134'] = func_6134
mod = relay.transform.InferType()(mod)
output = func_6134()
func_6135 = relay.Function([], output)
mutated_mod['func_6135'] = func_6135
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6134_call = mod.get_global_var('func_6134')
func_6135_call = mutated_mod.get_global_var('func_6135')
call_6188 = relay.TupleGetItem(func_6134_call(), 0)
call_6189 = relay.TupleGetItem(func_6135_call(), 0)
func_6121_call = mod.get_global_var('func_6121')
func_6123_call = mutated_mod.get_global_var('func_6123')
call_6192 = relay.TupleGetItem(func_6121_call(relay.reshape(call_6188.astype('float32'), [9, 2, 6])), 0)
call_6193 = relay.TupleGetItem(func_6123_call(relay.reshape(call_6188.astype('float32'), [9, 2, 6])), 0)
var_6197 = relay.var("var_6197", dtype = "float32", shape = (9, 2, 6))#candidate|6197|(9, 2, 6)|var|float32
bop_6198 = relay.maximum(call_6188.astype('int64'), relay.reshape(var_6197.astype('int64'), relay.shape_of(call_6188))) # shape=(9, 2, 6)
bop_6201 = relay.maximum(call_6189.astype('int64'), relay.reshape(var_6197.astype('int64'), relay.shape_of(call_6189))) # shape=(9, 2, 6)
var_6203 = relay.var("var_6203", dtype = "int64", shape = (9, 2, 6))#candidate|6203|(9, 2, 6)|var|int64
bop_6204 = relay.greater_equal(bop_6198.astype('bool'), relay.reshape(var_6203.astype('bool'), relay.shape_of(bop_6198))) # shape=(9, 2, 6)
bop_6207 = relay.greater_equal(bop_6201.astype('bool'), relay.reshape(var_6203.astype('bool'), relay.shape_of(bop_6201))) # shape=(9, 2, 6)
output = relay.Tuple([call_6192,bop_6204,])
output2 = relay.Tuple([call_6193,bop_6207,])
func_6208 = relay.Function([var_6197,var_6203,], output)
mod['func_6208'] = func_6208
mod = relay.transform.InferType()(mod)
var_6209 = relay.var("var_6209", dtype = "float32", shape = (9, 2, 6))#candidate|6209|(9, 2, 6)|var|float32
var_6210 = relay.var("var_6210", dtype = "int64", shape = (9, 2, 6))#candidate|6210|(9, 2, 6)|var|int64
output = func_6208(var_6209,var_6210,)
func_6211 = relay.Function([var_6209,var_6210,], output)
mutated_mod['func_6211'] = func_6211
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5978_call = mod.get_global_var('func_5978')
func_5979_call = mutated_mod.get_global_var('func_5979')
call_6213 = func_5978_call()
call_6214 = func_5978_call()
func_910_call = mod.get_global_var('func_910')
func_912_call = mutated_mod.get_global_var('func_912')
const_6225 = relay.const([[-6,-6,-9,5,8,-2,6,9,-1,4,-1,-7,3,10,9,10,2,-4,4,3,-3,-10,-8,9,-5,9,-5,-7,-6,-10,10,-10,-7,-5,4,-5,-3,-9,6,-2,4,9,8,6,4,8,-9,8,5,-8,-3,9,10,9,-6,8,-2,7,-4,3,2,-4,2,-8,-7,-9,1,-6,-5,-8,-6,1,5,8,-5,-1,-4,10,7,4,-4,4,-2,6,-5,-8,-3,9,-1,1,-7,4,5,7,2,8,6,-1,4,4,4,-2,-5,6,5,-3,-10,-4,-3,-9,-2,-2,10,-7,-3,-4,4,-5,-7,6,-10,6,10,-5,3,-9,-10,5,6,-4,2,-5,4,-7,5,-2,-6,5,10,-10],[-3,-8,-2,4,-5,-7,6,3,-6,-10,-6,5,3,-10,1,4,1,-8,-6,-10,-1,-10,-1,-7,-5,-7,9,5,-4,-5,-6,-1,-4,9,1,3,-8,-7,5,-7,10,1,8,3,2,-6,-8,5,-6,-2,-6,7,5,7,7,-10,10,10,7,1,-1,10,-6,1,-9,-8,-5,9,10,-10,9,-6,1,-8,-9,-10,6,2,-4,3,-4,-8,-6,1,-4,5,-2,4,-8,4,9,-10,5,-6,-4,2,-10,9,7,1,2,5,-8,-9,-9,-4,6,-5,5,-10,10,9,2,5,-9,-3,4,-6,6,9,-6,-8,-8,-5,-2,-1,9,-2,7,2,-8,6,-2,-6,-8,6,9,-10,6,-1],[-10,-3,-4,10,4,7,7,-4,8,7,-7,1,8,-5,7,-3,10,-8,10,-4,-1,8,8,7,2,-1,-9,-6,-6,-1,7,-1,-1,9,-10,8,8,1,8,10,-4,-8,7,-9,-5,7,-6,8,1,9,-2,5,2,4,4,1,-8,10,-3,8,1,1,-6,-5,6,-8,-2,10,9,-6,-9,2,6,-3,-10,10,-8,9,9,1,-7,-6,4,-4,10,-7,-7,-6,-10,3,-10,1,3,4,-3,9,-5,-8,-3,-3,2,-3,10,3,10,10,-10,-10,1,7,8,-2,5,6,-4,-2,-1,-9,-8,-9,-10,-10,9,7,5,-2,2,-8,7,4,2,-10,-2,-4,-1,9,-1,4,-9,10],[7,-7,-9,7,-10,7,-6,5,-6,-8,-1,8,6,-3,-7,8,-8,-4,-3,-1,1,-5,5,-6,-8,-5,1,-4,-9,9,2,9,-6,5,3,10,-3,10,-6,8,1,4,1,7,7,-6,-7,10,-6,-1,-2,3,-8,5,1,8,9,4,-2,-9,-10,7,-8,1,2,4,-2,1,-2,-2,10,-7,-3,-10,-3,-1,4,10,-7,-7,-2,-4,10,4,2,6,-9,-4,3,5,-2,9,-6,-7,10,3,9,-6,-5,-2,10,10,9,2,-7,-8,-3,7,5,-4,10,-7,-7,7,-7,8,6,-9,-3,9,-7,-2,-5,2,3,-5,5,3,8,3,-8,5,10,-1,4,-4,-6,-1,-3,10],[-1,10,-10,-10,-2,4,-4,4,-4,5,-4,8,3,-10,4,-4,-7,-3,-5,5,-3,-9,-9,-1,7,-10,-4,10,8,8,2,-7,4,7,-2,-1,1,-2,-3,3,8,1,-2,3,-5,-9,1,-7,5,-8,-6,4,7,10,-8,1,6,1,-5,7,-3,8,-4,1,-10,-8,8,-4,7,-8,-6,-4,1,10,10,-7,-4,7,1,-9,8,5,-9,-4,4,-3,1,5,-1,-7,4,3,10,-8,-1,9,-4,9,7,10,-5,4,-10,-7,3,1,-9,-7,-6,7,-2,9,5,1,-1,-3,-6,2,5,-7,3,-8,-4,-1,-10,10,-7,9,-8,5,-3,-6,5,-5,9,-9,-1,7,9,-8],[6,-2,6,6,2,-3,-10,-6,-1,3,4,-4,-6,10,9,-6,-3,-8,10,5,5,-8,1,10,-8,1,5,-5,-8,-8,-3,2,5,-9,7,-6,3,7,-2,5,-10,-10,-4,5,1,9,-10,-10,-4,-9,-2,-3,-10,1,9,-10,2,3,-6,-8,-4,1,-1,-8,-1,-5,-1,-9,1,1,-6,9,10,4,10,2,-10,-7,-5,3,3,10,6,-5,9,-7,6,3,-7,3,-8,1,-10,-8,-5,-1,-8,-2,-10,1,2,4,-3,-5,1,-8,-3,-6,9,-7,4,-5,-9,-9,4,6,-10,-4,-5,-3,-9,7,10,-4,-7,7,1,6,-9,-6,-8,10,3,3,5,8,7,-5,-9,9],[-1,1,-8,-9,5,1,10,-3,5,4,-2,-3,8,-9,6,6,2,-9,-4,7,-8,3,10,-2,2,5,6,4,-6,2,-10,-1,-6,5,1,-1,2,6,2,7,1,9,-9,-5,7,-7,8,1,8,-5,-8,9,-10,2,-2,5,10,-5,6,-6,-7,-2,-10,-8,9,-1,-10,8,5,2,-8,5,3,-9,-7,-4,7,-1,8,-7,-3,-3,9,2,1,3,5,9,5,-6,2,-1,5,8,-1,10,3,6,-5,6,-4,-7,-7,6,-6,-6,-2,9,-9,1,-4,-4,4,-9,-10,-9,5,5,4,-4,4,1,9,3,9,-7,-5,-9,3,-8,-4,7,-4,-1,-4,9,7,3,-3,3],[10,-4,5,4,3,10,10,7,10,10,-3,1,2,5,10,-7,1,3,-7,1,10,7,9,-2,2,-2,-3,-6,-6,-10,10,-7,9,7,9,-5,-9,7,-8,8,2,-8,4,-2,4,9,9,7,7,5,-1,-7,5,-10,-4,5,-10,-1,-5,-7,4,7,3,3,-7,10,-9,2,-10,6,-3,-9,2,-7,2,-7,3,2,-7,8,1,6,6,3,2,-1,8,10,-2,6,3,2,7,-2,7,2,1,-8,-8,2,-8,-5,-2,6,-1,8,6,-2,4,-9,7,10,9,-2,9,-7,4,5,8,-10,2,5,-9,-2,2,-5,1,4,3,7,9,-1,5,-10,5,-3,1,-8,-6,5],[-10,-6,6,-10,-7,3,10,-10,-9,-7,-2,3,10,-4,-2,2,-9,-10,10,8,-9,-3,6,-4,-4,9,-3,1,-6,8,4,-7,-10,-2,10,-6,-2,6,2,10,10,6,-6,7,-2,9,6,-10,4,5,-1,-3,-1,10,-8,3,-2,3,6,9,4,-3,-3,-7,5,2,-4,-9,-1,-10,9,-9,2,8,-10,5,4,-6,-9,5,4,1,2,3,-9,4,-8,-1,-3,-10,8,8,-3,9,7,7,-1,9,8,-7,-7,-7,2,-7,8,9,-3,8,-3,-8,-8,4,-3,1,7,10,-8,10,8,-4,-5,2,2,-3,-4,-7,-8,-2,-6,-4,-2,8,3,10,3,8,1,-5,-10,7]], dtype = "int64")#candidate|6225|(9, 140)|const|int64
call_6224 = relay.TupleGetItem(func_910_call(relay.reshape(const_6225.astype('int64'), [10, 14, 9])), 0)
call_6226 = relay.TupleGetItem(func_912_call(relay.reshape(const_6225.astype('int64'), [10, 14, 9])), 0)
output = relay.Tuple([call_6213,call_6224,const_6225,])
output2 = relay.Tuple([call_6214,call_6226,const_6225,])
func_6227 = relay.Function([], output)
mod['func_6227'] = func_6227
mod = relay.transform.InferType()(mod)
output = func_6227()
func_6228 = relay.Function([], output)
mutated_mod['func_6228'] = func_6228
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5773_call = mod.get_global_var('func_5773')
func_5774_call = mutated_mod.get_global_var('func_5774')
call_6287 = func_5773_call()
call_6288 = func_5773_call()
uop_6307 = relay.cos(call_6287.astype('float64')) # shape=(9, 2, 6)
uop_6309 = relay.cos(call_6288.astype('float64')) # shape=(9, 2, 6)
output = uop_6307
output2 = uop_6309
func_6336 = relay.Function([], output)
mod['func_6336'] = func_6336
mod = relay.transform.InferType()(mod)
mutated_mod['func_6336'] = func_6336
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6336_call = mutated_mod.get_global_var('func_6336')
call_6337 = func_6336_call()
output = call_6337
func_6338 = relay.Function([], output)
mutated_mod['func_6338'] = func_6338
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6227_call = mod.get_global_var('func_6227')
func_6228_call = mutated_mod.get_global_var('func_6228')
call_6344 = relay.TupleGetItem(func_6227_call(), 0)
call_6345 = relay.TupleGetItem(func_6228_call(), 0)
var_6346 = relay.var("var_6346", dtype = "float32", shape = (9, 2, 6))#candidate|6346|(9, 2, 6)|var|float32
bop_6347 = relay.floor_divide(call_6344.astype('float32'), relay.reshape(var_6346.astype('float32'), relay.shape_of(call_6344))) # shape=(9, 2, 6)
bop_6350 = relay.floor_divide(call_6345.astype('float32'), relay.reshape(var_6346.astype('float32'), relay.shape_of(call_6345))) # shape=(9, 2, 6)
uop_6351 = relay.sqrt(var_6346.astype('float32')) # shape=(9, 2, 6)
output = relay.Tuple([bop_6347,uop_6351,])
output2 = relay.Tuple([bop_6350,uop_6351,])
func_6355 = relay.Function([var_6346,], output)
mod['func_6355'] = func_6355
mod = relay.transform.InferType()(mod)
mutated_mod['func_6355'] = func_6355
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6356 = relay.var("var_6356", dtype = "float32", shape = (9, 2, 6))#candidate|6356|(9, 2, 6)|var|float32
func_6355_call = mutated_mod.get_global_var('func_6355')
call_6357 = func_6355_call(var_6356)
output = call_6357
func_6358 = relay.Function([var_6356], output)
mutated_mod['func_6358'] = func_6358
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6227_call = mod.get_global_var('func_6227')
func_6228_call = mutated_mod.get_global_var('func_6228')
call_6413 = relay.TupleGetItem(func_6227_call(), 2)
call_6414 = relay.TupleGetItem(func_6228_call(), 2)
var_6424 = relay.var("var_6424", dtype = "int64", shape = (9, 140))#candidate|6424|(9, 140)|var|int64
bop_6425 = relay.multiply(call_6413.astype('uint32'), relay.reshape(var_6424.astype('uint32'), relay.shape_of(call_6413))) # shape=(9, 140)
bop_6428 = relay.multiply(call_6414.astype('uint32'), relay.reshape(var_6424.astype('uint32'), relay.shape_of(call_6414))) # shape=(9, 140)
output = bop_6425
output2 = bop_6428
func_6430 = relay.Function([var_6424,], output)
mod['func_6430'] = func_6430
mod = relay.transform.InferType()(mod)
mutated_mod['func_6430'] = func_6430
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6431 = relay.var("var_6431", dtype = "int64", shape = (9, 140))#candidate|6431|(9, 140)|var|int64
func_6430_call = mutated_mod.get_global_var('func_6430')
call_6432 = func_6430_call(var_6431)
output = call_6432
func_6433 = relay.Function([var_6431], output)
mutated_mod['func_6433'] = func_6433
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6443 = relay.var("var_6443", dtype = "float64", shape = (5, 4))#candidate|6443|(5, 4)|var|float64
var_6444 = relay.var("var_6444", dtype = "float64", shape = (5, 4))#candidate|6444|(5, 4)|var|float64
bop_6445 = relay.floor_mod(var_6443.astype('float64'), relay.reshape(var_6444.astype('float64'), relay.shape_of(var_6443))) # shape=(5, 4)
func_6134_call = mod.get_global_var('func_6134')
func_6135_call = mutated_mod.get_global_var('func_6135')
call_6453 = relay.TupleGetItem(func_6134_call(), 0)
call_6454 = relay.TupleGetItem(func_6135_call(), 0)
func_2128_call = mod.get_global_var('func_2128')
func_2130_call = mutated_mod.get_global_var('func_2130')
var_6461 = relay.var("var_6461", dtype = "float32", shape = (882,))#candidate|6461|(882,)|var|float32
call_6460 = relay.TupleGetItem(func_2128_call(relay.reshape(var_6461.astype('float32'), [9, 7, 14])), 1)
call_6462 = relay.TupleGetItem(func_2130_call(relay.reshape(var_6461.astype('float32'), [9, 7, 14])), 1)
func_824_call = mod.get_global_var('func_824')
func_827_call = mutated_mod.get_global_var('func_827')
var_6468 = relay.var("var_6468", dtype = "float32", shape = (128,))#candidate|6468|(128,)|var|float32
var_6469 = relay.var("var_6469", dtype = "uint32", shape = (70,))#candidate|6469|(70,)|var|uint32
call_6467 = relay.TupleGetItem(func_824_call(relay.reshape(var_6468.astype('float32'), [8, 16]), relay.reshape(var_6469.astype('uint32'), [70,]), ), 3)
call_6470 = relay.TupleGetItem(func_827_call(relay.reshape(var_6468.astype('float32'), [8, 16]), relay.reshape(var_6469.astype('uint32'), [70,]), ), 3)
output = relay.Tuple([bop_6445,call_6453,call_6460,var_6461,call_6467,var_6468,var_6469,])
output2 = relay.Tuple([bop_6445,call_6454,call_6462,var_6461,call_6470,var_6468,var_6469,])
func_6472 = relay.Function([var_6443,var_6444,var_6461,var_6468,var_6469,], output)
mod['func_6472'] = func_6472
mod = relay.transform.InferType()(mod)
var_6473 = relay.var("var_6473", dtype = "float64", shape = (5, 4))#candidate|6473|(5, 4)|var|float64
var_6474 = relay.var("var_6474", dtype = "float64", shape = (5, 4))#candidate|6474|(5, 4)|var|float64
var_6475 = relay.var("var_6475", dtype = "float32", shape = (882,))#candidate|6475|(882,)|var|float32
var_6476 = relay.var("var_6476", dtype = "float32", shape = (128,))#candidate|6476|(128,)|var|float32
var_6477 = relay.var("var_6477", dtype = "uint32", shape = (70,))#candidate|6477|(70,)|var|uint32
output = func_6472(var_6473,var_6474,var_6475,var_6476,var_6477,)
func_6478 = relay.Function([var_6473,var_6474,var_6475,var_6476,var_6477,], output)
mutated_mod['func_6478'] = func_6478
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6505 = relay.var("var_6505", dtype = "int8", shape = (1, 16, 13))#candidate|6505|(1, 16, 13)|var|int8
var_6506 = relay.var("var_6506", dtype = "int8", shape = (9, 16, 13))#candidate|6506|(9, 16, 13)|var|int8
bop_6507 = relay.add(var_6505.astype('int8'), var_6506.astype('int8')) # shape=(9, 16, 13)
output = relay.Tuple([bop_6507,])
output2 = relay.Tuple([bop_6507,])
func_6514 = relay.Function([var_6505,var_6506,], output)
mod['func_6514'] = func_6514
mod = relay.transform.InferType()(mod)
var_6515 = relay.var("var_6515", dtype = "int8", shape = (1, 16, 13))#candidate|6515|(1, 16, 13)|var|int8
var_6516 = relay.var("var_6516", dtype = "int8", shape = (9, 16, 13))#candidate|6516|(9, 16, 13)|var|int8
output = func_6514(var_6515,var_6516,)
func_6517 = relay.Function([var_6515,var_6516,], output)
mutated_mod['func_6517'] = func_6517
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5978_call = mod.get_global_var('func_5978')
func_5979_call = mutated_mod.get_global_var('func_5979')
call_6623 = func_5978_call()
call_6624 = func_5978_call()
func_5363_call = mod.get_global_var('func_5363')
func_5367_call = mutated_mod.get_global_var('func_5367')
var_6643 = relay.var("var_6643", dtype = "uint64", shape = (72,))#candidate|6643|(72,)|var|uint64
const_6644 = relay.const([9,10,-4,-9,-9,-7,-10,1,-7,-1,-10,4,-6,3,5,-3,8,2,6,-6,-2,9,8,-4,-2,5,-7,8,-1,-7,-2,3,-4,1,-10,-4,-4,4,4,6,-7,9,-1,-7,-7,1,5,-1,-2,-8,1,-5,-6,6,9,5,6,7,-1,2,-9,7,-8,6,1,2,-7,-7,-6,-4,-7,-8,-2,-10,9,1,4,5,-6,-4,4,-9,1,-3,-10,-1,-7,10,5,-4,-4,4,3,-10,8,-6,-9,3,-10,8,-5,-7,-9,-2,8,1,-9,10,4,-10,5,5,8,6,4,6,-5,2,1,-8,-7,1,-4,9,2,-2,-5,10,5,-1,-10,-10,1,8,-5,-3,7,-2,6,1,-1,4,10,-9,-2,7,9,-8,1,-4,-4,3,-10,4,-4,-3,-8,1,5,-4,-2,10,10,2,3,2,-3,-9,-7,1,8,10,-5,5,-1,-6,1,4,3,5,-4,-3,1,3,3,-1,8,-6,-2,-2,9,6,5,1,8,5,-4,-10,-8,-3,5,-3,-7,7,-9,2,10,-8,-10,4,-9,-9,-7,6,-9,8,2,8,-10,9,-5,-9,-1,-1,-8,-8,-6,-7,-3,8,-1,8,10,3,1,9,-10,-3,5,-1,-1,-9,-5,9,1,-4,6,6,-5,5,-8,6,-5,1,4,-5,3,3,-2,10,2,8,3,3,2,8,4,-9,2,1,4,-5,1,6,2,9,-1,5,10,4,8,1,5,-3,10,6,-9,10], dtype = "uint64")#candidate|6644|(288,)|const|uint64
const_6645 = relay.const([2.237915,-9.402418,-2.623950,3.917732,3.977775,-5.568367,-4.929472,7.939178,9.117486,8.436045,-4.325599,-7.525987,9.033829,6.410772,-9.871174,9.008756,1.088891,-9.526665,-0.658534,0.873370,0.323243,3.531725,1.083813,-5.556401,1.323584,2.571674,-1.074978,-8.042767,-9.153975,-6.684831,-3.329363,-9.896183,0.418441,6.672241,2.482482,5.020889,2.734950,-2.355543,-9.451619,9.842922,7.918626,2.953542,-4.521687,0.745867,5.368016,6.498214,-0.602591,1.371939,-5.607033,3.791001,-4.082548,-9.492753,6.426856,-8.263515,5.874748,6.038142,4.344663,-0.269554,-5.457168,-0.061142,1.787321,0.751136,2.839796,-6.526176,-8.154231,7.493114,-5.884529,-6.924699,7.348683,6.103825,-7.755238,9.311788,4.513280,0.229421,0.680806,8.872477,1.608102,-8.217251,-2.667653,-3.781054,-7.086399,0.968815,7.449587,-0.624740,-9.885658,0.859229,-9.692219,-7.297216,9.572093,2.375297,1.864747,2.711661,-7.983722,-6.683079,-5.170217,0.071659,-2.921087,-5.729386,-1.834893,-9.089458,-8.762727,2.054781,-1.200537,3.099931,9.593361,4.391895,0.434333,3.052981,-5.085202,-3.675693,-0.183671,-9.849209,-7.879739,-6.587010,4.498495,-4.201546,-0.827752,1.742711,4.761195,-3.668589,4.484856,-9.023828,4.346196,-2.241988,9.133708,-5.214167,-6.855284,-2.041653,9.268292,2.231947,-0.215613,8.544045,9.440209,5.658658,1.713083,0.404113,6.187567,0.391062,7.738926,1.128364,8.340547,-1.768654,-7.350182,-9.692327,0.642744,-5.613232,0.879068,1.486180,-1.727473,-8.856080,-6.812094,3.982134,6.306551,-2.020473,-2.230376,7.306672,-3.289526,-7.231248,-6.804102,-5.162696,-5.558758,4.757795,-8.801922,3.546009,-2.262791,-7.678778,1.342016,-5.828190,2.193874,-8.261416,-5.904419,2.711405,0.315113,9.718358,-3.906678,-4.190101,4.438943,9.176614,-9.198622,-1.322304,-6.977675,5.606098,-6.175502,-9.493732,7.428848,-6.233913,-8.350608,-5.010399,3.082593,6.837814,6.208036,-9.514280,-8.891046,8.257848,-7.664229,8.579093,-1.262153,4.235108,-0.349268,-6.206990,-2.086183,-0.792862,-1.195668,-8.159831,-5.368957,-7.638030,6.539023,-9.927046,-0.822478,-9.031329,-7.013106,9.870878,4.923801,1.370856,-4.763722,7.593286,-1.900407,8.843810,-2.859907,-2.486493,7.283406,-7.714490,-9.112062,-3.737906,-9.075777,9.923459,-8.839515,-9.384092,3.552282,-2.517298,3.031618,-6.148449,6.389732,4.963083,-2.037614,-8.834956,-4.111973,-0.771574,-9.431450,5.253434,-9.723969,1.960817,7.810759,-1.909508,0.240495,-6.636514,-4.709051,7.660343,-8.997393,3.446602,-8.622753,-7.535160,-9.807329,8.836122,-5.256992,-9.696361,-9.174680,1.179226,1.162258,-5.056072,-0.708810,0.464641,-2.306360,-9.107064,1.331748,8.269248,-4.327253,-1.197686,-1.875170,8.250705,-8.920295,2.947178,0.171780,-1.114931,-7.635904,6.339828,4.144718,9.896066,5.941477,-1.386781,7.096106,3.979259,-9.159595,1.269625,8.685423,4.707276,-2.046256,-3.701318,7.706875,-0.869668,-6.402313,1.410283,-6.890860,4.855601,-1.860009,0.073295,2.291584,0.669874,-0.411894,-9.368847,3.219064,-8.903667,3.276732,0.776473,0.523010,-4.665183,-0.027289,-8.439871,5.114340,-6.821627,6.335670,2.096658,-9.924104,-9.083702,7.056455,5.439561,-9.330863,-7.994704,-1.485711,7.610930,3.348749,2.722441,0.054403,4.083152,9.171523,-6.451120,6.150855,5.616569,2.526839,-8.052986,8.709062,1.214838,3.478940,8.966234,-0.054755,-8.867806,-1.991820,8.167289,2.817285,-8.989245,-4.525351,0.690025,5.167789,-1.496670,5.823528,9.672544,-2.617612,-2.894156,5.051607,4.181477,-4.335509,1.115787,-0.480284,-1.674850,7.792340,-0.282144,-2.199188,6.037678,9.112187,-0.118743,9.032332,3.977078,-3.548084,3.773810,4.452043,0.471473,-0.097522,-4.127343,2.741035,-8.353189,-6.392907,4.894383,3.334230,-3.835835,-3.424686,5.595126,-4.717606,7.867548,-6.002353,-3.179772,8.946958,-1.833485,1.874887,-0.781921,5.930542,0.656336,-4.349116,-3.178443,-1.883895,-8.798754,7.219673,-2.703437,-0.417173,1.818950,-8.697782,-9.713114,0.781372,-3.096491,0.350216,-2.126389,2.046722,-2.878700,-4.500364,6.525869,5.950199,0.341840,9.575997,0.151876,6.898014,1.032213,-8.724324,2.362803,-4.843414,-1.476600,1.588923,-8.772571,7.565907,-6.835069,-9.107080,-4.545691,6.498158,-6.163410,6.665184,-5.332596,-1.069482,-7.504615,2.286803,2.582522,1.353096,9.791841,-8.304203,-7.875455,9.298198,8.782215,-1.615488,3.657622,3.633804,0.764052,2.430249,7.971925,8.885026,2.526220,7.852754,-3.016281,-1.779369,0.291431,2.575902,-2.563485,-0.426582,-6.144586,9.708707,-2.118083,-8.582443,7.941144,0.942576,5.031195,6.561427,0.045694,6.838063,5.323242,-7.224085,-7.891146,-9.934461,-6.565712,-3.269037,-8.571862,-9.914591,-8.155595,-4.565017,1.221902,-6.533935,-5.262615,2.101235,8.262760,1.101397,-3.736292,4.948724,3.877722,-7.934828,6.341686,7.936360,-6.783653,-0.203411,-4.131689,9.331552,5.793880,-2.658274,4.286587,1.369357,8.868527,0.652055,-8.782851,-5.228774,5.463278,2.202814,-7.278819,-5.031157,8.308658,8.997777,8.943169,1.379854,4.791122,-9.442261,1.631047,4.698948,-2.109731,-7.004514,6.566631,-8.269122,5.405262,5.347572,-6.083221,7.514495,1.361012,2.705382,2.668754,7.799944,9.371571,7.111473,0.375451,8.267229,5.882703,5.681849,-7.391327,2.543163,6.170087,7.440983,-9.700633,0.512695,-6.194927,-9.931363,6.260373,-6.152281,8.548877,2.978733,-1.341544,-3.699872,6.524577,-1.717614,-3.731993,2.270564,9.816053,0.038374,9.928204,9.397438,-0.359356,0.456229,2.665834,-1.307621,3.065226,4.847044,-9.946151,-5.392505,8.996413,1.794582,-9.731616,-9.118359,-9.154800,-0.525000,-1.031459,6.403239,9.365728,8.966953,-7.359082,-1.093576,6.262438,4.429630,0.233796,3.489494,-1.291053,-0.935303,-6.971988,-2.348990,4.869734,-4.316782,-3.981931,-7.119174,9.714923,-8.155839,4.611268,8.396468,1.441408,-8.764943,-5.380356,4.064778,-1.365333,-3.426051,-7.880936,7.027138,1.341043,-0.001558,7.501567,5.916211,-5.334316,-6.083756,-3.289328,-9.215462,-3.858430,7.390081,2.784440,-0.455373,-1.639588,-9.478089,5.537316,-0.253024,2.371375,6.103068,0.350876,7.072744,-6.340911,5.007393,-4.526311,-8.447494,-5.380940,0.749097,2.970619,-6.538036,-2.450543,-2.583979,-7.810586,-7.896675,0.114004,8.280821,1.508741,-4.552156,-6.816320,-9.976821,-6.358364,-7.367230,-2.133133,-3.413115,3.733756,-2.997062,7.942799,1.764432,1.614759,6.102910,5.060773,-4.080892,-9.063818,6.481556,-4.305295,5.206991,-1.810770,-8.136152,6.745510,-4.858892,6.685928,5.100617,-5.089166,-0.241427,-9.797512,-0.470656,-7.843616,-7.314441,-8.494113,-1.960507,-2.197412,3.769595,5.467649,9.917373,-8.326358,5.561352,-1.307200,-1.628244,4.025444,2.024398,-6.871852,-7.189621,-2.370706,8.706932,-2.424986,7.309473,7.126958,2.943457,-6.716149,-6.737700,3.907027,-5.342296,-2.084819,-3.635379,-4.140890,4.376512,2.718198,8.363485,3.653916,-8.274970,-0.785938,-6.723977,-6.505179,-7.551304,-1.749178,6.917239,-4.834847,-4.299553,-2.602959,2.760898,-8.162655,-3.052803,-7.995925,4.525543,-4.420301,0.573658,3.754518,4.231016,3.148686,3.359033,-1.774111,0.069416,-0.686744,3.929886,-3.319523,8.535606,1.308343,4.079051,-7.951023,3.043966,-1.985536,5.153067,-5.205750,-9.400061,5.638431,-4.910359,-0.532874,-4.207114,8.042689,-3.716780,-7.545513,-9.645242,8.089520,1.631788,-3.342943,-2.678283,7.478588,-6.168464,-4.079183,-4.924331,-8.309629,1.954886,-8.592499,-7.496843,5.982235,-4.116637,-5.720816,-5.885918,-3.208164,1.156294,-2.060129,2.866860,-0.800660,-6.399369,-2.168903,-8.894927,0.077425,-3.536478,5.268825,9.514739,6.488646,8.592609,-2.664132,2.658945,0.393493,6.751174,-9.241756,-3.349975,-7.939810,-7.693671,5.890052,-1.534390,-3.444255,-6.790598,3.493789,1.303744,5.431856,-5.853311,-3.649711,-8.784149,0.294773,3.069827,6.929146,-5.334254,-9.867926,-9.229130,9.961222,-3.487918,9.521709,0.948934,-4.354743,1.562349,2.929780,3.514608,7.011887,-8.929706,8.313865,1.080413,4.664655,2.883646,-7.348793,3.138107,-6.846422,1.682395,-0.578461,-9.973148,5.893636,6.617655,5.699080,-8.387238,-3.109120,1.529798,6.375755,-2.122240,-4.974377,-8.102006,-5.053528,-1.876564,-4.292417,-7.890669,9.136531,7.159592,6.644068,5.740759,-6.068118,6.575089,-2.973253,-3.947356,0.210401,-3.455080,-3.844258,-7.168386,-2.344116,2.700822,4.908607,-3.690822,-4.734292,1.405189,-3.508799,0.087098,1.713208,7.555263,4.918456,6.460108,2.719421,5.398336,-0.512394,-0.431561,-0.250196,0.666185,5.739318,-5.245067,-6.880106,8.611217,2.072893,8.445774,-1.465051,-6.660538,-3.232504,-6.854256,-4.503248,-0.047747,-1.209482,8.471288,-9.217183,-3.452078,-3.730288,-7.203389,-8.076114,4.624743,-0.517344,-9.800267,-6.883366,-1.647727,-7.032817,-5.660364,-6.099839,-7.386137,8.981479,-5.656468,-7.467328,6.490074,1.321787,9.893587,-9.679432,6.783747,1.344311,8.237563,3.232698,5.759372,-3.209520,-2.994291,-5.043295,6.170738,-7.901099,4.596839,-5.178345,-2.865170,-7.120343,-2.885779,-8.252008,9.731362,2.693694,9.323847,8.473963,9.953989,-3.224138,-8.203883,-6.402517,-4.124069,8.159960,7.020857,0.682780,-3.163248,-7.970358,-2.691818,-2.412312,-6.869040,-3.769068,-2.409683,-5.382753,3.825215,9.561130,3.382441,-5.303483,0.392234,-4.720181,1.885764,-6.110044,5.130431,-0.310760,6.333006,-0.544691,8.014686,-2.654060,-7.448875,4.707378,2.537252,2.418439,-3.532965,8.429454,-0.716260,-5.222237,6.401043,9.091895,6.394139,-1.466796,-8.560439,4.610437,6.319515,-0.395338,-9.414225,0.823674,-7.004406,8.178174,-7.590565,-7.711645,-6.178255,3.905684,7.453068,-1.643274,-5.073366,-9.188685,6.767047,-5.393462,8.444669,-7.406055,-6.962295,8.916955,0.441557,0.656550,7.037468,-1.649032,4.850572,3.618141,-0.859726,9.107981,-2.347927,2.288897,0.484705,-6.300408,-6.419986,0.025792,4.099906,-0.867119,0.769971,-3.840309,1.379287,-0.163758,-2.639074,-0.056902,9.133188,-8.405369,5.487451,-8.898558,0.474657,2.176194,4.853906,3.581230,3.295030,4.751930,4.210476,-9.309447,-8.757308,8.357679,-0.728727,9.593547,-4.053450,-4.912846,-4.727376,-1.790780,3.066653,2.093692,-4.677954,3.918807,-3.931054,-4.735793,1.678531,6.660695,2.382491,-7.906965,-0.490238,-8.691980,4.728933,-4.931726,0.227646,-2.384199,-8.775169,6.956361,-8.674534,-6.291942,-9.881088,-1.398615,1.724931,1.808706,7.799538,6.509712,-7.915116,-9.554049,-9.665102,7.648597,4.853828,-2.881723,5.151320,8.893248,0.280519,8.995888,-5.383145,2.616074,5.022851,9.880468,-9.494550,-3.076304,-4.254029,9.048199,5.519720,-6.109685,-1.385391,-1.974281,-7.346765,9.396765,2.783678,1.035046,-6.070340,-3.390229,-7.594027,-7.184528,-9.706252,3.180984,2.121911,3.460901,7.080901,-5.814035,-4.561629,7.952714,-7.552483,-2.752103,1.750075,0.874407,-6.712040,1.259297,3.178254,-8.530797], dtype = "float64")#candidate|6645|(1080,)|const|float64
call_6642 = relay.TupleGetItem(func_5363_call(relay.reshape(var_6643.astype('uint64'), [1, 8, 9]), relay.reshape(const_6644.astype('uint64'), [4, 8, 9]), relay.reshape(const_6645.astype('float64'), [1080,]), ), 2)
call_6646 = relay.TupleGetItem(func_5367_call(relay.reshape(var_6643.astype('uint64'), [1, 8, 9]), relay.reshape(const_6644.astype('uint64'), [4, 8, 9]), relay.reshape(const_6645.astype('float64'), [1080,]), ), 2)
func_4574_call = mod.get_global_var('func_4574')
func_4577_call = mutated_mod.get_global_var('func_4577')
const_6660 = relay.const([True,True,True,False,False,True,True,False,False,True,True,True,False,False,True,False,True,True,False,True,False,True,False,True,False,True,True,False,True,True,False,True,True,False,True,True,True,False,True,True,False,False,False,False,False,False,False,False,True,False,True,True,True,True,True,True,True,False,False,False,True,False,True,False,False,False,True,False,True,False,True,True,True,False,True,True,False,True,True,True,True,False,True,True,False,False,False,True,False,False,True,True,True,True,False,True,True,True,True,False,False,True,True,True,True,False,False,True,True,False,False,True,False,True,False,False,True,False,True,True,True,True,True,False,False,True,True,True,False,True,False,False,False,True,True,True,False,False,False,True,False,False,False,False,False,False,True,True,True,False,True,False,True,False,False,True,True,True,True,True,False,True,False,False,False,True,True,False,True,True,False,True,False,False,False,False,True,True,True,False,True,False,False,True,False,False,False,True,True,True,True,False,False,True,False,True,False,False,True,False,True,True,True,True,False,True,True,True,False,True,True,False,True,True,True,False,True,True,True,False,True,False,False,True,True,True,False,False,True,False,False,False,True,True,False,True,True,True,False,True,False,True,True,False,False,False,False,True,False,True,False,True,False,False,False,True,True,True,True,False,True,True,True,False,True,True,False,False,False,False,True,True,False,True,True,False,True,True,False,True,False,False,False,False,False,True,False,False,False,True,False,True,True,True,True,False,False,True,False,True,False,True,False,False,False,True,False,False,False,False,True,False,False,False,True,True,True,True,True,True,False,True,False,True,True,True,True,True,True,True,False,True,True,False,True,True,True,True,True,True,False,True,False,False,True,True,True,False,False,False,True,False,False,True,False,True,False,True,False,True,True,True,False,False,True,True,True,True,True,True,False,True,False,False,True,True,True,True,True,True,True,False,False,True,True,False,False,True,True,True,True,False,False,True,False,True,True,False,False,False,True,True,True,True,True,False,False,True,True,True,False,True,True,False,False,False,False,True,True,False,False,False,False,False,False,True,True,True,True,False,True,False,True,False,True,False,False,True,True,False,False,False,True,True,False,True,True,True,False,False,True,False,True,True,False,True,False,False,False,True,False,True,True,True,True,False,True,True,True,True,True,True,True,False,False,True,False,True,False,False,False,True,True,True,True,True,False,True,True,False,True,True,True,False,False,False,True,False,True,False,True,True,False,False,True,False,True,True,False,False,False,False,True,True,True,False,False,True,False,False,True,True,True,False,True,False,False,False,False,True,True,True,False,True,True,False,True,False,True,True,False,True,True,False,False,False,False,True,True,False,True,False,True,False,False,True,False,False,True,False,False,False,True,False,True,False,False,True,True,False,False,True,True,False,True,False,False,False,True,False,False,False,False,False,False,True,True,True,True,False,True,True,True,True,False,False,True,False,True,False,False,False,False,False,False,True,False,False,True,True,False,False,True,True,False,True,False,True,False,True,True,False,True,False,True,True,True,False,True,False,True,False,False,True,False,False,False,False,True,False,True,True,False,False,False,False,True,False,True,False,False,False,False,True,True,True,False,False,True,True,False,False,True,True,True,True,True,False,True,False,False,False,False,False,False,False,False,False,True,True,False,True,True,False,False,False,True,False,False,False,True,True,True,True,False,False,False,True,False,False,False,False,False,False,False,True,False,False,True,True,True,True,False,True,True,False,True,False,False,False,False,False,True,True,True,True,False,True,False,False,True,False,True,False,False,True,True,True,False,False,False,True,True,True,False,False,True,False,False,False,False,False,False,True,False,True,False,False,False,False,False,False,True,True,False,True,True,True,False,True,True,True,False,False,False,True,False,True,True,False,True,True,False,True,False,False,False,False,False,True,False,True,True,True,False,True,True,True,False,True,False,True,False,True,True,False,False,True,False,True,True,True,False,True,True,False,False,True,False,False,False,False,True,True,False,False,False,True,True,False,False,False,True,True,True,False,True,True,True,True,False,False,True,False,False,False,False,False,True,False,False,False,False,False,True,False,False,False,True,True,False,False,True,False,True,False,False,False,True,False,False,True,False,True,True,False,True,True,False,False,True,True,False,False,True,False,False,True,False,False,False,False,False,False,False,True,False,True,True,False,True,True,True,True,False,True,False,True,False,False,False,False,True,False,False,False,False,False,True,False,False,False,True,False,False,True,True,False,False,True,False,True,False,False,True,True,True,True,False,True,True,False,True,True,True,True,True,True,False,True,False,False,True,True,True,True,False,False,True,True,True,False,False,False,False,True,True,True,False,True,False,False,False,False,True,True,True,False,False,True,True,False,False,False,True,True,True,False,True,True,True,True,True,True,True,True,True,False,False,True,True,False,True,True,False,False,False,False,True,True,True,False,True,True,True,True,False,False,True,False,True,False,True,False,True,False,True,False,False,True,False,True,False,True,True,False,False,True,False,True,False,False,True,False,True,False,True,False,True,False,False,False,False,True,True,True,True,False,False,True,False,False,False,False,True,True,False,True,True,True,False,True,True,False,True,False,False,False], dtype = "bool")#candidate|6660|(1078,)|const|bool
call_6659 = func_4574_call(relay.reshape(const_6660.astype('bool'), [11, 7, 14]))
call_6661 = func_4574_call(relay.reshape(const_6660.astype('bool'), [11, 7, 14]))
output = relay.Tuple([call_6623,call_6642,var_6643,const_6644,const_6645,call_6659,const_6660,])
output2 = relay.Tuple([call_6624,call_6646,var_6643,const_6644,const_6645,call_6661,const_6660,])
func_6669 = relay.Function([var_6643,], output)
mod['func_6669'] = func_6669
mod = relay.transform.InferType()(mod)
var_6670 = relay.var("var_6670", dtype = "uint64", shape = (72,))#candidate|6670|(72,)|var|uint64
output = func_6669(var_6670)
func_6671 = relay.Function([var_6670], output)
mutated_mod['func_6671'] = func_6671
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6685 = relay.var("var_6685", dtype = "int64", shape = (5, 3, 15))#candidate|6685|(5, 3, 15)|var|int64
var_6686 = relay.var("var_6686", dtype = "int64", shape = (5, 3, 15))#candidate|6686|(5, 3, 15)|var|int64
bop_6687 = relay.left_shift(var_6685.astype('int64'), relay.reshape(var_6686.astype('int64'), relay.shape_of(var_6685))) # shape=(5, 3, 15)
output = bop_6687
output2 = bop_6687
func_6694 = relay.Function([var_6685,var_6686,], output)
mod['func_6694'] = func_6694
mod = relay.transform.InferType()(mod)
mutated_mod['func_6694'] = func_6694
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6694_call = mutated_mod.get_global_var('func_6694')
var_6696 = relay.var("var_6696", dtype = "int64", shape = (5, 3, 15))#candidate|6696|(5, 3, 15)|var|int64
var_6697 = relay.var("var_6697", dtype = "int64", shape = (5, 3, 15))#candidate|6697|(5, 3, 15)|var|int64
call_6695 = func_6694_call(var_6696,var_6697,)
output = call_6695
func_6698 = relay.Function([var_6696,var_6697,], output)
mutated_mod['func_6698'] = func_6698
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6134_call = mod.get_global_var('func_6134')
func_6135_call = mutated_mod.get_global_var('func_6135')
call_6720 = relay.TupleGetItem(func_6134_call(), 0)
call_6721 = relay.TupleGetItem(func_6135_call(), 0)
output = call_6720
output2 = call_6721
func_6727 = relay.Function([], output)
mod['func_6727'] = func_6727
mod = relay.transform.InferType()(mod)
mutated_mod['func_6727'] = func_6727
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6727_call = mutated_mod.get_global_var('func_6727')
call_6728 = func_6727_call()
output = call_6728
func_6729 = relay.Function([], output)
mutated_mod['func_6729'] = func_6729
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6727_call = mod.get_global_var('func_6727')
func_6729_call = mutated_mod.get_global_var('func_6729')
call_6797 = func_6727_call()
call_6798 = func_6727_call()
func_2959_call = mod.get_global_var('func_2959')
func_2962_call = mutated_mod.get_global_var('func_2962')
const_6807 = relay.const([[-7,-2,10,-6,3,-8,-6,-7,-4],[7,-4,8,-1,-10,10,7,1,-10],[1,10,1,-10,-2,1,-5,-10,5],[7,-5,-6,4,-4,5,8,1,4],[5,-9,3,5,-8,-7,4,-2,-2],[6,4,-3,-4,-8,10,-7,10,-3],[5,10,-6,-8,-10,9,-9,-2,-5],[-3,-7,-3,5,-1,5,-7,-6,4],[4,2,2,-8,6,-5,4,-9,-1],[5,4,10,-1,-2,3,-9,-7,3],[-2,-2,10,9,-7,4,-3,-5,-6],[-10,3,-6,-7,-5,7,6,8,8],[-9,-1,-5,6,5,-9,-10,10,9],[2,-2,-2,7,-8,8,-3,3,3],[1,6,-3,-9,-3,6,4,8,7],[4,-8,8,-8,-2,9,9,-5,7],[9,10,-4,4,4,-5,3,-6,-2],[6,-7,3,6,-5,-6,-10,10,-8],[6,-2,5,-5,7,-1,4,-2,-8],[7,4,4,8,-6,-3,3,-6,4],[-4,-4,-8,1,2,7,8,-3,-7],[4,-2,4,-5,-7,-5,6,9,10],[3,-3,7,-7,3,-7,1,-8,2],[-8,-10,-9,7,-4,-3,6,-8,-3],[9,9,-3,4,6,5,-3,-4,-10],[-10,8,3,-8,1,10,-2,5,-2],[-6,2,-6,1,-2,4,9,10,8],[1,2,4,8,-10,-7,-3,9,-8],[-2,6,-5,-7,4,2,-1,-8,8],[7,-9,-1,1,1,7,5,-8,7],[-1,6,4,-7,-4,9,8,8,-5],[6,-2,6,-6,-1,1,-8,4,10],[-5,-2,4,2,7,1,-10,-10,4],[2,-6,-6,2,-1,-7,2,-8,10],[-6,-3,-2,-9,-3,-5,-6,9,-1],[-10,9,9,4,8,8,3,-10,-10],[-3,7,7,-5,8,-6,-10,-1,-8],[5,-4,4,-2,-5,-5,9,6,-6],[-9,-8,4,5,8,3,8,8,2]], dtype = "int16")#candidate|6807|(39, 9)|const|int16
call_6806 = func_2959_call(relay.reshape(const_6807.astype('int16'), [13, 9, 3]))
call_6808 = func_2959_call(relay.reshape(const_6807.astype('int16'), [13, 9, 3]))
output = relay.Tuple([call_6797,call_6806,const_6807,])
output2 = relay.Tuple([call_6798,call_6808,const_6807,])
func_6815 = relay.Function([], output)
mod['func_6815'] = func_6815
mod = relay.transform.InferType()(mod)
output = func_6815()
func_6816 = relay.Function([], output)
mutated_mod['func_6816'] = func_6816
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6336_call = mod.get_global_var('func_6336')
func_6338_call = mutated_mod.get_global_var('func_6338')
call_6817 = func_6336_call()
call_6818 = func_6336_call()
output = call_6817
output2 = call_6818
func_6824 = relay.Function([], output)
mod['func_6824'] = func_6824
mod = relay.transform.InferType()(mod)
output = func_6824()
func_6825 = relay.Function([], output)
mutated_mod['func_6825'] = func_6825
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6134_call = mod.get_global_var('func_6134')
func_6135_call = mutated_mod.get_global_var('func_6135')
call_6829 = relay.TupleGetItem(func_6134_call(), 0)
call_6830 = relay.TupleGetItem(func_6135_call(), 0)
output = relay.Tuple([call_6829,])
output2 = relay.Tuple([call_6830,])
func_6841 = relay.Function([], output)
mod['func_6841'] = func_6841
mod = relay.transform.InferType()(mod)
output = func_6841()
func_6842 = relay.Function([], output)
mutated_mod['func_6842'] = func_6842
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5978_call = mod.get_global_var('func_5978')
func_5979_call = mutated_mod.get_global_var('func_5979')
call_6865 = func_5978_call()
call_6866 = func_5978_call()
func_6841_call = mod.get_global_var('func_6841')
func_6842_call = mutated_mod.get_global_var('func_6842')
call_6890 = relay.TupleGetItem(func_6841_call(), 0)
call_6891 = relay.TupleGetItem(func_6842_call(), 0)
bop_6892 = relay.less_equal(call_6865.astype('bool'), relay.reshape(call_6890.astype('bool'), relay.shape_of(call_6865))) # shape=(9, 2, 6)
bop_6895 = relay.less_equal(call_6866.astype('bool'), relay.reshape(call_6891.astype('bool'), relay.shape_of(call_6866))) # shape=(9, 2, 6)
uop_6902 = relay.sin(call_6890.astype('float64')) # shape=(9, 2, 6)
uop_6904 = relay.sin(call_6891.astype('float64')) # shape=(9, 2, 6)
output = relay.Tuple([bop_6892,uop_6902,])
output2 = relay.Tuple([bop_6895,uop_6904,])
func_6909 = relay.Function([], output)
mod['func_6909'] = func_6909
mod = relay.transform.InferType()(mod)
output = func_6909()
func_6910 = relay.Function([], output)
mutated_mod['func_6910'] = func_6910
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6909_call = mod.get_global_var('func_6909')
func_6910_call = mutated_mod.get_global_var('func_6910')
call_6921 = relay.TupleGetItem(func_6909_call(), 0)
call_6922 = relay.TupleGetItem(func_6910_call(), 0)
output = call_6921
output2 = call_6922
func_6928 = relay.Function([], output)
mod['func_6928'] = func_6928
mod = relay.transform.InferType()(mod)
output = func_6928()
func_6929 = relay.Function([], output)
mutated_mod['func_6929'] = func_6929
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6727_call = mod.get_global_var('func_6727')
func_6729_call = mutated_mod.get_global_var('func_6729')
call_6955 = func_6727_call()
call_6956 = func_6727_call()
func_6841_call = mod.get_global_var('func_6841')
func_6842_call = mutated_mod.get_global_var('func_6842')
call_6965 = relay.TupleGetItem(func_6841_call(), 0)
call_6966 = relay.TupleGetItem(func_6842_call(), 0)
output = relay.Tuple([call_6955,call_6965,])
output2 = relay.Tuple([call_6956,call_6966,])
func_6983 = relay.Function([], output)
mod['func_6983'] = func_6983
mod = relay.transform.InferType()(mod)
mutated_mod['func_6983'] = func_6983
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6983_call = mutated_mod.get_global_var('func_6983')
call_6984 = func_6983_call()
output = call_6984
func_6985 = relay.Function([], output)
mutated_mod['func_6985'] = func_6985
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6909_call = mod.get_global_var('func_6909')
func_6910_call = mutated_mod.get_global_var('func_6910')
call_6986 = relay.TupleGetItem(func_6909_call(), 1)
call_6987 = relay.TupleGetItem(func_6910_call(), 1)
uop_6989 = relay.tan(call_6986.astype('float32')) # shape=(9, 2, 6)
uop_6991 = relay.tan(call_6987.astype('float32')) # shape=(9, 2, 6)
bop_6998 = relay.less(call_6986.astype('bool'), relay.reshape(uop_6989.astype('bool'), relay.shape_of(call_6986))) # shape=(9, 2, 6)
bop_7001 = relay.less(call_6987.astype('bool'), relay.reshape(uop_6991.astype('bool'), relay.shape_of(call_6987))) # shape=(9, 2, 6)
func_1580_call = mod.get_global_var('func_1580')
func_1586_call = mutated_mod.get_global_var('func_1586')
var_7005 = relay.var("var_7005", dtype = "int32", shape = (180,))#candidate|7005|(180,)|var|int32
const_7006 = relay.const([3,-1,-2,3,-7,-3,-7,-9,7,8,-10,7,2,1,6,-9,10,2,-6,-7,-7,1,5,6,-3,-1,-9,-6,-2,8,-5,-9,-6,8,-5,2,-7,6,4,-5,-8,-10,7,-5,-3,8,-1,-4,9,6,6,6,2,7,-3,3,-1,10,8,-8,10,10,5,6,-5,10,2,-5,9,10,-6,-5,5,6,1,-6,-2,-4,-10,10,5,-7,7,1,5,10,-4,10,-2,-7,-10,6,9,8,-10,-5,10,10,-5,5,-2,-1,2,10,-10,9,-9,-4,4,-10,-2,-9,-8,-2,-2,2,4,2,7,-1,8,6,4,-8,2,3,4,6,1,-6,5,-6,-3,6,-2,-8,-7,-2,6,9,7,-2,6,-2,6,-1,-5,-1,-7,10,-5,4,5,-5,5,7,-8,2,6,10,-3,4,-9,-8,-1,-8,7,10,-7,2,-9,-3,-7,10,10,-7,2,-10,-6,7,-7,6,6,-7,-9,4,-8,-6,1,-10,7,-5,9,-9,-4,-4,9,8,-4,-8,-3,-2,1,-6,3,5,-5,8,-6,1,-1,-2,5,-8,4,-3,-2,6,2,-6,-1,-4,1,-2,-6,8,10,-10,9,-5,7,8,2,1,-7,8,9,-4,-1,-1,3,-6,7,-9,7,-9,-1,-4,-10,-4,3,5,-3,4,7,-5,-5,5,-9,8,8,2,4,-10,-8,-3,8,5,-9,7,4,-8,3,1,-6,1,8,-1,7,9,8,8,-10,-9,-4,6,-10,-9,6,6,10,-5,-1,3,10,5,1,-5,-8,1,3,-10,-10,6,8,7,1,6,-10,2,-10,7,-2,-4,7,10,3,-2,8,8,-10,-6,8,-5,-3,-6,3,4,-8,-4,4,-4,6,1,-4,4,5,-4,-1,1,5,-7,-3,-4,1,-7,-3,-3,6,7,-2,-3,10,-2,-6,7,2,-2,6,7,1,4,2,-5,1,8,10,2,9,-2,-7,-10,2,-4,-5,8,3,-2,-9,-7,8,4,9,9,-10,-4,-10,3,-6,10,8,-7,-10,-9,-7,-9,-2,-4,-1,-8,4,7,8,-5,9,-4,-5,-9,2,-6,-4,4,10,-4,1,-1,6,8,-7,8,10,4,-7,-2,3,-7,-3,-1,-9,5,1,-6,1,2,-8,-4,6,-6,3,1,-6,-10,-3,3,10,-3,-3,7,-4,-1,-3,1,-5,2,4,3,-6,-8,-6,1,10,-6,-5,-6,5,-9,4,-8,6,-8,-5,-10,-4,10,-1,7,-4,-4,-7,8,-6,10,9,-1,-8,-5,2,4,4,-7,4,6,-6,-9,-9,-6,-3,8,-4,7,10,5,-7,-5,4,4,5,-7,10,-7,-2,5,9,7,2,7,8,-1,4,4,9,3,-9,6,-6,-8,6,-4,-7,-10,9,-1,3,9,-10,-3,-2,5,-7,-3,-4,1,-6,-6,-10,-4,-8,-3,6,6,7,-5,6,-2,-2,7,-6,7,3,-7,-4,1,5,-10,-8,-9,6,7,5,-6,-6,3,1,-6,-5,-7,-3,8,-4,8,-5,-10,2,-4,9,-4,-4,7,-6,10,-5,10,-7,5,-9,5,2,8,5,3,-3,-8,-3,-2,9,4,-1,3,5,9,-3,-1,-2,-2,-10,-10,1,1,3,7,-7,8,-5,4,-1,7,1,-2,6,9,-9,10,5,6,-7,1,-1,-10,10,-8,10,6,3,4,1,5,10,-10,9,4,8,-9,-4,5,6,-6,1,8,1,-3,-5,4,4,-2,-9,-10,-2,6,-10,2,8,-4,2,-3,6,-9,4,8,-7,-2,9,-5,-9,-8,4,6,-10,3,2,8,1,9,-9,5,9,4,7,10,-2,8,-2,10,-5,-5,8,-5,3,6,2,9,9,9,5,-4,10,3,-6,-4,-3,-8,-4,-9,8,10,9,9,-5,5,-10,4,-3,-9,-7,10,4,10,2,7,-7,1,-6,-3,1,-8,-7,8,-1,-6,2,10,-5,-5,2,-10,9,-2,-2,-6,10,-1,-10,6,-7,-10,10,6,2,6,-3,10,6,9,-6,-10,-2,-5,1,4,4,9,-3,1,4,9,2,1,3,5,-6,-10,-7,1,-6,5,8,-6,-7,-8,4,10,7,5,1,3,-6,-4,-8,10,9,-6,9,7,10,-7,-3,2,8,3,-1,5,-7,-10,-5,1,-6,-10,-8,1,2,-4,-6,-6,6,-2,-4,-4,-7,8,-7,-5,-3,-9,1,10,-7,8,-1,-8,4,3,6,-2,4,-4,-6,-5,3,1,4,-7,8,-6,2,5,3,-7,-5,-3,-7,-1,3,4,-2,10,-10,10,-2,6,-2,1,9,4,5,5,4,6,4,5,-7,-3,-10,3,-1,8,-10,-9,-7,2,-10,-5,-3,-4,-1,2,-2,4,-9,-5,-8,2,-2,-8,3,10,-9,10,5,8,2,5,4,-7,-8,1,-7,-5,-5,-9,-3,2,5,-3,-5,-6,10,3,3,-6,4,7,2,2,5,6,2,1,1,6,6,4,-5,9,-7,-9,2,-4,-9,2,10,3,7,9,-1,-3,-9,2,-6,-4,-6,5,10,-4,8,3,5,1,-4,-7,5,2,1,-10,3,-7,8,8,-1,-6,-8,10,7,-5,-10,-7,-6,-1,-1,1,6,4,2,-1,-4,-4,8,-8,-3,-7,7,2,-3,8,3,-9,-7,-10,-6,-2,7,-3,-9,-1,5,-9,-2,-4,3,8,-3,-2,1,-1,-4,5,10,8,2,4,-7,-10,6,-3,-7,-3,-7,1,7,-3,5,-4,-10,4,10,-9,-3,-6,-2,7,10,-10,-5,3,2,-4,-5,-2,1,-7,8,-7,-3,-1,4,4,8,-8,-4,-6,10,5], dtype = "int32")#candidate|7006|(1080,)|const|int32
var_7007 = relay.var("var_7007", dtype = "uint64", shape = (14, 64))#candidate|7007|(14, 64)|var|uint64
var_7008 = relay.var("var_7008", dtype = "uint32", shape = (70,))#candidate|7008|(70,)|var|uint32
call_7004 = relay.TupleGetItem(func_1580_call(relay.reshape(var_7005.astype('int32'), [1, 12, 15]), relay.reshape(const_7006.astype('int32'), [6, 12, 15]), relay.reshape(var_7007.astype('uint64'), [896,]), relay.reshape(var_7008.astype('uint32'), [7, 10]), ), 4)
call_7009 = relay.TupleGetItem(func_1586_call(relay.reshape(var_7005.astype('int32'), [1, 12, 15]), relay.reshape(const_7006.astype('int32'), [6, 12, 15]), relay.reshape(var_7007.astype('uint64'), [896,]), relay.reshape(var_7008.astype('uint32'), [7, 10]), ), 4)
output = relay.Tuple([bop_6998,call_7004,var_7005,const_7006,var_7007,var_7008,])
output2 = relay.Tuple([bop_7001,call_7009,var_7005,const_7006,var_7007,var_7008,])
func_7018 = relay.Function([var_7005,var_7007,var_7008,], output)
mod['func_7018'] = func_7018
mod = relay.transform.InferType()(mod)
var_7019 = relay.var("var_7019", dtype = "int32", shape = (180,))#candidate|7019|(180,)|var|int32
var_7020 = relay.var("var_7020", dtype = "uint64", shape = (14, 64))#candidate|7020|(14, 64)|var|uint64
var_7021 = relay.var("var_7021", dtype = "uint32", shape = (70,))#candidate|7021|(70,)|var|uint32
output = func_7018(var_7019,var_7020,var_7021,)
func_7022 = relay.Function([var_7019,var_7020,var_7021,], output)
mutated_mod['func_7022'] = func_7022
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5978_call = mod.get_global_var('func_5978')
func_5979_call = mutated_mod.get_global_var('func_5979')
call_7032 = func_5978_call()
call_7033 = func_5978_call()
func_4870_call = mod.get_global_var('func_4870')
func_4876_call = mutated_mod.get_global_var('func_4876')
var_7035 = relay.var("var_7035", dtype = "float64", shape = (112, 2))#candidate|7035|(112, 2)|var|float64
var_7036 = relay.var("var_7036", dtype = "float32", shape = (56, 12))#candidate|7036|(56, 12)|var|float32
var_7037 = relay.var("var_7037", dtype = "int32", shape = (180,))#candidate|7037|(180,)|var|int32
const_7038 = relay.const([-7,-7,-2,1,-8,-8,-6,8,7,-9,1,5,8,1,7,7,10,-10,8,6,-4,9,-3,8,-10,3,2,3,-7,9,6,-7,9,7,-9,-5,7,3,-1,-4,-9,10,4,1,-10,7,-8,10,-2,-7,2,-3,6,-3,-8,5,3,-7,1,-10,8,-4,-2,4,-1,-6,-4,4,-7,-6,3,2,-9,2,-9,-8,10,5,-6,5,-1,4,3,3,6,-7,-1,4,-10,-9,-9,-7,-8,-10,-1,-6,9,8,-8,2,-10,-5,-9,-2,-7,9,-5,4,9,2,10,-2,9,-1,-1,-3,1,4,6,9,7,9,4,-7,-1,3,-8,2,-7,6,-5,10,6,-6,-2,-6,-2,-10,10,9,8,-3,-1,6,8,-5,-1,-7,-3,-9,-9,-3,-10,9,-2,-1,2,-9,-1,-10,-8,-1,2,-8,-2,-1,2,4,-6,-1,-1,9,10,-6,-6,1,-1,-5,-10,-1,9,-5,-3,10,10,-6,-8,6,-4,1,9,3,2,-7,10,7,8,-10,-9,-10,6,1,10,1,8,-1,-2,8,-4,-8,-1,-6,5,1,8,2,-7,7,-10,1,-10,6,-9,-8,9,7,-1,10,9,-9,-1,3,5,5,-10,-3,9,6,2,-8,10,-3,-8,-6,-4,-6,-5,3,10,-5,-4,-3,-6,2,-3,-8,-6,5,-4,3,-5,3,5,-9,-3,5,3,-2,-9,8,5,-6,-9,-8,-1,10,-7,7,8,9,2,-1,-4,-3,-7,6,9,6,-4,-8,3,-2,-1,-4,-6,-10,-7,-3,-6,-3,-9,7,-2,3,-7,-2,1,3,-4,2,-8,-6,5,-5,8,-4,-8,5,5,-7,-1,3,4,5,-2,7,1,-4,-5,-5,-8,1,1,-5,4,-9,10,10,-9,-3,-3,-1,-4,-9,4,3,3,8,-10,10,-5,-10,10,-1,6,-10,-4,3,5,-10,-6,-3,-9,-4,-3,2,3,7,5,-4,3,9,-6,9,2,2,-2,-10,-7,-9,-9,10,-6,-9,6,9,-7,7,1,-5,-5,5,-4,-8,7,1,8,-2,-10,-5,-2,4,-5,5,8,10,-10,1,-8,-5,6,-5,-1,1,5,6,10,-1,4,10,-7,-5,5,-1,7,-10,-5,-9,9,6,6,5,3,-1,-1,8,1,-5,1,9,-3,3,3,2,2,8,-9,3,7,8,-3,6,-10,-10,8,-1,10,6,-5,-5,-8,4,6,-1,9,2,6,8,10,8,-9,8,-10,3,5,-2,-3,-2,4,-1,-3,-7,-1,-6,4,9,-3,-3,1,8,-5,9,-9,-6,-4,-9,10,-5,-2,-1,5,10,-5,10,-10,-4,-3,5,-3,6,-6,4,1,-6,-10,-9,-7,2,-1,-1,-3,8,-7,-7,-1,-10,7,4,3,1,9,10,-7,1,5,1,-5,3,9,2,2,-9,-6,-7,5,4,-5,9,9,2,-1,1,1,8,3,-1,2,3,5,8,-5,-3,9,4,3,1,8,-10,9,10,5,-6,-1,6,-7,5,9,4,-1,7,6,-6,3,5,3,3,-5,7,-7,2,-9,8,5,7,2,-10,1,3,3,5,3,3,6,6,3,7,-6,-10,-7,-9,-1,7,6,-8,-8,-2,-1,-3,-7,8,10,3,-10,-9,10,-8,-8,4,5,-2,5,5,10,-2,-8,6,8,4,-2,7,-4,4,-9,5,-10,-6,2,10,-9,1,-5,-5,-6,-10,-3,-2,-3,-8,-5,-4,-3,-8,2,-9,2,-2,6,-7,8,1,-8,10,-9,4,5,-7,-10,1,6,-7,-9,3,-6,-6,-10,8,1,-9,-6,4,-3,-8,-9,7,1,2,-2,-3,-5,-3,-7,-1,8,-7,-3,6,4,-10,-4,-6,10,-5,3,3,7,3,6,10,-5,8,10,5,9,4,-2,-10,-10,-5,3,1,3,-1,9,4,-10,4,-8,1,4,-3,-8,9,8,-1,3,10,-5,6,4,-9,-4,-4,4,10,-3,-6,-7,-10,-10,-5,-2,-10,6,2,6,6,-6,2,6,-8,6,1,-9,-10,2,4,2,3,-10,10,10,-5,4,4,9,10,-6,-1,-4,5,-8,-3,3,-6,3,-8,-2,9,10,8,5,-5,3,-5,-8,-4,-9,5,-5,4,9,-10,7,-6,3,6,-4,-9,8,-3,-4,1,5,5,8,-7,1,7,9,5,-9,-1,4,7,6,8,-8,3,-6,-3,-8,-1,-10,-9,4,-2,-4,4,-5,-10,5,-2,1,-8,6,3,-4,2,-5,-2,4,-1,-6,-6,8,-3,6,-7,3,-5,-7,-2,5,4,5,-8,-9,-7,4,8,-1,-6,-6,-5,-8,-7,-9,7,-3,1,-8,-4,7,-4,5,4], dtype = "uint64")#candidate|7038|(896,)|const|uint64
call_7034 = relay.TupleGetItem(func_4870_call(relay.reshape(var_7035.astype('float64'), [2, 8, 14]), relay.reshape(var_7036.astype('float32'), [672,]), relay.reshape(var_7037.astype('int32'), [180,]), relay.reshape(const_7038.astype('uint64'), [896,]), ), 6)
call_7039 = relay.TupleGetItem(func_4876_call(relay.reshape(var_7035.astype('float64'), [2, 8, 14]), relay.reshape(var_7036.astype('float32'), [672,]), relay.reshape(var_7037.astype('int32'), [180,]), relay.reshape(const_7038.astype('uint64'), [896,]), ), 6)
const_7050 = relay.const([[-5.726945,-0.750284],[-5.699886,-8.806225],[-5.166636,7.519772],[-9.662595,7.014540],[4.834128,1.225467],[2.256237,8.909236],[8.241805,-6.956518],[-6.989758,2.843407],[-8.893401,6.100584],[8.012728,-7.875025],[-5.280645,9.042621],[7.719154,-7.086999],[-5.567986,-5.809789],[-6.127043,-8.951836],[-9.273869,-7.887796],[-9.275660,4.919161],[5.285127,3.357647],[-0.965177,-1.235563],[-0.630434,2.849177],[-9.088766,-1.724012],[-5.531453,-2.136883],[-0.407609,-6.152923],[6.455068,6.572416],[-4.479441,9.926703],[9.135980,-7.387697],[-2.988059,-1.007406],[-0.740046,-0.349661],[-3.979611,8.601487],[-1.930288,2.181054],[-3.344720,9.228808],[-0.046612,6.567679],[1.232172,0.807020],[-3.213383,-8.459763],[-6.455246,5.940747],[-2.061362,-2.847782],[-8.858344,4.706119],[3.938782,-0.881512],[-3.750589,-3.881988],[-0.394504,7.305372],[-9.278287,2.414653],[-1.956600,5.914440],[-5.916122,2.198025],[-0.943091,9.177600],[5.739328,4.360104],[3.202344,-5.230017],[3.186718,7.146793],[5.114392,3.919120],[7.098373,-4.755636],[-5.777863,-1.817019],[-4.654942,-3.809796],[5.428713,4.464132],[-9.061441,-7.545991],[-0.815362,-0.563451],[6.037216,-1.121248],[-0.752784,-3.559827],[-7.985809,-6.416371],[-4.846657,4.107153],[-6.821766,0.400090],[-8.465588,2.067429],[-2.625845,-2.585882],[-2.539484,-3.751511],[-3.038765,-4.547978],[2.867238,-9.709707],[6.442412,-6.790717],[-3.399387,-3.633922],[8.763042,-4.604006],[4.597594,1.177903],[4.595502,-0.320101],[-1.825738,4.679515],[8.267922,3.971699],[-7.444443,-1.608037],[-6.528616,6.885860],[1.277218,-8.777086],[-1.630214,-4.152139],[-8.195251,9.230226],[9.767825,7.881911],[-0.524984,3.338509],[0.607268,-4.146687],[-3.742268,5.824214],[-9.167455,2.675513],[6.187809,-6.708124],[8.684952,6.845606],[-2.662572,8.379721],[-8.364159,6.688993],[-7.676219,2.407899],[-4.735820,5.940885],[-5.591512,7.615119],[-4.508567,-8.401054],[-2.114008,7.994666],[8.675338,1.840123],[8.149130,-1.575443],[-1.757235,-8.415340],[-1.362796,-3.764185],[-5.198318,0.096352],[-1.818295,4.986877],[-0.030134,-1.625127],[-7.264824,-5.633775],[-6.164886,-0.295692],[-7.546342,-0.374471],[-3.251425,6.264395],[-9.424608,8.704724],[-9.171576,3.331248],[-1.345496,9.188639],[9.130932,6.547032],[5.746248,3.435757],[-6.591095,5.343330],[-3.355276,0.651167],[-1.556823,7.097305],[-0.451570,8.414207],[-9.859564,9.559596],[0.713868,4.324226],[8.129018,1.736687]], dtype = "float64")#candidate|7050|(112, 2)|const|float64
bop_7051 = relay.subtract(var_7035.astype('uint16'), relay.reshape(const_7050.astype('uint16'), relay.shape_of(var_7035))) # shape=(112, 2)
output = relay.Tuple([call_7032,call_7034,var_7036,var_7037,const_7038,bop_7051,])
output2 = relay.Tuple([call_7033,call_7039,var_7036,var_7037,const_7038,bop_7051,])
func_7056 = relay.Function([var_7035,var_7036,var_7037,], output)
mod['func_7056'] = func_7056
mod = relay.transform.InferType()(mod)
mutated_mod['func_7056'] = func_7056
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7056_call = mutated_mod.get_global_var('func_7056')
var_7058 = relay.var("var_7058", dtype = "float64", shape = (112, 2))#candidate|7058|(112, 2)|var|float64
var_7059 = relay.var("var_7059", dtype = "float32", shape = (56, 12))#candidate|7059|(56, 12)|var|float32
var_7060 = relay.var("var_7060", dtype = "int32", shape = (180,))#candidate|7060|(180,)|var|int32
call_7057 = func_7056_call(var_7058,var_7059,var_7060,)
output = call_7057
func_7061 = relay.Function([var_7058,var_7059,var_7060,], output)
mutated_mod['func_7061'] = func_7061
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6909_call = mod.get_global_var('func_6909')
func_6910_call = mutated_mod.get_global_var('func_6910')
call_7067 = relay.TupleGetItem(func_6909_call(), 0)
call_7068 = relay.TupleGetItem(func_6910_call(), 0)
output = relay.Tuple([call_7067,])
output2 = relay.Tuple([call_7068,])
func_7075 = relay.Function([], output)
mod['func_7075'] = func_7075
mod = relay.transform.InferType()(mod)
output = func_7075()
func_7076 = relay.Function([], output)
mutated_mod['func_7076'] = func_7076
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6727_call = mod.get_global_var('func_6727')
func_6729_call = mutated_mod.get_global_var('func_6729')
call_7117 = func_6727_call()
call_7118 = func_6727_call()
output = relay.Tuple([call_7117,])
output2 = relay.Tuple([call_7118,])
func_7121 = relay.Function([], output)
mod['func_7121'] = func_7121
mod = relay.transform.InferType()(mod)
output = func_7121()
func_7122 = relay.Function([], output)
mutated_mod['func_7122'] = func_7122
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7172 = relay.var("var_7172", dtype = "int16", shape = (7, 14, 9))#candidate|7172|(7, 14, 9)|var|int16
var_7173 = relay.var("var_7173", dtype = "int16", shape = (7, 14, 9))#candidate|7173|(7, 14, 9)|var|int16
bop_7174 = relay.bitwise_and(var_7172.astype('int16'), relay.reshape(var_7173.astype('int16'), relay.shape_of(var_7172))) # shape=(7, 14, 9)
func_910_call = mod.get_global_var('func_910')
func_912_call = mutated_mod.get_global_var('func_912')
var_7179 = relay.var("var_7179", dtype = "int64", shape = (1260,))#candidate|7179|(1260,)|var|int64
call_7178 = relay.TupleGetItem(func_910_call(relay.reshape(var_7179.astype('int64'), [10, 14, 9])), 0)
call_7180 = relay.TupleGetItem(func_912_call(relay.reshape(var_7179.astype('int64'), [10, 14, 9])), 0)
output = relay.Tuple([bop_7174,call_7178,var_7179,])
output2 = relay.Tuple([bop_7174,call_7180,var_7179,])
func_7187 = relay.Function([var_7172,var_7173,var_7179,], output)
mod['func_7187'] = func_7187
mod = relay.transform.InferType()(mod)
var_7188 = relay.var("var_7188", dtype = "int16", shape = (7, 14, 9))#candidate|7188|(7, 14, 9)|var|int16
var_7189 = relay.var("var_7189", dtype = "int16", shape = (7, 14, 9))#candidate|7189|(7, 14, 9)|var|int16
var_7190 = relay.var("var_7190", dtype = "int64", shape = (1260,))#candidate|7190|(1260,)|var|int64
output = func_7187(var_7188,var_7189,var_7190,)
func_7191 = relay.Function([var_7188,var_7189,var_7190,], output)
mutated_mod['func_7191'] = func_7191
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6841_call = mod.get_global_var('func_6841')
func_6842_call = mutated_mod.get_global_var('func_6842')
call_7234 = relay.TupleGetItem(func_6841_call(), 0)
call_7235 = relay.TupleGetItem(func_6842_call(), 0)
func_5829_call = mod.get_global_var('func_5829')
func_5833_call = mutated_mod.get_global_var('func_5833')
var_7249 = relay.var("var_7249", dtype = "float64", shape = (1872,))#candidate|7249|(1872,)|var|float64
const_7250 = relay.const([0.174574,1.442379,-4.955994,2.974100,-7.340134,-3.137039,-5.646806,2.412908,-2.133196,2.020184,8.199204,2.652950,7.653438,-5.994387,0.561436,9.728985,-4.407737,5.014491,-1.337463,-7.909936,6.789670], dtype = "float64")#candidate|7250|(21,)|const|float64
const_7251 = relay.const([-4,-8,5,-9,6,-4,10,-1,6,-2,-1,-5,9,-1,1,-10,2,-4,-1,-4,10,8,-5,-6,1,5,6,-6,-9,7,-2,9,-6,9,-5,-2,2,-6,1,9,1,3,6,-2,6,-7,6,-2,-8,-10,5,-1,-4,-5,8,-8,-8,8,-8,-8,-8,3,-10,6,6,-10,-8,8,-7,-8,7,-8,6,-8,4,1,1,-8,8,9,-10,5,-2,-1,-7,6,4,2,9,6,-8,-7,-10,-9,9,-2,-7,-6,-1,-7,-5,-6,-6,10,-10,1,1,6,5,10,3,10,9,10,10,-2,-2,-3,-7,-6,-9,-5,-6,-2,6,2,5,1,7,-6,9,-3,8,-9,-1,4,-1,2,9,8,-7,-5,2,6,5,8,2,5,1,7,-1,4,9,1,10,-3,8,9,2,-1,9,-3,5,3,3,10,10,-10,-9,-6,10,10,-5,-10,-6,8,-2,-8,-10,-5,-10,9,-8,-10,-9,10,6,-9,-8,-10,2,10,8,5,9,-2,-2,1,-1,-10,7,-2,-7,4,2,10,1,-9,7,8,1,-7,1,6,-10,2,4,10,5,-9,-9,10,-8,-10,3,3,6,-1,-9,-10,-3,8,-6,-1,2,9,-8,1,8,-2,-9,-8,-6,-3,6,-6,6,6,-2,-5,8,8,-3,-3,10,3,-2,-6,10,5,-3,-4,-5,-10,-9,5,-9,5,-2,2,-4,3,7,-4,7,2,-10,-10,9,6,-7,7,-2,7,-3,-7,-5,4,-8,-9,-8,6,9,5,-7,10,-1,-9,1,8,8,-10,-4,7,3,-8,8,10,-1,7,-5,-10,-4,-9,9,-1,-3,-10,-7,10,2,2,-3,9,-7,-1,-3,-1,2,-4,-7,7,-7,-6,3,-4,-7,7,9,5,-2,2,-9,-4,1,3,-4,8,7,-4,4,-7,6,-1,10,5,-4,7,8,-4,1,8,8,-5,-2,5,-8,-6,-6,1,5,-10,-3,-2,-10,1,-4,5,5,-6,10,2,4,6,5,6,5,8,-4,-8,-7,-4,-6,-4,10,7,-1,-1,6,-5,-5,10,-8,8,1,6,5,-10,2,3,5,-3,-8,9,10,-7,-6,4,7,6,8,-5,-6,7,10,10,-1,-2,-5,-4,-7,-9,8,-7,-7,-3,6,1,5,-10,7,2,10,8,-5,2,3,-4,-7,6,-5,1,8,-5,-8,-10,2,-5,-6,-10,7,-4,5,1,-1,6,-9,9,-6,2,7,3,6,6,2,4,9,-10,-7,4,2,-4,-6,-8,-7,-10,-2,6,10,-1,-9,2,4,10,-2,1,-6,-5,-10,-7,-3,1,-10,5,-2,-4,1,9,-7,1,3,5,9,-4,-3,5,-7,-3,-7,9,-5,10,-1,3,8,-9,-6,-2,6,-3,4,7,8,10,-10,-5,-2,-1,4,2,8,4,-8,10,-10,-7,2,-8,5,6,-7,-10,-7,-3,-7,-6,-6,10,5,-10,-4,1,-10,-6,7,10,-6,2,-1,6,-9,2,3,1,-3,-4,7,-3,-4,-4,3,-2,6,2,-10,7,3,7,3,-3,-1,3,2,-7,-5,5,6,-6,-5,2,-9,5,8,9,9,10,-10,-10,-9,9,9,-3,-5,-9,-9,6,-2,3,2,-3,-5,3,-8,-10,-9,2,-6,6,5,-2,8,4,6,2,-9,-10,-10,2,7,6,10,5,4,-7,-7,-5,4,7,-9,9,3,-4,4,2,7,-9,-5,-5,6,-8], dtype = "int64")#candidate|7251|(660,)|const|int64
call_7248 = relay.TupleGetItem(func_5829_call(relay.reshape(var_7249.astype('float64'), [16, 9, 13]), relay.reshape(const_7250.astype('float64'), [21,]), relay.reshape(const_7251.astype('int64'), [660,]), ), 0)
call_7252 = relay.TupleGetItem(func_5833_call(relay.reshape(var_7249.astype('float64'), [16, 9, 13]), relay.reshape(const_7250.astype('float64'), [21,]), relay.reshape(const_7251.astype('int64'), [660,]), ), 0)
var_7264 = relay.var("var_7264", dtype = "float64", shape = (16, 9, 13))#candidate|7264|(16, 9, 13)|var|float64
bop_7265 = relay.less(call_7248.astype('bool'), relay.reshape(var_7264.astype('bool'), relay.shape_of(call_7248))) # shape=(16, 9, 13)
bop_7268 = relay.less(call_7252.astype('bool'), relay.reshape(var_7264.astype('bool'), relay.shape_of(call_7252))) # shape=(16, 9, 13)
func_1580_call = mod.get_global_var('func_1580')
func_1586_call = mutated_mod.get_global_var('func_1586')
var_7270 = relay.var("var_7270", dtype = "int32", shape = (3, 60))#candidate|7270|(3, 60)|var|int32
const_7271 = relay.const([[-10,-2],[-4,-8],[6,-2],[-6,-3],[8,-2],[1,3],[3,-6],[9,-4],[1,-1],[7,-3],[-9,-9],[1,-1],[-9,7],[2,-8],[7,3],[-4,-5],[5,9],[7,6],[-6,-2],[-6,-5],[8,7],[-3,-5],[8,8],[-7,4],[-1,5],[-4,6],[5,-10],[-1,-5],[8,10],[-6,-6],[5,4],[-9,5],[3,9],[-2,-1],[3,9],[6,-4],[6,10],[9,6],[-9,5],[3,7],[-1,-3],[-3,1],[6,1],[-3,-8],[9,3],[-1,-9],[3,8],[5,10],[-6,-2],[-9,-3],[2,-7],[-9,6],[-3,5],[9,-6],[-1,8],[2,3],[-3,6],[-9,-9],[5,7],[-2,-3],[3,-1],[-3,7],[-3,-9],[5,2],[-8,-1],[9,7],[7,7],[9,6],[-9,8],[-6,-5],[2,-4],[9,-4],[-6,3],[7,7],[-6,-7],[6,8],[-2,7],[-1,-7],[-8,7],[-6,-4],[8,-8],[-9,-8],[3,9],[9,-5],[2,-9],[8,-4],[-6,6],[4,6],[9,-4],[1,3],[-9,3],[8,1],[2,2],[7,-6],[9,-4],[-2,-2],[4,-9],[-9,-9],[5,-8],[-10,2],[10,-1],[2,-7],[9,-1],[-2,4],[-10,-1],[5,7],[9,-2],[4,-10],[8,1],[-1,10],[-10,3],[-5,-7],[1,-3],[-7,-6],[-8,5],[2,8],[1,1],[-8,3],[5,9],[4,4],[4,-2],[10,7],[-6,-3],[10,-2],[1,-2],[-6,6],[-1,-1],[8,8],[5,-3],[8,6],[-2,6],[-10,-4],[4,9],[-9,3],[-9,4],[-2,-1],[2,5],[-4,8],[9,10],[2,2],[10,-6],[-8,8],[1,-5],[4,-1],[10,10],[6,1],[-10,5],[-7,-6],[8,-5],[-10,4],[-6,-6],[4,9],[-3,9],[-7,-7],[5,8],[8,-10],[-7,5],[-9,9],[-7,-6],[-4,7],[3,9],[10,6],[-9,-9],[2,5],[6,7],[8,-3],[-4,-6],[-5,6],[-10,-10],[4,-6],[-4,-9],[-4,-6],[-4,-8],[-2,7],[-1,2],[5,5],[-6,4],[5,-10],[4,-3],[-4,9],[-3,-2],[7,9],[-10,5],[1,-1],[-7,7],[-6,10],[6,6],[-4,10],[3,2],[-9,9],[6,-9],[6,-5],[6,4],[9,-1],[9,9],[-4,1],[-10,9],[-6,3],[2,8],[-1,-10],[5,10],[-10,-2],[-8,-10],[-7,2],[-6,9],[7,5],[-3,7],[7,2],[1,-7],[2,-10],[8,5],[-3,-5],[5,-4],[-7,4],[-3,5],[-8,4],[-10,2],[10,-4],[-4,-6],[-5,-9],[-8,-7],[-1,6],[-3,5],[-1,-3],[-10,4],[-9,-8],[9,-1],[8,9],[2,-2],[8,-8],[-10,-4],[-2,1],[6,-1],[4,-9],[7,1],[1,-3],[5,-9],[-3,6],[1,-4],[9,-6],[1,-9],[9,1],[-9,3],[-10,4],[-2,-10],[9,10],[-8,-5],[-2,-1],[6,-9],[9,3],[10,-7],[-2,8],[3,9],[-6,3],[5,-10],[-7,-9],[2,-2],[-6,10],[-10,-10],[9,4],[-6,7],[2,-5],[-8,-4],[-7,-9],[-9,-9],[-3,4],[-7,4],[2,9],[3,-1],[5,-1],[-10,-7],[-8,-5],[7,-3],[-4,-4],[1,8],[-7,1],[-4,4],[8,-4],[4,7],[-8,-8],[-8,-5],[-2,-5],[10,6],[2,-9],[10,6],[3,-8],[1,-9],[-8,4],[-10,8],[2,4],[-7,-1],[-10,3],[-4,-9],[1,3],[5,-1],[-9,-10],[-7,-2],[2,-9],[8,7],[-10,7],[-1,2],[6,-6],[-7,3],[-3,8],[1,-7],[8,1],[-7,4],[-9,3],[7,-4],[1,3],[6,-8],[9,8],[-8,3],[2,1],[-4,-7],[6,-7],[-5,8],[-10,8],[5,4],[1,-3],[7,-6],[4,8],[-2,3],[7,5],[-10,10],[1,5],[-3,1],[-2,-5],[-2,10],[8,-4],[-5,2],[-6,5],[-7,-3],[2,-4],[8,1],[10,1],[-6,-10],[10,-7],[-10,8],[4,-1],[8,-1],[3,-5],[3,-2],[-3,6],[3,6],[-9,-10],[-1,-6],[-2,8],[-2,-10],[6,-9],[5,-1],[4,10],[3,-3],[-6,-3],[1,-4],[8,-5],[-10,-9],[-2,3],[-10,6],[2,-3],[1,-7],[-1,5],[-2,7],[8,-4],[6,-5],[2,8],[4,5],[-9,3],[6,-6],[-2,9],[8,6],[7,-6],[-5,-1],[-3,-8],[2,-5],[6,10],[9,9],[7,-7],[-5,4],[-5,4],[5,7],[-4,-5],[10,9],[7,8],[-7,5],[-4,-10],[-5,10],[7,10],[-9,10],[-1,2],[-2,-9],[-2,2],[3,-3],[2,-7],[-10,-7],[-1,10],[3,5],[-4,5],[-10,4],[-3,-9],[-6,5],[-8,4],[-1,6],[7,2],[-6,2],[-6,6],[3,-7],[-6,3],[9,-9],[2,4],[4,5],[-5,-9],[-4,1],[-2,-5],[4,-3],[8,-4],[6,5],[-7,-1],[-10,2],[3,-6],[-4,8],[-1,3],[7,-8],[2,6],[-5,7],[-4,5],[-5,9],[10,-7],[-2,2],[-2,-1],[-9,-7],[-8,10],[-6,7],[5,3],[-7,-10],[-8,3],[3,-5],[8,-5],[-2,-1],[-5,-6],[-10,-10],[3,7],[-6,8],[5,5],[-5,-3],[6,-4],[-10,3],[-6,6],[-1,10],[-10,5],[5,1],[5,8],[-8,-6],[10,-7],[3,-4],[8,-6],[4,3],[5,1],[3,10],[10,1],[8,4],[-7,8],[10,10],[2,7],[2,-2],[-9,-6],[5,-4],[3,-4],[-3,1],[-1,10],[1,-1],[4,8],[9,-2],[3,5],[-4,-2],[4,-10],[-6,7],[-1,9],[6,2],[-8,-7],[-2,-7],[9,-2],[9,-1],[-2,10],[-3,-3],[3,-6],[-2,9],[1,-6],[7,8],[5,8],[-6,7],[-10,-3],[-3,7],[10,4],[-2,-3],[3,7],[-5,3],[-5,-2],[-7,-10],[-7,10],[-1,7],[-2,5],[-8,-8],[8,-8],[-10,-2],[1,7],[-4,-7],[-10,-10],[-5,4],[10,1],[6,6],[5,-8],[4,-10],[-4,4],[-4,9],[-9,-6],[-8,2],[-10,5],[-6,-1],[-6,6],[10,6],[6,2],[-3,5],[1,-6],[2,8],[-5,-7],[3,-2],[8,10],[5,-2],[8,-1],[6,-10],[-9,-8],[4,-2],[-9,10],[10,3],[-9,6],[1,-4],[-3,-9],[-3,7],[-5,3]], dtype = "int32")#candidate|7271|(540, 2)|const|int32
const_7272 = relay.const([10,6,1,1,4,9,3,9,8,-4,-10,-5,-7,2,-2,4,2,-2,-6,9,5,9,7,-5,9,-9,6,-3,-4,2,-7,-10,8,2,-6,-3,10,-9,1,1,5,6,5,2,-6,7,-3,-2,10,-7,6,7,4,-2,-2,-3,-2,6,-10,-7,7,10,1,-2,-6,7,-9,-8,2,5,1,-1,-9,-8,-7,5,-9,5,7,-10,4,-4,2,5,-2,-10,-2,-5,7,-2,-10,-10,2,-8,-1,-3,-6,10,-1,-3,-7,5,3,-10,5,7,-9,-4,-2,-1,1,-10,10,-4,-4,1,2,-1,-8,-7,1,10,-3,-2,-7,10,4,2,1,-5,6,8,-4,5,10,-6,-8,-2,1,7,-6,3,-10,-5,4,8,6,8,-7,-3,-4,9,-7,2,6,3,10,-3,4,3,-6,10,9,3,10,4,-6,6,5,-1,-9,4,-2,-2,-2,6,6,-1,3,-2,1,7,-8,-1,10,5,-6,-1,-3,-7,-7,-3,1,7,-8,-9,4,6,-6,4,-9,-5,5,5,6,1,9,6,9,-5,4,-6,7,-8,-9,7,9,-4,8,2,-3,9,8,1,-1,-4,2,3,2,-2,-6,-8,3,-1,1,-4,8,-6,1,6,8,6,10,9,5,-10,10,-7,-1,-5,4,7,-5,10,2,7,-6,10,-4,-7,-8,-1,-6,-3,-7,-9,10,-10,-1,-8,-6,3,-7,9,9,2,4,8,-10,-9,1,-7,-6,-3,-9,9,5,-9,-4,6,4,-3,-1,-10,-5,-9,7,-7,-5,7,3,-1,-8,5,-9,-7,10,3,2,2,10,-6,-7,7,5,-6,-10,9,7,9,-6,1,8,-7,7,8,1,4,6,2,7,-2,-6,4,6,3,2,7,-10,-10,2,-6,-3,4,4,-3,-7,10,5,-1,1,-2,-8,3,-1,-6,-3,9,3,-7,3,-9,-2,-6,-7,7,-10,1,8,-7,8,-6,-6,-9,10,7,6,4,9,5,6,3,1,-6,-7,9,-8,10,-10,4,-5,-1,-1,10,-4,5,9,8,2,-10,-10,-6,-4,4,-5,3,-3,2,-1,3,9,7,-8,7,-2,-8,-6,1,-1,5,5,-6,4,2,2,3,7,-9,-7,-2,-3,-1,5,10,-9,1,-5,-4,-7,-6,-4,-2,1,6,6,-6,8,-8,1,8,5,6,6,-2,-6,4,9,3,-5,-7,8,-10,3,1,7,4,1,-3,9,2,4,-9,1,-3,2,-9,-5,9,6,2,3,7,-7,1,-4,3,-8,-2,-4,-5,-5,9,3,8,9,-5,7,4,-10,9,-7,-5,5,-4,-2,-7,3,-7,-1,-6,-4,-3,-2,-4,-2,-10,7,6,3,-3,6,2,-6,-6,5,-9,2,1,-9,-8,-7,-1,-4,-6,-6,-1,-9,-4,5,1,-1,-10,-2,-6,-3,-3,-3,-5,-1,3,10,-2,9,5,3,6,6,-6,5,9,-8,-10,-7,9,8,7,-8,-8,-4,-2,8,-10,2,-5,10,6,-6,-1,3,-3,2,8,9,-4,10,-10,4,5,8,2,5,7,6,6,-6,10,-7,7,-6,-8,6,7,10,5,-3,7,7,-1,2,4,-6,-7,7,-10,-4,1,8,2,-1,5,6,-4,-6,7,4,-7,10,-3,7,-9,-4,2,8,8,-1,-5,-5,-9,6,10,-9,-10,10,-5,-7,-7,-7,-10,3,6,3,2,-10,10,6,6,4,8,9,2,-10,-8,-9,1,10,-7,-7,-10,9,5,-7,-5,-8,8,4,5,8,10,6,1,-9,7,-7,-6,-7,4,-1,7,-9,9,5,-9,1,-2,3,1,4,-1,-4,-9,-6,-7,3,-10,-10,-8,-5,10,10,-1,7,-6,-1,-2,-2,8,-6,-8,-10,1,-7,5,-10,8,-6,3,-2,-4,6,9,-9,-9,-1,-5,-5,-1,7,-4,2,7,2,1,10,8,3,5,2,8,3,4,-2,-10,-2,8,-8,-2,-6,6,-10,2,-10,5,5,7,9,-5,10,-1,-2,6,5,-10,-3,-9,-1,-6,1,6,7,3,-9,-6,-6,1,8,-7,7,8,-6,-5,-9,1,-4,-4,-10,-6,7,-8,-3,-10,6,7,-7,-3,1,1,1,-8,8,-8,10,9,-10,-10,-4,3,8,-3,-5,7,6,-6,9,-2,9,-7,-5,-8,-3,-5,9,-9,10,-1,8,-2,5,9,-3,2,2,3,-8,-2,9,10,-7,-4,-10,-3,2,-3,5,-2,-7,-2,-8,6,-6,-8,6,-3,-8,-10,-2,9,10,3,-5,4,1,-1,-9,-6,-3,-9,4,-2,1,-3,6,-8,-3,10,8,-10,-9,10,7,-4,2,-1,-7,3,6,-4], dtype = "uint64")#candidate|7272|(896,)|const|uint64
const_7273 = relay.const([[1,8,-2,-10,2,3,10,4,-3,-3,7,4,-2,1,-6,-3,-10,-6,-3,7,8,5,-9,9,-8,-4,10,2,-6,6,-9,8,-10,-4,-3,-10,-10,-1,6,3,-4,10,3,-6,7,1,-10,7,-5,5,-3,-1,2,2,-5,3,-9,3,-6,-3,10,-9,4,10,-7,9,2,3,-3,-3]], dtype = "uint32")#candidate|7273|(1, 70)|const|uint32
call_7269 = relay.TupleGetItem(func_1580_call(relay.reshape(var_7270.astype('int32'), [1, 12, 15]), relay.reshape(const_7271.astype('int32'), [6, 12, 15]), relay.reshape(const_7272.astype('uint64'), [896,]), relay.reshape(const_7273.astype('uint32'), [7, 10]), ), 4)
call_7274 = relay.TupleGetItem(func_1586_call(relay.reshape(var_7270.astype('int32'), [1, 12, 15]), relay.reshape(const_7271.astype('int32'), [6, 12, 15]), relay.reshape(const_7272.astype('uint64'), [896,]), relay.reshape(const_7273.astype('uint32'), [7, 10]), ), 4)
output = relay.Tuple([call_7234,var_7249,const_7250,const_7251,bop_7265,call_7269,var_7270,const_7271,const_7272,const_7273,])
output2 = relay.Tuple([call_7235,var_7249,const_7250,const_7251,bop_7268,call_7274,var_7270,const_7271,const_7272,const_7273,])
func_7275 = relay.Function([var_7249,var_7264,var_7270,], output)
mod['func_7275'] = func_7275
mod = relay.transform.InferType()(mod)
mutated_mod['func_7275'] = func_7275
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7275_call = mutated_mod.get_global_var('func_7275')
var_7277 = relay.var("var_7277", dtype = "float64", shape = (1872,))#candidate|7277|(1872,)|var|float64
var_7278 = relay.var("var_7278", dtype = "float64", shape = (16, 9, 13))#candidate|7278|(16, 9, 13)|var|float64
var_7279 = relay.var("var_7279", dtype = "int32", shape = (3, 60))#candidate|7279|(3, 60)|var|int32
call_7276 = func_7275_call(var_7277,var_7278,var_7279,)
output = call_7276
func_7280 = relay.Function([var_7277,var_7278,var_7279,], output)
mutated_mod['func_7280'] = func_7280
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7075_call = mod.get_global_var('func_7075')
func_7076_call = mutated_mod.get_global_var('func_7076')
call_7338 = relay.TupleGetItem(func_7075_call(), 0)
call_7339 = relay.TupleGetItem(func_7076_call(), 0)
output = relay.Tuple([call_7338,])
output2 = relay.Tuple([call_7339,])
func_7342 = relay.Function([], output)
mod['func_7342'] = func_7342
mod = relay.transform.InferType()(mod)
mutated_mod['func_7342'] = func_7342
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7342_call = mutated_mod.get_global_var('func_7342')
call_7343 = func_7342_call()
output = call_7343
func_7344 = relay.Function([], output)
mutated_mod['func_7344'] = func_7344
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6336_call = mod.get_global_var('func_6336')
func_6338_call = mutated_mod.get_global_var('func_6338')
call_7348 = func_6336_call()
call_7349 = func_6336_call()
output = call_7348
output2 = call_7349
func_7350 = relay.Function([], output)
mod['func_7350'] = func_7350
mod = relay.transform.InferType()(mod)
mutated_mod['func_7350'] = func_7350
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7350_call = mutated_mod.get_global_var('func_7350')
call_7351 = func_7350_call()
output = call_7351
func_7352 = relay.Function([], output)
mutated_mod['func_7352'] = func_7352
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5955_call = mod.get_global_var('func_5955')
func_5957_call = mutated_mod.get_global_var('func_5957')
call_7353 = relay.TupleGetItem(func_5955_call(), 0)
call_7354 = relay.TupleGetItem(func_5957_call(), 0)
uop_7362 = relay.sigmoid(call_7353.astype('float32')) # shape=(9, 2, 6)
uop_7364 = relay.sigmoid(call_7354.astype('float32')) # shape=(9, 2, 6)
func_6430_call = mod.get_global_var('func_6430')
func_6433_call = mutated_mod.get_global_var('func_6433')
const_7371 = relay.const([-8,7,-1,4,3,8,-10,-9,6,8,2,-6,-6,9,-6,4,-7,-7,7,-4,5,4,2,4,5,7,1,-2,2,7,-4,-3,4,-3,-3,-3,8,6,1,7,-4,-3,2,6,-9,-1,3,-5,-3,-10,-3,9,-10,-1,-6,9,5,-7,-7,10,-5,10,4,-7,-2,-5,1,6,8,-6,-8,-6,-5,1,-7,10,9,-2,-5,-1,-9,4,2,-3,9,-5,-2,-1,4,-3,-10,-3,-4,3,-5,6,3,-3,-10,-5,8,4,-1,-9,7,-5,4,8,-4,-5,9,4,1,-7,8,10,4,-5,10,-1,3,-4,6,5,4,1,-3,-5,6,7,-8,7,-10,-8,-4,7,-2,6,-4,-8,-3,4,-7,10,3,-5,-4,-2,5,-7,6,10,-9,-8,9,3,-6,-8,6,-6,7,1,-6,-10,-2,1,2,-9,-8,-6,-4,9,-4,5,-4,10,-4,5,-3,-10,1,-4,-3,-6,2,7,10,8,-2,-5,-5,10,-3,9,1,2,9,6,1,-2,-5,10,5,-9,-10,5,-1,-5,1,2,-1,5,10,-3,-5,-5,6,-6,-3,7,-3,-9,7,-9,-7,-10,3,2,7,6,2,4,9,8,9,7,8,-6,-1,-3,4,-9,-9,2,-8,-9,2,-8,-5,2,4,6,5,-8,7,-7,5,9,8,-1,2,7,-7,-4,3,-6,7,-10,-6,-1,10,-1,3,-10,-1,-7,4,6,1,2,8,-3,-4,7,3,-10,-5,7,-2,1,9,6,-4,-3,-4,10,-6,5,8,-7,-10,-2,-9,5,8,-3,-5,-10,-3,3,9,1,6,5,-10,3,-1,-6,-5,-10,-8,10,3,-4,3,8,-1,-9,-5,-9,9,4,8,-10,3,-8,2,6,-7,6,6,-4,-2,-3,7,9,-5,-8,5,10,6,8,-5,7,-3,-2,6,-7,6,5,-4,-3,-9,4,7,-9,1,4,10,-5,-4,-5,10,-9,1,-4,-8,4,8,-1,-1,1,-8,5,6,-2,-7,-1,8,-7,-5,4,10,1,5,6,-2,7,1,7,-3,8,-7,-9,10,-4,1,-8,-5,10,3,-5,2,-5,3,10,5,6,-6,7,-2,-3,-8,-5,-2,-2,-8,9,6,-3,-10,-2,1,-8,-2,-5,5,-9,-8,7,-9,4,5,-9,1,-1,3,7,1,2,-8,2,-4,-10,5,-2,-8,4,-2,-4,3,6,-9,1,-6,-7,-10,2,10,-6,-9,1,-5,-9,-8,-3,-10,-10,-10,1,5,-2,9,-9,-6,-5,-3,10,-3,-6,6,3,-6,7,5,-6,7,5,4,4,9,2,-8,-10,3,-6,-5,5,4,-1,-9,1,-7,-2,2,-8,5,-5,-4,8,2,6,-2,3,2,-5,1,9,-2,-6,4,7,5,4,6,-5,-5,6,-4,1,2,-9,4,2,8,10,3,-3,9,6,-1,-4,3,-2,-10,5,3,-7,-3,-2,-7,4,2,-8,7,4,4,2,9,-6,-9,1,6,-8,6,-9,4,5,-1,5,-5,-5,9,8,-3,7,7,3,-7,-10,1,-8,-5,9,3,5,6,-1,-7,-3,3,-2,9,4,6,-8,5,4,-8,7,8,1,10,-9,1,7,3,6,7,-7,-6,-2,3,-3,10,4,10,3,7,8,5,6,7,1,2,8,5,8,-7,-8,-1,-6,8,-2,1,-7,-9,6,4,1,5,5,9,-7,6,-3,8,9,-9,4,-3,8,-3,8,-2,-7,-6,7,8,2,-9,-3,2,-6,-3,3,-1,-7,-5,-4,-4,6,-3,-7,-6,7,4,6,-1,9,1,9,-4,6,1,-8,1,9,6,-5,5,-10,1,6,-8,-6,-8,-3,-1,-2,1,9,4,3,4,-4,9,1,-10,4,4,9,4,4,2,-8,-6,4,7,-9,5,-3,7,-6,10,7,9,6,1,-1,-4,6,7,1,7,-6,-3,-9,-2,-9,7,6,5,1,10,9,-10,5,6,3,5,-6,-10,-3,1,5,-10,-8,-1,-1,1,-8,-4,10,8,-1,-5,-5,5,-5,10,6,1,4,-3,4,4,6,-4,6,-4,-8,8,-3,-1,-9,10,-2,-9,4,1,7,9,-3,-2,8,-8,4,-2,-6,5,6,3,6,-4,6,-8,1,8,4,-3,-7,-1,-6,8,-5,-9,8,-9,-6,5,-8,-6,-2,-3,6,9,6,6,2,-3,-9,-10,-4,3,9,3,3,-6,-4,3,6,5,3,-5,-7,4,3,-5,2,-9,8,-8,-1,-7,-5,7,2,7,-7,-2,3,2,-1,-4,-5,-4,5,5,6,3,2,-7,5,-4,6,-9,-4,-6,-6,-8,3,5,3,6,-1,5,10,-2,5,9,1,-2,-7,-10,9,5,1,2,1,7,6,7,-3,-2,4,2,7,8,4,-8,-7,5,-4,-4,-4,9,5,7,-5,-8,2,4,-6,5,2,3,8,-1,-4,9,8,-9,4,-2,-6,-9,2,10,-8,10,-2,-3,-10,3,9,-3,10,1,7,-2,-4,5,-6,6,2,6,-8,4,-1,-3,9,-7,-5,2,2,8,6,-3,-8,8,6,4,1,1,5,2,9,4,8,7,1,-7,9,-1,9,-7,-1,7,6,-4,4,-6,7,-7,5,6,-9,3,1,3,3,-4,-10,6,1,-9,-8,-7,5,10,6,-6,-9,3,4,9,-7,-4,6,-2,-2,1,6,-4,2,2,2,-4,-10,-8,-6,-4,9,-9,5,-1,2,6,-2,2,-4,3,-2,-4,6,7,-10,3,6,-4,3,10,1,-7,8,-8,-4,10,-8,8,-8,-3,7,-8,10,-8,9,-2,5,5,9,-6,2,10,-2,-5,-5,-9,-6,7,-2,1,-2,4,-4,-1,-10,-7,4,-4,6,-7,8,5,-6,2,-7,9,-7,9,2,6,10,6,-1,-10,-10,7,-6,3,-5,8,-9,-5,2,10,5,-5,9,9,-2,4,10,1,6,-6,9,4,4,6,5,-9,-2,-5,4,9,-7,-7,6,2,1,4,-5,10,10,-5,-2,5,-7,-4,-8,-8,-8,1,4,-6,1,-7,-8,6,-4,3,3,3,10,-4,10,1,-8,2,6,-7,9,5,-4,7,2,-6,-10,7,-6,-6,3,-6,4,3,7,-8,7,-6,-6,8,5,-5,5,-4,-2,-7,10,6,-3,-5,-10,-7,-8,-5,-7,2,-9,6,-8,-4,1,-7,-7,6,-3,-10,-3,9,1,-6,9,8,-7,-1,-5,7,-8,-6,9,-5,-10,-5,-2,-4,8,-1,8,-4,-4,-1,-10,4,5,3,1,-6,4], dtype = "int64")#candidate|7371|(1260,)|const|int64
call_7370 = func_6430_call(relay.reshape(const_7371.astype('int64'), [9, 140]))
call_7372 = func_6430_call(relay.reshape(const_7371.astype('int64'), [9, 140]))
func_6028_call = mod.get_global_var('func_6028')
func_6033_call = mutated_mod.get_global_var('func_6033')
var_7376 = relay.var("var_7376", dtype = "float64", shape = (224,))#candidate|7376|(224,)|var|float64
const_7377 = relay.const([8,-7,1,8,7,5,4,-4,-9,-10,-8,-8,-10,3,6,-7,1,-1,8,-4,-9,-4,9,3,4,-6,-2,7,9,-8,-5,1,-1,-10,-2,-3,-3,4,-4,8,2,2,-10,-8,2,-6,-10,-5,-9,-9,9,-4,8,4,4,-10,8,2,3,-9,-5,2,-9,-6,1,-1,-9,5,-10,-9,-3,-3,-3,10,-5,10,3,-3,6,3,5,2,-7,-1,-5,1,3,10,-9,1,9,-1,-3,7,6,-9,-3,4,7,7,8,-10,4,-7,10,6,-1,-6,-3,-6,-4,-9,5,5,9,-3,-1,-9,5,-7,-6,-8,10,-3,-6,4,-3,7,6,-9,-3,5,-7,9,10,9,-9,-7,1,-3,-9,7,10,10,-5,5,1,-3,2,-10,-10,-2,-4,-7,9,1,7,-9,-3,4,-8,-7,-7,-5,4,5,2,2,-4,-2,1,10,3,-4,8,4,7,5,2,4,5,2,5,-5,5,4,1,3,-5,10,-6,-1,6,4,-6,-5,-6,-10,5,1,-3,7,3,9,8,3,-4,5,-10,7,7,-7,-1,5,-2,-5,5,2,9,-6,-1,-8,-7,4,-2,-3,10,-4,-7,-6,-7,-6,10,-8,7,7,7,4,10,1,-6,-3,-4,-9,5,-8,6,-3,-1,-7,-9,8,-2,1,-8,-4,-7,-3,3,2,7,8,-3,10,-6,-2,-1,-2,-3,-5,-5,5,5,3,-8,-5,4,-8,8,2,-5,8,7,9,1,8,2,-10,-1,-6,-9,-6,8,-1,-4,-10,-9,4,-6,-3,4,5,-7,2,9,1,-1,-10,-2,5,3,-4,-2,6,1,7,3,1,6,-9,3,2,8,-5,10,-8,-5,-5,3,5,3,1,-3,-7,8,-5,-8,7,8,8,-1,-2,3,3,1,1,-9,1,5,-4,-5,-5,7,-1,-5,-2,-7,3,6,-7,-2,-2,-1,7,-10,-10,-10,-8,-9,2,9,-10,-10,8,9,-4,6,-3,8,2,1,-5,-10,-7,-5,5,-5,-10,-10,-3,-6,9,3,-8,4,-3,3,-7,4,-4,-5,10,-3,-8,-1,-1,8,-10,4,3,9,4,-5,-6,6,-5,8,4,-8,-6,3,-7,-9,-3,-6,-4,4,6,10,-8,2,1,9,-3,6,-7,9,10,-2,5,-1,2,7,-5,-1,-5,-6,-5,2,3,1,8,5,-10,-3,4,1,7,7,-7,5,-3,8,8,-10,-9,1,1,-5,3,-5,2,-5,6,-3,10,6,-10,3,-6,9,2,-3,5,3,8,5,3,-10,-3,3,4,-7,4,4,-3,-7,4,7,10,7,7,9,-5,-1,4,2,-3,-4,-10,-9,3,9,6,9,7,3,2,-6,-10,3,-2,2,5,4,-6,10,1,-9,5,-2,-5,-8,6,2,-2,-10,2,-2,9,2,-1,5,2,-10,1,3,6,1,-7,7,-9,-6,8,8,3,5,4,9,-5,7,10,3,1,-9,-8,10,3,6,3,1,4,2,-7,6,-10,7,10,8,-6,2,3,-9,5,10,-1,-3,-6,-5,-8,4,-3,-9,-10,6,6,-10,-7,7,-6,1,-7,-4,-1,-3,-9,8,7,7,-6,5,-1,3,6,2,-7,1,9,-5,4,1,7,7,1,-5,-7,1,7,-7,-3,7,4,-4,-3,5,-10,-3,10,-5,4,-9,10,10,-3,-10,-10,10,5,8,6,-7,4,5,10,6,-8,6,5,5,6,6,-6,-9,2,-1,3,-5,6,2,8,9,-2,-5,-2,5,-10,4,-9,7,2,-10,-3,-3,-2,4,-4,-7,-9,-3,5,-1,-3,8,-9,3,-10,8,7,2,-8,-1,-1,-1,3,1,2,-10,8,6,5,-1,-4,10,-2,-1,1,5,2,-10,9,-10,5,7,10,-3,5,-9,4,-2,-2,-9,7,-4,-9,4,8,-1,6,10,-1,10,-6,-7,-10,7,2,-6,-1,9,-5,-9,9,-5,8,-2,8,-9,4,-7,4,6,-1,6,1,1,10,-8,-10,3,-10,-8,-8,-5,4,-5,-7,6,-3,9,10,1,-1,-7,2,10,-5,-10,-7,5,6,-10,1,2,-8,10,-2,8,-10,4,-6,-3,5,6,-8,-3,-1,7,9,-7,-10,-7,-10,6,1,-1,6,-8,7,3,4,-10,-9,6,8,-6,-10,3,-7,9,2,-7,-6,-9,8,8,10,-7,-7,-6,4,-5,5,6,8,-4,-7,-9,5,-6,2,4,-6,-2,4,9,-1,4,-4,-10,8,-3,4,-10,9,-1,-3,-4,8,1,-3,-9,7,-10,6,5,7,-2,9,-9,9,-3,7,-1,-3,-6,-5,1,-2,4,5,3,7,-3,7,-7,4], dtype = "uint64")#candidate|7377|(896,)|const|uint64
const_7378 = relay.const([[False,False,True,True,True,False,True,False,False,True,False,True],[True,False,True,True,True,False,True,True,False,False,True,False],[False,False,True,True,False,False,True,True,False,False,False,True],[False,False,False,False,True,False,False,False,False,True,True,True],[True,True,False,True,True,False,False,False,False,True,True,True],[False,False,False,False,True,False,False,True,False,False,False,False],[False,False,False,False,True,False,False,True,True,False,False,False],[False,False,False,True,False,True,False,False,False,False,False,True],[False,False,False,True,False,False,True,False,False,True,True,False],[True,True,True,False,True,True,True,False,False,True,True,False],[True,True,False,True,True,False,False,True,True,False,False,True],[True,True,False,True,True,True,True,False,False,False,True,True],[False,False,True,False,True,False,False,False,True,False,True,False],[False,True,False,True,False,False,True,True,False,True,False,True],[False,False,True,False,False,False,True,False,False,True,False,False],[True,False,False,True,False,False,True,True,True,True,False,True],[False,True,False,False,False,True,True,False,True,False,False,True],[True,False,False,True,True,False,True,False,True,False,True,True],[False,True,False,True,False,True,True,False,False,True,False,True],[False,True,True,True,False,False,True,True,False,True,False,True],[True,False,True,False,False,True,False,False,False,False,True,False],[True,False,True,False,False,True,True,False,True,False,False,True],[False,True,False,False,False,False,True,True,False,True,False,False],[False,False,False,False,False,False,False,False,False,True,False,False],[True,True,True,False,True,True,True,False,False,True,False,False],[True,False,True,False,True,True,False,True,True,True,True,False],[True,True,False,True,True,False,False,False,True,True,False,False],[False,True,False,False,False,True,False,True,True,True,True,False],[True,False,True,False,True,False,False,False,True,False,True,False],[False,True,False,True,False,False,False,False,True,False,False,True],[True,False,True,False,False,False,False,True,False,True,True,True],[True,False,True,True,False,True,True,True,False,False,False,True],[False,False,True,False,True,False,True,False,False,False,True,False],[True,True,True,True,True,True,True,False,True,False,True,True],[True,True,False,False,True,True,True,True,True,False,True,False],[False,True,True,True,True,False,True,False,True,True,False,False],[False,True,True,True,True,False,False,True,True,True,True,False],[False,False,False,True,False,True,False,True,False,True,False,False],[True,True,False,False,False,False,True,False,True,False,True,True],[False,False,False,False,True,True,False,True,True,False,False,True]], dtype = "bool")#candidate|7378|(40, 12)|const|bool
call_7375 = relay.TupleGetItem(func_6028_call(relay.reshape(var_7376.astype('float64'), [224,]), relay.reshape(const_7377.astype('uint64'), [896,]), relay.reshape(const_7378.astype('bool'), [480,]), ), 5)
call_7379 = relay.TupleGetItem(func_6033_call(relay.reshape(var_7376.astype('float64'), [224,]), relay.reshape(const_7377.astype('uint64'), [896,]), relay.reshape(const_7378.astype('bool'), [480,]), ), 5)
const_7396 = relay.const([[True,True,False,False,True,True,False,True,True,False,True,False],[False,True,True,True,False,True,False,False,True,True,True,True],[True,False,False,True,True,True,True,False,False,True,True,True],[False,True,True,True,False,False,True,False,False,False,True,False],[False,True,False,True,False,True,True,False,False,True,True,True],[False,False,False,False,True,True,False,False,False,True,True,False],[True,True,False,True,True,True,True,True,True,True,True,True],[True,False,True,True,True,False,False,False,False,False,False,False],[True,False,False,False,True,True,False,True,False,True,False,False],[False,False,True,True,True,False,True,False,False,False,True,False],[True,False,False,True,False,False,True,False,True,True,False,False],[True,False,True,True,True,False,True,False,False,True,True,True],[True,False,False,False,True,True,False,False,True,False,True,False],[False,True,False,True,False,False,False,True,False,True,True,False],[True,False,False,True,True,True,True,True,False,True,True,True],[False,True,True,False,True,False,False,True,True,False,True,False],[False,True,True,False,False,False,False,False,True,False,True,False],[False,False,True,False,True,False,True,False,True,False,False,False],[False,False,False,False,False,True,False,False,False,True,False,False],[False,True,False,True,True,False,True,True,False,True,True,False],[True,False,False,True,False,False,True,True,False,True,True,False],[False,True,False,False,False,False,True,False,True,True,True,True],[True,True,False,False,False,False,False,True,False,False,False,True],[False,False,False,False,True,True,False,False,False,False,False,False],[False,True,True,False,True,False,True,False,True,True,False,True],[True,False,True,False,False,True,True,False,True,True,False,True],[False,False,True,False,False,True,False,True,True,True,True,False],[False,False,False,True,True,True,True,True,True,False,True,False],[True,False,False,True,True,True,False,True,True,True,True,False],[False,True,True,True,True,False,True,True,False,False,False,True],[True,True,False,False,True,True,False,True,True,True,False,False],[False,False,True,True,True,False,True,True,False,False,True,True],[False,False,False,False,False,False,False,True,False,False,False,True],[False,False,False,True,True,False,False,True,False,True,True,True],[False,False,True,False,True,False,True,True,False,True,False,True],[True,False,False,True,False,False,True,False,True,True,False,False],[False,False,False,False,True,True,False,True,True,True,True,False],[True,False,False,True,True,False,False,True,False,True,False,False],[True,True,True,False,True,True,True,True,True,True,True,False],[False,True,False,True,False,True,False,True,False,False,True,True]], dtype = "bool")#candidate|7396|(40, 12)|const|bool
bop_7397 = relay.maximum(const_7378.astype('float32'), relay.reshape(const_7396.astype('float32'), relay.shape_of(const_7378))) # shape=(40, 12)
func_2703_call = mod.get_global_var('func_2703')
func_2706_call = mutated_mod.get_global_var('func_2706')
call_7402 = func_2703_call(relay.reshape(call_7375.astype('bool'), [8, 4, 15]), relay.reshape(const_7378.astype('bool'), [8, 4, 15]), )
call_7403 = func_2703_call(relay.reshape(call_7375.astype('bool'), [8, 4, 15]), relay.reshape(const_7378.astype('bool'), [8, 4, 15]), )
func_2104_call = mod.get_global_var('func_2104')
func_2106_call = mutated_mod.get_global_var('func_2106')
const_7416 = relay.const([-5.417377,-8.805915,3.725454,9.763634,8.589509,1.227535,0.427735,-3.603304,-0.278178,-4.304328,5.400960,-1.399651,1.049081,-5.249211,1.100202,4.046187,8.190422,-8.291323,8.433366,0.320785,8.303697,-5.525560,-9.203820,-0.726556,-5.880290,-2.185620,1.837317,-8.820346,-7.382369,1.577250,-2.434396,9.392858,-2.880856,-0.090244,2.451878,0.716627,-9.896603,-4.876252,-9.360623,1.982660,2.925850,4.655104,-8.051761,-3.807552,-3.724669,9.832714,-1.585940,4.553919,-0.120634,7.261779,5.168558,-5.460352,-7.567997,9.414058,9.733073,4.292714,-5.615770,9.892217,-7.173675,4.134473,-2.940584,8.542546,-8.208887,3.289812,-2.529033,-5.842367,9.617508,1.834844,6.178376,2.623754,8.522121,-2.316203,8.084756,5.211327,6.476228,-8.329942,3.357376,-6.193762,-6.174089,-5.343575,-6.373133,1.042188,-1.080117,6.460960,4.212656,-9.482551,-1.078404,-9.239626,2.452594,5.779955,1.040080,-7.599803,-5.358306,-2.565273,-8.533598,5.067050,4.381903,2.566761,-2.150625,-2.048530,7.464086,-7.973104,8.255587,0.825721,-9.137702,5.686071,-9.170939,-9.657424,-6.113035,-3.552161,-3.719372,-5.012196,-3.492130,7.291089,-2.967356,-1.444151,-0.851729,9.121942,4.856203,-9.920162,-4.928309,1.574959,2.213266,4.735394,-8.840496,6.464043,3.783999,7.067924,5.412944,-8.955106,-2.699080,0.539809,-0.886085,-8.175149,5.487926,1.269539,-8.818007,-4.223193,8.832484,2.617954,2.028190,-1.513014,-6.622060,-1.934946,-3.937949,-8.905334,4.213001,5.755195,-8.289391,-5.433490,3.042492,5.733143,-7.540979,7.695331,4.975891,-2.315948,5.473457,-1.240046,-6.281915,0.526415,2.985740,8.210302,0.828063,-0.601705,-7.939864,4.890806,7.638005,0.574559,7.226540,5.332729,6.382177,5.522952,-0.873022,0.966974,3.349605,1.701183,-6.201871,7.743679,2.557435,2.506421,-1.801383,9.092564,-9.003870,-0.090775,-9.788210,-0.673027,1.093097,-0.857521,5.484020,-8.793182,8.295067,-3.360364,-8.951652,3.042911,1.220421,7.521839,-9.303244,9.055085,3.372848,-9.612357,5.961562,4.801536,-0.934762,-7.811346,6.902899,-6.914239,-8.384239,-7.994132,6.183068,4.710514,6.933310,-8.229736,2.128670,-5.773733,4.555828,-0.276461,6.207274,4.239347,-8.853264,-8.525143,-3.357524,-0.480540,1.322465,6.313829,-5.789025,5.883654,8.722034,7.740039,-7.156143,8.928419,-8.886564,-6.362152,-6.918208,-3.921577,-5.564440,-2.200088,9.105380,3.777865,-9.885693,5.655453,6.731853,-4.875964,7.072761,-1.564441,7.992352,7.409606,2.780927,3.538414,-9.537620,-1.074142,-4.388397,7.639123,7.537146,-7.991661,-4.777015,9.036442,9.434213,-9.149853,4.450807,-7.584069,3.165032,2.504069,9.123034,-9.370432,-2.026079,-2.085328,2.915425,-0.558890,1.113067,-2.177321,7.455078,8.492666,8.451301,3.339134,-3.065569,2.992804,1.642046,0.800757,-2.296529,-7.535733,-9.241999,4.404936,4.242393,1.987725,2.461364,-8.282284,4.360061,3.225911,5.840034,3.327617,-4.928058,6.592996,2.195780,-5.957072,-2.203454,-0.189185,-8.336729,3.544865,-6.996816,-3.764425,-8.194058,-1.017593,-0.767151,5.341929,-4.039173,-9.669361,0.227608,-4.168016,-2.548119,-8.925585,-3.155848,8.847327,7.834999,-1.424614,4.668298,4.634764,5.143855,1.450643,2.661792,7.924027,-2.638408,-5.667180,-1.047501,-6.719017,8.516011,0.378710,-2.086835,-9.641042,2.459975,0.540522,1.448914,1.126417,-8.076919,4.587435,1.188658,5.185656,-8.828992,8.115467,-7.777102,6.580848,8.048984,9.963054,1.143386,5.572847,-6.179791,-8.806216,8.896122,-4.439540,-7.512459,1.978022,7.291394,9.198771,-9.045032,-7.962751,0.118775,-7.330319,-6.786158,-9.107069,-2.474708,1.574087,-0.655658,-5.426301,8.778036,1.345000,-5.366654,8.178659,9.667752,2.423099,5.173893,-7.168729,9.058269,6.884498,3.400345,-0.080057,6.995155,-3.802524,1.417872,7.392931,-4.044637,-8.873439,6.380540,-8.095222,3.537106,-5.265838,7.884127,9.372884,-2.193107,-4.916280,-9.702588,3.224579,-7.066357,6.083673,-7.061612,-3.444462,5.935274,-7.945933,-4.296305,4.141230,-8.989530,8.655706,-5.911294,5.161648,2.076923,-2.921737,-5.723759,-2.841697,-1.902379,-8.565390,-7.429376,4.721719,0.899977,4.457519,-1.009411,4.444944,-9.135516,-8.487291,7.044051,1.953373,6.848459,-0.477149,7.786819,0.396824,-7.557587,1.425935,-0.628192,-9.871124,-5.990505,-9.630546,-7.425091,3.844440,-7.257420,-6.105023,5.882114,-9.532223,2.864824,-4.739603,5.020673,-8.466379,0.335411,5.103886,-7.785675,-7.675498,6.308569,6.703996,-7.501321,-8.368946,-1.901821,7.900956,0.339920,0.619027,-7.350150,1.170571,9.098058,-9.652395,5.387346,-5.366647,1.349061,-7.917790,4.580474,5.621369,5.755511,-8.949587,-5.876551,3.618762,-2.503017,-8.823701,7.458914,-0.457973,-9.198743,0.324062,-5.600078,9.923811,-2.250613,-9.631682,-9.340756,-3.872757,-6.028514,6.876480,-3.898788,-1.992259,5.462472,6.842859,-5.904600,3.996270,-5.331527,5.273647,2.039476,5.693710,-7.707668,9.851304,4.179014,-7.566445,5.197476,-2.279375,2.310585,-6.112670,9.491447,4.998913,9.102584,-5.318147,1.875764,6.122395,5.725587,2.278050,-7.451337,-4.044250,-1.554610,4.442629,-2.983248,4.767540,-9.166293,9.892223,1.984441,-1.109846,9.530923,6.881157,-8.626130,2.827329,3.596062,3.458739,-3.633622,1.439724,1.017774,-2.893295,-6.281964,5.106988,9.659836,-4.297727,3.801762,8.925570,-3.308723,9.895237,7.704528,-5.011997,2.905851,2.699505,3.051335,-0.258585,4.680810,-9.836216,-2.599506,6.208335,-3.222379,7.397052,-3.854577,2.510489,7.030939,3.065008,0.690636,7.207020,5.559180,-4.078677,9.836755,0.600276,3.022800,-3.416269,5.702833,6.808870,4.978132,4.820494,-7.071384,-4.345491,-1.028572,-1.848371,2.075147,-6.644400,-7.216569,2.336069,-7.538935,0.573629,5.091987,9.283595,2.964841,-1.538934,3.132967,-6.069737,-0.053122,3.115407,-5.992598,6.729563,9.521171,-0.969964,-1.733210,4.463926,1.886365,3.360726,-3.197482,5.967691,5.465505,3.365316,-6.905530,-9.908418,-4.840152,1.836798,-1.461273,1.995560,-6.910602,9.039416,9.880257,9.763808,4.661482,1.464096,-5.489703,7.963515,7.497205,-7.326275,-2.355211,-8.200904,1.138156,0.053925,-3.837110,1.829073,0.423022,-6.078996,-6.673427,6.983249,-4.646601,7.332020,6.362031,-8.454665,2.909171,-1.568657,-7.249816,1.556907,-9.171946,9.190973,3.549948,-8.110075,5.159161,2.262292,-3.982013,-9.364068,-5.982069,1.346974,-7.759963,-5.790063,5.345809,-8.761952,9.242110,0.292836,-5.099336,7.618942,6.110552,-0.263366,-0.085723,-8.978043,-4.041410,5.186714,9.512063,1.751541,-0.751774,3.970436,-9.323486,9.445630,0.520331,-5.549233,1.566319,0.597751,5.458858,-4.610279,-9.965136,-9.543793,2.932657,5.615318,9.380813,-4.566371,-8.724295,6.871427,6.073319,-3.966513,2.445947,1.191965,-9.548118,1.564157,-9.228643,2.852424,3.320022,-6.857846,2.584105,1.343772,-4.749558,5.545764,4.723166,1.256792,4.419770,-2.584803,-8.753450,-2.489580,-2.034388,-6.750110,7.443424,8.203028,-0.371032,9.417484,3.101223,-1.621978,-8.056759,-3.762533,-4.400252,5.062727,-3.446324,-0.738659,3.083916,7.732998,-7.776267,-1.082213,-3.659798,-9.216523,3.693489,-3.866467,-8.834149,-0.996214,-7.530372,7.101919,5.313589,0.871332,-8.370515,-1.764175,-0.850336,4.779094,-1.321697,-1.824918,-0.116798,3.019732,-7.731478,-5.137823,-7.014879,6.256978,-5.247258,7.865808,7.967456,5.231306,-4.300307,5.454471,6.485944,0.394285,5.400176,-3.829810,0.518180,4.538030,-3.241051,-2.307946,0.311708,5.737737,-2.757415,6.943764,2.091230,4.069575,-8.780280,-7.521602,-0.180864,0.878570,9.403447,6.424408,9.634701,-2.803282,-7.619046,-4.335479,2.690651,6.770073,-7.064995,6.564377,5.286311,2.636470,-2.615081,-6.205676,-2.190294,-4.756357,8.464441,-3.936834,-4.929862,-3.042363,2.923572,-9.295190,0.752564,4.558692,-0.304538,3.335246,7.680154,-7.385132,8.901684,-5.639067,-2.358032,6.593243,-5.512877,2.743813,4.991964,-7.558554,-9.810208,8.543491,-5.608587,-5.069077,3.537527,3.941731,-9.074956,-1.472318,-0.152530,2.618446,1.255284,-4.101823,-1.421586,6.202473,-7.838377,1.158930,-7.190639,-6.846490,5.165585,-7.352716,-1.663331,2.245908,2.115882,-6.328179,5.313364,-3.125040,3.783800,-9.249638,-7.631893,1.823067,7.570066,-4.435720,1.529747,7.239320,0.463136,7.813725,9.713873,-7.756512,3.130374,-8.212759,7.428181,7.741863,2.660875,-5.257052,3.761770,-7.784160,-1.822734,9.531429,2.775474,-5.149318,-7.714695,4.459310,3.800987,-7.488189,-6.763624,8.505357,5.172697,-6.749126,-9.652303,5.187313,-1.401621,9.503724,-6.133632,-8.435129,7.010852,-2.753840,1.180976,5.341254,9.987652,8.909069,-4.570852,9.295595,8.529185,-6.896248,1.844265,-8.658792,-1.224807,-8.567389,-2.826805,-6.671880,-0.043145,6.106571,-6.016153,-9.791052,-8.124111,-1.185516,-1.068922,-8.137788,1.126946,0.600164,-0.774439,1.411513,0.259018,3.142521,-0.760986,0.255797,-5.402137,-6.588530,5.231964,5.081440,-6.364485,-5.584611,1.493612,6.438545,-0.162563,3.385136,-9.639838,1.772902,0.797941,5.271506,-9.980309,-2.897312,5.239869,-2.120765,8.709230,-5.820425,3.098289,-8.975088,0.628528,4.823721,-9.887863,5.903932,9.439596,4.250606,2.543242,6.107606,0.659569,6.711997,-1.357036,-6.083238,5.122494,-3.411788,6.472106,4.091888,-7.138873,-9.513121,-2.215820,2.685657,-6.695704,-8.392781,4.792660,-6.857817,0.193951,5.702373,9.247321,2.530509,-1.113594,3.252905,-7.133181,-9.603390,3.802733,8.240290,-5.780192,-6.710956,5.637731,0.733231,-8.647076,-0.044221,9.376847,6.240366,4.871596,1.800961,-1.523176,2.081963,9.797806,2.422503,1.852934,-9.089036,2.618983,-8.327648,0.118008,0.818063,1.027260,0.603917,5.632628,8.565984,8.952641,-1.385722,8.663499,-9.220040,-7.609132,-2.878987,7.683249,8.971688,8.563127,8.963784,1.310152,-5.015601,-9.818121,4.359030,-5.075523,-4.124540,4.832861,-3.585270,3.308086,-6.680504,-6.756153,5.342712,8.530705,2.919800,-0.033926,-0.328842,1.798932,9.070816,-2.004163,-9.820863,4.669098,9.087780,7.040781,-2.589164,-2.369998,-0.387177,3.337476,-8.539545,1.732831,4.619143,3.487347,2.920484,-1.137075,-1.022646], dtype = "float32")#candidate|7416|(1008,)|const|float32
call_7415 = relay.TupleGetItem(func_2104_call(relay.reshape(const_7416.astype('float32'), [7, 16, 9])), 0)
call_7417 = relay.TupleGetItem(func_2106_call(relay.reshape(const_7416.astype('float32'), [7, 16, 9])), 0)
output = relay.Tuple([uop_7362,call_7370,const_7371,call_7375,var_7376,const_7377,bop_7397,call_7402,call_7415,const_7416,])
output2 = relay.Tuple([uop_7364,call_7372,const_7371,call_7379,var_7376,const_7377,bop_7397,call_7403,call_7417,const_7416,])
func_7420 = relay.Function([var_7376,], output)
mod['func_7420'] = func_7420
mod = relay.transform.InferType()(mod)
var_7421 = relay.var("var_7421", dtype = "float64", shape = (224,))#candidate|7421|(224,)|var|float64
output = func_7420(var_7421)
func_7422 = relay.Function([var_7421], output)
mutated_mod['func_7422'] = func_7422
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6336_call = mod.get_global_var('func_6336')
func_6338_call = mutated_mod.get_global_var('func_6338')
call_7438 = func_6336_call()
call_7439 = func_6336_call()
output = call_7438
output2 = call_7439
func_7447 = relay.Function([], output)
mod['func_7447'] = func_7447
mod = relay.transform.InferType()(mod)
output = func_7447()
func_7448 = relay.Function([], output)
mutated_mod['func_7448'] = func_7448
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6227_call = mod.get_global_var('func_6227')
func_6228_call = mutated_mod.get_global_var('func_6228')
call_7458 = relay.TupleGetItem(func_6227_call(), 1)
call_7459 = relay.TupleGetItem(func_6228_call(), 1)
uop_7460 = relay.log10(call_7458.astype('float64')) # shape=(10, 14, 9)
uop_7462 = relay.log10(call_7459.astype('float64')) # shape=(10, 14, 9)
output = uop_7460
output2 = uop_7462
func_7467 = relay.Function([], output)
mod['func_7467'] = func_7467
mod = relay.transform.InferType()(mod)
mutated_mod['func_7467'] = func_7467
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7467_call = mutated_mod.get_global_var('func_7467')
call_7468 = func_7467_call()
output = call_7468
func_7469 = relay.Function([], output)
mutated_mod['func_7469'] = func_7469
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6909_call = mod.get_global_var('func_6909')
func_6910_call = mutated_mod.get_global_var('func_6910')
call_7476 = relay.TupleGetItem(func_6909_call(), 0)
call_7477 = relay.TupleGetItem(func_6910_call(), 0)
func_7056_call = mod.get_global_var('func_7056')
func_7061_call = mutated_mod.get_global_var('func_7061')
var_7484 = relay.var("var_7484", dtype = "float64", shape = (224,))#candidate|7484|(224,)|var|float64
var_7485 = relay.var("var_7485", dtype = "float32", shape = (672,))#candidate|7485|(672,)|var|float32
const_7486 = relay.const([-9,6,8,-4,-2,-5,-8,-1,8,8,-4,-7,-2,6,-3,3,6,8,7,-6,9,-10,-2,8,7,-8,-8,1,-9,8,-3,-6,2,5,-5,10,4,-1,-1,4,4,10,-6,3,-7,9,-2,1,8,5,4,-9,5,5,-8,3,-3,-3,-3,6,7,-10,-10,-5,4,4,-5,-8,-3,-6,4,-1,2,7,2,5,-9,-10,-5,-1,-7,9,-8,-4,-2,1,10,4,-10,7,-4,-3,7,-6,-10,-1,2,1,-9,-2,-5,-8,9,-7,2,-10,8,1,-9,-10,-4,8,-3,9,-3,-4,5,1,1,-2,-6,9,-6,-9,-9,-5,-10,-10,-1,-6,9,-1,9,8,-4,2,3,-1,-4,-7,1,-8,5,7,-9,2,-10,-4,-7,-10,-5,8,-6,8,-3,-2,6,-9,-10,-9,-7,8,-4,-8,-7,1,-1,-9,-1,-6,9,-1,10,6,-4,8,5,-1,-8,-1], dtype = "int32")#candidate|7486|(180,)|const|int32
call_7483 = relay.TupleGetItem(func_7056_call(relay.reshape(var_7484.astype('float64'), [112, 2]), relay.reshape(var_7485.astype('float32'), [56, 12]), relay.reshape(const_7486.astype('int32'), [180,]), ), 0)
call_7487 = relay.TupleGetItem(func_7061_call(relay.reshape(var_7484.astype('float64'), [112, 2]), relay.reshape(var_7485.astype('float32'), [56, 12]), relay.reshape(const_7486.astype('int32'), [180,]), ), 0)
var_7515 = relay.var("var_7515", dtype = "int32", shape = (180,))#candidate|7515|(180,)|var|int32
bop_7516 = relay.bitwise_xor(const_7486.astype('int16'), relay.reshape(var_7515.astype('int16'), relay.shape_of(const_7486))) # shape=(180,)
output = relay.Tuple([call_7476,call_7483,var_7484,var_7485,bop_7516,])
output2 = relay.Tuple([call_7477,call_7487,var_7484,var_7485,bop_7516,])
func_7521 = relay.Function([var_7484,var_7485,var_7515,], output)
mod['func_7521'] = func_7521
mod = relay.transform.InferType()(mod)
mutated_mod['func_7521'] = func_7521
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7521_call = mutated_mod.get_global_var('func_7521')
var_7523 = relay.var("var_7523", dtype = "float64", shape = (224,))#candidate|7523|(224,)|var|float64
var_7524 = relay.var("var_7524", dtype = "float32", shape = (672,))#candidate|7524|(672,)|var|float32
var_7525 = relay.var("var_7525", dtype = "int32", shape = (180,))#candidate|7525|(180,)|var|int32
call_7522 = func_7521_call(var_7523,var_7524,var_7525,)
output = call_7522
func_7526 = relay.Function([var_7523,var_7524,var_7525,], output)
mutated_mod['func_7526'] = func_7526
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6824_call = mod.get_global_var('func_6824')
func_6825_call = mutated_mod.get_global_var('func_6825')
call_7607 = func_6824_call()
call_7608 = func_6824_call()
output = relay.Tuple([call_7607,])
output2 = relay.Tuple([call_7608,])
func_7625 = relay.Function([], output)
mod['func_7625'] = func_7625
mod = relay.transform.InferType()(mod)
mutated_mod['func_7625'] = func_7625
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7625_call = mutated_mod.get_global_var('func_7625')
call_7626 = func_7625_call()
output = call_7626
func_7627 = relay.Function([], output)
mutated_mod['func_7627'] = func_7627
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7075_call = mod.get_global_var('func_7075')
func_7076_call = mutated_mod.get_global_var('func_7076')
call_7647 = relay.TupleGetItem(func_7075_call(), 0)
call_7648 = relay.TupleGetItem(func_7076_call(), 0)
func_1745_call = mod.get_global_var('func_1745')
func_1749_call = mutated_mod.get_global_var('func_1749')
var_7656 = relay.var("var_7656", dtype = "bool", shape = (1320,))#candidate|7656|(1320,)|var|bool
const_7657 = relay.const([-4,7,-10,9,-3,5,3,-3,9,-6,-9,4,4,3,-7,-1,5,-4,1,1,2,-7,7,10,8,-5,-6,4,7,1,-2,-7,-10,-1,6,6,-8,-5,-3,-1,2,9,4,-5,1,-5,10,-9,2,-3,2,6,-10,-4,-3,-5,-10,-2,-8,-5,5,-3,1,5,-3,-10,8,6,-7,3], dtype = "uint32")#candidate|7657|(70,)|const|uint32
call_7655 = relay.TupleGetItem(func_1745_call(relay.reshape(var_7656.astype('bool'), [8, 11, 15]), relay.reshape(const_7657.astype('uint32'), [70,]), ), 0)
call_7658 = relay.TupleGetItem(func_1749_call(relay.reshape(var_7656.astype('bool'), [8, 11, 15]), relay.reshape(const_7657.astype('uint32'), [70,]), ), 0)
func_7275_call = mod.get_global_var('func_7275')
func_7280_call = mutated_mod.get_global_var('func_7280')
var_7669 = relay.var("var_7669", dtype = "float64", shape = (1872,))#candidate|7669|(1872,)|var|float64
const_7670 = relay.const([[-9,-1,3,-10,5,-4],[-3,-8,-5,8,-9,-7],[-2,3,-10,4,10,-2],[-7,9,8,-10,4,-2],[1,7,6,10,9,-4],[10,10,-7,-4,5,-8],[-9,-6,4,-2,-9,8],[-4,-1,-2,4,7,2],[8,-8,-1,8,5,-3],[-1,6,5,-3,-4,4],[1,10,3,2,9,-6],[4,-2,-7,10,3,6],[-1,9,-5,-3,-2,-4],[6,8,-6,8,10,1],[-5,3,-6,-6,-10,-6],[7,-3,4,-5,5,-8],[10,3,3,7,-4,6],[3,-10,-8,-8,-10,5],[10,6,5,-6,-7,-7],[4,10,6,9,1,-4],[10,5,5,-3,2,-8],[-1,-6,-5,1,-8,-7],[-1,6,8,3,2,-5],[8,9,5,-10,4,-7],[6,-8,2,-1,-2,7],[4,7,5,-2,9,-6],[-1,-3,10,-5,9,-3],[9,-6,-10,10,-10,-10],[8,-2,3,1,4,-2],[5,3,1,7,-1,-2]], dtype = "int32")#candidate|7670|(30, 6)|const|int32
call_7668 = relay.TupleGetItem(func_7275_call(relay.reshape(var_7669.astype('float64'), [1872,]), relay.reshape(var_7669.astype('float64'), [16, 9, 13]), relay.reshape(const_7670.astype('int32'), [3, 60]), ), 6)
call_7671 = relay.TupleGetItem(func_7280_call(relay.reshape(var_7669.astype('float64'), [1872,]), relay.reshape(var_7669.astype('float64'), [16, 9, 13]), relay.reshape(const_7670.astype('int32'), [3, 60]), ), 6)
output = relay.Tuple([call_7647,call_7655,var_7656,const_7657,call_7668,var_7669,const_7670,])
output2 = relay.Tuple([call_7648,call_7658,var_7656,const_7657,call_7671,var_7669,const_7670,])
func_7675 = relay.Function([var_7656,var_7669,], output)
mod['func_7675'] = func_7675
mod = relay.transform.InferType()(mod)
mutated_mod['func_7675'] = func_7675
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7675_call = mutated_mod.get_global_var('func_7675')
var_7677 = relay.var("var_7677", dtype = "bool", shape = (1320,))#candidate|7677|(1320,)|var|bool
var_7678 = relay.var("var_7678", dtype = "float64", shape = (1872,))#candidate|7678|(1872,)|var|float64
call_7676 = func_7675_call(var_7677,var_7678,)
output = call_7676
func_7679 = relay.Function([var_7677,var_7678,], output)
mutated_mod['func_7679'] = func_7679
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7075_call = mod.get_global_var('func_7075')
func_7076_call = mutated_mod.get_global_var('func_7076')
call_7714 = relay.TupleGetItem(func_7075_call(), 0)
call_7715 = relay.TupleGetItem(func_7076_call(), 0)
func_6928_call = mod.get_global_var('func_6928')
func_6929_call = mutated_mod.get_global_var('func_6929')
call_7743 = func_6928_call()
call_7744 = func_6928_call()
uop_7749 = relay.asin(call_7743.astype('float64')) # shape=(9, 2, 6)
uop_7751 = relay.asin(call_7744.astype('float64')) # shape=(9, 2, 6)
bop_7763 = relay.floor_mod(call_7714.astype('float64'), relay.reshape(call_7743.astype('float64'), relay.shape_of(call_7714))) # shape=(9, 2, 6)
bop_7766 = relay.floor_mod(call_7715.astype('float64'), relay.reshape(call_7744.astype('float64'), relay.shape_of(call_7715))) # shape=(9, 2, 6)
func_6824_call = mod.get_global_var('func_6824')
func_6825_call = mutated_mod.get_global_var('func_6825')
call_7767 = func_6824_call()
call_7768 = func_6824_call()
output = relay.Tuple([uop_7749,bop_7763,call_7767,])
output2 = relay.Tuple([uop_7751,bop_7766,call_7768,])
func_7786 = relay.Function([], output)
mod['func_7786'] = func_7786
mod = relay.transform.InferType()(mod)
output = func_7786()
func_7787 = relay.Function([], output)
mutated_mod['func_7787'] = func_7787
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7342_call = mod.get_global_var('func_7342')
func_7344_call = mutated_mod.get_global_var('func_7344')
call_7812 = relay.TupleGetItem(func_7342_call(), 0)
call_7813 = relay.TupleGetItem(func_7344_call(), 0)
output = call_7812
output2 = call_7813
func_7817 = relay.Function([], output)
mod['func_7817'] = func_7817
mod = relay.transform.InferType()(mod)
mutated_mod['func_7817'] = func_7817
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7817_call = mutated_mod.get_global_var('func_7817')
call_7818 = func_7817_call()
output = call_7818
func_7819 = relay.Function([], output)
mutated_mod['func_7819'] = func_7819
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6227_call = mod.get_global_var('func_6227')
func_6228_call = mutated_mod.get_global_var('func_6228')
call_7822 = relay.TupleGetItem(func_6227_call(), 2)
call_7823 = relay.TupleGetItem(func_6228_call(), 2)
output = relay.Tuple([call_7822,])
output2 = relay.Tuple([call_7823,])
func_7829 = relay.Function([], output)
mod['func_7829'] = func_7829
mod = relay.transform.InferType()(mod)
mutated_mod['func_7829'] = func_7829
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7829_call = mutated_mod.get_global_var('func_7829')
call_7830 = func_7829_call()
output = call_7830
func_7831 = relay.Function([], output)
mutated_mod['func_7831'] = func_7831
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6134_call = mod.get_global_var('func_6134')
func_6135_call = mutated_mod.get_global_var('func_6135')
call_7832 = relay.TupleGetItem(func_6134_call(), 0)
call_7833 = relay.TupleGetItem(func_6135_call(), 0)
func_2128_call = mod.get_global_var('func_2128')
func_2130_call = mutated_mod.get_global_var('func_2130')
const_7835 = relay.const([[-5.043585,-8.018109,-3.991811,5.140746,7.649010,-5.116223,1.790028,7.484746,-7.196352,8.851569,-0.250880,-0.339226,-7.295543,6.817234,-0.215386,4.240326,-3.490243,1.905475,7.608009,6.404220,0.053842,2.595314,5.706240,1.339824,5.426961,7.932902,-0.547907,7.366346,1.545981,7.406517,-6.478907,-3.951391,6.486242,4.007902,-2.136085,2.351766,-1.934762,-0.393746,7.449112,3.618731,-0.568125,-7.851635,5.279262,-7.581746,3.694226,-0.729964,-6.240059,-8.740986,-3.777227,-8.981464,-7.045520,-5.700680,-1.844365,9.932276,-7.053648,-4.826424,0.997365,-6.670543,-8.394427,9.336804,-5.717754,1.673663,-1.967392,-5.652313,8.771024,3.666340,-6.118506,-5.489313,-1.327308,8.672490,-9.475677,8.172984,-6.304165,-2.275054,-8.833574,-5.618261,3.514196,2.565799,8.482687,7.675480,-9.618492,6.930977,-1.013438,8.329038,1.928680,-4.854253,-7.074294,3.365402,2.971934,5.945114,9.434310,-5.980855,7.927100,-6.388047,-4.285004,5.543715,-2.642845,6.746487,-0.572390,9.729034,8.421203,-9.480324,2.587225,1.120473,8.786565,1.175544,-1.831201,-3.080481,5.187078,9.221163,-3.760497,7.237410,3.804413,8.621983,7.451972,5.813077,-8.065154,0.499137,8.175159,-3.715011,5.990340,4.939257,-7.106433,-8.946734,-4.164772,2.220575],[-1.426629,1.369793,6.864340,-9.527269,7.064544,-0.815669,8.162909,8.937597,-6.047331,4.003881,0.455988,1.763940,-3.981127,-3.137611,7.947099,6.053874,-9.893582,7.033281,-0.418866,-6.614333,6.699841,9.609931,-9.772691,7.537882,0.321857,8.689840,5.659995,-9.477228,-5.701168,-7.960064,-0.203953,7.561430,-0.635976,-6.330935,-3.244921,-3.046260,1.970435,-2.883318,3.179105,-1.083536,7.659230,8.210684,3.933012,-1.137918,-7.205308,3.319402,8.965893,4.724547,-8.094522,-7.658084,3.074030,-5.178964,-6.075479,-2.900798,5.199370,-0.211030,-5.169317,3.624084,5.493664,1.615458,4.778758,-6.042822,-6.141980,-6.094095,-0.187854,8.952912,-2.450606,-3.346711,0.521433,-8.684489,-0.476856,0.023982,-4.624054,-5.634832,-4.934281,-3.383849,-4.003400,-3.826373,-7.717962,2.656789,4.931098,-3.302109,4.554858,7.414459,-9.558794,1.041698,-0.415716,1.411310,7.497924,4.824415,-5.713142,8.969087,-7.653807,0.458022,9.005028,3.788039,2.579178,-0.919926,9.429509,3.931864,5.328215,-7.196516,1.261431,-8.441200,7.054953,9.056692,7.921186,-4.409057,-9.473908,3.944943,5.050146,6.924604,-6.547222,1.709106,0.633870,5.095294,0.239574,-4.883761,-0.796616,4.300304,-2.344985,2.314212,-1.125872,-0.171218,6.220016,-2.778537],[-2.566016,2.826991,0.448754,-4.950915,-0.734494,7.184656,0.823231,-3.009256,-0.795949,7.937709,-8.326830,5.919543,7.558009,-2.714797,2.872894,1.376564,-2.822274,-8.567776,1.399951,-5.596124,0.658478,0.690147,2.727533,-8.306221,3.182406,0.474166,-3.195722,-7.805721,-3.905850,-7.184000,9.223809,8.728894,-1.164249,5.427872,0.143678,2.531899,2.878205,6.379156,1.467586,5.334205,-3.300140,-1.431933,8.642410,-1.601786,6.870801,7.945908,-9.867711,-0.859089,-9.303670,-5.192861,4.613400,-1.568040,-5.944420,-0.235443,0.648734,-1.213642,-4.995953,-5.914695,-8.102178,3.607661,9.874967,-4.758219,1.544524,0.721456,8.893766,4.178240,7.267094,9.320788,-0.625088,7.709660,8.986872,1.685449,8.257110,5.643006,-6.665182,3.804336,0.021453,4.038203,2.924924,8.713413,-6.411427,6.076731,-5.247725,8.954336,-2.379612,5.530378,-7.436796,0.836610,-6.550576,4.590481,4.680105,3.244443,3.740409,-2.585962,7.660816,6.069300,-9.004868,6.945537,7.152806,8.543016,-6.812405,-5.106336,8.508971,-3.695972,-4.448620,-5.200033,-9.025723,9.281495,-7.998299,-2.478402,9.615016,6.756555,6.768562,-2.526810,6.165942,-7.281187,-1.375763,8.462761,6.288505,-4.905100,6.264125,7.370061,-8.766085,6.740785,-3.280231,-5.097223],[1.928789,-1.162786,-6.521926,-8.451227,-1.761870,5.723273,4.633105,7.679409,-0.067396,-8.640934,-6.734060,-1.543207,-6.848499,-1.795095,3.164993,-7.165416,-2.560355,5.228004,-5.533672,3.061562,6.839482,1.588405,9.627535,1.720238,-8.410486,0.830612,4.632266,4.850298,-9.647033,0.353013,-7.655359,-2.795086,-2.619050,-9.667848,8.737483,1.985746,-5.735864,1.872486,7.666907,-0.191216,8.419955,5.541365,5.354459,-4.726905,-5.765128,0.714221,-6.582715,8.040795,-9.527266,9.835163,7.657712,-7.823174,8.905465,7.235896,-9.502937,5.565066,-7.563558,-7.519446,1.258457,3.293831,-9.010668,5.739764,-6.607393,4.045560,-5.911620,9.686495,-0.503608,6.248922,0.462615,-4.427729,-4.131528,8.911777,-3.376290,-7.423015,1.198666,9.350699,8.974504,-1.946838,-4.099829,-5.094831,-7.149281,-8.338286,8.741620,-1.003172,6.407302,-6.978446,-2.997230,-5.107679,3.026089,8.269455,-4.724943,1.002936,0.316188,9.028992,3.209464,-2.948209,6.399803,-7.368363,-9.329558,-5.050989,-1.984775,-4.145269,-1.701927,7.787353,1.527029,-5.136028,-4.275430,2.494777,5.180432,0.931811,-1.551178,-8.364839,-0.675399,-7.175227,-6.108535,-4.333094,0.224882,7.135480,7.653696,-1.443715,7.891571,-3.948351,-4.817163,6.481535,1.978247,-6.887066],[-4.934261,7.281374,-7.465049,-7.837286,-8.780803,5.083007,0.170372,-2.825418,2.471885,6.059361,3.116317,-7.599485,-0.160623,-5.607422,-1.187686,5.581611,5.301283,-9.285110,8.705829,-9.463384,8.431519,7.504340,3.090010,-0.333513,-6.933396,6.844771,3.242626,3.833792,-0.984578,5.150603,7.003396,3.453304,-0.518994,-1.941945,-9.759534,4.513034,-9.791113,-8.376197,-0.180689,-6.309429,2.822759,9.930502,-1.139310,-6.826762,-4.211165,8.694740,-2.537772,-9.443429,-7.632726,-5.598699,-2.725883,0.370920,9.485171,-2.292003,-1.779815,-8.003056,-2.203846,-2.204988,3.153296,6.846407,7.863937,1.506671,-1.300934,-4.808900,-1.064558,1.134309,-7.879054,3.046759,7.010236,-7.838644,-6.960685,6.664701,-4.677124,5.917114,-4.899033,3.108820,-1.695736,6.930143,-2.522408,9.915511,0.546298,7.747360,0.498276,0.379095,-6.587369,-1.068042,-3.750965,-8.934340,-7.394626,-9.982924,-2.080502,-8.651343,-1.146833,9.850954,6.772418,0.138729,-7.662028,-0.182133,9.068959,-5.250404,6.839775,4.318952,-9.322990,-6.833017,3.852482,9.272824,-0.230386,-9.009406,9.825252,-6.197900,5.391955,3.409129,-7.535942,1.935023,6.419069,-4.998114,3.012124,5.238575,2.984000,-1.398428,-3.873190,-0.941101,5.838924,-6.700954,0.556168,2.691365],[-3.980890,-8.507062,-2.145104,7.176345,2.897608,2.692240,4.114491,-1.472822,-7.364198,7.578372,-3.806162,-5.322133,8.945889,-5.725623,6.779499,2.664534,7.543999,-1.632448,5.558531,1.916620,2.326920,7.425884,6.161501,1.304142,-5.208417,9.738655,4.446345,-6.035442,-2.131000,2.138236,-6.576373,2.155048,-6.313580,-3.922972,7.831145,-3.538315,-7.700394,9.873839,2.826944,2.794047,-7.089835,-3.917180,-9.876174,-3.832637,8.180286,-4.747045,-0.504398,5.624696,-0.153951,-2.038907,-5.911090,-3.557051,2.699569,-0.094294,2.132516,-1.850088,-6.154516,5.323791,-0.307118,7.415652,1.083157,7.531796,-0.321000,-0.834422,-8.767066,-1.241038,2.068253,7.854848,2.323477,2.132878,-5.099556,-0.704559,-0.842965,1.297415,3.059087,-3.472979,0.068568,-1.481373,1.143499,-0.512304,8.616878,-6.251226,3.387311,4.632473,0.715645,8.168119,4.635967,4.615406,9.598696,-2.793839,2.203752,7.179925,-4.709681,-8.088554,-2.405085,-2.997833,-4.366853,-0.656429,-9.940274,-0.565879,-1.635189,6.344799,0.781868,4.827053,-6.482830,2.445109,3.280359,-0.108877,-5.549991,1.738630,9.536003,-7.617703,-7.860809,4.895747,1.153034,-8.722860,-4.624617,1.470425,-6.212441,-1.278393,-5.843918,7.362111,9.210059,6.490382,-2.563492,-6.564207],[-4.633093,7.372443,-8.840551,-9.453147,-6.447351,7.622493,-2.084084,-3.450723,-7.617075,2.382106,-3.085579,-3.116567,-1.017710,2.266449,-2.095275,-9.862039,9.478041,2.741398,2.110291,1.371193,-4.174386,-2.807255,7.320848,-7.934621,6.734575,-4.888060,-7.153536,5.976923,-3.301178,9.494510,0.223399,-6.798199,-6.137829,-0.492147,8.234839,4.592855,-6.307175,-9.235901,7.032641,4.276186,0.900575,-0.825214,-7.229023,-7.947499,6.586040,4.576848,-0.847051,0.091613,2.784763,-4.497083,5.947965,8.851763,0.008302,7.318303,-6.968815,7.781940,-5.175391,7.301965,-1.840080,6.685515,2.420166,-6.636026,-7.772923,-5.286878,9.504012,-2.063848,4.996822,-4.726971,-6.863231,2.526321,6.831015,-8.667168,-5.460232,-8.395598,1.995753,-8.208900,0.543904,-2.742803,-7.622093,1.815406,7.059072,-5.872659,9.016482,6.429363,-0.728284,-1.486357,-2.443788,3.983729,-6.236403,4.887931,-0.421798,8.878779,-6.776500,4.248826,-0.197982,-1.942018,2.523973,-4.189792,7.505730,-8.841161,-2.103081,7.113253,9.126316,-4.388718,8.991110,5.200346,9.947793,3.813282,5.004646,8.853351,3.599865,6.977101,-8.875765,-9.534090,-0.952318,-6.843940,0.594137,7.202715,-2.168049,8.503392,3.032405,9.926426,4.296940,-0.819744,-9.495428,-6.494706]], dtype = "float32")#candidate|7835|(7, 126)|const|float32
call_7834 = relay.TupleGetItem(func_2128_call(relay.reshape(const_7835.astype('float32'), [9, 7, 14])), 0)
call_7836 = relay.TupleGetItem(func_2130_call(relay.reshape(const_7835.astype('float32'), [9, 7, 14])), 0)
output = relay.Tuple([call_7832,call_7834,const_7835,])
output2 = relay.Tuple([call_7833,call_7836,const_7835,])
func_7837 = relay.Function([], output)
mod['func_7837'] = func_7837
mod = relay.transform.InferType()(mod)
output = func_7837()
func_7838 = relay.Function([], output)
mutated_mod['func_7838'] = func_7838
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6815_call = mod.get_global_var('func_6815')
func_6816_call = mutated_mod.get_global_var('func_6816')
call_7841 = relay.TupleGetItem(func_6815_call(), 2)
call_7842 = relay.TupleGetItem(func_6816_call(), 2)
func_2128_call = mod.get_global_var('func_2128')
func_2130_call = mutated_mod.get_global_var('func_2130')
const_7846 = relay.const([[0.178081,-3.974078,6.462453,9.822976,-8.272024,-6.934897,-6.827727,9.476848,-8.941348,3.636100,-9.354236,-8.065150,2.690122,2.938322,4.168686,4.007372,-4.874904,-8.007309,-3.899824,-4.335947,9.625494,-2.507002,-4.859015,3.772956,6.140862,-7.348833,5.676751,0.459164,-1.093358,-8.968753,7.245646,-1.108933,6.898524,7.157971,9.948208,-3.447783,-3.361679,-4.605594,0.605711,1.673756,7.019523,-1.863825,3.906559,0.790345,-8.774008,1.963912,-7.754482,-5.544785,7.152187,4.550923,4.304103,1.490771,-5.174728,6.685372,9.237791,9.457143,-8.842120,-3.243738,0.194652,6.418590,7.586718,-6.429788,5.383099,-9.513921,-8.186819,8.521816,3.236741,-4.688984,-7.749232,7.850133,-3.749921,-5.755064,8.384547,-6.773656,3.630649,-4.513029,6.068865,-2.707298,9.623261,6.209241,-7.918286,-1.810547,1.747709,3.277048,-5.685698,-7.461470,7.525817,0.936029,4.340703,-8.404318,5.429851,5.837276,9.464361,7.456715,-5.655109,-9.815351,2.474956,3.356750,7.663917,7.739480,8.667224,5.748786,-4.949908,7.428312,-3.827676,-9.695801,3.280987,-2.573581,5.267824,8.747742,-2.797551,-4.538163,-3.681205,3.505839,7.176797,5.652933,-2.255787,2.148035,6.013296,-7.314975,-5.038379,-2.782548,-7.091163,-8.799594,-9.412839,-5.244075,-9.057715,0.861293,-5.415973,-5.681446,9.828311,-4.953115,-5.149227,-0.003823,1.637793,-1.662176,-8.633759,4.369513,6.074653,-9.224621,8.853398,3.007517,-0.927846,2.404599,5.061773,-4.121665,7.348550,-2.730429,-1.476999,-2.341579,9.753644,-8.272195,7.919420,-3.935469,3.182118,-7.800929,0.060519,-1.668014,-3.294369,-1.408655,-3.073080,-6.244397,-4.438005,6.013827,-5.726039,-3.308171,-7.637215,3.462089,-0.389208,9.475487,-2.850050,-8.162265,6.958806,6.207992,-2.970491,1.455937,-2.449625,7.539889,-5.210631,-3.585410,-3.026141,-0.525561,0.686074,-8.021454,4.439554,3.301024,9.994496,-1.841267,1.066721,6.254781,3.026346,-8.974128,-9.594279,-3.547803,-5.074671,0.380094,0.895051,-3.469259,0.934676,-1.208023,-6.228802,3.336639,-8.202062,-2.024907,3.633176,8.541345,-8.518540,6.569106,6.111538,7.899511,-1.168007,-2.480946,-8.848399,-3.056647,2.737909,-9.884413,-4.111375,-7.043489,8.441419,-6.595425,-5.099464,-4.356976,5.999259,4.037573,2.223765,7.761895,-8.661224,-7.148639,-6.618627,-4.097917,9.667515,6.644257,-0.284241,-7.233756,-6.480575,9.996836,1.854575,3.979413,9.551961,3.116576,0.670441,-6.068989,9.555405,-4.840561,2.699101,4.576940,7.111202,-0.224429,-2.549106,-7.359866,-7.448273,9.347744,6.238691,-5.408015,-3.438366,6.801009,-9.992927,3.248855,-7.145036,7.547438,-8.822997,7.081234,8.663349,-7.094084,-6.825056,-3.459511,-9.443916,-9.191162,-3.848419,-5.536881,4.321656,-5.267497,3.985443,3.993378,8.020866,9.332703,8.328565,-7.668065,-0.362692,3.498371,8.712487,4.536206,5.506240,8.501843,4.003539,-5.042622,4.352533,-0.914543,-9.038562,2.919200,0.934073,-6.270591,2.739609,9.893048,0.523133,-6.516490,9.201880,-2.229044,-7.937953,-5.423880,8.259619,-9.203251,-2.252604,9.670755,-2.409624,-6.135115,3.655913,-7.277822,1.465288,-6.345833,-2.836831,2.226790,9.846441,8.976498,5.771550,6.674351,-4.279904,-6.207490,-2.202895,-1.580655,-9.187957,-7.541042,9.532473,-7.535220,6.926887,7.830547,7.361008,6.129676,-0.003431,-5.864831,-2.965418,-1.097191,9.225230,3.446692,-7.568756,-1.945692,3.246785,-7.864355,-4.863313,1.154216,2.036932,0.316251,-2.799864,8.585051,3.330520,-2.975447,4.346065,8.679905,0.508481,0.820906,-2.534902,-2.909058,-4.038716,-0.937070,0.568332,-8.113636,-1.456210,-4.348436,-5.380410,5.347509,3.842340,-4.860226,-2.124074,-1.973725,-0.575911,8.201399,1.878083,-6.002533,-8.128718,-0.605629,5.962356,-7.279472,5.253708,-3.462887,1.524752,3.096517,2.251713,3.430111,4.797291,-4.881892,9.820413,-2.701552,1.454089,0.173783,8.248834,-2.993338,-1.068984,-3.198820,4.768197,-5.281468,-1.076472,7.757040,8.508154,5.896117,-4.746526,-6.187333,8.121945,9.235877,-5.630296,-2.670461,-3.455568,-2.288514,-0.574310,-5.348765,4.636101,-0.867282,7.477139,4.974051,-7.077302,6.221576,-0.911682,3.051990,9.873365,3.517324,7.694786,1.549190,-5.785428,-1.714814,5.715737,-8.876768,8.913537,-5.659435,-4.167628,5.855707,9.284698,-7.842580,4.672393,6.301217,-0.985661,-2.696763,5.864765,7.913814,1.556183,-4.471392,6.195996,4.700954,8.007024,4.900739,1.669027,-7.128051,2.756694,4.221534,-7.284450,6.234301,3.273504,-9.831974,-5.852745,-9.659814,-4.262468,-7.641637,6.251434,-4.767991,5.911426,-1.674262,6.279055,7.233593,9.977165,5.704890,-5.248058,-7.933056,-7.411264,-3.683376,7.793304,-8.104031,6.886739,9.073967,-1.218330,7.360569,8.640304,-8.001993,-9.018654,3.380559,-5.895727,-0.582227,-5.197935,-4.474910,0.473559,2.544758,8.729476,-5.138182,-9.974867,3.036599,-5.430751,-0.782985,9.259519,-1.981794,5.359716,7.678793,-9.955003,-9.458064,5.347471,6.262307,7.813201,3.235763,-8.520328,8.662214,4.114486,5.720311,5.539440,9.001019,-5.441759,-1.407500,2.602324,-5.851065,4.023924,-8.818852,9.003317,-0.821545,-9.975244,-5.509226,5.900244,1.670900,-6.322367,-2.401126,1.575907,-6.840614,9.451690,0.407615,3.251523,-2.177999,-5.136553,3.006297,-2.783723,-6.724152,1.163895,6.910909,-2.450353,5.326112,5.056629,-5.451021,3.490588,5.418447,7.150781,6.159304,-5.172089,-6.578598,7.292695,-0.668884,4.514942,-5.803107,6.581817,1.233550,5.658325,9.634094,7.541384,1.823006,-5.420505,7.363257,3.363190,-7.849541,3.285951,-4.928892,-9.453992,-9.286044,0.958339,-0.560087,6.493266,-3.547551,-4.846908,7.452864,7.553235,-5.779908,7.191626,0.295410,0.749044,-0.294915,-4.839195,1.119705,-0.161380,-2.403964,-1.405610,-0.836321,1.763140,-8.834857,-0.406942,8.258475,-2.785601,-0.296386,5.382704,-3.495144,5.648809,7.954612,8.041479,2.847273,0.604010,3.765484,-3.646576,6.661889,-2.564954,-0.017951,3.618482,-9.978098,4.209318,-9.186862,2.019584,3.999381,6.500086,-0.764862,8.967364,-5.326512,-5.920609,3.082327,-9.188490,-4.534458,-0.479870,9.191409,-3.867464,-8.970847,-5.364447,-3.521531,3.431729,1.094482,4.670828,-2.302162,0.822767,6.117754,-1.242283,-4.819935,3.814706,-9.478981,6.446066,5.116588,8.457127,-2.509249,-1.828612,8.635067,-2.044176,4.003157,9.682098,9.940310,-2.149527,-7.252494,4.799225,6.011251,1.577098,-3.394175,-6.556546,-1.637194,1.891095,3.441316,2.757225,-9.610209,8.791073,9.104587,3.304553,9.911123,3.298967,-9.423256,0.491444,8.703808,0.437988,5.344768,-4.250914,-2.808064,-7.505206,1.400210,-0.799147,-5.219672,8.183518,-6.824463,-7.525996,3.665605,5.594344,-0.145912,6.343380,6.641507,6.701432,-7.294469,-2.109337,-2.844331,5.017768,3.542399,2.673502,6.538433,2.426203,8.988353,-3.437899,-6.566830,-4.405308,-6.876646,-4.025542,8.648780,-4.923702,6.225062,-0.543013,-6.234587,-2.040052,7.458903,6.336711,-5.067207,6.681788,-6.903807,-8.892846,1.105617,9.786796,0.144397,-4.032161,9.804396,-0.473940,2.388562,-4.315835,-2.115306,4.859813,-5.981322,3.332388,-7.353328,-9.896103,-1.831523,5.622701,-7.941991,2.323411,-1.879730,-7.466191,-3.367474,4.476298,0.670300,0.697195,-5.797799,6.910016,9.535041,3.764013,0.596044,-7.752202,0.559161,-0.046870,-3.039946,4.516983,8.059522,0.941955,-6.750929,2.222863,-7.269844,-2.903251,-0.252203,-1.099711,-3.364709,7.668981,5.206889,6.790097,2.919270,-4.962252,2.369924,-3.831173,7.402580,-4.703504,-8.329810,9.143827,2.063123,5.906781,-2.094170,7.649101,-2.594041,-5.776957,0.550699,-7.814923,1.390485,-9.437583,-0.446269,6.680540,-5.999017,4.825494,-4.424696,-0.854685,-5.047116,2.412634,5.498444,5.876666,9.604762,3.066197,4.842615,9.503417,9.347405,4.593108,-8.802207,0.452141,6.775502,-7.294161,-9.025064,0.384244,-9.711823,9.359277,1.624264,6.155223,-7.495674,4.268772,-7.416324,6.040360,5.539734,7.365079,2.469271,-2.260823,-6.452947,-7.260037,5.567053,3.217463,-5.246243,1.570014,-9.060819,-5.746164,-0.499434,-4.821483,-2.495629,-1.368731,8.329614,-2.507641,-5.642953,6.037398,4.884825,2.999482,9.374579,-1.904291,9.470443,4.109835,1.905361,3.826753,-2.498440,-4.826600,6.684080,-5.752299,3.252416,7.244447,3.500447,-7.946066,9.648017,-3.730851,-9.843979,-6.685228,-3.958273,8.262331,-0.608042,8.197411,4.425495,4.689901,-3.898265,1.246459,-1.929401,-4.059511,8.992465,-5.363320,-6.151215,6.881112,-8.480280,9.689112,6.584200,-0.165750,0.250903,-3.789013,9.381948,1.915714,5.843362,6.215528,1.442583,-4.759603,-7.024927,9.915607,6.792030,-9.958159,4.577759,-6.082556,-8.996316,-3.901851,0.943450,-7.553519,-2.436809,-2.700675,-2.386918,-4.652727,8.858727,-6.431553,8.871545,8.168840,-7.501579,-5.236327,5.832878,4.257816,0.920985,9.205689,-0.527200,-3.569065,6.656937,6.479930,-2.633397]], dtype = "float32")#candidate|7846|(1, 882)|const|float32
call_7845 = relay.TupleGetItem(func_2128_call(relay.reshape(const_7846.astype('float32'), [9, 7, 14])), 0)
call_7847 = relay.TupleGetItem(func_2130_call(relay.reshape(const_7846.astype('float32'), [9, 7, 14])), 0)
output = relay.Tuple([call_7841,call_7845,const_7846,])
output2 = relay.Tuple([call_7842,call_7847,const_7846,])
func_7848 = relay.Function([], output)
mod['func_7848'] = func_7848
mod = relay.transform.InferType()(mod)
output = func_7848()
func_7849 = relay.Function([], output)
mutated_mod['func_7849'] = func_7849
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7837_call = mod.get_global_var('func_7837')
func_7838_call = mutated_mod.get_global_var('func_7838')
call_7859 = relay.TupleGetItem(func_7837_call(), 1)
call_7860 = relay.TupleGetItem(func_7838_call(), 1)
uop_7870 = relay.sin(call_7859.astype('float64')) # shape=(9, 7, 14)
uop_7872 = relay.sin(call_7860.astype('float64')) # shape=(9, 7, 14)
func_6815_call = mod.get_global_var('func_6815')
func_6816_call = mutated_mod.get_global_var('func_6816')
call_7879 = relay.TupleGetItem(func_6815_call(), 1)
call_7880 = relay.TupleGetItem(func_6816_call(), 1)
output = relay.Tuple([uop_7870,call_7879,])
output2 = relay.Tuple([uop_7872,call_7880,])
func_7885 = relay.Function([], output)
mod['func_7885'] = func_7885
mod = relay.transform.InferType()(mod)
mutated_mod['func_7885'] = func_7885
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7885_call = mutated_mod.get_global_var('func_7885')
call_7886 = func_7885_call()
output = call_7886
func_7887 = relay.Function([], output)
mutated_mod['func_7887'] = func_7887
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6928_call = mod.get_global_var('func_6928')
func_6929_call = mutated_mod.get_global_var('func_6929')
call_7912 = func_6928_call()
call_7913 = func_6928_call()
output = call_7912
output2 = call_7913
func_7924 = relay.Function([], output)
mod['func_7924'] = func_7924
mod = relay.transform.InferType()(mod)
output = func_7924()
func_7925 = relay.Function([], output)
mutated_mod['func_7925'] = func_7925
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6824_call = mod.get_global_var('func_6824')
func_6825_call = mutated_mod.get_global_var('func_6825')
call_7950 = func_6824_call()
call_7951 = func_6824_call()
func_7121_call = mod.get_global_var('func_7121')
func_7122_call = mutated_mod.get_global_var('func_7122')
call_7954 = relay.TupleGetItem(func_7121_call(), 0)
call_7955 = relay.TupleGetItem(func_7122_call(), 0)
bop_7957 = relay.minimum(call_7954.astype('int16'), relay.reshape(call_7950.astype('int16'), relay.shape_of(call_7954))) # shape=(9, 2, 6)
bop_7960 = relay.minimum(call_7955.astype('int16'), relay.reshape(call_7951.astype('int16'), relay.shape_of(call_7955))) # shape=(9, 2, 6)
uop_7965 = relay.acos(call_7954.astype('float64')) # shape=(9, 2, 6)
uop_7967 = relay.acos(call_7955.astype('float64')) # shape=(9, 2, 6)
bop_7991 = relay.mod(uop_7965.astype('float64'), relay.reshape(call_7954.astype('float64'), relay.shape_of(uop_7965))) # shape=(9, 2, 6)
bop_7994 = relay.mod(uop_7967.astype('float64'), relay.reshape(call_7955.astype('float64'), relay.shape_of(uop_7967))) # shape=(9, 2, 6)
bop_8013 = relay.left_shift(uop_7965.astype('int64'), relay.reshape(call_7954.astype('int64'), relay.shape_of(uop_7965))) # shape=(9, 2, 6)
bop_8016 = relay.left_shift(uop_7967.astype('int64'), relay.reshape(call_7955.astype('int64'), relay.shape_of(uop_7967))) # shape=(9, 2, 6)
output = relay.Tuple([bop_7957,bop_7991,bop_8013,])
output2 = relay.Tuple([bop_7960,bop_7994,bop_8016,])
func_8026 = relay.Function([], output)
mod['func_8026'] = func_8026
mod = relay.transform.InferType()(mod)
mutated_mod['func_8026'] = func_8026
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8026_call = mutated_mod.get_global_var('func_8026')
call_8027 = func_8026_call()
output = call_8027
func_8028 = relay.Function([], output)
mutated_mod['func_8028'] = func_8028
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7786_call = mod.get_global_var('func_7786')
func_7787_call = mutated_mod.get_global_var('func_7787')
call_8042 = relay.TupleGetItem(func_7786_call(), 2)
call_8043 = relay.TupleGetItem(func_7787_call(), 2)
output = relay.Tuple([call_8042,])
output2 = relay.Tuple([call_8043,])
func_8046 = relay.Function([], output)
mod['func_8046'] = func_8046
mod = relay.transform.InferType()(mod)
mutated_mod['func_8046'] = func_8046
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8046_call = mutated_mod.get_global_var('func_8046')
call_8047 = func_8046_call()
output = call_8047
func_8048 = relay.Function([], output)
mutated_mod['func_8048'] = func_8048
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7121_call = mod.get_global_var('func_7121')
func_7122_call = mutated_mod.get_global_var('func_7122')
call_8052 = relay.TupleGetItem(func_7121_call(), 0)
call_8053 = relay.TupleGetItem(func_7122_call(), 0)
func_7056_call = mod.get_global_var('func_7056')
func_7061_call = mutated_mod.get_global_var('func_7061')
const_8062 = relay.const([-8.979803,6.935686,8.502981,0.601401,4.561358,6.118994,9.517077,9.867544,8.511145,-9.589206,-7.502041,-5.290195,2.650494,8.012439,7.235372,0.517090,-8.613816,-1.849840,-0.352480,4.433214,-9.248996,3.306642,1.877676,-2.761396,8.507092,-2.802024,-2.642409,-1.567403,-3.490126,-8.837275,3.181574,3.283072,4.734303,8.465840,0.254759,6.438888,4.762854,-2.109261,-0.327034,-7.448845,9.209963,2.911913,9.384886,5.960040,8.939359,0.273552,9.559357,-5.372243,-2.334155,3.953405,-6.867996,9.323819,1.987062,-1.390309,1.297731,-1.390951,2.324864,-7.040983,9.442298,-2.000562,3.517850,3.054888,-3.557072,8.985854,4.191504,-6.069345,-6.046373,-1.919665,0.637321,1.400612,9.848362,0.925366,5.414850,1.105207,8.895449,6.097769,8.796810,-4.291851,-6.810679,-1.211719,-3.575054,7.069202,-9.290020,-1.832176,-1.546571,-7.706297,0.796146,-1.941218,9.295426,-0.215412,6.462410,-6.470562,-2.854293,-4.873311,-6.304101,2.127099,8.860371,3.011769,-0.054650,-2.076926,4.443931,-4.772283,-9.545180,7.283084,-8.927709,4.214197,5.912188,-5.053515,-0.892182,-8.672812,8.095298,8.080417,-3.848439,-2.514184,-1.795305,3.208267,-3.869358,7.817431,-1.810524,-3.349477,-2.508227,-0.291820,5.469069,8.503920,4.192084,5.924416,2.536922,-8.049215,5.149023,-8.290230,0.791192,-7.190213,0.522794,-1.190466,-2.903865,-5.778287,-6.451635,8.947924,3.024459,8.777518,-6.202585,7.380016,7.362314,-9.272265,7.260595,9.613333,-7.211414,-2.627825,8.597057,-1.647057,0.162668,-4.806183,1.805626,-9.289695,-4.451933,-7.916791,-6.910459,1.843068,9.502503,-0.464024,-2.239160,1.443067,0.313687,9.424550,-9.962415,5.006845,-2.823825,-1.084235,9.788644,2.579414,-7.135740,-4.791575,6.460047,8.263792,3.506587,3.197188,9.091726,5.053685,-9.212626,1.730244,-9.934589,0.561889,-4.582559,-6.210119,-9.993362,2.847130,7.028476,9.669054,8.739892,8.169355,-9.211134,6.494072,7.365527,7.940492,8.955514,8.656624,6.722384,-7.765027,-8.706188,0.889357,-9.628550,4.170302,-4.920501,1.935411,3.523293,3.290346,6.892787,7.492776,4.895018,8.880077,4.792986,-5.214078,9.106466,-0.593050,3.008831,-0.656742,8.213975,-4.482217,-6.846977,5.346654,-0.663774,7.269522,5.191747,8.125809], dtype = "float64")#candidate|8062|(224,)|const|float64
const_8063 = relay.const([2.524387,2.577580,1.455295,-6.740913,5.240007,-8.190979,-3.445336,1.724935,-8.554997,6.508194,6.858505,5.801253,0.656260,0.023285,3.224231,-0.802107,-2.245472,0.768398,0.029650,-2.351916,-5.079408,1.925024,9.288169,4.903511,-3.055621,1.756101,9.189928,-1.425373,4.133541,-4.931903,4.697917,2.837110,-3.605002,5.693966,-2.001612,3.752589,-3.630292,2.431777,1.867564,-6.042135,2.397322,0.931067,-9.297387,-9.458330,4.784591,-9.078447,9.106356,-9.774936,-2.861436,5.977571,7.265265,8.961931,-8.314436,-2.278548,6.747039,1.732991,-3.012961,6.244002,-3.129416,-5.129368,-2.717197,-0.539624,-4.041026,-8.986791,-4.913551,0.657951,-9.377980,-8.864997,3.666516,-6.670517,3.649789,-2.904447,-5.471287,-7.117530,1.819966,-3.404819,3.650418,2.185492,4.556163,-0.410070,5.290003,1.042601,-3.773138,-4.209925,-9.837919,-5.813953,-5.038520,9.331053,-8.400499,-4.201522,-6.175427,-5.163514,9.720867,0.239669,2.310669,7.287713,6.055934,-5.954361,-5.797581,-7.492321,6.556491,-9.469588,1.268896,-2.012928,1.729640,3.817908,2.279250,6.032385,3.328076,9.661925,-5.508579,5.888933,5.901285,3.155154,9.217727,6.976081,-9.455670,-2.927413,6.294979,5.549894,1.402052,0.168017,-4.037250,-1.836530,6.305425,-4.306324,-5.847859,-1.719590,8.948423,3.264895,9.822668,4.070426,-2.862522,0.405236,-0.351579,-7.090352,7.882931,-0.923490,-2.779860,3.296335,-4.294096,1.135967,9.476354,9.750292,9.461336,2.131926,5.641369,-1.322206,2.690537,8.491866,-9.491054,4.803164,6.799437,-3.003477,-8.981986,-5.912562,4.929750,5.833838,1.852428,-1.401656,3.148062,3.123129,-5.469118,-7.723450,2.862852,-9.352464,9.522520,2.972069,1.959578,-5.830588,4.752064,6.555877,-1.022827,1.386308,8.765866,-4.840772,-0.441994,2.450217,5.254275,-9.094745,1.795819,1.349844,-6.499707,-2.800591,-7.302204,-4.883092,8.029638,-6.689320,-9.295775,0.705452,4.918889,3.109479,8.377255,8.111639,-3.145060,0.110280,-3.710874,4.929772,7.040299,-0.143849,-3.323453,4.879773,-5.966354,-2.739109,7.724293,-5.170541,2.482996,-3.309674,-0.766551,-5.715507,1.735969,3.052451,-1.667713,7.305311,-3.521771,1.909735,-2.188496,-5.401632,-2.524644,1.750952,-5.232445,0.906562,6.177041,-5.825423,4.690910,1.540937,-6.436929,-7.823826,4.433900,-4.002184,5.985203,-3.909984,-9.988184,3.338737,1.551440,-7.435794,-4.701423,-2.297020,-6.572349,-4.552367,9.699819,-5.468436,-0.196778,-7.394392,-0.501036,5.686955,-5.742790,3.077008,-1.985467,3.425945,-0.880136,1.104801,5.757876,-2.218137,-1.385815,1.839839,-7.451021,1.004627,-8.855654,-0.309402,-5.531712,3.146162,-5.087532,5.885671,7.000103,-4.937460,-3.895110,-0.368598,4.827750,5.523549,4.560692,3.600780,7.234423,-9.171604,-6.002287,-7.111081,-3.870330,3.453134,1.417796,3.446971,-9.031759,-7.452634,6.716815,-8.325516,3.919495,-2.481617,1.573164,7.705902,-2.253203,-1.130672,-8.200042,0.337722,-5.052029,2.981139,2.251866,-4.801814,4.706448,8.236722,-2.548507,2.178562,7.815128,-6.197753,-8.949643,3.260714,-9.978398,8.798863,7.256639,9.698928,-4.035127,1.131708,-7.783700,1.319197,-0.506674,-6.712138,-9.753689,-2.268877,-5.043195,-8.125684,-0.160476,6.001741,-8.868369,-1.973118,-7.022142,0.488144,-6.833997,-0.004338,9.522714,-5.367550,-8.062867,-4.767100,8.056713,4.513978,0.685343,-0.455377,6.380131,-3.087515,-9.346349,2.952796,5.858552,0.804741,6.718668,-3.016774,4.118806,-0.795688,6.506931,5.151810,-1.180787,-9.111781,-1.268042,9.887378,1.412713,3.125997,-1.018706,-1.729911,-8.110473,-5.520103,2.215690,-8.845662,2.136455,1.779554,6.337337,6.095325,8.906760,1.948205,-4.914722,8.591795,9.669680,-2.688320,-2.004805,2.270635,-0.755977,-6.559355,-1.651249,6.388053,-0.665273,-4.041170,7.099419,1.002880,-9.312145,-3.551321,4.970633,-1.075773,9.759866,8.355510,6.356504,-1.691395,-1.798557,4.213948,2.124546,-7.045094,4.804876,0.857777,4.684861,4.200970,0.168405,-2.217433,-1.235080,6.551879,1.036592,7.121096,4.280384,7.358613,-0.893552,-4.462840,1.116368,6.761503,-7.517120,7.776033,9.591280,1.134225,-6.353601,-1.963189,-4.492827,-6.996792,-7.875336,-6.448975,4.789679,1.406146,-8.304169,2.078335,-7.052917,1.916307,4.539825,-1.185367,4.631237,-2.627092,-4.296285,-6.046606,-0.033098,-6.677512,-4.793468,1.899252,-6.795870,-2.916436,-1.810691,-8.632087,-2.571789,4.966743,-8.708062,2.892417,1.275905,-1.800123,-1.987045,-1.799703,6.967371,4.627456,7.922048,-6.448084,3.762427,9.295517,-3.639013,-1.351573,3.353926,4.492105,-2.003377,6.836784,-3.248708,0.255342,1.014738,4.798980,-8.963337,-5.653984,0.423842,-7.309551,2.716108,4.474110,9.034158,4.682142,4.461425,9.983578,6.419625,-2.939374,-8.160631,-9.457887,6.382481,-3.411211,-8.449361,-5.818901,6.575900,-3.552420,-6.581668,1.069259,8.217771,-6.113295,9.934993,-7.335352,-9.513214,-7.441776,-2.517421,-7.506214,-4.274859,-8.693334,-8.599240,4.982500,3.298227,-8.223342,3.856570,4.864570,-7.977407,2.211374,1.060146,-6.728644,-7.891450,-0.085221,0.208409,1.119616,-9.267640,-3.797078,-0.990730,-7.667644,5.380656,1.549576,-7.617638,-0.642048,-7.611918,-2.320040,9.159553,0.573806,6.034305,6.853909,4.662598,9.400734,-0.769970,-8.602516,6.636282,-9.830201,3.193134,1.645088,-0.310750,4.580685,2.931842,3.880383,-9.979811,6.566144,-2.152867,3.099662,3.254714,2.896169,-6.456764,-8.842789,4.617952,8.749125,-1.567769,-9.658407,-5.285349,1.983610,-6.054012,-8.618196,8.454843,-7.968739,-7.685588,4.118728,-3.082820,9.603718,-6.205442,-8.374864,-2.989586,5.201500,-8.573285,-2.138138,8.757001,9.509464,-5.636577,-8.677519,5.149632,6.133950,-6.866725,6.856457,-1.896873,-6.071558,-1.792241,-6.657324,-6.828615,7.925956,1.637706,7.476898,0.712309,-2.088819,-1.797941,4.343360,-7.598057,-5.256777,-2.243075,1.988677,-6.231431,9.588464,6.918257,-8.603915,8.069749,-1.763337,5.384327,1.311950,-0.192444,-2.971191,9.458509,-3.693594,-5.696392,-8.183840,-5.093621,3.690592,3.347374,4.602566,-4.999024,-5.715378,7.999450,3.974008,-5.693071,3.284291,-0.769023,-2.961425,-2.474985,9.182182,2.672375,3.427997,-2.434679,-2.785139,8.205058,-2.405195,4.392016,-9.670466,5.804903,6.834751,-3.672187,1.622427,-2.172195,-3.873375,-0.087771,-0.346613,-1.726655,-2.556469,-3.103374,-2.121174,-1.652281,-3.183317,-4.896433,3.904312,-6.641157,2.845022,7.347681,7.817033,-2.718276,-5.321699,-6.076429,-8.236881,-1.310803,1.838237,-0.685740,8.781916,-7.972680,-6.128772,-8.743761,-9.662337,0.975609,1.668180,-9.146240,-8.233856,3.984753,-3.276535,5.212167,-3.892076,7.541496,5.927473,5.527579,-6.787110,-7.318965,-6.358322,-8.435100,2.282545,0.689955,3.942378,4.374955,-1.824280], dtype = "float32")#candidate|8063|(672,)|const|float32
var_8064 = relay.var("var_8064", dtype = "int32", shape = (30, 6))#candidate|8064|(30, 6)|var|int32
call_8061 = relay.TupleGetItem(func_7056_call(relay.reshape(const_8062.astype('float64'), [112, 2]), relay.reshape(const_8063.astype('float32'), [56, 12]), relay.reshape(var_8064.astype('int32'), [180,]), ), 0)
call_8065 = relay.TupleGetItem(func_7061_call(relay.reshape(const_8062.astype('float64'), [112, 2]), relay.reshape(const_8063.astype('float32'), [56, 12]), relay.reshape(var_8064.astype('int32'), [180,]), ), 0)
func_7924_call = mod.get_global_var('func_7924')
func_7925_call = mutated_mod.get_global_var('func_7925')
call_8066 = func_7924_call()
call_8067 = func_7924_call()
func_6472_call = mod.get_global_var('func_6472')
func_6478_call = mutated_mod.get_global_var('func_6478')
const_8094 = relay.const([-9.219842,4.721384,-5.343282,7.964923,-4.259499,-4.254335,5.404702,-0.002208,6.707132,-1.826673,-6.566323,-6.024119,0.210598,-5.355275,5.249325,-0.504276,-8.501759,8.365047,8.410151,-3.256645], dtype = "float64")#candidate|8094|(20,)|const|float64
var_8095 = relay.var("var_8095", dtype = "float32", shape = (882,))#candidate|8095|(882,)|var|float32
var_8096 = relay.var("var_8096", dtype = "float32", shape = (8, 16))#candidate|8096|(8, 16)|var|float32
const_8097 = relay.const([-10,9,-6,5,-6,-6,-3,7,-3,-4,-8,-5,6,9,-1,-9,5,-6,1,-3,-10,-7,7,-10,-6,3,-5,-4,6,-7,6,-7,4,-3,7,-3,7,9,-5,6,3,-7,6,3,5,-1,6,3,3,4,-4,-6,-8,-6,-4,-6,2,7,-5,3,10,2,-4,-3,-10,7,-5,-6,-10,8], dtype = "uint32")#candidate|8097|(70,)|const|uint32
call_8093 = relay.TupleGetItem(func_6472_call(relay.reshape(const_8094.astype('float64'), [5, 4]), relay.reshape(const_8094.astype('float64'), [5, 4]), relay.reshape(var_8095.astype('float32'), [882,]), relay.reshape(var_8096.astype('float32'), [128,]), relay.reshape(const_8097.astype('uint32'), [70,]), ), 5)
call_8098 = relay.TupleGetItem(func_6478_call(relay.reshape(const_8094.astype('float64'), [5, 4]), relay.reshape(const_8094.astype('float64'), [5, 4]), relay.reshape(var_8095.astype('float32'), [882,]), relay.reshape(var_8096.astype('float32'), [128,]), relay.reshape(const_8097.astype('uint32'), [70,]), ), 5)
func_6472_call = mod.get_global_var('func_6472')
func_6478_call = mutated_mod.get_global_var('func_6478')
call_8108 = relay.TupleGetItem(func_6472_call(relay.reshape(const_8094.astype('float64'), [5, 4]), relay.reshape(const_8094.astype('float64'), [5, 4]), relay.reshape(var_8095.astype('float32'), [882,]), relay.reshape(var_8096.astype('float32'), [128,]), relay.reshape(const_8097.astype('uint32'), [70,]), ), 6)
call_8109 = relay.TupleGetItem(func_6478_call(relay.reshape(const_8094.astype('float64'), [5, 4]), relay.reshape(const_8094.astype('float64'), [5, 4]), relay.reshape(var_8095.astype('float32'), [882,]), relay.reshape(var_8096.astype('float32'), [128,]), relay.reshape(const_8097.astype('uint32'), [70,]), ), 6)
func_5096_call = mod.get_global_var('func_5096')
func_5100_call = mutated_mod.get_global_var('func_5100')
var_8112 = relay.var("var_8112", dtype = "float64", shape = (160,))#candidate|8112|(160,)|var|float64
const_8113 = relay.const([5.844027,-1.782768,8.843117,6.108615,-9.888854,4.714879,2.478474,2.114187,1.780208,1.086066,4.312543,-0.497878,-6.324114,-8.953394,-9.934886,-1.573213,-8.094598,1.874669,2.868603,2.628141,6.153349,-9.710763,-7.470186,2.238562,2.917086,6.227354,-6.378159,-5.164924,-0.405422,-7.471659,7.902730,-3.816867,-3.037644,-0.385613,-5.892709,8.714617,-1.525803,9.883544,-1.073029,-1.775701,3.870797,-8.545459,-2.942987,-0.938970,0.009341,6.988855,8.146166,3.924560,4.655696,6.670255,4.180999,-9.049584,5.181331,4.242487,-7.036683,9.429963,0.821778,-8.206502,3.412617,6.347772,4.028363,3.901926,-8.914881,-2.358489,-6.892073,-8.918920,3.835711,-5.651822,-9.264555,-6.099224,9.894536,-2.114207,5.778199,-5.403876,0.686260,-1.212376,7.647158,0.091082,-6.050560,6.759411,-7.186147,-6.555416,-4.286032,-6.156957,-4.867951,-2.801255,-8.482330,0.709563,4.150333,-7.519377,6.202993,5.682056,9.558370,-1.549230,1.546631,-7.285943,0.466367,9.453701,3.250694,-9.479386,-3.941875,-5.292151,0.716188,-5.812477,3.175957,8.545694,7.249356,2.649629,-3.044974,-9.761713,-2.691626,2.666662,-0.358840,6.662495,-6.428391,8.939673,-4.818230,4.906117,1.135715,-1.258852,9.181570,7.384586,3.262154,8.872893,0.656309,3.021584,-1.041143,7.323743,9.327038,9.952305,9.124644,-3.324896,-2.969915,2.903347,4.755383,-8.148363,-1.196750,-9.827550,1.979483,2.387735,7.457321,-5.207435,9.506278,-8.383287,-3.135159,-9.165321,7.366548,-2.662858,-6.947921,7.138764,6.725139,-2.925659,-9.393655,8.588225,-9.530174,-3.759083,5.166645,-5.851692,-2.514359,4.806303,-7.939502,-0.861837,-5.272588,4.368204,5.446881,0.240638,-4.103358,-5.775376,-4.003045,-1.818054,-6.008988,-3.423037,6.430722,-7.103548,-0.207838,5.505985,0.074195,-4.886311,-3.597469,-4.531859,-4.146124,-1.925660,-0.750373,3.066463,9.949159,5.606333,-3.143403,3.579602,-5.975804,-6.857730,-6.868311,9.985234,8.642297,2.110938,7.194256,5.264658,2.019876,6.872780,-0.371338,-4.516461,-4.848785,4.153072,-9.337938,6.597548,-1.985804,6.967044,0.490293,-8.994022,-3.632132,-6.201925,-0.688536,3.698366,6.846254,9.778770,-9.004066,5.509624,3.208171,0.155847,-2.733259,1.246789,-6.071510,5.684322,9.411099,3.458496,9.488869,-4.840710,6.064962,-1.475168,-7.862934,4.617794,4.427714,3.761387,4.936940,-0.761458,3.336696,6.318732,-8.653224,1.575183,-1.283638,2.774674,-3.190939,0.640829,-2.357519,0.129543,0.465423,9.300926,3.272926,-0.346551,0.103721,-0.456577,-4.137385,8.414628,-5.403628,-9.045140,4.964685,7.190904,1.809597,0.703349,-0.625606,-3.422171,8.492733,-4.134418,4.674647,-8.410898,-3.909005,7.162612,-8.455501,1.820303,-4.512828,3.046190,-4.031480,3.403171,-6.719165,7.678962,1.741393,-6.336033,2.207528,-9.585636,4.178367,8.886460,7.100684,-0.462484,2.579018,0.759337,-2.353179,1.331474,4.187759,-4.138990,-8.531590,-1.932708,-2.501402,-4.177743,5.644688,-3.282835,6.056419,-2.405408,-8.405963,-7.317588,7.200583,3.250775,3.637189,-6.909622,-8.829022,-5.659605,-2.728449,-9.807311,7.058190,-9.683635,9.936175,-5.049552,-2.309694,-0.323166,5.333657,9.171365,-3.262531,-5.217654,2.366863,-3.046387,-9.402445,-0.637084], dtype = "float32")#candidate|8113|(320,)|const|float32
call_8111 = relay.TupleGetItem(func_5096_call(relay.reshape(var_8112.astype('float64'), [8, 4, 5]), relay.reshape(const_8113.astype('float32'), [320,]), ), 1)
call_8114 = relay.TupleGetItem(func_5100_call(relay.reshape(var_8112.astype('float64'), [8, 4, 5]), relay.reshape(const_8113.astype('float32'), [320,]), ), 1)
func_5899_call = mod.get_global_var('func_5899')
func_5903_call = mutated_mod.get_global_var('func_5903')
call_8119 = relay.TupleGetItem(func_5899_call(relay.reshape(var_8112.astype('float64'), [160,]), relay.reshape(const_8113.astype('float32'), [320,]), ), 1)
call_8120 = relay.TupleGetItem(func_5903_call(relay.reshape(var_8112.astype('float64'), [160,]), relay.reshape(const_8113.astype('float32'), [320,]), ), 1)
output = relay.Tuple([call_8052,call_8061,const_8062,const_8063,var_8064,call_8066,call_8093,const_8094,var_8095,var_8096,const_8097,call_8108,call_8111,var_8112,const_8113,call_8119,])
output2 = relay.Tuple([call_8053,call_8065,const_8062,const_8063,var_8064,call_8067,call_8098,const_8094,var_8095,var_8096,const_8097,call_8109,call_8114,var_8112,const_8113,call_8120,])
func_8123 = relay.Function([var_8064,var_8095,var_8096,var_8112,], output)
mod['func_8123'] = func_8123
mod = relay.transform.InferType()(mod)
var_8124 = relay.var("var_8124", dtype = "int32", shape = (30, 6))#candidate|8124|(30, 6)|var|int32
var_8125 = relay.var("var_8125", dtype = "float32", shape = (882,))#candidate|8125|(882,)|var|float32
var_8126 = relay.var("var_8126", dtype = "float32", shape = (8, 16))#candidate|8126|(8, 16)|var|float32
var_8127 = relay.var("var_8127", dtype = "float64", shape = (160,))#candidate|8127|(160,)|var|float64
output = func_8123(var_8124,var_8125,var_8126,var_8127,)
func_8128 = relay.Function([var_8124,var_8125,var_8126,var_8127,], output)
mutated_mod['func_8128'] = func_8128
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6727_call = mod.get_global_var('func_6727')
func_6729_call = mutated_mod.get_global_var('func_6729')
call_8156 = func_6727_call()
call_8157 = func_6727_call()
uop_8162 = relay.cosh(call_8156.astype('float64')) # shape=(9, 2, 6)
uop_8164 = relay.cosh(call_8157.astype('float64')) # shape=(9, 2, 6)
output = relay.Tuple([uop_8162,])
output2 = relay.Tuple([uop_8164,])
func_8174 = relay.Function([], output)
mod['func_8174'] = func_8174
mod = relay.transform.InferType()(mod)
output = func_8174()
func_8175 = relay.Function([], output)
mutated_mod['func_8175'] = func_8175
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8236 = relay.var("var_8236", dtype = "float32", shape = (15, 2, 12))#candidate|8236|(15, 2, 12)|var|float32
uop_8237 = relay.atan(var_8236.astype('float32')) # shape=(15, 2, 12)
output = relay.Tuple([uop_8237,])
output2 = relay.Tuple([uop_8237,])
func_8243 = relay.Function([var_8236,], output)
mod['func_8243'] = func_8243
mod = relay.transform.InferType()(mod)
var_8244 = relay.var("var_8244", dtype = "float32", shape = (15, 2, 12))#candidate|8244|(15, 2, 12)|var|float32
output = func_8243(var_8244)
func_8245 = relay.Function([var_8244], output)
mutated_mod['func_8245'] = func_8245
mutated_mod = relay.transform.InferType()(mutated_mod)
const_8307 = relay.const([[[-4.005607,-4.685701,-0.524798,-4.507184,-0.050545,-3.914611,7.110886,6.511424,7.670318],[9.150958,5.557697,-6.346051,3.080467,-0.705941,6.697189,-2.336372,5.872729,7.797325],[8.482175,5.867173,-0.563805,4.794703,-3.268067,-9.850963,3.985503,6.492912,-6.075886],[3.305829,-5.210316,-9.905574,-3.748196,8.604052,3.134518,6.035513,-4.999323,-1.096616],[-3.496286,6.205422,9.992189,-7.314788,7.478071,9.497643,0.868746,1.950453,-9.485863],[2.846110,-5.932728,-1.485174,4.161606,-3.543636,9.735185,-5.323644,-5.928884,-0.687011],[-4.981578,-9.346922,-1.477869,9.279768,6.701931,9.023554,-6.854144,-1.990488,-2.469022],[-5.157769,-8.101496,8.905551,-1.891397,8.326442,5.907006,-4.636559,-9.533639,5.030170],[-5.252671,-8.693297,0.581463,-5.652800,-9.102894,-4.486531,9.197304,8.666916,4.643636],[4.618932,-5.303063,0.568745,-6.807847,2.022524,-4.685971,-5.760664,8.334243,-4.580367],[-3.772826,-4.072907,5.058293,5.945675,-8.769605,-9.652409,-6.724285,9.973183,-6.514222],[-7.724597,-2.209614,1.340968,9.632423,1.189443,-1.273832,2.587598,-4.084211,-9.190583],[7.964150,5.577265,-1.862219,0.101505,5.193616,0.030626,4.868259,6.118448,-5.273844],[2.982523,-4.037962,-2.402752,-4.360221,0.345892,-3.258882,6.621167,-2.314559,6.073566],[-6.590920,5.034563,3.863181,-2.502805,-6.620535,-2.751593,-6.928046,-1.583361,-9.006363]],[[-4.620653,7.404434,-1.454171,3.225384,1.208806,-2.709498,-3.723817,4.419348,-8.814870],[-6.266105,-4.071385,-2.753453,9.289458,-6.211587,8.467082,9.468343,0.511627,-9.562658],[-9.127805,2.815469,5.744610,-1.700328,4.419695,3.591705,-7.728619,-4.434142,-6.751133],[1.208709,5.812027,-4.120751,-6.072563,-4.208640,-2.484862,3.073542,-5.822446,-3.664447],[-8.418900,4.754422,-7.658285,-4.247863,6.874971,4.169190,8.667820,6.261693,-7.990154],[-8.333317,3.934442,2.277813,2.557107,-6.783285,4.772713,4.784344,8.942684,6.497803],[4.084651,-3.745483,-6.167544,-0.619127,-5.675776,3.544562,0.901569,-6.774980,-7.684632],[-4.412117,-8.833656,-9.818624,9.645011,-7.645945,-1.712185,4.464646,2.938767,-1.547518],[2.535841,8.104576,7.471581,0.212983,-8.432691,4.666196,7.806319,-4.031979,7.209650],[2.642384,-9.893255,1.559572,-3.533417,-6.762179,9.245393,0.496951,-0.928232,-4.804886],[7.347777,-9.729894,2.810527,5.100484,-9.924058,9.871477,-2.629814,-2.668058,-8.468397],[1.132040,-1.360307,-1.627149,6.987727,2.268880,-7.788828,9.536650,2.439209,-7.157106],[1.570615,4.043383,7.431021,2.945971,1.147103,6.415455,-1.866582,-8.944874,-5.467347],[-7.900609,7.228477,9.325127,0.101476,5.334529,6.471646,-3.591693,1.151973,-6.790839],[-0.636490,-6.193599,6.085136,9.545173,7.487661,6.749572,-9.795726,8.272258,4.266500]],[[5.999462,3.635542,1.000774,-8.433300,0.656412,2.382973,4.295897,-3.948025,1.882615],[1.550206,8.158530,5.789107,-4.026138,-0.019860,2.191259,6.092641,-0.483527,7.254692],[7.336046,5.512933,-0.759905,-4.913543,-0.745654,3.050010,-4.697814,-4.957671,7.545341],[-2.391796,6.300919,0.711371,-3.502031,-9.696296,1.909268,-8.823930,3.685010,-6.924269],[-4.532777,6.119702,1.065439,2.130309,6.574030,1.318608,3.863813,2.365324,-7.254096],[4.128010,9.348137,2.296670,5.269900,0.414923,-9.396348,-5.844815,-0.319119,0.108534],[1.198179,4.195504,1.462714,6.048975,3.564013,4.369746,-7.774085,-2.208239,-4.658350],[-8.270253,-0.912483,7.503076,4.954889,9.738681,0.443425,9.377228,1.625008,-5.197151],[2.494709,5.148402,-3.852527,-4.750328,2.227144,-2.496711,3.586375,-8.165744,-0.988192],[-8.313882,2.941778,7.180560,-0.572841,0.990438,1.146162,-1.534908,-1.853690,7.674215],[0.325761,3.877151,6.403984,-2.048475,-1.250233,-2.145990,-2.824085,1.348854,-4.597024],[6.203793,2.870097,0.762984,-4.640561,-3.109136,9.997378,0.351353,6.236764,-3.783355],[-2.038386,9.128482,4.113511,8.872068,-4.764929,6.709861,2.247262,-1.156931,-5.891728],[2.884404,6.974444,5.489603,-1.483160,8.874894,2.158172,-0.083566,1.632082,-5.288626],[1.877428,-7.306975,-8.275062,-4.666789,-1.309843,9.946846,-9.967372,3.448531,-8.892015]],[[9.345011,2.054887,-0.413508,-3.357214,-1.373823,2.768284,-1.619910,-0.607422,-4.018100],[-2.299932,-2.967999,3.512044,9.972184,2.897358,-5.001053,5.657217,-7.794147,-4.433618],[4.824099,8.347310,-4.631690,4.136951,3.282275,-6.834868,-3.531710,-1.309939,9.361987],[-3.252025,-7.265634,-2.673800,4.494999,-5.740551,-7.055330,9.966410,9.845824,-7.005930],[3.826683,-3.990912,0.029176,-7.362438,5.189396,3.125639,4.773204,-3.897224,1.309786],[-3.867235,-1.125189,-8.715104,6.220278,3.243003,-2.389297,1.434488,7.408817,-3.949213],[-6.000959,-7.115702,7.788137,-9.448659,-3.451629,-7.228781,3.572338,-6.560782,6.495317],[5.840311,-2.510733,4.668651,-8.609958,-6.882029,-3.910471,-3.511215,-9.754668,4.923958],[-4.147923,-7.294884,-2.561966,-3.193856,3.187146,8.309889,2.914737,1.271374,3.924346],[-9.849361,9.491292,2.679079,1.403923,-3.740040,5.529395,-0.712294,-5.595056,-6.980087],[3.586120,-3.380427,3.327190,-2.066212,-7.350805,6.404489,-7.257338,4.067791,-8.386584],[-5.498351,6.496397,6.756323,-8.047040,-0.164739,-4.983014,5.201431,-8.232953,-0.957347],[4.874058,-1.783377,8.842017,-9.352955,-2.212174,2.244505,-3.149240,-0.851068,9.737190],[-2.799475,0.923630,-0.493198,9.956706,-7.976280,2.581406,-2.627115,2.072315,6.796802],[-5.795987,-8.034902,8.349824,1.021678,8.174901,0.130841,-6.168943,-9.919993,9.428870]],[[3.188900,-7.731442,-8.390346,2.374808,2.045033,6.935661,9.475745,-4.831654,-2.285380],[0.554825,4.113858,-6.144252,0.033810,2.108800,-2.455739,-0.766232,4.731830,5.978600],[3.856138,-9.278122,0.927688,4.967804,9.906569,0.553899,3.420906,-5.587563,5.757020],[-2.888535,4.753803,4.158226,-1.991296,4.921240,-2.001886,1.201771,9.852171,-4.889263],[2.951662,9.504960,1.277015,0.892772,-0.163093,-6.565119,-3.283408,-5.610508,-4.738461],[3.749679,-9.039846,-9.346532,-1.039342,-5.337423,-3.061498,-2.592974,-6.041551,-7.870221],[-9.455090,-1.944677,9.660557,9.354603,9.708293,6.698273,5.387454,-2.981912,-4.264212],[-1.223985,-0.300318,-8.945417,-8.746045,5.751889,2.026454,-5.278991,7.403050,-1.033653],[7.144762,-7.151482,1.336327,-3.929672,-7.989809,-7.698934,-3.642117,0.342777,9.148941],[8.208548,5.555837,-4.737703,-7.270629,-7.446372,-8.094267,2.128275,-9.623066,-7.343107],[4.869227,-9.306441,-5.725179,-3.868743,-0.543083,4.580860,-8.088723,6.165592,0.776654],[-2.080537,-4.005222,6.270282,4.096813,8.080362,-9.271692,6.795579,-3.960823,-1.622293],[7.379476,8.583150,-2.361589,2.398128,0.099952,-9.096577,5.799319,9.362914,-9.479737],[-2.001332,6.284835,7.353062,3.372682,4.608693,9.087412,-4.815621,7.192518,-9.666937],[0.765897,-4.144342,-0.289041,3.758644,8.699944,5.853562,-2.509856,7.397680,0.769556]],[[8.354882,9.452823,9.137347,-1.303728,6.692121,8.793885,-0.257679,-4.253634,-8.561842],[1.736323,-6.228022,-1.838175,-9.701828,8.867876,-6.962845,0.446966,0.540794,-3.694244],[6.681410,1.274688,-1.724385,-0.834377,7.411599,7.084504,2.287019,8.239537,3.729507],[7.082715,-7.311477,5.004402,-9.990975,1.952367,-2.247551,-8.575808,-4.078397,-2.675859],[-3.011387,4.774944,9.514134,3.360750,-8.687003,-8.085726,-9.365094,5.814068,-2.049575],[0.740313,5.765240,4.295992,9.967842,0.749136,7.575161,-3.686646,-2.452261,6.764401],[0.103526,-1.348583,3.490102,5.702199,3.251538,7.621150,-2.409908,-6.733716,1.835898],[1.554344,1.276023,-4.556398,-7.500147,-0.886719,6.248078,1.747539,2.729871,-1.623968],[-2.045467,-8.355242,-8.925642,-7.680085,7.991308,8.378241,-3.301545,0.658386,1.413914],[-8.429327,-7.370419,4.698430,-0.419156,-6.145485,-7.933914,-9.679303,6.500845,-2.849268],[-0.192257,-1.365189,7.637368,-3.250705,-2.128563,9.274840,-2.000015,2.064314,4.515263],[-8.181594,3.213946,0.115409,5.265437,1.092626,-6.745560,-3.645605,-8.476396,-6.827255],[-9.383753,9.400579,-6.767487,0.651272,-7.542422,-4.460646,5.578788,6.220938,9.615924],[-4.626584,-6.798279,8.481786,-6.471783,-5.328256,-5.950213,-0.745198,6.509150,0.735021],[7.192797,-2.366934,-2.249120,8.421975,8.858026,-4.543822,1.751812,4.156230,-2.348926]],[[-0.228237,7.470609,4.875183,-2.118899,-4.895759,3.941203,8.340136,-9.702598,-3.633499],[-2.886569,-3.677864,-6.534234,7.350951,-5.391151,-5.933991,2.549696,0.916626,5.969739],[1.864571,-9.199087,7.182886,9.411517,-2.112342,2.235423,-9.044305,-2.744138,9.721605],[-9.258959,-5.153387,-0.930407,8.705729,-6.990853,-2.386041,-4.776250,5.776338,5.754267],[-2.957775,1.406202,8.885324,-8.386381,5.530871,-0.933844,1.328225,6.135482,1.504760],[-1.255703,9.807260,3.751116,-9.989338,9.468305,9.144022,3.402894,-5.472421,-3.158389],[6.591662,7.857264,-1.227121,3.560853,-9.610096,1.023034,-7.685652,8.959270,-2.883863],[8.707966,-0.288450,-2.521285,-7.578766,1.266755,5.351276,-1.853167,-7.080672,0.987189],[4.761516,9.820809,2.023636,-4.385931,-2.630715,3.506586,-5.306073,-5.910369,-4.711961],[-5.274815,-2.711854,1.598130,-2.620495,-5.630208,3.378775,4.360983,-1.866688,0.942500],[9.879697,-9.780233,6.095558,0.047082,-8.568837,-2.313537,-5.593000,7.982967,-3.882350],[-2.746423,-9.924109,-8.054865,-0.047651,6.899244,-1.901375,-5.141851,-9.002384,2.634218],[5.423997,8.354858,-1.019470,-5.495551,3.011217,3.727558,-6.538825,-9.602730,-4.423320],[-2.773701,-8.549669,-2.033404,-0.292359,-8.205352,1.530017,-9.594656,-1.641456,-3.537542],[1.757706,-7.149096,4.215614,8.633196,5.261052,-2.006099,-5.216639,8.253261,-2.335123]],[[1.666046,-8.988248,5.999247,1.590705,-9.422144,-9.389908,4.020227,9.049827,-7.930387],[2.707891,-6.710454,8.311770,6.400025,-5.602183,-2.472106,-1.707413,7.008608,4.689256],[-6.301904,9.895049,8.560575,4.336746,2.934495,-9.822645,8.427944,2.339312,-9.311632],[4.890877,-5.690042,-0.702191,-2.295102,-3.040474,-5.748999,8.119898,6.220648,9.994398],[-6.703742,5.840369,-7.416046,6.950071,0.678117,2.191870,1.762798,7.149006,-4.900298],[-7.566304,-2.592392,8.535828,-1.631870,4.653973,8.164618,-0.107100,-8.054577,6.445392],[2.527953,-9.474343,-1.968045,7.595829,-2.008642,6.984151,-9.185839,-3.706305,8.733471],[5.058304,-4.813795,1.228493,-0.896839,6.224680,7.353717,5.224700,4.114373,0.632555],[0.027448,1.526478,-0.559035,9.218037,-9.296429,6.803149,8.601998,7.608198,-1.572949],[3.580875,1.395032,3.132714,6.195580,6.680023,-9.319260,-4.399723,4.681878,-2.072298],[8.264587,6.028254,3.215848,0.933894,4.899855,-6.134004,4.578946,-7.679172,-6.476338],[3.602691,-5.577880,-8.496943,6.544959,6.100656,-3.553983,-2.590072,1.505069,5.468040],[0.985525,0.164468,0.182802,-9.036919,3.805600,6.213145,-4.654085,7.910080,-9.809833],[1.490669,4.113503,-9.734381,-5.565659,5.271833,-8.909575,-0.621058,4.269702,1.064283],[0.443227,9.404130,-0.090866,-2.929689,6.072567,-1.281092,1.493514,0.584799,-9.579102]],[[-6.307255,7.362583,-3.771787,-0.368195,0.036233,-4.797024,4.265023,-7.101425,-7.602602],[0.462826,9.965528,-3.849190,-1.377018,6.139357,-0.446766,-8.762748,0.640135,-7.135648],[6.202166,-1.408927,-4.314782,6.801370,7.701225,-1.066615,9.017643,-4.820037,-7.592862],[-8.811264,0.334345,5.739057,2.000805,-2.220045,9.085815,-4.421674,-4.571053,8.405794],[0.491876,-5.768903,-7.132269,-2.907405,-4.486922,-4.457659,1.568341,-8.371452,-2.589528],[2.233068,3.641202,-2.838948,-2.400346,0.528786,-9.029076,-5.782875,-6.831000,-4.482947],[4.464061,-0.461061,4.321285,8.857239,5.956295,9.505822,0.467293,6.028363,5.407678],[6.019636,-6.660505,-4.841562,4.792351,-4.180785,4.310231,-3.219418,2.119846,-5.070285],[2.808961,8.995698,4.892240,-4.110363,9.603163,8.496200,-5.506572,9.762705,-5.254847],[2.604116,-1.885657,8.833839,-5.199350,-0.849288,-7.396081,-8.417608,-6.621654,-1.417656],[4.277670,-6.106675,-1.485313,0.351679,-7.254910,0.734328,-7.914442,-6.279995,-5.462070],[-7.945456,8.922358,-5.789927,3.545768,3.286690,-0.486920,-4.748947,5.415158,5.193910],[-3.767116,-6.522103,3.353219,2.216947,-7.885874,-4.276060,6.482922,1.788961,6.553074],[-5.536876,-1.320425,1.554372,4.373449,-7.663098,-7.939604,-0.655367,-5.565325,-3.738953],[-2.574177,0.767678,0.887095,6.090481,-6.853969,-9.744567,-3.745787,6.600769,-2.373035]],[[-5.392432,-2.033973,-4.001140,-6.230006,6.547527,8.107161,-1.474721,-9.368418,-0.100755],[3.249517,-2.989627,-2.667800,1.879916,-7.180879,-6.976067,2.235754,-8.141435,7.283699],[1.148182,-0.716557,4.913553,-4.308901,3.457958,3.198569,-1.066566,-8.470114,7.932063],[0.575248,1.734056,5.390354,5.279172,-4.635832,-7.021619,-5.043345,2.005724,-3.021785],[3.763469,-3.466063,9.643522,-8.016049,-8.446484,8.479853,-3.612309,5.036867,-1.778445],[1.198770,4.266848,7.888482,1.344314,9.430893,-2.212981,8.429847,-7.022634,4.994344],[-9.790389,-9.944855,-8.535580,-0.490816,-9.768843,-7.190954,-4.626669,-7.863274,-7.980826],[6.589549,-7.498247,-3.893030,-1.432819,-1.390707,-6.900102,2.577613,4.575276,1.418228],[8.073560,-3.573635,0.560671,-7.399649,-3.870333,-6.692533,-3.324523,5.930345,-1.899388],[-9.132744,4.251335,-4.833604,-7.491988,-7.349449,3.344240,2.087180,3.535591,-7.018888],[-9.518650,-5.040478,-3.531670,6.365466,-3.653702,0.220882,5.070736,-4.023814,-1.217962],[-7.696496,-4.806771,-7.472145,-3.230946,-3.869516,-5.538050,7.007247,8.186407,3.382522],[-4.515645,-2.455617,2.132593,5.716778,4.712469,-0.435726,-0.943059,-9.219634,3.096006],[-7.316953,-2.686921,-2.445001,-2.489771,-4.384801,3.886633,7.125718,-6.630302,1.007495],[6.698030,-7.136184,-4.964095,-4.283987,8.856226,1.743354,0.834448,5.308351,-7.522536]],[[-5.840635,1.488771,-3.341333,8.371879,-0.590730,1.822567,1.958103,-0.301125,-8.000617],[-6.654595,-0.377599,6.079817,3.050380,4.513018,7.085088,-4.734148,-6.569452,-0.654785],[-9.169025,-2.867921,5.120865,-2.370681,-2.616688,7.973788,7.991387,2.829563,6.353512],[1.269687,-2.010042,3.126443,-3.640142,2.549525,6.689036,2.201412,0.335129,-8.479307],[-2.566529,-7.674749,-2.846503,1.725352,1.638078,5.109024,5.193269,6.234515,9.043857],[2.742097,-0.541323,2.257402,-8.311453,-9.617109,-7.981333,2.577776,0.020156,-4.584262],[6.338724,-0.153922,-5.346220,9.152009,-8.028902,9.075627,-0.813799,-5.908044,-3.133834],[-3.307404,-6.723358,-4.056258,-7.724394,7.357099,7.213613,9.942951,3.356534,-1.219154],[1.597062,-8.388199,-9.405815,0.636323,-7.516662,-6.812364,8.976434,-8.512805,5.300116],[4.748730,-7.149230,7.445927,-9.250870,-6.443197,-2.470153,4.613321,-8.764308,-8.225234],[-0.178178,8.646803,1.250719,3.354354,6.575756,-8.587326,-0.042609,-6.818483,4.847234],[7.428203,-9.348229,1.017615,-8.685620,-3.336682,-4.656918,2.791097,-0.108452,-8.263500],[-2.241595,5.412058,1.560227,-5.877263,0.317932,-4.517633,8.525471,-6.843202,0.290340],[-6.430180,-1.419243,-4.009182,3.798042,6.390512,2.580849,8.003763,9.189538,6.163467],[5.954566,6.215829,-2.640089,8.522708,2.456883,7.059071,5.275503,-9.097148,-7.875236]],[[8.354500,-7.292800,3.787782,-4.614076,-5.467275,6.274751,-1.040076,6.577601,4.736079],[5.043884,9.853746,-9.736944,6.466551,6.648649,-9.050845,-6.547858,7.674574,-6.794175],[-5.084077,-2.970706,7.912898,-9.081065,-0.029916,0.286487,5.331648,-9.219819,6.043187],[5.680098,-1.115321,-1.299449,-5.213068,-2.167498,4.503581,4.544971,0.261509,-3.736301],[4.306621,-6.458705,0.370568,-9.371702,-3.918524,1.929758,7.669625,-6.081773,9.230302],[-3.573079,-2.127938,-1.268838,-8.864955,8.781135,2.893132,-2.528841,6.080465,-8.348100],[-5.871099,6.338374,3.933780,-6.568799,-5.620290,-9.746580,2.295531,7.745968,-9.804712],[8.749395,1.152556,-0.363742,6.685774,-7.503186,-9.653610,6.080692,0.171855,8.342782],[0.504695,2.003004,7.624902,-0.433011,3.789830,-3.541074,4.624244,-6.098089,-0.549730],[2.404748,3.425932,-9.564372,-0.697537,-6.142176,3.129550,-8.333750,5.593392,-7.496190],[8.328635,5.258827,-5.998938,-9.821583,0.002616,3.419318,-5.180169,8.767539,-1.924974],[0.667095,1.548728,-7.022701,0.363878,-4.989215,-6.199757,6.000116,3.667736,-5.121193],[-5.858178,4.515087,6.936192,-7.385711,8.476492,3.224119,7.542109,-2.704665,-0.815003],[8.886479,9.374525,-2.162168,-3.085058,1.741109,-7.843276,-8.858306,1.700792,1.497554],[-4.755354,-6.017139,9.308827,8.041464,-8.776783,-5.304767,-1.807851,-6.613355,8.258515]],[[2.775126,6.168005,9.693453,6.879232,-2.257815,2.987729,5.214724,5.613253,3.167946],[-9.226209,-6.251861,-6.218716,2.161371,-8.283591,-2.607265,9.688769,-4.463308,-1.627797],[-0.498142,7.733626,-1.670487,-7.728114,-8.484528,4.179108,4.405207,-7.877579,-5.099236],[-0.479735,8.158220,-8.901269,-9.336174,4.597492,-7.571377,-9.993123,0.563459,7.443680],[-7.363313,-2.208335,-8.377945,-5.802569,3.567106,9.882601,2.208387,1.992704,-9.451071],[-4.428065,6.780227,6.074155,6.034641,1.740372,1.591042,3.402938,-7.173145,-6.182966],[5.874903,-5.512517,3.906924,7.524597,4.180700,0.993996,-6.788523,-3.619937,-7.433012],[4.883936,5.477952,-4.984237,3.925897,-0.862190,5.810638,-9.024820,9.382938,4.352202],[-4.544275,6.574624,-1.492826,-5.932982,-7.030372,-6.108280,-3.351915,8.196571,-1.107339],[8.398854,0.778747,-0.226589,-9.573100,2.220561,0.210007,8.459852,6.234826,-3.898856],[1.570396,-1.300321,7.428113,-0.283967,-8.505367,-0.788403,-6.747423,2.875190,8.315679],[-5.283618,-1.169543,-8.736007,2.180687,-5.588060,-0.642984,-2.231373,5.859113,-7.554564],[0.523548,-6.379099,-8.443691,2.690733,-9.548414,-5.034287,-3.907553,-1.093245,-1.463010],[-6.196068,-9.205718,4.010358,0.701771,-9.946309,-5.580032,-1.023553,-1.343078,-8.208170],[1.829946,7.106676,-9.708430,8.974845,-8.404307,5.598981,-6.400329,-5.258682,-9.315334]]], dtype = "float32")#candidate|8307|(13, 15, 9)|const|float32
uop_8308 = relay.sigmoid(const_8307.astype('float32')) # shape=(13, 15, 9)
func_6841_call = mod.get_global_var('func_6841')
func_6842_call = mutated_mod.get_global_var('func_6842')
call_8316 = relay.TupleGetItem(func_6841_call(), 0)
call_8317 = relay.TupleGetItem(func_6842_call(), 0)
uop_8321 = relay.cos(uop_8308.astype('float64')) # shape=(13, 15, 9)
output = relay.Tuple([call_8316,uop_8321,])
output2 = relay.Tuple([call_8317,uop_8321,])
func_8328 = relay.Function([], output)
mod['func_8328'] = func_8328
mod = relay.transform.InferType()(mod)
output = func_8328()
func_8329 = relay.Function([], output)
mutated_mod['func_8329'] = func_8329
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6134_call = mod.get_global_var('func_6134')
func_6135_call = mutated_mod.get_global_var('func_6135')
call_8342 = relay.TupleGetItem(func_6134_call(), 0)
call_8343 = relay.TupleGetItem(func_6135_call(), 0)
func_7848_call = mod.get_global_var('func_7848')
func_7849_call = mutated_mod.get_global_var('func_7849')
call_8360 = relay.TupleGetItem(func_7848_call(), 1)
call_8361 = relay.TupleGetItem(func_7849_call(), 1)
output = relay.Tuple([call_8342,call_8360,])
output2 = relay.Tuple([call_8343,call_8361,])
func_8365 = relay.Function([], output)
mod['func_8365'] = func_8365
mod = relay.transform.InferType()(mod)
mutated_mod['func_8365'] = func_8365
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8365_call = mutated_mod.get_global_var('func_8365')
call_8366 = func_8365_call()
output = call_8366
func_8367 = relay.Function([], output)
mutated_mod['func_8367'] = func_8367
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8328_call = mod.get_global_var('func_8328')
func_8329_call = mutated_mod.get_global_var('func_8329')
call_8386 = relay.TupleGetItem(func_8328_call(), 1)
call_8387 = relay.TupleGetItem(func_8329_call(), 1)
output = relay.Tuple([call_8386,])
output2 = relay.Tuple([call_8387,])
func_8400 = relay.Function([], output)
mod['func_8400'] = func_8400
mod = relay.transform.InferType()(mod)
mutated_mod['func_8400'] = func_8400
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8400_call = mutated_mod.get_global_var('func_8400')
call_8401 = func_8400_call()
output = call_8401
func_8402 = relay.Function([], output)
mutated_mod['func_8402'] = func_8402
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6824_call = mod.get_global_var('func_6824')
func_6825_call = mutated_mod.get_global_var('func_6825')
call_8431 = func_6824_call()
call_8432 = func_6824_call()
output = relay.Tuple([call_8431,])
output2 = relay.Tuple([call_8432,])
func_8442 = relay.Function([], output)
mod['func_8442'] = func_8442
mod = relay.transform.InferType()(mod)
output = func_8442()
func_8443 = relay.Function([], output)
mutated_mod['func_8443'] = func_8443
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6227_call = mod.get_global_var('func_6227')
func_6228_call = mutated_mod.get_global_var('func_6228')
call_8508 = relay.TupleGetItem(func_6227_call(), 1)
call_8509 = relay.TupleGetItem(func_6228_call(), 1)
output = call_8508
output2 = call_8509
func_8513 = relay.Function([], output)
mod['func_8513'] = func_8513
mod = relay.transform.InferType()(mod)
mutated_mod['func_8513'] = func_8513
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8513_call = mutated_mod.get_global_var('func_8513')
call_8514 = func_8513_call()
output = call_8514
func_8515 = relay.Function([], output)
mutated_mod['func_8515'] = func_8515
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5955_call = mod.get_global_var('func_5955')
func_5957_call = mutated_mod.get_global_var('func_5957')
call_8587 = relay.TupleGetItem(func_5955_call(), 0)
call_8588 = relay.TupleGetItem(func_5957_call(), 0)
func_5363_call = mod.get_global_var('func_5363')
func_5367_call = mutated_mod.get_global_var('func_5367')
var_8603 = relay.var("var_8603", dtype = "uint64", shape = (72,))#candidate|8603|(72,)|var|uint64
var_8604 = relay.var("var_8604", dtype = "uint64", shape = (288,))#candidate|8604|(288,)|var|uint64
const_8605 = relay.const([5.832478,5.831795,0.509038,-9.044266,6.203848,2.581423,9.239162,-1.673863,-9.497158,5.992509,8.948914,7.809478,6.754147,-5.001686,-1.404200,-5.638491,-6.213551,1.420921,-8.827869,-4.571763,-4.482895,3.382391,-1.339139,9.949942,0.639739,1.181978,-1.287343,-4.264053,-7.965335,-0.107281,-7.564722,-1.982264,1.852572,-1.032728,1.415518,4.301829,-8.678474,3.894932,-5.505155,7.432363,-3.224280,-9.839879,2.627211,-6.185501,-8.913639,-3.211566,-6.317366,4.451055,8.155009,0.614425,-2.803982,-8.778560,8.132625,6.207956,-9.185946,6.276548,4.722118,5.883589,8.354652,-3.448207,7.028830,-9.224805,-5.940262,7.578742,2.200838,-1.598040,5.852731,-6.969427,3.731842,-2.224241,-0.857328,-7.807784,-5.557274,-7.823017,4.023117,6.945163,4.682763,-9.917036,2.366378,4.146232,-9.037109,-6.996726,-8.983917,6.365405,-2.409640,6.156008,8.670976,-5.115493,-0.581312,5.807554,8.213793,-3.185713,-5.083463,-7.546975,-6.412997,-7.183971,-0.639040,-7.072634,6.984709,-2.732374,0.596659,-0.926205,1.972275,-5.938696,9.728829,8.954682,-0.884094,-9.929792,6.106288,-2.111229,-3.003130,-3.107378,0.665476,-6.343559,-5.515495,-2.712657,-8.675296,4.651179,7.227654,6.541718,5.053696,-6.763460,-1.149457,3.436593,1.708115,6.904464,-3.019404,-7.196650,-9.077677,8.473712,6.318513,8.689521,-6.649146,5.502170,-1.216969,0.871668,-3.947084,-4.407305,-3.076947,-7.659289,0.884959,3.376922,0.274775,-4.313136,-8.978200,7.388084,0.962190,-0.617705,1.699284,-5.967767,-0.348203,5.501110,8.338279,-3.701776,3.253511,9.143446,-8.726970,1.260861,3.662622,-9.596003,5.968434,3.813419,-6.705793,-8.668539,-8.550780,2.748569,-3.548543,0.462149,-5.756840,3.789529,-2.702036,2.228984,-6.468459,-3.320746,-7.794520,4.787468,-3.656768,-8.608165,-1.419464,-7.940136,8.087967,-1.012556,0.239875,2.398364,4.174318,3.653348,-4.087938,-0.577552,2.270433,-6.909033,7.466760,2.177942,-2.784208,-9.191016,9.817229,3.357841,5.637527,-4.871596,6.858018,-1.753882,6.922718,-0.265186,-4.869662,-4.943093,-3.513512,4.136533,-9.746010,3.983558,7.257624,-5.686227,6.061571,5.015186,5.076290,5.826174,-5.921745,9.921883,9.824149,1.155936,-2.185051,-0.569065,-7.180657,0.218517,-9.960592,7.470826,-6.158800,-3.306929,-3.841559,-7.128393,-6.363737,-2.867842,-9.527669,-6.407748,-1.613152,2.493843,3.331190,7.923087,-7.623573,-7.116246,8.757514,-3.697542,4.670966,3.004367,-3.942892,0.556791,8.539729,1.851225,4.896239,-7.705362,5.625713,4.735278,1.657043,-0.825352,9.082025,-1.745101,9.680043,-5.846813,-8.795750,-1.028036,-2.814260,8.251225,4.304453,0.324852,-0.607408,-8.229852,2.858960,-6.469378,-7.848580,-9.613806,6.063283,2.889069,4.877804,-0.076601,3.481898,3.797440,-2.325880,-8.688419,6.808297,1.916987,6.112999,-6.965327,0.061848,3.674985,9.692865,7.446414,-3.275496,7.659093,-8.113339,5.212472,-0.294409,2.131438,5.050430,8.687953,6.170324,-4.663956,-7.529836,-5.284431,7.214803,-3.338977,0.850052,-1.659449,-8.971145,-6.093760,1.456917,-7.733864,-9.963931,-3.537703,8.115477,-3.337356,-5.913377,7.341064,8.188993,-2.241006,2.072460,-9.796098,-9.551583,7.410764,-5.726625,-7.716873,2.863544,-5.332174,-3.332327,-5.499790,-4.029993,4.566040,7.622623,5.728253,-7.089620,-9.338742,-2.963469,-5.764384,3.535963,9.837470,2.006386,5.545936,2.176357,-9.335866,-1.973593,0.370434,-7.446216,-9.450128,-3.005458,-9.478280,2.052264,-3.382535,9.367943,0.532015,-2.028585,3.269118,-6.333855,2.246363,-9.075290,3.619338,-5.406253,8.837913,6.858451,-6.853580,7.983519,-0.513620,4.732741,0.838685,-2.981473,7.813639,2.495673,-7.921480,4.859289,7.487785,-4.449836,9.051424,-2.712535,8.973225,-3.465654,1.997065,-8.199677,-2.745109,-7.461455,7.831184,-0.884361,-9.388651,1.969580,1.772774,-3.297181,-0.572217,-9.530149,6.172687,-6.922140,-1.120008,-3.670026,-4.266226,-6.797860,1.564707,-0.361334,1.173602,5.308267,0.406147,-0.211175,-2.356587,8.211811,7.390518,-9.882416,-4.293390,5.063318,3.755787,-3.544500,1.468157,-2.353923,-6.320905,4.936882,-2.675173,8.708456,9.118120,-6.764652,-1.589480,-0.864868,1.953529,-5.245380,7.976427,8.122941,4.490068,-1.463709,-3.912024,9.392909,-2.632049,-4.155501,-4.017113,-6.582133,0.632660,6.530449,-6.971483,-1.134067,-2.244499,-4.790451,-6.571189,-8.648936,0.752539,-0.023044,3.059009,-9.171072,-3.271121,-0.064930,-4.113270,-2.405505,-2.507967,4.962188,8.926673,-2.648872,-2.778453,0.892586,-1.419074,0.362226,7.902339,9.862221,8.159379,-3.694909,-9.801016,-4.213947,5.598090,2.812643,-4.168306,-6.642601,-8.428219,8.439241,2.237734,8.755457,-6.316241,-6.027998,2.538322,3.353320,0.901685,-5.220508,-6.925289,5.073100,-7.484503,5.593544,0.763126,-5.658495,5.406185,4.065470,9.250125,-4.298976,9.786503,9.025411,6.932475,5.885040,-4.661475,-4.000710,7.638466,-5.515791,-3.841184,-7.526453,4.092191,9.290229,1.246844,-5.983346,-7.879130,-5.911957,9.291013,-8.435692,-5.309375,9.818122,2.934345,-5.046775,4.002598,-1.392360,-3.679560,-0.768830,-2.982344,-9.389861,-8.933459,-4.288411,-2.363459,-0.861678,-5.641657,-5.729529,-5.996004,1.361410,6.188015,-1.620607,-9.204373,5.906261,-8.549585,-4.119266,9.430575,-0.608794,7.591570,-9.946349,1.483819,7.746662,5.340540,6.356334,-8.997440,-4.810284,-8.196194,-5.651377,6.525613,6.053292,8.164470,-0.256367,6.292944,-8.373862,4.382090,-5.095128,4.278516,-8.618959,7.758892,2.282991,-1.371902,7.239429,-1.420317,6.468521,0.282777,5.995542,4.790273,-5.158450,-1.647004,5.595374,8.219394,6.835211,-6.529315,-5.330335,3.558018,9.365035,2.589179,-4.952070,-5.484911,5.103399,-5.316158,7.647641,1.318791,-5.353228,-1.833667,8.719803,6.174864,9.860314,0.744488,7.333294,6.616582,-3.794508,-0.574051,-4.529898,6.225244,-3.046487,2.803531,6.650287,6.648056,-4.048258,4.464056,-9.113488,-1.141010,-2.924753,8.561525,-4.587363,-2.266416,8.444437,2.245341,-2.557173,7.234562,5.923954,-4.059329,9.563925,-4.149227,2.139912,-9.548504,4.477507,2.193816,-3.145555,3.411823,1.155619,6.971001,-0.827111,1.387883,1.207190,-5.013922,0.242671,4.105211,-4.871225,-4.257488,-4.549116,4.012048,-7.695528,5.945213,7.728415,7.124312,8.344739,3.149257,-2.390934,-1.378200,-8.318701,-7.922720,5.540849,-2.939166,3.418916,6.969321,0.312683,8.341536,-7.845798,-1.509281,-2.365866,-7.836360,2.737747,1.565449,-1.732836,6.932184,-5.961107,-4.320565,-1.515158,-8.989312,-3.428719,3.597357,-2.163070,4.507896,9.218204,4.543003,2.434210,5.081073,4.456878,-9.004013,-2.051145,-7.629069,3.726486,-4.706627,-6.582391,-9.022848,3.520922,-6.506982,-3.154979,-8.931678,-3.389586,0.434086,2.955842,-7.006173,-3.359404,0.269871,-6.900947,8.854811,-1.995721,3.112769,-2.242547,3.154835,6.918760,-8.512234,8.933886,-7.076442,-1.600044,-2.473514,-8.774022,-0.637647,3.494881,-2.722916,-5.486871,-8.136924,0.832481,3.230353,6.740479,9.542643,-8.294050,-2.459534,-9.959252,5.017447,8.087333,8.171161,-4.661603,-8.400888,0.203157,-6.652392,-0.338020,-0.471188,-1.672183,-6.664428,8.325311,0.328709,0.016096,7.205195,-6.324746,-2.197689,-1.321963,2.715930,0.358091,8.271428,-9.560577,-4.881892,-2.151522,6.020804,-5.286657,-7.768538,4.121697,-5.992891,0.152388,8.477282,-9.635373,0.909270,7.138970,-9.846734,-1.181543,5.891293,0.211449,-9.823247,-9.176465,-4.427936,9.896349,-6.788999,-3.047784,6.318287,8.389056,2.975437,-6.222004,-2.296640,-4.604329,-4.495324,-0.606314,2.161143,-2.847458,5.064826,4.104911,4.515582,-6.661979,-0.985752,-6.542357,7.714582,-7.349645,-5.317962,5.279436,-0.133627,7.106176,2.998214,-4.091047,0.902158,-4.726035,7.657186,-6.934007,-4.360906,0.774399,-2.563883,-6.521134,2.949861,-4.855250,6.334139,-1.478096,9.339461,-7.290777,-4.576581,-2.458934,1.941501,-4.107661,-4.347955,-8.766376,-5.257273,2.883081,0.269132,-5.754272,-3.658452,-9.636212,-5.666785,4.040797,-4.685155,-4.426684,-6.059853,-9.010988,7.554219,5.825698,-7.240644,-4.614621,4.445679,1.812579,4.532284,8.441499,-8.093582,1.268250,-0.818957,1.441376,2.541696,2.731813,-5.327833,2.171398,5.087621,0.720056,-1.470282,-7.287259,-5.149473,8.520850,5.231565,5.184322,-2.932804,-9.960058,-4.344403,-1.249990,-8.739909,8.513861,6.816985,-2.447078,3.003719,-3.586156,-7.879712,5.514832,-5.249089,-4.524703,1.908959,-0.095176,2.454634,5.314103,-7.302309,3.949500,1.435534,6.760114,3.806767,0.267785,6.472419,9.054737,-6.515542,-8.776526,1.608056,-6.301940,0.845762,-1.111802,-6.936806,-7.479351,1.010781,7.017704,-6.511785,-1.727327,-6.887340,4.369839,5.540141,5.293558,7.685561,6.804308,5.760179,-7.544541,-9.830967,2.654233,-4.753444,8.884741,1.776561,-7.503754,0.416421,0.368927,2.004697,1.671158,1.747433,-3.391613,0.964948,7.837720,-3.716822,3.219925,0.702458,4.544329,-6.379502,3.021148,7.551197,2.208986,-1.439432,-5.370264,4.306245,7.617376,9.163801,-4.798551,4.481504,0.689680,6.185939,-2.739639,7.023266,-6.257833,-1.880208,2.581251,3.932665,-7.927163,8.436206,6.772423,-8.881379,-7.703695,7.339716,-5.785151,-6.279720,-0.818749,-9.540918,-3.887571,-2.422048,0.174481,8.099619,-8.419894,-8.677501,-7.469256,8.877700,-7.292025,-6.459187,4.862186,3.004105,-8.981765,3.134064,1.427607,9.789272,1.273994,-3.660999,-0.785337,9.096130,0.785646,7.573299,-2.816972,1.264403,2.660973,9.408851,5.566733,-5.133594,-9.165343,-1.464151,-3.671943,-9.344069,1.275785,-8.861237,-7.447219,-4.901532,1.495579,2.971176,6.988907,7.287418,5.633878,0.819387,6.533231,-2.166359,-5.893388,-6.363638,1.282973,-2.143654,2.433065,-1.263053,1.302644,7.304596,9.335948,-1.758013,-8.350502,5.981834,-0.864776,-9.142080,-6.415122,3.988564,-0.611544,8.535655,-4.825285,-1.572380,7.730086,7.202184,-6.987342,0.847297,-3.884447,-2.789083,8.288765,-8.046693,-9.428272,-4.099740,1.494657,3.752970,0.289919,0.171585,0.802015,7.421500,0.698659,4.759780,-8.063359,7.730564,-0.147599,2.556175,8.874360,1.603608,-2.454985,-4.981216,0.609161,3.843189,5.056913,5.506568,1.232367,4.201397,9.617152,-4.093353,7.780616,-7.101453,6.804098,-9.356583,3.747743,-0.525086,3.100944,-8.319188,0.076022,2.406275,-2.879402,4.138065,0.822269,-7.840301,0.487857,-0.891942,-2.639292,-6.765146,-5.648563,-9.078204,-2.207634,-7.109309,-9.798488,-0.002220,-4.374965,-6.309296,-4.393445,-4.463709,-5.086660,3.983665,3.622548,-5.180987,-1.144182,8.348759,0.039852,8.835767,1.581008,0.498342,-2.783515,2.669715,5.610996,4.306845,2.338535,-2.154024,1.619624,2.525973,0.606378,-0.537091,-6.294295,9.227400,-0.621399,5.291295,-1.624832,2.137526,-9.228918,0.608248,-0.797477,-2.135414,8.455363,9.365190,-4.755004,2.582375,-6.219180,1.073009,-0.387757,7.043388,3.204126,-0.089096], dtype = "float64")#candidate|8605|(1080,)|const|float64
call_8602 = relay.TupleGetItem(func_5363_call(relay.reshape(var_8603.astype('uint64'), [1, 8, 9]), relay.reshape(var_8604.astype('uint64'), [4, 8, 9]), relay.reshape(const_8605.astype('float64'), [1080,]), ), 1)
call_8606 = relay.TupleGetItem(func_5367_call(relay.reshape(var_8603.astype('uint64'), [1, 8, 9]), relay.reshape(var_8604.astype('uint64'), [4, 8, 9]), relay.reshape(const_8605.astype('float64'), [1080,]), ), 1)
func_7342_call = mod.get_global_var('func_7342')
func_7344_call = mutated_mod.get_global_var('func_7344')
call_8623 = relay.TupleGetItem(func_7342_call(), 0)
call_8624 = relay.TupleGetItem(func_7344_call(), 0)
bop_8639 = relay.right_shift(call_8623.astype('int64'), relay.reshape(call_8587.astype('int64'), relay.shape_of(call_8623))) # shape=(9, 2, 6)
bop_8642 = relay.right_shift(call_8624.astype('int64'), relay.reshape(call_8588.astype('int64'), relay.shape_of(call_8624))) # shape=(9, 2, 6)
func_7420_call = mod.get_global_var('func_7420')
func_7422_call = mutated_mod.get_global_var('func_7422')
var_8645 = relay.var("var_8645", dtype = "float64", shape = (224,))#candidate|8645|(224,)|var|float64
call_8644 = relay.TupleGetItem(func_7420_call(relay.reshape(var_8645.astype('float64'), [224,])), 6)
call_8646 = relay.TupleGetItem(func_7422_call(relay.reshape(var_8645.astype('float64'), [224,])), 6)
uop_8655 = relay.sqrt(var_8603.astype('float32')) # shape=(72,)
func_4229_call = mod.get_global_var('func_4229')
func_4232_call = mutated_mod.get_global_var('func_4232')
const_8665 = relay.const([[-0.005123],[9.742307],[-7.195870],[-5.523582],[-2.982956],[-5.231194],[8.041973],[7.797029],[9.409893],[3.667423],[4.195877],[1.453652],[6.318943],[6.153802],[-9.678797],[8.951508],[-3.828359],[-9.100673],[-3.986817],[-7.231324],[4.602705],[7.823930],[-5.107606],[0.251094],[-9.797722],[3.889979],[-9.495986],[6.453619],[3.630099],[5.165985],[-5.923922],[9.416272],[7.061397]], dtype = "float64")#candidate|8665|(33, 1)|const|float64
call_8664 = relay.TupleGetItem(func_4229_call(relay.reshape(const_8665.astype('float64'), [1, 11, 3])), 1)
call_8666 = relay.TupleGetItem(func_4232_call(relay.reshape(const_8665.astype('float64'), [1, 11, 3])), 1)
output = relay.Tuple([call_8602,var_8604,const_8605,bop_8639,call_8644,var_8645,uop_8655,call_8664,const_8665,])
output2 = relay.Tuple([call_8606,var_8604,const_8605,bop_8642,call_8646,var_8645,uop_8655,call_8666,const_8665,])
func_8668 = relay.Function([var_8603,var_8604,var_8645,], output)
mod['func_8668'] = func_8668
mod = relay.transform.InferType()(mod)
var_8669 = relay.var("var_8669", dtype = "uint64", shape = (72,))#candidate|8669|(72,)|var|uint64
var_8670 = relay.var("var_8670", dtype = "uint64", shape = (288,))#candidate|8670|(288,)|var|uint64
var_8671 = relay.var("var_8671", dtype = "float64", shape = (224,))#candidate|8671|(224,)|var|float64
output = func_8668(var_8669,var_8670,var_8671,)
func_8672 = relay.Function([var_8669,var_8670,var_8671,], output)
mutated_mod['func_8672'] = func_8672
mutated_mod = relay.transform.InferType()(mutated_mod)
const_8693 = relay.const([[[5.188716,-6.133390,-5.198425],[4.762909,-4.571373,5.851764],[5.527364,-7.767193,0.749517],[-9.239114,1.394104,8.132219],[-0.381484,7.349779,8.869499],[4.325942,-1.217098,-7.302182],[1.759889,9.307260,-1.444599],[-5.282050,0.710484,3.726636],[5.740980,3.620000,-2.625434],[4.424580,-6.357560,-1.319600],[-7.490705,3.699506,3.820254],[1.854934,6.953455,-4.092980],[1.240403,1.079112,7.532904],[2.349909,-6.216111,5.978114]],[[0.226313,7.983397,9.734058],[4.628356,3.536491,-4.580316],[-5.274546,9.100238,-4.104249],[2.087938,5.186860,-6.667896],[7.965612,9.360960,-3.252742],[-2.549174,-6.336141,-5.010148],[9.393555,5.519848,-1.460765],[-9.704350,4.589591,-0.687984],[3.993021,3.209491,-0.245729],[-8.209949,2.319139,1.771644],[-5.619348,-5.352310,8.346685],[0.120248,-9.838593,5.513761],[-6.410351,-9.957334,-6.557306],[-2.292194,-5.933835,-1.565727]],[[4.489200,1.690795,-5.245523],[5.212187,-0.687764,2.928419],[-4.902598,4.148316,0.788555],[4.223852,-8.010219,1.098164],[-4.923803,-3.086615,5.313025],[0.826033,8.191788,-9.710947],[1.173777,4.389169,6.768114],[9.775243,7.120688,-3.098516],[9.251739,-1.545835,4.918129],[-5.220262,4.639638,2.845274],[7.219752,-1.235144,2.675142],[9.944431,-5.676417,-1.967525],[6.972592,6.430758,-4.348774],[-1.233369,6.373798,7.423095]],[[-2.511225,-5.861641,0.850824],[1.994698,-6.639761,0.106794],[-4.252551,-9.856743,2.904191],[-0.981192,-2.191609,8.039439],[5.930189,-2.259870,2.385453],[-4.971677,-4.507306,1.593846],[-0.138241,-8.288895,-0.762446],[-7.437510,-6.673481,0.356173],[6.773915,1.152262,8.745699],[4.777146,-5.547535,3.763380],[1.653739,1.286895,-1.121417],[4.783485,9.870412,9.937316],[-7.987500,-6.264964,-7.081098],[-3.244357,9.585845,3.598852]],[[9.520018,-9.644897,8.414370],[4.856871,7.003209,-1.111878],[1.724662,-6.195946,9.826624],[9.125622,7.786354,4.953045],[1.277264,9.799550,1.807980],[-5.623588,9.298151,-5.265602],[-0.717625,-7.918738,-0.981579],[-3.559782,-5.401340,9.470742],[-4.244439,0.584516,-1.553613],[-7.947354,5.099903,1.814211],[-0.402627,6.511326,-6.535402],[-8.601709,0.272467,-1.560915],[7.746077,4.202168,6.392900],[-2.920726,0.863482,7.340053]]], dtype = "float64")#candidate|8693|(5, 14, 3)|const|float64
uop_8694 = relay.sigmoid(const_8693.astype('float64')) # shape=(5, 14, 3)
bop_8697 = relay.bitwise_or(uop_8694.astype('uint32'), relay.reshape(const_8693.astype('uint32'), relay.shape_of(uop_8694))) # shape=(5, 14, 3)
output = relay.Tuple([bop_8697,])
output2 = relay.Tuple([bop_8697,])
func_8704 = relay.Function([], output)
mod['func_8704'] = func_8704
mod = relay.transform.InferType()(mod)
mutated_mod['func_8704'] = func_8704
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8704_call = mutated_mod.get_global_var('func_8704')
call_8705 = func_8704_call()
output = call_8705
func_8706 = relay.Function([], output)
mutated_mod['func_8706'] = func_8706
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7350_call = mod.get_global_var('func_7350')
func_7352_call = mutated_mod.get_global_var('func_7352')
call_8707 = func_7350_call()
call_8708 = func_7350_call()
uop_8724 = relay.erf(call_8707.astype('float32')) # shape=(9, 2, 6)
uop_8726 = relay.erf(call_8708.astype('float32')) # shape=(9, 2, 6)
output = relay.Tuple([uop_8724,])
output2 = relay.Tuple([uop_8726,])
func_8730 = relay.Function([], output)
mod['func_8730'] = func_8730
mod = relay.transform.InferType()(mod)
output = func_8730()
func_8731 = relay.Function([], output)
mutated_mod['func_8731'] = func_8731
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7447_call = mod.get_global_var('func_7447')
func_7448_call = mutated_mod.get_global_var('func_7448')
call_8735 = func_7447_call()
call_8736 = func_7447_call()
var_8739 = relay.var("var_8739", dtype = "float64", shape = (9, 2, 6))#candidate|8739|(9, 2, 6)|var|float64
bop_8740 = relay.logical_xor(call_8735.astype('uint32'), relay.reshape(var_8739.astype('uint32'), relay.shape_of(call_8735))) # shape=(9, 2, 6)
bop_8743 = relay.logical_xor(call_8736.astype('uint32'), relay.reshape(var_8739.astype('uint32'), relay.shape_of(call_8736))) # shape=(9, 2, 6)
func_6694_call = mod.get_global_var('func_6694')
func_6698_call = mutated_mod.get_global_var('func_6698')
var_8745 = relay.var("var_8745", dtype = "int64", shape = (225,))#candidate|8745|(225,)|var|int64
call_8744 = func_6694_call(relay.reshape(var_8745.astype('int64'), [5, 3, 15]), relay.reshape(var_8745.astype('int64'), [5, 3, 15]), )
call_8746 = func_6694_call(relay.reshape(var_8745.astype('int64'), [5, 3, 15]), relay.reshape(var_8745.astype('int64'), [5, 3, 15]), )
uop_8749 = relay.sigmoid(var_8745.astype('float32')) # shape=(225,)
func_6909_call = mod.get_global_var('func_6909')
func_6910_call = mutated_mod.get_global_var('func_6910')
call_8772 = relay.TupleGetItem(func_6909_call(), 1)
call_8773 = relay.TupleGetItem(func_6910_call(), 1)
output = relay.Tuple([bop_8740,call_8744,uop_8749,call_8772,])
output2 = relay.Tuple([bop_8743,call_8746,uop_8749,call_8773,])
func_8775 = relay.Function([var_8739,var_8745,], output)
mod['func_8775'] = func_8775
mod = relay.transform.InferType()(mod)
mutated_mod['func_8775'] = func_8775
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8775_call = mutated_mod.get_global_var('func_8775')
var_8777 = relay.var("var_8777", dtype = "float64", shape = (9, 2, 6))#candidate|8777|(9, 2, 6)|var|float64
var_8778 = relay.var("var_8778", dtype = "int64", shape = (225,))#candidate|8778|(225,)|var|int64
call_8776 = func_8775_call(var_8777,var_8778,)
output = call_8776
func_8779 = relay.Function([var_8777,var_8778,], output)
mutated_mod['func_8779'] = func_8779
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8513_call = mod.get_global_var('func_8513')
func_8515_call = mutated_mod.get_global_var('func_8515')
call_8904 = func_8513_call()
call_8905 = func_8513_call()
func_7187_call = mod.get_global_var('func_7187')
func_7191_call = mutated_mod.get_global_var('func_7191')
var_8912 = relay.var("var_8912", dtype = "int16", shape = (882,))#candidate|8912|(882,)|var|int16
call_8911 = relay.TupleGetItem(func_7187_call(relay.reshape(var_8912.astype('int16'), [7, 14, 9]), relay.reshape(var_8912.astype('int16'), [7, 14, 9]), relay.reshape(call_8904.astype('int64'), [1260,]), ), 2)
call_8913 = relay.TupleGetItem(func_7191_call(relay.reshape(var_8912.astype('int16'), [7, 14, 9]), relay.reshape(var_8912.astype('int16'), [7, 14, 9]), relay.reshape(call_8904.astype('int64'), [1260,]), ), 2)
uop_8914 = relay.sigmoid(call_8904.astype('float32')) # shape=(10, 14, 9)
uop_8916 = relay.sigmoid(call_8905.astype('float32')) # shape=(10, 14, 9)
func_8123_call = mod.get_global_var('func_8123')
func_8128_call = mutated_mod.get_global_var('func_8128')
const_8918 = relay.const([4,-9,9,8,-8,-7,7,2,8,3,-2,-8,-2,-4,-10,2,-8,-8,2,-4,-10,-5,6,-3,9,4,-6,2,1,-3,-8,-6,-7,-5,4,-1,-8,-1,4,-3,-1,-4,9,-5,3,5,4,-8,-8,1,-10,-6,9,-7,3,-7,6,1,7,-8,-3,-2,6,7,-2,-6,1,3,1,-4,-9,-1,2,2,8,-2,5,-10,-5,-5,-5,9,4,5,-5,2,-8,1,-6,9,-5,7,-6,-8,-3,-8,-5,4,1,7,-8,2,-3,-6,-5,3,8,9,4,-5,-2,7,1,9,1,-10,4,-5,-4,-5,7,-9,5,-1,7,8,-8,-7,8,-3,-1,-8,-4,1,5,6,-2,-7,5,8,3,-1,2,-1,3,9,-4,8,-1,5,5,-8,-8,-5,-10,-3,10,-5,2,-3,10,9,-9,2,-8,-8,8,-3,8,9,3,-2,-8,5,10,6,-8,-4,4,10], dtype = "int32")#candidate|8918|(180,)|const|int32
const_8919 = relay.const([[3.131574,-9.555589,3.849576,-1.015375],[-8.389675,1.907533,-0.425059,-9.732884],[-1.965042,8.475061,-6.977716,1.608955],[-1.088036,-0.538495,4.302486,-1.115233],[7.773566,-5.088173,-0.120263,-9.290879],[-0.253490,9.740090,0.380974,3.740740],[4.695409,-7.639757,1.345057,1.751212],[3.834911,-1.127220,-1.466770,5.280107],[8.292411,-8.927895,8.501083,-2.909487],[-8.145604,-6.882652,-7.366003,3.308285],[6.302340,6.613628,9.483381,-5.810965],[-9.663894,1.884963,2.762651,-4.486818],[9.577078,1.645107,4.476013,-6.292560],[8.261159,5.803893,-4.921489,-7.304741],[4.767640,-9.473443,-7.886898,0.179463],[9.246194,9.974122,6.614917,8.768053],[-7.572109,3.626369,-3.639739,8.968105],[0.459069,2.473600,-7.803843,1.283183],[2.214407,-4.419091,-2.359672,6.223912],[6.897787,0.744730,-6.379488,5.478555],[2.540867,9.015045,-2.499055,6.566639],[6.142048,9.787626,-4.462632,1.035102],[-6.085184,6.834062,4.972960,-3.760400],[0.784615,-2.881002,-8.746095,-6.240105],[-9.461745,1.340191,6.116470,-0.571452],[-0.994189,-8.433172,-1.373242,-2.107608],[1.439294,-9.442028,-1.227542,7.511591],[-7.138588,-6.401958,5.438777,-7.419880],[-3.247699,-6.961902,-0.457919,-2.494012],[-2.297942,-9.361530,5.838411,9.504595],[-6.266988,6.795377,-9.722567,2.578426],[-0.378949,6.494304,-0.643894,-0.657936]], dtype = "float32")#candidate|8919|(32, 4)|const|float32
var_8920 = relay.var("var_8920", dtype = "float64", shape = (160,))#candidate|8920|(160,)|var|float64
call_8917 = relay.TupleGetItem(func_8123_call(relay.reshape(const_8918.astype('int32'), [30, 6]), relay.reshape(var_8912.astype('float32'), [882,]), relay.reshape(const_8919.astype('float32'), [8, 16]), relay.reshape(var_8920.astype('float64'), [160,]), ), 11)
call_8921 = relay.TupleGetItem(func_8128_call(relay.reshape(const_8918.astype('int32'), [30, 6]), relay.reshape(var_8912.astype('float32'), [882,]), relay.reshape(const_8919.astype('float32'), [8, 16]), relay.reshape(var_8920.astype('float64'), [160,]), ), 11)
output = relay.Tuple([call_8911,var_8912,uop_8914,call_8917,const_8918,const_8919,var_8920,])
output2 = relay.Tuple([call_8913,var_8912,uop_8916,call_8921,const_8918,const_8919,var_8920,])
func_8939 = relay.Function([var_8912,var_8920,], output)
mod['func_8939'] = func_8939
mod = relay.transform.InferType()(mod)
mutated_mod['func_8939'] = func_8939
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8939_call = mutated_mod.get_global_var('func_8939')
var_8941 = relay.var("var_8941", dtype = "int16", shape = (882,))#candidate|8941|(882,)|var|int16
var_8942 = relay.var("var_8942", dtype = "float64", shape = (160,))#candidate|8942|(160,)|var|float64
call_8940 = func_8939_call(var_8941,var_8942,)
output = call_8940
func_8943 = relay.Function([var_8941,var_8942,], output)
mutated_mod['func_8943'] = func_8943
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5978_call = mod.get_global_var('func_5978')
func_5979_call = mutated_mod.get_global_var('func_5979')
call_8947 = func_5978_call()
call_8948 = func_5978_call()
func_8174_call = mod.get_global_var('func_8174')
func_8175_call = mutated_mod.get_global_var('func_8175')
call_8951 = relay.TupleGetItem(func_8174_call(), 0)
call_8952 = relay.TupleGetItem(func_8175_call(), 0)
output = relay.Tuple([call_8947,call_8951,])
output2 = relay.Tuple([call_8948,call_8952,])
func_8964 = relay.Function([], output)
mod['func_8964'] = func_8964
mod = relay.transform.InferType()(mod)
mutated_mod['func_8964'] = func_8964
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8964_call = mutated_mod.get_global_var('func_8964')
call_8965 = func_8964_call()
output = call_8965
func_8966 = relay.Function([], output)
mutated_mod['func_8966'] = func_8966
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7075_call = mod.get_global_var('func_7075')
func_7076_call = mutated_mod.get_global_var('func_7076')
call_8970 = relay.TupleGetItem(func_7075_call(), 0)
call_8971 = relay.TupleGetItem(func_7076_call(), 0)
func_7420_call = mod.get_global_var('func_7420')
func_7422_call = mutated_mod.get_global_var('func_7422')
var_8986 = relay.var("var_8986", dtype = "float64", shape = (8, 28))#candidate|8986|(8, 28)|var|float64
call_8985 = relay.TupleGetItem(func_7420_call(relay.reshape(var_8986.astype('float64'), [224,])), 6)
call_8987 = relay.TupleGetItem(func_7422_call(relay.reshape(var_8986.astype('float64'), [224,])), 6)
var_8989 = relay.var("var_8989", dtype = "float32", shape = (40, 12))#candidate|8989|(40, 12)|var|float32
bop_8990 = relay.not_equal(call_8985.astype('bool'), relay.reshape(var_8989.astype('bool'), relay.shape_of(call_8985))) # shape=(40, 12)
bop_8993 = relay.not_equal(call_8987.astype('bool'), relay.reshape(var_8989.astype('bool'), relay.shape_of(call_8987))) # shape=(40, 12)
output = relay.Tuple([call_8970,var_8986,bop_8990,])
output2 = relay.Tuple([call_8971,var_8986,bop_8993,])
func_8999 = relay.Function([var_8986,var_8989,], output)
mod['func_8999'] = func_8999
mod = relay.transform.InferType()(mod)
var_9000 = relay.var("var_9000", dtype = "float64", shape = (8, 28))#candidate|9000|(8, 28)|var|float64
var_9001 = relay.var("var_9001", dtype = "float32", shape = (40, 12))#candidate|9001|(40, 12)|var|float32
output = func_8999(var_9000,var_9001,)
func_9002 = relay.Function([var_9000,var_9001,], output)
mutated_mod['func_9002'] = func_9002
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7837_call = mod.get_global_var('func_7837')
func_7838_call = mutated_mod.get_global_var('func_7838')
call_9012 = relay.TupleGetItem(func_7837_call(), 0)
call_9013 = relay.TupleGetItem(func_7838_call(), 0)
func_8442_call = mod.get_global_var('func_8442')
func_8443_call = mutated_mod.get_global_var('func_8443')
call_9015 = relay.TupleGetItem(func_8442_call(), 0)
call_9016 = relay.TupleGetItem(func_8443_call(), 0)
output = relay.Tuple([call_9012,call_9015,])
output2 = relay.Tuple([call_9013,call_9016,])
func_9024 = relay.Function([], output)
mod['func_9024'] = func_9024
mod = relay.transform.InferType()(mod)
mutated_mod['func_9024'] = func_9024
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9024_call = mutated_mod.get_global_var('func_9024')
call_9025 = func_9024_call()
output = call_9025
func_9026 = relay.Function([], output)
mutated_mod['func_9026'] = func_9026
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8400_call = mod.get_global_var('func_8400')
func_8402_call = mutated_mod.get_global_var('func_8402')
call_9197 = relay.TupleGetItem(func_8400_call(), 0)
call_9198 = relay.TupleGetItem(func_8402_call(), 0)
output = relay.Tuple([call_9197,])
output2 = relay.Tuple([call_9198,])
func_9199 = relay.Function([], output)
mod['func_9199'] = func_9199
mod = relay.transform.InferType()(mod)
mutated_mod['func_9199'] = func_9199
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9199_call = mutated_mod.get_global_var('func_9199')
call_9200 = func_9199_call()
output = call_9200
func_9201 = relay.Function([], output)
mutated_mod['func_9201'] = func_9201
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9224 = relay.var("var_9224", dtype = "float64", shape = (9, 12, 4))#candidate|9224|(9, 12, 4)|var|float64
uop_9225 = relay.asinh(var_9224.astype('float64')) # shape=(9, 12, 4)
func_8964_call = mod.get_global_var('func_8964')
func_8966_call = mutated_mod.get_global_var('func_8966')
call_9238 = relay.TupleGetItem(func_8964_call(), 0)
call_9239 = relay.TupleGetItem(func_8966_call(), 0)
uop_9240 = relay.log10(uop_9225.astype('float64')) # shape=(9, 12, 4)
func_8775_call = mod.get_global_var('func_8775')
func_8779_call = mutated_mod.get_global_var('func_8779')
const_9247 = relay.const([[5,-6,-6],[8,3,9],[1,-10,5],[2,-8,-7],[4,-3,-10],[-9,-4,-10],[2,-6,-5],[1,-1,4],[-3,-5,-1],[-10,-10,4],[-10,5,-9],[-4,-4,-8],[-7,6,7],[6,-8,-5],[-3,4,7],[-5,2,-1],[-4,2,7],[-10,6,-4],[8,7,1],[5,-6,-9],[-6,10,-4],[-8,7,-10],[-7,-3,-6],[8,-7,10],[-4,3,-1],[-2,7,-6],[6,1,2],[-10,-2,4],[9,4,4],[5,-6,-7],[-1,7,-5],[-8,6,4],[1,-9,-8],[10,2,5],[-7,-3,9],[1,2,-7],[-10,-8,4],[-4,-10,7],[3,-7,-3],[-10,-5,3],[-4,-3,2],[-3,-4,-9],[-7,-5,-6],[-4,2,-6],[6,-3,-1],[-6,-1,-1],[-10,5,7],[4,7,-10],[-4,5,-8],[8,7,6],[8,-2,2],[1,-8,-5],[2,-9,-1],[-3,-3,-8],[9,4,9],[-3,3,-9],[-9,-4,9],[-1,1,10],[-7,6,3],[-1,-1,-8],[7,1,-7],[5,-9,2],[-8,-8,1],[2,5,9],[1,-10,-5],[3,10,-1],[2,-4,3],[-2,-6,-4],[10,-8,2],[-1,-5,3],[9,-1,-2],[7,-6,-7],[-6,-4,9],[3,1,-4],[-7,4,-6]], dtype = "int64")#candidate|9247|(75, 3)|const|int64
call_9246 = relay.TupleGetItem(func_8775_call(relay.reshape(call_9238.astype('float64'), [9, 2, 6]), relay.reshape(const_9247.astype('int64'), [225,]), ), 1)
call_9248 = relay.TupleGetItem(func_8779_call(relay.reshape(call_9238.astype('float64'), [9, 2, 6]), relay.reshape(const_9247.astype('int64'), [225,]), ), 1)
uop_9251 = relay.sigmoid(uop_9225.astype('float64')) # shape=(9, 12, 4)
output = relay.Tuple([call_9238,uop_9240,call_9246,const_9247,uop_9251,])
output2 = relay.Tuple([call_9239,uop_9240,call_9248,const_9247,uop_9251,])
func_9258 = relay.Function([var_9224,], output)
mod['func_9258'] = func_9258
mod = relay.transform.InferType()(mod)
mutated_mod['func_9258'] = func_9258
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9259 = relay.var("var_9259", dtype = "float64", shape = (9, 12, 4))#candidate|9259|(9, 12, 4)|var|float64
func_9258_call = mutated_mod.get_global_var('func_9258')
call_9260 = func_9258_call(var_9259)
output = call_9260
func_9261 = relay.Function([var_9259], output)
mutated_mod['func_9261'] = func_9261
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7837_call = mod.get_global_var('func_7837')
func_7838_call = mutated_mod.get_global_var('func_7838')
call_9297 = relay.TupleGetItem(func_7837_call(), 2)
call_9298 = relay.TupleGetItem(func_7838_call(), 2)
output = relay.Tuple([call_9297,])
output2 = relay.Tuple([call_9298,])
func_9301 = relay.Function([], output)
mod['func_9301'] = func_9301
mod = relay.transform.InferType()(mod)
mutated_mod['func_9301'] = func_9301
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9301_call = mutated_mod.get_global_var('func_9301')
call_9302 = func_9301_call()
output = call_9302
func_9303 = relay.Function([], output)
mutated_mod['func_9303'] = func_9303
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6909_call = mod.get_global_var('func_6909')
func_6910_call = mutated_mod.get_global_var('func_6910')
call_9336 = relay.TupleGetItem(func_6909_call(), 1)
call_9337 = relay.TupleGetItem(func_6910_call(), 1)
func_8668_call = mod.get_global_var('func_8668')
func_8672_call = mutated_mod.get_global_var('func_8672')
const_9346 = relay.const([[-7,-2,4,-1,6,-2,-9,-8,8,9,-10,5],[5,-6,-9,10,1,6,-9,-10,-8,10,3,-8],[-7,-10,-3,-2,-4,9,3,1,5,-1,4,-9],[-2,-2,6,7,-9,4,-1,10,5,9,1,3],[-7,10,4,6,2,-2,-1,4,7,10,4,-5],[9,8,6,-8,6,6,1,7,-1,-2,9,2]], dtype = "uint64")#candidate|9346|(6, 12)|const|uint64
const_9347 = relay.const([3,-4,-8,-2,5,-8,1,-4,5,9,9,-2,-4,-8,-4,-8,2,-5,5,7,-7,4,10,-7,1,6,9,2,6,8,3,-8,8,-5,5,4,8,2,-3,-10,6,-6,-3,-8,8,-10,-4,8,-6,-8,7,-2,7,3,-6,8,-9,7,-3,-3,-3,-6,3,-2,6,-9,1,10,-7,9,5,5,2,-8,-1,9,-5,-2,8,-7,-3,9,-8,-1,9,-10,9,-8,1,7,-6,5,-1,10,-10,-4,-3,-6,-4,-10,7,7,9,-7,3,10,2,3,-2,-3,-1,-7,1,-9,-10,-8,-1,5,4,10,-7,9,8,3,6,-4,2,-3,-3,-10,1,10,-4,-2,6,-6,-2,2,-8,10,10,10,5,5,-6,-3,-4,1,-7,-6,4,-7,8,8,4,-1,2,-6,-7,-7,7,-3,2,-9,-8,-3,9,-1,-1,5,5,-2,9,5,3,10,1,-1,7,1,8,-8,-6,-6,-5,6,8,10,8,-3,7,-10,-7,1,-2,-7,-8,7,-1,-3,-5,8,-9,-3,4,-5,-9,1,-8,8,-5,-2,2,-9,4,1,2,-5,10,5,3,-6,7,-8,10,-6,-5,-9,10,9,-1,3,10,4,7,-5,-3,5,-10,6,-1,6,1,-10,-5,-4,9,-10,9,-10,-5,-7,8,8,-4,-8,9,10,1,-2,9,3,-5,-9,-8,9,6,2,9,-1,-8,-10,5,6,10,-10,-4,-8,-5,1,4,7,-9,3,2,-3,-5,5], dtype = "uint64")#candidate|9347|(288,)|const|uint64
var_9348 = relay.var("var_9348", dtype = "float64", shape = (224,))#candidate|9348|(224,)|var|float64
call_9345 = relay.TupleGetItem(func_8668_call(relay.reshape(const_9346.astype('uint64'), [72,]), relay.reshape(const_9347.astype('uint64'), [288,]), relay.reshape(var_9348.astype('float64'), [224,]), ), 6)
call_9349 = relay.TupleGetItem(func_8672_call(relay.reshape(const_9346.astype('uint64'), [72,]), relay.reshape(const_9347.astype('uint64'), [288,]), relay.reshape(var_9348.astype('float64'), [224,]), ), 6)
func_5096_call = mod.get_global_var('func_5096')
func_5100_call = mutated_mod.get_global_var('func_5100')
var_9355 = relay.var("var_9355", dtype = "float64", shape = (8, 20))#candidate|9355|(8, 20)|var|float64
const_9356 = relay.const([8.833213,7.047578,-5.594201,4.835659,-8.509866,2.817457,4.030932,3.169247,8.528058,8.225048,-1.303205,0.056359,-8.984706,-1.033566,-7.579738,-9.753543,7.192333,-1.662403,4.774100,7.049152,-8.185475,0.795985,-7.349019,9.343250,-3.034213,-0.179286,4.724733,4.875387,-3.701559,3.425809,-9.570843,4.984460,2.663758,6.743609,7.162118,-1.429298,6.215256,-4.337135,7.733984,6.196719,-9.343228,-2.133612,-7.709781,2.140941,-4.863958,3.713360,-7.420387,-9.875191,-7.111262,4.425282,2.927661,3.446995,2.540430,-4.472643,1.506218,-9.566925,0.135327,6.157541,-7.099117,-8.843853,-1.704477,3.507843,-0.542364,-9.586857,-7.566192,9.471689,-5.360750,-6.774927,-8.125031,-2.263466,2.454746,1.352478,0.144189,-0.668567,-3.650775,-7.002949,-3.549840,4.727906,-5.472146,6.566671,0.011606,-7.192678,6.291525,6.998297,4.943881,6.951543,-7.897654,0.400261,-4.240613,-4.243308,-5.812411,7.142616,-3.398485,-3.900038,-2.015161,7.390060,-1.525056,2.728440,9.963452,9.121608,-3.558916,6.251937,1.138124,1.718108,-1.382578,-7.026511,-1.689779,5.266534,7.288305,9.393321,1.390720,5.844281,-2.945811,6.913623,-0.378843,-8.099950,7.555074,9.081625,-3.534823,-5.739809,-0.188239,-5.462001,-0.338962,-3.659567,5.932068,-9.683527,-0.940732,-4.134087,-1.928919,-9.507353,-2.482317,-1.252075,-2.328882,-2.495499,-0.742916,4.058999,-7.985080,9.069566,7.516254,-7.115881,-9.991946,9.065284,-9.813200,7.486366,9.955022,4.151759,2.163710,-7.420172,-5.184877,-0.552879,4.807915,9.019390,5.542697,6.839541,-3.259871,3.864863,-7.946835,-1.535682,-5.123992,9.449552,0.704996,6.996310,-0.843607,1.651774,9.241221,6.415493,6.430490,-9.686209,-6.116592,-9.575132,8.475643,5.766989,-8.895382,-5.087784,2.047938,8.576296,3.793885,7.162886,-8.980149,-0.252190,7.995592,-3.893406,-4.914981,0.992463,-2.494871,-6.290358,-3.329032,9.998526,0.219930,9.663812,-9.227551,9.038974,-2.738525,6.199929,4.384412,-5.417562,-4.829895,-4.414132,7.043061,0.213092,7.373060,9.947038,3.067343,-9.338007,-5.004678,0.585943,-6.542691,-7.267019,-0.056264,9.048131,2.269271,-6.458200,3.862263,1.864275,-6.472834,-8.087355,-2.261119,2.056978,0.109156,-2.215034,-5.811597,-6.308367,-4.838035,9.692772,-2.178316,4.869169,-8.849100,5.132804,-2.243626,-9.448362,6.608588,-8.190304,-7.301784,4.134337,1.180730,4.646297,-2.812612,9.296373,6.949461,4.877137,6.975988,0.018270,-8.542010,8.714153,4.830161,7.774947,2.395519,-1.692267,-7.973643,1.997937,5.192542,2.455117,-3.417229,7.704609,2.621275,8.597500,2.141401,-3.890204,-7.295024,-8.510801,3.923208,-4.282999,5.381853,-4.586284,8.824088,0.153910,-8.709060,-6.105903,1.967219,-4.235000,-3.216442,-2.965980,5.681475,4.462948,-1.256885,8.497691,0.938127,-4.880083,7.394120,-0.492553,-5.759561,1.934545,-2.836197,3.450696,9.355922,-3.426045,-7.904408,1.199986,1.043187,9.086075,-5.780403,9.724535,-5.429787,-2.672277,-1.850251,-6.830309,7.835506,-2.425517,5.655492,8.520585,7.336719,-6.423145,-9.980702,9.091843,-0.762318,-6.537822,-9.692844,4.928289,4.947085,-1.648856,-0.218044,9.309799,-2.912737,-8.727145,5.384785,4.795889,7.402535,-1.683791,0.203522,-1.417711], dtype = "float32")#candidate|9356|(320,)|const|float32
call_9354 = relay.TupleGetItem(func_5096_call(relay.reshape(var_9355.astype('float64'), [8, 4, 5]), relay.reshape(const_9356.astype('float32'), [320,]), ), 4)
call_9357 = relay.TupleGetItem(func_5100_call(relay.reshape(var_9355.astype('float64'), [8, 4, 5]), relay.reshape(const_9356.astype('float32'), [320,]), ), 4)
func_6694_call = mod.get_global_var('func_6694')
func_6698_call = mutated_mod.get_global_var('func_6698')
var_9359 = relay.var("var_9359", dtype = "int64", shape = (75, 3))#candidate|9359|(75, 3)|var|int64
call_9358 = func_6694_call(relay.reshape(var_9359.astype('int64'), [5, 3, 15]), relay.reshape(var_9359.astype('int64'), [5, 3, 15]), )
call_9360 = func_6694_call(relay.reshape(var_9359.astype('int64'), [5, 3, 15]), relay.reshape(var_9359.astype('int64'), [5, 3, 15]), )
func_7018_call = mod.get_global_var('func_7018')
func_7022_call = mutated_mod.get_global_var('func_7022')
const_9370 = relay.const([-2,-4,-9,-6,7,-1,-1,3,7,5,-3,10,-9,9,3,5,-4,-8,9,7,-10,-2,-1,6,1,8,4,-6,-10,4,-8,1,-7,6,-4,2,1,5,-9,2,2,5,-7,8,5,-1,10,-6,10,3,-5,8,-10,-10,5,10,9,5,6,3,7,6,-5,-6,-8,-9,-5,9,-1,4,-10,-7,-2,4,8,-1,1,-6,-2,1,1,-3,6,-2,2,5,2,2,6,10,-5,-1,-8,3,9,-2,-4,1,-8,9,10,-3,-7,4,10,9,7,-2,-7,9,-8,10,-7,-4,-3,6,-8,-4,3,-10,4,-10,9,9,4,-4,8,-4,5,9,-10,9,-5,7,-3,-3,-8,9,5,-5,-6,3,5,9,7,5,-5,9,9,2,-3,-10,-7,8,7,-3,2,-6,-5,-6,5,2,-8,-1,-7,1,-7,-10,-10,-8,-2,9,-9,3,-10,-8,2,4,-1,9], dtype = "int32")#candidate|9370|(180,)|const|int32
var_9371 = relay.var("var_9371", dtype = "uint64", shape = (896,))#candidate|9371|(896,)|var|uint64
const_9372 = relay.const([-10,1,3,-6,-4,-1,10,7,-2,-2,5,4,-10,3,4,-5,4,6,-9,6,-7,-6,-8,-6,8,-5,-3,8,-4,5,8,4,-8,-3,5,10,-4,-1,-9,-5,5,9,-8,5,-5,-2,10,9,8,-5,-1,7,9,-10,-2,-5,-4,7,9,-6,2,-1,3,8,-4,-6,-8,-10,8,-5], dtype = "uint32")#candidate|9372|(70,)|const|uint32
call_9369 = relay.TupleGetItem(func_7018_call(relay.reshape(const_9370.astype('int32'), [180,]), relay.reshape(var_9371.astype('uint64'), [14, 64]), relay.reshape(const_9372.astype('uint32'), [70,]), ), 1)
call_9373 = relay.TupleGetItem(func_7022_call(relay.reshape(const_9370.astype('int32'), [180,]), relay.reshape(var_9371.astype('uint64'), [14, 64]), relay.reshape(const_9372.astype('uint32'), [70,]), ), 1)
func_1580_call = mod.get_global_var('func_1580')
func_1586_call = mutated_mod.get_global_var('func_1586')
const_9375 = relay.const([4,10,2,7,4,-5,-3,7,-2,2,-4,-6,3,1,4,2,2,9,5,9,-7,-6,-1,-10,10,9,-2,-2,8,9,-9,-1,4,-7,7,-10,10,7,-1,-6,-10,-2,9,9,7,-9,-10,9,2,5,-4,6,-3,7,1,-4,8,5,-1,-3,4,-7,2,-10,-4,6,10,-3,-4,-4,2,7,-5,7,5,-4,-2,5,7,-10,10,10,-9,-2,1,-9,-5,5,7,4,2,4,9,9,5,-8,7,-5,-8,1,-3,6,-7,6,5,-9,-9,2,-2,-3,-4,2,-8,-10,-3,8,3,4,7,7,3,10,9,-8,-6,-6,4,4,4,-8,6,5,-2,-9,-10,-10,2,-4,3,-2,5,-9,-7,-8,-6,-9,4,2,-4,4,9,8,-7,2,4,-9,3,7,3,-2,4,3,-5,4,6,-3,4,-8,-4,1,6,7,1,9,1,-5,3,3,-1,-7,-4,3,4,9,2,5,1,7,-8,-6,-8,-6,-6,-8,5,-5,-8,9,10,1,1,1,-10,3,-7,-10,9,5,-2,-4,10,8,-8,3,6,-1,10,8,-2,-1,-2,-3,5,-8,-3,-6,4,3,10,1,10,2,7,1,10,8,10,-5,-1,4,5,-9,3,-10,-9,-8,4,10,-1,-1,-2,-5,2,1,-10,9,4,-4,-1,-7,-5,1,6,-1,4,-8,-8,-1,10,6,-7,-7,3,6,-6,-6,10,10,-1,-3,-10,-1,3,-1,-6,-4,1,1,-3,-10,10,7,5,3,8,-3,6,-9,8,1,4,-6,-7,9,-2,6,-4,1,2,-9,2,1,6,7,7,-9,-3,7,1,-9,-4,-6,-10,2,-3,-4,-1,-2,-4,-4,-7,3,-9,2,-6,-3,-8,1,-6,-1,1,3,-10,-2,2,-5,-10,-8,9,-9,1,-5,2,6,-6,6,-4,-1,4,1,9,6,6,-8,-4,-8,-10,-5,-9,-10,-9,2,7,-8,-5,6,4,-5,6,5,-2,-8,-8,-5,-5,9,1,-5,-5,9,9,5,-9,-6,-6,6,4,2,-8,-6,-4,-5,6,-3,-3,10,2,-9,-8,6,4,1,8,7,-2,9,9,1,5,8,-10,4,-6,1,-6,5,10,7,3,6,-8,-3,10,-2,-10,5,-1,-2,-1,-8,-1,-6,-2,1,-6,3,3,-1,-10,1,5,3,-4,10,9,4,-4,-3,3,4,-2,-3,2,9,9,3,-6,8,3,-7,10,2,-2,-10,8,4,10,-4,-3,4,3,-6,6,-10,3,-9,1,-5,-6,-9,9,-6,-3,1,5,8,3,-10,-7,7,-10,-3,2,5,4,-4,-7,4,-1,8,8,-8,1,3,-8,7,9,-10,-9,8,-1,8,3,10,7,-3,-3,8,-9,-1,1,5,-10,-2,-2,-4,-5,10,4,-5,7,6,9,5,6,4,-6,1,8,6,-6,-2,3,-8,-4,-10,2,-1,3,-8,-4,8,5,-9,-3,-2,5,7,-8,9,-1,-2,-4,-4,1,-5,6,6,-3,4,-9,-4,-10,4,-9,9,1,-2,4,-3,-10,9,-4,-9,7,-6,8,1,-2,-6,-2,-2,6,-2,-2,5,-5,-7,-7,-9,-8,3,4,5,-2,10,6,7,-8,2,5,-1,10,-1,-2,5,5,7,-3,9,1,-9,3,-9,-6,2,-8,10,-9,-9,3,-3,2,-10,-10,10,10,10,-7,8,-2,3,-1,10,-7,-3,10,1,-5,9,-1,9,-8,9,-10,9,5,-1,-8,-8,-9,5,6,3,6,7,1,-1,6,6,-6,7,-8,8,1,-3,9,-10,-4,8,-5,1,2,-4,-1,2,5,9,-10,-3,6,-1,-4,10,4,-1,-3,-4,4,3,8,5,5,-9,2,3,-8,3,-7,-1,2,-1,-4,-2,-3,-6,-8,-6,-4,7,-7,-5,7,6,-4,-5,8,-3,-3,1,-10,8,-7,-3,7,10,-2,-8,5,-3,8,-5,-5,1,1,-5,10,-9,6,-9,-1,9,-3,4,-1,-7,8,7,8,3,-1,-10,-10,9,2,2,-6,1,-8,-7,4,9,-6,5,-6,3,7,-8,6,-4,5,4,-7,-3,9,-5,6,5,10,-5,-10,-4,4,3,-1,-8,3,10,-8,6,-4,10,-4,-1,-7,-3,-5,-4,-10,6,-6,-10,8,-10,4,4,6,10,-1,6,-7,4,5,8,-7,-9,-1,-3,-2,7,-8,5,-7,3,6,-7,-8,3,-9,1,7,8,-2,7,3,-9,5,6,-7,-1,8,-5,8,-2,-9,2,4,2,-8,-7,4,-3,-9,4,-8,10,2,-4,3,5,8,6,7,5,10,8,9,-5,-10,8,-4,4,4,-4,2,7,-9,2,-4,1,1,5,1,-2,-9,-9,-9,-8,-10,9,4,-4,10,8,2,-5,-1,5,-4,-4,-9,7,3,10,8,7,-5,4,4,-9,-3,1,7,-5,5,6,-10,2,8,9,9,-9,-7,-10,-7,9,-5,2,-6,-5,-6,-5,-3,4,-8,7,-10,-2,9,10,-2,6,7,1,6,-6,-6,3,-9,1,1,-5,-4,8,10,1,-6,1,-6,-9,-10,-7,8,-8,-6,-2,-6,-5,-3,-6,-4,-7,4,6,-2,-2,-9,-1,-8,2,7,-8,1,3,-10,-7,6,5,-3,9,5,10,-2,-3,-1,4,-10,-2,10,5,4,4,-7,7,-1,5,-10,2,-7,10,-1,-7,9,-4,-5,-8,-2,-9,3,-6,4,10,8,4,8,-5,-10,-2,4,-7,4,9,8,-4,6,5,3,4,9,5,3,6,4,2,3,-6,5,-2,3,-5,-6,-9,-6,-10,-10,-2,-7,-6,-8,7], dtype = "int32")#candidate|9375|(1080,)|const|int32
call_9374 = relay.TupleGetItem(func_1580_call(relay.reshape(const_9370.astype('int32'), [1, 12, 15]), relay.reshape(const_9375.astype('int32'), [6, 12, 15]), relay.reshape(var_9371.astype('uint64'), [896,]), relay.reshape(const_9372.astype('uint32'), [7, 10]), ), 4)
call_9376 = relay.TupleGetItem(func_1586_call(relay.reshape(const_9370.astype('int32'), [1, 12, 15]), relay.reshape(const_9375.astype('int32'), [6, 12, 15]), relay.reshape(var_9371.astype('uint64'), [896,]), relay.reshape(const_9372.astype('uint32'), [7, 10]), ), 4)
func_7075_call = mod.get_global_var('func_7075')
func_7076_call = mutated_mod.get_global_var('func_7076')
call_9381 = relay.TupleGetItem(func_7075_call(), 0)
call_9382 = relay.TupleGetItem(func_7076_call(), 0)
output = relay.Tuple([call_9336,call_9345,const_9346,const_9347,var_9348,call_9354,var_9355,const_9356,call_9358,var_9359,call_9369,const_9370,var_9371,const_9372,call_9374,const_9375,call_9381,])
output2 = relay.Tuple([call_9337,call_9349,const_9346,const_9347,var_9348,call_9357,var_9355,const_9356,call_9360,var_9359,call_9373,const_9370,var_9371,const_9372,call_9376,const_9375,call_9382,])
func_9433 = relay.Function([var_9348,var_9355,var_9359,var_9371,], output)
mod['func_9433'] = func_9433
mod = relay.transform.InferType()(mod)
var_9434 = relay.var("var_9434", dtype = "float64", shape = (224,))#candidate|9434|(224,)|var|float64
var_9435 = relay.var("var_9435", dtype = "float64", shape = (8, 20))#candidate|9435|(8, 20)|var|float64
var_9436 = relay.var("var_9436", dtype = "int64", shape = (75, 3))#candidate|9436|(75, 3)|var|int64
var_9437 = relay.var("var_9437", dtype = "uint64", shape = (896,))#candidate|9437|(896,)|var|uint64
output = func_9433(var_9434,var_9435,var_9436,var_9437,)
func_9438 = relay.Function([var_9434,var_9435,var_9436,var_9437,], output)
mutated_mod['func_9438'] = func_9438
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6841_call = mod.get_global_var('func_6841')
func_6842_call = mutated_mod.get_global_var('func_6842')
call_9462 = relay.TupleGetItem(func_6841_call(), 0)
call_9463 = relay.TupleGetItem(func_6842_call(), 0)
uop_9464 = relay.acosh(call_9462.astype('float32')) # shape=(9, 2, 6)
uop_9466 = relay.acosh(call_9463.astype('float32')) # shape=(9, 2, 6)
uop_9500 = relay.rsqrt(uop_9464.astype('float32')) # shape=(9, 2, 6)
uop_9502 = relay.rsqrt(uop_9466.astype('float32')) # shape=(9, 2, 6)
output = uop_9500
output2 = uop_9502
func_9528 = relay.Function([], output)
mod['func_9528'] = func_9528
mod = relay.transform.InferType()(mod)
output = func_9528()
func_9529 = relay.Function([], output)
mutated_mod['func_9529'] = func_9529
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8365_call = mod.get_global_var('func_8365')
func_8367_call = mutated_mod.get_global_var('func_8367')
call_9581 = relay.TupleGetItem(func_8365_call(), 0)
call_9582 = relay.TupleGetItem(func_8367_call(), 0)
func_7924_call = mod.get_global_var('func_7924')
func_7925_call = mutated_mod.get_global_var('func_7925')
call_9596 = func_7924_call()
call_9597 = func_7924_call()
bop_9600 = relay.power(call_9596.astype('float32'), relay.reshape(call_9581.astype('float32'), relay.shape_of(call_9596))) # shape=(9, 2, 6)
bop_9603 = relay.power(call_9597.astype('float32'), relay.reshape(call_9582.astype('float32'), relay.shape_of(call_9597))) # shape=(9, 2, 6)
output = relay.Tuple([bop_9600,])
output2 = relay.Tuple([bop_9603,])
func_9607 = relay.Function([], output)
mod['func_9607'] = func_9607
mod = relay.transform.InferType()(mod)
output = func_9607()
func_9608 = relay.Function([], output)
mutated_mod['func_9608'] = func_9608
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9024_call = mod.get_global_var('func_9024')
func_9026_call = mutated_mod.get_global_var('func_9026')
call_9628 = relay.TupleGetItem(func_9024_call(), 0)
call_9629 = relay.TupleGetItem(func_9026_call(), 0)
var_9631 = relay.var("var_9631", dtype = "float32", shape = (9, 2, 6))#candidate|9631|(9, 2, 6)|var|float32
bop_9632 = relay.add(call_9628.astype('int32'), relay.reshape(var_9631.astype('int32'), relay.shape_of(call_9628))) # shape=(9, 2, 6)
bop_9635 = relay.add(call_9629.astype('int32'), relay.reshape(var_9631.astype('int32'), relay.shape_of(call_9629))) # shape=(9, 2, 6)
func_7447_call = mod.get_global_var('func_7447')
func_7448_call = mutated_mod.get_global_var('func_7448')
call_9639 = func_7447_call()
call_9640 = func_7447_call()
output = relay.Tuple([bop_9632,call_9639,])
output2 = relay.Tuple([bop_9635,call_9640,])
func_9641 = relay.Function([var_9631,], output)
mod['func_9641'] = func_9641
mod = relay.transform.InferType()(mod)
var_9642 = relay.var("var_9642", dtype = "float32", shape = (9, 2, 6))#candidate|9642|(9, 2, 6)|var|float32
output = func_9641(var_9642)
func_9643 = relay.Function([var_9642], output)
mutated_mod['func_9643'] = func_9643
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7924_call = mod.get_global_var('func_7924')
func_7925_call = mutated_mod.get_global_var('func_7925')
call_9734 = func_7924_call()
call_9735 = func_7924_call()
output = call_9734
output2 = call_9735
func_9748 = relay.Function([], output)
mod['func_9748'] = func_9748
mod = relay.transform.InferType()(mod)
mutated_mod['func_9748'] = func_9748
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9748_call = mutated_mod.get_global_var('func_9748')
call_9749 = func_9748_call()
output = call_9749
func_9750 = relay.Function([], output)
mutated_mod['func_9750'] = func_9750
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7342_call = mod.get_global_var('func_7342')
func_7344_call = mutated_mod.get_global_var('func_7344')
call_9759 = relay.TupleGetItem(func_7342_call(), 0)
call_9760 = relay.TupleGetItem(func_7344_call(), 0)
func_8026_call = mod.get_global_var('func_8026')
func_8028_call = mutated_mod.get_global_var('func_8028')
call_9761 = relay.TupleGetItem(func_8026_call(), 0)
call_9762 = relay.TupleGetItem(func_8028_call(), 0)
output = relay.Tuple([call_9759,call_9761,])
output2 = relay.Tuple([call_9760,call_9762,])
func_9768 = relay.Function([], output)
mod['func_9768'] = func_9768
mod = relay.transform.InferType()(mod)
mutated_mod['func_9768'] = func_9768
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9768_call = mutated_mod.get_global_var('func_9768')
call_9769 = func_9768_call()
output = call_9769
func_9770 = relay.Function([], output)
mutated_mod['func_9770'] = func_9770
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9774 = relay.var("var_9774", dtype = "float64", shape = (16, 6, 5))#candidate|9774|(16, 6, 5)|var|float64
uop_9775 = relay.asinh(var_9774.astype('float64')) # shape=(16, 6, 5)
bop_9780 = relay.power(var_9774.astype('float64'), relay.reshape(uop_9775.astype('float64'), relay.shape_of(var_9774))) # shape=(16, 6, 5)
uop_9785 = relay.cosh(bop_9780.astype('float64')) # shape=(16, 6, 5)
output = relay.Tuple([uop_9785,])
output2 = relay.Tuple([uop_9785,])
F = relay.Function([var_9774,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_9774,], output2)
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
