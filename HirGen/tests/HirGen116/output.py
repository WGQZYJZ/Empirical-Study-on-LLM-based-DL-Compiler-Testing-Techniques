import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_108 = relay.var("var_108", dtype = "float64", shape = (16, 12, 4))#candidate|108|(16, 12, 4)|var|float64
var_109 = relay.var("var_109", dtype = "float64", shape = (16, 12, 4))#candidate|109|(16, 12, 4)|var|float64
bop_110 = relay.mod(var_108.astype('float64'), relay.reshape(var_109.astype('float64'), relay.shape_of(var_108))) # shape=(16, 12, 4)
output = relay.Tuple([bop_110,])
output2 = relay.Tuple([bop_110,])
func_113 = relay.Function([var_108,var_109,], output)
mod['func_113'] = func_113
mod = relay.transform.InferType()(mod)
var_114 = relay.var("var_114", dtype = "float64", shape = (16, 12, 4))#candidate|114|(16, 12, 4)|var|float64
var_115 = relay.var("var_115", dtype = "float64", shape = (16, 12, 4))#candidate|115|(16, 12, 4)|var|float64
output = func_113(var_114,var_115,)
func_116 = relay.Function([var_114,var_115,], output)
mutated_mod['func_116'] = func_116
mutated_mod = relay.transform.InferType()(mutated_mod)
const_172 = relay.const(-6, dtype = "uint16")#candidate|172|()|const|uint16
var_173 = relay.var("var_173", dtype = "uint16", shape = (14, 11, 1))#candidate|173|(14, 11, 1)|var|uint16
bop_174 = relay.maximum(const_172.astype('uint16'), var_173.astype('uint16')) # shape=(14, 11, 1)
uop_179 = relay.acos(var_173.astype('float32')) # shape=(14, 11, 1)
output = relay.Tuple([bop_174,uop_179,])
output2 = relay.Tuple([bop_174,uop_179,])
func_181 = relay.Function([var_173,], output)
mod['func_181'] = func_181
mod = relay.transform.InferType()(mod)
mutated_mod['func_181'] = func_181
mutated_mod = relay.transform.InferType()(mutated_mod)
var_182 = relay.var("var_182", dtype = "uint16", shape = (14, 11, 1))#candidate|182|(14, 11, 1)|var|uint16
func_181_call = mutated_mod.get_global_var('func_181')
call_183 = func_181_call(var_182)
output = call_183
func_184 = relay.Function([var_182], output)
mutated_mod['func_184'] = func_184
mutated_mod = relay.transform.InferType()(mutated_mod)
var_282 = relay.var("var_282", dtype = "uint8", shape = (10, 13, 4))#candidate|282|(10, 13, 4)|var|uint8
const_283 = relay.const([[[-1,6,3,8],[-6,1,-6,-7],[3,3,6,-4],[4,-7,-5,2],[9,5,-1,-1],[2,8,10,-2],[-9,10,-6,10],[-2,-6,9,4],[-5,1,4,6],[-5,-5,-10,-9],[1,-4,4,6],[10,-5,-1,8],[-10,3,-2,-9]],[[3,-1,-10,-4],[8,9,-10,9],[8,-1,-5,-4],[-10,8,-7,-9],[10,5,-8,2],[-5,-9,-7,-8],[-4,-3,-10,1],[-5,1,7,-10],[8,8,4,-4],[-10,-5,3,3],[2,6,2,-9],[-8,7,-10,10],[-4,-6,10,-7]],[[-6,9,-6,9],[-8,-10,-2,-7],[1,4,3,-1],[-6,-7,-10,-7],[9,-8,-8,-2],[9,5,1,4],[6,-5,-3,9],[-7,6,-1,4],[8,-6,6,-1],[10,-10,9,-4],[1,-7,-8,-6],[3,2,4,3],[-7,-8,-6,2]],[[6,10,-6,-2],[6,5,-6,-8],[-4,2,-6,10],[5,-10,9,-1],[-4,2,-5,-8],[6,4,-6,-10],[5,-8,8,-8],[-8,-3,10,3],[5,3,10,3],[-5,-7,-1,1],[10,9,-9,-10],[-3,5,-9,7],[-4,5,2,-9]],[[7,9,-6,6],[-4,-1,-1,-2],[-3,8,-5,-5],[-5,-2,-8,-7],[-10,5,-9,-9],[5,5,-2,10],[6,-7,-5,10],[5,-9,5,-10],[-2,-9,5,3],[-10,5,9,-7],[-3,6,9,8],[-1,6,2,-1],[10,-7,-9,-4]],[[3,3,5,5],[-4,-8,10,-8],[-4,7,2,-2],[9,9,2,-1],[5,4,-3,9],[-3,-2,-6,2],[-5,-8,6,-1],[-1,-4,-4,-9],[8,8,-4,9],[-6,8,1,2],[10,3,3,-2],[-4,9,-3,6],[2,3,1,-3]],[[2,8,5,9],[3,-3,8,1],[4,-10,6,10],[-10,-6,-4,-7],[-4,10,-9,7],[5,-6,-5,-6],[5,-10,4,3],[-5,-2,-9,5],[-7,3,8,-6],[9,-7,-1,7],[-1,-8,-7,8],[9,-10,10,-2],[-4,3,-4,-6]],[[-2,-9,-8,-8],[-3,5,-9,-3],[2,7,-1,-10],[-3,-9,-3,9],[-8,8,-5,6],[-5,10,-1,-2],[-4,-6,5,2],[-9,4,5,-7],[4,-10,2,-8],[6,-10,-9,-9],[-1,-10,3,4],[-2,-3,-2,2],[6,4,8,6]],[[10,-1,10,1],[-7,8,2,1],[10,3,-4,7],[-6,9,-5,-8],[-3,-3,10,-6],[5,-6,-8,5],[1,-10,-4,5],[8,-4,9,7],[4,8,-3,1],[-10,9,4,-6],[3,-7,2,6],[6,-4,-3,-10],[2,1,2,-5]],[[8,10,9,4],[1,8,-5,-5],[4,7,-2,-6],[-3,-10,-8,-7],[1,6,-3,-4],[4,-8,-8,-10],[-2,-2,4,-7],[-5,-3,-3,9],[8,-6,8,3],[-5,10,6,8],[7,-2,-7,1],[7,-7,4,4],[1,-1,3,-10]]], dtype = "uint8")#candidate|283|(10, 13, 4)|const|uint8
bop_284 = relay.right_shift(var_282.astype('uint8'), relay.reshape(const_283.astype('uint8'), relay.shape_of(var_282))) # shape=(10, 13, 4)
output = relay.Tuple([bop_284,])
output2 = relay.Tuple([bop_284,])
func_292 = relay.Function([var_282,], output)
mod['func_292'] = func_292
mod = relay.transform.InferType()(mod)
var_293 = relay.var("var_293", dtype = "uint8", shape = (10, 13, 4))#candidate|293|(10, 13, 4)|var|uint8
output = func_292(var_293)
func_294 = relay.Function([var_293], output)
mutated_mod['func_294'] = func_294
mutated_mod = relay.transform.InferType()(mutated_mod)
var_647 = relay.var("var_647", dtype = "bool", shape = (10, 14, 11))#candidate|647|(10, 14, 11)|var|bool
var_648 = relay.var("var_648", dtype = "bool", shape = (10, 14, 11))#candidate|648|(10, 14, 11)|var|bool
bop_649 = relay.logical_and(var_647.astype('bool'), relay.reshape(var_648.astype('bool'), relay.shape_of(var_647))) # shape=(10, 14, 11)
var_654 = relay.var("var_654", dtype = "bool", shape = (10, 14, 11))#candidate|654|(10, 14, 11)|var|bool
bop_655 = relay.maximum(bop_649.astype('int16'), relay.reshape(var_654.astype('int16'), relay.shape_of(bop_649))) # shape=(10, 14, 11)
output = bop_655
output2 = bop_655
func_664 = relay.Function([var_647,var_648,var_654,], output)
mod['func_664'] = func_664
mod = relay.transform.InferType()(mod)
mutated_mod['func_664'] = func_664
mutated_mod = relay.transform.InferType()(mutated_mod)
func_664_call = mutated_mod.get_global_var('func_664')
var_666 = relay.var("var_666", dtype = "bool", shape = (10, 14, 11))#candidate|666|(10, 14, 11)|var|bool
var_667 = relay.var("var_667", dtype = "bool", shape = (10, 14, 11))#candidate|667|(10, 14, 11)|var|bool
var_668 = relay.var("var_668", dtype = "bool", shape = (10, 14, 11))#candidate|668|(10, 14, 11)|var|bool
call_665 = func_664_call(var_666,var_667,var_668,)
output = call_665
func_669 = relay.Function([var_666,var_667,var_668,], output)
mutated_mod['func_669'] = func_669
mutated_mod = relay.transform.InferType()(mutated_mod)
var_882 = relay.var("var_882", dtype = "int32", shape = (14, 3, 3))#candidate|882|(14, 3, 3)|var|int32
var_883 = relay.var("var_883", dtype = "int32", shape = (14, 3, 3))#candidate|883|(14, 3, 3)|var|int32
bop_884 = relay.right_shift(var_882.astype('int32'), relay.reshape(var_883.astype('int32'), relay.shape_of(var_882))) # shape=(14, 3, 3)
func_113_call = mod.get_global_var('func_113')
func_116_call = mutated_mod.get_global_var('func_116')
var_892 = relay.var("var_892", dtype = "float64", shape = (2, 384))#candidate|892|(2, 384)|var|float64
call_891 = relay.TupleGetItem(func_113_call(relay.reshape(var_892.astype('float64'), [16, 12, 4]), relay.reshape(var_892.astype('float64'), [16, 12, 4]), ), 0)
call_893 = relay.TupleGetItem(func_116_call(relay.reshape(var_892.astype('float64'), [16, 12, 4]), relay.reshape(var_892.astype('float64'), [16, 12, 4]), ), 0)
func_292_call = mod.get_global_var('func_292')
func_294_call = mutated_mod.get_global_var('func_294')
const_901 = relay.const([2,-2,8,-6,-6,4,6,5,2,8,2,4,9,6,-1,-8,5,-9,-9,9,10,1,9,-2,7,-2,-7,5,-10,-7,-10,-5,-6,7,-9,-3,4,-5,-7,5,-6,-4,-5,-10,-10,7,-1,-6,-7,6,-3,-7,10,-9,10,2,-3,10,5,-5,6,-6,2,-7,7,7,10,-9,9,-9,4,-6,8,-6,-7,-10,3,-1,10,-6,-9,10,-10,-10,-7,-7,-10,9,-10,-5,-6,-9,2,3,-5,-10,-5,-4,9,1,4,-6,-10,6,-2,6,-5,6,-4,9,10,-6,2,-10,-7,-7,-1,-7,10,3,-2,9,-4,3,5,-9,-3,-2,6,-6,-2,-4,-7,-4,-2,-10,-5,-2,-5,-9,8,7,-5,-8,10,-4,8,5,-8,-4,-5,-7,-3,-9,7,-1,8,-8,-9,-3,-10,-1,-6,-4,5,-9,2,1,8,-6,-10,9,6,-10,-4,2,-2,4,9,-4,-8,7,10,5,-7,-2,9,4,9,-10,9,-8,-7,10,-2,2,-9,10,-4,9,6,-10,-1,10,-8,-4,2,-9,6,-7,-4,-8,6,4,3,-3,3,7,8,5,-8,5,10,-1,3,-5,-6,2,3,4,-1,8,-10,9,2,4,-2,-4,-2,9,4,2,8,-2,2,-10,2,-9,3,-10,2,7,-2,-6,-7,-8,8,-10,6,9,7,10,-9,4,9,-9,6,4,-8,-2,5,7,-2,10,-9,7,-10,9,-8,-1,5,-7,-9,-10,-1,-3,2,10,5,3,10,-3,-9,-8,-3,3,1,10,-2,7,1,-2,10,-1,3,-2,-6,-1,-5,-1,2,-6,-5,-4,-7,2,3,-2,-7,9,-7,-1,3,-7,5,-7,-5,9,-9,8,-4,-5,4,9,2,-1,8,-3,6,-7,9,9,7,5,10,4,-6,2,-10,-3,-8,1,-6,7,6,4,-10,-1,-2,-4,10,8,-9,-7,-3,1,-3,-7,9,-3,-10,10,2,6,8,6,-8,-5,7,5,-10,-1,-9,2,-4,4,-3,-3,-6,1,-7,-3,1,1,7,8,-2,-10,7,2,-8,7,-1,-10,-7,2,-8,-8,-2,-9,-5,-6,-5,-2,10,-6,-10,-4,1,-9,-5,-2,-5,-3,9,6,8,3,-10,-8,8,-1,-6,9,-10,-8,9,-9,-10,3,-6,-1,1,-10,8,-3,1,-5,8,-6,10,5,-2,6,-7,-9,-6,-9,-6,-9,-4,-3,6,-4,9,5,2,1,-4,-7,-3,-6,-9,-7,-4,3,1,-5,-3,-1,8,4,-6,3,-1,1,-9,5,3,-6,10,-5,5,-6,-10,3,-3,-6,-3,8,-1,7,7,-9,4,5,5,3,-1,-8,-7,7,-9,10,-3,-5,-7,-6,4,5], dtype = "uint8")#candidate|901|(520,)|const|uint8
call_900 = relay.TupleGetItem(func_292_call(relay.reshape(const_901.astype('uint8'), [10, 13, 4])), 0)
call_902 = relay.TupleGetItem(func_294_call(relay.reshape(const_901.astype('uint8'), [10, 13, 4])), 0)
output = relay.Tuple([bop_884,call_891,var_892,call_900,const_901,])
output2 = relay.Tuple([bop_884,call_893,var_892,call_902,const_901,])
func_905 = relay.Function([var_882,var_883,var_892,], output)
mod['func_905'] = func_905
mod = relay.transform.InferType()(mod)
mutated_mod['func_905'] = func_905
mutated_mod = relay.transform.InferType()(mutated_mod)
func_905_call = mutated_mod.get_global_var('func_905')
var_907 = relay.var("var_907", dtype = "int32", shape = (14, 3, 3))#candidate|907|(14, 3, 3)|var|int32
var_908 = relay.var("var_908", dtype = "int32", shape = (14, 3, 3))#candidate|908|(14, 3, 3)|var|int32
var_909 = relay.var("var_909", dtype = "float64", shape = (2, 384))#candidate|909|(2, 384)|var|float64
call_906 = func_905_call(var_907,var_908,var_909,)
output = call_906
func_910 = relay.Function([var_907,var_908,var_909,], output)
mutated_mod['func_910'] = func_910
mutated_mod = relay.transform.InferType()(mutated_mod)
var_953 = relay.var("var_953", dtype = "float32", shape = (5, 8, 8))#candidate|953|(5, 8, 8)|var|float32
uop_954 = relay.sinh(var_953.astype('float32')) # shape=(5, 8, 8)
func_664_call = mod.get_global_var('func_664')
func_669_call = mutated_mod.get_global_var('func_669')
const_957 = relay.const([True,False,True,True,False,True,True,True,True,False,False,False,True,True,False,False,True,True,True,False,False,False,False,True,False,False,True,False,True,True,False,False,False,False,True,False,True,False,False,False,False,False,False,True,False,False,False,True,False,True,True,False,False,False,False,False,False,True,False,True,True,True,True,True,True,False,True,False,False,True,False,False,False,False,False,False,True,False,True,True,True,True,True,True,True,True,True,True,True,False,True,False,True,False,True,False,True,False,False,True,False,False,False,False,False,False,False,True,False,True,False,True,False,False,True,True,True,False,True,False,False,False,False,True,False,True,True,True,False,True,True,False,True,True,False,False,True,False,True,True,True,False,False,False,False,True,True,True,False,False,False,False,False,False,False,True,False,True,False,False,True,True,False,False,False,False,False,True,False,False,False,True,False,True,True,False,False,True,True,False,True,True,True,False,False,True,True,False,False,True,False,True,True,False,False,True,False,False,True,False,False,True,True,False,False,True,False,True,False,False,True,True,True,False,True,True,True,False,True,False,False,True,True,True,True,True,False,True,False,True,True,False,True,True,True,True,False,True,False,False,True,False,True,True,False,True,False,False,True,False,False,True,True,True,False,True,True,True,False,True,False,False,True,True,True,False,True,True,False,True,True,True,True,False,False,False,True,True,False,True,True,False,False,False,True,True,True,False,False,False,True,False,False,True,False,True,True,True,False,True,False,True,True,False,True,True,False,True,False,False,False,True,False,False,False,True,True,True,False,True,True,True,False,True,False,False,False,False,True,False,True,True,True,False,True,True,False,True,False,False,True,False,False,True,False,False,True,False,True,True,True,True,False,True,False,True,True,True,True,False,True,False,False,True,True,True,False,True,True,False,True,False,False,True,False,False,True,True,False,True,False,False,False,False,True,False,True,True,True,False,True,True,True,True,False,False,True,False,True,False,False,False,False,False,False,False,False,True,True,True,False,True,True,False,False,False,True,True,True,False,False,True,True,True,False,True,True,True,True,False,True,True,False,False,True,False,False,False,False,False,True,False,True,False,True,True,False,False,True,False,False,True,True,False,False,True,True,True,True,True,True,False,False,True,False,False,False,True,False,False,True,True,False,False,True,True,False,True,True,True,True,False,False,False,False,False,False,True,True,True,False,False,True,True,True,False,True,True,True,True,True,False,False,False,False,True,True,False,False,True,True,False,True,True,False,True,True,False,False,False,True,True,False,True,False,False,True,True,True,False,False,True,False,False,True,False,True,False,True,True,True,False,True,False,False,False,True,True,False,False,False,False,True,False,True,True,False,False,False,False,False,False,True,False,False,False,False,True,False,True,False,False,False,False,False,False,False,False,True,False,False,True,False,True,False,True,False,False,True,False,False,True,False,True,True,False,True,False,True,False,True,True,False,True,True,False,True,True,False,True,False,False,False,False,True,False,False,True,True,True,True,True,True,True,True,False,True,False,False,False,False,False,False,False,True,True,True,True,True,True,False,True,False,False,True,True,True,True,True,False,True,False,True,False,False,False,False,True,True,True,False,True,True,False,False,False,True,True,True,False,False,True,True,False,False,True,False,True,False,True,True,True,True,False,True,True,True,False,True,False,True,True,True,False,True,True,False,False,False,False,True,True,True,False,True,True,True,True,False,False,False,True,True,False,False,True,True,True,True,False,True,False,True,False,False,False,False,False,True,False,False,False,True,False,False,True,True,False,False,False,False,True,True,True,True,True,False,False,False,True,True,True,True,False,False,True,True,False,False,False,False,False,False,False,False,False,True,False,False,True,False,False,False,True,False,True,True,False,False,True,False,True,True,True,True,True,True,False,True,True,False,True,True,False,True,False,True,False,False,True,False,False,False,False,True,False,False,False,False,False,False,False,True,True,False,False,False,True,True,True,False,True,False,True,False,False,True,True,False,True,False,False,True,False,True,True,False,True,True,True,True,True,True,False,False,True,False,False,False,True,True,False,True,False,False,True,False,True,False,False,True,False,True,False,True,False,True,True,True,True,False,False,False,False,False,True,True,False,True,False,False,True,False,True,True,False,False,True,False,False,True,True,False,False,True,True,False,True,True,True,False,True,True,False,True,True,True,True,False,True,True,False,False,True,True,True,False,True,False,False,True,True,True,True,False,False,True,False,True,False,False,True,True,True,False,True,True,True,False,True,False,True,True,False,False,False,True,False,True,True,False,False,True,True,True,True,False,False,True,True,False,True,True,False,True,True,True,False,False,True,True,True,False,False,True,False,False,True,True,True,False,True,True,True,True,False,False,True,True,False,False,True,True,True,True,False,False,False,False,True,True,True,False,True,True,True,False,True,False,True,False,True,False,True,False,True,False,True,False,True,True,True,False,False,False,False,True,True,False,True,False,False,True,False,True,False,True,True,False,False,False,False,True,True,False,True,False,False,False,True,True,True,False,True,False,False,True,True,True,False,False,True,False,True,True,True,False,True,True,False,True,True,False,False,False,False,True,True,False,False,False,True,True,False,True,True,False,False,False,False,False,True,True,False,False,True,False,False,False,True,False,True,False,True,True,True,True,False,False,False,False,False,True,False,False,False,True,False,True,False,False,True,True,False,False,True,True,False,False,True,True,False,False,True,True,True,False,True,True,False,True,False,False,False,False,False,True,True,True,False,True,True,True,False,True,True,False,False,True,False,True,False,False,True,False,False,False,False,True,False,True,False,False,True,False,False,False,True,True,True,True,True,False,True,True,False,False,True,False,False,True,False,False,False,True,False,False,False,True,True,False,False,True,False,True,True,False,True,True,True,False,False,False,True,True,False,True,False,True,True,False,True,True,False,True,True,True,True,True,False,False,True,False,True,True,True,False,True,True,True,False,True,False,True,False,True,True,True,True,False,True,True,True,False,False,False,True,True,True,False,True,True,True,True,False,False,False,True,True,True,False,False,True,False,True,True,False,False,True,True,False,False,True,False,False,True,False,False,False,False,False,True,True,False,False,False,False,False,True,False,False,True,False,True,False,True,False,False,True,True,True,True,True,False,True,False,True,False,False,True,False,False,False,True,False,False,True,True,True,False,True,True,False,True,False,False,False,False,False,True,False,True,False,True,False,False,True,True,False,True,True,False,False,True,True,False,False,True,True,True,True,False,False,True,True,False,True,True,False,True,False,False,True,True,False,True,True,True,False,True,True,True,True,True,True,False,True,True,True,True,False,True,True,False,False,True,False,False,False,False,True,True,True,False,False,True,True,True,False,False,False,True,True,True,False,False,True,False,True,True,True,True,False,False,True,False,True,True,False,False,False,False,True,True,False,True,False,False,False,False,False,False,False,True,True,False,False,False,False,True,True,True,True,True,False,False,False,True,False,False,True,False,False,False,True,True,True,True,True,True,True,True,True,True,False,False,False,False,True,False,False,False,False,True,False,False,True,False,True,True,False,True,True,True,True,False,False,True,True,True,False,True,False,False,False,False,False,False,True,True,True,True,False,True,False,False,True,True,False,False,True,False,True,False,True,True,True,True,False,False,False,False,True,False,False,False,True,True,False,False], dtype = "bool")#candidate|957|(1540,)|const|bool
call_956 = func_664_call(relay.reshape(const_957.astype('bool'), [10, 14, 11]), relay.reshape(const_957.astype('bool'), [10, 14, 11]), relay.reshape(const_957.astype('bool'), [10, 14, 11]), )
call_958 = func_664_call(relay.reshape(const_957.astype('bool'), [10, 14, 11]), relay.reshape(const_957.astype('bool'), [10, 14, 11]), relay.reshape(const_957.astype('bool'), [10, 14, 11]), )
func_113_call = mod.get_global_var('func_113')
func_116_call = mutated_mod.get_global_var('func_116')
const_969 = relay.const([6.375043,-4.615003,-2.047742,7.645011,0.758957,2.801260,-3.776991,-2.654039,6.205237,3.468002,-9.362299,2.795020,-2.151245,-4.248478,7.897674,-0.016962,-9.189950,9.146343,-8.859314,9.261338,6.979705,-8.203914,-3.057217,-8.594177,1.473366,3.821370,0.913597,5.296991,-1.384334,8.199441,9.806044,5.803629,9.237991,-9.823642,5.916589,4.504572,-3.881974,-5.423920,-6.684733,-9.429775,7.924131,4.197033,6.768699,-0.660695,2.437576,3.594438,-5.791732,-2.685744,1.114576,3.473858,-1.767594,0.492644,-0.186844,-7.365443,6.749308,3.140317,-1.583832,2.062758,4.787758,-6.822683,-7.823083,0.991934,-1.191636,-9.607754,-1.182154,-8.477290,-4.050714,-2.110232,-0.870112,0.417134,5.275587,-7.247638,0.154093,6.408028,2.803973,1.545706,-2.070863,-3.788223,-9.898009,-8.070595,-2.946060,-4.063672,5.970693,-9.365798,4.756468,6.449833,-1.846441,-0.893889,8.067337,-1.369321,5.858893,-8.785968,0.017467,-5.740389,3.462954,-3.461050,-2.546351,-9.596550,1.965376,7.077990,-8.427057,-4.090065,-9.130362,3.992444,-3.830838,-2.133309,9.970341,1.548005,-1.780309,2.532408,9.017738,7.427076,-1.587939,9.368099,-6.743736,-6.068034,5.183338,0.631427,8.113510,6.875029,5.228680,-4.625550,9.341960,1.390929,5.736843,9.764506,-6.480350,-0.884562,4.596637,1.669642,-7.651549,-5.368250,-1.859150,2.764030,-4.779119,3.478385,6.716538,5.568694,-5.737226,-2.763712,5.086946,-5.801443,-9.572418,-6.855927,-0.086527,-9.386610,8.707245,-4.732412,-9.707420,1.841822,-0.088755,-6.701383,-7.538308,-4.544586,-7.572503,3.332246,1.265723,-1.052559,-1.742443,9.110526,-4.159084,-3.996749,-4.080512,5.536418,-1.966122,-0.555011,0.463583,-8.606179,-8.397203,-5.155566,0.397664,-7.375440,8.660932,9.565744,5.451200,-0.639789,-1.217915,1.299048,6.626320,6.388473,5.100370,1.793236,4.777801,6.008118,-1.848124,-7.116947,4.228851,-6.147619,9.534978,-2.896789,-3.659635,-2.040758,0.011158,-2.689999,-8.445269,3.755852,4.217828,5.789363,-7.182670,-2.698777,-3.852240,2.825754,7.927319,2.409213,7.134925,1.253645,-4.893707,-0.116783,0.328355,3.305709,-6.441526,6.806030,4.253070,-5.567298,4.880440,-1.840189,-2.851007,1.836608,-5.507923,-8.744582,7.502975,6.077197,-9.406989,4.576959,-0.359423,8.064336,7.571533,-9.525386,4.423054,3.997249,3.274729,2.554772,0.714538,4.858073,2.237578,2.315035,1.126272,-4.119303,-3.743011,3.615234,-2.762511,7.619845,-3.880117,-2.173945,0.512250,-6.886152,-2.838670,-8.637473,7.075283,1.747156,0.516897,9.693657,3.914123,-9.695944,8.990243,5.640698,3.223152,-6.597956,-2.733655,7.590834,-7.996456,4.068111,7.457243,-9.553031,8.182543,6.575946,-8.142772,-5.903460,1.059281,9.350228,-1.686167,-5.612228,0.828656,0.097818,-1.376239,7.086917,2.200501,5.013643,-5.833268,7.945981,4.550508,0.430107,6.350123,5.001073,-2.421368,8.634621,3.505677,-8.017101,-7.660373,5.244176,6.213208,6.781061,7.519955,0.469397,-5.789878,1.531546,-8.083454,5.394829,-3.764873,-4.283292,4.320315,-6.402599,0.366285,-3.055605,-6.061374,-8.510189,-7.216951,-3.471375,-4.386630,-4.116369,-2.357846,-2.467546,-7.459812,-9.509009,4.789844,9.214377,7.775127,5.326575,4.078006,-6.111458,3.241267,2.385236,0.993168,6.053011,3.413976,-1.897237,-9.196959,-8.653198,2.296238,9.654820,1.430953,8.941420,-5.543627,-7.446979,-2.414693,-8.590244,4.896533,-6.451828,2.740975,4.017460,3.374336,6.147822,-4.134516,-8.724904,-9.686391,-9.062091,-2.417620,-7.529473,4.665309,-0.071034,-1.112665,6.944840,-2.949285,-2.610261,-7.216127,2.317443,8.654722,2.689950,-9.510029,3.843007,2.042920,6.753847,-9.890247,7.059244,-8.684665,1.560078,-4.122139,-2.311177,-4.500636,-9.975594,-4.740326,-3.090663,-5.069222,-8.477611,6.805668,-9.858635,0.273645,3.740525,7.635093,7.465634,-8.023652,-7.527531,-7.617197,-6.970866,3.583272,0.629480,-0.705425,-9.655874,1.916310,8.416127,-9.152814,3.173211,1.179969,2.717106,7.303182,-0.771533,-2.862647,-2.430243,-3.429114,2.097970,-8.832660,9.510543,9.291577,4.785077,-2.589902,9.928687,-6.273694,0.534849,5.146387,5.437979,4.590016,0.312126,-7.047065,-0.775507,-0.543337,6.651828,-2.391487,2.604983,-8.313727,-0.410528,5.596765,0.745543,1.107348,-3.934240,-6.784332,3.543157,3.526113,1.569689,0.253672,-8.178594,6.587211,-0.545643,0.158632,2.850037,-5.226167,-1.602457,-7.069347,-6.902526,-7.852153,-6.989690,-6.579433,0.199749,-1.205159,5.850034,-0.304110,4.484038,2.145670,-5.899771,7.222340,-1.000307,3.121198,-9.262751,9.381111,9.588396,3.759388,-9.135452,-2.278556,8.564801,-1.725924,-3.428824,9.463962,-8.375545,2.569126,7.631520,1.730618,-7.474497,-5.214982,-8.583474,3.295155,-3.510743,9.669195,-6.413670,-3.260457,9.284618,1.142348,8.795574,9.944803,9.023406,-8.516046,-9.156648,4.432943,8.284845,5.702701,5.056263,3.473794,9.915114,-6.660225,-8.509789,1.807617,5.674229,4.882979,0.375107,-6.821829,2.688826,8.032157,-6.675650,4.926240,2.552173,7.960346,7.179156,-3.087601,-0.792184,6.680803,3.144603,-7.022600,8.869574,7.865795,-4.076521,8.262295,3.560110,2.274346,6.372477,1.856704,9.554117,6.366673,0.556945,4.003495,-7.917917,8.616886,-9.250994,-3.385707,9.632725,-6.766950,-1.563367,-1.872372,9.138576,1.623335,-4.766716,1.441295,-3.360045,-0.788763,-2.466284,9.147143,-2.309217,-9.530208,-3.039410,-3.325599,-5.439700,9.718377,9.454150,-0.079329,-0.387153,6.027372,-4.652362,-8.655252,-1.433956,6.687764,1.149302,9.354579,7.067878,-9.193911,2.499797,3.372559,1.669735,-5.476794,-1.120261,7.938455,-0.664045,9.454414,4.704517,2.584910,2.005796,-2.978071,9.482701,-1.269782,5.464367,-9.183805,-2.457411,9.316808,3.183693,-4.512383,-5.941352,-2.025787,-7.064123,-9.156859,7.082493,8.092617,-5.163339,4.043664,-7.026042,-5.194691,-8.863486,-0.015349,-9.371612,3.576893,2.301317,-1.322836,8.376793,-8.775458,-4.495064,-0.656408,7.947355,-1.245080,8.725096,4.436479,-2.411328,-5.226848,6.991761,6.147999,-7.227305,6.051388,-7.602133,0.010765,-0.257089,3.711194,-0.265690,-9.034048,-2.330408,5.769114,6.302142,8.590555,-1.321484,-3.024809,-3.322326,-5.834252,-3.669208,-8.775168,2.653309,2.741614,4.827794,-5.869737,-2.248858,8.212527,-8.893241,-0.203571,-1.430078,6.083907,9.226320,-0.077205,0.633210,-2.125017,-8.240173,-6.397384,6.637837,4.496749,-5.429925,-5.394118,-9.267987,0.153391,0.971618,-6.877965,7.104062,-7.418439,-4.841843,-7.763594,3.375814,1.998850,4.629704,2.840683,7.384471,-9.620840,0.575167,-7.803832,-5.659967,-3.144779,-1.815876,5.127766,-5.244707,-3.782663,-7.360919,-3.454946,-4.605479,7.257674,4.074039,-6.106035,5.737647,-0.976231,6.673945,9.661904,4.487095,0.181135,-8.397168,4.123903,9.821716,5.531919,7.205716,6.406137,-8.050490,4.777021,-5.385342,-9.031864,-9.312560,-5.703955,-6.068546,-6.883330,6.879160,8.827357,-7.153258,-3.768638,-8.886029,-4.423344,3.819288,6.589263,-5.199115,5.858155,-3.564702,1.126532,-6.297185,9.164958,8.693290,-1.202377,1.727026,-3.138519,6.678871,1.351846,1.282506,9.711614,-3.116338,-7.925739,1.605861,8.016486,2.157656,9.409296,-5.669510,-8.643175,-8.126667,-3.134938,-6.374164,7.999994,9.211751,-6.023761,-7.852047,0.281906,-1.198836,-9.401536,0.377027,-9.323488,-4.493429,-7.756365,-4.496397,-8.726093,-0.595698,-8.874457,1.633977,-3.516460,6.781475,6.765019,-3.914580,-7.095895,-3.166882,-2.556415,-2.726858,4.781256,-4.278564,6.187898,-0.317180,3.202538,-6.485200,-8.544069,-3.756642,-7.479844,1.040126,6.792872,-4.438274,-9.981720,-4.546346,-1.882695,6.062191,1.283170,8.045934,-0.740715,-3.138870,-4.279666,-8.444467,5.145717,1.419417,-5.589738,8.962432], dtype = "float64")#candidate|969|(768,)|const|float64
call_968 = relay.TupleGetItem(func_113_call(relay.reshape(const_969.astype('float64'), [16, 12, 4]), relay.reshape(const_969.astype('float64'), [16, 12, 4]), ), 0)
call_970 = relay.TupleGetItem(func_116_call(relay.reshape(const_969.astype('float64'), [16, 12, 4]), relay.reshape(const_969.astype('float64'), [16, 12, 4]), ), 0)
bop_1001 = relay.greater_equal(uop_954.astype('bool'), relay.reshape(var_953.astype('bool'), relay.shape_of(uop_954))) # shape=(5, 8, 8)
var_1008 = relay.var("var_1008", dtype = "float32", shape = (5, 8, 8))#candidate|1008|(5, 8, 8)|var|float32
bop_1009 = relay.floor_mod(uop_954.astype('float64'), relay.reshape(var_1008.astype('float64'), relay.shape_of(uop_954))) # shape=(5, 8, 8)
output = relay.Tuple([call_956,const_957,call_968,const_969,bop_1001,bop_1009,])
output2 = relay.Tuple([call_958,const_957,call_970,const_969,bop_1001,bop_1009,])
func_1015 = relay.Function([var_953,var_1008,], output)
mod['func_1015'] = func_1015
mod = relay.transform.InferType()(mod)
var_1016 = relay.var("var_1016", dtype = "float32", shape = (5, 8, 8))#candidate|1016|(5, 8, 8)|var|float32
var_1017 = relay.var("var_1017", dtype = "float32", shape = (5, 8, 8))#candidate|1017|(5, 8, 8)|var|float32
output = func_1015(var_1016,var_1017,)
func_1018 = relay.Function([var_1016,var_1017,], output)
mutated_mod['func_1018'] = func_1018
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1100 = relay.var("var_1100", dtype = "uint32", shape = ())#candidate|1100|()|var|uint32
var_1101 = relay.var("var_1101", dtype = "uint32", shape = (8, 5, 13))#candidate|1101|(8, 5, 13)|var|uint32
bop_1102 = relay.logical_xor(var_1100.astype('uint32'), var_1101.astype('uint32')) # shape=(8, 5, 13)
output = bop_1102
output2 = bop_1102
func_1106 = relay.Function([var_1100,var_1101,], output)
mod['func_1106'] = func_1106
mod = relay.transform.InferType()(mod)
var_1107 = relay.var("var_1107", dtype = "uint32", shape = ())#candidate|1107|()|var|uint32
var_1108 = relay.var("var_1108", dtype = "uint32", shape = (8, 5, 13))#candidate|1108|(8, 5, 13)|var|uint32
output = func_1106(var_1107,var_1108,)
func_1109 = relay.Function([var_1107,var_1108,], output)
mutated_mod['func_1109'] = func_1109
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1611 = relay.var("var_1611", dtype = "float64", shape = (8, 5, 6))#candidate|1611|(8, 5, 6)|var|float64
uop_1612 = relay.sigmoid(var_1611.astype('float64')) # shape=(8, 5, 6)
uop_1643 = relay.sinh(uop_1612.astype('float32')) # shape=(8, 5, 6)
uop_1654 = relay.exp(uop_1612.astype('float32')) # shape=(8, 5, 6)
func_1106_call = mod.get_global_var('func_1106')
func_1109_call = mutated_mod.get_global_var('func_1109')
var_1663 = relay.var("var_1663", dtype = "uint32", shape = ())#candidate|1663|()|var|uint32
const_1664 = relay.const([8,1,1,2,8,-6,-8,-6,9,6,4,8,-5,-4,-5,-6,-8,10,-6,9,-8,2,7,6,-1,3,-10,-3,-9,7,-4,6,-9,3,7,-1,6,-2,-9,-8,1,-8,-4,7,1,-9,6,-9,10,-2,4,3,-7,5,-3,10,6,-6,-10,8,-8,6,-2,9,-9,-10,-6,-2,-10,-1,-10,1,-9,-8,2,10,-1,-4,-3,5,-3,4,-2,2,-3,-6,-4,-9,-6,1,1,7,-2,-6,-3,-7,-8,6,9,-1,-1,-5,6,9,1,9,5,-5,-7,2,-2,6,9,-9,10,-1,6,7,2,-3,7,-6,-10,-9,-3,-6,-9,-4,-4,7,2,-4,-5,-2,8,9,-9,-10,-7,-7,8,-7,8,5,4,-6,3,-5,-3,-5,-2,6,3,-2,3,-3,5,-9,-9,2,8,10,-8,-10,-1,1,1,-7,-3,5,10,-10,7,-5,4,2,7,-5,-6,-7,-10,-10,-8,-7,10,1,-1,-5,10,5,-9,-8,-8,5,-8,8,-1,-10,9,-1,1,-9,1,-9,3,-5,-10,3,5,-9,-8,-2,-9,-9,-10,-7,10,-3,9,-4,-5,-7,3,10,-7,3,-8,-6,7,-5,-6,8,-8,7,-3,10,-9,1,-8,-1,2,10,-9,6,4,3,-4,5,3,9,-4,-4,-5,-8,7,-8,3,8,-6,10,-6,1,-5,3,-10,-4,1,-9,2,-1,-7,6,7,-4,8,5,6,-5,-2,-8,3,9,7,-2,7,8,4,-6,7,6,-5,-1,-8,-3,-7,3,3,5,1,-9,-3,-2,10,-10,7,4,10,2,-6,-8,-6,-2,-4,8,-4,-2,5,-6,2,-4,3,-1,-7,-10,-8,5,-9,4,6,7,-1,9,-4,3,-2,-5,6,7,-8,6,3,-1,-8,6,-7,4,-3,-5,9,-3,4,-5,3,-2,8,9,9,6,7,3,-6,-3,1,7,4,10,-7,8,6,-1,10,-8,1,8,7,-1,6,3,10,7,2,-1,10,-1,9,-3,-3,8,6,-2,-5,5,7,-1,9,-2,-5,2,-2,4,-6,-2,9,-4,8,-7,1,8,-9,4,7,9,-8,-7,-3,-6,9,1,-10,4,-3,2,-10,-1,-9,9,10,8,-8,-10,8,-1,6,7,-8,-7,-10,4,-9,-1,9,-6,7,-1,-9,-5,9,-5,9,-2,-1,-6,7,-4,-7,7,-4,-7,7,5,8,-4,-9,1,-1,5,-3,-4,2,-9,5,-5,8,-2,-9,-4,9,4,-7,6,-2,-1,-1,-5,4,-2,-7,8,8,-4,-8,-3,-6,-5,-4,10,-1,8,7,4,5,-2,10,2,9,4,4,-4,-2,3,9,1,6,1,5,7,-9,4,9,9], dtype = "uint32")#candidate|1664|(520,)|const|uint32
call_1662 = func_1106_call(relay.reshape(var_1663.astype('uint32'), []), relay.reshape(const_1664.astype('uint32'), [8, 5, 13]), )
call_1665 = func_1106_call(relay.reshape(var_1663.astype('uint32'), []), relay.reshape(const_1664.astype('uint32'), [8, 5, 13]), )
func_905_call = mod.get_global_var('func_905')
func_910_call = mutated_mod.get_global_var('func_910')
const_1667 = relay.const([-1,-2,9,9,1,10,-2,-5,-10,-6,-1,-8,-7,3,3,9,-7,2,-10,1,-1,-1,-4,9,-5,6,4,-6,-1,2,-1,5,-1,7,10,-1,8,5,10,-10,10,3,-10,-6,10,-2,-6,10,-7,-9,4,7,1,4,5,10,-9,-9,4,7,-1,6,9,-7,2,1,-5,5,-2,9,4,3,4,10,7,-3,-8,8,-6,4,-10,-3,-5,10,9,5,1,-7,-1,-3,6,-7,-7,-4,1,-1,2,5,-4,7,8,-9,1,6,-6,-10,-6,-9,-1,8,-8,2,-4,-9,6,4,-9,3,-2,4,7,-10,-1,8,1,-4], dtype = "int32")#candidate|1667|(126,)|const|int32
const_1668 = relay.const([7.627703,3.797554,2.491955,-8.332320,-4.472377,-6.075656,0.232245,-3.507036,-8.176661,-8.453747,-6.101095,2.901983,5.944162,7.113859,-8.894579,-8.312451,8.170561,-5.285690,5.761696,8.128397,-0.308057,7.959570,-8.121193,2.344919,3.356106,-4.499011,-7.259690,4.602703,1.473650,-9.076522,5.507081,1.824972,-6.874982,9.068102,7.699595,6.157210,-0.181432,2.925930,0.236043,-8.585071,1.470258,-3.729855,-2.024632,2.939890,2.184156,3.795282,-5.829511,4.054962,-3.658313,7.729532,7.174402,-6.028227,3.715095,-6.005571,-2.597769,0.275061,5.165689,1.670695,2.705498,3.833404,-5.027391,5.600721,-8.211134,-0.915396,-6.919153,-8.959101,-4.218020,2.027778,-5.677817,-2.971361,-2.939100,-4.968863,-7.785309,1.484994,8.005121,-1.332411,6.679353,-4.929312,-2.282022,1.381428,-4.428090,3.304934,-7.324799,-4.619795,-8.122863,4.955718,6.484137,8.916601,0.872674,2.374134,1.876924,-3.333275,-3.441341,-0.362844,7.051309,8.949758,4.214210,8.554467,6.590899,6.110458,-9.859608,4.453806,-9.543419,9.568337,5.756910,-5.295822,-1.800981,-9.998908,-0.503051,-9.156170,-3.987265,8.606530,-7.780027,8.947256,1.336736,5.594611,2.030874,3.939373,3.748955,6.869318,2.504999,-6.483360,-7.288648,-6.718431,7.226418,6.892488,-0.034804,-9.026748,7.944640,7.037743,-8.063898,-7.312922,0.958198,3.395329,0.247059,4.774490,2.742061,-3.629019,-5.403111,-5.721707,2.280188,7.076514,-7.174183,-6.858664,9.437599,-8.451264,6.008837,0.548881,-7.416127,9.979278,2.360608,6.138296,-8.609230,0.542936,-1.688624,0.842281,9.220858,-0.498202,-1.426898,0.102406,-3.188181,7.858457,-3.053117,-0.427713,8.415577,-3.627800,-9.288461,0.107675,-9.057574,-0.080719,-1.519723,-2.308021,-9.053629,-2.419989,-6.438127,1.465869,8.340831,-0.428323,2.373324,5.561908,-3.742760,-7.450226,3.365721,-8.444090,-6.825486,-4.049875,-7.049148,-9.965641,2.250963,3.261221,-5.017215,-7.968505,0.476510,3.752032,1.652567,3.779937,7.123597,8.919975,-8.892649,-9.294478,-4.520422,6.340640,7.669622,2.839912,-7.592674,-9.471430,0.482941,4.885553,8.450922,-8.748829,0.976824,3.765534,8.968150,6.139741,-9.026561,-4.033144,-8.747742,5.923750,7.686446,9.911371,5.113357,-0.602863,-6.616136,7.690776,-5.615392,4.434549,6.092077,-7.738624,2.013701,-7.950117,3.261175,-9.211145,4.402920,-7.887847,-0.265696,-0.783716,3.077222,5.065687,-9.903746,-7.248492,-4.815777,-8.791377,-2.402994,-1.840727,-0.224505,2.829708,8.483540,-1.596674,6.359947,4.463777,-5.035044,4.374741,-1.193684,0.948089,3.895022,5.722785,7.037966,1.326987,7.933587,9.900430,2.282991,6.231086,-8.848242,3.701296,-5.198681,-7.906743,-9.572853,8.871522,-8.757812,-7.159245,-9.544444,1.612554,0.855050,2.717243,-8.328297,4.714971,6.956170,-0.128066,-0.347485,0.479271,-2.868706,1.917558,8.658786,2.693179,0.339288,4.585750,4.478106,-5.119787,9.309158,6.286874,-3.303278,3.642337,-1.979022,-2.357397,4.622826,0.322923,0.088596,2.851731,4.695605,-5.737718,-9.771641,-1.638349,-1.428172,-6.946937,-9.764333,8.153356,-4.881791,-0.154207,-7.245003,1.706814,-0.599215,9.432949,8.461114,-9.917671,1.127503,-0.622129,-4.315752,1.535083,4.995095,4.677623,-3.597456,-4.207302,8.830258,5.084936,9.485306,-3.732469,6.269833,2.303556,-0.940257,-3.649278,-6.488318,9.221277,1.823603,6.666650,-3.642502,9.851681,7.753597,-3.987794,-7.618741,-7.552363,-6.477950,-3.310464,-2.468257,9.491600,0.045634,-4.929542,-3.811188,9.888902,5.504812,-4.850950,6.566652,-5.070264,8.444089,1.090595,-3.492921,-2.231841,-4.803598,-5.922355,-1.394027,4.720282,8.908798,-0.414632,3.270143,-3.832922,-1.781092,3.824309,-6.389503,1.420174,-9.710858,9.840691,-1.823943,3.896976,-6.341572,-5.526275,4.335135,4.302394,4.178196,-0.826389,0.436709,3.016838,3.610443,2.913068,-5.435286,-1.382708,1.476108,3.562367,5.174291,6.808349,3.378977,-5.090453,0.643786,0.264728,3.637574,-4.819292,-9.183949,9.851448,-2.971207,6.640760,6.676644,9.601356,-7.569806,-7.957860,8.543413,5.585482,4.570265,-0.392214,5.890904,-6.167318,0.414858,0.147076,-0.952590,-8.394393,2.831369,-3.064635,1.213930,-0.491783,-9.318961,1.881353,-6.801523,-9.101637,-4.405804,-0.878311,5.528975,7.446769,5.773420,-3.780680,6.530766,-4.511171,2.392100,4.309641,-7.189879,-8.349145,-7.509495,6.955458,-8.404232,4.929990,-3.473869,0.694353,-6.969341,-1.828817,1.604381,2.025950,0.245630,-4.191745,-7.913339,0.174026,4.515135,-2.897862,7.957532,-8.221414,1.182478,9.263319,5.802094,3.641865,4.522088,-1.421018,9.185091,4.132136,5.186209,1.355391,3.996769,4.789218,-8.987744,-9.983184,5.082226,0.886342,-2.178965,-4.307471,9.595314,3.479901,6.262363,-8.969007,-6.009876,-5.933410,5.808590,2.926785,-2.643064,0.303968,-5.961150,8.719077,-0.813054,0.020861,8.110329,-8.383628,4.405254,2.625211,0.767355,0.021851,9.177321,-1.545506,7.096678,4.537295,-8.149765,-2.964540,-3.192903,-2.351482,7.062416,-7.732213,9.060895,5.398393,-6.866833,9.616058,-8.890044,7.289433,-5.755486,-2.829021,-7.820339,-1.806089,-4.232696,9.259670,-6.098637,4.731177,7.570403,-6.663223,3.532292,-9.747908,-2.670158,0.273284,-8.625387,-0.207451,-9.013880,4.659685,-3.256016,6.307035,-6.119420,9.494096,-4.459679,-4.288610,-7.717653,-6.703669,0.889443,-2.318025,5.468911,-3.511391,-5.390503,-9.762815,-2.666417,7.356724,6.454930,3.273871,-4.247377,-6.030894,-8.668553,-3.447394,1.202390,-4.306144,2.071604,-6.510527,-5.276686,0.464211,1.643930,-2.986078,0.164663,-5.281163,-2.291717,-7.694858,3.784996,-4.131190,-6.870563,-4.304570,6.504459,-0.499285,7.170586,9.770677,2.307340,7.785312,0.228201,-5.768292,0.050225,4.375023,3.412619,-5.317735,7.026412,-7.790845,-1.150532,2.023173,2.170522,-5.089384,6.901144,-2.521582,-1.708871,1.704136,2.541156,-5.392549,8.554722,3.255994,-8.613292,0.176182,-8.667262,0.440653,-5.255901,-9.872289,-6.581090,8.406336,0.738301,-3.644596,7.328669,3.928228,-9.912145,1.744792,6.287222,-5.554279,4.381615,5.812918,7.175762,-6.892288,-4.096306,8.096220,8.680957,-5.754978,-1.207968,7.577146,-9.402967,7.583642,-9.746057,-1.302269,1.584420,5.450074,-8.865162,-5.722721,7.823830,-3.217590,7.096035,-0.474594,-8.786323,4.421178,-4.094895,-4.624024,6.086238,4.992175,-2.218216,-2.240943,-5.814277,-4.791476,-9.168741,-9.045555,3.005485,9.025304,-8.775039,-8.715374,-1.516728,7.220572,-9.965771,-9.546626,9.659235,7.765122,6.897872,1.316536,-6.785159,8.326100,-4.165159,-5.625933,-5.767762,6.047733,-0.024824,4.196547,4.048887,7.246468,-1.991357,-2.652278,8.234541,3.058875,8.937956,-2.503310,7.687932,-1.943980,0.123902,1.306171,0.464941,-4.889795,-4.173633,-7.710378,-2.478902,2.751984,0.246750,4.728186,-9.732786,-2.504884,2.476458,8.772594,-1.756379,6.417263,-0.585703,2.848766,7.580784,2.839752,4.151372,2.322275,6.197200,-7.196081,-1.483164,2.048902,-0.277349,-5.275115,-2.790856,-2.141145,-3.562468,-6.797724,1.135433,-1.659926,6.034848,-4.926599,7.285092,6.946237,1.118531,-3.647277,7.481195,-4.659080,2.362778,6.421590,-8.442734,-7.284261,0.151014,2.309112,-4.169757,5.332381,-1.653691,-8.006167,-0.309760,-3.148718,4.735479,4.781870,4.606746,-5.642308,6.462296,-8.860586,-9.899148,-4.610323,-5.205244,-6.846011,6.638946,-5.520806,0.492523,1.209818,-3.550407,2.668496,-1.143909,-6.124778,-9.465833,-6.658100,1.427839,6.579519,7.187977,7.960817,-5.353277,-6.313850,-4.885179,8.324946,3.723250,0.484590,-2.096950,7.706632,8.871043,-6.577152,9.364459,2.426145,-7.765029,-3.117432,-9.362614,8.157562,7.265686,-2.781835,-6.365240,1.013180,3.108348,-4.637920,-0.324719,-9.523880], dtype = "float64")#candidate|1668|(768,)|const|float64
call_1666 = relay.TupleGetItem(func_905_call(relay.reshape(const_1667.astype('int32'), [14, 3, 3]), relay.reshape(const_1667.astype('int32'), [14, 3, 3]), relay.reshape(const_1668.astype('float64'), [2, 384]), ), 4)
call_1669 = relay.TupleGetItem(func_910_call(relay.reshape(const_1667.astype('int32'), [14, 3, 3]), relay.reshape(const_1667.astype('int32'), [14, 3, 3]), relay.reshape(const_1668.astype('float64'), [2, 384]), ), 4)
output = relay.Tuple([uop_1643,uop_1654,call_1662,var_1663,const_1664,call_1666,const_1667,const_1668,])
output2 = relay.Tuple([uop_1643,uop_1654,call_1665,var_1663,const_1664,call_1669,const_1667,const_1668,])
func_1676 = relay.Function([var_1611,var_1663,], output)
mod['func_1676'] = func_1676
mod = relay.transform.InferType()(mod)
mutated_mod['func_1676'] = func_1676
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1676_call = mutated_mod.get_global_var('func_1676')
var_1678 = relay.var("var_1678", dtype = "float64", shape = (8, 5, 6))#candidate|1678|(8, 5, 6)|var|float64
var_1679 = relay.var("var_1679", dtype = "uint32", shape = ())#candidate|1679|()|var|uint32
call_1677 = func_1676_call(var_1678,var_1679,)
output = call_1677
func_1680 = relay.Function([var_1678,var_1679,], output)
mutated_mod['func_1680'] = func_1680
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1881 = relay.var("var_1881", dtype = "float32", shape = (14, 7, 5))#candidate|1881|(14, 7, 5)|var|float32
var_1882 = relay.var("var_1882", dtype = "float32", shape = (14, 7, 5))#candidate|1882|(14, 7, 5)|var|float32
bop_1883 = relay.add(var_1881.astype('float32'), relay.reshape(var_1882.astype('float32'), relay.shape_of(var_1881))) # shape=(14, 7, 5)
func_292_call = mod.get_global_var('func_292')
func_294_call = mutated_mod.get_global_var('func_294')
var_1903 = relay.var("var_1903", dtype = "uint8", shape = (10, 52))#candidate|1903|(10, 52)|var|uint8
call_1902 = relay.TupleGetItem(func_292_call(relay.reshape(var_1903.astype('uint8'), [10, 13, 4])), 0)
call_1904 = relay.TupleGetItem(func_294_call(relay.reshape(var_1903.astype('uint8'), [10, 13, 4])), 0)
output = relay.Tuple([bop_1883,call_1902,var_1903,])
output2 = relay.Tuple([bop_1883,call_1904,var_1903,])
func_1907 = relay.Function([var_1881,var_1882,var_1903,], output)
mod['func_1907'] = func_1907
mod = relay.transform.InferType()(mod)
mutated_mod['func_1907'] = func_1907
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1907_call = mutated_mod.get_global_var('func_1907')
var_1909 = relay.var("var_1909", dtype = "float32", shape = (14, 7, 5))#candidate|1909|(14, 7, 5)|var|float32
var_1910 = relay.var("var_1910", dtype = "float32", shape = (14, 7, 5))#candidate|1910|(14, 7, 5)|var|float32
var_1911 = relay.var("var_1911", dtype = "uint8", shape = (10, 52))#candidate|1911|(10, 52)|var|uint8
call_1908 = func_1907_call(var_1909,var_1910,var_1911,)
output = call_1908
func_1912 = relay.Function([var_1909,var_1910,var_1911,], output)
mutated_mod['func_1912'] = func_1912
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1945 = relay.var("var_1945", dtype = "uint16", shape = (11, 4, 1))#candidate|1945|(11, 4, 1)|var|uint16
var_1946 = relay.var("var_1946", dtype = "uint16", shape = (11, 4, 1))#candidate|1946|(11, 4, 1)|var|uint16
bop_1947 = relay.bitwise_xor(var_1945.astype('uint16'), relay.reshape(var_1946.astype('uint16'), relay.shape_of(var_1945))) # shape=(11, 4, 1)
output = bop_1947
output2 = bop_1947
func_1953 = relay.Function([var_1945,var_1946,], output)
mod['func_1953'] = func_1953
mod = relay.transform.InferType()(mod)
mutated_mod['func_1953'] = func_1953
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1953_call = mutated_mod.get_global_var('func_1953')
var_1955 = relay.var("var_1955", dtype = "uint16", shape = (11, 4, 1))#candidate|1955|(11, 4, 1)|var|uint16
var_1956 = relay.var("var_1956", dtype = "uint16", shape = (11, 4, 1))#candidate|1956|(11, 4, 1)|var|uint16
call_1954 = func_1953_call(var_1955,var_1956,)
output = call_1954
func_1957 = relay.Function([var_1955,var_1956,], output)
mutated_mod['func_1957'] = func_1957
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2384 = relay.var("var_2384", dtype = "uint32", shape = ())#candidate|2384|()|var|uint32
var_2385 = relay.var("var_2385", dtype = "uint32", shape = (12, 14, 12))#candidate|2385|(12, 14, 12)|var|uint32
bop_2386 = relay.logical_xor(var_2384.astype('uint32'), var_2385.astype('uint32')) # shape=(12, 14, 12)
func_181_call = mod.get_global_var('func_181')
func_184_call = mutated_mod.get_global_var('func_184')
const_2391 = relay.const([2,9,-9,6,-6,-2,1,-2,4,10,-7,-2,-6,-4,6,6,-7,-5,4,10,6,-1,-3,-7,-10,-5,-3,5,3,-8,9,1,10,2,7,-8,-2,-9,-3,-4,-3,-9,5,-6,3,9,7,-8,6,-5,-2,4,-1,10,7,-8,-2,7,-10,6,-6,-7,-7,-3,7,-3,-8,-2,10,-4,8,9,8,-9,-10,4,-2,-8,8,-9,9,1,-1,-8,-8,1,-4,-8,-8,-1,-2,2,-7,-10,-4,-9,4,-2,-4,-7,-5,-10,9,-1,3,-3,8,6,10,10,8,8,-1,9,3,10,4,-4,6,-10,-7,3,-2,3,-8,3,2,7,2,-9,-2,2,8,9,-1,-4,-5,8,-7,-7,-3,8,4,1,1,-2,10,9,7,-2,10,-1,-5,2], dtype = "uint16")#candidate|2391|(154,)|const|uint16
call_2390 = relay.TupleGetItem(func_181_call(relay.reshape(const_2391.astype('uint16'), [14, 11, 1])), 0)
call_2392 = relay.TupleGetItem(func_184_call(relay.reshape(const_2391.astype('uint16'), [14, 11, 1])), 0)
output = relay.Tuple([bop_2386,call_2390,const_2391,])
output2 = relay.Tuple([bop_2386,call_2392,const_2391,])
func_2395 = relay.Function([var_2384,var_2385,], output)
mod['func_2395'] = func_2395
mod = relay.transform.InferType()(mod)
mutated_mod['func_2395'] = func_2395
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2395_call = mutated_mod.get_global_var('func_2395')
var_2397 = relay.var("var_2397", dtype = "uint32", shape = ())#candidate|2397|()|var|uint32
var_2398 = relay.var("var_2398", dtype = "uint32", shape = (12, 14, 12))#candidate|2398|(12, 14, 12)|var|uint32
call_2396 = func_2395_call(var_2397,var_2398,)
output = call_2396
func_2399 = relay.Function([var_2397,var_2398,], output)
mutated_mod['func_2399'] = func_2399
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2614 = relay.var("var_2614", dtype = "int8", shape = (2, 1, 1))#candidate|2614|(2, 1, 1)|var|int8
var_2615 = relay.var("var_2615", dtype = "int8", shape = (2, 12, 8))#candidate|2615|(2, 12, 8)|var|int8
bop_2616 = relay.maximum(var_2614.astype('int8'), var_2615.astype('int8')) # shape=(2, 12, 8)
output = bop_2616
output2 = bop_2616
func_2622 = relay.Function([var_2614,var_2615,], output)
mod['func_2622'] = func_2622
mod = relay.transform.InferType()(mod)
var_2623 = relay.var("var_2623", dtype = "int8", shape = (2, 1, 1))#candidate|2623|(2, 1, 1)|var|int8
var_2624 = relay.var("var_2624", dtype = "int8", shape = (2, 12, 8))#candidate|2624|(2, 12, 8)|var|int8
output = func_2622(var_2623,var_2624,)
func_2625 = relay.Function([var_2623,var_2624,], output)
mutated_mod['func_2625'] = func_2625
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2787 = relay.const([[[-5],[-8],[-10],[4],[-4],[-7],[-3],[-9],[-4],[-7],[4],[5],[-5],[6]],[[-9],[3],[7],[-8],[-2],[7],[3],[6],[-6],[-7],[9],[-7],[1],[2]],[[-8],[-7],[-5],[-4],[-2],[3],[7],[3],[-4],[8],[-3],[2],[-10],[5]],[[-3],[-9],[-3],[-10],[7],[-5],[8],[-6],[-8],[7],[-5],[3],[1],[-9]],[[6],[-6],[9],[2],[2],[-4],[-7],[9],[-7],[-10],[-1],[6],[-3],[5]],[[8],[-7],[-8],[-5],[-8],[2],[-10],[8],[-5],[3],[-9],[4],[10],[-7]],[[1],[-7],[6],[5],[-8],[-4],[7],[4],[-2],[5],[9],[-7],[2],[10]],[[5],[5],[9],[-7],[9],[-2],[10],[1],[2],[5],[8],[-1],[-9],[-5]],[[4],[-3],[3],[5],[1],[9],[-3],[6],[7],[-3],[5],[-2],[9],[1]],[[-4],[6],[-4],[-4],[-6],[-10],[-2],[8],[-10],[-9],[4],[-7],[-1],[3]],[[4],[5],[-10],[5],[10],[10],[-10],[-5],[-9],[-8],[-9],[-7],[10],[-3]],[[7],[-10],[-8],[1],[5],[-4],[5],[3],[4],[10],[2],[2],[4],[6]],[[5],[2],[5],[-5],[6],[-3],[-1],[-8],[-8],[-4],[6],[6],[9],[-1]]], dtype = "int8")#candidate|2787|(13, 14, 1)|const|int8
const_2788 = relay.const([[[-6,7,8,-1,-7,6,9,-4,6],[5,-6,3,1,2,-6,9,7,9],[10,-8,-6,-4,4,2,-3,9,10],[-3,-5,-4,8,-10,-3,-2,-10,9],[-7,-2,4,10,-3,-9,2,-5,-9],[-5,-6,3,7,-2,6,-2,8,-3],[-10,-10,-3,-5,10,-1,10,-5,-2],[-6,2,5,-3,8,-2,4,3,4],[-10,10,-8,-9,6,7,-10,6,-4],[9,-9,-9,-7,3,-4,7,-6,7],[5,-4,-10,8,5,2,-4,-5,10],[-4,-6,9,3,-7,1,5,-8,7],[-10,-7,-9,-2,-2,8,2,8,-10],[-9,3,4,-8,1,7,-3,3,10]],[[1,-6,1,-2,5,-1,7,8,4],[5,10,-9,4,-4,3,8,5,6],[8,-9,8,-6,9,-8,-7,-8,-8],[5,-10,10,10,9,2,3,3,-2],[1,-7,-3,7,7,6,2,-9,10],[-8,-7,-6,-10,10,-1,6,10,6],[8,3,1,-5,3,-7,-3,-3,-2],[3,8,-7,6,2,-7,-1,-4,-2],[-6,-7,-1,1,-9,-6,5,-3,3],[-3,1,6,6,3,-4,2,-4,-10],[-3,-2,-7,-3,10,-5,-6,-3,-4],[7,8,7,-8,1,-9,-8,-2,-3],[9,-9,-4,1,1,-8,-4,-4,-6],[-4,1,6,-4,2,-5,3,3,-2]],[[-6,-6,8,3,-9,-6,-9,7,6],[2,8,-8,-1,4,4,-10,2,9],[-9,3,1,-3,2,2,3,-1,-10],[-1,-9,6,4,6,-3,5,-7,-2],[-10,1,-4,3,9,-8,3,3,-8],[-7,-4,-8,8,-10,2,5,6,-5],[9,8,1,10,-7,8,-1,-10,8],[3,-1,-2,3,-6,-1,9,-10,1],[-5,7,-3,9,-10,8,-7,5,-4],[-1,-4,5,-2,7,-3,5,-9,-2],[-7,-6,-2,-6,-7,-6,-8,7,-6],[7,-9,9,-3,10,7,4,-2,1],[-7,10,-8,5,5,-7,-6,-10,9],[7,-6,-5,6,8,-2,-2,8,4]],[[-10,3,1,-10,-4,-10,-2,6,3],[-2,3,-6,9,-5,-2,2,-8,-9],[4,-5,-10,3,3,1,-3,4,-2],[-2,-10,7,-7,-2,-5,3,-10,8],[-3,-1,2,-2,-4,-4,7,-7,-4],[9,-5,-4,1,10,6,-1,-10,-5],[4,-1,2,-5,1,7,10,7,-6],[6,8,1,5,-3,2,-7,-3,-7],[4,-5,-5,10,-8,-3,-8,4,-4],[-10,-6,-3,-8,7,1,-8,5,9],[10,9,4,4,10,10,4,-2,2],[9,8,-3,1,3,7,-9,-1,4],[-8,-9,-10,-2,-6,3,2,8,-1],[10,-2,-7,4,7,2,-1,2,9]],[[-9,-6,-9,-3,-2,-2,3,4,-4],[-6,5,-2,-5,-9,4,-10,-1,8],[-5,1,-5,2,-5,-3,5,7,-3],[9,5,6,6,-2,10,6,-2,-3],[-2,-3,1,-5,-7,6,-5,-7,-5],[-8,7,-9,-10,4,-4,9,4,-2],[-9,-9,3,-4,4,-9,-4,-9,8],[2,5,-10,-3,-6,2,-9,-6,5],[6,10,-5,-9,5,-4,6,-1,-9],[9,-1,-8,2,3,-6,1,-2,-3],[7,5,-10,7,4,6,-10,-5,1],[-5,1,-2,6,10,-2,4,7,-3],[10,-10,9,-6,-2,-1,6,-5,-2],[3,-10,-8,8,-6,-3,9,-1,8]],[[8,9,6,-10,-6,7,-3,7,-5],[-10,9,7,6,-7,-8,9,8,-5],[-9,-7,1,-2,6,10,8,-6,5],[-1,1,2,-3,-7,-10,-7,7,-4],[8,3,-9,7,4,-4,-7,1,-7],[9,-3,-2,9,10,3,-6,-1,-7],[3,-6,7,5,-9,4,-9,-7,-1],[5,-8,8,10,2,-3,2,5,1],[9,6,2,5,2,6,-1,-5,-8],[10,-5,9,-3,3,10,10,10,1],[-7,-5,-8,-4,2,8,10,-7,-10],[4,1,1,-3,-1,10,-7,8,-8],[3,-7,-9,4,-3,-8,-1,-6,2],[-4,-2,-8,-6,-7,-6,-3,7,1]],[[-7,7,8,-4,-10,1,-2,4,9],[4,6,-2,-8,-1,-8,-3,9,-6],[-7,-8,-3,-6,-4,-8,-4,-8,6],[5,8,-1,8,1,3,-6,8,-7],[3,-7,-8,9,9,-4,-1,1,5],[-6,-3,2,-4,8,4,-4,-9,-3],[-8,-8,-4,-2,-1,4,4,-1,-5],[-4,-5,1,-6,-4,8,1,-2,10],[3,-10,-4,2,-2,-4,-10,-8,-9],[-2,-5,-1,8,6,-2,7,-10,-2],[1,2,-9,-4,3,3,10,8,-6],[8,-10,3,3,-9,-6,7,5,3],[-6,-4,-9,-2,6,4,-8,5,7],[1,-7,4,9,3,1,-9,-4,-7]],[[-2,10,2,8,-6,-9,1,4,-10],[3,10,-5,-3,9,5,-8,6,3],[-2,7,5,3,-5,4,-5,-7,5],[5,4,3,1,-6,-9,-4,-3,-1],[6,4,2,9,7,2,5,9,-3],[-1,-4,-1,8,-6,-6,-1,2,6],[-5,1,2,-5,-3,6,-7,-8,4],[3,-5,-6,7,-5,-3,3,9,-4],[-7,8,3,6,1,-8,5,10,10],[1,1,6,-1,4,3,9,-6,2],[10,-9,1,-7,-1,-6,-3,8,-5],[10,3,5,3,-10,10,-10,9,3],[-7,6,-9,8,-1,4,1,1,-9],[4,2,-2,-5,7,10,-1,2,2]],[[2,-1,-6,-9,10,-5,-8,-2,-2],[-5,5,-8,-1,1,-8,3,4,-1],[9,-1,1,10,4,10,-4,-10,8],[-5,7,-2,-10,-5,9,9,7,8],[4,7,-10,2,3,-5,10,-8,6],[3,5,4,-5,5,-1,-10,-3,-2],[6,-6,-8,8,1,-6,-7,6,-7],[9,1,6,7,8,-2,10,6,7],[-9,5,-4,-10,10,-5,6,10,8],[-9,1,2,8,3,1,2,-8,1],[-8,3,9,-8,3,-2,6,-7,-9],[-2,2,2,9,5,-9,-7,9,6],[9,-3,-1,-5,-6,-4,1,1,3],[-9,7,10,-10,4,9,9,3,-2]],[[9,-1,-10,-10,-3,6,-6,2,9],[-1,9,2,5,-5,5,3,3,-9],[-3,5,1,5,6,-1,7,6,7],[-3,-1,-1,4,-8,-1,1,5,-9],[-7,6,-10,-10,10,5,6,-10,-4],[3,4,-8,-8,9,7,2,2,9],[6,3,7,-1,-3,10,-3,-9,4],[-4,-6,-8,10,-7,9,-8,-7,-10],[8,7,-4,1,10,4,9,6,10],[-8,-7,7,-3,2,-6,4,6,7],[8,9,10,-10,1,2,-4,-6,-9],[9,-7,-4,3,-9,9,1,4,5],[-3,-10,-3,-10,7,7,6,-10,5],[8,-1,-1,2,10,-1,-9,2,-1]],[[-6,-1,6,8,4,-6,1,-8,-4],[-5,-10,4,1,-8,-5,-7,1,-3],[-8,2,7,10,6,10,-9,-6,-3],[-2,6,-7,-10,-3,4,9,-6,-3],[-1,-1,-1,4,-10,-8,-3,-7,-10],[-3,9,-3,-3,-7,5,2,-3,10],[-7,-3,-5,10,-1,8,-9,4,-6],[-5,1,-7,-1,10,-3,-7,5,7],[-3,1,-2,-7,-9,-3,8,-5,9],[3,3,6,-6,-4,5,2,-8,3],[-1,3,1,-8,-1,8,-6,-1,-6],[3,-4,-2,10,-8,-8,-8,-9,-2],[6,-9,-4,-8,10,9,8,8,1],[-10,8,1,9,9,-10,-10,3,-3]],[[8,7,-1,-6,8,-3,-7,-2,-3],[3,2,-9,2,-1,9,-2,-5,7],[-5,7,6,-2,4,-8,-7,-6,2],[1,7,9,-6,-4,-7,-9,3,-6],[7,-2,4,-8,2,9,-1,9,2],[3,6,1,8,8,5,10,3,-2],[3,-5,-4,-10,7,-3,7,9,3],[9,-9,3,-2,-7,-5,2,-9,-5],[-3,9,6,9,10,-5,7,4,-2],[1,10,-10,6,-4,-1,7,-6,4],[-8,3,10,-3,-5,-4,-4,2,-4],[8,6,-5,3,-3,-8,-10,9,-6],[-5,-9,-6,9,9,-3,-6,10,-4],[-9,7,-7,8,-3,3,7,6,8]],[[10,-1,9,-9,-6,-6,-6,-9,-8],[9,-4,-4,-10,6,-8,10,-4,-4],[-7,-9,-6,5,-2,6,-3,-6,7],[-5,-1,-5,-9,-5,-5,7,4,7],[1,-3,-8,-2,3,-9,6,-7,7],[5,6,9,3,-5,2,-8,-6,5],[-9,7,3,-4,10,-7,3,4,-6],[-5,1,-5,-4,5,3,5,6,-5],[6,9,1,4,10,7,5,4,-4],[10,-3,9,4,9,4,9,5,7],[-6,2,-2,-1,-3,-4,5,6,-8],[5,8,4,-9,-5,2,2,4,-3],[5,5,10,-4,3,4,-4,5,-2],[6,-5,8,3,-7,-4,-7,-6,-6]]], dtype = "int8")#candidate|2788|(13, 14, 9)|const|int8
bop_2789 = relay.minimum(const_2787.astype('int8'), const_2788.astype('int8')) # shape=(13, 14, 9)
output = bop_2789
output2 = bop_2789
func_2801 = relay.Function([], output)
mod['func_2801'] = func_2801
mod = relay.transform.InferType()(mod)
mutated_mod['func_2801'] = func_2801
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2801_call = mutated_mod.get_global_var('func_2801')
call_2802 = func_2801_call()
output = call_2802
func_2803 = relay.Function([], output)
mutated_mod['func_2803'] = func_2803
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2804 = relay.var("var_2804", dtype = "float64", shape = (4, 1, 1))#candidate|2804|(4, 1, 1)|var|float64
uop_2805 = relay.asinh(var_2804.astype('float64')) # shape=(4, 1, 1)
func_2395_call = mod.get_global_var('func_2395')
func_2399_call = mutated_mod.get_global_var('func_2399')
const_2809 = relay.const(-5, dtype = "uint32")#candidate|2809|()|const|uint32
var_2810 = relay.var("var_2810", dtype = "uint32", shape = (1008, 2))#candidate|2810|(1008, 2)|var|uint32
call_2808 = relay.TupleGetItem(func_2395_call(relay.reshape(const_2809.astype('uint32'), []), relay.reshape(var_2810.astype('uint32'), [12, 14, 12]), ), 2)
call_2811 = relay.TupleGetItem(func_2399_call(relay.reshape(const_2809.astype('uint32'), []), relay.reshape(var_2810.astype('uint32'), [12, 14, 12]), ), 2)
func_2395_call = mod.get_global_var('func_2395')
func_2399_call = mutated_mod.get_global_var('func_2399')
call_2814 = relay.TupleGetItem(func_2395_call(relay.reshape(const_2809.astype('uint32'), []), relay.reshape(var_2810.astype('uint32'), [12, 14, 12]), ), 0)
call_2815 = relay.TupleGetItem(func_2399_call(relay.reshape(const_2809.astype('uint32'), []), relay.reshape(var_2810.astype('uint32'), [12, 14, 12]), ), 0)
func_2622_call = mod.get_global_var('func_2622')
func_2625_call = mutated_mod.get_global_var('func_2625')
var_2828 = relay.var("var_2828", dtype = "int8", shape = (2, 1))#candidate|2828|(2, 1)|var|int8
const_2829 = relay.const([2,-7,-5,7,-2,6,5,7,7,4,-8,-1,-10,3,9,-3,1,6,-6,3,-5,-3,4,-8,5,-5,6,9,6,-7,3,8,3,-1,8,7,2,4,10,-9,3,-10,-1,4,-3,2,2,-2,-5,1,7,-7,-10,5,4,-8,9,5,-7,7,1,-7,-1,-5,2,-2,-8,5,1,-9,-3,1,5,2,-4,-1,8,7,7,-8,9,-7,8,-4,-4,-3,10,-1,-9,-6,-9,9,6,-7,-5,3,4,1,-4,2,-8,6,-10,-4,9,-3,8,8,-5,9,9,-7,4,6,3,-7,-2,2,2,-10,-5,-1,-4,-8,-3,2,-9,-6,5,2,-9,-2,5,-2,9,8,-4,8,8,-6,3,5,-7,6,5,1,-10,-5,-6,-10,7,-10,8,9,-5,7,5,1,-4,-3,8,3,8,1,-2,-10,2,2,-7,6,-7,2,-6,1,4,1,1,-10,-9,-4,3,-4,3,4,8,-4,2,7,8,10,-4,-4], dtype = "int8")#candidate|2829|(192,)|const|int8
call_2827 = func_2622_call(relay.reshape(var_2828.astype('int8'), [2, 1, 1]), relay.reshape(const_2829.astype('int8'), [2, 12, 8]), )
call_2830 = func_2622_call(relay.reshape(var_2828.astype('int8'), [2, 1, 1]), relay.reshape(const_2829.astype('int8'), [2, 12, 8]), )
output = relay.Tuple([uop_2805,call_2808,const_2809,var_2810,call_2814,call_2827,var_2828,const_2829,])
output2 = relay.Tuple([uop_2805,call_2811,const_2809,var_2810,call_2815,call_2830,var_2828,const_2829,])
func_2833 = relay.Function([var_2804,var_2810,var_2828,], output)
mod['func_2833'] = func_2833
mod = relay.transform.InferType()(mod)
mutated_mod['func_2833'] = func_2833
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2833_call = mutated_mod.get_global_var('func_2833')
var_2835 = relay.var("var_2835", dtype = "float64", shape = (4, 1, 1))#candidate|2835|(4, 1, 1)|var|float64
var_2836 = relay.var("var_2836", dtype = "uint32", shape = (1008, 2))#candidate|2836|(1008, 2)|var|uint32
var_2837 = relay.var("var_2837", dtype = "int8", shape = (2, 1))#candidate|2837|(2, 1)|var|int8
call_2834 = func_2833_call(var_2835,var_2836,var_2837,)
output = call_2834
func_2838 = relay.Function([var_2835,var_2836,var_2837,], output)
mutated_mod['func_2838'] = func_2838
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2801_call = mod.get_global_var('func_2801')
func_2803_call = mutated_mod.get_global_var('func_2803')
call_2868 = func_2801_call()
call_2869 = func_2801_call()
func_2801_call = mod.get_global_var('func_2801')
func_2803_call = mutated_mod.get_global_var('func_2803')
call_2882 = func_2801_call()
call_2883 = func_2801_call()
output = relay.Tuple([call_2868,call_2882,])
output2 = relay.Tuple([call_2869,call_2883,])
func_2885 = relay.Function([], output)
mod['func_2885'] = func_2885
mod = relay.transform.InferType()(mod)
mutated_mod['func_2885'] = func_2885
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2885_call = mutated_mod.get_global_var('func_2885')
call_2886 = func_2885_call()
output = call_2886
func_2887 = relay.Function([], output)
mutated_mod['func_2887'] = func_2887
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2801_call = mod.get_global_var('func_2801')
func_2803_call = mutated_mod.get_global_var('func_2803')
call_2905 = func_2801_call()
call_2906 = func_2801_call()
func_292_call = mod.get_global_var('func_292')
func_294_call = mutated_mod.get_global_var('func_294')
const_2908 = relay.const([-5,1,4,-7,4,-1,-4,-1,10,3,-1,-5,6,6,-7,4,-3,-9,4,-4,-10,3,-5,-6,-4,-5,6,3,9,-6,10,8,8,10,3,-10,8,6,-10,8,-1,-9,4,9,-1,10,6,5,-7,-5,3,-3,1,-6,-4,-4,-9,4,-5,7,-9,-9,6,8,-3,6,-10,-6,-10,1,7,3,-8,-7,1,1,10,-4,6,-2,6,-2,6,-9,-8,-2,-8,9,3,1,10,3,-3,-8,2,-5,-9,7,5,-2,8,8,-1,4,-4,8,-8,-6,10,8,-6,-2,-10,-10,7,-7,-10,-1,-1,4,9,-9,-5,-7,-1,-8,-10,3,9,4,-7,-1,6,-7,8,-2,5,5,8,-6,-7,-7,-5,8,6,-10,-4,2,-2,9,-2,6,-4,-9,10,-1,-2,-5,-3,-10,6,-3,-8,2,-4,9,-2,3,-3,8,8,4,2,-6,4,-3,4,1,-1,-2,-4,10,6,-3,8,4,-3,-5,-8,9,6,2,-7,4,4,2,-6,3,10,1,-7,1,3,-6,-6,3,-6,2,8,9,1,-9,8,1,9,-3,8,8,-1,-4,-9,10,4,9,7,3,1,-7,5,6,-1,-2,-4,-4,-7,5,7,-3,9,-2,-10,-6,-8,-10,4,-7,-7,-6,9,10,-10,4,-2,10,-7,-10,9,7,-3,-10,-5,2,6,-4,1,3,-1,-1,-1,4,7,-2,4,-4,6,-3,-1,-2,-4,3,10,-7,10,4,10,9,6,4,1,-6,-1,10,4,10,8,-3,9,9,-7,3,3,-5,-1,8,6,-1,-10,1,-2,-2,-6,9,3,7,3,9,1,-4,4,6,-5,-9,9,9,-2,-2,-5,8,-8,-2,-4,-8,5,-7,5,9,2,7,9,-3,-8,-1,-5,-3,-3,-6,5,4,-8,-9,6,-5,7,2,-9,-6,9,9,6,8,6,10,10,1,5,-2,-9,3,-10,-9,9,5,-3,-3,8,-10,-7,-8,-4,-6,-1,2,-7,8,-10,-4,4,-1,6,8,7,-8,8,-3,7,1,-10,-9,-10,2,-4,10,-10,5,-5,9,2,-10,5,3,5,-9,-9,-1,5,-8,2,7,1,7,6,9,5,-8,-5,2,5,4,-10,-2,6,4,-9,1,4,5,-4,-7,6,-7,6,-10,1,-6,6,-5,-9,-4,9,-10,1,-2,2,2,-7,-8,8,-4,1,-9,-10,-1,3,-9,9,3,5,-5,-5,6,7,4,3,6,10,8,2,-8,5,5,-5,3,4,-8,6,2,9,1,-6,3,-4,5,-2,-1,10,-10,4,6,3,6,7,5,4,7,2,-5,3,-2,-2,-4,9,-5,1,-1,-5,-6,-7,-10,6,10], dtype = "uint8")#candidate|2908|(520,)|const|uint8
call_2907 = relay.TupleGetItem(func_292_call(relay.reshape(const_2908.astype('uint8'), [10, 13, 4])), 0)
call_2909 = relay.TupleGetItem(func_294_call(relay.reshape(const_2908.astype('uint8'), [10, 13, 4])), 0)
uop_2910 = relay.sin(const_2908.astype('float32')) # shape=(520,)
func_1015_call = mod.get_global_var('func_1015')
func_1018_call = mutated_mod.get_global_var('func_1018')
const_2913 = relay.const([-4.513437,9.392220,-5.936531,0.455838,1.519794,6.723258,3.055661,5.905062,-8.143676,4.867619,-7.093796,1.272498,-4.004143,-1.941358,-8.099840,-9.472558,5.224532,5.303862,-0.351057,-9.515493,0.324692,-0.581200,9.923674,0.102357,2.919056,-9.968130,-6.667701,3.370299,2.051210,-6.836961,-9.323534,-7.090875,6.569572,1.526504,-4.559906,4.652179,1.114105,-6.570111,2.959518,-2.634172,0.867032,-9.776038,-8.667441,-0.529246,-9.728725,5.198155,9.122014,-7.418134,8.723164,-6.163015,-4.119184,-6.461531,-4.410120,-1.931092,-8.632375,-6.126053,-3.567500,0.985069,-4.793504,-7.630439,-5.204503,9.331130,9.787878,-9.746846,4.529957,0.105088,-1.874666,-4.475738,-5.372191,-4.917308,6.201270,-7.491644,-1.300506,5.288516,-3.309450,9.849079,0.569028,-8.693514,-1.046346,-0.339722,-8.854883,1.863066,7.693150,2.057432,0.721364,-2.454269,-8.225810,-9.140982,-3.350990,8.662477,1.390184,2.557040,0.546685,9.986375,3.906379,0.583144,6.952075,-2.901759,-2.623965,2.260099,-0.419249,2.879908,-1.101025,9.257377,4.499860,2.984340,4.192082,4.547476,5.811156,-9.747706,-3.046322,-0.854414,3.711335,-7.859592,-3.976750,3.771603,4.609998,0.528881,-3.378873,-9.928292,5.927213,-8.351715,5.858297,9.053559,-4.053203,8.051074,6.564952,1.198616,-6.340700,0.047009,4.753371,5.191354,0.407158,-3.001423,3.703346,9.728356,8.939433,3.428868,3.267691,1.722244,6.940480,6.961406,-3.674943,4.388272,-6.007014,9.218222,7.709228,0.143458,1.052229,-9.995378,-2.237287,6.143596,5.872229,-6.429635,2.008997,-4.356037,-3.944890,5.045565,-9.274643,-4.906524,1.672537,-7.406091,-2.565675,2.458474,-4.998110,0.026456,1.435422,-6.756615,7.436529,-4.537711,-9.519868,1.218007,-3.159258,7.852577,0.888535,1.749111,2.724086,3.581158,3.856620,3.345022,-5.982956,7.374467,2.694268,-7.154386,-7.301742,8.617581,-7.347593,-6.497545,6.929941,9.139861,9.583196,-2.760034,9.994502,-1.724644,-9.483591,-6.027568,-8.087951,0.948443,5.724671,2.658773,-9.285717,-0.093121,7.942843,0.661383,-1.538259,-7.760879,5.421463,-5.662057,-0.646154,-1.308948,-1.251557,-1.376730,-3.050930,-6.368803,5.149638,0.906778,-4.156123,-5.951354,-2.342747,-0.423491,3.586732,-7.589732,9.676401,1.751269,-9.042683,6.363542,-0.500883,4.948987,0.895673,-3.670414,5.391970,-9.894165,4.430287,-0.984014,-6.476845,-2.617897,1.792005,-8.228908,9.187827,-5.367173,3.634792,-0.321778,2.273792,-3.720983,7.013732,-7.103707,2.232956,-0.967857,7.958871,-7.593835,2.884119,8.330979,-9.504218,-2.862263,2.330817,8.883116,-7.697603,-5.266153,3.060314,-4.683451,8.644393,-9.088334,7.347523,1.278016,1.728394,-9.819246,-4.931058,0.042261,2.129959,-3.916200,-6.747960,-5.587040,7.275647,1.817248,1.556294,1.440398,-6.723472,2.868610,-2.040220,-0.442280,2.938319,2.485148,4.817171,-3.269583,-1.952049,1.162410,-8.704452,9.513717,9.776126,-1.255106,-5.187912,8.601322,5.901091,-3.893430,-8.620683,7.441356,0.858066,0.748167,4.275895,9.046960,4.490282,2.858426,-7.392553,1.984384,2.935481,9.283608,-8.885937,-6.685204,7.181435,1.242470,5.831976,8.234340,8.129707,9.404928,-0.941501,-0.255931,-0.276847,5.532971,-6.450151,-7.378662], dtype = "float32")#candidate|2913|(320,)|const|float32
call_2912 = relay.TupleGetItem(func_1015_call(relay.reshape(const_2913.astype('float32'), [5, 8, 8]), relay.reshape(const_2913.astype('float32'), [5, 8, 8]), ), 4)
call_2914 = relay.TupleGetItem(func_1018_call(relay.reshape(const_2913.astype('float32'), [5, 8, 8]), relay.reshape(const_2913.astype('float32'), [5, 8, 8]), ), 4)
func_905_call = mod.get_global_var('func_905')
func_910_call = mutated_mod.get_global_var('func_910')
const_2917 = relay.const([-6,-8,8,3,-6,-7,6,2,7,6,-8,4,10,7,4,-10,-10,-7,-6,6,-9,-5,-8,1,-10,9,-5,2,-2,-7,10,9,8,8,8,-8,-7,-4,-1,-10,1,-1,-2,-4,-3,-3,10,2,-9,4,6,-4,4,-8,10,7,7,2,10,-4,-8,-7,10,-8,2,4,-3,-1,-6,-3,-8,2,8,-5,-9,-3,-7,-7,2,3,7,-1,8,9,-2,-2,5,-6,-5,3,-9,3,9,-10,-5,-2,-2,5,5,-4,8,-7,-8,-6,-1,9,7,5,-1,-6,10,9,3,2,9,6,1,-2,6,2,-9,9,-4,-2,9,-3], dtype = "int32")#candidate|2917|(126,)|const|int32
const_2918 = relay.const([-8.578625,2.071499,-7.856951,-0.072475,-2.523723,-7.581128,8.012474,-8.083592,-9.609543,5.141505,4.546502,-2.622533,0.208689,-4.825600,1.585743,8.626618,-1.633075,-8.318002,1.116350,-0.063030,4.659883,-5.027223,1.110634,-0.456462,7.184810,-4.648384,5.072868,-5.324106,1.090099,4.368417,-2.789670,-9.209516,-6.435896,5.740988,7.036242,8.507532,-1.018199,6.820589,-7.783146,-8.370007,-8.692346,-0.771297,6.362343,-0.521914,6.488767,7.300791,-0.436107,-0.026878,-3.263299,-3.060694,-4.221793,-6.612180,-0.262904,-2.799308,3.571702,-9.632540,1.404816,1.486376,9.280129,7.582389,-9.483390,9.237476,-2.445592,2.742533,4.651953,-3.427647,8.716874,4.974147,8.132051,-9.835295,-5.982613,-0.126834,0.638731,-3.841326,4.676351,-1.222461,-2.783385,-7.141785,5.163190,5.572583,9.521894,-6.277777,-0.331372,-3.174992,-0.450162,-9.839499,2.224539,-7.041625,6.884872,-9.934578,3.225418,-6.491082,-7.496062,-7.351601,-5.877567,-5.089402,-9.436079,-5.851329,-9.730200,-5.848652,5.757271,3.247825,4.565044,8.769799,-5.682910,8.369836,-8.542381,5.613474,-1.379810,8.431109,0.655554,-6.353152,-8.152816,-9.210853,-4.586694,6.340454,-8.168137,-6.390019,7.795299,-1.438053,0.157996,3.923179,2.626268,-2.206688,-8.621054,-5.108526,-1.487986,4.530847,8.377578,0.670958,-3.576803,3.740047,-9.730025,-4.822589,9.356898,5.335486,-9.313391,1.770850,-3.269379,3.068102,7.161231,-0.940608,2.097399,-4.739517,-8.859501,-1.712383,6.674036,3.093628,2.988679,3.092059,-1.413652,-7.222761,6.963222,-5.467766,7.443930,-0.367561,2.725265,-0.420000,3.001922,9.518478,6.902219,-3.020153,1.509378,-4.387244,-3.518764,2.494798,-3.553845,2.644585,1.456545,3.060497,-9.752391,3.452989,7.743863,-3.952735,4.463474,-4.907264,7.365985,6.725412,-1.657388,6.565748,3.281861,0.263360,-7.705288,8.810933,-3.754858,2.747653,-1.710166,-0.922886,-7.249916,-0.287262,-7.223331,-6.909205,-6.577185,-7.882771,2.293371,6.968654,-2.060059,6.344192,7.661321,7.927654,6.835214,-4.597914,9.078580,5.262585,5.758227,5.161350,-2.268923,7.544097,3.274093,8.180009,-7.374870,6.534641,3.443684,1.484300,9.551801,-7.038890,9.218243,6.333313,1.656408,9.259473,-6.032529,-1.652046,-2.029272,6.278269,4.961961,7.415090,9.684725,1.044940,7.614920,-8.918697,6.292038,5.361913,1.223667,6.179862,-0.867297,-3.625537,-5.841036,1.118503,-8.055518,-1.321867,-1.083722,1.296755,7.439406,-9.559254,-5.222843,8.026788,-7.219483,-4.955251,9.118098,-5.659022,-6.020821,3.279341,-4.416362,-0.613046,3.305891,-0.533414,-9.183071,-7.259900,-6.897028,-7.063531,4.935978,-3.704486,-4.318483,0.512738,4.968102,6.593510,-6.017520,-0.020054,-6.688489,-9.855328,9.849781,3.091690,-6.919931,0.041148,-8.224770,3.436009,-9.265833,0.815177,1.432889,-7.021768,8.823222,-4.595391,-9.674573,-8.380666,3.163699,9.929400,9.086414,-1.989480,-7.067143,4.296607,5.127679,-1.518353,-5.779630,4.754649,-9.296444,-1.072047,9.869397,-6.987965,1.198263,-3.316398,0.527398,-2.146213,-7.753671,-6.835620,-7.382613,-5.956086,5.288907,2.700014,-2.157515,7.365537,6.408471,-8.335074,-1.522456,-6.543240,4.385327,0.170350,-9.402209,-3.878745,-0.364293,9.401790,-2.526300,9.864224,-2.435246,4.544950,6.066311,-5.821116,8.983019,6.635570,6.810241,3.912778,1.504010,3.391585,-2.981491,-0.188300,-8.235499,-0.049895,1.530239,-1.269136,-4.794299,0.241757,-3.712973,-2.720676,-7.566327,-8.198746,-0.347649,2.948154,-6.675865,8.641262,-5.755293,7.190168,-1.392205,0.146755,1.145344,3.035615,6.693189,0.699592,-7.422697,7.249854,-5.847700,-5.525634,-9.759707,-3.083492,-3.098047,9.840932,0.266313,-0.301104,-7.990089,-7.091973,7.960376,-6.867942,-4.691906,6.621735,2.019201,5.327339,-2.800131,-4.402288,7.484350,4.505899,4.159889,-2.835905,7.032730,-7.023604,-8.490215,-1.536905,-5.025912,2.619099,-1.173166,-1.955589,6.616235,6.661474,5.693035,-8.457189,-8.416829,2.513084,9.854109,9.985322,-8.353324,-8.085527,-7.060413,-3.587932,5.143067,9.460162,-9.753315,-9.285037,1.174004,4.658571,2.070327,-1.535702,4.663070,0.292317,6.431799,-6.317607,-1.316858,0.035266,2.180986,-3.592706,8.959155,-4.813205,2.428643,4.289733,6.115708,8.502612,7.755261,-4.391678,7.936327,4.255771,-7.979175,-0.691820,-4.297885,0.372650,-8.443790,5.458547,8.404850,3.252091,-3.510973,-3.508073,-3.150923,-4.134420,0.703935,-7.669518,4.864871,6.938317,0.015770,-0.673471,0.034240,3.541564,0.984841,1.490001,5.432830,0.847881,-0.154245,2.918835,-8.771404,-4.518648,-7.329557,-3.281106,-4.976190,-1.205637,-2.204086,8.117892,-7.690286,7.156479,1.114584,6.902086,2.788115,-8.765285,-0.967106,-5.578599,-4.264354,-3.936903,-4.819359,-5.895973,-7.078959,-7.414114,8.450271,0.641051,2.351525,-1.978773,9.228995,4.131115,-9.609751,-0.900441,6.173886,3.227504,8.947002,-8.671666,2.990407,-8.663449,7.853080,-4.610198,0.064743,5.213675,-5.617984,9.992790,6.788231,-1.464174,2.216234,-6.839520,-2.613415,-5.174081,5.454808,2.918599,4.590332,-6.820473,-0.078433,6.960322,-3.090719,-5.765420,-5.283655,3.310017,-2.071049,-4.555509,-2.966304,-0.120611,-3.485258,8.582790,-7.333614,-6.144740,-2.250327,-4.646597,1.788942,-6.236696,-4.275553,-3.971068,8.657698,-5.918276,-7.828272,5.536210,9.758595,1.883656,-0.668375,4.170348,3.300671,-3.527617,5.504033,-8.540130,-1.807483,-5.226835,-7.636450,-2.296493,-5.964756,7.490093,9.801408,-0.780366,2.896673,-8.711917,-7.910954,-4.362689,-7.929298,2.233491,5.433301,-8.020763,7.275327,7.227356,-1.119650,1.139052,-5.037594,4.886956,2.220325,1.001743,5.726654,-1.092906,5.181050,0.032777,9.318746,3.762376,-3.672522,-7.559075,6.691320,6.897310,6.200478,-5.871243,-1.941182,9.677843,2.211928,-2.758271,7.876879,-1.487975,5.009566,-7.503662,8.022739,2.879762,4.801962,0.745783,5.675932,-8.496659,2.211756,8.846113,-5.636362,6.716286,5.277087,-2.717924,-7.294482,8.171934,-2.002919,-1.395737,-9.250643,-7.898302,0.475014,-0.596493,-1.121882,-4.841953,2.135709,6.480356,-4.980197,-6.416686,-3.933444,-6.506960,8.454122,-6.382916,5.768816,0.304147,5.626806,-1.978924,4.659282,2.798981,5.441695,4.521219,4.765051,6.246018,1.147792,6.129695,-1.938977,-3.195617,-7.888137,-9.035608,1.251614,1.226198,0.174789,-8.302743,-8.331716,-2.506099,3.411581,-2.047799,5.942169,-0.299375,3.472382,-8.351661,-3.048857,-0.672082,-3.471609,-1.420631,-1.538773,-0.940141,2.000654,5.423124,-8.417426,-1.200497,2.883608,6.420781,-1.790925,-3.983827,2.248573,3.605809,0.086953,-1.584293,-5.774015,-9.755719,-9.723040,-6.776560,2.420440,4.035037,-3.406594,2.351205,5.919324,-4.407890,-0.148106,4.300917,4.761078,0.731611,-9.835742,-2.608261,3.759986,-0.509806,9.731942,0.067695,-0.774462,4.222687,-5.349428,-1.945075,3.916055,6.744091,2.236834,4.631297,-5.838955,-0.777355,6.499994,0.391932,9.260857,-1.400863,4.768782,3.899133,1.365753,-5.358499,3.898800,1.844290,5.252732,-5.701386,8.369774,2.217301,0.812734,6.607486,0.288286,3.927423,-1.588714,4.595624,8.904639,5.663144,8.168699,9.928105,-4.860018,1.793072,9.292747,2.865829,-1.351574,-5.909003,-7.917745,-1.111455,2.007703,-4.015934,3.334884,7.066352,-8.482892,6.189373,-8.407342,-1.061759,6.384831,-9.403141,4.300073,-2.247045,-7.842106,4.734209,-0.012684,-9.788058,3.106722,3.061655,3.433716,-1.881432,1.151517,2.481247,-7.610124,-6.405298,-3.998928,-4.272914,-3.413310,4.037737,-0.738496,9.429650,-8.268266,-7.350939,-6.341693,-8.055437,-8.075379,5.746243,2.495018,7.569346,-2.912503,5.250057,-4.988621,4.655611,-4.976335,1.665832,6.210289,8.180648,1.541709,-8.334202,1.827308,5.381708], dtype = "float64")#candidate|2918|(768,)|const|float64
call_2916 = relay.TupleGetItem(func_905_call(relay.reshape(const_2917.astype('int32'), [14, 3, 3]), relay.reshape(const_2917.astype('int32'), [14, 3, 3]), relay.reshape(const_2918.astype('float64'), [2, 384]), ), 3)
call_2919 = relay.TupleGetItem(func_910_call(relay.reshape(const_2917.astype('int32'), [14, 3, 3]), relay.reshape(const_2917.astype('int32'), [14, 3, 3]), relay.reshape(const_2918.astype('float64'), [2, 384]), ), 3)
func_2885_call = mod.get_global_var('func_2885')
func_2887_call = mutated_mod.get_global_var('func_2887')
call_2923 = relay.TupleGetItem(func_2885_call(), 0)
call_2924 = relay.TupleGetItem(func_2887_call(), 0)
output = relay.Tuple([call_2905,call_2907,uop_2910,call_2912,const_2913,call_2916,const_2917,const_2918,call_2923,])
output2 = relay.Tuple([call_2906,call_2909,uop_2910,call_2914,const_2913,call_2919,const_2917,const_2918,call_2924,])
func_2929 = relay.Function([], output)
mod['func_2929'] = func_2929
mod = relay.transform.InferType()(mod)
mutated_mod['func_2929'] = func_2929
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2929_call = mutated_mod.get_global_var('func_2929')
call_2930 = func_2929_call()
output = call_2930
func_2931 = relay.Function([], output)
mutated_mod['func_2931'] = func_2931
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2885_call = mod.get_global_var('func_2885')
func_2887_call = mutated_mod.get_global_var('func_2887')
call_2941 = relay.TupleGetItem(func_2885_call(), 1)
call_2942 = relay.TupleGetItem(func_2887_call(), 1)
func_2833_call = mod.get_global_var('func_2833')
func_2838_call = mutated_mod.get_global_var('func_2838')
var_2944 = relay.var("var_2944", dtype = "float64", shape = (4,))#candidate|2944|(4,)|var|float64
var_2945 = relay.var("var_2945", dtype = "uint32", shape = (2016,))#candidate|2945|(2016,)|var|uint32
const_2946 = relay.const([3,-5], dtype = "int8")#candidate|2946|(2,)|const|int8
call_2943 = relay.TupleGetItem(func_2833_call(relay.reshape(var_2944.astype('float64'), [4, 1, 1]), relay.reshape(var_2945.astype('uint32'), [1008, 2]), relay.reshape(const_2946.astype('int8'), [2, 1]), ), 3)
call_2947 = relay.TupleGetItem(func_2838_call(relay.reshape(var_2944.astype('float64'), [4, 1, 1]), relay.reshape(var_2945.astype('uint32'), [1008, 2]), relay.reshape(const_2946.astype('int8'), [2, 1]), ), 3)
output = relay.Tuple([call_2941,call_2943,var_2944,var_2945,const_2946,])
output2 = relay.Tuple([call_2942,call_2947,var_2944,var_2945,const_2946,])
func_2955 = relay.Function([var_2944,var_2945,], output)
mod['func_2955'] = func_2955
mod = relay.transform.InferType()(mod)
var_2956 = relay.var("var_2956", dtype = "float64", shape = (4,))#candidate|2956|(4,)|var|float64
var_2957 = relay.var("var_2957", dtype = "uint32", shape = (2016,))#candidate|2957|(2016,)|var|uint32
output = func_2955(var_2956,var_2957,)
func_2958 = relay.Function([var_2956,var_2957,], output)
mutated_mod['func_2958'] = func_2958
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3008 = relay.var("var_3008", dtype = "bool", shape = ())#candidate|3008|()|var|bool
var_3009 = relay.var("var_3009", dtype = "bool", shape = (13, 15, 1))#candidate|3009|(13, 15, 1)|var|bool
bop_3010 = relay.logical_and(var_3008.astype('bool'), var_3009.astype('bool')) # shape=(13, 15, 1)
output = bop_3010
output2 = bop_3010
func_3021 = relay.Function([var_3008,var_3009,], output)
mod['func_3021'] = func_3021
mod = relay.transform.InferType()(mod)
var_3022 = relay.var("var_3022", dtype = "bool", shape = ())#candidate|3022|()|var|bool
var_3023 = relay.var("var_3023", dtype = "bool", shape = (13, 15, 1))#candidate|3023|(13, 15, 1)|var|bool
output = func_3021(var_3022,var_3023,)
func_3024 = relay.Function([var_3022,var_3023,], output)
mutated_mod['func_3024'] = func_3024
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3045 = relay.var("var_3045", dtype = "float64", shape = (1, 13, 5))#candidate|3045|(1, 13, 5)|var|float64
const_3046 = relay.const([[[4.034283,3.582917,-9.234280,2.815271,5.647476],[-1.580441,9.653727,-6.961980,-3.607246,-3.335280],[-1.370575,-7.946443,-1.273911,-6.256757,-9.312652],[6.377919,7.948392,-1.267176,-7.113319,-2.149410],[3.438052,-2.655566,-3.066977,4.381026,4.825611],[-4.603912,2.359416,8.203898,8.305334,-0.390315],[7.751920,6.690544,-1.148400,5.937099,3.440433],[-1.588488,-7.502386,-1.249898,-6.442048,2.486781],[7.119082,0.766796,-1.444720,8.709888,-1.412135],[3.317777,1.538886,8.545478,-3.327682,-2.161389],[-0.303944,-6.135870,2.978200,3.816864,1.052894],[-0.479678,-6.824317,1.806982,-9.850884,-7.119423],[5.239161,6.767439,5.258907,-4.898919,0.090751]],[[2.227294,-2.759532,-8.007925,-7.828824,4.316934],[-1.778418,1.549170,4.111462,0.857583,4.528236],[3.431693,8.442981,5.439835,0.527598,-9.112167],[-8.645001,-3.783671,3.148787,5.065187,-4.210374],[3.091606,-6.788882,6.997716,-4.091141,8.365261],[-1.109195,-4.663102,8.241582,-9.208975,1.023886],[6.770048,0.503700,-1.865382,-2.467169,-0.021668],[-8.763421,9.563925,-6.062522,5.843601,1.268272],[-1.781192,4.854701,1.325420,-0.350430,2.710857],[-8.468956,-7.621279,-3.273754,3.253349,-6.264816],[5.405456,1.339440,6.639801,9.885351,-2.541187],[6.887696,-8.972364,3.859898,-5.865942,-3.175425],[-6.826897,-0.255588,-9.061998,2.330247,-0.350080]],[[6.049010,7.947030,-8.146606,1.802787,9.760815],[4.779396,-2.815299,8.961749,5.690455,-2.230575],[8.932132,9.169773,0.526513,-8.706489,8.699472],[-2.971124,-0.174405,3.810725,-7.649660,-9.292032],[2.436530,-8.482937,7.679037,8.159559,8.734713],[-2.818773,-6.824150,2.855100,8.683179,1.420393],[-4.937722,-1.094290,0.039368,1.702846,-1.621122],[0.831573,9.845806,4.450579,7.020259,-0.992320],[-7.943893,6.108698,-7.521143,-7.410626,-4.871924],[-1.465695,1.945950,0.781037,-6.527648,-1.452486],[-1.433006,-7.161317,-5.105928,-3.659214,7.493414],[-2.256288,-6.257937,-6.820435,-7.445468,-9.602415],[-1.994541,1.036409,0.460970,-5.727174,-6.462417]],[[-8.866821,-4.914728,-6.710966,2.025640,-3.548956],[8.403167,-9.807280,-8.882200,-3.950865,-7.548114],[5.874364,7.635958,-1.175042,3.940671,6.610617],[-4.879337,-4.990268,-1.743165,2.840651,-6.097185],[-0.099952,-8.474870,7.282879,-1.441538,-6.848619],[-4.866912,6.936717,-0.830417,5.720938,1.797516],[6.340578,-3.317618,-6.026872,1.856453,-9.531843],[-0.980926,1.370798,-7.807199,4.010093,6.126093],[2.583581,-1.701104,8.031131,-2.975794,-9.505992],[2.210413,9.963740,-0.744343,7.399190,8.832827],[8.766250,-1.146739,3.124924,1.849495,0.552578],[-5.495241,-1.141687,-1.684836,4.699565,-1.315230],[-4.961731,-4.745444,-3.048695,1.900459,-5.607511]],[[5.797655,-4.303860,-8.725154,-3.777145,6.766468],[-4.078070,-2.879318,-4.753101,2.143042,-1.744775],[1.208336,2.037100,-6.499444,-9.150173,6.432485],[4.328853,-9.058901,5.928112,6.943440,-5.983907],[5.308645,-1.268051,-2.700784,-3.744514,-9.359524],[1.300036,2.650596,2.868318,-2.087272,-7.285002],[-4.983151,0.517938,4.481897,-2.244448,-8.069527],[5.749093,4.072787,-0.595790,-3.855944,0.968496],[5.240678,9.402606,-1.402136,-1.908482,-2.853077],[-6.063543,-5.945711,-6.471193,-2.196152,-8.211178],[1.319945,2.390969,0.271744,-0.716129,-0.911231],[7.499588,0.506078,0.038500,0.290544,-6.319641],[-9.263357,5.515559,-2.340886,-1.021782,-8.161325]],[[-7.520238,8.838567,-8.824037,6.866674,-7.307418],[2.764209,8.185829,-8.902228,-4.248492,-8.854315],[-6.825215,7.788150,-1.129759,3.366944,9.726237],[3.117434,9.085258,6.888701,-1.146356,3.114758],[-9.627365,-5.914263,8.060099,-4.516621,-7.289129],[-2.976637,8.205770,-0.334489,-9.666196,6.632963],[7.643782,2.617616,6.025892,5.923464,8.908918],[-8.819878,2.394592,1.673884,-3.819583,-3.950423],[-0.431693,6.712710,-7.786022,4.157475,4.047424],[-3.984135,-1.912286,5.096556,-4.762528,9.888698],[9.158155,-7.587208,-9.005272,4.409154,6.037273],[0.257865,5.498219,-0.110096,5.541627,-5.778115],[-1.364410,2.037978,-1.227476,-8.215692,6.280896]],[[-7.713153,8.349995,1.190707,-4.469846,-9.252868],[-2.068707,7.054381,-7.752414,-3.021479,-7.291147],[-4.795776,4.441252,7.384170,7.992132,9.058202],[2.656961,3.055434,-1.504463,-8.812640,-6.098884],[-6.692166,-3.601629,-4.464693,0.712037,-1.329593],[1.200544,-4.703837,3.039734,-7.021464,3.379930],[0.699528,4.055312,-6.007540,-6.131124,-0.836652],[6.093579,9.301571,-7.204537,2.519488,-2.391208],[7.846044,-5.705284,3.893288,3.350429,-1.515332],[0.656761,1.501850,3.780967,-7.131199,-0.445649],[-0.699602,3.553527,-1.228168,1.341277,-9.605356],[7.426172,8.344214,1.815854,5.736156,-4.747021],[-2.996057,-2.619373,-0.993733,7.932675,8.793771]],[[0.527085,5.206436,8.591153,-1.680503,7.536166],[6.914095,1.235569,5.949985,1.032389,5.100252],[-8.222046,6.116146,-4.884848,-1.205534,-7.708783],[9.425757,8.851300,-9.410670,-5.710727,3.081007],[3.444326,5.632940,1.175708,-7.396968,1.222401],[-5.646445,2.640429,-9.424636,9.789060,4.977696],[-5.861921,2.058660,5.656602,8.336629,5.076832],[-8.486147,9.602437,1.226973,-3.632477,2.632318],[7.331441,1.520640,3.912014,-8.841581,1.160199],[-3.419166,1.780189,3.175299,1.026669,-4.130101],[-2.187447,-4.916342,-6.508664,-3.008373,8.059892],[2.133010,-7.795963,1.604983,-8.925234,-6.487900],[2.219937,-4.769761,7.041853,8.046806,-0.176635]],[[1.042500,-9.055993,-0.182793,7.222593,1.059577],[-9.732745,4.753665,-1.077607,-4.712103,6.918293],[-5.572849,3.269508,1.970082,-5.594683,6.012753],[-0.538709,8.878331,-7.422116,-4.722311,7.160913],[-3.442589,-2.475387,-1.132963,-2.781440,4.714974],[9.615950,-6.199940,-6.748341,5.763077,4.401431],[0.139806,9.102116,-8.604764,-3.407498,5.975959],[3.352570,8.206461,-6.130545,-2.284102,-4.048558],[-6.383717,8.280490,-4.000226,-6.415060,-1.495585],[9.606083,4.518612,7.818230,-6.956645,-2.539339],[3.474910,-6.757550,5.576327,-6.188097,7.035426],[-4.998160,-8.381389,5.274180,4.802794,8.230248],[4.747206,-6.238868,3.986907,-8.786740,6.188739]],[[-2.620087,-8.604966,-0.108648,2.253074,4.143113],[1.417774,-3.070589,1.089684,3.061808,1.826659],[8.866967,0.925762,6.305827,9.541244,-6.938810],[8.633907,4.232074,8.508988,1.333119,-2.895029],[-3.289710,-4.191618,5.514794,-2.541576,4.786708],[5.631726,-2.176140,-5.668528,-1.396921,8.694093],[-5.560622,1.927749,3.199503,3.551831,7.236420],[2.272716,-9.158093,-3.348246,-8.501098,-3.866979],[-2.533298,-2.593816,-4.107843,-5.358657,-2.217104],[4.217804,-6.514558,-9.032058,-3.899551,0.312198],[7.361394,2.456701,-8.922056,6.788699,-4.663181],[-2.583803,-5.745232,9.625979,1.658382,2.398636],[8.853348,6.312783,4.653058,4.729958,0.470890]],[[5.722091,-4.226122,-7.433865,-1.389826,7.373684],[8.352405,3.994695,-3.291800,-8.905570,-8.779938],[2.773640,9.871360,-4.322545,-6.413918,-1.055242],[-1.306780,-6.122669,-3.926583,4.788600,-3.154646],[6.175711,8.164121,5.205520,2.000171,9.796737],[3.537463,6.211871,8.553721,1.934740,-8.448757],[-9.348657,8.022058,1.628471,5.405360,-7.055740],[8.771563,-9.604504,-1.518618,-4.116436,6.909191],[-2.876960,-8.081026,8.973980,7.534732,2.574157],[-2.553149,-7.286331,-4.712162,5.831590,-2.692402],[5.092035,5.060867,-4.638251,-7.287891,0.258341],[0.715966,-9.757913,-7.493409,5.036294,5.447419],[0.421104,-4.356015,0.419000,6.613699,2.171272]],[[9.106893,2.496230,-2.310140,-3.948999,-0.077122],[-3.214074,5.951995,6.515918,0.703971,7.424884],[2.679862,-8.658614,-6.214205,-3.920442,3.421288],[-6.678079,-0.277924,8.245107,3.374719,2.273532],[-3.220276,6.832700,2.703701,4.005067,-3.384041],[4.685460,2.133094,6.843495,2.135594,9.575639],[3.770343,8.127114,5.009647,-9.715015,5.513390],[-3.783983,-1.048134,7.001138,-0.178962,-4.044852],[-9.500813,-7.971955,9.053699,5.535046,9.287442],[9.374474,-4.558216,-4.768871,-4.880753,2.335207],[9.350699,9.812236,4.666396,4.561700,5.843854],[-3.291822,6.307082,0.752586,3.018096,9.106892],[8.393913,6.992624,-1.728164,0.905287,6.884601]],[[-5.102061,-6.154623,-5.266326,-8.902660,3.424990],[0.696905,8.694371,-2.253252,8.299906,-7.575181],[-4.027592,-3.692881,3.064530,0.301642,2.589431],[1.863354,7.874127,3.244979,-2.615256,8.500815],[8.879498,0.604427,6.207180,5.166841,8.805400],[-9.074124,4.708640,-7.083276,2.871586,1.860094],[-4.080132,-4.801391,-8.142559,2.887627,2.649223],[-9.072236,7.298678,-9.902852,9.506537,5.232446],[4.197436,-0.351451,-1.724673,9.138130,-8.275693],[-0.357971,-4.308309,7.526870,-9.368356,0.828679],[4.911935,-2.621105,1.715250,-8.547201,-2.730142],[-3.234032,5.624781,-1.741429,8.230885,5.247171],[-3.457580,-3.242746,-4.249345,8.894330,-3.146910]],[[-5.106618,-2.093481,-6.562305,1.650349,-2.196968],[-4.475780,1.234558,5.526439,-1.856158,-2.870319],[8.758527,2.381878,9.525895,3.421083,7.225631],[4.361085,6.294689,-5.317194,5.744726,-4.798511],[-8.211816,-5.248133,-9.286604,3.750670,-3.236530],[-2.078331,5.306053,4.359200,1.862382,9.668619],[-1.210490,6.850939,4.945046,7.655365,3.228524],[-0.238849,5.636154,-6.762922,9.364251,-0.662886],[7.957785,6.834968,-4.708317,5.123759,9.060089],[-4.098279,8.631089,2.084175,-8.572520,7.607492],[1.005476,1.788765,6.795746,-7.010554,0.389958],[-4.811464,-9.248510,3.435002,7.040687,-9.351067],[-3.902378,-8.161467,-1.680435,-6.327099,9.931666]]], dtype = "float64")#candidate|3046|(14, 13, 5)|const|float64
bop_3047 = relay.power(var_3045.astype('float64'), const_3046.astype('float64')) # shape=(14, 13, 5)
output = bop_3047
output2 = bop_3047
func_3051 = relay.Function([var_3045,], output)
mod['func_3051'] = func_3051
mod = relay.transform.InferType()(mod)
mutated_mod['func_3051'] = func_3051
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3052 = relay.var("var_3052", dtype = "float64", shape = (1, 13, 5))#candidate|3052|(1, 13, 5)|var|float64
func_3051_call = mutated_mod.get_global_var('func_3051')
call_3053 = func_3051_call(var_3052)
output = call_3053
func_3054 = relay.Function([var_3052], output)
mutated_mod['func_3054'] = func_3054
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2929_call = mod.get_global_var('func_2929')
func_2931_call = mutated_mod.get_global_var('func_2931')
call_3079 = relay.TupleGetItem(func_2929_call(), 2)
call_3080 = relay.TupleGetItem(func_2931_call(), 2)
output = relay.Tuple([call_3079,])
output2 = relay.Tuple([call_3080,])
func_3081 = relay.Function([], output)
mod['func_3081'] = func_3081
mod = relay.transform.InferType()(mod)
mutated_mod['func_3081'] = func_3081
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3081_call = mutated_mod.get_global_var('func_3081')
call_3082 = func_3081_call()
output = call_3082
func_3083 = relay.Function([], output)
mutated_mod['func_3083'] = func_3083
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2801_call = mod.get_global_var('func_2801')
func_2803_call = mutated_mod.get_global_var('func_2803')
call_3101 = func_2801_call()
call_3102 = func_2801_call()
output = relay.Tuple([call_3101,])
output2 = relay.Tuple([call_3102,])
func_3107 = relay.Function([], output)
mod['func_3107'] = func_3107
mod = relay.transform.InferType()(mod)
output = func_3107()
func_3108 = relay.Function([], output)
mutated_mod['func_3108'] = func_3108
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2929_call = mod.get_global_var('func_2929')
func_2931_call = mutated_mod.get_global_var('func_2931')
call_3142 = relay.TupleGetItem(func_2929_call(), 7)
call_3143 = relay.TupleGetItem(func_2931_call(), 7)
func_3021_call = mod.get_global_var('func_3021')
func_3024_call = mutated_mod.get_global_var('func_3024')
var_3157 = relay.var("var_3157", dtype = "bool", shape = ())#candidate|3157|()|var|bool
var_3158 = relay.var("var_3158", dtype = "bool", shape = (195,))#candidate|3158|(195,)|var|bool
call_3156 = func_3021_call(relay.reshape(var_3157.astype('bool'), []), relay.reshape(var_3158.astype('bool'), [13, 15, 1]), )
call_3159 = func_3021_call(relay.reshape(var_3157.astype('bool'), []), relay.reshape(var_3158.astype('bool'), [13, 15, 1]), )
output = relay.Tuple([call_3142,call_3156,var_3157,var_3158,])
output2 = relay.Tuple([call_3143,call_3159,var_3157,var_3158,])
func_3168 = relay.Function([var_3157,var_3158,], output)
mod['func_3168'] = func_3168
mod = relay.transform.InferType()(mod)
var_3169 = relay.var("var_3169", dtype = "bool", shape = ())#candidate|3169|()|var|bool
var_3170 = relay.var("var_3170", dtype = "bool", shape = (195,))#candidate|3170|(195,)|var|bool
output = func_3168(var_3169,var_3170,)
func_3171 = relay.Function([var_3169,var_3170,], output)
mutated_mod['func_3171'] = func_3171
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2801_call = mod.get_global_var('func_2801')
func_2803_call = mutated_mod.get_global_var('func_2803')
call_3182 = func_2801_call()
call_3183 = func_2801_call()
func_905_call = mod.get_global_var('func_905')
func_910_call = mutated_mod.get_global_var('func_910')
var_3195 = relay.var("var_3195", dtype = "int32", shape = (126,))#candidate|3195|(126,)|var|int32
var_3196 = relay.var("var_3196", dtype = "float64", shape = (2, 384))#candidate|3196|(2, 384)|var|float64
call_3194 = relay.TupleGetItem(func_905_call(relay.reshape(var_3195.astype('int32'), [14, 3, 3]), relay.reshape(var_3195.astype('int32'), [14, 3, 3]), relay.reshape(var_3196.astype('float64'), [2, 384]), ), 3)
call_3197 = relay.TupleGetItem(func_910_call(relay.reshape(var_3195.astype('int32'), [14, 3, 3]), relay.reshape(var_3195.astype('int32'), [14, 3, 3]), relay.reshape(var_3196.astype('float64'), [2, 384]), ), 3)
func_3051_call = mod.get_global_var('func_3051')
func_3054_call = mutated_mod.get_global_var('func_3054')
var_3210 = relay.var("var_3210", dtype = "float64", shape = (13, 5))#candidate|3210|(13, 5)|var|float64
call_3209 = func_3051_call(relay.reshape(var_3210.astype('float64'), [1, 13, 5]))
call_3211 = func_3051_call(relay.reshape(var_3210.astype('float64'), [1, 13, 5]))
var_3216 = relay.var("var_3216", dtype = "float64", shape = (14, 13, 5))#candidate|3216|(14, 13, 5)|var|float64
bop_3217 = relay.right_shift(call_3209.astype('int8'), relay.reshape(var_3216.astype('int8'), relay.shape_of(call_3209))) # shape=(14, 13, 5)
bop_3220 = relay.right_shift(call_3211.astype('int8'), relay.reshape(var_3216.astype('int8'), relay.shape_of(call_3211))) # shape=(14, 13, 5)
output = relay.Tuple([call_3182,call_3194,var_3195,var_3196,var_3210,bop_3217,])
output2 = relay.Tuple([call_3183,call_3197,var_3195,var_3196,var_3210,bop_3220,])
func_3223 = relay.Function([var_3195,var_3196,var_3210,var_3216,], output)
mod['func_3223'] = func_3223
mod = relay.transform.InferType()(mod)
mutated_mod['func_3223'] = func_3223
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3223_call = mutated_mod.get_global_var('func_3223')
var_3225 = relay.var("var_3225", dtype = "int32", shape = (126,))#candidate|3225|(126,)|var|int32
var_3226 = relay.var("var_3226", dtype = "float64", shape = (2, 384))#candidate|3226|(2, 384)|var|float64
var_3227 = relay.var("var_3227", dtype = "float64", shape = (13, 5))#candidate|3227|(13, 5)|var|float64
var_3228 = relay.var("var_3228", dtype = "float64", shape = (14, 13, 5))#candidate|3228|(14, 13, 5)|var|float64
call_3224 = func_3223_call(var_3225,var_3226,var_3227,var_3228,)
output = call_3224
func_3229 = relay.Function([var_3225,var_3226,var_3227,var_3228,], output)
mutated_mod['func_3229'] = func_3229
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2885_call = mod.get_global_var('func_2885')
func_2887_call = mutated_mod.get_global_var('func_2887')
call_3274 = relay.TupleGetItem(func_2885_call(), 1)
call_3275 = relay.TupleGetItem(func_2887_call(), 1)
output = call_3274
output2 = call_3275
func_3296 = relay.Function([], output)
mod['func_3296'] = func_3296
mod = relay.transform.InferType()(mod)
mutated_mod['func_3296'] = func_3296
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3296_call = mutated_mod.get_global_var('func_3296')
call_3297 = func_3296_call()
output = call_3297
func_3298 = relay.Function([], output)
mutated_mod['func_3298'] = func_3298
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3107_call = mod.get_global_var('func_3107')
func_3108_call = mutated_mod.get_global_var('func_3108')
call_3310 = relay.TupleGetItem(func_3107_call(), 0)
call_3311 = relay.TupleGetItem(func_3108_call(), 0)
output = relay.Tuple([call_3310,])
output2 = relay.Tuple([call_3311,])
func_3316 = relay.Function([], output)
mod['func_3316'] = func_3316
mod = relay.transform.InferType()(mod)
output = func_3316()
func_3317 = relay.Function([], output)
mutated_mod['func_3317'] = func_3317
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3296_call = mod.get_global_var('func_3296')
func_3298_call = mutated_mod.get_global_var('func_3298')
call_3392 = func_3296_call()
call_3393 = func_3296_call()
output = relay.Tuple([call_3392,])
output2 = relay.Tuple([call_3393,])
func_3399 = relay.Function([], output)
mod['func_3399'] = func_3399
mod = relay.transform.InferType()(mod)
output = func_3399()
func_3400 = relay.Function([], output)
mutated_mod['func_3400'] = func_3400
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3296_call = mod.get_global_var('func_3296')
func_3298_call = mutated_mod.get_global_var('func_3298')
call_3435 = func_3296_call()
call_3436 = func_3296_call()
func_3051_call = mod.get_global_var('func_3051')
func_3054_call = mutated_mod.get_global_var('func_3054')
const_3447 = relay.const([-3.820415,1.597233,-9.049612,4.532245,3.071837,6.374761,-4.441978,-4.829851,1.703253,-8.717748,6.497482,-8.940228,-2.864288,-6.924189,-1.449039,-9.566490,9.916075,-0.998555,7.142432,2.116545,8.066058,7.429333,-1.332964,-6.620929,-8.587464,-1.259736,-5.333160,-8.381152,-1.472755,-0.002327,-4.638147,0.444877,6.644776,8.133414,4.859583,7.252481,-1.451345,1.695037,-6.528995,-2.434318,-9.967869,-1.772154,6.192251,-0.505971,-1.278175,-9.245101,2.566970,-9.522496,7.257042,-3.646668,-1.659971,-2.759836,-8.127588,2.967555,2.887267,3.352338,-1.974651,0.290842,9.460005,6.684766,-8.666865,-8.588828,5.428551,-9.872840,7.903066], dtype = "float64")#candidate|3447|(65,)|const|float64
call_3446 = func_3051_call(relay.reshape(const_3447.astype('float64'), [1, 13, 5]))
call_3448 = func_3051_call(relay.reshape(const_3447.astype('float64'), [1, 13, 5]))
uop_3453 = relay.sin(call_3446.astype('float64')) # shape=(14, 13, 5)
uop_3455 = relay.sin(call_3448.astype('float64')) # shape=(14, 13, 5)
func_905_call = mod.get_global_var('func_905')
func_910_call = mutated_mod.get_global_var('func_910')
const_3458 = relay.const([[-5],[-4],[-9],[1],[-1],[-3],[-2],[-3],[-8],[-9],[6],[-1],[-5],[-2],[-8],[-5],[-3],[-3],[-6],[-4],[-3],[-7],[5],[-9],[8],[6],[-6],[-1],[-1],[-6],[-7],[-3],[-2],[3],[-3],[4],[-3],[1],[2],[1],[-8],[1],[3],[4],[7],[6],[-3],[-6],[-7],[6],[7],[4],[-10],[10],[-4],[1],[7],[7],[8],[-5],[-1],[10],[-1],[-2],[7],[-6],[7],[-4],[6],[-10],[-2],[-4],[5],[-10],[-3],[7],[-7],[-10],[5],[-7],[-2],[-5],[-5],[-6],[3],[-3],[9],[6],[9],[6],[-3],[5],[-1],[-10],[-7],[-9],[10],[-7],[-4],[-5],[-1],[2],[6],[-3],[-5],[4],[-1],[10],[4],[-6],[-7],[-1],[10],[-1],[1],[9],[-6],[1],[2],[4],[2],[-7],[-7],[-4],[-7],[3]], dtype = "int32")#candidate|3458|(126, 1)|const|int32
const_3459 = relay.const([8.165296,4.486133,-9.092518,-5.587348,8.840715,-6.617077,-9.778456,8.048140,-0.165437,-3.630487,6.504446,-3.588179,9.256268,2.701560,-0.540840,6.314596,-8.499030,-4.459835,-5.409642,8.925424,-2.052781,5.467294,1.444894,2.008828,7.805696,-4.840161,1.975077,6.511754,-8.898000,0.416803,-9.093774,-9.378125,-1.250338,5.817950,0.947422,-9.968928,7.380194,6.263063,5.323415,-0.949968,-2.068555,6.446290,2.802062,-5.703042,-1.963212,-4.565888,8.008562,1.574276,-9.409846,-9.022875,-4.477105,8.898611,-9.486314,-5.111178,-6.782654,9.436446,0.313294,-8.814052,4.857601,-5.211719,9.643694,9.366464,-7.857277,-4.724225,0.938643,-1.977429,5.243341,7.786958,-0.655211,0.073038,-5.587511,8.199504,-4.283649,7.641382,7.524585,6.451815,-1.443624,0.592590,8.362449,6.885445,-2.124685,-8.894521,-6.988254,6.227058,6.505658,3.610745,3.417793,1.724852,-9.414059,-9.731360,7.857674,-3.523783,-4.414312,-4.497568,0.720342,-2.868187,7.003560,-8.455601,0.740742,8.594799,-9.051597,-7.573084,9.197251,2.493472,-4.913059,1.854943,4.538229,-8.579018,8.490410,-5.066044,-2.207332,-4.378677,7.513742,5.342602,2.338654,-1.457428,4.118523,6.059803,-0.662060,7.834466,-3.410790,-2.234813,-6.378575,4.938570,0.326114,5.966380,7.245622,-6.048543,-5.773182,7.304792,-5.658725,3.034769,-9.725018,-5.434485,-5.565111,-7.234838,4.665459,-3.195712,2.367877,2.491431,3.207388,-9.584095,0.435081,-3.303223,2.285806,1.052773,4.991637,1.905009,1.455021,-1.106009,5.757454,9.018784,-3.345038,5.512934,6.230710,-2.265230,4.990626,8.408386,2.327101,-8.900994,9.081166,-5.823427,-9.729591,4.995400,-4.899344,1.580855,-7.214766,-5.327019,3.109456,-9.002695,-4.862565,1.625040,4.926382,-5.578401,-1.848587,5.442149,-7.580214,-9.466658,-5.702109,1.141024,-8.126132,-7.267839,6.941151,8.694880,-2.508942,8.898747,-7.985758,-4.156652,-4.594184,5.811574,7.861588,-4.082582,-4.222571,3.454816,-9.649798,8.245837,5.986539,0.357617,-6.975257,2.713761,-5.188737,-4.845119,-0.836067,0.834320,5.841588,5.352432,5.969101,3.982985,1.013803,-7.295731,8.626504,-1.697790,-9.834894,5.479885,-1.499733,6.960600,1.608953,4.220433,0.163719,-8.898122,6.472153,1.763797,-4.517138,1.386170,2.002889,0.948960,0.704526,-9.270957,-9.476183,3.367515,-5.166161,8.246820,-3.678100,6.635303,7.732518,-7.867709,-2.064500,-2.911179,-5.645957,-0.232362,3.407217,-9.586808,5.260447,-9.564951,-8.232531,-6.392715,2.288239,4.149239,-4.137093,5.245520,-7.800319,3.553089,3.080595,7.174439,1.854019,-3.891769,-6.251794,6.794192,1.652111,4.772660,1.729446,-3.015106,1.023534,-6.909389,7.703985,-6.216788,-9.882569,-0.072192,5.043563,6.891859,0.869376,5.864108,6.562459,9.407594,2.770071,-6.705608,-1.966156,1.330994,-6.806514,3.330691,6.963852,-2.376044,3.143429,7.114703,-1.119200,5.332739,-9.324513,1.478871,-9.547393,-0.842792,3.755331,-3.875871,-1.578316,-8.343005,-8.049151,-6.677635,6.873827,8.082982,6.240996,9.706211,2.202997,4.966841,3.454231,8.632040,7.265789,5.958752,1.284728,-0.504322,7.680414,-3.678360,-3.040810,2.245244,1.236559,5.168522,-4.383690,8.719132,8.197227,3.737391,7.398694,-1.188117,1.845616,-2.373030,-4.961028,-0.023533,4.469058,5.958007,8.714383,2.971274,6.948881,0.229247,8.502804,1.439386,8.101326,5.460090,-5.906607,9.766172,-2.244809,-3.932244,-9.376493,-4.421712,5.037275,8.054689,4.242445,-8.368465,0.645542,-6.451370,-5.319043,-1.211403,-3.772817,-7.277257,6.072251,-9.188577,0.702692,-2.637024,9.200211,0.229461,-9.137969,0.604991,0.863860,-6.186995,4.963653,6.444080,6.436154,6.212751,-3.089802,-1.111889,3.776022,4.131626,4.718273,-8.448103,-5.542905,0.210980,2.884316,-3.991035,-1.652026,1.880578,6.548543,7.733645,-2.388036,1.192888,6.514518,6.193803,-0.815719,3.712586,-7.231074,7.473905,-4.600400,-3.566601,8.789135,-4.738304,2.377816,-8.509167,8.364488,4.301394,-5.589958,-1.526102,-9.989922,4.191228,-1.286336,-7.104799,-5.320211,5.967593,4.751614,-3.974308,0.708817,-8.853517,0.107724,4.851555,8.966908,-6.984758,1.409697,4.099061,-5.362530,5.816705,2.374094,-1.702908,2.432357,-5.546955,9.862802,2.346064,-0.451315,5.801844,-6.771978,-2.003895,-4.182910,-5.181612,6.064708,1.288485,-2.090475,-6.372701,0.844934,7.812953,-9.574598,3.700061,6.337631,-6.664706,-4.731231,3.902479,3.032848,-0.702390,-5.834423,1.454523,-2.796204,-0.132615,7.676038,2.301734,5.763475,0.502556,-3.887312,7.523713,-4.467859,8.337181,8.749104,9.635880,-2.762794,-2.406395,-0.441137,-1.133878,0.211555,6.316899,7.712740,6.335131,-9.655259,2.591673,6.908327,-5.769643,-8.668940,-3.779781,-6.842189,-3.416075,-1.707334,9.011025,4.217618,6.190153,-9.714106,8.333507,6.712271,-3.515788,-6.605149,1.434059,-9.483386,1.654336,6.806925,2.915705,8.236785,1.663872,-4.524600,5.052879,-7.563664,-0.972651,9.822070,3.641139,-8.413239,-4.241806,5.954102,-4.792285,6.069136,-0.695229,-5.700726,-1.797575,-2.043259,5.561586,0.151277,-5.718219,9.058304,-5.632805,-4.786949,-7.953006,-4.231811,5.722129,-7.122461,0.352651,9.819493,-4.033577,5.716937,-3.113893,-7.472708,5.118795,-6.721867,-3.543579,-8.757685,-9.707161,-9.525677,-8.718576,-3.371434,-5.626070,1.473543,-7.449222,2.310538,-0.753531,-7.646962,-7.932344,-3.535416,-7.050594,2.945682,8.977194,6.771117,3.338300,-5.523650,-1.723584,9.512540,2.473891,8.476613,-1.081204,-1.481009,0.362313,4.018258,-1.648313,1.768086,-7.541793,1.960561,2.456318,4.366728,-5.662888,-0.903739,-7.306071,8.668394,-1.663716,-5.771814,8.788103,-7.210390,9.988851,2.722685,9.681660,-1.328469,7.621265,2.282254,-3.980520,2.799909,-4.792263,-5.366008,-0.505076,-9.871042,-1.026753,0.828217,-9.407655,-6.191850,0.600022,8.287379,9.660926,-9.446302,9.413397,1.220947,-5.795829,-7.657030,-6.697791,-7.701096,-6.136158,5.700294,6.884675,-8.790545,-9.566233,5.229536,-8.462521,6.190157,-1.790319,0.916038,0.303227,5.324891,7.249510,9.032394,-5.776262,-5.844001,-0.530016,1.565271,-9.235474,3.787043,1.660346,-3.119358,7.063909,2.185146,9.324842,3.464649,9.437397,7.911139,-5.923330,-3.050618,-2.094686,6.366021,-8.865142,-1.322480,8.184753,-6.016839,-4.559391,-4.083636,-8.674316,9.189867,-8.166546,-4.663555,2.828196,9.023188,-5.102041,7.167429,-9.879990,-9.113836,6.662736,-3.037119,-2.656198,1.611021,5.022974,4.278677,1.489688,-9.220801,0.415879,1.433329,-7.910707,7.456730,-2.310269,7.410498,4.313443,-4.112377,-4.073336,4.114835,7.292659,6.344222,4.565992,-9.754364,4.726757,-3.361096,5.211413,1.102989,-5.907704,9.859508,2.779093,-8.323340,-1.409180,-4.473769,8.993903,1.501889,-2.529457,6.639999,9.866642,7.575493,-3.055611,-2.921606,4.842120,4.304198,-6.499016,8.602085,6.221296,-2.032376,-0.045271,-5.975389,1.454619,-8.179807,-6.754563,4.654155,5.902732,-7.245625,-7.243419,9.066468,0.583148,-6.573402,4.399101,4.778858,5.439415,-3.908793,-8.796747,1.061405,2.238323,-1.693882,6.254348,7.266652,-0.686850,7.461914,-4.859423,-2.405301,4.795412,0.942418,-8.208316,-5.460342,6.946632,4.326039,9.681619,0.132164,-0.222193,7.806330,1.428748,-7.664320,-0.344760,-4.430643,3.543203,-0.686814,2.288995,7.248785,3.682331,5.281778,5.189457,-0.245554,4.046003,3.731622,8.507977,-8.724795,7.325171,-6.554152,-0.908710,3.871989,-0.758832,-4.748816,1.617492,1.862361,3.452792,9.610400,-9.035523,-5.382252,2.361394,8.541633,-2.801585,0.363226,4.320066,9.948104,1.368495,6.998595,9.393281,3.541313,2.716162,9.087979,-8.114851,3.064318,-4.791330,-2.178504,6.171873,9.523366,9.996499,-6.652495,-4.770150,-0.266011,-7.723874], dtype = "float64")#candidate|3459|(768,)|const|float64
call_3457 = relay.TupleGetItem(func_905_call(relay.reshape(const_3458.astype('int32'), [14, 3, 3]), relay.reshape(const_3458.astype('int32'), [14, 3, 3]), relay.reshape(const_3459.astype('float64'), [2, 384]), ), 1)
call_3460 = relay.TupleGetItem(func_910_call(relay.reshape(const_3458.astype('int32'), [14, 3, 3]), relay.reshape(const_3458.astype('int32'), [14, 3, 3]), relay.reshape(const_3459.astype('float64'), [2, 384]), ), 1)
bop_3465 = relay.bitwise_and(uop_3453.astype('uint64'), relay.reshape(call_3446.astype('uint64'), relay.shape_of(uop_3453))) # shape=(14, 13, 5)
bop_3468 = relay.bitwise_and(uop_3455.astype('uint64'), relay.reshape(call_3448.astype('uint64'), relay.shape_of(uop_3455))) # shape=(14, 13, 5)
bop_3474 = relay.not_equal(bop_3465.astype('bool'), relay.reshape(uop_3453.astype('bool'), relay.shape_of(bop_3465))) # shape=(14, 13, 5)
bop_3477 = relay.not_equal(bop_3468.astype('bool'), relay.reshape(uop_3455.astype('bool'), relay.shape_of(bop_3468))) # shape=(14, 13, 5)
func_3223_call = mod.get_global_var('func_3223')
func_3229_call = mutated_mod.get_global_var('func_3229')
call_3489 = relay.TupleGetItem(func_3223_call(relay.reshape(const_3458.astype('int32'), [126,]), relay.reshape(call_3457.astype('float64'), [2, 384]), relay.reshape(const_3447.astype('float64'), [13, 5]), relay.reshape(bop_3474.astype('float64'), [14, 13, 5]), ), 0)
call_3490 = relay.TupleGetItem(func_3229_call(relay.reshape(const_3458.astype('int32'), [126,]), relay.reshape(call_3457.astype('float64'), [2, 384]), relay.reshape(const_3447.astype('float64'), [13, 5]), relay.reshape(bop_3474.astype('float64'), [14, 13, 5]), ), 0)
func_3316_call = mod.get_global_var('func_3316')
func_3317_call = mutated_mod.get_global_var('func_3317')
call_3491 = relay.TupleGetItem(func_3316_call(), 0)
call_3492 = relay.TupleGetItem(func_3317_call(), 0)
output = relay.Tuple([call_3435,const_3447,call_3457,const_3458,const_3459,bop_3474,call_3489,call_3491,])
output2 = relay.Tuple([call_3436,const_3447,call_3460,const_3458,const_3459,bop_3477,call_3490,call_3492,])
func_3493 = relay.Function([], output)
mod['func_3493'] = func_3493
mod = relay.transform.InferType()(mod)
output = func_3493()
func_3494 = relay.Function([], output)
mutated_mod['func_3494'] = func_3494
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3399_call = mod.get_global_var('func_3399')
func_3400_call = mutated_mod.get_global_var('func_3400')
call_3508 = relay.TupleGetItem(func_3399_call(), 0)
call_3509 = relay.TupleGetItem(func_3400_call(), 0)
var_3510 = relay.var("var_3510", dtype = "int8", shape = (13, 14, 9))#candidate|3510|(13, 14, 9)|var|int8
bop_3511 = relay.mod(call_3508.astype('float32'), relay.reshape(var_3510.astype('float32'), relay.shape_of(call_3508))) # shape=(13, 14, 9)
bop_3514 = relay.mod(call_3509.astype('float32'), relay.reshape(var_3510.astype('float32'), relay.shape_of(call_3509))) # shape=(13, 14, 9)
func_292_call = mod.get_global_var('func_292')
func_294_call = mutated_mod.get_global_var('func_294')
var_3520 = relay.var("var_3520", dtype = "uint8", shape = (520, 1))#candidate|3520|(520, 1)|var|uint8
call_3519 = relay.TupleGetItem(func_292_call(relay.reshape(var_3520.astype('uint8'), [10, 13, 4])), 0)
call_3521 = relay.TupleGetItem(func_294_call(relay.reshape(var_3520.astype('uint8'), [10, 13, 4])), 0)
func_181_call = mod.get_global_var('func_181')
func_184_call = mutated_mod.get_global_var('func_184')
const_3526 = relay.const([8,-8,8,10,-9,7,9,-3,7,2,3,10,3,1,10,9,-6,5,-6,-9,-9,10,6,-1,-5,6,-10,-5,4,2,-10,3,10,9,-2,-5,-7,-9,10,-7,-6,2,7,-6,7,-4,2,2,5,10,-4,-6,-9,3,6,4,-10,7,-8,-8,-2,-4,2,-8,9,-4,-10,3,7,9,-5,5,-1,-5,-7,6,9,-6,5,-8,2,7,-2,1,8,5,3,1,4,7,-10,3,-10,-10,2,1,-10,6,-1,-3,7,2,-10,7,6,-5,4,6,8,-1,4,4,10,-9,-9,10,2,7,3,-4,-8,7,-9,-10,-1,-7,2,-2,-5,5,-3,9,5,5,-2,8,2,-3,-2,-7,-3,9,-10,-8,-2,-7,8,-10,2,2,6,3,7,10], dtype = "uint16")#candidate|3526|(154,)|const|uint16
call_3525 = relay.TupleGetItem(func_181_call(relay.reshape(const_3526.astype('uint16'), [14, 11, 1])), 1)
call_3527 = relay.TupleGetItem(func_184_call(relay.reshape(const_3526.astype('uint16'), [14, 11, 1])), 1)
output = relay.Tuple([bop_3511,call_3519,var_3520,call_3525,const_3526,])
output2 = relay.Tuple([bop_3514,call_3521,var_3520,call_3527,const_3526,])
func_3544 = relay.Function([var_3510,var_3520,], output)
mod['func_3544'] = func_3544
mod = relay.transform.InferType()(mod)
mutated_mod['func_3544'] = func_3544
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3544_call = mutated_mod.get_global_var('func_3544')
var_3546 = relay.var("var_3546", dtype = "int8", shape = (13, 14, 9))#candidate|3546|(13, 14, 9)|var|int8
var_3547 = relay.var("var_3547", dtype = "uint8", shape = (520, 1))#candidate|3547|(520, 1)|var|uint8
call_3545 = func_3544_call(var_3546,var_3547,)
output = call_3545
func_3548 = relay.Function([var_3546,var_3547,], output)
mutated_mod['func_3548'] = func_3548
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3296_call = mod.get_global_var('func_3296')
func_3298_call = mutated_mod.get_global_var('func_3298')
call_3561 = func_3296_call()
call_3562 = func_3296_call()
func_3316_call = mod.get_global_var('func_3316')
func_3317_call = mutated_mod.get_global_var('func_3317')
call_3571 = relay.TupleGetItem(func_3316_call(), 0)
call_3572 = relay.TupleGetItem(func_3317_call(), 0)
func_1953_call = mod.get_global_var('func_1953')
func_1957_call = mutated_mod.get_global_var('func_1957')
var_3577 = relay.var("var_3577", dtype = "uint16", shape = (44,))#candidate|3577|(44,)|var|uint16
call_3576 = func_1953_call(relay.reshape(var_3577.astype('uint16'), [11, 4, 1]), relay.reshape(var_3577.astype('uint16'), [11, 4, 1]), )
call_3578 = func_1953_call(relay.reshape(var_3577.astype('uint16'), [11, 4, 1]), relay.reshape(var_3577.astype('uint16'), [11, 4, 1]), )
func_2395_call = mod.get_global_var('func_2395')
func_2399_call = mutated_mod.get_global_var('func_2399')
var_3584 = relay.var("var_3584", dtype = "uint32", shape = ())#candidate|3584|()|var|uint32
const_3585 = relay.const([[-9,-10,-6,4,10,5,9,9,10,4,7,2,6,4,7,-7,6,-9,-4,4,-10,-8,-8,4,-6,-6,8,9,-1,-8,-10,5,2,2,9,-10,8,8,6,4,2,-5,7,-6,8,7,9,-3,7,9,-3,5,-8,5,-4,-7,8,9,-7,-6,-1,2,6,-2,-3,7,9,-5,-4,10,9,4,-9,-3,-10,-3,1,-10,1,9,3,7,-7,-9,-5,9,-8,1,10,6,-2,-8,2,-9,-9,6,4,4,-8,-4,-3,6,10,9,-3,7,-3,10,4,-10,-8,7,-10,7,5,2,6,9,7,-5,4,10,10,5,-9,-9,9,-3,6,-10,1,8,10,-3,-7,1,-4,-9,1,8,-6,9,10,8,-9,-8,-10,8,-6,-9,1,4,-1,8,6,-1,3,-10,9,-3,-8,-9,-9,-6,-9,-10,7,6,9,-7,3,7,-6,-1,9,-5,2,3,2,8,6,-4,2,-10,-7,5,-5,-4,-1,9,-8,5,8,-3,9,4,7,-8,-9,1,-5,5,-9,2,5,-2,-6,3,6,6,7,-1,-9,5,-7,-5,-1,4,-9,-3,-10,9,1,1,8,-3,9,-9,-4,8,1,6,4,-5,10,9,-3,5,-10,3,4,-3,1,3,10,-9,-5,-4,-8,-3,-7,6,3,-3,-10,1,4,8,9,1,5,10,-8,10,-3,2,-7,1,-4,3,1,-9,-1,10,-10,-9,4,6,4,-6,3,1,10,2,-6,-5,10,-4,1,-10,7,-8,9,-3,-4,-3,8,-6,4,2,2,9,-1,2,-6,-7,-4,-6,-2,9,9,-2,-6,7,8,-1,7,4,-2,-4,-3,-5,-7,-1,9,5,-1,-7,7,6,5,8,7,4,10,-10,-10,-9,6,-5,1,-5,1,9,7,-5,-5,4,7,-1,-5,-2,-8,1,-3,8,-10,-6,4,9,1,4,9,7,-8,-4,3,-8,-9,2,-9,5,3,8,-5,9,-3,3,10,9,-2,1,-9,4,-9,-9,7,8,3,7,5,7,8,-9,2,8,-10,-1,9,-8,-2,-7,-1,10,2,-4,-3,4,-3,-2,2,-10,1,3,7,-8,-10,-1,-1,5,-8,10,-1,5,-7,10,-8,-4,-2,-7,-10,-9,4,-1,8,-8,-6,10,-3,1,1,-1,-10,6,-2,2,-1,-4,10,10,1,6,8,-3,10,-1,5,-10,7,-8,2,-4,-10,8,2,-10,7,8,-2,6,-7,5,-9,7,-4,8,7,-8,10,7,-3,-5,-4,6,6,-10,-9,4,-1,-5,-6,-8,6,-9,2,-10,-4,-5,-10,4,1,8,8,-7,5,-3,-8,3,7,-10,-2,3,-5,-6,-7,10,4,-9,2,-3,-9,-7,7,1,-5,-2,3,-5,-2,-3,1,9,1,-10,-6,-1,9,-2,-1,-10,-5,-3,6,5,9,8,-1,-5,-7,-7,-8,-7,-8,3,1,-6,-4,3,9,7,-7,-7,-4,-3,7,-1,10,-2,-7,10,8,4,-4,-1,8,10,5,-6,-10,-9,10,-2,9,1,-10,-4,6,10,7,-5,-3,10,2,8,-4,-7,-6,9,4,1,-2,10,-3,9,6,-4,-9,-7,-2,-1,10,3,8,3,-1,-5,9,10,-8,1,3,2,-4,10,-4,2,-2,1,-8,-1,-7,3,-2,8,-2,-3,-8,6,4,6,9,-1,7,-1,6,-6,-6,1,-2,9,9,10,9,-9,-9,10,-7,9,4,-8,1,7,3,-7,-8,10,8,-7,3,9,-3,2,-1,1,-2,-8,-5,10,5,-2,4,10,-1,1,5,5,-1,5,9,-9,-6,-4,4,-8,1,-1,3,1,10,-5,-5,10,-1,-10,-2,-1,-8,1,1,10,-9,-9,2,-4,5,7,4,-4,4,-7,-2,7,5,1,-7,-8,-2,9,-10,-6,6,2,1,-7,1,1,4,5,-8,-5,-7,-1,1,-3,-5,-3,10,-3,1,-6,-3,6,-7,-7,9,-7,-5,7,10,-7,9,-6,-3,-10,10,-9,-4,-10,-7,-5,-1,3,3,-1,10,-8,8,-7,-2,7,4,-4,-2,1,-5,4,-9,1,-4,4,2,2,5,-3,8,-10,-8,3,1,7,-10,-2,-7,2,-7,7,8,9,9,-10,-2,1,5,7,-8,1,-7,-7,-6,-6,-5,10,2,-5,-1,-10,-5,2,5,-7,-6,-8,-1,-7,-4,-8,6,10,-9,-9,-2,-3,7,1,7,-4,-4,7,-9,-2,7,-4,10,-9,3,-9,-6,-3,10,-7,-2,9,5,-3,8,1,-7,-8,-1,8,-6,8,-1,-7,7,-5,6,4,10,10,-3,5,8,-7,-2,-2,1,-2,-2,-3,-4,-5,4,4,7,6,-4,9,6,-10,10,9,-1,4,-10,10,7,4,7,9,-1,5,6,9,10,2,-1,-1,-2,6,4,-7,3,4,1,-5,8,10,-2,8,10,1,-3,-4,5,-8,-7,-10,6,2,9,2,5,-3,-4,-10,3,4,2,-10,9,8,2,-4,-3,-8,4,-2,-5,-8,8,-1,-9,-6,4,-10,3,-7,-7,3,-9,-4,2,-4,3,-6,-1,-9,-4,5,-2,-1,4,-9,-10,3,-5,4,7,6,3,-8,-9,-9,3,-10,-9,-9,10,-6,-2,2,9,7,-8,-5,-5,5,1,6,8,-8,-7,-1,-7,-9,-9,-8,-1,-4,10,-9,-4,8,8,9,9,2,8,-3,2,4,5,10,9,-4,-5,3,-7,5,2,-1,5,7,7,-8,5,8,6,-5,-2,-3,2,-8,-8,4,1,10,-7,9,10,2,-9,-5,-8,1,1,-1,-1,-2,4,-8,-1,10,9,3,7,7,8,3,4,10,-10,-10,9,-10,10,-5,8,1,7,7,1,-3,5,7,-2,5,-7,2,7,-9,10,9,1,3,6,-3,-3,-6,-4,8,-1,7,9,3,1,-2,8,-7,1,-9,2,-4,10,-3,-4,-2,7,-4,-1,2,-9,-3,8,-7,1,-6,10,8,-1,-8,-4,-3,-2,-7,3,4,-4,10,6,10,5,-8,7,7,-9,-6,-5,-3,-3,-9,2,8,-8,-7,-8,-2,5,8,-6,-4,9,-7,7,1,-4,8,-4,1,7,-8,7,7,-2,5,-9,-2,-9,3,2,-7,4,10,2,-2,9,5,10,7,-5,9,-1,4,-3,-5,-3,-1,8,7,-5,2,-8,10,-6,-1,1,-7,-2,-2,8,-2,-2,9,6,-3,-4,-7,-9,-4,5,-8,-7,9,-7,-6,8,7,-1,-9,4,-6,-6,-3,-9,2,2,10,-6,-9,-2,10,-3,10,-5,8,3,-8,-8,-4,7,5,-5,-1,6,5,-6,-7,-4,-4,-10,-10,8,-1,-10,7,2,-9,7,-9,-1,-10,-9,-8,6,6,4,-8,-6,3,4,3,2,-3,5,1,-6,5,-9,-10,6,-10,4,5,7,-3,-7,-6,-2,9,3,-3,2,6,-2,-6,-4,9,4,-5,-3,1,7,-1,10,-4,2,2,5,5,4,-6,-10,6,10,-5,10,-4,-7,5,9,-10,9,4,10,1,-3,-4,-3,-6,-10,7,1,8,-10,-5,2,-7,7,-5,1,3,-5,6,7,-1,5,10,1,1,-9,-10,2,-2,-1,8,-4,-5,-9,-7,2,-7,7,-2,3,10,2,7,-7,2,7,-9,10,10,-6,-8,-8,-5,2,5,-3,-1,5,6,6,-10,-8,4,5,-9,-2,9,-2,4,4,-3,-4,-1,-10,-1,-6,9,-1,2,-6,7,10,7,2,7,-1,-2,-3,-4,-1,1,-7,1,-3,8,-6,7,-10,-7,4,-8,-4,-9,-3,-4,-7,2,-5,-4,6,8,-6,5,7,-10,-7,7,-9,10,9,-8,7,2,3,-2,9,-10,-5,3,-8,-7,3,6,-2,6,8,-10,2,-9,-8,-3,-1,4,-9,-9,1,-1,10,6,4,5,-6,9,5,-4,-8,-1,-1,4,1,-6,-9,-9,-6,5,9,-4,-3,4,10,2,-6,-7,-8,-8,4,1,2,-6,-5,10,9,8,6,1,-3,-2,-5,-7,-9,10,-8,1,-3,10,-8,-3,-4,-10,-4,-6,1,7,8,9,-6,3,3,5,8,5,4,4,10,10,-2,-2,-4,-1,10,10,-10,-1,-6,9,10,2,2,5,8,6,2,7,5,-8,9,-3,2,1,10,4,4,5,-1,-7,-6,1,1,3,9,10,-1,8,-7,-5,-1,-7,4,2,-2,6,-10,-3,-6,-6,10,-4,1,8,1,4,-10,-8,3,-2,6,5,5,-8,4,8,2,-7,-2,-2,6,-6,7,3,-3,-8,-2,-9,-1,-10,3,-1,7,-9,-10,-5,-8,-5,6,-8,-6,10,-7,7,-5,5,4,-4,-5,-2,-5,3,10,8,-9,-7,-1,3,5,10,-4,8,2,-10,5,1,-1,-3,4,6,-6,-8,-9,8,8,4,2,1,3,10,3,10,-8,4,-2,7,3,-8,-4,-6,2,-6,1,-10,-9,4,4,6,5,-7,-2,9,-10,10,1,10,-8,-10,6,-5,2,8,5,1,-6,9,3,-5,-4,10,-5,-9,-7,-3,-10,-9,-2,-8,3,-7,8,-10,5,-5,-2,-4,-5,1,-3,6,-5,-6,4,-1,5,-9,-7,5,4,-1,-7,5,-8,-4,1,4,7,-10,-6,-9,3,4,-6,-2,-9,9,5,-5,-10,-6,3,4,2,10,-9,8,8,1,-9,6,-5,-1,1,-5,-9,2,3,-1,-2,-4,3,-4,-2,-6,-8,-8,-1,5,-6,-3,-3,8,-2,2,1,8,6,4,-9,-8,5,9,-4,8,-5,7,-7,-6,4,-7,-2,7,-7,5,-1,2,-8,2,7,1,2,-2,5,-9,5,-3,1,6,-3,3,-5,-2,7,-4,5,-8,7,5,9,-10,10,-1,5,8,-2,4,7,10,-9,10,-4,-10,-10,1,-8,4,-6,10,4,-9,-10,-4,6,-1,-2,10,1,5,4,-5,-8,-10,-5,6,-8,-8,6,5,9,1,-9,7,1,-5,9,7,8,2,8,3,-2,4,4,-2,-7,4,3,10,-1,-1,5,-8,5,-6,-9,-1,-1,-9,-6,8,5,1,-3,-4,-8,-7,-2,7,6,-4,-4,3,2,2,2,-3,-4,-5,-7,-3,5,-7,-4,8,-8,4,5,-9,1,7,3,-2,-4,4,-7,6,7,-1,-10,3,-1,-9,-6,5,10,-3,-10,10,2,-7,2,-3,1,-2,-2,8,-3,10,-3,-9,7,-6,4,2,1,-5,7,2,1,-8,8,-8,10,2,-5,10,10,-8,1,10,-1,5,-2,-5,-2,10]], dtype = "uint32")#candidate|3585|(1, 2016)|const|uint32
call_3583 = relay.TupleGetItem(func_2395_call(relay.reshape(var_3584.astype('uint32'), []), relay.reshape(const_3585.astype('uint32'), [12, 14, 12]), ), 1)
call_3586 = relay.TupleGetItem(func_2399_call(relay.reshape(var_3584.astype('uint32'), []), relay.reshape(const_3585.astype('uint32'), [12, 14, 12]), ), 1)
func_1015_call = mod.get_global_var('func_1015')
func_1018_call = mutated_mod.get_global_var('func_1018')
const_3589 = relay.const([-2.067070,7.845728,-3.284643,2.702401,-2.632377,-7.795692,2.350665,4.974829,2.966551,-7.721237,8.104322,3.039260,-2.175536,-8.240174,-3.326534,4.584070,-8.562568,6.044438,-7.896946,8.348158,5.942876,-8.406594,1.037829,-5.708921,3.719564,-2.540006,2.598162,-5.277842,7.957946,-1.256056,-3.311798,-9.945309,-7.406221,4.213008,-2.278156,4.902874,1.841280,7.889485,3.881668,7.149308,-2.523137,1.735701,4.782281,6.467840,6.471627,-8.773979,1.088186,-3.882070,-4.795205,9.227628,-8.704050,-1.590985,-2.124630,-0.764271,9.160479,-2.145830,-9.704874,-3.783505,6.357912,-5.299848,6.399976,-8.760836,-2.280490,-6.215267,1.876359,1.376740,-3.541132,9.289406,4.329726,-4.293422,4.624692,-4.461635,0.576390,1.453326,7.357880,6.642125,-7.124821,7.705066,-5.235958,8.346534,4.551539,5.300829,-1.228662,-1.093099,-3.730623,-6.506887,4.777850,9.063027,2.794500,5.791727,6.983904,8.097280,0.615844,-8.034699,-8.468662,5.301507,-5.035537,7.462336,1.481072,2.495731,2.936481,1.941698,-1.579224,9.842798,0.931899,-9.961738,6.149176,-0.327178,3.429228,-8.195142,-7.860110,0.453773,-7.537591,0.916646,0.021142,1.502574,-7.642414,2.479796,-7.161982,4.250496,-1.357327,-7.677611,6.475689,-5.320571,8.302485,5.481165,-5.160672,-5.738609,2.737840,-4.566487,-6.562889,9.263465,-2.030576,-9.158316,3.228798,-1.761187,0.408164,7.838691,9.574942,9.711020,-6.662728,-0.131679,-4.255751,8.319939,-2.928898,-6.197982,-6.031776,8.545576,-4.114490,7.299341,3.603858,6.459584,-4.803527,-3.023939,-2.767187,-8.261969,-8.148995,6.738256,8.406964,-2.706650,-6.213153,6.513322,2.034055,2.173527,-2.143184,0.465460,-0.795093,-1.355289,-3.413637,-3.465034,3.319516,1.640700,6.738636,-6.175577,-8.667198,-6.078815,9.658214,0.211304,4.109919,-4.129010,3.646327,4.951832,6.339064,-7.164784,-7.755570,-2.586374,8.591913,9.836238,0.170812,7.912929,8.159658,-5.524136,6.443628,1.445963,2.158232,-2.048853,8.560582,-7.845473,-5.346908,-3.402459,-5.488383,-4.251420,0.832220,-0.043496,9.923131,-5.481178,-3.121201,7.719352,-4.288662,-9.660804,-9.693421,-2.063964,-2.879253,-6.212924,1.677932,-8.324735,-9.157372,1.724945,-7.764496,-6.459572,7.412501,-3.123997,9.444964,-8.580042,-5.338610,4.447827,1.771557,3.825527,5.768389,-0.714995,-1.110370,-8.112691,6.526324,-0.731288,6.283247,2.041554,6.516436,-1.743019,3.091596,-1.484635,3.559446,0.418208,9.106185,0.710947,-7.752466,1.694066,-2.600179,0.362603,8.253150,4.342822,-3.257661,-2.846839,2.183828,3.978401,9.788559,-2.560846,8.767308,0.611788,-9.254803,5.434226,3.921263,-0.400332,-1.299907,5.501690,2.301413,9.765669,-0.208349,-5.202534,-8.370429,-3.344689,8.663641,1.594123,-3.845293,-0.379061,5.698258,-0.252187,-6.839287,-8.848277,-0.547186,7.757483,-4.593001,-7.933915,-9.892733,-0.914652,-7.235366,-4.176364,-0.528191,-2.691510,-1.029334,2.861079,6.604441,-7.890333,-2.802572,-0.895675,3.894781,9.976186,-8.798637,-6.211443,-7.496618,-5.944791,4.907982,-2.801983,-8.469398,0.739926,1.722496,-3.037440,-3.159050,1.438099,2.957380,4.635217,3.979108,-3.181351,-4.211607,-9.758523,-9.099972,6.653935,6.406843,2.504396,4.034171,-4.613821], dtype = "float32")#candidate|3589|(320,)|const|float32
call_3588 = relay.TupleGetItem(func_1015_call(relay.reshape(const_3589.astype('float32'), [5, 8, 8]), relay.reshape(const_3589.astype('float32'), [5, 8, 8]), ), 5)
call_3590 = relay.TupleGetItem(func_1018_call(relay.reshape(const_3589.astype('float32'), [5, 8, 8]), relay.reshape(const_3589.astype('float32'), [5, 8, 8]), ), 5)
uop_3591 = relay.sigmoid(call_3561.astype('float32')) # shape=(13, 14, 9)
uop_3593 = relay.sigmoid(call_3562.astype('float32')) # shape=(13, 14, 9)
func_3107_call = mod.get_global_var('func_3107')
func_3108_call = mutated_mod.get_global_var('func_3108')
call_3596 = relay.TupleGetItem(func_3107_call(), 0)
call_3597 = relay.TupleGetItem(func_3108_call(), 0)
func_1106_call = mod.get_global_var('func_1106')
func_1109_call = mutated_mod.get_global_var('func_1109')
const_3602 = relay.const([2,8,-6,9,-6,-9,-7,1,-1,8,1,-1,6,-5,4,-6,1,10,-2,9,-2,-6,1,2,10,-6,-2,10,-6,-4,10,9,-3,-1,8,10,10,8,5,-5,-2,10,10,3,-4,10,-8,-7,8,7,-10,3,-4,1,-10,6,7,-5,5,-7,-6,5,6,6,-2,7,9,3,-10,3,-1,4,-5,7,9,-7,10,9,-5,-7,6,-10,3,-10,-8,-5,-2,-8,-7,6,-8,-1,6,2,2,10,-1,-5,-6,9,8,4,2,8,5,-5,9,-1,3,8,-3,5,1,-10,5,-10,3,4,5,7,7,5,6,-3,-9,8,1,8,5,6,9,-4,1,-10,-3,-8,-6,8,-9,5,-2,-4,6,5,-1,-3,9,3,-7,-8,-9,-1,-9,1,10,10,10,-4,-3,10,-10,-4,-10,2,-1,8,-7,9,7,-6,9,-8,-7,5,-3,-5,8,3,8,7,-6,-1,1,-8,3,5,7,9,10,-5,-1,-6,-2,8,6,9,-10,4,-2,2,-8,7,2,1,-2,-5,-9,-3,-1,10,8,-1,2,10,10,1,-10,-3,-4,4,-1,10,-9,-10,4,10,-1,-10,8,9,3,6,-8,-8,5,10,-3,7,-3,-4,9,1,-5,-3,3,1,-9,3,-7,-2,5,10,10,9,4,-10,-7,3,4,-5,5,4,4,-3,-8,-5,5,-10,3,-10,-3,2,-3,-4,-10,-3,8,2,7,-4,10,-8,7,2,5,10,2,2,8,2,6,4,-3,7,-2,4,2,-5,-8,-10,-10,-3,-2,-8,2,8,-5,3,9,-9,10,-10,-5,-1,3,8,-2,6,7,-6,-5,-8,-7,2,8,6,7,10,5,7,-5,-3,-9,2,-4,4,3,4,2,7,-9,9,2,-10,-3,5,5,4,7,-9,-6,-4,4,10,-6,-7,3,3,-7,2,-3,5,-5,9,9,-6,-10,6,8,1,7,9,5,-7,6,-2,6,-6,-8,-6,-2,2,3,-7,7,7,9,4,-9,-8,-10,-5,-6,9,5,-1,-10,-10,-2,-5,6,-3,-9,10,-7,6,-7,-4,-1,8,-10,6,1,-2,4,4,-1,-4,-3,10,-3,7,-7,-2,4,8,-9,4,10,-5,-5,-4,-5,9,-5,7,-7,-5,-5,-7,-6,-5,-7,7,6,2,2,-10,-4,-8,-1,-4,-1,-5,7,7,6,2,-2,-1,-2,4,6,-4,6,-9,7,5,4,4,1,9,-5,1,10,10,4,8,9,-2,4,-9,-5,-8,-6,4,-4,-5,4,10,9,-7,-3,2,-9,-6,6,-3,-2,3,3,-5,10,8,7,9,-8,-8,-3,5,-5,-2,-10,1,6,-10,-1,6,9,7], dtype = "uint32")#candidate|3602|(520,)|const|uint32
call_3601 = func_1106_call(relay.reshape(var_3584.astype('uint32'), []), relay.reshape(const_3602.astype('uint32'), [8, 5, 13]), )
call_3603 = func_1106_call(relay.reshape(var_3584.astype('uint32'), []), relay.reshape(const_3602.astype('uint32'), [8, 5, 13]), )
output = relay.Tuple([call_3571,call_3576,var_3577,call_3583,var_3584,const_3585,call_3588,const_3589,uop_3591,call_3596,call_3601,const_3602,])
output2 = relay.Tuple([call_3572,call_3578,var_3577,call_3586,var_3584,const_3585,call_3590,const_3589,uop_3593,call_3597,call_3603,const_3602,])
func_3609 = relay.Function([var_3577,var_3584,], output)
mod['func_3609'] = func_3609
mod = relay.transform.InferType()(mod)
mutated_mod['func_3609'] = func_3609
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3609_call = mutated_mod.get_global_var('func_3609')
var_3611 = relay.var("var_3611", dtype = "uint16", shape = (44,))#candidate|3611|(44,)|var|uint16
var_3612 = relay.var("var_3612", dtype = "uint32", shape = ())#candidate|3612|()|var|uint32
call_3610 = func_3609_call(var_3611,var_3612,)
output = call_3610
func_3613 = relay.Function([var_3611,var_3612,], output)
mutated_mod['func_3613'] = func_3613
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3627 = relay.var("var_3627", dtype = "float32", shape = (6, 12, 6))#candidate|3627|(6, 12, 6)|var|float32
var_3628 = relay.var("var_3628", dtype = "float32", shape = (6, 12, 6))#candidate|3628|(6, 12, 6)|var|float32
bop_3629 = relay.mod(var_3627.astype('float32'), relay.reshape(var_3628.astype('float32'), relay.shape_of(var_3627))) # shape=(6, 12, 6)
func_3107_call = mod.get_global_var('func_3107')
func_3108_call = mutated_mod.get_global_var('func_3108')
call_3636 = relay.TupleGetItem(func_3107_call(), 0)
call_3637 = relay.TupleGetItem(func_3108_call(), 0)
output = relay.Tuple([bop_3629,call_3636,])
output2 = relay.Tuple([bop_3629,call_3637,])
func_3646 = relay.Function([var_3627,var_3628,], output)
mod['func_3646'] = func_3646
mod = relay.transform.InferType()(mod)
var_3647 = relay.var("var_3647", dtype = "float32", shape = (6, 12, 6))#candidate|3647|(6, 12, 6)|var|float32
var_3648 = relay.var("var_3648", dtype = "float32", shape = (6, 12, 6))#candidate|3648|(6, 12, 6)|var|float32
output = func_3646(var_3647,var_3648,)
func_3649 = relay.Function([var_3647,var_3648,], output)
mutated_mod['func_3649'] = func_3649
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3296_call = mod.get_global_var('func_3296')
func_3298_call = mutated_mod.get_global_var('func_3298')
call_3747 = func_3296_call()
call_3748 = func_3296_call()
output = call_3747
output2 = call_3748
func_3755 = relay.Function([], output)
mod['func_3755'] = func_3755
mod = relay.transform.InferType()(mod)
output = func_3755()
func_3756 = relay.Function([], output)
mutated_mod['func_3756'] = func_3756
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3808 = relay.const([[[4.127587,-5.910615,8.107203,7.228870,9.319611,8.587673,-0.922825,6.487276,-6.821136,1.985300,7.110636,9.873830,-9.530828],[-1.075329,8.938020,6.462702,2.052636,3.282994,-4.858582,6.753585,4.955347,7.197868,-9.827656,9.487128,3.548049,-9.117212]],[[-2.784190,-7.542767,4.544314,3.214922,-3.460346,-2.339111,-1.415575,-2.984310,-2.148229,0.492473,-7.555318,3.561044,3.803567],[-0.970137,2.111471,-6.787911,-3.515058,3.480356,3.316321,-8.421061,6.022559,3.059132,9.397399,-6.218435,5.954182,3.933414]],[[-6.390803,8.313290,7.748820,8.848499,-1.591347,-6.663594,-1.672295,3.204613,-5.491196,9.618091,-9.630562,-3.085421,4.856937],[5.455332,-3.085866,-9.335557,-0.082543,-8.213331,1.763102,-4.306232,3.452426,5.036752,-5.292511,6.085835,-8.612001,-9.373683]],[[-4.232305,-8.945966,-2.910247,-5.965004,-5.719551,7.783727,-1.406641,-5.321650,2.218441,-6.175293,-4.461752,-3.053656,-2.838965],[3.617621,9.692489,0.702232,-5.569198,5.064900,0.713688,9.341291,-4.349274,-9.143352,2.214301,8.478793,-3.171628,7.712812]],[[0.933142,0.071416,-2.015047,-7.812241,8.682418,7.328714,-8.763940,-8.988844,-4.560055,2.108891,-1.161526,-9.400110,9.612737],[3.722687,4.336180,-7.885498,-5.689113,-7.079702,-1.632433,-6.677080,-8.908247,-7.509216,-3.092840,-4.585307,-3.169217,-5.506259]],[[-6.874626,-8.167275,-7.294983,5.209392,9.848814,-9.718960,0.071393,-7.664101,1.094913,2.534064,-4.078526,-6.738796,-1.079043],[5.069391,2.824168,-3.700047,-7.110878,9.175154,-5.817525,-7.746548,-2.304526,1.018462,1.645662,5.616240,6.769523,-6.711900]],[[-4.487466,-1.465129,-2.013102,-4.489700,6.125079,5.218541,8.619352,-3.242595,4.029332,5.963313,2.730778,3.583610,-0.050218],[-0.243522,-4.978571,3.213294,1.578259,2.648644,-3.256607,4.372053,-4.015862,0.889735,4.385754,1.179858,6.297433,-4.899082]],[[-8.168741,7.974149,1.674245,-0.449661,3.411744,-4.426632,4.135897,-2.678503,0.581520,-7.168032,-8.658810,-9.162673,2.020601],[-0.628962,-7.544932,-1.203815,-9.048701,-3.328379,0.170261,7.867605,-2.553087,3.864997,-3.477677,4.632831,-2.133819,8.749913]],[[-0.651079,-0.525546,-0.416384,-4.733484,-5.354062,1.766086,-6.996244,-9.846268,-8.020500,-2.507207,8.533543,-0.869522,5.380932],[-7.922883,9.269800,-8.527428,9.128891,-1.390850,6.358359,-5.907606,5.652683,9.666530,6.909405,1.018466,5.308005,9.565194]],[[2.356181,-9.845640,2.537499,-4.778238,3.395322,-2.363895,-7.112695,-9.679848,5.069595,2.444430,-3.424716,0.132420,-9.496402],[6.675388,-5.101349,-3.807132,-4.818428,9.741119,6.343438,1.869896,-5.010209,2.134468,-8.449357,2.249810,3.438506,-9.508294]],[[3.619590,5.320273,-7.938500,5.281769,3.974814,-6.053495,8.553593,-5.728986,-4.903108,8.427698,4.585169,5.436099,-0.295535],[-6.572642,9.031330,4.058106,-0.032082,-6.942385,4.050245,8.391357,7.770733,-8.200666,9.413077,-3.590970,-6.374307,5.910066]]], dtype = "float64")#candidate|3808|(11, 2, 13)|const|float64
var_3809 = relay.var("var_3809", dtype = "float64", shape = (11, 2, 13))#candidate|3809|(11, 2, 13)|var|float64
bop_3810 = relay.divide(const_3808.astype('float64'), relay.reshape(var_3809.astype('float64'), relay.shape_of(const_3808))) # shape=(11, 2, 13)
func_3316_call = mod.get_global_var('func_3316')
func_3317_call = mutated_mod.get_global_var('func_3317')
call_3817 = relay.TupleGetItem(func_3316_call(), 0)
call_3818 = relay.TupleGetItem(func_3317_call(), 0)
uop_3822 = relay.asinh(bop_3810.astype('float32')) # shape=(11, 2, 13)
bop_3825 = relay.maximum(uop_3822.astype('int32'), relay.reshape(const_3808.astype('int32'), relay.shape_of(uop_3822))) # shape=(11, 2, 13)
output = relay.Tuple([call_3817,bop_3825,])
output2 = relay.Tuple([call_3818,bop_3825,])
func_3838 = relay.Function([var_3809,], output)
mod['func_3838'] = func_3838
mod = relay.transform.InferType()(mod)
mutated_mod['func_3838'] = func_3838
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3839 = relay.var("var_3839", dtype = "float64", shape = (11, 2, 13))#candidate|3839|(11, 2, 13)|var|float64
func_3838_call = mutated_mod.get_global_var('func_3838')
call_3840 = func_3838_call(var_3839)
output = call_3840
func_3841 = relay.Function([var_3839], output)
mutated_mod['func_3841'] = func_3841
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3081_call = mod.get_global_var('func_3081')
func_3083_call = mutated_mod.get_global_var('func_3083')
call_3845 = relay.TupleGetItem(func_3081_call(), 0)
call_3846 = relay.TupleGetItem(func_3083_call(), 0)
output = call_3845
output2 = call_3846
func_3851 = relay.Function([], output)
mod['func_3851'] = func_3851
mod = relay.transform.InferType()(mod)
output = func_3851()
func_3852 = relay.Function([], output)
mutated_mod['func_3852'] = func_3852
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3296_call = mod.get_global_var('func_3296')
func_3298_call = mutated_mod.get_global_var('func_3298')
call_3855 = func_3296_call()
call_3856 = func_3296_call()
output = call_3855
output2 = call_3856
func_3859 = relay.Function([], output)
mod['func_3859'] = func_3859
mod = relay.transform.InferType()(mod)
output = func_3859()
func_3860 = relay.Function([], output)
mutated_mod['func_3860'] = func_3860
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3081_call = mod.get_global_var('func_3081')
func_3083_call = mutated_mod.get_global_var('func_3083')
call_3873 = relay.TupleGetItem(func_3081_call(), 0)
call_3874 = relay.TupleGetItem(func_3083_call(), 0)
const_3881 = relay.const([2.969247,-2.299407,-8.813136,-8.351088,-3.643508,6.020147,-3.177717,5.125856,-7.946242,-3.657458,-3.371237,-3.599325,-5.983514,-8.304645,6.353340,7.075906,-7.950288,6.935682,-4.104513,-6.482632,-4.023460,3.634006,2.075124,-8.526413,-8.758510,-4.807593,-0.904355,-6.901895,8.023610,0.409894,-4.812968,-3.794147,-5.836380,5.175048,8.019376,0.083491,-2.297593,-2.100434,9.226043,6.534138,9.380344,-8.057030,-2.701997,-6.656985,-5.844981,-5.812676,-5.468676,6.880365,-5.133088,-8.805286,-3.486784,-7.693946,-7.752677,-8.620576,1.554508,8.231817,-9.828086,-0.626736,-3.319593,-9.902539,-6.640208,-6.003643,3.944536,3.661832,-2.722699,4.016284,8.435839,1.776936,3.602410,-3.409820,5.698306,5.241739,6.662910,-4.907010,2.160323,-9.802850,7.364753,-0.319634,-5.432207,9.588662,8.799026,-6.355367,-1.930650,-8.681752,5.795770,-8.098376,-3.504366,-9.497983,-5.424200,-2.367427,-2.489809,1.358927,0.703981,-7.552624,-7.594155,-9.841804,4.063355,-8.326378,7.514412,3.643607,7.093425,7.132359,0.746430,-7.361682,7.472127,8.761383,5.575494,3.474428,3.829845,6.114146,4.224263,0.002694,-7.506049,-7.827054,3.851829,-6.933013,-3.330274,-6.864625,-7.789526,5.691517,3.076420,5.008320,8.625076,2.143677,-0.648566,-5.355221,5.679554,-4.037165,-2.118559,0.510622,-2.969589,-0.883464,4.622920,2.363410,7.723126,5.727843,0.332774,-0.640634,-8.285011,1.174132,-4.121129,-1.042658,-0.567438,8.499990,-9.540721,-7.851794,-8.566541,5.488479,3.306250,9.196531,4.970093,-9.988730,1.778860,9.467893,-7.862297,8.651763,7.648004,-5.968389,-2.488522,-1.459866,-8.303185,-1.883266,1.116514,6.045812,-4.256829,-8.589459,0.711344,-5.502353,5.329981,-7.247299,6.976803,-1.659659,-7.740368,-4.403149,-4.191476,8.308912,3.833434,7.605846,4.264844,3.878532,-6.104160,6.899329,-7.805187,-8.940837,8.131052,-2.536444,-2.250697,0.074323,0.776852,-7.659192,-5.565950,3.594817,8.413017,3.561637,0.856737,-1.579774,-3.404248,6.107609,4.664976,-5.575622,1.659523,5.879303,9.369243,-3.494547,-3.281482,-3.817499,-6.610183,-3.256936,-4.775906,-6.948176,0.293551,9.552762,-6.714810,-9.648680,2.489486,-5.733707,2.543355,-3.334598,8.481273,-3.053017,6.927455,-0.242830,-3.686133,1.652002,-8.620386,-7.073016,-3.435187,1.475367,-6.559956,7.003342,-2.960781,-3.150611,6.549853,-9.435737,4.582676,7.679426,8.562278,-3.901486,-7.484871,7.726014,5.757499,-7.502674,5.584410,-5.321667,-5.880736,1.589333,-1.039293,-4.517818,5.012560,-3.019903,4.320803,3.664692,4.563918,-0.827974,-6.313697,1.617460,1.571019,8.212152,2.050155,3.508834,2.925548,9.233551,-5.214726,-1.908073,-7.978364,4.124635,-8.678232,5.268611,-1.734375,2.059828,8.575734,5.323095,7.124352,7.415081,-6.641759,-1.689232,-7.417848,8.367266,4.884389,-6.182845,-9.435297,-4.398182,-6.030689,0.455037,7.309193,5.350823,8.001652,-7.527740,-3.766921,6.057551,-8.920108,-4.512104,7.288392,8.376948,3.206646,2.327119,9.362723,-4.918559,1.538208,1.949056,7.278864,5.109854,9.715685,4.154498,0.580052,-6.110580,-5.940773,-4.274497,3.797327,-2.345425,3.793824,-9.510916,6.466223,7.153300,-8.836527,-3.173366,9.744242,-3.382066,9.658328,-9.098104,4.037693,-4.411155,-1.201504,9.715188,-4.301935,-6.673693,5.077818,4.858458,-4.261738,6.927861,3.272368,-4.353087,6.819436,9.575111,-4.943143,-6.670755,-8.447448,1.211485,6.963691,-6.560900,-6.253514,-4.288014,-6.854644,6.749381,-4.401940,5.126845,-7.141777,-2.505050,0.771404,-4.660644,-3.840423,1.861667,4.179571,1.643170,0.590304,-7.216821,-2.563269,-2.791010,-4.989059,3.564860,-8.691456,-0.985918,-5.452931,2.539216,-4.887377,8.728380,-2.898648,-5.963396,1.972087,-8.289235,2.022232,5.323740,8.156991,-2.610823,4.676610,-4.109007,3.493604,-0.088358,-6.361562,1.413715,6.242692,1.789833,9.644457,4.887007,0.492784,0.984618,-9.051068,-1.531819,-4.010166,-2.100493,5.541956,-8.368550,8.557413,-3.164919,-1.592866,7.529707,5.543709,3.192375,-7.461509,7.969670,-6.745332,-2.265617,7.281289,3.412085,-3.437767,2.336322,-0.430081,-9.820563,-1.735095,8.146195,-5.793678,-5.373132,1.844433,-6.130466,-1.138962,0.656361,-6.514477,-0.948785,7.211572,-0.070500,2.287867,8.997126,4.654950,1.251839,-3.422785,-0.472079,9.982003,-4.274760,-7.094555,-0.471573,9.283148,1.779728,-7.056311,9.465999,4.006097,9.645004,-2.533502,7.973958,-1.068834,2.496962,8.744609,0.698736,8.395661,-1.011090,-6.424874,-7.357233,-4.491726,6.680547,1.467118,-2.735478,-2.310199,2.198348,-9.166117,-2.251113,-4.853226,-4.387300,5.510100,-4.688368,3.348494,-5.765884,-8.736131,8.495474,8.521408,4.498571,-5.925150,1.907354,7.314368,7.612962,4.942228,-6.784052,1.663617,-0.289000,-6.554752,8.975596,3.346666,3.134686,1.481873,-2.838768,8.604730,2.476593,-2.902879,7.746383,-3.026319,0.186639,-5.455116,2.397488,-8.552062,4.450974,-0.151206,8.781575,-9.187142,3.510747,6.129484,-3.688899,2.275588,-1.226474,2.025015,2.685210,-6.744555,3.884278,-8.913635,7.239325,-2.651809,2.170639,3.287440,-2.458462,9.267697,0.942895,-0.829877,-2.273551,-6.229599,2.880469,-8.453179,4.436265,3.355615,3.131158,0.634742,7.789911,9.839571,-8.548129], dtype = "float32")#candidate|3881|(520,)|const|float32
bop_3882 = relay.equal(call_3873.astype('bool'), relay.reshape(const_3881.astype('bool'), relay.shape_of(call_3873))) # shape=(520,)
bop_3885 = relay.equal(call_3874.astype('bool'), relay.reshape(const_3881.astype('bool'), relay.shape_of(call_3874))) # shape=(520,)
output = relay.Tuple([bop_3882,])
output2 = relay.Tuple([bop_3885,])
func_3890 = relay.Function([], output)
mod['func_3890'] = func_3890
mod = relay.transform.InferType()(mod)
output = func_3890()
func_3891 = relay.Function([], output)
mutated_mod['func_3891'] = func_3891
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3851_call = mod.get_global_var('func_3851')
func_3852_call = mutated_mod.get_global_var('func_3852')
call_4242 = func_3851_call()
call_4243 = func_3851_call()
func_2929_call = mod.get_global_var('func_2929')
func_2931_call = mutated_mod.get_global_var('func_2931')
call_4249 = relay.TupleGetItem(func_2929_call(), 8)
call_4250 = relay.TupleGetItem(func_2931_call(), 8)
func_3544_call = mod.get_global_var('func_3544')
func_3548_call = mutated_mod.get_global_var('func_3548')
call_4270 = relay.TupleGetItem(func_3544_call(relay.reshape(call_4249.astype('int8'), [13, 14, 9]), relay.reshape(call_4242.astype('uint8'), [520, 1]), ), 2)
call_4271 = relay.TupleGetItem(func_3548_call(relay.reshape(call_4249.astype('int8'), [13, 14, 9]), relay.reshape(call_4242.astype('uint8'), [520, 1]), ), 2)
output = relay.Tuple([call_4242,call_4249,call_4270,])
output2 = relay.Tuple([call_4243,call_4250,call_4271,])
func_4283 = relay.Function([], output)
mod['func_4283'] = func_4283
mod = relay.transform.InferType()(mod)
output = func_4283()
func_4284 = relay.Function([], output)
mutated_mod['func_4284'] = func_4284
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3081_call = mod.get_global_var('func_3081')
func_3083_call = mutated_mod.get_global_var('func_3083')
call_4317 = relay.TupleGetItem(func_3081_call(), 0)
call_4318 = relay.TupleGetItem(func_3083_call(), 0)
var_4323 = relay.var("var_4323", dtype = "float32", shape = (520,))#candidate|4323|(520,)|var|float32
bop_4324 = relay.less_equal(call_4317.astype('bool'), relay.reshape(var_4323.astype('bool'), relay.shape_of(call_4317))) # shape=(520,)
bop_4327 = relay.less_equal(call_4318.astype('bool'), relay.reshape(var_4323.astype('bool'), relay.shape_of(call_4318))) # shape=(520,)
func_3890_call = mod.get_global_var('func_3890')
func_3891_call = mutated_mod.get_global_var('func_3891')
call_4331 = relay.TupleGetItem(func_3890_call(), 0)
call_4332 = relay.TupleGetItem(func_3891_call(), 0)
output = relay.Tuple([bop_4324,call_4331,])
output2 = relay.Tuple([bop_4327,call_4332,])
func_4337 = relay.Function([var_4323,], output)
mod['func_4337'] = func_4337
mod = relay.transform.InferType()(mod)
mutated_mod['func_4337'] = func_4337
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4338 = relay.var("var_4338", dtype = "float32", shape = (520,))#candidate|4338|(520,)|var|float32
func_4337_call = mutated_mod.get_global_var('func_4337')
call_4339 = func_4337_call(var_4338)
output = call_4339
func_4340 = relay.Function([var_4338], output)
mutated_mod['func_4340'] = func_4340
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3890_call = mod.get_global_var('func_3890')
func_3891_call = mutated_mod.get_global_var('func_3891')
call_4350 = relay.TupleGetItem(func_3890_call(), 0)
call_4351 = relay.TupleGetItem(func_3891_call(), 0)
func_3544_call = mod.get_global_var('func_3544')
func_3548_call = mutated_mod.get_global_var('func_3548')
const_4357 = relay.const([[-9,7,-1],[7,1,5],[7,5,-9],[-6,-1,8],[-1,2,6],[5,2,-1],[2,-3,6],[-8,-5,10],[-6,-6,1],[-4,2,-10],[-7,-6,-6],[1,8,10],[1,9,-10],[9,-5,-2],[9,-7,-1],[9,-1,-6],[3,2,3],[-5,1,-10],[1,7,-4],[-10,-7,4],[-5,8,8],[-2,3,-2],[7,1,-1],[9,2,-8],[8,-1,-7],[5,-8,6],[6,8,-4],[-6,-8,-9],[1,1,-5],[-10,-6,-8],[-6,5,-3],[-1,-8,8],[9,-3,2],[8,-9,7],[-5,-4,9],[-6,-2,-10],[-1,-6,10],[-3,8,8],[7,5,2],[-7,-10,9],[-3,-6,-5],[2,5,-5],[1,-4,5],[3,5,-7],[10,3,6],[-1,9,6],[2,-10,-7],[2,4,-1],[7,10,-1],[-8,-10,3],[4,-3,-9],[-7,-8,-10],[1,-2,-9],[1,-6,7],[-7,-8,-7],[-10,-5,4],[-3,-7,-7],[5,10,-10],[-2,-4,-3],[4,7,6],[3,4,3],[3,10,-9],[8,2,5],[8,6,-6],[4,-10,3],[4,-4,-5],[-8,-4,-10],[-5,9,6],[-1,1,-6],[-6,-6,1],[2,7,-6],[2,-3,-4],[1,9,7],[6,-10,5],[4,4,8],[1,-3,-8],[1,4,-8],[6,6,-3],[-1,-10,6],[4,-7,-9],[-8,-6,9],[1,-6,5],[-1,-5,-4],[-1,7,-5],[7,10,2],[10,2,-10],[-2,10,-3],[-1,-5,3],[-5,4,6],[-5,-1,-6],[6,2,5],[-8,2,-4],[4,1,-4],[-9,-1,-10],[-4,-9,-2],[7,-2,-6],[10,4,4],[7,5,-7],[4,-7,9],[-1,4,8],[-6,4,4],[7,-3,-6],[-10,5,4],[-2,6,-5],[-1,-7,-8],[-1,-10,4],[-6,-9,-1],[6,-1,7],[-2,4,-10],[-4,5,6],[-8,8,3],[-3,-3,7],[-1,-5,5],[8,1,-5],[2,2,3],[-3,-4,-1],[2,-5,8],[9,7,2],[6,-7,-3],[-7,-6,-4],[-6,1,9],[10,-4,6],[-9,1,-1],[-5,-4,-5],[9,-4,3],[-5,7,3],[-6,9,8],[-3,-2,-2],[-9,1,3],[2,10,-8],[-8,-1,7],[-2,7,-2],[-7,-1,-1],[-4,-1,-6],[3,-8,-8],[5,7,10],[2,-6,3],[1,5,9],[-6,-8,9],[3,6,4],[-8,-9,-5],[-9,-2,5],[5,3,9],[-5,8,5],[-9,-1,10],[8,-4,-2],[-7,7,6],[-3,9,8],[-2,4,8],[9,-8,2],[-6,5,-9],[-1,6,4],[-10,-2,6],[9,-4,-8],[-2,2,5],[-7,6,3],[7,-2,3],[-4,4,4],[-7,-8,3],[5,-2,5],[-3,-10,-2],[-4,8,3],[-1,-4,4],[-7,-8,2],[-10,9,4],[-9,6,-5],[4,-9,-3],[-2,9,1],[4,2,2],[7,1,-4],[-10,1,4],[-6,5,-1],[-6,-7,10],[10,-8,8],[-6,-4,3],[-3,2,-8],[-4,-7,10],[9,10,2],[-4,6,5],[-3,-10,-2],[-6,-3,1],[-9,8,3],[-3,-3,-10],[2,7,5],[-1,5,-7],[2,1,6],[-9,-8,10],[-4,-6,3],[-1,-10,-3],[2,-5,-5],[1,-8,5],[6,-8,2],[6,8,-4],[-7,-7,5],[4,-6,-2],[3,-8,-8],[6,10,8],[3,-9,-7],[-3,-8,-3],[-10,8,-6],[-7,-6,2],[2,7,4],[-4,-9,-8],[-6,1,1],[6,-1,-9],[7,-7,-5],[-6,-9,-6],[8,1,-3],[-6,-10,-4],[2,-6,6],[-1,-3,5],[-9,4,-6],[2,2,-3],[-10,5,-5],[5,-9,-10],[6,6,-2],[-9,4,9],[-4,3,-4],[-1,3,-6],[-5,8,10],[6,1,-9],[-3,-4,-2],[6,-5,3],[3,-4,10],[-7,-1,-6],[4,10,4],[-8,6,5],[-8,5,9],[-3,-2,1],[8,-6,4],[1,5,-3],[9,-9,7],[4,-6,9],[6,10,-10],[1,-10,7],[10,1,-7],[6,8,-2],[9,2,-4],[-1,-4,10],[1,-4,-8],[-4,-8,6],[1,-3,5],[-6,9,2],[-9,-6,5],[1,-5,6],[5,-4,6],[10,1,-10],[7,3,-4],[-1,-9,9],[1,9,-2],[-3,-6,2],[6,1,3],[4,-9,-8],[-1,7,-6],[-3,6,-4],[6,7,-4],[-5,-1,6],[10,-8,8],[-2,-4,10],[-7,6,-4],[4,-8,3],[2,-2,4],[8,9,-3],[-1,5,-3],[-7,7,-4],[4,2,-10],[3,1,-6],[-5,-9,2],[1,-6,-1],[1,-9,-1],[-9,2,-8],[4,-4,-9],[2,-7,-8],[2,2,-6],[-8,9,5],[-2,-7,-6],[9,-8,-9],[-3,1,-1],[-9,-8,2],[2,-1,7],[2,-10,6],[-4,8,-5],[-7,7,10],[-6,-2,8],[8,-3,-10],[3,-10,1],[-1,-8,-4],[-7,5,10],[-1,-4,1],[-6,-1,-8],[-7,-5,5],[2,10,6],[-5,7,-6],[-5,3,9],[-3,-5,-4],[-9,1,10],[1,-2,4],[-7,3,-10],[2,6,-7],[1,2,8],[6,-8,1],[-5,-10,7],[6,-4,9],[8,1,7],[10,2,2],[1,5,-5],[7,-3,6],[2,4,-1],[-2,-4,-2],[5,-1,-8],[-4,10,-6],[10,-6,10],[-2,6,-10],[1,-5,-5],[8,-10,6],[1,-7,-1],[-8,6,-3],[8,1,-3],[10,-1,9],[-1,-7,-7],[1,4,8],[10,-8,2],[5,9,1],[-6,-6,-7],[6,-3,10],[-5,7,-8],[-5,-3,-5],[4,-2,-7],[-5,-5,10],[7,1,-9],[9,4,3],[10,-8,-3],[-5,-4,-2],[-3,4,9],[1,9,3],[5,-4,-7],[-8,-7,10],[-1,6,4],[-8,4,-7],[5,-6,-10],[-4,2,-1],[-5,6,7],[-1,-2,6],[5,-3,6],[-10,7,-7],[9,-1,9],[10,3,7],[1,-10,7],[1,2,8],[5,10,8],[-9,1,7],[-4,-6,-2],[-8,-1,8],[-6,9,-2],[-9,9,-8],[-9,1,7],[-9,-5,-7],[-8,-2,3],[8,-8,9],[-5,8,8],[-8,-3,6],[-9,10,-10],[2,3,-8],[3,-6,-2],[-4,3,-9],[-8,-9,-8],[-10,2,2],[8,-9,-8],[-7,-2,4],[10,-10,-10],[6,-6,10],[2,4,1],[-5,9,-1],[-10,8,3],[-5,-1,-6],[4,10,8],[7,-9,3],[6,-2,1],[-4,2,-4],[-5,6,4],[9,-5,-1],[9,3,8],[10,4,-10],[5,-6,7],[2,1,-10],[-1,4,-7],[6,-2,4],[5,-3,-7],[-3,-1,9],[-1,2,10],[-6,10,-6],[-4,1,-3],[3,10,-6],[2,-7,-8],[-1,-9,10],[4,10,-5],[-10,-9,4],[-7,-10,6],[-4,-5,9],[1,-4,-2],[10,8,1],[8,-4,-6],[1,-7,2],[8,10,-9],[9,-1,-10],[7,1,4],[1,-7,9],[1,-9,-2],[2,9,5],[2,-9,9],[6,-3,-1],[10,7,5],[1,5,-6],[10,-6,1],[8,5,6],[1,10,-10],[-9,3,10],[-3,5,10],[6,1,-1],[-3,-6,8],[-4,6,3],[7,8,1],[7,6,3],[-5,-6,-2],[9,-7,8],[6,6,-8],[-8,2,-4],[-4,8,-4],[8,1,6],[-2,-9,-9],[-6,-8,7],[-3,2,10],[8,-6,-6],[7,-10,9],[-2,-10,-9],[7,-1,8],[-3,-4,-6],[-1,-10,3],[9,-1,10],[4,8,4],[-2,3,-8],[-3,3,7],[2,6,-7],[8,-10,-5],[-9,-4,-5],[-4,-1,-2],[1,-1,-3],[-4,4,-6],[10,7,5],[2,-4,-10],[-7,8,3],[-9,7,9],[-6,-4,-4],[3,4,-3],[5,2,-6],[-10,7,2],[-10,-4,-1],[-7,-7,-1],[-9,2,6],[4,-3,-1],[-1,1,-9],[-7,6,-5],[8,3,-1],[6,-9,-5],[6,-8,-8],[-7,2,-6],[-2,9,8],[-4,6,-2],[4,-8,4],[9,5,-8],[-10,3,-6],[-2,-3,8],[-5,-6,2],[9,-3,8],[-10,-9,8],[-7,4,-8],[-8,1,-1],[1,-1,-10],[-6,-8,4],[8,7,-7],[7,-1,4],[3,2,-3],[3,3,-2],[7,-10,7],[-3,9,4],[-4,2,4],[-7,-9,-3],[3,6,-9],[9,-6,-1],[4,-8,3],[-9,-3,-2],[-8,-5,9],[-9,1,-10],[-6,6,-9],[-5,-10,-8],[-6,-2,9],[-7,-5,3],[-8,10,-8],[2,3,-5],[5,-7,-4],[-10,3,9],[-7,8,7],[-10,4,6],[2,5,6],[-8,-2,5],[-10,-6,8],[5,-2,-9],[-2,5,7],[-7,9,-4],[6,3,-9],[-3,5,3],[5,-1,1],[-5,7,9],[1,-4,-2],[5,-2,-3],[1,1,-5],[1,2,-6],[-10,-4,-1],[2,2,4],[6,-9,10],[-9,-10,-8],[5,-7,-9],[-8,4,-5],[-8,6,-3],[-2,-10,9],[-5,-2,1],[3,9,-2],[3,-9,-3],[-3,-3,9],[-9,-9,5],[2,6,-6],[6,-10,-9],[5,-2,10],[-1,6,-4],[-4,-7,-4],[8,-2,-10],[9,10,-2],[4,3,-4],[-9,8,2],[10,4,8],[-10,6,3],[2,3,-3],[-1,4,1],[8,4,-7],[7,2,-7],[-1,-9,2]], dtype = "int8")#candidate|4357|(546, 3)|const|int8
call_4356 = relay.TupleGetItem(func_3544_call(relay.reshape(const_4357.astype('int8'), [13, 14, 9]), relay.reshape(call_4350.astype('uint8'), [520, 1]), ), 2)
call_4358 = relay.TupleGetItem(func_3548_call(relay.reshape(const_4357.astype('int8'), [13, 14, 9]), relay.reshape(call_4350.astype('uint8'), [520, 1]), ), 2)
uop_4367 = relay.tan(const_4357.astype('float64')) # shape=(546, 3)
func_3890_call = mod.get_global_var('func_3890')
func_3891_call = mutated_mod.get_global_var('func_3891')
call_4370 = relay.TupleGetItem(func_3890_call(), 0)
call_4371 = relay.TupleGetItem(func_3891_call(), 0)
func_4283_call = mod.get_global_var('func_4283')
func_4284_call = mutated_mod.get_global_var('func_4284')
call_4379 = relay.TupleGetItem(func_4283_call(), 2)
call_4380 = relay.TupleGetItem(func_4284_call(), 2)
func_2801_call = mod.get_global_var('func_2801')
func_2803_call = mutated_mod.get_global_var('func_2803')
call_4382 = func_2801_call()
call_4383 = func_2801_call()
func_181_call = mod.get_global_var('func_181')
func_184_call = mutated_mod.get_global_var('func_184')
const_4390 = relay.const([3,5,2,1,-5,9,8,-6,9,7,6,5,6,6,-7,9,-1,-3,4,-8,5,-6,1,7,7,-9,5,2,3,5,-7,10,-9,-10,-7,1,-8,-6,-10,-9,6,9,4,-7,9,9,-4,-3,1,5,4,1,-4,10,-1,2,7,-1,3,9,9,8,-6,6,4,7,-7,1,7,-9,2,-6,-3,1,-4,-7,-6,-6,-6,10,-6,-2,-7,-8,6,-1,-7,7,-5,-7,1,-1,9,-1,-4,8,10,-4,-3,-1,8,-7,-10,-6,-7,3,-6,-4,4,1,6,7,-9,1,3,-1,6,7,-6,-1,5,8,-8,6,6,1,7,6,-1,8,-10,5,10,-2,-5,7,8,-9,10,10,3,7,-1,5,-3,6,-3,1,-4,-10,-7,7,4,2], dtype = "uint16")#candidate|4390|(154,)|const|uint16
call_4389 = relay.TupleGetItem(func_181_call(relay.reshape(const_4390.astype('uint16'), [14, 11, 1])), 0)
call_4391 = relay.TupleGetItem(func_184_call(relay.reshape(const_4390.astype('uint16'), [14, 11, 1])), 0)
output = relay.Tuple([call_4350,call_4356,uop_4367,call_4370,call_4379,call_4382,call_4389,const_4390,])
output2 = relay.Tuple([call_4351,call_4358,uop_4367,call_4371,call_4380,call_4383,call_4391,const_4390,])
func_4394 = relay.Function([], output)
mod['func_4394'] = func_4394
mod = relay.transform.InferType()(mod)
output = func_4394()
func_4395 = relay.Function([], output)
mutated_mod['func_4395'] = func_4395
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4283_call = mod.get_global_var('func_4283')
func_4284_call = mutated_mod.get_global_var('func_4284')
call_4447 = relay.TupleGetItem(func_4283_call(), 0)
call_4448 = relay.TupleGetItem(func_4284_call(), 0)
func_3296_call = mod.get_global_var('func_3296')
func_3298_call = mutated_mod.get_global_var('func_3298')
call_4455 = func_3296_call()
call_4456 = func_3296_call()
const_4458 = relay.const([5.244222,2.523446,7.825076,3.971021,-2.921224,2.982340,8.484535,8.312330,8.036728,-9.126131,-9.475980,-5.720669,0.218479,1.003697,2.747119,2.236944,5.929856,-0.754178,-9.431431,1.956589,2.030247,1.147493,-1.349761,1.703971,-2.755378,-9.902952,6.621178,-0.417988,-4.952658,-5.028383,-5.184350,6.714360,-2.497136,-7.116502,3.677803,8.748249,-3.887277,8.987212,3.317994,-0.043218,0.929516,1.827543,4.100606,2.773100,7.104262,4.331474,-9.756327,0.157601,-9.458700,0.434378,-0.053768,3.172380,4.051167,3.851887,1.860889,-8.284057,-5.470239,8.623357,4.914856,6.261192,-1.371404,-3.365989,5.781810,-0.115370,7.149977,-5.293293,-7.449454,-7.543694,-3.227336,1.365721,6.514827,-4.446873,9.278947,3.801648,7.604138,2.967789,1.785503,-4.207799,-8.989300,4.224690,-2.432537,5.737233,3.219818,-7.059852,0.286410,8.087610,4.913086,-4.979746,-9.080859,4.418751,-0.969697,1.235891,-0.969093,5.535158,-2.921797,-4.281974,-8.730146,-1.769805,3.382115,8.548721,-5.487804,3.574103,1.952236,-5.525759,6.576428,1.596043,-1.956373,6.494434,-2.698322,5.147459,8.501404,1.113592,0.247702,7.760976,-1.195122,5.971714,-2.075457,-9.810977,-4.734836,4.070559,-1.138220,-5.003593,3.012344,3.491700,-3.204242,6.104760,-6.743559,9.409111,-2.800174,-3.618391,8.846983,1.105257,-9.010266,9.563055,-8.707796,-2.670492,3.483428,6.035570,-9.654646,-6.323091,-9.419171,4.699016,-7.891018,-7.724042,3.339140,4.995277,1.782640,-8.087686,-2.897966,-6.389219,-3.064599,4.316308,3.626650,2.224116,5.420651,-8.920903,4.455625,-6.955747,-3.006652,-0.575160,0.941639,9.120230,-5.089648,-5.045940,7.479205,0.173492,5.037860,-1.304538,6.657606,0.819398,2.174457,-8.009587,8.949323,2.305067,-0.522681,7.525519,6.098280,-2.396594,9.372318,2.152743,8.735765,-6.227641,3.065095,-8.727203,-2.989383,-7.421606,2.809361,-5.685050,6.825252,6.067219,8.393485,-9.293959,5.927057,-1.028102,8.527047,2.059967,-3.286326,-8.484941,-4.049568,5.174560,-8.600433,0.010440,-0.950065,-9.014041,6.232876,0.276711,-5.385594,0.568308,-4.466284,-8.055698,4.555375,4.302803,-7.818245,-3.497075,-6.396880,4.362087,1.198263,-8.349143,8.940136,3.120357,-0.440385,7.956425,-6.392836,-7.551685,1.822894,8.111916,7.406355,-0.117508,-9.843076,-2.790041,-1.032825,8.643363,-9.162487,-6.940857,-9.382510,-6.197754,-1.357928,7.654871,8.417263,-6.300344,4.748065,6.900559,-3.227807,-4.721798,-1.009542,9.062588,-6.479490,-7.153275,-5.529128,-5.579755,3.508899,-9.506383,2.706242,-2.995342,4.930007,8.358846,-1.871806,7.954886,-2.927649,8.370214,6.650131,-0.885201,7.736446,-6.251850,9.384278,-2.739209,-1.765981,-9.817450,4.944419,-5.676081,6.941544,5.547878,-2.817442,-8.091496,-8.113838,-4.536265,-0.093739,8.335525,0.749866,-0.490219,8.970798,7.853451,5.921706,0.075560,2.438936,7.929870,0.577266,-2.094019,-4.819560,-5.524605,3.617852,-9.684239,9.529480,1.405227,9.520112,2.248842,4.269023,-8.605139,7.056502,0.679088,6.459715,5.575097,8.064899,7.655772,0.890985,-5.857033,-4.344811,-5.382317,-3.802116,-7.848310,6.854051,-6.415476,0.570164,5.344696,-7.960504,5.229111,-0.907018,-4.359415,-5.799935,9.424279,-6.627321,-7.484543,-2.221550,-7.777713,7.526099,-0.726290,6.735489,3.516380,-8.171491,7.686518,5.485824,-4.567328,0.556616,4.795995,-8.726404,2.932848,-0.769668,0.456305,7.365512,9.893891,5.996580,3.130116,8.847508,5.274394,-4.082601,-6.722795,0.421983,1.404469,-3.419816,-8.288868,8.897896,7.376160,-6.929333,-6.256237,-2.551646,-9.390393,9.128753,-0.309009,-1.669632,-9.394738,-9.889001,-3.233548,-6.351090,4.443575,-0.667012,4.087085,5.677985,7.309765,-8.315092,4.705918,2.093563,-0.212323,-2.624561,8.922785,-7.276745,8.702593,4.629789,-6.077295,8.861040,-8.379586,5.325035,2.562732,-4.020327,-4.045784,-0.508400,5.019977,4.857382,-5.377901,0.192636,-9.556367,-1.986904,-5.708527,1.599475,7.829598,-0.448232,-2.652476,8.467543,0.024561,-3.939046,-9.838781,9.215593,2.401266,4.323694,-8.425731,6.975298,-3.840848,-8.834694,6.946030,6.074206,-4.157480,-2.215664,-7.636453,-1.403197,9.420396,9.898272,8.553654,-9.209676,-8.262604,2.848650,-3.950235,0.585022,-5.051581,4.825390,-3.517078,-1.778834,4.197591,5.891459,-6.559039,7.684969,6.427027,-5.253669,2.458261,0.546171,-9.393701,9.072670,9.741444,-1.906402,-1.060668,-4.314135,-4.738196,-3.537897,3.578197,9.601273,3.792152,-6.533543,-1.078826,-9.317053,4.533233,2.755183,-9.081296,-7.968321,1.759220,8.970885,-4.013441,-1.496174,-2.321497,-3.635398,9.918331,8.491368,-7.063425,1.051536,-1.814904,8.742129,4.799214,-5.042245,1.872808,3.514854,2.850660,-8.376477,-3.019542,-2.348937,4.284490,0.167910,0.563137,-8.781820,-7.130977,-0.590795,9.238180,-6.208084,-5.409167,-5.193532,8.861081,-2.439220,-7.265158,-6.060827,-5.197392,6.820333,-3.282782,-3.819070,0.561288,1.050260,-5.296147,7.614514,0.714958,-3.230379,-7.107805,3.862212,-5.543998,-1.901102,1.252382,-8.878432,8.200060,2.812883,-4.083862,6.131503,-1.285795,3.393403,-1.504976,-9.611269,-3.118644,3.812323,3.468582,-8.014779,2.345910,-7.122151,9.504958,-2.727025,-5.462452,-1.726907,5.787916], dtype = "float32")#candidate|4458|(520,)|const|float32
bop_4459 = relay.logical_and(call_4447.astype('bool'), relay.reshape(const_4458.astype('bool'), relay.shape_of(call_4447))) # shape=(520,)
bop_4462 = relay.logical_and(call_4448.astype('bool'), relay.reshape(const_4458.astype('bool'), relay.shape_of(call_4448))) # shape=(520,)
output = relay.Tuple([call_4455,bop_4459,])
output2 = relay.Tuple([call_4456,bop_4462,])
func_4463 = relay.Function([], output)
mod['func_4463'] = func_4463
mod = relay.transform.InferType()(mod)
output = func_4463()
func_4464 = relay.Function([], output)
mutated_mod['func_4464'] = func_4464
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4490 = relay.var("var_4490", dtype = "bool", shape = ())#candidate|4490|()|var|bool
var_4491 = relay.var("var_4491", dtype = "bool", shape = (3, 11, 11))#candidate|4491|(3, 11, 11)|var|bool
bop_4492 = relay.logical_and(var_4490.astype('bool'), var_4491.astype('bool')) # shape=(3, 11, 11)
func_3296_call = mod.get_global_var('func_3296')
func_3298_call = mutated_mod.get_global_var('func_3298')
call_4523 = func_3296_call()
call_4524 = func_3296_call()
func_113_call = mod.get_global_var('func_113')
func_116_call = mutated_mod.get_global_var('func_116')
const_4559 = relay.const([-4.044892,-9.926583,-2.423408,-3.932911,-6.708174,-3.502191,-8.361961,-8.450247,-5.832190,2.941776,-9.104597,5.742086,-1.973060,0.009936,5.807167,0.794651,2.894804,-1.168100,-6.697280,-6.932912,2.900770,3.278996,-6.187835,5.220229,9.333978,4.346023,-5.336937,0.919163,-6.576095,-0.226276,-0.106937,8.502246,3.447522,6.780397,8.561985,-9.266039,-9.569393,-7.601396,3.264148,0.917502,-4.952359,-6.271240,1.756921,8.211038,-1.594823,4.722921,4.261035,-0.818819,-1.237048,6.350084,-8.720245,3.966685,0.117927,9.928867,5.020717,7.080296,7.673365,-5.079613,2.368190,5.425228,-3.898388,-6.555627,0.709749,-5.321294,-7.859656,5.924174,-6.200579,6.017734,5.852188,-3.426360,-1.352246,-9.184098,-7.744243,-7.733772,5.389645,5.860922,5.841839,3.190724,6.530829,-6.902863,6.192371,-9.119886,-7.439890,-8.097707,-0.517324,-4.436847,-5.364907,-8.875570,-6.554165,0.938559,-3.329387,4.905184,-5.601255,7.278860,-8.939655,-9.135033,7.743435,9.918233,-8.016925,7.711028,4.943481,0.561542,8.588464,-4.804129,1.530928,3.272158,-5.873414,0.341227,4.695198,-6.366771,-3.826469,-1.237163,9.078673,-1.968013,5.312258,-9.747693,9.635005,-5.307366,-8.958936,-4.721491,-8.684604,6.012181,-0.027135,-4.361833,3.574225,-0.038869,4.328518,-3.754757,-3.544961,-6.728430,-3.284317,-9.057407,0.626894,-4.057348,4.225088,2.584001,-4.015541,2.334115,3.462311,8.347978,-4.874718,-8.761180,-4.573842,2.558995,6.826058,-5.753635,-4.950805,-2.892190,7.665473,4.062238,4.040920,7.253722,-8.493453,3.611830,-3.370067,-8.961529,-5.623074,-0.042188,9.619442,5.831856,0.156858,4.215996,0.003673,7.129693,-9.139021,0.180667,9.168915,-7.672257,0.069913,9.431345,-4.144509,9.425008,0.986681,4.494102,7.878808,9.941942,-3.324309,-3.413460,-1.621811,-0.315753,6.821574,3.127893,-7.885444,-6.979042,1.398173,0.861210,5.504301,-4.963984,-2.904423,-5.230722,-1.314994,9.368770,-3.794594,-5.528042,0.193116,1.865331,4.613795,-6.977740,-3.095681,6.489268,-6.461867,0.010572,9.571331,-2.141518,0.145871,1.042501,0.995041,-7.319927,6.212530,-5.765025,-2.064798,7.869711,-7.817591,7.936643,-2.411605,-4.140160,-6.320523,-9.834448,8.134369,4.277444,1.358674,5.535872,6.607815,-0.277419,-6.766779,-0.958386,1.989858,-6.162917,8.747564,-5.297365,0.966143,-9.960212,3.371023,2.202694,-8.652142,0.521924,-5.246193,-4.225290,3.673728,-5.027905,2.211350,-8.111520,-8.792746,9.188803,-1.617996,7.640345,-7.474400,0.052042,-7.975316,3.886280,-4.164193,8.782851,7.782100,-4.044145,-5.366088,-3.100661,7.945686,-2.875925,-4.010747,2.649646,-8.779664,-6.886490,7.576160,-5.557800,-5.573763,-5.784481,-0.080506,6.564844,3.048586,-6.267277,-5.404141,2.117939,5.275969,1.726345,1.304439,1.732763,4.966076,2.349338,1.702732,1.855258,0.009400,-6.014405,1.963107,7.364567,-6.571476,-1.495247,-8.498384,-3.910468,-0.052880,4.939625,0.380511,6.559133,-1.804222,7.298593,-8.754028,-5.459698,-4.728660,4.635580,-9.893693,-4.590100,7.999091,-1.534683,-6.442357,9.357067,-7.604694,1.647777,0.272007,4.626212,6.886191,-1.298888,3.154383,5.840093,4.509815,0.082690,5.877389,-1.462319,-8.500812,-1.337287,-5.780649,9.074947,3.806457,-7.365962,6.116027,-3.915859,-2.360157,-7.753532,8.031751,4.468800,5.118661,1.225730,-7.413103,0.704202,-2.774331,6.683802,1.048358,8.085605,8.514880,-1.212743,9.671775,1.795687,7.365117,8.771067,1.672275,3.669330,5.675539,7.883366,8.129841,8.226527,4.840381,-3.124572,9.933710,0.251485,0.898704,-2.956745,-0.902463,-3.386316,6.407861,6.341998,-5.584926,7.274833,2.290436,7.554626,1.242566,-3.459390,9.774523,-0.724070,-2.790896,-4.658973,3.506114,0.355028,-9.162814,2.500784,1.258535,8.948137,7.123249,-5.794539,4.935800,5.278180,-8.542963,2.614875,-8.269014,-5.800199,8.823091,-0.265746,3.594668,7.046440,1.457878,-3.487420,4.732864,-7.343155,-1.461680,5.969704,-7.337785,6.343247,-2.200054,7.746990,-9.884870,1.781149,-4.133678,-7.943761,0.038024,4.793212,-1.710470,-5.045180,9.073750,-3.415250,0.678889,-9.431796,5.818188,-2.198820,-7.064289,-7.258848,1.072462,3.035391,-0.233961,-7.716402,7.277001,-1.548801,7.540712,9.106752,-2.521371,-0.333489,5.466211,7.365101,-2.709941,-7.581394,2.981323,0.841850,-1.703101,-5.146229,-0.488870,4.215674,3.345576,3.585502,-3.768396,9.970512,0.295849,-5.506458,-6.234454,8.756360,1.771188,-1.806487,-6.946059,0.083591,-0.346383,1.223960,-7.102223,-1.016595,6.369534,-4.921217,-3.178349,-3.998241,-2.491614,-8.896359,-0.806484,9.567268,2.280337,2.910105,-6.631279,-7.253002,-5.094010,0.990299,-7.189457,-5.723143,-4.189810,2.402492,1.400608,-8.464522,-4.715039,-5.871718,-9.132821,-0.124801,8.326249,2.510442,8.914777,-5.576159,-2.300338,-3.407551,6.959037,-2.955650,-6.296202,-1.553755,5.370007,0.058664,6.848022,-0.563290,6.336265,4.572455,-8.794977,-1.211615,3.025146,-4.883460,0.726460,-4.524696,5.544212,-0.117699,6.728881,8.280429,0.489563,-2.043239,3.618578,-4.950585,-1.894058,8.827824,-8.371814,-7.367869,4.912997,5.556224,0.330965,0.912775,-7.847749,-7.253363,2.395127,-3.687944,-3.184951,3.990851,-1.282771,8.829508,-6.653544,5.841799,-6.374573,-2.916570,-6.435310,-0.083002,9.747659,5.913911,6.988179,6.011807,0.844560,4.775968,5.378948,2.441565,-0.816181,-3.677395,-6.207089,-3.167884,2.897952,-3.249071,-5.957431,4.711326,-7.503714,-7.539544,7.891021,-2.933988,4.168689,-8.919255,0.541248,-5.067102,-3.137259,-8.784052,0.802717,-4.387576,2.660477,-3.214957,4.112846,9.026355,-4.751457,-7.828951,-0.675305,9.300857,-5.361293,-9.870026,3.977542,-7.915655,7.277045,-0.319726,6.445525,1.196059,0.930646,-3.810773,3.479442,0.978343,9.371214,9.725450,-1.925424,-6.210572,0.402836,-9.231091,8.707740,-9.996199,2.181024,5.227392,9.799157,3.117241,7.060766,-8.794311,-7.111725,-0.387940,0.386005,3.277004,-2.227144,-6.274400,-5.835984,3.579044,8.302155,-3.358581,-1.617297,8.191951,-6.928224,8.784375,9.670530,-0.584990,1.494960,2.718930,2.918519,-4.529245,-7.797710,5.447304,-7.985542,5.296220,-9.640072,-9.630775,0.561201,6.441588,4.526912,3.441454,-9.889908,-4.806977,3.133126,-1.148166,-0.121432,-9.675134,7.836290,9.083958,-1.832485,-1.605285,-2.983707,-6.862848,-9.395486,0.493311,-3.720376,-3.492371,-0.986134,-0.205386,7.987771,-6.777087,0.680620,-7.961861,-0.809284,-5.938820,-3.160058,-5.609166,-8.421583,1.942903,-8.575410,-2.068763,7.580672,1.309297,4.342416,3.699343,-4.138279,-0.390431,2.182891,-4.269317,-2.736696,-1.067407,1.261389,8.637732,1.023658,3.129888,2.527589,-9.072440,-2.901784,-3.901481,7.394270,-3.584203,-6.213155,-2.276407,-8.481543,7.513848,4.901947,6.609130,-6.664262,-4.572755,7.204082,5.739529,5.204674,-2.545750,6.533940,0.592990,-3.306749,-1.883491,-0.830897,-9.534852,-7.466952,5.926321,-4.136140,-1.196797,9.908417,-8.341996,-3.548235,6.118530,-1.917338,-8.592158,1.270941,-1.548233,3.736807,-8.282031,7.484763,-7.882693,-9.326020,-5.761890,9.834156,-5.842219,7.357429,8.557284,-5.503290,-6.092023,-4.326686,8.132055,-6.205077,-0.795729,-1.345395,-9.717147,5.111969,7.872845,-0.687306,-8.454548,5.601532,8.747616,-1.452693,-4.325933,6.228145,4.705645,2.004888,7.127520,-8.444319,-9.340079,-0.881538,9.165529,3.765870,-3.063043,-7.505178,0.146196,5.245473,-0.144317,-9.787268,-3.959897,3.817149,4.515287,-5.194101,5.195646,-3.176791,-5.265506,-8.545229,1.181874,-6.760606,9.301992,-8.184523,-7.170428,3.170387,0.464205,-7.074953,-1.893674,8.894670,-7.946413,-4.818248,9.262393,4.020704,-1.971972,2.225379,-1.502763,5.968103,-9.019624,-1.011223,3.315024,4.166157,0.566158], dtype = "float64")#candidate|4559|(768,)|const|float64
call_4558 = relay.TupleGetItem(func_113_call(relay.reshape(const_4559.astype('float64'), [16, 12, 4]), relay.reshape(const_4559.astype('float64'), [16, 12, 4]), ), 0)
call_4560 = relay.TupleGetItem(func_116_call(relay.reshape(const_4559.astype('float64'), [16, 12, 4]), relay.reshape(const_4559.astype('float64'), [16, 12, 4]), ), 0)
bop_4636 = relay.not_equal(call_4558.astype('bool'), relay.reshape(const_4559.astype('bool'), relay.shape_of(call_4558))) # shape=(16, 12, 4)
bop_4639 = relay.not_equal(call_4560.astype('bool'), relay.reshape(const_4559.astype('bool'), relay.shape_of(call_4560))) # shape=(16, 12, 4)
output = relay.Tuple([bop_4492,call_4523,bop_4636,])
output2 = relay.Tuple([bop_4492,call_4524,bop_4639,])
func_4643 = relay.Function([var_4490,var_4491,], output)
mod['func_4643'] = func_4643
mod = relay.transform.InferType()(mod)
mutated_mod['func_4643'] = func_4643
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4643_call = mutated_mod.get_global_var('func_4643')
var_4645 = relay.var("var_4645", dtype = "bool", shape = ())#candidate|4645|()|var|bool
var_4646 = relay.var("var_4646", dtype = "bool", shape = (3, 11, 11))#candidate|4646|(3, 11, 11)|var|bool
call_4644 = func_4643_call(var_4645,var_4646,)
output = call_4644
func_4647 = relay.Function([var_4645,var_4646,], output)
mutated_mod['func_4647'] = func_4647
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4394_call = mod.get_global_var('func_4394')
func_4395_call = mutated_mod.get_global_var('func_4395')
call_4686 = relay.TupleGetItem(func_4394_call(), 6)
call_4687 = relay.TupleGetItem(func_4395_call(), 6)
uop_4711 = relay.tan(call_4686.astype('float64')) # shape=(14, 11, 1)
uop_4713 = relay.tan(call_4687.astype('float64')) # shape=(14, 11, 1)
bop_4714 = relay.power(call_4686.astype('float64'), relay.reshape(uop_4711.astype('float64'), relay.shape_of(call_4686))) # shape=(14, 11, 1)
bop_4717 = relay.power(call_4687.astype('float64'), relay.reshape(uop_4713.astype('float64'), relay.shape_of(call_4687))) # shape=(14, 11, 1)
bop_4722 = relay.subtract(bop_4714.astype('int32'), relay.reshape(call_4686.astype('int32'), relay.shape_of(bop_4714))) # shape=(14, 11, 1)
bop_4725 = relay.subtract(bop_4717.astype('int32'), relay.reshape(call_4687.astype('int32'), relay.shape_of(bop_4717))) # shape=(14, 11, 1)
output = relay.Tuple([bop_4722,])
output2 = relay.Tuple([bop_4725,])
func_4727 = relay.Function([], output)
mod['func_4727'] = func_4727
mod = relay.transform.InferType()(mod)
mutated_mod['func_4727'] = func_4727
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4727_call = mutated_mod.get_global_var('func_4727')
call_4728 = func_4727_call()
output = call_4728
func_4729 = relay.Function([], output)
mutated_mod['func_4729'] = func_4729
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4737 = relay.var("var_4737", dtype = "float64", shape = (6, 4, 16))#candidate|4737|(6, 4, 16)|var|float64
uop_4738 = relay.atanh(var_4737.astype('float64')) # shape=(6, 4, 16)
func_3296_call = mod.get_global_var('func_3296')
func_3298_call = mutated_mod.get_global_var('func_3298')
call_4745 = func_3296_call()
call_4746 = func_3296_call()
bop_4749 = relay.add(var_4737.astype('uint64'), relay.reshape(uop_4738.astype('uint64'), relay.shape_of(var_4737))) # shape=(6, 4, 16)
output = relay.Tuple([call_4745,bop_4749,])
output2 = relay.Tuple([call_4746,bop_4749,])
func_4759 = relay.Function([var_4737,], output)
mod['func_4759'] = func_4759
mod = relay.transform.InferType()(mod)
mutated_mod['func_4759'] = func_4759
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4760 = relay.var("var_4760", dtype = "float64", shape = (6, 4, 16))#candidate|4760|(6, 4, 16)|var|float64
func_4759_call = mutated_mod.get_global_var('func_4759')
call_4761 = func_4759_call(var_4760)
output = call_4761
func_4762 = relay.Function([var_4760], output)
mutated_mod['func_4762'] = func_4762
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3755_call = mod.get_global_var('func_3755')
func_3756_call = mutated_mod.get_global_var('func_3756')
call_4764 = func_3755_call()
call_4765 = func_3755_call()
output = call_4764
output2 = call_4765
func_4786 = relay.Function([], output)
mod['func_4786'] = func_4786
mod = relay.transform.InferType()(mod)
mutated_mod['func_4786'] = func_4786
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4786_call = mutated_mod.get_global_var('func_4786')
call_4787 = func_4786_call()
output = call_4787
func_4788 = relay.Function([], output)
mutated_mod['func_4788'] = func_4788
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3316_call = mod.get_global_var('func_3316')
func_3317_call = mutated_mod.get_global_var('func_3317')
call_4794 = relay.TupleGetItem(func_3316_call(), 0)
call_4795 = relay.TupleGetItem(func_3317_call(), 0)
func_3851_call = mod.get_global_var('func_3851')
func_3852_call = mutated_mod.get_global_var('func_3852')
call_4806 = func_3851_call()
call_4807 = func_3851_call()
output = relay.Tuple([call_4794,call_4806,])
output2 = relay.Tuple([call_4795,call_4807,])
func_4821 = relay.Function([], output)
mod['func_4821'] = func_4821
mod = relay.transform.InferType()(mod)
output = func_4821()
func_4822 = relay.Function([], output)
mutated_mod['func_4822'] = func_4822
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2801_call = mod.get_global_var('func_2801')
func_2803_call = mutated_mod.get_global_var('func_2803')
call_4823 = func_2801_call()
call_4824 = func_2801_call()
func_3168_call = mod.get_global_var('func_3168')
func_3171_call = mutated_mod.get_global_var('func_3171')
var_4834 = relay.var("var_4834", dtype = "bool", shape = ())#candidate|4834|()|var|bool
const_4835 = relay.const([False,False,True,True,False,False,False,True,False,True,True,True,True,False,True,True,True,False,False,True,True,True,False,True,True,True,False,True,False,False,True,False,True,True,True,True,True,True,False,True,True,True,False,False,True,True,True,True,True,False,False,True,True,False,False,False,True,False,False,True,False,True,False,True,False,True,True,True,True,True,True,False,True,True,False,False,True,True,True,False,True,False,True,False,False,True,True,False,True,True,True,False,False,True,True,True,True,False,False,False,False,True,False,True,True,False,True,False,True,True,False,True,True,False,True,True,True,False,True,True,True,True,True,False,False,False,True,True,True,True,True,True,True,True,False,False,True,True,False,True,False,False,False,True,False,True,True,False,False,False,True,True,True,False,True,False,False,False,True,True,False,True,False,True,False,False,True,False,False,True,True,False,True,True,False,False,False,True,False,False,True,True,False,True,True,True,True,True,False,False,True,False,True,True,True], dtype = "bool")#candidate|4835|(195,)|const|bool
call_4833 = relay.TupleGetItem(func_3168_call(relay.reshape(var_4834.astype('bool'), []), relay.reshape(const_4835.astype('bool'), [195,]), ), 0)
call_4836 = relay.TupleGetItem(func_3171_call(relay.reshape(var_4834.astype('bool'), []), relay.reshape(const_4835.astype('bool'), [195,]), ), 0)
bop_4842 = relay.divide(call_4823.astype('float32'), var_4834.astype('float32')) # shape=(13, 14, 9)
bop_4845 = relay.divide(call_4824.astype('float32'), var_4834.astype('float32')) # shape=(13, 14, 9)
func_3081_call = mod.get_global_var('func_3081')
func_3083_call = mutated_mod.get_global_var('func_3083')
call_4848 = relay.TupleGetItem(func_3081_call(), 0)
call_4849 = relay.TupleGetItem(func_3083_call(), 0)
func_4337_call = mod.get_global_var('func_4337')
func_4340_call = mutated_mod.get_global_var('func_4340')
call_4854 = relay.TupleGetItem(func_4337_call(relay.reshape(call_4848.astype('float32'), [520,])), 1)
call_4855 = relay.TupleGetItem(func_4340_call(relay.reshape(call_4848.astype('float32'), [520,])), 1)
output = relay.Tuple([call_4833,const_4835,bop_4842,call_4848,call_4854,])
output2 = relay.Tuple([call_4836,const_4835,bop_4845,call_4849,call_4855,])
func_4859 = relay.Function([var_4834,], output)
mod['func_4859'] = func_4859
mod = relay.transform.InferType()(mod)
var_4860 = relay.var("var_4860", dtype = "bool", shape = ())#candidate|4860|()|var|bool
output = func_4859(var_4860)
func_4861 = relay.Function([var_4860], output)
mutated_mod['func_4861'] = func_4861
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3859_call = mod.get_global_var('func_3859')
func_3860_call = mutated_mod.get_global_var('func_3860')
call_4863 = func_3859_call()
call_4864 = func_3859_call()
var_4869 = relay.var("var_4869", dtype = "int8", shape = (13, 14, 9))#candidate|4869|(13, 14, 9)|var|int8
bop_4870 = relay.floor_mod(call_4863.astype('float64'), relay.reshape(var_4869.astype('float64'), relay.shape_of(call_4863))) # shape=(13, 14, 9)
bop_4873 = relay.floor_mod(call_4864.astype('float64'), relay.reshape(var_4869.astype('float64'), relay.shape_of(call_4864))) # shape=(13, 14, 9)
output = relay.Tuple([bop_4870,])
output2 = relay.Tuple([bop_4873,])
func_4880 = relay.Function([var_4869,], output)
mod['func_4880'] = func_4880
mod = relay.transform.InferType()(mod)
var_4881 = relay.var("var_4881", dtype = "int8", shape = (13, 14, 9))#candidate|4881|(13, 14, 9)|var|int8
output = func_4880(var_4881)
func_4882 = relay.Function([var_4881], output)
mutated_mod['func_4882'] = func_4882
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4463_call = mod.get_global_var('func_4463')
func_4464_call = mutated_mod.get_global_var('func_4464')
call_4929 = relay.TupleGetItem(func_4463_call(), 1)
call_4930 = relay.TupleGetItem(func_4464_call(), 1)
uop_4934 = relay.log2(call_4929.astype('float32')) # shape=(520,)
uop_4936 = relay.log2(call_4930.astype('float32')) # shape=(520,)
func_4337_call = mod.get_global_var('func_4337')
func_4340_call = mutated_mod.get_global_var('func_4340')
call_4937 = relay.TupleGetItem(func_4337_call(relay.reshape(uop_4934.astype('float32'), [520,])), 0)
call_4938 = relay.TupleGetItem(func_4340_call(relay.reshape(uop_4934.astype('float32'), [520,])), 0)
output = relay.Tuple([uop_4934,call_4937,])
output2 = relay.Tuple([uop_4936,call_4938,])
func_4948 = relay.Function([], output)
mod['func_4948'] = func_4948
mod = relay.transform.InferType()(mod)
output = func_4948()
func_4949 = relay.Function([], output)
mutated_mod['func_4949'] = func_4949
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3851_call = mod.get_global_var('func_3851')
func_3852_call = mutated_mod.get_global_var('func_3852')
call_4957 = func_3851_call()
call_4958 = func_3851_call()
uop_4970 = relay.sinh(call_4957.astype('float64')) # shape=(520,)
uop_4972 = relay.sinh(call_4958.astype('float64')) # shape=(520,)
uop_4973 = relay.log(uop_4970.astype('float64')) # shape=(520,)
uop_4975 = relay.log(uop_4972.astype('float64')) # shape=(520,)
output = uop_4973
output2 = uop_4975
func_4982 = relay.Function([], output)
mod['func_4982'] = func_4982
mod = relay.transform.InferType()(mod)
output = func_4982()
func_4983 = relay.Function([], output)
mutated_mod['func_4983'] = func_4983
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5022 = relay.var("var_5022", dtype = "float32", shape = ())#candidate|5022|()|var|float32
const_5023 = relay.const([[[-4.443834,-8.674490,9.359688,8.257178,8.595935,-2.212338,-9.951236,6.342255,-2.308904,4.706715,8.300607,-0.421122,2.016041,-8.420947],[6.142873,6.626564,0.833676,8.039092,0.534024,-6.025421,-0.382344,-3.930849,2.595178,6.666854,-8.723543,9.393146,-7.112567,-2.586036],[0.259928,-1.389588,-5.667065,8.633931,3.269279,3.617088,5.016430,1.999285,-8.220298,-3.615072,4.540928,3.726345,-6.215725,9.495676]],[[-7.991285,-1.077927,-4.203056,-5.493256,4.674555,-1.223620,-4.478992,6.957363,-4.419589,4.417295,-8.647456,-6.731368,0.566587,8.349532],[-9.212148,4.573681,-3.194768,3.503779,-3.944127,-3.405478,1.540210,-3.908246,-3.062908,8.697944,-2.996997,9.171167,-9.316319,-2.954294],[0.903436,8.272878,-7.845565,-3.659047,4.211017,7.601012,6.892002,8.938726,-4.875730,7.463838,0.758747,0.264171,0.167908,-5.740614]],[[-9.207116,-0.160037,-7.621632,-6.666454,-7.434105,8.637966,-6.341558,2.589335,-4.838239,-0.719914,-1.769897,0.493726,-1.560864,8.680695],[8.945751,7.220887,-1.682579,9.309046,3.171648,2.733982,-4.726536,6.325207,0.482900,4.999594,6.839975,-9.363288,1.137987,5.333560],[6.512512,8.145447,-6.664444,-4.105732,-2.484657,1.187394,1.190482,7.777578,-8.830069,-7.215816,8.817080,5.661090,5.231894,-0.670993]],[[-5.558649,-2.742941,-0.692300,-6.918879,-5.668193,3.724893,3.285630,7.065134,6.254242,-3.755262,9.832000,5.438428,-0.178213,-4.207151],[2.882645,-6.733932,-1.752286,2.478304,8.419144,-0.910050,-4.986622,-2.538197,-7.176840,7.871590,3.087999,4.389796,-9.682761,1.799429],[-4.110604,6.733144,1.371696,5.290221,-4.190076,-2.228872,-9.107867,-4.291510,5.932815,-4.788095,-0.762733,4.590042,-7.422916,-0.345124]],[[-3.622416,7.604787,0.660119,-6.575297,4.759866,7.878095,-4.512417,1.320175,-1.285043,3.960847,-0.651335,2.312393,9.314991,-7.124221],[-6.285951,9.498556,5.526374,1.282887,2.602192,5.839665,4.661027,-1.149150,-1.003949,-7.343515,8.098962,-4.888903,-1.297644,-5.802269],[1.521778,4.359567,-7.395943,-6.821101,6.925145,-8.118884,1.841737,1.805995,-0.393607,-3.852481,3.077452,7.392483,-2.550559,2.718497]],[[-3.709275,2.238355,-7.669976,5.159256,9.952678,-5.246572,5.934461,9.773334,-1.848671,1.732607,-7.960455,-0.188152,-7.205803,2.620119],[9.739368,1.895052,-4.370340,5.675655,4.568953,0.381216,-6.591208,-8.873963,6.865883,-6.456051,-3.870336,-0.601169,9.739415,9.243148],[1.624233,7.690476,0.037483,-6.859122,1.676547,-6.060170,-4.136465,8.704579,-6.945769,-4.531771,7.150588,5.974683,-1.592019,-6.444403]],[[-2.973309,0.155872,-3.443507,6.701056,-2.078790,-6.181423,7.212455,-0.447443,-5.730901,6.341638,7.534967,-8.713087,-6.649258,1.283947],[-4.371214,4.451389,2.783540,-0.012104,6.441186,5.062369,0.220599,1.305199,-1.584082,-7.456475,9.645893,8.097615,5.666761,9.285996],[-6.761100,-0.146474,-8.827796,8.913394,-1.296808,-1.305614,9.582739,7.915354,8.992978,-5.671730,9.541079,-4.053553,-7.476029,5.179425]]], dtype = "float32")#candidate|5023|(7, 3, 14)|const|float32
bop_5024 = relay.floor_mod(var_5022.astype('float32'), const_5023.astype('float32')) # shape=(7, 3, 14)
bop_5044 = relay.bitwise_xor(const_5023.astype('int32'), relay.reshape(bop_5024.astype('int32'), relay.shape_of(const_5023))) # shape=(7, 3, 14)
func_4982_call = mod.get_global_var('func_4982')
func_4983_call = mutated_mod.get_global_var('func_4983')
call_5049 = func_4982_call()
call_5050 = func_4982_call()
const_5051 = relay.const([[[-9.027378,1.481997,-3.633415,8.713800,-9.812728,5.159844,5.438507,-8.362662,-5.517493],[4.931490,4.659975,0.944947,-2.517227,-2.908526,-8.941676,7.688822,4.246434,-3.258917],[-5.612865,0.611256,-7.506808,-7.268585,-6.762377,-1.190510,-9.270219,-2.988701,3.726172],[4.004230,-5.517862,3.378374,5.232501,-4.887071,9.163377,-8.739391,-0.548963,-9.188292],[-6.379006,-3.774121,-1.282716,3.030806,4.761259,-9.088208,-8.918773,-8.959010,-8.154620],[7.387473,-4.067729,-7.631170,-0.830297,-0.288369,-6.407114,0.656837,0.587013,9.078560],[-4.040188,6.195399,-4.788781,9.754684,6.133879,-3.636888,8.851157,6.161024,5.602470],[-6.418709,-1.016615,-7.025368,6.435605,-8.827532,0.223274,-7.803126,-1.751215,3.370531],[-9.189266,6.903952,8.269886,6.907016,2.480275,-1.770717,-0.838700,8.498548,9.658540],[-0.099627,7.507973,-0.022280,-2.421582,2.509355,-0.655046,-9.379076,1.757216,-8.070682],[2.422294,0.378740,-2.323213,8.881720,-3.201593,1.062778,-1.784456,6.456680,-4.878907],[-3.208531,-9.901121,-1.887710,5.928146,4.997335,-0.276576,1.778183,0.679911,1.663807],[-2.021136,3.174754,6.497282,0.228443,-0.359134,7.794168,-3.587876,0.371790,9.470285],[1.678060,-3.269294,2.409548,-9.856714,-0.610957,-0.028137,7.724476,-8.674516,3.661271],[9.537194,0.862381,4.600121,7.923852,1.217915,0.694060,-7.405025,5.300192,9.504873]],[[1.039431,9.402873,-4.877745,2.598522,-1.386118,-3.039995,6.990696,-2.482494,0.959992],[-2.908874,6.123944,6.823494,-6.902109,2.237239,6.065931,7.470434,-6.367798,-3.643979],[-2.738159,-8.579629,-8.275785,-5.160868,9.647968,-5.230314,3.534311,5.966049,-9.798019],[5.438889,-6.073867,-8.986031,2.835228,-8.792478,-6.825916,-1.908634,5.944219,-9.374224],[0.926862,5.985045,6.964000,3.992553,-4.810269,-2.617459,-4.071263,-8.570099,-1.039745],[-0.261699,-4.870496,-6.977674,9.223649,6.780309,3.743656,-8.170822,-3.567672,1.978599],[-2.459182,-7.713579,7.896488,8.027163,-9.170486,-7.963221,3.087549,2.985307,-9.027027],[-1.441716,-1.368013,-1.259741,6.898332,5.416979,-9.813350,-4.710803,9.134907,-2.061638],[4.168500,-6.062269,8.701434,-1.020842,7.978465,-5.301217,2.524916,-4.033025,-8.737991],[-8.990457,5.387100,5.464942,-4.650102,-6.520478,3.033528,5.309462,3.804532,-1.574301],[-4.780867,0.821106,-7.040732,9.651065,-7.003165,-9.189047,-3.704034,0.753568,-9.490611],[-4.180276,-9.072081,-0.005560,4.777963,-3.119995,-7.414419,8.981957,6.755939,-9.801506],[-7.391056,-3.009110,9.124549,8.742084,4.573071,-8.853690,0.075284,-6.220710,0.377914],[5.822192,-2.009084,0.885612,8.067301,-5.819249,1.785238,-2.815421,-0.848250,8.202539],[4.555719,-5.149220,3.694615,-3.405547,6.822670,-7.247867,-2.182795,6.703533,8.950987]],[[3.178476,0.303209,9.399143,-6.534530,-9.084592,-2.632950,9.101411,-4.625531,-3.237399],[-9.980330,-8.498469,-4.910645,-8.353043,7.492721,9.298638,2.387754,3.525685,-1.581930],[5.492962,-6.310545,-0.658781,5.502556,8.032726,6.122835,6.927375,-1.218928,1.649458],[-7.371039,2.296660,0.556367,-8.931795,7.531649,6.304024,9.801524,4.748343,-5.962400],[-6.509590,1.204060,5.575410,-8.150113,-1.573918,-3.038502,5.093895,7.321874,-6.078491],[2.205381,6.286170,-2.085057,4.240232,-1.018849,-4.388607,-2.858002,-1.143692,-8.087984],[-9.829957,6.100684,6.849840,-7.669836,-9.341182,-9.495663,-4.074643,-8.774034,-9.852766],[-4.076400,-0.983402,-9.968593,0.049047,3.125918,-0.580871,1.107790,-3.905605,0.331434],[-5.065753,-1.365634,-6.107579,-8.814515,1.393401,-9.762318,7.776962,9.676650,6.183268],[-7.855337,-3.085423,9.074106,4.907924,4.180683,5.310584,-9.808442,-4.261794,-2.722771],[3.348085,9.532498,4.828724,-6.017268,-4.709650,-0.656182,-2.127249,-7.999903,3.580486],[4.948983,-9.049156,-8.621606,-9.641588,3.535990,-5.716627,2.553110,-8.792399,-5.481027],[-3.584260,8.539793,-0.207709,6.106490,-5.787141,4.604972,8.707111,1.692857,6.261082],[0.915567,-6.639728,-1.866747,-0.840605,-2.666427,-3.276387,2.251692,2.514826,3.322742],[-8.642249,-1.358684,-2.411498,-8.241189,9.659839,0.097460,-1.508350,-6.571137,0.938306]],[[6.298175,-0.086973,3.176177,-5.958564,5.100524,8.716102,1.510539,2.923621,-5.329235],[2.533310,0.668269,-0.062349,6.956548,2.473706,6.071246,-9.769442,3.141354,-9.231954],[8.967794,3.035301,2.429752,7.383560,-3.026819,-8.123445,-0.475125,-1.656806,-8.298867],[-6.777506,7.399620,9.668087,-4.528709,4.443472,-3.868027,-7.318141,-7.443430,7.606471],[-6.630734,-6.436794,0.741318,-4.058552,-8.826417,-3.249859,7.842174,-6.090758,-3.645596],[-3.620459,8.454591,-3.649278,1.518173,0.532521,-0.475416,4.314098,3.539780,-4.118591],[1.878837,-0.596054,0.590647,-6.532531,0.553927,2.088345,1.982316,-7.605245,0.538119],[-6.257800,-2.979703,-2.545904,-0.994208,1.366009,4.995568,2.764650,-3.366228,-6.438719],[-4.578636,8.061414,3.980054,1.240735,-0.160840,4.274420,8.969340,-5.406841,7.678634],[-3.197800,6.109606,7.535716,5.935934,9.593029,-6.081791,3.946868,-0.007899,-0.066681],[3.203670,-9.379880,8.743694,5.665925,-7.038159,-8.787146,-6.858829,0.304005,5.060307],[-1.522793,1.795406,-8.363539,1.284530,-9.788979,-3.198857,0.925824,3.743359,2.175161],[9.328012,2.627427,5.419988,7.515389,-3.979245,6.342808,1.599358,1.874057,0.400155],[-1.717260,6.423161,-1.304579,1.669736,-0.131376,-4.360565,-9.534265,-6.799120,7.254713],[7.844279,-4.274629,2.492174,0.530764,3.830861,-6.781461,3.628684,-5.460421,3.631816]],[[-7.784249,-0.621995,7.124878,9.131230,8.429711,8.450673,6.968839,2.475283,4.397477],[8.764904,-5.094980,3.897646,2.733885,4.121753,4.967175,-8.444785,-2.950548,-5.525009],[0.810625,4.921263,-2.229203,1.686972,1.555717,7.131508,-5.312425,-2.423247,1.693047],[6.160182,-4.085203,-6.926325,2.612779,9.811913,-5.193901,-8.440442,6.276331,-4.793653],[-3.014567,7.872999,-0.783637,-6.988508,8.249439,0.884322,-4.721112,5.984090,-9.074205],[5.176041,4.138438,3.306853,-2.765181,0.688716,9.406490,3.343531,-1.563334,5.928873],[3.956874,9.824164,-9.922179,-6.308370,9.934675,8.885955,1.444195,7.352266,-7.125338],[-5.976983,-4.342211,-9.066179,0.303642,-5.377177,6.369125,0.639484,7.745811,0.388811],[4.198162,3.124482,-3.743480,-0.144111,1.722997,-6.320627,-7.313524,-9.813915,-8.460352],[-7.200595,4.223535,3.420320,7.621532,4.475851,7.460177,-8.113544,-1.320424,9.165015],[1.985683,8.713502,-6.137074,-5.590431,-9.884595,0.165751,7.811176,1.080244,-2.493628],[4.024161,9.728146,1.044411,-9.236404,2.032114,7.240322,0.357922,1.489191,3.786767],[-5.305645,-8.229776,-0.607577,0.265555,-9.153611,-4.252487,-1.076564,-9.383524,1.660335],[-4.124575,8.615387,-8.463333,5.210407,8.941146,-5.812784,-9.113045,-5.261357,-1.632178],[-9.915879,3.772865,-3.479861,-6.381081,3.288575,-5.150264,-4.417410,-7.804347,-8.514505]],[[-3.956513,-1.909333,-8.109359,-7.267624,3.799234,-4.277954,1.779186,-1.957029,9.553647],[6.768611,1.680383,-2.749793,2.284122,-1.972469,-6.167498,-1.129187,-5.347559,8.868341],[-5.230746,8.674272,-8.408295,0.137525,7.687460,-9.444496,-2.231866,-5.210147,9.725302],[8.412835,8.392018,-9.129507,-4.834641,-7.693411,-4.666414,-6.895681,1.417593,-6.750633],[1.274460,8.962696,3.299399,7.917392,1.254331,2.526991,-7.915129,0.640828,9.441395],[9.211614,7.979090,-9.866886,6.884754,-6.776463,0.766273,6.255265,-1.933415,1.112834],[-5.944633,7.791368,-5.361250,-4.007180,5.908912,-1.478278,-9.041707,-6.877455,2.779031],[3.104386,9.295127,0.437505,-1.408246,4.840928,4.640223,6.764467,5.388370,-7.754639],[8.097707,-9.665659,-3.214926,2.393810,5.232718,-8.312426,8.502509,3.633208,4.935664],[0.744289,9.222088,-4.461968,9.706093,1.425299,-8.944627,-0.719470,-0.972412,-3.488959],[4.279718,6.136353,-3.170794,2.303392,3.200143,-2.557528,7.883587,4.740010,2.182213],[7.009645,0.592358,7.069605,-3.605526,6.370698,2.255753,-5.905597,-3.241575,3.084622],[2.722381,-3.878717,5.055702,-8.856722,-9.025738,-6.988032,8.760326,-4.371954,-9.888340],[7.648513,5.355312,4.182778,-8.350936,7.475323,-0.345386,1.008238,0.874994,-7.016448],[8.556587,1.046441,-1.537868,8.199824,9.220658,-1.110017,2.738541,5.269095,4.437193]],[[3.898920,-7.569664,-4.110836,8.382098,-7.885090,0.673202,-6.629929,8.165874,-6.508833],[3.448879,-8.456691,2.570668,-6.108728,-0.695166,6.590177,-1.295780,9.037715,6.973152],[4.413717,-7.802840,7.091439,0.561323,-2.583478,3.088035,-9.058519,-4.037712,3.695688],[-9.116735,-0.161468,1.141903,-0.044467,4.412951,-0.624172,9.006527,3.981637,-2.004928],[9.893135,-5.406135,-5.815453,-7.349593,-0.745675,7.710822,-9.960449,1.579158,-3.253807],[-1.953454,5.384984,2.443734,-2.832111,5.897616,-9.609082,-2.389703,1.846632,5.204762],[-8.394935,4.533716,-9.505463,-6.378509,-5.248286,7.154859,8.104671,3.163343,5.254517],[-2.714344,1.050793,-3.904161,7.590222,4.348836,3.930589,8.404397,-1.627180,5.739469],[5.440675,7.282647,1.221176,9.446219,-1.247373,4.506012,0.173854,9.916647,-2.094021],[-4.636362,-5.159326,-4.586213,-0.502226,3.432251,-4.452464,8.072269,-3.277489,9.475536],[4.758019,-1.006087,4.328124,-3.807432,-6.297749,3.417384,6.929517,-9.043649,6.919292],[0.981626,-0.808983,-5.502882,9.760833,2.846455,-1.667325,-8.569889,4.976408,1.072409],[-1.208476,4.431450,6.923059,4.649136,-4.241838,-2.322633,7.512950,3.667317,-5.014168],[-9.830500,8.983272,-5.453012,7.393823,7.794714,7.973469,9.693444,-1.916974,-4.502054],[-3.358894,-7.945768,-6.030984,-2.107493,8.033917,7.816940,-7.853327,7.895398,1.859707]],[[0.553856,-3.874769,7.539303,-3.158410,-1.543210,7.757870,-3.067044,-2.927060,-6.708443],[-3.522138,-8.937997,-3.748371,6.360969,-1.499095,-8.626445,-5.550572,-9.087269,1.034390],[1.775037,-8.101999,-6.024794,-8.032901,8.099541,-0.954176,5.519973,1.505965,-1.905490],[-3.544153,-0.144303,-4.921932,-6.811618,-0.925256,-0.931252,1.033790,3.370612,5.416265],[3.598281,3.030735,-5.296992,7.071955,-5.427206,-7.541305,-4.555598,-0.216287,2.043675],[-3.598714,-4.406137,-5.654959,-9.786197,-6.138233,8.702262,0.249657,1.142655,-7.012130],[-7.900512,-8.368978,-7.256493,9.253169,9.909049,3.050030,6.302325,-9.175545,-7.962683],[-1.527080,-0.743228,9.456316,-8.228831,0.945312,6.232510,0.529302,7.632933,-1.929977],[-8.264279,-5.178369,1.712063,-3.282423,7.165295,-2.430611,6.794977,-8.326033,5.145605],[-4.259722,1.435035,-9.794752,7.858639,-9.924418,5.013754,-9.179962,7.285921,2.603024],[-6.199173,6.019739,-5.993840,2.636165,-3.701491,-4.345937,4.612150,6.203881,-9.990550],[8.092834,2.058208,-9.339990,-8.819765,2.274267,3.726624,3.141619,-3.111661,-2.956237],[-5.523141,7.592279,8.466973,6.126136,-6.755737,1.092507,-6.497651,-2.379823,0.640073],[-7.088342,9.869893,6.717822,-9.719742,-9.221641,3.160972,1.712280,-0.823620,-3.235926],[-7.257817,8.612450,-2.050641,8.410158,9.703252,-5.773418,-3.827001,5.265848,-0.225353]],[[8.831652,9.603904,-0.839446,-1.418508,-2.785896,-0.986510,-9.716541,-2.155551,8.613836],[4.378312,7.883300,-0.907553,6.843764,-6.014001,-3.293550,7.797860,2.098150,8.051248],[0.852204,-6.650700,-0.809922,-7.918473,7.716369,-9.707530,3.818747,-8.200114,2.827183],[-7.450491,8.176179,0.635656,-5.326817,0.827232,2.592376,1.984157,-9.064401,-1.984362],[-7.139857,-6.414234,-1.066568,-2.617624,-5.759740,-5.901916,8.117005,-1.010350,-1.987358],[-5.777260,-0.430055,-8.772387,-9.445088,-9.574161,5.259173,8.935322,1.067647,-3.419540],[3.884941,6.159609,1.799687,2.637480,-6.172064,8.540211,7.706898,8.308108,-4.870160],[3.620796,6.638710,6.035469,-1.800212,-0.100640,-1.511503,0.420093,2.390179,0.624771],[8.139537,5.222883,-1.534672,-4.134263,-7.964233,9.892508,3.878833,9.456940,-0.526248],[-5.293311,-2.879817,-2.164027,1.550304,-4.732549,-0.353205,1.097767,-9.584888,-0.805773],[4.501027,-1.592348,-2.601970,-2.892491,-3.349652,6.979368,5.993172,9.802656,-1.145216],[-3.113094,-8.799345,2.033192,3.269420,-3.775162,5.129855,-3.098237,3.659623,9.811046],[1.928169,0.940696,4.349538,-4.671637,-9.833012,-9.541660,-5.555568,-4.682282,8.554497],[8.546600,-6.121910,-7.723589,-7.704743,1.157816,5.638140,-0.317194,-7.028490,-1.016826],[-9.055600,-2.090140,9.614364,5.588942,-3.292872,-1.361045,9.029003,-1.823645,3.722956]],[[-4.677372,4.299609,4.431227,-3.543508,9.391791,3.035641,-6.583900,8.852149,3.542518],[-2.359808,-6.326966,-7.138498,-8.236803,-3.575161,-7.068206,-5.647210,-7.457533,-6.806828],[-8.815995,3.076974,6.838120,-6.210720,-9.218389,5.043865,-7.569484,-5.003919,-7.893463],[4.405699,3.972691,1.597306,7.416584,-3.522605,2.934008,8.881688,6.780543,-9.507295],[2.881224,-9.877213,-3.717173,9.931924,9.807100,1.667901,2.230476,8.485084,-7.230162],[-6.651096,-2.139742,8.533454,8.797861,0.507046,7.413995,0.376681,-0.074113,-3.104582],[8.689784,5.836996,-8.478260,-4.221405,4.511125,-7.673185,-7.156243,3.616575,5.216776],[1.767197,2.431791,4.893118,-1.106735,-6.349421,-5.601232,2.188621,-8.040410,5.819580],[0.519884,-7.270543,9.971752,-2.032717,7.791485,-8.826570,4.226318,0.372209,-8.930961],[5.766929,-8.953996,-6.571060,1.214951,-9.274562,-1.522880,-5.694357,-5.247155,8.182728],[4.842403,3.386659,8.878693,0.170340,9.401925,-4.510433,1.089190,-3.907072,7.065438],[-5.395437,-0.488852,-7.382371,-9.796237,-9.232429,-7.885919,-5.228220,-5.324408,-0.110933],[5.065218,-0.781765,6.122075,8.773526,-5.013614,-1.346255,-1.901424,-3.679290,7.517625],[9.552365,0.746739,-7.873932,1.868239,8.776459,8.680304,-6.606682,6.615027,4.571615],[2.398322,1.733594,7.642007,9.633989,7.189242,-5.267078,-0.781336,-5.878346,-6.923298]],[[3.340297,-6.073398,6.588691,5.824563,-6.655206,-6.311811,7.715153,-7.860876,3.263626],[-2.586362,0.613125,4.617115,-5.791887,-7.180405,4.208654,-0.307525,-8.891218,-0.202503],[-9.401034,8.632407,-5.941718,-7.473573,5.173714,3.325027,-7.299450,7.611943,6.092674],[-9.057357,6.017347,-5.551466,7.860213,6.957756,2.459140,6.005410,4.354293,3.358308],[-2.391662,7.037013,-5.695085,-0.862198,-4.922212,5.556560,-4.976051,-7.730020,-8.869052],[6.245524,6.348951,0.573695,-5.954597,-9.732885,-1.138431,5.711851,4.473905,-7.797405],[8.720080,0.221861,6.334944,7.198385,-7.545438,0.190493,5.572058,-9.965600,2.401716],[7.874544,-0.351034,-2.754740,4.412559,8.188264,-6.986146,5.981771,-9.293259,-5.304412],[4.049655,-3.982968,2.269101,-1.351718,-6.233032,0.099900,-8.914152,0.447849,-1.484059],[2.386698,2.200857,-1.527085,4.877152,-5.201415,-1.044072,5.139754,-9.708583,7.254055],[8.741529,-1.644342,-8.983986,1.160318,8.916405,0.477704,-2.133926,1.493862,4.692413],[-4.543162,8.821481,2.470182,3.601116,6.340567,-3.944886,5.188808,-5.568150,4.842277],[0.435056,-1.756595,8.169376,-7.858920,-2.515574,8.646897,7.352666,-8.296716,-9.573228],[3.599385,-0.853771,-7.337296,7.023526,-7.699795,2.810053,9.127930,5.829236,6.729079],[6.336070,-4.516984,-1.803638,-8.342234,3.290275,-2.559285,-6.330782,7.780138,8.800044]],[[3.718587,5.383420,-9.562485,9.739896,3.624780,4.217968,5.694893,-9.249155,8.556398],[8.760566,9.131078,-0.695749,7.456833,6.836706,-7.740542,-3.271771,7.776785,0.938936],[-7.886573,1.997213,5.325251,1.992979,-5.194589,6.625618,-4.216541,2.657672,9.211029],[0.894875,-6.616371,-7.368035,0.738038,-0.273563,-0.107928,2.322279,-1.703035,0.107837],[2.507584,-4.258362,-9.057869,1.738713,-7.964532,-7.457604,5.534772,-7.547458,-2.465781],[-9.182753,5.239708,0.623964,-9.206134,1.255112,7.152100,2.706836,9.907465,-2.712157],[8.494967,-1.184734,-3.980917,0.481998,-9.713668,3.016735,-2.880729,2.084131,-8.466584],[-5.199413,8.109916,9.262356,-9.010019,8.175178,-2.983726,0.523886,-4.037921,-2.879971],[3.099986,-5.455910,6.863794,-0.986583,9.822819,-3.068637,-4.625683,-2.157805,-3.999050],[5.567784,-2.136937,-2.946301,-4.434185,-2.670823,0.750391,-9.735731,9.190096,-5.299379],[-8.642580,-9.323742,-2.029831,-5.694747,3.037996,-4.406834,-6.673145,-8.637484,0.872867],[-6.121571,3.053147,-0.944111,7.398302,2.832292,0.881568,7.045883,-0.553333,9.065313],[-5.046496,-3.597393,-0.716566,2.016811,-0.547141,-7.325808,-1.251864,8.416969,0.405839],[-9.749813,-9.060190,0.035921,-6.630501,-5.748540,5.562014,1.500476,5.791349,2.889378],[6.366154,-3.800531,4.163887,2.168393,0.305243,9.288857,-3.415749,5.872036,4.334483]],[[-6.887513,-9.520115,-8.075990,-7.686276,2.428386,8.231383,8.496304,-5.967736,-8.842436],[-5.398024,2.548337,1.159379,7.042845,7.707342,-2.402148,6.469530,-6.462356,1.929607],[3.803513,-4.086397,4.340189,-0.631088,-9.631885,8.714715,-3.055326,-2.923217,5.850008],[-2.398299,8.645183,-2.749866,-4.840306,-3.965493,5.566926,1.025075,0.926925,8.480930],[-5.222662,-6.754734,-0.485888,1.111284,7.275856,2.381301,5.828826,2.449683,4.013349],[3.586125,-6.564371,-3.384383,5.861351,-8.630479,7.888918,-5.904592,0.713915,0.058421],[-5.848612,-3.302994,-0.021515,-2.449865,3.651191,0.479140,8.508819,-5.784398,-2.080746],[1.278461,1.381680,9.639942,-8.915870,-5.296347,-9.779952,1.244183,-1.724836,-5.624479],[6.492783,5.451860,2.113825,0.413817,0.609483,-4.480946,-0.335528,5.970625,8.643902],[7.254694,-0.366092,-3.229336,1.156277,8.873951,5.056269,-0.866393,1.847357,-2.427685],[-5.669384,0.620717,2.729233,-3.663798,-2.882352,6.891959,-2.532607,4.400707,-2.388914],[1.792398,2.968687,-3.210846,-3.727331,-6.484605,-7.326028,-1.074952,-5.678978,-7.638087],[3.167990,-7.497905,-8.495119,-1.167727,-1.277814,-1.827583,0.579276,-0.214252,-2.147029],[8.031007,7.059284,-2.543842,-0.200285,3.639283,4.562559,0.664732,-4.732909,-5.970111],[1.677350,0.924677,-8.977940,6.451693,4.829158,-2.480593,-8.254371,-1.488186,5.500225]],[[9.402690,-6.284166,6.427731,-1.992651,-8.833705,-8.357354,3.310760,6.098234,6.680111],[-1.503869,6.983235,-7.549749,-3.861420,-6.708088,-9.018642,8.980355,7.240526,-4.270365],[9.883081,2.273195,9.018744,-1.825812,-4.722326,4.400751,2.566588,-5.484787,3.652323],[7.891896,8.802634,7.151345,3.656466,1.279467,-2.645883,5.098110,-1.672667,3.323593],[-1.233588,-5.272150,-9.085155,-5.717302,-4.980249,-3.989455,7.726152,2.007870,9.021716],[6.592189,4.282183,-7.878717,-6.780925,-4.997326,-7.961267,0.942790,1.223683,5.723785],[9.574180,-5.481682,-6.177445,-6.496998,-7.168489,-7.405451,-3.180735,-8.475109,-2.866988],[6.438214,6.680759,5.415020,3.401489,-1.466302,5.428565,-8.874745,-5.198769,-2.512032],[-7.470528,-8.724158,-7.729748,-0.002804,-5.497355,-1.381488,8.604342,-6.297367,0.054583],[6.036396,-8.116552,-5.626471,0.010788,-5.969576,0.489739,6.493549,2.294284,-9.381644],[-8.801935,-6.227127,4.327145,-7.139593,-8.554706,6.703830,-1.181554,7.588736,9.635986],[-3.443402,-2.605413,-0.332568,5.217242,4.893044,9.200418,-2.873281,1.091194,8.760842],[-6.367916,0.251908,-6.892827,-8.047371,0.464573,6.155903,5.110558,-1.195864,-9.081224],[4.461096,-2.206278,2.372427,-8.659819,0.974430,-0.515443,7.107829,-5.361258,-3.016915],[0.488796,-8.750395,-7.024216,5.732442,2.036994,4.378627,-4.117772,-0.988728,-5.970756]],[[0.293406,6.523725,-2.765290,9.777019,-0.597845,-8.276238,-8.817539,-7.555012,3.114845],[-5.713074,-0.089263,-6.248961,3.580970,2.729908,4.286463,1.083984,-9.752686,7.945769],[9.552642,-3.874782,1.854989,-7.183592,6.199036,-2.584342,8.169815,7.795906,-5.764123],[9.353916,4.395467,7.756811,-5.889675,6.583647,-6.833098,8.686568,7.752201,6.232547],[5.974256,-5.241335,-1.288298,1.384213,0.199570,-3.605138,-4.063534,7.460673,-0.388162],[-4.169732,-7.611942,8.100186,-3.052642,-2.862419,6.127985,-9.844293,8.444814,4.492211],[2.591199,7.771889,3.709785,2.673355,4.122106,3.876983,8.528353,4.933211,4.382757],[-4.454973,7.710208,7.069772,8.114052,1.254551,-4.342203,-4.703660,7.790352,-0.506207],[7.354895,-1.427777,9.196607,-6.801564,6.828398,-8.755570,7.613584,2.120280,3.723005],[4.157813,-9.314012,8.392867,2.858517,3.182482,8.105090,5.773838,5.270812,4.727588],[-5.930150,3.573920,0.056645,-1.322172,9.477041,-5.437187,5.043695,6.800445,-3.473078],[-9.615362,-8.671528,9.259438,-4.003877,2.935876,-9.179288,-1.972628,-8.271842,7.874116],[4.628024,-8.114469,7.797572,3.012756,-6.326253,-8.365545,9.931124,-3.059852,-5.455018],[6.230015,8.946536,-5.828807,3.974558,-0.935135,4.212914,-6.506031,9.543041,1.729730],[4.601280,3.044716,5.694256,-2.776378,7.353397,-0.711665,-4.317694,-2.162976,-6.083659]]], dtype = "float32")#candidate|5051|(15, 15, 9)|const|float32
bop_5052 = relay.greater(var_5022.astype('bool'), const_5051.astype('bool')) # shape=(15, 15, 9)
uop_5061 = relay.sin(const_5023.astype('float64')) # shape=(7, 3, 14)
bop_5063 = relay.logical_and(uop_5061.astype('bool'), relay.reshape(bop_5044.astype('bool'), relay.shape_of(uop_5061))) # shape=(7, 3, 14)
func_2622_call = mod.get_global_var('func_2622')
func_2625_call = mutated_mod.get_global_var('func_2625')
var_5076 = relay.var("var_5076", dtype = "int8", shape = (2,))#candidate|5076|(2,)|var|int8
const_5077 = relay.const([-5,-10,6,3,-7,10,7,-3,5,3,7,7,4,2,-10,-6,-4,8,-10,-1,-6,-8,6,-7,-5,10,-10,7,-10,8,7,-5,-10,-2,-5,-7,5,-3,-9,4,5,-3,9,-8,10,-9,10,8,8,-10,3,6,-5,1,-3,5,6,-10,-9,-4,-4,3,-10,6,1,2,5,3,7,3,6,-8,7,9,-6,-2,9,-6,8,-6,-10,-4,6,-5,9,3,-6,-10,-8,-9,-2,-7,-8,-8,7,-7,2,-9,7,1,2,3,-4,-2,-10,7,4,4,6,-10,6,9,-9,6,2,3,-1,1,9,-8,-6,2,-10,4,8,1,1,4,6,-7,-7,-2,7,4,1,-5,-10,9,-5,5,6,9,-6,9,-5,2,-7,10,10,-7,9,-7,3,6,8,-3,-9,-6,-7,7,-1,6,3,-1,-2,-5,-2,-8,10,-3,9,-5,-10,3,5,-1,-1,4,3,-1,4,7,-2,-3,1,3,3,10,8,-3,5,1], dtype = "int8")#candidate|5077|(192,)|const|int8
call_5075 = func_2622_call(relay.reshape(var_5076.astype('int8'), [2, 1, 1]), relay.reshape(const_5077.astype('int8'), [2, 12, 8]), )
call_5078 = func_2622_call(relay.reshape(var_5076.astype('int8'), [2, 1, 1]), relay.reshape(const_5077.astype('int8'), [2, 12, 8]), )
func_2955_call = mod.get_global_var('func_2955')
func_2958_call = mutated_mod.get_global_var('func_2958')
const_5099 = relay.const([9.234964,5.062072,2.201538,0.129311], dtype = "float64")#candidate|5099|(4,)|const|float64
const_5100 = relay.const([-2,5,-9,7,9,6,-2,10,6,9,10,5,4,-5,-3,-1,5,1,6,-1,-1,6,3,-9,9,8,9,-9,1,-5,8,-1,3,-8,-2,-3,-3,8,-8,7,-6,7,6,8,9,2,-1,-2,-5,-3,-7,-1,9,8,-6,-5,10,8,7,3,-3,-3,10,-1,4,-3,2,3,3,1,8,4,7,4,-1,-9,-6,1,8,2,-5,4,10,1,9,-5,-9,5,-4,-1,7,-1,4,8,1,-5,6,-6,-9,2,-8,-6,-9,-4,-9,-9,-4,-9,2,2,9,2,9,4,4,7,-4,-8,4,-5,6,1,-6,-8,-8,-6,10,-4,5,-8,-3,-2,9,-7,3,-8,-8,8,-9,-6,9,-6,9,7,-6,-4,1,6,-7,5,-7,-6,-1,-2,-1,9,-8,8,-5,-3,1,1,-5,-3,2,-2,-10,7,-3,4,-5,5,-8,-3,7,5,7,-1,5,-7,-4,5,7,7,-10,7,6,1,4,-8,-1,-10,-10,-3,9,-1,8,8,7,7,-8,3,6,-7,-7,3,1,8,-6,-6,10,-7,3,-4,-3,-6,-5,5,2,-4,-1,8,-2,-3,9,3,-7,10,6,-8,4,1,4,5,-2,-2,-7,2,9,8,-5,7,-3,-1,10,-9,-5,8,-6,5,3,10,-10,-9,-10,-4,10,-8,-10,-2,-10,7,-1,7,9,5,9,-1,-8,7,9,-2,7,-2,8,-7,4,4,-2,-1,2,2,1,-2,6,-4,3,4,5,6,7,-2,1,6,-8,2,-3,5,10,1,-9,8,3,3,-7,3,-4,5,-2,9,-8,-2,-7,-4,-6,-10,-4,-6,-2,6,10,3,6,-3,1,-10,3,9,-1,-7,-2,2,7,2,9,-7,7,6,10,-4,1,9,10,-6,-2,9,-9,-9,-9,6,-9,10,4,1,-7,-4,-1,-2,2,-1,2,8,1,10,8,-1,-10,5,8,10,1,4,9,-10,-6,5,2,-9,-3,-2,-4,10,-3,10,10,-9,-5,2,10,5,4,-4,-3,9,2,9,-4,2,5,-3,5,6,4,4,-10,10,8,2,6,9,3,-8,8,-8,-3,8,10,7,-1,-8,1,9,-1,-3,2,-7,-2,4,4,-5,-3,-6,-8,-7,-8,-4,-2,-10,-1,7,7,-8,8,10,-6,-2,1,-1,5,-10,2,1,6,-6,4,-10,-9,9,4,3,8,8,5,10,7,2,3,-5,5,-6,5,10,-8,-3,-2,-2,-2,-10,8,-7,-10,-6,2,-2,5,6,5,5,-6,-6,7,-1,-8,5,2,3,-3,-7,-4,-2,8,-8,7,-8,4,-3,4,9,4,-10,-10,-10,-5,7,-5,-8,-10,-8,4,10,-2,8,-7,-9,-4,9,3,-6,4,8,4,-2,6,3,-4,7,-6,-1,3,5,-9,1,2,2,1,-5,8,3,-7,-2,-7,-8,-6,-7,-1,6,7,-5,5,4,7,-4,1,9,-2,-1,-9,-4,-10,-4,5,4,-9,8,-4,1,6,-6,-1,-4,-5,-3,-4,1,-10,-6,7,5,-8,-10,-9,-6,4,-3,9,9,-2,2,1,-1,-10,-6,-8,-1,-7,-1,-1,3,-2,-2,4,5,-4,-2,-10,-6,2,7,4,-8,-8,7,-9,5,-7,-10,-6,6,4,5,-3,-4,10,6,-9,4,5,-7,2,-4,6,-9,-1,-4,-5,10,-9,-2,6,-4,-2,2,-8,2,10,-8,-1,3,-3,8,-6,-5,-3,-4,7,-3,4,8,4,-3,-7,-5,9,-2,-2,10,7,3,-2,-8,-4,-10,8,-4,8,-9,10,5,1,-2,8,-3,5,6,4,8,6,-8,-6,7,10,10,9,9,-3,-2,-1,7,-2,7,6,6,3,-4,-8,4,-6,-8,-2,-6,-8,-7,5,6,6,5,-9,3,5,-1,-8,-1,-1,-1,7,-9,8,-5,1,-10,7,6,6,-9,9,-4,-7,3,-7,3,4,1,10,-4,-9,8,10,3,-5,7,-4,-1,7,9,10,7,1,-5,6,-4,6,3,5,-1,10,-2,-10,-5,7,-10,3,-1,5,-7,-5,-6,-2,6,8,-8,7,5,5,4,-4,-8,-10,-1,-7,6,1,5,-2,3,-10,10,-10,-5,-3,-8,-3,-3,-9,10,7,8,-9,-3,3,2,-6,-3,5,3,8,6,2,-6,6,-5,-3,10,5,4,-1,3,9,4,-3,6,10,3,-3,-3,7,1,2,-2,9,6,4,-5,-3,-1,-8,8,-10,2,-1,4,4,8,9,2,7,5,-7,-8,-1,-7,-7,1,-9,3,-9,-10,2,-8,9,8,9,-9,6,-7,10,8,-10,-7,1,10,8,-4,7,3,3,2,-5,-6,-2,-9,-6,10,-5,6,-8,7,-6,6,2,-1,-9,5,-6,8,-4,8,6,-8,4,9,2,-8,7,-4,-1,4,-8,7,-1,-1,2,9,-9,8,-2,-5,-3,5,-5,10,5,-8,-4,6,8,4,-7,7,-9,9,-2,-6,-9,6,1,10,2,9,-2,3,2,-1,10,7,5,-1,-2,5,-9,5,-8,5,4,-8,-9,-8,8,-2,-1,8,-6,-4,-7,10,-1,3,2,9,-2,-4,-8,1,-4,-4,3,1,-10,-8,6,-10,-4,6,3,-4,4,5,10,8,1,1,4,5,-8,3,-2,-1,-10,-4,4,-9,6,10,1,2,-2,8,-6,1,8,10,-9,-8,-7,1,8,2,3,10,2,10,6,1,2,5,-8,-10,7,-3,10,-8,3,4,1,-3,-7,-6,-2,-4,9,-4,6,3,2,8,1,10,-5,1,8,9,-7,-6,-10,-1,10,7,9,-9,-5,3,-4,-9,7,5,1,1,-8,7,7,-8,-3,-5,4,-5,1,-6,-1,4,-4,1,4,5,9,2,10,-7,7,-7,-5,2,8,-3,-3,-7,7,-2,10,-4,7,-8,-6,-10,-6,5,-7,9,7,6,-10,-6,-1,-9,6,-1,-9,-2,4,1,-8,1,-5,5,-4,-1,2,-3,-6,5,8,-4,6,4,-9,10,-1,-5,3,8,10,4,-7,-6,-9,-4,8,-6,6,-4,4,2,-9,2,10,-9,-9,6,-10,-8,5,8,2,6,3,-2,-6,-4,5,6,6,-6,10,9,-4,9,-9,-3,-2,-8,10,3,8,10,-3,-9,-4,2,-6,-2,-9,2,-1,-10,3,-7,2,9,-7,-1,7,-7,-6,-5,-1,-7,-1,2,-3,2,-2,8,-10,2,-8,-8,-7,-8,-6,-5,3,9,10,-5,-4,8,-7,-8,3,-2,6,-8,5,-4,-10,-7,-3,-6,-8,6,7,5,-10,8,-6,-6,10,-3,-1,-7,-8,-3,-1,-3,-7,10,-1,-7,2,4,-8,8,6,5,10,6,6,-8,8,7,-8,-9,-4,2,4,3,8,-9,5,-2,6,5,-9,1,4,-3,5,-5,-10,6,-3,-5,-2,-5,-10,4,-7,10,-1,1,6,-10,-8,1,-2,-4,-6,7,-5,5,-1,1,-5,4,-1,3,-9,-8,10,6,6,8,-9,8,-1,-7,-9,2,1,-9,-9,10,7,-6,9,8,10,-7,-5,2,5,10,-10,-9,-6,-3,-3,4,5,7,-2,9,-3,10,1,-5,1,-2,8,4,-10,-1,-2,-2,-7,-10,4,-10,8,-8,-1,-5,8,5,-9,-2,-6,3,-9,4,6,2,5,-8,1,-2,-8,-7,6,-6,9,-7,2,2,7,-7,1,-4,3,-1,-9,-9,2,5,7,5,1,2,4,-7,3,-3,-7,-1,8,-9,7,-3,-5,8,-4,-10,7,-10,-10,-9,3,7,10,2,-10,-6,-8,-5,-9,-5,-6,-10,8,1,7,9,5,-1,4,4,4,-10,-8,5,7,-2,4,-5,2,-8,-7,2,-5,-6,6,-4,9,5,10,-7,-10,2,-3,-6,-5,7,-5,6,1,8,4,-10,-7,-10,-4,8,8,-8,8,-7,10,7,-2,-3,6,10,7,-1,-4,-3,-10,2,2,-2,-6,5,4,9,-6,-8,-6,-10,-8,-7,-4,1,-1,3,-5,-4,-3,-4,1,-2,8,9,8,-8,10,1,8,-7,6,-4,4,-1,7,5,-9,-6,9,-2,3,-5,5,-7,7,4,4,4,6,-9,1,2,3,10,5,8,1,-1,1,-1,-3,-4,3,-7,5,1,-9,7,-2,3,10,5,7,10,-7,-6,10,-7,8,-1,9,-9,6,2,5,-7,-9,6,10,3,1,-6,-9,-3,7,10,-7,-8,-4,-10,8,-6,10,4,-10,-7,-6,3,6,-2,9,2,-10,-8,3,-5,-7,-9,-3,-7,1,5,9,-5,-3,1,-9,-9,-3,3,-6,8,-9,2,-3,-6,-5,4,-8,-10,-7,6,-3,-5,3,4,-8,7,-3,-9,8,-1,-6,-8,5,7,8,-8,-10,9,2,-5,8,-8,-10,7,2,-2,2,-5,7,-7,-7,8,-7,-1,10,9,-9,-1,4,9,-6,6,-1,7,5,3,-10,-9,7,7,-5,7,3,-5,8,5,-4,-5,4,-1,5,-10,4,-3,-9,-8,5,10,-7,-5,8,-10,2,7,7,-6,-1,-9,-6,-6,3,1,1,-7,8,-3,1,1,1,9,4,-4,2,2,8,-4,3,-10,-9,-5,7,7,5,1,-4,6,8,6,3,-9,-7,-1,-10,-9,8,-10,-3,-6,5,-4,10,8,10,-7,4,-4,-8,-3,10,1,-5,-4,8,-5,-7,-9,-9,-4,-2,1,-4,-9,4,3,4,-1,-5,-7,4,3,3,8,-10,10,-1,10,-10,10,-2,9,8,-7,4,3,6,-9,9,-10,2,-5,-2,10,5,-7,6,-5,5,-7,-5,-7,8,9,-7,-8,-10,-2,7,8,6,1,1,-6,5,5,6,3,10,-3,3,-4,4,9,9,-5,1,7,-9,8,6,6,-3,-6,-2,-10,10,-10,-3,6,-4,-7,7,7,-8,-2,6,6,8,4,3,-5,-1,7,-1,6,-6,-10,-8,10,2,10,-1,-1,10,-7,1,-4,-6,-6,8,2,-4,8,1,-8,10,-3,4,-10,-1,-7,-8,7,-4,10,-7,-5,-5,3,-10,9,10,-1,-7,-1,7,-3,9,-10,4,-4,-2,-2,-3,-5,7,-3,9,3,4,-6,-10,-7,-8,-3,-6,-1,-7,9,7,4,-9,3,2,4,10,6,-7,-10,-9,7,-9,6,-1,-7,-9,6,-8,6,5,-6,9,4,5,3,6,-1,-10,10,-2,-2,5,-8,7,5,-5,-8,4,-2,-7,-5,7,-5,-3,-8,9,3,-10,-9,7,10,6,6,-9,1,5,8,-1,9], dtype = "uint32")#candidate|5100|(2016,)|const|uint32
call_5098 = relay.TupleGetItem(func_2955_call(relay.reshape(const_5099.astype('float64'), [4,]), relay.reshape(const_5100.astype('uint32'), [2016,]), ), 4)
call_5101 = relay.TupleGetItem(func_2958_call(relay.reshape(const_5099.astype('float64'), [4,]), relay.reshape(const_5100.astype('uint32'), [2016,]), ), 4)
output = relay.Tuple([call_5049,bop_5052,bop_5063,call_5075,var_5076,const_5077,call_5098,const_5099,const_5100,])
output2 = relay.Tuple([call_5050,bop_5052,bop_5063,call_5078,var_5076,const_5077,call_5101,const_5099,const_5100,])
func_5103 = relay.Function([var_5022,var_5076,], output)
mod['func_5103'] = func_5103
mod = relay.transform.InferType()(mod)
var_5104 = relay.var("var_5104", dtype = "float32", shape = ())#candidate|5104|()|var|float32
var_5105 = relay.var("var_5105", dtype = "int8", shape = (2,))#candidate|5105|(2,)|var|int8
output = func_5103(var_5104,var_5105,)
func_5106 = relay.Function([var_5104,var_5105,], output)
mutated_mod['func_5106'] = func_5106
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3755_call = mod.get_global_var('func_3755')
func_3756_call = mutated_mod.get_global_var('func_3756')
call_5174 = func_3755_call()
call_5175 = func_3755_call()
output = call_5174
output2 = call_5175
func_5176 = relay.Function([], output)
mod['func_5176'] = func_5176
mod = relay.transform.InferType()(mod)
mutated_mod['func_5176'] = func_5176
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5176_call = mutated_mod.get_global_var('func_5176')
call_5177 = func_5176_call()
output = call_5177
func_5178 = relay.Function([], output)
mutated_mod['func_5178'] = func_5178
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4948_call = mod.get_global_var('func_4948')
func_4949_call = mutated_mod.get_global_var('func_4949')
call_5190 = relay.TupleGetItem(func_4948_call(), 1)
call_5191 = relay.TupleGetItem(func_4949_call(), 1)
func_5176_call = mod.get_global_var('func_5176')
func_5178_call = mutated_mod.get_global_var('func_5178')
call_5192 = func_5176_call()
call_5193 = func_5176_call()
func_4337_call = mod.get_global_var('func_4337')
func_4340_call = mutated_mod.get_global_var('func_4340')
call_5211 = relay.TupleGetItem(func_4337_call(relay.reshape(call_5190.astype('float32'), [520,])), 1)
call_5212 = relay.TupleGetItem(func_4340_call(relay.reshape(call_5190.astype('float32'), [520,])), 1)
bop_5213 = relay.mod(call_5190.astype('float32'), relay.reshape(call_5211.astype('float32'), relay.shape_of(call_5190))) # shape=(520,)
bop_5216 = relay.mod(call_5191.astype('float32'), relay.reshape(call_5212.astype('float32'), relay.shape_of(call_5191))) # shape=(520,)
output = relay.Tuple([call_5192,bop_5213,])
output2 = relay.Tuple([call_5193,bop_5216,])
func_5218 = relay.Function([], output)
mod['func_5218'] = func_5218
mod = relay.transform.InferType()(mod)
output = func_5218()
func_5219 = relay.Function([], output)
mutated_mod['func_5219'] = func_5219
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4982_call = mod.get_global_var('func_4982')
func_4983_call = mutated_mod.get_global_var('func_4983')
call_5280 = func_4982_call()
call_5281 = func_4982_call()
var_5285 = relay.var("var_5285", dtype = "float64", shape = (520,))#candidate|5285|(520,)|var|float64
bop_5286 = relay.not_equal(call_5280.astype('bool'), relay.reshape(var_5285.astype('bool'), relay.shape_of(call_5280))) # shape=(520,)
bop_5289 = relay.not_equal(call_5281.astype('bool'), relay.reshape(var_5285.astype('bool'), relay.shape_of(call_5281))) # shape=(520,)
func_3838_call = mod.get_global_var('func_3838')
func_3841_call = mutated_mod.get_global_var('func_3841')
const_5295 = relay.const([-9.684739,-1.323103,-1.187730,7.328608,-9.082269,2.831492,3.330542,0.033818,4.698673,7.267548,7.619778,0.909179,-4.534994,-7.666978,8.717755,0.924722,-2.960672,-3.447761,0.851102,4.670464,-9.704475,-3.080904,3.143400,-0.123460,-2.241239,-4.976252,8.768871,2.080413,2.843451,8.867474,-2.367369,-6.839632,-0.180363,6.231636,-2.476530,2.612428,-5.409553,7.379419,9.467363,-7.637120,0.723236,7.818145,9.132853,-9.518935,-2.894045,5.686216,-6.695328,-7.608375,3.851342,-5.082344,-7.889037,-4.507468,4.359466,-8.008741,3.213356,-4.843133,-2.765368,3.789361,6.227688,-5.535275,-4.284738,-7.359752,1.014835,3.995950,-6.804048,2.326712,-0.352388,1.821891,5.667937,-0.800669,9.662111,8.139296,3.003423,3.216508,-2.264012,-6.609337,4.677750,9.672728,2.577187,7.721095,-9.385811,6.231018,-0.268816,-8.953057,-1.496741,-5.833769,2.998453,5.828969,4.986716,7.386594,-8.654301,-7.566409,-7.072683,8.672782,-1.617566,-0.785092,1.685106,5.241094,-0.016414,9.337186,6.287895,-9.433233,6.112582,7.433026,-0.130004,-4.181747,-7.750672,9.015312,-7.262275,5.446546,6.394869,4.129420,2.613537,3.334388,-5.418872,-0.388862,-3.589583,-0.755561,2.143879,-2.919140,3.047001,-4.014447,9.155368,-6.691892,-6.719424,2.978637,9.126675,-1.589354,3.176960,6.010760,-3.312247,3.546787,-7.839420,-3.354856,5.958643,-8.575453,7.824134,4.897213,-0.605448,-9.557409,4.739137,-5.311177,-1.942056,5.265556,-7.243070,1.278212,-8.764962,-3.894987,3.278380,-5.120289,5.213756,2.485363,-3.826122,-9.673600,-8.767391,6.437679,-6.435494,7.199200,0.285096,-9.901511,9.884816,-7.698190,9.678718,-7.579966,-4.343507,9.959283,4.921447,-6.777893,9.123240,-8.680391,-5.932513,9.533589,-0.836745,0.233135,7.648633,7.012928,-7.120928,3.382640,-8.804068,-5.619184,-6.078887,8.851905,-2.727614,5.824569,-1.262874,5.495719,-5.215084,9.179809,9.598093,-0.233212,-6.062283,8.245181,9.488810,-2.057251,3.040498,-8.936485,4.707773,3.733909,-7.703076,2.960809,2.874669,3.464683,-5.971505,-8.773487,8.221572,-6.442015,-8.878588,-1.748927,-9.961514,-2.877541,0.641874,-5.704291,-2.347954,-9.236285,-4.096484,7.974217,9.168146,6.123960,6.406526,7.816403,-0.993709,-2.587299,-7.211763,6.641427,-5.661453,-7.419795,-6.418750,-3.510322,-0.468139,1.627934,-9.597980,-2.064991,5.068749,9.517053,5.960072,-6.071796,6.433242,4.303159,0.497559,-1.052529,-0.663418,-2.384139,1.980625,0.102586,3.808568,6.629957,4.564286,5.980011,1.934287,6.386080,-6.218205,1.034884,-8.318229,5.926587,5.530833,2.514607,-5.417699,-8.060766,-2.354616,5.324824,7.507471,-4.284616,5.238760,7.451791,-9.625243,0.466153,-9.475992,-4.823024,4.805223,0.499708,-2.933922,-1.068255,-3.602419,-5.861521,-0.965603,-0.825894,-3.654087,-2.568329,7.878579,5.075817,-8.843057,-0.370444,8.680601,-1.775202,-4.431533,7.902645], dtype = "float64")#candidate|5295|(286,)|const|float64
call_5294 = relay.TupleGetItem(func_3838_call(relay.reshape(const_5295.astype('float64'), [11, 2, 13])), 0)
call_5296 = relay.TupleGetItem(func_3841_call(relay.reshape(const_5295.astype('float64'), [11, 2, 13])), 0)
uop_5298 = relay.atan(var_5285.astype('float64')) # shape=(520,)
output = relay.Tuple([bop_5286,call_5294,const_5295,uop_5298,])
output2 = relay.Tuple([bop_5289,call_5296,const_5295,uop_5298,])
func_5302 = relay.Function([var_5285,], output)
mod['func_5302'] = func_5302
mod = relay.transform.InferType()(mod)
mutated_mod['func_5302'] = func_5302
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5303 = relay.var("var_5303", dtype = "float64", shape = (520,))#candidate|5303|(520,)|var|float64
func_5302_call = mutated_mod.get_global_var('func_5302')
call_5304 = func_5302_call(var_5303)
output = call_5304
func_5305 = relay.Function([var_5303], output)
mutated_mod['func_5305'] = func_5305
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3493_call = mod.get_global_var('func_3493')
func_3494_call = mutated_mod.get_global_var('func_3494')
call_5324 = relay.TupleGetItem(func_3493_call(), 6)
call_5325 = relay.TupleGetItem(func_3494_call(), 6)
output = relay.Tuple([call_5324,])
output2 = relay.Tuple([call_5325,])
func_5327 = relay.Function([], output)
mod['func_5327'] = func_5327
mod = relay.transform.InferType()(mod)
output = func_5327()
func_5328 = relay.Function([], output)
mutated_mod['func_5328'] = func_5328
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3755_call = mod.get_global_var('func_3755')
func_3756_call = mutated_mod.get_global_var('func_3756')
call_5329 = func_3755_call()
call_5330 = func_3755_call()
output = relay.Tuple([call_5329,])
output2 = relay.Tuple([call_5330,])
func_5331 = relay.Function([], output)
mod['func_5331'] = func_5331
mod = relay.transform.InferType()(mod)
output = func_5331()
func_5332 = relay.Function([], output)
mutated_mod['func_5332'] = func_5332
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5327_call = mod.get_global_var('func_5327')
func_5328_call = mutated_mod.get_global_var('func_5328')
call_5336 = relay.TupleGetItem(func_5327_call(), 0)
call_5337 = relay.TupleGetItem(func_5328_call(), 0)
func_5218_call = mod.get_global_var('func_5218')
func_5219_call = mutated_mod.get_global_var('func_5219')
call_5357 = relay.TupleGetItem(func_5218_call(), 0)
call_5358 = relay.TupleGetItem(func_5219_call(), 0)
bop_5359 = relay.add(call_5357.astype('uint64'), relay.reshape(call_5336.astype('uint64'), relay.shape_of(call_5357))) # shape=(13, 14, 9)
bop_5362 = relay.add(call_5358.astype('uint64'), relay.reshape(call_5337.astype('uint64'), relay.shape_of(call_5358))) # shape=(13, 14, 9)
output = bop_5359
output2 = bop_5362
func_5373 = relay.Function([], output)
mod['func_5373'] = func_5373
mod = relay.transform.InferType()(mod)
output = func_5373()
func_5374 = relay.Function([], output)
mutated_mod['func_5374'] = func_5374
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5388 = relay.var("var_5388", dtype = "int64", shape = (5, 9, 2))#candidate|5388|(5, 9, 2)|var|int64
const_5389 = relay.const([[[-9,9],[9,-8],[2,6],[3,-8],[-1,-9],[7,3],[1,7],[-10,-5],[-7,9]],[[-2,-7],[-7,10],[-10,-8],[-5,10],[-8,-3],[-6,-6],[9,5],[4,3],[3,2]],[[-10,-9],[-9,3],[-5,-7],[-6,3],[-1,10],[8,7],[1,10],[10,3],[2,-2]],[[8,-4],[10,7],[2,-10],[9,-4],[-9,-9],[-2,6],[2,-4],[1,7],[5,4]],[[5,-3],[-3,9],[-5,7],[7,-6],[-8,1],[-2,-4],[2,2],[-5,3],[2,-4]]], dtype = "int64")#candidate|5389|(5, 9, 2)|const|int64
bop_5390 = relay.minimum(var_5388.astype('int64'), relay.reshape(const_5389.astype('int64'), relay.shape_of(var_5388))) # shape=(5, 9, 2)
uop_5404 = relay.atanh(var_5388.astype('float32')) # shape=(5, 9, 2)
func_4643_call = mod.get_global_var('func_4643')
func_4647_call = mutated_mod.get_global_var('func_4647')
const_5407 = relay.const(False, dtype = "bool")#candidate|5407|()|const|bool
var_5408 = relay.var("var_5408", dtype = "bool", shape = (11, 33))#candidate|5408|(11, 33)|var|bool
call_5406 = relay.TupleGetItem(func_4643_call(relay.reshape(const_5407.astype('bool'), []), relay.reshape(var_5408.astype('bool'), [3, 11, 11]), ), 2)
call_5409 = relay.TupleGetItem(func_4647_call(relay.reshape(const_5407.astype('bool'), []), relay.reshape(var_5408.astype('bool'), [3, 11, 11]), ), 2)
func_3851_call = mod.get_global_var('func_3851')
func_3852_call = mutated_mod.get_global_var('func_3852')
call_5421 = func_3851_call()
call_5422 = func_3851_call()
bop_5431 = relay.right_shift(uop_5404.astype('int64'), relay.reshape(bop_5390.astype('int64'), relay.shape_of(uop_5404))) # shape=(5, 9, 2)
uop_5434 = relay.sqrt(var_5388.astype('float32')) # shape=(5, 9, 2)
func_4337_call = mod.get_global_var('func_4337')
func_4340_call = mutated_mod.get_global_var('func_4340')
call_5447 = relay.TupleGetItem(func_4337_call(relay.reshape(call_5421.astype('float32'), [520,])), 0)
call_5448 = relay.TupleGetItem(func_4340_call(relay.reshape(call_5421.astype('float32'), [520,])), 0)
uop_5454 = relay.cos(bop_5431.astype('float64')) # shape=(5, 9, 2)
uop_5457 = relay.rsqrt(const_5389.astype('float64')) # shape=(5, 9, 2)
bop_5463 = relay.logical_or(bop_5431.astype('bool'), relay.reshape(uop_5404.astype('bool'), relay.shape_of(bop_5431))) # shape=(5, 9, 2)
var_5466 = relay.var("var_5466", dtype = "float32", shape = (5, 9, 2))#candidate|5466|(5, 9, 2)|var|float32
bop_5467 = relay.add(uop_5404.astype('uint16'), relay.reshape(var_5466.astype('uint16'), relay.shape_of(uop_5404))) # shape=(5, 9, 2)
func_5176_call = mod.get_global_var('func_5176')
func_5178_call = mutated_mod.get_global_var('func_5178')
call_5482 = func_5176_call()
call_5483 = func_5176_call()
uop_5484 = relay.sigmoid(uop_5454.astype('float32')) # shape=(5, 9, 2)
func_4463_call = mod.get_global_var('func_4463')
func_4464_call = mutated_mod.get_global_var('func_4464')
call_5487 = relay.TupleGetItem(func_4463_call(), 1)
call_5488 = relay.TupleGetItem(func_4464_call(), 1)
output = relay.Tuple([call_5406,const_5407,var_5408,call_5421,uop_5434,call_5447,uop_5457,bop_5463,bop_5467,call_5482,uop_5484,call_5487,])
output2 = relay.Tuple([call_5409,const_5407,var_5408,call_5422,uop_5434,call_5448,uop_5457,bop_5463,bop_5467,call_5483,uop_5484,call_5488,])
func_5489 = relay.Function([var_5388,var_5408,var_5466,], output)
mod['func_5489'] = func_5489
mod = relay.transform.InferType()(mod)
var_5490 = relay.var("var_5490", dtype = "int64", shape = (5, 9, 2))#candidate|5490|(5, 9, 2)|var|int64
var_5491 = relay.var("var_5491", dtype = "bool", shape = (11, 33))#candidate|5491|(11, 33)|var|bool
var_5492 = relay.var("var_5492", dtype = "float32", shape = (5, 9, 2))#candidate|5492|(5, 9, 2)|var|float32
output = func_5489(var_5490,var_5491,var_5492,)
func_5493 = relay.Function([var_5490,var_5491,var_5492,], output)
mutated_mod['func_5493'] = func_5493
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5535 = relay.var("var_5535", dtype = "float64", shape = (15, 11, 2))#candidate|5535|(15, 11, 2)|var|float64
uop_5536 = relay.log10(var_5535.astype('float64')) # shape=(15, 11, 2)
bop_5548 = relay.divide(uop_5536.astype('float32'), relay.reshape(var_5535.astype('float32'), relay.shape_of(uop_5536))) # shape=(15, 11, 2)
func_113_call = mod.get_global_var('func_113')
func_116_call = mutated_mod.get_global_var('func_116')
var_5567 = relay.var("var_5567", dtype = "float64", shape = (768,))#candidate|5567|(768,)|var|float64
call_5566 = relay.TupleGetItem(func_113_call(relay.reshape(var_5567.astype('float64'), [16, 12, 4]), relay.reshape(var_5567.astype('float64'), [16, 12, 4]), ), 0)
call_5568 = relay.TupleGetItem(func_116_call(relay.reshape(var_5567.astype('float64'), [16, 12, 4]), relay.reshape(var_5567.astype('float64'), [16, 12, 4]), ), 0)
func_664_call = mod.get_global_var('func_664')
func_669_call = mutated_mod.get_global_var('func_669')
const_5571 = relay.const([False,False,False,True,False,True,False,False,False,True,False,True,True,True,True,True,False,False,True,False,True,True,False,False,False,True,False,False,False,False,False,False,True,False,True,True,False,True,True,False,True,False,True,False,True,False,True,True,False,True,True,False,False,True,False,False,False,True,False,False,True,False,False,False,True,False,False,True,True,True,True,False,True,True,True,False,True,False,True,False,True,True,False,False,False,False,False,True,True,True,True,True,True,False,True,False,False,True,True,True,True,True,False,False,False,True,True,True,True,False,True,True,True,True,True,False,False,True,True,True,False,False,False,False,False,False,False,False,True,False,False,False,True,False,True,True,True,False,False,False,False,False,True,False,True,False,False,True,False,True,True,False,True,True,False,False,True,True,False,True,True,False,True,False,False,False,True,True,False,True,False,True,True,True,True,True,False,True,False,False,False,True,False,True,True,True,True,False,False,False,True,True,False,True,True,True,True,False,False,False,True,False,True,True,False,False,False,False,True,False,False,True,False,False,False,True,True,False,True,True,False,True,False,False,False,True,True,True,True,False,True,True,False,False,False,False,False,False,False,True,False,False,False,False,True,True,True,False,True,True,False,True,False,False,True,False,False,True,True,True,True,True,False,True,True,False,False,False,False,False,True,True,True,False,True,False,True,True,False,False,False,False,True,False,True,False,False,True,True,True,False,False,False,True,False,False,True,False,False,False,False,True,True,True,True,False,True,False,True,False,False,True,False,True,True,True,False,True,False,True,True,True,False,True,False,False,True,True,False,True,True,False,True,False,False,False,True,True,True,False,True,True,False,False,True,True,True,True,True,False,False,False,True,False,True,True,False,True,False,False,False,False,True,True,False,True,False,True,False,True,False,False,False,False,False,True,True,True,False,False,True,True,False,False,True,False,True,False,True,False,False,True,False,True,True,False,False,True,False,True,False,False,True,False,False,True,False,True,False,False,False,False,True,False,False,True,False,False,True,True,False,True,True,False,True,False,False,True,True,False,False,True,False,True,True,False,False,True,False,True,False,False,True,True,False,True,False,True,True,True,False,True,True,True,True,False,True,False,True,False,False,False,True,True,True,True,True,False,False,True,True,False,True,False,False,False,True,False,True,True,False,True,False,True,True,False,True,False,False,False,True,False,False,False,True,False,True,True,False,False,False,True,False,False,True,False,False,False,True,True,True,True,False,False,False,True,False,True,False,False,True,True,False,False,True,False,False,True,True,False,True,True,True,True,True,False,False,True,False,True,False,False,False,True,False,False,False,False,True,False,False,False,True,False,False,True,False,False,False,True,False,True,True,True,False,False,True,False,False,False,True,False,False,True,True,False,True,False,False,False,False,False,True,False,False,True,True,True,False,True,False,False,False,True,False,False,False,True,True,False,True,False,False,True,False,False,True,True,False,True,False,False,True,True,False,False,False,True,True,False,False,True,True,False,True,True,True,True,False,False,True,False,False,True,True,False,True,True,False,True,False,False,False,False,True,False,False,True,False,True,False,False,False,True,True,True,False,False,False,False,False,True,False,False,True,False,True,False,True,True,False,True,True,False,True,False,False,True,True,False,False,True,True,True,False,False,False,False,False,True,True,False,False,True,False,True,True,True,False,False,False,False,False,True,False,True,True,False,True,True,True,True,False,False,False,True,False,True,True,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,True,True,False,False,False,True,False,True,True,False,False,True,True,True,True,True,False,True,False,False,False,False,True,False,False,True,False,False,True,False,False,True,False,False,True,False,False,True,True,True,False,True,True,True,True,False,True,True,False,True,True,False,True,False,False,True,False,False,True,True,True,True,False,True,True,False,True,True,True,True,True,True,False,False,True,True,False,False,False,False,True,True,False,False,False,False,True,False,True,False,True,False,True,False,True,False,False,False,False,True,True,True,True,False,True,False,True,True,False,False,False,True,True,False,True,True,True,False,True,False,False,True,False,True,True,True,True,True,True,True,False,True,False,True,True,True,True,False,True,True,False,True,False,False,True,True,True,False,True,True,False,True,False,False,False,True,True,False,False,True,True,False,False,False,False,True,True,True,True,False,True,False,True,True,False,True,True,True,True,False,False,False,False,False,False,False,True,False,False,True,True,False,False,True,False,False,False,True,True,True,False,False,True,True,False,True,False,True,True,False,True,True,False,True,False,False,False,True,False,False,True,True,False,True,False,False,True,False,False,False,False,False,True,True,True,True,True,False,False,False,False,True,True,False,True,True,False,True,True,True,True,False,False,False,True,True,False,False,True,False,False,True,False,True,True,False,False,False,False,False,False,False,False,True,False,True,True,False,False,False,True,True,False,False,True,True,True,False,True,False,False,True,False,True,True,True,True,True,True,True,False,True,True,False,False,True,True,True,True,True,True,True,False,True,True,False,False,False,False,True,False,False,True,False,True,False,True,False,True,False,True,True,True,False,True,False,True,False,True,True,True,True,False,False,False,True,False,True,True,False,False,True,False,True,False,False,True,True,False,True,False,False,False,True,False,False,True,False,False,True,True,False,False,True,False,False,False,False,True,True,False,False,False,False,True,False,False,True,False,True,False,False,True,False,True,True,False,True,True,True,False,False,True,False,True,True,False,True,True,False,False,True,False,True,True,True,True,False,False,True,True,False,True,False,True,True,True,True,False,True,False,False,True,True,False,True,False,False,False,True,False,True,False,False,False,False,False,True,False,False,True,True,True,False,True,False,True,False,True,True,True,False,True,True,True,True,False,False,False,False,True,False,True,False,True,True,False,True,True,False,True,False,True,False,False,False,False,False,False,False,True,False,False,True,True,True,False,True,True,False,True,True,True,True,True,False,False,True,True,True,True,False,True,False,True,False,False,True,False,False,True,True,False,True,False,True,True,True,False,False,True,False,True,False,True,False,False,True,True,True,True,False,False,False,False,True,False,False,False,False,True,False,False,True,True,False,True,False,True,True,True,True,True,False,True,False,True,False,False,False,True,True,True,True,True,True,False,False,False,True,False,True,True,False,False,False,True,True,True,False,True,False,True,False,False,True,True,True,True,True,False,False,False,True,False,True,False,False,True,False,True,False,True,False,False,False,True,True,True,False,False,False,False,True,True,False,False,False,False,True,True,False,False,True,True,False,False,True,False,False,False,False,False,True,False,False,True,True,False,True,True,False,True,True,True,False,False,False,False,False,True,True,False,True,False,True,True,True,False,False,True,False,False,True,False,False,True,True,False,True,False,True,True,False,True,True,False,True,True,True,True,False,False,True,False,True,False,True,False,False,True,True,True,True,False,True,False,True,False,False,True,True,True,False,True,False,True,True,True,False,False,False,True,True,True,True,False,True,False,False,False,False,True,True,True,True,False,True,False,False,True,True,True,True,False,False,True,True,False,True,False,False,True,True,True,True,False,True,False,False,True,False,False,False,True,False,True,True,True,False,False,True,True,True,False,True,False,True,True,False,False,True,False,False,False,False,True,False,True,True,False,True,False,True,True,True,True,True,True,False,True,True,True,False], dtype = "bool")#candidate|5571|(1540,)|const|bool
call_5570 = func_664_call(relay.reshape(const_5571.astype('bool'), [10, 14, 11]), relay.reshape(const_5571.astype('bool'), [10, 14, 11]), relay.reshape(const_5571.astype('bool'), [10, 14, 11]), )
call_5572 = func_664_call(relay.reshape(const_5571.astype('bool'), [10, 14, 11]), relay.reshape(const_5571.astype('bool'), [10, 14, 11]), relay.reshape(const_5571.astype('bool'), [10, 14, 11]), )
output = relay.Tuple([bop_5548,call_5566,var_5567,call_5570,const_5571,])
output2 = relay.Tuple([bop_5548,call_5568,var_5567,call_5572,const_5571,])
func_5579 = relay.Function([var_5535,var_5567,], output)
mod['func_5579'] = func_5579
mod = relay.transform.InferType()(mod)
var_5580 = relay.var("var_5580", dtype = "float64", shape = (15, 11, 2))#candidate|5580|(15, 11, 2)|var|float64
var_5581 = relay.var("var_5581", dtype = "float64", shape = (768,))#candidate|5581|(768,)|var|float64
output = func_5579(var_5580,var_5581,)
func_5582 = relay.Function([var_5580,var_5581,], output)
mutated_mod['func_5582'] = func_5582
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4982_call = mod.get_global_var('func_4982')
func_4983_call = mutated_mod.get_global_var('func_4983')
call_5597 = func_4982_call()
call_5598 = func_4982_call()
uop_5606 = relay.acosh(call_5597.astype('float32')) # shape=(520,)
uop_5608 = relay.acosh(call_5598.astype('float32')) # shape=(520,)
output = relay.Tuple([uop_5606,])
output2 = relay.Tuple([uop_5608,])
func_5615 = relay.Function([], output)
mod['func_5615'] = func_5615
mod = relay.transform.InferType()(mod)
output = func_5615()
func_5616 = relay.Function([], output)
mutated_mod['func_5616'] = func_5616
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5327_call = mod.get_global_var('func_5327')
func_5328_call = mutated_mod.get_global_var('func_5328')
call_5635 = relay.TupleGetItem(func_5327_call(), 0)
call_5636 = relay.TupleGetItem(func_5328_call(), 0)
uop_5638 = relay.acosh(call_5635.astype('float64')) # shape=(13, 14, 9)
uop_5640 = relay.acosh(call_5636.astype('float64')) # shape=(13, 14, 9)
uop_5679 = relay.rsqrt(uop_5638.astype('float64')) # shape=(13, 14, 9)
uop_5681 = relay.rsqrt(uop_5640.astype('float64')) # shape=(13, 14, 9)
func_3838_call = mod.get_global_var('func_3838')
func_3841_call = mutated_mod.get_global_var('func_3841')
var_5685 = relay.var("var_5685", dtype = "float64", shape = (1, 286))#candidate|5685|(1, 286)|var|float64
call_5684 = relay.TupleGetItem(func_3838_call(relay.reshape(var_5685.astype('float64'), [11, 2, 13])), 1)
call_5686 = relay.TupleGetItem(func_3841_call(relay.reshape(var_5685.astype('float64'), [11, 2, 13])), 1)
output = relay.Tuple([uop_5679,call_5684,var_5685,])
output2 = relay.Tuple([uop_5681,call_5686,var_5685,])
func_5688 = relay.Function([var_5685,], output)
mod['func_5688'] = func_5688
mod = relay.transform.InferType()(mod)
mutated_mod['func_5688'] = func_5688
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5689 = relay.var("var_5689", dtype = "float64", shape = (1, 286))#candidate|5689|(1, 286)|var|float64
func_5688_call = mutated_mod.get_global_var('func_5688')
call_5690 = func_5688_call(var_5689)
output = call_5690
func_5691 = relay.Function([var_5689], output)
mutated_mod['func_5691'] = func_5691
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5327_call = mod.get_global_var('func_5327')
func_5328_call = mutated_mod.get_global_var('func_5328')
call_5713 = relay.TupleGetItem(func_5327_call(), 0)
call_5714 = relay.TupleGetItem(func_5328_call(), 0)
output = call_5713
output2 = call_5714
func_5715 = relay.Function([], output)
mod['func_5715'] = func_5715
mod = relay.transform.InferType()(mod)
mutated_mod['func_5715'] = func_5715
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5715_call = mutated_mod.get_global_var('func_5715')
call_5716 = func_5715_call()
output = call_5716
func_5717 = relay.Function([], output)
mutated_mod['func_5717'] = func_5717
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5760 = relay.var("var_5760", dtype = "float32", shape = (14, 9, 11))#candidate|5760|(14, 9, 11)|var|float32
uop_5761 = relay.log10(var_5760.astype('float32')) # shape=(14, 9, 11)
func_3859_call = mod.get_global_var('func_3859')
func_3860_call = mutated_mod.get_global_var('func_3860')
call_5763 = func_3859_call()
call_5764 = func_3859_call()
func_4463_call = mod.get_global_var('func_4463')
func_4464_call = mutated_mod.get_global_var('func_4464')
call_5770 = relay.TupleGetItem(func_4463_call(), 0)
call_5771 = relay.TupleGetItem(func_4464_call(), 0)
output = relay.Tuple([uop_5761,call_5763,call_5770,])
output2 = relay.Tuple([uop_5761,call_5764,call_5771,])
func_5778 = relay.Function([var_5760,], output)
mod['func_5778'] = func_5778
mod = relay.transform.InferType()(mod)
var_5779 = relay.var("var_5779", dtype = "float32", shape = (14, 9, 11))#candidate|5779|(14, 9, 11)|var|float32
output = func_5778(var_5779)
func_5780 = relay.Function([var_5779], output)
mutated_mod['func_5780'] = func_5780
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3755_call = mod.get_global_var('func_3755')
func_3756_call = mutated_mod.get_global_var('func_3756')
call_5792 = func_3755_call()
call_5793 = func_3755_call()
func_5176_call = mod.get_global_var('func_5176')
func_5178_call = mutated_mod.get_global_var('func_5178')
call_5798 = func_5176_call()
call_5799 = func_5176_call()
func_4727_call = mod.get_global_var('func_4727')
func_4729_call = mutated_mod.get_global_var('func_4729')
call_5827 = relay.TupleGetItem(func_4727_call(), 0)
call_5828 = relay.TupleGetItem(func_4729_call(), 0)
func_1676_call = mod.get_global_var('func_1676')
func_1680_call = mutated_mod.get_global_var('func_1680')
const_5831 = relay.const([-7.804474,-6.617651,-8.198374,5.767516,4.704586,8.782023,6.411042,8.892424,0.514728,-6.544166,-1.837123,6.213056,7.008183,-9.783989,-1.983038,-8.294591,-9.047990,-5.528308,0.780412,3.895521,3.551334,-0.417783,4.834512,-9.089435,-5.430662,6.161172,3.990430,5.544055,6.864583,2.835652,-0.955070,2.497393,-8.639341,8.770910,7.568833,-5.968855,1.058825,6.500151,-6.560485,-3.525172,-3.446770,-2.082186,-0.128240,0.806606,2.053251,-2.830287,-0.746348,-1.549513,6.025342,-1.382171,4.450277,-4.525332,-3.610123,8.520141,0.014661,5.921350,9.017189,5.125912,9.827800,-0.073444,-8.796247,-1.154347,-3.613075,7.040600,5.960606,-4.102173,8.506905,1.060083,2.911373,-6.676604,-7.360668,-8.924791,5.912318,-5.920718,-8.799941,6.265016,0.648948,3.110950,3.280422,1.788871,5.785977,7.998484,-8.285910,-0.875818,4.673268,-4.897735,-3.886032,-1.236379,1.517165,-9.282488,7.687517,-6.541619,-6.194467,-5.061287,-0.124942,-8.324708,5.755321,-6.580114,-2.831699,2.286442,-8.726358,-2.455505,9.902235,-4.923019,3.187968,-9.143244,6.325560,6.150606,0.366048,5.387438,0.303938,7.161880,1.485985,7.275044,-7.951686,5.617716,-8.092049,0.606602,-4.933801,-6.678768,-5.421198,-7.552612,3.128749,8.112472,8.238642,0.884109,-0.005546,-0.658256,-3.581781,-0.885748,-6.384241,7.997702,9.529589,-7.773846,5.673109,6.802258,-7.478702,4.082828,0.704625,-2.232909,7.048061,8.705004,-2.715526,1.912207,0.281860,3.269860,5.956440,8.071191,7.075048,0.875294,-5.617890,-2.511850,-6.913349,4.181119,1.806639,8.071562,2.280647,-9.166840,-2.933485,-7.143469,5.641574,3.780207,9.223608,9.443839,1.554743,2.420762,2.628804,-4.406954,4.667143,9.867399,9.542638,9.654323,-6.424459,-1.118878,1.692751,-8.042486,-4.614878,5.388189,-8.934964,-9.579206,3.156717,-1.205140,6.624025,2.026438,-0.687813,6.358847,0.920608,-6.980480,4.329781,-9.994034,0.808300,2.059518,-7.569105,7.737868,-3.982311,-0.052546,5.184369,-4.190232,7.117325,8.636329,4.161609,7.456146,7.159987,-8.867062,-8.969112,4.820146,4.962885,3.157804,-4.021444,3.823984,-8.740056,-3.971913,-7.769271,9.449608,-9.878922,6.877475,8.175598,-8.633400,-5.213965,7.443979,9.356742,-7.638089,-4.082811,4.217682,1.783531,7.065783,-9.337476,1.588630,-2.540051,5.696724,-7.467478,-6.126419,6.673022,-5.711532,2.168110,8.626981,7.126352,-1.079087,1.899214,-1.340661], dtype = "float64")#candidate|5831|(240,)|const|float64
var_5832 = relay.var("var_5832", dtype = "uint32", shape = ())#candidate|5832|()|var|uint32
call_5830 = relay.TupleGetItem(func_1676_call(relay.reshape(const_5831.astype('float64'), [8, 5, 6]), relay.reshape(var_5832.astype('uint32'), []), ), 2)
call_5833 = relay.TupleGetItem(func_1680_call(relay.reshape(const_5831.astype('float64'), [8, 5, 6]), relay.reshape(var_5832.astype('uint32'), []), ), 2)
uop_5837 = relay.sigmoid(call_5830.astype('float64')) # shape=(8, 5, 13)
uop_5839 = relay.sigmoid(call_5833.astype('float64')) # shape=(8, 5, 13)
uop_5844 = relay.log10(uop_5837.astype('float64')) # shape=(8, 5, 13)
uop_5846 = relay.log10(uop_5839.astype('float64')) # shape=(8, 5, 13)
func_1953_call = mod.get_global_var('func_1953')
func_1957_call = mutated_mod.get_global_var('func_1957')
const_5848 = relay.const([-1,6,-9,3,-8,1,5,-1,-2,-9,7,8,4,-3,3,8,-10,4,-5,7,9,3,7,8,-10,-6,3,-8,-4,-7,4,-4,10,-4,-4,2,-10,9,9,-7,-6,-10,8,5], dtype = "uint16")#candidate|5848|(44,)|const|uint16
call_5847 = func_1953_call(relay.reshape(const_5848.astype('uint16'), [11, 4, 1]), relay.reshape(const_5848.astype('uint16'), [11, 4, 1]), )
call_5849 = func_1953_call(relay.reshape(const_5848.astype('uint16'), [11, 4, 1]), relay.reshape(const_5848.astype('uint16'), [11, 4, 1]), )
uop_5853 = relay.erf(uop_5844.astype('float64')) # shape=(8, 5, 13)
uop_5855 = relay.erf(uop_5846.astype('float64')) # shape=(8, 5, 13)
output = relay.Tuple([call_5792,call_5798,call_5827,const_5831,var_5832,call_5847,const_5848,uop_5853,])
output2 = relay.Tuple([call_5793,call_5799,call_5828,const_5831,var_5832,call_5849,const_5848,uop_5855,])
func_5856 = relay.Function([var_5832,], output)
mod['func_5856'] = func_5856
mod = relay.transform.InferType()(mod)
var_5857 = relay.var("var_5857", dtype = "uint32", shape = ())#candidate|5857|()|var|uint32
output = func_5856(var_5857)
func_5858 = relay.Function([var_5857], output)
mutated_mod['func_5858'] = func_5858
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3755_call = mod.get_global_var('func_3755')
func_3756_call = mutated_mod.get_global_var('func_3756')
call_5886 = func_3755_call()
call_5887 = func_3755_call()
output = relay.Tuple([call_5886,])
output2 = relay.Tuple([call_5887,])
func_5896 = relay.Function([], output)
mod['func_5896'] = func_5896
mod = relay.transform.InferType()(mod)
output = func_5896()
func_5897 = relay.Function([], output)
mutated_mod['func_5897'] = func_5897
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2929_call = mod.get_global_var('func_2929')
func_2931_call = mutated_mod.get_global_var('func_2931')
call_5950 = relay.TupleGetItem(func_2929_call(), 1)
call_5951 = relay.TupleGetItem(func_2931_call(), 1)
func_3296_call = mod.get_global_var('func_3296')
func_3298_call = mutated_mod.get_global_var('func_3298')
call_5959 = func_3296_call()
call_5960 = func_3296_call()
func_1907_call = mod.get_global_var('func_1907')
func_1912_call = mutated_mod.get_global_var('func_1912')
const_5962 = relay.const([1.764740,0.990136,8.225219,2.402174,7.561392,-8.198595,-5.180568,-4.738722,8.819028,-0.612391,-3.069901,5.977171,-6.133908,8.275592,7.486554,2.959262,9.522973,-6.445149,-1.781861,1.406839,5.290086,-5.391059,-6.349945,2.621998,-8.625921,-7.377816,-2.161343,-7.291179,-7.067875,8.463000,4.980114,-3.207253,0.688579,3.721633,-4.939068,-0.840641,-5.078358,8.089802,0.876544,5.662450,-4.128708,-6.239327,8.538761,7.476035,-8.133609,8.154455,-4.316580,-2.112025,5.404724,9.621365,-9.250018,9.248952,-1.753565,-7.503207,-4.262604,7.439352,2.672429,3.340198,-0.965502,-4.782326,9.861378,-2.312837,5.457932,-0.453859,-4.695845,-9.744113,6.067475,-8.191478,-4.891490,4.685444,-1.845570,0.173771,9.544482,-1.623808,-2.541905,-8.726929,-3.349003,2.147096,-8.195583,-7.634353,7.094531,8.387708,6.835935,-8.969264,-1.621346,-3.480382,-2.383693,-9.600356,-1.334051,2.025493,0.969242,4.666778,-9.863870,0.157943,-5.788327,7.922061,-7.813039,-8.556577,-8.621448,5.789131,-8.148374,0.111708,-6.052174,-6.714722,-4.775829,6.296451,-3.551805,-3.877948,2.257370,5.577442,1.931011,6.819769,4.456136,6.592247,-0.446370,5.983621,-9.355382,7.670132,-0.978645,-9.256740,0.513493,0.649078,-4.105535,-1.048858,0.668650,5.097556,-5.130232,2.175052,-3.840181,-6.204163,0.475373,8.129280,-3.598261,-1.228505,4.856805,-2.711104,-0.049617,-0.807385,0.821804,-5.042790,-3.824288,3.222976,-3.830005,-0.332159,-9.143851,6.497497,-2.978992,6.841005,2.422976,-6.566689,-1.718222,4.353483,-0.857339,4.043335,-8.408728,-1.771685,2.571870,-8.862420,-4.120099,-4.327532,8.902898,6.110329,0.172094,-7.254051,-7.105460,5.788120,8.701195,-2.527527,-1.756628,4.401657,8.676496,3.182666,-3.127681,8.072699,-9.902101,1.739677,1.538589,-6.087038,8.231174,-4.547903,0.420853,4.785956,-7.382185,-8.525159,6.533900,-1.468713,9.333742,-1.415993,8.206529,2.290242,2.589761,1.214354,2.512575,7.127588,-1.175760,-9.809069,3.243560,2.897327,4.852823,-7.935211,8.311169,-8.676522,-1.044945,-9.294769,-5.074298,-9.464139,-0.982634,-4.699988,5.138498,0.431460,9.728202,5.226360,8.657755,4.639468,-9.024751,0.287315,-3.872647,-8.899627,-4.521508,-5.710108,-7.668999,4.462551,-0.875940,-4.217076,9.555140,6.528430,-5.117861,-9.707700,8.193113,-9.339034,1.323233,-8.281026,4.599481,3.416782,3.986252,-9.914874,-1.803330,2.877188,-6.020589,-7.221475,4.391498,-1.898585,-3.631614,2.918992,-1.691032,4.644998,8.326044,4.755709,-9.183072,2.182552,-8.716296,-3.494520,3.175387,2.995271,9.582415,0.822361,-7.085535,-4.493540,-3.377415,-3.026312,-1.479635,8.010888,7.249183,-7.521494,0.711246,-9.818598,-6.015202,-8.146435,-2.348376,7.014486,4.669822,-0.375691,-3.460835,-1.636319,-5.498880,-8.435548,-6.146893,-7.567432,-4.513432,1.881380,-8.219707,-7.604836,-2.030285,-0.615499,-4.873880,8.354195,4.638544,4.835337,-5.621015,-1.786777,0.400478,4.581849,-6.878634,9.472512,8.243670,-7.514440,-1.732470,-8.162072,4.117341,6.315717,-4.033716,5.352321,-3.354974,9.077025,-9.791888,5.543982,-3.118165,5.113936,3.359285,-4.158940,-9.360086,-3.196131,3.544531,7.944403,-2.906074,-0.769520,2.102796,-8.200734,6.222359,9.229508,2.498097,9.964102,7.644641,7.032531,3.018630,9.257850,-5.012662,1.791654,-9.926619,4.342046,3.331962,6.405518,5.964846,0.933786,-8.923336,2.067287,3.860102,3.922855,7.864109,2.437373,-8.260683,-9.842826,1.798520,-9.499642,2.604084,-0.558485,-6.113992,0.104785,0.112905,-9.596879,3.985294,1.168100,-3.656957,-6.142576,4.045511,-0.241134,-5.335482,1.414423,-5.190395,-8.762415,6.535881,0.477346,-0.743228,2.426808,7.897707,5.323891,3.549831,3.786964,-8.974344,-4.141342,-3.244341,3.309959,0.099839,-5.098843,2.146433,8.143173,0.867568,-0.281364,-5.383170,3.637930,7.920600,-2.219926,7.375440,-8.806016,9.887967,-4.028578,9.973075,5.355179,-9.187628,5.228765,-5.801715,-4.895245,7.207453,0.072787,-2.406375,0.191589,-6.078727,5.654272,3.965098,0.908468,-4.244202,-1.153507,5.299886,-9.020728,6.686120,6.000466,1.596676,5.507913,-7.206482,-4.111595,4.966125,-1.133830,6.809341,-1.857149,1.447996,-0.351943,8.473089,-4.334506,-9.323109,-3.786058,-6.570291,8.192448,9.707824,-3.902787,3.268057,-8.628441,-6.007076,-4.425700,-9.816242,-0.981622,-1.133366,7.791346,-8.916605,4.706897,5.759939,-6.209999,0.669724,0.960416,8.979581,3.949374,-7.696055,8.559628,-5.873280,-7.793450,-8.358998,7.244418,1.291663,-8.333524,-7.678312,-7.199067,6.002410,4.115785,-3.554081,8.462197,-2.697808,1.341105,8.704258,6.667058,-0.093371,-5.981063,-2.243395,-5.863151,9.406496,5.394244,-2.499904,3.745446,5.532244,-0.880347,4.231767,1.696363,-4.998781,-4.878020,3.757526,-9.347853,2.727057,4.259321,-2.408775,-8.935894,-8.105525,3.862747,0.309701,6.820594,1.065480,8.943212,8.154812,-5.663332,8.081931,2.251892,-0.898112,-5.531431], dtype = "float32")#candidate|5962|(490,)|const|float32
call_5961 = relay.TupleGetItem(func_1907_call(relay.reshape(const_5962.astype('float32'), [14, 7, 5]), relay.reshape(const_5962.astype('float32'), [14, 7, 5]), relay.reshape(call_5950.astype('uint8'), [10, 52]), ), 1)
call_5963 = relay.TupleGetItem(func_1912_call(relay.reshape(const_5962.astype('float32'), [14, 7, 5]), relay.reshape(const_5962.astype('float32'), [14, 7, 5]), relay.reshape(call_5950.astype('uint8'), [10, 52]), ), 1)
func_3316_call = mod.get_global_var('func_3316')
func_3317_call = mutated_mod.get_global_var('func_3317')
call_5968 = relay.TupleGetItem(func_3316_call(), 0)
call_5969 = relay.TupleGetItem(func_3317_call(), 0)
func_3859_call = mod.get_global_var('func_3859')
func_3860_call = mutated_mod.get_global_var('func_3860')
call_5980 = func_3859_call()
call_5981 = func_3859_call()
func_3107_call = mod.get_global_var('func_3107')
func_3108_call = mutated_mod.get_global_var('func_3108')
call_5982 = relay.TupleGetItem(func_3107_call(), 0)
call_5983 = relay.TupleGetItem(func_3108_call(), 0)
func_3646_call = mod.get_global_var('func_3646')
func_3649_call = mutated_mod.get_global_var('func_3649')
var_5987 = relay.var("var_5987", dtype = "float32", shape = (432, 1))#candidate|5987|(432, 1)|var|float32
call_5986 = relay.TupleGetItem(func_3646_call(relay.reshape(var_5987.astype('float32'), [6, 12, 6]), relay.reshape(var_5987.astype('float32'), [6, 12, 6]), ), 1)
call_5988 = relay.TupleGetItem(func_3649_call(relay.reshape(var_5987.astype('float32'), [6, 12, 6]), relay.reshape(var_5987.astype('float32'), [6, 12, 6]), ), 1)
bop_5993 = relay.less_equal(const_5962.astype('bool'), var_5987.astype('bool')) # shape=(432, 490)
output = relay.Tuple([call_5950,call_5959,call_5961,call_5968,call_5980,call_5982,call_5986,bop_5993,])
output2 = relay.Tuple([call_5951,call_5960,call_5963,call_5969,call_5981,call_5983,call_5988,bop_5993,])
func_6001 = relay.Function([var_5987,], output)
mod['func_6001'] = func_6001
mod = relay.transform.InferType()(mod)
var_6002 = relay.var("var_6002", dtype = "float32", shape = (432, 1))#candidate|6002|(432, 1)|var|float32
output = func_6001(var_6002)
func_6003 = relay.Function([var_6002], output)
mutated_mod['func_6003'] = func_6003
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5327_call = mod.get_global_var('func_5327')
func_5328_call = mutated_mod.get_global_var('func_5328')
call_6019 = relay.TupleGetItem(func_5327_call(), 0)
call_6020 = relay.TupleGetItem(func_5328_call(), 0)
output = call_6019
output2 = call_6020
func_6023 = relay.Function([], output)
mod['func_6023'] = func_6023
mod = relay.transform.InferType()(mod)
mutated_mod['func_6023'] = func_6023
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6023_call = mutated_mod.get_global_var('func_6023')
call_6024 = func_6023_call()
output = call_6024
func_6025 = relay.Function([], output)
mutated_mod['func_6025'] = func_6025
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2885_call = mod.get_global_var('func_2885')
func_2887_call = mutated_mod.get_global_var('func_2887')
call_6032 = relay.TupleGetItem(func_2885_call(), 1)
call_6033 = relay.TupleGetItem(func_2887_call(), 1)
func_3890_call = mod.get_global_var('func_3890')
func_3891_call = mutated_mod.get_global_var('func_3891')
call_6034 = relay.TupleGetItem(func_3890_call(), 0)
call_6035 = relay.TupleGetItem(func_3891_call(), 0)
func_4948_call = mod.get_global_var('func_4948')
func_4949_call = mutated_mod.get_global_var('func_4949')
call_6038 = relay.TupleGetItem(func_4948_call(), 1)
call_6039 = relay.TupleGetItem(func_4949_call(), 1)
uop_6040 = relay.log10(call_6034.astype('float32')) # shape=(520,)
uop_6042 = relay.log10(call_6035.astype('float32')) # shape=(520,)
output = relay.Tuple([call_6032,call_6038,uop_6040,])
output2 = relay.Tuple([call_6033,call_6039,uop_6042,])
func_6051 = relay.Function([], output)
mod['func_6051'] = func_6051
mod = relay.transform.InferType()(mod)
output = func_6051()
func_6052 = relay.Function([], output)
mutated_mod['func_6052'] = func_6052
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3316_call = mod.get_global_var('func_3316')
func_3317_call = mutated_mod.get_global_var('func_3317')
call_6064 = relay.TupleGetItem(func_3316_call(), 0)
call_6065 = relay.TupleGetItem(func_3317_call(), 0)
func_5489_call = mod.get_global_var('func_5489')
func_5493_call = mutated_mod.get_global_var('func_5493')
const_6070 = relay.const([-6,-1,-7,7,9,-5,-5,-9,6,10,4,-8,1,-4,10,8,-8,-4,-5,5,5,2,-2,-2,2,-10,-4,-9,-8,3,-8,-3,-9,-9,10,-8,-5,6,1,6,1,-2,-6,-9,3,2,4,6,-2,10,3,8,8,7,-3,-5,-9,-9,-5,1,2,-9,-9,-10,4,-5,-7,4,9,7,4,-8,8,-8,-6,2,2,-4,8,2,-5,-8,-1,10,-6,4,8,3,-9,-10], dtype = "int64")#candidate|6070|(90,)|const|int64
const_6071 = relay.const([False,False,False,True,True,False,False,False,False,False,True,False,True,False,True,False,False,False,True,True,False,False,False,False,False,False,True,True,False,False,False,False,False,False,True,True,False,True,False,True,False,True,True,True,True,False,False,False,False,True,True,False,False,True,True,False,False,False,False,False,False,False,False,False,False,True,False,True,True,False,False,True,True,True,False,True,True,False,True,True,False,False,True,False,False,False,False,False,True,False,False,True,False,False,False,True,True,False,False,False,False,False,True,True,True,False,False,False,False,True,True,False,False,False,False,False,True,True,False,False,True,False,True,False,False,True,True,True,True,True,False,True,True,True,True,False,True,True,False,False,True,True,False,True,True,True,True,False,False,True,False,True,True,False,True,True,True,False,False,True,True,False,False,False,False,True,False,True,True,False,True,False,True,False,True,True,True,False,True,True,True,False,False,False,False,False,True,True,False,True,False,False,False,True,False,False,False,True,True,True,True,True,True,True,True,False,False,False,False,True,True,True,True,True,True,True,True,False,True,False,False,True,False,False,False,False,False,True,True,True,False,True,False,False,False,True,False,False,True,True,True,False,False,True,False,False,False,True,False,True,True,False,True,True,False,True,False,False,False,True,False,True,False,False,True,False,False,True,False,True,False,False,False,True,True,False,True,True,True,True,True,True,False,False,False,False,True,False,True,False,False,True,True,False,True,False,True,True,True,True,True,False,True,True,True,False,True,False,False,False,True,True,True,True,True,False,False,False,False,True,False,False,False,True,True,True,True,False,True,True,True,False,True,True,True,False,True,False,False,True,False,True,False,False,True,True,False,True,False,False,False,False,True,False,False,False,True,True,False,False,False,True,False], dtype = "bool")#candidate|6071|(363,)|const|bool
call_6069 = relay.TupleGetItem(func_5489_call(relay.reshape(const_6070.astype('int64'), [5, 9, 2]), relay.reshape(const_6071.astype('bool'), [11, 33]), relay.reshape(const_6070.astype('float32'), [5, 9, 2]), ), 8)
call_6072 = relay.TupleGetItem(func_5493_call(relay.reshape(const_6070.astype('int64'), [5, 9, 2]), relay.reshape(const_6071.astype('bool'), [11, 33]), relay.reshape(const_6070.astype('float32'), [5, 9, 2]), ), 8)
func_5896_call = mod.get_global_var('func_5896')
func_5897_call = mutated_mod.get_global_var('func_5897')
call_6075 = relay.TupleGetItem(func_5896_call(), 0)
call_6076 = relay.TupleGetItem(func_5897_call(), 0)
var_6084 = relay.var("var_6084", dtype = "int8", shape = (13, 14, 9))#candidate|6084|(13, 14, 9)|var|int8
bop_6085 = relay.greater_equal(call_6064.astype('bool'), relay.reshape(var_6084.astype('bool'), relay.shape_of(call_6064))) # shape=(13, 14, 9)
bop_6088 = relay.greater_equal(call_6065.astype('bool'), relay.reshape(var_6084.astype('bool'), relay.shape_of(call_6065))) # shape=(13, 14, 9)
func_5373_call = mod.get_global_var('func_5373')
func_5374_call = mutated_mod.get_global_var('func_5374')
call_6092 = func_5373_call()
call_6093 = func_5373_call()
func_5778_call = mod.get_global_var('func_5778')
func_5780_call = mutated_mod.get_global_var('func_5780')
const_6102 = relay.const([1.474385,8.609890,1.051673,-9.009458,4.955689,-8.111205,-7.670497,9.147040,-2.453406,7.645444,0.391704,-2.570766,-9.670984,-3.986712,-8.711487,-3.298562,-4.726810,-6.471820,-0.679533,3.583377,-8.738173,-9.679210,-1.237939,1.883537,-7.703256,8.629184,8.620542,-9.884804,-8.264470,0.440992,1.515486,-9.576585,5.153032,8.249978,8.844232,-0.516124,2.986065,9.610664,-9.966221,-3.382903,2.377337,-6.631950,-5.960215,-7.758288,5.978128,8.545225,-7.964062,3.592400,8.044144,5.621298,4.803940,-6.274400,-8.455158,2.977543,-8.019990,6.773874,9.294779,-0.060050,-9.999344,-7.201513,-6.893393,6.112065,0.437158,-7.341530,9.492903,3.165615,7.920094,3.262850,8.096886,-3.007061,9.444204,5.943195,3.624764,-3.916522,9.274866,-6.558002,-0.392722,-1.730520,-8.431521,-1.901126,-4.005155,-5.946194,4.886809,-5.657820,-8.593179,-5.457460,-6.508208,-3.928018,5.070831,-5.745126,0.131328,-2.216750,-9.571852,1.708415,-6.214281,-1.270410,-4.048630,-9.497855,8.345082,-8.219945,-2.612713,7.892071,7.716399,-6.858845,-7.158313,4.640154,3.420276,3.280866,-1.064454,-9.776517,4.454374,9.018918,-4.152584,7.776933,-9.367261,2.867475,1.894206,-5.186275,7.604258,0.129148,8.216283,9.756320,7.435234,-7.915066,-9.463382,-9.441023,4.920893,1.571584,0.663449,3.208777,-2.613901,-6.874447,8.373434,-5.978354,-1.432865,-7.806140,-7.014568,-2.022029,8.437902,0.368724,-8.663893,9.563092,-1.694775,7.884126,7.868892,0.262136,1.797630,9.929455,-7.986604,1.652066,-7.987594,-5.899610,-7.511788,-9.000077,8.133773,0.813873,2.131032,-2.602890,9.351956,1.983617,-9.073908,-6.673855,8.883589,0.262869,-9.515620,-7.297681,-0.941585,3.214255,5.883256,-0.007743,-6.275864,-4.332742,-8.860209,8.805655,-3.486274,1.449050,8.072542,9.305394,2.122166,1.252113,6.398642,-9.501923,-2.060719,-8.038899,5.937779,7.524337,-9.027664,8.048968,-7.024105,-7.579801,-7.720693,4.659421,-8.447208,-4.989834,2.525042,5.004185,3.752707,1.607929,6.011463,2.202715,-1.957312,-8.330428,0.955649,-3.034791,-1.731319,-5.836120,-0.096828,8.605814,-2.236351,-8.479794,4.860099,8.006786,-3.093536,-2.378973,-6.150995,-4.341750,-1.704145,-6.994164,0.166033,9.442627,9.613872,-7.944913,-7.860101,-4.695492,1.036823,-5.117271,-1.134015,8.983903,-5.950880,5.780748,5.360768,-3.005721,-4.646809,9.480253,1.154157,-4.903163,7.511388,-6.960470,-4.193258,-0.816063,2.760910,-1.284356,-8.848480,-8.930747,5.580025,-6.649123,-3.828218,8.841317,3.016338,-4.306644,9.120934,9.408717,6.308837,-4.064188,3.794680,6.657694,-8.144531,-3.384080,1.542615,5.911198,-4.418567,8.013575,-6.344845,-4.242984,-7.200443,-1.250570,5.107215,-0.200433,7.746986,-4.707103,9.010158,-4.586141,4.667691,6.656829,6.230560,3.164237,-3.228149,-0.022673,8.336986,-5.896157,4.121353,-0.477775,-7.117936,4.843556,8.043309,-1.848939,4.620251,-7.743475,-0.118583,0.113179,5.164070,3.384203,-5.744205,-2.083523,-8.303871,5.757786,-0.045059,-1.912340,-5.186490,-8.396769,9.047900,-3.250081,4.588193,2.384367,-3.653244,-1.632837,-3.470919,8.083336,8.727860,-7.617535,-5.439234,-2.112788,5.104953,-3.952163,-0.743879,-2.659852,7.504757,0.583017,8.347015,-7.660413,4.928933,1.277676,6.195027,-5.154345,8.254616,-4.729319,-2.650225,-8.145620,-1.730131,5.658552,3.494607,-4.051700,6.851310,-0.696060,7.698046,-8.631617,4.157240,-9.956583,9.025217,3.562186,4.092100,-0.161068,-6.091638,-4.347128,4.902060,-3.187910,8.321727,-7.342405,-3.753485,8.440606,7.780481,-3.001297,-8.744253,4.512286,-9.039264,-8.064466,9.102401,2.460607,7.814911,-0.829613,-2.896852,5.515217,2.861204,-1.655442,-8.299274,5.377929,5.863067,-0.317250,-2.986241,7.197185,7.303980,9.720963,0.402715,-0.271867,-0.231050,1.785001,1.197898,-0.021296,-9.888462,-1.219433,-3.926024,2.869661,-8.174949,0.330979,6.271118,9.133989,-0.193944,2.752256,8.954388,-8.481824,-9.070746,-9.117195,8.897107,4.215188,2.642899,-5.292520,7.071307,-7.716074,-2.986702,0.021775,-0.248442,-2.813680,6.328128,-8.998847,2.610465,-5.119350,9.249883,-0.031962,0.917060,-8.957464,0.353989,-9.084980,-9.598832,-8.844287,6.420481,2.586027,-7.767546,-2.144690,5.906219,2.154304,-0.356247,7.333139,-8.377460,-1.347271,5.951229,2.782031,0.206325,1.795521,-6.348152,-8.389862,0.782264,2.948549,7.255492,8.281605,6.199594,-3.157330,-1.828692,5.755992,7.787383,-8.002980,-5.127290,1.714952,-6.155130,-4.174603,2.862961,-0.557909,-2.267105,-6.488290,2.539504,-7.834700,-1.458282,-3.569652,-8.031404,-5.132858,8.694305,-0.183119,-4.886787,-2.578242,4.087874,9.449587,2.242683,6.822997,9.857874,-2.222717,-5.124201,8.262700,6.460371,2.112803,0.645014,3.873616,5.074141,5.085354,6.533846,-2.671481,-9.080962,4.144485,9.197251,7.453152,5.505924,0.899303,-8.680849,-3.316757,4.626521,-3.600199,2.119453,4.177197,8.885092,-3.017697,-1.724737,5.271986,-3.223921,7.422163,-9.063772,8.613370,-5.219158,9.916349,8.083589,-6.490011,1.121589,-7.310714,-2.908835,3.291683,-8.733003,-2.904510,-9.322791,5.131666,8.261859,-4.482306,2.828202,3.932418,1.355487,-4.782254,-5.133597,7.973145,0.860048,1.201000,9.749858,-6.858154,-4.454881,0.817559,-0.503175,-7.285703,0.124910,2.455492,-5.676327,-7.680233,9.314860,-4.841559,8.474759,-8.746543,4.018645,-6.254368,-8.179500,-0.594788,9.466093,-3.341230,-4.306856,7.122434,3.779274,-4.512292,0.671845,9.941042,-5.626476,5.024673,2.873507,-9.442910,7.691413,-7.648478,9.561179,-8.771662,-0.538023,3.345225,6.301961,-5.342136,0.743873,-0.776110,7.364163,-9.088515,-3.113586,3.670906,5.211786,-3.070094,-3.312625,-2.040383,-4.936701,-0.815248,3.232231,0.744058,4.144336,-4.060139,5.300132,9.566901,-0.010796,-4.915164,5.437081,8.193122,7.945329,9.239582,-1.797345,-2.491339,1.788703,2.980061,-4.395845,0.061898,-3.694557,-9.322961,7.934053,-8.481609,7.601640,-7.451479,-7.364902,1.352803,5.605794,0.142476,2.838192,-3.678655,-4.738372,5.997870,8.961232,-7.607620,-5.186659,8.662414,9.216471,-9.818384,-3.430728,6.442186,-6.402030,-6.323306,-8.917475,7.466840,1.702912,-8.832028,7.000726,-8.939818,-7.667396,-4.811471,-2.201315,-3.976957,9.240088,-6.122880,8.950708,-7.129164,3.942456,-4.092800,-2.942757,1.027683,2.026902,4.454975,2.877296,2.380331,9.629486,4.695310,2.511322,4.121257,-1.448086,-2.026094,1.750160,0.456762,-6.321073,-6.053888,9.957508,-0.668242,0.229925,6.795057,-3.068748,9.438477,-4.994564,8.720558,-0.554165,-0.090167,-3.007285,7.754892,8.499299,-5.776041,-5.732763,-7.579799,-6.558328,-9.359310,-9.097031,6.479063,7.741632,-5.297805,9.772873,9.247012,-7.330996,-9.764467,9.432140,3.189471,-0.271866,-0.428512,-8.483885,-4.185401,4.352945,2.201660,-4.004482,-6.980732,5.106758,5.130523,-2.000690,-9.240175,-5.066091,-1.894491,-7.274912,-8.945382,1.401411,2.167299,9.634924,3.473383,1.905260,-2.338429,2.027181,7.792466,-4.472622,3.819356,7.610060,8.061787,-5.706175,9.144386,6.628518,2.390510,-7.598283,8.284267,-0.508593,3.555160,5.315723,5.704890,-4.766898,3.242357,0.600784,-4.771789,-6.501690,-7.913364,4.885803,-3.273692,6.031484,0.413049,-4.581450,3.298960,6.978278,-7.135921,-2.666805,9.494107,-1.108644,9.334896,3.189928,0.514404,-6.529842,-8.657388,8.476053,-3.398506,-5.478020,1.760970,-4.140052,9.705511,8.617584,-6.875410,0.882755,-0.367257,-4.390537,1.253331,2.836525,-6.195253,-4.041332,7.522170,1.972843,-1.957837,-1.774558,-7.244835,-2.925564,-0.423407,-2.010919,-6.225644,9.230725,9.806759,-6.159471,4.287950,4.703033,7.324319,7.567658,-4.596626,2.353444,-8.735242,-2.888149,-6.980983,2.651997,-8.702727,-0.321231,7.167182,2.233465,7.492781,-1.121106,-3.643260,-0.728366,0.081244,-3.427993,-7.066517,1.804799,3.765472,-6.655863,-1.449906,8.634313,5.473867,0.859291,7.024669,4.615231,9.714723,0.841946,-1.031321,9.891900,2.777521,0.038753,1.878800,7.199853,-6.789325,1.967035,7.205502,4.056370,-8.946628,0.815306,0.539750,-8.146155,-5.515703,-3.772307,-8.677223,9.314963,-8.210782,7.794963,1.933330,-9.433313,-3.836330,-5.189400,-4.171802,-7.787056,1.770509,-0.287616,4.879862,9.265485,3.962050,-4.394775,4.084731,2.605382,-2.970664,-0.056500,3.846023,2.076036,-2.268085,1.117977,3.659711,5.779534,-4.483596,6.530399,-1.239397,4.491126,3.307619,8.410013,2.290067,-8.515648,-7.507043,1.813045,6.697097,1.799251,0.747974,4.959862,8.877504,0.006499,-0.117331,5.725583,4.838618,-8.847903,-2.868032,4.636625,2.703007,7.325942,-1.932382,0.247626,3.857995,3.484526,-6.195569,1.864335,2.632074,2.527010,8.078322,5.035593,7.507217,4.249871,2.642768,-7.782132,-3.772945,-2.016734,-4.498585,6.872456,9.343625,-6.860883,4.813336,9.745256,-4.466675,-8.644500,8.610483,-3.742428,-3.731121,-5.420675,3.149928,-5.087264,-3.356215,-4.973110,-7.144741,-0.735803,1.353904,8.230028,-6.507736,1.218441,6.896768,-5.522292,1.264692,-9.213121,8.178217,-5.797612,8.594312,-4.460204,4.697378,-1.920124,-8.723099,9.477729,-1.158589,-9.405805,9.686725,2.816610,-4.530199,2.299208,4.308592,3.111590,-7.521896,7.308569,-7.144021,5.686851,-2.294568,9.286171,-0.735556,-0.894655,-2.467997,0.804340,5.883527,-2.662294,1.597089,3.221762,4.463274,1.286862,-9.866590,1.408906,-7.848451,9.805968,8.466157,-7.740163,6.881540,-5.183845,3.412654,-5.959372,-8.274647,-0.966403,-0.139667,-8.816965,-7.927153,-1.963026,-1.854461,0.682419,-1.168602,-6.942888,-0.186288,-1.679730,2.267271,2.171242,-7.513643,6.245584,-7.708822,-3.134049,-2.882164,2.248906,-1.649032,3.558097,8.041775,-1.554846,2.041066,7.026165,8.809294,-6.394673,-5.463597,7.203189,9.548194,-0.958512,2.931054,-3.084589,6.397591,-6.097829,3.053511,5.224081,2.323919,4.497733,-0.644516,-8.892714,-2.798732,-1.631241,-7.777009,4.961838,0.275598,2.125815,9.145437,-6.997141,0.091256,-6.287778,-3.975865,-1.068936,7.945074,6.437834,-0.145798,6.665368,-8.556869,-3.659981,-2.800108,-7.373367,9.617081,-0.260650,3.481735,5.492269,2.549793,-1.708689,9.115248,6.725419,-7.336394,-8.270844,-9.677568,7.227676,-8.037790,6.026586,1.679974,-5.918859,-7.946292,3.451733,3.347203,-4.440431,4.169738,-5.553940,6.149968,9.376535,-9.194209,2.923133,-3.077075,6.671518,-1.245899,7.350799,-7.429991,-1.913417,-1.676809,5.161242,-1.082768,-3.868879,-3.557913,7.446367,0.403620,3.816613,-1.586393,-6.645057,1.137229,3.852789,6.681283,8.665075,-7.758825,-9.116658,-1.601875,-6.848535,3.535222,-3.858687,-7.036317,-1.290871,-7.529746,1.805088,-4.173421,1.113493,-1.170210,2.840107,0.709204,3.994069,-5.204926,-7.299946,0.590454,6.140779,-9.968539,-4.514106,1.917996,-0.889087,-1.919263,4.884827,1.429908,-7.990453,4.182662,5.695368,5.879857,0.867660,-1.652302,-6.601736,-9.690595,2.418614,6.588649,0.493732,-7.445789,-3.386117,-0.238208,4.601432,5.108648,7.253990,9.918905,0.882320,6.138155,-7.489171,6.152554,-4.387739,-9.529838,-5.648235,6.448068,6.223617,1.419033,9.117819,8.118833,4.932939,-2.887099,8.579604,-0.160759,-5.867678,8.238643,5.784403,4.548706,4.528055,8.097886,1.797913,6.903678,-2.089693,2.712038,-9.279832,-5.258978,4.202316,-8.794369,-9.178647,1.332333,1.811745,9.197872,7.441783,-0.245487,0.275136,-7.768291,-4.310159,9.272438,-6.574312,-9.074779,5.940898,2.702165,-6.143030,4.808808,-6.538642,3.022976,-7.726855,-9.957387,-5.213905,-8.920667,7.240424,-3.966636,-1.070383,-2.724183,-4.107509,-7.745645,-0.439075,-7.375597,1.730445,9.985332,5.779182,6.563568,-9.520723,6.087462,-7.912372,-4.308573,1.295384,-3.139083,-2.133189,-1.989606,0.019438,-5.279932,-5.269412,-2.014712,-4.124450,6.981920,3.840956,2.280374,9.033053,-4.595880,-4.173797,4.704487,7.148392,-7.384787,-5.227153,3.600010,8.620563,7.546693,-7.628978,6.021205,-3.469561,-9.028639,-0.435325,3.422737,9.435673,3.776095,-3.235355,2.230757,-9.265077,2.498901,-3.855225,1.800324,-9.964019,-9.159259,-5.193252,0.380974,-1.690164,-4.572108,-6.095472,-2.415976,7.007222,7.987681,-7.482196,-7.672865,-6.462848,-2.405024,-8.309231,-3.448411,-8.436924,0.465039,9.837184,0.305708,2.341458,-1.605234,5.942070,9.698963,-0.080160,-1.013579,2.766392,-0.937391,-2.135256,-1.488394,-2.999675,3.882771,5.859839,9.539075,-4.342725,3.393257,9.613858,5.855868,-2.429685,4.228251,6.639342,-8.560411,-2.546977,4.197015,1.273025,0.242185,-2.404323,-4.828139,-9.181329,-5.999840,7.170113,-8.342580,3.137469,1.891667,-3.358660,1.715057,0.712278,-0.980100,-9.250955,-8.641191,4.038464,5.940447,8.744742,-4.939008,4.018469,-8.832569,-3.936903,2.427756,-3.215112,6.107555,-2.190478,-5.108004,-7.293999,7.278896,-1.406352,-1.761301,-7.145430,-1.880238,-8.864363,3.300229,5.394141,-7.492720,-1.634230,-3.356158,-4.803620,4.210921,-7.276133,-0.015396,-7.026286,5.938444,-5.755964,-2.444356,4.267197,-7.538808,0.422456,7.930853,1.033755,-6.605596,-8.827902,-6.740695,4.718301,7.441396,9.239075,-9.502541,1.815437,6.011987,-3.828395,-4.851821,-4.457005,7.443369,-8.032527,-5.164759,-8.754391,3.803006,2.979013,9.964216,9.638551,-5.488539,3.182540,-2.634939,-5.705081,-7.574137,-7.531253,-1.496139,9.402186,-9.539621,3.192183,5.859791,-3.543131,-2.237929,-5.069870,-4.636839,-6.755051,-5.190594,5.400858,-2.466750,-3.244208,-0.021261,-3.335621,8.582629,-7.773167,7.032788,6.486281,3.838140,-4.387549,2.789477,-3.874160,-5.138362,9.911688,-4.630769,-4.626012,-1.546601,3.538491,9.548083,-4.997129,3.167957,-5.728969,-4.185275,0.478456,9.094592,9.317988,-5.888954,-4.509860,-1.729801,2.959721,5.232588,5.459294,1.644234,-1.953096,-5.730540,7.744760,-7.920740,1.501845,2.647717,-5.494373,-2.592028,-9.846012,6.687394,1.785099,-0.846100,-4.300270,-8.537141,7.628526,-8.382138,-1.243914,-1.087907,-6.725335,-1.654778,0.783558,-3.682189,-9.080265,9.996626], dtype = "float32")#candidate|6102|(1386,)|const|float32
call_6101 = relay.TupleGetItem(func_5778_call(relay.reshape(const_6102.astype('float32'), [14, 9, 11])), 2)
call_6103 = relay.TupleGetItem(func_5780_call(relay.reshape(const_6102.astype('float32'), [14, 9, 11])), 2)
output = relay.Tuple([call_6069,const_6070,const_6071,call_6075,bop_6085,call_6092,call_6101,const_6102,])
output2 = relay.Tuple([call_6072,const_6070,const_6071,call_6076,bop_6088,call_6093,call_6103,const_6102,])
func_6108 = relay.Function([var_6084,], output)
mod['func_6108'] = func_6108
mod = relay.transform.InferType()(mod)
var_6109 = relay.var("var_6109", dtype = "int8", shape = (13, 14, 9))#candidate|6109|(13, 14, 9)|var|int8
output = func_6108(var_6109)
func_6110 = relay.Function([var_6109], output)
mutated_mod['func_6110'] = func_6110
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3081_call = mod.get_global_var('func_3081')
func_3083_call = mutated_mod.get_global_var('func_3083')
call_6117 = relay.TupleGetItem(func_3081_call(), 0)
call_6118 = relay.TupleGetItem(func_3083_call(), 0)
output = relay.Tuple([call_6117,])
output2 = relay.Tuple([call_6118,])
func_6119 = relay.Function([], output)
mod['func_6119'] = func_6119
mod = relay.transform.InferType()(mod)
mutated_mod['func_6119'] = func_6119
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6119_call = mutated_mod.get_global_var('func_6119')
call_6120 = func_6119_call()
output = call_6120
func_6121 = relay.Function([], output)
mutated_mod['func_6121'] = func_6121
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4786_call = mod.get_global_var('func_4786')
func_4788_call = mutated_mod.get_global_var('func_4788')
call_6157 = func_4786_call()
call_6158 = func_4786_call()
var_6185 = relay.var("var_6185", dtype = "int8", shape = (13, 14, 9))#candidate|6185|(13, 14, 9)|var|int8
bop_6186 = relay.right_shift(call_6157.astype('int32'), relay.reshape(var_6185.astype('int32'), relay.shape_of(call_6157))) # shape=(13, 14, 9)
bop_6189 = relay.right_shift(call_6158.astype('int32'), relay.reshape(var_6185.astype('int32'), relay.shape_of(call_6158))) # shape=(13, 14, 9)
func_2955_call = mod.get_global_var('func_2955')
func_2958_call = mutated_mod.get_global_var('func_2958')
var_6199 = relay.var("var_6199", dtype = "float64", shape = (4,))#candidate|6199|(4,)|var|float64
var_6200 = relay.var("var_6200", dtype = "uint32", shape = (2016,))#candidate|6200|(2016,)|var|uint32
call_6198 = relay.TupleGetItem(func_2955_call(relay.reshape(var_6199.astype('float64'), [4,]), relay.reshape(var_6200.astype('uint32'), [2016,]), ), 2)
call_6201 = relay.TupleGetItem(func_2958_call(relay.reshape(var_6199.astype('float64'), [4,]), relay.reshape(var_6200.astype('uint32'), [2016,]), ), 2)
func_2955_call = mod.get_global_var('func_2955')
func_2958_call = mutated_mod.get_global_var('func_2958')
call_6203 = relay.TupleGetItem(func_2955_call(relay.reshape(var_6199.astype('float64'), [4,]), relay.reshape(var_6200.astype('uint32'), [2016,]), ), 3)
call_6204 = relay.TupleGetItem(func_2958_call(relay.reshape(var_6199.astype('float64'), [4,]), relay.reshape(var_6200.astype('uint32'), [2016,]), ), 3)
func_5327_call = mod.get_global_var('func_5327')
func_5328_call = mutated_mod.get_global_var('func_5328')
call_6205 = relay.TupleGetItem(func_5327_call(), 0)
call_6206 = relay.TupleGetItem(func_5328_call(), 0)
output = relay.Tuple([bop_6186,call_6198,var_6199,var_6200,call_6203,call_6205,])
output2 = relay.Tuple([bop_6189,call_6201,var_6199,var_6200,call_6204,call_6206,])
func_6209 = relay.Function([var_6185,var_6199,var_6200,], output)
mod['func_6209'] = func_6209
mod = relay.transform.InferType()(mod)
var_6210 = relay.var("var_6210", dtype = "int8", shape = (13, 14, 9))#candidate|6210|(13, 14, 9)|var|int8
var_6211 = relay.var("var_6211", dtype = "float64", shape = (4,))#candidate|6211|(4,)|var|float64
var_6212 = relay.var("var_6212", dtype = "uint32", shape = (2016,))#candidate|6212|(2016,)|var|uint32
output = func_6209(var_6210,var_6211,var_6212,)
func_6213 = relay.Function([var_6210,var_6211,var_6212,], output)
mutated_mod['func_6213'] = func_6213
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6051_call = mod.get_global_var('func_6051')
func_6052_call = mutated_mod.get_global_var('func_6052')
call_6225 = relay.TupleGetItem(func_6051_call(), 0)
call_6226 = relay.TupleGetItem(func_6052_call(), 0)
output = call_6225
output2 = call_6226
func_6260 = relay.Function([], output)
mod['func_6260'] = func_6260
mod = relay.transform.InferType()(mod)
output = func_6260()
func_6261 = relay.Function([], output)
mutated_mod['func_6261'] = func_6261
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6268 = relay.var("var_6268", dtype = "bool", shape = (4, 8, 12))#candidate|6268|(4, 8, 12)|var|bool
var_6269 = relay.var("var_6269", dtype = "bool", shape = (4, 8, 12))#candidate|6269|(4, 8, 12)|var|bool
bop_6270 = relay.logical_or(var_6268.astype('bool'), relay.reshape(var_6269.astype('bool'), relay.shape_of(var_6268))) # shape=(4, 8, 12)
uop_6275 = relay.acosh(bop_6270.astype('float64')) # shape=(4, 8, 12)
bop_6279 = relay.less_equal(uop_6275.astype('bool'), relay.reshape(var_6269.astype('bool'), relay.shape_of(uop_6275))) # shape=(4, 8, 12)
bop_6289 = relay.multiply(var_6269.astype('uint64'), relay.reshape(uop_6275.astype('uint64'), relay.shape_of(var_6269))) # shape=(4, 8, 12)
output = relay.Tuple([bop_6279,bop_6289,])
output2 = relay.Tuple([bop_6279,bop_6289,])
func_6301 = relay.Function([var_6268,var_6269,], output)
mod['func_6301'] = func_6301
mod = relay.transform.InferType()(mod)
var_6302 = relay.var("var_6302", dtype = "bool", shape = (4, 8, 12))#candidate|6302|(4, 8, 12)|var|bool
var_6303 = relay.var("var_6303", dtype = "bool", shape = (4, 8, 12))#candidate|6303|(4, 8, 12)|var|bool
output = func_6301(var_6302,var_6303,)
func_6304 = relay.Function([var_6302,var_6303,], output)
mutated_mod['func_6304'] = func_6304
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4394_call = mod.get_global_var('func_4394')
func_4395_call = mutated_mod.get_global_var('func_4395')
call_6344 = relay.TupleGetItem(func_4394_call(), 1)
call_6345 = relay.TupleGetItem(func_4395_call(), 1)
uop_6377 = relay.exp(call_6344.astype('float32')) # shape=(520, 1)
uop_6379 = relay.exp(call_6345.astype('float32')) # shape=(520, 1)
func_3544_call = mod.get_global_var('func_3544')
func_3548_call = mutated_mod.get_global_var('func_3548')
var_6387 = relay.var("var_6387", dtype = "int8", shape = (1638,))#candidate|6387|(1638,)|var|int8
call_6386 = relay.TupleGetItem(func_3544_call(relay.reshape(var_6387.astype('int8'), [13, 14, 9]), relay.reshape(uop_6377.astype('uint8'), [520, 1]), ), 0)
call_6388 = relay.TupleGetItem(func_3548_call(relay.reshape(var_6387.astype('int8'), [13, 14, 9]), relay.reshape(uop_6377.astype('uint8'), [520, 1]), ), 0)
output = relay.Tuple([uop_6377,call_6386,var_6387,])
output2 = relay.Tuple([uop_6379,call_6388,var_6387,])
func_6390 = relay.Function([var_6387,], output)
mod['func_6390'] = func_6390
mod = relay.transform.InferType()(mod)
mutated_mod['func_6390'] = func_6390
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6391 = relay.var("var_6391", dtype = "int8", shape = (1638,))#candidate|6391|(1638,)|var|int8
func_6390_call = mutated_mod.get_global_var('func_6390')
call_6392 = func_6390_call(var_6391)
output = call_6392
func_6393 = relay.Function([var_6391], output)
mutated_mod['func_6393'] = func_6393
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4786_call = mod.get_global_var('func_4786')
func_4788_call = mutated_mod.get_global_var('func_4788')
call_6427 = func_4786_call()
call_6428 = func_4786_call()
const_6436 = relay.const([[[9,-3,-2,8,3,1,3,1,-8],[10,-6,2,-3,-10,-4,3,6,-10],[-8,10,-2,-7,4,6,6,7,-5],[6,10,1,6,-7,9,-3,-8,8],[1,-4,5,6,-8,-5,-1,-2,-6],[-5,8,-7,1,-6,2,-10,1,-7],[-6,10,-7,8,8,1,7,-6,-1],[-4,2,3,5,-6,-7,-7,-7,8],[3,-4,-10,-3,-4,-1,-4,7,-6],[8,4,-10,-7,6,3,10,4,7],[2,8,-2,8,4,10,8,1,-1],[2,9,4,4,10,-1,-1,-8,6],[9,-4,1,-3,1,8,-9,2,10],[10,3,3,6,4,2,3,-5,-4]],[[-10,-5,5,5,-8,1,-4,-4,-10],[10,1,-1,-5,4,-9,10,9,10],[-1,-7,-3,-6,9,5,-9,9,-10],[-2,-5,7,-9,5,2,-2,-2,1],[9,-4,9,10,-2,-5,1,9,6],[-10,-3,-2,2,-10,-5,10,10,2],[3,7,-3,10,-2,10,5,4,6],[-4,2,-3,-7,-8,-6,6,2,-5],[-6,9,-3,7,-10,5,8,4,-3],[4,-9,7,-5,-7,6,4,-8,-1],[3,-7,8,-6,-1,-4,-7,-6,-5],[6,-6,6,8,4,-4,-6,-3,-9],[5,7,8,-2,-2,-5,-1,-4,5],[-9,-4,8,-7,5,7,1,1,-10]],[[9,-6,-10,7,-4,-8,-3,-2,9],[-4,-4,8,-5,3,-7,7,-7,-7],[5,-8,-5,6,3,-6,7,1,-1],[3,8,-3,1,8,-2,6,-9,4],[1,3,-9,-8,-8,-8,-8,6,8],[-10,7,10,-5,9,-1,9,5,7],[10,2,6,9,-2,-1,-2,3,9],[3,10,-7,4,-2,-7,-5,-4,-4],[-9,-4,8,5,-6,-1,2,10,-3],[2,2,-8,-2,-7,4,-7,-6,7],[-8,-4,-1,-1,7,6,8,-9,1],[-1,-4,1,2,10,1,-2,10,-3],[-10,-5,-6,9,10,-4,7,5,-6],[7,4,-5,-7,-4,-2,-7,3,-9]],[[4,3,-6,-6,-2,4,7,5,-1],[6,7,2,-1,2,-10,3,1,-7],[-2,-1,3,-4,7,2,8,-5,-8],[-4,7,-2,-9,2,-4,-8,-3,3],[-4,-6,4,10,-6,7,-5,4,9],[10,5,-5,-2,-5,1,3,-5,-8],[-9,-1,5,-2,2,-2,-5,6,-4],[-9,5,-5,4,-2,7,7,10,2],[9,4,1,10,-8,-6,-9,-3,10],[3,-4,-2,6,-8,1,-10,5,2],[1,1,-8,4,-1,4,-2,7,1],[-8,3,3,-7,4,8,9,-8,9],[-5,-5,-9,-2,-5,9,-10,-5,5],[7,-3,-8,-5,-10,-5,-8,3,9]],[[-4,5,1,9,2,-6,-4,-3,-4],[-9,5,-3,-10,3,6,-7,4,-2],[-9,6,-7,-10,-5,-9,5,-9,9],[3,3,-5,7,-9,-8,-7,4,-8],[-8,-3,5,-2,-1,-1,1,10,-9],[2,8,8,-4,5,-8,8,-3,-9],[-2,9,3,4,5,7,10,7,-3],[-6,-9,5,-3,-1,4,7,2,1],[-9,9,-8,5,8,-8,8,-5,4],[-4,3,-5,7,4,1,3,10,-3],[10,8,1,-6,9,-8,1,2,-7],[-10,-1,2,-10,4,-8,-10,-5,4],[-4,5,-4,-10,4,9,-1,4,5],[-5,-2,5,-4,-10,-3,4,-7,-3]],[[-3,5,5,7,-5,7,8,7,1],[-3,6,3,-8,-9,8,-5,6,-8],[-6,-8,-7,-2,-9,6,10,-4,-3],[-8,-5,-7,10,4,3,-9,-7,3],[2,-9,-4,-8,8,-3,-10,-3,7],[-6,5,-2,-3,9,-8,4,-8,10],[1,8,-1,-10,1,5,-7,-6,-2],[1,1,-5,-4,10,3,-6,9,4],[7,2,1,-8,10,-1,4,10,-5],[6,-6,-1,-6,3,-3,7,5,9],[-9,-4,-3,-3,-8,4,-10,3,5],[-4,5,6,6,-7,5,7,-3,4],[6,4,-4,7,7,9,8,-2,-1],[-8,-4,-10,-10,-4,5,-10,-9,7]],[[1,7,-8,1,-8,-6,3,-9,-2],[7,-5,-7,-1,3,9,3,-6,1],[7,-7,-5,5,10,7,5,3,7],[10,5,9,-5,-8,-5,2,-1,6],[-5,-5,6,-4,8,-1,-5,2,-4],[8,5,10,-4,-1,-5,-2,9,5],[3,-8,-7,3,-10,6,8,-5,9],[-5,2,-10,3,7,-3,-1,2,-5],[-8,10,7,-4,-9,10,-8,3,-2],[-7,6,9,4,6,-9,4,-1,-7],[-2,5,-4,1,1,2,-6,-10,-10],[-6,1,10,-2,7,-1,-4,-7,-4],[4,-3,-9,8,-1,-2,7,7,9],[-8,-4,-6,1,-7,9,-1,7,9]],[[6,-3,-6,-10,-10,-3,-6,10,9],[-4,8,-1,5,1,6,9,-7,-1],[-5,10,-7,4,5,3,2,6,-1],[8,-1,-7,6,10,-8,8,3,-9],[-2,-4,-7,-3,-4,-10,8,-10,-4],[7,-5,-7,10,-6,-5,3,-8,-4],[-4,5,-6,7,-10,4,-8,-7,-7],[-7,10,-10,-6,2,-10,10,-3,-5],[9,-4,9,-4,8,9,6,2,9],[2,-5,-1,1,10,-6,5,-7,4],[-9,-4,-2,4,-8,5,-10,-5,3],[9,-9,8,-4,-9,-3,8,1,-9],[-4,10,-9,1,4,-4,4,-1,-2],[8,-3,10,8,-8,-7,-2,9,-5]],[[7,-6,4,9,3,2,-8,-5,7],[-7,-3,-6,1,1,9,8,4,8],[6,-9,-7,8,3,-6,-9,7,-9],[2,10,2,1,-5,6,6,-1,2],[-8,-3,4,-3,-6,4,-3,7,-2],[-1,1,-2,9,8,3,-8,-10,3],[-2,-6,-7,4,-1,-1,2,-7,-10],[-9,-7,9,-6,-2,-9,10,-3,2],[1,10,-8,4,-5,-4,-10,-3,1],[6,10,6,4,1,-6,-7,-8,8],[10,-8,3,-9,7,9,-4,7,-6],[3,1,-7,-8,4,1,-4,4,-5],[5,1,8,2,-6,5,-4,-1,-4],[-1,-1,8,7,-3,3,-9,2,10]],[[9,-1,1,-6,-6,-9,3,3,-5],[8,-1,4,-8,2,-2,-9,4,-5],[-6,1,9,-4,-2,-10,8,-10,6],[-2,-8,4,9,-10,-3,-10,-9,3],[-5,-2,-4,5,-8,-10,10,1,-8],[-9,-10,10,5,4,-4,-1,4,5],[6,9,-6,10,-10,-5,8,5,-2],[-3,8,-10,4,1,-7,-7,6,-4],[-2,-10,7,-1,9,5,3,-10,-3],[5,-4,-7,-1,-1,-10,-1,1,-5],[5,3,1,7,6,-7,8,8,8],[-2,-2,8,-7,-2,-8,-7,2,1],[8,9,5,-2,-10,6,8,7,-10],[9,3,6,-10,-8,-4,8,-7,7]],[[7,-7,-2,4,-3,-9,9,-10,1],[6,10,-6,3,6,2,-3,3,-7],[5,4,-4,8,-10,6,4,-5,-7],[9,-6,9,-8,-9,2,-5,-5,4],[-9,5,-3,-1,4,-3,8,1,5],[-3,2,-4,-6,-3,8,-2,-4,-8],[-9,-5,-6,4,-8,-9,-4,-8,2],[3,2,1,-7,-9,-2,-7,-8,6],[9,-10,-6,2,1,8,-1,-3,9],[5,9,-7,2,3,-4,-4,8,2],[2,4,3,1,3,8,-10,-9,8],[-9,10,10,1,-1,-9,5,-6,-9],[2,-2,3,-10,5,-9,5,-5,2],[-3,3,-5,6,6,-10,-8,2,-9]],[[1,6,-9,1,5,-3,5,-1,9],[-1,-6,6,1,-10,5,7,-9,4],[-10,-3,2,3,1,6,-7,-4,3],[9,-3,6,-8,-6,6,6,4,2],[-5,-3,-8,-6,-7,8,-10,3,-7],[3,-2,2,-8,5,-8,-6,-3,-9],[10,-5,-4,7,1,-9,-9,-4,1],[10,-6,9,-3,7,8,6,-1,-4],[-6,-1,1,7,-2,2,9,-1,8],[-9,9,-6,1,-2,4,9,7,9],[10,7,-7,3,10,10,-8,-6,6],[1,-5,-2,-8,-1,1,-10,-5,10],[5,-9,1,-10,2,-3,1,8,6],[-9,2,-9,9,3,8,8,-1,10]],[[-8,-9,10,1,-8,9,8,8,5],[3,1,-8,1,4,-4,-4,-5,-5],[8,6,4,8,1,-3,7,2,4],[-7,-7,9,-5,6,-9,-5,-8,1],[-6,3,6,4,2,1,8,-2,-1],[8,5,6,-6,9,3,5,10,5],[-6,1,-6,5,-2,-1,-10,-9,-3],[-9,7,3,7,-7,8,4,4,-1],[8,6,-2,3,4,-5,6,-7,3],[4,8,6,5,9,5,-2,5,-3],[5,-9,7,-7,9,7,-4,1,-2],[1,8,9,-1,6,-10,-4,-4,-5],[8,-5,8,8,-3,-5,7,4,-5],[9,-3,3,-6,8,10,1,7,-5]]], dtype = "int8")#candidate|6436|(13, 14, 9)|const|int8
bop_6437 = relay.not_equal(call_6427.astype('bool'), relay.reshape(const_6436.astype('bool'), relay.shape_of(call_6427))) # shape=(13, 14, 9)
bop_6440 = relay.not_equal(call_6428.astype('bool'), relay.reshape(const_6436.astype('bool'), relay.shape_of(call_6428))) # shape=(13, 14, 9)
output = bop_6437
output2 = bop_6440
func_6444 = relay.Function([], output)
mod['func_6444'] = func_6444
mod = relay.transform.InferType()(mod)
output = func_6444()
func_6445 = relay.Function([], output)
mutated_mod['func_6445'] = func_6445
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3493_call = mod.get_global_var('func_3493')
func_3494_call = mutated_mod.get_global_var('func_3494')
call_6460 = relay.TupleGetItem(func_3493_call(), 6)
call_6461 = relay.TupleGetItem(func_3494_call(), 6)
var_6467 = relay.var("var_6467", dtype = "int8", shape = (13, 14, 9))#candidate|6467|(13, 14, 9)|var|int8
bop_6468 = relay.subtract(call_6460.astype('int8'), relay.reshape(var_6467.astype('int8'), relay.shape_of(call_6460))) # shape=(13, 14, 9)
bop_6471 = relay.subtract(call_6461.astype('int8'), relay.reshape(var_6467.astype('int8'), relay.shape_of(call_6461))) # shape=(13, 14, 9)
func_3081_call = mod.get_global_var('func_3081')
func_3083_call = mutated_mod.get_global_var('func_3083')
call_6474 = relay.TupleGetItem(func_3081_call(), 0)
call_6475 = relay.TupleGetItem(func_3083_call(), 0)
var_6476 = relay.var("var_6476", dtype = "float32", shape = (520,))#candidate|6476|(520,)|var|float32
bop_6477 = relay.bitwise_or(call_6474.astype('uint8'), relay.reshape(var_6476.astype('uint8'), relay.shape_of(call_6474))) # shape=(520,)
bop_6480 = relay.bitwise_or(call_6475.astype('uint8'), relay.reshape(var_6476.astype('uint8'), relay.shape_of(call_6475))) # shape=(520,)
func_5373_call = mod.get_global_var('func_5373')
func_5374_call = mutated_mod.get_global_var('func_5374')
call_6491 = func_5373_call()
call_6492 = func_5373_call()
output = relay.Tuple([bop_6468,bop_6477,call_6491,])
output2 = relay.Tuple([bop_6471,bop_6480,call_6492,])
func_6493 = relay.Function([var_6467,var_6476,], output)
mod['func_6493'] = func_6493
mod = relay.transform.InferType()(mod)
mutated_mod['func_6493'] = func_6493
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6493_call = mutated_mod.get_global_var('func_6493')
var_6495 = relay.var("var_6495", dtype = "int8", shape = (13, 14, 9))#candidate|6495|(13, 14, 9)|var|int8
var_6496 = relay.var("var_6496", dtype = "float32", shape = (520,))#candidate|6496|(520,)|var|float32
call_6494 = func_6493_call(var_6495,var_6496,)
output = call_6494
func_6497 = relay.Function([var_6495,var_6496,], output)
mutated_mod['func_6497'] = func_6497
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5218_call = mod.get_global_var('func_5218')
func_5219_call = mutated_mod.get_global_var('func_5219')
call_6518 = relay.TupleGetItem(func_5218_call(), 0)
call_6519 = relay.TupleGetItem(func_5219_call(), 0)
func_181_call = mod.get_global_var('func_181')
func_184_call = mutated_mod.get_global_var('func_184')
var_6523 = relay.var("var_6523", dtype = "uint16", shape = (11, 14))#candidate|6523|(11, 14)|var|uint16
call_6522 = relay.TupleGetItem(func_181_call(relay.reshape(var_6523.astype('uint16'), [14, 11, 1])), 1)
call_6524 = relay.TupleGetItem(func_184_call(relay.reshape(var_6523.astype('uint16'), [14, 11, 1])), 1)
func_5715_call = mod.get_global_var('func_5715')
func_5717_call = mutated_mod.get_global_var('func_5717')
call_6530 = func_5715_call()
call_6531 = func_5715_call()
output = relay.Tuple([call_6518,call_6522,var_6523,call_6530,])
output2 = relay.Tuple([call_6519,call_6524,var_6523,call_6531,])
func_6533 = relay.Function([var_6523,], output)
mod['func_6533'] = func_6533
mod = relay.transform.InferType()(mod)
var_6534 = relay.var("var_6534", dtype = "uint16", shape = (11, 14))#candidate|6534|(11, 14)|var|uint16
output = func_6533(var_6534)
func_6535 = relay.Function([var_6534], output)
mutated_mod['func_6535'] = func_6535
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3081_call = mod.get_global_var('func_3081')
func_3083_call = mutated_mod.get_global_var('func_3083')
call_6630 = relay.TupleGetItem(func_3081_call(), 0)
call_6631 = relay.TupleGetItem(func_3083_call(), 0)
func_6390_call = mod.get_global_var('func_6390')
func_6393_call = mutated_mod.get_global_var('func_6393')
const_6638 = relay.const([2,6,6,1,9,-10,4,-3,9,2,-2,-10,6,3,9,1,-1,3,-10,1,6,4,1,-5,-3,-10,-8,5,6,-3,8,-8,2,-6,8,4,9,6,-7,2,-9,-6,3,-10,-9,-3,6,-8,5,-1,-9,8,2,8,4,1,2,-10,-9,5,-5,5,-2,-2,-6,9,-9,-3,-1,-2,1,-10,-1,10,-5,9,3,-3,-8,-1,9,8,-9,3,-4,-8,-8,-9,-1,10,6,-5,-5,6,-5,-6,1,4,-8,1,-2,6,7,1,-6,3,-10,5,-9,9,-9,10,-2,9,1,-2,1,5,3,6,-6,-5,9,4,-10,4,1,-1,-10,4,4,-6,-4,-1,-6,-10,7,-1,-5,8,1,9,6,8,2,-9,10,9,6,-4,-10,7,10,-8,6,-2,-6,2,1,-9,-3,-9,-4,8,-10,-4,-5,-10,2,1,1,-6,4,-2,7,-8,-2,3,5,7,4,-6,4,-5,3,4,-1,3,-10,10,6,10,-5,3,-6,5,-2,8,-8,-4,-9,5,1,-5,2,-10,5,4,5,-10,-8,1,-8,5,4,-9,10,-4,3,-3,7,3,5,2,5,-3,8,2,-2,4,-8,10,-8,-10,2,-5,-7,10,6,-4,-5,3,-8,1,-5,8,9,-3,10,9,-7,2,-1,-7,-8,7,5,-7,8,-7,-5,6,2,-1,3,8,-4,-5,5,-1,5,6,-1,-7,1,4,8,9,1,4,-10,5,3,1,4,-2,-2,-10,-1,4,8,7,-7,-8,6,2,4,-4,-7,-8,-6,9,1,3,-6,-6,-2,-2,1,7,4,7,-7,7,-3,5,7,7,5,4,6,10,4,9,4,7,5,7,5,6,-1,9,-6,10,8,-7,-3,-4,-8,6,-9,9,-7,8,10,-1,-6,3,-1,-5,4,-5,6,-5,2,-4,4,-9,-10,4,10,3,8,-7,-6,9,-4,-10,-4,3,-6,-9,2,3,4,4,-3,-9,2,9,10,-9,-4,3,3,4,-6,-4,-2,2,2,-9,2,5,7,1,4,10,-8,6,2,5,-6,6,-5,3,4,-4,3,8,5,-5,-9,9,-1,-3,6,1,-6,-7,5,10,-3,6,4,-5,-3,-8,-7,-10,-1,-1,10,8,-9,10,-6,-3,-5,-6,-3,9,-1,-6,3,7,10,2,8,-9,4,10,10,-8,2,-7,3,1,-3,4,-5,-2,9,-7,4,3,-5,-6,8,-1,8,-7,2,-4,-5,2,9,4,-10,4,-7,9,-4,7,9,-4,6,7,-9,4,1,-5,4,8,-2,-7,3,-1,3,9,-7,-10,-6,10,9,-1,-2,1,-8,9,1,-1,3,1,1,9,-3,-1,-3,-6,5,-3,6,4,-10,5,8,-6,-7,9,7,8,-5,8,-9,10,-2,4,6,-1,10,10,10,-1,2,-9,-7,10,-7,10,3,-4,5,-2,-6,7,-8,4,-2,-9,4,-5,6,-1,-6,-10,4,-5,-2,10,-1,-1,-6,1,9,-4,7,-4,-7,-7,-7,-1,9,-10,4,-8,-8,7,4,-2,7,6,7,8,-4,-6,-10,-1,-4,1,-4,-6,7,-8,1,-4,6,-4,-9,-7,-7,-3,2,9,7,-8,10,5,7,-8,3,-7,-3,2,-3,-2,-3,-9,-1,5,-8,-8,6,6,5,4,-8,-9,-3,-3,-1,9,2,-3,6,-10,10,3,-3,1,-4,8,-7,-7,7,7,6,3,3,2,3,-6,-2,-1,1,-3,-9,9,5,4,-5,-1,8,1,-10,-3,-5,-8,-1,1,2,-6,-4,-5,-2,-2,-4,10,-7,-3,3,3,-8,-6,9,10,-9,2,-5,2,-8,6,7,3,-6,2,6,-1,6,3,3,9,-2,-7,8,4,-8,-9,6,-1,-2,-6,-8,-3,2,-2,-1,-1,3,-2,1,-8,-6,-4,-3,-7,-7,3,9,2,6,-10,-6,-2,1,10,9,3,-7,10,-3,4,1,7,-7,-1,4,10,4,-9,-5,9,8,-9,-10,-6,-7,2,10,-8,-8,-10,2,-2,-1,1,3,9,-3,-8,-7,-5,5,-2,9,-3,-9,-9,2,-7,-4,10,10,9,-6,-6,1,9,1,2,1,6,8,-3,7,-5,10,-6,-3,-4,2,-3,-3,1,-6,-3,8,-9,5,7,5,10,-7,6,3,-8,1,-10,-6,6,5,10,-1,10,-2,7,-8,5,-5,-3,2,-5,-7,-5,7,-6,5,6,5,-1,2,6,-6,3,-3,-10,-2,-8,-2,-3,-6,-1,-6,-6,-2,10,6,-2,-9,4,5,-9,-10,5,9,3,8,-8,-3,-5,-3,9,-3,10,7,-5,7,-1,-10,1,6,-7,-7,7,9,-5,9,10,4,-5,5,5,-4,10,-5,-3,4,3,5,1,4,-6,9,-4,-7,8,-10,5,1,8,-8,-5,3,6,-10,1,7,8,3,-1,-2,4,1,-4,9,-8,-4,-1,-3,-6,8,-8,5,10,-9,-10,-9,-10,8,-5,-7,3,-6,-10,-5,-1,-4,-5,6,-6,-8,3,-3,-10,-7,7,7,-9,6,9,6,4,10,8,7,-10,-2,-4,8,-7,8,10,6,8,9,-3,9,4,9,7,7,2,-2,6,2,-4,-7,-8,4,-5,3,-9,-7,4,-6,-3,8,-2,-6,8,-2,-10,9,-2,-6,-7,6,3,-10,1,-6,6,-4,4,-7,-7,7,7,-7,-8,-5,2,-2,7,2,5,-4,3,3,7,-2,-8,6,-4,6,6,8,3,4,9,7,5,-6,1,-6,1,7,-6,7,-5,-1,-4,-2,-6,-8,4,10,9,10,7,-10,-3,-8,-9,-8,-9,9,7,-2,-10,9,-8,-5,-8,8,-8,-6,7,-3,-10,-3,9,2,-5,-10,-7,-9,9,3,-7,-5,-1,-10,-4,7,4,-2,-1,-1,-1,1,2,-4,-4,-10,-9,-7,-5,-1,10,4,-7,6,-3,6,8,3,-7,-10,-5,1,-5,-6,-5,-1,6,-6,-2,-5,-9,-2,-8,6,-3,6,7,3,8,-4,10,-8,9,-1,8,9,-9,-6,-7,2,-3,9,8,3,3,6,1,2,-10,4,-1,7,3,6,-10,-1,7,-2,-3,-8,2,-2,10,4,8,-7,-10,-8,-8,4,-3,8,4,4,6,-4,7,-3,1,-6,7,8,8,2,-10,-3,-3,2,2,5,-9,-6,6,-5,7,5,-5,-3,9,-8,-4,-2,1,-4,-10,-10,-9,-5,-4,-3,-2,-6,1,1,-5,-9,-9,5,6,2,8,7,6,2,4,4,-4,-4,-10,-3,1,5,4,9,-9,6,-1,-5,-4,-1,-10,4,-5,-9,3,-3,5,-4,10,-8,4,-6,-8,-4,-8,1,-9,-2,-5,-1,-2,-3,-4,7,-10,-3,-1,-9,-2,1,9,-7,-9,3,1,-2,-10,-1,10,10,-3,6,4,2,10,7,5,8,-7,10,8,-1,5,-5,-2,-6,-10,10,10,1,7,-1,-3,8,3,8,-8,-2,-4,9,-5,-2,7,-8,-6,-1,8,5,5,1,-1,-1,-9,3,3,-9,7,1,3,-5,8,-10,-7,8,-10,10,-10,-2,4,-4,9,3,-5,2,-4,7,-2,-10,3,1,-9,-7,-1,-9,6,4,-9,1,-3,-1,9,-1,-6,2,-1,5,3,8,-2,-3,-2,-4,-5,-4,10,-7,7,2,1,5,6,-1,-1,-4,-7,1,-5,-10,-2,9,4,-2,8,-4,-7,-2,-8,-1,1,2,-4,5,10,10,-4,3,-8,6,-1,4,9,1,6,-6,1,3,3,-7,-7,-4,-7,-8,-3,1,-7,4,-1,-3,10,4,-7,9,8,2,2,-8,-4,5,1,3,-1,5,-3,10,8,-5,2,-7,-7,-8,7,-1,2,-10,4,-2,2,8,6,9,2,10,-5,4,6,-2,-10,5,10,5,-9,-8,4,8,-2,3,8,-7,10,6,5,-10,2,-7,1,4,-10,-2,-10,6,7,5,-3,-10,-6,-9,-4,-8,-4,-9,-8,4,-7,2,-9,9,-8,-1,9,-5,8,7,-5,-8,-9,-4,2,-5,-6,-8,7,-1,6,-7,-3,-1,6,-3,-3,10,2,1,1,4,-4,2,-2,6,5,2,-8,9,10,-5,-4,9,6,-9,7,-6,-8,2,-1,7,-4,4,-1,-5,4,8,-4,6,-8,-9,-2,7,3,-9,10,2,4,-7,8,8,4,2,4,10,-6,-10,-5,-8,6,5,-3,3,3,-2,6,3,-9,-7,-4,6,7,-10,-3,-3,6,-9,4,-4,-4,8,-8,9,5,-10,-5,10,-4,-6,-7,-8,-8,-1,8,1,-4], dtype = "int8")#candidate|6638|(1638,)|const|int8
call_6637 = relay.TupleGetItem(func_6390_call(relay.reshape(const_6638.astype('int8'), [1638,])), 0)
call_6639 = relay.TupleGetItem(func_6393_call(relay.reshape(const_6638.astype('int8'), [1638,])), 0)
output = relay.Tuple([call_6630,call_6637,const_6638,])
output2 = relay.Tuple([call_6631,call_6639,const_6638,])
func_6641 = relay.Function([], output)
mod['func_6641'] = func_6641
mod = relay.transform.InferType()(mod)
output = func_6641()
func_6642 = relay.Function([], output)
mutated_mod['func_6642'] = func_6642
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6643 = relay.var("var_6643", dtype = "float32", shape = (12, 15, 1))#candidate|6643|(12, 15, 1)|var|float32
uop_6644 = relay.tan(var_6643.astype('float32')) # shape=(12, 15, 1)
func_2929_call = mod.get_global_var('func_2929')
func_2931_call = mutated_mod.get_global_var('func_2931')
call_6653 = relay.TupleGetItem(func_2929_call(), 5)
call_6654 = relay.TupleGetItem(func_2931_call(), 5)
bop_6655 = relay.less(uop_6644.astype('bool'), relay.reshape(var_6643.astype('bool'), relay.shape_of(uop_6644))) # shape=(12, 15, 1)
func_3755_call = mod.get_global_var('func_3755')
func_3756_call = mutated_mod.get_global_var('func_3756')
call_6675 = func_3755_call()
call_6676 = func_3755_call()
output = relay.Tuple([call_6653,bop_6655,call_6675,])
output2 = relay.Tuple([call_6654,bop_6655,call_6676,])
func_6677 = relay.Function([var_6643,], output)
mod['func_6677'] = func_6677
mod = relay.transform.InferType()(mod)
var_6678 = relay.var("var_6678", dtype = "float32", shape = (12, 15, 1))#candidate|6678|(12, 15, 1)|var|float32
output = func_6677(var_6678)
func_6679 = relay.Function([var_6678], output)
mutated_mod['func_6679'] = func_6679
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4727_call = mod.get_global_var('func_4727')
func_4729_call = mutated_mod.get_global_var('func_4729')
call_6686 = relay.TupleGetItem(func_4727_call(), 0)
call_6687 = relay.TupleGetItem(func_4729_call(), 0)
const_6704 = relay.const([[[3],[5],[1],[-7],[2],[-3],[7],[-2],[10],[-6],[3]],[[1],[6],[10],[-1],[4],[-10],[10],[-2],[4],[-10],[2]],[[-1],[-8],[4],[9],[3],[1],[-3],[7],[-2],[10],[10]],[[5],[-6],[6],[8],[-3],[-2],[-1],[-5],[8],[-2],[9]],[[-10],[9],[-5],[-5],[-8],[7],[-9],[-10],[-2],[-7],[-6]],[[-1],[-1],[-10],[7],[-6],[4],[-10],[4],[-6],[-6],[-6]],[[7],[-2],[-1],[-3],[9],[9],[-2],[1],[-8],[8],[-4]],[[-3],[-2],[1],[-1],[2],[3],[6],[5],[2],[-3],[2]],[[-9],[9],[-1],[9],[3],[-6],[-10],[-4],[-3],[10],[-2]],[[-1],[-8],[-3],[-1],[-10],[-9],[8],[-4],[-7],[-1],[-6]],[[9],[-4],[6],[-10],[2],[7],[2],[3],[-4],[-6],[10]],[[5],[2],[-4],[5],[4],[8],[6],[-1],[4],[6],[5]],[[3],[3],[-1],[-2],[-2],[-6],[9],[7],[-8],[7],[8]],[[1],[10],[7],[9],[3],[-2],[-1],[5],[5],[-2],[-4]]], dtype = "int32")#candidate|6704|(14, 11, 1)|const|int32
bop_6705 = relay.equal(call_6686.astype('bool'), relay.reshape(const_6704.astype('bool'), relay.shape_of(call_6686))) # shape=(14, 11, 1)
bop_6708 = relay.equal(call_6687.astype('bool'), relay.reshape(const_6704.astype('bool'), relay.shape_of(call_6687))) # shape=(14, 11, 1)
uop_6709 = relay.sinh(const_6704.astype('float32')) # shape=(14, 11, 1)
output = relay.Tuple([bop_6705,uop_6709,])
output2 = relay.Tuple([bop_6708,uop_6709,])
func_6717 = relay.Function([], output)
mod['func_6717'] = func_6717
mod = relay.transform.InferType()(mod)
output = func_6717()
func_6718 = relay.Function([], output)
mutated_mod['func_6718'] = func_6718
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4463_call = mod.get_global_var('func_4463')
func_4464_call = mutated_mod.get_global_var('func_4464')
call_6736 = relay.TupleGetItem(func_4463_call(), 1)
call_6737 = relay.TupleGetItem(func_4464_call(), 1)
output = call_6736
output2 = call_6737
func_6741 = relay.Function([], output)
mod['func_6741'] = func_6741
mod = relay.transform.InferType()(mod)
mutated_mod['func_6741'] = func_6741
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6741_call = mutated_mod.get_global_var('func_6741')
call_6742 = func_6741_call()
output = call_6742
func_6743 = relay.Function([], output)
mutated_mod['func_6743'] = func_6743
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3851_call = mod.get_global_var('func_3851')
func_3852_call = mutated_mod.get_global_var('func_3852')
call_6760 = func_3851_call()
call_6761 = func_3851_call()
output = call_6760
output2 = call_6761
func_6774 = relay.Function([], output)
mod['func_6774'] = func_6774
mod = relay.transform.InferType()(mod)
output = func_6774()
func_6775 = relay.Function([], output)
mutated_mod['func_6775'] = func_6775
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6444_call = mod.get_global_var('func_6444')
func_6445_call = mutated_mod.get_global_var('func_6445')
call_6793 = func_6444_call()
call_6794 = func_6444_call()
output = call_6793
output2 = call_6794
func_6809 = relay.Function([], output)
mod['func_6809'] = func_6809
mod = relay.transform.InferType()(mod)
mutated_mod['func_6809'] = func_6809
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6809_call = mutated_mod.get_global_var('func_6809')
call_6810 = func_6809_call()
output = call_6810
func_6811 = relay.Function([], output)
mutated_mod['func_6811'] = func_6811
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6829 = relay.var("var_6829", dtype = "float32", shape = (16, 14, 4))#candidate|6829|(16, 14, 4)|var|float32
uop_6830 = relay.acos(var_6829.astype('float32')) # shape=(16, 14, 4)
output = uop_6830
output2 = uop_6830
func_6835 = relay.Function([var_6829,], output)
mod['func_6835'] = func_6835
mod = relay.transform.InferType()(mod)
var_6836 = relay.var("var_6836", dtype = "float32", shape = (16, 14, 4))#candidate|6836|(16, 14, 4)|var|float32
output = func_6835(var_6836)
func_6837 = relay.Function([var_6836], output)
mutated_mod['func_6837'] = func_6837
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3755_call = mod.get_global_var('func_3755')
func_3756_call = mutated_mod.get_global_var('func_3756')
call_6884 = func_3755_call()
call_6885 = func_3755_call()
var_6889 = relay.var("var_6889", dtype = "int8", shape = (13, 14, 9))#candidate|6889|(13, 14, 9)|var|int8
bop_6890 = relay.power(call_6884.astype('float32'), relay.reshape(var_6889.astype('float32'), relay.shape_of(call_6884))) # shape=(13, 14, 9)
bop_6893 = relay.power(call_6885.astype('float32'), relay.reshape(var_6889.astype('float32'), relay.shape_of(call_6885))) # shape=(13, 14, 9)
func_4880_call = mod.get_global_var('func_4880')
func_4882_call = mutated_mod.get_global_var('func_4882')
call_6895 = relay.TupleGetItem(func_4880_call(relay.reshape(var_6889.astype('int8'), [13, 14, 9])), 0)
call_6896 = relay.TupleGetItem(func_4882_call(relay.reshape(var_6889.astype('int8'), [13, 14, 9])), 0)
output = relay.Tuple([bop_6890,call_6895,])
output2 = relay.Tuple([bop_6893,call_6896,])
func_6899 = relay.Function([var_6889,], output)
mod['func_6899'] = func_6899
mod = relay.transform.InferType()(mod)
var_6900 = relay.var("var_6900", dtype = "int8", shape = (13, 14, 9))#candidate|6900|(13, 14, 9)|var|int8
output = func_6899(var_6900)
func_6901 = relay.Function([var_6900], output)
mutated_mod['func_6901'] = func_6901
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6933 = relay.var("var_6933", dtype = "int16", shape = (4, 5, 11))#candidate|6933|(4, 5, 11)|var|int16
var_6934 = relay.var("var_6934", dtype = "int16", shape = (4, 5, 11))#candidate|6934|(4, 5, 11)|var|int16
bop_6935 = relay.not_equal(var_6933.astype('bool'), relay.reshape(var_6934.astype('bool'), relay.shape_of(var_6933))) # shape=(4, 5, 11)
func_3399_call = mod.get_global_var('func_3399')
func_3400_call = mutated_mod.get_global_var('func_3400')
call_6938 = relay.TupleGetItem(func_3399_call(), 0)
call_6939 = relay.TupleGetItem(func_3400_call(), 0)
output = relay.Tuple([bop_6935,call_6938,])
output2 = relay.Tuple([bop_6935,call_6939,])
func_6943 = relay.Function([var_6933,var_6934,], output)
mod['func_6943'] = func_6943
mod = relay.transform.InferType()(mod)
mutated_mod['func_6943'] = func_6943
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6943_call = mutated_mod.get_global_var('func_6943')
var_6945 = relay.var("var_6945", dtype = "int16", shape = (4, 5, 11))#candidate|6945|(4, 5, 11)|var|int16
var_6946 = relay.var("var_6946", dtype = "int16", shape = (4, 5, 11))#candidate|6946|(4, 5, 11)|var|int16
call_6944 = func_6943_call(var_6945,var_6946,)
output = call_6944
func_6947 = relay.Function([var_6945,var_6946,], output)
mutated_mod['func_6947'] = func_6947
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6956 = relay.var("var_6956", dtype = "uint32", shape = (5, 7, 4))#candidate|6956|(5, 7, 4)|var|uint32
const_6957 = relay.const([[[-7,1,3,5],[-8,-9,-4,-9],[-6,-1,8,-9],[-9,4,8,-10],[-6,-9,10,-7],[3,-1,7,-2],[-5,-7,-8,-5]],[[-7,-7,-2,2],[-5,-9,4,-3],[3,4,2,-2],[8,-1,6,-3],[6,8,6,-5],[2,8,-9,-5],[-3,-2,-4,3]],[[2,10,1,-2],[3,6,-1,-10],[5,9,9,8],[-2,8,-3,-9],[6,-6,1,7],[-10,-3,1,2],[-3,2,6,5]],[[-8,-3,3,-9],[-9,9,5,-6],[-6,3,-6,5],[-7,-3,-5,-8],[-9,-6,-3,3],[-2,-4,8,-9],[8,-2,-7,4]],[[-2,-7,-5,-1],[-8,-9,4,2],[6,-2,-5,7],[-2,-10,7,-5],[2,5,-8,4],[-3,-8,-6,-2],[6,7,4,-7]]], dtype = "uint32")#candidate|6957|(5, 7, 4)|const|uint32
bop_6958 = relay.subtract(var_6956.astype('uint32'), relay.reshape(const_6957.astype('uint32'), relay.shape_of(var_6956))) # shape=(5, 7, 4)
output = relay.Tuple([bop_6958,])
output2 = relay.Tuple([bop_6958,])
func_6969 = relay.Function([var_6956,], output)
mod['func_6969'] = func_6969
mod = relay.transform.InferType()(mod)
mutated_mod['func_6969'] = func_6969
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6970 = relay.var("var_6970", dtype = "uint32", shape = (5, 7, 4))#candidate|6970|(5, 7, 4)|var|uint32
func_6969_call = mutated_mod.get_global_var('func_6969')
call_6971 = func_6969_call(var_6970)
output = call_6971
func_6972 = relay.Function([var_6970], output)
mutated_mod['func_6972'] = func_6972
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5218_call = mod.get_global_var('func_5218')
func_5219_call = mutated_mod.get_global_var('func_5219')
call_7042 = relay.TupleGetItem(func_5218_call(), 0)
call_7043 = relay.TupleGetItem(func_5219_call(), 0)
func_664_call = mod.get_global_var('func_664')
func_669_call = mutated_mod.get_global_var('func_669')
var_7045 = relay.var("var_7045", dtype = "bool", shape = (1540,))#candidate|7045|(1540,)|var|bool
call_7044 = func_664_call(relay.reshape(var_7045.astype('bool'), [10, 14, 11]), relay.reshape(var_7045.astype('bool'), [10, 14, 11]), relay.reshape(var_7045.astype('bool'), [10, 14, 11]), )
call_7046 = func_664_call(relay.reshape(var_7045.astype('bool'), [10, 14, 11]), relay.reshape(var_7045.astype('bool'), [10, 14, 11]), relay.reshape(var_7045.astype('bool'), [10, 14, 11]), )
uop_7059 = relay.rsqrt(call_7044.astype('float64')) # shape=(10, 14, 11)
uop_7061 = relay.rsqrt(call_7046.astype('float64')) # shape=(10, 14, 11)
output = relay.Tuple([call_7042,var_7045,uop_7059,])
output2 = relay.Tuple([call_7043,var_7045,uop_7061,])
func_7065 = relay.Function([var_7045,], output)
mod['func_7065'] = func_7065
mod = relay.transform.InferType()(mod)
var_7066 = relay.var("var_7066", dtype = "bool", shape = (1540,))#candidate|7066|(1540,)|var|bool
output = func_7065(var_7066)
func_7067 = relay.Function([var_7066], output)
mutated_mod['func_7067'] = func_7067
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6051_call = mod.get_global_var('func_6051')
func_6052_call = mutated_mod.get_global_var('func_6052')
call_7084 = relay.TupleGetItem(func_6051_call(), 2)
call_7085 = relay.TupleGetItem(func_6052_call(), 2)
uop_7109 = relay.atanh(call_7084.astype('float32')) # shape=(520,)
uop_7111 = relay.atanh(call_7085.astype('float32')) # shape=(520,)
func_6717_call = mod.get_global_var('func_6717')
func_6718_call = mutated_mod.get_global_var('func_6718')
call_7117 = relay.TupleGetItem(func_6717_call(), 0)
call_7118 = relay.TupleGetItem(func_6718_call(), 0)
func_4643_call = mod.get_global_var('func_4643')
func_4647_call = mutated_mod.get_global_var('func_4647')
var_7120 = relay.var("var_7120", dtype = "bool", shape = ())#candidate|7120|()|var|bool
var_7121 = relay.var("var_7121", dtype = "bool", shape = (363,))#candidate|7121|(363,)|var|bool
call_7119 = relay.TupleGetItem(func_4643_call(relay.reshape(var_7120.astype('bool'), []), relay.reshape(var_7121.astype('bool'), [3, 11, 11]), ), 2)
call_7122 = relay.TupleGetItem(func_4647_call(relay.reshape(var_7120.astype('bool'), []), relay.reshape(var_7121.astype('bool'), [3, 11, 11]), ), 2)
uop_7125 = relay.sin(call_7117.astype('float64')) # shape=(14, 11, 1)
uop_7127 = relay.sin(call_7118.astype('float64')) # shape=(14, 11, 1)
func_2955_call = mod.get_global_var('func_2955')
func_2958_call = mutated_mod.get_global_var('func_2958')
const_7133 = relay.const([[-2.390964,-0.064588,-6.788654,7.660982]], dtype = "float64")#candidate|7133|(1, 4)|const|float64
const_7134 = relay.const([10,7,5,-3,-1,1,-9,-6,-10,6,-2,3,9,-6,-7,-6,3,4,7,1,8,-5,-2,10,8,7,-4,-10,8,-6,1,3,7,3,5,-1,-3,9,-9,-5,-4,-9,-3,-1,-6,-7,1,10,7,2,-7,-4,1,-4,-2,-7,3,7,4,-8,-7,7,5,7,-5,6,4,-10,5,7,-5,4,-2,-6,8,-7,1,4,5,9,-2,10,7,5,6,-9,-8,-10,3,5,4,-8,-9,-2,-6,6,8,-8,-8,6,4,-6,8,1,6,7,-1,4,9,-6,-6,5,-8,10,-7,-1,-10,3,5,-1,3,2,3,6,1,-9,2,-3,-8,-6,7,-5,-4,-9,6,3,-8,-5,-10,-4,-1,-8,-6,5,1,-8,9,-7,6,6,-6,3,-2,6,7,3,-3,-3,9,5,-9,10,8,3,-3,-6,-7,-4,7,-1,2,-4,-4,-5,7,4,-5,-4,-2,-7,-5,8,3,-1,6,7,-7,-4,-10,-1,-1,2,9,-8,-4,-10,9,-3,1,-5,7,4,4,2,-9,10,-9,-7,-2,-3,-2,-7,2,3,3,10,-9,1,-2,-7,7,-2,-4,7,4,10,5,-4,7,-10,-9,-10,5,-2,-6,10,10,2,-1,-8,8,-8,7,-8,3,-7,-8,-1,-8,-4,3,10,7,7,-8,2,7,9,-4,-10,-6,-9,2,1,-4,8,10,3,7,-7,7,3,1,-7,2,4,-2,4,5,-8,2,-6,-2,-2,-1,6,-8,1,2,4,5,3,1,5,-5,-2,-9,-9,-1,1,-10,1,7,-5,2,-4,7,8,5,3,6,-6,8,-7,-8,1,5,-4,-4,1,10,2,-3,5,-4,5,-6,7,8,-2,-10,4,3,-10,-1,-2,8,-6,6,6,-10,2,-6,9,-10,-2,-4,-8,8,-5,-8,-8,10,-7,5,-8,6,2,-6,-6,4,9,-6,-6,-4,1,-7,-10,3,5,1,-5,-3,9,-10,8,-4,-3,-5,-3,9,2,-3,2,10,-3,3,1,5,-5,-6,-8,-1,1,9,4,-7,1,-9,-7,-2,-1,8,-1,2,7,-1,10,-5,6,4,1,6,-3,-7,-3,1,-6,-8,2,-2,-1,4,-3,-10,-5,8,-6,-8,-9,-9,5,-8,9,-5,9,-1,-10,-10,6,-3,2,4,6,-7,10,7,6,-6,3,-5,1,-1,-1,-4,-10,-7,-8,2,-5,-9,7,-10,-5,-7,10,-1,7,3,-4,4,-6,10,-2,-10,-3,3,6,4,-10,10,-10,2,-4,5,4,3,10,3,-8,-10,1,3,-7,-9,-6,8,1,-5,-6,4,-2,9,-2,6,5,-1,1,6,-2,6,3,6,-5,8,3,-1,-10,-7,-5,2,-8,8,8,-9,8,-8,9,-4,7,8,-5,3,3,6,2,8,3,-1,-10,3,8,-9,-7,3,-7,4,-2,-7,-10,3,-3,3,-8,8,7,-8,-5,3,-1,10,9,-2,-4,8,-2,-3,3,-2,2,-3,-3,7,-9,2,7,10,7,-9,-10,2,-9,6,2,-4,-8,-7,-9,1,-5,10,4,-7,3,-9,-4,-5,-7,-6,-9,-5,-7,-9,7,6,2,3,5,8,-10,1,9,9,-6,-5,5,-3,-4,-1,-2,-4,-1,4,-9,-6,-1,-2,-10,6,-4,-1,3,-1,6,-10,9,7,-1,7,-3,-8,7,-3,-1,-3,2,-5,-7,3,-10,-4,-7,8,1,-9,-8,7,8,-2,-10,7,-8,6,1,-9,-2,-10,5,10,-3,8,-7,5,-6,-8,4,10,-8,-7,6,9,-10,-1,-7,1,-2,-9,6,8,-3,-8,-10,8,5,-8,-3,2,-6,-8,-6,2,8,8,-9,5,1,-10,-4,-2,6,-1,-6,2,-10,6,-9,-3,-2,-10,7,3,-1,-10,3,-3,9,8,8,9,10,3,4,8,-9,6,-6,-2,4,-9,2,-6,5,-8,1,3,1,-3,-4,-10,9,-6,5,-1,10,7,-9,6,-6,9,2,-1,7,-9,-4,3,4,-10,7,-1,-9,-2,-1,4,-3,-7,4,9,1,-2,8,10,-5,3,2,-1,-10,1,3,1,10,-2,-5,8,10,2,-5,10,-3,-4,-6,-5,-9,-2,-4,10,-8,-8,5,8,6,-1,-4,-3,-5,1,-3,2,5,-6,-4,10,-1,4,2,9,-3,1,3,-4,2,-2,4,-8,-5,-5,-3,2,3,7,-9,5,9,1,1,-4,5,-7,9,7,2,-4,8,8,-1,9,3,4,-2,-8,2,-6,-6,-5,8,1,-3,4,1,3,9,2,5,-6,2,-2,5,-1,-10,-8,-8,8,-3,3,6,-6,7,7,-5,-1,-8,-1,-10,4,9,-8,-2,-6,-1,-1,-6,-2,-8,-7,3,-9,-2,3,-5,9,2,10,-6,-1,7,3,-10,6,-5,2,-10,10,3,1,-4,-3,10,10,-10,-2,-4,10,-2,-3,-9,7,-6,-1,-2,-1,7,-3,-5,-2,4,4,2,2,-10,3,10,9,8,-8,-6,-7,3,9,-2,5,-6,-4,10,-2,-2,2,-6,-9,2,-5,6,-9,-1,-7,9,1,-8,6,4,2,5,-8,-4,-5,6,-3,1,1,2,9,9,-9,-6,7,-2,-5,-1,-6,-2,1,1,10,10,8,-1,-3,8,7,8,-5,5,5,-5,-10,4,-6,-7,-10,10,-9,6,1,-8,7,4,-4,2,-6,-4,3,-10,-6,-7,-6,-6,-8,-8,6,9,2,3,-4,-9,1,9,-3,5,7,-8,9,-7,8,-7,-3,-8,-4,1,8,-10,-5,-5,7,-10,1,7,-3,8,10,-6,6,8,-6,1,10,3,10,4,7,4,-3,2,3,-9,-7,-8,8,-4,6,8,-7,-1,-6,-8,8,-3,-1,5,4,1,-9,-8,-6,3,10,-9,-10,-7,3,1,5,10,-10,-2,-1,10,3,-10,2,2,-5,-10,9,-3,-1,6,2,-4,3,9,-8,-5,-8,-1,-8,-4,-3,-10,-10,-7,-9,8,8,-4,-7,-4,-5,-7,6,5,10,7,-4,8,-9,-8,7,-10,6,-6,10,-8,-3,-9,-3,-2,-6,6,5,-5,-8,-3,-8,10,8,9,-9,4,-3,8,-7,-9,-9,-10,-1,-1,7,4,10,1,3,7,-6,2,1,-3,10,9,1,6,-8,10,4,3,1,1,2,4,6,-5,-5,5,-4,-7,-6,6,-1,-1,4,6,-6,9,-4,7,-10,6,3,-3,6,4,4,-7,-10,-1,-2,10,-5,-7,-4,8,7,3,3,-8,7,-2,4,7,8,6,6,-8,-7,-9,-1,8,1,7,7,-5,-9,-7,-6,5,-4,-4,9,3,-10,10,9,7,-9,-6,-4,-1,7,6,-2,-1,-3,9,8,-9,-4,8,-9,5,-3,-2,-3,-10,3,-6,-4,-3,2,9,2,10,9,1,-7,3,9,-7,-2,-5,-10,10,-9,-2,-3,-5,-1,2,5,7,4,-1,7,7,2,4,2,7,5,4,-10,-4,4,-2,-3,-10,-9,10,-7,-7,7,-3,5,2,-9,7,-5,-2,-9,7,-3,9,-6,-2,-5,3,2,5,-6,-7,-5,-6,-7,1,-5,10,-5,-2,7,7,-2,-6,-6,2,-7,-9,-3,-3,5,8,4,6,6,-4,1,-7,-2,7,-3,2,-6,-2,-7,-9,1,-10,7,6,-5,8,-4,7,7,5,-3,-8,9,-7,-5,1,-6,-2,-9,6,-1,-10,-7,-10,-2,-4,2,-3,-2,-9,9,-4,1,7,4,-5,-8,-1,-1,1,4,8,7,-8,2,-7,-9,5,7,-9,-7,-8,-9,-4,-10,6,2,3,-5,-10,10,7,8,-9,-6,-8,5,10,4,6,8,-9,8,-2,3,-10,-9,2,1,-4,2,-9,-7,10,-2,-7,-10,3,-10,-1,-8,8,9,7,-5,-6,3,3,4,-1,-2,1,7,-8,-10,2,1,5,1,-10,3,3,-3,5,-2,6,-7,5,-10,10,1,7,-1,-2,6,-1,9,-6,10,10,10,-5,-2,10,1,-1,4,-6,2,-1,1,-9,6,1,-7,-8,-6,3,-1,-9,4,9,-9,5,3,2,-6,4,-6,-7,-7,-9,8,-10,-6,-3,8,8,-5,1,-7,-3,3,6,-2,2,8,2,-7,4,1,4,7,9,5,1,-4,-8,2,8,-6,5,6,-7,10,-6,7,2,-2,-8,-4,10,5,-7,-1,-5,7,-9,9,-6,9,2,2,2,7,-10,2,9,7,8,-10,2,-3,2,9,1,-2,4,8,-7,-9,-6,-6,-8,-2,10,9,1,5,2,-5,-3,-7,-10,-4,-10,3,-4,2,1,-8,5,-5,9,-2,-5,5,4,5,-7,-1,4,4,3,9,1,5,7,2,9,9,3,-1,8,-10,-7,-5,-7,8,-6,-1,8,-2,-5,1,10,-9,-5,-9,6,-1,4,-5,-4,8,4,8,-7,-7,5,-6,1,10,-6,1,10,-7,8,5,7,-4,5,4,-10,-4,-10,-2,8,7,10,-5,9,-9,6,-9,-9,5,-2,-8,10,9,-6,1,4,-7,-7,7,6,5,9,-6,-6,6,10,4,8,9,6,-8,-9,5,9,4,-9,9,4,8,-6,9,8,5,-9,-10,4,7,2,1,-5,7,5,-4,1,8,8,-5,-1,2,5,-6,9,4,5,-3,2,6,5,-6,-4,6,-2,-8,-1,4,2,7,-3,-3,6,-1,-5,6,7,-8,6,10,-7,2,9,-6,-8,-2,-1,1,10,-8,7,7,-5,4,1,9,4,-7,-9,-4,3,-2,-3,-6,5,10,-5,5,-1,1,-2,-1,-2,-9,-1,-2,3,3,-6,-10,10,-2,-6,6,5,1,-8,6,-3,4,10,-2,-9,8,3,-6,-10,9,5,-5,-3,-10,3,2,2,1,2,-4,8,6,-2,4,1,9,-9,8,5,2,5,3,9,-9,7,10,7,-7,-10,-2,4,-9,-8,-4,5,8,-9,-7,-6,7,-2,-1,7,-10,10,-10,-5,-7,7,3,-9,-4,-3,7,7,-3,5,8,3,-8,1,-5,-8,9,-6,-9,-5,-3,4,-10,-6,-10,8,-2,5,1,-2,2,3,-7,-4,-3,-1,-9,-8,6,3,-6,3,1,-10,3,3,3,-7,-4,-9,9,-5,3,-7,-9,4,-3,-5,-6,-1,8,4,-9,-2,-1,-9,-8,-9,10,-1,-8,6,3,-8,-10,-10,2,-10,7,3,4,6,-10,5,3,-1,-3,2,10,-7,-10,9,-10,-4,-4,3,-3,-1,6,-3,4,-9,2,-4,-3,5,7,9,4,4,-2,-5,10,8,-2,4], dtype = "uint32")#candidate|7134|(2016,)|const|uint32
call_7132 = relay.TupleGetItem(func_2955_call(relay.reshape(const_7133.astype('float64'), [4,]), relay.reshape(const_7134.astype('uint32'), [2016,]), ), 0)
call_7135 = relay.TupleGetItem(func_2958_call(relay.reshape(const_7133.astype('float64'), [4,]), relay.reshape(const_7134.astype('uint32'), [2016,]), ), 0)
output = relay.Tuple([uop_7109,call_7119,var_7120,var_7121,uop_7125,call_7132,const_7133,const_7134,])
output2 = relay.Tuple([uop_7111,call_7122,var_7120,var_7121,uop_7127,call_7135,const_7133,const_7134,])
func_7141 = relay.Function([var_7120,var_7121,], output)
mod['func_7141'] = func_7141
mod = relay.transform.InferType()(mod)
mutated_mod['func_7141'] = func_7141
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7141_call = mutated_mod.get_global_var('func_7141')
var_7143 = relay.var("var_7143", dtype = "bool", shape = ())#candidate|7143|()|var|bool
var_7144 = relay.var("var_7144", dtype = "bool", shape = (363,))#candidate|7144|(363,)|var|bool
call_7142 = func_7141_call(var_7143,var_7144,)
output = call_7142
func_7145 = relay.Function([var_7143,var_7144,], output)
mutated_mod['func_7145'] = func_7145
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3081_call = mod.get_global_var('func_3081')
func_3083_call = mutated_mod.get_global_var('func_3083')
call_7198 = relay.TupleGetItem(func_3081_call(), 0)
call_7199 = relay.TupleGetItem(func_3083_call(), 0)
func_6119_call = mod.get_global_var('func_6119')
func_6121_call = mutated_mod.get_global_var('func_6121')
call_7216 = relay.TupleGetItem(func_6119_call(), 0)
call_7217 = relay.TupleGetItem(func_6121_call(), 0)
output = relay.Tuple([call_7198,call_7216,])
output2 = relay.Tuple([call_7199,call_7217,])
func_7246 = relay.Function([], output)
mod['func_7246'] = func_7246
mod = relay.transform.InferType()(mod)
output = func_7246()
func_7247 = relay.Function([], output)
mutated_mod['func_7247'] = func_7247
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4283_call = mod.get_global_var('func_4283')
func_4284_call = mutated_mod.get_global_var('func_4284')
call_7323 = relay.TupleGetItem(func_4283_call(), 0)
call_7324 = relay.TupleGetItem(func_4284_call(), 0)
func_2955_call = mod.get_global_var('func_2955')
func_2958_call = mutated_mod.get_global_var('func_2958')
const_7332 = relay.const([8.902173,-7.630002,4.501630,-4.944781], dtype = "float64")#candidate|7332|(4,)|const|float64
const_7333 = relay.const([-5,-5,1,8,-7,-5,10,2,1,-2,-4,-5,2,-8,-5,7,-5,-2,2,-10,-9,-4,8,-10,3,-3,2,2,7,10,-2,-9,-9,-1,-1,2,7,-10,3,3,1,-6,5,-8,7,-2,4,6,-4,-4,10,-8,1,10,-7,1,9,10,5,-6,-3,1,-4,1,-4,5,-3,10,1,10,-5,4,8,9,2,-6,-6,4,-4,9,2,-3,-7,10,5,5,-3,-3,3,-2,7,-9,5,-4,8,8,-9,6,-3,3,-8,-5,9,2,2,-6,4,-4,9,-9,-3,-1,-7,8,5,6,-2,-6,3,-3,-2,3,-6,-4,-7,4,-9,10,-1,-5,-2,2,4,-4,-8,9,6,5,-9,9,-3,5,7,7,6,6,3,-9,-10,3,10,7,5,9,4,-3,-8,-8,-6,7,-8,-7,3,-9,10,10,-7,-7,-10,10,2,-8,10,7,4,7,7,3,1,-4,6,-1,2,7,4,-3,-9,-7,8,6,-10,-3,8,-10,10,9,9,-10,10,2,-5,10,-5,-6,3,-4,-6,1,-5,-2,-6,-2,1,-7,-1,6,-1,3,-3,8,10,10,-10,-9,-3,-1,-2,-5,7,5,-8,-6,-7,-4,8,8,-3,6,-1,-8,6,5,-2,-2,-10,-7,-7,-7,1,-7,-3,-7,-5,-10,7,-3,7,10,8,-8,-8,9,9,-2,-7,-9,5,-9,-10,1,6,10,-3,5,-4,-2,-10,-2,8,1,-4,-8,-8,-1,5,-6,7,-8,-8,-4,6,7,-8,6,2,3,-8,6,9,4,1,-7,-6,9,-8,6,-8,1,-1,-3,-2,10,-7,-8,6,-10,-10,5,2,9,6,3,10,1,-8,-6,-9,2,3,-4,-2,5,-1,-9,2,-2,-5,2,8,-7,-8,-1,-9,4,-3,-2,5,8,-6,1,-4,6,-10,5,4,6,-4,10,10,-5,4,-9,-5,-7,5,-8,-2,8,-5,-8,4,-2,1,-10,-5,5,4,-10,-4,-9,4,-7,4,-8,10,-9,-2,-1,-2,-5,9,10,-5,-4,9,7,1,-10,9,3,6,4,-4,10,-7,4,-4,-9,7,7,7,9,-7,-4,-9,-8,10,10,6,-1,-4,8,1,8,-1,2,-10,-7,-2,-5,-7,-3,-2,2,-6,10,-9,-9,-6,-8,3,-4,-3,-1,-3,5,7,8,4,9,4,-9,8,5,6,-10,7,1,8,-4,-8,10,8,9,9,-1,9,-7,-7,-2,6,-1,7,-3,-6,3,-8,3,2,-10,-10,-3,-1,8,3,-1,2,-1,6,4,-3,-7,-2,8,2,7,1,1,-2,-9,6,3,-4,7,-8,-3,1,-3,10,-9,1,2,-5,3,-1,2,2,7,10,5,8,3,8,2,-9,-10,-6,4,7,-1,-10,8,-8,10,-1,-10,-5,-6,-10,10,-9,2,3,7,5,-10,10,-1,-3,10,7,2,-2,-4,-9,2,7,3,1,-1,9,3,7,10,4,5,2,3,8,-8,2,-2,5,-10,-5,-5,2,6,4,1,-5,-9,-6,3,-10,10,1,2,7,-4,-2,-9,-9,-4,-10,-2,3,-4,-4,2,5,5,-4,-4,10,7,7,6,2,10,5,1,-3,-7,-1,10,-3,-4,3,-9,-5,5,-4,-9,-1,10,-3,5,5,3,-5,4,8,-2,-7,6,-7,4,-1,8,4,-9,-7,2,-10,-10,8,10,3,6,5,1,-2,5,-10,5,-1,2,1,-1,-1,-6,4,-2,8,-4,2,6,2,7,-4,-7,-1,4,5,4,6,-2,6,7,5,-8,9,-3,5,5,4,-6,-5,8,-8,5,-2,6,4,-1,-7,8,-3,8,-10,-1,9,1,8,3,2,1,8,10,-1,10,10,-5,-6,-2,8,-1,1,-10,-1,-6,-2,5,-2,-1,-5,-2,-9,-7,10,3,5,6,6,-6,10,8,-6,-1,9,5,4,-7,2,10,-5,1,-5,-5,-2,7,-10,-3,1,9,7,2,-1,4,6,7,-7,1,-3,4,-7,7,-8,-8,-6,9,-2,7,-3,-9,7,10,4,5,-10,-5,9,-8,2,-8,-2,-6,-9,8,-5,10,-2,-7,4,4,-2,2,-10,-10,6,-3,-8,-5,-3,10,-1,-4,-1,-9,-5,-10,1,8,-4,-4,-10,-1,7,5,10,-1,-6,-5,-6,-3,-7,-5,8,-8,4,5,10,-10,5,-8,-1,-7,2,5,6,8,-2,10,6,4,-9,-4,6,-5,-9,5,1,-8,-4,2,10,3,-3,-4,10,-1,-7,-9,8,6,-8,9,5,-2,-10,-10,4,-6,6,-10,-8,-5,-7,-9,-10,-2,8,-8,1,-3,-6,-3,6,-9,-9,-9,1,3,-10,-1,-9,-9,-6,-1,6,-8,-9,-3,10,9,3,6,4,2,-2,-6,-7,8,-1,2,5,10,-1,-10,8,-10,-9,-5,-4,9,-1,6,10,-3,5,8,5,3,-2,-9,-4,1,5,-8,-4,-6,-4,3,8,-4,-3,-2,-2,-6,-8,5,4,-5,2,8,10,1,10,-9,1,-1,8,3,-8,2,-2,10,-3,-2,6,-10,-8,2,4,6,5,-10,-3,-10,-1,-9,-1,8,-3,10,-2,8,1,8,1,3,-3,8,-7,9,3,9,-8,-10,7,10,10,3,-10,-1,7,7,-8,-6,-3,2,-4,2,10,-2,-3,8,4,7,4,-5,1,-1,-6,5,-3,-7,-8,10,4,4,-8,-1,6,4,-5,1,2,-6,-10,-10,-7,-1,-10,4,-4,-9,5,-3,-9,2,-10,3,-4,2,1,-8,-1,-7,3,2,2,-10,-5,-9,-3,-10,4,5,-2,4,9,4,-5,8,2,5,-3,-10,-7,-5,-10,3,8,-3,-3,6,1,1,-8,-3,-10,4,-3,-4,-3,-1,3,8,10,-2,8,-8,-7,-6,9,-5,8,-4,4,-3,8,4,8,3,-1,2,4,-10,-8,-5,-8,7,10,8,1,2,5,-1,8,-10,10,10,-1,-2,-9,-7,-7,-2,6,-2,-1,-6,-2,9,2,9,-1,-5,-9,3,-6,-4,3,-2,8,-5,10,-7,-10,-2,-4,-6,10,-7,-10,7,-1,1,-9,-2,-8,-7,-10,-3,-1,-5,-4,1,-2,-2,-1,8,-2,-7,-3,9,7,2,-2,-10,-7,-9,-7,4,-1,2,5,-3,1,1,8,-5,-8,2,1,-5,8,9,4,-5,-10,-6,-10,-4,-8,5,5,-1,-9,2,-7,-8,1,-2,-1,-10,5,5,-5,-8,-4,-9,5,1,-4,-5,10,-8,1,5,-7,2,-9,9,6,6,-2,-8,-2,-2,9,-7,-1,9,-5,3,-9,3,-1,-3,2,6,4,-1,-10,5,10,-10,7,10,-4,-3,7,-5,10,3,7,6,-3,10,-9,3,-6,-10,-2,4,-3,-3,5,-9,5,-7,-3,-4,1,10,-8,9,5,7,-10,-5,8,-5,5,-9,8,-5,-8,-9,-2,9,3,-3,9,-8,-1,-4,-3,3,5,-8,-8,7,-1,-7,7,-4,5,-9,-7,3,-1,6,-8,-4,1,-7,5,4,-2,3,-6,8,-6,6,-5,1,8,2,6,-10,-7,5,4,-2,-2,-4,1,2,10,-1,8,4,9,3,-1,-4,3,2,3,-2,8,3,-9,-9,2,-5,-1,-6,5,8,6,6,-5,7,-2,-1,8,-2,-9,-5,10,-1,10,-3,-9,-5,-7,6,-9,10,-5,-4,6,-9,4,6,-5,4,6,-4,-10,-2,10,-9,-3,2,9,-1,9,-10,4,-8,-2,-6,-2,3,-1,-9,3,2,6,-3,10,-7,-4,4,2,-6,-6,3,7,4,-3,9,-2,1,2,2,-10,3,-8,9,-10,-4,-1,6,5,4,-4,3,3,-3,-9,-7,4,2,-6,1,10,-4,-4,-7,-2,-8,-5,10,6,2,-8,4,-8,3,-9,-2,10,8,-6,-5,-7,3,-6,9,-8,-5,10,8,10,-4,6,8,1,9,2,-6,-1,-2,-5,6,1,-10,5,-1,-9,-1,-2,-10,6,2,7,8,8,2,-10,7,-10,-2,-6,7,7,-10,-9,-4,2,-3,-6,5,-1,-9,5,-4,-4,-9,1,-8,6,-9,-10,7,9,-9,3,10,10,6,-7,10,9,4,7,-8,9,7,-10,-1,6,-5,5,2,-5,3,-9,3,-4,5,6,4,1,-7,6,2,-8,-1,-2,-8,-1,9,6,5,-9,-1,6,-4,-5,-9,-7,-2,-10,7,6,-1,8,5,3,4,-4,9,-8,-8,2,-3,10,5,10,2,-7,1,4,-9,-9,9,6,3,2,9,3,-4,-9,5,-1,5,1,-3,-3,-9,3,-4,-7,5,10,-3,5,-8,-8,-6,-9,7,5,2,-2,10,1,6,-1,-9,-4,6,4,8,6,-9,2,-2,5,7,-6,-3,-1,9,2,6,2,7,-7,-8,-8,-7,-2,-9,4,-4,-5,9,8,7,-6,5,-5,4,9,5,8,10,-1,-6,-7,5,-9,-7,10,8,6,-4,8,-5,9,-6,1,6,5,7,6,3,6,-4,-3,-4,6,10,-7,10,-4,-4,2,-9,4,8,-7,5,8,-2,2,10,4,-1,-4,9,-9,4,-3,-6,-8,6,5,1,-3,-4,8,2,-3,-3,5,-6,-4,-4,5,3,6,1,3,7,-6,10,5,6,-4,-7,-2,1,-7,-5,9,-8,-9,8,-2,7,-8,-1,-10,10,-9,-3,2,-9,1,1,-1,-6,-7,-2,1,-8,10,-1,8,4,-2,10,-1,3,4,3,-5,6,7,-3,-9,9,-2,-10,4,10,9,10,-1,-1,8,-8,6,7,2,-2,-10,-2,1,-3,-4,-1,-2,-2,-5,-6,8,8,-8,7,-2,2,-2,-4,-4,10,-9,10,3,4,6,10,4,8,-2,3,-6,10,1,10,3,5,10,-3,9,10,-9,-1,-10,-6,-6,10,6,-9,-4,-6,9,-8,9,2,1,5,-4,-3,-7,-9,-8,4,-9,-4,-2,-7,-2,-9,-6,-10,5,-9,2,-5,10,2,3,3,9,-2,-8,1,3,2,1,10,-7,-4,10,-10,3,10,7,7,-1,-6,-9,-10,9,6,1,-7,-5,-9,-2,7,10,3,-1,3,1,-10,8,-5,-1,8,-6,-2,8,10,-10,-5,-4,-8,-9,6,10,-10,-7,7,5,10,2,6,3,2,-3,-6,5,4,2,-4,8,-5,1,3,-9,9,6,3,-3,5,-2,-5,-4,3,-8,10,-2,-1,9,9,10,1,-3,-5,1,-4,-2,2,-7,2,1,-1,7,6,-9,-5,-2,3,5,4,2,1,-7,8,7,1,-1,2], dtype = "uint32")#candidate|7333|(2016,)|const|uint32
call_7331 = relay.TupleGetItem(func_2955_call(relay.reshape(const_7332.astype('float64'), [4,]), relay.reshape(const_7333.astype('uint32'), [2016,]), ), 2)
call_7334 = relay.TupleGetItem(func_2958_call(relay.reshape(const_7332.astype('float64'), [4,]), relay.reshape(const_7333.astype('uint32'), [2016,]), ), 2)
var_7339 = relay.var("var_7339", dtype = "float32", shape = (520,))#candidate|7339|(520,)|var|float32
bop_7340 = relay.floor_mod(call_7323.astype('float64'), relay.reshape(var_7339.astype('float64'), relay.shape_of(call_7323))) # shape=(520,)
bop_7343 = relay.floor_mod(call_7324.astype('float64'), relay.reshape(var_7339.astype('float64'), relay.shape_of(call_7324))) # shape=(520,)
output = relay.Tuple([call_7331,const_7332,const_7333,bop_7340,])
output2 = relay.Tuple([call_7334,const_7332,const_7333,bop_7343,])
F = relay.Function([var_7339,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_7339,], output2)
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
